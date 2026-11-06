# v16向け追加研究：立方因子の素数を指定素数・余因子から分離する

状態：進行中。DeepSeekが選んだ候補の範囲点検・Lean検証を進める作業記録であり、v16完成の宣言ではない。
元の四変数方程式と、固定した最終2定理は未解決。

## DeepSeekが選んだ候補

Let w,p,a,i,Q,r be natural numbers. Assume p is prime, 1 ≤ a, i = w * p^a + 2, 0 < Q, 0 < r, Q divides i * (i - 1), Q divides r^3, and Q does not divide r^2. Then there exists a prime q such that (q^3 divides i or q^3 divides i - 1) and (q = 2 or Nat.Coprime q (w * p)). Equivalently, the v15 cube obstruction in this branch is either the special prime 2 or an odd prime cube supported entirely outside the prescribed base p and the cofactor w.

これは、v15の必須立方因子を i=w*p^a+2 の族に結び付ける条件付きの命題。
Qがr³を割るがr²を割らないという仮定を使う。その仮定自体を元の方程式から導くv15のPell議論までLean形式化したことにはならない。
素数2の場合と、w*pの外に新たな奇素数の立方因子が現れる場合は残る。
したがって、この必要条件だけで30余因子の族や元の方程式全体を排除したとは扱わない。

## 検証済みの出発点

- v15の資料はPR #1の d5b90b2772516860cedc30d3cbbd14f2d3614e35 から取得。
- manifestの17記録のサイズ/SHAを照合。
- Pell生成・独立監査をこの環境で再実行：25係数対、188点、22分岐の合同式排除、残存0。定数の有理数6比較もPASS。
- これらの数値検算は、v15の一般記述証明のLean検証ではない。
- v16開始前のDeepSeek作成証明は52定理。依存元を含む15モジュールが実Lean検査PASSで、最新のCFVerifierBridgeも61c53b790ee26dbeafb3b78c27c609d51d06a562に保存済み。

## 保存する証拠

研究提案と訂正は V16_DEEPSEEK_RESEARCH_PROPOSAL.json、v15の再検証は v15_deepseek_handoff_check.json。
実際のLean結果はv10_formal/deepseek_generation_checks.jsonとadditional_kernel_check.json、自律実行の最新状態はDEEPSEEK_GOAL_PROGRESS.mdを参照する。
候補の文章、同じDeepSeekの範囲点検、実Lean通過、GitHub保存を区別する。

## 現在の範囲点検結果

候補は条件付きの記述として提案されたが、既存の最終目標への範囲点検では未採用となった。
Q∤r²を元の二項係数の等式から導く接続がLeanでは未完了で、提案した補題だけでは最終目標を放電できない。
この不足をDeepSeekへ返し、同じ固定目標を保って次の数学的な修正・接続・形式化を本人に選ばせる。
また、研究提案にあった「kappa>=q と log(i)<28*kappa からqの下限が出る」という推論は撤回・訂正済み。そのような下限を成果として主張しない。
元の候補のLean証明が成功したとは扱わない。

## 追加の形式化と手法研究（2026-11-06 JST）

初期提案の後、DeepSeekは元の式との接続を分解して実際に進めた。
ThirtyCofactorInputs、ThirtyCofactorSecondDivisor、ThirtyCofactorPrimeSeparation、
ThirtyCofactorQDivisibility、ThirtyCofactorCubePrimeExtractionの5モジュール・15定理が
実Lean検査を通過しGitHubへ保存された。既存分との合計は67定理、依存元を含む20モジュール。
元の式からQ|r³への接続、指定素数・余因子との素数分離、
Q|r³かつQ∤r²からの素数立方因子の抽出が入った。
Q∤r²を元の式から排除する全Pell議論と、固定した最終目標は未完了。

ユーザーの追加依頼により、数学研究の方法自体もDeepSeekが仮説・実験・評価する。
DEEPSEEK_METHOD_RESEARCH.md/.jsonに本人が選んだ手法と実測を保存する。
最初の実験は、有限区間被覆を証明書として組み立てる手法を、
既に固定済みのThirtyCofactorPellCoveringへ適用するもの。
別候補は、正確な不足約数deltaへ障害を局所化する数学的戦略。
両方とも手法の一般的有効性が証明されたとは扱わず、実際の固定型・Lean結果・基準履歴に結び付けて評価する。
