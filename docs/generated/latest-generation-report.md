# MathOS 自律作問・検証レポート

> この文書は `problem_synthesis/construct_pool.json` から機械的に生成される。
> 問題文や実績値を手作業で書き換えない。

## スナップショット

- 生成日時: `2026-07-25 21:38:40 +0000`
- 検証済み問題: **847問**
- 構造族: **24族**
- 深層族: **61問 / 10族**
- うち10射以上の超深層族: **34問 / 5族**
- 世界コーパス: **未記録問**

| 難易度帯 | 問題数 |
|---|---:|
| `A_olympiad` | 15 |
| `B_hard_university` | 538 |
| `C_standard_university` | 124 |
| `D_textbook` | 170 |

## 生成ループ

```text
型付き対象とパラメータを生成
  → 射を合成して観測量を定義
  → 専門backendで答を計算
  → 独立手段で反例・計算を照合
  → 世界コーパスとの衝突を検査
  → 難易度を推定
  → 合格候補だけを蓄積
```

直近ループの記録:

- 生成候補: 未記録
- 重複棄却: 未記録
- 新規性棄却: 未記録
- 検証失敗: 未記録
- 今回追加: 未記録

## 検証ゲート

| ゲート | 通過 |
|---|---:|
| backend計算 | 847/847 |
| 独立検証 | 847/847 |
| LiftCertificate型検査 | 847/847 |
| コーパス新規性 | 847/847 |

## 深層族の生成例

深層族は1問につき8個以上、超深層族は10〜12個の射を合成する。以下は各族で難易度推定値が
最も高い実データであり、説明用に新しく書き直した問題ではない。

### `deep.paley_spectrum_triangles`

- 難易度: `B_hard_university` / score `13.22`
- backend: `quadratic_residue+spectral+counting`
- 独立検証: `adjacency_trace_vs_exhaustive_triangle_count`
- 最大表層類似度: `0.0898`
- 射: `PrimeField → QuadraticResidueSet → PaleyGraph → AdjacencyMatrix → MatrixCube → ClosedWalkCount → TriangleCount → TraceInvariant`

**問題**

素数 \(p=97\)（\(p\equiv1\pmod4\)）に対し，頂点集合 \(\mathbb Z_{97}\) 上のグラフ \(G\) を，2頂点 \(x,y\) が \(x-y\) が平方剰余のとき辺で結ぶことで定める。\(G\) の隣接行列を \(A\) とするとき，\(\operatorname{tr}(A^3)\) を求めよ。

**答**: 107088

<details>
<summary>検証済み解法記録</summary>

\(\operatorname{tr}(A^3)\) は長さ3の閉じた歩道の総数で，三角形1個が6回数えられる。この \(G\) では各辺の共通隣接点が \((p-5)/4\) 個なので三角形は \(\frac{p(p-1)(p-5)}{48}=17848\) 個。よって \(\operatorname{tr}(A^3)=6\times17848=107088\)。

</details>

### `deep.polygon_subset_centroid`

- 難易度: `C_standard_university` / score `7.49`
- backend: `roots_of_unity+subset_enumeration`
- 独立検証: `exhaustive_subset_vanishing_sum_count`
- 最大表層類似度: `0.1078`
- 射: `RootOfUnity → RegularPolygon → SubsetFamily → CentroidMap → VanishingSum → CyclotomicRelation → SymmetryReduction → SubsetCount`

**問題**

単位円に内接する正 \(12\) 角形の頂点を \(z_j=\cos\frac{2\pi j}{12}+i\sin\frac{2\pi j}{12}\ (j=0,1,\ldots,11)\) とする。空でない部分集合 \(S\) であって，\(S\) に属する頂点の重心が円の中心と一致するものの個数を求めよ。

**答**: 99

<details>
<summary>検証済み解法記録</summary>

重心が中心であることは \(\sum_{j\in S}z_j=0\) と同値。\(z_j\) は1の \(12\) 乗根なので，和が消える部分集合を数えればよい。巡回対称性から，正多角形をなす頂点集合とその合併が条件を満たす。

</details>

### `deep.recurrence_period_quadratic_character`

- 難易度: `A_olympiad` / score `16.64`
- backend: `matrix_mod_order+legendre_symbol`
- 独立検証: `modular_period_then_euler_criterion`
- 最大表層類似度: `0.1674`
- 射: `LinearRecurrence → CompanionMatrix → ModularReduction → MultiplicativeOrder → MinimalPeriod → PrimeFactorization → EulerCriterion → LegendreSymbol`

**問題**

数列 \((a_n)\) を \(a_0=0,\ a_1=1,\ a_{n+2}=a_{n+1}+a_n\) で定める。\((a_n)\) を \(\bmod\ 13\) で見たときの最小周期を \(T\) とし，\(T\) の最大の素因数を \(q\) とする。ルジャンドル記号 \(\left(\dfrac{q}{13}\right)\) の値を求めよ。

**答**: -1

<details>
<summary>検証済み解法記録</summary>

\((a_{n+1},a_n)\) は随伴行列 \(\begin{pmatrix}1&1\\1&0\end{pmatrix}\) を掛けて進むので，\(\bmod\ 13\) でのこの行列の位数が周期 \(T=28\)。その最大素因数は \(q=7\)。オイラーの規準 \(q^{(13-1)/2}\equiv-1\pmod{13}\) より \(\left(\frac{7}{13}\right)=-1\)。

</details>

### `deep.rotation_diagonal_product_divisors`

- 難易度: `B_hard_university` / score `12.45`
- backend: `roots_of_unity+product+divisor_function`
- 独立検証: `cyclotomic_product_identity_plus_numeric_check`
- 最大表層類似度: `0.1078`
- 射: `RootOfUnity → RegularPolygon → VertexDistances → PolynomialFactorization → LimitEvaluation → DistanceProduct → IntegerValue → DivisorCount`

**問題**

単位円に内接する正 \(12\) 角形の頂点を \(z_j=\cos\frac{2\pi j}{12}+i\sin\frac{2\pi j}{12}\ (j=0,1,\ldots,11)\) とする。頂点 \(z_0\) から他の \(11\) 個の頂点までの距離の積を \(L\) とするとき，\(L\) の正の約数の個数を求めよ。

**答**: 6

<details>
<summary>検証済み解法記録</summary>

\(z^{12}-1=\prod_{j=0}^{11}(z-z_j)\) の両辺を \(z-1\) で割り \(z\to1\) とすると \(\prod_{j=1}^{11}(1-z_j)=12\)。絶対値をとって \(L=12\)。よって約数の個数は \(6\)。

</details>

### `deep.tangent_iteration_growth`

- 難易度: `B_hard_university` / score `11.00`
- backend: `symbolic_intersection+iteration+limit`
- 独立検証: `tangent_iteration_ratio_then_log_limit`
- 最大表層類似度: `0.1475`
- 射: `CubicCurve → TangentLine → Reintersection → RootSumRelation → GeometricIteration → GeneralTerm → GrowthRate → LogarithmicLimit`

**問題**

曲線 \(C: y=x^{3} - 9 x\) 上に点 \(P_0(t,\,t^{3} - 9 t)\)（\(t>0\)）をとる。\(P_i\) における \(C\) の接線が \(C\) と再び交わる点を \(P_{i+1}\) と定め，\(P_n\) の \(x\) 座標を \(x_n\) とする。極限 \(\displaystyle\lim_{n\to\infty}\frac{\log|x_n|}{n}\) を求めよ。

**答**: \log{\left(2 \right)}

<details>
<summary>検証済み解法記録</summary>

接点で重根をもつことと三次方程式の根の和の関係から \(x_{i+1}=-2x_i\)。したがって \(x_n=(-2)^n t\)，\(|x_n|=2^n|t|\)。\(\frac{\log|x_n|}{n}=\log 2+\frac{\log|t|}{n}\to\log 2\)。

</details>

### `ultradeep.cubic_root_triangle_discriminant_divisor_count`

- 難易度: `B_hard_university` / score `13.92`
- backend: `cubic_discriminant+vandermonde_area+numeric_roots`
- 独立検証: `symbolic_discriminant_identity_vs_numeric_root_triangle_area`
- 最大表層類似度: `0.1354`
- 射: `CubicPolynomial → ThreeRealRootSet → ParabolaEmbedding → TriangleConstruction → VandermondeDeterminant → AreaSquare → PolynomialDiscriminant → IntegerNormalization → PrimeFactorization → DivisorCount → ArithmeticObservation`

**問題**

方程式 \(x^3-48x+(-16)=0\) の3実根を \(\alpha,\beta,\gamma\) とする。放物線 \(y=x^2\) 上の3点 \((\alpha,\alpha^2),(\beta,\beta^2),(\gamma,\gamma^2)\) が作る三角形の面積を \(S\) とし，\(M=\frac{4S^2}{27}\) と定める。\(M\) が整数であることを示し，\(M\) の正の約数の個数を求めよ。

**答**: 54

<details>
<summary>検証済み解法記録</summary>

Vandermonde 行列式から \(4S^2\) は三次式の判別式に等しい。判別式は \(27(4\cdot 4^6-(-16)^2)=27\cdot 16128\) だから \(M=16128=2^{8}\cdot 3^{2}\cdot 7\)。したがって正の約数は \(54\) 個。

</details>

### `ultradeep.cyclotomic_distance_norm_divisor_count`

- 難易度: `A_olympiad` / score `14.97`
- backend: `cyclotomic_polynomial+algebraic_norm+numeric_product`
- 独立検証: `cyclotomic_evaluation_vs_numeric_primitive_root_product`
- 最大表層類似度: `0.1111`
- 射: `RootOfUnity → CoprimeIndexFilter → PrimitiveRootSet → DistanceMultiset → DistanceProduct → CyclotomicPolynomial → PolynomialEvaluation → AlgebraicNorm → IntegerInvariant → PrimeFactorization → DivisorCount`

**問題**

\(\zeta_j=\cos\frac{2\pi j}{9}+i\sin\frac{2\pi j}{9}\) とし，\(1\le j\le 9\) かつ \(\gcd(j,9)=1\) を満たす \(j\) について \(L=\prod |4-\zeta_j|\) と定める。\(L\) が整数であることを示し，\(L\) の正の約数の個数を求めよ。

**答**: 8

<details>
<summary>検証済み解法記録</summary>

積に現れるのは原始 \(9\) 乗根だから，\(\prod(4-\zeta_j)=\Phi_{9}(4)=4161\)。共役が対になるので絶対値の積も \(L=4161\)。\(L=3\cdot 19\cdot 73\) より，正の約数は \(8\) 個。

</details>

### `ultradeep.gambler_absorption_variance_divisor_count`

- 難易度: `C_standard_university` / score `7.59`
- backend: `absorbing_markov_moments+linear_system+factorization`
- 独立検証: `closed_variance_formula_vs_exact_two_moment_linear_system`
- 最大表層類似度: `0.0773`
- 射: `PathStateSpace → AbsorbingBoundary → SymmetricRandomWalk → HittingTime → FirstMomentConditioning → FirstMomentLinearSystem → SecondMomentConditioning → SecondMomentLinearSystem → VarianceTransform → IntegerInvariant → PrimeFactorization → DivisorCount`

**問題**

点 \(0,1,\ldots,12\) 上を動く対称ランダムウォークを考える。初期位置は \(3\) で，各時刻に確率 \(\frac12\) ずつで左右に1動き，\(0\) または \(12\) に着いたら停止する。停止時刻を \(T\) とするとき，\(\operatorname{Var}(T)\) の正の約数の個数を求めよ。

**答**: 24

<details>
<summary>検証済み解法記録</summary>

一次モーメントの差分方程式から \(E[T]=3(12-3)\)。二次モーメントにも条件付けして解くと \(\operatorname{Var}(T)=\frac{3(12-3)(12^2-2-2\cdot 3(12-3))}{3}=792\)。\(792=2^{3}\cdot 3^{2}\cdot 11\) より約数は \(24\) 個。

</details>

### `ultradeep.paley_four_cycle_divisor_count`

- 難易度: `B_hard_university` / score `9.38`
- backend: `strongly_regular_graph+trace_four+factorization`
- 独立検証: `common_neighbor_double_count_vs_adjacency_trace_four`
- 最大表層類似度: `0.1176`
- 射: `PrimeField → QuadraticResidueSet → PaleyGraph → StronglyRegularParameters → CommonNeighborRelation → OppositeVertexPairing → FourCycleDoubleCount → CycleCount → PrimeFactorization → DivisorCount`

**問題**

素数 \(p=29\) に対し，頂点集合 \(\mathbb Z_{29}\) 上で，\(x-y\) が平方剰余であるときに \(x,y\) を結んで得られる Paley グラフを \(G\) とする。\(G\) に含まれる単純な長さ4の閉路の個数を \(C\) とする。\(C\) の正の約数の個数を求めよ。

**答**: 24

<details>
<summary>検証済み解法記録</summary>

隣接2頂点の共通隣接点は \(6\) 個，非隣接2頂点では \(7\) 個。向かい合う頂点対で二重計数すると \(C=3654\)。\(C=2\cdot 3^{2}\cdot 7\cdot 29\) なので，正の約数は \(24\) 個。

</details>

### `ultradeep.paley_spanning_tree_divisor_count`

- 難易度: `B_hard_university` / score `12.95`
- backend: `paley_spectrum+matrix_tree+exact_determinant`
- 独立検証: `spectral_tree_formula_vs_exact_laplacian_cofactor`
- 最大表層類似度: `0.1216`
- 射: `PrimeField → QuadraticResidueSet → PaleyGraph → AdjacencyMatrix → AdjacencySpectrum → LaplacianTransform → LaplacianSpectrum → NonzeroEigenvalueProduct → MatrixTreeTheorem → SpanningTreeCount → PrimeFactorization → DivisorCount`

**問題**

素数 \(p=29\) に対し，頂点集合 \(\mathbb Z_{29}\) 上で，\(x-y\) が平方剰余であるときに \(x,y\) を結んで得られる Paley グラフを \(G\) とする。\(G\) の全域木の個数を \(\tau\) とするとき，\(\tau\) の正の約数の個数を求めよ。

**答**: 210

<details>
<summary>検証済み解法記録</summary>

Paley グラフの隣接行列の非自明固有値は \(\frac{-1\pm\sqrt{29}}2\)（各重複度 \(14\)）。次数 \(14\) のラプラシアンの非零固有値の積を Kirchhoff の定理で\(29\) で割ると \(\tau=29^{13}\left(\frac{29-1}4\right)^{14}=7^{14}\cdot 29^{13}\)。したがって約数の個数は \(210\)。

</details>

## 解釈上の注意

- `A_olympiad` などの難易度は人手採点ではなく、176問で較正した推定器の出力。
- `corpus_novel=true` は登録コーパス内での衝突がないことを示し、
  数学史上まったく新しいことの証明ではない。
- `exact_backend` と `independent_check` は生成器の検査契約であり、
  Leanによる全問の形式証明を意味しない。
- したがって、正しさ・新規性・難易度を同じ一語の「良問」でまとめず、
  それぞれ別の指標として追跡する。
