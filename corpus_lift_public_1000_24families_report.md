# Corpus Lift Protocol

## Scope

Public/TeX corpora usually lack gold LiftCertificate labels, so this reports coverage, backend success, wrong answers, and rejection. The full seven-axis match is measured on generated same-structure families.

## Counts

- total: 1000
- lifted: 25
- backend_executed: 17
- comparable: 960
- correct: 5
- wrong: 10
- rejected: 975
- errors: 0

## Rates

| metric | value |
|---|---:|
| `lift_rate` | 0.025 |
| `backend_execution_rate` | 0.017 |
| `backend_success_rate` | 0.005 |
| `precision_answered` | 0.294 |
| `wrong_rate_answered` | 0.588 |
| `rejection_rate` | 0.975 |
| `error_rate` | 0.000 |

## Source Summary

| source | total | lifted | backend | correct | wrong | lift rate | wrong/answered |
|---|---:|---:|---:|---:|---:|---:|---:|
| AQuA-RAT | 60 | 1 | 1 | 0 | 1 | 0.017 | 1.000 |
| ASDiv | 150 | 0 | 0 | 0 | 0 | 0.000 | 0.000 |
| GSM8K | 200 | 2 | 2 | 0 | 2 | 0.010 | 1.000 |
| MATH | 140 | 20 | 12 | 5 | 5 | 0.143 | 0.417 |
| MAWPS | 150 | 0 | 0 | 0 | 0 | 0.000 | 0.000 |
| MultiArith | 150 | 2 | 2 | 0 | 2 | 0.013 | 1.000 |
| SVAMP | 150 | 0 | 0 | 0 | 0 | 0.000 | 0.000 |

## Family Summary

| family | total | backend | correct | wrong |
|---|---:|---:|---:|---:|
| `<none>` | 975 | 0 | 0 | 0 |
| `affine_geometry.midpoint_observable` | 1 | 1 | 1 | 0 |
| `circle_group.clock_angle` | 1 | 1 | 1 | 0 |
| `discrete_affine_sequence.nth_term` | 1 | 0 | 0 | 0 |
| `inner_product_geometry.distance` | 2 | 1 | 1 | 0 |
| `ordered_field.absolute_value_equation` | 1 | 1 | 0 | 0 |
| `ordered_field.compound_growth_rate` | 1 | 1 | 1 | 0 |
| `ordered_field.scalar_percent_action` | 14 | 12 | 1 | 10 |
| `polynomial_notation.base_expansion` | 2 | 0 | 0 | 0 |
| `probability.complement_event` | 2 | 0 | 0 | 0 |

## Files

- json: `math_os_prototype\corpus_lift_public_1000_24families.json`
- jsonl: `math_os_prototype\corpus_lift_public_1000_24families.jsonl`
