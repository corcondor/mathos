# v30以降：公開に連動する検証・DeepSeek研究

2026-11-07 JST。GitHubイベントに反応する研究自動化。設計上の限界も明記する。

## 実装済み

- [公開イベントのワークフロー](../../../.github/workflows/nested-binomial-publish-research.yml)：新しいV30、V31などの研究ノートをPRで扱うと、APIを呼ばずにv30の合同式を再検算。新規のバージョン別検算Pythonも最大180秒で検査。これは数学的な完全証明や新規性の証明ではない。
- 新規バージョンノートがmasterに追加されると、Actionsの MISTRAL_API_KEY が存在する場合のみ、DeepSeekへ独立研究仮説を1件依頼。18,000文字までの公開研究ノートを送り、1リクエスト最大6,000出力トークン。429のみ1回再試行、最大2呼出し。新しい版の公開がなければAPI使用は発生しない。
- [研究仮説の生成コード](../../../.github/scripts/nested_binomial_ai_proposal.py) は生成物を厳密に UNVERIFIED と表示し、GitHub ArtifactとドラフトPRへの保存を試みる。出力は仮説であり、Leanで証明した数学的新結果ではない。
- [Lean検証ワークフロー](../../../.github/workflows/nested-binomial-lean-check.yml)：v10_formal 以下のLean証明モジュールが追加・変更されたとき、指定のLean 4.35.0とmathlibで検査する。モデル生成コードを無検証で実行しない。APIキー不要。

## 1回の設定

1. GitHubの [Actions Secrets](https://github.com/corcondor/mathos/settings/secrets/actions) でリポジトリシークレット MISTRAL_API_KEY を設定。**Codespaces Secretsとは独立**である。共有キーの所有者にAPI自動利用の許可を取る。
2. [PR #4](https://github.com/corcondor/mathos/pull/4) で内容を確認してmasterへマージ。マージ後は新しい版の公開ごとに自動トリガー。
3. [Actions画面](https://github.com/corcondor/mathos/actions)で検算とDeepSeekの結果を確認。GitHub ActionsによるPR作成を許可するには、Settings → Actions → General → Workflow permissions で適切な権限と Allow GitHub Actions to create and approve pull requests を確認。PR作成が禁止でもArtifactとして残る。
4. GitHub Actionsの無料枠・制限とMistralのAPI課金は別。キーが未設定ならAI推論は自動スキップされる。

## 現在のCodespaces復旧

添付ログ：実行中のプロセスなし、保存状態は97アクション、最後の課題は CFRationalCubeExclusionB。 Mistral 429容量エラーとNat.sub_assocのLean修正待ち。

同じCodespaceのターミナルで以下を実行すると保存済み状態からの再開を試みる：

    .devcontainer/research status
    .devcontainer/research logs
    .devcontainer/research run

1回あたり48アクション/6時間という既存上限は残る。今回のGitHub Actionsの研究仮説生成とは別プロセスであり、元の97アクションの保存状態をActionsへ移したわけではない。

## 未完成（誇張しない）

- v30→v31と一切の人手なしで新定理を探索し続け、SageMath・Leanで検証して正式な研究成果として公開する継続ワーカーは未実装。
- GitHub Actionsはイベント駆動の一時環境。常駐・無期限実行や、Codespaces内だけの秘密チェックポイントの自動移行は保証しない。
- AIの新しい仮説はドラフトPRとして公開するが、未検証の提案を数学的証明として公開しない。既存DeepSeekの固定Lean最終2目標は変更しない。
