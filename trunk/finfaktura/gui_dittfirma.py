# -*- coding:utf8 -*-
# kate: indent-width 4;
###########################################################################
#    Copyright (C) 2008 Håvard Gulldahl
#    <havard@gulldahl.no>
#
#    Lisens: GPL2
#
# $Id: faktura.py 260 2008-05-11 08:59:23Z havard.gulldahl $
#
###########################################################################

from PyQt4 import QtCore, QtGui
from ui import firma_ui

class firmaOppsett(firma_ui.Ui_firmaOppsett):
    def __init__(self, faktura):
        self.faktura = faktura
        self.gui = QtGui.QDialog()
        self.setupUi(self.gui)
        self.connect(self.gui.FinnFjernLogo, QtCore.SIGNAL("clicked()"), self.finnFjernLogo)
        self.connect(self.gui.Lagre, QtCore.SIGNAL("clicked()"), self.oppdaterFirma)

        self.vis()
        self.gui.show()

    def exec_(self):
        res = self.gui.exec_()
        if res == QtGui.QDialog.Accepted:
            debug('oppdaterer')
            self.oppdaterEpost()
        return res



        #for obj in (self.Firmanavn,
            #self.Organisasjonsnummer,
            #self.Kontaktperson,
            #self.Epost,
            #self.Postnummer,
            #self.Poststed,
            #self.Telefon,
            #self.Telefaks,
            #self.Mobil,
            #self.Kontonummer):
            #self.connect(obj, QtCore.SIGNAL("lostFocus()"), self.firmaSjekk)

        #for obj in (self.Adresse,
            ##self.Vilkar
            #):
            #obj.focusOutEvent = self.firmaSjekk

        #self.connect(self.Forfall, QtCore.SIGNAL("valueChanged(int)"), self.firmaSjekk)

        #self.KontrollKart = {
            #self.Firmanavn:'Firmanavn',
            #self.Organisasjonsnummer:u'Organisasjonsnummer fra Brønnøysund',
            #self.Kontaktperson:'Kontaktperson',
            #self.Epost:'Epostadresse',
            #self.Adresse:'Adresse',
            #self.Postnummer:'Postnummer',
            #self.Poststed:'Poststed',
            #self.Telefon:'Telefonnummer',
            #self.Mobil:'Mobilnummer',
            #self.Kontonummer:'Kontonummer',
            ##self.Mva:'Momssats',
            #self.Forfall:'Forfallsperiode',
        #}
############## FIRMAINFO ###################

    def firmaWidgetKart(self):
        return {
            self.gui.Firmanavn            :  self.firma.firmanavn,
            self.gui.Organisasjonsnummer  :  self.firma.organisasjonsnummer,
            self.gui.Kontaktperson        :  self.firma.kontaktperson,
            self.gui.Epost                :  self.firma.epost,
            self.gui.Adresse              :  self.firma.adresse,
            self.gui.Postnummer           :  self.firma.postnummer,
            self.gui.Poststed             :  self.firma.poststed,
            self.gui.Telefon              :  self.firma.telefon,
            self.gui.Mobil                :  self.firma.mobil,
            self.gui.Telefaks             :  self.firma.telefaks,
            self.gui.Kontonummer          :  self.firma.kontonummer,
            self.gui.Vilkar               :  self.firma.vilkar,
            self.gui.Mva                 :  self.firma.mva,
            self.gui.Forfall             :  self.firma.forfall,
            }

    def visFirma(self):
        format = { self.Postnummer: "%04i", }
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
            self.gui.FinnFjernLogo.setText('Finn logo')
            self.gui.LogoPixmap.setPixmap(QPixmap())
        else:
            logo = QtGui.QPixmap()
            logo.loadFromData(self.firma.logo)
            self.gui.LogoPixmap.setPixmap(logo)
            self.gui.FinnFjernLogo.setText('Fjern logo')

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
        self.firma.firmanavn  = unicode(self.gui.Firmanavn.text())
        self.firma.organisasjonsnummer = unicode(self.gui.Organisasjonsnummer.text())
        self.firma.kontaktperson = unicode(self.gui.Kontaktperson.text())
        self.firma.epost      = unicode(self.gui.Epost.text())
        self.firma.adresse    = unicode(self.gui.Adresse.text())
        self.firma.postnummer = self.kanskjetall(self.gui.Postnummer)
        self.firma.poststed   = unicode(self.gui.Poststed.text())
        self.firma.telefon    = self.kanskjetall(self.gui.Telefon)
        self.firma.mobil      = self.kanskjetall(self.gui.Mobil)
        self.firma.telefaks   = self.kanskjetall(self.gui.Telefaks)
        self.firma.kontonummer = self.kanskjetall(self.gui.Kontonummer)
        self.firma.vilkar     = unicode(self.gui.Vilkar.text())
        self.firma.mva        = int(self.gui.Mva.value())
        self.firma.forfall    = int(self.gui.Forfall.value())

        mangler = self.sjekkFirmaMangler()
        if mangler:
            mangel = u'Ufullstendige opplysninger. Du er nødt til å oppgi:\n%s' % ([ mangler[obj].lower() for obj in mangler.keys() ])
            print (mangel)
            #self.fakturaTab.showPage(self.fakturaTab.page(3))
            obj.setFocus()
            #self.gammelTab = 3
            return False
        #self.LagreInfo.setText('<font color=green><b>Opplysningene er lagret</b></font>')
        #print self.faktura.firmainfo()

    def sjekkFirmaMangler(self):
        kravkart = {}
        kravkart.update(self.KontrollKart)
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
        for obj in self.KontrollKart.keys():
            if isinstance(obj, QtGui.QSpinBox): test = obj.value() > 0
            elif isinstance(obj, QtGui.QComboBox): test = obj.currentText()
            elif isinstance(obj, (QLineEdit,QTextEdit,)): test = obj.text()
            if test:
                obj.setPaletteBackgroundColor(ok)
                #self.oppdaterFirmainfo(obj) # lagrer informasjonen
            else:
                s += u"<li>%s" % self.KontrollKart[obj]
                obj.setPaletteBackgroundColor(tom)
                mangler += 1
        if not mangler:
            self.gui.LagreInfo.setText('')
            self.gui.Lagre.setEnabled(True)
            return True
        else:
            s += "</ol>"
            self.gui.LagreInfo.setText(s)
            self.gui.Lagre.setEnabled(False)

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


