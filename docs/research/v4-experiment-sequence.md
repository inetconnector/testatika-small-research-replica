# V4 Inbetriebnahme- und Versuchsfolge

## Regel

Jeder Versuch beginnt von einer bekannten Konfiguration aus `v4-configurations.yaml`. Standard ist `M2-V4-B0`. Pro Lauf wird genau eine Variable geändert, außer ein vorab dokumentierter faktorieller Versuchsplan verlangt ausdrücklich mehrere Faktoren.

## Phase 0 — Wareneingang / Fertigungsprüfung

Vor Montage dokumentieren:

- Material und Abmessungen des Rotors;
- Drahtdurchmesser und Material;
- PMMA-/Acrylherkunft;
- Gittermaterial/-maschenweite;
- Magnetgeometrie und Feldstärke;
- reale Pot-Abmessungen;
- Crystal-Einsatz = `OPEN`.

Fotos und Messwerte mit Commit-SHA ablegen.

## Phase 1 — Mechanische Nullmessung

Konfiguration: `M2-V4-B0`, noch ohne nahe aktive Elektroden.

Messen:

- Rundlauf;
- Scheibenschlag;
- Lagerreibung;
- Auslaufzeit;
- statische/dynamische Unwucht;
- rpm-Sensor ohne elektrische Kopplung.

Erst danach Elektrodenabstände reduzieren.

## Phase 2 — Rotor-Isolationsmatrix

Pflicht vor jedem elektrischen Test:

- jeder Sektor gegen linken/rechten Nachbarn;
- stichprobenartig entfernte Sektoren gegeneinander;
- jeder Sektor gegen Welle/Hub;
- jeder Sektor gegen Hub-Bögen.

Erwartung der Baseline: offen/floating. Ein unbeabsichtigter Durchgang macht den Lauf ungültig.

## Phase 3 — Parasitische C(θ)-Map

Noch ohne aktive Kopplung:

- Rotorwinkel 0–360° als Mastervariable;
- Kapazität jedes zugänglichen Pickup-/Panel-Knotens gegen Rotor/Welle/benachbarte Knoten;
- beide Pots zunächst getrennt;
- Hub-Bögen floating;
- Crystal open.

Ziel: reale Kapazitätsmatrix statt einer geratenen Schaltung erfassen.

## Phase 4 — Hub-Bögen

Vergleich:

1. `M2-V4-B0` — leitfähige Bögen floating;
2. `M2-V4-ARCDUMMY` — geometrisch gleiche Isolator-Dummys;
3. `M2-V4-ARC0` — Bögen entfernt.

Messen:

- C(θ);
- Surface Potential;
- mechanisches Drehmoment/Drag;
- Pickup-Signal.

Damit wird erstmals geklärt, ob die video-identifizierten Bögen elektrisch relevant oder primär mechanisch/dekorativ sind.

## Phase 5 — Magnetkontrolle

Vergleich:

- reale Hufeisenmagnete;
- `M2-V4-MAG0` Dummy;
- bei Bedarf definierte umgekehrte Orientierung.

Nicht gleichzeitig Hub-Bögen, Rotorroute oder Crystal ändern.

Messen:

- 3-Achs-Magnetfeld;
- C(θ);
- Drehmoment;
- Pickup-Spannung;
- rpm bei identischer externer Anregung.

## Phase 6 — Pot-Charakterisierung isoliert

Jeden Pot einzeln charakterisieren:

- C;
- Verlustfaktor/ESR soweit messbar;
- Leakage;
- Entlade-/Relaxationskurve;
- Surface Potential;
- Abhängigkeit von RH/Temperatur.

Danach links/rechts vergleichen. Erst dann Pot-Verbindungen in die Maschinenmatrix aufnehmen.

## Phase 7 — Grid/Mesh vs. Folie

Mit identischer Geometrie und gleichem Abstand:

- Mesh/Lochblech;
- Vollfolie;
- isolierender Dummy.

Messen:

- C(θ);
- Corona-Onset bei kontrollierter, strombegrenzter Testquelle;
- Ionen-/Leckstrom;
- Pickup-Ladung pro Zyklus;
- Torque.

## Phase 8 — R0 gegen R4

Vergleich:

- `M2-V4-B0` R0;
- `M2-V4-R4`.

Alle anderen Eigenschaften identisch halten: 24 Cu-Sektoren, floating, gleiche Panels/Pots/Magnete/Crystal.

Ziel: Informationsgewinn über die historisch ungelöste through-disc-Geometrie ohne gleichzeitig die elektrische Topologie zu verändern.

## Phase 9 — Crystal-Blackbox

Ausgehend von Baseline:

- OPEN;
- definierter R;
- C;
- passive Diode;
- antiparallele Diode;
- historischer Kristalldetektor als Vergleich, wenn sicher verfügbar.

Rotorwinkel-synchron messen:

- Spannung an beiden Seiten des Blackbox-Einsatzes;
- Strom;
- Pot-/Pickup-Knoten;
- Torque;
- rpm.

Keine Variante wird als „Original-Crystal“ bezeichnet.

## Phase 10 — PMMA-Zustand / Feuchte

Vergleiche nur bei gleicher Geometrie:

- unbehandeltes PMMA;
- neutralisierte Kontrolle;
- dokumentiert vorkonditioniertes PMMA.

RH-Sweep gemäß Haupt-Experimentplan.

Pflicht: Konditionierungsenergie und Anfangsspeicherzustand vollständig bilanzieren.

## Phase 11 — erzwungener Drehzahl-Sweep

Externer Laborantrieb ist ausschließlich Messinstrumentierung.

Sweep, soweit mechanisch sicher:

`5 / 10 / 15 / 20 / 30 / 45 / 60 rpm`

Synchron erfassen:

- Rotorwinkel/rpm;
- Antriebsleistung bzw. Torque;
- Knotenspannungen;
- Pickup-/Gate-/Pot-Ströme;
- Leakage/Corona;
- Ladung pro Zyklus.

Nach jedem Block Antrieb vollständig abkoppeln und Nullzustand erneut prüfen.

## Phase 12 — Load-Reaction

Erst nach stabiler Node Map.

Vergleich:

- Ausgang offen;
- mehrere definierte ohmsche Lasten;
- Dummy-Lastlauf.

Synchron messen:

- `V_load(t)`;
- `I_load(t)`;
- rpm;
- Torque/Antriebsleistung;
- Bias-Energie;
- Speicherenergie vorher/nachher.

Hauptfrage: Wo erscheint die energetische Rückwirkung der Last?

## Phase 13 — gekoppelte Topologien

Erst jetzt kontrollierte Drive-/Load-Bus-Varianten testen. Jede Verbindung ist explizit in der Config-ID/Run-Metadatei zu speichern.

Keine Topologie wird allein deshalb historisch, weil sie funktioniert oder interessante Signale erzeugt.

## Phase 14 — geschlossene Energiebilanz

Nur bei einem reproduzierbaren interessanten Effekt.

Bilanz:

`E_out > E_mech,in + E_bias,in + E_aux,in + E_stored,initial - E_stored,final`

muss mit Messunsicherheit geprüft werden. Vor einer Anomalieaussage sind nötig:

- Langzeitlauf;
- Kalibrierungen;
- Blind-/Dummy-Versuche;
- unabhängige zweite Gerätefamilie oder zweite Gruppe;
- Rohdatenpublikation;
- vorab eingefrorenes Auswerteprotokoll.

## Abbruchkriterien

Versuch sofort ungültig/abbrechen bei:

- unerwartetem Rotor-Sektor-Durchgang;
- mechanischem Streifen;
- sichtbarem Riss/Unwucht;
- unkontrollierter Entladung;
- unbekannter zusätzlicher Energie-/Masseverbindung;
- fehlender Config-ID;
- nicht dokumentierter Änderung zwischen Vergleichsläufen.

Diese Reihenfolge optimiert nicht auf „Selbstlauf“, sondern auf maximalen Informationsgewinn und saubere Falsifizierbarkeit.
