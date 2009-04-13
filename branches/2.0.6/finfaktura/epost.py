#!/usr/bin/env python
# -*- coding:utf8 -*-
###########################################################################
#    Copyright (C) 2005-2009 Håvard Gulldahl
#    <havard@lurtgjort.no>
#
#    Lisens: GPL2
#
# $Id$
###########################################################################

import sys, types, os, os.path, logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders, generator
from email.header import Header, decode_header
from email.utils import parseaddr
import email.iterators
import socket
from string import join

TRANSPORTMETODER = ['auto', 'smtp', 'sendmail']

class SendeFeil(Exception): pass
class UgyldigVerdi(Exception): pass
class IkkeImplementert(Exception): pass

class epost:

    charset='iso-8859-15' # epostens tegnsett
    kopi = None
    brukernavn = None
    passord = None
    testmelding = True
    vedlegg = []

    def faktura(self, ordre, pdfFilnavn, tekst=None, fra=None, testmelding=False):
        if not type(pdfFilnavn) in types.StringTypes:
            raise UgyldigVerdi(u'pdfFilnavn skal være tekst (ikke "%s")' % type(pdfFilnavn))
        self.ordre = ordre
        self.pdfFilnavn = pdfFilnavn
        if fra is None: fra = ordre.firma.epost
        self.fra = fra
        self.til = ordre.kunde.epost
        self.tittel = u"Epostfaktura fra %s: '%s' (#%i)" % (ordre.firma.firmanavn, self.kutt(ordre.tekst), ordre.ID)
        if tekst is None: tekst = u'Vedlagt følger epostfaktura #%i:\n\n%s\n\n-- \n%s\n%s' % (ordre.ID, ordre.tekst,  ordre.firma, ordre.firma.vilkar)
        self.tekst = tekst
        self.testmelding = testmelding
        if self.testmelding: # vi er i utviklingsmodus, skift tittel
            self.tittel = u"TESTFAKTURA "+self.tittel

    def mimemelding(self):
        m = MIMEMultipart()
        m['Subject'] = Header(self.tittel, self.charset)
        n = self.ordre.firma.firmanavn.replace(';', ' ').replace(',',' ')
        m['From'] = '"%s" <%s>' % (Header(n, self.charset), self.fra)
        #m['To'] = '"%s" <%s>' % (Header(self.ordre.kunde.navn, self.charset), self.til)
        m['To'] = self.til #'"%s" <%s>' % (Header(self.ordre.kunde.navn, self.charset), self.til)
        m.preamble = 'You will not see this in a MIME-aware mail reader.\n'
        # To guarantee the message ends with a newline
        m.epilogue = ''

        # Legg til tekstlig informasjon
        t = MIMEText(self.tekst.encode(self.charset), 'plain', self.charset)
        m.attach(t)

        # Legg til fakturaen
        b = MIMEBase('application', 'x-pdf')
        _filename=Header('%s-%i.pdf' % (self.ordre.firma.firmanavn, self.ordre.ID), self.charset)
        b.add_header('Content-Disposition', 'attachment', filename=_filename.encode()) # legg til filnavn
        m.attach(b)
        fp = open(self.pdfFilnavn, 'rb')
        b.set_payload(fp.read()) # les inn fakturaen
        fp.close()
        encoders.encode_base64(b) #base64 encode subpart

        # Legg til vedlegg
        for filnavn, vedlegg in self.vedlegg:
            v = MIMEBase('application', 'octet-stream')
            _filename=Header(filnavn, self.charset)
            v.add_header('Content-Disposition', 'attachment', filename=_filename.encode()) # legg til filnavn
            m.attach(v)
            v.set_payload(vedlegg) 
            encoders.encode_base64(v) #base64 encode subpart

        return m

    def auth(self, brukernavn, passord):
        if not type(brukernavn) in types.StringTypes:
            raise UgyldigVerdi(u'Brukernavn skal være tekst (ikke "%s")' % type(brukernavn))
        if not type(passord) in types.StringTypes:
            raise UgyldigVerdi(u'Passord skal være tekst (ikke "%s")' % type(passord))
        self._auth = True
        self.brukernavn = brukernavn
        self.passord = passord

    def send(self): pass

    def test(self): pass

    def kutt(self, s, l=30):
        assert(type(s) in types.StringTypes)
        if len(s) < l: return s
        return s[0:l] + "..."

    def settKopi(self, s):
        # setter BCC-kopi til s
        if not type(s) in types.StringTypes:
            raise UgyldigVerdi(u'Epostadresse skal være tekst (ikke "%s")' % type(s))
        # sjekk at s er en gyldig epostadresse
        if not '@' in s:
            raise UgyldigVerdi(u'Denne epostadressen er ikke gyldig: %s' % s)
        self.kopi = s

    def nyttVedlegg(self, f):
        "Legg til vedlegg. `f' kan være et filnavn eller et file()-objekt"
        if os.path.exists(f):
            _f = open(f, 'rb')
            self.vedlegg.append((f, _f.read()))
            _f.close()
            return True
        elif hasattr(f, 'read'):
            self.vedlegg.append(('noname', f.read()))
            return True
        else:
            return False
            
class smtp(epost):
    smtpserver='localhost'
    smtpport=25
    _tls = False
    _auth = False

    def settServer(self, smtpserver, port=25):
        if not type(smtpserver) in types.StringTypes:
            raise UgyldigVerdi(u'smtpserver skal være tekst (ikke "%s")' % type(smtpserver))
        if not type(port) == types.IntType:
            raise UgyldigVerdi(u'port skal være et heltall (ikke "%s")' % type(port))
        self.smtpserver=unicode(smtpserver)
        self.smtpport=int(port)

    def tls(self, _bool):
        if not type(_bool) == bool:
            raise UgyldigVerdi(u'Verdien skal være True eller False (ikke "%s")' % type(_bool))
        self._tls = _bool

    def test(self):
        s = smtplib.SMTP()
        if self.testmelding: #debug
            s.set_debuglevel(1)
        s.connect(self.smtpserver, self.smtpport)
        s.ehlo()
        if self._tls:
            s.starttls()
            s.ehlo()
        if self._auth:
            s.login(self.brukernavn, self.passord)
        s.close()
        return True

    def send(self):
        s = smtplib.SMTP()
        if self.testmelding: #debug
            s.set_debuglevel(1)
        try:
            s.connect(self.smtpserver, self.smtpport)
            s.ehlo()
            if self._tls:
                s.starttls()
                s.ehlo()
            if self._auth:
                s.login(self.brukernavn, self.passord)
        except socket.error,E:
            raise SendeFeil(E)
        except:
            raise
        mottakere = [self.til,]
        if self.kopi: mottakere.append(self.kopi) # sender kopi til oss selv (BCC)
        logging.debug("mottaker: %s", mottakere)
        logging.debug("fra: %s (%s)", self.fra, type(self.fra))
        res = s.sendmail(self.fra, mottakere, self.mimemelding().as_string())
        s.close()
        if len(res) > 0:
            ### Fra help(smtplib):
            # >>> s.sendmail("me@my.org",tolist,msg)
            #|       { "three@three.org" : ( 550 ,"User unknown" ) }
            #|
            #|      In the above example, the message was accepted for delivery to three
            #|      of the four addresses, and one was rejected, with the error code
            #|      550.  If all addresses are accepted, then the method will return an
            #|      empty dictionary.

            feil = [ "%s: %s" % (a, res[a][1]) for a in res.keys() ]
            raise SendeFeil(u'Sendingen feilet for disse adressene:\n%s' % join(feil, '\n'))
        return True

class sendmail(epost):
    bin='/usr/lib/sendmail'
    _auth=False

    def settSti(self, sti):
        if not type(sti) in types.StringTypes:
            raise UgyldigVerdi(u'sti skal være tekst (ikke "%s")' % type(sti))
        self.bin = sti

    def test(self):
        import os.path as p
        real = p.realpath(self.bin)
        logging.debug("fullstendig sti: %s", real)
        if not (p.exists(real) and p.isfile(real)): # er dette tilstrekkelig?
            raise SendeFeil(u'%s er ikke en gyldig sendmail-kommando' % self.bin)
        return True

    def send(self):
        # ssmtp opsjoner:
        #-4     Forces ssmtp to use IPv4 addresses only.
        #-6     Forces ssmtp to use IPv6 addresses only.
        #-auusername
                #Specifies username for SMTP authentication.
        #-appassword
                #Specifies password for SMTP authentication.
        #-ammechanism
                #Specifies mechanism for SMTP authentication. (Only LOGIN and CRAM-MD5)
        # XXX TODO: Hvordan gjøre auth uavhengig av sendmail-implementasjon?
        kmd = "%s %s" % (self.bin, self.til)
        if self.kopi: kmd += " %s" % self.kopi # kopi til oss selv (BCC)
        logging.debug("starter prosess: %s", kmd)
        inn, ut = os.popen4(kmd)
        try:
            inn.write(self.mimemelding().as_string())
            r = inn.close()
        except:
            raise SendeFeil(u'Sendingen feilet fordi:\n' + ut.read())
        #i = inn.close()
        u = ut.close()
        logging.info('sendmail er avsluttet; %s U %s' % (r,u))
        return True

class dump(epost):
    def send(self):
        print self.mimemelding().as_string()
        return True
    def test(self): return self.send()

