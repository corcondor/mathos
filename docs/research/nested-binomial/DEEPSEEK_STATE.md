# DEEPSEEK_STATE.md — 現在の研究状態

最終更新: 2026-11-06（日本時間）。手順スキル deepseek-math-research より参照。

## 委任方針
- 証明生成・修正は可能な限り DeepSeek (`deepseek-v4-1-flash-1017`) へ委任。ホストは情報取得・API委任・コンパイル・実検算・成果保存を担当。成功した証明本文の手作業書き換えは禁止。
- モデル重みは更新しない。状態は本ファイルとスキルファイルに保存し、各API呼び出し前に再読込する。

## 検証済み（DeepSeekのみが作成・修正）
- LocalSquareRecovery: 4定理 Lean成功
- CriticalPrimeCRT: 3定理 Lean成功
- CFApproximationCore: 5定理 Lean成功
- GeometricReduction: 9定理 Lean成功（定義・定理文はホスト側で点検・訂正、証明本文と修正はDeepSeek）
- DeepSeek作成の証明本文は計21定理。依存元＋追加6本（計7モジュール）最新再実行 PASS
- 注: RecoveredDivisor と NormalizedCancellation はホスト修正あり。上記新規3モジュールとは区別。

## Python厳密検算
- 全5214曲線、4,877,566連分数係数、25,394,330既約分数、残存点0。`cf_current_revalidation.json` に保存。
- Python成功をLean形式化完了とは呼ばない。

## 未完・未解決
- 30余因子最終定理はCF部分の仮定を未だ外していない。
- 未了項目: 小分母 a∈[-1,4]、大分母 a-b*a_next∈[-3,3]、65組の網羅性、収束分数区間選択、円筒区間認証、全曲線候補のLean検査、最終定理接続。
- 全四変数の問題は未解決。

## モデルの既知失敗（再発防止）
- 近似定数3/2をLegendreの1/2へすり替え。
- det=-1から+1を同一列で導出。
- pQ-qP と b*(PmQ-PQm) の列取り違え。
- S|n-2 から rad(n-2)|S を導出。

## 環境
- Lean 4.35.0、mathlib `56a005855ea17e0b0958f73ec801ae140b0a1679`。
- 実行場所 `/workspace/.cloud-setup/lean/mathlib`、`ELAN_HOME=/workspace/.cloud-setup/lean/elan`、PATH先頭 `/workspace/.cloud-setup/lean/elan/bin`。

## 最新のユーザー指示と進行状態
- 幾何学の対象は現在の二項係数方程式と確定済み。三次曲線から楕円曲線への写像、降下法などをDeepSeekに検討させ、実Lean検証する。9定理で有理座標変換と逆、Δ=-432c^4≠0、IsElliptic、j=0、研究曲線への適用をLean検証済み。写像はx=-cr/y,z=c/y、逆はy=c/z,r=-x/z。階数・降下・全解は未計算。
- ユーザーは検証済み成果とスキルをリポジトリへアップロードするところまで明示依頼済み。GitHubへのpushは許可済み。反映先は既存PR #1のresearch/nested-binomial-2026-11-05。pushの実結果は実行後に追記する。既存PR #1の研究ブランチを基点に作業する。
- 環境スナップショット公開、新task復元、モデル重みの更新はこの作業では行わない。GitHub pushの結果は実行後に追記する。

## 再利用する資料と手順
- 追加11リポジトリの実在と固定コミットを確認し、README抜粋をDeepSeekへ共有済み。AI_RESEARCH_REFERENCES.mdとAI_RESEARCH_REFERENCE_CATALOG.jsonを参照。
- APIヘルパーは委任スキル、本状態、参考資料要約を呼び出しごとに再読込する。モデルの重みは更新していない。
- 不明なmathlib名はローカルの実宣言を検索して返す。一括生成で失敗したら1定理ずつ進め、成功済み本文は固定する。
- 幾何学の既知失敗：特異なモデルや符号の「吸収」を採用しない。逆のrは-x/zであり、-x/cや-x*z/cではない。
