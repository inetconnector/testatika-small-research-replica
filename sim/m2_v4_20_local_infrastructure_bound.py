#!/usr/bin/env python3
"""V4.20 local-building / mains / accidental-coupling source diagnostic.

The model asks whether ordinary 230-V, 50-Hz building infrastructure can be the
missing real-power source through pF/nF stray capacitance. It deliberately grants
the full mains RMS voltage across the coupling as an optimistic upper bound.

This is not a historical M2 schematic and not a mains-powered build recipe.
All proposed physical follow-up remains isolated, current-limited and low voltage.
"""
from __future__ import annotations

import math


def _positive(x: float, name: str) -> None:
    if x <= 0.0:
        raise ValueError(f"{name} must be positive")


def capacitive_current_a(frequency_hz: float, capacitance_f: float, voltage_rms_v: float) -> float:
    _positive(frequency_hz, "frequency_hz")
    _positive(capacitance_f, "capacitance_f")
    _positive(abs(voltage_rms_v), "voltage_rms_v magnitude")
    return 2.0 * math.pi * frequency_hz * capacitance_f * abs(voltage_rms_v)


def capacitive_reactance_ohm(frequency_hz: float, capacitance_f: float) -> float:
    _positive(frequency_hz, "frequency_hz")
    _positive(capacitance_f, "capacitance_f")
    return 1.0 / (2.0 * math.pi * frequency_hz * capacitance_f)


def apparent_power_va(voltage_rms_v: float, current_rms_a: float) -> float:
    _positive(abs(voltage_rms_v), "voltage_rms_v magnitude")
    _positive(abs(current_rms_a), "current_rms_a magnitude")
    return abs(voltage_rms_v * current_rms_a)


def current_for_real_power_a(real_power_w: float, voltage_rms_v: float, power_factor: float = 1.0) -> float:
    _positive(real_power_w, "real_power_w")
    _positive(abs(voltage_rms_v), "voltage_rms_v magnitude")
    if not (0.0 < power_factor <= 1.0):
        raise ValueError("power_factor must be in (0, 1]")
    return real_power_w / (abs(voltage_rms_v) * power_factor)


def capacitance_for_current_f(current_rms_a: float, frequency_hz: float, voltage_rms_v: float) -> float:
    _positive(abs(current_rms_a), "current_rms_a magnitude")
    _positive(frequency_hz, "frequency_hz")
    _positive(abs(voltage_rms_v), "voltage_rms_v magnitude")
    return abs(current_rms_a) / (2.0 * math.pi * frequency_hz * abs(voltage_rms_v))


def frequency_for_capacitive_current_hz(current_rms_a: float, capacitance_f: float, voltage_rms_v: float) -> float:
    _positive(abs(current_rms_a), "current_rms_a magnitude")
    _positive(capacitance_f, "capacitance_f")
    _positive(abs(voltage_rms_v), "voltage_rms_v magnitude")
    return abs(current_rms_a) / (2.0 * math.pi * capacitance_f * abs(voltage_rms_v))


def resonance_inductance_h(frequency_hz: float, capacitance_f: float) -> float:
    _positive(frequency_hz, "frequency_hz")
    _positive(capacitance_f, "capacitance_f")
    return 1.0 / ((2.0 * math.pi * frequency_hz) ** 2 * capacitance_f)


def capacitor_energy_j(capacitance_f: float, voltage_v: float) -> float:
    _positive(capacitance_f, "capacitance_f")
    _positive(abs(voltage_v), "voltage_v magnitude")
    return 0.5 * capacitance_f * voltage_v * voltage_v


def full_swing_switched_power_w(capacitance_f: float, voltage_v: float, events_per_s: float) -> float:
    _positive(events_per_s, "events_per_s")
    return capacitor_energy_j(capacitance_f, voltage_v) * events_per_s


def capacitance_for_full_swing_power_f(power_w: float, voltage_v: float, events_per_s: float) -> float:
    _positive(power_w, "power_w")
    _positive(abs(voltage_v), "voltage_v magnitude")
    _positive(events_per_s, "events_per_s")
    return 2.0 * power_w / (events_per_s * voltage_v * voltage_v)


def ideal_transformer_primary_current_a(output_power_w: float, primary_voltage_rms_v: float, efficiency: float = 1.0) -> float:
    _positive(output_power_w, "output_power_w")
    _positive(abs(primary_voltage_rms_v), "primary_voltage_rms_v magnitude")
    if not (0.0 < efficiency <= 1.0):
        raise ValueError("efficiency must be in (0, 1]")
    return output_power_w / (abs(primary_voltage_rms_v) * efficiency)


def main() -> None:
    v = 230.0
    f = 50.0
    p = 100.0
    i100 = current_for_real_power_a(p, v)
    c_current = capacitance_for_current_f(i100, f, v)

    print("V4.20 local-infrastructure / accidental-coupling bound")
    print(f"100 W at 230 V requires at least {i100:.6g} A at unity PF")
    print(f"50-Hz capacitive current path of that magnitude requires {c_current*1e6:.6g} uF")
    print("(that is only a current-carrying scale; an ideal capacitor itself supplies zero real power)")
    print()
    print(f"{'C':>10s} {'I@50Hz':>12s} {'VA@50Hz':>12s} {'24-event full-swing':>20s} {'Lres@50Hz':>14s}")
    for c in (50e-12, 150e-12, 1e-9, 10e-9):
        i = capacitive_current_a(f, c, v)
        s = apparent_power_va(v, i)
        psw = full_swing_switched_power_w(c, v, 24.0)
        l = resonance_inductance_h(f, c)
        print(f"{c*1e12:8.1f}pF {i:12.6g} {s:12.6g} {psw:20.6g} {l:14.6g}")

    print()
    for c in (150e-12, 1e-9):
        freq = frequency_for_capacitive_current_hz(i100, c, v)
        print(f"C={c*1e12:.0f} pF needs f={freq/1e6:.6g} MHz to carry 0.435 A reactively at 230 V")
        print(f"  matching L at that frequency: {resonance_inductance_h(freq, c)*1e6:.6g} uH")


if __name__ == "__main__":
    main()
