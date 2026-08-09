# 実行可能意味制約の修復（2026-08-10）

## 問題

型検査に成功しても、値を持つ制約として backend へ渡らない問題が多かった。従来の
3,574問評価では `morphism_to_backend_gap` が2,096件あり、型名の到達率を解答能力と
誤認できない状態だった。

## 追加した実行層

1. **TeX affine lowerer**: TeX ASTから一次制約を抽出し、有理数Gauss消去で実行する。
2. **Typed fact closure**: 型付き述語、Horn則、重複排除、閉包、証明tracebackを同一核で扱う。
3. **AlphaGeometry2 DDAR adapter**: 公式symbolic engineをMathOS Workerから呼び出す。
4. **Dimension-checked synthesis**: `apple/hour * hour -> apple` のように、次元消去で演算が
   一意な乗除だけを実行する。
5. **State/Event synthesis**: 同一状態sort上の明示イベントを
   `final = initial + gains - losses` へloweringする。

問題ID、データセット名、期待解は実行器へ入力しない。加減の意味が型だけで決まらない場合、
割合が現在状態に作用する場合、未知量が残る場合は棄却する。

## 定量結果

同一manifest (`996fd351...`) の3,574問を、case timeout 12秒、8 workers、外部検索なしで評価した。

| 指標 | 修復前 | 修復後 |
|---|---:|---:|
| exact | 672 / 3,574 | **681 / 3,574** |
| exact rate | 18.80% | **19.05%** |
| answered | 1,254 | 1,226 |
| answer precision | 53.59% | **55.55%** |
| held-out exact | 468 | **474** |
| wrong | 582 | **545** |

新規実行経路の内訳:

- dimension-checked synthesis: **10/10正解**
- State/Event synthesis: **12/12正解**

公式AlphaGeometry2の公開形式化例では、MathOS adapter経由でDDAR 26/26を再現した。これは
自然文幾何26問を自動形式化した結果ではなく、形式化後の閉包推論backendが接続された証拠である。

## 失敗から得た設計制約

初版の次元合成は加減も許し、88回答中16正解まで崩れた。次元は乗除を拘束できるが、
同型量の加算と減算を区別できない。加減をState/Event層へ分離すると10/10になった。

初版State/Eventは比較、割合、未知量、省略照応を同じイベントとして扱い18回答中9正解だった。
これらを別制約へ分離し、同一対象の省略だけを統合すると12/12になった。

したがって次の改善対象は語彙追加ではなく、比較式、割合作用、未知量を値付き制約へloweringし、
閉包エンジンとCASへ渡すことである。
