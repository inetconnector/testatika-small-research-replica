#!/usr/bin/env python3
"""Integrate Round-11 environmental-source bounds into canonical research state.

Idempotent by section markers / first-column TSV keys. The script intentionally
adds no RF/Tesla/resonance hardware to the M2 historical baseline.
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
    "## Internet source audit round 11 — 2026-08-18",
    r'''## Internet source audit round 11 — 2026-08-18

Canonical Round-11 records:

- [`internet-source-audit-round11-2026-08-18.md`](internet-source-audit-round11-2026-08-18.md)
- [`internet-source-ledger-round11.tsv`](internet-source-ledger-round11.tsv)
- [`m2-v4-11-environmental-port-survey.md`](m2-v4-11-environmental-port-survey.md)

High-value consequences:

1. **Linden 80–140 MHz correction:** the preserved second-hand Linden letter contains the reported ~700-V demonstration but no 80–140-MHz operating frequency. That number enters through Potter's later back-engineering and must not be presented as Baumann/Linden source-stated fact.
2. **Independent Linden controls:** Rimstar/Dufresne Series 1–3 failed to reproduce the reported 700-V effect. Finger-held plates produced a small body/contact-dependent reading that vanished with a plastic clamp; powered UHF/HV variants produced only ordinary small induced/rectified outputs at microamp scale.
3. **Atmospheric fair-weather current bound:** even granting the full ~250-kV ionosphere-ground potential at ~2 pA/m² gives only ~0.5 microW/m², requiring ~200 km² ideal capture area for 100 W. Local tabletop fair-weather power density is still much smaller.
4. **50-Hz capacitive pickup bound:** with the V4.10 working `Ceq=50 pF`, `h=0.20 m`, a 100-V/m room field gives only ~6.3 microW; 100 W would require ~399 kV/m at 50 Hz.
5. **Ambient RF bound:** at a high measured-average example around 200 microW/m², 100 W would require ~0.5 km² ideal aperture before receiver losses.
6. **Schumann/ELF bound:** pT/sub-mV-m natural fields are many orders below a tabletop 100-W reservoir; they remain possible timing/noise/reference signals, not bulk power.
7. **Geomagnetic bound:** a 200-mm one-turn loop at 60 rpm in ~50 microtesla has only ~9.9 microV optimistic peak Faraday EMF; ordinary generation still requires mechanical work.

Round 11 therefore narrows the conventional bulk-source search to overlooked local galvanic/base/table/chassis paths, a strong local near-field transmitter/coupler, mechanical work, finite stored energy, or historical output-estimation error. Resonance/tuning remains a conditioning hypothesis, not an energy source. No M2 historical CAD/electrical baseline changes.'''
)

append_block(
    "docs/REPLICATION_STATUS.md",
    "## V4.11 environmental-port discrimination",
    r'''## V4.11 environmental-port discrimination

V4.11 adds a **measurement/calculation layer only**. It does not alter the current M2 historical topology.

The new survey quantitatively rejects several tempting ordinary environmental reservoirs as ~100-W tabletop bulk sources under deliberately optimistic assumptions:

- fair-weather global-electric-circuit conduction;
- ordinary 50-Hz room-field pickup through pF-scale coupling;
- typical ambient broadcast/cellular/Wi-Fi RF;
- ordinary Schumann/ELF background;
- Earth's static magnetic field as an independent source.

A key provenance correction also prevents an HF reconstruction error: the preserved Linden-Experiment relay reports the ~700-V claim but **does not state 80–140 MHz**. The 80–140-MHz number belongs to Potter's later reconstruction.

The M2 baseline therefore remains unchanged: floating rotor wires, two-terminal side pots, Crystal black box, no rubbing contacts, no conventional built-in motor and no Tesla/HF historical stage. V4.11 instead strengthens the requirement to instrument base/table/chassis, front/rear field, mechanical and stored-energy ports simultaneously.'''
)

append_block(
    "docs/M6_REPLICATION_STATUS.md",
    "## Round 11 environmental-power boundary",
    r'''## Round 11 environmental-power boundary

The large/workshop source lines retain legitimate historical clues involving magnetized pickups, magnetic synchronization, resonance/tuning language and atmosphere/lightning analogies. Round 11 separates those clues from the power-source question.

Quantitative controls show that ordinary fair-weather atmospheric conduction, normal ambient RF, Schumann/ELF background and Earth's static magnetic field are far too small to provide sustained ~100-W tabletop power. A resonant or magnetically biased stage can transform impedance, establish phase and increase circulating reactive energy, but cannot supply missing real power.

For M6/M7-family experiments, the highest-priority conventional alternatives are therefore an electrically active base/table/chassis path, a strong local near-field coupler/transmitter, mechanical drive, or finite stored energy. None is promoted to historical fact without source or measurement evidence.'''
)

append_block(
    "docs/research/experiment-plan.md",
    "## V4.11 — environmental input-port discrimination",
    r'''## V4.11 — environmental input-port discrimination

Purpose: falsify candidate bulk-input paths **before** optimizing any apparent output.

For a passive or current-limited low-energy fixture, log simultaneously:

- front/rear/base/chassis differential potentials and displacement currents;
- wideband local E- and B-field spectra;
- any mechanical shaft torque/power;
- charge/storage energy before and after each run;
- load voltage/current using isolated differential instrumentation;
- conductive versus nonconductive rear/base shield controls, with capacitance changes measured separately.

The energy criterion is source-side, not resonance-amplitude based: a sustained conventional 100-W load requires real incoming power of the same order. A high-Q voltage/current peak without corresponding source real power is not a source mechanism.

Historical-control requirement: do not set an `80–140 MHz Linden` operating point as source-derived. If frequency sweeps are used, declare them laboratory scans and preserve source provenance separately.'''
)

append_tsv_rows(
    "docs/research/evidence_matrix.tsv",
    [
        "Linden 700-V relay without frequency\tRimstar preservation of second-hand Linden letter\tU-shaped wound magnet with closed wire loop + insulated plate sandwich; ~700 V reported; preserved relay contains no 80-140-MHz operating-frequency statement\tH2 / SOURCE-CORRECTION\tpreserve 700-V claim as hearsay; never encode 80-140 MHz as Baumann/Linden source-stated frequency",
        "Linden 80-140-MHz provenance\tPaul E. Potter later Testatika back-engineering\tPotter says Linden was thought to register ~80-140 MHz and builds an HF/electron-cascade theory around it\tS2/I1\tlater reconstruction only; explicit comparison hypothesis, not M2/M0b historical baseline",
        "Rimstar Linden finger-control\tSteven Dufresne Series 1\t~0.54-V finger-held reading also away from magnet; plastic clamp reduces reading to zero\tR1 CONTROL\tbody/contact/probe/electrochemical artifact must be excluded in all Linden-style tests",
        "Rimstar powered-UHF Linden control\tSteven Dufresne Series 2\t280-425-MHz powered sweep fails to reproduce Linden-scale effect; changed circuits yield only small induced/rectified voltages at microamp scale\tR1 CONTROL\tfrequency selectivity is compatible with ordinary induction/rectification; source oscillator power must be in ledger",
        "Rimstar HV-pulse conversion control\tSteven Dufresne Series 3\tHV spikes convert to low-voltage DC around 0.1 V and microamp current\tR1 CONTROL\tdemonstrates conventional pulse-energy conversion, not anomalous source",
        "Fair-weather atmosphere 100-W bound\tAGU global-electric-circuit literature + V4.11 derivation\t2 pA/m2 x 250 kV = 0.5 microW/m2 optimistic full-column density; 100 W requires ~200 km2 ideal area\tSCIENTIFIC CONTROL / DERIVED\tatmospheric conduction may bias charge state but is excluded as direct tabletop bulk source",
        "50-Hz pF-coupling 100-W bound\tWHO field scale + V4.10/V4.11 equation\tCeq=50 pF, h=0.20 m, E=100 V/m gives ~6.3 microW; 100 W requires ~399 kV/m at 50 Hz\tSCIENTIFIC CONTROL / DERIVED\tordinary room-field pickup excluded; test hidden galvanic/base/table path separately",
        "Ambient-RF 100-W aperture bound\tSensors 2021 field survey + V4.11 derivation\t~200 microW/m2 high measured-average example implies ~500000 m2 ideal aperture for 100 W\tSCIENTIFIC CONTROL / DERIVED\ttypical ambient RF excluded as tabletop bulk source; strong local near-field source remains separately testable",
        "Schumann-ELF bulk-power bound\tRadio Science pT/sub-mV-m measurements + V4.11 proxy\tE*B/mu0 order proxy ~1.6e-10 W/m2; 100-W ideal-area scale ~6.3e11 m2\tSCIENTIFIC CONTROL / DERIVED\tELF may be timing/reference/noise, not ordinary bulk source",
        "Geomagnetic 200-mm loop bound\t~50-uT Earth field + Faraday derivation\t200-mm one-turn loop at 60 rpm gives ~9.9 microV optimistic peak EMF; 24 ideal turns ~0.237 mV\tSCIENTIFIC CONTROL / DERIVED\tgeomagnetic bias remains test variable; loaded generation requires mechanical work",
    ],
)

append_block(
    "STATE.md",
    "## V4.11 / Internet audit round 11 — environmental source discrimination — 2026-08-18",
    r'''## V4.11 / Internet audit round 11 — environmental source discrimination — 2026-08-18

Canonical files: `docs/research/internet-source-audit-round11-2026-08-18.md`, `internet-source-ledger-round11.tsv`, `docs/research/m2-v4-11-environmental-port-survey.md`, `sim/m2_v4_11_environmental_port_survey.py`.

Round 11 makes one major provenance correction and one major physical narrowing. The preserved second-hand Linden relay contains the ~700-V claim but **no 80–140-MHz operating-frequency statement**; that frequency belongs to Potter's later back-engineering. Rimstar's controlled replication series did not reproduce the Linden-scale effect and exposed body/contact bias plus ordinary powered-UHF/HV induction/rectification at tiny power scales.

Quantitatively, ordinary fair-weather atmospheric conduction, ordinary 50-Hz room-field pickup through pF-scale coupling, typical ambient RF, Schumann/ELF background and Earth's static magnetic field are all orders of magnitude too small to explain a sustained ~100-W tabletop load. Resonance, magnetization and nonlinear commutation may still be timing/impedance/field-conditioning mechanisms but are not thereby an energy source.

Remaining conventional bulk-source priorities: overlooked galvanic/base/table/chassis path; strong local near-field coupler/transmitter; mechanical input; finite stored electrostatic/electret/chemical energy; historical output-estimation error. Only a closed simultaneous input/output/storage balance can leave an unexplained residual.

M2 historical baseline is unchanged: no Tesla/HF stage is added.'''
)

append_block(
    "addon.md",
    "## V4.11 / Round 11 handoff — 2026-08-18",
    r'''## V4.11 / Round 11 handoff — 2026-08-18

Before continuing the environmental-source search, read `docs/research/m2-v4-11-environmental-port-survey.md` and `docs/research/internet-source-audit-round11-2026-08-18.md`.

Do not quote `80–140 MHz` as a Linden/Baumann source fact: the preserved relay has no such frequency; it is Potter's later reconstruction. Ordinary fair-weather current, normal ambient RF, Schumann background and the static geomagnetic field are quantitatively excluded as direct ~100-W tabletop bulk reservoirs. The next conventional search should instrument base/table/chassis, local near-field, mechanical and stored-energy ports rather than treating resonance amplitude as power input.'''
)

append_block(
    "CHANGELOG.md",
    "### V4.11 / Internet source audit round 11 — 2026-08-18",
    r'''### V4.11 / Internet source audit round 11 — 2026-08-18

- added a deterministic environmental-port power-bound calculator and regression tests;
- corrected the widely repeated `Linden 80–140 MHz` claim to Potter-later-secondary rather than source-stated Linden evidence;
- added Rimstar/Dufresne Linden replication controls showing body/contact bias and small conventional UHF/HV induction/rectification rather than the reported 700-V effect;
- bounded fair-weather atmospheric conduction, 50-Hz pF pickup, ambient RF, Schumann/ELF and geomagnetic induction against the ~100-W tabletop scale;
- narrowed the remaining conventional source search to local hidden electrical/near-field/mechanical/storage paths or historical output-estimation error;
- left the M2 historical CAD/electrical baseline unchanged.'''
)

print("Round 11 environmental-source audit integrated idempotently.")
