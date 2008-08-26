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

def install_resources():
    """Kjører pyrcc4 og pyuic4 på de nødvendige filene"""
    ui_files = glob.glob(os.path.join('finfaktura', 'ui', '*.ui'))
    rc_files = ['faktura.qrc',]

    for f in ui_files:
        out = os.path.join('finfaktura', 'ui', os.path.basename(f) + '_ui.py')
        os.system('pyuic4 -x -o "%s" "%s"' % (out, f)
    for f in rc_files:
        out = os.path.join('finfaktura', 'ui', os.path.basename(f) + '_rc.py')
        os.system('pyrcc4 -x -o "%s" "%s"' % (out, f)
                  
setup(name="finfaktura",
      version=finfaktura.__version__,
      description="Fryktelig Fin Faktura - fakturaprogram for norske næringsdrivende",
      author="Håvard Gulldahl",
      author_email="havard@gulldahl.no",
      url="http://finfaktura.googlecode.com/",
      packages=['finfaktura',],
      data_files=[#('share/finfaktura/pixmaps', ['pixmaps/error.png', 'pixmaps/warning.png']),
            ('share/finfaktura/data', ['faktura.ui', 'sendepost.ui', 'faktura.sql']),
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
