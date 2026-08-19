#!/usr/bin/env python3
"""V4.17 Earth-rotation / geomagnetic corotation-dynamo bounds.

This diagnostic separates three often-conflated ideas:
1) the kinematic u x B term from Earth's rotation,
2) the compensated corotation electric field of the conducting Earth/ionosphere,
3) motional EMF from the M2 rotor moving relative to a magnetic field.

Static magnetic fields do no direct work on charges.  Any homopolar/motional
conversion under load is paid by mechanical torque; the Earth-corotation field at
ground is strongly compensated by induced charge and is tiny in the lower
atmosphere according to the Swarm-derived model of Maus (2017).
"""

from __future__ import annotations

import math

EARTH_OMEGA_RAD_S = 7.2921159e-5
EARTH_RADIUS_M = 6_371_000.0


def _positive(value: float, name: str) -> None:
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def surface_speed_m_s(latitude_deg: float) -> float:
    if not -90.0 <= latitude_deg <= 90.0:
        raise ValueError("latitude_deg must be between -90 and 90")
    return EARTH_OMEGA_RAD_S * EARTH_RADIUS_M * math.cos(math.radians(latitude_deg))


def kinematic_uxb_field_upper_v_m(latitude_deg: float, magnetic_field_t: float) -> float:
    """Maximum |u x B| scale if u and B are perpendicular.

    This is deliberately an upper kinematic term, not the usable field in a
    corotating ground laboratory; induced charges largely compensate it.
    """
    _positive(magnetic_field_t, "magnetic_field_t")
    return surface_speed_m_s(latitude_deg) * magnetic_field_t


def span_voltage_v(electric_field_v_m: float, span_m: float) -> float:
    _positive(abs(electric_field_v_m), "electric_field_v_m magnitude")
    _positive(span_m, "span_m")
    return abs(electric_field_v_m) * span_m


def current_for_power_a(power_w: float, voltage_v: float) -> float:
    _positive(power_w, "power_w")
    _positive(abs(voltage_v), "voltage_v magnitude")
    return power_w / abs(voltage_v)


def power_w(voltage_v: float, current_a: float) -> float:
    _positive(abs(voltage_v), "voltage_v magnitude")
    _positive(abs(current_a), "current_a magnitude")
    return abs(voltage_v * current_a)


def homopolar_center_to_rim_emf_v(magnetic_field_t: float, rotation_hz: float, radius_m: float) -> float:
    """Ideal conducting-disk center-to-rim EMF: 1/2 * B * omega * R^2."""
    _positive(abs(magnetic_field_t), "magnetic_field_t magnitude")
    _positive(rotation_hz, "rotation_hz")
    _positive(radius_m, "radius_m")
    omega = 2.0 * math.pi * rotation_hz
    return 0.5 * abs(magnetic_field_t) * omega * radius_m**2


def torque_for_power_nm(power_w_value: float, rotation_hz: float) -> float:
    _positive(power_w_value, "power_w_value")
    _positive(rotation_hz, "rotation_hz")
    return power_w_value / (2.0 * math.pi * rotation_hz)


def magnetic_lorentz_power_w(charge_c: float, velocity_m_s: tuple[float, float, float], magnetic_field_t: tuple[float, float, float]) -> float:
    """Return q*v dot (v cross B), identically zero up to floating-point error."""
    vx, vy, vz = velocity_m_s
    bx, by, bz = magnetic_field_t
    cx = vy * bz - vz * by
    cy = vz * bx - vx * bz
    cz = vx * by - vy * bx
    return charge_c * (vx * cx + vy * cy + vz * cz)


def main() -> None:
    print("V4.17 Earth-corotation / geomagnetic dynamo bounds")

    latitude = 47.0
    b_earth = 50e-6
    e_kin = kinematic_uxb_field_upper_v_m(latitude, b_earth)
    print(f"surface speed at {latitude:g} deg latitude: {surface_speed_m_s(latitude):.6g} m/s")
    print(f"naive max |u x B| at 50 uT: {e_kin:.6g} V/m")
    print(f"naive 0.2-m span voltage before corotation-charge compensation: {span_voltage_v(e_kin, 0.2):.6g} V")

    # Maus 2017 Swarm-derived lower-atmosphere corotation-charge field scale.
    e_corotation_lower = 0.3e-3
    v_corotation = span_voltage_v(e_corotation_lower, 0.2)
    print(f"Swarm-model lower-atmosphere corotation field scale: {e_corotation_lower:.6g} V/m")
    print(f"0.2-m span at that field: {v_corotation:.6g} V")
    print(f"power at 1 mA: {power_w(v_corotation, 1e-3):.6g} W")
    print(f"current needed for 100 W: {current_for_power_a(100.0, v_corotation):.6g} A")

    for b in (50e-6, 0.5):
        emf = homopolar_center_to_rim_emf_v(b, 1.0, 0.1)
        print(f"1-Hz, 0.1-m homopolar EMF at B={b:.6g} T: {emf:.6g} V; 100-W current={current_for_power_a(100.0, emf):.6g} A")

    print(f"mechanical torque required for 100 W at 1 Hz: {torque_for_power_nm(100.0, 1.0):.6g} N*m")
    print(f"q*v dot (v x B) check: {magnetic_lorentz_power_w(1.0, (1.0,2.0,3.0), (0.1,-0.2,0.3)):.6g} W")


if __name__ == "__main__":
    main()
