#!/usr/bin/python -d
# -*- coding:utf8 -*-
###########################################################################
#    Copyright (C) 2006 - Håvard Dahle
#    <havard@dahle.no>
#
#    Lisens: GPL2
#
# $Id$
###########################################################################


from qt import *
from cStringIO import StringIO

class QBuffer(QIODevice):

    def __init__(self):
        QIODevice.__init__(self)
        self.open( IO_ReadOnly)

    def open(self, mode):
        self.__io = StringIO()
        return True

    def close(self):
        self.__io.close()

    def flush(self):
        self.__io.flush()

    def readAll(self):
        return self.__io.read()

    def getch(self):
        return self.__io.read(1)

    def readBlock(self, size):
        result = self.__io.read(size)
        if result:
            return (result,)

        return None

    def writeBlock(self, data, length=None):
        if type(data) == QByteArray:
            data = data.data()

        self.__io.write(data)

        return len(data)

    def getData(self):
        return self.__io.getvalue()