#!/bin/bash
# Oppdaterer alle .ui og .qrc-filer

for f in finfaktura/ui/*.ui;
do
  F=$(basename "$f" .ui);
  pyuic4 -o "finfaktura/ui/$F" "$f";
done

pyrcc4 -o "finfaktura/ui/faktura_rc.py" faktura.qrc;

