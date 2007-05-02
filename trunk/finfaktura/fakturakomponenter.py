#!/usr/bin/python -d
# -*-*- coding:utf8 -*-*-
###########################################################################
#    Copyright (C) 2005-2007 - Håvard Dahle 
#    <havard@lurtgjort.no>
#
#    Lisens: GPL2
#
# $Id$
###########################################################################

import sqlite3 as sqlite
import types, time

from ekstra import debug
from fakturafeil import *

class fakturaKomponent:
    _egenskaper = {}
    _tabellnavn = ""
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
        #debug("__getattr__:2: %s" % type(self._egenskaper[egenskap]))
        return self._egenskaper[egenskap]

    def __setattr__(self, egenskap, verdi):
        #debug("__setattr__: %s  " % (egenskap))
        #debug("__setattr__: %s = %s " % (egenskap, verdi))
        if type(verdi) == types.BooleanType: verdi = int(verdi) # lagrer bool som int: 0 | 1
        if self._egenskaper.has_key(egenskap): # denne egenskapen skal lagres i databasen
            self.oppdaterEgenskap(egenskap, verdi) # oppdater databasen
        self.__dict__[egenskap] = verdi # oppdater lokalt for objektet

    def hentEgenskaperListe(self):
        try:
            self.c.execute("SELECT * FROM %s LIMIT 1" % self._tabellnavn)
        except sqlite.OperationalError:
            #pysqlite2 klager på blobs
            #pass
            raise
        self._egenskaperListe = map(lambda z: z[0], self.c.description)
        r = {}
        for z in self._egenskaperListe:
            r.update({z:None})
#       debug("hentEgenskaperListe: %s = %s" % (self._id, r))
        return r

    def hentEgenskaper(self):
        if self._id is None:
            return False
        #debug("SELECT * FROM %s WHERE ID=?" % self._tabellnavn, (self._id,))
        self.c.execute("SELECT * FROM %s WHERE ID=?" % self._tabellnavn, (self._id,))
        r = self.c.fetchone()
        if r is None: raise DBTomFeil(u'Det finnes ingen %s med ID %s' % (self._tabellnavn, self._id))
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
        try:
            import qt 
            if type(verdi) == qt.QString: verdi = unicode(verdi)
        except ImportError: pass
        _sql = "UPDATE %s SET %s=? WHERE ID=?" % (self._tabellnavn, egenskap)
        #debug(_sql, (verdi, self._id))
        self.c.execute(_sql, (verdi, self._id))
        self.db.commit()
        

    def nyId(self):
#       debug("nyId: -> %s <- %s" % (self._tabellnavn, self._IDnavn))
        self.c.execute("INSERT INTO %s (ID) VALUES (NULL)" % self._tabellnavn)
        self.db.commit()
        return self.c.lastrowid

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

    def epostadresse(self):
        "Gir en korrekt epostadresse"
        ### XXX: TODO: quote riktig
        return '"%s" <%s>' % (self.navn, self.epost)

    def settSlettet(self, erSlettet=True):
        debug("sletter kunde %s: %s" % (self._id, str(erSlettet)))
        if erSlettet: self.slettet = time.time()
        else: self.slettet = False
        
    def finnOrdrer(self):
        u'Finner alle gyldige ordrer tilhørende denne kunden'
        #Finn alle id-ene først
        self.c.execute('SELECT ID FROM %s WHERE kundeID=? AND kansellert=0 ORDER BY ordredato ASC' % fakturaOrdre._tabellnavn, (self._id,))
        return [fakturaOrdre(self.db, kunde=self, Id=i[0]) for i in self.c.fetchall()]
        

class fakturaVare(fakturaKomponent):
    _tabellnavn = "Vare"

    def __str__(self):
        return unicode("%s: %.2f kr (%s %% mva)" % (self.navn, self.pris, self.mva))

    def __repr__(self):
        return unicode("%s, vare # %s" % (self.navn, self._id))

    def settSlettet(self, erSlettet=True):
        debug("sletter vare? %s" % self._id)
        if erSlettet: self.slettet = time.time()
        else: self.slettet = False
        
    def finnKjopere(self):
        u"Finner hvem som har kjøpt denne varen, returnerer liste av fakturaKunde"
        sql='SELECT DISTINCT kundeID FROM Ordrehode INNER JOIN Ordrelinje ON Ordrehode.ID=Ordrelinje.ordrehodeID WHERE kansellert=0 AND vareID=?'
        self.c.execute(sql, (self._id,))
        return [fakturaKunde(self.db, Id=i[0]) for i in self.c.fetchall()]

    def finnTotalsalg(self):
        u'Finner det totale salgsbeløpet (eks mva) for denne varen'
        self.c.execute('SELECT SUM(kvantum*enhetspris) FROM Ordrelinje INNER JOIN Ordrehode ON Ordrelinje.ordrehodeID=Ordrehode.ID WHERE kansellert=0 AND vareID=?', (self._id,))
        try:
            return self.c.fetchone()[0]
        except TypeError:
            return 0.0

    def finnAntallSalg(self):
        u'Finner det totale antallet salg denne varen har gjort'
        self.c.execute('SELECT COUNT(*) FROM Ordrelinje INNER JOIN Ordrehode ON Ordrelinje.ordrehodeID=Ordrehode.ID WHERE kansellert=0 AND vareID=?', (self._id,))
        try:
            return self.c.fetchone()[0]
        except TypeError:
            return 0

    def finnSisteSalg(self):
        u'Finner det siste salg denne varen har var med i'
        self.c.execute('SELECT Ordrehode.ID FROM Ordrehode INNER JOIN Ordrelinje ON Ordrehode.ID=Ordrelinje.ordrehodeID WHERE kansellert=0 AND vareID=? ORDER BY ordredato DESC LIMIT 1', (self._id,))
        try:
            return fakturaOrdre(self.db, Id=self.c.fetchone()[0])
        except TypeError:
            return None

class fakturaOrdre(fakturaKomponent):
    _tabellnavn = "Ordrehode"
    linje      = []

    def __init__(self, db, kunde = None, Id = None, firma = None, dato = None):
        self.linje = []
        if dato is not None:
            self.ordredato = dato
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
        self.c.execute("INSERT INTO %s (ID, kundeID, ordredato, forfall) VALUES (NULL, ?, ?, ?)" % self._tabellnavn, (self.kunde._id, self.ordredato, self.ordredato+3600*24*forfall,))
        self.db.commit()
        return self.c.lastrowid

    def leggTilVare(self, vare, kvantum, pris, mva):
        vare = fakturaOrdrelinje(self.db, self, vare, kvantum, pris, mva)
        self.linje.append(vare)

    def finnVarer(self):
        self.linje = []
        self.c.execute("SELECT ID FROM %s WHERE ordrehodeID=?" % fakturaOrdrelinje._tabellnavn, (self._id,))
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
            self.kansellert = time.time()
        else:
            self.kansellert = False

    def betal(self, dato = False):
        debug("Betaler faktura #%s" % self._id)
        if not dato:
            dato = time.time()
        self.betalt = dato

    def fjernBetalt(self):
        self.betalt = None

    def lagFilnavn(self, katalog, fakturatype):
        n = "%s/faktura-%06d-%s-%s-%s.pdf" % (os.path.expanduser(katalog),
                                              self.ID,
                                              fakturatype,
                                              self.kunde.navn.replace(" ", "_"),
                                              strftime("%Y-%m-%d"))
        return n

    def forfalt(self):
        # forfalt() -> Bool. Er fakturaen forfalt (og ikke betalt)?
        return not self.betalt and time.time() > self.forfall

    def hentSikkerhetskopi(self):
        self.c.execute("SELECT ID FROM %s WHERE ordreID=?" % fakturaSikkerhetskopi._tabellnavn, (self._id,))
        return fakturaSikkerhetskopi(self.db, Id = self.c.fetchone()[0])


class fakturaOrdrelinje(fakturaKomponent):
    _tabellnavn = "Ordrelinje"

    def __init__(self, db, ordre, vare = None, kvantum = None, enhetspris = None, mva = None, Id = None):
        self.ordre = ordre
        self.vare = vare
        if Id is None:
            c = db.cursor()
            c.execute("INSERT INTO %s (ID, ordrehodeID, vareID, kvantum, enhetspris, mva) VALUES (NULL, ?, ?, ?, ?, ?)" % self._tabellnavn, (self.ordre._id, self.vare._id, kvantum, enhetspris, mva))
            db.commit()
            Id = c.lastrowid
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
        try:
            fakturaKomponent.__init__(self, db, Id=self._id)
        except DBTomFeil:
            self.lagFirma()
            fakturaKomponent.__init__(self, db, Id=self._id)
    
    def __init__(self, db):
        self.db = db
        self.c  = self.db.cursor()
        #self._egenskaperAldriCache = []

        self._egenskaper = self.hentEgenskaperListe()
        try:
            self.hentEgenskaper()
        except DBTomFeil:
            self.lagFirma()
            self._egenskaper = self.hentEgenskaperListe()
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
        self.c.execute("INSERT INTO %s (ID, firmanavn, mva, forfall) VALUES (?,?,?,?)" % self._tabellnavn, (self._id, nyFirmanavn, nyMva, nyForfall))
        
        self.db.commit()

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
    
    def __init__(self, db, versjonsjekk=True, apiversjon=None):
    
        self.apiversjon = apiversjon
        c = db.cursor()
        datastrukturer = [fakturaFirmainfo,
                          fakturaKunde,
                          fakturaVare,
                          fakturaOrdre,
                          fakturaOrdrelinje,
                          fakturaOppsett, 
                          fakturaSikkerhetskopi,
                          fakturaEpost]
        mangler = []
        for obj in datastrukturer:
            try:
                c.execute("SELECT * FROM %s LIMIT 1" % obj._tabellnavn)
            except sqlite.DatabaseError:
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
        except DBTomFeil:
            # finner ikke oppsett. Ny, tom database
            import os
            sql = "INSERT INTO %s (ID, databaseversjon, fakturakatalog) VALUES (?,?,?)" % self._tabellnavn
                
            c.execute(sql, (self._id, self.apiversjon, os.getenv('HOME'),))
            db.commit()
            fakturaKomponent.__init__(self, db, Id=self._id)
        except sqlite.DatabaseError:
            # tabellen finnes ikke
            self._sqlExists = False
            if versjonsjekk: 
                raise DBGammelFeil(u"Databasen mangler tabellen '%s'" % self._tabellnavn)
    
        if not versjonsjekk: return

        debug("sjekker versjon")
        debug("arkivet er %s, siste er %s" % (self.databaseversjon, self.apiversjon))
        if self.databaseversjon != self.apiversjon:
            raise DBGammelFeil(u"Databasen er versjon %s og må oppgraderes til %s" % (self.databaseversjon, self.apiversjon))
    
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
        self.dato  = int(time.time())
        if ordre is not None:
            self.ordre = ordre
            c = db.cursor()
            c.execute("INSERT INTO %s (ID, ordreID, dato) VALUES (NULL, ?, ?)" % self._tabellnavn, (self.ordre._id, self.dato))
            db.commit()
            Id = c.lastrowid
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
        sql = "SELECT ID, ordreID, dato, CAST(data as blob) FROM %s WHERE ID=?" % self._tabellnavn
        self.c.execute(sql, (self._id,))
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

    def vis(self):
        import os
        os.system('kpdf %s' % self.lagFil())


class fakturaEpost(fakturaKomponent):
    _tabellnavn = "Epost"
    _id = 1
    
    def __init__(self, db):
        self.db = db
        try: 
            fakturaKomponent.__init__(self, db, Id=self._id)
        except DBTomFeil:
            #ikke brukt før
            self.c.execute("INSERT INTO Epost (ID) VALUES (1)")
            self.db.commit()
            fakturaKomponent.__init__(self, db, Id=self._id)
        
    def nyId(self):
        pass

