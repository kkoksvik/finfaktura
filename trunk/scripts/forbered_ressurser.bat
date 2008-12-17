@ECHO OFF
SET RESSURSER="faktura.qrc"
SET UIDIR="..\finfaktura\ui"
SET UIFILER="epost.ui faktura.ui finfaktura_oppsett.ui firmainfo.ui sendepost.ui"

ECHO Kompilerer ressurser...
REM FOR %A IN (list) DO command [ parameters ]
REM FOR %? IN (%RESSURSER%) DO ECHO pyrcc4 -o %UIDIR%\faktura_rc.py %?
pyrcc4 -o %UIDIR%\faktura_rc.py ..\faktura.qrc

ECHO Kompilerer grensesnitt...
REM FOR %? IN (%UIFILER%) DO ECHO %? 
pyuic4 -o %UIDIR%\epost_ui.py %UIDIR%\epost.ui
pyuic4 -o %UIDIR%\faktura_ui.py %UIDIR%\faktura.ui
pyuic4 -o %UIDIR%\finfaktura_oppsett_ui.py %UIDIR%\finfaktura_oppsett.ui
pyuic4 -o %UIDIR%\firmainfo_ui.py %UIDIR%\firmainfo.ui
pyuic4 -o %UIDIR%\sendepost_ui.py %UIDIR%\sendepost.ui

