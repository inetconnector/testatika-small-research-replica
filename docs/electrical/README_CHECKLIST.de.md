# Freigabe-Checkliste für die Verdrahtungsdokumentation

Vor dem Merge von Änderungen in diesem Verzeichnis:

- Englische und deutsche elektrische README sind beide aktualisiert und gegenseitig verlinkt.
- `WIRING_VARIANTS.tsv`, `LAMELLA_TEST_MATRIX.tsv` und `SOURCE_IMAGE_FAMILIES.tsv` bleiben parsebar und nach Evidenzklassen gekennzeichnet.
- M2-/M6-SVG-Pläne bleiben gültiges XML und zeigen die OPEN-/W1-Grenzen.
- `python scripts/check_evidence_wiring.py` läuft erfolgreich durch.
- Keine reine Hypothesenverdrahtung wird als historische Baseline umetikettiert.
