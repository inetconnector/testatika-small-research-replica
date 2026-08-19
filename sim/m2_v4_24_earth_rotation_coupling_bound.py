#!/usr/bin/env python3
"""M2 V4.24 Earth-rotation / geomagnetic coupling bound.

This deliberately grants an unrealistically favorable interpretation in which a
laboratory conductor moves through a stationary geomagnetic field at the full
Earth-surface speed. A real Earth-fixed apparatus approximately co-rotates with
the geomagnetic field, so the v x B result below is an upper-bound comparison,
not a claim of an available local generator.
"""
from __future__ import annotations

import argparse
import math

EARTH_OMEGA_RAD_S = 7.2921159e-5
EARTH_RADIUS_M = 6.371e6


def _positive(name: str, value: float) -> float:
    if value <= 0.0:
        raise ValueError(f"{name} must be > 0")
    return value


def earth_surface_speed_m_s(latitude_deg: float, omega_rad_s: float = EARTH_OMEGA_RAD_S, radius_m: float = EARTH_RADIUS_M) -> float:
    if not -90.0 <= latitude_deg <= 90.0:
        raise ValueError("latitude_deg must be between -90 and 90")
    omega = _positive("omega_rad_s", omega_rad_s)
    radius = _positive("radius_m", radius_m)
    return omega * radius * math.cos(math.radians(latitude_deg))


def motional_emf_v(speed_m_s: float, magnetic_field_t: float, conductor_length_m: float, alignment: float = 1.0) -> float:
    """Upper-bound magnitude |v x B|*L with an explicit geometric alignment factor."""
    v = _positive("speed_m_s", speed_m_s)
    b = _positive("magnetic_field_t", magnetic_field_t)
    length = _positive("conductor_length_m", conductor_length_m)
    if not 0.0 <= alignment <= 1.0:
        raise ValueError("alignment must be in [0, 1]")
    return v * b * length * alignment


def current_for_real_power_a(power_w: float, voltage_v: float) -> float:
    return _positive("power_w", power_w) / _positive("voltage_v", voltage_v)


def equivalent_load_resistance_ohm(power_w: float, voltage_v: float) -> float:
    p = _positive("power_w", power_w)
    v = _positive("voltage_v", voltage_v)
    return v * v / p


def max_thevenin_source_resistance_ohm(power_w: float, open_circuit_voltage_v: float) -> float:
    """Matched-load ceiling Rs <= Voc^2/(4P)."""
    p = _positive("power_w", power_w)
    v = _positive("open_circuit_voltage_v", open_circuit_voltage_v)
    return v * v / (4.0 * p)


def conductor_force_n(current_a: float, magnetic_field_t: float, conductor_length_m: float, alignment: float = 1.0) -> float:
    i = _positive("current_a", current_a)
    b = _positive("magnetic_field_t", magnetic_field_t)
    length = _positive("conductor_length_m", conductor_length_m)
    if not 0.0 <= alignment <= 1.0:
        raise ValueError("alignment must be in [0, 1]")
    return i * b * length * alignment


def rotation_frequency_hz(omega_rad_s: float = EARTH_OMEGA_RAD_S) -> float:
    return _positive("omega_rad_s", omega_rad_s) / (2.0 * math.pi)


def rotating_loop_emf_peak_v(area_m2: float, magnetic_field_t: float, omega_rad_s: float = EARTH_OMEGA_RAD_S) -> float:
    """Peak emf A*B*omega for a loop rotating through a fixed uniform B field."""
    area = _positive("area_m2", area_m2)
    b = _positive("magnetic_field_t", magnetic_field_t)
    omega = _positive("omega_rad_s", omega_rad_s)
    return area * b * omega


def source_torque_nm_for_rotational_power(power_w: float, omega_rad_s: float = EARTH_OMEGA_RAD_S) -> float:
    return _positive("power_w", power_w) / _positive("omega_rad_s", omega_rad_s)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--power", type=float, default=100.0)
    parser.add_argument("--latitude", type=float, default=47.0)
    args = parser.parse_args()

    p = args.power
    b = 50e-6
    length = 0.2

    print("M2 V4.24 Earth-rotation / geomagnetic coupling upper bound")
    print("Deliberately favorable: full Earth-surface speed through a stationary B field.")

    for lat in (0.0, args.latitude):
        speed = earth_surface_speed_m_s(lat)
        emf = motional_emf_v(speed, b, length)
        current = current_for_real_power_a(p, emf)
        print(f"lat={lat:5.1f} deg: v={speed:.6g} m/s, emf<={emf:.6g} V, I@{p:.6g}W>={current:.6g} A")
        print(f"  Rload={equivalent_load_resistance_ohm(p, emf):.6g} ohm, Rs,max={max_thevenin_source_resistance_ohm(p, emf):.6g} ohm")
        print(f"  Lorentz reaction force scale={conductor_force_n(current, b, length):.6g} N")

    print("\nIf a 0.1 m^2 loop itself rotated once per sidereal-day through fixed 50 uT:")
    loop_emf = rotating_loop_emf_peak_v(0.1, b)
    print(f"f_rot={rotation_frequency_hz():.6g} Hz, emf_peak={loop_emf:.6g} V")
    print(f"I for {p:.6g} W at that emf scale={current_for_real_power_a(p, loop_emf):.6g} A")

    print("\nSource reaction if the extracted power literally came from Earth rotation:")
    print(f"tau = P/omega = {source_torque_nm_for_rotational_power(p):.6g} N m")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
