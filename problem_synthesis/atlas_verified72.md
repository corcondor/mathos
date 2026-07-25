# Atlas検証付き作問

生成日時: 2026-07-23T09:05:50.304207+00:00

## 検証契約

- An exported item must satisfy backend_verified and expected_family_id in observed LiftCertificates.

## 集計

- 評価候補数: 72
- 二重検証通過数: 72
- 棄却数: 0
- 異なる解答正規形: 60

## Lift family

| family | 検証済み問題数 |
| --- | ---: |
| `elementary_number_theory.prime_constraint_query` | 8 |
| `linear_algebra.frobenius_pairing` | 4 |
| `linear_algebra.orthogonal_projection` | 4 |
| `measure_geometry.planar_area` | 12 |
| `measure_geometry.solid_volume` | 6 |
| `optimization.inner_product_extremum` | 4 |
| `optimization.planar_area_extremum` | 8 |
| `optimization.positive_definite_quadratic` | 4 |
| `probability.autocorrelation_function` | 2 |
| `real_analysis.correlation_limit` | 2 |
| `real_analysis.limit_observable` | 10 |
| `real_analysis.normalized_inner_product_limit` | 4 |
| `real_analysis.planar_measure_limit` | 4 |

## 生成チャート

| chart | 検証済み問題数 |
| --- | ---: |
| `centered_l2_correlation_limit` | 2 |
| `circle_area_limit` | 4 |
| `ellipse_area` | 8 |
| `ellipsoid_volume` | 4 |
| `exponential_sequence_limit` | 5 |
| `frobenius_matrix_pairing` | 4 |
| `norm_constrained_inner_product_extremum` | 4 |
| `normalized_inner_product_limit` | 4 |
| `orthogonal_projection` | 4 |
| `parabolic_revolution_volume` | 2 |
| `parabolic_segment_area` | 4 |
| `positive_definite_quadratic_minimum` | 4 |
| `prime_sum_constraint` | 8 |
| `rational_sequence_limit` | 5 |
| `rectangle_diagonal_area_maximum` | 3 |
| `rectangle_perimeter_area_maximum` | 5 |
| `stationary_ar1_autocorrelation` | 2 |

## 解釈

検証は論理積である。backendによる答えの確認だけでも、LiftCertificateだけでも不十分であり、両方を通過した候補だけをCreativeBenchへ出力する。
