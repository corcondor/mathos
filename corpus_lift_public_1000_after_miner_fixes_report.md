# Corpus Lift Protocol

## Scope

Public/TeX corpora usually lack gold LiftCertificate labels, so this reports coverage, backend success, wrong answers, and rejection. The full seven-axis match is measured on generated same-structure families.

## Counts

- total: 1000
- lifted: 12
- backend_executed: 10
- comparable: 960
- correct: 8
- wrong: 0
- rejected: 988
- errors: 0

## Rates

| metric | value |
|---|---:|
| `lift_rate` | 0.012 |
| `backend_execution_rate` | 0.010 |
| `backend_success_rate` | 0.008 |
| `precision_answered` | 0.800 |
| `wrong_rate_answered` | 0.000 |
| `rejection_rate` | 0.988 |
| `error_rate` | 0.000 |

## Source Summary

| source | total | lifted | backend | correct | wrong | lift rate | wrong/answered |
|---|---:|---:|---:|---:|---:|---:|---:|
| AQuA-RAT | 60 | 0 | 0 | 0 | 0 | 0.000 | 0.000 |
| ASDiv | 150 | 0 | 0 | 0 | 0 | 0.000 | 0.000 |
| GSM8K | 200 | 0 | 0 | 0 | 0 | 0.000 | 0.000 |
| MATH | 140 | 12 | 10 | 8 | 0 | 0.086 | 0.000 |
| MAWPS | 150 | 0 | 0 | 0 | 0 | 0.000 | 0.000 |
| MultiArith | 150 | 0 | 0 | 0 | 0 | 0.000 | 0.000 |
| SVAMP | 150 | 0 | 0 | 0 | 0 | 0.000 | 0.000 |

## Family Summary

| family | total | backend | correct | wrong |
|---|---:|---:|---:|---:|
| `<none>` | 988 | 0 | 0 | 0 |
| `affine_geometry.midpoint_observable` | 1 | 1 | 1 | 0 |
| `circle_group.clock_angle` | 1 | 1 | 1 | 0 |
| `discrete_affine_sequence.nth_term` | 1 | 1 | 1 | 0 |
| `inner_product_geometry.distance` | 2 | 1 | 1 | 0 |
| `ordered_field.absolute_value_equation` | 1 | 1 | 0 | 0 |
| `ordered_field.compound_growth_rate` | 1 | 1 | 1 | 0 |
| `ordered_field.scalar_percent_action` | 1 | 1 | 1 | 0 |
| `polynomial_notation.base_expansion` | 2 | 2 | 2 | 0 |
| `probability.complement_event` | 2 | 1 | 0 | 0 |

## Files

- json: `math_os_prototype\corpus_lift_public_1000_after_miner_fixes.json`
- jsonl: `math_os_prototype\corpus_lift_public_1000_after_miner_fixes.jsonl`
