#!/usr/bin/env python3
"""M2 V4.31: pot-envelope reservoir and buffer feasibility bounds.

This module uses the current V4 research-CAD pot envelope as a geometric working
model.  Those dimensions are reconstruction values, not recovered historical
measurements.  The calculator asks three separate questions:

1. how much exposed cylindrical envelope area exists for a hypothetical surface
   process;
2. how much energy density a finite reservoir would need if it were confined to
   the two visible pot envelopes;
3. whether the simple visible grid/dielectric/spiral geometry could itself hide a
   10-kJ electrostatic buffer.

No anomalous source, hidden battery, specific chemistry, or historical capacitor
construction is asserted.
"""
from __future__ import annotations

import argparse
import math

EPS0_F_M = 8.8541878128e-12

# Current V4 research-CAD working dimensions; not primary-source measurements.
POT_OD_M = 0.084
POT_H_M = 0.110
GRID_ENVELOPE_D_M = 0.074
GRID_H_M = 0.096
SPIRAL_ENVELOPE_D_M = 0.042
SPIRAL_H_M = 0.088
POT_COUNT = 2


def _positive(name: str, value: float) -> float:
    if value <= 0.0:
        raise ValueError(f"{name} must be > 0")
    return value


def cylinder_lateral_area_m2(diameter_m: float, height_m: float) -> float:
    return math.pi * _positive("diameter_m", diameter_m) * _positive("height_m", height_m)


def cylinder_volume_m3(diameter_m: float, height_m: float) -> float:
    d = _positive("diameter_m", diameter_m)
    return math.pi * (d / 2.0) ** 2 * _positive("height_m", height_m)


def two_pot_electrode_envelope_area_m2() -> float:
    """Generous sum of grid-cylinder + spiral-envelope lateral areas for both pots."""
    one = cylinder_lateral_area_m2(GRID_ENVELOPE_D_M, GRID_H_M)
    one += cylinder_lateral_area_m2(SPIRAL_ENVELOPE_D_M, SPIRAL_H_M)
    return POT_COUNT * one


def two_pot_bounding_volume_m3() -> float:
    """External cylinder-envelope volume, larger than actual free/internal volume."""
    return POT_COUNT * cylinder_volume_m3(POT_OD_M, POT_H_M)


def recharge_power_w(energy_j: float, recharge_s: float) -> float:
    return _positive("energy_j", energy_j) / _positive("recharge_s", recharge_s)


def required_surface_power_density_w_m2(power_w: float, active_area_m2: float) -> float:
    return _positive("power_w", power_w) / _positive("active_area_m2", active_area_m2)


def required_area_multiplier(power_w: float, benchmark_power_density_w_m2: float, envelope_area_m2: float) -> float:
    required_area = _positive("power_w", power_w) / _positive(
        "benchmark_power_density_w_m2", benchmark_power_density_w_m2
    )
    return required_area / _positive("envelope_area_m2", envelope_area_m2)


def reservoir_energy_density_wh_l(energy_j: float, volume_m3: float) -> float:
    energy_wh = _positive("energy_j", energy_j) / 3600.0
    volume_l = _positive("volume_m3", volume_m3) * 1000.0
    return energy_wh / volume_l


def coax_capacitance_f(length_m: float, inner_radius_m: float, outer_radius_m: float, relative_permittivity: float = 1.0) -> float:
    """Ideal full-cylinder coaxial capacitance.

    Using the spiral envelope as a solid inner cylinder and a fully filled dielectric
    makes this an optimistic comparison for the sparse historical grid/spiral form.
    """
    length = _positive("length_m", length_m)
    a = _positive("inner_radius_m", inner_radius_m)
    b = _positive("outer_radius_m", outer_radius_m)
    if b <= a:
        raise ValueError("outer_radius_m must be > inner_radius_m")
    er = _positive("relative_permittivity", relative_permittivity)
    return 2.0 * math.pi * EPS0_F_M * er * length / math.log(b / a)


def two_pot_optimistic_capacitance_f(relative_permittivity: float = 3.0) -> float:
    # V4 envelope: spiral outer radius ~21 mm, grid inner-envelope radius ~35 mm.
    one = coax_capacitance_f(
        length_m=SPIRAL_H_M,
        inner_radius_m=SPIRAL_ENVELOPE_D_M / 2.0,
        outer_radius_m=0.035,
        relative_permittivity=relative_permittivity,
    )
    return POT_COUNT * one


def capacitor_energy_j(capacitance_f: float, voltage_v: float) -> float:
    return 0.5 * _positive("capacitance_f", capacitance_f) * _positive("voltage_v", voltage_v) ** 2


def required_capacitance_f(energy_j: float, voltage_v: float) -> float:
    return 2.0 * _positive("energy_j", energy_j) / _positive("voltage_v", voltage_v) ** 2


def capacitance_gap_factor(energy_j: float, voltage_v: float, available_capacitance_f: float) -> float:
    return required_capacitance_f(energy_j, voltage_v) / _positive(
        "available_capacitance_f", available_capacitance_f
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--burst-energy", type=float, default=10_000.0)
    parser.add_argument("--recharge-time", type=float, default=5_400.0)
    parser.add_argument("--benchmark-density", type=float, default=6.7)
    parser.add_argument("--er", type=float, default=3.0)
    args = parser.parse_args()

    area = two_pot_electrode_envelope_area_m2()
    volume = two_pot_bounding_volume_m3()
    p_recharge = recharge_power_w(args.burst_energy, args.recharge_time)
    c_pair = two_pot_optimistic_capacitance_f(args.er)

    print("M2 V4.31 pot-envelope reservoir/buffer bound")
    print("NOTE: V4 CAD dimensions are working reconstruction values, not primary measurements.")
    print(f"two-pot electrode-envelope area = {area:.6g} m^2")
    print(f"two-pot external bounding volume = {volume * 1000.0:.6g} L")
    print(f"recharge power for {args.burst_energy:.6g} J over {args.recharge_time:.6g} s = {p_recharge:.6g} W")
    print(f"required surface density over that envelope = {required_surface_power_density_w_m2(p_recharge, area):.6g} W/m^2")
    print(f"area multiplier versus {args.benchmark_density:.6g} W/m^2 benchmark = {required_area_multiplier(p_recharge, args.benchmark_density, area):.6g}x")
    print(f"energy density if burst energy were confined to pot bounding volume = {reservoir_energy_density_wh_l(args.burst_energy, volume):.6g} Wh/L")
    print(f"optimistic two-pot coax comparison capacitance (er={args.er:.6g}) = {c_pair:.6g} F")
    for voltage in (300.0, 10e3, 50e3, 100e3):
        e_available = capacitor_energy_j(c_pair, voltage)
        gap = capacitance_gap_factor(args.burst_energy, voltage, c_pair)
        print(f"{voltage:.6g} V: E_simple-pot={e_available:.6g} J, C-gap for burst={gap:.6g}x")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
