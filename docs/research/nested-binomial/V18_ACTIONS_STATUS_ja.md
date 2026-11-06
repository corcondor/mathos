# v18 Actions の導入・実行状態

初期実装はコミット `bba851b` として研究ブランチ
`research/nested-binomial-2026-11-05` にpush済み。
GitHub Contents APIでも新しいワークフローの保存を確認した。

今回のクラウド環境で確認した事実:

* 研究ブランチのActions実行一覧: **0件**。
* 新設workflowへの `workflow_dispatch` API: **HTTP 404 Not Found**。
* リポジトリのActions設定の読取API: **HTTP 403 Resource not accessible by integration**。
* 既存の4つのworkflowは `disabled_manually`。今回これらを有効化・変更していない。
* 新設workflowはデフォルトブランチmasterにまだ存在しない。GitHubの手動dispatchの前提を満たしていない。pushで実行が作られなかった原因については、設定APIが読めないため確定できない。

したがって、**GitHub runner上のSageインストール・rank計算・自動結果commitは未実行・未検証**。
「実行中」「ランク計算済み」とは扱わない。
追加のAPIキーや利用者のPCでの計算を求める問題ではない。

クラウド環境での軽量検証:

* 整数演算・残差座標・厳密高さ・打切りcheckpoint・未着artifactの回帰検査。
* 実Gitの一時リポジトリで、生成結果だけのcommitと、無関係な未保存Lean変更の保持を検査。
* actionlint 1.7.7でワークフロー構文検査。
* n≤5000の小さい探索でCLIと集約処理を検査（研究計算の完走結果としては保存しない）。
* 既存の独立監査を実行し、830候補・平方3件・残存0件を再確認。

起動方法と出力の意味は [V18_ACTIONS_ja.md](V18_ACTIONS_ja.md) に記載。
研究ブランチの計算コードは保存済みで、GitHub側で実行が有効になればPCなしで計算と結果保存が進む。
