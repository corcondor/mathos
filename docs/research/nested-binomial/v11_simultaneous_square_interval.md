# Combining the mixed prime conditions by CRT on squared values

## Scope and the uniform compression theorem

The equation remains

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

We work in the branch \(\ell=1,\ j=i-3\), with the v10 definitions
\(n=i,A=\binom n3,X=\binom{n^2}{6n-9},r=\min(k,A-k)\),
the recovered defect E, B=A/E, and F=c_3(B). In particular F divides r.
The complete v11 effective-defect calculation gives

\[
H=A/\gcd(A,r^3)\ge14.
\]

For **every** such solution, the necessary simultaneous local conditions can
be tested as follows. Enumerate the unitary divisors Z of E (whole prime-power
blocks are assigned to Z or to H=E/Z). For each eligible Z there are at most
**four integer squared values** to check. If E>=512 there is at most **one**
per Z. These bounds have no upper limit on n, E, or the number of their prime
factors. No enumeration of all choices of local square roots is needed.

The algorithm applies **to each prescribed candidate n**, after its E, K,
and local units have been computed. It bounds the remaining outer-index
candidates. Each squared value determines r; the original equation must
then be checked for k=r and k=A-r. Thus four square tests may lead to eight
original-equation substitutions. It does not assert that there are only
four possible n values.

This is a necessary-condition reduction. E remains unbounded, and this does
not show that every resulting candidate is impossible or solves the original
equation. Synthetic positive reduced examples are included in the checker
specifically to make that distinction testable.

## 1. Retain the cube-completion factor

Put

\[
K=F^3/B.
\]

This is a positive integer. At each prime its exponent is
\(3\lceil v_p(B)/3\rceil-v_p(B)\), hence is 0, 1, or 2.
If p divides E, the critical-prime description in v10 has
\(v_p(B)=3t_p\), so p does not divide K. Therefore

\[
\boxed{\gcd(K,E)=1.}
\tag{1}
\]

Writing r=Fu, keep the exact v10 quotient rather than dropping K:

\[
\boxed{162E<Ku^3<229E.}
\tag{2}
\]

At each prime power \(p^d\Vert E\), v10 proved

\[
u\equiv0\pmod{p^d}\quad\hbox{or}\quad
u^2\equiv-\lambda_p\pmod{p^d},
\]

where lambda_p is a unit. Thus Z=gcd(E,u) is a **unitary divisor** of E:
all of p^d belongs to Z or none of it does. Write

\[
E=ZH,\qquad u=Zv,\qquad J=KZ^2.
\]

Then gcd(Z,H)=gcd(v,H)=1, and (2) becomes

\[
\boxed{162H<Jv^3<229H.}
\tag{3}
\]

Moreover, H is exactly A/gcd(A,r^3), so H>=14. The integer
T=Jv^3 is coprime to H, consistent with the primitive cubic curves in
[the effective-defect proof](v11_effective_defect_cf.md).

## 2. Apply CRT before taking square roots

For the prime powers retained in H, Z is invertible and

\[
v^2\equiv-\lambda_p Z^{-2}\pmod{p^d}.
\tag{4}
\]

The Chinese remainder theorem combines (4) into one residue R:

\[
\boxed{v^2\equiv R\pmod H,\qquad 1\le R<H,\quad\gcd(R,H)=1.}
\tag{5}
\]

The residue is unique even when the quadratic congruence has multiple roots
or has no roots. Consequently every candidate satisfies

\[
\boxed{v^2=R+mH\quad\text{for an integer }m\ge0.}
\tag{6}
\]

The nonnegativity follows because m<=-1 would give R+mH<0. For primes put
in Z, u=Zv already satisfies the zero congruence. For primes put in H, (5)
ensures v is a unit, so gcd(E,u)=Z is recovered exactly. The construction
therefore captures both directions of the stated *reduced local conditions*.
Additional conditions from the full original equation are still necessary.

## 3. The interval for m has uniformly bounded length

By (3), the squared value in (6) lies strictly between

\[
L_*=(162H/J)^{2/3},\qquad U_*=(229H/J)^{2/3}.
\]

The corresponding interval for m has length

\[
\begin{aligned}
\frac{U_*-L_*}{H}
&=\frac{229^{2/3}-162^{2/3}}{(HJ^2)^{1/3}}\\
&=\frac{229^{2/3}-162^{2/3}}{(EK^2Z^3)^{1/3}}
<\frac8{(EK^2Z^3)^{1/3}}.
\end{aligned}
\tag{7}
\]

The last bound uses only the exact integer comparisons

\[
8\cdot229^2<75^3,\qquad8\cdot162^2>59^3,
\]

which imply \(229^{2/3}<75/2\), \(162^{2/3}>59/2\), and their
difference is less than 8.

Since E>=H>=14, the length is strictly less than 4:
\(8^3=512<4^3\cdot14=896\). An interval of length less than 4 contains
at most four integers. Thus **at most four m values per Z** require a
perfect-square test. If

\[
\boxed{EK^2Z^3\ge512,}
\tag{8}
\]

the length is less than 1, so there is at most one m. In particular E>=512
is sufficient, independently of all other data.

If the stronger condition

\[
EK^2Z^3\ge229^2=52441
\tag{9}
\]

holds, then (3) gives v^6 < 229^2 H^2/J^2 <= H^3. Therefore v^2<H and
m=0. Only the integer R itself can be the required square.

### Most nontrivial zero supports already have one test

Because E=ZH and H>=14, the denominator scale in (7) is
\(EK^2Z^3=HK^2Z^4\ge14K^2Z^4\). Hence:

- If Z>=3, the scale is at least \(14\cdot3^4=1134>512\): at most one m.
- If Z=2, the scale is at least 224>64, so (7) is less than 2: at most two m.
- If Z=2 and K>=2, the scale is at least 896: at most one m.
- Only Z=1 can require the general four-test bound.

If t unitary supports remain after H>=14 and J<229H are imposed, the total
number of integer squared values to inspect is therefore at most t+4.
There are at most 2^omega(E)-1 eligible supports, since Z=E gives H=1.

## 4. Exact algorithm, with no real-number approximation

Let icbrt denote the greatest integer whose cube does not exceed its input.
The strict bounds in (3) for W=v^2 are exactly

\[
\begin{aligned}
W_{\min}&=\operatorname{icbrt}\!\left(
 \left\lfloor\frac{(162H)^2}{J^2}\right\rfloor\right)+1,\\
W_{\max}&=\operatorname{icbrt}\!\left(
 \left\lfloor\frac{(229H)^2-1}{J^2}\right\rfloor\right).
\end{aligned}
\]

Thus set

\[
m_{\min}=\max\!\left(0,\left\lceil\frac{W_{\min}-R}{H}\right\rceil\right),
\qquad
m_{\max}=\left\lfloor\frac{W_{\max}-R}{H}\right\rfloor.
\]

For each of these at most four integers, compute the integer square root of
R+mH and accept it only if squaring reproduces that value exactly. Then
u=Zv and r=Fu. Empty intervals or nonsquares exclude the support immediately.

The companion checker implements this algorithm and compares it with a
separate direct check of the reduced u interval on synthetic data and on
labelled binomial examples. The source includes cases with nontrivial Z,
with v sharing a prime with Z, and thresholds 14, 512, and 52441.
These implementation checks do not replace the uniform proof above.

## 5. Verification and limits

The mixed-structure and local-square reviewers independently audited (1)-(9),
the unique CRT residue, all interval constants, m>=0, the additional
zero-support bounds, and the complete implementation, and reported PASS.
Both reproduced the checker with separate or captured output, without
changing the saved artifacts. It passed 2,760 synthetic cases, 4,320 support
branches, and 25 labelled original-binomial examples. There were 1,492 integer
square tests and 95 positive synthetic reduced candidates; the bound of four
was attained. None of those synthetic candidates is asserted to solve the
original equation. These are independent AI audits, not external peer review.
The full CRT theorem is a written proof; no complete Lean formalization of
it is claimed in this note. The elementary integer-interval span, uniqueness,
and rational constants were separately executed in v11_formal.

The delivered code is [v11_simultaneous_square_interval_checks.py](v11_simultaneous_square_interval_checks.py),
with exact output in [v11_simultaneous_square_interval_verification.json](v11_simultaneous_square_interval_verification.json).
The original four-variable equation and all possible unbounded effective
defects have not been solved.
