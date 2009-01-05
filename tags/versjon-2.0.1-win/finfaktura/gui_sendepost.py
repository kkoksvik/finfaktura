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

from PyQt4 import QtGui
from ui import sendepost_ui

class sendEpost(sendepost_ui.Ui_sendEpost):
    def __init__(self, parent, ordre):
        self.parent = parent
        #sendepost_ui.Ui_sendEpost.__init__()
        self.gui = QtGui.QDialog()
        self.setupUi(self.gui)
        self.tittel.setText(u'Sender faktura til %s <b>&lt;%s</b>&gt;' % (ordre.kunde.navn, ordre.kunde.epost))
        self.tekst.setPlainText(u'Vedlagt følger epostfaktura #%i:\n%s\n\n-- \n%s\n%s' % (ordre.ID, ordre.tekst,  ordre.firma, ordre.firma.vilkar))
        self.gui.show()

    def exec_(self):
        res = self.gui.exec_()
        return res, unicode(self.tekst.toPlainText())