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

try:
    import libgmail
    BRUK_GMAIL=True
except ImportError:
    BRUK_GMAIL=False
    

class SendeFeil(Exception): pass
class IkkeImplementert(Exception): pass

class epost:
      
    charset='iso-8859-15' # epostens tegnsett
    kopi = True
    
    def __init__(self, ordre, pdfFilnavn, tekst=None, fra=None, test=False, kopi=True):
        self.ordre = ordre
        self.pdfFilnavn = pdfFilnavn
        if fra is None: fra = ordre.firma.epost
        self.fra = fra 
        self.til = ordre.kunde.epost
        self.tittel = u"Epostfaktura fra %s: '%s' (#%i)" % (ordre.firma.firmanavn, self.kutt(ordre.tekst), ordre.ID)
        if tekst is None: tekst = u'Vedlagt følger epostfaktura #%i:\n\n%s\n\n-- \n%s\n%s' % (ordre.ID, ordre.tekst,  ordre.firma, ordre.firma.vilkar)
        self.tekst = tekst
        self.test = test
        self.kopi = kopi
        
    def mimemelding(self):
        m = MIMEMultipart()
        if self.test: # vi er i utviklingsmodus, skift tittel
            self.tittel = u"TESTFAKTURA "+self.tittel
        m['Subject'] = Header(self.tittel, self.charset)
        m['From'] = '%s <%s>' % (Header(self.ordre.firma.firmanavn, self.charset), Header(self.fra, self.charset).encode())
        if self.kopi:
            m['Bcc'] = '<%s>' % (Header(self.ordre.firma.epost, self.charset))
        m['To'] = '%s <%s>' % (Header(self.ordre.kunde.navn, self.charset), Header(self.til, self.charset).encode())
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
    
    def send(self):
        pass
    
    def kutt(self, s, l=30):
        if len(s) < l: return s
        return s[0:l] + "..."
    
class gmail(epost):
    def auth(self, brukernavn, passord):
        brukernavn, passord = file("/home/havard/.gmailpass").read().strip().split(",")
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
                                                filenames=[self.pdf.filnavn,]
                                                )
            
        except:
            raise u'Sikkerhetskopiering til Gmail som %s feilet!' % brukernavn
        return gmail.sendMessage(msg)
    
class smtp(epost):
    smtpserver='localhost'
    
    def settServer(smtpserver):
        self.smtpserver=smtpserver
    
    def send(self):
        s = smtplib.SMTP()
        try:
            s.connect()
        except socket.error,E:
            raise SendeFeil(E)
        except:
            raise
        res = s.sendmail(self.fra, [self.til], self.mimemelding().as_string())
        s.close()
        if len(res) > 0:
            # >>> s.sendmail("me@my.org",tolist,msg)
            #|       { "three@three.org" : ( 550 ,"User unknown" ) }
            #|
            #|      In the above example, the message was accepted for delivery to three
            #|      of the four addresses, and one was rejected, with the error code
            #|      550.  If all addresses are accepted, then the method will return an
            #|      empty dictionary.

            feil = [ "%s: %s" % (a, res[a][1]) for a in res.keys() ]
            raise Sendefeil(u'Sendingen feilet for følgende adresser:\n%s' % feil.join('\n'))
        return True

class sendmail(epost):
    bin='/usr/lib/sendmail'
    
    def send(self):
        # ssmtp: 
        #-4     Forces ssmtp to use IPv4 addresses only.
    
        #-6     Forces ssmtp to use IPv6 addresses only.
    
        #-auusername
                #Specifies username for SMTP authentication.
    
        #-appassword
                #Specifies password for SMTP authentication.
    
        #-ammechanism
                #Specifies mechanism for SMTP authentication. (Only LOGIN and CRAM-MD5)
        kmd = "%s %s" % (self.bin, self.til)
        inn, ut = os.popen4(kmd)
        try:
            inn.write(self.mimemelding().as_string())
            r = inn.close()
        except:
            raise Sendefeil(u'Sendingen feilet fordi:\n' + ut.read())
        i = inn.close()
        u = ut.close()
        debug(u'sendmail er avsluttet; %s U %s' % (i,u))
        return True

class test(epost):
    def send(self):
        print self.mimemelding().as_string()
        
    def xsend(self):
        f = open('/tmp/eposttest.msg', 'w')
        print "skriver epost til filen /tmp/eposttest.msg"
        f.write(self.mimemelding().as_string())
        f.close()
        print "ferdig"
        