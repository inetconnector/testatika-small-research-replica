import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "sim"))

from m2_v4_2_multiphase_corona import Config
from m2_v4_7_radioionization_integration import RadioConfig
from m2_v4_9_gate_efficiency_sensitivity import evaluate, robustness_class


class V49Tests(unittest.TestCase):
    def setUp(self):
        self.cfg = Config(rpm=15.0, seed_grid_charge_c=5e-9, crystal_knee_v=100.0)
        self.radio = RadioConfig(
            activity_bq=10_000.0,
            deposited_energy_mev_per_decay=5.0,
            collection_efficiency=1.0,
            electrical_energy_capture_efficiency=1.0,
        )

    def test_full_efficiency_reproduces_v48_window(self):
        r = evaluate(self.cfg, self.radio, 1.0, 1.0, duration_s=4.0)
        self.assertAlmostEqual(r.window_nc, 1.2880443351, delta=1e-5)
        self.assertAlmostEqual(r.voltage_deficit_covered_v, 25.8436837986, delta=1e-4)
        self.assertAlmostEqual(r.critical_plate_scale, 0.2311018421, delta=1e-5)

    def test_thirty_percent_still_multi_volt(self):
        r = evaluate(self.cfg, self.radio, 0.3, 0.3, duration_s=4.0)
        self.assertGreater(r.voltage_deficit_covered_v, 6.0)
        self.assertLess(r.voltage_deficit_covered_v, 8.0)
        self.assertGreater(r.critical_plate_scale, 0.05)
        self.assertEqual(robustness_class(r), "multi-volt")

    def test_ten_percent_is_about_two_volts(self):
        r = evaluate(self.cfg, self.radio, 0.1, 0.1, duration_s=4.0)
        self.assertAlmostEqual(r.voltage_deficit_covered_v, 2.2763287465, delta=1e-4)
        self.assertAlmostEqual(r.critical_plate_scale, 0.0225166877, delta=1e-5)
        self.assertEqual(robustness_class(r), "multi-volt")

    def test_one_percent_is_subvolt(self):
        r = evaluate(self.cfg, self.radio, 0.01, 0.01, duration_s=4.0)
        self.assertAlmostEqual(r.voltage_deficit_covered_v, 0.2252958294, delta=1e-4)
        self.assertLess(r.critical_plate_scale, 0.01)
        self.assertEqual(robustness_class(r), "sub-volt")

    def test_point_one_percent_is_fine_tuned(self):
        r = evaluate(self.cfg, self.radio, 0.001, 0.001, duration_s=4.0)
        self.assertLess(r.voltage_deficit_covered_v, 0.03)
        self.assertGreater(r.voltage_deficit_covered_v, 0.0)
        self.assertEqual(robustness_class(r), "fine-tuned")

    def test_energy_budget_can_be_more_restrictive_than_current(self):
        energy_limited = evaluate(self.cfg, self.radio, 1.0, 0.1, duration_s=4.0)
        current_limited = evaluate(self.cfg, self.radio, 0.1, 1.0, duration_s=4.0)
        self.assertLess(energy_limited.voltage_deficit_covered_v, current_limited.voltage_deficit_covered_v)

    def test_invalid_efficiency_rejected(self):
        with self.assertRaises(ValueError):
            evaluate(self.cfg, self.radio, 1.1, 1.0, duration_s=4.0)
        with self.assertRaises(ValueError):
            evaluate(self.cfg, self.radio, 1.0, -0.1, duration_s=4.0)

    def test_efficiency_reduction_monotonically_shrinks_window(self):
        rows = [evaluate(self.cfg, self.radio, e, e, duration_s=4.0) for e in (1.0, 0.3, 0.1, 0.03, 0.01)]
        widths = [r.window_nc for r in rows]
        deficits = [r.voltage_deficit_covered_v for r in rows]
        self.assertTrue(all(a > b for a, b in zip(widths, widths[1:])))
        self.assertTrue(all(a > b for a, b in zip(deficits, deficits[1:])))


if __name__ == "__main__":
    unittest.main()
