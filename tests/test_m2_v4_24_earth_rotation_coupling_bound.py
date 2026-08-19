import pytest

from sim.m2_v4_24_earth_rotation_coupling_bound import (
    conductor_force_n,
    earth_surface_speed_m_s,
    equivalent_load_resistance_ohm,
    max_thevenin_source_resistance_ohm,
    motional_emf_v,
    rotating_loop_emf_peak_v,
    rotation_frequency_hz,
    source_torque_nm_for_rotational_power,
)


def test_equator_surface_speed_is_about_464_58mps():
    assert earth_surface_speed_m_s(0.0) == pytest.approx(464.580703989)


def test_47deg_surface_speed_is_about_316_84mps():
    assert earth_surface_speed_m_s(47.0) == pytest.approx(316.843278237)


def test_absurdly_favorable_equator_vxb_across_20cm_50ut_is_only_4_646mv():
    v = earth_surface_speed_m_s(0.0)
    assert motional_emf_v(v, 50e-6, 0.2) == pytest.approx(4.64580703989e-3)


def test_absurdly_favorable_47deg_vxb_is_only_3_168mv():
    v = earth_surface_speed_m_s(47.0)
    assert motional_emf_v(v, 50e-6, 0.2) == pytest.approx(3.16843278237e-3)


def test_100w_at_equator_emf_would_need_21_5ka_and_sub_microohm_load():
    emf = motional_emf_v(earth_surface_speed_m_s(0.0), 50e-6, 0.2)
    current = 100.0 / emf
    assert current == pytest.approx(21524.7854983)
    assert equivalent_load_resistance_ohm(100.0, emf) == pytest.approx(2.15835230519e-7)
    assert max_thevenin_source_resistance_ohm(100.0, emf) == pytest.approx(5.39588076297e-8)


def test_100w_at_47deg_emf_would_need_31_6ka_and_tens_of_nanohms_source():
    emf = motional_emf_v(earth_surface_speed_m_s(47.0), 50e-6, 0.2)
    current = 100.0 / emf
    assert current == pytest.approx(31561.3449515)
    assert equivalent_load_resistance_ohm(100.0, emf) == pytest.approx(1.00389662964e-7)
    assert max_thevenin_source_resistance_ohm(100.0, emf) == pytest.approx(2.50974157410e-8)


def test_lorentz_force_times_surface_speed_closes_the_100w_reaction_scale():
    speed = earth_surface_speed_m_s(0.0)
    emf = motional_emf_v(speed, 50e-6, 0.2)
    current = 100.0 / emf
    force = conductor_force_n(current, 50e-6, 0.2)
    assert force == pytest.approx(0.215247854983)
    assert force * speed == pytest.approx(100.0)


def test_earth_rotation_frequency_is_about_11_6_microhertz():
    assert rotation_frequency_hz() == pytest.approx(1.16057629108e-5)


def test_0_1m2_loop_rotating_once_per_day_through_50ut_has_sub_nanovolt_emf():
    emf = rotating_loop_emf_peak_v(0.1, 50e-6)
    assert emf == pytest.approx(3.64605795e-10)
    assert 100.0 / emf == pytest.approx(2.74268816819e11)


def test_100w_literal_earth_rotation_source_reaction_is_1_37_mn_m():
    assert source_torque_nm_for_rotational_power(100.0) == pytest.approx(1.37134408409e6)


def test_invalid_latitude_and_alignment_are_rejected():
    with pytest.raises(ValueError):
        earth_surface_speed_m_s(91.0)
    with pytest.raises(ValueError):
        motional_emf_v(1.0, 50e-6, 0.2, alignment=1.1)
