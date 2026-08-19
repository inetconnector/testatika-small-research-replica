import math

import pytest

from sim.m2_v4_21_real_power_field_bound import (
    capacitive_reactance_ohm,
    far_field_field_for_received_power_v_m,
    far_field_power_density_w_m2,
    field_for_voltage_v_m,
    max_real_power_from_uniform_field_w,
    max_real_power_series_c_w,
    optimum_current_for_real_power_a,
    optimum_load_resistance_ohm,
    optimum_power_factor,
    source_voltage_for_real_power_v,
)


def test_series_c_power_maximum_uses_r_equal_xc():
    x = capacitive_reactance_ohm(1e6, 50e-12)
    assert x == pytest.approx(3183.09886184)
    assert optimum_load_resistance_ohm(1e6, 50e-12) == pytest.approx(x)
    assert optimum_power_factor() == pytest.approx(1.0 / math.sqrt(2.0))


def test_1mhz_50pf_needs_about_798v_for_100w_ideal_series_link():
    v = source_voltage_for_real_power_v(100.0, 1e6, 50e-12)
    i = optimum_current_for_real_power_a(100.0, 1e6, 50e-12)
    assert v == pytest.approx(797.884560803)
    assert i == pytest.approx(0.177245385091)
    assert max_real_power_series_c_w(v, 1e6, 50e-12) == pytest.approx(100.0)


def test_10mhz_50pf_needs_about_252v_for_100w():
    assert source_voltage_for_real_power_v(100.0, 10e6, 50e-12) == pytest.approx(252.313252202)
    assert optimum_current_for_real_power_a(100.0, 10e6, 50e-12) == pytest.approx(0.560499121640)


def test_100mhz_50pf_needs_about_80v_for_100w_before_aperture_limit():
    assert source_voltage_for_real_power_v(100.0, 100e6, 50e-12) == pytest.approx(79.7884560803)
    assert optimum_current_for_real_power_a(100.0, 100e6, 50e-12) == pytest.approx(1.77245385091)


def test_24hz_50pf_needs_about_163kv_source_for_100w():
    assert source_voltage_for_real_power_v(100.0, 24.0, 50e-12) == pytest.approx(162867.503968)
    assert optimum_current_for_real_power_a(100.0, 24.0, 50e-12) == pytest.approx(0.00086832150547)


def test_1mhz_100w_voltage_over_20cm_is_about_4kv_per_m():
    v = source_voltage_for_real_power_v(100.0, 1e6, 50e-12)
    assert field_for_voltage_v_m(v, 0.2) == pytest.approx(3989.42280401)


def test_100v_per_m_uniform_field_is_only_63mw_at_1mhz_for_50pf():
    assert max_real_power_from_uniform_field_w(100.0, 0.2, 1e6, 50e-12) == pytest.approx(0.0628318530718)


def test_100v_per_m_uniform_field_is_only_0_628w_at_10mhz_for_50pf():
    assert max_real_power_from_uniform_field_w(100.0, 0.2, 10e6, 50e-12) == pytest.approx(0.628318530718)


def test_100v_per_m_uniform_field_is_only_6_28w_at_100mhz_for_50pf():
    assert max_real_power_from_uniform_field_w(100.0, 0.2, 100e6, 50e-12) == pytest.approx(6.28318530718)


def test_far_field_100w_into_point_one_square_metre_needs_at_least_614v_per_m():
    e = far_field_field_for_received_power_v_m(100.0, 0.1, 1.0)
    assert e == pytest.approx(613.783604920)
    assert far_field_power_density_w_m2(e) == pytest.approx(1000.0)


def test_far_field_10percent_capture_needs_about_1_94kv_per_m():
    assert far_field_field_for_received_power_v_m(100.0, 0.1, 0.1) == pytest.approx(1940.95418201)


def test_far_field_1percent_capture_needs_about_6_14kv_per_m():
    assert far_field_field_for_received_power_v_m(100.0, 0.1, 0.01) == pytest.approx(6137.83604920)


def test_invalid_capture_efficiency_is_rejected():
    with pytest.raises(ValueError):
        far_field_field_for_received_power_v_m(100.0, 0.1, 0.0)
