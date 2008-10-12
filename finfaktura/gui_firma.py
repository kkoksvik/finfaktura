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

import logging
from PyQt4 import QtCore, QtGui
from ui import firmainfo_ui
from fakturabibliotek import typeofqt

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
        self.gui.show()
        self.vis()
        #self.visLogo()


    def exec_(self):
        res = self.gui.exec_()
        if res == QtGui.QDialog.Accepted:
            return self.samleInfo()
        return {}

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
        format = { self.Postnummer: "%04i", } # må formateres spesielt dersom det begynner med 0, eks. 0921
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
            self.lagreLogo.setText('&Finn logo')
            #self.LogoPixmap.setPixmap(QtGui.QPixmap())
            self.LogoPixmap.clear()
        else:
            #pass
            logging.debug('visLogo: %s, %s', repr(self.firma.logo), len(self.firma.logo))
            logo = QtGui.QPixmap()
            logo.loadFromData(self.firma.logo)
            self.LogoPixmap.setPixmap(logo)
            self.lagreLogo.setText('&Fjern logo')

    def kanskjetall(self, obj):
        try:
            return int(obj.text())
        except ValueError:
            return None

    def samleInfo(self):
        r = {}
        r['firmanavn'] = unicode(self.Firmanavn.text())
        r['organisasjonsnummer'] = unicode(self.Organisasjonsnummer.text())
        r['kontaktperson'] = unicode(self.Kontaktperson.text())
        r['epost'] = unicode(self.Epost.text())
        r['adresse'] = unicode(self.Adresse.toPlainText())
        r['postnummer'] = self.kanskjetall(self.Postnummer)
        r['poststed'] = unicode(self.Poststed.text())
        r['telefon'] = self.kanskjetall(self.Telefon)
        r['mobil'] = self.kanskjetall(self.Mobil)
        r['telefaks'] = self.kanskjetall(self.Telefaks)
        r['kontonummer'] = self.kanskjetall(self.Kontonummer)
        r['vilkar'] = unicode(self.Vilkar.toPlainText())
        r['mva'] = int(self.Mva.value())
        r['forfall'] = int(self.Forfall.value())
        return r

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
            mangel = u'Du er nødt til å oppgi:\n%s' % ([ mangler[obj].lower() for obj in mangler.keys() ])
            logging.debug (mangel)
            QtGui.QMessageBox.critical(self.gui, 'Ufullstendige opplysninger', mangel)
            mangler.keys()[0].setFocus()
            return False

    def sjekkFirmaMangler(self):
        kravkart = {}
        kravkart.update(self._kontrollkart)
        test = None
        for obj in kravkart.keys():
            if isinstance(obj, QtGui.QSpinBox): test = obj.value() > 0
            elif isinstance(obj, QtGui.QComboBox): test = obj.currentText()
            elif isinstance(obj, (QtGui.QLineEdit,QtGui.QTextEdit,)): test = obj.text()
            if test is None:
                logging.error('sjekkFirmaMangler: mangler test for % obj')
            elif test: kravkart.pop(obj)
        return kravkart

    def firmaSjekk(self, event=None):
        ok = QtGui.QColor('white')
        tom = QtGui.QColor('red')
        widget = 'QWidget'
        for obj in self._kontrollkart.keys():
            if isinstance(obj, (QtGui.QSpinBox, QtGui.QDoubleSpinBox)): test = obj.value() > 0
            elif isinstance(obj, QtGui.QComboBox): test = obj.currentText()
            elif isinstance(obj, (QtGui.QLineEdit,QtGui.QTextEdit,)): test = obj.text()
            elif isinstance(obj, (QtGui.QPlainTextEdit,)): test = obj.toPlainText()
            else:
                logging.error('mangler test for %s (%s)' % (obj, type(obj)))
            if test:
                #obj.setPaletteBackgroundColor(ok)
                #logging.debug('firmaSjekk: ok for %s', obj.typeName())
                obj.setStyleSheet("%s { background-color: white; }" % typeofqt(obj))
            else:
                obj.setStyleSheet("%s { background-color: red; }" % typeofqt(obj))
                #obj.setPaletteBackgroundColor(tom)

    def finnFjernLogo(self):
        logging.debug('finnFjernLogo %s', repr(self.firma.logo))
        logging.debug('finnFjern lengde %s', len(str(self.firma.logo)))
        if (self.firma.logo):
            logging.debug('fjerner logo %s', repr(self.firma.logo))
            self.firma.logo = ''
            self.visLogo()
        else:
            startdir = ""
            logofile = QtGui.QFileDialog.getOpenFileName(self.gui,
                "Velg bildefil for firmaets logo",
                startdir,
                'Bildefiler (*.png *.xpm *.jpg *.jpeg *.gif *.bmp *.ppm *.pgm *.pbm)',
                )
            if len(unicode(logofile)) > 0:
                logging.debug ("Setter ny logo: %s" % logofile)

                logo = QtGui.QPixmap(logofile)
                if logo.isNull(): # kunne ikke åpne logo
                    return False

                stream = QtCore.QBuffer()
                scaledlogo = logo.scaled(QtCore.QSize(360,360), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
                scaledlogo.save(stream, 'PNG')
                #self.firma.logo = buffer(stream.data())
                self.firma.logo = buffer(str(stream.data()))
                logging.debug('logo: %s %s %s', type(self.firma.logo), len(self.firma.logo), repr(self.firma.logo))
                self.visLogo()

                #self.firma.hentEgenskaper()
                #logging.debug('hentet egenskaper. logo: %s, %s', type(self.firma.logo), len(self.firma.logo))