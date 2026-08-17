# Wiring documentation release checklist

Before merging changes to this directory:

- English and German electrical README are both updated and cross-linked.
- `WIRING_VARIANTS.tsv`, `LAMELLA_TEST_MATRIX.tsv`, and `SOURCE_IMAGE_FAMILIES.tsv` remain parseable and evidence-classed.
- M2/M6 SVG diagrams remain valid XML and show OPEN/W1 boundaries.
- `python scripts/check_evidence_wiring.py` passes.
- No hypothesis-only wiring is relabeled as a historical baseline.
