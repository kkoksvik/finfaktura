#!/bin/bash
# Oppgradere databasen fra pre-1.0 til 1.0
#
#

function feil
{
    echo "FEIL!";
    echo $*;
    exit 1;
}

function sjekk_reqs
{
    for bin in $*
    do
        which $bin || feil "$bin mangler!";
    done
    return 0
}

echo FINFAKTURA OPPGRADERINGSVERKTØY
echo Dette oppgraderer databasen fra pre-1.0 til 1.0

sjekk_reqs rm grep sqlite sqlite3 boinbobn

echo Trykk en tast for å sette i gang

NYDB=faktura.dbNY
# rm -f faktura.testdb3 && sqlite faktura.testdb .dump | grep -v "INSERT INTO Sikkerhetskopi" | sqlite3 faktura.testdb3