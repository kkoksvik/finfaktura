# Jeg tror jeg har funnet en feil #

Det kan være ulike årsaker til at programmet ikke starter eller fungerer som det skal. Det vil vi gjerne høre om, slik at det kan fikses!

Du kan enten [sende en epost til epostlista](mailto:finfaktura@googlegroups.com), hvor du beskriver problemet, eller du kan [legge inn en feiloppføring](http://code.google.com/p/finfaktura/issues/list), slik at vi kan finne ut av det.

# Hvis noe er feil med Fryktelig Fin Faktura #

For å finne ut av årsaken til problemet, må prorammet startes på en spesiell måte, slik at alle feilmeldinger kommer frem.

Spesifikt må **programmet startes fra kommandolinja (også kalt terminalvindu), og all utputt må sendes inn**.

Her er et eksempel på hvordan det kan gjøres:

  1. Start et terminalvindu. I Gnome er dette kalt `gnome-terminal`, bruker du KDE heter programmet `konsole`.
  1. _Hold inne `Alt`-knappen og trykk `F2`. Da kan du skrive inn programnavnet_
  1. Skriv inn `/usr/bin/faktura.py -d` og trykk `[Enter]`. Da kommer en rekke linjer med informasjon på skjermen.
  1. Bruk programmet som normalt inntil problemet oppstår (hopp over dette dersom problemet er at programmet ikke starter, såklart).
  1. Kopiér alt som står i terminalvinduet og lim det inn i en epost eller en feiloppføring (som beskrevet i første avsnitt).
  1. Skriv også i meldinga hva det er du forsøker å gjøre, hvordan det går galt og hva du forventet skulle skje.

# Hvis programmet ikke vil la seg installere #

Som over må du gjøre installasjonen fra kommandolinja for at alle relevante feilmeldinger skal vises.

  1. Start et terminalvindu (se over).
  1. Last ned siste versjon av _Fryktelig Fin Faktura_, og lagre installasjonsfila et sted på harddisken.
  1. Start installasjonsprogrammet. I Debian og Ubuntu-varianter kan du bruke `dpkg`: skriv `sudo dpkg -i <sti til installasjonsfila>`. Bruker du Fedora, Red Hat, SuSE, Mandrake er det `rpm` som er installasjonsprogram: skriv `sudo rpm -i <sti til installasjonsfila>`.
  1. Send inn alt som kommer i vinduet etter denne kommandoen.