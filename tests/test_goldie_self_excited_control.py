import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "sim"))

from goldie_self_excited_control import GoldieConfig, simulate


class GoldieControlTests(unittest.TestCase):
    def test_small_signal_gain_formula(self):
        cfg = GoldieConfig(c_max_f=100e-12, c_min_f=20e-12, feedback_beta=0.40)
        self.assertAlmostEqual(cfg.capacitance_ratio, 5.0)
        self.assertAlmostEqual(cfg.ideal_small_signal_gain, 1.6)
        self.assertAlmostEqual(cfg.beta_critical, 0.25)

    def test_regenerative_case_grows_from_one_time_seed(self):
        cfg = GoldieConfig(cycles=80, feedback_beta=0.40, seed_v=10.0)
        r = simulate(cfg)
        self.assertGreater(cfg.ideal_small_signal_gain, 1.0)
        self.assertGreater(r.final_rail_v, r.samples[0].rail_v_after * 10.0)
        self.assertGreater(r.mechanical_work_j, 0.0)

    def test_below_threshold_does_not_sustain_growth(self):
        cfg = GoldieConfig(cycles=80, feedback_beta=0.10, seed_v=10.0)
        r = simulate(cfg)
        self.assertLess(cfg.ideal_small_signal_gain, 1.0)
        self.assertLess(r.final_rail_v, r.samples[0].rail_v_after)

    def test_zero_feedback_has_no_post_seed_growth(self):
        cfg = GoldieConfig(cycles=20, feedback_beta=0.0, seed_v=10.0)
        r = simulate(cfg)
        self.assertAlmostEqual(
            r.final_rail_v,
            r.samples[0].rail_v_after,
            delta=max(1e-12, r.samples[0].rail_v_after * 1e-12),
        )
        self.assertTrue(all(abs(s.mechanical_work_j) < 1e-30 for s in r.samples[1:]))

    def test_energy_balance_closes(self):
        cfg = GoldieConfig(cycles=60, feedback_beta=0.40, seed_v=10.0)
        r = simulate(cfg)
        scale = max(
            r.startup_input_j + r.mechanical_work_j + r.final_store_j
            + r.conversion_loss_j + r.load_loss_j + r.limiter_loss_j,
            1e-24,
        )
        self.assertLess(abs(r.energy_residual_j), scale * 1e-12)

    def test_limiter_clamps_rail(self):
        cfg = GoldieConfig(
            cycles=120,
            feedback_beta=0.55,
            seed_v=20.0,
            c_store_f=100e-12,
            rail_limit_v=500.0,
        )
        r = simulate(cfg)
        self.assertLessEqual(r.final_rail_v, 500.0 + 1e-9)
        self.assertGreater(r.limiter_loss_j, 0.0)

    def test_load_dissipation_is_bookkept(self):
        cfg = GoldieConfig(
            cycles=80,
            feedback_beta=0.45,
            seed_v=10.0,
            load_resistance_ohm=100e9,
        )
        r = simulate(cfg)
        self.assertGreater(r.load_loss_j, 0.0)
        scale = max(r.startup_input_j + r.mechanical_work_j, 1e-24)
        self.assertLess(abs(r.energy_residual_j), scale * 1e-12)


if __name__ == "__main__":
    unittest.main()
