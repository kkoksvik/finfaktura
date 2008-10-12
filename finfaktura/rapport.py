#!/usr/bin/python -d
# -*- coding:utf8 -*-
###########################################################################
#    Copyright (C) 2005-2008- Håvard Gulldahl
#    <havard@lurtgjort.no>
#
#    Lisens: GPL2
#
# $Id: oppgradering.py 217 2007-05-02 23:25:16Z havard.dahle $
###########################################################################

import time, os, types
from string import join, split
import logging, subprocess

import fakturafeil

try:
    import reportlab
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import Paragraph, SimpleDocTemplate
    REPORTLAB=True
except ImportError:
    REPORTLAB=False
    #raise

PDFVIS = "/usr/bin/kpdf"

class rapport:
    u'Lager økonomisk rapport på pdf'
    oppdatert = False

    def __init__(self, filnavn=None, rapportinfo={}):
        if not REPORTLAB:
            raise fakturafeil.InstallasjonsFeil('python-reportlab er ikke installert. Kan ikke lage PDF!')
        if filnavn is None:
            import tempfile
            self.filnavn = tempfile.mkstemp(suffix='.pdf', prefix='rapport-')
        else:
            self.filnavn = filnavn
        self.info = rapportinfo
        self.stiler = getSampleStyleSheet()
        self.normal = self.stiler['BodyText']
        self.liste  = self.stiler['Bullet']
        self.overskrift = self.stiler['Heading3']
        self.seksjonover = self.stiler['Heading2']
        #print dir(self.seksjonover)
        self.tittel = self.stiler['Heading1']
        self.flow = []
        self.flow.append(Paragraph(u'Fakturaer hos %s' % self.info['firma'].firmanavn, self.tittel))
        self.flow.append(Paragraph(u'Generert av <i>Fryktelig Fin Faktura</i> den %s' % time.strftime("%Y-%m-%d", time.localtime()), self.normal))
        det = u'Viser fakturaer '
        if self.info['visubetalte']: det += u'(også ubetalte) '
        else: det += u'(ikke ubetalte) '
        if self.info['dato'] != (None, None):
            _fra, _til = self.info['dato']
            if _fra is not None: det += "fra %s" % time.strftime("%Y-%m", time.localtime(_fra))
            if _til is not None: det += "til %s" % time.strftime("%Y-%m", time.localtime(_til))
        if self.info['kunde'] is not None:
            det += u'sendt til %s' % self.info['kunde'].navn
        self.flow.append(Paragraph(det, self.normal))
        self.okonomi = {'inn':0.0, 'mva':0.0, 'b':0, 'u':0}
        self.seksjon = ''
        logging.debug(self.info)

    def lag(self):
        dok = SimpleDocTemplate(self.filnavn,pagesize = A4)
        #dok.setAuthor("%s (Fryktelig Fin Faktura)" % self.info.firma.kontaktperson)
        #dok.setTitle("Fakturaer hos %s" % self.info.firma.firmanavn)
        #canvas.setSubject("How to Generate PDF files using the ReportLab modules")
        dok.build(self.flow)
        self.oppdatert = True

    def vis(self, program=PDFVIS):
        if not self.oppdatert: self.lag()
        subprocess.call((program, self.filnavn))

    def lastOrdreliste(self, ordreliste):
        for o in ordreliste: self.leggTilOrdre(o)

    def leggTilOrdre(self, ordre):
        self.oppdatert = False
        status = ""
        if self.info['sortering'] is not None:
            if self.info['sortering'] == 'dato':
                _seksjon = time.strftime("%Y-%m", time.localtime(ordre.ordredato))
            elif self.info['sortering'] == 'kunde':
                _seksjon = ordre.kunde.navn
            if self.seksjon != _seksjon:
                self.flow.append(Paragraph(_seksjon, self.seksjonover))
                self.seksjon = _seksjon
        if ordre.kansellert:
            status = "<font color=red><b>kansellert</b></font>"
        elif ordre.betalt:
            status = "<font color=green>betalt</font>"
            self.okonomi['inn'] += ordre.finnPris()
            self.okonomi['mva'] += ordre.finnMva()
            self.okonomi['b'] += 1
        else:
            status = "<font color=red>ubetalt</font>"
            self.okonomi['u'] += 1
        self.flow.append(Paragraph("ordre <i># %04i</i> (%s), utformet til %s den %s\n" % (ordre._id, status, ordre.kunde.navn, time.strftime("%Y-%m-%d", time.localtime(ordre.ordredato))), self.overskrift))
        if ordre.linje:
            for vare in ordre.linje:
                self.flow.append(Paragraph("<li> #%i: %s </li>" % (vare._id, unicode(vare)), self.liste))
