# Innledning #

I første rekke er finfaktura utviklet for at du skal kunne [lage, vise og administrere fakturaer i et grafisk grensesnitt](SlikSerDetUt.md), men det har også en "nød-modus" hvor man kan **opprette fakturaer fra kommandolinja** -- også kalt _konsollet_ eller _terminalen_.

## Hvorfor? ##

Den klassiske _use case_ for dette er at du befinner deg langt unna datamaskinen som har faktura-databasen, og du skal opprette en faktura. Du logger inn på maskinen over nettverket (for eksempel med _ssh_), men siden du er på en nettkafé som bare har windows, kan du ikke starte det grafiske grensesnittet.

Men ved hjelp av **konsoll-modusen til finfaktura kan du likevel opprette en faktura**, og sende pdf-en til kunden.

# Hvordan #

Bruk opsjonen `-i` (for interaktiv) når du starter finfaktura fra kommandolinja:

```
$ ./finfaktura.py -i

velg fra liste (3 valg):
        1 Kunde én, ****, kunde # 001
        2 Kunde to, ****, kunde # 002
        3 Kunde tre, ****, kunde # 004
velg kunde:

...
```


## Nødmodus ##

Dersom programmet **ikke klarer å laste det grafiske grensesnittet**, vil det falle tilbake til konsollmodus:

```
$ ./faktura.py
OOPS! Problemer med å laste moduler (bruk -d for å vise feilmelding)
Faller tilbake til konsollmodus ...

velg fra liste (3 valg):
        1 Kunde én, ****, kunde # 001
        2 Kunde to, ****, kunde # 002
        3 Kunde tre, ****, kunde # 004
velg kunde:

...
```

# Fremgangsmåte #

I konsollmodus kan du **utelukkende lage nye fakturaer**.

I listevalgene skriver du inn tallet foran elementet du velger. Til en hver tid kan du avbryte med `Ctrl-C`.

Programmet har følgende rekkefølge:

  1. Velg kunde
  1. Velg vare
  1. Velg antall av vare
  1. Skriv fakturatekst
  1. Bekreft (skriv "JA")

### Eksempel ###
```

velg fra liste (3 valg):
        1 Kunde én, ****, kunde # 001
        2 Kunde to, ****, kunde # 002
        3 Kunde tre, ****, kunde # 004
velg kunde: 1
kunde:  Kunde én, ****, kunde # 001
velg fra liste (3 valg):
        1 en fin vare: 201.00 kr (25 % mva)
        2 fisk: 1000.00 kr (25 % mva)
        3 Rå sild: 99.99 kr (25 % mva)
velg vare: 1
antall  meter: 4
Fakturatekst: Fire meter av den fineste varen
STEMMER DETTE?
    =====
    Kunde: Kunde én, ****, kunde # 001
    Vare: 4  meter en fin vare: 201.00 kr (25 % mva)
    Tekst: Fire meter av 2den fineste varen
    SUM: 1005.00 kr (derav mva: 201.00)
    =====
NEI/ja (Enter for å avbryte):

```