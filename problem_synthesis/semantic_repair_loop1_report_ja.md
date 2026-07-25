# SemanticRepairLoop v1 実験報告

実施日: 2026-07-23

## 目的

問題や解答を暗記せず、日本語・TeXから得た型付き数学対象と射の合成を反復検証し、
未見問題でも同じ数学的意味へliftできるかを測る。

## データ分割

jukenmath.netの公開問題477問を、投稿者と高類似問題が複数splitへ跨がないように
連結成分へまとめ、次の固定分割を作成した。

| split | 問題数 | 用途 |
| --- | ---: | --- |
| dev | 239 | 抽象演算子・射の昇格証拠 |
| calibration | 95 | score閾値の決定 |
| frozen held-out | 143 | 最後の一回だけ評価 |

held-outの評価回数は1回で固定した。データ集合のSHA-256は
`007339e74c8032a2272a469c5cfa9a90cf192ed873f4b19c24ade399bae346ef`。

解答文、正答値、問題ID、タイトル、完全な文型は昇格規則に使用していない。

## 追加した一般意味

- `Equation : Term(T) x Term(T) -> Prop`
- `RootSet : Equation x Sort -> Set(T)`
- `Distinct : Set(T) -> Prop`
- `Cardinality : FiniteSet(T) -> Natural`
- `Map : T x Function(T,U) -> U`
- `Image : Function(T,U) x Set(T) -> Set(U)`
- `ConvexHull : Set(Point2) -> Region2`
- `Derivative : Function -> Function`
- `Integral : Function x Interval -> Real`
- `FiniteSum : FiniteSet(T) x Function(T,A) -> A`
- `FiniteProduct : FiniteSet(T) x Function(T,A) -> A`
- `Variance : ProbabilitySpace x RandomVariable -> Real`

これらは問題型ではなく、型付き対象または射である。

## 反復プロトコル

1. 有限数学語彙を最長一致オートマトンで走査する。
2. 型が接続できる演算子列をparse forestとして列挙する。
3. 型、制約、query、量化の有無から候補を採点する。
4. 変数名変更で証明書が不変か検査する。
5. 数値変更で構造証明書が不変か検査する。
6. `forall/exists`変更で証明書が変わるか検査する。
7. `maximum/minimum`や`find/prove`変更でqueryが変わるか検査する。
8. devの複数分野・複数問題で安定した射だけを昇格する。
9. calibrationでscore閾値を4.0に固定する。
10. held-outを一回だけ評価する。

## devで昇格した規則

| 規則 | dev証拠数 | 分野数 | 反例テスト |
| --- | ---: | ---: | ---: |
| `Area -> Maximum` | 3 | 2 | 100% |
| `Area -> Minimum` | 3 | 3 | 100% |
| `Cardinality` | 4 | 3 | 100% |
| `Maximum` | 5 | 4 | 100% |
| `Minimum` | 6 | 5 | 100% |

途中で `Maximum -> Minimum`、`SetComprehension -> FiniteProduct` も候補になったが、
前者は同じquery階層の排他的演算子、後者は「積を」が「面積を」に部分一致した
偽規則だった。held-outを開く前に棄却した。

## 結果

| split | total | 旧type-checked | 旧Lift | 新type-checked | 反例テスト通過 | 昇格証明書 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| dev | 239 | 33 | 4 | 239 | 194 | 19 |
| calibration | 95 | 11 | 0 | 95 | 79 | 7 |
| held-out | 143 | 35 | 1 | 143 | 112 | 8 |

held-outでは、型付き候補は143問すべてで生成できた。111問はscore閾値と反例テストを
通過したが、devで同じ射の複数分野証拠がないものは昇格させなかった。そのため最終的な
昇格証明書は8問である。

## held-outで発火した意味

| 問題ID | 分野 | 射 |
| ---: | --- | --- |
| 512 | 微積分 | `Maximum` |
| 495 | 微積分 | `Area -> Maximum` |
| 319 | 図形 | `Area -> Maximum` |
| 274 | 数と式 | `Maximum` |
| 258 | 図形 | `Minimum` |
| 211 | 微積分 | `Cardinality` |
| 208 | 微積分 | `Minimum` |
| 14 | 図形 | `Area -> Maximum` |

## 解釈

旧Liftはheld-outで1/143、新しい昇格証明書は8/143であり、未見問題への構造転移は確認できた。
ただし8問は「問題を完全に解いた数」ではない。問題文からqueryまでの型付き意味射を、
表層・数値変更に耐える形で確定できた数である。

残る主な棄却理由は次の通り。

- devで未昇格の合成: 76
- composableな射がない: 28
- 反例テスト失敗: 27
- query不明: 2
- 制約不足: 1
- 型付き対象不足: 1

次の実験ではheld-outを再利用せず、新しい公開問題または次の時点の増分問題を
`future test` とする。改善対象は、`Equation -> RootSet`、`Derivative -> Limit`、
`Expectation -> Minimum`、`SetComprehension -> Cardinality` など、今回held-outで観測された
個別問題ではなく、別のdevコーパスでも再現する型付き射である。
