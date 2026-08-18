import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "sim"))

from m2_v4_6_radioionization_gate import (
    activity_required_for_ion_current_bq,
    charge_per_revolution_c,
    decay_power_w,
    saturation_ion_current_a,
    voltage_per_revolution_v,
    voltage_ramp_v_s,
)


class V46Tests(unittest.TestCase):
    def test_decay_power(self):
        p = decay_power_w(10_000.0, 5.0)
        self.assertAlmostEqual(p, 8.01088317e-9, delta=1e-18)

    def test_saturation_current(self):
        i = saturation_ion_current_a(10_000.0, 5.0)
        self.assertAlmostEqual(i, 8.01088317e-9 / 33.97, delta=1e-20)

    def test_efficiency_scales_current(self):
        i1 = saturation_ion_current_a(10_000.0, 5.0, 1.0)
        i2 = saturation_ion_current_a(10_000.0, 5.0, 0.25)
        self.assertAlmostEqual(i2, i1 / 4.0, delta=1e-22)

    def test_voltage_ramp(self):
        self.assertAlmostEqual(voltage_ramp_v_s(1e-9, 100e-12), 10.0)

    def test_charge_per_revolution(self):
        self.assertAlmostEqual(charge_per_revolution_c(1e-9, 15.0), 4e-9)

    def test_voltage_per_revolution(self):
        self.assertAlmostEqual(voltage_per_revolution_v(1e-9, 100e-12, 15.0), 40.0)

    def test_required_activity_inverse(self):
        target = 1e-9
        a = activity_required_for_ion_current_bq(target, 5.0)
        back = saturation_ion_current_a(a, 5.0)
        self.assertAlmostEqual(back, target, delta=1e-21)

    def test_invalid_efficiency(self):
        with self.assertRaises(ValueError):
            saturation_ion_current_a(1000, 5.0, 1.1)


if __name__ == "__main__":
    unittest.main()
