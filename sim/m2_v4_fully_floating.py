#!/usr/bin/env python3
"""Fully-floating M2 electrostatic network diagnostic.

No node is assigned to earth/ground and no hidden voltage source is present.
The network contains four stationary nodes (GRID_L, GRID_R, PICKUP_L,
PICKUP_R), 24 individually neutral rotor conductors that are eliminated by a
Schur complement, and an optional neutral metal plate behind the machine.

The global voltage gauge is fixed only mathematically by sum(V)=0. This does
not create an electrical connection to ground.

At fixed free charge q, rotation changes C(theta); the corresponding change in
field energy is booked as mechanical work. Passive one-way valves conserve
free charge and may only reduce field energy. The model therefore tests two
specific questions:

1. Can a completely floating variable-C / diode network self-excite from a
   finite seed without an unbooked energy input?
2. Can a nearby neutral metal plate suppress the differential modulation?

This is a falsifiable reduced model, not a recovered historical schematic.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
import argparse
import math
from typing import List, Sequence, Tuple

TAU = 2.0 * math.pi
NAMES = ("GRID_L", "GRID_R", "PICKUP_L", "PICKUP_R")


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


def _gaussian_eliminate(a: Sequence[Sequence[float]], b: Sequence[float]) -> List[float]:
    """Dense solve with partial pivoting; sufficient for the tiny matrices here."""
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
    steps_per_rev: int = 96
    revolutions: int = 20
    aperture_half_width_deg: float = 10.0
    pickup_phase_deg: float = 45.0
    grid_pickup_same_side_f: float = 8.0e-12
    grid_cross_f: float = 0.12e-12
    pickup_cross_f: float = 0.12e-12
    rotor_floor_f: float = 0.01e-12
    rotor_grid_peak_f: float = 0.75e-12
    rotor_pickup_peak_f: float = 0.45e-12
    plate_scale: float = 0.0
    plate_grid_coupling_f: float = 0.25e-12
    plate_pickup_coupling_f: float = 2.0e-12
    diode_drop_v: float = 0.0
    diode_relaxation: float = 0.55
    diode_passes: int = 2
    seed_charge_c: float = 2.0e-12


class FloatingNetwork:
    def __init__(self, cfg: Config):
        self.cfg = cfg
        self._matrices = [self.matrix(TAU * i / cfg.steps_per_rev) for i in range(cfg.steps_per_rev)]

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
        c = _zeros(4)
        _add_pair(c, 0, 2, cfg.grid_pickup_same_side_f)
        _add_pair(c, 1, 3, cfg.grid_pickup_same_side_f)
        _add_pair(c, 0, 1, cfg.grid_cross_f)
        _add_pair(c, 2, 3, cfg.pickup_cross_f)
        half = math.radians(cfg.aperture_half_width_deg)
        pickup_shift = math.radians(cfg.pickup_phase_deg)
        for k in range(cfg.sectors):
            phi = theta + TAU * k / cfg.sectors
            caps = [
                cfg.rotor_floor_f + cfg.rotor_grid_peak_f * _window(phi, 0.0, half),
                cfg.rotor_floor_f + cfg.rotor_grid_peak_f * _window(phi, math.pi, half),
                cfg.rotor_floor_f + cfg.rotor_pickup_peak_f * _window(phi, pickup_shift, half),
                cfg.rotor_floor_f + cfg.rotor_pickup_peak_f * _window(phi, math.pi + pickup_shift, half),
            ]
            self._eliminate_neutral_star(c, caps)
        if cfg.plate_scale > 0.0:
            caps = [
                cfg.plate_scale * cfg.plate_grid_coupling_f,
                cfg.plate_scale * cfg.plate_grid_coupling_f,
                cfg.plate_scale * cfg.plate_pickup_coupling_f,
                cfg.plate_scale * cfg.plate_pickup_coupling_f,
            ]
            self._eliminate_neutral_star(c, caps)
        return c

    @staticmethod
    def voltages_from_matrix(c: Sequence[Sequence[float]], q: Sequence[float]) -> List[float]:
        if abs(sum(q)) > 1e-20:
            raise ValueError("fully floating network requires total free charge = 0")
        n = len(q)
        a = _zeros(n + 1)
        b = list(q) + [0.0]
        for i in range(n):
            for j in range(n):
                a[i][j] = c[i][j]
            a[i][n] = 1.0
            a[n][i] = 1.0
        return _gaussian_eliminate(a, b)[:n]

    def voltages(self, phase: int, q: Sequence[float]) -> List[float]:
        return self.voltages_from_matrix(self._matrices[phase], q)

    def energy(self, phase: int, q: Sequence[float], v: Sequence[float] | None = None) -> float:
        if v is None:
            v = self.voltages(phase, q)
        return 0.5 * _dot(q, v)

    def transfer_ceff(self, phase: int, a: int, b: int) -> float:
        dq = [0.0] * 4
        dq[a] = -1.0
        dq[b] = +1.0
        dv = self.voltages(phase, dq)
        slope = dv[a] - dv[b]
        if slope >= 0.0:
            raise ValueError("unexpected passive transfer sensitivity")
        return -1.0 / slope

    def valve_step(self, phase: int, q: Sequence[float], topology: Sequence[Tuple[int, int]]) -> Tuple[List[float], float]:
        out = list(q)
        loss = 0.0
        for _ in range(self.cfg.diode_passes):
            for a, b in topology:
                v0 = self.voltages(phase, out)
                excess = v0[a] - v0[b] - self.cfg.diode_drop_v
                if excess <= 0.0:
                    continue
                dq = self.cfg.diode_relaxation * self.transfer_ceff(phase, a, b) * excess
                u0 = self.energy(phase, out, v0)
                out[a] -= dq
                out[b] += dq
                u1 = self.energy(phase, out)
                if u1 > u0 + max(1e-24, abs(u0) * 1e-10):
                    raise RuntimeError("passive valve increased field energy")
                loss += max(0.0, u0 - u1)
        return out, loss


CROSS_TOPOLOGY = ((2, 1), (3, 0))


@dataclass
class Result:
    amplitude_v: List[float]
    mechanical_work_j: float
    valve_loss_j: float
    initial_energy_j: float
    final_energy_j: float
    residual_j: float

    @property
    def late_gain(self) -> float:
        if len(self.amplitude_v) < 2 or self.amplitude_v[-2] <= 1e-30:
            return float("nan")
        return self.amplitude_v[-1] / self.amplitude_v[-2]


def simulate(cfg: Config, topology: Sequence[Tuple[int, int]] = CROSS_TOPOLOGY) -> Result:
    net = FloatingNetwork(cfg)
    q = [cfg.seed_charge_c, -cfg.seed_charge_c, 0.0, 0.0]
    phase = 0
    v = net.voltages(phase, q)
    u = net.energy(phase, q, v)
    initial = u
    mech = 0.0
    loss = 0.0
    amps: List[float] = []
    for step in range(1, cfg.revolutions * cfg.steps_per_rev + 1):
        new_phase = step % cfg.steps_per_rev
        u_rot = net.energy(new_phase, q)
        mech += u_rot - u
        q, dl = net.valve_step(new_phase, q, topology)
        loss += dl
        u = net.energy(new_phase, q)
        phase = new_phase
        if step % cfg.steps_per_rev == 0:
            v = net.voltages(phase, q)
            amps.append(max(v) - min(v))
    residual = initial + mech - loss - u
    return Result(amps, mech, loss, initial, u, residual)


def capacitance_modulation(cfg: Config, a: int = 0, b: int = 2) -> Tuple[float, float, float]:
    net = FloatingNetwork(cfg)
    vals = [net.transfer_ceff(i, a, b) for i in range(cfg.steps_per_rev)]
    cmin, cmax = min(vals), max(vals)
    return cmin, cmax, cmax / cmin


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--revolutions", type=int, default=20)
    p.add_argument("--plate", type=float, default=0.0, help="neutral rear-plate coupling scale")
    p.add_argument("--aperture", type=float, default=10.0)
    args = p.parse_args(argv)
    base = Config(revolutions=args.revolutions, aperture_half_width_deg=args.aperture, plate_scale=args.plate)
    r = simulate(base)
    cmin, cmax, ratio = capacitance_modulation(base)
    print("M2-V4 fully floating electrostatic diagnostic")
    print("No ground node; sum(V)=0 is gauge fixing only.")
    print(f"plate scale              = {base.plate_scale:.6g}")
    print(f"Ceff min/max [pF]        = {cmin*1e12:.6g} / {cmax*1e12:.6g}")
    print(f"Cmax/Cmin                = {ratio:.9g}")
    print(f"initial amplitude [V]    = {r.amplitude_v[0] if r.amplitude_v else float('nan'):.9g}")
    print(f"final amplitude [V]      = {r.amplitude_v[-1] if r.amplitude_v else float('nan'):.9g}")
    print(f"late per-rev gain        = {r.late_gain:.9g}")
    print(f"mechanical work [J]      = {r.mechanical_work_j:.9g}")
    print(f"valve loss [J]           = {r.valve_loss_j:.9g}")
    print(f"final field energy [J]   = {r.final_energy_j:.9g}")
    print(f"energy residual [J]      = {r.residual_j:.3g}")
    print("\nPlate sweep")
    print(f"{'scale':>8s} {'Cratio':>12s} {'Afinal[V]':>12s} {'gain':>12s}")
    for scale in (0.0, 0.25, 0.5, 1.0, 2.0, 5.0, 10.0):
        cfg = replace(base, plate_scale=scale)
        rr = simulate(cfg)
        _, _, cr = capacitance_modulation(cfg)
        print(f"{scale:8.3g} {cr:12.6g} {rr.amplitude_v[-1]:12.6g} {rr.late_gain:12.6g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
