#!/usr/bin/env python3
"""M2-V4.9: sensitivity of the V4.8 Crystal gate window to non-ideal collection.

Research model only; not a recovered historical Testatika schematic.

V4.8 deliberately used a 100% current-collection and 100% electrical-energy-capture
upper bound. V4.9 asks how quickly that gate-sensitive window collapses when either
budget is reduced.

The two efficiencies are kept separate:

- eta_current: fraction of the V4.6 ideal ion-pair saturation current that reaches the
  intended differential gate direction;
- eta_energy: fraction of radioactive decay power that is allowed to appear as added
  electrostatic field energy in the deliberately favorable V4.7/V4.8 pump model.

Neither parameter is asserted to equal a historical value. The sweep is a robustness
and falsification diagnostic.

Safety: simulation only. Do not use radioactive consumer products or minerals in a
replica. Physical gate tests should use a controlled non-radioactive, current- and
energy-limited surrogate.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
import argparse
from typing import Iterable, List, Sequence, Tuple

from m2_v4_2_multiphase_corona import Config
from m2_v4_7_radioionization_integration import RadioConfig
from m2_v4_8_workpoint_window import critical_plate_scale, seed_window_nc


@dataclass(frozen=True)
class SensitivityRow:
    eta_current: float
    eta_energy: float
    seed_radio_min_nc: float
    passive_seed_nc: float
    window_nc: float
    voltage_deficit_covered_v: float
    critical_plate_scale: float


def evaluate(
    base_cfg: Config,
    base_radio: RadioConfig,
    eta_current: float,
    eta_energy: float,
    duration_s: float | None = None,
) -> SensitivityRow:
    if not 0.0 <= eta_current <= 1.0:
        raise ValueError("eta_current must be between 0 and 1")
    if not 0.0 <= eta_energy <= 1.0:
        raise ValueError("eta_energy must be between 0 and 1")

    radio = replace(
        base_radio,
        collection_efficiency=eta_current,
        electrical_energy_capture_efficiency=eta_energy,
    )
    w = seed_window_nc(base_cfg, radio, plate_scale=0.0, duration_s=duration_s)
    crit = critical_plate_scale(base_cfg, radio, duration_s=duration_s)
    return SensitivityRow(
        eta_current=eta_current,
        eta_energy=eta_energy,
        seed_radio_min_nc=w.seed_radio_min_nc,
        passive_seed_nc=w.seed_no_radio_threshold_nc,
        window_nc=w.width_nc,
        voltage_deficit_covered_v=w.voltage_deficit_covered_v,
        critical_plate_scale=crit,
    )


def equal_efficiency_sweep(
    base_cfg: Config,
    base_radio: RadioConfig,
    efficiencies: Iterable[float],
    duration_s: float | None = None,
) -> List[SensitivityRow]:
    return [evaluate(base_cfg, base_radio, e, e, duration_s=duration_s) for e in efficiencies]


def split_efficiency_sweep(
    base_cfg: Config,
    base_radio: RadioConfig,
    pairs: Iterable[Tuple[float, float]],
    duration_s: float | None = None,
) -> List[SensitivityRow]:
    return [evaluate(base_cfg, base_radio, ei, ee, duration_s=duration_s) for ei, ee in pairs]


def robustness_class(row: SensitivityRow) -> str:
    """Descriptive model-only classification, not a physical probability."""
    if row.voltage_deficit_covered_v >= 10.0:
        return "broad"
    if row.voltage_deficit_covered_v >= 1.0:
        return "multi-volt"
    if row.voltage_deficit_covered_v >= 0.1:
        return "sub-volt"
    if row.voltage_deficit_covered_v > 0.0:
        return "fine-tuned"
    return "none"


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--seed-nc", type=float, default=5.0)
    p.add_argument("--rpm", type=float, default=15.0)
    p.add_argument("--activity-bq", type=float, default=10_000.0)
    p.add_argument("--energy-mev", type=float, default=5.0)
    p.add_argument("--crystal-knee-v", type=float, default=100.0)
    p.add_argument("--duration-s", type=float, default=None)
    p.add_argument("--eta-current", type=float, default=None)
    p.add_argument("--eta-energy", type=float, default=None)
    args = p.parse_args(argv)

    cfg = Config(
        rpm=args.rpm,
        seed_grid_charge_c=args.seed_nc * 1e-9,
        crystal_knee_v=args.crystal_knee_v,
    )
    radio = RadioConfig(
        activity_bq=args.activity_bq,
        deposited_energy_mev_per_decay=args.energy_mev,
        collection_efficiency=1.0,
        electrical_energy_capture_efficiency=1.0,
    )
    duration = args.duration_s if args.duration_s is not None else 60.0 / cfg.rpm

    print("M2-V4.9 gate-efficiency sensitivity")
    print("Model-only robustness sweep; not a historical efficiency claim.")
    print(f"duration                  = {duration:.6g} s")

    if args.eta_current is not None or args.eta_energy is not None:
        ei = 1.0 if args.eta_current is None else args.eta_current
        ee = 1.0 if args.eta_energy is None else args.eta_energy
        row = evaluate(cfg, radio, ei, ee, duration_s=duration)
        print(f"eta current / energy      = {ei:.6g} / {ee:.6g}")
        print(f"radio-min seed            = {row.seed_radio_min_nc:.6g} nC")
        print(f"passive threshold seed    = {row.passive_seed_nc:.6g} nC")
        print(f"candidate seed window     = {row.window_nc:.6g} nC")
        print(f"covered voltage deficit   = {row.voltage_deficit_covered_v:.6g} V")
        print(f"critical plate scale      = {row.critical_plate_scale:.6g}")
        print(f"model robustness class    = {robustness_class(row)}")
        return 0

    print("\nequal current/energy efficiency sweep")
    print(f"{'eta':>8s} {'radio-min[nC]':>14s} {'window[nC]':>11s} {'deficit[V]':>11s} {'platecrit':>10s} {'class':>12s}")
    for row in equal_efficiency_sweep(
        cfg,
        radio,
        (1.0, 0.3, 0.1, 0.03, 0.01, 0.003, 0.001),
        duration_s=duration,
    ):
        print(
            f"{row.eta_current:8.3g} {row.seed_radio_min_nc:14.6g} "
            f"{row.window_nc:11.6g} {row.voltage_deficit_covered_v:11.6g} "
            f"{row.critical_plate_scale:10.6g} {robustness_class(row):>12s}"
        )

    print("\nseparate current-vs-energy sensitivity")
    print(f"{'etaI':>8s} {'etaE':>8s} {'deficit[V]':>11s} {'platecrit':>10s}")
    for row in split_efficiency_sweep(
        cfg,
        radio,
        ((1.0, 0.1), (0.1, 1.0), (0.1, 0.1), (1.0, 0.01), (0.01, 1.0), (0.01, 0.01)),
        duration_s=duration,
    ):
        print(
            f"{row.eta_current:8.3g} {row.eta_energy:8.3g} "
            f"{row.voltage_deficit_covered_v:11.6g} {row.critical_plate_scale:10.6g}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
