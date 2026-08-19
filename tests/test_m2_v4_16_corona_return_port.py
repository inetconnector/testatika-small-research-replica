import pytest

from sim.m2_v4_16_corona_return_port import (
    chapman_ambient_point_current_a,
    charge_per_event_c,
    current_needed_for_power_a,
    equivalent_capacitance_for_charge_f,
    floating_voltage_slew_v_s,
    isolated_sphere_capacitance_f,
    max_return_resistance_ohm,
    point_potential_scale_v,
    real_power_w,
    required_collection_area_m2,
    required_independent_points,
    return_time_constant_s,
    time_to_self_bias_s,
    zero_onset_point_current_upper_bound_a,
)


def test_20cm_fair_weather_point_potential_is_only_20v():
    assert point_potential_scale_v(100.0, 0.2) == pytest.approx(20.0)


def test_chapman_fair_weather_20cm_point_is_below_5kv_onset():
    assert chapman_ambient_point_current_a(100.0, 0.2, 5_000.0) == 0.0


def test_zero_onset_fantasy_fair_weather_upper_bound_is_only_10pa():
    assert zero_onset_point_current_upper_bound_a(100.0, 0.2) == pytest.approx(1.0359399741e-11)


def test_zero_onset_points_for_1ma_are_about_97_million():
    i = zero_onset_point_current_upper_bound_a(100.0, 0.2)
    assert required_independent_points(1e-3, i) == pytest.approx(9.6530689519e7)


def test_4m_grounded_point_in_8kv_m_storm_is_microamp_scale():
    assert chapman_ambient_point_current_a(8_000.0, 4.0, 5_000.0) == pytest.approx(1.1188151720e-6)


def test_one_ma_needs_one_square_km_at_storm_corona_density():
    assert required_collection_area_m2(1e-3, 1e-9) == pytest.approx(1e6)


def test_one_ma_needs_500_square_km_at_fair_weather_density():
    assert required_collection_area_m2(1e-3, 2e-12) == pytest.approx(5e8)


def test_20cm_diameter_floating_body_self_capacitance_is_about_11pf():
    assert isolated_sphere_capacitance_f(0.1) == pytest.approx(1.1126500554e-11)


def test_one_microamp_self_biases_11pf_body_by_5kv_in_56ms():
    c = isolated_sphere_capacitance_f(0.1)
    assert floating_voltage_slew_v_s(1e-6, c) == pytest.approx(8.9875517874e4)
    assert time_to_self_bias_s(c, 5_000.0, 1e-6) == pytest.approx(5.5632502772e-2)


def test_one_milliamp_self_biases_11pf_body_by_5kv_in_56_microseconds():
    c = isolated_sphere_capacitance_f(0.1)
    assert floating_voltage_slew_v_s(1e-3, c) == pytest.approx(8.9875517874e7)
    assert time_to_self_bias_s(c, 5_000.0, 1e-3) == pytest.approx(5.5632502772e-5)


def test_milliamp_return_path_cannot_be_extremely_high_impedance():
    assert max_return_resistance_ohm(5_000.0, 1e-3) == pytest.approx(5e6)
    assert max_return_resistance_ohm(100_000.0, 1e-3) == pytest.approx(1e8)


def test_100mohm_return_with_11pf_body_has_millisecond_rc_scale():
    c = isolated_sphere_capacitance_f(0.1)
    assert return_time_constant_s(100e6, c) == pytest.approx(1.1126500554e-3)


def test_one_ma_at_24_events_requires_41_7_microcoulomb_per_event():
    q = charge_per_event_c(1e-3, 24.0)
    assert q == pytest.approx(4.1666666667e-5)
    assert equivalent_capacitance_for_charge_f(q, 100e3) == pytest.approx(4.1666666667e-10)


def test_100w_100kv_target_is_one_ma():
    assert current_needed_for_power_a(100.0, 100e3) == pytest.approx(1e-3)
    assert real_power_w(100e3, 1e-3) == pytest.approx(100.0)
