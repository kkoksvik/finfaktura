#!/usr/bin/python -d
# -*- coding: utf-8 -*-
# kate: indent-width 4;
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

from PyQt4 import QtCore, QtGui, uic

class nummersetter(object):
  def __init__(self):
    self.gui = uic.loadUi('gui.ui')
    self.gui.connect(self.gui.databasenavn, QtCore.SIGNAL('currentIndexChanged(QString&)'), self.slotDatabaseValgt)
    self.gui.show()
    self.gui.databasenavn.addItems(list(self.listDatabaser()))

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
    
      

if __name__ == '__main__':
  a = QtGui.QApplication(sys.argv)
  p = nummersetter()
  a.exec_()

  
