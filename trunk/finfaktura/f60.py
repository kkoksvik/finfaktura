#!/usr/bin/python 
# -*- coding:utf-8 -*-
"""Produsere en faktura etter norsk standard f60"""
###########################################################################
#    Copyright (C) 2006 - Håvard Dahle
#    <havard@dahle.no>
#
#    Lisens: GPL2
#
# $Id$
###########################################################################

import time, os, types
from string import join, split

try:
    import reportlab
    from reportlab.pdfgen import canvas
    from reportlab.lib.units import mm
    from reportlab.lib.colors import yellow, pink, white
    REPORTLAB=True
except ImportError:
    REPORTLAB=False

__version__ = '0.8'

__doc__ = """Modul for å produsere en faktura etter norsk standard f60"""

class f60Eksisterer(Exception): pass
class f60Feil(Exception):pass

class f60:
    standardskrift = "Helvetica"
    standardstorrelse = 10
    kunde = {}
    firma = {}
    faktura = {}
    filnavn = ''

    def __init__(self, filnavn, overskriv = False):
        self.overskriv = overskriv
        if filnavn is None: # lag tempfil
            self.filnavn = self.lagTempFilnavn()
        else:
            self.filnavn = self.sjekkFilnavn(filnavn)
        self.canvas = canvas.Canvas(filename=self.filnavn)

    def data(self):
        f = open(self.filnavn)
        d = f.read()
        f.close()
        return d

    # ============= MÅ FYLLES INN AV BRUKER =============== #

    def settFakturainfo(self, fakturanr, utstedtEpoch, forfallEpoch, fakturatekst, vilkaar = ''):
        self.faktura['nr'] = int(fakturanr)
        self.faktura['utstedt'] = time.strftime("%Y-%m-%d", time.localtime(utstedtEpoch))
        self.faktura['forfall'] = time.strftime("%Y-%m-%d", time.localtime(forfallEpoch))
        self.faktura['tekst'] = self._s(fakturatekst)
        self.faktura['vilkaar'] = self._s(vilkaar)

    def settOrdrelinje(self, ordrelinje):
        self.ordrelinje = ordrelinje

    def settLogo(self, logo):
        if logo: self.firma['logo'] = logo
        else: raise f60Feil(u'Ugyldig logo: %s' % logo)

    def settFirmainfo(self, info):
        """info er en dictionary med følgende info:
            %(firmanavn)s
            %(kontaktperson)s
            %(adresse)s
            %(postnummer)04i %(poststed)s
            Telefon: %(telefon)s
            Bankkonto: %(kontonummer)s
            Org.nr: %(organisasjonsnummer)s
            Epost: %(epost)s"""
        for k in info.keys():
            self.firma[k] = self._s(info[k])
        
    def settKundeinfo(self, kundenr, adresse):
        self.kunde['nr'] = int(kundenr)
        self.kunde['adresse'] = self._s(adresse)

    # ==================== OFFENTLIGE FUNKSJONER ================ #

    def lagPost(self):
        self.fyll()
        return self.settSammen()

    def lagEpost(self):
        self.lagBakgrunn()
        self.fyll()
        return self.settSammen()
    
    def lagKvittering(self):
        self.lagBakgrunn()
        self.fyll()
        self.lagKopimerke()
        return self.settSammen()

    def lagTempFilnavn(self):
        from tempfile import mkstemp
        f,filnavn = mkstemp(".pdf", "faktura-")
        #print dir(f)
        #f.close()
        return filnavn

    def skrivUt(self):
        if not os.path.exists(self.filnavn):
            raise "Feil filnavn"
        os.system('kprinter "%s"' % self.filnavn) ### XXX: fiks dette 

    # ==================== INTERNE FUNKSJONER ================ #
    
    def sjekkFilnavn(self, filnavnUtf8):
        filnavn = ''
        for b in filnavnUtf8: # XXX: reportlab støtter ikke utf8-filnavn...
            if ord(b) < 128: filnavn += b
            else: filnavn += '_'
        (katalog, fil) = os.path.split(os.path.expanduser(filnavn))
        if not os.path.exists(katalog):
            os.mkdir(katalog)
        filnavn = os.path.join(katalog, fil)
        if not self.overskriv and os.path.exists(filnavn):
            raise f60Eksisterer(filnavn)
        return filnavn

    def paragraf(self, t, par_bredde = 80):
        """Setter inn linjeskift for å sørge for at teksten aldri overskrider en viss bredde"""
        if not t: return ''
        if len(t) < par_bredde: return [t,]

        ret = ()
        i = par_bredde
        while len(t) > par_bredde:
            if t[i] == " ":
                ret += (t[:i],)
                t = t[i+1:]
            else:
                i -= 1
        ret += (t, )
        return list(ret)
        #return join(ret, "\n")

    def kutt(self, t, lengde = 200):
        """Kutter en tekst hvis den overstiger en gitt lengde"""
        if len(t) > lengde: t = "%s..." % t[:lengde-3]
        return t

    def _s(self, t):
        """Sørger for at tekst er i riktig kodesett (encoding)"""
        if not type(t) in (types.StringType,types.UnicodeType): return t
        # Reportlab 2.x vil ha unicode
        if reportlab.Version[0] == '2':
            try: 
                return unicode(t)
            except UnicodeDecodeError:
                return unicode(t, 'latin1')
        #elif reportlab.Version[0] == '1':
        else: # Reportlab 1.x vil ha latin1
            try: 
                return unicode(t).encode('latin1')
            except UnicodeDecodeError:
                return unicode(t, 'latin1').encode('latin1')

    def lagBakgrunn(self):
        "Lager den gule giroblanketten, bare for bruk til epostpdf, ikke print"

        # a4 format spec:
        # http://www.cl.cam.ac.uk/~mgk25/iso-paper.html
        # 210 x 297

        # faktura spek:
        # Norsk Standard f60
        # url: ?
        self.canvas.saveState()
        self.canvas.setFillColor(yellow)
        self.canvas.rect(0*mm, 101*mm, 210*mm, 21*mm, stroke=0, fill=1)
        self.canvas.rect(0*mm, 33*mm, 210*mm, 9*mm, stroke=0, fill=1)
        self.canvas.rect(0*mm, 14*mm, 210*mm, 2*mm, stroke=0, fill=1)

        self.canvas.setFillColor(white)
        self.canvas.rect(80*mm, 103*mm, 36*mm, 9*mm, stroke=0, fill=1)
        self.canvas.rect(121*mm, 103*mm, 40*mm, 9*mm, stroke=0, fill=1)
        self.canvas.rect(171*mm, 103*mm, 30*mm, 9*mm, stroke=0, fill=1)

        self.canvas.lines([(9*mm, 16*mm, 9*mm, 30*mm), (80*mm, 16*mm, 80*mm, 30*mm)])

        self.canvas.restoreState()
        blankettnr = "xxxxxxx"
        self.canvas.drawString(173*mm, 105*mm, blankettnr)
        self.canvas.drawString(173*mm, 20*mm, blankettnr)

    def lagKopimerke(self):
        """Lager teksten "Kvittering" på skrå over fakturaen"""
        self.canvas.saveState() # lagrer gjeldende oppsett
        merke = self.canvas.beginText()
        self.canvas.rotate(45)
        merke.setFillGray(0.6)
        merke.setFont("Helvetica", 70)
        merke.setTextOrigin(90*mm, 30*mm)
        merke.textLines("KVITTERING\n\n\nKVITTERING")
        self.canvas.drawText(merke)
        self.canvas.restoreState() # henter tilbake normalt oppsett

    def fyll(self): #, firma, faktura):
        "Fyller fakturaen med data"

        #firma.sjekkData() # sjekker at ndvendig firmainfo er fylt ut

        # logo
        logoForskyvning = 0
        if self.firma.has_key('logo') and self.firma['logo']:
            debug("Har logo!")
            try: import Image
            except ImportError: pass
            else:
                import StringIO
                l = StringIO.StringIO(self.firma['logo'])
                logo = Image.open(l)
                self.canvas.drawInlineImage(logo, 10*mm, 267*mm, width=25*mm, height=25*mm)
                logoForskyvning = 30

        # firmanavn: overskrift
        firmanavn = self.canvas.beginText()
        firmanavn.setTextOrigin((15+logoForskyvning)*mm, 270*mm) # skyv til høyre dersom logo
        firmanavn.setFont("Helvetica-Bold", 16)
        firmanavn.textLine(self.firma['firmanavn'])
        self.canvas.drawText(firmanavn)

        # firmainfo: oppe til høyre i liten skrift
        firmainfo = self.canvas.beginText()
        firmainfo.setTextOrigin(160*mm, 290*mm)
        firmainfo.setFont("Helvetica", 8)
        firmainfo.setFillGray(0.3)
        firmainfo.textLines(split("""%(kontaktperson)s
%(adresse)s
%(postnummer)04i %(poststed)s
Telefon: %(telefon)s
Bankkonto: %(kontonummer)s
Org.nr: %(organisasjonsnummer)s
Epost: %(epost)s""" % (self.firma), "\n"))
        self.canvas.drawText(firmainfo)


        self.canvas.line(5*mm, 265*mm, 205*mm, 265*mm)
        self.canvas.setFont("Helvetica", 10)

        # informasjon om kunden
        kunde = self.canvas.beginText()
        kunde.setFillGray(0.0)
        kunde.setTextOrigin(20*mm, 260*mm)
        kunde.textLines(split("Kunde# %03i\n%s" % (self.kunde['nr'], self.kunde['adresse']), '\n'))
        self.canvas.drawText(kunde)

        # detaljer om fakturaen
        sidenr = 1
        totalsider = 1
        fakturafakta = self.canvas.beginText()
        fakturafakta.setTextOrigin(150*mm, 260*mm)
        fakturafakta.textLines("""FAKTURA
Fakturanr : %04i
Fakturadato: %s
Forfallsdato: %s
Side: %i av %i
        """ % (self.faktura['nr'],
               self.faktura['utstedt'],
               self.faktura['forfall'],
               sidenr,
               totalsider)
               )
        self.canvas.drawText(fakturafakta)

        fakturatekst = self.canvas.beginText()
        fakturatekst.setTextOrigin(20*mm, 230*mm)
        fakturatekst.textLines(self.paragraf(self.faktura['tekst'], 100))
        fakturatekstNedreY = int(fakturatekst.getY() / mm)
        debug("fakturateksten strekker seg ned til Y: %i mm (%i PDF pt)" % (fakturatekstNedreY/mm, fakturatekstNedreY))
#         if fakturatekstNedreY > sikkerhetsgrense: tekst = self.kutt(faktura.tekst) ...
        self.canvas.drawText(fakturatekst)

        regnestykkeY = 215
        if fakturatekstNedreY < regnestykkeY: regnestykkeY = fakturatekstNedreY - 10
        self.canvas.drawString(20*mm, regnestykkeY*mm, "Beskrivelse")
        self.canvas.drawRightString(140*mm, regnestykkeY*mm, "Pris")
        self.canvas.drawRightString(160*mm, regnestykkeY*mm, "Mva")
        self.canvas.drawRightString(180*mm, regnestykkeY*mm, "SUM")
        self.canvas.setDash(1,0)
        self.canvas.setLineWidth(0.2*mm)
        self.canvas.line(15*mm, (regnestykkeY-2)*mm, 195*mm, (regnestykkeY-2)*mm)
        self.canvas.setFont("Helvetica", 8)

        tekstX = 20*mm
        Y      = (regnestykkeY-10)*mm
        bruttoX= 140*mm
        mvaX   = 160*mm
        prisX  = 180*mm

        totalBelop = 0
        totalMva = 0
        totalBrutto = 0
        
        if type(self.ordrelinje) in (types.FunctionType, types.MethodType):
            for vare in self.ordrelinje():
                brutto = vare.kvantum * vare.enhetspris
                mva = brutto * vare.mva / 100
                pris = brutto + mva
                totalBrutto += brutto
                totalMva += mva
                totalBelop += pris
                self.canvas.drawString(tekstX, Y, self._s(vare.detaljertBeskrivelse()))
                self.canvas.drawRightString(bruttoX, Y, "%.2f" % (brutto))
                self.canvas.drawRightString(mvaX, Y, "%.2f" % (mva))
                self.canvas.drawRightString(prisX, Y, "%.2f" % (pris))
                Y -= 7*mm
        elif type(self.ordrelinje) == types.ListType:
            for vare in self.ordrelinje:
                # [tekst, kvantum, enhetspris, mva]
                brutto = vare[1] * vare[2]
                mva = brutto * vare[3] / 100
                pris = brutto + mva
                totalBrutto += brutto
                totalMva += mva
                totalBelop += pris
                self.canvas.drawString(tekstX, Y, "%s %s a kr %s" % (vare[1], vare[0], vare[2]))
                self.canvas.drawRightString(bruttoX, Y, "%.2f" % (brutto))
                self.canvas.drawRightString(mvaX, Y, "%.2f" % (mva))
                self.canvas.drawRightString(prisX, Y, "%.2f" % (pris))
                Y -= 7*mm

        debug("Nå har vi kommet til Y: %i (%i)" % (Y/mm, Y))
#         if Y < 140*mm: self.lagNySide() # vi har lagt inn for mange varer til at vi får plass på en side

        sumY = 131*mm
        #belop = faktura.finnPris() + faktura.finnMva()
        self.canvas.line(110*mm, sumY, 190*mm, sumY)
        #self.canvas.drawRightString(prisX-30*mm, sumY-7*mm, "MVA: %.2f" % totalMva)
        #self.canvas.setFont("Helvetica-Bold", 10)
        #self.canvas.drawRightString(prisX, sumY-7*mm, "SUM: %.2f" % totalBelop)

        self.canvas.drawRightString(prisX-70*mm, sumY-7*mm, "Netto: %.2f" % totalBrutto)
        self.canvas.drawRightString(prisX-40*mm, sumY-7*mm, "MVA: %.2f" % totalMva)
        self.canvas.setFont("Helvetica-Bold", 10)
        self.canvas.drawRightString(prisX, sumY-7*mm, "TOTALT: %.2f" % totalBelop)

        # standard betalingsvilkår
        if len(self.faktura['vilkaar']):
            self.canvas.setFont("Helvetica", 10)
            vilkar = self.canvas.beginText()
            vilkar.setTextOrigin(15*mm, 130*mm)
            vilkar.textLines(self.paragraf(self.faktura['vilkaar'], 35).upper())
            self.canvas.drawText(vilkar)

        # Nederste del av skjemaet
        # den gule betalingsslippen
        self.canvas.setFont("Helvetica-Bold", 14)
        self.canvas.drawString(15*mm, 118*mm, "KVITTERING")
        self.canvas.setFont("Helvetica", 10)
        self.canvas.drawString(15*mm, 110*mm, "Innbetalt til konto")
        self.canvas.setFont("Courier", 10)
        self.canvas.drawString(20*mm, 105*mm, str(self.firma['kontonummer']))

        self.canvas.drawString(88*mm, 105*mm, "%.2f" % totalBelop)

        # betalingsfrist
        from time import strftime, localtime
        self.canvas.drawString(170*mm, 92*mm, self.faktura['forfall'])

        # fakturainformasjon
        t = self.canvas.beginText()
        t.setTextOrigin(15*mm, 90*mm)
        t.textLines("Kundenr: %04i\nFakturanr: %04i\nFakturadato: %s" % \
            (self.kunde['nr'], self.faktura['nr'], self.faktura['utstedt']))
        self.canvas.drawText(t)

        # mottakerfelt
        kundeinfo = self.canvas.beginText()
        kundeinfo.setTextOrigin(15*mm, 70*mm)
        kundeinfo.textLines(split(self.kunde['adresse'], '\n'))
        self.canvas.drawText(kundeinfo)

        # avsenderfelt
        firmaadresse = self.canvas.beginText()
        firmaadresse.setTextOrigin(115*mm, 70*mm)
        firmaadresse.textLines(split("%(firmanavn)s\n%(kontaktperson)s\n%(adresse)s\n%(postnummer)04i %(poststed)s" % (self.firma), '\n'))
        self.canvas.drawText(firmaadresse)

        # KID
        #self.canvas.drawString(14*mm, 20*mm, str(self.lagKid()))

        # SUM
        kr = int(totalBelop)
        ore = int((totalBelop - kr) * 100)
        self.canvas.drawString(90*mm, 20*mm, str(kr))
        self.canvas.drawString(110*mm, 20*mm, "%02d" % ore)
        self.canvas.drawString(135*mm, 20*mm, str(self.firma['kontonummer']))

    def settSammen(self):
        self.canvas.showPage()
        self.canvas.save()
        return True

def debug(s):
    print "[f60]:",s


if __name__ == '__main__':
    #test
    filnavn = '/tmp/testfaktura.pdf'
    faktura = f60(filnavn, overskriv=True)
    faktura.settFakturainfo(03, 1145542709, 1146546709, u"Rå løk")
    faktura.settFirmainfo({'firmanavn':'Test Firma Ein',
                           'kontaktperson':'Rattatta Hansen',
                           'adresse':u'Surdalsøyra',
                           'postnummer':8999,
                           'poststed':u'Fløya',
                           'kontonummer':97101164680,
                           'organisasjonsnummer':876876,
                           'telefon':23233322,
                           'epost':'ratata@ta.no'})
    faktura.settKundeinfo(06, "Topert\nRopertgata 33\n9022 Nissedal")
    faktura.settOrdrelinje([ ["Leder", 1, 300, 25], ['Reportasje', 1, 3000, 25], ])
    if faktura.lagKvittering():
        print "Kvittering laget i", filnavn
    else:
        print "Kvittering kunne ikke lagres i", filnavn
    
