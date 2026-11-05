# Factorial divisibility, smooth intervals, and resultant restrictions

This note concerns only the original squared-index equation

\[
L:=\binom{A}{B}=X+Y,
\qquad A=\binom ij,\quad B=\binom{k}{\ell},\quad
X=\binom{i^2}{j^2},\quad Y=\binom{k^2}{\ell^2}.
\]

Put \(t=A-B\), \(r=\min(B,t)\), and \(M=\max(j,\ell)\).
We use the previously proved endpoint exclusions, \(r\ge j+2\),
\(r<10M\) for \(M\ge21\), and the exclusion of \(M\le20\).
The new statements below are necessary conditions, not a proof of global
nonexistence. No Lean formalization is claimed.

For a positive integer \(m\), define

\[
d_m=\frac{(m^2)!}{m!},\qquad
P_m(z)=\prod_{a=0}^{m-1}(z-a),\qquad
G_m(z)=\prod_{s=0}^{m^2-1}(z^2-s).
\]

An integer is called \(y\)-smooth if every prime divisor is at most \(y\).

## 1. A factorial divisibility valid for every parameter

The polynomial \(P_m(z)\) divides \(G_m(z)\) in \(\mathbb Z[z]\).
Indeed, the factor \(z\) is supplied by the factor \(z^2\), and each
factor \(z-a\), \(1\le a<m\), is supplied by \(z^2-a^2\).
Writing \(G_m=P_m T_m\), with \(T_m\in\mathbb Z[z]\), therefore gives

\[
\boxed{d_m\binom{n^2}{m^2}=\binom nm T_m(n).} \tag{1}
\]

In particular,

\[
A\mid d_jX,\qquad B\mid d_\ell Y.
\]

The standard identity

\[
r\binom Ar=A\binom{A-1}{r-1}
\]

also gives \(A\mid rL\). Consequently, with
\(D=\operatorname{lcm}(r,d_j)\),

\[
\boxed{A\mid D Y.} \tag{2}
\]

This immediately implies the general largest-prime restriction

\[
\boxed{P^+(A)\le\max\{j^2,r,k^2\},} \tag{3}
\]

where \(P^+(A)\) denotes the largest prime divisor of \(A>1\).
Equation (2), including its restrictions on prime powers, is stronger
than (3).

If \(M=j\ge21\), then \(r<10j\le j^2-j\), and

\[
d_j=\binom{j^2}{j}(j^2-j)!
\]

is a multiple of \(r!\), in particular of \(r\). Thus

\[
\boxed{M=j\ge21\quad\Longrightarrow\quad A\mid d_jY.} \tag{4}
\]

## 2. The lower branch forces a smooth interval

Assume \(B\le t\), hence \(r=B\).

### 2.1 The case \(j>\ell\)

The previously proved classification gives

\[
k\ge\ell+2,\qquad B<10j.
\]

If \(\ell\ge2\), unimodality implies

\[
k(k-1)<20j.
\]

Since \(j\ge21\), this forces \(k<j\): otherwise
\(k(k-1)\ge j(j-1)\ge20j\).
Every prime divisor of \(Y\) is therefore at most \(k^2<j^2\).
If \(\ell=1\), then \(Y=k^2\) and \(k=B<10j<j^2\), so its prime
divisors are again below \(j^2\).
Equation (4) now proves

\[
\boxed{B\le t, j>\ell\quad\Longrightarrow\quad
       A\text{ is }j^2\text{-smooth}.} \tag{5}
\]

Equivalently, **every one of the \(j\) consecutive integers**

\[
\boxed{i-j+1,i-j+2,\ldots,i}
\]

must be \(j^2\)-smooth. The equivalence follows from
\(i(i-1)\cdots(i-j+1)=j!A\).

### 2.2 The case \(\ell>j\)

Here the existing classification gives \(k=\ell+1=M+1\), \(B=k\).
In (2), every prime divisor of \(D\) is at most \(\max(j^2,B)\),
and every prime divisor of \(Y\) is at most \(k^2\). Thus

\[
\boxed{B\le t, \ell>j\quad\Longrightarrow\quad
       A\text{ is }(\ell+1)^2\text{-smooth}.} \tag{6}
\]

The same smoothness bound applies to the entire interval
\(i-j+1,\ldots,i\).

## 3. The case \(\ell=1\): both branches, and an explicit divisor

Suppose \(\ell=1\). Then \(M=j\ge21\), \(B=k\), and \(Y=B^2\).
Since \(B^2\equiv r^2\pmod A\), equation (4) gives

\[
\boxed{A\mid d_j r^2.} \tag{7}
\]

Because \(r<10j<j^2\), the integer on the right has no prime factor
above \(j^2\). Therefore

\[
\boxed{\ell=1\quad\Longrightarrow\quad
 A\text{ and every integer }i-j+1,\ldots,i
 \text{ are }j^2\text{-smooth}.} \tag{8}
\]

This covers both \(r=B\) and \(r=t\); the conclusion is not restricted
to the lower branch. For fixed \(j,r\), (7) restricts \(A\) to divisors
of the explicit integer \(d_jr^2\).

## 4. Even \(j\): two more consecutive smooth integers

In either of the following settings,

1. \(B\le t\) and \(j>\ell\); or
2. \(\ell=1\), in either branch,

suppose in addition that \(j\) is even. Then **all \(j+2\) integers**

\[
\boxed{i-j+1,\ldots,i,i+1,i+2}
\]

are \(j^2\)-smooth.

Only \(i+1\) and \(i+2\) remain to be checked. Let \(p>j^2\) be prime.
Since \(r<10j<p\), factorial denominators in \(\binom Ar\) and
\(\binom ij\) are invertible modulo \(p\).

If \(p\mid i+1\), then

\[
A\equiv\binom{-1}{j}=1\pmod p,\qquad X\equiv0\pmod p.
\]

If \(p\mid i+2\), then

\[
A\equiv\binom{-2}{j}=j+1\pmod p,\qquad X\equiv0\pmod p.
\]

In both cases the polynomial formula for \(\binom Ar\), together with
\(r\ge j+2\), gives \(L\equiv0\pmod p\), so \(Y\equiv0\pmod p\).
In setting 1, every prime divisor of \(Y\) is below \(j^2\), a
contradiction.

In setting 2, \(Y=B^2\) implies \(p\mid B\). If \(r=B\), this is
impossible since \(0<B=r<p\). If \(r=t\), then \(t=A-B\) is congruent
to either 1 or \(j+1\) modulo \(p\). Since \(0<t=r<p\), this forces
\(t=1\) or \(t=j+1\), contrary to \(r\ge j+2\).

## 5. Resultants in the upper branch

Assume now \(t\le B\), so \(r=t\), and put

\[
F_{\ell,t}(z)=P_\ell(z)+\ell!t,\qquad
R_\ell(t)=\operatorname{Res}_z(F_{\ell,t},G_\ell).
\]

These are integer polynomials, with \(R_\ell(t)\) an integer when
\(t\) is an integer. The standard Sylvester determinant/adjugate
identity supplies integer polynomials \(U,V\) such that

\[
R_\ell(t)=U(z)F_{\ell,t}(z)+V(z)G_\ell(z).
\]

At \(z=k\),

\[
F_{\ell,t}(k)=\ell!A,\qquad G_\ell(k)=(\ell^2)!Y.
\]

Combining this with (2) proves the exact divisibility

\[
\boxed{A\mid\operatorname{lcm}(t,d_j)R_\ell(t).} \tag{9}
\]

In particular,

\[
\boxed{M=j\ge21, t\le B\quad\Longrightarrow\quad
       A\mid d_jR_\ell(t).} \tag{10}
\]

### 5.1 A product of quadratic polynomials in \(t\)

For each integer \(s\), divide \(P_\ell(z)\) by the monic polynomial
\(z^2-s\), writing the remainder as

\[
P_\ell(z)\equiv U_\ell(s)z+V_\ell(s)\pmod{z^2-s},
\]

where \(U_\ell(s),V_\ell(s)\) are integers. Evaluating at the two roots
of \(z^2-s\), with multiplicity when \(s=0\), gives

\[
\boxed{R_\ell(t)=\prod_{s=0}^{\ell^2-1}
 \left((V_\ell(s)+\ell!t)^2-sU_\ell(s)^2\right).} \tag{11}
\]

Thus each large prime factor of \(A\) must occur in one of a prescribed
list of quadratic values in the *small outer gap* \(t\), unless the
resultant is zero. This restriction does not involve the unknown \(k\).

### 5.2 Exact classification of the zero-resultant exception

For positive integer \(t\),

\[
\boxed{R_\ell(t)=0\iff
 \ell\text{ is odd and }
 t=\binom{\ell+h-1}{\ell}
 \text{ for some integer }1\le h<\ell.} \tag{12}
\]

To verify this, a common root must be \(z=\pm\sqrt{s}\) for
\(0\le s<\ell^2\). For \(0\le x<\ell\), one has
\(|P_\ell(x)|<\ell!\), except that the non-strict inequality would
already suffice here. Indeed, putting \(a=\lfloor x\rfloor\), the
absolute product is bounded by
\((a+1)!(\ell-a-1)!\le\ell!\), with strictness away from the excluded
endpoint \(x=\ell\); integer \(x<\ell\) gives zero. Hence
\(P_\ell(\sqrt{s})+\ell!t\ne0\).

At \(z=-\sqrt{s}\), even \(\ell\) gives a nonnegative product, so
again no zero is possible. For odd \(\ell\), a zero is equivalent to

\[
\sqrt{s}(\sqrt{s}+1)\cdots(\sqrt{s}+\ell-1)=\ell!t.
\]

If \(s\) is not a perfect square, the left side is
\(a+b\sqrt{s}\) with integers \(a\ge0\), \(b>0\), as follows by
expanding the product, so it is irrational. Thus \(s=h^2\) with
\(1\le h<\ell\), yielding (12). Conversely, each listed value does
give the common root \(z=-h\).

For an actual remaining solution, the previous bound \(t>\varphi M\)
excludes \(h=1\) and \(h=2\). The cases \(h\ge3\) must not be silently
discarded. In a zero-resultant family, (9) is true but vacuous.

### 5.3 Explicit example: \(\ell=2\)

Here \(P_2(z)=z^2-z\), so

\[
R_2(t)=\prod_{s=0}^3((2t+s)^2-s)
 =64t^3(t+1)(2t^2+4t+1)(2t^2+6t+3).
\]

Let \(A_{>j^2}\) denote the product of all prime powers \(p^{v_p(A)}\)
with \(p>j^2\). For an upper-branch solution with \(\ell=2\),
\(M=j\ge21\) and \(t<10j\), and therefore

\[
\boxed{A_{>j^2}\mid
       (2t^2+4t+1)(2t^2+6t+3).} \tag{13}
\]

Indeed, the other factors in \(d_jR_2(t)\) have all their prime divisors
at most \(j^2\), including \(t+1\le10j<j^2\). Consequently

\[
\boxed{P^+(A)\le 2t^2+6t+3\le200j^2+20j-1.} \tag{14}
\]

The lower branch with \(\ell=2\) has the stronger bound (5).

## 6. A dual divisibility for the upper branch

The elementary Vandermonde identity gives

\[
\binom{B+t}{t}-1
 =\sum_{s=1}^t\binom Bs\binom ts.
\]

Let \(q_t=\operatorname{lcm}(1,2,\ldots,t)\). Since
\(s\binom Bs=B\binom{B-1}{s-1}\),

\[
B\mid q_t(L-1).
\]

Together with \(B\mid d_\ell Y\), this implies

\[
\boxed{B\mid\operatorname{lcm}(q_t,d_\ell)(X-1).} \tag{15}
\]

If \(M=\ell\ge21\), then \(t<10\ell\le\ell^2-\ell\), so
\(t!\mid d_\ell\) and hence

\[
\boxed{M=\ell\ge21, t\le B\quad\Longrightarrow\quad
       B\mid d_\ell(X-1).} \tag{16}
\]

Set

\[
S_j(t)=\operatorname{Res}_z
 \left(P_j(z)-j!t, G_j(z)-(j^2)!\right).
\]

Since the two polynomial values at \(z=i\) are respectively
\(j!B\) and \((j^2)!(X-1)\), the same integer resultant identity gives

\[
\boxed{M=\ell\ge21, t\le B\quad\Longrightarrow\quad
       B\mid d_\ell S_j(t).} \tag{17}
\]

This assertion remains valid if the resultant is zero, but is then
vacuous. No general classification of its zero cases is asserted here.
For \(j=1\), \(S_1(t)=t^2-1\), recovering

\[
\boxed{B\mid d_\ell(t^2-1).} \tag{18}
\]

Since \(t+1<\ell^2\), this forces \(B\), and all \(\ell\) consecutive
integers \(k-\ell+1,\ldots,k\), to be \(\ell^2\)-smooth.
The case \(j=1\) is also developed independently in the companion work.

## 7. A sharper necessary condition when \(i=k=p^a\)

The earlier same-row argument forces \(B=p^a\) and
\(\ell\in\{1,p^a-1\}\). Put \(n=p^a\), let
\(b=v_p(j)<a\), and put \(c=a-b\).

We first record an elementary lemma. If \(N\ge p^a\), write
\(N=q p^a+s\), \(0\le s<p^a\). Then

\[
\boxed{v_p\binom N{p^a}=v_p(q),\qquad
 \frac{\binom N{p^a}}{p^{v_p(q)}}
 \equiv\frac q{p^{v_p(q)}}\pmod p.} \tag{19}
\]

To prove this, single out the factor \(q p^a\) in the numerator
product. Every other factor has the form \(q p^a+u\) with
\(0<|u|<p^a\), so it has the same \(p\)-adic valuation and normalized
residue as \(u\). The product of these factors, divided by
\((p^a-1)!\), is a \(p\)-adic unit. Its residue is

\[
\frac{(-1)^{p^a-s-1}}{\binom{p^a-1}{s}}
\equiv(-1)^{p^a-1}\equiv1\pmod p,
\]

where the middle congruence follows from the coefficient identity
\((1+z)^{p^a-1}\equiv\sum_{s=0}^{p^a-1}(-z)^s\pmod p\).
This proves (19).

The identity \(u\binom Nu=N\binom{N-1}{u-1}\) shows, for
\(0<u<p^{2a}\),

\[
v_p\binom{p^{2a}}u=2a-v_p(u),
\]

because \(\binom{p^{2a}-1}{u-1}\) is a \(p\)-adic unit.
Consequently

\[
v_p(X)=2c,\qquad v_p(Y)=2a.
\]

The previously proved necessary condition \(p\mid j\) means \(b>0\),
so the valuations differ and the right side has valuation exactly
\(2c\). Applying (19) to \(N=A\) therefore gives

\[
\boxed{v_p\left\lfloor\frac{A}{p^a}\right\rfloor=2(a-v_p(j)).} \tag{20}
\]

Writing \(j=p^b u\), \(p\nmid u\), and comparing normalized residues
also gives

\[
\boxed{
\frac{\left\lfloor A/p^a\right\rfloor}{p^{2c}}
\equiv (-1)^{j-1}u^{-2}\pmod p.} \tag{21}
\]

Thus a prescribed block of \(2c\) base-\(p\) digits of \(A\), starting
at position \(a\), must vanish, and the next digit is prescribed by
\(j\). This is stricter than \(p\mid j\), but it does not by itself
exclude all prime powers and is not presented as doing so.

## Scope and next obstruction

The smoothness and divisibility conditions above are uniform in the
unbounded upper indices. They remove infinite families immediately and
give explicit divisor restrictions for the remaining families.
However, they do not bound \(M\). A general theorem asserting that every
relevant binomial coefficient has a prime factor above \(M^2\) has not
been proved here, and must not be assumed. The known possibility of
zero resultants in (12) also requires explicit handling in any future
argument using those resultants.
