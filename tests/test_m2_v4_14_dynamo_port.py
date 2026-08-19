import math

import pytest

from sim.m2_v4_14_dynamo_port import (
    area_normalized_source_resistance,
    charge_transport_current,
    effective_area_for_current,
    effective_area_for_loaded_target,
    faraday_emf_peak,
    geoelectric_span_voltage,
    ideal_transform_source,
    ion_magnetization_parameter,
    local_column_bound,
    max_matched_power,
    required_aperture_for_flux,
    resonant_voltage_gain_required,
    resonator_amplitude_ringdown_s,
    short_circuit_current,
    source_resistance_for_area,
    source_resistance_for_matched_power,
    switched_capacitance_for_power,
)


def test_fair_weather_area_normalized_resistance():
    assert area_normalized_source_resistance(250e3, 2e-12) == pytest.approx(1.25e17)


def test_tabletop_full_column_source_is_exahm_scale():
    r = source_resistance_for_area(250e3, 2e-12, 0.1)
    assert r == pytest.approx(1.25e18)
    assert short_circuit_current(2e-12, 0.1) == pytest.approx(2e-13)
    assert max_matched_power(250e3, r) == pytest.approx(12.5e-9)


def test_one_milliamp_needs_500_square_km_collection_area():
    assert effective_area_for_current(1e-3, 2e-12) == pytest.approx(5e8)


def test_100kv_1ma_loaded_from_250kv_needs_about_833_square_km():
    a = effective_area_for_loaded_target(250e3, 2e-12, 100e3, 1e-3)
    assert a == pytest.approx(8.333333333e8)


def test_100w_matched_from_250kv_requires_sub_160_megohm_source():
    r = source_resistance_for_matched_power(250e3, 100.0)
    assert r == pytest.approx(156.25e6)


def test_tabletop_gec_source_impedance_gap_is_about_eight_billion():
    r_table = source_resistance_for_area(250e3, 2e-12, 0.1)
    r_target = source_resistance_for_matched_power(250e3, 100.0)
    assert r_table / r_target == pytest.approx(8.0e9)


def test_local_20cm_port_is_only_picowatt_matched():
    v, sigma, r, p = local_column_bound(100.0, 2e-12, 0.2, 0.1)
    assert v == pytest.approx(20.0)
    assert sigma == pytest.approx(2e-14)
    assert r == pytest.approx(1e14)
    assert p == pytest.approx(1e-12)


def test_ideal_transformer_preserves_available_power():
    v1, r1 = 20.0, 1e14
    p1 = max_matched_power(v1, r1)
    v2, r2, i2_sc = ideal_transform_source(v1, r1, 5000.0)
    assert v2 == pytest.approx(100e3)
    assert r2 == pytest.approx(2.5e21)
    assert i2_sc == pytest.approx(4e-17)
    assert max_matched_power(v2, r2) == pytest.approx(p1)


def test_ulf_loop_emf_and_required_voltage_gain_are_extreme():
    area = math.pi * 0.1**2
    emf = faraday_emf_peak(area, 5e-3, 400e-9)
    assert emf == pytest.approx(3.9478417604e-10)
    gain = resonant_voltage_gain_required(100e3, emf)
    assert gain == pytest.approx(2.533029591e14)


def test_ultra_high_q_at_millihertz_implies_geological_ringdown():
    q = 2.533029591e14
    tau = resonator_amplitude_ringdown_s(q, 5e-3)
    years = tau / (365.25 * 24 * 3600)
    assert years == pytest.approx(5.109947276e8, rel=1e-6)


def test_even_one_tesla_does_not_magnetize_normal_small_air_ion_drift():
    beta = ion_magnetization_parameter(1.5e-4, 1.0)
    assert beta == pytest.approx(1.5e-4)
    assert beta < 1e-3


def test_auroral_10_mw_m2_flux_needs_10000_m2_ideal_aperture_for_100w():
    assert required_aperture_for_flux(100.0, 10e-3) == pytest.approx(1e4)


def test_extreme_1_5_v_per_km_storm_field_is_only_0_3_mv_across_20cm():
    assert geoelectric_span_voltage(1.5, 0.2) == pytest.approx(3e-4)


def test_250kv_24_event_switched_capacitance_power_scale_requires_sub_ma_charge_transport():
    c = switched_capacitance_for_power(100.0, 250e3, 24.0)
    assert c == pytest.approx(133.333333333e-12)
    assert charge_transport_current(c, 250e3, 24.0) == pytest.approx(0.8e-3)
