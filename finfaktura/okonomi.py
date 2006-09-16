#!/usr/bin/python 
# -*- coding:utf-8 -*-
"""Regne økonomi"""
###########################################################################
#    Copyright (C) 2006 - Håvard Dahle
#    <havard@dahle.no>
#
#    Lisens: GPL2
#
# $Id: okonomi.py,v 1.1 2006/06/03 00:48:23 havardda Exp $
###########################################################################

from fakturabibliotek import fakturaOrdre
from string import join

class ordreHenter:
    begrens = []
    vare    = []
    antall  = None
    
    def __init__(self, db):
        self.db = db
        self.c = db.cursor()
        self.begrens = []
        self.vare    = []
        self.antall  = None
        
    def begrensDato(self, fraEpoch=None, tilEpoch=None):
        if fraEpoch is not None:
            self.begrens.append(" ordredato > %i " % fraEpoch)
        if tilEpoch is not None:
            self.begrens.append(" ordredato < %i " % tilEpoch)
        
    def begrensKunde(self, kunde):
        self.begrens.append(" kundeID = %i " % kunde._id)
    
    def begrensVare(self, vare):
        self.vare.append(vare._id)
        
    def begrensAntall(self, antall):
        self.antall = antall
    
    def hentOrdrer(self):
        #self.c.execute("SELECT ID FROM %s" % fakturaOrdre._tabellnavn)
        self.c.execute(self._sql())
        return [ fakturaOrdre(self.db, Id=z[0]) for z in self.c.fetchall() ]
    
    def _sql(self):
        s = "SELECT ID FROM %s" % fakturaOrdre._tabellnavn
        if self.vare:
            # s += " LEFT JOIN xxx ON yyy=zzz
            pass
        if self.begrens:
            s += " WHERE " + join(self.begrens, " AND ")
        if self.antall:
            s += " LIMIT %i " % antall
        print s
        return s