#!/usr/bin/env python3
"""V4.11 environmental-port power bounds.

This module is a diagnostic extension of the fully floating M2 model. It does
not assert that any environmental source powered a historical Testatika and it
does not add RF/resonance hardware to the M2 historical baseline.

The calculations deliberately use optimistic upper bounds so that ordinary
candidate reservoirs can be rejected quantitatively before more speculative
mechanisms are considered.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

MU0 = 4.0 * math.pi * 1e-7


@dataclass(frozen=True)
class CandidateBound:
    name: str
    power_density_w_m2: float
    area_for_100w_m2: float
    note: str


def fair_weather_power_density(current_density_a_m2: float, potential_v: float) -> float:
    """Ideal DC power density J*V for an atmospheric current path."""
    return abs(current_density_a_m2 * potential_v)


def required_area(target_power_w: float, power_density_w_m2: float) -> float:
    """Ideal capture area for a spatially distributed power density."""
    if target_power_w < 0:
        raise ValueError("target_power_w must be non-negative")
    if power_density_w_m2 <= 0:
        return math.inf
    return target_power_w / power_density_w_m2


def capacitive_ac_bound(
    frequency_hz: float,
    equivalent_capacitance_f: float,
    field_v_m_rms: float,
    port_span_m: float,
) -> float:
    """Optimistic source-side apparent-power bound: 2*pi*f*C*(E*h)^2."""
    if min(frequency_hz, equivalent_capacitance_f, port_span_m) < 0:
        raise ValueError("frequency, capacitance and span must be non-negative")
    delta_v = abs(field_v_m_rms) * port_span_m
    return 2.0 * math.pi * frequency_hz * equivalent_capacitance_f * delta_v**2


def required_uniform_field(
    target_power_w: float,
    frequency_hz: float,
    equivalent_capacitance_f: float,
    port_span_m: float,
) -> float:
    """Uniform RMS field required to reach target power in the optimistic AC bound."""
    if target_power_w < 0:
        raise ValueError("target_power_w must be non-negative")
    if frequency_hz <= 0 or equivalent_capacitance_f <= 0 or port_span_m <= 0:
        return math.inf
    delta_v = math.sqrt(target_power_w / (2.0 * math.pi * frequency_hz * equivalent_capacitance_f))
    return delta_v / port_span_m


def plane_wave_flux_proxy(e_v_m_rms: float, b_t_rms: float) -> float:
    """E*H proxy using H=B/mu0.

    Natural ELF cavity fields are not generally free-space plane waves, so this
    is only an order-of-magnitude comparison, not a rigorous harvestable-power
    theorem.
    """
    return abs(e_v_m_rms * b_t_rms) / MU0


def rotating_loop_peak_emf(
    magnetic_flux_density_t: float,
    loop_area_m2: float,
    rpm: float,
    turns: int = 1,
) -> float:
    """Peak Faraday EMF N*B*A*omega for an optimally oriented rotating loop."""
    if loop_area_m2 < 0 or turns < 0:
        raise ValueError("area and turns must be non-negative")
    omega = 2.0 * math.pi * abs(rpm) / 60.0
    return turns * abs(magnetic_flux_density_t) * loop_area_m2 * omega


def canonical_bounds(target_power_w: float = 100.0) -> list[CandidateBound]:
    """Return source-order bounds used in the V4.11 research note."""
    candidates: list[CandidateBound] = []

    # Global electric circuit: deliberately grant access to the full ~250 kV
    # ionosphere-to-ground potential while retaining the measured pA/m^2 current.
    gec_density = fair_weather_power_density(2e-12, 250e3)
    candidates.append(
        CandidateBound(
            "fair-weather global electric circuit, full-column ideal",
            gec_density,
            required_area(target_power_w, gec_density),
            "optimistic: full 250 kV column potential at 2 pA/m^2",
        )
    )

    # Representative high ambient RF survey level: ~200 uW/m^2.
    rf_density = 200e-6
    candidates.append(
        CandidateBound(
            "ambient RF, high measured-average example",
            rf_density,
            required_area(target_power_w, rf_density),
            "before antenna/rectifier/mismatch losses",
        )
    )

    # Schumann/ELF order-of-magnitude proxy from ~0.2 mV/m and ~1 pT.
    sr_density = plane_wave_flux_proxy(0.2e-3, 1e-12)
    candidates.append(
        CandidateBound(
            "Schumann/ELF field proxy",
            sr_density,
            required_area(target_power_w, sr_density),
            "E*B/mu0 proxy only; Earth-ionosphere cavity is not a plane wave",
        )
    )

    return candidates


def main() -> None:
    target = 100.0
    print("V4.11 environmental-port optimistic bounds")
    print(f"target real power: {target:.3f} W")
    print()
    for row in canonical_bounds(target):
        print(row.name)
        print(f"  power density: {row.power_density_w_m2:.6g} W/m^2")
        print(f"  ideal area for 100 W: {row.area_for_100w_m2:.6g} m^2")
        print(f"  note: {row.note}")

    ceq = 50e-12
    span = 0.20
    for frequency, field in ((50.0, 100.0), (1e6, 100.0), (10e6, 100.0), (100e6, 100.0)):
        p = capacitive_ac_bound(frequency, ceq, field, span)
        print(f"capacitive bound f={frequency:g} Hz E={field:g} V/m: {p:.6g} W")

    e_req_50 = required_uniform_field(target, 50.0, ceq, span)
    print(f"50 Hz field required for 100 W with Ceq=50 pF, span=0.20 m: {e_req_50:.6g} V/m")

    disk_area = math.pi * 0.10**2
    emf = rotating_loop_peak_emf(50e-6, disk_area, 60.0)
    print(f"one-turn 200-mm loop in 50 uT at 60 rpm, optimistic peak EMF: {emf:.6g} V")


if __name__ == "__main__":
    main()
