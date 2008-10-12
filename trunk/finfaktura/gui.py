#!/usr/bin/python -d
# -*- coding:utf8 -*-
# kate: indent-width 4;
###########################################################################
#    Copyright (C) 2005-2008- Håvard Gulldahl og Håvard Sjøvoll
#    <havard@gulldahl.no>, <sjovoll@ntnu.no>
#
#    Lisens: GPL2
#
# $Id: faktura.py 260 2008-05-11 08:59:23Z havard.gulldahl $
#
###########################################################################


import sys, os.path, dircache, mimetypes, re
from string import join
from time import time, strftime, localtime, mktime
import logging

import finfaktura
from finfaktura.fakturabibliotek import PRODUKSJONSVERSJON, \
    FakturaBibliotek, kobleTilDatabase, lagDatabase, finnDatabasenavn, \
    sikkerhetskopierFil, lesRessurs
import finfaktura.f60 as f60
from finfaktura.epost import TRANSPORTMETODER
import finfaktura.okonomi as fakturaOkonomi
import finfaktura.sikkerhetskopi as sikkerhetskopi
import finfaktura.historikk as historikk
import finfaktura.rapport
import finfaktura.fakturakomponenter
from finfaktura.fakturafeil import *

from PyQt4 import QtCore, QtGui, uic
try:
    from finfaktura.ui.faktura_ui import Ui_FinFaktura
    import faktura_rc
    import gui_sendepost, gui_epost, gui_finfaktura_oppsett, gui_firma
except ImportError, (e):
    raise RessurserManglerFeil(e)

PDFVIS = "/usr/bin/kpdf" # program for å vise PDF

class FinFaktura(QtGui.QMainWindow):#Ui_MainWindow): ## leser gui fra faktura_ui.py
    db = None
    denne_kunde = None
    denne_vare = None
    gammelTab = 0

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.gui = Ui_FinFaktura()
        self.gui.setupUi(self)
        self.show()

        if not PRODUKSJONSVERSJON:
            self.setWindowTitle("FRYKTELIG FIN FADESE (utviklerversjon)")

        self.gui.actionSikkerhetskopi.setEnabled(False)
        self.gui.actionLover_og_regler.setEnabled(False)
        # rullegardinmeny:
        QtCore.QObject.connect(self.gui.actionDitt_firma, QtCore.SIGNAL("activated()"), self.visFirmaOppsett)
        QtCore.QObject.connect(self.gui.actionEpost, QtCore.SIGNAL("activated()"), self.visEpostOppsett)
        QtCore.QObject.connect(self.gui.actionProgrammer, QtCore.SIGNAL("activated()"), self.visProgramOppsett)
        QtCore.QObject.connect(self.gui.actionOm_Finfaktura, QtCore.SIGNAL("activated()"), lambda: self.visTekstVindu('om'))
        QtCore.QObject.connect(self.gui.actionLisens, QtCore.SIGNAL("activated()"), lambda: self.visTekstVindu('lisens'))
        #QtCore.QObject.connect(self.gui.actionLover_og_regler, QtCore.SIGNAL("activated()"), self.visLover)
        #QtCore.QObject.connect(self.gui.actionSikkerhetskopi, QtCore.SIGNAL("activated()"), self.visSikkerhetskopi)

        # kontroller i faktura-vinudet
        QtCore.QObject.connect(self.gui.fakturaTab, QtCore.SIGNAL("currentChanged(QWidget*)"), self.skiftTab)

        QtCore.QObject.connect(self.gui.fakturaNy, QtCore.SIGNAL("clicked()"), self.nyFaktura)
#     QtCore.QObject.connect(self.fakturaFakturaliste, QtCore.SIGNAL("doubleClicked(QListViewItem*, const QtGui.QPoint&, int)"), self.redigerFaktura)
        QtCore.QObject.connect(self.gui.fakturaFaktaLegginn, QtCore.SIGNAL("clicked()"), self.leggTilFaktura)
        QtCore.QObject.connect(self.gui.fakturaFakturaliste, QtCore.SIGNAL("currentItemChanged (QTreeWidgetItem *,QTreeWidgetItem *)"), self.visFakturadetaljer)
        QtCore.QObject.connect(self.gui.fakturaVareliste, QtCore.SIGNAL("cellChanged(int,int)"), self.fakturaVarelisteSynk)
        QtCore.QObject.connect(self.gui.fakturaFaktaVareLeggtil, QtCore.SIGNAL("clicked()"), self.leggVareTilOrdre)
        #QtCore.QObject.connect(self.gui.fakturaFaktaVareFjern, QtCore.SIGNAL("clicked()"), self.fjernVareFraOrdre)
        QtCore.QObject.connect(self.gui.fakturaLagEpost, QtCore.SIGNAL("clicked()"), self.lagFakturaEpost)
        QtCore.QObject.connect(self.gui.fakturaLagPapir, QtCore.SIGNAL("clicked()"), self.lagFakturaPapir)
        QtCore.QObject.connect(self.gui.fakturaLagKvittering, QtCore.SIGNAL("clicked()"), self.visFakturaKvittering)
        QtCore.QObject.connect(self.gui.fakturaBetalt, QtCore.SIGNAL("clicked()"), self.betalFaktura)
        QtCore.QObject.connect(self.gui.fakturaVisKansellerte, QtCore.SIGNAL("toggled(bool)"), self.visFaktura)
        QtCore.QObject.connect(self.gui.fakturaVisGamle, QtCore.SIGNAL("toggled(bool)"), self.visFaktura)
        self.gui.fakturaFaktaKryss.mousePressEvent = self.lukkFakta

        # kontroller i kunde-vinduet
        QtCore.QObject.connect(self.gui.kundeNy, QtCore.SIGNAL("clicked()"), self.lastKunde)
        QtCore.QObject.connect(self.gui.kundeKundeliste, QtCore.SIGNAL("itemDoubleClicked (QTreeWidgetItem *,int)"), self.redigerKunde)
        QtCore.QObject.connect(self.gui.kundeInfoEndre, QtCore.SIGNAL("clicked()"), self.leggTilKunde)
        QtCore.QObject.connect(self.gui.kundeNyFaktura, QtCore.SIGNAL("clicked()"), self.nyFakturaFraKunde)
        QtCore.QObject.connect(self.gui.kundeKundeliste, QtCore.SIGNAL("currentItemChanged (QTreeWidgetItem *,QTreeWidgetItem *)"), self.visKundedetaljer)
        QtCore.QObject.connect(self.gui.kundeVisFjernede, QtCore.SIGNAL("toggled(bool)"), self.visKunder)
        self.gui.kundeInfoKryss.mousePressEvent = self.lukkKundeinfo

        #QtCore.QObject.connect(self.gui.varerVareliste, QtCore.SIGNAL("selected(const QtGui.QString&)"), self.nyFaktura)

        # kontroller i vare-vinduet
        QtCore.QObject.connect(self.gui.varerNy, QtCore.SIGNAL("clicked()"), self.lastVare)
        QtCore.QObject.connect(self.gui.varerVareliste, QtCore.SIGNAL("itemDoubleClicked (QTreeWidgetItem *,int)"), self.redigerVare)
        QtCore.QObject.connect(self.gui.varerInfoLegginn, QtCore.SIGNAL("clicked()"), self.registrerVare)
        QtCore.QObject.connect(self.gui.varerVareliste, QtCore.SIGNAL("currentItemChanged (QTreeWidgetItem *,QTreeWidgetItem *)"), self.visVaredetaljer)
        QtCore.QObject.connect(self.gui.varerVisFjernede, QtCore.SIGNAL("toggled(bool)"), self.visVarer)
        self.gui.varerInfoKryss.mousePressEvent = self.lukkVarerinfo

        # kontroller i økonomi-vinduet

        QtCore.QObject.connect(self.gui.okonomiAvgrensningerDatoManed, QtCore.SIGNAL("highlighted(int)"), self.okonomiFyllDatoPeriode)
        QtCore.QObject.connect(self.gui.okonomiAvgrensningerDato, QtCore.SIGNAL("toggled(bool)"), self.okonomiFyllDato)
        QtCore.QObject.connect(self.gui.okonomiAvgrensningerKunde, QtCore.SIGNAL("toggled(bool)"), self.okonomiFyllKunder)
        QtCore.QObject.connect(self.gui.okonomiAvgrensningerVare, QtCore.SIGNAL("toggled(bool)"), self.okonomiFyllVarer)
        QtCore.QObject.connect(self.gui.okonomiSorter, QtCore.SIGNAL("toggled(bool)"), self.okonomiFyllSortering)
        QtCore.QObject.connect(self.gui.okonomiRegnskapRegnut, QtCore.SIGNAL("clicked()"), self.okonomiRegnRegnskap)
        QtCore.QObject.connect(self.gui.okonomiFakturaerSkrivut, QtCore.SIGNAL("clicked()"), self.okonomiSkrivUtFakturaer)

        topplinje = self.gui.fakturaVareliste.horizontalHeader()
        topplinje.setResizeMode(0, QtGui.QHeaderView.Stretch)
        topplinje.setResizeMode(3, QtGui.QHeaderView.Fixed)
        topplinje.resizeSection(1, 100)
        topplinje.resizeSection(2, 100)
        topplinje.resizeSection(3, 85)

        self.gui.kundeKundeliste.contextMenuEvent = self.kundeContextMenu
        self.gui.fakturaFakturaliste.contextMenuEvent = self.fakturaContextMenu
        self.gui.varerVareliste.contextMenuEvent = self.vareContextMenu

        self.databaseTilkobler()

        self.fakturaForfaltIkon = QtGui.QIcon(':/pix/important.svg')
        self.slettetIkon = QtGui.QIcon(':/pix/stop.svg')

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
            self.faktura = FakturaBibliotek(self.db)
            self.firma   = self.faktura.firmainfo()
            self.obs(u"Dette er første gang du starter programmet.\nFør du kan legge inn din første faktura, \ner jeg nødt til å få informasjon om firmaet ditt.")
            self.visFirmaOppsett()
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
        if not self.faktura.oppsett.vispdf:
            self.faktura.oppsett.vispdf = PDFVIS
        finfaktura.rapport.PDFVIS = self.faktura.oppsett.vispdf
        finfaktura.fakturakomponenter.PDFVIS = self.faktura.oppsett.vispdf

        self.skiftTab(0)
        self.resize(880, 600)

    def avslutt(self):
        logging.debug("sikkerhetskopierer databasen: %s ", finnDatabasenavn())
        sikkerhetskopierFil(finnDatabasenavn())
        self.db.commit()
        #self.c.close()
        #self.db.close()

    def databaseTilkobler(self):
        self.db = kobleTilDatabase()
        self.c = self.db.cursor()

    def skiftTab(self, w):
        i = self.gui.fakturaTab.currentIndex()
        if i is 0: self.visFaktura()
        elif i is 1: self.visKunder()
        elif i is 2: self.visVarer()
        elif i is 3: self.visOkonomi()
        elif i is 4: self.visFirma()
        self.gammelTab = i

################## FAKTURA ########################

    def lukkFakta(self, *ev):
        self.gui.fakturaFakta.hide()
        self.gui.fakturaHandlinger.show()
        self.gui.fakturaDetaljer.show()
        self.gui.fakturaFakturaliste.show()

    def fakturaContextMenu(self, event):
        try:
            ordre = self.gui.fakturaFakturaliste.selectedItems()[0].ordre
        except IndexError:
            return None #ingen ordre er valgt
        meny = QtGui.QMenu(self)
        meny.setTitle(u"Redigér faktura")
        if not ordre.betalt:
            meny.addAction("Er betalt", self.betalFaktura)
            #meny.addAction("Send purring", self.purrFaktura)
            #meny.addAction("Send til inkasso", self.inkassoFaktura)
        else:
            meny.addAction("Ikke betalt", self.avbetalFaktura)
        if not ordre.kansellert:
            meny.addAction(u"Kansellér", self.kansellerFaktura)
        else:
            meny.addAction("Ikke kansellert", self.avkansellerFaktura)
        meny.addAction("Vis kvittering", self.visFakturaKvittering)
        #meny.addAction("Dupliser", self.dupliserFaktura)
        meny.exec_(event.globalPos())

    def visFaktura(self):
        visKansellerte = self.gui.fakturaVisKansellerte.isChecked()
        visGamle = self.gui.fakturaVisGamle.isChecked()
        self.gui.fakturaDetaljerTekst.setText('')
        self.gui.fakturaFakta.hide()
        self.gui.fakturaHandlinger.show()
        self.gui.fakturaDetaljer.show()
        self.gui.fakturaFakturaliste.show()
        i = self.gui.fakturaFakturaliste.addTopLevelItem
        self.gui.fakturaFakturaliste.clear()
        nu = time()
        for ordre in self.faktura.hentOrdrer():
            if not visKansellerte and ordre.kansellert: continue
            if not visGamle and ordre.betalt and ordre.ordredato < nu-60*60*24*7*4*6: continue # eldre enn seks mnd og betalt
            if ordre.betalt: bet = strftime("%Y-%m-%d %H:%M", localtime(ordre.betalt))
            else: bet = "Nei"
            l = QtGui.QTreeWidgetItem([
                              "%06d" % ordre.ID,
                              '%s' % ordre.tekst,
                              '%s' % ordre.kunde.navn,
                              "%.2f kr" % (ordre.finnPris() + ordre.finnMva()),
                              strftime("%Y-%m-%d %H:%M", localtime(ordre.forfall)),
                              bet,
                              ]
                             )
            l.ordre = ordre
            if ordre.forfalt():
                logging.debug("%s er forfalt men ikke betalt!" % ordre._id)
                l.setIcon(5, self.fakturaForfaltIkon)
            if bool(ordre.kansellert):
                l.setIcon(0, self.slettetIkon)
            i(l)
        self.gui.fakturaBetaltDato.setDate(QtCore.QDate.currentDate())
        for col in range(0, self.gui.fakturaFakturaliste.columnCount()):
            logging.debug("resizeing column # %i", col)
            self.gui.fakturaFakturaliste.resizeColumnToContents(col)

    def nyFakturaFraKunde(self):
        try:
            kunde = self.gui.kundeKundeliste.selectedItems()[0].kunde
        except IndexError:
            self.alert(u'Ingen kunde er valgt')
            return False
        logging.debug("ny faktura fra kunde: %s" % kunde.ID)
        self.gui.fakturaTab.setCurrentIndex(0)
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
            self.visFirmaOppsett()
            return False
        if kunde is not None:
            self.gui.fakturaFaktaMottaker.clear()
            self.gui.fakturaFaktaMottaker.addItem(unicode(kunde), QtCore.QVariant(kunde))
            self.gui.fakturaVareliste.setFocus()
        else:
            self.gui.fakturaFaktaMottaker.setEnabled(True)
            self.gui.fakturaFaktaMottaker.clear()
            kunder = 0
            for k in self.faktura.hentKunder():
                self.gui.fakturaFaktaMottaker.addItem(unicode(k), QtCore.QVariant(k))
                kunder += 1
            if kunder == 0: # ingen kunder registrert
                self.gui.fakturaTab.setCurrentIndex(1)
                self.lastKunde()
                self.alert(u'Du må registrere minst én kunde før du fyller inn fakturaen')
                return
            self.gui.fakturaFaktaMottaker.setFocus()
        self.gui.fakturaFaktaTekst.setPlainText("")
        self.gui.fakturaVareliste.clearContents()
        self.leggVareTilOrdre(rad=0) # legg til tom rad
        self.gui.fakturaFaktaDato.setDate(QtCore.QDate.currentDate())
        self.gui.fakturaFaktaLeveringsdato.setDate(QtCore.QDate.currentDate())
        self.gui.fakturaFaktaLeveringsdato.setEnabled(False)
        forfall = QtCore.QDate(QtCore.QDate.currentDate())
        self.gui.fakturaFaktaForfall.setDate(forfall.addDays(self.firma.forfall))
        self.gui.fakturaHandlinger.hide()
        self.gui.fakturaFaktaOverstyr.setChecked(False)
        self.gui.fakturaAlternativer.hide()
        self.gui.fakturaDetaljer.hide()
        self.gui.fakturaFakta.show()

    def leggTilFaktura(self):
        #legg inn faktura i registeret
        #er all nødvendig info samlet inn?
        if not len(unicode(self.gui.fakturaFaktaTekst.toPlainText())) and \
            not self.JaNei(u"Vil du virkelig legge inn fakturaen uten fakturatekst?"):
            self.gui.fakturaFaktaTekst.setFocus()
            return False
        if self.gui.fakturaFaktaDato.date() > self.gui.fakturaFaktaForfall.date():
            self.gui.fakturaAlternativer.show()
            self.gui.fakturaFaktaForfall.setFocus()
            self.alert(u"Forfallsdato kan ikke være tidligere enn fakturadato")
            return False
        kunde = self.gui.fakturaFaktaMottaker.itemData(self.gui.fakturaFaktaMottaker.currentIndex()).toPyObject()
        d = self.gui.fakturaFaktaDato.date()
        dato = mktime((d.year(),d.month(),d.day(),11,59,0,0,0,0)) # på midten av dagen (11:59) for å kunne betale fakturaen senere laget samme dag
        fd = self.gui.fakturaFaktaForfall.date()
        fdato = mktime((fd.year(),fd.month(),fd.day(),11,59,0,0,0,0))
        f = self.faktura.nyOrdre(kunde, ordredato=dato, forfall=fdato)
        f.tekst = unicode(self.gui.fakturaFaktaTekst.toPlainText())
        #finn varene som er i fakturaen
        varer = {}
        for i in range(self.gui.fakturaVareliste.rowCount()): # gå gjennom alle rader
            v = {'id': None, 'ant': 0, 'pris': 0.0, 'mva': 0}
            _tekst  = unicode(self.gui.fakturaVareliste.cellWidget(i, 0).currentText()).strip()
            v['ant'] = self.gui.fakturaVareliste.cellWidget(i, 1).value()
            _enhet = unicode(self.gui.fakturaVareliste.cellWidget(i, 1).suffix()).strip()
            v['pris'] = float(self.gui.fakturaVareliste.cellWidget(i, 2).value())
            v['mva'] = int(self.gui.fakturaVareliste.cellWidget(i, 3).value())
            # sjekk at alt er riktig
            if not v['ant'] > 0:
                self.alert(u'Antallet %s kan ikke være null (i rad %s) ' % (_tekst, i+1))
                return False
            if not v['pris'] > 0.0:
                self.alert(u'Prisen kan ikke være null (i rad %s) ' % (i+1))
                return False
            # hvilken vare er dette?
            vare = self.faktura.finnVareEllerLagNy(_tekst, v['pris'], v['mva'], _enhet)
            logging.debug("fant vare i fakturaen: %s -> %s", unicode(v), unicode(vare))
            # er dette en duplikatoppføring?
            if varer.has_key(vare.ID) and varer[v['id']]['mva'] == v['mva'] \
                and varer[v['id']]['pris'] == v['pris']:
                # den samme varen, med samme pris og mva, er lagt inn tidligere
                if self.JaNei(u'Du har lagt inn %s mer enn én gang. Vil du slå sammen oppføringene?' % _tekst):
                    varer[v['id']]['ant'] += v['ant']
            #legg varen til den interne listen (for duplikatokontroll)
            varer[v['id']] = v
            #legg varen til fakturaen
            f.leggTilVare(vare, v['ant'], v['pris'], v['mva'])

        logging.debug("legger inn faktura: %s " % unicode(f))
        logging.debug("Lager sikkerhetskopi")
        self.faktura.lagSikkerhetskopi(f)
        self.gui.fakturaFakta.hide()
        self.visFaktura() # oppdater listen slik at den nye fakturaen blir med
        try:
            # velg den nye fakturaen - søk etter den nye fakturaens ID i lista
            nylinje = self.gui.fakturaFakturaliste.findItems("%06d" % f.ID, QtCore.Qt.MatchExactly, 0)[0]
            self.gui.fakturaFakturaliste.setCurrentItem(nylinje)
        except IndexError:
            pass

        #skal vi lage blanketter nå?
        s = u'Den nye fakturaen er laget. Vil du lage tilhørende blankett nå?'
        knapp = QtGui.QMessageBox.information(self, u'Lage blankett?', s, 'Epost', 'Papir', 'Senere', 0, 2)
        if knapp == 0: self.lagFaktura(Type='epost')
        elif knapp == 1: self.lagFaktura(Type='papir')

#   def redigerFaktura(self, rad, koord, kolonne):
#     linje = {}
#     for (ant, vare) in map(lambda x:(x.kvantum, x.vare), rad.ordre.linje):
#       linje[vare] = ant
# #     self.nyFaktura(kunde = rad.ordre.kunde, ordrelinje = linje)
#     self.nyFaktura(ordre = rad.ordre, ordrelinje = linje)

    def leggVareTilOrdre(self, rad=None):
        if rad is None:
            rad = self.gui.fakturaVareliste.rowCount()
        Antall = QtGui.QDoubleSpinBox(self.gui.fakturaVareliste)
        Antall.setMaximum(100000.0)
        Antall.setValue(0.0)
        Antall.setDecimals(1)
        Antall.show()
        Antall.setToolTip(u'Antall varer levert')
        QtCore.QObject.connect(Antall, QtCore.SIGNAL("valueChanged(double)"),
            lambda x: self.fakturaVarelisteSynk(rad, 1))

        Pris = QtGui.QDoubleSpinBox(self.gui.fakturaVareliste)
        Pris.setButtonSymbols(QtGui.QDoubleSpinBox.UpDownArrows)
        Pris.setMaximum(999999999.0)
        Pris.setDecimals(2)
        Pris.setSuffix(' kr')
        Pris.show()
        Pris.setToolTip(u'Varens pris (uten MVA)')
        QtCore.QObject.connect(Pris, QtCore.SIGNAL("valueChanged(double)"),
            lambda x: self.fakturaVarelisteSynk(rad, 2))

        Mva = QtGui.QDoubleSpinBox(self.gui.fakturaVareliste)
        Mva.setButtonSymbols(QtGui.QDoubleSpinBox.UpDownArrows)
        Mva.setValue(25)
        Mva.setSuffix(' %')
        Mva.show()
        Mva.setToolTip(u'MVA-sats som skal beregnes på varen')
        QtCore.QObject.connect(Mva, QtCore.SIGNAL("valueChanged(double)"),
            lambda x: self.fakturaVarelisteSynk(rad, 3))

        Vare = QtGui.QComboBox(self.gui.fakturaVareliste)
        for v in self.faktura.hentVarer():
            Vare.addItem(unicode(v.navn), QtCore.QVariant(v))
        Vare.setEditable(True)
        Vare.setAutoCompletion(True)
        Vare.show()
        Vare.setToolTip(u'Velg vare; eller skriv inn nytt varenavn og trykk <em>enter</em> for å legge til en ny vare')
        QtCore.QObject.connect(Vare, QtCore.SIGNAL("activated(int)"),
            lambda x: self.fakturaVarelisteSynk(rad, 0))


        self.gui.fakturaVareliste.setRowCount(rad+1)
        self.gui.fakturaVareliste.setCellWidget(rad, 0, Vare)
        self.gui.fakturaVareliste.setCellWidget(rad, 1, Antall)
        self.gui.fakturaVareliste.setCellWidget(rad, 2, Pris)
        self.gui.fakturaVareliste.setCellWidget(rad, 3, Mva)
        return self.fakturaVarelisteSynk(rad, 0)

    def fakturaVarelisteSynk(self, rad, kol):
        logging.debug("synk: %s, %s", rad, kol)
        sender = self.gui.fakturaVareliste.cellWidget(rad, kol)
        if kol == 0: # endret på varen -> oppdater metadata
            _vare = sender.itemData(sender.currentIndex())
            if _vare.isValid():
                vare = _vare.toPyObject()
            else:
                # ny vare, tøm andre felt
                logging.debug("ny vare opprettet: %s", unicode(sender.currentText()))
                self.gui.fakturaVareliste.cellWidget(rad, 1).setSuffix('')
                self.gui.fakturaVareliste.cellWidget(rad, 2).setValue(0.0)
                self.gui.fakturaVareliste.cellWidget(rad, 3).setValue(float(self.firma.mva))
                return
            self.gui.fakturaVareliste.cellWidget(rad, 1).setSuffix(' '+str(vare.enhet))
            self.gui.fakturaVareliste.cellWidget(rad, 2).setValue(float(vare.pris))
            self.gui.fakturaVareliste.cellWidget(rad, 3).setValue(float(vare.mva))
        else:
            # endret på antall, mva eller pris -> oppdater sum
            p = mva = 0.0
            for i in range(self.gui.fakturaVareliste.rowCount()):
                _antall = float(self.gui.fakturaVareliste.cellWidget(i, 1).value())
                _pris   = float(self.gui.fakturaVareliste.cellWidget(i, 2).value())
                _mva    = float(self.gui.fakturaVareliste.cellWidget(i, 3).value())
                p += _pris * _antall
                mva += _pris * _antall * _mva / 100
            self.gui.fakturaFaktaSum.setText("<u>%.2fkr (+%.2fkr mva)</u>" % (p, mva))

    def visFakturadetaljer(self, linje):
        if linje is None:
            self.gui.fakturaDetaljerTekst.setText('')
            self.gui.fakturaHandlinger.setEnabled(False)
            return
        self.gui.fakturaHandlinger.setEnabled(True)
        s = "<p><b>%s</b><p>" % unicode(linje.ordre.tekst)
        if linje.ordre.kansellert:
            s += '<b><font color=red>Denne fakturaen er kansellert</font></b><p>'
            self.gui.fakturaHandlinger.setEnabled(False)
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
        for logglinje in ():#ordre.hentHistorikk():
            s += "<i>%s:</i> %i<br>" % (strftime("%Y-%m-%d", localtime(logglinje.dato)), logglinje.info)
        self.gui.fakturaDetaljerTekst.setText(s)
        # oppdater datofeltet. minste dato er ordredato. største dato er i dag
        minst, maks = localtime(linje.ordre.ordredato), localtime()
        self.gui.fakturaBetaltDato.setDateRange(QtCore.QDate(minst[0]-1, minst[1], minst[2]), QtCore.QDate(maks[0]+1, maks[1], maks[2])) # utvider rangen med ett år i hver retning slik at QtGui.QDateEdit-kontrollen skal bli brukelig

    def visFakturaKvittering(self):
        try:
            ordre = self.gui.fakturaFakturaliste.selectedItems()[0].ordre
        except IndexError:
            self.alert(u'Ingen faktura er valgt')
            return False
        kvitt = ordre.hentSikkerhetskopi()
        kvitt.vis(program=self.faktura.oppsett.vispdf)

    def lagFakturaEpost(self): return self.lagFaktura(Type='epost')
    def lagFakturaPapir(self): return self.lagFaktura(Type='papir')

    def lagFaktura(self, Type="epost"):
        try:
            ordre = self.gui.fakturaFakturaliste.selectedItems()[0].ordre
        except IndexError:
            self.alert(u'Ingen faktura er valgt')
            return False
        ordre.firma = self.firma
        fakturanavn = ordre.lagFilnavn(self.faktura.oppsett.fakturakatalog, fakturatype=Type)
        try:
            pdf = f60.f60(fakturanavn)
            pdf.settFirmainfo(self.firma._egenskaper)
            pdf.settKundeinfo(ordre.kunde._id, ordre.kunde.postadresse())
            pdf.settFakturainfo(ordre._id, ordre.ordredato, ordre.forfall, ordre.tekst)
            pdf.settOrdrelinje(ordre.hentOrdrelinje)
        except f60.f60Eksisterer, (E):
            # HACK XXX: E er nå filnavnet
            if Type == "epost":
                self.visEpostfaktura(ordre, unicode(E))
            elif Type == "papir":
                if self.JaNei(u"Blanketten er laget fra før av. Vil du skrive den ut nå?"):
                    self.faktura.skrivUt(unicode(E), program=self.faktura.oppsett.vispdf)
            return None
        try:
            pdf.fyll()
        except FirmainfoFeil,(E):
            historikk.pdfEpost(ordre, False, "firmainfofeil: %s" % E)
            self.alert(u"Du må fylle ut firmainfo først:\n%s" % E)
            self.visFirmaOppsett()
            return
        except KundeFeil,(E):
            self.alert(u"Kan ikke lage PDF!\nÅrsak: %s" % E)
            historikk.pdfEpost(ordre, False, "kundefeil: %s" % E)
            return
        if Type == "epost":
            res = pdf.lagEpost()
        elif Type == "kvittering":
            res = pdf.lagKvittering()
        else:
            res = pdf.lagPost()
        if not res:
            historikk.pdfEpost(ordre, False, "ukjent grunn")
            self.alert("Kunne ikke lage PDF! ('%s')" % pdf.filnavn)
        else:
            if Type == "epost":
                historikk.pdfEpost(ordre, True, "interaktivt")
                self.visEpostfaktura(ordre, pdf.filnavn)
            elif Type == "papir":
                historikk.pdfPapir(ordre, True, "interaktivt")
                if self.JaNei(u"Blanketten er laget. Vil du skrive den ut nå?"):
                    suksess = pdf.skrivUt(program=self.faktura.oppsett.vispdf)
                    historikk.utskrift(ordre, suksess, "interaktivt")
                else: self.obs(u"Blanketten er lagret med filnavn: %s" % pdf.filnavn)

    def betalFaktura(self):
        try:
            ordre = self.gui.fakturaFakturaliste.selectedItems()[0].ordre
        except IndexError:
            self.alert("Ingen faktura er valgt")
            return
        if ordre.betalt:
            self.obs("Denne fakturaen er allerede betalt (%s)." % strftime("%Y-%m-%d", localtime(ordre.betalt)))
            return False
        if ordre.kansellert:
            self.obs("Denne fakturaen ble kansellert den %s, og kan ikke betales." % strftime("%Y-%m-%d", localtime(ordre.kansellert)))
            return False
        d = self.gui.fakturaBetaltDato.date()
        dato = mktime((d.year(),d.month(),d.day(),23,59,0,0,0,1)) # på slutten av dagen (23:59) for å kunne betale fakturaer laget tidligere samme dag
        if dato < ordre.ordredato:
            self.obs(u'Betalingsdato kan ikke være tidligere enn ordredato')
            return False
        ikveld = localtime()[0:3]+(23,59,0,0,0,1)
        if dato > mktime(ikveld):
            self.obs(u'Betalingsdato kan ikke være i fremtiden')
            return False
        ordre.betal(dato)
        historikk.betalt(ordre, True, 'brukerklikk')
        self.visFaktura()

    def avbetalFaktura(self):
        try:
            ordre = self.gui.fakturaFakturaliste.selectedItems()[0].ordre
        except IndexError:
            self.alert("Ingen faktura er valgt")
            return
        #if ordre.kansellert:
            #self.alert(u"Du kan ikke fjerne betaldenne ordren, den er betalt.")
        if self.JaNei(u"Vil du virkelig fjerne betalt-status på ordre nr %s?" % ordre.ID):
            ordre.fjernBetalt()
            historikk.avbetalt(ordre, True, 'brukerklikk')
            self.visFaktura()

    def kansellerFaktura(self):
        try:
            ordre = self.gui.fakturaFakturaliste.selectedItems()[0].ordre
        except IndexError:
            self.alert("Ingen faktura er valgt")
            return
        if ordre.betalt:
            self.alert(u"Du kan ikke kansellere denne ordren, den er betalt.")
        elif self.JaNei(u"Vil du virkelig kansellere ordre nr %s?" % ordre.ID):
            ordre.settKansellert()
            historikk.kansellert(ordre, True, 'brukerklikk')
            self.visFaktura()

    def avkansellerFaktura(self):
        try:
            ordre = self.gui.fakturaFakturaliste.selectedItems()[0].ordre
        except IndexError:
            self.alert("Ingen faktura er valgt")
            return
        ordre.settKansellert(False)
        historikk.avKansellert(ordre, True, 'brukerklikk')
        self.visFaktura()

    def purrFaktura(self):
        try:
            ordre = self.gui.fakturaFakturaliste.selectedItems()[0].ordre
        except IndexError:
            self.alert("Ingen faktura er valgt")
            return
        historikk.purret(ordre, True, 'brukerklikk')

    def inkassoFaktura(self):
        try:
            ordre = self.gui.fakturaFakturaliste.selectedItems()[0].ordre
        except IndexError:
            self.alert("Ingen faktura er valgt")
            return
        historikk.sendtTilInkasso(ordre, True, 'brukerklikk')

    def visEpostfaktura(self, ordre, pdfFilnavn):
        epostboks = gui_sendepost.sendEpost(self, ordre)
        res, tekst = epostboks.exec_()
        if res == QtGui.QDialog.Accepted:
          return self.sendEpostfaktura(ordre, tekst, pdfFilnavn)

    def sendEpostfaktura(self, ordre, tekst, filnavn):
        try:
            logging.debug('sender epostfaktura: ordre # %i, til: %s', ordre._id, ordre.kunde.epost)
            logging.debug('bruker transport %s' % TRANSPORTMETODER[self.faktura.epostoppsett.transport])
            self.faktura.sendEpost(ordre,
                                   filnavn,
                                   tekst,
                                   TRANSPORTMETODER[self.faktura.epostoppsett.transport]
                                   )
        except:
            f = sys.exc_info()[1]
            self.alert(u'Feil ved sending av faktura. Prøv å sende med en annen epostmetode.\n\nDetaljer:\n%s' % f)
            #historikk.epostSendt(ordre, 0, f) ## TODO: logg feilmelding
            raise
        else:
            historikk.epostSendt(ordre, True, "Tid: %s, transport: %s" % (time(), trans[self.faktura.epostoppsett.transport]))
            self.obs('Fakturaen er sendt')

################## KUNDER ###########################

    def lukkKundeinfo(self, *ev):self.gui.kundeInfo.hide()

    def kundeContextMenu(self, event):
        try:
            kunde = self.gui.kundeKundeliste.selectedItems()[0].kunde
        except IndexError:
            return None # ingen kunde er valgt i lista
        meny = QtGui.QMenu(self)
        meny.setTitle(u"Redigér kunde")
        if not kunde.slettet:
            meny.addAction(u"Redigér", self.redigerKunde)
            meny.addAction("Slett", self.slettKunde)
        else:
            meny.addAction("Ikke slettet", self.ikkeSlettKunde)
        meny.exec_(event.globalPos())

    def visKunder(self):
        visFjernede = self.gui.kundeVisFjernede.isChecked()
        self.gui.kundeDetaljerTekst.setText('')
        self.gui.kundeInfo.hide()
        i = self.gui.kundeKundeliste.addTopLevelItem
        self.gui.kundeKundeliste.clear()
        for kunde in self.faktura.hentKunder(inkluderSlettede=visFjernede):
            l = QtGui.QTreeWidgetItem([
                              "%03d" % kunde.ID,
                              '%s' % kunde.navn,
                              '%s' % kunde.epost,
                              '%s' % kunde.status,
                              "%s, %s %s" % (kunde.adresse, kunde.postnummer, kunde.poststed),
                              '%s' % kunde.telefon
                              ]
                             )
            l.kunde = kunde
            if kunde.slettet:
                l.setIcon(0, self.slettetIkon)
            i(l)

    def redigerKunde(self, *kw):
        kunde = self.gui.kundeKundeliste.currentItem().kunde
        self.lastKunde(kunde)

    def lastKunde(self, kunde = None):
        self.denne_kunde = kunde
        statuser = self.faktura.hentEgenskapVerdier("Kunde", "status")
        self.gui.kundeInfoStatus.clear()
        self.gui.kundeInfoStatus.addItems(statuser)

        if kunde is not None: #redigerer eksisterende kunde
            self.gui.kundeInfoNavn.setText(kunde.navn)
            self.gui.kundeInfoKontaktperson.setText(unicode(kunde.kontaktperson))
            self.gui.kundeInfoEpost.setText(unicode(kunde.epost))
            comboidx = self.gui.kundeInfoStatus.findText(unicode(kunde.status))
            if comboidx != 1: self.gui.kundeInfoStatus.setCurrentIndex(comboidx)
            self.gui.kundeInfoAdresse.setPlainText(unicode(kunde.adresse))
            self.gui.kundeInfoPoststed.setText(unicode(kunde.poststed))
            self.gui.kundeInfoPostnummer.setText(str(kunde.postnummer))
            self.gui.kundeInfoTelefon.setText(str(kunde.telefon))
            self.gui.kundeInfoTelefaks.setText(str(kunde.telefaks))
            self.gui.kundeInfoEndre.setText("Oppdate&r")
        else: # ny kunde - tømmer skjemaet helt
            self.gui.kundeInfoNavn.setText("")
            self.gui.kundeInfoKontaktperson.setText("")
            self.gui.kundeInfoEpost.setText("")
            self.gui.kundeInfoStatus.setCurrentIndex(0)
            self.gui.kundeInfoAdresse.setPlainText("")
            self.gui.kundeInfoPoststed.setText("")
            self.gui.kundeInfoPostnummer.setText("")
            self.gui.kundeInfoTelefon.setText("")
            self.gui.kundeInfoTelefaks.setText("")
            self.gui.kundeInfoEndre.setText("&Legg inn")

        self.gui.kundeInfo.show()
        self.gui.kundeInfoNavn.setFocus()

    def leggTilKunde(self):
        k = self.denne_kunde

        # sjekk om all nødvendig info er gitt
        kravkart = {self.gui.kundeInfoNavn: "Kundens navn",
                    self.gui.kundeInfoKontaktperson: "Kontaktperson",
                    self.gui.kundeInfoEpost:"Epostadresse",
                    self.gui.kundeInfoAdresse: "Adresse",
                    self.gui.kundeInfoPoststed: "Poststed",
                    }
        for obj in kravkart.keys():
            if hasattr(obj, 'text'): t = obj.text()
            elif hasattr(obj, 'toPlainText'): t = obj.toPlainText()
            if not len(t):
                self.alert(u'Du er nødt til å oppgi %s' % (kravkart[obj].lower()))
                obj.setFocus()
                return False

        if k is None:
            logging.debug("registrerer ny kunde")
            k = self.faktura.nyKunde()
        else:
            logging.debug("oppdaterer kunde, som var " + unicode(k))
        k.navn = unicode(self.gui.kundeInfoNavn.text()).strip()
        k.kontaktperson = unicode(self.gui.kundeInfoKontaktperson.text()).strip()
        k.epost = unicode(self.gui.kundeInfoEpost.text()).strip()
        k.status = unicode(self.gui.kundeInfoStatus.currentText()).strip()
        k.adresse = unicode(self.gui.kundeInfoAdresse.toPlainText()).strip()
        k.poststed = unicode(self.gui.kundeInfoPoststed.text()).strip()
        k.postnummer = self.gui.kundeInfoPostnummer.text()
        k.telefon = self.gui.kundeInfoTelefon.text()
        k.telefaks = self.gui.kundeInfoTelefaks.text()
        self.gui.kundeInfo.hide()
        self.visKunder()

    def visKundedetaljer(self, linje):
        if linje is None:
            self.gui.kundeDetaljerTekst.setText('')
            self.gui.kundeNyFaktura.setEnabled(False)
            return

        self.gui.kundeNyFaktura.setEnabled(True)
        s = "<p><b>%s</b></p>" % unicode(linje.kunde)
        if linje.kunde.slettet:
            s += '<p><b><font color=red>Fjernet %s</font></b>' % strftime('%Y-%m-%d', localtime(linje.kunde.slettet))
        s += "<p><i>Historikk:</i><br>"
        fakturaer = linje.kunde.finnOrdrer()
        if not fakturaer:
            s += "Aldri fakturert"
            self.gui.kundeDetaljerTekst.setText(s)
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
        logging.debug("kunde#%i: fakturaer som er betalt før forfall: %i - etter forfall eller aldri: %i" %\
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
        self.gui.kundeDetaljerTekst.setText(s)

    def slettKunde(self):
        try:
            kunde = self.gui.kundeKundeliste.selectedItems()[0].kunde
        except IndexError:
            return None # ingen kunde er valgt i lista
        logging.debug("Sletter kunde # %i" % kunde.ID)
        if self.JaNei("Vil du virkelig slette kunde nr %s (%s)?" % (kunde.ID, kunde.navn)):
            kunde.settSlettet()
            self.visKunder()

    def ikkeSlettKunde(self):
        try:
            kunde = self.gui.kundeKundeliste.selectedItems()[0].kunde
        except IndexError:
            return None # ingen kunde er valgt i lista
        logging.debug("Fjerner slettet status for kunde # %i" % kunde.ID)
        kunde.settSlettet(False)
        self.visKunder()

################## VARER #########################

    def lukkVarerinfo(self, *ev):self.gui.varerInfo.hide()

    def vareContextMenu(self, event):
        try:
            vare = self.gui.varerVareliste.selectedItems()[0].vare
        except IndexError:
            return None # ingen vare er valgt i lista
        meny = QtGui.QMenu(self)
        meny.setTitle(u"Redigér faktura")
        if not vare.slettet:
            meny.addAction(u"Redigér", self.redigerVare)
            meny.addAction("Slett", self.slettVare)
        else:
            meny.addAction("Ikke slettet", self.ikkeSlettVare)
        meny.exec_(event.globalPos())

    def visVarer(self):
        visFjernede = self.gui.varerVisFjernede.isChecked()
        self.gui.varerDetaljerTekst.setText('')
        self.gui.varerInfo.hide()
        i = self.gui.varerVareliste.addTopLevelItem
        self.gui.varerVareliste.clear()
        for vare in self.faktura.hentVarer(inkluderSlettede=visFjernede):
            if vare.pris is None: p = 0.0
            else: p = vare.pris
            l = QtGui.QTreeWidgetItem([
                              "%03d" % vare.ID,
                              unicode(vare.navn),
                              unicode(vare.detaljer),
                              "%.2f" % p,
                              unicode(vare.enhet)
                              ]
                             )
            l.vare = vare
            if vare.slettet:
                l.setIcon(0, self.slettetIkon)
            i(l)

    def redigerVare(self, linje = None, koord = None, kolonne = None):
        self.lastVare(self.gui.varerVareliste.currentItem().vare)

    def lastVare(self, vare = None):
        self.denne_vare = vare
        enheter = self.faktura.hentEgenskapVerdier("Vare", "enhet")
        self.gui.varerInfoEnhet.clear()
        self.gui.varerInfoEnhet.addItems(enheter)
        if vare is not None:
            self.gui.varerInfoNavn.setText(unicode(vare.navn))
            self.gui.varerInfoDetaljer.setPlainText(unicode(vare.detaljer))
            idx = self.gui.varerInfoEnhet.findText(unicode(vare.enhet))
            if idx != -1: self.gui.varerInfoEnhet.setCurrentIndex(idx)
            self.gui.varerInfoPris.setValue(int(vare.pris))
            if vare.enhet: sfx = unicode(" kr per %s" % vare.enhet)
            else: sfx = " kr"

            self.gui.varerInfoPris.setSuffix(sfx)
            self.gui.varerInfoMva.setValue(int(vare.mva))
            self.gui.varerInfoLegginn.setText('Oppda&ter')
        else:
            self.gui.varerInfoNavn.setText("")
            self.gui.varerInfoDetaljer.setPlainText("")
            self.gui.varerInfoEnhet.clearEditText()
            self.gui.varerInfoPris.setValue(0)
            self.gui.varerInfoPris.setSuffix("")
            self.gui.varerInfoMva.setValue(int(self.firma.mva))
            self.gui.varerInfoLegginn.setText('&Lag ny vare')
        self.gui.varerInfo.show()
        self.gui.varerInfoNavn.setFocus()

    def registrerVare(self):
        v = self.denne_vare
        if unicode(self.gui.varerInfoEnhet.currentText()).strip().isnumeric() and not \
            self.JaNei(u"Enhet bruker ikke å være et tall. Er du sikker på at du vil dette?"):
            self.gui.varerInfoEnhet.setFocus()
            return
        kravkart = {self.gui.varerInfoNavn:"Varenavn",
                    self.gui.varerInfoEnhet:"Enhet",
                    #self.gui.varerInfoPris:"Pris",
                    }
        for obj in kravkart.keys():
            if isinstance(obj, (QtGui.QSpinBox, QtGui.QDoubleSpinBox)): test = obj.value() > 0.0
            elif isinstance(obj, QtGui.QComboBox): test = obj.currentText()
            elif isinstance(obj, QtGui.QLineEdit): test = obj.text()
            elif isinstance(obj, QtGui.QPlainTextEdit): test = obj.toPlainText()
            if not test:
                self.alert(u'Du er nødt til å oppgi %s' % (kravkart[obj].lower()))
                obj.setFocus()
                return False

        logging.debug("Vare er v=%s", v)
        if v is None:
            v = self.faktura.nyVare()
            logging.debug("Ny vare: %s", v)
        else:
            logging.debug("oppdaterer vare, som var: " + unicode(v))
        v.navn = unicode(self.gui.varerInfoNavn.text()).strip()
        v.detaljer = unicode(self.gui.varerInfoDetaljer.toPlainText()).strip()
        v.enhet = unicode(self.gui.varerInfoEnhet.currentText()).strip()
        v.pris = float(self.gui.varerInfoPris.value())
        v.mva = int(self.gui.varerInfoMva.value())
        self.gui.varerInfo.hide()
        self.visVarer()

    def visVaredetaljer(self, linje):
        if linje is None:
            self.gui.varerDetaljerTekst.setText('')
            return
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
        self.gui.varerDetaljerTekst.setText(s)

    def slettVare(self, linje = None):
        try:
            vare = self.gui.varerVareliste.selectedItems()[0].vare
        except IndexError:
            return None # ingen vare er valgt i lista
        logging.debug("Sletter vare # %i" % vare._id)
        if self.JaNei("Vil du virkelig slette vare nr %s (%s)?" % (vare.ID, vare.navn)):
            vare.settSlettet()
            self.visVarer()

    def ikkeSlettVare(self):
        try:
            vare = self.gui.varerVareliste.selectedItems()[0].vare
        except IndexError:
            return None # ingen vare er valgt i lista
        vare.settSlettet(False)
        self.visVarer()


############## ØKONOMI ###################

    def visOkonomi(self):
        self.gui.okonomiAvgrensningerDatoAr.setValue(localtime()[0])

    def hentAktuelleOrdrer(self):
        ordrehenter = fakturaOkonomi.ordreHenter(self.db)
        begrensninger = {'dato':(None,None),
                         'kunde':None,
                         'vare':None,
                         'sortering':None,
                         'firma':None,
                         'visubetalte':False,
                         'viskansellerte':False}
        if self.gui.okonomiAvgrensningerDato.isChecked():
            aar = self.gui.okonomiAvgrensningerDatoAr.value()
            bmnd = self.gui.okonomiAvgrensningerDatoManed.currentIndex()
            if bmnd == 0:
                bmnd = 1
                smnd = 12
            else:
                smnd = bmnd + self.gui.okonomiAvgrensningerDatoPeriode.currentIndex()
            beg = mktime((aar,bmnd,1,0,0,0,0,0,0))
            slutt = mktime((aar,smnd,31,0,0,0,0,0,0))
            logging.debug("%s %s %s %s" % (bmnd, smnd, beg, slutt))
            ordrehenter.begrensDato(beg, slutt)
            begrensninger['dato'] = (beg,slutt)
        if self.gui.okonomiAvgrensningerKunde.isChecked():
            kliste = self.gui.okonomiAvgrensningerKundeliste
            try:
                kunde = kliste.itemData(kliste.currentIndex()).toPyObject()
                ordrehenter.begrensKunde(kunde)
                begrensninger['kunde'] = kunde
            except IndexError:
                raise
        if self.gui.okonomiAvgrensningerVare.isChecked():
            vliste = self.gui.okonomiAvgrensningerVareliste
            try:
                vare = vliste.itemData(vliste.currentIndex()).toPyObject()
                ordrehenter.begrensVare(vare)
                begrensninger['vare'] = vare
            except IndexError:
                raise
        begrensninger['viskansellerte'] = self.gui.okonomiAvgrensningerVisKansellerte.isChecked()
        ordrehenter.visKansellerte(begrensninger['viskansellerte'])
        begrensninger['visubetalte'] = not self.gui.okonomiAvgrensningerSkjulUbetalte.isChecked()
        ordrehenter.visUbetalte(not self.gui.okonomiAvgrensningerSkjulUbetalte.isChecked())

        if self.gui.okonomiSorter.isChecked():
            sorter = [ 'dato', 'kunde', 'vare' ]
            ordrehenter.sorterEtter(sorter[self.gui.okonomiSorterListe.currentIndex()])
            begrensninger['sortering'] = sorter[self.gui.okonomiSorterListe.currentIndex()]

        ordreliste = ordrehenter.hentOrdrer()
        return ordreliste, begrensninger

    def okonomiRegnRegnskap(self):
        logging.debug("regner regnskap")
        ordreliste = self.hentAktuelleOrdrer()[0]
        inn = mva = 0.0
        b = u = 0
        s = "<b>Fakturaer funnet:</b><br><ul>"
        for ordre in ordreliste:
            s += "<li>"
            if ordre.kansellert:
                s += " <font color=red><b>Kansellert:</b></font> "
            elif ordre.betalt:
                s += " <font color=green>Betalt:</font> "
            else:
                s += " <font color=red>Ubetalt:</font> "
            #s += unicode(ordre)
            s += "ordre <i># %04i</i>, utformet til %s den %s\n" % (ordre._id, ordre.kunde.navn, strftime("%Y-%m-%d", localtime(ordre.ordredato)))
            if ordre.linje:
                s += "<ol>"
                for vare in ordre.linje:
                    s += "<li> #%i: %s </li>" % (vare._id, unicode(vare))
                s += "</ol>\n"
            s += "</li>\n"
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
        self.gui.okonomiRegnskapTotalUMva.setText("%.2f kr" % inn)
        self.gui.okonomiRegnskapTotalMMva.setText("%.2f kr" % (inn+mva))
        self.gui.okonomiRegnskapMoms.setText("%.2f kr" % mva)
        self.gui.okonomiRegnskapAntallFakturaer.setText("%i stk (%i ubetalte)" % (b, u))
        #skriv detaljer om ordrer
        self.gui.okonomiDetaljregnskap.setText(s)

    def okonomiFyllDato(self, ibruk):
        self.gui.okonomiAvgrensningerDatoAr.setEnabled(ibruk)
        self.gui.okonomiAvgrensningerDatoManed.setEnabled(ibruk)
        if not ibruk:
            self.gui.okonomiAvgrensningerDatoPeriode.setEnabled(ibruk) # alltid disable denne
        self.gui.okonomiAvgrensningerDatoManed.clear()
        self.gui.okonomiAvgrensningerDatoPeriode.clear()
        mnd = [u'Hele året', 'Januar', 'Februar', 'Mars', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Desember']
        self.gui.okonomiAvgrensningerDatoManed.addItems(mnd)
        self.gui.okonomiAvgrensningerDatoPeriode.addItems( [ u'Og %i måneder fram' % i for i in range(1,12) ] )

    def okonomiFyllDatoPeriode(self, manedId):
        #bare tilgjengelig dersom det ikke er valgt 'Hele året'
        self.gui.okonomiAvgrensningerDatoPeriode.setEnabled(manedId > 0)

    def okonomiFyllKunder(self, ibruk):
        self.gui.okonomiAvgrensningerKundeliste.setEnabled(ibruk)
        self.gui.okonomiAvgrensningerKundeliste.clear()
        if ibruk:
            i = self.gui.okonomiAvgrensningerKundeliste.addItem
            for kunde in self.faktura.hentKunder(inkluderSlettede=True):
                i(unicode(kunde), QtCore.QVariant(kunde))

    def okonomiFyllVarer(self, ibruk):
        self.gui.okonomiAvgrensningerVareliste.setEnabled(ibruk)
        self.gui.okonomiAvgrensningerVareliste.clear()
        if ibruk:
            i = self.gui.okonomiAvgrensningerVareliste.addItem
            for v in self.faktura.hentVarer(inkluderSlettede=True):
                i(unicode("(#%i) %s") % (v.ID, v), QtCore.QVariant(v))

    def okonomiFyllSortering(self, ibruk):
        self.gui.okonomiSorterListe.setEnabled(ibruk)

    def okonomiSkrivUtFakturaer(self):
        if not finfaktura.rapport.REPORTLAB:
            self.alert("Kunne ikke laste reportlab-modulen. Ingen pdf tilgjengelig!")
            return False
        ordrer, beskrivelse = self.hentAktuelleOrdrer()
        beskrivelse['firma'] = self.firma
        rapport = finfaktura.rapport.rapport(rapportinfo=beskrivelse)
        rapport.lastOrdreliste(ordrer)
        rapport.vis(program=self.faktura.oppsett.vispdf)

############## INTERNE DIALOGER ###################

    def visEpostOppsett(self):
        dialog = gui_epost.epostOppsett(self.faktura)
        res = dialog.exec_()

    def visProgramOppsett(self):
        dialog = gui_finfaktura_oppsett.finfakturaOppsett(self.faktura)
        res = dialog.exec_()

    def visFirmaOppsett(self):
        dialog = gui_firma.firmaOppsett(self.firma)
        res = dialog.exec_()
        logging.debug('visFirmaOppsett.exec: %s', res)
        for egenskap, verdi in res.iteritems():
            logging.debug('setter %s = %s', egenskap, repr(verdi))
            setattr(self.firma, egenskap, verdi)

    def visTekstVindu(self, ressurs):
        if ressurs == 'om':
            tittel = 'Om Fryktelig Fin Faktura, versjon %s' % finfaktura.__version__
            r = ':/data/README'
        elif ressurs == 'lisens':
            tittel = u'Programmet er fritt tilgjengelig under GPL, versjon 2:'
            r = ':/data/LICENSE'
        try:
            vindu = tekstVindu(tittel, lesRessurs(r))
            res = vindu.exec_()
            return res
        except IOError, (e):
            self.alert(unicode(e))

############## GENERELLE METODER ###################

    def alert(self, msg):
        QtGui.QMessageBox.critical(self, "Feil!", msg, QtGui.QMessageBox.Ok)

    def obs(self, msg):
        QtGui.QMessageBox.information(self, "Obs!", msg, QtGui.QMessageBox.Ok)

    def JaNei(self, s):
        svar = QtGui.QMessageBox.question(self, "Hm?", s, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No | QtGui.QMessageBox.Default, QtGui.QMessageBox.NoButton)
        return svar == QtGui.QMessageBox.Yes

class tekstVindu(object):
    def __init__(self, tittel, tekst):
        self.gui = QtGui.QDialog()
        self.gui.setObjectName('tekstvindu')
        self.gui.resize(600, 600)
        self.gui.setModal(True)

        self.vbox = QtGui.QVBoxLayout(self.gui)
        self.tittel = QtGui.QLabel(self.gui)
        self.tittel.setText('<b>%s</b>' % tittel)
        self.tekst = QtGui.QPlainTextEdit(self.gui)
        self.tekst.setTabChangesFocus(True)
        self.tekst.setObjectName("tekst")
        self.tekst.setPlainText(tekst)
        self.tekst.setReadOnly(True)
        self.knapper = QtGui.QDialogButtonBox(self.gui)
        self.knapper.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.vbox.addWidget(self.tittel)
        self.vbox.addWidget(self.tekst)
        self.vbox.addWidget(self.knapper)

        QtCore.QObject.connect(self.knapper, QtCore.SIGNAL("accepted()"), self.gui.accept)

        self.gui.show()
    def exec_(self):
        return self.gui.exec_()

def start():
    app = QtGui.QApplication(sys.argv)
    ff = FinFaktura()
    QtCore.QObject.connect(app, QtCore.SIGNAL("lastWindowClosed()"), ff.avslutt)
    return app.exec_()

