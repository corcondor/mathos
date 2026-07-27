# MathOS 大学受験数学プール監査

この文書は受験用配信プールから機械的に生成した記録である。
問題インスタンス数ではなく、数値変種を除いた構造数を数える。

## 結果

- 検証済み構造: **46**
- 構造族: **46**
- 幾何・代数・複素数系: **36**
- ギャンブラー破産系: **0**
- Paley・グラフ理論を表面に出す問題: **0**
- 同一構造の数値変種として除外: **179**
- 高校範囲への還元を証明できず除外: **51**

## 採用契約

```text
型付き数学対象
  -> 射の合成
  -> 厳密backend計算
  -> 独立検算
  -> 数I/A・II/B・III/Cの原始操作へのlowering
  -> 構造署名で商を取り、数値違いを除外
  -> Discord配信
```

内部探索で大学数学の概念を使うこと自体は禁止しない。
ただし問題文と完結した解法を高校範囲へ還元できない候補は、
研究キューには残しても受験用プールへは出さない。

## 構造一覧

| 分野 | 構造族 | lowering |
|---|---|---|
| `algebra` | `construct.mobius_fixed_points` | `rational_function -> quadratic_equation -> fixed_point_equation` |
| `algebra` | `construct.mobius_iteration_period` | `rational_function -> function_composition -> periodicity` |
| `algebra` | `construct.reciprocal_recurrence` | `recurrence -> algebraic_transform -> sequence_limit` |
| `algebra` | `polynomial.interpolation_harmonic_observable` | `polynomial_factorization -> finite_difference -> differentiation` |
| `algebraic_geometry` | `algebraic_geometry.cubic_discriminant_triangle_area` | `polynomial_roots -> vieta_relations -> coordinate_area -> one_variable_extremum` |
| `algebraic_geometry` | `algebraic_geometry.even_quartic_parabola_hull_area` | `polynomial_roots -> vieta_relations -> coordinate_area -> one_variable_extremum` |
| `algebraic_geometry_number_theory` | `ultradeep.cubic_root_triangle_discriminant_divisor_count` | `polynomial_roots -> vieta_relations -> coordinate_area -> integer_factorization` |
| `analytic_geometry` | `conic_duality.tangent_intercept_centroid_minimum` | `differentiation -> tangent_line -> centroid -> quadratic_minimum` |
| `analytic_geometry` | `ultradeep.geometry_astroid_envelope_area` | `trigonometric_parameter -> tangent_line -> parameter_elimination -> definite_integral -> area` |
| `combinatorics` | `lattice_paths.dyck_reflection_catalan_count` | `lattice_path -> combination -> reflection_bijection` |
| `combinatorics_number_theory` | `binomial.roots_of_unity_filter_mod3` | `binomial_theorem -> complex_plane -> roots_of_unity` |
| `complex` | `construct.complex_affine_limit` | `complex_number -> geometric_sequence -> sequence_limit` |
| `complex` | `construct.complex_rotation_period` | `complex_plane -> de_moivre -> integer_period` |
| `complex_algebra_number_theory` | `ultradeep.cyclotomic_distance_norm_divisor_count` | `complex_plane -> roots_of_unity -> polynomial_factorization -> integer_factorization` |
| `complex_geometry` | `complex_geometry.reciprocal_root_polygon_area` | `complex_plane -> roots_of_unity -> polygon_area -> trigonometry` |
| `complex_geometry` | `deep.polygon_subset_centroid` | `complex_plane -> roots_of_unity -> centroid -> combination` |
| `complex_geometry` | `deep.rotation_diagonal_product_divisors` | `complex_plane -> roots_of_unity -> distance -> polynomial_factorization -> integer_factorization` |
| `complex_geometry` | `layered.rotation_orbit_hull_area` | `complex_plane -> de_moivre -> regular_polygon -> area` |
| `complex_geometry` | `traceback.regular_polygon.area` | `trigonometric_ratio -> triangle_decomposition -> area_sum` |
| `complex_geometry` | `traceback.regular_polygon.centroid_zero_subsets` | `complex_plane -> symmetry -> subset_counting` |
| `complex_geometry` | `traceback.regular_polygon.diagonal_count` | `combination_counting` |
| `complex_geometry` | `traceback.regular_polygon.distance_product_divisors` | `complex_plane -> polynomial_factorization -> divisor_counting` |
| `complex_geometry` | `traceback.regular_polygon.sum_sq_pairwise` | `complex_plane -> vector_sum -> squared_distance` |
| `complex_geometry` | `traceback.regular_polygon.vertex_distance_product` | `complex_plane -> polynomial_factorization -> limit_evaluation` |
| `differential_geometry` | `ultradeep.geometry_parabola_normal_envelope` | `parabola -> differentiation -> normal_line -> parameter_elimination -> locus` |
| `euclidean_geometry` | `ultradeep.geometry_orthocenter_locus_area` | `ellipse -> inner_product -> orthocenter -> parameter_elimination -> area` |
| `geometry` | `construct.parabola_right_angle_chord` | `coordinate_geometry -> inner_product -> quadratic_equation` |
| `geometry` | `passage_region.line_family_sweep` | `quadratic_range -> parameter_elimination -> definite_integral -> area` |
| `geometry` | `passage_region.parabola_family_sweep` | `quadratic_range -> parameter_elimination -> definite_integral -> area` |
| `geometry_algebra` | `construct.cubic_tangent_midpoint_locus` | `differentiation -> tangent_line -> vieta_relations -> parameter_elimination -> locus` |
| `geometry_algebra` | `layered.cubic_tangent_iteration` | `differentiation -> tangent_line -> recurrence -> mathematical_induction` |
| `geometry_algebra` | `traceback.cubic_tangent.iterate_x_n` | `differentiation -> geometric_sequence -> general_term` |
| `geometry_algebra` | `traceback.cubic_tangent.log_growth_limit` | `geometric_sequence -> logarithm -> limit_evaluation` |
| `geometry_algebra` | `traceback.cubic_tangent.midpoint_locus` | `differentiation -> midpoint -> locus_elimination` |
| `geometry_algebra` | `traceback.cubic_tangent.reintersection_x` | `differentiation -> cubic_equation -> vieta_relations` |
| `geometry_analysis` | `deep.tangent_iteration_growth` | `differentiation -> tangent_line -> recurrence -> logarithm -> sequence_limit` |
| `linear_algebra_number_theory` | `recurrence.cassini_fibonacci_determinant_invariant` | `recurrence -> mathematical_induction -> algebraic_identity` |
| `number_theory` | `construct.linear_recurrence_mod_period` | `recurrence -> congruence -> finite_state_iteration` |
| `number_theory` | `layered.recurrence_period_observable` | `recurrence -> congruence -> finite_counting -> integer_factorization` |
| `probability` | `probability.left_to_right_maxima_expectation` | `permutation -> indicator_counting -> expectation` |
| `projective_geometry` | `ultradeep.geometry_ellipse_tangent_pair_locus` | `ellipse -> differentiation -> tangent_line -> simultaneous_equations -> parameter_elimination -> locus` |
| `real_analysis` | `analysis.boundary_layer_integral_limit` | `definite_integral -> substitution -> inequality -> sequence_limit` |
| `real_analysis` | `analysis.reflection_symmetric_integral` | `definite_integral -> substitution -> trigonometric_identity` |
| `real_analysis` | `asymptotic.recurrence_square_increment` | `recurrence -> inequality -> sequence_limit` |
| `real_analysis` | `fusion.trig_absolute_value_integral` | `trigonometric_equation -> sign_partition -> definite_integral` |
| `real_analysis` | `fusion.trig_floor_integral` | `trigonometric_inequality -> piecewise_function -> definite_integral` |
