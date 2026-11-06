# v10の追加形式化：回復約数の積と正規化した平方合同式

既存の `ValuationRecovery.lean` を出発点に、数学ノート
`v10_valuation_recovery.md` の未形式化部分2点を追加した。
元の方程式全体の解決や、新しい数学定理の発見を主張するものではない。
以前の実行記録・版別manifestは変更していない。

## 回復約数と不足分の積

`RecoveredDivisor.lean` は任意の自然数A、Xについて、既存の
`recoveredExponent` を使い

\[
B=\prod_{p\mid A}p^{\mathrm{recoveredExponent}(v_p(A),v_p(X))},
\quad E=A/B
\]

を定義する。以下を一般の素数の有限積について証明する。

- `recoveredDivisor_dvd`：BがAを割る。
- `recoveredDivisor_dvd_cube`：X、rが非零かつAがr(X+r²)を割るなら、Bがr³を割る。
- `gcd_dvd_recoveredDivisor`：A、Xが非零ならgcd(A,X)がBを割る。
- `recoveredDefect_dvd_old_defect`：同じ非零条件でEがA/gcd(A,X)を割る。
- `recoveredDefectProduct_eq_recoveredDefect`：ノートの不足指数d_pによる積とE=A/Bが一致する。
- `original_recovers_divisor`：A.choose k=X+k²から直接適用でき、r=min(k,A−k)の両分岐を含む。

素因数の個数、指数、Aの大きさに上限を置かない。
不足分の積と商の一致にはA≠0、gcdを含む比較にはA≠0かつX≠0を要求する。
解析的な高さ上限や有限領域の証明書を仮定しない。

## 正規化した平方合同式

`NormalizedCancellation.lean` は素数pについてe=v_p(r)、a=v_p(A)とし、
X≠0、r≠0、A|r(X+r²)、3e<aから

\[
v_p(X)=2e,\qquad \gcd(p,r/p^e)=1,
\]

\[
\boxed{p^{a-3e}\mid X/p^{2e}+(r/p^e)^2}
\]

を証明する。最後の整除が、u=r/p^e、v=X/p^{2e}に対する
u²≡−v (mod p^{a−3e})の自然数による定式化である。
`original_normalized_square_congruence` は元の外側二項係数の式からの直接適用である。

このモジュールは、ユーザーが送信を許可した既存の
`ValuationRecovery.lean` をMistral APIの `deepseek-v4-1-flash-1017` に渡して
証明案を生成し、Leanの実エラーを返して修正した後、この環境で残りを修正した。
APIが返した文章やコードを、そのまま検証済みとして扱ってはいない。
`RecoveredDivisor.lean` はこの環境内で作成した。

## DeepSeekだけによる追加の証明生成

続く3モジュールは、証明の作成・エラー修正をすべて
`deepseek-v4-1-flash-1017` に担当させた。ホスト側は固定した定理文への
組み込みとLeanの実行を行い、証明本文の手動編集はしていない。

- `LocalSquareRecovery.lean`：4定理。正規化した平方合同式が解を持たない場合、
  臨界素数でv_p(r)≥t+dとなり、p^{v_p(A)}がr³を割ることを証明する。
  A.choose k=X+k²からの直接適用も含む。
- `CriticalPrimeCRT.lean`：3定理。λがp単元ならp^d|u(u²+λ)から
  p^d|uまたはp^d|(u²+λ)へ分岐する。有限個の互いに素な法について、
  CRTの区間内での存在・一意性と、複数の平方値合同式を1剰余へまとめる一般補題を証明する。
- `CFApproximationCore.lean`：5定理。行列式が+1・−1の両方で整数係数表示の
  存在・一意性を証明し、正の分母q、Q、N、Q≤q<N、近似誤差<3/(2q²)、
  収束分数の誤差<1/Nから|pQ−qP|<5/2を導く。整数の場合は高々2となり、
  対応する前の収束分数の係数bについて|b|≤2が従う。

局所平方非剰余からの回復と、一般のCRTの集約部分を形式化した段階である。
全臨界素数の剰余クラス数の上限、平方根の持ち上げ、原問題の全条件との
接続までを一括して証明したとは主張しない。

後続の `GeometricReduction.lean` では、有理点の前後の座標写像、合成の恒等式、
Weierstrassモデルの判別式と非特異性、j=0、研究曲線への適用を9定理で確認した。
この9定理の証明本文・修正もDeepSeekが担当し、幾何学の定義と定理文には
ホスト側の点検・訂正が入っている。[幾何学的還元の説明](../GEOMETRIC_APPROACH.md) を参照。
さらに `GeometricDescent.lean` で古典的3-isogeny公式の座標部分を6定理として検証した。
像の曲線方程式、判別式、元の枝の像座標、Pell型の必要等式を含む。
群準同型性、次数3、降下の完全性、階数、全有理点は未証明である。
[座標公式の検証範囲](../GEOMETRIC_DESCENT_COORDINATES.md) を参照。
後続の `CFCoefficientRanges.lean` は係数範囲・既約な零係数分岐・候補集合の対応・要素数65以下の6補題を追加する。
[係数範囲の仮定と未接続部分](../CF_COEFFICIENT_RANGES.md) を参照。
今回のDeepSeek作成の証明本文は6モジュール・33定理である。

## 連分数の再検証と、まだ残る仮定

PR内の `v9_cf_certificates/S01.json`〜`S12.json` と検証コードをコピーし、
元のファイルを変更せずに全件の厳密検証を再実行した。
5,214曲線、4,877,566個の係数、25,394,330件の既約分数を確認し、残存点は0。
入力証明書とソースのハッシュが元の資料と一致することも確認した。
今回の実結果を `cf_current_revalidation.json` と `cf_current_revalidation.txt` に保存する。

これはPythonによる整数演算の検証であり、Leanカーネルによる全証明書の検証ではない。
`CFApproximationCore` は誤差評価と|b|≤2までを形式化するが、
小分母側a∈[-1,4]、大分母側a−b*a_next∈[-3,3]、候補集合の要素数65以下は
`CFCoefficientRanges` で明示仮定の下に形式化した。実収束分数データの供給、
1つの候補被覆定理、各収束分数区間の選択と円筒区間認証、全曲線の候補評価はまだ接続していない。
従って、30余因子の最終定理から連分数部分の仮定を外したとは主張しない。

`deepseek_generation_checks.json` に生成試行・コンパイル結果・ソースハッシュ・
意味の点検結果を記録する。手順の出典と制約は
[研究ワークフロー](RESEARCH_WORKFLOW.md) に記す。

## 再実行

Lean 4.35.0、mathlibコミット
`56a005855ea17e0b0958f73ec801ae140b0a1679` を使用する。
そのmathlib作業ディレクトリで、次を実行する。

```sh
lake env python3 /absolute/path/v10_formal/check_additional_formalization.py
```

このスクリプトは依存元 `ValuationRecovery.lean` と存在する追加モジュールを
新しい一時ディレクトリへ順にコンパイルする。既存の.oleanに依存せず、
コンパイラの終了コードと実出力を保存する。元の証明のログは上書きしない。

- `additional_kernel_check.json`：今回の終了コード、ツールバージョン、各ソースとログのSHA-256。
- `*.additional_check.txt`：対応する実コンパイラ出力と公理依存。

追加モジュールは証明穴、独自公理、ネイティブ実行による決定手続きを使わない。
表示された公理依存はLean/mathlib標準の `propext`、`Classical.choice`、`Quot.sound` のみ。
独立プロジェクトでの `lake build` は今回の実行方法ではない。

## 残る形式化

平方非剰余で改善した約数を積へまとめる部分、CRTの全候補数と原問題への完全な接続、連分数による完全性、
解析的な高さ上限、30余因子・94余因子の全領域は今回の対象外である。
進行中だったPR外のファイルの内容を復元した、という主張でもない。
