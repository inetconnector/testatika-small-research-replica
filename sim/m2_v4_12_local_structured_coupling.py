#!/usr/bin/env python3
"""V4.12 local structured coupling bounds.

This diagnostic follows V4.11. Ordinary ambient atmosphere/RF/ELF/geomagnetic
reservoirs were too weak for a sustained ~100-W tabletop load, so V4.12 asks a
narrower conventional question: could a *local* structured source couple power
through base/table/chassis capacitance or a driven magnetic near field?

All equations are optimistic source-side bounds. They demonstrate what a local
source would have to provide; they do not assert that such a source existed in
any historical Testatika and they do not add RF/AC hardware to the M2 baseline.
"""

from __future__ import annotations

import math

EPS0 = 8.8541878128e-12


def energy_per_cycle(power_w: float, frequency_hz: float) -> float:
    if power_w < 0:
        raise ValueError("power_w must be non-negative")
    if frequency_hz <= 0:
        return math.inf
    return power_w / frequency_hz


def hidden_conductive_current(power_w: float, voltage_v_rms: float, efficiency: float = 1.0) -> float:
    """Minimum RMS current for a galvanic/real-power port at a given voltage."""
    if power_w < 0:
        raise ValueError("power_w must be non-negative")
    if voltage_v_rms <= 0 or efficiency <= 0 or efficiency > 1:
        return math.inf
    return power_w / (efficiency * voltage_v_rms)


def plate_capacitance(area_m2: float, gap_m: float, epsilon_r: float = 1.0, parallel_gaps: int = 1) -> float:
    """Parallel-plate estimate epsilon0*epsilon_r*A/d times parallel gaps.

    `parallel_gaps` is a laboratory geometry parameter only. It must not be used
    to claim a historical multilayer wiring topology without source evidence.
    """
    if area_m2 < 0 or epsilon_r <= 0 or parallel_gaps < 0:
        raise ValueError("area, epsilon_r and parallel_gaps must be non-negative")
    if gap_m <= 0:
        return math.inf
    return EPS0 * epsilon_r * area_m2 * parallel_gaps / gap_m


def capacitive_rms_current(frequency_hz: float, capacitance_f: float, voltage_v_rms: float) -> float:
    if frequency_hz < 0 or capacitance_f < 0:
        raise ValueError("frequency and capacitance must be non-negative")
    return 2.0 * math.pi * frequency_hz * capacitance_f * abs(voltage_v_rms)


def capacitive_apparent_power_bound(frequency_hz: float, capacitance_f: float, voltage_v_rms: float) -> float:
    """Optimistic apparent-power scale omega*C*V^2.

    A real WPT path still requires a source, a return path/matching network and
    real source power equal to load power plus losses.
    """
    return abs(voltage_v_rms) * capacitive_rms_current(frequency_hz, capacitance_f, voltage_v_rms)


def required_capacitance(
    target_power_w: float,
    frequency_hz: float,
    voltage_v_rms: float,
    transfer_fraction: float = 1.0,
) -> float:
    """C required for target real power not to exceed transfer_fraction*omega*C*V^2."""
    if target_power_w < 0:
        raise ValueError("target_power_w must be non-negative")
    if frequency_hz <= 0 or voltage_v_rms <= 0 or transfer_fraction <= 0 or transfer_fraction > 1:
        return math.inf
    return target_power_w / (transfer_fraction * 2.0 * math.pi * frequency_hz * voltage_v_rms**2)


def required_capacitive_voltage(
    target_power_w: float,
    frequency_hz: float,
    capacitance_f: float,
    transfer_fraction: float = 1.0,
) -> float:
    if target_power_w < 0:
        raise ValueError("target_power_w must be non-negative")
    if frequency_hz <= 0 or capacitance_f <= 0 or transfer_fraction <= 0 or transfer_fraction > 1:
        return math.inf
    return math.sqrt(target_power_w / (transfer_fraction * 2.0 * math.pi * frequency_hz * capacitance_f))


def induced_rms_voltage(
    frequency_hz: float,
    turns: int,
    loop_area_m2: float,
    magnetic_flux_density_t_rms: float,
) -> float:
    """Sinusoidal Faraday magnitude Vrms = omega*N*A*B_rms, optimum orientation."""
    if frequency_hz < 0 or turns < 0 or loop_area_m2 < 0:
        raise ValueError("frequency, turns and area must be non-negative")
    return 2.0 * math.pi * frequency_hz * turns * loop_area_m2 * abs(magnetic_flux_density_t_rms)


def required_b_field_rms(
    induced_voltage_v_rms: float,
    frequency_hz: float,
    turns: int,
    loop_area_m2: float,
) -> float:
    if induced_voltage_v_rms < 0:
        raise ValueError("induced voltage must be non-negative")
    denom = 2.0 * math.pi * frequency_hz * turns * loop_area_m2
    if denom <= 0:
        return math.inf
    return induced_voltage_v_rms / denom


def required_mutual_inductance(
    induced_voltage_v_rms: float,
    frequency_hz: float,
    primary_current_a_rms: float,
) -> float:
    """M from V2 = omega*M*I1 for a sinusoidal local inductive source."""
    if induced_voltage_v_rms < 0:
        raise ValueError("induced voltage must be non-negative")
    denom = 2.0 * math.pi * frequency_hz * abs(primary_current_a_rms)
    if denom <= 0:
        return math.inf
    return induced_voltage_v_rms / denom


def main() -> None:
    target = 100.0
    area = 0.09  # 30 cm x 30 cm laboratory comparison plate
    c_base = plate_capacitance(area, 5e-3, epsilon_r=3.0)
    c_thin = plate_capacitance(area, 0.5e-3, epsilon_r=3.0)

    print("V4.12 local structured coupling bounds")
    print(f"target real power: {target:.3f} W")
    print(f"30x30 cm, 5 mm, eps_r=3 plate C: {c_base:.6g} F")
    print(f"30x30 cm, 0.5 mm, eps_r=3 plate C: {c_thin:.6g} F")

    for f in (50.0, 1e3, 10e3, 100e3, 1e6):
        v = required_capacitive_voltage(target, f, c_base)
        i = capacitive_rms_current(f, c_base, v)
        print(f"base bound f={f:g} Hz: V={v:.6g} Vrms I={i:.6g} Arms E/cycle={energy_per_cycle(target, f):.6g} J")

    for f in (50.0, 100e3, 1e6):
        for v in (1e3, 10e3, 100e3):
            c = required_capacitance(target, f, v)
            print(f"required C at f={f:g} Hz V={v:g} Vrms: {c:.6g} F")

    disk_area = math.pi * 0.10**2
    for f in (100e3, 1e6):
        b_1 = required_b_field_rms(100.0, f, 1, disk_area)
        b_24 = required_b_field_rms(100.0, f, 24, disk_area)
        print(f"B for 100 Vrms on 200-mm loop at {f:g} Hz: 1 turn={b_1:.6g} T, 24 turns={b_24:.6g} T")

    print(f"conductive current at 100 kV for 100 W: {hidden_conductive_current(100.0, 100e3):.6g} A")


if __name__ == "__main__":
    main()
