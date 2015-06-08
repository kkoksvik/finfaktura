## Enkel fakturering ##

_Fryktelig Fin Faktura_ er et fakturaprogram for norske forhold. Fakturaene lages på PDF eller skjema F60.

Det er **fritt, åpent og gratis**, og laget for linux og windows (mac-versjon kommer!).

## Mai 2009: 2.0.6b for Ubuntu ##

Ubuntu 9.04 og fremtidige Debian-systemer har lagt om måten python-moduler skal installeres. Derfor har jeg lastet opp en ny .deb-pakke, som skal løse installasjonsproblemer på disse systemene.

Last ned her: [finfaktura\_2.0.6b\_all.deb](http://finfaktura.googlecode.com/files/finfaktura_2.0.6b_all.deb)


## April 2009: ny versjon 2.0.6 ##

Litt vårrengjøring førte til en ny bugfiks-versjon. Last ned fra lista til høyre.

![http://finfaktura.googlecode.com/svn/screenshots/finfaktura2-screenie-liten.png](http://finfaktura.googlecode.com/svn/screenshots/finfaktura2-screenie-liten.png)

_Slik ser Finfaktura2 ut_

[Flere bilder av programmet](SlikSerDetUt.md)

## Mars 2009: ny installer for windows ##

Jeg har laget et nytt installasjonsprogram for windows. Det passer **både for oppgraderinger og ny-installasjoner**. Dermed blir det _mindre å laste ned_.

Last ned her: [finfaktura-2.0.6-netinstaller.exe](http://finfaktura.googlecode.com/files/finfaktura-2.0.6-netinstaller.exe)

### Oppgradering ###

Oppgi stien til din eksisterende finfakturainstallasjon, så vil programmet oppgradere de nødvendige filene og intet annet.

### Ny-installasjon ###

Programmet merker at finfaktura ikke er installert fra før, og laster ned de nødvendige filene fra nettet. Det betyr at du **må ha kontakt med internett under installeringen**.



## Mars 2009: bugfiks-versjon 2.0.5 ##

Nå er alle BBS' krav til blanketten er oppfylt. Kontonummer som begynner på 0 kan brukes. Alle endringer:

  * f60.py: massive forbedringer av blanketten (stor takk til cbrattli), se [issue#38](https://code.google.com/p/finfaktura/issues/detail?id=#38)
  * f60.py: skriver beløp i kroner og med kommaskilletegn
  * f60.py: Fiks i mod10-algoritme, og inn med mod11 (KID) - igjen, takk til cbrattli.
  * f60.py: Spesifisert momsgrunnlag
  * fiks utskrift av kontonummer som starter på 0 ([issue#47](https://code.google.com/p/finfaktura/issues/detail?id=#47) igjen)
  * Laster logoer på en annen måte (forhåpentlig løser dette [issue#48](https://code.google.com/p/finfaktura/issues/detail?id=#48))

Mac-versjonen vil ta fortsatt noe tid (beklager!)

## Januar 2009: bugfiks-versjon 2.0.1 ##

Tre viktige fikser tvang frem en ny versjon.

  * Fikser feil som inntrer når ny faktura skal lages, og noe av informasjonen om firmaet mangler ([issue#45](https://code.google.com/p/finfaktura/issues/detail?id=#45)) -- takk, Audun!
  * Fikser feil som gir alle fakturaer dagens dato
  * Fikser feil på windows når brukernavnet inneholder æøå (ikke-ascii tegn)

## Desember 2008: stabil versjon 2.0 ##

Etter et halvt års utvikling er programmet endelig stabilt nok til versjon 2.0.

Programmet har fått en ansiktsløfting ([issue#3](https://code.google.com/p/finfaktura/issues/detail?id=#3)), og har også fått noe ny funksjonalitet. Fra [endringsloggen](http://code.google.com/p/finfaktura/source/browse/trunk/debian/changelog):

  * Fikser rapport.py: utskrift av pdf og rapport fra firma med '&' i firmanavnet ([issue#43](https://code.google.com/p/finfaktura/issues/detail?id=#43)) -- takk, Eivind!
  * Fikser scrollelinjer dersom skjermen/vinduet er mindre enn informasjonen som skal vises -- takk, Johan!
  * Bedre installasjon på Debian/Ubuntu
  * Fikser vising av PDF på windows
  * Logoer og dokumenter installeres
  * Grensesnittet er portert til PyQt4 ([issue#3](https://code.google.com/p/finfaktura/issues/detail?id=#3)) og redesignet
  * Det går an å føre halve antall av varer (f.eks. timer) ([issue#22](https://code.google.com/p/finfaktura/issues/detail?id=#22))
  * Kan sette vilkårlig forfallsdato på ny faktura ([issue#25](https://code.google.com/p/finfaktura/issues/detail?id=#25))


(Programmet behøver nå [minimum PyQt4.4](http://www.riverbankcomputing.co.uk/software/pyqt/download))

## Innspill ##

Hvis du savner noe i programmet, [legg det til i arbeidslista](http://code.google.com/p/finfaktura/issues/list)!