# ADDON.md — Testatika / Thesta-Distatica
## Externe Ergänzungen, Quellenregister, Konfliktmatrix und vollständiger Session-Handoff

**Version:** 1.0  
**Stand:** 2026-08-16  
**Ziel-Repository:** `inetconnector/testatika-small-research-replica`  
**Audit-Basis:** Branch `main`; beim Audit sichtbarer Git-tree `aa20ef584ceae74effb8e0135386708c15ce292c`  
**Rolle:** Ergänzung zu `STATE.md`, nicht Ersatz.

Diese Datei bündelt externe Informationen, die beim Repository-Audit noch nicht überall explizit auffindbar waren, korrigiert einige verbreitete Datierungs-/Quellenfehler und stellt einen vollständigen Handoff für neue Arbeitssitzungen bereit. Wo sich Inhalte mit `STATE.md` oder dem Augenzeugen-Dossier überschneiden, ist die Redundanz absichtlich: besonders kritische Invarianten sollen in einer neuen Session nicht verloren gehen.

---

# 0. ZUERST LESEN — Arbeitsanweisung für jede neue Session

Eine neue Session soll in dieser Reihenfolge lesen:

1. `AGENTS.md`
2. `README.md`
3. `ADDON.md` — diese Datei
4. `STATE.md`
5. `docs/Testatika_Augenzeugen_Dossier.pdf`
6. `docs/sources.md`
7. `docs/research/source-basis.md`
8. `docs/research/evidence_matrix.tsv`
9. `docs/research/rotor-wire-routing.md`
10. `docs/research/electrodes.md`
11. `docs/research/pots.md`
12. `docs/research/magnets.md`
13. `docs/research/photogrammetry.md`
14. `docs/scientific-status.md`
15. `docs/research/experiment-plan.md`

## 0.1 Nicht verhandelbare epistemische Regeln

- **Beobachtung ≠ Funktionsdeutung.**
- **Augenzeugenbericht ≠ kontrolliertes Messprotokoll.**
- **Betreiberbehauptung ≠ unabhängige Messung.**
- **Rekonstruktionszeichnung ≠ Originalschaltplan.**
- **Ähnliche historische Maschine ≠ identische Testatika.**
- **Resonanz / hohe Spannung / großer Peak ≠ Energieüberschuss.**
- **Fehlende Erklärung ≠ Beweis exotischer Physik.**
- Verschiedene Testatika-Modelle dürfen nicht stillschweigend zu einer einzigen Maschine verschmolzen werden.
- Negative Replikationen beweisen nicht, dass jede historische Beobachtung falsch war; sie sind aber starke Gegeninformation gegen konkrete Rekonstruktionshypothesen.
- Energieerhaltung bleibt die **Nullhypothese**, bis eine geschlossene, unabhängige und reproduzierbare Energiebilanz das Gegenteil zeigt.

## 0.2 Bevor CAD geändert wird

Jede Geometrieänderung braucht:

- Quelle / Foto / Zeuge;
- Maschinenvariante;
- beobachtet / source-stated / derived / hypothesized;
- Maßtyp: gemessen / fotoabgeleitet / Arbeitsmaß;
- Unsicherheit;
- Konflikte mit anderen Quellen;
- Konsequenz für STL, STEP, Photogrammetrie und Evidenzmatrix.

---

# 1. Wichtigste externe Deltas gegenüber dem aktuellen Repository

Beim Audit waren `STATE.md`, die Forschungsdokumentation und das Augenzeugen-Dossier bereits sehr umfangreich. Die folgenden Punkte verdienen dennoch eine ausdrückliche Addon-Aufnahme:

1. **1999-Datum korrigieren:** Vorführung vor 34 Ingenieuren am **5. Juni 1999**. **4. August 1999** ist das Datum der Übersetzung/Verbreitung des Holzherr-Berichts.
2. **Neuer Rotorhinweis:** Holzherr berichtet, dass bei mehreren Maschinen `sector wires` in die Scheibe „eingewebt“ seien und **dreimal die Seite wechseln**. Das ist ein wichtiger Kandidat für eine neue Routing-Familie **R4**.
3. **1984 Weber/Schneider-Maschine:** >1 m breit, ~45 cm tief, ~60 cm hoch, ~20 kg ohne Acrylhaube; Acryl, Leichtmetallgitter, isolierte Kupferleiter; Zentralteil ~10 cm; 300 V/10 A nur als Betreiber-/Zeugenclaim.
4. **Principle Experiment:** zusätzlicher glocken-/halbkugelförmiger Zentralfuß; Kondensatoren ungefähr 8 cm hoch und 3–4 cm Durchmesser; Baumann sagte, **Metallfolie statt Gitter funktioniere nicht**.
5. **Linden Experiment:** ausdrücklich Hearsay/Erinnerung; ~700-V-Claim nicht reproduziert.
6. **Mike-Watson-Bericht 2001:** Marinov→Watson→E-Mail; enthält einen Materialkonflikt **Eisendraht vs. Kupferdraht** und Ost-West-/Shield-Plate-Angaben.
7. **Nieper / P. H. Matthey 1984:** zusätzliche historische Zeugenclaims; 3–4 kW, 230 V DC, ~50 rpm, Gewächshausgeschichte; stark theoriebeladen, keine unabhängige Metrologie.
8. **Kelly/Bailey 1991:** echte IECEC-Konferenzpublikation, aber kein unabhängiger Funktionsnachweis.
9. **Novaretti 2015/2025:** wichtiges, noch nicht vollständig erschlossenes Sekundärwerk mit angeblich bisher unveröffentlichtem Gruppenmaterial.
10. **Schneider/Schneider 2023:** Web-Metadaten widersprechen sich bei Seitenzahl/ISBN; physisches Impressum als Autorität sichern.
11. **Methernitha 2010:** alternative-Energie-Forschungsgruppe bestand nach eigener Aussage nicht mehr; Thestatika könne nicht mehr gezeigt werden; Internetmaterial sei nicht autorisiert.
12. **Paul Baumann:** zeitgenössischer NET-Journal-Nachruf nennt **19. August 2011**, Alter 93; verbreitete 2008-Angaben sind sehr wahrscheinlich falsch.
13. **Historische konventionelle Vorläufer:** Poggendorff/Holtz/Wommelsdorf zeigen, dass Gegenrotation, eingebettete Sektoren, Kondensatormaschinen und elektrostatische Motoreffekte lange vor Testatika existierten.
14. **Moderne Fachliteratur:** PMMA-Ladung/Feuchte, Gittergeometrie/Corona und variable-C-/Electret-Generatoren liefern kontrollierte konventionelle Vergleichsmodelle.
15. **Patent-Recherche:** gezielte Websuche ergab kein eindeutig Testatika/Methernitha/Paul-Baumann zuordenbares Patent. Systematische Swissreg/Espacenet-Handsuche bleibt offen.

---

# 2. Kanonische Suchbegriffe und Aliase

Bei jeder externen Recherche mindestens folgende Begriffe mitverwenden.

## 2.1 Gerätenamen

- Testatika
- Testatica
- Thestatica
- Thestatika
- Thesta-Distatica
- Thesta Distatica
- Testa-Distatica
- Swiss M-L Converter
- Swiss ML Converter
- M/L Converter
- ML Converter
- Methernitha converter
- Methernitha electrostatic machine

## 2.2 Personen

- Paul Baumann — auch „Vatti/Vati“
- Luzius / Luzi Cathomen
- Francis Bosshard / Bosshardt
- Viktor Bosshard
- Inge Schönthal — spätere Inge Schneider
- Adolf Schneider
- Hans Weber
- Stefan Marinov
- Albert Hauser
- Hans Holzherr
- Donald A. / Don Kelly
- Patrick G. Bailey
- Paul E. Potter
- P. H. Matthey
- Hans Nieper
- Elena Novaretti / Elena Design
- Sven Bönisch / Bosnich
- Wolfgang Wiedergut
- Harald Chmela
- Stefan Hartmann

---

# 3. Erweiterte Evidenzklassen für externe Quellen

Die vorhandenen Repo-Regeln bleiben maßgeblich. Für externe Quellen zusätzlich:

| Code | Bedeutung |
|---|---|
| **P0** | Originalobjekt / Originalfoto mit gesicherter Provenienz |
| **P1** | zeitnaher direkter Augenzeugenbericht |
| **P2** | späterer direkter Augenzeugenbericht |
| **H1** | direkte Weitergabe eines Augenzeugen an Autor |
| **H2** | Hearsay zweiter/dritter Ordnung |
| **O1** | Betreiber-/Methernitha-eigene Funktionsbehauptung |
| **R1** | kontrollierte Replikation / Messversuch |
| **S1** | etablierte peer-reviewte Fachliteratur |
| **S2** | historische Fachliteratur / Patent |
| **I1** | spätere Interpretation / Backengineering |
| **C** | nicht verifizierter Leistungs-/Energieclaim |

Ein Detail kann gleichzeitig z. B. `P1 + C` sein: Ein Zeuge kann glaubwürdig berichten, dass eine Lampe leuchtete, ohne damit den Nettoenergiefluss bewiesen zu haben.

---

# 4. Kanonische Maschinen-Taxonomie

Historische Namen sind uneinheitlich. Für Projektarbeit interne IDs verwenden.

## M0 — Principle Experiment / Schwenkarm

Berichtet:

- horizontal schwenkbarer Plexiglasarm;
- kleine Platten an beiden Enden;
- perforiertes Aluminium;
- Messingdrahtgitter;
- je fünf zusätzliche Plexiglasplatten unter den Endplatten;
- Gitter zwischen den Platten;
- unterstes Gitter → zwei parallel geschaltete Kondensatoren;
- Arm ungefähr zehnmal hin- und herbewegt;
- berichtete 60 V DC;
- hörbarer Knall beim Kurzschluss;
- laut Baumann funktioniere Metallfolie statt Gitter nicht;
- zusätzlicher glocken-/halbkugelförmiger Zentralfuß.

## M0b — Linden Experiment

- U-/Hufeisenmagnet;
- Drahtschleife;
- zwei Metallplatten mit Papier;
- im Magnetspalt;
- berichtete ~700 V;
- ausdrücklich zweit-handige Erinnerungsquelle;
- Replikationen ohne Resultat.

## M1 — frühe „Ruck-Zuck“-/Panning-Arm-Maschine

- fragmentarisch überliefert;
- nicht automatisch mit M0 gleichsetzen.

## M2 — kleine Ein-Scheiben-Marinov-Maschine

- aktuelle Repo-Hauptreferenz;
- ~200-mm-Scheibe;
- frühe Drahtsektoren;
- publiziert bei Marinov als ungefähr 1-mm-Kupferdraht;
- 20–30, später etwa 20–25 berichtet;
- keine reibenden Bürsten;
- bei erster kleiner Maschine Hufeisenmagnete sichtbar;
- zweite kleine Variante ohne sichtbare Magnete;
- seitliche Pots als Gitter/Dielektrikum/dicke Kupferspirale;
- Crystal-Funktion unbekannt;
- vollständige Verschaltung unbekannt.

## M3 — zweite kleine / Begleitmaschine

- Details nicht automatisch von M2 übernehmen;
- keine sichtbaren Hufeisenmagnete laut Marinov.

## M4 — 12-cm-Modell im 1999-Bericht

- ca. 12-cm-Scheiben;
- kurz ~130 V am DMM;
- kleine Lampen + Widerstand, Werte unbekannt;
- Körper-Kurzschluss führte laut Bericht zu Schlag;
- DMM zeigte nur kurz 130 V und fiel danach aus.

## M5 — Weber/Schneider-Maschine vom 13.03.1984

- >1 m breit;
- ~45 cm tief;
- ~60 cm hoch;
- ~20 kg ohne Acrylhaube;
- Acryl, Leichtmetallgitter, isolierte Kupferleiter;
- Kristalldioden-Gleichrichter behauptet;
- vergoldete Pole;
- zwei gegenläufige Scheiben;
- zentrale ~10-cm-Scheibe mit Regenbogenschimmer;
- berührungslose Stromabnahme;
- Start per Fingerschub;
- behauptete 300 V DC / 10 A;
- Lampen-/Heizstabdemo;
- Weber durfte Gerät laut Bericht anheben.

## M6 — 50-cm-Maschine, Vorführung 05.06.1999

- 34 Ingenieure laut Seminarprogramm;
- 50-cm-Scheiben;
- bei Eintritt bereits laufend;
- Besuch ~1,5 h;
- ~15 rpm;
- magnetische Drehzahlregelung beschrieben;
- 1000-W-Lampe ~10 s;
- sehr schneller Heizeffekt;
- ~1-cm-Lichtbogen;
- unter Plexiglashaube;
- Basis durfte nicht angefasst/angehoben werden;
- keine geschlossene Energiebilanz.

## M7 — ~1-m-Modell im Bau

- Holzherr erwähnt `sector wires`;
- Drähte in Scheibe eingewebt;
- **dreimaliger Seitenwechsel**;
- nicht automatisch M2-Routing.

## M8 — sehr große unvollständige Modelle

- Namensgebung in Sekundärquellen uneinheitlich;
- keine Details ohne Quellen-ID übertragen.

## M9 — Tandem-/Mehrmaschinen

- spätere Fotografien/Zeichnungen;
- jede Variante separat behandeln.

---

# 5. Chronologie — korrigierter Kern

## 13. März 1984 — Hans Weber + Inge Schönthal/Schneider

Spätere Wiedergaben nennen diesen Tag explizit als erste Begegnung.

Wichtig:

- direkte Maschinenbesichtigung;
- Lastdemonstrationen;
- Geometrie beschrieben;
- keine geschlossene Input-/Output-Messung.

## 17. März 1984 — separater Swiss-ML-Besuchsbericht

Nicht mit Weber/Schneider 13.03.1984 vermischen.

## 20. Oktober 1984 — P. H. Matthey

Nieper berichtet von Matthey-Besuch mit weiteren Schweizer Ingenieuren.

## 28. Oktober 1984 — Hans Nieper

Nieper berichtet eigene Besichtigung; physikalische Interpretation stark tachyon-/gravitationsfeldtheoretisch.

## 1988/1989 — Marinov

- Besuche 1988 und Februar/März 1989;
- *The Thorny Way of Truth, Part V* 1989;
- Marinov sagt ausdrücklich, dass er das vollständige Geheimnis nicht kennt.

## 1989 — SAFE / Einsiedeln

Bibliographisch belegt:

- `Methernitha (1989), Informationsfilm Thesta-Distatica: Sound Track Transcription`
- Proceedings `Internationaler Kongress für Freie Energie`, Einsiedeln 1989
- ISBN **3-9520025-1-8**

Falls der vollständige Scan fehlt: hohe Akquisitionspriorität.

## 5. Juni 1999 — Vorführung vor 34 Ingenieuren

**Korrektur:** Seminarprogramm von 2004 nennt ausdrücklich **5. Juni 1999**.

## 4. August 1999 — Übersetzung Holzherr/Hartmann

Der online verbreitete Bericht trägt dieses Datum als Übersetzungsdatum.

> Künftige Chronologie: **Demonstration 05.06.1999; Übersetzung 04.08.1999.**

## 13. März 2004 — Seminar „Das Geheimnis der Testatika“

Programmpunkte:

- Hans Weber: erster Besuch 13.03.1984;
- Vorführung 34 Ingenieure 05.06.1999;
- Polymerketten/Luftionisation als theoretisches Modell;
- Adolf Schneider: weitere Theorien;
- Sven Bönisch: Replikation;
- weitere Elektrostatik-/Elektret-Themen.

Theorien nicht als verifizierte Testatika-Erklärung behandeln.

## 2010 — Methernitha-Status

Methernitha erklärte sinngemäß:

- Forschungsgruppe für alternative Energie existiere nicht mehr;
- Thestatika könne nicht mehr gezeigt werden;
- Internetmaterial sei nicht mit ihrem Wissen entstanden;
- Testatika könne als Inspiration für erneuerbare Energieforschung dienen.

## 19. August 2011 — Tod Paul Baumanns

NET-Journal-Retrospektive nennt:

- Tod am **19.08.2011**;
- Alter 93.

Verbreitete 2008-Angaben markieren als wahrscheinlich falsch.

---

# 6. Weber/Schneider 1984 — technische Extraktion

**Evidenz:** `P1 + C`

## 6.1 Geometrie / Material

Berichtet:

- >1 m Breite;
- ~45 cm Tiefe;
- ~60 cm Höhe;
- ~20 kg ohne Acrylhaube;
- Acrylglas;
- Leichtmetallgitter;
- isolierte Kupferleiter;
- publizierte Beschreibung spricht von Kristalldioden-Gleichrichter;
- vergoldete Ausgangspole.

## 6.2 Start

- Baumann stand seitlich;
- Fingerschub brachte zwei Scheiben in Gegenrotation;
- danach laut Bericht ruhige, geräuscharme Rotation.

## 6.3 Zentrale ~10-cm-Scheibe

- schimmerte in Regenbogenfarben.

Keine Funktion daraus ableiten. Banale Möglichkeiten: Oberflächenbeugung, Spannungsbirefringenz, Beschichtung, Reflexion.

## 6.4 Ausgang

Berichtet:

- „Leydener Flaschen“ nach wenigen Sekunden bereit;
- 300 V DC / 10 A laut Baumann;
- 380-V-Lampe hell;
- 380-V-Heizstab schnell heiß.

Nicht vorhanden:

- dokumentierte simultane kalibrierte U/I-Messung;
- Dauerlauf an definierter Last;
- Eingangsleistung;
- Anfangsenergie aller Speicher;
- unabhängige Replikation.

## 6.5 Unterseitenkontrolle

Weber durfte das Gerät laut Bericht anheben.

Das ist wertvoll gegen die Hypothese eines **offensichtlichen** Kabels/Batteriekastens, schließt aber nicht aus:

- interne Speicher;
- vorher geladene Kondensatoren;
- kapazitive/induktive externe Kopplung;
- nicht inspizierte Volumina;
- Messfehler.

---

# 7. Holzherr 1999 — wichtige technische Ergänzungen

**Quelle:** Hans Holzherr → Stefan Hartmann; Übersetzung 04.08.1999.  
**Evidenz:** `P1 + C`

## 7.1 50-cm-Maschine

- lief bereits beim Betreten;
- ca. 1,5 h Besuch;
- 1000-W-Lampe ~10 s, Helligkeit laut Bericht stabil;
- U-Heizelement sehr schnelle Erwärmung;
- ~1-cm-Lichtbogen beim Abziehen eines Leiters;
- ungefähr 15 rpm;
- magnetische Drehzahlregelung beschrieben;
- kein Lastabfall bemerkt, aber Aufmerksamkeit des Zeugen lag auf Last;
- Plexiglashaube;
- Basis durfte nicht angefasst/angehoben werden.

## 7.2 Kleine Geräte

- ungefähr 12-cm-Scheiben;
- Geräte durften angefasst/angehoben werden;
- „Originalmodell“ kurz ~130 V am DMM;
- Last aus zwei kleinen Lampen + Widerstand, Werte unbekannt;
- Körper-Kurzschluss führte laut Bericht zu Schlag;
- DMM fiel nach kurzer Anzeige aus; später analoge Messgeräte.

### Metrologie-Folge

HV-Impulse/EMI können DMMs stören oder beschädigen. Künftige Tests benötigen HV-/EMI-taugliche Instrumente.

## 7.3 Motor-Widerspruch

Holzherr nennt ein „earliest model“ als einzige motorgetriebene Maschine; Motor werde von kontinuierlich nachgeladenem Kondensator gespeist.

Das kollidiert mit Marinovs kleiner Maschine ohne Motor.

Mögliche Auflösung:

- andere Generation;
- andere Maschine;
- Umbau;
- unterschiedliche Bedeutung von „earliest/original“.

Nicht vereinheitlichen.

## 7.4 Kleine Plexiglasblöcke

- teils perforierte Metalllagen auf zwei gegenüberliegenden Seiten;
- teils nur auf einer Seite, über Kante gebogen;
- Funktion unbekannt.

## 7.5 Große Kondensatoren

Baumann soll gesagt haben:

- **20 Lagen perforiertes Blech**.

Nur für größere Variante übernehmen.

## 7.6 Crystal-Geometrie

Holzherr erinnert:

- grobe Spule um geraden Zentralleiter;
- beim „Originalmodell“ vier Leitungen;
- bei 50-cm-Maschine nur zwei Zuleitungen sicher erkennbar;
- Kristall selbst nicht klar gesehen;
- mögliche umgebende Röhre unsicher.

Folge: Crystal nicht als universell identische Baugruppe modellieren.

## 7.7 Unsichtbare Leiter in Acryl

Holzherr weist darauf hin, dass sehr dünne Leiterlagen zwischen Plexiglasplatten optisch schwer sichtbar sein können.

Fotogrammetrie-Regel:

> „Auf Foto nicht sichtbar“ ≠ „nicht vorhanden“, wenn laminiertes Acryl vorliegt.

---

# 8. NEUER Schlüsselhinweis: dreifacher Seitenwechsel der Rotorleiter

Holzherr berichtet, `sector wires` seien bei mehreren Maschinen in die Scheibe „woven“ und würden **dreimal die Scheibenseite wechseln**.

Dies passt auffällig zu Marinovs separatem Hinweis, die Art, **wie Drähte durch die Scheibe gehen**, sei sehr wichtig.

## 8.1 Neue Routing-Familie R4

Zusätzlich zu R0–R3:

### R4 — `three-side-change weave`

Definition als Forschungsvariante:

- Leiter startet Seite A;
- Wechsel A→B;
- B→A;
- A→B;
- insgesamt drei Seitenwechsel;
- genaue Stichradien unbekannt;
- Startseite A/B parametrierbar.

**Wichtig:** Holzherr bezieht den Hinweis auf mehrere Maschinen, darunter ein 1-m-Modell. Noch nicht bewiesen, dass M2 exakt R4 verwendete.

## 8.2 CAD-Vorschlag

Neue Rotoren:

- `rotor_20wire_R4_3cross`
- `rotor_24wire_R4_3cross`
- `rotor_25wire_R4_3cross`

Parameter:

- Stitch-Radius 1–4;
- Startseite;
- alternierende Sektoren;
- Drahtdurchmesser;
- Material unabhängig.

## 8.3 Experimentvergleich R0–R4

Identisch messen:

- \(C(\theta)\);
- Ladung pro Winkel;
- Phasenlage Rotorposition/Elektrodenstrom;
- Torque mit externer sicherer Biasquelle;
- Oberflächenpotential;
- Corona-/Ionenstrom;
- Shield-Plate-Effekt;
- Feuchteabhängigkeit.

---

# 9. Principle Experiment — vollständige Ergänzung

## 9.1 Aufbau

Berichtet:

- horizontal schwenkbarer Plexiglasarm;
- kleine rechteckige Plexiglasplatten an beiden Enden;
- Unterseite des Arms: perforiertes Aluminium mit quadratischen Löchern;
- Unterseiten der Endplatten: Messingdrahtgitter;
- unter jeder Endplatte fünf zusätzliche Plexiglasplatten;
- Drahtgitter zwischen jedem Plattenpaar;
- unterste Gitterlage → zwei parallel geschaltete Kondensatoren;
- Arm ~10× hin und her;
- 60 V DC am Digitalmeter;
- hörbarer Knall beim Kurzschluss;
- Baumann: **Metallfolie statt Gitter funktioniere nicht**.

## 9.2 Zentralfuß

Späterer Bericht nennt ein ausgelassenes Detail:

- Basis des Zentralpfostens wie abgeflachte Halbkugel / halbe elektrische Glocke.

Mögliche klassische Funktionen:

- zusätzliche Umgebungskapazität;
- Faraday-Cup-artige Ladungsübertragung;
- Körper-/Handkopplung;
- triboelektrische Effekte.

Nicht festlegen, sondern testen.

## 9.3 Kondensatoren

Berichtet:

- ~8 cm hoch;
- 3–4 cm Durchmesser;
- teils gekauft, teils selbstgebaut;
- Baumann habe gesagt, das sei funktionell egal.

## 9.4 Warum „Gitter vs. Folie“ wichtig ist

Klassische Ursachen können sein:

- lokale Feldverstärkung an Kanten;
- Coronaonset;
- Ionentransport durch Öffnungen;
- Randlänge;
- effektive Kapazität;
- Oberflächenladung des Dielektrikums;
- Leckpfade;
- Kopplung an Hand/Körper.

Das ist eines der besten verblindbaren Experimente des gesamten Projekts.

---

# 10. Linden Experiment — Hearsay, nicht Primärbeweis

## 10.1 Quellenkette

- zwei Besucher sahen Versuch;
- erzählten einer anderen Person;
- diese schrieb einen Brief;
- Quelle bezeichnet die Information selbst als second-hand memory.

## 10.2 Berichteter Aufbau

- U-/Hufeisenmagnet;
- isolierte Leitung um Mittelteil;
- lange Enden, vielleicht ~3 ft;
- Enden abisoliert und galvanisch zu Schleife verbunden;
- zwei kleine Metallplatten;
- Papier dazwischen;
- Paket im Magnetspalt;
- nach Positionierung berichtete ~700 V;
- Spannung schien langsam abzufallen.

## 10.3 Kritik

- Messgerät/Modus nicht sicher;
- Hautwiderstands-/Ohmmeterfehler wurde vom Briefschreiber selbst erwogen;
- Replikationen ohne Resultat.

Status: `H2`, interessant als Hypothesenquelle, nicht als Beleg.

---

# 11. Mike Watson 2001 — Konfliktquelle, H2

Ein 2001 verbreiteter Text berichtet, Mike Watson habe Marinov persönlich zu Testatika befragt.

**Quellenkette:** Marinov → Watson → E-Mail → Webarchiv.

## 11.1 Berichtete Punkte

- kleine Pots ohne Magnete;
- Zentral-Elektrode: wenige Windungen dicker Draht als Helix;
- konzentrische Gitterzylinder durch klare Kunststoffzylinder isoliert;
- Einzelscheibe;
- **Eisendraht** als Rotorsektoren;
- radial von Seite zu Seite durch Scheibe;
- Achse angeblich Ost-West nötig;
- gestoppter Rotor habe Restdrehmoment gezeigt;
- Metallplatte hinter Maschine habe Rotation/Restdrehmoment beendet;
- keine Reibkontakte;
- wenige Handschwünge zum Start;
- mechanische Leistung <100 mW geschätzt;
- elektrische ~100 W aus Erwärmung eines Widerstands geschätzt;
- große Maschine: leicht magnetisierte Fe-Ni-Sektoren;
- Geheimnis unter Eid/NDA angeboten, Marinov habe abgelehnt.

## 11.2 Materialkonflikt

| Quelle | kleine Rotorleiter |
|---|---|
| Marinovs eigene Publikation / Repo | ca. 1-mm-**Kupferdraht** |
| Watson-Erinnerung an Marinov | **Eisendraht** |
| Holzherr | `sector wires`, Material nicht spezifiziert |
| größere Varianten | Stahl/Chromstahl/Fe-Ni-Berichte |

Arbeitsregel:

- Marinovs Eigenpublikation höher gewichten;
- Materialexperiment trotzdem offen halten: Cu / Fe / Edelstahl / Fe-Ni.

## 11.3 Ost-West-Effekt

Nur `H2`.

Sauber testbar:

- Drehtisch;
- randomisierte 0–360°-Orientierung;
- 3-Achs-Magnetometer;
- Netz-/Gebäudefelder loggen;
- gleiche Startenergie;
- Bediener möglichst verblindet.

---

# 12. Nieper / P. H. Matthey — historische Claims

Nieper berichtet sinngemäß:

- mehrere Besichtigungen;
- P. H. Matthey am 20.10.1984;
- Nieper selbst 28.10.1984;
- Maschine(n) seit 1982;
- Gewächshausbeheizung;
- 3–4 kW bei 230 V DC;
- ~50 rpm;
- keine sichtbare Primärantriebsquelle.

## 12.1 Quellenkritik

Trennen:

- **Besichtigungsclaim**
- **Leistungsclaim**
- **Gewächshaus-/Dauerlastclaim**
- **Niepers Tachyon-/Gravity-Stressing-Theorie**

Letztere ist durch den Besuch nicht bewiesen.

## 12.2 Gewächshausclaim

Falls je belastbar prüfbar, wären nötig:

- Heizlast;
- Fläche/Isolation;
- Außentemperatur;
- Laufzeit;
- Verkabelung;
- Energieabrechnungen;
- unabhängige Zeugen.

Bis dahin `C/H`.

---

# 13. Kelly/Bailey 1991 — echte Bibliographie, kein Energiebeweis

Bibliographisch belegt:

- Donald A. Kelly
- Patrick G. Bailey
- **The Methernitha Free Energy Machine — The Swiss M-L Converter**
- 26th Intersociety Energy Conversion Engineering Conference
- Vol. 4
- S. 467–472
- 1991

Das beweist:

- reale Proceedings-Publikation.

Es beweist nicht:

- unabhängige Laborprüfung;
- Originalschaltplan;
- Overunity.

Kelly-Schaltungen bleiben `I1`.

---

# 14. Bailey/Grotz 1993 — kritischer Kontext

- Patrick G. Bailey
- Toby Grotz
- `A Critical Review of the Available Information Regarding Claims of Zero-Point Energy, Free-Energy, and Over-Unity Experiments and Devices`
- 28th IECEC, Atlanta, August 1993

Nutzen:

- Forschungs-/Diskursgeschichte;
- keine Testatika-Validierung.

---

# 15. Methernitha-eigene technische Funktionsbeschreibung

Archivierte Wiedergaben der früheren Methernitha-Information beschreiben:

- zwei gegenläufige Scheiben;
- elektrostatische Ladung;
- Gitterelektroden;
- berührungslose `antenna keys`;
- Handschub;
- Rotation durch elektrostatische Anziehung/Abstoßung;
- `rectifying diode` stabilisiere den Zyklus;
- langsame konstante Drehzahl;
- `grid condensers` als Speicher/Puffer;
- weitere Vorrichtungen zur Spannungs-/Leistungsumformung;
- DC-Ausgang;
- behauptete 3–4 kW bei ca. 270–320 V;
- trockene Luft günstiger, hohe Feuchte ungünstig.

## 15.1 Status

`O1 + C`

Sehr wichtig für das Betreiber-Narrativ, nicht für unabhängige Energievalidierung.

## 15.2 Crystal-Folge

Unterstützt die Arbeitshypothese:

- nichtlinearer Ladungsweg;
- Kommutation;
- Clamping;
- Zyklusregelung;

mehr als die simple Annahme „Crystal = nur Ausgangsgleichrichter“.

---

# 16. Methernitha 2010 — Quellenwarnung

Methernitha erklärte:

- alternative-Energie-Forschungsgruppe nicht mehr aktiv;
- Thestatika nicht mehr vorführbar;
- Internetmaterial nicht mit ihrem Wissen entstanden.

Konsequenz:

> Keine heute kursierende Website allein als „offizielle Testatika-Dokumentation“ behandeln.

---

# 17. Elena Novaretti — wichtigste noch offene Sekundärquelle

## 17.1 Buch

- Elena Novaretti
- *Tutta la verità sul caso Testatika*
- Andromeda
- Erstauflage April 2015
- 194 Seiten
- ISBN **9788868320669**
- Händler/Verlag nennt 2025 als aktuelle Edition.

## 17.2 Warum hohe Priorität

Novaretti schreibt 2019 in der Testatika-Groups.io-Gruppe sinngemäß:

- etwa fünf Jahre Untersuchung;
- sehr viel Internetmaterial sei fake, falsch, Desinformation, Fantasie oder Spekulation;
- sie habe die frühere YahooGroups-Sammlung bewahren wollen;
- ihr Buch enthalte alle zusammengetragenen Informationen und mehrere zuvor unveröffentlichte Details;
- sie selbst habe keine endgültige Lösung gefunden.

### Arbeitsauftrag

Buch legal beschaffen und seitenweise extrahieren:

- direkte Quellen;
- Briefzitate;
- Gruppenmaterial;
- neue Fotos;
- neue Maße;
- neue Zeugen;
- widersprechende Details.

Ihre eigenen Vakuum-/Ionen-/ZPE-Deutungen nicht als Fakten übernehmen.

---

# 18. Schneider/Schneider 2023 — Bibliographie physisch verifizieren

Titel:

- Adolf Schneider
- Inge Schneider
- *Testatika und weitere Freie-Energie-Geräte*
- Jupiter Verlag
- 1. Auflage 2023

## 18.1 Web-Konflikt

Einige Quellen nennen:

- ISBN `9783906571454`
- 274 Seiten

Kopp nennt:

- gleiche ISBN
- 266 Seiten

Andere Shops nennen:

- 274 Seiten
- abweichende ISBN `978-3-906571-46-7`

### Aktion

Da das physische Buch bereits im Projekt benutzt wird:

> Titelblatt + Impressum + letzte nummerierte Seite fotografieren und im Repo als bibliographische Autorität dokumentieren.

## 18.2 Inhaltliche Bewertung

Das Buch ist eine moderne Kompilation mit:

- Augenzeugenberichten;
- technischen Interpretationen;
- Wiedergut-/Chmela-Theorien;
- weiteren „Free Energy“-Claims.

Jede Quelle im Buch separat auf Primärursprung zurückführen.

---

# 19. Historische konventionelle Vorläufer

Testatika darf nicht ohne klassische Elektrostatische Maschinen bewertet werden.

## 19.1 Poggendorff / Holtz

Poggendorff publizierte 1870 u. a. zum Holtz’schen Rotationsphänomen.

Lehre:

- elektrostatische Rotation;
- Ladungsfeedback;
- Selbst-/Fremderregung

sind historische bekannte Phänomene.

## 19.2 Wimshurst

- Gegenrotation;
- Sektoren;
- Influenz;
- Neutralisatoren;
- Leydener Flaschen.

Erklärt viel sichtbare Testatika-Geometrie, aber nicht automatisch unbekannte Nachstufen.

## 19.3 Heinrich Wommelsdorf

Besonders relevant:

- 1902 Kondensatormaschine;
- 1904 Doppeldrehung;
- 1905 Scheiben mit **eingebetteten Sektoren**;
- mehrstufige Induktor-/Kondensatorgeometrie;
- spätere vollständig isolierte Varianten.

Relevante Patente:

- `DE145440`
- `DE178052` — Doppeldrehung
- `DE176415` — eingebettete Sektoren
- `US882508`
- `US883846` — multiple influence/condenser machine, gegenläufige Systeme
- weitere im de-Queiroz-Archiv

## 19.4 Forschungsfolge

Gegenrotation + eingebettete Leiter + isolierte Induktoren können klassisch:

- hohe Spannung;
- höhere Ausgangsströme als einfache Wimshurst;
- starke kapazitive Kopplung

erzeugen.

Jede „Anomalie“ muss gegen diese Vorläufer quantifiziert werden.

---

# 20. Moderne kontrollierte Wissenschaft für relevante Teilphänomene

## 20.1 PMMA-Ladung und Feuchtigkeit

`Charge storage and transport in polymethylmethacrylate (PMMA) film`, Journal of Electrostatics 44 (1998), DOI:

`10.1016/S0304-3886(98)00023-0`

Ergebnis:

- relative Feuchte beeinflusst PMMA-Ladungsspeicherung signifikant.

Folge:

Methernithas „trocken besser“ ist **nicht exotisch**; Feuchte verändert Oberflächenleitfähigkeit, Leckstrom und Ladungsfallen.

## 20.2 Gittergeometrie und Corona

`Effects of the grid geometry on the performances of a triode-type corona electrode system`, Journal of Electrostatics 101 (2019), DOI:

`10.1016/j.elstat.2019.103367`

Ergebnis:

- Gittergeometrie beeinflusst I-V-Kennlinie;
- Corona-Onset;
- Stromdichteverteilung.

Folge:

„Gitter vs. Folie“ ist ein legitimes, hochinformatives Experiment.

## 20.3 Draht-Platte-Corona

`Corona discharges in sub-millimeter electrode gaps`, Journal of Electrostatics 69(1), 2011, DOI:

`10.1016/j.elstat.2010.10.006`

Ergebnis:

- kleinere Lücke und dünnerer Draht senken Onset-Spannung und können Strom erhöhen.

Folge:

Drahtdurchmesser, Abstand und Kantenradius sind kritische Replikationsparameter.

## 20.4 Electret-/Variable-C-Generatoren

Moderne etablierte Technik zeigt:

- variable Kapazität + Bias/Electret → elektrischer Strom;
- mechanische Arbeit bleibt Energiequelle;
- Charge-Pump-/Priming-Schaltungen sind möglich;
- hohe Spannung und kleine Ströme sind typisch.

Quellen:

- Suzuki 2011, DOI `10.1002/tee.20631`
- Sabzpoushan & Woias 2024, DOI `10.1016/j.nanoen.2024.110167`
- Peter et al. 2015, DOI `10.1016/j.eml.2015.07.008`

---

# 21. Minimales konventionelles Gleichungsmodell

## 21.1 Variable Kapazität

\[
Q(t)=C(t)V(t)
\]

\[
i(t)=\frac{dQ}{dt}=V\frac{dC}{dt}+C\frac{dV}{dt}
\]

Ein bewegter Rotor kann bei festem Bias Stromimpulse erzeugen.

## 21.2 Kondensatorenergie

\[
E_C=\frac{1}{2}CV^2
\]

## 21.3 Mechanische Leistung

\[
P_{mech}=\tau\omega
\]

Bereits ermittelte Größenordnung:

- 3 kW bei 60 rpm → ~477 N·m
- 3 kW bei 15 rpm → ~1910 N·m

Damit sind die sichtbaren leichten Scheiben als **alleiniger mechanischer kW-Energiepfad** extrem unplausibel.

## 21.4 Rotationsenergie

Zwei 500-mm-PMMA-Scheiben speichern bei ~60 rpm nur Energie in der Größenordnung weniger Joule.

1 kW × 10 s:

\[
10\,000~J \approx 2.78~Wh
\]

Folge:

- Schwungenergie erklärt die Lastdemo nicht;
- kurze Demo ist aber mit relativ kleinem elektrischen Speicher energetisch vereinbar.

---

# 22. Konfliktmatrix

| Thema | Quelle A | Quelle B | Status |
|---|---|---|---|
| kleine Rotorleiter | Marinov: Cu ~1 mm | Watson-Hearsay: Fe | Marinov höher; Materialtest |
| Drahtführung | Marinov: wichtig, durch Scheibe | Holzherr: 3 Seitenwechsel | R4 testen; Maschinenidentität offen |
| Magnete kleine Geräte | erste kleine: sichtbar | zweite kleine: nicht sichtbar | nicht universal |
| Motor | Marinov-Kleinmaschine ohne Motor | Holzherr „earliest“ motorgetrieben | Generations-/Modellkonflikt |
| Drehzahl | teils 50–60 rpm | Holzherr ~15 rpm | modellabhängig |
| 50/60 Hz | spätere Europe/US-Notiz | Marinov widerspricht, DC | stark herabgestuft |
| Tesla/HF | Potter/Kelly | Marinov widerspricht als Kern | nicht Baseline |
| Crystal | `rectifier` in Zeichnungen | Baumann sagte laut Marinov `crystal` | Funktion offen |
| Pots | Hauser groß: Mehrgitter/Magnet/Wicklung | Marinov klein: Gitter/Kunststoff/Cu-Helix | Modelltrennung |
| 1999 Datum | 4.8. oft als Demo | 5.6. Seminarprogramm; 4.8. Übersetzung | korrigiert |
| Radium | späte Hearsay-Claims | Baumann zu Holzherr: nein | verwerfen |
| Output | 130 / 270–320 / 300 / 580–770 V | unterschiedliche Modelle | nie universalisieren |

---

# 23. Häufige Internetfehler

## 23.1 „Ingenieur-Demo am 4. August 1999“

Falsch/irreführend.

- Demo: **5. Juni 1999**
- Übersetzung: **4. August 1999**

## 23.2 „Paul Baumann starb 2008“

Sehr wahrscheinlich falsch.

- zeitgenössische Retrospektive: **19. August 2011**, Alter 93.

## 23.3 „Vollständiger Originalschaltplan ist bekannt“

Nein.

Verbreitete `full circuit`-Grafiken sind Rekonstruktionen.

## 23.4 „Tesla-Spulen sind sicher der Kern“

Nicht haltbar, besonders für kleine Marinov-Maschine.

## 23.5 „50 Segmente erzeugen direkt 50-Hz-Netzausgang“

Nicht als universelles Prinzip haltbar.

## 23.6 „Magnete liefern die Energie“

Nicht belegt; Magnete nicht universal.

## 23.7 „Radiumchlorid ist das Geheimnis“

Baumann verneinte dies laut Holzherr.

## 23.8 „Konferenzpaper = wissenschaftlicher Nachweis“

Nein. Publikationsrealität ≠ experimentelle Validierung.

## 23.9 „10 s 1-kW-Lampe = 1 kW Dauerleistung“

Nein. Das sind nur ~2.78 Wh.

## 23.10 „Keine sichtbare Batterie = keine konventionelle Energiequelle“

Zu stark. Es ist eine nützliche Beobachtung, aber keine vollständige Ausschlussmessung.

---

# 24. Patentlage

Gezielte Websuche nach:

- Testatika / Thestatika
- Methernitha
- Paul Baumann
- elektrostatischer Generator
- Google Patents / Swissreg-Begriffen

ergab kein Patent, das eindeutig als Original-Testatika-Patent identifiziert werden konnte.

## 24.1 Das bedeutet nicht

- dass garantiert kein Patent existiert;
- dass nichts unter anderem Namen angemeldet wurde;
- dass andere Methernitha-Personen ausgeschlossen sind.

## 24.2 Offene Recherche

Systematisch in:

- Swissreg / IGE
- Espacenet
- WIPO Patentscope
- Google Patents

mit:

- Baumann
- Methernitha
- Cathomen
- Bosshard
- Linden/Oberdiessbach
- Influenzmaschine
- Kondensatormaschine
- H02N und ältere Klassen

suchen und Negativbefunde mit Query/Datum protokollieren.

---

# 25. CAD-/Hardware-Prioritäten für V3

## 25.1 R4-Rotor

Höchste Priorität.

Neue Varianten:

- 20 wire R4
- 24 wire R4
- 25 wire R4

Parameter:

- 3 Seitenwechsel
- 4 Stitch-Radien
- Startseite A/B
- alternierende Sektoren
- Drahtdurchmesser

## 25.2 Material-Kit

Identische Rotor-Geometrie für:

- Cu
- weicher Stahl
- Edelstahl
- Fe-Ni

Messen:

- Widerstand
- Permeabilität
- Remanenz
- Oberfläche

## 25.3 Elektroden-Kit

A/B-Träger für:

- Vollfolie
- quadratisches Lochblech
- rund perforiert
- Messinggitter
- unterschiedliche Maschenweite

Außenkontur, Abstand und Fläche möglichst konstant halten.

## 25.4 Umwelt-/Shield-Jig

Erweitern um:

- definierte rückwärtige Metallplatte
- Distanzskala
- floating / ground / R/C-grounded
- 360° Orientierungsindex
- Feuchte-/Temperaturhalter
- Magnetometerposition

## 25.5 Unsichtbare Leiter

CAD/Fotomodell sollte optionale laminierte Leiterlagen vorsehen, weil dünne Leiter zwischen Acrylplatten optisch verschwinden können.

---

# 26. MASTER-EXPERIMENTPLAN

Keine kW-HV-Maschine zuerst. Zuerst die Teilmechanismen trennen.

## E0 — Mechanische Nullmessung

- Lagerreibung
- Auslaufzeit
- Rotorträgheit
- Scheibenschlag
- Luftreibung

## E1 — \(C(\theta)\)

Für R0–R4:

- Kapazität Elektrode↔Rotor über 360°
- Vorder-/Rückseite
- Abstand
- Gittertyp
- Shield-Distanz

## E2 — PMMA-Oberflächenladung

- definierte Ladung
- Surface Potential vs. Zeit
- 10/20/40/60/80 % RH
- Temperatur konstant
- Materialcharge dokumentieren

## E3 — Gitter vs. Folie, verblindet

Faktoren:

- Vollfolie
- Lochblech
- Messinggitter
- gleiche projizierte Fläche
- gleicher Abstand
- gleiche Bias-Spannung
- randomisierte Reihenfolge

Messen:

- Corona-Onset
- Ionenstrom
- Leckstrom
- Kapazität
- Drehmoment
- Ladung pro Zyklus

## E4 — Rotormaterial

Cu vs. Fe vs. Edelstahl vs. Fe-Ni.

## E5 — sicherer externer Elektrostatik-Motortest

Nur gekapselte, strombegrenzte Labor-/Lehrquelle.

Messen:

\[
P_{mech}=\tau\omega
\]

und elektrische Eingangsleistung gleichzeitig.

## E6 — Ost-West-Test

- Drehtisch
- randomisierte Winkel
- Magnetometer
- Netz-/Gebäudefelder
- gleiche Startenergie
- verblindeter Bediener, soweit praktikabel

## E7 — rückseitige Metallplatte

- Distanzreihe
- floating
- geerdet
- R/C-geerdet
- \(C(\theta)\)
- Drehmoment
- Surface Potential
- Corona

## E8 — Pots

- äußeres Gitter ↔ innere Helix
- Kapazität
- Verlustfaktor
- Leckstrom
- transienter Ladungstransfer

Keine Tesla-Funktion voraussetzen.

## E9 — Crystal als Black Box

Bei niedriger Energie vergleichen:

- offen
- kurz
- Widerstand
- Si-Diode
- geeignete HV-Diode
- antiparallel
- historischer Kristalldetektor, falls sicher verfügbar

Bewerten:

- Gleichrichtung
- Clamping
- Zyklusstabilität
- Torque
- Ladungspumpeneffekt

## E10 — gekoppelte Maschine

Erst nach E0–E9.

\[
E_{in}=E_{mech}+E_{bias}+E_{aux}+E_{stored,initial}
\]

\[
E_{out}=\int u_{load}(t)i_{load}(t)dt+\Delta E_{stored,final}
\]

## E11 — unabhängige Replikation

- Protokoll vorab einfrieren
- Rohdaten veröffentlichen
- zweite Gruppe
- zweite Messgerätefamilie
- Kalibrierzertifikate
- Dummy-/Blindgerät

---

# 27. Metrologiecheckliste

## Elektrisch

- geeigneter HV-Differenztastkopf
- Elektrometer / picoammeter
- kontaktloses elektrostatisches Voltmeter
- isolierte Strommessung
- Oszilloskop mit dokumentierter Masseführung
- LCR-/Impedanzanalysator
- bekannte ohmsche Last
- kalorimetrische Gegenprüfung für Leistungsclaims

## Mechanisch

- Drehgeber
- Drehmomentsensor / Kraftzelle
- Rotorträgheit
- Vibrationsmessung
- Lagertemperatur

## Umwelt

- Temperatur
- relative Feuchte
- Luftdruck
- dreiachsiges Magnetfeld
- elektrisches Umgebungsfeld
- ggf. Luftionen
- Ozon/NOx bei Corona

## EMV

- Faraday-Cage-Test
- Schirmung
- batteriebetriebene Messgeräte
- Netz vollständig trennbar
- RF-Spektrum bei Impulsen

## Messfehler aktiv ausschließen

- Scheinleistung statt Wirkleistung
- Peak × Peak als Leistung
- kalter statt heißer Widerstand
- DMM-Störung durch HV-Impulse
- Scope-Masse als Strompfad
- Körperkapazität
- Anfangsenergie in Speichern
- Rückladung über Messgerät
- Leck-/Koronaströme
- RF-Gleichtaktströme

---

# 28. Datenschema für Experimente

```yaml
experiment_id: E3-grid-vs-foil-001
date_time_utc: ...
operator: ...
repo_commit: ...
cad_variant: ...
machine_reference: M2
rotor:
  diameter_mm: ...
  sector_count: ...
  routing: R0|R1|R2|R3|R4
  conductor_material: Cu|Fe|SS|FeNi
  conductor_diameter_mm: ...
electrodes:
  geometry: foil|square-perf|round-perf|mesh
  material: ...
  gap_mm: ...
  angle_deg: ...
environment:
  temperature_C: ...
  RH_percent: ...
  pressure_hPa: ...
  magnetic_field_uT_xyz: [...]
electrical:
  bias_source: ...
  bias_voltage_V: ...
  current_limit_A: ...
mechanical:
  rpm: ...
  torque_Nm: ...
measurements:
  raw_data_files: [...]
  calibration_files: [...]
notes: ...
```

Keine handschriftliche „best value“-Notiz ohne Rohdaten als Primärresultat verwenden.

---

# 29. Externes Quellenregister

Alle Links am 2026-08-16 recherchiert bzw. gegengeprüft.

## Q01 — Stefan Marinov, *The Thorny Way of Truth, Part V* (1989)

https://archive.org/details/thornywayoftruthpart5maririch

**Status:** wichtigste veröffentlichte direkte Quelle zur kleinen Maschine. Marinov sagt selbst, dass er Geheimnis/Schaltplan nicht vollständig kennt.

## Q02 — Hans Holzherr / Stefan Hartmann, 1999

https://rimstar.org/sdenergy/testa/report99.htm

**Status:** direkter Besucherbericht, Übersetzung 04.08.1999.  
**Schlüssel:** 15 rpm, Lastdemo, R4-Hinweis, 20-lagige Kondensatoren, kleine Modelle, DMM-Probleme.

## Q03 — Principle Experiment

https://rimstar.org/sdenergy/testa/principleexp.htm

**Schlüssel:** Gitter vs. Folie, 60 V, Plattenstapel, Zentralfuß.

## Q04 — Linden Experiment

https://rimstar.org/sdenergy/testa/lindenexp.htm

**Status:** ausdrücklich zweit-handige Erinnerung.

## Q05 — Testatika-Übersicht / Replikationen

https://rimstar.org/sdenergy/testa/

**Nutzen:** historische Archivierung vieler Quellen und negative/konventionelle Replikationen. Rimstar-eigene Theorie stets getrennt halten.

## Q06 — Methernitha technische Beschreibung, archivierte Wiedergabe

Über Rimstar-Testatika-Archiv erreichbar.

**Status:** Betreiber-Narrativ.

## Q07 — Weber/Schneider / Paul-Baumann-Retrospektive, NET-Journal 2011

https://www.yumpu.com/de/document/view/4114787/paul-baumann-erbauer-der-energiemaschine-testatika-93jahrig-

**Schlüssel:** 1984-Geometrie, Lastdemo, 2010-Status, Todesdatum 2011.

## Q08 — Seminarprogramm 13.03.2004

https://guns.connect.fi/innoplaza/energy/conference/Schneider/Testatika.html

**Schlüssel:** bestätigt 13.03.1984 und **05.06.1999**.

## Q09 — Kelly/Bailey IECEC 1991

https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=200902001434259167

**Status:** echte Proceedings-Referenz; keine unabhängige Validierung.

## Q10 — IECEC New Technology Area

https://www.padrak.com/ine/INE10.html

## Q11 — Related Published References / SAFE 1989

https://www.padrak.com/ine/INE11.html

Enthält Bibliographie:
`Methernitha (1989), Informationsfilm Thesta-Distatica: Sound Track Transcription`, Einsiedeln 1989.

## Q12 — Mike Watson 2001

https://www.novakcorp.com/energy/experiments/bswiss.htm

Alternativ:
https://www.robkalmeijer.nl/techniek/experiments/testakica/index.html

**Status:** H2.

## Q13 — Elena Novaretti

Verlags-/Händlerdatensatz:
https://www.gruppomacro.com/prodotti/tutta-la-verita-su-caso-testatika

Groups.io:
https://groups.io/g/testatika/topic/60555379

**ISBN:** 9788868320669

## Q14 — Schneider/Schneider 2023

Bibliographisch:
https://www.eurobuch.ch/buch/isbn/9783906571454.html

Händler:
https://www.kopp-verlag.de/a/testatika-und-weitere-freie-energie-geraete

Abweichende Metadaten:
https://www.auf1.shop/products/testatika-und-weitere-freie-energie-geraete

## Q15 — Relinfo 1990

https://www.relinfo.ch/methernitha/testatika.html

**Status:** unabhängiger Kontext, keine Energievalidierung.

## Q16 — Donald Hasler 1996/1997

https://www.relinfo.ch/methernitha/bericht.html

## Q17 — Elektrostatik-Archiv Antonio Carlos M. de Queiroz

Patente:
https://www.coe.ufrj.br/~acmq/patents.html

Wommelsdorf:
https://www.coe.ufrj.br/~acmq/wommelsd.html

Allgemein:
https://www.coe.ufrj.br/~acmq/electrostatic.html

## Q18 — Wommelsdorf US883846A

https://patents.google.com/patent/US883846A/en

**Schlüssel:** gegenläufige Platten/Systeme; historische Kondensatormaschine.

## Q19 — PMMA charge storage

DOI:
https://doi.org/10.1016/S0304-3886(98)00023-0

## Q20 — Grid geometry / corona

DOI:
https://doi.org/10.1016/j.elstat.2019.103367

## Q21 — Wire-plane corona

DOI:
https://doi.org/10.1016/j.elstat.2010.10.006

## Q22 — Electret review 2024

DOI:
https://doi.org/10.1016/j.nanoen.2024.110167

## Q23 — MEMS electret generator 2011

DOI:
https://doi.org/10.1002/tee.20631

## Q24 — Macroscale electret-like converter 2015

DOI:
https://doi.org/10.1016/j.eml.2015.07.008

## Q25 — Swissreg

https://www.swissreg.ch/

**Status:** offizielle Schweizer Patentdatenbank; systematische Testatika-Suche noch offen.

---

# 30. Quellenpriorität

## Rang A

- Marinov Part V
- Hauser-Originalkorrespondenz
- Originalfotos/-filme
- Holzherr 1999
- Weber/Schneider 1984 als Augenzeugenbericht
- Methernitha-Betreibertext nur für Betreiberbehauptungen

## Rang B

- Novaretti
- Schneider/Schneider quellengetrennt
- SAFE 1989
- Nieper/Matthey als Claims
- Relinfo für unabhängigen Kontext

## Rang C

- Kelly
- Potter
- Rimstar-eigene Theorien
- Watson-Hearsay

## Rang D

- Forenposts ohne Provenienz
- Free-energy-Sammelseiten
- ZPE/Tachyon/Orgon-Erklärungen ohne Messnachweis

---

# 31. Noch zu beschaffende Quellen

Höchste Priorität:

1. Novaretti 2015/2025 komplett.
2. SAFE Proceedings Einsiedeln 1989, besonders Soundtrack-Transkript.
3. Schneider/Schneider 2023 komplett quellenkritisch extrahieren; Impressum fotografieren.
4. Inge Schneider: frühere Publikation des 1984-Berichts.
5. Holzherr-Originalfotos 1999 in maximaler Auflösung.
6. Hauser-Originalskizzen in bestmöglicher Qualität.
7. Vollständige Marinov-Korrespondenz.
8. Methernitha-Film 1989 bestmögliche Masterkopie.
9. P. H. Matthey Originalbericht 1984.
10. Seminarvideo 13.03.2004.
11. Potter-Originaltexte mit Versionsdaten.
12. Kelly 1991 Volltext.
13. Sven Bönisch, `ELEKTRIE`, Nr. 5–8/2003, ISSN 0013-5399.
14. HCRS-Archiv / Originalmessungen.
15. Rimstar-Rohdaten, sofern vorhanden.

---

# 32. Was „funktionierende Replik“ heißen darf

## F1 — geometrisch funktionierend

- Mechanik korrekt;
- Rotor frei;
- Elektroden einstellbar;
- Pots messbar;
- \(C(\theta)\) plausibel.

## F2 — elektrostatik-funktionierend

- ladbar;
- variable-C-Impulse;
- definierter elektrostatischer Torque;
- Charge-Pump-/Rectification-Funktion;
- konventionell bilanziert.

## F3 — historischer Energieclaim reproduziert

Nur wenn:

- alle bekannten Inputs entfernt/bilanziert;
- Anfangsspeicher bilanziert;
- reale Lastleistung über lange Zeit;
- Inputs simultan gemessen;
- unabhängige Replikation;
- Messunsicherheit deutlich unter behauptetem Überschuss.

Bis F3 erreicht ist, kein bestätigter Overunity-/Free-Energy-Status.

---

# 33. Kritische Invarianten

Eine neue Session darf Folgendes nicht vergessen:

1. Testatika war eine **Familie**.
2. Kleine Marinov-Maschine ist einfacher als große Varianten.
3. Keine reibenden Sammelbürsten bei relevanter kleiner Maschine.
4. Rotor-Drahtführung durch die Scheibe ist Schlüsselparameter.
5. R4-Dreifach-Seitenwechsel ist ernst zu prüfen, aber noch nicht sicher M2.
6. Sektormaterial konfliktbehaftet: Cu vs. Fe.
7. Magnete nicht universal.
8. Tesla/HF nicht Kleinmaschinen-Baseline.
9. Crystal-Funktion unbekannt.
10. Gitter-vs.-Folie ist wichtiger experimenteller Hinweis.
11. Feuchte ist kritisch und klassisch erklärbar.
12. Shield-Plate-Effekt ist wichtiger Feldrandbedingungen-Test.
13. 1999 Demo = 05.06.; Übersetzung = 04.08.
14. ~15 rpm wurde 1999 direkt beobachtet.
15. Ausgang historisch als DC beschrieben; kein universelles 230-V/50-Hz-AC.
16. Radiumchlorid wurde von Baumann gegenüber Holzherr verneint.
17. Kurze kW-Demo ist keine Dauerenergiebilanz.
18. Scheiben-Schwungenergie ist viel zu klein für 10-s-kW-Demo.
19. Sichtbare Scheibenmechanik kann bei 15–60 rpm nicht unauffällig kW mechanisch übertragen.
20. Wenn historische kW-Claims real waren, fehlt weiterhin die Quelle dieser Energie.
21. Kontrollierte Replikationen haben bislang keinen bestätigten Nettoenergieüberschuss gezeigt.

---

# 34. Priorisierte Forschungsfragen

## Rotor / CAD

1. War R4 bei M2 vorhanden?
2. Exakte Stitch-Radien?
3. Start-/Endseite?
4. Sektoren isoliert oder verbunden?
5. Cu oder Fe?
6. Drahtdurchmesser exakt?

## Elektroden

7. Form/Maschenweite?
8. Material?
9. Front-/Back-Winkel?
10. Driving und Collecting getrennt oder gleich?

## Pots

11. Anzahl konzentrischer Gitter im kleinen Pot?
12. Helix-Windungszahl/Pitch/Drahtstärke?
13. Helix galvanischer Ausgang oder nur Elektrode?
14. reale Kapazität?
15. Links/rechts symmetrisch?

## Crystal

16. Material?
17. 2 oder 4 Anschlüsse?
18. Diode/Detektor/Schwellwertschalter?
19. Drive- oder Output-Kreis?

## Umwelt

20. Ost-West reproduzierbar?
21. Shield-Effekt rein kapazitiv?
22. Feuchtekennlinie?
23. Corona-/Ionenstrom?
24. Körperkapazität?

## Energie

25. Gibt es unabhängigen Lasttest über Minuten/Stunden?
26. Gewächshaus-Unterlagen?
27. Primärprotokoll 300 V × 10 A?
28. Matthey-Originalbericht?

---

# 35. Empfohlene GitHub-Issues

1. `research: add R4 three-side-change rotor routing`
2. `research: copper vs iron sector material conflict`
3. `sources: acquire Novaretti book and extract unpublished claims`
4. `sources: acquire SAFE 1989 soundtrack transcript`
5. `sources: verify Schneider 2023 physical ISBN and page count`
6. `sources: locate P.H. Matthey 1984 original report`
7. `experiment: blinded mesh-vs-foil test`
8. `experiment: controlled humidity / PMMA charge-decay matrix`
9. `experiment: shield plate distance/grounding matrix`
10. `experiment: randomized east-west orientation test`
11. `metrology: minimum accepted power-balance protocol`
12. `cad: material-swappable rotor conductor fixture`
13. `docs: canonical machine taxonomy M0-M9`
14. `docs: chronology correction 5 June / 4 August 1999`
15. `patents: systematic Swissreg/Espacenet search`

---

# 36. Handoff-Prompt für eine neue KI-Session

> Du arbeitest am GitHub-Projekt `inetconnector/testatika-small-research-replica`. Lies zuerst `AGENTS.md`, `README.md`, `ADDON.md` und danach `STATE.md` vollständig. Lies anschließend Augenzeugen-Dossier, Quellenbasis, Evidenzmatrix und hardwarebezogene Forschungsdateien. Behandle Testatika als Familie verschiedener Maschinen. Trenne direkte Beobachtung, Betreiberbehauptung, Hearsay, Rekonstruktion und wissenschaftliche Kontrollliteratur. Die kleine Marinov-Maschine ist die primäre CAD-Referenz; Tesla/HF ist nicht Baseline. Erfinde keine Originalverdrahtung. Besonders wichtig sind Rotor-Drahtführung durch die Scheibe, der Holzherr-Hinweis „changing sides three times“ als R4-Hypothese, Cu-vs.-Fe-Materialkonflikt, Gitter-vs.-Folie, Feuchte, Shield-Plate-Effekt, Crystal-Funktion und Driving-vs.-Collecting-Elektroden. Energieerhaltung ist Nullhypothese. Jede Leistungsaussage muss alle Inputs, gespeicherte Anfangsenergie, mechanische Leistung und reale Lastleistung bilanzieren. Historische kW-Claims sind nicht unabhängig verifiziert. Bei neuen Quellen immer URL, Datum, Provenienz, Maschinen-ID, Evidenzklasse, neue Information, Konflikte und CAD-/Experimentfolgen dokumentieren. CAD nie ohne Evidenzdokumentation ändern; STL/STEP/Manifest synchron halten.

---

# 37. Forschungsstand in einem Satz

> **Die am besten belegte Testatika-Technik ist eine Familie ungewöhnlich aufwendig gestalteter elektrostatischer Influence-/Variable-C-Maschinen mit nichtkontaktierenden Elektroden, Polymer-/Gitterstrukturen, Ladungsspeichern und modellabhängigen Zusatzstufen; die historische Geometrie lässt sich zunehmend rekonstruieren, aber weder die exakte kleine Originalverdrahtung noch eine unabhängige Energiebilanz für die behaupteten kW-Leistungen ist überliefert.**

---

# 38. Änderungsverlauf

## ADDON v1.0 — 2026-08-16

Neu bzw. explizit konsolidiert:

- Repository-Handoff;
- Maschinen-Taxonomie;
- 1999-Datum korrigiert;
- R4-Dreifach-Seitenwechsel;
- 1984 Weber/Schneider-Geometrie;
- Principle-Experiment-Gitter/Folie/Zentralfuß;
- Linden Experiment als Hearsay;
- Watson Cu/Fe-Konflikt;
- Nieper/Matthey;
- IECEC-Bibliographie;
- Novaretti als offene Quellenlücke;
- Schneider-2023-Bibliographiekonflikt;
- Methernitha-2010-Status;
- Baumann-Todesdatum-Korrektur;
- Wommelsdorf/Poggendorff als konventionelle Kontrollbasis;
- PMMA-/Corona-/Grid-/Electret-Fachliteratur;
- Patent-Negativsuche als offene Aufgabe;
- Masterexperimentplan;
- Datenformat;
- Handoff-Prompt.

---

# 39. Schlussregel

Diese Datei soll nicht durch ungefilterte Spekulation wachsen.

Neue Information nur aufnehmen, wenn mindestens eine Bedingung erfüllt ist:

1. neue Primär-/Augenzeugenquelle;
2. neue hochauflösende Geometrie;
3. neues Messprotokoll;
4. belastbare Fachliteratur;
5. klarer Konflikt, der Annahmen verändert;
6. negative Replikation, die konkrete Hypothese falsifiziert.

Jeder neue Eintrag benötigt:

- Quelle;
- Provenienz;
- Evidenzklasse;
- Maschinen-ID;
- Aussage;
- Unsicherheit;
- Konflikt;
- Konsequenz für CAD/Experiment/Wissensstand.

**Kein Detail stillschweigend von einer Testatika-Variante auf eine andere übertragen.**

---

# POST-AUDIT HARDENING NOTE — 2026-08-16

Dieser Block ist **additiv** und hat Vorrang vor veralteten Repository-Metadaten im Kopf dieser Datei.

1. Die kanonische Datei heißt weiterhin `addon.md`. Zusätzlich existiert nun `ADDON.md` als case-sicherer Kompatibilitäts-Einstieg, damit ältere Session-Anweisungen auf Linux/macOS nicht ins Leere laufen.
2. Der im historischen Header genannte Audit-Tree `aa20ef...` ist ein damaliger Audit-Anker, **nicht der aktuelle Repository-Head**. Aktuelle Sessions müssen den tatsächlichen `main`-Commit aus Git bestimmen und dürfen keinen fest verdrahteten alten SHA als Gegenwartsstand behandeln.
3. Vor `STATE.md` sollte eine neue Session jetzt `docs/REPLICATION_STATUS.md`, `docs/research/machines.yaml` und `docs/research/provenance-schema.yaml` berücksichtigen.
4. `testatika.zip` ist ein externer/nicht öffentlich redistribuierter Forschungskorpus und **nicht Bestandteil des öffentlichen Git-Repositories**. Siehe `docs/research/external-corpus.md`.
5. Die historische Sicherungsreferenz `state_pre_corpus_rebuild.md` war beim Audit nicht als Datei im öffentlichen Tree vorhanden; kein Ersatzinhalt darf erfunden werden.
6. V3 ist in `main` integriert. Der frühere Branch `research/small-machine-v3-pixel-analysis` ist nur noch Provenienz, keine Voraussetzung für Zugriff auf V3-Dateien.
7. `V3_COMPLETE` ist ein Convenience-Dateiname; die V3-Modellmetadaten bleiben `experimental` / photo interpretation.
8. Der 1:1-Zielbegriff ist evidenzgebunden: unbekannte Originaldetails bleiben UNKNOWN und werden durch reversible Varianten abgedeckt, bis Primärevidenz sie schließt.

## Aktualisierte Startreihenfolge

1. `AGENTS.md`
2. `README.md`
3. `docs/REPLICATION_STATUS.md`
4. `addon.md`
5. `STATE.md`
6. `docs/sources.md`
7. `docs/research/source-basis.md`
8. `docs/research/evidence_matrix.tsv`
9. `docs/research/machines.yaml`
10. `docs/research/provenance-schema.yaml`
11. `docs/research/experiment-plan.md`
12. relevante Subsystem-Dokumente

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


## Internet source audit 2026-08-17

A broad provenance-first public Internet crawl is integrated. Canonical entry points: `docs/research/internet-source-audit-2026-08-17.md`, `internet-source-ledger.tsv`, `control-replication-audit-2026-08-17.md`, `source-acquisition-backlog.tsv`.

Important corrections: M2 East-West startup is Baumann→Marinov source-stated (post-start orientation independence is separately Marinov-observed); rear metal-plate stop is direct Marinov observation; dry-air ~3–4 pushes, humidity dependence, restart memory and ~60 rpm are retained as model-specific observations. TWT-VII adds unresolved two-disc thick-grid/thin-sector asymmetry. New taxonomy: M6c large-under-construction Marinov conflict family, M8 ~1m, M9 ~2m, M10 tandem/double converter. Do not alter Hauser M6a CAD from these without an explicit object/source bridge. Kelly remains photo-derived/S2. No authentic complete hidden circuit or net-energy proof was found.


## Primary-publication web-audit addendum 2026-08-17

New stronger sources: Kelly/Bailey 1991 original IECEC PDF; Nieper 1985 book mirror including the L. L. Rorschach 17-Mar-1984 witness report; Schneider/Weber 13-Mar-1984 account republished by NET-Journal; recipient-side publication of a 2010 Methernitha reply. See `docs/research/internet-source-audit-addendum-2026-08-17.md` and `witness-source-independence-1984.md`.

Do not double-count M5 and M5a as independent until source dependence is resolved. Kelly/Bailey explicitly were not direct machine witnesses and their geometry is secondary/photo-derived. The 1999 engineer-demo date is CONFLICT (5 Jun vs 4 Aug / early-Aug publication chain). No hidden original circuit or closed historical net-energy proof was found.
