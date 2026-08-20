import pytest

from sim.m2_v4_31_pot_envelope_reservoir_bound import (
    capacitance_gap_factor,
    capacitor_energy_j,
    recharge_power_w,
    required_area_multiplier,
    reservoir_energy_density_wh_l,
    two_pot_bounding_volume_m3,
    two_pot_electrode_envelope_area_m2,
    two_pot_optimistic_capacitance_f,
)


def test_current_v4_two_pot_envelope_geometry_scale():
    assert two_pot_electrode_envelope_area_m2() == pytest.approx(0.06785840131753954)
    assert two_pot_bounding_volume_m3() == pytest.approx(0.001219189277005127)


def test_10kj_over_1_5h_only_requires_about_1_85w_average_recharge():
    assert recharge_power_w(10_000.0, 5_400.0) == pytest.approx(1.8518518518518519)


def test_pure_moisture_benchmark_needs_more_area_than_visible_envelope():
    area = two_pot_electrode_envelope_area_m2()
    power = recharge_power_w(10_000.0, 5_400.0)
    assert required_area_multiplier(power, 6.7, area) == pytest.approx(4.073125706137403)
    assert required_area_multiplier(100.0, 6.7, area) == pytest.approx(219.94878813141975)


def test_pot_bounding_volume_can_hold_small_finite_energy_density_scale():
    volume = two_pot_bounding_volume_m3()
    assert reservoir_energy_density_wh_l(10_000.0, volume) == pytest.approx(2.2783810768096973)
    assert reservoir_energy_density_wh_l(100.0 * 5_400.0, volume) == pytest.approx(123.03257814772365)


def test_simple_two_pot_electrostatic_geometry_is_far_too_small_for_10kj_buffer():
    c_pair = two_pot_optimistic_capacitance_f(relative_permittivity=3.0)
    assert c_pair == pytest.approx(5.750291312183665e-11)
    assert capacitor_energy_j(c_pair, 100_000.0) == pytest.approx(0.28751456560918326)
    assert capacitance_gap_factor(10_000.0, 100_000.0, c_pair) == pytest.approx(34780.84659402243)


def test_50kv_gap_is_even_larger():
    c_pair = two_pot_optimistic_capacitance_f(relative_permittivity=3.0)
    assert capacitance_gap_factor(10_000.0, 50_000.0, c_pair) == pytest.approx(139123.3863760897)
