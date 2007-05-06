#!/usr/bin/python -d
# -*- coding:utf8 -*-
###########################################################################
#    Copyright (C) 2005-2007 - Håvard Dahle
#    <havard@dahle.no>
#
#    Lisens: GPL2
#
# $Id: oppgradering.py 217 2007-05-02 23:25:16Z havard.dahle $
###########################################################################

import time, os, types
from string import join, split

try:
    import reportlab
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import Paragraph, SimpleDocTemplate
    REPORTLAB=True
except ImportError:
    REPORTLAB=False
    #raise

class rapport:
    u'Lager økonomisk rapport på pdf'
    oppdatert = False
    
    def __init__(self, filnavn=None, rapportinfo={}):
        self.filnavn = filnavn
        self.info = rapportinfo
        self.stiler = getSampleStyleSheet()
        self.normal = self.stiler['BodyText']
        self.liste  = self.stiler['Bullet']
        self.overskrift = self.stiler['Heading3']
        self.tittel = self.stiler['Heading1']
        self.flow = []
        self.flow.append(Paragraph(u'Økonomisk rapport fra <i>Fryktelig Fin Faktura</i>', self.tittel))
        #self.flow.append(Paragraph(u'Rapport over '+self.rapportnavn, self.normal))
        #canvas.setAuthor("the ReportLab Team")
        #canvas.setTitle("ReportLab PDF Generation User Guide")
        #canvas.setSubject("How to Generate PDF files using the ReportLab modules")

    def lag(self):
        dok = SimpleDocTemplate(self.filnavn,pagesize = A4)
        dok.build(self.flow)
        self.oppdatert = True
        
    def vis(self):
        if not self.oppdatert: self.lag()
        os.system('kpdf %s' % self.filnavn)
        
    def lastOrdreliste(self, ordreliste):
        for o in ordreliste: self.leggTilOrdre(o)
    
    def leggTilOrdre(self, ordre):
        self.oppdatert = False
        #self.flow.append(Paragraph("%s: %s" % (time.strftime("%Y-%m-%d", time.localtime(ordre.ordredato)), ordre.tekst), self.head))
        status = ""
        if ordre.kansellert:
            status = "<font color=red><b>kansellert</b></font>"
        elif ordre.betalt:
            status = "<font color=green>betalt</font>"
        else:
            status = "<font color=red>ubetalt</font>"
        self.flow.append(Paragraph("ordre <i># %04i</i> (%s), utformet til %s den %s\n" % (ordre._id, status, ordre.kunde.navn, time.strftime("%Y-%m-%d", time.localtime(ordre.ordredato))), self.overskrift))
        if ordre.linje:
            for vare in ordre.linje:
                self.flow.append(Paragraph("<li> #%i: %s </li>" % (vare._id, unicode(vare)), self.liste))
