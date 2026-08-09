# 公開ベンチ: elaboration / backend contract 修復（2026-08-09）

## 目的

135問監査で観測した25件のelaboration失敗と10件のbackend未接続を、
問題ID・固定数値・完成解答を記憶せず、有限の質問形式と型付き数学演算として修復する。

## 実装した一般規則

- 英語の数学的質問を `count / measure / select / classify / compute` に型付け
- 通貨の `$` とTeX数式区切り、百分率の `%` とTeXコメントを字句段階で分離
- `UnitRateSum`、`FiniteMean`、`ModularInverse` を型付き演算として実行
- 根の領域修飾語を許した `RootAggregate` と、有理方程式の分母消去
- `OppositePairProbability` を有限確率空間上の対合として実行
- `TridiagonalDeterminantSeries` を行列式漸化式から実行
- `UniformApproachElevation` を一定速度と正接の制約から実行
- `IsoscelesMidlineAreaComplement` を関係グラフと相似比から実行
- 埋め込みAsymptoteの点構成・直線交点・正多角形スケール・面積を厳密実行

旧10件はすべて正答した。さらに対象名・数値・係数を変更した別入力でも同じ演算が発火する
metamorphic testを追加した。完成解答やbenchmark IDによる分岐は追加していない。

## 135問回帰

固定manifest: `03e4c7fadcf6d153ce4ce9f6def175a8139898acbc64058009b51082fbf0d3a0`

| 指標 | 修復前 | 修復後（cold path） |
|---|---:|---:|
| 型付け成功 | 98 / 135 | **135 / 135** |
| 正答 | 98 / 135 (72.6%) | **108 / 135 (80.0%)** |
| 回答精度 | 98 / 102 (96.1%) | **108 / 112 (96.4%)** |
| held-out正答 | 66 / 91 | **71 / 91** |
| 誤答 | 4 | **4** |

表層morphismを許す比較条件は128/135だが、これは本線の成果に含めない。

## Frozen 3,574問

- manifest SHA-256: `996fd351f775eaee017ca35420049541f949be283c06923257a1ba81c4f4944a`
- surface morphism / Web検索 / 外部ツール / LLM: 無効
- 1問12秒、8 worker、実測72.429秒
- この修復後に一度だけ実行

| 指標 | 結果 |
|---|---:|
| 型付け成功 | **3,436 / 3,574 (96.14%)** |
| 正答 | **663 / 3,574 (18.55%)** |
| 回答 | 1,224 / 3,574 (34.25%) |
| 回答精度 | **663 / 1,224 (54.17%)** |
| 誤答 | 561 |
| 棄却 | 2,350 |
| timeout | 4 |

分野別正答は、GSM8K 53/1319、MATH 58/700、SVAMP 110/300、ASDiv 122/301、
AQuA-RAT 10/254、MultiArith 72/180、MAWPS 238/520だった。

## 反証と次の対象

135問での改善は成立したが、高校数学全体への汎化は成立していない。3,574問の最初の失敗層は
`morphism_to_backend_gap` 2,176件、意味・戦略誤り557件、elaboration 108件、
backend実行44件、timeout等26件だった。

したがって次の中心課題は、語句規則の追加ではない。型付き意味IRから、既存の一般backendが
受理する制約系へloweringする射を増やし、実行前の意味整合性gateで561件の確信的誤答を
棄却へ変えることである。射の総数だけを増やしても、この2,176件は解消しない。

## 検証

- `python -B -m unittest math_os_prototype.test_math_os`: 113件成功
- 135問cold path: 108正答、timeout 0
- frozen 3,574問cold path: 663正答、timeout 4

