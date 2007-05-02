#!/usr/bin/env python
# -*- coding:utf8 -*-
###########################################################################
#    Copyright (C) 2006 - Håvard Dahle 
#    <havard@dahle.no>
#
#    Lisens: GPL2
#
# $Id$
###########################################################################

import fakturabibliotek 
import types, sys, time

debug = fakturabibliotek.debug

class fakturaHandling(fakturabibliotek.fakturaKomponent):
    _tabellnavn = "Handling"
    def __init__(self, db, Id = None, navn = None):
        self.db = db
        self.navn = navn
        if Id is None:
            Id = self.nyId()
        self._id = Id
        
    def nyId(self):
        self.c.execute("INSERT INTO %s (ID, navn) VALUES (NULL, ?)" % self._tabellnavn, (self.navn,))
        self.db.commit()
        return self.c.lastrowid
                
class historiskHandling:
    handlingID = 0
    dato = 0
    suksess = 0
    navn = None
    forklaring = ''
    ordreID = 0
    db = None
        
    def handling(self):
        return fakturaHandling(self.db, self.handlingID)
    
    def settHandling(self, handling):
        assert isinstance(handling, fakturaHandling)
        self.handlingID = handling._id
        return True
    
    def finnHandling(self, navn):
        assert type(navn) in types.StringTypes
        self.c.execute('SELECT ID FROM Handling WHERE navn=?', (navn,))
        return fakturaHandling(self.db, self.c.fetchone()[0], navn)
    
    def registrerHandling(self):
        #skriver til databasen
        self.c.execute("INSERT INTO Historikk (ordreID, dato, handlingID, suksess, forklaring) VALUES (?,?,?,?,?)", (self.ordreID, self.dato, self.handlingID, self.suksess & 1, self.forklaring))
        self.db.commit()
    
    def __init__(self, ordre, suksess, forklaring=None):
        assert isinstance(ordre, fakturabibliotek.fakturaOrdre)
        self.db = ordre.db
        self.c  = self.db.cursor()
        self.ordreID = ordre.ID
        self.dato = time.mktime(time.localtime())
        self.suksess = suksess
        self.forklaring = forklaring
        if self.navn is not None:
            self.settHandling(self.finnHandling(self.navn))
        self.registrerHandling()
        
class opprettet(historiskHandling):
    navn = 'opprettet'
        
class forfalt(historiskHandling):
    navn = 'forfalt'
    
class markertForfalt(historiskHandling):
    navn = 'markertForfalt'
    
class purret(historiskHandling):
    navn = 'purret'    
    
class betalt(historiskHandling):
    navn = 'betalt'    
    
class avbetalt(historiskHandling):
    navn = 'avbetalt'    
    
class kansellert(historiskHandling):
    navn = 'kansellert'
    
class avKansellert(historiskHandling):
    navn = 'avKansellert'

class sendtTilInkasso(historiskHandling):
    navn = 'sendtTilInkasso'

class utskrift(historiskHandling):
    navn = 'utskrift'

class epostSendt(historiskHandling):
    navn = 'epostSendt'

class epostSendtSmtp(historiskHandling):
    navn = 'epostSendtSmtp'

class epostSendtGmail(historiskHandling):
    navn = 'epostSendtGmail'

class epostSendtSendmail(historiskHandling):
    navn = 'epostSendtSendmail'

class pdfEpost(historiskHandling):
    navn = 'pdfEpost'

class pdfPapir(historiskHandling):
    navn = 'pdfPapir'

class pdfSikkerhetskopi(historiskHandling):
    navn = 'pdfSikkerhetskopi'

