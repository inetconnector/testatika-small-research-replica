#!/usr/bin/env python3
"""M2-V4.5: two-environment-port source and plate-collapse bounds.

This source-side diagnostic treats a fully floating machine as receiving
external AC/RF energy only through two distinct environmental reservoirs.

Front machine port F couples to environmental reservoir A through C_front.
Rear machine port R couples to reservoir B through C_rear. A nearby metal
plate can additionally couple R toward reservoir A through C_plate_A.

At one frequency all three couplings are purely capacitive. The rear port then
sees the capacitive Thevenin equivalent

    V_R,th = (C_rear V_B + C_plate_A V_A)/(C_rear + C_plate_A)

with total rear coupling C_R = C_rear + C_plate_A.

The differential source seen by the floating device is therefore reduced as
the plate ties the rear port toward the same reservoir as the front port. The
front and rear couplings remain in series for through-device current.

The returned power is an optimistic apparent-power bound:

    P_bound = omega * C_eq * (Delta V_eff)^2

It is not a rectifier-efficiency model and not a historical Testatika claim.
Any real harvesting circuit can only deliver less unless it has another
explicit source.
"""
from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from typing import Iterable, Sequence

TAU = 2.0 * math.pi


def series_capacitance(c1_f: float, c2_f: float) -> float:
    if c1_f <= 0.0 or c2_f <= 0.0:
        raise ValueError("capacitances must be positive")
    return c1_f * c2_f / (c1_f + c2_f)


def rear_thevenin(
    c_rear_to_b_f: float,
    c_plate_to_a_f: float,
    v_a: float,
    v_b: float,
) -> tuple[float, float]:
    if c_rear_to_b_f <= 0.0 or c_plate_to_a_f < 0.0:
        raise ValueError("rear capacitance positive; plate capacitance non-negative")
    c_total = c_rear_to_b_f + c_plate_to_a_f
    v_th = (c_rear_to_b_f * v_b + c_plate_to_a_f * v_a) / c_total
    return v_th, c_total


@dataclass(frozen=True)
class TwoPortResult:
    power_bound_w: float
    delta_v_effective_rms: float
    coupling_ceq_f: float
    rear_thevenin_v_rms: float
    source_suppression: float


def two_port_plate_bound(
    c_front_to_a_f: float,
    c_rear_to_b_f: float,
    c_plate_to_a_f: float,
    source_delta_v_rms: float,
    f_hz: float,
) -> TwoPortResult:
    if c_front_to_a_f <= 0.0 or c_rear_to_b_f <= 0.0:
        raise ValueError("front/rear capacitances must be positive")
    if c_plate_to_a_f < 0.0 or source_delta_v_rms < 0.0 or f_hz < 0.0:
        raise ValueError("plate, voltage and frequency must be non-negative")

    # Symmetric source gauge: only Va-Vb matters.
    v_a = 0.5 * source_delta_v_rms
    v_b = -0.5 * source_delta_v_rms
    v_rear, c_rear_total = rear_thevenin(
        c_rear_to_b_f, c_plate_to_a_f, v_a, v_b
    )
    delta_v_eff = abs(v_a - v_rear)
    ceq = series_capacitance(c_front_to_a_f, c_rear_total)
    power = TAU * f_hz * ceq * delta_v_eff * delta_v_eff

    suppression = 1.0
    if source_delta_v_rms > 0.0:
        suppression = delta_v_eff / source_delta_v_rms

    return TwoPortResult(
        power_bound_w=power,
        delta_v_effective_rms=delta_v_eff,
        coupling_ceq_f=ceq,
        rear_thevenin_v_rms=v_rear,
        source_suppression=suppression,
    )


def required_source_delta_v(
    power_w: float,
    c_front_to_a_f: float,
    c_rear_to_b_f: float,
    c_plate_to_a_f: float,
    f_hz: float,
) -> float:
    if power_w < 0.0 or f_hz <= 0.0:
        raise ValueError("power non-negative; frequency positive")
    unit = two_port_plate_bound(
        c_front_to_a_f,
        c_rear_to_b_f,
        c_plate_to_a_f,
        1.0,
        f_hz,
    )
    if unit.power_bound_w <= 0.0:
        return math.inf
    return math.sqrt(power_w / unit.power_bound_w)


def plate_sweep(
    c_front_f: float,
    c_rear_f: float,
    source_delta_v_rms: float,
    f_hz: float,
    plate_caps_f: Iterable[float],
) -> list[tuple[float, TwoPortResult]]:
    return [
        (
            cp,
            two_port_plate_bound(
                c_front_f, c_rear_f, cp, source_delta_v_rms, f_hz
            ),
        )
        for cp in plate_caps_f
    ]


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--front-pf", type=float, default=100.0)
    p.add_argument("--rear-pf", type=float, default=100.0)
    p.add_argument("--plate-pf", type=float, default=0.0)
    p.add_argument("--dv-v", type=float, default=10_000.0)
    p.add_argument("--freq-hz", type=float, default=50.0)
    p.add_argument("--target-w", type=float, default=100.0)
    p.add_argument("--sweep", action="store_true")
    args = p.parse_args(argv)

    cf = args.front_pf * 1e-12
    cr = args.rear_pf * 1e-12
    cp = args.plate_pf * 1e-12

    r = two_port_plate_bound(cf, cr, cp, args.dv_v, args.freq_hz)
    req = required_source_delta_v(args.target_w, cf, cr, cp, args.freq_hz)

    print("M2-V4.5 two-environment-port / plate-collapse diagnostic")
    print("Optimistic source-side bound; no historical wiring claim.")
    print(f"C_front / C_rear / C_plate = {args.front_pf:g} / {args.rear_pf:g} / {args.plate_pf:g} pF")
    print(f"source DeltaV rms          = {args.dv_v:.6g} V")
    print(f"frequency                  = {args.freq_hz:.6g} Hz")
    print(f"effective DeltaV rms       = {r.delta_v_effective_rms:.6g} V")
    print(f"source-diff retention      = {r.source_suppression:.6g}")
    print(f"series C_eq                = {r.coupling_ceq_f*1e12:.6g} pF")
    print(f"optimistic power bound     = {r.power_bound_w:.6g} W")
    print(f"DeltaV needed for {args.target_w:g} W = {req:.6g} V rms")

    if args.sweep:
        print("\nPlate-to-front-environment coupling sweep")
        print(f"{'Cplate[pF]':>12s} {'DeltaVeff[V]':>14s} {'retain':>10s} {'Ceq[pF]':>10s} {'Pbound[W]':>12s}")
        vals_pf = (0, 10, 25, 50, 100, 250, 500, 1000, 10_000)
        for cppf in vals_pf:
            rr = two_port_plate_bound(cf, cr, cppf*1e-12, args.dv_v, args.freq_hz)
            print(
                f"{cppf:12.6g} {rr.delta_v_effective_rms:14.6g} "
                f"{rr.source_suppression:10.6g} {rr.coupling_ceq_f*1e12:10.6g} "
                f"{rr.power_bound_w:12.6g}"
            )

        print("\nSource DeltaV needed for target power, no plate")
        print(f"{'f[Hz]':>12s} {'DeltaVreq[V]':>16s}")
        for f in (50, 1e3, 1e4, 1e5, 1e6, 1e7):
            vv = required_source_delta_v(args.target_w, cf, cr, 0.0, f)
            print(f"{f:12.6g} {vv:16.6g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
