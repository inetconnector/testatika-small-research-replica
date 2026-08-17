# Testatika — electrical build documentation

<p align="center">
  <a href="README.de.md">Deutsch</a> · <strong>English</strong>
</p>

## Canonical plans

### Small M2 V5

- [`M2_V5_EVIDENCE_WIRING.md`](M2_V5_EVIDENCE_WIRING.md)
- [`diagrams/M2_V5_EVIDENCE_WIRING.svg`](diagrams/M2_V5_EVIDENCE_WIRING.svg)

### Large M6 V2

- [`M6_V2_EVIDENCE_WIRING.md`](M6_V2_EVIDENCE_WIRING.md)
- [`diagrams/M6_V2_EVIDENCE_WIRING.svg`](diagrams/M6_V2_EVIDENCE_WIRING.svg)

## Machine-readable registries

- [`WIRING_VARIANTS.tsv`](WIRING_VARIANTS.tsv) — all wiring variants with evidence class and claim boundary
- [`LAMELLA_TEST_MATRIX.tsv`](LAMELLA_TEST_MATRIX.tsv) — material/magnetization/geometry A/B matrix
- [`SOURCE_IMAGE_FAMILIES.tsv`](SOURCE_IMAGE_FAMILIES.tsv) — deduplicated schematic/image families
- [`SOURCE_IMAGE_FAMILIES.md`](SOURCE_IMAGE_FAMILIES.md) — interpretation key
- [`BUILD_ORDER.md`](BUILD_ORDER.md) — electrical commissioning sequence

## Source audits

- [`../research/wiring-and-lamella-audit-2026-08-17.md`](../research/wiring-and-lamella-audit-2026-08-17.md)
- [`../research/wiring-image-audit-addendum-2026-08-17.md`](../research/wiring-image-audit-addendum-2026-08-17.md)
- [`../research/hauser-marinov-primary-scan-audit-2026-08-16.md`](../research/hauser-marinov-primary-scan-audit-2026-08-16.md)
- [`../research/hartmann-overunity-cathomen-audit.md`](../research/hartmann-overunity-cathomen-audit.md)
- [`../research/r4-grid-vs-foil.md`](../research/r4-grid-vs-foil.md)

## Electrical contract

1. **No hidden guessed wiring.** Every historically uncertain connection is patched externally and receives a Config-ID.
2. **Direct sources outrank reverse engineering.** Marinov/Hauser/Cathomen/Holzherr constraints outrank Kelly/Potter/Rimstar reconstructions where they conflict.
3. **An electrically working laboratory circuit is not automatically the historical original circuit.**
4. **High-voltage tests start with low stored energy and commercial current-limited laboratory equipment.**
5. **Floating systems require floating/differential instrumentation.** Never assume oscilloscope ground is electrically harmless.
6. **Energy claims require a closed balance** including motor, bias source, initial/final stored energy, mechanics, load and measurement uncertainty.

## What remains unknown

The publicly available material still does **not disclose a reproducible authentic node-for-node Methernitha circuit**. The crystal material/function, exact M2 pot polarity, exact M6 grid interconnections and Cathomen's unexplained upper conditioning/capacitance stage also remain unresolved.

Those gaps are represented as open interfaces rather than hidden behind invented components.
