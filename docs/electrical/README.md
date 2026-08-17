# Testatika electrical build documentation

## Canonical plans

### Small M2 V5

- [`M2_V5_EVIDENCE_WIRING.md`](M2_V5_EVIDENCE_WIRING.md)
- [`diagrams/M2_V5_EVIDENCE_WIRING.svg`](diagrams/M2_V5_EVIDENCE_WIRING.svg)

### Large M6 V2

- [`M6_V2_EVIDENCE_WIRING.md`](M6_V2_EVIDENCE_WIRING.md)
- [`diagrams/M6_V2_EVIDENCE_WIRING.svg`](diagrams/M6_V2_EVIDENCE_WIRING.svg)

## Machine-readable experiment registries

- [`WIRING_VARIANTS.tsv`](WIRING_VARIANTS.tsv)
- [`LAMELLA_TEST_MATRIX.tsv`](LAMELLA_TEST_MATRIX.tsv)

## Source audit

- [`../research/wiring-and-lamella-audit-2026-08-17.md`](../research/wiring-and-lamella-audit-2026-08-17.md)
- [`../research/wiring-image-audit-addendum-2026-08-17.md`](../research/wiring-image-audit-addendum-2026-08-17.md)
- [`../research/hauser-marinov-primary-scan-audit-2026-08-16.md`](../research/hauser-marinov-primary-scan-audit-2026-08-16.md)
- [`../research/hartmann-overunity-cathomen-audit.md`](../research/hartmann-overunity-cathomen-audit.md)
- [`../research/r4-grid-vs-foil.md`](../research/r4-grid-vs-foil.md)

## Electrical contract

1. **No hidden guessed wiring.** Every uncertain historical connection is patched externally and receives a Config-ID.
2. **Direct sources outrank reverse engineering.** Marinov/Hauser/Cathomen/Holzherr constraints outrank Kelly/Potter/Rimstar reconstructions where they conflict.
3. **A working laboratory circuit is not automatically the historical circuit.** `LAB-CONVENTIONAL` means electrically coherent and experimentally useful, not historically authenticated.
4. **High-voltage work starts with low stored energy.** Use enclosed commercial current-limited laboratory electrostatic equipment; no open mains-derived HV construction is part of this repository.
5. **Floating systems require floating/differential instrumentation.** Never assume oscilloscope ground is electrically harmless.
6. **Energy claims require a closed balance.** Motor, bias source, initial capacitor energy, mechanical energy, output load and uncertainty are all included.

## What the current plans deliberately do not claim

The available public material still does not disclose a reproducible authentic node-for-node Methernitha circuit, the exact Crystal material/function, the exact M2 pot polarity, the exact M6 grid interconnections, the exact top-module internals or a closed independent net-energy balance.

Those gaps are represented as **open interfaces**, not silently invented parts.
