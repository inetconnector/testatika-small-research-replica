#!/usr/bin/env python3
from pathlib import Path
import json
import trimesh

ROOT = Path(__file__).resolve().parents[1]
FIXED = "2000-01-01T00:00:00"
KITS = {
    "m2-v5": ("FABRICATION_MANIFEST_M2_V5.json", "Testatika_M2_V5_FABRICATION_ASSEMBLY_REFERENCE_NOT_FOR_PRINT", ["shaft_alignment_jig_m2_v5", "pot_bottom_carrier_m2_v5", "crystal_module_tray_m2_v5"]),
    "m6-v2": ("FABRICATION_MANIFEST_M6_V2.json", "Testatika_M6_V2_FABRICATION_ASSEMBLY_REFERENCE_NOT_FOR_PRINT", ["lamella_pitch_jig_10position_m6_v2", "grid_centering_spider_m6_v2", "capacitor_mount_78mm_m6_v2"]),
}
# Match real functional parts specifically. Do not use broad tokens such as "shaft_":
# legitimate printable tooling includes names such as shaft_alignment_jig_m2_v5.
PROHIBITED_PRINT_TOKENS = (
    "bearing_tower",
    "bearing_retainer",
    "capacitor_can",
    "inner_shaft_",
    "outer_hollow_shaft_",
    "shaft_8mm_x",
    "rotor_disc_",
    "stator_perforated",
    "lamella_chrome",
)


def require(path: Path, size=80):
    if not path.is_file() or path.stat().st_size < size:
        raise SystemExit(f"missing or small build-kit asset: {path.relative_to(ROOT)}")


def check_step(path: Path):
    if FIXED not in path.read_text(encoding="utf-8", errors="strict")[:1400]:
        raise SystemExit(f"unnormalized STEP: {path.relative_to(ROOT)}")


def check_mesh(path: Path):
    mesh = trimesh.load_mesh(path, force="mesh")
    if len(mesh.vertices) < 3 or len(mesh.faces) < 1:
        raise SystemExit(f"invalid STL: {path.relative_to(ROOT)}")


def main():
    for kit, (manifest_name, assembly_name, required_print) in KITS.items():
        base = ROOT / "hardware" / "build-kits" / kit
        print_dir = base / "print"; fab_dir = base / "fabricate"; assy_dir = base / "assembly-reference"; meta_dir = base / "metadata"
        for directory in (print_dir, fab_dir, assy_dir, meta_dir):
            if not directory.is_dir():
                raise SystemExit(f"missing directory: {directory.relative_to(ROOT)}")
        print_stls = list(print_dir.glob("*.stl"))
        if len(print_stls) < 8:
            raise SystemExit(f"too few printable support parts in {kit}: {len(print_stls)}")
        for stl in print_stls:
            low = stl.stem.lower()
            if any(token in low for token in PROHIBITED_PRINT_TOKENS):
                raise SystemExit(f"real-material part found in print folder: {stl.relative_to(ROOT)}")
            check_mesh(stl); step = stl.with_suffix(".step"); require(step); check_step(step)
        for name in required_print:
            require(print_dir / f"{name}.stl"); require(print_dir / f"{name}.step")
        fabricated = list(fab_dir.glob("*.step"))
        if len(fabricated) < 10:
            raise SystemExit(f"too few real-material fabrication parts in {kit}: {len(fabricated)}")
        for step in fabricated:
            require(step); check_step(step)
        if list(fab_dir.glob("*.stl")):
            raise SystemExit("fabricate folder must not contain printable STL substitutes")
        assy_stl = assy_dir / f"{assembly_name}.stl"; assy_step = assy_dir / f"{assembly_name}.step"
        require(assy_stl, 1000); require(assy_step, 1000); check_mesh(assy_stl); check_step(assy_step)
        manifest_path = meta_dir / manifest_name; require(manifest_path)
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
        text = json.dumps(data).upper()
        for required in ("METAL", "PMMA", "PRINTABLE_SUPPORT"):
            if required not in text:
                raise SystemExit(f"{kit} manifest lacks {required} classification")
        if kit == "m2-v5":
            anchors = data["direct_or_preferred_anchors"]
            if anchors["rotor_diameter_mm"] != 200.0 or anchors["nominal_sector_count"] != 24:
                raise SystemExit("M2 source anchors changed")
        else:
            anchors = data["direct_anchor_mm"]
            if anchors["disc_diameter"] != 500.0 or anchors["lamella_count"] != 50:
                raise SystemExit("M6 source anchors changed")
    print("M2 V5 and M6 V2 fabrication-kit validation passed.")

if __name__ == "__main__":
    main()
