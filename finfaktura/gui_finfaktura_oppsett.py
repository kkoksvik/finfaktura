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

import sys, logging, os.path, glob
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
        logging.debug('Fakturakatalog fra db: %s', repr(self.faktura.oppsett.fakturakatalog))
        logging.debug('pdf-prog fra db: %s', repr(self.faktura.oppsett.vispdf))
        self.oppsettFakturakatalog.setText(self.faktura.oppsett.fakturakatalog)
        if self.faktura.oppsett.vispdf:
            self.oppsettProgramVisPDF.addItem('Gjeldende valg (%s)' % self.faktura.oppsett.vispdf, QtCore.QVariant(self.faktura.oppsett.vispdf))
        p = {
             'kpdf (KDE3)': '/usr/bin/kpdf',
             'okular (KDE4)': '/usr/bin/okular',
             'evince (Gnome)': '/usr/bin/evince',
             'xpdf (X11)': '/usr/bin/xpdf',
             'epdfview (X11)': '/usr/bin/epdfview',
             'Acrobat reader (win)': '%SYSTEMDRIVE%\%PROGRAMFILES%\Adobe\Reader*\Reader\AcroRd32.exe',
             'Foxit reader (win)': '%SYSTEMDRIVE%\%PROGRAMFILES%\Foxit Software\Foxit Reader\Foxit Reader.exe',
            }
        for tekst, s in p.iteritems():
            sti = os.path.expandvars(s)
            logging.debug('sti %s, exists: %s', sti, os.path.exists(sti))
            if os.path.exists(sti):
                self.oppsettProgramVisPDF.addItem(tekst, QtCore.QVariant(sti + ' %s'))
            elif '*' in sti:
                for _sti in [ _s for _s in glob.glob(sti) if os.path.exists(_s) ]:
                    self.oppsettProgramVisPDF.addItem(tekst, QtCore.QVariant(_sti+ ' %s'))
        if sys.platform.startswith('win'):
            self.oppsettProgramVisPDF.addItem('Vis i Utforsker (win)', QtCore.QVariant('explorer /c,%s'))

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
            u"Velg et program å åpne PDF i",
            self.oppsettProgramVisPDF.itemData(self.oppsettProgramVisPDF.currentIndex()).toPyObject())
            )
        if len(ny) > 0:
            logging.debug("Setter nytt visningsprogram: %s" % ny)
            self.faktura.oppsett.vispdf = ny
            self.oppsettProgramVisPDF.insertItem(0, ny, QtCore.QVariant(ny))

    def oppdater(self):
        logging.debug("Lager oppsett")
        self.faktura.oppsett.fakturakatalog = unicode(self.oppsettFakturakatalog.text())
        self.faktura.oppsett.vispdf = unicode(self.oppsettProgramVisPDF.itemData(self.oppsettProgramVisPDF.currentIndex()).toPyObject())

