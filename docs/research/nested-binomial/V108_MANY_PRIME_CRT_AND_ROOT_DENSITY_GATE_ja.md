# v108：全kに多数の「大→小」素因数／有限体の根の一括衝突／単独q進法の反例

2026-11-12。対象は元の二乗添字の入れ子二項係数方程式の
\(j=1,\ell=k-1\) 分岐
\[
\boxed{\binom{i}{k}=i^2+R_k,\quad R_k=\binom{k^2}{2k-1}}. \tag{108.1}
\]
v101の解析的高さ \(0<i<k^3\)、v106の有限体根証明書、v107の大→小q進単元縮約を継承。**元の四変数方程式全体、およびこの枝の全kの解決を主張しない。** 新しい焦点は、一つのqでの失敗を正しく認識し、全kで実際に大量のqがあることを証明し、多数の有限体根を同時に排除する明示的な十分条件を与えること。

## 定理1：全ての十分大きいkには、縮約可能な素数が少なくともk/(10log k)個存在

\(m=2k-1,\ N=k^2\) とし
\[
\mathcal P_k=\{q\text{ prime}: q>m,\ q\mid R_k\},\qquad \omega_>(k)=|\mathcal P_k|.
\]
**すべての自然数 k≥1000 に対し**
\[
\boxed{\omega_>(k)>\frac{k}{10\log k}.}\tag{108.2}
\]
この個数定理は外側の元等式の存在もiの探索も仮定しない。v107のSylvester–Schurによる非空性を著しく強めた、**このn=k²,m=2k−1系列での明示的な下界**。大きな素因数一般に関する結果は古典的に研究されており、世界初の一般定理とは主張しない。

**証明**：

1. Legendreの階乗付値恒等式
\[
v_p\binom Nm
=\sum_{a\ge1}\left(\left\lfloor N/p^a\right\rfloor-\left\lfloor m/p^a\right\rfloor-\left\lfloor(N-m)/p^a\right\rfloor\right)
\]
の各項は0か1。従って任意のpについて \(v_p(R_k)\le\lfloor\log_pN\rfloor\)、すなわち \(p^{v_p(R_k)}\le N=k²\)。
2. \(p\le m=2k-1\) なる素数は高々k個（素数2が最大1個、残りは奇数3,5,...,2k−1の最大k−1個）。従ってこれらの素数冪の積は \(\le k^{2k}\)。
3. \(q>m\) ならq≥2k、\(q²>k²=N\)。また分子の積 \(\prod_{h=0}^{m-1}(N-h)\) の区間長mはq未満、分母m!はqを含まない。従ってqがRに現れるなら**\(v_q(R)=1\)**。その積を \(P_k=\prod_{q\in\mathcal P_k}q\) と書くと
\[
P_k=\frac{R_k}{\prod_{p\le m}p^{v_p(R_k)}}\ge\frac{R_k}{k^{2k}}.
\]
4. Robbins/Stirlingの \(m!<3\sqrt m(m/e)^m\) と、\(N-m+1=k²-2k+2\) より
\[
R_k\ge\frac{(k²-2k+2)^m}{m!}
>\frac{[e(k²-2k+2)/m]^m}{3\sqrt m}.
\]
\(k\ge1000,\ m\le2k,\ e>8/3\) より \(e(k²-2k+2)/m>(13/10)k\)。従って
\[
\boxed{P_k>\frac{(13/10)^{2k-1}}{6k²}.}
\]
5. \(\log(13/10)>1/4\)（\(\log(1+x)>x-x²/2\) にx=3/10を入れる）と \(\log(6k²)<k/10\)（k≥1000では左の増加率2/k<1/10、端点で成立）より
\[
\log P_k>(2k-1)/4-k/10>k/5.
\]
各q≤k²なので \(\log P_k\le 2\omega_>(k)\log k\)、ゆえに(108.2)。

**漸近的な改良**：標準的なChebyshevの \(\pi(x)=O(x/\log x)\) とStirling精度 \(\log R_k=2k\log k+O(k)\) を使えば、
\[
\boxed{\omega_>(k)\ge k-O(k/\log k).}\tag{108.3}
\]
これは \(\log \prod_{p\le m}p^{v_p(R)}\le2\pi(m)\log k=O(k)\) と \(q\le k²\) だけで導ける。PNTの精密な漸近は不要。

## 定理2：多数のqの有限体非零根を、一括で処理する「3/5素数証明書」

\[
G_k(X)=\prod_{j=1}^{k-1}(X-j)-k!X\in\mathbb Z[X].
\]
整数係数多項式の恒等式
\[
\boxed{k!\left[\binom{i}{k}-i²\right]=i\,G_k(i)}
\]
は整数i≥kに有効。

**奇数k**では \(H_k(X)=G_k(X)\)。
**偶数k**では \(G_k(-1)=0\) なので \(G_k(X)=(X+1)H_k(X)\) となる**整数係数**多項式 \(H_k\) が存在する。
\(q>2k-1\) はk!を割らない。したがって元式(108.1)とq|Rから、有限体上で
\[
i\,H_k(i)\equiv0\pmod q \ (k\text{ odd}),\quad
i(i+1)H_k(i)\equiv0\pmod q\ (k\text{ even}).
\]
\[
\gcd_{\mathbb F_q[X]}(H_k(X),X^{q-1}-1)=1
\]
なら、**非零根がない**。またH_k(0)はq-unit（H(0)=(k−1)! up to sign, evenでも (X+1)は定数1）、よって実際に**H_kはFq上に根を一つも持たない**。

この「良い素数」の集合を \(\mathcal G_k\subset\mathcal P_k\) と定義する。すると：
- kが奇数で \(\boxed{|\mathcal G_k|\ge3}\) なら元式の全i無解（3つの異なるqがiを割り、その積> (2k−1)³>k³）。
- kが偶数で \(\boxed{|\mathcal G_k|\ge5}\) なら元式の全i無解（各qはiまたはi+1を割り、鳩の巣原理で少なくとも3つが同じ整数に付く。積>(2k−1)³>k³+1、なのにi<k³）。

これは全てのkに対する**明瞭な十分条件**であり、近接素数・等式のi探索・p進高次リフトは不要。ただし \( |\mathcal P_k|\gg k/\log k\) は証明済みでも、**そのうち良いqが必ず3/5個あることは未証明**。根の密度について特別な素因数集合q|R上の一様分布が必要。通常のChebotarev密度だけをこの変動するkの特殊なqに当てはめることはできない。

**偶数kの発見**：v106のG_kはX+1を因子に持つので、偶数kにG自体の「非零根なし」を要求すると恒等的に失敗する。**因子X+1を先に取り除いたH_kを使えば、偶数kにも一括root-free証明書が成立する**。これはv106のパリティ障害への構造的な対処。

## 定理3：1つのqの3桁Hensel根が高さ内側に残る具体的反例

\(k=8,q=17,i=68\) とする。\(R_8=\binom{64}{15}=159518999862720\) で17|R。実際
\[
0<i=68<8³=512,\qquad
\binom{68}{8}\equiv68²+\binom{64}{15}\pmod{17³=4913}.
\]
ただし**厳密な等式ではない**：
\[
\binom{68}{8}-68²-R_8=-159511607857576\ne0.
\]
これは「存在する1つのqの3桁p進リフトは、必ず高さの外に出る」という無条件主張の**真の反例**。証明者がこの誤った仮定で元式全解を宣言することを防ぐ。

## 具体的な多素数CRTの成功：k=8は2素数だけで全iを排除

q=19,59は、R_8を割る2つの素数であり、\(\mathbb F_{19}\) と \(\mathbb F_{59}\) における \(f_8(X)=\binom X8-X²\) の根は、いずれも
\[
\boxed{x\equiv0,-1\pmod q}
\]
だけである。有限体多項式G_8をX+1で割ったH_8のroot-free性は、\(X^{q-1}-1\)との多項式gcd=1という短い証明書にできる。

CRTによって、19·59=1121を法とする全4候補は
\[
\boxed{0,\ 531,\ 589,\ 1120\pmod{1121}}.
\]
任意の元式の解は \(0<i<8³=512\) なので、これらの剰余のどれにも一致できず、
\[
\boxed{\forall i\ge8,\quad
\binom i8\ne i²+\binom{64}{15}}
\]
となる。これはq=17の単独p進法が高さ内に偽候補68を残す一方、**2素数のCRTでその偽候補を消せる**という、明確な実例。

## 現在の正確な限界・次の論題

1. v107の「存在する1つのqの局所根が必ず実数高さと矛盾」は反例により偽。
2. **全k≥1000について良い素数の候補集合は少なくとも \(\gg k/\log k\) 個あるが、うちroot-freeなものが3個（奇数）/5個（偶数）以上という一様定理は未証明。**
3. G_kの奇数次数／偶数の既知線形因子を除いた多項式の分解群・Chebotarev型の根分布、あるいは特殊なq|Rに対する別の代数的制約が本命。一般のChebotarev定理は固定kの全素数中の密度であり、**q|R_kという有限でkとともに動く特異な集合**にそのまま適用してはいけない。
4. このv108は元の四変数方程式全体も、j=1,ell=k−1の無制限kの全解も決めていない。形式化できるのは、CRTの局所→大域矛盾や算術例、条件付きroot-free証明書の骨格。全kの根分布は新しい未解決補題として残る。

## 先行理論

- Legendre階乗付値公式・Robbins/Stirling不等式（古典）。
- Erdős–Graham, *On the Prime Factors of Binomial Coefficients*：大小素因数部分の分析が既存分野であることを明記。https://www.mathstat.dal.ca/FQ/Scanned/14-4/erdos.pdf
- Gallagherのlarger sieveにより、全てのqで根の個数が小さければ短いi区間の候補数を制限できる。しかし \(H_k\) の根数に**一様な小さい上限**は証明されておらず、単純な次数上界k−1を用いるだけでは十分なlarge-sieve分母を保証できない。https://ecroot.math.gatech.edu/gallagher.pdf

**検証状態**：一般下界(108.2/3)とroot-free→3/5素数衝突は記述証明。k8の2素数CRTとq17の反例は正確な整数演算および有限体GCDで独立照合。Lean定理は別ファイルで個別の成功ログを確認した場合のみ「kernel検証成功」と記す。


## 2026-11-12：固定Lean 4.35.0での本物のKernel検証

[CFV108TwoPrimeK8LocalGlobal.lean](v10_formal/CFV108TwoPrimeK8LocalGlobal.lean) を固定mathlibコミットで実行し、
[GitHub Actions 43167649879](https://github.com/corcondor/mathos/actions/runs/43167649879) は**ワークフロー成功**。
ログに CFV108TwoPrimeK8LocalGlobal.lean: exit=0, no proof holes=True と記録された。
新規モジュールは次の2定理を証明した：
- k8_original_equation_impossible_below_cubic_height：任意の正整数i<512に対する元式C(i,8)=i²+C(64,15)は矛盾。任意iへのLucas法19・法59、各有限体全根の正確な分類（決定的証明）、CRTの全4場合から導く。i<512自体は**v101の別の記述証明から入力する仮定**であり、このLean定理内部での高さ証明ではない。
- k8_spurious_one_prime_root：i=68が法17³における元等式の解であり、元の整数等式は偽、という**局所・大域不一致の反例**。
大きな素因数個数の全k≥1000の証明と奇偶3/5-rootfreeの**一般定理はこのLeanモジュールに含まない**。これらは本研究ノートの記述証明に依存し、全四変数の完全解決ではない。

整数・有限体多項式の独立検算は [GitHub Actions 43166808644](https://github.com/corcondor/mathos/actions/runs/43166808644) でPASS。
