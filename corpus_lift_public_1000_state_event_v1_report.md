# Corpus Lift Protocol

## Scope

Public/TeX corpora usually lack gold LiftCertificate labels, so this reports coverage, backend success, wrong answers, and rejection. The full seven-axis match is measured on generated same-structure families.

## Counts

- total: 1000
- lifted: 63
- backend_executed: 61
- comparable: 960
- correct: 15
- wrong: 44
- rejected: 937
- errors: 0

## Rates

| metric | value |
|---|---:|
| `lift_rate` | 0.063 |
| `backend_execution_rate` | 0.061 |
| `backend_success_rate` | 0.016 |
| `precision_answered` | 0.246 |
| `wrong_rate_answered` | 0.721 |
| `rejection_rate` | 0.937 |
| `error_rate` | 0.000 |

## Source Summary

| source | total | lifted | backend | correct | wrong | lift rate | wrong/answered |
|---|---:|---:|---:|---:|---:|---:|---:|
| AQuA-RAT | 60 | 0 | 0 | 0 | 0 | 0.000 | 0.000 |
| ASDiv | 150 | 5 | 5 | 2 | 3 | 0.033 | 0.600 |
| GSM8K | 200 | 2 | 2 | 0 | 2 | 0.010 | 1.000 |
| MATH | 140 | 12 | 10 | 8 | 0 | 0.086 | 0.000 |
| MAWPS | 150 | 26 | 26 | 0 | 26 | 0.173 | 1.000 |
| MultiArith | 150 | 13 | 13 | 4 | 9 | 0.087 | 0.692 |
| SVAMP | 150 | 5 | 5 | 1 | 4 | 0.033 | 0.800 |

## Family Summary

| family | total | backend | correct | wrong |
|---|---:|---:|---:|---:|
| `<none>` | 937 | 0 | 0 | 0 |
| `affine_geometry.midpoint_observable` | 1 | 1 | 1 | 0 |
| `circle_group.clock_angle` | 1 | 1 | 1 | 0 |
| `discrete_affine_sequence.nth_term` | 1 | 1 | 1 | 0 |
| `inner_product_geometry.distance` | 2 | 1 | 1 | 0 |
| `ordered_field.absolute_value_equation` | 1 | 1 | 0 | 0 |
| `ordered_field.compound_growth_rate` | 1 | 1 | 1 | 0 |
| `ordered_field.scalar_percent_action` | 1 | 1 | 1 | 0 |
| `polynomial_notation.base_expansion` | 2 | 2 | 2 | 0 |
| `probability.complement_event` | 2 | 1 | 0 | 0 |
| `state_event.additive_quantity` | 51 | 51 | 7 | 44 |

## Files

- json: `math_os_prototype\corpus_lift_public_1000_state_event_v1.json`
- jsonl: `math_os_prototype\corpus_lift_public_1000_state_event_v1.jsonl`
