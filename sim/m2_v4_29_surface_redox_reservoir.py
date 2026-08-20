#!/usr/bin/env python3
"""M2 V4.29: field-gated surface-redox / moisture reservoir scale model.

This module does NOT assert that the historical Testatika used electrochemistry.
It asks whether a local matter reservoir (metal/oxide/water/oxygen interfaces)
can satisfy the real-power scale that ordinary ambient fields fail to reach.

The model separates:
- projected-area humidity harvesting power density,
- battery-like chemical specific energy,
- stoichiometric oxidant demand for an aluminum-air comparison.
"""
from __future__ import annotations

import argparse


def _positive(name: str, value: float) -> float:
    if value <= 0.0:
        raise ValueError(f"{name} must be > 0")
    return value


def required_area_m2(power_w: float, power_density_w_m2: float) -> float:
    return _positive("power_w", power_w) / _positive("power_density_w_m2", power_density_w_m2)


def required_fuel_mass_kg(power_w: float, duration_s: float, specific_energy_wh_kg: float) -> float:
    energy_wh = _positive("power_w", power_w) * _positive("duration_s", duration_s) / 3600.0
    return energy_wh / _positive("specific_energy_wh_kg", specific_energy_wh_kg)


def aluminum_oxygen_mass_kg(aluminum_mass_kg: float) -> float:
    """O2 mass for 4 Al + 3 O2 -> 2 Al2O3, ideal stoichiometry."""
    m_al = _positive("aluminum_mass_kg", aluminum_mass_kg)
    molar_al = 26.9815385
    molar_o2 = 31.9988
    return m_al * (3.0 * molar_o2) / (4.0 * molar_al)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--power", type=float, default=100.0)
    parser.add_argument("--duration", type=float, default=3600.0)
    parser.add_argument("--humidity-power-density", type=float, default=6.7)
    parser.add_argument("--al-air-specific-energy", type=float, default=1878.0)
    args = parser.parse_args()

    area = required_area_m2(args.power, args.humidity_power_density)
    mass = required_fuel_mass_kg(args.power, args.duration, args.al_air_specific_energy)
    oxygen = aluminum_oxygen_mass_kg(mass)

    print("M2 V4.29 surface-redox reservoir scale")
    print(f"target power = {args.power:.6g} W")
    print(f"duration = {args.duration:.6g} s")
    print(f"humidity-harvester comparison density = {args.humidity_power_density:.6g} W/m^2")
    print(f"required projected area = {area:.6g} m^2")
    print(f"Al-air comparison specific energy = {args.al_air_specific_energy:.6g} Wh/kg")
    print(f"required active-Al-equivalent mass = {mass:.6g} kg")
    print(f"ideal O2 demand for that Al mass = {oxygen:.6g} kg")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
