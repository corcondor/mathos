# v15: a uniform square-root sparsity bound

Date: 2026-11-06 JST.

## Scope and statement

The original equation remains

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

This note concerns only the branch \(\ell=1,\ j=i-3\). Write
\(n=i\), \(A=\binom n3\), and \(r=\min(k,A-k)\). Both choices of
the outer branch are included. We use the previously established inputs
from `v6_offset_composite.md`, Sections 1 and 5:

\[
n\ge104,\qquad 3n<r<10n/3,
\tag{1}
\]

\[
Q=\frac n{\gcd(n,3)}\frac{n-1}{\gcd(n-1,6)}\mid r^3.
\tag{2}
\]

Let \(T(X)\) count the integers \(n\le X\) that can occur in a solution
in this branch, without counting different values of k more than once.
For every real \(X\ge104\),

\[
\boxed{
T(X)\le 4\sqrt{21X}\,H_{\lfloor X^{1/3}\rfloor}
\le4\sqrt{21X}\left(1+\frac{\log X}{3}\right).
}
\tag{3}
\]

Here \(H_M=\sum_{c=1}^M1/c\). In particular,

\[
\boxed{T(X)=O\bigl(X^{1/2}\log X\bigr).}
\tag{4}
\]

This improves the earlier bound \(O(X^{3/4})\). The proof does not
enumerate primes, use a finite search cutoff, invoke the v14 Thue
classification, or assume an upper bound for H, T, or n. It counts a
necessary superset; it does not prove existence or exclude all indices.
No new Lean execution or CAS completeness result is used in this note.

## 1. Retain the full cubic defect

For a positive integer m define

\[
c_3(m)=\prod_p p^{\lceil v_p(m)/3\rceil},\qquad
f(m)=\frac{m}{c_3(m)}.
\tag{5}
\]

Thus \(m\mid u^3\) if and only if \(c_3(m)\mid u\). The function
\(c_3\) is multiplicative on coprime arguments. If d divides m, the
prime-wise inequality

\[
\left\lceil\frac{v_p(m)}3\right\rceil
\le v_p(d)+\left\lceil\frac{v_p(m)-v_p(d)}3\right\rceil
\]

shows that

\[
c_3(m)\le d\,c_3(m/d).
\tag{6}
\]

Put

\[
g=\gcd(n,3),\quad d=\gcd(n-1,6),\quad
c_1=c_3(n/g),\quad c_2=c_3((n-1)/d).
\]

The two factors of Q are coprime. Equation (2) implies
\(c_1c_2\mid r\), and (6) gives

\[
c_3(n)c_3(n-1)\le gd\,c_1c_2\le6r<20n.
\tag{7}
\]

Indeed \(gd\mid6\): if \(g=3\), then 3 does not divide n-1, so
\(d\mid2\); if \(g=1\), then \(d\mid6\). Substituting (5) into
(7) and cancelling n proves

\[
\boxed{n-1<20f(n)f(n-1).}
\tag{8}
\]

An alternative derivation uses the v10--v14 inputs
\(6Hr^3=Tn(n-1)(n-2)\) and \(H\mid n-2\). Cancelling H gives
\(n(n-1)\mid6r^3\), hence
\(c_3(n)c_3(n-1)=c_3(n(n-1))\mid6r\), which again gives (7).
This alternative confirms that no particular choice of the primitive
defect H is required for (8).

## 2. A canonical factorization converts the condition into a simple ratio

Every positive integer m has a unique expression

\[
\boxed{m=a b^2 c^3,\qquad
a,b\text{ squarefree},\quad\gcd(a,b)=1.}
\tag{9}
\]

Here c is a positive integer; it need not be coprime to a or b. In the
prime factorization, write \(v_p(m)=3h+e\) with \(e\in\{0,1,2\}\):
put \(p^h\) in c, put p in a if e=1, and put p in b if e=2. This proves
existence and uniqueness, including cases where c shares a prime with
a or b.

Equation (5) becomes

\[
\boxed{c_3(m)=abc,\qquad f(m)=bc^2,\qquad
\frac{m}{f(m)^2}=\frac ac.}
\tag{10}
\]

At least one of \(f(n)^2,f(n-1)^2\) exceeds \((n-1)/20\), by (8).
If the larger one corresponds to m=n-1, then \(m<20f(m)^2\). If it
corresponds to m=n, then

\[
f(n)^2>\frac{n-1}{20}>\frac n{21}
\qquad(n\ge104>21).
\]

In either case there is an \(m\in\{n,n-1\}\) satisfying

\[
\boxed{m<21f(m)^2,\quad\text{or equivalently}\quad a<21c.}
\tag{11}
\]

This is a uniform, purely arithmetic restriction on every possible
index, stronger than replacing f(m) by the entire largest square
divisor of m. It is the actual cubic defect that yields the new count.

## 3. Count all witnesses

Let \(E_C(X)\) be the number of positive integers \(m\le X\) for which
the canonical factorization (9) satisfies \(a\le Cc\), where \(C\ge1\).
By uniqueness, E_C(X) is at most the number of all positive integer
triples a,b,c with \(a\le Cc\) and \(ab^2c^3\le X\), even after
discarding squarefreeness and coprimality. In particular,

\[
\begin{aligned}
E_C(X)
&\le\sum_{c=1}^{\lfloor X^{1/3}\rfloor}
  \sum_{a=1}^{\lfloor Cc\rfloor}
  \left\lfloor\sqrt{\frac{X}{ac^3}}\right\rfloor\\
&\le\sqrt X\sum_{c=1}^{\lfloor X^{1/3}\rfloor}
  c^{-3/2}\sum_{a=1}^{\lfloor Cc\rfloor}a^{-1/2}\\
&\le2\sqrt{CX}\sum_{c=1}^{\lfloor X^{1/3}\rfloor}\frac1c.
\end{aligned}
\tag{12}
\]

The final step uses
\(\sum_{a=1}^M a^{-1/2}\le2\sqrt M\), proved by integration of the
decreasing function \(t^{-1/2}\). There is no probabilistic independence
assumption for n and n-1.

Each possible n has a witness m=n or m=n-1 with m<=X, by (11). Each
fixed m accounts for at most two indices n, namely m and m+1. Therefore

\[
T(X)\le2E_{21}(X)
\le4\sqrt{21X}\,H_{\lfloor X^{1/3}\rfloor}.
\]

Finally, \(H_M\le1+\log M\le1+(\log X)/3\), which proves (3).

## 4. A smaller constant using the logarithmic gap

The exponent improvement (4) only needs r<10n/3. The logarithmic gap
from v6 additionally gives, for n>=1024,

\[
c_3(n)c_3(n-1)\le6r
<\left(18+\frac{9}{2\log n}\right)n
<\frac{75}{4}n,
\tag{13}
\]

where \(\log n>6\). It follows that

\[
f(n)f(n-1)>\frac4{75}(n-1).
\]

Since \(75n<76(n-1)\) for n>76, one of the two witnesses satisfies
\(m<19f(m)^2\), hence \(a<19c\). There are at most 920 integers
104<=n<1024. Thus a second explicit bound is

\[
\boxed{
T(X)\le920+4\sqrt{19X}\,H_{\lfloor X^{1/3}\rfloor}
\le920+4\sqrt{19X}\left(1+\frac{\log X}{3}\right).
}
\tag{14}
\]

For a given X one may take the smaller of (3) and (14). The constant
improvement is secondary; the new exponent is already unconditional on
the established elementary branch inputs.

## 5. Exact checks and their scope

`v15_cubic_defect_sparsity_checks.py` checks the canonical identities
against independently computed prime-exponent formulas; verifies the
two-factor inequality and witness ratio for all indices in a specified
small range that pass the exact common-divisor/interval condition; and
counts the witness set and its integer-triple upper bound exactly.

The counts do not represent solutions of the original binomial
equation. They are checks on the uniform proof, not a replacement for
it. The mathematical bound (3) applies to arbitrary X, not merely to
the checked range. No claim of a matching lower bound or optimality is
made.

For context, even retaining only the earlier square-divisor inequality
n<=20U^2V^2 would improve O(X^(3/4)) to O(X^(2/3)): split at Z, count
large square divisors by 2X/Z, and for U,V<=Z use the single CRT class
modulo U^2V^2 and n<=20U^2V^2 to obtain at most 20Z^2 values. The present
proof retains more of the cubic information and gives the stronger
square-root/logarithm bound.


Reproduce the finite consistency checks with:

```sh
python3 v15_cubic_defect_sparsity_checks.py --limit 100000 --output reproduced_sparsity_checks.json
```

The written proof was independently audited by the root and a separate
AI collaborator. All three agree on the general counting argument and
its constants. These are internal mathematical reviews, not external
peer review or a Lean kernel check.
