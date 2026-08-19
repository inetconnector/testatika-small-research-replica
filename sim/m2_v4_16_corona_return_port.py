#!/usr/bin/env python3
"""V4.16 passive atmospheric corona-current / floating-return diagnostics.

The question is whether sharp or magnetically structured electrodes can turn the
Earth-atmosphere potential into a milliamp-class current port for an M2-like
floating machine.  The model deliberately uses optimistic point-discharge
relations as upper-bound diagnostics; it is not a construction guide and it does
not add corona hardware to the historical M2 baseline.

Main lesson: corona can greatly increase atmospheric current under strong storm
fields, but it requires a real two-terminal return path.  A floating body charges
itself until the corona-driving field is reduced.  High open-circuit voltage and
brief microamp pulses are therefore not equivalent to a sustained 1 mA port.
"""

from __future__ import annotations

import math

EPS0 = 8.8541878128e-12


def _positive(value: float, name: str) -> None:
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def point_potential_scale_v(ambient_field_v_m: float, height_m: float) -> float:
    """Macroscopic point-potential scale Vp = E0*h used in Chapman-type models."""
    _positive(ambient_field_v_m, "ambient_field_v_m")
    _positive(height_m, "height_m")
    return ambient_field_v_m * height_m


def chapman_ambient_point_current_a(
    ambient_field_v_m: float,
    height_m: float,
    onset_potential_v: float,
    ion_mobility_m2_v_s: float = 1.5e-4,
) -> float:
    """Approximate grounded-point corona-current scale from Chapman (1977).

    Uses i ~= 3.9*eps0*k*E0*(Vp - V0p), Vp=E0*h, only when Vp>V0p.
    This is a literature-scale diagnostic, not a universal onset law.
    """
    _positive(ambient_field_v_m, "ambient_field_v_m")
    _positive(height_m, "height_m")
    _positive(onset_potential_v, "onset_potential_v")
    _positive(ion_mobility_m2_v_s, "ion_mobility_m2_v_s")
    vp = point_potential_scale_v(ambient_field_v_m, height_m)
    if vp <= onset_potential_v:
        return 0.0
    return 3.9 * EPS0 * ion_mobility_m2_v_s * ambient_field_v_m * (vp - onset_potential_v)


def zero_onset_point_current_upper_bound_a(
    ambient_field_v_m: float,
    height_m: float,
    ion_mobility_m2_v_s: float = 1.5e-4,
) -> float:
    """Unphysical V0=0 Chapman limit used only as an optimistic upper bound."""
    _positive(ambient_field_v_m, "ambient_field_v_m")
    _positive(height_m, "height_m")
    _positive(ion_mobility_m2_v_s, "ion_mobility_m2_v_s")
    vp = point_potential_scale_v(ambient_field_v_m, height_m)
    return 3.9 * EPS0 * ion_mobility_m2_v_s * ambient_field_v_m * vp


def required_independent_points(target_current_a: float, current_per_point_a: float) -> float:
    _positive(target_current_a, "target_current_a")
    _positive(current_per_point_a, "current_per_point_a")
    return target_current_a / current_per_point_a


def required_collection_area_m2(target_current_a: float, current_density_a_m2: float) -> float:
    _positive(target_current_a, "target_current_a")
    _positive(current_density_a_m2, "current_density_a_m2")
    return target_current_a / current_density_a_m2


def isolated_sphere_capacitance_f(radius_m: float) -> float:
    """Self-capacitance 4*pi*eps0*R used as a floating-body order-of-magnitude bound."""
    _positive(radius_m, "radius_m")
    return 4.0 * math.pi * EPS0 * radius_m


def floating_voltage_slew_v_s(current_a: float, capacitance_f: float) -> float:
    """Magnitude dV/dt = I/C for a floating body with no balancing return current."""
    _positive(abs(current_a), "current_a magnitude")
    _positive(capacitance_f, "capacitance_f")
    return abs(current_a) / capacitance_f


def time_to_self_bias_s(capacitance_f: float, bias_change_v: float, current_a: float) -> float:
    """Time C*DeltaV/I to charge a floating body enough to alter its corona field."""
    _positive(capacitance_f, "capacitance_f")
    _positive(bias_change_v, "bias_change_v")
    _positive(abs(current_a), "current_a magnitude")
    return capacitance_f * bias_change_v / abs(current_a)


def max_return_resistance_ohm(allowed_bias_change_v: float, sustained_current_a: float) -> float:
    """Largest DC return resistance compatible with I*R <= allowed self-bias."""
    _positive(allowed_bias_change_v, "allowed_bias_change_v")
    _positive(abs(sustained_current_a), "sustained_current_a magnitude")
    return allowed_bias_change_v / abs(sustained_current_a)


def return_time_constant_s(return_resistance_ohm: float, capacitance_f: float) -> float:
    _positive(return_resistance_ohm, "return_resistance_ohm")
    _positive(capacitance_f, "capacitance_f")
    return return_resistance_ohm * capacitance_f


def charge_per_event_c(current_a: float, events_per_s: float) -> float:
    _positive(abs(current_a), "current_a magnitude")
    _positive(events_per_s, "events_per_s")
    return abs(current_a) / events_per_s


def equivalent_capacitance_for_charge_f(charge_c: float, voltage_v: float) -> float:
    _positive(charge_c, "charge_c")
    _positive(voltage_v, "voltage_v")
    return charge_c / voltage_v


def real_power_w(voltage_v: float, current_a: float) -> float:
    _positive(abs(voltage_v), "voltage_v magnitude")
    _positive(abs(current_a), "current_a magnitude")
    return abs(voltage_v * current_a)


def current_needed_for_power_a(power_w: float, voltage_v: float) -> float:
    _positive(power_w, "power_w")
    _positive(abs(voltage_v), "voltage_v magnitude")
    return power_w / abs(voltage_v)


def current_density_gain(target_current_density_a_m2: float, baseline_current_density_a_m2: float) -> float:
    _positive(target_current_density_a_m2, "target_current_density_a_m2")
    _positive(baseline_current_density_a_m2, "baseline_current_density_a_m2")
    return target_current_density_a_m2 / baseline_current_density_a_m2


def main() -> None:
    print("V4.16 passive atmospheric corona / floating-return bounds")

    # Fair-weather tabletop comparison.
    e_fw = 100.0
    h_m2 = 0.2
    v0 = 5_000.0
    i_fw = chapman_ambient_point_current_a(e_fw, h_m2, v0)
    i_fw_zero = zero_onset_point_current_upper_bound_a(e_fw, h_m2)
    print(f"fair-weather point-potential scale E*h: {point_potential_scale_v(e_fw, h_m2):.6g} V")
    print(f"fair-weather 20-cm Chapman current with 5-kV onset: {i_fw:.6g} A")
    print(f"fair-weather 20-cm zero-onset fantasy upper bound: {i_fw_zero:.6g} A")
    print(f"independent zero-onset points needed for 1 mA: {required_independent_points(1e-3, i_fw_zero):.6g}")

    # Storm-scale comparison chosen to reproduce the microamp order reported in field studies.
    i_storm = chapman_ambient_point_current_a(8_000.0, 4.0, v0)
    print(f"4-m grounded point at 8 kV/m current scale: {i_storm:.6g} A")
    print(f"area for 1 mA at 1 nA/m^2 storm corona density: {required_collection_area_m2(1e-3, 1e-9):.6g} m^2")
    print(f"area for 1 mA at 2 pA/m^2 fair-weather density: {required_collection_area_m2(1e-3, 2e-12):.6g} m^2")

    # Floating-body self-bias bound.
    c_body = isolated_sphere_capacitance_f(0.1)
    print(f"0.1-m-radius isolated-sphere capacitance: {c_body:.6g} F")
    for current in (1e-6, 1e-3):
        slew = floating_voltage_slew_v_s(current, c_body)
        t5k = time_to_self_bias_s(c_body, 5_000.0, current)
        print(f"I={current:.6g} A -> dV/dt={slew:.6g} V/s, time to 5 kV self-bias={t5k:.6g} s")

    print(f"return R allowed for 1 mA with <=5 kV self-bias: {max_return_resistance_ohm(5_000.0, 1e-3):.6g} ohm")
    print(f"return R allowed for 1 mA with <=100 kV drop: {max_return_resistance_ohm(100_000.0, 1e-3):.6g} ohm")

    q_event = charge_per_event_c(1e-3, 24.0)
    c_eq = equivalent_capacitance_for_charge_f(q_event, 100e3)
    print(f"1 mA at 24 events/s -> charge per event: {q_event:.6g} C")
    print(f"same 100-kV target charge packet corresponds to C=Q/V: {c_eq:.6g} F")


if __name__ == "__main__":
    main()
