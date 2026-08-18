import math
import sys
import unittest
from dataclasses import replace
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "sim"))

from m2_v4_2_multiphase_corona import Config
from m2_v4_7_radioionization_integration import RadioConfig
from m2_v4_8_workpoint_window import (
    critical_plate_scale,
    initial_gate_snapshot,
    seed_window_nc,
)


class V48Tests(unittest.TestCase):
    def setUp(self):
        self.cfg = Config(rpm=15.0, seed_grid_charge_c=5e-9, crystal_knee_v=100.0)
        self.radio = RadioConfig(
            activity_bq=10_000.0,
            deposited_energy_mev_per_decay=5.0,
            collection_efficiency=1.0,
            electrical_energy_capture_efficiency=1.0,
        )

    def test_default_initial_drive_is_near_knee(self):
        s = initial_gate_snapshot(self.cfg, replace(self.radio, activity_bq=0.0), duration_s=4.0)
        self.assertAlmostEqual(s.drive_v, 100.321406240166, delta=1e-6)
        self.assertAlmostEqual(s.margin_v, 0.321406240166, delta=1e-6)

    def test_default_gate_effective_capacitance(self):
        s = initial_gate_snapshot(self.cfg, self.radio, duration_s=4.0)
        self.assertAlmostEqual(s.ceff_f, 3.559727430466e-12, delta=1e-18)

    def test_zero_activity_does_not_advance_gate(self):
        s = initial_gate_snapshot(self.cfg, replace(self.radio, activity_bq=0.0), duration_s=4.0)
        self.assertAlmostEqual(s.bound_v, s.drive_v, delta=1e-12)

    def test_plate_reduces_passive_drive(self):
        clear = initial_gate_snapshot(self.cfg, replace(self.radio, activity_bq=0.0), duration_s=4.0)
        plate = initial_gate_snapshot(replace(self.cfg, plate_scale=0.1), replace(self.radio, activity_bq=0.0), duration_s=4.0)
        self.assertLess(plate.drive_v, clear.drive_v)
        self.assertAlmostEqual(plate.drive_v, 89.6161701215, delta=1e-6)

    def test_optimistic_radio_bound_can_cover_multi_volt_deficit(self):
        cfg = replace(self.cfg, seed_grid_charge_c=4.0e-9)
        passive = initial_gate_snapshot(cfg, replace(self.radio, activity_bq=0.0), duration_s=4.0)
        biased = initial_gate_snapshot(cfg, self.radio, duration_s=4.0)
        self.assertLess(passive.drive_v, 100.0)
        self.assertGreater(biased.bound_v, passive.drive_v + 10.0)

    def test_seed_sensitive_window_is_not_microvolt_narrow(self):
        w = seed_window_nc(self.cfg, self.radio, plate_scale=0.0, duration_s=4.0)
        self.assertGreater(w.width_nc, 1.0)
        self.assertGreater(w.voltage_deficit_covered_v, 20.0)
        self.assertAlmostEqual(w.seed_no_radio_threshold_nc, 4.9839811735, delta=1e-6)

    def test_default_seed_has_finite_plate_failure_point(self):
        crit = critical_plate_scale(self.cfg, self.radio, duration_s=4.0)
        self.assertGreater(crit, 0.20)
        self.assertLess(crit, 0.26)
        self.assertAlmostEqual(crit, 0.2311018421, delta=1e-5)

    def test_plate_point_two_still_crosses_but_point_three_does_not(self):
        s02 = initial_gate_snapshot(replace(self.cfg, plate_scale=0.2), self.radio, duration_s=4.0)
        s03 = initial_gate_snapshot(replace(self.cfg, plate_scale=0.3), self.radio, duration_s=4.0)
        self.assertTrue(s02.crosses_knee)
        self.assertFalse(s03.crosses_knee)
        self.assertGreater(s02.bound_v, 100.0)
        self.assertLess(s03.bound_v, 100.0)


if __name__ == "__main__":
    unittest.main()
