import pytest

from sim.m2_v4_28_source_elimination_matrix import (
    captured_power_w,
    classify_gap,
    max_thevenin_resistance_ohm,
    ordinary_ambient_bounds,
    required_capture_area_m2,
    required_current_a,
)


def _by_prefix(prefix: str):
    return next(item for item in ordinary_ambient_bounds() if item.name.startswith(prefix))


def test_fair_weather_full_column_bound_is_billions_below_100w_for_0_1m2():
    item = _by_prefix("fair-weather")
    assert item.bound_w == pytest.approx(5e-8)
    assert item.gap(100.0) == pytest.approx(2e9)
    assert classify_gap(item.gap(100.0)) == "EXCLUDED_AS_BULK_AMBIENT"


def test_normal_50hz_stray_field_is_many_orders_below_100w():
    item = _by_prefix("50-Hz stray")
    assert item.bound_w == pytest.approx(6.28e-6)
    assert item.gap(100.0) == pytest.approx(1.5923566879e7)


def test_even_10kv_per_m_50hz_comparison_is_far_below_100w():
    item = _by_prefix("50-Hz extreme")
    assert item.bound_w == pytest.approx(0.0628)
    assert item.gap(100.0) == pytest.approx(1592.3566879)
    assert classify_gap(item.gap(100.0)) == "STRONGLY_CONSTRAINED"


def test_ambient_rf_power_density_over_tabletop_area_is_tiny():
    item = _by_prefix("ambient RF")
    assert item.bound_w == pytest.approx(20e-6)
    assert item.gap(100.0) == pytest.approx(5e6)
    assert required_capture_area_m2(100.0, 200e-6) == pytest.approx(500000.0)


def test_schumann_proxy_is_trillions_below_100w_for_0_1m2():
    item = _by_prefix("Schumann")
    assert item.bound_w == pytest.approx(1.59e-11)
    assert item.gap(100.0) == pytest.approx(6.2893081761e12)


def test_compact_geoelectric_voltage_requires_absurd_source_current_and_impedance():
    # V4.25 Carrington-median comparison: 30.3 V/km across 0.2 m = 6.06 mV.
    voltage = 6.06e-3
    assert required_current_a(100.0, voltage) == pytest.approx(16501.650165)
    assert max_thevenin_resistance_ohm(100.0, voltage) == pytest.approx(9.1809e-8)


def test_power_density_helpers_reject_zero_or_negative_inputs():
    with pytest.raises(ValueError):
        captured_power_w(0.0, 0.1)
    with pytest.raises(ValueError):
        required_capture_area_m2(100.0, 0.0)
