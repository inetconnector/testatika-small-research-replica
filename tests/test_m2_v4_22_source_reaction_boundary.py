import pytest

from sim.m2_v4_22_source_reaction_boundary import (
    boundary_flux_w_per_m2,
    current_density_a_per_m2,
    effective_load_resistance_ohm,
    loaded_voltage_fraction,
    max_source_resistance_for_droop_ohm,
    max_source_resistance_for_power_ohm,
    required_open_circuit_voltage_v,
    required_source_reaction_w,
    reservoir_duration_s,
    reservoir_energy_j,
    source_current_for_real_power_a,
    thevenin_max_power_w,
)


def test_100kv_100w_load_is_100_megohm():
    assert effective_load_resistance_ohm(100e3, 100.0) == pytest.approx(100e6)


def test_250kv_source_must_be_below_156_25_megohm_for_100w_even_with_matching():
    assert max_source_resistance_for_power_ohm(250e3, 100.0) == pytest.approx(156.25e6)


def test_100kv_source_must_be_below_25_megohm_for_100w_even_with_matching():
    assert max_source_resistance_for_power_ohm(100e3, 100.0) == pytest.approx(25e6)


def test_optimistic_fair_weather_thevenin_source_is_only_12_5_nanowatts():
    assert thevenin_max_power_w(250e3, 1.25e18) == pytest.approx(12.5e-9)


def test_fair_weather_source_resistance_would_need_22_36_gv_for_100w():
    assert required_open_circuit_voltage_v(100.0, 1.25e18) == pytest.approx(22.360679775e9)


def test_fair_weather_source_resistance_would_need_38_73_gv_for_300w():
    assert required_open_circuit_voltage_v(300.0, 1.25e18) == pytest.approx(38.729833462e9)


def test_100kv_100w_bus_needs_source_below_11_11_megohm_for_10pct_droop():
    rload = effective_load_resistance_ohm(100e3, 100.0)
    assert max_source_resistance_for_droop_ohm(rload, 0.10) == pytest.approx(11.111111111e6)


def test_atmospheric_source_would_collapse_100kv_100w_load_voltage():
    rload = effective_load_resistance_ohm(100e3, 100.0)
    assert loaded_voltage_fraction(1.25e18, rload) == pytest.approx(8.0e-11)


def test_source_reaction_scales_with_efficiency():
    assert required_source_reaction_w(100.0, 1.0) == pytest.approx(100.0)
    assert required_source_reaction_w(100.0, 0.5) == pytest.approx(200.0)
    assert required_source_reaction_w(100.0, 0.1) == pytest.approx(1000.0)
    assert required_source_reaction_w(100.0, 0.01) == pytest.approx(10000.0)


def test_100w_at_100kv_needs_1ma_real_current():
    assert source_current_for_real_power_a(100.0, 100e3) == pytest.approx(1e-3)


def test_100w_at_250kv_needs_0_4ma_real_current():
    assert source_current_for_real_power_a(100.0, 250e3) == pytest.approx(0.4e-3)


def test_100kv_100w_over_0_1m2_is_0_01_amp_per_m2():
    i = source_current_for_real_power_a(100.0, 100e3)
    assert current_density_a_per_m2(i, 0.1) == pytest.approx(0.01)


def test_50pf_100kv_only_stores_0_25j_and_runs_100w_for_2_5ms():
    assert reservoir_energy_j(50e-12, 100e3) == pytest.approx(0.25)
    assert reservoir_duration_s(50e-12, 100e3, 100.0) == pytest.approx(2.5e-3)


def test_50pf_250kv_stores_1_5625j_and_runs_100w_for_15_625ms():
    assert reservoir_energy_j(50e-12, 250e3) == pytest.approx(1.5625)
    assert reservoir_duration_s(50e-12, 250e3, 100.0) == pytest.approx(15.625e-3)


def test_100w_crossing_0_1m2_boundary_is_1000w_per_m2_net_flux():
    assert boundary_flux_w_per_m2(100.0, 0.1) == pytest.approx(1000.0)


def test_invalid_efficiency_and_droop_are_rejected():
    with pytest.raises(ValueError):
        required_source_reaction_w(100.0, 0.0)
    with pytest.raises(ValueError):
        max_source_resistance_for_droop_ohm(100e6, 1.0)
