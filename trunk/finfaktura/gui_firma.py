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
from ui import firmainfo_ui

class firmaOppsett(firmainfo_ui.Ui_firmaOppsett):
    def __init__(self, firma):
        self.firma = firma
        self.gui = QtGui.QDialog()
        self.setupUi(self.gui)
        self.gui.connect(self.lagreLogo, QtCore.SIGNAL("clicked()"), self.finnFjernLogo)

        self._kontrollkart = {
            self.Firmanavn:'Firmanavn',
            self.Organisasjonsnummer:u'Organisasjonsnummer fra Brønnøysund',
            self.Kontaktperson:'Kontaktperson',
            self.Epost:'Epostadresse',
            self.Adresse:'Adresse',
            self.Postnummer:'Postnummer',
            self.Poststed:'Poststed',
            self.Telefon:'Telefonnummer',
            self.Mobil:'Mobilnummer',
            self.Kontonummer:'Kontonummer',
            #self.Mva:'Momssats',
            self.Forfall:'Forfallsperiode',
        }
        self.vis()
        self.gui.show()


    def exec_(self):
        res = self.gui.exec_()
        if res == QtGui.QDialog.Accepted:
            print('oppdaterer')
            self.oppdater()
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

############## FIRMAINFO ###################

    def firmaWidgetKart(self):
        return {
            self.Firmanavn            :  self.firma.firmanavn,
            self.Organisasjonsnummer  :  self.firma.organisasjonsnummer,
            self.Kontaktperson        :  self.firma.kontaktperson,
            self.Epost                :  self.firma.epost,
            self.Adresse              :  self.firma.adresse,
            self.Postnummer           :  self.firma.postnummer,
            self.Poststed             :  self.firma.poststed,
            self.Telefon              :  self.firma.telefon,
            self.Mobil                :  self.firma.mobil,
            self.Telefaks             :  self.firma.telefaks,
            self.Kontonummer          :  self.firma.kontonummer,
            self.Vilkar               :  self.firma.vilkar,
            self.Mva                 :  self.firma.mva,
            self.Forfall             :  self.firma.forfall,
            }

    def vis(self):
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
            elif hasattr(til, 'setPlainText'):
                if not fra: continue
                til.setPlainText(unicode(fra))
        self.visLogo()
        self.firmaSjekk()

    def visLogo(self):
        if not self.firma.logo:
            self.lagreLogo.setText('Finn logo')
            self.LogoPixmap.setPixmap(QtGui.QPixmap())
        else:
            logo = QtGui.QPixmap()
            logo.loadFromData(self.firma.logo)
            self.LogoPixmap.setPixmap(logo)
            self.lagreLogo.setText('Fjern logo')

    def oppdaterFirmainfo(self, fraObj):
        kart = firmaWidgetKart()
        if isinstance(fraObj, QtGui.QSpinBox): fun = int(fraObj.value)
        elif isinstance(fraObj, QtGui.QComboBox): fun = unicode(fraObj.currentText)
        elif isinstance(fraObj, (QtGui.QLineEdit,QtGui.QTextEdit,)): fun = unicode(fraObj.text)

        debug(u'oppdatere %s til %s' % (fraObj, kart[fraObj]))
        kart[fraObj] = fun() # finner riktig lagringssted og kjører riktig funksjon

    def kanskjetall(self, obj):
        try:
            return int(obj.text())
        except ValueError:
            return None

    def oppdater(self):
        self.firma.firmanavn  = unicode(self.Firmanavn.text())
        self.firma.organisasjonsnummer = unicode(self.Organisasjonsnummer.text())
        self.firma.kontaktperson = unicode(self.Kontaktperson.text())
        self.firma.epost      = unicode(self.Epost.text())
        self.firma.adresse    = unicode(self.Adresse.toPlainText())
        self.firma.postnummer = self.kanskjetall(self.Postnummer)
        self.firma.poststed   = unicode(self.Poststed.text())
        self.firma.telefon    = self.kanskjetall(self.Telefon)
        self.firma.mobil      = self.kanskjetall(self.Mobil)
        self.firma.telefaks   = self.kanskjetall(self.Telefaks)
        self.firma.kontonummer = self.kanskjetall(self.Kontonummer)
        self.firma.vilkar     = unicode(self.Vilkar.toPlainText())
        self.firma.mva        = int(self.Mva.value())
        self.firma.forfall    = int(self.Forfall.value())

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
        kravkart.update(self._kontrollkart)
        for obj in kravkart.keys():
            if isinstance(obj, QtGui.QSpinBox): test = obj.value() > 0
            elif isinstance(obj, QtGui.QComboBox): test = obj.currentText()
            elif isinstance(obj, (QtGui.QLineEdit,QtGui.QTextEdit,)): test = obj.text()
            if test: kravkart.pop(obj)
        return kravkart

    def firmaSjekk(self, event=None):
        mangler = 0
        s = u"<b><font color=red>Følgende felter må fylles ut:</font></b><ol>"
        ok = QtGui.QColor('white')
        tom = QtGui.QColor('red')
        for obj in self._kontrollkart.keys():
            if isinstance(obj, QtGui.QSpinBox): test = obj.value() > 0
            elif isinstance(obj, QtGui.QComboBox): test = obj.currentText()
            elif isinstance(obj, (QtGui.QLineEdit,QtGui.QTextEdit,)): test = obj.text()
            if test:
                #obj.setPaletteBackgroundColor(ok)
                obj.setStyleSheet("QWidget { background-color: white; }")
                #self.oppdaterFirmainfo(obj) # lagrer informasjonen
            else:
                s += u"<li>%s" % self._kontrollkart[obj]
                obj.setStyleSheet("QWidget { background-color: red; }")
                #obj.setPaletteBackgroundColor(tom)
                mangler += 1
        if not mangler:
            #self.LagreInfo.setText('')
            #self.Lagre.setEnabled(True)
            return True
        else:
            s += "</ol>"
            #self.LagreInfo.setText(s)
            #self.Lagre.setEnabled(False)

    def finnFjernLogo(self):
        if self.firma.logo:
            self.firma.logo = ""
            self.visLogo()
        else:
            startdir = ""
            logo = QtGui.QFileDialog.getOpenFileName(self.gui,
                "Velg bildefil for firmaets logo",
                startdir,
                'Bildefiler (*.png *.xpm *.jpg *.jpeg *.gif *.bmp *.ppm *.pgm *.pbm)',
                )
            if len(unicode(logo)) > 0:
                print ("Setter ny logo: %s" % logo)

                l = QtGui.QPixmap()
                l.loadFromData(open(unicode(logo)).read())

                stream = QtCore.QBuffer()
                l.toImage().save(stream, 'PNG')
                #l.convertToImage().smoothScale(360,360, QtGui.QImage.ScaleMax).save(stream, 'PNG')

                #import sqlite

                #self.firma.logo = sqlite.encode(stream.getData())
                self.firma.logo = buffer(stream.data())
                self.visLogo()


