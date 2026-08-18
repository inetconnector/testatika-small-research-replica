import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "sim"))

from m2_v4_5_two_environment_ports import (
    series_capacitance,
    rear_thevenin,
    two_port_plate_bound,
    required_source_delta_v,
)


class V45Tests(unittest.TestCase):
    def test_equal_series_capacitances_halve(self):
        self.assertAlmostEqual(series_capacitance(100e-12, 100e-12), 50e-12, delta=1e-24)

    def test_no_plate_preserves_full_source_difference(self):
        r = two_port_plate_bound(100e-12, 100e-12, 0.0, 10_000.0, 50.0)
        self.assertAlmostEqual(r.delta_v_effective_rms, 10_000.0, delta=1e-9)
        self.assertAlmostEqual(r.source_suppression, 1.0, delta=1e-12)

    def test_equal_plate_and_rear_coupling_halves_source_difference(self):
        r = two_port_plate_bound(100e-12, 100e-12, 100e-12, 10_000.0, 50.0)
        self.assertAlmostEqual(r.delta_v_effective_rms, 5_000.0, delta=1e-9)
        self.assertAlmostEqual(r.source_suppression, 0.5, delta=1e-12)

    def test_plate_can_strongly_collapse_differential_source(self):
        clear = two_port_plate_bound(100e-12, 100e-12, 0.0, 10_000.0, 50.0)
        plated = two_port_plate_bound(100e-12, 100e-12, 1e-9, 10_000.0, 50.0)
        self.assertLess(plated.power_bound_w, clear.power_bound_w / 50.0)
        self.assertLess(plated.source_suppression, 0.1)

    def test_100pf_each_10kv_50hz_bound(self):
        r = two_port_plate_bound(100e-12, 100e-12, 0.0, 10_000.0, 50.0)
        self.assertAlmostEqual(r.power_bound_w, math.pi / 2.0, delta=1e-12)

    def test_required_voltage_for_100w_at_50hz(self):
        v = required_source_delta_v(100.0, 100e-12, 100e-12, 0.0, 50.0)
        self.assertAlmostEqual(v, 79_788.45608028653, delta=1e-6)

    def test_required_voltage_falls_as_inverse_sqrt_frequency(self):
        v50 = required_source_delta_v(100.0, 100e-12, 100e-12, 0.0, 50.0)
        v5k = required_source_delta_v(100.0, 100e-12, 100e-12, 0.0, 5_000.0)
        self.assertAlmostEqual(v50 / v5k, 10.0, delta=1e-10)

    def test_rear_thevenin_moves_toward_front_reservoir_with_plate(self):
        va, vb = 5_000.0, -5_000.0
        v0, _ = rear_thevenin(100e-12, 0.0, va, vb)
        v1, _ = rear_thevenin(100e-12, 1e-9, va, vb)
        self.assertAlmostEqual(v0, vb, delta=1e-9)
        self.assertGreater(v1, 4_000.0)
        self.assertLess(v1, va)


if __name__ == "__main__":
    unittest.main()
