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

- cases: 144
- same-structure pairs: 96
- splits: `{'calib': 27, 'dev': 78, 'held_out': 39}`
- transforms: `{'base': 48, 'numeric': 48, 'surface': 48}`

## Mode Summary

| mode | total | lift family match | pair match | success | answered | wrong/answered | rejected |
|---|---:|---:|---:|---:|---:|---:|---:|
| cold | 144 | 1.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| certified_lift_backend | 144 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 |
| surface_template_ablation | 144 | 1.000 | 1.000 | 0.500 | 0.583 | 0.143 | 0.000 |

## Split Summary

| mode | split | total | success | wrong/total | rejected | lift family match |
|---|---|---:|---:|---:|---:|---:|
| cold | calib | 27 | 0.000 | 0.000 | 0.000 | 1.000 |
| cold | dev | 78 | 0.000 | 0.000 | 0.000 | 1.000 |
| cold | held_out | 39 | 0.000 | 0.000 | 0.000 | 1.000 |
| certified_lift_backend | calib | 27 | 1.000 | 0.000 | 0.000 | 1.000 |
| certified_lift_backend | dev | 78 | 1.000 | 0.000 | 0.000 | 1.000 |
| certified_lift_backend | held_out | 39 | 1.000 | 0.000 | 0.000 | 1.000 |
| surface_template_ablation | calib | 27 | 0.630 | 0.111 | 0.000 | 1.000 |
| surface_template_ablation | dev | 78 | 0.449 | 0.077 | 0.000 | 1.000 |
| surface_template_ablation | held_out | 39 | 0.513 | 0.077 | 0.000 | 1.000 |

## Family Summary

| mode | family | total | success | wrong/total | rejected |
|---|---|---:|---:|---:|---:|
| cold | `affine_geometry.midpoint_observable` | 24 | 0.000 | 0.000 | 0.000 |
| cold | `circle_group.clock_angle` | 24 | 0.000 | 0.000 | 0.000 |
| cold | `discrete_affine_sequence.nth_term` | 24 | 0.000 | 0.000 | 0.000 |
| cold | `inner_product_geometry.distance` | 24 | 0.000 | 0.000 | 0.000 |
| cold | `ordered_field.scalar_percent_action` | 24 | 0.000 | 0.000 | 0.000 |
| cold | `quotient_ring.residue` | 24 | 0.000 | 0.000 | 0.000 |
| certified_lift_backend | `affine_geometry.midpoint_observable` | 24 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `circle_group.clock_angle` | 24 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `discrete_affine_sequence.nth_term` | 24 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `inner_product_geometry.distance` | 24 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `ordered_field.scalar_percent_action` | 24 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `quotient_ring.residue` | 24 | 1.000 | 0.000 | 0.000 |
| surface_template_ablation | `affine_geometry.midpoint_observable` | 24 | 0.250 | 0.000 | 0.000 |
| surface_template_ablation | `circle_group.clock_angle` | 24 | 1.000 | 0.000 | 0.000 |
| surface_template_ablation | `discrete_affine_sequence.nth_term` | 24 | 0.000 | 0.000 | 0.000 |
| surface_template_ablation | `inner_product_geometry.distance` | 24 | 0.583 | 0.000 | 0.000 |
| surface_template_ablation | `ordered_field.scalar_percent_action` | 24 | 0.500 | 0.500 | 0.000 |
| surface_template_ablation | `quotient_ring.residue` | 24 | 0.667 | 0.000 | 0.000 |

## Surface Template Ablation

- compared: 144
- improved: 72
- regressed: 0
- surface-template intents: 84

## Files

- json: `math_os_prototype\generalization_benchmark_protocol.json`
- jsonl: `math_os_prototype\generalization_benchmark_protocol.jsonl`
