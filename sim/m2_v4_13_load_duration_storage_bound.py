#!/usr/bin/env python3
"""V4.13 load-duration and finite-storage bounds.

Historical demonstrations often mix three different statements:

1. how long a machine was seen rotating;
2. how long a load was visibly connected;
3. the load's nameplate/rated power or an operator power claim.

Those are not interchangeable. This module converts observed/claimed load
intervals into energy requirements and asks whether finite stored energy remains
a conventional explanation. It does not assert fraud, batteries, or anomalous
energy in any historical machine.
"""

from __future__ import annotations

import math


def energy_j(power_w: float, duration_s: float) -> float:
    """Energy corresponding to constant real power over a duration."""
    if power_w < 0 or duration_s < 0:
        raise ValueError("power and duration must be non-negative")
    return power_w * duration_s


def joules_to_wh(energy_joules: float) -> float:
    if energy_joules < 0:
        raise ValueError("energy must be non-negative")
    return energy_joules / 3600.0


def wh_to_j(energy_wh: float) -> float:
    if energy_wh < 0:
        raise ValueError("energy must be non-negative")
    return energy_wh * 3600.0


def required_capacitance_for_energy(energy_joules: float, voltage_v: float) -> float:
    """Capacitance from E = 1/2 C V^2."""
    if energy_joules < 0:
        raise ValueError("energy must be non-negative")
    if voltage_v <= 0:
        return math.inf
    return 2.0 * energy_joules / voltage_v**2


def capacitor_energy_j(capacitance_f: float, voltage_v: float) -> float:
    if capacitance_f < 0:
        raise ValueError("capacitance must be non-negative")
    return 0.5 * capacitance_f * voltage_v**2


def runtime_s(storage_energy_j: float, load_power_w: float, efficiency: float = 1.0) -> float:
    """Idealized runtime from finite storage at constant load.

    efficiency is output energy / storage energy and is bounded (0, 1].
    """
    if storage_energy_j < 0 or load_power_w < 0:
        raise ValueError("energy and power must be non-negative")
    if load_power_w == 0:
        return math.inf
    if efficiency <= 0 or efficiency > 1:
        return 0.0
    return efficiency * storage_energy_j / load_power_w


def storage_wh_required(load_power_w: float, duration_s: float, efficiency: float = 1.0) -> float:
    if load_power_w < 0 or duration_s < 0:
        raise ValueError("power and duration must be non-negative")
    if efficiency <= 0 or efficiency > 1:
        return math.inf
    return joules_to_wh(energy_j(load_power_w, duration_s) / efficiency)


def main() -> None:
    # Historical-control examples only. The 1000-W lamp figure is a lamp rating
    # in the Holzherr report, not a calibrated simultaneous V*I measurement.
    lamp_rating_w = 1000.0
    lamp_interval_s = 10.0
    seen_running_s = 1.5 * 3600.0

    e_lamp = energy_j(lamp_rating_w, lamp_interval_s)
    print("V4.13 load-duration / finite-storage bounds")
    print(f"1000-W rating-equivalent for 10 s: {e_lamp:.6g} J = {joules_to_wh(e_lamp):.6g} Wh")
    print(f"1000 W sustained for 1.5 h: {joules_to_wh(energy_j(lamp_rating_w, seen_running_s)):.6g} Wh")
    print("These two quantities must not be conflated; the report states ~1.5 h running but ~10 s lamp connection.")

    for voltage in (30e3, 100e3):
        c = required_capacitance_for_energy(e_lamp, voltage)
        print(f"electrostatic C for 10 kJ at {voltage/1000:g} kV: {c:.6g} F")

    for p, t in ((100.0, 10.0), (100.0, 60.0), (100.0, 3600.0), (1000.0, 10.0), (1000.0, 5400.0)):
        e = energy_j(p, t)
        print(f"{p:g} W for {t:g} s -> {e:.6g} J = {joules_to_wh(e):.6g} Wh")


if __name__ == "__main__":
    main()
