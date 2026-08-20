import math

import pytest

from sim.m2_v4_27_reservoir_isolation import (
    EnergyBudget,
    capacitor_charge_for_event_energy_c,
    capacitor_voltage_for_event_energy_v,
    charge_per_event_c,
    energy_per_event_j,
    impulse_energy_j,
    residual_significance_sigma,
    rss_uncertainty_j,
    scale_gap,
    source_current_for_power_a,
)


def test_closed_budget_has_zero_residual():
    budget = EnergyBudget(
        load_j=1.0,
        delta_stored_j=0.2,
        losses_j=0.3,
        mechanical_in_j=1.5,
    )
    assert budget.demand_j == pytest.approx(1.5)
    assert budget.known_input_j == pytest.approx(1.5)
    assert budget.residual_j == pytest.approx(0.0)


def test_released_storage_reduces_required_external_input():
    budget = EnergyBudget(
        load_j=1.0,
        delta_stored_j=-0.4,
        losses_j=0.1,
        mechanical_in_j=0.7,
    )
    assert budget.residual_j == pytest.approx(0.0)


def test_rss_uncertainty_and_significance():
    sigma = rss_uncertainty_j(0.03, 0.04)
    assert sigma == pytest.approx(0.05)
    assert residual_significance_sigma(0.25, sigma) == pytest.approx(5.0)
    assert math.isinf(residual_significance_sigma(1.0, 0.0))


def test_v426_reference_impulse_is_five_nanojoule():
    e = impulse_energy_j(10e-9, 10e-9)
    assert e == pytest.approx(5e-9)


def test_100w_at_50hz_requires_two_joules_per_event():
    required = energy_per_event_j(100.0, 50.0)
    reference = impulse_energy_j(10e-9, 10e-9)
    assert required == pytest.approx(2.0)
    assert scale_gap(required, reference) == pytest.approx(4e8)


def test_3kw_at_50hz_requires_sixty_joules_per_event():
    required = energy_per_event_j(3000.0, 50.0)
    reference = impulse_energy_j(10e-9, 10e-9)
    assert required == pytest.approx(60.0)
    assert scale_gap(required, reference) == pytest.approx(1.2e10)


def test_required_charge_and_current_at_100kv():
    assert source_current_for_power_a(100.0, 100e3) == pytest.approx(1e-3)
    assert charge_per_event_c(100.0, 50.0, 100e3) == pytest.approx(20e-6)
    assert source_current_for_power_a(3000.0, 100e3) == pytest.approx(0.03)
    assert charge_per_event_c(3000.0, 50.0, 100e3) == pytest.approx(600e-6)


def test_equivalent_10nf_event_voltage_scale():
    assert capacitor_voltage_for_event_energy_v(100.0, 50.0, 10e-9) == pytest.approx(20_000.0)
    assert capacitor_charge_for_event_energy_c(100.0, 50.0, 10e-9) == pytest.approx(200e-6)
    assert capacitor_voltage_for_event_energy_v(3000.0, 50.0, 10e-9) == pytest.approx(109_544.5115, rel=1e-9)


def test_invalid_inputs_are_rejected():
    with pytest.raises(ValueError):
        energy_per_event_j(1.0, 0.0)
    with pytest.raises(ValueError):
        source_current_for_power_a(1.0, 0.0)
    with pytest.raises(ValueError):
        impulse_energy_j(-1.0, 1e-9)
