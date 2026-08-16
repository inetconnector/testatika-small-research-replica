# Contributing

Contributions are welcome if they improve provenance, geometry, measurement quality, falsifiability or reproducibility.

## Evidence labels

Every technical claim should use the canonical distinction documented in `docs/REPLICATION_STATUS.md` and `docs/research/provenance-schema.yaml`:

- **OBSERVED** — directly visible/measured in an adequately identified source or experiment;
- **SOURCE-STATED** — explicitly stated by a named source;
- **PHOTO-DERIVED** — estimated from imagery and carrying measurement uncertainty;
- **DERIVED** — calculated or logically derived from better-supported evidence;
- **HYPOTHESIS** — plausible/testable but not established;
- **CONFLICT** — relevant sources disagree or likely refer to different machine variants;
- **UNKNOWN** — surviving evidence does not currently determine the value/function.

Do not silently upgrade a hypothesis or photo interpretation to historical fact.

## Machine identity and provenance

1. Assign the relevant machine ID from `docs/research/machines.yaml` whenever possible.
2. Do not transfer a property between machine variants merely because the machines look related.
3. For high-value source claims include page, figure, frame, timecode or correspondence locator whenever available.
4. Record author/speaker separately from host, translator, interviewer or archive mirror.
5. Follow `docs/research/provenance-schema.yaml` for new structured source records.
6. Third-party scans/books/images must not be relicensed or redistributed without rights; stable links/archive IDs and hashes of legally held originals are preferred.

## CAD changes

1. state the evidence for the changed dimension/feature;
2. identify the affected machine and evidence class;
3. update the relevant research document and `docs/REPLICATION_STATUS.md` if M2 completeness changes;
4. regenerate STL/STEP assets only when the generator owns those outputs;
5. preserve binary-only historical assets until their source replacement has been validated;
6. update `docs/research/cad-reproducibility.md` if source coverage changes;
7. run `python scripts/validate_assets.py`;
8. regenerate/check integrity metadata with `python scripts/generate_manifest.py` and `python scripts/check_manifest.py`;
9. update `CHANGELOG.md` for release-relevant changes.

## Experimental reports

Please include:

- exact machine/configuration ID;
- CAD variant and repository commit;
- geometry/materials;
- rotor route and conductor material;
- electrode geometry/gap/angle;
- temperature, humidity and other relevant environment data;
- instruments/calibration;
- all electrical/mechanical/auxiliary input-energy paths;
- initial and final stored-energy states;
- raw data and analysis procedure where possible.

A spark, high open-circuit voltage, rotor coast-down or short lamp test is not by itself an energy-balance measurement.

## Preservation

Do not delete preservation-critical research/CAD merely because a newer interpretation exists. Add a correction/deprecation note and keep the historical state recoverable through Git/snapshots/releases. Pull requests that intentionally remove material must explain the recovery path.

## Commit style

Examples:

- `cad: refine first-machine pot geometry`
- `research: add Marinov source locator`
- `test: add C(theta) measurement dataset`
- `fix: correct rotor wire-routing jig`
- `docs: correct source attribution without deleting prior provenance`
