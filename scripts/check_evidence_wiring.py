#!/usr/bin/env python3
"""Structural and conventional-circuit sanity checks for the evidence wiring docs.

This does NOT simulate or validate a historical Testatika energy claim. It verifies that
our published W0/W1 documentation is internally consistent, machine-readable registries
parse cleanly, SVG drawings are valid XML, source-image families remain deduplicated, and
the passive rectifier/storage block used for the laboratory W1 variants is electrically
capable of producing DC from a differential pulsed/alternating input in an idealized
conventional model.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ELEC = ROOT / "docs" / "electrical"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"evidence-wiring validation failed: {message}")


def check_variant_registry() -> None:
    rows = read_tsv(ELEC / "WIRING_VARIANTS.tsv")
    ids = [r["variant"] for r in rows]
    require(len(ids) == len(set(ids)), "duplicate wiring variant ID")
    required = {
        "M2-W0", "M2-W1", "M2-W2", "M2-W3", "M2-W4",
        "M6-W0", "M6-W1", "M6-W2A", "M6-W2B", "M6-W3", "M6-W4", "M6-W5",
    }
    require(required.issubset(set(ids)), f"missing variants: {sorted(required - set(ids))}")
    for row in rows:
        require(row["evidence_class"], f"{row['variant']} has no evidence class")
        require(row["must_not_claim"], f"{row['variant']} lacks a claim boundary")


def check_source_image_registry() -> None:
    rows = read_tsv(ELEC / "SOURCE_IMAGE_FAMILIES.tsv")
    ids = [r["id"] for r in rows]
    require(len(ids) == len(set(ids)), "duplicate source-image family ID")
    require(len(rows) >= 13, "source-image census unexpectedly lost a distinct family")
    required_families = {
        "Albert Hauser drawing 3279 front/top/side/legend",
        "Don Kelly Magnets electro-schematic",
        "Paul E. Potter Full Circuit",
        "Sven Bönisch ELEKTRIE circuits",
        "Cathomen amateur workshop video",
        "Holzherr Principle Experiment drawing/report",
    }
    names = {r["family"] for r in rows}
    require(required_families.issubset(names),
            f"missing source-image families: {sorted(required_families - names)}")
    for row in rows:
        require(row["evidence_class"], f"{row['id']} has no evidence class")
        require(row["limitation"], f"{row['id']} lacks an evidence limitation")


def check_lamella_matrix() -> None:
    rows = read_tsv(ELEC / "LAMELLA_TEST_MATRIX.tsv")
    ids = [r["id"] for r in rows]
    require(len(ids) == len(set(ids)), "duplicate lamella test ID")
    require({"L02", "L03", "L04", "L05", "G00", "G01", "G03"}.issubset(set(ids)),
            "lamella matrix lost source-critical controls")
    states = {(r["material_or_geometry"], r["magnetization"]) for r in rows}
    require(any(m == "WEAK" for _, m in states), "no weak-magnetization test")
    require(any("SOLID FOIL" in r["perforation_surface"] for r in rows), "no foil control")
    require(any("WIRE MESH" in r["perforation_surface"] for r in rows), "no mesh control")


def check_svg() -> None:
    for name in ("M2_V5_EVIDENCE_WIRING.svg", "M6_V2_EVIDENCE_WIRING.svg"):
        path = ELEC / "diagrams" / name
        root = ET.parse(path).getroot()
        require(root.tag.endswith("svg"), f"{name} is not a valid SVG root")
        text = path.read_text(encoding="utf-8")
        require("OPEN" in text, f"{name} does not expose open/unknown boundary")
        require("W1" in text, f"{name} does not show W1 laboratory path")


def check_docs() -> None:
    m2 = (ELEC / "M2_V5_EVIDENCE_WIRING.md").read_text(encoding="utf-8")
    m6 = (ELEC / "M6_V2_EVIDENCE_WIRING.md").read_text(encoding="utf-8")
    for name, text in (("M2", m2), ("M6", m6)):
        require("W0" in text and "OPEN" in text, f"{name} missing open baseline")
        require("current-limited" in text or "strombegrenz" in text, f"{name} missing current limit")
        require("Energiebilanz" in text, f"{name} missing energy-accounting section")
        require("Oszilloskop" in text or "Scope" in text, f"{name} missing floating-scope warning")
    require("R01..R24" in m2, "M2 floating rotor node family missing")
    require("A1..A14" in m6, "M6 individual stator breakout missing")
    require("L-OG" in m6 and "R-OG" in m6, "M6 three-grid breakout missing")


def ideal_bridge_storage_sanity(v_peak: float, freq_hz: float, pulse_mode: bool = False) -> float:
    """Idealized bridge + storage C + load model in arbitrary safe simulation units.

    It intentionally models only a conventional rectifier/storage block. The electrostatic
    machine is represented by a prescribed differential waveform. Therefore a pass proves
    only that the documented output block is a coherent rectifier path.
    """
    c = 10e-6
    r_load = 100_000.0
    dt = 1.0 / (freq_hz * 2000.0)
    duration = 20.0 / freq_hz
    vc = 0.0
    diode_drop = 0.01 * v_peak
    steps = int(duration / dt)
    for i in range(steps):
        t = i * dt
        phase = 2.0 * math.pi * freq_hz * t
        if pulse_mode:
            raw = v_peak * (0.8 * math.sin(phase) + 0.35 * math.sin(2.0 * phase + 0.4))
        else:
            raw = v_peak * math.sin(phase)
        available = max(0.0, abs(raw) - 2.0 * diode_drop)
        if available > vc:
            vc = available
        else:
            vc *= math.exp(-dt / (r_load * c))
    return vc


def check_conventional_output_paths() -> None:
    m2_dc = ideal_bridge_storage_sanity(v_peak=100.0, freq_hz=20.0, pulse_mode=False)
    m6_dc = ideal_bridge_storage_sanity(v_peak=100.0, freq_hz=25.0, pulse_mode=True)
    require(m2_dc > 50.0, f"M2 W1 bridge/storage sanity failed: {m2_dc:.3f}")
    require(m6_dc > 40.0, f"M6 W1 bridge/storage sanity failed: {m6_dc:.3f}")
    print(f"M2 conventional bridge/storage sanity: {m2_dc:.2f} normalized V")
    print(f"M6 conventional bridge/storage sanity: {m6_dc:.2f} normalized V")


def main() -> None:
    check_variant_registry()
    check_source_image_registry()
    check_lamella_matrix()
    check_svg()
    check_docs()
    check_conventional_output_paths()
    print("Evidence wiring validation: OK")


if __name__ == "__main__":
    main()
