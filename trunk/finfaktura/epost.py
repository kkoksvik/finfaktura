#!/usr/bin/env python
# -*- coding:utf8 -*-
###########################################################################
#    Copyright (C) 2006 - Håvard Dahle 
#    <havard@dahle.no>
#
#    Lisens: GPL2
#
# $Id$
###########################################################################

import sys,types,os 
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
from email.Header import Header, decode_header
import socket
from string import join

transportmetoder = ['smtp', 'sendmail']
try:
    import libgmail
    BRUK_GMAIL=True
    transportmetoder.insert(0, 'gmail') # gmail er foretrukket transportmetode
except ImportError:
    BRUK_GMAIL=False
    

class SendeFeil(Exception): pass
class IkkeImplementert(Exception): pass

class epost:
      
    charset='iso-8859-15' # epostens tegnsett
    kopi = None
    
    def faktura(self, ordre, pdfFilnavn, tekst=None, fra=None, testmelding=False):
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
        m['From'] = '"%s" <%s>' % (Header(self.ordre.firma.firmanavn, self.charset), self.fra) # XXX: TODO: encode self.fra og self.til
        m['To'] = '"%s" <%s>' % (Header(self.ordre.kunde.navn, self.charset), self.til) # Header(self.til, self.charset).encode())
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
        Encoders.encode_base64(b) #base64 encode subpart
        return m
    
    def send(self): pass
    
    def test(self): pass
    
    def kutt(self, s, l=30):
        assert(type(s) in (types.StringType, types.UnicodeType))
        if len(s) < l: return s
        return s[0:l] + "..."
    
    def settKopi(self, s):
        # setter BCC-kopi til s
        assert(type(s) in (types.UnicodeType, types.StringType))
        # sjekk at s er en gyldig epostadresse
        # XXX TOODO
        self.kopi = s
    
class gmail(epost):
    def auth(self, brukernavn, passord):
        self.brukernavn = brukernavn
        self.passord = passord
        
    def send(self):
        gmail = libgmail.GmailAccount(self.brukernavn, self.passord)
        print "Logger inn i Gmail med brukernavn %s" % self.brukernavn
        gmail.login()
        print "Logget inn. Sender til %s" % self.til
        try:
            msg = libgmail.GmailComposedMessage(self.til,
                                                self.tittel.encode('utf-8'),
                                                self.tekst.encode('utf-8'),
                                                filenames=[self.pdfFilnavn,]
                                                )
            
        except:
            raise #u'Epostsending med Gmail som %s feilet!' % self.brukernavn
        return gmail.sendMessage(msg)
    
    def test(self):
        gmail = libgmail.GmailAccount(self.brukernavn, self.passord)
        print "Logger inn i Gmail med brukernavn %s" % self.brukernavn
        gmail.login()
        print "Logget inn."
        return True
        
    
class smtp(epost):
    smtpserver='localhost'
    smtpport=25
    _tls = False
    _auth = False
    
    def settServer(self, smtpserver, port=25):
        self.smtpserver=smtpserver
        self.smtpport=port
    
    def auth(self, brukernavn, passord):
        self._auth = True
        self.brukernavn = brukernavn
        self.passord = passord
    
    def test(self):
        s = smtplib.SMTP()
        s.connect(self.smtpserver, self.smtpport)
        if self._tls: s.starttls()
        if self._auth: s.login(self.brukernavn, self.passord)
        s.close()
        return True
    
    def send(self):
        s = smtplib.SMTP()
        try:
            s.connect(self.smtpserver, self.smtpport)
            if self._tls: s.starttls()
            if self._auth: s.login(self.brukernavn, self.passord)
        except socket.error,E:
            raise SendeFeil(E)
        except:
            raise
        mottakere = [self.til,]
        if self.kopi: mottakere += self.kopi # sender kopi til oss selv (BCC)
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
            raise SendeFeil(u'Sendingen feilet for følgende adresser:\n%s' % join(feil, '\n'))
        return True

class sendmail(epost):
    bin='/usr/lib/sendmail'
    _auth=False
    
    def settSti(self, sti):
        self.bin = sti
    
    def test(self):
        import os.path as p
        real = p.realpath(self.bin)
        if not (p.exists(real) and p.isfile(real)): # er dette tilstrekkelig?
            raise SendeFeil(u'%s er ikke en gyldig sendmail-kommando' % self.bin)
        return True
    
    def auth(self, brukernavn, passord):
        self._auth = True
        self.brukernavn = brukernavn
        self.passord = passord
    
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
        
