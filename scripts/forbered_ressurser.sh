#!/bin/bash
# Oppdaterer alle .ui og .qrc-filer

PREFIX="$1";

echo "Forbereder GUI (grafisk grensesnitt)";
for f in finfaktura/ui/*.ui;
do
  F=$(basename "$f" .ui);
  echo ".. $F.ui";
#   echo pyuic4 -o "${PREFIX}finfaktura/ui/${F}_ui.py" "$f";
  pyuic4 -o "${PREFIX}finfaktura/ui/${F}_ui.py" "$f";
done

echo "Forbereder QRC (ressurser)";
echo ".. faktura.qrc";
pyrcc4 -o "${PREFIX}faktura_rc.py" faktura.qrc;

