# M6 V2 — evidenzbasierte Verdrahtung und funktionsfähige Laborvarianten

## Status

Dies ist der kanonische elektrische Begleitplan für den real-material M6-V2-Bausatz.

Die große/ca. 500-mm-Maschinenfamilie ist mechanisch und baugruppenmäßig deutlich besser belegt als ihr vollständiger Stromlauf. Deshalb gilt:

> **Jeder historisch unsichere Knoten bleibt einzeln herausgeführt. Verdrahtung entsteht über einen dokumentierten Patchplan, nicht versteckt im Sockel.**

SVG-Übersicht:
`diagrams/M6_V2_EVIDENCE_WIRING.svg`

---

# 1. Quellenstarke Baugruppen

## Statoren / nichtkontaktierende Elektroden

- `A1..A8` — Frontstatoren;
- `A9..A14` — Rückstatoren;
- jeder einzeln terminiert;
- keine automatische +/- Gruppierung.

## Linker Zylinder

- `L-OG` — outer grid;
- `L-MG` — middle grid;
- `L-IG` — inner grid;
- `L-W1A`, `L-W1B` — Wicklungslage/Leiter 1 Anfang/Ende;
- `L-W2A`, `L-W2B` — Wicklungslage/Leiter 2 Anfang/Ende, soweit physisch separat ausgeführt;
- `L-MT` — zentrale Magnet-/Rohrreferenz;
- `L-OUT` — oberer Metallring/Abnahmekandidat.

## Rechter Zylinder

Analog:

- `R-OG`, `R-MG`, `R-IG`;
- `R-W1A/B`, `R-W2A/B`;
- `R-MT`;
- `R-OUT`.

## Hufeisenmodule

Jede reale Wicklung wird an beiden Enden separat geführt. Keine automatische Serien-/Parallel-/Bifilarverschaltung.

## Kondensator-/Top-Modul

- `CAP7-A/B`;
- `CAP8-A/B`;
- `TOP-C1/C2`;
- `TOP-X1..X3` bzw. zusätzliche Steckknoten.

Die obere Cathomen-`Verstärkungs-/Kapazitätsstufe` bleibt ein austauschbarer Modulplatz. **Es existiert keine hinreichend belegte interne Originalschaltung.**

---

# 2. M6-W0 — OPEN / vollständige Charakterisierung

```text
A1..A14        OPEN, individually measurable
L/R-OG/MG/IG  OPEN
L/R-W*         OPEN, four-wire characterization where available
L/R-MT         OPEN / insulated
L/R-OUT        OPEN
horseshoe coils OPEN
CAP7/CAP8      discharged and OPEN
TOP-C*         OPEN
TOP-X*         EMPTY/OPEN
LAB MOTOR      disconnected except mechanical qualification
BIAS           disconnected
LOAD           disconnected
```

### Pflichtmessungen

1. Isolationsmatrix;
2. Kapazitätsmatrix der drei Gitter je Zylinder;
3. Kopplung jedes Stators zu jedem Rotorkörper/Zylinderknoten;
4. `C(theta)` jedes relevanten Pfads;
5. Wicklungs-R, L und gegenseitige Induktivität;
6. Magnet-/Dummy-Kontrolle;
7. Rotorwinkel-zu-Statorsignal-Phasenkarte;
8. Leckstrom vs RH;
9. Oberflächenpotential der PMMA-/Lamellenbaugruppen;
10. magnetischer Restfluss der Lamellenvarianten vor/nach Versuch.

---

# 3. M6-W1 — funktionsfähiger Drei-Gitter-/Variable-Capacitance-Test

**Zweck:** Die quellenstarke drei-Gitter-Zylinderstruktur elektrisch real betreiben und überprüfen, ob die rotierende Segment-/Statorgeometrie reproduzierbare pulsierende Potentialunterschiede an den Gittern erzeugt.

## Feldseite

```text
commercial isolated current-limited electrostatic bias
     +BIAS -- Rlim+ -- selected phase-qualified stator/drive bus D+
     -BIAS -- Rlim- -- selected phase-qualified stator/drive bus D-
```

Die Zuordnung `A1..A14 -> D+/D-/OPEN` erfolgt erst nach der W0-Phasenkarte.

## Zylinder

Startzustand:

```text
L-OG -> guarded FIELD-L node
R-OG -> guarded FIELD-R node
L-MG/L-IG -> separate sense nodes
R-MG/R-IG -> separate sense nodes
all winding nodes -> OPEN
magnet tubes -> OPEN
```

Alle sechs Gitter bleiben separat messbar. Erst nach der Signalaufnahme werden passive Patchvarianten eingesetzt.

## Passive Abnahme

Ein HV-geeigneter, potentialfreier Gleichrichter wird zwischen dem gewählten linken und rechten Sense-Knoten geschaltet:

```text
SENSE-L ----[ isolated HV rectifier ]---- +STORE
SENSE-R ----[                       ]---- -STORE
+STORE ------------- Cstore ------------- -STORE
+STORE/-STORE ------- defined bleeder network ------- guarded reference
```

### Erfolgskriterium

- reproduzierbare, winkel-/drehzahlabhängige Signale;
- definierte Ladung auf `Cstore` oberhalb der Mess-/Leckgrenze;
- reproduzierbare Änderung bei Grid-/Mesh-/Lamellen-A/B-Versuchen.

Das ist **kein** Beleg eines autonomen Energieüberschusses.

---

# 4. M6-W2 — Hauser-kompatible Anschlussfamilie

Hausers Besucherrekonstruktion stützt grob:

- horizontale Elektroden übertragen hohe Spannung in Richtung `pos. 6`/Zylinder;
- mehrere leitfähige Schichten sind intern verbunden;
- Verbindungen existieren auch zu weiteren Baugruppen;
- die nutzbare Abnahme erscheint in seiner Zeichnung an zwei Metallringen oben an den Zylindern.

Die genaue Knotenkarte fehlt. Daher wird diese Familie als Patchvariante aufgebaut.

## Minimalvariante `M6-W2A`

```text
phase-qualified horizontal stator group LEFT  -> L-OG through Rlim
phase-qualified horizontal stator group RIGHT -> R-OG through Rlim
L-MG, L-IG -> sense only
R-MG, R-IG -> sense only
L/R-W1/W2 -> OPEN
L/R-MT -> OPEN
L-OUT/R-OUT -> differential output measurement only
TOP/CAP/HM -> OPEN
```

## Erweiterung `M6-W2B`

Nur wenn W2A eine reproduzierbare Kopplung zeigt:

- `L-OUT/R-OUT` über passive HV-Gleichrichtung an einen bekannten Speicher;
- jeweils **eine** weitere Hauser-Baugruppe pro Versuch zuschalten;
- nie mehrere unbekannte Module gleichzeitig aktivieren.

Reihenfolge:

1. CAP7;
2. CAP8;
3. ein Horseshoe-Wicklungsmodul;
4. Zylinder-Wicklung;
5. Top-Modul-Surrogat.

So bleibt kausal feststellbar, welches Modul ein Signal verändert.

---

# 5. M6-W3 — Rimstar-`DC from the Pots` Reproduktionszweig

Dieser Zweig ist **kein historischer Originalanspruch**, aber eine publizierte reale Testtopologie, die gepulste Potentialunterschiede an drei konzentrischen Zylindern untersucht.

Prinzip:

```text
LEFT POT/CYLINDER:
  outer grid + center field electrode -> field/excitation pair
  middle grid -> OUTPUT-L
  inner grid -> floating/sense

RIGHT POT/CYLINDER:
  outer grid + center field electrode -> field/excitation pair
  inner grid -> OUTPUT-R
  middle grid -> floating/sense

OUTPUT-L <---- measured differential/load ----> OUTPUT-R
```

Für M6 V2 wird die `center field electrode` zunächst durch einen **separat definierten Zylinder-/Wicklungsknoten** ersetzt; Magnettube und Wicklungen dürfen nicht unbemerkt zusammengelegt werden.

Rimstar berichtet messbare gepulste DC-Verhältnisse, weist aber ausdrücklich darauf hin, dass sein Versuch **keinen excess-energy output** demonstriert.

---

# 6. M6-W4 — Lamellen-/Stator-Materialmatrix

M6-W4 ändert **keine Verdrahtung**, sondern ausschließlich einen dokumentierten Lamellen-/Elektrodenparameter aus `LAMELLA_TEST_MATRIX.tsv`.

Konstant halten:

- Drehzahl;
- Rotor-/Statorabstand;
- aktive Fläche;
- Loch-/Mesh-Geometrie, sofern nicht gerade diese Variable getestet wird;
- Bias;
- Feuchte/Temperatur;
- Verdrahtung und Messgeräte;
- Auswuchtung.

Nur eine Variable je A/B-Test:

- Legierung;
- Magnetisierungszustand;
- Lochblech vs Vollfolie;
- Loch-/Meshpitch;
- Oberflächenzustand/Beschichtung.

---

# 7. M6-W5 — Cathomen-Topmodul als BLACK-BOX-Schnittstelle

Das Amateurvideo liefert direkte Evidenz dafür, dass Cathomen bei einer oberen Stufe die genaue Funktion **nicht offenlegte**. Er nennt Magnete und weitere Dinge/Spulen, spricht von Verstärkung/`Kapazität erhöhen`, verweigert aber die Details.

Darum wird die Stufe nicht mit Potter/Kelly-Inhalten gefüllt.

## Schnittstelle

```text
TOP-IN+ / TOP-IN-
TOP-OUT+ / TOP-OUT-
TOP-AUX1 / TOP-AUX2
optional MAGNET-MEAS / SHIELD
```

Baseline:

`ALL OPEN`

Zulässige Surrogate werden als separate Boxen geprüft:

- passive RLC-Netzwerke;
- kommerzieller HV-Gleichrichter;
- definierter Transformator nur bei AC-Test;
- definierte Magnet-/Spulen-Kopplung;
- passive Funkenstrecke nur in gekapseltem, energielimitiertem Prüfsystem.

Keines davon heißt `Methernitha secret` oder `original amplifier`.

---

# 8. Kelly-/Potter-Vollschaltung bleibt Vergleich, nicht Baseline

Die veröffentlichten `Full Circuit`-/Kelly-Pläne sind nützlich, um Prüfpunkte und mögliche Funktionsklassen zu sammeln. Sie werden aber nicht hart verdrahtet, weil:

- viele Details nicht durch Hauser/Marinov/Cathomen bestätigt sind;
- Don Kelly frühe Magnet-/Wicklungsdarstellungen später selbst korrigierte;
- Potter ausdrücklich back-engineert und zahlreiche innere Funktionen vermutet;
- Hauser seine elektrische Verbindungskarte als unvollständig kennzeichnet.

---

# 9. Impuls-/Synchron-Schnittstelle

Cathomen sagt im Werkstattdialog, an einer unfertigen Maschine müsse noch ein **Fühler für die Impulse** angebracht werden, damit die Frequenz gleich bleibe. Der Interviewer fasst dies als Synchronsteuerung zusammen, Cathomen bestätigt die Kontroll-/Synchronfunktion.

Daher erhält M6 V2 eine **Messschnittstelle**, aber keine erfundene historische Regelung:

- optischer/magnetischer Drehzahlsensor als Laborinstrument;
- `SYNC-PULSE` isolierter Messausgang;
- kein versteckter Motorregler im historischen Strompfad;
- falls ein Labormotor verwendet wird, wird dessen Regler elektrisch und energetisch separat bilanziert.

---

# 10. Messartefakt-Sperre

Floating-HV-Schaltungen dürfen nicht mit ungeprüfter geerdeter Scope-Masse gemessen werden.

Pflicht:

- HV-Differentialsonde oder geeignetes Elektrometer;
- dokumentierte Eingangskapazität;
- dokumentierter Massepfad;
- zweite Messmethode für überraschende Signale;
- Dummy-/Short-/Open-Kontrollen;
- simultane Messung aller externen Energiequellen.

---

# 11. Energiebilanz

Vor jeder Aussage über Anomalie oder Selbstlauf:

1. externe Motorenergie integrieren;
2. externe Biasenergie integrieren;
3. Anfangs-/Endenergie sämtlicher Kondensatoren erfassen;
4. mechanische Rotationsenergie berücksichtigen;
5. reale Lastenergie synchron messen;
6. Leck-/Corona-/Funkenverluste dokumentieren;
7. Messunsicherheit angeben;
8. aktive Module durch Dummys ersetzen und wiederholen.

Nur eine reproduzierbare, geschlossene Bilanz kann eine weitergehende Behauptung tragen.
