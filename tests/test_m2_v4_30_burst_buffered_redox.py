import pytest

from sim.m2_v4_30_burst_buffered_redox import (
    AL_AIR_PRACTICAL_COMPARISON_WH_KG,
    CU_TO_CU2O_THEORETICAL_WH_KG,
    CU_TO_CUO_THEORETICAL_WH_KG,
    active_mass_kg,
    average_recharge_power_w,
    burst_energy_j,
    burst_energy_wh,
    cells_in_series,
    required_buffer_capacitance_f,
    source_current_a,
)


def test_holzherr_scale_1kw_ten_second_burst_is_only_10kj():
    assert burst_energy_j(1000.0, 10.0) == pytest.approx(10000.0)
    assert burst_energy_wh(1000.0, 10.0) == pytest.approx(2.77777777778)


def test_10kj_recharged_over_one_and_a_half_hours_needs_under_two_watts_average():
    assert average_recharge_power_w(10000.0, 5400.0) == pytest.approx(1.85185185185)


def test_active_material_scale_for_single_10kj_burst():
    energy_wh = 10000.0 / 3600.0
    assert active_mass_kg(energy_wh, AL_AIR_PRACTICAL_COMPARISON_WH_KG) == pytest.approx(0.00147911489765)
    assert active_mass_kg(energy_wh, CU_TO_CUO_THEORETICAL_WH_KG) == pytest.approx(0.00495323169021)
    assert active_mass_kg(energy_wh, CU_TO_CU2O_THEORETICAL_WH_KG) == pytest.approx(0.00859391693602)


def test_buffer_capacitance_scale_falls_quadratically_with_voltage():
    energy_j = 10000.0
    assert required_buffer_capacitance_f(energy_j, 300.0) == pytest.approx(0.222222222222)
    assert required_buffer_capacitance_f(energy_j, 10000.0) == pytest.approx(200e-6)
    assert required_buffer_capacitance_f(energy_j, 50000.0) == pytest.approx(8e-6)
    assert required_buffer_capacitance_f(energy_j, 100000.0) == pytest.approx(2e-6)


def test_low_voltage_bulk_source_requires_large_current_without_series_stacking():
    assert source_current_a(100.0, 1.0) == pytest.approx(100.0)
    assert source_current_a(100.0, 100.0) == pytest.approx(1.0)
    assert cells_in_series(100.0, 1.0) == 100
    assert cells_in_series(100.0, 1.5) == 67


def test_positive_inputs_are_required():
    with pytest.raises(ValueError):
        burst_energy_j(0.0, 10.0)
    with pytest.raises(ValueError):
        required_buffer_capacitance_f(100.0, 0.0)
    with pytest.raises(ValueError):
        active_mass_kg(1.0, 0.0)
