#!/usr/bin/python
# -*- coding:utf8 -*-
# kate: indent-width 4;
###########################################################################
#    Copyright (C) 2005-2009 Håvard Gulldahl og Håvard Sjøvoll
#    <havard@gulldahl.no>, <sjovoll@ntnu.no>
#
#    Lisens: GPL2
#
# $Id$
#
###########################################################################

__doc__ = """Fryktelig fin faktura: skriv ut fakturaene dine"""

import sys, logging
from finfaktura.fakturafeil import *

if __name__ == "__main__":

    DEBUG = "-d" in sys.argv[1:]

    if DEBUG:
        logging.basicConfig(level=logging.DEBUG)
    if "-h" in sys.argv[1:]:
        print __doc__
        print "Bruk %s -i for å lage kommandolinjefaktura" % sys.argv[0]
        sys.exit()
    elif '-v' in sys.argv[1:]:
        import finfaktura
        print finfaktura.__version__
    elif "-i" in sys.argv[1:]:
        #interactive"
        from finfaktura.cli import cli_faktura
        cli_faktura()
    else:
        try:
            import finfaktura.gui
            sys.exit(finfaktura.gui.start())
        except RessurserManglerFeil, (e):
            print e
            print u"Feil! Ressursene er ikke generert (det må \ndu gjøre dersom du sjekker ut fra SVN selv)"
            print u"Lager ressursene. Ta en titt på \nscripts/forbered_ressurser.sh eller \nfinfaktura/ekstra.py for detaljer"
            from finfaktura.ekstra import forbered_ressurser
            forbered_ressurser()
        except ImportError, (e):
            print u"OOPS! Problemer med å laste moduler (bruk -d for å vise feilmelding)"
            if DEBUG:
                logging.exception(e)
            print u"Faller tilbake til konsollmodus ..."
            print
            from finfaktura.cli import cli_faktura
            cli_faktura()
