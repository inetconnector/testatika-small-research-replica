#!/usr/bin/env python3
"""M2-V4.3: explicit external-source bounds for a fully floating Testatika model.

V4.0-V4.2 deliberately kept the machine charge-closed and energy-closed except
for explicitly booked shaft work. V4.3 asks what changes if the real machine
was electrically floating (no earth wire) but NOT environmentally closed.

Four candidate source classes are bounded without assuming a historical circuit:

1. sinusoidal capacitive coupling to an external AC potential,
2. net ion/charge exchange with an external potential reservoir,
3. finite electrostatic/electret storage,
4. mechanical shaft power.

The equations are intentionally generous. In particular, the capacitive-coupling
number S = omega*C*V_rms^2 is an apparent-power upper bound; real harvestable
power cannot exceed it and practical rectification/matching reduces it.

No source is hidden: any sustained output must be assigned to one of these or
another explicitly metered reservoir.
"""
from __future__ import annotations

from dataclasses import dataclass
import argparse
import math
from typing import Iterable, Sequence

TAU = 2.0 * math.pi


def capacitive_apparent_power_bound(c_f: float, v_rms: float, f_hz: float) -> float:
    """Optimistic upper bound S = V_rms * I_rms = omega*C*V_rms^2."""
    if c_f < 0 or v_rms < 0 or f_hz < 0:
        raise ValueError("inputs must be non-negative")
    return TAU * f_hz * c_f * v_rms * v_rms


def capacitive_current_rms(c_f: float, v_rms: float, f_hz: float) -> float:
    if c_f < 0 or v_rms < 0 or f_hz < 0:
        raise ValueError("inputs must be non-negative")
    return TAU * f_hz * c_f * v_rms


def minimum_coupling_capacitance_for_power(power_w: float, v_rms: float, f_hz: float) -> float:
    """Minimum C from the optimistic inequality P <= omega*C*V^2."""
    if power_w < 0 or v_rms <= 0 or f_hz <= 0:
        raise ValueError("power must be non-negative; voltage/frequency positive")
    return power_w / (TAU * f_hz * v_rms * v_rms)


def external_current_required(power_w: float, potential_v: float) -> float:
    """Minimum DC-equivalent current from P = V*I, ignoring all losses."""
    if power_w < 0 or potential_v <= 0:
        raise ValueError("power must be non-negative and potential positive")
    return power_w / potential_v


def external_charge_energy(charge_c: float, potential_v: float) -> float:
    """Energy transferred by charge crossing a fixed potential: E = V*Q."""
    if potential_v < 0:
        raise ValueError("potential magnitude must be non-negative")
    return abs(charge_c) * potential_v


def electrostatic_store_energy(c_f: float, v: float) -> float:
    if c_f < 0:
        raise ValueError("capacitance must be non-negative")
    return 0.5 * c_f * v * v


def reservoir_duration_s(c_f: float, v: float, power_w: float) -> float:
    if power_w <= 0:
        raise ValueError("power must be positive")
    return electrostatic_store_energy(c_f, v) / power_w


def capacitance_for_duration(power_w: float, v: float, duration_s: float) -> float:
    if power_w < 0 or duration_s < 0 or v == 0:
        raise ValueError("power/duration non-negative and voltage non-zero")
    return 2.0 * power_w * duration_s / (v * v)


def mechanical_torque_required(power_w: float, rpm: float) -> float:
    if power_w < 0 or rpm <= 0:
        raise ValueError("power must be non-negative and rpm positive")
    omega = rpm * TAU / 60.0
    return power_w / omega


def collector_area_required(power_w: float, potential_v: float, current_density_a_m2: float) -> float:
    """Ideal P = V*J*A bound for a replenished atmospheric/ionic current."""
    if power_w < 0 or potential_v <= 0 or current_density_a_m2 <= 0:
        raise ValueError("power non-negative; potential/current density positive")
    return power_w / (potential_v * current_density_a_m2)


@dataclass(frozen=True)
class BoundCase:
    power_w: float
    rotor_rpm: float = 15.0
    room_v_rms: float = 230.0
    room_f_hz: float = 50.0
    hv_environment_v_rms: float = 10_000.0
    ion_potential_v: float = 250_000.0
    ion_current_density_a_m2: float = 2e-12
    pot_voltage_v: float = 30_000.0
    pot_capacitance_f: float = 120e-12


def summarize_case(case: BoundCase) -> dict[str, float]:
    p = case.power_w
    return {
        "torque_nm": mechanical_torque_required(p, case.rotor_rpm),
        "c_230v_50hz_f": minimum_coupling_capacitance_for_power(
            p, case.room_v_rms, case.room_f_hz
        ),
        "c_10kv_50hz_f": minimum_coupling_capacitance_for_power(
            p, case.hv_environment_v_rms, case.room_f_hz
        ),
        "ion_current_a": external_current_required(p, case.ion_potential_v),
        "ion_area_m2": collector_area_required(
            p, case.ion_potential_v, case.ion_current_density_a_m2
        ),
        "pot_energy_j": electrostatic_store_energy(
            case.pot_capacitance_f, case.pot_voltage_v
        ),
        "pot_duration_s": reservoir_duration_s(
            case.pot_capacitance_f, case.pot_voltage_v, p
        ),
        "c_for_1h_at_pot_v_f": capacitance_for_duration(
            p, case.pot_voltage_v, 3600.0
        ),
    }


def coupling_sweep(
    capacitances_f: Iterable[float],
    v_rms: float = 230.0,
    f_hz: float = 50.0,
) -> list[tuple[float, float, float]]:
    out = []
    for c in capacitances_f:
        out.append((
            float(c),
            capacitive_current_rms(c, v_rms, f_hz),
            capacitive_apparent_power_bound(c, v_rms, f_hz),
        ))
    return out


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--power-w", type=float, default=100.0)
    p.add_argument("--rpm", type=float, default=15.0)
    args = p.parse_args(argv)

    case = BoundCase(power_w=args.power_w, rotor_rpm=args.rpm)
    r = summarize_case(case)
    print("M2-V4.3 explicit external-source bounds")
    print("All source terms are optimistic upper/minimum bounds; no hidden energy.")
    print(f"target power                         = {case.power_w:.6g} W")
    print(f"mechanical torque @ {case.rotor_rpm:g} rpm          = {r['torque_nm']:.6g} N m")
    print(f"minimum C @ 230 V / 50 Hz           = {r['c_230v_50hz_f']*1e6:.6g} uF")
    print(f"minimum C @ 10 kV / 50 Hz           = {r['c_10kv_50hz_f']*1e9:.6g} nF")
    print(f"external current @ 250 kV           = {r['ion_current_a']*1e3:.6g} mA")
    print(f"ideal area @ 2 pA/m2, 250 kV        = {r['ion_area_m2']/1e6:.6g} km2")
    print(f"120 pF @ 30 kV store                = {r['pot_energy_j']:.6g} J")
    print(f"duration of that store @ target     = {r['pot_duration_s']*1e3:.6g} ms")
    print(f"C needed for 1 h @ 30 kV            = {r['c_for_1h_at_pot_v_f']*1e6:.6g} uF")

    print("\n230 V / 50 Hz capacitive-coupling sweep")
    print(f"{'C':>12s} {'I_rms':>14s} {'S_bound':>14s}")
    for c, i, s in coupling_sweep((10e-12, 100e-12, 1e-9, 10e-9, 100e-9, 1e-6)):
        print(f"{c:12.3g} {i:14.6g} {s:14.6g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
