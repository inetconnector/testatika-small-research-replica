#!/usr/bin/env python3
"""M2-V4.2: fully-floating multiphase crystal/corona diagnostic.

Research model, not a recovered historical Testatika schematic.

V4.2 extends V4.1 in three directions:
* eight explicit stationary field/pickup electrodes (4 GRID + 4 PICKUP),
* a continuous forward crystal I(V) surrogate rather than a hard switch,
* a separate passive corona/ion-conduction path across each local GRID-PICKUP gap.

Two internal POT/Leydener nodes complete a 10-node floating network. Twenty-four
neutral rotor conductors and an optional neutral rear plate are eliminated as
floating stars. There is no physical ground node and no hidden source.

All nonlinear charge transfers are passive: they conserve total free charge and
may only reduce electrostatic field energy. At fixed speed, field-energy changes
caused by C(theta) are booked as shaft work. In free-rotor mode, the same changes
come from / return to rotor kinetic energy.

The model therefore asks whether a floating rear plate can move local fields
through a corona threshold and thereby shunt a continuous crystal commutation
path, while preserving a closed energy balance.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
import argparse
import math
from typing import Iterable, List, Sequence, Tuple

TAU = 2.0 * math.pi


def _zeros(n: int) -> List[List[float]]:
    return [[0.0 for _ in range(n)] for _ in range(n)]


def _dot(a: Sequence[float], b: Sequence[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def _add_pair(c: List[List[float]], i: int, j: int, value: float) -> None:
    if value < 0.0:
        raise ValueError("capacitance cannot be negative")
    c[i][i] += value
    c[j][j] += value
    c[i][j] -= value
    c[j][i] -= value


def _wrap(x: float) -> float:
    return (x + math.pi) % TAU - math.pi


def _window(angle: float, center: float, half_width: float) -> float:
    d = abs(_wrap(angle - center))
    if d >= half_width:
        return 0.0
    return 0.5 * (1.0 + math.cos(math.pi * d / half_width))


def _solve(a: Sequence[Sequence[float]], b: Sequence[float]) -> List[float]:
    n = len(a)
    m = [list(row) + [float(bi)] for row, bi in zip(a, b)]
    for k in range(n):
        p = max(range(k, n), key=lambda i: abs(m[i][k]))
        if abs(m[p][k]) < 1e-30:
            raise ValueError("singular augmented system")
        if p != k:
            m[k], m[p] = m[p], m[k]
        pivot = m[k][k]
        for i in range(k + 1, n):
            factor = m[i][k] / pivot
            if factor == 0.0:
                continue
            for j in range(k, n + 1):
                m[i][j] -= factor * m[k][j]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        rhs = m[i][n] - sum(m[i][j] * x[j] for j in range(i + 1, n))
        x[i] = rhs / m[i][i]
    return x


def smooth_forward_fraction(dv: float, knee_v: float, scale_v: float, max_relaxation: float) -> float:
    """Smooth passive forward-conduction surrogate.

    This is intentionally not a fitted semiconductor law. It provides a
    continuous monotonic turn-on around ``knee_v`` and never reverses energy flow.
    """
    if dv <= 0.0 or max_relaxation <= 0.0:
        return 0.0
    x = (dv - knee_v) / max(scale_v, 1e-12)
    if x >= 50.0:
        sigmoid = 1.0
    elif x <= -50.0:
        sigmoid = math.exp(x)
    else:
        sigmoid = 1.0 / (1.0 + math.exp(-x))
    return max_relaxation * sigmoid


def corona_fraction(abs_dv: float, onset_v: float, scale_v: float, max_relaxation: float) -> float:
    """Passive ion-conduction fraction above a local field-voltage onset."""
    if abs_dv <= onset_v or max_relaxation <= 0.0:
        return 0.0
    return max_relaxation * (1.0 - math.exp(-(abs_dv - onset_v) / max(scale_v, 1e-12)))


@dataclass(frozen=True)
class Config:
    sectors: int = 24
    stations: int = 4  # 4 GRID + 4 PICKUP = 8 stationary phase electrodes
    steps_per_rev: int = 48
    revolutions: int = 10
    rpm: float = 30.0

    aperture_half_width_deg: float = 8.0
    pickup_phase_deg: float = 7.5

    grid_pickup_local_f: float = 1.5e-12
    grid_ring_neighbor_f: float = 0.05e-12
    pickup_ring_neighbor_f: float = 0.05e-12
    pot_pair_f: float = 120.0e-12
    pot_grid_f: float = 18.0e-12
    pot_pickup_f: float = 2.0e-12

    rotor_floor_f: float = 0.003e-12
    rotor_grid_peak_f: float = 1.20e-12
    rotor_pickup_peak_f: float = 0.80e-12

    # Neutral rear-plate star; stronger to pickups than grids.
    plate_scale: float = 0.0
    plate_grid_f: float = 0.20e-12
    plate_pickup_f: float = 3.0e-12
    plate_pot_f: float = 0.50e-12

    # Continuous crystal surrogate.
    crystal_knee_v: float = 100.0
    crystal_scale_v: float = 12.0
    crystal_max_relaxation: float = 0.35
    crystal_passes: int = 2

    # Separate passive corona/ion path.
    corona_onset_v: float = 240.0
    corona_scale_v: float = 80.0
    corona_max_relaxation: float = 0.05
    corona_passes: int = 1

    # One-time bipolar seed; no later injection.
    seed_grid_charge_c: float = 5.0e-9
    min_event_charge_c: float = 1.0e-18

    # Passive load surrogate across POT_P/POT_N.
    load_relaxation: float = 0.0

    # Free rotor.
    rotor_inertia_kg_m2: float = 1.5e-3
    friction_torque_nm: float = 0.0

    @property
    def node_count(self) -> int:
        return 2 * self.stations + 2

    @property
    def pot_n(self) -> int:
        return 2 * self.stations

    @property
    def pot_p(self) -> int:
        return 2 * self.stations + 1

    @property
    def omega0(self) -> float:
        return self.rpm * TAU / 60.0

    def grid(self, i: int) -> int:
        return i

    def pickup(self, i: int) -> int:
        return self.stations + i


@dataclass
class TransferStats:
    crystal_events: int = 0
    crystal_charge_c: float = 0.0
    crystal_loss_j: float = 0.0
    corona_events: int = 0
    corona_charge_c: float = 0.0
    corona_loss_j: float = 0.0


@dataclass
class Result:
    mode: str
    pot_voltage_v: List[float]
    crystal_events: int
    crystal_charge_c: float
    corona_events: int
    corona_charge_c: float
    crystal_loss_j: float
    corona_loss_j: float
    load_energy_j: float
    mechanical_work_j: float
    initial_field_j: float
    final_field_j: float
    initial_kinetic_j: float
    final_kinetic_j: float
    friction_loss_j: float
    final_rpm: float
    stopped: bool
    residual_j: float


class Network:
    def __init__(self, cfg: Config):
        if cfg.stations < 2 or cfg.stations % 2:
            raise ValueError("stations must be an even integer >= 2")
        if cfg.steps_per_rev <= 0:
            raise ValueError("steps_per_rev must be positive")
        self.cfg = cfg
        self._matrices = [self.matrix(TAU * i / cfg.steps_per_rev) for i in range(cfg.steps_per_rev)]
        self._ceff_cache: dict[Tuple[int, int, int], float] = {}

    @staticmethod
    def _eliminate_neutral_star(c: List[List[float]], caps: Sequence[float]) -> None:
        total = sum(caps)
        if total <= 0.0:
            return
        n = len(caps)
        for i in range(n):
            c[i][i] += caps[i]
        for i in range(n):
            for j in range(n):
                c[i][j] -= caps[i] * caps[j] / total

    def matrix(self, theta: float) -> List[List[float]]:
        cfg = self.cfg
        c = _zeros(cfg.node_count)
        pn, pp = cfg.pot_n, cfg.pot_p
        _add_pair(c, pn, pp, cfg.pot_pair_f)

        for i in range(cfg.stations):
            g, p = cfg.grid(i), cfg.pickup(i)
            _add_pair(c, g, p, cfg.grid_pickup_local_f)
            _add_pair(c, g, cfg.grid((i + 1) % cfg.stations), cfg.grid_ring_neighbor_f)
            _add_pair(c, p, cfg.pickup((i + 1) % cfg.stations), cfg.pickup_ring_neighbor_f)
            rail = pp if i % 2 == 0 else pn
            _add_pair(c, rail, g, cfg.pot_grid_f)
            _add_pair(c, rail, p, cfg.pot_pickup_f)

        half = math.radians(cfg.aperture_half_width_deg)
        shift = math.radians(cfg.pickup_phase_deg)
        centers = [TAU * i / cfg.stations for i in range(cfg.stations)]
        for k in range(cfg.sectors):
            phi = theta + TAU * k / cfg.sectors
            caps: List[float] = []
            for center in centers:
                caps.append(cfg.rotor_floor_f + cfg.rotor_grid_peak_f * _window(phi, center, half))
            for center in centers:
                caps.append(cfg.rotor_floor_f + cfg.rotor_pickup_peak_f * _window(phi, center + shift, half))
            caps.extend((cfg.rotor_floor_f, cfg.rotor_floor_f))
            self._eliminate_neutral_star(c, caps)

        if cfg.plate_scale > 0.0:
            s = cfg.plate_scale
            caps = (
                [s * cfg.plate_grid_f] * cfg.stations
                + [s * cfg.plate_pickup_f] * cfg.stations
                + [s * cfg.plate_pot_f, s * cfg.plate_pot_f]
            )
            self._eliminate_neutral_star(c, caps)
        return c

    def voltages(self, phase: int, q: Sequence[float]) -> List[float]:
        if abs(sum(q)) > max(1e-22, max((abs(x) for x in q), default=0.0) * 1e-12):
            raise ValueError("fully floating network requires total free charge = 0")
        c = self._matrices[phase % self.cfg.steps_per_rev]
        n = len(q)
        a = _zeros(n + 1)
        b = list(q) + [0.0]
        for i in range(n):
            for j in range(n):
                a[i][j] = c[i][j]
            a[i][n] = 1.0
            a[n][i] = 1.0
        return _solve(a, b)[:n]

    def energy(self, phase: int, q: Sequence[float], v: Sequence[float] | None = None) -> float:
        if v is None:
            v = self.voltages(phase, q)
        return 0.5 * _dot(q, v)

    def transfer_ceff(self, phase: int, a: int, b: int) -> float:
        key = (phase % self.cfg.steps_per_rev, a, b)
        if key not in self._ceff_cache:
            dq = [0.0] * self.cfg.node_count
            dq[a] = -1.0
            dq[b] = +1.0
            dv = self.voltages(phase, dq)
            slope = dv[a] - dv[b]
            if slope >= 0.0:
                raise ValueError("unexpected passive transfer sensitivity")
            self._ceff_cache[key] = -1.0 / slope
        return self._ceff_cache[key]

    def passive_transfer(
        self, phase: int, q: Sequence[float], a: int, b: int, relaxation: float
    ) -> Tuple[List[float], float, float, bool]:
        if relaxation <= 0.0:
            return list(q), 0.0, 0.0, False
        out = list(q)
        v0 = self.voltages(phase, out)
        dv = v0[a] - v0[b]
        if dv <= 0.0:
            return out, 0.0, 0.0, False
        ceff = self.transfer_ceff(phase, a, b)
        dq = min(0.95, relaxation) * ceff * dv
        u0 = self.energy(phase, out, v0)
        out[a] -= dq
        out[b] += dq
        u1 = self.energy(phase, out)
        tol = max(1e-24, abs(u0) * 1e-10)
        if u1 > u0 + tol:
            raise RuntimeError("passive transfer increased field energy")
        return out, max(0.0, u0 - u1), abs(dq), True

    def nonlinear_step(self, phase: int, q: Sequence[float]) -> Tuple[List[float], TransferStats]:
        cfg = self.cfg
        out = list(q)
        stats = TransferStats()

        # Continuous, mirrored crystal commutation.
        for _ in range(cfg.crystal_passes):
            for i in range(cfg.stations):
                p = cfg.pickup(i)
                target = cfg.pot_p if i % 2 == 0 else cfg.pot_n
                a, b = (p, target) if i % 2 == 0 else (target, p)
                v = self.voltages(phase, out)
                fraction = smooth_forward_fraction(
                    v[a] - v[b], cfg.crystal_knee_v, cfg.crystal_scale_v,
                    cfg.crystal_max_relaxation,
                )
                out, loss, dq, on = self.passive_transfer(phase, out, a, b, fraction)
                stats.crystal_loss_j += loss
                stats.crystal_charge_c += dq
                stats.crystal_events += int(on and dq >= cfg.min_event_charge_c)

        # Separate local air/ion path. It is bidirectional and always dissipative.
        for _ in range(cfg.corona_passes):
            for i in range(cfg.stations):
                g, p = cfg.grid(i), cfg.pickup(i)
                v = self.voltages(phase, out)
                dv = v[g] - v[p]
                fraction = corona_fraction(
                    abs(dv), cfg.corona_onset_v, cfg.corona_scale_v,
                    cfg.corona_max_relaxation,
                )
                if fraction <= 0.0:
                    continue
                a, b = (g, p) if dv > 0.0 else (p, g)
                out, loss, dq, on = self.passive_transfer(phase, out, a, b, fraction)
                stats.corona_loss_j += loss
                stats.corona_charge_c += dq
                stats.corona_events += int(on and dq >= cfg.min_event_charge_c)
        return out, stats

    def load_step(self, phase: int, q: Sequence[float]) -> Tuple[List[float], float]:
        cfg = self.cfg
        if cfg.load_relaxation <= 0.0:
            return list(q), 0.0
        v = self.voltages(phase, q)
        a, b = (cfg.pot_p, cfg.pot_n) if v[cfg.pot_p] >= v[cfg.pot_n] else (cfg.pot_n, cfg.pot_p)
        out, loss, _, _ = self.passive_transfer(phase, q, a, b, cfg.load_relaxation)
        return out, loss


def _initial_charge(cfg: Config) -> List[float]:
    q = [0.0] * cfg.node_count
    for i in range(cfg.stations):
        q[cfg.grid(i)] = cfg.seed_grid_charge_c * (1.0 if i % 2 == 0 else -1.0)
    # stations is even, so the sum is zero by construction.
    return q


def simulate_fixed(cfg: Config) -> Result:
    net = Network(cfg)
    q = _initial_charge(cfg)
    phase = 0
    u = net.energy(phase, q)
    initial_u = u
    mech = crystal_loss = corona_loss = load_energy = 0.0
    crystal_events = corona_events = 0
    crystal_charge = corona_charge = 0.0
    pots: List[float] = []

    for step in range(1, cfg.revolutions * cfg.steps_per_rev + 1):
        new_phase = step % cfg.steps_per_rev
        u_rot = net.energy(new_phase, q)
        mech += u_rot - u
        phase = new_phase
        u = u_rot

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

    residual = initial_u + mech - crystal_loss - corona_loss - load_energy - u
    return Result(
        "fixed", pots, crystal_events, crystal_charge, corona_events, corona_charge,
        crystal_loss, corona_loss, load_energy, mech, initial_u, u,
        0.0, 0.0, 0.0, cfg.rpm, False, residual,
    )


def simulate_free_rotor(cfg: Config) -> Result:
    net = Network(cfg)
    q = _initial_charge(cfg)
    phase = 0
    u = net.energy(phase, q)
    initial_u = u
    kinetic = 0.5 * cfg.rotor_inertia_kg_m2 * cfg.omega0 * cfg.omega0
    initial_k = kinetic
    crystal_loss = corona_loss = load_energy = friction_loss = 0.0
    crystal_events = corona_events = 0
    crystal_charge = corona_charge = 0.0
    pots: List[float] = []
    stopped = False
    dtheta = TAU / cfg.steps_per_rev

    for step in range(1, cfg.revolutions * cfg.steps_per_rev + 1):
        new_phase = step % cfg.steps_per_rev
        u_rot = net.energy(new_phase, q)
        dfield = u_rot - u
        friction = cfg.friction_torque_nm * dtheta
        released = max(0.0, -dfield)
        needed = max(0.0, dfield) + friction
        if kinetic + released <= needed + 1e-18:
            friction_loss += kinetic
            kinetic = 0.0
            stopped = True
            break
        kinetic = kinetic - dfield - friction
        friction_loss += friction
        phase = new_phase
        u = u_rot

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

    omega = math.sqrt(max(0.0, 2.0 * kinetic / cfg.rotor_inertia_kg_m2)) if kinetic > 0.0 else 0.0
    final_rpm = omega * 60.0 / TAU
    residual = (
        initial_u + initial_k - u - kinetic - crystal_loss - corona_loss
        - load_energy - friction_loss
    )
    return Result(
        "free", pots, crystal_events, crystal_charge, corona_events, corona_charge,
        crystal_loss, corona_loss, load_energy,
        initial_k - kinetic - friction_loss, initial_u, u,
        initial_k, kinetic, friction_loss, final_rpm, stopped, residual,
    )


def plate_sweep(base: Config, scales: Iterable[float]) -> List[Tuple[float, Result]]:
    return [(float(s), simulate_fixed(replace(base, plate_scale=float(s)))) for s in scales]


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--plate", type=float, default=0.0)
    p.add_argument("--revolutions", type=int, default=10)
    p.add_argument("--steps-per-rev", type=int, default=48)
    p.add_argument("--crystal-knee-v", type=float, default=100.0)
    p.add_argument("--corona-onset-v", type=float, default=240.0)
    p.add_argument("--load-relax", type=float, default=0.0)
    p.add_argument("--free-rotor", action="store_true")
    p.add_argument("--sweep", action="store_true")
    args = p.parse_args(argv)

    cfg = Config(
        plate_scale=args.plate,
        revolutions=args.revolutions,
        steps_per_rev=args.steps_per_rev,
        crystal_knee_v=args.crystal_knee_v,
        corona_onset_v=args.corona_onset_v,
        load_relaxation=args.load_relax,
    )
    r = simulate_free_rotor(cfg) if args.free_rotor else simulate_fixed(cfg)
    print("M2-V4.2 floating multiphase crystal/corona model")
    print("No ground node, no hidden source; crystal and corona paths are passive.")
    print(f"mode                     = {r.mode}")
    print(f"plate scale              = {cfg.plate_scale:.6g}")
    print(f"crystal |dQ|             = {r.crystal_charge_c:.6g} C")
    print(f"corona |dQ|              = {r.corona_charge_c:.6g} C")
    print(f"crystal/corona events    = {r.crystal_events} / {r.corona_events}")
    print(f"load energy              = {r.load_energy_j:.6g} J")
    print(f"mechanical work          = {r.mechanical_work_j:.6g} J")
    print(f"crystal/corona loss      = {r.crystal_loss_j:.6g} / {r.corona_loss_j:.6g} J")
    print(f"final field energy       = {r.final_field_j:.6g} J")
    if r.pot_voltage_v:
        print(f"final pot differential   = {r.pot_voltage_v[-1]:.6g} V")
    if r.mode == "free":
        print(f"final rpm                = {r.final_rpm:.6g}")
        print(f"stopped                  = {r.stopped}")
    print(f"energy residual          = {r.residual_j:.3g} J")

    if args.sweep:
        print("\nfloating rear-plate sweep")
        print(f"{'plate':>8s} {'crystalQ[C]':>14s} {'coronaQ[C]':>14s} {'corona_ev':>10s} {'Vpot[V]':>12s}")
        for scale, rr in plate_sweep(cfg, (0, 0.5, 1, 2, 5)):
            vpot = rr.pot_voltage_v[-1] if rr.pot_voltage_v else float("nan")
            print(f"{scale:8.3g} {rr.crystal_charge_c:14.6g} {rr.corona_charge_c:14.6g} {rr.corona_events:10d} {vpot:12.6g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
