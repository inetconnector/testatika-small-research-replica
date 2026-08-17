# Experimentplan V3 — Charge-State / Primärquellen-Tests

Der Plan prüft die in [`baumann-language-decoding.md`](baumann-language-decoding.md) übersetzten Funktionshypothesen. Er beginnt mit energiearmen Teiltests; ein behaupteter Selbstlauf ist **nicht** Voraussetzung.

Die neue Primärscanlage hat zwei Experimente hochpriorisiert: **floating Rotordrähte** als Kleinmaschinen-Baseline und eine **historisch zweipolige Pot-Schnittstelle**.

## Stufe 0 — Mechanik

- Auslaufzeit ohne Elektroden/Pots.
- Lagerreibung und Scheibenschlag.
- 20/24/25-Sektorrotoren vergleichen.
- Rotorträgheit bestimmen.
- Labormotor/Kupplung: Reibung mit Drive OFF bestimmen; vollständige mechanische Abkopplung für Selbstrotationsversuche dokumentieren.

## Stufe 1 — C(θ), Rotor-Routing und elektrische Sektortopologie

- Kapazität zwischen einzelnen Elektroden und Rotor als Funktion des Winkels.
- R0/R1/R2/R3/R4-Drahtführung vergleichen.
- Vorder-/Rückseite getrennt messen.
- rückwärtige Metallplatte mit dem Experiment-Jig annähern.
- Shield floating / geerdet / R-gekoppelt / C-gekoppelt vergleichen.
- geometriegleiche nichtleitende Platte als Kontrolle; Abstand und Plattenfläche systematisch variieren.
- Der Metallplatten-Stopp ist nun als direkte Marinov-Beobachtung eingestuft; seine Ursache bleibt offen.

Ziel: `Taster` als kapazitiven/Influenz-Pickup und den Metallplatten-Stoppversuch quantitativ prüfen.

### Stufe 1a — E0 floating sectors gegen E1 Sekundär-Ring

Direkter Marinov-Scan `SMwebL1.jpg`: die Drähte auf der beschriebenen Kleinmaschinen-Scheibe seien **`connected to nothing`**.

Daher ist:

- **E0 = bevorzugte historische Kleinmaschinen-Baseline:** jedes Segment elektrisch floating;
- **E1 = Sekundär-Kontrolle:** Nachbarsegmente über 1 kΩ verbunden, ausschließlich um die späte Frolov-Zuschreibung zu falsifizieren/vergleichen.

E0/E1 müssen geometrisch identisch sein. Nur die elektrische Verbindung darf variieren.

Vor jedem Lauf:

- Isolation aller E0-Sektoren gegeneinander und gegen Welle/Hub dokumentieren;
- Widerstandsring E1 vollständig durchmessen;
- DC-Widerstand jedes Sektors erfassen.

Synchron messen:

- Sektorpotentiale, soweit berührungslos möglich;
- `C(theta)`;
- Pickup-Strom;
- Surface Potential;
- Torque;
- rpm;
- Ladungsrelaxation nach Stop.

Ein E1-Effekt wäre **kein Beweis**, dass E1 historisch original war; die Quellenlage bliebe separat zu bewerten.

### Stufe 1b — Hub-Arcs

`meth4.asf` stärkt die Interpretation zweier kupferfarbener räumlicher Bogenstücke am Hub.

Vergleich:

- Bögen leitend + floating;
- leitend + separat instrumentiert;
- dimensionierter nichtleitender Dummy;
- Bögen entfernt.

Messen:

- C zu Welle/Rotordrähten/Statoren;
- lokale Potentiale;
- Torque/RPM;
- Pickup-Strom.

Keine historische Verbindung zu einem anderen Knoten voraussetzen.

## Stufe 2 — Gitter vs. Vollfolie

Quellenhypothese: Baumann sagte laut Holzherr, Vollfolie statt Drahtgitter erzeuge im Principle Experiment nicht denselben Effekt.

A/B-Test:

- gleiche Außenkontur;
- gleicher Abstand;
- gleiches Metall soweit möglich;
- Gitter/Lochblech vs. Vollfolie;
- randomisierte Reihenfolge;
- Bedienerblindung, wo praktikabel.

Messen:

- Kapazität;
- Leckstrom;
- Corona-Onset;
- Ionenstrom;
- Surface Potential;
- Drehmoment;
- Ladung pro Zyklus.

### Stufe 2b — Layered outer panel

`meth4` zeigt den Kleinmaschinen-Außenpanel als sichtbare Mehrlagenstruktur.

Geometrie konstant halten und einzeln variieren:

- grober Lochträger;
- dunkles feines Inset-Gitter;
- längliches rötliches Leiter-/Rahmenelement;
- isolierende Rücklage;
- elektrische Verbindung des Edge-Elements offen/floating/definiert.

Ziel: sichtbare Schichtung von spekulativer Materialfunktion trennen.

## Stufe 3 — Feuchte / PMMA

Messpunkte z. B. 10 / 20 / 40 / 60 / 80 % RH bei kontrollierter Temperatur.

Messen:

- Surface Potential Decay;
- Leckstrom;
- C(θ);
- Corona;
- Rotor-Torque.

Ziel: Methernithas `dry air works better` gegen etablierte PMMA-/Coronaeffekte abgleichen.

### Stufe 3b — PMMA-Vorkonditionierung / Electret-Kontrolle

Archiv-/Kelly/Potter-Material enthält Electret- bzw. vorbeladene-Dielektrikum-Deutungen. Dies ist **kein historisch bestätigtes M2-Geheimnis**, aber eine sauber testbare Variable.

Vergleich bei identischer Geometrie:

- unbehandeltes PMMA;
- kontrolliert elektrostatisch vorkonditioniertes PMMA mit dokumentierter, energiearmer Laborprozedur;
- neutralisiertes/entladenes Kontrollstück;
- gleicher PMMA-Typ in unterschiedlichen Schnitt-/Herstellungsorientierungen, sofern aus dem Halbzeug nachvollziehbar.

Vor und nach jedem Lauf erfassen:

- räumliche Surface-Potential-Map;
- Abklingkurve des Oberflächenpotentials;
- Temperatur und RH;
- Leckstrom;
- C(θ);
- Corona-Onset;
- Startmoment und stationäres Torque.

Ziel: feststellen, ob ein langlebiger Dielektrikum-Ladungszustand die beobachtbaren Teilphänomene erklärt oder beeinflusst, **ohne** ihn als Energiequelle anzunehmen.

## Stufe 4 — externer Elektrostatik-Motortest

- nur mit kommerzieller/gekapselter, strombegrenzter Lehr-/Labor-Elektrostatikquelle;
- zunächst 2 Elektroden, danach 4;
- Winkel 0°, 15°, 30°, 45° systematisch vergleichen;
- Drehmoment mit Kraft-/Drehmomentsensor bestimmen;
- Rotorwinkel synchron erfassen.

### Drehzahl-Sweep nach erweitertem Quellenstand

Historische Berichte sind nicht einheitlich: Hauser/Cathomen nennen modellbezogen ungefähr 60 rpm, während Holzherr 1999 bei einer 50-cm-Demo ungefähr **15 rpm** beobachtete. Deshalb keine einzelne Soll-Drehzahl voraussetzen.

Empfohlene Sweep-Punkte für Vergleichstests, soweit mechanisch sicher:

`5 / 10 / 15 / 20 / 30 / 45 / 60 rpm`

Bei jedem Punkt synchron erfassen:

- rpm und Rotorwinkel;
- Torque;
- Knotenpotentiale;
- Gate-/Pickup-Strom;
- Leck-/Corona-Strom;
- Ladung pro Zyklus.

Ziel: RC-/Relaxations-/Phasenfenster gegen Drehzahl auflösen.

## Stufe 5 — M2-Pots

Primärquellenmodus pro Pot: **zwei externe Leitungen**.

Bauteilbasis:

- äußeres zylindrisches Gitter;
- Kunststoff-/PMMA-Isolation;
- zentrale Kupferspirale.

Pflichtmessungen:

- Kapazität und Verlustfaktor;
- externe Zweipol-Impedanz;
- Leakage und dielektrische Relaxation;
- intern, nur über versteckte Labortaps: Gitter/Spirale einzeln charakterisieren;
- keine Tesla-Funktion voraussetzen.

### Zweipolige Topologie-Matrix

Die historische Außenansicht bleibt zweipolig, während intern reversible Varianten geprüft werden:

- Gitter an Lead A / Spirale an Lead B;
- vertauschte Polarität/Zuordnung;
- eine Elektrode intern floating mit kapazitiver Kopplung;
- high-value leakage path;
- diode-gated internal path;
- disconnected control.

Zusätzliche Messterminals müssen während des historischen Zweipol-Laufs vollständig isoliert/entfernt sein.

### Großmaschinen-Kontrolle — 20-Lagen / Hauser-Zylinder

Getrennt als M6-Versuch, niemals M2-Pot nennen:

- 2 / 5 / 10 / 20 perforierte Elektrodenlagen;
- Hauser-Variante: 3 konzentrische Metallgitter + Acryl + optional Magnettube + bifilare Wicklung;
- identische Vergleichsmaße und vollständige Eingangs-/Speicherenergiebilanz.

Messen:

- C;
- ESR/Verlustfaktor;
- Leakage;
- Relaxation;
- Impulsantwort;
- Magnet/Wicklung A/B.

## Stufe 6 — Crystal-/Diode-Gate

Nur bei niedriger Testenergie:

- offen;
- kurz;
- passive Diode;
- Dioden mit unterschiedlichen Schwell-/Sperreigenschaften;
- antiparallele Diode;
- Widerstand;
- Kondensator;
- geeigneter Kristalldetektor.

Zeitgleich messen:

- Rotorwinkel;
- Spannung vor/nach Gate;
- Gate-Strom;
- Torque;
- Speicherladung;
- rpm.

Ziel: prüfen, ob eine nichtlineare Schwelle phasenselektive Kommutation erzeugt.

### Quellen-Trennung

Nicht still gleichsetzen:

- Marinov/`crystal`;
- Methernitha/`rectifying diode keeps cycles steady`;
- Hauser/M6a top crystals + rectifier interpretation;
- Holzherr/four-lead early top module.

### Vier-Terminal-Topmodul

Experimenteller Träger:

- alle Terminals offen;
- Zentralleiter separat / Wicklung separat;
- Wicklungsenden vertauscht;
- Zentralleiter floating / referenziert / kapazitiv gekoppelt;
- passive R/C/Diode-Kopplung zwischen beiden Zweipolen.

Jede Topologie erhält eine eindeutige Config-ID. Keine davon wird als `original crystal` bezeichnet.

## Stufe 7 — Phasenaufgelöste Node Map

Alle zugänglichen Knoten gegen Rotorwinkel erfassen:

- mögliche Driving-Elektroden;
- Collecting-Elektroden;
- beide sichtbaren Pot-Leads;
- versteckte Labortaps nur in expliziten Characterization-Runs;
- Crystal-Gate;
- Speicher-/Ausgangsknoten;
- Hub-Arcs, falls instrumentiert.

Ergebnisformat: 0–360° `charge-state map`.

Gesucht wird insbesondere:

- welche Knoten floating sind;
- wann Polarität wechselt;
- wann das Gate leitet;
- wann positives/negatives Torque entsteht.

## Stufe 8 — Zwei-Bus-Test

Arbeitshypothese nach Marinov:

- HV-/kleine-C-Driving-Bus;
- niedrigere-V-/größere-C-Load-/Storage-Bus.

Beide Busse getrennt instrumentieren.

Fragen:

1. Wird der Drive-Bus pro Zyklus regeneriert?
2. Wie viel Ladung geht in den Load-Bus?
3. Verändert Last den Drive-Bus?
4. Steigt unter Last mechanisches Bremsmoment oder Bias-Nachladestrom?

## Stufe 9 — Load-Reaction-Test

Offener Ausgang vs. definierte ohmsche Lasten.

Simultan messen:

- `V_load(t)`;
- `I_load(t)`;
- Torque;
- rpm;
- Bias-Eingangsleistung;
- Speicherenergie vorher/nachher.

Das ist der wichtigste Test der Hypothese, man könne Ladung am Sekundärknoten abnehmen, ohne den Rotor-Bias direkt zu entladen.

### Quellenmotivierter Instrumentierungsstandard

Holzherr berichtete bei der 50-cm-Demo keinen sichtbaren Drehzahlabfall unter Last, weist aber selbst darauf hin, dass die Aufmerksamkeit auf der Lampe/Last lag. Deshalb ist `kein sichtbarer rpm drop` **kein** ausreichender Befund.

Pflichtmessungen:

- optischer/encoderbasierter rpm-Verlauf mit ausreichend hoher Zeitauflösung;
- Torque oder Antriebsleistung synchron;
- Load-V/I synchron;
- initiale/finale Speicherenergie;
- Labormotor-Eingang falls gekoppelt;
- mindestens ein identischer Dummy-Lauf.

## Stufe 10 — Luftionen-Hypothese

Nur wenn messbare Hinweise auf Corona/Raumladung bestehen:

Vergleich:

- normale Luft;
- gefilterte Luft;
- definierte externe Ionisation bei streng bilanzierter Energie;
- identische Feuchte/Temperatur;
- ggf. geschirmtes Gehäuse.

Messen:

- Ionenkonzentration;
- Corona-Strom;
- Output charge/cycle;
- Torque.

Ziel: prüfen, ob Baumanns second-hand überlieferte `random particles` sinnvoll mit Luftionen identifiziert werden können.

## Stufe 11 — Ost-West-Startup und Post-Start-Reorientierung

Quellenstatus korrigiert: Die East-West-Anweisung ist **Baumann→Marinov SOURCE-STATED**, nicht bloß H2. Separat berichtet Marinov direkt, dass die laufende Kleinmaschine nach dem Start bewegt, gekippt und umorientiert werden konnte. Eine geomagnetische Ursache ist damit **nicht** belegt.

Startup-Test:

- Maschine auf Drehtisch;
- randomisierte Winkelstellungen 0–360°;
- dreiachsiges Magnetfeld loggen;
- Netz-/Gebäudefelder kontrollieren;
- gleiche Startenergie;
- Bediener möglichst blind.
- Startimpuls mechanisch quantifizieren/standardisieren.
- RH und Temperatur protokollieren; trockene/feuchte Bedingungen separat randomisieren.
- Anzahl identischer Startimpulse bis zum stabilen Lauf erfassen.

Post-Start-Test separat:

- erst bei definierter Referenzorientierung starten;
- nach stabilem Lauf die gesamte Maschine auf randomisierte Azimute/Neigungen bewegen;
- rpm, Torque, Surface Potential und Feldvektoren kontinuierlich loggen.

### Stufe 11b — Restart-Memory / Zustandsabhängigkeit

Marinov berichtet, dass zweite/dritte Starts nach dem Metallplatten-Stopp leichter waren. Daher vergleichen:

- definierte Ruhezeit ohne Entladung;
- kontrollierte Neutralisierung/Entladung;
- identische RH/Temperatur;
- Surface-Potential-Map vor/nach jedem Lauf;
- randomisierte Reihenfolge und gleicher mechanischer Startimpuls.

Ziel: persistente Dielektrikum-/Oberflächenladung, Feuchtehistorie und Bedienereffekt von einer echten Orientierungsabhängigkeit trennen.

## Stufe 12 — gekoppelte Forschungsvariante

Erst wenn Teilblöcke verstanden sind.

Bilanz:

`E_in = E_mech + E_bias + E_aux + E_stored_initial`

`E_out = integral(V_load * I_load dt) + E_stored_final`

Keine Aussage zu Energieüberschuss ohne Unsicherheitsrechnung und langen Lastlauf.

## Stufe 13 — unabhängige Replikation

- Protokoll vorher einfrieren;
- Rohdaten veröffentlichen;
- zweite Gruppe;
- andere Messgerätefamilie;
- Kalibrierung;
- Dummy-/Blindvarianten.

## Optische Quellenregel

Holzherr weist darauf hin, dass eine sehr dünne Schicht zwischen Plexiglasplatten durch Totalreflexion optisch kaum sichtbar sein kann. Daher gilt für Fotoanalyse:

> `not visible` ist bei transparenten Mehrschichtbauteilen **nicht** gleich `not present`.

Verdeckte Leiter-/Zwischenschicht-Hypothesen dürfen nur als reversible Varianten getestet werden und brauchen für eine historische Hochstufung zusätzliche Primärevidenz.

**Kein Selbstlauf-/Overunity-Schluss aus Nachlauf, Feldspeicherung, hoher Leerlaufspannung, Video-Metadaten oder kurzen Lastimpulsen.**
