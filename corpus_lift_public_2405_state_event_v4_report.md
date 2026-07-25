# Corpus Lift Protocol

## Scope

Public/TeX corpora usually lack gold LiftCertificate labels, so this reports coverage, backend success, wrong answers, and rejection. The full seven-axis match is measured on generated same-structure families.

## Counts

- total: 2405
- lifted: 109
- backend_executed: 103
- comparable: 2307
- correct: 92
- wrong: 8
- rejected: 2296
- errors: 0

## Rates

| metric | value |
|---|---:|
| `lift_rate` | 0.045 |
| `backend_execution_rate` | 0.043 |
| `backend_success_rate` | 0.040 |
| `precision_answered` | 0.893 |
| `wrong_rate_answered` | 0.078 |
| `rejection_rate` | 0.955 |
| `error_rate` | 0.000 |

## Source Summary

| source | total | lifted | backend | correct | wrong | lift rate | wrong/answered |
|---|---:|---:|---:|---:|---:|---:|---:|
| AQuA-RAT | 254 | 2 | 0 | 0 | 0 | 0.008 | 0.000 |
| ASDiv | 301 | 9 | 9 | 6 | 3 | 0.030 | 0.333 |
| GSM8K | 500 | 4 | 4 | 1 | 3 | 0.008 | 0.750 |
| MATH | 350 | 16 | 12 | 8 | 1 | 0.046 | 0.083 |
| MAWPS | 520 | 58 | 58 | 58 | 0 | 0.112 | 0.000 |
| MultiArith | 180 | 15 | 15 | 14 | 1 | 0.083 | 0.067 |
| SVAMP | 300 | 5 | 5 | 5 | 0 | 0.017 | 0.000 |

## Family Summary

| family | total | backend | correct | wrong |
|---|---:|---:|---:|---:|
| `<none>` | 2296 | 0 | 0 | 0 |
| `affine_geometry.midpoint_observable` | 2 | 2 | 1 | 1 |
| `circle_group.clock_angle` | 1 | 1 | 1 | 0 |
| `discrete_affine_sequence.nth_term` | 1 | 1 | 1 | 0 |
| `inner_product_geometry.distance` | 2 | 1 | 1 | 0 |
| `ordered_field.absolute_value_equation` | 1 | 1 | 0 | 0 |
| `ordered_field.compound_growth_rate` | 2 | 1 | 1 | 0 |
| `ordered_field.scalar_percent_action` | 1 | 1 | 1 | 0 |
| `polynomial_notation.base_expansion` | 2 | 2 | 2 | 0 |
| `probability.complement_event` | 5 | 1 | 0 | 0 |
| `real_closed_field.quadratic_root_observable` | 1 | 1 | 0 | 0 |
| `state_event.additive_quantity` | 91 | 91 | 84 | 7 |

## Files

- json: `math_os_prototype\corpus_lift_public_2405_state_event_v4.json`
- jsonl: `math_os_prototype\corpus_lift_public_2405_state_event_v4.jsonl`
