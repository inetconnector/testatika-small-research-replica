import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "sim"))

from m2_v3_distributed_rotor import (
    DistributedConfig,
    ROUTES,
    effective_arc_pickup_capacitance,
    neutral_wire_mediated_capacitance,
    scan_modulation,
    sweep,
)


class DistributedRotorTests(unittest.TestCase):
    def test_route_weights_sum_to_one(self):
        for route, lobes in ROUTES.items():
            self.assertAlmostEqual(sum(x.weight for x in lobes), 1.0, places=12)

    def test_neutral_wire_schur_term(self):
        c = neutral_wire_mediated_capacitance(2e-12, 3e-12, 1e-12)
        self.assertAlmostEqual(c, 1e-12, delta=1e-24)

    def test_geometry_repeats_after_one_sector_pitch(self):
        cfg = DistributedConfig(route="R0", aperture_half_width_deg=10)
        c0 = effective_arc_pickup_capacitance(0.123, cfg)
        c1 = effective_arc_pickup_capacitance(
            0.123 + 2 * math.pi / cfg.sectors, cfg
        )
        self.assertAlmostEqual(c0, c1, delta=max(abs(c0), 1e-30) * 1e-10)

    def test_narrow_pickup_modulates_more_than_broad(self):
        narrow = scan_modulation(
            DistributedConfig(route="R0", aperture_half_width_deg=10)
        )
        broad = scan_modulation(
            DistributedConfig(route="R0", aperture_half_width_deg=38)
        )
        self.assertGreater(narrow.ratio, broad.ratio * 2.0)

    def test_r0_10deg_crosses_bridge_threshold_at_beta_04(self):
        r = scan_modulation(
            DistributedConfig(
                route="R0", aperture_half_width_deg=10, feedback_beta=0.4
            )
        )
        self.assertGreater(r.rho_bridge, 1.0)

    def test_r0_38deg_stays_far_below_threshold(self):
        r = scan_modulation(
            DistributedConfig(
                route="R0", aperture_half_width_deg=38, feedback_beta=0.4
            )
        )
        self.assertLess(r.rho_bridge, 0.01)

    def test_r3_phase_shift_moves_aperture_optimum(self):
        r10 = scan_modulation(
            DistributedConfig(
                route="R3", aperture_half_width_deg=10, feedback_beta=0.4
            )
        )
        r15 = scan_modulation(
            DistributedConfig(
                route="R3", aperture_half_width_deg=15, feedback_beta=0.4
            )
        )
        self.assertLess(r10.rho_bridge, 1.0)
        self.assertGreater(r15.rho_bridge, 1.0)

    def test_sweep_contains_all_route_width_pairs(self):
        rows = sweep(
            DistributedConfig(samples_per_sector=20),
            half_widths_deg=(10, 38),
        )
        self.assertEqual(len(rows), 8)


if __name__ == "__main__":
    unittest.main()
