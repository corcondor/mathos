# Prime first upper index and second lower index one: complete exclusion

## 1. Statement and prerequisites

Consider the equation

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2},
\tag{1}
\]

with ordinary binomial coefficients at valid nonnegative integer arguments.
Write

\[
A=\binom ij,\quad B=\binom{k}{\ell},\quad
X=\binom{i^2}{j^2},\quad Y=\binom{k^2}{\ell^2},
\quad M=\max(j,\ell),\quad r=\min(B,A-B).
\]

The earlier boundary reductions, exact certificate for \(M\le20\), and
`sharp_q_bounds.md` establish that every remaining solution satisfies

\[
1\le j\le i-2,\qquad 1\le\ell\le k-1,\qquad
1<B<A,\qquad M\ge21,\qquad r<10M.
\tag{2}
\]

We also use the proved inequality

\[
\binom{n^2}{m^2}<16\binom nm^{2m}
\qquad(1\le m\le n-2).
\tag{3}
\]

**Theorem.** Equation (1) has no solution with \(i\) prime and
\(\ell=1\), in either branch \(B\le A/2\) or \(B\ge A/2\).

Apart from the previously established exclusion of \(M\le20\), the
main proof below uses only uniform inequalities and congruences. In particular,
the new prime-index argument requires no additional finite search.

A second result from Section 3.2 of `sharp_q_bounds.md` is

\[
M\ge21,\quad A\ge M^3/6
\quad\Longrightarrow\quad r<5M.
\tag{4}
\]

In particular, if \(M=j\) and \(i-j\ge3\), then
\(A\ge\binom{j+3}{3}>j^3/6\), so \(r<5j\).

## 2. Prime congruences force a multiple of the prime

Assume \(i=p\) is prime and \(\ell=1\). Then

\[
M=j\ge21,\qquad 21\le j\le p-2,\qquad p\ge23,
\qquad B=k,\qquad Y=B^2.
\tag{5}
\]

For \(0<j<p\), the identity

\[
A=\binom pj=\frac p j\binom{p-1}{j-1}
\]

shows that \(A=pu\) for an integer \(u\) with \(p\nmid u\).
Writing \(a\in\{1,\ldots,p-1\}\) for the residue of \(u\), we have

\[
a\equiv(-1)^{j-1}j^{-1}\pmod p.
\tag{6}
\]

Here \(\binom{p-1}{j-1}\equiv(-1)^{j-1}\pmod p\), as follows
directly from its product formula.

Also

\[
j^2X=p^2\binom{p^2-1}{j^2-1},
\]

so \(p^2\mid X\), because \(p\nmid j\).
Since \(B\) is either \(r\) or \(A-r\),

\[
X+Y\equiv r^2\pmod p.
\tag{7}
\]

The elementary polynomial congruence

\[
(1+z)^{pu}\equiv(1+z^p)^u\pmod p
\tag{8}
\]

implies \(\binom Ar\equiv0\pmod p\) whenever \(p\nmid r\).
This would contradict (7). Therefore \(r=mp\) for some positive
integer \(m\). The prior bound \(r<10j<10p\) gives

\[
1\le m\le9<p.
\tag{9}
\]

Comparing coefficients of \(z^{mp}\) in (8), and using \(m<p\), gives

\[
\binom A{mp}\equiv\binom u m\equiv\binom a m\pmod p.
\tag{10}
\]

The second congruence follows by reducing the falling factorial modulo
\(p\); the denominator \(m!\) is invertible modulo \(p\).
By (7), the left side of (10) must vanish modulo \(p\).
For \(0\le a,m<p\), \(\binom a m\) is nonzero modulo \(p\)
when \(m\le a\), and is zero when \(a<m\). Hence

\[
a<m.
\tag{11}
\]

We must also have \(a\ne1\). Indeed, \(a=1\) and (6) would imply

\[
j\equiv(-1)^{j-1}\pmod p.
\]

For odd \(j\), this forces \(j=1\), excluded by the earlier
\(M\le20\) result. For even \(j\), it forces \(j=p-1\), excluded
by the boundary condition \(j\le p-2\). Thus every prime-index
candidate satisfies

\[
\boxed{r=mp,\qquad 2\le a<m\le9.}
\tag{12}
\]

In particular, \(m\ge3\); this also excludes \(m=1\) and \(m=2\),
including their boundary cases.

## 3. The congruence forces a gap larger than the analytic upper bound

Let \(\varepsilon=(-1)^{j-1}\). By (6), there is an integer \(h\) such
that

\[
aj=hp+\varepsilon.
\]

Since \(j\le p-2\) and \(a\ge2\),

\[
hp=aj-\varepsilon\le a(p-2)+1<ap,
\]

and therefore \(h\le a-1\). It follows that

\[
j\le\frac{(a-1)p+1}{a}.
\tag{13}
\]

On the other hand, \(m\ge a+1\), so \(r=mp\ge(a+1)p\).
Combining this with (13) gives

\[
\begin{aligned}
r-5j
&\ge(a+1)p-5\frac{(a-1)p+1}{a}\\
&=\frac{\bigl((a-2)^2+1\bigr)p-5}{a}>0.
\end{aligned}
\tag{14}
\]

The last inequality uses only \(p\ge23\) and \(a>0\).
Thus \(r>5j\).

If \(p-j\ge3\), then the prior analytic bound (4) gives \(r<5j\),
a contradiction. The only remaining offset allowed by the boundary
conditions is \(p-j=2\). But then \(j=p-2\) is odd, and (6) gives

\[
a\equiv(-2)^{-1}\pmod p,
\qquad a=\frac{p-1}{2}\ge11,
\]

contradicting \(a<m\le9\).

This proves the theorem for \(M\ge21\). The previously certified
\(M\le20\) cases complete the claim for all valid nonnegative
integers. \(\square\)

## 4. Independent finite cross-check, not needed by the proof

Before the uniform arguments in this note were obtained, the weaker
\(j\ge100\) offset bound reduced this prime-index family to
\(21\le j\le99\), prime \(p<330\), and the necessary modular conditions in (12).
The exact-integer program `verify_prime_first_ell_one.py` checks the
resulting 188 triples \((p,j,m)\), with both \(B=r\) and \(B=A-r\).
Its saved report is `verification_prime_first_ell_one.json`.

There are 376 equations in that cross-check; all have left side strictly
larger than right side, and none is an equality. The program was
independently read and rerun. These calculations are redundant for the
main proof in Sections 2-3, which excludes the whole range at once.

## Appendix. A further uniform offset lemma valid in both branches

The following independent lemma is not needed for the shorter proof above.
It gives another route from (12) to two possible offsets.

**Lemma.** Every remaining solution with

\[
M=j\ge21,\qquad r\ge3i
\]

must satisfy

\[
\boxed{i-j\in\{2,3\}.}
\tag{A1}
\]

**Proof.** Put \(n=i\), and suppose instead that \(n-j\ge4\).
Then \(n\ge25\), and \(4\le j\le n-4\). Unimodality in the
\(n\)-th binomial row gives

\[
A\ge\binom n4
=\frac{n^4}{24}\prod_{h=1}^3(1-h/n)
>\frac{n^4}{24}(1-6/n)
\ge\frac{19n^4}{600}
>\frac{n^4}{32}.
\tag{A2}
\]

The strict product bound follows by expanding the three factors, or by
the inequality \(\prod_h(1-x_h)\ge1-\sum_hx_h\) for \(0\le x_h\le1\).

The endpoint \(\ell=k-1\) cannot occur here: it would give
\(B=k=\ell+1\le j+1<3n\le r\), contrary to \(r\le B\).
Thus \(k\ge\ell+2\). Since \(\ell\le j\), (3) and \(B<A\) imply

\[
X+Y<16A^{2j}+16B^{2\ell}
<32A^{2j}\le32A^{2n-8}.
\tag{A3}
\]

Since \(3n\le r\le A/2\), we have \(A\ge6n\) and
\(\binom Ar\ge\binom A{3n}\). For any integers \(A\ge2s\),

\[
\begin{aligned}
\binom As
&=\binom{2s}{s}\prod_{h=0}^{s-1}\frac{A-h}{2s-h}\\
&\ge\binom{2s}{s}\left(\frac A{2s}\right)^s
\ge\frac{(2A/s)^s}{2s+1}.
\end{aligned}
\tag{A4}
\]

The last step uses \(\binom{2s}{s}\ge4^s/(2s+1)\).
Taking \(s=3n\), and then applying (A2), gives

\[
\begin{aligned}
\frac{\binom Ar}{X+Y}
&>\frac{(2A/(3n))^{3n}}{32(6n+1)A^{2n-8}}\\
&=\frac{2^{3n}A^{n+8}}{32(6n+1)3^{3n}n^{3n}}\\
&>H(n):=\frac{(n/108)^n n^{32}}{2^{45}(6n+1)}.
\end{aligned}
\tag{A5}
\]

We next show \(H(n)>1\) for every real \(n\ge25\).
At the initial point, \(25/108>1/8\), \(25>16\), and \(151<256\),
so

\[
H(25)>
\frac{(1/8)^{25}16^{32}}{2^{45}\,256}
=2^{-75+128-45-8}=1.
\tag{A6}
\]

Moreover,

\[
\frac{d}{dn}\log H(n)
=\log(n/108)+1+\frac{32}{n}-\frac6{6n+1}
>\log(n/108)+1+\frac{31}{n}.
\tag{A7}
\]

The expression on the right has its global minimum over \(n>0\)
at \(n=31\), where its value is
\(\log(31/108)+2>0\). Indeed, \(e>2\) implies
\(31e^2>124>108\). Consequently \(H\) increases, and (A6) proves the
claim. Equation (A5) now contradicts (1). Together with \(i-j\ge2\),
this proves (A1). \(\square\)

## Scope

This note eliminates the full infinite family \(i\) prime,
\(\ell=1\), including both branches of the outer binomial coefficient.
It does not establish nonexistence for general composite \(i\), or for
general \(\ell>1\). The separate previously certified small-\(M\)
result remains a prerequisite; the present argument is not a Lean
formalization.
