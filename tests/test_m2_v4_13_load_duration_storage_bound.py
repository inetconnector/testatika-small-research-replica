import math

import pytest

from sim.m2_v4_13_load_duration_storage_bound import (
    capacitor_energy_j,
    energy_j,
    joules_to_wh,
    required_capacitance_for_energy,
    runtime_s,
    storage_wh_required,
    wh_to_j,
)


def test_1000w_for_10s_is_10kj():
    assert energy_j(1000.0, 10.0) == pytest.approx(10000.0)


def test_10kj_is_2_78wh():
    assert joules_to_wh(10000.0) == pytest.approx(2.7777777778)


def test_1000w_for_1_5h_is_1_5kwh():
    e = energy_j(1000.0, 1.5 * 3600.0)
    assert joules_to_wh(e) == pytest.approx(1500.0)


def test_100w_for_one_hour_is_100wh():
    assert joules_to_wh(energy_j(100.0, 3600.0)) == pytest.approx(100.0)


def test_100w_for_one_minute_is_1_667wh():
    assert joules_to_wh(energy_j(100.0, 60.0)) == pytest.approx(1.6666666667)


def test_10kj_at_100kv_requires_2uf():
    assert required_capacitance_for_energy(10000.0, 100e3) == pytest.approx(2e-6)


def test_10kj_at_30kv_requires_22_22uf():
    assert required_capacitance_for_energy(10000.0, 30e3) == pytest.approx(22.222222222e-6)


def test_100w_one_hour_at_100kv_requires_72uf_ideal():
    e = energy_j(100.0, 3600.0)
    assert required_capacitance_for_energy(e, 100e3) == pytest.approx(72e-6)


def test_2uf_at_100kv_stores_10kj():
    assert capacitor_energy_j(2e-6, 100e3) == pytest.approx(10000.0)


def test_2_78wh_storage_can_ideally_supply_1kw_for_10s():
    e = wh_to_j(2.7777777778)
    assert runtime_s(e, 1000.0) == pytest.approx(10.0)


def test_efficiency_increases_required_storage():
    assert storage_wh_required(1000.0, 10.0, efficiency=0.8) == pytest.approx(3.4722222222)


def test_zero_load_gives_infinite_runtime():
    assert math.isinf(runtime_s(1000.0, 0.0))
