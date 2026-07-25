# Self-authored 54-Problem PDCA Snapshot

Date: 2026-07-22

## Scope

- Source: `C:\Users\81808\OneDrive - 東京理科大学\全問題.tex`
- Rights basis: `self_authored`
- Source SHA-256: `8f9d07f2b9bfd73c5afaccc1d8479a7eb6cf3ff7585b54cea16f8d20fdd14627`
- Extracted problem blocks before the answer section: 81
- Frozen evaluation sample: 54
- Answer section imported: no
- Selection rule after the first import: fixed record IDs

Stable IDs use the source ID, source ordinal, and statement hash. Duplicate display
labels therefore remain distinct. The source contains duplicate labels for problems
49, 61, 65, and 66.

## PDCA Result

| Measurement | Baseline | Current |
| --- | ---: | ---: |
| Frozen human records | 54 | 54 |
| Semantic compilation failures | 0 | 0 |
| Certified LiftCertificates | 1 | 34 |
| Unlifted records | 53 | 20 |
| Type-checked semantic graphs | not recorded | 52 |
| Semantic graphs needing review | not recorded | 2 |

The change from 1 to 34 certificates came from typed query objects and reusable
atlas morphisms for area, volume, limit, correlation, primality, and extrema. No
problem ID, display number, numeric answer, or full problem statement is used as a
dispatch key.

Current certified-family counts in the frozen sample:

| Certificate family | Count |
| --- | ---: |
| elementary_number_theory.prime_constraint_query | 9 |
| real_analysis.limit_observable | 6 |
| measure_geometry.planar_area | 5 |
| optimization.planar_area_extremum | 4 |
| real_analysis.planar_measure_limit | 4 |
| real_analysis.correlation_limit | 2 |
| elementary_number_theory.prime_power_symmetric_primality | 1 |
| measure_geometry.locus_area | 1 |
| measure_geometry.solid_volume | 1 |
| optimization.scalar_minimum | 1 |

## Remaining Lift Failures

The 20 rejected records are concentrated in proof goals and structures whose
domain objects are still underspecified:

| Rejected match group | Count |
| --- | ---: |
| algebra:prove:Proof | 3 |
| inequalities:prove:Proof | 3 |
| geometry:2d:existence_prop | 2 |
| geometry:3d:solid_volume | 2 |
| real_analysis:sequence:classify_and_plan | 2 |
| other singleton groups | 8 |

These records remain rejected rather than being forced into a nearby family.

## CreativeBench Result

- Human records: 54/54
- System records: 37/54
- Human certified structures: 34/54, with 30 unique certified signatures
- System certified structures: 37/37, with 3 unique certified signatures
- Shared match groups: 0
- Structurally eligible blind pairs: 0
- Human validity labels: 54 unknown, because solutions were deliberately excluded

The current generator only emits `geometry:2d:curve` and
`geometry:2d:region`. The human corpus requests area, volume, limits, proof,
existence, optimization, probability, and number-theoretic solution sets. Therefore
no claim comparing human and MathOS creativity is valid yet. The zero-pair result is
a measured generator-coverage failure, not evidence for or against creativity.

## Next Experiment

Add synthesis charts for the already certified human output types, beginning with
planar area, scalar/area extrema, limits, solid volume, and prime constraints. Each
generated problem must carry the same LiftCertificate and backend-verification
contract. Freeze a new system set only after it reaches 54 verified records, then
form blind pairs strictly within shared match groups and collect human ratings.

Artifacts:

- `all_problems_selfauthored54_lift_vocab1.jsonl`
- `all_problems_selfauthored54_lift_vocab1_report.json`
- `creative_benchmark_selfauthored54_lift_vocab1.json`
- `creative_benchmark_selfauthored54_lift_vocab1.md`
- `creative_benchmark_selfauthored54_lift_vocab1_blind_pairs.json`
