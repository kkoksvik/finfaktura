#!/usr/bin/python -d
# -*-*- coding:utf8 -*-*-
###########################################################################
#    Copyright (C) 2005-2006 - Håvard Dahle og Håvard Sjøvoll
#    <havard@dahle.no>, <sjovoll@ntnu.no>
#
#    Lisens: GPL2
#
# $Id: fakturabibliotek.py,v 1.6 2006/09/16 22:58:36 havardda Exp $
###########################################################################

import types, os, sys, os.path
from string import join
from time import time, strftime, localtime
import sqlite

DATABASEVERSJON=2.6
DATABASESQL="faktura.sql" # TODO: hvordan finne riktig katalog?
DATABASENAVN="faktura.db"
#DATABASECONVERTERS={"pdf":pdfdataToType}

class FakturaFeil(Exception): pass
class KundeFeil(Exception): pass
class DBKorruptFeil(Exception): pass
class DBGammelFeil(Exception): pass
class DBNyFeil(Exception): pass
class FirmainfoFeil(Exception): pass
class SikkerhetskopiFeil(Exception): pass
class PDFFeil(Exception): pass

class FakturaBibliotek:
    def __init__(self, db, sjekkVersjon=True):
        self.db = db
        self.c  = db.cursor()
        self.__firmainfo = None
        self.oppsett = fakturaOppsett(db, versjonsjekk=sjekkVersjon)

    def versjon(self):
        v = self.oppsett.hentVersjon()
        if v is None: return 2.0 # før versjonsnummeret kom inn i db
        else: return v

    def hentKunde(self, kundeID):
        #assert(type(kundeID
        return fakturaKunde(self.db, kundeID)

    def hentKunder(self, inkluderSlettede=False):
        sql = "SELECT ID FROM %s" % fakturaKunde._tabellnavn
        if not inkluderSlettede: sql += " WHERE slettet IS NULL OR slettet = 0"
        self.c.execute(sql)
        return [fakturaKunde(self.db, z[0]) for z in self.c.fetchall()]

    def nyKunde(self):
        return fakturaKunde(self.db)

    def hentVarer(self, inkluderSlettede=False):
        sql = "SELECT ID FROM %s" % fakturaVare._tabellnavn
        if not inkluderSlettede: sql += " WHERE slettet IS NULL OR slettet = 0"
        self.c.execute(sql)
        return [fakturaVare(self.db, z[0]) for z in self.c.fetchall()]

    def nyVare(self):
        return fakturaVare(self.db)

    def hentVare(self, Id):
        return fakturaVare(self.db, Id)

    def nyOrdre(self, _kunde = None, _Id = None):
        return fakturaOrdre(self.db, kunde=_kunde, Id=_Id, firma = self.__firmainfo)

    def hentOrdrer(self):
        self.c.execute("SELECT ID FROM %s" % fakturaOrdre._tabellnavn)
        return [ fakturaOrdre(self.db, Id=z[0]) for z in self.c.fetchall() ]

    def firmainfo(self):
        if not self.__firmainfo:
            self.__firmainfo = fakturaFirmainfo(self.db)
        return self.__firmainfo

    def hentEgenskapVerdier(self, tabell, egenskap):
        self.c.execute("SELECT DISTINCT %s FROM %s" % (egenskap, tabell))
        return [str(x[0]) for x in self.c.fetchall() if x[0]]

    def lagSikkerhetskopi(self, ordre):
        return fakturaSikkerhetskopi(self.db, ordre)

    def hentSikkerhetskopier(self):
        self.c.execute("SELECT ID FROM %s" % fakturaSikkerhetskopi._tabellnavn)
        return [ fakturaSikkerhetskopi(self.db, Id = z[0]) for z in self.c.fetchall() ]

    def sjekkSikkerhetskopier(self, lagNyAutomatisk=False):
        sql = "SELECT Ordrehode.ID, Sikkerhetskopi.ID FROM Ordrehode LEFT OUTER JOIN Sikkerhetskopi ON Ordrehode.ID=Sikkerhetskopi.ordreID WHERE data IS NULL"
        self.c.execute(sql)
        ordrer = []
        for z in self.c.fetchall():
            debug("Ordre #%i har ingen gyldig sikkerhetskopi!" % z[0])
            o = fakturaOrdre(self.db, Id=z[0], firma=self.firmainfo())
            if lagNyAutomatisk: 
                # merk evt. gammel sikkerhetskopi som ugyldig
                if z[1]:
                    s = fakturaSikkerhetskopi(self.db, Id=z[1])
                    s.data = False
                try:
                    self.lagSikkerhetskopi(o)
                except FakturaFeil, e:
                    raise SikkerhetskopiFeil(u'Kunne ikke lage sikkerhetskopi for ordre #%s! Årsak:\n%s' % (z[0], e))
            else:
                ordrer.append(o)
        return ordrer
                
    def lagPDF(self, ordre, blankettType, _filnavn=None):
        from f60 import f60, REPORTLAB
        if not REPORTLAB: 
            raise PDFFeil(u'Modulen "reportlab" er ikke installert. Uten denne kan du ikke lage pdf-fakturaer.')
            
        pdf = f60(filnavn=_filnavn)
        pdf.settFakturainfo(ordre._id, ordre.ordredato, ordre.forfall, ordre.tekst)
        pdf.settFirmainfo(ordre.firma._egenskaper)
        try:
            pdf.settKundeinfo(ordre.kunde._id, ordre.kunde.postadresse())
        except KundeFeil, e:
            raise FakturaFeil(u"Kunne ikke lage PDF! %s" % e)
        pdf.settOrdrelinje(ordre.hentOrdrelinje)
        if blankettType.lower() == "epost":
            res = pdf.lagEpost()
        elif blankettType.lower() == "post":
            res = pdf.lagPost()
        elif blankettType.lower() == "kvittering":
            res = pdf.lagKvittering()
        else:
            raise FakturaFeil(u"Ugyldig blankett-type: %s" % blankettType)
        if not res: 
            raise FakturaFeil(u"Kunne ikke lage PDF! ('%s')" % spdf.filnavn)
 
        return pdf
    
    def skrivUt(self, filnavn):
        if not os.path.exists(filnavn):
            raise "Feil filnavn"
        ## XXX: TODO: Skrive ut for alle os
        os.system('kprinter "%s"' % filnavn)
        
    def sendEpost(self, ordre, pdf, tekst=None):
        import epost
        m = epost.smtp(ordre, pdf, tekst)
        #m = epost.gmail(ordre, pdf, tekst)
        return m.send()
        
class fakturaKomponent:
    _egenskaper = {}
    _tabellnavn = ""
    _IDnavn     = "ID"
    _sqlExists  = True 
    _egenskaperBlob = []

    def __init__(self, db, Id = None):
        self.db = db
        self.c  = self.db.cursor()
        self._egenskaperAldriCache = []

        if Id is None:
            Id = self.nyId()
        self._id = Id
        self._egenskaper = self.hentEgenskaperListe()
        self.hentEgenskaper()

    def __getattr__(self, egenskap):
        #debug("__getattr__: %s" % (egenskap))
        if not self._sqlExists: #tabellen finnes ikke i databasen
            return None
        if not self._egenskaper.has_key(egenskap):
            raise AttributeError(u"%s har ikke egenskapen %s" % (self.__class__, egenskap))
        if egenskap in self._egenskaperAldriCache:
            self.hentEgenskaper()
        #if type(self._egenskaper[egenskap]) in (types.StringType,):
            #return unicode(self._egenskaper[egenskap], 'utf8')
        #debug("__getattr__:2: %s" % type(self._egenskaper[egenskap]))
        return self._egenskaper[egenskap]

    def __setattr__(self, egenskap, verdi):
        #debug("__setattr__: %s  " % (egenskap))
        #debug("__setattr__: %s = %s " % (egenskap, verdi))
        #try:
            #import qt 
            #if type(verdi) == qt.QString: verdi = unicode(verdi)
        #except ImportError: pass
        if type(verdi) == types.BooleanType: verdi = int(verdi) # lagrer bool som int: 0 | 1
        if self._egenskaper.has_key(egenskap):
            self.oppdaterEgenskap(egenskap, verdi)
        else: self.__dict__[egenskap] = verdi

    def hentEgenskaperListe(self):
        self.c.execute("SELECT * FROM %s LIMIT 1" % self._tabellnavn)
        self._egenskaperListe = map(lambda z: z[0], self.c.description)
        r = {}
        for z in self._egenskaperListe:
            r.update({z:None})
#       debug("hentEgenskaperListe: %s = %s" % (self._id, r))
        return r

    def hentEgenskaper(self):
        if self._id is None:
            return False
        self.c.execute("SELECT * FROM %s WHERE %s=%s" % (self._tabellnavn, self._IDnavn, self._id))
        r = self.c.fetchone()
        if r is None: raise DBNyFeil(u'Det finnes ingen %s med ID %s' % (self._tabellnavn, self._id))
        for z in self._egenskaper.keys():
            try:verdi = r[self._egenskaperListe.index(z)]
            except TypeError: print self._tabellnavn, self._id, z, self._egenskaperListe.index(z),r
            
            #if not z in self._egenskaperBlob and type(verdi) == types.StringType:
                #try:
                    #verdi = verdi.decode("utf8")
                #except:
                    #verdi = verdi.decode("latin1")
                    #print self._tabellnavn, "feil enkdoing:", verdi[0:20]
                    #raise
            self._egenskaper.update({z:r[self._egenskaperListe.index(z)]})
            self._egenskaper[z] = verdi

    def oppdaterEgenskap(self, egenskap, verdi):
        if not egenskap in self._egenskaperBlob and type(verdi) in (types.UnicodeType,):
            verdi = verdi.encode('utf8')
        try:
            import qt 
            if type(verdi) == qt.QString: verdi = unicode(verdi)
        except ImportError: pass
        #self.c.execute("UPDATE %s SET %s=%%s WHERE %s=%s" % (self._tabellnavn, egenskap, self._IDnavn, self._id), verdi)
        _sql = "UPDATE %s SET %s=%%s WHERE %s=%s" % (self._tabellnavn, egenskap, self._IDnavn, self._id)
        #print _sql, type(verdi)
        self.c.execute(_sql, (verdi,))
        self.db.commit()
        self.hentEgenskaper()

    def nyId(self):
#       debug("nyId: -> %s <- %s" % (self._tabellnavn, self._IDnavn))
        self.c.execute("INSERT INTO %s (%s) VALUES (NULL)" % (self._tabellnavn, self._IDnavn))
        self.db.commit()
        return self.db.insert_id()

class fakturaKunde(fakturaKomponent):
    _tabellnavn = "Kunde"

    def __init__(self, db, Id = None):
        fakturaKomponent.__init__(self, db, Id)

    def __str__(self):
        return "%s, %s, kunde # %03i" % (self.navn, self.epost, self._id)

    def __repr__(self):
        return "kunde # %s, egenskaper: %s" % (self._id, self._egenskaper)

    def postadresse(self):
        #if not self.navn or not self.adresse or not self.poststed:
            #raise KundeFeil("Kundeinfo ikke korrekt utfylt")
        e = dict(self._egenskaper) # lager kopi
        if not e['postnummer'] and not str(e['postnummer']).isdigit(): e['postnummer'] = ''
        else: e['postnummer'] = str(e['postnummer']).zfill(4)
        try:
            return "%(navn)s \n"\
                    "v/ %(kontaktperson)s \n"\
                    "%(adresse)s \n"\
                    "%(postnummer)s %(poststed)s" % e #(self._egenskaper)
        except TypeError:
            raise KundeFeil(u"Kundeinfo ikke korrekt utfylt")

    def settSlettet(self, erSlettet=True):
        debug("sletter kunde %s: %s" % (self._id, str(erSlettet)))
        if erSlettet: self.slettet = time()
        else: self.slettet = False
        
    def finnOrdrer(self):
        u'Finner alle gyldige ordrer tilhørende denne kunden'
        #Finn alle id-ene først
        self.c.execute('SELECT ID FROM Ordrehode WHERE kundeID=%i AND kansellert=0 ORDER BY ordredato ASC' % self._id)
        return [fakturaOrdre(self.db, kunde=self, Id=i[0]) for i in self.c.fetchall()]
        

class fakturaVare(fakturaKomponent):
    _tabellnavn = "Vare"

    def __str__(self):
        return unicode("%s: %.2f kr (%s %% mva)" % (self.navn, self.pris, self.mva))

    def __repr__(self):
        return unicode("%s, vare # %s" % (self.navn, self._id))

    def settSlettet(self, erSlettet=True):
        debug("sletter vare? %s" % self._id)
        if erSlettet: self.slettet = time()
        else: self.slettet = False
        
    def finnKjopere(self):
        u"Finner hvem som har kjøpt denne varen, returnerer liste av fakturaKunde"
        sql='SELECT DISTINCT kundeID FROM Ordrehode INNER JOIN Ordrelinje ON Ordrehode.ID=Ordrelinje.ordrehodeID WHERE vareID=%i'
        self.c.execute(sql % self._id)
        return [fakturaKunde(self.db, Id=i[0]) for i in self.c.fetchall()]

    def finnTotalsalg(self):
        u'Finner det totale salgsbeløpet (eks mva) for denne varen'
        self.c.execute('SELECT SUM(kvantum*enhetspris) FROM Ordrelinje WHERE vareID=%i' % self._id)
        try:
            return self.c.fetchone()[0]
        except TypeError:
            return 0.0

    def finnAntallSalg(self):
        u'Finner det totale antallet salg denne varen har gjort'
        self.c.execute('SELECT COUNT(*) FROM Ordrelinje WHERE vareID=%i' % self._id)
        try:
            return self.c.fetchone()[0]
        except TypeError:
            return 0

    def finnSisteSalg(self):
        u'Finner det siste salg denne varen har var med i'
        self.c.execute('SELECT Ordrehode.ID FROM Ordrehode INNER JOIN Ordrelinje ON Ordrehode.ID=Ordrelinje.ordrehodeID WHERE vareID=%i ORDER BY ordredato DESC LIMIT 1' % self._id)
        try:
            return fakturaOrdre(self.db, Id=self.c.fetchone()[0])
        except TypeError:
            return None

class fakturaOrdre(fakturaKomponent):
    _tabellnavn = "Ordrehode"
    linje      = []

    def __init__(self, db, kunde = None, Id = None, firma = None):
        self.linje = []
        self.kunde = kunde
        self.firma = firma
        fakturaKomponent.__init__(self, db, Id)
        self._egenskaperAldriCache = ['kansellert', 'betalt']
        if Id is not None:
            self.finnVarer()
            self.kunde  = fakturaKunde(db, self.kundeID)

    def __str__(self):
        s = "ordre # %04i, utformet til %s den %s" % (self._id, self.kunde.navn, strftime("%Y-%m-%d %H:%M", localtime(self.ordredato)))
        if self.linje:
            s += "\n"
            for ordre in self.linje:
                s += " o #%i: %s \n" % (ordre._id, unicode(ordre))
        return unicode(s)

    def nyId(self):
        forfall = self.firma.forfall
        self.c.execute("INSERT INTO %s (ID, kundeID, ordredato, forfall) VALUES (NULL, %s, %s, %s)" %  \
          (self._tabellnavn, self.kunde._id, time(), time()+3600*24*forfall))
        self.db.commit()
        return self.db.insert_id()

    def leggTilVare(self, vare, kvantum, pris, mva):
        vare = fakturaOrdrelinje(self.db, self, vare, kvantum, pris, mva)
        self.linje.append(vare)

    def finnVarer(self):
        self.linje = []
        self.c.execute("SELECT ID FROM %s WHERE ordrehodeID=%s" % (fakturaOrdrelinje._tabellnavn, self._id))
        for linjeID in map(lambda x:x[0], self.c.fetchall()):
            o = fakturaOrdrelinje(self.db, self, Id=linjeID)
            self.linje.append(o)

    def hentOrdrelinje(self):
        self.finnVarer()
        return self.linje
            
    def finnPris(self):
        "regner ut fakturabeløpet uten mva"
        if not self.linje: return 0.0
        p = 0.0
        for vare in self.linje:
            p += vare.kvantum * vare.enhetspris
        return p

    def finnMva(self):
        "regner ut mva for fakturaen"
        if not self.linje: return 0.0
        mva = 0.0
        for vare in self.linje:
            mva += vare.kvantum * vare.enhetspris * vare.mva / 100
        return mva

    def settKansellert(self, kansellert=True):
        debug("Ordre #%s er kansellert: %s" % (self._id, str(kansellert)))
        if kansellert:
            self.kansellert = time()
        else:
            self.kansellert = False

    def betal(self, dato = False):
        debug("Betaler faktura #%s" % self._id)
        if not dato:
            dato = time()
        self.betalt = dato

    def lagFilnavn(self, katalog, fakturatype):
        n = "%s/faktura-%06d-%s-%s-%s.pdf" % (os.path.expanduser(katalog),
                                              self.ID,
                                              fakturatype,
                                              self.kunde.navn.replace(" ", "_"),
                                              strftime("%Y-%m-%d"))
        return n

    def forfalt(self):
        # forfalt() -> Bool. Er fakturaen forfalt (og ikke betalt)?
        return not self.betalt and time() > self.forfall

    def hentSikkerhetskopi(self):
        self.c.execute("SELECT ID FROM %s WHERE ordreID = %i" % (fakturaSikkerhetskopi._tabellnavn, self._id))
        return fakturaSikkerhetskopi(self.db, Id = self.c.fetchone()[0])


class fakturaOrdrelinje(fakturaKomponent):
    _tabellnavn = "Ordrelinje"

    def __init__(self, db, ordre, vare = None, kvantum = None, enhetspris = None, mva = None, Id = None):
        self.ordre = ordre
        self.vare = vare
        if Id is None:
            db.cursor().execute("INSERT INTO %s (ID, ordrehodeID, vareID, kvantum, enhetspris, mva) VALUES (NULL, %s, %s, %s, %s, %s)" % (self._tabellnavn, self.ordre._id, self.vare._id, kvantum, enhetspris, mva))
            db.commit()
            Id = db.insert_id()
        fakturaKomponent.__init__(self, db, Id)
        if Id is not None:
            self.vare = fakturaVare(db, self.vareID)

    def __str__(self):
        return "%s %s %s a kr %2.2f" % (self.kvantum, self.vare.enhet, self.vare.navn, self.enhetspris)

    def __repr__(self):
        return "%03d %s: %s %s a kr %2.2f (%s%% mva)" % (self.vare.ID, self.vare.navn, self.kvantum, self.vare.enhet, self.enhetspris, self.mva)

    def nyId(self):
        pass

    def detaljertBeskrivelse(self):
        return unicode("%03d %s: %s %s a kr %2.2f (%s%% mva)" % (self.vare.ID, self.vare.navn, self.kvantum, self.vare.enhet, self.enhetspris, self.mva))

class fakturaFirmainfo(fakturaKomponent):
    _tabellnavn = "Firma"
    _id         = 1
    _egenskaperAldriCache = []

    def __initgammel__(self, db):
        self._egenskaperBlob = ['logo',]
        fakturaKomponent.__init__(self, db, Id=self._id)
        if not self._egenskaper:
            self.lagFirma()
    
    def __init__(self, db):
        self.db = db
        self.c  = self.db.cursor()
        #self._egenskaperAldriCache = []

        self._egenskaper = self.hentEgenskaperListe()
        try:
            self.hentEgenskaper()
        except DBNyFeil:
            self.lagFirma()
            self.hentEgenskaper()
        #print self._egenskaper
        
    def __str__(self):
        return u"""
      == FIRMA: %(firmanavn)s ==
      Kontakt: %(kontaktperson)s
      Adresse: %(adresse)s, %(postnummer)04s %(poststed)s
      Konto  : %(kontonummer)s
      Org.nr : %(organisasjonsnummer)s
      """ % (self._egenskaper)

    #def nyId(self):
        #pass

    def lagFirma(self):
        debug("Lager firma")
        nyFirmanavn = "Fryktelig fint firma"
        nyMva       = 25 #prosent
        nyForfall   = 21 #dager
        self.c.execute("INSERT INTO %s (ID, firmanavn, mva, forfall) VALUES (%s, '%s', %s, %s)" % (self._tabellnavn, self._id, nyFirmanavn, nyMva, nyForfall))
        
        self.db.commit()
        #self._egenskaper = self.hentEgenskaperListe()
        #self.hentEgenskaper()

    def postadresse(self):
        return "%(firmanavn)s \n"\
               "v/%(kontaktperson)s \n"\
               "%(adresse)s \n"\
               "%(postnummer)04i %(poststed)s" % (self._egenskaper)

    def sjekkData(self):
        sjekk = ["firmanavn", "kontaktperson", "adresse", "postnummer", "poststed", "kontonummer", "organisasjonsnummer","epost"]
        mangler = [felt for felt in sjekk if not getattr(self, felt)]
        if mangler: raise FirmainfoFeil(u"Følgende felt er ikke fylt ut: %s" % join(mangler, ", "))

class fakturaOppsett(fakturaKomponent):
    _tabellnavn = "Oppsett"
    _id         = 1
    
    def __init__(self, db, versjonsjekk=True):
    
        from _sqlite import DatabaseError
        c = db.cursor()
        datastrukturer = [fakturaFirmainfo,
                          fakturaKunde,
                          fakturaVare,
                          fakturaOrdre,
                          fakturaOrdrelinje,
                          fakturaOppsett, 
                          fakturaSikkerhetskopi]
        mangler = []
        for obj in datastrukturer:
            try:
                c.execute("SELECT * FROM %s" % obj._tabellnavn)
            except DatabaseError,e:
                # db mangler eller er korrupt
                # for å finne ut om det er en gammel versjon
                # sparer vi på tabellene som mangler og sammenligner
                # når vi er ferdige
                mangler.append( obj )
        # hvis alle strukturene mangler, er det en tom (ny) fil
        if datastrukturer == mangler:
            raise DBNyFeil(u"Databasen er ikke bygget opp")
        elif mangler: #noen av strukturene mangler, dette er en gammel fil
            if versjonsjekk:
                raise DBGammelFeil(u"Databasen er gammel eller korrupt, følgende felt mangler: %s" %  ",".join([o._tabellnavn for o in mangler]))
        
        try:
            fakturaKomponent.__init__(self, db, Id=self._id)
        except DatabaseError:
            # tabellen finnes ikke
            self._sqlExists = False
            if versjonsjekk: 
                raise DBGammelFeil(u"Databasen mangler tabellen '%s'" % self._tabellnavn)
    
        if not versjonsjekk: return

        debug("sjekker versjon")
        debug("arkivet er %s, siste er %s" % (self.databaseversjon, DATABASEVERSJON))
        if self.databaseversjon != DATABASEVERSJON:
            raise DBGammelFeil(u"Databasen er versjon %s og må oppgraderes til %s" % (self.databaseversjon, DATABASEVERSJON))
    
    def nyId(self):
        pass

    
    def migrerDatabase(self, nydb, sqlFil):
        from oppgradering import oppgradering
        db = lagDatabase(nydb, sqlFil)
        # hva nå?
        
    def hentVersjon(self):
        if not self._sqlExists: #arbeider med for gammel versjon til at tabellen finnes
            return None
        try:
            return self.databaseversjon
        except AttributeError:
            return None #gammel databaselayout

class fakturaSikkerhetskopi(fakturaKomponent):
    _tabellnavn = "Sikkerhetskopi"

    def __init__(self, db, ordre = None, Id = None):
        self.dato  = int(time())
        if ordre is not None:
            self.ordre = ordre
            db.cursor().execute("INSERT INTO %s (ID, ordreID, dato) VALUES (NULL, %s, %s)" % (self._tabellnavn, self.ordre._id, self.dato))
            db.commit()
            Id = db.insert_id()
            fakturaKomponent.__init__(self, db, Id)
            from f60 import f60
            spdf = f60(filnavn=None)
            spdf.settFakturainfo(ordre._id, ordre.ordredato, ordre.forfall, ordre.tekst)
            spdf.settFirmainfo(ordre.firma._egenskaper)
            try:
                spdf.settKundeinfo(ordre.kunde._id, ordre.kunde.postadresse())
            except KundeFeil, e:
                raise FakturaFeil(u"Kunne ikke lage PDF! %s" % e)

            spdf.settOrdrelinje(ordre.hentOrdrelinje)
            spdf.lagBakgrunn()
            spdf.lagKopimerke()
            spdf.fyll()
    
            res = spdf.settSammen()
            if not res: 
                raise FakturaFeil(u"Kunne ikke lage PDF! ('%s')" % spdf.filnavn)
                    
            self.data = pdfType(spdf.data())
            
        elif Id is not None:
            fakturaKomponent.__init__(self, db, Id)
        
    def ordre(self):
        return fakturaOrdre(self.db, Id=self.ordreID)

    def hentEgenskaper(self):
        if self._id is None:
            return False
        self.c.execute("SELECT ID,ordreID,dato,data FROM %s WHERE %s=%s" % (self._tabellnavn, self._IDnavn, self._id))
        r = self.c.fetchone()
        self._egenskaper['ordreID'] = r[1]
        self._egenskaper['dato']    = r[2]
        self._egenskaper['data']    = pdfType(r[3])

    def lagFil(self):
        from tempfile import mkstemp
        f,filnavn = mkstemp('.pdf', 'sikkerhetsfaktura')
        fil = file(filnavn, "wb")
        fil.write(str(self.data))
        fil.close()
        return filnavn

    def skrivUt(self):
        import os
        os.system('kprinter "%s"' % self.lagFil()) 

class pdfType:
    'Egen type for å holde pdf (f.eks. sikkerhetskopi)'
    def __init__(self, data):
        self.data = data
    
    def _quote(self): 
        'Returnerer streng som kan puttes rett inn i sqlite. Kalles internt av pysqlite'
        if not self.data: return "''"
        import sqlite
        return "'%s'" % sqlite.encode(self.data)
    
    def __str__(self):
        return self.data

def debug(s):
    print "[FAKTURA]: %s" % s

def lagDatabase(database, dbsql=DATABASESQL):
    import sqlite
    logg = open("faktura.sqlite.lag.log", "a+")
    print "datbase:",database
    db = sqlite.connect(db=database, encoding="utf-8", command_logfile=logg)
    c = db.cursor()
    c.execute(file(dbsql).read())
    db.commit()
    return db

def byggDatabase(db):
    c = db.cursor()
    c.execute(file(DATABASESQL).read())
    db.commit()
    return db

def finnDatabasenavn(databasenavn="faktura.db"):
    fdir = os.getenv('FAKTURADIR')
    if not fdir:
        #sjekk for windows
        if sys.platform.startswith('win'):
            pdir = os.getenv('USERPROFILE')
            fdir = os.path.join(pdir, "finfaktura")
        else:
            #sjekk for mac
            #sjekk for linux
            pdir = os.getenv('HOME')
            fdir = os.path.join(pdir, ".finfaktura")
    if not os.path.exists(fdir):
        os.mkdir(fdir, 0700)
    return os.path.join(fdir, databasenavn)

def finnDatabaseSQL():
    top = os.path.realpath(__file__)

def kobleTilDatabase(dbnavn=None, loggfil=None):
    if dbnavn is None:
        dbnavn = finnDatabasenavn()
    enc = "utf-8"
    db = sqlite.connect(db=dbnavn, encoding=enc, command_logfile=loggfil)
    return db

if __name__ == "__main__":
    #test biblioteket
    import sys
    test = sys.argv[1:]
    if "hjelp" in test:
        from os import execl
        execl("/bin/grep", "grep", "in test:", "fakturabibliotek.py")
    import sqlite
    from pprint import pprint
    logg = open("faktura.sqlite.log", "a+")
    #enc = ("utf-8", "replace")
    cx = sqlite.connect(finnDatabasenavn(), encoding='utf-8', command_logfile=logg)
    if "kunde" in test:
        kunde = fakturaKunde(cx)
        kunde.navn = "Håvard Dahle"
        kunde.epost = "havard@dahle.no"
        print "kunde:", kunde
    if "hentKunder" in test:
        b = FakturaBibliotek(cx)
        pprint(b.hentKunder())
    if "vare" in test:
        v = fakturaVare(cx)
        v.navn = "2-sider Linuxmagasinet"
        v.detaljer = "Tekst som går over to sider"
        v.enhet = "stk"
        v.pris = "2500"
        print "vare:", v
    if "nyfaktura" in test:
        _kunde = fakturaKunde(cx, 3)
        _firma = fakturaFirmainfo(cx)
        f = fakturaOrdre(cx, kunde=_kunde, firma=_firma)
        f.tekst = u"råtøff vask"
        v = fakturaVare(cx, 2)
        f.leggTilVare(v, 4, 2500, 12)
        v2 = fakturaVare(cx, 3)
        f.leggTilVare(v2, 1, 2000, 24)
        print "faktura:", f
        b = FakturaBibliotek(cx)
        pdf = b.lagPDF(f, "epost")
        print "pdf:",pdf.filnavn
    if "pdf" in test:
        _firma = fakturaFirmainfo(cx)
        f = fakturaOrdre(cx, Id=22, firma=_firma)
        b = FakturaBibliotek(cx)
        pdf = b.lagPDF(f, "epost")
        print "pdf:",pdf.filnavn
        
    if "hentordrer" in test:
        b = FakturaBibliotek(cx)
        for z in b.hentOrdrer():
            print z
    if "firma" in test:
        f = fakturaFirmainfo(cx)
        print f.__str__()
        print f.firmanavn
    
    if "oppdater" in test:
        f = fakturaFirmainfo(cx)
        f.firmanavn=u'Hålåxx'
        print f.firmanavn
    
    if "firmalogo" in test:
        f = fakturaFirmainfo(cx)
        print "firmalogo:",type(f.logo)
        #out = file("/tmp/firmalogo.gif", "w")
        #out.write(f.logo)
        #out.close()

    if "database" in test:
        b = FakturaBibliotek(cx)
    if "lagdatabase" in test:
        dbnavn = finnDatabasenavn()
        print "lager db:", dbnavn
        db = lagDatabase(dbnavn)
        b = FakturaBibliotek(db)
        print b
    if "hentsikkerhetskopier" in test:
        b = FakturaBibliotek(cx)
        for kopi in b.hentSikkerhetskopier():
            if kopi.data is None:
                print "ordre# %s har ingen sikkerhetskopi!" % kopi.ordreID
                continue
            fil = "/tmp/sikk.%s.%s.pdf" % (kopi.dato, kopi.ordreID)
            f = file(fil, "w")
            f.write(str(kopi.data))
            f.close()
            print "sikkerhetskopi#%i av faktura # %s dumpet til %s" % (kopi._id, kopi.ordreID, fil)
    if "epost" in test:
        _firma = fakturaFirmainfo(cx)
        f = fakturaOrdre(cx, Id=1, firma=_firma)
        b = FakturaBibliotek(cx)
        pdf = b.lagPDF(f, "epost")
        print "pdf:",pdf.filnavn
        import epost
        print "tester mime"
        m = epost.test(f, pdf.filnavn)
        m.send()
        print "tester sendmail"
        sm = epost.sendmail(f, pdf.filnavn)
        sm.send()
        print "tester smtp"
        mp = epost.smtp(f, pdf.filnavn)
        #mp.send()
        print "tester gmail"
        gm = epost.gmail(f, pdf.filnavn)
        #gm.send('a','b')
        

    cx.close()
