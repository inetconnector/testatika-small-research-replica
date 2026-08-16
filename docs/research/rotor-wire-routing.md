# Rotor-Drahtführung — der derzeit wichtigste ungeklärte Detailpunkt

Marinov nennt für die frühen kleinen Maschinen radiale Kupferdrähte von ungefähr 1 mm.
In einer späteren Korrespondenz präzisiert er, dass **sehr wichtig sei, wie diese Drähte durch die Scheibe gehen**.

Deshalb enthält V2 drei Rotorvarianten:
- `rotor_20wire`: untere Grenze des berichteten Bereichs.
- `rotor_24wire`: nominale Foto-/Text-Arbeitsvariante.
- `rotor_25wire`: obere Grenze der späteren Marinov-Angabe.

Jede V2-Position besitzt innere/äußere Durchführungsbohrungen für alternative Routen.

## Testbare Führungsvarianten

### R0 — einseitig radial
Ein gerader Draht liegt auf einer Scheibenseite zwischen Innen- und Außenradius.
**Status:** einfachste Interpretation.

### R1 — U-/Stitch-Führung
Draht läuft radial auf Vorderseite, durch das äußere Loch nach hinten und auf der Rückseite zurück.
**Status:** mit Marinovs Hinweis „through the disk“ vereinbar, aber nicht belegt.

### R2 — alternierende Flächen
Gerade radiale Leiter wechseln von Segment zu Segment Vorder-/Rückseite.
**Status:** Hypothese.

### R3 — winkelversetzte Durchleitung
Innenloch Segment i → Außenloch Segment i+1 auf der Gegenseite.
**Status:** experimentelle Hypothese; kann eine elektrische/geometrische Phasenverschiebung erzeugen.

### R4 — three-side-change weave
Hans Holzherr berichtet für mehrere Testatika-Maschinen, darunter ein größeres Modell im Bau, dass `sector wires` in die Scheibe eingewebt seien und **dreimal die Scheibenseite wechseln**.

Dies ist besonders relevant, weil Marinov unabhängig davon die genaue Führung der Drähte **durch die Scheibe** als wichtig bezeichnet.

Die optionale V3-Forschungsgeometrie setzt deshalb pro Sektor fünf Bohrungsradien:

- 27 mm: Innenanker
- 40 mm: Seitenwechsel 1
- 60 mm: Seitenwechsel 2
- 80 mm: Seitenwechsel 3
- 94 mm: Außenanker

Nominale Testführung:

`Vorderseite 27→40 | Rückseite 40→60 | Vorderseite 60→80 | Rückseite 80→94`

Dateien:
- `rotor_20wire_R4_3cross`
- `rotor_24wire_R4_3cross`
- `rotor_25wire_R4_3cross`

**Evidenzstatus:** stark testwürdig, aber **nicht als gesicherte M2-Originalgeometrie** behandeln. Holzherrs Aussage bezieht sich auf mehrere Maschinen; eine direkte Identität mit Marinovs kleiner Maschine ist nicht bewiesen.

Siehe auch `docs/research/r4-grid-vs-foil.md`.

## Methodische Regel

Keine der Varianten R1–R4 darf ohne zusätzliche Primärevidenz als „die Originalführung“ bezeichnet werden. Varianten sind möglichst bei identischer Scheibe, identischem Drahtmaterial, Elektrodenabstand und Umgebungsbedingungen gegeneinander zu messen.
