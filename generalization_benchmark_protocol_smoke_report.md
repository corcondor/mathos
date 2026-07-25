# Generalization Benchmark Protocol

## Scope

This report tests whether generated problems can be lifted to the same abstract structure before claiming generalization.

## Protocol Coverage

1. same_structure_pair_generation
2. surface_transformation
3. numeric_transformation
4. held_out_split
5. lift_certificate_match_rate
6. backend_success_rate
7. wrong_answer_rate
8. rejection_rate
9. surface_template_ablation

## Generated Data

- cases: 18
- same-structure pairs: 12
- splits: `{'calib': 6, 'dev': 9, 'held_out': 3}`
- transforms: `{'base': 6, 'numeric': 6, 'surface': 6}`

## Mode Summary

| mode | total | lift family match | pair match | success | answered | wrong/answered | rejected |
|---|---:|---:|---:|---:|---:|---:|---:|
| cold | 18 | 1.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| certified_lift_backend | 18 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 |
| surface_template_ablation | 18 | 1.000 | 1.000 | 0.722 | 0.722 | 0.000 | 0.000 |

## Surface Template Ablation

- compared: 18
- improved: 13
- regressed: 0
- surface-template intents: 13

## Files

- json: `math_os_prototype\generalization_benchmark_protocol_smoke.json`
- jsonl: `math_os_prototype\generalization_benchmark_protocol_smoke.jsonl`
