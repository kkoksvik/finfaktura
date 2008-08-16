#!/usr/bin/python 
# -*- coding:utf-8 -*-
"""Regne økonomi"""
###########################################################################
#    Copyright (C) 2005-2008- Håvard Gulldahl
#    <havard@lurtgjort.no>
#
#    Lisens: GPL2
#
# $Id$
###########################################################################

from fakturakomponenter import fakturaOrdre
from string import join

class ordreHenter:
    begrens = []
    varer   = []
    vare    = False
    sorter  = None
    antall  = None
    
    
    def __init__(self, db):
        self.db = db
        self.c = db.cursor()
        self.begrens = []
        self.varer   = []
        self.vare    = False
        self.sorter  = None
        self.antall  = None
        
    def begrensDato(self, fraEpoch=None, tilEpoch=None):
        if fraEpoch is not None:
            self.begrens.append(" ordredato > %i " % fraEpoch)
        if tilEpoch is not None:
            self.begrens.append(" ordredato < %i " % tilEpoch)
        
    def begrensKunde(self, kunde):
        self.begrens.append(" kundeID = %i " % kunde._id)
    
    def begrensVare(self, vare):
        self.vare = True
        self.varer.append(vare._id)
        
    def begrensAntall(self, antall):
        self.antall = antall
    
    def visKansellerte(self, vis):
        if not vis: self.begrens.append(" kansellert = 0 ")
    
    def visUbetalte(self, vis):
        if not vis: self.begrens.append(" betalt != 0 ")
    
    def sorterEtter(self, kolonne):
        s = { 'dato':'ordredato', 'kunde':'kundeID', 'vare':'vareID' }
        self.sorter = " ORDER BY %s " % s[kolonne]
        if kolonne == 'vare': self.vare = True
    
    def hentOrdrer(self):
        self.c.execute(self._sql())
        return [ fakturaOrdre(self.db, Id=z[0]) for z in self.c.fetchall() ]
    
    def _sql(self):
        s = "SELECT Ordrehode.ID FROM %s" % fakturaOrdre._tabellnavn
        if self.vare:
            # SELECT Ordrehode.ID FROM Ordrehode LEFT OUTER JOIN Ordrelinje ON Ordrehode.ID=Ordrelinje.ordrehodeID WHERE vareID=3;
            s += " LEFT OUTER JOIN Ordrelinje ON Ordrehode.ID=Ordrelinje.ordrehodeID "
            #s += join(vareID=%i " % self.
            for v in self.varer: self.begrens.append(" vareID=%i " % v)
        if self.begrens:
            s += " WHERE " + join(self.begrens, " AND ")
        if self.sorter:
            s += self.sorter
        if self.antall:
            s += " LIMIT %i " % antall
        print s
        return s