# A uniform reduction and exact certificate method for a nested binomial equation

## 1. Equation, conventions, and scope

We consider

\[
\boxed{\binom{\binom{i}{j}}{\binom{k}{\ell}}
       =\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.} \tag{1}
\]

All four variables are nonnegative integers. Every binomial coefficient in (1) is required to have valid nonnegative arguments: initially \(0\le j\le i\), \(0\le\ell\le k\), and \(\binom{k}{\ell}\le\binom{i}{j}\). Thus this note does not extend the equation by assigning zero to binomial coefficients with an invalid lower argument. In particular, the right side contains binomial coefficients **at squared arguments**, not squares of binomial coefficients.

Write

\[
A=\binom{i}{j},\qquad B=\binom{k}{\ell},\qquad
X=\binom{i^2}{j^2},\qquad Y=\binom{k^2}{\ell^2},
\]

\[
M=\max(j,\ell),\qquad t=A-B,\qquad r=\min(B,t).
\]

The results below prove the following parameter-uniform reduction:

\[
1\le j\le i-2,\quad 1\le\ell\le k-1,\quad
j+2\le r<12M,\quad t\ge M+2. \tag{2}
\]

They also give an explicit height bound for every family in the branch \(t\le B\), with \(j,\ell,t\) fixed. These statements reduce the proposed exclusion of all solutions with \(M\le N\) to a finite list of polynomial families, for which exact congruence and lifting certificates may be sought. The upper indices \(i,k\) are not bounded by an experimental cutoff: their relevant bounds are proved below.

This note proves the mathematical reduction and the certificate validation rules. A particular computed exclusion range \(N\), its family counts, and the outcomes of an independent verifier belong in the accompanying computation report; they are not asserted here.

## 2. Boundary cases and necessary lower bounds on the gap

### 2.1 A grid inequality

For integers \(1\le m\le n\), let \(D=\binom{n}{m}\). Then

\[
\binom{n^2}{m^2}\ge D^{m+1}. \tag{3}
\]

To prove this, identify the \(n^2\) objects with the cells of an \(n\times n\) grid. Choose exactly \(m\) occupied rows, in \(D\) ways. In each chosen row, independently choose \(m\) cells, in \(D^m\) ways. Every resulting set has exactly \(m^2\) cells. The set determines its occupied rows and its choices within each row, so all \(D^{m+1}\) sets are distinct. This proves (3).

### 2.2 Elimination of the endpoints

Every valid binomial coefficient in (1) is positive, so \(X+Y\ge2\). If \(A=1\), then the left side is at most 1, which is impossible. Thus \(A>1\), and consequently \(1\le j\le i-1\).

If \(B=1\), then \(\ell=0\) or \(\ell=k\), so \(Y=1\) and the left side equals \(A\). But (3) gives \(X\ge A^{j+1}\ge A\), a contradiction. Thus \(B>1\), and \(1\le\ell\le k-1\). If \(B=A\), the left side is again 1, which is impossible. Therefore

\[
1<B<A.
\]

For every interior binomial coefficient, \(\binom{n}{m}\ge n\). This follows, for example, from symmetry and unimodality of the binomial coefficients in a row. Hence

\[
i\le A,\qquad k\le B<A. \tag{4}
\]

### 2.3 The smaller outer index satisfies \(r\ge j+2\)

By symmetry of the outer binomial coefficient and (3),

\[
\binom{A}{B}=\binom{A}{r}\le A^r,
\qquad X\ge A^{j+1}.
\]

If \(r\le j+1\), then the left side of (1) is at most \(X\), whereas the right side is \(X+Y>X\). Consequently

\[
\boxed{r\ge j+2.} \tag{5}
\]

In particular, \(B\ge j+2\) and \(t\ge j+2\). If \(j=i-1\), then \(A=i\), while (5) and \(r\le A/2\) would imply \(i+1\le i/2\). This is impossible, so

\[
1\le j\le i-2. \tag{6}
\]

### 2.4 The complementary gap satisfies \(t\ge\ell+2\)

If \(\ell=1\), this follows from \(t\ge j+2\ge3\). Suppose \(\ell\ge2\), and put \(m=\ell+1\ge3\). From (4), \(B\ge k\ge m\). If \(t\le m\), then

\[
\binom{A}{B}=\binom{B+t}{t}\le\binom{B+m}{m}<B^m\le Y. \tag{7}
\]

Here the final inequality is (3), applied to \((k,\ell)\). To verify the strict middle inequality, if \(m\ge4\), use

\[
\binom{B+m}{m}<\frac{(2B)^m}{m!}\le B^m,
\]

because \(B\ge m\) and \(m!\ge2^m\) for \(m\ge4\). If \(m=3\), use

\[
\frac{\binom{B+3}{3}}{B^3}
=\frac{(1+1/B)(1+2/B)(1+3/B)}6
\le\frac{20}{27}<1.
\]

Equation (7) contradicts (1). Thus \(t\ge\ell+2\), and, together with (5),

\[
\boxed{t\ge\max(j,\ell)+2=M+2.} \tag{8}
\]

## 3. A uniform estimate for binomial coefficients at squared arguments

For \(1\le m<n\), define

\[
Q_m(n)=\frac{\binom{n^2}{m^2}}{\binom{n}{m}^{2m}}.
\]

We will prove

\[
\boxed{Q_m(n)\le(8/e)^m<3^m<4^m.} \tag{9}
\]

No monotonicity assertion about \(Q_m\) is needed.

### 3.1 The entropy estimates, including their constants

Let

\[
h(p)=-p\log p-(1-p)\log(1-p),\qquad 0<p<1.
\]

For integers \(0<a<n\) and \(p=a/n\), the estimates we need are

\[
\frac{e^{nh(p)}}{\sqrt{8np(1-p)}}
\le\binom{n}{a}\le e^{nh(p)}. \tag{10}
\]

The upper bound follows because the term
\(\binom{n}{a}p^a(1-p)^{n-a}\) is at most the sum of all terms of the binomial probability distribution, which is 1.

For completeness, the lower bound follows with the stated constant from Robbins's precise Stirling bounds [R]: for every integer \(v\ge1\),

\[
\sqrt{2\pi v}(v/e)^v e^{1/(12v+1)}
<v!<\sqrt{2\pi v}(v/e)^v e^{1/(12v)}. \tag{11}
\]

Write \(b=n-a\), and set

\[
f=\frac1{12a}+\frac1{12b}-\frac1{12n+1}.
\]

Applying the lower bound in (11) to \(n!\) and the upper bound to \(a!,b!\) gives

\[
\binom{n}{a}>
\frac{e^{nh(p)}e^{-f}}{\sqrt{2\pi np(1-p)}}. \tag{12}
\]

If \(n\ge3\), then \(f<1/10\). Indeed, when \(a,b\ge2\), one has \(f<1/12\). Otherwise, after interchanging \(a,b\), take \(a=1\) and \(b\ge2\); then

\[
f=\frac1{12}+\frac{13}{12b(12b+13)}
\le\frac{29}{296}<\frac1{10}.
\]

Moreover \(2\pi e^{1/5}<8\): one may use \(\pi<22/7\) and
\(e^{1/5}<\sum_{v\ge0}(1/5)^v=5/4\), giving the stronger upper bound \(55/7<8\). Thus (12) implies the lower bound in (10). For \(n=2,a=1\), that lower bound is equality, so (10) holds in every case needed here.

### 3.2 Application to \(Q_m(n)\)

Put \(p=m/n\), \(u=m(1-p)\), and

\[
D(p)=2p h(p)-h(p^2).
\]

Applying the upper bound in (10) to \(\binom{n^2}{m^2}\) and the lower bound to \(\binom{n}{m}\) gives

\[
Q_m(n)\le(8u)^m e^{-n^2D(p)}. \tag{13}
\]

The following identity supplies the required comparison of entropies:

\[
D(p)=(1-p)\bigl((1-p)\log(1-p)+(1+p)\log(1+p)\bigr).
\]

If the expression in parentheses is denoted by \(F(p)\), then \(F(0)=0\) and

\[
F'(p)=\log\frac{1+p}{1-p}\ge2p.
\]

The latter inequality follows by differentiation, or by integrating
\(2/(1-p^2)\ge2\). Therefore \(F(p)\ge p^2\), and

\[
n^2D(p)\ge n^2(1-p)p^2=m^2(1-p)=mu.
\]

Equation (13) now yields

\[
Q_m(n)\le(8u e^{-u})^m\le(8/e)^m,
\]

since \(u e^{-u}\le1/e\) for \(u>0\). Finally \(e>8/3\), proving (9). In particular, every solution of (1) satisfies

\[
X+Y<4^jA^{2j}+4^\ell B^{2\ell}
\le2\cdot4^M A^{2M}. \tag{14}
\]

## 4. The global gap bound \(r<12M\)

Suppose, for contradiction, that \(r\ge12M\), and put \(s=12M\). Since \(r\le A/2\),

\[
A\ge24M. \tag{15}
\]

We also have

\[
A\ge M^2/2. \tag{16}
\]

For \(M=1\), this already follows from (15). If \(M=j\ge2\), then (6) and unimodality give \(A\ge\binom{i}{2}\ge M^2/2\). If \(M=\ell\ge2\), the case \(\ell=k-1\) would give \(B=k=M+1<12M\le r\), a contradiction. Thus \(2\le\ell\le k-2\), and \(A>B\ge\binom{k}{2}\ge M^2/2\). This checks the endpoint that would otherwise obstruct (16).

By unimodality, \(\binom{A}{r}\ge\binom{A}{s}\). Since \(A\ge2s\),

\[
\binom{A}{s}
=\binom{2s}{s}\prod_{h=0}^{s-1}\frac{A-h}{2s-h}
\ge\binom{2s}{s}\left(\frac{A}{2s}\right)^s
\ge\frac{4^s}{2s+1}\left(\frac{A}{2s}\right)^s.
\]

The last step uses the fact that the central coefficient is the largest of the \(2s+1\) coefficients whose sum is \(4^s\). Consequently

\[
\binom{A}{r}\ge\frac{(A/(6M))^{12M}}{24M+1}. \tag{17}
\]

Define

\[
q=\frac{A^{10}}{4(6M)^{12}}.
\]

The quotient of the lower bound in (17) by the upper bound in (14) is

\[
\frac{q^M}{2(24M+1)}. \tag{18}
\]

From (15) and (16), respectively,

\[
q\ge\frac{65536}{9M^2},\qquad
q\ge\frac{M^8}{12^{12}}.
\]

For \(M\le48\), the first bound is at least \(256/81\). For \(M\ge48\), the second is at least \(256/81\). Hence \(q\ge256/81>3\) for every \(M\).

For \(M\ge5\), \(3^M>48M+2\): the base case is \(243>242\), and the inequality is preserved by increasing \(M\) by one. For \(1\le M\le4\), the first bound above gives \(q\ge4096/9>194\ge48M+2\). Thus (18) is strictly greater than 1 in every case. This would make the left side of (1) larger than its right side, a contradiction. We have proved

\[
\boxed{r<12M.} \tag{19}
\]

## 5. An explicit height bound for each upper-branch family

In this section fix positive \(j,\ell,t\), and consider a solution in the upper branch

\[
t=A-B\le B,\qquad B\ge A/2. \tag{20}
\]

Put

\[
M=\max(j,\ell),\quad
H_0=2(6M^3)^M,\quad
K_M=M^{2M^2},\quad
C_M=9M^3+6M^2+3.
\]

For a positive integer \(v\) and positive integer \(d\), let
\(\lfloor v^{1/d}\rfloor\) mean the exact integer floor root, computed by integer comparisons, without floating-point rounding. The bound implemented by `bound(j,l,t)` in `hensel_upper_experiment.py` is

\[
\boxed{
H(j,\ell,t)=
\begin{cases}
\displaystyle\max\left\{H_0,
\left\lfloor\bigl(2^{2M+1}(M^2)!\bigr)^{1/(2M-t)}\right\rfloor\right\},
&t<2M,\\[6pt]
\displaystyle\max\left\{H_0,
\bigl(C_M\,t!\,(M^2)!\bigr)^M\right\},
&t=2M,\\[6pt]
\displaystyle\left\lfloor\bigl(2K_Mt^t\bigr)^{1/(t-2M)}\right\rfloor,
&t>2M.
\end{cases}} \tag{21}
\]

Every solution in (20) satisfies \(A\le H(j,\ell,t)\). The following proof also explains why equal leading degrees do not leave an unbounded exceptional family.

### 5.1 The leading coefficient and a quantitative approximation

Define

\[
q_m=\frac{(m!)^{2m}}{(m^2)!}.
\]

One has

\[
\frac1{(m^2)!}\le q_m\le1. \tag{22}
\]

For the upper bound, group the factors of \((m^2)!\) into \(m\) blocks:

\[
(m^2)!=\prod_{s=0}^{m-1}\prod_{h=1}^m(sm+h)
\ge\prod_{s=0}^{m-1}\prod_{h=1}^m(s+1)h
=(m!)^{2m}.
\]

For \(n\ge2m^3\), the product formula is

\[
\frac{Q_m(n)}{q_m}
=\frac{\prod_{s=0}^{m^2-1}(1-s/n^2)}
       {\prod_{h=0}^{m-1}(1-h/n)^{2m}}
=\frac{U}{V}.
\]

The elementary inequality \(\prod(1-z_a)\ge1-\sum z_a\), for \(0\le z_a\le1\), gives

\[
0\le1-V\le\frac{m^2(m-1)}n\le\frac{m^3}n,
\quad V\ge\frac12,
\quad 0\le1-U\le\frac{m^4}{2n^2}.
\]

It follows that

\[
\boxed{\left|\frac{Q_m(n)}{q_m}-1\right|
\le\frac{2m^3}{n}+\frac{m^4}{n^2}
\le\frac{3m^3}{n}.} \tag{23}
\]

If \(A\ge H_0\), then \(A\le i^j\), \(B\le k^\ell\), and (20) imply

\[
i,k\ge6M^3.
\]

Equations (22) and (23) then give

\[
\frac{q_j}{2}\le Q_j(i)\le\frac32,
\qquad
\frac{q_\ell}{2}\le Q_\ell(k)\le\frac32. \tag{24}
\]

### 5.2 Case \(t<2M\)

Suppose \(A\ge H_0\). At least one of \(j,\ell\) equals \(M\). Its contribution to the right side of (1), using (20), (22), and (24), is at least

\[
\frac{A^{2M}}{2^{2M+1}(M^2)!}.
\]

Since \(\binom{A}{t}\le A^t\),

\[
A^{2M-t}\le2^{2M+1}(M^2)!.
\]

Taking the exact integer floor root, and including the alternative \(A<H_0\), proves the first line of (21).

### 5.3 Case \(t>2M\)

This case needs no assumption \(A\ge H_0\). For \(1\le m\le n\),

\[
\binom{n}{m}\ge(n/m)^m,
\qquad
\binom{n^2}{m^2}\le n^{2m^2}.
\]

The first inequality follows by comparing the factors
\((n-h)/(m-h)\ge n/m\), for \(0\le h<m\). Therefore

\[
X\le j^{2j^2}A^{2j}\le K_M A^{2M},
\qquad
Y\le\ell^{2\ell^2}B^{2\ell}\le K_M A^{2M}.
\]

The same lower estimate gives \(\binom{A}{t}\ge(A/t)^t\). Equation (1) implies

\[
A^{t-2M}\le2K_Mt^t,
\]

which proves the third line of (21).

### 5.4 Case \(t=2M\): the leading coefficients do not cancel

Let

\[
c=\mathbf1_{j=M}+\mathbf1_{\ell=M}\in\{1,2\},
\qquad
\delta=\left|\frac1{t!}-c q_M\right|.
\]

We first prove \(\delta>0\) for every \(M\ge1\). If it were zero, then

\[
(M^2)!=c(2M)!(M!)^{2M}. \tag{25}
\]

For \(M=1\), this says \(1=2c\), and for \(M=2\) it says \(24=384c\), both impossible. For \(M=3\), the prime 7 divides the left side of (25) but not the right side. For \(M\ge4\), Bertrand's postulate supplies a prime

\[
2M<p<4M\le M^2.
\]

Such a prime divides the left side of (25), while every prime divisor of its right side is at most \(2M\). This is again a contradiction. Bertrand's postulate is a classical theorem; an original elementary proof is cited in [E].

The numerator of \(\delta\), when written over the denominator \(t!(M^2)!\), is a nonzero integer. Hence

\[
\delta\ge\frac1{t!(M^2)!}. \tag{26}
\]

It remains to bound the approximation errors. Assume \(A\ge H_0\). For the left side,

\[
\left|\frac{\binom{A}{t}}{A^t}-\frac1{t!}\right|
\le\frac{t(t-1)}{2A}\le\frac{2M^2}{A}. \tag{27}
\]

If \(j=M\), the error of \(X/A^{2M}\) from \(q_M\) is at most
\(3M^3/i\le3M^3A^{-1/M}\). If \(\ell=M\), then

\[
\frac{Y}{A^{2M}}=Q_M(k)\left(1-\frac tA\right)^{2M},
\]

whose error from \(q_M\) is at most

\[
\frac{3M^3}{k}+\frac{4M^2}{A}
\le6M^3A^{-1/M}+\frac{4M^2}{A}.
\]

Here \(k\ge(A/2)^{1/M}\) and
\(1-(1-t/A)^{2M}\le2Mt/A=4M^2/A\). Each contribution with index strictly below \(M\) is, after division by \(A^{2M}\), at most \((3/2)A^{-2}\), by (24). Thus the combined contribution of all such terms is at most \(3A^{-2}\).

Comparing the normalized two sides of (1), and using (27), gives

\[
\delta\le9M^3A^{-1/M}+6M^2A^{-1}+3A^{-2}
\le C_MA^{-1/M}.
\]

Together with (26), this yields

\[
A\le\bigl(C_Mt!(M^2)!\bigr)^M.
\]

Including the alternative \(A<H_0\) proves the middle line of (21).

### 5.5 Bounds on the two upper indices

The simple bounds \(i,k\le A\le H\), where \(H=H(j,\ell,t)\), already suffice for a finite-height argument. The implementation uses the smaller safe bounds

\[
\boxed{
I=\min\{H,\ j\lceil H^{1/j}\rceil\},\qquad
K=\min\{H,\ \ell\lceil H^{1/\ell}\rceil\}.
} \tag{28}
\]

Indeed, \(\binom{i}{j}\ge(i/j)^j\) gives \(i\le jH^{1/j}\), and the analogous argument applies to \(k\), since \(B\le H\). The ceilings in (28) are exact integer ceiling roots. Replacing them by floor roots before multiplication would not in general be justified.

For certificate purposes one may use the slightly enlarged coordinate box

\[
j+1\le i\le I,\qquad \ell+1\le k\le K. \tag{29}
\]

Allowing \(i=j+1\) is harmless: it enlarges the set tested, although (6) already excludes that boundary for actual solutions.

## 6. A finite list of families for every prescribed \(N\)

Fix \(N\ge1\), and suppose \(M\le N\). Split into two branches, allowing equality in either branch if desired.

### 6.1 Lower branch: \(B\le A-B\)

Here \(r=B<12M\). Since \(B\ge k\), only the finite triples

\[
1\le j,\ell\le N,\qquad
\ell+1\le k<12M,\qquad
j+2\le B=\binom{k}{\ell}<12M \tag{30}
\]

need to be considered. For each triple, the remaining unknown \(i\) satisfies the one-variable polynomial equation

\[
F(i)=\binom{\binom{i}{j}}{B}
     -\binom{i^2}{j^2}-\binom{k^2}{\ell^2}=0. \tag{31}
\]

The polynomial interpretation in this section is
\(\binom{z}{d}=z(z-1)\cdots(z-d+1)/d!\), with fixed nonnegative integer \(d\). It extends the expressions to all residue classes solely for the purpose of forming necessary congruences; it does not change the original domain of (1).

If a prime \(p>\max(j^2,\ell^2,B)\) has no root of (31) in \(\mathbb F_p\), then this entire family is excluded for every integer \(i\). All factorial denominators are invertible modulo \(p\). A certificate consists of the family parameters and such a prime, and a verifier checks every residue class exactly.

### 6.2 Upper branch: \(t=A-B\le B\)

Here \(r=t<12M\), so the finite list is

\[
1\le j,\ell\le N,\qquad M+2\le t<12M. \tag{32}
\]

For each triple define

\[
\begin{aligned}
F_1(x,y)&=\binom{x}{j}-\binom{y}{\ell}-t,\\
F_2(x,y)&=\binom{\binom{x}{j}}{t}
         -\binom{x^2}{j^2}-\binom{y^2}{\ell^2}.
\end{aligned} \tag{33}
\]

An actual solution gives \(F_1(i,k)=F_2(i,k)=0\). For every prime

\[
p>\max(j^2,\ell^2,t), \tag{34}
\]

these polynomials and their derivatives have coefficients integral at \(p\). Thus reduction modulo \(p^e\) is legitimate for every \(e\ge1\), using modular inverses for the factorial denominators.

A prime for which (33) has no common zero in \(\mathbb F_p^2\) immediately excludes the family. Complete residue enumeration can be implemented without testing all pairs: make a table of

\[
\left(\binom{y}{\ell},\binom{y^2}{\ell^2}\right),\qquad y\in\mathbb F_p,
\]

and, for each \(x\), look up

\[
\left(\binom{x}{j}-t,
\binom{\binom{x}{j}}{t}-\binom{x^2}{j^2}\right).
\]

This table lookup is an exhaustive test of the same congruences. Its correctness is independent of how the table is stored.

## 7. Exact Hensel certificates for families with residue roots

Some polynomial families have residue roots at many primes, including roots related to nonpositive integer solutions of the polynomial extension. Their existence does not imply a solution of the original equation. The proved height and coordinate bounds allow an exact exclusion of these roots.

### 7.1 Unique lifting at a nonsingular residue root

This is the nonsingular case of the multivariate Hensel theorem; see [H], Theorem 3.3. A direct finite-modulus proof is also given below.

For \(F=(F_1,F_2)^T\), let \(J_F\) be its \(2\times2\) Jacobian matrix. Suppose a common root \(z=(x,y)^T\) modulo \(p\) satisfies

\[
\det J_F(z)\not\equiv0\pmod p. \tag{35}
\]

Then it lifts uniquely to a common root in that residue class modulo every \(p^e\). The elementary proof is to write a prospective lift from modulus \(p^e\) to \(p^{e+1}\) as \(z+p^e v\). Taylor expansion gives one linear system for \(v\bmod p\), and its matrix \(J_F(z)\bmod p\) is invertible by (35). There is exactly one solution at each step.

The implementation doubles the exponent. If \(q=p^e\), \(F(z)\equiv0\pmod q\), and (35) holds, then

\[
\boxed{z'\equiv z-J_F(z)^{-1}F(z)\pmod{q^2}} \tag{36}
\]

is the unique lift modulo \(q^2\), with both coordinates chosen in \([0,q^2-1]\). The inverse in (36) is computed modulo \(q^2\). Since the correction is divisible by \(q\), the quadratic and higher Taylor terms are divisible by \(q^2\). This proves (36) directly. A verifier can check both \(z'\equiv z\pmod q\) and \(F(z')\equiv0\pmod{q^2}\).

### 7.2 Exact interval exclusion at any precision

For a canonical residue \(0\le x<q\), the smallest integer congruent to \(x\pmod q\) and at least \(L\) is

\[
x+q\max\left\{0,\left\lceil\frac{L-x}{q}\right\rceil\right\}.
\]

Therefore its residue class intersects \([L,U]\) if and only if

\[
x+q\max\left\{0,\left\lceil\frac{L-x}{q}\right\rceil\right\}\le U. \tag{37}
\]

Apply (37) to the two intervals in (29). If either lifted coordinate class misses its interval, no original solution can lie above that residue root. This is valid at any precision; it is not necessary to wait until \(q>H\). It is also valid for a singular initial root whose coordinate class is already excluded, so nonsingularity need only be required for the initial roots whose two coordinate classes both intersect (29).

Once \(q>\max(I,K)\), each coordinate residue class contains at most one nonnegative integer in its allowed interval. If both remain possible, the unique pair may be checked in the original integer equation. Alternatively, lifting can continue until a coordinate class is excluded. A surviving pair, a singular root not already excluded by its interval, or an incomplete lift must be reported as unresolved unless separately proved impossible. Such a case cannot be silently counted as certified.

### 7.3 What an independent verifier must establish

A nonsingular lifting certificate for an upper family is valid when an exact verifier establishes all of the following:

1. The parameter triple lies in (32), the prime satisfies (34), and the prime is actually prime.
2. The complete list of common roots of (33) modulo \(p\) is recomputed. No viable root is omitted.
3. The height \(H\) and coordinate bounds \(I,K\) are recomputed using (21) and (28), with exact integer roots.
4. Every initial residue root is either excluded immediately by (37), or has invertible Jacobian modulo \(p\) and is lifted by (36).
5. Every required lifted root is ultimately excluded by (37), or its unique possible integer representative is explicitly ruled out by an exact original-equation check.

The stored certificate may give a prime, the initial roots, and the terminal exponents. The verifier should recompute the arithmetic rather than trust a textual `certified` field or a claimed coordinate-exclusion flag. No rounding, approximate root location, or statistical sampling is involved.

## 8. The conclusion warranted by a complete certificate suite

For a prescribed \(N\), generate the full finite lists (30) and (32). If every lower family has a verified obstruction and every upper family has either a verified obstruction or a verified lifting exclusion, then (1) has **no valid solution with \(\max(j,\ell)\le N\)**.

This conclusion covers all nonnegative upper indices \(i,k\), however large. The reasons are the uniform gap bound (19), which makes the family lists exhaustive, and the explicit height bound (21), which makes interval exclusion in the upper branch logically complete.

The method does not, merely by excluding one finite range of \(M\), prove that (1) has no solution for arbitrary \(M\). A computation report should state the exact verified value of \(N\), the number of families generated in each branch, the number excluded by each certificate type, whether any families remain unresolved, and which independently executed verification produced those conclusions. Those computed outcomes should be kept distinct from the uniform theorems proved above.

## References

- **[R]** Herbert Robbins, “A Remark on Stirling's Formula,” *The American Mathematical Monthly* **62**(1) (1955), 26–29. [DOI: 10.2307/2308012](https://doi.org/10.2307/2308012). [Scan of the original paper hosted by the University of Southern California](https://dornsife.usc.edu/sergey-lototsky/wp-content/uploads/sites/211/2024/02/Stirling-Robbins.pdf). The precise factorial estimate (11) is the external input used to derive (10); the entropy comparison and the gap bound are proved in this note.
- **[E]** Paul Erdős, “Beweis eines Satzes von Tschebyschef,” *Acta Litterarum ac Scientiarum Regiae Universitatis Hungaricae Francisco-Josephinae, Sectio Scientiarum Mathematicarum* **5** (1932), 194–198. [Original paper in the Alfréd Rényi Institute archive](https://www.renyi.hu/~p_erdos/1932-01.pdf). [University of Szeged bibliographic record](https://acta.bibl.u-szeged.hu/13396/). This is an elementary proof of the prime-between-\(n\)-and-\(2n\) theorem used after (25).

- **[H]** Keith Conrad, [A Multivariable Hensel's Lemma](https://kconrad.math.uconn.edu/blurbs/gradnumthy/multivarhensel.pdf), Theorem 3.3. The square system version applies to the two polynomials used here.
