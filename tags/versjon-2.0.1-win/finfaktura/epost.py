#!/usr/bin/env python
# -*- coding:utf8 -*-
###########################################################################
#    Copyright (C) 2005-2008- Håvard Gulldahl
#    <havard@lurtgjort.no>
#
#    Lisens: GPL2
#
# $Id$
###########################################################################

import sys,types,os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders, generator
from email.header import Header, decode_header
import email.iterators
import socket
from string import join

TRANSPORTMETODER = ['auto', 'smtp', 'sendmail']

class SendeFeil(Exception): pass
class IkkeImplementert(Exception): pass

class epost:

    charset='iso-8859-15' # epostens tegnsett
    kopi = None
    brukernavn = None
    passord = None
    testmelding = True

    def faktura(self, ordre, pdfFilnavn, tekst=None, fra=None, testmelding=False):
        assert type(pdfFilnavn) in types.StringTypes
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
        return m

    def auth(self, brukernavn, passord):
        assert type(brukernavn) in types.StringTypes
        assert type(passord) in types.StringTypes
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
        assert(type(s) in types.StringTypes)
        # sjekk at s er en gyldig epostadresse
        # XXX TOODO
        self.kopi = s


class smtp(epost):
    smtpserver='localhost'
    smtpport=25
    _tls = False
    _auth = False

    def settServer(self, smtpserver, port=25):
        assert type(smtpserver) in types.StringTypes
        assert type(port) == types.IntType
        self.smtpserver=unicode(smtpserver)
        self.smtpport=int(port)

    def tls(self, bool):
        assert type(bool) == types.BooleanType
        self._tls = bool

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
        print "mottaker:",mottakere
        print "fra:", self.fra, type(self.fra)
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
        assert type(sti) in types.StringTypes
        self.bin = sti

    def test(self):
        import os.path as p
        real = p.realpath(self.bin)
        print real
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
        print kmd
        inn, ut = os.popen4(kmd)
        try:
            inn.write(self.mimemelding().as_string())
            r = inn.close()
        except:
            raise SendeFeil(u'Sendingen feilet fordi:\n' + ut.read())
        #i = inn.close()
        u = ut.close()
        print(u'[epost.py]: sendmail er avsluttet; %s U %s' % (r,u))
        return True

class dump(epost):
    def send(self):
        print self.mimemelding().as_string()
        return True
    def test(self): return self.send()

