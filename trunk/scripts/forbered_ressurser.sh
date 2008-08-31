#!/bin/bash
# Oppdaterer alle .ui og .qrc-filer

echo "Forbereder GUI (grafisk grensesnitt)";
for f in finfaktura/ui/*.ui;
do
  F=$(basename "$f" .ui);
  echo ".. $F.ui";
  pyuic4 -o "finfaktura/ui/$F" "$f";
done

echo "Forbereder QRC (ressurser)";
echo ".. faktura.qrc";
pyrcc4 -o "finfaktura/ui/faktura_rc.py" faktura.qrc;

