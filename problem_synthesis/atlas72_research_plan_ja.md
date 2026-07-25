# MathOS Atlas72 作問研究企画書

作成日: 2026-07-23

## 1. 目的

MathOSの作問能力を、問題文や解法文型の記憶ではなく、型付き数学対象と射の
合成から評価する。今回の主眼は、相関係数とスカラー最小値を個別問題型として
扱う設計を廃止し、内積空間、二次形式、射影、正規化という共通核へ移すことで
ある。

生成候補は次の二条件を同時に満たした場合だけ採用する。

1. CAS・有限探索・行列計算などのbackendが厳密な答えを返し、検証義務を満たす。
2. 生成された日本語TeXを通常の意味解析器へ戻したとき、期待した
   `LiftCertificate.family_id` が再現される。

## 2. 旧12構造署名の具体名

2026-07-23のAtlas54で数えていた12構造署名は、次の生成チャートに対応する。

| 番号 | chart_id | 日本語名 | 主な数学操作 |
| ---: | --- | --- | --- |
| 1 | `ellipse_area` | 楕円領域の面積 | 座標変換・対称性・積分 |
| 2 | `parabolic_segment_area` | 放物線分割領域の面積 | 縦断面・多項式積分 |
| 3 | `rectangle_perimeter_area_maximum` | 周長固定長方形の面積最大 | 制約代入・停留点・境界 |
| 4 | `rectangle_diagonal_area_maximum` | 対角線固定長方形の面積最大 | 対称式・等号条件 |
| 5 | `scalar_quadratic_minimum` | 平方完成型スカラー最小値 | 平方完成・二階微分 |
| 6 | `rational_sequence_limit` | 有理式数列の極限 | 最高次正規化 |
| 7 | `exponential_sequence_limit` | 指数型数列の極限 | 対数化・指数復元 |
| 8 | `circle_area_limit` | 円面積列の極限 | 測度構成・極限 |
| 9 | `independent_noise_correlation_limit` | 独立雑音付き相関係数の極限 | 共分散・分散・正規化 |
| 10 | `ellipsoid_volume` | 楕円体の体積 | Jacobian・三重積分 |
| 11 | `parabolic_revolution_volume` | 放物線回転体の体積 | 円板法・積分 |
| 12 | `prime_sum_constraint` | 素数和制約の全解探索 | 有界化・素数証明・完全探索 |

このうち5と9は、数学的familyよりも提示文型が狭かった。特に5は
`(x-h)^2+c` を直接提示しており、一般の二次最適化とは言いにくかった。

## 3. 一般化した数学核

### 3.1 内積空間

基本対象を内積空間 `(V, <.,.>)` とし、次の射を共通語彙とする。

```text
Center        : L2(P) -> L2_0(P)
InnerProduct  : V x V -> R
Norm          : V -> R_{\ge 0}
Normalize     : V \ {0} -> UnitSphere(V)
Projection    : V x Subspace(V) -> V
QuadraticForm : SelfAdjoint(V) x V -> R
```

相関係数は独立した原始操作ではなく、

```text
Corr(X,Y)
= <Center(X), Center(Y)>_{L2(P)}
  / (||Center(X)|| ||Center(Y)||)
```

とする。したがって、確率変数の相関、ベクトルのcosine similarity、
関数の正規化相関、行列のFrobenius角は同じ `NormalizedInnerProduct` の
異なるチャートになる。

### 3.2 Frobenius内積

行列空間では

```text
<A,B>_F = tr(A^T B) = sum_ij A_ij B_ij
```

を使う。backendはtrace表示と成分表示の一致を検証する。これは行列専用の
解法暗記ではなく、有限次元内積空間の具体化である。

### 3.3 正定値二次形式

旧スカラー最小値を

```text
f(x) = x^T Q x + l^T x + c,  Q > 0
```

へ置換した。backendは主座小行列式による正定値性、線形停留条件
`2Qx+l=0`、大域的下界を別々に検証する。変数次元、基底、係数表示が変わっても
同じ射の合成を使える。

### 3.4 射影と最小二乗

直交射影はGram方程式を解き、残差が部分空間に直交することを検証する。
最小二乗問題は後に

```text
argmin_x ||Ax-b||^2 = Projection(b, Image(A))
```

として同じfamilyへ接続できる。

### 3.5 相関関数

弱定常過程の相関関数を、lagで添字付けされた正規化内積として扱う。
AR(1)チャートではYule-Walker方程式をbackend契約とし、
単なる「相関係数の公式当てはめ」と区別する。

## 4. 拡張後17構造署名

旧12のうち次を置換した。

- `scalar_quadratic_minimum`
  -> `positive_definite_quadratic_minimum`
- `independent_noise_correlation_limit`
  -> `centered_l2_correlation_limit`

さらに次の5構造を追加した。

| chart_id | 日本語名 | Lift family |
| --- | --- | --- |
| `frobenius_matrix_pairing` | Frobenius行列内積 | `linear_algebra.frobenius_pairing` |
| `orthogonal_projection` | Gram方程式による直交射影 | `linear_algebra.orthogonal_projection` |
| `norm_constrained_inner_product_extremum` | ノルム制約下の内積最大 | `optimization.inner_product_extremum` |
| `normalized_inner_product_limit` | 正規化内積の極限 | `real_analysis.normalized_inner_product_limit` |
| `stationary_ar1_autocorrelation` | 定常AR(1)過程の自己相関 | `probability.autocorrelation_function` |

## 5. 定量結果

| 指標 | Atlas54 | Atlas72 |
| --- | ---: | ---: |
| 生成問題 | 54 | 72 |
| backend検証通過 | 54 | 72 |
| 再lift検証通過 | 54 | 72 |
| 構造署名 | 12 | 17 |
| Lift family | 8 | 13 |
| 異なる解答正規形 | 48 | 60 |
| 固定人間54問との盲検ペア | 31 | 30 |

盲検ペアが1組減ったのは失敗ではない。旧スカラー最小値を、より厳密な
正定値二次形式familyへ移したため、人間側の単純スカラー最小値と同一構造だと
見なさなくなったからである。

新しい内積系6 familyには固定人間集合内の対応問題がない。そのため、72問の
成立率と30組の人間比較を混同しない。

## 6. 創造性の操作的定義

創造性を単一の主観点として定義しない。まず次のベクトルとして測る。

### 6.1 妥当性 `V`

問題が成立し、答えと解法義務が検証されているか。これは0/1のゲートであり、
妥当でない問題には創造性総合評価を与えない。

### 6.2 構造的新規性 `N_s`

`family_id + morphism_chain + constraint_skeleton + query_signature` の距離を、
凍結した人間問題集合と比較する。数値変更、変数名変更、言い換えは新規構造に
数えない。

### 6.3 構成的新規性 `N_c`

既知の射を新しい順序または新しい可換図式で合成しているかを測る。
新しい単語の追加ではなく、証明可能な射の合成差を見る。

### 6.4 条件必然性 `C`

各条件を一つずつ除去・緩和し、次を確認する。

- 解が一意でなくなる
- 問題が自明化する
- 閉形式を失う
- 難易度相が変わる

どの条件を除いても何も変わらない問題は、人工的で冗長と評価する。

### 6.5 解法深度 `D`

必要な非自明射の数、分岐数、補題数、異なるbackend間の受け渡し数で測る。
単なる式の長さや計算量とは分離する。

### 6.6 人間評価 `H`

盲検で次の4軸を1--5点評価する。

- 驚き: 解答前の予想と解法後の構造理解に有意な差があるか
- 美しさ: 条件、結論、解法が少数の原理で統一されるか
- 教育価値: 解後に再利用可能な概念が残るか
- 作問意図: 条件が偶然の数合わせではなく、明確な現象を作っているか

研究上は

```text
CreativityVector = (V, N_s, N_c, C, D, H)
```

を主結果とする。単一値が必要な場合も、重みを事前登録し、`V=0` なら0とする。

## 7. 自然さの操作的定義

自然さは「人間らしい文章」だけではない。次の5軸に分ける。

1. 言語自然性: 日本語とTeXが読みやすく、照応と助詞が一意である。
2. 数学自然性: 対象、量化、定義域、退化条件が慣用的に提示される。
3. 認知自然性: 条件を保持しながら問題の目的を把握できる。
4. 意図自然性: 各条件が結論または解法上の役割を持つ。
5. 難易度整合性: 文面から予想される負荷と実際の解法深度が一致する。

盲検評価では各軸を1--5点で採点し、さらに「人間作 / MathOS作」の出所予想と
確信度を記録する。出所判別率が50%に近いだけでは自然とは結論しない。
数学的欠陥が両者を同程度に見分けにくくする可能性があるためである。

## 8. 評価プロトコル

1. 同一 `lift:family_id` 内で難易度が近い人間問題とMathOS問題を組にする。
2. 出所、family名、解答を隠す。
3. 数学経験別に評価者を層化する。
4. 各問題を最低5名が評価する。
5. 順序効果を避けるためA/B配置を乱数固定する。
6. Krippendorffのalphaまたは級内相関で評価者一致度を出す。
7. 自然さ・驚き・美しさは平均値だけでなく分布と信頼区間を報告する。
8. 人間問題の正答・成立性も独立検証し、systemだけに厳しい検証を課さない。

## 9. 反証条件

次のいずれかが起きた場合、一般化の主張を棄却する。

- 係数や基底を変えると同じLift familyへ戻らない。
- Frobenius、確率相関、ベクトル正規化が別々のbackend分岐を必要とし、
  共通のGram表現を共有できない。
- 正定値二次形式を次元3以上へ拡張するとチャートを全面的に書き直す必要がある。
- 人間評価で条件の不自然さが一貫して高く、条件除去実験でも冗長性が確認される。
- 新規構造数が増えず、数値違いだけで問題数が増える。

## 10. 次の実験

1. 内積チャートを次元可変にし、有限次元ベクトル・関数・行列を同じGram backendへ渡す。
2. 直交射影から最小二乗、回帰、Fourier係数へ射を拡張する。
3. 相関関数から畳み込み、スペクトル密度、正定値核へ接続する。
4. 条件アブレーションを全72問で実行し、条件必然性を定量化する。
5. 30盲検ペアについて人間評価を収集する。
6. 新しい内積系familyに対応する人間問題を別の凍結集合から収集する。

## 11. 成果物

- `atlas_verified72.json`
- `atlas_verified72.md`
- `creative_benchmark_atlas72_vs_selfauthored54.json`
- `creative_benchmark_atlas72_vs_selfauthored54_blind_pairs.json`
- `all_problems_selfauthored54_lift_match2.jsonl`
