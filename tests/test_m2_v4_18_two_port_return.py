import pytest

from sim.m2_v4_18_two_port_return import (
    apparent_power_va,
    capacitive_current_rms_a,
    capacitive_reactance_ohm,
    common_mode_charge_rate_a,
    equal_port_capacitance_for_series_f,
    floating_rear_plate_return_capacitance_f,
    max_uncompensated_load_power_w,
    optimum_resistive_load_uncompensated_ohm,
    plate_capacitance_f,
    plate_gap_for_capacitance_m,
    real_power_w,
    recharge_fraction_per_event,
    recharge_time_constant_s,
    required_power_factor,
    required_series_capacitance_for_current_f,
    series_capacitance_f,
    thevenin_available_power_w,
)


def test_two_equal_100pf_ports_make_50pf_series_return():
    assert series_capacitance_f(100e-12, 100e-12) == pytest.approx(50e-12)
    assert equal_port_capacitance_for_series_f(50e-12) == pytest.approx(100e-12)


def test_series_capacitance_needed_for_1ma_at_100kv():
    assert required_series_capacitance_for_current_f(1e-3, 100e3, 1.0) == pytest.approx(1.5915494309e-9)
    assert required_series_capacitance_for_current_f(1e-3, 100e3, 24.0) == pytest.approx(66.3145596216e-12)
    assert required_series_capacitance_for_current_f(1e-3, 100e3, 50.0) == pytest.approx(31.8309886184e-12)
    assert required_series_capacitance_for_current_f(1e-3, 100e3, 1e3) == pytest.approx(1.5915494309e-12)
    assert required_series_capacitance_for_current_f(1e-3, 100e3, 100e3) == pytest.approx(15.9154943092e-15)
    assert required_series_capacitance_for_current_f(1e-3, 100e3, 1e6) == pytest.approx(1.5915494309e-15)


def test_symmetric_24hz_ports_need_133pf_each():
    ceq = required_series_capacitance_for_current_f(1e-3, 100e3, 24.0)
    assert equal_port_capacitance_for_series_f(ceq) == pytest.approx(132.629119243e-12)


def test_30cm_plate_geometry_for_symmetric_24hz_return_is_mm_scale():
    ceq = required_series_capacitance_for_current_f(1e-3, 100e3, 24.0)
    ceach = equal_port_capacitance_for_series_f(ceq)
    assert plate_gap_for_capacitance_m(0.09, ceach) == pytest.approx(6.0083102994e-3)


def test_30cm_plate_geometry_for_symmetric_50hz_return_is_about_12_5mm():
    ceq = required_series_capacitance_for_current_f(1e-3, 100e3, 50.0)
    ceach = equal_port_capacitance_for_series_f(ceq)
    assert plate_gap_for_capacitance_m(0.09, ceach) == pytest.approx(12.5173131238e-3)


def test_30cm_rear_plate_at_2cm_is_about_40pf():
    c = plate_capacitance_f(0.09, 0.02)
    assert c == pytest.approx(39.8438451576e-12)
    assert capacitive_current_rms_a(100e3, 24.0, c) == pytest.approx(0.600831029942e-3)
    assert capacitive_current_rms_a(250e3, 24.0, c) == pytest.approx(1.50207757485e-3)


def test_24hz_66pf_series_port_has_100_megohm_reactance():
    ceq = required_series_capacitance_for_current_f(1e-3, 100e3, 24.0)
    assert capacitive_reactance_ohm(24.0, ceq) == pytest.approx(100e6)


def test_uncompensated_ideal_source_with_that_port_maxes_at_50w():
    ceq = required_series_capacitance_for_current_f(1e-3, 100e3, 24.0)
    assert optimum_resistive_load_uncompensated_ohm(0.0, 24.0, ceq) == pytest.approx(100e6)
    assert max_uncompensated_load_power_w(100e3, 0.0, 24.0, ceq) == pytest.approx(50.0)


def test_reactive_compensation_cannot_beat_atmospheric_thevenin_power():
    assert thevenin_available_power_w(250e3, 1.25e18) == pytest.approx(12.5e-9)


def test_atmospheric_source_recharge_of_66pf_port_takes_years():
    ceq = required_series_capacitance_for_current_f(1e-3, 100e3, 24.0)
    tau = recharge_time_constant_s(1.25e18, ceq)
    assert tau == pytest.approx(8.2893199527e7)
    assert recharge_fraction_per_event(1.25e18, ceq, 24.0) == pytest.approx(5.0265480667e-10)


def test_100kv_1ma_is_100va_and_needs_unity_pf_for_100w():
    assert apparent_power_va(100e3, 1e-3) == pytest.approx(100.0)
    assert required_power_factor(100.0, 100e3, 1e-3) == pytest.approx(1.0)
    assert real_power_w(100e3, 1e-3, 0.0) == pytest.approx(0.0)


def test_250kv_1ma_needs_pf_0_4_for_100w():
    assert apparent_power_va(250e3, 1e-3) == pytest.approx(250.0)
    assert required_power_factor(100.0, 250e3, 1e-3) == pytest.approx(0.4)


def test_floating_rear_plate_adds_another_series_capacitance():
    assert floating_rear_plate_return_capacitance_f(100e-12, 100e-12) == pytest.approx(50e-12)


def test_external_kcl_requires_balancing_terminal_for_zero_common_mode_charge():
    assert common_mode_charge_rate_a((1e-3, -1e-3)) == pytest.approx(0.0)
    assert common_mode_charge_rate_a((1e-3,)) == pytest.approx(1e-3)
