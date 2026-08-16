#!/usr/bin/env python3
"""Verify the materialized M6 Large V1 CAD/build family."""
from __future__ import annotations
import json
from pathlib import Path
import trimesh

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "hardware" / "experimental" / "m6-large-v1-best-evidence"
FIXED = "2000-01-01T00:00:00"
PARTS = [
    "base_platform_m6_v1",
    "front_disc_500mm_50lamella_m6_v1",
    "rear_disc_500mm_50lamella_both_sides_m6_v1",
    "shaft_nested_counterrotation_m6_v1",
    "bearing_pedestal_m6_v1",
    "stationary_electrode_perforated_m6_v1",
    "stationary_electrode_sets_8front_6rear_m6_v1",
    "large_cylinder_complete_3grid_bifilar_m6_v1",
    "large_cylinder_cutaway_3grid_bifilar_m6_v1",
    "large_cylinder_grid_outer_m6_v1",
    "large_cylinder_grid_middle_m6_v1",
    "large_cylinder_grid_inner_m6_v1",
    "large_cylinder_acrylic_outer_m6_v1",
    "large_cylinder_acrylic_inner_m6_v1",
    "large_cylinder_magnet_tube_m6_v1",
    "large_cylinder_bifilar_winding_m6_v1",
    "horseshoe_wound_module_m6_v1",
    "capacitor_big_m6_v1",
    "capacitor_small_m6_v1",
    "spiral_pipe_m6_v1",
    "top_crystal_rectifier_blackbox_m6_v1",
    "magnet_timing_wheel_m6_v1",
    "drive_regulator_module_m6_v1",
    "terminal_board_3isolated_open_m6_v1",
    "lab_counterrotation_drive_m6_v1",
    "adjustable_lab_motor_mount_m6_v1",
    "lab_drive_pulley_m6_v1",
    "lab_guard_frame_m6_v1",
]
COMPLETE = [
    "Testatika_M6_LARGE_V1_BEST_EVIDENCE",
    "Testatika_M6_LARGE_V1_SAFE_LAB_GUARDED",
    "Testatika_M6_LARGE_V1_SERVICE_EXPLODED",
]


def require(p: Path, size=128):
    if not p.is_file() or p.stat().st_size < size:
        raise SystemExit(f"missing/small M6 asset: {p.relative_to(ROOT)}")


def verify_step(p: Path):
    text=p.read_text(encoding="utf-8", errors="strict")
    if FIXED not in text[:1200]:
        raise SystemExit(f"M6 STEP timestamp not normalized: {p.relative_to(ROOT)}")


def mesh_extents(p: Path):
    m=trimesh.load_mesh(p, force="mesh")
    if len(m.vertices)<3 or len(m.faces)<1:
        raise SystemExit(f"invalid mesh: {p.relative_to(ROOT)}")
    return [float(x) for x in m.extents]


def main():
    for name in PARTS:
        sp=BASE/"stl"/f"{name}.stl"; tp=BASE/"step"/f"{name}.step"
        require(sp); require(tp); verify_step(tp)
    for name in COMPLETE:
        sp=BASE/"complete-model"/f"{name}.stl"; tp=BASE/"complete-model"/f"{name}.step"
        require(sp,1000); require(tp,1000); verify_step(tp)

    meta=BASE/"metadata"/"MODEL_INFO_M6_V1.json"; require(meta)
    data=json.loads(meta.read_text(encoding="utf-8"))
    d=data["direct_anchor_mm"]
    if d["disc_diameter"] != 500.0 or d["lamella_count"] != 50:
        raise SystemExit("M6 metadata lost 500-mm / 50-lamella anchor")
    features=" ".join(data["observed_or_source_supported_features"]).lower()
    for phrase in ("8 front / 6 rear", "three concentric metal grids", "bifilar"):
        if phrase not in features:
            raise SystemExit(f"M6 metadata missing source constraint: {phrase}")

    # The STEP circle is exactly 500 mm. STL chord tessellation can undershoot the
    # axis-aligned mesh extent slightly depending on angular phase/tolerance.
    front=mesh_extents(BASE/"stl"/"front_disc_500mm_50lamella_m6_v1.stl")
    largest=sorted(front)[-2:]
    if not all(498.0 <= x <= 501.5 for x in largest):
        raise SystemExit(f"front disc tessellated diameter out of tolerance: {front}")

    complete=mesh_extents(BASE/"complete-model"/"Testatika_M6_LARGE_V1_BEST_EVIDENCE.stl")
    guarded=mesh_extents(BASE/"complete-model"/"Testatika_M6_LARGE_V1_SAFE_LAB_GUARDED.stl")
    if not (740 <= complete[0] <= 790 and 620 <= complete[2] <= 660):
        raise SystemExit(f"unexpected M6 complete envelope: {complete}")
    if guarded[2] < complete[2] or guarded[1] < complete[1]:
        raise SystemExit(f"guarded model should not be smaller: complete={complete}, guarded={guarded}")

    print("M6 Large V1 asset verification passed.")
    print("Front disc tessellated bbox:", front)
    print("Complete bbox:", complete)
    print("Guarded bbox:", guarded)

if __name__ == "__main__":
    main()
