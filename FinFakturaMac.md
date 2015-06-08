Dette dokumentet går gjennom alternativer for å bruke _Fin Faktura_ på OS X.

## Fink ##

Inntil noen lager en korrekt pakke (har du en mac og har lyst til å [hjelpe til?](mailto:havard@gulldahl.no)), er dette det eneste alternativet.

[Fink er et prosjekt som frir til OSX' unix-bakgrunn](http://www.finkproject.org/index.php) og pakker en rekke programmer slik at de passer inn i systemet. Ved hjelp av enkle tekstkommandoer i konsollet kan man installere et lass av nyttige hjelpemidler.

Det er i utgangspunktet ikke grafisk styrt, og bruken forutsetter at man er komfortabel med det tekst-baserte konsollet.

> ### Slik går du frem ###

  1. Sett opp Fink
  1. Installer pakken [pyqt4-py25-bin](http://pdb.finkproject.org/pdb/package.php/pyqt4-py25-bin)
  1. Last ned [\_Fin Faktura\_ som \*python kildekode\*](http://code.google.com/p/finfaktura/downloads/list) (slutter på .zip)
  1. I konsollet, kjør `python setup.py install`
  1. Ferdig.

## Lenker ##

http://aralbalkan.com/1675