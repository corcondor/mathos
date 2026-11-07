# v18: two further integer separations and lower-gap exponents 5/8 and 7/11

Date: 2026-11-07 JST. Written proof and exact coefficient verification.
No new Lean verification, DeepSeek API call, complete CAS solver, or external
peer review is claimed. Existing successful proof bodies and fixed goals
are unchanged.

## 1. Scope and conclusions

Retain the original squared-index equation

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}
\]

and the branch \(\ell=1,j=i-3\), for both \(k=r\) and \(k=A-r\). Put

\[
n=i,\quad A=\binom n3,\quad r=\min(k,A-k),\quad
t=r-3n,\quad u=t+3,
\]
\[
M=\gcd(n,3)\gcd(n-1,6),\qquad Q=\frac{n(n-1)}M.
\]

The starting necessary conditions are

\[
n\ge104,\qquad Q\mid r^3,\qquad 3n<r<10n/3.
\tag{1}
\]

The v16 lower-gap and v17 residual deductions from these conditions are
the written inputs below. In particular, the v17 complete classification
establishes \(h>81M\) already under (1). The stronger \(h\ge93M\), which
uses the original binomial congruences, is not needed here.

**Theorem.** Under (1), including the proved v17 deductions, one has

\[
\boxed{n^5<40^8u^8,\qquad n^7<96^{11}u^{11}.}
\tag{2}
\]

Consequently every original solution in this branch must satisfy

\[
\boxed{
r-3n+3>
\max\left(\frac{n^{5/8}}{40},\frac{n^{7/11}}{96}\right).
}
\tag{3}
\]

The first estimate strengthens v16's \(n^{3/5}/64\) for every positive n.
The second has the larger exponent but a larger constant; both are kept.
The already proved square-root bounds remain in force as well.

These are uniform bounds in n and all prime factors, obtained by integer
separation, not extrapolation from a finite scan. They do not give a global
upper bound on n or solve the entire branch.

## 2. The residual coordinate and a height retaining the residual

Define the positive integer h as in v16/v17:

\[
h=\frac{M\{(9t^2+27t+27)n+t^3\}}{n(n-1)}.
\]

Let

\[
g=\gcd(h,81M),\qquad a=h/g,\qquad b=81M/g.
\]

Thus \(h/(81M)=a/b\) is reduced. The established properties are

\[
a>b\ge1,\quad b\mid486,\quad b\le486,\quad u\ge7,
\tag{4}
\]

and, with the integer residual renamed \(\rho\) to avoid confusion with
the original lower binomial index j,

\[
\rho=a^2+ab(9n-t-6)-b^2(t^2+3t+3)\in\mathbb Z_{>0},
\]
\[
1377\rho<216a^2+760b^2.
\tag{5}
\]

The discriminant reconstruction proves that the nonnegative integer

\[
\begin{aligned}
F(a,b,\rho)={}&4a^6+24a^4b^2-12a^4\rho+36a^2b^4\\
&+60a^2b^2\rho+12a^2\rho^2-3b^2\rho^2-4\rho^3
\end{aligned}
\tag{6}
\]

is a square, say \(y^2=F\) with \(y\ge0\).

Two useful inherited inequalities, with the residual retained, are

\[
\boxed{
\rho u<
\frac{27a(2a^2+3ab+6b^2)}{17b}
<\frac{297a^3}{17b},
}
\tag{7}
\]

and

\[
\boxed{a<\frac{28b}{243}\frac{u^2}{n}\le56\frac{u^2}{n}.}
\tag{8}
\]

The second strict inequality in (7) uses \(a>b\). Inequality (8) follows
directly from \(h<28Mu^2/(3n)\) and \(a/b=h/(81M)\).

For clarity, (7) is the v17 height before replacing the positive residual
by 1. In the notation \(J=g^2\rho\) used there, v16's exact difference
of squares and \(u\ge7\) give

\[
J u<
\frac{13122}{17}Mh+\frac{81}{17}h^2+\frac{2}{51M}h^3.
\]

Dividing by \(g^2\), using \(h/g=a\), \(M/g=b/81\), gives the first
inequality in (7). No new approximation is hidden in this step.

## 3. First new separation: an integer cubic polynomial

Set

\[
q_0=2a^3+(6b^2-3\rho)a\in\mathbb Z.
\tag{9}
\]

From (5),

\[
q_0>
\frac{26}{17}a^3+\frac{1994}{459}ab^2
>\frac32a^3>0.
\tag{10}
\]

Also (4)-(5) yield

\[
0<\rho<\frac{976}{1377}a^2<\frac34a^2.
\tag{11}
\]

The coefficient comparisons are exact:
\(26/17-3/2=1/34\) and
\(3/4-976/1377=227/5508\).

Exact expansion of (6) and (9) gives

\[
\boxed{
D_0:=F-q_0^2
=3\rho(32b^2+\rho)a^2-\rho^2(3b^2+4\rho).
}
\tag{12}
\]

It is positive, because it can also be grouped as

\[
D_0=3b^2\rho(32a^2-\rho)+\rho^2(3a^2-4\rho)>0
\]

by (11). Therefore the integers y and \(q_0\) satisfy \(y\ge q_0+1\).
In particular,

\[
3a^3<2q_0+1\le y^2-q_0^2
<3\rho(32b^2+\rho)a^2.
\]

Canceling \(3a^2>0\) proves the dual residual-height inequality

\[
\boxed{a<\rho(\rho+32b^2)\le33b^2\rho^2.}
\tag{13}
\]

The last bound uses \(\rho\ge1\) and \(b\ge1\).

### Consequence: exponent 5/8

Square (7), then apply (13):

\[
u^2<
\left(\frac{297}{17}\right)^2
\frac{a^6}{b^2\rho^2}
<
\frac{33\cdot297^2}{17^2}a^5.
\]

Using (8) and canceling \(u^2>0\),

\[
\boxed{
n^5<
K_5u^8,\qquad
K_5=\frac{33\cdot297^2}{17^2}\,56^5
=\frac{1603123474563072}{289}
<40^8.
}
\tag{14}
\]

The final positive margin is

\[
40^8-K_5=\frac{290866925436928}{289}>0.
\]

This proves the first inequality in (2).

### A fixed residual now gives a polynomial height

Unlike the v17 height for fixed a, (13) bounds a once \(\rho\) and b
are fixed. Keeping \(\rho\) in (7), then using (8), gives

\[
n<
\frac{84a(2a^2+3ab+6b^2)^2}{289b\rho^2}
<
\frac{36a^5}{b\rho^2}.
\]

Substitute (13) to obtain

\[
\boxed{
n<\frac{36}{b}\rho^3(\rho+32b^2)^5.
}
\tag{15}
\]

There are only twelve possible b. Thus a fixed positive residual \(\rho\)
gives an explicit finite range and a degree-eight bound in \(\rho\).
The residual itself is unbounded in this result.

## 4. Second new separation: denominator 4a

Define the positive rational number

\[
q_1=q_0+\frac{3\rho(\rho+32b^2)}{4a}.
\tag{16}
\]

Its denominator divides \(4a\), so \(4aq_1\) is an integer. Another
exact expansion gives

\[
\boxed{
R_1:=F-q_1^2
=\frac{\rho}{2}(\rho^2+264b^2\rho-576b^4)
-\frac{9\rho^2(\rho+32b^2)^2}{16a^2}.
}
\tag{17}
\]

One cannot assume this remainder is always positive. We split into two
regions, and the smaller-residual region is handled by (13).

### Region I: \(\rho\ge7b^2\)

Write \(x=b^2/\rho\), so \(0<x\le1/7\). Using (11) in the final term of
(17),

\[
\begin{aligned}
\frac{R_1}{\rho^3}
&=\frac12+132x-288x^2
-\frac9{16}\frac{\rho}{a^2}(1+32x)^2\\
&>\frac5{64}+105x-720x^2\\
&\ge\frac5{64}+\frac{15}{7}x>0.
\end{aligned}
\tag{18}
\]

Thus \(y>q_1>q_0>3a^3/2\). The positive integer
\(4ay-4aq_1\) is at least 1, so

\[
R_1=(y-q_1)(y+q_1)>\frac{3a^2}{4}.
\tag{19}
\]

On the other hand, dropping the negative terms in (17) gives

\[
R_1<
\frac{\rho^3}{2}+132b^2\rho^2
\le\frac{271}{14}\rho^3.
\]

Consequently,

\[
\boxed{a^2<\frac{542}{21}\rho^3<26\rho^3
\qquad(\rho\ge7b^2).}
\tag{20}
\]

### Region II: \(1\le\rho<7b^2\)

Here no sign claim about \(R_1\) is made. Instead, (13) gives

\[
\begin{aligned}
a^2
&<\rho^2(\rho+32b^2)^2\\
&=\rho^3\left(\rho+64b^2+\frac{1024b^4}{\rho}\right)\\
&<\rho^3(71b^2+1024b^4)
\le1095b^4\rho^3.
\end{aligned}
\tag{21}
\]

Region I also satisfies this last, weaker uniform bound, because
\(26<1095b^4\). Hence, throughout the full residual domain,

\[
\boxed{a^2<1095b^4\rho^3.}
\tag{22}
\]

### Consequence: exponent 7/11

Cube (7) and apply (22):

\[
u^3<
\left(\frac{297}{17}\right)^3
\frac{a^9}{b^3\rho^3}
<
\left(\frac{297}{17}\right)^3 1095b\,a^7.
\]

Using (8), \(b\le486\), and canceling \(u^3>0\), gives

\[
\boxed{
n^7<K_7u^{11},\qquad
K_7=
\left(\frac{297}{17}\right)^3 1095\cdot486\cdot56^7
=\frac{24078860209989084260597760}{4913}
<96^{11}.
}
\tag{23}
\]

All constants are rationally compared in the accompanying verification.
Taking positive eleventh roots proves the second inequality in (2).

The two regions cover every positive integer residual. No residual
cutoff is tested computationally, and no sign-zero exception from (17)
is dropped: any such case in Region II is already covered by (21).

### Improved heights for either fixed parameter

The same estimates sharpen the v17 height for fixed a. Since
\(u^3<(297/17)^3 1095b a^7\), combine its square with (8) cubed to get

\[
\boxed{
n^3<\left(\frac{10164}{289}\right)^3
1095^2 b^5 a^{11}.
}
\tag{24}
\]

Thus, for the twelve possible denominators, \(n=O(a^{11/3})\), improving
the earlier degree-five height. Equivalently a must grow at least on
the order of \(n^{3/11}\), with an absolute constant after b<=486.
This is not a bound on a itself independent of n.

Likewise the retained height
\(n<10164a^5/(289b\rho^2)\), together with (22), yields

\[
\boxed{
n^2<\left(\frac{10164}{289}\right)^2
1095^5 b^{18}\rho^{11}.
}
\tag{25}
\]

For fixed \(\rho\) there is therefore a degree-11/2 height, also a
sharpening of the simpler degree-eight bound (15). Neither a nor rho
has been uniformly bounded over all original solutions.

## 5. Verification and remaining scope

Run

~~~sh
python3 v18_residual_gap_checks.py
~~~

in the directory containing this proof note and the script. The script
uses only Python's standard library. It independently multiplies
multivariate integer polynomials to check (12), both groupings of (12),
and the denominator-cleared form of (17). Exact rational comparisons
check all displayed constants and the positivity estimate (18).

For support only, it enumerates the older necessary conditions (1) in
a stated finite n range, recomputes h,a,b,rho and the discriminant root,
and checks every new inequality with exact integers or rational numbers.
Those pairs are not original solutions. This finite sample is not the
basis of the universal theorem.

The proof depends on the v16/v17 written deductions, including the
complete v17 result h>81M. It does not depend on a new elliptic-curve
solver, on ranks, on a bound for H or delta, or on assuming the full
binomial equation at a stage where only (1) was used.

No global upper bound for n, no complete classification of the branch,
no new original solution, and no improvement of the global
O(sqrt(X) log(X)) first-index count is claimed.

