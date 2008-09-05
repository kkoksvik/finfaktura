#!/bin/bash
# Oppdaterer alle .ui og .qrc-filer

echo "Forbereder GUI (grafisk grensesnitt)";
for f in finfaktura/ui/*.ui;
do
  F=$(basename "$f" .ui);
  echo ".. $F.ui";
#   echo pyuic4 -o "finfaktura/ui/${F}_ui.py" "$f";
  pyuic4 -o "finfaktura/ui/${F}_ui.py" "$f";
done

echo "Forbereder QRC (ressurser)";
echo ".. faktura.qrc";
pyrcc4 -o "faktura_rc.py" faktura.qrc;

