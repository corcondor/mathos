# MathOS 大学受験数学プール監査

この文書は受験用配信プールから機械的に生成した記録である。
問題インスタンス数ではなく、数値変種を除いた構造数を数える。

## 結果

- 検証済み構造: **30**
- 構造族: **30**
- 幾何・代数・複素数系: **21**
- 高校の語彙へ書き換えた問題: **1**
- 同一構造の数値変種として除外: **7**（生成時点で潰しているため通常は 0）
- 高校の語彙へ還元できず除外: **6**
- 制約が合流しない2段合成として除外: **0**
- 複合分野なのに型付き経路がなく保留: **26**
- 経路はあるが条件が合流する証明DAGがなく保留: **0**
- 配信目的と合わず除外（サイコロ・ギャンブラー）: **26**
- スキップ票により公開プールから除外: **142**
- 旧難易度8.4未満（注釈のみ・除外しない）: **135**
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
| `algebra` | `polynomial.interpolation_harmonic_observable` | `polynomial_factorization -> simultaneous_equations -> roots_of_unity -> sum_of_series -> differentiation -> remainder_theorem` |
| `algebra` | `relation.polynomial_root_set.reciprocal_image` | `vieta_relations -> polynomial_factorization -> rational_function -> simultaneous_equations -> polynomial_expansion` |
| `algebra_inequality` | `relation.constrained_symmetric.product_reciprocal_prove_bound` | `inequality -> algebraic_identity -> simultaneous_equations -> polynomial_factorization` |
| `algebra_inequality` | `relation.constrained_symmetric.reciprocal_prove_bound` | `inequality -> algebraic_identity -> simultaneous_equations -> polynomial_factorization` |
| `algebraic_geometry` | `algebraic_geometry.cubic_discriminant_triangle_area` | `polynomial_factorization -> parabola -> coordinate_geometry -> area_shoelace -> quadratic_discriminant -> extremum -> differentiation` |
| `algebraic_geometry` | `algebraic_geometry.even_quartic_parabola_hull_area` | `polynomial_factorization -> parabola -> coordinate_geometry -> convex_hull -> area_shoelace -> extremum -> differentiation` |
| `analytic_geometry` | `conic_duality.tangent_intercept_centroid_minimum` | `tangent_line -> parameter_elimination -> line_equation -> coordinate_geometry -> midpoint -> complex_modulus -> distance_formula -> extremum -> differentiation` |
| `analytic_geometry` | `ultradeep.geometry_astroid_envelope_area` | `circle_equation -> ellipse -> coordinate_geometry -> line_equation -> parameter_elimination -> envelope -> differentiation -> parametric_curve -> area_integral -> definite_integral` |
| `complex_geometry` | `complex_geometry.reciprocal_root_polygon_area` | `complex_plane -> roots_of_unity -> symmetry -> counting -> convex_hull -> area_shoelace -> extremum -> differentiation` |
| `complex_geometry_algebra_combinatorics` | `morphology.unit_roots_antipodal_compatibility_count` | `regular_polygon -> complex_plane -> roots_of_unity -> vieta_relations -> algebraic_identity -> polynomial_factorization -> counting -> combination -> symmetry` |
| `complex_geometry_combinatorics_probability` | `morphology.cyclic_configuration_character_count` | `regular_polygon -> roots_of_unity -> complex_plane -> symmetry -> congruence -> periodicity -> sum_of_series -> polynomial_expansion -> counting -> combination -> probability -> expectation` |
| `conic_geometry` | `traceback.parabola_focal_chord.parameter_product` | `parabola -> hyperbola -> distance_formula -> parameter_elimination` |
| `convex_geometry` | `ultradeep.geometry_triangle_displacement_locus_area` | `coordinate_geometry -> triangle_area -> vector_addition -> locus -> convex_hull -> symmetry -> area_shoelace -> area_integral` |
| `differential_geometry` | `ultradeep.geometry_parabola_normal_envelope` | `parabola -> differentiation -> vector_addition -> normal_line -> parameter_elimination -> envelope -> extremum -> parametric_curve -> simultaneous_equations -> locus` |
| `euclidean_geometry` | `relation.triangle.sixty_degree_side_bound` | `sine_cosine_rule -> trigonometric_identity -> simultaneous_equations -> algebraic_identity -> polynomial_factorization -> inequality` |
| `euclidean_geometry` | `ultradeep.spatial_cube_diagonal_section_maximum` | `polyhedron -> solid_coordinate_geometry -> solid_vector -> inner_product -> solid_section -> inequality -> volume -> definite_integral -> counting -> algebraic_identity -> quadratic_extremum -> symmetry -> extremum` |
| `euclidean_geometry` | `ultradeep.spatial_tetrahedron_displacement_locus_volume` | `polyhedron -> solid_coordinate_geometry -> coordinate_geometry -> vector_addition -> solid_vector -> locus -> inequality -> volume -> counting -> combination` |
| `geometry` | `passage_region.parabola_family_sweep` | `parabola -> parameter_elimination -> quadratic_range -> area_integral` |
| `geometry_algebra_analysis` | `morphology.parabola_root_invariant_locus_extremum` | `parabola -> coordinate_geometry -> distance_formula -> simultaneous_equations -> polynomial_expansion -> quadratic_equation -> vieta_relations -> algebraic_identity -> tangent_line -> differentiation -> midpoint -> parameter_elimination -> locus -> extremum` |
| `number_theory` | `deep.recurrence_period_quadratic_character` | `recurrence -> general_term -> congruence -> periodicity -> prime_factorization -> square_number` |
| `number_theory` | `traceback.digit_power.leading_one_count` | `geometric_sequence -> exponential -> logarithm -> integer_arithmetic` |
| `probability` | `probability.random_bridge_zero_count` | `counting -> combination -> expectation -> sum_of_series` |
| `probability_algebra_analysis` | `motif.quadratic_root_lattice_limit` | `counting -> probability -> integer_arithmetic -> quadratic_discriminant -> inequality -> coordinate_geometry -> limit -> definite_integral -> area_integral -> quadratic_equation -> algebraic_identity -> sum_of_series` |
| `real_analysis` | `analysis.boundary_layer_integral_limit` | `definite_integral -> area_integral -> algebraic_identity -> limit -> inequality` |
| `real_analysis` | `asymptotic.recurrence_square_increment` | `square_number -> integer_arithmetic -> limit -> differentiation -> sequence -> quadratic_equation -> inequality` |
| `sequence` | `relation.sequence.affine_fixed_point_coordinate` | `recurrence -> function_composition -> simultaneous_equations -> geometric_sequence -> general_term -> inequality -> mathematical_induction` |
| `sequence_analysis` | `relation.iteration.error_squaring_coordinate` | `recurrence -> polynomial_expansion -> algebraic_identity -> exponential -> general_term -> limit` |
| `trigonometry` | `relation.triangle_angles.cos_sum_maximum` | `trigonometric_identity -> extremum -> differentiation` |
| `trigonometry` | `relation.triangle_angles.sin_product_maximum` | `trigonometric_identity -> extremum -> differentiation` |
