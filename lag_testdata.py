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

import types, os, sys, os.path, random, logging
from string import join
from time import time, strftime, localtime
from finfaktura.fakturabibliotek import *

ANTALL_KUNDER=4
ANTALL_VARER=10
ANTALL_ORDRER_PER_KUNDE=3

if __name__ == "__main__":
  logging.basicConfig(level=logging.DEBUG)
  import sys
  dbnavn = sys.argv[1]
  sqlitedb = finnDatabasenavn(dbnavn)
  logging.debug('bruker sqlitedb: %s', os.path.abspath(sqlitedb))
  from pysqlite2 import dbapi2 as sqlite
  from pprint import pprint
  cx = kobleTilDatabase(sqlitedb)

  kunder = []
  varer = []
  ordrer = []

  try:
    firma = fakturaFirmainfo(cx)
  except Exception, (e):
    print e
    if 'no such table' in e.message:
      byggDatabase(cx, 'faktura.sql')
      firma = fakturaFirmainfo(cx)

  firma.firmanavn = 'Testefirma'
  firma.kontaktperson = 'Testekontakt for firma'
  firma.forfall = 14
  firma.organisasjonsnummer = '232323232323 ORG'
  firma.kontonummer = '23232323232'
  firma.adresse = 'Firmaadresse\nSted xx2'
  firma.poststed = 'Firmapoststed'
  firma.postnummer = 3300
  firma.mva = 25
  firma.epost = 'firma@localhost'


  for iv in range(ANTALL_VARER):
    v = fakturaVare(cx)
    v.navn = u'Testvare %i ÆØÅ' % (iv + 1)
    v.detaljer = u'Denne varen er nr %i av %i' % (iv + 1, ANTALL_VARER)
    v.enhet = 'stk'
    v.mva = random.choice([0, 12, 25])
    v.pris = float(random.randint(10, 3000))
    varer.append(v)

  for ik in range(ANTALL_KUNDER):
    k = fakturaKunde(cx)
    k.navn = u'Testkunde %i ÆØÅ' % (ik + 1)
    k.kontaktperson = u'Testkontakt %i ÆØÅ' % (ik + 1)
    k.adresse = u'Adresse 1\nAdresse 2'
    k.postnummer = 3001
    k.poststed = u'Sunndalsøyra'
    k.epost = 'testkunde%i@localhost' % (ik + 1)
    kunder.append(k)
    for iif in range(ANTALL_ORDRER_PER_KUNDE):
      # lag en tilfeldig dato mellom 2008-01-01 og nå
      ordredato = random.randrange(1199142000, int(time()), 3600)
      logging.debug('tilfeldig dato: %s', ordredato)
      f = fakturaOrdre(cx, kunde=k, firma=firma, dato=ordredato)
      f.tekst = u'Testfaktura %i-%i ÆØÅ' % (ik + 1, iif + 1)
      vare = fakturaVare(cx, random.randint(1,ANTALL_VARER))
      f.leggTilVare(vare, random.randint(1,10), vare.pris, 25)
      f.betalt = random.choice([0, ordredato+7200])



  #cx.close()
