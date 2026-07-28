# MathOS 大学受験数学プール監査

この文書は受験用配信プールから機械的に生成した記録である。
問題インスタンス数ではなく、数値変種を除いた構造数を数える。

## 結果

- 検証済み構造: **100**
- 構造族: **98**
- 幾何・代数・複素数系: **64**
- 高校の語彙へ書き換えた問題: **4**
- 同一構造の数値変種として除外: **70**（生成時点で潰しているため通常は 0）
- 高校の語彙へ還元できず除外: **10**

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
| `algebra` | `series.telescoping_triple_partial_fraction` | `rational_function -> algebraic_identity -> sum_of_series` |
| `algebraic_geometry` | `algebraic_geometry.cubic_discriminant_triangle_area` | `polynomial_factorization -> parabola -> coordinate_geometry -> area_shoelace -> quadratic_discriminant -> extremum -> differentiation` |
| `algebraic_geometry` | `algebraic_geometry.even_quartic_parabola_hull_area` | `polynomial_factorization -> parabola -> coordinate_geometry -> convex_hull -> area_shoelace -> extremum -> differentiation` |
| `algebraic_geometry_number_theory` | `ultradeep.cubic_root_triangle_discriminant_divisor_count` | `polynomial_expansion -> vieta_relations -> differentiation -> extremum -> quadratic_discriminant -> parabola -> coordinate_geometry -> triangle_area -> polynomial_factorization -> algebraic_identity -> area_shoelace -> integer_arithmetic -> prime_factorization -> divisor_counting` |
| `analytic_geometry` | `conic_duality.tangent_intercept_centroid_minimum` | `tangent_line -> parameter_elimination -> line_equation -> coordinate_geometry -> midpoint -> complex_modulus -> distance_formula -> extremum -> differentiation` |
| `analytic_geometry` | `ultradeep.geometry_astroid_envelope_area` | `circle_equation -> ellipse -> coordinate_geometry -> line_equation -> parameter_elimination -> envelope -> differentiation -> parametric_curve -> area_integral -> definite_integral` |
| `combinatorics` | `lattice_paths.dyck_reflection_catalan_count` | `counting -> combination -> symmetry -> algebraic_identity` |
| `combinatorics` | `traceback.lattice_path.catalan_divisor_count` | `counting -> recurrence -> combination -> symmetry -> prime_factorization -> divisor_counting` |
| `combinatorics` | `traceback.lattice_path.catalan_paths` | `counting -> recurrence -> combination -> symmetry` |
| `combinatorics` | `traceback.lattice_path.strictly_above_paths` | `counting -> recurrence -> combination -> symmetry` |
| `combinatorics` | `traceback.lattice_path.through_center_paths` | `counting -> recurrence -> combination` |
| `combinatorics` | `traceback.lattice_path.total_paths` | `counting -> recurrence -> combination` |
| `combinatorics` | `traceback.lattice_path.total_paths_divisor_count` | `counting -> recurrence -> combination -> prime_factorization -> divisor_counting` |
| `combinatorics_analysis` | `binomial.beta_integral_duality` | `polynomial_expansion -> combination -> definite_integral` |
| `combinatorics_number_theory` | `binomial.roots_of_unity_filter_mod3` | `combination -> polynomial_expansion -> roots_of_unity -> sum_of_series -> trigonometric_identity` |
| `complex` | `construct.complex_affine_limit` | `recurrence -> algebraic_identity -> geometric_sequence -> limit -> complex_plane` |
| `complex` | `construct.complex_rotation_period` | `roots_of_unity -> de_moivre -> periodicity` |
| `complex_algebra_number_theory` | `ultradeep.cyclotomic_distance_norm_divisor_count` | `roots_of_unity -> gcd_lcm -> counting -> distance_formula -> polynomial_factorization -> remainder_theorem -> polynomial_expansion -> integer_arithmetic -> algebraic_identity -> prime_factorization -> divisor_counting` |
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
| `convex_geometry` | `ultradeep.geometry_regular_polygon_minkowski_perimeter` | `roots_of_unity -> complex_plane -> regular_polygon -> de_moivre -> symmetry -> vector_addition -> convex_hull -> distance_formula -> sum_of_series` |
| `differential_geometry` | `ultradeep.geometry_parabola_normal_envelope` | `parabola -> differentiation -> vector_addition -> normal_line -> parameter_elimination -> envelope -> extremum -> parametric_curve -> simultaneous_equations -> locus` |
| `euclidean_geometry` | `ultradeep.geometry_orthocenter_locus_area` | `ellipse -> coordinate_geometry -> triangle_area -> inner_product -> line_equation -> triangle_center -> simultaneous_equations -> vector_addition -> parameter_elimination -> area_shoelace -> area_integral` |
| `geometry` | `construct.parabola_right_angle_chord` | `inner_product -> line_equation -> algebraic_identity -> simultaneous_equations` |
| `geometry` | `passage_region.line_family_sweep` | `line_equation -> parameter_elimination -> quadratic_range -> area_integral` |
| `geometry` | `passage_region.parabola_family_sweep` | `parabola -> parameter_elimination -> quadratic_range -> area_integral` |
| `geometry_algebra` | `construct.cubic_tangent_midpoint_locus` | `tangent_line -> differentiation -> vieta_relations -> midpoint -> locus -> parameter_elimination` |
| `geometry_algebra` | `layered.cubic_tangent_iteration` | `tangent_line -> differentiation -> vieta_relations -> geometric_sequence -> recurrence -> general_term` |
| `geometry_algebra` | `traceback.cubic_tangent.iterate_x_n` | `differentiation -> coordinate_geometry -> tangent_line -> vieta_relations -> geometric_sequence -> recurrence -> general_term` |
| `geometry_algebra` | `traceback.cubic_tangent.log_growth_limit` | `differentiation -> coordinate_geometry -> tangent_line -> geometric_sequence -> recurrence -> general_term -> limit -> logarithm` |
| `geometry_algebra` | `traceback.cubic_tangent.midpoint_locus` | `differentiation -> coordinate_geometry -> tangent_line -> vieta_relations -> simultaneous_equations -> midpoint -> locus -> parameter_elimination` |
| `geometry_algebra` | `traceback.cubic_tangent.reintersection_x` | `differentiation -> coordinate_geometry -> tangent_line -> vieta_relations -> simultaneous_equations` |
| `geometry_analysis` | `deep.tangent_iteration_growth` | `differentiation -> coordinate_geometry -> tangent_line -> vieta_relations -> simultaneous_equations -> geometric_sequence -> recurrence -> general_term -> limit -> logarithm` |
| `graph_combinatorics_number_theory` | `ultradeep.paley_four_cycle_divisor_count` | `congruence -> integer_arithmetic -> square_number -> counting -> combination -> regular_polygon -> symmetry -> prime_factorization -> divisor_counting` |
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
| `number_theory_graph` | `layered.paley_triangle_count` | `congruence -> square_number -> counting -> combination` |
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
| `probability` | `construct.gambler_ruin_probability` | `probability -> recurrence_probability -> recurrence -> simultaneous_equations -> geometric_sequence -> general_term` |
| `probability` | `probability.left_to_right_maxima_expectation` | `probability -> expectation -> sum_of_series` |
| `probability` | `probability.random_bridge_zero_count` | `counting -> combination -> expectation -> sum_of_series` |
| `probability` | `traceback.dice_sum.modal_sum` | `probability -> polynomial_expansion -> counting -> combination` |
| `probability` | `traceback.dice_sum.modal_ways_divisor_count` | `probability -> polynomial_expansion -> counting -> combination -> prime_factorization -> divisor_counting` |
| `probability` | `traceback.dice_sum.prob_sum_divisible_by_3` | `probability -> polynomial_expansion -> counting -> roots_of_unity -> sum_of_series -> complex_plane` |
| `probability` | `traceback.dice_sum.total_outcomes` | `probability -> polynomial_expansion -> counting -> combination` |
| `probability` | `traceback.dice_sum.variance_times_12` | `probability -> polynomial_expansion -> counting -> variance -> expectation` |
| `probability` | `traceback.dice_sum.ways_for_modal_sum` | `probability -> polynomial_expansion -> counting -> combination` |
| `probability_linear_algebra_number_theory` | `ultradeep.gambler_absorption_variance_divisor_count` | `counting -> recurrence -> recurrence_probability -> simultaneous_equations -> probability -> expectation -> conditional_probability -> variance -> integer_arithmetic -> algebraic_identity -> prime_factorization -> divisor_counting` |
| `projective_geometry` | `ultradeep.geometry_ellipse_tangent_pair_locus` | `ellipse -> trigonometric_identity -> complex_plane -> parameter_elimination -> symmetry -> tangent_line -> line_equation -> simultaneous_equations -> de_moivre -> coordinate_geometry -> locus` |
| `real_analysis` | `analysis.boundary_layer_integral_limit` | `definite_integral -> area_integral -> algebraic_identity -> limit -> inequality` |
| `real_analysis` | `analysis.reflection_symmetric_integral` | `definite_integral -> symmetry -> vector_addition -> area_integral` |
| `real_analysis` | `asymptotic.recurrence_square_increment` | `square_number -> integer_arithmetic -> limit -> differentiation -> sequence -> quadratic_equation -> inequality` |
| `real_analysis` | `fusion.trig_absolute_value_integral` | `trigonometric_identity -> trigonometric_equation -> inequality -> definite_integral` |
| `real_analysis` | `fusion.trig_floor_integral` | `trigonometric_equation -> inequality -> counting -> definite_integral` |
