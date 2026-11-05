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
- GeometricDescent: 6定理 Lean成功。古典的3-isogeny公式の座標等式、像の曲線方程式、判別式、元の枝の座標、Pell型等式。群準同型・次数・降下完全性は未証明。
- DeepSeek作成の証明本文は計27定理。依存元＋追加7本（計8モジュール）最新再実行 PASS
- 注: RecoveredDivisor と NormalizedCancellation はホスト修正あり。上記5モジュールとは区別。

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
- ユーザーは検証済み成果とスキルをリポジトリへアップロードするところまで明示依頼済み。GitHubへのpushは許可済み。反映先は既存PR #1のresearch/nested-binomial-2026-11-05。既存PR #1の研究ブランチを基点に作業する。
- 環境スナップショット公開、新task復元、モデル重みの更新はこの作業では行わない。GitHub pushの結果は実行後に追記する。

## 再利用する資料と手順
- 追加11リポジトリの実在と固定コミットを確認し、README抜粋をDeepSeekへ共有済み。AI_RESEARCH_REFERENCES.mdとAI_RESEARCH_REFERENCE_CATALOG.jsonを参照。
- APIヘルパーは委任スキル、本状態、参考資料要約を呼び出しごとに再読込する。モデルの重みは更新していない。
- 不明なmathlib名はローカルの実宣言を検索して返す。一括生成で失敗したら1定理ずつ進め、成功済み本文は固定する。
- 幾何学の既知失敗：特異なモデルや符号の「吸収」を採用しない。逆のrは-x/zであり、-x/cや-x*z/cではない。

## GitHubへの反映確認
- 2026-11-06（日本時間）、コミット `75adc345637784811f39fb5ad9bf74cfbcc4e073` を `research/nested-binomial-2026-11-05` へ通常のfast-forward pushで反映し、`git ls-remote` で同じ先頭SHAを確認した。
- 対象は https://github.com/corcondor/mathos/pull/1 。この記録を含む後続コミットがあるため、今後の作業前には現在のPR先頭を再確認する。mergeや環境スナップショットの公開はしていない。

## 長い推論と専用チャット（2026-11-06 JST）
- APIモデル名は実際のmodelsエンドポイントで確認。`reasoning_effort: high` を実APIで試し、thinking/textの複合応答と推論トークンを確認済み。xhigh/maxは未確認のため使わない。
- 現在の研究プロファイル: High、max_tokens 65536、HTTP待機900秒、最大試行20、Lean待機180秒。推論時間は固定できず、トークン予算と待機時間は別。
- 実研究依頼にPR #1・固定コミット・許可済み研究ファイル本文・スキル・状態・11参考リポジトリ要約を共有。32768推論トークンで最終回答なしの最初の応答は未採用。文脈を引き継いだ続行は推論10148トークン、31.869秒で最終提案を取得。
- GeometricDescentの6証明はすべてDeepSeek。ホストは定理固定前に余分なnamespaceを除去しただけで、成功した証明本文を修正していない。
- 「最先端の数学が必須」とする根拠は現時点ではない。まず古典的・確立手法の射程と完全性の穴を調べ、道具の新しさを目的にしない。
- チャットにはLean実行・GitHub pushのツールは接続していない。返答の証明案を検証済みと扱わない。別の既存goal workerで実検証する。
- 実際の研究質問をUIから送り、DeepSeekの日本語回答を取得。会話復元、スマホ表示、スキル表示をPlaywrightで確認。ブラウザプラグインは利用不可。

## Mistral公式UIへの移行（2026-11-06 JST）
- ユーザーの意図は独自UIの新規作成ではなく、Mistral公式UIでDeepSeekと直接会話すること。独自UIの追加作業は止める。
- 公式Playgroundをブラウザで開くとログイン画面。ユーザーのログイン済みセッションにはアクセスできず、Playground上のモデル選択は未実施。
- /v1/agents の作成は組織側で403「Creating agents is not available for this organization. Use Managed Agents instead.」。管理者権限不足と断定しない。Managed Agentのデプロイも実行していない。
- 現行 /v2/prompts と /v2/skills は利用可。両方へ非公開で保存し、GETで本文・共有範囲を照合済み。
- Prompt: 二項係数方程式・Lean研究（DeepSeek）、name=mathos-nested-binomial-research、id=01a1ae13-ed1a-7756-9e6c-8b887385f678、version=1、sharingScope=private。公式画面 https://console.mistral.ai/build/prompts 。
- Skill: mathos-nested-binomial-research、id=01a1ae13-df1d-733f-99f3-36d60f397ee0、version=1、sharingScope=private。公式画面 https://console.mistral.ai/build/skills 。
- 許可済み研究資料26ファイル（v10/v11のノート・Leanソース・スキル・状態・参考資料）を保存。静的なスナップショットであり、自動GitHub同期・自動ファイル再読込・モデルの重み更新ではない。
- 保存したPromptをAPIで再取得して deepseek-v4-1-flash-1017 / high / max_tokens=65536 に実送信。4.43秒、prompt_tokens=78110、reasoning_tokens=709、finish_reason=stopで引き継ぎ内容の日本語回答を確認。
- 推奨モデル名をPromptに記載してもPlaygroundのモデル選択は変更されない。UIで選択済みと主張しない。
- 保存物と照合結果: /workspace/.cloud-setup/mistral-studio/studio_result.json と saved_prompt_connection_check.json。キーは保存していない。

## 最新の決定：このチャットで研究を継続
- ユーザーは公式UIへの移行を取りやめ、このCodexチャットで進めると決定。UI作成やログイン対応を追加で進めない。
- DeepSeekが研究・証明生成と修正、ホストが実Lean検証・成果保存・既存PRへのpushを担当する。
- 新しいGeometricDescentの6定理を含む8モジュールの実Lean検査がPASS。推論設定と一緒に既存PRへ保存する段階。
