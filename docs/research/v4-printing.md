# V4 3D-Druck- und Fertigungshinweise

## Zweck

Die STL-Dateien machen die **mechanische Forschungsplattform** reproduzierbar. Elektrisch aktive historische Materialien sollen dort, wo relevant, nicht durch beliebigen 3D-Druck-Kunststoff ersetzt werden.

## Druckteile vs. echte Funktionsmaterialien

### Sinnvoll druckbar

- mechanische Träger;
- Hüllen;
- Montagejigs;
- Panel-Träger;
- Crystal-Blackbox-Träger;
- Schutzhaubenpfosten;
- Magnet-Dummys;
- Bohr-/Routingrotoren für mechanische Versuche.

### Nicht einfach durch Druckmaterial ersetzen

- echte Cu-Rotorleiter;
- Metallgitter/Lochblech;
- innere Pot-Cu-Spiralen;
- echtes PMMA/Acryl-Dielektrikum, wenn dessen Ladungs-/Leckverhalten untersucht wird;
- reale Magnete;
- sicherheitsrelevante Hochspannungsisolatoren.

## Allgemeine Druckparameter

Für rein mechanische Prototypen als Startpunkt:

- Düse: 0,4 mm;
- Layer: 0,20 mm;
- 3–4 Perimeter;
- 20–35 % Infill bei Trägern;
- mehr Infill/Perimeter an Lager-/Schraubstellen;
- keine automatische Skalierung im Slicer;
- STEP als Geometriereferenz verwenden, wenn der Slicer/Workflow dies unterstützt.

Diese Werte sind **Fertigungsstartwerte**, keine historischen Materialdaten.

## Materialwahl

- PLA: gut für Maß-/Passprototypen, nicht als zertifizierter HV-Isolator;
- PETG/ASA: oft robuster für mechanische Träger;
- PMMA-Funktionsteile: wenn die historische Dielektrikumklasse untersucht wird, echtes Acryl/PMMA verwenden;
- PTFE/Keramik: nur als bewusst abweichende Isolations-/Kontrollmaterialien dokumentieren.

## Rotor

Der Rotor ist besonders sicherheitskritisch.

1. Scheibe plan drucken/fertigen.
2. Bohrungen nacharbeiten ohne Kerben/Risse.
3. Cu-Drähte einzeln einsetzen.
4. alle Leiter mechanisch sichern.
5. statisch und dynamisch auswuchten.
6. zunächst bei sehr niedriger Drehzahl testen.
7. nur unter Schutzhaube hochdrehen.

Für ernsthafte Rotationsversuche kann eine gefräste PMMA-Scheibe dem FDM-Rotor mechanisch überlegen sein. Die CAD-Datei dient dann als Bohr-/Routingvorlage.

## Pots

`pot_grid_former_v4`, `pot_acrylic_sleeve_jig_v4` und `pot_spiral_mandrel_v4` sind primär Montage-/Formhilfen.

Empfohlener Forschungsaufbau:

- gedruckter äußerer Träger;
- echtes Metallgitter;
- echtes PMMA-Rohr;
- echte Cu-Spirale;
- gedruckter Deckel mit zwei isolierten Buchsen.

## Außenpanels

`outer_panel_layered_v4` bildet die beobachtete Mehrlagenform ab. Für elektrische Versuche aktive und passive Ebenen trennen:

- gedruckter grober Träger;
- austauschbares echtes Metallgitter/Lochblech;
- austauschbares feines Inset;
- isolierender Dummy gleicher Geometrie;
- Vollfolie als kontrollierte Vergleichsvariante.

## Hub-Bögen

Die CAD-Bögen sind zunächst nur Geometrie.

Für A/B-Versuche mindestens herstellen:

1. leitfähige Cu-/Messingvariante;
2. elektrisch isolierende geometrisch gleiche Dummyvariante;
3. `absent`-Konfiguration.

## Toleranzen

Vor Serienfertigung immer Testcoupons/Einzelteile prüfen:

- Welle/Lager;
- Schraubenlöcher;
- Pot-Rohrdurchmesser;
- Buchsenbohrungen;
- Rotor-Bohrungen.

Druckerabhängige Passung wird nicht als historische Abmessung in das CAD zurückgeschrieben.

## Dateiorganisation

Nach Materialisierung:

- `hardware/experimental/v4-best-evidence-m2/stl/` — Druck-/Mesh-Dateien;
- `hardware/experimental/v4-best-evidence-m2/step/` — editierbare neutrale CAD-Ausgabe;
- `hardware/experimental/v4-best-evidence-m2/complete-model/` — komplette Nominal-/R4-Baugruppe;
- `hardware/experimental/v4-best-evidence-m2/metadata/` — Modellstatus und Evidenzgrenzen.

## Sicherheit

Für elektrische/rotierende Versuche gilt zusätzlich `safety.md`. Gedruckte Kunststoffe sind nicht automatisch für historische Hochspannung oder gespeicherte Energie geeignet.
