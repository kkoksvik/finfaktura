#!/bin/bash
# Oppgradere databasen fra pre-1.0 til 1.0
#
# $Id$

GMLDB=${FAKTURADB:-~/.finfaktura/faktura.db}
NYDB=${GMLDB}-ny

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
        which $bin > /dev/null || feil "$bin mangler! Kanskje du må installere den?";
    done
    return 0
}

echo 'FINFAKTURA OPPGRADERINGSVERKTØY';
echo 'Dette oppgraderer databasen fra pre-1.0 (sqlite2) til 1.0 (sqlite3)';
echo "Den eksisterende databasen $GMLDB skal oppdateres";
sjekk_reqs cp mv rm grep cat date sqlite sqlite3 python

echo Trykk en tast for å sette i gang

######################################
test -f "$GMLDB" || feil "$GMLDB eksisterer ikke!";

tidsstempel=$(date +%s);

cp "${GMLDB}" "${GMLDB}-${tidsstempel}~" || feil "Kunne ikke lage backup av $GMLDB";

DBBACKUP="${GMLDB}-${tidsstempel}~";

rm -f "$NYDB" && sqlite "$GMLDB" .dump | grep -v "INSERT INTO Sikkerhetskopi" | sqlite3 "$NYDB"

cat<<PYTHON1|/usr/bin/env python
# -*-*- encoding: utf-8 -*-*-*
import sys
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
    r = c1.fetchone()
    liste.append(tuple(r[0:3]) + tuple((sqlite3.Binary(r[3]),)))
db1.close()

c2.executemany("INSERT INTO Sikkerhetskopi (ID, ordreID, dato, data) VALUES (?,?,?,?)", liste)
db2.commit()
print "Oppdatert"
db2.close()

PYTHON1

test $? -eq 0 || feil "Noe gikk galt med python-skriptet! Stopper før det skjer noe mer."

echo "Sjekker den nye databasen"
l=$(sqlite3 "$NYDB" "SELECT ID,ordreID,dato,length(data) FROM Sikkerhetskopi" | wc -l);

test $l -gt 0 || feil "Noe gikk galt med python-skriptet! Stopper før det skjer noe mer."

mv "${GMLDB}" "${GMLDB}-`date +%s`~" && mv "$NYDB" "$GMLDB" && echo "Finfint. Den oppgraderte databasen er flyttet til $GMLDB "
