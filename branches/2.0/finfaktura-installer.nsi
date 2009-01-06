;Finfaktura installer
;By havard@gulldahl.no
;
; Based on
;  "Start Menu Folder Selection Example Script"
;  Written by Joost Verburg

;--------------------------------
;Include Modern UI

  !include "MUI2.nsh"


;--------------------------------
; uninstaller stuff from
;   http://nsis.sourceforge.net/Uninstall_only_installed_files
;

!define UninstLog "uninstall.log"
Var UninstLog
 
; Uninstall log file missing.
LangString UninstLogMissing ${LANG_ENGLISH} "${UninstLog} not found!$\r$\nUninstallation cannot proceed!"
 
; AddItem macro
!macro AddItem Path
 FileWrite $UninstLog "${Path}$\r$\n"
!macroend
!define AddItem "!insertmacro AddItem"
 
; File macro
!macro File FilePath FileName
 IfFileExists "$OUTDIR\${FileName}" +2
  FileWrite $UninstLog "$OUTDIR\${FileName}$\r$\n"
 File "${FilePath}${FileName}"
!macroend
!define File "!insertmacro File"
 
; Copy files macro
!macro CopyFiles SourcePath DestPath
 IfFileExists "${DestPath}" +2
  FileWrite $UninstLog "${DestPath}$\r$\n"
 CopyFiles "${SourcePath}" "${DestPath}"
!macroend
!define CopyFiles "!insertmacro CopyFiles"
 
; Rename macro
!macro Rename SourcePath DestPath
 IfFileExists "${DestPath}" +2
  FileWrite $UninstLog "${DestPath}$\r$\n"
 Rename "${SourcePath}" "${DestPath}"
!macroend
!define Rename "!insertmacro Rename"
 
; CreateDirectory macro
!macro CreateDirectory Path
 CreateDirectory "${Path}"
 FileWrite $UninstLog "${Path}$\r$\n"
!macroend
!define CreateDirectory "!insertmacro CreateDirectory"
 
; SetOutPath macro
!macro SetOutPath Path
 SetOutPath "${Path}"
 FileWrite $UninstLog "${Path}$\r$\n"
!macroend
!define SetOutPath "!insertmacro SetOutPath"
 
; WriteUninstaller macro
!macro WriteUninstaller Path
 WriteUninstaller "${Path}"
 FileWrite $UninstLog "${Path}$\r$\n"
!macroend
!define WriteUninstaller "!insertmacro WriteUninstaller"
 
Section -openlogfile
 CreateDirectory "$INSTDIR"
 IfFileExists "$INSTDIR\${UninstLog}" +3
  FileOpen $UninstLog "$INSTDIR\${UninstLog}" w
 Goto +4
  SetFileAttributes "$INSTDIR\${UninstLog}" NORMAL
  FileOpen $UninstLog "$INSTDIR\${UninstLog}" a
  FileSeek $UninstLog 0 END
SectionEnd

;--------------------------------
;General

  ;Name and file
  Name "Fryktelig Fin Faktura"
  OutFile "dist\finfaktura-install.exe"

  ;Default installation folder
  InstallDir "$PROGRAMFILES\Fryktelig Fin Faktura"
  
  ;Get installation folder from registry if available
  InstallDirRegKey HKCU "Software\Fryktelig Fin Faktura" ""

  ;Request application privileges for Windows Vista
  RequestExecutionLevel user

  SetCompressor /SOLID /FINAL zlib

;--------------------------------
;Variables

  Var StartMenuFolder

;--------------------------------
;Interface Settings

  !define MUI_ABORTWARNING

;--------------------------------
;Pages

  !insertmacro MUI_PAGE_LICENSE "LICENSE" ;; lisens-fil
  ;!insertmacro MUI_PAGE_COMPONENTS
  !insertmacro MUI_PAGE_DIRECTORY
  
  ;Start Menu Folder Page Configuration
  !define MUI_STARTMENUPAGE_REGISTRY_ROOT "HKCU" 
  !define MUI_STARTMENUPAGE_REGISTRY_KEY "Software\Fryktelig Fin Faktura" 
  !define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "Start Menu Folder"
  
  !insertmacro MUI_PAGE_STARTMENU Application $StartMenuFolder
  
  !insertmacro MUI_PAGE_INSTFILES
  
  !insertmacro MUI_UNPAGE_CONFIRM
  !insertmacro MUI_UNPAGE_INSTFILES

;--------------------------------
;Languages
 
  !insertmacro MUI_LANGUAGE "English"

;--------------------------------
;Installer Sections

Section "Installere Fryktelig Fin Faktura" SecInstall

  ${SetOutPath} "$INSTDIR"
  
  ;ADD YOUR OWN FILES HERE...
  ${File} "dist\" "_elementtree.pyd"
  ${File} "dist\" "_hashlib.pyd"
  ${File} "dist\" "_rl_accel.pyd"
  ${File} "dist\" "_socket.pyd"
  ${File} "dist\" "_sqlite3.pyd"
  ${File} "dist\" "_ssl.pyd"
  ${File} "dist\" "bz2.pyd"
  ${File} "dist\" "faktura.exe"
  ${File} "dist\" "library.zip"
  ${File} "dist\" "mingwm10.dll"
  ${File} "dist\" "PyQt4.QtCore.pyd"
  ${File} "dist\" "PyQt4.QtGui.pyd"
  ${File} "dist\" "python25.dll"
  ${File} "dist\" "QtCore4.dll"
  ${File} "dist\" "QtGui4.dll"
  ${File} "dist\" "select.pyd"
  ${File} "dist\" "sgmlop.pyd"
  ${File} "dist\" "sip.pyd"
  ${File} "dist\" "sqlite3.dll"
  ${File} "dist\" "unicodedata.pyd"
  ${File} "dist\" "w9xpopen.exe"
  
  ;Store installation folder
  WriteRegStr HKCU "Software\Fryktelig Fin Faktura" "" $INSTDIR
  
  ;Create uninstaller
  ${WriteUninstaller} "$INSTDIR\finfaktura-uninstall.exe"
  
  !insertmacro MUI_STARTMENU_WRITE_BEGIN Application
    
    ;Create shortcuts
    CreateDirectory "$SMPROGRAMS\$StartMenuFolder"
    CreateShortCut "$SMPROGRAMS\$StartMenuFolder\Uninstall.lnk" "$INSTDIR\finfaktura-uninstall.exe"
    CreateShortCut "$SMPROGRAMS\$StartMenuFolder\Fryktelig Fin Faktura.lnk" "$INSTDIR\faktura.exe"
  
  !insertmacro MUI_STARTMENU_WRITE_END

SectionEnd

;--------------------------------
;Descriptions

  ;Language strings
  LangString DESC_SecInstall ${LANG_ENGLISH} "Installere Fryktelig Fin Faktura"

  ;Assign language strings to sections
  !insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
    !insertmacro MUI_DESCRIPTION_TEXT ${SecInstall} $(DESC_SecInstall)
  !insertmacro MUI_FUNCTION_DESCRIPTION_END
 
;--------------------------------
;Uninstaller Section

Section -closelogfile
   FileClose $UninstLog
   SetFileAttributes "$INSTDIR\${UninstLog}" READONLY|SYSTEM|HIDDEN
SectionEnd
   
Section Uninstall
   
   ; Can't uninstall if uninstall log is missing!
   IfFileExists "$INSTDIR\${UninstLog}" +3
    MessageBox MB_OK|MB_ICONSTOP "$(UninstLogMissing)"
     Abort
   
   Push $R0
   Push $R1
   Push $R2
   SetFileAttributes "$INSTDIR\${UninstLog}" NORMAL
   FileOpen $UninstLog "$INSTDIR\${UninstLog}" r
   StrCpy $R1 0
   
   GetLineCount:
    ClearErrors
     FileRead $UninstLog $R0
     IntOp $R1 $R1 + 1
     IfErrors 0 GetLineCount
   
   LoopRead:
    FileSeek $UninstLog 0 SET
    StrCpy $R2 0
    FindLine:
     FileRead $UninstLog $R0
     IntOp $R2 $R2 + 1
     StrCmp $R1 $R2 0 FindLine
   
     StrCpy $R0 $R0 -2
     IfFileExists "$R0\*.*" 0 +3
      RMDir $R0  #is dir
     Goto +3
     IfFileExists $R0 0 +2
      Delete $R0 #is file
   
    IntOp $R1 $R1 - 1
    StrCmp $R1 0 LoopDone
    Goto LoopRead
   LoopDone:
   FileClose $UninstLog
   Delete "$INSTDIR\${UninstLog}"
   RMDir "$INSTDIR"
   Pop $R2
   Pop $R1
   Pop $R0
  
  !insertmacro MUI_STARTMENU_GETFOLDER Application $StartMenuFolder
    
  Delete "$SMPROGRAMS\$StartMenuFolder\Uninstall.lnk"
  Delete "$SMPROGRAMS\$StartMenuFolder\Fryktelig Fin Faktura.lnk"
  RMDir "$SMPROGRAMS\$StartMenuFolder"
  
  DeleteRegKey /ifempty HKCU "Software\Fryktelig Fin Faktura"

SectionEnd


