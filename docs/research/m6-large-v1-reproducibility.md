# M6 Large V1 — CAD and package reproducibility

## Source owner

`cad/generate_m6_large_v1.py` owns the declared M6 V1 generated part and complete-assembly family.

## Deterministic STEP handling

OpenCascade writes a current export timestamp into the STEP `FILE_NAME` header. `scripts/normalize_m6_step.py` rewrites only that volatile timestamp to:

`2000-01-01T00:00:00`

The STEP DATA geometry is not altered by this normalization.

## Rebuild

```bash
python -m pip install -r requirements-cad.txt
python cad/generate_m6_large_v1.py
python scripts/normalize_m6_step.py
python scripts/check_m6_assets.py
python scripts/build_m6_package.py
```

## Required complete models

- `Testatika_M6_LARGE_V1_BEST_EVIDENCE.step/.stl`
- `Testatika_M6_LARGE_V1_SAFE_LAB_GUARDED.step/.stl`
- `Testatika_M6_LARGE_V1_SERVICE_EXPLODED.step/.stl`

## Integrity expectations

The checker verifies at minimum:

- presence of all declared STEP/STL assets;
- fixed STEP timestamp;
- 500 mm disc diameter within tolerance;
- complete-model envelope plausibility;
- model metadata with 50-lamella, 8-front/6-rear and 3-grid constraints;
- guarded model larger than the unguarded model;
- package SHA-256.

## Historical reproducibility boundary

Byte-reproducible CAD does not make the historical unknowns disappear. The model is reproducible as a **declared research configuration**, not proven identical to every historical M6 machine.
