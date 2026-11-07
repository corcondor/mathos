# v20: an upper logarithmic gap and a shorter defect height

Date: 2026-11-07 JST. Written proofs with exact rational verification.
No new Lean execution or DeepSeek API call is claimed.

## 1. Scope and conclusions

Keep the original equation with squared indices

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

In the inherited branch \(\ell=1,j=i-3\), set

\[
n=i,\quad A=\binom n3,\quad B=\binom{n^2}{6n-9},
\quad r=\min(k,A-k),\quad t=r-3n.
\]

The previously established necessary conditions include \(n\ge104\),
\(3n<r<10n/3\), and

\[
B<\binom Ar<2B,\qquad
C=M\delta,\quad Cr^2=Kn(n-1),\quad K,C\in\mathbb Z_{>0},
\quad M\le6,\quad\delta\ge25.
\tag{1}
\]

Here \(M=\gcd(n,3)\gcd(n-1,6)\),
\(Q=n(n-1)/M\), and \(\delta=Q/\gcd(Q,r^2)\). The bound
\(\delta\ge25\) is the complete v19 exclusion, not a new calculation.

This note proves

\[
\boxed{t<\frac{47n}{100\log n}\quad(n\ge2^{256}),}
\tag{2}
\]

and then, for **every** original solution in this branch,

\[
\boxed{\log n<17\delta,\qquad n<2^{25\delta}.}
\tag{3}
\]

The second bound replaces the old \(n<2^{42\delta}\). It bounds the
same intrinsic defect; it does not bound \(\delta\) itself. The large
threshold in (2) is harmless for (3): its entire lower range is covered
by \(\delta\ge25\), as proved below. No enumeration up to that threshold
is performed or needed.

## 2. Exact logarithmic constants

The exponential series gives \(8/3<e<3\), and a positive truncated
series gives \(\log2<7/10\). A lower bound follows from integration:

\[
\log2=2\int_0^{1/3}\frac{du}{1-u^2}
>2\int_0^{1/3}(1+u^2)\,du=\frac{56}{81}.
\tag{4}
\]

Let \(N_0=2^{256}\), \(L=\log n\), and
\(x=47/(100L)\). For \(n\ge N_0\),

\[
L>\frac{14336}{81}>100,\qquad
0<x<\frac{3807}{1433600}<\frac1{100}.
\tag{5}
\]

The following rational comparison will be used without any floating
point approximation:

\[
\frac{19}{1350}-\frac{11421}{1433600}>\frac1{200}.
\tag{6}
\]

Also \((8/3)^3>6(3+1/100)\) and \((8/3)^4>48\), so
\(\log(6y)<3\) for \(3\le y\le3+x\), and \(\log48<4\).

## 3. A binomial coefficient beyond the proposed upper gap

Set \(a=(3+x)n\) and \(b=\lceil a\rceil\). Then \(b<4n\).
For \(n\ge N_0\),
\(A>n^3/7>16n^2>b^2\); in particular \(b<A/2\).

The elementary product inequality gives

\[
\prod_{j=0}^{b-1}(1-j/A)
\ge1-\frac{b(b-1)}{2A}>\frac12.
\]

Integration of \(\log u\) gives \(b!\le eb(b/e)^b\). Consequently

\[
\binom Ab>\frac{(eA/b)^b}{2eb}
\ge\frac{(eA/a)^a}{2eb}.
\tag{7}
\]

The last inequality uses monotonicity of
\(y\mapsto y\log(eA/y)\) for \(0<y<A\); it also covers integral \(a\).
Further,

\[
\log A>3\log n-\log6-\frac4n.
\tag{8}
\]

Indeed \(A>(n^3/6)(1-3/n)\), and
\(\log(1-3/n)>-3/(n-3)\ge-4/n\) for \(n\ge12\).
The factorial lower bound and the same monotonicity argument yield

\[
B<\left(\frac{en}{6}\right)^{6n},
\tag{9}
\]

because \(6n-9<6n<n^2\).

Write \(f(y)=y(1-\log(6y))\). Combining (7)-(9), with
\(2x\log n=47/50\), gives

\[
\log\frac{\binom Ab}{2B}
>n\left\{3\log2-\frac{103}{50}+f(3+x)-f(3)\right\}
-4(3+x)-\log(4eb).
\tag{10}
\]

On the required interval, \(f'(y)=-\log(6y)>-3\). Thus the quantity
in braces is greater than

\[
\frac{19}{1350}-3x
>\frac{19}{1350}-\frac{11421}{1433600}
>\frac1{200}.
\]

Since \(4(3+x)<13\), \(4eb<48n\), (10) is greater than
\(n/200-13-\log(48n)\). This function increases for \(n>200\).
At \(N_0\), \(\log N_0<180\), so its value is greater than
\(2^{256}/200-197>0\). Hence \(\binom Ab>2B\).

But (1) gives \(\binom Ar<2B\). Monotonicity on the binomial row
up to \(A/2\) forces \(r<b=\lceil a\rceil\). Because \(r\) is an
integer, this implies \(r<a\), proving (2). Both choices of \(k\)
are included throughout.

## 4. The intrinsic defect height

First suppose \(n\ge N_0\). Since \(r>3n\),
\(K>9C\), so the integer \(K-9C\) is at least 1. Let
\(\alpha=47/100\). By (2),

\[
\begin{aligned}
\frac{L}{C}
&\le L\left(\frac KC-9\right)\\
&=L\left(\frac{r^2}{n(n-1)}-9\right)\\
&<\frac{(6\alpha+\alpha^2/L)n+9L}{n-1}.
\end{aligned}
\tag{11}
\]

From (5), \(\alpha^2/L<1/400\). Also \(9L<n/1000\).
For the latter, \(\log n/n\) decreases for \(n>e\), and at \(N_0\)
the bounds \(\log N_0<180\) and \(2^{256}>9000\cdot180\)
give it exactly. Finally \(n/(n-1)<1001/1000\). Therefore (11) and
\(C=M\delta\le6\delta\) imply

\[
L<6\delta\left(\frac{141}{50}+\frac1{400}+\frac1{1000}\right)
\frac{1001}{1000}
=\frac{16957941}{1000000}\delta<17\delta.
\tag{12}
\]

If \(n<N_0\), the inherited \(\delta\ge25\) gives instead

\[
\log n<256\log2<\frac{896}{5}<425\le17\delta.
\]

Thus \(\log n<17\delta\) holds globally. Finally,
\(25\log2>1400/81>17\), so exponentiation gives \(n<2^{25\delta}\).

## 5. Verification and remaining freedom

`v20_sharper_defect_height_checks.py` verifies all finite rational
comparisons and the polynomial identities in (10)-(12). The monotone
functions and factorial estimates above supply the universal argument;
no finite sample is promoted to an unbounded proof.

The exact solver used in v19 needed a proved height to cover every
Pell or lattice family of fixed \(\delta\). Bound (3) reduces that
height from 42 to 25 bits per unit of \(\delta\), a reduction by
\(17/42\). This is a reduction of the certified domain, **not** a
measured speedup of an implementation, and no old certificate is
rewritten. Values \(\delta\ge25\) remain unbounded; neither branch
nor the full four-variable equation is solved.
