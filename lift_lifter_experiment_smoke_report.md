# LiftCertificate Lifter Experiment

## Objective

learn problem_text -> LiftCertificate, not problem_text -> answer

## Counts

- total: 36
- train/dev: 18
- calib: 9
- held_out: 9

## Seven-Axis Held-Out Summary

| axis | score |
|---|---:|
| `1_family_id` | 0.000 |
| `2_morphism_chain` | 0.000 |
| `3_constraint_skeleton` | 0.333 |
| `4_query_signature` | 0.000 |
| `5_backend_execution_success` | 0.000 |
| `6_surface_numeric_same_structure` | 0.000 |
| `7_negative_structure_not_confused` | 1.000 |
| `overall_backend_success` | 0.000 |

## Split Summary

| split | family | morphism | constraint | query | backend contract | backend success | wrong | rejected |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| calib | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| dev | 0.000 | 0.000 | 0.167 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| held_out | 0.000 | 0.000 | 0.333 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |

## Pair Tests

- same-structure pairs: 0/24
- negative pair confusion: 0/30

## Files

- json: `math_os_prototype\lift_lifter_experiment_smoke.json`
- jsonl: `math_os_prototype\lift_lifter_experiment_smoke.jsonl`
- report: `math_os_prototype\lift_lifter_experiment_smoke_report.md`
