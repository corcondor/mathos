# MathOS 研究候補・保留キュー

> `unresolved_by_mathos` は人類未解決という意味ではない。
> 現在のMathOSが証明も反例も得られなかった状態を表す。

## 集計

- 保留候補: **464件**
- 異なる型付き射列: **464件**
- 問いの型: **24種類**
- 数値替え: **0件**
- 各候補の照合母数: **28074問以上**
- atlas自律探索候補: **452件**
- 今回の自律追加: **12件**
- 現在の探索深さ下限: **29射**

## 自律探索

- 世代: `39`
- 射アトラス: `92射`
- チャート: `6領域`
- 探索試行: `172`
- 商: `typed operation classes + type aliases + numeric erasure + commuting-block normalization`

## 候補

### 重心ペダル三角形の反復力学

- ID: `research.geometry.centroid_pedal_iteration`
- 状態: `unresolved_by_mathos`
- 射数: `10`
- 問い: `dynamical_classification`
- 難度仮説: `15`
- 生成元: `curated_seed`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0656`
- 照合方式: `exact_3gram_jaccard`

鋭角不等辺三角形 \(T_0\) をとる。\(T_n\) の重心から3辺へ下ろした垂線の足が作る三角形を \(T_{n+1}\) とする。各段階で重心を原点，面積を1，第1頂点を正の \(x\) 軸上に置く相似正規化を行う。三角形のモジュライ空間における全ての極限集合と周期軌道を分類せよ。

射列: `Centroid → PedalProjection → TriangleFormation → SimilarityNormalization → ModuliProjection → Iteration → Compactification → LimitSet → PeriodicDecomposition → ClassificationQuery`

### 四次曲線上の頂点が作る垂心軌跡

- ID: `research.geometry.quartic_orthocenter_locus`
- 状態: `unresolved_by_mathos`
- 射数: `10`
- 問い: `algebraic_curve_invariants`
- 難度仮説: `10`
- 生成元: `curated_seed`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.06`
- 照合方式: `exact_3gram_jaccard`

\(A=(-1,0),B=(1,0)\) とし，\(P\) を \(x^4+y^4=1,\ y>0\) 上で動かす。三角形 \(ABP\) の垂心 \(H(P)\) の軌跡の射影閉包について，既約分解・全特異点・幾何種数を決定せよ。

射列: `MovingPoint → TriangleAttachment → AltitudeConstruction → Intersection → RationalCoordinateMap → ParameterElimination → ProjectiveClosure → SingularityResolution → GenusComputation → ClassificationQuery`

### 楕円の三接線が作る三角形中心の分類

- ID: `research.geometry.ellipse_tritangent_center_locus`
- 状態: `unresolved_by_mathos`
- 射数: `10`
- 問い: `parameter_classification`
- 難度仮説: `13`
- 生成元: `curated_seed`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.088`
- 照合方式: `exact_3gram_jaccard`

楕円 \(E:x^2/a^2+y^2/b^2=1\ (a>b>0)\) の媒介点を \(P(t)\) とする。接線 \(l_t,l_{t+\alpha},l_{t+\beta}\) が作る三角形の九点中心を \(N(t)\)とする。\(0<\alpha<\beta<2\pi\) に対し，\(N(t)\) の軌跡が円錐曲線となるための必要十分条件を求め，各場合の方程式を決定せよ。

射列: `TrigonometricChart → TwoShiftAction → TangentDualization → PairwiseIntersection → CenterPairConstruction → MidpointCombination → TrigonometricNormalForm → ParameterElimination → ConicRecognition → ParameterClassification`

### 反転と発展曲線の可換性

- ID: `research.geometry.inversion_evolute_commutator`
- 状態: `unresolved_by_mathos`
- 射数: `10`
- 問い: `commutation_classification`
- 難度仮説: `13`
- 生成元: `curated_seed`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0928`
- 照合方式: `exact_3gram_jaccard`

原点を通らない非退化実円錐曲線 \(C\) と単位円反転 \(I\) を考える。正則枝ごとの発展曲線を \(\mathcal E(C)\) とする。\(I(\mathcal E(C))\) と \(\mathcal E(I(C))\) が相似変換で一致する円錐曲線 \(C\) を，相似を除いて全て分類せよ。

射列: `EvoluteWithSource → CircleInversionOfPair → RegularBranchSelection → SecondEvoluteConstruction → CurveComparison → BranchCompatibility → SimilarityWitness → SimilarityQuotient → CommutatorVanishing → ConicClassification`

### Minkowski和と極双対による凸体力学

- ID: `research.geometry.minkowski_polar_iteration`
- 状態: `unresolved_by_mathos`
- 射数: `10`
- 問い: `convex_dynamical_classification`
- 難度仮説: `15`
- 生成元: `curated_seed`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0608`
- 照合方式: `exact_3gram_jaccard`

原点対称で \(C^\infty\) 級，厳密凸な代数的凸体 \(K\subset\mathbb R^2\)を面積 \(\pi\) に正規化する。極体を \(K^\circ\) とし，\(\Phi(K)\) を \(K+K^\circ\) を再び面積 \(\pi\) に正規化した凸体とする。代数的境界を持つ固定点を線形同値を除いて分類し，\(\Phi^n(K)\) の収束・非収束条件を決定せよ。

射列: `PolarPairing → MinkowskiPairing → MinkowskiAddition → AreaNormalization → Iteration → SupportFunctionChart → FixedPointEquation → LinearEquivalenceQuotient → StabilityAnalysis → GlobalClassification`

### 多項式グラフの発展曲線に現れる実尖点の最大数

- ID: `research.geometry.polynomial_evolute_real_cusps`
- 状態: `unresolved_by_mathos`
- 射数: `10`
- 問い: `extremal_real_singularity_count`
- 難度仮説: `12`
- 生成元: `curated_seed`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.1145`
- 照合方式: `exact_3gram_jaccard`

\(d\ge3\) を固定し，実係数モニック多項式 \(f\)（次数 \(d\)）のグラフ \(y=f(x)\) の発展曲線を考える。係数を動かしたときに現れ得る孤立実尖点の最大数を \(d\) の式で求め，最大値を達成する多項式を係数空間の連結成分ごとに特徴付けよ。

射列: `CoefficientSpace → UniversalPolynomial → GraphEmbedding → NormalField → Envelope → SingularityCondition → RealStratification → CuspCountFunction → GlobalMaximum → ExtremizerClassification`

### 曲線の等角共役像の次数・種数公式

- ID: `research.geometry.isogonal_curve_transform`
- 状態: `unresolved_by_mathos`
- 射数: `10`
- 問い: `birational_invariant_formula`
- 難度仮説: `12`
- 生成元: `curated_seed`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0547`
- 照合方式: `exact_3gram_jaccard`

三角形の重心座標で等角共役写像を \(\iota[x:y:z]=[yz:zx:xy]\) とする。三頂点を成分に持たない既約平面曲線\(C\) について，次数，三頂点での重複度，接錐のデータから\(\overline{\iota(C)}\) の次数・全特異点・幾何種数を与える完全な公式を求めよ。

射列: `VertexMultiplicityData → QuadraticCremonaMap → BasePointBlowup → StrictTransform → DegreeAndExceptionalData → SingularityExtraction → DeltaInvariant → AdjunctionFormula → GenusCorrection → ClosedFormulaQuery`

### 楕円の倍角弦を反転した円族の包絡線

- ID: `research.geometry.inverted_chord_envelope`
- 状態: `unresolved_by_mathos`
- 射数: `10`
- 問い: `degree_genus_classification`
- 難度仮説: `15`
- 生成元: `curated_seed`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0601`
- 照合方式: `exact_3gram_jaccard`

楕円 \(E:x^2/a^2+y^2/b^2=1\) を \(P(t)\) で媒介表示し，整数 \(m\ge2\)に対して弦 \(P(t)P(mt)\) を考える。各弦を単位円反転で原点を通る円へ移した円族の包絡線について，既約成分，次数，幾何種数を \(m\) の関数として決定し，有理成分を持つ \(m\) を分類せよ。

射列: `TrigonometricChart → MultiplicationMap → ChordConstruction → CircleInversion → EnvelopeStationarity → TrigonometricAlgebraization → ParameterElimination → IrreducibleDecomposition → GenusComputation → IntegerParameterClassification`

### 巡回三頂点外心写像による多角形力学

- ID: `research.geometry.cyclic_polygon_circumcenter_iteration`
- 状態: `unresolved_by_mathos`
- 射数: `11`
- 問い: `polygon_dynamical_classification`
- 難度仮説: `14`
- 生成元: `curated_seed`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0656`
- 照合方式: `exact_3gram_jaccard`

同一直線上に3点を持たない凸 \(n\) 角形 \(P_0=(V_1,\ldots,V_n)\) に対し，\(V_{i-1},V_i,V_{i+1}\) の外心を新しい頂点 \(W_i\) として \(P_{k+1}\)を作る。重心0・二次モーメント1に正規化しながら反復するとき，全ての周期軌道と収束する初期多角形を相似を除いて分類せよ。

射列: `ConsecutiveTriple → Circumcenter → PolygonFormation → MomentNormalization → Iteration → SimilarityQuotient → OrbitClosure → PeriodicAndLimitData → PeriodicPointEquation → AlgebraicDecomposition → GlobalClassification`

### 超楕円上の頂点が作る類似重心の軌跡

- ID: `research.geometry.superellipse_symmedian_locus`
- 状態: `unresolved_by_mathos`
- 射数: `10`
- 問い: `parametric_locus_classification`
- 難度仮説: `13`
- 生成元: `curated_seed`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0705`
- 照合方式: `exact_3gram_jaccard`

\(A=(-1,0),B=(1,0)\) とし，\(P\) を \(x^{2r}+y^{2r}=1,\ y>0\)上で動かす。三角形 \(ABP\) の類似重心（symmedian point）\(K(P)\) の軌跡の射影閉包について，次数・既約成分・幾何種数を \(r\ge2\) の関数として決定し，有理軌跡となる \(r\) を分類せよ。

射列: `MovingPoint → TriangleAttachment → SideLengthSquareWeights → BarycentricCombination → RationalCoordinateMap → ParameterElimination → ProjectiveClosure → IrreducibleDecomposition → GenusComputation → IntegerParameterClassification`

### 平行曲線と極双対の可換性

- ID: `research.geometry.offset_polar_duality`
- 状態: `unresolved_by_mathos`
- 射数: `10`
- 問い: `duality_commutation_classification`
- 難度仮説: `13`
- 生成元: `curated_seed`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0806`
- 照合方式: `exact_3gram_jaccard`

原点を内部に持つ \(C^\infty\) 級厳密凸代数曲線 \(C\) に対し，外向き距離 \(s\) の平行曲線を \(C_s\)，極双対を \(C^\circ\) とする。\((C_s)^\circ\) と \((C^\circ)_t\) がある \(s,t>0\) で相似になる代数曲線 \(C\) を相似を除いて分類せよ。

射列: `SupportAndDualChart → OffsetAddition → CurveReconstruction → PolarOnFirstBranch → RegularityRestriction → SimilarityComparison → SimilarityInvariantExtraction → OffsetParameterElimination → FunctionalConstraint → AlgebraicCurveClassification`

### 円錐曲線の反射焦線を反復したときの次数成長

- ID: `research.geometry.iterated_conic_caustic_degree`
- 状態: `unresolved_by_mathos`
- 射数: `11`
- 問い: `degree_growth_classification`
- 難度仮説: `14`
- 生成元: `curated_seed`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0556`
- 照合方式: `exact_3gram_jaccard`

光源 \(S\) と，\(S\) を通らない非退化実円錐曲線 \(C_0\) をとる。\(C_{n+1}\) を，\(S\) から \(C_n\) へ入射して反射する光線族の包絡線の射影閉包とする。退化成分を除いた次数列の成長率を決定し，次数が有界または周期的となる \((C_0,S)\) を射影同値を除いて分類せよ。

射列: `IncidentRayFamily → ReflectionLaw → Envelope → ProjectiveClosure → DegenerateComponentRemoval → Iteration → DegreeSequence → AsymptoticGrowth → DegreeDynamics → ExceptionalParameterExtraction → ProjectiveClassification`

### 三角形変換の合成力学（IncenterMark・CevianTrace・SimilarityNormalization・ModuliProjection）

- ID: `research.autonomous.triangle_dynamics.d3b289e5c0`
- 状態: `unresolved_by_mathos`
- 射数: `12`
- 問い: `triangle_transform_fixed_points`
- 難度仮説: `15`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0317`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 内心を標識点として付加する，(2) 標識点を通る三本のcevianの辺上の足をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 垂足三角形へ移す，(5) 反中点三角形へ移す，(6) 重心を標識点として付加する，(7) 標識点を三辺に関して反射した三点をとる，(8) 三点を頂点とする向き付き三角形を作る，(9) 反中点三角形へ移す，(10) 重心・面積・向きを固定して相似正規化する，(11) 相似類のモジュライ点へ射影する。最後に、誘導写像の固定点と有限周期点を相似を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IncenterMark → CevianTrace → TriangleFormation → OrthicTransform → AnticomplementaryTransform → CentroidMark → SideReflectionTrace → TriangleFormation → AnticomplementaryTransform → SimilarityNormalization → ModuliProjection → TriangleFixedPointQuery`

### Cayleyグラフのスペクトル合成（CharacterLevelConnection・CayleyConstruction・ClosedWalkExtraction・WalkArithmeticInvariant）

- ID: `research.autonomous.cayley_spectral.21a399e89d`
- 状態: `unresolved_by_mathos`
- 射数: `12`
- 問い: `closed_walk_congruence`
- 難度仮説: `15`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.029`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「有限アーベル群と、その自己同型で不変な生成集合を初期データとする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 非自明指標の値が指定軌道に属する元を生成集合とする，(2) 対応する無向Cayleyグラフを作る，(3) ループを除いた補グラフをとる，(4) 距離2の頂点を結ぶグラフをとる，(5) 距離が指定範囲以内の頂点を結ぶグラフ冪をとる，(6) 距離2の頂点を結ぶグラフをとる，(7) 隣接作用素を群環上に表す，(8) 指標表で同時対角化してスペクトルを得る，(9) スペクトルモーメント列を作る，(10) 閉歩道数と原始閉路数を抽出する，(11) 閉路数列の合同不変量を抽出する。最後に、閉路数列が指定合同周期を持つ場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CharacterLevelConnection → CayleyConstruction → GraphComplement → DistanceTwoGraph → GraphPower → DistanceTwoGraph → AdjacencyOperator → CharacterDiagonalization → SpectralMoments → ClosedWalkExtraction → WalkArithmeticInvariant → WalkCongruenceQuery`

### Cayleyグラフのスペクトル合成（PowerResidueConnection・CayleyConstruction・ClosedWalkExtraction・WalkArithmeticInvariant）

- ID: `research.autonomous.cayley_spectral.3a75fc748c`
- 状態: `unresolved_by_mathos`
- 射数: `12`
- 問い: `closed_walk_congruence`
- 難度仮説: `15`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0291`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「有限アーベル群と、その自己同型で不変な生成集合を初期データとする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 冪剰余類の自己同型軌道を生成集合とする，(2) 対応する無向Cayleyグラフを作る，(3) 距離2の頂点を結ぶグラフをとる，(4) 距離が指定範囲以内の頂点を結ぶグラフ冪をとる，(5) ループを除いた補グラフをとる，(6) 距離2の頂点を結ぶグラフをとる，(7) 組合せLaplacianを群環上に表す，(8) 指標表で同時対角化してスペクトルを得る，(9) スペクトルモーメント列を作る，(10) 閉歩道数と原始閉路数を抽出する，(11) 閉路数列の合同不変量を抽出する。最後に、閉路数列が指定合同周期を持つ場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `PowerResidueConnection → CayleyConstruction → DistanceTwoGraph → GraphPower → GraphComplement → DistanceTwoGraph → LaplacianOperator → CharacterDiagonalization → SpectralMoments → ClosedWalkExtraction → WalkArithmeticInvariant → WalkCongruenceQuery`

### Cayleyグラフのスペクトル合成（CharacterLevelConnection・CayleyConstruction・ClosedWalkExtraction・WalkArithmeticInvariant）

- ID: `research.autonomous.cayley_spectral.7bf74073d0`
- 状態: `unresolved_by_mathos`
- 射数: `10`
- 問い: `closed_walk_congruence`
- 難度仮説: `13`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0297`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「有限アーベル群と、その自己同型で不変な生成集合を初期データとする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 非自明指標の値が指定軌道に属する元を生成集合とする，(2) 対応する無向Cayleyグラフを作る，(3) 距離が指定範囲以内の頂点を結ぶグラフ冪をとる，(4) ループを除いた補グラフをとる，(5) 隣接作用素を群環上に表す，(6) 指標表で同時対角化してスペクトルを得る，(7) スペクトルモーメント列を作る，(8) 閉歩道数と原始閉路数を抽出する，(9) 閉路数列の合同不変量を抽出する。最後に、閉路数列が指定合同周期を持つ場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CharacterLevelConnection → CayleyConstruction → GraphPower → GraphComplement → AdjacencyOperator → CharacterDiagonalization → SpectralMoments → ClosedWalkExtraction → WalkArithmeticInvariant → WalkCongruenceQuery`

### 三角形変換の合成力学（CircumcenterMark・SideReflectionTrace・SimilarityNormalization・ModuliProjection）

- ID: `research.autonomous.triangle_dynamics.92b876f6ad`
- 状態: `unresolved_by_mathos`
- 射数: `11`
- 問い: `triangle_transform_fixed_points`
- 難度仮説: `14`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0322`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 外心を標識点として付加する，(2) 標識点を三辺に関して反射した三点をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 類似重心を標識点として付加する，(5) 標識点から三辺への垂足三点をとる，(6) 三点を頂点とする向き付き三角形を作る，(7) 傍心三角形へ移す，(8) 三辺の中点三角形へ移す，(9) 重心・面積・向きを固定して相似正規化する，(10) 相似類のモジュライ点へ射影する。最後に、誘導写像の固定点と有限周期点を相似を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CircumcenterMark → SideReflectionTrace → TriangleFormation → SymmedianMark → PedalProjection → TriangleFormation → ExcentralTransform → MedialTransform → SimilarityNormalization → ModuliProjection → TriangleFixedPointQuery`

### Markov関手と到達時刻不変量（StateLumping・DoobTransform・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.2e8c26887a`
- 状態: `unresolved_by_mathos`
- 射数: `12`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `15`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0298`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自己同型軌道に沿って強 lumping する，(2) 正の固有関数によるDoob変換を施す，(3) 恒等遷移との凸結合でlazy化する，(4) 自己同型軌道に沿って強 lumping する，(5) 正の固有関数によるDoob変換を施す，(6) 定常分布に関する時間反転をとる，(7) 恒等遷移との凸結合でlazy化する，(8) 指定集合で吸収させ過渡核をとる，(9) 過渡核のGreen作用素をとる，(10) 到達時刻の高次モーメント連立系を作る，(11) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `StateLumping → DoobTransform → LazyPerturbation → StateLumping → DoobTransform → TimeReversal → LazyPerturbation → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 多項式変換と算術観測（ShiftConjugacy・RootMultiset・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.0a69682fb4`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `recurrence_order_drop`
- 難度仮説: `16`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0297`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根の重心を0へ移す平行移動共役を施す，(2) 重複度付き根配置へ移す，(3) 根配置からモニック多項式を再構成する，(4) 導関数をモニックに再正規化する，(5) 根を二乗するGraeffe変換を施す，(6) 臨界値を根にもつ消去多項式を作る，(7) 根の重心を0へ移す平行移動共役を施す，(8) 重複度付き根配置へ移す，(9) 根の冪和モーメント列を作る，(10) モーメントからHankel行列族を作る，(11) 主小行列式列をとる，(12) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ShiftConjugacy → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → GraeffeTransform → CriticalValuePolynomial → ShiftConjugacy → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 平面代数曲線の合成変換（IsogonalCremona・ProjectiveDual・CircleInversion・IsogonalCremona）

- ID: `research.autonomous.plane_curve.77b6afa48f`
- 状態: `unresolved_by_mathos`
- 射数: `11`
- 問い: `birational_periodicity`
- 難度仮説: `13`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.029`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定基準三角形に関する等角共役Cremona像をとる，(2) 正則接線族の射影双対曲線をとる，(3) 法線族の包絡線である発展曲線をとる，(4) 原点中心の円反転像をとる，(5) 固定光源からの反射光線族の包絡線をとる，(6) 正則接線族の射影双対曲線をとる，(7) 射影閉包をとり無限遠点を加える，(8) 基点を避ける一般アフィンチャートへ移す，(9) 原点中心の円反転像をとる，(10) 固定基準三角形に関する等角共役Cremona像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IsogonalCremona → ProjectiveDual → Evolute → CircleInversion → Catacaustic → ProjectiveDual → ProjectiveClosure → AffineChartChange → CircleInversion → IsogonalCremona → BirationalPeriodQuery`

### Cayleyグラフのスペクトル合成（AutomorphismOrbitConnection・CayleyConstruction・ClosedWalkExtraction・WalkArithmeticInvariant）

- ID: `research.autonomous.cayley_spectral.8b4f87f255`
- 状態: `unresolved_by_mathos`
- 射数: `10`
- 問い: `closed_walk_congruence`
- 難度仮説: `13`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.03`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「有限アーベル群と、その自己同型で不変な生成集合を初期データとする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自己同型群の複数軌道の和を生成集合とする，(2) 対応する無向Cayleyグラフを作る，(3) 距離が指定範囲以内の頂点を結ぶグラフ冪をとる，(4) 距離2の頂点を結ぶグラフをとる，(5) 組合せLaplacianを群環上に表す，(6) 指標表で同時対角化してスペクトルを得る，(7) スペクトルモーメント列を作る，(8) 閉歩道数と原始閉路数を抽出する，(9) 閉路数列の合同不変量を抽出する。最後に、閉路数列が指定合同周期を持つ場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `AutomorphismOrbitConnection → CayleyConstruction → GraphPower → DistanceTwoGraph → LaplacianOperator → CharacterDiagonalization → SpectralMoments → ClosedWalkExtraction → WalkArithmeticInvariant → WalkCongruenceQuery`

### Cayleyグラフのスペクトル合成（CharacterLevelConnection・CayleyConstruction・ClosedWalkExtraction・WalkArithmeticInvariant）

- ID: `research.autonomous.cayley_spectral.80f94f1601`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `closed_walk_congruence`
- 難度仮説: `16`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0288`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「有限アーベル群と、その自己同型で不変な生成集合を初期データとする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 非自明指標の値が指定軌道に属する元を生成集合とする，(2) 対応する無向Cayleyグラフを作る，(3) 距離2の頂点を結ぶグラフをとる，(4) 距離が指定範囲以内の頂点を結ぶグラフ冪をとる，(5) ループを除いた補グラフをとる，(6) 距離2の頂点を結ぶグラフをとる，(7) ループを除いた補グラフをとる，(8) 隣接作用素を群環上に表す，(9) 指標表で同時対角化してスペクトルを得る，(10) スペクトルモーメント列を作る，(11) 閉歩道数と原始閉路数を抽出する，(12) 閉路数列の合同不変量を抽出する。最後に、閉路数列が指定合同周期を持つ場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CharacterLevelConnection → CayleyConstruction → DistanceTwoGraph → GraphPower → GraphComplement → DistanceTwoGraph → GraphComplement → AdjacencyOperator → CharacterDiagonalization → SpectralMoments → ClosedWalkExtraction → WalkArithmeticInvariant → WalkCongruenceQuery`

### 多項式変換と算術観測（ReciprocalPolynomial・CriticalValuePolynomial・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.8c2fa5ad56`
- 状態: `unresolved_by_mathos`
- 射数: `12`
- 問い: `recurrence_order_drop`
- 難度仮説: `15`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0315`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を逆数へ移す相反多項式をとる，(2) 臨界値を根にもつ消去多項式を作る，(3) 重複度付き根配置へ移す，(4) 根配置からモニック多項式を再構成する，(5) 根を逆数へ移す相反多項式をとる，(6) 導関数をモニックに再正規化する，(7) 重複度付き根配置へ移す，(8) 根の冪和モーメント列を作る，(9) モーメントからHankel行列族を作る，(10) 主小行列式列をとる，(11) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ReciprocalPolynomial → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → ReciprocalPolynomial → DerivativeRenormalization → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 多項式変換と算術観測（GraeffeTransform・ReciprocalPolynomial・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.2f5a9496eb`
- 状態: `unresolved_by_mathos`
- 射数: `11`
- 問い: `recurrence_order_drop`
- 難度仮説: `14`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0313`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を二乗するGraeffe変換を施す，(2) 根を逆数へ移す相反多項式をとる，(3) 重複度付き根配置へ移す，(4) 根配置からモニック多項式を再構成する，(5) 導関数をモニックに再正規化する，(6) 重複度付き根配置へ移す，(7) 根の冪和モーメント列を作る，(8) モーメントからHankel行列族を作る，(9) 主小行列式列をとる，(10) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `GraeffeTransform → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 多項式変換と算術観測（ReciprocalPolynomial・CriticalValuePolynomial・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.f561dfa52f`
- 状態: `unresolved_by_mathos`
- 射数: `10`
- 問い: `recurrence_order_drop`
- 難度仮説: `13`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.033`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を逆数へ移す相反多項式をとる，(2) 臨界値を根にもつ消去多項式を作る，(3) 重複度付き根配置へ移す，(4) 根配置からモニック多項式を再構成する，(5) 重複度付き根配置へ移す，(6) 根の冪和モーメント列を作る，(7) モーメントからHankel行列族を作る，(8) 主小行列式列をとる，(9) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ReciprocalPolynomial → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### Cayleyグラフのスペクトル合成（PowerResidueConnection・CayleyConstruction・ClosedWalkExtraction・WalkArithmeticInvariant）

- ID: `research.autonomous.cayley_spectral.6c7ee79391`
- 状態: `unresolved_by_mathos`
- 射数: `12`
- 問い: `closed_walk_congruence`
- 難度仮説: `15`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0295`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「有限アーベル群と、その自己同型で不変な生成集合を初期データとする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 冪剰余類の自己同型軌道を生成集合とする，(2) 対応する無向Cayleyグラフを作る，(3) ループを除いた補グラフをとる，(4) 距離が指定範囲以内の頂点を結ぶグラフ冪をとる，(5) 距離2の頂点を結ぶグラフをとる，(6) ループを除いた補グラフをとる，(7) 隣接作用素を群環上に表す，(8) 指標表で同時対角化してスペクトルを得る，(9) スペクトルモーメント列を作る，(10) 閉歩道数と原始閉路数を抽出する，(11) 閉路数列の合同不変量を抽出する。最後に、閉路数列が指定合同周期を持つ場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `PowerResidueConnection → CayleyConstruction → GraphComplement → GraphPower → DistanceTwoGraph → GraphComplement → AdjacencyOperator → CharacterDiagonalization → SpectralMoments → ClosedWalkExtraction → WalkArithmeticInvariant → WalkCongruenceQuery`

### Cayleyグラフのスペクトル合成（PowerResidueConnection・CayleyConstruction・ClosedWalkExtraction・WalkArithmeticInvariant）

- ID: `research.autonomous.cayley_spectral.909555fca1`
- 状態: `unresolved_by_mathos`
- 射数: `12`
- 問い: `closed_walk_congruence`
- 難度仮説: `15`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0293`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「有限アーベル群と、その自己同型で不変な生成集合を初期データとする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 冪剰余類の自己同型軌道を生成集合とする，(2) 対応する無向Cayleyグラフを作る，(3) 距離が指定範囲以内の頂点を結ぶグラフ冪をとる，(4) ループを除いた補グラフをとる，(5) 距離が指定範囲以内の頂点を結ぶグラフ冪をとる，(6) ループを除いた補グラフをとる，(7) 組合せLaplacianを群環上に表す，(8) 指標表で同時対角化してスペクトルを得る，(9) スペクトルモーメント列を作る，(10) 閉歩道数と原始閉路数を抽出する，(11) 閉路数列の合同不変量を抽出する。最後に、閉路数列が指定合同周期を持つ場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `PowerResidueConnection → CayleyConstruction → GraphPower → GraphComplement → GraphPower → GraphComplement → LaplacianOperator → CharacterDiagonalization → SpectralMoments → ClosedWalkExtraction → WalkArithmeticInvariant → WalkCongruenceQuery`

### Markov関手と到達時刻不変量（StateLumping・LazyPerturbation・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.a7a78a8a59`
- 状態: `unresolved_by_mathos`
- 射数: `12`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `15`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0291`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自己同型軌道に沿って強 lumping する，(2) 恒等遷移との凸結合でlazy化する，(3) 正の固有関数によるDoob変換を施す，(4) 恒等遷移との凸結合でlazy化する，(5) 定常分布に関する時間反転をとる，(6) 自己同型軌道に沿って強 lumping する，(7) 自身との同期積連鎖を作る，(8) 指定集合で吸収させ過渡核をとる，(9) 過渡核のGreen作用素をとる，(10) 到達時刻の高次モーメント連立系を作る，(11) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `StateLumping → LazyPerturbation → DoobTransform → LazyPerturbation → TimeReversal → StateLumping → ProductChain → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 三角形変換の合成力学（MedialTransform・IncenterMark・SimilarityNormalization・ModuliProjection）

- ID: `research.autonomous.triangle_dynamics.cc816b4e6b`
- 状態: `unresolved_by_mathos`
- 射数: `10`
- 問い: `triangle_transform_fixed_points`
- 難度仮説: `12`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0333`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 三辺の中点三角形へ移す，(2) 内心を標識点として付加する，(3) 標識点を通る三本のcevianの辺上の足をとる，(4) 三点を頂点とする向き付き三角形を作る，(5) 外心を標識点として付加する，(6) 標識点を通る三本のcevianの辺上の足をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 重心・面積・向きを固定して相似正規化する，(9) 相似類のモジュライ点へ射影する。最後に、誘導写像の固定点と有限周期点を相似を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `MedialTransform → IncenterMark → CevianTrace → TriangleFormation → CircumcenterMark → CevianTrace → TriangleFormation → SimilarityNormalization → ModuliProjection → TriangleFixedPointQuery`

### 多項式変換と算術観測（DerivativeRenormalization・GraeffeTransform・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.92012b8cfd`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `recurrence_order_drop`
- 難度仮説: `16`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0305`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 導関数をモニックに再正規化する，(2) 根を二乗するGraeffe変換を施す，(3) 根の重心を0へ移す平行移動共役を施す，(4) 重複度付き根配置へ移す，(5) 根配置からモニック多項式を再構成する，(6) 導関数をモニックに再正規化する，(7) 根を二乗するGraeffe変換を施す，(8) 重複度付き根配置へ移す，(9) 根の冪和モーメント列を作る，(10) モーメントからHankel行列族を作る，(11) 主小行列式列をとる，(12) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DerivativeRenormalization → GraeffeTransform → ShiftConjugacy → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → GraeffeTransform → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### Cayleyグラフのスペクトル合成（AutomorphismOrbitConnection・CayleyConstruction・ClosedWalkExtraction・WalkArithmeticInvariant）

- ID: `research.autonomous.cayley_spectral.5e4474d2d4`
- 状態: `unresolved_by_mathos`
- 射数: `12`
- 問い: `closed_walk_congruence`
- 難度仮説: `15`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.03`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「有限アーベル群と、その自己同型で不変な生成集合を初期データとする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自己同型群の複数軌道の和を生成集合とする，(2) 対応する無向Cayleyグラフを作る，(3) 距離が指定範囲以内の頂点を結ぶグラフ冪をとる，(4) 距離2の頂点を結ぶグラフをとる，(5) 距離が指定範囲以内の頂点を結ぶグラフ冪をとる，(6) 距離2の頂点を結ぶグラフをとる，(7) 隣接作用素を群環上に表す，(8) 指標表で同時対角化してスペクトルを得る，(9) スペクトルモーメント列を作る，(10) 閉歩道数と原始閉路数を抽出する，(11) 閉路数列の合同不変量を抽出する。最後に、閉路数列が指定合同周期を持つ場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `AutomorphismOrbitConnection → CayleyConstruction → GraphPower → DistanceTwoGraph → GraphPower → DistanceTwoGraph → AdjacencyOperator → CharacterDiagonalization → SpectralMoments → ClosedWalkExtraction → WalkArithmeticInvariant → WalkCongruenceQuery`

### 凸体関手の合成力学（PolarDual・DifferenceBody・SteinerSymmetrization・VolumeNormalization）

- ID: `research.autonomous.convex_body.b0ca52efe2`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `16`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0338`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 原点に関する極体をとる，(2) 差体をとる，(3) 自身と極体のMinkowski和をとる，(4) 射影体をとる，(5) 原点に関する極体をとる，(6) 交叉体をとる，(7) 主慣性軸方向にSteiner対称化する，(8) 重心体をとる，(9) 射影体をとる，(10) 差体をとる，(11) 主慣性軸方向にSteiner対称化する，(12) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `PolarDual → DifferenceBody → MinkowskiPolarSum → ProjectionBody → PolarDual → IntersectionBody → SteinerSymmetrization → CentroidBody → ProjectionBody → DifferenceBody → SteinerSymmetrization → VolumeNormalization → ConvexFixedPointQuery`

### 平面代数曲線の合成変換（OffsetCurve・Catacaustic・CircleInversion・ProjectiveDual）

- ID: `research.autonomous.plane_curve.34b028d7c6`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `birational_periodicity`
- 難度仮説: `16`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0285`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 法線方向の代数的平行曲線をとる，(2) 固定光源からの反射光線族の包絡線をとる，(3) 固定非退化二次形式に関する極逆像をとる，(4) 法線方向の代数的平行曲線をとる，(5) 定義多項式のHessian曲線をとる，(6) 固定光源からの反射光線族の包絡線をとる，(7) 固定基準三角形に関する等角共役Cremona像をとる，(8) 法線族の包絡線である発展曲線をとる，(9) 固定基準三角形に関する等角共役Cremona像をとる，(10) 法線族の包絡線である発展曲線をとる，(11) 原点中心の円反転像をとる，(12) 正則接線族の射影双対曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `OffsetCurve → Catacaustic → PolarReciprocal → OffsetCurve → HessianCurve → Catacaustic → IsogonalCremona → Evolute → IsogonalCremona → Evolute → CircleInversion → ProjectiveDual → BirationalPeriodQuery`

### 凸体関手の合成力学（DifferenceBody・PolarDual・ProjectionBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.59f74c4fe3`
- 状態: `unresolved_by_mathos`
- 射数: `12`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `14`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0357`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 差体をとる，(2) 原点に関する極体をとる，(3) 自身と極体のMinkowski和をとる，(4) 原点に関する極体をとる，(5) 自身と極体のMinkowski和をとる，(6) 重心体をとる，(7) 交叉体をとる，(8) 重心体をとる，(9) 交叉体をとる，(10) 射影体をとる，(11) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DifferenceBody → PolarDual → MinkowskiPolarSum → PolarDual → MinkowskiPolarSum → CentroidBody → IntersectionBody → CentroidBody → IntersectionBody → ProjectionBody → VolumeNormalization → ConvexFixedPointQuery`

### 平面代数曲線の合成変換（OffsetCurve・ProjectiveDual・OffsetCurve・IsogonalCremona）

- ID: `research.autonomous.plane_curve.fe3c01722e`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `birational_periodicity`
- 難度仮説: `15`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0284`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 法線方向の代数的平行曲線をとる，(2) 正則接線族の射影双対曲線をとる，(3) 定義多項式のHessian曲線をとる，(4) 法線族の包絡線である発展曲線をとる，(5) 正則接線族の射影双対曲線をとる，(6) 定義多項式のHessian曲線をとる，(7) 固定基準三角形に関する等角共役Cremona像をとる，(8) 射影閉包をとり無限遠点を加える，(9) 基点を避ける一般アフィンチャートへ移す，(10) 法線族の包絡線である発展曲線をとる，(11) 法線方向の代数的平行曲線をとる，(12) 固定基準三角形に関する等角共役Cremona像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `OffsetCurve → ProjectiveDual → HessianCurve → Evolute → ProjectiveDual → HessianCurve → IsogonalCremona → ProjectiveClosure → AffineChartChange → Evolute → OffsetCurve → IsogonalCremona → BirationalPeriodQuery`

### Markov関手と到達時刻不変量（ProductChain・StateLumping・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.8d59a1e1f7`
- 状態: `unresolved_by_mathos`
- 射数: `12`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `15`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.03`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身との同期積連鎖を作る，(2) 自己同型軌道に沿って強 lumping する，(3) 恒等遷移との凸結合でlazy化する，(4) 正の固有関数によるDoob変換を施す，(5) 自己同型軌道に沿って強 lumping する，(6) 正の固有関数によるDoob変換を施す，(7) 自身との同期積連鎖を作る，(8) 指定集合で吸収させ過渡核をとる，(9) 過渡核のGreen作用素をとる，(10) 到達時刻の高次モーメント連立系を作る，(11) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProductChain → StateLumping → LazyPerturbation → DoobTransform → StateLumping → DoobTransform → ProductChain → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 凸体関手の合成力学（MinkowskiPolarSum・CentroidBody・ProjectionBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.76f1c07dad`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `16`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0338`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身と極体のMinkowski和をとる，(2) 重心体をとる，(3) 原点に関する極体をとる，(4) 交叉体をとる，(5) 射影体をとる，(6) 主慣性軸方向にSteiner対称化する，(7) 差体をとる，(8) 重心体をとる，(9) 原点に関する極体をとる，(10) 自身と極体のMinkowski和をとる，(11) 射影体をとる，(12) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `MinkowskiPolarSum → CentroidBody → PolarDual → IntersectionBody → ProjectionBody → SteinerSymmetrization → DifferenceBody → CentroidBody → PolarDual → MinkowskiPolarSum → ProjectionBody → VolumeNormalization → ConvexFixedPointQuery`

### 凸体関手の合成力学（MinkowskiPolarSum・IntersectionBody・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.7890a27099`
- 状態: `unresolved_by_mathos`
- 射数: `12`
- 問い: `convex_body_dynamics`
- 難度仮説: `15`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0296`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身と極体のMinkowski和をとる，(2) 交叉体をとる，(3) 差体をとる，(4) 射影体をとる，(5) 自身と極体のMinkowski和をとる，(6) 射影体をとる，(7) 重心体をとる，(8) 面積と二次モーメントを固定して正規化する，(9) ここまでの凸体関手を反復する，(10) 支持関数の軌道へ移す，(11) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `MinkowskiPolarSum → IntersectionBody → DifferenceBody → ProjectionBody → MinkowskiPolarSum → ProjectionBody → CentroidBody → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### Markov関手と到達時刻不変量（ProductChain・StateLumping・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.563a95a9d1`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `16`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.029`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身との同期積連鎖を作る，(2) 自己同型軌道に沿って強 lumping する，(3) 定常分布に関する時間反転をとる，(4) 恒等遷移との凸結合でlazy化する，(5) 正の固有関数によるDoob変換を施す，(6) 恒等遷移との凸結合でlazy化する，(7) 自己同型軌道に沿って強 lumping する，(8) 自身との同期積連鎖を作る，(9) 指定集合で吸収させ過渡核をとる，(10) 過渡核のGreen作用素をとる，(11) 到達時刻の高次モーメント連立系を作る，(12) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProductChain → StateLumping → TimeReversal → LazyPerturbation → DoobTransform → LazyPerturbation → StateLumping → ProductChain → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 平面代数曲線の合成変換（Catacaustic・HessianCurve・AffineChartChange・CircleInversion）

- ID: `research.autonomous.plane_curve.c47710a1ae`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `birational_periodicity`
- 難度仮説: `16`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0268`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定光源からの反射光線族の包絡線をとる，(2) 定義多項式のHessian曲線をとる，(3) 固定基準三角形に関する等角共役Cremona像をとる，(4) 固定光源からの反射光線族の包絡線をとる，(5) 定義多項式のHessian曲線をとる，(6) 正則接線族の射影双対曲線をとる，(7) 固定非退化二次形式に関する極逆像をとる，(8) 原点中心の円反転像をとる，(9) 法線方向の代数的平行曲線をとる，(10) 射影閉包をとり無限遠点を加える，(11) 基点を避ける一般アフィンチャートへ移す，(12) 原点中心の円反転像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `Catacaustic → HessianCurve → IsogonalCremona → Catacaustic → HessianCurve → ProjectiveDual → PolarReciprocal → CircleInversion → OffsetCurve → ProjectiveClosure → AffineChartChange → CircleInversion → BirationalPeriodQuery`

### 三角形変換の合成力学（SymmedianMark・SideReflectionTrace・SimilarityNormalization・ModuliProjection）

- ID: `research.autonomous.triangle_dynamics.7e1a177a15`
- 状態: `unresolved_by_mathos`
- 射数: `11`
- 問い: `triangle_transform_fixed_points`
- 難度仮説: `14`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0316`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 類似重心を標識点として付加する，(2) 標識点を三辺に関して反射した三点をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 内心を標識点として付加する，(5) 標識点を通る三本のcevianの辺上の足をとる，(6) 三点を頂点とする向き付き三角形を作る，(7) 三辺の中点三角形へ移す，(8) 垂足三角形へ移す，(9) 重心・面積・向きを固定して相似正規化する，(10) 相似類のモジュライ点へ射影する。最後に、誘導写像の固定点と有限周期点を相似を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `SymmedianMark → SideReflectionTrace → TriangleFormation → IncenterMark → CevianTrace → TriangleFormation → MedialTransform → OrthicTransform → SimilarityNormalization → ModuliProjection → TriangleFixedPointQuery`

### 平面代数曲線の合成変換（ProjectiveDual・IsogonalCremona・ProjectiveDual・PolarReciprocal）

- ID: `research.autonomous.plane_curve.bfb045d237`
- 状態: `unresolved_by_mathos`
- 射数: `14`
- 問い: `birational_periodicity`
- 難度仮説: `17`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0283`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 正則接線族の射影双対曲線をとる，(2) 固定基準三角形に関する等角共役Cremona像をとる，(3) 定義多項式のHessian曲線をとる，(4) 固定光源からの反射光線族の包絡線をとる，(5) 法線族の包絡線である発展曲線をとる，(6) 原点中心の円反転像をとる，(7) 法線族の包絡線である発展曲線をとる，(8) 固定基準三角形に関する等角共役Cremona像をとる，(9) 法線方向の代数的平行曲線をとる，(10) 定義多項式のHessian曲線をとる，(11) 原点中心の円反転像をとる，(12) 正則接線族の射影双対曲線をとる，(13) 固定非退化二次形式に関する極逆像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectiveDual → IsogonalCremona → HessianCurve → Catacaustic → Evolute → CircleInversion → Evolute → IsogonalCremona → OffsetCurve → HessianCurve → CircleInversion → ProjectiveDual → PolarReciprocal → BirationalPeriodQuery`

### 三角形変換の合成力学（OrthicTransform・MedialTransform・SimilarityNormalization・ModuliProjection）

- ID: `research.autonomous.triangle_dynamics.2ff1c41479`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `triangle_transform_fixed_points`
- 難度仮説: `16`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0323`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 垂足三角形へ移す，(2) 三辺の中点三角形へ移す，(3) 重心を標識点として付加する，(4) 標識点を通る三本のcevianの辺上の足をとる，(5) 三点を頂点とする向き付き三角形を作る，(6) 内心を標識点として付加する，(7) 標識点を通る三本のcevianの辺上の足をとる，(8) 三点を頂点とする向き付き三角形を作る，(9) 三辺の中点三角形へ移す，(10) 垂足三角形へ移す，(11) 重心・面積・向きを固定して相似正規化する，(12) 相似類のモジュライ点へ射影する。最後に、誘導写像の固定点と有限周期点を相似を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `OrthicTransform → MedialTransform → CentroidMark → CevianTrace → TriangleFormation → IncenterMark → CevianTrace → TriangleFormation → MedialTransform → OrthicTransform → SimilarityNormalization → ModuliProjection → TriangleFixedPointQuery`

### 凸体関手の合成力学（MinkowskiPolarSum・CentroidBody・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.5649a514bb`
- 状態: `unresolved_by_mathos`
- 射数: `12`
- 問い: `convex_body_dynamics`
- 難度仮説: `15`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0286`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身と極体のMinkowski和をとる，(2) 重心体をとる，(3) 主慣性軸方向にSteiner対称化する，(4) 差体をとる，(5) 自身と極体のMinkowski和をとる，(6) 重心体をとる，(7) 射影体をとる，(8) 面積と二次モーメントを固定して正規化する，(9) ここまでの凸体関手を反復する，(10) 支持関数の軌道へ移す，(11) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `MinkowskiPolarSum → CentroidBody → SteinerSymmetrization → DifferenceBody → MinkowskiPolarSum → CentroidBody → ProjectionBody → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### Markov関手と到達時刻不変量（LazyPerturbation・StateLumping・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.d34b1b83e8`
- 状態: `unresolved_by_mathos`
- 射数: `11`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `14`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.03`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 恒等遷移との凸結合でlazy化する，(2) 自己同型軌道に沿って強 lumping する，(3) 定常分布に関する時間反転をとる，(4) 自己同型軌道に沿って強 lumping する，(5) 恒等遷移との凸結合でlazy化する，(6) 正の固有関数によるDoob変換を施す，(7) 指定集合で吸収させ過渡核をとる，(8) 過渡核のGreen作用素をとる，(9) 到達時刻の高次モーメント連立系を作る，(10) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `LazyPerturbation → StateLumping → TimeReversal → StateLumping → LazyPerturbation → DoobTransform → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 平面代数曲線の合成変換（CircleInversion・Catacaustic・HessianCurve・PolarReciprocal）

- ID: `research.autonomous.plane_curve.b480b7cdf6`
- 状態: `unresolved_by_mathos`
- 射数: `14`
- 問い: `birational_periodicity`
- 難度仮説: `17`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0261`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 原点中心の円反転像をとる，(2) 固定光源からの反射光線族の包絡線をとる，(3) 法線族の包絡線である発展曲線をとる，(4) 法線方向の代数的平行曲線をとる，(5) 固定基準三角形に関する等角共役Cremona像をとる，(6) 法線方向の代数的平行曲線をとる，(7) 固定基準三角形に関する等角共役Cremona像をとる，(8) 射影閉包をとり無限遠点を加える，(9) 基点を避ける一般アフィンチャートへ移す，(10) 固定光源からの反射光線族の包絡線をとる，(11) 正則接線族の射影双対曲線をとる，(12) 定義多項式のHessian曲線をとる，(13) 固定非退化二次形式に関する極逆像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CircleInversion → Catacaustic → Evolute → OffsetCurve → IsogonalCremona → OffsetCurve → IsogonalCremona → ProjectiveClosure → AffineChartChange → Catacaustic → ProjectiveDual → HessianCurve → PolarReciprocal → BirationalPeriodQuery`

### 多項式変換と算術観測（DerivativeRenormalization・CriticalValuePolynomial・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.b8c8dc28d0`
- 状態: `unresolved_by_mathos`
- 射数: `14`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `18`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.029`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 導関数をモニックに再正規化する，(2) 臨界値を根にもつ消去多項式を作る，(3) 根を逆数へ移す相反多項式をとる，(4) 根を二乗するGraeffe変換を施す，(5) 臨界値を根にもつ消去多項式を作る，(6) 重複度付き根配置へ移す，(7) 根配置からモニック多項式を再構成する，(8) 重複度付き根配置へ移す，(9) 根の冪和モーメント列を作る，(10) モーメントからHankel行列族を作る，(11) 主小行列式列をとる，(12) 満たす最小線形漸化式を抽出する，(13) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DerivativeRenormalization → CriticalValuePolynomial → ReciprocalPolynomial → GraeffeTransform → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 凸体関手の合成力学（SteinerSymmetrization・DifferenceBody・PolarDual・VolumeNormalization）

- ID: `research.autonomous.convex_body.271d96e1e8`
- 状態: `unresolved_by_mathos`
- 射数: `14`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `17`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0335`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 主慣性軸方向にSteiner対称化する，(2) 差体をとる，(3) 交叉体をとる，(4) 射影体をとる，(5) 重心体をとる，(6) 交叉体をとる，(7) 差体をとる，(8) 主慣性軸方向にSteiner対称化する，(9) 重心体をとる，(10) 原点に関する極体をとる，(11) 自身と極体のMinkowski和をとる，(12) 原点に関する極体をとる，(13) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `SteinerSymmetrization → DifferenceBody → IntersectionBody → ProjectionBody → CentroidBody → IntersectionBody → DifferenceBody → SteinerSymmetrization → CentroidBody → PolarDual → MinkowskiPolarSum → PolarDual → VolumeNormalization → ConvexFixedPointQuery`

### 三角形変換の合成力学（AnticomplementaryTransform・CircumcenterMark・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.aa2d7ecff4`
- 状態: `unresolved_by_mathos`
- 射数: `14`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `18`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0278`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 反中点三角形へ移す，(2) 外心を標識点として付加する，(3) 標識点を通る三本のcevianの辺上の足をとる，(4) 三点を頂点とする向き付き三角形を作る，(5) 三辺の中点三角形へ移す，(6) 類似重心を標識点として付加する，(7) 標識点を三辺に関して反射した三点をとる，(8) 三点を頂点とする向き付き三角形を作る，(9) 重心・面積・向きを固定して相似正規化する，(10) 相似類のモジュライ点へ射影する，(11) ここまでの合成が誘導する写像を反復する，(12) 退化三角形を境界として軌道をコンパクト化する，(13) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `AnticomplementaryTransform → CircumcenterMark → CevianTrace → TriangleFormation → MedialTransform → SymmedianMark → SideReflectionTrace → TriangleFormation → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### Markov関手と到達時刻不変量（StateLumping・TimeReversal・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.8aa138f40e`
- 状態: `unresolved_by_mathos`
- 射数: `14`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `17`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0288`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自己同型軌道に沿って強 lumping する，(2) 定常分布に関する時間反転をとる，(3) 恒等遷移との凸結合でlazy化する，(4) 自身との同期積連鎖を作る，(5) 正の固有関数によるDoob変換を施す，(6) 定常分布に関する時間反転をとる，(7) 正の固有関数によるDoob変換を施す，(8) 自身との同期積連鎖を作る，(9) 恒等遷移との凸結合でlazy化する，(10) 指定集合で吸収させ過渡核をとる，(11) 過渡核のGreen作用素をとる，(12) 到達時刻の高次モーメント連立系を作る，(13) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `StateLumping → TimeReversal → LazyPerturbation → ProductChain → DoobTransform → TimeReversal → DoobTransform → ProductChain → LazyPerturbation → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 平面代数曲線の合成変換（CircleInversion・HessianCurve・IsogonalCremona・HessianCurve）

- ID: `research.autonomous.plane_curve.60dabc128d`
- 状態: `unresolved_by_mathos`
- 射数: `14`
- 問い: `birational_periodicity`
- 難度仮説: `17`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0275`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 原点中心の円反転像をとる，(2) 定義多項式のHessian曲線をとる，(3) 法線方向の代数的平行曲線をとる，(4) 法線族の包絡線である発展曲線をとる，(5) 原点中心の円反転像をとる，(6) 固定光源からの反射光線族の包絡線をとる，(7) 固定基準三角形に関する等角共役Cremona像をとる，(8) 射影閉包をとり無限遠点を加える，(9) 基点を避ける一般アフィンチャートへ移す，(10) 射影閉包をとり無限遠点を加える，(11) 基点を避ける一般アフィンチャートへ移す，(12) 固定基準三角形に関する等角共役Cremona像をとる，(13) 定義多項式のHessian曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CircleInversion → HessianCurve → OffsetCurve → Evolute → CircleInversion → Catacaustic → IsogonalCremona → ProjectiveClosure → AffineChartChange → ProjectiveClosure → AffineChartChange → IsogonalCremona → HessianCurve → BirationalPeriodQuery`

### 凸体関手の合成力学（MinkowskiPolarSum・ProjectionBody・MinkowskiPolarSum・VolumeNormalization）

- ID: `research.autonomous.convex_body.e39ceadb7a`
- 状態: `unresolved_by_mathos`
- 射数: `11`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `13`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0346`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身と極体のMinkowski和をとる，(2) 射影体をとる，(3) 重心体をとる，(4) 差体をとる，(5) 重心体をとる，(6) 原点に関する極体をとる，(7) 主慣性軸方向にSteiner対称化する，(8) 差体をとる，(9) 自身と極体のMinkowski和をとる，(10) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `MinkowskiPolarSum → ProjectionBody → CentroidBody → DifferenceBody → CentroidBody → PolarDual → SteinerSymmetrization → DifferenceBody → MinkowskiPolarSum → VolumeNormalization → ConvexFixedPointQuery`

### Markov関手と到達時刻不変量（ProductChain・TimeReversal・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.6aae2ed4f7`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `16`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.029`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身との同期積連鎖を作る，(2) 定常分布に関する時間反転をとる，(3) 恒等遷移との凸結合でlazy化する，(4) 正の固有関数によるDoob変換を施す，(5) 自己同型軌道に沿って強 lumping する，(6) 自身との同期積連鎖を作る，(7) 定常分布に関する時間反転をとる，(8) 自己同型軌道に沿って強 lumping する，(9) 指定集合で吸収させ過渡核をとる，(10) 過渡核のGreen作用素をとる，(11) 到達時刻の高次モーメント連立系を作る，(12) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProductChain → TimeReversal → LazyPerturbation → DoobTransform → StateLumping → ProductChain → TimeReversal → StateLumping → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 多項式変換と算術観測（CriticalValuePolynomial・DerivativeRenormalization・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.3dd38deccd`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `recurrence_order_drop`
- 難度仮説: `16`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0307`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 臨界値を根にもつ消去多項式を作る，(2) 導関数をモニックに再正規化する，(3) 臨界値を根にもつ消去多項式を作る，(4) 導関数をモニックに再正規化する，(5) 重複度付き根配置へ移す，(6) 根配置からモニック多項式を再構成する，(7) 根を二乗するGraeffe変換を施す，(8) 重複度付き根配置へ移す，(9) 根の冪和モーメント列を作る，(10) モーメントからHankel行列族を作る，(11) 主小行列式列をとる，(12) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CriticalValuePolynomial → DerivativeRenormalization → CriticalValuePolynomial → DerivativeRenormalization → RootMultiset → PolynomialReconstruction → GraeffeTransform → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 三角形変換の合成力学（MedialTransform・CircumcenterMark・SimilarityNormalization・ModuliProjection）

- ID: `research.autonomous.triangle_dynamics.40f514574f`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `triangle_transform_fixed_points`
- 難度仮説: `16`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0315`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 三辺の中点三角形へ移す，(2) 外心を標識点として付加する，(3) 各頂点と標識点が定める円の対応交点をとる，(4) 三点を頂点とする向き付き三角形を作る，(5) 反中点三角形へ移す，(6) 垂足三角形へ移す，(7) 内心を標識点として付加する，(8) 標識点から三辺への垂足三点をとる，(9) 三点を頂点とする向き付き三角形を作る，(10) 傍心三角形へ移す，(11) 重心・面積・向きを固定して相似正規化する，(12) 相似類のモジュライ点へ射影する。最後に、誘導写像の固定点と有限周期点を相似を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `MedialTransform → CircumcenterMark → VertexCircleTrace → TriangleFormation → AnticomplementaryTransform → OrthicTransform → IncenterMark → PedalProjection → TriangleFormation → ExcentralTransform → SimilarityNormalization → ModuliProjection → TriangleFixedPointQuery`

### 平面代数曲線の合成変換（PolarReciprocal・HessianCurve・CircleInversion・HessianCurve）

- ID: `research.autonomous.plane_curve.5ef24a9e3e`
- 状態: `unresolved_by_mathos`
- 射数: `12`
- 問い: `birational_periodicity`
- 難度仮説: `14`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0302`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定非退化二次形式に関する極逆像をとる，(2) 定義多項式のHessian曲線をとる，(3) 法線族の包絡線である発展曲線をとる，(4) 固定非退化二次形式に関する極逆像をとる，(5) 法線方向の代数的平行曲線をとる，(6) 固定光源からの反射光線族の包絡線をとる，(7) 正則接線族の射影双対曲線をとる，(8) 法線族の包絡線である発展曲線をとる，(9) 固定光源からの反射光線族の包絡線をとる，(10) 原点中心の円反転像をとる，(11) 定義多項式のHessian曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `PolarReciprocal → HessianCurve → Evolute → PolarReciprocal → OffsetCurve → Catacaustic → ProjectiveDual → Evolute → Catacaustic → CircleInversion → HessianCurve → BirationalPeriodQuery`

### 多項式変換と算術観測（CriticalValuePolynomial・ShiftConjugacy・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.db3d6ee7bf`
- 状態: `unresolved_by_mathos`
- 射数: `12`
- 問い: `recurrence_order_drop`
- 難度仮説: `15`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0301`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 臨界値を根にもつ消去多項式を作る，(2) 根の重心を0へ移す平行移動共役を施す，(3) 臨界値を根にもつ消去多項式を作る，(4) 根を逆数へ移す相反多項式をとる，(5) 根を二乗するGraeffe変換を施す，(6) 導関数をモニックに再正規化する，(7) 重複度付き根配置へ移す，(8) 根の冪和モーメント列を作る，(9) モーメントからHankel行列族を作る，(10) 主小行列式列をとる，(11) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CriticalValuePolynomial → ShiftConjugacy → CriticalValuePolynomial → ReciprocalPolynomial → GraeffeTransform → DerivativeRenormalization → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 三角形変換の合成力学（CircumcenterMark・CevianTrace・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.f1b2e219dc`
- 状態: `unresolved_by_mathos`
- 射数: `15`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `19`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0276`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 外心を標識点として付加する，(2) 標識点を通る三本のcevianの辺上の足をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 重心を標識点として付加する，(5) 各頂点と標識点が定める円の対応交点をとる，(6) 三点を頂点とする向き付き三角形を作る，(7) 垂足三角形へ移す，(8) 三辺の中点三角形へ移す，(9) 垂足三角形へ移す，(10) 重心・面積・向きを固定して相似正規化する，(11) 相似類のモジュライ点へ射影する，(12) ここまでの合成が誘導する写像を反復する，(13) 退化三角形を境界として軌道をコンパクト化する，(14) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CircumcenterMark → CevianTrace → TriangleFormation → CentroidMark → VertexCircleTrace → TriangleFormation → OrthicTransform → MedialTransform → OrthicTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 凸体関手の合成力学（CentroidBody・MinkowskiPolarSum・ProjectionBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.d9d2a80f31`
- 状態: `unresolved_by_mathos`
- 射数: `14`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `17`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0335`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重心体をとる，(2) 自身と極体のMinkowski和をとる，(3) 主慣性軸方向にSteiner対称化する，(4) 自身と極体のMinkowski和をとる，(5) 主慣性軸方向にSteiner対称化する，(6) 交叉体をとる，(7) 射影体をとる，(8) 交叉体をとる，(9) 重心体をとる，(10) 差体をとる，(11) 原点に関する極体をとる，(12) 射影体をとる，(13) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CentroidBody → MinkowskiPolarSum → SteinerSymmetrization → MinkowskiPolarSum → SteinerSymmetrization → IntersectionBody → ProjectionBody → IntersectionBody → CentroidBody → DifferenceBody → PolarDual → ProjectionBody → VolumeNormalization → ConvexFixedPointQuery`

### Markov関手と到達時刻不変量（LazyPerturbation・ProductChain・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.4c7e718de4`
- 状態: `unresolved_by_mathos`
- 射数: `12`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `15`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0304`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 恒等遷移との凸結合でlazy化する，(2) 自身との同期積連鎖を作る，(3) 正の固有関数によるDoob変換を施す，(4) 自身との同期積連鎖を作る，(5) 定常分布に関する時間反転をとる，(6) 正の固有関数によるDoob変換を施す，(7) 定常分布に関する時間反転をとる，(8) 指定集合で吸収させ過渡核をとる，(9) 過渡核のGreen作用素をとる，(10) 到達時刻の高次モーメント連立系を作る，(11) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `LazyPerturbation → ProductChain → DoobTransform → ProductChain → TimeReversal → DoobTransform → TimeReversal → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 平面代数曲線の合成変換（IsogonalCremona・PolarReciprocal・Catacaustic・HessianCurve）

- ID: `research.autonomous.plane_curve.e3bdf73157`
- 状態: `unresolved_by_mathos`
- 射数: `14`
- 問い: `birational_periodicity`
- 難度仮説: `17`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0268`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定基準三角形に関する等角共役Cremona像をとる，(2) 固定非退化二次形式に関する極逆像をとる，(3) 固定光源からの反射光線族の包絡線をとる，(4) 定義多項式のHessian曲線をとる，(5) 射影閉包をとり無限遠点を加える，(6) 基点を避ける一般アフィンチャートへ移す，(7) 原点中心の円反転像をとる，(8) 法線族の包絡線である発展曲線をとる，(9) 射影閉包をとり無限遠点を加える，(10) 基点を避ける一般アフィンチャートへ移す，(11) 法線方向の代数的平行曲線をとる，(12) 固定光源からの反射光線族の包絡線をとる，(13) 定義多項式のHessian曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IsogonalCremona → PolarReciprocal → Catacaustic → HessianCurve → ProjectiveClosure → AffineChartChange → CircleInversion → Evolute → ProjectiveClosure → AffineChartChange → OffsetCurve → Catacaustic → HessianCurve → BirationalPeriodQuery`

### 多項式変換と算術観測（ReciprocalPolynomial・GraeffeTransform・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.8b34eac40f`
- 状態: `unresolved_by_mathos`
- 射数: `15`
- 問い: `recurrence_order_drop`
- 難度仮説: `18`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0295`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を逆数へ移す相反多項式をとる，(2) 根を二乗するGraeffe変換を施す，(3) 根を逆数へ移す相反多項式をとる，(4) 根の重心を0へ移す平行移動共役を施す，(5) 根を二乗するGraeffe変換を施す，(6) 重複度付き根配置へ移す，(7) 根配置からモニック多項式を再構成する，(8) 根の重心を0へ移す平行移動共役を施す，(9) 臨界値を根にもつ消去多項式を作る，(10) 重複度付き根配置へ移す，(11) 根の冪和モーメント列を作る，(12) モーメントからHankel行列族を作る，(13) 主小行列式列をとる，(14) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ReciprocalPolynomial → GraeffeTransform → ReciprocalPolynomial → ShiftConjugacy → GraeffeTransform → RootMultiset → PolynomialReconstruction → ShiftConjugacy → CriticalValuePolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 三角形変換の合成力学（AnticomplementaryTransform・IncenterMark・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.5c5411644b`
- 状態: `unresolved_by_mathos`
- 射数: `14`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `18`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0281`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 反中点三角形へ移す，(2) 内心を標識点として付加する，(3) 標識点を三辺に関して反射した三点をとる，(4) 三点を頂点とする向き付き三角形を作る，(5) 垂心を標識点として付加する，(6) 標識点を通る三本のcevianの辺上の足をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 反中点三角形へ移す，(9) 重心・面積・向きを固定して相似正規化する，(10) 相似類のモジュライ点へ射影する，(11) ここまでの合成が誘導する写像を反復する，(12) 退化三角形を境界として軌道をコンパクト化する，(13) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `AnticomplementaryTransform → IncenterMark → SideReflectionTrace → TriangleFormation → OrthocenterMark → CevianTrace → TriangleFormation → AnticomplementaryTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 凸体関手の合成力学（DifferenceBody・PolarDual・ProjectionBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.005ca1664a`
- 状態: `unresolved_by_mathos`
- 射数: `15`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `18`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0332`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 差体をとる，(2) 原点に関する極体をとる，(3) 主慣性軸方向にSteiner対称化する，(4) 差体をとる，(5) 原点に関する極体をとる，(6) 自身と極体のMinkowski和をとる，(7) 重心体をとる，(8) 自身と極体のMinkowski和をとる，(9) 重心体をとる，(10) 射影体をとる，(11) 交叉体をとる，(12) 主慣性軸方向にSteiner対称化する，(13) 射影体をとる，(14) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DifferenceBody → PolarDual → SteinerSymmetrization → DifferenceBody → PolarDual → MinkowskiPolarSum → CentroidBody → MinkowskiPolarSum → CentroidBody → ProjectionBody → IntersectionBody → SteinerSymmetrization → ProjectionBody → VolumeNormalization → ConvexFixedPointQuery`

### Markov関手と到達時刻不変量（StateLumping・TimeReversal・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.53e38db338`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `16`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.029`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自己同型軌道に沿って強 lumping する，(2) 定常分布に関する時間反転をとる，(3) 自身との同期積連鎖を作る，(4) 定常分布に関する時間反転をとる，(5) 自身との同期積連鎖を作る，(6) 恒等遷移との凸結合でlazy化する，(7) 自己同型軌道に沿って強 lumping する，(8) 正の固有関数によるDoob変換を施す，(9) 指定集合で吸収させ過渡核をとる，(10) 過渡核のGreen作用素をとる，(11) 到達時刻の高次モーメント連立系を作る，(12) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `StateLumping → TimeReversal → ProductChain → TimeReversal → ProductChain → LazyPerturbation → StateLumping → DoobTransform → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### Cayleyグラフのスペクトル合成（AutomorphismOrbitConnection・CayleyConstruction・ClosedWalkExtraction・WalkArithmeticInvariant）

- ID: `research.autonomous.cayley_spectral.1f051bf78f`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `closed_walk_congruence`
- 難度仮説: `16`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0288`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「有限アーベル群と、その自己同型で不変な生成集合を初期データとする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自己同型群の複数軌道の和を生成集合とする，(2) 対応する無向Cayleyグラフを作る，(3) ループを除いた補グラフをとる，(4) 距離が指定範囲以内の頂点を結ぶグラフ冪をとる，(5) 距離2の頂点を結ぶグラフをとる，(6) ループを除いた補グラフをとる，(7) 距離が指定範囲以内の頂点を結ぶグラフ冪をとる，(8) 組合せLaplacianを群環上に表す，(9) 指標表で同時対角化してスペクトルを得る，(10) スペクトルモーメント列を作る，(11) 閉歩道数と原始閉路数を抽出する，(12) 閉路数列の合同不変量を抽出する。最後に、閉路数列が指定合同周期を持つ場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `AutomorphismOrbitConnection → CayleyConstruction → GraphComplement → GraphPower → DistanceTwoGraph → GraphComplement → GraphPower → LaplacianOperator → CharacterDiagonalization → SpectralMoments → ClosedWalkExtraction → WalkArithmeticInvariant → WalkCongruenceQuery`

### 三角形変換の合成力学（OrthocenterMark・PedalProjection・SimilarityNormalization・ModuliProjection）

- ID: `research.autonomous.triangle_dynamics.af7aad363c`
- 状態: `unresolved_by_mathos`
- 射数: `12`
- 問い: `triangle_transform_fixed_points`
- 難度仮説: `15`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0316`
- 照合方式: `exact_3gram_jaccard`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 垂心を標識点として付加する，(2) 標識点から三辺への垂足三点をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 三辺の中点三角形へ移す，(5) 内心を標識点として付加する，(6) 標識点を通る三本のcevianの辺上の足をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 垂足三角形へ移す，(9) 反中点三角形へ移す，(10) 重心・面積・向きを固定して相似正規化する，(11) 相似類のモジュライ点へ射影する。最後に、誘導写像の固定点と有限周期点を相似を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `OrthocenterMark → PedalProjection → TriangleFormation → MedialTransform → IncenterMark → CevianTrace → TriangleFormation → OrthicTransform → AnticomplementaryTransform → SimilarityNormalization → ModuliProjection → TriangleFixedPointQuery`

### Cayleyグラフのスペクトル合成（AutomorphismOrbitConnection・CayleyConstruction・ClosedWalkExtraction・WalkArithmeticInvariant）

- ID: `research.autonomous.cayley_spectral.362cd1ebfd`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `closed_walk_congruence`
- 難度仮説: `16`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0625`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限アーベル群と、その自己同型で不変な生成集合を初期データとする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自己同型群の複数軌道の和を生成集合とする，(2) 対応する無向Cayleyグラフを作る，(3) 距離が指定範囲以内の頂点を結ぶグラフ冪をとる，(4) 距離2の頂点を結ぶグラフをとる，(5) 距離が指定範囲以内の頂点を結ぶグラフ冪をとる，(6) ループを除いた補グラフをとる，(7) 距離2の頂点を結ぶグラフをとる，(8) 組合せLaplacianを群環上に表す，(9) 指標表で同時対角化してスペクトルを得る，(10) スペクトルモーメント列を作る，(11) 閉歩道数と原始閉路数を抽出する，(12) 閉路数列の合同不変量を抽出する。最後に、閉路数列が指定合同周期を持つ場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `AutomorphismOrbitConnection → CayleyConstruction → GraphPower → DistanceTwoGraph → GraphPower → GraphComplement → DistanceTwoGraph → LaplacianOperator → CharacterDiagonalization → SpectralMoments → ClosedWalkExtraction → WalkArithmeticInvariant → WalkCongruenceQuery`

### 凸体関手の合成力学（SteinerSymmetrization・CentroidBody・IntersectionBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.290a4969dd`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `15`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 主慣性軸方向にSteiner対称化する，(2) 重心体をとる，(3) 自身と極体のMinkowski和をとる，(4) 重心体をとる，(5) 自身と極体のMinkowski和をとる，(6) 主慣性軸方向にSteiner対称化する，(7) 原点に関する極体をとる，(8) 交叉体をとる，(9) 原点に関する極体をとる，(10) 射影体をとる，(11) 交叉体をとる，(12) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `SteinerSymmetrization → CentroidBody → MinkowskiPolarSum → CentroidBody → MinkowskiPolarSum → SteinerSymmetrization → PolarDual → IntersectionBody → PolarDual → ProjectionBody → IntersectionBody → VolumeNormalization → ConvexFixedPointQuery`

### 平面代数曲線の合成変換（Evolute・ProjectiveClosure・ProjectiveDual・OffsetCurve）

- ID: `research.autonomous.plane_curve.195bb3a6a3`
- 状態: `unresolved_by_mathos`
- 射数: `12`
- 問い: `birational_periodicity`
- 難度仮説: `14`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 法線族の包絡線である発展曲線をとる，(2) 射影閉包をとり無限遠点を加える，(3) 基点を避ける一般アフィンチャートへ移す，(4) 法線族の包絡線である発展曲線をとる，(5) 法線方向の代数的平行曲線をとる，(6) 定義多項式のHessian曲線をとる，(7) 射影閉包をとり無限遠点を加える，(8) 基点を避ける一般アフィンチャートへ移す，(9) 固定光源からの反射光線族の包絡線をとる，(10) 正則接線族の射影双対曲線をとる，(11) 法線方向の代数的平行曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `Evolute → ProjectiveClosure → AffineChartChange → Evolute → OffsetCurve → HessianCurve → ProjectiveClosure → AffineChartChange → Catacaustic → ProjectiveDual → OffsetCurve → BirationalPeriodQuery`

### 多項式変換と算術観測（GraeffeTransform・DerivativeRenormalization・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.b21586a76f`
- 状態: `unresolved_by_mathos`
- 射数: `14`
- 問い: `recurrence_order_drop`
- 難度仮説: `17`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を二乗するGraeffe変換を施す，(2) 導関数をモニックに再正規化する，(3) 根を逆数へ移す相反多項式をとる，(4) 導関数をモニックに再正規化する，(5) 重複度付き根配置へ移す，(6) 根配置からモニック多項式を再構成する，(7) 根を二乗するGraeffe変換を施す，(8) 根を逆数へ移す相反多項式をとる，(9) 重複度付き根配置へ移す，(10) 根の冪和モーメント列を作る，(11) モーメントからHankel行列族を作る，(12) 主小行列式列をとる，(13) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `GraeffeTransform → DerivativeRenormalization → ReciprocalPolynomial → DerivativeRenormalization → RootMultiset → PolynomialReconstruction → GraeffeTransform → ReciprocalPolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### Markov関手と到達時刻不変量（LazyPerturbation・DoobTransform・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.6ce48d0c1a`
- 状態: `unresolved_by_mathos`
- 射数: `14`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `17`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 恒等遷移との凸結合でlazy化する，(2) 正の固有関数によるDoob変換を施す，(3) 定常分布に関する時間反転をとる，(4) 自己同型軌道に沿って強 lumping する，(5) 定常分布に関する時間反転をとる，(6) 恒等遷移との凸結合でlazy化する，(7) 自身との同期積連鎖を作る，(8) 正の固有関数によるDoob変換を施す，(9) 自身との同期積連鎖を作る，(10) 指定集合で吸収させ過渡核をとる，(11) 過渡核のGreen作用素をとる，(12) 到達時刻の高次モーメント連立系を作る，(13) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `LazyPerturbation → DoobTransform → TimeReversal → StateLumping → TimeReversal → LazyPerturbation → ProductChain → DoobTransform → ProductChain → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 三角形変換の合成力学（IncenterMark・VertexCircleTrace・SimilarityNormalization・ModuliProjection）

- ID: `research.autonomous.triangle_dynamics.741c2c243d`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `triangle_transform_fixed_points`
- 難度仮説: `15`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 内心を標識点として付加する，(2) 各頂点と標識点が定める円の対応交点をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 垂足三角形へ移す，(5) 内心を標識点として付加する，(6) 各頂点と標識点が定める円の対応交点をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 反中点三角形へ移す，(9) 傍心三角形へ移す，(10) 反中点三角形へ移す，(11) 重心・面積・向きを固定して相似正規化する，(12) 相似類のモジュライ点へ射影する。最後に、誘導写像の固定点と有限周期点を相似を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IncenterMark → VertexCircleTrace → TriangleFormation → OrthicTransform → IncenterMark → VertexCircleTrace → TriangleFormation → AnticomplementaryTransform → ExcentralTransform → AnticomplementaryTransform → SimilarityNormalization → ModuliProjection → TriangleFixedPointQuery`

### 凸体関手の合成力学（ProjectionBody・MinkowskiPolarSum・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.99f3f8ad1d`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `convex_body_dynamics`
- 難度仮説: `16`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 射影体をとる，(2) 自身と極体のMinkowski和をとる，(3) 交叉体をとる，(4) 自身と極体のMinkowski和をとる，(5) 交叉体をとる，(6) 原点に関する極体をとる，(7) 主慣性軸方向にSteiner対称化する，(8) 射影体をとる，(9) 面積と二次モーメントを固定して正規化する，(10) ここまでの凸体関手を反復する，(11) 支持関数の軌道へ移す，(12) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectionBody → MinkowskiPolarSum → IntersectionBody → MinkowskiPolarSum → IntersectionBody → PolarDual → SteinerSymmetrization → ProjectionBody → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 多項式変換と算術観測（DerivativeRenormalization・GraeffeTransform・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.668f6a60ab`
- 状態: `unresolved_by_mathos`
- 射数: `12`
- 問い: `recurrence_order_drop`
- 難度仮説: `15`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 導関数をモニックに再正規化する，(2) 根を二乗するGraeffe変換を施す，(3) 導関数をモニックに再正規化する，(4) 臨界値を根にもつ消去多項式を作る，(5) 重複度付き根配置へ移す，(6) 根配置からモニック多項式を再構成する，(7) 重複度付き根配置へ移す，(8) 根の冪和モーメント列を作る，(9) モーメントからHankel行列族を作る，(10) 主小行列式列をとる，(11) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DerivativeRenormalization → GraeffeTransform → DerivativeRenormalization → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### Markov関手と到達時刻不変量（ProductChain・LazyPerturbation・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.eecb578508`
- 状態: `unresolved_by_mathos`
- 射数: `12`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `15`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身との同期積連鎖を作る，(2) 恒等遷移との凸結合でlazy化する，(3) 正の固有関数によるDoob変換を施す，(4) 自身との同期積連鎖を作る，(5) 恒等遷移との凸結合でlazy化する，(6) 定常分布に関する時間反転をとる，(7) 正の固有関数によるDoob変換を施す，(8) 指定集合で吸収させ過渡核をとる，(9) 過渡核のGreen作用素をとる，(10) 到達時刻の高次モーメント連立系を作る，(11) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProductChain → LazyPerturbation → DoobTransform → ProductChain → LazyPerturbation → TimeReversal → DoobTransform → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### Cayleyグラフのスペクトル合成（CharacterLevelConnection・CayleyConstruction・ClosedWalkExtraction・WalkArithmeticInvariant）

- ID: `research.autonomous.cayley_spectral.4babf269ea`
- 状態: `unresolved_by_mathos`
- 射数: `12`
- 問い: `closed_walk_congruence`
- 難度仮説: `15`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0625`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限アーベル群と、その自己同型で不変な生成集合を初期データとする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 非自明指標の値が指定軌道に属する元を生成集合とする，(2) 対応する無向Cayleyグラフを作る，(3) ループを除いた補グラフをとる，(4) 距離が指定範囲以内の頂点を結ぶグラフ冪をとる，(5) 距離2の頂点を結ぶグラフをとる，(6) ループを除いた補グラフをとる，(7) 組合せLaplacianを群環上に表す，(8) 指標表で同時対角化してスペクトルを得る，(9) スペクトルモーメント列を作る，(10) 閉歩道数と原始閉路数を抽出する，(11) 閉路数列の合同不変量を抽出する。最後に、閉路数列が指定合同周期を持つ場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CharacterLevelConnection → CayleyConstruction → GraphComplement → GraphPower → DistanceTwoGraph → GraphComplement → LaplacianOperator → CharacterDiagonalization → SpectralMoments → ClosedWalkExtraction → WalkArithmeticInvariant → WalkCongruenceQuery`

### 平面代数曲線の合成変換（HessianCurve・CircleInversion・IsogonalCremona・Evolute）

- ID: `research.autonomous.plane_curve.d7a27ff8ee`
- 状態: `unresolved_by_mathos`
- 射数: `12`
- 問い: `birational_periodicity`
- 難度仮説: `15`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 定義多項式のHessian曲線をとる，(2) 原点中心の円反転像をとる，(3) 固定非退化二次形式に関する極逆像をとる，(4) 射影閉包をとり無限遠点を加える，(5) 基点を避ける一般アフィンチャートへ移す，(6) 法線方向の代数的平行曲線をとる，(7) 正則接線族の射影双対曲線をとる，(8) 固定基準三角形に関する等角共役Cremona像をとる，(9) 定義多項式のHessian曲線をとる，(10) 固定基準三角形に関する等角共役Cremona像をとる，(11) 法線族の包絡線である発展曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `HessianCurve → CircleInversion → PolarReciprocal → ProjectiveClosure → AffineChartChange → OffsetCurve → ProjectiveDual → IsogonalCremona → HessianCurve → IsogonalCremona → Evolute → BirationalPeriodQuery`

### Cayleyグラフのスペクトル合成（CharacterLevelConnection・CayleyConstruction・ClosedWalkExtraction・WalkArithmeticInvariant）

- ID: `research.autonomous.cayley_spectral.d905241a79`
- 状態: `unresolved_by_mathos`
- 射数: `14`
- 問い: `closed_walk_congruence`
- 難度仮説: `17`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0625`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限アーベル群と、その自己同型で不変な生成集合を初期データとする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 非自明指標の値が指定軌道に属する元を生成集合とする，(2) 対応する無向Cayleyグラフを作る，(3) 距離2の頂点を結ぶグラフをとる，(4) ループを除いた補グラフをとる，(5) 距離が指定範囲以内の頂点を結ぶグラフ冪をとる，(6) ループを除いた補グラフをとる，(7) 距離が指定範囲以内の頂点を結ぶグラフ冪をとる，(8) 距離2の頂点を結ぶグラフをとる，(9) 隣接作用素を群環上に表す，(10) 指標表で同時対角化してスペクトルを得る，(11) スペクトルモーメント列を作る，(12) 閉歩道数と原始閉路数を抽出する，(13) 閉路数列の合同不変量を抽出する。最後に、閉路数列が指定合同周期を持つ場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CharacterLevelConnection → CayleyConstruction → DistanceTwoGraph → GraphComplement → GraphPower → GraphComplement → GraphPower → DistanceTwoGraph → AdjacencyOperator → CharacterDiagonalization → SpectralMoments → ClosedWalkExtraction → WalkArithmeticInvariant → WalkCongruenceQuery`

### 凸体関手の合成力学（ProjectionBody・MinkowskiPolarSum・SteinerSymmetrization・VolumeNormalization）

- ID: `research.autonomous.convex_body.d598e563a2`
- 状態: `unresolved_by_mathos`
- 射数: `14`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `17`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 射影体をとる，(2) 自身と極体のMinkowski和をとる，(3) 重心体をとる，(4) 原点に関する極体をとる，(5) 射影体をとる，(6) 交叉体をとる，(7) 原点に関する極体をとる，(8) 交叉体をとる，(9) 差体をとる，(10) 自身と極体のMinkowski和をとる，(11) 重心体をとる，(12) 主慣性軸方向にSteiner対称化する，(13) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectionBody → MinkowskiPolarSum → CentroidBody → PolarDual → ProjectionBody → IntersectionBody → PolarDual → IntersectionBody → DifferenceBody → MinkowskiPolarSum → CentroidBody → SteinerSymmetrization → VolumeNormalization → ConvexFixedPointQuery`

### Markov関手と到達時刻不変量（LazyPerturbation・DoobTransform・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.16e08c8eaf`
- 状態: `unresolved_by_mathos`
- 射数: `14`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `17`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 恒等遷移との凸結合でlazy化する，(2) 正の固有関数によるDoob変換を施す，(3) 定常分布に関する時間反転をとる，(4) 正の固有関数によるDoob変換を施す，(5) 自身との同期積連鎖を作る，(6) 自己同型軌道に沿って強 lumping する，(7) 恒等遷移との凸結合でlazy化する，(8) 自身との同期積連鎖を作る，(9) 自己同型軌道に沿って強 lumping する，(10) 指定集合で吸収させ過渡核をとる，(11) 過渡核のGreen作用素をとる，(12) 到達時刻の高次モーメント連立系を作る，(13) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `LazyPerturbation → DoobTransform → TimeReversal → DoobTransform → ProductChain → StateLumping → LazyPerturbation → ProductChain → StateLumping → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 多項式変換と算術観測（ShiftConjugacy・ReciprocalPolynomial・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.2a6c6100ad`
- 状態: `unresolved_by_mathos`
- 射数: `16`
- 問い: `recurrence_order_drop`
- 難度仮説: `19`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根の重心を0へ移す平行移動共役を施す，(2) 根を逆数へ移す相反多項式をとる，(3) 重複度付き根配置へ移す，(4) 根配置からモニック多項式を再構成する，(5) 根の重心を0へ移す平行移動共役を施す，(6) 根を二乗するGraeffe変換を施す，(7) 臨界値を根にもつ消去多項式を作る，(8) 根を二乗するGraeffe変換を施す，(9) 根を逆数へ移す相反多項式をとる，(10) 臨界値を根にもつ消去多項式を作る，(11) 重複度付き根配置へ移す，(12) 根の冪和モーメント列を作る，(13) モーメントからHankel行列族を作る，(14) 主小行列式列をとる，(15) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ShiftConjugacy → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → ShiftConjugacy → GraeffeTransform → CriticalValuePolynomial → GraeffeTransform → ReciprocalPolynomial → CriticalValuePolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 平面代数曲線の合成変換（CircleInversion・OffsetCurve・ProjectiveClosure・AffineChartChange）

- ID: `research.autonomous.plane_curve.94eb108714`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `birational_periodicity`
- 難度仮説: `16`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 原点中心の円反転像をとる，(2) 法線方向の代数的平行曲線をとる，(3) 正則接線族の射影双対曲線をとる，(4) 法線方向の代数的平行曲線をとる，(5) 固定基準三角形に関する等角共役Cremona像をとる，(6) 固定非退化二次形式に関する極逆像をとる，(7) 原点中心の円反転像をとる，(8) 固定非退化二次形式に関する極逆像をとる，(9) 正則接線族の射影双対曲線をとる，(10) 固定光源からの反射光線族の包絡線をとる，(11) 射影閉包をとり無限遠点を加える，(12) 基点を避ける一般アフィンチャートへ移す。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CircleInversion → OffsetCurve → ProjectiveDual → OffsetCurve → IsogonalCremona → PolarReciprocal → CircleInversion → PolarReciprocal → ProjectiveDual → Catacaustic → ProjectiveClosure → AffineChartChange → BirationalPeriodQuery`

### 三角形変換の合成力学（IncenterMark・CevianTrace・SimilarityNormalization・ModuliProjection）

- ID: `research.autonomous.triangle_dynamics.d536cd309b`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `triangle_transform_fixed_points`
- 難度仮説: `16`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 内心を標識点として付加する，(2) 標識点を通る三本のcevianの辺上の足をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 三辺の中点三角形へ移す，(5) 外心を標識点として付加する，(6) 標識点を三辺に関して反射した三点をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 傍心三角形へ移す，(9) 反中点三角形へ移す，(10) 垂足三角形へ移す，(11) 重心・面積・向きを固定して相似正規化する，(12) 相似類のモジュライ点へ射影する。最後に、誘導写像の固定点と有限周期点を相似を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IncenterMark → CevianTrace → TriangleFormation → MedialTransform → CircumcenterMark → SideReflectionTrace → TriangleFormation → ExcentralTransform → AnticomplementaryTransform → OrthicTransform → SimilarityNormalization → ModuliProjection → TriangleFixedPointQuery`

### 三角形変換の合成力学（CircumcenterMark・VertexCircleTrace・SimilarityNormalization・ModuliProjection）

- ID: `research.autonomous.triangle_dynamics.62e16559a4`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `triangle_transform_fixed_points`
- 難度仮説: `16`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0625`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 外心を標識点として付加する，(2) 各頂点と標識点が定める円の対応交点をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 三辺の中点三角形へ移す，(5) 外心を標識点として付加する，(6) 標識点から三辺への垂足三点をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 傍心三角形へ移す，(9) 三辺の中点三角形へ移す，(10) 傍心三角形へ移す，(11) 重心・面積・向きを固定して相似正規化する，(12) 相似類のモジュライ点へ射影する。最後に、誘導写像の固定点と有限周期点を相似を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CircumcenterMark → VertexCircleTrace → TriangleFormation → MedialTransform → CircumcenterMark → PedalProjection → TriangleFormation → ExcentralTransform → MedialTransform → ExcentralTransform → SimilarityNormalization → ModuliProjection → TriangleFixedPointQuery`

### 多項式変換と算術観測（GraeffeTransform・ShiftConjugacy・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.c2dc27b068`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `17`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を二乗するGraeffe変換を施す，(2) 根の重心を0へ移す平行移動共役を施す，(3) 根を逆数へ移す相反多項式をとる，(4) 導関数をモニックに再正規化する，(5) 臨界値を根にもつ消去多項式を作る，(6) 根の重心を0へ移す平行移動共役を施す，(7) 重複度付き根配置へ移す，(8) 根の冪和モーメント列を作る，(9) モーメントからHankel行列族を作る，(10) 主小行列式列をとる，(11) 満たす最小線形漸化式を抽出する，(12) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `GraeffeTransform → ShiftConjugacy → ReciprocalPolynomial → DerivativeRenormalization → CriticalValuePolynomial → ShiftConjugacy → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 平面代数曲線の合成変換（CircleInversion・PolarReciprocal・IsogonalCremona・OffsetCurve）

- ID: `research.autonomous.plane_curve.4f6ebe9de1`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `birational_periodicity`
- 難度仮説: `16`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 原点中心の円反転像をとる，(2) 固定非退化二次形式に関する極逆像をとる，(3) 原点中心の円反転像をとる，(4) 射影閉包をとり無限遠点を加える，(5) 基点を避ける一般アフィンチャートへ移す，(6) 固定非退化二次形式に関する極逆像をとる，(7) 定義多項式のHessian曲線をとる，(8) 固定光源からの反射光線族の包絡線をとる，(9) 固定基準三角形に関する等角共役Cremona像をとる，(10) 法線方向の代数的平行曲線をとる，(11) 固定基準三角形に関する等角共役Cremona像をとる，(12) 法線方向の代数的平行曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CircleInversion → PolarReciprocal → CircleInversion → ProjectiveClosure → AffineChartChange → PolarReciprocal → HessianCurve → Catacaustic → IsogonalCremona → OffsetCurve → IsogonalCremona → OffsetCurve → BirationalPeriodQuery`

### 凸体関手の合成力学（CentroidBody・PolarDual・SteinerSymmetrization・VolumeNormalization）

- ID: `research.autonomous.convex_body.95f1a6ef0e`
- 状態: `unresolved_by_mathos`
- 射数: `16`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `19`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重心体をとる，(2) 原点に関する極体をとる，(3) 交叉体をとる，(4) 主慣性軸方向にSteiner対称化する，(5) 射影体をとる，(6) 原点に関する極体をとる，(7) 交叉体をとる，(8) 重心体をとる，(9) 自身と極体のMinkowski和をとる，(10) 差体をとる，(11) 自身と極体のMinkowski和をとる，(12) 射影体をとる，(13) 差体をとる，(14) 主慣性軸方向にSteiner対称化する，(15) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CentroidBody → PolarDual → IntersectionBody → SteinerSymmetrization → ProjectionBody → PolarDual → IntersectionBody → CentroidBody → MinkowskiPolarSum → DifferenceBody → MinkowskiPolarSum → ProjectionBody → DifferenceBody → SteinerSymmetrization → VolumeNormalization → ConvexFixedPointQuery`

### Markov関手と到達時刻不変量（DoobTransform・ProductChain・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.8dba6a278c`
- 状態: `unresolved_by_mathos`
- 射数: `16`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `19`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 正の固有関数によるDoob変換を施す，(2) 自身との同期積連鎖を作る，(3) 自己同型軌道に沿って強 lumping する，(4) 正の固有関数によるDoob変換を施す，(5) 自己同型軌道に沿って強 lumping する，(6) 恒等遷移との凸結合でlazy化する，(7) 自身との同期積連鎖を作る，(8) 定常分布に関する時間反転をとる，(9) 恒等遷移との凸結合でlazy化する，(10) 定常分布に関する時間反転をとる，(11) 指定集合で吸収させ過渡核をとる，(12) 過渡核のGreen作用素をとる，(13) 到達時刻の高次モーメント連立系を作る，(14) モーメント次数方向の漸化式を抽出する，(15) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DoobTransform → ProductChain → StateLumping → DoobTransform → StateLumping → LazyPerturbation → ProductChain → TimeReversal → LazyPerturbation → TimeReversal → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### Cayleyグラフのスペクトル合成（CharacterLevelConnection・CayleyConstruction・ClosedWalkExtraction・WalkArithmeticInvariant）

- ID: `research.autonomous.cayley_spectral.d41e87f169`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `closed_walk_congruence`
- 難度仮説: `16`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0625`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限アーベル群と、その自己同型で不変な生成集合を初期データとする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 非自明指標の値が指定軌道に属する元を生成集合とする，(2) 対応する無向Cayleyグラフを作る，(3) 距離が指定範囲以内の頂点を結ぶグラフ冪をとる，(4) 距離2の頂点を結ぶグラフをとる，(5) 距離が指定範囲以内の頂点を結ぶグラフ冪をとる，(6) 距離2の頂点を結ぶグラフをとる，(7) ループを除いた補グラフをとる，(8) 組合せLaplacianを群環上に表す，(9) 指標表で同時対角化してスペクトルを得る，(10) スペクトルモーメント列を作る，(11) 閉歩道数と原始閉路数を抽出する，(12) 閉路数列の合同不変量を抽出する。最後に、閉路数列が指定合同周期を持つ場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CharacterLevelConnection → CayleyConstruction → GraphPower → DistanceTwoGraph → GraphPower → DistanceTwoGraph → GraphComplement → LaplacianOperator → CharacterDiagonalization → SpectralMoments → ClosedWalkExtraction → WalkArithmeticInvariant → WalkCongruenceQuery`

### 凸体関手の合成力学（SteinerSymmetrization・DifferenceBody・ProjectionBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.53bc1ab3a7`
- 状態: `unresolved_by_mathos`
- 射数: `16`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `19`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 主慣性軸方向にSteiner対称化する，(2) 差体をとる，(3) 交叉体をとる，(4) 射影体をとる，(5) 差体をとる，(6) 主慣性軸方向にSteiner対称化する，(7) 交叉体をとる，(8) 重心体をとる，(9) 原点に関する極体をとる，(10) 自身と極体のMinkowski和をとる，(11) 原点に関する極体をとる，(12) 自身と極体のMinkowski和をとる，(13) 重心体をとる，(14) 射影体をとる，(15) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `SteinerSymmetrization → DifferenceBody → IntersectionBody → ProjectionBody → DifferenceBody → SteinerSymmetrization → IntersectionBody → CentroidBody → PolarDual → MinkowskiPolarSum → PolarDual → MinkowskiPolarSum → CentroidBody → ProjectionBody → VolumeNormalization → ConvexFixedPointQuery`

### 三角形変換の合成力学（IncenterMark・PedalProjection・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.4dccb9da48`
- 状態: `unresolved_by_mathos`
- 射数: `16`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `20`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 内心を標識点として付加する，(2) 標識点から三辺への垂足三点をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 類似重心を標識点として付加する，(5) 標識点を三辺に関して反射した三点をとる，(6) 三点を頂点とする向き付き三角形を作る，(7) 三辺の中点三角形へ移す，(8) 垂足三角形へ移す，(9) 三辺の中点三角形へ移す，(10) 垂足三角形へ移す，(11) 重心・面積・向きを固定して相似正規化する，(12) 相似類のモジュライ点へ射影する，(13) ここまでの合成が誘導する写像を反復する，(14) 退化三角形を境界として軌道をコンパクト化する，(15) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IncenterMark → PedalProjection → TriangleFormation → SymmedianMark → SideReflectionTrace → TriangleFormation → MedialTransform → OrthicTransform → MedialTransform → OrthicTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 平面代数曲線の合成変換（PolarReciprocal・IsogonalCremona・ResolveSingularities・CurveInvariantExtraction）

- ID: `research.autonomous.plane_curve.cbc0472fad`
- 状態: `unresolved_by_mathos`
- 射数: `16`
- 問い: `singularity_classification`
- 難度仮説: `19`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定非退化二次形式に関する極逆像をとる，(2) 固定基準三角形に関する等角共役Cremona像をとる，(3) 原点中心の円反転像をとる，(4) 固定非退化二次形式に関する極逆像をとる，(5) 固定光源からの反射光線族の包絡線をとる，(6) 固定基準三角形に関する等角共役Cremona像をとる，(7) 法線方向の代数的平行曲線をとる，(8) 射影閉包をとり無限遠点を加える，(9) 基点を避ける一般アフィンチャートへ移す，(10) 固定光源からの反射光線族の包絡線をとる，(11) 法線方向の代数的平行曲線をとる，(12) 正則接線族の射影双対曲線をとる，(13) 射影閉包をとり無限遠点を加える，(14) 全特異点を解消して正規化曲線を得る，(15) 次数、分岐、種数、自己交点データを抽出する。最後に、全特異点型と実枝数を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `PolarReciprocal → IsogonalCremona → CircleInversion → PolarReciprocal → Catacaustic → IsogonalCremona → OffsetCurve → ProjectiveClosure → AffineChartChange → Catacaustic → OffsetCurve → ProjectiveDual → ProjectiveClosure → ResolveSingularities → CurveInvariantExtraction → SingularityQuery`

### 多項式変換と算術観測（ReciprocalPolynomial・CriticalValuePolynomial・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.486aba9276`
- 状態: `unresolved_by_mathos`
- 射数: `16`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `20`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を逆数へ移す相反多項式をとる，(2) 臨界値を根にもつ消去多項式を作る，(3) 導関数をモニックに再正規化する，(4) 根を二乗するGraeffe変換を施す，(5) 根の重心を0へ移す平行移動共役を施す，(6) 重複度付き根配置へ移す，(7) 根配置からモニック多項式を再構成する，(8) 根の重心を0へ移す平行移動共役を施す，(9) 臨界値を根にもつ消去多項式を作る，(10) 重複度付き根配置へ移す，(11) 根の冪和モーメント列を作る，(12) モーメントからHankel行列族を作る，(13) 主小行列式列をとる，(14) 満たす最小線形漸化式を抽出する，(15) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ReciprocalPolynomial → CriticalValuePolynomial → DerivativeRenormalization → GraeffeTransform → ShiftConjugacy → RootMultiset → PolynomialReconstruction → ShiftConjugacy → CriticalValuePolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### Markov関手と到達時刻不変量（DoobTransform・ProductChain・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.dafc206234`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `16`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 正の固有関数によるDoob変換を施す，(2) 自身との同期積連鎖を作る，(3) 正の固有関数によるDoob変換を施す，(4) 自身との同期積連鎖を作る，(5) 定常分布に関する時間反転をとる，(6) 恒等遷移との凸結合でlazy化する，(7) 自己同型軌道に沿って強 lumping する，(8) 指定集合で吸収させ過渡核をとる，(9) 過渡核のGreen作用素をとる，(10) 到達時刻の高次モーメント連立系を作る，(11) モーメント次数方向の漸化式を抽出する，(12) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DoobTransform → ProductChain → DoobTransform → ProductChain → TimeReversal → LazyPerturbation → StateLumping → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### Cayleyグラフのスペクトル合成（AutomorphismOrbitConnection・CayleyConstruction・ClosedWalkExtraction・WalkArithmeticInvariant）

- ID: `research.autonomous.cayley_spectral.2b7dcfded2`
- 状態: `unresolved_by_mathos`
- 射数: `14`
- 問い: `closed_walk_congruence`
- 難度仮説: `17`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0469`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限アーベル群と、その自己同型で不変な生成集合を初期データとする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自己同型群の複数軌道の和を生成集合とする，(2) 対応する無向Cayleyグラフを作る，(3) ループを除いた補グラフをとる，(4) 距離2の頂点を結ぶグラフをとる，(5) 距離が指定範囲以内の頂点を結ぶグラフ冪をとる，(6) 距離2の頂点を結ぶグラフをとる，(7) ループを除いた補グラフをとる，(8) 距離が指定範囲以内の頂点を結ぶグラフ冪をとる，(9) 隣接作用素を群環上に表す，(10) 指標表で同時対角化してスペクトルを得る，(11) スペクトルモーメント列を作る，(12) 閉歩道数と原始閉路数を抽出する，(13) 閉路数列の合同不変量を抽出する。最後に、閉路数列が指定合同周期を持つ場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `AutomorphismOrbitConnection → CayleyConstruction → GraphComplement → DistanceTwoGraph → GraphPower → DistanceTwoGraph → GraphComplement → GraphPower → AdjacencyOperator → CharacterDiagonalization → SpectralMoments → ClosedWalkExtraction → WalkArithmeticInvariant → WalkCongruenceQuery`

### 凸体関手の合成力学（PolarDual・CentroidBody・ProjectionBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.6d89657e27`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `16`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 原点に関する極体をとる，(2) 重心体をとる，(3) 射影体をとる，(4) 自身と極体のMinkowski和をとる，(5) 重心体をとる，(6) 自身と極体のMinkowski和をとる，(7) 原点に関する極体をとる，(8) 交叉体をとる，(9) 主慣性軸方向にSteiner対称化する，(10) 差体をとる，(11) 射影体をとる，(12) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `PolarDual → CentroidBody → ProjectionBody → MinkowskiPolarSum → CentroidBody → MinkowskiPolarSum → PolarDual → IntersectionBody → SteinerSymmetrization → DifferenceBody → ProjectionBody → VolumeNormalization → ConvexFixedPointQuery`

### 三角形変換の合成力学（AnticomplementaryTransform・OrthicTransform・SimilarityNormalization・ModuliProjection）

- ID: `research.autonomous.triangle_dynamics.a5782f30c4`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `triangle_transform_fixed_points`
- 難度仮説: `15`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 反中点三角形へ移す，(2) 垂足三角形へ移す，(3) 類似重心を標識点として付加する，(4) 標識点を三辺に関して反射した三点をとる，(5) 三点を頂点とする向き付き三角形を作る，(6) 垂足三角形へ移す，(7) 類似重心を標識点として付加する，(8) 標識点を三辺に関して反射した三点をとる，(9) 三点を頂点とする向き付き三角形を作る，(10) 反中点三角形へ移す，(11) 重心・面積・向きを固定して相似正規化する，(12) 相似類のモジュライ点へ射影する。最後に、誘導写像の固定点と有限周期点を相似を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `AnticomplementaryTransform → OrthicTransform → SymmedianMark → SideReflectionTrace → TriangleFormation → OrthicTransform → SymmedianMark → SideReflectionTrace → TriangleFormation → AnticomplementaryTransform → SimilarityNormalization → ModuliProjection → TriangleFixedPointQuery`

### Markov関手と到達時刻不変量（StateLumping・LazyPerturbation・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.d2c0ffe562`
- 状態: `unresolved_by_mathos`
- 射数: `15`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `18`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自己同型軌道に沿って強 lumping する，(2) 恒等遷移との凸結合でlazy化する，(3) 正の固有関数によるDoob変換を施す，(4) 恒等遷移との凸結合でlazy化する，(5) 自己同型軌道に沿って強 lumping する，(6) 自身との同期積連鎖を作る，(7) 定常分布に関する時間反転をとる，(8) 自身との同期積連鎖を作る，(9) 正の固有関数によるDoob変換を施す，(10) 定常分布に関する時間反転をとる，(11) 指定集合で吸収させ過渡核をとる，(12) 過渡核のGreen作用素をとる，(13) 到達時刻の高次モーメント連立系を作る，(14) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `StateLumping → LazyPerturbation → DoobTransform → LazyPerturbation → StateLumping → ProductChain → TimeReversal → ProductChain → DoobTransform → TimeReversal → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 平面代数曲線の合成変換（IsogonalCremona・HessianCurve・ProjectiveDual・PolarReciprocal）

- ID: `research.autonomous.plane_curve.158541dc87`
- 状態: `unresolved_by_mathos`
- 射数: `14`
- 問い: `birational_periodicity`
- 難度仮説: `17`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定基準三角形に関する等角共役Cremona像をとる，(2) 定義多項式のHessian曲線をとる，(3) 射影閉包をとり無限遠点を加える，(4) 基点を避ける一般アフィンチャートへ移す，(5) 固定基準三角形に関する等角共役Cremona像をとる，(6) 法線方向の代数的平行曲線をとる，(7) 正則接線族の射影双対曲線をとる，(8) 射影閉包をとり無限遠点を加える，(9) 基点を避ける一般アフィンチャートへ移す，(10) 法線族の包絡線である発展曲線をとる，(11) 固定非退化二次形式に関する極逆像をとる，(12) 正則接線族の射影双対曲線をとる，(13) 固定非退化二次形式に関する極逆像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IsogonalCremona → HessianCurve → ProjectiveClosure → AffineChartChange → IsogonalCremona → OffsetCurve → ProjectiveDual → ProjectiveClosure → AffineChartChange → Evolute → PolarReciprocal → ProjectiveDual → PolarReciprocal → BirationalPeriodQuery`

### 多項式変換と算術観測（ShiftConjugacy・RootMultiset・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.c86fb8c9d0`
- 状態: `unresolved_by_mathos`
- 射数: `16`
- 問い: `recurrence_order_drop`
- 難度仮説: `20`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根の重心を0へ移す平行移動共役を施す，(2) 重複度付き根配置へ移す，(3) 根配置からモニック多項式を再構成する，(4) 導関数をモニックに再正規化する，(5) 根を逆数へ移す相反多項式をとる，(6) 根を二乗するGraeffe変換を施す，(7) 導関数をモニックに再正規化する，(8) 根を逆数へ移す相反多項式をとる，(9) 臨界値を根にもつ消去多項式を作る，(10) 根の重心を0へ移す平行移動共役を施す，(11) 重複度付き根配置へ移す，(12) 根の冪和モーメント列を作る，(13) モーメントからHankel行列族を作る，(14) 主小行列式列をとる，(15) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ShiftConjugacy → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → ReciprocalPolynomial → GraeffeTransform → DerivativeRenormalization → ReciprocalPolynomial → CriticalValuePolynomial → ShiftConjugacy → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### Cayleyグラフのスペクトル合成（CharacterLevelConnection・CayleyConstruction・ClosedWalkExtraction・WalkArithmeticInvariant）

- ID: `research.autonomous.cayley_spectral.7b788f9960`
- 状態: `unresolved_by_mathos`
- 射数: `13`
- 問い: `closed_walk_congruence`
- 難度仮説: `16`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0625`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限アーベル群と、その自己同型で不変な生成集合を初期データとする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 非自明指標の値が指定軌道に属する元を生成集合とする，(2) 対応する無向Cayleyグラフを作る，(3) 距離2の頂点を結ぶグラフをとる，(4) 距離が指定範囲以内の頂点を結ぶグラフ冪をとる，(5) ループを除いた補グラフをとる，(6) 距離が指定範囲以内の頂点を結ぶグラフ冪をとる，(7) ループを除いた補グラフをとる，(8) 組合せLaplacianを群環上に表す，(9) 指標表で同時対角化してスペクトルを得る，(10) スペクトルモーメント列を作る，(11) 閉歩道数と原始閉路数を抽出する，(12) 閉路数列の合同不変量を抽出する。最後に、閉路数列が指定合同周期を持つ場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CharacterLevelConnection → CayleyConstruction → DistanceTwoGraph → GraphPower → GraphComplement → GraphPower → GraphComplement → LaplacianOperator → CharacterDiagonalization → SpectralMoments → ClosedWalkExtraction → WalkArithmeticInvariant → WalkCongruenceQuery`

### 多項式変換と算術観測（DerivativeRenormalization・ReciprocalPolynomial・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.041abfc52e`
- 状態: `unresolved_by_mathos`
- 射数: `16`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `20`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 導関数をモニックに再正規化する，(2) 根を逆数へ移す相反多項式をとる，(3) 根の重心を0へ移す平行移動共役を施す，(4) 根を逆数へ移す相反多項式をとる，(5) 臨界値を根にもつ消去多項式を作る，(6) 根を二乗するGraeffe変換を施す，(7) 根の重心を0へ移す平行移動共役を施す，(8) 重複度付き根配置へ移す，(9) 根配置からモニック多項式を再構成する，(10) 重複度付き根配置へ移す，(11) 根の冪和モーメント列を作る，(12) モーメントからHankel行列族を作る，(13) 主小行列式列をとる，(14) 満たす最小線形漸化式を抽出する，(15) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DerivativeRenormalization → ReciprocalPolynomial → ShiftConjugacy → ReciprocalPolynomial → CriticalValuePolynomial → GraeffeTransform → ShiftConjugacy → RootMultiset → PolynomialReconstruction → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### Markov関手と到達時刻不変量（StateLumping・ProductChain・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.8d30d2b2f9`
- 状態: `unresolved_by_mathos`
- 射数: `16`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `19`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自己同型軌道に沿って強 lumping する，(2) 自身との同期積連鎖を作る，(3) 自己同型軌道に沿って強 lumping する，(4) 自身との同期積連鎖を作る，(5) 恒等遷移との凸結合でlazy化する，(6) 正の固有関数によるDoob変換を施す，(7) 定常分布に関する時間反転をとる，(8) 正の固有関数によるDoob変換を施す，(9) 恒等遷移との凸結合でlazy化する，(10) 定常分布に関する時間反転をとる，(11) 指定集合で吸収させ過渡核をとる，(12) 過渡核のGreen作用素をとる，(13) 到達時刻の高次モーメント連立系を作る，(14) モーメント次数方向の漸化式を抽出する，(15) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `StateLumping → ProductChain → StateLumping → ProductChain → LazyPerturbation → DoobTransform → TimeReversal → DoobTransform → LazyPerturbation → TimeReversal → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 三角形変換の合成力学（MedialTransform・ExcentralTransform・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.b9ff873c65`
- 状態: `unresolved_by_mathos`
- 射数: `14`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `18`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0625`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 三辺の中点三角形へ移す，(2) 傍心三角形へ移す，(3) 垂心を標識点として付加する，(4) 標識点から三辺への垂足三点をとる，(5) 三点を頂点とする向き付き三角形を作る，(6) 内心を標識点として付加する，(7) 標識点を三辺に関して反射した三点をとる，(8) 三点を頂点とする向き付き三角形を作る，(9) 重心・面積・向きを固定して相似正規化する，(10) 相似類のモジュライ点へ射影する，(11) ここまでの合成が誘導する写像を反復する，(12) 退化三角形を境界として軌道をコンパクト化する，(13) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `MedialTransform → ExcentralTransform → OrthocenterMark → PedalProjection → TriangleFormation → IncenterMark → SideReflectionTrace → TriangleFormation → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 平面代数曲線の合成変換（Catacaustic・Evolute・ProjectiveDual・CircleInversion）

- ID: `research.autonomous.plane_curve.acf85f8784`
- 状態: `unresolved_by_mathos`
- 射数: `14`
- 問い: `birational_periodicity`
- 難度仮説: `16`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定光源からの反射光線族の包絡線をとる，(2) 法線族の包絡線である発展曲線をとる，(3) 法線方向の代数的平行曲線をとる，(4) 固定光源からの反射光線族の包絡線をとる，(5) 固定基準三角形に関する等角共役Cremona像をとる，(6) 法線方向の代数的平行曲線をとる，(7) 正則接線族の射影双対曲線をとる，(8) 法線族の包絡線である発展曲線をとる，(9) 原点中心の円反転像をとる，(10) 固定非退化二次形式に関する極逆像をとる，(11) 固定基準三角形に関する等角共役Cremona像をとる，(12) 正則接線族の射影双対曲線をとる，(13) 原点中心の円反転像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `Catacaustic → Evolute → OffsetCurve → Catacaustic → IsogonalCremona → OffsetCurve → ProjectiveDual → Evolute → CircleInversion → PolarReciprocal → IsogonalCremona → ProjectiveDual → CircleInversion → BirationalPeriodQuery`

### 凸体関手の合成力学（ProjectionBody・CentroidBody・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.aaf9e6b7b2`
- 状態: `unresolved_by_mathos`
- 射数: `14`
- 問い: `convex_body_dynamics`
- 難度仮説: `18`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0625`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 射影体をとる，(2) 重心体をとる，(3) 交叉体をとる，(4) 差体をとる，(5) 主慣性軸方向にSteiner対称化する，(6) 原点に関する極体をとる，(7) 差体をとる，(8) 重心体をとる，(9) 自身と極体のMinkowski和をとる，(10) 面積と二次モーメントを固定して正規化する，(11) ここまでの凸体関手を反復する，(12) 支持関数の軌道へ移す，(13) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectionBody → CentroidBody → IntersectionBody → DifferenceBody → SteinerSymmetrization → PolarDual → DifferenceBody → CentroidBody → MinkowskiPolarSum → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### Cayleyグラフのスペクトル合成（PowerResidueConnection・CayleyConstruction・ClosedWalkExtraction・WalkArithmeticInvariant）

- ID: `research.autonomous.cayley_spectral.fe53bf60ae`
- 状態: `unresolved_by_mathos`
- 射数: `14`
- 問い: `closed_walk_congruence`
- 難度仮説: `17`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限アーベル群と、その自己同型で不変な生成集合を初期データとする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 冪剰余類の自己同型軌道を生成集合とする，(2) 対応する無向Cayleyグラフを作る，(3) 距離が指定範囲以内の頂点を結ぶグラフ冪をとる，(4) 距離2の頂点を結ぶグラフをとる，(5) 距離が指定範囲以内の頂点を結ぶグラフ冪をとる，(6) ループを除いた補グラフをとる，(7) 距離2の頂点を結ぶグラフをとる，(8) ループを除いた補グラフをとる，(9) 組合せLaplacianを群環上に表す，(10) 指標表で同時対角化してスペクトルを得る，(11) スペクトルモーメント列を作る，(12) 閉歩道数と原始閉路数を抽出する，(13) 閉路数列の合同不変量を抽出する。最後に、閉路数列が指定合同周期を持つ場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `PowerResidueConnection → CayleyConstruction → GraphPower → DistanceTwoGraph → GraphPower → GraphComplement → DistanceTwoGraph → GraphComplement → LaplacianOperator → CharacterDiagonalization → SpectralMoments → ClosedWalkExtraction → WalkArithmeticInvariant → WalkCongruenceQuery`

### 平面代数曲線の合成変換（Catacaustic・OffsetCurve・ProjectiveDual・IsogonalCremona）

- ID: `research.autonomous.plane_curve.426371ae3a`
- 状態: `unresolved_by_mathos`
- 射数: `16`
- 問い: `birational_periodicity`
- 難度仮説: `19`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定光源からの反射光線族の包絡線をとる，(2) 法線方向の代数的平行曲線をとる，(3) 原点中心の円反転像をとる，(4) 固定光源からの反射光線族の包絡線をとる，(5) 固定基準三角形に関する等角共役Cremona像をとる，(6) 固定非退化二次形式に関する極逆像をとる，(7) 法線族の包絡線である発展曲線をとる，(8) 法線方向の代数的平行曲線をとる，(9) 原点中心の円反転像をとる，(10) 法線族の包絡線である発展曲線をとる，(11) 射影閉包をとり無限遠点を加える，(12) 基点を避ける一般アフィンチャートへ移す，(13) 定義多項式のHessian曲線をとる，(14) 正則接線族の射影双対曲線をとる，(15) 固定基準三角形に関する等角共役Cremona像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `Catacaustic → OffsetCurve → CircleInversion → Catacaustic → IsogonalCremona → PolarReciprocal → Evolute → OffsetCurve → CircleInversion → Evolute → ProjectiveClosure → AffineChartChange → HessianCurve → ProjectiveDual → IsogonalCremona → BirationalPeriodQuery`

### Markov関手と到達時刻不変量（LazyPerturbation・DoobTransform・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.5df568a188`
- 状態: `unresolved_by_mathos`
- 射数: `14`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `17`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 恒等遷移との凸結合でlazy化する，(2) 正の固有関数によるDoob変換を施す，(3) 自身との同期積連鎖を作る，(4) 恒等遷移との凸結合でlazy化する，(5) 自身との同期積連鎖を作る，(6) 自己同型軌道に沿って強 lumping する，(7) 定常分布に関する時間反転をとる，(8) 自己同型軌道に沿って強 lumping する，(9) 正の固有関数によるDoob変換を施す，(10) 指定集合で吸収させ過渡核をとる，(11) 過渡核のGreen作用素をとる，(12) 到達時刻の高次モーメント連立系を作る，(13) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `LazyPerturbation → DoobTransform → ProductChain → LazyPerturbation → ProductChain → StateLumping → TimeReversal → StateLumping → DoobTransform → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 凸体関手の合成力学（ProjectionBody・SteinerSymmetrization・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.5a3684d716`
- 状態: `unresolved_by_mathos`
- 射数: `16`
- 問い: `convex_body_dynamics`
- 難度仮説: `20`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 射影体をとる，(2) 主慣性軸方向にSteiner対称化する，(3) 差体をとる，(4) 重心体をとる，(5) 自身と極体のMinkowski和をとる，(6) 主慣性軸方向にSteiner対称化する，(7) 射影体をとる，(8) 交叉体をとる，(9) 自身と極体のMinkowski和をとる，(10) 原点に関する極体をとる，(11) 差体をとる，(12) 面積と二次モーメントを固定して正規化する，(13) ここまでの凸体関手を反復する，(14) 支持関数の軌道へ移す，(15) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectionBody → SteinerSymmetrization → DifferenceBody → CentroidBody → MinkowskiPolarSum → SteinerSymmetrization → ProjectionBody → IntersectionBody → MinkowskiPolarSum → PolarDual → DifferenceBody → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 多項式変換と算術観測（DerivativeRenormalization・GraeffeTransform・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.297ab4f2fb`
- 状態: `unresolved_by_mathos`
- 射数: `17`
- 問い: `recurrence_order_drop`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 導関数をモニックに再正規化する，(2) 根を二乗するGraeffe変換を施す，(3) 導関数をモニックに再正規化する，(4) 根の重心を0へ移す平行移動共役を施す，(5) 根を二乗するGraeffe変換を施す，(6) 臨界値を根にもつ消去多項式を作る，(7) 根を逆数へ移す相反多項式をとる，(8) 根の重心を0へ移す平行移動共役を施す，(9) 根を逆数へ移す相反多項式をとる，(10) 重複度付き根配置へ移す，(11) 根配置からモニック多項式を再構成する，(12) 重複度付き根配置へ移す，(13) 根の冪和モーメント列を作る，(14) モーメントからHankel行列族を作る，(15) 主小行列式列をとる，(16) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DerivativeRenormalization → GraeffeTransform → DerivativeRenormalization → ShiftConjugacy → GraeffeTransform → CriticalValuePolynomial → ReciprocalPolynomial → ShiftConjugacy → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 三角形変換の合成力学（ExcentralTransform・MedialTransform・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.15ef9d8478`
- 状態: `unresolved_by_mathos`
- 射数: `16`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `20`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 傍心三角形へ移す，(2) 三辺の中点三角形へ移す，(3) 類似重心を標識点として付加する，(4) 標識点を通る三本のcevianの辺上の足をとる，(5) 三点を頂点とする向き付き三角形を作る，(6) 傍心三角形へ移す，(7) 類似重心を標識点として付加する，(8) 標識点から三辺への垂足三点をとる，(9) 三点を頂点とする向き付き三角形を作る，(10) 反中点三角形へ移す，(11) 重心・面積・向きを固定して相似正規化する，(12) 相似類のモジュライ点へ射影する，(13) ここまでの合成が誘導する写像を反復する，(14) 退化三角形を境界として軌道をコンパクト化する，(15) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ExcentralTransform → MedialTransform → SymmedianMark → CevianTrace → TriangleFormation → ExcentralTransform → SymmedianMark → PedalProjection → TriangleFormation → AnticomplementaryTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### Cayleyグラフのスペクトル合成（CharacterLevelConnection・CayleyConstruction・ClosedWalkExtraction・WalkArithmeticInvariant）

- ID: `research.autonomous.cayley_spectral.9ae6fcebc6`
- 状態: `unresolved_by_mathos`
- 射数: `14`
- 問い: `closed_walk_congruence`
- 難度仮説: `17`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0625`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限アーベル群と、その自己同型で不変な生成集合を初期データとする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 非自明指標の値が指定軌道に属する元を生成集合とする，(2) 対応する無向Cayleyグラフを作る，(3) 距離が指定範囲以内の頂点を結ぶグラフ冪をとる，(4) ループを除いた補グラフをとる，(5) 距離が指定範囲以内の頂点を結ぶグラフ冪をとる，(6) 距離2の頂点を結ぶグラフをとる，(7) ループを除いた補グラフをとる，(8) 距離2の頂点を結ぶグラフをとる，(9) 組合せLaplacianを群環上に表す，(10) 指標表で同時対角化してスペクトルを得る，(11) スペクトルモーメント列を作る，(12) 閉歩道数と原始閉路数を抽出する，(13) 閉路数列の合同不変量を抽出する。最後に、閉路数列が指定合同周期を持つ場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CharacterLevelConnection → CayleyConstruction → GraphPower → GraphComplement → GraphPower → DistanceTwoGraph → GraphComplement → DistanceTwoGraph → LaplacianOperator → CharacterDiagonalization → SpectralMoments → ClosedWalkExtraction → WalkArithmeticInvariant → WalkCongruenceQuery`

### 凸体関手の合成力学（IntersectionBody・DifferenceBody・MinkowskiPolarSum・VolumeNormalization）

- ID: `research.autonomous.convex_body.61462bca92`
- 状態: `unresolved_by_mathos`
- 射数: `15`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `18`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 交叉体をとる，(2) 差体をとる，(3) 主慣性軸方向にSteiner対称化する，(4) 差体をとる，(5) 重心体をとる，(6) 主慣性軸方向にSteiner対称化する，(7) 射影体をとる，(8) 交叉体をとる，(9) 射影体をとる，(10) 原点に関する極体をとる，(11) 重心体をとる，(12) 原点に関する極体をとる，(13) 自身と極体のMinkowski和をとる，(14) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IntersectionBody → DifferenceBody → SteinerSymmetrization → DifferenceBody → CentroidBody → SteinerSymmetrization → ProjectionBody → IntersectionBody → ProjectionBody → PolarDual → CentroidBody → PolarDual → MinkowskiPolarSum → VolumeNormalization → ConvexFixedPointQuery`

### 多項式変換と算術観測（ReciprocalPolynomial・DerivativeRenormalization・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.78fa12675c`
- 状態: `unresolved_by_mathos`
- 射数: `15`
- 問い: `recurrence_order_drop`
- 難度仮説: `19`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を逆数へ移す相反多項式をとる，(2) 導関数をモニックに再正規化する，(3) 根の重心を0へ移す平行移動共役を施す，(4) 臨界値を根にもつ消去多項式を作る，(5) 重複度付き根配置へ移す，(6) 根配置からモニック多項式を再構成する，(7) 根を二乗するGraeffe変換を施す，(8) 根を逆数へ移す相反多項式をとる，(9) 根の重心を0へ移す平行移動共役を施す，(10) 重複度付き根配置へ移す，(11) 根の冪和モーメント列を作る，(12) モーメントからHankel行列族を作る，(13) 主小行列式列をとる，(14) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ReciprocalPolynomial → DerivativeRenormalization → ShiftConjugacy → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → GraeffeTransform → ReciprocalPolynomial → ShiftConjugacy → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 三角形変換の合成力学（OrthicTransform・SymmedianMark・SimilarityNormalization・ModuliProjection）

- ID: `research.autonomous.triangle_dynamics.c72f98f3b3`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `triangle_transform_fixed_points`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 垂足三角形へ移す，(2) 類似重心を標識点として付加する，(3) 各頂点と標識点が定める円の対応交点をとる，(4) 三点を頂点とする向き付き三角形を作る，(5) 類似重心を標識点として付加する，(6) 各頂点と標識点が定める円の対応交点をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 内心を標識点として付加する，(9) 標識点を通る三本のcevianの辺上の足をとる，(10) 三点を頂点とする向き付き三角形を作る，(11) 反中点三角形へ移す，(12) 傍心三角形へ移す，(13) 三辺の中点三角形へ移す，(14) 垂足三角形へ移す，(15) 三辺の中点三角形へ移す，(16) 重心・面積・向きを固定して相似正規化する，(17) 相似類のモジュライ点へ射影する。最後に、誘導写像の固定点と有限周期点を相似を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `OrthicTransform → SymmedianMark → VertexCircleTrace → TriangleFormation → SymmedianMark → VertexCircleTrace → TriangleFormation → IncenterMark → CevianTrace → TriangleFormation → AnticomplementaryTransform → ExcentralTransform → MedialTransform → OrthicTransform → MedialTransform → SimilarityNormalization → ModuliProjection → TriangleFixedPointQuery`

### Markov関手と到達時刻不変量（ProductChain・StateLumping・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.1d4baa069a`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身との同期積連鎖を作る，(2) 自己同型軌道に沿って強 lumping する，(3) 定常分布に関する時間反転をとる，(4) 自己同型軌道に沿って強 lumping する，(5) 正の固有関数によるDoob変換を施す，(6) 恒等遷移との凸結合でlazy化する，(7) 自身との同期積連鎖を作る，(8) 恒等遷移との凸結合でlazy化する，(9) 自己同型軌道に沿って強 lumping する，(10) 定常分布に関する時間反転をとる，(11) 正の固有関数によるDoob変換を施す，(12) 自身との同期積連鎖を作る，(13) 指定集合で吸収させ過渡核をとる，(14) 過渡核のGreen作用素をとる，(15) 到達時刻の高次モーメント連立系を作る，(16) モーメント次数方向の漸化式を抽出する，(17) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProductChain → StateLumping → TimeReversal → StateLumping → DoobTransform → LazyPerturbation → ProductChain → LazyPerturbation → StateLumping → TimeReversal → DoobTransform → ProductChain → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 平面代数曲線の合成変換（CircleInversion・HessianCurve・OffsetCurve・IsogonalCremona）

- ID: `research.autonomous.plane_curve.fc70e0f45a`
- 状態: `unresolved_by_mathos`
- 射数: `15`
- 問い: `birational_periodicity`
- 難度仮説: `17`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 原点中心の円反転像をとる，(2) 定義多項式のHessian曲線をとる，(3) 法線族の包絡線である発展曲線をとる，(4) 定義多項式のHessian曲線をとる，(5) 正則接線族の射影双対曲線をとる，(6) 原点中心の円反転像をとる，(7) 固定基準三角形に関する等角共役Cremona像をとる，(8) 法線族の包絡線である発展曲線をとる，(9) 固定非退化二次形式に関する極逆像をとる，(10) 法線方向の代数的平行曲線をとる，(11) 固定非退化二次形式に関する極逆像をとる，(12) 正則接線族の射影双対曲線をとる，(13) 法線方向の代数的平行曲線をとる，(14) 固定基準三角形に関する等角共役Cremona像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CircleInversion → HessianCurve → Evolute → HessianCurve → ProjectiveDual → CircleInversion → IsogonalCremona → Evolute → PolarReciprocal → OffsetCurve → PolarReciprocal → ProjectiveDual → OffsetCurve → IsogonalCremona → BirationalPeriodQuery`

### 平面代数曲線の合成変換（Catacaustic・CircleInversion・CircleInversion・PolarReciprocal）

- ID: `research.autonomous.plane_curve.005ed3c685`
- 状態: `unresolved_by_mathos`
- 射数: `15`
- 問い: `birational_periodicity`
- 難度仮説: `18`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定光源からの反射光線族の包絡線をとる，(2) 原点中心の円反転像をとる，(3) 固定基準三角形に関する等角共役Cremona像をとる，(4) 固定光源からの反射光線族の包絡線をとる，(5) 法線族の包絡線である発展曲線をとる，(6) 射影閉包をとり無限遠点を加える，(7) 基点を避ける一般アフィンチャートへ移す，(8) 法線族の包絡線である発展曲線をとる，(9) 固定基準三角形に関する等角共役Cremona像をとる，(10) 正則接線族の射影双対曲線をとる，(11) 固定非退化二次形式に関する極逆像をとる，(12) 正則接線族の射影双対曲線をとる，(13) 原点中心の円反転像をとる，(14) 固定非退化二次形式に関する極逆像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `Catacaustic → CircleInversion → IsogonalCremona → Catacaustic → Evolute → ProjectiveClosure → AffineChartChange → Evolute → IsogonalCremona → ProjectiveDual → PolarReciprocal → ProjectiveDual → CircleInversion → PolarReciprocal → BirationalPeriodQuery`

### 多項式変換と算術観測（RootMultiset・PolynomialReconstruction・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.7fc9c5cded`
- 状態: `unresolved_by_mathos`
- 射数: `15`
- 問い: `recurrence_order_drop`
- 難度仮説: `19`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重複度付き根配置へ移す，(2) 根配置からモニック多項式を再構成する，(3) 根を二乗するGraeffe変換を施す，(4) 導関数をモニックに再正規化する，(5) 根を二乗するGraeffe変換を施す，(6) 根の重心を0へ移す平行移動共役を施す，(7) 導関数をモニックに再正規化する，(8) 根を逆数へ移す相反多項式をとる，(9) 臨界値を根にもつ消去多項式を作る，(10) 重複度付き根配置へ移す，(11) 根の冪和モーメント列を作る，(12) モーメントからHankel行列族を作る，(13) 主小行列式列をとる，(14) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `RootMultiset → PolynomialReconstruction → GraeffeTransform → DerivativeRenormalization → GraeffeTransform → ShiftConjugacy → DerivativeRenormalization → ReciprocalPolynomial → CriticalValuePolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 三角形変換の合成力学（OrthocenterMark・PedalProjection・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.381a15127d`
- 状態: `unresolved_by_mathos`
- 射数: `15`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `19`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 垂心を標識点として付加する，(2) 標識点から三辺への垂足三点をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 垂足三角形へ移す，(5) 外心を標識点として付加する，(6) 各頂点と標識点が定める円の対応交点をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 反中点三角形へ移す，(9) 傍心三角形へ移す，(10) 重心・面積・向きを固定して相似正規化する，(11) 相似類のモジュライ点へ射影する，(12) ここまでの合成が誘導する写像を反復する，(13) 退化三角形を境界として軌道をコンパクト化する，(14) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `OrthocenterMark → PedalProjection → TriangleFormation → OrthicTransform → CircumcenterMark → VertexCircleTrace → TriangleFormation → AnticomplementaryTransform → ExcentralTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 凸体関手の合成力学（PolarDual・MinkowskiPolarSum・CentroidBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.8b616431d0`
- 状態: `unresolved_by_mathos`
- 射数: `15`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `18`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 原点に関する極体をとる，(2) 自身と極体のMinkowski和をとる，(3) 主慣性軸方向にSteiner対称化する，(4) 差体をとる，(5) 交叉体をとる，(6) 射影体をとる，(7) 原点に関する極体をとる，(8) 差体をとる，(9) 交叉体をとる，(10) 自身と極体のMinkowski和をとる，(11) 重心体をとる，(12) 射影体をとる，(13) 重心体をとる，(14) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `PolarDual → MinkowskiPolarSum → SteinerSymmetrization → DifferenceBody → IntersectionBody → ProjectionBody → PolarDual → DifferenceBody → IntersectionBody → MinkowskiPolarSum → CentroidBody → ProjectionBody → CentroidBody → VolumeNormalization → ConvexFixedPointQuery`

### Markov関手と到達時刻不変量（LazyPerturbation・ProductChain・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.a20c96d809`
- 状態: `unresolved_by_mathos`
- 射数: `16`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `19`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 恒等遷移との凸結合でlazy化する，(2) 自身との同期積連鎖を作る，(3) 恒等遷移との凸結合でlazy化する，(4) 定常分布に関する時間反転をとる，(5) 正の固有関数によるDoob変換を施す，(6) 定常分布に関する時間反転をとる，(7) 自身との同期積連鎖を作る，(8) 自己同型軌道に沿って強 lumping する，(9) 正の固有関数によるDoob変換を施す，(10) 自己同型軌道に沿って強 lumping する，(11) 指定集合で吸収させ過渡核をとる，(12) 過渡核のGreen作用素をとる，(13) 到達時刻の高次モーメント連立系を作る，(14) モーメント次数方向の漸化式を抽出する，(15) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `LazyPerturbation → ProductChain → LazyPerturbation → TimeReversal → DoobTransform → TimeReversal → ProductChain → StateLumping → DoobTransform → StateLumping → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 多項式変換と算術観測（GraeffeTransform・DerivativeRenormalization・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.4e6bc8378e`
- 状態: `unresolved_by_mathos`
- 射数: `15`
- 問い: `recurrence_order_drop`
- 難度仮説: `18`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を二乗するGraeffe変換を施す，(2) 導関数をモニックに再正規化する，(3) 重複度付き根配置へ移す，(4) 根配置からモニック多項式を再構成する，(5) 導関数をモニックに再正規化する，(6) 根を逆数へ移す相反多項式をとる，(7) 根を二乗するGraeffe変換を施す，(8) 臨界値を根にもつ消去多項式を作る，(9) 根を逆数へ移す相反多項式をとる，(10) 重複度付き根配置へ移す，(11) 根の冪和モーメント列を作る，(12) モーメントからHankel行列族を作る，(13) 主小行列式列をとる，(14) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `GraeffeTransform → DerivativeRenormalization → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → ReciprocalPolynomial → GraeffeTransform → CriticalValuePolynomial → ReciprocalPolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 三角形変換の合成力学（CentroidMark・SideReflectionTrace・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.7209cdfa7c`
- 状態: `unresolved_by_mathos`
- 射数: `15`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `19`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重心を標識点として付加する，(2) 標識点を三辺に関して反射した三点をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 垂心を標識点として付加する，(5) 標識点を通る三本のcevianの辺上の足をとる，(6) 三点を頂点とする向き付き三角形を作る，(7) 垂足三角形へ移す，(8) 反中点三角形へ移す，(9) 傍心三角形へ移す，(10) 重心・面積・向きを固定して相似正規化する，(11) 相似類のモジュライ点へ射影する，(12) ここまでの合成が誘導する写像を反復する，(13) 退化三角形を境界として軌道をコンパクト化する，(14) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CentroidMark → SideReflectionTrace → TriangleFormation → OrthocenterMark → CevianTrace → TriangleFormation → OrthicTransform → AnticomplementaryTransform → ExcentralTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 平面代数曲線の合成変換（Catacaustic・Evolute・ProjectiveDual・IsogonalCremona）

- ID: `research.autonomous.plane_curve.27f6a4ef5f`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `birational_periodicity`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定光源からの反射光線族の包絡線をとる，(2) 法線族の包絡線である発展曲線をとる，(3) 定義多項式のHessian曲線をとる，(4) 固定光源からの反射光線族の包絡線をとる，(5) 射影閉包をとり無限遠点を加える，(6) 基点を避ける一般アフィンチャートへ移す，(7) 固定光源からの反射光線族の包絡線をとる，(8) 正則接線族の射影双対曲線をとる，(9) 固定非退化二次形式に関する極逆像をとる，(10) 法線族の包絡線である発展曲線をとる，(11) 固定非退化二次形式に関する極逆像をとる，(12) 法線族の包絡線である発展曲線をとる，(13) 固定基準三角形に関する等角共役Cremona像をとる，(14) 定義多項式のHessian曲線をとる，(15) 原点中心の円反転像をとる，(16) 正則接線族の射影双対曲線をとる，(17) 固定基準三角形に関する等角共役Cremona像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `Catacaustic → Evolute → HessianCurve → Catacaustic → ProjectiveClosure → AffineChartChange → Catacaustic → ProjectiveDual → PolarReciprocal → Evolute → PolarReciprocal → Evolute → IsogonalCremona → HessianCurve → CircleInversion → ProjectiveDual → IsogonalCremona → BirationalPeriodQuery`

### 凸体関手の合成力学（CentroidBody・MinkowskiPolarSum・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.440b87db04`
- 状態: `unresolved_by_mathos`
- 射数: `17`
- 問い: `convex_body_dynamics`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重心体をとる，(2) 自身と極体のMinkowski和をとる，(3) 原点に関する極体をとる，(4) 重心体をとる，(5) 主慣性軸方向にSteiner対称化する，(6) 射影体をとる，(7) 差体をとる，(8) 射影体をとる，(9) 原点に関する極体をとる，(10) 主慣性軸方向にSteiner対称化する，(11) 自身と極体のMinkowski和をとる，(12) 交叉体をとる，(13) 面積と二次モーメントを固定して正規化する，(14) ここまでの凸体関手を反復する，(15) 支持関数の軌道へ移す，(16) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CentroidBody → MinkowskiPolarSum → PolarDual → CentroidBody → SteinerSymmetrization → ProjectionBody → DifferenceBody → ProjectionBody → PolarDual → SteinerSymmetrization → MinkowskiPolarSum → IntersectionBody → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### Markov関手と到達時刻不変量（DoobTransform・LazyPerturbation・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.136d4a6fe5`
- 状態: `unresolved_by_mathos`
- 射数: `16`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `19`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 正の固有関数によるDoob変換を施す，(2) 恒等遷移との凸結合でlazy化する，(3) 自身との同期積連鎖を作る，(4) 定常分布に関する時間反転をとる，(5) 恒等遷移との凸結合でlazy化する，(6) 正の固有関数によるDoob変換を施す，(7) 定常分布に関する時間反転をとる，(8) 自己同型軌道に沿って強 lumping する，(9) 自身との同期積連鎖を作る，(10) 自己同型軌道に沿って強 lumping する，(11) 指定集合で吸収させ過渡核をとる，(12) 過渡核のGreen作用素をとる，(13) 到達時刻の高次モーメント連立系を作る，(14) モーメント次数方向の漸化式を抽出する，(15) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DoobTransform → LazyPerturbation → ProductChain → TimeReversal → LazyPerturbation → DoobTransform → TimeReversal → StateLumping → ProductChain → StateLumping → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 多項式変換と算術観測（ShiftConjugacy・DerivativeRenormalization・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.aacbe1e40e`
- 状態: `unresolved_by_mathos`
- 射数: `16`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `20`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根の重心を0へ移す平行移動共役を施す，(2) 導関数をモニックに再正規化する，(3) 根を二乗するGraeffe変換を施す，(4) 臨界値を根にもつ消去多項式を作る，(5) 根の重心を0へ移す平行移動共役を施す，(6) 臨界値を根にもつ消去多項式を作る，(7) 根を二乗するGraeffe変換を施す，(8) 導関数をモニックに再正規化する，(9) 根を逆数へ移す相反多項式をとる，(10) 重複度付き根配置へ移す，(11) 根の冪和モーメント列を作る，(12) モーメントからHankel行列族を作る，(13) 主小行列式列をとる，(14) 満たす最小線形漸化式を抽出する，(15) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ShiftConjugacy → DerivativeRenormalization → GraeffeTransform → CriticalValuePolynomial → ShiftConjugacy → CriticalValuePolynomial → GraeffeTransform → DerivativeRenormalization → ReciprocalPolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 凸体関手の合成力学（PolarDual・SteinerSymmetrization・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.fcd846ee52`
- 状態: `unresolved_by_mathos`
- 射数: `16`
- 問い: `convex_body_dynamics`
- 難度仮説: `19`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 原点に関する極体をとる，(2) 主慣性軸方向にSteiner対称化する，(3) 重心体をとる，(4) 交叉体をとる，(5) 自身と極体のMinkowski和をとる，(6) 射影体をとる，(7) 自身と極体のMinkowski和をとる，(8) 交叉体をとる，(9) 射影体をとる，(10) 重心体をとる，(11) 原点に関する極体をとる，(12) 面積と二次モーメントを固定して正規化する，(13) ここまでの凸体関手を反復する，(14) 支持関数の軌道へ移す，(15) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `PolarDual → SteinerSymmetrization → CentroidBody → IntersectionBody → MinkowskiPolarSum → ProjectionBody → MinkowskiPolarSum → IntersectionBody → ProjectionBody → CentroidBody → PolarDual → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 平面代数曲線の合成変換（Evolute・Catacaustic・AffineChartChange・ProjectiveDual）

- ID: `research.autonomous.plane_curve.693ce44a24`
- 状態: `unresolved_by_mathos`
- 射数: `15`
- 問い: `birational_periodicity`
- 難度仮説: `18`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 法線族の包絡線である発展曲線をとる，(2) 固定光源からの反射光線族の包絡線をとる，(3) 固定基準三角形に関する等角共役Cremona像をとる，(4) 原点中心の円反転像をとる，(5) 固定基準三角形に関する等角共役Cremona像をとる，(6) 定義多項式のHessian曲線をとる，(7) 固定非退化二次形式に関する極逆像をとる，(8) 固定光源からの反射光線族の包絡線をとる，(9) 原点中心の円反転像をとる，(10) 固定非退化二次形式に関する極逆像をとる，(11) 法線方向の代数的平行曲線をとる，(12) 射影閉包をとり無限遠点を加える，(13) 基点を避ける一般アフィンチャートへ移す，(14) 正則接線族の射影双対曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `Evolute → Catacaustic → IsogonalCremona → CircleInversion → IsogonalCremona → HessianCurve → PolarReciprocal → Catacaustic → CircleInversion → PolarReciprocal → OffsetCurve → ProjectiveClosure → AffineChartChange → ProjectiveDual → BirationalPeriodQuery`

### Markov関手と到達時刻不変量（TimeReversal・LazyPerturbation・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.d143a0a3bb`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 定常分布に関する時間反転をとる，(2) 恒等遷移との凸結合でlazy化する，(3) 自身との同期積連鎖を作る，(4) 定常分布に関する時間反転をとる，(5) 正の固有関数によるDoob変換を施す，(6) 定常分布に関する時間反転をとる，(7) 自己同型軌道に沿って強 lumping する，(8) 自身との同期積連鎖を作る，(9) 恒等遷移との凸結合でlazy化する，(10) 自身との同期積連鎖を作る，(11) 正の固有関数によるDoob変換を施す，(12) 自己同型軌道に沿って強 lumping する，(13) 恒等遷移との凸結合でlazy化する，(14) 指定集合で吸収させ過渡核をとる，(15) 過渡核のGreen作用素をとる，(16) 到達時刻の高次モーメント連立系を作る，(17) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `TimeReversal → LazyPerturbation → ProductChain → TimeReversal → DoobTransform → TimeReversal → StateLumping → ProductChain → LazyPerturbation → ProductChain → DoobTransform → StateLumping → LazyPerturbation → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 三角形変換の合成力学（ExcentralTransform・OrthocenterMark・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.67d4a4e6e9`
- 状態: `unresolved_by_mathos`
- 射数: `16`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `20`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 傍心三角形へ移す，(2) 垂心を標識点として付加する，(3) 標識点を三辺に関して反射した三点をとる，(4) 三点を頂点とする向き付き三角形を作る，(5) 重心を標識点として付加する，(6) 各頂点と標識点が定める円の対応交点をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 反中点三角形へ移す，(9) 傍心三角形へ移す，(10) 反中点三角形へ移す，(11) 重心・面積・向きを固定して相似正規化する，(12) 相似類のモジュライ点へ射影する，(13) ここまでの合成が誘導する写像を反復する，(14) 退化三角形を境界として軌道をコンパクト化する，(15) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ExcentralTransform → OrthocenterMark → SideReflectionTrace → TriangleFormation → CentroidMark → VertexCircleTrace → TriangleFormation → AnticomplementaryTransform → ExcentralTransform → AnticomplementaryTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 凸体関手の合成力学（CentroidBody・SteinerSymmetrization・PolarDual・VolumeNormalization）

- ID: `research.autonomous.convex_body.7bf1d60bd4`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重心体をとる，(2) 主慣性軸方向にSteiner対称化する，(3) 重心体をとる，(4) 交叉体をとる，(5) 差体をとる，(6) 射影体をとる，(7) 重心体をとる，(8) 主慣性軸方向にSteiner対称化する，(9) 原点に関する極体をとる，(10) 差体をとる，(11) 主慣性軸方向にSteiner対称化する，(12) 差体をとる，(13) 原点に関する極体をとる，(14) 射影体をとる，(15) 自身と極体のMinkowski和をとる，(16) 原点に関する極体をとる，(17) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CentroidBody → SteinerSymmetrization → CentroidBody → IntersectionBody → DifferenceBody → ProjectionBody → CentroidBody → SteinerSymmetrization → PolarDual → DifferenceBody → SteinerSymmetrization → DifferenceBody → PolarDual → ProjectionBody → MinkowskiPolarSum → PolarDual → VolumeNormalization → ConvexFixedPointQuery`

### 平面代数曲線の合成変換（ProjectiveClosure・AffineChartChange・IsogonalCremona・Evolute）

- ID: `research.autonomous.plane_curve.6d8428e31a`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `birational_periodicity`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 射影閉包をとり無限遠点を加える，(2) 基点を避ける一般アフィンチャートへ移す，(3) 正則接線族の射影双対曲線をとる，(4) 定義多項式のHessian曲線をとる，(5) 法線方向の代数的平行曲線をとる，(6) 定義多項式のHessian曲線をとる，(7) 射影閉包をとり無限遠点を加える，(8) 基点を避ける一般アフィンチャートへ移す，(9) 法線方向の代数的平行曲線をとる，(10) 原点中心の円反転像をとる，(11) 射影閉包をとり無限遠点を加える，(12) 基点を避ける一般アフィンチャートへ移す，(13) 定義多項式のHessian曲線をとる，(14) 法線方向の代数的平行曲線をとる，(15) 固定非退化二次形式に関する極逆像をとる，(16) 固定基準三角形に関する等角共役Cremona像をとる，(17) 法線族の包絡線である発展曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectiveClosure → AffineChartChange → ProjectiveDual → HessianCurve → OffsetCurve → HessianCurve → ProjectiveClosure → AffineChartChange → OffsetCurve → CircleInversion → ProjectiveClosure → AffineChartChange → HessianCurve → OffsetCurve → PolarReciprocal → IsogonalCremona → Evolute → BirationalPeriodQuery`

### 多項式変換と算術観測（CriticalValuePolynomial・DerivativeRenormalization・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.ec111153c9`
- 状態: `unresolved_by_mathos`
- 射数: `17`
- 問い: `recurrence_order_drop`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 臨界値を根にもつ消去多項式を作る，(2) 導関数をモニックに再正規化する，(3) 重複度付き根配置へ移す，(4) 根配置からモニック多項式を再構成する，(5) 根を二乗するGraeffe変換を施す，(6) 導関数をモニックに再正規化する，(7) 根を逆数へ移す相反多項式をとる，(8) 臨界値を根にもつ消去多項式を作る，(9) 根の重心を0へ移す平行移動共役を施す，(10) 根を二乗するGraeffe変換を施す，(11) 根の重心を0へ移す平行移動共役を施す，(12) 重複度付き根配置へ移す，(13) 根の冪和モーメント列を作る，(14) モーメントからHankel行列族を作る，(15) 主小行列式列をとる，(16) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CriticalValuePolynomial → DerivativeRenormalization → RootMultiset → PolynomialReconstruction → GraeffeTransform → DerivativeRenormalization → ReciprocalPolynomial → CriticalValuePolynomial → ShiftConjugacy → GraeffeTransform → ShiftConjugacy → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### Markov関手と到達時刻不変量（TimeReversal・StateLumping・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.00fb8cec39`
- 状態: `unresolved_by_mathos`
- 射数: `15`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `18`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 定常分布に関する時間反転をとる，(2) 自己同型軌道に沿って強 lumping する，(3) 定常分布に関する時間反転をとる，(4) 自身との同期積連鎖を作る，(5) 自己同型軌道に沿って強 lumping する，(6) 自身との同期積連鎖を作る，(7) 恒等遷移との凸結合でlazy化する，(8) 正の固有関数によるDoob変換を施す，(9) 恒等遷移との凸結合でlazy化する，(10) 指定集合で吸収させ過渡核をとる，(11) 過渡核のGreen作用素をとる，(12) 到達時刻の高次モーメント連立系を作る，(13) モーメント次数方向の漸化式を抽出する，(14) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `TimeReversal → StateLumping → TimeReversal → ProductChain → StateLumping → ProductChain → LazyPerturbation → DoobTransform → LazyPerturbation → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 三角形変換の合成力学（MedialTransform・OrthocenterMark・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.ab98e36371`
- 状態: `unresolved_by_mathos`
- 射数: `15`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `19`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 三辺の中点三角形へ移す，(2) 垂心を標識点として付加する，(3) 標識点から三辺への垂足三点をとる，(4) 三点を頂点とする向き付き三角形を作る，(5) 垂心を標識点として付加する，(6) 各頂点と標識点が定める円の対応交点をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 三辺の中点三角形へ移す，(9) 傍心三角形へ移す，(10) 重心・面積・向きを固定して相似正規化する，(11) 相似類のモジュライ点へ射影する，(12) ここまでの合成が誘導する写像を反復する，(13) 退化三角形を境界として軌道をコンパクト化する，(14) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `MedialTransform → OrthocenterMark → PedalProjection → TriangleFormation → OrthocenterMark → VertexCircleTrace → TriangleFormation → MedialTransform → ExcentralTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 平面代数曲線の合成変換（Evolute・PolarReciprocal・Evolute・PolarReciprocal）

- ID: `research.autonomous.plane_curve.e0cf609cf2`
- 状態: `unresolved_by_mathos`
- 射数: `16`
- 問い: `birational_periodicity`
- 難度仮説: `19`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 法線族の包絡線である発展曲線をとる，(2) 固定非退化二次形式に関する極逆像をとる，(3) 正則接線族の射影双対曲線をとる，(4) 固定基準三角形に関する等角共役Cremona像をとる，(5) 法線方向の代数的平行曲線をとる，(6) 正則接線族の射影双対曲線をとる，(7) 射影閉包をとり無限遠点を加える，(8) 基点を避ける一般アフィンチャートへ移す，(9) 固定基準三角形に関する等角共役Cremona像をとる，(10) 法線方向の代数的平行曲線をとる，(11) 射影閉包をとり無限遠点を加える，(12) 基点を避ける一般アフィンチャートへ移す，(13) 定義多項式のHessian曲線をとる，(14) 法線族の包絡線である発展曲線をとる，(15) 固定非退化二次形式に関する極逆像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `Evolute → PolarReciprocal → ProjectiveDual → IsogonalCremona → OffsetCurve → ProjectiveDual → ProjectiveClosure → AffineChartChange → IsogonalCremona → OffsetCurve → ProjectiveClosure → AffineChartChange → HessianCurve → Evolute → PolarReciprocal → BirationalPeriodQuery`

### 凸体関手の合成力学（SteinerSymmetrization・DifferenceBody・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.96749f9775`
- 状態: `unresolved_by_mathos`
- 射数: `16`
- 問い: `convex_body_dynamics`
- 難度仮説: `19`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 主慣性軸方向にSteiner対称化する，(2) 差体をとる，(3) 原点に関する極体をとる，(4) 主慣性軸方向にSteiner対称化する，(5) 交叉体をとる，(6) 射影体をとる，(7) 重心体をとる，(8) 差体をとる，(9) 交叉体をとる，(10) 重心体をとる，(11) 原点に関する極体をとる，(12) 面積と二次モーメントを固定して正規化する，(13) ここまでの凸体関手を反復する，(14) 支持関数の軌道へ移す，(15) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `SteinerSymmetrization → DifferenceBody → PolarDual → SteinerSymmetrization → IntersectionBody → ProjectionBody → CentroidBody → DifferenceBody → IntersectionBody → CentroidBody → PolarDual → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 多項式変換と算術観測（ReciprocalPolynomial・DerivativeRenormalization・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.8b0649c5d1`
- 状態: `unresolved_by_mathos`
- 射数: `17`
- 問い: `recurrence_order_drop`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を逆数へ移す相反多項式をとる，(2) 導関数をモニックに再正規化する，(3) 根を逆数へ移す相反多項式をとる，(4) 根を二乗するGraeffe変換を施す，(5) 根の重心を0へ移す平行移動共役を施す，(6) 重複度付き根配置へ移す，(7) 根配置からモニック多項式を再構成する，(8) 臨界値を根にもつ消去多項式を作る，(9) 根を二乗するGraeffe変換を施す，(10) 導関数をモニックに再正規化する，(11) 根の重心を0へ移す平行移動共役を施す，(12) 重複度付き根配置へ移す，(13) 根の冪和モーメント列を作る，(14) モーメントからHankel行列族を作る，(15) 主小行列式列をとる，(16) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ReciprocalPolynomial → DerivativeRenormalization → ReciprocalPolynomial → GraeffeTransform → ShiftConjugacy → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → GraeffeTransform → DerivativeRenormalization → ShiftConjugacy → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### Markov関手と到達時刻不変量（DoobTransform・ProductChain・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.ab0c02a5fc`
- 状態: `unresolved_by_mathos`
- 射数: `19`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `22`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 正の固有関数によるDoob変換を施す，(2) 自身との同期積連鎖を作る，(3) 正の固有関数によるDoob変換を施す，(4) 恒等遷移との凸結合でlazy化する，(5) 正の固有関数によるDoob変換を施す，(6) 自己同型軌道に沿って強 lumping する，(7) 自身との同期積連鎖を作る，(8) 恒等遷移との凸結合でlazy化する，(9) 自身との同期積連鎖を作る，(10) 定常分布に関する時間反転をとる，(11) 自己同型軌道に沿って強 lumping する，(12) 恒等遷移との凸結合でlazy化する，(13) 自己同型軌道に沿って強 lumping する，(14) 定常分布に関する時間反転をとる，(15) 指定集合で吸収させ過渡核をとる，(16) 過渡核のGreen作用素をとる，(17) 到達時刻の高次モーメント連立系を作る，(18) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DoobTransform → ProductChain → DoobTransform → LazyPerturbation → DoobTransform → StateLumping → ProductChain → LazyPerturbation → ProductChain → TimeReversal → StateLumping → LazyPerturbation → StateLumping → TimeReversal → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 三角形変換の合成力学（OrthocenterMark・PedalProjection・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.9feadc000f`
- 状態: `unresolved_by_mathos`
- 射数: `19`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `23`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 垂心を標識点として付加する，(2) 標識点から三辺への垂足三点をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 類似重心を標識点として付加する，(5) 標識点を三辺に関して反射した三点をとる，(6) 三点を頂点とする向き付き三角形を作る，(7) 垂心を標識点として付加する，(8) 標識点を通る三本のcevianの辺上の足をとる，(9) 三点を頂点とする向き付き三角形を作る，(10) 垂足三角形へ移す，(11) 三辺の中点三角形へ移す，(12) 傍心三角形へ移す，(13) 三辺の中点三角形へ移す，(14) 重心・面積・向きを固定して相似正規化する，(15) 相似類のモジュライ点へ射影する，(16) ここまでの合成が誘導する写像を反復する，(17) 退化三角形を境界として軌道をコンパクト化する，(18) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `OrthocenterMark → PedalProjection → TriangleFormation → SymmedianMark → SideReflectionTrace → TriangleFormation → OrthocenterMark → CevianTrace → TriangleFormation → OrthicTransform → MedialTransform → ExcentralTransform → MedialTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 多項式変換と算術観測（GraeffeTransform・CriticalValuePolynomial・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.0a94cbe9b4`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `22`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を二乗するGraeffe変換を施す，(2) 臨界値を根にもつ消去多項式を作る，(3) 根の重心を0へ移す平行移動共役を施す，(4) 臨界値を根にもつ消去多項式を作る，(5) 根を二乗するGraeffe変換を施す，(6) 根の重心を0へ移す平行移動共役を施す，(7) 根を二乗するGraeffe変換を施す，(8) 根を逆数へ移す相反多項式をとる，(9) 根の重心を0へ移す平行移動共役を施す，(10) 導関数をモニックに再正規化する，(11) 根を逆数へ移す相反多項式をとる，(12) 重複度付き根配置へ移す，(13) 根の冪和モーメント列を作る，(14) モーメントからHankel行列族を作る，(15) 主小行列式列をとる，(16) 満たす最小線形漸化式を抽出する，(17) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `GraeffeTransform → CriticalValuePolynomial → ShiftConjugacy → CriticalValuePolynomial → GraeffeTransform → ShiftConjugacy → GraeffeTransform → ReciprocalPolynomial → ShiftConjugacy → DerivativeRenormalization → ReciprocalPolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 平面代数曲線の合成変換（IsogonalCremona・CircleInversion・ResolveSingularities・CurveInvariantExtraction）

- ID: `research.autonomous.plane_curve.541d89a1e0`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `degree_genus_formula`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定基準三角形に関する等角共役Cremona像をとる，(2) 原点中心の円反転像をとる，(3) 法線族の包絡線である発展曲線をとる，(4) 射影閉包をとり無限遠点を加える，(5) 基点を避ける一般アフィンチャートへ移す，(6) 法線方向の代数的平行曲線をとる，(7) 固定光源からの反射光線族の包絡線をとる，(8) 射影閉包をとり無限遠点を加える，(9) 基点を避ける一般アフィンチャートへ移す，(10) 固定光源からの反射光線族の包絡線をとる，(11) 定義多項式のHessian曲線をとる，(12) 原点中心の円反転像をとる，(13) 固定光源からの反射光線族の包絡線をとる，(14) 原点中心の円反転像をとる，(15) 射影閉包をとり無限遠点を加える，(16) 全特異点を解消して正規化曲線を得る，(17) 次数、分岐、種数、自己交点データを抽出する。最後に、次数と幾何種数を初期曲線の不変量で表示し例外を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IsogonalCremona → CircleInversion → Evolute → ProjectiveClosure → AffineChartChange → OffsetCurve → Catacaustic → ProjectiveClosure → AffineChartChange → Catacaustic → HessianCurve → CircleInversion → Catacaustic → CircleInversion → ProjectiveClosure → ResolveSingularities → CurveInvariantExtraction → DegreeGenusQuery`

### 凸体関手の合成力学（DifferenceBody・PolarDual・MinkowskiPolarSum・VolumeNormalization）

- ID: `research.autonomous.convex_body.0ff754643d`
- 状態: `unresolved_by_mathos`
- 射数: `19`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `22`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 差体をとる，(2) 原点に関する極体をとる，(3) 主慣性軸方向にSteiner対称化する，(4) 交叉体をとる，(5) 原点に関する極体をとる，(6) 射影体をとる，(7) 原点に関する極体をとる，(8) 主慣性軸方向にSteiner対称化する，(9) 差体をとる，(10) 重心体をとる，(11) 射影体をとる，(12) 主慣性軸方向にSteiner対称化する，(13) 差体をとる，(14) 交叉体をとる，(15) 射影体をとる，(16) 交叉体をとる，(17) 自身と極体のMinkowski和をとる，(18) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DifferenceBody → PolarDual → SteinerSymmetrization → IntersectionBody → PolarDual → ProjectionBody → PolarDual → SteinerSymmetrization → DifferenceBody → CentroidBody → ProjectionBody → SteinerSymmetrization → DifferenceBody → IntersectionBody → ProjectionBody → IntersectionBody → MinkowskiPolarSum → VolumeNormalization → ConvexFixedPointQuery`

### Markov関手と到達時刻不変量（LazyPerturbation・TimeReversal・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.085bf4410e`
- 状態: `unresolved_by_mathos`
- 射数: `19`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `22`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 恒等遷移との凸結合でlazy化する，(2) 定常分布に関する時間反転をとる，(3) 自己同型軌道に沿って強 lumping する，(4) 自身との同期積連鎖を作る，(5) 恒等遷移との凸結合でlazy化する，(6) 定常分布に関する時間反転をとる，(7) 正の固有関数によるDoob変換を施す，(8) 定常分布に関する時間反転をとる，(9) 恒等遷移との凸結合でlazy化する，(10) 正の固有関数によるDoob変換を施す，(11) 自身との同期積連鎖を作る，(12) 正の固有関数によるDoob変換を施す，(13) 自己同型軌道に沿って強 lumping する，(14) 自身との同期積連鎖を作る，(15) 指定集合で吸収させ過渡核をとる，(16) 過渡核のGreen作用素をとる，(17) 到達時刻の高次モーメント連立系を作る，(18) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `LazyPerturbation → TimeReversal → StateLumping → ProductChain → LazyPerturbation → TimeReversal → DoobTransform → TimeReversal → LazyPerturbation → DoobTransform → ProductChain → DoobTransform → StateLumping → ProductChain → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 三角形変換の合成力学（IncenterMark・VertexCircleTrace・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.1d4d95216a`
- 状態: `unresolved_by_mathos`
- 射数: `16`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `20`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 内心を標識点として付加する，(2) 各頂点と標識点が定める円の対応交点をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 傍心三角形へ移す，(5) 反中点三角形へ移す，(6) 垂心を標識点として付加する，(7) 標識点を三辺に関して反射した三点をとる，(8) 三点を頂点とする向き付き三角形を作る，(9) 傍心三角形へ移す，(10) 反中点三角形へ移す，(11) 重心・面積・向きを固定して相似正規化する，(12) 相似類のモジュライ点へ射影する，(13) ここまでの合成が誘導する写像を反復する，(14) 退化三角形を境界として軌道をコンパクト化する，(15) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IncenterMark → VertexCircleTrace → TriangleFormation → ExcentralTransform → AnticomplementaryTransform → OrthocenterMark → SideReflectionTrace → TriangleFormation → ExcentralTransform → AnticomplementaryTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 凸体関手の合成力学（IntersectionBody・MinkowskiPolarSum・DifferenceBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.d1c2cf6f94`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 交叉体をとる，(2) 自身と極体のMinkowski和をとる，(3) 主慣性軸方向にSteiner対称化する，(4) 原点に関する極体をとる，(5) 交叉体をとる，(6) 主慣性軸方向にSteiner対称化する，(7) 射影体をとる，(8) 自身と極体のMinkowski和をとる，(9) 射影体をとる，(10) 差体をとる，(11) 重心体をとる，(12) 主慣性軸方向にSteiner対称化する，(13) 自身と極体のMinkowski和をとる，(14) 原点に関する極体をとる，(15) 射影体をとる，(16) 差体をとる，(17) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IntersectionBody → MinkowskiPolarSum → SteinerSymmetrization → PolarDual → IntersectionBody → SteinerSymmetrization → ProjectionBody → MinkowskiPolarSum → ProjectionBody → DifferenceBody → CentroidBody → SteinerSymmetrization → MinkowskiPolarSum → PolarDual → ProjectionBody → DifferenceBody → VolumeNormalization → ConvexFixedPointQuery`

### 平面代数曲線の合成変換（PolarReciprocal・ProjectiveDual・HessianCurve・PolarReciprocal）

- ID: `research.autonomous.plane_curve.6bf2535a3d`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `birational_periodicity`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定非退化二次形式に関する極逆像をとる，(2) 正則接線族の射影双対曲線をとる，(3) 射影閉包をとり無限遠点を加える，(4) 基点を避ける一般アフィンチャートへ移す，(5) 原点中心の円反転像をとる，(6) 固定光源からの反射光線族の包絡線をとる，(7) 原点中心の円反転像をとる，(8) 固定非退化二次形式に関する極逆像をとる，(9) 法線族の包絡線である発展曲線をとる，(10) 原点中心の円反転像をとる，(11) 正則接線族の射影双対曲線をとる，(12) 射影閉包をとり無限遠点を加える，(13) 基点を避ける一般アフィンチャートへ移す，(14) 法線族の包絡線である発展曲線をとる，(15) 正則接線族の射影双対曲線をとる，(16) 定義多項式のHessian曲線をとる，(17) 固定非退化二次形式に関する極逆像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `PolarReciprocal → ProjectiveDual → ProjectiveClosure → AffineChartChange → CircleInversion → Catacaustic → CircleInversion → PolarReciprocal → Evolute → CircleInversion → ProjectiveDual → ProjectiveClosure → AffineChartChange → Evolute → ProjectiveDual → HessianCurve → PolarReciprocal → BirationalPeriodQuery`

### 多項式変換と算術観測（ReciprocalPolynomial・DerivativeRenormalization・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.d7ea8ae91b`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `recurrence_order_drop`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を逆数へ移す相反多項式をとる，(2) 導関数をモニックに再正規化する，(3) 根の重心を0へ移す平行移動共役を施す，(4) 根を逆数へ移す相反多項式をとる，(5) 根を二乗するGraeffe変換を施す，(6) 根の重心を0へ移す平行移動共役を施す，(7) 臨界値を根にもつ消去多項式を作る，(8) 根の重心を0へ移す平行移動共役を施す，(9) 根を二乗するGraeffe変換を施す，(10) 臨界値を根にもつ消去多項式を作る，(11) 導関数をモニックに再正規化する，(12) 根を逆数へ移す相反多項式をとる，(13) 重複度付き根配置へ移す，(14) 根の冪和モーメント列を作る，(15) モーメントからHankel行列族を作る，(16) 主小行列式列をとる，(17) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ReciprocalPolynomial → DerivativeRenormalization → ShiftConjugacy → ReciprocalPolynomial → GraeffeTransform → ShiftConjugacy → CriticalValuePolynomial → ShiftConjugacy → GraeffeTransform → CriticalValuePolynomial → DerivativeRenormalization → ReciprocalPolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 三角形変換の合成力学（IncenterMark・VertexCircleTrace・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.ffc3bf5bb1`
- 状態: `unresolved_by_mathos`
- 射数: `19`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `23`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 内心を標識点として付加する，(2) 各頂点と標識点が定める円の対応交点をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 垂足三角形へ移す，(5) 重心を標識点として付加する，(6) 標識点を三辺に関して反射した三点をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 三辺の中点三角形へ移す，(9) 重心を標識点として付加する，(10) 標識点を通る三本のcevianの辺上の足をとる，(11) 三点を頂点とする向き付き三角形を作る，(12) 傍心三角形へ移す，(13) 三辺の中点三角形へ移す，(14) 重心・面積・向きを固定して相似正規化する，(15) 相似類のモジュライ点へ射影する，(16) ここまでの合成が誘導する写像を反復する，(17) 退化三角形を境界として軌道をコンパクト化する，(18) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IncenterMark → VertexCircleTrace → TriangleFormation → OrthicTransform → CentroidMark → SideReflectionTrace → TriangleFormation → MedialTransform → CentroidMark → CevianTrace → TriangleFormation → ExcentralTransform → MedialTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### Markov関手と到達時刻不変量（DoobTransform・LazyPerturbation・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.402eb450ea`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 正の固有関数によるDoob変換を施す，(2) 恒等遷移との凸結合でlazy化する，(3) 正の固有関数によるDoob変換を施す，(4) 自己同型軌道に沿って強 lumping する，(5) 定常分布に関する時間反転をとる，(6) 自身との同期積連鎖を作る，(7) 恒等遷移との凸結合でlazy化する，(8) 定常分布に関する時間反転をとる，(9) 自身との同期積連鎖を作る，(10) 定常分布に関する時間反転をとる，(11) 恒等遷移との凸結合でlazy化する，(12) 自身との同期積連鎖を作る，(13) 正の固有関数によるDoob変換を施す，(14) 指定集合で吸収させ過渡核をとる，(15) 過渡核のGreen作用素をとる，(16) 到達時刻の高次モーメント連立系を作る，(17) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DoobTransform → LazyPerturbation → DoobTransform → StateLumping → TimeReversal → ProductChain → LazyPerturbation → TimeReversal → ProductChain → TimeReversal → LazyPerturbation → ProductChain → DoobTransform → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### Markov関手と到達時刻不変量（ProductChain・DoobTransform・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.4902fe90e1`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身との同期積連鎖を作る，(2) 正の固有関数によるDoob変換を施す，(3) 自身との同期積連鎖を作る，(4) 定常分布に関する時間反転をとる，(5) 自身との同期積連鎖を作る，(6) 正の固有関数によるDoob変換を施す，(7) 定常分布に関する時間反転をとる，(8) 正の固有関数によるDoob変換を施す，(9) 定常分布に関する時間反転をとる，(10) 恒等遷移との凸結合でlazy化する，(11) 自己同型軌道に沿って強 lumping する，(12) 恒等遷移との凸結合でlazy化する，(13) 自己同型軌道に沿って強 lumping する，(14) 指定集合で吸収させ過渡核をとる，(15) 過渡核のGreen作用素をとる，(16) 到達時刻の高次モーメント連立系を作る，(17) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProductChain → DoobTransform → ProductChain → TimeReversal → ProductChain → DoobTransform → TimeReversal → DoobTransform → TimeReversal → LazyPerturbation → StateLumping → LazyPerturbation → StateLumping → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 凸体関手の合成力学（SteinerSymmetrization・PolarDual・CentroidBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.0598ce32fe`
- 状態: `unresolved_by_mathos`
- 射数: `19`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 主慣性軸方向にSteiner対称化する，(2) 原点に関する極体をとる，(3) 自身と極体のMinkowski和をとる，(4) 射影体をとる，(5) 交叉体をとる，(6) 原点に関する極体をとる，(7) 射影体をとる，(8) 重心体をとる，(9) 原点に関する極体をとる，(10) 主慣性軸方向にSteiner対称化する，(11) 自身と極体のMinkowski和をとる，(12) 主慣性軸方向にSteiner対称化する，(13) 交叉体をとる，(14) 自身と極体のMinkowski和をとる，(15) 交叉体をとる，(16) 射影体をとる，(17) 重心体をとる，(18) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `SteinerSymmetrization → PolarDual → MinkowskiPolarSum → ProjectionBody → IntersectionBody → PolarDual → ProjectionBody → CentroidBody → PolarDual → SteinerSymmetrization → MinkowskiPolarSum → SteinerSymmetrization → IntersectionBody → MinkowskiPolarSum → IntersectionBody → ProjectionBody → CentroidBody → VolumeNormalization → ConvexFixedPointQuery`

### 多項式変換と算術観測（DerivativeRenormalization・ReciprocalPolynomial・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.260468f3ac`
- 状態: `unresolved_by_mathos`
- 射数: `16`
- 問い: `recurrence_order_drop`
- 難度仮説: `20`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 導関数をモニックに再正規化する，(2) 根を逆数へ移す相反多項式をとる，(3) 根の重心を0へ移す平行移動共役を施す，(4) 根を二乗するGraeffe変換を施す，(5) 重複度付き根配置へ移す，(6) 根配置からモニック多項式を再構成する，(7) 導関数をモニックに再正規化する，(8) 臨界値を根にもつ消去多項式を作る，(9) 根を二乗するGraeffe変換を施す，(10) 臨界値を根にもつ消去多項式を作る，(11) 重複度付き根配置へ移す，(12) 根の冪和モーメント列を作る，(13) モーメントからHankel行列族を作る，(14) 主小行列式列をとる，(15) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DerivativeRenormalization → ReciprocalPolynomial → ShiftConjugacy → GraeffeTransform → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → CriticalValuePolynomial → GraeffeTransform → CriticalValuePolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 平面代数曲線の合成変換（ProjectiveDual・CircleInversion・ProjectiveClosure・AffineChartChange）

- ID: `research.autonomous.plane_curve.bf2cc39d27`
- 状態: `unresolved_by_mathos`
- 射数: `16`
- 問い: `birational_periodicity`
- 難度仮説: `19`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 正則接線族の射影双対曲線をとる，(2) 原点中心の円反転像をとる，(3) 法線方向の代数的平行曲線をとる，(4) 正則接線族の射影双対曲線をとる，(5) 固定光源からの反射光線族の包絡線をとる，(6) 定義多項式のHessian曲線をとる，(7) 法線族の包絡線である発展曲線をとる，(8) 固定基準三角形に関する等角共役Cremona像をとる，(9) 法線方向の代数的平行曲線をとる，(10) 定義多項式のHessian曲線をとる，(11) 法線族の包絡線である発展曲線をとる，(12) 固定基準三角形に関する等角共役Cremona像をとる，(13) 固定光源からの反射光線族の包絡線をとる，(14) 射影閉包をとり無限遠点を加える，(15) 基点を避ける一般アフィンチャートへ移す。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectiveDual → CircleInversion → OffsetCurve → ProjectiveDual → Catacaustic → HessianCurve → Evolute → IsogonalCremona → OffsetCurve → HessianCurve → Evolute → IsogonalCremona → Catacaustic → ProjectiveClosure → AffineChartChange → BirationalPeriodQuery`

### 三角形変換の合成力学（SymmedianMark・SideReflectionTrace・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.78f44bcaa6`
- 状態: `unresolved_by_mathos`
- 射数: `16`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `20`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 類似重心を標識点として付加する，(2) 標識点を三辺に関して反射した三点をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 三辺の中点三角形へ移す，(5) 内心を標識点として付加する，(6) 標識点を通る三本のcevianの辺上の足をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 垂足三角形へ移す，(9) 三辺の中点三角形へ移す，(10) 垂足三角形へ移す，(11) 重心・面積・向きを固定して相似正規化する，(12) 相似類のモジュライ点へ射影する，(13) ここまでの合成が誘導する写像を反復する，(14) 退化三角形を境界として軌道をコンパクト化する，(15) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `SymmedianMark → SideReflectionTrace → TriangleFormation → MedialTransform → IncenterMark → CevianTrace → TriangleFormation → OrthicTransform → MedialTransform → OrthicTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### Markov関手と到達時刻不変量（ProductChain・LazyPerturbation・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.14f922456e`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身との同期積連鎖を作る，(2) 恒等遷移との凸結合でlazy化する，(3) 定常分布に関する時間反転をとる，(4) 自身との同期積連鎖を作る，(5) 自己同型軌道に沿って強 lumping する，(6) 恒等遷移との凸結合でlazy化する，(7) 自身との同期積連鎖を作る，(8) 恒等遷移との凸結合でlazy化する，(9) 定常分布に関する時間反転をとる，(10) 正の固有関数によるDoob変換を施す，(11) 定常分布に関する時間反転をとる，(12) 正の固有関数によるDoob変換を施す，(13) 自己同型軌道に沿って強 lumping する，(14) 指定集合で吸収させ過渡核をとる，(15) 過渡核のGreen作用素をとる，(16) 到達時刻の高次モーメント連立系を作る，(17) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProductChain → LazyPerturbation → TimeReversal → ProductChain → StateLumping → LazyPerturbation → ProductChain → LazyPerturbation → TimeReversal → DoobTransform → TimeReversal → DoobTransform → StateLumping → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 平面代数曲線の合成変換（IsogonalCremona・HessianCurve・HessianCurve・OffsetCurve）

- ID: `research.autonomous.plane_curve.301e53f733`
- 状態: `unresolved_by_mathos`
- 射数: `19`
- 問い: `birational_periodicity`
- 難度仮説: `22`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定基準三角形に関する等角共役Cremona像をとる，(2) 定義多項式のHessian曲線をとる，(3) 原点中心の円反転像をとる，(4) 正則接線族の射影双対曲線をとる，(5) 法線族の包絡線である発展曲線をとる，(6) 正則接線族の射影双対曲線をとる，(7) 固定光源からの反射光線族の包絡線をとる，(8) 射影閉包をとり無限遠点を加える，(9) 基点を避ける一般アフィンチャートへ移す，(10) 定義多項式のHessian曲線をとる，(11) 法線族の包絡線である発展曲線をとる，(12) 法線方向の代数的平行曲線をとる，(13) 法線族の包絡線である発展曲線をとる，(14) 射影閉包をとり無限遠点を加える，(15) 基点を避ける一般アフィンチャートへ移す，(16) 固定光源からの反射光線族の包絡線をとる，(17) 定義多項式のHessian曲線をとる，(18) 法線方向の代数的平行曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IsogonalCremona → HessianCurve → CircleInversion → ProjectiveDual → Evolute → ProjectiveDual → Catacaustic → ProjectiveClosure → AffineChartChange → HessianCurve → Evolute → OffsetCurve → Evolute → ProjectiveClosure → AffineChartChange → Catacaustic → HessianCurve → OffsetCurve → BirationalPeriodQuery`

### 多項式変換と算術観測（RootMultiset・PolynomialReconstruction・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.82511a67a8`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `recurrence_order_drop`
- 難度仮説: `22`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重複度付き根配置へ移す，(2) 根配置からモニック多項式を再構成する，(3) 根を二乗するGraeffe変換を施す，(4) 重複度付き根配置へ移す，(5) 根配置からモニック多項式を再構成する，(6) 根を逆数へ移す相反多項式をとる，(7) 根の重心を0へ移す平行移動共役を施す，(8) 導関数をモニックに再正規化する，(9) 根を二乗するGraeffe変換を施す，(10) 導関数をモニックに再正規化する，(11) 臨界値を根にもつ消去多項式を作る，(12) 根を逆数へ移す相反多項式をとる，(13) 重複度付き根配置へ移す，(14) 根の冪和モーメント列を作る，(15) モーメントからHankel行列族を作る，(16) 主小行列式列をとる，(17) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `RootMultiset → PolynomialReconstruction → GraeffeTransform → RootMultiset → PolynomialReconstruction → ReciprocalPolynomial → ShiftConjugacy → DerivativeRenormalization → GraeffeTransform → DerivativeRenormalization → CriticalValuePolynomial → ReciprocalPolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 凸体関手の合成力学（CentroidBody・SteinerSymmetrization・PolarDual・VolumeNormalization）

- ID: `research.autonomous.convex_body.54aac65ad1`
- 状態: `unresolved_by_mathos`
- 射数: `16`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `19`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重心体をとる，(2) 主慣性軸方向にSteiner対称化する，(3) 原点に関する極体をとる，(4) 射影体をとる，(5) 重心体をとる，(6) 差体をとる，(7) 主慣性軸方向にSteiner対称化する，(8) 射影体をとる，(9) 自身と極体のMinkowski和をとる，(10) 差体をとる，(11) 交叉体をとる，(12) 自身と極体のMinkowski和をとる，(13) 交叉体をとる，(14) 原点に関する極体をとる，(15) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CentroidBody → SteinerSymmetrization → PolarDual → ProjectionBody → CentroidBody → DifferenceBody → SteinerSymmetrization → ProjectionBody → MinkowskiPolarSum → DifferenceBody → IntersectionBody → MinkowskiPolarSum → IntersectionBody → PolarDual → VolumeNormalization → ConvexFixedPointQuery`

### 三角形変換の合成力学（ExcentralTransform・SymmedianMark・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.877868a930`
- 状態: `unresolved_by_mathos`
- 射数: `19`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `23`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 傍心三角形へ移す，(2) 類似重心を標識点として付加する，(3) 各頂点と標識点が定める円の対応交点をとる，(4) 三点を頂点とする向き付き三角形を作る，(5) 垂心を標識点として付加する，(6) 標識点を三辺に関して反射した三点をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 垂足三角形へ移す，(9) 反中点三角形へ移す，(10) 垂心を標識点として付加する，(11) 標識点を通る三本のcevianの辺上の足をとる，(12) 三点を頂点とする向き付き三角形を作る，(13) 傍心三角形へ移す，(14) 重心・面積・向きを固定して相似正規化する，(15) 相似類のモジュライ点へ射影する，(16) ここまでの合成が誘導する写像を反復する，(17) 退化三角形を境界として軌道をコンパクト化する，(18) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ExcentralTransform → SymmedianMark → VertexCircleTrace → TriangleFormation → OrthocenterMark → SideReflectionTrace → TriangleFormation → OrthicTransform → AnticomplementaryTransform → OrthocenterMark → CevianTrace → TriangleFormation → ExcentralTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 平面代数曲線の合成変換（HessianCurve・PolarReciprocal・PolarReciprocal・ProjectiveDual）

- ID: `research.autonomous.plane_curve.a113bf4f21`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `birational_periodicity`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 定義多項式のHessian曲線をとる，(2) 固定非退化二次形式に関する極逆像をとる，(3) 定義多項式のHessian曲線をとる，(4) 法線方向の代数的平行曲線をとる，(5) 原点中心の円反転像をとる，(6) 法線族の包絡線である発展曲線をとる，(7) 固定基準三角形に関する等角共役Cremona像をとる，(8) 射影閉包をとり無限遠点を加える，(9) 基点を避ける一般アフィンチャートへ移す，(10) 原点中心の円反転像をとる，(11) 定義多項式のHessian曲線をとる，(12) 原点中心の円反転像をとる，(13) 射影閉包をとり無限遠点を加える，(14) 基点を避ける一般アフィンチャートへ移す，(15) 正則接線族の射影双対曲線をとる，(16) 固定非退化二次形式に関する極逆像をとる，(17) 正則接線族の射影双対曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `HessianCurve → PolarReciprocal → HessianCurve → OffsetCurve → CircleInversion → Evolute → IsogonalCremona → ProjectiveClosure → AffineChartChange → CircleInversion → HessianCurve → CircleInversion → ProjectiveClosure → AffineChartChange → ProjectiveDual → PolarReciprocal → ProjectiveDual → BirationalPeriodQuery`

### 三角形変換の合成力学（AnticomplementaryTransform・SymmedianMark・SimilarityNormalization・ModuliProjection）

- ID: `research.autonomous.triangle_dynamics.478431726e`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `triangle_transform_fixed_points`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0625`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 反中点三角形へ移す，(2) 類似重心を標識点として付加する，(3) 標識点から三辺への垂足三点をとる，(4) 三点を頂点とする向き付き三角形を作る，(5) 類似重心を標識点として付加する，(6) 標識点を三辺に関して反射した三点をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 内心を標識点として付加する，(9) 標識点から三辺への垂足三点をとる，(10) 三点を頂点とする向き付き三角形を作る，(11) 傍心三角形へ移す，(12) 反中点三角形へ移す，(13) 傍心三角形へ移す，(14) 反中点三角形へ移す，(15) 垂足三角形へ移す，(16) 重心・面積・向きを固定して相似正規化する，(17) 相似類のモジュライ点へ射影する。最後に、誘導写像の固定点と有限周期点を相似を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `AnticomplementaryTransform → SymmedianMark → PedalProjection → TriangleFormation → SymmedianMark → SideReflectionTrace → TriangleFormation → IncenterMark → PedalProjection → TriangleFormation → ExcentralTransform → AnticomplementaryTransform → ExcentralTransform → AnticomplementaryTransform → OrthicTransform → SimilarityNormalization → ModuliProjection → TriangleFixedPointQuery`

### 多項式変換と算術観測（DerivativeRenormalization・RootMultiset・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.24e0574bd5`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 導関数をモニックに再正規化する，(2) 重複度付き根配置へ移す，(3) 根配置からモニック多項式を再構成する，(4) 根を二乗するGraeffe変換を施す，(5) 根の重心を0へ移す平行移動共役を施す，(6) 重複度付き根配置へ移す，(7) 根配置からモニック多項式を再構成する，(8) 根の重心を0へ移す平行移動共役を施す，(9) 根を二乗するGraeffe変換を施す，(10) 根の重心を0へ移す平行移動共役を施す，(11) 根を逆数へ移す相反多項式をとる，(12) 導関数をモニックに再正規化する，(13) 臨界値を根にもつ消去多項式を作る，(14) 重複度付き根配置へ移す，(15) 根の冪和モーメント列を作る，(16) モーメントからHankel行列族を作る，(17) 主小行列式列をとる，(18) 満たす最小線形漸化式を抽出する，(19) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DerivativeRenormalization → RootMultiset → PolynomialReconstruction → GraeffeTransform → ShiftConjugacy → RootMultiset → PolynomialReconstruction → ShiftConjugacy → GraeffeTransform → ShiftConjugacy → ReciprocalPolynomial → DerivativeRenormalization → CriticalValuePolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 凸体関手の合成力学（SteinerSymmetrization・MinkowskiPolarSum・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.7a2c62478e`
- 状態: `unresolved_by_mathos`
- 射数: `19`
- 問い: `convex_body_dynamics`
- 難度仮説: `23`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 主慣性軸方向にSteiner対称化する，(2) 自身と極体のMinkowski和をとる，(3) 交叉体をとる，(4) 射影体をとる，(5) 重心体をとる，(6) 差体をとる，(7) 射影体をとる，(8) 交叉体をとる，(9) 重心体をとる，(10) 原点に関する極体をとる，(11) 自身と極体のMinkowski和をとる，(12) 重心体をとる，(13) 原点に関する極体をとる，(14) 差体をとる，(15) 面積と二次モーメントを固定して正規化する，(16) ここまでの凸体関手を反復する，(17) 支持関数の軌道へ移す，(18) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `SteinerSymmetrization → MinkowskiPolarSum → IntersectionBody → ProjectionBody → CentroidBody → DifferenceBody → ProjectionBody → IntersectionBody → CentroidBody → PolarDual → MinkowskiPolarSum → CentroidBody → PolarDual → DifferenceBody → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### Markov関手と到達時刻不変量（DoobTransform・TimeReversal・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.a1cb8d9d00`
- 状態: `unresolved_by_mathos`
- 射数: `19`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `22`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 正の固有関数によるDoob変換を施す，(2) 定常分布に関する時間反転をとる，(3) 正の固有関数によるDoob変換を施す，(4) 自己同型軌道に沿って強 lumping する，(5) 定常分布に関する時間反転をとる，(6) 自身との同期積連鎖を作る，(7) 自己同型軌道に沿って強 lumping する，(8) 定常分布に関する時間反転をとる，(9) 自身との同期積連鎖を作る，(10) 恒等遷移との凸結合でlazy化する，(11) 自身との同期積連鎖を作る，(12) 自己同型軌道に沿って強 lumping する，(13) 恒等遷移との凸結合でlazy化する，(14) 正の固有関数によるDoob変換を施す，(15) 指定集合で吸収させ過渡核をとる，(16) 過渡核のGreen作用素をとる，(17) 到達時刻の高次モーメント連立系を作る，(18) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DoobTransform → TimeReversal → DoobTransform → StateLumping → TimeReversal → ProductChain → StateLumping → TimeReversal → ProductChain → LazyPerturbation → ProductChain → StateLumping → LazyPerturbation → DoobTransform → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 凸体関手の合成力学（IntersectionBody・MinkowskiPolarSum・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.49a062c879`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `convex_body_dynamics`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 交叉体をとる，(2) 自身と極体のMinkowski和をとる，(3) 主慣性軸方向にSteiner対称化する，(4) 自身と極体のMinkowski和をとる，(5) 原点に関する極体をとる，(6) 射影体をとる，(7) 差体をとる，(8) 主慣性軸方向にSteiner対称化する，(9) 原点に関する極体をとる，(10) 射影体をとる，(11) 自身と極体のMinkowski和をとる，(12) 射影体をとる，(13) 交叉体をとる，(14) 重心体をとる，(15) 差体をとる，(16) 面積と二次モーメントを固定して正規化する，(17) ここまでの凸体関手を反復する，(18) 支持関数の軌道へ移す，(19) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IntersectionBody → MinkowskiPolarSum → SteinerSymmetrization → MinkowskiPolarSum → PolarDual → ProjectionBody → DifferenceBody → SteinerSymmetrization → PolarDual → ProjectionBody → MinkowskiPolarSum → ProjectionBody → IntersectionBody → CentroidBody → DifferenceBody → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 平面代数曲線の合成変換（PolarReciprocal・IsogonalCremona・Catacaustic・Evolute）

- ID: `research.autonomous.plane_curve.334c056d56`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `birational_periodicity`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定非退化二次形式に関する極逆像をとる，(2) 固定基準三角形に関する等角共役Cremona像をとる，(3) 原点中心の円反転像をとる，(4) 法線方向の代数的平行曲線をとる，(5) 固定非退化二次形式に関する極逆像をとる，(6) 法線族の包絡線である発展曲線をとる，(7) 固定非退化二次形式に関する極逆像をとる，(8) 正則接線族の射影双対曲線をとる，(9) 法線方向の代数的平行曲線をとる，(10) 法線族の包絡線である発展曲線をとる，(11) 法線方向の代数的平行曲線をとる，(12) 定義多項式のHessian曲線をとる，(13) 固定基準三角形に関する等角共役Cremona像をとる，(14) 原点中心の円反転像をとる，(15) 正則接線族の射影双対曲線をとる，(16) 固定光源からの反射光線族の包絡線をとる，(17) 法線族の包絡線である発展曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `PolarReciprocal → IsogonalCremona → CircleInversion → OffsetCurve → PolarReciprocal → Evolute → PolarReciprocal → ProjectiveDual → OffsetCurve → Evolute → OffsetCurve → HessianCurve → IsogonalCremona → CircleInversion → ProjectiveDual → Catacaustic → Evolute → BirationalPeriodQuery`

### 多項式変換と算術観測（CriticalValuePolynomial・GraeffeTransform・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.9c7d6ac077`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `recurrence_order_drop`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 臨界値を根にもつ消去多項式を作る，(2) 根を二乗するGraeffe変換を施す，(3) 臨界値を根にもつ消去多項式を作る，(4) 重複度付き根配置へ移す，(5) 根配置からモニック多項式を再構成する，(6) 根を二乗するGraeffe変換を施す，(7) 導関数をモニックに再正規化する，(8) 根の重心を0へ移す平行移動共役を施す，(9) 重複度付き根配置へ移す，(10) 根配置からモニック多項式を再構成する，(11) 根を二乗するGraeffe変換を施す，(12) 根を逆数へ移す相反多項式をとる，(13) 根の重心を0へ移す平行移動共役を施す，(14) 根を逆数へ移す相反多項式をとる，(15) 重複度付き根配置へ移す，(16) 根の冪和モーメント列を作る，(17) モーメントからHankel行列族を作る，(18) 主小行列式列をとる，(19) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CriticalValuePolynomial → GraeffeTransform → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → GraeffeTransform → DerivativeRenormalization → ShiftConjugacy → RootMultiset → PolynomialReconstruction → GraeffeTransform → ReciprocalPolynomial → ShiftConjugacy → ReciprocalPolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 三角形変換の合成力学（OrthicTransform・CircumcenterMark・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.bfc2154bc7`
- 状態: `unresolved_by_mathos`
- 射数: `19`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `23`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 垂足三角形へ移す，(2) 外心を標識点として付加する，(3) 標識点から三辺への垂足三点をとる，(4) 三点を頂点とする向き付き三角形を作る，(5) 三辺の中点三角形へ移す，(6) 内心を標識点として付加する，(7) 標識点を三辺に関して反射した三点をとる，(8) 三点を頂点とする向き付き三角形を作る，(9) 三辺の中点三角形へ移す，(10) 内心を標識点として付加する，(11) 標識点を三辺に関して反射した三点をとる，(12) 三点を頂点とする向き付き三角形を作る，(13) 三辺の中点三角形へ移す，(14) 重心・面積・向きを固定して相似正規化する，(15) 相似類のモジュライ点へ射影する，(16) ここまでの合成が誘導する写像を反復する，(17) 退化三角形を境界として軌道をコンパクト化する，(18) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `OrthicTransform → CircumcenterMark → PedalProjection → TriangleFormation → MedialTransform → IncenterMark → SideReflectionTrace → TriangleFormation → MedialTransform → IncenterMark → SideReflectionTrace → TriangleFormation → MedialTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### Markov関手と到達時刻不変量（StateLumping・LazyPerturbation・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.f83c2f51aa`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `23`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自己同型軌道に沿って強 lumping する，(2) 恒等遷移との凸結合でlazy化する，(3) 正の固有関数によるDoob変換を施す，(4) 自己同型軌道に沿って強 lumping する，(5) 正の固有関数によるDoob変換を施す，(6) 恒等遷移との凸結合でlazy化する，(7) 自己同型軌道に沿って強 lumping する，(8) 自身との同期積連鎖を作る，(9) 定常分布に関する時間反転をとる，(10) 正の固有関数によるDoob変換を施す，(11) 定常分布に関する時間反転をとる，(12) 自身との同期積連鎖を作る，(13) 定常分布に関する時間反転をとる，(14) 自身との同期積連鎖を作る，(15) 指定集合で吸収させ過渡核をとる，(16) 過渡核のGreen作用素をとる，(17) 到達時刻の高次モーメント連立系を作る，(18) モーメント次数方向の漸化式を抽出する，(19) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `StateLumping → LazyPerturbation → DoobTransform → StateLumping → DoobTransform → LazyPerturbation → StateLumping → ProductChain → TimeReversal → DoobTransform → TimeReversal → ProductChain → TimeReversal → ProductChain → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 凸体関手の合成力学（PolarDual・ProjectionBody・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.1359e64789`
- 状態: `unresolved_by_mathos`
- 射数: `17`
- 問い: `convex_body_dynamics`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 原点に関する極体をとる，(2) 射影体をとる，(3) 交叉体をとる，(4) 差体をとる，(5) 重心体をとる，(6) 原点に関する極体をとる，(7) 重心体をとる，(8) 差体をとる，(9) 主慣性軸方向にSteiner対称化する，(10) 射影体をとる，(11) 自身と極体のMinkowski和をとる，(12) 交叉体をとる，(13) 面積と二次モーメントを固定して正規化する，(14) ここまでの凸体関手を反復する，(15) 支持関数の軌道へ移す，(16) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `PolarDual → ProjectionBody → IntersectionBody → DifferenceBody → CentroidBody → PolarDual → CentroidBody → DifferenceBody → SteinerSymmetrization → ProjectionBody → MinkowskiPolarSum → IntersectionBody → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 平面代数曲線の合成変換（ProjectiveClosure・AffineChartChange・Catacaustic・IsogonalCremona）

- ID: `research.autonomous.plane_curve.0fa562c345`
- 状態: `unresolved_by_mathos`
- 射数: `17`
- 問い: `birational_periodicity`
- 難度仮説: `20`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 射影閉包をとり無限遠点を加える，(2) 基点を避ける一般アフィンチャートへ移す，(3) 法線方向の代数的平行曲線をとる，(4) 正則接線族の射影双対曲線をとる，(5) 定義多項式のHessian曲線をとる，(6) 射影閉包をとり無限遠点を加える，(7) 基点を避ける一般アフィンチャートへ移す，(8) 法線族の包絡線である発展曲線をとる，(9) 原点中心の円反転像をとる，(10) 定義多項式のHessian曲線をとる，(11) 原点中心の円反転像をとる，(12) 固定光源からの反射光線族の包絡線をとる，(13) 法線方向の代数的平行曲線をとる，(14) 固定基準三角形に関する等角共役Cremona像をとる，(15) 固定光源からの反射光線族の包絡線をとる，(16) 固定基準三角形に関する等角共役Cremona像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectiveClosure → AffineChartChange → OffsetCurve → ProjectiveDual → HessianCurve → ProjectiveClosure → AffineChartChange → Evolute → CircleInversion → HessianCurve → CircleInversion → Catacaustic → OffsetCurve → IsogonalCremona → Catacaustic → IsogonalCremona → BirationalPeriodQuery`

### 三角形変換の合成力学（CentroidMark・CevianTrace・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.c59096f5b8`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `22`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重心を標識点として付加する，(2) 標識点を通る三本のcevianの辺上の足をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 三辺の中点三角形へ移す，(5) 重心を標識点として付加する，(6) 各頂点と標識点が定める円の対応交点をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 類似重心を標識点として付加する，(9) 標識点を三辺に関して反射した三点をとる，(10) 三点を頂点とする向き付き三角形を作る，(11) 三辺の中点三角形へ移す，(12) 垂足三角形へ移す，(13) 重心・面積・向きを固定して相似正規化する，(14) 相似類のモジュライ点へ射影する，(15) ここまでの合成が誘導する写像を反復する，(16) 退化三角形を境界として軌道をコンパクト化する，(17) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CentroidMark → CevianTrace → TriangleFormation → MedialTransform → CentroidMark → VertexCircleTrace → TriangleFormation → SymmedianMark → SideReflectionTrace → TriangleFormation → MedialTransform → OrthicTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 多項式変換と算術観測（GraeffeTransform・ShiftConjugacy・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.df97122f69`
- 状態: `unresolved_by_mathos`
- 射数: `17`
- 問い: `recurrence_order_drop`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を二乗するGraeffe変換を施す，(2) 根の重心を0へ移す平行移動共役を施す，(3) 臨界値を根にもつ消去多項式を作る，(4) 重複度付き根配置へ移す，(5) 根配置からモニック多項式を再構成する，(6) 導関数をモニックに再正規化する，(7) 臨界値を根にもつ消去多項式を作る，(8) 根を二乗するGraeffe変換を施す，(9) 根を逆数へ移す相反多項式をとる，(10) 導関数をモニックに再正規化する，(11) 根を逆数へ移す相反多項式をとる，(12) 重複度付き根配置へ移す，(13) 根の冪和モーメント列を作る，(14) モーメントからHankel行列族を作る，(15) 主小行列式列をとる，(16) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `GraeffeTransform → ShiftConjugacy → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → CriticalValuePolynomial → GraeffeTransform → ReciprocalPolynomial → DerivativeRenormalization → ReciprocalPolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### Markov関手と到達時刻不変量（LazyPerturbation・StateLumping・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.ab19731118`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `23`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 恒等遷移との凸結合でlazy化する，(2) 自己同型軌道に沿って強 lumping する，(3) 定常分布に関する時間反転をとる，(4) 正の固有関数によるDoob変換を施す，(5) 恒等遷移との凸結合でlazy化する，(6) 定常分布に関する時間反転をとる，(7) 恒等遷移との凸結合でlazy化する，(8) 定常分布に関する時間反転をとる，(9) 正の固有関数によるDoob変換を施す，(10) 自己同型軌道に沿って強 lumping する，(11) 正の固有関数によるDoob変換を施す，(12) 自身との同期積連鎖を作る，(13) 自己同型軌道に沿って強 lumping する，(14) 自身との同期積連鎖を作る，(15) 指定集合で吸収させ過渡核をとる，(16) 過渡核のGreen作用素をとる，(17) 到達時刻の高次モーメント連立系を作る，(18) モーメント次数方向の漸化式を抽出する，(19) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `LazyPerturbation → StateLumping → TimeReversal → DoobTransform → LazyPerturbation → TimeReversal → LazyPerturbation → TimeReversal → DoobTransform → StateLumping → DoobTransform → ProductChain → StateLumping → ProductChain → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 凸体関手の合成力学（MinkowskiPolarSum・DifferenceBody・SteinerSymmetrization・VolumeNormalization）

- ID: `research.autonomous.convex_body.f7ce4b7e70`
- 状態: `unresolved_by_mathos`
- 射数: `19`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `22`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身と極体のMinkowski和をとる，(2) 差体をとる，(3) 射影体をとる，(4) 差体をとる，(5) 交叉体をとる，(6) 重心体をとる，(7) 自身と極体のMinkowski和をとる，(8) 主慣性軸方向にSteiner対称化する，(9) 自身と極体のMinkowski和をとる，(10) 射影体をとる，(11) 重心体をとる，(12) 主慣性軸方向にSteiner対称化する，(13) 射影体をとる，(14) 交叉体をとる，(15) 原点に関する極体をとる，(16) 交叉体をとる，(17) 主慣性軸方向にSteiner対称化する，(18) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `MinkowskiPolarSum → DifferenceBody → ProjectionBody → DifferenceBody → IntersectionBody → CentroidBody → MinkowskiPolarSum → SteinerSymmetrization → MinkowskiPolarSum → ProjectionBody → CentroidBody → SteinerSymmetrization → ProjectionBody → IntersectionBody → PolarDual → IntersectionBody → SteinerSymmetrization → VolumeNormalization → ConvexFixedPointQuery`

### 多項式変換と算術観測（ReciprocalPolynomial・RootMultiset・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.6d687aa33b`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を逆数へ移す相反多項式をとる，(2) 重複度付き根配置へ移す，(3) 根配置からモニック多項式を再構成する，(4) 根を二乗するGraeffe変換を施す，(5) 根を逆数へ移す相反多項式をとる，(6) 臨界値を根にもつ消去多項式を作る，(7) 根の重心を0へ移す平行移動共役を施す，(8) 重複度付き根配置へ移す，(9) 根配置からモニック多項式を再構成する，(10) 臨界値を根にもつ消去多項式を作る，(11) 導関数をモニックに再正規化する，(12) 根の重心を0へ移す平行移動共役を施す，(13) 臨界値を根にもつ消去多項式を作る，(14) 重複度付き根配置へ移す，(15) 根の冪和モーメント列を作る，(16) モーメントからHankel行列族を作る，(17) 主小行列式列をとる，(18) 満たす最小線形漸化式を抽出する，(19) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → GraeffeTransform → ReciprocalPolynomial → CriticalValuePolynomial → ShiftConjugacy → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → DerivativeRenormalization → ShiftConjugacy → CriticalValuePolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 平面代数曲線の合成変換（ProjectiveClosure・AffineChartChange・Catacaustic・IsogonalCremona）

- ID: `research.autonomous.plane_curve.d14aa6995d`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `birational_periodicity`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 射影閉包をとり無限遠点を加える，(2) 基点を避ける一般アフィンチャートへ移す，(3) 正則接線族の射影双対曲線をとる，(4) 固定光源からの反射光線族の包絡線をとる，(5) 法線族の包絡線である発展曲線をとる，(6) 定義多項式のHessian曲線をとる，(7) 固定光源からの反射光線族の包絡線をとる，(8) 法線族の包絡線である発展曲線をとる，(9) 固定非退化二次形式に関する極逆像をとる，(10) 原点中心の円反転像をとる，(11) 正則接線族の射影双対曲線をとる，(12) 原点中心の円反転像をとる，(13) 固定基準三角形に関する等角共役Cremona像をとる，(14) 法線方向の代数的平行曲線をとる，(15) 正則接線族の射影双対曲線をとる，(16) 固定光源からの反射光線族の包絡線をとる，(17) 固定基準三角形に関する等角共役Cremona像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectiveClosure → AffineChartChange → ProjectiveDual → Catacaustic → Evolute → HessianCurve → Catacaustic → Evolute → PolarReciprocal → CircleInversion → ProjectiveDual → CircleInversion → IsogonalCremona → OffsetCurve → ProjectiveDual → Catacaustic → IsogonalCremona → BirationalPeriodQuery`

### Markov関手と到達時刻不変量（ProductChain・LazyPerturbation・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.b05453ab74`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `23`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身との同期積連鎖を作る，(2) 恒等遷移との凸結合でlazy化する，(3) 自己同型軌道に沿って強 lumping する，(4) 正の固有関数によるDoob変換を施す，(5) 自身との同期積連鎖を作る，(6) 正の固有関数によるDoob変換を施す，(7) 自身との同期積連鎖を作る，(8) 定常分布に関する時間反転をとる，(9) 自己同型軌道に沿って強 lumping する，(10) 定常分布に関する時間反転をとる，(11) 正の固有関数によるDoob変換を施す，(12) 定常分布に関する時間反転をとる，(13) 自己同型軌道に沿って強 lumping する，(14) 恒等遷移との凸結合でlazy化する，(15) 指定集合で吸収させ過渡核をとる，(16) 過渡核のGreen作用素をとる，(17) 到達時刻の高次モーメント連立系を作る，(18) モーメント次数方向の漸化式を抽出する，(19) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProductChain → LazyPerturbation → StateLumping → DoobTransform → ProductChain → DoobTransform → ProductChain → TimeReversal → StateLumping → TimeReversal → DoobTransform → TimeReversal → StateLumping → LazyPerturbation → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 三角形変換の合成力学（SymmedianMark・SideReflectionTrace・SimilarityNormalization・ModuliProjection）

- ID: `research.autonomous.triangle_dynamics.80ba832d19`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `triangle_transform_fixed_points`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0625`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 類似重心を標識点として付加する，(2) 標識点を三辺に関して反射した三点をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 垂心を標識点として付加する，(5) 標識点を三辺に関して反射した三点をとる，(6) 三点を頂点とする向き付き三角形を作る，(7) 重心を標識点として付加する，(8) 標識点から三辺への垂足三点をとる，(9) 三点を頂点とする向き付き三角形を作る，(10) 垂足三角形へ移す，(11) 反中点三角形へ移す，(12) 傍心三角形へ移す，(13) 反中点三角形へ移す，(14) 垂足三角形へ移す，(15) 三辺の中点三角形へ移す，(16) 重心・面積・向きを固定して相似正規化する，(17) 相似類のモジュライ点へ射影する。最後に、誘導写像の固定点と有限周期点を相似を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `SymmedianMark → SideReflectionTrace → TriangleFormation → OrthocenterMark → SideReflectionTrace → TriangleFormation → CentroidMark → PedalProjection → TriangleFormation → OrthicTransform → AnticomplementaryTransform → ExcentralTransform → AnticomplementaryTransform → OrthicTransform → MedialTransform → SimilarityNormalization → ModuliProjection → TriangleFixedPointQuery`

### 平面代数曲線の合成変換（OffsetCurve・HessianCurve・ProjectiveDual・PolarReciprocal）

- ID: `research.autonomous.plane_curve.3d66dec7ae`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `birational_periodicity`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 法線方向の代数的平行曲線をとる，(2) 定義多項式のHessian曲線をとる，(3) 法線方向の代数的平行曲線をとる，(4) 定義多項式のHessian曲線をとる，(5) 法線方向の代数的平行曲線をとる，(6) 原点中心の円反転像をとる，(7) 射影閉包をとり無限遠点を加える，(8) 基点を避ける一般アフィンチャートへ移す，(9) 正則接線族の射影双対曲線をとる，(10) 法線族の包絡線である発展曲線をとる，(11) 固定光源からの反射光線族の包絡線をとる，(12) 射影閉包をとり無限遠点を加える，(13) 基点を避ける一般アフィンチャートへ移す，(14) 正則接線族の射影双対曲線をとる，(15) 固定基準三角形に関する等角共役Cremona像をとる，(16) 正則接線族の射影双対曲線をとる，(17) 固定非退化二次形式に関する極逆像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `OffsetCurve → HessianCurve → OffsetCurve → HessianCurve → OffsetCurve → CircleInversion → ProjectiveClosure → AffineChartChange → ProjectiveDual → Evolute → Catacaustic → ProjectiveClosure → AffineChartChange → ProjectiveDual → IsogonalCremona → ProjectiveDual → PolarReciprocal → BirationalPeriodQuery`

### 凸体関手の合成力学（SteinerSymmetrization・PolarDual・IntersectionBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.26b3e403da`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `22`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 主慣性軸方向にSteiner対称化する，(2) 原点に関する極体をとる，(3) 自身と極体のMinkowski和をとる，(4) 主慣性軸方向にSteiner対称化する，(5) 原点に関する極体をとる，(6) 主慣性軸方向にSteiner対称化する，(7) 重心体をとる，(8) 自身と極体のMinkowski和をとる，(9) 射影体をとる，(10) 原点に関する極体をとる，(11) 重心体をとる，(12) 射影体をとる，(13) 交叉体をとる，(14) 自身と極体のMinkowski和をとる，(15) 交叉体をとる，(16) 射影体をとる，(17) 重心体をとる，(18) 交叉体をとる，(19) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `SteinerSymmetrization → PolarDual → MinkowskiPolarSum → SteinerSymmetrization → PolarDual → SteinerSymmetrization → CentroidBody → MinkowskiPolarSum → ProjectionBody → PolarDual → CentroidBody → ProjectionBody → IntersectionBody → MinkowskiPolarSum → IntersectionBody → ProjectionBody → CentroidBody → IntersectionBody → VolumeNormalization → ConvexFixedPointQuery`

### 多項式変換と算術観測（GraeffeTransform・RootMultiset・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.9e5d169104`
- 状態: `unresolved_by_mathos`
- 射数: `17`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を二乗するGraeffe変換を施す，(2) 重複度付き根配置へ移す，(3) 根配置からモニック多項式を再構成する，(4) 導関数をモニックに再正規化する，(5) 根を二乗するGraeffe変換を施す，(6) 根を逆数へ移す相反多項式をとる，(7) 根の重心を0へ移す平行移動共役を施す，(8) 導関数をモニックに再正規化する，(9) 根の重心を0へ移す平行移動共役を施す，(10) 臨界値を根にもつ消去多項式を作る，(11) 重複度付き根配置へ移す，(12) 根の冪和モーメント列を作る，(13) モーメントからHankel行列族を作る，(14) 主小行列式列をとる，(15) 満たす最小線形漸化式を抽出する，(16) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `GraeffeTransform → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → GraeffeTransform → ReciprocalPolynomial → ShiftConjugacy → DerivativeRenormalization → ShiftConjugacy → CriticalValuePolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### Markov関手と到達時刻不変量（LazyPerturbation・ProductChain・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.f389dc171a`
- 状態: `unresolved_by_mathos`
- 射数: `19`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `22`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 恒等遷移との凸結合でlazy化する，(2) 自身との同期積連鎖を作る，(3) 自己同型軌道に沿って強 lumping する，(4) 正の固有関数によるDoob変換を施す，(5) 恒等遷移との凸結合でlazy化する，(6) 正の固有関数によるDoob変換を施す，(7) 定常分布に関する時間反転をとる，(8) 自身との同期積連鎖を作る，(9) 正の固有関数によるDoob変換を施す，(10) 自己同型軌道に沿って強 lumping する，(11) 自身との同期積連鎖を作る，(12) 自己同型軌道に沿って強 lumping する，(13) 恒等遷移との凸結合でlazy化する，(14) 定常分布に関する時間反転をとる，(15) 指定集合で吸収させ過渡核をとる，(16) 過渡核のGreen作用素をとる，(17) 到達時刻の高次モーメント連立系を作る，(18) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `LazyPerturbation → ProductChain → StateLumping → DoobTransform → LazyPerturbation → DoobTransform → TimeReversal → ProductChain → DoobTransform → StateLumping → ProductChain → StateLumping → LazyPerturbation → TimeReversal → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 三角形変換の合成力学（IncenterMark・PedalProjection・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.37331f5c31`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 内心を標識点として付加する，(2) 標識点から三辺への垂足三点をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 傍心三角形へ移す，(5) 反中点三角形へ移す，(6) 重心を標識点として付加する，(7) 標識点を通る三本のcevianの辺上の足をとる，(8) 三点を頂点とする向き付き三角形を作る，(9) 外心を標識点として付加する，(10) 標識点から三辺への垂足三点をとる，(11) 三点を頂点とする向き付き三角形を作る，(12) 反中点三角形へ移す，(13) 傍心三角形へ移す，(14) 三辺の中点三角形へ移す，(15) 重心・面積・向きを固定して相似正規化する，(16) 相似類のモジュライ点へ射影する，(17) ここまでの合成が誘導する写像を反復する，(18) 退化三角形を境界として軌道をコンパクト化する，(19) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IncenterMark → PedalProjection → TriangleFormation → ExcentralTransform → AnticomplementaryTransform → CentroidMark → CevianTrace → TriangleFormation → CircumcenterMark → PedalProjection → TriangleFormation → AnticomplementaryTransform → ExcentralTransform → MedialTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 三角形変換の合成力学（SymmedianMark・SideReflectionTrace・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.9fbe704f45`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `22`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 類似重心を標識点として付加する，(2) 標識点を三辺に関して反射した三点をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 三辺の中点三角形へ移す，(5) 重心を標識点として付加する，(6) 標識点から三辺への垂足三点をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 三辺の中点三角形へ移す，(9) 垂心を標識点として付加する，(10) 標識点から三辺への垂足三点をとる，(11) 三点を頂点とする向き付き三角形を作る，(12) 反中点三角形へ移す，(13) 重心・面積・向きを固定して相似正規化する，(14) 相似類のモジュライ点へ射影する，(15) ここまでの合成が誘導する写像を反復する，(16) 退化三角形を境界として軌道をコンパクト化する，(17) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `SymmedianMark → SideReflectionTrace → TriangleFormation → MedialTransform → CentroidMark → PedalProjection → TriangleFormation → MedialTransform → OrthocenterMark → PedalProjection → TriangleFormation → AnticomplementaryTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### Markov関手と到達時刻不変量（DoobTransform・TimeReversal・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.28c610269b`
- 状態: `unresolved_by_mathos`
- 射数: `19`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `22`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 正の固有関数によるDoob変換を施す，(2) 定常分布に関する時間反転をとる，(3) 自己同型軌道に沿って強 lumping する，(4) 正の固有関数によるDoob変換を施す，(5) 自身との同期積連鎖を作る，(6) 定常分布に関する時間反転をとる，(7) 恒等遷移との凸結合でlazy化する，(8) 正の固有関数によるDoob変換を施す，(9) 定常分布に関する時間反転をとる，(10) 自身との同期積連鎖を作る，(11) 恒等遷移との凸結合でlazy化する，(12) 自身との同期積連鎖を作る，(13) 自己同型軌道に沿って強 lumping する，(14) 恒等遷移との凸結合でlazy化する，(15) 指定集合で吸収させ過渡核をとる，(16) 過渡核のGreen作用素をとる，(17) 到達時刻の高次モーメント連立系を作る，(18) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DoobTransform → TimeReversal → StateLumping → DoobTransform → ProductChain → TimeReversal → LazyPerturbation → DoobTransform → TimeReversal → ProductChain → LazyPerturbation → ProductChain → StateLumping → LazyPerturbation → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 平面代数曲線の合成変換（OffsetCurve・HessianCurve・IsogonalCremona・PolarReciprocal）

- ID: `research.autonomous.plane_curve.7f1096a46d`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `birational_periodicity`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 法線方向の代数的平行曲線をとる，(2) 定義多項式のHessian曲線をとる，(3) 固定非退化二次形式に関する極逆像をとる，(4) 法線方向の代数的平行曲線をとる，(5) 固定光源からの反射光線族の包絡線をとる，(6) 射影閉包をとり無限遠点を加える，(7) 基点を避ける一般アフィンチャートへ移す，(8) 定義多項式のHessian曲線をとる，(9) 法線族の包絡線である発展曲線をとる，(10) 固定光源からの反射光線族の包絡線をとる，(11) 固定非退化二次形式に関する極逆像をとる，(12) 原点中心の円反転像をとる，(13) 正則接線族の射影双対曲線をとる，(14) 原点中心の円反転像をとる，(15) 固定光源からの反射光線族の包絡線をとる，(16) 固定基準三角形に関する等角共役Cremona像をとる，(17) 固定非退化二次形式に関する極逆像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `OffsetCurve → HessianCurve → PolarReciprocal → OffsetCurve → Catacaustic → ProjectiveClosure → AffineChartChange → HessianCurve → Evolute → Catacaustic → PolarReciprocal → CircleInversion → ProjectiveDual → CircleInversion → Catacaustic → IsogonalCremona → PolarReciprocal → BirationalPeriodQuery`

### 凸体関手の合成力学（DifferenceBody・ProjectionBody・CentroidBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.c0bcddf37c`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 差体をとる，(2) 射影体をとる，(3) 交叉体をとる，(4) 差体をとる，(5) 主慣性軸方向にSteiner対称化する，(6) 自身と極体のMinkowski和をとる，(7) 主慣性軸方向にSteiner対称化する，(8) 差体をとる，(9) 重心体をとる，(10) 交叉体をとる，(11) 自身と極体のMinkowski和をとる，(12) 重心体をとる，(13) 自身と極体のMinkowski和をとる，(14) 主慣性軸方向にSteiner対称化する，(15) 原点に関する極体をとる，(16) 射影体をとる，(17) 交叉体をとる，(18) 射影体をとる，(19) 重心体をとる，(20) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DifferenceBody → ProjectionBody → IntersectionBody → DifferenceBody → SteinerSymmetrization → MinkowskiPolarSum → SteinerSymmetrization → DifferenceBody → CentroidBody → IntersectionBody → MinkowskiPolarSum → CentroidBody → MinkowskiPolarSum → SteinerSymmetrization → PolarDual → ProjectionBody → IntersectionBody → ProjectionBody → CentroidBody → VolumeNormalization → ConvexFixedPointQuery`

### 多項式変換と算術観測（DerivativeRenormalization・ReciprocalPolynomial・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.e33b2eab46`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `recurrence_order_drop`
- 難度仮説: `22`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 導関数をモニックに再正規化する，(2) 根を逆数へ移す相反多項式をとる，(3) 導関数をモニックに再正規化する，(4) 臨界値を根にもつ消去多項式を作る，(5) 根を二乗するGraeffe変換を施す，(6) 根を逆数へ移す相反多項式をとる，(7) 根の重心を0へ移す平行移動共役を施す，(8) 根を逆数へ移す相反多項式をとる，(9) 導関数をモニックに再正規化する，(10) 臨界値を根にもつ消去多項式を作る，(11) 重複度付き根配置へ移す，(12) 根配置からモニック多項式を再構成する，(13) 重複度付き根配置へ移す，(14) 根の冪和モーメント列を作る，(15) モーメントからHankel行列族を作る，(16) 主小行列式列をとる，(17) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DerivativeRenormalization → ReciprocalPolynomial → DerivativeRenormalization → CriticalValuePolynomial → GraeffeTransform → ReciprocalPolynomial → ShiftConjugacy → ReciprocalPolynomial → DerivativeRenormalization → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### Markov関手と到達時刻不変量（DoobTransform・LazyPerturbation・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.4b078d19f1`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 正の固有関数によるDoob変換を施す，(2) 恒等遷移との凸結合でlazy化する，(3) 定常分布に関する時間反転をとる，(4) 恒等遷移との凸結合でlazy化する，(5) 定常分布に関する時間反転をとる，(6) 自己同型軌道に沿って強 lumping する，(7) 恒等遷移との凸結合でlazy化する，(8) 定常分布に関する時間反転をとる，(9) 自己同型軌道に沿って強 lumping する，(10) 正の固有関数によるDoob変換を施す，(11) 自身との同期積連鎖を作る，(12) 正の固有関数によるDoob変換を施す，(13) 自身との同期積連鎖を作る，(14) 自己同型軌道に沿って強 lumping する，(15) 自身との同期積連鎖を作る，(16) 指定集合で吸収させ過渡核をとる，(17) 過渡核のGreen作用素をとる，(18) 到達時刻の高次モーメント連立系を作る，(19) モーメント次数方向の漸化式を抽出する，(20) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DoobTransform → LazyPerturbation → TimeReversal → LazyPerturbation → TimeReversal → StateLumping → LazyPerturbation → TimeReversal → StateLumping → DoobTransform → ProductChain → DoobTransform → ProductChain → StateLumping → ProductChain → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 凸体関手の合成力学（IntersectionBody・DifferenceBody・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.58cd19c778`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `convex_body_dynamics`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 交叉体をとる，(2) 差体をとる，(3) 重心体をとる，(4) 原点に関する極体をとる，(5) 自身と極体のMinkowski和をとる，(6) 交叉体をとる，(7) 差体をとる，(8) 主慣性軸方向にSteiner対称化する，(9) 自身と極体のMinkowski和をとる，(10) 交叉体をとる，(11) 自身と極体のMinkowski和をとる，(12) 原点に関する極体をとる，(13) 差体をとる，(14) 射影体をとる，(15) 重心体をとる，(16) 射影体をとる，(17) 面積と二次モーメントを固定して正規化する，(18) ここまでの凸体関手を反復する，(19) 支持関数の軌道へ移す，(20) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IntersectionBody → DifferenceBody → CentroidBody → PolarDual → MinkowskiPolarSum → IntersectionBody → DifferenceBody → SteinerSymmetrization → MinkowskiPolarSum → IntersectionBody → MinkowskiPolarSum → PolarDual → DifferenceBody → ProjectionBody → CentroidBody → ProjectionBody → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 多項式変換と算術観測（RootMultiset・PolynomialReconstruction・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.194f410630`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `recurrence_order_drop`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重複度付き根配置へ移す，(2) 根配置からモニック多項式を再構成する，(3) 導関数をモニックに再正規化する，(4) 重複度付き根配置へ移す，(5) 根配置からモニック多項式を再構成する，(6) 根の重心を0へ移す平行移動共役を施す，(7) 臨界値を根にもつ消去多項式を作る，(8) 導関数をモニックに再正規化する，(9) 根を二乗するGraeffe変換を施す，(10) 根の重心を0へ移す平行移動共役を施す，(11) 導関数をモニックに再正規化する，(12) 根を逆数へ移す相反多項式をとる，(13) 根を二乗するGraeffe変換を施す，(14) 臨界値を根にもつ消去多項式を作る，(15) 重複度付き根配置へ移す，(16) 根の冪和モーメント列を作る，(17) モーメントからHankel行列族を作る，(18) 主小行列式列をとる，(19) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `RootMultiset → PolynomialReconstruction → DerivativeRenormalization → RootMultiset → PolynomialReconstruction → ShiftConjugacy → CriticalValuePolynomial → DerivativeRenormalization → GraeffeTransform → ShiftConjugacy → DerivativeRenormalization → ReciprocalPolynomial → GraeffeTransform → CriticalValuePolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 三角形変換の合成力学（IncenterMark・CevianTrace・SimilarityNormalization・ModuliProjection）

- ID: `research.autonomous.triangle_dynamics.f84c8d3162`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `triangle_transform_fixed_points`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 内心を標識点として付加する，(2) 標識点を通る三本のcevianの辺上の足をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 外心を標識点として付加する，(5) 標識点を三辺に関して反射した三点をとる，(6) 三点を頂点とする向き付き三角形を作る，(7) 垂心を標識点として付加する，(8) 標識点を通る三本のcevianの辺上の足をとる，(9) 三点を頂点とする向き付き三角形を作る，(10) 垂足三角形へ移す，(11) 三辺の中点三角形へ移す，(12) 傍心三角形へ移す，(13) 反中点三角形へ移す，(14) 垂足三角形へ移す，(15) 反中点三角形へ移す，(16) 重心・面積・向きを固定して相似正規化する，(17) 相似類のモジュライ点へ射影する。最後に、誘導写像の固定点と有限周期点を相似を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IncenterMark → CevianTrace → TriangleFormation → CircumcenterMark → SideReflectionTrace → TriangleFormation → OrthocenterMark → CevianTrace → TriangleFormation → OrthicTransform → MedialTransform → ExcentralTransform → AnticomplementaryTransform → OrthicTransform → AnticomplementaryTransform → SimilarityNormalization → ModuliProjection → TriangleFixedPointQuery`

### 平面代数曲線の合成変換（HessianCurve・Catacaustic・ResolveSingularities・CurveInvariantExtraction）

- ID: `research.autonomous.plane_curve.fe5b04aa98`
- 状態: `unresolved_by_mathos`
- 射数: `19`
- 問い: `degree_genus_formula`
- 難度仮説: `23`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 定義多項式のHessian曲線をとる，(2) 固定光源からの反射光線族の包絡線をとる，(3) 法線族の包絡線である発展曲線をとる，(4) 固定基準三角形に関する等角共役Cremona像をとる，(5) 固定非退化二次形式に関する極逆像をとる，(6) 法線方向の代数的平行曲線をとる，(7) 固定基準三角形に関する等角共役Cremona像をとる，(8) 射影閉包をとり無限遠点を加える，(9) 基点を避ける一般アフィンチャートへ移す，(10) 定義多項式のHessian曲線をとる，(11) 正則接線族の射影双対曲線をとる，(12) 固定基準三角形に関する等角共役Cremona像をとる，(13) 射影閉包をとり無限遠点を加える，(14) 基点を避ける一般アフィンチャートへ移す，(15) 原点中心の円反転像をとる，(16) 射影閉包をとり無限遠点を加える，(17) 全特異点を解消して正規化曲線を得る，(18) 次数、分岐、種数、自己交点データを抽出する。最後に、次数と幾何種数を初期曲線の不変量で表示し例外を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `HessianCurve → Catacaustic → Evolute → IsogonalCremona → PolarReciprocal → OffsetCurve → IsogonalCremona → ProjectiveClosure → AffineChartChange → HessianCurve → ProjectiveDual → IsogonalCremona → ProjectiveClosure → AffineChartChange → CircleInversion → ProjectiveClosure → ResolveSingularities → CurveInvariantExtraction → DegreeGenusQuery`

### 多項式変換と算術観測（ShiftConjugacy・CriticalValuePolynomial・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.34b079a99b`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `recurrence_order_drop`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根の重心を0へ移す平行移動共役を施す，(2) 臨界値を根にもつ消去多項式を作る，(3) 根の重心を0へ移す平行移動共役を施す，(4) 根を逆数へ移す相反多項式をとる，(5) 重複度付き根配置へ移す，(6) 根配置からモニック多項式を再構成する，(7) 根を逆数へ移す相反多項式をとる，(8) 重複度付き根配置へ移す，(9) 根配置からモニック多項式を再構成する，(10) 臨界値を根にもつ消去多項式を作る，(11) 根を逆数へ移す相反多項式をとる，(12) 臨界値を根にもつ消去多項式を作る，(13) 根を二乗するGraeffe変換を施す，(14) 根の重心を0へ移す平行移動共役を施す，(15) 導関数をモニックに再正規化する，(16) 重複度付き根配置へ移す，(17) 根の冪和モーメント列を作る，(18) モーメントからHankel行列族を作る，(19) 主小行列式列をとる，(20) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ShiftConjugacy → CriticalValuePolynomial → ShiftConjugacy → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → ReciprocalPolynomial → CriticalValuePolynomial → GraeffeTransform → ShiftConjugacy → DerivativeRenormalization → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 平面代数曲線の合成変換（ProjectiveDual・OffsetCurve・HessianCurve・ProjectiveDual）

- ID: `research.autonomous.plane_curve.1c92a4175f`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `birational_periodicity`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 正則接線族の射影双対曲線をとる，(2) 法線方向の代数的平行曲線をとる，(3) 定義多項式のHessian曲線をとる，(4) 法線方向の代数的平行曲線をとる，(5) 固定光源からの反射光線族の包絡線をとる，(6) 原点中心の円反転像をとる，(7) 固定基準三角形に関する等角共役Cremona像をとる，(8) 射影閉包をとり無限遠点を加える，(9) 基点を避ける一般アフィンチャートへ移す，(10) 固定非退化二次形式に関する極逆像をとる，(11) 法線族の包絡線である発展曲線をとる，(12) 射影閉包をとり無限遠点を加える，(13) 基点を避ける一般アフィンチャートへ移す，(14) 原点中心の円反転像をとる，(15) 射影閉包をとり無限遠点を加える，(16) 基点を避ける一般アフィンチャートへ移す，(17) 固定光源からの反射光線族の包絡線をとる，(18) 法線族の包絡線である発展曲線をとる，(19) 定義多項式のHessian曲線をとる，(20) 正則接線族の射影双対曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectiveDual → OffsetCurve → HessianCurve → OffsetCurve → Catacaustic → CircleInversion → IsogonalCremona → ProjectiveClosure → AffineChartChange → PolarReciprocal → Evolute → ProjectiveClosure → AffineChartChange → CircleInversion → ProjectiveClosure → AffineChartChange → Catacaustic → Evolute → HessianCurve → ProjectiveDual → BirationalPeriodQuery`

### Markov関手と到達時刻不変量（DoobTransform・StateLumping・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.5da32eaf6a`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 正の固有関数によるDoob変換を施す，(2) 自己同型軌道に沿って強 lumping する，(3) 定常分布に関する時間反転をとる，(4) 恒等遷移との凸結合でlazy化する，(5) 正の固有関数によるDoob変換を施す，(6) 自身との同期積連鎖を作る，(7) 正の固有関数によるDoob変換を施す，(8) 自己同型軌道に沿って強 lumping する，(9) 恒等遷移との凸結合でlazy化する，(10) 自己同型軌道に沿って強 lumping する，(11) 恒等遷移との凸結合でlazy化する，(12) 定常分布に関する時間反転をとる，(13) 指定集合で吸収させ過渡核をとる，(14) 過渡核のGreen作用素をとる，(15) 到達時刻の高次モーメント連立系を作る，(16) モーメント次数方向の漸化式を抽出する，(17) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DoobTransform → StateLumping → TimeReversal → LazyPerturbation → DoobTransform → ProductChain → DoobTransform → StateLumping → LazyPerturbation → StateLumping → LazyPerturbation → TimeReversal → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 三角形変換の合成力学（ExcentralTransform・AnticomplementaryTransform・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.267e15069f`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 傍心三角形へ移す，(2) 反中点三角形へ移す，(3) 傍心三角形へ移す，(4) 類似重心を標識点として付加する，(5) 各頂点と標識点が定める円の対応交点をとる，(6) 三点を頂点とする向き付き三角形を作る，(7) 類似重心を標識点として付加する，(8) 標識点から三辺への垂足三点をとる，(9) 三点を頂点とする向き付き三角形を作る，(10) 垂足三角形へ移す，(11) 反中点三角形へ移す，(12) 類似重心を標識点として付加する，(13) 標識点を三辺に関して反射した三点をとる，(14) 三点を頂点とする向き付き三角形を作る，(15) 重心・面積・向きを固定して相似正規化する，(16) 相似類のモジュライ点へ射影する，(17) ここまでの合成が誘導する写像を反復する，(18) 退化三角形を境界として軌道をコンパクト化する，(19) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ExcentralTransform → AnticomplementaryTransform → ExcentralTransform → SymmedianMark → VertexCircleTrace → TriangleFormation → SymmedianMark → PedalProjection → TriangleFormation → OrthicTransform → AnticomplementaryTransform → SymmedianMark → SideReflectionTrace → TriangleFormation → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 凸体関手の合成力学（MinkowskiPolarSum・IntersectionBody・SteinerSymmetrization・VolumeNormalization）

- ID: `research.autonomous.convex_body.4826ac412f`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身と極体のMinkowski和をとる，(2) 交叉体をとる，(3) 重心体をとる，(4) 自身と極体のMinkowski和をとる，(5) 原点に関する極体をとる，(6) 射影体をとる，(7) 原点に関する極体をとる，(8) 射影体をとる，(9) 差体をとる，(10) 原点に関する極体をとる，(11) 差体をとる，(12) 主慣性軸方向にSteiner対称化する，(13) 交叉体をとる，(14) 差体をとる，(15) 射影体をとる，(16) 交叉体をとる，(17) 重心体をとる，(18) 自身と極体のMinkowski和をとる，(19) 主慣性軸方向にSteiner対称化する，(20) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `MinkowskiPolarSum → IntersectionBody → CentroidBody → MinkowskiPolarSum → PolarDual → ProjectionBody → PolarDual → ProjectionBody → DifferenceBody → PolarDual → DifferenceBody → SteinerSymmetrization → IntersectionBody → DifferenceBody → ProjectionBody → IntersectionBody → CentroidBody → MinkowskiPolarSum → SteinerSymmetrization → VolumeNormalization → ConvexFixedPointQuery`

### 多項式変換と算術観測（CriticalValuePolynomial・ShiftConjugacy・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.aba715f128`
- 状態: `unresolved_by_mathos`
- 射数: `19`
- 問い: `recurrence_order_drop`
- 難度仮説: `23`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 臨界値を根にもつ消去多項式を作る，(2) 根の重心を0へ移す平行移動共役を施す，(3) 重複度付き根配置へ移す，(4) 根配置からモニック多項式を再構成する，(5) 根を逆数へ移す相反多項式をとる，(6) 臨界値を根にもつ消去多項式を作る，(7) 根を逆数へ移す相反多項式をとる，(8) 根を二乗するGraeffe変換を施す，(9) 臨界値を根にもつ消去多項式を作る，(10) 導関数をモニックに再正規化する，(11) 根の重心を0へ移す平行移動共役を施す，(12) 重複度付き根配置へ移す，(13) 根配置からモニック多項式を再構成する，(14) 重複度付き根配置へ移す，(15) 根の冪和モーメント列を作る，(16) モーメントからHankel行列族を作る，(17) 主小行列式列をとる，(18) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CriticalValuePolynomial → ShiftConjugacy → RootMultiset → PolynomialReconstruction → ReciprocalPolynomial → CriticalValuePolynomial → ReciprocalPolynomial → GraeffeTransform → CriticalValuePolynomial → DerivativeRenormalization → ShiftConjugacy → RootMultiset → PolynomialReconstruction → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 凸体関手の合成力学（MinkowskiPolarSum・PolarDual・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.5ef705e437`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `convex_body_dynamics`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身と極体のMinkowski和をとる，(2) 原点に関する極体をとる，(3) 主慣性軸方向にSteiner対称化する，(4) 差体をとる，(5) 主慣性軸方向にSteiner対称化する，(6) 射影体をとる，(7) 交叉体をとる，(8) 重心体をとる，(9) 交叉体をとる，(10) 差体をとる，(11) 自身と極体のMinkowski和をとる，(12) 交叉体をとる，(13) 重心体をとる，(14) 差体をとる，(15) 射影体をとる，(16) 面積と二次モーメントを固定して正規化する，(17) ここまでの凸体関手を反復する，(18) 支持関数の軌道へ移す，(19) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `MinkowskiPolarSum → PolarDual → SteinerSymmetrization → DifferenceBody → SteinerSymmetrization → ProjectionBody → IntersectionBody → CentroidBody → IntersectionBody → DifferenceBody → MinkowskiPolarSum → IntersectionBody → CentroidBody → DifferenceBody → ProjectionBody → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 平面代数曲線の合成変換（Catacaustic・Evolute・ProjectiveDual・CircleInversion）

- ID: `research.autonomous.plane_curve.7dfcda3b44`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `birational_periodicity`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定光源からの反射光線族の包絡線をとる，(2) 法線族の包絡線である発展曲線をとる，(3) 固定非退化二次形式に関する極逆像をとる，(4) 射影閉包をとり無限遠点を加える，(5) 基点を避ける一般アフィンチャートへ移す，(6) 法線族の包絡線である発展曲線をとる，(7) 射影閉包をとり無限遠点を加える，(8) 基点を避ける一般アフィンチャートへ移す，(9) 原点中心の円反転像をとる，(10) 固定非退化二次形式に関する極逆像をとる，(11) 原点中心の円反転像をとる，(12) 法線族の包絡線である発展曲線をとる，(13) 固定非退化二次形式に関する極逆像をとる，(14) 固定基準三角形に関する等角共役Cremona像をとる，(15) 法線方向の代数的平行曲線をとる，(16) 射影閉包をとり無限遠点を加える，(17) 基点を避ける一般アフィンチャートへ移す，(18) 法線方向の代数的平行曲線をとる，(19) 正則接線族の射影双対曲線をとる，(20) 原点中心の円反転像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `Catacaustic → Evolute → PolarReciprocal → ProjectiveClosure → AffineChartChange → Evolute → ProjectiveClosure → AffineChartChange → CircleInversion → PolarReciprocal → CircleInversion → Evolute → PolarReciprocal → IsogonalCremona → OffsetCurve → ProjectiveClosure → AffineChartChange → OffsetCurve → ProjectiveDual → CircleInversion → BirationalPeriodQuery`

### 三角形変換の合成力学（CentroidMark・CevianTrace・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.eb1996366b`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `26`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重心を標識点として付加する，(2) 標識点を通る三本のcevianの辺上の足をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 類似重心を標識点として付加する，(5) 標識点から三辺への垂足三点をとる，(6) 三点を頂点とする向き付き三角形を作る，(7) 垂心を標識点として付加する，(8) 各頂点と標識点が定める円の対応交点をとる，(9) 三点を頂点とする向き付き三角形を作る，(10) 傍心三角形へ移す，(11) 三辺の中点三角形へ移す，(12) 垂足三角形へ移す，(13) 反中点三角形へ移す，(14) 垂足三角形へ移す，(15) 三辺の中点三角形へ移す，(16) 重心・面積・向きを固定して相似正規化する，(17) 相似類のモジュライ点へ射影する，(18) ここまでの合成が誘導する写像を反復する，(19) 退化三角形を境界として軌道をコンパクト化する，(20) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CentroidMark → CevianTrace → TriangleFormation → SymmedianMark → PedalProjection → TriangleFormation → OrthocenterMark → VertexCircleTrace → TriangleFormation → ExcentralTransform → MedialTransform → OrthicTransform → AnticomplementaryTransform → OrthicTransform → MedialTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### Markov関手と到達時刻不変量（ProductChain・StateLumping・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.e5e7cb602f`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `23`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身との同期積連鎖を作る，(2) 自己同型軌道に沿って強 lumping する，(3) 自身との同期積連鎖を作る，(4) 自己同型軌道に沿って強 lumping する，(5) 正の固有関数によるDoob変換を施す，(6) 自己同型軌道に沿って強 lumping する，(7) 正の固有関数によるDoob変換を施す，(8) 自身との同期積連鎖を作る，(9) 定常分布に関する時間反転をとる，(10) 正の固有関数によるDoob変換を施す，(11) 定常分布に関する時間反転をとる，(12) 恒等遷移との凸結合でlazy化する，(13) 定常分布に関する時間反転をとる，(14) 恒等遷移との凸結合でlazy化する，(15) 指定集合で吸収させ過渡核をとる，(16) 過渡核のGreen作用素をとる，(17) 到達時刻の高次モーメント連立系を作る，(18) モーメント次数方向の漸化式を抽出する，(19) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProductChain → StateLumping → ProductChain → StateLumping → DoobTransform → StateLumping → DoobTransform → ProductChain → TimeReversal → DoobTransform → TimeReversal → LazyPerturbation → TimeReversal → LazyPerturbation → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 多項式変換と算術観測（RootMultiset・PolynomialReconstruction・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.0df696dc2e`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重複度付き根配置へ移す，(2) 根配置からモニック多項式を再構成する，(3) 重複度付き根配置へ移す，(4) 根配置からモニック多項式を再構成する，(5) 根を二乗するGraeffe変換を施す，(6) 臨界値を根にもつ消去多項式を作る，(7) 根の重心を0へ移す平行移動共役を施す，(8) 根を逆数へ移す相反多項式をとる，(9) 根を二乗するGraeffe変換を施す，(10) 臨界値を根にもつ消去多項式を作る，(11) 根を逆数へ移す相反多項式をとる，(12) 根の重心を0へ移す平行移動共役を施す，(13) 臨界値を根にもつ消去多項式を作る，(14) 重複度付き根配置へ移す，(15) 根の冪和モーメント列を作る，(16) モーメントからHankel行列族を作る，(17) 主小行列式列をとる，(18) 満たす最小線形漸化式を抽出する，(19) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `RootMultiset → PolynomialReconstruction → RootMultiset → PolynomialReconstruction → GraeffeTransform → CriticalValuePolynomial → ShiftConjugacy → ReciprocalPolynomial → GraeffeTransform → CriticalValuePolynomial → ReciprocalPolynomial → ShiftConjugacy → CriticalValuePolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 三角形変換の合成力学（SymmedianMark・PedalProjection・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.c19536187e`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `22`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 類似重心を標識点として付加する，(2) 標識点から三辺への垂足三点をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 内心を標識点として付加する，(5) 各頂点と標識点が定める円の対応交点をとる，(6) 三点を頂点とする向き付き三角形を作る，(7) 外心を標識点として付加する，(8) 標識点を通る三本のcevianの辺上の足をとる，(9) 三点を頂点とする向き付き三角形を作る，(10) 垂足三角形へ移す，(11) 反中点三角形へ移す，(12) 傍心三角形へ移す，(13) 重心・面積・向きを固定して相似正規化する，(14) 相似類のモジュライ点へ射影する，(15) ここまでの合成が誘導する写像を反復する，(16) 退化三角形を境界として軌道をコンパクト化する，(17) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `SymmedianMark → PedalProjection → TriangleFormation → IncenterMark → VertexCircleTrace → TriangleFormation → CircumcenterMark → CevianTrace → TriangleFormation → OrthicTransform → AnticomplementaryTransform → ExcentralTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 凸体関手の合成力学（SteinerSymmetrization・PolarDual・ProjectionBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.3f42c15de5`
- 状態: `unresolved_by_mathos`
- 射数: `18`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `21`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 主慣性軸方向にSteiner対称化する，(2) 原点に関する極体をとる，(3) 主慣性軸方向にSteiner対称化する，(4) 交叉体をとる，(5) 重心体をとる，(6) 自身と極体のMinkowski和をとる，(7) 重心体をとる，(8) 自身と極体のMinkowski和をとる，(9) 重心体をとる，(10) 自身と極体のMinkowski和をとる，(11) 交叉体をとる，(12) 差体をとる，(13) 原点に関する極体をとる，(14) 射影体をとる，(15) 差体をとる，(16) 射影体をとる，(17) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `SteinerSymmetrization → PolarDual → SteinerSymmetrization → IntersectionBody → CentroidBody → MinkowskiPolarSum → CentroidBody → MinkowskiPolarSum → CentroidBody → MinkowskiPolarSum → IntersectionBody → DifferenceBody → PolarDual → ProjectionBody → DifferenceBody → ProjectionBody → VolumeNormalization → ConvexFixedPointQuery`

### 平面代数曲線の合成変換（CircleInversion・Evolute・HessianCurve・Evolute）

- ID: `research.autonomous.plane_curve.d3e947e81b`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `birational_periodicity`
- 難度仮説: `23`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 原点中心の円反転像をとる，(2) 法線族の包絡線である発展曲線をとる，(3) 固定光源からの反射光線族の包絡線をとる，(4) 法線方向の代数的平行曲線をとる，(5) 原点中心の円反転像をとる，(6) 固定光源からの反射光線族の包絡線をとる，(7) 法線方向の代数的平行曲線をとる，(8) 法線族の包絡線である発展曲線をとる，(9) 原点中心の円反転像をとる，(10) 固定光源からの反射光線族の包絡線をとる，(11) 固定非退化二次形式に関する極逆像をとる，(12) 正則接線族の射影双対曲線をとる，(13) 固定基準三角形に関する等角共役Cremona像をとる，(14) 固定非退化二次形式に関する極逆像をとる，(15) 定義多項式のHessian曲線をとる，(16) 固定非退化二次形式に関する極逆像をとる，(17) 法線方向の代数的平行曲線をとる，(18) 定義多項式のHessian曲線をとる，(19) 法線族の包絡線である発展曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CircleInversion → Evolute → Catacaustic → OffsetCurve → CircleInversion → Catacaustic → OffsetCurve → Evolute → CircleInversion → Catacaustic → PolarReciprocal → ProjectiveDual → IsogonalCremona → PolarReciprocal → HessianCurve → PolarReciprocal → OffsetCurve → HessianCurve → Evolute → BirationalPeriodQuery`

### Markov関手と到達時刻不変量（StateLumping・LazyPerturbation・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.93719a8b0b`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自己同型軌道に沿って強 lumping する，(2) 恒等遷移との凸結合でlazy化する，(3) 自己同型軌道に沿って強 lumping する，(4) 定常分布に関する時間反転をとる，(5) 自身との同期積連鎖を作る，(6) 恒等遷移との凸結合でlazy化する，(7) 自身との同期積連鎖を作る，(8) 自己同型軌道に沿って強 lumping する，(9) 正の固有関数によるDoob変換を施す，(10) 定常分布に関する時間反転をとる，(11) 自身との同期積連鎖を作る，(12) 正の固有関数によるDoob変換を施す，(13) 恒等遷移との凸結合でlazy化する，(14) 正の固有関数によるDoob変換を施す，(15) 定常分布に関する時間反転をとる，(16) 指定集合で吸収させ過渡核をとる，(17) 過渡核のGreen作用素をとる，(18) 到達時刻の高次モーメント連立系を作る，(19) モーメント次数方向の漸化式を抽出する，(20) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `StateLumping → LazyPerturbation → StateLumping → TimeReversal → ProductChain → LazyPerturbation → ProductChain → StateLumping → DoobTransform → TimeReversal → ProductChain → DoobTransform → LazyPerturbation → DoobTransform → TimeReversal → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 凸体関手の合成力学（CentroidBody・DifferenceBody・MinkowskiPolarSum・VolumeNormalization）

- ID: `research.autonomous.convex_body.cea464c951`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `23`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重心体をとる，(2) 差体をとる，(3) 重心体をとる，(4) 射影体をとる，(5) 差体をとる，(6) 主慣性軸方向にSteiner対称化する，(7) 交叉体をとる，(8) 主慣性軸方向にSteiner対称化する，(9) 原点に関する極体をとる，(10) 差体をとる，(11) 原点に関する極体をとる，(12) 射影体をとる，(13) 主慣性軸方向にSteiner対称化する，(14) 自身と極体のMinkowski和をとる，(15) 原点に関する極体をとる，(16) 交叉体をとる，(17) 射影体をとる，(18) 自身と極体のMinkowski和をとる，(19) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CentroidBody → DifferenceBody → CentroidBody → ProjectionBody → DifferenceBody → SteinerSymmetrization → IntersectionBody → SteinerSymmetrization → PolarDual → DifferenceBody → PolarDual → ProjectionBody → SteinerSymmetrization → MinkowskiPolarSum → PolarDual → IntersectionBody → ProjectionBody → MinkowskiPolarSum → VolumeNormalization → ConvexFixedPointQuery`

### 三角形変換の合成力学（MedialTransform・SymmedianMark・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.2b61b4f56a`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 三辺の中点三角形へ移す，(2) 類似重心を標識点として付加する，(3) 標識点を三辺に関して反射した三点をとる，(4) 三点を頂点とする向き付き三角形を作る，(5) 類似重心を標識点として付加する，(6) 標識点を三辺に関して反射した三点をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 重心を標識点として付加する，(9) 標識点を三辺に関して反射した三点をとる，(10) 三点を頂点とする向き付き三角形を作る，(11) 傍心三角形へ移す，(12) 三辺の中点三角形へ移す，(13) 傍心三角形へ移す，(14) 三辺の中点三角形へ移す，(15) 傍心三角形へ移す，(16) 重心・面積・向きを固定して相似正規化する，(17) 相似類のモジュライ点へ射影する，(18) ここまでの合成が誘導する写像を反復する，(19) 退化三角形を境界として軌道をコンパクト化する，(20) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `MedialTransform → SymmedianMark → SideReflectionTrace → TriangleFormation → SymmedianMark → SideReflectionTrace → TriangleFormation → CentroidMark → SideReflectionTrace → TriangleFormation → ExcentralTransform → MedialTransform → ExcentralTransform → MedialTransform → ExcentralTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 多項式変換と算術観測（DerivativeRenormalization・GraeffeTransform・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.15811a51d3`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `recurrence_order_drop`
- 難度仮説: `23`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 導関数をモニックに再正規化する，(2) 根を二乗するGraeffe変換を施す，(3) 臨界値を根にもつ消去多項式を作る，(4) 重複度付き根配置へ移す，(5) 根配置からモニック多項式を再構成する，(6) 根を逆数へ移す相反多項式をとる，(7) 重複度付き根配置へ移す，(8) 根配置からモニック多項式を再構成する，(9) 導関数をモニックに再正規化する，(10) 臨界値を根にもつ消去多項式を作る，(11) 根を逆数へ移す相反多項式をとる，(12) 臨界値を根にもつ消去多項式を作る，(13) 根を二乗するGraeffe変換を施す，(14) 根を逆数へ移す相反多項式をとる，(15) 重複度付き根配置へ移す，(16) 根の冪和モーメント列を作る，(17) モーメントからHankel行列族を作る，(18) 主小行列式列をとる，(19) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DerivativeRenormalization → GraeffeTransform → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → CriticalValuePolynomial → ReciprocalPolynomial → CriticalValuePolynomial → GraeffeTransform → ReciprocalPolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 平面代数曲線の合成変換（Evolute・CircleInversion・OffsetCurve・PolarReciprocal）

- ID: `research.autonomous.plane_curve.47e49433fe`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `birational_periodicity`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 法線族の包絡線である発展曲線をとる，(2) 原点中心の円反転像をとる，(3) 固定非退化二次形式に関する極逆像をとる，(4) 定義多項式のHessian曲線をとる，(5) 法線方向の代数的平行曲線をとる，(6) 正則接線族の射影双対曲線をとる，(7) 射影閉包をとり無限遠点を加える，(8) 基点を避ける一般アフィンチャートへ移す，(9) 定義多項式のHessian曲線をとる，(10) 射影閉包をとり無限遠点を加える，(11) 基点を避ける一般アフィンチャートへ移す，(12) 射影閉包をとり無限遠点を加える，(13) 基点を避ける一般アフィンチャートへ移す，(14) 固定非退化二次形式に関する極逆像をとる，(15) 法線族の包絡線である発展曲線をとる，(16) 固定光源からの反射光線族の包絡線をとる，(17) 固定基準三角形に関する等角共役Cremona像をとる，(18) 定義多項式のHessian曲線をとる，(19) 法線方向の代数的平行曲線をとる，(20) 固定非退化二次形式に関する極逆像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `Evolute → CircleInversion → PolarReciprocal → HessianCurve → OffsetCurve → ProjectiveDual → ProjectiveClosure → AffineChartChange → HessianCurve → ProjectiveClosure → AffineChartChange → ProjectiveClosure → AffineChartChange → PolarReciprocal → Evolute → Catacaustic → IsogonalCremona → HessianCurve → OffsetCurve → PolarReciprocal → BirationalPeriodQuery`

### Markov関手と到達時刻不変量（TimeReversal・DoobTransform・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.0746451264`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 定常分布に関する時間反転をとる，(2) 正の固有関数によるDoob変換を施す，(3) 恒等遷移との凸結合でlazy化する，(4) 自身との同期積連鎖を作る，(5) 自己同型軌道に沿って強 lumping する，(6) 恒等遷移との凸結合でlazy化する，(7) 自身との同期積連鎖を作る，(8) 恒等遷移との凸結合でlazy化する，(9) 正の固有関数によるDoob変換を施す，(10) 自己同型軌道に沿って強 lumping する，(11) 定常分布に関する時間反転をとる，(12) 正の固有関数によるDoob変換を施す，(13) 自己同型軌道に沿って強 lumping する，(14) 定常分布に関する時間反転をとる，(15) 自身との同期積連鎖を作る，(16) 指定集合で吸収させ過渡核をとる，(17) 過渡核のGreen作用素をとる，(18) 到達時刻の高次モーメント連立系を作る，(19) モーメント次数方向の漸化式を抽出する，(20) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `TimeReversal → DoobTransform → LazyPerturbation → ProductChain → StateLumping → LazyPerturbation → ProductChain → LazyPerturbation → DoobTransform → StateLumping → TimeReversal → DoobTransform → StateLumping → TimeReversal → ProductChain → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 平面代数曲線の合成変換（OffsetCurve・Catacaustic・ProjectiveClosure・AffineChartChange）

- ID: `research.autonomous.plane_curve.71b4c63e7a`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `birational_periodicity`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 法線方向の代数的平行曲線をとる，(2) 固定光源からの反射光線族の包絡線をとる，(3) 固定非退化二次形式に関する極逆像をとる，(4) 法線族の包絡線である発展曲線をとる，(5) 原点中心の円反転像をとる，(6) 固定光源からの反射光線族の包絡線をとる，(7) 原点中心の円反転像をとる，(8) 固定光源からの反射光線族の包絡線をとる，(9) 正則接線族の射影双対曲線をとる，(10) 固定非退化二次形式に関する極逆像をとる，(11) 固定基準三角形に関する等角共役Cremona像をとる，(12) 法線方向の代数的平行曲線をとる，(13) 固定基準三角形に関する等角共役Cremona像をとる，(14) 射影閉包をとり無限遠点を加える，(15) 基点を避ける一般アフィンチャートへ移す，(16) 射影閉包をとり無限遠点を加える，(17) 基点を避ける一般アフィンチャートへ移す，(18) 固定基準三角形に関する等角共役Cremona像をとる，(19) 射影閉包をとり無限遠点を加える，(20) 基点を避ける一般アフィンチャートへ移す。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `OffsetCurve → Catacaustic → PolarReciprocal → Evolute → CircleInversion → Catacaustic → CircleInversion → Catacaustic → ProjectiveDual → PolarReciprocal → IsogonalCremona → OffsetCurve → IsogonalCremona → ProjectiveClosure → AffineChartChange → ProjectiveClosure → AffineChartChange → IsogonalCremona → ProjectiveClosure → AffineChartChange → BirationalPeriodQuery`

### 三角形変換の合成力学（OrthocenterMark・CevianTrace・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.31416b1009`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 垂心を標識点として付加する，(2) 標識点を通る三本のcevianの辺上の足をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 垂心を標識点として付加する，(5) 各頂点と標識点が定める円の対応交点をとる，(6) 三点を頂点とする向き付き三角形を作る，(7) 外心を標識点として付加する，(8) 各頂点と標識点が定める円の対応交点をとる，(9) 三点を頂点とする向き付き三角形を作る，(10) 反中点三角形へ移す，(11) 傍心三角形へ移す，(12) 反中点三角形へ移す，(13) 傍心三角形へ移す，(14) 三辺の中点三角形へ移す，(15) 傍心三角形へ移す，(16) 重心・面積・向きを固定して相似正規化する，(17) 相似類のモジュライ点へ射影する，(18) ここまでの合成が誘導する写像を反復する，(19) 退化三角形を境界として軌道をコンパクト化する，(20) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `OrthocenterMark → CevianTrace → TriangleFormation → OrthocenterMark → VertexCircleTrace → TriangleFormation → CircumcenterMark → VertexCircleTrace → TriangleFormation → AnticomplementaryTransform → ExcentralTransform → AnticomplementaryTransform → ExcentralTransform → MedialTransform → ExcentralTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 凸体関手の合成力学（MinkowskiPolarSum・SteinerSymmetrization・IntersectionBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.6b517b9895`
- 状態: `unresolved_by_mathos`
- 射数: `22`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身と極体のMinkowski和をとる，(2) 主慣性軸方向にSteiner対称化する，(3) 差体をとる，(4) 自身と極体のMinkowski和をとる，(5) 射影体をとる，(6) 重心体をとる，(7) 原点に関する極体をとる，(8) 主慣性軸方向にSteiner対称化する，(9) 原点に関する極体をとる，(10) 射影体をとる，(11) 自身と極体のMinkowski和をとる，(12) 原点に関する極体をとる，(13) 重心体をとる，(14) 主慣性軸方向にSteiner対称化する，(15) 重心体をとる，(16) 差体をとる，(17) 射影体をとる，(18) 交叉体をとる，(19) 差体をとる，(20) 交叉体をとる，(21) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `MinkowskiPolarSum → SteinerSymmetrization → DifferenceBody → MinkowskiPolarSum → ProjectionBody → CentroidBody → PolarDual → SteinerSymmetrization → PolarDual → ProjectionBody → MinkowskiPolarSum → PolarDual → CentroidBody → SteinerSymmetrization → CentroidBody → DifferenceBody → ProjectionBody → IntersectionBody → DifferenceBody → IntersectionBody → VolumeNormalization → ConvexFixedPointQuery`

### 多項式変換と算術観測（GraeffeTransform・RootMultiset・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.9f01b40906`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を二乗するGraeffe変換を施す，(2) 重複度付き根配置へ移す，(3) 根配置からモニック多項式を再構成する，(4) 臨界値を根にもつ消去多項式を作る，(5) 根の重心を0へ移す平行移動共役を施す，(6) 臨界値を根にもつ消去多項式を作る，(7) 根を二乗するGraeffe変換を施す，(8) 根の重心を0へ移す平行移動共役を施す，(9) 根を逆数へ移す相反多項式をとる，(10) 臨界値を根にもつ消去多項式を作る，(11) 根の重心を0へ移す平行移動共役を施す，(12) 重複度付き根配置へ移す，(13) 根配置からモニック多項式を再構成する，(14) 根を逆数へ移す相反多項式をとる，(15) 重複度付き根配置へ移す，(16) 根の冪和モーメント列を作る，(17) モーメントからHankel行列族を作る，(18) 主小行列式列をとる，(19) 満たす最小線形漸化式を抽出する，(20) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `GraeffeTransform → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → ShiftConjugacy → CriticalValuePolynomial → GraeffeTransform → ShiftConjugacy → ReciprocalPolynomial → CriticalValuePolynomial → ShiftConjugacy → RootMultiset → PolynomialReconstruction → ReciprocalPolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### Markov関手と到達時刻不変量（ProductChain・LazyPerturbation・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.407ee55d47`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身との同期積連鎖を作る，(2) 恒等遷移との凸結合でlazy化する，(3) 正の固有関数によるDoob変換を施す，(4) 自身との同期積連鎖を作る，(5) 自己同型軌道に沿って強 lumping する，(6) 恒等遷移との凸結合でlazy化する，(7) 自身との同期積連鎖を作る，(8) 自己同型軌道に沿って強 lumping する，(9) 定常分布に関する時間反転をとる，(10) 正の固有関数によるDoob変換を施す，(11) 定常分布に関する時間反転をとる，(12) 正の固有関数によるDoob変換を施す，(13) 自己同型軌道に沿って強 lumping する，(14) 定常分布に関する時間反転をとる，(15) 恒等遷移との凸結合でlazy化する，(16) 指定集合で吸収させ過渡核をとる，(17) 過渡核のGreen作用素をとる，(18) 到達時刻の高次モーメント連立系を作る，(19) モーメント次数方向の漸化式を抽出する，(20) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProductChain → LazyPerturbation → DoobTransform → ProductChain → StateLumping → LazyPerturbation → ProductChain → StateLumping → TimeReversal → DoobTransform → TimeReversal → DoobTransform → StateLumping → TimeReversal → LazyPerturbation → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 凸体関手の合成力学（DifferenceBody・MinkowskiPolarSum・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.5b4f87f08b`
- 状態: `unresolved_by_mathos`
- 射数: `19`
- 問い: `convex_body_dynamics`
- 難度仮説: `23`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 差体をとる，(2) 自身と極体のMinkowski和をとる，(3) 差体をとる，(4) 主慣性軸方向にSteiner対称化する，(5) 重心体をとる，(6) 射影体をとる，(7) 主慣性軸方向にSteiner対称化する，(8) 差体をとる，(9) 原点に関する極体をとる，(10) 射影体をとる，(11) 重心体をとる，(12) 交叉体をとる，(13) 自身と極体のMinkowski和をとる，(14) 主慣性軸方向にSteiner対称化する，(15) 面積と二次モーメントを固定して正規化する，(16) ここまでの凸体関手を反復する，(17) 支持関数の軌道へ移す，(18) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DifferenceBody → MinkowskiPolarSum → DifferenceBody → SteinerSymmetrization → CentroidBody → ProjectionBody → SteinerSymmetrization → DifferenceBody → PolarDual → ProjectionBody → CentroidBody → IntersectionBody → MinkowskiPolarSum → SteinerSymmetrization → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 三角形変換の合成力学（CircumcenterMark・PedalProjection・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.51831ad589`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 外心を標識点として付加する，(2) 標識点から三辺への垂足三点をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 三辺の中点三角形へ移す，(5) 外心を標識点として付加する，(6) 各頂点と標識点が定める円の対応交点をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 反中点三角形へ移す，(9) 重心を標識点として付加する，(10) 標識点を三辺に関して反射した三点をとる，(11) 三点を頂点とする向き付き三角形を作る，(12) 垂足三角形へ移す，(13) 反中点三角形へ移す，(14) 傍心三角形へ移す，(15) 重心・面積・向きを固定して相似正規化する，(16) 相似類のモジュライ点へ射影する，(17) ここまでの合成が誘導する写像を反復する，(18) 退化三角形を境界として軌道をコンパクト化する，(19) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CircumcenterMark → PedalProjection → TriangleFormation → MedialTransform → CircumcenterMark → VertexCircleTrace → TriangleFormation → AnticomplementaryTransform → CentroidMark → SideReflectionTrace → TriangleFormation → OrthicTransform → AnticomplementaryTransform → ExcentralTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 多項式変換と算術観測（GraeffeTransform・ReciprocalPolynomial・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.8318d247d3`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `recurrence_order_drop`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を二乗するGraeffe変換を施す，(2) 根を逆数へ移す相反多項式をとる，(3) 根を二乗するGraeffe変換を施す，(4) 臨界値を根にもつ消去多項式を作る，(5) 根を逆数へ移す相反多項式をとる，(6) 導関数をモニックに再正規化する，(7) 根の重心を0へ移す平行移動共役を施す，(8) 根を二乗するGraeffe変換を施す，(9) 臨界値を根にもつ消去多項式を作る，(10) 根を逆数へ移す相反多項式をとる，(11) 重複度付き根配置へ移す，(12) 根配置からモニック多項式を再構成する，(13) 臨界値を根にもつ消去多項式を作る，(14) 導関数をモニックに再正規化する，(15) 重複度付き根配置へ移す，(16) 根の冪和モーメント列を作る，(17) モーメントからHankel行列族を作る，(18) 主小行列式列をとる，(19) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `GraeffeTransform → ReciprocalPolynomial → GraeffeTransform → CriticalValuePolynomial → ReciprocalPolynomial → DerivativeRenormalization → ShiftConjugacy → GraeffeTransform → CriticalValuePolynomial → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → DerivativeRenormalization → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 平面代数曲線の合成変換（ProjectiveDual・Evolute・HessianCurve・IsogonalCremona）

- ID: `research.autonomous.plane_curve.e0d3d22b31`
- 状態: `unresolved_by_mathos`
- 射数: `22`
- 問い: `birational_periodicity`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 正則接線族の射影双対曲線をとる，(2) 法線族の包絡線である発展曲線をとる，(3) 正則接線族の射影双対曲線をとる，(4) 法線方向の代数的平行曲線をとる，(5) 正則接線族の射影双対曲線をとる，(6) 法線方向の代数的平行曲線をとる，(7) 固定非退化二次形式に関する極逆像をとる，(8) 射影閉包をとり無限遠点を加える，(9) 基点を避ける一般アフィンチャートへ移す，(10) 射影閉包をとり無限遠点を加える，(11) 基点を避ける一般アフィンチャートへ移す，(12) 法線族の包絡線である発展曲線をとる，(13) 原点中心の円反転像をとる，(14) 射影閉包をとり無限遠点を加える，(15) 基点を避ける一般アフィンチャートへ移す，(16) 固定非退化二次形式に関する極逆像をとる，(17) 固定光源からの反射光線族の包絡線をとる，(18) 固定非退化二次形式に関する極逆像をとる，(19) 法線族の包絡線である発展曲線をとる，(20) 定義多項式のHessian曲線をとる，(21) 固定基準三角形に関する等角共役Cremona像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectiveDual → Evolute → ProjectiveDual → OffsetCurve → ProjectiveDual → OffsetCurve → PolarReciprocal → ProjectiveClosure → AffineChartChange → ProjectiveClosure → AffineChartChange → Evolute → CircleInversion → ProjectiveClosure → AffineChartChange → PolarReciprocal → Catacaustic → PolarReciprocal → Evolute → HessianCurve → IsogonalCremona → BirationalPeriodQuery`

### Markov関手と到達時刻不変量（TimeReversal・StateLumping・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.62785d1e1a`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 定常分布に関する時間反転をとる，(2) 自己同型軌道に沿って強 lumping する，(3) 正の固有関数によるDoob変換を施す，(4) 自己同型軌道に沿って強 lumping する，(5) 恒等遷移との凸結合でlazy化する，(6) 自身との同期積連鎖を作る，(7) 正の固有関数によるDoob変換を施す，(8) 自己同型軌道に沿って強 lumping する，(9) 正の固有関数によるDoob変換を施す，(10) 恒等遷移との凸結合でlazy化する，(11) 定常分布に関する時間反転をとる，(12) 恒等遷移との凸結合でlazy化する，(13) 自身との同期積連鎖を作る，(14) 定常分布に関する時間反転をとる，(15) 自身との同期積連鎖を作る，(16) 指定集合で吸収させ過渡核をとる，(17) 過渡核のGreen作用素をとる，(18) 到達時刻の高次モーメント連立系を作る，(19) モーメント次数方向の漸化式を抽出する，(20) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `TimeReversal → StateLumping → DoobTransform → StateLumping → LazyPerturbation → ProductChain → DoobTransform → StateLumping → DoobTransform → LazyPerturbation → TimeReversal → LazyPerturbation → ProductChain → TimeReversal → ProductChain → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 三角形変換の合成力学（OrthicTransform・MedialTransform・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.053beee06b`
- 状態: `unresolved_by_mathos`
- 射数: `19`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `23`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 垂足三角形へ移す，(2) 三辺の中点三角形へ移す，(3) 類似重心を標識点として付加する，(4) 各頂点と標識点が定める円の対応交点をとる，(5) 三点を頂点とする向き付き三角形を作る，(6) 傍心三角形へ移す，(7) 内心を標識点として付加する，(8) 標識点を通る三本のcevianの辺上の足をとる，(9) 三点を頂点とする向き付き三角形を作る，(10) 三辺の中点三角形へ移す，(11) 外心を標識点として付加する，(12) 標識点を三辺に関して反射した三点をとる，(13) 三点を頂点とする向き付き三角形を作る，(14) 重心・面積・向きを固定して相似正規化する，(15) 相似類のモジュライ点へ射影する，(16) ここまでの合成が誘導する写像を反復する，(17) 退化三角形を境界として軌道をコンパクト化する，(18) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `OrthicTransform → MedialTransform → SymmedianMark → VertexCircleTrace → TriangleFormation → ExcentralTransform → IncenterMark → CevianTrace → TriangleFormation → MedialTransform → CircumcenterMark → SideReflectionTrace → TriangleFormation → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 多項式変換と算術観測（CriticalValuePolynomial・GraeffeTransform・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.e42f5bf1ff`
- 状態: `unresolved_by_mathos`
- 射数: `19`
- 問い: `recurrence_order_drop`
- 難度仮説: `22`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 臨界値を根にもつ消去多項式を作る，(2) 根を二乗するGraeffe変換を施す，(3) 重複度付き根配置へ移す，(4) 根配置からモニック多項式を再構成する，(5) 根の重心を0へ移す平行移動共役を施す，(6) 根を二乗するGraeffe変換を施す，(7) 根の重心を0へ移す平行移動共役を施す，(8) 臨界値を根にもつ消去多項式を作る，(9) 根の重心を0へ移す平行移動共役を施す，(10) 根を逆数へ移す相反多項式をとる，(11) 重複度付き根配置へ移す，(12) 根配置からモニック多項式を再構成する，(13) 臨界値を根にもつ消去多項式を作る，(14) 重複度付き根配置へ移す，(15) 根の冪和モーメント列を作る，(16) モーメントからHankel行列族を作る，(17) 主小行列式列をとる，(18) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CriticalValuePolynomial → GraeffeTransform → RootMultiset → PolynomialReconstruction → ShiftConjugacy → GraeffeTransform → ShiftConjugacy → CriticalValuePolynomial → ShiftConjugacy → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 凸体関手の合成力学（ProjectionBody・PolarDual・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.ce2d8baf0d`
- 状態: `unresolved_by_mathos`
- 射数: `22`
- 問い: `convex_body_dynamics`
- 難度仮説: `26`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 射影体をとる，(2) 原点に関する極体をとる，(3) 射影体をとる，(4) 交叉体をとる，(5) 差体をとる，(6) 交叉体をとる，(7) 差体をとる，(8) 射影体をとる，(9) 差体をとる，(10) 交叉体をとる，(11) 重心体をとる，(12) 主慣性軸方向にSteiner対称化する，(13) 自身と極体のMinkowski和をとる，(14) 原点に関する極体をとる，(15) 主慣性軸方向にSteiner対称化する，(16) 原点に関する極体をとる，(17) 重心体をとる，(18) 面積と二次モーメントを固定して正規化する，(19) ここまでの凸体関手を反復する，(20) 支持関数の軌道へ移す，(21) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectionBody → PolarDual → ProjectionBody → IntersectionBody → DifferenceBody → IntersectionBody → DifferenceBody → ProjectionBody → DifferenceBody → IntersectionBody → CentroidBody → SteinerSymmetrization → MinkowskiPolarSum → PolarDual → SteinerSymmetrization → PolarDual → CentroidBody → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 平面代数曲線の合成変換（OffsetCurve・HessianCurve・Evolute・IsogonalCremona）

- ID: `research.autonomous.plane_curve.64167b60e4`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `birational_periodicity`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 法線方向の代数的平行曲線をとる，(2) 定義多項式のHessian曲線をとる，(3) 固定非退化二次形式に関する極逆像をとる，(4) 定義多項式のHessian曲線をとる，(5) 固定非退化二次形式に関する極逆像をとる，(6) 射影閉包をとり無限遠点を加える，(7) 基点を避ける一般アフィンチャートへ移す，(8) 定義多項式のHessian曲線をとる，(9) 正則接線族の射影双対曲線をとる，(10) 法線族の包絡線である発展曲線をとる，(11) 正則接線族の射影双対曲線をとる，(12) 原点中心の円反転像をとる，(13) 固定非退化二次形式に関する極逆像をとる，(14) 法線族の包絡線である発展曲線をとる，(15) 固定光源からの反射光線族の包絡線をとる，(16) 固定基準三角形に関する等角共役Cremona像をとる，(17) 正則接線族の射影双対曲線をとる，(18) 固定基準三角形に関する等角共役Cremona像をとる，(19) 法線族の包絡線である発展曲線をとる，(20) 固定基準三角形に関する等角共役Cremona像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `OffsetCurve → HessianCurve → PolarReciprocal → HessianCurve → PolarReciprocal → ProjectiveClosure → AffineChartChange → HessianCurve → ProjectiveDual → Evolute → ProjectiveDual → CircleInversion → PolarReciprocal → Evolute → Catacaustic → IsogonalCremona → ProjectiveDual → IsogonalCremona → Evolute → IsogonalCremona → BirationalPeriodQuery`

### Markov関手と到達時刻不変量（DoobTransform・StateLumping・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.82ce17b4da`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `23`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 正の固有関数によるDoob変換を施す，(2) 自己同型軌道に沿って強 lumping する，(3) 恒等遷移との凸結合でlazy化する，(4) 自身との同期積連鎖を作る，(5) 正の固有関数によるDoob変換を施す，(6) 自身との同期積連鎖を作る，(7) 恒等遷移との凸結合でlazy化する，(8) 正の固有関数によるDoob変換を施す，(9) 定常分布に関する時間反転をとる，(10) 自己同型軌道に沿って強 lumping する，(11) 恒等遷移との凸結合でlazy化する，(12) 定常分布に関する時間反転をとる，(13) 自身との同期積連鎖を作る，(14) 定常分布に関する時間反転をとる，(15) 指定集合で吸収させ過渡核をとる，(16) 過渡核のGreen作用素をとる，(17) 到達時刻の高次モーメント連立系を作る，(18) モーメント次数方向の漸化式を抽出する，(19) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DoobTransform → StateLumping → LazyPerturbation → ProductChain → DoobTransform → ProductChain → LazyPerturbation → DoobTransform → TimeReversal → StateLumping → LazyPerturbation → TimeReversal → ProductChain → TimeReversal → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 平面代数曲線の合成変換（ProjectiveClosure・AffineChartChange・ResolveSingularities・CurveInvariantExtraction）

- ID: `research.autonomous.plane_curve.1769a34057`
- 状態: `unresolved_by_mathos`
- 射数: `19`
- 問い: `singularity_classification`
- 難度仮説: `22`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 射影閉包をとり無限遠点を加える，(2) 基点を避ける一般アフィンチャートへ移す，(3) 法線族の包絡線である発展曲線をとる，(4) 射影閉包をとり無限遠点を加える，(5) 基点を避ける一般アフィンチャートへ移す，(6) 正則接線族の射影双対曲線をとる，(7) 固定基準三角形に関する等角共役Cremona像をとる，(8) 固定非退化二次形式に関する極逆像をとる，(9) 固定光源からの反射光線族の包絡線をとる，(10) 正則接線族の射影双対曲線をとる，(11) 固定基準三角形に関する等角共役Cremona像をとる，(12) 正則接線族の射影双対曲線をとる，(13) 固定基準三角形に関する等角共役Cremona像をとる，(14) 固定非退化二次形式に関する極逆像をとる，(15) 法線方向の代数的平行曲線をとる，(16) 射影閉包をとり無限遠点を加える，(17) 全特異点を解消して正規化曲線を得る，(18) 次数、分岐、種数、自己交点データを抽出する。最後に、全特異点型と実枝数を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectiveClosure → AffineChartChange → Evolute → ProjectiveClosure → AffineChartChange → ProjectiveDual → IsogonalCremona → PolarReciprocal → Catacaustic → ProjectiveDual → IsogonalCremona → ProjectiveDual → IsogonalCremona → PolarReciprocal → OffsetCurve → ProjectiveClosure → ResolveSingularities → CurveInvariantExtraction → SingularityQuery`

### 凸体関手の合成力学（ProjectionBody・SteinerSymmetrization・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.5cabfe5b74`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `convex_body_dynamics`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 射影体をとる，(2) 主慣性軸方向にSteiner対称化する，(3) 射影体をとる，(4) 重心体をとる，(5) 交叉体をとる，(6) 自身と極体のMinkowski和をとる，(7) 差体をとる，(8) 原点に関する極体をとる，(9) 射影体をとる，(10) 重心体をとる，(11) 交叉体をとる，(12) 主慣性軸方向にSteiner対称化する，(13) 自身と極体のMinkowski和をとる，(14) 差体をとる，(15) 重心体をとる，(16) 交叉体をとる，(17) 面積と二次モーメントを固定して正規化する，(18) ここまでの凸体関手を反復する，(19) 支持関数の軌道へ移す，(20) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectionBody → SteinerSymmetrization → ProjectionBody → CentroidBody → IntersectionBody → MinkowskiPolarSum → DifferenceBody → PolarDual → ProjectionBody → CentroidBody → IntersectionBody → SteinerSymmetrization → MinkowskiPolarSum → DifferenceBody → CentroidBody → IntersectionBody → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 多項式変換と算術観測（ShiftConjugacy・DerivativeRenormalization・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.3b51118bc9`
- 状態: `unresolved_by_mathos`
- 射数: `22`
- 問い: `recurrence_order_drop`
- 難度仮説: `26`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根の重心を0へ移す平行移動共役を施す，(2) 導関数をモニックに再正規化する，(3) 根を二乗するGraeffe変換を施す，(4) 根を逆数へ移す相反多項式をとる，(5) 根の重心を0へ移す平行移動共役を施す，(6) 重複度付き根配置へ移す，(7) 根配置からモニック多項式を再構成する，(8) 重複度付き根配置へ移す，(9) 根配置からモニック多項式を再構成する，(10) 根を逆数へ移す相反多項式をとる，(11) 導関数をモニックに再正規化する，(12) 根の重心を0へ移す平行移動共役を施す，(13) 臨界値を根にもつ消去多項式を作る，(14) 根を二乗するGraeffe変換を施す，(15) 根を逆数へ移す相反多項式をとる，(16) 臨界値を根にもつ消去多項式を作る，(17) 重複度付き根配置へ移す，(18) 根の冪和モーメント列を作る，(19) モーメントからHankel行列族を作る，(20) 主小行列式列をとる，(21) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ShiftConjugacy → DerivativeRenormalization → GraeffeTransform → ReciprocalPolynomial → ShiftConjugacy → RootMultiset → PolynomialReconstruction → RootMultiset → PolynomialReconstruction → ReciprocalPolynomial → DerivativeRenormalization → ShiftConjugacy → CriticalValuePolynomial → GraeffeTransform → ReciprocalPolynomial → CriticalValuePolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 三角形変換の合成力学（ExcentralTransform・CircumcenterMark・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.f5420e7921`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 傍心三角形へ移す，(2) 外心を標識点として付加する，(3) 標識点から三辺への垂足三点をとる，(4) 三点を頂点とする向き付き三角形を作る，(5) 三辺の中点三角形へ移す，(6) 傍心三角形へ移す，(7) 外心を標識点として付加する，(8) 標識点から三辺への垂足三点をとる，(9) 三点を頂点とする向き付き三角形を作る，(10) 重心を標識点として付加する，(11) 標識点から三辺への垂足三点をとる，(12) 三点を頂点とする向き付き三角形を作る，(13) 傍心三角形へ移す，(14) 反中点三角形へ移す，(15) 重心・面積・向きを固定して相似正規化する，(16) 相似類のモジュライ点へ射影する，(17) ここまでの合成が誘導する写像を反復する，(18) 退化三角形を境界として軌道をコンパクト化する，(19) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ExcentralTransform → CircumcenterMark → PedalProjection → TriangleFormation → MedialTransform → ExcentralTransform → CircumcenterMark → PedalProjection → TriangleFormation → CentroidMark → PedalProjection → TriangleFormation → ExcentralTransform → AnticomplementaryTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### Markov関手と到達時刻不変量（TimeReversal・ProductChain・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.623df1300d`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `23`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 定常分布に関する時間反転をとる，(2) 自身との同期積連鎖を作る，(3) 自己同型軌道に沿って強 lumping する，(4) 正の固有関数によるDoob変換を施す，(5) 定常分布に関する時間反転をとる，(6) 自己同型軌道に沿って強 lumping する，(7) 自身との同期積連鎖を作る，(8) 正の固有関数によるDoob変換を施す，(9) 定常分布に関する時間反転をとる，(10) 自身との同期積連鎖を作る，(11) 正の固有関数によるDoob変換を施す，(12) 恒等遷移との凸結合でlazy化する，(13) 自己同型軌道に沿って強 lumping する，(14) 恒等遷移との凸結合でlazy化する，(15) 指定集合で吸収させ過渡核をとる，(16) 過渡核のGreen作用素をとる，(17) 到達時刻の高次モーメント連立系を作る，(18) モーメント次数方向の漸化式を抽出する，(19) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `TimeReversal → ProductChain → StateLumping → DoobTransform → TimeReversal → StateLumping → ProductChain → DoobTransform → TimeReversal → ProductChain → DoobTransform → LazyPerturbation → StateLumping → LazyPerturbation → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 多項式変換と算術観測（ReciprocalPolynomial・CriticalValuePolynomial・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.0dc6b2f330`
- 状態: `unresolved_by_mathos`
- 射数: `22`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `26`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を逆数へ移す相反多項式をとる，(2) 臨界値を根にもつ消去多項式を作る，(3) 重複度付き根配置へ移す，(4) 根配置からモニック多項式を再構成する，(5) 重複度付き根配置へ移す，(6) 根配置からモニック多項式を再構成する，(7) 根を逆数へ移す相反多項式をとる，(8) 根の重心を0へ移す平行移動共役を施す，(9) 臨界値を根にもつ消去多項式を作る，(10) 根を二乗するGraeffe変換を施す，(11) 根の重心を0へ移す平行移動共役を施す，(12) 根を逆数へ移す相反多項式をとる，(13) 根を二乗するGraeffe変換を施す，(14) 根の重心を0へ移す平行移動共役を施す，(15) 臨界値を根にもつ消去多項式を作る，(16) 重複度付き根配置へ移す，(17) 根の冪和モーメント列を作る，(18) モーメントからHankel行列族を作る，(19) 主小行列式列をとる，(20) 満たす最小線形漸化式を抽出する，(21) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ReciprocalPolynomial → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → RootMultiset → PolynomialReconstruction → ReciprocalPolynomial → ShiftConjugacy → CriticalValuePolynomial → GraeffeTransform → ShiftConjugacy → ReciprocalPolynomial → GraeffeTransform → ShiftConjugacy → CriticalValuePolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 凸体関手の合成力学（SteinerSymmetrization・IntersectionBody・DifferenceBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.ea757f8a29`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 主慣性軸方向にSteiner対称化する，(2) 交叉体をとる，(3) 原点に関する極体をとる，(4) 主慣性軸方向にSteiner対称化する，(5) 差体をとる，(6) 交叉体をとる，(7) 自身と極体のMinkowski和をとる，(8) 重心体をとる，(9) 原点に関する極体をとる，(10) 主慣性軸方向にSteiner対称化する，(11) 重心体をとる，(12) 自身と極体のMinkowski和をとる，(13) 原点に関する極体をとる，(14) 自身と極体のMinkowski和をとる，(15) 重心体をとる，(16) 差体をとる，(17) 射影体をとる，(18) 交叉体をとる，(19) 差体をとる，(20) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `SteinerSymmetrization → IntersectionBody → PolarDual → SteinerSymmetrization → DifferenceBody → IntersectionBody → MinkowskiPolarSum → CentroidBody → PolarDual → SteinerSymmetrization → CentroidBody → MinkowskiPolarSum → PolarDual → MinkowskiPolarSum → CentroidBody → DifferenceBody → ProjectionBody → IntersectionBody → DifferenceBody → VolumeNormalization → ConvexFixedPointQuery`

### 平面代数曲線の合成変換（CircleInversion・Catacaustic・HessianCurve・Evolute）

- ID: `research.autonomous.plane_curve.b854ea56de`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `birational_periodicity`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 原点中心の円反転像をとる，(2) 固定光源からの反射光線族の包絡線をとる，(3) 原点中心の円反転像をとる，(4) 固定光源からの反射光線族の包絡線をとる，(5) 固定基準三角形に関する等角共役Cremona像をとる，(6) 法線方向の代数的平行曲線をとる，(7) 正則接線族の射影双対曲線をとる，(8) 射影閉包をとり無限遠点を加える，(9) 基点を避ける一般アフィンチャートへ移す，(10) 正則接線族の射影双対曲線をとる，(11) 固定光源からの反射光線族の包絡線をとる，(12) 定義多項式のHessian曲線をとる，(13) 原点中心の円反転像をとる，(14) 固定非退化二次形式に関する極逆像をとる，(15) 正則接線族の射影双対曲線をとる，(16) 射影閉包をとり無限遠点を加える，(17) 基点を避ける一般アフィンチャートへ移す，(18) 固定基準三角形に関する等角共役Cremona像をとる，(19) 定義多項式のHessian曲線をとる，(20) 法線族の包絡線である発展曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CircleInversion → Catacaustic → CircleInversion → Catacaustic → IsogonalCremona → OffsetCurve → ProjectiveDual → ProjectiveClosure → AffineChartChange → ProjectiveDual → Catacaustic → HessianCurve → CircleInversion → PolarReciprocal → ProjectiveDual → ProjectiveClosure → AffineChartChange → IsogonalCremona → HessianCurve → Evolute → BirationalPeriodQuery`

### 三角形変換の合成力学（MedialTransform・CentroidMark・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.6fb1b55b2c`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 三辺の中点三角形へ移す，(2) 重心を標識点として付加する，(3) 標識点から三辺への垂足三点をとる，(4) 三点を頂点とする向き付き三角形を作る，(5) 重心を標識点として付加する，(6) 標識点を通る三本のcevianの辺上の足をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 類似重心を標識点として付加する，(9) 各頂点と標識点が定める円の対応交点をとる，(10) 三点を頂点とする向き付き三角形を作る，(11) 傍心三角形へ移す，(12) 反中点三角形へ移す，(13) 傍心三角形へ移す，(14) 三辺の中点三角形へ移す，(15) 傍心三角形へ移す，(16) 重心・面積・向きを固定して相似正規化する，(17) 相似類のモジュライ点へ射影する，(18) ここまでの合成が誘導する写像を反復する，(19) 退化三角形を境界として軌道をコンパクト化する，(20) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `MedialTransform → CentroidMark → PedalProjection → TriangleFormation → CentroidMark → CevianTrace → TriangleFormation → SymmedianMark → VertexCircleTrace → TriangleFormation → ExcentralTransform → AnticomplementaryTransform → ExcentralTransform → MedialTransform → ExcentralTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### Markov関手と到達時刻不変量（TimeReversal・StateLumping・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.089b8ecb45`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `23`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 定常分布に関する時間反転をとる，(2) 自己同型軌道に沿って強 lumping する，(3) 正の固有関数によるDoob変換を施す，(4) 恒等遷移との凸結合でlazy化する，(5) 正の固有関数によるDoob変換を施す，(6) 定常分布に関する時間反転をとる，(7) 自身との同期積連鎖を作る，(8) 正の固有関数によるDoob変換を施す，(9) 自身との同期積連鎖を作る，(10) 定常分布に関する時間反転をとる，(11) 自身との同期積連鎖を作る，(12) 自己同型軌道に沿って強 lumping する，(13) 恒等遷移との凸結合でlazy化する，(14) 自己同型軌道に沿って強 lumping する，(15) 恒等遷移との凸結合でlazy化する，(16) 指定集合で吸収させ過渡核をとる，(17) 過渡核のGreen作用素をとる，(18) 到達時刻の高次モーメント連立系を作る，(19) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `TimeReversal → StateLumping → DoobTransform → LazyPerturbation → DoobTransform → TimeReversal → ProductChain → DoobTransform → ProductChain → TimeReversal → ProductChain → StateLumping → LazyPerturbation → StateLumping → LazyPerturbation → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 多項式変換と算術観測（ShiftConjugacy・ReciprocalPolynomial・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.9bd4fb5fcb`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `recurrence_order_drop`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根の重心を0へ移す平行移動共役を施す，(2) 根を逆数へ移す相反多項式をとる，(3) 導関数をモニックに再正規化する，(4) 重複度付き根配置へ移す，(5) 根配置からモニック多項式を再構成する，(6) 重複度付き根配置へ移す，(7) 根配置からモニック多項式を再構成する，(8) 臨界値を根にもつ消去多項式を作る，(9) 根を逆数へ移す相反多項式をとる，(10) 臨界値を根にもつ消去多項式を作る，(11) 根の重心を0へ移す平行移動共役を施す，(12) 臨界値を根にもつ消去多項式を作る，(13) 根の重心を0へ移す平行移動共役を施す，(14) 導関数をモニックに再正規化する，(15) 根を二乗するGraeffe変換を施す，(16) 重複度付き根配置へ移す，(17) 根の冪和モーメント列を作る，(18) モーメントからHankel行列族を作る，(19) 主小行列式列をとる，(20) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ShiftConjugacy → ReciprocalPolynomial → DerivativeRenormalization → RootMultiset → PolynomialReconstruction → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → ReciprocalPolynomial → CriticalValuePolynomial → ShiftConjugacy → CriticalValuePolynomial → ShiftConjugacy → DerivativeRenormalization → GraeffeTransform → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 平面代数曲線の合成変換（CircleInversion・Catacaustic・Evolute・OffsetCurve）

- ID: `research.autonomous.plane_curve.2b18500dab`
- 状態: `unresolved_by_mathos`
- 射数: `22`
- 問い: `birational_periodicity`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 原点中心の円反転像をとる，(2) 固定光源からの反射光線族の包絡線をとる，(3) 法線方向の代数的平行曲線をとる，(4) 正則接線族の射影双対曲線をとる，(5) 固定非退化二次形式に関する極逆像をとる，(6) 固定光源からの反射光線族の包絡線をとる，(7) 射影閉包をとり無限遠点を加える，(8) 基点を避ける一般アフィンチャートへ移す，(9) 固定非退化二次形式に関する極逆像をとる，(10) 原点中心の円反転像をとる，(11) 定義多項式のHessian曲線をとる，(12) 法線族の包絡線である発展曲線をとる，(13) 固定基準三角形に関する等角共役Cremona像をとる，(14) 法線族の包絡線である発展曲線をとる，(15) 定義多項式のHessian曲線をとる，(16) 固定光源からの反射光線族の包絡線をとる，(17) 正則接線族の射影双対曲線をとる，(18) 固定非退化二次形式に関する極逆像をとる，(19) 定義多項式のHessian曲線をとる，(20) 法線族の包絡線である発展曲線をとる，(21) 法線方向の代数的平行曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CircleInversion → Catacaustic → OffsetCurve → ProjectiveDual → PolarReciprocal → Catacaustic → ProjectiveClosure → AffineChartChange → PolarReciprocal → CircleInversion → HessianCurve → Evolute → IsogonalCremona → Evolute → HessianCurve → Catacaustic → ProjectiveDual → PolarReciprocal → HessianCurve → Evolute → OffsetCurve → BirationalPeriodQuery`

### 凸体関手の合成力学（DifferenceBody・ProjectionBody・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.9113b6cc63`
- 状態: `unresolved_by_mathos`
- 射数: `22`
- 問い: `convex_body_dynamics`
- 難度仮説: `26`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 差体をとる，(2) 射影体をとる，(3) 原点に関する極体をとる，(4) 差体をとる，(5) 自身と極体のMinkowski和をとる，(6) 差体をとる，(7) 交叉体をとる，(8) 射影体をとる，(9) 原点に関する極体をとる，(10) 主慣性軸方向にSteiner対称化する，(11) 交叉体をとる，(12) 原点に関する極体をとる，(13) 自身と極体のMinkowski和をとる，(14) 交叉体をとる，(15) 自身と極体のMinkowski和をとる，(16) 重心体をとる，(17) 主慣性軸方向にSteiner対称化する，(18) 面積と二次モーメントを固定して正規化する，(19) ここまでの凸体関手を反復する，(20) 支持関数の軌道へ移す，(21) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DifferenceBody → ProjectionBody → PolarDual → DifferenceBody → MinkowskiPolarSum → DifferenceBody → IntersectionBody → ProjectionBody → PolarDual → SteinerSymmetrization → IntersectionBody → PolarDual → MinkowskiPolarSum → IntersectionBody → MinkowskiPolarSum → CentroidBody → SteinerSymmetrization → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 三角形変換の合成力学（CircumcenterMark・SideReflectionTrace・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.f52b1f68a2`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 外心を標識点として付加する，(2) 標識点を三辺に関して反射した三点をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 垂足三角形へ移す，(5) 垂心を標識点として付加する，(6) 標識点から三辺への垂足三点をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 反中点三角形へ移す，(9) 垂心を標識点として付加する，(10) 標識点を三辺に関して反射した三点をとる，(11) 三点を頂点とする向き付き三角形を作る，(12) 三辺の中点三角形へ移す，(13) 垂足三角形へ移す，(14) 三辺の中点三角形へ移す，(15) 垂足三角形へ移す，(16) 重心・面積・向きを固定して相似正規化する，(17) 相似類のモジュライ点へ射影する，(18) ここまでの合成が誘導する写像を反復する，(19) 退化三角形を境界として軌道をコンパクト化する，(20) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CircumcenterMark → SideReflectionTrace → TriangleFormation → OrthicTransform → OrthocenterMark → PedalProjection → TriangleFormation → AnticomplementaryTransform → OrthocenterMark → SideReflectionTrace → TriangleFormation → MedialTransform → OrthicTransform → MedialTransform → OrthicTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### Markov関手と到達時刻不変量（DoobTransform・ProductChain・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.0edfc52935`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `23`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 正の固有関数によるDoob変換を施す，(2) 自身との同期積連鎖を作る，(3) 正の固有関数によるDoob変換を施す，(4) 自身との同期積連鎖を作る，(5) 正の固有関数によるDoob変換を施す，(6) 自己同型軌道に沿って強 lumping する，(7) 恒等遷移との凸結合でlazy化する，(8) 自己同型軌道に沿って強 lumping する，(9) 定常分布に関する時間反転をとる，(10) 自身との同期積連鎖を作る，(11) 自己同型軌道に沿って強 lumping する，(12) 恒等遷移との凸結合でlazy化する，(13) 定常分布に関する時間反転をとる，(14) 恒等遷移との凸結合でlazy化する，(15) 指定集合で吸収させ過渡核をとる，(16) 過渡核のGreen作用素をとる，(17) 到達時刻の高次モーメント連立系を作る，(18) モーメント次数方向の漸化式を抽出する，(19) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DoobTransform → ProductChain → DoobTransform → ProductChain → DoobTransform → StateLumping → LazyPerturbation → StateLumping → TimeReversal → ProductChain → StateLumping → LazyPerturbation → TimeReversal → LazyPerturbation → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 多項式変換と算術観測（RootMultiset・PolynomialReconstruction・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.df64e7dfde`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `recurrence_order_drop`
- 難度仮説: `23`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重複度付き根配置へ移す，(2) 根配置からモニック多項式を再構成する，(3) 重複度付き根配置へ移す，(4) 根配置からモニック多項式を再構成する，(5) 根を逆数へ移す相反多項式をとる，(6) 根の重心を0へ移す平行移動共役を施す，(7) 根を二乗するGraeffe変換を施す，(8) 根の重心を0へ移す平行移動共役を施す，(9) 臨界値を根にもつ消去多項式を作る，(10) 根を逆数へ移す相反多項式をとる，(11) 根を二乗するGraeffe変換を施す，(12) 根を逆数へ移す相反多項式をとる，(13) 根を二乗するGraeffe変換を施す，(14) 根の重心を0へ移す平行移動共役を施す，(15) 重複度付き根配置へ移す，(16) 根の冪和モーメント列を作る，(17) モーメントからHankel行列族を作る，(18) 主小行列式列をとる，(19) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `RootMultiset → PolynomialReconstruction → RootMultiset → PolynomialReconstruction → ReciprocalPolynomial → ShiftConjugacy → GraeffeTransform → ShiftConjugacy → CriticalValuePolynomial → ReciprocalPolynomial → GraeffeTransform → ReciprocalPolynomial → GraeffeTransform → ShiftConjugacy → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 凸体関手の合成力学（ProjectionBody・DifferenceBody・SteinerSymmetrization・VolumeNormalization）

- ID: `research.autonomous.convex_body.07df27c455`
- 状態: `unresolved_by_mathos`
- 射数: `22`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 射影体をとる，(2) 差体をとる，(3) 交叉体をとる，(4) 自身と極体のMinkowski和をとる，(5) 交叉体をとる，(6) 重心体をとる，(7) 射影体をとる，(8) 主慣性軸方向にSteiner対称化する，(9) 原点に関する極体をとる，(10) 自身と極体のMinkowski和をとる，(11) 重心体をとる，(12) 差体をとる，(13) 自身と極体のMinkowski和をとる，(14) 射影体をとる，(15) 差体をとる，(16) 重心体をとる，(17) 原点に関する極体をとる，(18) 交叉体をとる，(19) 原点に関する極体をとる，(20) 主慣性軸方向にSteiner対称化する，(21) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectionBody → DifferenceBody → IntersectionBody → MinkowskiPolarSum → IntersectionBody → CentroidBody → ProjectionBody → SteinerSymmetrization → PolarDual → MinkowskiPolarSum → CentroidBody → DifferenceBody → MinkowskiPolarSum → ProjectionBody → DifferenceBody → CentroidBody → PolarDual → IntersectionBody → PolarDual → SteinerSymmetrization → VolumeNormalization → ConvexFixedPointQuery`

### 平面代数曲線の合成変換（HessianCurve・ProjectiveClosure・Evolute・OffsetCurve）

- ID: `research.autonomous.plane_curve.c363417c52`
- 状態: `unresolved_by_mathos`
- 射数: `22`
- 問い: `birational_periodicity`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 定義多項式のHessian曲線をとる，(2) 射影閉包をとり無限遠点を加える，(3) 基点を避ける一般アフィンチャートへ移す，(4) 固定非退化二次形式に関する極逆像をとる，(5) 原点中心の円反転像をとる，(6) 法線方向の代数的平行曲線をとる，(7) 定義多項式のHessian曲線をとる，(8) 原点中心の円反転像をとる，(9) 射影閉包をとり無限遠点を加える，(10) 基点を避ける一般アフィンチャートへ移す，(11) 法線族の包絡線である発展曲線をとる，(12) 原点中心の円反転像をとる，(13) 定義多項式のHessian曲線をとる，(14) 法線族の包絡線である発展曲線をとる，(15) 射影閉包をとり無限遠点を加える，(16) 基点を避ける一般アフィンチャートへ移す，(17) 正則接線族の射影双対曲線をとる，(18) 法線方向の代数的平行曲線をとる，(19) 固定光源からの反射光線族の包絡線をとる，(20) 法線族の包絡線である発展曲線をとる，(21) 法線方向の代数的平行曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `HessianCurve → ProjectiveClosure → AffineChartChange → PolarReciprocal → CircleInversion → OffsetCurve → HessianCurve → CircleInversion → ProjectiveClosure → AffineChartChange → Evolute → CircleInversion → HessianCurve → Evolute → ProjectiveClosure → AffineChartChange → ProjectiveDual → OffsetCurve → Catacaustic → Evolute → OffsetCurve → BirationalPeriodQuery`

### 三角形変換の合成力学（IncenterMark・SideReflectionTrace・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.4eee61be40`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 内心を標識点として付加する，(2) 標識点を三辺に関して反射した三点をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 反中点三角形へ移す，(5) 垂心を標識点として付加する，(6) 各頂点と標識点が定める円の対応交点をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 垂足三角形へ移す，(9) 外心を標識点として付加する，(10) 標識点を通る三本のcevianの辺上の足をとる，(11) 三点を頂点とする向き付き三角形を作る，(12) 垂足三角形へ移す，(13) 三辺の中点三角形へ移す，(14) 傍心三角形へ移す，(15) 重心・面積・向きを固定して相似正規化する，(16) 相似類のモジュライ点へ射影する，(17) ここまでの合成が誘導する写像を反復する，(18) 退化三角形を境界として軌道をコンパクト化する，(19) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IncenterMark → SideReflectionTrace → TriangleFormation → AnticomplementaryTransform → OrthocenterMark → VertexCircleTrace → TriangleFormation → OrthicTransform → CircumcenterMark → CevianTrace → TriangleFormation → OrthicTransform → MedialTransform → ExcentralTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### Markov関手と到達時刻不変量（ProductChain・TimeReversal・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.767c46c7be`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `23`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身との同期積連鎖を作る，(2) 定常分布に関する時間反転をとる，(3) 恒等遷移との凸結合でlazy化する，(4) 正の固有関数によるDoob変換を施す，(5) 恒等遷移との凸結合でlazy化する，(6) 正の固有関数によるDoob変換を施す，(7) 自己同型軌道に沿って強 lumping する，(8) 定常分布に関する時間反転をとる，(9) 自身との同期積連鎖を作る，(10) 定常分布に関する時間反転をとる，(11) 自己同型軌道に沿って強 lumping する，(12) 正の固有関数によるDoob変換を施す，(13) 恒等遷移との凸結合でlazy化する，(14) 自己同型軌道に沿って強 lumping する，(15) 自身との同期積連鎖を作る，(16) 指定集合で吸収させ過渡核をとる，(17) 過渡核のGreen作用素をとる，(18) 到達時刻の高次モーメント連立系を作る，(19) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProductChain → TimeReversal → LazyPerturbation → DoobTransform → LazyPerturbation → DoobTransform → StateLumping → TimeReversal → ProductChain → TimeReversal → StateLumping → DoobTransform → LazyPerturbation → StateLumping → ProductChain → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 平面代数曲線の合成変換（PolarReciprocal・ProjectiveClosure・OffsetCurve・PolarReciprocal）

- ID: `research.autonomous.plane_curve.4109893021`
- 状態: `unresolved_by_mathos`
- 射数: `22`
- 問い: `birational_periodicity`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定非退化二次形式に関する極逆像をとる，(2) 射影閉包をとり無限遠点を加える，(3) 基点を避ける一般アフィンチャートへ移す，(4) 定義多項式のHessian曲線をとる，(5) 原点中心の円反転像をとる，(6) 固定光源からの反射光線族の包絡線をとる，(7) 原点中心の円反転像をとる，(8) 固定光源からの反射光線族の包絡線をとる，(9) 固定基準三角形に関する等角共役Cremona像をとる，(10) 正則接線族の射影双対曲線をとる，(11) 法線族の包絡線である発展曲線をとる，(12) 固定光源からの反射光線族の包絡線をとる，(13) 法線族の包絡線である発展曲線をとる，(14) 定義多項式のHessian曲線をとる，(15) 正則接線族の射影双対曲線をとる，(16) 法線族の包絡線である発展曲線をとる，(17) 法線方向の代数的平行曲線をとる，(18) 正則接線族の射影双対曲線をとる，(19) 定義多項式のHessian曲線をとる，(20) 法線方向の代数的平行曲線をとる，(21) 固定非退化二次形式に関する極逆像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `PolarReciprocal → ProjectiveClosure → AffineChartChange → HessianCurve → CircleInversion → Catacaustic → CircleInversion → Catacaustic → IsogonalCremona → ProjectiveDual → Evolute → Catacaustic → Evolute → HessianCurve → ProjectiveDual → Evolute → OffsetCurve → ProjectiveDual → HessianCurve → OffsetCurve → PolarReciprocal → BirationalPeriodQuery`

### 多項式変換と算術観測（DerivativeRenormalization・GraeffeTransform・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.3750d3b00e`
- 状態: `unresolved_by_mathos`
- 射数: `22`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `26`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 導関数をモニックに再正規化する，(2) 根を二乗するGraeffe変換を施す，(3) 根を逆数へ移す相反多項式をとる，(4) 根を二乗するGraeffe変換を施す，(5) 根の重心を0へ移す平行移動共役を施す，(6) 根を二乗するGraeffe変換を施す，(7) 臨界値を根にもつ消去多項式を作る，(8) 根を逆数へ移す相反多項式をとる，(9) 根の重心を0へ移す平行移動共役を施す，(10) 根を逆数へ移す相反多項式をとる，(11) 重複度付き根配置へ移す，(12) 根配置からモニック多項式を再構成する，(13) 臨界値を根にもつ消去多項式を作る，(14) 導関数をモニックに再正規化する，(15) 根の重心を0へ移す平行移動共役を施す，(16) 重複度付き根配置へ移す，(17) 根の冪和モーメント列を作る，(18) モーメントからHankel行列族を作る，(19) 主小行列式列をとる，(20) 満たす最小線形漸化式を抽出する，(21) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DerivativeRenormalization → GraeffeTransform → ReciprocalPolynomial → GraeffeTransform → ShiftConjugacy → GraeffeTransform → CriticalValuePolynomial → ReciprocalPolynomial → ShiftConjugacy → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → DerivativeRenormalization → ShiftConjugacy → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 凸体関手の合成力学（PolarDual・IntersectionBody・CentroidBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.b905b91493`
- 状態: `unresolved_by_mathos`
- 射数: `23`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `26`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 原点に関する極体をとる，(2) 交叉体をとる，(3) 射影体をとる，(4) 主慣性軸方向にSteiner対称化する，(5) 射影体をとる，(6) 交叉体をとる，(7) 差体をとる，(8) 主慣性軸方向にSteiner対称化する，(9) 交叉体をとる，(10) 主慣性軸方向にSteiner対称化する，(11) 原点に関する極体をとる，(12) 自身と極体のMinkowski和をとる，(13) 原点に関する極体をとる，(14) 差体をとる，(15) 重心体をとる，(16) 差体をとる，(17) 射影体をとる，(18) 自身と極体のMinkowski和をとる，(19) 重心体をとる，(20) 自身と極体のMinkowski和をとる，(21) 重心体をとる，(22) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `PolarDual → IntersectionBody → ProjectionBody → SteinerSymmetrization → ProjectionBody → IntersectionBody → DifferenceBody → SteinerSymmetrization → IntersectionBody → SteinerSymmetrization → PolarDual → MinkowskiPolarSum → PolarDual → DifferenceBody → CentroidBody → DifferenceBody → ProjectionBody → MinkowskiPolarSum → CentroidBody → MinkowskiPolarSum → CentroidBody → VolumeNormalization → ConvexFixedPointQuery`

### Markov関手と到達時刻不変量（TimeReversal・StateLumping・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.380201a12f`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `23`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 定常分布に関する時間反転をとる，(2) 自己同型軌道に沿って強 lumping する，(3) 自身との同期積連鎖を作る，(4) 恒等遷移との凸結合でlazy化する，(5) 自身との同期積連鎖を作る，(6) 恒等遷移との凸結合でlazy化する，(7) 正の固有関数によるDoob変換を施す，(8) 自己同型軌道に沿って強 lumping する，(9) 正の固有関数によるDoob変換を施す，(10) 自己同型軌道に沿って強 lumping する，(11) 自身との同期積連鎖を作る，(12) 正の固有関数によるDoob変換を施す，(13) 定常分布に関する時間反転をとる，(14) 恒等遷移との凸結合でlazy化する，(15) 指定集合で吸収させ過渡核をとる，(16) 過渡核のGreen作用素をとる，(17) 到達時刻の高次モーメント連立系を作る，(18) モーメント次数方向の漸化式を抽出する，(19) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `TimeReversal → StateLumping → ProductChain → LazyPerturbation → ProductChain → LazyPerturbation → DoobTransform → StateLumping → DoobTransform → StateLumping → ProductChain → DoobTransform → TimeReversal → LazyPerturbation → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 三角形変換の合成力学（CircumcenterMark・CevianTrace・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.62c6c8e8d0`
- 状態: `unresolved_by_mathos`
- 射数: `20`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 外心を標識点として付加する，(2) 標識点を通る三本のcevianの辺上の足をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 垂足三角形へ移す，(5) 重心を標識点として付加する，(6) 標識点から三辺への垂足三点をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 傍心三角形へ移す，(9) 垂心を標識点として付加する，(10) 標識点を三辺に関して反射した三点をとる，(11) 三点を頂点とする向き付き三角形を作る，(12) 反中点三角形へ移す，(13) 傍心三角形へ移す，(14) 反中点三角形へ移す，(15) 重心・面積・向きを固定して相似正規化する，(16) 相似類のモジュライ点へ射影する，(17) ここまでの合成が誘導する写像を反復する，(18) 退化三角形を境界として軌道をコンパクト化する，(19) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CircumcenterMark → CevianTrace → TriangleFormation → OrthicTransform → CentroidMark → PedalProjection → TriangleFormation → ExcentralTransform → OrthocenterMark → SideReflectionTrace → TriangleFormation → AnticomplementaryTransform → ExcentralTransform → AnticomplementaryTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 平面代数曲線の合成変換（IsogonalCremona・CircleInversion・OffsetCurve・Catacaustic）

- ID: `research.autonomous.plane_curve.0e233f8fa8`
- 状態: `unresolved_by_mathos`
- 射数: `23`
- 問い: `birational_periodicity`
- 難度仮説: `26`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定基準三角形に関する等角共役Cremona像をとる，(2) 原点中心の円反転像をとる，(3) 固定基準三角形に関する等角共役Cremona像をとる，(4) 射影閉包をとり無限遠点を加える，(5) 基点を避ける一般アフィンチャートへ移す，(6) 正則接線族の射影双対曲線をとる，(7) 固定光源からの反射光線族の包絡線をとる，(8) 正則接線族の射影双対曲線をとる，(9) 射影閉包をとり無限遠点を加える，(10) 基点を避ける一般アフィンチャートへ移す，(11) 法線族の包絡線である発展曲線をとる，(12) 法線方向の代数的平行曲線をとる，(13) 原点中心の円反転像をとる，(14) 射影閉包をとり無限遠点を加える，(15) 基点を避ける一般アフィンチャートへ移す，(16) 法線方向の代数的平行曲線をとる，(17) 定義多項式のHessian曲線をとる，(18) 法線族の包絡線である発展曲線をとる，(19) 固定非退化二次形式に関する極逆像をとる，(20) 法線族の包絡線である発展曲線をとる，(21) 法線方向の代数的平行曲線をとる，(22) 固定光源からの反射光線族の包絡線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IsogonalCremona → CircleInversion → IsogonalCremona → ProjectiveClosure → AffineChartChange → ProjectiveDual → Catacaustic → ProjectiveDual → ProjectiveClosure → AffineChartChange → Evolute → OffsetCurve → CircleInversion → ProjectiveClosure → AffineChartChange → OffsetCurve → HessianCurve → Evolute → PolarReciprocal → Evolute → OffsetCurve → Catacaustic → BirationalPeriodQuery`

### 多項式変換と算術観測（DerivativeRenormalization・RootMultiset・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.d8e69a4191`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `recurrence_order_drop`
- 難度仮説: `28`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 導関数をモニックに再正規化する，(2) 重複度付き根配置へ移す，(3) 根配置からモニック多項式を再構成する，(4) 根を逆数へ移す相反多項式をとる，(5) 根を二乗するGraeffe変換を施す，(6) 臨界値を根にもつ消去多項式を作る，(7) 根を逆数へ移す相反多項式をとる，(8) 重複度付き根配置へ移す，(9) 根配置からモニック多項式を再構成する，(10) 重複度付き根配置へ移す，(11) 根配置からモニック多項式を再構成する，(12) 根を逆数へ移す相反多項式をとる，(13) 臨界値を根にもつ消去多項式を作る，(14) 導関数をモニックに再正規化する，(15) 根の重心を0へ移す平行移動共役を施す，(16) 導関数をモニックに再正規化する，(17) 根の重心を0へ移す平行移動共役を施す，(18) 根を二乗するGraeffe変換を施す，(19) 重複度付き根配置へ移す，(20) 根の冪和モーメント列を作る，(21) モーメントからHankel行列族を作る，(22) 主小行列式列をとる，(23) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DerivativeRenormalization → RootMultiset → PolynomialReconstruction → ReciprocalPolynomial → GraeffeTransform → CriticalValuePolynomial → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → RootMultiset → PolynomialReconstruction → ReciprocalPolynomial → CriticalValuePolynomial → DerivativeRenormalization → ShiftConjugacy → DerivativeRenormalization → ShiftConjugacy → GraeffeTransform → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 凸体関手の合成力学（DifferenceBody・SteinerSymmetrization・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.888ccaec4c`
- 状態: `unresolved_by_mathos`
- 射数: `23`
- 問い: `convex_body_dynamics`
- 難度仮説: `27`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 差体をとる，(2) 主慣性軸方向にSteiner対称化する，(3) 原点に関する極体をとる，(4) 射影体をとる，(5) 自身と極体のMinkowski和をとる，(6) 重心体をとる，(7) 自身と極体のMinkowski和をとる，(8) 原点に関する極体をとる，(9) 自身と極体のMinkowski和をとる，(10) 射影体をとる，(11) 原点に関する極体をとる，(12) 主慣性軸方向にSteiner対称化する，(13) 射影体をとる，(14) 重心体をとる，(15) 交叉体をとる，(16) 重心体をとる，(17) 差体をとる，(18) 交叉体をとる，(19) 面積と二次モーメントを固定して正規化する，(20) ここまでの凸体関手を反復する，(21) 支持関数の軌道へ移す，(22) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DifferenceBody → SteinerSymmetrization → PolarDual → ProjectionBody → MinkowskiPolarSum → CentroidBody → MinkowskiPolarSum → PolarDual → MinkowskiPolarSum → ProjectionBody → PolarDual → SteinerSymmetrization → ProjectionBody → CentroidBody → IntersectionBody → CentroidBody → DifferenceBody → IntersectionBody → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 三角形変換の合成力学（ExcentralTransform・OrthocenterMark・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.64e673a512`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `29`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0625`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 傍心三角形へ移す，(2) 垂心を標識点として付加する，(3) 標識点を三辺に関して反射した三点をとる，(4) 三点を頂点とする向き付き三角形を作る，(5) 三辺の中点三角形へ移す，(6) 垂足三角形へ移す，(7) 内心を標識点として付加する，(8) 標識点を三辺に関して反射した三点をとる，(9) 三点を頂点とする向き付き三角形を作る，(10) 重心を標識点として付加する，(11) 標識点を通る三本のcevianの辺上の足をとる，(12) 三点を頂点とする向き付き三角形を作る，(13) 類似重心を標識点として付加する，(14) 標識点から三辺への垂足三点をとる，(15) 三点を頂点とする向き付き三角形を作る，(16) 三辺の中点三角形へ移す，(17) 垂足三角形へ移す，(18) 三辺の中点三角形へ移す，(19) 重心・面積・向きを固定して相似正規化する，(20) 相似類のモジュライ点へ射影する，(21) ここまでの合成が誘導する写像を反復する，(22) 退化三角形を境界として軌道をコンパクト化する，(23) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ExcentralTransform → OrthocenterMark → SideReflectionTrace → TriangleFormation → MedialTransform → OrthicTransform → IncenterMark → SideReflectionTrace → TriangleFormation → CentroidMark → CevianTrace → TriangleFormation → SymmedianMark → PedalProjection → TriangleFormation → MedialTransform → OrthicTransform → MedialTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### Markov関手と到達時刻不変量（DoobTransform・LazyPerturbation・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.937e23df5c`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 正の固有関数によるDoob変換を施す，(2) 恒等遷移との凸結合でlazy化する，(3) 定常分布に関する時間反転をとる，(4) 自身との同期積連鎖を作る，(5) 自己同型軌道に沿って強 lumping する，(6) 恒等遷移との凸結合でlazy化する，(7) 自身との同期積連鎖を作る，(8) 恒等遷移との凸結合でlazy化する，(9) 自己同型軌道に沿って強 lumping する，(10) 自身との同期積連鎖を作る，(11) 正の固有関数によるDoob変換を施す，(12) 自己同型軌道に沿って強 lumping する，(13) 定常分布に関する時間反転をとる，(14) 正の固有関数によるDoob変換を施す，(15) 定常分布に関する時間反転をとる，(16) 指定集合で吸収させ過渡核をとる，(17) 過渡核のGreen作用素をとる，(18) 到達時刻の高次モーメント連立系を作る，(19) モーメント次数方向の漸化式を抽出する，(20) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DoobTransform → LazyPerturbation → TimeReversal → ProductChain → StateLumping → LazyPerturbation → ProductChain → LazyPerturbation → StateLumping → ProductChain → DoobTransform → StateLumping → TimeReversal → DoobTransform → TimeReversal → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 多項式変換と算術観測（GraeffeTransform・RootMultiset・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.33afc2dd12`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を二乗するGraeffe変換を施す，(2) 重複度付き根配置へ移す，(3) 根配置からモニック多項式を再構成する，(4) 臨界値を根にもつ消去多項式を作る，(5) 根の重心を0へ移す平行移動共役を施す，(6) 重複度付き根配置へ移す，(7) 根配置からモニック多項式を再構成する，(8) 根の重心を0へ移す平行移動共役を施す，(9) 臨界値を根にもつ消去多項式を作る，(10) 根を二乗するGraeffe変換を施す，(11) 導関数をモニックに再正規化する，(12) 根の重心を0へ移す平行移動共役を施す，(13) 導関数をモニックに再正規化する，(14) 臨界値を根にもつ消去多項式を作る，(15) 重複度付き根配置へ移す，(16) 根の冪和モーメント列を作る，(17) モーメントからHankel行列族を作る，(18) 主小行列式列をとる，(19) 満たす最小線形漸化式を抽出する，(20) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `GraeffeTransform → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → ShiftConjugacy → RootMultiset → PolynomialReconstruction → ShiftConjugacy → CriticalValuePolynomial → GraeffeTransform → DerivativeRenormalization → ShiftConjugacy → DerivativeRenormalization → CriticalValuePolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 凸体関手の合成力学（DifferenceBody・IntersectionBody・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.fdc78cf930`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `convex_body_dynamics`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 差体をとる，(2) 交叉体をとる，(3) 差体をとる，(4) 射影体をとる，(5) 交叉体をとる，(6) 差体をとる，(7) 交叉体をとる，(8) 主慣性軸方向にSteiner対称化する，(9) 自身と極体のMinkowski和をとる，(10) 射影体をとる，(11) 主慣性軸方向にSteiner対称化する，(12) 射影体をとる，(13) 自身と極体のMinkowski和をとる，(14) 主慣性軸方向にSteiner対称化する，(15) 重心体をとる，(16) 自身と極体のMinkowski和をとる，(17) 面積と二次モーメントを固定して正規化する，(18) ここまでの凸体関手を反復する，(19) 支持関数の軌道へ移す，(20) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DifferenceBody → IntersectionBody → DifferenceBody → ProjectionBody → IntersectionBody → DifferenceBody → IntersectionBody → SteinerSymmetrization → MinkowskiPolarSum → ProjectionBody → SteinerSymmetrization → ProjectionBody → MinkowskiPolarSum → SteinerSymmetrization → CentroidBody → MinkowskiPolarSum → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 平面代数曲線の合成変換（PolarReciprocal・IsogonalCremona・HessianCurve・Catacaustic）

- ID: `research.autonomous.plane_curve.9ff2ad79b8`
- 状態: `unresolved_by_mathos`
- 射数: `22`
- 問い: `birational_periodicity`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定非退化二次形式に関する極逆像をとる，(2) 固定基準三角形に関する等角共役Cremona像をとる，(3) 法線方向の代数的平行曲線をとる，(4) 正則接線族の射影双対曲線をとる，(5) 射影閉包をとり無限遠点を加える，(6) 基点を避ける一般アフィンチャートへ移す，(7) 正則接線族の射影双対曲線をとる，(8) 射影閉包をとり無限遠点を加える，(9) 基点を避ける一般アフィンチャートへ移す，(10) 正則接線族の射影双対曲線をとる，(11) 法線方向の代数的平行曲線をとる，(12) 固定光源からの反射光線族の包絡線をとる，(13) 法線族の包絡線である発展曲線をとる，(14) 法線方向の代数的平行曲線をとる，(15) 原点中心の円反転像をとる，(16) 固定非退化二次形式に関する極逆像をとる，(17) 法線族の包絡線である発展曲線をとる，(18) 固定光源からの反射光線族の包絡線をとる，(19) 原点中心の円反転像をとる，(20) 定義多項式のHessian曲線をとる，(21) 固定光源からの反射光線族の包絡線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `PolarReciprocal → IsogonalCremona → OffsetCurve → ProjectiveDual → ProjectiveClosure → AffineChartChange → ProjectiveDual → ProjectiveClosure → AffineChartChange → ProjectiveDual → OffsetCurve → Catacaustic → Evolute → OffsetCurve → CircleInversion → PolarReciprocal → Evolute → Catacaustic → CircleInversion → HessianCurve → Catacaustic → BirationalPeriodQuery`

### 三角形変換の合成力学（OrthocenterMark・CevianTrace・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.a8e0adf9e0`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 垂心を標識点として付加する，(2) 標識点を通る三本のcevianの辺上の足をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 傍心三角形へ移す，(5) 内心を標識点として付加する，(6) 標識点を三辺に関して反射した三点をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 反中点三角形へ移す，(9) 傍心三角形へ移す，(10) 内心を標識点として付加する，(11) 標識点を通る三本のcevianの辺上の足をとる，(12) 三点を頂点とする向き付き三角形を作る，(13) 三辺の中点三角形へ移す，(14) 垂足三角形へ移す，(15) 反中点三角形へ移す，(16) 重心・面積・向きを固定して相似正規化する，(17) 相似類のモジュライ点へ射影する，(18) ここまでの合成が誘導する写像を反復する，(19) 退化三角形を境界として軌道をコンパクト化する，(20) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `OrthocenterMark → CevianTrace → TriangleFormation → ExcentralTransform → IncenterMark → SideReflectionTrace → TriangleFormation → AnticomplementaryTransform → ExcentralTransform → IncenterMark → CevianTrace → TriangleFormation → MedialTransform → OrthicTransform → AnticomplementaryTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### Markov関手と到達時刻不変量（StateLumping・LazyPerturbation・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.c65d1b4be2`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自己同型軌道に沿って強 lumping する，(2) 恒等遷移との凸結合でlazy化する，(3) 定常分布に関する時間反転をとる，(4) 正の固有関数によるDoob変換を施す，(5) 自身との同期積連鎖を作る，(6) 恒等遷移との凸結合でlazy化する，(7) 自己同型軌道に沿って強 lumping する，(8) 自身との同期積連鎖を作る，(9) 恒等遷移との凸結合でlazy化する，(10) 定常分布に関する時間反転をとる，(11) 自己同型軌道に沿って強 lumping する，(12) 定常分布に関する時間反転をとる，(13) 正の固有関数によるDoob変換を施す，(14) 自身との同期積連鎖を作る，(15) 正の固有関数によるDoob変換を施す，(16) 指定集合で吸収させ過渡核をとる，(17) 過渡核のGreen作用素をとる，(18) 到達時刻の高次モーメント連立系を作る，(19) モーメント次数方向の漸化式を抽出する，(20) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `StateLumping → LazyPerturbation → TimeReversal → DoobTransform → ProductChain → LazyPerturbation → StateLumping → ProductChain → LazyPerturbation → TimeReversal → StateLumping → TimeReversal → DoobTransform → ProductChain → DoobTransform → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 多項式変換と算術観測（ReciprocalPolynomial・GraeffeTransform・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.c681962540`
- 状態: `unresolved_by_mathos`
- 射数: `23`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `27`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を逆数へ移す相反多項式をとる，(2) 根を二乗するGraeffe変換を施す，(3) 根の重心を0へ移す平行移動共役を施す，(4) 重複度付き根配置へ移す，(5) 根配置からモニック多項式を再構成する，(6) 臨界値を根にもつ消去多項式を作る，(7) 根を逆数へ移す相反多項式をとる，(8) 根を二乗するGraeffe変換を施す，(9) 導関数をモニックに再正規化する，(10) 根を逆数へ移す相反多項式をとる，(11) 根を二乗するGraeffe変換を施す，(12) 重複度付き根配置へ移す，(13) 根配置からモニック多項式を再構成する，(14) 根の重心を0へ移す平行移動共役を施す，(15) 臨界値を根にもつ消去多項式を作る，(16) 導関数をモニックに再正規化する，(17) 重複度付き根配置へ移す，(18) 根の冪和モーメント列を作る，(19) モーメントからHankel行列族を作る，(20) 主小行列式列をとる，(21) 満たす最小線形漸化式を抽出する，(22) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ReciprocalPolynomial → GraeffeTransform → ShiftConjugacy → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → ReciprocalPolynomial → GraeffeTransform → DerivativeRenormalization → ReciprocalPolynomial → GraeffeTransform → RootMultiset → PolynomialReconstruction → ShiftConjugacy → CriticalValuePolynomial → DerivativeRenormalization → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 凸体関手の合成力学（CentroidBody・IntersectionBody・SteinerSymmetrization・VolumeNormalization）

- ID: `research.autonomous.convex_body.8c24c7c474`
- 状態: `unresolved_by_mathos`
- 射数: `22`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重心体をとる，(2) 交叉体をとる，(3) 射影体をとる，(4) 自身と極体のMinkowski和をとる，(5) 射影体をとる，(6) 原点に関する極体をとる，(7) 差体をとる，(8) 原点に関する極体をとる，(9) 差体をとる，(10) 原点に関する極体をとる，(11) 交叉体をとる，(12) 重心体をとる，(13) 自身と極体のMinkowski和をとる，(14) 差体をとる，(15) 自身と極体のMinkowski和をとる，(16) 重心体をとる，(17) 主慣性軸方向にSteiner対称化する，(18) 射影体をとる，(19) 交叉体をとる，(20) 主慣性軸方向にSteiner対称化する，(21) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CentroidBody → IntersectionBody → ProjectionBody → MinkowskiPolarSum → ProjectionBody → PolarDual → DifferenceBody → PolarDual → DifferenceBody → PolarDual → IntersectionBody → CentroidBody → MinkowskiPolarSum → DifferenceBody → MinkowskiPolarSum → CentroidBody → SteinerSymmetrization → ProjectionBody → IntersectionBody → SteinerSymmetrization → VolumeNormalization → ConvexFixedPointQuery`

### 平面代数曲線の合成変換（IsogonalCremona・HessianCurve・CircleInversion・ProjectiveDual）

- ID: `research.autonomous.plane_curve.67ecb7cfd0`
- 状態: `unresolved_by_mathos`
- 射数: `23`
- 問い: `birational_periodicity`
- 難度仮説: `26`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定基準三角形に関する等角共役Cremona像をとる，(2) 定義多項式のHessian曲線をとる，(3) 原点中心の円反転像をとる，(4) 法線族の包絡線である発展曲線をとる，(5) 固定基準三角形に関する等角共役Cremona像をとる，(6) 法線方向の代数的平行曲線をとる，(7) 固定非退化二次形式に関する極逆像をとる，(8) 固定基準三角形に関する等角共役Cremona像をとる，(9) 射影閉包をとり無限遠点を加える，(10) 基点を避ける一般アフィンチャートへ移す，(11) 法線族の包絡線である発展曲線をとる，(12) 定義多項式のHessian曲線をとる，(13) 法線族の包絡線である発展曲線をとる，(14) 固定非退化二次形式に関する極逆像をとる，(15) 正則接線族の射影双対曲線をとる，(16) 定義多項式のHessian曲線をとる，(17) 法線方向の代数的平行曲線をとる，(18) 射影閉包をとり無限遠点を加える，(19) 基点を避ける一般アフィンチャートへ移す，(20) 固定光源からの反射光線族の包絡線をとる，(21) 原点中心の円反転像をとる，(22) 正則接線族の射影双対曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IsogonalCremona → HessianCurve → CircleInversion → Evolute → IsogonalCremona → OffsetCurve → PolarReciprocal → IsogonalCremona → ProjectiveClosure → AffineChartChange → Evolute → HessianCurve → Evolute → PolarReciprocal → ProjectiveDual → HessianCurve → OffsetCurve → ProjectiveClosure → AffineChartChange → Catacaustic → CircleInversion → ProjectiveDual → BirationalPeriodQuery`

### Markov関手と到達時刻不変量（LazyPerturbation・DoobTransform・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.9433ca9d5c`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 恒等遷移との凸結合でlazy化する，(2) 正の固有関数によるDoob変換を施す，(3) 自己同型軌道に沿って強 lumping する，(4) 定常分布に関する時間反転をとる，(5) 自身との同期積連鎖を作る，(6) 定常分布に関する時間反転をとる，(7) 正の固有関数によるDoob変換を施す，(8) 恒等遷移との凸結合でlazy化する，(9) 定常分布に関する時間反転をとる，(10) 自身との同期積連鎖を作る，(11) 自己同型軌道に沿って強 lumping する，(12) 正の固有関数によるDoob変換を施す，(13) 自己同型軌道に沿って強 lumping する，(14) 自身との同期積連鎖を作る，(15) 恒等遷移との凸結合でlazy化する，(16) 指定集合で吸収させ過渡核をとる，(17) 過渡核のGreen作用素をとる，(18) 到達時刻の高次モーメント連立系を作る，(19) モーメント次数方向の漸化式を抽出する，(20) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `LazyPerturbation → DoobTransform → StateLumping → TimeReversal → ProductChain → TimeReversal → DoobTransform → LazyPerturbation → TimeReversal → ProductChain → StateLumping → DoobTransform → StateLumping → ProductChain → LazyPerturbation → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 三角形変換の合成力学（MedialTransform・OrthocenterMark・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.48b81438db`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 三辺の中点三角形へ移す，(2) 垂心を標識点として付加する，(3) 標識点を通る三本のcevianの辺上の足をとる，(4) 三点を頂点とする向き付き三角形を作る，(5) 類似重心を標識点として付加する，(6) 標識点を三辺に関して反射した三点をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 傍心三角形へ移す，(9) 類似重心を標識点として付加する，(10) 標識点を通る三本のcevianの辺上の足をとる，(11) 三点を頂点とする向き付き三角形を作る，(12) 反中点三角形へ移す，(13) 垂足三角形へ移す，(14) 三辺の中点三角形へ移す，(15) 傍心三角形へ移す，(16) 重心・面積・向きを固定して相似正規化する，(17) 相似類のモジュライ点へ射影する，(18) ここまでの合成が誘導する写像を反復する，(19) 退化三角形を境界として軌道をコンパクト化する，(20) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `MedialTransform → OrthocenterMark → CevianTrace → TriangleFormation → SymmedianMark → SideReflectionTrace → TriangleFormation → ExcentralTransform → SymmedianMark → CevianTrace → TriangleFormation → AnticomplementaryTransform → OrthicTransform → MedialTransform → ExcentralTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 凸体関手の合成力学（SteinerSymmetrization・PolarDual・IntersectionBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.f085b3f44a`
- 状態: `unresolved_by_mathos`
- 射数: `23`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `26`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 主慣性軸方向にSteiner対称化する，(2) 原点に関する極体をとる，(3) 差体をとる，(4) 原点に関する極体をとる，(5) 自身と極体のMinkowski和をとる，(6) 差体をとる，(7) 原点に関する極体をとる，(8) 主慣性軸方向にSteiner対称化する，(9) 自身と極体のMinkowski和をとる，(10) 射影体をとる，(11) 重心体をとる，(12) 自身と極体のMinkowski和をとる，(13) 差体をとる，(14) 主慣性軸方向にSteiner対称化する，(15) 重心体をとる，(16) 射影体をとる，(17) 交叉体をとる，(18) 重心体をとる，(19) 交叉体をとる，(20) 射影体をとる，(21) 交叉体をとる，(22) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `SteinerSymmetrization → PolarDual → DifferenceBody → PolarDual → MinkowskiPolarSum → DifferenceBody → PolarDual → SteinerSymmetrization → MinkowskiPolarSum → ProjectionBody → CentroidBody → MinkowskiPolarSum → DifferenceBody → SteinerSymmetrization → CentroidBody → ProjectionBody → IntersectionBody → CentroidBody → IntersectionBody → ProjectionBody → IntersectionBody → VolumeNormalization → ConvexFixedPointQuery`

### 多項式変換と算術観測（CriticalValuePolynomial・GraeffeTransform・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.f94249c6cd`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 臨界値を根にもつ消去多項式を作る，(2) 根を二乗するGraeffe変換を施す，(3) 根の重心を0へ移す平行移動共役を施す，(4) 根を逆数へ移す相反多項式をとる，(5) 根の重心を0へ移す平行移動共役を施す，(6) 重複度付き根配置へ移す，(7) 根配置からモニック多項式を再構成する，(8) 臨界値を根にもつ消去多項式を作る，(9) 根を二乗するGraeffe変換を施す，(10) 重複度付き根配置へ移す，(11) 根配置からモニック多項式を再構成する，(12) 根を二乗するGraeffe変換を施す，(13) 臨界値を根にもつ消去多項式を作る，(14) 導関数をモニックに再正規化する，(15) 重複度付き根配置へ移す，(16) 根の冪和モーメント列を作る，(17) モーメントからHankel行列族を作る，(18) 主小行列式列をとる，(19) 満たす最小線形漸化式を抽出する，(20) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CriticalValuePolynomial → GraeffeTransform → ShiftConjugacy → ReciprocalPolynomial → ShiftConjugacy → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → GraeffeTransform → RootMultiset → PolynomialReconstruction → GraeffeTransform → CriticalValuePolynomial → DerivativeRenormalization → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 平面代数曲線の合成変換（HessianCurve・ProjectiveDual・IsogonalCremona・PolarReciprocal）

- ID: `research.autonomous.plane_curve.4557e9eb74`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `birational_periodicity`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 定義多項式のHessian曲線をとる，(2) 正則接線族の射影双対曲線をとる，(3) 固定非退化二次形式に関する極逆像をとる，(4) 法線方向の代数的平行曲線をとる，(5) 射影閉包をとり無限遠点を加える，(6) 基点を避ける一般アフィンチャートへ移す，(7) 法線方向の代数的平行曲線をとる，(8) 原点中心の円反転像をとる，(9) 定義多項式のHessian曲線をとる，(10) 法線方向の代数的平行曲線をとる，(11) 正則接線族の射影双対曲線をとる，(12) 射影閉包をとり無限遠点を加える，(13) 基点を避ける一般アフィンチャートへ移す，(14) 定義多項式のHessian曲線をとる，(15) 法線族の包絡線である発展曲線をとる，(16) 射影閉包をとり無限遠点を加える，(17) 基点を避ける一般アフィンチャートへ移す，(18) 固定非退化二次形式に関する極逆像をとる，(19) 固定基準三角形に関する等角共役Cremona像をとる，(20) 固定非退化二次形式に関する極逆像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `HessianCurve → ProjectiveDual → PolarReciprocal → OffsetCurve → ProjectiveClosure → AffineChartChange → OffsetCurve → CircleInversion → HessianCurve → OffsetCurve → ProjectiveDual → ProjectiveClosure → AffineChartChange → HessianCurve → Evolute → ProjectiveClosure → AffineChartChange → PolarReciprocal → IsogonalCremona → PolarReciprocal → BirationalPeriodQuery`

### Markov関手と到達時刻不変量（StateLumping・ProductChain・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.ccb5cfffe0`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自己同型軌道に沿って強 lumping する，(2) 自身との同期積連鎖を作る，(3) 自己同型軌道に沿って強 lumping する，(4) 正の固有関数によるDoob変換を施す，(5) 定常分布に関する時間反転をとる，(6) 恒等遷移との凸結合でlazy化する，(7) 自身との同期積連鎖を作る，(8) 正の固有関数によるDoob変換を施す，(9) 自己同型軌道に沿って強 lumping する，(10) 恒等遷移との凸結合でlazy化する，(11) 正の固有関数によるDoob変換を施す，(12) 自身との同期積連鎖を作る，(13) 定常分布に関する時間反転をとる，(14) 恒等遷移との凸結合でlazy化する，(15) 定常分布に関する時間反転をとる，(16) 指定集合で吸収させ過渡核をとる，(17) 過渡核のGreen作用素をとる，(18) 到達時刻の高次モーメント連立系を作る，(19) モーメント次数方向の漸化式を抽出する，(20) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `StateLumping → ProductChain → StateLumping → DoobTransform → TimeReversal → LazyPerturbation → ProductChain → DoobTransform → StateLumping → LazyPerturbation → DoobTransform → ProductChain → TimeReversal → LazyPerturbation → TimeReversal → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 三角形変換の合成力学（CircumcenterMark・CevianTrace・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.ca793ee9f6`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `28`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0625`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 外心を標識点として付加する，(2) 標識点を通る三本のcevianの辺上の足をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 垂足三角形へ移す，(5) 類似重心を標識点として付加する，(6) 標識点を三辺に関して反射した三点をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 三辺の中点三角形へ移す，(9) 傍心三角形へ移す，(10) 三辺の中点三角形へ移す，(11) 類似重心を標識点として付加する，(12) 標識点から三辺への垂足三点をとる，(13) 三点を頂点とする向き付き三角形を作る，(14) 三辺の中点三角形へ移す，(15) 外心を標識点として付加する，(16) 標識点から三辺への垂足三点をとる，(17) 三点を頂点とする向き付き三角形を作る，(18) 垂足三角形へ移す，(19) 重心・面積・向きを固定して相似正規化する，(20) 相似類のモジュライ点へ射影する，(21) ここまでの合成が誘導する写像を反復する，(22) 退化三角形を境界として軌道をコンパクト化する，(23) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CircumcenterMark → CevianTrace → TriangleFormation → OrthicTransform → SymmedianMark → SideReflectionTrace → TriangleFormation → MedialTransform → ExcentralTransform → MedialTransform → SymmedianMark → PedalProjection → TriangleFormation → MedialTransform → CircumcenterMark → PedalProjection → TriangleFormation → OrthicTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 凸体関手の合成力学（IntersectionBody・DifferenceBody・MinkowskiPolarSum・VolumeNormalization）

- ID: `research.autonomous.convex_body.6b8fba2b78`
- 状態: `unresolved_by_mathos`
- 射数: `22`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 交叉体をとる，(2) 差体をとる，(3) 主慣性軸方向にSteiner対称化する，(4) 射影体をとる，(5) 原点に関する極体をとる，(6) 射影体をとる，(7) 主慣性軸方向にSteiner対称化する，(8) 差体をとる，(9) 原点に関する極体をとる，(10) 主慣性軸方向にSteiner対称化する，(11) 自身と極体のMinkowski和をとる，(12) 交叉体をとる，(13) 差体をとる，(14) 射影体をとる，(15) 重心体をとる，(16) 自身と極体のMinkowski和をとる，(17) 重心体をとる，(18) 原点に関する極体をとる，(19) 交叉体をとる，(20) 自身と極体のMinkowski和をとる，(21) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IntersectionBody → DifferenceBody → SteinerSymmetrization → ProjectionBody → PolarDual → ProjectionBody → SteinerSymmetrization → DifferenceBody → PolarDual → SteinerSymmetrization → MinkowskiPolarSum → IntersectionBody → DifferenceBody → ProjectionBody → CentroidBody → MinkowskiPolarSum → CentroidBody → PolarDual → IntersectionBody → MinkowskiPolarSum → VolumeNormalization → ConvexFixedPointQuery`

### 多項式変換と算術観測（CriticalValuePolynomial・DerivativeRenormalization・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.adc25c70b9`
- 状態: `unresolved_by_mathos`
- 射数: `23`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `27`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 臨界値を根にもつ消去多項式を作る，(2) 導関数をモニックに再正規化する，(3) 根の重心を0へ移す平行移動共役を施す，(4) 根を二乗するGraeffe変換を施す，(5) 重複度付き根配置へ移す，(6) 根配置からモニック多項式を再構成する，(7) 根の重心を0へ移す平行移動共役を施す，(8) 根を逆数へ移す相反多項式をとる，(9) 導関数をモニックに再正規化する，(10) 根を二乗するGraeffe変換を施す，(11) 重複度付き根配置へ移す，(12) 根配置からモニック多項式を再構成する，(13) 根の重心を0へ移す平行移動共役を施す，(14) 根を逆数へ移す相反多項式をとる，(15) 根を二乗するGraeffe変換を施す，(16) 導関数をモニックに再正規化する，(17) 重複度付き根配置へ移す，(18) 根の冪和モーメント列を作る，(19) モーメントからHankel行列族を作る，(20) 主小行列式列をとる，(21) 満たす最小線形漸化式を抽出する，(22) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CriticalValuePolynomial → DerivativeRenormalization → ShiftConjugacy → GraeffeTransform → RootMultiset → PolynomialReconstruction → ShiftConjugacy → ReciprocalPolynomial → DerivativeRenormalization → GraeffeTransform → RootMultiset → PolynomialReconstruction → ShiftConjugacy → ReciprocalPolynomial → GraeffeTransform → DerivativeRenormalization → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 平面代数曲線の合成変換（Evolute・HessianCurve・AffineChartChange・CircleInversion）

- ID: `research.autonomous.plane_curve.0c8d471301`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `birational_periodicity`
- 難度仮説: `27`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 法線族の包絡線である発展曲線をとる，(2) 定義多項式のHessian曲線をとる，(3) 固定基準三角形に関する等角共役Cremona像をとる，(4) 固定光源からの反射光線族の包絡線をとる，(5) 定義多項式のHessian曲線をとる，(6) 正則接線族の射影双対曲線をとる，(7) 法線方向の代数的平行曲線をとる，(8) 固定非退化二次形式に関する極逆像をとる，(9) 法線族の包絡線である発展曲線をとる，(10) 定義多項式のHessian曲線をとる，(11) 原点中心の円反転像をとる，(12) 固定光源からの反射光線族の包絡線をとる，(13) 固定基準三角形に関する等角共役Cremona像をとる，(14) 正則接線族の射影双対曲線をとる，(15) 原点中心の円反転像をとる，(16) 射影閉包をとり無限遠点を加える，(17) 基点を避ける一般アフィンチャートへ移す，(18) 法線方向の代数的平行曲線をとる，(19) 固定基準三角形に関する等角共役Cremona像をとる，(20) 原点中心の円反転像をとる，(21) 射影閉包をとり無限遠点を加える，(22) 基点を避ける一般アフィンチャートへ移す，(23) 原点中心の円反転像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `Evolute → HessianCurve → IsogonalCremona → Catacaustic → HessianCurve → ProjectiveDual → OffsetCurve → PolarReciprocal → Evolute → HessianCurve → CircleInversion → Catacaustic → IsogonalCremona → ProjectiveDual → CircleInversion → ProjectiveClosure → AffineChartChange → OffsetCurve → IsogonalCremona → CircleInversion → ProjectiveClosure → AffineChartChange → CircleInversion → BirationalPeriodQuery`

### Markov関手と到達時刻不変量（LazyPerturbation・DoobTransform・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.97a6c0a173`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `24`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 恒等遷移との凸結合でlazy化する，(2) 正の固有関数によるDoob変換を施す，(3) 自己同型軌道に沿って強 lumping する，(4) 正の固有関数によるDoob変換を施す，(5) 自身との同期積連鎖を作る，(6) 恒等遷移との凸結合でlazy化する，(7) 定常分布に関する時間反転をとる，(8) 自己同型軌道に沿って強 lumping する，(9) 自身との同期積連鎖を作る，(10) 正の固有関数によるDoob変換を施す，(11) 定常分布に関する時間反転をとる，(12) 自身との同期積連鎖を作る，(13) 自己同型軌道に沿って強 lumping する，(14) 定常分布に関する時間反転をとる，(15) 恒等遷移との凸結合でlazy化する，(16) 指定集合で吸収させ過渡核をとる，(17) 過渡核のGreen作用素をとる，(18) 到達時刻の高次モーメント連立系を作る，(19) モーメント次数方向の漸化式を抽出する，(20) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `LazyPerturbation → DoobTransform → StateLumping → DoobTransform → ProductChain → LazyPerturbation → TimeReversal → StateLumping → ProductChain → DoobTransform → TimeReversal → ProductChain → StateLumping → TimeReversal → LazyPerturbation → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 三角形変換の合成力学（OrthicTransform・IncenterMark・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.7b06177d60`
- 状態: `unresolved_by_mathos`
- 射数: `21`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 垂足三角形へ移す，(2) 内心を標識点として付加する，(3) 標識点を通る三本のcevianの辺上の足をとる，(4) 三点を頂点とする向き付き三角形を作る，(5) 垂足三角形へ移す，(6) 三辺の中点三角形へ移す，(7) 類似重心を標識点として付加する，(8) 標識点を通る三本のcevianの辺上の足をとる，(9) 三点を頂点とする向き付き三角形を作る，(10) 反中点三角形へ移す，(11) 垂心を標識点として付加する，(12) 標識点を三辺に関して反射した三点をとる，(13) 三点を頂点とする向き付き三角形を作る，(14) 垂足三角形へ移す，(15) 三辺の中点三角形へ移す，(16) 重心・面積・向きを固定して相似正規化する，(17) 相似類のモジュライ点へ射影する，(18) ここまでの合成が誘導する写像を反復する，(19) 退化三角形を境界として軌道をコンパクト化する，(20) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `OrthicTransform → IncenterMark → CevianTrace → TriangleFormation → OrthicTransform → MedialTransform → SymmedianMark → CevianTrace → TriangleFormation → AnticomplementaryTransform → OrthocenterMark → SideReflectionTrace → TriangleFormation → OrthicTransform → MedialTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 平面代数曲線の合成変換（OffsetCurve・IsogonalCremona・HessianCurve・CircleInversion）

- ID: `research.autonomous.plane_curve.5e88cbc4c7`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `birational_periodicity`
- 難度仮説: `28`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 法線方向の代数的平行曲線をとる，(2) 固定基準三角形に関する等角共役Cremona像をとる，(3) 固定光源からの反射光線族の包絡線をとる，(4) 定義多項式のHessian曲線をとる，(5) 射影閉包をとり無限遠点を加える，(6) 基点を避ける一般アフィンチャートへ移す，(7) 法線族の包絡線である発展曲線をとる，(8) 定義多項式のHessian曲線をとる，(9) 原点中心の円反転像をとる，(10) 固定非退化二次形式に関する極逆像をとる，(11) 射影閉包をとり無限遠点を加える，(12) 基点を避ける一般アフィンチャートへ移す，(13) 法線方向の代数的平行曲線をとる，(14) 正則接線族の射影双対曲線をとる，(15) 固定非退化二次形式に関する極逆像をとる，(16) 定義多項式のHessian曲線をとる，(17) 法線方向の代数的平行曲線をとる，(18) 固定基準三角形に関する等角共役Cremona像をとる，(19) 固定非退化二次形式に関する極逆像をとる，(20) 射影閉包をとり無限遠点を加える，(21) 基点を避ける一般アフィンチャートへ移す，(22) 固定非退化二次形式に関する極逆像をとる，(23) 定義多項式のHessian曲線をとる，(24) 原点中心の円反転像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `OffsetCurve → IsogonalCremona → Catacaustic → HessianCurve → ProjectiveClosure → AffineChartChange → Evolute → HessianCurve → CircleInversion → PolarReciprocal → ProjectiveClosure → AffineChartChange → OffsetCurve → ProjectiveDual → PolarReciprocal → HessianCurve → OffsetCurve → IsogonalCremona → PolarReciprocal → ProjectiveClosure → AffineChartChange → PolarReciprocal → HessianCurve → CircleInversion → BirationalPeriodQuery`

### 多項式変換と算術観測（ShiftConjugacy・GraeffeTransform・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.27f66753e0`
- 状態: `unresolved_by_mathos`
- 射数: `22`
- 問い: `recurrence_order_drop`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根の重心を0へ移す平行移動共役を施す，(2) 根を二乗するGraeffe変換を施す，(3) 臨界値を根にもつ消去多項式を作る，(4) 重複度付き根配置へ移す，(5) 根配置からモニック多項式を再構成する，(6) 根の重心を0へ移す平行移動共役を施す，(7) 臨界値を根にもつ消去多項式を作る，(8) 導関数をモニックに再正規化する，(9) 根の重心を0へ移す平行移動共役を施す，(10) 臨界値を根にもつ消去多項式を作る，(11) 導関数をモニックに再正規化する，(12) 根を二乗するGraeffe変換を施す，(13) 導関数をモニックに再正規化する，(14) 重複度付き根配置へ移す，(15) 根配置からモニック多項式を再構成する，(16) 根を二乗するGraeffe変換を施す，(17) 重複度付き根配置へ移す，(18) 根の冪和モーメント列を作る，(19) モーメントからHankel行列族を作る，(20) 主小行列式列をとる，(21) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ShiftConjugacy → GraeffeTransform → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → ShiftConjugacy → CriticalValuePolynomial → DerivativeRenormalization → ShiftConjugacy → CriticalValuePolynomial → DerivativeRenormalization → GraeffeTransform → DerivativeRenormalization → RootMultiset → PolynomialReconstruction → GraeffeTransform → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 凸体関手の合成力学（CentroidBody・IntersectionBody・DifferenceBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.a78c4088b4`
- 状態: `unresolved_by_mathos`
- 射数: `22`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重心体をとる，(2) 交叉体をとる，(3) 重心体をとる，(4) 交叉体をとる，(5) 自身と極体のMinkowski和をとる，(6) 交叉体をとる，(7) 原点に関する極体をとる，(8) 射影体をとる，(9) 自身と極体のMinkowski和をとる，(10) 主慣性軸方向にSteiner対称化する，(11) 差体をとる，(12) 自身と極体のMinkowski和をとる，(13) 主慣性軸方向にSteiner対称化する，(14) 射影体をとる，(15) 重心体をとる，(16) 原点に関する極体をとる，(17) 差体をとる，(18) 主慣性軸方向にSteiner対称化する，(19) 射影体をとる，(20) 差体をとる，(21) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CentroidBody → IntersectionBody → CentroidBody → IntersectionBody → MinkowskiPolarSum → IntersectionBody → PolarDual → ProjectionBody → MinkowskiPolarSum → SteinerSymmetrization → DifferenceBody → MinkowskiPolarSum → SteinerSymmetrization → ProjectionBody → CentroidBody → PolarDual → DifferenceBody → SteinerSymmetrization → ProjectionBody → DifferenceBody → VolumeNormalization → ConvexFixedPointQuery`

### Markov関手と到達時刻不変量（TimeReversal・StateLumping・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.6cbbb9fe11`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `27`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 定常分布に関する時間反転をとる，(2) 自己同型軌道に沿って強 lumping する，(3) 定常分布に関する時間反転をとる，(4) 自身との同期積連鎖を作る，(5) 自己同型軌道に沿って強 lumping する，(6) 定常分布に関する時間反転をとる，(7) 自己同型軌道に沿って強 lumping する，(8) 恒等遷移との凸結合でlazy化する，(9) 自身との同期積連鎖を作る，(10) 恒等遷移との凸結合でlazy化する，(11) 自己同型軌道に沿って強 lumping する，(12) 恒等遷移との凸結合でlazy化する，(13) 定常分布に関する時間反転をとる，(14) 正の固有関数によるDoob変換を施す，(15) 恒等遷移との凸結合でlazy化する，(16) 自身との同期積連鎖を作る，(17) 正の固有関数によるDoob変換を施す，(18) 自身との同期積連鎖を作る，(19) 正の固有関数によるDoob変換を施す，(20) 指定集合で吸収させ過渡核をとる，(21) 過渡核のGreen作用素をとる，(22) 到達時刻の高次モーメント連立系を作る，(23) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `TimeReversal → StateLumping → TimeReversal → ProductChain → StateLumping → TimeReversal → StateLumping → LazyPerturbation → ProductChain → LazyPerturbation → StateLumping → LazyPerturbation → TimeReversal → DoobTransform → LazyPerturbation → ProductChain → DoobTransform → ProductChain → DoobTransform → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 三角形変換の合成力学（OrthicTransform・MedialTransform・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.360a204a12`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `29`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0625`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 垂足三角形へ移す，(2) 三辺の中点三角形へ移す，(3) 内心を標識点として付加する，(4) 標識点から三辺への垂足三点をとる，(5) 三点を頂点とする向き付き三角形を作る，(6) 外心を標識点として付加する，(7) 標識点を通る三本のcevianの辺上の足をとる，(8) 三点を頂点とする向き付き三角形を作る，(9) 垂心を標識点として付加する，(10) 標識点を三辺に関して反射した三点をとる，(11) 三点を頂点とする向き付き三角形を作る，(12) 外心を標識点として付加する，(13) 各頂点と標識点が定める円の対応交点をとる，(14) 三点を頂点とする向き付き三角形を作る，(15) 垂足三角形へ移す，(16) 反中点三角形へ移す，(17) 垂足三角形へ移す，(18) 反中点三角形へ移す，(19) 重心・面積・向きを固定して相似正規化する，(20) 相似類のモジュライ点へ射影する，(21) ここまでの合成が誘導する写像を反復する，(22) 退化三角形を境界として軌道をコンパクト化する，(23) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `OrthicTransform → MedialTransform → IncenterMark → PedalProjection → TriangleFormation → CircumcenterMark → CevianTrace → TriangleFormation → OrthocenterMark → SideReflectionTrace → TriangleFormation → CircumcenterMark → VertexCircleTrace → TriangleFormation → OrthicTransform → AnticomplementaryTransform → OrthicTransform → AnticomplementaryTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 多項式変換と算術観測（ReciprocalPolynomial・GraeffeTransform・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.9dcd193d24`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `recurrence_order_drop`
- 難度仮説: `28`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を逆数へ移す相反多項式をとる，(2) 根を二乗するGraeffe変換を施す，(3) 臨界値を根にもつ消去多項式を作る，(4) 重複度付き根配置へ移す，(5) 根配置からモニック多項式を再構成する，(6) 重複度付き根配置へ移す，(7) 根配置からモニック多項式を再構成する，(8) 根を二乗するGraeffe変換を施す，(9) 根の重心を0へ移す平行移動共役を施す，(10) 導関数をモニックに再正規化する，(11) 根の重心を0へ移す平行移動共役を施す，(12) 根を二乗するGraeffe変換を施す，(13) 導関数をモニックに再正規化する，(14) 根を逆数へ移す相反多項式をとる，(15) 根を二乗するGraeffe変換を施す，(16) 根を逆数へ移す相反多項式をとる，(17) 導関数をモニックに再正規化する，(18) 根の重心を0へ移す平行移動共役を施す，(19) 重複度付き根配置へ移す，(20) 根の冪和モーメント列を作る，(21) モーメントからHankel行列族を作る，(22) 主小行列式列をとる，(23) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ReciprocalPolynomial → GraeffeTransform → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → RootMultiset → PolynomialReconstruction → GraeffeTransform → ShiftConjugacy → DerivativeRenormalization → ShiftConjugacy → GraeffeTransform → DerivativeRenormalization → ReciprocalPolynomial → GraeffeTransform → ReciprocalPolynomial → DerivativeRenormalization → ShiftConjugacy → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 平面代数曲線の合成変換（OffsetCurve・HessianCurve・IsogonalCremona・CircleInversion）

- ID: `research.autonomous.plane_curve.f405d2ff34`
- 状態: `unresolved_by_mathos`
- 射数: `22`
- 問い: `birational_periodicity`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 法線方向の代数的平行曲線をとる，(2) 定義多項式のHessian曲線をとる，(3) 固定光源からの反射光線族の包絡線をとる，(4) 原点中心の円反転像をとる，(5) 固定非退化二次形式に関する極逆像をとる，(6) 法線族の包絡線である発展曲線をとる，(7) 固定光源からの反射光線族の包絡線をとる，(8) 法線族の包絡線である発展曲線をとる，(9) 正則接線族の射影双対曲線をとる，(10) 射影閉包をとり無限遠点を加える，(11) 基点を避ける一般アフィンチャートへ移す，(12) 固定光源からの反射光線族の包絡線をとる，(13) 法線方向の代数的平行曲線をとる，(14) 法線族の包絡線である発展曲線をとる，(15) 射影閉包をとり無限遠点を加える，(16) 基点を避ける一般アフィンチャートへ移す，(17) 定義多項式のHessian曲線をとる，(18) 原点中心の円反転像をとる，(19) 定義多項式のHessian曲線をとる，(20) 固定基準三角形に関する等角共役Cremona像をとる，(21) 原点中心の円反転像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `OffsetCurve → HessianCurve → Catacaustic → CircleInversion → PolarReciprocal → Evolute → Catacaustic → Evolute → ProjectiveDual → ProjectiveClosure → AffineChartChange → Catacaustic → OffsetCurve → Evolute → ProjectiveClosure → AffineChartChange → HessianCurve → CircleInversion → HessianCurve → IsogonalCremona → CircleInversion → BirationalPeriodQuery`

### 凸体関手の合成力学（MinkowskiPolarSum・CentroidBody・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.795f200ce8`
- 状態: `unresolved_by_mathos`
- 射数: `23`
- 問い: `convex_body_dynamics`
- 難度仮説: `27`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身と極体のMinkowski和をとる，(2) 重心体をとる，(3) 自身と極体のMinkowski和をとる，(4) 原点に関する極体をとる，(5) 差体をとる，(6) 主慣性軸方向にSteiner対称化する，(7) 原点に関する極体をとる，(8) 射影体をとる，(9) 差体をとる，(10) 重心体をとる，(11) 自身と極体のMinkowski和をとる，(12) 重心体をとる，(13) 主慣性軸方向にSteiner対称化する，(14) 射影体をとる，(15) 原点に関する極体をとる，(16) 主慣性軸方向にSteiner対称化する，(17) 差体をとる，(18) 交叉体をとる，(19) 面積と二次モーメントを固定して正規化する，(20) ここまでの凸体関手を反復する，(21) 支持関数の軌道へ移す，(22) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `MinkowskiPolarSum → CentroidBody → MinkowskiPolarSum → PolarDual → DifferenceBody → SteinerSymmetrization → PolarDual → ProjectionBody → DifferenceBody → CentroidBody → MinkowskiPolarSum → CentroidBody → SteinerSymmetrization → ProjectionBody → PolarDual → SteinerSymmetrization → DifferenceBody → IntersectionBody → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 三角形変換の合成力学（AnticomplementaryTransform・IncenterMark・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.1a2954d2ac`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 反中点三角形へ移す，(2) 内心を標識点として付加する，(3) 標識点を三辺に関して反射した三点をとる，(4) 三点を頂点とする向き付き三角形を作る，(5) 類似重心を標識点として付加する，(6) 標識点を通る三本のcevianの辺上の足をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 内心を標識点として付加する，(9) 標識点から三辺への垂足三点をとる，(10) 三点を頂点とする向き付き三角形を作る，(11) 垂足三角形へ移す，(12) 重心を標識点として付加する，(13) 標識点から三辺への垂足三点をとる，(14) 三点を頂点とする向き付き三角形を作る，(15) 垂足三角形へ移す，(16) 反中点三角形へ移す，(17) 傍心三角形へ移す，(18) 反中点三角形へ移す，(19) 傍心三角形へ移す，(20) 重心・面積・向きを固定して相似正規化する，(21) 相似類のモジュライ点へ射影する，(22) ここまでの合成が誘導する写像を反復する，(23) 退化三角形を境界として軌道をコンパクト化する，(24) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `AnticomplementaryTransform → IncenterMark → SideReflectionTrace → TriangleFormation → SymmedianMark → CevianTrace → TriangleFormation → IncenterMark → PedalProjection → TriangleFormation → OrthicTransform → CentroidMark → PedalProjection → TriangleFormation → OrthicTransform → AnticomplementaryTransform → ExcentralTransform → AnticomplementaryTransform → ExcentralTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### Markov関手と到達時刻不変量（ProductChain・StateLumping・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.59fe5581d3`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `27`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身との同期積連鎖を作る，(2) 自己同型軌道に沿って強 lumping する，(3) 自身との同期積連鎖を作る，(4) 定常分布に関する時間反転をとる，(5) 正の固有関数によるDoob変換を施す，(6) 恒等遷移との凸結合でlazy化する，(7) 自己同型軌道に沿って強 lumping する，(8) 定常分布に関する時間反転をとる，(9) 自己同型軌道に沿って強 lumping する，(10) 定常分布に関する時間反転をとる，(11) 自己同型軌道に沿って強 lumping する，(12) 定常分布に関する時間反転をとる，(13) 自身との同期積連鎖を作る，(14) 恒等遷移との凸結合でlazy化する，(15) 正の固有関数によるDoob変換を施す，(16) 恒等遷移との凸結合でlazy化する，(17) 自身との同期積連鎖を作る，(18) 恒等遷移との凸結合でlazy化する，(19) 正の固有関数によるDoob変換を施す，(20) 指定集合で吸収させ過渡核をとる，(21) 過渡核のGreen作用素をとる，(22) 到達時刻の高次モーメント連立系を作る，(23) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProductChain → StateLumping → ProductChain → TimeReversal → DoobTransform → LazyPerturbation → StateLumping → TimeReversal → StateLumping → TimeReversal → StateLumping → TimeReversal → ProductChain → LazyPerturbation → DoobTransform → LazyPerturbation → ProductChain → LazyPerturbation → DoobTransform → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 凸体関手の合成力学（SteinerSymmetrization・CentroidBody・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.85d2c4c8ae`
- 状態: `unresolved_by_mathos`
- 射数: `23`
- 問い: `convex_body_dynamics`
- 難度仮説: `27`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 主慣性軸方向にSteiner対称化する，(2) 重心体をとる，(3) 射影体をとる，(4) 交叉体をとる，(5) 主慣性軸方向にSteiner対称化する，(6) 自身と極体のMinkowski和をとる，(7) 原点に関する極体をとる，(8) 差体をとる，(9) 原点に関する極体をとる，(10) 自身と極体のMinkowski和をとる，(11) 交叉体をとる，(12) 重心体をとる，(13) 射影体をとる，(14) 主慣性軸方向にSteiner対称化する，(15) 射影体をとる，(16) 交叉体をとる，(17) 重心体をとる，(18) 原点に関する極体をとる，(19) 面積と二次モーメントを固定して正規化する，(20) ここまでの凸体関手を反復する，(21) 支持関数の軌道へ移す，(22) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `SteinerSymmetrization → CentroidBody → ProjectionBody → IntersectionBody → SteinerSymmetrization → MinkowskiPolarSum → PolarDual → DifferenceBody → PolarDual → MinkowskiPolarSum → IntersectionBody → CentroidBody → ProjectionBody → SteinerSymmetrization → ProjectionBody → IntersectionBody → CentroidBody → PolarDual → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 多項式変換と算術観測（CriticalValuePolynomial・RootMultiset・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.c300359350`
- 状態: `unresolved_by_mathos`
- 射数: `22`
- 問い: `recurrence_order_drop`
- 難度仮説: `26`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 臨界値を根にもつ消去多項式を作る，(2) 重複度付き根配置へ移す，(3) 根配置からモニック多項式を再構成する，(4) 重複度付き根配置へ移す，(5) 根配置からモニック多項式を再構成する，(6) 根を逆数へ移す相反多項式をとる，(7) 導関数をモニックに再正規化する，(8) 根を逆数へ移す相反多項式をとる，(9) 導関数をモニックに再正規化する，(10) 根を逆数へ移す相反多項式をとる，(11) 導関数をモニックに再正規化する，(12) 根を二乗するGraeffe変換を施す，(13) 臨界値を根にもつ消去多項式を作る，(14) 根の重心を0へ移す平行移動共役を施す，(15) 根を二乗するGraeffe変換を施す，(16) 臨界値を根にもつ消去多項式を作る，(17) 重複度付き根配置へ移す，(18) 根の冪和モーメント列を作る，(19) モーメントからHankel行列族を作る，(20) 主小行列式列をとる，(21) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → RootMultiset → PolynomialReconstruction → ReciprocalPolynomial → DerivativeRenormalization → ReciprocalPolynomial → DerivativeRenormalization → ReciprocalPolynomial → DerivativeRenormalization → GraeffeTransform → CriticalValuePolynomial → ShiftConjugacy → GraeffeTransform → CriticalValuePolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 平面代数曲線の合成変換（CircleInversion・OffsetCurve・ProjectiveDual・HessianCurve）

- ID: `research.autonomous.plane_curve.c738e6cd0d`
- 状態: `unresolved_by_mathos`
- 射数: `23`
- 問い: `birational_periodicity`
- 難度仮説: `26`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 原点中心の円反転像をとる，(2) 法線方向の代数的平行曲線をとる，(3) 正則接線族の射影双対曲線をとる，(4) 法線族の包絡線である発展曲線をとる，(5) 法線方向の代数的平行曲線をとる，(6) 原点中心の円反転像をとる，(7) 定義多項式のHessian曲線をとる，(8) 固定基準三角形に関する等角共役Cremona像をとる，(9) 固定光源からの反射光線族の包絡線をとる，(10) 固定基準三角形に関する等角共役Cremona像をとる，(11) 射影閉包をとり無限遠点を加える，(12) 基点を避ける一般アフィンチャートへ移す，(13) 原点中心の円反転像をとる，(14) 固定非退化二次形式に関する極逆像をとる，(15) 法線方向の代数的平行曲線をとる，(16) 正則接線族の射影双対曲線をとる，(17) 固定光源からの反射光線族の包絡線をとる，(18) 法線族の包絡線である発展曲線をとる，(19) 固定非退化二次形式に関する極逆像をとる，(20) 固定基準三角形に関する等角共役Cremona像をとる，(21) 正則接線族の射影双対曲線をとる，(22) 定義多項式のHessian曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CircleInversion → OffsetCurve → ProjectiveDual → Evolute → OffsetCurve → CircleInversion → HessianCurve → IsogonalCremona → Catacaustic → IsogonalCremona → ProjectiveClosure → AffineChartChange → CircleInversion → PolarReciprocal → OffsetCurve → ProjectiveDual → Catacaustic → Evolute → PolarReciprocal → IsogonalCremona → ProjectiveDual → HessianCurve → BirationalPeriodQuery`

### 三角形変換の合成力学（CentroidMark・PedalProjection・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.9b5acbfe09`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重心を標識点として付加する，(2) 標識点から三辺への垂足三点をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 三辺の中点三角形へ移す，(5) 外心を標識点として付加する，(6) 各頂点と標識点が定める円の対応交点をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 反中点三角形へ移す，(9) 傍心三角形へ移す，(10) 垂心を標識点として付加する，(11) 標識点から三辺への垂足三点をとる，(12) 三点を頂点とする向き付き三角形を作る，(13) 類似重心を標識点として付加する，(14) 標識点を通る三本のcevianの辺上の足をとる，(15) 三点を頂点とする向き付き三角形を作る，(16) 垂足三角形へ移す，(17) 反中点三角形へ移す，(18) 垂足三角形へ移す，(19) 反中点三角形へ移す，(20) 重心・面積・向きを固定して相似正規化する，(21) 相似類のモジュライ点へ射影する，(22) ここまでの合成が誘導する写像を反復する，(23) 退化三角形を境界として軌道をコンパクト化する，(24) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CentroidMark → PedalProjection → TriangleFormation → MedialTransform → CircumcenterMark → VertexCircleTrace → TriangleFormation → AnticomplementaryTransform → ExcentralTransform → OrthocenterMark → PedalProjection → TriangleFormation → SymmedianMark → CevianTrace → TriangleFormation → OrthicTransform → AnticomplementaryTransform → OrthicTransform → AnticomplementaryTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### Markov関手と到達時刻不変量（ProductChain・TimeReversal・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.506a0b6cf3`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `27`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身との同期積連鎖を作る，(2) 定常分布に関する時間反転をとる，(3) 自身との同期積連鎖を作る，(4) 正の固有関数によるDoob変換を施す，(5) 定常分布に関する時間反転をとる，(6) 恒等遷移との凸結合でlazy化する，(7) 定常分布に関する時間反転をとる，(8) 自身との同期積連鎖を作る，(9) 定常分布に関する時間反転をとる，(10) 正の固有関数によるDoob変換を施す，(11) 自身との同期積連鎖を作る，(12) 恒等遷移との凸結合でlazy化する，(13) 正の固有関数によるDoob変換を施す，(14) 恒等遷移との凸結合でlazy化する，(15) 自己同型軌道に沿って強 lumping する，(16) 正の固有関数によるDoob変換を施す，(17) 恒等遷移との凸結合でlazy化する，(18) 自己同型軌道に沿って強 lumping する，(19) 指定集合で吸収させ過渡核をとる，(20) 過渡核のGreen作用素をとる，(21) 到達時刻の高次モーメント連立系を作る，(22) モーメント次数方向の漸化式を抽出する，(23) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProductChain → TimeReversal → ProductChain → DoobTransform → TimeReversal → LazyPerturbation → TimeReversal → ProductChain → TimeReversal → DoobTransform → ProductChain → LazyPerturbation → DoobTransform → LazyPerturbation → StateLumping → DoobTransform → LazyPerturbation → StateLumping → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 多項式変換と算術観測（GraeffeTransform・RootMultiset・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.f982c30807`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `28`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を二乗するGraeffe変換を施す，(2) 重複度付き根配置へ移す，(3) 根配置からモニック多項式を再構成する，(4) 根を二乗するGraeffe変換を施す，(5) 導関数をモニックに再正規化する，(6) 根を二乗するGraeffe変換を施す，(7) 根を逆数へ移す相反多項式をとる，(8) 根を二乗するGraeffe変換を施す，(9) 根の重心を0へ移す平行移動共役を施す，(10) 臨界値を根にもつ消去多項式を作る，(11) 導関数をモニックに再正規化する，(12) 重複度付き根配置へ移す，(13) 根配置からモニック多項式を再構成する，(14) 重複度付き根配置へ移す，(15) 根配置からモニック多項式を再構成する，(16) 臨界値を根にもつ消去多項式を作る，(17) 根の重心を0へ移す平行移動共役を施す，(18) 重複度付き根配置へ移す，(19) 根の冪和モーメント列を作る，(20) モーメントからHankel行列族を作る，(21) 主小行列式列をとる，(22) 満たす最小線形漸化式を抽出する，(23) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `GraeffeTransform → RootMultiset → PolynomialReconstruction → GraeffeTransform → DerivativeRenormalization → GraeffeTransform → ReciprocalPolynomial → GraeffeTransform → ShiftConjugacy → CriticalValuePolynomial → DerivativeRenormalization → RootMultiset → PolynomialReconstruction → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → ShiftConjugacy → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 平面代数曲線の合成変換（ProjectiveClosure・AffineChartChange・OffsetCurve・CircleInversion）

- ID: `research.autonomous.plane_curve.8347d6dfb7`
- 状態: `unresolved_by_mathos`
- 射数: `22`
- 問い: `birational_periodicity`
- 難度仮説: `25`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 射影閉包をとり無限遠点を加える，(2) 基点を避ける一般アフィンチャートへ移す，(3) 法線方向の代数的平行曲線をとる，(4) 射影閉包をとり無限遠点を加える，(5) 基点を避ける一般アフィンチャートへ移す，(6) 定義多項式のHessian曲線をとる，(7) 原点中心の円反転像をとる，(8) 法線族の包絡線である発展曲線をとる，(9) 射影閉包をとり無限遠点を加える，(10) 基点を避ける一般アフィンチャートへ移す，(11) 正則接線族の射影双対曲線をとる，(12) 固定基準三角形に関する等角共役Cremona像をとる，(13) 固定光源からの反射光線族の包絡線をとる，(14) 法線族の包絡線である発展曲線をとる，(15) 正則接線族の射影双対曲線をとる，(16) 法線族の包絡線である発展曲線をとる，(17) 固定基準三角形に関する等角共役Cremona像をとる，(18) 法線方向の代数的平行曲線をとる，(19) 固定非退化二次形式に関する極逆像をとる，(20) 法線方向の代数的平行曲線をとる，(21) 原点中心の円反転像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectiveClosure → AffineChartChange → OffsetCurve → ProjectiveClosure → AffineChartChange → HessianCurve → CircleInversion → Evolute → ProjectiveClosure → AffineChartChange → ProjectiveDual → IsogonalCremona → Catacaustic → Evolute → ProjectiveDual → Evolute → IsogonalCremona → OffsetCurve → PolarReciprocal → OffsetCurve → CircleInversion → BirationalPeriodQuery`

### 凸体関手の合成力学（DifferenceBody・CentroidBody・IntersectionBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.13fa18173a`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `27`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 差体をとる，(2) 重心体をとる，(3) 主慣性軸方向にSteiner対称化する，(4) 差体をとる，(5) 交叉体をとる，(6) 重心体をとる，(7) 原点に関する極体をとる，(8) 主慣性軸方向にSteiner対称化する，(9) 重心体をとる，(10) 自身と極体のMinkowski和をとる，(11) 原点に関する極体をとる，(12) 主慣性軸方向にSteiner対称化する，(13) 原点に関する極体をとる，(14) 重心体をとる，(15) 交叉体をとる，(16) 射影体をとる，(17) 差体をとる，(18) 射影体をとる，(19) 主慣性軸方向にSteiner対称化する，(20) 交叉体をとる，(21) 自身と極体のMinkowski和をとる，(22) 交叉体をとる，(23) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DifferenceBody → CentroidBody → SteinerSymmetrization → DifferenceBody → IntersectionBody → CentroidBody → PolarDual → SteinerSymmetrization → CentroidBody → MinkowskiPolarSum → PolarDual → SteinerSymmetrization → PolarDual → CentroidBody → IntersectionBody → ProjectionBody → DifferenceBody → ProjectionBody → SteinerSymmetrization → IntersectionBody → MinkowskiPolarSum → IntersectionBody → VolumeNormalization → ConvexFixedPointQuery`

### 三角形変換の合成力学（IncenterMark・PedalProjection・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.09a157f602`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 内心を標識点として付加する，(2) 標識点から三辺への垂足三点をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 三辺の中点三角形へ移す，(5) 類似重心を標識点として付加する，(6) 各頂点と標識点が定める円の対応交点をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 垂心を標識点として付加する，(9) 各頂点と標識点が定める円の対応交点をとる，(10) 三点を頂点とする向き付き三角形を作る，(11) 類似重心を標識点として付加する，(12) 標識点を通る三本のcevianの辺上の足をとる，(13) 三点を頂点とする向き付き三角形を作る，(14) 三辺の中点三角形へ移す，(15) 垂足三角形へ移す，(16) 反中点三角形へ移す，(17) 垂足三角形へ移す，(18) 三辺の中点三角形へ移す，(19) 傍心三角形へ移す，(20) 重心・面積・向きを固定して相似正規化する，(21) 相似類のモジュライ点へ射影する，(22) ここまでの合成が誘導する写像を反復する，(23) 退化三角形を境界として軌道をコンパクト化する，(24) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IncenterMark → PedalProjection → TriangleFormation → MedialTransform → SymmedianMark → VertexCircleTrace → TriangleFormation → OrthocenterMark → VertexCircleTrace → TriangleFormation → SymmedianMark → CevianTrace → TriangleFormation → MedialTransform → OrthicTransform → AnticomplementaryTransform → OrthicTransform → MedialTransform → ExcentralTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### Markov関手と到達時刻不変量（TimeReversal・ProductChain・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.0236f7d28b`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `27`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 定常分布に関する時間反転をとる，(2) 自身との同期積連鎖を作る，(3) 自己同型軌道に沿って強 lumping する，(4) 自身との同期積連鎖を作る，(5) 恒等遷移との凸結合でlazy化する，(6) 自身との同期積連鎖を作る，(7) 恒等遷移との凸結合でlazy化する，(8) 自身との同期積連鎖を作る，(9) 恒等遷移との凸結合でlazy化する，(10) 定常分布に関する時間反転をとる，(11) 恒等遷移との凸結合でlazy化する，(12) 自己同型軌道に沿って強 lumping する，(13) 定常分布に関する時間反転をとる，(14) 自己同型軌道に沿って強 lumping する，(15) 正の固有関数によるDoob変換を施す，(16) 自己同型軌道に沿って強 lumping する，(17) 定常分布に関する時間反転をとる，(18) 正の固有関数によるDoob変換を施す，(19) 指定集合で吸収させ過渡核をとる，(20) 過渡核のGreen作用素をとる，(21) 到達時刻の高次モーメント連立系を作る，(22) モーメント次数方向の漸化式を抽出する，(23) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `TimeReversal → ProductChain → StateLumping → ProductChain → LazyPerturbation → ProductChain → LazyPerturbation → ProductChain → LazyPerturbation → TimeReversal → LazyPerturbation → StateLumping → TimeReversal → StateLumping → DoobTransform → StateLumping → TimeReversal → DoobTransform → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 平面代数曲線の合成変換（PolarReciprocal・CircleInversion・Evolute・ProjectiveDual）

- ID: `research.autonomous.plane_curve.045a52002b`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `birational_periodicity`
- 難度仮説: `27`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定非退化二次形式に関する極逆像をとる，(2) 原点中心の円反転像をとる，(3) 定義多項式のHessian曲線をとる，(4) 固定光源からの反射光線族の包絡線をとる，(5) 原点中心の円反転像をとる，(6) 定義多項式のHessian曲線をとる，(7) 法線方向の代数的平行曲線をとる，(8) 固定非退化二次形式に関する極逆像をとる，(9) 法線族の包絡線である発展曲線をとる，(10) 射影閉包をとり無限遠点を加える，(11) 基点を避ける一般アフィンチャートへ移す，(12) 法線族の包絡線である発展曲線をとる，(13) 正則接線族の射影双対曲線をとる，(14) 定義多項式のHessian曲線をとる，(15) 固定非退化二次形式に関する極逆像をとる，(16) 固定光源からの反射光線族の包絡線をとる，(17) 定義多項式のHessian曲線をとる，(18) 法線方向の代数的平行曲線をとる，(19) 原点中心の円反転像をとる，(20) 固定光源からの反射光線族の包絡線をとる，(21) 固定基準三角形に関する等角共役Cremona像をとる，(22) 法線族の包絡線である発展曲線をとる，(23) 正則接線族の射影双対曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `PolarReciprocal → CircleInversion → HessianCurve → Catacaustic → CircleInversion → HessianCurve → OffsetCurve → PolarReciprocal → Evolute → ProjectiveClosure → AffineChartChange → Evolute → ProjectiveDual → HessianCurve → PolarReciprocal → Catacaustic → HessianCurve → OffsetCurve → CircleInversion → Catacaustic → IsogonalCremona → Evolute → ProjectiveDual → BirationalPeriodQuery`

### 凸体関手の合成力学（IntersectionBody・SteinerSymmetrization・CentroidBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.2531029b40`
- 状態: `unresolved_by_mathos`
- 射数: `23`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `26`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 交叉体をとる，(2) 主慣性軸方向にSteiner対称化する，(3) 差体をとる，(4) 交叉体をとる，(5) 重心体をとる，(6) 自身と極体のMinkowski和をとる，(7) 交叉体をとる，(8) 射影体をとる，(9) 原点に関する極体をとる，(10) 射影体をとる，(11) 主慣性軸方向にSteiner対称化する，(12) 差体をとる，(13) 原点に関する極体をとる，(14) 主慣性軸方向にSteiner対称化する，(15) 射影体をとる，(16) 差体をとる，(17) 自身と極体のMinkowski和をとる，(18) 重心体をとる，(19) 自身と極体のMinkowski和をとる，(20) 原点に関する極体をとる，(21) 重心体をとる，(22) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IntersectionBody → SteinerSymmetrization → DifferenceBody → IntersectionBody → CentroidBody → MinkowskiPolarSum → IntersectionBody → ProjectionBody → PolarDual → ProjectionBody → SteinerSymmetrization → DifferenceBody → PolarDual → SteinerSymmetrization → ProjectionBody → DifferenceBody → MinkowskiPolarSum → CentroidBody → MinkowskiPolarSum → PolarDual → CentroidBody → VolumeNormalization → ConvexFixedPointQuery`

### 多項式変換と算術観測（RootMultiset・PolynomialReconstruction・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.a5a16bfb36`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `recurrence_order_drop`
- 難度仮説: `28`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重複度付き根配置へ移す，(2) 根配置からモニック多項式を再構成する，(3) 導関数をモニックに再正規化する，(4) 根を二乗するGraeffe変換を施す，(5) 導関数をモニックに再正規化する，(6) 根を二乗するGraeffe変換を施す，(7) 根を逆数へ移す相反多項式をとる，(8) 導関数をモニックに再正規化する，(9) 重複度付き根配置へ移す，(10) 根配置からモニック多項式を再構成する，(11) 重複度付き根配置へ移す，(12) 根配置からモニック多項式を再構成する，(13) 導関数をモニックに再正規化する，(14) 根の重心を0へ移す平行移動共役を施す，(15) 臨界値を根にもつ消去多項式を作る，(16) 根を二乗するGraeffe変換を施す，(17) 根を逆数へ移す相反多項式をとる，(18) 根を二乗するGraeffe変換を施す，(19) 重複度付き根配置へ移す，(20) 根の冪和モーメント列を作る，(21) モーメントからHankel行列族を作る，(22) 主小行列式列をとる，(23) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `RootMultiset → PolynomialReconstruction → DerivativeRenormalization → GraeffeTransform → DerivativeRenormalization → GraeffeTransform → ReciprocalPolynomial → DerivativeRenormalization → RootMultiset → PolynomialReconstruction → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → ShiftConjugacy → CriticalValuePolynomial → GraeffeTransform → ReciprocalPolynomial → GraeffeTransform → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 三角形変換の合成力学（IncenterMark・CevianTrace・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.10b983bea8`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `28`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 内心を標識点として付加する，(2) 標識点を通る三本のcevianの辺上の足をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 重心を標識点として付加する，(5) 標識点を三辺に関して反射した三点をとる，(6) 三点を頂点とする向き付き三角形を作る，(7) 垂心を標識点として付加する，(8) 標識点を三辺に関して反射した三点をとる，(9) 三点を頂点とする向き付き三角形を作る，(10) 内心を標識点として付加する，(11) 標識点を三辺に関して反射した三点をとる，(12) 三点を頂点とする向き付き三角形を作る，(13) 垂足三角形へ移す，(14) 三辺の中点三角形へ移す，(15) 傍心三角形へ移す，(16) 三辺の中点三角形へ移す，(17) 傍心三角形へ移す，(18) 三辺の中点三角形へ移す，(19) 重心・面積・向きを固定して相似正規化する，(20) 相似類のモジュライ点へ射影する，(21) ここまでの合成が誘導する写像を反復する，(22) 退化三角形を境界として軌道をコンパクト化する，(23) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IncenterMark → CevianTrace → TriangleFormation → CentroidMark → SideReflectionTrace → TriangleFormation → OrthocenterMark → SideReflectionTrace → TriangleFormation → IncenterMark → SideReflectionTrace → TriangleFormation → OrthicTransform → MedialTransform → ExcentralTransform → MedialTransform → ExcentralTransform → MedialTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### Markov関手と到達時刻不変量（ProductChain・StateLumping・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.80948b3ba7`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `28`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身との同期積連鎖を作る，(2) 自己同型軌道に沿って強 lumping する，(3) 正の固有関数によるDoob変換を施す，(4) 自身との同期積連鎖を作る，(5) 恒等遷移との凸結合でlazy化する，(6) 自己同型軌道に沿って強 lumping する，(7) 自身との同期積連鎖を作る，(8) 自己同型軌道に沿って強 lumping する，(9) 自身との同期積連鎖を作る，(10) 正の固有関数によるDoob変換を施す，(11) 定常分布に関する時間反転をとる，(12) 自己同型軌道に沿って強 lumping する，(13) 正の固有関数によるDoob変換を施す，(14) 恒等遷移との凸結合でlazy化する，(15) 定常分布に関する時間反転をとる，(16) 正の固有関数によるDoob変換を施す，(17) 恒等遷移との凸結合でlazy化する，(18) 定常分布に関する時間反転をとる，(19) 恒等遷移との凸結合でlazy化する，(20) 定常分布に関する時間反転をとる，(21) 指定集合で吸収させ過渡核をとる，(22) 過渡核のGreen作用素をとる，(23) 到達時刻の高次モーメント連立系を作る，(24) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProductChain → StateLumping → DoobTransform → ProductChain → LazyPerturbation → StateLumping → ProductChain → StateLumping → ProductChain → DoobTransform → TimeReversal → StateLumping → DoobTransform → LazyPerturbation → TimeReversal → DoobTransform → LazyPerturbation → TimeReversal → LazyPerturbation → TimeReversal → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 多項式変換と算術観測（DerivativeRenormalization・ShiftConjugacy・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.791af49faa`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `recurrence_order_drop`
- 難度仮説: `28`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 導関数をモニックに再正規化する，(2) 根の重心を0へ移す平行移動共役を施す，(3) 導関数をモニックに再正規化する，(4) 根の重心を0へ移す平行移動共役を施す，(5) 導関数をモニックに再正規化する，(6) 臨界値を根にもつ消去多項式を作る，(7) 根の重心を0へ移す平行移動共役を施す，(8) 導関数をモニックに再正規化する，(9) 臨界値を根にもつ消去多項式を作る，(10) 重複度付き根配置へ移す，(11) 根配置からモニック多項式を再構成する，(12) 根の重心を0へ移す平行移動共役を施す，(13) 根を逆数へ移す相反多項式をとる，(14) 臨界値を根にもつ消去多項式を作る，(15) 重複度付き根配置へ移す，(16) 根配置からモニック多項式を再構成する，(17) 根を逆数へ移す相反多項式をとる，(18) 根を二乗するGraeffe変換を施す，(19) 重複度付き根配置へ移す，(20) 根の冪和モーメント列を作る，(21) モーメントからHankel行列族を作る，(22) 主小行列式列をとる，(23) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DerivativeRenormalization → ShiftConjugacy → DerivativeRenormalization → ShiftConjugacy → DerivativeRenormalization → CriticalValuePolynomial → ShiftConjugacy → DerivativeRenormalization → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → ShiftConjugacy → ReciprocalPolynomial → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → ReciprocalPolynomial → GraeffeTransform → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 凸体関手の合成力学（PolarDual・ProjectionBody・SteinerSymmetrization・VolumeNormalization）

- ID: `research.autonomous.convex_body.e068ce8995`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `27`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 原点に関する極体をとる，(2) 射影体をとる，(3) 差体をとる，(4) 主慣性軸方向にSteiner対称化する，(5) 交叉体をとる，(6) 重心体をとる，(7) 差体をとる，(8) 原点に関する極体をとる，(9) 射影体をとる，(10) 重心体をとる，(11) 自身と極体のMinkowski和をとる，(12) 交叉体をとる，(13) 主慣性軸方向にSteiner対称化する，(14) 交叉体をとる，(15) 射影体をとる，(16) 自身と極体のMinkowski和をとる，(17) 交叉体をとる，(18) 重心体をとる，(19) 主慣性軸方向にSteiner対称化する，(20) 差体をとる，(21) 射影体をとる，(22) 主慣性軸方向にSteiner対称化する，(23) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `PolarDual → ProjectionBody → DifferenceBody → SteinerSymmetrization → IntersectionBody → CentroidBody → DifferenceBody → PolarDual → ProjectionBody → CentroidBody → MinkowskiPolarSum → IntersectionBody → SteinerSymmetrization → IntersectionBody → ProjectionBody → MinkowskiPolarSum → IntersectionBody → CentroidBody → SteinerSymmetrization → DifferenceBody → ProjectionBody → SteinerSymmetrization → VolumeNormalization → ConvexFixedPointQuery`

### 平面代数曲線の合成変換（HessianCurve・OffsetCurve・IsogonalCremona・Catacaustic）

- ID: `research.autonomous.plane_curve.092d203298`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `birational_periodicity`
- 難度仮説: `29`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 定義多項式のHessian曲線をとる，(2) 法線方向の代数的平行曲線をとる，(3) 射影閉包をとり無限遠点を加える，(4) 基点を避ける一般アフィンチャートへ移す，(5) 正則接線族の射影双対曲線をとる，(6) 定義多項式のHessian曲線をとる，(7) 法線族の包絡線である発展曲線をとる，(8) 固定非退化二次形式に関する極逆像をとる，(9) 固定基準三角形に関する等角共役Cremona像をとる，(10) 法線方向の代数的平行曲線をとる，(11) 射影閉包をとり無限遠点を加える，(12) 基点を避ける一般アフィンチャートへ移す，(13) 定義多項式のHessian曲線をとる，(14) 法線族の包絡線である発展曲線をとる，(15) 原点中心の円反転像をとる，(16) 固定光源からの反射光線族の包絡線をとる，(17) 定義多項式のHessian曲線をとる，(18) 射影閉包をとり無限遠点を加える，(19) 基点を避ける一般アフィンチャートへ移す，(20) 法線方向の代数的平行曲線をとる，(21) 原点中心の円反転像をとる，(22) 射影閉包をとり無限遠点を加える，(23) 基点を避ける一般アフィンチャートへ移す，(24) 固定基準三角形に関する等角共役Cremona像をとる，(25) 固定光源からの反射光線族の包絡線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `HessianCurve → OffsetCurve → ProjectiveClosure → AffineChartChange → ProjectiveDual → HessianCurve → Evolute → PolarReciprocal → IsogonalCremona → OffsetCurve → ProjectiveClosure → AffineChartChange → HessianCurve → Evolute → CircleInversion → Catacaustic → HessianCurve → ProjectiveClosure → AffineChartChange → OffsetCurve → CircleInversion → ProjectiveClosure → AffineChartChange → IsogonalCremona → Catacaustic → BirationalPeriodQuery`

### 三角形変換の合成力学（CircumcenterMark・SideReflectionTrace・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.4056377bd6`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `31`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 外心を標識点として付加する，(2) 標識点を三辺に関して反射した三点をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 三辺の中点三角形へ移す，(5) 傍心三角形へ移す，(6) 内心を標識点として付加する，(7) 標識点から三辺への垂足三点をとる，(8) 三点を頂点とする向き付き三角形を作る，(9) 類似重心を標識点として付加する，(10) 各頂点と標識点が定める円の対応交点をとる，(11) 三点を頂点とする向き付き三角形を作る，(12) 垂足三角形へ移す，(13) 類似重心を標識点として付加する，(14) 標識点を通る三本のcevianの辺上の足をとる，(15) 三点を頂点とする向き付き三角形を作る，(16) 反中点三角形へ移す，(17) 傍心三角形へ移す，(18) 反中点三角形へ移す，(19) 傍心三角形へ移す，(20) 三辺の中点三角形へ移す，(21) 重心・面積・向きを固定して相似正規化する，(22) 相似類のモジュライ点へ射影する，(23) ここまでの合成が誘導する写像を反復する，(24) 退化三角形を境界として軌道をコンパクト化する，(25) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CircumcenterMark → SideReflectionTrace → TriangleFormation → MedialTransform → ExcentralTransform → IncenterMark → PedalProjection → TriangleFormation → SymmedianMark → VertexCircleTrace → TriangleFormation → OrthicTransform → SymmedianMark → CevianTrace → TriangleFormation → AnticomplementaryTransform → ExcentralTransform → AnticomplementaryTransform → ExcentralTransform → MedialTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### Markov関手と到達時刻不変量（DoobTransform・StateLumping・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.f1435096ec`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `28`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 正の固有関数によるDoob変換を施す，(2) 自己同型軌道に沿って強 lumping する，(3) 正の固有関数によるDoob変換を施す，(4) 自身との同期積連鎖を作る，(5) 恒等遷移との凸結合でlazy化する，(6) 定常分布に関する時間反転をとる，(7) 正の固有関数によるDoob変換を施す，(8) 恒等遷移との凸結合でlazy化する，(9) 定常分布に関する時間反転をとる，(10) 正の固有関数によるDoob変換を施す，(11) 定常分布に関する時間反転をとる，(12) 自身との同期積連鎖を作る，(13) 自己同型軌道に沿って強 lumping する，(14) 自身との同期積連鎖を作る，(15) 定常分布に関する時間反転をとる，(16) 自己同型軌道に沿って強 lumping する，(17) 自身との同期積連鎖を作る，(18) 恒等遷移との凸結合でlazy化する，(19) 自己同型軌道に沿って強 lumping する，(20) 指定集合で吸収させ過渡核をとる，(21) 過渡核のGreen作用素をとる，(22) 到達時刻の高次モーメント連立系を作る，(23) モーメント次数方向の漸化式を抽出する，(24) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DoobTransform → StateLumping → DoobTransform → ProductChain → LazyPerturbation → TimeReversal → DoobTransform → LazyPerturbation → TimeReversal → DoobTransform → TimeReversal → ProductChain → StateLumping → ProductChain → TimeReversal → StateLumping → ProductChain → LazyPerturbation → StateLumping → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 平面代数曲線の合成変換（Catacaustic・HessianCurve・HessianCurve・PolarReciprocal）

- ID: `research.autonomous.plane_curve.2b4fb03fc7`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `birational_periodicity`
- 難度仮説: `27`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定光源からの反射光線族の包絡線をとる，(2) 定義多項式のHessian曲線をとる，(3) 固定非退化二次形式に関する極逆像をとる，(4) 正則接線族の射影双対曲線をとる，(5) 射影閉包をとり無限遠点を加える，(6) 基点を避ける一般アフィンチャートへ移す，(7) 定義多項式のHessian曲線をとる，(8) 固定非退化二次形式に関する極逆像をとる，(9) 固定光源からの反射光線族の包絡線をとる，(10) 正則接線族の射影双対曲線をとる，(11) 原点中心の円反転像をとる，(12) 法線方向の代数的平行曲線をとる，(13) 固定光源からの反射光線族の包絡線をとる，(14) 固定基準三角形に関する等角共役Cremona像をとる，(15) 原点中心の円反転像をとる，(16) 固定基準三角形に関する等角共役Cremona像をとる，(17) 原点中心の円反転像をとる，(18) 法線方向の代数的平行曲線をとる，(19) 固定光源からの反射光線族の包絡線をとる，(20) 定義多項式のHessian曲線をとる，(21) 法線族の包絡線である発展曲線をとる，(22) 定義多項式のHessian曲線をとる，(23) 固定非退化二次形式に関する極逆像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `Catacaustic → HessianCurve → PolarReciprocal → ProjectiveDual → ProjectiveClosure → AffineChartChange → HessianCurve → PolarReciprocal → Catacaustic → ProjectiveDual → CircleInversion → OffsetCurve → Catacaustic → IsogonalCremona → CircleInversion → IsogonalCremona → CircleInversion → OffsetCurve → Catacaustic → HessianCurve → Evolute → HessianCurve → PolarReciprocal → BirationalPeriodQuery`

### 凸体関手の合成力学（IntersectionBody・DifferenceBody・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.cefc41bc39`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `convex_body_dynamics`
- 難度仮説: `29`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 交叉体をとる，(2) 差体をとる，(3) 重心体をとる，(4) 射影体をとる，(5) 交叉体をとる，(6) 自身と極体のMinkowski和をとる，(7) 交叉体をとる，(8) 差体をとる，(9) 射影体をとる，(10) 自身と極体のMinkowski和をとる，(11) 射影体をとる，(12) 自身と極体のMinkowski和をとる，(13) 重心体をとる，(14) 射影体をとる，(15) 主慣性軸方向にSteiner対称化する，(16) 差体をとる，(17) 自身と極体のMinkowski和をとる，(18) 原点に関する極体をとる，(19) 差体をとる，(20) 重心体をとる，(21) 面積と二次モーメントを固定して正規化する，(22) ここまでの凸体関手を反復する，(23) 支持関数の軌道へ移す，(24) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IntersectionBody → DifferenceBody → CentroidBody → ProjectionBody → IntersectionBody → MinkowskiPolarSum → IntersectionBody → DifferenceBody → ProjectionBody → MinkowskiPolarSum → ProjectionBody → MinkowskiPolarSum → CentroidBody → ProjectionBody → SteinerSymmetrization → DifferenceBody → MinkowskiPolarSum → PolarDual → DifferenceBody → CentroidBody → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 多項式変換と算術観測（ShiftConjugacy・CriticalValuePolynomial・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.17767a0270`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `recurrence_order_drop`
- 難度仮説: `28`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根の重心を0へ移す平行移動共役を施す，(2) 臨界値を根にもつ消去多項式を作る，(3) 根の重心を0へ移す平行移動共役を施す，(4) 根を二乗するGraeffe変換を施す，(5) 根を逆数へ移す相反多項式をとる，(6) 根を二乗するGraeffe変換を施す，(7) 臨界値を根にもつ消去多項式を作る，(8) 根の重心を0へ移す平行移動共役を施す，(9) 重複度付き根配置へ移す，(10) 根配置からモニック多項式を再構成する，(11) 根を二乗するGraeffe変換を施す，(12) 重複度付き根配置へ移す，(13) 根配置からモニック多項式を再構成する，(14) 根を二乗するGraeffe変換を施す，(15) 根を逆数へ移す相反多項式をとる，(16) 臨界値を根にもつ消去多項式を作る，(17) 根の重心を0へ移す平行移動共役を施す，(18) 臨界値を根にもつ消去多項式を作る，(19) 根を逆数へ移す相反多項式をとる，(20) 重複度付き根配置へ移す，(21) 根の冪和モーメント列を作る，(22) モーメントからHankel行列族を作る，(23) 主小行列式列をとる，(24) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ShiftConjugacy → CriticalValuePolynomial → ShiftConjugacy → GraeffeTransform → ReciprocalPolynomial → GraeffeTransform → CriticalValuePolynomial → ShiftConjugacy → RootMultiset → PolynomialReconstruction → GraeffeTransform → RootMultiset → PolynomialReconstruction → GraeffeTransform → ReciprocalPolynomial → CriticalValuePolynomial → ShiftConjugacy → CriticalValuePolynomial → ReciprocalPolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 三角形変換の合成力学（AnticomplementaryTransform・CentroidMark・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.1d43a3050b`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `28`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 反中点三角形へ移す，(2) 重心を標識点として付加する，(3) 各頂点と標識点が定める円の対応交点をとる，(4) 三点を頂点とする向き付き三角形を作る，(5) 三辺の中点三角形へ移す，(6) 垂心を標識点として付加する，(7) 標識点を通る三本のcevianの辺上の足をとる，(8) 三点を頂点とする向き付き三角形を作る，(9) 外心を標識点として付加する，(10) 各頂点と標識点が定める円の対応交点をとる，(11) 三点を頂点とする向き付き三角形を作る，(12) 外心を標識点として付加する，(13) 標識点を通る三本のcevianの辺上の足をとる，(14) 三点を頂点とする向き付き三角形を作る，(15) 傍心三角形へ移す，(16) 三辺の中点三角形へ移す，(17) 傍心三角形へ移す，(18) 三辺の中点三角形へ移す，(19) 重心・面積・向きを固定して相似正規化する，(20) 相似類のモジュライ点へ射影する，(21) ここまでの合成が誘導する写像を反復する，(22) 退化三角形を境界として軌道をコンパクト化する，(23) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `AnticomplementaryTransform → CentroidMark → VertexCircleTrace → TriangleFormation → MedialTransform → OrthocenterMark → CevianTrace → TriangleFormation → CircumcenterMark → VertexCircleTrace → TriangleFormation → CircumcenterMark → CevianTrace → TriangleFormation → ExcentralTransform → MedialTransform → ExcentralTransform → MedialTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 凸体関手の合成力学（ProjectionBody・DifferenceBody・MinkowskiPolarSum・VolumeNormalization）

- ID: `research.autonomous.convex_body.938932fee5`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `28`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 射影体をとる，(2) 差体をとる，(3) 原点に関する極体をとる，(4) 交叉体をとる，(5) 自身と極体のMinkowski和をとる，(6) 差体をとる，(7) 原点に関する極体をとる，(8) 主慣性軸方向にSteiner対称化する，(9) 原点に関する極体をとる，(10) 主慣性軸方向にSteiner対称化する，(11) 交叉体をとる，(12) 主慣性軸方向にSteiner対称化する，(13) 射影体をとる，(14) 差体をとる，(15) 重心体をとる，(16) 差体をとる，(17) 射影体をとる，(18) 自身と極体のMinkowski和をとる，(19) 原点に関する極体をとる，(20) 重心体をとる，(21) 交叉体をとる，(22) 主慣性軸方向にSteiner対称化する，(23) 自身と極体のMinkowski和をとる，(24) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectionBody → DifferenceBody → PolarDual → IntersectionBody → MinkowskiPolarSum → DifferenceBody → PolarDual → SteinerSymmetrization → PolarDual → SteinerSymmetrization → IntersectionBody → SteinerSymmetrization → ProjectionBody → DifferenceBody → CentroidBody → DifferenceBody → ProjectionBody → MinkowskiPolarSum → PolarDual → CentroidBody → IntersectionBody → SteinerSymmetrization → MinkowskiPolarSum → VolumeNormalization → ConvexFixedPointQuery`

### 平面代数曲線の合成変換（Catacaustic・CircleInversion・Catacaustic・Evolute）

- ID: `research.autonomous.plane_curve.fa248ba1e8`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `birational_periodicity`
- 難度仮説: `27`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定光源からの反射光線族の包絡線をとる，(2) 原点中心の円反転像をとる，(3) 正則接線族の射影双対曲線をとる，(4) 固定光源からの反射光線族の包絡線をとる，(5) 原点中心の円反転像をとる，(6) 固定非退化二次形式に関する極逆像をとる，(7) 正則接線族の射影双対曲線をとる，(8) 固定基準三角形に関する等角共役Cremona像をとる，(9) 定義多項式のHessian曲線をとる，(10) 固定光源からの反射光線族の包絡線をとる，(11) 固定基準三角形に関する等角共役Cremona像をとる，(12) 法線方向の代数的平行曲線をとる，(13) 原点中心の円反転像をとる，(14) 正則接線族の射影双対曲線をとる，(15) 定義多項式のHessian曲線をとる，(16) 固定非退化二次形式に関する極逆像をとる，(17) 射影閉包をとり無限遠点を加える，(18) 基点を避ける一般アフィンチャートへ移す，(19) 法線族の包絡線である発展曲線をとる，(20) 射影閉包をとり無限遠点を加える，(21) 基点を避ける一般アフィンチャートへ移す，(22) 固定光源からの反射光線族の包絡線をとる，(23) 法線族の包絡線である発展曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `Catacaustic → CircleInversion → ProjectiveDual → Catacaustic → CircleInversion → PolarReciprocal → ProjectiveDual → IsogonalCremona → HessianCurve → Catacaustic → IsogonalCremona → OffsetCurve → CircleInversion → ProjectiveDual → HessianCurve → PolarReciprocal → ProjectiveClosure → AffineChartChange → Evolute → ProjectiveClosure → AffineChartChange → Catacaustic → Evolute → BirationalPeriodQuery`

### Markov関手と到達時刻不変量（ProductChain・DoobTransform・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.25e8eac0da`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `27`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身との同期積連鎖を作る，(2) 正の固有関数によるDoob変換を施す，(3) 恒等遷移との凸結合でlazy化する，(4) 自己同型軌道に沿って強 lumping する，(5) 恒等遷移との凸結合でlazy化する，(6) 自己同型軌道に沿って強 lumping する，(7) 自身との同期積連鎖を作る，(8) 定常分布に関する時間反転をとる，(9) 正の固有関数によるDoob変換を施す，(10) 自己同型軌道に沿って強 lumping する，(11) 自身との同期積連鎖を作る，(12) 正の固有関数によるDoob変換を施す，(13) 自己同型軌道に沿って強 lumping する，(14) 恒等遷移との凸結合でlazy化する，(15) 定常分布に関する時間反転をとる，(16) 恒等遷移との凸結合でlazy化する，(17) 自身との同期積連鎖を作る，(18) 正の固有関数によるDoob変換を施す，(19) 指定集合で吸収させ過渡核をとる，(20) 過渡核のGreen作用素をとる，(21) 到達時刻の高次モーメント連立系を作る，(22) モーメント次数方向の漸化式を抽出する，(23) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProductChain → DoobTransform → LazyPerturbation → StateLumping → LazyPerturbation → StateLumping → ProductChain → TimeReversal → DoobTransform → StateLumping → ProductChain → DoobTransform → StateLumping → LazyPerturbation → TimeReversal → LazyPerturbation → ProductChain → DoobTransform → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 多項式変換と算術観測（ReciprocalPolynomial・DerivativeRenormalization・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.bd93cd1e7c`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `29`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を逆数へ移す相反多項式をとる，(2) 導関数をモニックに再正規化する，(3) 重複度付き根配置へ移す，(4) 根配置からモニック多項式を再構成する，(5) 導関数をモニックに再正規化する，(6) 根の重心を0へ移す平行移動共役を施す，(7) 導関数をモニックに再正規化する，(8) 根を逆数へ移す相反多項式をとる，(9) 根を二乗するGraeffe変換を施す，(10) 根を逆数へ移す相反多項式をとる，(11) 根を二乗するGraeffe変換を施す，(12) 根を逆数へ移す相反多項式をとる，(13) 根の重心を0へ移す平行移動共役を施す，(14) 根を二乗するGraeffe変換を施す，(15) 導関数をモニックに再正規化する，(16) 重複度付き根配置へ移す，(17) 根配置からモニック多項式を再構成する，(18) 根の重心を0へ移す平行移動共役を施す，(19) 重複度付き根配置へ移す，(20) 根の冪和モーメント列を作る，(21) モーメントからHankel行列族を作る，(22) 主小行列式列をとる，(23) 満たす最小線形漸化式を抽出する，(24) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ReciprocalPolynomial → DerivativeRenormalization → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → ShiftConjugacy → DerivativeRenormalization → ReciprocalPolynomial → GraeffeTransform → ReciprocalPolynomial → GraeffeTransform → ReciprocalPolynomial → ShiftConjugacy → GraeffeTransform → DerivativeRenormalization → RootMultiset → PolynomialReconstruction → ShiftConjugacy → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 三角形変換の合成力学（AnticomplementaryTransform・IncenterMark・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.7098d47914`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 反中点三角形へ移す，(2) 内心を標識点として付加する，(3) 標識点を三辺に関して反射した三点をとる，(4) 三点を頂点とする向き付き三角形を作る，(5) 反中点三角形へ移す，(6) 類似重心を標識点として付加する，(7) 標識点を三辺に関して反射した三点をとる，(8) 三点を頂点とする向き付き三角形を作る，(9) 垂足三角形へ移す，(10) 内心を標識点として付加する，(11) 各頂点と標識点が定める円の対応交点をとる，(12) 三点を頂点とする向き付き三角形を作る，(13) 垂心を標識点として付加する，(14) 標識点から三辺への垂足三点をとる，(15) 三点を頂点とする向き付き三角形を作る，(16) 垂足三角形へ移す，(17) 三辺の中点三角形へ移す，(18) 傍心三角形へ移す，(19) 三辺の中点三角形へ移す，(20) 重心・面積・向きを固定して相似正規化する，(21) 相似類のモジュライ点へ射影する，(22) ここまでの合成が誘導する写像を反復する，(23) 退化三角形を境界として軌道をコンパクト化する，(24) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `AnticomplementaryTransform → IncenterMark → SideReflectionTrace → TriangleFormation → AnticomplementaryTransform → SymmedianMark → SideReflectionTrace → TriangleFormation → OrthicTransform → IncenterMark → VertexCircleTrace → TriangleFormation → OrthocenterMark → PedalProjection → TriangleFormation → OrthicTransform → MedialTransform → ExcentralTransform → MedialTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### Markov関手と到達時刻不変量（LazyPerturbation・StateLumping・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.7c6d852220`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `28`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 恒等遷移との凸結合でlazy化する，(2) 自己同型軌道に沿って強 lumping する，(3) 正の固有関数によるDoob変換を施す，(4) 自己同型軌道に沿って強 lumping する，(5) 正の固有関数によるDoob変換を施す，(6) 自身との同期積連鎖を作る，(7) 正の固有関数によるDoob変換を施す，(8) 自己同型軌道に沿って強 lumping する，(9) 恒等遷移との凸結合でlazy化する，(10) 定常分布に関する時間反転をとる，(11) 正の固有関数によるDoob変換を施す，(12) 自身との同期積連鎖を作る，(13) 定常分布に関する時間反転をとる，(14) 恒等遷移との凸結合でlazy化する，(15) 定常分布に関する時間反転をとる，(16) 恒等遷移との凸結合でlazy化する，(17) 自身との同期積連鎖を作る，(18) 自己同型軌道に沿って強 lumping する，(19) 自身との同期積連鎖を作る，(20) 定常分布に関する時間反転をとる，(21) 指定集合で吸収させ過渡核をとる，(22) 過渡核のGreen作用素をとる，(23) 到達時刻の高次モーメント連立系を作る，(24) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `LazyPerturbation → StateLumping → DoobTransform → StateLumping → DoobTransform → ProductChain → DoobTransform → StateLumping → LazyPerturbation → TimeReversal → DoobTransform → ProductChain → TimeReversal → LazyPerturbation → TimeReversal → LazyPerturbation → ProductChain → StateLumping → ProductChain → TimeReversal → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 凸体関手の合成力学（SteinerSymmetrization・DifferenceBody・CentroidBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.9d3f9a6a62`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `28`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 主慣性軸方向にSteiner対称化する，(2) 差体をとる，(3) 自身と極体のMinkowski和をとる，(4) 差体をとる，(5) 原点に関する極体をとる，(6) 主慣性軸方向にSteiner対称化する，(7) 自身と極体のMinkowski和をとる，(8) 主慣性軸方向にSteiner対称化する，(9) 重心体をとる，(10) 交叉体をとる，(11) 主慣性軸方向にSteiner対称化する，(12) 自身と極体のMinkowski和をとる，(13) 原点に関する極体をとる，(14) 差体をとる，(15) 交叉体をとる，(16) 差体をとる，(17) 交叉体をとる，(18) 自身と極体のMinkowski和をとる，(19) 重心体をとる，(20) 射影体をとる，(21) 交叉体をとる，(22) 射影体をとる，(23) 重心体をとる，(24) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `SteinerSymmetrization → DifferenceBody → MinkowskiPolarSum → DifferenceBody → PolarDual → SteinerSymmetrization → MinkowskiPolarSum → SteinerSymmetrization → CentroidBody → IntersectionBody → SteinerSymmetrization → MinkowskiPolarSum → PolarDual → DifferenceBody → IntersectionBody → DifferenceBody → IntersectionBody → MinkowskiPolarSum → CentroidBody → ProjectionBody → IntersectionBody → ProjectionBody → CentroidBody → VolumeNormalization → ConvexFixedPointQuery`

### 平面代数曲線の合成変換（CircleInversion・HessianCurve・PolarReciprocal・ProjectiveDual）

- ID: `research.autonomous.plane_curve.bf8aa8123c`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `birational_periodicity`
- 難度仮説: `28`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 原点中心の円反転像をとる，(2) 定義多項式のHessian曲線をとる，(3) 固定基準三角形に関する等角共役Cremona像をとる，(4) 正則接線族の射影双対曲線をとる，(5) 法線族の包絡線である発展曲線をとる，(6) 法線方向の代数的平行曲線をとる，(7) 射影閉包をとり無限遠点を加える，(8) 基点を避ける一般アフィンチャートへ移す，(9) 固定基準三角形に関する等角共役Cremona像をとる，(10) 定義多項式のHessian曲線をとる，(11) 射影閉包をとり無限遠点を加える，(12) 基点を避ける一般アフィンチャートへ移す，(13) 原点中心の円反転像をとる，(14) 射影閉包をとり無限遠点を加える，(15) 基点を避ける一般アフィンチャートへ移す，(16) 定義多項式のHessian曲線をとる，(17) 法線族の包絡線である発展曲線をとる，(18) 定義多項式のHessian曲線をとる，(19) 固定光源からの反射光線族の包絡線をとる，(20) 原点中心の円反転像をとる，(21) 法線族の包絡線である発展曲線をとる，(22) 正則接線族の射影双対曲線をとる，(23) 固定非退化二次形式に関する極逆像をとる，(24) 正則接線族の射影双対曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CircleInversion → HessianCurve → IsogonalCremona → ProjectiveDual → Evolute → OffsetCurve → ProjectiveClosure → AffineChartChange → IsogonalCremona → HessianCurve → ProjectiveClosure → AffineChartChange → CircleInversion → ProjectiveClosure → AffineChartChange → HessianCurve → Evolute → HessianCurve → Catacaustic → CircleInversion → Evolute → ProjectiveDual → PolarReciprocal → ProjectiveDual → BirationalPeriodQuery`

### 多項式変換と算術観測（ShiftConjugacy・CriticalValuePolynomial・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.a9d49b6e64`
- 状態: `unresolved_by_mathos`
- 射数: `23`
- 問い: `recurrence_order_drop`
- 難度仮説: `27`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根の重心を0へ移す平行移動共役を施す，(2) 臨界値を根にもつ消去多項式を作る，(3) 重複度付き根配置へ移す，(4) 根配置からモニック多項式を再構成する，(5) 根を逆数へ移す相反多項式をとる，(6) 根の重心を0へ移す平行移動共役を施す，(7) 導関数をモニックに再正規化する，(8) 根を逆数へ移す相反多項式をとる，(9) 臨界値を根にもつ消去多項式を作る，(10) 根を二乗するGraeffe変換を施す，(11) 根を逆数へ移す相反多項式をとる，(12) 根の重心を0へ移す平行移動共役を施す，(13) 臨界値を根にもつ消去多項式を作る，(14) 根を二乗するGraeffe変換を施す，(15) 重複度付き根配置へ移す，(16) 根配置からモニック多項式を再構成する，(17) 導関数をモニックに再正規化する，(18) 重複度付き根配置へ移す，(19) 根の冪和モーメント列を作る，(20) モーメントからHankel行列族を作る，(21) 主小行列式列をとる，(22) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ShiftConjugacy → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → ReciprocalPolynomial → ShiftConjugacy → DerivativeRenormalization → ReciprocalPolynomial → CriticalValuePolynomial → GraeffeTransform → ReciprocalPolynomial → ShiftConjugacy → CriticalValuePolynomial → GraeffeTransform → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 三角形変換の合成力学（MedialTransform・OrthicTransform・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.38139605e9`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `29`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0625`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 三辺の中点三角形へ移す，(2) 垂足三角形へ移す，(3) 類似重心を標識点として付加する，(4) 標識点を通る三本のcevianの辺上の足をとる，(5) 三点を頂点とする向き付き三角形を作る，(6) 反中点三角形へ移す，(7) 内心を標識点として付加する，(8) 標識点から三辺への垂足三点をとる，(9) 三点を頂点とする向き付き三角形を作る，(10) 垂心を標識点として付加する，(11) 標識点から三辺への垂足三点をとる，(12) 三点を頂点とする向き付き三角形を作る，(13) 垂心を標識点として付加する，(14) 標識点を三辺に関して反射した三点をとる，(15) 三点を頂点とする向き付き三角形を作る，(16) 反中点三角形へ移す，(17) 垂足三角形へ移す，(18) 三辺の中点三角形へ移す，(19) 重心・面積・向きを固定して相似正規化する，(20) 相似類のモジュライ点へ射影する，(21) ここまでの合成が誘導する写像を反復する，(22) 退化三角形を境界として軌道をコンパクト化する，(23) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `MedialTransform → OrthicTransform → SymmedianMark → CevianTrace → TriangleFormation → AnticomplementaryTransform → IncenterMark → PedalProjection → TriangleFormation → OrthocenterMark → PedalProjection → TriangleFormation → OrthocenterMark → SideReflectionTrace → TriangleFormation → AnticomplementaryTransform → OrthicTransform → MedialTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### Markov関手と到達時刻不変量（DoobTransform・StateLumping・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.1ac6cea2ea`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `28`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 正の固有関数によるDoob変換を施す，(2) 自己同型軌道に沿って強 lumping する，(3) 定常分布に関する時間反転をとる，(4) 正の固有関数によるDoob変換を施す，(5) 定常分布に関する時間反転をとる，(6) 自己同型軌道に沿って強 lumping する，(7) 正の固有関数によるDoob変換を施す，(8) 定常分布に関する時間反転をとる，(9) 自己同型軌道に沿って強 lumping する，(10) 定常分布に関する時間反転をとる，(11) 自己同型軌道に沿って強 lumping する，(12) 自身との同期積連鎖を作る，(13) 恒等遷移との凸結合でlazy化する，(14) 正の固有関数によるDoob変換を施す，(15) 恒等遷移との凸結合でlazy化する，(16) 自身との同期積連鎖を作る，(17) 恒等遷移との凸結合でlazy化する，(18) 自身との同期積連鎖を作る，(19) 恒等遷移との凸結合でlazy化する，(20) 指定集合で吸収させ過渡核をとる，(21) 過渡核のGreen作用素をとる，(22) 到達時刻の高次モーメント連立系を作る，(23) モーメント次数方向の漸化式を抽出する，(24) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DoobTransform → StateLumping → TimeReversal → DoobTransform → TimeReversal → StateLumping → DoobTransform → TimeReversal → StateLumping → TimeReversal → StateLumping → ProductChain → LazyPerturbation → DoobTransform → LazyPerturbation → ProductChain → LazyPerturbation → ProductChain → LazyPerturbation → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 凸体関手の合成力学（CentroidBody・ProjectionBody・DifferenceBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.f28a39cacf`
- 状態: `unresolved_by_mathos`
- 射数: `23`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `26`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重心体をとる，(2) 射影体をとる，(3) 重心体をとる，(4) 射影体をとる，(5) 自身と極体のMinkowski和をとる，(6) 主慣性軸方向にSteiner対称化する，(7) 差体をとる，(8) 射影体をとる，(9) 交叉体をとる，(10) 主慣性軸方向にSteiner対称化する，(11) 重心体をとる，(12) 原点に関する極体をとる，(13) 自身と極体のMinkowski和をとる，(14) 原点に関する極体をとる，(15) 交叉体をとる，(16) 主慣性軸方向にSteiner対称化する，(17) 交叉体をとる，(18) 原点に関する極体をとる，(19) 差体をとる，(20) 自身と極体のMinkowski和をとる，(21) 差体をとる，(22) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CentroidBody → ProjectionBody → CentroidBody → ProjectionBody → MinkowskiPolarSum → SteinerSymmetrization → DifferenceBody → ProjectionBody → IntersectionBody → SteinerSymmetrization → CentroidBody → PolarDual → MinkowskiPolarSum → PolarDual → IntersectionBody → SteinerSymmetrization → IntersectionBody → PolarDual → DifferenceBody → MinkowskiPolarSum → DifferenceBody → VolumeNormalization → ConvexFixedPointQuery`

### 多項式変換と算術観測（RootMultiset・PolynomialReconstruction・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.b8139b30e6`
- 状態: `unresolved_by_mathos`
- 射数: `23`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `27`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重複度付き根配置へ移す，(2) 根配置からモニック多項式を再構成する，(3) 根を二乗するGraeffe変換を施す，(4) 根を逆数へ移す相反多項式をとる，(5) 根の重心を0へ移す平行移動共役を施す，(6) 導関数をモニックに再正規化する，(7) 根の重心を0へ移す平行移動共役を施す，(8) 根を二乗するGraeffe変換を施す，(9) 導関数をモニックに再正規化する，(10) 臨界値を根にもつ消去多項式を作る，(11) 根を二乗するGraeffe変換を施す，(12) 重複度付き根配置へ移す，(13) 根配置からモニック多項式を再構成する，(14) 根を逆数へ移す相反多項式をとる，(15) 臨界値を根にもつ消去多項式を作る，(16) 根の重心を0へ移す平行移動共役を施す，(17) 重複度付き根配置へ移す，(18) 根の冪和モーメント列を作る，(19) モーメントからHankel行列族を作る，(20) 主小行列式列をとる，(21) 満たす最小線形漸化式を抽出する，(22) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `RootMultiset → PolynomialReconstruction → GraeffeTransform → ReciprocalPolynomial → ShiftConjugacy → DerivativeRenormalization → ShiftConjugacy → GraeffeTransform → DerivativeRenormalization → CriticalValuePolynomial → GraeffeTransform → RootMultiset → PolynomialReconstruction → ReciprocalPolynomial → CriticalValuePolynomial → ShiftConjugacy → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 平面代数曲線の合成変換（Catacaustic・Evolute・PolarReciprocal・OffsetCurve）

- ID: `research.autonomous.plane_curve.0de82c3bf1`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `birational_periodicity`
- 難度仮説: `28`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定光源からの反射光線族の包絡線をとる，(2) 法線族の包絡線である発展曲線をとる，(3) 固定光源からの反射光線族の包絡線をとる，(4) 固定非退化二次形式に関する極逆像をとる，(5) 定義多項式のHessian曲線をとる，(6) 固定基準三角形に関する等角共役Cremona像をとる，(7) 正則接線族の射影双対曲線をとる，(8) 固定非退化二次形式に関する極逆像をとる，(9) 正則接線族の射影双対曲線をとる，(10) 原点中心の円反転像をとる，(11) 固定基準三角形に関する等角共役Cremona像をとる，(12) 原点中心の円反転像をとる，(13) 法線族の包絡線である発展曲線をとる，(14) 定義多項式のHessian曲線をとる，(15) 固定基準三角形に関する等角共役Cremona像をとる，(16) 固定非退化二次形式に関する極逆像をとる，(17) 固定基準三角形に関する等角共役Cremona像をとる，(18) 法線方向の代数的平行曲線をとる，(19) 射影閉包をとり無限遠点を加える，(20) 基点を避ける一般アフィンチャートへ移す，(21) 正則接線族の射影双対曲線をとる，(22) 法線方向の代数的平行曲線をとる，(23) 固定非退化二次形式に関する極逆像をとる，(24) 法線方向の代数的平行曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `Catacaustic → Evolute → Catacaustic → PolarReciprocal → HessianCurve → IsogonalCremona → ProjectiveDual → PolarReciprocal → ProjectiveDual → CircleInversion → IsogonalCremona → CircleInversion → Evolute → HessianCurve → IsogonalCremona → PolarReciprocal → IsogonalCremona → OffsetCurve → ProjectiveClosure → AffineChartChange → ProjectiveDual → OffsetCurve → PolarReciprocal → OffsetCurve → BirationalPeriodQuery`

### 三角形変換の合成力学（OrthicTransform・CentroidMark・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.63e801762c`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `31`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 垂足三角形へ移す，(2) 重心を標識点として付加する，(3) 標識点を三辺に関して反射した三点をとる，(4) 三点を頂点とする向き付き三角形を作る，(5) 重心を標識点として付加する，(6) 標識点から三辺への垂足三点をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 内心を標識点として付加する，(9) 各頂点と標識点が定める円の対応交点をとる，(10) 三点を頂点とする向き付き三角形を作る，(11) 傍心三角形へ移す，(12) 三辺の中点三角形へ移す，(13) 垂心を標識点として付加する，(14) 標識点から三辺への垂足三点をとる，(15) 三点を頂点とする向き付き三角形を作る，(16) 三辺の中点三角形へ移す，(17) 傍心三角形へ移す，(18) 反中点三角形へ移す，(19) 垂足三角形へ移す，(20) 反中点三角形へ移す，(21) 重心・面積・向きを固定して相似正規化する，(22) 相似類のモジュライ点へ射影する，(23) ここまでの合成が誘導する写像を反復する，(24) 退化三角形を境界として軌道をコンパクト化する，(25) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `OrthicTransform → CentroidMark → SideReflectionTrace → TriangleFormation → CentroidMark → PedalProjection → TriangleFormation → IncenterMark → VertexCircleTrace → TriangleFormation → ExcentralTransform → MedialTransform → OrthocenterMark → PedalProjection → TriangleFormation → MedialTransform → ExcentralTransform → AnticomplementaryTransform → OrthicTransform → AnticomplementaryTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### Markov関手と到達時刻不変量（StateLumping・TimeReversal・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.6b21d466af`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `27`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自己同型軌道に沿って強 lumping する，(2) 定常分布に関する時間反転をとる，(3) 正の固有関数によるDoob変換を施す，(4) 恒等遷移との凸結合でlazy化する，(5) 自己同型軌道に沿って強 lumping する，(6) 定常分布に関する時間反転をとる，(7) 正の固有関数によるDoob変換を施す，(8) 定常分布に関する時間反転をとる，(9) 自己同型軌道に沿って強 lumping する，(10) 正の固有関数によるDoob変換を施す，(11) 定常分布に関する時間反転をとる，(12) 恒等遷移との凸結合でlazy化する，(13) 自身との同期積連鎖を作る，(14) 自己同型軌道に沿って強 lumping する，(15) 恒等遷移との凸結合でlazy化する，(16) 正の固有関数によるDoob変換を施す，(17) 恒等遷移との凸結合でlazy化する，(18) 自身との同期積連鎖を作る，(19) 指定集合で吸収させ過渡核をとる，(20) 過渡核のGreen作用素をとる，(21) 到達時刻の高次モーメント連立系を作る，(22) モーメント次数方向の漸化式を抽出する，(23) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `StateLumping → TimeReversal → DoobTransform → LazyPerturbation → StateLumping → TimeReversal → DoobTransform → TimeReversal → StateLumping → DoobTransform → TimeReversal → LazyPerturbation → ProductChain → StateLumping → LazyPerturbation → DoobTransform → LazyPerturbation → ProductChain → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 凸体関手の合成力学（DifferenceBody・ProjectionBody・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.a0d618dfa9`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `convex_body_dynamics`
- 難度仮説: `29`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 差体をとる，(2) 射影体をとる，(3) 原点に関する極体をとる，(4) 重心体をとる，(5) 差体をとる，(6) 射影体をとる，(7) 原点に関する極体をとる，(8) 射影体をとる，(9) 原点に関する極体をとる，(10) 主慣性軸方向にSteiner対称化する，(11) 射影体をとる，(12) 交叉体をとる，(13) 重心体をとる，(14) 差体をとる，(15) 主慣性軸方向にSteiner対称化する，(16) 差体をとる，(17) 原点に関する極体をとる，(18) 交叉体をとる，(19) 自身と極体のMinkowski和をとる，(20) 交叉体をとる，(21) 面積と二次モーメントを固定して正規化する，(22) ここまでの凸体関手を反復する，(23) 支持関数の軌道へ移す，(24) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DifferenceBody → ProjectionBody → PolarDual → CentroidBody → DifferenceBody → ProjectionBody → PolarDual → ProjectionBody → PolarDual → SteinerSymmetrization → ProjectionBody → IntersectionBody → CentroidBody → DifferenceBody → SteinerSymmetrization → DifferenceBody → PolarDual → IntersectionBody → MinkowskiPolarSum → IntersectionBody → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 平面代数曲線の合成変換（Catacaustic・CircleInversion・ProjectiveDual・HessianCurve）

- ID: `research.autonomous.plane_curve.a3144d0d3d`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `birational_periodicity`
- 難度仮説: `28`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定光源からの反射光線族の包絡線をとる，(2) 原点中心の円反転像をとる，(3) 法線方向の代数的平行曲線をとる，(4) 定義多項式のHessian曲線をとる，(5) 固定非退化二次形式に関する極逆像をとる，(6) 定義多項式のHessian曲線をとる，(7) 固定基準三角形に関する等角共役Cremona像をとる，(8) 法線族の包絡線である発展曲線をとる，(9) 原点中心の円反転像をとる，(10) 正則接線族の射影双対曲線をとる，(11) 法線方向の代数的平行曲線をとる，(12) 固定非退化二次形式に関する極逆像をとる，(13) 原点中心の円反転像をとる，(14) 法線族の包絡線である発展曲線をとる，(15) 定義多項式のHessian曲線をとる，(16) 固定光源からの反射光線族の包絡線をとる，(17) 固定基準三角形に関する等角共役Cremona像をとる，(18) 原点中心の円反転像をとる，(19) 正則接線族の射影双対曲線をとる，(20) 固定非退化二次形式に関する極逆像をとる，(21) 固定光源からの反射光線族の包絡線をとる，(22) 固定非退化二次形式に関する極逆像をとる，(23) 正則接線族の射影双対曲線をとる，(24) 定義多項式のHessian曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `Catacaustic → CircleInversion → OffsetCurve → HessianCurve → PolarReciprocal → HessianCurve → IsogonalCremona → Evolute → CircleInversion → ProjectiveDual → OffsetCurve → PolarReciprocal → CircleInversion → Evolute → HessianCurve → Catacaustic → IsogonalCremona → CircleInversion → ProjectiveDual → PolarReciprocal → Catacaustic → PolarReciprocal → ProjectiveDual → HessianCurve → BirationalPeriodQuery`

### 多項式変換と算術観測（ReciprocalPolynomial・ShiftConjugacy・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.d6de2cadd7`
- 状態: `unresolved_by_mathos`
- 射数: `27`
- 問い: `recurrence_order_drop`
- 難度仮説: `31`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を逆数へ移す相反多項式をとる，(2) 根の重心を0へ移す平行移動共役を施す，(3) 導関数をモニックに再正規化する，(4) 根を逆数へ移す相反多項式をとる，(5) 臨界値を根にもつ消去多項式を作る，(6) 根を二乗するGraeffe変換を施す，(7) 根の重心を0へ移す平行移動共役を施す，(8) 導関数をモニックに再正規化する，(9) 根を二乗するGraeffe変換を施す，(10) 根の重心を0へ移す平行移動共役を施す，(11) 根を二乗するGraeffe変換を施す，(12) 根の重心を0へ移す平行移動共役を施す，(13) 根を二乗するGraeffe変換を施す，(14) 重複度付き根配置へ移す，(15) 根配置からモニック多項式を再構成する，(16) 臨界値を根にもつ消去多項式を作る，(17) 重複度付き根配置へ移す，(18) 根配置からモニック多項式を再構成する，(19) 重複度付き根配置へ移す，(20) 根配置からモニック多項式を再構成する，(21) 根を逆数へ移す相反多項式をとる，(22) 重複度付き根配置へ移す，(23) 根の冪和モーメント列を作る，(24) モーメントからHankel行列族を作る，(25) 主小行列式列をとる，(26) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ReciprocalPolynomial → ShiftConjugacy → DerivativeRenormalization → ReciprocalPolynomial → CriticalValuePolynomial → GraeffeTransform → ShiftConjugacy → DerivativeRenormalization → GraeffeTransform → ShiftConjugacy → GraeffeTransform → ShiftConjugacy → GraeffeTransform → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → RootMultiset → PolynomialReconstruction → ReciprocalPolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 三角形変換の合成力学（OrthocenterMark・SideReflectionTrace・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.26cfb3eade`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `31`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 垂心を標識点として付加する，(2) 標識点を三辺に関して反射した三点をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 三辺の中点三角形へ移す，(5) 垂足三角形へ移す，(6) 垂心を標識点として付加する，(7) 各頂点と標識点が定める円の対応交点をとる，(8) 三点を頂点とする向き付き三角形を作る，(9) 外心を標識点として付加する，(10) 標識点から三辺への垂足三点をとる，(11) 三点を頂点とする向き付き三角形を作る，(12) 重心を標識点として付加する，(13) 標識点から三辺への垂足三点をとる，(14) 三点を頂点とする向き付き三角形を作る，(15) 反中点三角形へ移す，(16) 傍心三角形へ移す，(17) 反中点三角形へ移す，(18) 傍心三角形へ移す，(19) 反中点三角形へ移す，(20) 垂足三角形へ移す，(21) 重心・面積・向きを固定して相似正規化する，(22) 相似類のモジュライ点へ射影する，(23) ここまでの合成が誘導する写像を反復する，(24) 退化三角形を境界として軌道をコンパクト化する，(25) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `OrthocenterMark → SideReflectionTrace → TriangleFormation → MedialTransform → OrthicTransform → OrthocenterMark → VertexCircleTrace → TriangleFormation → CircumcenterMark → PedalProjection → TriangleFormation → CentroidMark → PedalProjection → TriangleFormation → AnticomplementaryTransform → ExcentralTransform → AnticomplementaryTransform → ExcentralTransform → AnticomplementaryTransform → OrthicTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### Markov関手と到達時刻不変量（ProductChain・TimeReversal・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.ffcc60ba30`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `27`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身との同期積連鎖を作る，(2) 定常分布に関する時間反転をとる，(3) 自己同型軌道に沿って強 lumping する，(4) 恒等遷移との凸結合でlazy化する，(5) 自己同型軌道に沿って強 lumping する，(6) 恒等遷移との凸結合でlazy化する，(7) 正の固有関数によるDoob変換を施す，(8) 自身との同期積連鎖を作る，(9) 恒等遷移との凸結合でlazy化する，(10) 自身との同期積連鎖を作る，(11) 恒等遷移との凸結合でlazy化する，(12) 定常分布に関する時間反転をとる，(13) 正の固有関数によるDoob変換を施す，(14) 自己同型軌道に沿って強 lumping する，(15) 正の固有関数によるDoob変換を施す，(16) 自身との同期積連鎖を作る，(17) 正の固有関数によるDoob変換を施す，(18) 定常分布に関する時間反転をとる，(19) 自己同型軌道に沿って強 lumping する，(20) 指定集合で吸収させ過渡核をとる，(21) 過渡核のGreen作用素をとる，(22) 到達時刻の高次モーメント連立系を作る，(23) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProductChain → TimeReversal → StateLumping → LazyPerturbation → StateLumping → LazyPerturbation → DoobTransform → ProductChain → LazyPerturbation → ProductChain → LazyPerturbation → TimeReversal → DoobTransform → StateLumping → DoobTransform → ProductChain → DoobTransform → TimeReversal → StateLumping → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 平面代数曲線の合成変換（OffsetCurve・PolarReciprocal・Evolute・CircleInversion）

- ID: `research.autonomous.plane_curve.fab4bd61bb`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `birational_periodicity`
- 難度仮説: `27`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 法線方向の代数的平行曲線をとる，(2) 固定非退化二次形式に関する極逆像をとる，(3) 定義多項式のHessian曲線をとる，(4) 法線方向の代数的平行曲線をとる，(5) 法線族の包絡線である発展曲線をとる，(6) 定義多項式のHessian曲線をとる，(7) 法線方向の代数的平行曲線をとる，(8) 正則接線族の射影双対曲線をとる，(9) 固定光源からの反射光線族の包絡線をとる，(10) 原点中心の円反転像をとる，(11) 定義多項式のHessian曲線をとる，(12) 法線族の包絡線である発展曲線をとる，(13) 正則接線族の射影双対曲線をとる，(14) 定義多項式のHessian曲線をとる，(15) 固定基準三角形に関する等角共役Cremona像をとる，(16) 原点中心の円反転像をとる，(17) 射影閉包をとり無限遠点を加える，(18) 基点を避ける一般アフィンチャートへ移す，(19) 射影閉包をとり無限遠点を加える，(20) 基点を避ける一般アフィンチャートへ移す，(21) 正則接線族の射影双対曲線をとる，(22) 法線族の包絡線である発展曲線をとる，(23) 原点中心の円反転像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `OffsetCurve → PolarReciprocal → HessianCurve → OffsetCurve → Evolute → HessianCurve → OffsetCurve → ProjectiveDual → Catacaustic → CircleInversion → HessianCurve → Evolute → ProjectiveDual → HessianCurve → IsogonalCremona → CircleInversion → ProjectiveClosure → AffineChartChange → ProjectiveClosure → AffineChartChange → ProjectiveDual → Evolute → CircleInversion → BirationalPeriodQuery`

### 凸体関手の合成力学（PolarDual・ProjectionBody・IntersectionBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.919c5772f7`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `28`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 原点に関する極体をとる，(2) 射影体をとる，(3) 原点に関する極体をとる，(4) 射影体をとる，(5) 主慣性軸方向にSteiner対称化する，(6) 原点に関する極体をとる，(7) 交叉体をとる，(8) 自身と極体のMinkowski和をとる，(9) 射影体をとる，(10) 差体をとる，(11) 重心体をとる，(12) 主慣性軸方向にSteiner対称化する，(13) 射影体をとる，(14) 自身と極体のMinkowski和をとる，(15) 交叉体をとる，(16) 主慣性軸方向にSteiner対称化する，(17) 差体をとる，(18) 主慣性軸方向にSteiner対称化する，(19) 交叉体をとる，(20) 原点に関する極体をとる，(21) 自身と極体のMinkowski和をとる，(22) 重心体をとる，(23) 交叉体をとる，(24) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `PolarDual → ProjectionBody → PolarDual → ProjectionBody → SteinerSymmetrization → PolarDual → IntersectionBody → MinkowskiPolarSum → ProjectionBody → DifferenceBody → CentroidBody → SteinerSymmetrization → ProjectionBody → MinkowskiPolarSum → IntersectionBody → SteinerSymmetrization → DifferenceBody → SteinerSymmetrization → IntersectionBody → PolarDual → MinkowskiPolarSum → CentroidBody → IntersectionBody → VolumeNormalization → ConvexFixedPointQuery`

### 多項式変換と算術観測（RootMultiset・PolynomialReconstruction・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.49a319bd32`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重複度付き根配置へ移す，(2) 根配置からモニック多項式を再構成する，(3) 臨界値を根にもつ消去多項式を作る，(4) 導関数をモニックに再正規化する，(5) 根を二乗するGraeffe変換を施す，(6) 根を逆数へ移す相反多項式をとる，(7) 導関数をモニックに再正規化する，(8) 根を二乗するGraeffe変換を施す，(9) 根の重心を0へ移す平行移動共役を施す，(10) 根を二乗するGraeffe変換を施す，(11) 重複度付き根配置へ移す，(12) 根配置からモニック多項式を再構成する，(13) 重複度付き根配置へ移す，(14) 根配置からモニック多項式を再構成する，(15) 根の重心を0へ移す平行移動共役を施す，(16) 根を逆数へ移す相反多項式をとる，(17) 導関数をモニックに再正規化する，(18) 根を逆数へ移す相反多項式をとる，(19) 臨界値を根にもつ消去多項式を作る，(20) 重複度付き根配置へ移す，(21) 根の冪和モーメント列を作る，(22) モーメントからHankel行列族を作る，(23) 主小行列式列をとる，(24) 満たす最小線形漸化式を抽出する，(25) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → DerivativeRenormalization → GraeffeTransform → ReciprocalPolynomial → DerivativeRenormalization → GraeffeTransform → ShiftConjugacy → GraeffeTransform → RootMultiset → PolynomialReconstruction → RootMultiset → PolynomialReconstruction → ShiftConjugacy → ReciprocalPolynomial → DerivativeRenormalization → ReciprocalPolynomial → CriticalValuePolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 三角形変換の合成力学（SymmedianMark・VertexCircleTrace・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.adec13efcc`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `31`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 類似重心を標識点として付加する，(2) 各頂点と標識点が定める円の対応交点をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 外心を標識点として付加する，(5) 標識点から三辺への垂足三点をとる，(6) 三点を頂点とする向き付き三角形を作る，(7) 傍心三角形へ移す，(8) 反中点三角形へ移す，(9) 傍心三角形へ移す，(10) 重心を標識点として付加する，(11) 各頂点と標識点が定める円の対応交点をとる，(12) 三点を頂点とする向き付き三角形を作る，(13) 内心を標識点として付加する，(14) 標識点を三辺に関して反射した三点をとる，(15) 三点を頂点とする向き付き三角形を作る，(16) 反中点三角形へ移す，(17) 垂足三角形へ移す，(18) 反中点三角形へ移す，(19) 垂足三角形へ移す，(20) 反中点三角形へ移す，(21) 重心・面積・向きを固定して相似正規化する，(22) 相似類のモジュライ点へ射影する，(23) ここまでの合成が誘導する写像を反復する，(24) 退化三角形を境界として軌道をコンパクト化する，(25) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `SymmedianMark → VertexCircleTrace → TriangleFormation → CircumcenterMark → PedalProjection → TriangleFormation → ExcentralTransform → AnticomplementaryTransform → ExcentralTransform → CentroidMark → VertexCircleTrace → TriangleFormation → IncenterMark → SideReflectionTrace → TriangleFormation → AnticomplementaryTransform → OrthicTransform → AnticomplementaryTransform → OrthicTransform → AnticomplementaryTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### Markov関手と到達時刻不変量（ProductChain・TimeReversal・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.a2a4a91146`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `28`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身との同期積連鎖を作る，(2) 定常分布に関する時間反転をとる，(3) 正の固有関数によるDoob変換を施す，(4) 自身との同期積連鎖を作る，(5) 自己同型軌道に沿って強 lumping する，(6) 自身との同期積連鎖を作る，(7) 定常分布に関する時間反転をとる，(8) 自己同型軌道に沿って強 lumping する，(9) 自身との同期積連鎖を作る，(10) 正の固有関数によるDoob変換を施す，(11) 自己同型軌道に沿って強 lumping する，(12) 定常分布に関する時間反転をとる，(13) 正の固有関数によるDoob変換を施す，(14) 定常分布に関する時間反転をとる，(15) 恒等遷移との凸結合でlazy化する，(16) 自己同型軌道に沿って強 lumping する，(17) 恒等遷移との凸結合でlazy化する，(18) 正の固有関数によるDoob変換を施す，(19) 恒等遷移との凸結合でlazy化する，(20) 指定集合で吸収させ過渡核をとる，(21) 過渡核のGreen作用素をとる，(22) 到達時刻の高次モーメント連立系を作る，(23) モーメント次数方向の漸化式を抽出する，(24) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProductChain → TimeReversal → DoobTransform → ProductChain → StateLumping → ProductChain → TimeReversal → StateLumping → ProductChain → DoobTransform → StateLumping → TimeReversal → DoobTransform → TimeReversal → LazyPerturbation → StateLumping → LazyPerturbation → DoobTransform → LazyPerturbation → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 凸体関手の合成力学（ProjectionBody・IntersectionBody・IntersectionBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.636b77f8b9`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `29`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 射影体をとる，(2) 交叉体をとる，(3) 自身と極体のMinkowski和をとる，(4) 差体をとる，(5) 射影体をとる，(6) 重心体をとる，(7) 原点に関する極体をとる，(8) 射影体をとる，(9) 主慣性軸方向にSteiner対称化する，(10) 差体をとる，(11) 重心体をとる，(12) 主慣性軸方向にSteiner対称化する，(13) 差体をとる，(14) 射影体をとる，(15) 原点に関する極体をとる，(16) 自身と極体のMinkowski和をとる，(17) 原点に関する極体をとる，(18) 主慣性軸方向にSteiner対称化する，(19) 差体をとる，(20) 原点に関する極体をとる，(21) 自身と極体のMinkowski和をとる，(22) 主慣性軸方向にSteiner対称化する，(23) 重心体をとる，(24) 交叉体をとる，(25) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectionBody → IntersectionBody → MinkowskiPolarSum → DifferenceBody → ProjectionBody → CentroidBody → PolarDual → ProjectionBody → SteinerSymmetrization → DifferenceBody → CentroidBody → SteinerSymmetrization → DifferenceBody → ProjectionBody → PolarDual → MinkowskiPolarSum → PolarDual → SteinerSymmetrization → DifferenceBody → PolarDual → MinkowskiPolarSum → SteinerSymmetrization → CentroidBody → IntersectionBody → VolumeNormalization → ConvexFixedPointQuery`

### 平面代数曲線の合成変換（Evolute・HessianCurve・PolarReciprocal・IsogonalCremona）

- ID: `research.autonomous.plane_curve.6a2921ebcf`
- 状態: `unresolved_by_mathos`
- 射数: `27`
- 問い: `birational_periodicity`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 法線族の包絡線である発展曲線をとる，(2) 定義多項式のHessian曲線をとる，(3) 射影閉包をとり無限遠点を加える，(4) 基点を避ける一般アフィンチャートへ移す，(5) 固定光源からの反射光線族の包絡線をとる，(6) 射影閉包をとり無限遠点を加える，(7) 基点を避ける一般アフィンチャートへ移す，(8) 射影閉包をとり無限遠点を加える，(9) 基点を避ける一般アフィンチャートへ移す，(10) 法線方向の代数的平行曲線をとる，(11) 固定基準三角形に関する等角共役Cremona像をとる，(12) 固定非退化二次形式に関する極逆像をとる，(13) 法線方向の代数的平行曲線をとる，(14) 固定非退化二次形式に関する極逆像をとる，(15) 正則接線族の射影双対曲線をとる，(16) 固定光源からの反射光線族の包絡線をとる，(17) 射影閉包をとり無限遠点を加える，(18) 基点を避ける一般アフィンチャートへ移す，(19) 原点中心の円反転像をとる，(20) 法線族の包絡線である発展曲線をとる，(21) 原点中心の円反転像をとる，(22) 法線方向の代数的平行曲線をとる，(23) 定義多項式のHessian曲線をとる，(24) 固定基準三角形に関する等角共役Cremona像をとる，(25) 固定非退化二次形式に関する極逆像をとる，(26) 固定基準三角形に関する等角共役Cremona像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `Evolute → HessianCurve → ProjectiveClosure → AffineChartChange → Catacaustic → ProjectiveClosure → AffineChartChange → ProjectiveClosure → AffineChartChange → OffsetCurve → IsogonalCremona → PolarReciprocal → OffsetCurve → PolarReciprocal → ProjectiveDual → Catacaustic → ProjectiveClosure → AffineChartChange → CircleInversion → Evolute → CircleInversion → OffsetCurve → HessianCurve → IsogonalCremona → PolarReciprocal → IsogonalCremona → BirationalPeriodQuery`

### 多項式変換と算術観測（CriticalValuePolynomial・ReciprocalPolynomial・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.49208c8a91`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `recurrence_order_drop`
- 難度仮説: `27`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 臨界値を根にもつ消去多項式を作る，(2) 根を逆数へ移す相反多項式をとる，(3) 重複度付き根配置へ移す，(4) 根配置からモニック多項式を再構成する，(5) 根の重心を0へ移す平行移動共役を施す，(6) 導関数をモニックに再正規化する，(7) 根の重心を0へ移す平行移動共役を施す，(8) 臨界値を根にもつ消去多項式を作る，(9) 導関数をモニックに再正規化する，(10) 根の重心を0へ移す平行移動共役を施す，(11) 導関数をモニックに再正規化する，(12) 重複度付き根配置へ移す，(13) 根配置からモニック多項式を再構成する，(14) 導関数をモニックに再正規化する，(15) 臨界値を根にもつ消去多項式を作る，(16) 重複度付き根配置へ移す，(17) 根配置からモニック多項式を再構成する，(18) 臨界値を根にもつ消去多項式を作る，(19) 重複度付き根配置へ移す，(20) 根の冪和モーメント列を作る，(21) モーメントからHankel行列族を作る，(22) 主小行列式列をとる，(23) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CriticalValuePolynomial → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → ShiftConjugacy → DerivativeRenormalization → ShiftConjugacy → CriticalValuePolynomial → DerivativeRenormalization → ShiftConjugacy → DerivativeRenormalization → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 三角形変換の合成力学（IncenterMark・CevianTrace・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.86d5a38927`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `28`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0625`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 内心を標識点として付加する，(2) 標識点を通る三本のcevianの辺上の足をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 三辺の中点三角形へ移す，(5) 外心を標識点として付加する，(6) 標識点を三辺に関して反射した三点をとる，(7) 三点を頂点とする向き付き三角形を作る，(8) 反中点三角形へ移す，(9) 垂足三角形へ移す，(10) 反中点三角形へ移す，(11) 傍心三角形へ移す，(12) 反中点三角形へ移す，(13) 外心を標識点として付加する，(14) 標識点を通る三本のcevianの辺上の足をとる，(15) 三点を頂点とする向き付き三角形を作る，(16) 垂心を標識点として付加する，(17) 標識点から三辺への垂足三点をとる，(18) 三点を頂点とする向き付き三角形を作る，(19) 重心・面積・向きを固定して相似正規化する，(20) 相似類のモジュライ点へ射影する，(21) ここまでの合成が誘導する写像を反復する，(22) 退化三角形を境界として軌道をコンパクト化する，(23) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IncenterMark → CevianTrace → TriangleFormation → MedialTransform → CircumcenterMark → SideReflectionTrace → TriangleFormation → AnticomplementaryTransform → OrthicTransform → AnticomplementaryTransform → ExcentralTransform → AnticomplementaryTransform → CircumcenterMark → CevianTrace → TriangleFormation → OrthocenterMark → PedalProjection → TriangleFormation → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### Markov関手と到達時刻不変量（LazyPerturbation・DoobTransform・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.ee79d540ac`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `27`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 恒等遷移との凸結合でlazy化する，(2) 正の固有関数によるDoob変換を施す，(3) 恒等遷移との凸結合でlazy化する，(4) 自己同型軌道に沿って強 lumping する，(5) 定常分布に関する時間反転をとる，(6) 自己同型軌道に沿って強 lumping する，(7) 恒等遷移との凸結合でlazy化する，(8) 正の固有関数によるDoob変換を施す，(9) 自己同型軌道に沿って強 lumping する，(10) 恒等遷移との凸結合でlazy化する，(11) 正の固有関数によるDoob変換を施す，(12) 自己同型軌道に沿って強 lumping する，(13) 定常分布に関する時間反転をとる，(14) 自身との同期積連鎖を作る，(15) 正の固有関数によるDoob変換を施す，(16) 自身との同期積連鎖を作る，(17) 定常分布に関する時間反転をとる，(18) 自身との同期積連鎖を作る，(19) 指定集合で吸収させ過渡核をとる，(20) 過渡核のGreen作用素をとる，(21) 到達時刻の高次モーメント連立系を作る，(22) モーメント次数方向の漸化式を抽出する，(23) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `LazyPerturbation → DoobTransform → LazyPerturbation → StateLumping → TimeReversal → StateLumping → LazyPerturbation → DoobTransform → StateLumping → LazyPerturbation → DoobTransform → StateLumping → TimeReversal → ProductChain → DoobTransform → ProductChain → TimeReversal → ProductChain → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 平面代数曲線の合成変換（Evolute・OffsetCurve・CircleInversion・PolarReciprocal）

- ID: `research.autonomous.plane_curve.8964ee01f7`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `birational_periodicity`
- 難度仮説: `29`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 法線族の包絡線である発展曲線をとる，(2) 法線方向の代数的平行曲線をとる，(3) 射影閉包をとり無限遠点を加える，(4) 基点を避ける一般アフィンチャートへ移す，(5) 固定基準三角形に関する等角共役Cremona像をとる，(6) 法線族の包絡線である発展曲線をとる，(7) 射影閉包をとり無限遠点を加える，(8) 基点を避ける一般アフィンチャートへ移す，(9) 定義多項式のHessian曲線をとる，(10) 射影閉包をとり無限遠点を加える，(11) 基点を避ける一般アフィンチャートへ移す，(12) 固定光源からの反射光線族の包絡線をとる，(13) 射影閉包をとり無限遠点を加える，(14) 基点を避ける一般アフィンチャートへ移す，(15) 法線族の包絡線である発展曲線をとる，(16) 法線方向の代数的平行曲線をとる，(17) 固定光源からの反射光線族の包絡線をとる，(18) 固定非退化二次形式に関する極逆像をとる，(19) 法線方向の代数的平行曲線をとる，(20) 固定光源からの反射光線族の包絡線をとる，(21) 固定非退化二次形式に関する極逆像をとる，(22) 定義多項式のHessian曲線をとる，(23) 固定基準三角形に関する等角共役Cremona像をとる，(24) 原点中心の円反転像をとる，(25) 固定非退化二次形式に関する極逆像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `Evolute → OffsetCurve → ProjectiveClosure → AffineChartChange → IsogonalCremona → Evolute → ProjectiveClosure → AffineChartChange → HessianCurve → ProjectiveClosure → AffineChartChange → Catacaustic → ProjectiveClosure → AffineChartChange → Evolute → OffsetCurve → Catacaustic → PolarReciprocal → OffsetCurve → Catacaustic → PolarReciprocal → HessianCurve → IsogonalCremona → CircleInversion → PolarReciprocal → BirationalPeriodQuery`

### 凸体関手の合成力学（MinkowskiPolarSum・DifferenceBody・PolarDual・VolumeNormalization）

- ID: `research.autonomous.convex_body.693d415826`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `29`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身と極体のMinkowski和をとる，(2) 差体をとる，(3) 原点に関する極体をとる，(4) 差体をとる，(5) 自身と極体のMinkowski和をとる，(6) 主慣性軸方向にSteiner対称化する，(7) 交叉体をとる，(8) 差体をとる，(9) 重心体をとる，(10) 差体をとる，(11) 重心体をとる，(12) 自身と極体のMinkowski和をとる，(13) 射影体をとる，(14) 主慣性軸方向にSteiner対称化する，(15) 射影体をとる，(16) 原点に関する極体をとる，(17) 主慣性軸方向にSteiner対称化する，(18) 交叉体をとる，(19) 重心体をとる，(20) 自身と極体のMinkowski和をとる，(21) 主慣性軸方向にSteiner対称化する，(22) 交叉体をとる，(23) 射影体をとる，(24) 原点に関する極体をとる，(25) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `MinkowskiPolarSum → DifferenceBody → PolarDual → DifferenceBody → MinkowskiPolarSum → SteinerSymmetrization → IntersectionBody → DifferenceBody → CentroidBody → DifferenceBody → CentroidBody → MinkowskiPolarSum → ProjectionBody → SteinerSymmetrization → ProjectionBody → PolarDual → SteinerSymmetrization → IntersectionBody → CentroidBody → MinkowskiPolarSum → SteinerSymmetrization → IntersectionBody → ProjectionBody → PolarDual → VolumeNormalization → ConvexFixedPointQuery`

### 多項式変換と算術観測（CriticalValuePolynomial・GraeffeTransform・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.2d3dc706d2`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 臨界値を根にもつ消去多項式を作る，(2) 根を二乗するGraeffe変換を施す，(3) 導関数をモニックに再正規化する，(4) 臨界値を根にもつ消去多項式を作る，(5) 根を逆数へ移す相反多項式をとる，(6) 導関数をモニックに再正規化する，(7) 重複度付き根配置へ移す，(8) 根配置からモニック多項式を再構成する，(9) 重複度付き根配置へ移す，(10) 根配置からモニック多項式を再構成する，(11) 導関数をモニックに再正規化する，(12) 根の重心を0へ移す平行移動共役を施す，(13) 重複度付き根配置へ移す，(14) 根配置からモニック多項式を再構成する，(15) 根の重心を0へ移す平行移動共役を施す，(16) 根を逆数へ移す相反多項式をとる，(17) 導関数をモニックに再正規化する，(18) 根の重心を0へ移す平行移動共役を施す，(19) 根を逆数へ移す相反多項式をとる，(20) 重複度付き根配置へ移す，(21) 根の冪和モーメント列を作る，(22) モーメントからHankel行列族を作る，(23) 主小行列式列をとる，(24) 満たす最小線形漸化式を抽出する，(25) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CriticalValuePolynomial → GraeffeTransform → DerivativeRenormalization → CriticalValuePolynomial → ReciprocalPolynomial → DerivativeRenormalization → RootMultiset → PolynomialReconstruction → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → ShiftConjugacy → RootMultiset → PolynomialReconstruction → ShiftConjugacy → ReciprocalPolynomial → DerivativeRenormalization → ShiftConjugacy → ReciprocalPolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 三角形変換の合成力学（MedialTransform・OrthicTransform・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.85f9fc5d21`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `29`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 三辺の中点三角形へ移す，(2) 垂足三角形へ移す，(3) 外心を標識点として付加する，(4) 各頂点と標識点が定める円の対応交点をとる，(5) 三点を頂点とする向き付き三角形を作る，(6) 重心を標識点として付加する，(7) 各頂点と標識点が定める円の対応交点をとる，(8) 三点を頂点とする向き付き三角形を作る，(9) 反中点三角形へ移す，(10) 外心を標識点として付加する，(11) 標識点から三辺への垂足三点をとる，(12) 三点を頂点とする向き付き三角形を作る，(13) 内心を標識点として付加する，(14) 各頂点と標識点が定める円の対応交点をとる，(15) 三点を頂点とする向き付き三角形を作る，(16) 反中点三角形へ移す，(17) 垂足三角形へ移す，(18) 反中点三角形へ移す，(19) 傍心三角形へ移す，(20) 重心・面積・向きを固定して相似正規化する，(21) 相似類のモジュライ点へ射影する，(22) ここまでの合成が誘導する写像を反復する，(23) 退化三角形を境界として軌道をコンパクト化する，(24) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `MedialTransform → OrthicTransform → CircumcenterMark → VertexCircleTrace → TriangleFormation → CentroidMark → VertexCircleTrace → TriangleFormation → AnticomplementaryTransform → CircumcenterMark → PedalProjection → TriangleFormation → IncenterMark → VertexCircleTrace → TriangleFormation → AnticomplementaryTransform → OrthicTransform → AnticomplementaryTransform → ExcentralTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### Markov関手と到達時刻不変量（StateLumping・TimeReversal・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.bce1715d72`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `27`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自己同型軌道に沿って強 lumping する，(2) 定常分布に関する時間反転をとる，(3) 自己同型軌道に沿って強 lumping する，(4) 定常分布に関する時間反転をとる，(5) 正の固有関数によるDoob変換を施す，(6) 定常分布に関する時間反転をとる，(7) 自身との同期積連鎖を作る，(8) 正の固有関数によるDoob変換を施す，(9) 自己同型軌道に沿って強 lumping する，(10) 定常分布に関する時間反転をとる，(11) 自身との同期積連鎖を作る，(12) 正の固有関数によるDoob変換を施す，(13) 恒等遷移との凸結合でlazy化する，(14) 自身との同期積連鎖を作る，(15) 正の固有関数によるDoob変換を施す，(16) 恒等遷移との凸結合でlazy化する，(17) 自己同型軌道に沿って強 lumping する，(18) 恒等遷移との凸結合でlazy化する，(19) 自身との同期積連鎖を作る，(20) 指定集合で吸収させ過渡核をとる，(21) 過渡核のGreen作用素をとる，(22) 到達時刻の高次モーメント連立系を作る，(23) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `StateLumping → TimeReversal → StateLumping → TimeReversal → DoobTransform → TimeReversal → ProductChain → DoobTransform → StateLumping → TimeReversal → ProductChain → DoobTransform → LazyPerturbation → ProductChain → DoobTransform → LazyPerturbation → StateLumping → LazyPerturbation → ProductChain → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 凸体関手の合成力学（SteinerSymmetrization・CentroidBody・MinkowskiPolarSum・VolumeNormalization）

- ID: `research.autonomous.convex_body.3a60f40db8`
- 状態: `unresolved_by_mathos`
- 射数: `24`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `27`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 主慣性軸方向にSteiner対称化する，(2) 重心体をとる，(3) 交叉体をとる，(4) 原点に関する極体をとる，(5) 自身と極体のMinkowski和をとる，(6) 重心体をとる，(7) 差体をとる，(8) 主慣性軸方向にSteiner対称化する，(9) 差体をとる，(10) 重心体をとる，(11) 差体をとる，(12) 射影体をとる，(13) 主慣性軸方向にSteiner対称化する，(14) 原点に関する極体をとる，(15) 主慣性軸方向にSteiner対称化する，(16) 重心体をとる，(17) 差体をとる，(18) 原点に関する極体をとる，(19) 交叉体をとる，(20) 射影体をとる，(21) 交叉体をとる，(22) 自身と極体のMinkowski和をとる，(23) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `SteinerSymmetrization → CentroidBody → IntersectionBody → PolarDual → MinkowskiPolarSum → CentroidBody → DifferenceBody → SteinerSymmetrization → DifferenceBody → CentroidBody → DifferenceBody → ProjectionBody → SteinerSymmetrization → PolarDual → SteinerSymmetrization → CentroidBody → DifferenceBody → PolarDual → IntersectionBody → ProjectionBody → IntersectionBody → MinkowskiPolarSum → VolumeNormalization → ConvexFixedPointQuery`

### 平面代数曲線の合成変換（OffsetCurve・IsogonalCremona・HessianCurve・PolarReciprocal）

- ID: `research.autonomous.plane_curve.48e6ec0b47`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `birational_periodicity`
- 難度仮説: `28`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 法線方向の代数的平行曲線をとる，(2) 固定基準三角形に関する等角共役Cremona像をとる，(3) 射影閉包をとり無限遠点を加える，(4) 基点を避ける一般アフィンチャートへ移す，(5) 射影閉包をとり無限遠点を加える，(6) 基点を避ける一般アフィンチャートへ移す，(7) 法線族の包絡線である発展曲線をとる，(8) 正則接線族の射影双対曲線をとる，(9) 固定光源からの反射光線族の包絡線をとる，(10) 法線族の包絡線である発展曲線をとる，(11) 固定非退化二次形式に関する極逆像をとる，(12) 定義多項式のHessian曲線をとる，(13) 固定非退化二次形式に関する極逆像をとる，(14) 射影閉包をとり無限遠点を加える，(15) 基点を避ける一般アフィンチャートへ移す，(16) 固定非退化二次形式に関する極逆像をとる，(17) 固定基準三角形に関する等角共役Cremona像をとる，(18) 法線方向の代数的平行曲線をとる，(19) 正則接線族の射影双対曲線をとる，(20) 固定光源からの反射光線族の包絡線をとる，(21) 定義多項式のHessian曲線をとる，(22) 固定光源からの反射光線族の包絡線をとる，(23) 定義多項式のHessian曲線をとる，(24) 固定非退化二次形式に関する極逆像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `OffsetCurve → IsogonalCremona → ProjectiveClosure → AffineChartChange → ProjectiveClosure → AffineChartChange → Evolute → ProjectiveDual → Catacaustic → Evolute → PolarReciprocal → HessianCurve → PolarReciprocal → ProjectiveClosure → AffineChartChange → PolarReciprocal → IsogonalCremona → OffsetCurve → ProjectiveDual → Catacaustic → HessianCurve → Catacaustic → HessianCurve → PolarReciprocal → BirationalPeriodQuery`

### 多項式変換と算術観測（ShiftConjugacy・ReciprocalPolynomial・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.20c7dafdc8`
- 状態: `unresolved_by_mathos`
- 射数: `28`
- 問い: `recurrence_order_drop`
- 難度仮説: `32`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根の重心を0へ移す平行移動共役を施す，(2) 根を逆数へ移す相反多項式をとる，(3) 根を二乗するGraeffe変換を施す，(4) 根を逆数へ移す相反多項式をとる，(5) 根を二乗するGraeffe変換を施す，(6) 根を逆数へ移す相反多項式をとる，(7) 根の重心を0へ移す平行移動共役を施す，(8) 導関数をモニックに再正規化する，(9) 根を逆数へ移す相反多項式をとる，(10) 根の重心を0へ移す平行移動共役を施す，(11) 重複度付き根配置へ移す，(12) 根配置からモニック多項式を再構成する，(13) 臨界値を根にもつ消去多項式を作る，(14) 導関数をモニックに再正規化する，(15) 重複度付き根配置へ移す，(16) 根配置からモニック多項式を再構成する，(17) 根を二乗するGraeffe変換を施す，(18) 臨界値を根にもつ消去多項式を作る，(19) 導関数をモニックに再正規化する，(20) 根の重心を0へ移す平行移動共役を施す，(21) 根を二乗するGraeffe変換を施す，(22) 臨界値を根にもつ消去多項式を作る，(23) 重複度付き根配置へ移す，(24) 根の冪和モーメント列を作る，(25) モーメントからHankel行列族を作る，(26) 主小行列式列をとる，(27) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ShiftConjugacy → ReciprocalPolynomial → GraeffeTransform → ReciprocalPolynomial → GraeffeTransform → ReciprocalPolynomial → ShiftConjugacy → DerivativeRenormalization → ReciprocalPolynomial → ShiftConjugacy → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → DerivativeRenormalization → RootMultiset → PolynomialReconstruction → GraeffeTransform → CriticalValuePolynomial → DerivativeRenormalization → ShiftConjugacy → GraeffeTransform → CriticalValuePolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### Markov関手と到達時刻不変量（LazyPerturbation・TimeReversal・MomentRecurrence・DenominatorArithmetic）

- ID: `research.autonomous.markov_dynamics.77a87110c4`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `hitting_moment_arithmetic`
- 難度仮説: `28`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 恒等遷移との凸結合でlazy化する，(2) 定常分布に関する時間反転をとる，(3) 自身との同期積連鎖を作る，(4) 恒等遷移との凸結合でlazy化する，(5) 自己同型軌道に沿って強 lumping する，(6) 自身との同期積連鎖を作る，(7) 恒等遷移との凸結合でlazy化する，(8) 正の固有関数によるDoob変換を施す，(9) 定常分布に関する時間反転をとる，(10) 正の固有関数によるDoob変換を施す，(11) 定常分布に関する時間反転をとる，(12) 正の固有関数によるDoob変換を施す，(13) 自己同型軌道に沿って強 lumping する，(14) 自身との同期積連鎖を作る，(15) 正の固有関数によるDoob変換を施す，(16) 自己同型軌道に沿って強 lumping する，(17) 定常分布に関する時間反転をとる，(18) 自己同型軌道に沿って強 lumping する，(19) 自身との同期積連鎖を作る，(20) 指定集合で吸収させ過渡核をとる，(21) 過渡核のGreen作用素をとる，(22) 到達時刻の高次モーメント連立系を作る，(23) モーメント次数方向の漸化式を抽出する，(24) 既約分母と素数ごとの付値列を抽出する。最後に、付値列が周期的または有界となる連鎖を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `LazyPerturbation → TimeReversal → ProductChain → LazyPerturbation → StateLumping → ProductChain → LazyPerturbation → DoobTransform → TimeReversal → DoobTransform → TimeReversal → DoobTransform → StateLumping → ProductChain → DoobTransform → StateLumping → TimeReversal → StateLumping → ProductChain → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → DenominatorArithmetic → MarkovMomentQuery`

### 凸体関手の合成力学（IntersectionBody・ProjectionBody・CentroidBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.fc19ccde26`
- 状態: `unresolved_by_mathos`
- 射数: `28`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `31`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 交叉体をとる，(2) 射影体をとる，(3) 主慣性軸方向にSteiner対称化する，(4) 自身と極体のMinkowski和をとる，(5) 主慣性軸方向にSteiner対称化する，(6) 交叉体をとる，(7) 差体をとる，(8) 原点に関する極体をとる，(9) 射影体をとる，(10) 交叉体をとる，(11) 原点に関する極体をとる，(12) 差体をとる，(13) 自身と極体のMinkowski和をとる，(14) 交叉体をとる，(15) 主慣性軸方向にSteiner対称化する，(16) 自身と極体のMinkowski和をとる，(17) 差体をとる，(18) 自身と極体のMinkowski和をとる，(19) 主慣性軸方向にSteiner対称化する，(20) 射影体をとる，(21) 原点に関する極体をとる，(22) 差体をとる，(23) 重心体をとる，(24) 原点に関する極体をとる，(25) 射影体をとる，(26) 重心体をとる，(27) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IntersectionBody → ProjectionBody → SteinerSymmetrization → MinkowskiPolarSum → SteinerSymmetrization → IntersectionBody → DifferenceBody → PolarDual → ProjectionBody → IntersectionBody → PolarDual → DifferenceBody → MinkowskiPolarSum → IntersectionBody → SteinerSymmetrization → MinkowskiPolarSum → DifferenceBody → MinkowskiPolarSum → SteinerSymmetrization → ProjectionBody → PolarDual → DifferenceBody → CentroidBody → PolarDual → ProjectionBody → CentroidBody → VolumeNormalization → ConvexFixedPointQuery`

### 平面代数曲線の合成変換（IsogonalCremona・PolarReciprocal・ProjectiveDual・OffsetCurve）

- ID: `research.autonomous.plane_curve.815be7d5f1`
- 状態: `unresolved_by_mathos`
- 射数: `27`
- 問い: `birational_periodicity`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定基準三角形に関する等角共役Cremona像をとる，(2) 固定非退化二次形式に関する極逆像をとる，(3) 正則接線族の射影双対曲線をとる，(4) 射影閉包をとり無限遠点を加える，(5) 基点を避ける一般アフィンチャートへ移す，(6) 固定非退化二次形式に関する極逆像をとる，(7) 射影閉包をとり無限遠点を加える，(8) 基点を避ける一般アフィンチャートへ移す，(9) 定義多項式のHessian曲線をとる，(10) 固定光源からの反射光線族の包絡線をとる，(11) 固定非退化二次形式に関する極逆像をとる，(12) 固定基準三角形に関する等角共役Cremona像をとる，(13) 原点中心の円反転像をとる，(14) 法線族の包絡線である発展曲線をとる，(15) 正則接線族の射影双対曲線をとる，(16) 固定光源からの反射光線族の包絡線をとる，(17) 射影閉包をとり無限遠点を加える，(18) 基点を避ける一般アフィンチャートへ移す，(19) 原点中心の円反転像をとる，(20) 法線方向の代数的平行曲線をとる，(21) 定義多項式のHessian曲線をとる，(22) 法線方向の代数的平行曲線をとる，(23) 正則接線族の射影双対曲線をとる，(24) 定義多項式のHessian曲線をとる，(25) 正則接線族の射影双対曲線をとる，(26) 法線方向の代数的平行曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IsogonalCremona → PolarReciprocal → ProjectiveDual → ProjectiveClosure → AffineChartChange → PolarReciprocal → ProjectiveClosure → AffineChartChange → HessianCurve → Catacaustic → PolarReciprocal → IsogonalCremona → CircleInversion → Evolute → ProjectiveDual → Catacaustic → ProjectiveClosure → AffineChartChange → CircleInversion → OffsetCurve → HessianCurve → OffsetCurve → ProjectiveDual → HessianCurve → ProjectiveDual → OffsetCurve → BirationalPeriodQuery`

### 多項式変換と算術観測（ReciprocalPolynomial・RootMultiset・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.aaba8db90d`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `recurrence_order_drop`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を逆数へ移す相反多項式をとる，(2) 重複度付き根配置へ移す，(3) 根配置からモニック多項式を再構成する，(4) 根の重心を0へ移す平行移動共役を施す，(5) 根を逆数へ移す相反多項式をとる，(6) 重複度付き根配置へ移す，(7) 根配置からモニック多項式を再構成する，(8) 根を二乗するGraeffe変換を施す，(9) 根を逆数へ移す相反多項式をとる，(10) 根の重心を0へ移す平行移動共役を施す，(11) 根を逆数へ移す相反多項式をとる，(12) 重複度付き根配置へ移す，(13) 根配置からモニック多項式を再構成する，(14) 根を二乗するGraeffe変換を施す，(15) 臨界値を根にもつ消去多項式を作る，(16) 導関数をモニックに再正規化する，(17) 根を二乗するGraeffe変換を施す，(18) 臨界値を根にもつ消去多項式を作る，(19) 根の重心を0へ移す平行移動共役を施す，(20) 導関数をモニックに再正規化する，(21) 重複度付き根配置へ移す，(22) 根の冪和モーメント列を作る，(23) モーメントからHankel行列族を作る，(24) 主小行列式列をとる，(25) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → ShiftConjugacy → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → GraeffeTransform → ReciprocalPolynomial → ShiftConjugacy → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → GraeffeTransform → CriticalValuePolynomial → DerivativeRenormalization → GraeffeTransform → CriticalValuePolynomial → ShiftConjugacy → DerivativeRenormalization → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### Markov関手と到達時刻不変量（DoobTransform・TimeReversal・HittingMomentSystem・MomentRecurrence）

- ID: `research.autonomous.markov_dynamics.51907f779e`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `hitting_moment_recurrence`
- 難度仮説: `28`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「有限既約可逆Markov連鎖と指定状態集合を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 正の固有関数によるDoob変換を施す，(2) 定常分布に関する時間反転をとる，(3) 恒等遷移との凸結合でlazy化する，(4) 正の固有関数によるDoob変換を施す，(5) 定常分布に関する時間反転をとる，(6) 恒等遷移との凸結合でlazy化する，(7) 定常分布に関する時間反転をとる，(8) 正の固有関数によるDoob変換を施す，(9) 定常分布に関する時間反転をとる，(10) 自己同型軌道に沿って強 lumping する，(11) 恒等遷移との凸結合でlazy化する，(12) 正の固有関数によるDoob変換を施す，(13) 恒等遷移との凸結合でlazy化する，(14) 自身との同期積連鎖を作る，(15) 自己同型軌道に沿って強 lumping する，(16) 自身との同期積連鎖を作る，(17) 自己同型軌道に沿って強 lumping する，(18) 自身との同期積連鎖を作る，(19) 自己同型軌道に沿って強 lumping する，(20) 自身との同期積連鎖を作る，(21) 指定集合で吸収させ過渡核をとる，(22) 過渡核のGreen作用素をとる，(23) 到達時刻の高次モーメント連立系を作る，(24) モーメント次数方向の漸化式を抽出する。最後に、到達時刻モーメントの漸化式次数が低下する場合を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DoobTransform → TimeReversal → LazyPerturbation → DoobTransform → TimeReversal → LazyPerturbation → TimeReversal → DoobTransform → TimeReversal → StateLumping → LazyPerturbation → DoobTransform → LazyPerturbation → ProductChain → StateLumping → ProductChain → StateLumping → ProductChain → StateLumping → ProductChain → KilledChain → GreenOperator → HittingMomentSystem → MomentRecurrence → MarkovRecurrenceQuery`

### 凸体関手の合成力学（ProjectionBody・SteinerSymmetrization・IntersectionBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.2f5b6097e3`
- 状態: `unresolved_by_mathos`
- 射数: `28`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `31`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 射影体をとる，(2) 主慣性軸方向にSteiner対称化する，(3) 交叉体をとる，(4) 主慣性軸方向にSteiner対称化する，(5) 射影体をとる，(6) 差体をとる，(7) 自身と極体のMinkowski和をとる，(8) 原点に関する極体をとる，(9) 重心体をとる，(10) 射影体をとる，(11) 自身と極体のMinkowski和をとる，(12) 原点に関する極体をとる，(13) 主慣性軸方向にSteiner対称化する，(14) 射影体をとる，(15) 重心体をとる，(16) 交叉体をとる，(17) 主慣性軸方向にSteiner対称化する，(18) 重心体をとる，(19) 自身と極体のMinkowski和をとる，(20) 差体をとる，(21) 原点に関する極体をとる，(22) 差体をとる，(23) 交叉体をとる，(24) 差体をとる，(25) 重心体をとる，(26) 交叉体をとる，(27) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectionBody → SteinerSymmetrization → IntersectionBody → SteinerSymmetrization → ProjectionBody → DifferenceBody → MinkowskiPolarSum → PolarDual → CentroidBody → ProjectionBody → MinkowskiPolarSum → PolarDual → SteinerSymmetrization → ProjectionBody → CentroidBody → IntersectionBody → SteinerSymmetrization → CentroidBody → MinkowskiPolarSum → DifferenceBody → PolarDual → DifferenceBody → IntersectionBody → DifferenceBody → CentroidBody → IntersectionBody → VolumeNormalization → ConvexFixedPointQuery`

### 平面代数曲線の合成変換（PolarReciprocal・IsogonalCremona・Catacaustic・OffsetCurve）

- ID: `research.autonomous.plane_curve.d334869ef3`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `birational_periodicity`
- 難度仮説: `29`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定非退化二次形式に関する極逆像をとる，(2) 固定基準三角形に関する等角共役Cremona像をとる，(3) 射影閉包をとり無限遠点を加える，(4) 基点を避ける一般アフィンチャートへ移す，(5) 固定基準三角形に関する等角共役Cremona像をとる，(6) 定義多項式のHessian曲線をとる，(7) 射影閉包をとり無限遠点を加える，(8) 基点を避ける一般アフィンチャートへ移す，(9) 固定基準三角形に関する等角共役Cremona像をとる，(10) 固定光源からの反射光線族の包絡線をとる，(11) 定義多項式のHessian曲線をとる，(12) 法線方向の代数的平行曲線をとる，(13) 定義多項式のHessian曲線をとる，(14) 固定非退化二次形式に関する極逆像をとる，(15) 固定基準三角形に関する等角共役Cremona像をとる，(16) 正則接線族の射影双対曲線をとる，(17) 定義多項式のHessian曲線をとる，(18) 原点中心の円反転像をとる，(19) 固定非退化二次形式に関する極逆像をとる，(20) 射影閉包をとり無限遠点を加える，(21) 基点を避ける一般アフィンチャートへ移す，(22) 固定非退化二次形式に関する極逆像をとる，(23) 原点中心の円反転像をとる，(24) 固定光源からの反射光線族の包絡線をとる，(25) 法線方向の代数的平行曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `PolarReciprocal → IsogonalCremona → ProjectiveClosure → AffineChartChange → IsogonalCremona → HessianCurve → ProjectiveClosure → AffineChartChange → IsogonalCremona → Catacaustic → HessianCurve → OffsetCurve → HessianCurve → PolarReciprocal → IsogonalCremona → ProjectiveDual → HessianCurve → CircleInversion → PolarReciprocal → ProjectiveClosure → AffineChartChange → PolarReciprocal → CircleInversion → Catacaustic → OffsetCurve → BirationalPeriodQuery`

### 多項式変換と算術観測（CriticalValuePolynomial・RootMultiset・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.619078da82`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `recurrence_order_drop`
- 難度仮説: `29`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 臨界値を根にもつ消去多項式を作る，(2) 重複度付き根配置へ移す，(3) 根配置からモニック多項式を再構成する，(4) 根の重心を0へ移す平行移動共役を施す，(5) 根を二乗するGraeffe変換を施す，(6) 導関数をモニックに再正規化する，(7) 根を二乗するGraeffe変換を施す，(8) 根を逆数へ移す相反多項式をとる，(9) 根を二乗するGraeffe変換を施す，(10) 根を逆数へ移す相反多項式をとる，(11) 根の重心を0へ移す平行移動共役を施す，(12) 根を二乗するGraeffe変換を施す，(13) 臨界値を根にもつ消去多項式を作る，(14) 根の重心を0へ移す平行移動共役を施す，(15) 根を逆数へ移す相反多項式をとる，(16) 重複度付き根配置へ移す，(17) 根配置からモニック多項式を再構成する，(18) 根の重心を0へ移す平行移動共役を施す，(19) 根を逆数へ移す相反多項式をとる，(20) 重複度付き根配置へ移す，(21) 根の冪和モーメント列を作る，(22) モーメントからHankel行列族を作る，(23) 主小行列式列をとる，(24) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → ShiftConjugacy → GraeffeTransform → DerivativeRenormalization → GraeffeTransform → ReciprocalPolynomial → GraeffeTransform → ReciprocalPolynomial → ShiftConjugacy → GraeffeTransform → CriticalValuePolynomial → ShiftConjugacy → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → ShiftConjugacy → ReciprocalPolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 平面代数曲線の合成変換（ProjectiveDual・Catacaustic・ProjectiveDual・PolarReciprocal）

- ID: `research.autonomous.plane_curve.d37a99cfde`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `birational_periodicity`
- 難度仮説: `29`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 正則接線族の射影双対曲線をとる，(2) 固定光源からの反射光線族の包絡線をとる，(3) 正則接線族の射影双対曲線をとる，(4) 射影閉包をとり無限遠点を加える，(5) 基点を避ける一般アフィンチャートへ移す，(6) 固定光源からの反射光線族の包絡線をとる，(7) 法線方向の代数的平行曲線をとる，(8) 固定非退化二次形式に関する極逆像をとる，(9) 固定光源からの反射光線族の包絡線をとる，(10) 射影閉包をとり無限遠点を加える，(11) 基点を避ける一般アフィンチャートへ移す，(12) 射影閉包をとり無限遠点を加える，(13) 基点を避ける一般アフィンチャートへ移す，(14) 原点中心の円反転像をとる，(15) 固定光源からの反射光線族の包絡線をとる，(16) 法線方向の代数的平行曲線をとる，(17) 原点中心の円反転像をとる，(18) 定義多項式のHessian曲線をとる，(19) 正則接線族の射影双対曲線をとる，(20) 射影閉包をとり無限遠点を加える，(21) 基点を避ける一般アフィンチャートへ移す，(22) 固定非退化二次形式に関する極逆像をとる，(23) 原点中心の円反転像をとる，(24) 正則接線族の射影双対曲線をとる，(25) 固定非退化二次形式に関する極逆像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectiveDual → Catacaustic → ProjectiveDual → ProjectiveClosure → AffineChartChange → Catacaustic → OffsetCurve → PolarReciprocal → Catacaustic → ProjectiveClosure → AffineChartChange → ProjectiveClosure → AffineChartChange → CircleInversion → Catacaustic → OffsetCurve → CircleInversion → HessianCurve → ProjectiveDual → ProjectiveClosure → AffineChartChange → PolarReciprocal → CircleInversion → ProjectiveDual → PolarReciprocal → BirationalPeriodQuery`

### 凸体関手の合成力学（ProjectionBody・PolarDual・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.424a10dadc`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `convex_body_dynamics`
- 難度仮説: `29`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 射影体をとる，(2) 原点に関する極体をとる，(3) 交叉体をとる，(4) 射影体をとる，(5) 交叉体をとる，(6) 原点に関する極体をとる，(7) 差体をとる，(8) 原点に関する極体をとる，(9) 差体をとる，(10) 射影体をとる，(11) 原点に関する極体をとる，(12) 主慣性軸方向にSteiner対称化する，(13) 重心体をとる，(14) 主慣性軸方向にSteiner対称化する，(15) 差体をとる，(16) 交叉体をとる，(17) 重心体をとる，(18) 差体をとる，(19) 自身と極体のMinkowski和をとる，(20) 交叉体をとる，(21) 面積と二次モーメントを固定して正規化する，(22) ここまでの凸体関手を反復する，(23) 支持関数の軌道へ移す，(24) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectionBody → PolarDual → IntersectionBody → ProjectionBody → IntersectionBody → PolarDual → DifferenceBody → PolarDual → DifferenceBody → ProjectionBody → PolarDual → SteinerSymmetrization → CentroidBody → SteinerSymmetrization → DifferenceBody → IntersectionBody → CentroidBody → DifferenceBody → MinkowskiPolarSum → IntersectionBody → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 多項式変換と算術観測（RootMultiset・PolynomialReconstruction・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.fa12621a8e`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `recurrence_order_drop`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重複度付き根配置へ移す，(2) 根配置からモニック多項式を再構成する，(3) 導関数をモニックに再正規化する，(4) 根を二乗するGraeffe変換を施す，(5) 根の重心を0へ移す平行移動共役を施す，(6) 根を逆数へ移す相反多項式をとる，(7) 導関数をモニックに再正規化する，(8) 根を逆数へ移す相反多項式をとる，(9) 根を二乗するGraeffe変換を施す，(10) 導関数をモニックに再正規化する，(11) 根の重心を0へ移す平行移動共役を施す，(12) 導関数をモニックに再正規化する，(13) 臨界値を根にもつ消去多項式を作る，(14) 根を逆数へ移す相反多項式をとる，(15) 臨界値を根にもつ消去多項式を作る，(16) 重複度付き根配置へ移す，(17) 根配置からモニック多項式を再構成する，(18) 重複度付き根配置へ移す，(19) 根配置からモニック多項式を再構成する，(20) 根を二乗するGraeffe変換を施す，(21) 重複度付き根配置へ移す，(22) 根の冪和モーメント列を作る，(23) モーメントからHankel行列族を作る，(24) 主小行列式列をとる，(25) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `RootMultiset → PolynomialReconstruction → DerivativeRenormalization → GraeffeTransform → ShiftConjugacy → ReciprocalPolynomial → DerivativeRenormalization → ReciprocalPolynomial → GraeffeTransform → DerivativeRenormalization → ShiftConjugacy → DerivativeRenormalization → CriticalValuePolynomial → ReciprocalPolynomial → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → RootMultiset → PolynomialReconstruction → GraeffeTransform → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 三角形変換の合成力学（CircumcenterMark・PedalProjection・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.ea19790aea`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 外心を標識点として付加する，(2) 標識点から三辺への垂足三点をとる，(3) 三点を頂点とする向き付き三角形を作る，(4) 垂心を標識点として付加する，(5) 標識点を三辺に関して反射した三点をとる，(6) 三点を頂点とする向き付き三角形を作る，(7) 垂足三角形へ移す，(8) 反中点三角形へ移す，(9) 重心を標識点として付加する，(10) 標識点から三辺への垂足三点をとる，(11) 三点を頂点とする向き付き三角形を作る，(12) 類似重心を標識点として付加する，(13) 各頂点と標識点が定める円の対応交点をとる，(14) 三点を頂点とする向き付き三角形を作る，(15) 三辺の中点三角形へ移す，(16) 垂足三角形へ移す，(17) 三辺の中点三角形へ移す，(18) 垂足三角形へ移す，(19) 反中点三角形へ移す，(20) 重心・面積・向きを固定して相似正規化する，(21) 相似類のモジュライ点へ射影する，(22) ここまでの合成が誘導する写像を反復する，(23) 退化三角形を境界として軌道をコンパクト化する，(24) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CircumcenterMark → PedalProjection → TriangleFormation → OrthocenterMark → SideReflectionTrace → TriangleFormation → OrthicTransform → AnticomplementaryTransform → CentroidMark → PedalProjection → TriangleFormation → SymmedianMark → VertexCircleTrace → TriangleFormation → MedialTransform → OrthicTransform → MedialTransform → OrthicTransform → AnticomplementaryTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 三角形変換の合成力学（MedialTransform・OrthocenterMark・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.a3459ac662`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 三辺の中点三角形へ移す，(2) 垂心を標識点として付加する，(3) 標識点から三辺への垂足三点をとる，(4) 三点を頂点とする向き付き三角形を作る，(5) 反中点三角形へ移す，(6) 類似重心を標識点として付加する，(7) 標識点から三辺への垂足三点をとる，(8) 三点を頂点とする向き付き三角形を作る，(9) 三辺の中点三角形へ移す，(10) 重心を標識点として付加する，(11) 各頂点と標識点が定める円の対応交点をとる，(12) 三点を頂点とする向き付き三角形を作る，(13) 垂足三角形へ移す，(14) 外心を標識点として付加する，(15) 標識点から三辺への垂足三点をとる，(16) 三点を頂点とする向き付き三角形を作る，(17) 垂足三角形へ移す，(18) 三辺の中点三角形へ移す，(19) 垂足三角形へ移す，(20) 重心・面積・向きを固定して相似正規化する，(21) 相似類のモジュライ点へ射影する，(22) ここまでの合成が誘導する写像を反復する，(23) 退化三角形を境界として軌道をコンパクト化する，(24) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `MedialTransform → OrthocenterMark → PedalProjection → TriangleFormation → AnticomplementaryTransform → SymmedianMark → PedalProjection → TriangleFormation → MedialTransform → CentroidMark → VertexCircleTrace → TriangleFormation → OrthicTransform → CircumcenterMark → PedalProjection → TriangleFormation → OrthicTransform → MedialTransform → OrthicTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 凸体関手の合成力学（PolarDual・CentroidBody・PolarDual・VolumeNormalization）

- ID: `research.autonomous.convex_body.52c51b310a`
- 状態: `unresolved_by_mathos`
- 射数: `28`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `31`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 原点に関する極体をとる，(2) 重心体をとる，(3) 射影体をとる，(4) 主慣性軸方向にSteiner対称化する，(5) 交叉体をとる，(6) 重心体をとる，(7) 原点に関する極体をとる，(8) 主慣性軸方向にSteiner対称化する，(9) 差体をとる，(10) 交叉体をとる，(11) 差体をとる，(12) 自身と極体のMinkowski和をとる，(13) 主慣性軸方向にSteiner対称化する，(14) 重心体をとる，(15) 交叉体をとる，(16) 射影体をとる，(17) 自身と極体のMinkowski和をとる，(18) 差体をとる，(19) 主慣性軸方向にSteiner対称化する，(20) 交叉体をとる，(21) 原点に関する極体をとる，(22) 自身と極体のMinkowski和をとる，(23) 差体をとる，(24) 重心体をとる，(25) 自身と極体のMinkowski和をとる，(26) 原点に関する極体をとる，(27) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `PolarDual → CentroidBody → ProjectionBody → SteinerSymmetrization → IntersectionBody → CentroidBody → PolarDual → SteinerSymmetrization → DifferenceBody → IntersectionBody → DifferenceBody → MinkowskiPolarSum → SteinerSymmetrization → CentroidBody → IntersectionBody → ProjectionBody → MinkowskiPolarSum → DifferenceBody → SteinerSymmetrization → IntersectionBody → PolarDual → MinkowskiPolarSum → DifferenceBody → CentroidBody → MinkowskiPolarSum → PolarDual → VolumeNormalization → ConvexFixedPointQuery`

### 多項式変換と算術観測（DerivativeRenormalization・CriticalValuePolynomial・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.f7100c6a0c`
- 状態: `unresolved_by_mathos`
- 射数: `27`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `31`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 導関数をモニックに再正規化する，(2) 臨界値を根にもつ消去多項式を作る，(3) 根を逆数へ移す相反多項式をとる，(4) 根を二乗するGraeffe変換を施す，(5) 導関数をモニックに再正規化する，(6) 重複度付き根配置へ移す，(7) 根配置からモニック多項式を再構成する，(8) 重複度付き根配置へ移す，(9) 根配置からモニック多項式を再構成する，(10) 重複度付き根配置へ移す，(11) 根配置からモニック多項式を再構成する，(12) 導関数をモニックに再正規化する，(13) 根を二乗するGraeffe変換を施す，(14) 根の重心を0へ移す平行移動共役を施す，(15) 臨界値を根にもつ消去多項式を作る，(16) 導関数をモニックに再正規化する，(17) 根の重心を0へ移す平行移動共役を施す，(18) 臨界値を根にもつ消去多項式を作る，(19) 根を二乗するGraeffe変換を施す，(20) 臨界値を根にもつ消去多項式を作る，(21) 重複度付き根配置へ移す，(22) 根の冪和モーメント列を作る，(23) モーメントからHankel行列族を作る，(24) 主小行列式列をとる，(25) 満たす最小線形漸化式を抽出する，(26) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DerivativeRenormalization → CriticalValuePolynomial → ReciprocalPolynomial → GraeffeTransform → DerivativeRenormalization → RootMultiset → PolynomialReconstruction → RootMultiset → PolynomialReconstruction → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → GraeffeTransform → ShiftConjugacy → CriticalValuePolynomial → DerivativeRenormalization → ShiftConjugacy → CriticalValuePolynomial → GraeffeTransform → CriticalValuePolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 平面代数曲線の合成変換（ProjectiveClosure・AffineChartChange・Catacaustic・Evolute）

- ID: `research.autonomous.plane_curve.ce33edd999`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `birational_periodicity`
- 難度仮説: `29`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 射影閉包をとり無限遠点を加える，(2) 基点を避ける一般アフィンチャートへ移す，(3) 正則接線族の射影双対曲線をとる，(4) 法線族の包絡線である発展曲線をとる，(5) 原点中心の円反転像をとる，(6) 正則接線族の射影双対曲線をとる，(7) 固定非退化二次形式に関する極逆像をとる，(8) 定義多項式のHessian曲線をとる，(9) 固定基準三角形に関する等角共役Cremona像をとる，(10) 定義多項式のHessian曲線をとる，(11) 固定非退化二次形式に関する極逆像をとる，(12) 正則接線族の射影双対曲線をとる，(13) 法線族の包絡線である発展曲線をとる，(14) 固定光源からの反射光線族の包絡線をとる，(15) 法線族の包絡線である発展曲線をとる，(16) 法線方向の代数的平行曲線をとる，(17) 原点中心の円反転像をとる，(18) 法線方向の代数的平行曲線をとる，(19) 固定非退化二次形式に関する極逆像をとる，(20) 原点中心の円反転像をとる，(21) 射影閉包をとり無限遠点を加える，(22) 基点を避ける一般アフィンチャートへ移す，(23) 定義多項式のHessian曲線をとる，(24) 固定光源からの反射光線族の包絡線をとる，(25) 法線族の包絡線である発展曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectiveClosure → AffineChartChange → ProjectiveDual → Evolute → CircleInversion → ProjectiveDual → PolarReciprocal → HessianCurve → IsogonalCremona → HessianCurve → PolarReciprocal → ProjectiveDual → Evolute → Catacaustic → Evolute → OffsetCurve → CircleInversion → OffsetCurve → PolarReciprocal → CircleInversion → ProjectiveClosure → AffineChartChange → HessianCurve → Catacaustic → Evolute → BirationalPeriodQuery`

### 多項式変換と算術観測（ReciprocalPolynomial・ShiftConjugacy・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.bdfb2f3a22`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `recurrence_order_drop`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を逆数へ移す相反多項式をとる，(2) 根の重心を0へ移す平行移動共役を施す，(3) 重複度付き根配置へ移す，(4) 根配置からモニック多項式を再構成する，(5) 根の重心を0へ移す平行移動共役を施す，(6) 根を二乗するGraeffe変換を施す，(7) 重複度付き根配置へ移す，(8) 根配置からモニック多項式を再構成する，(9) 臨界値を根にもつ消去多項式を作る，(10) 導関数をモニックに再正規化する，(11) 臨界値を根にもつ消去多項式を作る，(12) 重複度付き根配置へ移す，(13) 根配置からモニック多項式を再構成する，(14) 臨界値を根にもつ消去多項式を作る，(15) 根を逆数へ移す相反多項式をとる，(16) 臨界値を根にもつ消去多項式を作る，(17) 導関数をモニックに再正規化する，(18) 根の重心を0へ移す平行移動共役を施す，(19) 導関数をモニックに再正規化する，(20) 根の重心を0へ移す平行移動共役を施す，(21) 重複度付き根配置へ移す，(22) 根の冪和モーメント列を作る，(23) モーメントからHankel行列族を作る，(24) 主小行列式列をとる，(25) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ReciprocalPolynomial → ShiftConjugacy → RootMultiset → PolynomialReconstruction → ShiftConjugacy → GraeffeTransform → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → DerivativeRenormalization → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → ReciprocalPolynomial → CriticalValuePolynomial → DerivativeRenormalization → ShiftConjugacy → DerivativeRenormalization → ShiftConjugacy → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 凸体関手の合成力学（SteinerSymmetrization・MinkowskiPolarSum・IntersectionBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.71a7227d07`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `28`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 主慣性軸方向にSteiner対称化する，(2) 自身と極体のMinkowski和をとる，(3) 射影体をとる，(4) 重心体をとる，(5) 射影体をとる，(6) 原点に関する極体をとる，(7) 主慣性軸方向にSteiner対称化する，(8) 自身と極体のMinkowski和をとる，(9) 交叉体をとる，(10) 重心体をとる，(11) 差体をとる，(12) 射影体をとる，(13) 自身と極体のMinkowski和をとる，(14) 射影体をとる，(15) 重心体をとる，(16) 自身と極体のMinkowski和をとる，(17) 交叉体をとる，(18) 主慣性軸方向にSteiner対称化する，(19) 交叉体をとる，(20) 重心体をとる，(21) 差体をとる，(22) 原点に関する極体をとる，(23) 交叉体をとる，(24) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `SteinerSymmetrization → MinkowskiPolarSum → ProjectionBody → CentroidBody → ProjectionBody → PolarDual → SteinerSymmetrization → MinkowskiPolarSum → IntersectionBody → CentroidBody → DifferenceBody → ProjectionBody → MinkowskiPolarSum → ProjectionBody → CentroidBody → MinkowskiPolarSum → IntersectionBody → SteinerSymmetrization → IntersectionBody → CentroidBody → DifferenceBody → PolarDual → IntersectionBody → VolumeNormalization → ConvexFixedPointQuery`

### 平面代数曲線の合成変換（ProjectiveClosure・AffineChartChange・ProjectiveDual・HessianCurve）

- ID: `research.autonomous.plane_curve.f67e436ca5`
- 状態: `unresolved_by_mathos`
- 射数: `27`
- 問い: `birational_periodicity`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 射影閉包をとり無限遠点を加える，(2) 基点を避ける一般アフィンチャートへ移す，(3) 原点中心の円反転像をとる，(4) 定義多項式のHessian曲線をとる，(5) 固定光源からの反射光線族の包絡線をとる，(6) 定義多項式のHessian曲線をとる，(7) 原点中心の円反転像をとる，(8) 法線族の包絡線である発展曲線をとる，(9) 射影閉包をとり無限遠点を加える，(10) 基点を避ける一般アフィンチャートへ移す，(11) 射影閉包をとり無限遠点を加える，(12) 基点を避ける一般アフィンチャートへ移す，(13) 定義多項式のHessian曲線をとる，(14) 法線方向の代数的平行曲線をとる，(15) 固定非退化二次形式に関する極逆像をとる，(16) 原点中心の円反転像をとる，(17) 固定基準三角形に関する等角共役Cremona像をとる，(18) 正則接線族の射影双対曲線をとる，(19) 法線方向の代数的平行曲線をとる，(20) 固定非退化二次形式に関する極逆像をとる，(21) 固定光源からの反射光線族の包絡線をとる，(22) 正則接線族の射影双対曲線をとる，(23) 原点中心の円反転像をとる，(24) 固定基準三角形に関する等角共役Cremona像をとる，(25) 正則接線族の射影双対曲線をとる，(26) 定義多項式のHessian曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectiveClosure → AffineChartChange → CircleInversion → HessianCurve → Catacaustic → HessianCurve → CircleInversion → Evolute → ProjectiveClosure → AffineChartChange → ProjectiveClosure → AffineChartChange → HessianCurve → OffsetCurve → PolarReciprocal → CircleInversion → IsogonalCremona → ProjectiveDual → OffsetCurve → PolarReciprocal → Catacaustic → ProjectiveDual → CircleInversion → IsogonalCremona → ProjectiveDual → HessianCurve → BirationalPeriodQuery`

### 多項式変換と算術観測（RootMultiset・PolynomialReconstruction・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.47c0a78bed`
- 状態: `unresolved_by_mathos`
- 射数: `25`
- 問い: `recurrence_order_drop`
- 難度仮説: `29`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重複度付き根配置へ移す，(2) 根配置からモニック多項式を再構成する，(3) 臨界値を根にもつ消去多項式を作る，(4) 根を逆数へ移す相反多項式をとる，(5) 根の重心を0へ移す平行移動共役を施す，(6) 根を逆数へ移す相反多項式をとる，(7) 根を二乗するGraeffe変換を施す，(8) 根を逆数へ移す相反多項式をとる，(9) 根を二乗するGraeffe変換を施す，(10) 導関数をモニックに再正規化する，(11) 根を二乗するGraeffe変換を施す，(12) 根を逆数へ移す相反多項式をとる，(13) 臨界値を根にもつ消去多項式を作る，(14) 重複度付き根配置へ移す，(15) 根配置からモニック多項式を再構成する，(16) 導関数をモニックに再正規化する，(17) 根を二乗するGraeffe変換を施す，(18) 重複度付き根配置へ移す，(19) 根配置からモニック多項式を再構成する，(20) 重複度付き根配置へ移す，(21) 根の冪和モーメント列を作る，(22) モーメントからHankel行列族を作る，(23) 主小行列式列をとる，(24) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → ReciprocalPolynomial → ShiftConjugacy → ReciprocalPolynomial → GraeffeTransform → ReciprocalPolynomial → GraeffeTransform → DerivativeRenormalization → GraeffeTransform → ReciprocalPolynomial → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → GraeffeTransform → RootMultiset → PolynomialReconstruction → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 凸体関手の合成力学（ProjectionBody・PolarDual・MinkowskiPolarSum・VolumeNormalization）

- ID: `research.autonomous.convex_body.841431c574`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `29`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 射影体をとる，(2) 原点に関する極体をとる，(3) 差体をとる，(4) 原点に関する極体をとる，(5) 重心体をとる，(6) 射影体をとる，(7) 自身と極体のMinkowski和をとる，(8) 交叉体をとる，(9) 重心体をとる，(10) 差体をとる，(11) 原点に関する極体をとる，(12) 交叉体をとる，(13) 射影体をとる，(14) 重心体をとる，(15) 射影体をとる，(16) 重心体をとる，(17) 交叉体をとる，(18) 自身と極体のMinkowski和をとる，(19) 差体をとる，(20) 自身と極体のMinkowski和をとる，(21) 主慣性軸方向にSteiner対称化する，(22) 差体をとる，(23) 原点に関する極体をとる，(24) 自身と極体のMinkowski和をとる，(25) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectionBody → PolarDual → DifferenceBody → PolarDual → CentroidBody → ProjectionBody → MinkowskiPolarSum → IntersectionBody → CentroidBody → DifferenceBody → PolarDual → IntersectionBody → ProjectionBody → CentroidBody → ProjectionBody → CentroidBody → IntersectionBody → MinkowskiPolarSum → DifferenceBody → MinkowskiPolarSum → SteinerSymmetrization → DifferenceBody → PolarDual → MinkowskiPolarSum → VolumeNormalization → ConvexFixedPointQuery`

### 平面代数曲線の合成変換（Evolute・OffsetCurve・ProjectiveClosure・AffineChartChange）

- ID: `research.autonomous.plane_curve.f8bd11d9a4`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `birational_periodicity`
- 難度仮説: `29`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 法線族の包絡線である発展曲線をとる，(2) 法線方向の代数的平行曲線をとる，(3) 定義多項式のHessian曲線をとる，(4) 固定基準三角形に関する等角共役Cremona像をとる，(5) 固定光源からの反射光線族の包絡線をとる，(6) 法線族の包絡線である発展曲線をとる，(7) 固定非退化二次形式に関する極逆像をとる，(8) 固定光源からの反射光線族の包絡線をとる，(9) 射影閉包をとり無限遠点を加える，(10) 基点を避ける一般アフィンチャートへ移す，(11) 法線方向の代数的平行曲線をとる，(12) 法線族の包絡線である発展曲線をとる，(13) 射影閉包をとり無限遠点を加える，(14) 基点を避ける一般アフィンチャートへ移す，(15) 固定光源からの反射光線族の包絡線をとる，(16) 正則接線族の射影双対曲線をとる，(17) 固定光源からの反射光線族の包絡線をとる，(18) 射影閉包をとり無限遠点を加える，(19) 基点を避ける一般アフィンチャートへ移す，(20) 固定非退化二次形式に関する極逆像をとる，(21) 法線族の包絡線である発展曲線をとる，(22) 固定基準三角形に関する等角共役Cremona像をとる，(23) 正則接線族の射影双対曲線をとる，(24) 射影閉包をとり無限遠点を加える，(25) 基点を避ける一般アフィンチャートへ移す。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `Evolute → OffsetCurve → HessianCurve → IsogonalCremona → Catacaustic → Evolute → PolarReciprocal → Catacaustic → ProjectiveClosure → AffineChartChange → OffsetCurve → Evolute → ProjectiveClosure → AffineChartChange → Catacaustic → ProjectiveDual → Catacaustic → ProjectiveClosure → AffineChartChange → PolarReciprocal → Evolute → IsogonalCremona → ProjectiveDual → ProjectiveClosure → AffineChartChange → BirationalPeriodQuery`

### 多項式変換と算術観測（CriticalValuePolynomial・ReciprocalPolynomial・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.9187f77d13`
- 状態: `unresolved_by_mathos`
- 射数: `28`
- 問い: `recurrence_order_drop`
- 難度仮説: `32`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 臨界値を根にもつ消去多項式を作る，(2) 根を逆数へ移す相反多項式をとる，(3) 導関数をモニックに再正規化する，(4) 重複度付き根配置へ移す，(5) 根配置からモニック多項式を再構成する，(6) 導関数をモニックに再正規化する，(7) 重複度付き根配置へ移す，(8) 根配置からモニック多項式を再構成する，(9) 根を二乗するGraeffe変換を施す，(10) 根を逆数へ移す相反多項式をとる，(11) 根を二乗するGraeffe変換を施す，(12) 臨界値を根にもつ消去多項式を作る，(13) 導関数をモニックに再正規化する，(14) 根の重心を0へ移す平行移動共役を施す，(15) 根を逆数へ移す相反多項式をとる，(16) 臨界値を根にもつ消去多項式を作る，(17) 根の重心を0へ移す平行移動共役を施す，(18) 根を二乗するGraeffe変換を施す，(19) 根を逆数へ移す相反多項式をとる，(20) 根の重心を0へ移す平行移動共役を施す，(21) 重複度付き根配置へ移す，(22) 根配置からモニック多項式を再構成する，(23) 重複度付き根配置へ移す，(24) 根の冪和モーメント列を作る，(25) モーメントからHankel行列族を作る，(26) 主小行列式列をとる，(27) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CriticalValuePolynomial → ReciprocalPolynomial → DerivativeRenormalization → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → RootMultiset → PolynomialReconstruction → GraeffeTransform → ReciprocalPolynomial → GraeffeTransform → CriticalValuePolynomial → DerivativeRenormalization → ShiftConjugacy → ReciprocalPolynomial → CriticalValuePolynomial → ShiftConjugacy → GraeffeTransform → ReciprocalPolynomial → ShiftConjugacy → RootMultiset → PolynomialReconstruction → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 凸体関手の合成力学（CentroidBody・PolarDual・ProjectionBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.8823052495`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `29`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重心体をとる，(2) 原点に関する極体をとる，(3) 主慣性軸方向にSteiner対称化する，(4) 自身と極体のMinkowski和をとる，(5) 射影体をとる，(6) 交叉体をとる，(7) 射影体をとる，(8) 主慣性軸方向にSteiner対称化する，(9) 交叉体をとる，(10) 主慣性軸方向にSteiner対称化する，(11) 重心体をとる，(12) 交叉体をとる，(13) 主慣性軸方向にSteiner対称化する，(14) 差体をとる，(15) 重心体をとる，(16) 差体をとる，(17) 交叉体をとる，(18) 差体をとる，(19) 原点に関する極体をとる，(20) 射影体をとる，(21) 差体をとる，(22) 重心体をとる，(23) 自身と極体のMinkowski和をとる，(24) 射影体をとる，(25) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CentroidBody → PolarDual → SteinerSymmetrization → MinkowskiPolarSum → ProjectionBody → IntersectionBody → ProjectionBody → SteinerSymmetrization → IntersectionBody → SteinerSymmetrization → CentroidBody → IntersectionBody → SteinerSymmetrization → DifferenceBody → CentroidBody → DifferenceBody → IntersectionBody → DifferenceBody → PolarDual → ProjectionBody → DifferenceBody → CentroidBody → MinkowskiPolarSum → ProjectionBody → VolumeNormalization → ConvexFixedPointQuery`

### 平面代数曲線の合成変換（CircleInversion・ProjectiveDual・ProjectiveDual・Catacaustic）

- ID: `research.autonomous.plane_curve.82361f9d2e`
- 状態: `unresolved_by_mathos`
- 射数: `27`
- 問い: `birational_periodicity`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 原点中心の円反転像をとる，(2) 正則接線族の射影双対曲線をとる，(3) 法線方向の代数的平行曲線をとる，(4) 原点中心の円反転像をとる，(5) 法線方向の代数的平行曲線をとる，(6) 法線族の包絡線である発展曲線をとる，(7) 正則接線族の射影双対曲線をとる，(8) 定義多項式のHessian曲線をとる，(9) 固定非退化二次形式に関する極逆像をとる，(10) 原点中心の円反転像をとる，(11) 固定基準三角形に関する等角共役Cremona像をとる，(12) 原点中心の円反転像をとる，(13) 定義多項式のHessian曲線をとる，(14) 射影閉包をとり無限遠点を加える，(15) 基点を避ける一般アフィンチャートへ移す，(16) 射影閉包をとり無限遠点を加える，(17) 基点を避ける一般アフィンチャートへ移す，(18) 固定非退化二次形式に関する極逆像をとる，(19) 法線族の包絡線である発展曲線をとる，(20) 射影閉包をとり無限遠点を加える，(21) 基点を避ける一般アフィンチャートへ移す，(22) 射影閉包をとり無限遠点を加える，(23) 基点を避ける一般アフィンチャートへ移す，(24) 法線族の包絡線である発展曲線をとる，(25) 正則接線族の射影双対曲線をとる，(26) 固定光源からの反射光線族の包絡線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CircleInversion → ProjectiveDual → OffsetCurve → CircleInversion → OffsetCurve → Evolute → ProjectiveDual → HessianCurve → PolarReciprocal → CircleInversion → IsogonalCremona → CircleInversion → HessianCurve → ProjectiveClosure → AffineChartChange → ProjectiveClosure → AffineChartChange → PolarReciprocal → Evolute → ProjectiveClosure → AffineChartChange → ProjectiveClosure → AffineChartChange → Evolute → ProjectiveDual → Catacaustic → BirationalPeriodQuery`

### 平面代数曲線の合成変換（ProjectiveDual・ProjectiveClosure・Evolute・HessianCurve）

- ID: `research.autonomous.plane_curve.d1afb524fa`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `birational_periodicity`
- 難度仮説: `29`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 正則接線族の射影双対曲線をとる，(2) 射影閉包をとり無限遠点を加える，(3) 基点を避ける一般アフィンチャートへ移す，(4) 原点中心の円反転像をとる，(5) 固定光源からの反射光線族の包絡線をとる，(6) 原点中心の円反転像をとる，(7) 正則接線族の射影双対曲線をとる，(8) 定義多項式のHessian曲線をとる，(9) 正則接線族の射影双対曲線をとる，(10) 固定非退化二次形式に関する極逆像をとる，(11) 原点中心の円反転像をとる，(12) 固定基準三角形に関する等角共役Cremona像をとる，(13) 射影閉包をとり無限遠点を加える，(14) 基点を避ける一般アフィンチャートへ移す，(15) 固定光源からの反射光線族の包絡線をとる，(16) 原点中心の円反転像をとる，(17) 法線族の包絡線である発展曲線をとる，(18) 射影閉包をとり無限遠点を加える，(19) 基点を避ける一般アフィンチャートへ移す，(20) 定義多項式のHessian曲線をとる，(21) 固定光源からの反射光線族の包絡線をとる，(22) 定義多項式のHessian曲線をとる，(23) 正則接線族の射影双対曲線をとる，(24) 法線族の包絡線である発展曲線をとる，(25) 定義多項式のHessian曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectiveDual → ProjectiveClosure → AffineChartChange → CircleInversion → Catacaustic → CircleInversion → ProjectiveDual → HessianCurve → ProjectiveDual → PolarReciprocal → CircleInversion → IsogonalCremona → ProjectiveClosure → AffineChartChange → Catacaustic → CircleInversion → Evolute → ProjectiveClosure → AffineChartChange → HessianCurve → Catacaustic → HessianCurve → ProjectiveDual → Evolute → HessianCurve → BirationalPeriodQuery`

### 凸体関手の合成力学（MinkowskiPolarSum・PolarDual・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.ec3fef993a`
- 状態: `unresolved_by_mathos`
- 射数: `29`
- 問い: `convex_body_dynamics`
- 難度仮説: `33`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身と極体のMinkowski和をとる，(2) 原点に関する極体をとる，(3) 自身と極体のMinkowski和をとる，(4) 重心体をとる，(5) 自身と極体のMinkowski和をとる，(6) 原点に関する極体をとる，(7) 自身と極体のMinkowski和をとる，(8) 重心体をとる，(9) 差体をとる，(10) 重心体をとる，(11) 原点に関する極体をとる，(12) 主慣性軸方向にSteiner対称化する，(13) 差体をとる，(14) 原点に関する極体をとる，(15) 主慣性軸方向にSteiner対称化する，(16) 交叉体をとる，(17) 差体をとる，(18) 重心体をとる，(19) 差体をとる，(20) 射影体をとる，(21) 交叉体をとる，(22) 射影体をとる，(23) 交叉体をとる，(24) 射影体をとる，(25) 面積と二次モーメントを固定して正規化する，(26) ここまでの凸体関手を反復する，(27) 支持関数の軌道へ移す，(28) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `MinkowskiPolarSum → PolarDual → MinkowskiPolarSum → CentroidBody → MinkowskiPolarSum → PolarDual → MinkowskiPolarSum → CentroidBody → DifferenceBody → CentroidBody → PolarDual → SteinerSymmetrization → DifferenceBody → PolarDual → SteinerSymmetrization → IntersectionBody → DifferenceBody → CentroidBody → DifferenceBody → ProjectionBody → IntersectionBody → ProjectionBody → IntersectionBody → ProjectionBody → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 多項式変換と算術観測（CriticalValuePolynomial・GraeffeTransform・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.ebf72044f2`
- 状態: `unresolved_by_mathos`
- 射数: `28`
- 問い: `recurrence_order_drop`
- 難度仮説: `32`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 臨界値を根にもつ消去多項式を作る，(2) 根を二乗するGraeffe変換を施す，(3) 重複度付き根配置へ移す，(4) 根配置からモニック多項式を再構成する，(5) 重複度付き根配置へ移す，(6) 根配置からモニック多項式を再構成する，(7) 臨界値を根にもつ消去多項式を作る，(8) 根を二乗するGraeffe変換を施す，(9) 臨界値を根にもつ消去多項式を作る，(10) 導関数をモニックに再正規化する，(11) 臨界値を根にもつ消去多項式を作る，(12) 根を逆数へ移す相反多項式をとる，(13) 導関数をモニックに再正規化する，(14) 根の重心を0へ移す平行移動共役を施す，(15) 導関数をモニックに再正規化する，(16) 根を逆数へ移す相反多項式をとる，(17) 導関数をモニックに再正規化する，(18) 根を二乗するGraeffe変換を施す，(19) 根を逆数へ移す相反多項式をとる，(20) 根を二乗するGraeffe変換を施す，(21) 重複度付き根配置へ移す，(22) 根配置からモニック多項式を再構成する，(23) 重複度付き根配置へ移す，(24) 根の冪和モーメント列を作る，(25) モーメントからHankel行列族を作る，(26) 主小行列式列をとる，(27) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CriticalValuePolynomial → GraeffeTransform → RootMultiset → PolynomialReconstruction → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → GraeffeTransform → CriticalValuePolynomial → DerivativeRenormalization → CriticalValuePolynomial → ReciprocalPolynomial → DerivativeRenormalization → ShiftConjugacy → DerivativeRenormalization → ReciprocalPolynomial → DerivativeRenormalization → GraeffeTransform → ReciprocalPolynomial → GraeffeTransform → RootMultiset → PolynomialReconstruction → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 凸体関手の合成力学（CentroidBody・ProjectionBody・IntersectionBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.41bb22881b`
- 状態: `unresolved_by_mathos`
- 射数: `27`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重心体をとる，(2) 射影体をとる，(3) 自身と極体のMinkowski和をとる，(4) 主慣性軸方向にSteiner対称化する，(5) 射影体をとる，(6) 重心体をとる，(7) 差体をとる，(8) 重心体をとる，(9) 射影体をとる，(10) 原点に関する極体をとる，(11) 射影体をとる，(12) 重心体をとる，(13) 自身と極体のMinkowski和をとる，(14) 差体をとる，(15) 自身と極体のMinkowski和をとる，(16) 差体をとる，(17) 自身と極体のMinkowski和をとる，(18) 差体をとる，(19) 交叉体をとる，(20) 原点に関する極体をとる，(21) 交叉体をとる，(22) 主慣性軸方向にSteiner対称化する，(23) 交叉体をとる，(24) 原点に関する極体をとる，(25) 交叉体をとる，(26) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CentroidBody → ProjectionBody → MinkowskiPolarSum → SteinerSymmetrization → ProjectionBody → CentroidBody → DifferenceBody → CentroidBody → ProjectionBody → PolarDual → ProjectionBody → CentroidBody → MinkowskiPolarSum → DifferenceBody → MinkowskiPolarSum → DifferenceBody → MinkowskiPolarSum → DifferenceBody → IntersectionBody → PolarDual → IntersectionBody → SteinerSymmetrization → IntersectionBody → PolarDual → IntersectionBody → VolumeNormalization → ConvexFixedPointQuery`

### 平面代数曲線の合成変換（ProjectiveDual・HessianCurve・CircleInversion・HessianCurve）

- ID: `research.autonomous.plane_curve.a94d73ad64`
- 状態: `unresolved_by_mathos`
- 射数: `29`
- 問い: `birational_periodicity`
- 難度仮説: `32`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 正則接線族の射影双対曲線をとる，(2) 定義多項式のHessian曲線をとる，(3) 固定非退化二次形式に関する極逆像をとる，(4) 法線族の包絡線である発展曲線をとる，(5) 原点中心の円反転像をとる，(6) 固定非退化二次形式に関する極逆像をとる，(7) 正則接線族の射影双対曲線をとる，(8) 定義多項式のHessian曲線をとる，(9) 正則接線族の射影双対曲線をとる，(10) 法線族の包絡線である発展曲線をとる，(11) 射影閉包をとり無限遠点を加える，(12) 基点を避ける一般アフィンチャートへ移す，(13) 法線方向の代数的平行曲線をとる，(14) 射影閉包をとり無限遠点を加える，(15) 基点を避ける一般アフィンチャートへ移す，(16) 法線族の包絡線である発展曲線をとる，(17) 射影閉包をとり無限遠点を加える，(18) 基点を避ける一般アフィンチャートへ移す，(19) 固定基準三角形に関する等角共役Cremona像をとる，(20) 固定光源からの反射光線族の包絡線をとる，(21) 法線方向の代数的平行曲線をとる，(22) 固定光源からの反射光線族の包絡線をとる，(23) 法線方向の代数的平行曲線をとる，(24) 正則接線族の射影双対曲線をとる，(25) 固定基準三角形に関する等角共役Cremona像をとる，(26) 定義多項式のHessian曲線をとる，(27) 原点中心の円反転像をとる，(28) 定義多項式のHessian曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectiveDual → HessianCurve → PolarReciprocal → Evolute → CircleInversion → PolarReciprocal → ProjectiveDual → HessianCurve → ProjectiveDual → Evolute → ProjectiveClosure → AffineChartChange → OffsetCurve → ProjectiveClosure → AffineChartChange → Evolute → ProjectiveClosure → AffineChartChange → IsogonalCremona → Catacaustic → OffsetCurve → Catacaustic → OffsetCurve → ProjectiveDual → IsogonalCremona → HessianCurve → CircleInversion → HessianCurve → BirationalPeriodQuery`

### 多項式変換と算術観測（ShiftConjugacy・GraeffeTransform・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.23799c51ad`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根の重心を0へ移す平行移動共役を施す，(2) 根を二乗するGraeffe変換を施す，(3) 根の重心を0へ移す平行移動共役を施す，(4) 根を二乗するGraeffe変換を施す，(5) 根を逆数へ移す相反多項式をとる，(6) 導関数をモニックに再正規化する，(7) 根を二乗するGraeffe変換を施す，(8) 重複度付き根配置へ移す，(9) 根配置からモニック多項式を再構成する，(10) 重複度付き根配置へ移す，(11) 根配置からモニック多項式を再構成する，(12) 根を逆数へ移す相反多項式をとる，(13) 重複度付き根配置へ移す，(14) 根配置からモニック多項式を再構成する，(15) 根を二乗するGraeffe変換を施す，(16) 臨界値を根にもつ消去多項式を作る，(17) 根の重心を0へ移す平行移動共役を施す，(18) 導関数をモニックに再正規化する，(19) 根の重心を0へ移す平行移動共役を施す，(20) 重複度付き根配置へ移す，(21) 根の冪和モーメント列を作る，(22) モーメントからHankel行列族を作る，(23) 主小行列式列をとる，(24) 満たす最小線形漸化式を抽出する，(25) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ShiftConjugacy → GraeffeTransform → ShiftConjugacy → GraeffeTransform → ReciprocalPolynomial → DerivativeRenormalization → GraeffeTransform → RootMultiset → PolynomialReconstruction → RootMultiset → PolynomialReconstruction → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → GraeffeTransform → CriticalValuePolynomial → ShiftConjugacy → DerivativeRenormalization → ShiftConjugacy → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 凸体関手の合成力学（SteinerSymmetrization・ProjectionBody・MinkowskiPolarSum・VolumeNormalization）

- ID: `research.autonomous.convex_body.d2093ebc77`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `29`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 主慣性軸方向にSteiner対称化する，(2) 射影体をとる，(3) 交叉体をとる，(4) 射影体をとる，(5) 交叉体をとる，(6) 原点に関する極体をとる，(7) 主慣性軸方向にSteiner対称化する，(8) 交叉体をとる，(9) 差体をとる，(10) 交叉体をとる，(11) 主慣性軸方向にSteiner対称化する，(12) 原点に関する極体をとる，(13) 射影体をとる，(14) 原点に関する極体をとる，(15) 重心体をとる，(16) 主慣性軸方向にSteiner対称化する，(17) 射影体をとる，(18) 重心体をとる，(19) 原点に関する極体をとる，(20) 重心体をとる，(21) 自身と極体のMinkowski和をとる，(22) 重心体をとる，(23) 差体をとる，(24) 自身と極体のMinkowski和をとる，(25) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `SteinerSymmetrization → ProjectionBody → IntersectionBody → ProjectionBody → IntersectionBody → PolarDual → SteinerSymmetrization → IntersectionBody → DifferenceBody → IntersectionBody → SteinerSymmetrization → PolarDual → ProjectionBody → PolarDual → CentroidBody → SteinerSymmetrization → ProjectionBody → CentroidBody → PolarDual → CentroidBody → MinkowskiPolarSum → CentroidBody → DifferenceBody → MinkowskiPolarSum → VolumeNormalization → ConvexFixedPointQuery`

### 平面代数曲線の合成変換（IsogonalCremona・Catacaustic・ProjectiveClosure・AffineChartChange）

- ID: `research.autonomous.plane_curve.1521951f19`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `birational_periodicity`
- 難度仮説: `29`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定基準三角形に関する等角共役Cremona像をとる，(2) 固定光源からの反射光線族の包絡線をとる，(3) 原点中心の円反転像をとる，(4) 固定光源からの反射光線族の包絡線をとる，(5) 定義多項式のHessian曲線をとる，(6) 射影閉包をとり無限遠点を加える，(7) 基点を避ける一般アフィンチャートへ移す，(8) 原点中心の円反転像をとる，(9) 固定基準三角形に関する等角共役Cremona像をとる，(10) 固定光源からの反射光線族の包絡線をとる，(11) 固定基準三角形に関する等角共役Cremona像をとる，(12) 固定非退化二次形式に関する極逆像をとる，(13) 法線族の包絡線である発展曲線をとる，(14) 固定光源からの反射光線族の包絡線をとる，(15) 原点中心の円反転像をとる，(16) 固定非退化二次形式に関する極逆像をとる，(17) 正則接線族の射影双対曲線をとる，(18) 法線族の包絡線である発展曲線をとる，(19) 射影閉包をとり無限遠点を加える，(20) 基点を避ける一般アフィンチャートへ移す，(21) 原点中心の円反転像をとる，(22) 定義多項式のHessian曲線をとる，(23) 法線族の包絡線である発展曲線をとる，(24) 射影閉包をとり無限遠点を加える，(25) 基点を避ける一般アフィンチャートへ移す。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IsogonalCremona → Catacaustic → CircleInversion → Catacaustic → HessianCurve → ProjectiveClosure → AffineChartChange → CircleInversion → IsogonalCremona → Catacaustic → IsogonalCremona → PolarReciprocal → Evolute → Catacaustic → CircleInversion → PolarReciprocal → ProjectiveDual → Evolute → ProjectiveClosure → AffineChartChange → CircleInversion → HessianCurve → Evolute → ProjectiveClosure → AffineChartChange → BirationalPeriodQuery`

### 多項式変換と算術観測（GraeffeTransform・ReciprocalPolynomial・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.7631b03335`
- 状態: `unresolved_by_mathos`
- 射数: `27`
- 問い: `recurrence_order_drop`
- 難度仮説: `31`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を二乗するGraeffe変換を施す，(2) 根を逆数へ移す相反多項式をとる，(3) 根の重心を0へ移す平行移動共役を施す，(4) 臨界値を根にもつ消去多項式を作る，(5) 根を二乗するGraeffe変換を施す，(6) 根を逆数へ移す相反多項式をとる，(7) 重複度付き根配置へ移す，(8) 根配置からモニック多項式を再構成する，(9) 導関数をモニックに再正規化する，(10) 根を逆数へ移す相反多項式をとる，(11) 臨界値を根にもつ消去多項式を作る，(12) 導関数をモニックに再正規化する，(13) 根を逆数へ移す相反多項式をとる，(14) 根の重心を0へ移す平行移動共役を施す，(15) 重複度付き根配置へ移す，(16) 根配置からモニック多項式を再構成する，(17) 根を二乗するGraeffe変換を施す，(18) 根の重心を0へ移す平行移動共役を施す，(19) 重複度付き根配置へ移す，(20) 根配置からモニック多項式を再構成する，(21) 臨界値を根にもつ消去多項式を作る，(22) 重複度付き根配置へ移す，(23) 根の冪和モーメント列を作る，(24) モーメントからHankel行列族を作る，(25) 主小行列式列をとる，(26) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `GraeffeTransform → ReciprocalPolynomial → ShiftConjugacy → CriticalValuePolynomial → GraeffeTransform → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → ReciprocalPolynomial → CriticalValuePolynomial → DerivativeRenormalization → ReciprocalPolynomial → ShiftConjugacy → RootMultiset → PolynomialReconstruction → GraeffeTransform → ShiftConjugacy → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 凸体関手の合成力学（SteinerSymmetrization・IntersectionBody・MinkowskiPolarSum・VolumeNormalization）

- ID: `research.autonomous.convex_body.1ba16017cc`
- 状態: `unresolved_by_mathos`
- 射数: `28`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `31`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 主慣性軸方向にSteiner対称化する，(2) 交叉体をとる，(3) 原点に関する極体をとる，(4) 差体をとる，(5) 原点に関する極体をとる，(6) 交叉体をとる，(7) 射影体をとる，(8) 原点に関する極体をとる，(9) 交叉体をとる，(10) 重心体をとる，(11) 差体をとる，(12) 重心体をとる，(13) 射影体をとる，(14) 原点に関する極体をとる，(15) 交叉体をとる，(16) 差体をとる，(17) 主慣性軸方向にSteiner対称化する，(18) 重心体をとる，(19) 射影体をとる，(20) 差体をとる，(21) 主慣性軸方向にSteiner対称化する，(22) 射影体をとる，(23) 重心体をとる，(24) 自身と極体のMinkowski和をとる，(25) 主慣性軸方向にSteiner対称化する，(26) 自身と極体のMinkowski和をとる，(27) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `SteinerSymmetrization → IntersectionBody → PolarDual → DifferenceBody → PolarDual → IntersectionBody → ProjectionBody → PolarDual → IntersectionBody → CentroidBody → DifferenceBody → CentroidBody → ProjectionBody → PolarDual → IntersectionBody → DifferenceBody → SteinerSymmetrization → CentroidBody → ProjectionBody → DifferenceBody → SteinerSymmetrization → ProjectionBody → CentroidBody → MinkowskiPolarSum → SteinerSymmetrization → MinkowskiPolarSum → VolumeNormalization → ConvexFixedPointQuery`

### 三角形変換の合成力学（ExcentralTransform・SymmedianMark・OrbitCompactification・LimitSetExtraction）

- ID: `research.autonomous.triangle_dynamics.b7103a2a25`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `triangle_moduli_dynamics`
- 難度仮説: `31`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「鋭角不等辺三角形を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 傍心三角形へ移す，(2) 類似重心を標識点として付加する，(3) 標識点を三辺に関して反射した三点をとる，(4) 三点を頂点とする向き付き三角形を作る，(5) 三辺の中点三角形へ移す，(6) 垂足三角形へ移す，(7) 類似重心を標識点として付加する，(8) 標識点から三辺への垂足三点をとる，(9) 三点を頂点とする向き付き三角形を作る，(10) 外心を標識点として付加する，(11) 標識点を通る三本のcevianの辺上の足をとる，(12) 三点を頂点とする向き付き三角形を作る，(13) 反中点三角形へ移す，(14) 垂足三角形へ移す，(15) 垂心を標識点として付加する，(16) 標識点を通る三本のcevianの辺上の足をとる，(17) 三点を頂点とする向き付き三角形を作る，(18) 反中点三角形へ移す，(19) 傍心三角形へ移す，(20) 三辺の中点三角形へ移す，(21) 重心・面積・向きを固定して相似正規化する，(22) 相似類のモジュライ点へ射影する，(23) ここまでの合成が誘導する写像を反復する，(24) 退化三角形を境界として軌道をコンパクト化する，(25) 極限集合と周期点データを抽出する。最後に、全周期軌道、吸引域、退化境界上の極限を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ExcentralTransform → SymmedianMark → SideReflectionTrace → TriangleFormation → MedialTransform → OrthicTransform → SymmedianMark → PedalProjection → TriangleFormation → CircumcenterMark → CevianTrace → TriangleFormation → AnticomplementaryTransform → OrthicTransform → OrthocenterMark → CevianTrace → TriangleFormation → AnticomplementaryTransform → ExcentralTransform → MedialTransform → SimilarityNormalization → ModuliProjection → InducedIteration → OrbitCompactification → LimitSetExtraction → TriangleDynamicsQuery`

### 平面代数曲線の合成変換（Catacaustic・ProjectiveDual・Catacaustic・CircleInversion）

- ID: `research.autonomous.plane_curve.cecd229894`
- 状態: `unresolved_by_mathos`
- 射数: `29`
- 問い: `birational_periodicity`
- 難度仮説: `32`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定光源からの反射光線族の包絡線をとる，(2) 正則接線族の射影双対曲線をとる，(3) 固定基準三角形に関する等角共役Cremona像をとる，(4) 射影閉包をとり無限遠点を加える，(5) 基点を避ける一般アフィンチャートへ移す，(6) 法線方向の代数的平行曲線をとる，(7) 射影閉包をとり無限遠点を加える，(8) 基点を避ける一般アフィンチャートへ移す，(9) 固定光源からの反射光線族の包絡線をとる，(10) 射影閉包をとり無限遠点を加える，(11) 基点を避ける一般アフィンチャートへ移す，(12) 正則接線族の射影双対曲線をとる，(13) 射影閉包をとり無限遠点を加える，(14) 基点を避ける一般アフィンチャートへ移す，(15) 固定基準三角形に関する等角共役Cremona像をとる，(16) 法線方向の代数的平行曲線をとる，(17) 固定光源からの反射光線族の包絡線をとる，(18) 固定非退化二次形式に関する極逆像をとる，(19) 法線族の包絡線である発展曲線をとる，(20) 固定基準三角形に関する等角共役Cremona像をとる，(21) 固定非退化二次形式に関する極逆像をとる，(22) 法線族の包絡線である発展曲線をとる，(23) 正則接線族の射影双対曲線をとる，(24) 固定基準三角形に関する等角共役Cremona像をとる，(25) 固定非退化二次形式に関する極逆像をとる，(26) 法線方向の代数的平行曲線をとる，(27) 固定光源からの反射光線族の包絡線をとる，(28) 原点中心の円反転像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `Catacaustic → ProjectiveDual → IsogonalCremona → ProjectiveClosure → AffineChartChange → OffsetCurve → ProjectiveClosure → AffineChartChange → Catacaustic → ProjectiveClosure → AffineChartChange → ProjectiveDual → ProjectiveClosure → AffineChartChange → IsogonalCremona → OffsetCurve → Catacaustic → PolarReciprocal → Evolute → IsogonalCremona → PolarReciprocal → Evolute → ProjectiveDual → IsogonalCremona → PolarReciprocal → OffsetCurve → Catacaustic → CircleInversion → BirationalPeriodQuery`

### 多項式変換と算術観測（ShiftConjugacy・ReciprocalPolynomial・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.69cd14e18e`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `recurrence_order_drop`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根の重心を0へ移す平行移動共役を施す，(2) 根を逆数へ移す相反多項式をとる，(3) 根を二乗するGraeffe変換を施す，(4) 根の重心を0へ移す平行移動共役を施す，(5) 根を逆数へ移す相反多項式をとる，(6) 臨界値を根にもつ消去多項式を作る，(7) 導関数をモニックに再正規化する，(8) 重複度付き根配置へ移す，(9) 根配置からモニック多項式を再構成する，(10) 根を逆数へ移す相反多項式をとる，(11) 重複度付き根配置へ移す，(12) 根配置からモニック多項式を再構成する，(13) 根を二乗するGraeffe変換を施す，(14) 臨界値を根にもつ消去多項式を作る，(15) 根を逆数へ移す相反多項式をとる，(16) 重複度付き根配置へ移す，(17) 根配置からモニック多項式を再構成する，(18) 臨界値を根にもつ消去多項式を作る，(19) 根を二乗するGraeffe変換を施す，(20) 導関数をモニックに再正規化する，(21) 重複度付き根配置へ移す，(22) 根の冪和モーメント列を作る，(23) モーメントからHankel行列族を作る，(24) 主小行列式列をとる，(25) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ShiftConjugacy → ReciprocalPolynomial → GraeffeTransform → ShiftConjugacy → ReciprocalPolynomial → CriticalValuePolynomial → DerivativeRenormalization → RootMultiset → PolynomialReconstruction → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → GraeffeTransform → CriticalValuePolynomial → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → GraeffeTransform → DerivativeRenormalization → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 平面代数曲線の合成変換（Catacaustic・Evolute・ResolveSingularities・CurveInvariantExtraction）

- ID: `research.autonomous.plane_curve.495a882df1`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `singularity_classification`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定光源からの反射光線族の包絡線をとる，(2) 法線族の包絡線である発展曲線をとる，(3) 固定非退化二次形式に関する極逆像をとる，(4) 固定光源からの反射光線族の包絡線をとる，(5) 原点中心の円反転像をとる，(6) 正則接線族の射影双対曲線をとる，(7) 法線族の包絡線である発展曲線をとる，(8) 射影閉包をとり無限遠点を加える，(9) 基点を避ける一般アフィンチャートへ移す，(10) 法線族の包絡線である発展曲線をとる，(11) 固定基準三角形に関する等角共役Cremona像をとる，(12) 正則接線族の射影双対曲線をとる，(13) 固定光源からの反射光線族の包絡線をとる，(14) 原点中心の円反転像をとる，(15) 定義多項式のHessian曲線をとる，(16) 射影閉包をとり無限遠点を加える，(17) 基点を避ける一般アフィンチャートへ移す，(18) 固定光源からの反射光線族の包絡線をとる，(19) 法線方向の代数的平行曲線をとる，(20) 射影閉包をとり無限遠点を加える，(21) 基点を避ける一般アフィンチャートへ移す，(22) 法線族の包絡線である発展曲線をとる，(23) 射影閉包をとり無限遠点を加える，(24) 全特異点を解消して正規化曲線を得る，(25) 次数、分岐、種数、自己交点データを抽出する。最後に、全特異点型と実枝数を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `Catacaustic → Evolute → PolarReciprocal → Catacaustic → CircleInversion → ProjectiveDual → Evolute → ProjectiveClosure → AffineChartChange → Evolute → IsogonalCremona → ProjectiveDual → Catacaustic → CircleInversion → HessianCurve → ProjectiveClosure → AffineChartChange → Catacaustic → OffsetCurve → ProjectiveClosure → AffineChartChange → Evolute → ProjectiveClosure → ResolveSingularities → CurveInvariantExtraction → SingularityQuery`

### 多項式変換と算術観測（ShiftConjugacy・GraeffeTransform・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.5616d99de9`
- 状態: `unresolved_by_mathos`
- 射数: `29`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `33`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根の重心を0へ移す平行移動共役を施す，(2) 根を二乗するGraeffe変換を施す，(3) 根の重心を0へ移す平行移動共役を施す，(4) 根を二乗するGraeffe変換を施す，(5) 臨界値を根にもつ消去多項式を作る，(6) 根の重心を0へ移す平行移動共役を施す，(7) 重複度付き根配置へ移す，(8) 根配置からモニック多項式を再構成する，(9) 根を二乗するGraeffe変換を施す，(10) 導関数をモニックに再正規化する，(11) 重複度付き根配置へ移す，(12) 根配置からモニック多項式を再構成する，(13) 重複度付き根配置へ移す，(14) 根配置からモニック多項式を再構成する，(15) 根を二乗するGraeffe変換を施す，(16) 臨界値を根にもつ消去多項式を作る，(17) 根の重心を0へ移す平行移動共役を施す，(18) 根を逆数へ移す相反多項式をとる，(19) 臨界値を根にもつ消去多項式を作る，(20) 根を逆数へ移す相反多項式をとる，(21) 臨界値を根にもつ消去多項式を作る，(22) 導関数をモニックに再正規化する，(23) 重複度付き根配置へ移す，(24) 根の冪和モーメント列を作る，(25) モーメントからHankel行列族を作る，(26) 主小行列式列をとる，(27) 満たす最小線形漸化式を抽出する，(28) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ShiftConjugacy → GraeffeTransform → ShiftConjugacy → GraeffeTransform → CriticalValuePolynomial → ShiftConjugacy → RootMultiset → PolynomialReconstruction → GraeffeTransform → DerivativeRenormalization → RootMultiset → PolynomialReconstruction → RootMultiset → PolynomialReconstruction → GraeffeTransform → CriticalValuePolynomial → ShiftConjugacy → ReciprocalPolynomial → CriticalValuePolynomial → ReciprocalPolynomial → CriticalValuePolynomial → DerivativeRenormalization → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 凸体関手の合成力学（ProjectionBody・MinkowskiPolarSum・MinkowskiPolarSum・VolumeNormalization）

- ID: `research.autonomous.convex_body.7b91d2cb33`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `29`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 射影体をとる，(2) 自身と極体のMinkowski和をとる，(3) 重心体をとる，(4) 主慣性軸方向にSteiner対称化する，(5) 交叉体をとる，(6) 重心体をとる，(7) 差体をとる，(8) 主慣性軸方向にSteiner対称化する，(9) 差体をとる，(10) 交叉体をとる，(11) 射影体をとる，(12) 重心体をとる，(13) 原点に関する極体をとる，(14) 自身と極体のMinkowski和をとる，(15) 原点に関する極体をとる，(16) 交叉体をとる，(17) 重心体をとる，(18) 差体をとる，(19) 原点に関する極体をとる，(20) 自身と極体のMinkowski和をとる，(21) 交叉体をとる，(22) 原点に関する極体をとる，(23) 差体をとる，(24) 自身と極体のMinkowski和をとる，(25) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectionBody → MinkowskiPolarSum → CentroidBody → SteinerSymmetrization → IntersectionBody → CentroidBody → DifferenceBody → SteinerSymmetrization → DifferenceBody → IntersectionBody → ProjectionBody → CentroidBody → PolarDual → MinkowskiPolarSum → PolarDual → IntersectionBody → CentroidBody → DifferenceBody → PolarDual → MinkowskiPolarSum → IntersectionBody → PolarDual → DifferenceBody → MinkowskiPolarSum → VolumeNormalization → ConvexFixedPointQuery`

### 平面代数曲線の合成変換（PolarReciprocal・OffsetCurve・Evolute・Catacaustic）

- ID: `research.autonomous.plane_curve.69a2cfae34`
- 状態: `unresolved_by_mathos`
- 射数: `27`
- 問い: `birational_periodicity`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定非退化二次形式に関する極逆像をとる，(2) 法線方向の代数的平行曲線をとる，(3) 定義多項式のHessian曲線をとる，(4) 固定非退化二次形式に関する極逆像をとる，(5) 固定基準三角形に関する等角共役Cremona像をとる，(6) 射影閉包をとり無限遠点を加える，(7) 基点を避ける一般アフィンチャートへ移す，(8) 原点中心の円反転像をとる，(9) 正則接線族の射影双対曲線をとる，(10) 定義多項式のHessian曲線をとる，(11) 法線方向の代数的平行曲線をとる，(12) 定義多項式のHessian曲線をとる，(13) 法線族の包絡線である発展曲線をとる，(14) 定義多項式のHessian曲線をとる，(15) 法線方向の代数的平行曲線をとる，(16) 射影閉包をとり無限遠点を加える，(17) 基点を避ける一般アフィンチャートへ移す，(18) 正則接線族の射影双対曲線をとる，(19) 固定光源からの反射光線族の包絡線をとる，(20) 法線方向の代数的平行曲線をとる，(21) 原点中心の円反転像をとる，(22) 固定非退化二次形式に関する極逆像をとる，(23) 原点中心の円反転像をとる，(24) 固定非退化二次形式に関する極逆像をとる，(25) 法線族の包絡線である発展曲線をとる，(26) 固定光源からの反射光線族の包絡線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `PolarReciprocal → OffsetCurve → HessianCurve → PolarReciprocal → IsogonalCremona → ProjectiveClosure → AffineChartChange → CircleInversion → ProjectiveDual → HessianCurve → OffsetCurve → HessianCurve → Evolute → HessianCurve → OffsetCurve → ProjectiveClosure → AffineChartChange → ProjectiveDual → Catacaustic → OffsetCurve → CircleInversion → PolarReciprocal → CircleInversion → PolarReciprocal → Evolute → Catacaustic → BirationalPeriodQuery`

### 凸体関手の合成力学（ProjectionBody・CentroidBody・MinkowskiPolarSum・VolumeNormalization）

- ID: `research.autonomous.convex_body.6b12d9b25b`
- 状態: `unresolved_by_mathos`
- 射数: `27`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 射影体をとる，(2) 重心体をとる，(3) 交叉体をとる，(4) 射影体をとる，(5) 重心体をとる，(6) 射影体をとる，(7) 差体をとる，(8) 重心体をとる，(9) 原点に関する極体をとる，(10) 自身と極体のMinkowski和をとる，(11) 射影体をとる，(12) 差体をとる，(13) 重心体をとる，(14) 差体をとる，(15) 主慣性軸方向にSteiner対称化する，(16) 交叉体をとる，(17) 原点に関する極体をとる，(18) 差体をとる，(19) 主慣性軸方向にSteiner対称化する，(20) 交叉体をとる，(21) 主慣性軸方向にSteiner対称化する，(22) 交叉体をとる，(23) 自身と極体のMinkowski和をとる，(24) 原点に関する極体をとる，(25) 自身と極体のMinkowski和をとる，(26) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectionBody → CentroidBody → IntersectionBody → ProjectionBody → CentroidBody → ProjectionBody → DifferenceBody → CentroidBody → PolarDual → MinkowskiPolarSum → ProjectionBody → DifferenceBody → CentroidBody → DifferenceBody → SteinerSymmetrization → IntersectionBody → PolarDual → DifferenceBody → SteinerSymmetrization → IntersectionBody → SteinerSymmetrization → IntersectionBody → MinkowskiPolarSum → PolarDual → MinkowskiPolarSum → VolumeNormalization → ConvexFixedPointQuery`

### 多項式変換と算術観測（CriticalValuePolynomial・ReciprocalPolynomial・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.90be73ff07`
- 状態: `unresolved_by_mathos`
- 射数: `27`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `31`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 臨界値を根にもつ消去多項式を作る，(2) 根を逆数へ移す相反多項式をとる，(3) 重複度付き根配置へ移す，(4) 根配置からモニック多項式を再構成する，(5) 根を逆数へ移す相反多項式をとる，(6) 重複度付き根配置へ移す，(7) 根配置からモニック多項式を再構成する，(8) 根を二乗するGraeffe変換を施す，(9) 導関数をモニックに再正規化する，(10) 根を逆数へ移す相反多項式をとる，(11) 根の重心を0へ移す平行移動共役を施す，(12) 根を二乗するGraeffe変換を施す，(13) 重複度付き根配置へ移す，(14) 根配置からモニック多項式を再構成する，(15) 導関数をモニックに再正規化する，(16) 根を逆数へ移す相反多項式をとる，(17) 根を二乗するGraeffe変換を施す，(18) 根の重心を0へ移す平行移動共役を施す，(19) 根を二乗するGraeffe変換を施す，(20) 臨界値を根にもつ消去多項式を作る，(21) 重複度付き根配置へ移す，(22) 根の冪和モーメント列を作る，(23) モーメントからHankel行列族を作る，(24) 主小行列式列をとる，(25) 満たす最小線形漸化式を抽出する，(26) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CriticalValuePolynomial → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → GraeffeTransform → DerivativeRenormalization → ReciprocalPolynomial → ShiftConjugacy → GraeffeTransform → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → ReciprocalPolynomial → GraeffeTransform → ShiftConjugacy → GraeffeTransform → CriticalValuePolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 凸体関手の合成力学（MinkowskiPolarSum・PolarDual・ProjectionBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.6136289ba1`
- 状態: `unresolved_by_mathos`
- 射数: `26`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `29`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身と極体のMinkowski和をとる，(2) 原点に関する極体をとる，(3) 差体をとる，(4) 主慣性軸方向にSteiner対称化する，(5) 射影体をとる，(6) 交叉体をとる，(7) 重心体をとる，(8) 差体をとる，(9) 自身と極体のMinkowski和をとる，(10) 主慣性軸方向にSteiner対称化する，(11) 自身と極体のMinkowski和をとる，(12) 主慣性軸方向にSteiner対称化する，(13) 重心体をとる，(14) 自身と極体のMinkowski和をとる，(15) 重心体をとる，(16) 主慣性軸方向にSteiner対称化する，(17) 重心体をとる，(18) 原点に関する極体をとる，(19) 交叉体をとる，(20) 原点に関する極体をとる，(21) 交叉体をとる，(22) 差体をとる，(23) 原点に関する極体をとる，(24) 射影体をとる，(25) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `MinkowskiPolarSum → PolarDual → DifferenceBody → SteinerSymmetrization → ProjectionBody → IntersectionBody → CentroidBody → DifferenceBody → MinkowskiPolarSum → SteinerSymmetrization → MinkowskiPolarSum → SteinerSymmetrization → CentroidBody → MinkowskiPolarSum → CentroidBody → SteinerSymmetrization → CentroidBody → PolarDual → IntersectionBody → PolarDual → IntersectionBody → DifferenceBody → PolarDual → ProjectionBody → VolumeNormalization → ConvexFixedPointQuery`

### 平面代数曲線の合成変換（HessianCurve・ProjectiveClosure・CircleInversion・HessianCurve）

- ID: `research.autonomous.plane_curve.8791963d4e`
- 状態: `unresolved_by_mathos`
- 射数: `29`
- 問い: `birational_periodicity`
- 難度仮説: `32`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 定義多項式のHessian曲線をとる，(2) 射影閉包をとり無限遠点を加える，(3) 基点を避ける一般アフィンチャートへ移す，(4) 固定基準三角形に関する等角共役Cremona像をとる，(5) 法線族の包絡線である発展曲線をとる，(6) 法線方向の代数的平行曲線をとる，(7) 固定光源からの反射光線族の包絡線をとる，(8) 法線族の包絡線である発展曲線をとる，(9) 固定基準三角形に関する等角共役Cremona像をとる，(10) 固定非退化二次形式に関する極逆像をとる，(11) 射影閉包をとり無限遠点を加える，(12) 基点を避ける一般アフィンチャートへ移す，(13) 法線方向の代数的平行曲線をとる，(14) 固定基準三角形に関する等角共役Cremona像をとる，(15) 法線族の包絡線である発展曲線をとる，(16) 固定光源からの反射光線族の包絡線をとる，(17) 正則接線族の射影双対曲線をとる，(18) 法線族の包絡線である発展曲線をとる，(19) 法線方向の代数的平行曲線をとる，(20) 正則接線族の射影双対曲線をとる，(21) 定義多項式のHessian曲線をとる，(22) 原点中心の円反転像をとる，(23) 固定光源からの反射光線族の包絡線をとる，(24) 原点中心の円反転像をとる，(25) 射影閉包をとり無限遠点を加える，(26) 基点を避ける一般アフィンチャートへ移す，(27) 原点中心の円反転像をとる，(28) 定義多項式のHessian曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `HessianCurve → ProjectiveClosure → AffineChartChange → IsogonalCremona → Evolute → OffsetCurve → Catacaustic → Evolute → IsogonalCremona → PolarReciprocal → ProjectiveClosure → AffineChartChange → OffsetCurve → IsogonalCremona → Evolute → Catacaustic → ProjectiveDual → Evolute → OffsetCurve → ProjectiveDual → HessianCurve → CircleInversion → Catacaustic → CircleInversion → ProjectiveClosure → AffineChartChange → CircleInversion → HessianCurve → BirationalPeriodQuery`

### 多項式変換と算術観測（ReciprocalPolynomial・CriticalValuePolynomial・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.865d13af3a`
- 状態: `unresolved_by_mathos`
- 射数: `27`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `31`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を逆数へ移す相反多項式をとる，(2) 臨界値を根にもつ消去多項式を作る，(3) 導関数をモニックに再正規化する，(4) 根を逆数へ移す相反多項式をとる，(5) 根を二乗するGraeffe変換を施す，(6) 臨界値を根にもつ消去多項式を作る，(7) 根の重心を0へ移す平行移動共役を施す，(8) 導関数をモニックに再正規化する，(9) 根を二乗するGraeffe変換を施す，(10) 根を逆数へ移す相反多項式をとる，(11) 臨界値を根にもつ消去多項式を作る，(12) 根の重心を0へ移す平行移動共役を施す，(13) 導関数をモニックに再正規化する，(14) 根を逆数へ移す相反多項式をとる，(15) 臨界値を根にもつ消去多項式を作る，(16) 導関数をモニックに再正規化する，(17) 根の重心を0へ移す平行移動共役を施す，(18) 根を二乗するGraeffe変換を施す，(19) 根の重心を0へ移す平行移動共役を施す，(20) 根を二乗するGraeffe変換を施す，(21) 重複度付き根配置へ移す，(22) 根の冪和モーメント列を作る，(23) モーメントからHankel行列族を作る，(24) 主小行列式列をとる，(25) 満たす最小線形漸化式を抽出する，(26) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ReciprocalPolynomial → CriticalValuePolynomial → DerivativeRenormalization → ReciprocalPolynomial → GraeffeTransform → CriticalValuePolynomial → ShiftConjugacy → DerivativeRenormalization → GraeffeTransform → ReciprocalPolynomial → CriticalValuePolynomial → ShiftConjugacy → DerivativeRenormalization → ReciprocalPolynomial → CriticalValuePolynomial → DerivativeRenormalization → ShiftConjugacy → GraeffeTransform → ShiftConjugacy → GraeffeTransform → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 凸体関手の合成力学（DifferenceBody・PolarDual・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.899cadec47`
- 状態: `unresolved_by_mathos`
- 射数: `29`
- 問い: `convex_body_dynamics`
- 難度仮説: `33`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 差体をとる，(2) 原点に関する極体をとる，(3) 射影体をとる，(4) 交叉体をとる，(5) 原点に関する極体をとる，(6) 重心体をとる，(7) 交叉体をとる，(8) 主慣性軸方向にSteiner対称化する，(9) 交叉体をとる，(10) 射影体をとる，(11) 差体をとる，(12) 重心体をとる，(13) 原点に関する極体をとる，(14) 自身と極体のMinkowski和をとる，(15) 原点に関する極体をとる，(16) 自身と極体のMinkowski和をとる，(17) 差体をとる，(18) 交叉体をとる，(19) 重心体をとる，(20) 主慣性軸方向にSteiner対称化する，(21) 差体をとる，(22) 自身と極体のMinkowski和をとる，(23) 重心体をとる，(24) 主慣性軸方向にSteiner対称化する，(25) 面積と二次モーメントを固定して正規化する，(26) ここまでの凸体関手を反復する，(27) 支持関数の軌道へ移す，(28) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DifferenceBody → PolarDual → ProjectionBody → IntersectionBody → PolarDual → CentroidBody → IntersectionBody → SteinerSymmetrization → IntersectionBody → ProjectionBody → DifferenceBody → CentroidBody → PolarDual → MinkowskiPolarSum → PolarDual → MinkowskiPolarSum → DifferenceBody → IntersectionBody → CentroidBody → SteinerSymmetrization → DifferenceBody → MinkowskiPolarSum → CentroidBody → SteinerSymmetrization → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 平面代数曲線の合成変換（IsogonalCremona・CircleInversion・ProjectiveClosure・AffineChartChange）

- ID: `research.autonomous.plane_curve.45e51d4618`
- 状態: `unresolved_by_mathos`
- 射数: `29`
- 問い: `birational_periodicity`
- 難度仮説: `32`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定基準三角形に関する等角共役Cremona像をとる，(2) 原点中心の円反転像をとる，(3) 固定基準三角形に関する等角共役Cremona像をとる，(4) 定義多項式のHessian曲線をとる，(5) 法線族の包絡線である発展曲線をとる，(6) 固定光源からの反射光線族の包絡線をとる，(7) 法線族の包絡線である発展曲線をとる，(8) 固定基準三角形に関する等角共役Cremona像をとる，(9) 固定非退化二次形式に関する極逆像をとる，(10) 固定基準三角形に関する等角共役Cremona像をとる，(11) 原点中心の円反転像をとる，(12) 正則接線族の射影双対曲線をとる，(13) 原点中心の円反転像をとる，(14) 定義多項式のHessian曲線をとる，(15) 射影閉包をとり無限遠点を加える，(16) 基点を避ける一般アフィンチャートへ移す，(17) 法線族の包絡線である発展曲線をとる，(18) 原点中心の円反転像をとる，(19) 法線方向の代数的平行曲線をとる，(20) 固定非退化二次形式に関する極逆像をとる，(21) 正則接線族の射影双対曲線をとる，(22) 定義多項式のHessian曲線をとる，(23) 法線族の包絡線である発展曲線をとる，(24) 固定光源からの反射光線族の包絡線をとる，(25) 固定非退化二次形式に関する極逆像をとる，(26) 法線方向の代数的平行曲線をとる，(27) 射影閉包をとり無限遠点を加える，(28) 基点を避ける一般アフィンチャートへ移す。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IsogonalCremona → CircleInversion → IsogonalCremona → HessianCurve → Evolute → Catacaustic → Evolute → IsogonalCremona → PolarReciprocal → IsogonalCremona → CircleInversion → ProjectiveDual → CircleInversion → HessianCurve → ProjectiveClosure → AffineChartChange → Evolute → CircleInversion → OffsetCurve → PolarReciprocal → ProjectiveDual → HessianCurve → Evolute → Catacaustic → PolarReciprocal → OffsetCurve → ProjectiveClosure → AffineChartChange → BirationalPeriodQuery`

### 多項式変換と算術観測（GraeffeTransform・ReciprocalPolynomial・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.80862091f6`
- 状態: `unresolved_by_mathos`
- 射数: `28`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `32`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を二乗するGraeffe変換を施す，(2) 根を逆数へ移す相反多項式をとる，(3) 根を二乗するGraeffe変換を施す，(4) 導関数をモニックに再正規化する，(5) 重複度付き根配置へ移す，(6) 根配置からモニック多項式を再構成する，(7) 臨界値を根にもつ消去多項式を作る，(8) 根の重心を0へ移す平行移動共役を施す，(9) 重複度付き根配置へ移す，(10) 根配置からモニック多項式を再構成する，(11) 根を逆数へ移す相反多項式をとる，(12) 導関数をモニックに再正規化する，(13) 臨界値を根にもつ消去多項式を作る，(14) 根を二乗するGraeffe変換を施す，(15) 重複度付き根配置へ移す，(16) 根配置からモニック多項式を再構成する，(17) 導関数をモニックに再正規化する，(18) 根を逆数へ移す相反多項式をとる，(19) 臨界値を根にもつ消去多項式を作る，(20) 根を二乗するGraeffe変換を施す，(21) 臨界値を根にもつ消去多項式を作る，(22) 重複度付き根配置へ移す，(23) 根の冪和モーメント列を作る，(24) モーメントからHankel行列族を作る，(25) 主小行列式列をとる，(26) 満たす最小線形漸化式を抽出する，(27) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `GraeffeTransform → ReciprocalPolynomial → GraeffeTransform → DerivativeRenormalization → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → ShiftConjugacy → RootMultiset → PolynomialReconstruction → ReciprocalPolynomial → DerivativeRenormalization → CriticalValuePolynomial → GraeffeTransform → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → ReciprocalPolynomial → CriticalValuePolynomial → GraeffeTransform → CriticalValuePolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 平面代数曲線の合成変換（OffsetCurve・ProjectiveClosure・ProjectiveClosure・AffineChartChange）

- ID: `research.autonomous.plane_curve.0485fea4e8`
- 状態: `unresolved_by_mathos`
- 射数: `30`
- 問い: `birational_periodicity`
- 難度仮説: `33`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 法線方向の代数的平行曲線をとる，(2) 射影閉包をとり無限遠点を加える，(3) 基点を避ける一般アフィンチャートへ移す，(4) 固定光源からの反射光線族の包絡線をとる，(5) 固定非退化二次形式に関する極逆像をとる，(6) 射影閉包をとり無限遠点を加える，(7) 基点を避ける一般アフィンチャートへ移す，(8) 定義多項式のHessian曲線をとる，(9) 固定非退化二次形式に関する極逆像をとる，(10) 固定基準三角形に関する等角共役Cremona像をとる，(11) 法線族の包絡線である発展曲線をとる，(12) 固定光源からの反射光線族の包絡線をとる，(13) 固定非退化二次形式に関する極逆像をとる，(14) 固定光源からの反射光線族の包絡線をとる，(15) 法線方向の代数的平行曲線をとる，(16) 固定光源からの反射光線族の包絡線をとる，(17) 固定基準三角形に関する等角共役Cremona像をとる，(18) 原点中心の円反転像をとる，(19) 固定非退化二次形式に関する極逆像をとる，(20) 固定光源からの反射光線族の包絡線をとる，(21) 法線族の包絡線である発展曲線をとる，(22) 固定基準三角形に関する等角共役Cremona像をとる，(23) 法線方向の代数的平行曲線をとる，(24) 正則接線族の射影双対曲線をとる，(25) 固定基準三角形に関する等角共役Cremona像をとる，(26) 原点中心の円反転像をとる，(27) 定義多項式のHessian曲線をとる，(28) 射影閉包をとり無限遠点を加える，(29) 基点を避ける一般アフィンチャートへ移す。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `OffsetCurve → ProjectiveClosure → AffineChartChange → Catacaustic → PolarReciprocal → ProjectiveClosure → AffineChartChange → HessianCurve → PolarReciprocal → IsogonalCremona → Evolute → Catacaustic → PolarReciprocal → Catacaustic → OffsetCurve → Catacaustic → IsogonalCremona → CircleInversion → PolarReciprocal → Catacaustic → Evolute → IsogonalCremona → OffsetCurve → ProjectiveDual → IsogonalCremona → CircleInversion → HessianCurve → ProjectiveClosure → AffineChartChange → BirationalPeriodQuery`

### 凸体関手の合成力学（ProjectionBody・MinkowskiPolarSum・DifferenceBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.2afbe11294`
- 状態: `unresolved_by_mathos`
- 射数: `27`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 射影体をとる，(2) 自身と極体のMinkowski和をとる，(3) 原点に関する極体をとる，(4) 射影体をとる，(5) 差体をとる，(6) 交叉体をとる，(7) 主慣性軸方向にSteiner対称化する，(8) 重心体をとる，(9) 自身と極体のMinkowski和をとる，(10) 射影体をとる，(11) 主慣性軸方向にSteiner対称化する，(12) 交叉体をとる，(13) 原点に関する極体をとる，(14) 射影体をとる，(15) 自身と極体のMinkowski和をとる，(16) 差体をとる，(17) 原点に関する極体をとる，(18) 交叉体をとる，(19) 重心体をとる，(20) 自身と極体のMinkowski和をとる，(21) 差体をとる，(22) 主慣性軸方向にSteiner対称化する，(23) 交叉体をとる，(24) 重心体をとる，(25) 差体をとる，(26) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectionBody → MinkowskiPolarSum → PolarDual → ProjectionBody → DifferenceBody → IntersectionBody → SteinerSymmetrization → CentroidBody → MinkowskiPolarSum → ProjectionBody → SteinerSymmetrization → IntersectionBody → PolarDual → ProjectionBody → MinkowskiPolarSum → DifferenceBody → PolarDual → IntersectionBody → CentroidBody → MinkowskiPolarSum → DifferenceBody → SteinerSymmetrization → IntersectionBody → CentroidBody → DifferenceBody → VolumeNormalization → ConvexFixedPointQuery`

### 多項式変換と算術観測（DerivativeRenormalization・CriticalValuePolynomial・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.ce5a95bea7`
- 状態: `unresolved_by_mathos`
- 射数: `28`
- 問い: `recurrence_order_drop`
- 難度仮説: `32`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 導関数をモニックに再正規化する，(2) 臨界値を根にもつ消去多項式を作る，(3) 根を二乗するGraeffe変換を施す，(4) 重複度付き根配置へ移す，(5) 根配置からモニック多項式を再構成する，(6) 根を二乗するGraeffe変換を施す，(7) 重複度付き根配置へ移す，(8) 根配置からモニック多項式を再構成する，(9) 根を二乗するGraeffe変換を施す，(10) 重複度付き根配置へ移す，(11) 根配置からモニック多項式を再構成する，(12) 臨界値を根にもつ消去多項式を作る，(13) 導関数をモニックに再正規化する，(14) 臨界値を根にもつ消去多項式を作る，(15) 根の重心を0へ移す平行移動共役を施す，(16) 導関数をモニックに再正規化する，(17) 根の重心を0へ移す平行移動共役を施す，(18) 導関数をモニックに再正規化する，(19) 根を逆数へ移す相反多項式をとる，(20) 根の重心を0へ移す平行移動共役を施す，(21) 臨界値を根にもつ消去多項式を作る，(22) 根の重心を0へ移す平行移動共役を施す，(23) 重複度付き根配置へ移す，(24) 根の冪和モーメント列を作る，(25) モーメントからHankel行列族を作る，(26) 主小行列式列をとる，(27) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DerivativeRenormalization → CriticalValuePolynomial → GraeffeTransform → RootMultiset → PolynomialReconstruction → GraeffeTransform → RootMultiset → PolynomialReconstruction → GraeffeTransform → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → DerivativeRenormalization → CriticalValuePolynomial → ShiftConjugacy → DerivativeRenormalization → ShiftConjugacy → DerivativeRenormalization → ReciprocalPolynomial → ShiftConjugacy → CriticalValuePolynomial → ShiftConjugacy → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 平面代数曲線の合成変換（CircleInversion・IsogonalCremona・ResolveSingularities・CurveInvariantExtraction）

- ID: `research.autonomous.plane_curve.42c4d83e82`
- 状態: `unresolved_by_mathos`
- 射数: `30`
- 問い: `degree_genus_formula`
- 難度仮説: `34`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 原点中心の円反転像をとる，(2) 固定基準三角形に関する等角共役Cremona像をとる，(3) 固定光源からの反射光線族の包絡線をとる，(4) 法線族の包絡線である発展曲線をとる，(5) 固定光源からの反射光線族の包絡線をとる，(6) 固定非退化二次形式に関する極逆像をとる，(7) 固定基準三角形に関する等角共役Cremona像をとる，(8) 固定光源からの反射光線族の包絡線をとる，(9) 射影閉包をとり無限遠点を加える，(10) 基点を避ける一般アフィンチャートへ移す，(11) 射影閉包をとり無限遠点を加える，(12) 基点を避ける一般アフィンチャートへ移す，(13) 定義多項式のHessian曲線をとる，(14) 固定非退化二次形式に関する極逆像をとる，(15) 原点中心の円反転像をとる，(16) 射影閉包をとり無限遠点を加える，(17) 基点を避ける一般アフィンチャートへ移す，(18) 固定非退化二次形式に関する極逆像をとる，(19) 法線族の包絡線である発展曲線をとる，(20) 固定基準三角形に関する等角共役Cremona像をとる，(21) 固定光源からの反射光線族の包絡線をとる，(22) 法線方向の代数的平行曲線をとる，(23) 固定基準三角形に関する等角共役Cremona像をとる，(24) 原点中心の円反転像をとる，(25) 射影閉包をとり無限遠点を加える，(26) 基点を避ける一般アフィンチャートへ移す，(27) 射影閉包をとり無限遠点を加える，(28) 全特異点を解消して正規化曲線を得る，(29) 次数、分岐、種数、自己交点データを抽出する。最後に、次数と幾何種数を初期曲線の不変量で表示し例外を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CircleInversion → IsogonalCremona → Catacaustic → Evolute → Catacaustic → PolarReciprocal → IsogonalCremona → Catacaustic → ProjectiveClosure → AffineChartChange → ProjectiveClosure → AffineChartChange → HessianCurve → PolarReciprocal → CircleInversion → ProjectiveClosure → AffineChartChange → PolarReciprocal → Evolute → IsogonalCremona → Catacaustic → OffsetCurve → IsogonalCremona → CircleInversion → ProjectiveClosure → AffineChartChange → ProjectiveClosure → ResolveSingularities → CurveInvariantExtraction → DegreeGenusQuery`

### 凸体関手の合成力学（IntersectionBody・MinkowskiPolarSum・PolarDual・VolumeNormalization）

- ID: `research.autonomous.convex_body.2a424b4ca6`
- 状態: `unresolved_by_mathos`
- 射数: `29`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `32`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 交叉体をとる，(2) 自身と極体のMinkowski和をとる，(3) 射影体をとる，(4) 自身と極体のMinkowski和をとる，(5) 射影体をとる，(6) 原点に関する極体をとる，(7) 自身と極体のMinkowski和をとる，(8) 射影体をとる，(9) 主慣性軸方向にSteiner対称化する，(10) 交叉体をとる，(11) 射影体をとる，(12) 主慣性軸方向にSteiner対称化する，(13) 原点に関する極体をとる，(14) 自身と極体のMinkowski和をとる，(15) 差体をとる，(16) 重心体をとる，(17) 差体をとる，(18) 原点に関する極体をとる，(19) 主慣性軸方向にSteiner対称化する，(20) 交叉体をとる，(21) 主慣性軸方向にSteiner対称化する，(22) 差体をとる，(23) 重心体をとる，(24) 差体をとる，(25) 交叉体をとる，(26) 重心体をとる，(27) 原点に関する極体をとる，(28) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IntersectionBody → MinkowskiPolarSum → ProjectionBody → MinkowskiPolarSum → ProjectionBody → PolarDual → MinkowskiPolarSum → ProjectionBody → SteinerSymmetrization → IntersectionBody → ProjectionBody → SteinerSymmetrization → PolarDual → MinkowskiPolarSum → DifferenceBody → CentroidBody → DifferenceBody → PolarDual → SteinerSymmetrization → IntersectionBody → SteinerSymmetrization → DifferenceBody → CentroidBody → DifferenceBody → IntersectionBody → CentroidBody → PolarDual → VolumeNormalization → ConvexFixedPointQuery`

### 多項式変換と算術観測（CriticalValuePolynomial・DerivativeRenormalization・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.677f8b05b7`
- 状態: `unresolved_by_mathos`
- 射数: `30`
- 問い: `recurrence_order_drop`
- 難度仮説: `33`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 臨界値を根にもつ消去多項式を作る，(2) 導関数をモニックに再正規化する，(3) 根を逆数へ移す相反多項式をとる，(4) 導関数をモニックに再正規化する，(5) 臨界値を根にもつ消去多項式を作る，(6) 根の重心を0へ移す平行移動共役を施す，(7) 重複度付き根配置へ移す，(8) 根配置からモニック多項式を再構成する，(9) 根の重心を0へ移す平行移動共役を施す，(10) 導関数をモニックに再正規化する，(11) 根の重心を0へ移す平行移動共役を施す，(12) 根を逆数へ移す相反多項式をとる，(13) 重複度付き根配置へ移す，(14) 根配置からモニック多項式を再構成する，(15) 根を逆数へ移す相反多項式をとる，(16) 重複度付き根配置へ移す，(17) 根配置からモニック多項式を再構成する，(18) 導関数をモニックに再正規化する，(19) 根の重心を0へ移す平行移動共役を施す，(20) 導関数をモニックに再正規化する，(21) 根の重心を0へ移す平行移動共役を施す，(22) 根を逆数へ移す相反多項式をとる，(23) 重複度付き根配置へ移す，(24) 根配置からモニック多項式を再構成する，(25) 重複度付き根配置へ移す，(26) 根の冪和モーメント列を作る，(27) モーメントからHankel行列族を作る，(28) 主小行列式列をとる，(29) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CriticalValuePolynomial → DerivativeRenormalization → ReciprocalPolynomial → DerivativeRenormalization → CriticalValuePolynomial → ShiftConjugacy → RootMultiset → PolynomialReconstruction → ShiftConjugacy → DerivativeRenormalization → ShiftConjugacy → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → ShiftConjugacy → DerivativeRenormalization → ShiftConjugacy → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 平面代数曲線の合成変換（Catacaustic・Evolute・ResolveSingularities・CurveInvariantExtraction）

- ID: `research.autonomous.plane_curve.7ef266e2e8`
- 状態: `unresolved_by_mathos`
- 射数: `27`
- 問い: `singularity_classification`
- 難度仮説: `31`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定光源からの反射光線族の包絡線をとる，(2) 法線族の包絡線である発展曲線をとる，(3) 原点中心の円反転像をとる，(4) 法線族の包絡線である発展曲線をとる，(5) 固定基準三角形に関する等角共役Cremona像をとる，(6) 射影閉包をとり無限遠点を加える，(7) 基点を避ける一般アフィンチャートへ移す，(8) 固定非退化二次形式に関する極逆像をとる，(9) 法線族の包絡線である発展曲線をとる，(10) 固定光源からの反射光線族の包絡線をとる，(11) 固定基準三角形に関する等角共役Cremona像をとる，(12) 固定非退化二次形式に関する極逆像をとる，(13) 固定光源からの反射光線族の包絡線をとる，(14) 法線方向の代数的平行曲線をとる，(15) 射影閉包をとり無限遠点を加える，(16) 基点を避ける一般アフィンチャートへ移す，(17) 定義多項式のHessian曲線をとる，(18) 固定基準三角形に関する等角共役Cremona像をとる，(19) 原点中心の円反転像をとる，(20) 法線方向の代数的平行曲線をとる，(21) 正則接線族の射影双対曲線をとる，(22) 法線方向の代数的平行曲線をとる，(23) 固定光源からの反射光線族の包絡線をとる，(24) 射影閉包をとり無限遠点を加える，(25) 全特異点を解消して正規化曲線を得る，(26) 次数、分岐、種数、自己交点データを抽出する。最後に、全特異点型と実枝数を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `Catacaustic → Evolute → CircleInversion → Evolute → IsogonalCremona → ProjectiveClosure → AffineChartChange → PolarReciprocal → Evolute → Catacaustic → IsogonalCremona → PolarReciprocal → Catacaustic → OffsetCurve → ProjectiveClosure → AffineChartChange → HessianCurve → IsogonalCremona → CircleInversion → OffsetCurve → ProjectiveDual → OffsetCurve → Catacaustic → ProjectiveClosure → ResolveSingularities → CurveInvariantExtraction → SingularityQuery`

### 凸体関手の合成力学（CentroidBody・IntersectionBody・PolarDual・VolumeNormalization）

- ID: `research.autonomous.convex_body.f586a5bd8a`
- 状態: `unresolved_by_mathos`
- 射数: `27`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重心体をとる，(2) 交叉体をとる，(3) 差体をとる，(4) 自身と極体のMinkowski和をとる，(5) 差体をとる，(6) 自身と極体のMinkowski和をとる，(7) 交叉体をとる，(8) 射影体をとる，(9) 重心体をとる，(10) 交叉体をとる，(11) 射影体をとる，(12) 主慣性軸方向にSteiner対称化する，(13) 原点に関する極体をとる，(14) 主慣性軸方向にSteiner対称化する，(15) 自身と極体のMinkowski和をとる，(16) 差体をとる，(17) 射影体をとる，(18) 差体をとる，(19) 交叉体をとる，(20) 重心体をとる，(21) 射影体をとる，(22) 重心体をとる，(23) 自身と極体のMinkowski和をとる，(24) 主慣性軸方向にSteiner対称化する，(25) 原点に関する極体をとる，(26) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CentroidBody → IntersectionBody → DifferenceBody → MinkowskiPolarSum → DifferenceBody → MinkowskiPolarSum → IntersectionBody → ProjectionBody → CentroidBody → IntersectionBody → ProjectionBody → SteinerSymmetrization → PolarDual → SteinerSymmetrization → MinkowskiPolarSum → DifferenceBody → ProjectionBody → DifferenceBody → IntersectionBody → CentroidBody → ProjectionBody → CentroidBody → MinkowskiPolarSum → SteinerSymmetrization → PolarDual → VolumeNormalization → ConvexFixedPointQuery`

### 多項式変換と算術観測（RootMultiset・PolynomialReconstruction・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.cdc3e4d66a`
- 状態: `unresolved_by_mathos`
- 射数: `27`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `31`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重複度付き根配置へ移す，(2) 根配置からモニック多項式を再構成する，(3) 根を逆数へ移す相反多項式をとる，(4) 導関数をモニックに再正規化する，(5) 根の重心を0へ移す平行移動共役を施す，(6) 臨界値を根にもつ消去多項式を作る，(7) 根の重心を0へ移す平行移動共役を施す，(8) 根を逆数へ移す相反多項式をとる，(9) 根の重心を0へ移す平行移動共役を施す，(10) 重複度付き根配置へ移す，(11) 根配置からモニック多項式を再構成する，(12) 導関数をモニックに再正規化する，(13) 根の重心を0へ移す平行移動共役を施す，(14) 根を二乗するGraeffe変換を施す，(15) 臨界値を根にもつ消去多項式を作る，(16) 導関数をモニックに再正規化する，(17) 根を二乗するGraeffe変換を施す，(18) 臨界値を根にもつ消去多項式を作る，(19) 導関数をモニックに再正規化する，(20) 根を逆数へ移す相反多項式をとる，(21) 重複度付き根配置へ移す，(22) 根の冪和モーメント列を作る，(23) モーメントからHankel行列族を作る，(24) 主小行列式列をとる，(25) 満たす最小線形漸化式を抽出する，(26) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `RootMultiset → PolynomialReconstruction → ReciprocalPolynomial → DerivativeRenormalization → ShiftConjugacy → CriticalValuePolynomial → ShiftConjugacy → ReciprocalPolynomial → ShiftConjugacy → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → ShiftConjugacy → GraeffeTransform → CriticalValuePolynomial → DerivativeRenormalization → GraeffeTransform → CriticalValuePolynomial → DerivativeRenormalization → ReciprocalPolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 凸体関手の合成力学（ProjectionBody・PolarDual・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.cc3e89ae34`
- 状態: `unresolved_by_mathos`
- 射数: `29`
- 問い: `convex_body_dynamics`
- 難度仮説: `33`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 射影体をとる，(2) 原点に関する極体をとる，(3) 差体をとる，(4) 重心体をとる，(5) 自身と極体のMinkowski和をとる，(6) 射影体をとる，(7) 自身と極体のMinkowski和をとる，(8) 主慣性軸方向にSteiner対称化する，(9) 自身と極体のMinkowski和をとる，(10) 重心体をとる，(11) 射影体をとる，(12) 差体をとる，(13) 交叉体をとる，(14) 射影体をとる，(15) 差体をとる，(16) 交叉体をとる，(17) 主慣性軸方向にSteiner対称化する，(18) 重心体をとる，(19) 自身と極体のMinkowski和をとる，(20) 差体をとる，(21) 交叉体をとる，(22) 主慣性軸方向にSteiner対称化する，(23) 交叉体をとる，(24) 原点に関する極体をとる，(25) 面積と二次モーメントを固定して正規化する，(26) ここまでの凸体関手を反復する，(27) 支持関数の軌道へ移す，(28) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectionBody → PolarDual → DifferenceBody → CentroidBody → MinkowskiPolarSum → ProjectionBody → MinkowskiPolarSum → SteinerSymmetrization → MinkowskiPolarSum → CentroidBody → ProjectionBody → DifferenceBody → IntersectionBody → ProjectionBody → DifferenceBody → IntersectionBody → SteinerSymmetrization → CentroidBody → MinkowskiPolarSum → DifferenceBody → IntersectionBody → SteinerSymmetrization → IntersectionBody → PolarDual → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 平面代数曲線の合成変換（Evolute・OffsetCurve・ProjectiveDual・HessianCurve）

- ID: `research.autonomous.plane_curve.1444ebe819`
- 状態: `unresolved_by_mathos`
- 射数: `29`
- 問い: `birational_periodicity`
- 難度仮説: `32`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 法線族の包絡線である発展曲線をとる，(2) 法線方向の代数的平行曲線をとる，(3) 法線族の包絡線である発展曲線をとる，(4) 固定光源からの反射光線族の包絡線をとる，(5) 法線方向の代数的平行曲線をとる，(6) 固定光源からの反射光線族の包絡線をとる，(7) 射影閉包をとり無限遠点を加える，(8) 基点を避ける一般アフィンチャートへ移す，(9) 射影閉包をとり無限遠点を加える，(10) 基点を避ける一般アフィンチャートへ移す，(11) 固定光源からの反射光線族の包絡線をとる，(12) 固定非退化二次形式に関する極逆像をとる，(13) 原点中心の円反転像をとる，(14) 固定基準三角形に関する等角共役Cremona像をとる，(15) 正則接線族の射影双対曲線をとる，(16) 固定非退化二次形式に関する極逆像をとる，(17) 固定基準三角形に関する等角共役Cremona像をとる，(18) 定義多項式のHessian曲線をとる，(19) 正則接線族の射影双対曲線をとる，(20) 射影閉包をとり無限遠点を加える，(21) 基点を避ける一般アフィンチャートへ移す，(22) 定義多項式のHessian曲線をとる，(23) 法線方向の代数的平行曲線をとる，(24) 射影閉包をとり無限遠点を加える，(25) 基点を避ける一般アフィンチャートへ移す，(26) 法線族の包絡線である発展曲線をとる，(27) 正則接線族の射影双対曲線をとる，(28) 定義多項式のHessian曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `Evolute → OffsetCurve → Evolute → Catacaustic → OffsetCurve → Catacaustic → ProjectiveClosure → AffineChartChange → ProjectiveClosure → AffineChartChange → Catacaustic → PolarReciprocal → CircleInversion → IsogonalCremona → ProjectiveDual → PolarReciprocal → IsogonalCremona → HessianCurve → ProjectiveDual → ProjectiveClosure → AffineChartChange → HessianCurve → OffsetCurve → ProjectiveClosure → AffineChartChange → Evolute → ProjectiveDual → HessianCurve → BirationalPeriodQuery`

### 多項式変換と算術観測（CriticalValuePolynomial・DerivativeRenormalization・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.1f5ad77069`
- 状態: `unresolved_by_mathos`
- 射数: `27`
- 問い: `recurrence_order_drop`
- 難度仮説: `31`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 臨界値を根にもつ消去多項式を作る，(2) 導関数をモニックに再正規化する，(3) 根の重心を0へ移す平行移動共役を施す，(4) 導関数をモニックに再正規化する，(5) 根を逆数へ移す相反多項式をとる，(6) 導関数をモニックに再正規化する，(7) 根の重心を0へ移す平行移動共役を施す，(8) 根を二乗するGraeffe変換を施す，(9) 根の重心を0へ移す平行移動共役を施す，(10) 導関数をモニックに再正規化する，(11) 根を逆数へ移す相反多項式をとる，(12) 重複度付き根配置へ移す，(13) 根配置からモニック多項式を再構成する，(14) 根を二乗するGraeffe変換を施す，(15) 根を逆数へ移す相反多項式をとる，(16) 臨界値を根にもつ消去多項式を作る，(17) 重複度付き根配置へ移す，(18) 根配置からモニック多項式を再構成する，(19) 根の重心を0へ移す平行移動共役を施す，(20) 臨界値を根にもつ消去多項式を作る，(21) 根を逆数へ移す相反多項式をとる，(22) 重複度付き根配置へ移す，(23) 根の冪和モーメント列を作る，(24) モーメントからHankel行列族を作る，(25) 主小行列式列をとる，(26) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CriticalValuePolynomial → DerivativeRenormalization → ShiftConjugacy → DerivativeRenormalization → ReciprocalPolynomial → DerivativeRenormalization → ShiftConjugacy → GraeffeTransform → ShiftConjugacy → DerivativeRenormalization → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → GraeffeTransform → ReciprocalPolynomial → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → ShiftConjugacy → CriticalValuePolynomial → ReciprocalPolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 平面代数曲線の合成変換（PolarReciprocal・ProjectiveDual・CircleInversion・PolarReciprocal）

- ID: `research.autonomous.plane_curve.304f823242`
- 状態: `unresolved_by_mathos`
- 射数: `27`
- 問い: `birational_periodicity`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定非退化二次形式に関する極逆像をとる，(2) 正則接線族の射影双対曲線をとる，(3) 固定基準三角形に関する等角共役Cremona像をとる，(4) 原点中心の円反転像をとる，(5) 射影閉包をとり無限遠点を加える，(6) 基点を避ける一般アフィンチャートへ移す，(7) 固定非退化二次形式に関する極逆像をとる，(8) 正則接線族の射影双対曲線をとる，(9) 原点中心の円反転像をとる，(10) 正則接線族の射影双対曲線をとる，(11) 原点中心の円反転像をとる，(12) 定義多項式のHessian曲線をとる，(13) 固定光源からの反射光線族の包絡線をとる，(14) 射影閉包をとり無限遠点を加える，(15) 基点を避ける一般アフィンチャートへ移す，(16) 射影閉包をとり無限遠点を加える，(17) 基点を避ける一般アフィンチャートへ移す，(18) 定義多項式のHessian曲線をとる，(19) 固定基準三角形に関する等角共役Cremona像をとる，(20) 正則接線族の射影双対曲線をとる，(21) 固定光源からの反射光線族の包絡線をとる，(22) 固定基準三角形に関する等角共役Cremona像をとる，(23) 法線族の包絡線である発展曲線をとる，(24) 固定基準三角形に関する等角共役Cremona像をとる，(25) 原点中心の円反転像をとる，(26) 固定非退化二次形式に関する極逆像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `PolarReciprocal → ProjectiveDual → IsogonalCremona → CircleInversion → ProjectiveClosure → AffineChartChange → PolarReciprocal → ProjectiveDual → CircleInversion → ProjectiveDual → CircleInversion → HessianCurve → Catacaustic → ProjectiveClosure → AffineChartChange → ProjectiveClosure → AffineChartChange → HessianCurve → IsogonalCremona → ProjectiveDual → Catacaustic → IsogonalCremona → Evolute → IsogonalCremona → CircleInversion → PolarReciprocal → BirationalPeriodQuery`

### 凸体関手の合成力学（PolarDual・MinkowskiPolarSum・IntersectionBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.90ce1d6398`
- 状態: `unresolved_by_mathos`
- 射数: `27`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 原点に関する極体をとる，(2) 自身と極体のMinkowski和をとる，(3) 原点に関する極体をとる，(4) 差体をとる，(5) 重心体をとる，(6) 原点に関する極体をとる，(7) 射影体をとる，(8) 交叉体をとる，(9) 射影体をとる，(10) 重心体をとる，(11) 差体をとる，(12) 重心体をとる，(13) 原点に関する極体をとる，(14) 差体をとる，(15) 重心体をとる，(16) 主慣性軸方向にSteiner対称化する，(17) 自身と極体のMinkowski和をとる，(18) 主慣性軸方向にSteiner対称化する，(19) 射影体をとる，(20) 交叉体をとる，(21) 主慣性軸方向にSteiner対称化する，(22) 差体をとる，(23) 射影体をとる，(24) 自身と極体のMinkowski和をとる，(25) 交叉体をとる，(26) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `PolarDual → MinkowskiPolarSum → PolarDual → DifferenceBody → CentroidBody → PolarDual → ProjectionBody → IntersectionBody → ProjectionBody → CentroidBody → DifferenceBody → CentroidBody → PolarDual → DifferenceBody → CentroidBody → SteinerSymmetrization → MinkowskiPolarSum → SteinerSymmetrization → ProjectionBody → IntersectionBody → SteinerSymmetrization → DifferenceBody → ProjectionBody → MinkowskiPolarSum → IntersectionBody → VolumeNormalization → ConvexFixedPointQuery`

### 多項式変換と算術観測（GraeffeTransform・ShiftConjugacy・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.79e3a6352d`
- 状態: `unresolved_by_mathos`
- 射数: `27`
- 問い: `recurrence_order_drop`
- 難度仮説: `31`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を二乗するGraeffe変換を施す，(2) 根の重心を0へ移す平行移動共役を施す，(3) 根を逆数へ移す相反多項式をとる，(4) 導関数をモニックに再正規化する，(5) 根の重心を0へ移す平行移動共役を施す，(6) 根を逆数へ移す相反多項式をとる，(7) 導関数をモニックに再正規化する，(8) 根を逆数へ移す相反多項式をとる，(9) 根を二乗するGraeffe変換を施す，(10) 重複度付き根配置へ移す，(11) 根配置からモニック多項式を再構成する，(12) 臨界値を根にもつ消去多項式を作る，(13) 重複度付き根配置へ移す，(14) 根配置からモニック多項式を再構成する，(15) 根を逆数へ移す相反多項式をとる，(16) 重複度付き根配置へ移す，(17) 根配置からモニック多項式を再構成する，(18) 根の重心を0へ移す平行移動共役を施す，(19) 導関数をモニックに再正規化する，(20) 根の重心を0へ移す平行移動共役を施す，(21) 根を二乗するGraeffe変換を施す，(22) 重複度付き根配置へ移す，(23) 根の冪和モーメント列を作る，(24) モーメントからHankel行列族を作る，(25) 主小行列式列をとる，(26) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `GraeffeTransform → ShiftConjugacy → ReciprocalPolynomial → DerivativeRenormalization → ShiftConjugacy → ReciprocalPolynomial → DerivativeRenormalization → ReciprocalPolynomial → GraeffeTransform → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → ShiftConjugacy → DerivativeRenormalization → ShiftConjugacy → GraeffeTransform → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 平面代数曲線の合成変換（ProjectiveDual・ProjectiveClosure・ProjectiveClosure・AffineChartChange）

- ID: `research.autonomous.plane_curve.7ccd66ddc7`
- 状態: `unresolved_by_mathos`
- 射数: `27`
- 問い: `birational_periodicity`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 正則接線族の射影双対曲線をとる，(2) 射影閉包をとり無限遠点を加える，(3) 基点を避ける一般アフィンチャートへ移す，(4) 固定非退化二次形式に関する極逆像をとる，(5) 正則接線族の射影双対曲線をとる，(6) 固定光源からの反射光線族の包絡線をとる，(7) 固定基準三角形に関する等角共役Cremona像をとる，(8) 法線族の包絡線である発展曲線をとる，(9) 固定基準三角形に関する等角共役Cremona像をとる，(10) 定義多項式のHessian曲線をとる，(11) 固定非退化二次形式に関する極逆像をとる，(12) 定義多項式のHessian曲線をとる，(13) 固定光源からの反射光線族の包絡線をとる，(14) 定義多項式のHessian曲線をとる，(15) 原点中心の円反転像をとる，(16) 固定非退化二次形式に関する極逆像をとる，(17) 射影閉包をとり無限遠点を加える，(18) 基点を避ける一般アフィンチャートへ移す，(19) 固定基準三角形に関する等角共役Cremona像をとる，(20) 法線方向の代数的平行曲線をとる，(21) 固定光源からの反射光線族の包絡線をとる，(22) 法線方向の代数的平行曲線をとる，(23) 固定光源からの反射光線族の包絡線をとる，(24) 固定基準三角形に関する等角共役Cremona像をとる，(25) 射影閉包をとり無限遠点を加える，(26) 基点を避ける一般アフィンチャートへ移す。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ProjectiveDual → ProjectiveClosure → AffineChartChange → PolarReciprocal → ProjectiveDual → Catacaustic → IsogonalCremona → Evolute → IsogonalCremona → HessianCurve → PolarReciprocal → HessianCurve → Catacaustic → HessianCurve → CircleInversion → PolarReciprocal → ProjectiveClosure → AffineChartChange → IsogonalCremona → OffsetCurve → Catacaustic → OffsetCurve → Catacaustic → IsogonalCremona → ProjectiveClosure → AffineChartChange → BirationalPeriodQuery`

### 凸体関手の合成力学（IntersectionBody・PolarDual・MinkowskiPolarSum・VolumeNormalization）

- ID: `research.autonomous.convex_body.f11d35aa2e`
- 状態: `unresolved_by_mathos`
- 射数: `27`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 交叉体をとる，(2) 原点に関する極体をとる，(3) 重心体をとる，(4) 射影体をとる，(5) 重心体をとる，(6) 自身と極体のMinkowski和をとる，(7) 重心体をとる，(8) 原点に関する極体をとる，(9) 重心体をとる，(10) 主慣性軸方向にSteiner対称化する，(11) 射影体をとる，(12) 主慣性軸方向にSteiner対称化する，(13) 差体をとる，(14) 交叉体をとる，(15) 射影体をとる，(16) 主慣性軸方向にSteiner対称化する，(17) 射影体をとる，(18) 原点に関する極体をとる，(19) 交叉体をとる，(20) 自身と極体のMinkowski和をとる，(21) 交叉体をとる，(22) 主慣性軸方向にSteiner対称化する，(23) 原点に関する極体をとる，(24) 差体をとる，(25) 自身と極体のMinkowski和をとる，(26) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IntersectionBody → PolarDual → CentroidBody → ProjectionBody → CentroidBody → MinkowskiPolarSum → CentroidBody → PolarDual → CentroidBody → SteinerSymmetrization → ProjectionBody → SteinerSymmetrization → DifferenceBody → IntersectionBody → ProjectionBody → SteinerSymmetrization → ProjectionBody → PolarDual → IntersectionBody → MinkowskiPolarSum → IntersectionBody → SteinerSymmetrization → PolarDual → DifferenceBody → MinkowskiPolarSum → VolumeNormalization → ConvexFixedPointQuery`

### 多項式変換と算術観測（ReciprocalPolynomial・CriticalValuePolynomial・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.a9d04dde33`
- 状態: `unresolved_by_mathos`
- 射数: `28`
- 問い: `recurrence_order_drop`
- 難度仮説: `32`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を逆数へ移す相反多項式をとる，(2) 臨界値を根にもつ消去多項式を作る，(3) 導関数をモニックに再正規化する，(4) 根を逆数へ移す相反多項式をとる，(5) 導関数をモニックに再正規化する，(6) 重複度付き根配置へ移す，(7) 根配置からモニック多項式を再構成する，(8) 導関数をモニックに再正規化する，(9) 臨界値を根にもつ消去多項式を作る，(10) 根を二乗するGraeffe変換を施す，(11) 導関数をモニックに再正規化する，(12) 根を逆数へ移す相反多項式をとる，(13) 臨界値を根にもつ消去多項式を作る，(14) 根を二乗するGraeffe変換を施す，(15) 臨界値を根にもつ消去多項式を作る，(16) 根を二乗するGraeffe変換を施す，(17) 重複度付き根配置へ移す，(18) 根配置からモニック多項式を再構成する，(19) 根の重心を0へ移す平行移動共役を施す，(20) 根を二乗するGraeffe変換を施す，(21) 根を逆数へ移す相反多項式をとる，(22) 根の重心を0へ移す平行移動共役を施す，(23) 重複度付き根配置へ移す，(24) 根の冪和モーメント列を作る，(25) モーメントからHankel行列族を作る，(26) 主小行列式列をとる，(27) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ReciprocalPolynomial → CriticalValuePolynomial → DerivativeRenormalization → ReciprocalPolynomial → DerivativeRenormalization → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → CriticalValuePolynomial → GraeffeTransform → DerivativeRenormalization → ReciprocalPolynomial → CriticalValuePolynomial → GraeffeTransform → CriticalValuePolynomial → GraeffeTransform → RootMultiset → PolynomialReconstruction → ShiftConjugacy → GraeffeTransform → ReciprocalPolynomial → ShiftConjugacy → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 平面代数曲線の合成変換（PolarReciprocal・HessianCurve・IsogonalCremona・PolarReciprocal）

- ID: `research.autonomous.plane_curve.4731c21236`
- 状態: `unresolved_by_mathos`
- 射数: `27`
- 問い: `birational_periodicity`
- 難度仮説: `30`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定非退化二次形式に関する極逆像をとる，(2) 定義多項式のHessian曲線をとる，(3) 射影閉包をとり無限遠点を加える，(4) 基点を避ける一般アフィンチャートへ移す，(5) 正則接線族の射影双対曲線をとる，(6) 法線族の包絡線である発展曲線をとる，(7) 法線方向の代数的平行曲線をとる，(8) 固定光源からの反射光線族の包絡線をとる，(9) 固定基準三角形に関する等角共役Cremona像をとる，(10) 法線族の包絡線である発展曲線をとる，(11) 法線方向の代数的平行曲線をとる，(12) 固定非退化二次形式に関する極逆像をとる，(13) 固定光源からの反射光線族の包絡線をとる，(14) 固定基準三角形に関する等角共役Cremona像をとる，(15) 固定光源からの反射光線族の包絡線をとる，(16) 定義多項式のHessian曲線をとる，(17) 固定基準三角形に関する等角共役Cremona像をとる，(18) 原点中心の円反転像をとる，(19) 固定非退化二次形式に関する極逆像をとる，(20) 法線方向の代数的平行曲線をとる，(21) 正則接線族の射影双対曲線をとる，(22) 法線族の包絡線である発展曲線をとる，(23) 固定光源からの反射光線族の包絡線をとる，(24) 定義多項式のHessian曲線をとる，(25) 固定基準三角形に関する等角共役Cremona像をとる，(26) 固定非退化二次形式に関する極逆像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `PolarReciprocal → HessianCurve → ProjectiveClosure → AffineChartChange → ProjectiveDual → Evolute → OffsetCurve → Catacaustic → IsogonalCremona → Evolute → OffsetCurve → PolarReciprocal → Catacaustic → IsogonalCremona → Catacaustic → HessianCurve → IsogonalCremona → CircleInversion → PolarReciprocal → OffsetCurve → ProjectiveDual → Evolute → Catacaustic → HessianCurve → IsogonalCremona → PolarReciprocal → BirationalPeriodQuery`

### 凸体関手の合成力学（SteinerSymmetrization・CentroidBody・DifferenceBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.306ae9fa35`
- 状態: `unresolved_by_mathos`
- 射数: `28`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `31`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 主慣性軸方向にSteiner対称化する，(2) 重心体をとる，(3) 交叉体をとる，(4) 原点に関する極体をとる，(5) 重心体をとる，(6) 自身と極体のMinkowski和をとる，(7) 射影体をとる，(8) 重心体をとる，(9) 交叉体をとる，(10) 自身と極体のMinkowski和をとる，(11) 主慣性軸方向にSteiner対称化する，(12) 交叉体をとる，(13) 原点に関する極体をとる，(14) 交叉体をとる，(15) 主慣性軸方向にSteiner対称化する，(16) 自身と極体のMinkowski和をとる，(17) 原点に関する極体をとる，(18) 射影体をとる，(19) 自身と極体のMinkowski和をとる，(20) 射影体をとる，(21) 原点に関する極体をとる，(22) 主慣性軸方向にSteiner対称化する，(23) 射影体をとる，(24) 差体をとる，(25) 重心体をとる，(26) 差体をとる，(27) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `SteinerSymmetrization → CentroidBody → IntersectionBody → PolarDual → CentroidBody → MinkowskiPolarSum → ProjectionBody → CentroidBody → IntersectionBody → MinkowskiPolarSum → SteinerSymmetrization → IntersectionBody → PolarDual → IntersectionBody → SteinerSymmetrization → MinkowskiPolarSum → PolarDual → ProjectionBody → MinkowskiPolarSum → ProjectionBody → PolarDual → SteinerSymmetrization → ProjectionBody → DifferenceBody → CentroidBody → DifferenceBody → VolumeNormalization → ConvexFixedPointQuery`

### 多項式変換と算術観測（CriticalValuePolynomial・DerivativeRenormalization・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.6cbe528cd7`
- 状態: `unresolved_by_mathos`
- 射数: `28`
- 問い: `recurrence_order_drop`
- 難度仮説: `32`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 臨界値を根にもつ消去多項式を作る，(2) 導関数をモニックに再正規化する，(3) 根を逆数へ移す相反多項式をとる，(4) 根の重心を0へ移す平行移動共役を施す，(5) 臨界値を根にもつ消去多項式を作る，(6) 導関数をモニックに再正規化する，(7) 根を二乗するGraeffe変換を施す，(8) 根を逆数へ移す相反多項式をとる，(9) 重複度付き根配置へ移す，(10) 根配置からモニック多項式を再構成する，(11) 根の重心を0へ移す平行移動共役を施す，(12) 臨界値を根にもつ消去多項式を作る，(13) 根を二乗するGraeffe変換を施す，(14) 導関数をモニックに再正規化する，(15) 根を逆数へ移す相反多項式をとる，(16) 臨界値を根にもつ消去多項式を作る，(17) 根を逆数へ移す相反多項式をとる，(18) 重複度付き根配置へ移す，(19) 根配置からモニック多項式を再構成する，(20) 根を二乗するGraeffe変換を施す，(21) 重複度付き根配置へ移す，(22) 根配置からモニック多項式を再構成する，(23) 重複度付き根配置へ移す，(24) 根の冪和モーメント列を作る，(25) モーメントからHankel行列族を作る，(26) 主小行列式列をとる，(27) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CriticalValuePolynomial → DerivativeRenormalization → ReciprocalPolynomial → ShiftConjugacy → CriticalValuePolynomial → DerivativeRenormalization → GraeffeTransform → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → ShiftConjugacy → CriticalValuePolynomial → GraeffeTransform → DerivativeRenormalization → ReciprocalPolynomial → CriticalValuePolynomial → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → GraeffeTransform → RootMultiset → PolynomialReconstruction → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 凸体関手の合成力学（SteinerSymmetrization・ProjectionBody・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.d68a4a38a3`
- 状態: `unresolved_by_mathos`
- 射数: `31`
- 問い: `convex_body_dynamics`
- 難度仮説: `35`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 主慣性軸方向にSteiner対称化する，(2) 射影体をとる，(3) 原点に関する極体をとる，(4) 射影体をとる，(5) 主慣性軸方向にSteiner対称化する，(6) 射影体をとる，(7) 原点に関する極体をとる，(8) 重心体をとる，(9) 主慣性軸方向にSteiner対称化する，(10) 自身と極体のMinkowski和をとる，(11) 差体をとる，(12) 射影体をとる，(13) 交叉体をとる，(14) 自身と極体のMinkowski和をとる，(15) 交叉体をとる，(16) 差体をとる，(17) 交叉体をとる，(18) 差体をとる，(19) 自身と極体のMinkowski和をとる，(20) 射影体をとる，(21) 主慣性軸方向にSteiner対称化する，(22) 差体をとる，(23) 原点に関する極体をとる，(24) 自身と極体のMinkowski和をとる，(25) 主慣性軸方向にSteiner対称化する，(26) 重心体をとる，(27) 面積と二次モーメントを固定して正規化する，(28) ここまでの凸体関手を反復する，(29) 支持関数の軌道へ移す，(30) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `SteinerSymmetrization → ProjectionBody → PolarDual → ProjectionBody → SteinerSymmetrization → ProjectionBody → PolarDual → CentroidBody → SteinerSymmetrization → MinkowskiPolarSum → DifferenceBody → ProjectionBody → IntersectionBody → MinkowskiPolarSum → IntersectionBody → DifferenceBody → IntersectionBody → DifferenceBody → MinkowskiPolarSum → ProjectionBody → SteinerSymmetrization → DifferenceBody → PolarDual → MinkowskiPolarSum → SteinerSymmetrization → CentroidBody → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 平面代数曲線の合成変換（Evolute・HessianCurve・Evolute・Catacaustic）

- ID: `research.autonomous.plane_curve.db3233530f`
- 状態: `unresolved_by_mathos`
- 射数: `29`
- 問い: `birational_periodicity`
- 難度仮説: `32`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 法線族の包絡線である発展曲線をとる，(2) 定義多項式のHessian曲線をとる，(3) 射影閉包をとり無限遠点を加える，(4) 基点を避ける一般アフィンチャートへ移す，(5) 固定非退化二次形式に関する極逆像をとる，(6) 正則接線族の射影双対曲線をとる，(7) 固定基準三角形に関する等角共役Cremona像をとる，(8) 正則接線族の射影双対曲線をとる，(9) 原点中心の円反転像をとる，(10) 正則接線族の射影双対曲線をとる，(11) 固定光源からの反射光線族の包絡線をとる，(12) 固定基準三角形に関する等角共役Cremona像をとる，(13) 法線方向の代数的平行曲線をとる，(14) 射影閉包をとり無限遠点を加える，(15) 基点を避ける一般アフィンチャートへ移す，(16) 固定光源からの反射光線族の包絡線をとる，(17) 固定基準三角形に関する等角共役Cremona像をとる，(18) 法線族の包絡線である発展曲線をとる，(19) 法線方向の代数的平行曲線をとる，(20) 固定光源からの反射光線族の包絡線をとる，(21) 固定基準三角形に関する等角共役Cremona像をとる，(22) 法線族の包絡線である発展曲線をとる，(23) 固定非退化二次形式に関する極逆像をとる，(24) 原点中心の円反転像をとる，(25) 法線方向の代数的平行曲線をとる，(26) 原点中心の円反転像をとる，(27) 法線族の包絡線である発展曲線をとる，(28) 固定光源からの反射光線族の包絡線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `Evolute → HessianCurve → ProjectiveClosure → AffineChartChange → PolarReciprocal → ProjectiveDual → IsogonalCremona → ProjectiveDual → CircleInversion → ProjectiveDual → Catacaustic → IsogonalCremona → OffsetCurve → ProjectiveClosure → AffineChartChange → Catacaustic → IsogonalCremona → Evolute → OffsetCurve → Catacaustic → IsogonalCremona → Evolute → PolarReciprocal → CircleInversion → OffsetCurve → CircleInversion → Evolute → Catacaustic → BirationalPeriodQuery`

### 多項式変換と算術観測（GraeffeTransform・RootMultiset・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.9cffb5374e`
- 状態: `unresolved_by_mathos`
- 射数: `29`
- 問い: `recurrence_order_drop`
- 難度仮説: `33`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を二乗するGraeffe変換を施す，(2) 重複度付き根配置へ移す，(3) 根配置からモニック多項式を再構成する，(4) 臨界値を根にもつ消去多項式を作る，(5) 導関数をモニックに再正規化する，(6) 臨界値を根にもつ消去多項式を作る，(7) 根の重心を0へ移す平行移動共役を施す，(8) 重複度付き根配置へ移す，(9) 根配置からモニック多項式を再構成する，(10) 導関数をモニックに再正規化する，(11) 根を逆数へ移す相反多項式をとる，(12) 重複度付き根配置へ移す，(13) 根配置からモニック多項式を再構成する，(14) 導関数をモニックに再正規化する，(15) 臨界値を根にもつ消去多項式を作る，(16) 根を二乗するGraeffe変換を施す，(17) 臨界値を根にもつ消去多項式を作る，(18) 根の重心を0へ移す平行移動共役を施す，(19) 根を逆数へ移す相反多項式をとる，(20) 導関数をモニックに再正規化する，(21) 根を逆数へ移す相反多項式をとる，(22) 根の重心を0へ移す平行移動共役を施す，(23) 根を逆数へ移す相反多項式をとる，(24) 重複度付き根配置へ移す，(25) 根の冪和モーメント列を作る，(26) モーメントからHankel行列族を作る，(27) 主小行列式列をとる，(28) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `GraeffeTransform → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → DerivativeRenormalization → CriticalValuePolynomial → ShiftConjugacy → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → CriticalValuePolynomial → GraeffeTransform → CriticalValuePolynomial → ShiftConjugacy → ReciprocalPolynomial → DerivativeRenormalization → ReciprocalPolynomial → ShiftConjugacy → ReciprocalPolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 平面代数曲線の合成変換（IsogonalCremona・HessianCurve・HessianCurve・OffsetCurve）

- ID: `research.autonomous.plane_curve.5e761ff8b7`
- 状態: `unresolved_by_mathos`
- 射数: `29`
- 問い: `birational_periodicity`
- 難度仮説: `32`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定基準三角形に関する等角共役Cremona像をとる，(2) 定義多項式のHessian曲線をとる，(3) 法線族の包絡線である発展曲線をとる，(4) 原点中心の円反転像をとる，(5) 正則接線族の射影双対曲線をとる，(6) 射影閉包をとり無限遠点を加える，(7) 基点を避ける一般アフィンチャートへ移す，(8) 射影閉包をとり無限遠点を加える，(9) 基点を避ける一般アフィンチャートへ移す，(10) 固定基準三角形に関する等角共役Cremona像をとる，(11) 固定光源からの反射光線族の包絡線をとる，(12) 固定基準三角形に関する等角共役Cremona像をとる，(13) 射影閉包をとり無限遠点を加える，(14) 基点を避ける一般アフィンチャートへ移す，(15) 固定基準三角形に関する等角共役Cremona像をとる，(16) 原点中心の円反転像をとる，(17) 射影閉包をとり無限遠点を加える，(18) 基点を避ける一般アフィンチャートへ移す，(19) 原点中心の円反転像をとる，(20) 固定非退化二次形式に関する極逆像をとる，(21) 固定光源からの反射光線族の包絡線をとる，(22) 法線方向の代数的平行曲線をとる，(23) 固定光源からの反射光線族の包絡線をとる，(24) 法線方向の代数的平行曲線をとる，(25) 正則接線族の射影双対曲線をとる，(26) 原点中心の円反転像をとる，(27) 定義多項式のHessian曲線をとる，(28) 法線方向の代数的平行曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IsogonalCremona → HessianCurve → Evolute → CircleInversion → ProjectiveDual → ProjectiveClosure → AffineChartChange → ProjectiveClosure → AffineChartChange → IsogonalCremona → Catacaustic → IsogonalCremona → ProjectiveClosure → AffineChartChange → IsogonalCremona → CircleInversion → ProjectiveClosure → AffineChartChange → CircleInversion → PolarReciprocal → Catacaustic → OffsetCurve → Catacaustic → OffsetCurve → ProjectiveDual → CircleInversion → HessianCurve → OffsetCurve → BirationalPeriodQuery`

### 凸体関手の合成力学（CentroidBody・SteinerSymmetrization・CentroidBody・VolumeNormalization）

- ID: `research.autonomous.convex_body.426d852fea`
- 状態: `unresolved_by_mathos`
- 射数: `29`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `32`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 重心体をとる，(2) 主慣性軸方向にSteiner対称化する，(3) 自身と極体のMinkowski和をとる，(4) 重心体をとる，(5) 射影体をとる，(6) 重心体をとる，(7) 射影体をとる，(8) 主慣性軸方向にSteiner対称化する，(9) 交叉体をとる，(10) 差体をとる，(11) 交叉体をとる，(12) 自身と極体のMinkowski和をとる，(13) 原点に関する極体をとる，(14) 交叉体をとる，(15) 原点に関する極体をとる，(16) 自身と極体のMinkowski和をとる，(17) 交叉体をとる，(18) 差体をとる，(19) 原点に関する極体をとる，(20) 射影体をとる，(21) 差体をとる，(22) 自身と極体のMinkowski和をとる，(23) 差体をとる，(24) 射影体をとる，(25) 原点に関する極体をとる，(26) 主慣性軸方向にSteiner対称化する，(27) 重心体をとる，(28) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CentroidBody → SteinerSymmetrization → MinkowskiPolarSum → CentroidBody → ProjectionBody → CentroidBody → ProjectionBody → SteinerSymmetrization → IntersectionBody → DifferenceBody → IntersectionBody → MinkowskiPolarSum → PolarDual → IntersectionBody → PolarDual → MinkowskiPolarSum → IntersectionBody → DifferenceBody → PolarDual → ProjectionBody → DifferenceBody → MinkowskiPolarSum → DifferenceBody → ProjectionBody → PolarDual → SteinerSymmetrization → CentroidBody → VolumeNormalization → ConvexFixedPointQuery`

### 多項式変換と算術観測（DerivativeRenormalization・ShiftConjugacy・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.15b0c0a4cd`
- 状態: `unresolved_by_mathos`
- 射数: `30`
- 問い: `recurrence_order_drop`
- 難度仮説: `33`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 導関数をモニックに再正規化する，(2) 根の重心を0へ移す平行移動共役を施す，(3) 臨界値を根にもつ消去多項式を作る，(4) 根の重心を0へ移す平行移動共役を施す，(5) 根を逆数へ移す相反多項式をとる，(6) 根の重心を0へ移す平行移動共役を施す，(7) 根を二乗するGraeffe変換を施す，(8) 根を逆数へ移す相反多項式をとる，(9) 根を二乗するGraeffe変換を施す，(10) 臨界値を根にもつ消去多項式を作る，(11) 導関数をモニックに再正規化する，(12) 臨界値を根にもつ消去多項式を作る，(13) 根を逆数へ移す相反多項式をとる，(14) 根を二乗するGraeffe変換を施す，(15) 臨界値を根にもつ消去多項式を作る，(16) 根を逆数へ移す相反多項式をとる，(17) 臨界値を根にもつ消去多項式を作る，(18) 根を逆数へ移す相反多項式をとる，(19) 根を二乗するGraeffe変換を施す，(20) 根の重心を0へ移す平行移動共役を施す，(21) 導関数をモニックに再正規化する，(22) 根を二乗するGraeffe変換を施す，(23) 根の重心を0へ移す平行移動共役を施す，(24) 導関数をモニックに再正規化する，(25) 重複度付き根配置へ移す，(26) 根の冪和モーメント列を作る，(27) モーメントからHankel行列族を作る，(28) 主小行列式列をとる，(29) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DerivativeRenormalization → ShiftConjugacy → CriticalValuePolynomial → ShiftConjugacy → ReciprocalPolynomial → ShiftConjugacy → GraeffeTransform → ReciprocalPolynomial → GraeffeTransform → CriticalValuePolynomial → DerivativeRenormalization → CriticalValuePolynomial → ReciprocalPolynomial → GraeffeTransform → CriticalValuePolynomial → ReciprocalPolynomial → CriticalValuePolynomial → ReciprocalPolynomial → GraeffeTransform → ShiftConjugacy → DerivativeRenormalization → GraeffeTransform → ShiftConjugacy → DerivativeRenormalization → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 凸体関手の合成力学（MinkowskiPolarSum・DifferenceBody・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.a121f897e7`
- 状態: `unresolved_by_mathos`
- 射数: `31`
- 問い: `convex_body_dynamics`
- 難度仮説: `34`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身と極体のMinkowski和をとる，(2) 差体をとる，(3) 自身と極体のMinkowski和をとる，(4) 重心体をとる，(5) 自身と極体のMinkowski和をとる，(6) 差体をとる，(7) 重心体をとる，(8) 射影体をとる，(9) 重心体をとる，(10) 射影体をとる，(11) 原点に関する極体をとる，(12) 重心体をとる，(13) 原点に関する極体をとる，(14) 重心体をとる，(15) 原点に関する極体をとる，(16) 主慣性軸方向にSteiner対称化する，(17) 自身と極体のMinkowski和をとる，(18) 主慣性軸方向にSteiner対称化する，(19) 自身と極体のMinkowski和をとる，(20) 主慣性軸方向にSteiner対称化する，(21) 原点に関する極体をとる，(22) 射影体をとる，(23) 原点に関する極体をとる，(24) 射影体をとる，(25) 主慣性軸方向にSteiner対称化する，(26) 差体をとる，(27) 面積と二次モーメントを固定して正規化する，(28) ここまでの凸体関手を反復する，(29) 支持関数の軌道へ移す，(30) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `MinkowskiPolarSum → DifferenceBody → MinkowskiPolarSum → CentroidBody → MinkowskiPolarSum → DifferenceBody → CentroidBody → ProjectionBody → CentroidBody → ProjectionBody → PolarDual → CentroidBody → PolarDual → CentroidBody → PolarDual → SteinerSymmetrization → MinkowskiPolarSum → SteinerSymmetrization → MinkowskiPolarSum → SteinerSymmetrization → PolarDual → ProjectionBody → PolarDual → ProjectionBody → SteinerSymmetrization → DifferenceBody → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 平面代数曲線の合成変換（CircleInversion・Evolute・ResolveSingularities・CurveInvariantExtraction）

- ID: `research.autonomous.plane_curve.8a08ee9597`
- 状態: `unresolved_by_mathos`
- 射数: `29`
- 問い: `degree_genus_formula`
- 難度仮説: `32`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 原点中心の円反転像をとる，(2) 法線族の包絡線である発展曲線をとる，(3) 原点中心の円反転像をとる，(4) 固定基準三角形に関する等角共役Cremona像をとる，(5) 原点中心の円反転像をとる，(6) 固定基準三角形に関する等角共役Cremona像をとる，(7) 固定非退化二次形式に関する極逆像をとる，(8) 法線方向の代数的平行曲線をとる，(9) 法線族の包絡線である発展曲線をとる，(10) 固定光源からの反射光線族の包絡線をとる，(11) 射影閉包をとり無限遠点を加える，(12) 基点を避ける一般アフィンチャートへ移す，(13) 原点中心の円反転像をとる，(14) 固定非退化二次形式に関する極逆像をとる，(15) 射影閉包をとり無限遠点を加える，(16) 基点を避ける一般アフィンチャートへ移す，(17) 法線方向の代数的平行曲線をとる，(18) 固定非退化二次形式に関する極逆像をとる，(19) 法線方向の代数的平行曲線をとる，(20) 射影閉包をとり無限遠点を加える，(21) 基点を避ける一般アフィンチャートへ移す，(22) 固定基準三角形に関する等角共役Cremona像をとる，(23) 固定光源からの反射光線族の包絡線をとる，(24) 法線方向の代数的平行曲線をとる，(25) 固定基準三角形に関する等角共役Cremona像をとる，(26) 射影閉包をとり無限遠点を加える，(27) 全特異点を解消して正規化曲線を得る，(28) 次数、分岐、種数、自己交点データを抽出する。最後に、次数と幾何種数を初期曲線の不変量で表示し例外を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CircleInversion → Evolute → CircleInversion → IsogonalCremona → CircleInversion → IsogonalCremona → PolarReciprocal → OffsetCurve → Evolute → Catacaustic → ProjectiveClosure → AffineChartChange → CircleInversion → PolarReciprocal → ProjectiveClosure → AffineChartChange → OffsetCurve → PolarReciprocal → OffsetCurve → ProjectiveClosure → AffineChartChange → IsogonalCremona → Catacaustic → OffsetCurve → IsogonalCremona → ProjectiveClosure → ResolveSingularities → CurveInvariantExtraction → DegreeGenusQuery`

### 多項式変換と算術観測（CriticalValuePolynomial・ShiftConjugacy・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.20f3545b0f`
- 状態: `unresolved_by_mathos`
- 射数: `31`
- 問い: `recurrence_order_drop`
- 難度仮説: `35`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 臨界値を根にもつ消去多項式を作る，(2) 根の重心を0へ移す平行移動共役を施す，(3) 根を逆数へ移す相反多項式をとる，(4) 重複度付き根配置へ移す，(5) 根配置からモニック多項式を再構成する，(6) 重複度付き根配置へ移す，(7) 根配置からモニック多項式を再構成する，(8) 根を逆数へ移す相反多項式をとる，(9) 根の重心を0へ移す平行移動共役を施す，(10) 根を二乗するGraeffe変換を施す，(11) 臨界値を根にもつ消去多項式を作る，(12) 導関数をモニックに再正規化する，(13) 根を逆数へ移す相反多項式をとる，(14) 導関数をモニックに再正規化する，(15) 根を二乗するGraeffe変換を施す，(16) 導関数をモニックに再正規化する，(17) 根の重心を0へ移す平行移動共役を施す，(18) 重複度付き根配置へ移す，(19) 根配置からモニック多項式を再構成する，(20) 根を二乗するGraeffe変換を施す，(21) 重複度付き根配置へ移す，(22) 根配置からモニック多項式を再構成する，(23) 臨界値を根にもつ消去多項式を作る，(24) 根を二乗するGraeffe変換を施す，(25) 臨界値を根にもつ消去多項式を作る，(26) 重複度付き根配置へ移す，(27) 根の冪和モーメント列を作る，(28) モーメントからHankel行列族を作る，(29) 主小行列式列をとる，(30) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CriticalValuePolynomial → ShiftConjugacy → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → RootMultiset → PolynomialReconstruction → ReciprocalPolynomial → ShiftConjugacy → GraeffeTransform → CriticalValuePolynomial → DerivativeRenormalization → ReciprocalPolynomial → DerivativeRenormalization → GraeffeTransform → DerivativeRenormalization → ShiftConjugacy → RootMultiset → PolynomialReconstruction → GraeffeTransform → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → GraeffeTransform → CriticalValuePolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 平面代数曲線の合成変換（CircleInversion・ProjectiveClosure・IsogonalCremona・PolarReciprocal）

- ID: `research.autonomous.plane_curve.13cd7f280d`
- 状態: `unresolved_by_mathos`
- 射数: `30`
- 問い: `birational_periodicity`
- 難度仮説: `33`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 原点中心の円反転像をとる，(2) 射影閉包をとり無限遠点を加える，(3) 基点を避ける一般アフィンチャートへ移す，(4) 原点中心の円反転像をとる，(5) 定義多項式のHessian曲線をとる，(6) 原点中心の円反転像をとる，(7) 法線方向の代数的平行曲線をとる，(8) 固定非退化二次形式に関する極逆像をとる，(9) 固定基準三角形に関する等角共役Cremona像をとる，(10) 法線方向の代数的平行曲線をとる，(11) 固定光源からの反射光線族の包絡線をとる，(12) 射影閉包をとり無限遠点を加える，(13) 基点を避ける一般アフィンチャートへ移す，(14) 法線方向の代数的平行曲線をとる，(15) 法線族の包絡線である発展曲線をとる，(16) 法線方向の代数的平行曲線をとる，(17) 固定光源からの反射光線族の包絡線をとる，(18) 法線族の包絡線である発展曲線をとる，(19) 定義多項式のHessian曲線をとる，(20) 固定基準三角形に関する等角共役Cremona像をとる，(21) 固定光源からの反射光線族の包絡線をとる，(22) 法線族の包絡線である発展曲線をとる，(23) 射影閉包をとり無限遠点を加える，(24) 基点を避ける一般アフィンチャートへ移す，(25) 射影閉包をとり無限遠点を加える，(26) 基点を避ける一般アフィンチャートへ移す，(27) 原点中心の円反転像をとる，(28) 固定基準三角形に関する等角共役Cremona像をとる，(29) 固定非退化二次形式に関する極逆像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CircleInversion → ProjectiveClosure → AffineChartChange → CircleInversion → HessianCurve → CircleInversion → OffsetCurve → PolarReciprocal → IsogonalCremona → OffsetCurve → Catacaustic → ProjectiveClosure → AffineChartChange → OffsetCurve → Evolute → OffsetCurve → Catacaustic → Evolute → HessianCurve → IsogonalCremona → Catacaustic → Evolute → ProjectiveClosure → AffineChartChange → ProjectiveClosure → AffineChartChange → CircleInversion → IsogonalCremona → PolarReciprocal → BirationalPeriodQuery`

### 凸体関手の合成力学（IntersectionBody・ProjectionBody・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.7bc4e090f1`
- 状態: `unresolved_by_mathos`
- 射数: `30`
- 問い: `convex_body_dynamics`
- 難度仮説: `34`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 交叉体をとる，(2) 射影体をとる，(3) 交叉体をとる，(4) 自身と極体のMinkowski和をとる，(5) 原点に関する極体をとる，(6) 射影体をとる，(7) 主慣性軸方向にSteiner対称化する，(8) 重心体をとる，(9) 自身と極体のMinkowski和をとる，(10) 交叉体をとる，(11) 原点に関する極体をとる，(12) 交叉体をとる，(13) 自身と極体のMinkowski和をとる，(14) 差体をとる，(15) 主慣性軸方向にSteiner対称化する，(16) 差体をとる，(17) 自身と極体のMinkowski和をとる，(18) 交叉体をとる，(19) 自身と極体のMinkowski和をとる，(20) 主慣性軸方向にSteiner対称化する，(21) 重心体をとる，(22) 原点に関する極体をとる，(23) 射影体をとる，(24) 重心体をとる，(25) 原点に関する極体をとる，(26) 面積と二次モーメントを固定して正規化する，(27) ここまでの凸体関手を反復する，(28) 支持関数の軌道へ移す，(29) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IntersectionBody → ProjectionBody → IntersectionBody → MinkowskiPolarSum → PolarDual → ProjectionBody → SteinerSymmetrization → CentroidBody → MinkowskiPolarSum → IntersectionBody → PolarDual → IntersectionBody → MinkowskiPolarSum → DifferenceBody → SteinerSymmetrization → DifferenceBody → MinkowskiPolarSum → IntersectionBody → MinkowskiPolarSum → SteinerSymmetrization → CentroidBody → PolarDual → ProjectionBody → CentroidBody → PolarDual → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 多項式変換と算術観測（ReciprocalPolynomial・GraeffeTransform・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.efc7f4cd20`
- 状態: `unresolved_by_mathos`
- 射数: `28`
- 問い: `recurrence_order_drop`
- 難度仮説: `32`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を逆数へ移す相反多項式をとる，(2) 根を二乗するGraeffe変換を施す，(3) 臨界値を根にもつ消去多項式を作る，(4) 導関数をモニックに再正規化する，(5) 臨界値を根にもつ消去多項式を作る，(6) 重複度付き根配置へ移す，(7) 根配置からモニック多項式を再構成する，(8) 根を逆数へ移す相反多項式をとる，(9) 導関数をモニックに再正規化する，(10) 根を逆数へ移す相反多項式をとる，(11) 根を二乗するGraeffe変換を施す，(12) 重複度付き根配置へ移す，(13) 根配置からモニック多項式を再構成する，(14) 臨界値を根にもつ消去多項式を作る，(15) 根の重心を0へ移す平行移動共役を施す，(16) 根を二乗するGraeffe変換を施す，(17) 導関数をモニックに再正規化する，(18) 根を逆数へ移す相反多項式をとる，(19) 根を二乗するGraeffe変換を施す，(20) 重複度付き根配置へ移す，(21) 根配置からモニック多項式を再構成する，(22) 導関数をモニックに再正規化する，(23) 重複度付き根配置へ移す，(24) 根の冪和モーメント列を作る，(25) モーメントからHankel行列族を作る，(26) 主小行列式列をとる，(27) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ReciprocalPolynomial → GraeffeTransform → CriticalValuePolynomial → DerivativeRenormalization → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → ReciprocalPolynomial → DerivativeRenormalization → ReciprocalPolynomial → GraeffeTransform → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → ShiftConjugacy → GraeffeTransform → DerivativeRenormalization → ReciprocalPolynomial → GraeffeTransform → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 平面代数曲線の合成変換（PolarReciprocal・HessianCurve・ProjectiveClosure・AffineChartChange）

- ID: `research.autonomous.plane_curve.27de193ace`
- 状態: `unresolved_by_mathos`
- 射数: `29`
- 問い: `birational_periodicity`
- 難度仮説: `32`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定非退化二次形式に関する極逆像をとる，(2) 定義多項式のHessian曲線をとる，(3) 原点中心の円反転像をとる，(4) 正則接線族の射影双対曲線をとる，(5) 法線方向の代数的平行曲線をとる，(6) 原点中心の円反転像をとる，(7) 正則接線族の射影双対曲線をとる，(8) 定義多項式のHessian曲線をとる，(9) 正則接線族の射影双対曲線をとる，(10) 定義多項式のHessian曲線をとる，(11) 法線方向の代数的平行曲線をとる，(12) 定義多項式のHessian曲線をとる，(13) 正則接線族の射影双対曲線をとる，(14) 原点中心の円反転像をとる，(15) 固定光源からの反射光線族の包絡線をとる，(16) 固定非退化二次形式に関する極逆像をとる，(17) 法線族の包絡線である発展曲線をとる，(18) 原点中心の円反転像をとる，(19) 固定非退化二次形式に関する極逆像をとる，(20) 射影閉包をとり無限遠点を加える，(21) 基点を避ける一般アフィンチャートへ移す，(22) 射影閉包をとり無限遠点を加える，(23) 基点を避ける一般アフィンチャートへ移す，(24) 固定光源からの反射光線族の包絡線をとる，(25) 法線方向の代数的平行曲線をとる，(26) 法線族の包絡線である発展曲線をとる，(27) 射影閉包をとり無限遠点を加える，(28) 基点を避ける一般アフィンチャートへ移す。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `PolarReciprocal → HessianCurve → CircleInversion → ProjectiveDual → OffsetCurve → CircleInversion → ProjectiveDual → HessianCurve → ProjectiveDual → HessianCurve → OffsetCurve → HessianCurve → ProjectiveDual → CircleInversion → Catacaustic → PolarReciprocal → Evolute → CircleInversion → PolarReciprocal → ProjectiveClosure → AffineChartChange → ProjectiveClosure → AffineChartChange → Catacaustic → OffsetCurve → Evolute → ProjectiveClosure → AffineChartChange → BirationalPeriodQuery`

### 凸体関手の合成力学（MinkowskiPolarSum・SteinerSymmetrization・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.87000eb6ff`
- 状態: `unresolved_by_mathos`
- 射数: `30`
- 問い: `convex_body_dynamics`
- 難度仮説: `34`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身と極体のMinkowski和をとる，(2) 主慣性軸方向にSteiner対称化する，(3) 交叉体をとる，(4) 主慣性軸方向にSteiner対称化する，(5) 原点に関する極体をとる，(6) 自身と極体のMinkowski和をとる，(7) 射影体をとる，(8) 重心体をとる，(9) 主慣性軸方向にSteiner対称化する，(10) 交叉体をとる，(11) 原点に関する極体をとる，(12) 射影体をとる，(13) 主慣性軸方向にSteiner対称化する，(14) 原点に関する極体をとる，(15) 重心体をとる，(16) 交叉体をとる，(17) 重心体をとる，(18) 差体をとる，(19) 自身と極体のMinkowski和をとる，(20) 交叉体をとる，(21) 原点に関する極体をとる，(22) 主慣性軸方向にSteiner対称化する，(23) 交叉体をとる，(24) 重心体をとる，(25) 自身と極体のMinkowski和をとる，(26) 面積と二次モーメントを固定して正規化する，(27) ここまでの凸体関手を反復する，(28) 支持関数の軌道へ移す，(29) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `MinkowskiPolarSum → SteinerSymmetrization → IntersectionBody → SteinerSymmetrization → PolarDual → MinkowskiPolarSum → ProjectionBody → CentroidBody → SteinerSymmetrization → IntersectionBody → PolarDual → ProjectionBody → SteinerSymmetrization → PolarDual → CentroidBody → IntersectionBody → CentroidBody → DifferenceBody → MinkowskiPolarSum → IntersectionBody → PolarDual → SteinerSymmetrization → IntersectionBody → CentroidBody → MinkowskiPolarSum → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 多項式変換と算術観測（ReciprocalPolynomial・RootMultiset・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.74f7cc898b`
- 状態: `unresolved_by_mathos`
- 射数: `30`
- 問い: `recurrence_order_drop`
- 難度仮説: `34`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を逆数へ移す相反多項式をとる，(2) 重複度付き根配置へ移す，(3) 根配置からモニック多項式を再構成する，(4) 臨界値を根にもつ消去多項式を作る，(5) 重複度付き根配置へ移す，(6) 根配置からモニック多項式を再構成する，(7) 根の重心を0へ移す平行移動共役を施す，(8) 導関数をモニックに再正規化する，(9) 臨界値を根にもつ消去多項式を作る，(10) 根の重心を0へ移す平行移動共役を施す，(11) 根を逆数へ移す相反多項式をとる，(12) 導関数をモニックに再正規化する，(13) 根を二乗するGraeffe変換を施す，(14) 導関数をモニックに再正規化する，(15) 根を二乗するGraeffe変換を施す，(16) 臨界値を根にもつ消去多項式を作る，(17) 根を逆数へ移す相反多項式をとる，(18) 重複度付き根配置へ移す，(19) 根配置からモニック多項式を再構成する，(20) 導関数をモニックに再正規化する，(21) 臨界値を根にもつ消去多項式を作る，(22) 根の重心を0へ移す平行移動共役を施す，(23) 臨界値を根にもつ消去多項式を作る，(24) 根を逆数へ移す相反多項式をとる，(25) 重複度付き根配置へ移す，(26) 根の冪和モーメント列を作る，(27) モーメントからHankel行列族を作る，(28) 主小行列式列をとる，(29) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → ShiftConjugacy → DerivativeRenormalization → CriticalValuePolynomial → ShiftConjugacy → ReciprocalPolynomial → DerivativeRenormalization → GraeffeTransform → DerivativeRenormalization → GraeffeTransform → CriticalValuePolynomial → ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → CriticalValuePolynomial → ShiftConjugacy → CriticalValuePolynomial → ReciprocalPolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 平面代数曲線の合成変換（OffsetCurve・ProjectiveDual・ProjectiveClosure・AffineChartChange）

- ID: `research.autonomous.plane_curve.0a33b06c3f`
- 状態: `unresolved_by_mathos`
- 射数: `29`
- 問い: `birational_periodicity`
- 難度仮説: `32`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 法線方向の代数的平行曲線をとる，(2) 正則接線族の射影双対曲線をとる，(3) 定義多項式のHessian曲線をとる，(4) 固定非退化二次形式に関する極逆像をとる，(5) 法線方向の代数的平行曲線をとる，(6) 原点中心の円反転像をとる，(7) 正則接線族の射影双対曲線をとる，(8) 原点中心の円反転像をとる，(9) 法線方向の代数的平行曲線をとる，(10) 定義多項式のHessian曲線をとる，(11) 原点中心の円反転像をとる，(12) 定義多項式のHessian曲線をとる，(13) 原点中心の円反転像をとる，(14) 射影閉包をとり無限遠点を加える，(15) 基点を避ける一般アフィンチャートへ移す，(16) 法線族の包絡線である発展曲線をとる，(17) 定義多項式のHessian曲線をとる，(18) 射影閉包をとり無限遠点を加える，(19) 基点を避ける一般アフィンチャートへ移す，(20) 射影閉包をとり無限遠点を加える，(21) 基点を避ける一般アフィンチャートへ移す，(22) 法線族の包絡線である発展曲線をとる，(23) 固定基準三角形に関する等角共役Cremona像をとる，(24) 固定非退化二次形式に関する極逆像をとる，(25) 法線族の包絡線である発展曲線をとる，(26) 固定光源からの反射光線族の包絡線をとる，(27) 射影閉包をとり無限遠点を加える，(28) 基点を避ける一般アフィンチャートへ移す。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `OffsetCurve → ProjectiveDual → HessianCurve → PolarReciprocal → OffsetCurve → CircleInversion → ProjectiveDual → CircleInversion → OffsetCurve → HessianCurve → CircleInversion → HessianCurve → CircleInversion → ProjectiveClosure → AffineChartChange → Evolute → HessianCurve → ProjectiveClosure → AffineChartChange → ProjectiveClosure → AffineChartChange → Evolute → IsogonalCremona → PolarReciprocal → Evolute → Catacaustic → ProjectiveClosure → AffineChartChange → BirationalPeriodQuery`

### 凸体関手の合成力学（SteinerSymmetrization・PolarDual・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.ef9f6bba7c`
- 状態: `unresolved_by_mathos`
- 射数: `30`
- 問い: `convex_body_dynamics`
- 難度仮説: `34`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 主慣性軸方向にSteiner対称化する，(2) 原点に関する極体をとる，(3) 重心体をとる，(4) 原点に関する極体をとる，(5) 自身と極体のMinkowski和をとる，(6) 交叉体をとる，(7) 原点に関する極体をとる，(8) 交叉体をとる，(9) 自身と極体のMinkowski和をとる，(10) 射影体をとる，(11) 主慣性軸方向にSteiner対称化する，(12) 原点に関する極体をとる，(13) 主慣性軸方向にSteiner対称化する，(14) 差体をとる，(15) 射影体をとる，(16) 差体をとる，(17) 主慣性軸方向にSteiner対称化する，(18) 交叉体をとる，(19) 自身と極体のMinkowski和をとる，(20) 差体をとる，(21) 交叉体をとる，(22) 差体をとる，(23) 射影体をとる，(24) 主慣性軸方向にSteiner対称化する，(25) 原点に関する極体をとる，(26) 面積と二次モーメントを固定して正規化する，(27) ここまでの凸体関手を反復する，(28) 支持関数の軌道へ移す，(29) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `SteinerSymmetrization → PolarDual → CentroidBody → PolarDual → MinkowskiPolarSum → IntersectionBody → PolarDual → IntersectionBody → MinkowskiPolarSum → ProjectionBody → SteinerSymmetrization → PolarDual → SteinerSymmetrization → DifferenceBody → ProjectionBody → DifferenceBody → SteinerSymmetrization → IntersectionBody → MinkowskiPolarSum → DifferenceBody → IntersectionBody → DifferenceBody → ProjectionBody → SteinerSymmetrization → PolarDual → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 多項式変換と算術観測（CriticalValuePolynomial・RootMultiset・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.5ebab1dc4d`
- 状態: `unresolved_by_mathos`
- 射数: `28`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `32`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 臨界値を根にもつ消去多項式を作る，(2) 重複度付き根配置へ移す，(3) 根配置からモニック多項式を再構成する，(4) 導関数をモニックに再正規化する，(5) 臨界値を根にもつ消去多項式を作る，(6) 根を逆数へ移す相反多項式をとる，(7) 導関数をモニックに再正規化する，(8) 根の重心を0へ移す平行移動共役を施す，(9) 導関数をモニックに再正規化する，(10) 根を逆数へ移す相反多項式をとる，(11) 根を二乗するGraeffe変換を施す，(12) 重複度付き根配置へ移す，(13) 根配置からモニック多項式を再構成する，(14) 臨界値を根にもつ消去多項式を作る，(15) 根の重心を0へ移す平行移動共役を施す，(16) 根を逆数へ移す相反多項式をとる，(17) 導関数をモニックに再正規化する，(18) 臨界値を根にもつ消去多項式を作る，(19) 根を二乗するGraeffe変換を施す，(20) 根の重心を0へ移す平行移動共役を施す，(21) 根を逆数へ移す相反多項式をとる，(22) 重複度付き根配置へ移す，(23) 根の冪和モーメント列を作る，(24) モーメントからHankel行列族を作る，(25) 主小行列式列をとる，(26) 満たす最小線形漸化式を抽出する，(27) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → CriticalValuePolynomial → ReciprocalPolynomial → DerivativeRenormalization → ShiftConjugacy → DerivativeRenormalization → ReciprocalPolynomial → GraeffeTransform → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → ShiftConjugacy → ReciprocalPolynomial → DerivativeRenormalization → CriticalValuePolynomial → GraeffeTransform → ShiftConjugacy → ReciprocalPolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 平面代数曲線の合成変換（HessianCurve・CircleInversion・Evolute・IsogonalCremona）

- ID: `research.autonomous.plane_curve.c1a0207a26`
- 状態: `unresolved_by_mathos`
- 射数: `31`
- 問い: `birational_periodicity`
- 難度仮説: `34`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 定義多項式のHessian曲線をとる，(2) 原点中心の円反転像をとる，(3) 固定光源からの反射光線族の包絡線をとる，(4) 原点中心の円反転像をとる，(5) 固定基準三角形に関する等角共役Cremona像をとる，(6) 定義多項式のHessian曲線をとる，(7) 射影閉包をとり無限遠点を加える，(8) 基点を避ける一般アフィンチャートへ移す，(9) 原点中心の円反転像をとる，(10) 固定光源からの反射光線族の包絡線をとる，(11) 固定基準三角形に関する等角共役Cremona像をとる，(12) 射影閉包をとり無限遠点を加える，(13) 基点を避ける一般アフィンチャートへ移す，(14) 法線族の包絡線である発展曲線をとる，(15) 正則接線族の射影双対曲線をとる，(16) 原点中心の円反転像をとる，(17) 固定基準三角形に関する等角共役Cremona像をとる，(18) 法線族の包絡線である発展曲線をとる，(19) 法線方向の代数的平行曲線をとる，(20) 原点中心の円反転像をとる，(21) 固定光源からの反射光線族の包絡線をとる，(22) 定義多項式のHessian曲線をとる，(23) 固定非退化二次形式に関する極逆像をとる，(24) 法線方向の代数的平行曲線をとる，(25) 固定光源からの反射光線族の包絡線をとる，(26) 法線族の包絡線である発展曲線をとる，(27) 固定光源からの反射光線族の包絡線をとる，(28) 固定基準三角形に関する等角共役Cremona像をとる，(29) 法線族の包絡線である発展曲線をとる，(30) 固定基準三角形に関する等角共役Cremona像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `HessianCurve → CircleInversion → Catacaustic → CircleInversion → IsogonalCremona → HessianCurve → ProjectiveClosure → AffineChartChange → CircleInversion → Catacaustic → IsogonalCremona → ProjectiveClosure → AffineChartChange → Evolute → ProjectiveDual → CircleInversion → IsogonalCremona → Evolute → OffsetCurve → CircleInversion → Catacaustic → HessianCurve → PolarReciprocal → OffsetCurve → Catacaustic → Evolute → Catacaustic → IsogonalCremona → Evolute → IsogonalCremona → BirationalPeriodQuery`

### 凸体関手の合成力学（IntersectionBody・SteinerSymmetrization・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.3e69deaba5`
- 状態: `unresolved_by_mathos`
- 射数: `30`
- 問い: `convex_body_dynamics`
- 難度仮説: `34`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 交叉体をとる，(2) 主慣性軸方向にSteiner対称化する，(3) 交叉体をとる，(4) 重心体をとる，(5) 原点に関する極体をとる，(6) 差体をとる，(7) 重心体をとる，(8) 差体をとる，(9) 原点に関する極体をとる，(10) 主慣性軸方向にSteiner対称化する，(11) 自身と極体のMinkowski和をとる，(12) 射影体をとる，(13) 原点に関する極体をとる，(14) 重心体をとる，(15) 主慣性軸方向にSteiner対称化する，(16) 重心体をとる，(17) 差体をとる，(18) 自身と極体のMinkowski和をとる，(19) 主慣性軸方向にSteiner対称化する，(20) 原点に関する極体をとる，(21) 重心体をとる，(22) 主慣性軸方向にSteiner対称化する，(23) 原点に関する極体をとる，(24) 射影体をとる，(25) 交叉体をとる，(26) 面積と二次モーメントを固定して正規化する，(27) ここまでの凸体関手を反復する，(28) 支持関数の軌道へ移す，(29) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `IntersectionBody → SteinerSymmetrization → IntersectionBody → CentroidBody → PolarDual → DifferenceBody → CentroidBody → DifferenceBody → PolarDual → SteinerSymmetrization → MinkowskiPolarSum → ProjectionBody → PolarDual → CentroidBody → SteinerSymmetrization → CentroidBody → DifferenceBody → MinkowskiPolarSum → SteinerSymmetrization → PolarDual → CentroidBody → SteinerSymmetrization → PolarDual → ProjectionBody → IntersectionBody → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 多項式変換と算術観測（ReciprocalPolynomial・RootMultiset・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.1f7119ae7b`
- 状態: `unresolved_by_mathos`
- 射数: `29`
- 問い: `recurrence_order_drop`
- 難度仮説: `33`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根を逆数へ移す相反多項式をとる，(2) 重複度付き根配置へ移す，(3) 根配置からモニック多項式を再構成する，(4) 重複度付き根配置へ移す，(5) 根配置からモニック多項式を再構成する，(6) 根を逆数へ移す相反多項式をとる，(7) 根の重心を0へ移す平行移動共役を施す，(8) 臨界値を根にもつ消去多項式を作る，(9) 導関数をモニックに再正規化する，(10) 根を二乗するGraeffe変換を施す，(11) 導関数をモニックに再正規化する，(12) 臨界値を根にもつ消去多項式を作る，(13) 重複度付き根配置へ移す，(14) 根配置からモニック多項式を再構成する，(15) 根の重心を0へ移す平行移動共役を施す，(16) 根を二乗するGraeffe変換を施す，(17) 導関数をモニックに再正規化する，(18) 根を二乗するGraeffe変換を施す，(19) 導関数をモニックに再正規化する，(20) 根を二乗するGraeffe変換を施す，(21) 臨界値を根にもつ消去多項式を作る，(22) 根を逆数へ移す相反多項式をとる，(23) 根の重心を0へ移す平行移動共役を施す，(24) 重複度付き根配置へ移す，(25) 根の冪和モーメント列を作る，(26) モーメントからHankel行列族を作る，(27) 主小行列式列をとる，(28) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ReciprocalPolynomial → RootMultiset → PolynomialReconstruction → RootMultiset → PolynomialReconstruction → ReciprocalPolynomial → ShiftConjugacy → CriticalValuePolynomial → DerivativeRenormalization → GraeffeTransform → DerivativeRenormalization → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → ShiftConjugacy → GraeffeTransform → DerivativeRenormalization → GraeffeTransform → DerivativeRenormalization → GraeffeTransform → CriticalValuePolynomial → ReciprocalPolynomial → ShiftConjugacy → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 平面代数曲線の合成変換（Catacaustic・PolarReciprocal・ProjectiveDual・IsogonalCremona）

- ID: `research.autonomous.plane_curve.774d04600b`
- 状態: `unresolved_by_mathos`
- 射数: `30`
- 問い: `birational_periodicity`
- 難度仮説: `33`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定光源からの反射光線族の包絡線をとる，(2) 固定非退化二次形式に関する極逆像をとる，(3) 法線方向の代数的平行曲線をとる，(4) 正則接線族の射影双対曲線をとる，(5) 法線族の包絡線である発展曲線をとる，(6) 固定光源からの反射光線族の包絡線をとる，(7) 射影閉包をとり無限遠点を加える，(8) 基点を避ける一般アフィンチャートへ移す，(9) 固定光源からの反射光線族の包絡線をとる，(10) 法線族の包絡線である発展曲線をとる，(11) 法線方向の代数的平行曲線をとる，(12) 法線族の包絡線である発展曲線をとる，(13) 固定基準三角形に関する等角共役Cremona像をとる，(14) 原点中心の円反転像をとる，(15) 固定非退化二次形式に関する極逆像をとる，(16) 射影閉包をとり無限遠点を加える，(17) 基点を避ける一般アフィンチャートへ移す，(18) 法線方向の代数的平行曲線をとる，(19) 固定基準三角形に関する等角共役Cremona像をとる，(20) 射影閉包をとり無限遠点を加える，(21) 基点を避ける一般アフィンチャートへ移す，(22) 固定光源からの反射光線族の包絡線をとる，(23) 法線族の包絡線である発展曲線をとる，(24) 法線方向の代数的平行曲線をとる，(25) 射影閉包をとり無限遠点を加える，(26) 基点を避ける一般アフィンチャートへ移す，(27) 固定光源からの反射光線族の包絡線をとる，(28) 正則接線族の射影双対曲線をとる，(29) 固定基準三角形に関する等角共役Cremona像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `Catacaustic → PolarReciprocal → OffsetCurve → ProjectiveDual → Evolute → Catacaustic → ProjectiveClosure → AffineChartChange → Catacaustic → Evolute → OffsetCurve → Evolute → IsogonalCremona → CircleInversion → PolarReciprocal → ProjectiveClosure → AffineChartChange → OffsetCurve → IsogonalCremona → ProjectiveClosure → AffineChartChange → Catacaustic → Evolute → OffsetCurve → ProjectiveClosure → AffineChartChange → Catacaustic → ProjectiveDual → IsogonalCremona → BirationalPeriodQuery`

### 凸体関手の合成力学（MinkowskiPolarSum・CentroidBody・SteinerSymmetrization・VolumeNormalization）

- ID: `research.autonomous.convex_body.1a02a64cc5`
- 状態: `unresolved_by_mathos`
- 射数: `28`
- 問い: `convex_functor_fixed_points`
- 難度仮説: `31`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身と極体のMinkowski和をとる，(2) 重心体をとる，(3) 自身と極体のMinkowski和をとる，(4) 原点に関する極体をとる，(5) 交叉体をとる，(6) 重心体をとる，(7) 原点に関する極体をとる，(8) 射影体をとる，(9) 自身と極体のMinkowski和をとる，(10) 交叉体をとる，(11) 原点に関する極体をとる，(12) 射影体をとる，(13) 交叉体をとる，(14) 主慣性軸方向にSteiner対称化する，(15) 原点に関する極体をとる，(16) 重心体をとる，(17) 差体をとる，(18) 自身と極体のMinkowski和をとる，(19) 交叉体をとる，(20) 差体をとる，(21) 重心体をとる，(22) 射影体をとる，(23) 差体をとる，(24) 射影体をとる，(25) 差体をとる，(26) 主慣性軸方向にSteiner対称化する，(27) 面積と二次モーメントを固定して正規化する。最後に、合成関手の固定体を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `MinkowskiPolarSum → CentroidBody → MinkowskiPolarSum → PolarDual → IntersectionBody → CentroidBody → PolarDual → ProjectionBody → MinkowskiPolarSum → IntersectionBody → PolarDual → ProjectionBody → IntersectionBody → SteinerSymmetrization → PolarDual → CentroidBody → DifferenceBody → MinkowskiPolarSum → IntersectionBody → DifferenceBody → CentroidBody → ProjectionBody → DifferenceBody → ProjectionBody → DifferenceBody → SteinerSymmetrization → VolumeNormalization → ConvexFixedPointQuery`

### 多項式変換と算術観測（ShiftConjugacy・DerivativeRenormalization・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.f02e6b9d22`
- 状態: `unresolved_by_mathos`
- 射数: `29`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `33`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根の重心を0へ移す平行移動共役を施す，(2) 導関数をモニックに再正規化する，(3) 重複度付き根配置へ移す，(4) 根配置からモニック多項式を再構成する，(5) 根を二乗するGraeffe変換を施す，(6) 根を逆数へ移す相反多項式をとる，(7) 根を二乗するGraeffe変換を施す，(8) 重複度付き根配置へ移す，(9) 根配置からモニック多項式を再構成する，(10) 根の重心を0へ移す平行移動共役を施す，(11) 根を二乗するGraeffe変換を施す，(12) 重複度付き根配置へ移す，(13) 根配置からモニック多項式を再構成する，(14) 根の重心を0へ移す平行移動共役を施す，(15) 導関数をモニックに再正規化する，(16) 根を逆数へ移す相反多項式をとる，(17) 臨界値を根にもつ消去多項式を作る，(18) 根の重心を0へ移す平行移動共役を施す，(19) 臨界値を根にもつ消去多項式を作る，(20) 導関数をモニックに再正規化する，(21) 根を二乗するGraeffe変換を施す，(22) 臨界値を根にもつ消去多項式を作る，(23) 重複度付き根配置へ移す，(24) 根の冪和モーメント列を作る，(25) モーメントからHankel行列族を作る，(26) 主小行列式列をとる，(27) 満たす最小線形漸化式を抽出する，(28) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ShiftConjugacy → DerivativeRenormalization → RootMultiset → PolynomialReconstruction → GraeffeTransform → ReciprocalPolynomial → GraeffeTransform → RootMultiset → PolynomialReconstruction → ShiftConjugacy → GraeffeTransform → RootMultiset → PolynomialReconstruction → ShiftConjugacy → DerivativeRenormalization → ReciprocalPolynomial → CriticalValuePolynomial → ShiftConjugacy → CriticalValuePolynomial → DerivativeRenormalization → GraeffeTransform → CriticalValuePolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 凸体関手の合成力学（SteinerSymmetrization・CentroidBody・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.ea6e67a7e0`
- 状態: `unresolved_by_mathos`
- 射数: `30`
- 問い: `convex_body_dynamics`
- 難度仮説: `34`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 主慣性軸方向にSteiner対称化する，(2) 重心体をとる，(3) 自身と極体のMinkowski和をとる，(4) 主慣性軸方向にSteiner対称化する，(5) 射影体をとる，(6) 差体をとる，(7) 交叉体をとる，(8) 自身と極体のMinkowski和をとる，(9) 原点に関する極体をとる，(10) 重心体をとる，(11) 主慣性軸方向にSteiner対称化する，(12) 自身と極体のMinkowski和をとる，(13) 差体をとる，(14) 射影体をとる，(15) 原点に関する極体をとる，(16) 重心体をとる，(17) 主慣性軸方向にSteiner対称化する，(18) 原点に関する極体をとる，(19) 主慣性軸方向にSteiner対称化する，(20) 自身と極体のMinkowski和をとる，(21) 重心体をとる，(22) 射影体をとる，(23) 差体をとる，(24) 原点に関する極体をとる，(25) 重心体をとる，(26) 面積と二次モーメントを固定して正規化する，(27) ここまでの凸体関手を反復する，(28) 支持関数の軌道へ移す，(29) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `SteinerSymmetrization → CentroidBody → MinkowskiPolarSum → SteinerSymmetrization → ProjectionBody → DifferenceBody → IntersectionBody → MinkowskiPolarSum → PolarDual → CentroidBody → SteinerSymmetrization → MinkowskiPolarSum → DifferenceBody → ProjectionBody → PolarDual → CentroidBody → SteinerSymmetrization → PolarDual → SteinerSymmetrization → MinkowskiPolarSum → CentroidBody → ProjectionBody → DifferenceBody → PolarDual → CentroidBody → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 平面代数曲線の合成変換（CircleInversion・Catacaustic・OffsetCurve・HessianCurve）

- ID: `research.autonomous.plane_curve.a71ab54d1f`
- 状態: `unresolved_by_mathos`
- 射数: `29`
- 問い: `birational_periodicity`
- 難度仮説: `32`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 原点中心の円反転像をとる，(2) 固定光源からの反射光線族の包絡線をとる，(3) 射影閉包をとり無限遠点を加える，(4) 基点を避ける一般アフィンチャートへ移す，(5) 固定基準三角形に関する等角共役Cremona像をとる，(6) 正則接線族の射影双対曲線をとる，(7) 固定光源からの反射光線族の包絡線をとる，(8) 固定基準三角形に関する等角共役Cremona像をとる，(9) 法線族の包絡線である発展曲線をとる，(10) 正則接線族の射影双対曲線をとる，(11) 定義多項式のHessian曲線をとる，(12) 正則接線族の射影双対曲線をとる，(13) 定義多項式のHessian曲線をとる，(14) 射影閉包をとり無限遠点を加える，(15) 基点を避ける一般アフィンチャートへ移す，(16) 射影閉包をとり無限遠点を加える，(17) 基点を避ける一般アフィンチャートへ移す，(18) 法線方向の代数的平行曲線をとる，(19) 固定基準三角形に関する等角共役Cremona像をとる，(20) 原点中心の円反転像をとる，(21) 定義多項式のHessian曲線をとる，(22) 射影閉包をとり無限遠点を加える，(23) 基点を避ける一般アフィンチャートへ移す，(24) 法線族の包絡線である発展曲線をとる，(25) 固定非退化二次形式に関する極逆像をとる，(26) 固定基準三角形に関する等角共役Cremona像をとる，(27) 法線方向の代数的平行曲線をとる，(28) 定義多項式のHessian曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `CircleInversion → Catacaustic → ProjectiveClosure → AffineChartChange → IsogonalCremona → ProjectiveDual → Catacaustic → IsogonalCremona → Evolute → ProjectiveDual → HessianCurve → ProjectiveDual → HessianCurve → ProjectiveClosure → AffineChartChange → ProjectiveClosure → AffineChartChange → OffsetCurve → IsogonalCremona → CircleInversion → HessianCurve → ProjectiveClosure → AffineChartChange → Evolute → PolarReciprocal → IsogonalCremona → OffsetCurve → HessianCurve → BirationalPeriodQuery`

### 多項式変換と算術観測（ShiftConjugacy・RootMultiset・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.600da85dfc`
- 状態: `unresolved_by_mathos`
- 射数: `30`
- 問い: `recurrence_order_drop`
- 難度仮説: `34`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根の重心を0へ移す平行移動共役を施す，(2) 重複度付き根配置へ移す，(3) 根配置からモニック多項式を再構成する，(4) 重複度付き根配置へ移す，(5) 根配置からモニック多項式を再構成する，(6) 根を二乗するGraeffe変換を施す，(7) 臨界値を根にもつ消去多項式を作る，(8) 根を二乗するGraeffe変換を施す，(9) 根を逆数へ移す相反多項式をとる，(10) 導関数をモニックに再正規化する，(11) 重複度付き根配置へ移す，(12) 根配置からモニック多項式を再構成する，(13) 臨界値を根にもつ消去多項式を作る，(14) 根を逆数へ移す相反多項式をとる，(15) 臨界値を根にもつ消去多項式を作る，(16) 根の重心を0へ移す平行移動共役を施す，(17) 導関数をモニックに再正規化する，(18) 重複度付き根配置へ移す，(19) 根配置からモニック多項式を再構成する，(20) 導関数をモニックに再正規化する，(21) 臨界値を根にもつ消去多項式を作る，(22) 根を逆数へ移す相反多項式をとる，(23) 根の重心を0へ移す平行移動共役を施す，(24) 導関数をモニックに再正規化する，(25) 重複度付き根配置へ移す，(26) 根の冪和モーメント列を作る，(27) モーメントからHankel行列族を作る，(28) 主小行列式列をとる，(29) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ShiftConjugacy → RootMultiset → PolynomialReconstruction → RootMultiset → PolynomialReconstruction → GraeffeTransform → CriticalValuePolynomial → GraeffeTransform → ReciprocalPolynomial → DerivativeRenormalization → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → ReciprocalPolynomial → CriticalValuePolynomial → ShiftConjugacy → DerivativeRenormalization → RootMultiset → PolynomialReconstruction → DerivativeRenormalization → CriticalValuePolynomial → ReciprocalPolynomial → ShiftConjugacy → DerivativeRenormalization → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 平面代数曲線の合成変換（Catacaustic・ProjectiveClosure・AffineChartChange・IsogonalCremona）

- ID: `research.autonomous.plane_curve.1bcca40754`
- 状態: `unresolved_by_mathos`
- 射数: `30`
- 問い: `birational_periodicity`
- 難度仮説: `33`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 固定光源からの反射光線族の包絡線をとる，(2) 射影閉包をとり無限遠点を加える，(3) 基点を避ける一般アフィンチャートへ移す，(4) 正則接線族の射影双対曲線をとる，(5) 法線方向の代数的平行曲線をとる，(6) 射影閉包をとり無限遠点を加える，(7) 基点を避ける一般アフィンチャートへ移す，(8) 固定非退化二次形式に関する極逆像をとる，(9) 正則接線族の射影双対曲線をとる，(10) 法線族の包絡線である発展曲線をとる，(11) 正則接線族の射影双対曲線をとる，(12) 定義多項式のHessian曲線をとる，(13) 原点中心の円反転像をとる，(14) 固定非退化二次形式に関する極逆像をとる，(15) 法線族の包絡線である発展曲線をとる，(16) 法線方向の代数的平行曲線をとる，(17) 射影閉包をとり無限遠点を加える，(18) 基点を避ける一般アフィンチャートへ移す，(19) 法線族の包絡線である発展曲線をとる，(20) 法線方向の代数的平行曲線をとる，(21) 射影閉包をとり無限遠点を加える，(22) 基点を避ける一般アフィンチャートへ移す，(23) 法線族の包絡線である発展曲線をとる，(24) 固定光源からの反射光線族の包絡線をとる，(25) 原点中心の円反転像をとる，(26) 固定基準三角形に関する等角共役Cremona像をとる，(27) 射影閉包をとり無限遠点を加える，(28) 基点を避ける一般アフィンチャートへ移す，(29) 固定基準三角形に関する等角共役Cremona像をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `Catacaustic → ProjectiveClosure → AffineChartChange → ProjectiveDual → OffsetCurve → ProjectiveClosure → AffineChartChange → PolarReciprocal → ProjectiveDual → Evolute → ProjectiveDual → HessianCurve → CircleInversion → PolarReciprocal → Evolute → OffsetCurve → ProjectiveClosure → AffineChartChange → Evolute → OffsetCurve → ProjectiveClosure → AffineChartChange → Evolute → Catacaustic → CircleInversion → IsogonalCremona → ProjectiveClosure → AffineChartChange → IsogonalCremona → BirationalPeriodQuery`

### 凸体関手の合成力学（PolarDual・ProjectionBody・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.4de3b5481a`
- 状態: `unresolved_by_mathos`
- 射数: `30`
- 問い: `convex_body_dynamics`
- 難度仮説: `34`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 原点に関する極体をとる，(2) 射影体をとる，(3) 重心体をとる，(4) 自身と極体のMinkowski和をとる，(5) 射影体をとる，(6) 差体をとる，(7) 射影体をとる，(8) 重心体をとる，(9) 自身と極体のMinkowski和をとる，(10) 重心体をとる，(11) 主慣性軸方向にSteiner対称化する，(12) 交叉体をとる，(13) 重心体をとる，(14) 原点に関する極体をとる，(15) 交叉体をとる，(16) 主慣性軸方向にSteiner対称化する，(17) 原点に関する極体をとる，(18) 差体をとる，(19) 射影体をとる，(20) 自身と極体のMinkowski和をとる，(21) 交叉体をとる，(22) 重心体をとる，(23) 自身と極体のMinkowski和をとる，(24) 差体をとる，(25) 射影体をとる，(26) 面積と二次モーメントを固定して正規化する，(27) ここまでの凸体関手を反復する，(28) 支持関数の軌道へ移す，(29) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `PolarDual → ProjectionBody → CentroidBody → MinkowskiPolarSum → ProjectionBody → DifferenceBody → ProjectionBody → CentroidBody → MinkowskiPolarSum → CentroidBody → SteinerSymmetrization → IntersectionBody → CentroidBody → PolarDual → IntersectionBody → SteinerSymmetrization → PolarDual → DifferenceBody → ProjectionBody → MinkowskiPolarSum → IntersectionBody → CentroidBody → MinkowskiPolarSum → DifferenceBody → ProjectionBody → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 多項式変換と算術観測（ShiftConjugacy・CriticalValuePolynomial・RecurrenceExtraction・ModularOrbit）

- ID: `research.autonomous.polynomial.44b9608263`
- 状態: `unresolved_by_mathos`
- 射数: `30`
- 問い: `polynomial_arithmetic_dynamics`
- 難度仮説: `34`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 根の重心を0へ移す平行移動共役を施す，(2) 臨界値を根にもつ消去多項式を作る，(3) 根を逆数へ移す相反多項式をとる，(4) 臨界値を根にもつ消去多項式を作る，(5) 重複度付き根配置へ移す，(6) 根配置からモニック多項式を再構成する，(7) 臨界値を根にもつ消去多項式を作る，(8) 根の重心を0へ移す平行移動共役を施す，(9) 根を二乗するGraeffe変換を施す，(10) 導関数をモニックに再正規化する，(11) 重複度付き根配置へ移す，(12) 根配置からモニック多項式を再構成する，(13) 根を逆数へ移す相反多項式をとる，(14) 根の重心を0へ移す平行移動共役を施す，(15) 臨界値を根にもつ消去多項式を作る，(16) 重複度付き根配置へ移す，(17) 根配置からモニック多項式を再構成する，(18) 根の重心を0へ移す平行移動共役を施す，(19) 根を逆数へ移す相反多項式をとる，(20) 臨界値を根にもつ消去多項式を作る，(21) 根の重心を0へ移す平行移動共役を施す，(22) 導関数をモニックに再正規化する，(23) 根を二乗するGraeffe変換を施す，(24) 重複度付き根配置へ移す，(25) 根の冪和モーメント列を作る，(26) モーメントからHankel行列族を作る，(27) 主小行列式列をとる，(28) 満たす最小線形漸化式を抽出する，(29) 各素数法での周期と例外素数を抽出する。最後に、周期が有界または特異となる初期多項式を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `ShiftConjugacy → CriticalValuePolynomial → ReciprocalPolynomial → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → ShiftConjugacy → GraeffeTransform → DerivativeRenormalization → RootMultiset → PolynomialReconstruction → ReciprocalPolynomial → ShiftConjugacy → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → ShiftConjugacy → ReciprocalPolynomial → CriticalValuePolynomial → ShiftConjugacy → DerivativeRenormalization → GraeffeTransform → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → ModularOrbit → PolynomialArithmeticQuery`

### 平面代数曲線の合成変換（HessianCurve・PolarReciprocal・OffsetCurve・Evolute）

- ID: `research.autonomous.plane_curve.76c61854a4`
- 状態: `unresolved_by_mathos`
- 射数: `30`
- 問い: `birational_periodicity`
- 難度仮説: `33`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 定義多項式のHessian曲線をとる，(2) 固定非退化二次形式に関する極逆像をとる，(3) 射影閉包をとり無限遠点を加える，(4) 基点を避ける一般アフィンチャートへ移す，(5) 法線方向の代数的平行曲線をとる，(6) 原点中心の円反転像をとる，(7) 定義多項式のHessian曲線をとる，(8) 正則接線族の射影双対曲線をとる，(9) 固定光源からの反射光線族の包絡線をとる，(10) 正則接線族の射影双対曲線をとる，(11) 法線方向の代数的平行曲線をとる，(12) 固定非退化二次形式に関する極逆像をとる，(13) 固定光源からの反射光線族の包絡線をとる，(14) 射影閉包をとり無限遠点を加える，(15) 基点を避ける一般アフィンチャートへ移す，(16) 射影閉包をとり無限遠点を加える，(17) 基点を避ける一般アフィンチャートへ移す，(18) 正則接線族の射影双対曲線をとる，(19) 射影閉包をとり無限遠点を加える，(20) 基点を避ける一般アフィンチャートへ移す，(21) 固定非退化二次形式に関する極逆像をとる，(22) 射影閉包をとり無限遠点を加える，(23) 基点を避ける一般アフィンチャートへ移す，(24) 正則接線族の射影双対曲線をとる，(25) 固定光源からの反射光線族の包絡線をとる，(26) 固定基準三角形に関する等角共役Cremona像をとる，(27) 固定光源からの反射光線族の包絡線をとる，(28) 法線方向の代数的平行曲線をとる，(29) 法線族の包絡線である発展曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `HessianCurve → PolarReciprocal → ProjectiveClosure → AffineChartChange → OffsetCurve → CircleInversion → HessianCurve → ProjectiveDual → Catacaustic → ProjectiveDual → OffsetCurve → PolarReciprocal → Catacaustic → ProjectiveClosure → AffineChartChange → ProjectiveClosure → AffineChartChange → ProjectiveDual → ProjectiveClosure → AffineChartChange → PolarReciprocal → ProjectiveClosure → AffineChartChange → ProjectiveDual → Catacaustic → IsogonalCremona → Catacaustic → OffsetCurve → Evolute → BirationalPeriodQuery`

### 凸体関手の合成力学（MinkowskiPolarSum・ProjectionBody・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.142ee900fc`
- 状態: `unresolved_by_mathos`
- 射数: `30`
- 問い: `convex_body_dynamics`
- 難度仮説: `34`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 自身と極体のMinkowski和をとる，(2) 射影体をとる，(3) 交叉体をとる，(4) 自身と極体のMinkowski和をとる，(5) 重心体をとる，(6) 自身と極体のMinkowski和をとる，(7) 重心体をとる，(8) 主慣性軸方向にSteiner対称化する，(9) 交叉体をとる，(10) 重心体をとる，(11) 原点に関する極体をとる，(12) 差体をとる，(13) 交叉体をとる，(14) 主慣性軸方向にSteiner対称化する，(15) 自身と極体のMinkowski和をとる，(16) 主慣性軸方向にSteiner対称化する，(17) 重心体をとる，(18) 主慣性軸方向にSteiner対称化する，(19) 差体をとる，(20) 原点に関する極体をとる，(21) 自身と極体のMinkowski和をとる，(22) 原点に関する極体をとる，(23) 主慣性軸方向にSteiner対称化する，(24) 射影体をとる，(25) 重心体をとる，(26) 面積と二次モーメントを固定して正規化する，(27) ここまでの凸体関手を反復する，(28) 支持関数の軌道へ移す，(29) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `MinkowskiPolarSum → ProjectionBody → IntersectionBody → MinkowskiPolarSum → CentroidBody → MinkowskiPolarSum → CentroidBody → SteinerSymmetrization → IntersectionBody → CentroidBody → PolarDual → DifferenceBody → IntersectionBody → SteinerSymmetrization → MinkowskiPolarSum → SteinerSymmetrization → CentroidBody → SteinerSymmetrization → DifferenceBody → PolarDual → MinkowskiPolarSum → PolarDual → SteinerSymmetrization → ProjectionBody → CentroidBody → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 多項式変換と算術観測（DerivativeRenormalization・GraeffeTransform・MinorSequence・RecurrenceExtraction）

- ID: `research.autonomous.polynomial.e341422932`
- 状態: `unresolved_by_mathos`
- 射数: `29`
- 問い: `recurrence_order_drop`
- 難度仮説: `33`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0938`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「重根を持たないモニック実多項式を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 導関数をモニックに再正規化する，(2) 根を二乗するGraeffe変換を施す，(3) 導関数をモニックに再正規化する，(4) 臨界値を根にもつ消去多項式を作る，(5) 根を二乗するGraeffe変換を施す，(6) 導関数をモニックに再正規化する，(7) 根の重心を0へ移す平行移動共役を施す，(8) 根を逆数へ移す相反多項式をとる，(9) 臨界値を根にもつ消去多項式を作る，(10) 重複度付き根配置へ移す，(11) 根配置からモニック多項式を再構成する，(12) 臨界値を根にもつ消去多項式を作る，(13) 根を二乗するGraeffe変換を施す，(14) 根の重心を0へ移す平行移動共役を施す，(15) 重複度付き根配置へ移す，(16) 根配置からモニック多項式を再構成する，(17) 根の重心を0へ移す平行移動共役を施す，(18) 根を逆数へ移す相反多項式をとる，(19) 根の重心を0へ移す平行移動共役を施す，(20) 根を逆数へ移す相反多項式をとる，(21) 導関数をモニックに再正規化する，(22) 根を二乗するGraeffe変換を施す，(23) 臨界値を根にもつ消去多項式を作る，(24) 重複度付き根配置へ移す，(25) 根の冪和モーメント列を作る，(26) モーメントからHankel行列族を作る，(27) 主小行列式列をとる，(28) 満たす最小線形漸化式を抽出する。最後に、漸化式の最小次数が低下する係数条件を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `DerivativeRenormalization → GraeffeTransform → DerivativeRenormalization → CriticalValuePolynomial → GraeffeTransform → DerivativeRenormalization → ShiftConjugacy → ReciprocalPolynomial → CriticalValuePolynomial → RootMultiset → PolynomialReconstruction → CriticalValuePolynomial → GraeffeTransform → ShiftConjugacy → RootMultiset → PolynomialReconstruction → ShiftConjugacy → ReciprocalPolynomial → ShiftConjugacy → ReciprocalPolynomial → DerivativeRenormalization → GraeffeTransform → CriticalValuePolynomial → RootMultiset → PowerMomentSequence → HankelConstruction → MinorSequence → RecurrenceExtraction → RecurrenceOrderQuery`

### 凸体関手の合成力学（SteinerSymmetrization・IntersectionBody・SupportFunctionChart・StabilityLinearization）

- ID: `research.autonomous.convex_body.f4f359996a`
- 状態: `unresolved_by_mathos`
- 射数: `31`
- 問い: `convex_body_dynamics`
- 難度仮説: `35`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「原点対称で滑らかな厳密凸代数的凸体を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 主慣性軸方向にSteiner対称化する，(2) 交叉体をとる，(3) 原点に関する極体をとる，(4) 自身と極体のMinkowski和をとる，(5) 主慣性軸方向にSteiner対称化する，(6) 原点に関する極体をとる，(7) 差体をとる，(8) 重心体をとる，(9) 差体をとる，(10) 原点に関する極体をとる，(11) 差体をとる，(12) 自身と極体のMinkowski和をとる，(13) 差体をとる，(14) 原点に関する極体をとる，(15) 射影体をとる，(16) 交叉体をとる，(17) 重心体をとる，(18) 原点に関する極体をとる，(19) 交叉体をとる，(20) 自身と極体のMinkowski和をとる，(21) 交叉体をとる，(22) 射影体をとる，(23) 主慣性軸方向にSteiner対称化する，(24) 交叉体をとる，(25) 重心体をとる，(26) 射影体をとる，(27) 面積と二次モーメントを固定して正規化する，(28) ここまでの凸体関手を反復する，(29) 支持関数の軌道へ移す，(30) 固定点の周りで線形化しスペクトルを求める。最後に、固定体、周期軌道、局所安定性を線形同値を除いて分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `SteinerSymmetrization → IntersectionBody → PolarDual → MinkowskiPolarSum → SteinerSymmetrization → PolarDual → DifferenceBody → CentroidBody → DifferenceBody → PolarDual → DifferenceBody → MinkowskiPolarSum → DifferenceBody → PolarDual → ProjectionBody → IntersectionBody → CentroidBody → PolarDual → IntersectionBody → MinkowskiPolarSum → IntersectionBody → ProjectionBody → SteinerSymmetrization → IntersectionBody → CentroidBody → ProjectionBody → VolumeNormalization → BodyIteration → SupportFunctionChart → StabilityLinearization → ConvexDynamicsQuery`

### 平面代数曲線の合成変換（Evolute・Catacaustic・Catacaustic・OffsetCurve）

- ID: `research.autonomous.plane_curve.d30611f685`
- 状態: `unresolved_by_mathos`
- 射数: `30`
- 問い: `birational_periodicity`
- 難度仮説: `33`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 法線族の包絡線である発展曲線をとる，(2) 固定光源からの反射光線族の包絡線をとる，(3) 射影閉包をとり無限遠点を加える，(4) 基点を避ける一般アフィンチャートへ移す，(5) 定義多項式のHessian曲線をとる，(6) 射影閉包をとり無限遠点を加える，(7) 基点を避ける一般アフィンチャートへ移す，(8) 定義多項式のHessian曲線をとる，(9) 法線族の包絡線である発展曲線をとる，(10) 射影閉包をとり無限遠点を加える，(11) 基点を避ける一般アフィンチャートへ移す，(12) 固定光源からの反射光線族の包絡線をとる，(13) 固定非退化二次形式に関する極逆像をとる，(14) 定義多項式のHessian曲線をとる，(15) 法線方向の代数的平行曲線をとる，(16) 法線族の包絡線である発展曲線をとる，(17) 固定非退化二次形式に関する極逆像をとる，(18) 固定基準三角形に関する等角共役Cremona像をとる，(19) 固定光源からの反射光線族の包絡線をとる，(20) 法線方向の代数的平行曲線をとる，(21) 固定非退化二次形式に関する極逆像をとる，(22) 法線方向の代数的平行曲線をとる，(23) 定義多項式のHessian曲線をとる，(24) 固定非退化二次形式に関する極逆像をとる，(25) 正則接線族の射影双対曲線をとる，(26) 射影閉包をとり無限遠点を加える，(27) 基点を避ける一般アフィンチャートへ移す，(28) 固定光源からの反射光線族の包絡線をとる，(29) 法線方向の代数的平行曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `Evolute → Catacaustic → ProjectiveClosure → AffineChartChange → HessianCurve → ProjectiveClosure → AffineChartChange → HessianCurve → Evolute → ProjectiveClosure → AffineChartChange → Catacaustic → PolarReciprocal → HessianCurve → OffsetCurve → Evolute → PolarReciprocal → IsogonalCremona → Catacaustic → OffsetCurve → PolarReciprocal → OffsetCurve → HessianCurve → PolarReciprocal → ProjectiveDual → ProjectiveClosure → AffineChartChange → Catacaustic → OffsetCurve → BirationalPeriodQuery`

### 平面代数曲線の合成変換（Evolute・HessianCurve・PolarReciprocal・HessianCurve）

- ID: `research.autonomous.plane_curve.0b751a2586`
- 状態: `unresolved_by_mathos`
- 射数: `31`
- 問い: `birational_periodicity`
- 難度仮説: `34`
- 生成元: `autonomous_atlas_search`
- 既知問題との表層衝突: `検出なし`
- 表層照合コーパス: `28074問`
- 最大表層Jaccard: `0.0781`
- 照合方式: `minhash64_conservative`

\(\mathcal X_0\) を「特異点を持たない既約実代数平面曲線を初期対象とする」で定める。各構成が定義される非退化な範囲で，\(\mathcal X_i\) に次の型付き構成を順に施す：(1) 法線族の包絡線である発展曲線をとる，(2) 定義多項式のHessian曲線をとる，(3) 射影閉包をとり無限遠点を加える，(4) 基点を避ける一般アフィンチャートへ移す，(5) 法線方向の代数的平行曲線をとる，(6) 法線族の包絡線である発展曲線をとる，(7) 固定基準三角形に関する等角共役Cremona像をとる，(8) 法線方向の代数的平行曲線をとる，(9) 射影閉包をとり無限遠点を加える，(10) 基点を避ける一般アフィンチャートへ移す，(11) 固定非退化二次形式に関する極逆像をとる，(12) 正則接線族の射影双対曲線をとる，(13) 原点中心の円反転像をとる，(14) 法線族の包絡線である発展曲線をとる，(15) 原点中心の円反転像をとる，(16) 固定光源からの反射光線族の包絡線をとる，(17) 固定基準三角形に関する等角共役Cremona像をとる，(18) 固定光源からの反射光線族の包絡線をとる，(19) 射影閉包をとり無限遠点を加える，(20) 基点を避ける一般アフィンチャートへ移す，(21) 定義多項式のHessian曲線をとる，(22) 固定非退化二次形式に関する極逆像をとる，(23) 固定光源からの反射光線族の包絡線をとる，(24) 法線方向の代数的平行曲線をとる，(25) 固定非退化二次形式に関する極逆像をとる，(26) 正則接線族の射影双対曲線をとる，(27) 固定基準三角形に関する等角共役Cremona像をとる，(28) 原点中心の円反転像をとる，(29) 固定非退化二次形式に関する極逆像をとる，(30) 定義多項式のHessian曲線をとる。最後に、合成変換で元の曲線と双有理同値になる初期曲線を分類せよ。分類では途中で生じる退化成分と例外パラメータも明示せよ。

射列: `Evolute → HessianCurve → ProjectiveClosure → AffineChartChange → OffsetCurve → Evolute → IsogonalCremona → OffsetCurve → ProjectiveClosure → AffineChartChange → PolarReciprocal → ProjectiveDual → CircleInversion → Evolute → CircleInversion → Catacaustic → IsogonalCremona → Catacaustic → ProjectiveClosure → AffineChartChange → HessianCurve → PolarReciprocal → Catacaustic → OffsetCurve → PolarReciprocal → ProjectiveDual → IsogonalCremona → CircleInversion → PolarReciprocal → HessianCurve → BirationalPeriodQuery`

## 注意

- 有名問題スクリーニングは局所マーカーと既存コーパス照合の入口であり、
  文献調査や研究上の新規性証明の代わりではない。
- 保留候補は公開前に専門家レビュー、文献検索、より長い反例探索を行う。
- 解けなかったこと自体を難しさや新規性の証拠にはしない。
