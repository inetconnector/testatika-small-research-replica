# M2 V5 — evidenzbasierte Verdrahtung und funktionsfähige Laborvarianten

## Status

Dies ist der **kanonische elektrische Begleitplan** für den real-material M2-V5-Bausatz.

Er trennt strikt:

- historisch belegte Knoten/Anschlussklassen;
- unbekannte historische Verbindungen;
- konventionell funktionsfähige Laborverdrahtungen;
- spekulative Vergleichsvarianten.

Ein Laboraufbau gilt nicht deshalb als historische Testatika-Schaltung, weil er messbare Spannung liefert.

SVG-Übersicht:
`diagrams/M2_V5_EVIDENCE_WIRING.svg`

---

## 1. Historisch starke M2-Knoten

### Rotor

`R01..R24`

- nominal 24 reale Cu-Drahtsektoren;
- untereinander offen;
- gegen Welle/Nabe offen;
- keine Reibbürste;
- kein automatisch angenommener Widerstandsring.

### Linker Pot

- `GRID-L` — zylindrisches leitfähiges Gitter;
- `SPIRAL-L` — zentrale Kupferspirale.

### Rechter Pot

- `GRID-R`;
- `SPIRAL-R`.

Die direkte Marinov-Quellenlinie stützt einen **sichtbaren Zwei-Leiter-Anschluss pro Pot**, nicht dessen externe Polung.

### Nichtkontaktierende Elektroden / Pickups

Arbeitsknoten:

- `STAT-L1..Ln`;
- `STAT-R1..Rn`;
- `PICKUP-L`;
- `PICKUP-R`;
- `CENTER-LOWER`;
- `ARC-L`, `ARC-R` soweit physisch umgesetzt.

Keine dieser Bezeichnungen behauptet einen historischen Knotennamen.

### Crystal / Top-Modul

- `X1..X4`;
- Baseline = offen.

Keine Internetzeichnung darf hier ohne Config-ID fest verdrahtet werden.

---

# 2. M2-W0 — OPEN / Charakterisierung

```text
R01..R24       FLOATING
GRID-L/R       OPEN -> guarded measurement terminal
SPIRAL-L/R     OPEN -> guarded measurement terminal
STAT/PICKUP    individually OPEN -> measurement terminal
ARC-L/R        FLOATING
X1..X4         OPEN
MAGNETS        mechanically present as selected variant, electrically isolated
LOAD           disconnected
EXTERNAL BIAS  disconnected
LAB DRIVE      mechanically decoupled unless measuring C(theta)
```

### Pflichtmessungen

Vor jeder Verschaltung:

1. Isolationsmatrix aller Knoten;
2. Kapazitätsmatrix bei festem Rotorwinkel;
3. `C(theta)` über mindestens eine Umdrehung;
4. Oberflächenpotential nach definiertem Startzustand;
5. Leckstrom vs relative Feuchte;
6. Rotor-Drehmoment ohne elektrische Biasquelle;
7. Pot-Kapazitäten `GRID↔SPIRAL` links/rechts.

W0 ist der Referenzzustand für alle späteren Behauptungen.

---

# 3. M2-W1 — konventionell funktionsfähiger elektrostatischer Charge-Transfer-Test

**Zweck:** Nachweisen, dass die reale Geometrie rotationsabhängige Ladung/Spannung erzeugen bzw. übertragen kann, ohne historische Geheimverbindungen zu erfinden.

## Schaltung

```text
commercial isolated current-limited electrostatic bias
      +BIAS ---------------- Rlim+ ---------------- DRIVE/PANEL-L
      -BIAS ---------------- Rlim- ---------------- DRIVE/PANEL-R

PICKUP-L -------------------+----[ HV rectifier bridge ]---- +STORE
PICKUP-R -------------------+----[                  ]---- -STORE

+STORE -------- Cstore -------- -STORE
+STORE -------- Rbleed_hi ------ MID/guard reference
-STORE -------- Rbleed_lo ------ MID/guard reference

GRID-L ---- measurement/patch only
SPIRAL-L -- measurement/patch only
GRID-R ---- measurement/patch only
SPIRAL-R -- measurement/patch only
X1..X4 ---- OPEN
```

### Sicherheits-/Messgrenze

- nur gekapselte, kommerzielle, potentialfreie und strombegrenzte Labor-Elektrostatikquelle;
- erste Versuche auf **niedrige gespeicherte Energie** begrenzen;
- `Rlim` und Bleeder so dimensionieren, dass nach Abschalten ein definierter sicherer Entladezustand entsteht;
- HV-Differentialsonde/Elektrometer verwenden; Oszilloskop-Schutzleiter niemals ungeprüft an einen floating-HV-Knoten legen;
- Rotor zunächst über externen Niederspannungs-Labormotor mit separat gemessener Eingangsleistung drehen.

### Erfolgskriterium

W1 ist erfolgreich, wenn reproduzierbar messbar sind:

- rotorwinkel-/drehzahlabhängiger Pickup-Strom oder Ladung;
- definierte Polarität nach Gleichrichtung;
- Ladung von `Cstore` oberhalb Leck-/Messartefakt;
- quantitative Abhängigkeit von Spalt, Feuchte und Drehzahl.

Das ist ein **konventioneller Funktionsnachweis**, kein Nettoenergiebeweis.

---

# 4. M2-W2 — Marinov-nahe Drive-/Collection-Bus-Hypothese

Marinov unterscheidet in seiner eigenen Interpretation zwischen Elektroden, die eine hohe Feld-/Drive-Spannung tragen, und Elektroden, die Ladung für eine niedrigere Ausgangs-/Speicherstufe sammeln könnten. Die exakten originalen Gruppen sind unbekannt.

Darum wird W2 **nicht per Kabelbaum festgelegt**, sondern über einen Patchblock.

## Patchbusse

- `D+` / `D-` = Drive-/Feldelektrodenbus;
- `C+` / `C-` = Collection-Bus;
- jeder physische Stator/Pickup kann einzeln auf **einen** dieser Busse oder `OPEN` gesteckt werden;
- jede Änderung erhält eine Config-ID.

## Erstes symmetrisches Testmuster

```text
selected left field electrode(s)   -> D+
selected right field electrode(s)  -> D-
selected left pickup(s)            -> C+
selected right pickup(s)           -> C-

D+ / D- -> current-limited bias or precharged low-energy field capacitors
C+ / C- -> HV rectifier -> measured storage capacitor/load
```

Die Auswahl der Elektroden erfolgt **nach gemessener Phasenlage**, nicht nach einem Internetbild.

### Pot-Varianten innerhalb W2

Je Pot nur eine Variante gleichzeitig:

- `P0` = GRID/SPIRAL offen;
- `P1` = GRID an jeweiligen Drive-Bus, SPIRAL nur messen;
- `P2` = GRID an Drive-Bus, SPIRAL über HV-Diode an Collection-Bus;
- `P3` = GRID/SPIRAL als reiner Speicher-/Kopplungskondensator mit bekannter externer Kapazität parallel;
- `P4` = Seiten vertauscht.

`P1..P4` sind **Laborhypothesen**, keine Originalschaltung.

---

# 5. M2-W3 — Crystal-/Diodentest ohne Originalbehauptung

Baumann sprach gegenüber Marinov von einem `crystal`; die Methernitha-Beschreibung verwendet an anderer Stelle die Funktionsbezeichnung `rectifying diode`. Material und genaue M2-Topologie sind offen.

Darum:

```text
X1--X2  replaceable two-terminal test module
X3--X4  independent control module
```

Zulässige Vergleichsmodule:

- OPEN;
- SHORT über definierten Messshunt;
- kommerziell spezifizierte HV-Diode;
- antiparallele Dioden;
- R;
- C;
- RC;
- passiver Kristalldetektor als ausdrücklich experimentelle Variante.

Keine radioaktiven Materialien. Kein Modul darf als `original crystal` beschriftet werden.

---

# 6. M2-W4 — Potter/Kelly-Vergleich nur als ausgeschlossene Vergleichslinie

Kelly-/Potter-Bilder enthalten Reibbürsten-/HF-/Magnetspulen- und zusätzliche Verstärkerschaltungen. Diese sind **nicht** M2-Baseline, weil stärkere direkte M2-Quellen u. a. floating Rotorleiter, keine Reibbürsten und keine gesicherte Tesla/HF-Pot-Funktion stützen.

W4 darf nur auf einer **externen Vergleichsplatte** aufgebaut werden. Kein W4-Bauteil wird dauerhaft in den M2-V5-Kabelbaum integriert.

---

# 7. Messartefakt-Sperre

Bei floating elektrostatischen Systemen kann eine geerdete Oszilloskopmasse die Schaltung fundamental verändern oder kurzschließen.

Für jeden Messkanal dokumentieren:

- galvanisch verbunden / potentialfrei / optisch isoliert;
- Eingangswiderstand;
- Eingangskapazität;
- maximal zulässige Gleichtaktspannung;
- Masse-/Schirmverbindung;
- Messgerät-Erde.

Ein Signal gilt erst als real, wenn es mit mindestens einer zweiten, elektrisch anders ankoppelnden Messmethode bestätigt ist.

---

# 8. Pflicht-Energiebilanz

Für jede Konfiguration:

```text
Eout_load
<=/?>
E_lab_motor + E_bias_supply + delta(E_all_caps) + delta(E_mechanical) + E_other_aux
```

Aufzeichnen:

- Motorleistung und Zeit;
- Biasquellen-Leistung und Zeit;
- Anfangs-/Endspannung **jedes** Speicherkondensators;
- Drehzahl und Trägheitsänderung;
- Lastspannung/-strom synchron;
- Temperatur/RH;
- Null-/Dummy-Versuche.

Eine hohe Leerlaufspannung, ein Funke oder ein kurz aufleuchtendes Leuchtmittel ist kein Energieüberschussnachweis.
