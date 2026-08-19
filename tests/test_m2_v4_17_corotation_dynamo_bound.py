import pytest

from sim.m2_v4_17_corotation_dynamo_bound import (
    current_for_power_a,
    homopolar_center_to_rim_emf_v,
    kinematic_uxb_field_upper_v_m,
    magnetic_lorentz_power_w,
    power_w,
    span_voltage_v,
    surface_speed_m_s,
    torque_for_power_nm,
)


def test_midlatitude_surface_speed_is_about_317m_s():
    assert surface_speed_m_s(47.0) == pytest.approx(316.8432782372)


def test_naive_uxb_upper_term_is_only_16mv_m_at_50ut():
    e = kinematic_uxb_field_upper_v_m(47.0, 50e-6)
    assert e == pytest.approx(1.5842163912e-2)
    assert span_voltage_v(e, 0.2) == pytest.approx(3.1684327824e-3)


def test_swarm_corotation_charge_field_scale_is_60uv_across_20cm():
    v = span_voltage_v(0.3e-3, 0.2)
    assert v == pytest.approx(6e-5)
    assert power_w(v, 1e-3) == pytest.approx(6e-8)
    assert current_for_power_a(100.0, v) == pytest.approx(1.6666666667e6)


def test_earth_field_homopolar_emf_at_60rpm_is_microvolt_scale():
    emf = homopolar_center_to_rim_emf_v(50e-6, 1.0, 0.1)
    assert emf == pytest.approx(1.5707963268e-6)
    assert current_for_power_a(100.0, emf) == pytest.approx(6.3661977237e7)


def test_half_tesla_local_magnet_homopolar_emf_is_only_15_7mv():
    emf = homopolar_center_to_rim_emf_v(0.5, 1.0, 0.1)
    assert emf == pytest.approx(1.5707963268e-2)
    assert current_for_power_a(100.0, emf) == pytest.approx(6366.1977237)


def test_100w_at_one_hz_needs_15_9_nm_mechanical_torque():
    assert torque_for_power_nm(100.0, 1.0) == pytest.approx(15.9154943092)


def test_static_magnetic_lorentz_force_does_zero_direct_work():
    p = magnetic_lorentz_power_w(1.0, (1.0, 2.0, 3.0), (0.1, -0.2, 0.3))
    assert p == pytest.approx(0.0, abs=1e-15)
