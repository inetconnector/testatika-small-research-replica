import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "sim"))

from m2_regenerative_grid_model import ModelConfig, M2Network, simulate, scenario_matrix


class M2ModelTests(unittest.TestCase):
    def test_full_capacitance_matrix_is_symmetric(self):
        net = M2Network(ModelConfig(steps_per_rev=24, revolutions=1))
        c = net.full_capacitance_matrix(0.37)
        for i in range(net.n_full):
            self.assertGreater(c[i][i], 0.0)
            for j in range(net.n_full):
                self.assertAlmostEqual(c[i][j], c[j][i], delta=1e-28)

    def test_reduced_neutral_rotor_matrix_is_symmetric(self):
        net = M2Network(ModelConfig(steps_per_rev=24, revolutions=1))
        c = net.reduced_capacitance_matrix(0.123)
        self.assertEqual(len(c), 4)
        for i in range(4):
            self.assertGreater(c[i][i], 0.0)
            for j in range(4):
                self.assertAlmostEqual(c[i][j], c[j][i], delta=1e-28)

    def test_mesh_exposes_more_rotor_spiral_coupling_than_foil(self):
        mesh = M2Network(ModelConfig(grid_mode="mesh", steps_per_rev=24, revolutions=1))
        foil = M2Network(ModelConfig(grid_mode="foil", steps_per_rev=24, revolutions=1))
        theta = math.radians(52.0)
        cm = mesh.full_capacitance_matrix(theta)
        cf = foil.full_capacitance_matrix(theta)
        self.assertGreater(abs(cm[0][mesh.SL]), abs(cf[0][foil.SL]))

    def test_passive_valve_transfer_conserves_total_free_charge(self):
        cfg = ModelConfig(steps_per_rev=24, revolutions=1, feedback=True, diode_drop_v=0.0)
        net = M2Network(cfg)
        q = [0.0, 0.0, 10e-12, -10e-12]
        total0 = sum(q)
        q1, loss, _ = net.valve_step(0, q, (("SPIRAL_L", "GRID_R"),))
        self.assertAlmostEqual(sum(q1), total0, delta=1e-26)
        self.assertGreaterEqual(loss, 0.0)

    def test_energy_balance_closes(self):
        r = simulate(ModelConfig(steps_per_rev=48, revolutions=3, feedback=True))
        scale = max(abs(r.initial_energy_j) + abs(r.mechanical_work_j) + abs(r.final_energy_j) + abs(r.valve_loss_j), 1e-24)
        self.assertLess(abs(r.energy_residual_j), scale * 1e-9)

    def test_four_falsification_scenarios_are_available(self):
        cases = scenario_matrix(ModelConfig(steps_per_rev=24, revolutions=1))
        self.assertEqual([name[0] for name, _ in cases], ["A", "B", "C", "D"])
        self.assertEqual([(r.config.grid_mode, r.config.feedback) for _, r in cases], [
            ("foil", False), ("mesh", False), ("foil", True), ("mesh", True)
        ])

    def test_30_rpm_24_sector_event_rate_is_12_hz(self):
        self.assertEqual(ModelConfig(rpm=30.0).sector_event_hz, 12.0)


if __name__ == "__main__":
    unittest.main()
