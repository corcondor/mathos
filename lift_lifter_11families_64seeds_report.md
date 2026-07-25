# LiftCertificate Lifter Experiment

## Objective

learn problem_text -> LiftCertificate, not problem_text -> answer

## Counts

- total: 2112
- train/dev: 1254
- calib: 429
- held_out: 429

## Seven-Axis Held-Out Summary

| axis | score |
|---|---:|
| `1_family_id` | 1.000 |
| `2_morphism_chain` | 1.000 |
| `3_constraint_skeleton` | 1.000 |
| `4_query_signature` | 1.000 |
| `5_backend_execution_success` | 1.000 |
| `6_surface_numeric_same_structure` | 1.000 |
| `7_negative_structure_not_confused` | 1.000 |
| `overall_backend_success` | 1.000 |

## Split Summary

| split | family | morphism | constraint | query | backend contract | backend success | wrong | rejected |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| calib | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 |
| dev | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 |
| held_out | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 |

## Pair Tests

- same-structure pairs: 1408/1408
- negative pair confusion: 0/1920

## Files

- json: `math_os_prototype\lift_lifter_11families_64seeds.json`
- jsonl: `math_os_prototype\lift_lifter_11families_64seeds.jsonl`
- report: `math_os_prototype\lift_lifter_11families_64seeds_report.md`
