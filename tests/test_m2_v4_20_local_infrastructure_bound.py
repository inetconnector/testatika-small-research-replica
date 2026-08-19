import pytest

from sim.m2_v4_20_local_infrastructure_bound import (
    apparent_power_va,
    capacitance_for_current_f,
    capacitance_for_full_swing_power_f,
    capacitive_current_a,
    capacitive_reactance_ohm,
    current_for_real_power_a,
    frequency_for_capacitive_current_hz,
    full_swing_switched_power_w,
    ideal_transformer_primary_current_a,
    resonance_inductance_h,
)


def test_100w_at_230v_needs_435ma_at_unity_power_factor():
    assert current_for_real_power_a(100.0, 230.0) == pytest.approx(0.4347826087)


def test_50hz_capacitive_path_for_435ma_needs_about_6uf():
    i = current_for_real_power_a(100.0, 230.0)
    assert capacitance_for_current_f(i, 50.0, 230.0) == pytest.approx(6.0172001169e-6)


def test_150pf_at_230v_50hz_is_only_10_84ua_and_2_49mva():
    i = capacitive_current_a(50.0, 150e-12, 230.0)
    assert i == pytest.approx(1.0838494655e-5)
    assert apparent_power_va(230.0, i) == pytest.approx(2.4928537706e-3)


def test_1nf_at_230v_50hz_is_only_72ua_and_16_6mva():
    i = capacitive_current_a(50.0, 1e-9, 230.0)
    assert i == pytest.approx(7.2256631033e-5)
    assert apparent_power_va(230.0, i) == pytest.approx(1.6619025137e-2)


def test_150pf_full_charge_discharge_24times_at_230v_is_only_95uw():
    assert full_swing_switched_power_w(150e-12, 230.0, 24.0) == pytest.approx(9.522e-5)


def test_1nf_full_charge_discharge_24times_at_230v_is_only_0_635mw():
    assert full_swing_switched_power_w(1e-9, 230.0, 24.0) == pytest.approx(6.348e-4)


def test_100w_full_swing_at_24_events_230v_would_need_158uf():
    c = capacitance_for_full_swing_power_f(100.0, 230.0, 24.0)
    assert c == pytest.approx(157.52993069e-6)


def test_resonating_150pf_at_50hz_needs_about_67_5_kilohenry():
    assert resonance_inductance_h(50.0, 150e-12) == pytest.approx(67547.4557616)


def test_resonating_1nf_at_50hz_needs_about_10_1_kilohenry():
    assert resonance_inductance_h(50.0, 1e-9) == pytest.approx(10132.1183642)


def test_hf_transition_for_150pf_reaches_100va_current_near_2mhz():
    target_i = current_for_real_power_a(100.0, 230.0)
    freq = frequency_for_capacitive_current_hz(target_i, 150e-12, 230.0)
    assert freq == pytest.approx(2.0057333723e6)
    assert resonance_inductance_h(freq, 150e-12) == pytest.approx(41.97615e-6)


def test_hf_transition_for_1nf_reaches_same_current_near_301khz():
    target_i = current_for_real_power_a(100.0, 230.0)
    freq = frequency_for_capacitive_current_hz(target_i, 1e-9, 230.0)
    assert freq == pytest.approx(300860.005845)
    assert resonance_inductance_h(freq, 1e-9) == pytest.approx(279.841e-6)


def test_150pf_reactance_at_50hz_is_21_2_megaohm():
    assert capacitive_reactance_ohm(50.0, 150e-12) == pytest.approx(2.1220659079e7)


def test_ideal_transformer_does_not_remove_100w_primary_current_requirement():
    assert ideal_transformer_primary_current_a(100.0, 230.0) == pytest.approx(0.4347826087)
    assert ideal_transformer_primary_current_a(100.0, 230.0, efficiency=0.8) == pytest.approx(0.5434782609)


def test_invalid_power_factor_is_rejected():
    with pytest.raises(ValueError):
        current_for_real_power_a(100.0, 230.0, power_factor=0.0)
