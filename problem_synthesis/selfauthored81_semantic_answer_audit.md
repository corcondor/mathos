# 全問題.tex 構文・意味・解答依存監査

- 問題: **81**
- 解答を対応付けた問題: **11**
- 意味グラフ type_checked: **79**
- query 抽出: **81**
- constraint 抽出: **81**
- LiftCertificate: **59**
- Lift不能: **22** ([1, 5, 13, 14, 17, 18, 19, 28, 29, 35, 38, 41, 42, 43, 44, 56, 62, 65, 66, 71, 78, 81])
- 解答の論証単位: **754**
- 抽出した依存辺: **677**
- 複数依存が合流した節点: **178**
- 解答で初めて検出した潜在射: **77**

## 解答で初めて現れた射

`Differentiation` × 5, `Expectation` × 4, `CaseSplit` × 4, `Integral` × 4, `PercentOf` × 4, `RootSet` × 4, `Evaluation` × 3, `Map` × 3, `Derivative` × 3, `MonotonicityTest` × 3, `Limit` × 2, `FiniteSum` × 2, `RestrictedAverage` × 2, `Variance` × 2, `Factorial` × 2, `CoefficientComparison` × 2, `Discriminant` × 2, `QuadraticDiscriminant` × 2, `Center` × 1, `Correlation` × 1, `Covariance` × 1, `InnerProduct` × 1, `Norm` × 1, `NormalizedInnerProduct` × 1, `ProbabilitySpace` × 1, `CoordinateSum` × 1, `FiniteShape` × 1, `Intersection` × 1, `Midpoint` × 1, `Polygon` × 1, `Cardinality` × 1, `FiniteProduct` × 1, `RegionLimit` × 1, `Distance` × 1, `Image` × 1, `Divides` × 1, `GCD` × 1, `ModResidue` × 1, `PowerMod` × 1, `ComplexConjugation` × 1, `PolynomialTranslation` × 1, `Distinct` × 1

## 作問構想の横断レンズ

これは完成解法のfamily分類ではなく、問題文と意味グラフから得た横断的な構想証拠である。
解答未収録の問題では理論背景は仮説であり、証明済みとは扱わない。

| lens | problems |
|---|---:|
| `arithmetic_rigidity` | 43 |
| `discrete_continuous_bridge` | 42 |
| `inverse_existence_design` | 39 |
| `boundary_extremum` | 31 |
| `moving_configuration_to_global_region` | 26 |
| `iteration_and_fixed_structure` | 26 |
| `asymptotic_renormalization` | 19 |
| `symmetry_to_dimension_reduction` | 11 |
| `representation_change` | 10 |

## 問題別

| # | label | design lenses | status | objects | morphisms | constraints | query | lift | answer units / edges / merges |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| 1 | 問題1 | discrete_continuous_bridge | type_checked | 4 | 4 | 8 | 2 | 0 | 99 / 53 / 9 |
| 2 | 問題2 | moving_configuration_to_global_region, discrete_continuous_bridge, iteration_and_fixed_structure, boundary_extremum, asymptotic_renormalization | type_checked | 6 | 5 | 2 | 2 | 2 | 47 / 35 / 7 |
| 3 | 問題3 | discrete_continuous_bridge, iteration_and_fixed_structure, arithmetic_rigidity, asymptotic_renormalization | type_checked | 4 | 11 | 2 | 1 | 1 | 123 / 152 / 48 |
| 4 | 問題4 | discrete_continuous_bridge, iteration_and_fixed_structure, arithmetic_rigidity, asymptotic_renormalization | type_checked | 5 | 11 | 7 | 2 | 1 | 60 / 69 / 21 |
| 5 | 問題5 | - | needs_review | 0 | 1 | 2 | 2 | 0 | 108 / 84 / 22 |
| 6 | 問題6 | arithmetic_rigidity, inverse_existence_design | type_checked | 2 | 5 | 6 | 1 | 1 | 17 / 16 / 5 |
| 7 | 問題7 | moving_configuration_to_global_region, symmetry_to_dimension_reduction, boundary_extremum, inverse_existence_design | type_checked | 9 | 9 | 13 | 1 | 1 | 33 / 58 / 19 |
| 8 | 問題8 | boundary_extremum | type_checked | 1 | 4 | 9 | 2 | 2 | 187 / 117 / 27 |
| 9 | 問題9 | discrete_continuous_bridge, iteration_and_fixed_structure, asymptotic_renormalization | type_checked | 1 | 2 | 2 | 2 | 1 | 20 / 13 / 3 |
| 10 | 問題10 | representation_change, iteration_and_fixed_structure, arithmetic_rigidity, inverse_existence_design | type_checked | 8 | 5 | 42 | 1 | 1 | 19 / 44 / 8 |
| 11 | 問題11 | discrete_continuous_bridge, iteration_and_fixed_structure, asymptotic_renormalization, inverse_existence_design | type_checked | 6 | 5 | 8 | 1 | 1 | 41 / 36 / 9 |
| 12 | 問題12 | moving_configuration_to_global_region, symmetry_to_dimension_reduction, boundary_extremum | type_checked | 4 | 6 | 1 | 1 | 1 | - |
| 13 | 問題13 | moving_configuration_to_global_region, representation_change, arithmetic_rigidity, inverse_existence_design | type_checked | 8 | 7 | 8 | 1 | 0 | - |
| 14 | 問題14 | discrete_continuous_bridge, arithmetic_rigidity, inverse_existence_design | type_checked | 5 | 9 | 8 | 1 | 0 | - |
| 15 | 問題15 | moving_configuration_to_global_region, boundary_extremum | type_checked | 7 | 4 | 3 | 2 | 1 | - |
| 16 | 問題16 | moving_configuration_to_global_region, discrete_continuous_bridge, iteration_and_fixed_structure, boundary_extremum, asymptotic_renormalization, inverse_existence_design | type_checked | 11 | 4 | 31 | 1 | 1 | - |
| 17 | 問題17 | - | type_checked | 1 | 2 | 4 | 1 | 0 | - |
| 18 | 問題18 | representation_change, iteration_and_fixed_structure, arithmetic_rigidity | type_checked | 13 | 5 | 23 | 2 | 0 | - |
| 19 | 問題19 | symmetry_to_dimension_reduction, arithmetic_rigidity, inverse_existence_design | type_checked | 7 | 3 | 10 | 1 | 0 | - |
| 20 | 問題20 | discrete_continuous_bridge, iteration_and_fixed_structure, asymptotic_renormalization | type_checked | 6 | 3 | 15 | 2 | 1 | - |
| 21 | 問題21 | moving_configuration_to_global_region, discrete_continuous_bridge, representation_change, arithmetic_rigidity, boundary_extremum | type_checked | 8 | 11 | 12 | 2 | 2 | - |
| 22 | 問題22 | arithmetic_rigidity, inverse_existence_design | type_checked | 1 | 4 | 6 | 1 | 1 | - |
| 23 | 問題23 | moving_configuration_to_global_region, discrete_continuous_bridge, arithmetic_rigidity, boundary_extremum | type_checked | 4 | 5 | 3 | 2 | 1 | - |
| 24 | 問題24 | moving_configuration_to_global_region, discrete_continuous_bridge, arithmetic_rigidity, boundary_extremum | type_checked | 4 | 5 | 4 | 2 | 1 | - |
| 25 | 問題25 | discrete_continuous_bridge, representation_change, arithmetic_rigidity | type_checked | 5 | 6 | 23 | 1 | 1 | - |
| 26 | 問題26 | discrete_continuous_bridge, iteration_and_fixed_structure, asymptotic_renormalization | type_checked | 3 | 3 | 11 | 2 | 1 | - |
| 27 | 問題27 | moving_configuration_to_global_region, symmetry_to_dimension_reduction, boundary_extremum, inverse_existence_design | type_checked | 10 | 4 | 2 | 1 | 1 | - |
| 28 | 問題28 | discrete_continuous_bridge, inverse_existence_design | type_checked | 1 | 3 | 8 | 1 | 0 | - |
| 29 | 問題29 | discrete_continuous_bridge, iteration_and_fixed_structure, inverse_existence_design | type_checked | 4 | 4 | 13 | 1 | 0 | - |
| 30 | 問題30 | discrete_continuous_bridge, iteration_and_fixed_structure, arithmetic_rigidity, asymptotic_renormalization, inverse_existence_design | type_checked | 10 | 6 | 45 | 1 | 1 | - |
| 31 | 問題31 | discrete_continuous_bridge, representation_change, arithmetic_rigidity, inverse_existence_design | type_checked | 8 | 9 | 36 | 1 | 1 | - |
| 32 | 問題32 | discrete_continuous_bridge, symmetry_to_dimension_reduction, iteration_and_fixed_structure, asymptotic_renormalization | type_checked | 7 | 9 | 14 | 2 | 1 | - |
| 33 | 問題33 | discrete_continuous_bridge, arithmetic_rigidity, inverse_existence_design | type_checked | 3 | 5 | 4 | 1 | 1 | - |
| 34 | 問題34 | moving_configuration_to_global_region, discrete_continuous_bridge, arithmetic_rigidity, boundary_extremum | type_checked | 12 | 5 | 28 | 2 | 1 | - |
| 35 | 問題35 | arithmetic_rigidity, inverse_existence_design | type_checked | 4 | 6 | 16 | 2 | 0 | - |
| 36 | 問題36 | discrete_continuous_bridge, representation_change, iteration_and_fixed_structure, asymptotic_renormalization | type_checked | 8 | 6 | 5 | 2 | 1 | - |
| 37 | 問題37 | moving_configuration_to_global_region, discrete_continuous_bridge, representation_change, iteration_and_fixed_structure, boundary_extremum, asymptotic_renormalization | type_checked | 9 | 6 | 5 | 2 | 2 | - |
| 38 | 問題38 | discrete_continuous_bridge, inverse_existence_design | type_checked | 1 | 3 | 8 | 1 | 0 | - |
| 39 | 問題39 | discrete_continuous_bridge, arithmetic_rigidity, inverse_existence_design | type_checked | 5 | 5 | 5 | 2 | 1 | - |
| 40 | 問題40 | discrete_continuous_bridge, iteration_and_fixed_structure, arithmetic_rigidity, asymptotic_renormalization | type_checked | 6 | 6 | 4 | 2 | 1 | - |
| 41 | 問題41 | moving_configuration_to_global_region, boundary_extremum, inverse_existence_design | type_checked | 5 | 5 | 3 | 1 | 0 | - |
| 42 | 問題42 | - | type_checked | 1 | 2 | 2 | 2 | 0 | - |
| 43 | 問題43 | discrete_continuous_bridge, arithmetic_rigidity, inverse_existence_design | type_checked | 5 | 6 | 14 | 1 | 0 | - |
| 44 | 問題44 | discrete_continuous_bridge, arithmetic_rigidity, inverse_existence_design | type_checked | 1 | 4 | 6 | 1 | 0 | - |
| 45 | 問題45 | discrete_continuous_bridge, arithmetic_rigidity, boundary_extremum | type_checked | 5 | 5 | 3 | 2 | 1 | - |
| 46 | 問題46 | discrete_continuous_bridge, arithmetic_rigidity | type_checked | 5 | 5 | 10 | 2 | 1 | - |
| 47 | 問題47 | arithmetic_rigidity | type_checked | 2 | 5 | 11 | 2 | 1 | - |
| 48 | 問題48 | discrete_continuous_bridge, arithmetic_rigidity, inverse_existence_design | type_checked | 7 | 7 | 10 | 2 | 1 | - |
| 49 | 問題49 | discrete_continuous_bridge, arithmetic_rigidity, inverse_existence_design | type_checked | 3 | 6 | 5 | 2 | 1 | - |
| 50 | 問題49 | discrete_continuous_bridge, arithmetic_rigidity, inverse_existence_design | type_checked | 2 | 5 | 4 | 2 | 1 | - |
| 51 | 問題50 | iteration_and_fixed_structure, arithmetic_rigidity, inverse_existence_design | type_checked | 5 | 5 | 5 | 2 | 1 | - |
| 52 | 問題51 | moving_configuration_to_global_region, discrete_continuous_bridge, arithmetic_rigidity, boundary_extremum, inverse_existence_design | type_checked | 6 | 8 | 9 | 2 | 2 | - |
| 53 | 問題52 | arithmetic_rigidity, inverse_existence_design | type_checked | 4 | 5 | 6 | 2 | 1 | - |
| 54 | 問題53 | iteration_and_fixed_structure, arithmetic_rigidity, inverse_existence_design | type_checked | 8 | 6 | 28 | 2 | 1 | - |
| 55 | 問題54 | discrete_continuous_bridge, arithmetic_rigidity, inverse_existence_design | type_checked | 7 | 9 | 23 | 1 | 2 | - |
| 56 | 問題55 | iteration_and_fixed_structure, arithmetic_rigidity, inverse_existence_design | type_checked | 7 | 4 | 40 | 1 | 0 | - |
| 57 | 問題56 | moving_configuration_to_global_region, boundary_extremum, inverse_existence_design | type_checked | 3 | 6 | 3 | 1 | 1 | - |
| 58 | 問題57 | moving_configuration_to_global_region, symmetry_to_dimension_reduction, boundary_extremum | type_checked | 9 | 9 | 9 | 2 | 1 | - |
| 59 | 問題58 | moving_configuration_to_global_region, symmetry_to_dimension_reduction, boundary_extremum | type_checked | 5 | 6 | 3 | 2 | 1 | - |
| 60 | 問題59 | moving_configuration_to_global_region, boundary_extremum | type_checked | 5 | 4 | 8 | 2 | 1 | - |
| 61 | 問題60 | discrete_continuous_bridge, arithmetic_rigidity | type_checked | 5 | 5 | 3 | 1 | 1 | - |
| 62 | 問題61 | inverse_existence_design | type_checked | 1 | 2 | 8 | 1 | 0 | - |
| 63 | 問題62 | boundary_extremum | type_checked | 6 | 6 | 11 | 2 | 1 | - |
| 64 | 問題63 | boundary_extremum | type_checked | 9 | 7 | 10 | 2 | 1 | - |
| 65 | 問題64 | boundary_extremum | type_checked | 8 | 7 | 7 | 2 | 0 | - |
| 66 | 問題65 | inverse_existence_design | needs_review | 0 | 2 | 8 | 1 | 0 | - |
| 67 | 問題66 | discrete_continuous_bridge, iteration_and_fixed_structure, arithmetic_rigidity, boundary_extremum, asymptotic_renormalization | type_checked | 3 | 4 | 8 | 2 | 2 | - |
| 68 | 問題65 | moving_configuration_to_global_region, boundary_extremum | type_checked | 6 | 8 | 5 | 2 | 2 | - |
| 69 | 問題66 | moving_configuration_to_global_region, symmetry_to_dimension_reduction, boundary_extremum | type_checked | 4 | 8 | 2 | 1 | 2 | - |
| 70 | 問題67 | moving_configuration_to_global_region, boundary_extremum | type_checked | 7 | 6 | 23 | 2 | 2 | - |
| 71 | 問題68 | arithmetic_rigidity, inverse_existence_design | type_checked | 2 | 4 | 6 | 1 | 0 | - |
| 72 | 問題69 | moving_configuration_to_global_region, discrete_continuous_bridge, representation_change, iteration_and_fixed_structure, arithmetic_rigidity, boundary_extremum, asymptotic_renormalization, inverse_existence_design | type_checked | 10 | 8 | 41 | 1 | 2 | - |
| 73 | 問題70 | arithmetic_rigidity, inverse_existence_design | type_checked | 6 | 6 | 27 | 2 | 1 | - |
| 74 | 問題71 | moving_configuration_to_global_region, discrete_continuous_bridge, symmetry_to_dimension_reduction, iteration_and_fixed_structure, boundary_extremum, asymptotic_renormalization | type_checked | 9 | 7 | 8 | 1 | 1 | - |
| 75 | 問題72 | moving_configuration_to_global_region, discrete_continuous_bridge, representation_change, iteration_and_fixed_structure, arithmetic_rigidity, boundary_extremum, asymptotic_renormalization, inverse_existence_design | type_checked | 6 | 6 | 23 | 1 | 2 | - |
| 76 | 問題73 | moving_configuration_to_global_region, boundary_extremum, inverse_existence_design | type_checked | 4 | 6 | 14 | 2 | 1 | - |
| 77 | 問題74 | symmetry_to_dimension_reduction, arithmetic_rigidity, inverse_existence_design | type_checked | 3 | 6 | 8 | 3 | 1 | - |
| 78 | 問題75 | iteration_and_fixed_structure | type_checked | 1 | 1 | 3 | 2 | 0 | - |
| 79 | 問題76 | moving_configuration_to_global_region, discrete_continuous_bridge, symmetry_to_dimension_reduction, iteration_and_fixed_structure, arithmetic_rigidity, boundary_extremum, asymptotic_renormalization | type_checked | 9 | 6 | 7 | 1 | 1 | - |
| 80 | 問題61 | discrete_continuous_bridge, iteration_and_fixed_structure, asymptotic_renormalization | type_checked | 3 | 3 | 11 | 2 | 1 | - |
| 81 | 問題61 | arithmetic_rigidity | type_checked | 4 | 3 | 8 | 2 | 0 | - |

## 注意

解答依存辺は、変数定義の参照と明示的な接続語から抽出した証拠グラフであり、論理的含意を形式証明したものではない。辺が少ない問題は、解答が簡単という意味ではなく、現行パーサが依存を回収できていない可能性を含む。
