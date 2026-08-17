# M6 Large replication status

## Meaning of “complete” for M6 Large V1

M6 Large V1 is **complete as a documented, manufacturable, reversible research assembly**, not complete as a recovered historical circuit.

| Subsystem | Physical geometry | Historical electrical topology | V1 status |
|---|---|---|---|
| Base/frame | high working confidence | n/a | BUILD-READY |
| Front/rear 500 mm discs | strong direct anchor | rotor electrical role only partly known | BUILD-READY |
| 50 sheet lamellae | strong direct anchor | exact charge/network state unknown | BUILD-READY / terminal-neutral |
| 8 front + 6 rear stators | direct count/non-contact evidence | grouping/polarity unknown | BUILD-READY / individually terminated |
| Two large cylinders | strong external + internal source support | grid/winding interconnection unknown | BUILD-READY / all layers broken out |
| Three grids per cylinder | direct 1988 source | exact node map unknown | BUILD-READY / open baseline |
| Acrylic separators | direct source | dielectric details incomplete | BUILD-READY |
| Central magnet tube | direct-source geometry | magnetic/electrical function unknown | REVERSIBLE |
| Bifilar winding | direct-source two-layer/18-gauge clue | turns/pitch/connections unknown | BUILD-READY working fit |
| Horseshoe modules | direct large-machine evidence | winding topology/function unknown | BUILD-READY / separate terminals |
| Capacitor positions | visible/drawing-supported | exact C/dielectric/connections unknown | MODULAR |
| Pipe/spiral | drawing-supported | function unknown | MODULAR |
| Top crystal/rectifier assembly | strong geometry precedent | crystal material, polarity, I-V unknown | BLACKBOX / empty baseline |
| Motor/magnet wheel | source-supported large-machine configuration | exact transmission/control unknown | GEOMETRY CANDIDATE |
| Counterrotation lab drive | engineering-derived | not historical | READY FOR MECHANICAL TEST |
| Safety guard | engineering-derived | not historical | REQUIRED FOR POWERED TEST |
| Complete hidden wiring | not recovered | unknown | **OPEN** |
| Historical startup/priming | not recovered | unknown | **OPEN** |
| Claimed net energy source | not established | unknown | **NOT PROVEN** |

## Current complete deliverables

- complete unguarded STL/STEP;
- complete guarded laboratory STL/STEP;
- service/exploded STL/STEP;
- individual part STL/STEP family;
- detailed BOM;
- assembly procedure;
- terminal/node map;
- machine-readable configuration registry;
- staged experiment sequence;
- deterministic build ZIP + SHA-256;
- source map tying each major subsystem to evidence/status.

## Next evidence that could materially improve historical fidelity

1. higher-resolution scan of Hauser drawing 3279 and its notes;
2. calibrated dimensions from an original ~500 mm machine;
3. rear/side images resolving exact stator angles and gaps;
4. direct source for cylinder grid-to-winding node connections;
5. direct source for the top crystal material/terminal map;
6. direct source for the motor/magnet-wheel transmission;
7. contemporaneous schematic with provenance.


## Internet-audit variant boundary — 2026-08-17

The public-source crawl found additional primary-author large-machine evidence, but it does **not** justify silently modifying the existing Hauser-anchored M6a V1 CAD.

Newly separated evidence:

- Marinov TWT-VII: thick electrically connected grid sectors on both faces of one wheel versus thin sectors only on the external face of the other, plus insulating spray on slightly magnetized sectors; exact medium/large object unresolved.
- `M6c`: Marinov's 1989 large-under-construction / approximately 2:1-medium-copy line, including a simpler open cylindrical outer-electrode + thick-Cu-inner-coil capacitor interpretation and ~30-cm horseshoe-magnet scale. This conflicts with M6a enough to remain a separate family.
- `M8` / `M9`: approximately 1-m / 2-m large-scale machines under construction/workshop discussion.
- `M10`: tandem/double-converter workshop family.

**M6a V1 therefore remains frozen as the Hauser-1986/1988 best-evidence build.** A future M6c/M8/M9/M10 CAD package must be source-separated rather than averaged into M6a.

## Additional large-family source separation from March 1984 and Kelly/Bailey 1991

- `M5` (Schneider/Weber, 13-Mar-1984) and `M5a` (L. L. Rorschach report dated 17-Mar-1984) are separate documentary IDs because source independence and exact object identity are unresolved. Both describe ~1.1-m-wide apparatuses and therefore are not silently folded into Hauser's later ~500-mm-disc M6a reconstruction.
- Kelly/Bailey 1991 is not a direct-observer source. Their disc-size/pickup/component descriptions are explicitly based on available reports/photos/video and contain conjecture. They cannot override Hauser direct-visit scans.
- The M6a V1 CAD remains unchanged by this addendum.

## Internet crawl round 2 — M6 provenance guard

Round 2 strengthens source separation rather than changing the M6a CAD baseline:

- Kelly's 1998 self-correction explicitly downgrades an early Kelly-derived horseshoe-magnet-near-disc depiction. It must not be used as an M6a geometry authority.
- Hauser's direct 1986/1988 source line remains the construction anchor for M6a.
- The L. L./Nieper 17-Mar-1984 machine is retained as M5a because it may be the same object/source family as Schneider/Weber M5 and is not proven to be Hauser M6a.
- Kelly/SEA prototype construction reported in 1998 is replication-history evidence only; a successful result has not been recovered.
- No new source closes the three-grid-cylinder node map, top-crystal electrical function, original speed-control transmission or hidden historical buses.

No M6 V1 STEP/STL geometry is silently altered by these provenance findings.
