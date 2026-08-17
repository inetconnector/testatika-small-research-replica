#!/usr/bin/env python3
"""Bridge the M2 capacitance model to a Goldie-style regeneration criterion.

This diagnostic asks a narrow question: if the existing M2 model is reduced to
its four stationary nodes with every rotor wire constrained to zero net free
charge, is the resulting angle-dependent two-terminal capacitance modulation
large enough to support a passive Goldie-like cross-feedback loop?

For a reduced ideal self-excited variable-capacitance stage, a necessary
small-signal condition is

    beta * (Cmax/Cmin - 1) > 1,

where beta is a passive returned-output fraction (0 <= beta <= 1). Therefore

    beta_critical = 1 / (Cmax/Cmin - 1).

If beta_critical >> 1 for every candidate node pair, the current aggregate M2
model cannot realize that mechanism. That result does not rule out the
historical device: it identifies missing state/geometry in the model, such as
spatial polarization along a through-disc rotor wire, persistent non-zero
sector charge, or additional stationary pickup nodes.
"""
from __future__ import annotations

from dataclasses import dataclass
import argparse
import math
from typing import Iterable, List, Sequence, Tuple

from m2_regenerative_grid_model import ModelConfig, M2Network, STATIONARY_NAMES


@dataclass(frozen=True)
class PairScan:
    node_a: str
    node_b: str
    c_min_f: float
    c_max_f: float
    ratio: float
    modulation_ppm: float
    beta_critical: float

    @property
    def passive_goldie_possible(self) -> bool:
        return self.beta_critical <= 1.0


def effective_pair_capacitance(
    net: M2Network,
    phase: int,
    node_a: str,
    node_b: str,
    test_charge_c: float = 1e-12,
) -> float:
    """Return differential C between two reduced nodes at one rotor phase."""
    if node_a == node_b:
        raise ValueError("node_a and node_b must differ")
    if test_charge_c <= 0.0:
        raise ValueError("test_charge_c must be positive")
    try:
        ia = STATIONARY_NAMES.index(node_a)
        ib = STATIONARY_NAMES.index(node_b)
    except ValueError as exc:
        raise ValueError("unknown stationary node") from exc

    q = [0.0] * len(STATIONARY_NAMES)
    q[ia] = test_charge_c
    q[ib] = -test_charge_c
    v = net.voltages(phase, q)
    dv = v[ia] - v[ib]
    if dv <= 0.0:
        raise RuntimeError("non-positive differential voltage in passive C network")
    return test_charge_c / dv


def scan_pair(net: M2Network, node_a: str, node_b: str) -> PairScan:
    values = [
        effective_pair_capacitance(net, phase, node_a, node_b)
        for phase in range(net.cfg.steps_per_rev)
    ]
    c_min = min(values)
    c_max = max(values)
    ratio = c_max / c_min
    rminus = ratio - 1.0
    beta_critical = math.inf if rminus <= 0.0 else 1.0 / rminus
    return PairScan(
        node_a=node_a,
        node_b=node_b,
        c_min_f=c_min,
        c_max_f=c_max,
        ratio=ratio,
        modulation_ppm=rminus * 1e6,
        beta_critical=beta_critical,
    )


def all_undirected_pairs(names: Sequence[str] = STATIONARY_NAMES) -> Iterable[Tuple[str, str]]:
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            yield a, b


def scan_config(cfg: ModelConfig) -> List[PairScan]:
    net = M2Network(cfg)
    return [scan_pair(net, a, b) for a, b in all_undirected_pairs()]


def strongest_modulation(rows: Sequence[PairScan]) -> PairScan:
    if not rows:
        raise ValueError("rows must not be empty")
    return max(rows, key=lambda r: r.ratio)


def passive_goldie_available(rows: Sequence[PairScan]) -> bool:
    return any(r.passive_goldie_possible for r in rows)


def _fmt_beta(x: float) -> str:
    return "inf" if math.isinf(x) else f"{x:.6g}"


def print_scan(mode: str, rows: Sequence[PairScan]) -> None:
    print(f"\n{mode.upper()} — aggregate four-node q_rotor=0 model")
    print(
        f"{'pair':29s} {'Cmin[pF]':>11s} {'Cmax[pF]':>11s} "
        f"{'ratio':>12s} {'mod[ppm]':>12s} {'beta_crit':>12s}"
    )
    for r in rows:
        pair = f"{r.node_a}--{r.node_b}"
        print(
            f"{pair:29s} {r.c_min_f*1e12:11.6f} {r.c_max_f*1e12:11.6f} "
            f"{r.ratio:12.9f} {r.modulation_ppm:12.3f} {_fmt_beta(r.beta_critical):>12s}"
        )
    best = strongest_modulation(rows)
    print(
        "best modulation          = "
        f"{best.node_a}--{best.node_b}, ratio={best.ratio:.9f}, "
        f"beta_crit={_fmt_beta(best.beta_critical)}"
    )
    if passive_goldie_available(rows):
        print("reduced Goldie criterion = at least one pair can reach threshold with beta <= 1")
    else:
        print("reduced Goldie criterion = NO pair reaches threshold with passive beta <= 1")


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--steps-per-rev", type=int, default=192)
    p.add_argument("--rpm", type=float, default=30.0)
    args = p.parse_args(argv)

    print("M2 -> Goldie regeneration bridge diagnostic")
    print("Necessary reduced-model criterion: beta*(Cmax/Cmin - 1) > 1")
    print("No over-unity assumption; beta is restricted to a passive returned fraction <= 1.")

    for mode in ("mesh", "foil"):
        cfg = ModelConfig(
            grid_mode=mode,
            feedback=False,
            steps_per_rev=args.steps_per_rev,
            revolutions=1,
            rpm=args.rpm,
        )
        rows = scan_config(cfg)
        print_scan(mode, rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
