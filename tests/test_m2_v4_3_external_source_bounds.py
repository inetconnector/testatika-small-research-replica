import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "sim"))

from m2_v4_3_external_source_bounds import (
    BoundCase,
    capacitive_apparent_power_bound,
    capacitive_current_rms,
    capacitance_for_duration,
    collector_area_required,
    electrostatic_store_energy,
    external_charge_energy,
    external_current_required,
    mechanical_torque_required,
    minimum_coupling_capacitance_for_power,
    reservoir_duration_s,
    summarize_case,
)


class V43BoundsTests(unittest.TestCase):
    def test_capacitive_power_identity(self):
        c, v, f = 100e-12, 230.0, 50.0
        i = capacitive_current_rms(c, v, f)
        s = capacitive_apparent_power_bound(c, v, f)
        self.assertAlmostEqual(s, v * i, places=15)

    def test_100w_requires_about_6uf_at_230v_50hz_optimistic_bound(self):
        c = minimum_coupling_capacitance_for_power(100.0, 230.0, 50.0)
        self.assertAlmostEqual(c * 1e6, 6.0172001169, places=9)

    def test_100w_at_15rpm_requires_large_torque(self):
        tau = mechanical_torque_required(100.0, 15.0)
        self.assertAlmostEqual(tau, 63.6619772368, places=9)

    def test_120pf_30kv_is_only_54_millijoule(self):
        e = electrostatic_store_energy(120e-12, 30_000.0)
        self.assertAlmostEqual(e, 0.054, places=12)
        self.assertAlmostEqual(
            reservoir_duration_s(120e-12, 30_000.0, 100.0),
            0.00054,
            places=12,
        )

    def test_100w_one_hour_at_30kv_needs_800uf(self):
        c = capacitance_for_duration(100.0, 30_000.0, 3600.0)
        self.assertAlmostEqual(c * 1e6, 800.0, places=9)

    def test_external_charge_ledger(self):
        self.assertAlmostEqual(
            external_current_required(100.0, 250_000.0), 0.0004, places=15
        )
        self.assertAlmostEqual(
            external_charge_energy(0.001, 250_000.0), 250.0, places=12
        )

    def test_fair_weather_ideal_area_is_huge(self):
        a = collector_area_required(100.0, 250_000.0, 2e-12)
        self.assertAlmostEqual(a / 1e6, 200.0, places=9)

    def test_summary_is_consistent(self):
        r = summarize_case(BoundCase(power_w=300.0))
        self.assertGreater(r["torque_nm"], 190.0)
        self.assertGreater(r["c_230v_50hz_f"], 18e-6)
        self.assertAlmostEqual(r["ion_area_m2"] / 1e6, 600.0, places=9)


if __name__ == "__main__":
    unittest.main()
