#!/usr/bin/python -d
# -*- coding:utf8 -*-
###########################################################################
#    Copyright (C) 2005-2008- Håvard Gulldahl
#    <havard@lurtgjort.no>
#
#    Lisens: GPL2
#
# $Id$
###########################################################################

PRODUKSJONSVERSJON=False

import os.path, glob

def forbered_ressurser():
    """Kjører pyrcc4 og pyuic4 på de nødvendige filene"""
    ui_files = glob.glob(os.path.join('finfaktura', 'ui', '*.ui'))
    rc_files = ['faktura.qrc',]

    for f in ui_files:
        ret = os.system('pyuic4 -x -o "%s" "%s"' % (os.path.splitext(f)[0] + '_ui.py', f))
        print "%s: %s" % (f, ret)
    for f in rc_files:
        ret = os.system('pyrcc4 -o "%s" "%s"' % (os.path.splitext(f)[0] + '_rc.py', f))
        print "%s: %s" % (f, ret)
                  
def debug(*s):
    if not PRODUKSJONSVERSJON: print "[faktura]:", s

