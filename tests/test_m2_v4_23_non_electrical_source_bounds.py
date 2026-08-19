import pytest

from sim.m2_v4_23_non_electrical_source_bounds import (
    acoustic_pressure_rms_pa_for_power,
    acoustic_spl_db_for_power,
    carnot_efficiency,
    intercepted_radiant_power_w,
    minimum_heat_flow_w_for_power,
    required_irradiance_w_m2,
    solid_disk_rotational_energy_j,
    stored_energy_required_j,
    vibration_force_rms_n_for_power,
    wind_speed_for_power_m_s,
)


def test_100w_airflow_over_0_1m2_needs_nearly_11_86mps_at_100pct():
    assert wind_speed_for_power_m_s(100.0, 0.1) == pytest.approx(11.856311015)


def test_100w_airflow_over_0_1m2_needs_nearly_17_71mps_at_30pct():
    assert wind_speed_for_power_m_s(100.0, 0.1, efficiency=0.3) == pytest.approx(17.710976153)


def test_300w_airflow_needs_over_17mps_even_at_100pct():
    assert wind_speed_for_power_m_s(300.0, 0.1) == pytest.approx(17.099759467)


def test_100w_acoustic_over_0_1m2_is_about_150db_even_at_100pct_capture():
    assert acoustic_pressure_rms_pa_for_power(100.0, 0.1) == pytest.approx(641.560597294)
    assert acoustic_spl_db_for_power(100.0, 0.1) == pytest.approx(150.124153748)


def test_10pct_acoustic_capture_pushes_requirement_to_about_160db():
    assert acoustic_spl_db_for_power(100.0, 0.1, efficiency=0.1) == pytest.approx(160.124153748)


def test_10k_gradient_at_room_temperature_has_only_3_3pct_carnot_ceiling():
    eta = carnot_efficiency(303.0, 293.0)
    assert eta == pytest.approx(0.03300330033)
    assert minimum_heat_flow_w_for_power(100.0, 303.0, 293.0) == pytest.approx(3030.0)


def test_50k_gradient_still_needs_at_least_686w_heat_flow_for_100w_output():
    assert minimum_heat_flow_w_for_power(100.0, 343.0, 293.0) == pytest.approx(686.0)


def test_100k_gradient_still_needs_at_least_393w_heat_flow_for_100w_output():
    assert minimum_heat_flow_w_for_power(100.0, 393.0, 293.0) == pytest.approx(393.0)


def test_1000w_per_m2_over_0_1m2_only_intercepts_100w_before_conversion_losses():
    assert intercepted_radiant_power_w(1000.0, 0.1) == pytest.approx(100.0)
    assert intercepted_radiant_power_w(1000.0, 0.1, 0.2) == pytest.approx(20.0)


def test_100w_at_20pct_optical_conversion_needs_5000w_per_m2_over_0_1m2():
    assert required_irradiance_w_m2(100.0, 0.1, 0.2) == pytest.approx(5000.0)


def test_100w_for_one_minute_needs_at_least_6kj_stored_energy():
    assert stored_energy_required_j(100.0, 60.0) == pytest.approx(6000.0)


def test_100w_for_one_hour_needs_100wh_360kj():
    assert stored_energy_required_j(100.0, 3600.0) == pytest.approx(360000.0)


def test_generous_1kg_20cm_disk_at_60rpm_has_only_0_099j():
    e = solid_disk_rotational_energy_j(1.0, 0.1, 60.0)
    assert e == pytest.approx(0.09869604401)
    assert e / 100.0 == pytest.approx(0.00098696044)


def test_1mm_rms_50hz_vibration_would_need_318n_in_phase_for_100w():
    assert vibration_force_rms_n_for_power(100.0, 50.0, 1e-3) == pytest.approx(318.309886184)


def test_0_1mm_rms_50hz_vibration_would_need_3183n_in_phase_for_100w():
    assert vibration_force_rms_n_for_power(100.0, 50.0, 1e-4) == pytest.approx(3183.09886184)


def test_invalid_efficiency_and_temperature_order_are_rejected():
    with pytest.raises(ValueError):
        wind_speed_for_power_m_s(100.0, 0.1, efficiency=0.0)
    with pytest.raises(ValueError):
        carnot_efficiency(293.0, 293.0)
