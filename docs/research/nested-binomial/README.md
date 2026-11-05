# 入れ子の二項係数方程式の研究記録

\[
\boxed{\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}}
\]

右辺は上下の添字を二乗した二項係数。通常の非負整数の範囲で扱う。

**状態：全体の解の分類は未完了。具体的な解も未発見。**
部分的な無限族の排除と必要条件を記録する。
必要条件を満たすことを、元の式の解であることとは扱わない。

## 読み始める場所

- **[最新：v10 日本語概要](PROGRESS_v10_ja.md)**
- [元の等式からの付値回復、混合素因数のCRT条件、一般の高さ上限](v10_valuation_recovery.md)
- [w/gcd(w,6)≤12 の全30余因子を全素数・全指数で排除](v10_small_cofactors.md)
- [一般の付値回復補題と円分の有限合同計算の実行済みLean検証](v10_formal/README.md)
- [円分因子の小さい剰余環による排除と外部定理依存の縮小](v10_cyclotomic_auxiliary_rings.md)
- [v9 日本語概要](PROGRESS_v9_ja.md)
- [連分数による GCD 不足分 S≤12 の全排除](v9_gcd_defect_continued_fractions.md)
- [任意の固定余因子に対する正確な GCD 公式と有限上限](v9_gcd_structure.md)
- [i=2P^a+2 の全素数・全指数の排除](v9_cofactor_two.md)
- [新しい2,592件の有限算術証明書の Lean 検証](v9_formal/README.md)
- [円分因子の primary trace による全指数の制約](v9_cyclotomic_primary_trace.md)
- [v8 日本語概要](PROGRESS_v8_ja.md)
- [シフト素数冪 i=P^a+2 の完全排除](v8_shifted_prime_power_completion.md)
- [全2,903件の有限算術証明書の Lean 検証](v8_formal/README.md)
- [大きい素数冪因子の一様な分類](v8_composite_dominant_prime_powers.md)
- [一般の共通約数の不足分による高さ上限](v8_gcd_defect_height.md)
- [円分因子7q^aの偶数指数・高次付値の制限](v8_cyclotomic_even_exponents.md)
- [v7 日本語概要](PROGRESS_v7_ja.md)
- [v6 日本語概要](PROGRESS_v6_ja.md)
- [版ごとの研究記録](RESEARCH_LOG.md)
- [新しい共通約数と i-1 が平方自由な場合の完全排除](v6_common_divisor.md)
- [対数幅、R≤12 の排除、候補の疎性](v6_offset_composite.md)
- [素数冪に必要な Wieferich 因子](v6_offset_prime_powers_wieferich.md)
- [円分因子による制限と p²+p+1=7q の完全排除](v6_large_prime_cyclotomic.md)
- [v6 の Lean 検証範囲・実行方法](v6_formal/README.md)
- [v5 日本語概要](PROGRESS_v5_ja.md)
- [v4 日本語概要](PROGRESS_v4_ja.md)
- [ell=1、j=i-3 の区間・付値の証明](v5_offset_three_structure.md)
- [i=3^a の全指数の排除](v5_offset_three_three_power.md)
- [i=jp^3 の一候補への絞り込みと高次合同式](v5_large_prime_localization.md)
- [v5 の Lean 検証範囲・実行方法](v5_formal/README.md)

## 2026年11月5日の追加：v10

ell=1、j=i-3 の枝で、元の等式から A|r(X+r²) を保つと、
α=v_p(A)、x=v_p(X)、e=v_p(r) に対し 3e<α⇒x=2e が必要になる。
特にxが奇数なら、Aのその素数成分は全てr³へ回復する。
回復後の不足分Eは旧Sの約数で、既存の完全なCF結果を移すことで E≥13 が必要となる。
さらに残る各素数について平方合同と零剰余の二択を作り、CRTで同時に扱う。
r=Fu とした商の範囲は u³<229E に収まる。

任意の i=wp^a+2 に対し、底pの大きさを仮定せず、
log i<128w/gcd(w,6)、i<2^(192w/gcd(w,6)) まで一般上限を改善した。
w/gcd(w,6)≤12 の全30余因子は、全素数・全指数で排除を完了した。
理論から得た全983組・955添字を厳密に排除し、別実装でも証明された広い領域
2,423組・2,393添字を証明書なしで再現した。
任意の正確な素数冪因子 q|i−2 について、q≤(i−2)/13 が必要となる。

円分枝では法2・5・7の一様な条件を導き、v9で残ったq=19,31,67を全指数で排除。
q≥241、偶数指数ではq≥463が必要になった。素数pのこの枝での3|a排除は
4元体の短い証明で代替でき、当該結論のThomas–Mignotte依存を除去した。
v7の一般の整数に対する、より広い定理の外部依存はそのまま保持している。

今回は局所付値回復の一般補題自体をLeanで実際に実行し終了0を確認。
円分枝の20個の有限算術定理も実行済み。積全体、平方合同、CRT、CF移植、
解析的高さ評価、30余因子の有限領域全体まで全形式化したとはしない。
詳しくは [v10 日本語概要](PROGRESS_v10_ja.md) と
[v10_manifest.json](v10_manifest.json) を参照。

## 2026年11月5日の追加：v9

ell=1、j=i-3 の枝全体に対し、A=C(i,3)、X=C(i²,6i−9)、
S=A/gcd(A,X) とすると S≥13 が必要だと証明した。
S≤12 なら理論的に残る全5,214曲線を連分数の完全な近似分類で扱い、
全係数を保存した証明書と別実装の再計算で候補0件を確認した。
第一添字の上限まで整数を順番に走査していない。

一般の i=wp^a+2 では、p∤w、p^a>4w のとき
D_w=C(6w,2w)/gcd(C(6w,2w),6)、c_w=w/gcd(w,6) を用いて
v_p(S)=v_p(D_w)、S|c_w p^v_p(D_w) を証明した。
これにより全ての固定余因子 w について、明示的に有限化できる。

i=2P^a+2 は全素数・全指数で完全排除した。
別の付値と整数商による証明で残る全2,592件は Lean で実際に検証済み。
一般 GCD 公式と S≤12 の排除からも、v8 の i=P^a+2 と併せて再証明できる。

円分因子7q^aの枝は、Eisenstein整数の primary trace から指数に依存する
合同式を導き、q≤211の全21底のうち18底を全指数で排除した。
偶数指数では q≥367 が必要で、4q=1+27m²（q≠7素数）の形も全指数で排除。
奇数指数の付値と二項係数の縮約も強めた。

証明・全証明書・検算・監査と未形式化の範囲は
[v9 日本語概要](PROGRESS_v9_ja.md) と [v9_manifest.json](v9_manifest.json) に記録する。
元の四変数方程式の全体は引き続き未解決である。

## 2026年11月5日の追加：v8

ell=1、j=i-3、i=P^a+2 を、任意の素数 P・正整数 a について完全排除した。
共通約数から整数商を取り出し、対数幅と合わせて i<2^192 を証明。
さらに底の素数を合同条件で有限化し、残る全2,903件の値が立方数でないことを
厳密整数計算と Lean カーネルで確認した。底3には別の短い全指数の証明がある。
v7 と合わせて i=3P^a+2 も P=3 を含む全ての素数について排除した。

同じ ell=1、j=i-3 の枝の一般の合成数では、i=wp^a+2、p>6w の指数を分類し、3|w のときは
a=2、i<961η²w³+2（η=1または2）へ還元した。
また A=C(i,3)、X=C(i²,6i−9)、S=A/gcd(A,X) とすると、
S|i−2、log i<128S、i<2^(192S) が必要であることを証明した。

i=jp³ の円分因子7q^aの枝では、4の倍数の指数を全排除し、
偶数指数の素数合同条件と、外側二項係数の正確な q-adic 付値を追加した。
全体の解の分類は未完了。解析・付値から有限領域への帰着は数学的証明であり、
全証明の Lean 形式化を主張していない。詳細は
[v8 日本語概要](PROGRESS_v8_ja.md) と [v8_manifest.json](v8_manifest.json) を参照。

## 2026年11月5日の追加：v7

ell=1、d=i-j に対して、d≥7 なら i<172d^36、d≥9 なら
さらに i<27d^35 を証明した。固定したオフセットごとの上限であり、
残りの有限範囲を全排除した主張ではない。

ell=1、j=i-3 では i-2 の最大素因数に P⁺(i-2)²≤6(i-2) が必要。
さらに i=3p^a+2、p≠3 の全素数・全指数を、正確な付値と
共通約数により40+16組へ還元し、完全な証明書で排除した。
i=P^a+2 の指数条件・立方剰余条件・Wieferich 因子の必要条件も追加した。

i=jp³ の円分因子7q^aについては全指数に合同条件を拡張し、
Thomas–Mignotte の既知の三次 Thue 方程式の定理へ帰着して
3の倍数の指数を排除した。詳細な仮定と外部定理への依存、
未形式化の範囲は [v7 日本語概要](PROGRESS_v7_ja.md) と
[v7_manifest.json](v7_manifest.json) に記録する。

## 2026年11月5日の追加：v6

ell=1、j=i-3、n=i、r=min(k,C(n,3)-k) の枝では、

\[
\frac n{\gcd(n,3)}\frac{n-1}{\gcd(n-1,6)}\mid r^3
\]

という新しい共通約数の条件を証明した。これにより n-1 が
平方自由な場合を全範囲で排除し、2・5の冪には特定の有限集合の
外にある Wieferich 素因数が必要だと示した。

また n≥1024 では

\[
3n<r<3n+\frac{3n}{4\log n}
\]

を証明。c₃(z)=∏p^ceil(v_p(z)/3)、R=n/c₃(n/gcd(n,3)) とすると
R≤12 の全範囲を理論的に有限化し、全2,180組・4,360式を排除した。
両隣の平方約数を使い、この枝で可能な第一添字 n≤X の個数が
O(X^(3/4)) 以下であることも証明した。

別の残存形 i=jp³、k=p、ell=1 では、p²+p+1 が3以外の
素因数を少なくとも二つ持つことが必要になった。
さらに p²+p+1=7q、q素数の場合は、合同式からの二次方程式と
実数評価を組み合わせ、証明された17候補をすべて排除した。

詳細な仮定・証明・残る範囲は [v6 日本語概要](PROGRESS_v6_ja.md)、
ファイルハッシュと検証範囲は [v6_manifest.json](v6_manifest.json) に記録する。

## 2026年11月5日の基準点：v5

ell=1、j=i-3、r=min(k,C(i,3)-k) について、
3i<r<10i/3 を証明した。その上で、
i/gcd(i,3) が平方因子を持たない場合、i=3^a、13^a、19^a、
および任意の素数 p に対する i=p^2,p^4 を排除した。

別の残存形 i=jp^3、k=p、ell=1 は、明示的な実関数の根の近傍へ
j を絞り、各素数 p につき高々一候補にした。さらに調和数の
法 p^5 の必要条件を導いた。この族の全排除はまだできていない。

ell>j の下側 k=ell+1=b の分岐でも、8j/3<=b<=4j を排除し、
隣接する 5j/2<=b<8j/3 では i=j+4 の形だけに絞った。
各主張の仮定・依存する前段階の証明は、それぞれのノートに明記している。

## 証明と検証の区別

1. 数学的証明：Markdown の各ノートに、無限範囲を含む議論を記す。
2. 有限証明書：まず理論的に有限範囲へ還元し、各候補を排除する
   素数・剰余等を生成する。独立した列挙・計算法で検証する。
3. Lean：実際に実行したソース・ログ・バージョンを記録する。
   明示的な仮定として残している解析評価まで形式化済みとはしない。
4. 実験・未完了の方向：必要条件と観察だけで、解なしの定理にしない。

過去の版の元ファイルは、その時点の記録として保存している。
後続の結果は新しい版名で追加し、訂正が必要になった場合は
旧主張と訂正理由を明示する。

## 再計算

このディレクトリを作業場所にする。代表的な小さい検算は Python の
標準ライブラリだけで実行できる。

    python3 v10_valuation_recovery_checks.py
    python3 v10_small_cofactors_checks.py verify
    python3 v10_small_cofactors_independent_reproduction.py
    python3 v10_cyclotomic_auxiliary_rings_checks.py

前の版：

    python3 v9_gcd_structure_checks.py
    python3 v9_cofactor_two_checks.py
    python3 v9_gcd_defect_cf_checks.py verify
    python3 v9_gcd_defect_cf_reproduction.py 12
    python3 v9_cyclotomic_primary_trace_checks.py

前の版：

    python3 v8_shifted_base_three_checks.py
    python3 v8_shifted_prime_power_completion_checks.py
    python3 v8_composite_shifted_completion_audit.py
    python3 v8_composite_dominant_prime_powers_checks.py
    python3 v8_cyclotomic_even_exponents_checks.py

前の版：

    python3 v7_fixed_offset_checks.py
    python3 v7_offset_cofactor_three_checks.py
    python3 v7_offset_shifted_prime_powers_checks.py
    python3 v7_large_prime_prime_power_extensions_checks.py

前の版：

    python3 v6_common_divisor_checks.py
    python3 v6_offset_composite_checks.py all
    python3 v6_offset_prime_powers_checks.py
    python3 v6_large_prime_cyclotomic_checks.py

前の版：

    python3 v5_offset_three_checks.py
    python3 v5_large_prime_localization_checks.py

v5 の有限証明書を再生成して独立検証する場合：

    python3 v5_l1_expanded_band.py generate
    python3 v5_l1_expanded_band.py verify
    python3 v5_l1_offset_four.py generate
    python3 v5_l1_offset_four.py verify

前段階の再計算方法は各証明ノート、スクリプトの説明、
v4_formal/README.md と v5_formal/README.md を参照。

## 大きい生成済み証明書

Git には証明、生成器、独立検証器、小さい結果記録を収録した。
v6〜v10 の有限証明書は全件含む。v9の大きい連分数係数列は、完全な内容を
圧縮テキストと再検証器で収録している。v5 までの基準アーカイブにあった
100 KB を超える生成済み証明書やバイナリ出力の一部は収録していない。
省略した16ファイルの名前・サイズ・SHA-256、および基準アーカイブとの
対応は [ARCHIVE_MANIFEST.json](ARCHIVE_MANIFEST.json) にある。

完全な生成済み証明書を含む以前のアーカイブ：
[nested_binomial_progress_v2.zip](https://chatgpt.com/library?file_id=libfile_77d5da929dd481918744ac98b12a8e70&account_id=personal)。
リンク先の利用には所有者のアクセス権が必要。再生成器はこのディレクトリにある。
Lean の実行環境本体と mathlib の依存チェックアウトは Git に含めない。

## 現在残る主な課題

- ell=1、j=i-3 で、回復後の不足分E≥13と平方合同・CRT条件を全て通過する混合素因数。
- 同じ枝の各正確な素数冪qに対し、補因子w=(i−2)/qがw/gcd(w,6)≥13かつlog i/128より大きい未排除の値。
- i 自身が素数冪になる旧来の残存族とその Wieferich 条件。i=P^a+2 の族は v8 で完了。
- i=jp^3 で、p²+p+1 の未排除の因数構造と、実数評価・合同条件の両立。
- 下側 i=j+4 の残存区間、およびその他の未排除分岐。

これらはこの研究記録の未完了部分であり、既知の未解決問題であると
分類したという意味ではない。
