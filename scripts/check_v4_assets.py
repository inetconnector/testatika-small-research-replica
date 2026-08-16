#!/usr/bin/env python3
"""Verify the materialized V4 best-evidence M2 build family."""
from __future__ import annotations

import json
from pathlib import Path
import struct

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "hardware" / "experimental" / "v4-best-evidence-m2"

PARTS = [
    "rotor_20wire_floating_R0_v4",
    "rotor_24wire_floating_R0_v4",
    "rotor_25wire_floating_R0_v4",
    "rotor_24wire_floating_R4_v4_research",
    "hub_disk_v4",
    "hub_arc_pair_v4_video_refined",
    "pot_outer_shell_v4",
    "pot_grid_former_v4",
    "pot_acrylic_sleeve_jig_v4",
    "pot_spiral_mandrel_v4",
    "pot_terminal_lid_2wire_v4",
    "outer_panel_layered_v4",
    "lower_central_cage_v4",
    "top_crystal_carrier_4pos_v4",
    "horseshoe_magnet_shape_v4",
    "horseshoe_dummy_v4",
    "guard_post_v4",
]
COMPLETE = [
    "Testatika_M2_V4_BEST_EVIDENCE",
    "Testatika_M2_V4_R4_RESEARCH",
]


def require_file(path: Path, min_size=100):
    if not path.is_file():
        raise SystemExit(f"missing V4 asset: {path.relative_to(ROOT)}")
    if path.stat().st_size < min_size:
        raise SystemExit(f"unexpectedly small V4 asset: {path.relative_to(ROOT)}")


def binary_stl_bbox(path: Path):
    data = path.read_bytes()
    if len(data) < 84:
        raise SystemExit(f"invalid STL: {path}")
    count = struct.unpack_from("<I", data, 80)[0]
    expected = 84 + count * 50
    if expected != len(data):
        raise SystemExit(f"STL is not expected binary layout: {path}")
    mins = [float("inf")] * 3
    maxs = [float("-inf")] * 3
    offset = 84
    for _ in range(count):
        # normal at +0; vertices begin at +12
        for vertex in range(3):
            x, y, z = struct.unpack_from("<fff", data, offset + 12 + vertex * 12)
            for i, value in enumerate((x, y, z)):
                mins[i] = min(mins[i], value)
                maxs[i] = max(maxs[i], value)
        offset += 50
    return tuple(maxs[i] - mins[i] for i in range(3))


def main():
    for part in PARTS:
        require_file(BASE / "stl" / f"{part}.stl")
        require_file(BASE / "step" / f"{part}.step")

    for name in COMPLETE:
        require_file(BASE / "complete-model" / f"{name}.stl", 1000)
        require_file(BASE / "complete-model" / f"{name}.step", 1000)

    meta_path = BASE / "metadata" / "MODEL_INFO_V4.json"
    require_file(meta_path)
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    baseline = meta["baseline"]
    assert baseline["nominal_sector_count"] == 24
    assert baseline["sector_electrical_state"].startswith("individually floating")
    assert baseline["pot_external_terminals_each"] == 2
    assert baseline["conventional_drive_motor"].startswith("absent")

    rotor_dims = binary_stl_bbox(BASE / "stl" / "rotor_24wire_floating_R0_v4.stl")
    xy = sorted(rotor_dims[:2])
    if not (199.0 <= xy[0] <= 201.0 and 199.0 <= xy[1] <= 201.0):
        raise SystemExit(f"rotor diameter out of tolerance: {rotor_dims}")
    if not (3.0 <= rotor_dims[2] <= 4.0):
        raise SystemExit(f"rotor thickness out of tolerance: {rotor_dims}")

    lid_dims = binary_stl_bbox(BASE / "stl" / "pot_terminal_lid_2wire_v4.stl")
    if not (83.0 <= lid_dims[0] <= 85.0 and 83.0 <= lid_dims[1] <= 85.0):
        raise SystemExit(f"pot lid OD out of tolerance: {lid_dims}")

    print("V4 materialized asset verification passed.")
    print("Rotor bbox:", rotor_dims)
    print("Pot lid bbox:", lid_dims)


if __name__ == "__main__":
    main()
