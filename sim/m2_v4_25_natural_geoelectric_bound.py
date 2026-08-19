#!/usr/bin/env python3
"""M2 V4.25 natural geoelectric/telluric coupling bound.

The model grants the complete measured/modeled horizontal geoelectric-field
potential across a compact apparatus span. That is already favorable to the
source hypothesis: a floating device without two well-coupled terminals may see
less. The calculator tests voltage/current/source-impedance scale only; it does
not claim that a historical Testatika used ground electrodes.
"""
from __future__ import annotations

import argparse


def _positive(name: str, value: float) -> float:
    if value <= 0.0:
        raise ValueError(f"{name} must be > 0")
    return value


def field_v_per_m(field_v_per_km: float) -> float:
    return _positive("field_v_per_km", field_v_per_km) / 1000.0


def voltage_across_span_v(field_v_per_km: float, span_m: float) -> float:
    return field_v_per_m(field_v_per_km) * _positive("span_m", span_m)


def current_for_real_power_a(power_w: float, voltage_v: float) -> float:
    return _positive("power_w", power_w) / _positive("voltage_v", voltage_v)


def equivalent_load_resistance_ohm(power_w: float, voltage_v: float) -> float:
    p = _positive("power_w", power_w)
    v = _positive("voltage_v", voltage_v)
    return v * v / p


def max_thevenin_source_resistance_ohm(power_w: float, open_circuit_voltage_v: float) -> float:
    p = _positive("power_w", power_w)
    v = _positive("open_circuit_voltage_v", open_circuit_voltage_v)
    return v * v / (4.0 * p)


def span_for_voltage_m(target_voltage_v: float, field_v_per_km_value: float) -> float:
    return _positive("target_voltage_v", target_voltage_v) / field_v_per_m(field_v_per_km_value)


def integrated_line_voltage_v(field_v_per_km_value: float, line_length_km: float) -> float:
    return _positive("field_v_per_km", field_v_per_km_value) * _positive("line_length_km", line_length_km)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--power", type=float, default=100.0)
    parser.add_argument("--span", type=float, default=0.2)
    args = parser.parse_args()
    p = args.power
    span = args.span

    cases = (
        ("moderate ULF storm measurement", 1.0),
        ("2023 N-Europe strong modeled peak", 3.0),
        ("1989 Britain modeled peak", 12.0),
        ("1989 US peak", 21.66),
        ("Carrington Virginia median model", 30.30),
        ("Carrington Virginia upper CI model", 47.20),
    )

    print("M2 V4.25 natural geoelectric/telluric compact-span bound")
    print(f"target real output = {p:.6g} W, compact span = {span:.6g} m")
    print(f"{'case':38s} {'E[V/km]':>10s} {'Vspan[V]':>12s} {'I@P[A]':>12s} {'Rs,max[ohm]':>14s}")
    for label, e in cases:
        v = voltage_across_span_v(e, span)
        i = current_for_real_power_a(p, v)
        rs = max_thevenin_source_resistance_ohm(p, v)
        print(f"{label:38s} {e:10.4g} {v:12.6g} {i:12.6g} {rs:14.6g}")

    print("\nBaseline needed to accumulate 100 kV directly")
    for label, e in cases:
        length_km = span_for_voltage_m(100e3, e) / 1000.0
        print(f"{label:38s} -> {length_km:.6g} km")

    print("\nWhy long infrastructure is different")
    for e in (1.0, 30.3):
        for length_km in (1.0, 10.0, 100.0):
            print(f"E={e:5.1f} V/km, L={length_km:6.1f} km -> {integrated_line_voltage_v(e, length_km):.6g} V")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
