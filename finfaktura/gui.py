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
from finfaktura.fakturabibliotek import PRODUKSJONSVERSJON, \
    FakturaBibliotek, kobleTilDatabase
import finfaktura.f60 as f60
from finfaktura.myndighetene import myndighetene
from finfaktura.epost import BRUK_GMAIL
import finfaktura.okonomi as fakturaOkonomi
import finfaktura.sikkerhetskopi as sikkerhetskopi
import finfaktura.historikk as historikk
import finfaktura.rapport
import finfaktura.fakturakomponenter
from finfaktura.fakturafeil import *
##from finfaktura.sendepost_ui import sendEpost

from PyQt4 import QtCore, QtGui, uic
import faktura_rc
#from finfaktura.ekstra import QtGui.QBuffer, slettetIkon_data, forfaltLogo_data
#from finfaktura.faktura_ui import faktura ## husk å kjøre "pyuic -x faktura.ui > faktura_ui.py" først!
from ekstra import debug


PDFVIS = "/usr/bin/kpdf" # program for å vise PDF

class FinFaktura(QtGui.QMainWindow): ## leser gui fra faktura_ui.py
    db = None
    denne_kunde = None
    denne_faktura = None
    denne_vare = None
    gammelTab = 0

    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.gui = uic.loadUi('faktura4.ui')

        #skjul ikke-ferdige tabs dersom vi er i produksjon
        # TODO: gjøre dem klare for produksjon
        if PRODUKSJONSVERSJON:
            self.gui.fakturaTab.removeTab(3) # myndighetene
        else:
            self.gui.setWindowTitle("FRYKTELIG FIN FADESE (utviklerversjon)")
            self.patchDebugModus() # vis live debug-konsoll

        self.connect(self.gui.fakturaTab, QtCore.SIGNAL("currentChanged(QWidget*)"), self.skiftTab)

        self.connect(self.gui.fakturaNy, QtCore.SIGNAL("clicked()"), self.nyFaktura)
#     self.connect(self.fakturaFakturaliste, QtCore.SIGNAL("doubleClicked(QListViewItem*, const QtGui.QPoint&, int)"), self.redigerFaktura)
        self.connect(self.gui.fakturaFaktaLegginn, QtCore.SIGNAL("clicked()"), self.leggTilFaktura)
        #self.connect(self.fakturaFaktaVare, QtCore.SIGNAL("highlighted(int)"), self.fakturaVareOppdater)
        self.connect(self.gui.fakturaFakturaliste, QtCore.SIGNAL("currentItemChanged (QTreeWidgetItem *,QTreeWidgetItem *)"), self.visFakturadetaljer)
        self.connect(self.gui.fakturaVareliste, QtCore.SIGNAL("valueChanged(int,int)"), self.fakturaVarelisteSynk)
        self.connect(self.gui.fakturaFaktaVareLeggtil, QtCore.SIGNAL("clicked()"), self.leggVareTilOrdre)
        #self.connect(self.gui.fakturaFaktaVareFjern, QtCore.SIGNAL("clicked()"), self.fjernVareFraOrdre)
        self.connect(self.gui.fakturaLagEpost, QtCore.SIGNAL("clicked()"), self.lagFakturaEpost)
        self.connect(self.gui.fakturaLagPapir, QtCore.SIGNAL("clicked()"), self.lagFakturaPapir)
        self.connect(self.gui.fakturaLagKvittering, QtCore.SIGNAL("clicked()"), self.lagFakturaKvittering)
        self.connect(self.gui.fakturaBetalt, QtCore.SIGNAL("clicked()"), self.betalFaktura)
        self.connect(self.gui.fakturaVisKansellerte, QtCore.SIGNAL("toggled(bool)"), self.visFaktura)
        self.connect(self.gui.fakturaVisGamle, QtCore.SIGNAL("toggled(bool)"), self.visFaktura)
        self.gui.fakturaFaktaKryss.mousePressEvent = self.lukkFakta

        self.connect(self.gui.kundeNy, QtCore.SIGNAL("clicked()"), self.lastKunde)
        self.connect(self.gui.kundeKundeliste, QtCore.SIGNAL("itemDoubleClicked (QTreeWidgetItem *,int)"), self.redigerKunde)
        self.connect(self.gui.kundeInfoEndre, QtCore.SIGNAL("clicked()"), self.leggTilKunde)
        self.connect(self.gui.kundeNyFaktura, QtCore.SIGNAL("clicked()"), self.nyFakturaFraKunde)
        self.connect(self.gui.kundeKundeliste, QtCore.SIGNAL("currentItemChanged (QTreeWidgetItem *,QTreeWidgetItem *)"), self.visKundedetaljer)
        self.connect(self.gui.kundeVisFjernede, QtCore.SIGNAL("toggled(bool)"), self.visKunder)
        self.gui.kundeInfoKryss.mousePressEvent = self.lukkKundeinfo

        #self.connect(self.gui.varerVareliste, QtCore.SIGNAL("selected(const QtGui.QString&)"), self.nyFaktura)

        self.connect(self.gui.varerNy, QtCore.SIGNAL("clicked()"), self.lastVare)
        self.connect(self.gui.varerVareliste, QtCore.SIGNAL("itemDoubleClicked (QTreeWidgetItem *,int)"), self.redigerVare)
        self.connect(self.gui.varerInfoLegginn, QtCore.SIGNAL("clicked()"), self.registrerVare)
        self.connect(self.gui.varerVareliste, QtCore.SIGNAL("currentItemChanged (QTreeWidgetItem *,QTreeWidgetItem *)"), self.visVaredetaljer)
        self.connect(self.gui.varerVisFjernede, QtCore.SIGNAL("toggled(bool)"), self.visVarer)
        self.gui.varerInfoKryss.mousePressEvent = self.lukkVarerinfo

        #self.connect(self.gui.dittfirmaFinnFjernLogo, QtCore.SIGNAL("clicked()"), self.finnFjernLogo)
        #self.connect(self.gui.dittfirmaLagre, QtCore.SIGNAL("clicked()"), self.oppdaterFirma)

        #self.connect(self.gui.epostSmtpAuth, QtCore.SIGNAL("toggled(bool)"), self.epostVisAuth)
        #self.connect(self.gui.epostLagre, QtCore.SIGNAL("clicked()"), self.oppdaterEpost)
        #self.connect(self.epostLosning, QtCore.SIGNAL("clicked(int)"), self.roterAktivSeksjon)
        #self.connect(self.epostLosningTest, QtCore.SIGNAL("clicked()"), self.testEpost)

        #self.connect(self.oppsettFakturakatalogSok, QtCore.SIGNAL("clicked()"), self.endreFakturakatalog)
        #self.connect(self.oppsettProgrammerVisSok, QtCore.SIGNAL("clicked()"), self.endreProgramVis)
        #self.connect(self.oppsettProgrammerUtskriftSok, QtCore.SIGNAL("clicked()"), self.endreProgramUtskrift)
        #self.connect(self.oppsettLagre, QtCore.SIGNAL("clicked()"), self.oppdaterOppsett)


        self.connect(self.gui.okonomiAvgrensningerDatoManed, QtCore.SIGNAL("highlighted(int)"), self.okonomiFyllDatoPeriode)
        self.connect(self.gui.okonomiAvgrensningerDato, QtCore.SIGNAL("toggled(bool)"), self.okonomiFyllDato)
        self.connect(self.gui.okonomiAvgrensningerKunde, QtCore.SIGNAL("toggled(bool)"), self.okonomiFyllKunder)
        self.connect(self.gui.okonomiAvgrensningerVare, QtCore.SIGNAL("toggled(bool)"), self.okonomiFyllVarer)
        self.connect(self.gui.okonomiSorter, QtCore.SIGNAL("toggled(bool)"), self.okonomiFyllSortering)
        self.connect(self.gui.okonomiRegnskapRegnut, QtCore.SIGNAL("clicked()"), self.okonomiRegnRegnskap)
        self.connect(self.gui.okonomiFakturaerSkrivut, QtCore.SIGNAL("clicked()"), self.okonomiSkrivUtFakturaer)

        #self.connect(self.sikkerhetskopiGmailLastopp, QtCore.SIGNAL("clicked()"), self.sikkerhetskopiGmail)

        #self.gui.fakturaVareliste.setColumnStretchable(0, True)
        #self.gui.fakturaVareliste.setColumnWidth(1, 70)
        ##self.gui.fakturaVareliste.setColumnWidth(2, 70)
        #self.gui.fakturaVareliste.setColumnWidth(3, 70)

        #for obj in (self.dittfirmaFirmanavn,
            #self.dittfirmaOrganisasjonsnummer,
            #self.dittfirmaKontaktperson,
            #self.dittfirmaEpost,
            #self.dittfirmaPostnummer,
            #self.dittfirmaPoststed,
            #self.dittfirmaTelefon,
            #self.dittfirmaTelefaks,
            #self.dittfirmaMobil,
            #self.dittfirmaKontonummer):
            #self.connect(obj, QtCore.SIGNAL("lostFocus()"), self.firmaSjekk)

        #for obj in (self.dittfirmaAdresse,
            ##self.dittfirmaVilkar
            #):
            #obj.focusOutEvent = self.firmaSjekk

        #self.connect(self.dittfirmaForfall, QtCore.SIGNAL("valueChanged(int)"), self.firmaSjekk)

        #self.dittfirmaKontrollKart = {
            #self.dittfirmaFirmanavn:'Firmanavn',
            #self.dittfirmaOrganisasjonsnummer:u'Organisasjonsnummer fra Brønnøysund',
            #self.dittfirmaKontaktperson:'Kontaktperson',
            #self.dittfirmaEpost:'Epostadresse',
            #self.dittfirmaAdresse:'Adresse',
            #self.dittfirmaPostnummer:'Postnummer',
            #self.dittfirmaPoststed:'Poststed',
            #self.dittfirmaTelefon:'Telefonnummer',
            #self.dittfirmaMobil:'Mobilnummer',
            #self.dittfirmaKontonummer:'Kontonummer',
            ##self.dittfirmaMva:'Momssats',
            #self.dittfirmaForfall:'Forfallsperiode',
        #}

        self.gui.kundeKundeliste.contextMenuEvent = self.kundeContextMenu
        self.gui.fakturaFakturaliste.contextMenuEvent = self.fakturaContextMenu
        self.gui.varerVareliste.contextMenuEvent = self.vareContextMenu

        self.databaseTilkobler()

        self.fakturaForfaltIkon = QtGui.QIcon(':/pix/emblem-important.svg')
        self.slettetIkon = QtGui.QIcon(':/pix/process-stop.svg')

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
            self.fakturaTab.showPage(self.fakturaTab.page(4))
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
        if not self.faktura.oppsett.vispdf:
            self.faktura.oppsett.vispdf = PDFVIS
        finfaktura.rapport.PDFVIS = self.faktura.oppsett.vispdf
        finfaktura.fakturakomponenter.PDFVIS = self.faktura.oppsett.vispdf

        if not self.faktura.oppsett.skrivutpdf:
            self.faktura.oppsett.skrivutpdf = PDFUTSKRIFT
        finfaktura.fakturakomponenter.PDFUTSKRIFT = self.faktura.oppsett.skrivutpdf
        f60.PDFUTSKRIFT = self.faktura.oppsett.skrivutpdf

        self.skiftTab(0)

    def avslutt(self):
        debug("__del__")
        debug("sikkerhetskopierer databasen", finnDatabasenavn())
        sikkerhetskopierFil(finnDatabasenavn())
        self.c.close()
        self.db.close()

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
        elif i is 5: self.visEpost()
        elif i is 6: self.visOppsett()
        elif i is 7: self.visSikkerhetskopi()
        elif i is 8: self.visMyndigheter()
        self.gammelTab = i

################## DEBUG ########################

    def patchDebugModus(self):
        # lag et konsoll til live inspeksjon

        self.pythoncode = QtGui.QTextEdit(self.centralWidget())
        self.pythoncode.setGeometry(QtCore.QRect(310,770,410,70))

        self.pythoncodeRun = QtGui.QPushButton(self.centralWidget())
        self.pythoncodeRun.setGeometry(QtCore.QRect(740,797,141,41))
        self.pythoncodeRun.setText(u'K&jør')

        self.connect(self.pythoncodeRun, QtCore.SIGNAL("clicked()"), self.runDebugCode)


    def runDebugCode(self):
        # kjør debug-kode
        code = unicode(self.pythoncode.text())
        run = eval(code) # oooh!
        debug(run)

################## FAKTURA ########################

    fakturaVarelisteCache = []

    def lukkFakta(self, *ev):
        self.gui.fakturaFakta.hide()
        self.gui.fakturaHandlinger.show()

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
        #self.fakturaSendepostBoks.hide()
        i = self.gui.fakturaFakturaliste.addTopLevelItem
        self.gui.fakturaFakturaliste.clear()
        nu = time()
        for ordre in self.faktura.hentOrdrer():
            if not visKansellerte and ordre.kansellert: continue
            if not visGamle and ordre.betalt and ordre.ordredato < nu-60*60*24*7*4*6: continue # eldre enn seks mnd og betalt
            if ordre.betalt: bet = strftime("%Y-%m-%d %H:%M", localtime(ordre.betalt))
            else: bet = "Nei"
            l = QtGui.QTreeWidgetItem([#self.gui.fakturaFakturaliste,
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
                debug("%s er forfalt men ikke betalt!" % ordre._id)
                l.setIcon(5, self.fakturaForfaltIkon)
            if bool(ordre.kansellert):
                l.setIcon(0, self.slettetIkon)
            i(l)
        self.gui.fakturaBetaltDato.setDate(QtCore.QDate.currentDate())

    def nyFakturaFraKunde(self):
        try:
            kunde = self.gui.kundeKundeliste.selectedItems()[0].kunde
        except IndexError:
            self.alert(u'Ingen kunde er valgt')
            return False
        debug("ny faktura fra kunde: %s" % kunde.ID)
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
            self.fakturaTab.setCurrentPage(3)
            return False
        if not kunde and not ordrelinje:
            self.denne_faktura=None
        if kunde is not None:
            self.gui.fakturaFaktaMottaker.clear()
            self.gui.fakturaFaktaMottaker.addItem(unicode(kunde), QtCore.QVariant(kunde))
            self.gui.fakturaVareliste.setFocus()
        else:
            self.fyllFakturaMottaker()
            self.gui.fakturaFaktaMottaker.setFocus()
        self.gui.fakturaFaktaTekst.setPlainText("")
        #self.fyllFakturaVare()
        self.fakturaVarelisteCache = self.faktura.hentVarer()
        self.gui.fakturaVareliste.clearContents()
        self.leggVareTilOrdre() # legg til tom rad
        self.gui.fakturaFaktaDato.setDate(QtCore.QDate.currentDate())
        self.gui.fakturaHandlinger.hide()
        self.gui.fakturaFakta.show()

    def leggTilFaktura(self):
        #legg inn faktura i registeret
        #er all nødvendig info samlet inn?
        if not len(unicode(self.gui.fakturaFaktaTekst.toPlainText())) and \
            not self.JaNei(u"Vil du virkelig legge inn fakturaen uten fakturatekst?"):
            self.gui.fakturaFaktaTekst.setFocus()
            return False
        #all nødvendig info er der, legg inn fakturaen
        #kundetekst = self.gui.fakturaFaktaMottaker.currentText()
        #kre = re.search(re.compile(r'kunde\ #\s?(\d+)'), unicode(kundetekst))
        #kunde = self.faktura.hentKunde(kre.group(1))
        kunde = self.gui.fakturaFaktamottaker.itemData(self.gui.fakturaFaktaMottaker.currentIndex()).toPyObject()
        print kunde
        d = self.gui.fakturaFaktaDato.date()
        dato = mktime((d.year(),d.month(),d.day(),11,59,0,0,0,0)) # på midten av dagen (11:59) for å kunne betale fakturaen senere laget samme dag
        f = self.faktura.nyOrdre(kunde, ordredato=dato)
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
            debug("fant vare i fakturaen:", unicode(v), unicode(vare))
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

        debug("legger inn faktura: %s " % unicode(f))
        debug("Lager sikkerhetskopi")
        self.faktura.lagSikkerhetskopi(f)
        self.visFaktura() # oppdater listen slik at den nye fakturaen blir med
        self.gui.fakturaFakturaliste.setSelected(self.fakturaFakturaliste.lastItem(), True) # velg den nye fakturaen
        self.gui.fakturaFakta.hide()

        #skal vi lage blanketter nå?
        s = u'Den nye fakturaen er laget. Vil du lage tilhørende blankett nå?'
        knapp = QtGui.QMessageBox.information(self, u'Lage blankett?', s, 'Epost', 'Papir', 'Senere', 0, 2)
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
        self.gui.fakturaFaktaMottaker.setEnabled(True)
        self.gui.fakturaFaktaMottaker.clear()
        self.gui.fakturaFaktaMottaker.addItems( [unicode(k) for k in self.faktura.hentKunder() ] )

    def leggVareTilOrdre(self):

        sisterad = self.gui.fakturaVareliste.rowCount()
        Antall = QtGui.QDoubleSpinBox(self.gui.fakturaVareliste)#, "Antall-%s" % sisterad)
        Antall.setMaximum(100000.0)
        Antall.setValue(0.0)
        Antall.setDecimals(2)
        Antall.show()
        self.connect(Antall, QtCore.SIGNAL("valueChanged(int)"), self.oppdaterFakturaSum)

        Pris = QtGui.QDoubleSpinBox(self.gui.fakturaVareliste)#, "Pris-%s" % sisterad)
        Pris.setButtonSymbols(QtGui.QDoubleSpinBox.UpDownArrows)
        Pris.setMaximum(999999999.0)
        Pris.setDecimals(2)
        Pris.show()
        #QtGui.QToolTip.add(Pris, u'Varens pris (uten MVA)')
        self.connect(Pris, QtCore.SIGNAL("valueChanged(int)"), self.oppdaterFakturaSum)

        #Mva = QtGui.QComboTableItem(self.fakturaFaktaVareliste, mvaListe, False)
        Mva = QtGui.QDoubleSpinBox(self.gui.fakturaVareliste)#, "Mva-%s" % sisterad)
        #Mva = QtGui.QComboBox(self.fakturaFaktaVareliste, "Mva-%s" % sisterad)
        #Mva.addItems( ['0','12','25'] )
        #Mva.setEditable(False)
        Mva.setButtonSymbols(QtGui.QDoubleSpinBox.UpDownArrows)
        Mva.setValue(25)
        Mva.show()
        self.connect(Mva, QtCore.SIGNAL("valueChanged(int)"), self.oppdaterFakturaSum)
        #QtGui.QToolTip.add(Mva, u'MVA-sats som skal beregnes på varen')
        #QObject.connect(Mva, QtCore.SIGNAL("highlighted(int)"), self.oppdaterFakturaSum)

        #Vare = QtGui.QComboTableItem(self.fakturaFaktaVareliste, varer, True)
        Vare = QtGui.QComboBox(self.gui.fakturaVareliste)#, "Beskrivelse-%s" % sisterad)
        Vare.addItems([unicode(v.navn) for v in self.faktura.hentVarer()])
        Vare.setEditable(True)
        Vare.setAutoCompletion(True)
        Vare.show()
        #QtGui.QToolTip.add(Vare, u'Velg vare; eller skriv inn nytt varenavn og trykk enter for å legge til en ny vare')
        self.connect(Vare, QtCore.SIGNAL("activated(int)"), self.oppdaterFakturaSum)


        self.gui.fakturaVareliste.setRowCount(sisterad+1)
#        self.fakturaFaktaVareliste.setItem(sisterad, 0, Vare)
        self.gui.fakturaVareliste.setCellWidget(sisterad, 0, Vare)
        self.gui.fakturaVareliste.setCellWidget(sisterad, 1, Antall)
        self.gui.fakturaVareliste.setCellWidget(sisterad, 2, Pris)
        self.gui.fakturaVareliste.setCellWidget(sisterad, 3, Mva)
        return self.fakturaVarelisteSynk(sisterad, 0)

    def fakturaVarelisteSynk(self, rad, kol):
        debug("synk:", rad, kol)
        sender = self.gui.fakturaVareliste.cellWidget(rad, kol)
        if kol == 0: # endret på varen -> oppdater metadata
            try:
                vare = self.gui.fakturaVarelisteCache[sender.currentItem()]
            except IndexError: #
                if sender.currentItem() >= len(self.fakturaVarelisteCache):
                    # ny vare, tøm andre felt
                    debug("ny vare opprettet", unicode(sender.currentText()))
                    self.gui.fakturaVareliste.cellWidget(rad, 1).setSuffix('')
                    self.gui.fakturaVareliste.cellWidget(rad, 2).setValue(0)
                    self.gui.fakturaVareliste.cellWidget(rad, 3).setValue(self.firma.mva)
                    return
                else: raise # ukjent problem
            except AttributeError: # hvorfor er dette ikke 0?
                try:
                    vare = self.fakturaVarelisteCache[0] # UGH! HACK
                except IndexError: #ingen varer lagt inn
                    return # UGH UGH UGH
            self.gui.fakturaVareliste.cellWidget(rad, 1).setSuffix(' '+vare.enhet)
            self.gui.fakturaVareliste.cellWidget(rad, 2).setValue(int(vare.pris))
            self.gui.fakturaVareliste.cellWidget(rad, 3).setValue(vare.mva)
            #self.fakturaFaktaVareliste.cellWidget(rad, 3).setCurrentText(str(vare.mva))
        else:
            # endret på antall, mva eller pris -> oppdater sum
            p = mva = 0.0
            for i in range(self.gui.fakturaVareliste.rowCount()):
                _antall = self.gui.fakturaVareliste.cellWidget(i, 1).value()
                _pris   = float(self.gui.fakturaVareliste.cellWidget(i, 2).value())
                _mva    = self.gui.fakturaVareliste.cellWidget(i, 3).value()
                p += _pris * _antall
                mva += _pris * _antall * _mva / 100
            self.gui.fakturaFaktaSum.setText("<u>%.2fkr (+%.2fkr mva)</u>" % (p, mva))

    def oppdaterFakturaSum(self):
        k = ['Beskrivelse', 'Antall', 'Pris', 'Mva']
        sender = self.sender()
        _kol, rad = sender.name().split('-')
        self.fakturaVarelisteSynk(int(rad), k.index(_kol))

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

    def lagFakturaKvittering(self):
        try:
            ordre = self.gui.fakturaFakturaliste.selectedItems()[0].ordre
        except IndexError:
            self.alert(u'Ingen faktura er valgt')
            return False
        kvitt = ordre.hentSikkerhetskopi()
        kvitt.skrivUt(program=self.faktura.oppsett.skrivutpdf)

    def visFakturaKvittering(self):
        try:
            ordre = self.gui.fakturaFakturaliste.selectedItems()[0].ordre
        except IndexError:
            self.alert(u'Ingen faktura er valgt')
            return False
        kvitt = ordre.hentSikkerhetskopi()
        kvitt.vis()

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
                    self.faktura.skrivUt(unicode(E), program=self.faktura.oppsett.skrivutpdf)
            return None
        if Type == "epost":
            pdf.lagBakgrunn()
        elif Type == "kvittering":
            pdf.lagBakgrunn()
            pdf.lagKopimerke()

        try:
            pdf.fyll()
        except FirmainfoFeil,(E):
            historikk.pdfEpost(ordre, False, "firmainfofeil: %s" % E)
            self.alert(u"Du må fylle ut firmainfo først:\n%s" % E)
            self.gui.fakturaTab.setCurrentPage(3)
        except KundeFeil,(E):
            self.alert(u"Kan ikke lage PDF!\nÅrsak: %s" % E)
            historikk.pdfEpost(ordre, False, "kundefeil: %s" % E)
        else:
            res = pdf.settSammen()
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
                        suksess = pdf.skrivUt(program=self.faktura.oppsett.skrivutpdf)
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

    ##def skjulSendepostBoks(self):
        #self.fakturaSendepostBoks.hide()

    def visEpostfaktura(self, ordre, pdfFilnavn):
        ##u'Vedlagt følger epostfaktura #%i:\n%s\n\n-- \n%s\n' % (ordre.ID, ordre.tekst,  ordre.firma)
        epostboks = sendEpost()
        #self.fakturaSendepostBoks.show()
        self.connect(epostboks.sendEpostSend, QtCore.SIGNAL("clicked()"), epostboks.accept)
        self.connect(epostboks.sendEpostAvbryt, QtCore.SIGNAL("clicked()"), epostboks.reject)
        epostboks.sendEpostTittel.setText(u'Sender faktura til %s <b>&lt;%s</b>&gt;' % (ordre.kunde.navn, ordre.kunde.epost))
        epostboks.sendEpostTekst.setText(u'Vedlagt følger epostfaktura #%i:\n%s\n\n-- \n%s\n%s' % (ordre.ID, ordre.tekst,  ordre.firma, ordre.firma.vilkar))
        res = epostboks.exec_loop()
        if res == QtGui.QDialog.Accepted:
          return self.sendEpostfaktura(ordre, unicode(epostboks.sendEpostTekst.text()), pdfFilnavn)
        else:
          #print unicode(epostboks.sendEpostTekst.text())
          pass


    def sendEpostfaktura(self, ordre, tekst, filnavn):
        try:
            debug('sender epostfaktura: ordre # %i, til: %s' % (ordre._id, ordre.kunde.epost))
            trans = ['auto', 'smtp', 'sendmail']
            debug('bruker transport %s' % trans[self.faktura.epostoppsett.transport])
            self.faktura.sendEpost(ordre,
                                   filnavn,
                                   tekst,
                                   trans[self.faktura.epostoppsett.transport]
                                   )
            #self.fakturaSendepostBoks.ordre.sendt = time() # XXX TODO: logg tid for sending

        except:
            f = sys.exc_info()[1]
            self.alert(u'Feil ved sending av faktura. Prøv å sende med en annen epostmetode.\n\nDetaljer:\n%s' % f)
            #historikk.epostSendt(ordre, 0, f)
            raise
        else:
            historikk.epostSendt(ordre, True, "Tid: %s, transport: %s" % (time(), trans[self.faktura.epostoppsett.transport]))
            #self.fakturaSendepostBoks.hide()
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
            l = QtGui.QTreeWidgetItem([ #self.kundeKundeliste,
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
            #debug("registrerer ny kunde")
            k = self.faktura.nyKunde()
        else:
            debug("oppdaterer kunde, som var " + unicode(k))
        k.navn = self.gui.kundeInfoNavn.text()
        k.kontaktperson = self.gui.kundeInfoKontaktperson.text()
        k.epost = self.gui.kundeInfoEpost.text()
        k.status = self.gui.kundeInfoStatus.currentText()
        k.adresse = self.gui.kundeInfoAdresse.toPlainText()
        k.poststed = self.gui.kundeInfoPoststed.text()
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
        self.gui.kundeDetaljerTekst.setText(s)

    def slettKunde(self):
        try:
            kunde = self.gui.kundeKundeliste.selectedItems()[0].kunde
        except IndexError:
            return None # ingen kunde er valgt i lista
        debug("Sletter kunde # %i" % kunde.ID)
        if self.JaNei("Vil du virkelig slette kunde nr %s (%s)?" % (kunde.ID, kunde.navn)):
            kunde.settSlettet()
            self.visKunder()

    def ikkeSlettKunde(self):
        try:
            kunde = self.gui.kundeKundeliste.selectedItems()[0].kunde
        except IndexError:
            return None # ingen kunde er valgt i lista
        debug("Fjerner slettet status for kunde # %i" % kunde.ID)
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
            l = QtGui.QTreeWidgetItem([
                              "%03d" % vare.ID,
                              unicode(vare.navn),
                              unicode(vare.detaljer),
                              "%.2f" % vare.pris,
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
            self.gui.varerInfoLegginn.setText('&Oppdater')
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
        kravkart = {self.gui.varerInfoNavn:"Varenavn",
                    self.gui.varerInfoEnhet:"Enhet",
                    self.gui.varerInfoPris:"Pris",
                    }
        for obj in kravkart.keys():
            if isinstance(obj, QtGui.QSpinBox): test = obj.value() > 0
            elif isinstance(obj, QtGui.QComboBox): test = obj.currentText()
            elif isinstance(obj, QtGui.QLineEdit): test = obj.text()
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
        v.navn = self.gui.varerInfoNavn.text()
        v.detaljer = self.gui.varerInfoDetaljer.toPlainText()
        v.enhet = self.gui.varerInfoEnhet.currentText()
        v.pris = float(self.gui.varerInfoPris.value())
        v.mva = self.gui.varerInfoMva.value()
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
        debug("Sletter vare # %i" % vare._id)
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

############## FIRMAINFO ###################

    def firmaWidgetKart(self):
        return {
            self.dittfirmaFirmanavn            :  self.firma.firmanavn,
            self.dittfirmaOrganisasjonsnummer  :  self.firma.organisasjonsnummer,
            self.dittfirmaKontaktperson        :  self.firma.kontaktperson,
            self.dittfirmaEpost                :  self.firma.epost,
            self.dittfirmaAdresse              :  self.firma.adresse,
            self.dittfirmaPostnummer           :  self.firma.postnummer,
            self.dittfirmaPoststed             :  self.firma.poststed,
            self.dittfirmaTelefon              :  self.firma.telefon,
            self.dittfirmaMobil                :  self.firma.mobil,
            self.dittfirmaTelefaks             :  self.firma.telefaks,
            self.dittfirmaKontonummer          :  self.firma.kontonummer,
            self.dittfirmaVilkar               :  self.firma.vilkar,
            self.dittfirmaMva                 :  self.firma.mva,
            self.dittfirmaForfall             :  self.firma.forfall,
            }

    def visFirma(self):
        format = { self.dittfirmaPostnummer: "%04i", }
        for til, fra in self.firmaWidgetKart().iteritems():
            #debug("fra", fra, type(fra))
            #debug("til", til, type(til))
            if hasattr(til, 'setText'):
                if not fra: continue
                if til in format: s = format[til] % fra
                else: s = unicode(fra)
                til.setText(s)
            elif hasattr(til, 'setValue'):
                if not fra: continue
                til.setValue(int(fra))
        self.visLogo()
        self.firmaSjekk()

    def visLogo(self):
        if not self.firma.logo:
            self.dittfirmaFinnFjernLogo.setText('Finn logo')
            self.dittfirmaLogoPixmap.setPixmap(QPixmap())
        else:
            logo = QtGui.QPixmap()
            logo.loadFromData(self.firma.logo)
            self.dittfirmaLogoPixmap.setPixmap(logo)
            self.dittfirmaFinnFjernLogo.setText('Fjern logo')

    def oppdaterFirmainfo(self, fraObj):
        kart = firmaWidgetKart()
        if isinstance(fraObj, QtGui.QSpinBox): fun = int(fraObj.value)
        elif isinstance(fraObj, QtGui.QComboBox): fun = unicode(fraObj.currentText)
        elif isinstance(fraObj, (QLineEdit,QTextEdit,)): fun = unicode(fraObj.text)

        debug(u'oppdatere %s til %s' % (fraObj, kart[fraObj]))
        kart[fraObj] = fun() # finner riktig lagringssted og kjører riktig funksjon

    def kanskjetall(self, obj):
        try:
            return int(obj.text())
        except ValueError:
            return None

    def oppdaterFirma(self):
        self.firma.firmanavn  = unicode(self.dittfirmaFirmanavn.text())
        self.firma.organisasjonsnummer = unicode(self.dittfirmaOrganisasjonsnummer.text())
        self.firma.kontaktperson = unicode(self.dittfirmaKontaktperson.text())
        self.firma.epost      = unicode(self.dittfirmaEpost.text())
        self.firma.adresse    = unicode(self.dittfirmaAdresse.text())
        self.firma.postnummer = self.kanskjetall(self.dittfirmaPostnummer)
        self.firma.poststed   = unicode(self.dittfirmaPoststed.text())
        self.firma.telefon    = self.kanskjetall(self.dittfirmaTelefon)
        self.firma.mobil      = self.kanskjetall(self.dittfirmaMobil)
        self.firma.telefaks   = self.kanskjetall(self.dittfirmaTelefaks)
        self.firma.kontonummer = self.kanskjetall(self.dittfirmaKontonummer)
        self.firma.vilkar     = unicode(self.dittfirmaVilkar.text())
        self.firma.mva        = int(self.dittfirmaMva.value())
        self.firma.forfall    = int(self.dittfirmaForfall.value())

        mangler = self.sjekkFirmaMangler()
        if mangler:
            mangel = u'Ufullstendige opplysninger. Du er nødt til å oppgi:\n%s' % ([ mangler[obj].lower() for obj in mangler.keys() ])
            self.alert(mangel)
            self.fakturaTab.showPage(self.fakturaTab.page(3))
            obj.setFocus()
            self.gammelTab = 3
            return False
        self.dittfirmaLagreInfo.setText('<font color=green><b>Opplysningene er lagret</b></font>')
        #print self.faktura.firmainfo()

    def sjekkFirmaMangler(self):
        kravkart = {}
        kravkart.update(self.dittfirmaKontrollKart)
        for obj in kravkart.keys():
            if isinstance(obj, QtGui.QSpinBox): test = obj.value() > 0
            elif isinstance(obj, QtGui.QComboBox): test = obj.currentText()
            elif isinstance(obj, (QLineEdit,QTextEdit,)): test = obj.text()
            if test: kravkart.pop(obj)
        return kravkart

    def firmaSjekk(self, event=None):
        mangler = 0
        s = u"<b><font color=red>Følgende felter må fylles ut:</font></b><ol>"
        ok = QtGui.QColor('white')
        tom = QtGui.QColor('red')
        for obj in self.dittfirmaKontrollKart.keys():
            if isinstance(obj, QtGui.QSpinBox): test = obj.value() > 0
            elif isinstance(obj, QtGui.QComboBox): test = obj.currentText()
            elif isinstance(obj, (QLineEdit,QTextEdit,)): test = obj.text()
            if test:
                obj.setPaletteBackgroundColor(ok)
                #self.oppdaterFirmainfo(obj) # lagrer informasjonen
            else:
                s += u"<li>%s" % self.dittfirmaKontrollKart[obj]
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
            logo = QtGui.QFileDialog.getOpenFileName(
                startdir,
                'Bildefiler (*.png *.xpm *.jpg *.jpeg *.gif *.bmp *.ppm *.pgm *.pbm)',
                self,
                "Velg logofil",
                "Velg bildefil for firmaets logo"
                )
            if len(unicode(logo)) > 0:
                debug("Setter ny logo: %s" % logo)

                l = QtGui.QPixmap()
                l.loadFromData(open(unicode(logo)).read())

                stream = QtGui.QBuffer()
                l.convertToImage().smoothScale(360,360, QtGui.QImage.ScaleMax).save(stream, 'PNG')

                #import sqlite

                #self.firma.logo = sqlite.encode(stream.getData())
                self.firma.logo = buffer(stream.getData())
                self.visLogo()




############## Epost ###################

    def visEpost(self):
        if self.faktura.epostoppsett.bcc:
            self.epostSendkopi.setChecked(True)
            self.epostKopiadresse.setText(self.faktura.epostoppsett.bcc)
        self.epostLosning.setButton(self.faktura.epostoppsett.transport)
        self.roterAktivSeksjon(self.faktura.epostoppsett.transport)
        if self.faktura.epostoppsett.smtpserver:
            self.epostSmtpServer.setText(self.faktura.epostoppsett.smtpserver)
        if self.faktura.epostoppsett.smtpport:
            self.epostSmtpPort.setValue(self.faktura.epostoppsett.smtpport)
        self.epostSmtpTLS.setChecked(self.faktura.epostoppsett.smtptls)
        self.epostSmtpAuth.setChecked(self.faktura.epostoppsett.smtpauth)
        if self.faktura.epostoppsett.smtpbruker: # husk brukernavn og passord for smtp
            self.epostSmtpHuskEpost.setChecked(True)
            if self.faktura.epostoppsett.smtpbruker:
                self.epostSmtpBrukernavn.setText(self.faktura.epostoppsett.smtpbruker)
            if self.faktura.epostoppsett.smtppassord:
                self.epostSmtpPassord.setText(self.faktura.epostoppsett.smtppassord)
        if self.faktura.epostoppsett.sendmailsti:
            self.epostSendmailSti.setText(self.faktura.epostoppsett.sendmailsti)
        else:
            self.epostSendmailSti.setText('~')

    def oppdaterEpost(self):
        debug("lagrer epost")
        self.faktura.epostoppsett.transport = self.epostLosning.selectedId()
        if not self.epostSendkopi.isChecked():
            self.epostKopiadresse.setText('')
        self.faktura.epostoppsett.bcc = unicode(self.epostKopiadresse.text())
        self.faktura.epostoppsett.smtpserver = unicode(self.epostSmtpServer.text())
        self.faktura.epostoppsett.smtpport = self.epostSmtpPort.value()
        self.faktura.epostoppsett.smtptls = self.epostSmtpTLS.isChecked()
        self.faktura.epostoppsett.smtpauth = self.epostSmtpAuth.isChecked()
        if self.epostSmtpHuskEpost.isChecked():
            self.faktura.epostoppsett.smtpbruker = unicode(self.epostSmtpBrukernavn.text())
            self.faktura.epostoppsett.smtppassord = unicode(self.epostSmtpPassord.text())
        else:
            self.faktura.epostoppsett.smtpbruker = ''
            self.faktura.epostoppsett.smtppassord = ''
        self.faktura.epostoppsett.sendmailsti = unicode(self.epostSendmailSti.text())

    def roterAktivSeksjon(self, aktivId=None):
        return
        if aktivId is None: aktivId = self.epostLosning.selectedId()
        i = 1
        debug("roterer til %i er synlig" % aktivId)
        for seksjon in [self.epostSeksjonSmtp, self.epostSeksjonSendmail]:
            seksjon.setEnabled(aktivId == i)
            i += 1

    def testEpost(self):
        self.oppdaterEpost() # må lagre for å bruke de inntastede verdiene
        trans = ['auto', 'smtp', 'sendmail']
        debug('bruker transport %s' % trans[self.epostLosning.selectedId()])
        try:
            transport = self.faktura.testEpost(trans[self.epostLosning.selectedId()])
        except Exception,ex:
            s = u'Epostoppsettet fungerer ikke. Oppgitt feilmelding:\n %s \n\nKontroller at de oppgitte innstillingene \ner korrekte' % ex.message
            raise
            trans = getattr(ex, 'transport')
            if trans != 'auto':
                ex.transportmetoder.remove(trans) # fjerner feilet metode fra tilgjengelig-liste
                s += u', eller prøv en annen metode.\nTilgjengelige metoder:\n%s' % ', '.join(ex.transportmetoder)
            self.alert(s)
        else:
            self.obs("Epostoppsettet fungerer. Bruker %s" % transport)
            try:
                self.epostLosning.setButton(trans.index(transport))
                self.roterAktivSeksjon(trans.index(transport))
            except:pass
            self.oppdaterEpost() # må lagre for å bruke den aktive løsningen

    def epostVisAuth(self, vis):
        self.epostSmtpBrukernavn.setEnabled(vis)
        self.epostSmtpPassord.setEnabled(vis)

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
            bmnd = self.gui.okonomiAvgrensningerDatoManed.currentItem()
            if bmnd == 0:
                bmnd = 1
                smnd = 12
            else:
                smnd = bmnd + self.okonomiAvgrensningerDatoPeriode.currentItem()
            beg = mktime((aar,bmnd,1,0,0,0,0,0,0))
            slutt = mktime((aar,smnd,31,0,0,0,0,0,0))
            debug("%s %s %s %s" % (bmnd, smnd, beg, slutt))
            ordrehenter.begrensDato(beg, slutt)
            begrensninger['dato'] = (beg,slutt)
        if self.gui.okonomiAvgrensningerKunde.isChecked():
            krex = re.search(re.compile(r'kunde\ #\s?(\d+)'),
                unicode(self.gui.okonomiAvgrensningerKundeliste.currentText()))
            try:
                kunde = self.faktura.hentKunde(int(krex.group(1)))
                ordrehenter.begrensKunde(kunde)
                begrensninger['kunde'] = kunde
            except IndexError:
                raise
        if self.gui.okonomiAvgrensningerVare.isChecked():
            vrex = re.search(re.compile(r'^\(#(\d+)\)'),
                unicode(self.gui.okonomiAvgrensningerVareliste.currentText()))
            try:
                vare = self.faktura.hentVare(int(vrex.group(1)))
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
            ordrehenter.sorterEtter(sorter[self.gui.okonomiSorterListe.currentItem()])
            begrensninger['sortering'] = sorter[self.gui.okonomiSorterListe.currentItem()]

        ordreliste = ordrehenter.hentOrdrer()
        return ordreliste, begrensninger

    def okonomiRegnRegnskap(self):
        debug("regner regnskap")
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
        in1 = self.gui.okonomiAvgrensningerDatoManed.insertItem
        in2 = self.gui.okonomiAvgrensningerDatoPeriode.insertItem
        for z in mnd: in1(z)
        for i in range(1,12): in2(u'Og %i måneder fram' % i)

    def okonomiFyllDatoPeriode(self, manedId):
        #bare tilgjengelig dersom det ikke er valgt 'Hele året'
        self.gui.okonomiAvgrensningerDatoPeriode.setEnabled(manedId > 0)

    def okonomiFyllKunder(self, ibruk):
        self.gui.okonomiAvgrensningerKundeliste.setEnabled(ibruk)
        self.gui.okonomiAvgrensningerKundeliste.clear()
        i = self.gui.okonomiAvgrensningerKundeliste.insertItem
        for kunde in self.faktura.hentKunder(inkluderSlettede=True):
            i(unicode(kunde))

    def okonomiFyllVarer(self, ibruk):
        self.gui.okonomiAvgrensningerVareliste.setEnabled(ibruk)
        self.gui.okonomiAvgrensningerVareliste.clear()
        i = self.gui.okonomiAvgrensningerVareliste.insertItem
        for v in self.faktura.hentVarer(inkluderSlettede=True):
            i(unicode("(#%i) %s") % (v.ID, v))

    def okonomiFyllSortering(self, ibruk):
        self.gui.okonomiSorterListe.setEnabled(ibruk)

    def okonomiSkrivUtFakturaer(self):
        if not finfaktura.rapport.REPORTLAB:
            self.alert("Kunne ikke laste reportlab-modulen. Ingen pdf tilgjengelig!")
            return False
        ordrer, beskrivelse = self.hentAktuelleOrdrer()
        beskrivelse['firma'] = self.firma
        rapport = finfaktura.rapport.rapport('/tmp/hei.pdf', beskrivelse)
        rapport.lastOrdreliste(ordrer)
        rapport.vis(program=self.faktura.oppsett.vispdf)

############## OPPSETT ###################

    def visOppsett(self):
        self.oppsettFakturakatalog.setText(self.faktura.oppsett.fakturakatalog)
        self.oppsettProgramVisPDF.setText(self.faktura.oppsett.vispdf)
        self.oppsettProgramSkrivUtPDF.setText(self.faktura.oppsett.skrivutpdf)

    def endreFakturakatalog(self):
        nu = self.oppsettFakturakatalog.text()
        startdir = nu
        ny = QtGui.QFileDialog.getExistingDirectory(startdir, self, "Velg katalog fakturaene skal lagres i", "Velg fakturakatalog")
        if len(unicode(ny)) > 0:
            debug("Setter ny fakturakataolg: %s" % ny)
            self.faktura.oppsett.fakturakatalog = unicode(ny)
            self.dittfirmaFakturakatalog.setText(unicode(ny))

    def endreProgramVis(self):
        ny = unicode(QFileDialog.getOpenFileName(self.oppsettProgramVisPDF.text(), "", self, "Velg program", u"Velg et program til å vise PDF i"))
        if len(ny) > 0:
            debug("Setter nytt visningsprogram: %s" % ny)
            self.faktura.oppsett.vispdf= ny
            self.oppsettProgramVisPDF.setText(ny)

    def endreProgramUtskrift(self):
        ny = unicode(QFileDialog.getOpenFileName(self.oppsettProgramSkrivUtPDF.text(), "", self, "Velg program", u"Velg et program til å skrive ut PDF med"))
        if len(ny) > 0:
            debug("Setter nytt utskriftsprogram: %s" % ny)
            self.faktura.oppsett.skrivutpdf = ny
            self.oppsettProgramSkrivUtPDF.setText(ny)

    def oppdaterOppsett(self):
        debug("Lager oppsett")
        self.faktura.oppsett.fakturakatalog = unicode(self.oppsettFakturakatalog.text())
        self.faktura.oppsett.vispdf = unicode(self.oppsettProgramVisPDF.text())
        self.faktura.oppsett.skrivutpdf = unicode(self.oppsettProgramSkrivUtPDF.text())

############## MYNDIGHETER ###################

    def visMyndigheter(self):
        from finfaktura.myndighetene import myndighetene
        offentlige = myndighetene()

        debug("finner skjemaplikter for %s" % self.firma.organisasjonsnummer)
        self.myndigheteneSkjemaListe.clear()
        for skjema in offentlige.skjemaplikter(self.firma.organisasjonsnummer):
            i = QtGui.QListViewItem(self.myndigheteneSkjemaListe, skjema[0],skjema[1],skjema[2],skjema[3])
            self.myndigheteneSkjemaListe.insertItem(i)




############## SIKKERHETSKOPI ###################

    def visSikkerhetskopi(self):

        if sikkerhetskopi.BRUK_GMAIL:
            self.sikkerhetskopiGmailUbrukelig.hide()
            self.sikkerhetskopiGmailLastopp.setEnabled(True)
            if len(self.faktura.epostoppsett.gmailbruker):
                self.sikkerhetskopiGmailHuskEpost.setChecked(True)
            if len(self.faktura.epostoppsett.gmailpassord):
                self.sikkerhetskopiGmailHuskPassord.setChecked(True)
            self.sikkerhetskopiGmailEpost.setText(self.faktura.epostoppsett.gmailbruker)
            self.sikkerhetskopiGmailPassord.setText(self.faktura.epostoppsett.gmailpassord)
        else:
            self.sikkerhetskopiGmailUbrukelig.show()
            self.sikkerhetskopiGmailLastopp.setEnabled(False)


    def sikkerhetskopiGmail(self):
        bruker = self.sikkerhetskopiGmailEpost.text()
        passord = self.sikkerhetskopiGmailPassord.text()
        if not (bruker and passord):
            self.alert(u'Du har ikke oppgitt brukernavn og passord i Gmail')
            return False
        if PRODUKSJONSVERSJON: label = "finfaktura"
        else: label = "fakturatest"
        sikker = sikkerhetskopi.gmailkopi(finnDatabasenavn(), bruker, passord, label)
        r = sikker.lagre()
        if self.sikkerhetskopiGmailHuskEpost.isChecked():
            self.faktura.epostoppsett.gmailbruker = self.sikkerhetskopiGmailEpost.text()
        if self.sikkerhetskopiGmailHuskPassord.isChecked():
            self.faktura.epostoppsett.gmailpassord = self.sikkerhetskopiGmailPassord.text()
        return r


############## GENERELLE METODER ###################

    def alert(self, msg):
        QtGui.QMessageBox.critical(self, "Feil!", msg, QtGui.QMessageBox.Ok)

    def obs(self, msg):
        QtGui.QMessageBox.information(self, "Obs!", msg, QtGui.QMessageBox.Ok)

    def JaNei(self, s):
        svar = QtGui.QMessageBox.question(self, "Hm?", s, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No | QtGui.QMessageBox.Default, QtGui.QMessageBox.NoButton)
        return svar == QtGui.QMessageBox.Yes

def start():
    app = QtGui.QApplication(sys.argv)
    ff = FinFaktura()
    ff.gui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":

    DEBUG = "-d" in sys.argv[1:]


