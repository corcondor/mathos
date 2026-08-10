# 型付きIRからCAS制約への接続 PDCA（2026-08-11）

## 問題

前回の3,574問監査では、2,258問が `morphism_to_backend_gap` に残った。
型付きIRには問合せ名があっても、CASが実行できる等式・不等式がない場合が
多く、バックエンドを呼ぶだけでは解けなかった。

## 実装した共通契約

問題ID、期待解、固有名詞、固定数値を入力にせず、次の数学的関係を実行可能な
制約へ変換した。

1. `Partition`: `total = fibre_count * fibre_size`
2. `StateTransition`: `final = initial + signed_delta`
3. `RationalLinearConstraintProjection`: 有理線形制約系から指定射影を観測
4. `RealFunctionSetObservation`: 実関数の定義域・値域・定義域の端点を観測
5. `FiniteIntegerSetAggregate`: 不等式で定まる有限整数集合を集約

全契約で、型付き穴は1個、数値前提の消費、CAS解の元制約への代入検査を
実行条件にした。検証不能な候補は回答しない。

## 暗記との区別

- ベンチマーク名、問題番号、期待解はコードから参照しない。
- 固有名詞はアルファ変換可能な頂点名として扱う。
- 数値を変えた場合は同じ制約骨格を使い、CASが再計算する。
- 配分、袋詰め、切片化は同じ `Partition` 射へ落ちる。
- 未接続構造を既知の答えで埋めず、棄却を維持する。

単体・統合テストでは、名詞・数値を変更した問題、異なる表層から同一法則へ
落ちる問題、LaTeX区間表現の同値性を含む172件が通過した。

## 同一3,574問での結果

条件は同じマニフェスト、12秒/問、8ワーカー、外部検索なし、表層問題別
アダプタなしである。

| 指標 | 前回 | 今回 | 差 |
|---|---:|---:|---:|
| 正答 | 851 | 1,094 | +243 |
| 誤答 | 267 | 267 | 0 |
| 棄却 | 2,456 | 2,213 | -243 |
| exact rate | 23.8109% | 30.6100% | +6.7991 pt |
| 回答精度 | 76.1181% | 80.3821% | +4.2640 pt |
| held-out正答 | 591 | 769 | +178 |

問題ID単位の差分は、新規正答243、既存正答からの回帰0だった。新規正答の
内訳は `Partition` 174、`StateTransition` 62、線形制約2、関数集合観測4、
有限整数集約1である。

## 残差

`morphism_to_backend_gap` は2,258から2,014へ減ったが、完了ではない。
最大残差は次の通り。

- generic `cas_symbolic_algebra`: 1,748
- LaTeX後のgeneric CAS: 238
- 型レビューが必要なgeneric CAS: 87
- 実行前の多変数制約・幾何・証明義務

次の反復では、GSM8Kに多い複数イベントと率の合成を、個別文型ではなく
`AffineAction`、`Rate`、`Composition` の制約閉包として接続する。

## 再現物

- `artifacts/public_benchmark_3574_dependency_gate_v3_20260810.json`
- `artifacts/public_benchmark_3574_typed_cas_lowering_v3_20260811.json`
