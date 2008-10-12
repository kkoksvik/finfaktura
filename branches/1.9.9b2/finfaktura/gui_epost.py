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
from ui import epost_ui
import epost


class epostOppsett(epost_ui.Ui_epostOppsett):
    def __init__(self, faktura):
        self.faktura = faktura
        self.gui = QtGui.QDialog()
        self.setupUi(self.gui)
        self._epostlosninger = [self.epostLosningAuto, self.epostLosningSmtp, self.epostLosningSendmail]
        self.gui.connect(self.epostLosningAuto, QtCore.SIGNAL("toggled(bool)"),
            lambda b: self.roterAktivSeksjon('auto'))
        self.gui.connect(self.epostLosningSmtp, QtCore.SIGNAL("toggled(bool)"),
            lambda b: self.roterAktivSeksjon('smtp'))
        self.gui.connect(self.epostLosningSendmail, QtCore.SIGNAL("toggled(bool)"),
            lambda b: self.roterAktivSeksjon('sendmail'))
        self.gui.connect(self.epostLosningTest, QtCore.SIGNAL("clicked()"), self.testEpost)

        self.vis()
        self.gui.show()

    def exec_(self):
        res = self.gui.exec_()
        if res == QtGui.QDialog.Accepted:
            logging.debug('oppdaterer')
            self.oppdaterEpost()
        return res

    def vis(self):
        if self.faktura.epostoppsett.bcc:
            self.sendKopi.setChecked(True)
            self.kopiAdresse.setText(self.faktura.epostoppsett.bcc)
        self.roterAktivSeksjon(self.faktura.epostoppsett.transport)
        self._epostlosninger[epost.TRANSPORTMETODER.index(self.faktura.epostoppsett.transport)].setChecked(True)
        if self.faktura.epostoppsett.smtpserver:
            self.smtpServer.setText(self.faktura.epostoppsett.smtpserver)
        if self.faktura.epostoppsett.smtpport:
            self.smtpPort.setValue(self.faktura.epostoppsett.smtpport)
        self.smtpTLS.setChecked(self.faktura.epostoppsett.smtptls)
        self.smtpAuth.setChecked(self.faktura.epostoppsett.smtpauth)
        if self.faktura.epostoppsett.smtpbruker: # husk brukernavn og passord for smtp
            self.smtpHuskEpost.setChecked(True)
            if self.faktura.epostoppsett.smtpbruker:
                self.smtpBrukernavn.setText(self.faktura.epostoppsett.smtpbruker)
            if self.faktura.epostoppsett.smtppassord:
                self.smtpPassord.setText(self.faktura.epostoppsett.smtppassord)
        if self.faktura.epostoppsett.sendmailsti:
            self.sendmailSti.setText(self.faktura.epostoppsett.sendmailsti)
        else:
            self.sendmailSti.setText('~')

    def oppdaterEpost(self):
        logging.debug("lagrer epost")
        self.faktura.epostoppsett.transport = self.finnAktivTransport()
        if not self.sendKopi.isChecked():
            self.kopiAdresse.setText('')
        self.faktura.epostoppsett.bcc = unicode(self.kopiAdresse.text())
        self.faktura.epostoppsett.smtpserver = unicode(self.smtpServer.text())
        self.faktura.epostoppsett.smtpport = self.smtpPort.value()
        self.faktura.epostoppsett.smtptls = self.smtpTLS.isChecked()
        self.faktura.epostoppsett.smtpauth = self.smtpAuth.isChecked()
        if self.smtpHuskEpost.isChecked():
            self.faktura.epostoppsett.smtpbruker = unicode(self.smtpBrukernavn.text())
            self.faktura.epostoppsett.smtppassord = unicode(self.smtpPassord.text())
        else:
            self.faktura.epostoppsett.smtpbruker = ''
            self.faktura.epostoppsett.smtppassord = ''
        self.faktura.epostoppsett.sendmailsti = unicode(self.sendmailSti.text())

    def roterAktivSeksjon(self, seksjon):
        logging.debug("roterer til %s er synlig" % seksjon)
        bokser = {'smtp':self.boxSMTP, 'sendmail':self.boxSendmail}
        if seksjon == 'auto': #vis alt
            map(lambda x: x.setEnabled(True), bokser.values())
            return
        for merke, box in bokser.iteritems():
            box.setEnabled(merke == seksjon)

    def testEpost(self):
        self.oppdaterEpost() # må lagre for å bruke de inntastede verdiene
        try:
            transport = self.faktura.testEpost(self.finnAktivTransport())
        except Exception,ex:
            logging.debug('Fikk feil: %s', ex)
            s = u'Epostoppsettet fungerer ikke. Oppgitt feilmelding:\n %s \n\nKontroller at de oppgitte innstillingene \ner korrekte' % ex.message
            trans = getattr(ex, 'transport')
            if trans != 'auto':
                ex.transportmetoder.remove(trans) # fjerner feilet metode fra tilgjengelig-liste
                s += u', eller prøv en annen metode.\nTilgjengelige metoder:\n%s' % ', '.join(ex.transportmetoder)
            self.alert(s)
        else:
            self.obs("Epostoppsettet fungerer. Bruker %s" % transport)
            try:
                self.epostLosning.setButton(epost.TRANSPORTMETODER.index(transport))
                self.roterAktivSeksjon(transport)
            except:pass
            self.oppdaterEpost() # må lagre for å bruke den aktive løsningen

    def finnAktivTransport(self):
        for i, w in enumerate(self._epostlosninger):
            if w.isChecked(): return epost.TRANSPORTMETODER[i]

    def alert(self, msg):
        QtGui.QMessageBox.critical(self.gui, "Feil!", msg, QtGui.QMessageBox.Ok)

    def obs(self, msg):
        QtGui.QMessageBox.information(self.gui, "Obs!", msg, QtGui.QMessageBox.Ok)
    #def epostVisAuth(self, vis):
        ##self.epostSmtpBrukernavn.setEnabled(vis)
        #self.epostSmtpPassord.setEnabled(vis)

