#!/usr/bin/env python3
"""Reduced, energy-accounted control model of Goldie's self-excited
variable-capacitance electrostatic generator (US 3,013,201).

This is NOT a literal SPICE transcription of the patent. It preserves the
functions that matter for the Testatika comparison:

* two opposite-polarity sections,
* a charging/induction electrode and stator/collector per section,
* an electrically isolated moving capacitive link,
* rectified transfer to an output store,
* cross-feedback of a fraction of the opposite section output,
* a small one-time start reference,
* shaft work as the only sustained external energy input.

The state variable is the magnitude of one symmetric output rail. The total
stored output energy is C_store * V_rail**2 (two equal rail capacitors).

For one section, after the stator is clamped at maximum capacitance Cmax while
the induction electrode is at V_ind, the magnitude of induced free charge is

    Q = Cmax * V_ind.

During the mechanically driven stroke to Cmin, Q is held constant and field
energy rises. For both sections together,

    U_field,maxC = Cmax * V_ind**2
    U_field,minC = (Cmax**2 / Cmin) * V_ind**2
    W_mech        = Cmax * V_ind**2 * (Cmax/Cmin - 1).

The ideal open-circuit stator excursion of one section relative to its clamp is

    V_peak ~= (Cmax/Cmin - 1) * V_ind - V_diode.

With cross-feedback V_ind ~= beta * V_rail, the small-signal voltage criterion
for possible regeneration in this reduced model is

    G0 = beta * (Cmax/Cmin - 1) > 1.

That criterion is a diagnostic for this control model, not a claim about the
historical Testatika.

Every joule is assigned to startup reference input, shaft work, stored output,
load dissipation, limiter dissipation, or conversion/reset loss. Any residual
above floating-point error is treated as a model bug.
"""
from __future__ import annotations

from dataclasses import dataclass
import argparse
import csv
import math
from pathlib import Path
from typing import List, Sequence


@dataclass(frozen=True)
class GoldieConfig:
    cycles: int = 120
    event_hz: float = 12.0

    # One variable-capacitance section. Two symmetric sections are simulated.
    c_max_f: float = 100e-12
    c_min_f: float = 20e-12

    # Equal output-storage capacitor on each rail. Total energy is C_store*V^2.
    c_store_f: float = 500e-12

    # Fraction of the opposite section output returned to the induction plate.
    feedback_beta: float = 0.40

    # One-time startup reference, analogous to Goldie's small reference source.
    seed_v: float = 10.0

    diode_drop_v: float = 0.20
    transfer_efficiency: float = 0.98

    # Optional sustained load across the two output rails.
    load_resistance_ohm: float = math.inf

    # Symmetric rail magnitude limiter; full load voltage is 2*rail voltage.
    rail_limit_v: float = 50_000.0

    @property
    def capacitance_ratio(self) -> float:
        return self.c_max_f / self.c_min_f

    @property
    def ideal_small_signal_gain(self) -> float:
        return self.feedback_beta * (self.capacitance_ratio - 1.0)

    @property
    def beta_critical(self) -> float:
        rminus = self.capacitance_ratio - 1.0
        return math.inf if rminus <= 0.0 else 1.0 / rminus


@dataclass
class CycleSample:
    cycle: int
    rail_v_before: float
    induction_v: float
    peak_stator_v: float
    rail_v_after: float
    feedback_field_j: float
    mechanical_work_j: float
    returned_to_store_j: float
    conversion_loss_j: float
    load_loss_j: float
    limiter_loss_j: float
    startup_input_j: float


@dataclass
class GoldieResult:
    config: GoldieConfig
    samples: List[CycleSample]
    initial_store_j: float
    final_store_j: float
    startup_input_j: float
    mechanical_work_j: float
    conversion_loss_j: float
    load_loss_j: float
    limiter_loss_j: float
    energy_residual_j: float

    @property
    def final_rail_v(self) -> float:
        c = self.config.c_store_f
        return math.sqrt(max(self.final_store_j, 0.0) / c)

    @property
    def final_load_v(self) -> float:
        return 2.0 * self.final_rail_v

    @property
    def observed_cycle_gain(self) -> float:
        vals = [s.rail_v_after for s in self.samples]
        vals = [v for v in vals if v > max(1e-12, self.config.seed_v * 1e-6)]
        if len(vals) < 6:
            return float("nan")
        a0, a1 = vals[-6], vals[-1]
        if a0 <= 0:
            return float("nan")
        return (a1 / a0) ** (1.0 / 5.0)


def _load_decay_energy(energy_j: float, cfg: GoldieConfig) -> tuple[float, float]:
    """Dissipate output-store energy in a load between generation events."""
    if not math.isfinite(cfg.load_resistance_ohm):
        return energy_j, 0.0
    if cfg.load_resistance_ohm <= 0.0:
        return 0.0, energy_j
    c_eq = cfg.c_store_f / 2.0
    dt = 1.0 / cfg.event_hz
    # Capacitor energy decays as exp(-2t/RC).
    factor = math.exp(-2.0 * dt / (cfg.load_resistance_ohm * c_eq))
    after = energy_j * factor
    return after, energy_j - after


def simulate(cfg: GoldieConfig) -> GoldieResult:
    if cfg.cycles <= 0:
        raise ValueError("cycles must be positive")
    if cfg.c_max_f <= 0 or cfg.c_min_f <= 0 or cfg.c_store_f <= 0:
        raise ValueError("capacitances must be positive")
    if cfg.c_max_f <= cfg.c_min_f:
        raise ValueError("c_max_f must exceed c_min_f")
    if not (0.0 <= cfg.feedback_beta <= 1.0):
        raise ValueError("feedback_beta must be in [0, 1]")
    if not (0.0 < cfg.transfer_efficiency <= 1.0):
        raise ValueError("transfer_efficiency must be in (0, 1]")
    if cfg.event_hz <= 0:
        raise ValueError("event_hz must be positive")

    # Two equal output rails: E_total = C_store * Vrail^2.
    store = 0.0
    initial_store = store
    startup_total = 0.0
    mech_total = 0.0
    conversion_total = 0.0
    load_total = 0.0
    limiter_total = 0.0
    samples: List[CycleSample] = []

    ratio = cfg.capacitance_ratio

    for cycle in range(cfg.cycles):
        rail_before = math.sqrt(max(store, 0.0) / cfg.c_store_f)

        # Cross-feedback after the first event; seed is only a startup reference.
        induction_v = cfg.feedback_beta * rail_before
        if cycle == 0:
            induction_v += cfg.seed_v

        # Establishing the two max-C fields costs electrical energy.
        feedback_field = cfg.c_max_f * induction_v * induction_v
        from_store = min(store, feedback_field)
        store -= from_store
        startup = feedback_field - from_store
        startup_total += startup

        # Shaft work raises field energy while capacitance decreases.
        mechanical = cfg.c_max_f * induction_v * induction_v * (ratio - 1.0)
        mech_total += mechanical
        field_available = feedback_field + mechanical

        # Ideal rectifier threshold/open-circuit limit for each section.
        peak = max(0.0, (ratio - 1.0) * induction_v - cfg.diode_drop_v)

        # Field energy can return only until the storage rail reaches peak.
        target_store = cfg.c_store_f * peak * peak
        requested = max(0.0, target_store - store)
        returned = min(field_available * cfg.transfer_efficiency, requested)
        store += returned

        conversion_loss = field_available - returned
        conversion_total += conversion_loss

        # Voltage limiting, analogous to Goldie's suggested corona limiter.
        rail_now = math.sqrt(max(store, 0.0) / cfg.c_store_f)
        if rail_now > cfg.rail_limit_v:
            limited_store = cfg.c_store_f * cfg.rail_limit_v * cfg.rail_limit_v
            limiter_loss = store - limited_store
            store = limited_store
        else:
            limiter_loss = 0.0
        limiter_total += limiter_loss

        store, load_loss = _load_decay_energy(store, cfg)
        load_total += load_loss

        rail_after = math.sqrt(max(store, 0.0) / cfg.c_store_f)
        samples.append(CycleSample(
            cycle=cycle,
            rail_v_before=rail_before,
            induction_v=induction_v,
            peak_stator_v=peak,
            rail_v_after=rail_after,
            feedback_field_j=feedback_field,
            mechanical_work_j=mechanical,
            returned_to_store_j=returned,
            conversion_loss_j=conversion_loss,
            load_loss_j=load_loss,
            limiter_loss_j=limiter_loss,
            startup_input_j=startup,
        ))

    residual = (
        initial_store
        + startup_total
        + mech_total
        - conversion_total
        - load_total
        - limiter_total
        - store
    )
    return GoldieResult(
        config=cfg,
        samples=samples,
        initial_store_j=initial_store,
        final_store_j=store,
        startup_input_j=startup_total,
        mechanical_work_j=mech_total,
        conversion_loss_j=conversion_total,
        load_loss_j=load_total,
        limiter_loss_j=limiter_total,
        energy_residual_j=residual,
    )


def write_csv(path: Path, result: GoldieResult) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([
            "cycle", "rail_v_before", "induction_v", "peak_stator_v",
            "rail_v_after", "feedback_field_j", "mechanical_work_j",
            "returned_to_store_j", "conversion_loss_j", "load_loss_j",
            "limiter_loss_j", "startup_input_j",
        ])
        for s in result.samples:
            w.writerow([
                s.cycle, s.rail_v_before, s.induction_v, s.peak_stator_v,
                s.rail_v_after, s.feedback_field_j, s.mechanical_work_j,
                s.returned_to_store_j, s.conversion_loss_j, s.load_loss_j,
                s.limiter_loss_j, s.startup_input_j,
            ])


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--cycles", type=int, default=120)
    p.add_argument("--cmax-pf", type=float, default=100.0)
    p.add_argument("--cmin-pf", type=float, default=20.0)
    p.add_argument("--store-pf", type=float, default=500.0)
    p.add_argument("--feedback", type=float, default=0.40)
    p.add_argument("--seed-v", type=float, default=10.0)
    p.add_argument("--event-hz", type=float, default=12.0)
    p.add_argument("--limit-v", type=float, default=50_000.0)
    p.add_argument("--load-megohm", type=float, default=math.inf)
    p.add_argument("--csv", type=Path)
    args = p.parse_args(argv)

    load = math.inf if math.isinf(args.load_megohm) else args.load_megohm * 1e6
    cfg = GoldieConfig(
        cycles=args.cycles,
        event_hz=args.event_hz,
        c_max_f=args.cmax_pf * 1e-12,
        c_min_f=args.cmin_pf * 1e-12,
        c_store_f=args.store_pf * 1e-12,
        feedback_beta=args.feedback,
        seed_v=args.seed_v,
        rail_limit_v=args.limit_v,
        load_resistance_ohm=load,
    )
    r = simulate(cfg)

    print("Goldie self-excited variable-capacitance control model")
    print("US 3,013,201 functional reduction; not a literal patent netlist.")
    print(f"Cmax/Cmin              = {cfg.capacitance_ratio:.6g}")
    print(f"feedback beta          = {cfg.feedback_beta:.6g}")
    print(f"ideal small-signal G0  = {cfg.ideal_small_signal_gain:.6g}")
    print(f"critical beta          = {cfg.beta_critical:.6g}")
    print(f"final rail voltage     = {r.final_rail_v:.6g} V")
    print(f"final load voltage     = {r.final_load_v:.6g} V")
    print(f"startup input          = {r.startup_input_j:.6g} J")
    print(f"shaft work             = {r.mechanical_work_j:.6g} J")
    print(f"conversion/reset loss  = {r.conversion_loss_j:.6g} J")
    print(f"load loss              = {r.load_loss_j:.6g} J")
    print(f"limiter loss           = {r.limiter_loss_j:.6g} J")
    print(f"energy residual        = {r.energy_residual_j:.6g} J")
    if cfg.ideal_small_signal_gain > 1.0:
        print("criterion               = regenerative regime possible in this reduced model")
    else:
        print("criterion               = below reduced-model regeneration threshold")

    if args.csv:
        write_csv(args.csv, r)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
