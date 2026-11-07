# Codespaces で DeepSeek の Lean 証明ランナーを起動する

1. [研究ブランチから Codespace を作成](https://codespaces.new/corcondor/mathos/tree/research/nested-binomial-2026-11-05)します。作成画面に `MISTRAL_API_KEY` 欄があれば、そこにキーを登録できます。[Codespaces のシークレット設定](https://github.com/settings/codespaces)から登録する場合は、`corcondor/mathos` にアクセスを許可します。作成済みの Codespace に後からキーを追加した場合は、一度停止してから開き直します。
2. 自動セットアップが終わったら、Codespaces のターミナルで実行します。

   ```bash
   .devcontainer/research run
   ```

セットアップはバックグラウンドで Lean 4.35.0 と mathlib のコミット `56a005855ea17e0b0958f73ec801ae140b0a1679` を用意し、短い証明を実際にコンパイルして起動環境を確認します。既存の証明モジュール全体は GitHub Actions と `verify` で再検証できます。Python 3.11 以上の標準ライブラリでランナーを実行します。セットアップと再検証は Mistral API を呼び出しません。

初回は、ブランチに保存されている Lean モジュールを引き継いで新規実行します。以前の 179 アクション分の `state.json` は取り込んでいません。同じ Codespace で再度 `run` を実行すると、その Codespace の保存状態から再開します。

| コマンド | 動作 |
| --- | --- |
| `.devcontainer/research status` | 稼働の有無、保存済みの進捗、API 使用状況を表示します。 |
| `.devcontainer/research logs` | ランナーのログの末尾 80 行を表示します。 |
| `.devcontainer/research pause` | 一時停止を要求します。処理中の API 呼び出しが戻るまで待つ場合があります。 |
| `.devcontainer/research verify` | 既存の証明を再検証します。 |
| `.devcontainer/research setup` | 初期セットアップに失敗したときに再試行します。 |

同時に起動できるランナーは、同じ Codespace 内で 1 つです。状態、ログ、Lean のキャッシュは `.mathos-codespaces/` に保存され、Git の対象外です。同じ Codespace の停止やコンテナーの再構築をまたいで残ります。Codespace を削除すると、その中だけにある状態も失われます。新しい証明の公開には、対象ブランチへの書き込み権限を持つ Codespaces の GitHub 認証を使います。

公開前に、新しい証明とそのローカル依存を Lean で再検証します。変更のないモジュールは、同じ Lean と mathlib で検証済みであり、ソースとログのハッシュが保存済みの記録に一致するときに、以前の検証記録を再利用します。

Codespaces でも既存ランナーの研究設定を使います。1 回の起動につき研究操作は最大 48 件、API 送信を始められる時間枠は 6 時間、出力の使用枠は推論を含めて合計 200 万トークンです。1 回の送信には最大 131,072 出力トークンを使えます。区切りに達したら、再度 `run` を実行すると保存地点から再開します。

## 同じCodespacesのAPIキーを使う自動再開（任意）

このCodespaceでは、既存の `MISTRAL_API_KEY` をそのまま使用できます。新しいAPI契約や別のAPIキーは不要です。

現在の研究の保存状態から通常再開するには `.devcontainer/research run`。
48アクションごとの手動再実行を減らすには、一度だけ次を実行します。

```bash
.devcontainer/research auto
```

これにより `.mathos-codespaces/autopilot.enabled` が保存され、同じCodespaceが稼働している間は、既存の `state.json` から**小さく区切ったDeepSeek研究を自動再実行**します。研究ブランチを証明保護付きで同期してから各実行に入ります。新規Lean証明の公表時は既存の核検証・GitHub公開手順を通します。

操作：

```bash
.devcontainer/research auto-status
.devcontainer/research status
.devcontainer/research logs
tail -n 80 .mathos-codespaces/autopilot-run.log
.devcontainer/research auto-stop
```

**利用上限**：既定ではUTC日付ごとに出力（推論を含む）350,000トークン、API最大12回、1回の周期は最大12アクション・250,000出力トークン・8API回・2時間。上限に到達したら追加のAPI呼び出しを行わず、次のUTC日付まで停止状態で待ちます。入力トークンとCodespaces計算資源の費用も別途発生します。安全のため、`complete`、`paused`、`blocked` または実行エラーなら自動ループを止めます。既存の手動 `run` コマンドのデフォルト（48アクション）には影響しません。

**重要な限界**：GitHub Codespacesはアイドル停止し、連続稼働の上限もあります。自動再開はCodespaceが起動したときだけです。完全な24時間常駐や、Codespace停止中にv31が公開された瞬間のDeepSeek API実行までは保証しません。新しいdevcontainerの起動フックを既存Codespaceへ適用するには、設定変更を取り込んでからコンテナーの再構築が必要な場合があります。自動監視の状態はCodespace専用ディレクトリに保持され、削除すると失われます。

`auto` は**既存の固定Lean最終2目標を再開する**機能です。GitHubのv30・v31研究ノートは背景資料として同期されますが、それだけで新しい独立ゴールに切り替わったと主張しません。新しい版の公開ごとに別研究を始めるには、既存固定ゴールとは分離された研究キューも必要です。

