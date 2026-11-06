# DeepSeek自身が進める継続目標

ユーザーの意図は、Codexの `/goal` を説明することではなく、DeepSeek自身に
課題選択から研究・証明生成・修正まで継続させること。
この実装は **DeepSeek用のカスタムスキルと実行器**であり、DeepSeek APIに
ネイティブの `/goal` コマンドがあるという意味ではない。

## 誰が判断するか

`deepseek-v4-1-flash-1017` が毎回JSONで次の行動を選ぶ。
資料・mathlibの読取と検索、固定ジョブの提案、証明、修正試行数、
チェックポイント、検証済み成果の公開先ブランチへの保存を選べる。
Pythonは選ばれた操作を実行し、実際のLean結果を返す。
Codexは実行器の実装・監視を担当し、次の数学補題を指示し続ける構造にはしない。

数学の目標・定理文・証明はDeepSeekが作成する。
ホストは定理文と元ノートの対応を点検し、最終目標を固定した。
証明本文はホストが手作業で編集しない。

## 固定した完了条件

[goal.json](../../../.agents/skills/deepseek-goal/goal.json) に、DeepSeekが作成した
2つの正確な定理文とSHA-256を保存した。

- `CFSmallDefectGoal.small_defect_curve_exclusion`：ノートのS=1..12の条件の下での曲線排除。
- `ThirtyCofactorGoal.thirty_cofactor_exclusion`：元の二項係数の式をそのまま使った30余因子の非存在。

どちらもCFの正しさ・証明書の健全性を仮定に入れていない。
型を弱める、既存証明を上書きする、補題数で完了判定する、モデルのPASSだけを採用することはできない。
両方の固定定理が実Leanで通り、標準公理依存のみで、GitHubへ保存済みの場合だけ `complete` にできる。
全四変数方程式の解決とは区別する。

## 実行と確認

リポジトリのルートから実行する。既存のキーとmax推論プロファイルを使う。

```bash
python3 docs/research/nested-binomial/v10_formal/deepseek_goal.py run
python3 docs/research/nested-binomial/v10_formal/deepseek_goal.py status
python3 docs/research/nested-binomial/v10_formal/deepseek_goal.py pause
```

`run` は保存状態を再開する。スキルは毎回読み、元の研究スキル・状態・参考資料もAPIヘルパーが読み込む。
数学的な次の指示をCodexへ求める必要はない。
途中のチェックポイントでは継続し、上限・停止・実行エラーでは未完了のまま状態を保存する。
停止要求は現在の操作終了時に確認し、実行中の証明ワーカーは停止して成功済みの前半を保持する。
プランナーのAPI応答待ちは停止要求後も応答まで待つ場合がある。

既定の1回の実行上限は **6時間・48判断・API報告の出力合計200万トークン**。
プランナー、別呼び出しの範囲点検、子ワーカーの推論を同じ予算ファイルで集計する。
各呼び出しはmax、出力上限131072（推論込み）を基本とし、残り予算に合わせて上限を下げる。
修正試行はDeepSeekが1〜20回から選び、指定なしなら5回で一度結果を返して次の方針を考え直す。
不明なusageは無料扱いせず、その要求上限で計上する。
これはAPIが返した使用量の管理であり、請求額の保証ではない。

実行状態と非公開の生応答は `/workspace/.cloud-setup/deepseek-goal/nested-binomial-cf/`。
進捗の公開用要約は `DEEPSEEK_GOAL_PROGRESS.md`。
生の推論チャンクやAPIキーをGitHubへ保存しない。
環境停止中に動作し続ける常設サービスや、Mistralへのデプロイではない。

## 検証と保存

固定ジョブの範囲は別のDeepSeek呼び出しで点検する。同じモデルであり、外部の独立査読ではない。
証明は既存の `deepseek_goal_worker.py` で実行・修正し、検証済みモジュールを
`goal_verified_modules.json` へ登録する。全体チェッカーは局所依存を順にコンパイルする。
保存は検証済みソース、固定ジョブ、検査記録、進捗要約だけを明示的にstageする。
無関係なstage済み変更があれば、それを混ぜてcommitしない。

保存先は既存の非公開PR #1の `research/nested-binomial-2026-11-05`。
通常のpush後にremote SHAを照合し、merge・環境公開・新しい公開サイトの作成は行わない。
