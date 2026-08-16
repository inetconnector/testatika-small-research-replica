# Baumanns Erklärsprache entschlüsselt — Quellenkritische technische Übersetzung

**Stand:** 2026-08-16  
**Status:** Forschungsdokument / keine behauptete Originalschaltung  
**Zweck:** Alle auffindbaren Aussagen von Paul Baumann bzw. Methernitha zur Funktionsweise der Testatika nach Provenienz trennen, in konventionelle technische Begriffe übersetzen und daraus ein konsistentes, falsifizierbares Arbeitsmodell ableiten.

---

# 1. Wichtigste Korrektur vorab: „unbekannte Sprache“ ist derzeit KEIN belegtes Marinov-Zitat

Im Projekt war sinngemäß die Aussage im Umlauf, Paul Baumann habe Stefan Marinov die Maschine erklärt, Marinov habe die Erklärung aber wie eine „unbekannte Sprache“ empfunden und deshalb weiterhin nichts verstanden.

Nach erneuter Suche in:

- dem Repository-Korpus;
- Marinov-Material und späteren Marinov-Texten;
- Hans Holzherrs direktem Besuchsbericht;
- archivierter Methernitha-Funktionsbeschreibung;
- Mike-Watson-Hearsay;
- dem Linden-/Principle-Experiment-Material;
- späteren technischen Kompilationen

ist die **wörtliche Zuschreibung an Marinov nicht verifiziert**.

Was sich dagegen sauber belegen lässt, sind drei getrennte Sachverhalte:

1. **Marinov:** Er verstand das vollständige Wirkprinzip nicht, kannte den exakten Schaltplan nicht und konnte die Maschine nicht reproduzieren. Das ist bereits in `STATE.md` dokumentiert.
2. **Hans Holzherr:** Er schrieb nach dem Besuch von 1999, dass er Baumann schwer verstand, weil dieser leise und schnell sprach und seine Erklärungen in **nicht-wissenschaftlichen Begriffen** gab.
3. **Methernitha selbst:** In der eigenen technischen Beschreibung heißt es sinngemäß, die übliche physikalische Terminologie reiche nur teilweise aus; für Teile der Maschine benutze man eigene Begriffe wie `Taster`/`antenna keys`.

Daraus kann leicht die spätere Paraphrase „Baumann sprach für Marinov wie in einer unbekannten Sprache“ entstanden sein. Für eine quellenkritische Wissensbasis muss aber künftig formuliert werden:

> **Marinov verstand das vollständige Testatika-Prinzip trotz seiner Untersuchungen nicht. Unabhängig davon berichtete Holzherr, Baumanns Erklärungen seien schwer verständlich und nicht-wissenschaftlich formuliert gewesen; Methernitha selbst verwendete bewusst eigene Begriffe. Ein direktes Marinov-Zitat „wie eine unbekannte Sprache“ ist bislang nicht belegt.**

Diese Korrektur ist wichtig, weil sie aus einer scheinbaren Primäraussage wieder drei unterschiedlich starke Quellen macht.

---

# 2. Quellenhierarchie speziell für „Was sagte Baumann?“

| ID | Quelle | Sprecher / Übertragung | Klasse | Verwendbarkeit |
|---|---|---|---|---|
| B01 | ehemalige Methernitha-Web-/Film-Beschreibung | institutionelle Methernitha-Erklärung | O1 | beste Quelle für Methernithas eigene Begriffe, keine unabhängige Physikvalidierung |
| B02 | Hans Holzherr 1999 | direkter Besucher; Baumann vor Ort | P1 | stark für beobachtete Demo und ausdrücklich Baumann zugeschriebene kurze Aussagen |
| B03 | Principle Experiment 1999 | Holzherr beobachtet Baumanns Demonstration | P1 | stark für Geometrie/Demo; Erklärung des Grundprinzips unvollständig |
| B04 | Linden Experiment | zwei Besucher → Dritter schreibt Erinnerung | H2 | besonders interessant für Baumanns „random particles / rectify flux“-Sprache, aber ausdrücklich second hand |
| B05 | Stefan Marinov | direkte Besuche/Untersuchung; eigene Veröffentlichungen | P1/I1 | stark für das, was er sah; seine Funktionsdeutung separat behandeln |
| B06 | Baumann → Marinov | einzelne von Marinov berichtete Aussagen | M3/P1 | z. B. `crystal`; nur dort hoch gewichten, wo Marinov selbst Quelle ist |
| B07 | Luzi Cathomen Amateurvideo | Cathomen direkt aufgenommen | O1/P1 | sehr wertvoll für Werkstattdenken, aber **nicht Baumann** |
| B08 | Mike Watson 2001 | Marinov → Watson → Mail/Web | H2 | Hinweise, keine Primärquelle |
| B09 | Frolov 2021 | späte Kompilation unbekannter Ursprungsketten | H2/I1 | nur Source Leads; 1-kΩ- und „never withdraw electrons“-Claims nicht primär bestätigt |
| B10 | Potter/Kelly | Backengineering | I1 | nicht als Baumann-Aussage behandeln |

---

# 3. Was Methernitha offiziell sagte — Baustein für Baustein

Archivierte technische Beschreibung:

`https://rimstar.org/sdenergy/testa/methernitha_testatika_technical_info.htm`

Die Quelle reproduziert den früheren technischen Text der Methernitha-Webseite. Sie ist daher besonders wichtig, um die **eigene Sprache der Gruppe** zu verstehen.

## 3.1 „Eine Scheibe ist die Erde, die andere die Wolke“

### Quellenwortlaut sinngemäß

Zwei gegenläufige Scheiben erzeugen elektrostatische Ladung; eine stellt Erde, die andere Wolke dar.

### Technische Übersetzung

Das sollte zunächst als **Analogie für zwei Potential-/Polaritätsräume** gelesen werden:

- zwei gegensinnig bewegte Ladungsträgersysteme;
- unterschiedliche bzw. entgegengesetzte Oberflächenpotentiale;
- ein starkes elektrisches Feld zwischen diesen Systemen;
- ähnliche Feldgeometrie wie ein großflächiger Kondensator „Wolke–Erde“.

Die Analogie beweist **nicht**, dass atmosphärische Energie eingespeist wird. Sie beschreibt zunächst eine Feld-/Potentialstruktur.

### Arbeitsbegriff

**bipolares elektrostatisches Bias-/Feldsystem**

---

## 3.2 „Mit Gitterelektroden wird die Ladung festgehalten“

### Technische Übersetzung

`festhalten` kann physikalisch bedeuten:

- Feldlinien und Potentialverteilung definieren;
- induzierte Oberflächenladung an einer statischen Elektrode tragen;
- Raumladungs-/Corona-Transport regulieren;
- ein dielektrisches Oberflächenpotential gegenüber Leckpfaden stabilisieren;
- Ladung in einem kapazitiven Knoten puffern.

Perforation ist dabei nicht bedeutungslos. Moderne Corona-Literatur zeigt, dass Gittergeometrie:

- Corona-Onset;
- Strom-Spannungs-Kennlinie;
- Stromdichteverteilung;
- Potentialgradienten

stark beeinflussen kann.

### Arbeitsbegriff

**feldformende / kapazitive Gitterelektrode mit möglicher Raumladungssteuerung**

---

## 3.3 „Taster“ / englisch später „antenna keys“

Die englische Übersetzung `antenna keys` klingt nach Funkantenne und hat viele spätere HF-Deutungen provoziert. Im deutschen Kontext ist `Taster` wesentlich neutraler.

### Technische Übersetzung

Da die Teile ausdrücklich **berührungsfrei** arbeiten, ist der konservativste Begriff:

**nichtkontaktierender kapazitiver/Influenz-Abnehmer**

Mögliche Funktionen:

- lokale Potentialprobe;
- Ladungsinduktion;
- displacement-current pickup;
- feldabhängiger Sammelelektrodenknoten;
- bei ionisierter Luft zusätzlich Ionenstrom-Sammler.

### Wichtig

`Taster` ist **kein Beleg für RF-Antennenbetrieb**.

---

## 3.4 „Die Ladungen werden geordnet“

### Technische Übersetzung

`ordnen` ist am ehesten:

- Polarität trennen;
- Ladung auf definierte Knoten verteilen;
- wechselnde/impulsartige Ladung in einen gerichteten Ladungstransfer überführen;
- positive und negative Halbwellen/Positionen verschiedenen Speichern zuführen.

### Arbeitsbegriff

**polarity sorting / charge routing**

---

## 3.5 „Gleichrichterdiode hält die Zyklen im Takt“

Das ist eine der technisch aussagekräftigsten Methernitha-Formulierungen.

### Wichtige Konsequenz

Eine Diode, die den **mechanischen Anziehungs-/Abstoßungszyklus** stabilisiert, ist funktionell mehr als ein bloßer Ausgangsgleichrichter.

Plausible technische Rollen:

1. Rückladung in einer bestimmten Rotorphase verhindern;
2. Ladung erst ab einer Schwellspannung auf einen anderen Knoten übertragen;
3. die Polarität eines Elektrodenknotens über einen Teil der Rotation „festhalten“;
4. Ladungszustände zweier Rotorpositionen asymmetrisch machen;
5. dadurch elektrostatisches Drehmoment phasenrichtig erzeugen;
6. einen Regenerations-/Kommutationszyklus stabilisieren.

### Arbeitsbegriff

**nichtlineares Ladungsventil / phasenselektiver Clamp / elektrostatischer Kommutator**

Das passt bemerkenswert gut dazu, dass Baumann gegenüber Marinov vom oberen Bauteil als `crystal` sprach, während spätere Zeichnungen es als `rectifier` bezeichneten.

---

## 3.6 „Sonst würden die Anziehungs- und Abstoßungsimpulse die Scheibe immer schneller machen“

Wörtlich genommen ist diese Formulierung mechanisch problematisch: Ein passives System beschleunigt nicht unbegrenzt, weil Verluste, Feldrückwirkung und Ladungszustände Grenzbedingungen setzen.

Als **Regelungsbeschreibung** ist sie jedoch sinnvoll:

- Ladungsphase relativ zum Rotorwinkel bestimmt Vorzeichen und Größe des Drehmoments;
- ohne geeigneten Entlade-/Rückladezeitpunkt kann die Rotationsphase instabil werden;
- mit Diode/Schwelle kann ein definierter Grenzzyklus entstehen.

### Arbeitsbegriff

**phase-locked electrostatic commutation**

---

## 3.7 „Richtige Geschwindigkeit ist sehr wichtig; langsam und gleichmäßig“

Das spricht stark gegen die Idee, die sichtbare Rotation sei nur zufälliges Beiwerk.

Plausible klassische Ursache:

- elektrische Relaxationszeit `tau = R*C`;
- Oberflächenleckage;
- Corona-/Ionentransportzeit;
- Charge-Trapping in PMMA;
- Zeit, bis ein floating node eine Schwellspannung erreicht;
- Zeitfenster eines Dioden-/Crystal-Knotens.

Wenn Rotorereignisfrequenz und elektrische Relaxation zusammenpassen, kann die Phasenlage stabil sein.

### Arbeitsbegriff

**RC-/Ladungsrelaxations-Synchronisation**

Nicht ableiten:

- universelle 50-Hz-Netzfrequenz;
- bewiesene HF-Resonanz.

---

## 3.8 „Gitterkondensatoren speichern Energie und geben sie gleichmäßig ab“

Das ist technisch unproblematisch:

- Ladungsspeicher;
- DC-Puffer;
- Glättung;
- Potentialreservoir;
- eventuell floating capacitive divider.

### Aber

Ein Kondensator erhöht nicht von selbst die Energie. Er kann:

- Spannung/Strom zeitlich umverteilen;
- Spitzenleistung liefern;
- Impedanz anpassen;
- eine kurze Lastdemo ermöglichen.

### Arbeitsbegriff

**HV charge reservoir / buffer capacitor network**

---

## 3.9 „Hohe Spannung heruntersetzen und Leistung mit zusätzlichen Einrichtungen aufbauen“

Diese Formulierung ist der am schlechtesten erklärte Teil der offiziellen Beschreibung.

`Leistung aufbauen` kann in Ingenieurssprache bedeuten:

- hohe Spannung / kleiner Strom → niedrigere Spannung / höherer Strom umformen;
- Pulsenergie sammeln und in anderer Impedanz ausgeben;
- kapazitive Ladungspumpe;
- induktive Impedanztransformation;
- gepulsten DC-Strom konditionieren.

### Wichtige Einschränkung

Ein klassischer Transformator funktioniert nicht mit ideal stationärem DC. Wenn das interne System DC-Potentiale verwendet, muss eine Transformatorwirkung durch **zeitliche Änderungen** entstehen:

- Rotor-Kommutation;
- impulsartige Umladung;
- Corona-/Spark-Transienten;
- Diodenschalten;
- variable Kapazität.

Daher ist ein Begriff wie

**DC-biased pulsed impedance/charge converter**

besser als „50-Hz-Trafo“.

---

## 3.10 „Je trockener die Luft, desto besser“

Das passt vollständig zu bekannter Elektrostatik:

- PMMA-Ladungsspeicherung ist feuchteabhängig;
- Oberflächenleitfähigkeit ändert sich;
- Corona-Modi und Corona-Onset ändern sich;
- Leckströme ändern sich.

Quellenvergleich:

- PMMA charge storage: DOI `10.1016/S0304-3886(98)00023-0`
- grid-corona geometry: DOI `10.1016/j.elstat.2019.103367`
- humidity in three-electrode corona: DOI `10.1016/0304-3886(95)00009-Y`

Die Feuchteabhängigkeit ist daher **kein Hinweis auf exotische Energie**, sondern ein starkes Argument dafür, Feuchte als Hauptparameter jeder Replikation zu kontrollieren.

---

# 4. Was Baumann im Principle Experiment tatsächlich demonstrierte

Quelle:

`https://rimstar.org/sdenergy/testa/report99.htm`

Direkter Besucherbericht von Hans Holzherr.

## 4.1 Beobachteter Aufbau

- schwenkender Plexiglasarm;
- perforierte Aluminiumlage;
- Messingdrahtgitter;
- mehrere Plexiglas-/Gitterlagen;
- zwei parallele Kondensatoren;
- ungefähr zehn Hin-/Herbewegungen;
- berichtete 60 V DC;
- Kurzschlussknall.

## 4.2 Entscheidende Baumann-Aussage

Holzherr fragte nach Materialfunktion. Baumann sagte sinngemäß:

> **Mit geschlossener Metallfolie statt Drahtgitter entstehe der Effekt nicht.**

Das ist einer der stärksten konkreten Konstruktionshinweise überhaupt.

## 4.3 Was das in normaler Physik heißen kann

Gitter statt Folie ändert gleichzeitig:

- Randlänge;
- lokale Feldüberhöhung;
- Kapazitätsmatrix;
- Feldpenetration;
- Corona- und Ionenpfade;
- Oberflächenladungsverteilung;
- Kopplung durch das Dielektrikum.

Darum muss `mesh vs foil` experimentell isoliert werden; genau dafür existiert im Repo inzwischen der V3-A/B-Testzweig.

---

# 5. Das Linden-Experiment: die deutlichste überlieferte „Baumann-Sprache“

Quelle:

`https://rimstar.org/sdenergy/testa/lindenexp.htm`

**Achtung:** Diese Quelle sagt selbst, dass die Information second hand und aus Erinnerung stammt.

## 5.1 Überlieferte Erklärung

Zwei Ingenieure sollen Baumann nach dem Prinzip gefragt haben. Seine Erklärung wird sinngemäß so wiedergegeben:

- in der Natur gebe es sehr feine Teilchen;
- sie bewegten sich zufällig/fluktuierend und sehr schnell;
- um daraus Nutzen zu ziehen, müsse man diesen Fluss **richten / gleichrichten**.

Danach demonstrierte er:

- U-/Hufeisenmagnet;
- Drahtschleife;
- zwei Metallplatten mit Papier als Dielektrikum;
- Platten im Magnetspalt;
- berichtete hohe Spannung.

Ihm wird anschließend sinngemäß die Aussage zugeschrieben:

> Wenn man diesen Versuch verstehe, verstehe man auch das Funktionsprinzip; dies sei nur der Anfang.

## 5.2 Quellenstatus

Diese Aussagen sind **H2**. Sie dürfen nicht zum originalen Baumann-Schaltplan hochgestuft werden.

## 5.3 Technische Übersetzung von „zufällige Teilchen richten“

Es gibt mehrere mögliche Bedeutungsebenen:

### A. Luftionen / Raumladung

Dann bedeutet `random particles`:

- positive/negative Ionen;
- Elektronen nur in stark ionisierten Bereichen;
- geladene Aerosole.

`rectify/order` wäre:

- Feldgradient erzeugen;
- Ladungsträger nach Polarität driften lassen;
- asymmetrisch einsammeln.

### B. schwankende induzierte Oberflächenladung

Dann sind `particles` metaphorisch für Ladungsträger/Elektronen im Leiter. `Richten` wäre ein Dioden-/Schwellwertprozess.

### C. thermische Zufallsbewegung

Wenn Baumann tatsächlich thermische Gleichgewichtsfluktuationen meinte, gilt eine harte physikalische Grenze:

> Ein passives Gleichrichten von thermischem Gleichgewichtsrauschen liefert ohne Nichtgleichgewichtsquelle keine dauerhafte Nettoarbeit.

Dann müsste eine zusätzliche freie Energiequelle vorhanden sein, z. B.:

- mechanische Rotorarbeit;
- atmosphärisches elektrisches Feld;
- Corona/Ionisierung;
- Temperaturgradient;
- externe EM-Kopplung;
- gespeicherte elektrische Energie.

### D. unbekannte „Äther“-Teilchen

Spätere Autoren setzen Baumanns Teilchen mit Äther-/Vakuumteilchen gleich. Dafür existiert **keine belastbare direkte Messung**. Diese Interpretation bleibt I1/H.

## 5.4 Der wichtigste sachliche Kern

Unabhängig davon, was Baumann mit `Teilchen` meinte, ist die **operationale Aussage** klarer als die Ontologie:

> Es gibt einen zunächst bidirektionalen/fluktuierenden Ladungs- oder Feldprozess, der durch Geometrie und Nichtlinearität in einen gerichteten Ladungstransfer überführt werden soll.

Das ist technisch als **rectification + charge sorting** modellierbar.

---

# 6. Hans Holzherr erklärt, warum Baumanns Sprache so schwer zu verstehen war

Quelle:

`https://www.novakcorp.com/energy/experiments/tesnews.htm`

Holzherr schrieb direkt nach dem Besuch sinngemäß:

- Baumann sprach leise;
- schnell;
- und erklärte in **nicht-wissenschaftlicher Terminologie**.

Das ist die bislang klarste Quelle für die oft wiederholte Behauptung von der „unverständlichen Sprache“.

### Konsequenz für dieses Projekt

Wir müssen Baumanns Wörter **nicht wörtlich ontologisch glauben**, sondern in messbare technische Zustandsgrößen übersetzen.

Beispiel:

| Baumann-/Methernitha-Wort | Nicht automatisch bedeuten | Messbare Übersetzung |
|---|---|---|
| Wolke / Erde | kosmische Energiequelle | zwei Potential-/Feldreservoirs |
| Ladung festhalten | Elektronen einfrieren | floating/statischer Feldknoten, geringe Leckage |
| Taster | HF-Antenne | non-contact capacitive pickup |
| ordnen | mystische Ordnung | polarity routing / rectification |
| im Takt halten | 50 Hz Netz | phase-selective charge commutation |
| Kapazität erhöhen | Energie erzeugen | C erhöhen / gespeicherte Ladung umverteilen / effektive Impedanz ändern |
| Leistung aufbauen | Overunity | U/I-Transformation bzw. Power conditioning |
| Teilchen richten | Äther bewiesen | asymmetrischer Transport geladener Träger |

---

# 7. Luzi Cathomen: Werkstatt-Erklärung — NICHT mit Baumann verwechseln

Ein Amateurvideo dokumentiert Luzi Cathomen, nicht Paul Baumann. Es ist trotzdem extrem wertvoll, weil Cathomen die Maschine praktisch mitentwickelte/baute.

Transkript u. a. archiviert unter:

`https://www.allmystery.de/themen/gw11473-5`

## 7.1 Wesentliche Aussagen

Cathomen erklärt sinngemäß:

1. Rotorsegmente seien Speziallegierungen und könnten magnetisiert werden.
2. Scheiben sollen ungefähr 60 rpm laufen, nicht schneller.
3. Seitliche Behälter seien Kondensatoren/Leydener Flaschen.
4. Das elektrostatische Feld werde an zwei Polen abgenommen.
5. Die Energie gehe „nach oben“ und werde dort „verstärkt“.
6. Ein Besucher nennt dies Transformator; Cathomen betont jedoch den DC-Charakter.
7. Es liege intern sehr hohe Spannung vor; im Gespräch wird ~100 kV genannt.
8. Die obere Einrichtung erhöhe „Kapazität“; auf Nachfrage verweigert Cathomen Details und erwähnt Magnete sowie wahrscheinlich Spulen.
9. Danach gehe Energie zurück zu Kondensatoren, werde gespeichert und von dort ausgegeben.
10. Die Abnehmer berühren die Scheibe nicht.
11. Ein `Fühler` diene den Impulsen bzw. einer konstanten Frequenz/Drehzahl — Cathomen stimmt dem Begriff Synchronsteuerung zu.
12. Die Ausgangsidee sei durch statische Elektrizität bei Schallplatten entstanden.
13. Bei Schul-/Demonstrationsgeräten bekomme man nur einen einzelnen Spannungsimpuls; das Problem sei, **die Spannung aufrechtzuerhalten**.

## 7.2 Warum das technisch wichtig ist

Der letzte Punkt ist vielleicht die klarste Werkstattbeschreibung des eigentlichen Entwicklungsproblems:

> Nicht „wie erzeuge ich einmal Hochspannung?“, sondern „wie regeneriere ich den Ladungszustand zyklisch, ohne dass er nach einem Impuls zusammenbricht?“

Das passt zu:

- Influence self-excitation;
- variable capacitance;
- nichtkontaktierenden Pickups;
- phasenrichtigem Ladungsrouting;
- Dioden/Crystal-Kommutation;
- Speicherbus.

## 7.3 Was `verstärken` wahrscheinlich NICHT bedeutet

Es darf nicht als Beweis eines Energieverstärkers verstanden werden.

Technisch könnte gemeint sein:

- Spannungstransformation;
- Stromaufbereitung;
- Ladungsakkumulation über mehrere Zyklen;
- Impedanzumformung;
- Pulsformung.

---

# 8. Was Baumann Marinov konkret sagte — gesicherter Kern

Aus dem Marinov-Korpus ist besonders wichtig:

## 8.1 `Crystal`

Marinov korrigiert spätere Begriffe:

- Baumann habe von einem **`crystal`** gesprochen;
- nicht sicher von einem `rectifier`.

Marinov wusste die Funktion nicht.

### Technische Interpretation

Ein Kristall kann in historischem Elektronikkontext sein:

- Halbleiter-Gleichrichter;
- Detektorkristall;
- nichtlinearer Kontakt;
- schwellwertabhängiger Leiter.

Damit passt er sehr gut zur offiziellen Aussage über eine Diode, die den Zyklus stabilisiert.

Aber:

- Material unbekannt;
- Anschlusszahl unsicher;
- Position im Drive-/Outputpfad unsicher.

## 8.2 Wolke-/Erde-Analogie

Auch in Hauser-/Weber-Berichten wird Baumann die Wolke-/Erde-Erklärung zugeschrieben.

Das stützt, dass die Analogie wirklich Teil von Baumanns eigener Erklärsprache war.

## 8.3 Spezialmaterial großer Scheiben

Späte Überlieferungen Baumann→Marinov/Watson nennen eine leicht magnetisierte Fe-Ni-Speziallegierung für größere Maschinen.

Status:

- nicht auf kleine Cu-Draht-Maschine übertragen;
- H2 bei Watson;
- Material experimentell offen halten.

## 8.4 Das Entscheidende: Baumann gab Marinov offensichtlich KEINEN reproduzierbaren Schaltplan

Marinov konnte trotz:

- Besuchen;
- Anfassen/Testen der kleinen Maschine;
- Einsicht in einzelne Komponenten;
- Gesprächen mit Baumann

das System nicht reproduzieren.

Das bedeutet für jede moderne Rekonstruktion:

> Baumanns Erklärungen waren entweder unvollständig, nicht in Ingenieurterminologie formuliert, auf ein Prinzip statt auf Verschaltung bezogen oder enthielten bewusst ausgelassene Details.

---

# 9. Was Marinov selbst daraus verstand

Marinov entwickelte später ein eigenes Modell. Dies ist **Marinovs Interpretation**, nicht Baumanns bestätigte Schaltung.

## 9.1 Kopplung aus Influenzgenerator + Elektrostatikmotor

Marinovs Arbeitsmodell:

- Wimshurst-/Holtz-artiger Influenzgenerator;
- Gruel-/Poggendorff-artiger Elektrostatikmotor;
- dieselbe Scheibe übernimmt Generator- und Motorfunktion.

Diese Topologie ist bemerkenswert plausibel für die sichtbare Maschine.

## 9.2 Zwei elektrische „Busse“

Marinov vermutete sinngemäß:

- kleinen Kapazitätswert / hohe Spannung für Driving-Elektroden;
- größere Kapazität / niedrigere Spannung für Collecting-/Lastkreis.

Das lässt sich technisch als **Zwei-Bus-System** formulieren:

### H-Bus

- hohe Spannung;
- geringe gespeicherte Ladung pro Kapazität;
- bestimmt das elektrostatische Rotorfeld;
- möglichst nicht direkt durch Last entladen.

### L-Bus

- niedrigere Spannung;
- größere effektive Kapazität;
- Lastpuffer;
- bekommt pro Zyklus Ladung übertragen.

## 9.3 Warum Marinov trotzdem scheiterte

Marinov baute eigene Influenzgenerator-/Motorversuche und bekam den typischen kleinen Strom solcher Maschinen. Er schrieb später, dass er keinen Weg sah, den hohen behaupteten Testatika-Strom zu erreichen.

Das ist eine zentrale negative Information:

> Marinov hatte wahrscheinlich die **Topologieklasse** verstanden, aber nicht denjenigen konstruktiven Mechanismus, der nach den historischen Claims den hohen Laststrom erzeugt haben soll.

---

# 10. Die beste technische Übersetzung des gesamten Baumann-Narrativs

Aus allen höher gewichteten Aussagen ergibt sich folgende **kohärente Arbeitsarchitektur**.

## Stufe A — Feld/Bias erzeugen

Rotierende segmentierte Kunststoffscheibe(n) erzeugen durch Influenz/tribo-/electret-artige Ladung ein starkes elektrostatisches Potential.

Mögliche Zustandsgröße:

`V_R(theta,t)` = Rotoroberflächenpotential.

---

## Stufe B — variable Kapazität / Feldmodulation

Rotorsegmente bewegen sich relativ zu stationären Gitter-/Tasterelektroden.

Damit gilt allgemein:

`Q = C(theta) * V`

und

`i = V*dC/dt + C*dV/dt`.

Auch ohne mechanischen Kontakt entsteht ein displacement-/induction current.

---

## Stufe C — Ladung nicht direkt vom Rotor „verbrauchen“

Die historische Erklärsprache legt nahe, dass der Rotor eher **Feld-/Biasgeber** ist und die nutzbare Ladung an sekundären/floating Elektroden induziert wird.

Das ist eine technisch wichtige Unterscheidung:

- direktes Entladen des Rotors zerstört seinen Bias;
- induktive/kapazitive Aufnahme kann den Rotorzustand teilweise erhalten;
- dennoch erzeugt reale Last unter klassischer Physik eine Rückwirkung, die irgendwo energetisch bezahlt werden muss.

---

## Stufe D — Ladungen „ordnen“

Dioden-/Crystal-/Schwellwertpfade leiten Ladung nur in bestimmten Phasen weiter.

Das kann eine **elektrostatische Ladungspumpe** erzeugen.

---

## Stufe E — den Motorzyklus phasenrichtig regenerieren

Ein Teil der Ladung bleibt/kehrt in den Driving-Bus zurück.

Die sichtbare Langsamkeit ist dann keine Schwäche, sondern Teil der Kommutation:

- Rotorwinkel;
- RC-Zeit;
- Leckage;
- Crystal-Schwellwert;
- Elektrodenposition

müssen zueinander passen.

---

## Stufe F — Ausgangspuffer

Gitterkondensatoren/Leydener Flaschen sammeln viele kleine Ladungsimpulse und liefern einen glatteren DC-Ausgang.

---

## Stufe G — zusätzliche Umformung größerer Maschinen

Magnet-/Spulen-/Mehrgitter-Baugruppen können bei größeren Geräten:

- gepulsten Strom transformieren;
- induktive Energie zwischenspeichern;
- Impedanz verändern;
- Spannungs-/Stromverhältnis verändern;
- Transienten formen.

Sie müssen **nicht** das Grundprinzip der kleinen Maschine sein.

---

# 11. Das derzeit stärkste „Secret“-Arbeitsmodell

Wenn man Baumanns ungewöhnliche Sprache in Ingenieurbegriffe übersetzt, ist der am stärksten gestützte Kandidat **nicht**:

- Permanentmagnetenergie;
- Tesla-HF als notwendiger Kern;
- 50-Hz-Segmentmagie;
- Radium;
- ein gewöhnlicher Transformator.

Sondern:

> **phasengesteuertes Management des Ladungszustands einer selbstangeregten elektrostatischen Variable-C-Maschine — mit berührungslosen Pickups, Gitterfeldsteuerung, nichtlinearem Crystal-/Diodenpfad, getrenntem Drive- und Load-Speicher und zyklischer Regeneration des Hochspannungs-Bias.**

Kurz:

**regenerative electrostatic commutation / charge-state management**

Das erklärt sehr viel von Baumanns Sprache:

- „Wolke/Erde“ → Biasfelder;
- „Taster“ → Pickup;
- „ordnen“ → charge sorting;
- „im Takt“ → Kommutation;
- „langsam“ → RC-/Phasenfenster;
- „Gitterkondensator“ → Ladungspuffer;
- „Spannung aufrechterhalten“ → Regeneration;
- `crystal` → nichtlinearer Gate-Pfad.

Es erklärt **nicht automatisch** die behauptete Nettoenergie.

---

# 12. Mathematisches Minimalmodell für eine Testatika-Replik

Für `n` leitfähige/floating Knoten ist eine Kapazitätsmatrix geeigneter als ein einzelner Kondensator.

## 12.1 Knotenladungen

Für Knoten `i`:

`Q_i = sum_j C_ij(theta) * (V_i - V_j)`

Da der Rotor rotiert, ist `C_ij` winkelabhängig.

## 12.2 Strom

`I_i = dQ_i/dt`

Damit entstehen zwei Beiträge:

1. Spannungsänderung bei konstanter Geometrie;
2. Geometrieänderung bei konstantem Potential.

Der zweite Beitrag ist das Herz einer Variable-C-Maschine.

## 12.3 Elektrostatisches Drehmoment

Für eine vereinfachte feste Spannungsbedingung gilt qualitativ:

`tau_e ~ 1/2 * V^2 * dC/dtheta`

Bei mehreren Knoten muss die komplette Matrix betrachtet werden.

### Konsequenz

Elektrodenwinkel und Ladungsphase entscheiden darüber, ob der Rotor:

- beschleunigt;
- gebremst;
- nahezu drehmomentfrei

wird.

## 12.4 Diode/Crystal

Mit einer Diode wird das System **stückweise nichtlinear**:

- Knoten ist zunächst floating;
- bei Schwellspannung leitet der Pfad;
- Ladung wird auf Speicher übertragen;
- danach sperrt der Pfad wieder.

Das ist genau die Art Mechanismus, die man sprachlich als „ordnet“ oder „hält im Takt“ beschreiben könnte.

## 12.5 Energiebilanz

Elektrische Speicherenergie:

`E_C = 1/2 C V^2`

Mechanische Leistung:

`P_mech = tau * omega`

Für eine belastbare Anomalie müsste gelten:

`E_out > E_mech,in + E_bias,in + E_aux,in + E_stored,initial - E_stored,final`

mit ausreichend kleiner Messunsicherheit und unabhängiger Replikation.

---

# 13. Warum „Last abnehmen ohne Rotorladung abzuziehen“ technisch interessant, aber nicht magisch ist

Eine späte Frolov-Kompilation schreibt Baumann die Aussage zu, Elektronen dürften niemals direkt von den Scheiben abgezogen werden. Die Primärprovenienz ist unklar; deshalb nur H2/I1.

Trotzdem ist das Konzept technisch sinnvoll:

1. Rotor bleibt Bias-/Feldquelle;
2. statische Gegenelektrode wird induktiv polarisiert;
3. Laststrom wird am Sekundärknoten entnommen;
4. Rotor wird nicht unmittelbar galvanisch entladen.

Das ähnelt einem Transformationsprinzip in elektrostatischer statt magnetischer Form.

### Aber

Bei echter Last entsteht nach Energieerhaltung eine Reaktionswirkung:

- veränderte Feldenergie;
- zusätzliches Drehmoment;
- zusätzlicher Bias-Nachladebedarf;
- oder Verbrauch einer externen Energiequelle.

Die entscheidende Messfrage lautet daher nicht „wird Rotorladung direkt abgezogen?“, sondern:

> **Wie verändert sich die vollständige Feld-/Mechanikenergiebilanz, wenn der Load-Bus belastet wird?**

---

# 14. Warum Baumanns „Teilchen richten“ nicht mit Maxwell-Dämon verwechselt werden darf

Die Vorstellung, zufällige thermische Teilchenbewegung einfach mit einer Diode zu gleichrichten, führt bei thermischem Gleichgewicht zum klassischen Brownian-ratchet-/Maxwell-Demon-Problem.

Ohne Nichtgleichgewicht kann daraus keine dauerhafte Nettoarbeit gewonnen werden.

Darum muss jedes reale `rectify random particles`-Modell eine Quelle identifizieren:

- mechanische Bewegung;
- externe Hochspannungs-Vorladung;
- atmosphärisches Feld;
- Temperaturgradient;
- ionisierende Entladung;
- Luftströmung;
- chemische Reaktion;
- Strahlung;
- gespeicherte Electret-Ladung;
- RF/EM-Einkopplung.

Solange keine solche Quelle quantitativ nachgewiesen ist, bleibt „Energie aus zufälligen Teilchen“ eine unvollständige Beschreibung.

---

# 15. Was wir jetzt tatsächlich „verstanden“ haben

## Mit relativ hoher Sicherheit

- Die Scheiben-/Tasterzone ist ein elektrostatisches Influence-/Variable-C-System.
- Nichtkontaktierende Pickups sind zentral.
- Der Rotorladungzustand und seine Phasenlage sind wichtiger als bloße Drehzahl.
- Perforierte Gitter sind funktionell relevant und nicht nur Dekoration.
- Feuchtigkeit verändert das Verhalten stark.
- Eine nichtlineare Gleichrichter-/Crystal-Funktion ist für den Takt/Kommutation plausibel.
- Speicher-/Gitterkondensatoren glätten und puffern.
- Das ursprüngliche Entwicklungsproblem war wahrscheinlich, **Hochspannung zyklisch aufrechtzuerhalten**, nicht bloß einmal zu erzeugen.

## Mit mittlerer Sicherheit

- getrennte Drive- und Load-Busse;
- der Rotor dient eher als Bias-/Feldmodulator als als direkt entladene Stromquelle;
- Crystal/Diode bewirkt phasenselektives Charge-Gating;
- größere Zusatzmodule dienen primär Impedanz-/Puls-/Ladungsumformung.

## Weiter ungeklärt

- exakte kleine Originalverdrahtung;
- exakter Crystal-Werkstoff;
- exakte Rotor-Drahtführung;
- Cu-vs.-Fe-Konflikt;
- Driving-/Collecting-Elektrodenzuordnung;
- ob und welche externe Umweltenergie überhaupt relevant ist;
- behaupteter hohe Ausgangsstrom;
- historischer kW-Claim.

---

# 16. Neue Hypothesenfamilie B — Baumann-Semantik → technische Hypothesen

| Code | Hypothese | Status | stärkster Test |
|---|---|---|---|
| B-H01 | `Taster` = kapazitiver Influenz-Pickup | stark | C(theta), pickup current |
| B-H02 | `ordnen` = polarity-selective charge routing | stark-mittel | Mehrkanal-U/I vs Rotorwinkel |
| B-H03 | `rectifying diode` = phasenselektiver Kommutator | mittel-stark | Diode offen/kurz/verschiedene Schwellen |
| B-H04 | slow/steady = RC-relaxation phase lock | mittel-stark | rpm sweep + phase measurement |
| B-H05 | grid essential due field/corona geometry | mittel-stark | blinded mesh-vs-foil |
| B-H06 | PMMA charge retention central | mittel | RH + surface-potential decay |
| B-H07 | Drive-Bus und Load-Bus getrennt | mittel | node mapping / load perturbation |
| B-H08 | Rotor bleibt Biasquelle statt direkter output source | mittel | rotor potential under load |
| B-H09 | Crystal = threshold charge valve | mittel | I-V + phase-resolved current |
| B-H10 | top/side stages are pulsed impedance conversion | mittel-low | impedance/oscilloscope mapping |
| B-H11 | random particles = atmospheric ions | low-mittel | ion counter + enclosure + filtered gas |
| B-H12 | east-west effect genuine | low | randomized orientation experiment |
| B-H13 | permanent magnets fundamental energy source | sehr niedrig/rejected | compare with no-magnet small variant |
| B-H14 | intentional Tesla/HF core on small machine | niedrig | no primary support |
| B-H15 | equilibrium thermal fluctuations supply net work | rejected absent non-equilibrium source | calorimetric closed test |

---

# 17. Neue Experimente mit höchstem Informationsgewinn

## X1 — Phasenaufgelöste Node Map

Ziel:

- Rotorwinkel als Master-Zeitbasis;
- Spannung jedes Pickups;
- Strom in jeden Speicher;
- Crystal-Leitphase;
- Torque gleichzeitig.

Ergebnis soll eine `charge-state map` über 360° liefern.

---

## X2 — „Crystal hält im Takt“-Falsifikation

Varianten:

- Crystal-Pfad offen;
- kurz;
- normale Diode;
- verschiedene Schwellspannungen;
- bidirektionale symmetrische Begrenzung.

Messen:

- Startfähigkeit;
- stabile rpm;
- Torque;
- Charge-Bus;
- Load-Bus.

Wenn keinerlei phasenabhängiger Unterschied entsteht, wird B-H03 geschwächt.

---

## X3 — Grid vs Foil

Bereits als V3-Forschungszweig vorbereitet.

Kontrollieren:

- gleiche Außenkontur;
- gleiche projizierte Fläche soweit möglich;
- identischer Abstand;
- identisches Material;
- Blind-/Randomisierung.

Messen:

- Kapazität;
- Leckstrom;
- Corona-Onset;
- Ionenstrom;
- Torque;
- Charge per cycle.

---

## X4 — Feuchte-Matrix

PMMA bei:

- 10 % RH;
- 20 %;
- 40 %;
- 60 %;
- 80 %.

Messen:

- Surface Potential Decay;
- C(theta);
- Corona;
- Rotor torque;
- leakage.

---

## X5 — Load-Reaction-Test

Kernfrage:

> Wird eine reale Belastung als zusätzliches Bremsmoment oder zusätzlicher Bias-Nachladebedarf sichtbar?

Messung:

- offene Last;
- mehrere ohmsche Lasten;
- Torque und rpm geregelt;
- alle Busenergien.

Das ist entscheidender als jede Leerlaufspannung.

---

## X6 — Shield-Plate-Test

Marinovs direkte Beobachtung:

- große Metallplatte hinter kleiner Maschine → Rotation und Restdrehmoment verschwanden.

Varianten:

- floating;
- geerdet;
- über R;
- über C;
- verschiedene Distanz.

Wenn Effekt mit C(theta) korreliert, spricht das stark für Feldrandbedingungen statt exotische Magnetphysik.

---

## X7 — Ionisierungstest

Wenn Baumanns `Teilchen` Luftionen meint:

Vergleich:

- normale Luft;
- HEPA/ionengefilterte Luft;
- definierte Ionisation;
- geschirmtes Gehäuse;
- gleiche Feuchte.

Messen:

- Luftionenkonzentration;
- Corona current;
- Output charge per cycle.

---

# 18. Quellen, die NICHT vermischt werden dürfen

## Baumann

- Principle-/Linden-Berichte;
- kurze ihm zugeschriebene Antworten;
- Wolke/Erde;
- Mesh statt Folie;
- `crystal` via Marinov.

## Methernitha institutionell

- offizieller Film/Webtext;
- `Taster`, Gitter, Diode, slow/steady, Gitterkondensator.

## Cathomen

- Werkstatt-Amateurvideo;
- 100 kV;
- Kapazität erhöhen;
- Magnete/Spulen;
- Synchronfühler;
- Schallplatten-Ursprung;
- Spannung aufrechterhalten.

## Marinov

- direkte kleine-Maschinen-Beobachtungen;
- keine Bürsten;
- Pot-Innenleben;
- seine eigene Motor+Generator-Theorie;
- Zwei-Bus-Hypothese.

## Potter/Kelly/Frolov

- Rekonstruktions- oder Sekundärtheorien;
- nicht zu Baumann-Primärwissen hochstufen.

---

# 19. Besonders problematische spätere Baumann-Zuschreibungen

## 19.1 „Elektronen niemals von Scheiben abziehen“

Quelle derzeit nur späte Frolov-Kompilation.

**Status:** H2/I1.

Technisch interessant, aber nicht primär bestätigt.

## 19.2 „Jede Lamelle über 1-kΩ-Widerstand mit Nachbarn verbunden“

Ebenfalls späte/sekundäre Quelle.

**Status:** H2/I1.

Nicht in Baseline-CAD übernehmen, bevor Originalquelle identifiziert ist.

## 19.3 „Maschinen gewinnen Elektrizität aus Luft“

Sekundär Baumann zugeschrieben.

Kann bedeuten:

- atmosphärische Ionen;
- elektrostatische Feldumgebung;
- philosophische Kurzform.

Nicht als nachgewiesene Energiequelle behandeln.

---

# 20. Wissenschaftliche Vergleichsquellen

## 20.1 Wommelsdorf — Gegenrotation und eingebettete Sektoren

Patent:

`https://patents.google.com/patent/US883846A/en`

US883846A beschreibt historische multiple Influence-/Condenser-Maschinen mit gegensinnig rotierenden Platten und in isolierendem Material eingebetteten Sektoren.

Bedeutung:

- Gegenrotation ist konventioneller Stand der historischen Elektrostatik;
- eingebettete Leiter sind ebenfalls bekannt;
- hohe Potentiale allein sind keine Anomalie.

## 20.2 PMMA

DOI `10.1016/S0304-3886(98)00023-0`

Relative Feuchte beeinflusst Ladungsspeicherung stark.

## 20.3 Grid-corona

DOI `10.1016/j.elstat.2019.103367`

Gittergeometrie beeinflusst Corona und Stromverteilung deutlich.

## 20.4 Humidity-corona

DOI `10.1016/0304-3886(95)00009-Y`

Feuchte, Gitterpotential und Gitterposition beeinflussen Corona-Modi.

---

# 21. Zusammenführung: die Sprache als Blockdiagramm

```text
        START / PRIMING
             |
             v
  [charged segmented rotor]
             |
             | C(theta), influence
             v
 [grid / Taster pickup nodes]
             |
             | "ordnen"
             v
 [crystal / diode phase gate]
        /             \
       /               \
      v                 v
[HV DRIVE BUS]      [LOAD/STORE BUS]
      |                 |
      | electrostatic   | grid capacitors
      | torque          | smoothing
      v                 v
    ROTOR  <----- regeneration     DC LOAD

larger machines may insert additional pulsed capacitive/inductive
impedance-conversion stages between pickup/gate and load bus.
```

Dieses Blockdiagramm ist **kein Originalschaltplan**, sondern die derzeit beste technische Übersetzung des quellenübergreifenden Narrativs.

---

# 22. Was an der Energieseite weiterhin fehlt

Selbst wenn das gesamte oben beschriebene Charge-Management korrekt ist, bleibt die Kernfrage:

> Woher kommt unter Last die Energie, die pro Zyklus in den Load-Bus übertragen wird?

Mögliche konventionelle Quellen müssen einzeln bilanziert werden:

1. mechanische Arbeit der Rotoren;
2. gespeicherte Anfangsladung;
3. externe Biasquelle;
4. atmosphärisches elektrisches Feld;
5. Corona-/Ionisationsquelle;
6. EM/RF-Kopplung;
7. Temperatur-/Feuchtegradient;
8. chemische/Materialeffekte.

Die historische Dokumentation schließt diese Möglichkeiten nicht kontrolliert aus.

### Warum die sichtbaren Scheiben kaum selbst kW mechanisch liefern

Bei 3 kW und 60 rpm wären ungefähr 477 N·m erforderlich; bei 15 rpm ungefähr 1910 N·m.

Das passt nicht zu einem leichten Plexiglasrotor als unauffälligem alleinigen mechanischen Energiepfad.

Daher gilt:

- wenn die kW-Claims stimmen, ist ein zusätzlicher Energiepfad nötig;
- wenn kein solcher Pfad existiert, sind die kW-Claims/Messungen falsch oder unvollständig.

---

# 23. Forschungsurteil zur Frage „Verstehen wir Baumann jetzt?“

## Ja — auf Funktionsblockebene deutlich besser

Die scheinbar fremde Sprache lässt sich größtenteils in bekannte elektrostatische Begriffe übersetzen:

- Feldreservoir;
- variable Kapazität;
- Influence pickup;
- floating nodes;
- polarity routing;
- nonlinear rectification;
- phase commutation;
- charge pump;
- storage buffer;
- impedance conversion.

## Nein — auf Originalschaltungs- und Energiequellenebene noch nicht

Uns fehlen weiterhin:

- exakte Verdrahtung;
- Crystal-I-V-Charakteristik;
- exakte Rotor-Routing-Geometrie;
- vollständige Node Map;
- belastbare kW-Energiebilanz.

### Deshalb lautet die präziseste aktuelle Aussage

> **Baumanns Erklärungen wirken weniger mysteriös, wenn man sie als phasenabhängiges elektrostatisches Charge-Management liest. Das erklärt die sichtbaren Komponenten und einen möglichen Selbstanregungs-/Motorzyklus wesentlich besser als Tesla-/Magnetenergie-Theorien. Es liefert aber noch keine Erklärung für einen Nettoenergieüberschuss.**

---

# 24. Quellenregister für dieses Dokument

## Primär-/nahe Quellen

- Methernitha technical information (archived):  
  `https://rimstar.org/sdenergy/testa/methernitha_testatika_technical_info.htm`
- Holzherr 1999 report:  
  `https://rimstar.org/sdenergy/testa/report99.htm`
- Holzherr/Methernitha news archive:  
  `https://www.novakcorp.com/energy/experiments/tesnews.htm`
- Linden experiment, explicit second-hand warning:  
  `https://rimstar.org/sdenergy/testa/lindenexp.htm`
- Stefan Marinov, *The Thorny Way of Truth, Part V* (1989):  
  Internet Archive identifier `thornywayoftruthpart5maririch`

## Werkstatt-/Sekundärquellen

- Cathomen amateur-video transcript mirror:  
  `https://www.allmystery.de/themen/gw11473-5`
- Marinov pot statement archive:  
  `https://rimstar.org/sdenergy/testa/potstheory1.htm`
- Mike Watson recollection:  
  `https://www.novakcorp.com/energy/experiments/bswiss.htm`
- Frolov late compilation — low provenance for Baumann quotes:  
  `https://www.researchgate.net/publication/356969854_New_Sources_of_Energy_English_version`

## Physikalische Kontrollliteratur

- Heinrich Wommelsdorf, US883846A:  
  `https://patents.google.com/patent/US883846A/en`
- PMMA charge storage / humidity:  
  DOI `10.1016/S0304-3886(98)00023-0`
- grid geometry / corona:  
  DOI `10.1016/j.elstat.2019.103367`
- humidity / three-electrode corona:  
  DOI `10.1016/0304-3886(95)00009-Y`

---

# 25. Regeln für künftige Quellenfunde zu Baumann

Jede neu gefundene Baumann-Aussage muss mit diesen Feldern gespeichert werden:

```yaml
statement_id: B-...
speaker: Paul Baumann|Methernitha|Luzi Cathomen|other
transmission: direct_audio|direct_witness|letter|second_hand|later_compilation
source_url: ...
date: ...
machine_id: M0|M2|M5|M6|...
original_language: de|en|...
short_source_wording: ...
paraphrase: ...
conventional_translation: ...
confidence: high|medium|low
conflicts: [...]
cad_implication: ...
experiment_implication: ...
```

**Keine spätere technische Interpretation darf in `short_source_wording` hineingeschrieben werden.**

---

# 26. Offene Suchaufträge

1. Vollständige Originalaufnahme/Transkription des 1989-Methernitha-Films in deutscher Sprache sichern.
2. Originale deutsche Methernitha-Webbeschreibung aus Webarchiv finden, um `Taster`, `ordnen`, `Gitterkondensator` ohne Übersetzungszwischenstufe zu zitieren.
3. Marinov Part V + VI/VII nach **allen direkten Baumann-Dialogen** seitenweise neu indexieren.
4. Vollständige Marinov-Briefe 1989–1991 sichern, insbesondere `crystal` und Pot-Korrektur.
5. Hans-Weber-/Inge-Schneider-Bericht im frühesten Druck identifizieren.
6. Originalquelle hinter Frolovs `never withdraw electrons` und `1 kΩ` finden; bis dahin H2.
7. Originalquelle hinter der Partikel-/`straightening`-Formulierung suchen und mit Linden-Bericht abgleichen.
8. Novaretti-Buch auf unveröffentlichte direkte Baumann-Zitate prüfen.

---

# 27. Endstatus

**Quellenkritischer Kern:**

- Ein direktes Marinov-Zitat „Baumanns Erklärung war wie eine unbekannte Sprache“ ist nicht belegt.
- Marinovs Nichtverstehen ist belegt.
- Holzherrs Schwierigkeit mit Baumanns nicht-wissenschaftlicher Sprache ist belegt.
- Methernitha sagt selbst, dass sie eigene Begriffe verwendet.
- Baumanns/Methernithas Erklärsprache lässt sich zu einem erheblichen Teil als **elektrostatisches, phasenabhängiges Ladungsmanagement** übersetzen.
- Das erklärt noch **keinen** verifizierten Energieüberschuss.

**Der derzeit wichtigste konstruktive Suchpunkt ist daher nicht „welcher geheime Magnet?“ sondern:**

> **Wie sind Rotorwinkel, Gitter/Taster, Crystal-/Diodenleitphase, Drive-Bus, Load-Bus und Ladungsrückführung exakt miteinander verschaltet und zeitlich phasenbezogen?**

Das ist die Frage, die eine Replikation jetzt experimentell beantworten muss.

# V6-Ergänzung: Hartmann ist nicht Baumann

Der Hartmann-/Overunity-Audit liefert eine wichtige zusätzliche Sprechertrennung:

- Hartmanns **Juni-2000-Electret-/Influenzmodell** ist eine technische Interpretation Hartmanns;
- Hartmanns spätere **Radioaktivitäts-/Beta-Elektronen-Hypothese** ist ebenfalls Hartmanns eigene spätere Theorie;
- Hartmanns 2008er `negative resistance`-Aussage darf nicht rückwirkend als Baumanns Erklärung gelesen werden;
- der von Holzherr berichtete Satz, Baumann habe **Radiumchlorid** als Energiequelle verneint, bleibt als zeitnaher Augenzeugenbericht erhalten;
- eine sekundäre Rimstar-Zuschreibung, Hartmann sei gesagt worden `the secret is in the crystals`, bleibt offen, solange kein originales Hartmann-Besuchsprotokoll gefunden ist.

Für die Entschlüsselung von Baumanns Begriffen darf daher nur dort Hartmann herangezogen werden, wo er eine **engineering translation** anbietet, nicht als Ersatz für Baumann-Wortlaut. Besonders nützlich ist 2000 die Deutung `Taster -> non-contact influence pickup` und `grid/electret -> charge-state/field-forming structure`; die behauptete Energiequelle bleibt separat offen.
