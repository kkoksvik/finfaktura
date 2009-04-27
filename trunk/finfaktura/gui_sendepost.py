# -*- coding: utf-8 -*-
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

import sys, os, logging
from PyQt4 import QtCore, QtGui
from ui import sendepost_ui

class sendEpost(sendepost_ui.Ui_sendEpost):
    _vedlegg = []
    def __init__(self, parent, ordre):
        self.parent = parent
        self.gui = QtGui.QDialog()
        self.setupUi(self.gui)
        self.tittel.setText(u'Sender faktura til %s <b>&lt;%s</b>&gt;' % (ordre.kunde.navn, ordre.kunde.epost))
        self.tekst.setPlainText(u'Vedlagt følger epostfaktura #%i:\n%s\n\n-- \n%s\n%s' % (ordre.ID, ordre.tekst,  ordre.firma, ordre.firma.vilkar))
        self.gui.connect(self.leggVedFil, QtCore.SIGNAL("clicked()"), self.lagVedlegg)
        self.vedlegg.hide()
        self.gui.show()

    def lagVedlegg(self):
        f = QtGui.QFileDialog.getOpenFileName(self.gui,
            u"Velg en fil å legge ved",
            os.getenv('HOME', '.'))
        if len(f) > 0:
            self.vedlegg.show()
            logging.debug("Legger ved fil: %s", unicode(f))
            self._vedlegg.append(unicode(f).encode(sys.getfilesystemencoding()))
            i = QtGui.QTreeWidgetItem([f, '', ''])
            self.vedlegg.addTopLevelItem(i)
            
    def exec_(self):
        res = self.gui.exec_()
        return res, unicode(self.tekst.toPlainText())