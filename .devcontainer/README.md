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
