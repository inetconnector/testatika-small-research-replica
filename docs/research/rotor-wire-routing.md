# Rotor-Drahtführung — Geometrie und elektrische Topologie getrennt

Marinov nennt für die frühen kleinen Maschinen radiale Kupferdrähte von ungefähr 1 mm. In späterer Korrespondenz betont er, dass **sehr wichtig sei, wie diese Drähte durch die Scheibe gehen**.

Ein neuer direkt ausgewerteter Marinov-Scan (`hauser/SMwebL1.jpg`) klärt zusätzlich eine andere Frage: Die Drähte auf der beschriebenen kleinen Scheibe seien **`connected to nothing`**.

Damit müssen zwei Dimensionen strikt getrennt werden:

1. **geometrische Führung R0–R4** — weiterhin teilweise unbekannt;
2. **elektrische Topologie E0/E1** — E0 floating ist jetzt die bevorzugte Kleinmaschinen-Baseline.

## Sektorzahl

V2/V3 führen weiterhin:

- `rotor_20wire` — untere Grenze;
- `rotor_24wire` — nominale Foto-/Text-Arbeitsvariante;
- `rotor_25wire` — obere Grenze der späteren Marinov-Angabe.

## Elektrische Topologie

### E0 — floating individual sectors — Baseline

Direkte Primärquelle: `SMwebL1.jpg`.

Jeder Sektordraht:

- ist galvanisch von den anderen Sektoren getrennt;
- ist nicht an einen gemeinsamen Hub-/Collector-Ring angeschlossen;
- ist nicht über Nachbarwiderstände verbunden;
- soll mechanisch so fixiert werden, dass die Isolation erhalten bleibt.

Vor Versuchen sind zu protokollieren:

- Widerstand Drahtende↔Drahtende desselben Sektors;
- Isolation jedes Sektors gegen Nachbarsektoren;
- Isolation gegen Hub/Welle;
- Isolation gegen magnetische/strukturelle Bauteile.

### E1 — 1-kΩ neighbour ring — nur Sekundärkontrolle

Eine späte Frolov-Kompilation schreibt benachbarten Lamellen ~1-kΩ-Verbindungen zu. Dafür fehlt eine ältere maschinenspezifische Primärquelle, und der Claim steht für die kleine Maschine nun im Konflikt mit Marinovs direkter Aussage `connected to nothing`.

Daher:

- **nicht M2-Baseline**;
- nicht als `original` bezeichnen;
- nur als geometrisch identischer, klar markierter Kontrollrotor testen;
- E0/E1 niemals gleichzeitig mit Material oder Route variieren.

## Testbare geometrische Führungsvarianten

### R0 — einseitig radial

Ein gerader Draht liegt auf einer Scheibenseite zwischen Innen- und Außenradius.

**Status:** einfachste geometrische Interpretation; elektrisch E0 floating.

### R1 — U-/Stitch-Führung

Draht läuft radial auf Vorderseite, durch das äußere Loch nach hinten und auf der Rückseite zurück.

**Status:** mit Marinovs Hinweis `through the disk` vereinbar, aber nicht belegt.

### R2 — alternierende Flächen

Gerade radiale Leiter wechseln von Segment zu Segment Vorder-/Rückseite.

**Status:** Hypothese.

### R3 — winkelversetzte Durchleitung

Innenloch Segment i → Außenloch Segment i+1 auf der Gegenseite.

**Status:** experimentelle Hypothese; kann eine geometrische/elektrische Phasenverschiebung erzeugen.

### R4 — three-side-change weave

Hans Holzherr berichtet für mehrere Testatika-Maschinen, darunter ein größeres Modell im Bau, dass `sector wires` in die Scheibe eingewebt seien und **dreimal die Scheibenseite wechseln**.

Dies ist relevant, weil Marinov unabhängig davon die genaue Führung der Drähte **durch die Scheibe** als wichtig bezeichnet.

Die optionale V3-Forschungsgeometrie setzt deshalb pro Sektor fünf Bohrungsradien:

- 27 mm: Innenanker;
- 40 mm: Seitenwechsel 1;
- 60 mm: Seitenwechsel 2;
- 80 mm: Seitenwechsel 3;
- 94 mm: Außenanker.

Nominale Testführung:

`Vorderseite 27→40 | Rückseite 40→60 | Vorderseite 60→80 | Rückseite 80→94`

Dateien:

- `rotor_20wire_R4_3cross`;
- `rotor_24wire_R4_3cross`;
- `rotor_25wire_R4_3cross`.

**Evidenzstatus:** stark testwürdig, aber **nicht als gesicherte M2-Originalgeometrie** behandeln. Holzherrs Aussage bezieht sich auf mehrere Maschinen; eine direkte Identität mit Marinovs kleiner Maschine ist nicht bewiesen.

## Experimentelle Matrix

Empfohlene Reihenfolge:

1. E0-R0, E0-R1, E0-R2, E0-R3, E0-R4 bei gleichem Material;
2. beste/auffälligste E0-Route gegen E1 derselben Route;
3. erst danach Cu/Fe/Fe-Ni-Materialvarianten.

Messen:

- `C(theta)`;
- Sektor-/Oberflächenpotential;
- Pickup-Strom;
- Ladungsrelaxation;
- Torque/RPM;
- Load Reaction.

Siehe auch:

- [`r4-grid-vs-foil.md`](r4-grid-vs-foil.md)
- [`hauser-marinov-primary-scan-audit-2026-08-16.md`](hauser-marinov-primary-scan-audit-2026-08-16.md)
- [`replica-configuration-matrix.md`](replica-configuration-matrix.md)

## Methodische Regel

Keine R1–R4-Geometrie darf ohne zusätzliche Primärevidenz als `Originalführung` bezeichnet werden. **Elektrisch ist E0 floating inzwischen stärker gestützt als die zuvor offen gehaltenen Ringvarianten; geometrisch bleibt die durch-die-Scheibe-Route dennoch ungelöst.**
