#!/usr/bin/env python3
"""M2-V4.1: fully-floating pot/crystal threshold + energy-accounted rotor model.

Hypothesis test, not a recovered historical schematic.

The network contains six stationary nodes:
    GRID_L, GRID_R, PICKUP_L, PICKUP_R, POT_N, POT_P

plus 24 individually neutral floating rotor conductors and an optional neutral
rear metal plate.  There is no physical ground node and no hidden source.
sum(V)=0 is only a gauge condition.

Two nonlinear passive "crystal" valves rectify phase-dependent pickup
excursions into the two pot rails.  An optional resistive-load surrogate
dissipates energy across POT_P/POT_N.  Every passive transfer is checked to
reduce electrostatic field energy.

Two simulation modes are supplied:

* fixed-speed: prescribed rotation; field-energy increase caused by changing
  C(theta) is booked as mechanical shaft work.
* free-rotor: no external shaft source; the same field-energy change is taken
  from / returned to rotor kinetic energy, with optional friction.

Thus a threshold-induced metal-plate collapse can be studied without treating
the plate as ground or smuggling in an energy source.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
import argparse
import math
from typing import Iterable, List, Sequence, Tuple

TAU = 2.0 * math.pi
NAMES = ("GRID_L", "GRID_R", "PICKUP_L", "PICKUP_R", "POT_N", "POT_P")
GL, GR, PL, PR, PN, PP = range(6)


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
            f = m[i][k] / pivot
            if f == 0.0:
                continue
            for j in range(k, n + 1):
                m[i][j] -= f * m[k][j]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        rhs = m[i][n] - sum(m[i][j] * x[j] for j in range(i + 1, n))
        x[i] = rhs / m[i][i]
    return x


@dataclass(frozen=True)
class Config:
    sectors: int = 24
    steps_per_rev: int = 192
    revolutions: int = 30
    rpm: float = 30.0

    aperture_half_width_deg: float = 8.0
    pickup_phase_deg: float = 45.0

    # stationary pair capacitances
    grid_pickup_same_side_f: float = 2.0e-12
    grid_cross_f: float = 0.10e-12
    pickup_cross_f: float = 0.10e-12
    pot_pair_f: float = 120.0e-12
    pot_to_opposite_grid_f: float = 18.0e-12
    pot_to_same_pickup_f: float = 2.0e-12

    # neutral rotor-wire star couplings
    rotor_floor_f: float = 0.005e-12
    rotor_grid_peak_f: float = 1.20e-12
    rotor_pickup_peak_f: float = 0.80e-12

    # optional neutral rear plate; stronger coupling to rear pickups
    plate_scale: float = 0.0
    plate_grid_coupling_f: float = 0.20e-12
    plate_pickup_coupling_f: float = 3.0e-12
    plate_pot_coupling_f: float = 0.50e-12

    # nonlinear passive crystal threshold
    crystal_threshold_v: float = 100.0
    crystal_relaxation: float = 0.60
    crystal_passes: int = 2

    # one-time equal/opposite seed on the two grids. No later source is injected.
    # This represents an initial electrostatic asymmetry after hand-start/charging,
    # not a sustained supply.
    seed_grid_charge_c: float = 5.0e-9

    # optional load surrogate across the two pot rails.
    # 0 => open circuit. Higher fraction removes more differential charge/event.
    load_relaxation: float = 0.0

    # free-rotor parameters
    rotor_inertia_kg_m2: float = 1.5e-3
    friction_torque_nm: float = 0.0

    @property
    def omega0(self) -> float:
        return self.rpm * TAU / 60.0


@dataclass
class TransferStats:
    crystal_events: int = 0
    crystal_charge_c: float = 0.0
    crystal_loss_j: float = 0.0


@dataclass
class Result:
    mode: str
    pot_voltage_v: List[float]
    pickup_excursion_v: List[float]
    crystal_events: int
    crystal_charge_c: float
    mechanical_work_j: float
    crystal_loss_j: float
    load_energy_j: float
    initial_field_j: float
    final_field_j: float
    initial_kinetic_j: float
    final_kinetic_j: float
    friction_loss_j: float
    final_rpm: float
    stopped: bool
    residual_j: float

    @property
    def late_gain(self) -> float:
        if len(self.pot_voltage_v) < 2 or abs(self.pot_voltage_v[-2]) < 1e-30:
            return float("nan")
        return abs(self.pot_voltage_v[-1] / self.pot_voltage_v[-2])


class Network:
    def __init__(self, cfg: Config):
        self.cfg = cfg

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
        c = _zeros(6)

        _add_pair(c, GL, PL, cfg.grid_pickup_same_side_f)
        _add_pair(c, GR, PR, cfg.grid_pickup_same_side_f)
        _add_pair(c, GL, GR, cfg.grid_cross_f)
        _add_pair(c, PL, PR, cfg.pickup_cross_f)
        _add_pair(c, PN, PP, cfg.pot_pair_f)

        # POT_P biases left grid; POT_N biases right grid (cross-coupled fields).
        _add_pair(c, PP, GL, cfg.pot_to_opposite_grid_f)
        _add_pair(c, PN, GR, cfg.pot_to_opposite_grid_f)
        _add_pair(c, PP, PL, cfg.pot_to_same_pickup_f)
        _add_pair(c, PN, PR, cfg.pot_to_same_pickup_f)

        half = math.radians(cfg.aperture_half_width_deg)
        shift = math.radians(cfg.pickup_phase_deg)
        for k in range(cfg.sectors):
            phi = theta + TAU * k / cfg.sectors
            caps = [
                cfg.rotor_floor_f + cfg.rotor_grid_peak_f * _window(phi, 0.0, half),
                cfg.rotor_floor_f + cfg.rotor_grid_peak_f * _window(phi, math.pi, half),
                cfg.rotor_floor_f + cfg.rotor_pickup_peak_f * _window(phi, shift, half),
                cfg.rotor_floor_f + cfg.rotor_pickup_peak_f * _window(phi, math.pi + shift, half),
                cfg.rotor_floor_f,
                cfg.rotor_floor_f,
            ]
            self._eliminate_neutral_star(c, caps)

        if cfg.plate_scale > 0.0:
            s = cfg.plate_scale
            caps = [
                s * cfg.plate_grid_coupling_f,
                s * cfg.plate_grid_coupling_f,
                s * cfg.plate_pickup_coupling_f,
                s * cfg.plate_pickup_coupling_f,
                s * cfg.plate_pot_coupling_f,
                s * cfg.plate_pot_coupling_f,
            ]
            self._eliminate_neutral_star(c, caps)

        return c

    @staticmethod
    def voltages_from_matrix(c: Sequence[Sequence[float]], q: Sequence[float]) -> List[float]:
        if abs(sum(q)) > max(1e-22, max((abs(x) for x in q), default=0.0) * 1e-12):
            raise ValueError("fully floating network requires total free charge = 0")
        n = len(q)
        a = _zeros(n + 1)
        b = list(q) + [0.0]
        for i in range(n):
            for j in range(n):
                a[i][j] = c[i][j]
            a[i][n] = 1.0
            a[n][i] = 1.0
        return _solve(a, b)[:n]

    def voltages(self, theta: float, q: Sequence[float]) -> List[float]:
        return self.voltages_from_matrix(self.matrix(theta), q)

    def energy(self, theta: float, q: Sequence[float], v: Sequence[float] | None = None) -> float:
        if v is None:
            v = self.voltages(theta, q)
        return 0.5 * _dot(q, v)

    def transfer_ceff(self, theta: float, a: int, b: int) -> float:
        dq = [0.0] * 6
        dq[a] = -1.0
        dq[b] = +1.0
        dv = self.voltages(theta, dq)
        slope = dv[a] - dv[b]
        if slope >= 0.0:
            raise ValueError("unexpected passive transfer sensitivity")
        return -1.0 / slope

    def passive_transfer(
        self,
        theta: float,
        q: Sequence[float],
        a: int,
        b: int,
        threshold_v: float,
        relaxation: float,
    ) -> Tuple[List[float], float, float, bool]:
        """Move positive charge a->b only if Va-Vb exceeds threshold."""
        out = list(q)
        v0 = self.voltages(theta, out)
        excess = v0[a] - v0[b] - threshold_v
        if excess <= 0.0 or relaxation <= 0.0:
            return out, 0.0, 0.0, False
        ceff = self.transfer_ceff(theta, a, b)
        dq = relaxation * ceff * excess
        u0 = self.energy(theta, out, v0)
        out[a] -= dq
        out[b] += dq
        u1 = self.energy(theta, out)
        tol = max(1e-24, abs(u0) * 1e-10)
        if u1 > u0 + tol:
            raise RuntimeError("passive transfer increased field energy")
        return out, max(0.0, u0 - u1), abs(dq), True

    def crystal_step(self, theta: float, q: Sequence[float]) -> Tuple[List[float], TransferStats]:
        """Mirrored rectification into the two pot rails."""
        out = list(q)
        stats = TransferStats()
        for _ in range(self.cfg.crystal_passes):
            for a, b in ((PL, PP), (PN, PR)):
                out, loss, dq, on = self.passive_transfer(
                    theta, out, a, b,
                    self.cfg.crystal_threshold_v,
                    self.cfg.crystal_relaxation,
                )
                stats.crystal_loss_j += loss
                stats.crystal_charge_c += dq
                stats.crystal_events += int(on)
        return out, stats

    def load_step(self, theta: float, q: Sequence[float]) -> Tuple[List[float], float]:
        """Passive discrete load across POT_P -> POT_N."""
        if self.cfg.load_relaxation <= 0.0:
            return list(q), 0.0
        out, loss, _, _ = self.passive_transfer(
            theta, q, PP, PN, 0.0, self.cfg.load_relaxation
        )
        return out, loss


def _initial_charge(cfg: Config) -> List[float]:
    # Equal/opposite one-time grid charge; whole machine remains net neutral.
    return [cfg.seed_grid_charge_c, -cfg.seed_grid_charge_c, 0.0, 0.0, 0.0, 0.0]


def _record(net: Network, theta: float, q: Sequence[float]) -> Tuple[float, float]:
    v = net.voltages(theta, q)
    return v[PP] - v[PN], max(v[PL], v[PR]) - min(v[PL], v[PR])


def simulate_fixed(cfg: Config) -> Result:
    net = Network(cfg)
    q = _initial_charge(cfg)
    theta = 0.0
    u = net.energy(theta, q)
    initial_u = u
    mech = 0.0
    crystal_loss = 0.0
    load_energy = 0.0
    crystal_events = 0
    crystal_charge = 0.0
    pots: List[float] = []
    pickups: List[float] = []

    total_steps = cfg.revolutions * cfg.steps_per_rev
    dtheta = TAU / cfg.steps_per_rev
    for step in range(1, total_steps + 1):
        theta_new = theta + dtheta

        # Geometry change at fixed charge: external shaft work.
        u_rot = net.energy(theta_new, q)
        mech += u_rot - u
        theta = theta_new
        u = u_rot

        q, cs = net.crystal_step(theta, q)
        crystal_loss += cs.crystal_loss_j
        crystal_events += cs.crystal_events
        crystal_charge += cs.crystal_charge_c
        u = net.energy(theta, q)

        q, load_loss = net.load_step(theta, q)
        load_energy += load_loss
        u = net.energy(theta, q)

        if step % cfg.steps_per_rev == 0:
            pv, px = _record(net, theta, q)
            pots.append(pv)
            pickups.append(px)

    residual = initial_u + mech - crystal_loss - load_energy - u
    return Result(
        mode="fixed",
        pot_voltage_v=pots,
        pickup_excursion_v=pickups,
        crystal_events=crystal_events,
        crystal_charge_c=crystal_charge,
        mechanical_work_j=mech,
        crystal_loss_j=crystal_loss,
        load_energy_j=load_energy,
        initial_field_j=initial_u,
        final_field_j=u,
        initial_kinetic_j=0.0,
        final_kinetic_j=0.0,
        friction_loss_j=0.0,
        final_rpm=cfg.rpm,
        stopped=False,
        residual_j=residual,
    )


def simulate_free_rotor(cfg: Config, max_revolutions: float | None = None) -> Result:
    """Energy-consistent free-rotor stepping with no external shaft input."""
    net = Network(cfg)
    q = _initial_charge(cfg)
    theta = 0.0
    u = net.energy(theta, q)
    initial_u = u
    omega = cfg.omega0
    kinetic = 0.5 * cfg.rotor_inertia_kg_m2 * omega * omega
    initial_k = kinetic

    crystal_loss = 0.0
    load_energy = 0.0
    friction_loss = 0.0
    crystal_events = 0
    crystal_charge = 0.0
    pots: List[float] = []
    pickups: List[float] = []

    dtheta_nom = TAU / cfg.steps_per_rev
    max_steps = int((max_revolutions or cfg.revolutions) * cfg.steps_per_rev)
    stopped = False

    for step in range(1, max_steps + 1):
        theta_new = theta + dtheta_nom
        u_rot = net.energy(theta_new, q)
        dfield = u_rot - u

        friction = cfg.friction_torque_nm * dtheta_nom
        needed = max(0.0, dfield) + friction
        released = max(0.0, -dfield)

        if kinetic + released <= needed + 1e-18:
            friction_loss += kinetic
            kinetic = 0.0
            stopped = True
            break

        kinetic = kinetic - dfield - friction
        friction_loss += friction
        theta = theta_new
        u = u_rot

        q, cs = net.crystal_step(theta, q)
        crystal_loss += cs.crystal_loss_j
        crystal_events += cs.crystal_events
        crystal_charge += cs.crystal_charge_c
        u = net.energy(theta, q)

        q, load_loss = net.load_step(theta, q)
        load_energy += load_loss
        u = net.energy(theta, q)

        omega = math.sqrt(max(0.0, 2.0 * kinetic / cfg.rotor_inertia_kg_m2))
        if step % cfg.steps_per_rev == 0:
            pv, px = _record(net, theta, q)
            pots.append(pv)
            pickups.append(px)

    final_rpm = omega * 60.0 / TAU if kinetic > 0.0 else 0.0
    residual = initial_u + initial_k - u - kinetic - crystal_loss - load_energy - friction_loss
    return Result(
        mode="free",
        pot_voltage_v=pots,
        pickup_excursion_v=pickups,
        crystal_events=crystal_events,
        crystal_charge_c=crystal_charge,
        mechanical_work_j=initial_k - kinetic - friction_loss,
        crystal_loss_j=crystal_loss,
        load_energy_j=load_energy,
        initial_field_j=initial_u,
        final_field_j=u,
        initial_kinetic_j=initial_k,
        final_kinetic_j=kinetic,
        friction_loss_j=friction_loss,
        final_rpm=final_rpm,
        stopped=stopped,
        residual_j=residual,
    )


def threshold_sweep(
    base: Config,
    thresholds_v: Iterable[float],
    plate_scales: Iterable[float],
) -> List[Tuple[float, float, Result]]:
    out = []
    for th in thresholds_v:
        for ps in plate_scales:
            cfg = replace(base, crystal_threshold_v=float(th), plate_scale=float(ps))
            out.append((float(th), float(ps), simulate_fixed(cfg)))
    return out


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--plate", type=float, default=0.0)
    p.add_argument("--threshold-v", type=float, default=100.0)
    p.add_argument("--rpm", type=float, default=30.0)
    p.add_argument("--revolutions", type=int, default=30)
    p.add_argument("--load-relax", type=float, default=0.0)
    p.add_argument("--free-rotor", action="store_true")
    p.add_argument("--sweep", action="store_true")
    args = p.parse_args(argv)

    cfg = Config(
        plate_scale=args.plate,
        crystal_threshold_v=args.threshold_v,
        rpm=args.rpm,
        revolutions=args.revolutions,
        load_relaxation=args.load_relax,
    )
    r = simulate_free_rotor(cfg) if args.free_rotor else simulate_fixed(cfg)
    print("M2-V4.1 fully-floating pot/crystal model")
    print("No ground node, no hidden source; threshold element is passive.")
    print(f"mode                     = {r.mode}")
    print(f"plate scale              = {cfg.plate_scale:.6g}")
    print(f"crystal threshold        = {cfg.crystal_threshold_v:.6g} V")
    print(f"crystal events           = {r.crystal_events}")
    print(f"crystal |dQ|             = {r.crystal_charge_c:.6g} C")
    print(f"mechanical work          = {r.mechanical_work_j:.6g} J")
    print(f"load energy              = {r.load_energy_j:.6g} J")
    print(f"crystal loss             = {r.crystal_loss_j:.6g} J")
    print(f"final field energy       = {r.final_field_j:.6g} J")
    if r.pot_voltage_v:
        print(f"final pot differential   = {r.pot_voltage_v[-1]:.6g} V")
        print(f"late pot gain            = {r.late_gain:.9g}")
    if r.mode == "free":
        print(f"initial/final kinetic    = {r.initial_kinetic_j:.6g} / {r.final_kinetic_j:.6g} J")
        print(f"final rpm                = {r.final_rpm:.6g}")
        print(f"stopped                  = {r.stopped}")
    print(f"energy residual          = {r.residual_j:.3g} J")

    if args.sweep:
        print("\nthreshold / plate sweep")
        print(f"{'Vth':>8s} {'plate':>8s} {'events':>8s} {'Vpot':>12s} {'Wmech[J]':>12s}")
        for th, ps, rr in threshold_sweep(
            cfg,
            thresholds_v=(0, 10, 20, 30, 40, 50, 75, 100, 150),
            plate_scales=(0, 0.5, 1, 2, 5, 10),
        ):
            vpot = rr.pot_voltage_v[-1] if rr.pot_voltage_v else float("nan")
            print(f"{th:8.3g} {ps:8.3g} {rr.crystal_events:8d} {vpot:12.6g} {rr.mechanical_work_j:12.6g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
