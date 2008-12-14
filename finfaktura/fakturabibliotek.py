#!/usr/bin/python -d
# -*-*- coding:utf8 -*-*-
###########################################################################
#    Copyright (C) 2005-2008- Håvard Gulldahl og Håvard Sjøvoll
#    <havard@lurtgjort.no>, <sjovoll@ntnu.no>
#
#    Lisens: GPL2
#
# $Id$
###########################################################################

import types, os, sys, os.path, shutil
from string import join
from time import time, strftime, localtime
import logging, subprocess
try:
    import sqlite3 as sqlite # python2.5 har sqlite3 innebygget
except ImportError:
    from pysqlite2 import dbapi2 as sqlite # prøv bruker/system-installert modul

import historikk
from fakturakomponenter import fakturaOppsett, fakturaEpost, fakturaFirmainfo, \
        fakturaOrdre, fakturaVare, fakturaKunde, fakturaSikkerhetskopi
from fakturafeil import *

PRODUKSJONSVERSJON=False # Sett denne til True for å skjule funksjonalitet som ikke er ferdigstilt
DATABASEVERSJON=3.1
DATABASENAVN="faktura.db"
#DATABASECONVERTERS={"pdf":pdfdataToType}


class FakturaBibliotek:

    produksjonsversjon = False # dersom false er vi i utvikling, ellers produksjon

    def __init__(self, db, sjekkVersjon=True):
        self.db = db
        self.c  = db.cursor()
        self.__firmainfo = None
        self.oppsett = fakturaOppsett(db, versjonsjekk=sjekkVersjon, apiversjon=DATABASEVERSJON)
        try:
            self.epostoppsett = fakturaEpost(db)
        except sqlite.DatabaseError,e:
            if "no such table" in str(e).lower(): self.epostoppsett = None ## for gammel versjon
            else: raise

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

    def hentVarer(self, inkluderSlettede=False, sorterEtterKunde=None):
        sql = "SELECT ID FROM %s" % fakturaVare._tabellnavn
        if not inkluderSlettede: sql += " WHERE slettet IS NULL OR slettet = 0"
        if sorterEtterKunde is not None:
            sql += " ORDER BY "
        self.c.execute(sql)
        return [fakturaVare(self.db, z[0]) for z in self.c.fetchall()]

    def nyVare(self):
        return fakturaVare(self.db)

    def hentVare(self, Id):
        return fakturaVare(self.db, Id)

    def finnVareEllerLagNy(self, navn, pris, mva, enhet):
        sql = "SELECT ID FROM %s" % fakturaVare._tabellnavn
        sql += " WHERE navn=? AND pris=? AND mva=?"
        #print sql, navn, pris, mva
        self.c.execute(sql, (navn.strip(), pris, mva,))
        try:
            return fakturaVare(self.db, self.c.fetchone()[0])
        except TypeError:
            # varen finnes ikke, lag ny og returner
            vare = self.nyVare()
            vare.navn = navn.strip()
            vare.pris = pris
            vare.mva = mva
            vare.enhet = enhet.strip()
            return vare

    def nyOrdre(self, kunde = None, Id = None, ordredato = None, forfall = None):
        return fakturaOrdre(self.db, kunde=kunde, Id=Id, firma=self.firmainfo(), dato=ordredato, forfall=forfall)

    def hentOrdrer(self):
        self.c.execute("SELECT ID FROM %s" % fakturaOrdre._tabellnavn)
        return [ fakturaOrdre(self.db, Id=z[0]) for z in self.c.fetchall() ]

    def firmainfo(self):
        try:
            self.__firmainfo.hentEgenskaper()
            self.__firmainfo.sjekkData()
        except AttributeError:
            self.__firmainfo = fakturaFirmainfo(self.db)
        except FirmainfoFeil:
            self.__firmainfo = fakturaFirmainfo(self.db)
        return self.__firmainfo

    def hentEgenskapVerdier(self, tabell, egenskap):
        self.c.execute("SELECT DISTINCT %s FROM %s" % (egenskap, tabell))
        return [str(x[0]) for x in self.c.fetchall() if x[0]]

    def lagSikkerhetskopi(self, ordre):
        s = fakturaSikkerhetskopi(self.db, ordre)
        #historikk.pdfSikkerhetskopi(ordre, True, "lagSikkerhetskopi)")
        return s

    def hentSikkerhetskopier(self):
        self.c.execute("SELECT ID FROM %s" % fakturaSikkerhetskopi._tabellnavn)
        return [ fakturaSikkerhetskopi(self.db, Id = z[0]) for z in self.c.fetchall() ]

    def sjekkSikkerhetskopier(self, lagNyAutomatisk=False):
        sql = "SELECT Ordrehode.ID, Sikkerhetskopi.ID FROM Ordrehode LEFT OUTER JOIN Sikkerhetskopi ON Ordrehode.ID=Sikkerhetskopi.ordreID WHERE data IS NULL"
        self.c.execute(sql)
        ordrer = []
        for z in self.c.fetchall():
            logging.debug("Ordre #%i har ingen gyldig sikkerhetskopi!", z[0])
            o = fakturaOrdre(self.db, Id=z[0], firma=self.firmainfo())
            if lagNyAutomatisk:
                # merk evt. gammel sikkerhetskopi som ugyldig
                if z[1]:
                    s = fakturaSikkerhetskopi(self.db, Id=z[1])
                    s.data = False
                try:
                    self.lagSikkerhetskopi(o)
                    #historikk.pdfSikkerhetskopi(o, True, "sjekksikkerhetskopier(lagNyAutomatisk=True)")
                except FakturaFeil, e:
                    #historikk.pdfSikkerhetskopi(o, False, "sjekksikkerhetskopier: %s" % e)
                    raise SikkerhetskopiFeil(u'Kunne ikke lage sikkerhetskopi for ordre #%s! Årsak:\n%s' % (z[0], e))
            else:
                ordrer.append(o)
        return ordrer

    def lagPDF(self, ordre, blankettType, _filnavn=None):
        from f60 import f60, REPORTLAB
        if not REPORTLAB:
            raise PDFFeil(u'Modulen "reportlab" er ikke installert. Uten denne kan du ikke lage pdf-fakturaer.')

        pdf = f60(filnavn=_filnavn)
        #if not self.produksjonsversjon: pdf.settTestversjon()
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

    def skrivUt(self, filnavn, program='/usr/bin/kpdf'):
        if not os.path.exists(filnavn):
            raise Exception("Ugyldig filnavn: '%s'" % filnavn)
        ## XXX: TODO: Skrive ut for alle os ## QPrint() ?
        logging.debug("skriver ut '%s' vha programmet '%s'", filnavn, program)
        p = program.encode(sys.getfilesystemencoding())
        # subprocess.call på windows takler ikke unicode!
        f = filnavn.encode(sys.getfilesystemencoding())
        if '%s' in program:
            command = (p % f).split(' ')
        else:
            command = (p,  f)
        logging.debug('kjører kommando: %s',  command)
        subprocess.call(command)

    def sendEpost(self, ordre, pdf, tekst=None, transport='auto'):
        import epost
        if type(transport) == int:
            transport = epost.TRANSPORTMETODER[transport]
        if transport == 'auto':
            transport = self.testEpost()
            if transport is None:
                return False
            self.epostoppsett.transport = transport

        m = getattr(epost,transport)() # laster riktig transport (smtp/sendmail)
        oppsett = self.epostoppsett
        if transport == 'smtp':
            m.tls(bool(oppsett.smtptls))
            m.settServer(oppsett.smtpserver, oppsett.smtpport)
            if oppsett.smtpbruker: m.auth(oppsett.smtpbruker, oppsett.smtppassord)
        elif transport == 'sendmail':
            m.settSti(oppsett.sendmailsti)
        if oppsett.bcc is not None and len(oppsett.bcc) > 0:
            m.settKopi(oppsett.bcc)
        m.faktura(ordre, pdf, tekst, testmelding=self.produksjonsversjon==False)
        return m.send()

    def testEpost(self, transport='auto'):
        import epost
        if type(transport) == int:
            transport = epost.TRANSPORTMETODER[transport]
        logging.debug('skal teste transport: %s', transport)
        # finn riktig transport (gmail/smtp/sendmail)
        if not transport in epost.TRANSPORTMETODER: #ugyldig transport oppgitt
            transport = 'auto'
        if transport == 'auto':
            feil = []
            for mt in epost.TRANSPORTMETODER[1:]:
                try:
                    if self.testEpost(mt):
                        return mt
                except epost.SendeFeil,E:
                    feil += E
            ex = epost.SendeFeil()
            ex.transport = transport
            ex.transportmetoder = epost.TRANSPORTMETODER[:]
            ex.message = ', '.join(feil)
            #return (False, transport, epost.TRANSPORTMETODER)
            raise ex
        logging.debug('tester epost. transport: %s', transport)
        m = getattr(epost,transport)() # laster riktig transport
        assert(m, epost.epost)
        oppsett = self.epostoppsett
        if transport == 'smtp':
            m.tls(bool(oppsett.smtptls))
            m.settServer(oppsett.smtpserver, oppsett.smtpport)
            if oppsett.smtpbruker: m.auth(oppsett.smtpbruker, oppsett.smtppassord)
        elif transport == 'sendmail':
            m.settSti(oppsett.sendmailsti)
        try:
            t = m.test()
        except Exception,inst:
            logging.debug("%s gikk %s", transport, inst.__str__())
            ex = epost.SendeFeil()
            ex.transport = transport
            ex.transportmetoder = epost.TRANSPORTMETODER[:]
            ex.message = inst.__str__()
            raise ex
        else:
            if t:
                logging.debug("%s gikk %s", transport, t)
                return transport
            else:
                return None


def lagDatabase(database, sqlfile=None):
    "lager databasestruktur. 'database' er filnavn (unicode)"
    try:
        db = sqlite.connect(os.path.normpath(database.encode('utf8')), isolation_level=None)
        return byggDatabase(db, sqlfile)
    except sqlite.DatabaseError:
        raise
        # hmm, kanskje gammel database?
        dbver = sjekkDatabaseVersjon(database)
        if dbver != sqlite.sqlite_version_info[0]:
            e = "Databasen din (versjon %s) kan ikke leses av pysqlite, som leser versjon %s" % (dbver, sqlite.sqlite_version_info[0])
            print "FEIL!",e
            raise DBVersjonFeil(e)

def byggDatabase(db, sqlfile=None):
    "lager databasestruktur. 'db' er et sqlite3.Connection-objekt"
    if sqlfile is not None:
        sql = file(sqlfile).read()
    else:
        sql = unicode(lesRessurs(':/sql/faktura.sql'))
    db.executescript(sql)
    db.cursor().execute("INSERT INTO Oppsett (ID, databaseversjon, fakturakatalog) VALUES (1, ?, ?)",
        (DATABASEVERSJON, '~'))
    db.commit()
    return db

def finnDatabasenavn(databasenavn=DATABASENAVN):
    """finner et egnet sted for databasefila, enten fra miljøvariabler eller i standard plassering.

    følgende miljøvariabler påvirker denne funksjonen:
    FAKTURADB=navnet eller hele stien til databasefila (eks. firma2.db)
    FAKTURADIR=stien til en katalog databasene skal lagres i (eks. ~/.mittandrefirma)

    også verdien av den interne konstanten PRODUKSJONSVERSJON påvirker returverdien.

    returnerer filnavn som unicode-streng
    """
    db = os.getenv('FAKTURADB')
    if db is not None and (not PRODUKSJONSVERSJON or os.path.exists(db)):
        return db.decode(sys.getfilesystemencoding()) # returnerer miljøvariabelen $FAKTURADB
    fdir = os.getenv('FAKTURADIR')
    if not fdir:
        #sjekk for utviklermodus
        if not PRODUKSJONSVERSJON:
            return databasenavn # returner DATABASENAVN ('faktura.db'?) i samme katalog
        #sjekk for windows
        if sys.platform.startswith('win'):
            pdir = os.getenv('USERPROFILE')
            fdir = os.path.join(pdir, "finfaktura")
        else:
            #sjekk for mac
            #sjekk for linux
            pdir = os.getenv('HOME')
            fdir = os.path.join(pdir, ".finfaktura")
    fdir = fdir.decode(sys.getfilesystemencoding())
    if not os.path.exists(fdir):
        os.mkdir(fdir, 0700)
    return os.path.join(fdir, databasenavn)

def kobleTilDatabase(dbnavn=None):
    if dbnavn is None:
        dbnavn = finnDatabasenavn()
    logging.debug('skal koble til %s (%s/%s)', dbnavn, repr(dbnavn), type(dbnavn))
    dbfil = os.path.normpath(os.path.realpath(dbnavn.encode('utf-8')))
    try:
        db = sqlite.connect(database=os.path.abspath(dbfil), isolation_level=None) # isolation_level = None gir autocommit-modus
        logging.debug("Koblet til databasen %s", os.path.abspath(dbfil))
    except sqlite.DatabaseError, (E):
        logging.debug("Vi bruker sqlite %s", sqlite.apilevel)
        dbver = sjekkDatabaseVersjon(dbnavn)
        logging.debug("Databasen er sqlite %s", dbver)
        if sqlite.apilevel != dbver:
            raise DBVersjonFeil("Databasen er versjon %s, men biblioteket er versjon %s" % (dbver, sqlite.apilevel))
    return db

def sjekkDatabaseVersjon(dbnavn):
    """ skiller melllom sqlite 2 og 3. Forventer dbnavn i unicode"""
    #http://marc.10east.com/?l=sqlite-users&m=109382344409938&w=2
    #> It is safe to read the first N bytes in a db file ... ?
    #Yes.  As far as I know, that's the only sure way to determine
    #the version.  Unfortunately, the form of the header changed in
    #version 3, but if you read the first 33 bytes, you'll have an
    #array that you can search for "SQLite 2" or "SQLite format 3".

    try:
        f=open(dbnavn.encode(sys.getfilesystemencoding()))
        magic=f.read(33)
    except IOError:
        return False
    f.close()
    if 'SQLite 2' in magic: return 2
    elif 'SQLite format 3' in magic: return 3
    else: return False

def sikkerhetskopierFil(filnavn):
    """lager sikkerhetskopi av filnavn -> filnavn~

    Forventer filnavn i unicode"""
    f = filnavn.encode(sys.getfilesystemencoding())
    logging.debug('skal sikkerhetskopiere %s (altså %s)',
                  repr(filnavn), repr(f))
    assert os.path.exists(f)
    bkpfil = "%s-%s~" % (f, int(time()))
    return shutil.copyfile(f, bkpfil)

def lesRessurs(ressurs):
    """Leser en intern QT4-ressurs (qrc) og returnerer den som en QString.

    'ressurs' er på formatet ':/sti/navn', for eksempel ':/sql/faktura.sql'
    """
    from PyQt4 import QtCore
    f = QtCore.QFile(ressurs)
    if not f.open(QtCore.QIODevice.ReadOnly | QtCore.QIODevice.Text):
        raise IOError(u"Kunne ikke åpne ressursen '%s'" % ressurs)
    t = QtCore.QTextStream(f)
    t.setCodec("UTF-8")
    s = QtCore.QString(t.readAll())
    f.close()
    return s

def typeofqt(obj):
  from PyQt4 import QtGui
  if isinstance(obj, QtGui.QSpinBox): return 'QSpinBox'
  elif isinstance(obj, QtGui.QDoubleSpinBox): return 'QDoubleSpinBox'
  elif isinstance(obj, QtGui.QLineEdit): return 'QLineEdit'
  elif isinstance(obj, QtGui.QTextEdit): return 'QTextEdit'
  elif isinstance(obj, QtGui.QPlainTextEdit): return 'QPlainTextEdit'
  elif isinstance(obj, QtGui.QHtmlTextEdit): return 'QHtmlTextEdit'
  elif isinstance(obj, QtGui.QComboBox): return 'QComboBox'
  return "QWidget"

