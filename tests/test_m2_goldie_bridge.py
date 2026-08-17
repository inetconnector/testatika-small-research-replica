import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "sim"))

from m2_regenerative_grid_model import ModelConfig, M2Network
from m2_goldie_bridge import (
    all_undirected_pairs,
    passive_goldie_available,
    scan_config,
    scan_pair,
    strongest_modulation,
)


class M2GoldieBridgeTests(unittest.TestCase):
    def test_all_six_stationary_pairs_are_scanned(self):
        self.assertEqual(len(list(all_undirected_pairs())), 6)

    def test_effective_capacitance_is_positive_and_modulated(self):
        net = M2Network(ModelConfig(steps_per_rev=48, revolutions=1, grid_mode="mesh"))
        row = scan_pair(net, "GRID_L", "GRID_R")
        self.assertGreater(row.c_min_f, 0.0)
        self.assertGreaterEqual(row.c_max_f, row.c_min_f)
        self.assertGreaterEqual(row.ratio, 1.0)

    def test_default_aggregate_model_is_below_passive_goldie_threshold(self):
        rows = scan_config(ModelConfig(
            steps_per_rev=96,
            revolutions=1,
            grid_mode="mesh",
            feedback=False,
        ))
        self.assertFalse(passive_goldie_available(rows))
        self.assertTrue(all(r.beta_critical > 1.0 for r in rows))

    def test_default_modulation_is_small(self):
        rows = scan_config(ModelConfig(
            steps_per_rev=96,
            revolutions=1,
            grid_mode="mesh",
            feedback=False,
        ))
        best = strongest_modulation(rows)
        self.assertLess(best.ratio, 1.01)


if __name__ == "__main__":
    unittest.main()
