# MathOS 研究候補・保留キュー

> `unresolved_by_mathos` は人類未解決という意味ではない。
> 現在のMathOSが証明も反例も得られなかった状態を表す。

## 集計

- 保留候補: **12件**
- 異なる型付き射列: **12件**
- 問いの型: **12種類**
- 数値替え: **0件**
- 各候補の照合母数: **28074問以上**

## 候補

### 重心ペダル三角形の反復力学

- ID: `research.geometry.centroid_pedal_iteration`
- 状態: `unresolved_by_mathos`
- 射数: `10`
- 問い: `dynamical_classification`
- 難度仮説: `15`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0656`

鋭角不等辺三角形 \(T_0\) をとる。\(T_n\) の重心から3辺へ下ろした垂線の足が作る三角形を \(T_{n+1}\) とする。各段階で重心を原点，面積を1，第1頂点を正の \(x\) 軸上に置く相似正規化を行う。三角形のモジュライ空間における全ての極限集合と周期軌道を分類せよ。

射列: `Centroid → PedalProjection → TriangleFormation → SimilarityNormalization → ModuliProjection → Iteration → Compactification → LimitSet → PeriodicDecomposition → ClassificationQuery`

### 四次曲線上の頂点が作る垂心軌跡

- ID: `research.geometry.quartic_orthocenter_locus`
- 状態: `unresolved_by_mathos`
- 射数: `10`
- 問い: `algebraic_curve_invariants`
- 難度仮説: `10`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.06`

\(A=(-1,0),B=(1,0)\) とし，\(P\) を \(x^4+y^4=1,\ y>0\) 上で動かす。三角形 \(ABP\) の垂心 \(H(P)\) の軌跡の射影閉包について，既約分解・全特異点・幾何種数を決定せよ。

射列: `MovingPoint → TriangleAttachment → AltitudeConstruction → Intersection → RationalCoordinateMap → ParameterElimination → ProjectiveClosure → SingularityResolution → GenusComputation → ClassificationQuery`

### 楕円の三接線が作る三角形中心の分類

- ID: `research.geometry.ellipse_tritangent_center_locus`
- 状態: `unresolved_by_mathos`
- 射数: `10`
- 問い: `parameter_classification`
- 難度仮説: `13`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.088`

楕円 \(E:x^2/a^2+y^2/b^2=1\ (a>b>0)\) の媒介点を \(P(t)\) とする。接線 \(l_t,l_{t+\alpha},l_{t+\beta}\) が作る三角形の九点中心を \(N(t)\)とする。\(0<\alpha<\beta<2\pi\) に対し，\(N(t)\) の軌跡が円錐曲線となるための必要十分条件を求め，各場合の方程式を決定せよ。

射列: `TrigonometricChart → TwoShiftAction → TangentDualization → PairwiseIntersection → CenterPairConstruction → MidpointCombination → TrigonometricNormalForm → ParameterElimination → ConicRecognition → ParameterClassification`

### 反転と発展曲線の可換性

- ID: `research.geometry.inversion_evolute_commutator`
- 状態: `unresolved_by_mathos`
- 射数: `10`
- 問い: `commutation_classification`
- 難度仮説: `13`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0928`

原点を通らない非退化実円錐曲線 \(C\) と単位円反転 \(I\) を考える。正則枝ごとの発展曲線を \(\mathcal E(C)\) とする。\(I(\mathcal E(C))\) と \(\mathcal E(I(C))\) が相似変換で一致する円錐曲線 \(C\) を，相似を除いて全て分類せよ。

射列: `EvoluteWithSource → CircleInversionOfPair → RegularBranchSelection → SecondEvoluteConstruction → CurveComparison → BranchCompatibility → SimilarityWitness → SimilarityQuotient → CommutatorVanishing → ConicClassification`

### Minkowski和と極双対による凸体力学

- ID: `research.geometry.minkowski_polar_iteration`
- 状態: `unresolved_by_mathos`
- 射数: `10`
- 問い: `convex_dynamical_classification`
- 難度仮説: `15`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0608`

原点対称で \(C^\infty\) 級，厳密凸な代数的凸体 \(K\subset\mathbb R^2\)を面積 \(\pi\) に正規化する。極体を \(K^\circ\) とし，\(\Phi(K)\) を \(K+K^\circ\) を再び面積 \(\pi\) に正規化した凸体とする。代数的境界を持つ固定点を線形同値を除いて分類し，\(\Phi^n(K)\) の収束・非収束条件を決定せよ。

射列: `PolarPairing → MinkowskiPairing → MinkowskiAddition → AreaNormalization → Iteration → SupportFunctionChart → FixedPointEquation → LinearEquivalenceQuotient → StabilityAnalysis → GlobalClassification`

### 多項式グラフの発展曲線に現れる実尖点の最大数

- ID: `research.geometry.polynomial_evolute_real_cusps`
- 状態: `unresolved_by_mathos`
- 射数: `10`
- 問い: `extremal_real_singularity_count`
- 難度仮説: `12`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.1145`

\(d\ge3\) を固定し，実係数モニック多項式 \(f\)（次数 \(d\)）のグラフ \(y=f(x)\) の発展曲線を考える。係数を動かしたときに現れ得る孤立実尖点の最大数を \(d\) の式で求め，最大値を達成する多項式を係数空間の連結成分ごとに特徴付けよ。

射列: `CoefficientSpace → UniversalPolynomial → GraphEmbedding → NormalField → Envelope → SingularityCondition → RealStratification → CuspCountFunction → GlobalMaximum → ExtremizerClassification`

### 曲線の等角共役像の次数・種数公式

- ID: `research.geometry.isogonal_curve_transform`
- 状態: `unresolved_by_mathos`
- 射数: `10`
- 問い: `birational_invariant_formula`
- 難度仮説: `12`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0547`

三角形の重心座標で等角共役写像を \(\iota[x:y:z]=[yz:zx:xy]\) とする。三頂点を成分に持たない既約平面曲線\(C\) について，次数，三頂点での重複度，接錐のデータから\(\overline{\iota(C)}\) の次数・全特異点・幾何種数を与える完全な公式を求めよ。

射列: `VertexMultiplicityData → QuadraticCremonaMap → BasePointBlowup → StrictTransform → DegreeAndExceptionalData → SingularityExtraction → DeltaInvariant → AdjunctionFormula → GenusCorrection → ClosedFormulaQuery`

### 楕円の倍角弦を反転した円族の包絡線

- ID: `research.geometry.inverted_chord_envelope`
- 状態: `unresolved_by_mathos`
- 射数: `10`
- 問い: `degree_genus_classification`
- 難度仮説: `15`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0601`

楕円 \(E:x^2/a^2+y^2/b^2=1\) を \(P(t)\) で媒介表示し，整数 \(m\ge2\)に対して弦 \(P(t)P(mt)\) を考える。各弦を単位円反転で原点を通る円へ移した円族の包絡線について，既約成分，次数，幾何種数を \(m\) の関数として決定し，有理成分を持つ \(m\) を分類せよ。

射列: `TrigonometricChart → MultiplicationMap → ChordConstruction → CircleInversion → EnvelopeStationarity → TrigonometricAlgebraization → ParameterElimination → IrreducibleDecomposition → GenusComputation → IntegerParameterClassification`

### 巡回三頂点外心写像による多角形力学

- ID: `research.geometry.cyclic_polygon_circumcenter_iteration`
- 状態: `unresolved_by_mathos`
- 射数: `11`
- 問い: `polygon_dynamical_classification`
- 難度仮説: `14`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0656`

同一直線上に3点を持たない凸 \(n\) 角形 \(P_0=(V_1,\ldots,V_n)\) に対し，\(V_{i-1},V_i,V_{i+1}\) の外心を新しい頂点 \(W_i\) として \(P_{k+1}\)を作る。重心0・二次モーメント1に正規化しながら反復するとき，全ての周期軌道と収束する初期多角形を相似を除いて分類せよ。

射列: `ConsecutiveTriple → Circumcenter → PolygonFormation → MomentNormalization → Iteration → SimilarityQuotient → OrbitClosure → PeriodicAndLimitData → PeriodicPointEquation → AlgebraicDecomposition → GlobalClassification`

### 超楕円上の頂点が作る類似重心の軌跡

- ID: `research.geometry.superellipse_symmedian_locus`
- 状態: `unresolved_by_mathos`
- 射数: `10`
- 問い: `parametric_locus_classification`
- 難度仮説: `13`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0705`

\(A=(-1,0),B=(1,0)\) とし，\(P\) を \(x^{2r}+y^{2r}=1,\ y>0\)上で動かす。三角形 \(ABP\) の類似重心（symmedian point）\(K(P)\) の軌跡の射影閉包について，次数・既約成分・幾何種数を \(r\ge2\) の関数として決定し，有理軌跡となる \(r\) を分類せよ。

射列: `MovingPoint → TriangleAttachment → SideLengthSquareWeights → BarycentricCombination → RationalCoordinateMap → ParameterElimination → ProjectiveClosure → IrreducibleDecomposition → GenusComputation → IntegerParameterClassification`

### 平行曲線と極双対の可換性

- ID: `research.geometry.offset_polar_duality`
- 状態: `unresolved_by_mathos`
- 射数: `10`
- 問い: `duality_commutation_classification`
- 難度仮説: `13`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0806`

原点を内部に持つ \(C^\infty\) 級厳密凸代数曲線 \(C\) に対し，外向き距離 \(s\) の平行曲線を \(C_s\)，極双対を \(C^\circ\) とする。\((C_s)^\circ\) と \((C^\circ)_t\) がある \(s,t>0\) で相似になる代数曲線 \(C\) を相似を除いて分類せよ。

射列: `SupportAndDualChart → OffsetAddition → CurveReconstruction → PolarOnFirstBranch → RegularityRestriction → SimilarityComparison → SimilarityInvariantExtraction → OffsetParameterElimination → FunctionalConstraint → AlgebraicCurveClassification`

### 円錐曲線の反射焦線を反復したときの次数成長

- ID: `research.geometry.iterated_conic_caustic_degree`
- 状態: `unresolved_by_mathos`
- 射数: `11`
- 問い: `degree_growth_classification`
- 難度仮説: `14`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0556`

光源 \(S\) と，\(S\) を通らない非退化実円錐曲線 \(C_0\) をとる。\(C_{n+1}\) を，\(S\) から \(C_n\) へ入射して反射する光線族の包絡線の射影閉包とする。退化成分を除いた次数列の成長率を決定し，次数が有界または周期的となる \((C_0,S)\) を射影同値を除いて分類せよ。

射列: `IncidentRayFamily → ReflectionLaw → Envelope → ProjectiveClosure → DegenerateComponentRemoval → Iteration → DegreeSequence → AsymptoticGrowth → DegreeDynamics → ExceptionalParameterExtraction → ProjectiveClassification`

## 注意

- 有名問題スクリーニングは局所マーカーと既存コーパス照合の入口であり、
  文献調査や研究上の新規性証明の代わりではない。
- 保留候補は公開前に専門家レビュー、文献検索、より長い反例探索を行う。
- 解けなかったこと自体を難しさや新規性の証拠にはしない。
