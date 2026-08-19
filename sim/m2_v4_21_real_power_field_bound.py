#!/usr/bin/env python3
"""V4.21 real-power bound for a capacitive environmental/HF field port.

V4.10/V4.18 used I=omega*C*V as a useful displacement-current scale. V4.21
adds the missing series-load real-power optimization: for an ideal RMS voltage
source feeding a resistor through a lossless series capacitance, maximum load
power occurs at R_load = |X_C| and is V_s^2/(2|X_C|).

This gives a stricter field-amplitude target than equating V*I with watts.
It remains an optimistic bound: source resistance, receiver loss, imperfect
coupling, rectifier loss and finite effective aperture can only increase the
required external field/source power.
"""
from __future__ import annotations

import math

Z0_FREE_SPACE_OHM = 376.730313668


def _positive(x: float, name: str) -> None:
    if x <= 0.0:
        raise ValueError(f"{name} must be positive")


def capacitive_reactance_ohm(frequency_hz: float, capacitance_f: float) -> float:
    _positive(frequency_hz, "frequency_hz")
    _positive(capacitance_f, "capacitance_f")
    return 1.0 / (2.0 * math.pi * frequency_hz * capacitance_f)


def max_real_power_series_c_w(voltage_rms_v: float, frequency_hz: float, capacitance_f: float) -> float:
    """Maximum resistor power through an ideal series C from an ideal RMS source."""
    _positive(abs(voltage_rms_v), "voltage_rms_v magnitude")
    x = capacitive_reactance_ohm(frequency_hz, capacitance_f)
    return voltage_rms_v * voltage_rms_v / (2.0 * x)


def optimum_load_resistance_ohm(frequency_hz: float, capacitance_f: float) -> float:
    return capacitive_reactance_ohm(frequency_hz, capacitance_f)


def source_voltage_for_real_power_v(power_w: float, frequency_hz: float, capacitance_f: float) -> float:
    _positive(power_w, "power_w")
    x = capacitive_reactance_ohm(frequency_hz, capacitance_f)
    return math.sqrt(2.0 * power_w * x)


def optimum_current_for_real_power_a(power_w: float, frequency_hz: float, capacitance_f: float) -> float:
    _positive(power_w, "power_w")
    x = capacitive_reactance_ohm(frequency_hz, capacitance_f)
    return math.sqrt(power_w / x)


def optimum_power_factor() -> float:
    return 1.0 / math.sqrt(2.0)


def field_for_voltage_v_m(voltage_rms_v: float, span_m: float) -> float:
    _positive(abs(voltage_rms_v), "voltage_rms_v magnitude")
    _positive(span_m, "span_m")
    return abs(voltage_rms_v) / span_m


def voltage_from_uniform_field_v(field_rms_v_m: float, span_m: float) -> float:
    _positive(abs(field_rms_v_m), "field_rms_v_m magnitude")
    _positive(span_m, "span_m")
    return abs(field_rms_v_m) * span_m


def max_real_power_from_uniform_field_w(
    field_rms_v_m: float,
    span_m: float,
    frequency_hz: float,
    capacitance_f: float,
) -> float:
    v = voltage_from_uniform_field_v(field_rms_v_m, span_m)
    return max_real_power_series_c_w(v, frequency_hz, capacitance_f)


def far_field_power_density_w_m2(field_rms_v_m: float) -> float:
    _positive(abs(field_rms_v_m), "field_rms_v_m magnitude")
    return field_rms_v_m * field_rms_v_m / Z0_FREE_SPACE_OHM


def far_field_field_for_received_power_v_m(
    received_power_w: float,
    effective_area_m2: float,
    capture_efficiency: float = 1.0,
) -> float:
    _positive(received_power_w, "received_power_w")
    _positive(effective_area_m2, "effective_area_m2")
    if not (0.0 < capture_efficiency <= 1.0):
        raise ValueError("capture_efficiency must be in (0, 1]")
    required_density = received_power_w / (effective_area_m2 * capture_efficiency)
    return math.sqrt(required_density * Z0_FREE_SPACE_OHM)


def main() -> None:
    p = 100.0
    c = 50e-12
    span = 0.20
    print("V4.21 real-power field/capacitive-port bound")
    print("Assumption: ideal RMS source -> series C=50 pF -> optimum resistive load")
    print(f"{'f':>10s} {'Xc[ohm]':>14s} {'Vs for100W':>14s} {'Iopt[A]':>12s} {'E over20cm':>14s}")
    for f in (24.0, 50.0, 1e3, 10e3, 100e3, 1e6, 10e6, 100e6):
        x = capacitive_reactance_ohm(f, c)
        v = source_voltage_for_real_power_v(p, f, c)
        i = optimum_current_for_real_power_a(p, f, c)
        e = field_for_voltage_v_m(v, span)
        print(f"{f:10.4g} {x:14.6g} {v:14.6g} {i:12.6g} {e:14.6g}")

    print("\nIdeal maximum real power from a uniform 100 V/m field over 20 cm, C=50 pF")
    for f in (1e6, 10e6, 100e6):
        print(f"{f/1e6:6.1f} MHz -> {max_real_power_from_uniform_field_w(100.0, span, f, c):.6g} W")

    print("\nFar-field flux floor for 100 W into 0.1 m^2 effective capture area")
    for eta in (1.0, 0.5, 0.1, 0.01):
        e = far_field_field_for_received_power_v_m(100.0, 0.1, eta)
        print(f"capture efficiency {eta:5.1%}: E_rms >= {e:.6g} V/m")


if __name__ == "__main__":
    main()
