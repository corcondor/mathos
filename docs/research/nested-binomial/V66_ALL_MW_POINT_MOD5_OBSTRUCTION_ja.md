# v66：第一楕円商が正階数でも使える、全有理点の整数復元に対する法5の一様障害

2026-11-08。v28は \(T\equiv1\pmod5\) の排除を第二楕円商の巡回部分群 \(\langle R\rangle\) を使って示した。しかし正階数の特殊化曲線には \(\langle R\rangle\) の外側の有理点があり、巡回部分群のみのふるいでは元の整数解全体をカバーできない。本稿は**種数2曲線の整数平方条件だけで、任意の有理点から来る元の整数候補に適用できる**法5の必要条件を示す。

## 定理：\(\rho\equiv b^2\pmod5\) なら元の主枝の整数解は存在しない

元の主枝の解に対する v20 の整数復元条件
\[
a,b,\rho,S\in\mathbb Z,\quad b\mid486,\quad
S^2=F(a,b,\rho)
\]
を仮定する。\(5\nmid b\) なので、
\[
u=\frac ab\in\mathbb Z_5,\qquad T=\frac{\rho}{b^2}\in\mathbb Z_5,
\qquad
\frac{F(a,b,\rho)}{b^6}
=f(u,T)
=(6u^2+2+3T)^2+4(u^2-1-T)^3.
\tag{66.1}
\]
\(b^6\) は有理平方なので、\(F\) が整数平方なら \(f(u,T)\) は \(\mathbb Q_5\) でも平方である。ところが \(T\equiv1\pmod5\) では
\[
f(u,T)\equiv f(u,1)
\equiv 4u^6+2u^4+3u^2+3\pmod5.
\tag{66.2}
\]
\(\mathbb F_5\) において \(u^2\in\{0,1,4\}\) の場合分けをすると
\[
\boxed{
\begin{array}{c|ccc}
u^2\bmod5&0&1&4\\ \hline
f(u,1)\bmod5&3&2&3
\end{array}
}\tag{66.3}
\]
となる。いずれも平方剰余 \(\{0,1,4\}\) に含まれない。従って
\[
\boxed{
\rho\equiv b^2\pmod5
\quad\Longrightarrow\quad
\text{元の主枝には整数解が存在しない}.
}\tag{66.4}
\]

**重要**：第二楕円商の点が \(P=mR\) か、二次基底変換の \(mR+nH\) か、その他の特殊化で新しく生じた有理点かを**一切仮定しない**。さらに \(\rho\) の高さ上限、\(n,t\) の有限探索、第一楕円商の階数認証も必要ない。全ての整数解は(66.1)を必要とする、という既証明の射影だけを使っている。

## 補助系：\(T\equiv2\pmod5\) なら \(a/b\not\equiv\pm2\pmod5\)

同様に \(T\equiv2\pmod5\) では
\[
f(0,2)\equiv1,\quad f(\pm1,2)\equiv4,\quad
f(\pm2,2)\equiv3\pmod5.
\]
従って
\[
\boxed{
\rho\equiv2b^2\pmod5\text{ かつ元の整数解}
\Longrightarrow a\not\equiv\pm2b\pmod5.
}\tag{66.5}
\]
これも任意の楕円曲線上の有理点の整数復元に適用する。

## 全25残基の検算表

\[
\begin{array}{c|ccccc}
T\bmod5\backslash u\bmod5&0&1&2&3&4\\ \hline
0&0&4&4&4&4\\
1&3&2&3&3&2\\
2&1&4&3&3&4\\
3&0&1&0&0&1\\
4&1&4&0&0&4
\end{array}
\]
この表は \(b\mid486\) の全12種類、\(\rho,a\bmod5\) の全25組に対し、元の整数六次式 \(F(a,b,\rho)\) を**別途直接評価**して一致することを検証した。

[再現用の独立検算](v66_unrestricted_five_adic_square_verify.py) は群法則を一切使わず、有限体上の正確な整数演算と符号化されている六次式を照合する。

## v64/v65との接続と限界

- [v64](V64_UNIFORM_POSITIVE_RANK_NECESSITY_ja.md) から「元の整数解があれば第一楕円商は正階数」だが、それだけでは不十分。
- [v65](V65_POSITIVE_RANK_SQUARE_COVER_AND_UNIFORM_EXCLUSION_ja.md) には、正階数で平方被覆を通る無限族 \(T=u^2-6u-3\) が実際に存在する。しかし元の \(t\) の整除性により、その族も排除できた。
- **本v66は** \(\rho\equiv b^2\pmod5\) の全無限族を、正階数かどうかに関係なく一挙に排除する。

これは元の方程式の主枝からの必要条件に基づく定理であり、残る法5の4類型や正階数の全有理点まで決定したわけではない。Lean形式化・外部査読は未実施。
