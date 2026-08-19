#!/usr/bin/env python3
"""V4.18 explicit environmental two-port / rear-plate return diagnostics.

A floating M2-like converter cannot sustain net charge transfer through one
external terminal.  This model therefore represents the missing environmental
coupling as at least two ports: a front/sky-side coupling and a rear/base/Earth-
side return.  It separates three quantities that are easily conflated:

1. displacement-current carrying capacity, I = omega*C*V;
2. reactive apparent power, |S| = V*I;
3. real power, P = V*I*cos(phi), which the external source must actually supply.

The model is a low-energy analytical diagnostic.  It does not assert that the
historical M2 had an external AC source, a grounded rear plate, or any hidden
transmitter.
"""

from __future__ import annotations

import math

EPS0 = 8.8541878128e-12


def _positive(value: float, name: str) -> None:
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def series_capacitance_f(c1_f: float, c2_f: float) -> float:
    """Equivalent capacitance of the two environmental coupling capacitors."""
    _positive(c1_f, "c1_f")
    _positive(c2_f, "c2_f")
    return c1_f * c2_f / (c1_f + c2_f)


def equal_port_capacitance_for_series_f(c_series_f: float) -> float:
    """Each of two equal capacitors must be 2*Ceq to give series Ceq."""
    _positive(c_series_f, "c_series_f")
    return 2.0 * c_series_f


def capacitive_reactance_ohm(frequency_hz: float, capacitance_f: float) -> float:
    _positive(frequency_hz, "frequency_hz")
    _positive(capacitance_f, "capacitance_f")
    return 1.0 / (2.0 * math.pi * frequency_hz * capacitance_f)


def capacitive_current_rms_a(voltage_rms_v: float, frequency_hz: float, capacitance_f: float) -> float:
    """RMS displacement-current magnitude through a sinusoidally driven capacitor."""
    _positive(abs(voltage_rms_v), "voltage_rms_v magnitude")
    return abs(voltage_rms_v) / capacitive_reactance_ohm(frequency_hz, capacitance_f)


def required_series_capacitance_for_current_f(current_rms_a: float, voltage_rms_v: float, frequency_hz: float) -> float:
    """Ceq that can carry the requested sinusoidal RMS current magnitude."""
    _positive(abs(current_rms_a), "current_rms_a magnitude")
    _positive(abs(voltage_rms_v), "voltage_rms_v magnitude")
    _positive(frequency_hz, "frequency_hz")
    return abs(current_rms_a) / (2.0 * math.pi * frequency_hz * abs(voltage_rms_v))


def plate_capacitance_f(area_m2: float, gap_m: float, eps_r: float = 1.0, coupling_factor: float = 1.0) -> float:
    """Parallel-plate scale k*eps0*eps_r*A/d; k captures shielding/fringing (<~1)."""
    _positive(area_m2, "area_m2")
    _positive(gap_m, "gap_m")
    _positive(eps_r, "eps_r")
    if coupling_factor <= 0:
        raise ValueError("coupling_factor must be positive")
    return coupling_factor * EPS0 * eps_r * area_m2 / gap_m


def plate_gap_for_capacitance_m(area_m2: float, capacitance_f: float, eps_r: float = 1.0, coupling_factor: float = 1.0) -> float:
    _positive(area_m2, "area_m2")
    _positive(capacitance_f, "capacitance_f")
    _positive(eps_r, "eps_r")
    if coupling_factor <= 0:
        raise ValueError("coupling_factor must be positive")
    return coupling_factor * EPS0 * eps_r * area_m2 / capacitance_f


def floating_rear_plate_return_capacitance_f(machine_to_plate_f: float, plate_to_earth_f: float) -> float:
    """If the rear plate itself floats, its return is two capacitors in series."""
    return series_capacitance_f(machine_to_plate_f, plate_to_earth_f)


def apparent_power_va(voltage_rms_v: float, current_rms_a: float) -> float:
    _positive(abs(voltage_rms_v), "voltage_rms_v magnitude")
    _positive(abs(current_rms_a), "current_rms_a magnitude")
    return abs(voltage_rms_v * current_rms_a)


def real_power_w(voltage_rms_v: float, current_rms_a: float, power_factor: float) -> float:
    """Real source power. power_factor is cos(phi), constrained to [-1, 1]."""
    if not -1.0 <= power_factor <= 1.0:
        raise ValueError("power_factor must be in [-1, 1]")
    return voltage_rms_v * current_rms_a * power_factor


def required_power_factor(target_power_w: float, voltage_rms_v: float, current_rms_a: float) -> float:
    _positive(target_power_w, "target_power_w")
    s = apparent_power_va(voltage_rms_v, current_rms_a)
    return target_power_w / s


def optimum_resistive_load_uncompensated_ohm(source_resistance_ohm: float, frequency_hz: float, coupling_capacitance_f: float) -> float:
    """Rload maximizing real power for Vs--Rs--C--Rload without compensation."""
    if source_resistance_ohm < 0:
        raise ValueError("source_resistance_ohm must be non-negative")
    x = capacitive_reactance_ohm(frequency_hz, coupling_capacitance_f)
    return math.sqrt(source_resistance_ohm**2 + x**2)


def max_uncompensated_load_power_w(
    source_voltage_rms_v: float,
    source_resistance_ohm: float,
    frequency_hz: float,
    coupling_capacitance_f: float,
) -> float:
    """Maximum Rload power through an uncompensated series capacitive port.

    Pmax = Vs^2 / [2*(Rs + sqrt(Rs^2 + Xc^2))].
    Lossless reactive compensation can remove Xc, but can never beat the source's
    own Thevenin available-power bound.
    """
    _positive(abs(source_voltage_rms_v), "source_voltage_rms_v magnitude")
    if source_resistance_ohm < 0:
        raise ValueError("source_resistance_ohm must be non-negative")
    x = capacitive_reactance_ohm(frequency_hz, coupling_capacitance_f)
    root = math.sqrt(source_resistance_ohm**2 + x**2)
    return source_voltage_rms_v**2 / (2.0 * (source_resistance_ohm + root))


def thevenin_available_power_w(source_voltage_rms_v: float, source_resistance_ohm: float) -> float:
    """Maximum real power after ideal lossless reactive compensation/matching."""
    _positive(abs(source_voltage_rms_v), "source_voltage_rms_v magnitude")
    _positive(source_resistance_ohm, "source_resistance_ohm")
    return source_voltage_rms_v**2 / (4.0 * source_resistance_ohm)


def recharge_time_constant_s(source_resistance_ohm: float, capacitance_f: float) -> float:
    _positive(source_resistance_ohm, "source_resistance_ohm")
    _positive(capacitance_f, "capacitance_f")
    return source_resistance_ohm * capacitance_f


def recharge_fraction_per_event(source_resistance_ohm: float, capacitance_f: float, events_per_s: float) -> float:
    """Fraction of a first-order voltage deficit recovered in one event interval."""
    _positive(events_per_s, "events_per_s")
    tau = recharge_time_constant_s(source_resistance_ohm, capacitance_f)
    return 1.0 - math.exp(-(1.0 / events_per_s) / tau)


def common_mode_charge_rate_a(external_currents_a: tuple[float, ...]) -> float:
    """KCL: dQ_machine/dt equals algebraic sum of all external terminal currents."""
    return sum(external_currents_a)


def main() -> None:
    print("V4.18 explicit front/rear environmental two-port bounds")

    target_i = 1e-3
    target_v = 100e3
    for f in (1.0, 24.0, 50.0, 1e3, 100e3, 1e6):
        ceq = required_series_capacitance_for_current_f(target_i, target_v, f)
        ceach = equal_port_capacitance_for_series_f(ceq)
        print(
            f"f={f:g} Hz: Ceq for 1 mA @100 kV = {ceq*1e12:.6g} pF; "
            f"two equal ports need {ceach*1e12:.6g} pF each"
        )

    # 30x30-cm plate geometry, deliberately ideal parallel-plate upper scale.
    area = 0.09
    for f in (24.0, 50.0):
        ceq = required_series_capacitance_for_current_f(target_i, target_v, f)
        ceach = equal_port_capacitance_for_series_f(ceq)
        d = plate_gap_for_capacitance_m(area, ceach)
        print(f"30x30-cm ideal equal-port gap for {f:g} Hz current scale: {d*1e3:.6g} mm")

    rear_2cm = plate_capacitance_f(area, 0.02)
    for v in (100e3, 250e3):
        i = capacitive_current_rms_a(v, 24.0, rear_2cm)
        print(f"30x30-cm rear plate at 2 cm, 24 Hz, {v/1e3:g} kV: |I_C|={i*1e3:.6g} mA")

    # Source-impedance reality check: atmospheric full-column optimism from V4.14.
    rs_atmos = 1.25e18
    ceq_24 = required_series_capacitance_for_current_f(target_i, target_v, 24.0)
    print(f"fair-weather full-column Rs*Ceq(24Hz) tau: {recharge_time_constant_s(rs_atmos, ceq_24):.6g} s")
    print(f"recharge fraction in one 24-Hz interval: {recharge_fraction_per_event(rs_atmos, ceq_24, 24.0):.6g}")
    print(f"ideal compensated Thevenin Pmax at 250 kV / 1.25e18 ohm: {thevenin_available_power_w(250e3, rs_atmos):.6g} W")

    print(f"100 kV * 1 mA apparent power: {apparent_power_va(100e3, 1e-3):.6g} VA")
    print(f"PF required for 100 W at 100 kV, 1 mA: {required_power_factor(100.0, 100e3, 1e-3):.6g}")
    print(f"PF required for 100 W at 250 kV, 1 mA: {required_power_factor(100.0, 250e3, 1e-3):.6g}")

    # A floating rear plate is itself another series capacitor to Earth.
    print(
        "100-pF machine-to-rear and 100-pF rear-to-Earth -> floating return: "
        f"{floating_rear_plate_return_capacitance_f(100e-12, 100e-12)*1e12:.6g} pF"
    )


if __name__ == "__main__":
    main()
