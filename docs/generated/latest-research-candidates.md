# MathOS 研究候補・保留キュー

> `unresolved_by_mathos` は人類未解決という意味ではない。
> 現在のMathOSが証明も反例も得られなかった状態を表す。

## 集計

- 保留候補: **115件**
- 異なる型付き射列: **115件**
- 問いの型: **23種類**
- 数値替え: **0件**
- 各候補の照合母数: **28074問以上**
- atlas自律探索候補: **103件**
- 今回の自律追加: **12件**
- 現在の探索深さ下限: **14射**

## 自律探索

- 世代: `9`
- 射アトラス: `92射`
- チャート: `6領域`
- 探索試行: `27`
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

## 注意

- 有名問題スクリーニングは局所マーカーと既存コーパス照合の入口であり、
  文献調査や研究上の新規性証明の代わりではない。
- 保留候補は公開前に専門家レビュー、文献検索、より長い反例探索を行う。
- 解けなかったこと自体を難しさや新規性の証拠にはしない。
