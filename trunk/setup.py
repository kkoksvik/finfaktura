#!/usr/bin/env python
# -*- coding:utf8 -*-
###########################################################################
#    Copyright (C) 2005-2008- Håvard Gulldahl og Håvard Sjøvoll
#    <havard@lurtgjort.no>, <sjovoll@ntnu.no>
#
#    Lisens: GPL2
#
# $Id$
###########################################################################


from distutils.core import setup
#from setuptools import setup

import sys, os, os.path, glob

import finfaktura # for versjonsnummer

setup(name="finfaktura",
      version=finfaktura.__version__,
      description="Fryktelig Fin Faktura - fakturaprogram for norske næringsdrivende",
      author="Håvard Gulldahl",
      author_email="havard@gulldahl.no",
      url="http://finfaktura.googlecode.com/",
      packages=['finfaktura', 'finfaktura.ui'],
      data_files=[
            ('share/finfaktura/scripts', glob.glob('scripts/*')),
           ],
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
