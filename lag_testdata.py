#!/usr/bin/python -d
# -*-*- coding:utf8 -*-*-
###########################################################################
#    Copyright (C) 2005-2008- Håvard Gulldahl
#    <havard@lurtgjort.no>
#
#    Lisens: GPL2
#
# $Id: test.py 260 2008-05-11 08:59:23Z havard.gulldahl $
###########################################################################

import types, os, sys, os.path, random
from string import join
from time import time, strftime, localtime
from finfaktura.fakturabibliotek import *

ANTALL_KUNDER=4
ANTALL_VARER=10
ANTALL_ORDRER_PER_KUNDE=3

if __name__ == "__main__":
    #test biblioteket
    import sys
    dbnavn = sys.argv[1]
    from pysqlite2 import dbapi2 as sqlite
    from pprint import pprint
    cx = sqlite.connect(finnDatabasenavn())

    kunder = []
    varer = []
    ordrer = []

    firma = fakturaFirmainfo(cx)
    firma.navn = 'Testefirma'
    firma.kontakt = 'Testekontakt for firma'

    for iv in range(ANTALL_VARER):
      v = fakturaVare(cx)
      v.navn = u'Testvare %i ÆØÅ' % iv
      v.detaljer = u'Denne varen er nr %i av %i' % (iv, ANTALL_VARER)
      v.enhet = 'stk'
      v.pris = random.randint(10, 3000)
      varer.append(v)

    for ik in range(ANTALL_KUNDER):
      k = fakturaKunde(cx)
      k.navn = u'Testkunde %i ÆØÅ' % ik
      k.epost = 'testkunde%i@localhost' % ik
      kunder.append(k)
      for iif in range(ANTALL_ORDRER_PER_KUNDE):
        f = fakturaOrdre(cx, kunde=k, firma=firma)
        f.tekst = u'Testfaktura %i-%i ÆØÅ' % (ik, iif)
        vare = fakturaVare(cx, random.randint(1,ANTALL_VARER))
        f.leggTilVare(vare, random.randint(1,10), vare.pris, 25)



    cx.close()
