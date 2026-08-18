import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "sim"))

from m2_v4_1_pot_crystal import (
    Config, Network, simulate_fixed, simulate_free_rotor, replace
)


class V41Tests(unittest.TestCase):
    def test_matrix_is_floating_laplacian(self):
        net = Network(Config(steps_per_rev=48, revolutions=1, plate_scale=0.5))
        c = net.matrix(0.37)
        for i in range(len(c)):
            self.assertAlmostEqual(sum(c[i]), 0.0, delta=5e-25)
            for j in range(len(c)):
                self.assertAlmostEqual(c[i][j], c[j][i], delta=1e-28)

    def test_crystal_preserves_total_free_charge(self):
        cfg = Config(steps_per_rev=48, revolutions=1, crystal_threshold_v=0.0)
        net = Network(cfg)
        q = [cfg.seed_grid_charge_c, -cfg.seed_grid_charge_c, 0.0, 0.0, 0.0, 0.0]
        q1, stats = net.crystal_step(0.0, q)
        self.assertAlmostEqual(sum(q1), sum(q), delta=1e-24)
        self.assertGreaterEqual(stats.crystal_loss_j, 0.0)

    def test_passive_crystal_never_raises_field_energy(self):
        cfg = Config(steps_per_rev=48, revolutions=1, crystal_threshold_v=0.0)
        net = Network(cfg)
        q = [cfg.seed_grid_charge_c, -cfg.seed_grid_charge_c, 0.0, 0.0, 0.0, 0.0]
        u0 = net.energy(0.0, q)
        q1, _ = net.crystal_step(0.0, q)
        u1 = net.energy(0.0, q1)
        self.assertLessEqual(u1, u0 + max(1e-24, abs(u0) * 1e-10))

    def test_fixed_speed_energy_balance_closes(self):
        r = simulate_fixed(Config(steps_per_rev=48, revolutions=2, crystal_threshold_v=100.0))
        scale = max(
            abs(r.initial_field_j) + abs(r.mechanical_work_j) + abs(r.final_field_j)
            + abs(r.crystal_loss_j) + abs(r.load_energy_j),
            1e-24,
        )
        self.assertLess(abs(r.residual_j), scale * 1e-9)

    def test_floating_plate_can_switch_threshold_conduction_off(self):
        base = Config(steps_per_rev=48, revolutions=2, crystal_threshold_v=100.0)
        clear = simulate_fixed(base)
        plated = simulate_fixed(replace(base, plate_scale=0.5))
        self.assertGreater(clear.crystal_events, 0)
        self.assertEqual(plated.crystal_events, 0)

    def test_load_energy_is_booked_not_created(self):
        r = simulate_fixed(Config(
            steps_per_rev=48, revolutions=2, crystal_threshold_v=100.0,
            load_relaxation=0.01
        ))
        self.assertGreater(r.load_energy_j, 0.0)
        scale = max(abs(r.initial_field_j) + abs(r.mechanical_work_j), 1e-24)
        self.assertLess(abs(r.residual_j), scale * 1e-9)

    def test_free_rotor_energy_balance_closes(self):
        r = simulate_free_rotor(Config(
            steps_per_rev=48, revolutions=2, crystal_threshold_v=100.0,
            load_relaxation=0.005, friction_torque_nm=1e-5
        ))
        scale = max(
            abs(r.initial_field_j) + abs(r.initial_kinetic_j)
            + abs(r.final_field_j) + abs(r.final_kinetic_j)
            + abs(r.crystal_loss_j) + abs(r.load_energy_j) + abs(r.friction_loss_j),
            1e-24,
        )
        self.assertLess(abs(r.residual_j), scale * 1e-8)


if __name__ == "__main__":
    unittest.main()
