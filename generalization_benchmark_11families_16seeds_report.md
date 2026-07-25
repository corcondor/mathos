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

- cases: 528
- same-structure pairs: 352
- splits: `{'calib': 132, 'dev': 282, 'held_out': 114}`
- transforms: `{'base': 176, 'numeric': 176, 'surface': 176}`

## Mode Summary

| mode | total | lift family match | pair match | success | answered | wrong/answered | rejected |
|---|---:|---:|---:|---:|---:|---:|---:|
| certified_lift_backend | 528 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 |

## Split Summary

| mode | split | total | success | wrong/total | rejected | lift family match |
|---|---|---:|---:|---:|---:|---:|
| certified_lift_backend | calib | 132 | 1.000 | 0.000 | 0.000 | 1.000 |
| certified_lift_backend | dev | 282 | 1.000 | 0.000 | 0.000 | 1.000 |
| certified_lift_backend | held_out | 114 | 1.000 | 0.000 | 0.000 | 1.000 |

## Family Summary

| mode | family | total | success | wrong/total | rejected |
|---|---|---:|---:|---:|---:|
| certified_lift_backend | `affine_geometry.midpoint_observable` | 48 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `circle_group.clock_angle` | 48 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `discrete_affine_sequence.nth_term` | 48 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `inner_product_geometry.distance` | 48 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `ordered_field.absolute_value_equation` | 48 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `ordered_field.compound_growth_rate` | 48 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `ordered_field.scalar_percent_action` | 48 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `polynomial_notation.base_expansion` | 48 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `probability.complement_event` | 48 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `quotient_ring.residue` | 48 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `real_closed_field.quadratic_interval` | 48 | 1.000 | 0.000 | 0.000 |

## Surface Template Ablation

- compared: 0
- improved: 0
- regressed: 0
- surface-template intents: 0

## Files

- json: `math_os_prototype\generalization_benchmark_11families_16seeds.json`
- jsonl: `math_os_prototype\generalization_benchmark_11families_16seeds.jsonl`
