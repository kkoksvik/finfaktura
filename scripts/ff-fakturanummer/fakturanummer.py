#!/usr/bin/python -d
# -*- coding: utf-8 -*-
# kate: indent-width 4; encoding utf-8
###########################################################################
#    Copyright (C) 2009 Håvard Gulldahl
#    <havard@gulldahl.no>
#
#    Lisens: GPL2
#
# $Id: faktura.py 260 2008-05-11 08:59:23Z havard.gulldahl $
#
###########################################################################


import sys, os, os.path, logging, glob
from time import time, strftime, localtime, mktime
import logging

from stat import ST_MTIME

from PyQt4 import QtCore, QtGui, uic

import sqlite3

class nummersetter(object):
  def __init__(self):
    pass

  def settDatabase(self, db):
    self.databasenavn = db
    self.db = sqlite3.connect(db)

  def lesDBInfo(self, database=None):
    if database is None:
      databasenavn = self.databasenavn
      db = self.db
    else:
      databasenavn = database
      if not os.path.exists(databasenavn): return False
      db = sqlite3.connect(databasenavn)


    mtime = os.stat(databasenavn)[ST_MTIME]

    cursor = db.cursor()
    try:
      cursor.execute('SELECT firmanavn FROM Firma')
      fnavn = cursor.fetchone()
      cursor.execute('SELECT * FROM Ordrehode')
      ffaktura = cursor.fetchall()

      status = len(ffaktura) == 0
    except sqlite3.Error:
      status = False
      firmanavn = 'Feil'

    
    ret = {'filnavn':databasenavn,
           'firmanavn':firmanavn,
           'endret':mtime,
           'status':status}

    return ret
    
        


class nummersettergui(object):
  def __init__(self):
    self.gui = uic.loadUi('gui.ui')
    self.gui.connect(self.gui.databasenavn, QtCore.SIGNAL('activated(QString)'), self.slotDatabaseValgt)
    self.gui.show()
    self.gui.databasenavn.addItems(list(self.listDatabaser()))
    self.help = nummersetter()

  def listDatabaser(self):
    if os.path.exists(os.getenv('FAKTURADB', '')):
      yield os.getenv('FAKTURADB')
    for d in (os.path.join(os.getenv('HOME', ''), '.finfaktura'),
              os.path.join(os.getenv('HOME', ''), 'finfaktura'),
              os.getenv('FAKTURADIR'),
              '.'):
      if not d: continue
      if not os.path.exists(d): continue
      for f in glob.glob(os.path.join(d, '*.db')):
        yield f
    yield '...'

  def slotDatabaseValgt(self, s):
    logging.debug('valgte database: %s', s)
    filename = unicode(s, sys.getfilesystemencoding())
    if filename == '...':
      return self.velgDatabase()
    status = self.help.lesDBInfo()
    logging.debug('status:%s', status)

  
      

if __name__ == '__main__':
  logging.basicConfig(level=logging.DEBUG)
  a = QtGui.QApplication(sys.argv)
  p = nummersettergui()
  a.exec_()

  
