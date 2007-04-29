#!/bin/bash
###########################################################################
#    Copyright (C) 2006 - Håvard Dahle 
#    <havard@dahle.no>
#
#    Lisens: GPL2
#
# $Id$
###########################################################################


PROGRAMNAVN="FRYKTELIG FIN FADESE (utviklerversjon)" 

TESTNAVN="finfaktura" 
TESTDATO=$(date +%Y-%m-%d);

root_geometry=`xprop -root _NET_DESKTOP_GEOMETRY |cut -d= -f2`
root_x=`echo $root_geometry |cut -d, -f1`
root_y=`echo $root_geometry |cut -d, -f2`
xc=$((root_x/2-1))
yc=$((root_y/2-1))

echo XC: $xc
echo yC: $yc

function alt {
    KNAPP=$1;
    xte 'keydown Alt_L' "key $KNAPP" 'keyup Alt_L';
}

function knips {
    BILDENAVN=$1;
    KATALOG=$2;
    import -silent -window "$PROGRAMNAVN" "$KATALOG"/"$BILDENAVN".png;
}

function bilde {
    FUNKSJON=$1;
    KNAPP=$2;
    KATALOG=$3;
    echo "Trykker Alt+$KNAPP";
    alt $KNAPP;
    sleep 1;
    echo "Tar bilde av $FUNKSJON";
    knips "$FUNKSJON" "$KATALOG";
}



# FINN VERSJONEN VI TESTER
VERSJON=$(./faktura.py -v);

# LAG BILDEKATALOG
BILDEKATALOG=skjermbilder-$TESTNAVN-$VERSJON-$TESTDATO;
test -d "$BILDEKATALOG" || mkdir "$BILDEKATALOG";

# START PROGRAMMET
{ FAKTURADB=testdata.db ./faktura.py & };

# VENT TIL PROGRAMMET HAR STARTET
sleep 5;

# TA BILDE AV OPPSTARTSSKJERM
knips fakturaoversikt "$BILDEKATALOG";

# Velg første faktura
xte 'key Tab' 'key Tab' 'key space' 'key Menu';
knips fakturadetaljer "$BILDEKATALOG";

# Skriv ut epostfaktura
alt o;
knips epostfaktura "$BILDEKATALOG";

# KJØR TESTENE:

bilde nyfaktura n "$BILDEKATALOG";

bilde kundeoversikt k "$BILDEKATALOG";

bilde nykunde n "$BILDEKATALOG";

bilde vareoversikt v "$BILDEKATALOG";

bilde nyvare n "$BILDEKATALOG";

bilde firmainfo d "$BILDEKATALOG";

bilde epost e "$BILDEKATALOG";


bilde sikkerhetskopier s "$BILDEKATALOG";




# AVSLUTT PROGRAMMET
pkill faktura.py
