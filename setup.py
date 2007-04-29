#!/usr/bin/env python
# -*- coding:utf8 -*-
###########################################################################
#    Copyright (C) 2005-2006 - Håvard Dahle og Håvard Sjøvoll
#    <havard@dahle.no>, <sjovoll@ntnu.no>
#
#    Lisens: GPL2
#
# $Id$
###########################################################################


from distutils.core import setup
#from setuptools import setup

import sys, os.path, glob

import finfaktura # for versjonsnummer

setup(name="fryktelig-fin-faktura",
      version=finfaktura.__version__,
      description="Fryktelig Fin Faktura - fakturaprogram for norske næringsdrivende",
      author="Håvard Dahle",
      author_email="havard@dahle.no",
      url="http://www.orakel.ntnu.no/~havardda/kode?navn=fryktelig+fin+faktura",
      packages=['finfaktura',],
      data_files=[#('share/finfaktura/pixmaps', ['pixmaps/error.png', 'pixmaps/warning.png']),
            ('share/finfaktura/data', ['faktura.ui', 'faktura.sql']),
            ('share/finfaktura/scripts', glob.glob('scripts/*')),
           ],
      #package_data={'finfaktura': ['pixmaps/*.png'] },
      scripts=["faktura.py"],
      license="GPL2",
      long_description=file(os.path.split(os.path.realpath(sys.argv[0]))[0] + "/README").read(),
      #install_requires = ['docutils>=0.3', 'reportlab'],
      #zip_safe=True,
      #include_package_data = True,
          #entry_points = {
        #'console_scripts': [
            #'faktura_cli = faktura:cli_faktura',
        #],
     #}
     )
