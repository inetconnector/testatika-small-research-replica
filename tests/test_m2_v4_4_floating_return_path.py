import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "sim"))

from m2_v4_4_floating_return_path import (
    capacitive_power_bound_two_port,
    current_required_for_local_field,
    equal_each_capacitance_required,
    local_atmospheric_area_required,
    local_field_potential,
    series_capacitance,
    two_port_power,
)


class V44ReturnPathTests(unittest.TestCase):
    def test_equal_series_capacitances_halve(self):
        self.assertAlmostEqual(
            series_capacitance(100e-12, 100e-12), 50e-12, places=24
        )

    def test_100w_230v_50hz_needs_about_12uf_each(self):
        c = equal_each_capacitance_required(100.0, 230.0, 50.0)
        self.assertAlmostEqual(c * 1e6, 12.0344002338, places=9)

    def test_two_port_bound_uses_series_capacitance(self):
        p = capacitive_power_bound_two_port(100e-12, 100e-12, 230.0, 50.0)
        self.assertAlmostEqual(p, 0.0008309512568745, places=15)

    def test_local_half_meter_at_100v_per_m_is_only_50v(self):
        self.assertEqual(local_field_potential(100.0, 0.5), 50.0)

    def test_100w_at_local_50v_needs_2a(self):
        self.assertEqual(
            current_required_for_local_field(100.0, 100.0, 0.5), 2.0
        )

    def test_local_fair_weather_area_bound_is_enormous(self):
        a = local_atmospheric_area_required(100.0, 100.0, 0.5, 2e-12)
        self.assertAlmostEqual(a / 1e6, 1_000_000.0, places=6)

    def test_two_port_power_depends_on_potential_difference(self):
        self.assertAlmostEqual(
            two_port_power(100.0, 1e-3, 0.0, -1e-3), 0.1, places=12
        )
        self.assertAlmostEqual(
            two_port_power(100.0, 1e-3, 100.0, -1e-3), 0.0, places=12
        )

    def test_nonzero_net_charge_current_is_rejected(self):
        with self.assertRaises(ValueError):
            two_port_power(100.0, 1e-3, 0.0, 0.0)


if __name__ == "__main__":
    unittest.main()
