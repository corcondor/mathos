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
- 解答で初めて検出した潜在射: **72**

## 解答で初めて現れた射

`Differentiation` × 5, `Expectation` × 4, `CaseSplit` × 4, `Integral` × 4, `PercentOf` × 4, `RootSet` × 4, `Evaluation` × 3, `Map` × 3, `Derivative` × 3, `MonotonicityTest` × 3, `Limit` × 2, `FiniteSum` × 2, `Variance` × 2, `Factorial` × 2, `CoefficientComparison` × 2, `Discriminant` × 2, `Center` × 1, `Correlation` × 1, `Covariance` × 1, `InnerProduct` × 1, `Norm` × 1, `NormalizedInnerProduct` × 1, `ProbabilitySpace` × 1, `CoordinateSum` × 1, `FiniteShape` × 1, `Intersection` × 1, `Midpoint` × 1, `Polygon` × 1, `Cardinality` × 1, `FiniteProduct` × 1, `Distance` × 1, `Image` × 1, `Divides` × 1, `GCD` × 1, `ModResidue` × 1, `PowerMod` × 1, `ComplexConjugation` × 1, `PolynomialTranslation` × 1, `Distinct` × 1

## 問題別

| # | label | status | objects | morphisms | constraints | query | lift | answer units / edges / merges |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | 問題1 | type_checked | 4 | 4 | 8 | 2 | 0 | 99 / 53 / 9 |
| 2 | 問題2 | type_checked | 6 | 5 | 2 | 2 | 2 | 47 / 35 / 7 |
| 3 | 問題3 | type_checked | 4 | 11 | 2 | 1 | 1 | 123 / 152 / 48 |
| 4 | 問題4 | type_checked | 5 | 11 | 7 | 2 | 1 | 60 / 69 / 21 |
| 5 | 問題5 | needs_review | 0 | 1 | 2 | 2 | 0 | 108 / 84 / 22 |
| 6 | 問題6 | type_checked | 2 | 5 | 6 | 1 | 1 | 17 / 16 / 5 |
| 7 | 問題7 | type_checked | 9 | 9 | 13 | 1 | 1 | 33 / 58 / 19 |
| 8 | 問題8 | type_checked | 1 | 4 | 9 | 2 | 2 | 187 / 117 / 27 |
| 9 | 問題9 | type_checked | 1 | 2 | 2 | 2 | 1 | 20 / 13 / 3 |
| 10 | 問題10 | type_checked | 8 | 5 | 42 | 1 | 1 | 19 / 44 / 8 |
| 11 | 問題11 | type_checked | 6 | 5 | 8 | 1 | 1 | 41 / 36 / 9 |
| 12 | 問題12 | type_checked | 4 | 6 | 1 | 1 | 1 | - |
| 13 | 問題13 | type_checked | 8 | 7 | 8 | 1 | 0 | - |
| 14 | 問題14 | type_checked | 5 | 9 | 8 | 1 | 0 | - |
| 15 | 問題15 | type_checked | 7 | 4 | 3 | 2 | 1 | - |
| 16 | 問題16 | type_checked | 11 | 4 | 31 | 1 | 1 | - |
| 17 | 問題17 | type_checked | 1 | 2 | 4 | 1 | 0 | - |
| 18 | 問題18 | type_checked | 13 | 5 | 23 | 2 | 0 | - |
| 19 | 問題19 | type_checked | 7 | 3 | 10 | 1 | 0 | - |
| 20 | 問題20 | type_checked | 6 | 3 | 15 | 2 | 1 | - |
| 21 | 問題21 | type_checked | 8 | 11 | 12 | 2 | 2 | - |
| 22 | 問題22 | type_checked | 1 | 4 | 6 | 1 | 1 | - |
| 23 | 問題23 | type_checked | 4 | 5 | 3 | 2 | 1 | - |
| 24 | 問題24 | type_checked | 4 | 5 | 4 | 2 | 1 | - |
| 25 | 問題25 | type_checked | 5 | 6 | 23 | 1 | 1 | - |
| 26 | 問題26 | type_checked | 3 | 3 | 11 | 2 | 1 | - |
| 27 | 問題27 | type_checked | 10 | 4 | 2 | 1 | 1 | - |
| 28 | 問題28 | type_checked | 1 | 3 | 8 | 1 | 0 | - |
| 29 | 問題29 | type_checked | 4 | 4 | 13 | 1 | 0 | - |
| 30 | 問題30 | type_checked | 10 | 6 | 45 | 1 | 1 | - |
| 31 | 問題31 | type_checked | 8 | 9 | 36 | 1 | 1 | - |
| 32 | 問題32 | type_checked | 7 | 9 | 14 | 2 | 1 | - |
| 33 | 問題33 | type_checked | 3 | 5 | 4 | 1 | 1 | - |
| 34 | 問題34 | type_checked | 12 | 5 | 28 | 2 | 1 | - |
| 35 | 問題35 | type_checked | 4 | 6 | 16 | 2 | 0 | - |
| 36 | 問題36 | type_checked | 8 | 6 | 5 | 2 | 1 | - |
| 37 | 問題37 | type_checked | 9 | 6 | 5 | 2 | 2 | - |
| 38 | 問題38 | type_checked | 1 | 3 | 8 | 1 | 0 | - |
| 39 | 問題39 | type_checked | 5 | 5 | 5 | 2 | 1 | - |
| 40 | 問題40 | type_checked | 6 | 6 | 4 | 2 | 1 | - |
| 41 | 問題41 | type_checked | 5 | 5 | 3 | 1 | 0 | - |
| 42 | 問題42 | type_checked | 1 | 2 | 2 | 2 | 0 | - |
| 43 | 問題43 | type_checked | 5 | 6 | 14 | 1 | 0 | - |
| 44 | 問題44 | type_checked | 1 | 4 | 6 | 1 | 0 | - |
| 45 | 問題45 | type_checked | 5 | 5 | 3 | 2 | 1 | - |
| 46 | 問題46 | type_checked | 5 | 5 | 10 | 2 | 1 | - |
| 47 | 問題47 | type_checked | 2 | 5 | 11 | 2 | 1 | - |
| 48 | 問題48 | type_checked | 7 | 7 | 10 | 2 | 1 | - |
| 49 | 問題49 | type_checked | 3 | 6 | 5 | 2 | 1 | - |
| 50 | 問題49 | type_checked | 2 | 5 | 4 | 2 | 1 | - |
| 51 | 問題50 | type_checked | 5 | 5 | 5 | 2 | 1 | - |
| 52 | 問題51 | type_checked | 6 | 8 | 9 | 2 | 2 | - |
| 53 | 問題52 | type_checked | 4 | 5 | 6 | 2 | 1 | - |
| 54 | 問題53 | type_checked | 8 | 6 | 28 | 2 | 1 | - |
| 55 | 問題54 | type_checked | 7 | 9 | 23 | 1 | 2 | - |
| 56 | 問題55 | type_checked | 7 | 4 | 40 | 1 | 0 | - |
| 57 | 問題56 | type_checked | 3 | 6 | 3 | 1 | 1 | - |
| 58 | 問題57 | type_checked | 9 | 9 | 9 | 2 | 1 | - |
| 59 | 問題58 | type_checked | 5 | 6 | 3 | 2 | 1 | - |
| 60 | 問題59 | type_checked | 5 | 4 | 8 | 2 | 1 | - |
| 61 | 問題60 | type_checked | 5 | 5 | 3 | 1 | 1 | - |
| 62 | 問題61 | type_checked | 1 | 2 | 8 | 1 | 0 | - |
| 63 | 問題62 | type_checked | 6 | 6 | 11 | 2 | 1 | - |
| 64 | 問題63 | type_checked | 9 | 7 | 10 | 2 | 1 | - |
| 65 | 問題64 | type_checked | 8 | 7 | 7 | 2 | 0 | - |
| 66 | 問題65 | needs_review | 0 | 2 | 8 | 1 | 0 | - |
| 67 | 問題66 | type_checked | 3 | 4 | 8 | 2 | 2 | - |
| 68 | 問題65 | type_checked | 6 | 8 | 5 | 2 | 2 | - |
| 69 | 問題66 | type_checked | 4 | 8 | 2 | 1 | 2 | - |
| 70 | 問題67 | type_checked | 7 | 6 | 23 | 2 | 2 | - |
| 71 | 問題68 | type_checked | 2 | 4 | 6 | 1 | 0 | - |
| 72 | 問題69 | type_checked | 10 | 8 | 41 | 1 | 2 | - |
| 73 | 問題70 | type_checked | 6 | 6 | 27 | 2 | 1 | - |
| 74 | 問題71 | type_checked | 9 | 7 | 8 | 1 | 1 | - |
| 75 | 問題72 | type_checked | 6 | 6 | 23 | 1 | 2 | - |
| 76 | 問題73 | type_checked | 4 | 6 | 14 | 2 | 1 | - |
| 77 | 問題74 | type_checked | 3 | 6 | 8 | 3 | 1 | - |
| 78 | 問題75 | type_checked | 1 | 1 | 3 | 2 | 0 | - |
| 79 | 問題76 | type_checked | 9 | 6 | 7 | 1 | 1 | - |
| 80 | 問題61 | type_checked | 3 | 3 | 11 | 2 | 1 | - |
| 81 | 問題61 | type_checked | 4 | 3 | 8 | 2 | 0 | - |

## 注意

解答依存辺は、変数定義の参照と明示的な接続語から抽出した証拠グラフであり、論理的含意を形式証明したものではない。辺が少ない問題は、解答が簡単という意味ではなく、現行パーサが依存を回収できていない可能性を含む。
