#!/usr/bin/python -d
# -*- coding:utf8 -*-
###########################################################################
#    Copyright (C) 2006 - Håvard Dahle
#    <havard@dahle.no>
#
#    Lisens: GPL2
#
# $Id$
###########################################################################

# endringer er en linjeskiftseparert streng med følgende struktur:
# ver(float):tabellnavn[+|-|=nyttTabellNavn]:feltnavn<+|-|=nyttFeltNavn>
# for feltnavn gjelder følgende postulat:
#   +              :   feltet ble introdusert ved denne versjonen
#   -              :   feltet ble fjernet ved denne versjonen
#   =nyttFeltNavn  :   feltet ble gitt nytt navn ved denne versjonen
#
#   det samme gjelder for tabellnavn, med følgende spesialtilfelle:
#     dersom feltnavnet er None, blir det oversett (dette er bare fornuftig 
#     om tabellen har blitt fjernet eller gitt nytt navn

ENDRINGER ="""

1.6:Firma:orgnr=organisasjonsnummer
1.6:Kunde:kontakt=kontaktperson
1.6:Kunde:postnr=postnummer
1.6:Kunde:sted=poststed

1.7:Firma:mobil+
1.7:Firma:telefaks+
1.7:Firma:vilkar+

1.9:Database=Oppsett:None

2.0:Oppsett:ID+
2.0:Oppsett:fakturakatalog+
2.0:Oppsett:databaseversjon+

2.1:Ordrehode:mva-
2.1:Ordrelinje:mva+

2.1:Sikkerhetskopi:ID+
2.1:Sikkerhetskopi:ordreID+
2.1:Sikkerhetskopi:dato+
2.1:Sikkerhetskopi:data+

2.2:Postnummer:postnummer+
2.2:Postnummer:poststed+

2.6:Historikk+
2.6:Historikk:ordreid+
2.6:Historikk:dato+
2.6:Historikk:handlinid+
2.6:Historikk:suksess+
2.6:Historikk:forklaring+

2.6:Handling+
2.6:Handling:Id+
2.6:Handling:navn+
2.6:Handling:tekst+

2.7:Epost+
2.7:Epost:Id+
2.7:Epost:smtp_from+
2.7:Epost:transport+
2.7:Epost:gmailuser+
2.7:Epost:gmailpass+
2.7:Epost:smtpserver+
2.7:Epost:smtpport+
2.7:Epost:smtptls+
2.7:Epost:smtpauth+
2.7:Epost:smtpuser+
2.7:Epost:smtppass+
2.7:Epost:sendmailpath+


"""


import fakturabibliotek 
import sqlite
import types
from string import join

class OppgraderingsFeil(Exception): pass

class oppgrader:
    "For oppgradering mellom databaseversjoner"
    endringskart = {}
    
    def __init__(self):
        self.lastEndringer(ENDRINGER)
    
    def lastNyDatabase(self, database):
        self.nydb = database
        self.nydbc = database.cursor()
        try:
            self.nybib = fakturabibliotek.FakturaBibliotek(database, sjekkVersjon=True)
        except fakturabibliotek.DBNyFeil:  #tom fil, sql er ikke lastet
            self.nydb = fakturabibliotek.byggDatabase(self.nydb) #last sql
            print "lager db"
            self.nybib = fakturabibliotek.FakturaBibliotek(self.nydb, sjekkVersjon=False)
        #except DBGammelFeil:
    
    def lastGammelDatabase(self, database):
        self.gmldb = database
        self.gmldbc = database.cursor()
        self.gmlbib = fakturabibliotek.FakturaBibliotek(database, sjekkVersjon=False)
        
    def _oppgrader(self, objekt):
        print "oppgraderer %s #%s fra versjon %s til versjon %s" % (objekt._tabellnavn, objekt._id, self.gmlbib.versjon(), self.nybib.versjon())
        # først laster vi alle egenskapene til objektet inn i en ny dict
        # så går vi gjennom alle endringene og gjør endringene på den nye dict-en
        # returnerer den nye dict.
        if not objekt._egenskaper:
            # tomt objekt
            return
        egenskaper = dict(objekt._egenskaper)
        #print egenskaper
        if self.gmlbib.versjon() < 2.2:
            # gamle versjoner brukte ikke utf8
            egenskaper = self._unicode(egenskaper)
        for endringer in self.endringsmegler(objekt._tabellnavn):
            for felt in endringer.keys():
                if endringer[felt] == True: #lagt til
                    if not egenskaper.has_key(felt):
                        egenskaper[felt] = 0
                elif endringer[felt] == False: #fjernet
                    print "fjerner felt:",felt
                    egenskaper.pop(felt)
                else: #navnebytte
                    print "endrer navn på felt %s til %s" % (felt, endringer[felt])
                    egenskaper[endringer[felt]] = egenskaper[felt]
                    egenskaper.pop(felt)
            
        k = objekt
        sql = "INSERT INTO %s (%s) VALUES (%s)" % (k._tabellnavn, join(egenskaper.keys(), ","), join(["%s" for z in egenskaper.values()], ","))
        self.nydbc.execute(sql, egenskaper.values())
        self.nydb.commit()
    
    def _unicode(self, d):
        if self.gmlbib.versjon() < 2.2: fra = 'latin1'
        else: fra = 'utf8'
        for z in d.keys():
            if type(d[z]) in (types.StringType,):
                d[z] = unicode(d[z], fra)
        return d
    
    def endringsmegler(self, tabell):
        gmlver = self.gmlbib.versjon()
        nyver  = self.nybib.versjon()
        deltaer = [kartver for kartver in self.endringskart.keys() if kartver > gmlver and kartver <= nyver]
        if not deltaer: return
        deltaer.sort()
        for ver in deltaer:
            endringer = self.endringskart[ver]
            if not endringer.has_key(tabell): continue
            tabellendringer = endringer[tabell]
            yield tabellendringer
        
    def lastEndringer(self, endringer):
        for linje in endringer.split("\n"):
            if len(linje.strip()) == 0: continue #tom linje
            if linje.strip()[0] == '#': continue #utkommentert
            ver,tabell,felt = linje.strip().split(":")
            self.endre(float(ver),tabell,felt)
        from pprint import pprint
        pprint(self.endringskart)
    
    def endre(self,ver,tabell,felt):
        k = self.endringskart
        if not k.has_key(ver): k[ver] = {}
        v = k[ver]
        if not v.has_key(tabell): v[tabell] = {}
        t = v[tabell]
        #print felt.find("+")
        if tabell.find("=") != -1: #navnebytte
            t,tn = tabell.split("=")
            v[t] = tn
        if felt.find("+") != -1: t[felt[:-1]] = True #lagt til
        elif felt.find("-") != -1: t[felt[:-1]] = False # fjernet
        elif felt.find("=") != -1: #navnebytte
            f,n = felt.split("=")
            t[f] = n
        else: 
            if not felt == "None":
                raise OppgraderingsFeil("Ugyldig felt: %s" % felt)
        
        
    def oppgrader(self):
        nyversjon = self.nybib.versjon() #sparer på versjonsnummeret
        self._oppgrader(self.gmlbib.firmainfo())
        self._oppgrader(self.gmlbib.oppsett)
        try:
            for kopi in self.gmlbib.hentSikkerhetskopier():
                self._oppgrader(kopi)
        except sqlite.DatabaseError,e:
            if str(e).upper().startswith('NO SUCH TABLE'): pass #for gammel versjon
            else: raise
        for kunde in self.gmlbib.hentKunder(inkluderSlettede=True):
            self._oppgrader(kunde)
        for vare in self.gmlbib.hentVarer(inkluderSlettede=True):
            self._oppgrader(vare)
        for ordre in self.gmlbib.hentOrdrer():
            self._oppgrader(ordre)
            for linje in ordre.hentOrdrelinje():
                self._oppgrader(linje)
        #for postnr in self.gmlbib.hentPostnummer():
            #self._oppgrader(postnr)
        
        self.nybib.oppsett.databaseversjon = nyversjon # skriver tilbake versjonsnummeret, det kan ha blitt overskrevet
        
        # databaseintegritet:
        print "kontrollerer den nye databasen"
        self.nybib.sjekkSikkerhetskopier(lagNyAutomatisk=True)


    def oppgraderSamme(self, dbSti):
        #flytt gammel database 
        import os, time
        katalog, database = os.path.split(dbSti)
        dbBackupNavn = "%s-%s~" % (database, int(time.time()))
        dbBackup = os.path.join(katalog, dbBackupNavn)
        os.rename(dbSti, dbBackup)
        
        #kjør oppgradering
        from fakturabibliotek import kobleTilDatabase
        ny = kobleTilDatabase(dbSti)
        gml = kobleTilDatabase(dbBackup)
        self.lastNyDatabase(ny)
        self.lastGammelDatabase(gml)
        self.oppgrader()
        return True
        
        

if __name__ == '__main__':
    import sqlite
    from pprint import pprint
    loggNy = open("faktura.nydb.log", "a+")
    loggGml = open("faktura.gmldb.log", "a+")
    enc = "utf-8"
    ny = sqlite.connect(db="faktura.nydb", encoding=enc, command_logfile=loggNy)
    #gml = sqlite.connect(db="faktura.juksedb", encoding=enc, command_logfile=loggGml)
    gml = sqlite.connect(db="faktura.gmldb", encoding=enc, command_logfile=loggGml)
    opp = oppgrader(endringer)
    opp.lastNyDatabase(ny)
    opp.lastGammelDatabase(gml)
    opp.oppgrader()