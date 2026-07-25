# LiftCertificate Lifter Experiment

## Objective

learn problem_text -> LiftCertificate, not problem_text -> answer

## Counts

- total: 288
- train/dev: 162
- calib: 54
- held_out: 72

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

- same-structure pairs: 192/192
- negative pair confusion: 0/240

## Files

- json: `math_os_prototype\lift_lifter_experiment_16seeds.json`
- jsonl: `math_os_prototype\lift_lifter_experiment_16seeds.jsonl`
- report: `math_os_prototype\lift_lifter_experiment_16seeds_report.md`
