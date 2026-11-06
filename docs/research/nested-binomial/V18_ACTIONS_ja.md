# v18 の GitHub Actions 計算

このワークフローは GitHub の `ubuntu-latest` 上で動く。利用者のPC、Mistral API、既存のDeepSeek/Leanプロセスは計算に使わない。新しいAPIキーは不要。

## 起動

ワークフロー: [v18-number-theory.yml](../../../.github/workflows/v18-number-theory.yml)

`research/nested-binomial-2026-11-05` または `research/v18-next-descent` への計算コード・入力資料のpushで起動する。結果だけのcommitでは再起動しない。初回はこのpushトリガーを利用する。

手動実行は GitHub → **Actions → v18 number theory computations → Run workflow** で研究ブランチを選ぶ。`workflow_dispatch` のGitHub仕様上、ワークフローがデフォルトブランチに存在しない段階ではボタン/APIが利用できない場合がある。その場合も研究ブランチのpushトリガーは使える。これを理由にmasterを自動更新しない。

CLIでの手動実行（GitHub側でdispatchが利用可能な場合）:

```sh
gh workflow run v18-number-theory.yml --repo corcondor/mathos \
  --ref research/nested-binomial-2026-11-05 \
  -f a_max=20 -f n_max=1000000 \
  -f j_small_max=100 -f j_complement_max=30 -f curve_seconds=120
```

|入力|既定値|意味|
|:--|--:|:--|
|a_max|20|既約残差係数の分子上限|
|n_max|1000000|固定J探索のnの上限（最大10000000）|
|j_small_max|100|k=rのcanonical J上限|
|j_complement_max|30|k=A-rのcanonical J上限|
|curve_seconds|120|1曲線あたりのCAS強制終了時間（秒）|

## 実行される計算

### 1. 残差曲線・ランク・Mordell–Weil・整数点

micromambaでconda-forgeの `sage=10.6`, `python=3.12` をインストールする。`ubuntu-latest` のaptリポジトリでのSageパッケージの有無に依存しない。環境のexplicit package listをartifactに残す。Actions自体もコミットSHAに固定する。

a≥1, b|486, gcd(a,b)=1, 27a<31b, a≤a_maxの全係数対を4ジョブへ分割する。既定では83対、うち (1,3) は判別式0なので特異曲線として別扱いする。

Sageで元の曲線・有理最小モデル・モデル間同型・最小判別式を構成し、conductor、`rank(proof=True)`、`gens(proof=True)`、`gens_certain()`、ねじれ生成元を記録する。生成元は最小モデル上の射影座標。時間切れはrank=0や空の認証済み基底に置き換えずunknown/partialとして残す。

残差区間では、ρ>0、ρ≡a² (mod b)、1377ρ<216a²+760b² の全ρを列挙し、X=4a²-b²-4ρについて元の曲線の右辺が整数平方かを厳密に判定する。Yの両符号を保存する。この有限区間の完全性はMW基底の認証に依存しない。最小モデル上の整数点を逆写像して元の整数点を取り落とす方法は使わない。無制限の整数点全列挙や元の二項係数等式の解の主張ではない。

出力:

* `v18_ranks_a20.md`, `v18_ranks_a20.json`（a_max変更時はファイル名も変更）
* `v18_modular_levels.json`: 正rankと確認できた曲線のconductor、LMFDB用レベル、検索URL。newform照合は後段。

### 2. 固定Jの探索

標準Pythonで最小素因数表を作り、各nの Q=n(n-1)/M に対して F=∏p^ceil(v_p(Q)/3) を計算する。Q|r³と同値なF|rを使い、3n<r<10n/3内の全rを生成する。v17/v18のgap、δ、canonical Jの必要条件で絞り、元の等式

```
binom(binom(n,3), k) = binom(n^2, (n-3)^2) + k^2
```

を両分岐についてLucasの定理で素数2〜43を法として検査する。排除時は法と左右の剰余、未排除時は未決候補を残す。

高さはsmall枝の n<16J⁶ と n¹⁴<2³⁵²J³³ の小さい方、補分岐の n³<2³⁵²J³³ を使用する。整数根の切り上げも整数演算で行う。要求したJすべての高さを走破したと装わず、Jごとに `height_fully_covered` を保存する。既定のn≤1000000ではsmall枝J≤6の高さ全域を覆える。J=7〜100と補分岐J≤30は一部探索である。任意の上限打切りを完全排除と呼ばない。

出力: `v18_fixed_J_search.md`, `v18_fixed_J_search.json`。

### 3. 短いLCMの830例外

既存の `v18_short_lcm_independent_audit.py` を変更せず再実行し、828件の三次式と2件の7乗式を再構成する。新しいrunディレクトリへ全830レコード、独立監査、ソース・入力・出力のSHA-256を保存する。保存済み証明書のPASS表示だけを転載する処理ではない。

### 4. δ,Jの列挙と条件付き高さ

13≤δ≤200 と指定J範囲で gcd(δ,J)|25（small）、gcd(δ,J)|72（補分岐）を満たす対を列挙する。これは必要条件の表で、対が実現するという主張ではない。

固定Jの候補に対し、適用可能なn²-cまたはn²+2にp²が実際に存在しp²>6n-9であると確認したときだけ、v18の分岐制約とδ⁴高さを検査する。仮定なしにn<定数δ⁴を使わない。

## 失敗・途中結果・保存

各曲線では有限残差列挙をCASより先に保存し、CASの各段階を原子的にcheckpointする。曲線を別プロセスに隔離し、ハング時はそのプロセス群だけを終了する。ランク計算全体は45分、固定J探索は15分の内部予算とし、ジョブの80分/35分制限より先にartifact保存へ進む。各artifact uploadと集約ジョブは `if: always()`、matrixは `fail-fast: false`。

ジョブ結果が欠けた場合は未着の係数対・未計算を報告する。runner自体の消失やGitHub側の強制取消では、最後のupload前のcheckpointを回収できない場合がある。回収できた結果を成功データに混ぜて完全性を主張しない。

集約ジョブは `permissions: contents: write` と既定の `GITHUB_TOKEN` で、**同じ研究ブランチ**へ生成結果だけを通常commit/pushする。DeepSeekのLeanファイル、既存workflow、master、PRのmerge状態は変更しない。同時更新時はfetch/mergeして最大3回再試行し、force pushしない。結果commitは `[skip ci]` とパスフィルタで再実行を防ぐ。

* 最新概要: `v18_actions_latest.json`（各ファイルSHA、実行URL、完全性）
* 実行別証明書: `v18_actions/<run_id>-<run_attempt>/`
* 完全なログと環境一覧: 各実行のArtifacts（30日保存）
* push拒否でも `v18-final-reports` artifactへ先に保存

リポジトリまたは組織でActionsが無効、ワークフローファイル更新権限が不足、課金枠が停止、あるいはブランチ保護でbotのpushが拒否される場合は、GitHubが実行・保存を拒否する。コード側でそれを成功扱いにしない。個別のworkflowを新設し、手動無効化されている既存の4つのworkflowは有効化しない。

## 計算コードの直接実行（GitHub runner上での切り分け用）

```sh
sage -python scripts/research/v18_compute.py ranks --a-max 20 --out _results
python3 scripts/research/v18_compute.py fixed-j --n-max 1000000 --out _results
python3 scripts/research/v18_compute.py lcm --out _results
python3 scripts/research/v18_compute.py auxiliary --out _results
python3 scripts/research/v18_report.py --input _results --run-key manual-1
```

軽量回帰テスト: `python3 -m unittest discover -s scripts/research -p 'v18_test.py' -v`。
