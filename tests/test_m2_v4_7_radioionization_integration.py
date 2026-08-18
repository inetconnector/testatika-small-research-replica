import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "sim"))

from m2_v4_2_multiphase_corona import Config, Network, _initial_charge, simulate_fixed as simulate_v42
from m2_v4_7_radioionization_integration import (
    RadioConfig,
    max_voltage_from_source_energy_v,
    radioionization_step,
    simulate_fixed,
    time_to_charge_cap_from_source_s,
)


class V47Tests(unittest.TestCase):
    def test_energy_only_voltage_bound(self):
        radio = RadioConfig()
        v = max_voltage_from_source_energy_v(radio.electrical_power_ceiling_w, 40.0, 100e-12)
        self.assertAlmostEqual(v, 80.0543973558, delta=1e-9)

    def test_time_to_100v_energy_bound(self):
        radio = RadioConfig()
        t = time_to_charge_cap_from_source_s(radio.electrical_power_ceiling_w, 100e-12, 100.0)
        self.assertAlmostEqual(t, 62.4150907446, delta=1e-9)

    def test_zero_activity_is_exact_v42_path(self):
        cfg = Config(steps_per_rev=24, revolutions=2, rpm=15.0)
        r42 = simulate_v42(cfg)
        r47 = simulate_fixed(cfg, RadioConfig(activity_bq=0.0))
        self.assertAlmostEqual(r47.final_field_j, r42.final_field_j, delta=max(1e-24, abs(r42.final_field_j) * 1e-10))
        self.assertAlmostEqual(r47.mechanical_work_j, r42.mechanical_work_j, delta=max(1e-24, abs(r42.mechanical_work_j) * 1e-10))
        self.assertEqual(r47.crystal_events, r42.crystal_events)
        self.assertEqual(r47.corona_events, r42.corona_events)
        self.assertEqual(r47.radio_charge_c, 0.0)
        self.assertEqual(r47.radio_source_energy_j, 0.0)

    def test_radio_step_conserves_total_free_charge(self):
        cfg = Config(steps_per_rev=24, revolutions=1, rpm=15.0)
        net = Network(cfg)
        q0 = _initial_charge(cfg)
        q1, _ = radioionization_step(net, 0, q0, 0.1, RadioConfig())
        self.assertAlmostEqual(sum(q1), sum(q0), delta=1e-20)

    def test_radio_step_respects_current_ceiling(self):
        cfg = Config(steps_per_rev=24, revolutions=1, rpm=15.0)
        net = Network(cfg)
        q0 = _initial_charge(cfg)
        radio = RadioConfig()
        dt = 0.25
        _, stats = radioionization_step(net, 0, q0, dt, radio)
        self.assertLessEqual(stats.transferred_charge_c, radio.current_ceiling_a * dt * (1.0 + 1e-9) + 1e-24)

    def test_radio_step_respects_energy_ceiling(self):
        cfg = Config(steps_per_rev=24, revolutions=1, rpm=15.0)
        net = Network(cfg)
        q0 = _initial_charge(cfg)
        radio = RadioConfig()
        dt = 0.25
        _, stats = radioionization_step(net, 0, q0, dt, radio)
        self.assertLessEqual(stats.source_energy_j, radio.electrical_power_ceiling_w * dt * (1.0 + 1e-9) + 1e-24)

    def test_full_simulation_energy_balance_closes(self):
        cfg = Config(steps_per_rev=24, revolutions=2, rpm=15.0, load_relaxation=0.002)
        r = simulate_fixed(cfg, RadioConfig())
        scale = max(
            abs(r.initial_field_j) + abs(r.mechanical_work_j) + abs(r.radio_source_energy_j)
            + abs(r.radio_passive_loss_j) + abs(r.crystal_loss_j) + abs(r.corona_loss_j)
            + abs(r.load_energy_j) + abs(r.final_field_j),
            1e-24,
        )
        self.assertLess(abs(r.residual_j), scale * 1e-8)

    def test_source_used_never_exceeds_available_over_run(self):
        cfg = Config(steps_per_rev=24, revolutions=3, rpm=15.0)
        radio = RadioConfig()
        r = simulate_fixed(cfg, radio)
        self.assertLessEqual(r.radio_source_energy_j, r.radio_available_energy_j * (1.0 + 1e-9) + 1e-24)
        duration = cfg.revolutions * 60.0 / cfg.rpm
        self.assertAlmostEqual(r.radio_available_energy_j, radio.electrical_power_ceiling_w * duration, delta=1e-20)


if __name__ == "__main__":
    unittest.main()
