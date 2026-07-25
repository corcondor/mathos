# Corpus Lift Protocol

## Scope

Public/TeX corpora usually lack gold LiftCertificate labels, so this reports coverage, backend success, wrong answers, and rejection. The full seven-axis match is measured on generated same-structure families.

## Counts

- total: 1000
- lifted: 51
- backend_executed: 49
- comparable: 960
- correct: 47
- wrong: 0
- rejected: 949
- errors: 0

## Rates

| metric | value |
|---|---:|
| `lift_rate` | 0.051 |
| `backend_execution_rate` | 0.049 |
| `backend_success_rate` | 0.049 |
| `precision_answered` | 0.959 |
| `wrong_rate_answered` | 0.000 |
| `rejection_rate` | 0.949 |
| `error_rate` | 0.000 |

## Source Summary

| source | total | lifted | backend | correct | wrong | lift rate | wrong/answered |
|---|---:|---:|---:|---:|---:|---:|---:|
| AQuA-RAT | 60 | 0 | 0 | 0 | 0 | 0.000 | 0.000 |
| ASDiv | 150 | 4 | 4 | 4 | 0 | 0.027 | 0.000 |
| GSM8K | 200 | 1 | 1 | 1 | 0 | 0.005 | 0.000 |
| MATH | 140 | 12 | 10 | 8 | 0 | 0.086 | 0.000 |
| MAWPS | 150 | 17 | 17 | 17 | 0 | 0.113 | 0.000 |
| MultiArith | 150 | 12 | 12 | 12 | 0 | 0.080 | 0.000 |
| SVAMP | 150 | 5 | 5 | 5 | 0 | 0.033 | 0.000 |

## Family Summary

| family | total | backend | correct | wrong |
|---|---:|---:|---:|---:|
| `<none>` | 949 | 0 | 0 | 0 |
| `affine_geometry.midpoint_observable` | 1 | 1 | 1 | 0 |
| `circle_group.clock_angle` | 1 | 1 | 1 | 0 |
| `discrete_affine_sequence.nth_term` | 1 | 1 | 1 | 0 |
| `inner_product_geometry.distance` | 2 | 1 | 1 | 0 |
| `ordered_field.absolute_value_equation` | 1 | 1 | 0 | 0 |
| `ordered_field.compound_growth_rate` | 1 | 1 | 1 | 0 |
| `ordered_field.scalar_percent_action` | 1 | 1 | 1 | 0 |
| `polynomial_notation.base_expansion` | 2 | 2 | 2 | 0 |
| `probability.complement_event` | 2 | 1 | 0 | 0 |
| `state_event.additive_quantity` | 39 | 39 | 39 | 0 |

## Files

- json: `math_os_prototype\corpus_lift_public_1000_state_event_v6.json`
- jsonl: `math_os_prototype\corpus_lift_public_1000_state_event_v6.jsonl`
