# Experimentplan V3 — Charge-State / Baumann-Language Tests

Der Plan prüft die in [`baumann-language-decoding.md`](baumann-language-decoding.md) übersetzten Funktionshypothesen. Er beginnt mit energiearmen Teiltests; ein behaupteter Selbstlauf ist **nicht** Voraussetzung.

## Stufe 0 — Mechanik

- Auslaufzeit ohne Elektroden/Pots.
- Lagerreibung und Scheibenschlag.
- 20/24/25-Sektorrotoren vergleichen.
- Rotorträgheit bestimmen.

## Stufe 1 — C(θ) und Rotor-Routing

- Kapazität zwischen einzelnen Elektroden und Rotor als Funktion des Winkels.
- R0/R1/R2/R3/R4-Drahtführung vergleichen.
- Vorder-/Rückseite getrennt messen.
- rückwärtige Metallplatte mit dem Experiment-Jig annähern.
- Shield floating / geerdet / R-gekoppelt / C-gekoppelt vergleichen.

Ziel: `Taster` als kapazitiven/Influenz-Pickup und den Metallplatten-Stoppversuch quantitativ prüfen.

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

Historische Berichte sind nicht einheitlich: Cathomen nennt modellbezogen ungefähr 60 rpm, während Holzherr 1999 bei der 50-cm-Demo ungefähr **15 rpm** beobachtete. Deshalb keine einzelne Soll-Drehzahl voraussetzen.

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

## Stufe 5 — Pots

- Kapazität und Verlustfaktor jedes Pots messen;
- Außen-Gitter / Innen-Spirale getrennt dokumentieren;
- Impedanz über Frequenz bei kleinen Testsignalen;
- Leakage und dielektrische Relaxation;
- keine Tesla-Funktion voraussetzen.

### Großmaschinen-Kontrolle — 20-Lagen-Gitterkondensator

Holzherr überliefert für die große Maschine Baumanns Aussage, die großen Kondensatoren enthielten **20 Lagen perforiertes Blech**. Dies darf nicht auf M2 übertragen werden, ist aber als getrennte M6-Kontrollstruktur interessant.

Nur als eigenes Modell untersuchen:

- 2 / 5 / 10 / 20 gleichartige perforierte Elektrodenlagen;
- identischer Dielektrikumtyp und definierte Abstände;
- C, ESR/Verlustfaktor, Leakage, Relaxation und Impulsantwort.

Ziel: prüfen, ob die große Struktur als gewöhnliches multilayer capacitance / field-shaping network erklärbar ist.

## Stufe 6 — Crystal-/Diode-Gate

Nur bei niedriger Testenergie:

- offen;
- kurz;
- passive Diode;
- Dioden mit unterschiedlichen Schwell-/Sperreigenschaften;
- antiparallele Diode;
- Widerstand;
- geeigneter Kristalldetektor.

Zeitgleich messen:

- Rotorwinkel;
- Spannung vor/nach Gate;
- Gate-Strom;
- Torque;
- Speicherladung;
- rpm.

Ziel: die Methernitha-Aussage `rectifying diode keeps the cycles steady` als **phasenselektive Kommutation** prüfen.

### Vier-Terminal-Topmodul

Holzherr erinnerte beim frühen/originalen Modell eine grobe Spule um einen geraden Zentralleiter mit insgesamt **vier Leitungen**. Dies ist modellbezogen und keine gesicherte M2-Topologie.

Der experimentelle Topmodul-Träger soll deshalb vier isolierte Terminals anbieten. Bei niedriger Energie systematisch testen:

- alle Terminals offen;
- Zentralleiter separat / Wicklung separat;
- Wicklungsenden vertauscht;
- Zentralleiter floating / geerdet / kapazitiv gekoppelt;
- passive R/C/Diode-Kopplung zwischen den beiden Zweipolen.

Jede Topologie erhält eine eindeutige Config-ID. Keine davon wird als `original crystal` bezeichnet.

## Stufe 7 — Phasenaufgelöste Node Map

Alle zugänglichen Knoten gegen Rotorwinkel erfassen:

- mögliche Driving-Elektroden;
- Collecting-Elektroden;
- Pot außen/innen;
- Crystal-Gate;
- Speicher-/Ausgangsknoten.

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

## Stufe 11 — Ost-West-Test

Nur als H2-Prüfung:

- Maschine auf Drehtisch;
- randomisierte Winkelstellungen 0–360°;
- dreiachsiges Magnetfeld loggen;
- Netz-/Gebäudefelder kontrollieren;
- gleiche Startenergie;
- Bediener möglichst blind.

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

**Kein Selbstlauf-/Overunity-Schluss aus Nachlauf, Feldspeicherung, hoher Leerlaufspannung oder kurzen Lastimpulsen.**
