# v11：実行したLean証明の範囲

`ArithmeticCore.lean` は Lean 4.35.0 と、mathlib
`56a005855ea17e0b0958f73ec801ae140b0a1679` で実際に実行し、
終了コード0を確認した。主要7定理と補助1定理を含む。

| 定理 | 実行した主張 |
|---|---|
| `cubic_difference_dvd_product` | gcd(p,q)=1、D+a p³=Tq³、D|Tq なら D|aT。新しい連分数ふるいの一般補題。 |
| `divisor_of_top_dvd_choose` | d|n、gcd(d,k)=1 なら d|C(n,k)。 |
| `four_dvd_choose_of_odd_bottom` | 上側添字が4の倍数、下側添字が奇数なら、二項係数は4の倍数。 |
| `binary_defect_gain` | x≥3 の下で、偶数付値なら不足指数は高々 max(alpha−6,0)（Leanの自然数減算）、奇数なら0。 |
| `integer_interval_span_four` | 長さ4未満の実区間に入る任意の2整数の差は高々3。最大4個という計数部分。 |
| `integer_interval_unique` | 長さ1未満の実区間に入る整数は一意。 |
| `cube_interval_constants` | 平方値区間の幅、512の閾値、ゼロ剰余の支持に使う正確な整数定数。 |

補助定理は、上側添字が「下側添字×二項係数」を割る恒等式である。
一般補題の仮定を省略して、元の問題全体を形式化したという意味ではない。

## 実行記録

実際のコマンド、実行セッション、終了コード、ソースとログのハッシュは
[arithmetic_kernel_check.json](arithmetic_kernel_check.json) に記録する。
Leanが出力した公理依存の表示は
[arithmetic_kernel_check.log](arithmetic_kernel_check.log) に、そのまま保存した。

`sorry`、`admit`、独自の公理、`native_decide` は使っていない。
公理依存は通常の `propext`、`Classical.choice`、`Quot.sound` の範囲である。
`.olean` バイナリは配布に含めない。

このフォルダの `lakefile.toml` は再現用の固定依存を示す。
実際の確認は準備済みの同一バージョンmathlib環境から `lake env lean`
を直接実行したもので、この独立フォルダで `lake build` を実行したという
主張ではない。

mixed-structure担当が8定理の仮定・結論と数学上の対応を独立に点検し、
同じソースハッシュでPASSを確認した。これは独立したAI監査である。

## 未形式化の範囲

二進桁の3回の繰り上がりそのもの、素数ごとの結果を積へまとめる全体、
CRTによる平方値の唯一の剰余、実数の三乗根を使う区間幅の全導出、
連分数近似の完全性、804曲線の全計算、余因子の有限領域の完全性と全証明書、
局所単位の一般公式、n−3側の新しい族の全証明は、このLeanソースに
形式化していない。これらは各ノートの数学的証明と独立した厳密計算による。

関連する数学ノートは
[混合素因数の平方値CRT](../v11_simultaneous_square_interval.md)、
[不足分13の排除](../v11_effective_defect_cf.md)、
[余因子の一括排除](../v11_cofactor_extension.md) を参照。
