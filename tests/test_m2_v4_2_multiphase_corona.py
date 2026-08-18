import sys
import unittest
from dataclasses import replace
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "sim"))

from m2_v4_2_multiphase_corona import (
    Config, Network, _initial_charge, simulate_fixed, simulate_free_rotor
)


class V42Tests(unittest.TestCase):
    def test_matrix_is_floating_laplacian(self):
        cfg = Config(steps_per_rev=24, revolutions=1, plate_scale=2.0)
        net = Network(cfg)
        c = net.matrix(0.37)
        for i in range(len(c)):
            self.assertAlmostEqual(sum(c[i]), 0.0, delta=5e-24)
            for j in range(len(c)):
                self.assertAlmostEqual(c[i][j], c[j][i], delta=1e-28)

    def test_nonlinear_paths_conserve_total_charge(self):
        cfg = Config(steps_per_rev=24, revolutions=1, plate_scale=2.0)
        net = Network(cfg)
        q = _initial_charge(cfg)
        q1, st = net.nonlinear_step(0, q)
        self.assertAlmostEqual(sum(q1), sum(q), delta=1e-23)
        self.assertGreaterEqual(st.crystal_loss_j, 0.0)
        self.assertGreaterEqual(st.corona_loss_j, 0.0)

    def test_nonlinear_paths_never_raise_field_energy(self):
        cfg = Config(steps_per_rev=24, revolutions=1, plate_scale=2.0)
        net = Network(cfg)
        q = _initial_charge(cfg)
        u0 = net.energy(0, q)
        q1, _ = net.nonlinear_step(0, q)
        self.assertLessEqual(net.energy(0, q1), u0 + max(1e-24, abs(u0) * 1e-10))

    def test_plate_can_cross_corona_onset(self):
        base = Config(steps_per_rev=24, revolutions=1, corona_onset_v=240.0)
        clear = simulate_fixed(base)
        plated = simulate_fixed(replace(base, plate_scale=5.0))
        self.assertEqual(clear.corona_events, 0)
        self.assertGreater(plated.corona_events, 0)

    def test_plate_strongly_suppresses_continuous_crystal_charge(self):
        base = Config(steps_per_rev=24, revolutions=1)
        clear = simulate_fixed(base)
        plated = simulate_fixed(replace(base, plate_scale=5.0))
        self.assertGreater(clear.crystal_charge_c, 0.0)
        self.assertLess(plated.crystal_charge_c, clear.crystal_charge_c / 100.0)

    def test_fixed_speed_energy_balance_closes_with_load(self):
        r = simulate_fixed(Config(
            steps_per_rev=24, revolutions=1, plate_scale=2.0,
            load_relaxation=0.005,
        ))
        scale = max(
            abs(r.initial_field_j) + abs(r.mechanical_work_j) + abs(r.final_field_j)
            + r.crystal_loss_j + r.corona_loss_j + r.load_energy_j,
            1e-24,
        )
        self.assertGreater(r.load_energy_j, 0.0)
        self.assertLess(abs(r.residual_j), scale * 1e-9)

    def test_free_rotor_energy_balance_closes(self):
        r = simulate_free_rotor(Config(
            steps_per_rev=24, revolutions=1, plate_scale=2.0,
            load_relaxation=0.005, friction_torque_nm=1e-6,
        ))
        scale = max(
            abs(r.initial_field_j) + abs(r.initial_kinetic_j)
            + abs(r.final_field_j) + abs(r.final_kinetic_j)
            + r.crystal_loss_j + r.corona_loss_j + r.load_energy_j
            + r.friction_loss_j,
            1e-24,
        )
        self.assertLess(abs(r.residual_j), scale * 1e-8)


if __name__ == "__main__":
    unittest.main()
