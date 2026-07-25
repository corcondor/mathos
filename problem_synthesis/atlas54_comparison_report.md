# Atlas54 vs Self-authored54

Date: 2026-07-23

## Experimental Contract

The system corpus is generated from typed synthesis charts, not from stored
problem statements. A generated candidate is exported only when both conditions
hold:

1. the chart backend computes and independently verifies an exact answer;
2. the rendered Japanese TeX is processed by the normal semantic pipeline and
   produces the chart's required admissible `LiftCertificate`.

Blind pairing uses `lift:<family_id>`. Surface domain labels and problem numbers
are not pairing keys.

## Generation Result

- Evaluated system candidates: 54
- Backend and lift verified: 54
- Rejected: 0
- Synthesis charts: 12
- Lift families: 8
- Unique answer normal forms: 48

| Lift family | System count |
| --- | ---: |
| `measure_geometry.planar_area` | 12 |
| `optimization.planar_area_extremum` | 8 |
| `optimization.scalar_minimum` | 4 |
| `real_analysis.limit_observable` | 10 |
| `real_analysis.planar_measure_limit` | 4 |
| `real_analysis.correlation_limit` | 2 |
| `measure_geometry.solid_volume` | 6 |
| `elementary_number_theory.prime_constraint_query` | 8 |

Backend evidence includes exact one-, two-, or three-dimensional integration,
stationary and boundary checks, nonnegative polynomial identities, symbolic
limits, moment identities, and exhaustive bounded prime enumeration.

## CreativeBench Result

| Measurement | Human | MathOS |
| --- | ---: | ---: |
| Records | 54 | 54 |
| Machine-adjudicated valid | not adjudicated | 54 |
| Certified structures | 34 | 54 |
| Unique certified structural signatures | 30 | 12 |
| Mean statement characters | 177.5 | 58.389 |

- Shared Lift families: 8
- Structurally eligible blind pairs: 31
- Human records without a pair: 23
- System records without a pair: 23
- System-only Lift families: 0

Of the 23 unmatched human records, 20 are deliberately unlifted. The other
three belong to certified families not generated in this experiment:
`elementary_number_theory.prime_power_symmetric_primality` and
`measure_geometry.locus_area`.

## What Is Established

- The previous zero-pair generator coverage failure is removed for eight
  abstract families.
- Every system item carries executable backend evidence and an independently
  reproduced LiftCertificate.
- A 31-pair, source-hidden evaluation set now exists.
- The system set is much less structurally diverse than the human set
  (12 versus 30 certified signatures), despite having the same record count.

## What Is Not Established

- No human problem is yet marked valid or invalid because the answer section was
  excluded from the import.
- No elegance, surprise, naturalness, or pedagogical claim is valid before blind
  ratings are collected.
- The 31 pairs measure within-family comparison, not general mathematical
  creativity or high-school-mathematics coverage.
- Parameter variation inside one chart is not counted as a new abstract method.

## Next Falsifiable Steps

1. Collect blind ratings for the 31 public pairs without exposing the private key.
2. Import or independently verify the human solutions in a separate answer
   channel, preserving problem/answer separation.
3. Add `locus_area` and a non-problem-specific symmetric-primality chart.
4. Increase system structural signatures through new backend contracts, not by
   paraphrasing or changing constants.
5. Test whether chart-generated curriculum improves solver performance on a
   frozen held-out set from the same Lift families.

Artifacts:

- `atlas_verified54.json`
- `atlas_verified54.md`
- `all_problems_selfauthored54_lift_match1.jsonl`
- `all_problems_selfauthored54_lift_match1_report.json`
- `creative_benchmark_atlas54_vs_selfauthored54.json`
- `creative_benchmark_atlas54_vs_selfauthored54.md`
- `creative_benchmark_atlas54_vs_selfauthored54_blind_pairs.json`
