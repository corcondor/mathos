# v15: a height bound controlled by actual cube factors

Date: 2026-11-06 JST.

## 1. Statement

We retain the original squared-index equation and the branch
ell=1, j=i-3. Put n=i, r=min(k,binom(n,3)-k), and

\[
M=\gcd(n,3)\gcd(n-1,6)\in\{1,2,3,6\},\qquad
Q=\frac{n(n-1)}M.
\]

Let

\[
\boxed{\kappa=\prod_p p^{\lfloor v_p(Q)/3\rfloor}.}
\tag{1}
\]

Thus kappa is the largest positive integer whose cube divides Q. In
particular it measures actual cube factors, rather than the cube-free
part left after removing them. The necessary conditions imply

\[
\boxed{\log n<28\kappa,\qquad n<e^{28\kappa}.}
\tag{2}
\]

This bound is uniform in all prime factors and independent of the
primitive defect H. Together with the separate Pell exclusion in
[v15_pell_square_divisor.md](v15_pell_square_divisor.md), we have

\[
\boxed{\kappa\ge2,\qquad \kappa>\frac{\log n}{28}.}
\tag{3}
\]

The coefficient 28 is a convenient rigorous constant; optimality is
not asserted. This result is not a bound on n independent of kappa.

## 2. The integer that supplies the separation

The existing branch inputs, valid for both k choices, are

\[
n\ge104,\qquad Q\mid r^3,\qquad 3n<r<10n/3,
\tag{4}
\]

and, for n>=1024,

\[
r<3n+\frac{3n}{4\log n}.
\tag{5}
\]

They are recorded in [v6_offset_composite.md](v6_offset_composite.md)
and [v6_common_divisor.md](v6_common_divisor.md).

Write Q in its canonical form

\[
Q=a b^2\kappa^3,
\]

where a,b are coprime square-free positive integers. Kappa may share
primes with a or b. The least positive integer whose cube is divisible
by Q is ab*kappa. Therefore (4) gives r=ab*kappa*v for some positive
integer v, and

\[
\boxed{K=\frac{\kappa r^2}{Q}=a v^2\in\mathbb Z_{>0}.}
\tag{6}
\]

On the other hand,

\[
K=M\kappa\frac{r^2}{n(n-1)}>9M\kappa.
\tag{7}
\]

Both K and 9M*kappa are integers. We show that log(n)>=28*kappa
would place K strictly below the next integer.

## 3. Exact upper comparison

Suppose log(n)>=28*kappa. Since e>2,

\[
n\ge e^{28\kappa}>2^{28\kappa}>8192\kappa+1.
\tag{8}
\]

For completeness, 2^kappa>=kappa+1 for every integer kappa>=1,
and 2^(27*kappa)>=2^27, so the last inequality is immediate.
In particular n>=1024 and n-1>8192*kappa.

Put eta=3/(4 log(n)). Then 0<eta<=3/(112*kappa), and (5) gives

\[
\begin{aligned}
K-9M\kappa
&<M\kappa(6\eta+\eta^2)
  +\frac{M\kappa}{n-1}(9+6\eta+\eta^2)\\
&<6\left(\frac9{56}+\frac9{12544}\right)
  +\frac6{8192}\left(9+\frac9{56}+\frac9{12544}\right)\\
&=\frac{50111163}{51380224}<1.
\end{aligned}
\tag{9}
\]

The second line uses M<=6 and kappa>=1. All inequalities are strict
where needed because the bound on r in (5) and (8) is strict. The
last rational difference from 1 is exactly 1269061/51380224>0.

Equations (7) and (9) say

\[
9M\kappa<K<9M\kappa+1,
\]

contradicting integrality. This proves (2), without a finite search
or a CAS computation.

## 4. Connection to the Pell exclusion

If kappa=1, Q is cube-free. Prime by prime, Q|r^3 then implies Q|r^2:
each positive exponent of Q is 1 or 2, while r contains that prime at
least once. The independent v15 Pell argument excludes Q|r^2 for the
original equation, proving kappa>=2.

More precisely, that argument proves that the smallest positive integer
t with Q|r^t is exactly 3. Some prime must satisfy
2v_p(r)<v_p(Q)<=3v_p(r). This exponent obstruction is stronger than
merely kappa>=2. For example exponents equal to 4 produce a cube factor
but cannot by themselves witness Q not dividing r^2.

Since Q is a product of two coprime factors from n and n-1, write
kappa=kappa0*kappa1 for their largest cube-root factors. At least one
of these factors exceeds sqrt(log(n)/28), and its cube divides n or
n-1. This is a consequence, not a new bound on the number of prime
factors or their sizes.

## 5. Verification boundary

The proof is a written elementary deduction from (4)-(5). A separate
AI collaborator independently checked the canonical identity, integer
separation, every endpoint and the rational constant (9), and reported
no correction needed. The root checked the same deductions. Exact
constants and review scope are recorded in
[v15_theory_audit.json](v15_theory_audit.json).

No new Lean run, DeepSeek call, CAS complete solver, or Selmer computation
is part of this proof. The original four-variable problem remains
unresolved. The exponent bound and kappa>=2 must not be described as
having solved the whole offset-three branch.
