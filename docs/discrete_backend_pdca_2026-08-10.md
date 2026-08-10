# MathOS 整数論・計数確率の離散backend PDCA（2026-08-10）

## 問題の特定

アフィン・n次元幾何接続後のMATH各100問では、次が最大の分野別欠損だった。

| 分野 | 正解 | 回答 | morphism→backend未接続 |
|---|---:|---:|---:|
| 整数論 | 8/100 | 9/100 | 78 |
| 計数・確率 | 6/100 | 11/100 | 85 |

共通原因は、有限集合・合同類・順列・部分集合・確率空間を型付き意味IRから実行核へ渡せていないことだった。

## 共通IR

問題別の解答規則ではなく、次の対象と射を実装した。

```text
FiniteDomain / CongruenceClass
  -> PredicateFilter
  -> Cardinality | Extremum | Probability | ModularObservation
```

主なexecutor contract:

- `modular_observation`
- `congruence_system_extremum`
- `finite_set_filter_count`
- `finite_probability`
- `injective_role_assignment_count`
- `word_predicate_count`
- `multiset_selection_count`
- `permutation_predicate_count`
- `combinatorial_expression`
- `multiset_permutation_count`
- `subset_selection_count`
- `grouped_subset_selection_count`
- `block_permutation_count`

整数論と計数確率の両方が `finite_set_filter_count` を共有する。例えば「区間内で倍数条件を満たす整数」と「上限以下で末尾条件を満たす素数」は、domainとpredicateが異なるだけで同じ射を通る。

## 解法暗記を避ける検査

- benchmark名、問題番号、期待解をIR・executorへ渡さない。
- 数値変更でも同じoperatorへloweringされ、答えだけが変わるテストを置いた。
- executorは有限列挙、CRT、階乗商、二項係数を再計算する。
- 確率は `favorable / all outcomes` として既約分数化する。
- 共有意味グラフに `FiniteDomain -> operator -> output sort` と全predicateを記録する。
- 旧正答からの回帰を問題ID単位で比較する。

## 定量結果

固定manifest: `996fd351f775eaee017ca35420049541f949be283c06923257a1ba81c4f4944a`

| 指標 | 開始時 | アフィン・n次元後 | 離散backend後 |
|---|---:|---:|---:|
| 3,574問 正解 | 776 | 782 | **807** |
| 正答率 | 21.7124% | 21.8802% | **22.5797%** |
| 回答数 | 1,137 | 1,137 | **1,162** |
| 回答精度 | 68.2498% | 68.7775% | **69.4492%** |
| 誤答 | 361 | 355 | **355** |
| held-out正解 | 544 | 549 | **565** |
| morphism→backend未接続 | 2,239 | 2,242* | **2,218** |
| 正答回帰 | - | 0 | **0** |

`*` 前回タイムアウト3問が完走して未接続と判明したため、一時的に増えた。

MATH 700問は114→145。分野別では整数論8→12、計数確率6→27。

対象テスト198件は成功。全テスト探索は5分上限では完走しなかったため、「全テスト成功」とは記録しない。

## 次の重点

整数論は12/100に留まる。残る主要な制約スケルトンは次の通り。

1. 線形合同方程式と合同式連立
2. gcd/lcmと素因数指数ベクトル
3. 基数変換と桁制約
4. 約数集合・平方因子・終端小数条件
5. 有限整数探索の最小・最大観測

計数確率では、超幾何分布、条件付き有限確率、線形拡張、格子経路、包除原理を同じ有限集合核へ接続する。

