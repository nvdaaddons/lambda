# Lambda #

* Tekijä: Alberto Zanella ja Lambda-NVDA-tiimi
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]

Tämä lisäosa sisältää sovellusmoduulin LAMBDA-ohjelmistoa varten. Se on saanut innoituksensa Peter Leckyn työstä Comenius Universityssä. 
LAMBDA (Linear Access to Mathematic for Braille Device and Audio-synthesis) on ohjelmisto, joka auttaa sokeita lukemaan ja kirjoittamaan matemaattista sisältöä pistenäyttöä ja/tai puhesyntetisaattoria käyttäen.
LAMBDA on EU-hankkeen tulos. Lisätietoja löytyy osoitteesta [https://www.lambdaproject.org/](https://www.lambdaproject.org/).  
Lisäosan nykyinen versio sisältää italialaisen ja espanjalaisen
pistetaulukon, ja sen käyttöliittymä on saatavana useimmilla NVDA:n
tukemista kielistä.  Mikäli et ole italialainen LAMBDA-käyttäjä ja haluaisit
osallistua kielialueesi pistetaulukon sovittamiseen, ota yhteyttä tekijään
(katso alta) tai liity projektin postituslistalle.

**Huomaa:** Tämän lisäosan on kehittänyt Alberto Zanella vapaaehtoistoimintana. Tekijä tai projektiin osallistuneet eivät myy LAMBDA-ohjelmistoa tai ole mukana sen kehityksessä. Jos tarvitset lisätietoja tai tukea ohjelmiston käytössä, ota yhteyttä paikalliseen jälleenmyyjääsi. Mikäli sinulla on vaikeuksia tämän lisäosan käytössä tai asentamisessa, ota yhteyttä tekijään tai käytä "Issues"-linkkiä GitHub-projektisivulla.

### [Virallinen GitHub-koodivarasto](https://github.com/lambda-nvda/lambdaNvda/)

## Lisäosan ominaisuudet:

### Puhetuki:

* Valintaikkunat ja valikot luetaan asianmukaisesti;
* Luonnollinen puhetuki matemaattisille kaavoille
  Lambda-matematiikkamoottoria käyttäen, esim. "yhdysjuuri 3 jaettuna
  yhdysjuuri 3 x plus 24, yhdysjuuri loppuu, miinus 3 on yhtä kuin 0".
* Toteutettu merkeittäin, sanoittain ja riveittäin lukeminen sekä jatkuva
  luku.
* Puhuu tekstilohkon valitsemisen tai valinnan laajentamisen (Ctrl+B- ja
  Ctrl+Vaihto+B-komentoja käyttäen).
* Puhuu, kun  tekstieditorissa liikutaan Windowsin tavallisia ja Lambdan
  omia komentoja käyttäen.
* Sekä laajennettua että lyhyttä puhetilaa tuetaan (tila valitaan Lambdan
  Työkalut-valikosta).
* Erikoisvalintaikkunat, kuten rakennetila-, laskin- ja matriisi-ikkuna,
  puhutaan nyt oikein, ja NVDA lukee asianmukaisesti, kun kohdistinta
  siirretään tai uutta tekstiä kirjoitetaan.
* Merkkien kaiutus käyttää Lambdan tekstiprosessoria, joten symbolit ja
  merkit puhutaan oikein.

### Pistekirjoituksen tuki:

* Lisäosa asentaa käyttäjäprofiilihakemistoon mukautetun pistetaulukon ja
  ottaa sen käyttöön. Tämä taulukko voi olla erilainen eri
  kielillä. Mukautetut pistetaulukot on tehty JAWSin Lambda-laajennuksen
  mukana toimitettujen jbt-tiedostojen pohjalta. Tämän ansiosta symbolit ja
  merkit esitetään samoilla pistekuvioilla.
* Lisäosa luo NVDA:n asetusprofiilin vakiopistekirjoitusasetuksia
  varten. Tällä tavoin mukautettu pistetaulukko otetaan käyttöön
  tulostustaulukkona vain, kun Lambda-sovellus on aktiivisena.
* Valintaikkunat ja valikot näytetään oikein pistekirjoituksella.
* Editorin sisältö hahmonnetaan oikein pistekirjoituksella, ja käyttäjä voi
  liikkua pistenäytön vieritys- tai kohdistimensiirtonäppäimillä.
* Lisäosan versiosta 1.1.0 alkaen Lambda-editorissa oleva teksti
  hahmonnetaan kahdella tavalla: "tasatussa tilassa" ja "ei-tasatussa
  tilassa". Kun "tasattu tila" on käytössä, NVDA käyttää näyttömallia
  tietojen hakemiseen editorista ja kohdistimen sijainnin
  määrittämiseen. Tämä on erityisen hyödyllistä silloin, kun käyttäjän
  täytyy liikkua näytöllä, jopa tyhjässä tilassa. Kun "tasattu tila" ei ole
  käytössä, tekstin hahmonnus pistenäytöllä on vakaampaa, koska NVDA käyttää
  Windowsin rajapintaa sen hakemiseen. Kuitenkin, kun kohdistinta siirretään
  tyhjässä tilassa tekstirivin lopun vieressä, pistenäyttö ei seuraa oikeaa
  kohdistinta niin kauan kuin käyttäjä on lisännyt jonkin muun kuin
  tyhjätilamerkin.

"Tasattu tila" on oletusarvoisesti käytössä. Voit ottaa sen käyttöön tai
poistaa käytöstä painamalla NVDA+Vaihto+F.

Suosittelemme poistamaan tasatun tilan käytöstä, jos käytät Windowsissa
mukautettua DPI:tä (mukautettu kokovaihtoehto), varsinkin jos näytön
asetuksissa on valittuna kooksi yli 96 DPI (suurempi kuin 100 %).

* Valintaikkunoiden rakenne on helpompi; toistuva tieto on poistettu.
* Valinta merkitään oikein pisteitä 7 ja 8 käyttäen, ja merkintä päivitetään
  oikein, kun tavallisia Windows-komentoja (Vaihto+Nuolinäppäimet) tai
  Lambda-komentoja (Ctrl+B, Ctrl+Vaihto+B) painetaan.

## Ennen kuin aloitat tämän lisäosan käytön:

This addon creates an NVDA profile named "lambda" which is associated with
the "lambda.exe" application. The profile automatically sets all braille
options: the custom braille table, the focus tethering and flat mode
settings.

If a previous profile with the same name is present in your system, the
addon will not override it and you have to manually adjust your
configuration profile.

To stave off this situation, if you have specific settings you'd like to
preserve, you can use the "Revert LAMBDA Profile Wizard". The shortcut to
start this tool is NVDA+alt+r (when focused in LAMBDA).

An easy option is also to delete old versions of the "lambda" profile after
the installation of the addon. To do so, open the NVDA menu, select the
"Configuration profiles" menu Item and press ENTER.

In the Configuration profiles dialog, you'll be able to locate and delete
the "lambda" profile. The profile will be re-created the next time the
Lambda application is started.

Deleting the "lambda" profile should be an easy solution also when the addon
runs into any problem. For instance, if the braille table is not properly
set, instead of manually configuring the profile, you can simply delete
it. The addon will create a new one the next time you'll load the Lambda
editor.

Each time the Lambda editor is started, this addon checks if a profile with
the name "lambda" exists. If it doesn't, it automatically generates a
profile with the following form:

```
filename : userData\profiles\lambda.ini :

[braille]
	readByParagraph = False
	tetherTo = focus
	translationTable = path-to-the-addon-brailleTable-dir\tableName

[lambda]
	brailleFlatMode = True

```

Where :

* path-to-the-addon-brailleTable-dir : is the absolute path of the addon
  directory + "\brailleTables"
* tableName : depends on the active NVDA language. Currently only the
  italian and Spanish braille tables, "lambda-ita.utb" and "lambda-esp.utb"
  respectively, is present.

## Addon Keyboard Shortcuts:

* **NVDA+Shift+f**: Toggle braille flat mode on or off;
* **NVDA+alt+r**: Open the "Revert LAMBDA Profile Wizard";
* **NVDA+d**: Duplicate lines (use this instad of control+d).

## Known issues:

Due to a bug present in LAMBDA, the add-on provides an extra-logic that
reports white spaces. This logic may fail in the following situations:

* When words like "space", "spazio" "Espacio" etc. are inserted into the
  text, they may be reported by NVDA as the local NVDA language translation.
* Blank lines are not reported by the LAMBDA speech engine. The user will
  hear the translation of the word "space" instead. This could be both a
  blank line or a line containing only the word "space".

## Useful tips

This is a set of tips that will help you on using the addon in a more
eficient way.

* Character-by-character reporting: Normally, when working with maths you
  would like NVDA to report things you're writing character by character. To
  do this, there are a couple of simple steps: ensure to have the focus on
  the LAMBDA's window or one of its variants (the six dots representation,
  for example); press NVDA+2 (number two) or navigate to NVDA
  menu>Preferences>Keyboard settings and check the box to Speak typed
  characters; go to LAMBDA>Options>Voice paramethers and ensure the checkbox
  "echo" is ON, otherwhise NVDA won't receive anything from the speech
  engine while you are typing. And done, NVDA will speak written characters,
  but don't worry, only in LAMBDA or its special windows, the settings for
  the rest of applications will be left as they were.

## Addon mailing list:

To report bugs, suggestions or if you want to contribute you can subscribe
the Addon Group (in English).  You can subscribe from the website:
<https://groups.io/g/lambda-nvda>.

## Change log

Below is a list of changes between the different add-on versions. Next to
the version number, between parentheses, is the development status. The
current development release isn't included as it could have changes until it
is flagged as stable or discarded as candidate.

### Version 1.3.0 (stable)

* Support for newer version of NVDA (Support for Python 3)
* Solved an issue while pressing duplicate line command NVDA+d in a blank
  line caused clipboard content to be pasted. Now when you press NVDA+d and
  you are in a blank line, a new blank line appears as expected.

### Version 1.2.2 (stable)

* Improved compatibility with WX Python version 4 (introduced with NVDA
  2018.3). Warning related with wx.NewId() is no longer displayed in debug
  log.
* Implemented guiHelper to enhance dialogs's appearance.
* New languages. Updated translations.

### Version 1.2.1a (stable)

This update is intended to be a long-term support release. It means that
until, at least, june 2018, it won't be released a version as stable as
this. We do it to provide students maximum stability and to minimize the
changes during the academical year.

* New languages. Updated translations.

### Version 1.2.1 (stable)

* Added compatibility with the way that NVDA 2017.3 uses to manage
  braille. Backwards compatibility kept.
* fixed many braille issues.

### Version 1.2.0 (development)

This version was not published as stable because the version 1.2.1 included
major fixes.

* New locales. Updated localizations.

### Version 1.1.8 (stable)

* Initial stable release.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=lambda

[2]: https://addons.nvda-project.org/files/get.php?file=lambda-dev
