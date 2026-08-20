#!/usr/bin/env python3
"""M2 V4.28 source-elimination matrix.

This module synthesizes source-power bounds already established in V4.11 and
V4.23-V4.27. It does not invent a Testatika energy source. It asks how far
ordinary weak ambient channels fall below a chosen real-power target and keeps
strong/local/finite reservoirs open until directly measured.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass


def _positive(name: str, value: float) -> float:
    if value <= 0.0:
        raise ValueError(f"{name} must be > 0")
    return value


@dataclass(frozen=True)
class PowerBound:
    name: str
    bound_w: float
    basis: str

    def gap(self, target_w: float) -> float:
        return _positive("target_w", target_w) / _positive("bound_w", self.bound_w)


def captured_power_w(power_density_w_m2: float, area_m2: float) -> float:
    return _positive("power_density_w_m2", power_density_w_m2) * _positive("area_m2", area_m2)


def required_capture_area_m2(target_w: float, power_density_w_m2: float) -> float:
    return _positive("target_w", target_w) / _positive("power_density_w_m2", power_density_w_m2)


def required_current_a(target_w: float, source_voltage_v: float) -> float:
    return _positive("target_w", target_w) / _positive("source_voltage_v", source_voltage_v)


def max_thevenin_resistance_ohm(target_w: float, open_circuit_voltage_v: float) -> float:
    """Largest source resistance that can deliver target power at max-power transfer."""
    p = _positive("target_w", target_w)
    v = _positive("open_circuit_voltage_v", open_circuit_voltage_v)
    return v * v / (4.0 * p)


def ordinary_ambient_bounds(area_m2: float = 0.1) -> tuple[PowerBound, ...]:
    area = _positive("area_m2", area_m2)
    return (
        PowerBound(
            "fair-weather global electric circuit (optimistic full-column density)",
            captured_power_w(5e-7, area),
            "V4.11: J~2 pA/m2 and full ~250 kV gives 0.5 uW/m2",
        ),
        PowerBound(
            "50-Hz stray E-field, 100 V/m, Ceq=50 pF, h=0.2 m",
            6.28e-6,
            "V4.11 floating two-port bound",
        ),
        PowerBound(
            "50-Hz extreme E-field, 10 kV/m, Ceq=50 pF, h=0.2 m",
            62.8e-3,
            "V4.11 deliberately strong comparison field",
        ),
        PowerBound(
            "ambient RF survey upper example, 200 uW/m2 over capture area",
            captured_power_w(200e-6, area),
            "V4.11 ideal 100% aperture capture",
        ),
        PowerBound(
            "strong local RF comparison, 0.1 W/m2 over capture area",
            captured_power_w(0.1, area),
            "V4.11 ideal 100% aperture capture",
        ),
        PowerBound(
            "Schumann/ELF proxy, 1.59e-10 W/m2 over capture area",
            captured_power_w(1.59e-10, area),
            "V4.11 order-of-magnitude E*B/mu0 proxy",
        ),
    )


def classify_gap(gap: float) -> str:
    g = _positive("gap", gap)
    if g >= 1e6:
        return "EXCLUDED_AS_BULK_AMBIENT"
    if g >= 100.0:
        return "STRONGLY_CONSTRAINED"
    if g > 1.0:
        return "INSUFFICIENT_AT_STATED_BOUND"
    return "NOT_EXCLUDED_BY_POWER_SCALE"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=float, default=100.0)
    parser.add_argument("--area", type=float, default=0.1)
    args = parser.parse_args()

    target = _positive("target", args.target)
    area = _positive("area", args.area)
    print("M2 V4.28 source-elimination matrix")
    print(f"target = {target:.6g} W, comparison capture area = {area:.6g} m^2")
    print(f"{'candidate':66s} {'bound[W]':>12s} {'gap':>13s} {'classification':>27s}")
    for item in ordinary_ambient_bounds(area):
        gap = item.gap(target)
        print(f"{item.name:66s} {item.bound_w:12.6g} {gap:13.6g} {classify_gap(gap):>27s}")

    print("\nChannels that cannot be generically eliminated and require direct measurement:")
    for name in (
        "hidden galvanic/base/table/chassis input",
        "strong local near-field transmitter/coupler",
        "mechanical shaft/fixture work",
        "finite chemical/electrical storage",
        "corona/ion return path driven by a local field source",
        "thermal/airflow/radiant source strong enough to meet measured threshold",
    ):
        print(f"- OPEN_MEASURE_DIRECTLY: {name}")

    print("\nUnknown/vacuum-field source remains LAST_RESORT only after a reproducible positive closed-budget residual.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
