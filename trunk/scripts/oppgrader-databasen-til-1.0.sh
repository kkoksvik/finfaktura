#!/bin/bash
# Oppgradere databasen fra pre-1.0 til 1.0
#
# $Id$

function feil
{
    echo -n "FEIL! ";
    echo $*;
    exit 1;
}

function sjekk_reqs
{
    for bin in $*
    do
        which $bin > /dev/null || feil "$bin mangler!";
    done
    return 0
}

echo 'FINFAKTURA OPPGRADERINGSVERKTØY';
echo 'Dette oppgraderer databasen fra pre-1.0 (sqlite2) til 1.0 (sqlite3)';

sjekk_reqs rm grep sqlite sqlite3 python

echo Trykk en tast for å sette i gang

NYDB=faktura.dbNY
GMLDB=faktura.testdb
KAT=$(mktemp -d /tmp/sikkerhetskopi.XXXXXXX);

rm -r "$NYDB" && sqlite "$GMLDB" .dump | grep -v "INSERT INTO Sikkerhetskopi" | sqlite3 "$NYDB"

# export IFS='|'
# sqlite faktura.testdb "SELECT * FROM Sikkerhetskopi" | 
# ( while read id ordre dato blob; do echo $id $dato; echo $blob > /tmp/id-$id-ordre-$ordre-dato-$dato.pdf; done )  

cat<<PYTHON1|/usr/bin/env python
# -*-*- encoding: utf-8 -*-*-*
import sqlite

try: import sqlite3
except ImportError: from pysqlite2 import dbapi2 as sqlite3

db1 = sqlite.connect("$GMLDB")
c1 = db1.cursor()

db2 = sqlite3.connect("$NYDB")
c2 = db2.cursor()

liste = []

c1.execute("SELECT ID FROM Sikkerhetskopi")
for _i in c1.fetchall():
    i = _i[0]
    c1.execute("SELECT ID,ordreID,dato,data FROM Sikkerhetskopi WHERE ID=%s" % i)
    liste.append(c1.fetchone())
db1.close()

c2.executemany("INSERT INTO Sikkerhetskopi (ID, ordreID, dato, data) VALUES (?,?,?,?)", liste)
db2.commit()
print "Oppdatert"

PYTHON1

echo "Sjekker den nye databasen"
sqlite3 "$NYDB" "SELECT ID,ordreID,dato,length(data) FROM Sikkerhetskopi"


echo "Finfint. Den oppgraderte databasen heter $NYDB. Du må selv flytte "
echo "den til ~/.finfaktura eller den katalogen hvor du har fakturadatabasen din"