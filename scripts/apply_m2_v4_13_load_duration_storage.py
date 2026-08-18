#!/usr/bin/env python3
"""Integrate V4.13 load-duration / finite-storage findings canonically.

Idempotent by section markers / first-column TSV keys. This integration does
not assert hidden batteries or fraud. It separates observed running duration,
load-connected duration, load ratings, measured power and operator claims.
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
    "## V4.13 / load-duration versus finite storage — 2026-08-18",
    r'''## V4.13 / load-duration versus finite storage — 2026-08-18

Canonical records:

- [`load-duration-storage-audit-2026-08-18.md`](load-duration-storage-audit-2026-08-18.md)
- [`internet-source-ledger-round13.tsv`](internet-source-ledger-round13.tsv)
- `sim/m2_v4_13_load_duration_storage_bound.py`
- `tests/test_m2_v4_13_load_duration_storage_bound.py`

The main evidence correction is an **energy-integral** distinction. Holzherr's 1999 M6b report says the ~50-cm machine remained running during an approximately 1.5-hour visit, but the explicitly identified 1000-W lamp was connected for only about 10 seconds. When asked whether hidden flat batteries could account for the demonstration, Holzherr answered that he could not judge it. The protected 50-cm machine could not be touched/lifted; his liftable-while-running observation applies to separate ~12-cm M4-family models.

Therefore `1.5 h running` must not be converted into `1.5 h x 1 kW output`. If the 1000-W lamp had actually received its full nameplate power for ten seconds, the rating-equivalent load energy would be only `10 kJ = 2.78 Wh`. The report contains no synchronized calibrated V-I trace establishing that exact real power.

A later reproduction of the Schneider/Weber 13-Mar-1984 M5 visit similarly separates an approximately `300 V / 10 A` output statement from Baumann's claim that operation could continue for hours/years. The witnessed lamp/heater effects are short qualitative demonstrations, while the lift/underside inspection constrains obvious external feeds but is not a closed internal/storage/field audit.

Derived electrostatic-storage comparison: 10 kJ requires ideally ~`2 uF at 100 kV` or ~`22.2 uF at 30 kV`. This is a measurement target, not a claim about original capacitor values.

V4.13 consequently keeps **finite internal storage** open as a conventional explanation for short historical load demonstrations. The decisive criterion is integrated load energy versus all measured external/mechanical inputs and initial-to-final storage change. No M2 historical topology change follows.'''
)

append_block(
    "docs/REPLICATION_STATUS.md",
    "## V4.13 load-duration / storage-energy discriminator",
    r'''## V4.13 load-duration / storage-energy discriminator

V4.13 adds no historical M2 hardware. It corrects a common energy-accounting error: machine-running duration is not automatically load-delivery duration.

For the M6b Holzherr 1999 report, ~1.5 h is the observed running interval, while the explicitly described 1000-W lamp interval is only ~10 s. Even if the lamp received its full rating, that interval represents only ~10 kJ = 2.78 Wh. The actual synchronized V-I load power was not recorded in the preserved report.

Finite storage is therefore not excluded by that demonstration alone. Future tests must predeclare a minimum delivered-energy target and continuously integrate isolated load voltage/current while also measuring external electrical, mechanical and storage-energy terms. M2 baseline remains unchanged.'''
)

append_block(
    "docs/M6_REPLICATION_STATUS.md",
    "## V4.13 M6b load-duration evidence boundary",
    r'''## V4.13 M6b load-duration evidence boundary

Holzherr's 1999 M6b source must be represented as two separate time statements: the ~50-cm machine reportedly ran throughout an approximately 1.5-hour visit, while the named 1000-W lamp was connected for only about 10 seconds. The report does not establish a 1.5-hour 1-kW load test.

Holzherr also says he could not judge whether hidden flat batteries could account for the operation and that the protected 50-cm machine could not be lifted. His observation that running machines could be lifted applies to separate ~12-cm small models.

For M6 replication/metrology, load tests must therefore use integrated `V(t)*I(t)` energy and a separately bounded initial storage reservoir. Brightness, heater temperature, rotor runtime and nameplate wattage are supporting observations, not substitutes for a closed energy ledger.'''
)

append_block(
    "docs/research/experiment-plan.md",
    "## V4.13 — loaded-energy challenge",
    r'''## V4.13 — loaded-energy challenge

Define a minimum **energy** challenge before any source claim. Continuous isolated logging must integrate

`E_load = integral(V_load(t) * I_load(t) dt)`.

Simultaneously bound external electrical input, mechanical work and storage change. Useful benchmark energies:

- 100 W x 10 s = 0.278 Wh;
- 100 W x 1 min = 1.67 Wh;
- 100 W x 1 h = 100 Wh;
- 1 kW x 10 s = 2.78 Wh;
- 1 kW x 1.5 h = 1.5 kWh.

The run should continue until delivered load energy materially exceeds the independently measured/bounded initial storage reservoir if the goal is to exclude finite storage. Rotor runtime without a characterized load is not a substitute for this test.'''
)

append_tsv_rows(
    "docs/research/evidence_matrix.tsv",
    [
        "M6b running-vs-load duration\tHans Holzherr 1999 report preserved by Rimstar/Novak\t50-cm machine reportedly ran during ~1.5h visit; explicitly named 1000-W lamp connected ~10s\tP1 SOURCE-STATED / duration separation\tdo not infer 1.5kWh; integrate actual load V-I energy",
        "M6b hidden-battery judgment\tHans Holzherr 1999 follow-up Q&A\twhen asked whether hidden flat batteries could explain operation, Holzherr says he cannot judge that\tP1 observer limitation\tfinite storage remains open; social plausibility argument is not metrology",
        "M6b protected base inspection limit\tHans Holzherr 1999 report\t50-cm machine could not be touched or lifted; base only appeared solid\tP1 OBSERVATION\tdo not use M4 liftability to clear M6b base/internal storage",
        "M6b 10s lamp rating-equivalent energy\tHolzherr load description + V4.13 derivation\t1000W nameplate x 10s = 10kJ = 2.78Wh if full rated real power was actually delivered\tDERIVED CONTROL\tshort burst is energy-wise compatible with finite storage; actual real power remains unmeasured in source",
        "M5 continuous-hours wording\tSchneider/Weber 1984 account later NET-Journal reproduction\t~300V/10A output statement is followed by Baumann-attributed claim of continuous hours/years; witnessed lamp/heater effects are short qualitative observations\tH1/P1 SOURCE-SEPARATION\tdo not convert operator duration claim into observed long-duration load metrology",
        "V4.13 10kJ electrostatic storage bound\tE=1/2CV2 derivation\t10kJ requires ideally 2uF at 100kV or 22.2uF at 30kV\tDERIVED CONTROL\tmeasure original-like storage C/V before excluding finite electrostatic storage",
    ],
)

append_block(
    "STATE.md",
    "## V4.13 — load-duration and finite-storage bound — 2026-08-18",
    r'''## V4.13 — load-duration and finite-storage bound — 2026-08-18

V4.13 directly tightens the unresolved energy-source question. The best recovered Holzherr M6b duration evidence does **not** show a 1000-W load for 1.5 hours: the machine reportedly ran for ~1.5 h, while the 1000-W lamp was connected for ~10 s. Holzherr explicitly says he cannot judge whether hidden flat batteries could account for the operation, and the protected 50-cm machine could not be lifted.

If full lamp rating were actually delivered, 1 kW x 10 s is only 10 kJ = 2.78 Wh. In contrast, 1 kW x 1.5 h would be 1.5 kWh, a factor 540 larger. The historical source does not establish the latter. A 10-kJ electrostatic store would require ideally ~2 uF at 100 kV or ~22.2 uF at 30 kV; exact M6b storage values are unknown.

Finite storage therefore moves upward as an unresolved conventional candidate for short demonstrations. This is not a fraud allegation. The correct discriminator is continuous integrated load energy compared with all incoming electrical/mechanical power and storage-state change. M2 historical baseline remains unchanged.'''
)

append_block(
    "addon.md",
    "## V4.13 handoff — load duration versus stored energy — 2026-08-18",
    r'''## V4.13 handoff — load duration versus stored energy — 2026-08-18

Read `docs/research/load-duration-storage-audit-2026-08-18.md` before making stronger energy-source claims. The key correction is that Holzherr's M6b machine reportedly ran for ~1.5 h, but the 1000-W lamp was connected only ~10 s. At full rating that is just 2.78 Wh, and Holzherr explicitly said he could not judge the hidden-battery question. The 50-cm base was not cleared by lifting; liftability applied to separate ~12-cm models.

Next work should prioritize a minimum loaded-energy challenge and full storage inventory, not just instantaneous power or autonomous rotor runtime.'''
)

append_block(
    "CHANGELOG.md",
    "### V4.13 load-duration / finite-storage audit — 2026-08-18",
    r'''### V4.13 load-duration / finite-storage audit — 2026-08-18

- separated historical machine-running duration from load-connected duration and operator continuity claims;
- recorded Holzherr M6b ~1.5-h running versus ~10-s 1000-W lamp description and his explicit inability to judge the hidden-battery question;
- added deterministic load-energy, Wh/runtime and capacitor-storage calculations with regression tests;
- quantified the 10-s 1-kW rating-equivalent as 10 kJ / 2.78 Wh rather than 1.5 kWh;
- added ideal electrostatic storage requirements at 30 kV and 100 kV;
- kept finite internal storage as an unresolved conventional explanation without asserting fraud;
- left M2 historical topology unchanged.'''
)

print("V4.13 load-duration/storage findings integrated idempotently.")
