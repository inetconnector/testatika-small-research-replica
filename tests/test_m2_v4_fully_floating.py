import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "sim"))

from m2_v4_fully_floating import Config, FloatingNetwork, capacitance_modulation, simulate


class FullyFloatingTests(unittest.TestCase):
    def test_rows_sum_to_zero_no_ground_shunt(self):
        net = FloatingNetwork(Config(steps_per_rev=24, revolutions=1))
        c = net.matrix(0.37)
        for row in c:
            self.assertAlmostEqual(sum(row), 0.0, delta=2e-26)

    def test_common_mode_is_gauge_only(self):
        net = FloatingNetwork(Config(steps_per_rev=24, revolutions=1))
        c = net.matrix(0.11)
        q = [2e-12, -2e-12, 0.0, 0.0]
        v = net.voltages_from_matrix(c, q)
        self.assertAlmostEqual(sum(v), 0.0, delta=1e-12)

    def test_total_charge_required_zero(self):
        net = FloatingNetwork(Config(steps_per_rev=24, revolutions=1))
        with self.assertRaises(ValueError):
            net.voltages(0, [1e-12, 0.0, 0.0, 0.0])

    def test_passive_energy_balance_closes(self):
        r = simulate(Config(steps_per_rev=48, revolutions=4))
        scale = max(abs(r.initial_energy_j) + abs(r.mechanical_work_j) + abs(r.valve_loss_j) + abs(r.final_energy_j), 1e-24)
        self.assertLess(abs(r.residual_j), scale * 1e-9)

    def test_default_case_does_not_grow_after_settling(self):
        r = simulate(Config(steps_per_rev=48, revolutions=6))
        self.assertTrue(math.isfinite(r.late_gain))
        self.assertAlmostEqual(r.late_gain, 1.0, delta=1e-9)

    def test_plate_changes_capacitance_and_reduces_final_amplitude(self):
        base = Config(steps_per_rev=48, revolutions=4, plate_scale=0.0)
        plated = Config(steps_per_rev=48, revolutions=4, plate_scale=10.0)
        rb = simulate(base)
        rp = simulate(plated)
        _, _, ratio_base = capacitance_modulation(base)
        _, _, ratio_plate = capacitance_modulation(plated)
        self.assertNotAlmostEqual(ratio_base, ratio_plate, delta=1e-7)
        self.assertLess(rp.amplitude_v[-1], rb.amplitude_v[-1])


if __name__ == "__main__":
    unittest.main()
