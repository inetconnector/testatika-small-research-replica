#!/usr/bin/env python3
"""M2-V4.7: integrate a source-limited radioionization bias into V4.2.

Research model only; not a recovered historical Testatika schematic.

V4.6 estimated the *ion-pair current ceiling* from a weak radioactive source. V4.7
adds the missing energy constraint and couples that tiny current to the explicit
V4.2 floating Grid/Pickup/Pot network.

Two constraints are enforced simultaneously:

1. charge-rate ceiling: |dQ/dt| <= ideal ion-pair saturation current,
2. source-energy ceiling: any increase of electrostatic field energy caused by the
   radioionization pump is <= radioactive decay energy available during that step.

This distinction matters. ``I_sat/C`` is a useful high-impedance current scale when
an existing electric field collects ion pairs; it is NOT a license to charge an
isolated capacitor indefinitely at constant current while ignoring the energy
required to raise its voltage.

The radioionization pump is deliberately optimistic: its collection geometry is
chosen to reinforce the mirrored V4.2 Crystal drive. If even this upper-bound model
cannot explain bulk output, a real weak source certainly cannot. Radioactivity is
never modeled as a 100 W / 300 W power source.

Safety: simulation only. Do not use, dismantle or heat old gas mantles, smoke-detector
sources, radioactive minerals or other radioactive consumer products. Experimental
surrogates should be non-radioactive and current-limited.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
import argparse
import math
from typing import Iterable, List, Sequence, Tuple

from m2_v4_2_multiphase_corona import Config, Network, _initial_charge
from m2_v4_6_radioionization_gate import decay_power_w, saturation_ion_current_a

TAU = 2.0 * math.pi


@dataclass(frozen=True)
class RadioConfig:
    """Total radioionization source feeding all stations together."""

    activity_bq: float = 10_000.0
    deposited_energy_mev_per_decay: float = 5.0
    collection_efficiency: float = 1.0
    electrical_energy_capture_efficiency: float = 1.0

    def validate(self) -> None:
        if self.activity_bq < 0.0:
            raise ValueError("activity_bq must be non-negative")
        if self.deposited_energy_mev_per_decay < 0.0:
            raise ValueError("deposited_energy_mev_per_decay must be non-negative")
        if not 0.0 <= self.collection_efficiency <= 1.0:
            raise ValueError("collection_efficiency must be between 0 and 1")
        if not 0.0 <= self.electrical_energy_capture_efficiency <= 1.0:
            raise ValueError("electrical_energy_capture_efficiency must be between 0 and 1")

    @property
    def decay_power_w(self) -> float:
        self.validate()
        return decay_power_w(self.activity_bq, self.deposited_energy_mev_per_decay)

    @property
    def current_ceiling_a(self) -> float:
        self.validate()
        return saturation_ion_current_a(
            self.activity_bq,
            self.deposited_energy_mev_per_decay,
            self.collection_efficiency,
        )

    @property
    def electrical_power_ceiling_w(self) -> float:
        return self.decay_power_w * self.electrical_energy_capture_efficiency


@dataclass
class RadioStepStats:
    transferred_charge_c: float = 0.0
    source_energy_j: float = 0.0
    passive_field_loss_j: float = 0.0
    attempts: int = 0


@dataclass
class Result:
    pot_voltage_v: List[float]
    crystal_events: int
    crystal_charge_c: float
    corona_events: int
    corona_charge_c: float
    radio_charge_c: float
    radio_source_energy_j: float
    radio_available_energy_j: float
    radio_passive_loss_j: float
    crystal_loss_j: float
    corona_loss_j: float
    load_energy_j: float
    mechanical_work_j: float
    initial_field_j: float
    final_field_j: float
    residual_j: float


def max_voltage_from_source_energy_v(power_w: float, time_s: float, capacitance_f: float) -> float:
    """Absolute energy-only bound for charging a capacitor from zero.

    1/2*C*V^2 <= P*t -> V <= sqrt(2*P*t/C).
    This is independent of the ion-current ceiling and is intentionally optimistic.
    """
    if power_w < 0.0 or time_s < 0.0:
        raise ValueError("power and time must be non-negative")
    if capacitance_f <= 0.0:
        raise ValueError("capacitance must be positive")
    return math.sqrt(2.0 * power_w * time_s / capacitance_f)


def time_to_charge_cap_from_source_s(power_w: float, capacitance_f: float, voltage_v: float) -> float:
    if power_w <= 0.0 or capacitance_f <= 0.0:
        raise ValueError("power and capacitance must be positive")
    if voltage_v < 0.0:
        raise ValueError("voltage must be non-negative")
    return 0.5 * capacitance_f * voltage_v * voltage_v / power_w


def _trial_transfer(
    net: Network,
    phase: int,
    q: Sequence[float],
    src: int,
    dst: int,
    dq_c: float,
) -> Tuple[List[float], float]:
    """Transfer positive free charge src -> dst and return Delta field energy."""
    if dq_c < 0.0:
        raise ValueError("dq_c must be non-negative")
    out = list(q)
    if dq_c == 0.0:
        return out, 0.0
    u0 = net.energy(phase, out)
    out[src] -= dq_c
    out[dst] += dq_c
    u1 = net.energy(phase, out)
    return out, u1 - u0


def _energy_limited_transfer(
    net: Network,
    phase: int,
    q: Sequence[float],
    src: int,
    dst: int,
    dq_cap_c: float,
    source_energy_cap_j: float,
) -> Tuple[List[float], float, float, float]:
    """Attempt an ionization-enabled transfer with exact field-energy capping.

    Returns ``(q_new, |dQ|, source_energy_used, passive_field_loss)``.

    If the chosen transfer direction is downhill in electrostatic energy, the field
    supplies the energy and the decrease is booked as passive ionization loss. If it
    is uphill, only the explicit radioactive source-energy budget may supply it.
    """
    if dq_cap_c <= 0.0:
        return list(q), 0.0, 0.0, 0.0
    if source_energy_cap_j < 0.0:
        raise ValueError("source_energy_cap_j must be non-negative")

    trial, du_full = _trial_transfer(net, phase, q, src, dst, dq_cap_c)
    if du_full <= source_energy_cap_j + 1e-30:
        return trial, dq_cap_c, max(0.0, du_full), max(0.0, -du_full)

    # Exact energy change along a fixed charge-transfer direction is convex for a
    # linear capacitance network. Find the largest fraction satisfying the budget.
    lo, hi = 0.0, 1.0
    best_q = list(q)
    best_du = 0.0
    best_fraction = 0.0
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        cand, du = _trial_transfer(net, phase, q, src, dst, dq_cap_c * mid)
        if du <= source_energy_cap_j:
            lo = mid
            best_q, best_du, best_fraction = cand, du, mid
        else:
            hi = mid
    dq = dq_cap_c * best_fraction
    return best_q, dq, max(0.0, best_du), max(0.0, -best_du)


def radioionization_step(
    net: Network,
    phase: int,
    q: Sequence[float],
    dt_s: float,
    radio: RadioConfig,
) -> Tuple[List[float], RadioStepStats]:
    """Optimistic mirrored radio-bias step for the V4.2 Crystal path.

    The *total* source current and decay power are shared across all stations.
    Geometry is chosen to increase the same differential that the mirrored Crystal
    commutator subsequently rectifies:

    even station: POT_P -> PICKUP_i
    odd station:  PICKUP_i -> POT_N

    This is an upper-bound research topology, not a historical wiring claim.
    """
    radio.validate()
    if dt_s < 0.0:
        raise ValueError("dt_s must be non-negative")
    out = list(q)
    stats = RadioStepStats()
    if dt_s == 0.0 or radio.activity_bq == 0.0:
        return out, stats

    cfg = net.cfg
    current_total = radio.current_ceiling_a
    energy_total = radio.electrical_power_ceiling_w * dt_s
    dq_share = current_total * dt_s / cfg.stations
    energy_share = energy_total / cfg.stations

    for i in range(cfg.stations):
        p = cfg.pickup(i)
        if i % 2 == 0:
            src, dst = cfg.pot_p, p
        else:
            src, dst = p, cfg.pot_n
        out, dq, source_e, passive_loss = _energy_limited_transfer(
            net, phase, out, src, dst, dq_share, energy_share
        )
        stats.transferred_charge_c += dq
        stats.source_energy_j += source_e
        stats.passive_field_loss_j += passive_loss
        stats.attempts += 1

    if abs(sum(out) - sum(q)) > 1e-20:
        raise RuntimeError("radioionization step violated total free-charge conservation")
    if stats.source_energy_j > energy_total + max(1e-24, abs(energy_total) * 1e-9):
        raise RuntimeError("radioionization step exceeded radioactive source-energy budget")
    if stats.transferred_charge_c > current_total * dt_s + max(1e-24, abs(current_total * dt_s) * 1e-9):
        raise RuntimeError("radioionization step exceeded saturation-current charge budget")
    return out, stats


def simulate_fixed(cfg: Config, radio: RadioConfig) -> Result:
    """V4.2 fixed-speed simulation with explicit source-limited radio-bias step."""
    radio.validate()
    if cfg.rpm <= 0.0:
        raise ValueError("rpm must be positive")
    net = Network(cfg)
    q = _initial_charge(cfg)
    phase = 0
    u = net.energy(phase, q)
    initial_u = u
    mech = crystal_loss = corona_loss = load_energy = 0.0
    radio_source = radio_passive_loss = radio_charge = 0.0
    crystal_events = corona_events = 0
    crystal_charge = corona_charge = 0.0
    pots: List[float] = []
    dt = 60.0 / (cfg.rpm * cfg.steps_per_rev)
    steps = cfg.revolutions * cfg.steps_per_rev

    for step in range(1, steps + 1):
        new_phase = step % cfg.steps_per_rev
        u_rot = net.energy(new_phase, q)
        mech += u_rot - u
        phase = new_phase
        u = u_rot

        q, rs = radioionization_step(net, phase, q, dt, radio)
        radio_source += rs.source_energy_j
        radio_passive_loss += rs.passive_field_loss_j
        radio_charge += rs.transferred_charge_c
        u = net.energy(phase, q)

        q, stats = net.nonlinear_step(phase, q)
        crystal_loss += stats.crystal_loss_j
        corona_loss += stats.corona_loss_j
        crystal_events += stats.crystal_events
        corona_events += stats.corona_events
        crystal_charge += stats.crystal_charge_c
        corona_charge += stats.corona_charge_c
        u = net.energy(phase, q)

        q, load_loss = net.load_step(phase, q)
        load_energy += load_loss
        u = net.energy(phase, q)

        if step % cfg.steps_per_rev == 0:
            v = net.voltages(phase, q)
            pots.append(v[cfg.pot_p] - v[cfg.pot_n])

    total_time = steps * dt
    radio_available = radio.electrical_power_ceiling_w * total_time
    residual = (
        initial_u + mech + radio_source
        - radio_passive_loss - crystal_loss - corona_loss - load_energy - u
    )
    return Result(
        pots,
        crystal_events,
        crystal_charge,
        corona_events,
        corona_charge,
        radio_charge,
        radio_source,
        radio_available,
        radio_passive_loss,
        crystal_loss,
        corona_loss,
        load_energy,
        mech,
        initial_u,
        u,
        residual,
    )


def ion_current_sweep(
    base_cfg: Config,
    base_radio: RadioConfig,
    activities_bq: Iterable[float],
    plate_scales: Iterable[float],
) -> List[Tuple[float, float, Result]]:
    rows: List[Tuple[float, float, Result]] = []
    for plate in plate_scales:
        cfg = replace(base_cfg, plate_scale=float(plate))
        for activity in activities_bq:
            r = simulate_fixed(cfg, replace(base_radio, activity_bq=float(activity)))
            rows.append((float(plate), float(activity), r))
    return rows


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--activity-bq", type=float, default=10_000.0)
    p.add_argument("--energy-mev", type=float, default=5.0)
    p.add_argument("--eta-current", type=float, default=1.0)
    p.add_argument("--eta-energy", type=float, default=1.0)
    p.add_argument("--plate", type=float, default=0.0)
    p.add_argument("--rpm", type=float, default=15.0)
    p.add_argument("--revolutions", type=int, default=10)
    p.add_argument("--steps-per-rev", type=int, default=48)
    p.add_argument("--seed-nc", type=float, default=5.0)
    p.add_argument("--crystal-knee-v", type=float, default=100.0)
    p.add_argument("--corona-onset-v", type=float, default=240.0)
    p.add_argument("--load-relax", type=float, default=0.0)
    p.add_argument("--sweep", action="store_true")
    args = p.parse_args(argv)

    cfg = Config(
        plate_scale=args.plate,
        rpm=args.rpm,
        revolutions=args.revolutions,
        steps_per_rev=args.steps_per_rev,
        seed_grid_charge_c=args.seed_nc * 1e-9,
        crystal_knee_v=args.crystal_knee_v,
        corona_onset_v=args.corona_onset_v,
        load_relaxation=args.load_relax,
    )
    radio = RadioConfig(
        activity_bq=args.activity_bq,
        deposited_energy_mev_per_decay=args.energy_mev,
        collection_efficiency=args.eta_current,
        electrical_energy_capture_efficiency=args.eta_energy,
    )
    r = simulate_fixed(cfg, radio)
    duration = cfg.revolutions * 60.0 / cfg.rpm

    print("M2-V4.7 source-limited radioionization integration")
    print("Simulation only; radioactivity is a tiny bias/gate candidate, not bulk power.")
    print(f"duration                  = {duration:.6g} s")
    print(f"activity                  = {radio.activity_bq:.6g} Bq")
    print(f"decay/electrical P ceiling= {radio.decay_power_w:.6g} / {radio.electrical_power_ceiling_w:.6g} W")
    print(f"ion-current ceiling       = {radio.current_ceiling_a:.6g} A")
    print(f"radio |dQ|                = {r.radio_charge_c:.6g} C")
    print(f"radio source used/avail   = {r.radio_source_energy_j:.6g} / {r.radio_available_energy_j:.6g} J")
    print(f"radio passive field loss  = {r.radio_passive_loss_j:.6g} J")
    print(f"crystal |dQ| / events     = {r.crystal_charge_c:.6g} C / {r.crystal_events}")
    print(f"corona |dQ| / events      = {r.corona_charge_c:.6g} C / {r.corona_events}")
    print(f"load energy               = {r.load_energy_j:.6g} J")
    print(f"mechanical work           = {r.mechanical_work_j:.6g} J")
    if r.pot_voltage_v:
        print(f"final pot differential    = {r.pot_voltage_v[-1]:.6g} V")
    print(f"energy residual           = {r.residual_j:.3g} J")

    c_demo = 100e-12
    print("\nenergy-only radio-source bound on a 100 pF node from zero")
    print(f"Vmax after {duration:.6g} s       = {max_voltage_from_source_energy_v(radio.electrical_power_ceiling_w, duration, c_demo):.6g} V")
    if radio.electrical_power_ceiling_w > 0.0:
        print(f"time to 100 V, ideal      = {time_to_charge_cap_from_source_s(radio.electrical_power_ceiling_w, c_demo, 100.0):.6g} s")

    if args.sweep:
        print("\nactivity / floating-plate sweep")
        print(f"{'plate':>7s} {'Bq':>10s} {'radioQ[C]':>13s} {'crystalQ[C]':>13s} {'cr_ev':>7s} {'co_ev':>7s} {'Vpot[V]':>11s}")
        for plate, activity, rr in ion_current_sweep(
            cfg, radio,
            activities_bq=(0.0, 100.0, 1_000.0, 10_000.0, 100_000.0),
            plate_scales=(0.0, 0.5, 1.0, 2.0, 5.0),
        ):
            vpot = rr.pot_voltage_v[-1] if rr.pot_voltage_v else float("nan")
            print(f"{plate:7.3g} {activity:10.3g} {rr.radio_charge_c:13.5g} {rr.crystal_charge_c:13.5g} {rr.crystal_events:7d} {rr.corona_events:7d} {vpot:11.5g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
