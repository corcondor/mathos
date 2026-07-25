# Atlas Verified Problem Synthesis

Generated: 2026-07-23T08:22:19.267689+00:00

## Contract

- An exported item must satisfy backend_verified and expected_family_id in observed LiftCertificates.

## Summary

- evaluated: 54
- verified: 54
- rejected: 0
- unique normal forms: 48

## Families

| family | verified |
| --- | ---: |
| `elementary_number_theory.prime_constraint_query` | 8 |
| `measure_geometry.planar_area` | 12 |
| `measure_geometry.solid_volume` | 6 |
| `optimization.planar_area_extremum` | 8 |
| `optimization.scalar_minimum` | 4 |
| `real_analysis.correlation_limit` | 2 |
| `real_analysis.limit_observable` | 10 |
| `real_analysis.planar_measure_limit` | 4 |

## Charts

| chart | verified |
| --- | ---: |
| `circle_area_limit` | 4 |
| `ellipse_area` | 8 |
| `ellipsoid_volume` | 4 |
| `exponential_sequence_limit` | 5 |
| `independent_noise_correlation_limit` | 2 |
| `parabolic_revolution_volume` | 2 |
| `parabolic_segment_area` | 4 |
| `prime_sum_constraint` | 8 |
| `rational_sequence_limit` | 5 |
| `rectangle_diagonal_area_maximum` | 3 |
| `rectangle_perimeter_area_maximum` | 5 |
| `scalar_quadratic_minimum` | 4 |

## Interpretation

Verification is conjunctive: a backend proof alone is insufficient, and a LiftCertificate alone is insufficient. Only candidates passing both gates are exported to CreativeBench.
