# Math OS Prototype

小さい言語モデルを「答えを全部出す本体」ではなく、数学ツールへ仕事を渡すコンパイラとして使うための最小プロトタイプです。

## 目的

このプロトタイプは、数学問題を次の流れに分解します。

```text
自然言語の問題
  -> TinyRouter: タスク分類
  -> MathIR: 型付き中間表現(JSON)
  -> TypedSemanticGraph: 対象・射・制約・query
  -> ConstraintIR / VerifierGate: 型・単位・対象・query整合性チェック
  -> ToolCall: SymPy / 幾何エンジン / Lean 風バックエンド
  -> 実行できるものだけ実行、残りはコマンドとして提示
```

巨大LLMに全推論を持たせるのではなく、LLM相当の部分を「分類・IR生成・コマンド生成」に限定する設計です。

`TypedSemanticGraph` は圏論風の核表現です。数学対象を `SemanticObject`、構成・変換・観測を `SemanticMorphism`、条件を `Constraint`、求めるものを `SemanticQuery` として表します。算数文章題の `Quantity(value, unit, owner, object, state)` は、この核では `observe(owner, object, state) -> Count[object]` という観測射に持ち上げられます。幾何・整数論・確率・解析も同じ `objects + morphisms + constraints + query` 形式に落とします。

## 実行例

```powershell
python math_os_prototype\math_os.py --demo
```

ローカルツール検出:

```powershell
python math_os_prototype\math_os.py --tool-status
```

ブラウザUIを起動:

```powershell
python math_os_prototype\web_app.py --port 8765
```

起動後に `http://127.0.0.1:8765/` を開くと、問題入力欄から7層パイプラインへ投げて返答を受け取れます。

7層パイプラインをまとめて実行:

```powershell
python math_os_prototype\math_os.py --full-pipeline "平面上に一辺$\sqrt3$の正方形を固定する.一辺$\sqrt2+\sqrt6$の正三角形を, この正方形を含むように自由に動かすとき, 正三角形の通過領域の面積を求めよ."
```

Stack Exchange APIで類似問題検索も許可する場合:

```powershell
python math_os_prototype\math_os.py --full-pipeline --live-retrieval "曲線 y = t*x - t^2 の包絡線を求めよ。"
```

Wolfram/SymPyなどの実験ツールも実行する場合:

```powershell
python math_os_prototype\math_os.py --full-pipeline --external-tools "正の整数 n について n^2 = 9 を満たすものをすべて求めよ。"
```

デフォルトは cold mode です。ベンチに合わせた旧専用アダプタは使いません。旧アダプタを明示的に使う場合だけ、次のフラグを付けます。

```powershell
python math_os_prototype\math_os.py --full-pipeline --allow-specialized "..."
```

分野分類ベンチマークを実行:

```powershell
python math_os_prototype\math_os.py --domain-benchmark
```

TeX問題集をベンチ:

```powershell
python math_os_prototype\tex_benchmark.py --output math_os_prototype\tex_benchmark_results.json "C:\Users\81808\Downloads\hon3.tex" "C:\Users\81808\OneDrive - 東京理科大学\全問題.tex"
```

Problem Phase Diagram Synthesis を実行:

```powershell
python math_os_prototype\problem_phase_synthesis.py --limit 1560 --top-k 12 --prefix floor_log_phase0_full
```

床関数・積分・極限の問題族を生成し、`invalid_domain` / `divergent` / `finite_closed` / `vanishing` の相へ分類します。結果は `math_os_prototype\problem_synthesis\` にJSON/JSONL/Markdownで保存されます。

Problem Repair Loop を実行:

```powershell
python math_os_prototype\problem_phase_synthesis.py --repair --limit 240 --repair-limit 80 --top-k 8 --prefix floor_log_repair0
```

悪い候補を `fix_domain` / `move_to_finite_phase` / `increase_nontriviality` で修理し、有限非零の閉形式問題へ移せるかを記録します。これは「一発生成」ではなく、作問候補を検証して条件を直す最小の自己修正ループです。

通過領域・包絡線テーマを実行:

```powershell
python math_os_prototype\problem_phase_synthesis.py --theme geometry --limit 96 --top-k 8 --prefix geometry_sweep_phase0
```

曲線族 `y = a*t*x + b*t^2 + c*x + d` から、同じ核オブジェクトに対して `region` と `envelope` の観測を切り替えます。`region` は実数パラメータの存在消去、`envelope` は `resultant(F, dF/dt)` として既存Geometry DSLに渡します。

幾何テーマのRepair Loop:

```powershell
python math_os_prototype\problem_phase_synthesis.py --theme geometry --repair --limit 120 --repair-limit 40 --top-k 8 --prefix geometry_sweep_repair1
```

幾何側では、答え文字列ではなく `x,y` の多項式正規形で同値判定します。例えば包絡線 `-x**2 + 4*y = 0` は `x**2 - 4*y = 0`、通過領域 `y <= x**2/4` は `x**2 - 4*y >= 0` に正規化されます。

生成された閉形式問題は `curriculum_items` として、入力TeX、Geometry DSL、期待解、代数正規形、戦略タグ、証明義務を持ちます。これは問題を覚えさせるためではなく、Parser / Router / Strategy / Verifier の回帰テストや自己生成カリキュラムとして解く側へ戻すための形式です。

生成カリキュラムを solver benchmark に戻す:

```powershell
python math_os_prototype\synthetic_curriculum_benchmark.py --modes tex,dsl,tex_mutation,full_tex --output math_os_prototype\problem_synthesis\synthetic_curriculum_benchmark1.json
```

このベンチは、生成済みの `curriculum_items` を通常のMathOS solverへ初見入力として渡し、答え文字列ではなく代数正規形で採点します。`dsl` はbackendだけの検証、`tex` は通常の生成文、`tex_mutation` は言い換え、`full_tex` は `\documentclass` 付きTeX文書です。

MathOS-CreativeBench v0.2 を実行:

```powershell
python -B -m math_os_prototype.creative_benchmark `
  --mathos-report math_os_prototype\problem_synthesis\geometry_sweep_repair1.json `
  --output math_os_prototype\problem_synthesis\creative_benchmark_v0.json
```

許諾済み人間問題を比較対象に加える場合は、1行1 JSON のファイルを
`--human-jsonl` で渡します。必須フィールドは `record_id`, `domain`,
`task`, `statement_tex`, `rights_basis` です。`rights_basis` は
`self_authored`, `permission`, `licensed`, `public_domain`,
`research_excerpt` のいずれかでなければ読み込みを拒否します。
ただし `research_excerpt` は少数の方法検証用であり、60問の本評価には使いません。

```json
{"record_id":"human-001","domain":"geometry","task":"region","statement_tex":"...","rights_basis":"permission","difficulty":{"level":"B"},"verification":{"status":"verified"}}
```

盲検評価は `naturalness`, `elegance`, `surprise`, `pedagogical_value` を
各1--5で記録し、`--ratings-jsonl` で読み込みます。人間評価がない状態では、
成立率・構造重複・修正履歴のみを報告し、創造性総合点は出しません。研究仕様は
`creative_benchmark_protocol.md` に固定しています。

60問を固定した本評価では件数ゲートも有効にします。59問以下でもレポートは
保存されますが、終了コードは `2` となり、本評価完了とは扱われません。

```powershell
python -B -m math_os_prototype.creative_benchmark `
  --human-jsonl rights-cleared-human60.jsonl `
  --expected-human-count 60 `
  --require-complete-human-set `
  --output math_os_prototype\problem_synthesis\creative_benchmark_human60.json
```

外部問題の検証状態は `valid / invalid / unknown` の三値で集計します。
未検証を誤って無効問題として数えず、validity rate の分母は判定済み問題だけです。

本人作成の `itembox` 形式TeX問題集から、解答編を混入させず固定54問を作る場合:

```powershell
python -B -m math_os_prototype.creative_tex_corpus `
  --input "C:\Users\81808\OneDrive - 東京理科大学\全問題.tex" `
  --source-id all-problems-20260722 `
  --rights-basis self_authored `
  --limit 54 `
  --output math_os_prototype\problem_synthesis\all_problems_selfauthored54.jsonl `
  --report math_os_prototype\problem_synthesis\all_problems_selfauthored54_report.json
```

2回目以降は `--fixed-selection-report` に最初のレポートを渡します。これにより
DomainRegistryやLifterを変更しても同じ54問を評価し、改善に伴う再抽出・再標本化を
防ぎます。レコードIDは出題番号ではなく、出現順と問題本文のSHA-256から作るため、
重複した `問題49` なども衝突しません。

固定54問と現行作問器を比較する場合:

```powershell
python -B -m math_os_prototype.creative_benchmark `
  --mathos-report math_os_prototype\problem_synthesis\geometry_sweep_repair1.json `
  --human-jsonl math_os_prototype\problem_synthesis\all_problems_selfauthored54_lift_vocab1.jsonl `
  --expected-human-count 54 `
  --expected-system-count 54 `
  --output math_os_prototype\problem_synthesis\creative_benchmark_selfauthored54_lift_vocab1.json
```

2026-07-22時点の固定観測は
`problem_synthesis/selfauthored54_pdca_report.md` に記録しています。

面積・極値・極限・体積・素数制約を、backend検証と再lift検証の二重ゲートで
54問生成する場合:

```powershell
python -B -m math_os_prototype.atlas_problem_synthesis `
  --limit 54 `
  --output math_os_prototype\problem_synthesis\atlas_verified54.json
```

各生成チャートは `parameter space -> renderer` と `parameter space -> backend`
を分離しています。生成TeXを通常の意味解析器へ戻し、期待した
`LiftCertificate.family_id` が再現されない候補は出力しません。

固定人間54問と同一LiftCertificate内で比較:

```powershell
python -B -m math_os_prototype.creative_benchmark `
  --mathos-report math_os_prototype\problem_synthesis\atlas_verified54.json `
  --human-jsonl math_os_prototype\problem_synthesis\all_problems_selfauthored54_lift_match1.jsonl `
  --expected-human-count 54 `
  --expected-system-count 54 `
  --output math_os_prototype\problem_synthesis\creative_benchmark_atlas54_vs_selfauthored54.json
```

2026-07-23時点で両側54問、system成立率54/54、共有Lift family 8、
盲検ペア31組です。人間評価前なので創造性総合点は出しません。詳細は
`problem_synthesis/atlas54_comparison_report.md` に記録しています。

内積空間へ一般化した拡張版:

```powershell
python -B -m math_os_prototype.atlas_problem_synthesis `
  --limit 72 `
  --output math_os_prototype\problem_synthesis\atlas_verified72.json
```

拡張版では、平方完成済みのスカラー最小値チャートを正定値二次形式へ置換し、
相関係数を中心化した `L^2(P)` 内積の正規化として再定義しました。
Frobenius内積、直交射影、内積制約極値、正規化内積極限、定常過程の
自己相関関数も同じ内積空間の核から生成します。結果と評価企画は
`problem_synthesis/atlas72_research_plan_ja.md` に記録しています。

現時点の `geometry_sweep_repair1` では、37問を4条件で合計148件に展開し、148/148が正規形一致しました。これは通過領域・包絡線・媒介変数消去・二次範囲という同一抽象構造では、作問から解く側への接続が成立していることを示します。

全分野PDCAとして、生成カリキュラムから抽出した核操作を公開ベンチ solver に戻す実験も実行しています。固定265問スライスでは `172/252 = 68.25%` から `248/252 = 98.41%`、1130問スケールでは `431/1090 = 39.54%` から `502/1090 = 46.06%` へ改善しました。詳細は `pdca_allfield_public_report.md` と `pdca_allfield_after7_*.json` を参照してください。

公開ベンチPDCAを再実行:

```powershell
python math_os_prototype\public_benchmark.py --gsm8k 50 --math-per-config 5 --svamp 50 --asdiv 50 --aqua 20 --multiarith 30 --mawps 30 --output math_os_prototype\pdca_allfield_after7_265.json
python math_os_prototype\public_benchmark.py --gsm8k 300 --math-per-config 20 --svamp 200 --asdiv 150 --aqua 100 --multiarith 120 --mawps 120 --output math_os_prototype\pdca_allfield_after7_1130.json
```

Geometry DSLで厳密に渡す場合:

```powershell
python math_os_prototype\math_os.py "task envelope; family y = t*x - t^2; param t"
python math_os_prototype\math_os.py "task region; family y = t*x - t^2; param t in R"
python math_os_prototype\math_os.py "task locus; x = t + 1; y = 2*t; param t"
```

自然文からGeometry DSLへ変換して実行する場合:

```powershell
python math_os_prototype\math_os.py "tを実数として、曲線 y = t*x - t^2 の通過領域を求めよ。"
python math_os_prototype\math_os.py "曲線 y = t*x - t^2 の包絡線を求めよ。"
python math_os_prototype\math_os.py "(x,y)=(t+1,2t) で表される点の軌跡を求めよ。"
```

LaTeXコードを直接渡す場合:

```powershell
python math_os_prototype\math_os.py '\begin{problem}$t\in\mathbb{R}$ とする。曲線 \( y = tx - t^2 \) の通過領域を求めよ。\end{problem}'
```

PowerShellでは `$t` が変数展開されるため、LaTeXを直接渡すときはシングルクォートを使ってください。長い問題は `--latex-file` の方が安全です。

`.tex` ファイルから読む場合:

```powershell
python math_os_prototype\math_os.py --latex-file math_os_prototype\sample_region.tex
```

Wolframが入っている環境で追加検証まで実行する場合:

```powershell
python math_os_prototype\math_os.py --external-tools "tを実数として、曲線 y = t*x - t^2 の通過領域を求めよ。"
```

包絡線だけ試す場合:

```powershell
python math_os_prototype\math_os.py "包絡線 y = t*x - t^2 を求めて。parameter t"
```

IRをJSONで見る場合:

```powershell
python math_os_prototype\math_os.py --json "Minkowski sum [(0,0),(1,0),(1,1),(0,1)] + [(0,0),(2,0),(0,1)]"
```

ツール呼び出しを実行せず、計画だけ見る場合:

```powershell
python math_os_prototype\math_os.py --no-execute "Leanで n + 0 = n を証明したい"
```

## いま動くこと

- Seven-layer reasoning pipeline:
  - Domain Registry: 問題を数学分野別IRへ分類し、推奨ツールと検証方針を出す
  - Parser: LaTeX/自然文/DSLをMathIRへ変換
  - Structural Parser: 問題を変数・制約・関係式・操作・量・ツール候補へ分解
  - FormalIR Compiler: TeX中心の日本語問題を型付き完全括弧形式へ変換し、標準日本語へ逆翻訳
  - Memory/Retrieval: ローカル解法メモリと任意のStack Exchange検索
  - Strategy Planner: 解法候補を複数生成
  - MathSearch: 汎用の実験アクション木を作り、SymPy/Wolfram等で検証
  - Simulation Engine: 数値・幾何実験の観察と検証候補を出す
  - Tool Executor: SymPy/Wolfram/幾何エンジンへ委譲
  - Verifier: ツール実行状況と専用ソルバー結果を検査
  - Explanation Builder: 人間向けの短い説明へ戻す
- Geometry DSL:
  - `task envelope; family y = f(x,t); param t`
  - `task region; family y = f(x,t); param t in R`
  - `task region; family y = f(x,t); param t in [a,b]`
  - `task locus; x = f(t); y = g(t); param t`
- 包絡線: `y = f(x, t)` を `F = 0` と `dF/dt = 0` に変換し、SymPyのresultantで媒介変数を消去
- 通過領域: 実数全体の二次式族なら、存在条件を不等式に落とす
- 自然文フロントエンド:
  - `曲線 y = ... の包絡線`
  - `tを実数として y = ... の通過領域`
  - `(x,y)=(...,...) の軌跡`
- LaTeXフロントエンド:
  - `\(...\)`, `\[...\]`, `$...$` の数式抽出
  - `\frac`, `\sqrt`, `\mathbb{R}`, `\in`, `\leq`, `^` の正規化
  - `tx` や `2t` の暗黙の掛け算を `t*x`, `2*t` へ正規化
- Containment geometry:
  - 固定正方形を含む可動正三角形の通過領域面積
  - 例: 一辺 `sqrt(3)` の正方形、一辺 `sqrt(2)+sqrt(6)` の正三角形
- Specialized field adapters:
  - `NumberTheoryIR`: `m`週間と`n!`秒が等しい問題を階乗の割り切りへ変換
  - `GeometryIR`: 等半径2円の共通部分面積の漸近差を座標幾何式で処理
  - `ProbabilityIR`: カード平均の相加平均・相乗平均の相関係数をモーメント計算へ変換
  - `InequalityIR`: 証明前に小整数反例探索を走らせ、見つからない場合は証明扱いしない
- Tool adapters:
  - SymPy: 常用のprimary CAS
  - Wolfram: `wolframscript` を検出し、`Reduce` / `Eliminate` を実行
  - Z3: Python packageを検出
  - Shapely: Python packageを検出
  - Lean: `lean` / `lake` を検出
- ミンコフスキー和: 2つの凸多角形の頂点和を作り、凸包を返す
- 代数方程式: 簡単な `solve ... for x` をSymPyに渡す
- 微分: 簡単な式をSymPyに渡す
- Lean: 実行はしないが、Lean/Mathlibへ渡すためのstubと検証コマンドを出す
- Vision geometry: 画像からGeometry IRを作る予定のバックエンドとして計画を出す

## Cold Mode と解法木

このプロトタイプでは、評価用問題を覚えた専用検出器に頼らない `cold mode` をデフォルトにしています。代わりに、問題を次の形へ落とします。

```text
StructuralIR(
  variables,
  relations,
  constraints,
  operations,
  quantities,
  tool_affordances
)
```

そこから `MathSearch` が汎用アクションを作ります。

```text
generic_sympy_solve
generic_counterexample_search
generic_wolfram_experiment
generic_integer_search
generic_elimination_model
generic_probability_state_space
```

実行結果は `solution_graph` として返します。これは、検索候補・構造化状態・実験アクション・検証結果を木として保存するための形式です。モデルのパラメータに解法を詰め込むのではなく、外部メモリに「検証済みの解法木」として残すための土台です。

例:

```powershell
python math_os_prototype\math_os.py --json --full-pipeline --external-tools "正の整数 n について n^2 = 9 を満たすものをすべて求めよ。"
```

この例では、SymPyが `n = 3` を制約付きで検証し、Wolfram `Reduce` も `n == 3` を返します。

## FormalIR Compiler

`formal_language.py` は、入力を「数学コンパイラ」として扱う層です。自由文章を直接解くのではなく、TeXで確定した数式と有限個の数学日本語テンプレートから、完全括弧形式を作ります。

例:

```text
実数 $x,y$ が $x+y=5$ かつ $xy=6$ を満たすとき、$x^2+y^2$ を求めよ。
```

内部形式:

```lisp
(problem
  (declare x Real)
  (declare y Real)
  (meta a Real)
  (assume
    (and (= (+ x y) 5) (= (* x y) 6))
  )
  (goal
    (forall ((x Real) (y Real))
      (implies
        (and (= (+ x y) 5) (= (* x y) 6))
        (= a (+ (^ x 2) (^ y 2)))))
  )
)
```

同時に、MathOSが理解した意味を標準日本語として返します。UIでは `FormalIR` 欄に `type_checked / ambiguous / needs_review` とS式が表示されます。

現在対応している問いの型:

```text
値を求めよ
すべて求めよ
存在範囲/範囲を求めよ
証明せよ/示せ
```

曖昧性として、`log` の底、囲まれる領域の連結成分、型未確定変数などを検出します。これは最終的には、ユーザーがUI上で修正できる形式欄にするための土台です。

## Web Solution Pipeline

`--live-retrieval` を付けると、Math StackExchange検索結果を候補解法として扱います。

```text
WebSolutionFetcher
  -> StackExchange APIから質問本文・高スコア/accepted回答を取得
SolutionStepParser
  -> 回答本文を assume / transform / substitute / apply_theorem / conclude に分解
StepVerifier
  -> 抽出できた関係式を SymPy / Wolfram / 小ケース探索で検査
SolutionGraph
  -> 検索候補、解法ステップ、検証結果を木として保存
```

実行例:

```powershell
python math_os_prototype\math_os.py --json --full-pipeline --live-retrieval "prove that sqrt(2) is irrational"
```

現段階では、Webから回答本文を取得してステップ木にはできます。ただし自然文証明の全ステップをLeanで形式検証するところまでは未接続です。`StepVerifier` は、機械的に読める等式・不等式・小ケース検査だけを成功扱いし、読めない自然文推論は `planned` / `unverified` として残します。

## Domain Registry

`domain_registry.py` は、未登録問題でも最初に「どの数学分野として扱うべきか」を決める層です。答えを直接出すソルバーではなく、次の情報を返します。

```text
DomainIR(
  domain,
  operation,
  objects,
  symbols,
  target_tools,
  methods,
  verification,
  retrieval_queries
)
```

現在の登録分野:

```text
algebra, linear_algebra, calculus, real_analysis, complex_analysis,
geometry, convex_geometry, number_theory, combinatorics, graph_theory,
probability, statistics, optimization, differential_equations,
inequalities, functional_equations, topology, formal_proof
```

小ベンチマークは `domain_benchmark.jsonl` にあります。これは「全分野を解ける」ことのテストではなく、まず適切な分野・道具・検証方針へ振り分けられるかを見るテストです。

## TeX Benchmark

`tex_benchmark.py` はTeX原稿から問題を抽出し、各問題について次を記録します。

```text
domain, route, intent, strategy, verification, answer, status, warning
```

集計では、全体だけでなく分野別の進捗も追います。

```text
by_domain_status
domain_success_rates
```

`status` は大きく次の意味です。

```text
verified_answer: 型付き実行と内部証明書が成功し、答えまで返した
verified_no_answer: ツール実行は完了したが答えとしては空
partial_plan: 分野分類・戦略立案まではできたが、実行ソルバー未接続
error: パイプライン実行エラー
```

高度な問題では断片的なCAS実行を成功扱いしないため、非代数分野に対する単純な `sympy.solve` 結果は `partial_plan` として扱います。

2026-08-20の `全問題.tex` 85問ベンチでは、外部LLM・ウェブ検索・旧benchmark専用adapterを使わず、54問（63.53%）で型付き実行と内部証明書を伴う回答を返しました。開始時の10問（11.76%）から44問改善しています。記録と方法は `docs/mortra1_structural_theorem_pdca_2026-08-20.md` にあります。

この値は正解集とのexact matchではなく、MORTRA内部で回答と証明書の生成が完了した割合です。外部モデルの正答率とは直接比較しません。独立したgold answer監査は別指標として追加します。

## Geometry DSL

自然言語をいきなり完全理解する代わりに、まずは通過領域・包絡線・軌跡だけを専用DSLに落とします。

自然文フロントエンドは `geometry_nl.py` に分離しています。ここは後から小型LLMや分類器に置き換える前提です。下流の `geometry_dsl.py` は厳密なDSLだけを受け取ります。

LaTeXフロントエンドは `latex_frontend.py` に分離しています。ここではTeXを完全解釈せず、問題文と数式を抽出して自然文フロントエンドが読める表現へ変換します。

```text
task envelope
family y = t*x - t^2
param t
```

1行で書く場合:

```text
task envelope; family y = t*x - t^2; param t
```

通過領域:

```text
task region; family y = t*x - t^2; param t in R
```

この例は `exists t in R: y = t*x - t^2` を解析して、`y <= x^2/4` を返します。

有界パラメータでは、今は完全な場合分けまではせず、端点と臨界点の候補に落とします。

```text
task region; family y = t*x - t^2; param t in [0,2]
```

軌跡:

```text
task locus; x = t + 1; y = 2*t; param t
```

## 小型ルーター

`TinyRouter` は単語・キーワード特徴からルートを選ぶ小さな線形モデルです。各「特徴 -> ラベル」の重みを1パラメータとして数えます。

追加学習:

```powershell
python math_os_prototype\math_os.py --train-jsonl math_os_prototype\examples.jsonl --save-weights math_os_prototype\router.weights.json --demo
```

保存した重みを使う:

```powershell
python math_os_prototype\math_os.py --weights math_os_prototype\router.weights.json "通過領域を消去法で求めたい"
```

## Tool Adapters

`tool_adapters.py` がローカルツールの検出と実行を担当します。

```text
Geometry DSL
  -> SymPyAdapter
  -> WolframAdapter
  -> Z3/Shapely/Lean status
```

通常実行ではSymPyをprimary resultとして使い、Wolframはplanned commandとして結果に含めます。`--external-tools` を付けると、`wolframscript` が見つかった場合にWolframも実行します。Z3/Shapely/Leanは現時点では検出までで、次に実行アダプタを足す対象です。

Wolframの通過領域では、例えば次の形を生成します。

```wolfram
Reduce[Exists[t, Element[t, Reals] && y == t*x - t^2], {x, y}, Reals]
```

## Retrieval

`retriever.py` は、汎化のための最初の層です。デフォルトではネットに出ず、ローカルの解法メモリから「support function」「envelope elimination」「quantifier elimination」などの解法パターンを返します。

`--full-pipeline --live-retrieval` を付けた場合だけ、Stack Exchange APIで類似問題候補を検索します。検索結果はそのまま答えとして信用せず、Strategy Plannerの候補生成にだけ使い、最終的にはCAS/専用ソルバー/Verifierで検査します。

## 次に伸ばすなら

- 自然言語からGeometry DSLへの変換を学習器に置き換える
- 有界パラメータの通過領域を完全なpiecewise不等式へ落とす
- Leanの実行環境がある場合だけ `lake env lean` を実際に呼ぶ
- Mathematica/Wolfram Engineがある場合は `Reduce` / `Eliminate` に接続する
- 図形画像から点・線・円・ラベルを読む小型visionモジュールを追加する
- ルーターをMLPや小型Transformerに差し替え、ただし出力はMathIRに固定する
