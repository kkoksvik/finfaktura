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

        #self.connect(self.oppsettFakturakatalogSok, QtCore.SIGNAL("clicked()"), self.endreFakturakatalog)
        #self.connect(self.oppsettProgrammerVisSok, QtCore.SIGNAL("clicked()"), self.endreProgramVis)
        #self.connect(self.oppsettProgrammerUtskriftSok, QtCore.SIGNAL("clicked()"), self.endreProgramUtskrift)
        #self.connect(self.oppsettLagre, QtCore.SIGNAL("clicked()"), self.oppdaterOppsett)

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

