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

- cases: 4608
- same-structure pairs: 3072
- splits: `{'calib': 1005, 'dev': 2682, 'held_out': 921}`
- transforms: `{'base': 1536, 'numeric': 1536, 'surface': 1536}`

## Mode Summary

| mode | total | lift family match | pair match | success | answered | wrong/answered | rejected |
|---|---:|---:|---:|---:|---:|---:|---:|
| certified_lift_backend | 4608 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 |

## Split Summary

| mode | split | total | success | wrong/total | rejected | lift family match |
|---|---|---:|---:|---:|---:|---:|
| certified_lift_backend | calib | 1005 | 1.000 | 0.000 | 0.000 | 1.000 |
| certified_lift_backend | dev | 2682 | 1.000 | 0.000 | 0.000 | 1.000 |
| certified_lift_backend | held_out | 921 | 1.000 | 0.000 | 0.000 | 1.000 |

## Family Summary

| mode | family | total | success | wrong/total | rejected |
|---|---|---:|---:|---:|---:|
| certified_lift_backend | `affine_geometry.line_intersection` | 192 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `affine_geometry.midpoint_observable` | 192 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `calculus.polynomial_definite_integral` | 192 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `calculus.polynomial_derivative_value` | 192 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `circle_group.clock_angle` | 192 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `combinatorics.binomial_coefficient` | 192 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `discrete_affine_sequence.nth_term` | 192 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `elementary_functions.exponential_equation` | 192 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `elementary_functions.log_equation` | 192 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `elementary_functions.trig_pythagorean` | 192 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `euclidean_geometry.circle_radius` | 192 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `inner_product_geometry.distance` | 192 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `inner_product_geometry.dot_product` | 192 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `ordered_field.absolute_value_equation` | 192 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `ordered_field.compound_growth_rate` | 192 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `ordered_field.scalar_percent_action` | 192 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `polynomial_notation.base_expansion` | 192 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `polynomial_ring.remainder_linear_divisor` | 192 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `probability.binomial_exact` | 192 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `probability.complement_event` | 192 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `quotient_ring.residue` | 192 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `real_closed_field.quadratic_interval` | 192 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `real_closed_field.quadratic_root_observable` | 192 | 1.000 | 0.000 | 0.000 |
| certified_lift_backend | `vector_space.linear_system_2x2` | 192 | 1.000 | 0.000 | 0.000 |

## Surface Template Ablation

- compared: 0
- improved: 0
- regressed: 0
- surface-template intents: 0

## Files

- json: `math_os_prototype\generalization_benchmark_24families_64seeds_after_gates.json`
- jsonl: `math_os_prototype\generalization_benchmark_24families_64seeds_after_gates.jsonl`
