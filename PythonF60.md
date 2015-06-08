# Innledning #

F60.py er en **python-modul** for å produsere en **faktura i PDF-format**. Dokumentet er laget til å samsvare med _Norsk standard Giro F60_, og kan skrives ut på slike blanketter.

F60.py brukes av [finfaktura](SlikSerDetUt.md), men kan også brukes uavhengig, i ditt eget python-program. I det følgende vises hvordan.

Vil du bruke F60.py for seg selv, kan du laste modulen ned fra [nedlastingslista](http://code.google.com/p/finfaktura/downloads/list).

F60.py bruker [reportlab til å lage PDF-filer](http://www.reportlab.org/downloads.html). Denne pakken må du installere (den heter python-reportlab i linux).



# Eksempel #

```

import f60
filnavn = '/tmp/testfaktura.pdf'
faktura = f60(filnavn, overskriv=True)
faktura.settKundeinfo(06, "Topert\nRopertgata 33\n9022 Nissedal")
faktura.settFakturainfo(
  fakturanr=03,
  utstedtEpoch=1145542709,
  forfallEpoch=1146546709,
  fakturatekst=u"Produksjon i august",
  vilkaar=u"Takk for handelen, kom gjerne igjen.",
  kid=True)
faktura.settFirmainfo({'firmanavn':'Firma Ein',
                        'kontaktperson':'Rattatta Hansen',
                        'adresse':u'Surdalsøyra',
                        'postnummer':8999,
                        'poststed':u'Fløya',
                        'kontonummer':99999999999,
                        'organisasjonsnummer':876876,
                        'telefon':23233322,
                        'epost':'ratata@ta.no'})
faktura.settOrdrelinje([ ["Leder", 1, 300, 25], ['Reportasje', 1, 3000, 25], ])
if faktura.lagEpost():
    print "Kvittering laget i", filnavn
```

Gir følgende faktura:

![http://finfaktura.googlecode.com/svn/screenshots/f60-0.10.png](http://finfaktura.googlecode.com/svn/screenshots/f60-0.10.png)



# Informasjon om fakturaen #

## Fakturainfo ##

## Firmainfo ##

## Kundeinfo ##

## Ordrelinje ##

## Logo ##

**Metode:** `.settLogo(logo)`

Du kan sette inn en firmalogo med metoden `.settLogo(logo)`. Argumentet **logo** er 1) _et filnavn_, 2) _bildedata_ eller 3) _et [PIL-objekt](http://www.pythonware.com/products/pil/)_.

Dersom bildefila eller bildedata ikke er i [JPEG-format](http://en.wikipedia.org/wiki/JPEG), må [PIL](http://www.pythonware.com/products/pil/) være installert.

Logoen blir installert oppe i venstre hjørne av fakturaen, **med maks-størrelse 25\*25 mm!** Er bildet større, blir det nedskalert. _Det er likevel lurest å skalere logoen selv, siden det ofte gir bedre resultater._

## KID ##

  * **Metode:** `.lagKid()`
  * **Metode:** `.sjekkKid()`
  * **Metode:** `.lagKontrollsifferMod10()`
  * **Metode:** `.lagKontrollsifferMod11()`

f60 kan generere, kontrollere og sette [KID](http://no.wikipedia.org/wiki/KID). `.lagKid()` setter sammen en KID av _kundenummer_ + _fakturanummer_ + _kontrollsiffer_.

Kontrollsifferet skal regnes ut etter _mod10_ eller _mod11_-algoritmen, slik BBS Nordic oppgir den i _Kravspek for OCR_. I f60.py **brukes som standard mod10**.

Se detaljer i [issue#38](https://code.google.com/p/finfaktura/issues/detail?id=#38).

### Sett kundeinfo først ###

Siden f60 bruker kundenummer for å generere KID, må du huske å sette kundeinfoen (`.settKundeinfo()`) **før** du setter fakturainfoen dersom du skal autogenerere KID.

## Datoformat ##

**Metode:** `.settDatoformat(format)`

Standard datoformat er `%Y-%m-%d`, for eksempel **2009-01-31**. Du kan oppgi ditt eget datoformat.

Lista over [gyldige formatteringskoder finner du på python.org](http://www.python.org/doc/2.5.2/lib/module-time.html#l2h-2826).

# Format #

Fakturaene produseres i filformatet [PDF](http://en.wikipedia.org/wiki/PDF) gjennom [hjelpebiblioteket reportlab](http://www.reportlab.org/downloads.html). [Last ned en åpen pdf-leser](http://pdfreaders.org/index.nb.html).

Videre kan fakturaene få **ulike layout**, avhengig av **hvordan de skal sendes**.

## Epost ##

**Metode:** `.lagEpost()`

Her imiteres en ferdig utfylt giroblankett, altså en digital kopi av et skjema F60-1 med gule felter, og betalingsinformasjon.

**Vær obs på at det _ikke er lov_ å skrive denne ut til papir. Du _må_ skrive ut på en trykket blankett!** Da bruker du `.lagPost()` -- se neste punkt.

## Papir/Utskrift ##

**Metode:** `.lagPost()`

Dette valget gir en PDF-fil som egner seg for **utskrift på et skjema F60-1**, altså bare betalingsinformasjonen.

## Kvittering ##

**Metode:** `.lagKvittering()`

Dette er en spesiell versjon av den imiterte giroblanketten, hvor påskriften "KVITTERING" er trykket på tvers over arket. **Dette er den kopien av fordringen du skal beholde.**

Hensikten med denne layouten er å unngå sammenblanding dersom du velger å skrive ut kvitteringen.