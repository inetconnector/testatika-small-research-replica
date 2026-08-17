# CAD

## Primäre Fertigungsmodelle

Die primären CAD-Ausgaben sind jetzt **Fertigungs-Bausätze mit Werkstofftrennung**, nicht mehr all-solid/all-plastic Komplett-STLs:

- `generate_m2_v5_fabrication_kit.py` — kleine M2, reale Material-/Kaufteil-Schnittstellen;
- `generate_m6_v2_fabrication_kit.py` — große ~500-mm-M6, reale Material-/Kaufteil-Schnittstellen.

Die historischen Einstiegspunkte `generate_v4_best_evidence_m2.py` und `generate_m6_large_v1.py` bleiben aus Kompatibilitätsgründen bestehen, rufen aber jetzt die jeweiligen Fertigungs-Bausätze auf.

## Fertigungsklassen

Jeder Bausatz erzeugt:

- `print/` — ausschließlich Kunststoffteile, die technisch wirklich Kunststoff sein dürfen: Halter, Clips, Jigs, Zentrierringe, Träger und Schutzteile; primär tragende Lagerböcke/Retainer sind echte Fertigungsteile;
- `fabricate/` — STEP-Geometrien für echte PMMA-, Metall-, Wellen-, Elektroden-, Gitter- und Wickelteile;
- `assembly-reference/` — vollständige Passungs-/Montageansichten mit `REFERENCE_NOT_FOR_PRINT` im Namen;
- `metadata/` — maschinenlesbare Fertigungs-, Material-, Kaufteil- und Schnittlisten.

**Verbotene Abkürzung:** Ein Kondensator, Metallgitter, Magnetkern, Kupferwickel, Rotorblech, Welle, Lager oder eine PMMA-Rotorscheibe darf nicht nur deshalb als STL gedruckt werden, weil es geometrisch im Referenzmodell vorkommt.

## Kleine M2 — V5 Fertigungs-Bausatz

Ausgabe: `hardware/build-kits/m2-v5/`

Quellenbasis: M2 V4 best-evidence. Der Bausatz übernimmt insbesondere ca. 200-mm-Rotor, nominell 24 elektrisch getrennte Cu-Sektoren, zwei externe Pot-Anschlüsse und die reversible Crystal-/Magnet-/Stator-Forschungsgrenze.

Leitfaden: [`../docs/research/m2-v5-fabrication-kit.md`](../docs/research/m2-v5-fabrication-kit.md)

## Große M6 — V2 Fertigungs-Bausatz

Ausgabe: `hardware/build-kits/m6-v2/`

Quellenbasis: M6 V1 / M6a-Hauser. Der Bausatz bewahrt die Ø500×5-mm-Scheiben, 50-Lamellen-Anker, 8-vorn/6-hinten-Statoren und die Drei-Gitter-Zylinderarchitektur. Die konkrete Lager-/Wellenlösung ist eine stabile, dokumentierte LAB-BUILD-Mechanik und keine Behauptung über die historische Originalmechanik.

Leitfaden: [`../docs/research/m6-v2-fabrication-kit.md`](../docs/research/m6-v2-fabrication-kit.md)

## Referenz-CAD

Die bisherigen all-solid Modelle und Generatoren werden **nicht gelöscht**. Sie werden als `reference-visual-only`/`LEGACY_REFERENCE_ONLY` erhalten. Sie dienen zum Anschauen, zur Provenienz und zur Geometrievergleichung; sie sind keine Druckanweisung für funktionale Baugruppen.

Die ursprünglichen Generatorquellen liegen zusätzlich unter:

- `cad/reference/generate_m2_v4_visual_reference_legacy.py`
- `cad/reference/generate_m6_v1_visual_reference_legacy.py`

## Rebuild

```bash
python scripts/rebuild_research_assets.py
```

Für die neuen Bausätze zusätzlich explizit:

```bash
python cad/generate_m2_v5_fabrication_kit.py
python cad/generate_m6_v2_fabrication_kit.py
python scripts/normalize_buildkit_step.py
python scripts/check_build_kits.py
```

Die vollständige historische elektrische Schaltung ist weiterhin nicht belegt. Der CAD-Bausatz macht unbekannte Stellen austauschbar/offen, statt eine vermeintliche Funktionsschaltung zu erfinden.
