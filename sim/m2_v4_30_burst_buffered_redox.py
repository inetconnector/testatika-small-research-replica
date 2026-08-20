#!/usr/bin/env python3
"""M2 V4.30: burst-buffered distributed-redox scale model.

This module does not claim that the historical Testatika used chemistry, a dry
pile, copper oxide, or any specific rectifier material.  It quantifies a narrower
hypothesis: a finite matter reservoir could recharge an electrostatic/HV buffer
slowly while the observed load was applied only in short bursts.

The functions intentionally separate:
- burst energy and average recharge power,
- active-material specific-energy scale,
- buffer capacitance scale,
- source current versus source voltage,
- series-cell voltage stacking.
"""
from __future__ import annotations

import argparse
import math


AL_AIR_PRACTICAL_COMPARISON_WH_KG = 1878.0
CU_TO_CUO_THEORETICAL_WH_KG = 560.8010994660035
CU_TO_CU2O_THEORETICAL_WH_KG = 323.2260444752183


def _positive(name: str, value: float) -> float:
    if value <= 0.0:
        raise ValueError(f"{name} must be > 0")
    return value


def burst_energy_j(power_w: float, duration_s: float) -> float:
    return _positive("power_w", power_w) * _positive("duration_s", duration_s)


def burst_energy_wh(power_w: float, duration_s: float) -> float:
    return burst_energy_j(power_w, duration_s) / 3600.0


def average_recharge_power_w(energy_j: float, recharge_s: float) -> float:
    return _positive("energy_j", energy_j) / _positive("recharge_s", recharge_s)


def active_mass_kg(energy_wh: float, specific_energy_wh_kg: float) -> float:
    return _positive("energy_wh", energy_wh) / _positive(
        "specific_energy_wh_kg", specific_energy_wh_kg
    )


def required_buffer_capacitance_f(energy_j: float, voltage_v: float) -> float:
    """Ideal capacitance with 1/2*C*V^2 equal to the requested energy.

    This is an upper-level energy-scale calculation only.  A real capacitor cannot
    normally be discharged from V to zero while maintaining constant load power;
    dielectric, ESR, voltage rating, leakage, and safe clearances are omitted.
    """
    return 2.0 * _positive("energy_j", energy_j) / _positive("voltage_v", voltage_v) ** 2


def source_current_a(power_w: float, source_voltage_v: float) -> float:
    return _positive("power_w", power_w) / _positive("source_voltage_v", source_voltage_v)


def cells_in_series(target_voltage_v: float, cell_voltage_v: float) -> int:
    return math.ceil(_positive("target_voltage_v", target_voltage_v) / _positive("cell_voltage_v", cell_voltage_v))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--burst-power", type=float, default=1000.0)
    parser.add_argument("--burst-duration", type=float, default=10.0)
    parser.add_argument("--recharge-time", type=float, default=5400.0)
    args = parser.parse_args()

    e_j = burst_energy_j(args.burst_power, args.burst_duration)
    e_wh = e_j / 3600.0
    print("M2 V4.30 burst-buffered distributed-redox scale")
    print(f"burst = {args.burst_power:.6g} W x {args.burst_duration:.6g} s")
    print(f"burst energy = {e_j:.6g} J = {e_wh:.6g} Wh")
    print(f"average recharge power over {args.recharge_time:.6g} s = {average_recharge_power_w(e_j, args.recharge_time):.6g} W")
    print()
    print("active-material comparison for one burst")
    for label, spec in (
        ("Al-air practical comparison", AL_AIR_PRACTICAL_COMPARISON_WH_KG),
        ("Cu -> CuO thermodynamic ceiling", CU_TO_CUO_THEORETICAL_WH_KG),
        ("Cu -> Cu2O thermodynamic ceiling", CU_TO_CU2O_THEORETICAL_WH_KG),
    ):
        print(f"{label}: {1e3 * active_mass_kg(e_wh, spec):.6g} g")
    print()
    print("ideal buffer-C scale for the burst energy")
    for voltage in (300.0, 10e3, 50e3, 100e3):
        print(f"{voltage:.6g} V -> {required_buffer_capacitance_f(e_j, voltage):.6g} F")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
