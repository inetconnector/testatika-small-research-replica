import math

import pytest

from sim.m2_v4_11_environmental_port_survey import (
    capacitive_ac_bound,
    fair_weather_power_density,
    plane_wave_flux_proxy,
    required_area,
    required_uniform_field,
    rotating_loop_peak_emf,
)


def test_full_column_fair_weather_density_is_half_microwatt_per_m2():
    assert fair_weather_power_density(2e-12, 250e3) == pytest.approx(5e-7)


def test_full_column_fair_weather_needs_200_square_km_for_100w():
    density = fair_weather_power_density(2e-12, 250e3)
    assert required_area(100.0, density) == pytest.approx(2e8)


def test_tabletop_fair_weather_local_gradient_is_tiny():
    # 100 V/m over 0.2 m gives 20 V. At 2 pA/m^2 this is 40 pW/m^2.
    assert fair_weather_power_density(2e-12, 100.0 * 0.2) == pytest.approx(4e-11)


def test_50hz_home_field_capacitive_bound_is_microwatts():
    assert capacitive_ac_bound(50.0, 50e-12, 100.0, 0.2) == pytest.approx(6.283185307e-6)


def test_50hz_field_required_for_100w_is_hundreds_of_kv_per_m():
    required = required_uniform_field(100.0, 50.0, 50e-12, 0.2)
    assert required == pytest.approx(398942.2804)


def test_ambient_rf_high_average_capture_area_is_half_square_km():
    assert required_area(100.0, 200e-6) == pytest.approx(500000.0)


def test_schumann_proxy_is_sub_nanowatt_per_square_metre():
    proxy = plane_wave_flux_proxy(0.2e-3, 1e-12)
    assert proxy == pytest.approx(1.59154943e-10)
    assert required_area(100.0, proxy) == pytest.approx(6.283185307e11)


def test_geomagnetic_one_turn_200mm_loop_is_only_microvolts_at_60rpm():
    area = math.pi * 0.1**2
    emf = rotating_loop_peak_emf(50e-6, area, 60.0)
    assert emf == pytest.approx(9.8696044e-6)


def test_geomagnetic_24_turn_scaling_remains_sub_millivolt():
    area = math.pi * 0.1**2
    emf = rotating_loop_peak_emf(50e-6, area, 60.0, turns=24)
    assert emf == pytest.approx(2.368705056e-4)


def test_zero_power_density_requires_infinite_area():
    assert math.isinf(required_area(100.0, 0.0))
