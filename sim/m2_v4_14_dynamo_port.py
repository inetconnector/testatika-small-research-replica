#!/usr/bin/env python3
"""V4.14 Earth-ionosphere-magnetosphere dynamo-port bounds.

This module asks whether a very high-impedance, resonant, magnetically structured
M2-like apparatus could obtain real power from the global atmospheric electric
circuit (GEC) or magnetosphere-ionosphere dynamo potentials.

The model is deliberately optimistic about voltage access and ideal impedance
transformation. It never treats resonance, magnetic flux concentration, or an
ideal transformer as an energy source. The useful discriminator is available
real power and source impedance, not open-circuit voltage.
"""

from __future__ import annotations

import math


def require_positive(value: float, name: str) -> None:
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def area_normalized_source_resistance(voltage_v: float, current_density_a_m2: float) -> float:
    """Return V/J in ohm*m^2 for an equipotential atmospheric column model."""
    require_positive(voltage_v, "voltage_v")
    require_positive(current_density_a_m2, "current_density_a_m2")
    return voltage_v / current_density_a_m2


def source_resistance_for_area(voltage_v: float, current_density_a_m2: float, area_m2: float) -> float:
    """Thevenin source resistance for a collector area in the optimistic full-column model."""
    require_positive(area_m2, "area_m2")
    return area_normalized_source_resistance(voltage_v, current_density_a_m2) / area_m2


def short_circuit_current(current_density_a_m2: float, area_m2: float) -> float:
    require_positive(current_density_a_m2, "current_density_a_m2")
    require_positive(area_m2, "area_m2")
    return current_density_a_m2 * area_m2


def max_matched_power(voltage_v: float, source_resistance_ohm: float) -> float:
    """Maximum real power of an ideal resistive Thevenin source: V_oc^2/(4 R_s)."""
    require_positive(voltage_v, "voltage_v")
    require_positive(source_resistance_ohm, "source_resistance_ohm")
    return voltage_v**2 / (4.0 * source_resistance_ohm)


def effective_area_for_current(target_current_a: float, current_density_a_m2: float) -> float:
    require_positive(target_current_a, "target_current_a")
    require_positive(current_density_a_m2, "current_density_a_m2")
    return target_current_a / current_density_a_m2


def effective_area_for_loaded_target(
    source_open_voltage_v: float,
    current_density_a_m2: float,
    load_voltage_v: float,
    load_current_a: float,
) -> float:
    """Area required so a Thevenin GEC source can hold a specified loaded operating point.

    The optimistic source is V_oc with R_s = (V_oc/J)/A.  At the requested load
    point, R_s may be no larger than (V_oc - V_load)/I_load.
    """
    require_positive(source_open_voltage_v, "source_open_voltage_v")
    require_positive(current_density_a_m2, "current_density_a_m2")
    require_positive(load_voltage_v, "load_voltage_v")
    require_positive(load_current_a, "load_current_a")
    if load_voltage_v >= source_open_voltage_v:
        return math.inf
    allowed_source_r = (source_open_voltage_v - load_voltage_v) / load_current_a
    return area_normalized_source_resistance(source_open_voltage_v, current_density_a_m2) / allowed_source_r


def source_resistance_for_matched_power(source_open_voltage_v: float, target_power_w: float) -> float:
    """Largest Thevenin R_s that can deliver target_power_w under ideal matching."""
    require_positive(source_open_voltage_v, "source_open_voltage_v")
    require_positive(target_power_w, "target_power_w")
    return source_open_voltage_v**2 / (4.0 * target_power_w)


def local_column_bound(
    field_v_m: float,
    current_density_a_m2: float,
    height_m: float,
    area_m2: float,
) -> tuple[float, float, float, float]:
    """Return local V_oc, inferred conductivity, R_s and matched-power bound.

    This is more realistic for a tabletop object than granting the full ionosphere
    potential to a 20-cm apparatus.
    """
    require_positive(field_v_m, "field_v_m")
    require_positive(current_density_a_m2, "current_density_a_m2")
    require_positive(height_m, "height_m")
    require_positive(area_m2, "area_m2")
    voltage = field_v_m * height_m
    conductivity = current_density_a_m2 / field_v_m
    resistance = height_m / (conductivity * area_m2)
    return voltage, conductivity, resistance, max_matched_power(voltage, resistance)


def ideal_transform_source(voltage_v: float, source_resistance_ohm: float, voltage_ratio: float) -> tuple[float, float, float]:
    """Ideal transformer mapping of a Thevenin source.

    voltage_ratio = V_secondary/V_primary.  The transformed source resistance is
    n^2 R_s, so maximum available real power is invariant.
    """
    require_positive(voltage_v, "voltage_v")
    require_positive(source_resistance_ohm, "source_resistance_ohm")
    require_positive(voltage_ratio, "voltage_ratio")
    v2 = voltage_v * voltage_ratio
    r2 = source_resistance_ohm * voltage_ratio**2
    i2_sc = v2 / r2
    return v2, r2, i2_sc


def faraday_emf_peak(
    loop_area_m2: float,
    frequency_hz: float,
    magnetic_amplitude_t: float,
    turns: float = 1.0,
    flux_gain: float = 1.0,
) -> float:
    """Peak sinusoidal Faraday EMF N*A*omega*B, with an explicit flux-gain factor."""
    for value, name in (
        (loop_area_m2, "loop_area_m2"),
        (frequency_hz, "frequency_hz"),
        (magnetic_amplitude_t, "magnetic_amplitude_t"),
        (turns, "turns"),
        (flux_gain, "flux_gain"),
    ):
        require_positive(value, name)
    return turns * flux_gain * loop_area_m2 * (2.0 * math.pi * frequency_hz) * magnetic_amplitude_t


def resonant_voltage_gain_required(target_voltage_v: float, drive_voltage_v: float) -> float:
    require_positive(target_voltage_v, "target_voltage_v")
    require_positive(drive_voltage_v, "drive_voltage_v")
    return target_voltage_v / drive_voltage_v


def resonator_amplitude_ringdown_s(q_factor: float, frequency_hz: float) -> float:
    """Approximate amplitude e-folding time tau ~= Q/(pi*f)."""
    require_positive(q_factor, "q_factor")
    require_positive(frequency_hz, "frequency_hz")
    return q_factor / (math.pi * frequency_hz)


def ion_magnetization_parameter(mobility_m2_v_s: float, magnetic_field_t: float) -> float:
    """Return omega_c*tau = mobility*B for a singly charged drift carrier.

    beta << 1 means collision-dominated motion; beta >> 1 means magnetized drift.
    """
    require_positive(mobility_m2_v_s, "mobility_m2_v_s")
    require_positive(magnetic_field_t, "magnetic_field_t")
    return mobility_m2_v_s * magnetic_field_t


def required_aperture_for_flux(target_power_w: float, poynting_flux_w_m2: float) -> float:
    require_positive(target_power_w, "target_power_w")
    require_positive(poynting_flux_w_m2, "poynting_flux_w_m2")
    return target_power_w / poynting_flux_w_m2


def geoelectric_span_voltage(field_v_per_km: float, span_m: float) -> float:
    require_positive(field_v_per_km, "field_v_per_km")
    require_positive(span_m, "span_m")
    return (field_v_per_km / 1000.0) * span_m


def current_for_power(power_w: float, voltage_v: float) -> float:
    require_positive(power_w, "power_w")
    require_positive(voltage_v, "voltage_v")
    return power_w / voltage_v


def switched_capacitance_for_power(power_w: float, voltage_v: float, events_per_s: float) -> float:
    """C required if each event can transfer the full 1/2*C*V^2 electrostatic energy."""
    require_positive(power_w, "power_w")
    require_positive(voltage_v, "voltage_v")
    require_positive(events_per_s, "events_per_s")
    return 2.0 * power_w / (events_per_s * voltage_v**2)


def charge_transport_current(capacitance_f: float, voltage_v: float, events_per_s: float) -> float:
    """Average |Q| transport scale C*V*events_per_s for full recharge each event."""
    require_positive(capacitance_f, "capacitance_f")
    require_positive(voltage_v, "voltage_v")
    require_positive(events_per_s, "events_per_s")
    return capacitance_f * voltage_v * events_per_s


def main() -> None:
    v_iono = 250e3
    j_fw = 2e-12
    area = 0.1
    target_v = 100e3
    target_i = 1e-3
    target_p = target_v * target_i

    r_area = area_normalized_source_resistance(v_iono, j_fw)
    r_table = source_resistance_for_area(v_iono, j_fw, area)
    p_table = max_matched_power(v_iono, r_table)
    print("V4.14 Earth-ionosphere-magnetosphere dynamo-port bounds")
    print(f"fair-weather area-normalized source resistance: {r_area:.6g} ohm*m^2")
    print(f"optimistic full-column 0.1-m^2 source resistance: {r_table:.6g} ohm")
    print(f"0.1-m^2 short-circuit current scale: {short_circuit_current(j_fw, area):.6g} A")
    print(f"0.1-m^2 ideal matched-power bound: {p_table:.6g} W")

    area_i = effective_area_for_current(target_i, j_fw)
    area_loaded = effective_area_for_loaded_target(v_iono, j_fw, target_v, target_i)
    r_100w = source_resistance_for_matched_power(v_iono, target_p)
    print(f"area for 1 mA at 2 pA/m^2: {area_i:.6g} m^2")
    print(f"area to hold 100 kV at 1 mA from a 250-kV Thevenin source: {area_loaded:.6g} m^2")
    print(f"R_s required for 100 W matched from 250 kV: <= {r_100w:.6g} ohm")
    print(f"tabletop source-impedance gap: {r_table/r_100w:.6g}x")

    v_local, sigma, r_local, p_local = local_column_bound(100.0, j_fw, 0.2, area)
    print(f"20-cm local fair-weather port: V={v_local:.6g} V, sigma={sigma:.6g} S/m, R={r_local:.6g} ohm, Pmax={p_local:.6g} W")

    loop_area = math.pi * 0.1**2
    emf = faraday_emf_peak(loop_area, 5e-3, 400e-9)
    q_needed = resonant_voltage_gain_required(target_v, emf)
    print(f"400-nT, 5-mHz, 200-mm one-turn loop peak EMF: {emf:.6g} V")
    print(f"voltage gain to 100 kV from that one-turn EMF: {q_needed:.6g}")

    beta = ion_magnetization_parameter(1.5e-4, 1.0)
    print(f"small-air-ion magnetization parameter at 1 T for mobility 1.5e-4 m^2/V/s: {beta:.6g}")

    print(f"ideal aperture for 100 W at 10 mW/m^2 auroral Poynting flux: {required_aperture_for_flux(100.0, 10e-3):.6g} m^2")
    storm_v = geoelectric_span_voltage(1.5, 0.2)
    print(f"0.2-m span at 1.5 V/km storm geoelectric field: {storm_v:.6g} V; 100-W current would be {current_for_power(100.0, storm_v):.6g} A")

    c_req = switched_capacitance_for_power(100.0, 250e3, 24.0)
    i_q = charge_transport_current(c_req, 250e3, 24.0)
    print(f"full-swing switched C for 100 W at 250 kV and 24 events/s: {c_req:.6g} F")
    print(f"corresponding full-recharge charge-transport scale: {i_q:.6g} A")


if __name__ == "__main__":
    main()
