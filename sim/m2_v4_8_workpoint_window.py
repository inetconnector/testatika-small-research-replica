#!/usr/bin/env python3
"""M2-V4.8: Crystal work-point window under source-limited ionization bias.

Research model only; not a recovered historical Testatika schematic.

V4.8 asks a narrower question than V4.7:

    How close must the passive rotor/Grid/Pickup network already be to the Crystal
    knee for a pA/nA-scale ionization source to change the commutation state, and
    how strongly can a floating rear plate move the machine out of that window?

The calculation uses the exact V4.2 Maxwell-capacitance matrix at a selected rotor
phase, but it intentionally computes an *optimistic upper bound* for the ionization
bias over a finite time. The total V4.7 source current and source power are shared
across all stationary phases. A gate can only advance as far as BOTH limits allow:

    DeltaQ <= I_share * t
    DeltaU <= P_share * t

For a positive Crystal drive V and effective differential capacitance Ceff,

    V_charge = V + I_share*t/Ceff
    V_energy = sqrt(V^2 + 2*P_share*t/Ceff)
    V_bound = min(V_charge, V_energy)

This is deliberately favorable to the radioionization hypothesis. Real collection,
recombination, wall losses, geometry, phase duty cycle and Crystal loading can only
reduce the effect.

Safety: simulation only. Do not use radioactive consumer products or minerals in a
replica. A physical gate test should use a controlled non-radioactive, current-limited
surrogate.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
import argparse
import math
from typing import Iterable, List, Sequence

from m2_v4_2_multiphase_corona import Config, Network, _initial_charge
from m2_v4_7_radioionization_integration import RadioConfig


@dataclass(frozen=True)
class GateSnapshot:
    station: int
    drive_v: float
    margin_v: float
    ceff_f: float
    charge_limited_v: float
    energy_limited_v: float
    bound_v: float
    crosses_knee: bool


@dataclass(frozen=True)
class SeedWindow:
    plate_scale: float
    seed_radio_min_nc: float
    seed_no_radio_threshold_nc: float
    width_nc: float
    initial_drive_at_radio_min_v: float
    voltage_deficit_covered_v: float


def crystal_drive_v(cfg: Config, voltages: Sequence[float], station: int) -> float:
    """Forward Crystal drive used by the mirrored V4.2 commutator."""
    p = cfg.pickup(station)
    if station % 2 == 0:
        return voltages[p] - voltages[cfg.pot_p]
    return voltages[cfg.pot_n] - voltages[p]


def initial_gate_snapshot(
    cfg: Config,
    radio: RadioConfig,
    station: int = 0,
    phase: int = 0,
    duration_s: float | None = None,
) -> GateSnapshot:
    """Optimistic finite-time ionization bound for one Crystal gate.

    The V4.7 total source current/power is divided equally among ``cfg.stations``.
    The expression below is exact for the local linear differential mode while the
    capacitance matrix is held at the selected rotor phase. It is an upper bound for
    the real rotating/nonlinear machine.
    """
    if not (0 <= station < cfg.stations):
        raise ValueError("station out of range")
    if cfg.rpm <= 0.0:
        raise ValueError("rpm must be positive")
    if duration_s is None:
        duration_s = 60.0 / cfg.rpm  # one mechanical revolution
    if duration_s < 0.0:
        raise ValueError("duration_s must be non-negative")

    radio.validate()
    net = Network(cfg)
    q = _initial_charge(cfg)
    v = net.voltages(phase, q)
    drive = crystal_drive_v(cfg, v, station)

    p = cfg.pickup(station)
    if station % 2 == 0:
        a, b = p, cfg.pot_p
    else:
        a, b = cfg.pot_n, p
    ceff = net.transfer_ceff(phase, a, b)

    i_share = radio.current_ceiling_a / cfg.stations
    p_share = radio.electrical_power_ceiling_w / cfg.stations
    v_charge = drive + (i_share * duration_s / ceff if ceff > 0.0 else 0.0)

    # V4.8 targets the experimentally relevant near-knee positive-drive region.
    # If drive < 0, moving toward zero initially releases field energy, so the
    # simple positive-mode expression would be over-conservative. We therefore
    # report the charge ceiling as the bound for that remote regime rather than
    # pretending to have a sharp energy estimate there.
    if drive >= 0.0:
        v_energy = math.sqrt(max(0.0, drive * drive + 2.0 * p_share * duration_s / ceff))
        bound = min(v_charge, v_energy)
    else:
        v_energy = float("inf")
        bound = v_charge

    return GateSnapshot(
        station=station,
        drive_v=drive,
        margin_v=drive - cfg.crystal_knee_v,
        ceff_f=ceff,
        charge_limited_v=v_charge,
        energy_limited_v=v_energy,
        bound_v=bound,
        crosses_knee=bound >= cfg.crystal_knee_v,
    )


def _bisect_first_true(predicate, lo: float, hi: float, iterations: int = 70) -> float:
    if predicate(lo):
        return lo
    if not predicate(hi):
        raise ValueError("upper search bound does not satisfy predicate")
    for _ in range(iterations):
        mid = 0.5 * (lo + hi)
        if predicate(mid):
            hi = mid
        else:
            lo = mid
    return hi


def seed_window_nc(
    base_cfg: Config,
    radio: RadioConfig,
    plate_scale: float,
    duration_s: float | None = None,
    seed_hi_nc: float = 20.0,
) -> SeedWindow:
    """Seed interval where ionization can matter but passive drive is still sub-knee.

    ``seed_radio_min_nc`` is the smallest seed for which the optimistic ionization
    bound reaches the Crystal knee. ``seed_no_radio_threshold_nc`` is the passive
    threshold. Their difference is the candidate gate-sensitive window.
    """
    cfg0 = replace(base_cfg, plate_scale=float(plate_scale))

    def passive_cross(seed_nc: float) -> bool:
        cfg = replace(cfg0, seed_grid_charge_c=seed_nc * 1e-9)
        snap = initial_gate_snapshot(cfg, replace(radio, activity_bq=0.0), duration_s=duration_s)
        return snap.drive_v >= cfg.crystal_knee_v

    def radio_cross(seed_nc: float) -> bool:
        cfg = replace(cfg0, seed_grid_charge_c=seed_nc * 1e-9)
        return initial_gate_snapshot(cfg, radio, duration_s=duration_s).crosses_knee

    passive_seed = _bisect_first_true(passive_cross, 0.0, seed_hi_nc)
    radio_seed = _bisect_first_true(radio_cross, 0.0, seed_hi_nc)
    cfg_radio = replace(cfg0, seed_grid_charge_c=radio_seed * 1e-9)
    snap_radio = initial_gate_snapshot(cfg_radio, replace(radio, activity_bq=0.0), duration_s=duration_s)
    return SeedWindow(
        plate_scale=float(plate_scale),
        seed_radio_min_nc=radio_seed,
        seed_no_radio_threshold_nc=passive_seed,
        width_nc=max(0.0, passive_seed - radio_seed),
        initial_drive_at_radio_min_v=snap_radio.drive_v,
        voltage_deficit_covered_v=max(0.0, cfg0.crystal_knee_v - snap_radio.drive_v),
    )


def critical_plate_scale(
    base_cfg: Config,
    radio: RadioConfig,
    duration_s: float | None = None,
    plate_hi: float = 5.0,
) -> float:
    """Largest floating rear-plate scale whose optimistic gate bound still crosses."""
    def crosses(scale: float) -> bool:
        cfg = replace(base_cfg, plate_scale=scale)
        return initial_gate_snapshot(cfg, radio, duration_s=duration_s).crosses_knee

    if not crosses(0.0):
        return 0.0
    if crosses(plate_hi):
        return plate_hi
    lo, hi = 0.0, plate_hi
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        if crosses(mid):
            lo = mid
        else:
            hi = mid
    return lo


def sweep(
    base_cfg: Config,
    radio: RadioConfig,
    plate_scales: Iterable[float],
    duration_s: float | None = None,
) -> List[SeedWindow]:
    return [seed_window_nc(base_cfg, radio, p, duration_s=duration_s) for p in plate_scales]


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--seed-nc", type=float, default=5.0)
    p.add_argument("--plate", type=float, default=0.0)
    p.add_argument("--activity-bq", type=float, default=10_000.0)
    p.add_argument("--energy-mev", type=float, default=5.0)
    p.add_argument("--eta-current", type=float, default=1.0)
    p.add_argument("--eta-energy", type=float, default=1.0)
    p.add_argument("--rpm", type=float, default=15.0)
    p.add_argument("--crystal-knee-v", type=float, default=100.0)
    p.add_argument("--duration-s", type=float, default=None)
    p.add_argument("--sweep", action="store_true")
    args = p.parse_args(argv)

    cfg = Config(
        rpm=args.rpm,
        plate_scale=args.plate,
        seed_grid_charge_c=args.seed_nc * 1e-9,
        crystal_knee_v=args.crystal_knee_v,
    )
    radio = RadioConfig(
        activity_bq=args.activity_bq,
        deposited_energy_mev_per_decay=args.energy_mev,
        collection_efficiency=args.eta_current,
        electrical_energy_capture_efficiency=args.eta_energy,
    )
    duration = args.duration_s if args.duration_s is not None else 60.0 / cfg.rpm
    snap = initial_gate_snapshot(cfg, radio, duration_s=duration)
    crit = critical_plate_scale(cfg, radio, duration_s=duration)

    print("M2-V4.8 Crystal work-point window")
    print("Optimistic source-limited gate bound; not a historical wiring claim.")
    print(f"duration                  = {duration:.6g} s")
    print(f"seed                      = {args.seed_nc:.6g} nC")
    print(f"plate scale               = {args.plate:.6g}")
    print(f"initial Crystal drive     = {snap.drive_v:.6g} V")
    print(f"initial knee margin       = {snap.margin_v:.6g} V")
    print(f"gate Ceff                 = {snap.ceff_f*1e12:.6g} pF")
    print(f"charge-limited gate       = {snap.charge_limited_v:.6g} V")
    print(f"energy-limited gate       = {snap.energy_limited_v:.6g} V")
    print(f"combined upper bound      = {snap.bound_v:.6g} V")
    print(f"crosses Crystal knee      = {snap.crosses_knee}")
    print(f"critical plate scale      = {crit:.6g}")

    if args.sweep:
        print("\nplate / seed-sensitive window")
        print(f"{'plate':>7s} {'radio-min[nC]':>14s} {'passive[nC]':>13s} {'width[nC]':>11s} {'V0min[V]':>10s} {'deficit[V]':>11s}")
        for row in sweep(cfg, radio, (0.0, 0.05, 0.1, 0.2, 0.25, 0.3, 0.5, 1.0), duration_s=duration):
            print(
                f"{row.plate_scale:7.3g} {row.seed_radio_min_nc:14.6g} "
                f"{row.seed_no_radio_threshold_nc:13.6g} {row.width_nc:11.6g} "
                f"{row.initial_drive_at_radio_min_v:10.6g} {row.voltage_deficit_covered_v:11.6g}"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
