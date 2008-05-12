#!/usr/bin/python -d
# -*-*- coding:utf8 -*-*-
###########################################################################
#    Copyright (C) 2005-2008- Håvard Gulldahl 
#    <havard@lurtgjort.no>
#
#    Lisens: GPL2
#
# $Id$
###########################################################################

class FakturaFeil(Exception): pass
class KundeFeil(Exception): pass
class DBKorruptFeil(Exception): pass
class DBGammelFeil(Exception): pass
class DBNyFeil(Exception): pass
class DBTomFeil(Exception): pass
class DBVersjonFeil(Exception): pass
class FirmainfoFeil(Exception): pass
class SikkerhetskopiFeil(Exception): pass
class PDFFeil(Exception): pass


