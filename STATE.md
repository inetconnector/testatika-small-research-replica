# STATE.md — Testatika / Thesta-Distatica
## Korpusbasierte technische Wissensbasis, Quellenkritik und Rekonstruktionsstand

**Version:** 5.0 — Marinov Part V Primäranalyse / historische Influenzmaschinen / quellenkritische Neugewichtung  
**Stand:** 2026-08-16  
**Aktuelle Ergänzung:** 6.0 — Hartmann / Overunity.com Quellen- und Hypothesenaudit; Version-5-Inhalt bleibt vollständig erhalten.  
**Arbeitsstatus:** Archiv vollständig inventarisiert; Textdokumente extrahiert, technische Bildquellen und Video-Stichproben visuell geprüft; Widersprüche und Replikationsergebnisse integriert. Version 5.0 ergänzt eine systematische Primäranalyse von Stefan Marinovs vollständigem Band *The Thorny Way of Truth, Part V* (1989), einschließlich der technischen Testatika-Seiten, der von Marinov nachgedruckten historischen Influenzmaschinenliteratur, der Testatika-Korrespondenz und späterer Korrekturbriefe. Frühere V4-Hypothesen bleiben dokumentiert, werden aber dort ausdrücklich herabgestuft, wo Marinovs direkte Beobachtungen oder die historische Messtechnik dagegen sprechen.  
**Hauptarchiv:** `testatika.zip`  
**SHA-256 des Hauptarchivs:** `9a78f965651232b986ba38fdc671c5831205641763861b566e457ec423a3c14c`  
**Archivumfang:** 179 Dateien im Hauptarchiv, zusätzlich 35 Dateien in `assembly pics.zip` und 2 Dateien in `Replications.zip`; die verschachtelten Archive bestehen fast vollständig aus Duplikaten bereits vorhandener Dateien.  
**Zusätzliche Quellen außerhalb des ZIP:** 10 vom Nutzer fotografierte Buchseiten (`1000076410.jpg` … `1000076420.jpg`, mit Lücken in der Nummerierung) zu Testatika, Hauser und Hyde-Generator.

**Version-4.0-Kernänderungen:**  
- Pos. 6 erstmals als explizites Dreigitter-Kapazitätsnetzwerk formalisiert;  
- Pos. 9/10/12 nach Primär-, Gegen- und Rekonstruktionsquellen neu gewichtet;  
- Home-Video-Dialog als separate, übersetzungsunsichere Betreiberquelle ausgewertet;  
- mechanische kW-Plausibilität über Drehmoment und Rotationsenergie quantifiziert;  
- kurze Lampen-/Heizer-Demonstrationen energetisch neu eingeordnet;  
- Linden-Messblatt 770/580 V metrologisch neu bewertet;  
- Segmentwiderstands-Hypothese aus Report D als testbare, aber sekundäre Spur aufgenommen;  
- Zwei-Zeitskalen-Modell (langsame mechanische Kommutation + schnelles elektrisches Ringing) ergänzt;  
- vollständiges, ergebnisorientiertes Hypothesenprotokoll H01–H25 angelegt;  
- priorisierter Falsifikations-/Messplan für die offenen Kernblöcke ergänzt.

**Version-5.0-Kernänderungen:**  
- vollständiger externer Primär-/Quellenband `The Thorny Way of Truth, Part V` (Stefan Marinov, 1989) als eigenständige Quelle erschlossen;  
- Marinovs **direkte Beobachtung**, seine **eigene Hypothese**, Baumanns **mündliche Aussagen**, Hausers **Korrespondenz** und spätere **Drittquellen** strikt getrennt;  
- ursprüngliche kleine Testatika als wesentlich einfachere Referenzklasse aufgewertet: eine Scheibe, etwa 20–30 radiale Kupferdrähte, keine zwingenden Magnete/Teslaspulen;  
- 50/60-Hz-Hypothese deutlich herabgestuft: Marinov bezeichnet die Europe/USA-Segmentdeutung ausdrücklich als nicht sinnvoll und verweist auf DC-Ausgang;  
- absichtliches internes HF-/Tesla-System deutlich herabgestuft: Marinov sah geöffnete große Seitenkondensatoren und beschreibt sie als Kondensatoren mit äußerem Zylinder und innerer dicker Kupferspiral-Elektrode;  
- `crystal`-Bauteil als möglicher **einseitiger Ladungspfad / charge valve** höher gewichtet;  
- Marinovs Zwei-Kreis-Hypothese (HV-Driving-Elektroden / niedrigere Spannung an Collecting-Elektroden) als wichtige, aber explizit spekulative Topologie aufgenommen;  
- Marinovs „große Kondensatoren“-Erklärung elektromechanisch geprüft und als **nicht ausreichende Erklärung eines Energieüberschusses** bewertet;  
- Wommelsdorf-/Schmidt-Messdaten aus demselben Band als historische Gegenkontrolle integriert: klassische Kondensator-Influenzmaschinen zeigen messbare mechanische Eingangsleistung und Wirkungsgrade klar unter 100 %;  
- Marinovs eigener 25-kV-Elektrostatikmotor-Versuch metrologisch neu bewertet; sein Faktor 13,3 ist kein belastbarer COP-Nachweis;  
- Metallplatten-Stoppversuch und Feuchtigkeitsabhängigkeit als starke Hinweise auf Feldrandbedingungen/Korona/Kapazität zur Umgebung eingeordnet;  
- Testatika-relevante spätere Korrespondenz bis zum Epilog analysiert, einschließlich Marinovs eigener Korrektur: **keine Tesla-Transformatoren, kein AC, Maschine extrem einfach, Geheimnis unbekannt**;  
- V5-Hypothesenprotokoll und neuer Arbeitskonsens erstellt.

---

## 0. Zweck und wichtigste methodische Regel

Diese Datei soll nicht eine einzelne Theorie „beweisen“, sondern den vorhandenen Testatika-Korpus so präzise wie möglich in eine **quellenkritische technische Wissensbasis** überführen. Jede Aussage ist deshalb nach ihrem Evidenztyp zu lesen:

- **Beobachtete Geometrie** ist etwas anderes als eine behauptete Funktion.
- **Ein Augenzeugenbericht** ist etwas anderes als ein reproduzierbares Messprotokoll.
- **Eine Rekonstruktionszeichnung** ist nicht automatisch eine Original-Konstruktionszeichnung.
- **Eine erfolgreiche Energieübertragung in einem Resonanzversuch** ist kein Nachweis von Energieüberschuss.
- Verschiedene Testatika-Modelle unterscheiden sich. Ein Bauteil, das bei einem Modell beobachtet wurde, darf nicht automatisch auf alle Modelle übertragen werden.

Die bisherige `state.md` wurde deshalb nicht bloß ergänzt, sondern inhaltlich neu geordnet. Frühere zu starke Verallgemeinerungen wurden korrigiert. Eine Sicherung der vorherigen Fassung liegt als `state_pre_corpus_rebuild.md` vor.

---

# 1. Kurzfassung des derzeit belastbarsten Gesamtbilds

## 1.1 Was sehr gut gestützt ist

Die Testatika/Thesta-Distatica war keine einzelne unveränderliche Maschine, sondern eine **Familie mehrerer elektrostatischer Versuchs- und Demonstrationsgeräte** der Methernitha-Gruppe. Bei den am besten dokumentierten Varianten sind sichtbar bzw. durch frühe Beobachterberichte gut gestützt:

1. eine oder zwei große, segmentierte Kunststoffscheiben;
2. bei der 50-cm-Variante zwei gegenläufige Scheiben;
3. viele metallische Sektoren/Lamellen auf den Scheiben;
4. zahlreiche **nicht berührende** Elektroden bzw. perforierte Gitter in Scheibennähe;
5. positive und negative Ladungspfade;
6. große zylindrische Seitenmodule, deren Innenaufbau je nach Quelle und Modell unterschiedlich beschrieben wird;
7. kleinere Kondensator-/Gitterbaugruppen;
8. Hufeisen-Permanentmagnete mit Wicklungen bei mehreren größeren Modellen;
9. rückseitige Glas-/Kunststoffrohre mit spiralförmigen Metallleitern;
10. einen oberen, als „crystal“, „rectifier“ oder anders gedeuteten Baustein, dessen tatsächliche Funktion **ungeklärt** bleibt;
11. eine Drehzahlregelung bzw. -erfassung mit Magnet/Rad/Reed-ähnlichem Prinzip bei der gut dokumentierten größeren Maschine;
12. Gleichspannungs-Ausgangsbehauptungen und reale Lastdemonstrationen, aber **keine vollständige unabhängige Energiebilanz**, die die behaupteten Kilowatt-Leistungen verifiziert.

## 1.2 Das belastbarste konventionelle Funktionsmodell

Der mechanisch/elektrisch am besten mit den Quellen vereinbare Kern ist:

**segmentierte, gegenläufige elektrostatische Scheiben → zeitlich veränderliche Feld-/Kapazitätskopplung → nichtkontaktierende Gitter-/Sammelelektroden → Ladungs-/Impulsaufbereitung → Speicher-/Resonanz-/Transformationsstufen → Gleichrichtung bzw. DC-Ausgang.**

Der vordere Scheiben-/Gitterteil lässt sich ohne exotische Physik als Kombination aus:

- elektrostatischer Influenz,
- variabler Kapazität,
- variablem Dielektrikum,
- Feldmodulation,
- Funken-/Koronaimpulsen,
- kapazitiver Stromkopplung

modellieren.

Die **nachgeschaltete Leistungsumwandlung** ist der am schlechtesten dokumentierte Teil. Hier konkurrieren mehrere, teils widersprüchliche Deutungen: Gitterkondensator, kapazitiver Transformator, Tesla-/HF-Resonator, bifilare Spule um Magnetstapel, Pulsformungsnetzwerk, induktive Drossel/Transformatorstufe oder Kombinationen daraus.

## 1.3 Was der Korpus NICHT belegt

Der Korpus belegt nicht belastbar:

- einen Wirkungsgrad >100 %;
- eine Energiequelle aus Permanentmagneten;
- eine Radium-/Radioaktivitätsquelle;
- eine eindeutig identifizierte „Kristall“-Energiequelle;
- eine eindeutige Originalschaltung;
- eine einheitliche Innenkonstruktion der großen Seitenbehälter für alle Modelle;
- eine direkte 50-Hz-Netzausgabe allein durch 50 Scheibensegmente;
- dass Tesla-Spulen zwingend Bestandteil **aller Originalmaschinen** waren.

Die kontrollierteste im Korpus enthaltene technische Replikation (Sven Bönisch, 2003) fand ausdrücklich **keinen Overunity-Effekt**. Rimstar-Replikationen fanden die erwartbare variable-kapazitive Wechselspannung, jedoch nur im Millivoltbereich und ohne den behaupteten Leistungseffekt.

---

# 2. Evidenzsystem

| Code | Bedeutung | Verwendung |
|---|---|---|
| **E0** | direkte visuelle Quelle | Maschinenfoto, Video-Frame, direkt lesbare Zeichnungsgeometrie |
| **E1** | unmittelbarer/zeitnaher Augenzeugenbericht | Hauser, Holzherr, Marinov; kann irren und ersetzt keine kontrollierte Messung |
| **E2** | Methernitha-nahe/offizielle Erklärung | wichtig für behauptetes Funktionsverständnis, aber nicht unabhängig |
| **E3** | sekundäre technische Interpretation | Kelly, Potter, Web-Kompilationen; häufig Hypothesen |
| **R1** | technische Replikation/Messversuch | besonders wertvoll zur Plausibilitätsprüfung; nicht automatisch identisch mit Original |
| **H** | Hypothese/Hearsay | ausdrücklich nicht als Originaldetail behandeln |
| **X** | technisch nicht verwertbar/irrelevant | Duplikat, fremdes Gerät, Binärdatei, Metadatei usw. |

### 2.1 Prioritätsregeln bei Konflikten

1. **Direkte Primärgeometrie (E0)** schlägt eine spätere Rekonstruktionszeichnung.
2. Bei Textangaben wird eine frühe, klar formulierte Augenzeugenquelle (E1) höher gewichtet als spätere Web-Kompilationen.
3. Eine **explizite Unsicherheit des ursprünglichen Autors** bleibt Unsicherheit; Fragezeichen in Skizzen werden nicht entfernt.
4. Modellunterschiede werden bevorzugt angenommen, wenn zwei seriöse Beobachter verschiedene Maschinen beschreiben.
5. Leistungsangaben ohne Input-/Output-Messprotokoll werden als **behauptet oder demonstriert**, nicht als verifiziert bezeichnet.
6. Negative Replikationsergebnisse werden nicht als Beweis der Unmöglichkeit des Originals gewertet, aber als starke Gegeninformation gegen konkrete Rekonstruktionshypothesen.

---

# 3. Korpus-Audit

## 3.1 Hauptarchiv

Das entpackte Hauptarchiv enthält **179 Dateien**. Dateitypen:

- 76 × JPG
- 45 × GIF
- 10 × HTM
- 9 × PDF
- 9 × PNG
- 7 × MHT
- 5 × ASF
- 4 × DOC
- 4 × `Thumbs.db`
- 2 × ZIP
- 2 × TXT
- 2 × EXE
- 2 × RAM/RealVideo
- 1 × HTML
- 1 × WMV

33 textfähige Dokumente wurden in Textform erschlossen. 164 Bilddateien wurden inventarisiert; technische Schlüsselbilder wurden einzeln oder über Kontaktbögen geprüft. Alle acht Videodateien wurden mittels Metadaten und Stichproben-/Kontaktbildern geprüft.

## 3.2 Exakte Duplikate im Hauptarchiv

Exakt identische Datei-Hashes:

1. `HTML_UND_BILDER/fullcircit.gif` = `HTML_UND_BILDER/fullcircit_testatika.gif`
2. `Marinov.jpg` = `testatika reports/marinov.jpg`
3. `testatika russ..pdf` = `testatika russ.pdf`

Inhaltlich existieren weitere nahezu vollständige Duplikate:
- `HTML_UND_BILDER/report99.htm` und `THE FINAL SECRET OF FREE ENERGY.mht`
- die kurze und die lange `Testatika - Replication Claim ...`-Fassung überschneiden sich stark
- `svali.pdf` steckt vollständig bzw. weitgehend in `EssentialSvali.pdf`
- `assembly pics.zip` dupliziert nahezu vollständig die Potter-GIFs
- `Replications.zip` enthält die beiden bereits im Hauptarchiv vorhandenen DOC-Dateien.

## 3.3 Verschachtelte Archive

`assembly pics.zip` enthält 35 Dateien. Bis auf eine eigene `Thumbs.db` entsprechen die Bilddateien bytegleich den Dateien in `HTML_UND_BILDER/`.

`Replications.zip` enthält:
- `Testatika - Replication Claim of the Swiss M L.doc`
- `Testatika - Replication Claim of the Swiss ML.doc`

Beide sind bytegleich mit den gleichnamigen Dateien im Hauptarchiv.

## 3.4 Dateien bewusst nicht als Testatika-Evidenz verwendet

- `EssentialSvali.pdf`, `svali.pdf`: thematisch nicht Testatika.
- `meg.pdf`, `meg_patent.pdf`: anderes Generatorprinzip (MEG).
- `De Keely ...mht`: historisches Fremdthema.
- `marinov.txt`: Marinovs allgemeine alternative-physikalische Texte; keine verlässlichen Konstruktionsdaten.
- `marinov1.exe`, `marinov2.exe`: aus Sicherheits- und Relevanzgründen **nicht ausgeführt**.
- `Thumbs.db`: Windows-Bildcaches.

Diese Dateien sind im Quellenledger trotzdem aufgeführt, damit die Archivprüfung nachvollziehbar vollständig bleibt.

---

# 4. Historische Quellen- und Modellchronologie

| Zeitraum | Quelle/Ereignis | Bedeutung |
|---|---|---|
| ca. 1960er ff. | Methernitha-eigene Darstellung | Beginn längerfristiger Energieexperimente wird behauptet |
| 14.02.1986 | Albert Hauser besucht Methernitha mit zwei Begleitern, ca. 4 h | zentrale frühe technische Augenzeugenquelle |
| 1986/1987 | Hauser-Berichte in DIFOT-News, UFO-Contact, engl. Fassung | frühe Verbreitung der Beobachtungen |
| 29.09.1988 | Hauser-Zeichnung Nr. 3279 / weitere Skizzen | wichtigste Bauteilnummerierung der mittleren Maschine |
| 09.04.1989 / 1990 | Stefan Marinov, Besuche/Briefe | wichtige Gegenquelle zu Tesla-/Magnet-Deutungen |
| 1992 | SEA-Material zum großen „Elephant“ | Existenz eines 2-m-Prototyps/Projekts dokumentiert; 30-kW-Angaben nur projektiert/promotional |
| ca. frühe 1990er | Linden-Experiment-Berichte | angebliche 700–770-V-Effekte; spätere Replikationen scheitern |
| 1999 | Hans Holzherr + >30 Techniker/Ingenieure | 50-cm-Maschine, 15 rpm, 1000-W-Lampen-/Heizerdemonstration, Prinzipversuch |
| 2003 | Sven Bönisch, ELEKTRIE | kontrollierte elektrostatische/HF-Replikation: Energieerhaltung, kein Overunity |
| 2005 | Rimstar/HCRS-Replikationen | variable Kapazität und Resonanzübertragung bestätigt, behauptete Testatika-Leistung nicht reproduziert |
| 2005 | Luzern-Folien Unipolar-Generatoren | methodischer Vergleich: gemessene COP-Werte deutlich <1 |

---

# 5. Die Testatika ist eine Maschinenfamilie

Eine zentrale Fehlerquelle früherer Rekonstruktionen ist die Annahme eines einzigen unveränderlichen „Originals“. Der Korpus zeigt mindestens folgende Klassen:

### 5.1 Kleine Modelle, ca. 12-cm-Scheibe
- von Holzherr berührbar und im laufenden Zustand anhebbar;
- einzelne Varianten mit nur einer Scheibe;
- Marinov beschreibt bei einem kleinen Modell **keine Magnete**;
- kleine Seitenkondensatoren nach Marinov: zylindrisches Gitter + transparenter Kunststoffisolator + zentrale Kupferspirale;
- Holzherr berichtet 130 V an einem Originalmodell und eine Last aus zwei kleinen Lampen + Widerstand;
- Hauser schätzte bei einem kleinen Modell ungefähr 200 W, allerdings ohne Lastprüfung;
- Antriebsbeschreibung widersprüchlich: kleiner DC-Motor laut Hauser für eine Variante; Poggendorff-artiger elektrostatischer Antrieb laut späterem Hauser-Brief; Marinov sagt bei seinem kleinen Gerät ausdrücklich kein Motor.

### 5.2 Mittlere/50-cm-Maschine
Dies ist die **am besten dokumentierte Referenzvariante**:
- zwei Plexiglasscheiben, ca. 500 mm Durchmesser, 5 mm Dicke;
- gegenläufig;
- 50 Metalllamellen auf mindestens einer Scheibe;
- zahlreiche nichtkontaktierende Gitterelektroden;
- zwei große Seitenzylinder;
- Hufeisenmagnete/Wicklungen;
- Drehzahl je nach Beobachtungszeitpunkt ca. 60 rpm bzw. 15 rpm;
- Hauser-Zeichnung Nr. 3279 bezieht sich auf eine mittlere Maschine;
- Leistungsbezeichnungen schwanken zwischen „1 kW“ in späterer Buchdarstellung und etwa 300 V × 10 A in Hausers Brief bzw. 3–4 kW in Methernitha-Darstellungen.

### 5.3 Größere 3-kW-/3–4-kW-Ausführungen
Direktfotos (`testabig.jpg`, `TESTA7.jpg`, `TESTA9.jpg`, `3kwfront.jpg`, `3kwrear.jpg`) zeigen mehrere deutlich komplexere Konfigurationen mit:
- großen zylindrischen Behältern,
- vielen perforierten Gittern,
- langen rückseitigen Röhren,
- Hufeisen-/Spulengruppen,
- oberen horizontalen Baugruppen.

Die genaue Zuordnung jedes Fotos zu einer bestimmten Leistungsstufe ist nicht immer gesichert.

### 5.4 „Elephant“ / 2-m-Klasse
Fotos/Notizen und RealVideo-Material belegen, dass sehr große Maschinen/Prototypen mit etwa 2-m-Scheibe gebaut bzw. montiert wurden. Die im SEA-Material genannten **30 kW** sind als projektiert/promotional zu behandeln; der Korpus enthält kein kontrolliertes 30-kW-Messprotokoll.

---

# 6. Referenzmaschine: Hauser-Zeichnung Nr. 3279

Die originale/zeitnahe Hauser-Zeichnung enthält Front-, Rück-, Drauf- und Seitenansicht sowie folgende Bauteilliste:

| Pos. | Lesbare Bezeichnung | Evidenz/Kommentar |
|---|---|---|
| 1 | `FRONT DISK` | vordere Scheibe |
| 2 | `BACK DISK` | hintere Scheibe |
| 3 | `GEAR-WHEEL / PULLEY` | Scheiben-/Riemen-/Drehzahlmechanik; Magnetrad ist Teil dieses Bereichs |
| 4 | `LAMELLA / SEGMENT` | metallische Scheibensegmente |
| 5 | `ELECTRODE` | nichtkontaktierende Elektroden/Gitter |
| 6 | `BIG CAPACITOR` | zwei große seitliche Zylindermodule |
| 7 | `CAPACITOR` | kleiner horizontaler/liegender Kondensator |
| 8 | `CAPACITOR` | zweiter kleiner Kondensator |
| 9 | `PIPE WITH SPIRAL` | langes Rohr mit Metallspirale |
| 10 | `HORSESHOE MAGNET` | Hufeisenmagnet mit Wicklung |
| 11 | `MAGNET` | weiterer Magnet, Position/Funktion nicht vollständig geklärt |
| 12 | `RECTIFIER` | Hausers damalige Funktionsbezeichnung; spätere Quellen sprechen teils nur von „crystal“ |
| A | `NYLON BELT` | Riemen für die gegenläufige Scheibenbewegung |

Die Zeichnung zeigt in der Draufsicht für Pos. 6 ausdrücklich:
- `Bifilar Coil`
- `Inside Grid`
- `Middle Grid`
- `Outside Grid`
- `Acrylic Tube Insulation`
- `Magnet Tube`

**Wichtig:** Eine spätere interpretierende Zeichnung im Hauser-Ordner (`ABweb4.jpg`) trägt zusätzliche Bezeichnungen wie „Tesla Coil“, „amplification component“ und „50 for Europe / 60 for U.S.“. Ihr Zeichenstil und die zusätzlichen Funktionsannahmen unterscheiden sich deutlich von Zeichnung 3279. Diese Labels dürfen nicht ohne Kennzeichnung als von Hauser direkt beobachtete Originalbeschriftungen ausgegeben werden.

### 6.1.1 Neu verifizierte Details aus der hochvergrößerten Zeichnung 3279

Bei erneuter visueller Prüfung der Originalgrafik `ABweb3.jpg` ist die nummerierte Teileliste konsistenter lesbar als in früheren Durchgängen:

- Pos. 1 `FRONT DISK`
- Pos. 2 `BACK DISK`
- Pos. 3 `GEAR-WHEEL` / Timing-/Riemenbereich
- Pos. 4 `LAMELLA`
- Pos. 5 `ELECTRODE`
- Pos. 6 `BIG CAPACITOR`
- Pos. 7 `CAPACITOR`
- Pos. 8 `CAPACITOR`
- Pos. 9 `PIPE WITH SPIRAL`
- Pos. 10 `HORSESHOE MAGNET`
- Pos. 11 `MAGNET`
- Pos. 12 `RECTIFIER`
- A `NYLON BELT`

Der Titelblock scheint außerdem eine Maschinenangabe in der Größenordnung **„3 kW – 300 V DC“** zu enthalten. Wegen der geringen Scanauflösung wird dies **nicht als gemessene Nennleistung**, sondern als Beschriftung/Claim der Zeichnung behandelt. Die Zeichnungsnummer **3279** und ein Maßstab ungefähr **1:7** sind erkennbar.

Diese erneute Prüfung erhöht das Vertrauen in die Bauteilidentitäten, **nicht** in die Leistungsangabe.

---

# 7. Scheiben: Maße, Material, Segmente

## 7.1 Hausers Primärangaben

Hauser schreibt für Pos. 1:
- Plexiglasscheibe;
- **Durchmesser 500 mm**;
- **Dicke 5 mm**;
- **50 Chromstahl-Lamellen**;
- Lamellengröße laut Hausers englischem Originalbericht ungefähr **0,2 × 20 × 160 mm**;
- Lamellen auf der äußeren Seite;
- Baumann habe diese Scheibe analog zu einer „Wolke“ erklärt.

Pos. 2:
- gleich groß und gleiches Grundmaterial;
- dunklere Färbung;
- dreht in entgegengesetzter Richtung;
- Lamellen auf **beiden Seiten**;
- von Baumann analog zum „Erdboden“ erklärt.

## 7.2 Wichtige Quellenabweichung: 160 mm vs. 60 mm

Die vom Nutzer fotografierte deutschsprachige Buchseite 88 druckt sichtbar **„0,2 × 20 × 60 mm“**. Hausers frühere Originalseite `ABweb1.jpg` sagt dagegen klar **„0,2x20x160mm“**.

Bewertung:
- **160 mm erhält Vorrang als Primärangabe (E1)**.
- 60 mm wird als **sekundärer Transkriptions-/Druckfehler oder abweichende Wiedergabe** dokumentiert, nicht stillschweigend gelöscht.
- Bei einer 500-mm-Scheibe ist eine radiale Länge von 160 mm geometrisch plausibel: sie kann etwa von einem Nabenradius ~80–90 mm bis nahe zum 250-mm-Außenradius reichen.
- 60 mm wäre für die auf Fotos sichtbaren langen radialen Segmente deutlich weniger plausibel.

## 7.3 Abgeleitete Geometrie bei 50 Segmenten

Durchmesser \(D=0{,}5\,m\), Radius \(r=0{,}25\,m\):

- Umfang: \(U=\pi D pprox 1{,}571\,m\)
- Winkelteilung bei 50 Segmenten: \(360°/50 = 7{,}2°\)
- Umfangsteilung am Außenrand: ca. **31,4 mm**
- bei 20-mm-Tangentialbreite blieben dort idealisiert ca. 11,4 mm Zwischenraum.

Die reine Metallfläche von 50 Lamellen à 20 × 160 mm wäre ca.:
\[
50 	imes 0{,}020 	imes 0{,}160 pprox 0{,}160\,m^2
\]
pro belegter Scheibenseite.

## 7.4 Magnetisierung der Lamellen

Hauser berichtet:
- Lamellen seien **leicht magnetisiert**;
- das Material bzw. eine Beschichtung solle gegen Korona-Oxidation schützen.

In einem späteren Brief relativiert er:
- bei einer großen Maschine seien Segmente magnetisch;
- kleinere Maschinen bzw. andere Varianten hätten dies nicht zwingend;
- er folgert selbst, die magnetische Funktion sei **nicht grundsätzlich notwendig**, sondern möglicherweise eine Verbesserung.

Damit ist „magnetische Segmentierung“ **modellabhängig**, nicht universell.

---

# 8. Elektroden, Gitter und „Taster/Antenna Keys“

## 8.1 Nichtkontakt ist sehr gut belegt

Hauser schreibt ausdrücklich:
> None of the electrodes touch the disks.

Dies wird durch:
- Zeichnung Nr. 3279,
- Direktbilder,
- die offizielle Filmtranskription („non-contacted … antennae keys“),
- Holzherrs Beobachtungen

gestützt.

## 8.2 Hausers Anzahl und Aufbau

Für Pos. 5:
- ungefähr **8 Elektroden vorne**;
- ebenfalls ungefähr **8 hinten**;
- hintere Elektroden nicht parallel zur Scheibe;
- Elektrodenränder radial/umgebogen;
- Konstruktion aus wechselnden Lagen perforierten Metalls und isolierender Platten.

Hauser vergleicht den Aufbau ausdrücklich mit einer alten Wimshurst-Maschine, weist aber auf mehr Elektroden und den fehlenden Kontakt hin.

## 8.3 Beobachtete Formen

Direktfotos zeigen mehrere Kategorien:
- horizontale Sammelelektroden in Scheibenmitte;
- diagonal zur Scheibe angeordnete perforierte „Finger“/Platten;
- vertikale perforierte Platte oben/zentral;
- rechteckige mehrlagige Gitterpaneele seitlich;
- kleine Plexiglasblöcke mit perforiertem Blech auf einer oder zwei Flächen;
- rückseitige Gitter, die bei manchen Rekonstruktionen um etwa 45° versetzt angenommen werden.

## 8.4 Funktionell plausible Rolle

Konventionell lassen sich die Gitter als:
- Influenz-/Feldelektroden,
- kapazitive Abnehmer,
- variable Kondensatorelektroden,
- Ladungssammler,
- Feldformungselemente

interpretieren.

Rimstar fand in einer Replikation tatsächlich ein **variables kapazitives/variables dielektrisches Verhalten** mit AC-Impulsen, jedoch nur ca. 20–50 mV.

---

# 9. Scheibenantrieb, Riemen, Drehzahlmessung und Selbstlauf — Widerspruchsbereich

## 9.1 Hauser 1986
Pos. 3:
- Magnetrad gegen Timing-/Antriebsrad;
- Regelung/Bremsung der Scheiben;
- Zielwert ca. **60 U/min**;
- flexible Riemenübertragung.

## 9.2 Hauser, späterer Brief
Er präzisiert:
- Magnetrad auf derselben Welle wie Riemenscheiben;
- Nylonriemen **nicht gekreuzt**; die Riemenscheiben bewirken die Gegenläufigkeit;
- große Maschine: Drehzahl mit Magnetrad geregelt;
- Scheiben seien bei dieser großen Maschine von einem **kleinen DC-Motor** angetrieben;
- kleine Maschinen seien nach seiner Aussage durch eine Art „Poggendorff effect“ angetrieben.

## 9.3 Methernitha-Film
Die offizielle Erklärung behauptet:
- Start von Hand;
- danach Selbstrotation durch elektrostatische Anziehung/Abstoßung;
- eine „rectifying diode“ halte die Zyklen stabil, damit sich Antriebsimpulse nicht aufschaukeln;
- langsame, konstante Drehzahl sei für optimale Leistung wesentlich.

## 9.4 Marinov
Für ein kleines Gerät:
- **kein Motor**;
- Rotation nur durch elektrostatische Abstoßung;
- die Scheibe des kleinen Geräts sei elektrisch „mit nichts verbunden“.

## 9.5 Holzherr 1999
- 50-cm-Maschine lief bereits beim Betreten;
- ungefähr **15 U/min**, nicht 50–60;
- „magnetisch“ geregelt;
- frühestes Modell sei nach seiner Information das einzige mit elektrischem Motor, der aus einem ständig nachgeladenen Kondensator gespeist werde.

## 9.6 Schluss
Es gibt **keine einzige universelle Antriebsbeschreibung**. Am wahrscheinlichsten ist:
- unterschiedliche Modelle/Entwicklungsstadien;
- teils Hilfsmotor;
- teils elektrostatischer Motorbetrieb;
- magnetische Regel-/Sensorik;
- im öffentlichen Narrativ Selbstlauf.

Jede Rekonstruktion, die „die Testatika hatte definitiv keinen Motor“ oder umgekehrt „sie war immer motorgetrieben“ sagt, ist mit dem Korpus unvereinbar.

---

# 10. Drehzahl und Frequenzen

## 10.1 Beobachtete/berichtete Drehzahlen
- Hauser: ca. 60 U/min für die große Referenzmaschine.
- diverse Sekundärquellen: ca. 50–60 U/min.
- Holzherr 1999: ca. **15 U/min** bei der 50-cm-Demonstration.

## 10.2 Segmentpassage an einem festen Abnehmer

Für \(N\) Segmente und \(n\) U/min:
\[
f_{fixed} = N\cdot n/60
\]

Bei 50 Segmenten:
- 60 rpm → **50 Hz**
- 15 rpm → **12,5 Hz**

Bei 60 Segmenten:
- 60 rpm → **60 Hz**
- 15 rpm → **15 Hz**

## 10.3 Relative Segmentausrichtung zweier gleich schneller, gegenläufiger Scheiben

Wenn beide Scheiben mit Betrag \(n\) gegenläufig laufen:
\[
f_{rel}pprox N\cdot 2n/60
\]

Bei 50 Segmenten:
- 60 rpm → ca. **100 relative Ausrichtungen/s**
- 15 rpm → ca. **25/s**

Welche dieser Frequenzen elektrisch dominant wäre, hängt vollständig von Elektrodenposition, Verschaltung, Polpaaren und Symmetrie ab.

## 10.4 „50 for Europe / 60 for U.S.“

In `ABweb4.jpg` bzw. der späteren Buchreproduktion ist lesbar:
**„Magnetic Stainless Steel Disc Segments … (50 for Europe) (60 for U.S.)“**.

Das ist auffällig, da 50/60 an Netzfrequenzen erinnert. Dennoch:
- bei 60 rpm ergibt nur eine **feste** 50-/60-Segmentpassage direkt 50/60 Hz;
- die Gegenrotation verdoppelt relative Musterraten;
- Holzherrs 15-rpm-Beobachtung passt nicht zu einem einfachen 50-Hz-Segmentargument;
- der offizielle Ausgang wird als DC beschrieben.

Daher bleibt eine gezielte 50/60-Hz-Abstimmung **plausibel, aber nicht bewiesen und nicht universell**.

---

# 11. Pos. 6 — die großen seitlichen „Kondensatoren“ / Pots

Dies ist der wichtigste und widersprüchlichste Baugruppenbereich.

## 11.1 Was visuell sicher ist
Bei mehreren größeren Modellen sind zwei große symmetrische zylindrische Seitenbaugruppen sichtbar:
- außen perforierte/meshartige Metallzylinder;
- isolierende bzw. schwarze Deckel;
- oben dicke Metallringe/-rohre oder Anschlüsse;
- innere Struktur von außen nicht vollständig sichtbar.

## 11.2 Hausers direkte Beschreibung
Hauser beschreibt **zwei Zylinder**, jeweils:
- drei konzentrische Metallrohre, ausdrücklich **Gitter, nicht Folie**;
- Acrylrohre zwischen den Gittern als Isolation;
- in der Mitte einen vertikalen „magnet tube“, vermutlich Stapel von Lautsprechermagneten;
- Nord/Süd axial, Orientierung könne umgekehrt sein;
- um den Magnetstapel **zwei Lagen 18-AWG emaillierten Kupferdraht**;
- Kunststofffolie zwischen Magnetrohr/erster Wicklung und zwischen erster/zweiter Wicklung;
- zweite Lage in entgegengesetzter Richtung gewickelt;
- Verbindung so, dass die Gesamtspule als **bifilar** arbeitet.

Hauser ist ausdrücklich **nicht sicher**, wie Magnettube und Spule elektrisch in den Gesamtstromkreis eingebunden sind.

## 11.3 Ausgang
Hausers späterer Brief:
- Oberseite der Pos.-6-Zylinder zu den horizontalen Elektroden neben den Scheiben verbinden;
- nutzbarer Ausgang angeblich **300 V × 10 A**;
- Abnahme an Kupferringen oben auf den beiden Zylindern;
- Hauser vermutet eine Verbindung dieser Ringe mit dem mittleren Gitterrohr;
- die Maschine enthalte **drei isolierende Schaltungen**, die „in harmony“ sein müssten.

Dies ist eine wichtige Aussage über die behauptete Topologie, aber kein verifiziertes 3-kW-Messprotokoll.

## 11.4 Holzherr 1999
Baumann habe über die großen Kondensatoren gesagt:
- **20 Lagen perforiertes Blech**.

Von außen war der Innenaufbau nicht sichtbar.

## 11.5 Marinov — kleine Maschine
Bei einem kleinen Gerät sah Marinov:
- zylindrisches Gitter;
- zylindrischen Kunststoffisolator;
- zentrale Kupferspirale;
- **keine Magnete**.

Er betont später:
- die seitlichen Teile seien Kondensatoren;
- die „Spiralen“ seien lediglich eine Elektrode des Kondensators;
- **keine Tesla-Spulen**, kein Wechselstrom — seine damalige Interpretation.

Das betrifft eine **kleine Variante** und widerspricht deshalb nicht zwingend Hausers großer Maschine, zeigt aber, dass die Innenkonstruktion nicht pauschal übertragbar ist.

## 11.6 Potter-Rekonstruktion — ausdrücklich hypothetisch
Potter bzw. spätere Buchgrafiken rekonstruieren:
- zentralen Zylinder;
- mehrere verschachtelte Pancake-/Flachspulen;
- primäre und sekundäre Wicklungen;
- sechs hohle Ringmagnete mit Kunststoffabstandshaltern/Luftspalten;
- perforierten Aluminiumzylinder als elektrostatische Abschirmung;
- Kupferblech als magnetische/EM-Abschirmung;
- interne „grid condensers“;
- sekundären Ausgang zum oberen Ring;
- möglicherweise ein Pulsformungsnetzwerk.

Diese Darstellung ist technisch interessant, aber die zugehörige deutsche Buchseite bezeichnet sie selbst als **„Vermuteter Innenaufbau“**. Sie ist keine fotografisch bestätigte Schnittzeichnung des Originals.

## 11.7 Spätes Hearsay
Ein Web-Kompendium berichtet, ein weiterer Informant habe behauptet:
- ältere große „pots“ seien Kunststoffbehälter mit Aluminium-Drehspänen;
- der obere „rectifier“ sei eher eine Solenoid-/variable Induktivitätsanordnung mit verschiebbarem Abgriff.

Diese Aussage steht im Konflikt zu mehreren anderen Beschreibungen und bleibt **H**.

## 11.8 Konservativer Schluss
Für Pos. 6 darf als **korpusweit sicherster gemeinsamer Nenner** gelten:
- symmetrische zylindrische Hochspannungs-/Speicher-/Kopplungsmodule;
- perforierte Gitter-/Metallflächen;
- Isolatoren;
- bei mindestens einer größeren Hauser-Maschine bifilare Wicklung + zentraler Magnetstapel;
- bei anderen/kleinen Varianten möglicherweise deutlich simpler.

Eine einheitliche „Tesla-Pancake-6-Ringmagnet“-Innenarchitektur ist **nicht belegt**.

---

# 12. Pos. 7 und Pos. 8 — kleinere Kondensatoren

Hauser beschreibt Pos. 7 und 8 schlicht als:
- kleinere, liegende „capacitors“.

Er schreibt später, Baumann habe gesagt, die kleinen Kondensatoren seien **ähnlich zu den großen**. Das könnte auf Gitter-/Mehrschichtaufbau hinweisen, ist aber zu unpräzise für eine sichere Innenrekonstruktion.

In Hausers Zeichnung sind sie im mittleren Maschinenbereich vor/nahe den großen Seitenmodulen angeordnet.

---

# 13. Pos. 9 — Rohr mit Metallspirale

Hausers direkte Beschreibung:
- Glasrohr;
- darin/umgeben von einer Aluminiumspirale;
- die Spirale sei tatsächlich ein **revolving shaving**, also ein Dreh-/Drechsel-/Drehbankspan bzw. spiralförmiger Metallspan.

Späterer Hauser-Brief:
- die hohen dünnen Kondensatoren/Rohre auf der Rückseite würden zum „drive the discs“ benötigt.

Potter interpretiert die langen hinteren Rohre als HF-Drosseln/Chokes oder Teile eines LC-Netzwerks. Das ist **E3/H**, nicht Hausers sichere Funktion.

Direktfotos (`TESTA9.jpg`) bestätigen lange, schlanke, vertikale, perforierte/spiralige leitende Strukturen hinter bzw. neben der Scheibe.

---

# 14. Pos. 10 — Hufeisenmagnete mit bifilaren Wicklungen

Hauser:
- Hufeisenmagnete;
- Wicklungen seien bifilar;
- die kleinen Spulen sitzen tatsächlich **direkt auf den Beinen** der Hufeisenmagnete;
- zwischen den Magnetbeinen mehrere Lagen:
  - Isolierplatten,
  - perforierte Metallbleche.

Direktfotos zeigen im unteren Mittelbereich:
- zwei symmetrische Hufeisen-/U-förmige Baugruppen;
- Wicklungen bzw. rote Spulen-/Leiterelemente;
- dazwischen perforierte/mehrschichtige Blocks.

Funktion bleibt offen. Konventionell möglich:
- magnetisch vorgespannte Induktivität;
- gekoppelte Drossel;
- HF-/Impulsfilter;
- feldabhängige Kopplung;
- Bestandteil eines Resonanzkreises.

**Nicht zulässig als Schluss:** Permanentmagnete seien eine kontinuierliche Energiequelle.

---

# 15. Pos. 11 — zusätzlicher Magnet

Hauser markiert einen weiteren Magneten (Pos. 11), kann aber später die genaue Verbindung/Funktion nicht erklären.

In der Zeichnung liegt er im oberen/mittleren Maschinenbereich. Wegen fehlender eindeutiger Detailbeschreibung bleibt:
- Existenz/Position in Zeichnung: **E0/E1**
- konkrete elektrische Funktion: **unbekannt**.

---

# 16. Pos. 12 — „Rectifier“, „Crystal“, obere Baugruppe

Dies ist einer der größten Konfliktpunkte.

## 16.1 Hauser 1986
„Possibly a rectifier“:
- längliches Stück perforierte Metallplatte;
- vertikal angeordnet;
- eine Spule darum;
- Glasabdeckung;
- ein oder mehrere „crystals“ darin;
- andere Besucher hätten magnetische Endkappen erwähnt;
- Hauser meint, das System sei wahrscheinlich **nicht evakuiert**, da eine kleinere Maschine einen offenen „rectifier“ hatte.

## 16.2 Hauser später
- Kristalle seien nur **oben an der Maschine** gesehen worden, bei Pos. 12.

## 16.3 Marinov
- Baumann habe immer von einem **„crystal“** gesprochen;
- nicht vom Wort „rectifier“;
- Marinov wusste nicht, was der Kristall bedeute oder wie er wirke.

## 16.4 Holzherr 1999
- „crystal diode“ sei wahrscheinlich das obere Objekt;
- beim Originalmodell wirkte es wie eine grobe Spule um einen geraden zentralen Draht;
- insgesamt 4 Anschlüsse;
- an der 50-cm-Maschine konnte er nur 2 Zuleitungen erkennen;
- ein Kristall war nicht sichtbar.

## 16.5 Potter
Hypothese eines selbstgebauten thermionischen/Vakuum-Gleichrichters bzw. einer HF-Oszillator-/Ventilfunktion. `glow.jpg` zeigt eine leuchtende/orange Linie in einem oberen Bauteil, beweist aber weder Vakuumröhre noch konkrete Elektronenröhrenfunktion.

## 16.6 Spätes Hearsay
Andere Angaben deuten das obere Teil als Solenoid mit verschiebbarem Abgriff/Abstimmung statt Diode.

## 16.7 Geometrische Korrektur aus den Direktfotos

Die Beschreibung „vertikale perforierte Platte“ darf nicht mit der Orientierung der **gesamten** Pos.-12-Baugruppe verwechselt werden. In `testabig.jpg` ist die obere Baugruppe als **horizontal quer über der Maschine liegendes Rohr-/Spulenmodul** sichtbar. Darin bzw. daran kann eine vertikal orientierte perforierte Innenplatte sitzen. Beide Beobachtungen sind geometrisch miteinander vereinbar.

Damit gilt:
- Gesamtbaugruppe bei mindestens einer großen fotografierten Maschine: horizontal;
- interne perforierte Elektrode/Platte nach Hauser: vertikal;
- Endbereiche wirken spulen-/gitterartig;
- zentrale Zone ist heller/isolierend/perforiert;
- eine universelle identische Pos.-12-Geometrie für alle Modelle ist nicht gesichert.

## 16.8 Schluss
Die korrekte State-Bezeichnung lautet:
**„obere Crystal-/Rectifier-/Spulenbaugruppe, Funktion und interne Verschaltung ungeklärt“**.

Keine einzelne der folgenden Aussagen ist ausreichend belegt:
- normale Halbleiterdiode;
- Vakuumdiode;
- thermionischer Gleichrichter;
- Kristalldetektor;
- Resonanzspule;
- variable Induktivität.

---

# 17. Direktfotos: zusätzliche Geometriedetails

## 17.1 `testabig.jpg`
Hochauflösende Frontansicht zeigt:
- zentrale dunkle/transparente Scheibe mit vielen radialen Draht-/Metallsektoren;
- zentrale Nabe und horizontale Träger-/Kollektoranordnung;
- zentrale vertikale perforierte Platte;
- zwei schräg nach außen gerichtete perforierte Elektroden;
- oben horizontale rot/weiße Baugruppe mit perforiertem Mittelteil und dunklen Wicklungspaketen an beiden Enden;
- seitlich oben zwei große rechteckige mehrlagige Paneele: helle perforierte Außenplatte, dunkles Gitter innen, rötlicher Leiterrahmen;
- links/rechts unten große Zylinder mit perforiertem Außenmantel, schwarzem Deckel und ring-/rohrförmigen oberen Anschlüssen;
- seitlich unterhalb der Scheibe treppenartige perforierte Gittermodule;
- zwei lange vertikale Spiral-/Rohrbauteile im unteren Bereich;
- mittig unten perforierter Block über einem hufeisenförmigen/magnetischen Kern;
- mehrere massive Anschlussklemmen an der Frontbasis.

## 17.2 `TESTA7.jpg`
Andere Variante:
- zwei große seitliche Behälter mit schwarzem Deckel und U-förmigem Metallanschluss;
- zentral große segmentierte Scheibe;
- zwei innere vertikale zylindrische/perforierte Module;
- mehrere rote Spulen-/Kerne unten;
- obere mehrfach gefingerte/perforierte Baugruppe;
- stärker sichtbare Kupfer-/Metallbänder um die großen Zylinder.

## 17.3 `TESTA9.jpg`
Seiten-/Rückansicht:
- bestätigt deutlich die Dicke/Mehrlagengeometrie der Scheiben;
- lange vertikale perforierte Zylinder nahe der Scheibe;
- weiße Isolator-/Trägerplatten;
- große rote Wicklungen unten;
- mechanische Rolle/Riemen-/Motorbereiche;
- rückseitige elektrische Verbindungselemente.

## 17.4 `f31.jpg`
Nahaufnahme eines rechteckigen Paneels:
- helle perforierte Außenschicht;
- dunkles quadratisches Gitter;
- rötlicher Leiter-/Rahmenbereich;
- unterstützt die Interpretation eines **mehrlagigen Gitter-/Dielektrikumsystems**, ohne dessen Schaltung zu verraten.

## 17.5 `glow.jpg`
Leuchtende obere Röhre/Baugruppe:
- visueller Hinweis auf Stromfluss, Entladung oder erhitztes Element;
- **keine eindeutige Identifikation** als thermionische Röhre.

---

# 18. Basisplatte und mögliche Gitter-/Kapazitätsfunktion

Hauser berichtet aus anderen Besucherangaben:
- die dicke Holzgrundplatte solle abwechselnde Lagen perforierter Metallplatten und Isolierplatten enthalten.

Holzherr:
- konnte die 50-cm-Maschine nicht anheben;
- Basis erschien massiv;
- kleine Modelle konnten angehoben werden.

Spätere Prinzipversuchs-Videos/Notizen zeigen eine außen mit Gitter bedeckte Basis.

Bewertung:
- Ein kapazitiv/elektrostatisch aktiver Sockel ist **plausibel**, aber für die Hauptmaschine nicht direkt durch einen geöffneten Querschnitt bestätigt.
- Verdeckte Batterien wurden von Holzherr diskutiert, aber weder nachgewiesen noch ausgeschlossen.

---

# 19. Elektrische Verbindungen: was tatsächlich bekannt ist

## 19.1 Belastbar
- horizontale Elektroden neben der Scheibe sind mit oberen Bereichen der Pos.-6-Zylinder verbunden (Hauser);
- positiver und negativer Ausgang werden an zwei oberen Metall-/Kupferringen der Pos.-6-Zylinder beschrieben;
- viele Beschichtungen/Gitter sind untereinander verbunden;
- Verbindungen zu Pos. 7/8 sowie teilweise Pos. 9/10/12 werden erwähnt;
- rote/blaue Leitungen in Fotografien/Zeichnungen markieren zwei Polaritätssysteme.

## 19.2 Nicht bekannt
Es fehlt ein vollständiger, originaler, durchgehend nachvollziehbarer Schaltplan mit:
- allen Knoten,
- allen Kapazitäten,
- Wicklungssinnen,
- Windungszahlen,
- Magnetpolungen,
- Dioden-/Kristallanschlüssen,
- Erd-/Bezugspotential,
- Ausgangsfilterung.

Hauser schreibt selbst, die elektrischen Verbindungen seien nur **unvollständig** bekannt.

### 19.3 Direkt belegte bzw. stark gestützte Teilpfade

Aus Hauser-Briefen, Zeichnung 3279, Direktfotos und Holzherr lassen sich derzeit folgende Teilpfade getrennt festhalten:

1. **Scheiben-/Elektrodenpfad:** segmentierte Scheiben ↔ nichtkontaktierende perforierte Elektroden.
2. **Elektroden → Pos. 6:** horizontale Scheibenelektroden führen zu den oberen Bereichen der großen Zylindermodule.
3. **Pos. 6 → Ausgang:** Hauser beschreibt die oberen Kupferringe der beiden Pos.-6-Zylinder als Ausgangspunkte; er vermutet eine Verbindung zum mittleren Gitterrohr.
4. **Pos. 7/8:** kleinere Kondensatoren sind mit Teilen des Hauptsystems verbunden; exakte Knoten unbekannt.
5. **Pos. 9/10/12:** Teilverbindungen werden erwähnt bzw. in Skizzen gezeigt, aber ihre Polarität, Reihenfolge und galvanische/kapazitive/induktive Natur bleiben offen.
6. **Zweipoligkeit:** rote und blaue Leitungsfamilien bzw. Plus-/Minus-Seiten sind bei mehreren Rekonstruktionen und Beobachterzeichnungen konsistent.
7. **DC-Ausgang:** Betreiber-/Beobachterquellen beschreiben den Nutzerausgang als Gleichstrom.

### 19.4 Hausers „three isolating circuits“

Hauser schreibt, die Maschine enthalte **„three isolating circuits“**, die miteinander „in harmony“ sein müssten. Der Wortlaut ist wichtig, aber die drei Kreise werden nicht eindeutig benannt. Drei derzeit denkbare Zuordnungen werden deshalb getrennt geführt:

- **Hypothese T1 – drei Kopplungsarten:** elektrostatisch/kapazitiv, magnetisch/induktiv und nichtlinear/gleichrichtend.
- **Hypothese T2 – drei Potentialdomänen:** positiver Zweig, negativer Zweig und mittlerer/Steuer-/Center-Zweig.
- **Hypothese T3 – drei hintereinandergeschaltete Isolationsblöcke:** Scheibe→Gitter, Gitter→Pos.-6-Innenkreis, Pos.-6/10/12→Ausgang.

Keine dieser drei Zuordnungen ist bislang direkt belegt. T2 passt geometrisch zur ausgeprägten Links-/Rechts-Symmetrie und zu einem Centerline-/Centering-Kondensator in späteren Zeichnungen; T1 passt zu den beobachteten unterschiedlichen Kopplungselementen. Beide bleiben **prüfbare Hypothesen**.

Daher ist jede im Korpus gezeigte „full circuit“-Grafik als **Rekonstruktion**, nicht als bestätigter Originalschaltplan zu behandeln.

---

# 20. Methernitha-eigene Funktionsbeschreibung

Die Filmtranskription formuliert folgende Kette:

1. zwei gegenläufige Scheiben erzeugen elektrostatische Ladung;
2. eine Scheibe steht sinnbildlich für Erde, eine für Wolke;
3. Gitterelektroden „binden“ Ladungen;
4. berührungslose „Taster/antennae keys“ sammeln sie;
5. Ladungen werden danach „sorted“/geordnet (Transkript unsicher);
6. Scheiben werden von Hand gestartet;
7. danach Rotation durch elektrostatische Anziehung/Abstoßung;
8. eine „rectifying diode“ halte den Zyklus stabil;
9. korrekte langsame, gleichmäßige Drehzahl sei wichtig;
10. „grid condensers“ speichern Energie und geben sie gleichmäßig ab;
11. dabei werde Hochspannung reduziert und mit zusätzlichen Bauteilen „power built up“;
12. Endausgang: gleichmäßiger Gleichstrom.

Behauptete Daten:
- **3–4 kW dauerhafte Ausgangsleistung**
- ca. **270–320 V**
- Leistung abhängig von Luftfeuchtigkeit;
- hohe Feuchtigkeit erschwere Potentialaufbau, trockene Luft begünstige ihn.

Diese Angaben sind **E2: offizielle Behauptung**, nicht unabhängige metrologische Verifikation.

---

# 21. Beobachtete Lastdemonstrationen und Leistungsangaben

| Quelle | Modell/Situation | Beobachtung/Behauptung | Evidenzbewertung |
|---|---|---|---|
| Hauser 1986 | große Maschine | 1000-W-Glühlampe während Besuch getestet | E1, Lastverhalten beobachtet; kein vollständiges Messprotokoll |
| Hauser später | mittlere Maschine | 300 V × 10 A an oberen Pos.-6-Ringen | E1-Angabe/Behauptung; 3 kW rechnerisch |
| Methernitha-Film | größere Modelle | 3–4 kW, 270–320 V DC | E2, offizielle Angabe |
| Holzherr 1999 | 50-cm | 1000-W-Lampe ca. 10 s, Helligkeit blieb; U-Heizer sehr schnell heiß; ~1-cm-Lichtbogen | E1-Demonstration; keine simultane vollständige U/I/Input-Messung |
| Holzherr 1999 | 12-cm | 130 V; zwei kleine Lampen + Widerstand, Werte unbekannt | E1; digitaler Voltmeter fiel danach aus |
| Linden-Bericht | mittlere Maschine | ~770 V Leerlauf; ~580 V an Heizlast, behauptet ~3 A | E1/E3; Drittquelle, Messkette/Lastdaten inkonsistent |
| Kelly | mittlere | 300 V, 10 A, 3 kW | E3; abgeleitet |
| Web-Kompendium | 3-kW | 230 V, 13 A, gepulster DC | E3; unbestätigt |
| SEA | „Elephant“ | 30 kW projektiert | E3/promotional; kein Leistungsnachweis |

## 21.1 Holzherr-Details
- Maschine lief ca. 1,5 h während Besuch.
- 1000-W-Lampe ca. 10 s.
- U-förmiges Heizelement wurde nach etwa 1 s zu heiß zum Halten.
- beim Zurückziehen eines Kontaktleiters ca. 1-cm-Lichtbogen etwa 1 s.
- keine merkliche Drehzahländerung unter Last beobachtet; Holzherr räumt ein, dass die Aufmerksamkeit auf der Last lag.
- Maschine unter Plexiglashaube; Anschlussleitungen durch Öffnungen nahe der Basis.

**Wichtig:** Das ist ein eindrucksvoller Demonstrationsbericht, aber kein kalorimetrisch/elektrisch geschlossener Leistungsnachweis.

---

# 22. Feuchtigkeit und Korona

Methernitha behauptet ausdrücklich:
- höhere Luftfeuchtigkeit verschlechtert Potentialaufbau;
- trockenere Luft verbessert Betrieb.

Das ist qualitativ mit normaler Hochspannungselektrostatik vereinbar:
- feuchte Oberflächen erhöhen Leckströme;
- Oberflächenwiderstände von Isolatoren sinken;
- Ladungen dissipieren schneller.

Die Feuchtigkeitsabhängigkeit ist daher **kein Hinweis auf exotische Energie**, sondern zunächst ein typisches Elektrostatikmerkmal.

---

# 23. Holzherrs „Prinzipversuch“ 1999

## 23.1 Beobachteter Aufbau
- horizontal schwenkbarer Plexiglasarm;
- an beiden Enden kleine rechteckige Plexiglasplatten auf Unterseite;
- Unterseite des Arms mit perforiertem Aluminiumblech, quadratische Löcher;
- Unterseite der Endplatten mit Messingdrahtgitter;
- unter jeder Endplatte fünf weitere Plexiglasplatten auf der Basis;
- Gitterlagen zwischen den Platten;
- unterste Gitterlage zu zwei parallel geschalteten Kondensatoren.

## 23.2 Demonstration
- Baumann bewegte den Arm etwa zehnmal hin und her;
- volle Rotation wegen Kondensatoren nicht möglich;
- Digitalmessgerät zeigte angeblich **60 V DC**;
- Kurzschluss der Kondensatoren erzeugte lauten Knall;
- Baumann sagte, mit Metallfolie statt Drahtgitter funktioniere der Effekt nicht.

## 23.3 Bedeutung
Dieser Versuch ist wichtig, weil Baumann laut Holzherr dazu sagte:
**„this is how it all started“**.

Er deutet auf:
- variable Kapazität,
- Bewegung metallischer Gitter relativ zu Mehrlagenkondensatoren,
- Material-/Gittergeometrie als Kernfaktor.

---

# 24. Replikation des Prinzipversuchs

Im Replikationsdossier wird ein detaillierter Nachbau dokumentiert.

## 24.1 Nachbauabmessungen

Fester Teil:
- Basis ca. 350 × 160 × 5 mm;
- je Block 5 Plexiglasplatten ca. 60 × 90 × 3 mm;
- insgesamt/je Block mehrere Messinggitterlagen, Draht ca. 0,3 mm;
- Ausgangselko 220 µF / 100 V;
- Lager ID ca. 6 mm / OD ca. 19 mm;
- Achse Ø8 mm × 40 mm mit Ø6-mm-Absatz.

Bewegter Balken:
- 270 × 45 × 10 mm;
- 16-mm-Zentralbohrung;
- 2 Plexiglasplatten 60 × 90 × 3 mm;
- 2 Messingnetzlagen 60 × 90 mm, Draht 0,3 mm;
- 2 Aluminium-Gitter 140 × 45 × 0,8 mm, bei 20 mm aufgebogen;
- Löcher Ø2 mm, Lochabstand 4 mm;
- 2 Eisen-Gittersegmente 105 mm, verjüngt 40 → 10 mm;
- quadratische Löcher ca. 5 mm, Teilung ca. 7 mm.

## 24.2 Ergebnis
- nach etwa zehn Schwenkbewegungen **keine Ladung** messbar;
- Vorladung des Elkos auf 30 V + Bewegung: keine Spannungsänderung;
- ohne Kondensator ebenfalls keine elektrostatische Aufladung;
- Epoxid-Leckage als möglicher Versuchsfehler diskutiert;
- viele Gitterlagen teilen Spannung offenbar ähnlich Serienkondensatoren.

Dies ist ein **negatives Replikationsergebnis** für diese konkrete Bauform.

---

# 25. Linden-Experiment

Der Linden-Bericht beschreibt einen anderen, stark vereinfachten Aufbau.

## 25.1 Überlieferter Aufbau
- Hufeisen-Permanentmagnet;
- um die Beine/den Magneten ca. 20–30 Windungen normaler isolierter Installationsleitung (Angabe je nach Skizze);
- Drahtenden galvanisch zu einer Schleife verbunden;
- kleiner „Kondensator“ aus:
  - Aluminiumplatte,
  - Papierisolator,
  - Kupferplatte;
- dieser Stapel wird zwischen die Magnetpole geschoben und auf eine Position mit maximaler Anzeige eingestellt;
- Messgerät am Aufbau.

## 25.2 Behauptete Messung
- etwa 700 V bzw. in verwandten Feldnotizen mehrere hundert Volt;
- ein separater Besucherbericht zur Hauptmaschine nennt ~770 V Leerlauf und ~580 V/ca. 3 A an Heizer.

## 25.3 Reproduzierbarkeit
Entscheidend:
- die ursprünglichen Besucher konnten den Linden-Effekt später **nicht reproduzieren**;
- der Berichtautor selbst konnte keinen verlässlichen Effekt erzeugen;
- die mögliche Messgeräteinstellung, Haut-/Körperkopplung, langsame Entladung und elektrostatische Vorladung werden als Unsicherheiten diskutiert.

Das Linden-Experiment ist daher **kein gesicherter Energieeffekt**, aber eine wichtige Quelle für die Rolle von Hufeisenmagnet + Gitter-/Kondensatorstapel in Baumanns Demonstrationssprache.

---

# 26. HCRS — „Kapazitiver Transformator“

Diese Versuchsreihe ist technisch wertvoll, weil sie einen Teil der Potter/Testatika-Hypothese mit konventioneller HF-Technik untersucht.

## 26.1 Erster Aufbau
- CW-Teslatrafo;
- Versorgung durch ca. 40-W-Mittelwellensender;
- Al-Lochblech als offener Zylinder, ca. 10 cm Durchmesser;
- 230-V/60-W-Lampe zwischen Gitter und Masse;
- Resonanz etwa 1 MHz;
- Lampe kann sehr hell leuchten.

## 26.2 Leistungsanpassung
Vergleich mit 50-Hz-Regeltrafo und Wattmeter:
- optimale Anpassung um ca. 300 Ω;
- bis zu etwa **42 W** an Lampenleistung;
- entspricht im Wesentlichen der Senderleistung, also **keine überschüssige Energie**.

## 26.3 Kapazitives Ersatzmodell
- 12-pF/15-kV-Vakuumkondensator statt Gitter zeigt denselben grundsätzlichen Effekt;
- Interpretation als kapazitiver Spannungsteiler, dessen Blindstrom durch abgestimmte Sekundärspule kompensiert wird.

## 26.4 dokumentierte Spulendaten
Sekundärspule:
- 650 Windungen;
- 0,26-mm-Lackdraht;
- 40-mm-PVC-Rohr;
- ca. 200 mm hoch;
- L ≈ 3,5 mH;
- DC-Widerstand ≈ 27 Ω;
- freie Resonanz ≈ 1,5 MHz;
- mit geerdetem Gitter ≈ 1,13 MHz.

Gitter:
- 1-mm-Aluminium-Lochblech;
- Lochgröße 5 × 5 mm;
- Stegbreite 2,5 mm;
- offener Zylinder ca. 210 mm hoch;
- Durchmesser ca. 105 mm;
- Spalt ca. 5 mm.

## 26.5 Rückwärtige Erregung
- HF nur am Gitter gegen Masse;
- Generator nur ca. 50 V;
- an Teslaspitze etwa 1-cm-Funke;
- Primärspule unbeschaltet.

Das zeigt reale **resonante Impedanz-/Spannungstransformation**, nicht Overunity.

## 26.6 Selbstkritische Korrektur
Der HCRS-Text erkennt später, dass hohe Ströme bereits durch parasitäre Kapazitäten am Teslatrafo fließen und frühere „Transformations“-Deutungen teilweise Arbeitspunkt-/Resonanzeffekte waren. Diese Selbstkorrektur erhöht den technischen Wert der Versuchsreihe.

---

# 27. Rimstar-Testbeds 2005

## 27.1 Testbed 1
- Scheibenwobble zu groß;
- Messung floatinger Spannungen mit Oszilloskop falsch;
- eine Elektrode wurde versehentlich über die Messmasse geerdet;
- Resultate deshalb nicht belastbar.

## 27.2 Testbed 2
Verbessert:
- weniger Wobble;
- bessere Justierbarkeit;
- korrekte Messung floatinger Spannungen.

Ergebnis:
- Scheibe wirkt gegenüber den Gittern als **variables Dielektrikum**;
- Gitter verhalten sich wie **variable Kondensatoren**;
- Ausgang ist Wechselspannung/Impulsfolge;
- elektrisches Verhalten grundsätzlich konsistent.

Aber:
- nur ca. **20–50 mV Impulsspitzen**;
- für moderne Siliziumdiode wurden mindestens ca. 700 mV als praktisch nötig angesehen;
- Versuche, mit Magnet-/Spulenanordnungen nach Tesla-Patent 413,353 eine Gleichrichtung zu erzeugen, scheiterten;
- mechanische Instabilität und Widerstände verhinderten reproduzierbare Amplituden.

**Schluss:** Rimstar unterstützt das variable-kapazitive Frontend, nicht die behauptete Kilowattverstärkung.

---

# 28. Sven Bönisch 2003 — wichtigste kontrollierte technische Replikation

Titel:
**„Electrostatic Discharge Power Transformation – An Approach to Understand the Working Principles of the ‘Thestatika’ Free Energy Device“**, ELEKTRIE No. 5–8/2003.

## 28.1 Methodische Position
Der Autor schreibt ausdrücklich:
- Aufbau basiert auf **bekannten elektrodynamischen Prinzipien**;
- Wirkungsgrad sollte 100 % nicht überschreiten;
- Laborbetrieb mit Handkurbel.

## 28.2 Elektrostatischer Generator
- zwei gegenläufige Scheiben;
- für die Messversion ca. 200 mm Durchmesser;
- 16 Kupfersektoren je Scheibe;
- Standard-FR4, 1,5 mm;
- Kupfer 35 µm;
- Mindestabstand Sektoren ca. 10 mm für bis zu 30 kV;
- Scheibenabstand ca. 5 mm;
- sechs elektrisch verbundene Elektrodenpositionen je Scheibenseite;
- zwei Leydener Flaschen je ca. 140 pF;
- Messingelektroden ca. 30 × 12 mm;
- Spitzen an Elektroden;
- Elektrodenabstand zur Scheibe ca. 1 mm, einstellbar;
- anfängliche Vorladung mindestens +10 kV an einer Leydener Flasche.

Der Autor betont:
- HV1/HV2 sind in seinem Aufbau **nicht einfach DC**;
- einzelne Überschläge erzeugen hochfrequente Oszillationspakete;
- mechanische Arbeit ist für Influenzladung erforderlich.

## 28.3 HF-Transformationsstufe
- Pulsformungs-/Resonanznetzwerk;
- Zielresonanz zunächst ca. 80 MHz;
- L1/L2: je 7 Windungen Lackdraht;
- RG-58-Leitung T3, ca. 1,20 m;
- zylindrische Luftkondensatoren C1/C2:
  - aktive Höhe 100 mm,
  - Innenstab Ø4 mm,
  - Außenelektrode Ø28 mm;
- helical transmission line:
  - perforiertes Al, ca. 0,8 mm dick, 100 mm breit;
  - etwa 10 mm Luft-/Schaum-Abstand zwischen Lagen;
  - elektrische Länge ca. 910 mm;
  - charakteristische Impedanz ca. 16 Ω;
  - Spannungsfestigkeit ca. 15 kV;
- Last: 12-V/21-W-Autolampe.

## 28.4 Gemessene Resonanz
- ursprüngliche Leitungsresonanz ca. 80 MHz;
- gesamtes belastetes System abgestimmt auf ca. **53 MHz**.

## 28.5 Betriebsmessung
- Scheiben ca. 10 Umdrehungen/s;
- ca. 30 kV äquivalente Generator-Hochspannung;
- Entladungs-/Paketwiederholung unregelmäßig ca. **100–400 Hz**;
- mittlere Lastleistung ca. **10 mW**;
- theoretisch erwartete Generatorleistung ca. **80 mW**.

## 28.6 Schluss des Autors
- Energieerhaltung wird erfüllt;
- **kein Overunity-Effekt detektiert**;
- echte Testatika könnte anders aufgebaut sein.

Dies ist die stärkste im Korpus enthaltene Gegeninformation gegen die Annahme, dass bereits bekannte Scheiben-/HF-Kopplungsprinzipien automatisch Kilowattüberschuss erzeugen.

---

# 29. Don-Kelly-Modell

Die Marinov-Scans enthalten einen Don-Kelly-Artikel mit sekundärer Gesamtschaltung.

Kelly ordnet der Maschine zu:
- gegenläufige Wimshurst-artige Scheiben;
- Stahlsegmente;
- Kollektorbürsten;
- Hufeisenmagnete/Spulen;
- Crystal-Diode/Kondensator;
- Leydener „Transmitter“ und „Receiver“;
- drei miteinander gekoppelte Kreise.

Er nennt/übernimmt u. a.:
- ca. 300 V × 10 A = 3 kW;
- 60 rpm;
- Abmessungen etwa 43,3 × 17,7 × 23,6 inch;
- Gewicht ca. 44 lb.

Er vergleicht das Gerät mit Poggendorff-, Searl-, Ecklin- und Cole-Effekten. Diese Funktionsverknüpfungen sind **sekundäre Theorie**, nicht direkte Maschinenbeobachtung.

Besonders wichtig ist Kellys eigener Vorbehalt:
Die vollständige Arbeitsweise sei nur Baumann und eventuell wenigen engen Mitarbeitern bekannt; Hauser, Marinov, Kelly und andere Forscher hätten **nicht das vollständige Bild**.

---

# 30. Paul E. Potter — Back-Engineering: wertvoll, aber strikt von Beobachtung trennen

Potters Korpus ist umfangreich und enthält viele detaillierte technische Ideen. Er ist nützlich, weil er:
- Fotos vergleicht;
- Elektrodengeometrie systematisiert;
- klassische Influenzmaschinen heranzieht;
- plausible Ersatzschaltungen formuliert.

Aber viele Details sind **explizit rekonstruiert**.

## 30.1 Pidgeon statt reine Wimshurst
Potter sieht stärkere Ähnlichkeit zu einer Pidgeon-Influenzmaschine (1898):
- perforierte/korrugierte Sektoren;
- spezielle Neutralisator-/Feldelektroden;
- berührungslose Ladungssammlung.

Diese historische Analogie ist plausibel, aber keine Originalaussage Baumanns.

## 30.2 „Antenna keys“
Potter interpretiert die nichtberührenden perforierten Sammler als variable Kapazitäts-/Feldelektroden.

Dies wird durch Rimstar qualitativ gestützt.

## 30.3 Oberes „Rectifier“-Teil
Potter spekuliert über:
- thermionischen Gleichrichter;
- Vakuumröhre;
- Pearson-Anson-artige R/C/Ventil-Oszillation;
- Barkhausen-Kurz-artige HF-Funktion.

Keines davon ist als Originalfunktion bestätigt.

## 30.4 Rückseitige lange Rohre
Potter interpretiert sie als:
- Drosseln/Chokes;
- Teil eines HF-LC-Netzwerks;
- mit äußerer elektrostatischer Abschirmung.

Hauser beobachtete lediglich Rohr + Aluminiumspan und ordnete sie dem Scheibenantrieb zu.

## 30.5 „Electron cascade generator“
Potter bringt die Hufeisen-/Schichtbaugruppe mit Flanagan-artigen Elektronenlawinen-/Dielektrikumsystemen in Verbindung. Dies bleibt Hypothese.

## 30.6 Große Pots
Potters Schnittbild mit:
- Pancake-Coils,
- Ringmagneten,
- Gitterkondensatoren,
- PFN-/Delay-Line-Analogie

ist eine Rekonstruktionsfamilie, keine gesicherte Originalzeichnung.

## 30.7 Wichtigste korrekte Verwendung Potters
Potter ist am nützlichsten als **Hypothesenkatalog und geometrische Vergleichsanalyse**, nicht als Quelle für „so war die Maschine innen definitiv gebaut“.

---

# 31. Marinov — besonders wichtige Gegenstimme innerhalb der Befürworter

Marinov war von der Existenz einer Energieanomalie überzeugt und ist daher **kein skeptischer Gegenzeuge**. Gerade deshalb haben seine technischen Korrekturen besonderes Gewicht. Seit Version 5.0 wird zwischen dem kurzen Archivscan `marinov.pdf` und dem wesentlich umfangreicheren Originalband *The Thorny Way of Truth, Part V* (1989) unterschieden.

## 31.1 Quellenwert von Marinov
Marinov gibt selbst eine ungewöhnlich klare Grenze seiner Kenntnis an:
- Er besuchte Methernitha im Juli 1988 und im Februar/März 1989.
- Beim zweiten Besuch beobachtete und berührte/testete er **eine kleine Maschine** mit etwa 20-cm-Scheibe; eine zweite kleine Maschine sah er ebenfalls.
- Die mittlere Maschine mit zwei etwa 50-cm-Gegenscheiben sah er **nur im Film**.
- Von der großen, damals im Bau befindlichen Maschine mit etwa 100-cm-Scheiben sah er **einzelne Bauteile**, nicht eine vollständig laufende Gesamtmaschine.
- Er schreibt ausdrücklich, dass er das Prinzip **nicht verstanden** habe, die Maschine **nicht rekonstruieren** könne und weder einen exakten Schaltplan noch eine klare Erklärung besitze.

Damit gilt für Version 5.0:
- direkte Angaben zur kleinen Maschine: **E1 / relativ hoher Quellenwert für Geometrie und Verhalten**;
- Angaben zur mittleren Maschine: **E2 / Filmbeobachtung**;
- Angaben zu geöffneten Einzelbauteilen der großen Maschine: **E1/E2, lokal stark, systemisch begrenzt**;
- Leistungsangaben und Overunity-Schlussfolgerungen: **nicht als Messprotokoll verwertbar**;
- Marinovs theoretische Deutung: **Hypothese, nicht Beobachtung**.

## 31.2 Wichtigste technische Korrekturen aus Part V
Marinov schreibt bzw. beobachtet:
- kleine Maschine: kein äußerer Motor in der von ihm getesteten Variante; Start durch mehrere Fingerstöße, danach elektrostatisches Drehmoment;
- keine schleifenden „collection brushes“: die Platten sind **berührungslose Elektroden**;
- ursprüngliche kleine Maschinen: etwa 20–30 radiale **Kupferdrähte**, nicht zwingend magnetisierte Stahl-Lamellen;
- Magnete fehlen bei mindestens einer kleinen Variante, daher nicht universelles Grundprinzip;
- geöffnete große Seitenmodule: nach Marinov **einfache Kondensatoren** mit äußerer zylindrischer Elektrode und innerer Elektrode aus dicker Kupferdraht-Spirale;
- Marinov widerspricht einer absichtlichen Tesla-/HF-Interpretation ausdrücklich: nach seiner Beobachtung **keine Tesla-Transformatoren, kein bewusstes AC/HF-System**;
- Baumann sprach gegenüber Marinov von einem **„crystal“**; Marinov erwägt als mögliche Funktion ein einseitiges Ladungsventil, kennt das Bauteil aber nicht;
- die 50-Europe/60-USA-Deutung der Segmentzahl weist Marinov zurück, weil die Maschine DC liefert und kleine Maschinen nur etwa 20–30 Drähte besitzen;
- seine eigene Hauptdeutung: elektrostatischer Holtz/Poggendorff/Gruel-Motor + Influenzgenerator; möglicherweise getrennte Hochspannungs-„Driving“- und niedrigere Spannungs-„Collecting“-Kreise.

## 31.3 Wichtige Selbstkorrektur gegenüber Internetrekonstruktionen
In einem später im selben Band abgedruckten Brief korrigiert Marinov fremde Testatika-Darstellungen ausdrücklich:
- kein Solid-State-Amplifier;
- kein Transformer-Amplifier;
- **keine Tesla-artigen Transformatoren**;
- 50/60 Segmentzahl nicht als Netzfrequenzlogik;
- Kondensatorform zwar ungewöhnlich, Zweck unbekannt;
- für reine Rotation könnten laut Marinov etwa **80 % der übrigen Bauteile entfernt** werden;
- das Grundgeheimnis sei einfach, aber er kenne es nicht.

Die vollständige Part-V-Auswertung und wissenschaftliche Neugewichtung steht in den Abschnitten 75–91.

# 32. Späte Web-Kompilationen und Hearsay

`swiss Testakica free energy device.mht`, die tschechische Kopie und `testatika1.doc` sammeln:
- Hauser/Marinov/Methernitha-Texte;
- spätere E-Mails;
- Replikationshypothesen;
- teils spekulative Radium-/ZPE-Erklärungen.

Wert:
- gut zum Auffinden von Widersprüchen;
- schlecht als unabhängige Evidenz, weil zahlreiche Quellen zirkulär voneinander abschreiben.

### 32.1 Radium-Hypothese
Webtexte spekulieren über radiumdotierte Kondensatoren.

Gegeninformation:
- Holzherr fragte Baumann 1999 ausdrücklich, ob Radiumchlorid die Energiequelle sei;
- Antwort laut Holzherr: **definitiv NEIN**.

Es gibt im Korpus **keinen materiellen Nachweis** radioaktiver Bestandteile. Radium ist daher nicht Bestandteil des belastbaren Testatika-Modells.

### 32.2 Mike-Watson/Marinov-Hearsay
Später Bericht:
- kleines Modell mit einer Scheibe;
- Eisen-Drahtsektoren von einer Scheibenseite zur anderen „gewebt“;
- Seitenpots ohne Magnete;
- Achse müsse angeblich Ost-West liegen;
- Metallplatte hinter Gerät stoppe Rotation;
- geschätzte ~100 W anhand Widerstandserwärmung, aber **keine Instrumente**.

Diese Angaben sind interessant, aber mehrfach vermittelt und daher **H/E3**.

---

# 33. Der russische „GCT“-Entwurf

`testatika russ.pdf` und identisches Duplikat beschreiben einen von A. N. Burenkov vorgeschlagenen variablen Kapazitätsgenerator, nicht die Original-Testatika.

Merkmale:
- radial segmentierter Rotor/Stator;
- HV-Vorspannung;
- Motor;
- Transformator/Gleichrichter;
- 60 Platten bei 1 U/s → 60 Hz;
- alternativ 50 Platten bzw. 0,83 U/s → 50 Hz;
- große berechnete Leistungsangaben.

Kritik:
Die Berechnung behandelt die Änderung der Kapazität/Rotation zu günstig und berücksichtigt elektrostatisches Gegenmoment bzw. vollständige mechanische Energiebilanz nicht angemessen.

Nutzen für Testatika:
- zeigt, dass die **Segmentzahl-Frequenz-Idee** unabhängig als Rekonstruktionsgedanke existiert;
- ist **kein Beweis**, dass Baumanns Maschine so arbeitete.

---

# 34. Hyde-Generator — Vergleich aus den Nutzer-Buchseiten

Die Buchseiten 117/118/124 vergleichen Testatika mit einem Generator nach William W. Hyde.

## 34.1 Hyde-Grundprinzip laut Buch
- externe Hochspannungs-/Feldaufladung;
- stationäre Feldplatten;
- rotierende Abschirmsegmente;
- zyklische Änderung der Feldkopplung;
- Statorsegmente;
- Kondensator-/Diodennetzwerk;
- Motorantrieb;
- im Buch für eine Ausführung **>6000 U/min**.

Physikalisch ist dies eine variable elektrostatische Maschine:
\[
C=C(t),\quad Q=C\,V,\quad i=rac{dQ}{dt}
\]

Mechanische Arbeit gegen elektrostatische Kräfte wird in elektrische Energie umgewandelt.

## 34.2 Buchvergleich Testatika ↔ Hyde
Die Seite 124 ordnet hypothetisch zu:
- Testatika-Scheibensegmente ↔ Hyde-Rotor;
- „antenna keys“ ↔ Hyde-Stator;
- Gitter hinter Scheibe ↔ HV-Feldplatten;
- Testatika-Pots ↔ Kondensator-/Dioden-Puffer.

Dieser Vergleich ist **eine spätere Interpretationshilfe**, kein Nachweis identischer Schaltung.

## 34.3 Wichtiger Unterschied
- Hyde im Buch: >6000 rpm;
- Testatika: ca. 15–60 rpm.

Daher kann Hyde höchstens einen **Teilmechanismus der Feldmodulation**, nicht die gesamte Testatika erklären.

---

# 35. Buchseite 94 — Kelly-artiges Gesamtschema

Die Seite zeigt:
- rotierende Scheibe;
- Kollektorbürsten;
- Hinweis „Brushes do not touch here“;
- zwei Hufeisenmagnete;
- `Crystal diode / Capacitor` zwischen N/S;
- Leydener Flaschen `Transmitter` und `Receiver`;
- Plus-/Minus-Ausgang;
- rote/blaue Ladungspfade.

Dieses Schema ist als **sekundäres Funktionsmodell** zu behandeln, nicht als Originalverdrahtung.

---

# 36. Buchseite 106 — „Vermuteter Innenaufbau der grossen Kondensatoren“

Die Überschrift ist entscheidend: **vermutet**.

Gezeigt werden:
- zentraler Zylinder;
- gestapelte/verschachtelte Flachspulen;
- primäre und sekundäre Wicklungen;
- etwa sechs hohle Ringmagnete;
- Plastikabstandshalter und Luftspalte;
- perforierter Aluminium-Außenzylinder als elektrostatische Abschirmung;
- Kupferblech zur magnetischen Flussabschirmung;
- `secondary output`;
- `high tension insulation`;
- Gitterkondensator-/Pulsformungsstruktur.

Diese Seite ist in `state.md` nur als **Potter-/Sekundärrekonstruktion** zu verwenden.

---

# 37. Buchseite 109 — rekonstruierter Gesamtaufbau

Gezeigt:
- `antenna keys`;
- `HT lead`;
- `collectors`;
- Endbehälter/Leydener Flaschen;
- `induction coil`;
- `magnet and reed switch`;
- `brass pulley`;
- Aluminiumzylinder;
- zentrale `Mutual Induction Coil (M2)`;
- bifilar/close-coupled winding;
- ein als `electron avalanche generator` interpretierter Bereich.

Auch dies ist eine **Rekonstruktionsgrafik**, nicht eine verifizierte Originalschaltung.

---

# 38. Buchseiten 87/88 — Hauser-Wiedergabe und Abweichungen

Die Buchseite 87 reproduziert eine interpretierte Übersicht:
- `Twin Wimshurst Discs`;
- Collection Brushes +/−;
- `Magnetic Stainless Steel Disc Segments ... (50 for Europe) (60 for U.S.)`;
- „Tesla Coil Windings“;
- `Centerline Capacitor`;
- Hufeisenmagnete und magnetische Wicklungen;
- linke/rechte kapazitive/Transformationsmodule.

Die Buchseite 88 reproduziert Hausers Zeichnung Nr. 3279 und Textpositionen.

**Wichtige Abweichung:** Buchseite 88 gibt die Lamellenlänge als 60 mm wieder; Hausers Originalbericht sagt 160 mm. Für die Wissensbasis ist deshalb die Primärquelle mit dokumentiertem Konflikt maßgeblich.

---

# 39. Videoquellen

## 39.1 Metadaten
- `meth1.asf`: 153,936 s, 320×240, 25 fps
- `meth2.asf`: 114,118 s, 320×240, 25 fps
- `meth3.asf`: 125,918 s, 320×240, 25 fps
- `meth4.asf`: 100,286 s, 320×240, 25 fps
- `meth5.asf`: 195,686 s, 320×240, 25 fps
- `testa01.ram`: 318,957 s, 352×288, 25 fps
- `testa02.ram`: 317,041 s, 352×288, 25 fps
- `testatikadeutsch.wmv`: 114,118 s, 320×240, 25 fps

`meth2.asf` und `testatikadeutsch.wmv` haben identische Dauer und weitgehend gleiche Bildfolge; vermutlich Sprach-/Container-Varianten.

## 39.2 Visuell erkannte Inhalte
`meth1`:
- historische Elektrostatik-/Funken-Demonstrationen;
- kleine Geräte;
- größere Testatika;
- Gemeinschaft/Workshop-Kontext.

`meth2` / `testatikadeutsch`:
- Frontansicht größerer Testatika;
- enge Nahaufnahmen perforierter rechteckiger Elektroden;
- obere Rohr-/Gitterbaugruppen;
- zentrale untere Wicklungs-/Topfbereiche.

`meth3`:
- Scheiben-/Seitennahaufnahmen;
- lange perforierte Vertikalmodule;
- Demonstrationsinteraktion.

`meth4`:
- zentrale Nabe;
- Frontgitter;
- untere Baugruppe;
- analoge Messgeräte.

`meth5`:
- Sanwa-ZX-505-Messgeräte sichtbar;
- Maschine;
- Last-/Glühlampendemonstration mit leuchtender Lampe;
- aus dem Video allein keine geschlossene Input-/Output-Leistungsbilanz ableitbar.

`testa01`/`testa02`:
- Werkstatt-/Montageaufnahmen einer sehr großen „Elephant“-artigen Maschine;
- große Scheibe und Strukturteile;
- belegen Bau/Existenz eines Großprototyps, nicht dessen behauptete Ausgangsleistung.

---

# 40. Kontrollierte und halbkontrollierte Replikationen — Gesamtergebnis

| Replikation | Was reproduziert wurde | Ergebnis |
|---|---|---|
| Holzherr-Nachbau 50-cm nach Literatur | optische/klassische Testatika-Form | nicht selbstlaufend |
| Prinzipversuch-Nachbau | Gitter/Plexi-Schwenkarm | keine Ladung, auch bei 30-V-Vorladung keine Änderung |
| Linden-Versuche | Magnet + Schleife + Al/Papier/Cu | ursprünglicher Effekt nicht reproduzierbar |
| HCRS kapazitiver Transformator | Tesla + perforiertes Gitter | starke Resonanz-/Impedanztransformation; Leistung entspricht Quelle |
| Rimstar Testbed 1 | kleine Scheibe/Gitter | Messfehler durch Massebezug/Wobble |
| Rimstar Testbed 2 | variable Dielektrikums-/Gitterkopplung | AC-Impulse 20–50 mV; keine nutzbare Gleichrichtung/Leistungssteigerung |
| Bönisch 2003 | brushless E-Generator + HF-Transformer | ~10 mW Last, ~80 mW Generator-Theorie; Energieerhaltung, kein Overunity |

**Kernbefund:** Mehrere Teilphänomene sind konventionell reproduzierbar — Influenz, variable Kapazität, HF-Resonanz, kapazitive Transformation. Der behauptete Energieüberschuss wurde in den technisch dokumentierten Replikationen **nicht reproduziert**.

---

# 41. Electret-Hypothese

Der Korpus enthält:
- Bernhard-Gross-Electret-Material;
- Eguchi-Historie;
- Potter-Electret-Seiten;
- Hinweise auf dielektrische Absorption/Polarisation.

Reale Physik:
- permanente/quasipermanente Polarisation in Dielektrika;
- Oberflächen-/Raumladung;
- lange Relaxationszeiten;
- dielektrische Absorption.

Aber:
- kein eindeutiger Nachweis, dass originale Testatika-Platten als präparierte Electrete fungierten;
- Holzherrs Bemerkung zur möglichen „molecular orientation“ ist Hearsay/Interpretation;
- ein Electret wäre ein gespeicherter Polarisationszustand, keine unbegrenzte Energiequelle.

Status: **plausible Material-/Bias-Hypothese, nicht belegt**.

---

# 42. Elektronenlawinen-/Flanagan-Hypothese

Potter und das Replikationsdossier diskutieren:
- dielektrische Schichten mit leitenden/halbleitenden Partikeln;
- HF/HV-Anregung;
- „electron cascade“;
- Flanagan-artige Patent-/Versuchsparameter.

Diese Materialien sind **benachbarte Theoriequellen**, nicht direkte Testatika-Beobachtung. Selbst reale Lawinen-/Ionisationsvorgänge würden vorhandene Feldenergie umsetzen, nicht ohne Input neue Energie erzeugen.

Status: **H**.

---

# 43. Unipolar-Generator-Folien, Luzern 2005

29 Folien „Unipolar-Generatoren“, Chr. Monstein, 15.10.2005:
- N-/C-Generator-Varianten;
- Ringmagnete, Cu/C-Kontakte;
- Messungen von Spannung, Strom, Reibung und mechanischer Leistung;
- Abschlusswerte zeigen COP deutlich unter 1 (je nach Konfiguration etwa Größenordnung 0,1 oder deutlich kleiner).

Diese Folien liefern **keine Testatika-Konstruktionsdetails**, sind aber methodisch wichtig:
- magnetische/unipolare Generatoren müssen über mechanische Gegenkräfte bilanziert werden;
- reine Ausgangsspannung ohne Drehmomentmessung ist keine Energieanalyse.

---

# 44. Konventionelle elektrodynamische Synthese

## 44.1 Variable Kapazität
\[
C=arepsilon rac{A}{d}
\]

Durch rotierende Metall-/Dielektrikumssegmente ändern sich:
- effektive Überdeckungsfläche \(A\),
- effektive Permittivität \(arepsilon\),
- Feldlinienweg/Abstand \(d\).

## 44.2 Strom bei zeitabhängiger Kapazität
\[
Q=C\,V
\]
\[
i=rac{dQ}{dt}=Vrac{dC}{dt}+Crac{dV}{dt}
\]

Das erklärt, warum selbst **nichtkontaktierende** Elektroden Wechsel-/Impulsströme erhalten können.

## 44.3 Energie
\[
E_C=rac12 C V^2
\]

Wird \(C\) mechanisch verändert, treten elektrostatische Kräfte und Gegenmoment auf. Die mechanische Arbeit muss in einer Energiebilanz erfasst werden.

## 44.4 Funken-/Koronaimpulse
Hohe Sektorpotentiale können:
- lokale Überschläge;
- ns–µs-Impulse;
- breite HF-Spektren

erzeugen. Bönisch zeigt, dass solche Impulse Resonanznetzwerke anregen können.

## 44.5 Gitter
Perforiertes Metall kann:
- Wirbelströme gegenüber Vollblech reduzieren;
- gleichzeitig kapazitive Feldkopplung ermöglichen;
- verteilte Induktivität/Kapazität erzeugen;
- Korona-/Feldverteilung beeinflussen.

Das erklärt, warum Lochblech technisch sinnvoll sein kann, ohne exotische Energiequelle.

---

# 45. Wahrscheinlichste Funktionsarchitektur — nach Evidenz gestuft (V5)

## Stufe A — elektrostatischer Motor-/Influenzkern (**hoch**)
- je nach Modell eine oder zwei segmentierte/verdrahtete Scheiben;
- bei mittleren/großen Varianten Gegenrotation;
- elektrostatische Ladungstrennung und Selbstverstärkung nach Influenzprinzip;
- keine schleifenden Scheibenbürsten in den von Marinov/Hauser beschriebenen Testatika-Ausführungen;
- nichtkontaktierende Elektroden erzeugen/sammeln Ladung und können zugleich Drehmoment beitragen.

## Stufe B — zeitabhängige Feld-/Kapazitätskopplung (**hoch bis mittel**)
- perforierte oder flächige Elektroden/Gitter;
- Scheibe/Sektoren verändern Feldgeometrie, Ladungsverteilung und wirksame Kapazitäten;
- daraus entstehen Ladungsverschiebungen und ggf. Impulse/Transienten;
- **ein absichtliches internes AC-/HF-System ist nicht belegt**. Moderne Replikationen können Ringing/HF zeigen, das darf nicht rückwirkend als Originalprinzip gesetzt werden.

## Stufe C — zwei Potential-/Speicherfamilien (**mittel; Marinov-Hypothese + Geometrie**)
- Hochspannungszweig für „driving electrodes“ denkbar;
- niedrigere Spannung/größere Kapazität auf der Sammel-/Nutzseite denkbar;
- linke/rechte Kondensator-/Pot-Strukturen;
- Marinov vermutet beide Kondensatorgruppen würden durch die Maschine selbst geladen; die konkrete Verdrahtung fehlt.

## Stufe D — Kondensator-/Kopplungsnachstufe (**hoch für Existenz, niedrig für genaue Funktion**)
- große seitliche Pos.-6-/Pot-Baugruppen;
- Hauser beschreibt bei einer größeren Variante drei konzentrische Gitter, Acryl, Magnettube und bifilare Wicklung;
- Marinov sah bei der großen Maschine geöffnete Seitenbauteile und beschreibt dort äußere Zylinderelektrode + innere dicke Kupferspiral-Elektrode und **keinen absichtlichen Tesla-Transformator**;
- Varianten dürfen nicht zu einem einzigen Innenaufbau verschmolzen werden.

## Stufe E — asymmetrischer Ladungspfad / Crystal / Gleichrichtung (**mittel**)
- „crystal“ direkt von Baumann gegenüber Marinov erwähnt;
- Hauser nennt Pos. 12 möglicherweise `RECTIFIER`;
- plausible Minimalfunktion: einseitige Ladungsübertragung, Rückstromsperre, Schwellen-/Clamp-Funktion;
- Material, I-V-Kennlinie und genaue Knoten unbekannt.

## Stufe F — DC-Puffer/Ausgang (**DC-Beschreibung mittel bis hoch; Kilowattwert niedrig/unverifiziert**)
- Betreiber und mehrere Beobachter beschreiben Gleichspannung/Gleichstrom;
- zwei Ausgangspole und Lastdemonstrationen sind dokumentiert;
- eine geschlossene Input-/Output-Energiebilanz fehlt.

# 46. Widerspruchsmatrix

| Thema | Quelle A | Quelle B | belastbarste Auflösung |
|---|---|---|---|
| Antrieb | Methernitha/Marinov: selbstlaufend elektrostatisch | Hauser: große Maschine kleiner DC-Motor | modellabhängig; nicht einheitlich |
| Drehzahl | Hauser ~60 rpm | Holzherr ~15 rpm | verschiedene Zeitpunkte/Betriebszustände |
| Magnete | größere Modelle klar mit Magneten | Marinov kleines Modell: keine | modellabhängig |
| Tesla-Spulen/HF | Kelly/Potter/Buchzeichnung + spätere Replikationen | Marinov sah geöffnete große Seitenkondensatoren und korrigiert ausdrücklich: keine Tesla-artigen Transformatoren, kein AC | **absichtliches HF/Tesla-Originalprinzip stark herabgestuft**; parasitäres/ringendes Verhalten bleibt physikalisch möglich |
| Pos.-6-Innenleben | Hauser: 3 Gitter + Acryl + Magnettube + bifilar 18 AWG | Marinov klein: Gitter + Kunststoff + Kupferspirale ohne Magnet | Varianten; nicht zusammenmischen |
| Pos.-6-Innenleben 2 | Potter: Pancakes + 6 Ringmagnete | spätes Hearsay: Al-Drehspäne | beides unbestätigt |
| Top-Bauteil | Hauser: möglicherweise Rectifier + Crystal | Marinov: Baumann sagte nur Crystal; Potter: Vakuumröhre; Hearsay: Solenoid | Funktion ungeklärt |
| 50/60 Hz | Hauser-/Interpretationsnotiz 50 Europe/60 US | Marinov nennt diese Deutung ausdrücklich unsinnig; kleine Geräte 20–30 Drähte, DC-Ausgang | **als Grundprinzip stark herabgestuft**; höchstens modell-/konstruktionsspezifische Segmentzahl |
| Radium | Web-Spekulation | Baumann laut Holzherr: klares Nein | keine Evidenz für Radium |
| Ausgang | 130 V / 270–320 V / 300 V / 580–770 V | unterschiedliche Modelle/Lastzustände | nicht auf einen einzigen Nennwert reduzieren |
| Leistung | 1 kW / 3 kW / 3–4 kW / 30 kW projektiert | kontrollierte Replikationen mW–Quellleistung | hohe Werte unbestätigte Originalclaims/Demos |
| Frequenz intern | Marinov: kein AC | Bönisch/Potter: HF-Pulse plausibel | moderne Rekonstruktion kann HF nutzen; Originalfrequenz unbekannt |

---

# 47. Was für eine originalgetreue Rekonstruktion noch fehlt

## 47.1 Scheiben
- exakte Sektorform jeder Modellvariante;
- exakter Radius innen/außen;
- Stahllegierung;
- Magnetisierung;
- Oberflächenbeschichtung;
- elektrische Verbindung einzelner Sektoren;
- Scheibenabstand;
- relative Phasenlage der beiden Scheiben.

## 47.2 Elektroden
- exakte Anzahl vorne/hinten je Modell;
- Winkelpositionen;
- Abstände zur Scheibe;
- Material/Lochbild;
- welche Elektroden miteinander verbunden sind;
- Neutralisator-/Influenzpfade.

## 47.3 Pos. 6
- reale Anzahl Gitterlagen;
- Magnettyp/Polung;
- Windungszahl, Drahtdurchmesser, Verschaltung;
- ggf. Pancake-Coils ja/nein;
- interne Kapazitäten;
- Verbindung des mittleren Gitters zum Ausgang;
- Variation zwischen Modellen.

## 47.4 Pos. 9
- Spiralabmessungen;
- Material;
- Kapazität/Induktivität;
- externe Abschirmung;
- genaue Funktion im Scheibenantrieb.

## 47.5 Pos. 10/11
- Magnetmaterial/Feldstärke;
- Wicklungszahlen und Richtung;
- Schichtfolge zwischen Polen;
- elektrische Einbindung.

## 47.6 Pos. 12
- Kristallmaterial;
- mechanischer Aufbau;
- Vakuum ja/nein;
- Anschlusszahl;
- Gleichrichter-, Oszillator- oder Regelrolle.

## 47.7 Ausgang
- DC-Welligkeit;
- Strom-/Spannungsverlauf;
- Ausgangsimpedanz;
- Schutz-/Entladewiderstände;
- reale Lastkennlinie;
- vollständige Inputleistungsbilanz.

---

# 48. Anforderungen an eine wissenschaftlich brauchbare Replikation

Eine moderne Replikation muss **zuerst Teilfunktionen messen**, nicht sofort ein Kilowattgerät bauen.

## 48.1 Mechanik
- Drehzahl \(n(t)\);
- Drehmoment \(	au(t)\);
- mechanische Leistung:
\[
P_{mech}=	au\omega
\]
- Lager-/Luftreibung separat.

## 48.2 Elektrostatik
- HV-Differenztastköpfe mit definierter Eingangs-C;
- potentialfreie Messung;
- Feldmühle/Elektrometer bei Bedarf;
- keine Oszilloskop-Erde unbemerkt an floating Knoten.

## 48.3 HF
- Bandbreite ausreichend für Entladungspulse;
- Stromsonden/Rogowski;
- zeitgleiche \(u(t)\) und \(i(t)\);
- Wirkleistung:
\[
P_{avg}=rac1T\int_0^T u(t)i(t)\,dt
\]

## 48.4 Speicherenergie
Vor-/Nachenergie aller Kondensatoren:
\[
E=rac12CV^2
\]

## 48.5 Kalorimetrie
Bei behaupteten kW-Werten:
- definierter ohmscher Lastwiderstand oder Wasserlast;
- Temperatur, Masse, Zeit;
- unabhängig zur elektrischen Messung.

## 48.6 Blindleistungsfalle
Bei HF/Resonanz niemals:
\[
U_{RMS}	imes I_{RMS}
\]
ohne Phasen-/Zeitinformation automatisch als Wirkleistung interpretieren.

---

# 49. Sicherheitsstatus

Die Original-/Rekonstruktionsquellen enthalten:
- mehrere 10 kV bis möglicherweise >30 kV;
- Leydener Flaschen;
- Funkenstrecken;
- HF;
- rotierende Scheiben;
- möglicherweise große gespeicherte Energie.

Gefahren:
- tödlicher Stromschlag;
- HF-Verbrennungen;
- Lichtbogen;
- Ozon/NOx;
- Brand;
- unkontrollierte Kondensatorentladung;
- Scheibenbruch;
- Messgerätezerstörung;
- ungewollte Erdpfade.

Eine mechanisch/elektrostatische Demonstrationsreplikation sollte deshalb zunächst im energiearmen Bereich bleiben. Kilowatt-/Netzspannungsaufbauten gehören nicht in einen ungeschützten Heimversuch.

---

# 50. Endbewertung des Wissensstands

## Sehr hohe Sicherheit
- mehrere Testatika-Varianten existierten und wurden fotografiert/gefilmt;
- zentrale elektrostatische Scheiben-/Gitterarchitektur;
- gegenläufige 50-cm-Scheiben;
- nichtkontaktierende Elektroden;
- perforierte Metallgitter als dominantes Konstruktionsmotiv;
- große Seitenzylinder;
- Magnet-/Wicklungsbaugruppen bei mehreren größeren Geräten;
- DC-Ausgang wurde von Betreibern/Beobachtern als solcher beschrieben.

## Hohe bis mittlere Sicherheit
- 500-mm-/5-mm-Scheibenangabe;
- 50 Lamellen;
- 60-rpm-Regelziel in einer Hauser-Variante;
- 15 rpm bei 1999-Demo;
- Pos.-6-Grundbeschreibung nach Hauser;
- 20 Gitterlagen in großen Kondensatoren laut Baumann/Holzherr;
- Modellabhängigkeit der Magnetik.

## Mittlere bis niedrige Sicherheit
- genaue elektrische Funktion der Pos. 6/9/10/12;
- beabsichtigte 50/60-Hz-Segmentierung;
- internes HF-Resonanzsystem;
- Tesla-Spulencharakter.

## Nicht verifiziert
- 1–4 kW Nettoleistung ohne entsprechende Energiezufuhr;
- 30-kW-Elephant-Leistung;
- Overunity;
- ZPE-/Radium-/„freie Energie“-Quelle;
- irgendeine spezifische exotische Energiephysik.

**Professioneller Arbeitskonsens für weitere Entwicklung (V5):**  
Die Testatika sollte primär als **elektrostatischer Motor-/Influenzgenerator mit berührungsloser Ladungsübertragung und unbekannter, modellabhängiger Kondensator-/Kopplungsnachstufe** untersucht werden. Eine absichtliche Tesla-/HF-Resonanzarchitektur ist nach Marinov Part V nicht mehr die bevorzugte Originalhypothese. Magnetische/bifilare Zusatzstufen sind für einige größere Modelle gut dokumentiert, aber nicht für das primitive Grundprinzip erforderlich. Die Originaldaten reichen nicht aus, eine sicher funktionierende Kilowattmaschine exakt zu reproduzieren. Sie reichen jedoch für präzise Experimente an Elektroden, Kondensatorgeometrie, Ladungspfaden und Drehmoment.

---


---

# 51. Vertiefte Kernanalyse: Wo kann die eigentliche Umwandlungsfunktion liegen?

Diese Version 4.0 konzentriert sich auf die Frage, welche Funktion **nach** dem gut belegten elektrostatischen Scheiben-/Gitter-Frontend stattfinden müsste, damit die beobachtete Architektur als Ganzes technisch Sinn ergibt.

Die wichtigste methodische Trennung lautet:

- **Scheiben/Gitter:** relativ gut verstanden und mit konventioneller Elektrostatik erklärbar.
- **Pos. 6/7/8/9/10/12:** deutlich schlechter dokumentiert; hier liegt die eigentliche Rekonstruktionslücke.
- **behauptete Kilowattleistung:** nicht durch eine geschlossene Energiebilanz bestätigt.

## 51.1 Neue Rangfolge der Funktionsblöcke

Nach erneuter Prüfung sämtlicher einschlägiger Quellen ist folgende Reihenfolge derzeit am konsistentesten:

### Block A — langsamer elektrostatischer Feld-/Ladungsmodulator
**Evidenz: hoch**

- eine oder zwei segmentierte Scheiben;
- bei der Referenzmaschine gegenläufig;
- nichtkontaktierende perforierte Elektroden;
- langsame mechanische Drehung;
- bipolarer Ladungsaufbau;
- variable Kapazität/Feldüberdeckung.

### Block B — Ladungssortierung und bipolare Pufferung
**Evidenz: hoch bis mittel**

- Plus-/Minus-Zweige;
- Gitter-/Leydener-Kondensatoren;
- Pos. 7/8 als kleinere Zusatzkondensatoren;
- große Pos.-6-Zylinder als Speicher-/Kopplungselemente.

### Block C — Impuls-/Phasen-/Impedanzumwandlung
**Evidenz für Existenz: mittel; Topologie: niedrig**

- Pos. 6: drei konzentrische Gitter + bifilare Wicklung + Magnettube bei Hausers größerer Maschine;
- Pos. 9: Glasrohr + Aluminiumspirale/-Drehspan;
- Pos. 10: Hufeisenmagnet + bifilare Wicklung + Isolier-/Lochblechlagen;
- mögliche resonante bzw. phasenverschiebende Funktion;
- keine belastbare Grundlage für die pauschale Aussage „Tesla-Transformator“.

### Block D — nichtlineare Zyklussteuerung/Gleichrichtung
**Evidenz: mittel**

- Pos. 12 wird von Hauser als `RECTIFIER` bezeichnet;
- Baumann sprach laut Marinov lediglich von `crystal`;
- offizielle Beschreibung nennt eine `rectifying diode`, die den Zyklus stabil halte;
- oberes Bauteil besitzt je nach Modell 2 oder 4 erkennbare Anschlüsse;
- Funktion könnte Regelung, Gleichrichtung, Begrenzung, Impulsschaltung oder eine Kombination sein.

### Block E — DC-Speicher/Ausgang
**Evidenz für behaupteten DC-Ausgang: mittel bis hoch; Leistung: niedrig**

- Ausgang an zwei Polen;
- Betreiber sprechen ausdrücklich von Gleichstrom;
- Hauser ordnet die oberen Pos.-6-Ringe dem Ausgang zu;
- unterschiedliche Spannungswerte verschiedener Maschinen;
- keine universelle 230-V/50-Hz-AC-Stufe.

---

# 52. Pos. 6 als Dreigitter-Kapazitätsnetzwerk — wesentlich präziseres Ersatzmodell

Die direkteste Hauser-Beschreibung von Pos. 6 ist elektrisch interessanter als ein einfacher „Kondensator“:

1. `Inside Grid`
2. Acryl-Isolation
3. `Middle Grid`
4. Acryl-Isolation
5. `Outside Grid`
6. zentral `Magnet Tube`
7. darum bifilare Wicklung

Damit existieren mindestens drei kapazitive Kopplungen:

\[
C_{IM},\quad C_{MO},\quad C_{IO}
\]

mit:
- \(I\) = inneres Gitter,
- \(M\) = mittleres Gitter,
- \(O\) = äußeres Gitter.

Zusätzlich existieren Streukapazitäten gegen Sockel, Gehäuse, Umgebung und Ausgang.

## 52.1 Koaxiale Näherung

Für zwei annähernd koaxiale Zylinder gilt idealisiert:

\[
C \approx \frac{2\pi \varepsilon L}{\ln(r_2/r_1)}
\]

Die tatsächlichen Gitter sind perforiert, offen und durch weitere Bauteile beeinflusst; die Formel dient daher nur als Grundmodell.

## 52.2 Floating-Middle-Grid-Modell

Für ein elektrisch schwebendes mittleres Gitter ergibt sich näherungsweise:

\[
Q_M =
C_{IM}(V_M-V_I)
+
C_{MO}(V_M-V_O)
+
C_{Mg}(V_M-V_g)
\]

und damit:

\[
V_M \approx
\frac{
C_{IM}V_I + C_{MO}V_O + C_{Mg}V_g + Q_M
}{
C_{IM}+C_{MO}+C_{Mg}
}
\]

### Wichtige Konsequenz

Ein passives Dreigitter allein erzeugt **keine zusätzliche Energie**. Es kann jedoch:

- Potentiale gewichten;
- Ladung zwischen Zweigen verschieben;
- eine schwebende Mittenspannung erzeugen;
- als kapazitiver Summier-/Teilerknoten arbeiten;
- zusammen mit geschalteten/zeitvariablen Kapazitäten eine Ladungspumpe bilden;
- zusammen mit Induktivitäten resonant Energie zwischen Feldformen austauschen;
- hohe Spannung gegen größeren Ladungsstrom/andere Impedanz transformieren.

Das macht Pos. 6 zu einem plausiblen **kapazitiven Transformations-/Kopplungsknoten**, ohne einen Energieüberschuss vorauszusetzen.

## 52.3 Warum die mittleren Gitter besonders wichtig sind

Hauser vermutet, dass die oberen Ausgangsringe mit dem **mittleren Gitter** verbunden sind. Falls dies stimmt, wäre das mittlere Gitter nicht bloß eine Abschirmung, sondern ein **Nutzknoten**.

Eine besonders prüfenswerte Topologie wäre:

- inneres und äußeres Gitter werden von zwei phasenverschiedenen/bipolaren Ladungspfaden angeregt;
- das mittlere Gitter sammelt die resultierende Ladungsverschiebung;
- die zentrale bifilare Wicklung kompensiert Blindanteile oder erzeugt eine zweite Kopplungsart;
- der obere Ring führt das Ergebnis nach außen.

Diese Topologie ist **plausibel, aber noch nicht bewiesen**.

---

# 53. Pos. 9 — Glasrohr mit Aluminiumspirale: Funktionsrangfolge

Die Primärbeschreibung ist ungewöhnlich konkret: Glasrohr + Aluminiumspirale bzw. ein spiralförmiger Aluminium-Drehspan.

Hauser verbindet die hohen dünnen rückseitigen Bauteile später mit dem **Scheibenantrieb**. Das schränkt mögliche Funktionen ein.

## 53.1 Derzeit wahrscheinlichste Rollen

### P9-H1 — Hochspannungs-Phasen-/Verzögerungsglied
**Rang: mittel**

Eine lange, dünne, spiralförmige Leiterstruktur in einem Dielektrikum besitzt verteilt:

- Serieninduktivität;
- Widerstand;
- Eigenkapazität;
- Kapazität zur Umgebung.

Damit kann sie Ladungsimpulse zeitlich verschieben oder formen.

### P9-H2 — verteiltes RC/RLC-Ballastglied
**Rang: mittel**

Die Aluminiumspirale könnte hochfrequente Spitzen und Koronaströme begrenzen und gleichzeitig eine definierte Ladezeit erzeugen.

### P9-H3 — HF-Drossel
**Rang: niedrig bis mittel**

Potter nennt Pos. 9 ausdrücklich „chokes“. Das ist elektrisch plausibel, aber **nicht direkt beobachtet**; Hauser nennt lediglich Rohr + Spirale und eine Verbindung zum Antriebsbereich.

### P9-H4 — zusätzlicher Energiespeicher
**Rang: niedrig**

Glas + Leiter + umgebende metallische Flächen können Kapazität bilden, doch eine reine Speicherfunktion erklärt Hausers Antriebszuordnung schlecht.

## 53.2 Neue Arbeitsannahme

Pos. 9 wird in Version 4.0 primär als **distributed phase/delay/impedance element** geführt, nicht als sicherer „Tesla-Choke“.

---

# 54. Pos. 10 — Hufeisenmagnete mit bifilaren Wicklungen

Direkt bzw. relativ gut gestützt:

- Hufeisenmagnete;
- Spulen direkt um die Schenkel;
- bifilare Wicklung;
- Schichten aus Isoliermaterial/perforiertem Metall zwischen den Polen.

## 54.1 Bifilar bedeutet noch keine eindeutige Magnetfunktion

Zwei nebeneinanderliegende bzw. gegensinnig gewickelte Drähte können je nach Verschaltung:

- magnetische Felder addieren;
- Felder teilweise kompensieren;
- hohe gegenseitige Induktivität erzeugen;
- eine kapazitiv stark gekoppelte Doppelleitung bilden;
- als Common-Mode-/Differential-Element arbeiten.

Ohne die **vier Anschlussenden** und deren Verschaltung kennt man die magnetische Wirkung nicht.

## 54.2 Plausible Rollen

### P10-H1 — magnetisch vorgespannte Induktivität / Sättigungsdrossel
**Rang: mittel**

Permanentmagnetische Vormagnetisierung kann die differentielle Induktivität und das Impulsverhalten verändern.

### P10-H2 — induktive Isolation/Kopplung
**Rang: mittel**

Hausers Begriff der „isolating circuits“ passt prinzipiell zu galvanisch getrennten induktiven Pfaden.

### P10-H3 — Phasenkompensation eines kapazitiven Netzes
**Rang: mittel**

Da das Frontend stark kapazitiv ist, kann eine Induktivität Blindströme kompensieren und Resonanz erzeugen.

### P10-H4 — magnetischer Verstärker
**Rang: niedrig**

Potter/Report-Material diskutiert Magnetverstärker. Eine solche Funktion wäre technisch möglich, benötigt aber eine klar definierte Steuer-/Leistungswicklung und ist am Original **nicht nachgewiesen**.

### P10-H5 — Energiequelle durch Permanentmagnet
**Rang: verworfen**

Ein stationärer Permanentmagnet ist keine kontinuierliche Nettoenergiequelle. Er kann Feldenergie speichern/vorspannen und Kräfte verändern, aber keinen dauerhaften Kilowattfluss liefern.

---

# 55. Pos. 12 — wahrscheinlich eher Zyklus-/Nichtlinearitätsknoten als universeller Ausgangsgleichrichter

Die erneute Gesamtbetrachtung verändert die Gewichtung von Pos. 12.

## 55.1 Quellenlage

- Zeichnung 3279: `RECTIFIER`.
- Hauser: perforierte Platte, Spule, Glas, Kristall(e), vermutlich nicht evakuiert.
- Marinov: Baumann sagte `crystal`, nicht `rectifier`.
- Holzherr: bei einem Original grobe Spule um zentralen geraden Leiter, vier Anschlüsse; 50-cm-Gerät eher zwei sichtbare Zuleitungen.
- Direktfotos: gesamte Baugruppe bei mindestens einem großen Modell horizontal.
- offizielle Funktionsbeschreibung: `rectifying diode` halte die Anziehungs-/Abstoßungszyklen stabil und verhindere unkontrolliertes Hochlaufen der Scheiben.
- Potter: thermionische/Vakuum-/HF-Deutungen, nicht belegt.

## 55.2 Neue priorisierte Funktionshypothesen

### P12-H1 — nichtlineare Zyklusbegrenzung / Kommutation
**Rang: mittel bis hoch relativ zu den Alternativen**

Wenn die Diode/Kristall-Stufe Ladung nur in einer Richtung umverteilt, kann sie die Feldpolarität zwischen Segmenten und stationären Elektroden phasenrichtig halten. Das passt unmittelbar zur offiziellen Aussage über die Drehzahlstabilisierung.

### P12-H2 — Gleichrichtung eines internen Impuls-/Wechselanteils
**Rang: mittel**

Auch bei einem DC-Endausgang können intern Wechsel-/Impulssignale existieren.

### P12-H3 — Funken-/Schwellwertschalter
**Rang: mittel bis niedrig**

Das Glas-/Spulen-/Kristallgebilde könnte erst oberhalb einer Feldstärke leitend werden und dadurch zyklisch Ladung übertragen.

### P12-H4 — thermionische Vakuumdiode
**Rang: niedrig**

Potters Deutung ist geometrisch denkbar, aber Hauser vermutete ausdrücklich, dass die beobachtete Einheit nicht evakuiert sei.

### P12-H5 — Hauptenergieverstärker
**Rang: niedrig**

Keine Quelle zeigt, dass Pos. 12 allein eine Leistungssteigerung erzeugt.

## 55.3 Entscheidende neue Interpretation

Pos. 12 sollte künftig **nicht automatisch als Ausgangsgleichrichter** gezeichnet werden. Wahrscheinlicher ist eine Rolle als **nichtlinearer Timing-/Kommutations-/Clamping-Knoten innerhalb des elektrostatischen Zyklus**. Die Endgleichrichtung kann ganz oder teilweise an anderer Stelle erfolgen.

---

# 56. Home-Video-Transkription: stärkster direkte-ish Hinweis auf den geheim gehaltenen Block

Eine im Korpus enthaltene, schlecht maschinell übersetzte Transkription eines privaten Videos enthält ein Gespräch mit einem Methernitha-Mann. Wegen Übersetzungsfehlern ist sie nicht wortwörtlich als präzises technisches Protokoll verwendbar, aber mehrere Aussagen sind strukturell bemerkenswert.

## 56.1 Segmente

Auf die Frage, ob die Scheibensegmente Magnete seien, lautet die Antwort sinngemäß:

- **nein, spezielle Legierungen**;
- man könne sie magnetisieren.

Das passt zu Hausers späterer Relativierung, dass magnetisierte Lamellen **nicht universell notwendig** seien.

## 56.2 Drehzahl

Der Methernitha-Mann nennt ungefähr:

- **60 U/min, nicht schneller**.

Der Besucher verbindet dies mit „50 cycles per second“. Diese 50-Hz-Zuordnung stammt im Dialog erkennbar zumindest teilweise vom Besucher und darf nicht als eindeutige Betreiberbestätigung gelesen werden.

## 56.3 Energieweg laut Gespräch

Sinngemäß:

1. elektrostatisches Feld wird aufgebaut;
2. Energie wird zu zwei Polen geführt;
3. sie gehe „nach oben“;
4. **„there it is strengthened“**;
5. Besucher sagt „Transformer“;
6. Antwort weist einen normalen Transformatorvergleich zurück bzw. betont: **„We have direct current.“**
7. Hochspannung wird im Dialog in der Größenordnung **100 kV** genannt; Übersetzung/OCR ist unsicher;
8. auf die Frage, wie dort „capacity“ erhöht werde bzw. ob Funkenstrecken verwendet würden, antwortet der Betreiber sinngemäß:
   **„No, there are only magnets and things/coils in it.“**
9. weitere Details wolle er nicht nennen;
10. danach komme die Energie wieder nach unten in die Kondensatoren, werde dort gespeichert und gehe von dort gleichmäßig heraus.

## 56.4 Bedeutung

Diese Quelle ist kein Beweis einer unbekannten Energiequelle. Sie ist aber für die **Architektur** sehr wertvoll:

- die Scheiben werden als Hochspannungs-/Felderzeuger behandelt;
- ein nachgelagerter Bereich wird als „strengthening“ beschrieben;
- dieser Bereich wird mit Magneten/Spulen verbunden;
- der Nutzerausgang bleibt DC;
- die Kondensatoren werden als nachgelagerte Speicher/Puffer beschrieben.

### Neue Synthese

Falls die Gesprächsübersetzung den technischen Sinn korrekt wiedergibt, liegt der versteckte Kniff **nicht in einer normalen AC-Netztransformatorstufe**, sondern in einer DC-vorgespannten, impuls-/resonanzfähigen **kapazitiv-magnetischen Umwandlungsstufe**.

Das stimmt überraschend gut mit:
- Pos. 6 Dreigitter + bifilarer Magnetspule;
- Pos. 9 verteiltem RLC-Element;
- Pos. 10 magnetisch vorgespannter bifilarer Struktur;
- Pos. 12 nichtlinearer Kommutation

überein.

---

# 57. Zwei-Zeitskalen-Modell: langsame Mechanik, schnelle elektrische Impulse

Ein häufiger Widerspruch im Korpus lautet:

- Scheiben drehen nur 15–60 rpm;
- manche Rekonstruktionen finden MHz-Resonanzen.

Das ist **kein zwingender Widerspruch**.

## 57.1 Langsame mechanische Skala

Bei 50 Segmenten:

### 60 rpm
\[
f_{rot}=1\,Hz
\]

feste Elektrode:

\[
f_{seg}=50\,Hz
\]

relative Begegnung zweier gleich schneller Gegenrotoren kann geometrisch bis etwa:

\[
100\,s^{-1}
\]

erreichen.

### 15 rpm
\[
f_{rot}=0{,}25\,Hz
\]

feste Elektrode:

\[
f_{seg}=12{,}5\,Hz
\]

relative Begegnungsrate zweier gleich schneller Gegenrotoren:

\[
25\,s^{-1}
\]

## 57.2 Schnelle elektrische Skala

Ein mechanisch langsames Ereignis kann eine sehr steile elektrische Flanke erzeugen:

- Koronaeinsetzen;
- Mikrofunken;
- Kristall-/Diodenschalten;
- Ladungsüberschlag;
- schlagartige Kapazitätsentladung.

Eine ns–µs-Flanke besitzt ein breites Frequenzspektrum und kann einen LC-Kreis im kHz-/MHz-Bereich zum **Ringen** anregen.

### Konsequenz

Eine originale Testatika könnte gleichzeitig besitzen:

- langsame mechanische Kommutation im Bereich einiger 10 Hz;
- kurze Hochspannungsimpulse;
- schnelle gedämpfte elektrische Resonanz.

Damit werden HF-Beobachtungen moderner Replikationen **prinzipiell kompatibel** mit langsamen Scheiben, ohne zu behaupten, dass das Original dauerhaft bei 53 MHz oder 80–140 MHz oszillierte.

---

# 58. Report D: mögliche Widerstandsverbindungen zwischen den Scheibensegmenten

Eine der interessanteren, aber **sekundären** Report-Seiten (`testatika reports/D.jpg`) zeigt:

- magnetische Lamellen/Segmente;
- eine behauptete Magnetisierungsorientierung;
- handschriftlich eine Verbindung von Widerständen an den inneren Segmentenden;
- unten eine Notiz sinngemäß **50 Lamellen pro Seite und 50 Widerstände**, mit einem schwer lesbaren Widerstandswert, der in späterer Replikationsliteratur als ungefähr **1 kΩ** wiedergegeben wird.

Dies ist **nicht** in Hausers Primärbericht als gesicherte Eigenschaft beschrieben. Es bleibt deshalb H/E3.

## 58.1 Warum dieser Hinweis trotzdem wichtig ist

Elektrisch verbundene Segmente würden die Scheibe von einer reinen Sammlung isolierter Metallflächen zu einem **verteilten RC-Rotor** machen.

Eine mögliche Zeitkonstante wäre:

\[
\tau = R_{seg} C_{seg}
\]

Ein elektrostatisches Drehmoment kann entstehen, wenn die induzierte Ladung dem äußeren Feld zeitlich hinterherläuft. Ein grobes Kriterium für starke Phasenverschiebung wäre:

\[
\omega_e \tau \sim 1
\]

## 58.2 Diskriminierende Größenordnung

Bei 50 Hz:

\[
\omega_e \approx 314\,rad/s
\]

Für \(\tau \approx 3{,}2\,ms\) wäre eine deutliche 50-Hz-Phasenlage denkbar.

Beispiele:

- \(R=1\,k\Omega\) würde dafür \(C\approx3{,}2\,\mu F\) pro wirksamem Segmentpfad verlangen — für eine einzelne offene Scheibenlamelle sehr groß.
- bei \(C=100\,pF\) und \(R=1\,k\Omega\) ist \(\tau=100\,ns\): für 50 Hz praktisch keine Verzögerung.
- selbst \(R=1\,M\Omega\) und \(C=100\,pF\) ergeben nur \(100\,\mu s\), also deutlich unter 20 ms.

### Schluss

Die bloße Behauptung „1-kΩ-Widerstände zwischen Segmenten“ erklärt **nicht automatisch** die langsame elektrostatische Selbstrotation. Der tatsächliche Widerstandswert, die Topologie und die wirksame verteilte Kapazität sind entscheidend.

**Experimentelle Priorität:** Segment-zu-Segment-Widerstände an einem erhaltenen/hochauflösenden Originalfoto oder durch bessere Primärquelle verifizieren.

---

# 59. Quantitative Energiebilanz: Die langsamen Scheiben können behauptete Kilowatt nicht direkt mechanisch liefern

Dies ist eine der wichtigsten neuen Schlussfolgerungen.

Falls die gesamte behauptete Ausgangsleistung aus der mechanischen Wellenleistung der 50-cm-Scheiben stammen würde, müsste gelten:

\[
P=\tau\omega
\]

## 59.1 Erforderliches Drehmoment bei 60 rpm

\[
\omega=2\pi\,rad/s
\]

Für 1 kW:

\[
\tau \approx159\,N\,m
\]

Für 3 kW:

\[
\tau \approx477\,N\,m
\]

Für 4 kW:

\[
\tau \approx637\,N\,m
\]

Bei 25-cm-Radius entspräche 3 kW einer tangentialen Gesamtkraft von ungefähr:

\[
F=\tau/r \approx1910\,N
\]

also etwa der Gewichtskraft von **195 kg**.

## 59.2 Bei 15 rpm wird es noch extremer

Für 3 kW:

\[
\tau\approx1910\,N\,m
\]

Tangential am 25-cm-Radius:

\[
F\approx7640\,N
\]

entsprechend grob **780 kg Gewichtskraft**.

### Interpretation

Eine leichte 50-cm-Plexiglasscheibe, die langsam von einem kleinen Motor bzw. elektrostatischen Kräften bewegt wird, kann diese Größenordnung nicht unauffällig als mechanische Eingangsleistung übertragen.

**Folgerung:** Wenn die berichteten Kilowatt-Demonstrationen real waren, dann waren die Scheiben sehr wahrscheinlich **nicht die primäre mechanische Energiequelle**, sondern eher:

- Feld-/Bias-Erzeuger;
- Kommutator;
- Trigger;
- Phasen-/Timinggeber.

Das beweist **keine freie Energie**. Es bedeutet lediglich, dass bei realer kW-Ausgabe eine andere Energiequelle bzw. ein anderer Energiespeicher existiert haben müsste.

---

# 60. Rotationsenergie der Scheiben ist als Quelle der Lastdemonstration ausgeschlossen

Für eine reine 500-mm-PMMA-Scheibe mit:

- Radius \(r=0{,}25\,m\)
- Dicke \(d=5\,mm\)
- Dichte PMMA ungefähr \(1180\,kg/m^3\)

ergibt sich überschlägig eine Masse von rund:

\[
m\approx1{,}16\,kg
\]

und für eine Vollscheibe:

\[
I\approx\frac12mr^2\approx0{,}036\,kg\,m^2
\]

Bei 60 rpm besitzt eine solche Scheibe ungefähr:

\[
E_{rot}\approx0{,}71\,J
\]

Zwei Scheiben zusammen also nur ungefähr:

\[
1{,}4\,J
\]

plus ein begrenzter Zuschlag durch Metallsegmente/Naben.

Eine 1-kW-Lampe für 10 s benötigt dagegen:

\[
10\,000\,J
\]

also mehr als **vier Größenordnungen** mehr als die Rotationsenergie der Scheiben.

### Konsequenz

Die beobachtete Lampendemonstration kann unmöglich aus bloßem Abbremsen/Rotationsspeicher der Scheiben stammen.

Mögliche Quellen wären nur:
- laufende externe/verborgene Energiezufuhr;
- zuvor gespeicherte elektrische Energie;
- eine andere physikalische Energiequelle, die erst nachgewiesen werden müsste.

---

# 61. Warum kurze Lastdemonstrationen noch keinen Dauerleistungsnachweis liefern

Holzherrs 1000-W-Lampe für ungefähr 10 s entspricht:

\[
E\approx10\,kJ\approx2{,}8\,Wh
\]

Das ist energetisch **sehr wenig** im Vergleich zur Kapazität selbst kleiner moderner Batterien oder anderer versteckter Speicher.

Selbst wenn die Lampe tatsächlich ihre Nennleistung erhalten hätte, beweist eine 10-s-Demonstration daher nicht:

- 1 kW Dauerleistung;
- Selbstversorgung;
- Overunity.

## 61.1 Kondensatorspeicher als Größenordnung

Bei 100 kV wären für 10 kJ idealisiert nötig:

\[
C=\frac{2E}{V^2}\approx2\,\mu F
\]

Das wäre ein erheblicher Hochspannungskondensator, aber die Größenordnung zeigt: ein kurzer heller Lasttest ist grundsätzlich auch als Speicherentladung denkbar.

## 61.2 1,5 Stunden Maschinenlauf

Die 50-cm-Maschine lief laut Holzherr etwa 1,5 h, aber **nicht 1,5 h unter 1-kW-Last**. Deshalb darf aus der Laufzeit nicht \(1{,}5\,kWh\) Nutzenergie abgeleitet werden.

---

# 62. Neubewertung des Linden-Messblatts 770 V / 580 V

`testatika reports/1.jpg` enthält handschriftlich:

- Leerlauf etwa **770 V DC**;
- kalter Lastwiderstand etwa **180,5 Ω**;
- belastet etwa **580 V DC**;
- Strom ungefähr **3,3 A DC**, ausdrücklich als `calculated I` notiert.

Rechnerisch:

\[
I=\frac{580}{180{,}5}\approx3{,}21\,A
\]

und:

\[
P\approx580\times3{,}21\approx1{,}86\,kW
\]

### Warum dies kein verifizierter 1,86-kW-Nachweis ist

1. Der Widerstandswert ist als **cold** markiert.
2. Bei starker Erwärmung ändert sich der Widerstand.
3. Der Strom ist offenbar berechnet, nicht unabhängig gemessen.
4. Keine Zeitkurve.
5. Keine Temperatur/kalorimetrische Gegenmessung.
6. Keine gleichzeitige Eingangsleistungsmessung.
7. Messgerätebandbreite/Innenwiderstand unbekannt.

Der Zettel ist deshalb ein **interessanter Lastindikator**, aber kein geschlossenes Leistungsprotokoll.

---

# 63. 100-kV-Hinweis: Ladungsfluss, der für Kilowatt nötig wäre

Die Home-Video-Transkription nennt in schlechter Übersetzung eine Hochspannung in der Größenordnung von **100 kV**.

Nimmt man diese Zahl nur als Gedankenexperiment:

Für 1 kW bei 100 kV wäre ideal:

\[
I=10\,mA
\]

Für 3 kW:

\[
I=30\,mA
\]

Für 4 kW:

\[
I=40\,mA
\]

Bei 60 rpm = 1 U/s wären bei 3 kW also pro Umdrehung etwa:

\[
Q=30\,mC
\]

zu übertragen.

Bei 50 Segmentereignissen pro Umdrehung:

\[
Q_{event}\approx0{,}6\,mC
\]

Dies entspräche bei 100 kV einer effektiven Ladekapazität pro Ereignis von:

\[
C_{event}=Q/V\approx6\,nF
\]

### Bedeutung

Mehrere Nanofarad **wirksam pro Segmentereignis bei 100 kV** sind für eine offene 50-cm-Scheiben-/Elektrodengeometrie eine sehr anspruchsvolle Größenordnung.

Daher erscheint es unwahrscheinlich, dass die behaupteten 3 kW einfach als direkter klassischer Influenzstrom von den Scheibensegmenten stammen.

Wiederum spricht dies dafür, dass die Scheiben im behaupteten Gesamtprinzip eher **Bias/Trigger/Kommutation** liefern sollten.

---

# 64. V4-Kernhypothese: DC-vorgespannte parametrische Ladungs-/Impedanzwandlung — in V5 teilweise herabgestuft

**V5-Hinweis:** Dieser Abschnitt dokumentiert den V4-Denkstand. Marinov Part V macht eine gezielt resonante/magnetische Nachstufe als universelles Originalprinzip deutlich weniger wahrscheinlich. Die hier entwickelte Topologie bleibt als Hypothese für größere Hauser-Varianten erhalten, ist aber nicht mehr der übergreifende Hauptkandidat.

Die in V4 physikalisch kohärenteste Arbeitshypothese lautete:

> **Eine langsame elektrostatische Doppelscheibe erzeugt bzw. moduliert ein bipolares Hochspannungs-Biasfeld. Nichtkontaktierende Gitter kommutieren Ladung in ein mehrstufiges kapazitives Netzwerk. Dreigitter-Zylinder, verteilte Spiralen und magnetisch vorgespannte bifilare Induktivitäten formen die Impulse und kompensieren Blindanteile. Ein nichtlinearer Crystal-/Rectifier-Knoten erzwingt eine bevorzugte Ladungsrichtung und stabilisiert die mechanisch-elektrische Phase. Die Ausgangskondensatoren integrieren diese Ladung zu DC.**

Diese Hypothese erklärt viele Bauteile gleichzeitig, ohne eine exotische Energiequelle zu erfinden.

## 64.1 Was sie erklären kann

- Nichtkontakt-Elektroden;
- Gegenrotation;
- langsame mechanische Drehung;
- zahlreiche perforierte Gitter;
- Plus-/Minus-Symmetrie;
- „three isolating circuits“;
- Pos.-6-Dreigitter;
- bifilare Wicklungen;
- Pos.-9-Phasen-/Delay-Strukturen;
- Pos.-10-Magnetbias;
- Pos.-12-Diode/Kristall;
- DC-Endausgang;
- mögliche schnelle elektrische Ringing-Vorgänge trotz langsamer Mechanik.

## 64.2 Was sie **nicht** erklärt

Sie erklärt **keinen Energieüberschuss**.

Ein parametrischer/kapazitiver Wandler benötigt Energie aus:
- mechanischer Arbeit;
- einer elektrischen Biasquelle;
- einem gespeicherten Feld;
- oder einer anderen nachweisbaren Quelle.

Falls echte Kilowattleistung bei geringem Scheibenantrieb existierte, bleibt die **Energiequelle** weiterhin offen.

---

# 65. Alternative Kernhypothese: Scheiben nur als Bias-/Steuerquelle

`testatika reports/B.jpg` enthält eine bemerkenswert ähnliche Überlegung eines damaligen Untersuchers:

- Wimshurst-Scheiben dienten nur dazu, das System zu **biasen**;
- der eigentliche „active component“ liege auf einer DC-Vorspannung;
- Magnet-/Spulenstapel seien der interessanteste Bereich;
- der Autor schreibt sinngemäß, er habe nie geglaubt, die Kilowatt kämen direkt von den Wimshurst-Scheiben.

Diese Quelle ist **spekulativ**, aber die quantitative Drehmomentanalyse in Kapitel 59 macht die Grundidee technisch relevant.

### Version-4.0-Bewertung

**„Disks as bias/commutator, not as primary kW source“** wird von einer Randhypothese zu einer **wichtigen Prüfoption** hochgestuft.

Nicht hochgestuft wird die Behauptung, dass die nachgelagerte Stufe freie Energie erzeugt.

---

# 66. Was das „Geheimnis“ derzeit wahrscheinlich NICHT ist

## 66.1 Nicht einfach die 50 Segmente
Sie bestimmen Modulation/Frequenzgeometrie, erklären aber keine Leistungssteigerung.

## 66.2 Nicht einfach Permanentmagnete
Magnete fehlen bei kleinen Varianten und liefern keine kontinuierliche Nettoenergie.

## 66.3 Nicht einfach eine Tesla-Spule
Marinov widerspricht ausdrücklich; die Tesla-Deutung ist stark rekonstruktionsabhängig.

## 66.4 Nicht eine versteckte 230-V/50-Hz-Ausgangsstufe
Der Nutzerausgang wird als DC beschrieben; Spannungen variieren zwischen Modellen.

## 66.5 Nicht Radium
Baumann verneinte laut Holzherr Radiumchlorid ausdrücklich; kein materieller Beleg.

## 66.6 Nicht Rotorträgheit
Quantitativ um Größenordnungen zu klein.

## 66.7 Nicht ein einzelner bekannter Resonanzeffekt
Resonanz kann Spannung/Strom/Impedanz transformieren, aber keine Nettoenergie erzeugen.

---

# 67. Professionelles Hypothesenprotokoll — bisherige Überlegungen vollständig konsolidiert

Dieser Abschnitt hält die **Ergebnisse der bisherigen Überlegungen** fest. Er ist bewusst kein ungefiltertes Gedankenprotokoll, sondern eine nachvollziehbare Folge aus Beobachtung → Hypothese → Status.

| ID | Hypothese | Was dafür spricht | Was dagegen/offen ist | Status |
|---|---|---|---|---|
| H01 | klassischer Influenzkern | Gegenscheiben, Segmente, Elektroden, Hochspannung | erklärt kW nicht | **stark** |
| H02 | variable Kapazität als Frontend | nichtkontaktierende Gitter; Rimstar bestätigt C(t)-Effekt | Amplituden klein in Replikation | **stark** |
| H03 | Pos. 6 als kapazitiver Transformationsknoten | 3 Gitter + Mittelgitter-Ausgangsvermutung | interne Knoten unbekannt | **mittel-stark** |
| H04 | Pos. 6 universal als Tesla-Transformator | Potter/Kelly/Buchgrafik | Marinov: NO Tesla coils; Hauser beschreibt anders | **herabgestuft** |
| H05 | Pos. 6 absichtlich resonant/LC | Wicklung + Kapazitäten physikalisch vorhanden | Marinov: keine Tesla-/Resonanzkreise; Originalfrequenz unbekannt | **niedrig-mittel für Original, modellabhängig** |
| H06 | Pos. 9 als HF-Choke | Spiralgeometrie, Potter | keine Primärbestätigung | **niedrig-mittel** |
| H07 | Pos. 9 als Phasen-/Delayglied für Drive | Hauser ordnet es Drive zu; distributed RLC plausibel | Anschlüsse fehlen | **mittel** |
| H08 | Pos. 10 als saturierbare Drossel | PM-Bias + Wicklung | kein Magnetisierungs-/I-L-Verlauf | **mittel** |
| H09 | Pos. 10 als Magnetverstärker | Report/Potter-Analogien | Original-Steuerwicklung nicht belegt | **niedrig** |
| H10 | Pos. 12 als Output-Rectifier | Hauser-Label `RECTIFIER` | Betreiber sagt „crystal“; Ausgangspfad unklar | **mittel-niedrig** |
| H11 | Pos. 12 / Crystal als Zyklus-Kommutator, Rückstromsperre oder Clamp | „crystal“, Hauser-Rectifier, Marinovs one-way-gate-Idee | konkrete I-V-Kennlinie unbekannt | **mittel-stark als Minimalfunktion** |
| H12 | 50 Segmente = 50 Hz | 60 rpm + 50; Europe/US-Notiz | Marinov weist Deutung ausdrücklich zurück; kleine Geräte 20–30 Drähte; DC | **stark herabgestuft / nicht fundamental** |
| H13 | internes HF-Ringing trotz langsamer Rotoren | scharfe HV-Transienten können passive Resonanzen anregen; Replikationen | Marinov sah keinen absichtlichen HF-Kreis; Originalfrequenz nicht gemessen | **niedrig-mittel als Nebenphänomen** |
| H14 | 80–140 MHz als Originalfrequenz | Linden-/Replikationshinweise | Potter selbst warnt; nicht reproduziert | **niedrig** |
| H15 | Scheiben liefern mechanisch die kW | klassische Generatorannahme | Drehmomentrechnung macht dies extrem unplausibel | **stark herabgestuft** |
| H16 | Scheiben dienen primär Bias/Kommutation | Report B + Drehmomentargument + Operatorgespräch | Energiequelle danach offen | **wichtige Prüfoption** |
| H17 | Segmentwiderstände erzeugen Phasenlagemotor | Report D; elektrostatisch plausibel | Widerstandswert/Topologie Primärquelle fehlt | **niedrig-mittel, testbar** |
| H18 | Electret-artige Vorspannung | Electret-Material im Korpus, Plexiglas-Hinweise | kein direkter Originalnachweis | **niedrig-mittel** |
| H19 | spezielle „molecular orientation“ des Plexiglas | Hearsay | keine Primär-/Materialmessung | **niedrig** |
| H20 | Radium/ZPE | späte Webtexte | Radium verneint; keine Messung; Replikationen negativ | **verworfen/nicht belegt** |
| H21 | versteckte elektrische Speicherung erklärt kurze Demos | 10-s-Test benötigt nur 2,8 Wh | kein Nachweis versteckter Batterie | **konventionelle Alternativerklärung** |
| H22 | kW-Leistung real und aus unbekannter Stufe | Betreiber-/Zeugenclaims | keine geschlossene Messung | **offen, nicht verifiziert** |
| H23 | drei Isolationskreise = +/−/Center | Symmetrie/Centerline capacitor | Hauser benennt sie nicht | **mittel-niedrig** |
| H24 | drei Isolationskreise = C/L/NL-Kopplungsarten | Bauteilmix passt | rein interpretativ | **niedrig-mittel** |
| H25 | Pos. 6 Mittelgitter ist Nutzknoten | Hausers Ring→middle-grid-Vermutung | nicht geöffnet/verfolgt | **mittel** |
| H26 | ursprüngliches Grundprinzip ist deutlich einfacher als spätere Großmaschinen | frühe Ein-Scheiben-Geräte aus Abfallmaterial, Cu-Drahtsektoren, 80 % Bauteile für Rotation entfernbar laut Marinov | Ausgangsleistungsstufe bleibt unklar | **stark für Motorgrundfunktion** |
| H27 | getrennte Driving- und Collecting-Elektrodengruppen | Marinov zählt ≥10 Elektroden und vermutet unterschiedliche Potentiale | keine Verdrahtung verfolgt | **mittel / testbar** |
| H28 | Driving-Kondensatoren HV, Collecting-Kondensatoren niedrigere V/größere C | Marinovs explizite Schluss-Hypothese | nicht direkt gemessen | **mittel-niedrig** |
| H29 | special-form big capacitors sind Kern der hohen Leistung | Marinovs eigene Vermutung; ungewöhnliche Geometrie beobachtet | Energiegleichungen + historische Messungen liefern keinen Overunity-Mechanismus | **Geometrie wichtig, Energieüberschuss unbelegt** |
| H30 | Crystal ist primär ein one-way charge gate | Baumann nennt Crystal; Marinov erklärt Minimalfunktion so | Material/Schaltung unbekannt | **mittel** |
| H31 | Magnete sind Optimierung, nicht Grundvoraussetzung | mindestens eine kleine Maschine ohne Hufeisenmagnete; frühe Cu-Drahtsektoren | größere Varianten nutzen Magnete deutlich | **stark modellabhängig** |
| H32 | Metallplatte stoppt durch Änderung externer Feldrandbedingungen | Marinovs direkter Versuch; historische Poggendorff-Beobachtungen mit nahen Platten | Geometrie/Abstand nicht quantifiziert | **stark als elektrostatische Erklärung** |
| H33 | Ost-West-Ausrichtung ist fundamentale Energieankopplung | Baumann-Aussage zum Start der kleinen Maschine | nach Start beliebige Orientierung; keine kontrollierte Richtungsserie | **niedrig** |
| H34 | Marinovs gemessener Faktor 13,3 beweist Overunity des elektrostatischen Motors | seine 25-kV-Messung | unzureichende Wellenleistungsmessung und ungeeignete Differenzmethode | **nicht belastbar** |
| H35 | klassische Influenzmaschinen können bei großem C und niedriger V ohne Gegenarbeit hohe Nettoleistung liefern | Marinovs Spekulation | Wommelsdorf/Schmidt zeigen Eingangsarbeit, Strom-Drehzahl-Skalierung, η < 1 | **wissenschaftlich nicht gestützt** |

---

# 68. Priorisierte offene Fragen — jetzt nach Informationswert sortiert

Nicht alle unbekannten Details sind gleich wichtig. Für das Funktionsprinzip haben folgende Fragen den höchsten Informationsgewinn:

## Priorität A — kann die Gesamtarchitektur entscheiden

1. **Sind die oberen Ausgangsringe von Pos. 6 tatsächlich mit dem mittleren Gitter verbunden?**
2. **Welche Knoten treiben Inside Grid und Outside Grid?**
3. **Wie sind die vier Enden der bifilaren Pos.-6-Wicklung verbunden?**
4. **Welche vier bzw. zwei Anschlüsse besitzt Pos. 12 elektrisch?**
5. **Wo liegt Pos. 12 relativ zu Drive-Elektroden und Ausgang?**
6. **Existieren Segmentwiderstände im Original, und wenn ja: welcher Wert/Schaltpfad?**
7. **Welche Funktion haben Pos. 9 im Antriebspfad und ihre Anschlusspunkte?**
8. **Sind Pos.-10-Wicklungen in Reihe, gegensinnig, getrennt oder mit Gitterlagen gekoppelt?**

## Priorität B — Resonanz/Impedanz

9. Kapazitätsmatrix der drei Pos.-6-Gitter.
10. Eigeninduktivität/Kopplung der bifilaren Wicklung.
11. Magnet-B/H-Arbeitspunkt.
12. Pos.-9-R/L/C-Verteilung.
13. Impulsform an Pos.-12-Eingang/Ausgang.
14. tatsächliche interne Ringing-Frequenzen.

## Priorität C — Materialdetails

15. genaue Stahllegierung der Lamellen.
16. Magnetisierung der Segmente.
17. Oberflächenbeschichtung.
18. Plexiglas-/Acryltyp und eventuelle Electret-Vorbehandlung.
19. Lochblechgeometrie.
20. Umgebungs-/Feuchtigkeitsabhängigkeit quantitativ.

---

# 69. Experimentplan zur Falsifikation der Hypothesen — zuerst energiearm

Die sinnvollste weitere Arbeit ist **nicht**, sofort ein Hochspannungs-kW-Gerät zu bauen. Die offenen Hypothesen lassen sich zunächst mit kleinen, ungefährlichen Signalen trennen.

## Experiment E1 — Pos.-6-Kapazitätsmatrix

Ziel:
- \(C_{IM}\), \(C_{MO}\), \(C_{IO}\), Streukapazitäten bestimmen.

Methode:
- geometrischer Nachbau ohne Hochspannung;
- LCR-/Impedanzmessung;
- Mittelgitter floating, geerdet und belastet vergleichen.

Entscheidet über:
- H03/H25.

## Experiment E2 — C(θ) der Scheiben-/Gitteranordnung

Ziel:
- reale zeitabhängige Kapazität über Rotorwinkel bestimmen.

Methode:
- einzelner segmentierter Rotor;
- nichtkontaktierendes Lochblechgitter;
- LCR-Messung über 360°;
- zweite Gegenrotorscheibe später ergänzen.

Ergebnis:
- direktes \(C(\theta)\)-Modell statt Spekulation.

## Experiment E3 — Segment-RC-Hypothese

Ziel:
- prüfen, ob Widerstandsverbindungen relevante Phasenverschiebung erzeugen können.

Methode:
- ungefährliche Niederspannungs-Feldanregung;
- Widerstände über mehrere Dekaden;
- induzierte Ladungsphase/elektrostatische Kraft messen.

Entscheidet über:
- H17.

## Experiment E4 — bifilare Pos.-6-Spule

Ziel:
- Anschlussvarianten charakterisieren.

Messungen:
- L, M, Q;
- Serie addierend;
- Serie subtrahierend;
- parallele Varianten;
- mit/ohne Magnetstack;
- Frequenzgang.

Entscheidet über:
- H05/H08/H24.

## Experiment E5 — Pos. 9 als verteiltes Element

Ziel:
- unterscheiden zwischen Choke, Verzögerungsleitung, RC-Ballast und reinem Speicher.

Messungen:
- Impedanzspektrum;
- Phasenwinkel;
- Eigenresonanzen;
- Kopplung gegen umgebende Gitter.

## Experiment E6 — Pos. 12 als Black Box

Solange Originalmaterial fehlt, keine exotische Funktion voraussetzen.

Testbare Ersatzklassen:
- normale Diode;
- HV-Diodenkette;
- Funkenstrecke;
- Kristalldetektor;
- spannungsabhängiges Element;
- Spule + nichtlineares Element.

Kriterium:
Welche Klasse kann mit minimalen Annahmen gleichzeitig
- Gleichrichtung,
- Drehzahlbegrenzung,
- bipolare Ladungssortierung
erzeugen?

## Experiment E7 — vollständige Niederspannungs-Energiebilanz

Erst wenn Teilblöcke verstanden sind:

\[
P_{in,mech}+P_{in,bias}+P_{in,aux}
\]

gegen

\[
P_{out}
\]

mit zeitgleicher Messung.

---

# 70. Neue Gesamtbewertung des „Geheimnisses“

## 70.1 Funktionsgeheimnis

Das **Funktionsgeheimnis** ist inzwischen relativ eng eingegrenzt:

> Die ungewöhnliche Technik liegt wahrscheinlich in der phasenrichtigen Kopplung eines langsamen elektrostatischen Variable-C-Generators an ein mehrlagiges kapazitives, induktives und nichtlineares Ladungsübertragungsnetzwerk.

Die entscheidenden Kandidaten sind:
- Mittelgitter von Pos. 6;
- bifilare Magnetspule in Pos. 6;
- Pos.-9-Verzögerungs-/Impedanzglieder;
- Pos.-10-Magnetbias/Induktivität;
- Pos.-12-Kommutations-/Crystal-Knoten.

## 70.2 Energiegeheimnis

Das **Energiegeheimnis** bleibt dagegen ungelöst.

Die Dokumente liefern **keinen belastbaren Nachweis**, dass:
- dieses Netzwerk zusätzliche Energie erzeugt;
- eine bekannte Umweltenergiequelle Kilowatt einspeist;
- ZPE, Radium oder Permanentmagnete Nettoenergie liefern.

Kontrollierte Replikationen zeigen bislang Energieerhaltung.

## 70.3 Der entscheidende logische Punkt

Wenn die historischen kW-Demonstrationen korrekt waren, erzwingen die niedrige Drehzahl und die Drehmomentrechnung eine von drei Möglichkeiten:

1. **eine nicht dokumentierte konventionelle Energiequelle / Speicherung**, oder
2. **eine bislang nicht identifizierte externe Energiezufuhr**, oder
3. **ein tatsächlich unbekannter physikalischer Energiepfad**, der erst durch reproduzierbare Messung nachgewiesen werden müsste.

Die vorhandenen Dokumente entscheiden zwischen 1–3 nicht.

Deshalb lautet der professionelle Stand nicht „freie Energie bewiesen“, sondern:

> **Mechanismus der Ladungs-/Impedanzwandlung zunehmend eingrenzbar; Energiequelle der behaupteten hohen Leistung weiterhin unbelegt.**

---

# 71. Neue konkrete Rekonstruktionsmatrix für Pos. 6/9/10/12

| Bauteil | direkt beobachtete Struktur | stärkster Quellenhinweis zur Funktion | konservatives Ersatzmodell | Unsicherheit |
|---|---|---|---|---|
| Pos. 6 | 3 Gitter, Acryl, Magnettube, bifilar 18 AWG; bei kleinen Varianten einfacher | Speicher/Kopplung, Ausgangsringe, „big capacitor“ | 3-Knoten-C-Netz + gekoppelte L | interne Anschlüsse |
| Pos. 7/8 | kleine liegende Kondensatoren | ähnlich/ergänzend zu großen Kondensatoren | C7/C8 Puffer/Timing | Kapazität/Knoten |
| Pos. 9 | Glasrohr + Al-Spirale/Drehspan | laut Hauser mit Drive verknüpft | distributed R-L-C / Delay | Endanschlüsse |
| Pos. 10 | Hufeisenmagnet + bifilar + Lochblech/Isolator | magnetische Kopplung/Isolation | magnetisch vorgespannte gekoppelte L | Wicklungssinn/Knoten |
| Pos. 11 | Magnet | Timing/Regel-/Feldfunktion möglich | B-Feldquelle/Sensor | Position/Funktion |
| Pos. 12 | obere Spule/Gitter/Glas/Crystal; 2/4 Leads je Modell | rectifying diode stabilisiert cycle | nichtlinearer Schalter/Clamp/Rectifier | Material/I-V/Vakuum |

---

# 72. Dokumentierte Gegenbeweise gegen zu einfache Rekonstruktionen

Eine professionelle Wissensbasis muss auch festhalten, was bereits **nicht funktioniert** hat:

1. Literaturgetreuer 50-cm-Nachbau bei Holzherr: **nicht selbstlaufend**.
2. Prinzipversuch-Nachbauten: keine außergewöhnliche Ladung reproduziert.
3. Linden-Versuch: ursprünglicher Hochspannungseffekt nicht zuverlässig reproduziert.
4. Rimstar: variable Kapazität bestätigt, aber nur sehr kleine Impulse und keine Leistungssteigerung.
5. HCRS: starke Resonanz-/Impedanztransformation möglich, aber Leistung entspricht der Quelle.
6. Bönisch: brushless Elektrostatik + HF-Transformationsstufe funktioniert, aber Energieerhaltung; keine Overunity.

### Konsequenz

Eine neue Rekonstruktion, die lediglich:
- zwei Scheiben,
- Tesla-Spulen,
- Magnete und
- Kondensatoren

zusammenstellt, ist **nicht ausreichend**.

Sie muss die **Phasen-/Knotenstruktur** von Pos. 6/9/10/12 erklären und messen.

---

# 73. Neue zeichnerische Vorgabe für alle zukünftigen Testatika-Pläne

Jede zukünftige technische Zeichnung soll drei Ebenen unterscheiden:

### Schwarz / durchgezogen — beobachtet oder Primärquelle
- reale Geometrie;
- sichere Verbindung;
- direkte Bezeichnung.

### Orange / durchgezogen — starke Rekonstruktionshypothese
- physikalisch plausible Verbindung;
- von mehreren Quellen unterstützt.

### Grau / gestrichelt — unbekannt / alternative Hypothese
- nicht belegte Verbindung;
- Potter/Kelly/Hearsay;
- Variantenkonflikt.

Zusätzlich muss jede Darstellung:
- **koaxiale Gegenrotorscheiben** zeigen;
- berührungslose Elektroden zeigen;
- Pos. 6 mit drei Gittern statt generischem Kondensatorstack darstellen;
- Pos. 9 separat darstellen;
- Pos. 10 direkt auf Hufeisenbeinen wickeln;
- Pos. 12 als ungeklärten nichtlinearen Block kennzeichnen;
- keinen universellen 230-V/50-Hz-AC-Ausgang behaupten;
- keine kW-Zahl als Messwert ausgeben.

---

# 74. Version-4.0-Arbeitskonsens — historischer Zwischenstand, durch V5 teilweise überholt

Die derzeit beste technische Beschreibung lautet:

> **Die Testatika-Familie kombiniert einen langsamen, gegenläufigen elektrostatischen Influenz-/Variable-Kapazitäts-Generator mit berührungslosen perforierten Elektroden und einem ungewöhnlichen mehrstufigen Ladungsübertragungsnetzwerk. Bei größeren Hauser-Varianten enthält dieses Netzwerk konzentrische Gitterkondensatoren, bifilare Wicklungen auf Magnetstapeln, zusätzliche spiralige Hochimpedanzelemente, magnetisch vorgespannte Hufeisenbaugruppen und einen nicht eindeutig identifizierten Crystal-/Rectifier-Knoten. Die Architektur ist geeignet, Hochspannung zu puffern, Impulse zu formen, Blindleistung zu kompensieren, Potentiale zu transformieren und DC zu erzeugen. Die genaue Verschaltung sowie die Quelle der historisch behaupteten Kilowattleistung bleiben unbekannt.**

Diese Formulierung ersetzt alle früheren zu einfachen Erklärungen wie:
- „es ist einfach eine Wimshurstmaschine“;
- „es ist einfach eine Tesla-Spule“;
- „50 Segmente machen direkt 230 V/50 Hz“;
- „die Magnete liefern die Energie“.



---

# 75. Marinov Part V — Quellenidentität und Prüfmethodik

## 75.1 Quelle
Externe Primär-/Sammlungsquelle:

- **Stefan Marinov, *The Thorny Way of Truth, Part V***
- first published: **1989**
- Internet Archive identifier: `thornywayoftruthpart5maririch`
- bibliographischer Umfang: 259 Buchseiten; der IA-Scan enthält 328 Scan-Seiten inklusive Vorsatz/Deckel/Metadaten.
- Part V ist laut Marinovs Vorwort nahezu vollständig Testatika und historischer Influenzmaschinenphysik gewidmet.

Der vorhandene Archivbestand `marinov.pdf` war nur ein kurzer Scan-/Artikelcontainer. Part V ist **wesentlich umfangreicher** und ändert die Gewichtung mehrerer V4-Hypothesen.

## 75.2 Evidenzklassen speziell für Part V

| Code | Bedeutung | Beispiel |
|---|---|---|
| M0 | Marinov direkt am Gerät beobachtet/angefasst/getestet | kleine Ein-Scheiben-Maschine, Metallplatten-Stoppversuch |
| M1 | Marinov sah einzelnes Originalbauteil geöffnet | große Seitenkondensatoren |
| M2 | Marinov sah Modell nur im Film | mittlere Zwei-Scheiben-Maschine |
| M3 | Baumann sagte Marinov etwas | „crystal“, Ost-West-Startausrichtung, Materialangabe Fe-Ni |
| M4 | Marinovs eigene technische Deutung | HV-driving vs LV-collecting condensers |
| M5 | im Band abgedruckter Dritt-/Besucherbericht | 250 V, >10 A; Autarkie-/Batterieclaim |
| M6 | im Band nachgedruckte historische Fachliteratur | Holtz, Poggendorff, Wommelsdorf/Schmidt |

**Regel:** Ein M4/M5-Satz darf nicht zu einer Originaleigenschaft hochgestuft werden, nur weil Marinov ihn abdruckt.

---

# 76. Marinov Part V — technische Seiten 5–35, Seite für Seite / Funktionsblock für Funktionsblock

## Seite 5 — Vorwort: Scope und Besuchsstatus
- Marinov erklärt Part V ausdrücklich zum Testatika-/Influenzmaschinenband.
- Besuch 1: Juli 1988; Besuch 2: Februar/März 1989.
- Beim zweiten Besuch: eine kleine Maschine (~20 cm Scheibe) in Aktion beobachtet und getestet; zweite kleine Maschine gesehen.
- Mittlere Maschine: Film, zwei gegenläufige Scheiben ~50 cm.
- Große Maschine: Bauteile eines im Bau befindlichen Modells, Scheiben ~100 cm.

**V5-Folge:** Marinov darf für die kleine Maschine als direkter Augenzeuge, für die mittlere nur als Filmbeobachter und für die große nur bauteilbezogen zitiert werden.

## Seite 6 — Leistungsbehauptung versus Messqualität
- Marinov behauptet sehr große Differenz zwischen mechanischer und elektrischer Leistung.
- Kleine Maschine: Drehmoment/Mechanik von ihm im Wesentlichen **mit Hand/Finger geschätzt**.
- Größenordnung, die er nennt: <100 mW mechanisch, ~100 W elektrisch.
- Rotationsgeschwindigkeit grob ~1 U/s.

**Metrologischer Status:** keine kalibrierte Wellenleistungsmessung, keine simultane kalorimetrische Lastmessung, keine vollständige Eingangsbilanz. Die Aussage ist Augenzeugen-/Schätzbericht, kein COP-Nachweis.

## Seite 7 — wichtigste epistemische Selbstbegrenzung
Marinov schreibt ausdrücklich:
- kein exakter rekonstruierbarer Schaltplan vorhanden;
- klare Erklärung des Wirkprinzips fehlt;
- er kenne **weder** genaue Schaltung **noch** Erklärung;
- Motorwirkung sei ihm eher verständlich, Generator-/Leistungseffekt bleibe ein Rätsel.

**V5-Folge:** Keine spätere „Marinov-Schaltung“ darf als von Marinov verifiziertes Original ausgegeben werden.

## Seite 8 — Artikelbeginn und Namenskorrektur
- Titel: *The machine TESTATIKA and its physical background*.
- Marinov erklärt, kein Spezialist für Elektrostatik zu sein.
- Er wiederholt, dass er die Maschine nicht rekonstruieren könne.
- Baumann verneint gegenüber Marinov die Namensdeutung TESla + STATICa; Marinov gibt Baumanns Erklärung TEST + STATICA / statische Elektrizität wieder.

**V5-Folge:** Der Name liefert **kein** Indiz für Tesla-Spulen.

## Seiten 9–12 — Toepler-/Influenzgrundlagen und Marinovs erste Energiefrage
- Marinov führt klassische Influenzmaschinen als Hintergrund ein.
- Selbstverstärkung vorhandener Ladung, rotierende Dielektrika/Leiter und Ladungsabnahme stehen im Vordergrund.
- Er beginnt, mechanisches Gegenmoment der Ladungstrennung als zentrale Energiefrage zu diskutieren.
- Poggendorff-/Holtz-Beobachtungen, nach denen eine gekoppelte elektrostatische Maschine nach Anschub rotieren kann, werden als historische Parallele herangezogen.

**V5-Folge:** Selbstrotation nach einer Startladung ist kein einzigartiges Testatika-Merkmal und für sich **kein** Overunity-Beweis.

## Seiten 13–18 — Wimshurst und generatorische Ladungstrennung
- Wimshurst-artige Gegenrotation, Influenz und Ladungsverstärkung werden als Generator-Referenz behandelt.
- Marinov interessiert insbesondere das elektrostatische Rückmoment beim Sammeln/Trennen von Ladung.
- Seine spätere Testatika-Deutung greift auf diesen Generatorblock zurück.

**Physikalischer Kern:** Bei zeitabhängigen Kapazitäten/Influenzsystemen gilt weiterhin eine gekoppelte elektromechanische Energiebetrachtung; elektrische Energieabgabe erzeugt feldbedingte Gegenkräfte/-momente, sofern keine andere Energiequelle einspeist.

## Seiten 19–20 — Marinovs „große Kondensatoren“-Spekulation
Marinov argumentiert:
- sehr große Kapazität könne viel Ladung bei relativ niedriger Spannung aufnehmen;
- niedrige Kamm-/Elektrodenspannung könne kleines Gegenmoment bedeuten;
- zugleich könne großer Ladungsstrom hohe elektrische Leistung liefern;
- daraus folgert er die Möglichkeit, das Geheimnis könne in **sehr großen Kondensatoren besonderer Form** liegen.

Er nennt für Testatika als behauptete Größenordnung:
- wenige hundert Volt auf der Nutzseite;
- Ströme im Bereich von Zehnerampere beim mittleren Modell.

### Wissenschaftliche Korrektur
Diese Schlussfolgerung folgt **nicht** aus der Kondensatorphysik. Für eine variable Kapazität gilt beispielsweise:

Bei Spannungsrandbedingung:
\[
W=\frac12 C V^2,
\qquad
\tau = \frac12 V^2\frac{dC}{d\theta}
\]

Bei näherungsweise festem Ladungszustand:
\[
W=\frac{Q^2}{2C}
\]

und allgemein:
\[
i = V\frac{dC}{dt}+C\frac{dV}{dt}.
\]

Eine größere Kapazität bei niedrigerer Spannung **verschiebt** die Betriebsgrößen, eliminiert aber nicht die zum zyklischen Ladungstransport erforderliche Arbeit. Ausgangsleistung bleibt
\[
P=VI.
\]

Marinovs Gedanke macht die **Kondensatorgeometrie** zu einem wichtigen Forschungsobjekt, ist aber **kein Mechanismus für Energieerzeugung**.

## Seiten 20–22 — Gruel/Holtz/Poggendorff als Motorvorbild
- elektrostatisches Rotationsphänomen durch Anziehung/Abstoßung geladener Flächen;
- Start durch kleinen Anschub möglich;
- Drehzahl und Verhalten hängen stark von Elektrodenlage, Ladung, Isolation und Umgebung ab.

**V5-Folge:** Testatika-Selbstrotation passt qualitativ in eine bekannte Familie elektrostatischer Motorphänomene.

## Seiten 23–26 — Marinovs eigener 25-kV-Elektrostatikmotor
Marinovs Versuchsangaben:
- HV: 25 kV aus einer TV-Hochspannungskaskade;
- zwei Elektroden, etwa 45° versetzt;
- Drehzahl ~30–40 U/s;
- Strom festgehaltener Rotor ~360 nA;
- Strom rotierend ~720 nA;
- gesamte elektrische Aufnahme aus U·I ~18 mW;
- „No-load“-Anteil ~9 mW;
- als zusätzliche elektrische Leistung interpretiert Marinov ~9 mW.

Mechanische „Kalibrierung“:
- 24-V-DC-Motor treibt die Scheibe auf gleiche Geschwindigkeit;
- dessen Strom steigt von ~12 auf ~17 mA;
- Differenz der elektrischen Eingangsleistung ~120 mW;
- Marinov setzt dies näherungsweise mit mechanischer Wellenleistung gleich und erhält daraus einen behaupteten Faktor ~13,3.

### Warum der Faktor 13,3 wissenschaftlich nicht belastbar ist
1. **Differenz der elektrischen Aufnahme eines fremden DC-Motors ist keine kalibrierte Wellenleistungsmessung.** Motorwirkungsgrad, Eisen-/Bürsten-/Reibungsverluste und Arbeitspunkt ändern sich.
2. Der Kontakt zwischen Kalibriermotor und Scheibenrand bringt zusätzliche Reibungsverluste ein.
3. Der statische 9-mW-Strom bei festgehaltener Scheibe ist nicht zwingend ein vollständig subtrahierbarer „Grundverlust“; die Rotation ändert Feldlinien, Korona, Ladungswege und Stromverteilung.
4. Es gibt keine direkte Drehmomentmessung am Testmotor und keine kalorimetrische Bilanz aller Verlustkanäle.
5. Marinov schreibt selbst, dass die Messung kleiner Wärmeleistungen schwierig sei und führt die fehlende Bilanz nicht durch.

**V5-Urteil:** interessanter Elektrostatikmotorversuch, aber kein wissenschaftlicher Nachweis von COP > 1.

## Seite 26 — Scotch-Tape-Kontrollversuch
- Abdecken der Elektroden mit Klebeband stoppt Rotation und reduziert den Strom erheblich.

**Bedeutung:** starke Evidenz, dass Ladungsübertritt/Korona/Oberflächenkopplung an den Elektroden für Marinovs Motor wesentlich ist. Das stützt eine konventionelle elektrostatische/ionische Kopplung stärker als eine magnetische Energiequelle.

## Seite 27 — Beginn des eigentlichen Testatika-Kapitels
- Marinov kennzeichnet Fig. 10 als mittlere Maschine.
- Hausers Zeichnungen Fig. 11/12 werden nur deshalb erneut gedruckt, weil Marinov keine besseren Gesamtzeichnungen besitzt.
- Er kündigt ausdrücklich **Kommentare/Korrekturen** an Hausers Zeichnungen an.

## Seite 28 — Modellfamilie und spätere Metallsektoren
- mittlere/große Maschinen: zwei gegenläufige Scheiben;
- kleine Maschinen: eine Scheibe;
- mittlere nur im Film; große nur Bauteile;
- mittlere/große Sektoren perforiert;
- Baumann zeigt Marinov für große Maschine spezielles Fe-Ni-Material, leicht magnetisierbar.

**Entscheidend:** Diese Metall-/Magnetdetails gehören nicht automatisch zum Grundprinzip.

## Seite 29 — Hauser-Zeichnung 3279
- nummerierte Architektur wird als beste verfügbare Gesamtzeichnung reproduziert;
- Marinov selbst behandelt sie kritisch, nicht als vollständigen Schaltplan.

## Seite 30 — frühe Maschinen als Minimalbeweis
- erste zwei Maschinen entstanden laut Marinov 1978 aus einfachen Werkstatt-/Abfallmaterialien;
- Sektoren dieser frühen Geräte seien **einfache Kupferdrähte, etwa 1 mm**.

**V5-Folge:** Fe-Ni-Lamellen, leichte Magnetisierung, 50-Sektor-Geometrie und komplexe Großmodule können Optimierungen späterer Generationen sein; sie dürfen nicht als notwendiges Kerngeheimnis gelten.

## Seite 31 — „Brushes“ sind keine Bürsten
- Marinov korrigiert Hauser: keine Reibung, keine schleifenden Bürsten;
- Scheibe hat festen mechanischen Kontakt nur über Lager;
- Platten sollen besser `collecting electrodes` heißen;
- Marinov vermutet, dass elektrische Ladungen auf diesen Elektroden auch Drehmoment erzeugen können (`driving electrodes`);
- an der mittleren Maschine zählt er mindestens 9, vermutlich ≥10 Elektroden.

**Offene Schlüsselfrage:** Sind Sammel- und Antriebselektroden dieselben oder getrennte Gruppen?

## Seite 32 — Zwei-Potential-Hypothese, Startvorgang, Umwelteinfluss
Marinovs Hypothese:
- Collecting-Elektroden eher niedrigeres Potential;
- Driving-Elektroden eher hohes Potential;
- zugehörige Driving-Kondensatoren müssten durch die Maschine nachgeladen werden.

Direkte Beobachtungen am kleinen Gerät:
- mehrere Fingerstöße zum Start; trockene Luft leichter, feuchte Luft schwieriger;
- kleine Maschine dreht nur in einer Richtung;
- Baumann fordert für den Start ungefähr Ost-West-Ausrichtung der Achse;
- **nach dem Start** kann Marinov die Maschine jedoch kippen, drehen und in verschiedene Orientierungen bringen, ohne dass sie stoppt;
- große Metallplatte hinter der Maschine stoppt Rotation und beseitigt das statische Drehmoment.

### V5-Deutung Metallplatte
Eine große leitfähige Platte verändert unmittelbar:
- Kapazität zur Umgebung;
- elektrische Randbedingungen;
- Feldlinienführung;
- Koronaströme/Leckpfade;
- Potentiale floatinger Elektroden.

Das ist eine starke elektrostatische Kontrollbeobachtung, **kein Beleg für eine exotische Umgebungsenergiequelle**. Historische Poggendorff-Beobachtungen im selben Band zeigen ebenfalls deutliche Drehzahländerungen elektrostatischer Motoren durch nahe Glas-/Pappe-/Zinkplatten.

### V5-Deutung Ost-West
Da die Maschine nach erfolgreichem Start beliebig orientiert werden konnte, ist eine fundamentale kontinuierliche Erdmagnetfeld-/Kompassenergieankopplung wenig plausibel. Der Start-Hinweis bleibt eine unkontrollierte Baumann-Aussage und sollte experimentell blind getestet werden.

## Seite 33 — mechanische und elektrische Leistungsbehauptung
- lockerer Riemen/cord an größerer Maschine → nach Marinov schwache mechanische Kräfte;
- kleine Maschine mechanisch mit Finger <100 mW geschätzt;
- Widerstandserwärmung mit Hand auf ≥100 W geschätzt;
- Fotos zeigen Glühlampen am mittleren Modell.

**V5-Metrologie:** Dies ist der stärkste persönliche Claim Marinovs, aber gleichzeitig methodisch schwach. Ein Faktor ~1000 kann aus Hand-/Temperaturgefühl nicht wissenschaftlich abgeleitet werden.

## Seite 34 — Marinov trennt zwei Rätsel; Seitenkondensatoren geöffnet gesehen
Marinov unterscheidet:
1. warum die Maschine nach Anschub weiterläuft;
2. wie die angeblich große elektrische Nutzleistung entsteht.

Er sagt ausdrücklich: beim zweiten Problem sei er **weit von einer Erklärung entfernt**.

Dann widerspricht er der Tesla-Deutung:
- geöffnete „capacitive transformers“ der großen Maschine gesehen;
- nach seiner Beschreibung: **einfache Kondensatoren**;
- außen zylindrische Elektrode;
- innen Elektrode als Spule/Helix aus dickem Kupferdraht;
- nach Marinovs Interpretation kein Transformator, kein gezielter HF-/Resonanzkreis.

**V5-Folge:** Potters/Kellys Tesla/HF-Pfade bleiben Rekonstruktionszweige, nicht bevorzugte Originalbeschreibung.

## Seite 35 — Crystal, Magnete, Segmentzahl und Marinovs Schlussmodell
- kleine Maschine so langsam/einfach, dass Marinov keine beabsichtigten HF-Wechselströme annimmt;
- Baumann nennt einen `crystal`; Funktion unklar;
- wenn Diode, erwägt Marinov sie als **one-way gate**: Kondensator leicht laden, Rückentladung erschweren;
- Hufeisenmagnete: in erster kleiner und mittlerer Maschine, aber nicht sichtbar in zweiter kleiner; große Maschine hatte große Hufeisenmagnete;
- Marinov weist 50-Europe/60-USA-Frequenzdeutung zurück;
- kleine Maschinen nur ca. 20–30 radiale Kupferdrähte;
- seine Schluss-Hypothese: Holtz/Poggendorff/Gruel-artiger elektrostatischer Motor + Influenzgenerator, bei Zweischeibenmaschinen Wimshurst-verwandt, aber ohne schleifende Neutralisatorbürsten;
- vermutet getrennte HV-driving condensers (tausende Volt) und niedrigere collecting condensers (wenige hundert Volt), beide selbstgeladen;
- beendet Abschnitt erneut mit: reale Funktionsweise bleibt ihm unklar.

---

# 77. Seiten 36–55 — deutscher Marinov-Artikel: was er bestätigt und was nicht

Der deutschsprachige Beitrag *Die Gemeinde Methernitha und die Maschine Testatika* ist keine zweite unabhängige Quelle, aber nützlich zur Konsistenzprüfung.

Wesentliche Punkte:
- Marinov bezeichnet die Technik als **„kindlich einfach“**;
- technisch beschreibt er sie wieder als elektrostatischen Motor gekoppelt mit elektrostatischem Generator;
- er betont historische Influenzmotoren als Vergleich;
- er berichtet ausführlich über Methernitha und seine Eindrücke;
- besonders wichtig: Baumann habe versucht, ihm die Maschine zu erklären, aber Marinov empfand die Erklärung sinngemäß wie eine **unbekannte Sprache**; er verstehe die Maschine weiterhin nicht.

**V5-Folge:** Marinovs Überzeugung von Overunity darf nicht mit Kenntnis des internen Prinzips verwechselt werden.

---

# 78. Seiten 56–245 — historische Influenzmaschinenliteratur als wissenschaftliche Kontrollgruppe

Part V ist nicht nur Testatika-Erzählung. Marinov druckt historische Original-/Fachtexte nach:

| Startseite | Quelle/Thema | Relevanz für Testatika |
|---:|---|---|
| 56 | A. Toepler — intensive Ströme per Influenz | klassische Selbstverstärkung/Ladungstrennung |
| 86 | W. Holtz — neue Elektrisiermaschine | feldgesteuerte Influenzmaschine |
| 102 | Holtz — höhere Ladung isolierender Flächen | Feld-/Flächenkopplung |
| 113 | Holtz — hohe Dichte/feste influenzierende Flächen | Geometrie und Influenzierung |
| 130 | A. Kundt — geänderte Maschine | Konstruktionsvarianten |
| 141 | J. C. Poggendorff — ältere Influenzmaschinen | historische Vergleichsarchitekturen |
| 145 | Poggendorff — Holtzsches Rotationsphänomen | direkte Parallele zur Selbstrotation |
| 179 | Poggendorff — elektrischer Tourbillon | elektrostatischer Motor |
| 180 | F. Rosetti — Ströme der Elektrisiermaschinen | quantitative Strom-/Arbeitsmessung |
| 195 | C. A. Gruel — elektrische Versuche | Kondensatoren und Rotationsversuche |
| 201 | G. Wiedemann | Überblick Elektromotor-/Influenzphänomene |
| 204 | H. W. Schmidt — Influenzmaschinen | technischer Überblick |
| 223 | H. W. Schmidt — Leistungsfähigkeit | **entscheidende quantitative Energiebilanz** |

## 78.1 Holtz-/Poggendorff-Rotation ist real, aber kein Overunity-Nachweis
Die nachgedruckte historische Literatur beschreibt, dass eine elektrostatische Maschine nach Ankopplung an ein geladenes System und kleinem Anschub selbsttätig rotieren kann. Ursache wird bereits historisch als Anziehung/Abstoßung gleich-/ungleichnamiger Ladungen beschrieben.

Poggendorff berichtet außerdem, dass nahe Platten aus Glas, Pappe oder Zink die Rotation deutlich beeinflussen können. Das macht Marinovs Metallplatten-Stoppversuch **physikalisch weniger exotisch**.

## 78.2 Große Kondensatoren waren historisch bereits bekannt
Gruel beschreibt stärkere Kondensatoren für bestimmte Versuche. Große Kapazität verändert:
- Entladeintervalle;
- Impulsstärke;
- Ladungsreserve;
- Arbeitspunkt.

Sie erzeugt jedoch keine Energiequelle.

---

# 79. Seiten 223–245 — Wommelsdorf/Schmidt: der stärkste interne Gegencheck zu Marinovs Overunity-Idee

Marinov druckt eine historische Leistungsanalyse von Kondensator-Influenzmaschinen nach. Dort werden ausdrücklich bestimmt:
- Entladespannung;
- nutzbarer Strom;
- Nutzleistung;
- **aufgewandte mechanische Leistung**;
- Wirkungsgrad.

Für eine doppelt rotierende Wommelsdorf-Kondensatormaschine bei einer Scheibenumdrehung pro Sekunde enthält die Tabelle beispielsweise:

| Entladespannung | Nutzstrom | Nutzleistung | aufgewandte Leistung | Wirkungsgrad |
|---:|---:|---:|---:|---:|
| 18,8 kV | 27,81 µA | 0,262 W | 2,08 W | 12,55 % |
| 29,3 kV | 28,89 µA | 0,416 W | 2,23 W | 18,65 % |
| 50,8 kV | 25,80 µA | 0,654 W | 2,58 W | 25,4 % |
| 85,3 kV | 19,60 µA | 0,837 W | 3,13 W | 26,7 % |
| 105,2 kV | 16,20 µA | 0,853 W | 3,39 W | 26,2 % |

Der Text hält außerdem fest:
- bei hohen Spannungen sinkt der Nutzstrom durch Verluste/Übertragungsbedingungen;
- die erforderliche Leistung wächst mit der Entladespannung;
- Strom/Nutzleistung skalieren annähernd mit Drehzahl;
- Wirkungsgrad bleibt deutlich unter 100 %.

## 79.1 Warum das für Testatika zentral ist
Marinovs eigene Hypothese auf S. 19–20 lautet sinngemäß: sehr große C + niedrige V könnten geringes Gegenmoment, aber hohe elektrische Leistung erlauben. Die historischen Daten, die er selbst abdruckt, zeigen jedoch genau das, was die Energieerhaltung erwartet:

> Nutzbare Influenzleistung hat eine messbare mechanische Gegenleistung und ist nicht durch bloße Kondensatorvergrößerung von der Eingangsarbeit entkoppelt.

**V5-Schluss:** Wenn Testatika tatsächlich 10 A bei einigen hundert Volt dauerhaft lieferte, muss sie entweder wesentlich anders arbeiten als eine normale Influenzmaschine **oder** die Leistungs-/Inputbeobachtung ist unvollständig. „Große Kondensatoren“ allein lösen das Problem nicht.

---

# 80. Marinovs eigene Messlogik versus historische Messlogik

## 80.1 Historische gute Praxis
Wommelsdorf/Rosetti:
- definierte Drehzahl;
- definierte Last/Entladung;
- Strommessung;
- mechanische Arbeit/Gegenarbeit;
- Wirkungsgrad.

## 80.2 Marinovs Testatika-Praxis
- mechanisches Drehmoment: Fingergefühl;
- Lastleistung der kleinen Testatika: Wärmegefühl mit Hand;
- keine simultane Eingangsleistungsmessung;
- kein langzeitstabiler Belastungstest dokumentiert.

## 80.3 Marinovs eigener Motor
- besser instrumentiert als Testatika, aber Wellenleistung nur indirekt über fremden DC-Motor geschätzt;
- sein Faktor 13,3 beruht auf Differenzen zweier elektrischer Arbeitspunkte und nicht auf kalibriertem Torque-Speed-Produkt.

**V5-Gesamturteil:** Marinov ist als **Beobachter und Quellenkompilator** wertvoll; seine Overunity-Messtechnik erreicht nicht die Qualität eines belastbaren Energienachweises.

---

# 81. Seiten 246–254 — „Correspondence on TESTATIKA“ im Detail

## 81.1 Methernitha-Schreiben vom 15.03.1984
Methernitha behauptet gegenüber Erika Herbst:
- ein Converter könne messbare Energie aus einem „Tachyonenfeld“ entziehen;
- damit könnten Glühlampen und Bohrmaschinen betrieben werden;
- Gerät werde nicht verkauft/kommerziell angeboten.

**Status:** Betreiberbehauptung, keine technische Offenlegung und kein unabhängiges Messprotokoll. „Tachyonenfeld“ wird dadurch nicht als physikalische Quelle belegt.

## 81.2 Ingenieur-/Besucherbrief vom 12.09.1987
Berichtet:
- dreistündige Vorführung;
- mehrere kW brauchbare Leistung behauptet;
- Deutung: Elektronen aus Luft / magnetische Felder zwischen langsam rotierenden Scheiben;
- Wetter-/Gewitterabhängigkeit behauptet;
- keine sichtbare Netz-/Batterieversorgung.

**Status:** ernstzunehmender Besucherbericht, aber Deutung spekulativ; keine geschlossene Messkette.

## 81.3 Albert-Hauser-Bericht
Part V druckt Hausers zentrale technische Beobachtungen ab und bestätigt die bereits im Archiv extrahierten Punkte:
- Besuch 14.02.1986, ca. 4 h;
- 1000-W-Glühlampen-Demonstration an großer Maschine;
- Scheibe Pos. 1: 500×5 mm, 50 Chromstahl-Lamellen, **0,2×20×160 mm** in Hausers Original;
- zweite Scheibe gegenläufig;
- Magnet-/Timingrad und 60-rpm-Regelziel;
- Elektroden perforiert und ohne Scheibenkontakt;
- Pos. 6: drei konzentrische perforierte Metallrohre + Acryl + zentrale bifilare Spule um Magnettube;
- Pos. 7/8 kleine Kondensatoren;
- Pos. 9 Glasrohr + Aluminiumspirale/-Drehspan;
- Pos. 10 Hufeisenmagnete + bifilare Spulen;
- Pos. 12 möglicherweise Rectifier, Lochblech/Spule/Glas/Crystal;
- Verdrahtung ausdrücklich nur unvollständig bekannt.

**Wichtiger Modellkonflikt:** Hausers Pos.-6-Innenleben der mittleren/größeren Maschine und Marinovs geöffnete Kondensatorbeobachtung müssen als **Varianten-/Beobachtungskonflikt** geführt werden, nicht miteinander verschmolzen.

## 81.4 Weber/Schneider-Schönthal-Bericht
Behauptet:
- Methernitha-Haushalt teils über Wind + vier Testatika-Systeme und große Batterien versorgt;
- berührungslose/kapazitive Stromabnahme;
- ca. 80-cm-Plastikräder, langsam, handgestartet;
- >10 A bei 250 V DC;
- 1000-W-Lampe/Heizer innerhalb Sekunden zum Glühen;
- nach Bremsen würden Räder wieder anlaufen; erst Entladen bei stillstehenden Rädern stoppe System.

### V5-Relevanz der erwähnten Batterien
Der Bericht selbst nennt große Batteriespeicher im Energieversorgungssystem der Gemeinschaft. Das **beweist keine versteckte Batterie in einer Demonstration**, zeigt aber, dass Energiespeicherung in der Umgebung real vorhanden und technisch relevant war. Lastdemonstrationen müssen daher immer mit kontrollierter Isolation aller Speicher-/Leitungswege bewertet werden.

---

# 82. Routinekorrespondenz 1989 — Testatika-relevante Korrekturen nach dem Hauptartikel

Obwohl der Inhaltsindex ab S. 255 „Routine correspondence“ nennt, enthält dieser Block mehrere für Testatika **entscheidende** Briefe.

## 82.1 Marinov an Chris Carson, 5.03.1989
Marinov schreibt:
- Testatika sei seiner Überzeugung nach real, aber Prinzip nicht klar;
- die ersten Maschinen seien extrem einfach und in 2–3 Tagen baubar, **wenn man den Trick kennt**;
- frühe Geräte 1978 aus Werkstatt-/Abfallmaterial;
- Testatika sei Motor **und** Generator;
- nach Marinovs Literaturstudium arbeiteten die historischen Generatoren des 19. Jahrhunderts energieerhaltungskonform;
- Rotation und hohe Ausgangsleistung seien **zwei verschiedene Probleme**.

Diese Trennung ist für V5 zentral.

## 82.2 Marinovs technische Korrekturen
In einem weiteren Brief korrigiert er explizit verbreitete Darstellungen:
- **kein Solid-State-Amplifier**;
- **kein Transformer-Amplifier**;
- **keine Tesla-artigen Transformatoren**;
- 50/60-Segmentzählung nicht als Netzfrequenzmerkmal;
- frühe kleine Maschinen eher 20–25 radiale Drähte;
- Kondensatoren: äußere Zylinderelektrode + innere Kupferspiral-Elektrode;
- Zweck dieser Form bleibt ihm unklar;
- statische Elektrizität / DC als Grundcharakter;
- für die **Rotation** könnten etwa 80 % der übrigen Bauteile demontiert werden und das Gerät würde nach seiner Aussage weiterdrehen;
- statisches Drehmoment beim Fingerstopp und Initialladung werden betont;
- abschließend: das Geheimnis sei einfach, **aber er kenne es nicht**.

## 82.3 Chris-Carson-/Kelly-Gegenmaterial
Ein Korrespondent schreibt später:
- angebliche „center devices“ seien Tuning Coils;
- Coler-Schaltung ~180 kHz;
- magnetische Caduceus-Coils;
- Tesla coils hingegen ebenfalls verneint.

**V5-Quellenkritik:** Diese Resonanz-/Coler-Deutung ist die Hypothese eines Korrespondenten, **nicht Marinovs direkte Beobachtung** und nicht Baumanns bestätigte Erklärung. Genau aus solchen Briefen entstanden wahrscheinlich Teile der späteren Internet-HF-Rekonstruktionen.

---

# 83. Seiten 315–316 — Epilog: stärkste Aussage über die Grenzen der Quelle

Marinov kritisiert Geheimhaltung und „half-information“ im Free-Energy-Bereich. Dann formuliert er zur Testatika sinngemäß unmissverständlich:

> Er gebe das Geheimnis nicht deshalb nicht preis, weil er es verstecke, sondern weil er es **nicht kenne**.

Damit ist endgültig ausgeschlossen, Marinovs Band als verstecktes vollständiges Bauhandbuch zu behandeln.

---

# 84. Neue Marinov-Evidenzmatrix: Beobachtung, Aussage, Hypothese, wissenschaftlicher Status

| Aussage | Typ | V5-Bewertung |
|---|---|---|
| kleine Maschine dreht nach Anschub weiter | M0 | starke Verhaltensbeobachtung, Energiebilanz offen |
| Metallplatte hinter Gerät stoppt Rotation | M0 | starke elektrostatische Feld-/Randbedingungsbeobachtung |
| Feuchtigkeit erschwert Start | M0 | stark vereinbar mit Korona/Leck/Elektrostatik |
| keine Schleifbürsten | M0 + Hauser | sehr stark |
| frühe Sektoren ~1-mm-Kupferdraht | M0/M1 | stark für frühe Varianten |
| Fe-Ni, leicht magnetisiert | M3 | modellbezogen, nicht universal |
| zweite kleine Maschine ohne sichtbare Hufeisenmagnete | M0 | stark gegen Magnetpflicht |
| große Seitenkondensatoren außen Zylinder / innen Cu-Spirale | M1 | starke lokale Geometrieangabe |
| kein absichtliches Tesla/HF-System | Marinov Interpretation auf Basis M0/M1 | wichtig, aber nicht instrumentell durch Frequenzmessung belegt |
| Crystal vorhanden | M3 | relativ stark als Bauteilbegriff, Funktion offen |
| Crystal = one-way gate | M4 | plausible Hypothese |
| HV-driving / LV-collecting circuits | M4 | wichtige prüfbare Hypothese |
| „big capacitors“ erzeugen Energieüberschuss | M4 | physikalisch nicht hergeleitet |
| <100 mW mechanisch / ≥100 W elektrisch | Marinov Handschätzung | wissenschaftlich schwach |
| 3–4 kW mittlere Maschine | Beobachter-/Betreiberclaim | nicht unabhängig bilanziert |
| Tachyonenfeld als Energiequelle | Betreiberclaim | ohne experimentellen Nachweis |

---

# 85. Marinov versus Hauser versus Potter — V5-Auflösung der wichtigsten Konflikte

## 85.1 Scheibensegmente
- Hauser größere Maschine: 50 Chromstahl-Lamellen, leicht magnetisiert.
- Marinov frühe kleine Geräte: 20–30 radiale Kupferdrähte.

**Auflösung:** Generation/Modellvariante. Magnetische Metalllamellen nicht fundamental.

## 85.2 Pos. 6 / große Seitenmodule
- Hauser: drei Gitter + Acryl + bifilar + Magnettube.
- Marinov: bei geöffneter großer Baugruppe äußere Zylinderelektrode + innere dicke Cu-Spirale, als Kondensator interpretiert.
- Potter: Pancake-/Tesla-/Ringmagnet-Resonator.

**Auflösung:** Hauser und Marinov sind als Beobachter höher zu gewichten als Potter. Es kann Varianten geben; Potter darf nicht als Originalstandard verwendet werden.

## 85.3 HF/Tesla
- Kelly/Potter/spätere Webgrafiken: stark HF/Tesla-orientiert.
- Marinov: explizit kein Tesla-Transformator, kein AC; spätere Briefe wiederholen diese Korrektur.

**V5:** absichtliche HF/Tesla-Kernfunktion **stark herabgestuft**. HF-Transienten/parasitisches Ringing bleiben als Messphänomen möglich.

## 85.4 Magnete
- Hauser und große Fotos: deutlich vorhanden.
- Marinov zweite kleine Maschine: keine sichtbaren Hufeisenmagnete.

**V5:** Magnetik ist Zusatz-/Optimierungsfunktion einzelner Generationen, nicht sicherer Grundmechanismus.

## 85.5 50/60 Hz
- interpretierte Hauser-Grafik: 50 Europe / 60 US.
- Marinov: ausdrücklich zurückgewiesen; kleine Maschinen 20–30 Drähte, DC.

**V5:** keine fundamentale Netzfrequenzlogik.

---

# 86. V5-Kernhypothese: zuerst die einfachste funktionale Maschine erklären

Part V zwingt zu einer methodischen Umkehr:

> Nicht zuerst fragen, wozu die komplizierten Großmaschinen-Bauteile dienen, sondern zuerst erklären, wie die **frühe kleine Ein-Scheiben-Maschine** mit Kupferdrahtsektoren, wenigen Elementen und ohne zwingende Magnete überhaupt rotieren und DC laden konnte.

## 86.1 Minimaler beobachtungsnaher Kern
1. dielektrische/isolierende Scheibe;
2. radiale Leiter/Drähte bzw. Sektoren;
3. mehrere **berührungslose** stationäre Elektroden;
4. Initialladung durch Anschub/Influenz;
5. feldabhängiges elektrostatisches Drehmoment;
6. mindestens ein Kondensator-/Speicherpfad;
7. asymmetrische Ladungsführung (`crystal`/Diode als Kandidat);
8. DC-Abnahme.

## 86.2 Erweiterungen späterer Maschinen
- Gegenrotorscheibe;
- perforierte Lamellen;
- Magnetisierung;
- komplexe Pos.-6-Gitter;
- Hufeisenmagnete/bifilare Spulen;
- zusätzliche Pos. 9/10/12-Strukturen;
- Regelmechanismen.

**V5-Schluss:** Diese Erweiterungen können Leistungssteigerung, Stabilität, Feldführung oder Pufferung betreffen, sind aber nicht automatisch das ursprüngliche Geheimnis.

---

# 87. Neue elektrische Minimal-Topologie — ausdrücklich Hypothese

Marinovs Schlussmodell lässt sich als **prüfbares**, nicht als bestätigtes Schema formulieren:

### Kreis H — High-Voltage Drive
- HV-Kondensator(e);
- Driving-Elektroden;
- Scheibe/Segmente als bewegte Feld-/Ladungsträger;
- erzeugt elektrostatisches Drehmoment.

### Kreis L — Low(er)-Voltage Collection
- separate Collecting-Elektroden;
- größere Kapazität bei niedrigerem Potential;
- sammelt Ladung für Nutzerausgang.

### Kreis G — Charge Gate / Regeneration
- Crystal/Diode/anderes nichtlineares Bauteil;
- verhindert bzw. reduziert Rückentladung;
- koppelt Ladungszustände so, dass der Drive-Zweig nachgeladen bleibt.

**Unbekannt:** ob H/L/G tatsächlich drei getrennte Kreise sind und ob dies Hausers „three isolating circuits“ entspricht. Die Übereinstimmung ist interessant, aber noch nicht belegt.

---

# 88. Warum ein „Charge Gate“ wichtiger sein könnte als Resonanz

Bei einer selbstverstärkenden Influenzmaschine entscheidet nicht nur die Kapazität, sondern **wann und in welche Richtung Ladung übertragen werden darf**.

Ein ideales einseitiges Element kann:
- Ladung nach einem günstigen Feldzustand speichern;
- Rückfluss in einer ungünstigen Rotorphase blockieren;
- floatinge Elektroden aufbauen;
- eine Ladungspumpe/Peak-Hold-Struktur bilden;
- Startladung über viele Zyklen verstärken.

Das ist vollständig konventionelle Physik. Es kann erklären, warum ein `crystal` funktional zentral ist, **ohne** zusätzliche Energie zu erzeugen.

V5 priorisiert deshalb Experimente mit:
- Dioden-/Crystal-Position;
- Elektrodenphasenlage;
- Ladungsrichtung;
- Spannungsverlauf pro Rotorwinkel;
vor MHz-Abstimmungen.

---

# 89. Revidierte wissenschaftliche Bewertung von Marinovs „Kondensatorgeheimnis“

## Was an der Idee wertvoll ist
- ungewöhnliche Kondensatorgeometrie wurde tatsächlich beobachtet;
- große C bei niedrigerem V kann Ausgangsimpedanz senken;
- mehrere Kondensatorgruppen können Drive- und Collection-Potentiale entkoppeln;
- ein großes C kann kurze Lastimpulse glätten und beeindruckende Demonstrationen ermöglichen.

## Was falsch/ungenügend ist
Aus
- niedriger Spannung → kleines Gegenmoment
und
- großer Ladung → großer Strom
folgt **nicht**, dass Ausgangsenergie ohne entsprechende Eingangsarbeit entsteht.

Bei jedem periodischen Zyklus muss die vollständige Feldenergie bilanziert werden. Je nach Randbedingung verschiebt sich die Gegenkraft zwischen:
- mechanischer Rotation;
- Ladungsquelle;
- Kondensatoren;
- Leck/Korona;
- Nutzlast.

Die von Marinov selbst nachgedruckten Wommelsdorf-Daten sind der beste historische Gegenbeleg gegen eine naive „großes C = freie Energie“-Schlussfolgerung.

---

# 90. V5-Experimentprioritäten nach Marinov Part V

## Priorität 1 — frühe kleine Maschine statt 1-kW-Großmodell
Ziel: beweisen/quantifizieren, ob eine einseitig rotierende Ein-Scheiben-Anordnung nach Initialladung ohne mechanischen Kontakt ein dauerhaftes elektrostatisches Drehmoment erzeugt.

Messgrößen:
- Drehmoment vs. Winkel/Spannung;
- Rotordrehzahl;
- Elektrodenpotentiale;
- Ladungsstrom;
- Feuchtigkeit;
- Abstand/Position einer großen geerdeten/floating Metallplatte.

## Priorität 2 — getrennte Driving-/Collecting-Elektroden testen
Auf einem Rotor mindestens vier bis zehn verstellbare Elektroden vorsehen und systematisch prüfen:
- gleiche Elektrode für Drive + Collection;
- getrennte Gruppen;
- verschiedene Winkelversätze;
- getrennte HV-/LV-Kondensatoren.

## Priorität 3 — Crystal/Diode als Ladeventil
Vergleich:
- ohne Diode;
- Diode in beiden Polaritäten;
- antiparallele Dioden;
- HV-Diodenkette;
- schwellenbehaftetes Element/Funkenstrecke nur in kontrollierter Kleinenergieversion.

Messziel: Welche Konfiguration hält ein Drive-Potential nach Anschub am längsten und beeinflusst Drehmoment/Collection-Strom?

## Priorität 4 — Kondensatorgeometrie
Vergleich bei **gleicher gemessener Kapazität**:
- Plattenkondensator;
- Außen-Zylinder + innere Drahthelix;
- drei konzentrische Gitter;
- perforiert vs. massiv.

Damit lässt sich trennen, ob die Form mehr bewirkt als nur den C-Wert, etwa durch:
- Feldverteilung;
- Korona;
- verteilte Induktivität;
- Oberflächenleck;
- Kopplung zur Umgebung.

## Priorität 5 — erst danach Magnet-/Bifilar-Zusätze
Da eine frühe Maschine ohne zwingende Magnete existiert haben soll, Magnetik **nicht** als Voraussetzung in den ersten Funktionsnachbau einbauen.

## Priorität 6 — echte Energieprüfung
Erst wenn der elektrostatische Zyklus reproduzierbar ist:
\[
E_{in,elektrisch}+E_{in,mechanisch}+\Delta E_{Speicher}
\]
gegen
\[
E_{out,Last}+E_{Verluste}.
\]

Kein COP aus:
- Handgefühl;
- Lampenhelligkeit;
- Spitzenwerten;
- U×I aus nicht zeitgleichen Messungen;
- nur berechnetem Laststrom.

---

# 91. Version-5.0-Arbeitskonsens — Marinov Part V integriert

Nach Integration von *The Thorny Way of Truth, Part V* ist die beste quellenkritische Beschreibung:

> **Das wahrscheinlich ursprünglichste Testatika-Prinzip ist einfacher und stärker elektro-statisch als viele spätere Internetrekonstruktionen vermuten. Die frühe Referenzmaschine war ein langsamer, berührungsloser elektrostatischer Motor-/Influenzgenerator mit einer Scheibe, radialen Leitern, stationären Elektroden, Kondensatoren und mindestens einem unbekannten „Crystal“-Bauteil. Bei späteren größeren Maschinen kamen Gegenrotorscheiben, perforierte Metallsegmente, komplexe Gitterkondensatoren, Magnet-/Bifilar-Baugruppen und weitere Komponenten hinzu. Marinovs direkte Beobachtungen sprechen gegen die Annahme, dass Tesla-Spulen, eine feste 50/60-Hz-Abstimmung oder Permanentmagnete das universelle Grundgeheimnis bilden. Seine wichtigste plausible Schaltungsidee ist eine Trennung zwischen hochspannenden Antriebselektroden und niedriger spannenden Sammel-/Nutzkondensatoren mit asymmetrischer Ladungsführung. Diese Topologie kann Selbstaufladung, Drehmoment, Pufferung und DC-Abgabe konventionell modellieren, liefert aber keinen Beweis für zusätzliche Energie.**

## 91.1 Was V5 gegenüber V4 ändert
- **HF/Tesla:** von mittlerem Kernkandidaten → **niedrig/mittel als Neben-/Variantenphänomen**.
- **50/60 Hz:** von plausibler Designbeziehung → **nicht fundamental, stark herabgestuft**.
- **Magnete:** von möglichem Kern der Nachstufe → **modellabhängige Optimierung**.
- **Crystal/Diode:** von einem von mehreren Blocks → **höher priorisierter Kandidat für Ladungsasymmetrie/Kommutation**.
- **Kondensatorform:** bleibt sehr wichtig, aber als **Impedanz-/Feld-/Speicherproblem**, nicht als Energiequelle.
- **kleine frühe Maschine:** wird zur wichtigsten Referenz für das fundamentale Prinzip.
- **Pos. 6/9/10/12 Großmaschine:** bleiben wichtig für Leistungs-/Stabilitätssteigerung, aber nicht mehr automatisch das ursprüngliche Geheimnis.

## 91.2 Wissenschaftlicher Status
Sehr gut haltbar/reproduzierbar als Themen:
- Influenz;
- elektrostatisches Drehmoment;
- variable Kapazität/Feldrandbedingungen;
- berührungslose Ladungsübertragung;
- Kondensatorpufferung;
- asymmetrische Ladungspumpen/Rectification.

Nicht belegt:
- dauerhafte Netto-kW ohne äquivalente Energiequelle;
- Overunity;
- Tachyonen-/ZPE-Quelle;
- Marinovs behauptete Faktoren 1000 bzw. 13,3 als metrologisch gültige Energiebilanzen.

**Entscheidender Forschungsauftrag nach V5:** zuerst den einfachen elektrostatischen Motor-/Ladungszyklus der frühen Maschine mit sauberer Messtechnik rekonstruieren. Erst danach dürfen die komplizierten Großmaschinen-Komponenten als Leistungsoptimierungen untersucht werden.


# ANHANG A — Die 10 zusätzlich fotografierten Buchseiten

## A1 — `1000076410.jpg`, Seite 94
Sekundärschema mit Scheibe, nichtkontaktierenden Brushes, Hufeisenmagneten, `Crystal diode / Capacitor`, Leydener `Transmitter`/`Receiver`, Plus-/Minus-Ausgang. Nützlich zur Kelly-artigen Dreikreis-Hypothese, nicht Originalverdrahtung.

## A2 — `1000076411.jpg`, Seite 106
„Vermuteter Innenaufbau der grossen Kondensatoren“: Pancakes, Primär/Sekundär, Ringmagnete, Gitterkondensatoren, Abschirmzylinder. Explizit hypothetisch.

## A3 — `1000076412.jpg`, Seite 109
Rekonstruktions-Gesamtaufbau: antenna keys, collectors, Leyden jars, induction coil, reed/magnet, central mutual induction coil, electron-avalanche-Komponente. Sekundärrekonstruktion.

## A4 — `1000076413.jpg`, Seite 117
Hyde-Schnitt/Patentvergleich: rotierende elektrostatische Abschirmsegmente, >6000 rpm im Buchtext, Transformation/Gleichrichtung.

## A5 — `1000076414.jpg`, Seite 118
Hyde-Grundschaltung: Feldplatten, Rotor/Abschirmung, Stator, Motor und Dioden-/Kondensatornetzwerk.

## A6 — `1000076416.jpg`, Seite 124
Testatika↔Hyde-Zuordnung: disk sectors/rotor, antenna keys/stator, HV-Gitter/Feldplatten, Pots/Glättung. Interpretativer Vergleich.

## A7 — `1000076417.jpg`, Seite 161
Mechanischer Schnitt eines weiteren elektrostatischen Rotorgenerators mit Abschirmring, Rotorsegmenten, HV-Elektrode, Isolator, Antriebsflansch; Vergleichstechnik, nicht Testatika-Original.

## A8 — `1000076418.jpg`, Seite 88
Hauser-Bauteilzeichnung und deutsche Beschreibung Pos. 1–3. Enthält sekundäre Lamellenangabe 0,2×20×60 mm, die mit Hausers Original 0,2×20×160 mm kollidiert.

## A9 — `1000076419.jpg`, Seite 87
Hauser-Kapitel + interpretierte Übersicht mit `Twin Wimshurst Discs`, Tesla-Wicklungslabels, 50 Europe/60 U.S. und kapazitiven Transformatorbezeichnungen.

## A10 — `1000076420.jpg`, Seite 87
Zweite Aufnahme derselben Seite; keine unabhängige neue Quelle, aber bessere Lesbarkeit einzelner Beschriftungen.

---

# ANHANG B — Quellenbezogene Detaildossiers

## B1 — Albert Hauser: `ABweb1.jpg`
- Besuch 14. Februar 1986, mit zwei Begleitern, ca. vier Stunden.
- Methernitha etwa 200 Personen, eigene Schule/Werkstatt/Garten/Filmstudio laut Bericht.
- technische Entwicklung etwa 25 Jahre laut Gastgeber.
- Besucher sollten mit Veröffentlichung geduldig sein.
- großes Gerät mit 1000-W-Glühlampe getestet.
- Maschine etwa 20 kg; Grundplatte Holz; übrige Struktur überwiegend Plexiglas.
- Pos. 1: Ø500×5 mm, 50 Chromstahl-Lamellen 0,2×20×160 mm.
- Pos. 2: gleich groß, dunkler, gegenläufig, Lamellen beidseitig.
- Pos. 3: Magnet-/Timing-Rad, Regelung auf 60 rpm, flexibler Riemen.
- Pos. 4: Lamellen leicht magnetisiert, Material/Schutz gegen Koronaoxidation.

## B2 — Albert Hauser: `ABweb2.jpg`
- Pos. 5: alle Elektroden aus perforiertem Metall; kein Scheibenkontakt; etwa 8 vorn + 8 hinten; hintere nicht parallel; radiale Umkantung; geschichtete perforierte/isolierende Platten.
- Pos. 6: drei konzentrische perforierte Metall-/Gitterrohre mit Acryl dazwischen; zentral bifilare Spule um Magnettube.
- Pos. 7/8: kleinere liegende Kondensatoren.
- Pos. 9: Glasrohr mit Aluminium-Drehspan/-spirale.
- Pos. 10: Hufeisenmagnete mit bifilaren Spulen; zwischen den Beinen Isolier-/Lochblechlagen.
- Pos. 12: möglicherweise Gleichrichter; vertikale perforierte Platte, Spule, Glasabdeckung, Kristall(e); Hauser vermutet nicht evakuiert.
- Verbindungen nur unvollständig bekannt.
- horizontale Elektroden übertragen HV zu Pos. 6.
- viele Beschichtungen intern verbunden; Verbindungen zu 7/8 und teils 9/10/12.
- dicke Holzgrundplatte laut anderen Besuchern geschichtet.
- kleines Gerät ca. 1 kg, Scheibe ca. 12 cm, einfacher; von Hauser ohne Last nur messtechnisch beobachtet.

## B3 — Albert Hauser: `ABweb3.jpg`
- Zeichnung Nr. 3279.
- Front/Back/Top/Side.
- nummerierte Liste 1–12 + Nylon belt.
- Querschnitt Pos. 6: bifilar coil, inside/middle/outside grid, acrylic tube insulation, magnet tube.
- Zeichnungstitel scheint eine Leistungs-/DC-Angabe zu enthalten; wegen geringer Auflösung nicht als harte Zahl verwendet.

## B4 — `ABweb4.jpg`
- interpretierte Systemzeichnung.
- `Twin Wimshurst Discs`.
- `Magnetic Stainless Steel Disc Segments ... 50 for Europe / 60 for U.S.`.
- Collection Brush +/−.
- Tesla-Coil-/Amplification-Labels.
- Centerline capacitor.
- Hufeisenmagnete/magnetic windings.
- mehrere Fragezeichen an Funktionslabels: Unsicherheit ist Teil der Quelle.

## B5 — `AHwebL5.jpg`
- Hauser berichtet wenig Erfolg mit eigenem justierbaren Arbeitsmodell.
- verweist auf Probleme, ernsthafte technische Replikatoren zu finden.
- Magnetexperimente ohne Erfolg.
- denkt über externe HV-DC-Versorgung zum isolierten Studium nach.
- erwähnt Bosshardts „special spiral-magnets“.
- bekräftigt 8 Elektroden vorn und 8 hinten;
- erwägt Verbindungen zu um etwa 45° versetzten rückwärtigen Elektroden;
- mehrere mögliche Verschaltungsvarianten;
- berührend/nichtberührend als Vergleich zu klassischer Wimshurst.

## B6 — `AHwebL6.jpg`
- Baumann habe gesagt, kleine Kondensatoren seien ähnlich den großen.
- hohe dünne rückseitige Kondensatoren/Pos. 9 würden zum Scheibenantrieb benötigt.
- Magnetisierung der großen Segmente sei nicht bei allen kleinen Varianten vorhanden; Hauser folgert, Magnetfunktion sei Verbesserung, nicht Grundvoraussetzung.
- Hauser kennt Gitter-/Spulenverbindungen und Pos.-11-Magnetfunktion nicht.
- korrigiert übertriebene Newsletter-Angaben zu Großmaschinen.

## B7 — `AHwebL7.jpg`, 27.09.1988
- Pos. 6 je Zylinder drei konzentrische Gitterrohre;
- Acrylrohre als Isolation;
- zentral Magnettube, vermutlich Lautsprechermagnetstapel;
- zwei Lagen 18-AWG-Lackdraht;
- Plastikfolie zwischen Schichten;
- zweite Wicklung entgegengesetzt;
- Verbindung ergibt bifilare Funktion.

## B8 — `AHwebl8.jpg`
- Pos. 3 Magnetrad auf gleicher Welle wie Riemenscheiben;
- Nylonriemen nicht gekreuzt;
- ein Magnet in Scheibennähe von mehreren Besuchern beobachtet;
- Magnettube Pos. 6 vertikal in zwei Teilen, nicht horizontal;
- Kristalle nur oben Pos. 12;
- Spulen direkt auf Hufeisenbeinen;
- große Maschine: kleiner DC-Motor + Magnetradregelung;
- kleine Maschinen: Poggendorff-artiger Antrieb.

## B9 — `ABweb9.jpg`
- ausdrücklich kein Elektrodenkontakt mit Scheiben.
- Oberseite Pos. 6 zu horizontalen Scheibenelektroden.
- Magnettube-/Spulenverschaltung unbekannt.
- behaupteter nutzbarer Ausgang 300 V × 10 A an Kupferringen Pos. 6.
- vermutete Verbindung der Ringe zum mittleren Gitterrohr.
- „three isolating circuits“ müssten harmonieren.
- Brief bezieht sich auf mittlere Maschine Zeichnung 3279.

## B10 — `SMwebL1.jpg` / `SMweb2.jpg`
- Marinov: kleines Gerät ohne Motor, elektrostatische Rotation.
- kleine Scheibe/wires angeblich mit nichts verbunden.
- small pots: Gitter + Kunststoff + Kupferspirale; keine Magnete.
- Baumann sprach von „crystal“, nicht „rectifier“.
- Kondensatoren keine Tesla-Spulen; Marinov sagt kein AC.
- trotz eigener Überzeugung von „free energy“ konnte Marinov Prinzip nicht rekonstruieren.

---

# ANHANG C — Korrekturen gegenüber der vorherigen `state.md`

1. **Lamellenlänge:** nicht mehr pauschal 60 mm. Primärquelle Hauser = 160 mm; Buchseite = 60 mm. Konflikt dokumentiert.
2. **50-Hz-Hypothese:** von „besonders wahrscheinlicher Kernfunktion“ auf „plausible, aber nicht universelle Designbeziehung“ herabgestuft, weil 15-rpm-Demo und Gegenrotation berücksichtigt werden.
3. **Tesla-Spulen:** nicht mehr als sichere Originalbaugruppe dargestellt; expliziter Marinov-Widerspruch integriert.
4. **Große Pots:** Innenaufbau nicht mehr als einheitlich angenommen; Hauser, Marinov, Potter und spätes Hearsay getrennt.
5. **Antrieb:** DC-Motor, Poggendorff-Antrieb und offizielle Selbstlaufbehauptung als modellabhängiger Konflikt erfasst.
6. **Hyde:** klar als Vergleichsmodell, nicht als praktisch identische Testatika-Funktion getrennt.
7. **Leistungswerte:** alle als Quelle/Modell/Beobachtungsart gekennzeichnet; keine „1-kW“-Zahl als gesicherter Nennwert.
8. **Radium:** explizit als unbelegte und von Baumann laut Holzherr verneinte Hypothese markiert.
9. **Replikationen:** HCRS, Rimstar, Prinzipversuch und Bönisch vollständig integriert.
10. **Archivvollständigkeit:** jeder Hauptarchiv-Eintrag wird im folgenden Quellenledger erfasst.

---

# ANHANG D — Vollständiges Hauptarchiv-Quellenledger

**Spalten:** Pfad | Klasse | Evidenzcode | Prüfergebnis/Kurzbewertung  
Die Tabelle dient der Nachvollziehbarkeit, dass jeder Hauptarchiv-Eintrag in der Korpusanalyse berücksichtigt wurde.

- `3kwfront.jpg` — **DIREKTFOTO [E0]** — Direktes/archiviertes Maschinenfoto oder Detailfoto; Geometrie visuell verwertbar, Funktion daraus nicht beweisbar.

- `3kwrear.jpg` — **DIREKTFOTO [E0]** — Direktes/archiviertes Maschinenfoto oder Detailfoto; Geometrie visuell verwertbar, Funktion daraus nicht beweisbar.

- `Bernhard_Gross_electret_research[2].doc` — **HINTERGRUND ELEKTRET [H]** — Electret-Forschung; nur zur Bewertung der Electret-Hypothese.

- `De Keely #U00e0 Peregrinus 1-2.mht` — **HINTERGRUND HISTORISCH [X]** — Keely/Peregrinus-Hintergrund; keine spezifische Testatika-Evidenz.

- `Electrostatic Motors-Oleg Jefimenko.mht` — **HINTERGRUND ELEKTROSTATIK [H]** — Jefimenko/Elektrostatik-Hintergrund, keine Original-Testatika-Daten.

- `EssentialSvali.pdf` — **IRRELEVANT [X]** — Thematisch nicht Testatika; Verschwörungs-/Svali-Material, aus technischer Evidenz ausgeschlossen.

- `HTML_UND_BILDER/Thumbs.db` — **META [X]** — Windows-Bildcache; keine technische Primärinformation.

- `HTML_UND_BILDER/blu.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/cas1.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/cas2.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/circuit.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/date.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/discharger.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/efg2.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/efg3.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/eguchi.htm` — **HINTERGRUND ELEKTRET [H]** — Historische Electret-Quelle; nur Hintergrund zu einer Hypothese.

- `HTML_UND_BILDER/eguchi1.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/elecfg.htm` — **POTTER BACK-ENGINEERING [E3/H]** — Paul-E.-Potter-Rekonstruktion: wertvolle Geometrieanalyse, aber viele ausdrücklich spekulative Schaltungsdeutungen.

- `HTML_UND_BILDER/elect2.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/elect3.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/elect4.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/elect5.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/elect6.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/elect7.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/electret.htm` — **POTTER BACK-ENGINEERING [E3/H]** — Paul-E.-Potter-Rekonstruktion: wertvolle Geometrieanalyse, aber viele ausdrücklich spekulative Schaltungsdeutungen.

- `HTML_UND_BILDER/electroncasc.htm` — **POTTER BACK-ENGINEERING [E3/H]** — Paul-E.-Potter-Rekonstruktion: wertvolle Geometrieanalyse, aber viele ausdrücklich spekulative Schaltungsdeutungen.

- `HTML_UND_BILDER/fig1.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/fig2.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/fig3.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/fig4.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/fig5.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/fig6.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/fig7.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/freenotes.htm` — **POTTER BACK-ENGINEERING [E3/H]** — Paul-E.-Potter-Rekonstruktion: wertvolle Geometrieanalyse, aber viele ausdrücklich spekulative Schaltungsdeutungen.

- `HTML_UND_BILDER/fullcircit.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung. Exakt-Duplikatgruppe: HTML_UND_BILDER/fullcircit.gif / HTML_UND_BILDER/fullcircit_testatika.gif

- `HTML_UND_BILDER/fullcircit_testatika.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung. Exakt-Duplikatgruppe: HTML_UND_BILDER/fullcircit.gif / HTML_UND_BILDER/fullcircit_testatika.gif

- `HTML_UND_BILDER/index.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/index.html` — **POTTER BACK-ENGINEERING [E3/H]** — Paul-E.-Potter-Rekonstruktion: wertvolle Geometrieanalyse, aber viele ausdrücklich spekulative Schaltungsdeutungen.

- `HTML_UND_BILDER/linden.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/nonuni1.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/orse1.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/orse2.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/orse3.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/orse4.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/orse5.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/orsshoe.htm` — **POTTER BACK-ENGINEERING [E3/H]** — Paul-E.-Potter-Rekonstruktion: wertvolle Geometrieanalyse, aber viele ausdrücklich spekulative Schaltungsdeutungen.

- `HTML_UND_BILDER/principle.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/principles.htm` — **POTTER BACK-ENGINEERING [E3/H]** — Paul-E.-Potter-Rekonstruktion: wertvolle Geometrieanalyse, aber viele ausdrücklich spekulative Schaltungsdeutungen.

- `HTML_UND_BILDER/pulse.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/recircuit.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/rect.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/rectifier.htm` — **POTTER BACK-ENGINEERING [E3/H]** — Paul-E.-Potter-Rekonstruktion: wertvolle Geometrieanalyse, aber viele ausdrücklich spekulative Schaltungsdeutungen.

- `HTML_UND_BILDER/report99.htm` — **ZEITZEUGENBERICHT [E1]** — Hans-Holzherr-Bericht 1999; unabhängigerer Besucherbericht mit Lastdemonstrationen und Prinzipversuch.

- `HTML_UND_BILDER/title.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/titlestill.gif` — **POTTER-DIAGRAMM [E3/H]** — Illustration/Schaltbild aus Potter-Korpus; rekonstruktiv, nicht Original-Konstruktionszeichnung.

- `HTML_UND_BILDER/video.htm` — **OFFIZIELLE/NAHE OFFIZIELLE TRANSKRIPTION [E2]** — Transkription des Methernitha-Informationsfilms; offizielle Funktionsbehauptungen, nicht unabhängige Messung.

- `Leid-flasch_bau.jpg` — **HINTERGRUND [H]** — Generische Leydener-Flaschen-Skizze; erklärt Bauteiltyp, nicht Original-Testatika.

- `Marinov.jpg` — **HISTORISCHES FOTO [E0]** — Historisches Foto/Personenbezug; geringe Konstruktionsdichte. Exakt-Duplikatgruppe: Marinov.jpg / testatika reports/marinov.jpg

- `Mathernitha.pdf` — **SEKUNDÄR-KOMPENDIUM [E2/E3]** — Magazin-/Web-Kompilation mit Methernitha-Text und Holzherr-Bericht; teils Duplikat.

- `Replications.zip` — **ARCHIV-CONTAINER [X]** — Verschachteltes Archiv; Inhalt separat geprüft, überwiegend Duplikate/Replications.

- `TESTA7.jpg` — **DIREKTFOTO [E0]** — Direktes/archiviertes Maschinenfoto oder Detailfoto; Geometrie visuell verwertbar, Funktion daraus nicht beweisbar.

- `TESTA9.jpg` — **DIREKTFOTO [E0]** — Direktes/archiviertes Maschinenfoto oder Detailfoto; Geometrie visuell verwertbar, Funktion daraus nicht beweisbar.

- `THE FINAL SECRET OF FREE ENERGY.mht` — **DUPLIKAT/SEKUNDÄR [E1]** — Nahezu textgleich mit report99.htm; Holzherr-Bericht in anderem Container.

- `Testatika - Replication Claim of the Swiss M L.doc` — **REPLIKATIONS-DOSSIER [R1/H]** — Replikationssammlung mit HCRS/Rimstar/Prinzipversuch und spekulativen Abschnitten; Messdaten getrennt von Theorie bewerten.

- `Testatika - Replication Claim of the Swiss ML.doc` — **REPLIKATIONS-DOSSIER [R1/H]** — Replikationssammlung mit HCRS/Rimstar/Prinzipversuch und spekulativen Abschnitten; Messdaten getrennt von Theorie bewerten.

- `Testatika - stroj na transformaci voln#U00e9 energie.mht` — **SEKUNDÄR-KOMPENDIUM [E3]** — Tschechische Kopie/Übersetzung eines Testatika-Webkompendiums; weitgehend derivativ.

- `Thestatica Machine ML converter Paul Baumann Methernitha Group Stefan Marinov Free Energy Don Kelly Zero Point Energy ZPE Orgone.mht` — **SEKUNDÄR-WEBSEITE [E3]** — Kurze inoffizielle Webdarstellung; überwiegend abgeleitete Behauptungen.

- `Thumbs.db` — **META [X]** — Windows-Bildcache; keine technische Primärinformation.

- `Wimshurst Machines-tesla.mht` — **HINTERGRUND WIMSHURST [H]** — Klassische Wimshurst-/Influenzmaschinen-Konstruktionsinformation; Vergleichsgrundlage.

- `arm/58eb.jpg` — **REPLIKA/PRINZIPMODELL [R1/H]** — Fotos/Zeichnungen einer kleinen Replika bzw. legendierten Frühform; nicht sicher Originalgerät.

- `arm/6234.jpg` — **REPLIKA/PRINZIPMODELL [R1/H]** — Fotos/Zeichnungen einer kleinen Replika bzw. legendierten Frühform; nicht sicher Originalgerät.

- `arm/8dc1.jpg` — **REPLIKA/PRINZIPMODELL [R1/H]** — Fotos/Zeichnungen einer kleinen Replika bzw. legendierten Frühform; nicht sicher Originalgerät.

- `arm/Thumbs.db` — **META [X]** — Windows-Bildcache; keine technische Primärinformation.

- `arm/ba3b.jpg` — **REPLIKA/PRINZIPMODELL [R1/H]** — Fotos/Zeichnungen einer kleinen Replika bzw. legendierten Frühform; nicht sicher Originalgerät.

- `arm/ba69.jpg` — **REPLIKA/PRINZIPMODELL [R1/H]** — Fotos/Zeichnungen einer kleinen Replika bzw. legendierten Frühform; nicht sicher Originalgerät.

- `assembly pics.zip` — **ARCHIV-CONTAINER [X]** — Verschachteltes Archiv; Inhalt separat geprüft, überwiegend Duplikate/Replications.

- `constructiontips.txt` — **HINTERGRUND WIMSHURST [H]** — Klassische Wimshurst-/Influenzmaschinen-Konstruktionsinformation; Vergleichsgrundlage.

- `esd_transformation_for_web.pdf` — **TECHNISCHE REPLIKATION [R1]** — Sven Bönisch 2003: kontrollierter elektrostatischer/Resonanz-Nachbau; Energieerhaltung, kein Overunity.

- `f31.jpg` — **DIREKTFOTO [E0]** — Direktes/archiviertes Maschinenfoto oder Detailfoto; Geometrie visuell verwertbar, Funktion daraus nicht beweisbar.

- `front.jpg` — **DIREKTFOTO [E0]** — Direktes/archiviertes Maschinenfoto oder Detailfoto; Geometrie visuell verwertbar, Funktion daraus nicht beweisbar.

- `glow.jpg` — **DIREKTFOTO [E0]** — Direktes/archiviertes Maschinenfoto oder Detailfoto; Geometrie visuell verwertbar, Funktion daraus nicht beweisbar.

- `hauser/ABweb1.jpg` — **PRIMÄR-/ZEITZEUGENKORRESPONDENZ [E1]** — Albert-Hauser-Bericht, Zeichnung oder Brief; zentrale frühe Beobachterquelle.

- `hauser/ABweb2.jpg` — **PRIMÄR-/ZEITZEUGENKORRESPONDENZ [E1]** — Albert-Hauser-Bericht, Zeichnung oder Brief; zentrale frühe Beobachterquelle.

- `hauser/ABweb3.jpg` — **PRIMÄR-/ZEITZEUGENKORRESPONDENZ [E1]** — Albert-Hauser-Bericht, Zeichnung oder Brief; zentrale frühe Beobachterquelle.

- `hauser/ABweb4.jpg` — **PRIMÄR-/ZEITZEUGENKORRESPONDENZ [E1]** — Albert-Hauser-Bericht, Zeichnung oder Brief; zentrale frühe Beobachterquelle.

- `hauser/ABweb9.jpg` — **PRIMÄR-/ZEITZEUGENKORRESPONDENZ [E1]** — Albert-Hauser-Bericht, Zeichnung oder Brief; zentrale frühe Beobachterquelle.

- `hauser/AHwebL5.jpg` — **PRIMÄR-/ZEITZEUGENKORRESPONDENZ [E1]** — Albert-Hauser-Bericht, Zeichnung oder Brief; zentrale frühe Beobachterquelle.

- `hauser/AHwebL6.jpg` — **PRIMÄR-/ZEITZEUGENKORRESPONDENZ [E1]** — Albert-Hauser-Bericht, Zeichnung oder Brief; zentrale frühe Beobachterquelle.

- `hauser/AHwebL7.jpg` — **PRIMÄR-/ZEITZEUGENKORRESPONDENZ [E1]** — Albert-Hauser-Bericht, Zeichnung oder Brief; zentrale frühe Beobachterquelle.

- `hauser/AHwebl8.jpg` — **PRIMÄR-/ZEITZEUGENKORRESPONDENZ [E1]** — Albert-Hauser-Bericht, Zeichnung oder Brief; zentrale frühe Beobachterquelle.

- `hauser/SMweb2.jpg` — **PRIMÄR-/ZEITZEUGENKORRESPONDENZ [E1]** — Marinov-Brief/Korrespondenz; direkte Beobachterangaben, aber ohne kontrollierte Vollmessung.

- `hauser/SMwebL1.jpg` — **PRIMÄR-/ZEITZEUGENKORRESPONDENZ [E1]** — Marinov-Brief/Korrespondenz; direkte Beobachterangaben, aber ohne kontrollierte Vollmessung.

- `hauser/Thumbs.db` — **META [X]** — Windows-Bildcache; keine technische Primärinformation.

- `marinov.pdf` — **SCAN-CONTAINER [E1/E3]** — Gescannter Marinov-Artikel; Textlayer praktisch unbrauchbar, Inhalt über 9 PNG-Seiten erschlossen.

- `marinov.txt` — **AUTORENKONTEXT [X]** — Marinov-Text zu alternativer Physik; keine verwertbaren Testatika-Konstruktionsdetails.

- `marinov1.exe` — **BINÄR [X]** — Nicht ausgeführt; unbekanntes historisches Binärprogramm, keine belastbare Testatika-Evidenz extrahiert.

- `marinov2.exe` — **BINÄR [X]** — Nicht ausgeführt; unbekanntes historisches Binärprogramm, keine belastbare Testatika-Evidenz extrahiert.

- `marinov_1of9.png` — **ZEITGENÖSSISCHER ARTIKELSCAN [E1/E3]** — Scan eines Marinov/Kelly-Artikels; Beobachterbericht + sekundäre technische Interpretation.

- `marinov_2of9.png` — **ZEITGENÖSSISCHER ARTIKELSCAN [E1/E3]** — Scan eines Marinov/Kelly-Artikels; Beobachterbericht + sekundäre technische Interpretation.

- `marinov_3of9.png` — **ZEITGENÖSSISCHER ARTIKELSCAN [E1/E3]** — Scan eines Marinov/Kelly-Artikels; Beobachterbericht + sekundäre technische Interpretation.

- `marinov_4of9.png` — **ZEITGENÖSSISCHER ARTIKELSCAN [E1/E3]** — Scan eines Marinov/Kelly-Artikels; Beobachterbericht + sekundäre technische Interpretation.

- `marinov_5of9.png` — **ZEITGENÖSSISCHER ARTIKELSCAN [E1/E3]** — Scan eines Marinov/Kelly-Artikels; Beobachterbericht + sekundäre technische Interpretation.

- `marinov_6of9.png` — **ZEITGENÖSSISCHER ARTIKELSCAN [E1/E3]** — Scan eines Marinov/Kelly-Artikels; Beobachterbericht + sekundäre technische Interpretation.

- `marinov_7of9.png` — **ZEITGENÖSSISCHER ARTIKELSCAN [E1/E3]** — Scan eines Marinov/Kelly-Artikels; Beobachterbericht + sekundäre technische Interpretation.

- `marinov_8of9.png` — **ZEITGENÖSSISCHER ARTIKELSCAN [E1/E3]** — Scan eines Marinov/Kelly-Artikels; Beobachterbericht + sekundäre technische Interpretation.

- `marinov_9of9.png` — **ZEITGENÖSSISCHER ARTIKELSCAN [E1/E3]** — Scan eines Marinov/Kelly-Artikels; Beobachterbericht + sekundäre technische Interpretation.

- `meg.pdf` — **HINTERGRUND FREMDGERÄT [X]** — MEG/anderes Generatorprinzip; keine Testatika-Konstruktionsquelle.

- `meg_patent.pdf` — **HINTERGRUND FREMDGERÄT [X]** — MEG/anderes Generatorprinzip; keine Testatika-Konstruktionsquelle.

- `recircuit.gif` — **SONSTIG [X]** — Geprüft; keine eindeutige zusätzliche Testatika-Evidenz klassifiziert.

- `svali.pdf` — **IRRELEVANT [X]** — Thematisch nicht Testatika; Verschwörungs-/Svali-Material, aus technischer Evidenz ausgeschlossen.

- `swiss Testakica free energy device.mht` — **SEKUNDÄR-KOMPENDIUM [E3]** — Großes Web-Kompendium mit Hauser/Marinov/Hartmann-Hearsay; nützlich für Widersprüche, nicht unabhängig.

- `testabig.jpg` — **DIREKTFOTO [E0]** — Direktes/archiviertes Maschinenfoto oder Detailfoto; Geometrie visuell verwertbar, Funktion daraus nicht beweisbar.

- `testatika reports/1.jpg` — **MESSNOTIZ [E1/E3]** — Handschriftliche Drittquellen-Messwerte zum ML-Konverter; kein vollständiges Messprotokoll.

- `testatika reports/2.jpg` — **REKONSTRUKTIONSHYPOTHESE [E3/H]** — Handskizze/Interpretation; nicht als Originalschaltplan zu behandeln.

- `testatika reports/3.jpg` — **REKONSTRUKTIONSHYPOTHESE [E3/H]** — Handskizze/Interpretation; nicht als Originalschaltplan zu behandeln.

- `testatika reports/4.jpg` — **REKONSTRUKTIONSHYPOTHESE [E3/H]** — Handskizze/Interpretation; nicht als Originalschaltplan zu behandeln.

- `testatika reports/5.jpg` — **VARIANTEN-/FELDNOTIZ [E1/E3]** — Beobachtungs-/Hearsay-Notiz zu Varianten, Elephant oder Aufbauänderungen.

- `testatika reports/6(1).jpg` — **LINDEN-EXPERIMENT / FELDNOTIZ [E1/E3]** — Sekundärer Besucher-/Messbericht bzw. Handskizze zum Linden-Prinzipversuch; wichtige Replikations- und Messunsicherheit.

- `testatika reports/6.jpg` — **LINDEN-EXPERIMENT / FELDNOTIZ [E1/E3]** — Sekundärer Besucher-/Messbericht bzw. Handskizze zum Linden-Prinzipversuch; wichtige Replikations- und Messunsicherheit.

- `testatika reports/7(1).jpg` — **LINDEN-EXPERIMENT / FELDNOTIZ [E1/E3]** — Sekundärer Besucher-/Messbericht bzw. Handskizze zum Linden-Prinzipversuch; wichtige Replikations- und Messunsicherheit.

- `testatika reports/7.jpg` — **LINDEN-EXPERIMENT / FELDNOTIZ [E1/E3]** — Sekundärer Besucher-/Messbericht bzw. Handskizze zum Linden-Prinzipversuch; wichtige Replikations- und Messunsicherheit.

- `testatika reports/A.jpg` — **VARIANTEN-/FELDNOTIZ [E1/E3]** — Beobachtungs-/Hearsay-Notiz zu Varianten, Elephant oder Aufbauänderungen.

- `testatika reports/B.jpg` — **REKONSTRUKTIONSHYPOTHESE [E3/H]** — Handskizze/Interpretation; nicht als Originalschaltplan zu behandeln.

- `testatika reports/C.jpg` — **REKONSTRUKTIONSHYPOTHESE [E3/H]** — Handskizze/Interpretation; nicht als Originalschaltplan zu behandeln.

- `testatika reports/D.jpg` — **REKONSTRUKTIONSHYPOTHESE [E3/H]** — Handskizze/Interpretation; nicht als Originalschaltplan zu behandeln.

- `testatika reports/E.jpg` — **REKONSTRUKTIONSHYPOTHESE [E3/H]** — Handskizze/Interpretation; nicht als Originalschaltplan zu behandeln.

- `testatika reports/Linden Experiment diagram.jpg` — **LINDEN-EXPERIMENT / FELDNOTIZ [E1/E3]** — Sekundärer Besucher-/Messbericht bzw. Handskizze zum Linden-Prinzipversuch; wichtige Replikations- und Messunsicherheit.

- `testatika reports/Linden-Experiment-Report-1.jpg` — **LINDEN-EXPERIMENT / FELDNOTIZ [E1/E3]** — Sekundärer Besucher-/Messbericht bzw. Handskizze zum Linden-Prinzipversuch; wichtige Replikations- und Messunsicherheit.

- `testatika reports/Linden-Experiment-Report-2.jpg` — **LINDEN-EXPERIMENT / FELDNOTIZ [E1/E3]** — Sekundärer Besucher-/Messbericht bzw. Handskizze zum Linden-Prinzipversuch; wichtige Replikations- und Messunsicherheit.

- `testatika reports/SEA.jpg` — **VARIANTEN-/FELDNOTIZ [E1/E3]** — Beobachtungs-/Hearsay-Notiz zu Varianten, Elephant oder Aufbauänderungen.

- `testatika reports/fig1.gif` — **SEKUNDÄRDIAGRAMM [E3/H]** — Sekundäres Rekonstruktionsdiagramm, meist Potter-verwandt.

- `testatika reports/fig2.gif` — **SEKUNDÄRDIAGRAMM [E3/H]** — Sekundäres Rekonstruktionsdiagramm, meist Potter-verwandt.

- `testatika reports/fig4.gif` — **SEKUNDÄRDIAGRAMM [E3/H]** — Sekundäres Rekonstruktionsdiagramm, meist Potter-verwandt.

- `testatika reports/fig5.gif` — **SEKUNDÄRDIAGRAMM [E3/H]** — Sekundäres Rekonstruktionsdiagramm, meist Potter-verwandt.

- `testatika reports/fig6.gif` — **SEKUNDÄRDIAGRAMM [E3/H]** — Sekundäres Rekonstruktionsdiagramm, meist Potter-verwandt.

- `testatika reports/luzern folien/Folie1.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie10.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie11.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie12.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie13.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie14.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie15.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie16.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie17.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie18.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie19.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie2.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie20.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie21.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie22.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie23.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie24.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie25.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie26.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie27.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie28.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie29.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie3.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie4.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie5.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie6.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie7.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie8.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/luzern folien/Folie9.JPG` — **HINTERGRUND MESSMETHODIK [R1/X]** — 2005 Unipolar-Generator-Folien; keine Testatika-Geometrie, aber konventionelle Leistungs-/COP-Messungen.

- `testatika reports/marinov.jpg` — **HISTORISCHES FOTO [E0]** — Historisches Foto/Personenbezug; geringe Konstruktionsdichte. Exakt-Duplikatgruppe: Marinov.jpg / testatika reports/marinov.jpg

- `testatika reports/meter magnet.jpg` — **TESTATIKA-BERICHTSMATERIAL [E3]** — Sekundäres Berichtsmaterial.

- `testatika reports/testatika_pancake_fig7.gif` — **SEKUNDÄRDIAGRAMM [E3/H]** — Sekundäres Rekonstruktionsdiagramm, meist Potter-verwandt.

- `testatika reports/update-info.jpg` — **VARIANTEN-/FELDNOTIZ [E1/E3]** — Beobachtungs-/Hearsay-Notiz zu Varianten, Elephant oder Aufbauänderungen.

- `testatika russ..pdf` — **FREMDENTWURF / VARIABLE KAPAZITÄT [H]** — Burenkov-GCT-Entwurf; Testatika-inspiriert, aber kein Beleg für Originalmaschine. Exakt-Duplikatgruppe: testatika russ..pdf / testatika russ.pdf

- `testatika russ.pdf` — **FREMDENTWURF / VARIABLE KAPAZITÄT [H]** — Burenkov-GCT-Entwurf; Testatika-inspiriert, aber kein Beleg für Originalmaschine. Exakt-Duplikatgruppe: testatika russ..pdf / testatika russ.pdf

- `testatika1.doc` — **SEKUNDÄR-KOMPENDIUM [E3]** — Deutschsprachige Übersetzungs-/Kompilationsdatei; enthält viele bereits anderweitig vorhandene Quellen.

- `video/meth1.asf` — **VIDEO-PRIMÄRMATERIAL [E0/E2]** — Archivvideo: direkte visuelle Geometrie; Ton/Narration teils Methernitha-Behauptung. Leistung nicht allein durch Video verifiziert.

- `video/meth2.asf` — **VIDEO-PRIMÄRMATERIAL [E0/E2]** — Archivvideo: direkte visuelle Geometrie; Ton/Narration teils Methernitha-Behauptung. Leistung nicht allein durch Video verifiziert.

- `video/meth3.asf` — **VIDEO-PRIMÄRMATERIAL [E0/E2]** — Archivvideo: direkte visuelle Geometrie; Ton/Narration teils Methernitha-Behauptung. Leistung nicht allein durch Video verifiziert.

- `video/meth4.asf` — **VIDEO-PRIMÄRMATERIAL [E0/E2]** — Archivvideo: direkte visuelle Geometrie; Ton/Narration teils Methernitha-Behauptung. Leistung nicht allein durch Video verifiziert.

- `video/meth5.asf` — **VIDEO-PRIMÄRMATERIAL [E0/E2]** — Archivvideo: direkte visuelle Geometrie; Ton/Narration teils Methernitha-Behauptung. Leistung nicht allein durch Video verifiziert.

- `video/testa01.ram` — **VIDEO-PRIMÄRMATERIAL [E0/E2]** — Archivvideo: direkte visuelle Geometrie; Ton/Narration teils Methernitha-Behauptung. Leistung nicht allein durch Video verifiziert.

- `video/testa02.ram` — **VIDEO-PRIMÄRMATERIAL [E0/E2]** — Archivvideo: direkte visuelle Geometrie; Ton/Narration teils Methernitha-Behauptung. Leistung nicht allein durch Video verifiziert.

- `video/testatikadeutsch.wmv` — **VIDEO-PRIMÄRMATERIAL [E0/E2]** — Archivvideo: direkte visuelle Geometrie; Ton/Narration teils Methernitha-Behauptung. Leistung nicht allein durch Video verifiziert.


---

# ANHANG E — Verschachtelte Archive

## E1 `assembly pics.zip`
35 Dateien. Die 34 technischen GIFs sind bytegleich zu den gleichnamigen Potter-Grafiken in `HTML_UND_BILDER/`; zusätzlich eine separate `Thumbs.db`. Kein zusätzlicher technischer Informationsgewinn.

## E2 `Replications.zip`
2 Dateien, beide bytegleich mit den gleichnamigen Hauptarchiv-DOCs:
- `Testatika - Replication Claim of the Swiss M L.doc`
- `Testatika - Replication Claim of the Swiss ML.doc`

---

# ANHANG F — Glossar

**Antenna key / Taster / Tasten:** Methernitha-Bezeichnung für berührungslose Ladungssammler/Elektroden.  
**Bifilar:** zwei gemeinsam bzw. eng gekoppelt geführte Wicklungsleiter; genaue Verschaltung muss separat angegeben werden.  
**Centerline capacitor:** sekundäre Bezeichnung eines zentralen Kondensatorbereichs in Interpretationszeichnungen.  
**Crystal:** von Baumann laut Marinov/Hauser verwendeter Begriff für ein nicht eindeutig identifiziertes oberes Bauteil/Material.  
**Grid condenser / Gitterkondensator:** Kondensator-/Elektrodenstruktur mit perforierten/meshartigen leitenden Flächen.  
**Influenzmaschine:** elektrostatische Maschine, bei der Ladung durch elektrostatische Induktion getrennt und verstärkt wird.  
**Leydener Flasche:** historischer Hochspannungskondensator.  
**Magnet tube:** Hausers Begriff für den zentralen axialen Magnetstapel innerhalb Pos. 6.  
**Poggendorff-Effekt:** im Testatika-Korpus verwendeter Vergleich zu elektrostatischen Selbstantriebs-/Motorphänomenen; nicht als eigenständige Energiequelle verstehen.  
**Pot:** informelle Bezeichnung für die großen zylindrischen Seitenmodule.  
**T3 / helical transmission line:** Komponenten der Bönisch-Replikation, nicht notwendigerweise Original-Testatika.  
**Wimshurst/Pidgeon:** klassische Influenzmaschinen als mechanisch-elektrostatische Vergleichsmodelle.

---

# ANHANG G — Offene Forschungsprioritäten

Priorität 1:
- Original-/höher aufgelöste Hauser-Zeichnungen und Fotos finden;
- Pos. 6 eines konkreten Modells zerstörungsfrei/CT-artig dokumentieren;
- exakte Elektrodenwinkel und Scheibenabstände vermessen;
- Materialanalyse der Sektoren und Gitter.

Priorität 2:
- Pos. 12 optisch/spektroskopisch identifizieren;
- Pos. 9 als C/L/R/HF-Bauteil charakterisieren;
- Hufeisenwicklungen und Zwischenplatten vollständig vermessen.

Priorität 3:
- eine energiearme 50-cm-Geometrie nachbauen;
- zunächst nur \(C(t)\), induzierte Ladung, Spektren und mechanisches Gegenmoment messen;
- danach definierte Resonanz-/Gleichrichterstufen testen;
- jede Stufe mit vollständiger Energiebilanz.

---

# ANHANG H — Qualitätsstandard für zukünftige Ergänzungen

Neue Informationen werden nur eingepflegt, wenn mindestens folgende Metadaten festgehalten werden:

1. Dateiname/Quelle;
2. Datum/Urheber, soweit bekannt;
3. welches Maschinenmodell betroffen ist;
4. direkte Beobachtung vs. Interpretation;
5. exakter Wortlaut bei kritischen Zahlen;
6. Widerspruch zu vorhandenen Quellen;
7. Evidenzcode E0/E1/E2/E3/R1/H/X;
8. Änderung am Gesamtmodell;
9. offene Unsicherheit.

**Keine spekulative Rekonstruktionszeichnung darf künftig ohne Kennzeichnung in den Bereich „Originalaufbau“ übernommen werden.**

---

# Schlussstatus

Diese Version ist die erste **archivweite, widerspruchsbereinigte und replikationskritische** `state.md` des vorliegenden Korpus. Sie ist deutlich näher am dokumentierten Originalbestand als die frühere Fassung, weil sie nicht mehr versucht, widersprüchliche Gerätevarianten in eine einzige vermeintlich sichere Schaltung zu zwingen.

Der wichtigste technische Befund bleibt:

> Der sichtbare und reproduzierbare Kern der Testatika ist elektrostatisch: segmentierte rotierende Scheiben, berührungslose Gitter-/Kollektorelektroden und variable kapazitive Feldkopplung. Eine nachgeschaltete Speicher-/Resonanz-/Transformationsstruktur ist sehr wahrscheinlich, aber ihre exakte Originalschaltung ist nicht überliefert. Die im Korpus behaupteten Kilowatt-Leistungen wurden durch die enthaltenen kontrollierten Replikationen nicht bestätigt.


---

# ANHANG I — Potter-Grafikkorpus: Funktionszuordnung der einzelnen Diagrammgruppen

Die GIF-Dateien in `HTML_UND_BILDER/` sind größtenteils Illustrationen zu Paul E. Potters Back-Engineering-Seiten. Sie sind **keine Original-Baumann-Schaltpläne**. Ihre Bedeutung ist:

- `fullcircit.gif` / `fullcircit_testatika.gif`: Potters komplette zusammengesetzte Gesamtrekonstruktion. Beide Dateien sind exakt identisch.
- `circuit.gif`: elektromagnetische Hilfs-/Transformationsschaltung mit Spulen-, Kondensator-, Magnet-/ECG- und Ausgangsblöcken; Hypothese.
- `recircuit.gif`: Variante/Reduktion der Rectifier-/Ausgangsschaltung; Hypothese.
- `rect.gif`: Potters Erklärung einer Gleichrichter-/Valve-Baugruppe; thermionische Interpretation.
- `discharger.gif`: grafische Rekonstruktion des oberen Entladers/„single filament rectifier“.
- `fig1.gif`: zusammengesetzter grundlegender Testatika-Aufbau mit Ober-/Unterteilen, Antenna-Keys, Induktions-/Magnet-/Kondensatorblöcken.
- `fig2.gif`: Vergleich einer auf Methernitha konfigurierten Pidgeon-Anordnung mit Pidgeon- und Wimshurst-Maschine.
- `fig3.gif`: Potters Vollschaltungs-/Blockrekonstruktion.
- `fig4.gif`: „Tower circuits“ — hypothetische innere Schaltung der oberen/turmförmigen Bauteile.
- `fig5.gif`: Elektronenlawinen-/„electron cascade“-Illustration.
- `fig6.gif`: geschichteter Dielektrikum-/Partikelblock im Feld; Flanagan-/ECG-Hypothese.
- `fig7.gif`: hypothetischer Innenaufbau des großen Pot/Zylinders mit Pancake-Wicklungen, Ringmagneten, Gittern, Abschirmungen.
- `linden.gif`: kolorierte Illustration des Linden-Experiments mit Hufeisenmagnet, Drahtschleife, Al/Isolator/Cu-Stapel und Voltmeter.
- `principle.gif`: Potter/Holzherr-Darstellung des schwenkenden Gitter-/Plexiglas-Prinzipversuchs.
- `pulse.gif`: Pulsformungs-/LC-Kettenanalogie für einen mehrlagigen Basiskondensator.
- `nonuni1.gif`: Feldlinien-/Teilchenillustration zu nichtuniformen elektrostatischen Feldern.
- `cas1.gif`, `cas2.gif`: Polarisations-/Elektronenkaskaden-Schemata; theoretischer Hintergrund.
- `efg2.gif`, `efg3.gif`: patentähnliche Schichtquerschnitte zur Flanagan-Electron-Cascade-Hypothese.
- `elect2.gif` … `elect7.gif`: Electret-/Polarisation-/Gleichrichter-/Schichtmodelle; theoretische Nebenhypothese, nicht Originaltestatika.
- `eguchi1.gif`: historische Electret-Geometrie nach Eguchi; Hintergrund.
- `orse1.gif` … `orse5.gif`: mehrere Hufeisenmagnet-/Spulen-/Schwingkreis-Modelle und Spannungsverteilungsdiagramme; Potter-Hypothesen.
- `blu.gif`, `date.gif`, `index.gif`, `title.gif`, `titlestill.gif`: Navigations-/Titel-/Dekorgrafiken, ohne neue Maschinengeometrie.

Der Korpus enthält diese Diagramme zusätzlich in `assembly pics.zip`; dort entsteht kein weiterer unabhängiger Informationsgewinn.

---

# ANHANG J — Feldnotizen und `testatika reports/` im Detail

## J1 `1.jpg`
Handschriftliche Messnotiz „Messungen an ML-Konverter Linden“:
- Leerlaufspannung etwa 770 V DC;
- angegebene kalte Last etwa 180,5 Ω;
- Lastspannung etwa 580 V DC;
- daraus notiert/berechnet etwa 3,2–3,3 A;
- Bezug auf mittlere Maschine.
Keine vollständigen Angaben zu Messgerät, zeitlichem Verlauf, Temperaturkoeffizient oder Eingangsleistung.

## J2 `2.jpg`
Skizze einer angenommenen Wimshurst-/Erreger- und Spulenverschaltung. Rekonstruktiv; keine nachgewiesene Originalverdrahtung.

## J3 `3.jpg`
Handnotizen zu magnetischer Hysterese/Schleifen, Resonanz/Transformator- und Wellenvorstellungen. Theoretische Interpretation.

## J4 `4.jpg`
Weitere zusammengesetzte Spulen-/Kondensator-/„inverted pressure“-Schaltung. Hypothese, nicht Original.

## J5 `5.jpg`
Feldnotizen:
- Behauptung eines Chefingenieurs, Baumanns Modelle hätten wenigstens einen Magneten; steht im Konflikt zu Marinovs kleinem Modell.
- 1993 Sichtung des großen 2-m-„Elephant“ und unfertiger kleiner Modelle.
- Hearsay, dass früheste Baumann-Versuche hin- und herbewegte/reziproke Mechanik hatten.
- Skizze eines frühen Schwenk-/Magnet-/Plattenprinzips.

## J6 `6.jpg` und `6(1).jpg`
Linden-Experiment-Feldnotizen:
- Hufeisenmagnet;
- Drahtwicklung/Schleife;
- verschieblicher Al/Papier/Cu-Stapel;
- mehrere hundert Volt behauptet;
- Berichtautor konnte Effekt nicht zuverlässig reproduzieren;
- mögliche Messartefakte werden diskutiert.

## J7 `7.jpg` und `7(1).jpg`
Weitere Linden-Skizzen:
- ungefähr 10–25 bzw. 20–30 Windungen je nach Lesart;
- isolierter Installationsdraht um Hufeisen;
- Cu/Papier/Al-Kondensator;
- Grid-Dip-Meter-Resonanzangabe grob 80–140 MHz.
Die Resonanzangabe ist Bericht/Hearsay, keine gesicherte Messung am Hauptgerät.

## J8 `A.jpg`
„Elephant“-Feldzeichnung:
- ca. 2-m-Scheibenklasse;
- mehrere Elektroden E1…;
- Magnete M1…;
- Riemen-/Antriebssystem;
- Vergleich verschiedener Bauzustände um 1992–1994.
Belegt Entwicklungs-/Umbaucharakter, nicht 30-kW-Leistung.

## J9 `B.jpg`
Hypothese:
- Wimshurst/Scheiben könnten nur das System „biasen“;
- eigentliche Leistung aus AC-/Magnet-/Spulenteil.
Nicht beobachtete Originalfunktion.

## J10 `C.jpg`
Handschriftliche Pot-/„capacitive transformer“-Rekonstruktion:
- mehrere Pancake-Coils;
- extrem hohe Windungszahlen werden als von Informanten genannte Größen notiert;
- Magnet-/Luftspaltanordnung;
- Zahlen/Handschrift teilweise nicht eindeutig.
Diese Seite ist Ursprung mehrerer späterer Pot-Schnittbilder; sie darf nicht als vermessener Originalquerschnitt gelten.

## J11 `D.jpg`
Notizen zu magnetischen Lamellen:
- dünnes magnetisches Stahl-/Sektormaterial;
- Perforationsmuster;
- Magnetorientierung angeblich nach Baumann;
- mögliche Widerstandsverbindungen an Segmentenden werden handschriftlich angedeutet, Werte jedoch nicht eindeutig lesbar.
Status: Beobachtung + Hypothese vermischt.

## J12 `E.jpg`
„Luzi Cathomen’s private project“/freier Konverterversuch:
- Al/Cu-/Elektromagnet-/Kondensatorideen;
- **kein Original-Testatika-Schaltplan**.

## J13 `SEA.jpg`
Space Energy Newsletter, März 1992:
- Foto des großen Projekts;
- „newest and largest“;
- projektiert 30 kW;
- Bezug auf SEA Award.
Promotional, kein Messprotokoll.

## J14 `update-info.jpg`
Sekundäre Zusammenfassung:
- obere Röhre möglicherweise nicht klassischer Gleichrichter;
- kleine Funken im Scheibenbereich;
- Collector berührt Scheibe nicht;
- Reservoir-/Kondensatoridee;
- zwei Permanent-U-Magnete/Transformatorblöcke;
- Wicklungen grob 20–30 Windungen;
- Plexiglas-/Gitterlagen;
- Tachosensor.
Nützlich als Hinweisaggregation, nicht Primärquelle.

## J15 `meter magnet.jpg`
Foto eines U-/Hufeisenmagneten mit Beschriftung, dass ein „meter magnet“ für das Linden-Experiment benutzt worden sei. Belegt den verwendeten Magnettyp der Replikations-/Demonstrationsbeschreibung, nicht die Hauptmaschine.

## J16 `fig1.gif`, `fig2.gif`, `fig4.gif`, `fig5.gif`, `fig6.gif`, `testatika_pancake_fig7.gif`
Sekundäre Potter-/Rekonstruktionsgrafiken; inhaltlich entsprechen sie den oben beschriebenen Pidgeon-, Gesamt-, Tower-, Electron-Cascade-, Schicht- und Pot-Modellen.

---

# ANHANG K — Marinov-/Kelly-Scanserie Seite für Seite

Die neun PNGs `marinov_1of9.png` … `marinov_9of9.png` sind Seiten eines Zeitschriftenkonvoluts.

- **Seiten 1–6:** Stefan Marinov, „Methernitha und Testatika“. Historischer Augenzeugen-/Meinungstext. Marinov deutet Testatika als Kopplung elektrostatischen Motors und Generators, verweist auf Poggendorff und argumentiert stark zugunsten einer Verletzung der üblichen Energiebilanz. Er liefert jedoch keine vollständige technische Zeichnung und räumt Verständnislücken ein.
- **Seite 6:** enthält Foto/Caption eines größeren Modells mit Leistungsbehauptung im Bereich 3–4 kW; redaktionelle/sekundäre Angabe.
- **Seiten 7–8:** Don Kelly, „Der Schweizer ML-Konverter“. Enthält die bekannte Kelly-Schaltung mit Scheibe, Hufeisenmagneten, Crystal-Diode/Kondensator und Leydener Transmitter/Receiver sowie sekundäre Spezifikationen.
- **Seite 9:** thematisch nicht mehr Testatika („Lungenkrebs durch KAT?“); für die technische Wissensbasis ausgeschlossen.

`marinov.pdf` ist ein Scancontainer ohne brauchbaren Textlayer; die technische Auswertung stützt sich deshalb auf die neun Bildseiten.

---

# ANHANG L — Kleine Schwenkarm-/Frühform-Replika (`arm/`)

Die Dateien `8dc1.jpg`, `ba69.jpg`, `ba3b.jpg`, `58eb.jpg`, `6234.jpg` beschreiben/fotografieren eine kleine unfertige Replika, die in der Beschriftung als Nachbildung eines sehr frühen Baumann-Geräts bezeichnet wird.

Erkennbar/angegeben:
- hölzerne Basis, außen mit Aluminiumgitter;
- zwei Aluminium-„capacitor containers“;
- Hufeisen-Permanentmagnet, etwa 4 × 2,5 cm in einer Zeichnung;
- in einer Phase ausdrücklich „no coils yet“;
- schwenkender/panning arm aus Holz;
- Aluminiumgitterabdeckung;
- teilkreisförmiges Acrylstück mit Sensor-/Nut;
- Lagerung, „thorn/pin“, Holzpfosten;
- Breite ungefähr 24 cm, Gesamthöhe ungefähr 20 cm, Behälterhöhe ungefähr 12 cm in den Zeichnungen.

Die Legende, Baumann habe mit einem solchen Gerät im Gefängnis eine kleine Lampe eine Zeit lang leuchten lassen, ist **historische Überlieferung/Hearsay**, kein verifizierter Leistungsnachweis.

---

# ANHANG M — Direkte Fotoquellen, Einzelbewertung

- `front.jpg`: kleine Frontansicht einer größeren Testatika; bestätigt symmetrische Seitenzylinder, zentrale Scheibe, unteren Magnet-/Spulenbereich.
- `3kwfront.jpg`: Frontbild einer als 3-kW-Variante bezeichneten Maschine; niedrigauflösend, geometrisch konsistent mit anderen Fotos.
- `3kwrear.jpg`: Rückansicht; wichtig für lange vertikale Röhren/Spiralbauteile und rückwärtige Träger.
- `testabig.jpg`: beste hochauflösende Frontquelle des Korpus; siehe Abschnitt 17.1.
- `TESTA7.jpg`: alternative größere Variante; siehe Abschnitt 17.2.
- `TESTA9.jpg`: Seiten-/Rückkomposit; siehe Abschnitt 17.3.
- `f31.jpg`: Nahaufnahme mehrlagiges perforiertes Paneel; siehe Abschnitt 17.4.
- `glow.jpg`: leuchtendes oberes Rohr-/Spulenelement; Funktion offen.
- `Leid-flasch_bau.jpg`: generische Leydener-Flaschen-Skizze mit Aluminiumfolie, Isolation, Masse; Hintergrund, nicht Originaldetail.
- `Marinov.jpg` / `testatika reports/marinov.jpg`: exaktes Duplikat eines historischen Marinov-/Gerätefotos; geringe konstruktive Zusatzinformation.

---

# ANHANG N — Nicht-Testatika-Hintergrundquellen und warum sie nicht in den Originalaufbau übernommen werden

## `Bernhard_Gross_electret_research[2].doc`
Technisch seriöser Electret-Hintergrund zu langzeitiger Polarisation, Ladungsspeicherung und dielektrischer Absorption. Relevanz: kann Materialhypothesen erklären. Keine direkte Aussage, dass Baumann Electrete verwendete.

## `HTML_UND_BILDER/eguchi.htm` + `eguchi1.gif`
Historischer Electret-Hintergrund. Keine Testatika-Primärquelle.

## `Electrostatic Motors-Oleg Jefimenko.mht`
Allgemeine Elektrostatik-/Atmosphärenenergie-/Motorinformation. Hilfreich für konventionelle Vergleichsphysik, keine Originalmaße.

## `Wimshurst Machines-tesla.mht` + `constructiontips.txt`
Klassische Influenzmaschinen-/Nachbauinformation. Hilfreich für Scheiben, Neutralisatoren, Ladungssammler und Feuchtigkeitseffekte; keine Baumann-BOM.

## `HTML_UND_BILDER/elecfg.htm` / `electroncasc.htm`
Flanagan-/Electron-Cascade-Hintergrund; nur Hypothesentest.

## `De Keely ...mht`
Historisches Fremdthema, nicht in Testatika-Rekonstruktion übernommen.

## `meg.pdf` / `meg_patent.pdf`
Magnetic Energy Generator/MEG; anderes Prinzip, ausgeschlossen.

## `EssentialSvali.pdf` / `svali.pdf`
Kein technischer Testatika-Bezug, ausgeschlossen.

## `marinov.txt`
Marinovs allgemeine alternative-physikalische Positionen; nicht als Konstruktionsevidenz verwendet.

## `marinov1.exe` / `marinov2.exe`
Nicht ausgeführt. Binärdateien liefern für diese Wissensbasis keine geprüfte Testatika-Evidenz.

---

# ANHANG O — Verifikationslogik für Leistungsbehauptungen

Eine Behauptung wie „1000-W-Lampe leuchtet“ wird in dieser Datei in drei Ebenen getrennt:

1. **Lastklasse bekannt:** z. B. Lampe mit Nennaufdruck 1000 W.
2. **Lastverhalten beobachtet:** Lampe erscheint hell.
3. **tatsächliche elektrische Leistung gemessen:** erfordert RMS-/Momentanwerte, Wellenform, Power Factor bzw. kalorimetrische Kontrolle.

Im vorhandenen Originalkorpus sind Ebene 1 und 2 mehrfach vorhanden. Ebene 3 ist für die behaupteten Kilowatt-Testatika-Ausgänge **nicht ausreichend dokumentiert**.

Analog gilt für Heizwiderstände:
\[
P = \frac{V^2}{R}
\]
nur dann zuverlässig, wenn \(R\) **bei Betriebstemperatur** und die tatsächliche Wellenform/Spannung korrekt gemessen wurden. Ein Kaltwiderstand von 180 Ω und 580 V liefert rechnerisch ~1,87 kW, aber der Widerstand eines glühenden Heizers kann stark ansteigen; die Drittquellenangabe ~3 A kann daher nicht ohne Messdetails als präzise 1,74-kW-/1,9-kW-Messung behandelt werden.

---

# ANHANG P — Derived Data / Rechenwerte

Für die 500-mm-Scheibe:

- Radius: 250 mm
- Umfang: 1570,8 mm
- 50er Winkelteilung: 7,2°
- 50er Umfangsteilung am Rand: 31,416 mm
- Umfangsgeschwindigkeit bei 60 rpm: 1,571 m/s
- Umfangsgeschwindigkeit bei 15 rpm: 0,393 m/s

Bei 50 Segmenten:
- 60 rpm → 50 feste Segmentpassagen/s
- 15 rpm → 12,5 feste Segmentpassagen/s
- zwei gleich schnelle Gegenläufer → relative Musterrate 100/s bzw. 25/s

Bei 60 Segmenten:
- 60 rpm → 60 feste Segmentpassagen/s
- Gegenläufer → relative Musterrate 120/s

Aus 300 V × 10 A:
- rechnerisch 3,0 kW, **nur wenn beide Werte gleichzeitig unter realer Last gemessen wurden**.

Offizielle 3–4 kW bei 270–320 V entsprächen grob Strömen von etwa:
- 3 kW / 320 V = 9,4 A
- 4 kW / 270 V = 14,8 A

Diese Stromwerte sind **abgeleitet aus einer unbestätigten Leistungsbehauptung**, nicht zusätzliche Messwerte.


---

# 92. V2-Fotogrammetrie — erste kleine Marinov-Maschine

**Referenzgerät:** erste kleine Maschine rechts in Marinovs Fig. 13/14; dies ist die Maschine, die Marinov selbst testete.

### Neu festgehalten
- Ein-Scheiben-Maschine, Rotor ungefähr 200 mm.
- frühe Sektoren: einfache Kupferdrähte, ungefähr 1 mm.
- Sektorzahl: ca. 20–30; spätere Marinov-Korrespondenz ca. 20–25.
- entscheidender offener Punkt: Marinov betont, es sei sehr wichtig, wie die Drähte **durch die Scheibe** gehen; genaue Führung nicht überliefert.
- keine Schleifbürsten; feste mechanische Kopplung nur über Lager.
- Korrektur: die **erste kleine Maschine rechts besitzt Hufeisenmagnete**; die zweite links nicht.
- Seiten-Pots: äußere Zylinder-/Gitterelektrode + Dielektrikum + innere dicke Kupferspirale.
- Crystal vorhanden, Funktion unbekannt; one-way-gate ist nur Marinovs Hypothese.
- keine belastbare Tesla-/HF-Kernfunktion.
- Driving- versus Collecting-Elektroden bleibt ungeklärt.

### Fotogrammetrische V2-Arbeitsmaße
Aus Abb. 14 mit der 200-mm-Scheibe als Skalierungsanker:
- Basisbreite ~370 mm;
- Basistiefe als Arbeitsmaß 180 mm;
- Pot-OD ~84 mm;
- Pot-Körperhöhe ~110 mm;
- Rotorzentrum ~160 mm über Basis;
- Gesamthöhe etwa 280 mm.

Die photo-abgeleiteten Maße haben typischerweise ±10–15 % Unsicherheit.

### V2-CAD
- Rotoren mit 20, 24 und 25 Drahtpositionen;
- R0–R3-Drahtführungsvarianten;
- verstellbare sektorielle Elektroden;
- zwei Hufeisenmagnet-Halter;
- zwei photo-skalierte Pots;
- austauschbares Crystal-Modul;
- separater rückwärtiger Shield-Test;
- STEP + STL.

**Status:** bestmögliche fotogrammetrische Forschungsreplik. Eine historisch gesicherte vollständige Verdrahtung ist weiterhin nicht verfügbar.

# 93. V6 – Stefan Hartmann / Overunity.com: Quellenrolle und Archivgrenzen

Die V6-Erweiterung untersucht Stefan Hartmann und `overunity.com` separat vom Marinov-/Hauser-/Holzherr-Primärkorpus. Das ist notwendig, weil Hartmann zugleich **Archivar/Verteiler**, **Fragensteller/Übersetzer** und später **eigener Hypothesenautor** war.

Quellenklassen:

- **H1:** direkt von Hartmann verfasster, datierter Text/Interview;
- **H1-M:** als Hartmann-Mail gekennzeichneter historischer Mirror;
- **W1:** zeitnaher Augenzeugenbericht, den Hartmann nur erfragte/übersetzte;
- **A1:** Archiv-/Hostingbeleg für Thread oder Medium;
- **S2:** spätere Sekundärzuschreibung ohne gefundenes Originalprotokoll.

Wichtig: Das heutige `overunityarchives.com` ist nur eingeschränkt durchsuchbar und weist auf kostenpflichtigen Vollzugang hin. Deshalb ist dieser Audit **kein Anspruch auf vollständige Auswertung jedes historischen Overunity-Posts**. Belegt sind aber der historische Testatika-Threadpfad `topic 75`, mehrere auf Overunity gehostete Testatika-Filmdateien und die direkte Hartmann-Holzherr-Übertragungskette.

Vollständiges Dossier: `docs/research/hartmann-overunity-testatika.md`  
Quellenledger: `docs/research/hartmann-overunity-sources.tsv`

# 94. V6 – Hartmann-Zeitachse 1992 → 1999 → 2000 → später → 2008

## 1992
Hartmann vergleicht William Hydes US-Patent 4,897,592 (`Electrostatic Energy Field Power Generating System`) mit der Testatika und verweist auf eine von ihm zuvor erstellte Testatika-SVGA-Animation. Sein früher Deutungsrahmen ist damit klar **elektrostatisch / Rotor-Stator / variable Kapazität**. Er äußert gleichzeitig Skepsis gegenüber einer 900-%-Hyde-Behauptung.

## 1999
Hartmann befragt Hans Holzherr nach dessen Methernitha-Besuch, übersetzt/verteilt die Antworten und fragt um Erlaubnis, ein Bild auf `overunity.com` zu hosten. Die technischen Beobachtungen sind Holzherrs, nicht Hartmanns.

## Juni 2000
Hartmann formuliert ein **Electret-/Influenz-Modell**: Plexiglas/Gitter als polarisierte dielektrische Struktur, `Taster` als nichtkontaktierende Influenz-Pickups, elektrostatische Ausrichtung/Restmoment, phasenabhängige Umpolung/Impulse und kapazitive Spannungsumformung.

## später, im gefundenen Mirror undatiert
Hartmann wechselt zu einer **schwach-radioaktive-Mineralien-/Beta-Elektronen-Hypothese**.

## 2008
Hartmann bezeichnet in einem Interview `negative resistance` und angeregten radioaktiven Zerfall/Beta-Elektronen als Haupteffekt bei Moray und Methernitha/Testatika.

**Quellenkritische Konsequenz:** Es existiert nicht eine unveränderte „Hartmann-Geheimtheorie“. Seine Erklärung änderte sich materiell.

# 95. V6 – 1999 Holzherr über Hartmann: was neu für die Provenienz ist

Die 1999er Korrespondenz belegt explizit:

- Hartmann fragt Holzherr, ob er dessen Bild auf den `overunity.com`-Server stellen dürfe;
- Hartmann kündigt an, Holzherrs E-Mails ins Englische zu übersetzen und in Free-Energy-Listen zu posten;
- Holzherr stimmt zu;
- Holzherr bezeichnet sich selbst als Zeugen, der die Funktion nicht absolut beweisen könne;
- Holzherr kann eine versteckte Batterie nicht messtechnisch ausschließen;
- Baumann verneint laut Holzherr ausdrücklich **Radiumchlorid** als Energiequelle;
- Hartmann fügt damals hinzu, dass er Nelson Camus' Radiumchlorid-Geschichte stark bezweifle.

Damit ist `overunity.com` historisch als **Distributionsknoten** belegt, nicht als unabhängige Messinstanz.

Weitere Holzherr-Punkte bleiben hochrelevant: ca. 15 rpm bei diesem Besuch, Principle Experiment mit perforiertem Gitter, ungefähr 60 V nach mehreren Schwenks, Aussage `Vollfolie funktioniert nicht`, kleine Ein-Scheiben-Varianten, eingewebte Drahtsektoren und die schwierige nicht-wissenschaftliche Erklärsprache Baumanns.

# 96. V6 – Hartmanns Juni-2000-Electret-Modell: technisch wertvollster Teil

Hartmanns 2000er Hypothese konvergiert überraschend gut mit dem heutigen V5-Arbeitsmodell, obwohl sie **keine Primärbeschreibung des Originalgeheimnisses** ist:

1. Plexiglas/Dielektrikum trägt einen persistenten oder langsam relaxierenden Ladungs-/Polarisationszustand;
2. Rotor und feste Elektroden bilden eine winkelabhängige Kapazitätsmatrix `C_ij(theta)`;
3. `Taster` koppeln berührungslos über Influenz/Displacement Current;
4. Gitter/Lochbleche formen Feld, Oberflächenladung, Corona und Raumladung anders als Vollfolie;
5. ein nichtlineares Element (`crystal`/Diode) kann Ladung nur in ausgewählten Phasen weiterleiten;
6. getrennte Hochspannungs-Bias- und niedrigere Speicher-/Lastzustände sind möglich;
7. Kondensatorstufen können Spannung/Strom/Impedanz umformen, ohne Energie zu erzeugen.

Das stärkt **H11/H27/H28/H30/H32** aus V5 und führt zu H36–H38 unten.

# 97. V6 – Quantitativer Audit des `capacitive transformer`-Beispiels

Hartmann nennt: `1 µF @ 1000 V` wird auf `100 µF` entladen → ungefähr `10 V` und höhere Stromfähigkeit.

Für direkte Ladungsteilung gilt:

`V_f = C1*V1/(C1+C2) = 9.90099 V`.

Die Spannungsaussage stimmt größenordnungsmäßig. Die Energie jedoch:

- `E_i = 0.5 J`
- `E_f = 0.0049505 J`
- Differenz `≈ 0.49505 J = 99.01 %` der Anfangsenergie.

Bei einfacher dissipativer Ladungsteilung wird diese Differenz in realen Schalt-/Leitungs-/Strahlungsmechanismen verloren. Ein guter Wandler kann Hochspannung gegen höheren Strom bei niedrigerer Spannung tauschen, aber die Energie nicht vervielfachen.

**V6-Bewertung:** Die Form spezieller Testatika-Kondensatoren bleibt als Impedanz-/Feldgeometrie relevant. `Großer C bei kleinerem V` ist **kein Energiegewinnmechanismus**.

# 98. V6 – Gitter/Luftionen: wertvolle Geometriehypothese, schwache Energiequellenhypothese

Hartmann vermutet 2000, Gitter ließen ionisierte/polarisierte Luft besser an die Electret-Oberfläche koppeln und nennt ungefähr `10^23 Moleküle/cm³`.

Korrektur über ideales Gas bei ungefähr Raumtemperatur und 1 atm:

`n ≈ 2.5 × 10^19 Moleküle/cm³`.

Hartmanns Zahl ist damit ungefähr vier Größenordnungen zu hoch. Zudem ist normale Luft überwiegend neutral; aus der Moleküldichte folgt keine entsprechende frei verfügbare Ladungsdichte.

Trotzdem ist die Gitterspur experimentell stark, weil Mesh/Lochblech gegenüber Vollfolie ändern kann:

- lokale Feldspitzen;
- effektive Kapazität;
- Corona-/Ionisationsschwelle;
- Luft-/Ionentransport;
- Oberflächenladung;
- Leck- und Relaxationspfade.

**Priorität:** geometriekontrollierter Mesh-vs-Lochblech-vs-Folie-A/B-Test bleibt hoch. Ein Unterschied beweist zunächst nur einen Feld-/Transporteffekt.

# 99. V6 – Spätere Radioaktivitäts-/Betavoltaik-Hypothese Hartmanns

Ein späterer undatierter Hartmann-Kommentar im gleichen historischen Mirror behauptet/hypothetisiert, gepulste Hochspannung könne schwach radioaktive Mineralien/Gesteine in Testatika-Baugruppen stimulieren, sodass Beta-Elektronen von Drähten/Gittern gesammelt würden.

V6-Quellenbewertung:

- mehrfach spekulative Formulierungen (`probably`, `must be`);
- keine gefundene Testatika-Materialanalyse;
- keine Isotopenidentifikation;
- keine Dosis-/Aktivitätsmessung;
- keine geschlossene nukleare Energiebilanz;
- spezifische Radiumchlorid-Geschichte war 1999 laut Holzherr von Baumann verneint worden und wurde damals auch von Hartmann bezweifelt.

Betavoltaik selbst ist reale Physik: Betaenergie eines **konkreten Radioisotops** wird in elektrische Energie umgewandelt. Publizierte Modelle rechnen Isotop, Aktivität, Spektrum, Geometrie und Selbstabsorption explizit. Eine Hochleistungsarbeit nennt für 0.1-W- bis Watt-Niveaus Radioisotopenbeladungen >`10^13 Bq`.

**Konsequenz:** Selbst bei Nachweis radioaktiver Komponenten wäre die Energiequelle Kernzerfall, nicht Overunity. Für dieses Replikationsprojekt werden **keine radioaktiven Stoffe beschafft oder eingesetzt**.

# 100. V6 – `negative resistance` bei Hartmann 2008

Hartmann verbindet 2008 Testatika/Moray mit `negative resistance` und angeregtem radioaktivem Zerfall/Beta-Elektronen.

Negative differentielle Widerstandskennlinien sind real, aber keine selbständige Energiequelle. Reale NDR-Bauelemente oder aktive negative Impedanzen benötigen Bias/Pumpenergie oder setzen gespeicherte Energie um. Eine radioaktive NDR-/Verstärkerhypothese müsste wiederum die Kernzerfallsenergie bilanzieren.

**Status:** historisch wichtig für Hartmanns spätere Position; niedrig als Beweis für die Testatika.

# 101. V6 – Kristallspur: neue, aber sekundäre Hartmann-Zuschreibung

Rimstar führt eine Aussage, Hartmann habe Methernitha besucht und dort erfahren, das Geheimnis liege in den Kristallen. Im aktuellen Audit wurde **kein originales Hartmann-Besuchsprotokoll** gefunden, das diese konkrete Aussage verifiziert.

Daher:

- nicht als Baumann-Fakt behandeln;
- nicht als Hartmann-Primärbeobachtung behandeln;
- als **S2-Suchspur** erhalten;
- mit der bereits starken unabhängigen Tatsache trennen, dass Marinov/Baumann tatsächlich ein unbekanntes `crystal` erwähnen.

# 102. V6 – Neue Hypothesen H36–H42

**H36 — electretartige Rotorpolarisation / persistente Dielektrikum-Ladungszustände**  
Status: **mittel bis mittel-stark** als testbare Sekundärhypothese. Keine Evidenz, dass das Original zwingend thermisch hergestellte Electrets verwendete.

**H37 — Gittergeometrie koppelt/ordnet relevante Oberflächen-/Raumladung besser als Vollfolie**  
Status: **mittel-stark als Geometrie-/Transporthypothese**, niedrig als externe Energiequelle.

**H38 — `capacitive transformer` als Spannungs-/Impedanzkonditionierung**  
Status: **mittel**. Keine Energievervielfachung; vollständige Ladungs-/Energiebilanz erforderlich.

**H39 — schwach radioaktive Mineralien als Testatika-Kern**  
Status: **niedrig**. Hartmann-Späthypothese ohne Testatika-spezifische Material-/Strahlungsbefunde.

**H40 — negative resistance / stimulierter Zerfall als Kernmechanismus**  
Status: **niedrig**. Keine Testatika-Kennlinie oder Isotopen-/Leistungsbilanz.

**H41 — `Kristalle sind das Geheimnis`, Hartmann-Besuch**  
Status: **mittel-niedrig als Suchspur**, nicht verifiziert als Primärquelle.

**H42 — overunity.com als historischer Testatika-Medien-/Diskussionsknoten**  
Status: **stark**. Thread- und Dateipfade sowie Hartmann-Holzherr-Korrespondenz mehrfach erhalten.

# 103. V6 – Arbeitskonsens nach Hartmann-/Overunity-Audit

Die neue Recherche verändert den V5-Kern **nicht** in Richtung Tesla/HF oder Radioaktivität. Sie stärkt vielmehr eine konventionell testbare elektrostatische Rekonstruktion:

> **persistenter Dielektrikum-/Oberflächen-Ladungszustand → winkelabhängige Kapazitätsmatrix → berührungslose Taster/Influenz → Gitter-Feldformung → phasenselektives Crystal/Diode-Charge-Gating → getrennte Bias-/Speicherzustände → kapazitive/induktive Impedanzkonditionierung.**

Hartmanns Juni-2000-Electret-Modell ist hierfür eine wertvolle **sekundäre** Konvergenzquelle. Seine Luftionen-kW-Erklärung, spätere Radioaktivitätstheorie und Negative-Resistance-Deutung liefern dagegen derzeit **keinen geschlossenen Energiequellennachweis**.

Neue Forschungspriorität:

1. dielektrische Ladungs-/Polarisationsrelaxation messen;
2. Mesh/Lochblech/Folie kontrolliert vergleichen;
3. Metallplatten-Grenzbedingung wiederholen;
4. getrennte Drive-/Pickup-Elektroden testen;
5. Crystal/Diode als phasenselektives Charge-Gate testen;
6. Kondensatorstufen mit vollständiger Energie-/Ladungsbilanz prüfen;
7. erst danach Magnet-/Spulen-Zusatzstufen untersuchen.

**Keine radioaktiven Materialien im Replikationspfad.**

# 104. Repository hardening / public-corpus boundary — 2026-08-16

**Korrekturhinweis zu älteren Repository-Metadaten:** Frühere Abschnitte dieses kumulativen Ledgers nennen Arbeitsdateien wie `testatika.zip` und `state_pre_corpus_rebuild.md`. Diese Hinweise bleiben aus Preservation-Gründen stehen, dürfen aber nicht so gelesen werden, als lägen die Originalbytes heute im öffentlichen Git-Tree.

- `testatika.zip` bezeichnet einen historisch verwendeten externen Forschungskorpus mit Drittmaterial. Er ist **not part of the public repository / nicht Bestandteil des öffentlichen Repositories**, weil Redistribuierungsrechte für enthaltene Scans/Bücher/Bilder nicht pauschal geklärt sind.
- `state_pre_corpus_rebuild.md` wird in älteren Projektnotizen als Sicherung genannt; im auditierten öffentlichen Tree lag diese exakte Datei nicht vor. Es wird **kein Ersatzinhalt erfunden**. Falls eine authentische Kopie wiedergefunden wird, ist sie bytegetreu mit Hash/Provenienz zu archivieren.
- Der öffentliche Reproduzierbarkeitsrahmen ist jetzt in `docs/research/external-corpus.md` dokumentiert.
- Historische Recovery-Anker sind Git-History und `snapshot-main-*`-Tags; temporäre Konsolidierungsbranches sind nicht mehr als dauerhaft existierende Branches vorauszusetzen.

## 104.1 1:1-Begriff

Der verbindliche Vollständigkeitsstatus der kleinen Marinov-Maschine M2 steht in `docs/REPLICATION_STATUS.md`. Eine **vollständige Forschungsreplik** bedeutet: alle belegten Merkmale + dokumentierte Unsicherheiten + reversible Testvarianten. Sie bedeutet nicht, dass unbekannte Originalverdrahtung, Crystal-Material oder Pot-Topologie geraten und anschließend als Original ausgegeben werden.

## 104.2 Kleine quantitative Korrektur

Die an anderer Stelle verwendete Größenordnung `10 kJ` Lastenergie gegenüber ungefähr `1.4 J` Rotationsenergie entspricht einem Faktor von rund `7143`, also `log10(7143) ≈ 3.85` Größenordnungen. Die physikalische Schlussfolgerung bleibt unverändert (Rotationsspeicher ist viel zu klein), die Formulierung „mehr als vier Größenordnungen“ ist jedoch mathematisch etwas zu stark.

## 104.3 Kanonische neue Struktur

- Maschinen-IDs: `docs/research/machines.yaml`
- Provenienzschema: `docs/research/provenance-schema.yaml`
- Replikationslücken: `docs/REPLICATION_STATUS.md`
- CAD-Reproduzierbarkeit: `docs/research/cad-reproducibility.md`
- externer/nicht redistribuierter Korpus: `docs/research/external-corpus.md`
- Hardening-Plan: `docs/repository-hardening-plan-2026-08-16.md`

Diese Ergänzung löscht oder entwertet ältere Forschungsabschnitte nicht; sie definiert lediglich den aktuellen Repository-/Provenienzrahmen.

<!-- V4_BEST_EVIDENCE_M2_2026-08-16 -->
## V4 BEST-EVIDENCE M2 — current physical-build baseline (2026-08-16)

V4 is now the preferred starting point for any **new physical reconstruction of Marinov's first small machine (M2)**. V2/V3 remain preserved research/provenance families and must not be deleted.

Canonical files:

- `docs/research/v4-best-evidence-m2.md`
- `docs/research/v4-bom.md`
- `docs/research/v4-assembly.md`
- `docs/research/v4-electrical-boundary.md`
- `docs/research/v4-printing.md`
- `docs/research/v4-configurations.yaml`
- `cad/generate_v4_best_evidence_m2.py`
- `scripts/check_v4_assets.py`
- `scripts/build_v4_package.py`
- `.github/workflows/materialize-v4-best-evidence.yml`

Best-evidence V4 baseline:

1. one ~200-mm rotor;
2. nominal 24 sectors, with 20/25 count variants retained;
3. ~1-mm Cu wires;
4. **each sector individually floating / no neighbour ring**, based on direct Marinov `connected to nothing` wording;
5. R0 is the least-speculative nominal physical route; R4 is a separate research rotor and remains unproven specifically for M2;
6. no rubbing collectors;
7. two side pots with outer grid + dielectric/PMMA + inner Cu spiral;
8. **two external functional terminals per pot**, based on direct Marinov observation;
9. no Tesla/HF pot stage in the M2 baseline;
10. no built-in conventional drive motor in the historical baseline; any lab drive is removable instrumentation with separately measured input;
11. two visible horseshoe-magnet positions are retained, but magnet function remains unknown and matched nonmagnetic dummies are required for controls;
12. `meth4.asf`/`testabig.jpg` moving/still cross-check is integrated as geometry: two hub arcs, layered outer panels and a perforated lower central cage/prism;
13. `crystal` remains an unresolved Blackbox. V4 supports reversible low-energy surrogates but none is called original.

Nominal null configuration: `M2-V4-B0` in `docs/research/v4-configurations.yaml`.

Materialized CAD/output target:

- `hardware/experimental/v4-best-evidence-m2/stl/`
- `hardware/experimental/v4-best-evidence-m2/step/`
- `hardware/experimental/v4-best-evidence-m2/complete-model/Testatika_M2_V4_BEST_EVIDENCE.*`
- `hardware/experimental/v4-best-evidence-m2/complete-model/Testatika_M2_V4_R4_RESEARCH.*`
- `hardware/experimental/v4-best-evidence-m2/metadata/MODEL_INFO_V4.json`
- `release/experimental/testatika-m2-v4-best-evidence-build-package.zip`
- matching `.sha256`.

Still historically unresolved — do not invent:

- exact through-disc M2 routing;
- full node-to-node original wiring;
- exact pot polarity/capacitance/turn count;
- Crystal material/I-V/topology;
- exact stationary-electrode grouping;
- electrical role of hub arcs;
- magnet function;
- exact priming/start procedure;
- source of historical output claims / any net-energy anomaly.

Scientific boundary remains unchanged: no over-unity/free-energy claim is established. Energy conservation is the null hypothesis; any anomaly requires closed, uncertainty-aware energy accounting and independent replication.

<!-- M6-LARGE-V1-STATE -->
## M6 Large V1 best-evidence build

The repository now has a second canonical physical-build line for the large ~500-mm two-disc family. `M6-V1-B0` is anchored primarily to Albert Hauser's 1986/1988 M6a material and cross-checked against `meth2/meth3/meth5`. It is separate from M2 V4.

Canonical generator: `cad/generate_m6_large_v1.py`.
Materialized CAD: `hardware/experimental/m6-large-v1-best-evidence/`.
Primary STL: `complete-model/Testatika_M6_LARGE_V1_BEST_EVIDENCE.stl`.
Guarded lab STL: `complete-model/Testatika_M6_LARGE_V1_SAFE_LAB_GUARDED.stl`.
Build docs: `docs/research/m6-large-v1-*`.

Direct anchors include ~500 x 5 mm disc geometry, ~50 sheet lamellae (~0.2 x 20 x 160 mm source dimensions), ~8 front + ~6 rear non-contact perforated stators, three concentric grid tubes per large cylinder, acrylic separators, central magnet tube, two-layer bifilar ~18-gauge winding, wound horseshoe modules, top crystal/possible-rectifier geometry, and Hauser's motor/magnet-wheel large-machine configuration.

Historical hidden node wiring, exact crystal material/function, exact magnetic function, exact cylinder interconnections, exact startup state and any net-energy source remain unresolved. The V1 electrical default leaves unknown networks open at explicit test terminals. No over-unity claim is made.

