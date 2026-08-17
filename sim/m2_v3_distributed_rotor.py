#!/usr/bin/env python3
"""M2-V3 distributed floating-rotor capacitance diagnostic.

This model tests one narrow question suggested by Goldie's self-excited
variable-capacitance generator and the M2 evidence:

Can one electrically isolated Testatika rotor wire act as a spatially extended
neutral capacitive bridge between an inner field/arc region and an outer
contactless pickup region, and can electrode aperture/route geometry produce a
large enough Cmax/Cmin to make regenerative cross-feedback plausible?

The model is deliberately reduced. It is NOT a historical wiring claim and it
contains no energy source. For each rotor wire:

    Q_wire = 0

and the wire is eliminated exactly as a neutral floating conductor. If its
capacitances to ARC and PICKUP are Ca, Cp and stray-to-environment is Cg, the
wire contributes the mediated mutual capacitance

    Cmed = Ca * Cp / (Ca + Cp + Cg).

Twenty-four such wires are placed at the M2 nominal sector pitch. R0/R1/R3/R4
are geometric research routes from docs/research/rotor-wire-routing.md.

The script scans angular pickup aperture. A reduced Goldie bridge diagnostic is

    rho_bridge = beta * (Cmax/Cmin - 1)

where beta is a passive returned-output fraction. rho_bridge > 1 only says the
measured/geometric capacitance ratio would be large enough for a two-section
Goldie-like regenerative control topology. It is NOT the full M2 monodromy
matrix and does not establish self-running or over-unity behavior.
"""
from __future__ import annotations

from dataclasses import dataclass
import argparse
import csv
import math
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

TAU = 2.0 * math.pi


@dataclass(frozen=True)
class RouteLobe:
    angle_offset_deg: float
    radial_zone: str
    face: str
    weight: float


ROUTES: Dict[str, Tuple[RouteLobe, ...]] = {
    "R0": (
        RouteLobe(0.0, "inner", "F", 0.50),
        RouteLobe(0.0, "outer", "F", 0.50),
    ),
    "R1": (
        RouteLobe(0.0, "inner", "F", 0.50),
        RouteLobe(0.0, "outer", "B", 0.50),
    ),
    "R3": (
        RouteLobe(0.0, "inner", "F", 0.50),
        RouteLobe(15.0, "outer", "B", 0.50),
    ),
    "R4": (
        RouteLobe(0.0, "inner", "F", 0.20),
        RouteLobe(0.0, "mid1", "B", 0.20),
        RouteLobe(0.0, "mid2", "F", 0.20),
        RouteLobe(0.0, "mid3", "B", 0.20),
        RouteLobe(0.0, "outer", "B", 0.20),
    ),
}

ARC_ZONES = frozenset({"inner", "mid1"})
PICKUP_ZONES = frozenset({"mid2", "mid3", "outer"})


@dataclass(frozen=True)
class DistributedConfig:
    sectors: int = 24
    route: str = "R0"
    aperture_half_width_deg: float = 10.0
    samples_per_sector: int = 120
    feedback_beta: float = 0.40

    # Per-wire placeholder capacitances. Replace by FEM/bench data.
    direct_floor_f: float = 0.010e-12
    wire_stray_f: float = 0.100e-12
    arc_lobe_peak_f: float = 1.000e-12
    pickup_lobe_peak_f: float = 1.000e-12
    back_face_factor: float = 0.90

    @property
    def sector_pitch_deg(self) -> float:
        return 360.0 / self.sectors


@dataclass(frozen=True)
class ModulationResult:
    route: str
    aperture_half_width_deg: float
    c_min_f: float
    c_max_f: float
    ratio: float
    beta_critical: float
    rho_bridge: float
    theta_at_min_deg: float
    theta_at_max_deg: float

    @property
    def bridge_regenerative(self) -> bool:
        return self.rho_bridge > 1.0


def wrap_angle(x: float) -> float:
    return (x + math.pi) % TAU - math.pi


def raised_cosine(angle: float, center: float, half_width: float) -> float:
    d = abs(wrap_angle(angle - center))
    if d >= half_width:
        return 0.0
    return 0.5 * (1.0 + math.cos(math.pi * d / half_width))


def _face_factor(face: str, cfg: DistributedConfig) -> float:
    if face == "F":
        return 1.0
    if face == "B":
        return cfg.back_face_factor
    raise ValueError(f"unknown face: {face}")


def wire_pair_capacitances(theta: float, wire_index: int, cfg: DistributedConfig) -> Tuple[float, float]:
    """Return this neutral wire's Ca(theta), Cp(theta).

    ARC and PICKUP are represented by co-azimuthal narrow windows in this first
    diagnostic. Route lobes decide which radial/face portions of one equipotential
    wire couple into each region.
    """
    if cfg.route not in ROUTES:
        raise ValueError(f"unknown route: {cfg.route}")
    if cfg.sectors <= 0:
        raise ValueError("sectors must be positive")
    half = math.radians(cfg.aperture_half_width_deg)
    if half <= 0:
        raise ValueError("aperture_half_width_deg must be positive")

    phi0 = theta + TAU * wire_index / cfg.sectors
    ca = cfg.direct_floor_f
    cp = cfg.direct_floor_f
    for lobe in ROUTES[cfg.route]:
        phi = phi0 + math.radians(lobe.angle_offset_deg)
        window = raised_cosine(phi, 0.0, half)
        face = _face_factor(lobe.face, cfg)
        if lobe.radial_zone in ARC_ZONES:
            ca += lobe.weight * cfg.arc_lobe_peak_f * face * window
        if lobe.radial_zone in PICKUP_ZONES:
            cp += lobe.weight * cfg.pickup_lobe_peak_f * face * window
    return ca, cp


def neutral_wire_mediated_capacitance(ca: float, cp: float, cg: float) -> float:
    """Exact Schur-complement contribution for one q_wire=0 conductor."""
    if ca < 0 or cp < 0 or cg <= 0:
        raise ValueError("capacitances must be non-negative and cg positive")
    return ca * cp / (ca + cp + cg)


def effective_arc_pickup_capacitance(theta: float, cfg: DistributedConfig) -> float:
    total = 0.0
    for k in range(cfg.sectors):
        ca, cp = wire_pair_capacitances(theta, k, cfg)
        total += neutral_wire_mediated_capacitance(ca, cp, cfg.wire_stray_f)
    return total


def scan_modulation(cfg: DistributedConfig) -> ModulationResult:
    n = cfg.sectors * cfg.samples_per_sector
    if n <= 0:
        raise ValueError("samples_per_sector must be positive")
    best_min = (math.inf, 0.0)
    best_max = (-math.inf, 0.0)
    span = TAU / cfg.sectors
    for i in range(cfg.samples_per_sector):
        theta = span * i / cfg.samples_per_sector
        c = effective_arc_pickup_capacitance(theta, cfg)
        if c < best_min[0]:
            best_min = (c, theta)
        if c > best_max[0]:
            best_max = (c, theta)
    cmin, thmin = best_min
    cmax, thmax = best_max
    ratio = cmax / cmin
    delta = ratio - 1.0
    beta_critical = math.inf if delta <= 0.0 else 1.0 / delta
    rho = cfg.feedback_beta * delta
    return ModulationResult(
        route=cfg.route,
        aperture_half_width_deg=cfg.aperture_half_width_deg,
        c_min_f=cmin,
        c_max_f=cmax,
        ratio=ratio,
        beta_critical=beta_critical,
        rho_bridge=rho,
        theta_at_min_deg=math.degrees(thmin),
        theta_at_max_deg=math.degrees(thmax),
    )


def sweep(
    base: DistributedConfig,
    routes: Iterable[str] = ("R0", "R1", "R3", "R4"),
    half_widths_deg: Iterable[float] = (3, 5, 7, 10, 15, 20, 38),
) -> List[ModulationResult]:
    out: List[ModulationResult] = []
    for route in routes:
        for width in half_widths_deg:
            out.append(scan_modulation(DistributedConfig(
                sectors=base.sectors,
                route=route,
                aperture_half_width_deg=float(width),
                samples_per_sector=base.samples_per_sector,
                feedback_beta=base.feedback_beta,
                direct_floor_f=base.direct_floor_f,
                wire_stray_f=base.wire_stray_f,
                arc_lobe_peak_f=base.arc_lobe_peak_f,
                pickup_lobe_peak_f=base.pickup_lobe_peak_f,
                back_face_factor=base.back_face_factor,
            )))
    return out


def write_csv(path: Path, rows: Sequence[ModulationResult]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([
            "route", "aperture_half_width_deg", "c_min_f", "c_max_f",
            "cmax_cmin_ratio", "beta_critical", "rho_bridge",
            "bridge_regenerative", "theta_at_min_deg", "theta_at_max_deg",
        ])
        for r in rows:
            w.writerow([
                r.route, r.aperture_half_width_deg, r.c_min_f, r.c_max_f,
                r.ratio, r.beta_critical, r.rho_bridge,
                int(r.bridge_regenerative), r.theta_at_min_deg, r.theta_at_max_deg,
            ])


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--feedback", type=float, default=0.40)
    p.add_argument("--samples-per-sector", type=int, default=120)
    p.add_argument("--csv", type=Path)
    args = p.parse_args(argv)

    base = DistributedConfig(
        feedback_beta=args.feedback,
        samples_per_sector=args.samples_per_sector,
    )
    rows = sweep(base)

    print("M2-V3 distributed floating-wire / narrow-pickup diagnostic")
    print("NOTE: geometric bridge test only; not a historical circuit or energy-source claim.")
    print(f"sector pitch = {base.sector_pitch_deg:.6g} deg; beta = {base.feedback_beta:.6g}")
    print(
        f"{'route':5s} {'half[deg]':>9s} {'Cmax/Cmin':>11s} "
        f"{'beta_crit':>11s} {'rho_bridge':>11s} {'rho>1':>7s}"
    )
    for r in rows:
        bc = "inf" if not math.isfinite(r.beta_critical) else f"{r.beta_critical:.6g}"
        print(
            f"{r.route:5s} {r.aperture_half_width_deg:9.3g} "
            f"{r.ratio:11.6g} {bc:>11s} {r.rho_bridge:11.6g} "
            f"{str(r.bridge_regenerative):>7s}"
        )
    if args.csv:
        write_csv(args.csv, rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
