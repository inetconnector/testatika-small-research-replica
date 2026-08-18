import math

import pytest

from sim.m2_v4_12_local_structured_coupling import (
    capacitive_apparent_power_bound,
    capacitive_rms_current,
    energy_per_cycle,
    hidden_conductive_current,
    induced_rms_voltage,
    plate_capacitance,
    required_b_field_rms,
    required_capacitance,
    required_capacitive_voltage,
    required_mutual_inductance,
)


def test_100w_at_100khz_is_one_millijoule_per_cycle():
    assert energy_per_cycle(100.0, 100e3) == pytest.approx(1e-3)


def test_100w_at_50hz_is_two_joules_per_cycle():
    assert energy_per_cycle(100.0, 50.0) == pytest.approx(2.0)


def test_100kv_real_port_only_needs_one_milliamp_for_100w():
    assert hidden_conductive_current(100.0, 100e3) == pytest.approx(1e-3)


def test_30cm_plate_5mm_eps3_is_about_478pf():
    c = plate_capacitance(0.09, 5e-3, epsilon_r=3.0)
    assert c == pytest.approx(4.781261418912e-10)


def test_30cm_plate_half_mm_eps3_is_about_4_78nf():
    c = plate_capacitance(0.09, 0.5e-3, epsilon_r=3.0)
    assert c == pytest.approx(4.781261418912e-9)


def test_478pf_base_needs_about_577v_at_100khz_for_100va_bound():
    c = plate_capacitance(0.09, 5e-3, epsilon_r=3.0)
    v = required_capacitive_voltage(100.0, 100e3, c)
    assert v == pytest.approx(576.9508546)
    assert capacitive_rms_current(100e3, c, v) == pytest.approx(0.1733249881)
    assert capacitive_apparent_power_bound(100e3, c, v) == pytest.approx(100.0)


def test_478pf_base_needs_about_25_8kv_at_50hz_for_100va_bound():
    c = plate_capacitance(0.09, 5e-3, epsilon_r=3.0)
    assert required_capacitive_voltage(100.0, 50.0, c) == pytest.approx(25802.02661)


def test_1kv_100khz_needs_about_159pf_for_100va_bound():
    assert required_capacitance(100.0, 100e3, 1e3) == pytest.approx(1.591549431e-10)


def test_10kv_100khz_only_needs_about_1_59pf_for_100va_bound():
    assert required_capacitance(100.0, 100e3, 10e3) == pytest.approx(1.591549431e-12)


def test_100kv_50hz_needs_about_31_8pf_for_100va_bound():
    assert required_capacitance(100.0, 50.0, 100e3) == pytest.approx(3.183098862e-11)


def test_24turn_200mm_loop_needs_211_microtesla_for_100v_at_100khz():
    area = math.pi * 0.1**2
    b = required_b_field_rms(100.0, 100e3, 24, area)
    assert b == pytest.approx(2.110857993e-4)
    assert induced_rms_voltage(100e3, 24, area, b) == pytest.approx(100.0)


def test_same_24turn_loop_needs_21_microtesla_at_1mhz():
    area = math.pi * 0.1**2
    assert required_b_field_rms(100.0, 1e6, 24, area) == pytest.approx(2.110857993e-5)


def test_100v_at_100khz_from_1a_primary_needs_159uh_mutual_inductance():
    assert required_mutual_inductance(100.0, 100e3, 1.0) == pytest.approx(1.591549431e-4)


def test_invalid_transfer_fraction_returns_infinite_requirement():
    assert math.isinf(required_capacitance(100.0, 100e3, 1e3, transfer_fraction=0.0))
