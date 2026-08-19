import math

import pytest

from sim.m2_v4_19_rear_plate_human_return import (
    apparent_power_va,
    capacitor_energy_j,
    displacement_current_a,
    full_environment_ceq_f,
    full_swing_energy_rate_w,
    parallel_plate_capacitance_f,
    power_factor_required,
    rear_return_capacitance_f,
    required_ceq_f,
    required_front_capacitance_f,
    series_capacitance_f,
)


def test_30cm_square_plate_at_2cm_is_about_39_84pf():
    c = parallel_plate_capacitance_f(0.09, 0.02)
    assert c == pytest.approx(39.8438451576e-12)


def test_2cm_plate_in_series_with_150pf_body_is_about_31_48pf():
    cmp = parallel_plate_capacitance_f(0.09, 0.02)
    ret = rear_return_capacitance_f(cmp, 150e-12)
    assert ret == pytest.approx(31.4815408879e-12)


def test_human_held_2cm_plate_can_carry_milliamp_scale_reactive_current_at_250kv_24hz():
    cmp = parallel_plate_capacitance_f(0.09, 0.02)
    ret = rear_return_capacitance_f(cmp, 150e-12)
    assert displacement_current_a(24.0, ret, 250e3) == pytest.approx(1.1868261309e-3)
    assert displacement_current_a(24.0, ret, 100e3) == pytest.approx(0.4747304524e-3)


def test_distance_sweep_is_steep_for_human_held_plate():
    body = 150e-12
    c20 = rear_return_capacitance_f(parallel_plate_capacitance_f(0.09, 0.20), body)
    c2 = rear_return_capacitance_f(parallel_plate_capacitance_f(0.09, 0.02), body)
    assert c20 == pytest.approx(3.8812875685e-12)
    assert c2 == pytest.approx(31.4815408879e-12)
    assert c2 / c20 == pytest.approx(8.1111075467, rel=1e-6)


def test_target_ceq_for_1ma_at_250kv_24hz_is_26_53pf():
    target = required_ceq_f(1e-3, 24.0, 250e3)
    assert target == pytest.approx(26.5258238486e-12)


def test_front_port_still_matters_even_with_close_rear_plate():
    target = required_ceq_f(1e-3, 24.0, 250e3)
    cmp = parallel_plate_capacitance_f(0.09, 0.02)
    held = rear_return_capacitance_f(cmp, 150e-12)
    assert required_front_capacitance_f(target, cmp) == pytest.approx(79.3579461683e-12)
    assert required_front_capacitance_f(target, held) == pytest.approx(168.507160814e-12)


def test_50pf_front_plus_human_held_rear_only_gives_about_0_73ma_at_250kv():
    cmp = parallel_plate_capacitance_f(0.09, 0.02)
    held = rear_return_capacitance_f(cmp, 150e-12)
    ceq = full_environment_ceq_f(50e-12, held)
    assert ceq == pytest.approx(19.3182041876e-12)
    assert displacement_current_a(24.0, ceq, 250e3) == pytest.approx(0.7282791403e-3)


def test_100pf_front_plus_grounded_2cm_rear_crosses_1ma_at_250kv():
    rear = parallel_plate_capacitance_f(0.09, 0.02)
    ceq = full_environment_ceq_f(100e-12, rear)
    assert ceq == pytest.approx(28.4916687700e-12)
    assert displacement_current_a(24.0, ceq, 250e3) == pytest.approx(1.0741106076e-3)


def test_reactive_milliamp_is_not_100w_real_power():
    s = apparent_power_va(250e3, 1e-3)
    assert s == pytest.approx(250.0)
    assert power_factor_required(100.0, 250e3, 1e-3) == pytest.approx(0.4)


def test_human_held_rear_node_has_tens_of_watts_full_switching_energy_scale_at_250kv():
    cmp = parallel_plate_capacitance_f(0.09, 0.02)
    held = rear_return_capacitance_f(cmp, 150e-12)
    assert capacitor_energy_j(held, 250e3) == pytest.approx(0.9837981528)
    assert full_swing_energy_rate_w(24.0, held, 250e3) == pytest.approx(23.611155667)


def test_series_capacitance_rejects_missing_or_nonpositive_values():
    with pytest.raises(ValueError):
        series_capacitance_f()
    with pytest.raises(ValueError):
        series_capacitance_f(1e-12, 0.0)


def test_required_front_is_infinite_if_rear_itself_is_too_small():
    target = 30e-12
    assert math.isinf(required_front_capacitance_f(target, 20e-12))
