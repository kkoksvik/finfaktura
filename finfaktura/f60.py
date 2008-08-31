# -*- coding:utf-8 -*-
"""Denne modulen lager en PDF-faktura etter norsk standard f60

PDF-filen kan skrives ut på f60-skjema, eller sendes som en elektronisk
versjon av denne.

Her er et eksempel på hvordan man bruker modulen:

filnavn = '/tmp/testfaktura.pdf'
faktura = f60(filnavn, overskriv=True)
faktura.settFakturainfo(
  fakturanr=03,
  utstedtEpoch=1145542709,
  forfallEpoch=1146546709,
  fakturatekst=u"Produksjon i august",
  vilkaar=u"Takk for handelen, kom gjerne igjen.",
  kid='4466986711175280')
faktura.settFirmainfo({'firmanavn':'Firma Ein',
                        'kontaktperson':'Rattatta Hansen',
                        'adresse':u'Surdalsøyra',
                        'postnummer':8999,
                        'poststed':u'Fløya',
                        'kontonummer':99999999999,
                        'organisasjonsnummer':876876,
                        'telefon':23233322,
                        'epost':'ratata@ta.no'})
faktura.settKundeinfo(06, "Topert\nRopertgata 33\n9022 Nissedal")
faktura.settOrdrelinje([ ["Leder", 1, 300, 25], ['Reportasje', 1, 3000, 25], ])
if faktura.lagEpost():
    print "Kvittering laget i", filnavn

Se forøvrig http://code.google.com/p/finfaktura/wiki/PythonF60
"""
###########################################################################
#    Copyright (C) 2005-2008- Håvard Gulldahl
#    <havard@lurtgjort.no>
#
#    Lisens: GPL2
#
# $Id$
###########################################################################

import time, os, types
from string import join, split
import logging

try:
    import reportlab
    from reportlab.pdfgen import canvas
    from reportlab.lib.units import mm
    from reportlab.lib.colors import yellow, pink, white
    REPORTLAB=True
except ImportError:
    REPORTLAB=False

__version__ = '0.10'
__license__ = 'GPLv2'

class f60Eksisterer(Exception): pass
class f60Feil(Exception): pass
class f60FeilKID(Exception): pass

PDFUTSKRIFT = '/usr/bin/kprinter'

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

    def settFakturainfo(self, fakturanr, utstedtEpoch, forfallEpoch, fakturatekst, vilkaar = '', kid = None):
        """Sett vital info om fakturaen"""
        self.faktura['nr'] = int(fakturanr)
        self.faktura['utstedt'] = time.strftime("%Y-%m-%d", time.localtime(utstedtEpoch))
        self.faktura['forfall'] = time.strftime("%Y-%m-%d", time.localtime(forfallEpoch))
        self.faktura['tekst'] = self._s(fakturatekst)
        self.faktura['vilkaar'] = self._s(vilkaar)
        if kid and not self.sjekkKid(kid): raise f60FeilKID(u'KID-nummeret er ikke riktig')
        self.faktura['kid'] = kid

    def settOrdrelinje(self, ordrelinje):
        """Sett fakturaens ordrelinjer. Kan være
        1. en list() hvor hver ordre er en
          sekvens: [tekst, kvantum, enhetspris, mva]

        2. en funksjon eller en metode som returnerer et objekt
          med følgende egenskaper: .tekst, .kvantum, .enhetspris, .mva
        """
        self.ordrelinje = ordrelinje

    def settLogo(self, logo):
        """Setter logoen som kommer oppe til venstre på fakturaen.
        Må være en str(), i et bildeformat som er lesbart av PIL."""
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
        "Ferdigstiller dokumentet for utskrift på papir (uten F60 skjemafelt)"
        self.fyll()
        return self.settSammen()

    def lagEpost(self):
        "Ferdigstiller dokumentet for elektronisk forsendelse (med F60 skjemafelt)"
        self.lagBakgrunn()
        self.fyll()
        return self.settSammen()

    def lagKvittering(self):
        "Ferdigstiller en kvittering for utskrift på papir (med F60 skjemafelt)"
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

    def skrivUt(self, program=PDFUTSKRIFT):
        "Skriver ut den produserte PDF-filen"
        if not os.path.exists(self.filnavn):
            raise "Feil filnavn"
        os.system('"%s" "%s"' % (program, self.filnavn)) ### XXX: fiks dette

    def sjekkKid(self, kid):
        "Kontrollerer et kid-nr etter mod10/luhner-algoritmen. Returnerer True/False"
        #http://no.wikipedia.org/wiki/KID
        #hvert andre siffer (bakfra) skal dobles og tverrsummene av alle produktene legges sammen
        #totalsummen skal så moduleres med 10, uten rest

        #denne implementasjonen opprinnelig fra
        # http://www.elifulkerson.com
        try:
            cc = map(int, str(kid))
            cc.reverse() # snu rekken slik at vi jobber bakfra
        except TypeError:
            return False

        total = 0
        for a in range(0, len(cc)):
            if (a % 2) == 1: # hvert andre siffer
                assert(cc[a] >= 0 and cc[a] <= 9)
                d = cc[a]*2 # dobles
                if d < 10: total += d
                else: total += d - 9 # tverrsum
            else:
                total += cc[a]
        return (total % 10) == 0 # mod10 uten rest

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
        """Bryter teksten med harde linjeskift på en gitt bredde, 80 tegn hvis ikke annet er oppgitt"""
        #if not t: return ''
        assert(type(t) in (types.StringType, types.UnicodeType))
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
        "Lager de gule skjemafeltene. Se .lagEpost() og .lagKvittering()"

        # a4 format spec:
        # http://www.cl.cam.ac.uk/~mgk25/iso-paper.html
        # 210 x 297
        # faktura spek:
        # Norsk Standard f60
        # url: ?
        self.canvas.saveState()
        self.canvas.setFillColor(yellow)
        # Lag de gule feltene
        self.canvas.rect(0*mm, 101*mm, 210*mm, 21*mm, stroke=0, fill=1)
        self.canvas.rect(0*mm, 33*mm, 210*mm, 9*mm, stroke=0, fill=1)
        self.canvas.rect(0*mm, 14*mm, 210*mm, 2*mm, stroke=0, fill=1)

        self.canvas.setFillColor(white)
        # Legg de hvite feltene oppå for "gjennomsiktighet"
        self.canvas.rect(80*mm, 103*mm, 36*mm, 9*mm, stroke=0, fill=1) # beløp
        self.canvas.rect(126*mm, 103*mm, 40*mm, 9*mm, stroke=0, fill=1) # betalerens kontonummer
        self.canvas.rect(170*mm, 103*mm, 31*mm, 9*mm, stroke=0, fill=1) # blankettnummer

        self.canvas.lines([(9*mm, 16*mm, 9*mm, 30*mm), (80*mm, 16*mm, 80*mm, 30*mm)])

        self.canvas.restoreState()
        blankettnr = "xxxxxxx"
        self.canvas.drawString(173*mm, 105*mm, blankettnr)
        self.canvas.drawString(173*mm, 22*mm, blankettnr)

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
            logging.debug("Har logo!")
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
        #for z,y in self.firma.iteritems():
            #logging.debug("%s (%s): %s" % (z, type(y), y))
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
        #logging.debug("fakturateksten strekker seg ned til Y: %i mm (%i PDF pt)" % (fakturatekstNedreY/mm, fakturatekstNedreY))
        #if fakturatekstNedreY > sikkerhetsgrense: tekst = self.kutt(faktura.tekst) ...
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

        mvagrunnlag = {} # Holder en oppsummering av salg per mva-sats

        if type(self.ordrelinje) in (types.FunctionType, types.MethodType):
            for vare in self.ordrelinje():

                # regn ut alt som skal regnes
                brutto = vare.kvantum * vare.enhetspris
                mva = brutto * vare.mva / 100
                pris = brutto + mva
                totalBrutto += brutto
                totalMva += mva
                totalBelop += pris

                if not vare.mva in mvagrunnlag.keys(): # legg til i oppsummeringen av salg
                    mvagrunnlag[vare.mva] = []
                mvagrunnlag[vare.mva] += [brutto,]

                self.canvas.drawString(tekstX, Y, self._s(vare.detaljertBeskrivelse()))
                self.canvas.drawRightString(bruttoX, Y, "%.2f" % (brutto))
                self.canvas.drawRightString(mvaX, Y, "%.2f" % (mva))
                self.canvas.drawRightString(prisX, Y, "%.2f" % (pris))
                Y -= 3*mm
        elif type(self.ordrelinje) == types.ListType:
            for vare in self.ordrelinje:
                # [tekst, kvantum, enhetspris, mva]

                # regn ut alt som skal regnes
                brutto = vare[1] * vare[2]
                mva = brutto * vare[3] / 100
                pris = brutto + mva
                totalBrutto += brutto
                totalMva += mva
                totalBelop += pris

                if not vare[3] in mvagrunnlag.keys(): # legg til i oppsummeringen av salg
                    mvagrunnlag[vare[3]] = []
                mvagrunnlag[vare[3]] += [brutto,]

                self.canvas.drawString(tekstX, Y, "%s %s a kr %s" % (vare[1], vare[0], vare[2]))
                self.canvas.drawRightString(bruttoX, Y, "%.2f" % (brutto))
                self.canvas.drawRightString(mvaX, Y, "%.2f" % (mva))
                self.canvas.drawRightString(prisX, Y, "%.2f" % (pris))
                Y -= 3*mm

        #logging.debug("Nå har vi kommet til Y: %i (%i)" % (Y/mm, Y))
        #if Y < 140*mm: self.lagNySide() # vi har lagt inn for mange varer til at vi får plass på en side

        sumY = 131*mm
        self.canvas.line(90*mm, sumY, 190*mm, sumY)

        # legg sammen totalen
        self.canvas.drawRightString(prisX-70*mm, sumY-7*mm, "Netto: %.2f" % totalBrutto)
        self.canvas.drawRightString(prisX-40*mm, sumY-7*mm, "MVA: %.2f" % totalMva)
        self.canvas.setFont("Helvetica-Bold", 10)
        self.canvas.drawRightString(prisX, sumY-7*mm, "TOTALT: %.2f" % totalBelop)

        # sum mvagrunnlag


        # standard betalingsvilkår
        if len(self.faktura['vilkaar']):
            self.canvas.setFont("Helvetica", 10)
            vilkar = self.canvas.beginText()
            vilkar.setTextOrigin(9*mm, 131*mm)
            vilkar.textLines(self.paragraf(self.faktura['vilkaar'].upper(), 35))
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
        self.canvas.drawString(170*mm, 93*mm, self.faktura['forfall'])

        # fakturainformasjon
        t = self.canvas.beginText()
        t.setTextOrigin(15*mm, 90*mm)
        t.textLines("Kundenr: %04i\nFakturanr: %04i\nFakturadato: %s" % \
            (self.kunde['nr'], self.faktura['nr'], self.faktura['utstedt']))
        self.canvas.drawText(t)

        # mottakerfelt
        kundeinfo = self.canvas.beginText()
        kundeinfo.setTextOrigin(15*mm, 58*mm)
        kundeinfo.textLines(split(self.kunde['adresse'], '\n'))
        self.canvas.drawText(kundeinfo)

        # avsenderfelt
        firmaadresse = self.canvas.beginText()
        firmaadresse.setTextOrigin(115*mm, 58*mm)
        firmaadresse.textLines(split("%(firmanavn)s\n%(kontaktperson)s\n%(adresse)s\n%(postnummer)04i %(poststed)s" % (self.firma), '\n'))
        self.canvas.drawText(firmaadresse)

        # KID
        if self.faktura['kid'] and self.sjekkKid(self.faktura['kid']):
            self.canvas.drawString(14*mm, 21*mm, str(self.faktura['kid']))

        # SUM
        kr = int(totalBelop)
        ore = int((totalBelop - kr) * 100)
        self.canvas.drawString(90*mm, 21*mm, str(kr))
        self.canvas.drawString(110*mm, 21*mm, "%02d" % ore)
        self.canvas.drawString(135*mm, 21*mm, str(self.firma['kontonummer']))

    def settSammen(self):
        "Setter sammen fakturaen. Ikke for eksternt bruk. Bruk .lag*()-metodene"
        self.canvas.showPage()
        self.canvas.save()
        return True

if __name__ == '__main__':
    #test
    filnavn = '/tmp/testfaktura.pdf'
    faktura = f60(filnavn, overskriv=True)
    faktura.settFakturainfo(03, 1145542709, 1146546709, u"Rå løk", u"Takk for handelen, kom gjerne igjen når du vil, eller ikke hvis du ikke vil.", kid='4466986711175280')
    faktura.settFirmainfo({'firmanavn':'Test Firma Ein',
                           'kontaktperson':'Rattatta Hansen',
                           'adresse':u'Surdalsøyra',
                           'postnummer':8999,
                           'poststed':u'Fløya',
                           'kontonummer':99999999999,
                           'organisasjonsnummer':876876,
                           'telefon':23233322,
                           'epost':'ratata@ta.no'})
    faktura.settKundeinfo(06, "Topert\nRopertgata 33\n9022 Nissedal")
    faktura.settOrdrelinje([ ["Leder", 1, 300, 25], ['Reportasje', 1, 3000, 25], ])
    if faktura.lagEpost():
        print "Kvittering laget i", filnavn
    else:
        print "Kvittering kunne ikke lagres i", filnavn

