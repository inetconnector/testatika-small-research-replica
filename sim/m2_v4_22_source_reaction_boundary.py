#!/usr/bin/env python3
"""M2 V4.22 source-reaction and closed-boundary energy diagnostic.

This calculator does not assume an anomalous source. It asks what any sustained
source must look like at the machine boundary if the historical output claims
were real.

The electrical source is represented by an RMS Thevenin equivalent. The
calculation is deliberately optimistic: lossless matching is allowed and all
quoted source-resistance limits are best-case upper bounds.
"""
from __future__ import annotations

import argparse
import math


def _positive(name: str, value: float) -> float:
    if value <= 0.0:
        raise ValueError(f"{name} must be > 0")
    return value


def effective_load_resistance_ohm(voltage_v: float, real_power_w: float) -> float:
    """Equivalent resistive load at an RMS voltage and real power."""
    v = _positive("voltage_v", voltage_v)
    p = _positive("real_power_w", real_power_w)
    return v * v / p


def thevenin_max_power_w(open_circuit_voltage_v: float, source_resistance_ohm: float) -> float:
    """Maximum load power from an RMS Thevenin source, at matched load."""
    v = _positive("open_circuit_voltage_v", open_circuit_voltage_v)
    r = _positive("source_resistance_ohm", source_resistance_ohm)
    return v * v / (4.0 * r)


def max_source_resistance_for_power_ohm(open_circuit_voltage_v: float, real_power_w: float) -> float:
    """Largest Thevenin resistance that can still deliver P with ideal matching."""
    v = _positive("open_circuit_voltage_v", open_circuit_voltage_v)
    p = _positive("real_power_w", real_power_w)
    return v * v / (4.0 * p)


def required_open_circuit_voltage_v(real_power_w: float, source_resistance_ohm: float) -> float:
    """Minimum RMS open-circuit voltage for P at ideal matched load."""
    p = _positive("real_power_w", real_power_w)
    r = _positive("source_resistance_ohm", source_resistance_ohm)
    return 2.0 * math.sqrt(p * r)


def loaded_voltage_fraction(source_resistance_ohm: float, load_resistance_ohm: float) -> float:
    """V_load/V_oc for a resistive Thevenin divider."""
    rs = source_resistance_ohm
    if rs < 0.0:
        raise ValueError("source_resistance_ohm must be >= 0")
    rl = _positive("load_resistance_ohm", load_resistance_ohm)
    return rl / (rs + rl)


def max_source_resistance_for_droop_ohm(load_resistance_ohm: float, max_droop_fraction: float) -> float:
    """Largest source R for a requested fractional terminal-voltage droop."""
    rl = _positive("load_resistance_ohm", load_resistance_ohm)
    d = max_droop_fraction
    if not 0.0 < d < 1.0:
        raise ValueError("max_droop_fraction must be between 0 and 1")
    return rl * d / (1.0 - d)


def required_source_reaction_w(load_power_w: float, transfer_efficiency: float = 1.0) -> float:
    """Minimum increase in real source power needed to sustain the load."""
    p = _positive("load_power_w", load_power_w)
    eta = transfer_efficiency
    if not 0.0 < eta <= 1.0:
        raise ValueError("transfer_efficiency must be in (0, 1]")
    return p / eta


def source_current_for_real_power_a(real_power_w: float, source_voltage_v: float, power_factor: float = 1.0) -> float:
    p = _positive("real_power_w", real_power_w)
    v = _positive("source_voltage_v", source_voltage_v)
    pf = power_factor
    if not 0.0 < pf <= 1.0:
        raise ValueError("power_factor must be in (0, 1]")
    return p / (v * pf)


def current_density_a_per_m2(current_a: float, area_m2: float) -> float:
    i = _positive("current_a", current_a)
    a = _positive("area_m2", area_m2)
    return i / a


def reservoir_energy_j(capacitance_f: float, voltage_v: float) -> float:
    c = _positive("capacitance_f", capacitance_f)
    v = _positive("voltage_v", voltage_v)
    return 0.5 * c * v * v


def reservoir_duration_s(capacitance_f: float, voltage_v: float, load_power_w: float) -> float:
    p = _positive("load_power_w", load_power_w)
    return reservoir_energy_j(capacitance_f, voltage_v) / p


def boundary_flux_w_per_m2(net_input_power_w: float, boundary_area_m2: float) -> float:
    p = _positive("net_input_power_w", net_input_power_w)
    a = _positive("boundary_area_m2", boundary_area_m2)
    return p / a


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--power", type=float, default=100.0, help="target real output power [W]")
    args = parser.parse_args()
    p = args.power

    print("M2 V4.22 source-reaction / boundary diagnostic")
    print(f"target real output        = {p:.6g} W")

    print("\nThevenin source-resistance ceiling with ideal matching")
    print(f"{'Voc rms':>12s} {'Rs,max':>16s}")
    for v in (10e3, 100e3, 250e3, 1e6):
        rs = max_source_resistance_for_power_ohm(v, p)
        print(f"{v:12.6g} {rs:16.6g}")

    atmospheric_rs = 1.25e18
    atmospheric_v = 250e3
    print("\nOptimistic fair-weather full-column comparison")
    print(f"Voc                     = {atmospheric_v:.6g} V")
    print(f"effective Rs            = {atmospheric_rs:.6g} ohm")
    print(f"Pmax                    = {thevenin_max_power_w(atmospheric_v, atmospheric_rs):.6g} W")
    print(f"Voc needed for {p:.6g} W = {required_open_circuit_voltage_v(p, atmospheric_rs):.6g} V")

    load_r = effective_load_resistance_ohm(100e3, p)
    print("\n100-kV load stiffness")
    print(f"Rload                   = {load_r:.6g} ohm")
    for droop in (0.01, 0.05, 0.10, 0.20):
        rs = max_source_resistance_for_droop_ohm(load_r, droop)
        print(f"Rs for <= {droop*100:4.1f}% droop = {rs:.6g} ohm")
    print(f"Vload/Voc with atmospheric Rs = {loaded_voltage_fraction(atmospheric_rs, load_r):.6g}")

    print("\nMinimum source reaction")
    for eta in (1.0, 0.5, 0.1, 0.01):
        print(f"eta={eta:5.2%} -> source real-power increase >= {required_source_reaction_w(p, eta):.6g} W")

    print("\nFinite electrostatic reservoir examples")
    for c in (50e-12, 100e-12, 1e-9):
        for v in (100e3, 250e3):
            print(
                f"C={c*1e12:7.1f} pF V={v/1e3:6.1f} kV "
                f"U={reservoir_energy_j(c, v):.6g} J t@P={reservoir_duration_s(c, v, p):.6g} s"
            )

    print("\nClosed-boundary average flux floor")
    for area in (0.1, 0.5, 1.0):
        print(f"A={area:.3g} m^2 -> net inward flux >= {boundary_flux_w_per_m2(p, area):.6g} W/m^2")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
