# 公開ベンチ: 射・backend 被覆監査（2026-08-09）

## 固定条件

- 問題数: 135
- 内訳: GSM8K 30 / MATH 35 / SVAMP 30 / ASDiv 30 / AQuA-RAT 10
- manifest SHA-256: `03e4c7fadcf6d153ce4ce9f6def175a8139898acbc64058009b51082fbf0d3a0`
- surface-morphism adapter: 無効
- 外部検索・外部ツール: 無効
- 1問の上限: 12秒
- worker: 8

## 結果

| 指標 | 結果 |
|---|---:|
| 正答 | 98 / 135 (72.6%) |
| 回答 | 102 / 135 (75.6%) |
| 回答精度 | 98 / 102 (96.1%) |
| held-out 正答 | 66 / 91 (72.5%) |
| 誤答 | 4 |
| 棄却 | 33 |
| timeout | 0 |

## 不正解・棄却37問の最初の失敗層

| 層 | 件数 |
|---|---:|
| 指示対象・量化・型の elaboration | 25 |
| 射から backend への実行接続 | 10 |
| backend 実行 | 1 |
| 意味・戦略 | 1 |

## 被覆量

- semantic morphism: 567
- backend obligation: 190
- planned tool call: 135
- executable tool call: 104
- successfully executed tool call: 102

## 解釈

静的Atlasの型到達可能性だけでは、ベンチの実行可能性を説明できない。
この標本では射の総数よりも、問題を型付き目標へ確定する elaboration と、
既存射を実行器へ渡す contract が主な不足である。新しい射は、到達不能な
source/target が観測された場合に限って追加し、backend未接続を射不足と数えない。

この135問は回帰監査であり、3,574問全体への一般化を主張するものではない。

