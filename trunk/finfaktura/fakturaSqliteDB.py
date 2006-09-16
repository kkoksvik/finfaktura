#!/usr/bin/python -d
# -*- coding:utf8 -*-
###########################################################################
#    Copyright (C) 2006 - Håvard Dahle
#    <havard@dahle.no>
#
#    Lisens: GPL
#
# $Id: fakturaSqliteDB.py,v 1.1 2006/06/03 00:48:22 havardda Exp $
###########################################################################

def lagDatabase(database, dbsql=DATABASESQL):
    import sqlite
    logg = open("faktura.sqlite.lag.log", "a+")
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
    #sjekk for windows
    #sjekk for mac
    pdir = os.getenv('HOME')
    
    fdir = os.path.join(pdir, ".finfaktura")
    if not os.path.exists(fdir):
        os.mkdir(fdir, 0700)
    return os.path.join(fdir, databasenavn)
