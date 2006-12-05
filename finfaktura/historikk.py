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
#import sqlite
import types, sys, time

class fakturaHandling(fakturabibliotek.fakturaKomponent):
    _tabellnavn = "Handling"
    
class historiker:
    
    def __init__(self, db):
        print type(db)
        assert isinstance(db, SQLType)
        self.db = db
        self.c  = db.cursor()
    
    def logg(self, handling):
        assert isinstance(handling, historiskHandling)
        self.c.execute("""INSERT INTO Historikk
                     (ordreID, dato, handlingID, suksess, forklaring)
                     VALUES
                     (%s, %s, %s, %s, %s)""", dict(handling) )
        self.db.commit()
        
def finnHandling(self, navn):
    assert type(navn) in (types.StringType, types.UnicodeType)
    self.c.execute('SELECT ID FROM Handling WHERE navn=%s', navn)
    i = self.c.fetchone()
    return fakturaHandling(self.db, i)
        
class historiskHandling:
    handlingID = 0
    dato = 0
    suksess = 0
    navn = None
    forklaring = ''
    ordreID = 0
        
    def handling(self):
        return fakturaHandling(self.db, self.handlingID)
    
    def settHandling(self, handling):
        assert isinstance(handling, fakturaHandling)
        self.handlingID = handling.ID
        return True
    
    def __init__(self, ordre, suksess, forklaring=None):
        assert isinstance(ordre, fakturabibliotek.fakturaOrdrehode)
        self.ordreID = ordre.ID
        self.dato = time.mktime(time.localtime())
        self.suksess = suksess
        self.forklaring = None
        if self.navn is not None:
            self.settHandling(finnHandling(self.navn))
        
def opprettet(historiskHandling):
    navn = 'opprettet'
        
def forfalt(historiskHandling):
    navn = 'forfalt'
    
def markertForfalt(historiskHandling):
    navn = 'markertForfalt'
    
def purret(historiskHandling):
    navn = 'purret'    
    
def betalt(historiskHandling):
    navn = 'betalt'    
    
def kansellert(historiskHandling):
    navn = 'kansellert'
    
def avKansellert(historiskHandling):
    navn = 'avKansellert'

def utskrift(historiskHandling):
    navn = 'utskrift'

def epostSendt(historiskHandling):
    navn = 'epostSendt'

def epostSendtSmtp(historiskHandling):
    navn = 'epostSendtSmtp'

def epostSendtGmail(historiskHandling):
    navn = 'epostSendtGmail'

def epostSendtSendmail(historiskHandling):
    navn = 'epostSendtSendmail'

def pdfEpost(historiskHandling):
    navn = 'pdfEpost'

def pdfPapir(historiskHandling):
    navn = 'pdfPapir'

def pdfSikkerhetskopi(historiskHandling):
    navn = 'pdfSikkerhetskopi'

