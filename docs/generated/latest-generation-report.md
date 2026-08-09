# MathOS 自律作問・検証レポート

> この文書は `problem_synthesis/construct_pool.json` から機械的に生成される。
> 問題文や実績値を手作業で書き換えない。

## スナップショット

- 生成日時: `2026-08-09 06:51:14 +0000`
- 検証済み問題インスタンス: **102問**
- 構造族: **99族**
- 深層族: **20問 / 20族**
- うち10射以上の超深層族: **15問 / 15族**
- 世界コーパス: **未記録問**

| 難易度帯 | 問題数 |
|---|---:|
| `A` | 31 |
| `A_olympiad` | 1 |
| `B_hard_university` | 10 |
| `C_standard_university` | 26 |
| `D_textbook` | 34 |

ここで問題インスタンス数は、同じ構造族のパラメータ違いを含む。
創造性・構造多様性はインスタンス数ではなく構造族数と射列で評価する。

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
| backend計算 | 102/102 |
| 独立検証 | 102/102 |
| LiftCertificate型検査 | 102/102 |
| コーパス新規性 | 102/102 |

## 深層族の生成例

深層族は1問につき8個以上、超深層族は10〜12個の射を合成する。以下は各族で難易度推定値が
最も高い実データであり、説明用に新しく書き直した問題ではない。

### `deep.paley_spectrum_triangles`

- 難易度: `A` / score `0.00`
- backend: `quadratic_residue+spectral+counting`
- 独立検証: `adjacency_trace_vs_exhaustive_triangle_count`
- 最大表層類似度: `0.0`
- 射: `PrimeField → QuadraticResidueSet → PaleyGraph → AdjacencyMatrix → MatrixCube → ClosedWalkCount → TriangleCount → TraceInvariant`

**問題**

素数 \(p=13\)（\(p\equiv1\pmod4\)）に対し，頂点集合 \(\mathbb Z_{13}\) 上のグラフ \(G\) を，2頂点 \(x,y\) が \(x-y\) が平方剰余のとき辺で結ぶことで定める。\(G\) の隣接行列を \(A\) とするとき，\(\operatorname{tr}(A^3)\) を求めよ。

**答**: 156

<details>
<summary>検証済み解法記録</summary>

\(\operatorname{tr}(A^3)\) は長さ3の閉じた歩道の総数で，三角形1個が6回数えられる。この \(G\) では各辺の共通隣接点が \((p-5)/4\) 個なので三角形は \(\frac{p(p-1)(p-5)}{48}=26\) 個。よって \(\operatorname{tr}(A^3)=6\times26=156\)。

</details>

### `deep.polygon_subset_centroid`

- 難易度: `A` / score `0.00`
- backend: `roots_of_unity+subset_enumeration`
- 独立検証: `exhaustive_subset_vanishing_sum_count`
- 最大表層類似度: `0.0`
- 射: `RootOfUnity → RegularPolygon → SubsetFamily → CentroidMap → VanishingSum → CyclotomicRelation → SymmetryReduction → SubsetCount`

**問題**

単位円に内接する正 \(3\) 角形の頂点を \(z_j=\cos\frac{2\pi j}{3}+i\sin\frac{2\pi j}{3}\ (j=0,1,\ldots,2)\) とする。空でない部分集合 \(S\) であって，\(S\) に属する頂点の重心が円の中心と一致するものの個数を求めよ。

**答**: 1

<details>
<summary>検証済み解法記録</summary>

重心が中心であることは \(\sum_{j\in S}z_j=0\) と同値。\(z_j\) は1の \(3\) 乗根なので，和が消える部分集合を数えればよい。巡回対称性から，正多角形をなす頂点集合とその合併が条件を満たす。

</details>

### `deep.recurrence_period_quadratic_character`

- 難易度: `A` / score `0.00`
- backend: `matrix_mod_order+legendre_symbol`
- 独立検証: `modular_period_then_euler_criterion`
- 最大表層類似度: `0.0`
- 射: `LinearRecurrence → CompanionMatrix → ModularReduction → MultiplicativeOrder → MinimalPeriod → PrimeFactorization → EulerCriterion → LegendreSymbol`

**問題**

数列 \((a_n)\) を \(a_0=0,\ a_1=1,\ a_{n+2}=a_{n+1}+a_n\) で定める。\((a_n)\) を \(\bmod\ 7\) で見たときの最小周期を \(T\) とし，\(T\) の最大の素因数を \(q\) とする。ルジャンドル記号 \(\left(\dfrac{q}{7}\right)\) の値を求めよ。

**答**: 1

<details>
<summary>検証済み解法記録</summary>

\((a_{n+1},a_n)\) は随伴行列 \(\begin{pmatrix}1&1\\1&0\end{pmatrix}\) を掛けて進むので，\(\bmod\ 7\) でのこの行列の位数が周期 \(T=16\)。その最大素因数は \(q=2\)。オイラーの規準 \(q^{(7-1)/2}\equiv1\pmod{7}\) より \(\left(\frac{2}{7}\right)=1\)。

</details>

### `deep.rotation_diagonal_product_divisors`

- 難易度: `A` / score `0.00`
- backend: `roots_of_unity+product+divisor_function`
- 独立検証: `cyclotomic_product_identity_plus_numeric_check`
- 最大表層類似度: `0.0`
- 射: `RootOfUnity → RegularPolygon → VertexDistances → PolynomialFactorization → LimitEvaluation → DistanceProduct → IntegerValue → DivisorCount`

**問題**

単位円に内接する正 \(3\) 角形の頂点を \(z_j=\cos\frac{2\pi j}{3}+i\sin\frac{2\pi j}{3}\ (j=0,1,\ldots,2)\) とする。頂点 \(z_0\) から他の \(2\) 個の頂点までの距離の積を \(L\) とするとき，\(L\) の正の約数の個数を求めよ。

**答**: 2

<details>
<summary>検証済み解法記録</summary>

\(z^{3}-1=\prod_{j=0}^{2}(z-z_j)\) の両辺を \(z-1\) で割り \(z\to1\) とすると \(\prod_{j=1}^{2}(1-z_j)=3\)。絶対値をとって \(L=3\)。よって約数の個数は \(2\)。

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

- 難易度: `B_hard_university` / score `13.82`
- backend: `cubic_discriminant+vandermonde_area+numeric_roots`
- 独立検証: `symbolic_discriminant_identity_vs_numeric_root_triangle_area`
- 最大表層類似度: `0.1361`
- 射: `CubicPolynomial → ThreeRealRootSet → ParabolaEmbedding → TriangleConstruction → VandermondeDeterminant → AreaSquare → PolynomialDiscriminant → IntegerNormalization → PrimeFactorization → DivisorCount → ArithmeticObservation`

**問題**

方程式 \(x^3-12x+(-8)=0\) の3実根を \(\alpha,\beta,\gamma\) とする。放物線 \(y=x^2\) 上の3点 \((\alpha,\alpha^2),(\beta,\beta^2),(\gamma,\gamma^2)\) が作る三角形の面積を \(S\) とし，\(M=\frac{4S^2}{27}\) と定める。\(M\) が整数であることを示し，\(M\) の正の約数の個数を求めよ。

**答**: 14

<details>
<summary>検証済み解法記録</summary>

Vandermonde 行列式から \(4S^2\) は三次式の判別式に等しい。判別式は \(27(4\cdot 2^6-(-8)^2)=27\cdot 192\) だから \(M=192=2^{6}\cdot 3\)。したがって正の約数は \(14\) 個。

</details>

### `ultradeep.cyclotomic_distance_norm_divisor_count`

- 難易度: `A_olympiad` / score `14.87`
- backend: `cyclotomic_polynomial+algebraic_norm+numeric_product`
- 独立検証: `cyclotomic_evaluation_vs_numeric_primitive_root_product`
- 最大表層類似度: `0.1111`
- 射: `RootOfUnity → CoprimeIndexFilter → PrimitiveRootSet → DistanceMultiset → DistanceProduct → CyclotomicPolynomial → PolynomialEvaluation → AlgebraicNorm → IntegerInvariant → PrimeFactorization → DivisorCount`

**問題**

\(\zeta_j=\cos\frac{2\pi j}{5}+i\sin\frac{2\pi j}{5}\) とし，\(1\le j\le 5\) かつ \(\gcd(j,5)=1\) を満たす \(j\) について \(L=\prod |2-\zeta_j|\) と定める。\(L\) が整数であることを示し，\(L\) の正の約数の個数を求めよ。

**答**: 2

<details>
<summary>検証済み解法記録</summary>

積に現れるのは原始 \(5\) 乗根だから，\(\prod(2-\zeta_j)=\Phi_{5}(2)=31\)。共役が対になるので絶対値の積も \(L=31\)。\(L=31\) より，正の約数は \(2\) 個。

</details>

### `ultradeep.gambler_absorption_variance_divisor_count`

- 難易度: `A` / score `0.00`
- backend: `absorbing_markov_moments+linear_system+factorization`
- 独立検証: `closed_variance_formula_vs_exact_two_moment_linear_system`
- 最大表層類似度: `0.0`
- 射: `PathStateSpace → AbsorbingBoundary → SymmetricRandomWalk → HittingTime → FirstMomentConditioning → FirstMomentLinearSystem → SecondMomentConditioning → SecondMomentLinearSystem → VarianceTransform → IntegerInvariant → PrimeFactorization → DivisorCount`

**問題**

点 \(0,1,\ldots,4\) 上を動く対称ランダムウォークを考える。初期位置は \(1\) で，各時刻に確率 \(\frac12\) ずつで左右に1動き，\(0\) または \(4\) に着いたら停止する。停止時刻を \(T\) とするとき，\(\operatorname{Var}(T)\) の正の約数の個数を求めよ。

**答**: 4

<details>
<summary>検証済み解法記録</summary>

一次モーメントの差分方程式から \(E[T]=1(4-1)\)。二次モーメントにも条件付けして解くと \(\operatorname{Var}(T)=\frac{1(4-1)(4^2-2-2\cdot 1(4-1))}{3}=8\)。\(8=2^{3}\) より約数は \(4\) 個。

</details>

### `ultradeep.geometry_astroid_envelope_area`

- 難易度: `B_hard_university` / score `8.86`
- backend: `line_envelope+stationarity+numeric_shoelace`
- 独立検証: `symbolic_envelope_conditions_vs_numeric_shoelace`
- 最大表層類似度: `0.123`
- 射: `CircleParameter → AxisEndpointPair → JoiningLine → LineFamily → EnvelopeStationarity → ParameterElimination → AstroidIdentification → ClosedCurveOrientation → GreenAreaMorphism → AreaObservation`

**問題**

\(0<\theta<\frac{\pi}{2}\) に対し，点 \(A_\theta=(2\cos\theta,0)\), \(B_\theta=(0,2\sin\theta)\) をとる。直線 \(A_\theta B_\theta\) を対称性により全象限へ拡張して得られる直線族の包絡線が囲む面積を求めよ。

**答**: \frac{3 \pi}{2}

<details>
<summary>検証済み解法記録</summary>

直線族を \(F=\frac{x}{2\cos\theta}+\frac{y}{2\sin\theta}-1=0\) とする。\(F=F_\theta=0\) から \(x=2\cos^3\theta,\ y=2\sin^3\theta\)。したがって包絡線はアステロイドであり，Greenの公式より \(\frac12\oint(x\,dy-y\,dx)=\frac{3 \pi}{2}\)。

</details>

### `ultradeep.geometry_convex_polygon_disk_sweep_area`

- 難易度: `D_textbook` / score `5.58`
- backend: `minkowski_sum+parallel_body+numeric_hull`
- 独立検証: `polygon_parallel_body_decomposition_vs_sampled_minkowski_hull`
- 最大表層類似度: `0.0775`
- 射: `ConvexPolygon → MovingCenter → DiskTranslation → PassageUnion → MinkowskiAddition → ParallelBody → EdgeStripDecomposition → ExteriorAngleSum → SectorAreaMerge → AreaObservation`

**問題**

面積 \(A\)、周長 \(L\) の凸多角形 \(P\) 上を、半径 \(r\) の円板の中心が自由に動く。この円板が通過する領域の面積を \(A,L,r\) で表せ。

**答**: A+rL+\pi r^2

<details>
<summary>検証済み解法記録</summary>

通過領域は多角形 \(P\) と半径 \(r\) の円板とのMinkowski和である。元の \(P\) に加え、各辺の外側に面積 \(r\ell_i\) の長方形ができる。各頂点にできる扇形の中心角の和は \(2\pi\) なので、その面積の和は\(\pi r^2\)。したがって \(A+r\sum_i\ell_i+\pi r^2=A+rL+\pi r^2\) である。

</details>

### `ultradeep.geometry_ellipse_tangent_pair_locus`

- 難易度: `A` / score `0.00`
- backend: `dual_conic+tangent_intersection+linear_system`
- 独立検証: `closed_intersection_formula_vs_numeric_two_line_solve`
- 最大表層類似度: `0.0`
- 射: `EllipseObject → TrigonometricChart → PairedParameterShift → TangentDualization → DualLinePair → LinearIntersection → TrigonometricDiagonalization → HomothetyRecognition → ConicElimination → LocusEquationObservation`

**問題**

楕円 \(E:\frac{x^2}{4}+\frac{y^2}{1}=1\) 上の点を \(P(t)=(2\cos t,1\sin t)\) とする。\(P(t+\frac{\pi}{3})\) と \(P(t-\frac{\pi}{3})\) における2本の接線の交点を \(Q(t)\)とするとき，\(Q(t)\) の軌跡の方程式を求めよ。

**答**: \frac{x^2}{4}+\frac{y^2}{1}=4

<details>
<summary>検証済み解法記録</summary>

2本の接線の方程式を加減して解くと \(Q(t)=(2\sec\frac{\pi}{3}\cos t,1\sec\frac{\pi}{3}\sin t)\)。よって軌跡は \(\frac{x^2}{4}+\frac{y^2}{1}=4\)。

</details>

### `ultradeep.geometry_orthocenter_locus_area`

- 難易度: `B_hard_university` / score `12.08`
- backend: `orthocenter+linear_image+numeric_shoelace`
- 独立検証: `altitude_coordinate_formula_vs_numeric_locus_shoelace`
- 最大表層類似度: `0.0882`
- 射: `EllipseObject → MajorAxisVertexPair → MovingTriangle → AltitudeConstraint → OrthocenterIntersection → CoordinateSolve → LinearImageRecognition → ImageEllipse → DeterminantAreaScaling → AreaObservation`

**問題**

楕円 \(E:\frac{x^2}{4}+\frac{y^2}{1}=1\) の長軸の端点を \(A=(-2,0),B=(2,0)\) とする。\(E\) 上を動く点 \(P\ne A,B\) に対し，三角形 \(ABP\) の垂心を \(H\) とする。\(H\) の軌跡が囲む面積を求めよ。

**答**: 8 \pi

<details>
<summary>検証済み解法記録</summary>

\(P=(2\cos t,1\sin t)\) とおく。\(AB\) が水平なので垂心の \(x\) 座標は \(2\cos t\)。もう1本の高さから \(H=(2\cos t,\frac{4}{1}\sin t)\)。したがって軌跡は半軸 \(2,\frac{4}{1}\) の楕円で，面積は \(8 \pi\)。

</details>

### `ultradeep.geometry_parabola_normal_envelope`

- 難易度: `D_textbook` / score `2.19`
- backend: `normal_family+resultant+evolute`
- 独立検証: `symbolic_resultant_identity_vs_parametric_substitution`
- 最大表層類似度: `0.0818`
- 射: `ParabolaObject → TangentVector → NormalDirection → NormalLine → NormalLineFamily → EnvelopeStationarity → StationaryParameterSolve → EvoluteParametrization → ResultantElimination → ImplicitCurveObservation`

**問題**

放物線 \(C:y=\frac{x^2}{4}\) 上の各点で法線を引く。この法線族の包絡線の方程式を求めよ。

**答**: 4(y-2)^3=27x^2

<details>
<summary>検証済み解法記録</summary>

\(C\) を \(P(t)=(2t,1t^2)\) と表示する。法線族は \(F=x+ty-2t-1t^3=0\)。\(F=F_t=0\) から \(x=-2t^3,\ y=2+3t^2\)。消去すると \(4(y-2)^3=27x^2\)。

</details>

### `ultradeep.geometry_regular_polygon_minkowski_perimeter`

- 難易度: `C_standard_university` / score `7.41`
- backend: `minkowski_sum+support_faces+convex_hull`
- 独立検証: `regular_polygon_formula_vs_all_vertex_sums_convex_hull`
- 最大表層類似度: `0.0847`
- 射: `RootOfUnityChart → RegularPolygon → HalfStepRotation → SecondRegularPolygon → MinkowskiAddition → SupportDirectionMerge → VertexSumHull → RegularDoublePolygon → EdgeLengthObservation → PerimeterObservation`

**問題**

同じ中心・外接円半径 \(1\) の正 \(3\) 角形 \(P,Q\) があり，\(Q\) は \(P\) を中心のまわりに \(\frac{\pi}{3}\) 回転したものとする。Minkowski和 \(P+Q=\{p+q\mid p\in P,q\in Q\}\) の周長を求めよ。

**答**: 6 \sqrt{3}

<details>
<summary>検証済み解法記録</summary>

両多角形の辺の法線方向は交互に現れるため，\(P+Q\) は正 \(6\)角形になる。隣接頂点間の距離は \(2\cdot 1\sin\frac{\pi}{3}\)。したがって周長は \(6\cdot2\cdot 1\sin\frac{\pi}{3}=6 \sqrt{3}\)。

</details>

### `ultradeep.geometry_triangle_displacement_locus_area`

- 難易度: `B_hard_university` / score `9.47`
- backend: `difference_body+convex_hull+shoelace`
- 独立検証: `symbolic_difference_body_identity_vs_numeric_convex_hull`
- 最大表層類似度: `0.0752`
- 射: `TriangleConfiguration → IndependentPointPair → DisplacementMap → DifferenceBody → VertexDifferenceSet → ConvexHull → CentralSymmetry → HexagonRecognition → AffineNormalization → AreaObservation`

**問題**

面積が \(S\) である三角形 \(T\) の内部または周上を2点 \(P,Q\) が独立に動く。ベクトル \(\overrightarrow{PQ}\) を、その成分を座標とする平面上の点とみなすとき、この点の通過領域の面積を \(S\) で表せ。

**答**: 6S

<details>
<summary>検証済み解法記録</summary>

三角形を \(A=(0,0),B=\mathbf b,C=\mathbf c\) とおく。変位全体は \(T-T=\{Q-P\mid P,Q\in T\}\) であり、その頂点は \(\pm\mathbf b,\pm\mathbf c,\pm(\mathbf b-\mathbf c)\) の6点である。この中心対称六角形を3本の対角線で分けるか靴紐公式を用いると、面積は \(6[ABC]=6S\) となる。

</details>

### `ultradeep.paley_four_cycle_divisor_count`

- 難易度: `A` / score `0.00`
- backend: `strongly_regular_graph+trace_four+factorization`
- 独立検証: `common_neighbor_double_count_vs_adjacency_trace_four`
- 最大表層類似度: `0.0`
- 射: `PrimeField → QuadraticResidueSet → PaleyGraph → StronglyRegularParameters → CommonNeighborRelation → OppositeVertexPairing → FourCycleDoubleCount → CycleCount → PrimeFactorization → DivisorCount`

**問題**

素数 \(p=13\) に対し，頂点集合 \(\mathbb Z_{13}\) 上で，\(x-y\) が平方剰余であるときに \(x,y\) を結んで得られる Paley グラフを \(G\) とする。\(G\) に含まれる単純な長さ4の閉路の個数を \(C\) とする。\(C\) の正の約数の個数を求めよ。

**答**: 8

<details>
<summary>検証済み解法記録</summary>

隣接2頂点の共通隣接点は \(2\) 個，非隣接2頂点では \(3\) 個。向かい合う頂点対で二重計数すると \(C=78\)。\(C=2\cdot 3\cdot 13\) なので，正の約数は \(8\) 個。

</details>

### `ultradeep.paley_spanning_tree_divisor_count`

- 難易度: `A` / score `0.00`
- backend: `paley_spectrum+matrix_tree+exact_determinant`
- 独立検証: `spectral_tree_formula_vs_exact_laplacian_cofactor`
- 最大表層類似度: `0.0`
- 射: `PrimeField → QuadraticResidueSet → PaleyGraph → AdjacencyMatrix → AdjacencySpectrum → LaplacianTransform → LaplacianSpectrum → NonzeroEigenvalueProduct → MatrixTreeTheorem → SpanningTreeCount → PrimeFactorization → DivisorCount`

**問題**

素数 \(p=5\) に対し，頂点集合 \(\mathbb Z_{5}\) 上で，\(x-y\) が平方剰余であるときに \(x,y\) を結んで得られる Paley グラフを \(G\) とする。\(G\) の全域木の個数を \(\tau\) とするとき，\(\tau\) の正の約数の個数を求めよ。

**答**: 2

<details>
<summary>検証済み解法記録</summary>

Paley グラフの隣接行列の非自明固有値は \(\frac{-1\pm\sqrt{5}}2\)（各重複度 \(2\)）。次数 \(2\) のラプラシアンの非零固有値の積を Kirchhoff の定理で\(5\) で割ると \(\tau=5^{1}\left(\frac{5-1}4\right)^{2}=5\)。したがって約数の個数は \(2\)。

</details>

### `ultradeep.spatial_cube_ball_sweep_volume`

- 難易度: `D_textbook` / score `5.14`
- backend: `spatial_minkowski_sum+boundary_strata+sampled_convex_hull_3d`
- 独立検証: `boundary_stratum_decomposition_vs_sampled_sphere_minkowski_hull`
- 最大表層類似度: `0.0687`
- 射: `CubeConfiguration → MovingSphereCenter → SpatialPassageUnion → ThreeDimensionalMinkowskiAddition → FaceEdgeVertexStratification → FacePrismContribution → QuarterCylinderEdgeContribution → SphericalOctantVertexContribution → DisjointBoundaryLayerMerge → VolumeObservation`

**問題**

一辺 \(a\) の立方体の内部または表面を、半径 \(r\) の球の中心が自由に動く。この球が通過する空間領域の体積を求めよ。

**答**: a^3+6a^2r+3\pi ar^2+\frac{4\pi}{3}r^3

<details>
<summary>検証済み解法記録</summary>

通過領域は立方体と半径 \(r\) の球とのMinkowski和である。元の立方体に、6面から生じる厚さ \(r\) の角柱、12辺から生じる四分円柱、8頂点から生じる球の八分体を加える。それぞれの体積は \(a^3,6a^2r,12\cdot\frac14\pi r^2a,8\cdot\frac18\frac43\pi r^3\)。合計して答を得る。

</details>

### `ultradeep.spatial_cube_diagonal_section_maximum`

- 難易度: `D_textbook` / score `8.72`
- backend: `slice_volume_derivative+inclusion_exclusion+numeric_section_hull`
- 独立検証: `inclusion_exclusion_derivative_vs_edge_intersection_polygon_area`
- 最大表層類似度: `0.0544`
- 射: `CubeConfiguration → BodyDiagonalDirection → ParallelPlaneFamily → SublevelSolid → SliceVolumeCorrespondence → CoordinateSimplexVolume → ThreeCornerExclusion → InclusionExclusion → PiecewiseQuadraticSectionArea → CentralSymmetryReduction → ExtremumObservation`

**問題**

一辺 \(a\) の立方体を、3辺を座標軸に平行になるように \(0\le x,y,z\le a\) と置く。平面 \(x+y+z=t\) で切った断面の面積が最大となる \(t\) と、その最大面積を求めよ。

**答**: t=\frac{3a}{2},\qquad \frac{3\sqrt3}{4}a^2

<details>
<summary>検証済み解法記録</summary>

\(F(t)\) を立方体内で \(x+y+z\le t\) を満たす部分の体積とする。断面に垂直な移動距離は \(dt/\sqrt3\) なので断面積は \(\sqrt3F'(t)\)。対称性から \(0\le t\le3a/2\) だけ見ればよい。\(0\le t\le a\) では \(F=t^3/6\)、\(a\le t\le3a/2\) では包除原理により \(F=\{t^3-3(t-a)^3\}/6\)。後者の断面積は \(\frac{\sqrt3}{2}\{t^2-3(t-a)^2\}\) で、\(t=3a/2\) まで増加する。よって中央の正六角形断面で最大値 \(3\sqrt3a^2/4\) をとる。

</details>

### `ultradeep.spatial_tetrahedron_displacement_locus_volume`

- 難易度: `D_textbook` / score `12.08`
- backend: `difference_body+orthant_decomposition+numeric_convex_hull_3d`
- 独立検証: `orthant_simplex_volume_identity_vs_scipy_convex_hull_3d`
- 最大表層類似度: `0.0364`
- 射: `TetrahedronConfiguration → IndependentPointPair → SpatialDisplacementMap → ThreeDimensionalDifferenceBody → AffineSimplexNormalization → CoordinateSignPartition → PositiveNegativeMassConstraints → OrthantSimplexDecomposition → BinomialVolumeMerge → AffineVolumeScaling → VolumeObservation`

**問題**

体積が \(V\) である四面体 \(T\) の内部または表面を2点 \(P,Q\) が独立に動く。ベクトル \(\overrightarrow{PQ}\) の3成分を空間内の点の座標とみなすとき、この点の通過領域の体積を \(V\) で表せ。

**答**: 20V

<details>
<summary>検証済み解法記録</summary>

アフィン変換で \(T=\{(x,y,z)\mid x,y,z\ge0,\ x+y+z\le1\}\) としてよい。変位 \(u=Q-P\) 全体は、正の成分の和と負の成分の絶対値の和がともに1以下となる領域である。符号が正の座標を \(k\) 個指定した部分の体積は \(1/(k!(3-k)!)\)。したがって全体の体積は \(\sum_{k=0}^3\binom3k/(k!(3-k)!)=10/3\)。標準四面体の体積は \(1/6\) なので比は20であり、一般の四面体でもアフィン変換で同じ比が保たれる。よって答は \(20V\)。

</details>

## 解釈上の注意

- `A_olympiad` などの難易度は人手採点ではなく、176問で較正した推定器の出力。
- `corpus_novel=true` は登録コーパス内での衝突がないことを示し、
  数学史上まったく新しいことの証明ではない。
- `exact_backend` と `independent_check` は生成器の検査契約であり、
  Leanによる全問の形式証明を意味しない。
- したがって、正しさ・新規性・難易度を同じ一語の「良問」でまとめず、
  それぞれ別の指標として追跡する。
