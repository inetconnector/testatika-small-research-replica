import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "sim"))

from m2_v4_10_gate_controlled_two_port_power import (
    control_power_ratio,
    power_bound_from_uniform_field_w,
    requirement,
    required_uniform_field_rms_v_m,
    symmetric_port_capacitance_required_f,
)


class V410Tests(unittest.TestCase):
    def test_100w_10mhz_100pf_each(self):
        r = requirement(100.0, 10e6, 100e-12, 100e-12, 0.0, 0.20)
        self.assertAlmostEqual(r.source_delta_v_rms, 178.4124116153, delta=1e-6)
        self.assertAlmostEqual(r.uniform_field_rms_v_m, 892.0620580764, delta=1e-6)
        self.assertAlmostEqual(r.coupling_ceq_f, 50e-12, delta=1e-18)
        self.assertAlmostEqual(r.displacement_current_rms_a, 0.56049912164, delta=1e-9)

    def test_300w_requires_sqrt3_more_voltage(self):
        a = requirement(100.0, 10e6)
        b = requirement(300.0, 10e6)
        self.assertAlmostEqual(b.source_delta_v_rms / a.source_delta_v_rms, math.sqrt(3.0), delta=1e-12)
        self.assertAlmostEqual(b.uniform_field_rms_v_m, 1545.09680809, delta=1e-6)

    def test_100vm_field_only_gives_about_1p26w_at_10mhz(self):
        p = power_bound_from_uniform_field_w(100.0, 10e6, 100e-12, 100e-12, 0.0, 0.20)
        self.assertAlmostEqual(p, 1.25663706144, delta=1e-10)

    def test_30vm_at_100mhz_is_still_about_one_watt(self):
        p = power_bound_from_uniform_field_w(30.0, 100e6, 100e-12, 100e-12, 0.0, 0.20)
        self.assertAlmostEqual(p, 1.13097335529, delta=1e-10)

    def test_field_requirement_scales_inverse_with_span(self):
        e1 = required_uniform_field_rms_v_m(100.0, 100e-12, 100e-12, 0.0, 10e6, 0.20)
        e2 = required_uniform_field_rms_v_m(100.0, 100e-12, 100e-12, 0.0, 10e6, 0.40)
        self.assertAlmostEqual(e2, e1 / 2.0, delta=1e-12)

    def test_symmetric_capacitance_formula(self):
        c = symmetric_port_capacitance_required_f(100.0, 10e6, 20.0)
        expected = 2.0 * 100.0 / (2.0 * math.pi * 10e6 * 20.0**2)
        self.assertAlmostEqual(c, expected, delta=1e-20)

    def test_control_ratio_is_not_energy_gain(self):
        ratio = control_power_ratio(100.0, 8.01088317e-9)
        self.assertGreater(ratio, 1e10)
        self.assertLess(ratio, 2e10)

    def test_invalid_geometry_rejected(self):
        with self.assertRaises(ValueError):
            requirement(100.0, 10e6, port_separation_m=0.0)
        with self.assertRaises(ValueError):
            symmetric_port_capacitance_required_f(100.0, 0.0, 100.0)


if __name__ == "__main__":
    unittest.main()
