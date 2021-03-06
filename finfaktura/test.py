#!/usr/bin/python -d
# -*-*- coding:utf8 -*-*-
###########################################################################
#    Copyright (C) 2005-2009 Håvard Gulldahl
#    <havard@lurtgjort.no>
#
#    Lisens: GPL2
#
# $Id$
###########################################################################

import types, os, sys, os.path
from string import join
from time import time, strftime, localtime
try:
    import sqlite3 as sqlite
except ImportError:
    from pysqlite2 import dbapi2 as sqlite
from pprint import pprint
from fakturabibliotek import *

if __name__ == "__main__":
    #test biblioteket
    import sys
    test = sys.argv[1:]
    if sys.argv[1] in ("hjelp", '-h', '-help', '--help'):
        from os import execl
        execl("/bin/grep", "grep", "in test:", sys.argv[0])

    cx = sqlite.connect(finnDatabasenavn())
    if "kunde" in test:
        kunde = fakturaKunde(cx)
        kunde.navn = u"Havard Gulldahl"
        kunde.epost = "havard@lurtgjort.no"
        print "kunde:", kunde
    if "hentkunder" in test:
        b = FakturaBibliotek(cx)
        pprint(b.hentKunder())
    if "vare" in test:
        v = fakturaVare(cx)
        v.navn = "2-sider Linuxmagasinet"
        v.detaljer = "Tekst som går over to sider"
        v.enhet = "stk"
        v.pris = "2500"
        print "vare:", v
    if "nyfaktura" in test:
        _kunde = fakturaKunde(cx, 1)
        _firma = fakturaFirmainfo(cx)
        f = fakturaOrdre(cx, kunde=_kunde, firma=_firma)
        f.tekst = u"råtøff vask"
        v = fakturaVare(cx, 1)
        f.leggTilVare(v, 4, 2500, 12)
        #v2 = fakturaVare(cx, 3)
        #f.leggTilVare(v2, 1, 2000, 24)
        #print "faktura:", f
        b = FakturaBibliotek(cx)
        pdf = b.lagPDF(f, "epost")
        print "pdf:",pdf.filnavn
    if "pdf" in test:
        _firma = fakturaFirmainfo(cx)
        f = fakturaOrdre(cx, Id=3, firma=_firma)
        b = FakturaBibliotek(cx)
        pdf = b.lagPDF(f, "epost")
        print "pdf:",pdf.filnavn
        
    if "hentordrer" in test:
        b = FakturaBibliotek(cx)
        for z in b.hentOrdrer():
            print z
    if "firma" in test:
        f = fakturaFirmainfo(cx)
        print f.__str__()
        print f.firmanavn
    
    if "oppdater" in test:
        f = fakturaFirmainfo(cx)
        f.firmanavn=u'Hålåxx'
        print f.firmanavn
    
    if "firmalogo" in test:
        f = fakturaFirmainfo(cx)
        print "firmalogo:",type(f.logo)
        #out = file("/tmp/firmalogo.gif", "w")
        #out.write(f.logo)
        #out.close()

    if "database" in test:
        b = FakturaBibliotek(cx)
    if "lagdatabase" in test:
        dbnavn = finnDatabasenavn()
        print "lager db:", dbnavn
        db = lagDatabase(dbnavn)
        b = FakturaBibliotek(db)
        print b
    if "hentsikkerhetskopier" in test:
        b = FakturaBibliotek(cx)
        for kopi in b.hentSikkerhetskopier():
            if kopi.data is None:
                print "ordre# %s har ingen sikkerhetskopi!" % kopi.ordreID
                continue
            fil = "/tmp/sikk.%s.%s.pdf" % (kopi.dato, kopi.ordreID)
            f = file(fil, "w")
            f.write(kopi.data)
            f.close()
            print "sikkerhetskopi#%i av faktura # %s dumpet til %s" % (kopi._id, kopi.ordreID, fil)
    if "epost" in test:
        _firma = fakturaFirmainfo(cx)
        f = fakturaOrdre(cx, Id=1, firma=_firma)
        b = FakturaBibliotek(cx)
        pdf = b.lagPDF(f, "epost")
        print "pdf:",pdf.filnavn
        import epost
        for metode in ('dump', 'sendmail', 'smtp', 'gmail'):
            m = getattr(epost, metode)()
            m.faktura(f, pdf.filnavn)
            print 'tester %s' % metode
            print m.test()
            print 'sender %s' % metode
            #print m.send()
        
        
    if "dbtest" in test:
        print "tester om %s er en sqlite-database" % sys.argv[2]
        print sjekkDatabaseVersjon(sys.argv[2])

    if "kid" in test:
        print "tester kid-funksjoner i f60"
        import f60
        f = f60.f60(filnavn=None)
        kid = "001234000123"
        sjekksum = f.lagSjekksum(kid)
        fullKid = kid+str(sjekksum)
        print "sjekksum: %s, fullKid: %s" % (sjekksum, fullKid)
        print "full KID (%s) stemmer: %s" % (fullKid, f.sjekkKid(fullKid))

        fullKid2 = "0257270170026"
        print "fullKid2 (%s) stemmer: %s" % (fullKid2, f.sjekkKid(fullKid2))
        print f.lagSjekksum("12464533060099620")

    cx.close()
