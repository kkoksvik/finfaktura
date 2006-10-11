#!/usr/bin/python -d
# -*- coding:utf8 -*-
###########################################################################
#    Copyright (C) 2005-2006 - Håvard Dahle og Håvard Sjøvoll
#    <havard@dahle.no>, <sjovoll@ntnu.no>
#
#    Lisens: GPL2
#
# $Id$
###########################################################################

# Sett denne til True for å skjule funksjonalitet som ikke er ferdigstilt
PRODUKSJONSVERSJON=False

__doc__ = """Fryktelig fin faktura: skriv ut fakturaene dine"""

import sys, os.path, dircache, mimetypes, re
from string import join
from time import time, strftime, localtime, mktime
from finfaktura.fakturabibliotek import * 
from finfaktura.f60 import f60, f60Eksisterer
from finfaktura.myndighetene import myndighetene
from finfaktura.epost import BRUK_GMAIL
import finfaktura.okonomi as fakturaOkonomi
import finfaktura.sikkerhetskopi as sikkerhetskopi

def cli_faktura():
    from finfaktura.cli import CLIListe, CLIInput
    logg = open("faktura-interactive.sql.log", "a+")
    db = kobleTilDatabase(loggfil=logg)
    bib = FakturaBibliotek(db)
    firma = bib.firmainfo()
    kunder = bib.hentKunder()
    kunde = CLIListe(kunder, "velg kunde: ")
    print "kunde: ", kunde
    varer = bib.hentVarer()
    vare = CLIListe(varer, "velg vare: ")
    antall = ""
    while not antall.isdigit():
        antall = CLIInput("antall %s: " % vare.enhet)
    antall = int(antall)
    tekst = CLIInput("Fakturatekst: ")
    mva = vare.mva * vare.pris * antall / 100
    sum = vare.pris * antall + mva
    print u"""STEMMER DETTE?
    =====
    Kunde: %s
    Vare: %s %s %s
    Tekst: %s
    SUM: %.2f kr (derav mva: %.2f)
    ===== """ % (kunde, antall, vare.enhet, vare, tekst, sum, mva)
    ja = CLIInput("J/n ")
    if len(ja) and ja.strip().lower()[0] != "j":
        sys.exit(0)
    ordre = bib.nyOrdre(kunde)
    ordre.tekst = tekst
    ordre.leggTilVare(vare, antall, vare.pris, vare.mva)
    bib.lagSikkerhetskopi(ordre)

    fakturanavn = ordre.lagFilnavn(bib.oppsett.fakturakatalog, fakturatype="epost")
    
    try:
        pdf = bib.lagPDF(ordre, "epost", fakturanavn)
    except FakturaFeil,(E):
        print u"OUCH! Kunne ikke lage PDF! Årsak: %s" % E
    except KundeFeil,(E):
        print u"OUCH! Kunne ikke lage PDF! Årsak: %s" % E

    print "Lagde pdf: %s" % pdf.filnavn
    db.close()


nogui = False
try:
    from qt import *
    from finfaktura.faktura_ui import faktura ## husk å kjøre "pyuic -x faktura.ui > faktura_ui.py" først!
except ImportError:
    print u"OOPS! Problemer med å laste moduler (er PyQT installert?)"
    print u"Faller tilbake til konsollmodus ..."
    print
    cli_faktura()
    sys.exit()


# sys.setappdefaultencoding("utf-8")
forfaltLogo_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x10\x00\x00\x00\x10" \
    "\x08\x06\x00\x00\x00\x1f\xf3\xff\x61\x00\x00\x02" \
    "\x74\x49\x44\x41\x54\x38\x8d\x95\x93\x4b\x48\x54" \
    "\x71\x14\xc6\x7f\xff\x7b\xef\x5c\xe7\x8e\x4e\x3a" \
    "\x73\x67\x54\x46\x74\xcc\x4a\x7c\x94\x61\x68\x60" \
    "\x0f\x53\x29\xf0\x41\x68\x91\x4a\x2d\x22\x11\x85" \
    "\x30\x5d\x14\x2d\xda\xd8\xa6\x82\x36\x41\x8b\x68" \
    "\xd5\xb6\xbd\x56\x3b\x25\x08\x02\x85\xa2\x85\x96" \
    "\x96\xa6\x96\x66\x2a\xa3\xe9\xcc\x38\x0f\x75\xe6" \
    "\xdf\x4a\xf0\x11\x92\x67\x75\x38\xe7\xfb\x7d\x8b" \
    "\xc3\xf9\x44\x57\x57\x17\x3b\x4b\x02\x69\x56\x6c" \
    "\xb5\x19\x64\xbe\xf9\xc5\xcc\x42\x84\x55\xb1\x4b" \
    "\xb5\x47\x59\x15\x78\x50\x4c\xc7\xc8\x0d\xa6\xee" \
    "\x16\x72\x5b\x13\x68\xfb\xe1\x29\x77\x53\xf8\xf9" \
    "\xa6\x3a\x12\x79\xed\x90\x1f\xdb\xd5\xf1\x12\x27" \
    "\x27\xff\x1b\x76\xe8\x58\x9e\x9f\xe1\x69\xb0\xb7" \
    "\x4a\xca\x68\xaf\x0c\xf4\x56\xc9\x27\x65\xbc\x48" \
    "\x54\xb1\xff\x4b\xaf\xee\x1c\x5c\x3f\x48\x65\x7b" \
    "\x83\x79\x3f\x76\xae\x33\xf1\xeb\xef\x4c\x8c\x74" \
    "\x17\x39\xab\x83\xde\x89\xf1\xf0\xf0\x88\x9f\xd1" \
    "\x3d\x0d\x32\x0c\x92\xef\x9d\xe6\x71\x5e\x4b\xe3" \
    "\x89\xe1\x40\x29\x83\x03\x63\xc4\x74\x17\xf9\x05" \
    "\x71\xc3\xf6\x7d\xc8\x7c\xfb\x83\xbe\x50\x8c\xe0" \
    "\x56\x46\xd9\x6c\x0c\x15\x3a\xf3\xb8\x7c\xfc\x82" \
    "\xf7\xbc\x51\x74\x11\x4d\x13\xc4\x62\x1b\x68\x9a" \
    "\x82\xad\xb8\x8e\xb2\x9a\xcc\xb3\x4d\xd9\x34\x2a" \
    "\x5b\x98\x6d\x06\x25\x0e\xbc\xb5\xa5\x6a\x87\xb3" \
    "\xa6\xda\xc0\x6a\x62\x9a\x1b\x48\x19\xc5\x34\xd7" \
    "\x11\x46\x0a\xee\xea\x8a\x84\xe6\x53\x4a\x5b\xfe" \
    "\x01\xf2\x77\x19\x18\x0a\x4a\x53\x2e\xad\x59\x75" \
    "\x39\xc5\x96\xcc\x22\x60\x01\xa7\x33\x48\x42\x42" \
    "\x08\xb7\x3b\x00\xcc\xa2\x65\x1d\xe6\x58\x7d\x46" \
    "\xc1\xb5\x5c\x5a\x75\x05\xeb\xb6\x1b\x54\xa5\x51" \
    "\xd2\x71\xc9\xf2\xc8\x73\xb5\x22\x45\xd8\x5c\xc0" \
    "\x0a\x9a\x16\x20\x29\x69\x15\x8f\x27\x8c\xc5\xe2" \
    "\x03\x25\x80\x9e\x1a\x15\x8e\xb9\x19\xef\xa7\x2f" \
    "\xf2\xc3\x74\x98\x49\x00\x35\xcb\x86\xed\x61\x39" \
    "\xdd\x45\xed\x9e\x0a\xfd\x50\x0e\x10\x00\x96\x98" \
    "\x99\x99\x67\x70\x70\x0e\xbb\xdd\x87\x69\x2e\x02" \
    "\x0b\x08\x23\x8a\x3d\xd9\x6f\xd7\x47\xc3\xc6\xbb" \
    "\x9f\xf4\x47\xe2\x44\xd4\xb6\x23\x5c\xa9\x6f\x56" \
    "\xef\x38\x6b\x53\x0d\xa1\xad\x01\x8b\x80\x8f\x9e" \
    "\x9e\x59\xba\xbb\xa7\x71\x38\x16\x29\x2b\x5b\x02" \
    "\x7c\xc0\x1f\x34\xd7\x1a\xae\x60\xc4\x3b\x35\xcc" \
    "\xd8\xf0\x32\x43\xea\xb3\x7a\x5e\x66\xb5\xe8\x5e" \
    "\x8b\x0b\x90\x7e\x90\xcb\xc0\x32\xf6\x44\x3f\x6e" \
    "\x57\x88\xca\x8a\x55\xd2\xd3\xfd\x20\x57\x40\x06" \
    "\x10\x5a\x14\xc3\x1d\xd3\xf5\x11\x5c\x7d\x63\xf4" \
    "\x6b\xd1\x08\xda\xec\xab\xd8\xb2\xd0\x83\x02\x04" \
    "\x02\x01\x48\x34\x21\x69\xb0\x4a\xe2\x03\x71\x26" \
    "\xdf\x4b\x40\x82\x8c\x03\x71\xd8\x90\x62\x7d\x0d" \
    "\x1d\x41\x8a\x38\x7a\x80\x3c\x4f\x02\xd9\x71\x89" \
    "\x85\xad\x91\x93\x3b\x7f\x6e\xdb\x4a\x4e\x84\x98" \
    "\x9f\x0c\xf1\x4d\xdc\xea\xec\xda\xd4\xee\x2b\xb1" \
    "\x42\x80\x02\xf2\x2f\x88\xc9\xd2\x31\x87\xf1\x2f" \
    "\x13\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60" \
    "\x82"
slettetLogo_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x10\x00\x00\x00\x10" \
    "\x08\x06\x00\x00\x00\x1f\xf3\xff\x61\x00\x00\x02" \
    "\xf7\x49\x44\x41\x54\x38\x8d\x5d\x93\xcd\x6b\x54" \
    "\x67\x14\xc6\x7f\xe7\xcd\x9d\x9b\xf9\x40\x74\xd2" \
    "\xb1\xde\x44\x9b\xc9\x60\x4d\xc7\x60\x4a\x47\xc7" \
    "\x86\x5a\xc9\x84\x82\xd6\xc9\x1f\xd0\x9d\xba\x52" \
    "\x8c\x04\x09\x14\x71\x61\x56\x2e\xc4\x9d\x03\x09" \
    "\xd8\x65\x37\xba\x8b\x9b\x4a\x5c\x04\x24\x83\x64" \
    "\xd1\xa4\x03\x42\x2e\x64\x86\xf9\x30\x96\x01\xe3" \
    "\x30\xb6\x31\x24\x33\x73\x93\x9b\xfb\x76\x71\x53" \
    "\x0a\x7d\xe0\xc7\xd9\x1d\x9e\xf3\x70\x1e\x99\x9b" \
    "\x9b\x63\x71\x71\x11\x11\x41\x80\xcf\xa0\xfb\x1b" \
    "\xad\xbf\x1a\xd6\xfa\x5b\x4f\xeb\x01\x0f\xf0\x44" \
    "\xd6\x6d\x91\xe5\x55\x91\xd2\xdf\xe0\x68\x40\x6b" \
    "\xcd\xd8\xd8\x18\x46\x3e\x9f\x67\x66\x66\x06\x80" \
    "\x0c\x24\x6f\xc1\x64\x34\x1c\x1e\xdf\x3f\x79\xd2" \
    "\x0a\x1c\x3b\xd6\xad\x45\x68\x7f\xfc\xe8\x44\x2a" \
    "\x95\x8d\xcf\xb7\xb6\xe6\xe7\x61\x76\x19\x8a\x00" \
    "\x22\x82\xc1\x81\x7e\x80\xef\xef\x1b\x46\x6e\xe8" \
    "\xc2\x85\x73\xd1\x6b\xd7\xc4\x3c\x7b\x16\x09\x87" \
    "\x01\xd0\x8e\x13\x1a\x58\x5b\x4b\x0c\x3e\x7d\x7a" \
    "\x3b\xba\xb0\x30\x92\xeb\x74\xa6\x7e\x87\x25\x00" \
    "\x43\x80\x51\x48\xde\x57\x2a\x97\x1a\x1f\x4f\x1f" \
    "\xbe\x79\x13\xd5\xd7\x07\xad\x16\xec\xec\x00\x20" \
    "\x40\x70\x70\x90\x81\x3b\x77\x24\x18\x8b\xa5\xf7" \
    "\x9e\x3d\xcb\xed\x3a\xce\x55\x81\xa2\x3a\x0a\xe6" \
    "\x04\x4c\x0e\x25\x93\xe9\xc3\x57\xae\xa0\xe2\x71" \
    "\x88\xc7\xfd\x05\xd5\xaa\x4f\xbb\x0d\xf1\x38\x62" \
    "\x59\x58\xa3\xa3\x8c\xa4\xd3\xe9\x9f\x60\xf2\x08" \
    "\x98\xea\x6b\x48\x9e\x10\xc9\x46\x87\x86\x50\xed" \
    "\x36\x1c\x3a\x04\x3d\x3d\x90\x4a\x81\x88\x4f\x2a" \
    "\x05\x3d\x3d\xe8\x50\x08\x5d\x2a\xd1\xab\x14\xfd" \
    "\x90\xfd\x12\x92\xc6\xb0\xd6\xe7\xdd\x48\xc4\x0a" \
    "\x00\xbc\x79\x03\xdb\xdb\x70\xfd\xba\xef\x22\x9b" \
    "\xf5\x03\x8a\xc5\xd8\x5f\x5d\x65\xf7\xee\x5d\xf6" \
    "\x5f\xbf\x86\x4e\x87\x13\x60\x75\xc1\x79\xc3\x13" \
    "\x49\x98\x4a\x85\x55\xbd\x0e\x5d\x5d\x50\xa9\x40" \
    "\xbd\x0e\xd3\xd3\xd0\xdf\x0f\x80\x57\x2e\xe3\x4c" \
    "\x4c\xe0\x2e\x2d\x01\xa0\x80\x30\x84\x3b\x90\x30" \
    "\x3c\xc0\x6b\xb5\xa0\x56\xf3\xed\x7a\x1e\x58\x16" \
    "\x68\xcd\xff\xa5\x0e\xa6\x00\x1a\xf0\x00\xe5\xc1" \
    "\x5b\xc7\x75\x5b\x5e\xb3\x89\x6e\x34\xd0\xa7\x4f" \
    "\xa3\x1f\x3c\x80\x78\x1c\x5d\x2e\xa3\xcb\x65\xd4" \
    "\xa9\x53\x04\x9f\x3c\xc1\xbc\x78\x91\x00\x10\x00" \
    "\xb6\xa1\xe5\xc1\x5b\x65\xc3\xca\x3b\xd8\x70\x01" \
    "\xfa\xfa\xe0\xe1\x43\x38\x73\x06\x6c\x1b\x6e\xdc" \
    "\xf0\xb1\x6d\xd4\xf0\x30\x81\x47\x8f\x30\x8f\x1f" \
    "\xc7\x55\x8a\x1a\x6c\xd4\x60\x45\xd9\x50\xac\xc2" \
    "\xcb\xf7\xa1\x10\x28\x85\xe4\xf3\x48\xa1\x00\xd3" \
    "\xd3\x88\x6d\x23\xb6\xed\xe7\x51\x28\x20\xf9\x3c" \
    "\x28\x45\x25\x14\xa2\x04\x2f\xd7\xa1\x68\xfc\x05" \
    "\xbb\x2f\x60\x36\xea\x38\x23\x21\x48\x1f\x7d\xfe" \
    "\x1c\x79\xf5\x0a\x3e\x7c\x80\xde\x5e\xff\xe8\x6a" \
    "\x15\xee\xdd\x43\x6f\x6e\xf2\x27\xb0\xe0\x38\x7f" \
    "\xfc\x06\xb3\x3f\xc2\xae\xa1\x81\x15\x28\x3e\x76" \
    "\xdd\xa9\xbd\x46\x23\xf7\x9d\x69\x9e\xfb\x22\x18" \
    "\x14\xd3\xb2\x10\x11\xff\x95\xb5\xa6\xd3\x6e\x53" \
    "\xde\xdc\xd4\x0b\x8d\x46\xe1\x57\xd7\x9d\x2a\x42" \
    "\xf1\x32\xfc\xd7\x85\x65\x58\x7a\xec\x38\x57\xeb" \
    "\xb5\xda\x64\xa2\xd9\xcc\x26\x62\x31\x2b\x1c\x89" \
    "\x04\x3d\xe0\xd3\xce\x8e\x53\x6e\x36\x37\x4a\x5b" \
    "\x5b\xf3\x2f\xb4\x9e\x5d\x3b\x28\x13\x80\x91\xc9" \
    "\x64\xd0\x5a\xff\x5b\xe7\x62\x07\x7e\xde\xd3\xfa" \
    "\x17\x57\x64\xe4\x93\x52\x09\x0f\xd8\xf7\xbc\x75" \
    "\xd1\x7a\xb9\x5b\xa4\x74\x19\x9c\x4b\x07\xae\x32" \
    "\x99\x0c\xff\x00\x52\xc5\x38\x72\x53\x7f\x4a\xf3" \
    "\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82"

class Faktura (faktura): ## leser gui fra faktura_ui.py
    db = None
    denne_kunde = None
    denne_faktura = None
    denne_vare = None
    gammelTab = 0

    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        faktura.__init__(self, parent, name, fl)

        #skjul ikke-ferdige tabs dersom vi er i produksjon
        # TODO: gjøre dem klare for produksjon
        if PRODUKSJONSVERSJON:
            self.fakturaTab.removePage(self.fakturaTab.page(4))
            self.fakturaTab.removePage(self.fakturaTab.page(4))
            self.fakturaTab.removePage(self.fakturaTab.page(4))
            self.fakturaTab.removePage(self.fakturaTab.page(4))
        else:
            self.setCaption("FRYKTELIG FIN FADESE (utviklerversjon)")

        self.connect(self.fakturaTab, SIGNAL("currentChanged(QWidget*)"), self.skiftTab)

        self.connect(self.fakturaNy, SIGNAL("clicked()"), self.nyFaktura)
#     self.connect(self.fakturaFakturaliste, SIGNAL("doubleClicked(QListViewItem*, const QPoint&, int)"), self.redigerFaktura)
        self.connect(self.fakturaFaktaLegginn, SIGNAL("clicked()"), self.leggTilFaktura)
        self.connect(self.fakturaFaktaVare, SIGNAL("highlighted(int)"), self.fakturaVareOppdater)
        self.connect(self.fakturaFakturaliste, SIGNAL("selectionChanged(QListViewItem*)"), self.visFakturadetaljer)
        self.connect(self.fakturaFaktaVareLeggtil, SIGNAL("clicked()"), self.leggVareTilOrdre)
        self.connect(self.fakturaFaktaVareFjern, SIGNAL("clicked()"), self.fjernVareFraOrdre)
        self.connect(self.fakturaLagEpost, SIGNAL("clicked()"), self.lagFakturaEpost)
        self.connect(self.fakturaLagPapir, SIGNAL("clicked()"), self.lagFakturaPapir)
        self.connect(self.fakturaLagKvittering, SIGNAL("clicked()"), self.lagFakturaKvittering)
        self.connect(self.fakturaBetalt, SIGNAL("clicked()"), self.betalFaktura)
        self.connect(self.fakturaVisKansellerte, SIGNAL("toggled(bool)"), self.visFaktura)
        self.fakturaFaktaKryss.mousePressEvent = self.lukkFakta
        self.connect(self.fakturaSendepostSend, SIGNAL("clicked()"), self.sendEpostfaktura)
        self.connect(self.fakturaSendepostAvbryt, SIGNAL("clicked()"), self.skjulSendepostBoks)

        self.connect(self.kundeNy, SIGNAL("clicked()"), self.lastKunde)
        self.connect(self.kundeKundeliste, SIGNAL("doubleClicked(QListViewItem*, const QPoint&, int)"), self.redigerKunde)
        self.connect(self.kundeInfoEndre, SIGNAL("clicked()"), self.leggTilKunde)
        self.connect(self.kundeNyfaktura, SIGNAL("clicked()"), self.nyFakturaFraKunde)
        self.connect(self.kundeKundeliste, SIGNAL("selectionChanged(QListViewItem*)"), self.visKundedetaljer)
        self.connect(self.kundeVisFjernede, SIGNAL("toggled(bool)"), self.visKunder)
        self.kundeInfoKryss.mousePressEvent = self.lukkKundeinfo

        #self.connect(self.varerVareliste, SIGNAL("selected(const QString&)"), self.nyFaktura)

        self.connect(self.varerNy, SIGNAL("clicked()"), self.lastVare)
        self.connect(self.varerVareliste, SIGNAL("doubleClicked(QListViewItem*, const QPoint&, int)"), self.redigerVare)
        self.connect(self.varerInfoLegginn, SIGNAL("clicked()"), self.registrerVare)
        self.connect(self.varerVareliste, SIGNAL("selectionChanged(QListViewItem*)"), self.visVaredetaljer)
        self.connect(self.varerVisFjernede, SIGNAL("toggled(bool)"), self.visVarer)
        self.varerInfoKryss.mousePressEvent = self.lukkVarerinfo
        
        self.connect(self.dittfirmaFinnFjernLogo, SIGNAL("clicked()"), self.finnFjernLogo)
        self.connect(self.dittfirmaLagre, SIGNAL("clicked()"), self.oppdaterFirma)
        self.connect(self.dittfirmaFakturakatalogSok, SIGNAL("clicked()"), self.endreFakturakatalog)

        self.connect(self.okonomiAvgrensningerDato, SIGNAL("toggled(bool)"), self.okonomiFyllDato)
        self.connect(self.okonomiAvgrensningerKunde, SIGNAL("toggled(bool)"), self.okonomiFyllKunder)
        self.connect(self.okonomiAvgrensningerVare, SIGNAL("toggled(bool)"), self.okonomiFyllVarer)
        self.connect(self.okonomiRegnskapRegnut, SIGNAL("clicked()"), self.okonomiRegnRegnskap)
        self.connect(self.okonomiFakturaerSkrivut, SIGNAL("clicked()"), self.okonomiSkrivUtFakturaer)

        self.connect(self.sikkerhetskopiGmailLastopp, SIGNAL("clicked()"), self.sikkerhetskopiGmail)
        
        for obj in (self.dittfirmaFirmanavn,
            self.dittfirmaOrganisasjonsnummer,
            self.dittfirmaKontaktperson,
            self.dittfirmaEpost,
            self.dittfirmaAdresse,
            self.dittfirmaPostnummer,
            self.dittfirmaPoststed,
            self.dittfirmaTelefon,
            self.dittfirmaTelefaks,
            self.dittfirmaMobil,
            self.dittfirmaKontonummer,
            self.dittfirmaVilkar,
            self.dittfirmaFakturakatalog,
            self.dittfirmaForfall):
            self.connect(obj, SIGNAL("lostFocus()"), self.firmaSjekk)

        self.kundeKundeliste.contextMenuEvent = self.kundeContextMenu
        self.fakturaFakturaliste.contextMenuEvent = self.fakturaContextMenu
        self.varerVareliste.contextMenuEvent = self.vareContextMenu

        self.connect(self.epostLagre, SIGNAL("clicked()"), self.oppdaterEpost)


        self.databaseTilkobler()

        self.fakturaForfaltLogo = QPixmap()
        self.fakturaForfaltLogo.loadFromData(forfaltLogo_data,"PNG")
        self.slettetLogo = QPixmap()
        self.slettetLogo.loadFromData(slettetLogo_data,"PNG")

        try:
            self.faktura = FakturaBibliotek(self.db)
            self.firma   = self.faktura.firmainfo()
        except DBNyFeil, (E):
            # lag databasen fra faktura.sql
            self.db.close()
            del(self.db)
            del(self.c)
            self.db = lagDatabase(finnDatabasenavn())
            self.c = self.db.cursor()
            #self.databaseTilkobler()
            self.faktura = FakturaBibliotek(self.db)
            self.firma   = self.faktura.firmainfo()
            self.obs(u"Dette er første gang du starter programmet.\nFør du kan legge inn din første faktura, \ner jeg nødt til å få informasjon om firmaet ditt.")
            self.fakturaTab.showPage(self.fakturaTab.page(3))
            self.gammelTab = 3
        except DBGammelFeil, (E):
            #oppgrader databasen
            if not self.JaNei(u"Databasen må oppgraderes.\nVil du gjøre det nå?"):
                sys.exit(99)
                
            self.db.close()
            del(self.db)
            del(self.c)
            from finfaktura.oppgradering import oppgrader, OppgraderingsFeil
            o = oppgrader()
            try:
                o.oppgraderSamme(finnDatabasenavn())
            except OppgraderingsFeil:
                raise
            except SikkerhetskopiFeil, e:
                self.alert('Databasen er oppgradert, men kunne ikke lage sikkerhetskopier fordi:\n %s' % e) # str(e).decode('utf8'))
            self.databaseTilkobler()
            self.faktura = FakturaBibliotek(self.db)
            self.firma   = self.faktura.firmainfo()
            self.obs(u"Databasen er nå oppdatert til nyeste versjon.\nDu bør se over dataene dine og forsikre deg om at alt er i orden.")
                
                
        try:
            self.faktura.sjekkSikkerhetskopier(lagNyAutomatisk=True)
        except SikkerhetskopiFeil, e:
            self.alert(e.args[0])
        self.faktura.produksjonsversjon = PRODUKSJONSVERSJON

    def __del__(self):
        self.db.close()

    def databaseTilkobler(self):
        if not PRODUKSJONSVERSJON:
            logg=open('faktura-qtgui.log', 'a+')
        else:
            logg=None
        self.db = kobleTilDatabase(loggfil=logg)
        self.c = self.db.cursor()

    def skiftTab(self, w):
        i = self.fakturaTab.currentPageIndex()
        pass
        #debug("gammel tab:%s, ny:%s" % (self.gammelTab, i))
        # stygt hack!
        # TODO: finne ut hvorfor denne blir kalt to ganger for hvert bytte
        #if self.gammelTab == i: return
        #if self.gammelTab == 3:
            #skifter bort fra firmainfo, lagre automatisk
            #debug("Lagrer firmainfo automatisk")
            #self.oppdaterFirma()
            #self.gammelTab = i
        #debug("setter gammeltab til: %s" % i)
        if i is 0: self.visFaktura()
        elif i is 1: self.visKunder()
        elif i is 2: self.visVarer()
        elif i is 3: self.visFirma()
        elif i is 4: self.visEpost()
        elif i is 5: self.visOkonomi()
        elif i is 6: self.visMyndigheter()
        elif i is 7: self.visSikkerhetskopi()
        self.gammelTab = i
#     elif i is 5. self.visOppsett()

################## FAKTURA ########################

    fakturaOrdrelinjeDummytekst = u"[Legg inn en vare]"

    def lukkFakta(self, *ev):self.fakturaFakta.hide()

    def fakturaContextMenu(self, event):
        try:
            ordre = self.fakturaFakturaliste.selectedItem().ordre
        except AttributeError:
            return None #ingen ordre er valgt
        meny = QPopupMenu(self)
        tittel = QLabel("<b>Rediger faktura</b>", self)
        tittel.setAlignment(Qt.AlignCenter)
        meny.insertItem(tittel)
        if not ordre.kansellert:
#     meny.insertItem("Dupliser", self.dupliserFaktura)
            meny.insertItem("Er betalt", self.betalFaktura)
            meny.insertItem("Send purring", self.purrFaktura)
            meny.insertItem("Send til inkasso", self.inkassoFaktura)
            meny.insertItem(u"Kansellér", self.kansellerFaktura)
        else:
            meny.insertItem("Ikke kansellert", self.avkansellerFaktura)
        meny.exec_loop(QCursor.pos())

    def visFaktura(self):
        visKansellerte = self.fakturaVisKansellerte.isChecked()
        self.fakturaDetaljerTekst.setText('')
        self.fakturaFakta.hide()
        self.fakturaSendepostBoks.hide()
        i = self.fakturaFakturaliste.insertItem
        self.fakturaFakturaliste.clear()
        nu = time()
        for ordre in self.faktura.hentOrdrer():
            if not visKansellerte and ordre.kansellert: continue
            if ordre.betalt: bet = strftime("%Y-%m-%d %H:%M", localtime(ordre.betalt))
            else: bet = "Nei"
            l = QListViewItem(self.fakturaFakturaliste,
                              "%06d" % ordre.ID,
                              ordre.tekst,
                              ordre.kunde.navn,
                              "%.2f kr" % (ordre.finnPris() + ordre.finnMva()),
                              strftime("%Y-%m-%d %H:%M", localtime(ordre.forfall)),
                              bet
                             )
            l.ordre = ordre
            if ordre.forfalt():
                debug("%s er forfalt men ikke betalt!" % ordre._id)
                l.setPixmap(5, self.fakturaForfaltLogo)
            if bool(ordre.kansellert):
                l.setPixmap(0, self.slettetLogo)
            i(l)
        self.fakturaBetaltDato.setDate(QDate.currentDate())
        # to kart som gjenspeiler innholdet i ordrelinjer og varer
        self.fakturaKartOrdrelinje = {}
        self.fakturaKartVarer = {}

    def nyFakturaFraKunde(self):
        try:
            kunde = self.kundeKundeliste.selectedItem().kunde
        except AttributeError:
            self.alert(u'Ingen kunde er valgt')
            return False
        debug("ny faktura fra kunde: %s" % kunde.ID)
        self.fakturaTab.setCurrentPage(0)
        self.nyFaktura(kunde)

#   def nyFakturaFraFaktura(self, faktura):
#     kundeID = self.fakturaFakturaliste.currentItem().faktura.KundeID
#     kunde = self.faktura.hentKunde(kundeID)
#     self.nyFaktura(kunde)

    def nyFaktura(self, kunde = None, ordrelinje = None):
        # sjekk at firmainfo er fullstendig utfylt (så feiler vi ikke senere)
        try: self.firma.sjekkData()
        except FirmainfoFeil,e:
            self.alert(u'Informasjonen om firmaet ditt må være fullstendig'+\
                       u'før du kan fylle inn fakturaen.\n'+
                       str(e).decode("utf8"))
            self.fakturaTab.setCurrentPage(3)
            return False
        if not kunde and not ordrelinje:
            self.denne_faktura=None
        if kunde is not None:
            self.fakturaFaktaMottaker.clear()
            self.fakturaFaktaMottaker.insertItem(unicode(kunde))
            self.fakturaFaktaVare.setFocus()
        else:
            self.fyllFakturaMottaker()
            self.fakturaFaktaMottaker.setFocus()
        if ordrelinje is not None:
            self.fakturaOrdrelinje = ordrelinje
            self.fakturaFaktaOrdrelinje.clear()
            for vare in ordrelinje.keys():
                self.fakturaFaktaOrdrelinje.insertItem(unicode(vare))
                self.fakturaKartOrdrelinje[self.fakturaFaktaOrdrelinje.count() - 1] = vare
        else:
            self.fakturaOrdrelinje = {}
            self.fakturaFaktaOrdrelinje.clear()
            self.fakturaFaktaOrdrelinje.insertItem(self.fakturaOrdrelinjeDummytekst)
        self.fakturaFaktaTekst.setText("")
        self.fyllFakturaVare()
        self.fakturaFakta.show()

    def leggTilFaktura(self):
        #legg inn faktura i registeret 
        
        #er all nødvendig info samlet inn?
        if self.fakturaFaktaOrdrelinje.count() == 0 or \
            ( self.fakturaFaktaOrdrelinje.count() == 1 and \
            self.fakturaOrdrelinjeDummytekst == self.fakturaFaktaOrdrelinje.item(0).text() ): 
            # varelista er tom, eller inneholder bare standardtekst "legg inn en vare"
            self.alert(u"Du må legge til minst én vare")
            return False
        
        if not self.fakturaFaktaTekst.text() and \
            not self.JaNei(u"Vil du virkelig legge inn fakturaen uten fakturatekst?"):
            self.fakturaFaktaTekst.setFocus()
            return False
        
        #all nødvendig info er der, legg inn fakturaen
        kundetekst = self.fakturaFaktaMottaker.currentText()
        kre = re.search(re.compile(r'kunde\ #\s?(\d+)'), unicode(kundetekst))
        kunde = self.faktura.hentKunde(kre.group(1))
        f = self.faktura.nyOrdre(kunde)
        f.tekst = self.fakturaFaktaTekst.text()
        for vare in self.fakturaOrdrelinje.keys():
            antall = self.fakturaOrdrelinje[vare]
            #debug("fant vare i fakturaen: %s * %s " % (antall, vare))
            f.leggTilVare(vare, antall, vare.pris, vare.mva)
        debug("legger inn faktura: %s " % unicode(f))
        debug("Lager sikkerhetskopi")
        self.faktura.lagSikkerhetskopi(f)
        self.visFaktura() # oppdater listen slik at den nye fakturaen blir med
        self.fakturaFakturaliste.setSelected(self.fakturaFakturaliste.lastItem(), True) # velg den nye fakturaen
        self.fakturaFakta.hide()
        
        #skal vi lage blanketter nå?
        s = u'Den nye fakturaen er laget. Vil du lage tilhørende blankett nå?'
        knapp = QMessageBox.information(self, u'Lage blankett?', s, 'Epost', 'Papir', 'Senere', 0, 2)
        if knapp == 0: self.lagFaktura(Type='epost')
        elif knapp == 1: self.lagFaktura(Type='papir')
        
#   def redigerFaktura(self, rad, koord, kolonne):
#     self.denne_faktura = rad.ordre
#     linje = {}
#     for (ant, vare) in map(lambda x:(x.kvantum, x.vare), rad.ordre.linje):
#       linje[vare] = ant
# #     self.nyFaktura(kunde = rad.ordre.kunde, ordrelinje = linje)
#     self.nyFaktura(ordre = rad.ordre, ordrelinje = linje)

    def fyllFakturaMottaker(self):
        self.fakturaFaktaMottaker.setEnabled(True)
        self.fakturaFaktaMottaker.clear()
        i = self.fakturaFaktaMottaker.insertItem
        for kunde in self.faktura.hentKunder():
            i(unicode(kunde))

    def fyllFakturaVare(self):
        self.fakturaKartVarer = {}
        self.fakturaFaktaVare.setEnabled(True)
        self.fakturaFaktaVare.clear()
        i = self.fakturaFaktaVare.insertItem
        for v in self.faktura.hentVarer():
            i(unicode(v.navn))
            self.fakturaKartVarer[self.fakturaFaktaVare.count() - 1] = v
        self.fakturaVareOppdater(0)

    def leggVareTilOrdre(self):
        if self.fakturaFaktaOrdrelinje.count() == 1 and \
            self.fakturaOrdrelinjeDummytekst == self.fakturaFaktaOrdrelinje.item(0).text(): # er det dummy-tekst?
            self.fakturaFaktaOrdrelinje.clear()
        vare = self.fakturaKartVarer[self.fakturaFaktaVare.currentItem()]
        if self.fakturaOrdrelinje.has_key(vare):
            self.alert(u"Du har allerede lagt inn %s i fakturaen.\nDersom du vil endre antallet %ser må du fjerne den gamle posten først" % \
                (vare.navn, vare.navn))
            return False
        self.fakturaFaktaOrdrelinje.insertItem("%s %s %s" % (self.fakturaFaktaAntall.value(), vare.enhet, vare))
        self.fakturaKartOrdrelinje[self.fakturaFaktaOrdrelinje.count() - 1] = vare
        self.fakturaOrdrelinje[vare] = self.fakturaFaktaAntall.value()
        self.oppdaterFakturaSum()

    def fjernVareFraOrdre(self):
        valgt = self.fakturaFaktaOrdrelinje.currentItem()
        if valgt == -1: 
            self.alert(u"Du må velge en vare før du kan fjerne den")
        elif valgt == 1 and \
            self.fakturaOrdrelinjeDummytekst == self.fakturaFaktaOrdrelinje.item(valgt).text():
            # dummyteksten er markert
            return
        vare = self.fakturaKartOrdrelinje[valgt]
        debug("Fjerner vare fra ordre: %s" % vare)
        del(self.fakturaOrdrelinje[vare])
        self.fakturaFaktaOrdrelinje.removeItem(valgt)
        self.oppdaterFakturaSum()

    def oppdaterFakturaSum(self):
        p = mva = 0.0
        for vare in self.fakturaOrdrelinje.keys():
            antall = self.fakturaOrdrelinje[vare]
            p += vare.pris * antall
            mva += vare.pris * antall * vare.mva / 100
        self.fakturaFaktaSum.setText("<u>%.2fkr (+%.2fkr mva)</u>" % (p, mva))

    def fakturaVareOppdater(self, idx):
        # oppdaterer data avhengig av hvilken vare som er valgt i legg-inn-faktura-skjemaet
        try:
            vare = self.fakturaKartVarer[idx]
            self.fakturaFaktaAntall.setValue(1)
            self.fakturaFaktaAntall.setSuffix(" %s" % vare.enhet)
            self.fakturaFaktaVareDetaljer.setText("<i>"+vare.detaljer+"</i>")
            self.fakturaFaktaVarePris.setText("<b>%.2f kr</b> (+ %i%% mva: %.2f kr)" % (vare.pris, vare.mva, vare.pris * vare.mva / 100))
        except KeyError:
            pass

    def visFakturadetaljer(self, linje):
        s = "<p><b>%s</b><p>" % unicode(linje.ordre.tekst)
        if linje.ordre.kansellert:
            s += '<b><font color=red>Denne fakturaen er kansellert</font></b><p>'
        if linje.ordre.linje:
            for salg in linje.ordre.linje:
                s += "%i x <i>%s</i><br>\n" % (salg.kvantum, unicode(salg.vare.navn))
            pris = linje.ordre.finnPris()
            moms = linje.ordre.finnMva()
            s += "<p>&nbsp;&nbsp;&nbsp;%.2f kr<br> + mva %.2f kr<br> <u>= %.2f kr</u>\n" % (pris, moms, pris+moms)
            
        s += "<p><i>Historikk</i>:<br>"
        s += "Fakturert: %s<br>" % strftime("%Y-%m-%d", localtime(linje.ordre.ordredato))
        if linje.ordre.betalt > linje.ordre.forfall or \
            ( not linje.ordre.betalt and time() > linje.ordre.forfall ):
            s += "<font color=orange>Forfalt: %s</font><br>" % strftime("%Y-%m-%d", localtime(linje.ordre.forfall))
        if None:
            s += "<font color=darkred>Purret: %s</font><br>" % strftime("%Y-%m-%d", localtime(linje.ordre.ordredato))
        if None:
            s += "<font color=red>Inkasso: %s</font><br>" % strftime("%Y-%m-%d", localtime(linje.ordre.ordredato))
        if linje.ordre.kansellert:
            s += "<font color=red>Kansellert: %s</font><br>" % strftime("%Y-%m-%d", localtime(linje.ordre.kansellert))
        if linje.ordre.betalt:
            s += "<font color=darkgreen>Betalt: %s</font><br>" % strftime("%Y-%m-%d", localtime(linje.ordre.betalt))
        self.fakturaDetaljerTekst.setText(s)
        
        minstedato = localtime(linje.ordre.ordredato)
        self.fakturaBetaltDato.setMinValue(QDate(minstedato[0],minstedato[1],minstedato[2]))

    def lagFakturaKvittering(self): 
        try:
            ordre = self.fakturaFakturaliste.selectedItem().ordre
        except AttributeError:
            self.alert(u'Ingen faktura er valgt')
            return False
        kvitt = ordre.hentSikkerhetskopi()
        kvitt.skrivUt()
        #return self.lagFaktura(Type="kvittering")

    def lagFakturaEpost(self): return self.lagFaktura(Type='epost')
    def lagFakturaPapir(self): return self.lagFaktura(Type='papir')
    
    def lagFaktura(self, Type="epost"):
        try:
            ordre = self.fakturaFakturaliste.selectedItem().ordre
        except AttributeError:
            self.alert(u'Ingen faktura er valgt')
            return False
        ordre.firma = self.firma
        fakturanavn = ordre.lagFilnavn(self.faktura.oppsett.fakturakatalog, fakturatype=Type)
        try:
            pdf = f60(fakturanavn)
            pdf.settFirmainfo(self.firma._egenskaper)
            pdf.settKundeinfo(ordre.kunde._id, ordre.kunde.postadresse())
            pdf.settFakturainfo(ordre._id, ordre.ordredato, ordre.forfall, ordre.tekst)
            pdf.settOrdrelinje(ordre.hentOrdrelinje)
        except f60Eksisterer, (E):
            # HACK XXX: E er nå filnavnet
            if Type == "epost":
                self.visEpostfaktura(ordre, unicode(E))  
                #if self.JaNei(u"PDF-fila eksisterer fra før av: %s. \nVil du sende den til %s nå?" % (fakturanavn, ordre.kunde.epost)): 
                    #if self.faktura.sendEpost(ordre, fakturanavn): self.obs('Fakturaen er sendt')
            elif Type == "papir":
                if self.JaNei(u"Blanketten er laget fra før av. Vil du skrive den ut nå?"): 
                    self.faktura.skrivUt(unicode(E))
            return None
        if Type == "epost": 
            pdf.lagBakgrunn()
        elif Type == "kvittering":
            pdf.lagBakgrunn()
            pdf.lagKopimerke()

        try:
            pdf.fyll()
        except FirmainfoFeil,(E):
            self.alert(u"Du må fylle ut firmainfo først:\n%s" % E)
            self.fakturaTab.setCurrentPage(3)
        except KundeFeil,(E):
            self.alert(u"Kan ikke lage PDF!\nÅrsak: %s" % E)
        else:
            res = pdf.settSammen()
            if not res: 
                self.alert("Kunne ikke lage PDF! ('%s')" % pdf.filnavn)
            else: 
                if Type == "epost":
                    #self.obs("Lagde pdf: %s" % pdf.filnavn)
                    self.visEpostfaktura(ordre, fakturanavn)
                    #if self.JaNei(u'Blanketten er lagret i <b>%s</b><br>Vil du sende den til %s nå?' % (pdf.filnavn, ordre.kunde.epost)):
                        #if self.faktura.sendEpost(ordre, pdf.filnavn): self.obs('Fakturaen er sendt')
                elif Type == "papir":
                    if self.JaNei(u"Blanketten er laget. Vil du skrive den ut nå?"): pdf.skrivUt()
                    else: self.obs(u"Blanketten er lagret med filnavn: %s" % pdf.filnavn)

    def betalFaktura(self):
        try:
            ordre = self.fakturaFakturaliste.selectedItem().ordre
        except AttributeError:
            self.alert("Ingen faktura er valgt")
            return
        if ordre.betalt:
            self.obs("Denne fakturaen er allerede betalt (%s)." % strftime("%Y-%m-%d", localtime(ordre.betalt)))
            return False
        if ordre.kansellert:
            self.obs("Denne fakturaen ble kansellert den %s, og kan ikke betales." % strftime("%Y-%m-%d", localtime(ordre.kansellert)))
            return False
        d = self.fakturaBetaltDato.date()
        dato = mktime((d.year(),d.month(),d.day(),0,0,0,0,0,0))
        ordre.betal(dato)
        self.visFaktura()

    def kansellerFaktura(self):
        ordre = self.fakturaFakturaliste.selectedItem().ordre
        if ordre.betalt:
            self.alert(u"Du kan ikke kansellere denne ordren, den er betalt.")
        elif self.JaNei(u"Vil du virkelig kansellere ordre nr %s?" % ordre.ID):
            ordre.settKansellert()
            self.visFaktura()

    def avkansellerFaktura(self):
        ordre = self.fakturaFakturaliste.selectedItem().ordre
        ordre.settKansellert(False)
        self.visFaktura()

    def purrFaktura(self):pass
    def inkassoFaktura(self):pass
    
    def skjulSendepostBoks(self):
        self.fakturaSendepostBoks.hide()
    
    def visEpostfaktura(self, ordre, pdfFilnavn):
        ##u'Vedlagt følger epostfaktura #%i:\n%s\n\n-- \n%s\n' % (ordre.ID, ordre.tekst,  ordre.firma)
        self.fakturaSendepostBoks.show()
        self.fakturaSendepostTittel.setText(u'Sender faktura til %s <b>&lt;%s</b>&gt;' % (ordre.kunde.navn, ordre.kunde.epost))
        self.fakturaSendepostTekst.setText(u'Vedlagt følger epostfaktura #%i:\n%s\n\n-- \n%s\n%s' % (ordre.ID, ordre.tekst,  ordre.firma, ordre.firma.vilkar))
        self.fakturaSendepostBoks.ordre = ordre
        self.fakturaSendepostBoks.pdfFilnavn = pdfFilnavn
        
        
    def sendEpostfaktura(self):
        try:
            self.faktura.sendEpost(self.fakturaSendepostBoks.ordre, self.fakturaSendepostBoks.pdfFilnavn, unicode(self.fakturaSendepostTekst.text()))
            #self.fakturaSendepostBoks.ordre.sendt = time() # logg tid for sending

        except:
            self.alert('Feil ved sending av faktura!\n%s' % sys.exc_info()[1])
        else:
            self.fakturaSendepostBoks.hide()
            self.obs('Fakturaen er sendt')
    
################## KUNDER ###########################

    def lukkKundeinfo(self, *ev):self.kundeInfo.hide()
    
    def kundeContextMenu(self, event):
        try:
            kunde = self.kundeKundeliste.selectedItem().kunde
        except AttributeError:
            return None # ingen kunde er valgt i lista
        meny = QPopupMenu(self)
        tittel = QLabel("<b>Rediger kunde</b>", self)
        tittel.setAlignment(Qt.AlignCenter)
        meny.insertItem(tittel)
        if not kunde.slettet:
            meny.insertItem(u"Redigér", self.redigerKunde)
            meny.insertItem("Slett", self.slettKunde)
        else:
            meny.insertItem("Ikke slettet", self.ikkeSlettKunde)
        meny.exec_loop(QCursor.pos())

    def visKunder(self):
        visFjernede = self.kundeVisFjernede.isChecked()
        self.kundeDetaljerTekst.setText('')
        self.kundeInfo.hide()
        i = self.kundeKundeliste.insertItem
        self.kundeKundeliste.clear()
        for kunde in self.faktura.hentKunder(inkluderSlettede=visFjernede):
            l = QListViewItem(self.kundeKundeliste,
                              "%03d" % kunde.ID,
                              '%s' % kunde.navn,
                              '%s' % kunde.epost,
                              '%s' % kunde.status,
                              "%s, %s %s" % (kunde.adresse, kunde.postnummer, kunde.poststed),
                              '%s' % kunde.telefon
                             )
            l.kunde = kunde
            if kunde.slettet: 
                l.setPixmap(0, self.slettetLogo)
            i(l)

    def redigerKunde(self, *kw):
        kunde = self.kundeKundeliste.currentItem().kunde
        self.lastKunde(kunde)

    def lastKunde(self, kunde = None):
        self.denne_kunde = kunde
        statuser = self.faktura.hentEgenskapVerdier("Kunde", "status")
        self.kundeInfoStatus.clear()
        self.kundeInfoStatus.insertStrList(statuser)

        if kunde is not None: #redigerer eksisterende kunde
            self.kundeInfoNavn.setText(kunde.navn)
            self.kundeInfoKontaktperson.setText(unicode(kunde.kontaktperson))
            self.kundeInfoEpost.setText(unicode(kunde.epost))
            self.kundeInfoStatus.setCurrentText(unicode(kunde.status))
            self.kundeInfoAdresse.setText(unicode(kunde.adresse))
            self.kundeInfoPoststed.setText(unicode(kunde.poststed))
            self.kundeInfoPostnummer.setText(str(kunde.postnummer))
            self.kundeInfoTelefon.setText(str(kunde.telefon))
            self.kundeInfoTelefaks.setText(str(kunde.telefaks))
            self.kundeInfoEndre.setText("Oppdate&r")
        else: # ny kunde - tømmer skjemaet helt
            self.kundeInfoNavn.setText("")
            self.kundeInfoKontaktperson.setText("")
            self.kundeInfoEpost.setText("")
            self.kundeInfoStatus.setCurrentItem(0)
            self.kundeInfoAdresse.setText("")
            self.kundeInfoPoststed.setText("")
            self.kundeInfoPostnummer.setText("")
            self.kundeInfoTelefon.setText("")
            self.kundeInfoTelefaks.setText("")
            self.kundeInfoEndre.setText("&Legg inn")

        self.kundeInfo.show()
        self.kundeInfoNavn.setFocus()

    def leggTilKunde(self):
        k = self.denne_kunde
        
        # sjekk om all nødvendig info er gitt
        kravkart = {self.kundeInfoNavn: "Kundens navn",
                    self.kundeInfoKontaktperson: "Kontaktperson",
                    self.kundeInfoEpost:"Epostadresse",
                    self.kundeInfoAdresse: "Adresse",
                    self.kundeInfoPoststed: "Poststed",
                    }
        for obj in kravkart.keys():
            if not obj.text():
                self.alert(u'Du er nødt til å oppgi %s' % (kravkart[obj].lower()))
                obj.setFocus()
                return False
                    
        if k is None:
            #debug("registrerer ny kunde")
            k = self.faktura.nyKunde()
        else:
            debug("oppdaterer kunde, som var " + unicode(k))
        k.navn = self.kundeInfoNavn.text() 
        k.kontaktperson = self.kundeInfoKontaktperson.text()
        k.epost = self.kundeInfoEpost.text()
        k.status = self.kundeInfoStatus.currentText()
        k.adresse = self.kundeInfoAdresse.text()
        k.poststed = self.kundeInfoPoststed.text()
        k.postnummer = self.kundeInfoPostnummer.text()
        k.telefon = self.kundeInfoTelefon.text()
        k.telefaks = self.kundeInfoTelefaks.text()
        self.kundeInfo.hide()
        self.visKunder()

    def visKundedetaljer(self, linje):
        s = "<p><b>%s</b></p>" % unicode(linje.kunde)
        if linje.kunde.slettet:
            s += '<p><b><font color=red>Fjernet %s</font></b>' % strftime('%Y-%m-%d', localtime(linje.kunde.slettet))
        s += "<p><i>Historikk:</i><br>"
        fakturaer = linje.kunde.finnOrdrer()
        if not fakturaer:
            s += "Aldri fakturert"
            self.kundeDetaljerTekst.setText(s)
            return
            
        s += "Sist fakturert: %s<br>" % strftime('%Y-%m-%d', localtime(fakturaer[-1].ordredato))
        s += "Antall fakturaer: %i<br>" % len(fakturaer)
        verdi = 0.0
        innbetaling = 0.0
        punktlig = 0.0
        forfalte = []
        forfalt_betalt = 0
        forfalt_ikkebetalt = 0
        forfalt_sentbetalt = 0
        ny_betalt = 0
        ny_ubetalt = 0
        ubetalte = []
        nu = time()
        for f in fakturaer:
            verdi += f.finnPris()
            if f.betalt: innbetaling += f.finnPris()
            if nu > f.forfall:
                if f.betalt > f.forfall:
                    forfalt_sentbetalt += 1
                    #print "ordre forfalt og betalt for sent:",f._id 
                elif not f.betalt:
                    forfalt_ikkebetalt += 1
                    #print "ordre forfalt og ikke betalt:",f._id
                    forfalte.append(f)
                else:
                    #print "ordre forfalt og betalt før fristen:",f._id
                    forfalt_betalt += 1
            else: 
                if not f.betalt:
                    #print "ordre ikke forfalt og ikke betalt:",f._id
                    ny_ubetalt += 1
                    ubetalte.append(f)
                else:
                    #print "ordre ikke forfalt, men betalt:",f._id
                    ny_betalt += 1
            
        s += "Samlet verdi: %i kr<br>" % verdi
        s += "Samlet innbetaling: %i kr<br>" % innbetaling
        # er kunden punktlig?
        # finn ut hvor mange fakturaer som er betalt før forfall
        # TODO: mer avansert, ta høyde for antall dager, purring etc
        # og komme opp med en karakter
        debug("kunde#%i: fakturaer som er betalt før forfall: %i - etter forfall eller aldri: %i" %\
            (linje.kunde._id, ny_betalt+forfalt_betalt, forfalt_sentbetalt+forfalt_ikkebetalt))
        korpus = float(ny_betalt+forfalt_betalt+forfalt_sentbetalt+forfalt_ikkebetalt)
        if korpus == 0.0:
            punktlighet = 0
        else:
            betalt_for_fristen = float(ny_betalt + forfalt_betalt)
            punktlighet = betalt_for_fristen / korpus 
        s += "Punktlighet: %i%%<br>" % int(punktlighet * 100)
        
        if forfalte:
            #alle forfalte fakturaer - de som har gått utover fristen
            s += '<p><i>Forfalte fakturaer:</i><br><ul>'
            forfaltverdi = 0.0
            for ff in forfalte:
                forfaltverdi += ff.finnPris()
                s += '<li>#%i: %s' % (ff._id, ff.tekst)
            s += '</ul>%i forfalte fakturaer<br>' % len(forfalte)
            s += '<font color=red>Verdi: %.2f</font>' % forfaltverdi
        
        if ubetalte:
            #alle ubetalte (men ikke forfalte) fakturaer 
            s += '<p><i>Utest&aring;ende fakturaer:</i><br><ul>'
            ubetaltverdi = 0.0
            for uf in ubetalte:
                ubetaltverdi += uf.finnPris()
                s += '<li>#%i: %s' % (uf._id, uf.tekst)
            s += '</ul>%i ubetalte fakturaer<br>' % len(ubetalte)
            s += 'Verdi: %.2f' % ubetaltverdi
        self.kundeDetaljerTekst.setText(s)

    def slettKunde(self):
        kunde = self.kundeKundeliste.selectedItem().kunde
        debug("Sletter kunde # %i" % kunde.ID)
        if self.JaNei("Vil du virkelig slette kunde nr %s (%s)?" % (kunde.ID, kunde.navn)):
            kunde.settSlettet()
            self.visKunder()

    def ikkeSlettKunde(self):
        kunde = self.kundeKundeliste.selectedItem().kunde
        debug("Fjerner slettet status for kunde # %i" % kunde.ID)
        kunde.settSlettet(False)
        self.visKunder()

################## VARER #########################

    def lukkVarerinfo(self, *ev):self.varerInfo.hide()
    
    def vareContextMenu(self, event):
        try:
            vare = self.varerVareliste.selectedItem().vare
        except AttributeError:
            return None # ingen kunde er valgt i lista
        meny = QPopupMenu(self)
        tittel = QLabel("<b>Rediger vare</b>", self)
        tittel.setAlignment(Qt.AlignCenter)
        meny.insertItem(tittel)
        if not vare.slettet:
            meny.insertItem(u"Redigér", self.redigerVare)
            meny.insertItem("Slett", self.slettVare)
        else:
            meny.insertItem("Ikke slettet", self.ikkeSlettVare)
        meny.exec_loop(QCursor.pos())

    def visVarer(self):
        visFjernede = self.varerVisFjernede.isChecked()
        self.varerDetaljerTekst.setText('')
        self.varerInfo.hide()
        i = self.varerVareliste.insertItem
        self.varerVareliste.clear()
        for vare in self.faktura.hentVarer(inkluderSlettede=visFjernede):
            l = QListViewItem(self.varerVareliste,
                              "%03d" % vare.ID,
                              vare.navn,
                              vare.detaljer,
                              "%.2f" % vare.pris,
                              vare.enhet
                             )
            l.vare = vare
            if vare.slettet: 
                l.setPixmap(0, self.slettetLogo)
            i(l)

    def redigerVare(self, linje = None, koord = None, kolonne = None):
        self.lastVare(self.varerVareliste.currentItem().vare)

    def lastVare(self, vare = None):
        self.denne_vare = vare
        enheter = self.faktura.hentEgenskapVerdier("Vare", "enhet")
        self.varerInfoEnhet.clear()
        self.varerInfoEnhet.insertStrList(enheter)
        if vare is not None:
            self.varerInfoNavn.setText(vare.navn)
            self.varerInfoDetaljer.setText(vare.detaljer)
            self.varerInfoEnhet.setCurrentText(vare.enhet)
            self.varerInfoPris.setValue(int(vare.pris))
            self.varerInfoPris.setSuffix(" kr per %s" % vare.enhet)
            self.varerInfoMva.setValue(int(vare.mva))
        else:
            self.varerInfoNavn.setText("")
            self.varerInfoDetaljer.setText("")
            self.varerInfoEnhet.setCurrentText("")
            self.varerInfoPris.setValue(0)
            self.varerInfoPris.setSuffix("")
            self.varerInfoMva.setValue(int(self.firma.mva))
        self.varerInfo.show()
        self.varerInfoNavn.setFocus()

    def registrerVare(self):
        v = self.denne_vare
        kravkart = {self.varerInfoNavn:"Varenavn",
                    self.varerInfoEnhet:"Enhet",
                    self.varerInfoPris:"Pris",
                    }
        for obj in kravkart.keys():
            if isinstance(obj, QSpinBox): test = obj.value() > 0
            elif isinstance(obj, QComboBox): test = obj.currentText()
            elif isinstance(obj, QLineEdit): test = obj.text()
            if not test:
                self.alert(u'Du er nødt til å oppgi %s' % (kravkart[obj].lower()))
                obj.setFocus()
                return False
                    
        if v is None:
            #debug("registrerer ny vare")
            v = self.faktura.nyVare()
        else:
            debug("oppdaterer vare, som var: " + unicode(v))
        #print self.varerInfoNavn.text.utf8
        v.navn = self.varerInfoNavn.text()
        v.detaljer = self.varerInfoDetaljer.text()
        v.enhet = self.varerInfoEnhet.currentText()
        v.pris = self.varerInfoPris.value()
        v.mva = self.varerInfoMva.value()
        self.varerInfo.hide()
        self.visVarer()

    def visVaredetaljer(self, linje):
        s = '<p><b>%s</b></p>' % unicode(linje.vare)
        if linje.vare.slettet:
            s += '<p><b><font color=red>Fjernet %s</font></b>' % strftime('%Y-%m-%d', localtime(linje.vare.slettet))
        salg = linje.vare.finnAntallSalg()
        if salg:
            s += u'<p><i>Kjøpes av:</i><br><ul>'
            for kunde in linje.vare.finnKjopere():
                s += '<li>%s' % unicode(kunde.navn)
            s += '</ul>Antall salg: %i<br>' % salg
            s += 'Sist fakturert: %s<br>' % strftime("%Y-%m-%d", localtime(linje.vare.finnSisteSalg().ordredato))
            s += u'Totalbeløp: %.2f kr' % linje.vare.finnTotalsalg()
        else:
            s += u'Aldri solgt'
        self.varerDetaljerTekst.setText(s)

    def slettVare(self, linje = None):
        vare = self.varerVareliste.selectedItem().vare
        debug("Sletter vare # %i" % vare._id)
        if self.JaNei("Vil du virkelig slette vare nr %s (%s)?" % (vare.ID, vare.navn)):
            vare.settSlettet()
            self.visVarer()
            
    def ikkeSlettVare(self):
        vare = self.varerVareliste.selectedItem().vare
        vare.settSlettet(False)
        self.visVarer()

############## FIRMAINFO ###################

    def dittfirmaKontroller(self, o=None):
        k = {
            self.dittfirmaFirmanavn:'Firmanavn',
            self.dittfirmaOrganisasjonsnummer:u'Organisasjonsnummer fra Brønnøysund',
            self.dittfirmaKontaktperson:'Kontaktperson',
            self.dittfirmaEpost:'Epostadresse',
            self.dittfirmaAdresse:'Adresse',
            self.dittfirmaPostnummer:'Postnummer',
            self.dittfirmaPoststed:'Poststed',
            self.dittfirmaTelefon:'Telefonnummer',
            self.dittfirmaMobil:'Mobilnummer',
            self.dittfirmaKontonummer:'Kontonummer',
            #self.dittfirmaMva:'Momssats',
            self.dittfirmaForfall:'Forfallsperiode',
            self.dittfirmaFakturakatalog:'Lagringssted for fakturaer',
        }
        if o is None: return k
        else: return k[o]

    def visFirma(self):
        self.dittfirmaFirmanavn.setText(self.firma.firmanavn)
        try:
            self.dittfirmaOrganisasjonsnummer.setText(self.firma.organisasjonsnummer)
            self.dittfirmaKontaktperson.setText(self.firma.kontaktperson)
            self.dittfirmaEpost.setText(self.firma.epost)
            self.dittfirmaAdresse.setText(self.firma.adresse)
            if self.firma.postnummer:
                self.dittfirmaPostnummer.setText("%04i" % self.firma.postnummer)
            self.dittfirmaPoststed.setText(self.firma.poststed)
            self.dittfirmaTelefon.setText(str(self.firma.telefon))
            self.dittfirmaTelefaks.setText(str(self.firma.telefaks))
            self.dittfirmaMobil.setText(str(self.firma.mobil))
            self.dittfirmaKontonummer.setText(str(self.firma.kontonummer))
            self.dittfirmaVilkar.setText(self.firma.vilkar)
            self.dittfirmaMva.setValue(int(self.firma.mva))
            self.dittfirmaForfall.setValue(int(self.firma.forfall))
    
            self.dittfirmaFakturakatalog.setText(self.faktura.oppsett.fakturakatalog)
        except TypeError:
            # finnes ennå ikke
            pass
        
        self.visLogo()
        self.firmaSjekk()
        
    def visLogo(self):
        if not self.firma.logo: 
            self.dittfirmaFinnFjernLogo.setText('Finn logo')
            self.dittfirmaLogoPixmap.setPixmap(QPixmap())
        else:
            logo = QPixmap()
            #print self.firma.logo
            logo.loadFromData(self.firma.logo)
            self.dittfirmaLogoPixmap.setPixmap(logo)
            self.dittfirmaFinnFjernLogo.setText('Fjern logo')

    def oppdaterFirma(self):
        self.firma.firmanavn  = self.dittfirmaFirmanavn.text()
        self.firma.organisasjonsnummer = self.dittfirmaOrganisasjonsnummer.text()
        self.firma.kontaktperson = self.dittfirmaKontaktperson.text()
        self.firma.epost      = self.dittfirmaEpost.text()
        self.firma.adresse    = self.dittfirmaAdresse.text()
        self.firma.postnummer = self.dittfirmaPostnummer.text()
        self.firma.poststed   = self.dittfirmaPoststed.text()
        self.firma.telefon    = self.dittfirmaTelefon.text()
        self.firma.mobil      = self.dittfirmaMobil.text()
        self.firma.telefaks   = self.dittfirmaTelefaks.text()
        self.firma.kontonummer = self.dittfirmaKontonummer.text()
        self.firma.vilkar     = self.dittfirmaVilkar.text()
        self.firma.mva        = self.dittfirmaMva.value()
        self.firma.forfall    = self.dittfirmaForfall.value()
    
        self.faktura.oppsett.fakturakatalog = self.dittfirmaFakturakatalog.text()

        mangler = self.sjekkFirmaMangler()
        if mangler:
            mangel = u'Ufullstendige opplysninger. Du er nødt til å oppgi:\n%s' % ([ mangler[obj].lower() for obj in mangler.keys() ])
            self.alert(mangel)
            self.fakturaTab.showPage(self.fakturaTab.page(3))
            obj.setFocus()
            self.gammelTab = 3
            return False
        self.dittfirmaLagreInfo.setText('<font color=green><b>Opplysningene er lagret</b></font>')
        
    def sjekkFirmaMangler(self):
        m = []
        kravkart = self.dittfirmaKontroller()
        for obj in kravkart.keys():
            if isinstance(obj, QSpinBox): test = obj.value() > 0
            elif isinstance(obj, QComboBox): test = obj.currentText()
            elif isinstance(obj, (QLineEdit,QTextEdit,)): test = obj.text()
            if test: kravkart.pop(obj)
        return kravkart

    def firmaSjekk(self):
        mangler = 0
        s = u"<b><font color=red>Følgende felter må fylles ut:</font></b><ol>"
        ok = QColor('white')
        tom = QColor('red')
        for obj in self.dittfirmaKontroller().keys():
            if isinstance(obj, QSpinBox): test = obj.value() > 0
            elif isinstance(obj, QComboBox): test = obj.currentText()
            elif isinstance(obj, (QLineEdit,QTextEdit,)): test = obj.text()
            if test: 
                obj.setPaletteBackgroundColor(ok)
            else:
                s += u"<li>%s" % self.dittfirmaKontroller(obj)
                obj.setPaletteBackgroundColor(tom)
                mangler += 1
        if not mangler:
            self.dittfirmaLagreInfo.setText('')
            self.dittfirmaLagre.setEnabled(True) 
            return True
        else:
            s += "</ol>"
            self.dittfirmaLagreInfo.setText(s)
            self.dittfirmaLagre.setEnabled(False) 

    def finnFjernLogo(self):
        if self.firma.logo:
            self.firma.logo = ""
            self.visLogo()
        else:
            startdir = ""
            logo = QFileDialog.getOpenFileName(
                startdir, 
                'Bildefiler (*.png *.xpm *.jpg *.jpeg *.gif *.bmp *.ppm *.pgm *.pbm)',
                self, 
                "Velg logofil",
                "Velg bildefil for firmaets logo" 
                )
            if len(unicode(logo)) > 0:
                debug("Setter ny logo: %s" % logo)

                l = QPixmap()
                l.loadFromData(open(unicode(logo)).read())

                from finfaktura.ekstra import QBuffer
                stream = QBuffer()
                l.convertToImage().smoothScale(360,360, QImage.ScaleMax).save(stream, 'PNG')

                self.firma.logo = sqlite.encode(stream.getData())
                self.visLogo()
        

    def endreFakturakatalog(self):
        nu = self.dittfirmaFakturakatalog.text()
        startdir = nu
        ny = QFileDialog.getExistingDirectory(startdir, self, "Velg katalog fakturaene skal lagres i", "Velg fakturakatalog")
        if len(unicode(ny)) > 0:
            print type(ny)
            debug("Setter ny fakturakataolg: %s" % ny)
            self.faktura.oppsett.fakturakatalog = unicode(ny)
            self.dittfirmaFakturakatalog.setText(unicode(ny))
            
############## Epost ###################

    def visEpost(self): 
        if not self.faktura.epostoppsett.smtpfra:
            self.faktura.epostoppsett.smtpfra = self.firma.epost
        self.epostAvsenderadresse.setText(self.faktura.epostoppsett.smtpfra)
        self.epostLosning.setButton(self.faktura.epostoppsett.transport)
        if BRUK_GMAIL:
            self.epostSeksjonGmail.setEnabled(True)
            self.epostGmailUbrukelig.hide()
            self.epostGmailEpost.setText(self.faktura.epostoppsett.gmailbruker)
            self.epostGmailPassord.setText(self.faktura.epostoppsett.gmailbruker)
            #self.epostGmailHuskEpost.setChecked(True)

    def oppdaterEpost(self):
        debug("lagrer epost")
        self.faktura.epostoppsett.transport = self.epostLosning.selectedId()
        self.faktura.epostoppsett.smtpfra = self.epostAvsenderadresse.text()
        self.faktura.epostoppsett.gmailbruker = self.epostGmailEpost.text()
        self.faktura.epostoppsett.gmailpassord = self.epostGmailPassord.text()
        self.faktura.epostoppsett.smtpserver = self.epostSmtpServer.text()
        self.faktura.epostoppsett.smtpport = self.epostSmtpPort.value()
        self.faktura.epostoppsett.smtpbruker = self.epostSmtpBruker.text()
        self.faktura.epostoppsett.smtppassord = self.epostSmtpPassord.text()
        self.faktura.epostoppsett.sendmailsti= self.epostSendmailSti.text()

############## ØKONOMI ###################

    def visOkonomi(self): pass
    
    def okonomiRegnRegnskap(self):
        debug("regner regnskap")
        inn = mva = 0.0
        b = u = 0
        #for ordre in self.faktura.hentOrdrer():
        ordreliste = fakturaOkonomi.ordreHenter(self.db)
        if self.okonomiAvgrensningerDato.isChecked():
            aar = self.okonomiAvgrensningerDatoAr.value()
            bmnd = self.okonomiAvgrensningerDatoManed.currentItem()
            if bmnd == 0: 
                bmnd = 1
                smnd = 12
            else:
                smnd = bmnd + self.okonomiAvgrensningerDatoPeriode.currentItem()
            beg = mktime((aar,bmnd,1,0,0,0,0,0,0))
            slutt = mktime((aar,smnd,31,0,0,0,0,0,0))
            debug("%s %s %s %s" % (bmnd, smnd, beg, slutt))
            ordreliste.begrensDato(beg, slutt)
        if self.okonomiAvgrensningerKunde.isChecked():
            krex = re.search(re.compile(r'kunde\ #\s?(\d+)'), 
                unicode(self.okonomiAvgrensningerKundeliste.currentText()))
            try:
                ordreliste.begrensKunde(self.faktura.hentKunde(int(krex.group(1))))
            except IndexError:
                raise
        if self.okonomiAvgrensningerVare.isChecked():
            #ordreliste.begrensVare()
            debug("Begrenser til vare:")
        ordreliste = ordreliste.hentOrdrer()
        s = "<b>Fakturaer funnet:</b><br><ul>"
        for ordre in ordreliste:
            s += "<li>"
            if ordre.kansellert:
                s += " <font color=red><b>Kansellert:</b></font> "
            elif ordre.betalt:
                s += " <font color=green>Betalt:</font> "
            else:
                s += " <font color=red>Ubetalt:</font> "
            s += unicode(ordre)
            if ordre.kansellert: 
                continue
            if ordre.betalt: 
                inn += ordre.finnPris()
                mva += ordre.finnMva()
                b += 1
            else:
                u += 1
        s += "</ul>"
        #self.myndigheteneRegnskapHittil.setText("%d kr (derav MVA %d kr)" % (inn+mva, mva))
        self.okonomiRegnskapTotalUMva.setText("%.2f kr" % inn)
        self.okonomiRegnskapTotalMMva.setText("%.2f kr" % (inn+mva))
        self.okonomiRegnskapMoms.setText("%.2f kr" % mva)
        self.okonomiRegnskapAntallFakturaer.setText("%i stk (%i ubetalte)" % (b, u))
        #skriv detaljer om ordrer
        self.okonomiDetaljregnskap.setText(s)

    def okonomiFyllDato(self, ibruk):
        self.okonomiAvgrensningerDatoAr.setEnabled(ibruk)
        self.okonomiAvgrensningerDatoManed.setEnabled(ibruk)
        self.okonomiAvgrensningerDatoPeriode.setEnabled(ibruk)
        #self.okonomiAvgrensningerDatoAr.setValue(2000)
        self.okonomiAvgrensningerDatoManed.clear()
        self.okonomiAvgrensningerDatoPeriode.clear()
        mnd = [u'Hele året', 'Januar', 'Februar', 'Mars', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Desember']
        in1 = self.okonomiAvgrensningerDatoManed.insertItem
        in2 = self.okonomiAvgrensningerDatoPeriode.insertItem
        for z in mnd: in1(z)
        in2(u'Velg periode:')
        for i in range(1,12): in2(u'Og %i måneder fram' % i)
        
    def okonomiFyllKunder(self, ibruk):
        self.okonomiAvgrensningerKundeliste.setEnabled(ibruk)
        self.okonomiAvgrensningerKundeliste.clear()
        i = self.okonomiAvgrensningerKundeliste.insertItem
        for kunde in self.faktura.hentKunder(inkluderSlettede=True):
            i(unicode(kunde))

    def okonomiFyllVarer(self, ibruk):
        self.okonomiAvgrensningerVareliste.setEnabled(ibruk)
        self.okonomiAvgrensningerVareliste.clear()
        i = self.okonomiAvgrensningerVareliste.insertItem
        for v in self.faktura.hentVarer(inkluderSlettede=True):
            i(unicode(v))
            
    def okonomiSkrivUtFakturaer(self):
        self.alert("funker ikke ennu")

############## MYNDIGHETER ###################

    def visMyndigheter(self):
        from finfaktura.myndighetene import myndighetene
        offentlige = myndighetene()

        debug("finner skjemaplikter for %s" % self.firma.organisasjonsnummer)
        self.myndigheteneSkjemaListe.clear()
        for skjema in offentlige.skjemaplikter(self.firma.organisasjonsnummer):
            i = QListViewItem(self.myndigheteneSkjemaListe, skjema[0],skjema[1],skjema[2],skjema[3])
            self.myndigheteneSkjemaListe.insertItem(i)




############## SIKKERHETSKOPI ###################

    def visSikkerhetskopi(self):
        
        if sikkerhetskopi.BRUK_GMAIL:
            self.sikkerhetskopiGmailUbrukelig.hide()
            self.sikkerhetskopiGmailLastopp.setEnabled(True)
        else:
            #self.sikkerhetskopiGmailUbrukelig.setText(u"Du må installere modulen 'libgmail' for å sikkerhetskopiere til Gmail")
            self.sikkerhetskopiGmailUbrukelig.show()
            self.sikkerhetskopiGmailLastopp.setEnabled(False)


    def sikkerhetskopiGmail(self):
        bruker = self.sikkerhetskopiGmailEpost.text()
        passord = self.sikkerhetskopiGmailPassord.text()
        if not (bruker and passord):
            self.alert(u'Du har ikke oppgitt brukernavn og passord i Gmail')
            return False
        if PRODUKSJONSVERSJON: label = "finfaktura"
        else: label = "test"
        sikker = sikkerhetskopi.gmailkopi(finnDatabasenavn(), bruker, passord, label)
        return sikker.lagre()

############## GENERELLE METODER ###################

    def alert(self, msg):
        QMessageBox.critical(self, "Feil!", msg, QMessageBox.Ok)

    def obs(self, msg):
        QMessageBox.information(self, "Obs!", msg, QMessageBox.Ok)

    def JaNei(self, s):
        svar = QMessageBox.question(self, "Hm?", s, QMessageBox.Yes, QMessageBox.No | QMessageBox.Default, QMessageBox.NoButton)
        return svar == QMessageBox.Yes


if __name__ == "__main__":

    DEBUG = "-d" in sys.argv[1:]

    if "-h" in sys.argv[1:]:
        print __doc__
        print "Bruk %s -i for å lage kommandolinjefaktura" % sys.argv[0]
        sys.exit()
    elif nogui or "-i" in sys.argv[1:]:
        #interactive"
        cli_faktura()
    else:
        a = QApplication(sys.argv)
        QObject.connect(a,SIGNAL('lastWindowClosed()'),a,SLOT('quit()'))
        f = Faktura()
        a.setMainWidget(f)
        f.show()
        a.exec_loop()
