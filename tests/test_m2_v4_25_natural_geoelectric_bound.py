import pytest

from sim.m2_v4_25_natural_geoelectric_bound import (
    equivalent_load_resistance_ohm,
    integrated_line_voltage_v,
    max_thevenin_source_resistance_ohm,
    span_for_voltage_m,
    voltage_across_span_v,
)


def test_1v_per_km_across_20cm_is_only_0_2mv():
    assert voltage_across_span_v(1.0, 0.2) == pytest.approx(2e-4)


def test_3v_per_km_across_20cm_is_only_0_6mv():
    assert voltage_across_span_v(3.0, 0.2) == pytest.approx(6e-4)


def test_12v_per_km_across_20cm_is_only_2_4mv():
    assert voltage_across_span_v(12.0, 0.2) == pytest.approx(2.4e-3)


def test_1989_us_21_66v_per_km_across_20cm_is_4_332mv():
    v = voltage_across_span_v(21.66, 0.2)
    assert v == pytest.approx(4.332e-3)
    assert 100.0 / v == pytest.approx(23084.0258541)
    assert equivalent_load_resistance_ohm(100.0, v) == pytest.approx(1.8766224e-7)
    assert max_thevenin_source_resistance_ohm(100.0, v) == pytest.approx(4.691556e-8)


def test_carrington_median_30_3v_per_km_across_20cm_is_6_06mv():
    v = voltage_across_span_v(30.3, 0.2)
    assert v == pytest.approx(6.06e-3)
    assert 100.0 / v == pytest.approx(16501.650165)
    assert max_thevenin_source_resistance_ohm(100.0, v) == pytest.approx(9.1809e-8)


def test_carrington_upper_ci_47_2v_per_km_still_only_gives_9_44mv_across_20cm():
    v = voltage_across_span_v(47.2, 0.2)
    assert v == pytest.approx(9.44e-3)
    assert 100.0 / v == pytest.approx(10593.220339)
    assert max_thevenin_source_resistance_ohm(100.0, v) == pytest.approx(2.22784e-7)


def test_100kv_baseline_at_30_3v_per_km_is_about_3300km():
    assert span_for_voltage_m(100e3, 30.3) / 1000.0 == pytest.approx(3300.330033)


def test_100kv_baseline_at_47_2v_per_km_is_still_over_2100km():
    assert span_for_voltage_m(100e3, 47.2) / 1000.0 == pytest.approx(2118.644068)


def test_long_lines_integrate_geoelectric_field():
    assert integrated_line_voltage_v(1.0, 100.0) == pytest.approx(100.0)
    assert integrated_line_voltage_v(30.3, 100.0) == pytest.approx(3030.0)


def test_invalid_field_and_span_are_rejected():
    with pytest.raises(ValueError):
        voltage_across_span_v(0.0, 0.2)
    with pytest.raises(ValueError):
        voltage_across_span_v(1.0, 0.0)
