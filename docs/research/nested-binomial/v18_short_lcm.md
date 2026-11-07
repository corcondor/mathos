# v18: a one-digit loss and a shorter square-LCM condition

Date: 2026-11-07 JST. Written mathematical deductions with exact integer
certificates. No new Lean execution, DeepSeek API call, complete CAS solver,
or external peer review is claimed.

## 1. Scope and inherited inputs

Retain the original squared-index equation
\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}
\]
in the branch \(\ell=1,\ j=i-3\). Put
\[
n=i,\quad A=\binom n3,\quad m=6n-9,\quad
B=\binom{n^2}{m},\quad r=\min(k,A-k),
\]
\[
M=\gcd(n,3)\gcd(n-1,6),\qquad Q=\frac{n(n-1)}M.
\]
The inherited necessary conditions are
\[
n\ge104,\quad Q\mid r^3,\quad 3n<r<10n/3,\quad
\binom Ar=B+k^2,\quad k\in\{r,A-r\}.
\tag{1}
\]
Set
\[
\mathcal C=\{2,3,5,6,7,8,10,11,12,13,14,15\},\qquad
\mathcal C(n)=\{c\in\mathcal C:6\mid(c+2)n-3c\}.
\]
For \(c\in\mathcal C(n)\), let
\[
N_c=n^2-c,\qquad a_c=\frac{(c+2)n-3c}{6}.
\]
Then
\[
A-a_c=\frac{(n-3)N_c}{6},\qquad 0<a_c<r.
\tag{2}
\]
The v16 quadratic-neighbor theorem gives
\[
P^+(N_c)<r.
\tag{3}
\]
This strict prime bound is an input, not a consequence assumed from the
stronger square-LCM theorem below. Its proof is in
v16_quadratic_neighbors.md; the common notation and exact valuation
identity are in v17_quadratic_prime_powers.md.

For a positive integer \(u\), let \(L_u=\operatorname{lcm}(1,\ldots,u)\).
For each prime \(p\), write \(J_p=\lfloor\log_p r\rfloor\), defined by
\(p^{J_p}\le r<p^{J_p+1}\).

**Main conclusions.**

1. For every \(c\in\mathcal C(n)\) and every prime \(p\ge11\),
   \[
   \boxed{v_p(B)\ge v_p(N_c)-1.}
   \tag{4}
   \]
2. In both branches, the v17 simultaneous excess theorem can use \(L_r\)
   in place of \(L_m\).
3. In the small branch \(k=r\), all primes and all exponents satisfy
   \[
   \boxed{N_c\mid L_r^2\quad(c\in\mathcal C(n)).}
   \tag{5}
   \]
   In fact \(L_r=L_{r-1}\) under (1). Every exact odd prime power
   \(p^e\parallel N_c\), with \(w=N_c/p^e\), consequently satisfies
   \[
   \boxed{p<12w.}
   \tag{6}
   \]

Theorem (5) is not asserted for the complementary branch.

## 2. The endpoint obstruction has no large square prime factor

For \(c\in\mathcal C\) and \(0\le t\le c\), define
\[
D_{c,t}=(9+t)^2-36c.
\]
There are 118 such integers. Each is nonzero because \(c\) is not a square.
Moreover,
\[
-459\le D_{c,t}\le(c-9)^2\le49.
\tag{7}
\]

**Lemma.** No square of a prime \(p\ge11\) divides any \(D_{c,t}\).

If \(D_{c,t}>0\), this follows from \(D_{c,t}\le49<p^2\).
If it is negative and divisible by \(p^2\), write
\(D_{c,t}=-u p^2\). Since \(459<4\cdot11^2\), one has \(u\in\{1,2,3\}\).
Reduction modulo 4 of
\[
(9+t)^2=36c-u p^2
\]
forces \(u=3\). Reduction modulo 9 then gives
\((9+t)^2\equiv-3p^2\equiv6\pmod9\), impossible for a square.
This proves the lemma uniformly; the accompanying 118-row check is a
reproduction of the small constants, not the universal proof.

Now let \(e=v_p(N_c)\ge2\), with \(p\ge11\).
Since \(c\le15<p^2\), the residue of \(n^2\) modulo \(p^a\) is exactly
\(c\) for every \(2\le a\le e\).
We claim
\[
m\bmod p^2>c.
\tag{8}
\]
Otherwise \(t=m\bmod p^2\) lies in \([0,c]\). Since \(m+9=6n\),
\[
D_{c,t}\equiv(m+9)^2-36n^2\equiv0\pmod{p^2},
\]
contradicting the lemma.

For every \(2\le a\le e\), the residue \(m\bmod p^a\) is at least
\(m\bmod p^2\), hence exceeds \(c=n^2\bmod p^a\).
The corresponding term in Legendre's factorial-floor formula is therefore
1:
\[
\left\lfloor\frac{n^2}{p^a}\right\rfloor
-\left\lfloor\frac m{p^a}\right\rfloor
-\left\lfloor\frac{n^2-m}{p^a}\right\rfloor=1.
\]
These \(e-1\) terms prove (4). For \(e=0,1\), (4) is automatic.
No condition \(p^e>m\), no numerical cutoff in \(p\), and no restriction
on \(e\) is used in (4).

## 3. Both branches: move the simultaneous excess from L_m to L_r

For a positive integer \(u\), let \(u_{[\ge17]}\) retain only its prime
factors at least 17. Define
\[
\mathcal R_r=
\prod_{c\in\mathcal C(n)}
\left(\frac{N_c}{\gcd(N_c,L_r)}\right)_{[\ge17]}.
\tag{9}
\]

**Theorem.** Both branches obey
\[
\boxed{\mathcal R_r\mid k^2,\quad
\gcd(\mathcal R_r,Q)=1,\quad
\mathcal R_r^3Q^2\mid k^6.}
\tag{10}
\]
For \(k=r\),
\[
\boxed{\mathcal R_r<(225n)^{2/3}.}
\tag{11}
\]

Let \(p\ge17\) divide \(N_c\), and put \(e=v_p(N_c)\), \(J=J_p\).
By (3), \(J\ge1\). Only \(e>J\) contributes to (9).
By (2), \(p^e\mid A-a_c\). The binomial divisibility lemma proved in v17,
with lower-index ceiling \(r\), yields
\[
v_p\binom Ar\ge e-J.
\]
The new estimate (4) gives \(v_p(B)\ge e-1\ge e-J\).
Their difference \(k^2\) is therefore divisible by \(p^{e-J}\).

Distinct \(N_c\) do not share a prime at least 17, because their
differences have absolute value at most 13. These local divisibilities
multiply. Such a prime cannot divide \(n\) or \(n-1\), since
\(0<c<p\) and \(0<c-1<p\); thus it is coprime to \(Q\).

The established identity \(Q\mid A\) and \(Q\mid r^3\) imply \(Q\mid k^3\)
in either branch. Combining with \(\mathcal R_r\mid k^2\) gives (10).
For the small branch,
\[
\mathcal R_r^3\le\frac{r^6}{Q^2}.
\]
From (1), \(M\le6\), and \(n\ge104\),
\[
\frac{r^3}{Q}
<\frac{1000M}{27}\frac{n^2}{n-1}
\le\frac{2000}{9}\frac{104}{103}n
=\frac{208000}{927}n<225n.
\tag{12}
\]
This proves (11). Since \(r<m\), (9) contains at least the v17 excess
defined with \(L_m\), and may retain extra prime powers.

## 4. Small branch: every N_c divides the shorter square L_r²

Assume \(k=r\). Fix \(c\in\mathcal C(n)\) and a prime \(p\mid N_c\).
Let \(e=v_p(N_c)\), \(J=\lfloor\log_p r\rfloor\ge1\).
Suppose, for a contradiction, that \(e>2J\).

Since \(n<r/3<p^{J+1}/3\),
\[
p^e\le N_c<n^2<\frac{p^{2J+2}}9.
\]
It follows that
\[
\boxed{e=2J+1,\qquad
w=\frac{N_c}{p^e}\in\mathbb Z_{>0},\qquad w<p/9,\qquad p\ge11.}
\tag{13}
\]
For these primes, (4) and the outer binomial divisibility lemma give
\[
v_p(B)\ge e-1\ge e-J,\qquad
v_p\binom Ar\ge e-J.
\]
Writing \(s=v_p(r)\), the original equation implies
\[
\boxed{s\ge\left\lceil\frac{J+1}{2}\right\rceil.}
\tag{14}
\]

### The possible overlap with Q

Put \(d=v_p(Q)\). If \(p\mid n\), then \(p\mid c\).
As \(p\ge11\) and \(2\le c\le15\), this would give \(c=p\), and
\(v_p(n^2-c)=1\), contradicting \(e\ge3\). Thus \(p\nmid n\).

If \(p\mid n-1\), then \(c\equiv1\pmod p\). The only possibilities are
\[
(p,c)=(11,12)\quad\text{or}\quad(13,14).
\tag{15}
\]
Write \(n=1+pz\). The identity
\[
n^2-(p+1)=p(2z-1+pz^2)
\]
and \(e\ge3\) give \(2z\equiv1\pmod p\), hence \(v_p(n-1)=1\).
As \(p\nmid M\), this means \(d=1\). In all other cases \(d=0\).

Because \(Q\mid r^3\), the positive integer \(r^3/Q\) is divisible by
\(p^{3s-d}\). By (12) and \(3n<r<p^{J+1}\),
\[
p^{3s-d}<225n<75r<75p^{J+1}.
\]
Using (14),
\[
\boxed{
p^{\,3\lceil(J+1)/2\rceil-d-J-1}<75.
}
\tag{16}
\]

If \(d=0\), the exponent on the left is at least 2 for every \(J\ge2\).
Since \(p\ge11\), this is impossible. Thus \(J=1\), and then \(p<75\).

If \(d=1\), the prime is 11 or 13 by (15). The exponent in (16) is at
least 2 for \(J=2\) or \(J\ge4\), so the only possibilities are
\(J=1\) or \(J=3\). The \(J=1\) cases are already within \(p<75\).
The two additional cases have
\[
(p,c,e,w)=(11,12,7,1),\quad(13,14,7,1).
\tag{17}
\]

### A complete finite square reconstruction

There are 17 primes \(11\le p<75\). For each, (13) permits
\(1\le w\le\lfloor(p-1)/9\rfloor\), and \(c\) has 12 possible values.
This is **828** triples \((p,w,c)\). The equation to check is
\[
n^2=p^3w+c.
\tag{18}
\]
Every nonsquare is certified by its two consecutive bounding squares.
Exactly three squares occur:

| p | w | c | n | Disposition |
|---:|---:|---:|---:|---|
| 13 | 1 | 12 | 47 | \(n<104\); also \(a_c\) is not integral |
| 23 | 2 | 2 | 156 | \(Q\mid r^3\) forces \(4030\mid r\) |
| 61 | 6 | 3 | 1167 | \(Q\mid r^3\) forces \(226787\mid r\) |

For \(n=156\), one has \(M=3\) and
\[
Q=8060=2^2\cdot5\cdot13\cdot31.
\]
The least positive integer \(F_3\) with \(Q\mid F_3^3\) is 4030.
It exceeds \(10n/3=520\). For \(n=1167\), one has \(M=6\) and
\[
Q=226787=11\cdot53\cdot389.
\]
Here \(F_3=226787>10n/3=3890\). Both contradict (1).

Finally, the two numbers in (17) are nonsquares:
\[
4414^2<11^7+12=19487183<4415^2,
\]
\[
7921^2<13^7+14=62748531<7922^2.
\]
This exhausts every exception allowed by (13)-(16), without any chosen
cutoff in \(n\). Therefore \(e\le2J\) for every prime, proving (5).

## 5. Consequences and scope

### All applicable neighbors at once

Because primes at least 17 occur in at most one \(N_c\),
\[
\boxed{
\prod_{c\in\mathcal C(n)}(N_c)_{[\ge17]}\mid L_r^2
\quad(k=r).
}
\tag{19}
\]
For \(n\equiv3\pmod6\), all twelve factors are applicable. The theorem is
a divisibility condition, not a claim that these integers are squarefree.

The square offsets \(c=0,1,4,9,16\) also satisfy \(n^2-c\mid L_r^2\),
without an extra hypothesis, since \(n^2-c=(n-\sqrt c)(n+\sqrt c)\) and
both factors are positive and below \(r\). The nontrivial statement here
is the nonsquare family \(\mathcal C(n)\).

### The last index can be r−1

The coprime integers
\[
Q_0=n/\gcd(n,3)>1,\qquad Q_1=(n-1)/\gcd(n-1,6)>1
\]
multiply to \(Q\), so \(Q\) has at least two different prime factors.
Since \(Q\mid r^3\), \(r\) cannot be a prime power. The least common
multiple changes from \(L_{r-1}\) to \(L_r\) only at a prime power.
Thus \(L_r=L_{r-1}\) under (1).

### Odd exact prime powers have a linear cofactor bound

Let \(p^e\parallel N_c\), with odd \(e=2h+1\), and put \(w=N_c/p^e\).
The bound \(e\le2J\) implies \(h+1\le J\), so
\[
p^{e+1}\le p^{2J}\le r^2<\frac{100}{9}n^2<12(n^2-c).
\]
The final inequality holds for \(n\ge104,c\le15\):
\((8/9)n^2>12c\). Dividing by \(p^e\) proves \(p<12w\).
This covers arbitrary odd exponents; it does not bound all \(w\).

The positive-neighbor theorem \(n^2+1\mid L_m^2\) from v17 remains
a separate result for \(n\equiv3\pmod6\), in both branches.
It is not silently strengthened here to \(L_r^2\).

## 6. Reproduction and verification boundary

Run "python3 v18_short_lcm_checks.py" in this directory.
The standard-library script records all 118 endpoint constants, every one
of the 828 cubic square checks, the two seventh-power checks, and both
forced-divisor exclusions. It also checks the exact constants and a
separately labeled set of supporting valuation examples.

The universal valuation and finite-coverage arguments are the written
proof above. Supporting finite samples are not used as extrapolated
proofs. The complete 830 square candidates have a domain established
before computation. All original solutions, the complementary branch as
a whole, and the other \((j,\ell)\) branches remain unresolved.

