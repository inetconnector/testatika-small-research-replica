#!/usr/bin/env python3
"""Integrate V4.12 local structured coupling into canonical research state.

Idempotent by section markers / first-column TSV keys. This script adds a
measurement/calculation layer only and never promotes a local RF/HV source,
active base, or resonant-power stage to historical M2 fact.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def append_block(path: str, marker: str, block: str) -> None:
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    if marker in text:
        return
    if not text.endswith("\n"):
        text += "\n"
    text += "\n" + block.strip() + "\n"
    p.write_text(text, encoding="utf-8")


def append_tsv_rows(path: str, rows: list[str]) -> None:
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    existing = {line.split("\t", 1)[0] for line in text.splitlines() if line}
    if not text.endswith("\n"):
        text += "\n"
    changed = False
    for row in rows:
        key = row.split("\t", 1)[0]
        if key in existing:
            continue
        text += row.rstrip("\n") + "\n"
        existing.add(key)
        changed = True
    if changed:
        p.write_text(text, encoding="utf-8")


append_block(
    "docs/research/source-basis.md",
    "## V4.12 local structured coupling — 2026-08-18",
    r'''## V4.12 local structured coupling — 2026-08-18

Canonical files:

- [`m2-v4-12-local-structured-coupling.md`](m2-v4-12-local-structured-coupling.md)
- `sim/m2_v4_12_local_structured_coupling.py`
- `tests/test_m2_v4_12_local_structured_coupling.py`

V4.12 follows the V4.11 result that ordinary ambient atmosphere/RF/Schumann/geomagnetic reservoirs are far too weak for sustained ~100-W tabletop output. It therefore tests the narrower conventional possibility of a **local structured source** coupled through base/table/chassis capacitance or a driven magnetic near field.

Key derived bounds:

1. A 30 x 30 cm comparison plate with 5 mm dielectric spacing and `eps_r=3` is about `478 pF`.
2. At `100 kHz`, that capacitance reaches the optimistic `100 VA` scale at about `577 V rms` and `173 mA rms` displacement current; at 50 Hz it needs about `25.8 kV rms`.
3. A strong source needs surprisingly little parasitic C: `10 kV rms` at `100 kHz` needs only about `1.59 pF` for the optimistic 100-VA bound. This makes "no visible wire" insufficient to exclude a deliberately strong local capacitive transmitter, but such a transmitter must still supply real load power and produce measurable local fields/source currents.
4. For a 200-mm loop, `100 V rms` induction at `100 kHz` requires about `5.07 mT` for one turn or `0.211 mT` for 24 ideal turns. At `1 MHz`, the 24-turn value falls to about `21.1 microtesla`. The transmitter remains the energy source.
5. A slow ~50-Hz mechanical gating pattern can in principle control a much faster externally supplied carrier without being the carrier itself. This is a control hypothesis only; Marinov's M2 line still does not justify an HF/Tesla historical baseline.

V4.12 therefore upgrades **local active coupling** from a vague alternative to a quantitatively falsifiable conventional source hypothesis. It does not identify such a source historically and makes no M2 CAD/topology change.'''
)

append_block(
    "docs/REPLICATION_STATUS.md",
    "## V4.12 local structured coupling discriminator",
    r'''## V4.12 local structured coupling discriminator

V4.12 adds a conventional hidden-port discriminator after ordinary ambient sources failed the V4.11 power bounds. It does not change M2 historical geometry or wiring.

For a 30 x 30 cm laboratory comparison base with 5 mm dielectric and `eps_r=3`, the estimated coupling is ~478 pF. An optimistic 100-VA scale then requires ~577 V rms / 173 mA rms at 100 kHz, or ~25.8 kV rms at 50 Hz. Conversely, a deliberately strong 10-kV/100-kHz local source needs only ~1.59 pF effective coupling.

This makes the next test requirement explicit: no-wire visual inspection is insufficient. A modern replica must measure local E/H fields, base/table/chassis displacement current, all instrumentation returns, mechanical work and storage-energy change simultaneously. M2 remains no-Tesla/HF historical baseline unless new machine-specific primary evidence appears.'''
)

append_block(
    "docs/research/experiment-plan.md",
    "## V4.12 — local structured source / base-table coupling",
    r'''## V4.12 — local structured source / base-table coupling

Purpose: determine whether apparent output follows the machine, table/building, local field or stored energy.

Use only current-limited low-energy surrogate excitation for characterization. Measure:

- base/table/chassis capacitance matrix and leakage before/after each run;
- front/rear/base displacement current with isolated instrumentation;
- wideband local E-field and B/H-field spectra;
- conductive enclosure versus nonconductive geometric dummy;
- low-frequency magnetic-field control separately from electric shielding;
- position/orientation sweeps while the entire measurement chain remains isolated;
- all mechanical input and storage-energy change.

Derived reference target: a 478-pF base at 100 kHz needs ~577 V rms and ~173 mA rms at the optimistic 100-VA scale. If a 100-W local capacitive source exists, a corresponding source-side current/field signature must be present. A resonance peak without source-side real power does not satisfy the energy ledger.'''
)

append_tsv_rows(
    "docs/research/evidence_matrix.tsv",
    [
        "V4.12 30cm base capacitance bound\tparallel-plate derivation / laboratory comparison geometry\tA=0.09m2, d=5mm, eps_r=3 gives ~478pF\tDERIVED CONTROL\tnot historical geometry; use to size base/table coupling measurements",
        "V4.12 100kHz base 100VA bound\tV4.12 derivation\t478pF at 100kHz reaches optimistic 100VA scale at ~577Vrms and ~173mArms displacement current\tDERIVED CONTROL\tlocal active source would be measurable; apparent power is not generated by passive capacitance",
        "V4.12 10kV 100kHz parasitic-C bound\tV4.12 derivation\t100W optimistic bound at 10kVrms and 100kHz requires only ~1.59pF effective coupling\tDERIVED CONTROL\tno visible wire does not exclude strong local capacitive WPT; real source power still required",
        "V4.12 magnetic near-field bound\tFaraday sinusoidal loop derivation\t200mm loop, 24 ideal turns, 100Vrms requires ~0.211mT at 100kHz or ~21.1uT at 1MHz\tDERIVED CONTROL\tlocal driven magnetic transmitter remains measurable source; not M2 historical coil evidence",
        "Resonant magnetic WPT conventional control\tKurs et al Science 2007 DOI 10.1126/science.1143254\tdeliberately driven self-resonant coils experimentally transferred tens of watts over metre-scale distance\tSCIENTIFIC CONTROL\tshows local resonant coupling can transfer real power when a transmitter supplies it; not Testatika evidence",
    ],
)

append_block(
    "STATE.md",
    "## V4.12 — local structured coupling bounds — 2026-08-18",
    r'''## V4.12 — local structured coupling bounds — 2026-08-18

V4.12 narrows the remaining conventional energy-source search after V4.11. Ordinary ambient natural sources are too weak, but a deliberately strong **local** capacitive or inductive source can transfer a 100-W scale without a visible galvanic wire.

Representative derived comparison: 30 x 30 cm, 5 mm, `eps_r=3` -> ~478 pF. At 100 kHz, the optimistic 100-VA scale is ~577 V rms / 173 mA rms; a 10-kV/100-kHz source needs only ~1.59 pF. For a 200-mm, 24-turn ideal loop, 100 V rms induction needs ~0.211 mT at 100 kHz. These are transmitter/coupling requirements, not energy creation.

Consequently the strongest remaining conventional candidate becomes local active base/table/chassis/common-mode or near-field coupling. It is now quantitatively falsifiable by simultaneous field, displacement-current, mechanical, storage and load metrology. M2 historical baseline remains unchanged and no HF/Tesla stage is promoted.'''
)

append_block(
    "addon.md",
    "## V4.12 handoff — local structured coupling — 2026-08-18",
    r'''## V4.12 handoff — local structured coupling — 2026-08-18

Read `docs/research/m2-v4-12-local-structured-coupling.md` after V4.11. The key result is that ordinary ambient sources fail, while a **local active** high-voltage/high-frequency capacitive or magnetic source could transfer 100 W through surprisingly small parasitic coupling. Example: ~478 pF needs ~577 V rms / 173 mA rms at 100 kHz; 10 kV at 100 kHz needs only ~1.59 pF. The transmitter must still supply real power and should be measurable.

Next work should focus on complete base/table/chassis/common-mode and local near-field metrology rather than adding unverified historical RF hardware.'''
)

append_block(
    "CHANGELOG.md",
    "### V4.12 local structured coupling — 2026-08-18",
    r'''### V4.12 local structured coupling — 2026-08-18

- added deterministic local capacitive/inductive hidden-port calculator and regression tests;
- quantified 30-cm base/table capacitance examples and the voltage/current needed for a 100-W/100-VA scale;
- showed that strong local HV/HF sources can couple substantial power through pF-scale parasitics, making no-visible-wire inspection insufficient by itself;
- added magnetic near-field / mutual-inductance bounds as a conventional transmitter control;
- kept local source, active base, RF and resonance hardware outside the historical M2 baseline;
- strengthened the simultaneous input/output/storage metrology requirement.'''
)

print("V4.12 local structured coupling integrated idempotently.")
