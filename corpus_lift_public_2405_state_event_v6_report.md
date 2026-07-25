# Corpus Lift Protocol

## Scope

Public/TeX corpora usually lack gold LiftCertificate labels, so this reports coverage, backend success, wrong answers, and rejection. The full seven-axis match is measured on generated same-structure families.

## Counts

- total: 2405
- lifted: 107
- backend_executed: 101
- comparable: 2307
- correct: 98
- wrong: 0
- rejected: 2298
- errors: 0

## Rates

| metric | value |
|---|---:|
| `lift_rate` | 0.044 |
| `backend_execution_rate` | 0.042 |
| `backend_success_rate` | 0.042 |
| `precision_answered` | 0.970 |
| `wrong_rate_answered` | 0.000 |
| `rejection_rate` | 0.956 |
| `error_rate` | 0.000 |

## Source Summary

| source | total | lifted | backend | correct | wrong | lift rate | wrong/answered |
|---|---:|---:|---:|---:|---:|---:|---:|
| AQuA-RAT | 254 | 2 | 0 | 0 | 0 | 0.008 | 0.000 |
| ASDiv | 301 | 8 | 8 | 8 | 0 | 0.027 | 0.000 |
| GSM8K | 500 | 3 | 3 | 3 | 0 | 0.006 | 0.000 |
| MATH | 350 | 16 | 12 | 9 | 0 | 0.046 | 0.000 |
| MAWPS | 520 | 58 | 58 | 58 | 0 | 0.112 | 0.000 |
| MultiArith | 180 | 14 | 14 | 14 | 0 | 0.078 | 0.000 |
| SVAMP | 300 | 6 | 6 | 6 | 0 | 0.020 | 0.000 |

## Family Summary

| family | total | backend | correct | wrong |
|---|---:|---:|---:|---:|
| `<none>` | 2298 | 0 | 0 | 0 |
| `affine_geometry.midpoint_observable` | 2 | 2 | 2 | 0 |
| `circle_group.clock_angle` | 1 | 1 | 1 | 0 |
| `discrete_affine_sequence.nth_term` | 1 | 1 | 1 | 0 |
| `inner_product_geometry.distance` | 2 | 1 | 1 | 0 |
| `ordered_field.absolute_value_equation` | 1 | 1 | 0 | 0 |
| `ordered_field.compound_growth_rate` | 2 | 1 | 1 | 0 |
| `ordered_field.scalar_percent_action` | 1 | 1 | 1 | 0 |
| `polynomial_notation.base_expansion` | 2 | 2 | 2 | 0 |
| `probability.complement_event` | 5 | 1 | 0 | 0 |
| `real_closed_field.quadratic_root_observable` | 1 | 1 | 0 | 0 |
| `state_event.additive_quantity` | 89 | 89 | 89 | 0 |

## Files

- json: `math_os_prototype\corpus_lift_public_2405_state_event_v6.json`
- jsonl: `math_os_prototype\corpus_lift_public_2405_state_event_v6.jsonl`
