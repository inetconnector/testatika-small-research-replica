import pytest

from sim.m2_v4_26_two_time_phase_resonance import (
    Parameters,
    resonant_frequency_hz,
    simulate,
)


def test_resonant_frequency_for_10mh_10nf_is_about_15_9khz():
    assert resonant_frequency_hz(10e-3, 10e-9) == pytest.approx(15915.4943092)


def test_phase_gate_accumulates_dc_but_open_gate_does_not():
    on = simulate(Parameters(duration_s=0.04, steps_per_electrical_cycle=30))
    off = simulate(
        Parameters(
            duration_s=0.04,
            steps_per_electrical_cycle=30,
            diode_enabled=False,
        )
    )
    assert on.store_voltage_v > 0.05
    assert on.conduction_windows > 0
    assert off.store_voltage_v == pytest.approx(0.0)
    assert off.conduction_windows == 0


def test_passive_model_closes_energy_balance():
    r = simulate(Parameters(duration_s=0.04, steps_per_electrical_cycle=40))
    assert abs(r.energy_residual_j) < max(1e-15, r.pump_energy_j * 1e-4)
    accounted = (
        r.store_energy_j
        + r.resonator_energy_j
        + r.resonator_loss_j
        + r.diode_loss_j
        + r.load_energy_j
    )
    assert accounted == pytest.approx(r.pump_energy_j, rel=1e-4)


def test_zero_pump_cannot_self_start_or_charge_store():
    r = simulate(
        Parameters(
            duration_s=0.02,
            steps_per_electrical_cycle=30,
            impulse_charge_c=0.0,
        )
    )
    assert r.pump_energy_j == pytest.approx(0.0)
    assert r.store_voltage_v == pytest.approx(0.0)
    assert r.store_energy_j == pytest.approx(0.0)


def test_capacitance_shift_can_cross_diode_threshold_abruptly():
    conducting = simulate(
        Parameters(
            resonator_c_f=14e-9,
            resonator_l_h=10e-3,
            impulse_charge_c=3e-9,
            duration_s=0.02,
            steps_per_electrical_cycle=30,
        )
    )
    blocked = simulate(
        Parameters(
            resonator_c_f=15e-9,
            resonator_l_h=10e-3,
            impulse_charge_c=3e-9,
            duration_s=0.02,
            steps_per_electrical_cycle=30,
        )
    )
    assert conducting.conduction_windows > 0
    assert conducting.store_voltage_v > 0.0
    assert blocked.conduction_windows == 0
    assert blocked.store_voltage_v == pytest.approx(0.0)
