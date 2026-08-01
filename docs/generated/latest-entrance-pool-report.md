# MathOS 大学受験数学プール監査

この文書は受験用配信プールから機械的に生成した記録である。
問題インスタンス数ではなく、数値変種を除いた構造数を数える。

## 結果

- 検証済み構造: **117**
- 構造族: **115**
- 幾何・代数・複素数系: **87**
- 高校の語彙へ書き換えた問題: **2**
- 同一構造の数値変種として除外: **72**（生成時点で潰しているため通常は 0）
- 高校の語彙へ還元できず除外: **6**
- 制約が合流しない2段合成として除外: **0**
- 複合分野なのに型付き経路がなく保留: **26**
- 経路はあるが条件が合流する証明DAGがなく保留: **0**
- 配信目的と合わず除外（サイコロ・ギャンブラー）: **12**
- 旧難易度8.4未満（注釈のみ・除外しない）: **145**
- 射が3個未満（注釈のみ・除外しない）: **16**

難易度指標は人手判断に対する AUC が 0.086 だったため、
AUC 0.7 以上で再較正されるまでは配信可否に使わない。
厳密検証・高校範囲への還元・新規性・構造重複だけを採否条件とする。

## 採用契約

```text
型付き数学対象
  -> モルフォロジー・アトラス上の隣接射
  -> 解法射列との整列 + 証明DAGの条件合流
  -> 射の合成
  -> 厳密backend計算
  -> 独立検算
  -> 数I/A・II/B・III/Cの原始操作へのlowering
  -> 構造署名で商を取り、数値違いを除外
  -> Discord配信
```

判定は族の名前では行わない。射の連鎖が高校の原始操作へ還元できるか、
そして問題文と解法が高校の語彙で書けるかだけを見る。
内部探索で大学数学の概念を使うこと自体は禁止しない。
行列で導いた一次分数変換も、平方剰余で作ったグラフも、
問題文を高校の言葉で書き直せる限り受験用プールへ出す。
書き直せない候補だけを研究キューに残す。

## 構造一覧

| 分野 | 構造族 | lowering |
|---|---|---|
| `algebra` | `construct.mobius_fixed_points` | `rational_function -> function_composition -> quadratic_equation -> simultaneous_equations` |
| `algebra` | `construct.reciprocal_recurrence` | `recurrence -> algebraic_identity -> general_term` |
| `algebra` | `polynomial.interpolation_harmonic_observable` | `polynomial_factorization -> simultaneous_equations -> roots_of_unity -> sum_of_series -> differentiation -> remainder_theorem` |
| `algebra` | `relation.polynomial_root_set.affine_image` | `vieta_relations -> polynomial_factorization -> function_composition -> simultaneous_equations -> polynomial_expansion` |
| `algebra` | `relation.polynomial_root_set.reciprocal_image` | `vieta_relations -> polynomial_factorization -> rational_function -> simultaneous_equations -> polynomial_expansion` |
| `algebra` | `series.telescoping_triple_partial_fraction` | `rational_function -> algebraic_identity -> sum_of_series` |
| `algebra_inequality` | `relation.constrained_symmetric.cube_reciprocal_minimum` | `inequality -> algebraic_identity -> simultaneous_equations -> differentiation -> extremum` |
| `algebra_inequality` | `relation.constrained_symmetric.cube_reciprocal_prove_bound` | `inequality -> algebraic_identity -> simultaneous_equations -> polynomial_factorization` |
| `algebra_inequality` | `relation.constrained_symmetric.power_mean_minimum` | `inequality -> algebraic_identity -> simultaneous_equations -> differentiation -> extremum` |
| `algebra_inequality` | `relation.constrained_symmetric.power_mean_prove_bound` | `inequality -> algebraic_identity -> simultaneous_equations -> polynomial_factorization` |
| `algebra_inequality` | `relation.constrained_symmetric.product_reciprocal_minimum` | `inequality -> algebraic_identity -> simultaneous_equations -> differentiation -> extremum` |
| `algebra_inequality` | `relation.constrained_symmetric.product_reciprocal_prove_bound` | `inequality -> algebraic_identity -> simultaneous_equations -> polynomial_factorization` |
| `algebra_inequality` | `relation.constrained_symmetric.reciprocal_minimum` | `inequality -> algebraic_identity -> simultaneous_equations -> differentiation -> extremum` |
| `algebra_inequality` | `relation.constrained_symmetric.reciprocal_prove_bound` | `inequality -> algebraic_identity -> simultaneous_equations -> polynomial_factorization` |
| `algebra_inequality` | `relation.constrained_symmetric.square_reciprocal_minimum` | `inequality -> algebraic_identity -> simultaneous_equations -> differentiation -> extremum` |
| `algebra_inequality` | `relation.constrained_symmetric.square_reciprocal_prove_bound` | `inequality -> algebraic_identity -> simultaneous_equations -> polynomial_factorization` |
| `algebra_inequality` | `relation.constrained_symmetric.weighted_minimum` | `inequality -> algebraic_identity -> simultaneous_equations -> differentiation -> extremum` |
| `algebra_inequality` | `relation.constrained_symmetric.weighted_prove_bound` | `inequality -> algebraic_identity -> simultaneous_equations -> polynomial_factorization` |
| `algebraic_geometry` | `algebraic_geometry.cubic_discriminant_triangle_area` | `polynomial_factorization -> parabola -> coordinate_geometry -> area_shoelace -> quadratic_discriminant -> extremum -> differentiation` |
| `algebraic_geometry` | `algebraic_geometry.even_quartic_parabola_hull_area` | `polynomial_factorization -> parabola -> coordinate_geometry -> convex_hull -> area_shoelace -> extremum -> differentiation` |
| `analytic_geometry` | `conic_duality.tangent_intercept_centroid_minimum` | `tangent_line -> parameter_elimination -> line_equation -> coordinate_geometry -> midpoint -> complex_modulus -> distance_formula -> extremum -> differentiation` |
| `analytic_geometry` | `relation.ellipse.tangent_intercept_area_minimum` | `ellipse -> parametric_curve -> coordinate_geometry -> tangent_line -> differentiation -> line_equation -> area_shoelace -> simultaneous_equations -> algebraic_identity -> polynomial_factorization -> inequality -> extremum` |
| `analytic_geometry` | `relation.parabola.focal_chord_minimum` | `parabola -> parametric_curve -> coordinate_geometry -> line_equation -> distance_formula -> rational_function -> algebraic_identity -> polynomial_factorization -> inequality -> extremum -> differentiation` |
| `analytic_geometry` | `ultradeep.geometry_astroid_envelope_area` | `circle_equation -> ellipse -> coordinate_geometry -> line_equation -> parameter_elimination -> envelope -> differentiation -> parametric_curve -> area_integral -> definite_integral` |
| `combinatorics` | `lattice_paths.dyck_reflection_catalan_count` | `counting -> combination -> symmetry -> algebraic_identity` |
| `combinatorics` | `traceback.lattice_path.catalan_divisor_count` | `counting -> recurrence -> combination -> symmetry -> prime_factorization -> divisor_counting` |
| `combinatorics` | `traceback.lattice_path.catalan_paths` | `counting -> recurrence -> combination -> symmetry` |
| `combinatorics` | `traceback.lattice_path.strictly_above_paths` | `counting -> recurrence -> combination -> symmetry` |
| `combinatorics` | `traceback.lattice_path.through_center_paths` | `counting -> recurrence -> combination` |
| `combinatorics` | `traceback.lattice_path.total_paths` | `counting -> recurrence -> combination` |
| `combinatorics` | `traceback.lattice_path.total_paths_divisor_count` | `counting -> recurrence -> combination -> prime_factorization -> divisor_counting` |
| `complex` | `construct.complex_affine_limit` | `recurrence -> algebraic_identity -> geometric_sequence -> limit -> complex_plane` |
| `complex` | `construct.complex_rotation_period` | `roots_of_unity -> de_moivre -> periodicity` |
| `complex_geometry` | `complex_geometry.reciprocal_root_polygon_area` | `complex_plane -> roots_of_unity -> symmetry -> counting -> convex_hull -> area_shoelace -> extremum -> differentiation` |
| `complex_geometry` | `deep.polygon_subset_centroid` | `roots_of_unity -> regular_polygon -> combination -> coordinate_geometry -> midpoint -> sum_of_series -> polynomial_factorization -> symmetry -> counting` |
| `complex_geometry` | `deep.rotation_diagonal_product_divisors` | `roots_of_unity -> regular_polygon -> distance_formula -> polynomial_factorization -> limit -> integer_arithmetic -> prime_factorization -> divisor_counting` |
| `complex_geometry` | `layered.rotation_orbit_hull_area` | `roots_of_unity -> de_moivre -> symmetry -> regular_polygon -> area_shoelace` |
| `complex_geometry` | `traceback.regular_polygon.area` | `regular_polygon -> triangle_area -> coordinate_geometry -> sum_of_series` |
| `complex_geometry` | `traceback.regular_polygon.centroid_zero_subsets` | `regular_polygon -> combination -> roots_of_unity -> sum_of_series -> symmetry -> counting` |
| `complex_geometry` | `traceback.regular_polygon.diagonal_count` | `regular_polygon -> counting -> combination` |
| `complex_geometry` | `traceback.regular_polygon.distance_product_divisors` | `roots_of_unity -> polynomial_factorization -> distance_formula -> integer_arithmetic -> prime_factorization -> divisor_counting` |
| `complex_geometry` | `traceback.regular_polygon.sum_sq_pairwise` | `regular_polygon -> vector_addition -> roots_of_unity -> distance_formula -> sum_of_series` |
| `complex_geometry` | `traceback.regular_polygon.vertex_distance_product` | `roots_of_unity -> polynomial_factorization -> limit -> distance_formula` |
| `complex_geometry_algebra_combinatorics` | `morphology.unit_roots_antipodal_compatibility_count` | `regular_polygon -> complex_plane -> roots_of_unity -> vieta_relations -> algebraic_identity -> polynomial_factorization -> counting -> combination -> symmetry` |
| `complex_geometry_combinatorics_probability` | `morphology.cyclic_configuration_character_count` | `regular_polygon -> roots_of_unity -> complex_plane -> symmetry -> congruence -> periodicity -> sum_of_series -> polynomial_expansion -> counting -> combination -> probability -> expectation` |
| `conic_geometry` | `traceback.ellipse_tangent.center_to_polar_dist_sq` | `ellipse -> line_equation -> tangent_line -> coordinate_geometry -> simultaneous_equations` |
| `conic_geometry` | `traceback.ellipse_tangent.chord_length_sq` | `ellipse -> tangent_line -> differentiation -> line_equation -> distance_formula` |
| `conic_geometry` | `traceback.ellipse_tangent.chord_midpoint_x` | `ellipse -> tangent_line -> differentiation -> midpoint -> locus -> parameter_elimination` |
| `conic_geometry` | `traceback.ellipse_tangent.contact_triangle_area` | `ellipse -> tangent_line -> differentiation -> coordinate_geometry -> simultaneous_equations -> area_shoelace` |
| `conic_geometry` | `traceback.ellipse_tangent.monge_radius_sq` | `ellipse -> tangent_line -> differentiation -> inner_product -> circle_equation` |
| `conic_geometry` | `traceback.ellipse_tangent.tangent_slope_product` | `ellipse -> tangent_line -> differentiation -> coordinate_geometry -> simultaneous_equations` |
| `conic_geometry` | `traceback.hyperbola_asymptote.asymptote_distance_product` | `hyperbola -> line_equation -> coordinate_geometry -> simultaneous_equations` |
| `conic_geometry` | `traceback.hyperbola_asymptote.asymptote_intersection_x` | `hyperbola -> tangent_line -> differentiation -> line_equation -> simultaneous_equations` |
| `conic_geometry` | `traceback.hyperbola_asymptote.asymptote_triangle_area` | `hyperbola -> tangent_line -> differentiation -> line_equation -> area_shoelace` |
| `conic_geometry` | `traceback.hyperbola_asymptote.director_circle_radius_sq` | `hyperbola -> tangent_line -> differentiation -> inner_product -> circle_equation` |
| `conic_geometry` | `traceback.hyperbola_asymptote.eccentricity_sq` | `hyperbola -> algebraic_identity` |
| `conic_geometry` | `traceback.hyperbola_asymptote.focal_distance_difference` | `hyperbola -> distance_formula` |
| `conic_geometry` | `traceback.hyperbola_asymptote.semi_latus_rectum` | `hyperbola -> distance_formula -> coordinate_geometry -> simultaneous_equations` |
| `conic_geometry` | `traceback.parabola_focal_chord.chord_length` | `parabola -> hyperbola -> distance_formula` |
| `conic_geometry` | `traceback.parabola_focal_chord.midpoint_to_directrix` | `parabola -> hyperbola -> distance_formula -> midpoint` |
| `conic_geometry` | `traceback.parabola_focal_chord.min_chord_length` | `parabola -> hyperbola -> distance_formula -> extremum -> differentiation` |
| `conic_geometry` | `traceback.parabola_focal_chord.parameter_product` | `parabola -> hyperbola -> distance_formula -> parameter_elimination` |
| `conic_geometry` | `traceback.parabola_focal_chord.reciprocal_focal_radii_sum` | `parabola -> hyperbola -> distance_formula -> rational_function -> algebraic_identity` |
| `conic_geometry` | `traceback.parabola_focal_chord.tangent_intersection_x` | `parabola -> tangent_line -> differentiation -> simultaneous_equations -> line_equation` |
| `conic_geometry` | `traceback.parabola_focal_chord.tangent_slope_product` | `parabola -> tangent_line -> differentiation -> line_equation -> algebraic_identity` |
| `convex_geometry` | `ultradeep.geometry_regular_polygon_minkowski_perimeter` | `roots_of_unity -> complex_plane -> regular_polygon -> de_moivre -> symmetry -> vector_addition -> convex_hull -> distance_formula -> sum_of_series` |
| `differential_geometry` | `ultradeep.geometry_parabola_normal_envelope` | `parabola -> differentiation -> vector_addition -> normal_line -> parameter_elimination -> envelope -> extremum -> parametric_curve -> simultaneous_equations -> locus` |
| `euclidean_geometry` | `relation.triangle.sixty_degree_side_bound` | `sine_cosine_rule -> trigonometric_identity -> simultaneous_equations -> algebraic_identity -> polynomial_factorization -> inequality` |
| `euclidean_geometry` | `ultradeep.geometry_orthocenter_locus_area` | `ellipse -> coordinate_geometry -> triangle_area -> inner_product -> line_equation -> triangle_center -> simultaneous_equations -> vector_addition -> parameter_elimination -> area_shoelace -> area_integral` |
| `geometry` | `construct.parabola_right_angle_chord` | `inner_product -> line_equation -> algebraic_identity -> simultaneous_equations` |
| `geometry` | `passage_region.line_family_sweep` | `line_equation -> parameter_elimination -> quadratic_range -> area_integral` |
| `geometry` | `passage_region.parabola_family_sweep` | `parabola -> parameter_elimination -> quadratic_range -> area_integral` |
| `geometry_algebra_analysis` | `morphology.parabola_root_invariant_locus_extremum` | `parabola -> coordinate_geometry -> distance_formula -> simultaneous_equations -> polynomial_expansion -> quadratic_equation -> vieta_relations -> algebraic_identity -> tangent_line -> differentiation -> midpoint -> parameter_elimination -> locus -> extremum` |
| `number_theory` | `construct.linear_recurrence_mod_period` | `recurrence -> general_term -> congruence -> periodicity` |
| `number_theory` | `deep.recurrence_period_quadratic_character` | `recurrence -> general_term -> congruence -> periodicity -> prime_factorization -> square_number` |
| `number_theory` | `layered.recurrence_period_observable` | `recurrence -> general_term -> congruence -> periodicity -> prime_factorization -> divisor_counting` |
| `number_theory` | `layered.recurrence_period_observable` | `recurrence -> general_term -> congruence -> periodicity -> prime_factorization` |
| `number_theory` | `layered.recurrence_period_observable` | `recurrence -> general_term -> congruence -> periodicity -> gcd_lcm -> counting` |
| `number_theory` | `multiplicative.mobius_divisor_sum_totient_ratio` | `divisor_counting -> sum_of_series -> prime_factorization -> congruence` |
| `number_theory` | `traceback.digit_power.digit_count` | `geometric_sequence -> exponential -> logarithm -> integer_arithmetic` |
| `number_theory` | `traceback.digit_power.digit_increase_count` | `geometric_sequence -> exponential -> logarithm -> integer_arithmetic` |
| `number_theory` | `traceback.digit_power.digit_sum` | `geometric_sequence -> exponential -> integer_arithmetic` |
| `number_theory` | `traceback.digit_power.leading_digit` | `geometric_sequence -> exponential -> logarithm -> integer_arithmetic` |
| `number_theory` | `traceback.digit_power.leading_one_count` | `geometric_sequence -> exponential -> logarithm -> integer_arithmetic` |
| `plane_geometry` | `traceback.cyclic_quadrilateral.area` | `circle_equation -> trigonometric_ratio -> sine_cosine_rule -> area_shoelace` |
| `plane_geometry` | `traceback.cyclic_quadrilateral.circumradius_sq` | `circle_equation -> trigonometric_ratio -> sine_cosine_rule` |
| `plane_geometry` | `traceback.cyclic_quadrilateral.cos_angle_a` | `circle_equation -> trigonometric_ratio -> sine_cosine_rule` |
| `plane_geometry` | `traceback.cyclic_quadrilateral.diagonal_ac_sq` | `circle_equation -> trigonometric_ratio -> sine_cosine_rule` |
| `plane_geometry` | `traceback.cyclic_quadrilateral.diagonal_product` | `circle_equation -> trigonometric_ratio -> sine_cosine_rule -> algebraic_identity` |
| `plane_geometry` | `traceback.incircle_excircle.contact_segment_longest` | `coordinate_geometry -> triangle_area -> triangle_center -> distance_formula` |
| `plane_geometry` | `traceback.incircle_excircle.euler_OI_sq` | `coordinate_geometry -> triangle_area -> circle_equation -> triangle_center -> algebraic_identity` |
| `plane_geometry` | `traceback.incircle_excircle.exradii_product` | `coordinate_geometry -> triangle_area -> triangle_center` |
| `plane_geometry` | `traceback.incircle_excircle.exradii_reciprocal_sum` | `coordinate_geometry -> triangle_area -> triangle_center` |
| `plane_geometry` | `traceback.incircle_excircle.exradii_sum` | `coordinate_geometry -> triangle_area -> triangle_center -> circle_equation` |
| `plane_geometry` | `traceback.incircle_excircle.exradius_opposite_longest` | `coordinate_geometry -> triangle_area -> distance_formula -> triangle_center` |
| `plane_geometry` | `traceback.triangle_centers.OH_dist_sq` | `coordinate_geometry -> triangle_area -> circle_equation -> triangle_center -> inner_product -> distance_formula` |
| `plane_geometry` | `traceback.triangle_centers.area` | `coordinate_geometry -> triangle_area -> area_shoelace` |
| `plane_geometry` | `traceback.triangle_centers.circumradius_sq` | `coordinate_geometry -> triangle_area -> circle_equation -> simultaneous_equations` |
| `plane_geometry` | `traceback.triangle_centers.euler_line_slope` | `coordinate_geometry -> triangle_area -> circle_equation -> triangle_center -> inner_product -> line_equation` |
| `plane_geometry` | `traceback.triangle_centers.incenter_x` | `coordinate_geometry -> triangle_area -> distance_formula -> triangle_center` |
| `plane_geometry` | `traceback.triangle_centers.inradius` | `coordinate_geometry -> triangle_area -> distance_formula -> triangle_center` |
| `plane_geometry` | `traceback.triangle_centers.nine_point_radius_sq` | `coordinate_geometry -> triangle_area -> midpoint -> circle_equation` |
| `plane_geometry` | `traceback.triangle_centers.orthocenter_x` | `coordinate_geometry -> triangle_area -> triangle_center -> inner_product -> simultaneous_equations` |
| `probability` | `probability.left_to_right_maxima_expectation` | `probability -> expectation -> sum_of_series` |
| `probability` | `probability.random_bridge_zero_count` | `counting -> combination -> expectation -> sum_of_series` |
| `probability_algebra_analysis` | `motif.quadratic_root_lattice_limit` | `counting -> probability -> integer_arithmetic -> quadratic_discriminant -> inequality -> coordinate_geometry -> limit -> definite_integral -> area_integral -> quadratic_equation -> algebraic_identity -> sum_of_series` |
| `projective_geometry` | `ultradeep.geometry_ellipse_tangent_pair_locus` | `ellipse -> trigonometric_identity -> complex_plane -> parameter_elimination -> symmetry -> tangent_line -> line_equation -> simultaneous_equations -> de_moivre -> coordinate_geometry -> locus` |
| `real_analysis` | `analysis.boundary_layer_integral_limit` | `definite_integral -> area_integral -> algebraic_identity -> limit -> inequality` |
| `real_analysis` | `analysis.reflection_symmetric_integral` | `definite_integral -> symmetry -> vector_addition -> area_integral` |
| `real_analysis` | `asymptotic.recurrence_square_increment` | `square_number -> integer_arithmetic -> limit -> differentiation -> sequence -> quadratic_equation -> inequality` |
| `real_analysis` | `fusion.trig_absolute_value_integral` | `trigonometric_identity -> trigonometric_equation -> inequality -> definite_integral` |
| `real_analysis` | `fusion.trig_floor_integral` | `trigonometric_equation -> inequality -> counting -> definite_integral` |
| `sequence` | `relation.sequence.affine_fixed_point_coordinate` | `recurrence -> function_composition -> simultaneous_equations -> geometric_sequence -> general_term -> inequality -> mathematical_induction` |
| `sequence_analysis` | `relation.iteration.error_squaring_coordinate` | `recurrence -> polynomial_expansion -> algebraic_identity -> exponential -> general_term -> limit` |
| `trigonometry` | `relation.triangle_angles.cos_sum_maximum` | `trigonometric_identity -> extremum -> differentiation` |
| `trigonometry` | `relation.triangle_angles.sin_product_maximum` | `trigonometric_identity -> extremum -> differentiation` |
| `trigonometry` | `relation.triangle_angles.sin_sum_maximum` | `trigonometric_identity -> extremum -> differentiation` |
