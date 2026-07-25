# Corpus Lift Protocol

## Scope

Public/TeX corpora usually lack gold LiftCertificate labels, so this reports coverage, backend success, wrong answers, and rejection. The full seven-axis match is measured on generated same-structure families.

## Counts

- total: 93
- lifted: 1
- backend_executed: 1
- comparable: 0
- correct: 0
- wrong: 0
- rejected: 92
- errors: 0

## Rates

| metric | value |
|---|---:|
| `lift_rate` | 0.011 |
| `backend_execution_rate` | 0.011 |
| `backend_success_rate` | 0.000 |
| `precision_answered` | 0.000 |
| `wrong_rate_answered` | 0.000 |
| `rejection_rate` | 0.989 |
| `error_rate` | 0.000 |

## Source Summary

| source | total | lifted | backend | correct | wrong | lift rate | wrong/answered |
|---|---:|---:|---:|---:|---:|---:|---:|
| TeX:hon3.tex | 20 | 1 | 1 | 0 | 0 | 0.050 | 0.000 |
| TeX:全問題.tex | 73 | 0 | 0 | 0 | 0 | 0.000 | 0.000 |

## Family Summary

| family | total | backend | correct | wrong |
|---|---:|---:|---:|---:|
| `<none>` | 92 | 0 | 0 | 0 |
| `polynomial_ring.remainder_repeated_linear_divisor` | 1 | 1 | 0 | 0 |

## Files

- json: `math_os_prototype\corpus_lift_tex_200_25families.json`
- jsonl: `math_os_prototype\corpus_lift_tex_200_25families.jsonl`
