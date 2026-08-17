#!/usr/bin/env python3
"""Falsifiable numerical working model for a regenerative Testatika M2 hypothesis.

The model contains 24 electrically floating, neutral rotor conductors and four
stationary electrical nodes (left/right grid and left/right spiral).  The rotor
is eliminated analytically with a Schur complement after constructing the full
angle-dependent capacitance matrix.  Thus the simulated stationary network still
contains the electrostatic influence of all 24 floating rotor sectors.

Only conventional bookkeeping is used:
  q = C(theta) v
  U = 1/2 q^T v
  passive one-way charge valves conserve charge and dissipate field energy
  field-energy changes caused by prescribed rotation are counted as mechanical work

This is a research hypothesis, not a reconstruction of a known historical wiring
and not an over-unity model.  Default capacitances are placeholders to be replaced
by measured or FEM-derived C_ij(theta) data.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
import argparse
import csv
import itertools
import math
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

TAU = 2.0 * math.pi
STATIONARY_NAMES = ("GRID_L", "GRID_R", "SPIRAL_L", "SPIRAL_R")


def _zeros(n: int) -> List[List[float]]:
    return [[0.0 for _ in range(n)] for _ in range(n)]


def dot(a: Sequence[float], b: Sequence[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def lu_factor(a: Sequence[Sequence[float]]) -> Tuple[List[List[float]], List[int]]:
    """Small dense LU factorization with partial pivoting."""
    n = len(a)
    lu = [list(row) for row in a]
    piv = list(range(n))
    for k in range(n):
        p = max(range(k, n), key=lambda i: abs(lu[i][k]))
        if abs(lu[p][k]) < 1e-30:
            raise ValueError("singular capacitance matrix")
        if p != k:
            lu[k], lu[p] = lu[p], lu[k]
            piv[k], piv[p] = piv[p], piv[k]
        pivot = lu[k][k]
        for i in range(k + 1, n):
            lu[i][k] /= pivot
            m = lu[i][k]
            for j in range(k + 1, n):
                lu[i][j] -= m * lu[k][j]
    return lu, piv


def lu_solve(factor: Tuple[Sequence[Sequence[float]], Sequence[int]], b: Sequence[float]) -> List[float]:
    lu, piv = factor
    n = len(lu)
    x = [b[piv[i]] for i in range(n)]
    for i in range(n):
        for j in range(i):
            x[i] -= lu[i][j] * x[j]
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            x[i] -= lu[i][j] * x[j]
        x[i] /= lu[i][i]
    return x


def wrap_angle(x: float) -> float:
    return (x + math.pi) % TAU - math.pi


def raised_cosine(angle: float, center: float, half_width: float) -> float:
    d = abs(wrap_angle(angle - center))
    if d >= half_width:
        return 0.0
    return 0.5 * (1.0 + math.cos(math.pi * d / half_width))


@dataclass(frozen=True)
class ModelConfig:
    sectors: int = 24
    steps_per_rev: int = 96
    revolutions: int = 40
    rpm: float = 30.0
    grid_mode: str = "mesh"  # mesh | foil
    feedback: bool = True

    # Placeholder pair capacitances.  Replace with bench/FEM C_ij(theta).
    rotor_ground_f: float = 0.35e-12
    stationary_ground_f: float = 4.0e-12
    rotor_grid_floor_f: float = 0.03e-12
    rotor_grid_peak_f: float = 0.75e-12
    rotor_spiral_peak_f: float = 0.45e-12
    grid_spiral_f: float = 8.0e-12
    side_cross_f: float = 0.12e-12

    # Hypothesis parameter: a mesh permits more rotor-to-inner-spiral field
    # penetration than a continuous foil shield.
    mesh_penetration: float = 0.35
    foil_penetration: float = 0.025
    electrode_half_width_deg: float = 38.0
    pickup_phase_offset_deg: float = 52.0

    # Idealized crystal/diode valve.  No active source is hidden here.
    diode_drop_v: float = 0.15
    diode_relaxation: float = 0.55
    diode_passes: int = 2

    # Tiny anti-symmetric seed.  Its stored energy is explicitly included.
    seed_charge_c: float = 2.0e-12

    @property
    def sector_event_hz(self) -> float:
        return self.sectors * self.rpm / 60.0


@dataclass
class Sample:
    step: int
    revolution: float
    angle_deg: float
    v_grid_l: float
    v_grid_r: float
    v_spiral_l: float
    v_spiral_r: float
    field_energy_j: float
    mechanical_work_j: float
    valve_loss_j: float


@dataclass
class SimulationResult:
    config: ModelConfig
    topology: Tuple[Tuple[str, str], ...]
    samples: List[Sample]
    amplitudes_v: List[float]
    gains: List[float]
    qv_work_spiral_l_j: float
    mechanical_work_j: float
    valve_loss_j: float
    initial_energy_j: float
    final_energy_j: float
    energy_residual_j: float

    @property
    def final_gain(self) -> float:
        return self.gains[-1] if self.gains else float("nan")

    @property
    def final_amplitude_v(self) -> float:
        return self.amplitudes_v[-1] if self.amplitudes_v else 0.0

    @property
    def late_gain(self) -> float:
        """Geometric per-revolution gain over up to the last five revolutions."""
        n = min(5, len(self.amplitudes_v) - 1)
        if n <= 0:
            return float("nan")
        a0 = self.amplitudes_v[-1 - n]
        a1 = self.amplitudes_v[-1]
        floor = max(1e-12, self.amplitudes_v[0] * 1e-6)
        if a0 <= floor or a1 <= floor:
            return float("nan")
        return (a1 / a0) ** (1.0 / n)


class M2Network:
    """Angle-dependent capacitance network with neutral floating rotor sectors."""

    def __init__(self, config: ModelConfig):
        if config.grid_mode not in {"mesh", "foil"}:
            raise ValueError("grid_mode must be 'mesh' or 'foil'")
        if config.sectors <= 0 or config.steps_per_rev <= 0:
            raise ValueError("sectors and steps_per_rev must be positive")
        self.cfg = config
        self.rotor = list(range(config.sectors))
        self.GL = config.sectors
        self.GR = config.sectors + 1
        self.SL = config.sectors + 2
        self.SR = config.sectors + 3
        self.stationary_full = (self.GL, self.GR, self.SL, self.SR)
        self.n_full = config.sectors + 4
        self.name_to_reduced = {name: i for i, name in enumerate(STATIONARY_NAMES)}

        self._full_matrices: List[List[List[float]]] = []
        self._reduced_matrices: List[List[List[float]]] = []
        self._factors: List[Tuple[List[List[float]], List[int]]] = []
        self._ceff: List[Dict[Tuple[int, int], float]] = []
        self._precompute()

    @staticmethod
    def _add_pair(c: List[List[float]], i: int, j: int, value: float) -> None:
        if value < 0.0:
            raise ValueError("capacitance cannot be negative")
        c[i][i] += value
        c[j][j] += value
        c[i][j] -= value
        c[j][i] -= value

    def full_capacitance_matrix(self, theta: float) -> List[List[float]]:
        """Return the full (24 rotor + 4 stationary) nodal capacitance matrix."""
        cfg = self.cfg
        c = _zeros(self.n_full)
        for i in self.rotor:
            c[i][i] += cfg.rotor_ground_f
        for i in self.stationary_full:
            c[i][i] += cfg.stationary_ground_f

        self._add_pair(c, self.GL, self.SL, cfg.grid_spiral_f)
        self._add_pair(c, self.GR, self.SR, cfg.grid_spiral_f)
        self._add_pair(c, self.GL, self.GR, cfg.side_cross_f)
        self._add_pair(c, self.SL, self.SR, cfg.side_cross_f)

        half_width = math.radians(cfg.electrode_half_width_deg)
        pickup_shift = math.radians(cfg.pickup_phase_offset_deg)
        grid_centers = (0.0, math.pi)
        spiral_centers = (pickup_shift, math.pi + pickup_shift)
        penetration = cfg.mesh_penetration if cfg.grid_mode == "mesh" else cfg.foil_penetration

        for k in self.rotor:
            phi = theta + TAU * k / cfg.sectors
            pgl = raised_cosine(phi, grid_centers[0], half_width)
            pgr = raised_cosine(phi, grid_centers[1], half_width)
            psl = raised_cosine(phi, spiral_centers[0], half_width)
            psr = raised_cosine(phi, spiral_centers[1], half_width)
            self._add_pair(c, k, self.GL, cfg.rotor_grid_floor_f + cfg.rotor_grid_peak_f * pgl)
            self._add_pair(c, k, self.GR, cfg.rotor_grid_floor_f + cfg.rotor_grid_peak_f * pgr)
            self._add_pair(c, k, self.SL, penetration * cfg.rotor_spiral_peak_f * psl)
            self._add_pair(c, k, self.SR, penetration * cfg.rotor_spiral_peak_f * psr)
        return c

    def _reduce_neutral_floating_rotor(self, c: Sequence[Sequence[float]]) -> List[List[float]]:
        """Schur complement C_ss - C_sr C_rr^-1 C_rs for q_rotor = 0.

        Rotor sectors have no galvanic connection and no net free charge in this
        baseline.  They remain present electrostatically as induced-polarization
        mediators in the reduced 4x4 stationary capacitance matrix.
        """
        m = 4
        e = [[c[self.stationary_full[i]][self.stationary_full[j]] for j in range(m)] for i in range(m)]
        for r in self.rotor:
            d = c[r][r]
            for i in range(m):
                cri = c[self.stationary_full[i]][r]
                for j in range(m):
                    e[i][j] -= cri * c[r][self.stationary_full[j]] / d
        return e

    def reduced_capacitance_matrix(self, theta: float) -> List[List[float]]:
        return self._reduce_neutral_floating_rotor(self.full_capacitance_matrix(theta))

    def _precompute(self) -> None:
        all_edges = [(a, b) for a in range(4) for b in range(4) if a != b]
        for phase in range(self.cfg.steps_per_rev):
            theta = TAU * phase / self.cfg.steps_per_rev
            full = self.full_capacitance_matrix(theta)
            reduced = self._reduce_neutral_floating_rotor(full)
            factor = lu_factor(reduced)
            ceff: Dict[Tuple[int, int], float] = {}
            for a, b in all_edges:
                transfer = [0.0] * 4
                transfer[a] = -1.0
                transfer[b] = +1.0
                dv = lu_solve(factor, transfer)
                slope = dv[a] - dv[b]
                if slope >= 0.0:
                    raise ValueError("unexpected passive transfer sensitivity")
                ceff[(a, b)] = -1.0 / slope
            self._full_matrices.append(full)
            self._reduced_matrices.append(reduced)
            self._factors.append(factor)
            self._ceff.append(ceff)

    def voltages(self, phase: int, q_stationary: Sequence[float]) -> List[float]:
        return lu_solve(self._factors[phase], q_stationary)

    def energy(self, phase: int, q_stationary: Sequence[float], v: Sequence[float] | None = None) -> float:
        if v is None:
            v = self.voltages(phase, q_stationary)
        return 0.5 * dot(q_stationary, v)

    def resolve_topology(self, topology: Sequence[Tuple[str, str]]) -> Tuple[Tuple[int, int], ...]:
        return tuple((self.name_to_reduced[a], self.name_to_reduced[b]) for a, b in topology)

    def valve_step(self, phase: int, q: Sequence[float], topology: Sequence[Tuple[str, str]]) -> Tuple[List[float], float, Dict[int, float]]:
        """Apply passive one-way charge valves; total free charge is conserved."""
        if not topology:
            return list(q), 0.0, {}
        cfg = self.cfg
        edges = self.resolve_topology(topology)
        out = list(q)
        total_loss = 0.0
        delta_by_node: Dict[int, float] = {}
        for _ in range(cfg.diode_passes):
            for a, b in edges:
                v0 = self.voltages(phase, out)
                excess = v0[a] - v0[b] - cfg.diode_drop_v
                if excess <= 0.0:
                    continue
                dq = cfg.diode_relaxation * self._ceff[phase][(a, b)] * excess
                u0 = self.energy(phase, out, v0)
                out[a] -= dq
                out[b] += dq
                v1 = self.voltages(phase, out)
                u1 = self.energy(phase, out, v1)
                tol = max(1e-24, abs(u0) * 1e-10)
                if u1 > u0 + tol:
                    raise RuntimeError("passive valve step increased field energy")
                total_loss += max(0.0, u0 - u1)
                delta_by_node[a] = delta_by_node.get(a, 0.0) - dq
                delta_by_node[b] = delta_by_node.get(b, 0.0) + dq
        return out, total_loss, delta_by_node


SIMPLE_CROSS_TOPOLOGY: Tuple[Tuple[str, str], ...] = (
    ("SPIRAL_L", "GRID_R"),
    ("SPIRAL_R", "GRID_L"),
)


def simulate(config: ModelConfig, topology: Sequence[Tuple[str, str]] | None = None) -> SimulationResult:
    net = M2Network(config)
    if topology is None:
        topology = SIMPLE_CROSS_TOPOLOGY if config.feedback else ()
    topology = tuple(topology)

    q = [config.seed_charge_c, -config.seed_charge_c, 0.0, 0.0]
    phase = 0
    v = net.voltages(phase, q)
    u = net.energy(phase, q, v)
    initial_u = u
    mech = 0.0
    valve_loss = 0.0
    qv_work = 0.0
    samples: List[Sample] = []
    amplitudes = [abs(v[2] - v[3])]

    total_steps = config.revolutions * config.steps_per_rev
    for step in range(1, total_steps + 1):
        new_phase = step % config.steps_per_rev
        v_rot = net.voltages(new_phase, q)
        u_rot = net.energy(new_phase, q, v_rot)
        mech += u_rot - u

        q_before = list(q)
        v_before = v_rot
        q, loss, _ = net.valve_step(new_phase, q, topology)
        valve_loss += loss
        v = net.voltages(new_phase, q)
        u = net.energy(new_phase, q, v)

        dq_sl = q[2] - q_before[2]
        qv_work += 0.5 * (v_before[2] + v[2]) * dq_sl
        phase = new_phase

        if step % config.steps_per_rev == 0:
            amplitudes.append(abs(v[2] - v[3]))
        if step % max(1, config.steps_per_rev // 24) == 0:
            samples.append(Sample(
                step=step,
                revolution=step / config.steps_per_rev,
                angle_deg=360.0 * new_phase / config.steps_per_rev,
                v_grid_l=v[0], v_grid_r=v[1],
                v_spiral_l=v[2], v_spiral_r=v[3],
                field_energy_j=u,
                mechanical_work_j=mech,
                valve_loss_j=valve_loss,
            ))

    gains = [a1 / a0 if abs(a0) > 1e-30 else float("nan") for a0, a1 in zip(amplitudes, amplitudes[1:])]
    residual = initial_u + mech - valve_loss - u
    return SimulationResult(
        config=config,
        topology=topology,
        samples=samples,
        amplitudes_v=amplitudes,
        gains=gains,
        qv_work_spiral_l_j=qv_work,
        mechanical_work_j=mech,
        valve_loss_j=valve_loss,
        initial_energy_j=initial_u,
        final_energy_j=u,
        energy_residual_j=residual,
    )


def scenario_matrix(base: ModelConfig) -> List[Tuple[str, SimulationResult]]:
    cases = [
        ("A foil / feedback OFF", "foil", False),
        ("B mesh / feedback OFF", "mesh", False),
        ("C foil / feedback ON", "foil", True),
        ("D mesh / feedback ON", "mesh", True),
    ]
    return [(name, simulate(replace(base, grid_mode=mode, feedback=fb))) for name, mode, fb in cases]


def penetration_sweep(base: ModelConfig, values: Iterable[float]) -> List[Tuple[float, SimulationResult]]:
    return [(p, simulate(replace(base, grid_mode="mesh", feedback=True, mesh_penetration=p))) for p in values]


def search_passive_topologies(base: ModelConfig, max_edges: int = 3) -> List[Tuple[float, Tuple[Tuple[str, str], ...], SimulationResult]]:
    """Rank passive directed-valve networks by late per-revolution gain."""
    edges = [(a, b) for a in STATIONARY_NAMES for b in STATIONARY_NAMES if a != b]
    ranked = []
    for n_edges in range(1, max_edges + 1):
        for topology in itertools.combinations(edges, n_edges):
            r = simulate(base, topology)
            g = r.late_gain
            if math.isfinite(g):
                ranked.append((g, tuple(topology), r))
    ranked.sort(key=lambda x: x[0], reverse=True)
    return ranked


def write_csv(path: Path, result: SimulationResult) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["step", "revolution", "angle_deg", "v_grid_l", "v_grid_r", "v_spiral_l", "v_spiral_r", "field_energy_j", "mechanical_work_j", "valve_loss_j"])
        for s in result.samples:
            w.writerow([s.step, s.revolution, s.angle_deg, s.v_grid_l, s.v_grid_r, s.v_spiral_l, s.v_spiral_r, s.field_energy_j, s.mechanical_work_j, s.valve_loss_j])


def _fmt(x: float) -> str:
    return f"{x:.6g}"


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--rpm", type=float, default=30.0)
    p.add_argument("--revolutions", type=int, default=40)
    p.add_argument("--steps-per-rev", type=int, default=96)
    p.add_argument("--csv-dir", type=Path)
    p.add_argument("--sweep", action="store_true", help="sweep mesh field-penetration factor")
    p.add_argument("--search-topologies", action="store_true", help="search 1..3 passive valve-edge combinations")
    args = p.parse_args(argv)

    base = ModelConfig(rpm=args.rpm, revolutions=args.revolutions, steps_per_rev=args.steps_per_rev)
    print("Testatika M2 regenerative-grid working model")
    print("NOTE: falsifiable model hypothesis; no historical wiring or over-unity claim.")
    print(f"Rotor: {base.sectors} floating sectors; {base.rpm:g} rpm -> {base.sector_event_hz:g} sector events/s\n")
    print(f"{'scenario':28s} {'A_final[V]':>12s} {'g_late':>12s} {'W_mech[J]':>13s} {'U_final[J]':>13s} {'loss[J]':>12s} {'residual[J]':>13s}")
    results = scenario_matrix(base)
    for name, r in results:
        print(f"{name:28s} {_fmt(r.final_amplitude_v):>12s} {_fmt(r.late_gain):>12s} {_fmt(r.mechanical_work_j):>13s} {_fmt(r.final_energy_j):>13s} {_fmt(r.valve_loss_j):>12s} {_fmt(r.energy_residual_j):>13s}")
        if args.csv_dir:
            write_csv(args.csv_dir / f"scenario_{name[0].lower()}.csv", r)

    if args.sweep:
        print("\nmesh field-penetration sweep, simple cross-valves ON")
        print(f"{'penetration':>12s} {'A_final[V]':>12s} {'g_late':>12s} {'W_mech[J]':>13s}")
        for pval, r in penetration_sweep(base, [0.01, 0.025, 0.05, 0.1, 0.2, 0.35, 0.5, 0.7, 0.9]):
            print(f"{pval:12.3f} {_fmt(r.final_amplitude_v):>12s} {_fmt(r.late_gain):>12s} {_fmt(r.mechanical_work_j):>13s}")

    if args.search_topologies:
        search_cfg = replace(base, revolutions=min(base.revolutions, 8), steps_per_rev=min(base.steps_per_rev, 48), diode_drop_v=0.0)
        ranked = search_passive_topologies(search_cfg, max_edges=3)
        print("\nTop passive valve topologies (restricted four-node search)")
        for g, topology, r in ranked[:10]:
            print(f"g_late={_fmt(g):>10s} A_final={_fmt(r.final_amplitude_v):>10s} V  {topology}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
