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
from ui import finfaktura_oppsett_ui

class finfakturaOppsett(finfaktura_oppsett_ui.Ui_FinFakturaOppsett):
    def __init__(self, faktura):
        self.faktura = faktura
        self.gui = QtGui.QDialog()
        self.setupUi(self.gui)
        self.gui.connect(self.oppsettFakturakatalogSok, QtCore.SIGNAL("clicked()"), self.endreFakturakatalog)
        self.gui.connect(self.oppsettProgrammerVisSok, QtCore.SIGNAL("clicked()"), self.endreProgramVis)

        self.vis()
        self.gui.show()

    def exec_(self):
        res = self.gui.exec_()
        if res == QtGui.QDialog.Accepted:
            logging.debug('oppdaterer')
            self.oppdater()
        return res

    def vis(self):
        self.oppsettFakturakatalog.setText(self.faktura.oppsett.fakturakatalog)
        self.oppsettProgramVisPDF.setText(self.faktura.oppsett.vispdf)

    def visningsProgrammer(self):
        p = {'kpdf (KDE3)': '/usr/bin/kpdf',
             'okular (KDE4)': '/usr/bin/okular',
             'Acrobat reader (win)': '',
             'Vis i Utforsker (win)': '',
            }

    def endreFakturakatalog(self):
        nu = self.oppsettFakturakatalog.text()
        startdir = nu
        ny = QtGui.QFileDialog.getExistingDirectory(self.gui,
            "Velg katalog fakturaene skal lagres i",
            startdir,
            QtGui.QFileDialog.ShowDirsOnly
            )
        if len(unicode(ny)) > 0:
            logging.debug("Setter ny fakturakataolg: %s" % ny)
            self.faktura.oppsett.fakturakatalog = unicode(ny)
            self.oppsettFakturakatalog.setText(unicode(ny))

    def endreProgramVis(self):
        ny = unicode(QtGui.QFileDialog.getOpenFileName(self.gui,
            u"Velg et program til å åpne PDF i",
            self.oppsettProgramVisPDF.text()))
        if len(ny) > 0:
            logging.debug("Setter nytt visningsprogram: %s" % ny)
            self.faktura.oppsett.vispdf = ny
            self.oppsettProgramVisPDF.setText(ny)

    def oppdater(self):
        logging.debug("Lager oppsett")
        self.faktura.oppsett.fakturakatalog = unicode(self.oppsettFakturakatalog.text())
        self.faktura.oppsett.vispdf = unicode(self.oppsettProgramVisPDF.text())

