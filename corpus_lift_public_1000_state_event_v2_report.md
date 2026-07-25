# Corpus Lift Protocol

## Scope

Public/TeX corpora usually lack gold LiftCertificate labels, so this reports coverage, backend success, wrong answers, and rejection. The full seven-axis match is measured on generated same-structure families.

## Counts

- total: 1000
- lifted: 61
- backend_executed: 59
- comparable: 960
- correct: 41
- wrong: 16
- rejected: 939
- errors: 0

## Rates

| metric | value |
|---|---:|
| `lift_rate` | 0.061 |
| `backend_execution_rate` | 0.059 |
| `backend_success_rate` | 0.043 |
| `precision_answered` | 0.695 |
| `wrong_rate_answered` | 0.271 |
| `rejection_rate` | 0.939 |
| `error_rate` | 0.000 |

## Source Summary

| source | total | lifted | backend | correct | wrong | lift rate | wrong/answered |
|---|---:|---:|---:|---:|---:|---:|---:|
| AQuA-RAT | 60 | 0 | 0 | 0 | 0 | 0.000 | 0.000 |
| ASDiv | 150 | 4 | 4 | 2 | 2 | 0.027 | 0.500 |
| GSM8K | 200 | 2 | 2 | 1 | 1 | 0.010 | 0.500 |
| MATH | 140 | 12 | 10 | 8 | 0 | 0.086 | 0.000 |
| MAWPS | 150 | 20 | 20 | 20 | 0 | 0.133 | 0.000 |
| MultiArith | 150 | 16 | 16 | 6 | 10 | 0.107 | 0.625 |
| SVAMP | 150 | 7 | 7 | 4 | 3 | 0.047 | 0.429 |

## Family Summary

| family | total | backend | correct | wrong |
|---|---:|---:|---:|---:|
| `<none>` | 939 | 0 | 0 | 0 |
| `affine_geometry.midpoint_observable` | 1 | 1 | 1 | 0 |
| `circle_group.clock_angle` | 1 | 1 | 1 | 0 |
| `discrete_affine_sequence.nth_term` | 1 | 1 | 1 | 0 |
| `inner_product_geometry.distance` | 2 | 1 | 1 | 0 |
| `ordered_field.absolute_value_equation` | 1 | 1 | 0 | 0 |
| `ordered_field.compound_growth_rate` | 1 | 1 | 1 | 0 |
| `ordered_field.scalar_percent_action` | 1 | 1 | 1 | 0 |
| `polynomial_notation.base_expansion` | 2 | 2 | 2 | 0 |
| `probability.complement_event` | 2 | 1 | 0 | 0 |
| `state_event.additive_quantity` | 49 | 49 | 33 | 16 |

## Files

- json: `math_os_prototype\corpus_lift_public_1000_state_event_v2.json`
- jsonl: `math_os_prototype\corpus_lift_public_1000_state_event_v2.jsonl`
