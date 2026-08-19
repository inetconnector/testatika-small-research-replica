#!/usr/bin/env python3
"""M2 V4.23 non-electrical ambient/conventional source bounds.

This calculator closes several remaining conventional boundary terms using
optimistic upper bounds. It does not infer that any of these sources powered a
historical Testatika.
"""
from __future__ import annotations

import argparse
import math


def _positive(name: str, value: float) -> float:
    if value <= 0.0:
        raise ValueError(f"{name} must be > 0")
    return value


def wind_speed_for_power_m_s(power_w: float, area_m2: float, air_density_kg_m3: float = 1.2, efficiency: float = 1.0) -> float:
    """Wind speed from P = eta * 0.5*rho*A*v^3."""
    p = _positive("power_w", power_w)
    a = _positive("area_m2", area_m2)
    rho = _positive("air_density_kg_m3", air_density_kg_m3)
    if not 0.0 < efficiency <= 1.0:
        raise ValueError("efficiency must be in (0, 1]")
    return (2.0 * p / (rho * a * efficiency)) ** (1.0 / 3.0)


def acoustic_spl_db_for_power(power_w: float, area_m2: float, efficiency: float = 1.0, air_density_kg_m3: float = 1.2, sound_speed_m_s: float = 343.0, reference_pressure_pa: float = 20e-6) -> float:
    """Plane-wave SPL needed to deliver power through area, optimistic normal incidence."""
    p = _positive("power_w", power_w)
    a = _positive("area_m2", area_m2)
    rho = _positive("air_density_kg_m3", air_density_kg_m3)
    c = _positive("sound_speed_m_s", sound_speed_m_s)
    pref = _positive("reference_pressure_pa", reference_pressure_pa)
    if not 0.0 < efficiency <= 1.0:
        raise ValueError("efficiency must be in (0, 1]")
    intensity = p / (a * efficiency)
    p_rms = math.sqrt(intensity * rho * c)
    return 20.0 * math.log10(p_rms / pref)


def acoustic_pressure_rms_pa_for_power(power_w: float, area_m2: float, efficiency: float = 1.0, air_density_kg_m3: float = 1.2, sound_speed_m_s: float = 343.0) -> float:
    p = _positive("power_w", power_w)
    a = _positive("area_m2", area_m2)
    rho = _positive("air_density_kg_m3", air_density_kg_m3)
    c = _positive("sound_speed_m_s", sound_speed_m_s)
    if not 0.0 < efficiency <= 1.0:
        raise ValueError("efficiency must be in (0, 1]")
    intensity = p / (a * efficiency)
    return math.sqrt(intensity * rho * c)


def carnot_efficiency(hot_k: float, cold_k: float) -> float:
    th = _positive("hot_k", hot_k)
    tc = _positive("cold_k", cold_k)
    if th <= tc:
        raise ValueError("hot_k must exceed cold_k")
    return 1.0 - tc / th


def minimum_heat_flow_w_for_power(power_w: float, hot_k: float, cold_k: float) -> float:
    """Best-case heat flow from the Carnot efficiency ceiling."""
    p = _positive("power_w", power_w)
    return p / carnot_efficiency(hot_k, cold_k)


def intercepted_radiant_power_w(irradiance_w_m2: float, area_m2: float, conversion_efficiency: float = 1.0) -> float:
    s = _positive("irradiance_w_m2", irradiance_w_m2)
    a = _positive("area_m2", area_m2)
    if not 0.0 < conversion_efficiency <= 1.0:
        raise ValueError("conversion_efficiency must be in (0, 1]")
    return s * a * conversion_efficiency


def required_irradiance_w_m2(power_w: float, area_m2: float, conversion_efficiency: float = 1.0) -> float:
    p = _positive("power_w", power_w)
    a = _positive("area_m2", area_m2)
    if not 0.0 < conversion_efficiency <= 1.0:
        raise ValueError("conversion_efficiency must be in (0, 1]")
    return p / (a * conversion_efficiency)


def stored_energy_required_j(power_w: float, duration_s: float) -> float:
    return _positive("power_w", power_w) * _positive("duration_s", duration_s)


def solid_disk_rotational_energy_j(mass_kg: float, radius_m: float, rpm: float) -> float:
    """K = 1/2 I w^2 for a solid disk, I=1/2 m r^2."""
    m = _positive("mass_kg", mass_kg)
    r = _positive("radius_m", radius_m)
    n = _positive("rpm", rpm)
    inertia = 0.5 * m * r * r
    omega = n * 2.0 * math.pi / 60.0
    return 0.5 * inertia * omega * omega


def vibration_force_rms_n_for_power(power_w: float, frequency_hz: float, displacement_rms_m: float, efficiency: float = 1.0) -> float:
    """Optimistic in-phase F_rms*v_rms power transfer for sinusoidal base motion."""
    p = _positive("power_w", power_w)
    f = _positive("frequency_hz", frequency_hz)
    x = _positive("displacement_rms_m", displacement_rms_m)
    if not 0.0 < efficiency <= 1.0:
        raise ValueError("efficiency must be in (0, 1]")
    v_rms = 2.0 * math.pi * f * x
    return p / (efficiency * v_rms)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--power", type=float, default=100.0)
    args = parser.parse_args()
    p = args.power
    area = 0.1

    print("M2 V4.23 non-electrical source bounds")
    print(f"target real output = {p:.6g} W")

    print("\nAirflow, A=0.1 m^2, rho=1.2 kg/m^3")
    for eta in (1.0, 0.3):
        print(f"eta={eta:4.0%}: v >= {wind_speed_for_power_m_s(p, area, efficiency=eta):.6g} m/s")

    print("\nAcoustic plane-wave benchmark, A=0.1 m^2")
    for eta in (1.0, 0.1):
        prms = acoustic_pressure_rms_pa_for_power(p, area, efficiency=eta)
        spl = acoustic_spl_db_for_power(p, area, efficiency=eta)
        print(f"eta={eta:4.0%}: p_rms >= {prms:.6g} Pa, SPL >= {spl:.6g} dB")

    print("\nThermal-gradient Carnot lower bound, cold side 293 K")
    for dt in (10.0, 50.0, 100.0):
        hot = 293.0 + dt
        eta = carnot_efficiency(hot, 293.0)
        q = minimum_heat_flow_w_for_power(p, hot, 293.0)
        print(f"DeltaT={dt:5.1f} K: eta_C={eta:.4%}, Qdot >= {q:.6g} W")

    print("\nRadiant-input benchmark, A=0.1 m^2")
    for irr in (10.0, 100.0, 1000.0):
        print(f"irradiance={irr:7.1f} W/m^2 -> intercept={intercepted_radiant_power_w(irr, area):.6g} W")
    print(f"required at 20% conversion -> {required_irradiance_w_m2(p, area, 0.2):.6g} W/m^2")

    print("\nFinite stored-energy requirement")
    for duration in (1.0, 60.0, 600.0, 3600.0):
        e = stored_energy_required_j(p, duration)
        print(f"t={duration:7.1f} s -> E >= {e:.6g} J ({e/3600.0:.6g} Wh)")

    print("\nGenerous 1-kg, 20-cm-diameter solid rotor at 60 rpm")
    e_rot = solid_disk_rotational_energy_j(1.0, 0.1, 60.0)
    print(f"Krot = {e_rot:.6g} J -> {e_rot/p:.6g} s at target power")

    print("\nSinusoidal vibration benchmark at 50 Hz")
    for xrms in (1e-3, 1e-4):
        force = vibration_force_rms_n_for_power(p, 50.0, xrms)
        print(f"x_rms={xrms*1e3:.3g} mm -> F_rms >= {force:.6g} N at ideal phase")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
