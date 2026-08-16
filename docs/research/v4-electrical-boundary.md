# V4 elektrische Evidenzgrenze

## Grundregel

V4 rekonstruiert die **belegte Anschlussklasse**, nicht einen erfundenen vollständigen Originalschaltplan.

## Historisch bevorzugte elektrische Baseline

### Rotor

- 20–25 einzelne leitfähige Sektoren; nominal 24;
- ca. 1-mm-Cu als stärkster M2-Materialanker;
- direkter Marinov-Scan: Drähte `connected to nothing`;
- daher: **keine galvanische Verbindung zwischen unterschiedlichen Sektoren**;
- keine Verbindung zum Schaft/Hub in der Nominalbaseline;
- keine Reibbürste.

### Pots

Je Seite zwei zugängliche Knoten:

- `GRID-L`, `SPIRAL-L`;
- `GRID-R`, `SPIRAL-R`.

Direkte Marinov-Quelle stützt zwei sichtbare Leitungen zu jedem Kondensator. Die genaue externe Zielverbindung/Polung ist weiterhin unbekannt.

### Hub-Bögen

Arbeitsknoten:

- `ARC-L`;
- `ARC-R`.

Status: photo/video-derived physische Bauteilkandidaten. **Keine historische elektrische Verbindung bekannt.** Baseline: floating.

### äußere Panels / Pickups

Arbeitsnamen, keine historischen Knotennamen:

- `PANEL-L-CARRIER`, `PANEL-L-INSET`, `PANEL-L-EDGE`;
- `PANEL-R-CARRIER`, `PANEL-R-INSET`, `PANEL-R-EDGE`;
- `PICKUP-L`, `PICKUP-R`;
- `CENTER-LOWER`.

Die reale Baugruppe soll diese Ebenen soweit praktikabel separat instrumentierbar halten.

### Crystal

Arbeitsknoten:

- `X1`, `X2` = sichtbare/nominale innere Positionen;
- `X3`, `X4` = zusätzliche isolierte Forschungspositionen.

Baseline:

`X1..X4 = OPEN`

Kein bestimmtes Material wird als Original eingesetzt.

## Baseline-Konfiguration `M2-V4-B0`

```text
ROTOR[1..24]  = individually floating
ARC-L/R       = floating
GRID-L/R      = open external measurement nodes
SPIRAL-L/R    = open external measurement nodes
PANEL/PICKUP  = individually measurable where physically implemented
X1..X4        = open
MAGNETS       = present, electrically isolated
LOAD          = disconnected
DRIVE         = none / mechanically decoupled
```

Dieser Zustand ist absichtlich **keine funktionsbehauptende Schaltung**. Er dient der vollständigen parasitären Kapazitäts-/Feld- und Ladungszustandsmessung.

## Erlaubte Forschungs-Topologien

Jede nachfolgende Verbindung bekommt eine Config-ID und wird gegenüber `M2-V4-B0` verglichen.

Zulässig als Hypothesentest:

- Pot GRID↔SPIRAL über R/C/Diode;
- links/rechts symmetrische oder gegensinnige Kopplung;
- Crystal open/short/R/C/Diode/antiparallel/crystal detector;
- Hub-Bögen floating/geguarded/definiert gekoppelt;
- Pickup→Speicher über passive Gleichrichtung;
- definierter Drive-Bus vs Load-Bus;
- externe geringe Bias-Ladung mit vollständig bilanzierter Energie.

## Nicht in die Nominalbaseline übernehmen

Ohne neue M2-Primärquelle:

- 1-kΩ-Ring zwischen Rotorsektoren;
- galvanischer Ringkollektor;
- Reibbürsten;
- Tesla-/HF-Sekundärspule in den M2-Pots;
- Hauser-M6a-3-Gitter/Magnetröhren/Bifilar-Zylinder;
- 20-Lagen-Großkondensator als M2-Pot;
- vier Leitungen am Crystal als historisch gesicherte M2-Topologie;
- radioaktive Materialien;
- Netzspannungs-HV-Versorgung als Teil des Nachbaus.

## Messregel

Vor einer Aussage über Funktion muss für jede Konfiguration mindestens bekannt sein:

- Config-ID;
- Commit-SHA;
- Rotorroute/Sektorzahl/Material;
- alle geschlossenen und offenen Knotenverbindungen;
- Pot-Kapazitäten und Anfangsspannungen;
- Crystal-Einsatz;
- Magnet-/Dummy-Zustand;
- Temperatur/RH;
- rpm/Rotordrehwinkel;
- externe Bias-/Antriebsenergie;
- Ausgangslast und Speicherenergie vorher/nachher.

## Energiebilanz

Eine hohe Leerlaufspannung, ein Funke, Nachlauf oder kurze Lampenleistung sind kein Energieüberschussnachweis.

Für jede Anomaliebehauptung gilt mindestens:

`E_out > E_mech,in + E_bias,in + E_aux,in + E_stored,initial - E_stored,final`

unter Berücksichtigung der Messunsicherheit und mit unabhängiger Replikation.
