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

## Stufe 4 — externer Elektrostatik-Motortest

- nur mit kommerzieller/gekapselter, strombegrenzter Lehr-/Labor-Elektrostatikquelle;
- zunächst 2 Elektroden, danach 4;
- Winkel 0°, 15°, 30°, 45° systematisch vergleichen;
- Drehmoment mit Kraft-/Drehmomentsensor bestimmen;
- Rotorwinkel synchron erfassen.

Ziel: `tau(theta)` und die Phasenlage des elektrostatischen Motorzyklus bestimmen.

## Stufe 5 — Pots

- Kapazität und Verlustfaktor jedes Pots messen;
- Außen-Gitter / Innen-Spirale getrennt dokumentieren;
- Impedanz über Frequenz bei kleinen Testsignalen;
- Leakage und dielektrische Relaxation;
- keine Tesla-Funktion voraussetzen.

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

**Kein Selbstlauf-/Overunity-Schluss aus Nachlauf, Feldspeicherung, hoher Leerlaufspannung oder kurzen Lastimpulsen.**
