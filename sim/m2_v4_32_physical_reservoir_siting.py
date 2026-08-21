#!/usr/bin/env python3
"""V4.32 physical reservoir siting / energy-density discriminator.

This module does not assert that any historical Testatika contained a hidden battery,
active base, electrochemical reservoir, or anomalous energy source. It compares the
working CAD envelopes of several M2/M6 locations against finite-energy requirements.

Machine-family boundaries are mandatory:
- M2 dimensions are current research-CAD working values, not original measurements.
- M6 values are current M6 V1/V2 reconstruction envelopes.
- The large-family active-base clue is a low/medium-confidence relay and must never be
  transferred into M2 as a historical fact.
"""
from __future__ import annotations

import math

EPS0 = 8.8541878128e-12


def _positive(name: str, value: float) -> float:
    if value <= 0:
        raise ValueError(f"{name} must be > 0")
    return value


def cylinder_volume_l(diameter_m: float, height_m: float, count: int = 1) -> float:
    d = _positive("diameter_m", diameter_m)
    h = _positive("height_m", height_m)
    if count < 1:
        raise ValueError("count must be >= 1")
    return count * math.pi * (d / 2.0) ** 2 * h * 1000.0


def box_volume_l(width_m: float, depth_m: float, height_m: float, count: int = 1) -> float:
    w = _positive("width_m", width_m)
    d = _positive("depth_m", depth_m)
    h = _positive("height_m", height_m)
    if count < 1:
        raise ValueError("count must be >= 1")
    return count * w * d * h * 1000.0


def energy_density_wh_l(energy_wh: float, volume_l: float) -> float:
    return _positive("energy_wh", energy_wh) / _positive("volume_l", volume_l)


def dielectric_energy_density_j_m3(er: float, field_v_m: float) -> float:
    """Ideal linear-dielectric field-energy density: 0.5*eps0*er*E^2.

    This is an energy-scale bound, not a safe operating recommendation. Real materials
    have breakdown, partial-discharge, edge-field, heating, ageing and leakage limits.
    """
    return 0.5 * EPS0 * _positive("er", er) * _positive("field_v_m", field_v_m) ** 2


def dielectric_energy_j(volume_l: float, er: float, field_v_m: float) -> float:
    return dielectric_energy_density_j_m3(er, field_v_m) * _positive("volume_l", volume_l) / 1000.0


def multilayer_parallel_capacitance_f(
    sheet_count: int,
    sheet_diameter_m: float,
    gap_m: float,
    er: float = 3.0,
    active_area_fraction: float = 1.0,
) -> float:
    """Favourable alternating-sheet parallel-capacitance estimate.

    Each adjacent gap is treated as a capacitor in parallel between two alternating
    electrode buses. Full circular sheet area is available when active_area_fraction=1.
    This is deliberately generous for a perforated historical stack.
    """
    if sheet_count < 2:
        raise ValueError("sheet_count must be >= 2")
    if not 0 < active_area_fraction <= 1:
        raise ValueError("active_area_fraction must be in (0, 1]")
    area = math.pi * (_positive("sheet_diameter_m", sheet_diameter_m) / 2.0) ** 2
    area *= active_area_fraction
    gaps = sheet_count - 1
    return gaps * EPS0 * _positive("er", er) * area / _positive("gap_m", gap_m)


def stored_energy_j(capacitance_f: float, voltage_v: float) -> float:
    return 0.5 * _positive("capacitance_f", capacitance_f) * _positive("voltage_v", voltage_v) ** 2


def canonical_site_volumes_l() -> dict[str, float]:
    """Working reconstruction-envelope volumes, not historical metrology."""
    return {
        # M2 V4 working CAD
        "M2 two side-pot external envelopes": cylinder_volume_l(0.084, 0.110, 2),
        "M2 top-carrier bounding box": box_volume_l(0.170, 0.028, 0.018),
        "M2 lower-cage bounding box": box_volume_l(0.024, 0.018, 0.070),
        "M2 rotor-disc gross PMMA volume": cylinder_volume_l(0.200, 0.0035),
        "M2 base gross working envelope": box_volume_l(0.370, 0.180, 0.030),
        # M6 V1/V2 working CAD
        "M6 two large-cylinder external envelopes": cylinder_volume_l(0.146, 0.235, 2),
        "M6 two capacitor-can external envelopes": (
            cylinder_volume_l(0.078, 0.112) + cylinder_volume_l(0.062, 0.092)
        ),
        "M6 base gross working envelope": box_volume_l(0.760, 0.340, 0.028),
    }


def main() -> int:
    sites = canonical_site_volumes_l()
    targets = {
        "1 kW x 10 s burst": 10000.0 / 3600.0,
        "100 W x 1.5 h": 150.0,
        "1 kW x 1.5 h": 1500.0,
    }
    print("V4.32 physical reservoir siting discriminator")
    for name, volume_l in sites.items():
        print(f"\n{name}: {volume_l:.6g} L")
        for label, e_wh in targets.items():
            print(f"  {label}: {energy_density_wh_l(e_wh, volume_l):.6g} Wh/L")

    caps_l = sites["M6 two capacitor-can external envelopes"]
    for field in (30e6, 100e6):
        e = dielectric_energy_j(caps_l, 3.0, field)
        print(f"\nIdeal er=3 field energy filling BOTH M6 can envelopes at {field/1e6:.0f} MV/m: {e:.6g} J")

    c20 = multilayer_parallel_capacitance_f(20, 0.078, 1e-3, er=3.0)
    print(f"\n20-sheet, 78-mm, 1-mm-gap full-area favourable stack: C = {c20:.6g} F")
    print(f"At field-limited 30 MV/m across each 1-mm gap: E = {stored_energy_j(c20, 30e3):.6g} J")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
