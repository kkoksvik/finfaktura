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
