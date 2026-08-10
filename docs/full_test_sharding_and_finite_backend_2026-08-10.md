# 全テスト分割実行と共通有限モデル核（2026-08-10）

## 目的

テストを途中で打ち切らず全件実行し、失敗を問題文ごとの規則ではなく再利用可能なbackend契約へ分類する。その上で、整数論と確率に共通する最小表現を実装し、固定ベンチマークで効果を測る。

## 全テストの実行

`run_test_shards.py` を追加し、ルートの `test_*.py` をSHA-256で決定的に8分割した。各モジュールは独立プロセスで動き、個別タイムアウトとJSON記録を持つ。GitHub Actionsでも同じ8 shardを並列実行し、最後に結果を統合する。

最終結果:

| 指標 | 結果 |
|---|---:|
| モジュール | 49 |
| テスト | 431 |
| 成功モジュール | 49 |
| 失敗 | 0 |
| タイムアウト | 0 |
| ローカル総経過時間 | 702.286秒 |

重かった深層作問テストは、検証済み生成プールを一度だけ構築して共有するよう変更した。解析の大域最適性証明も、密な数値走査より先に記号的臨界点と境界極限を比較する形へ変更した。

## 共通有限モデル核

整数論と確率を別の問題型として追加せず、次の1つの射へ接続した。

```text
FiniteDomain
  -> PredicateFilter
  -> Observation(cardinality | probability | expectation | min | max)
```

実行operatorは `finite_model_observation` だけである。domainとして整数区間、正の約数、直積、組合せ、共通部分の濃度区間を持ち、predicateとして合同式、整除、階乗整除、平方数、出現回数、和の偶奇、積の整除などを合成する。

これは問題番号・benchmark名・期待解を読まない。数値を変えたときも同じoperatorと型を保ち、実行結果だけが変わることをテストしている。

## 固定3,574問での効果

manifestは `996fd351f775eaee017ca35420049541f949be283c06923257a1ba81c4f4944a` のまま固定した。

| 指標 | 実装前 | 実装後 | 差 |
|---|---:|---:|---:|
| 正解 | 807 | 816 | +9 |
| 正答率 | 22.5797% | 22.8316% | +0.2518pt |
| 回答 | 1,162 | 1,171 | +9 |
| 回答精度 | 69.4492% | 69.6840% | +0.2348pt |
| 誤答 | 355 | 355 | 0 |
| held-out正解 | 565 | 572 | +7 |
| morphism→backend未接続 | 2,218 | 2,209 | -9 |
| 正答回帰 | 0 | 0 | 0 |

増加した9問は、期待値、有限確率、平方数個数、約数、階乗整除、線形合同式、循環小数を同じ有限モデル観測で処理した結果である。

## 未接続の全数監査

未正解2,758件はすべて次の7契約へ割り当てた。うちmorphism→backend未接続2,209件の内訳は次の通り。

| 必要な共通契約 | 未接続 |
|---|---:|
| affine_system_eliminate_observe | 1,281 |
| finite_domain_filter_observe | 480 |
| typed_semantic_graph_requires_new_lowering | 222 |
| geometric_constraint_invariant_measure | 121 |
| symbolic_relation_eliminate_observe | 86 |
| matrix_vector_transform_observe | 15 |
| calculus_limit_integral_optimize | 4 |

したがって「全未接続を解消した」とはまだ言えない。全件を漏れなく分類し、同じ原因を問題別に直さず共通契約単位で接続する実験基盤まで完成した。次の最大対象は1,281件のアフィン状態・割合・比較・未知量の合成である。

## 再現コマンド

```powershell
python -B run_test_shards.py --all --shards 8 --jobs 4 --timeout 600 --report artifacts/test_shards/all.json
python -B audit_backend_gaps.py artifacts/public_benchmark_frozen_3574_after_finite_model_observation.json --output artifacts/backend_gap_contract_audit.json
```
