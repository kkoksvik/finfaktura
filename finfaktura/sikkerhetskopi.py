#!/usr/bin/python -d
# -*- coding:utf8 -*-
###########################################################################
#    Copyright (C) 2006 - Håvard Dahle
#    <havard@dahle.no>
#
#    Lisens: GPL2
#
# $Id$
###########################################################################

import sys,types

try:
    import libgmail
    BRUK_GMAIL=True
except ImportError:
    BRUK_GMAIL=False

class IkkeImplementert(Exception): pass
class Utilgjengelig(Exception): pass
class SikkerhetskopieringFeilet(Exception): pass

class sikkerhetskopi:
    metode = None
    data = None
    
    def __init__(self, obj, label=None):
        if label is not None: self.label=label
        if type(obj) in (types.StringType, types.UnicodeType):
            self.data = obj
        else: #er en fil
            self.data = obj.read()
        #self.fil  = self._f()
        
    def lagre(self): #skal subklasses av hver implementasjon
        raise IkkeImplementert(u"Metoden er ikke implementert for modulen!")
    
    def tilgjengeligeMetoder(self):
        metoder = {'gmail':BRUK_GMAIL,
                   'fil':True,
        }
        return [z for z in metoder.keys() if metoder[z]] # XXX:Dette er lite elegant
        
    def _z(self, data):
        try: 
            import bz2
            return 'bz2', bz2.compress(data)
        except ImportError: #bz2 finnes ikke < python 2.3
            import gzip
            raise
            # from StringIO import StringIO
            # s = StriogIO(data)
            # gz = GzipFile(mode='wb', fileobj=s)
            # return 'gzip', s.getvalue()
       #return '', data
            
    def _x(self, fil):
        metode = os.path.splitext(fil)[1]
        if metode == 'bz2':
            try:
                import bz2
                return bz2.decompress(open(fil).read())
            except ImportError:
                raise
        elif metode == 'gzip':
            try:
                import gzip
                return gzip.balbb
            except: raise
        
            
    def _f(self):
        "returnerer et filnavn med self.data i"
        if not self.data: return None
        from tempfile import mkstemp
        import time
        metode, data = self._z(self.data)
        if not metode:
            etternavn = '.db'
        else:
            etternavn = '.'+metode
        f,filnavn = mkstemp(etternavn, "faktura-%s-" % time.strftime('%Y-%m-%d'))
        fl = file(filnavn, "wb")
        fl.write(data)
        fl.close()
        return filnavn
        
            
class gmailkopi(sikkerhetskopi):
    label = "Fakturatest"
    brukelig = False
    
    def __init__(self, obj, brukernavn, passord, label=None):
        if not BRUK_GMAIL:
            raise Utilgjengelig(u'Gmail er ikke tilgjengelig. Har du installert libgmail?')
        self.brukelig = True
        
        #print "Bruker libgmail, versjon:",libgmail.Version
        self.brukernavn = brukernavn
        self.passord = passord
        sikkerhetskopi.__init__(self, obj, label)
        
    def lagre(self):
        #user,cred = file("/home/havard/.gmailpass").read().strip().split(",")

        gmail = libgmail.GmailAccount(self.brukernavn, self.passord)
        print "Logger inn i Gmail med brukernavn %s" % self.brukernavn
        gmail.login()
        fil = self._f()
        print "Logget inn. Laster opp fil:", fil
        try:
            return gmail.storeFile(fil, label=self.label)
        except:
            raise SikkerhetskopieringFeilet(u'Sikkerhetskopiering til Gmail som %s feilet!' % self.brukernavn)

class filkopi(sikkerhetskopi):
    label = "Faktura"
    brukelig = False
    
    def __init__(self, obj, hvor, label=None):
        self.brukelig = True
        self.hvor = hvor
        sikkerhetskopi.__init__(self, obj, label)
        
    def lagre(self):
        import os
        fra = self._f()
        nyttnavn = os.path.basename(fra)
        if self.label: nyttnavn = self.label + ":" + nyttnavn
        print "sikkerhetskopierer fra %s til %s" % (fra, self.hvor+"/"+nyttnavn)
        try:
            os.rename(fra, self.hvor+"/"+nyttnavn)
            return True
        except OSError:
            return False

if __name__ == '__main__':
    #test
    cx = "/home/havard/dev/faktura/faktura.db"
    user,cred = file("/home/havard/.gmailpass").read().strip().split(",")
    g = gmailkopi(file(cx), user, cred)
    #g = filkopi(file(cx), "/tmp/", "Test")
    if g.lagre():
        print "Finfint. Sikkerhetskopi lagert på gmail"
    else:
        print "Fillern. Sikkerhetskopi på gmail feilet!"
    
