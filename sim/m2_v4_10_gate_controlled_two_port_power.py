#!/usr/bin/env python3
"""M2-V4.10: combine a tiny Crystal gate with an external floating two-port power path.

Research model only; not a recovered historical Testatika schematic.

V4.8/V4.9 show that a tiny source can, in an optimistic high-impedance model, alter a
Crystal commutation state. That does not solve the bulk-energy question. V4.10 therefore
asks what an independent external AC/RF two-port source would have to provide if the
Crystal merely controlled that larger path.

The source-side bound is inherited from V4.5:

    P_bound = omega * C_eq * DeltaV_env,rms^2

For a working spatial separation h between two environmental ports, a uniform-field
interpretation gives the deliberately optimistic relation

    DeltaV_env,rms ~= E_rms * h.

Thus

    E_required ~= sqrt(P / (omega*C_eq)) / h.

This is an upper-bound/apparent-power calculation, not a rectifier efficiency model.
Actual harvested real power can only be smaller for the same field/coupling unless an
additional explicit source is present.
"""
from __future__ import annotations

from dataclasses import dataclass
import argparse
import math
from typing import Iterable, List, Sequence

from m2_v4_5_two_environment_ports import (
    required_source_delta_v,
    series_capacitance,
    two_port_plate_bound,
)

TAU = 2.0 * math.pi


@dataclass(frozen=True)
class ExternalPathRequirement:
    target_power_w: float
    frequency_hz: float
    source_delta_v_rms: float
    uniform_field_rms_v_m: float
    coupling_ceq_f: float
    displacement_current_rms_a: float


def required_uniform_field_rms_v_m(
    power_w: float,
    c_front_f: float,
    c_rear_f: float,
    c_plate_f: float,
    frequency_hz: float,
    port_separation_m: float,
) -> float:
    if port_separation_m <= 0.0:
        raise ValueError("port_separation_m must be positive")
    dv = required_source_delta_v(power_w, c_front_f, c_rear_f, c_plate_f, frequency_hz)
    return dv / port_separation_m


def requirement(
    power_w: float,
    frequency_hz: float,
    c_front_f: float = 100e-12,
    c_rear_f: float = 100e-12,
    c_plate_f: float = 0.0,
    port_separation_m: float = 0.20,
) -> ExternalPathRequirement:
    if power_w < 0.0:
        raise ValueError("power_w must be non-negative")
    if frequency_hz <= 0.0:
        raise ValueError("frequency_hz must be positive")
    dv = required_source_delta_v(power_w, c_front_f, c_rear_f, c_plate_f, frequency_hz)
    field = dv / port_separation_m
    unit = two_port_plate_bound(c_front_f, c_rear_f, c_plate_f, 1.0, frequency_hz)
    ceq = unit.coupling_ceq_f
    # Current through the optimistic series capacitive path at the required source DeltaV.
    current = TAU * frequency_hz * ceq * dv
    return ExternalPathRequirement(power_w, frequency_hz, dv, field, ceq, current)


def power_bound_from_uniform_field_w(
    field_rms_v_m: float,
    frequency_hz: float,
    c_front_f: float = 100e-12,
    c_rear_f: float = 100e-12,
    c_plate_f: float = 0.0,
    port_separation_m: float = 0.20,
) -> float:
    if field_rms_v_m < 0.0:
        raise ValueError("field_rms_v_m must be non-negative")
    if frequency_hz < 0.0:
        raise ValueError("frequency_hz must be non-negative")
    if port_separation_m <= 0.0:
        raise ValueError("port_separation_m must be positive")
    dv = field_rms_v_m * port_separation_m
    return two_port_plate_bound(
        c_front_f, c_rear_f, c_plate_f, dv, frequency_hz
    ).power_bound_w


def symmetric_port_capacitance_required_f(
    power_w: float,
    frequency_hz: float,
    source_delta_v_rms: float,
) -> float:
    """Capacitance required on EACH side for symmetric Cfront=Crear=C, no plate.

    Since Ceq=C/2 and P=omega*Ceq*V^2, C = 2P/(omega*V^2).
    """
    if power_w < 0.0 or frequency_hz <= 0.0 or source_delta_v_rms <= 0.0:
        raise ValueError("power non-negative; frequency and voltage positive")
    return 2.0 * power_w / (TAU * frequency_hz * source_delta_v_rms**2)


def control_power_ratio(load_power_w: float, gate_power_w: float) -> float:
    """Control-to-load ratio only; NOT an energy-gain or COP claim."""
    if load_power_w < 0.0 or gate_power_w <= 0.0:
        raise ValueError("load non-negative; gate power positive")
    return load_power_w / gate_power_w


def frequency_sweep(
    target_power_w: float,
    frequencies_hz: Iterable[float],
    c_front_f: float,
    c_rear_f: float,
    port_separation_m: float,
) -> List[ExternalPathRequirement]:
    return [
        requirement(
            target_power_w,
            f,
            c_front_f=c_front_f,
            c_rear_f=c_rear_f,
            port_separation_m=port_separation_m,
        )
        for f in frequencies_hz
    ]


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--target-w", type=float, default=100.0)
    p.add_argument("--freq-hz", type=float, default=10e6)
    p.add_argument("--front-pf", type=float, default=100.0)
    p.add_argument("--rear-pf", type=float, default=100.0)
    p.add_argument("--plate-pf", type=float, default=0.0)
    p.add_argument("--span-m", type=float, default=0.20)
    p.add_argument("--field-v-m", type=float, default=100.0)
    p.add_argument("--gate-nw", type=float, default=8.01088317)
    p.add_argument("--sweep", action="store_true")
    args = p.parse_args(argv)

    cf = args.front_pf * 1e-12
    cr = args.rear_pf * 1e-12
    cp = args.plate_pf * 1e-12
    r = requirement(
        args.target_w,
        args.freq_hz,
        c_front_f=cf,
        c_rear_f=cr,
        c_plate_f=cp,
        port_separation_m=args.span_m,
    )
    field_bound = power_bound_from_uniform_field_w(
        args.field_v_m,
        args.freq_hz,
        cf,
        cr,
        cp,
        args.span_m,
    )

    print("M2-V4.10 gate-controlled external two-port power bound")
    print("Tiny gate may control a larger path; it does not create the larger path's energy.")
    print(f"target power              = {r.target_power_w:.6g} W")
    print(f"frequency                 = {r.frequency_hz:.6g} Hz")
    print(f"Cfront / Crear            = {args.front_pf:.6g} / {args.rear_pf:.6g} pF")
    print(f"working port separation   = {args.span_m:.6g} m")
    print(f"required DeltaV rms       = {r.source_delta_v_rms:.6g} V")
    print(f"required uniform E rms    = {r.uniform_field_rms_v_m:.6g} V/m")
    print(f"series C_eq               = {r.coupling_ceq_f*1e12:.6g} pF")
    print(f"displacement current rms  = {r.displacement_current_rms_a:.6g} A")
    print(f"Pbound at {args.field_v_m:g} V/m      = {field_bound:.6g} W")
    print(f"load/gate control ratio   = {control_power_ratio(args.target_w, args.gate_nw*1e-9):.6g} (control ratio only)")

    if args.sweep:
        print("\nfrequency sweep, no plate")
        print(f"{'f[Hz]':>12s} {'DeltaV[V]':>13s} {'E[V/m]':>13s} {'Idisp[A]':>13s}")
        for row in frequency_sweep(
            args.target_w,
            (50.0, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8),
            cf,
            cr,
            args.span_m,
        ):
            print(
                f"{row.frequency_hz:12.6g} {row.source_delta_v_rms:13.6g} "
                f"{row.uniform_field_rms_v_m:13.6g} {row.displacement_current_rms_a:13.6g}"
            )

        print("\npower bound versus uniform-field amplitude")
        print(f"{'E[V/m]':>12s} {'P@1MHz[W]':>13s} {'P@10MHz[W]':>14s} {'P@100MHz[W]':>15s}")
        for e in (1.0, 10.0, 30.0, 100.0, 300.0, 1000.0):
            p1 = power_bound_from_uniform_field_w(e, 1e6, cf, cr, 0.0, args.span_m)
            p10 = power_bound_from_uniform_field_w(e, 1e7, cf, cr, 0.0, args.span_m)
            p100 = power_bound_from_uniform_field_w(e, 1e8, cf, cr, 0.0, args.span_m)
            print(f"{e:12.6g} {p1:13.6g} {p10:14.6g} {p100:15.6g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
