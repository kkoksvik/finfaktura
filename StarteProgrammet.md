# Miljøvariabler #

Programmet gjenkjenner en rekke miljøvariabler ved oppstart, og vil på bakgrunn av disse avgjøre hvor **databasen med fakturaer** skal lastes fra.

  * `FAKTURADB`: Dette oppgir **navnet på databasefila** eksplisitt
  * `FAKTURADIR`: Dette styrer **hvilken katalog databasefila skal hentes fra**

## Standarder ##

Dersom `FAKTURADB` ikke er satt, brukes standard databasenavn (`faktura.db`).

`FAKTURADIR` er i utgangspunktet `~/.finfaktura/` på Linux og `XXX` på Windows og OSX.


## Hvordan sette miljøvariabler ##

Avhengig av operativsystem, settes disse miljøvariablene på ulikt vis. Her er noen eksempler:

  * Linux 1) `export FAKTURADB=testdata.db`, og deretter `./faktura.py`
  * Linux 2) `FAKTURADB=testdata.db ./faktura.py` (_kortform av linja over_)
  * Windows `SET FAKTURADB=testdata.db` og deretter `faktura.py`



# Opsjoner #

Gjennom ulike programopsjoner kan du styre programmets oppførsel.

  * `-d`: Aktiverer _debug_-modus (skriver meldinger i konsollet)
  * `-v`: Skriver versjon og avslutter
  * `-h`: Skriver hjelpetekst og avslutter
  * `-i`: Starter [konsoll-modus](FakturaFraKommandolinja.md)

(Denne lista kan være utdatert. Se i [SVN for en oppdatert liste](http://code.google.com/p/finfaktura/source/browse/trunk/faktura.py))