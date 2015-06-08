# Introduksjon #

Skal du lage fakturaer for flere firma? _Fryktelig Fin Faktura_ har ikke støtte for å bytte mens programmet kjører, men det er [fullt støttet ved å sette miljøvariabler](StarteProgrammet.md)

# Hvordan? #

Fakturadatabasen rommer **alle innstillinger til gjeldende firma**, og kan flyttes mellom maskiner og installasjoner. Det gjør at man enkelt kan sette opp ulike firma, ved å angi ulike databaser.

Her er et eksempel på to ulike måter å sette opp firma nummer 2 i linux:

  * `FAKTURADIR=~/.mittandrefirma/ faktura.py` ## Setter annen katalog, **anbefales**
  * `FAKTURADB=~/.mittandrefirmadb faktura.py` ## Setter annen database direkte.

Slik gjør du det samme i windows (for eksempel i en `.bat`-fil):

  1. `SET FAKTURADIR="%HOMEPATH%\mitt_andre_firma\"`, og deretter
  1. `python faktura.py`
