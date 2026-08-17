# Legacy CAD sources — visual/provenance reference only

Dieser Ordner bewahrt die ursprünglichen all-solid Generatoren unverändert für Provenienz, Geometrievergleich und historische Reproduzierbarkeit.

- `generate_m2_v4_visual_reference_legacy.py` — ursprünglicher M2-V4-Vollmodellgenerator;
- `generate_m6_v1_visual_reference_legacy.py` — ursprünglicher M6-V1-Vollmodellgenerator.

Diese Generatoren sind **keine primäre Fertigungsanweisung**. Die real-materialisierten Bausätze werden von `cad/generate_m2_v5_fabrication_kit.py` und `cad/generate_m6_v2_fabrication_kit.py` erzeugt. Funktionale Metall-, PMMA-, Wellen-, Lager-, Magnet-, Gitter- und Wickelteile dürfen nicht durch die Vollmodell-STLs als Kunststoffteile interpretiert werden.
