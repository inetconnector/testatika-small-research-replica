#!/usr/bin/env python3
"""M2-V4.4: floating return-path and local-field source bounds.

A device with no galvanic earth connection still needs a closed displacement-
current or charge-exchange loop to receive sustained external power.

V4.4 adds two constraints omitted by the deliberately generous V4.3 bounds:

1. capacitive environmental pickup needs an input AND return capacitance; the
   effective coupling is their series capacitance,
2. a compact floating atmospheric device normally sees a local potential
   difference DeltaV ~= E*h, not the full earth-ionosphere potential, unless a
   separate mechanism couples it to the remote ionosphere.

These are source-side bounds only, not a historical Testatika circuit.
"""
from __future__ import annotations

import argparse
import math
from typing import Sequence

TAU = 2.0 * math.pi


def series_capacitance(c1_f: float, c2_f: float) -> float:
    if c1_f <= 0 or c2_f <= 0:
        raise ValueError("capacitances must be positive")
    return c1_f * c2_f / (c1_f + c2_f)


def capacitive_power_bound_two_port(c1_f: float, c2_f: float, v_rms: float, f_hz: float) -> float:
    if v_rms < 0 or f_hz < 0:
        raise ValueError("voltage/frequency must be non-negative")
    ceq = series_capacitance(c1_f, c2_f)
    return TAU * f_hz * ceq * v_rms * v_rms


def equal_each_capacitance_required(power_w: float, v_rms: float, f_hz: float) -> float:
    """If C1=C2=C, Ceq=C/2; return optimistic minimum C on each side."""
    if power_w < 0 or v_rms <= 0 or f_hz <= 0:
        raise ValueError("power non-negative; voltage/frequency positive")
    ceq = power_w / (TAU * f_hz * v_rms * v_rms)
    return 2.0 * ceq


def local_field_potential(field_v_m: float, separation_m: float) -> float:
    if field_v_m < 0 or separation_m < 0:
        raise ValueError("field and separation must be non-negative")
    return field_v_m * separation_m


def two_port_power(v1: float, i1: float, v2: float, i2: float, tol_a: float = 1e-15) -> float:
    """External electrical power into a charge-neutral floating device.

    Sustained charge neutrality requires i1+i2 ~= 0. Positive result means
    net source power entering the device.
    """
    if abs(i1 + i2) > tol_a:
        raise ValueError("sustained floating two-port requires i1 + i2 = 0")
    return v1 * i1 + v2 * i2


def current_required_for_local_field(power_w: float, field_v_m: float, separation_m: float) -> float:
    dv = local_field_potential(field_v_m, separation_m)
    if power_w < 0 or dv <= 0:
        raise ValueError("power non-negative and local potential positive")
    return power_w / dv


def local_atmospheric_area_required(
    power_w: float,
    field_v_m: float,
    separation_m: float,
    current_density_a_m2: float,
) -> float:
    if current_density_a_m2 <= 0:
        raise ValueError("current density must be positive")
    dv = local_field_potential(field_v_m, separation_m)
    if power_w < 0 or dv <= 0:
        raise ValueError("power non-negative and local potential positive")
    return power_w / (current_density_a_m2 * dv)


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--power-w", type=float, default=100.0)
    p.add_argument("--field-v-m", type=float, default=100.0)
    p.add_argument("--height-m", type=float, default=0.5)
    args = p.parse_args(argv)

    each_230 = equal_each_capacitance_required(args.power_w, 230.0, 50.0)
    each_10k = equal_each_capacitance_required(args.power_w, 10_000.0, 50.0)
    dv = local_field_potential(args.field_v_m, args.height_m)
    i = current_required_for_local_field(args.power_w, args.field_v_m, args.height_m)
    area = local_atmospheric_area_required(
        args.power_w, args.field_v_m, args.height_m, 2e-12
    )

    print("M2-V4.4 floating return-path / local-field bounds")
    print(f"target power                         = {args.power_w:.6g} W")
    print(f"equal C1=C2 needed @230V/50Hz       = {each_230*1e6:.6g} uF each")
    print(f"equal C1=C2 needed @10kV/50Hz       = {each_10k*1e9:.6g} nF each")
    print(f"local DeltaV @ {args.field_v_m:g} V/m, {args.height_m:g} m     = {dv:.6g} V")
    print(f"current needed at that DeltaV        = {i:.6g} A")
    print(f"ideal area @2pA/m2                  = {area/1e6:.6g} km2")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
