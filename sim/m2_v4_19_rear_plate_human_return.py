#!/usr/bin/env python3
"""V4.19 rear-plate / human-body environmental return-path diagnostic.

This is a reduced electro-quasistatic capacitance-network model, not a recovered
historical M2 schematic. It quantifies how strongly Marinov's rear metal plate
could change a floating machine's return capacitance when the plate is floating,
human-held, resistively referenced, or Earth-referenced.

The important distinction is preserved throughout:
- displacement-current capacity is not real power;
- a nearby conductor can strongly load/detune a high-impedance electrostatic
  system without being its energy source;
- the ordinary Earth-ionosphere source-impedance bound from V4.14 still applies.
"""
from __future__ import annotations

import math

EPS0 = 8.8541878128e-12


def _positive(x: float, name: str) -> None:
    if x <= 0.0:
        raise ValueError(f"{name} must be positive")


def parallel_plate_capacitance_f(area_m2: float, gap_m: float, eps_r: float = 1.0) -> float:
    _positive(area_m2, "area_m2")
    _positive(gap_m, "gap_m")
    _positive(eps_r, "eps_r")
    return EPS0 * eps_r * area_m2 / gap_m


def series_capacitance_f(*caps_f: float) -> float:
    if not caps_f:
        raise ValueError("at least one capacitance is required")
    for c in caps_f:
        _positive(c, "capacitance")
    return 1.0 / sum(1.0 / c for c in caps_f)


def rear_return_capacitance_f(machine_plate_f: float, plate_earth_f: float) -> float:
    """Machine -> rear plate -> Earth equivalent return capacitance."""
    return series_capacitance_f(machine_plate_f, plate_earth_f)


def full_environment_ceq_f(front_env_f: float, rear_return_f: float) -> float:
    """Front/environment and rear/Earth ports in series through a floating machine."""
    return series_capacitance_f(front_env_f, rear_return_f)


def displacement_current_a(frequency_hz: float, capacitance_f: float, voltage_rms_v: float) -> float:
    _positive(frequency_hz, "frequency_hz")
    _positive(capacitance_f, "capacitance_f")
    _positive(abs(voltage_rms_v), "voltage_rms_v magnitude")
    return 2.0 * math.pi * frequency_hz * capacitance_f * abs(voltage_rms_v)


def required_ceq_f(current_rms_a: float, frequency_hz: float, voltage_rms_v: float) -> float:
    _positive(abs(current_rms_a), "current_rms_a magnitude")
    _positive(frequency_hz, "frequency_hz")
    _positive(abs(voltage_rms_v), "voltage_rms_v magnitude")
    return abs(current_rms_a) / (2.0 * math.pi * frequency_hz * abs(voltage_rms_v))


def required_front_capacitance_f(target_ceq_f: float, rear_return_f: float) -> float:
    """Front capacitance required so series(front,rear)=target.

    Returns +inf when the rear return is itself <= the requested series C.
    """
    _positive(target_ceq_f, "target_ceq_f")
    _positive(rear_return_f, "rear_return_f")
    if rear_return_f <= target_ceq_f:
        return math.inf
    return 1.0 / (1.0 / target_ceq_f - 1.0 / rear_return_f)


def capacitor_energy_j(capacitance_f: float, voltage_v: float) -> float:
    _positive(capacitance_f, "capacitance_f")
    _positive(abs(voltage_v), "voltage_v magnitude")
    return 0.5 * capacitance_f * voltage_v * voltage_v


def full_swing_energy_rate_w(events_per_s: float, capacitance_f: float, voltage_v: float) -> float:
    """0.5*C*V^2 per event scale if each event fully charges/discharges the node.

    This is not the power of an ideal capacitor in sinusoidal steady state. It is
    only a switched-energy scale for nonlinear/rectified damping comparisons.
    """
    _positive(events_per_s, "events_per_s")
    return events_per_s * capacitor_energy_j(capacitance_f, voltage_v)


def apparent_power_va(voltage_rms_v: float, current_rms_a: float) -> float:
    _positive(abs(voltage_rms_v), "voltage_rms_v magnitude")
    _positive(abs(current_rms_a), "current_rms_a magnitude")
    return abs(voltage_rms_v * current_rms_a)


def power_factor_required(real_power_w: float, voltage_rms_v: float, current_rms_a: float) -> float:
    _positive(real_power_w, "real_power_w")
    s = apparent_power_va(voltage_rms_v, current_rms_a)
    return real_power_w / s


def main() -> None:
    area = 0.30 * 0.30
    body_to_earth = 150e-12  # literature-scale experimental body-to-Earth value
    f = 24.0

    print("V4.19 rear-plate / human-return diagnostic")
    print("30 cm x 30 cm plate; body-to-Earth comparison = 150 pF")
    print(f"{'gap':>8s} {'Cmp[pF]':>10s} {'held-return[pF]':>16s} {'I@100kV[mA]':>14s} {'I@250kV[mA]':>14s}")
    for gap in (0.20, 0.10, 0.05, 0.02, 0.01, 0.005):
        cmp = parallel_plate_capacitance_f(area, gap)
        ret = rear_return_capacitance_f(cmp, body_to_earth)
        i100 = displacement_current_a(f, ret, 100e3)
        i250 = displacement_current_a(f, ret, 250e3)
        print(f"{gap:8.3g} {cmp*1e12:10.3f} {ret*1e12:16.3f} {i100*1e3:14.3f} {i250*1e3:14.3f}")

    cmp_2cm = parallel_plate_capacitance_f(area, 0.02)
    held_2cm = rear_return_capacitance_f(cmp_2cm, body_to_earth)
    target = required_ceq_f(1e-3, f, 250e3)
    print("\n2-cm rear-plate comparison")
    print(f"machine-to-plate C              = {cmp_2cm*1e12:.3f} pF")
    print(f"human-held effective rear C     = {held_2cm*1e12:.3f} pF")
    print(f"Ceq needed for 1 mA @250kV/24Hz = {target*1e12:.3f} pF")
    print(f"front C needed if plate grounded= {required_front_capacitance_f(target, cmp_2cm)*1e12:.3f} pF")
    print(f"front C needed if human-held    = {required_front_capacitance_f(target, held_2cm)*1e12:.3f} pF")


if __name__ == "__main__":
    main()
