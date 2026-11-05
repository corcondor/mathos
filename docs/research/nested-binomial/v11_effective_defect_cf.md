# Excluding effective defect 13 by a positive-divisor continued-fraction sieve

## Scope and theorem

The equation is still
\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]
We restrict to ell=1, j=i-3. Set n=i, A=binom(n,3),
X=binom(n^2,6n-9), r=min(k,A-k). Let E and B=A/E be the
parity-sensitive recovered defect and divisor defined in v10.
The actual remaining defect is
\[
H=\frac{A}{\gcd(A,r^3)}=\frac{E}{\gcd(E,u)},\qquad r=Fu.
\]
Both choices k=r and k=A-r are covered by the prior reduction.

The new complete result is
\[
\boxed{H\ge14.}
\tag{1}
\]
Therefore E>=14 and the square-filtered defect E_sq>=14 as well.
This is a uniform exclusion of one effective-defect value, for every
n in its proved height bound and for any number of prime factors of n-2.
It is not a solution of the unrestricted original equation.

## 1. Why only primitive curves are needed

Write C=gcd(A,r^3). The v10 transfer gives
\[
H\mid n-2,\quad n\ge104,\quad n<2^{192H},\quad
3n<r<10n/3.
\tag{2}
\]
The quotient T=r^3/C is an integer. Since C is the full gcd,
\[
\boxed{\gcd(T,H)=1,\qquad 162H<T<229H.}
\tag{3}
\]
The curve equation is
\[
6Hr^3=Tn(n-1)(n-2)=T(x^3-x),\qquad x=n-1.
\tag{4}
\]
The earlier complete v9 calculation excludes H<=12, even without
the coprimality condition in (3). Thus only H=13 is new here.
Its entire list is
\[
2106<T<2977,\qquad13\nmid T.
\]
There are exactly 804 curves: 870 integers in the interval, minus
66 multiples of 13. The height is n<2^2496. No n-interval is scanned.

## 2. A new bounded-divisor restriction

Reduce r/x=p/q with gcd(p,q)=1 and write r=gp,x=gq. Equation (4)
becomes
\[
g^2 D=Tq,\qquad D=Tq^3-6Hp^3>0.
\tag{5}
\]
Besides requiring D|Tq and a square quotient, there is the stronger
finite-divisor condition
\[
\boxed{D\mid6HT.}
\tag{6}
\]
To prove it, put d=gcd(D,q). Since gcd(p,q)=1,
\[
d=\gcd(6Hp^3,q)=\gcd(6H,q)\mid6H.
\]
Dividing D|Tq by d gives D/d | T(q/d). The integers D/d and q/d
are coprime, so D/d divides T. Thus D divides dT and hence 6HT.

This lemma is valid for arbitrary positive H and T. Its more general
natural-number form, with a in place of 6H, was executed in Lean as
`cubic_difference_dvd_product` in
[v11_formal/ArithmeticCore.lean](v11_formal/ArithmeticCore.lean).

For each curve we record every positive divisor of 6HT. Choose M=6HT+1.
Every valid D is in [1,M-1], so its residue modulo M must be one of
those divisors. This gives an exact rejection sieve before computing
the large cubes of p and q. If the residue passes, we still compute
the exact D, require that it equals that small divisor, and check (5).
A modular match alone is never accepted as an integer solution.

## 3. Completeness of the rational approximations

The established v9 proof gives, for
\(\alpha=(T/(6H))^{1/3}\),
\[
0<\alpha-p/q<\frac{3}{2q^2},\qquad q<2^{192H}.
\]
Every such reduced p/q occurs in the complete coefficient lists of
Section3 of [the v9 CF proof](v9_gcd_defect_continued_fractions.md):
at each adjacent-convergent step, at most 65 coefficient pairs are
needed. The lemma includes the intermediate fractions; it does not
assume they are all convergents.

For H=13, alpha cannot be rational. A reduced rational cube-root
denominator would have its cube dividing 78, so that denominator
is 1. But 3<alpha<7/2 has no integer value.

The generator encloses each cube root in an exact dyadic interval.
The verifier reconstructs its full saved CF prefix and independently
authenticates the cylinder endpoints by exact rational cube comparisons.
It checks that the last denominator is the first to reach 2^2496.
It enumerates both denominator halves of the complete approximation
lemma, applies (6), recovers g from (5), and imposes every condition
in (2). All decisions are integer decisions.

## 4. Executed complete calculation

The complete certificate contains every partial quotient and every
divisor list, using documented lossless zlib/base64 encoding.

| Check | Result |
|---|---:|
| Primitive curves | 804 |
| Certified CF partial quotients | 1,173,389 |
| Proposed fractions subjected to the residue sieve | 8,866,186 |
| Residue matches before the coprimality check | 2,045 |
| Exact cubic calculations on reduced fractions | 1,405 |
| Points satisfying all necessary conditions | **0** |

The first count of fractions includes unreduced candidates; those are
discarded before the exact recovery. It must not be described as a
count of reduced fractions.

Four integer points were recovered before the lower n cutoff:

| T | n | r |
|---:|---:|---:|
|2352|28|84|
|2560|26|80|
|2646|14|42|
|2890|52|170|

All have n<104, so none can belong to the remaining original branch.
Together with the complete H<=12 result, this proves (1).

The certificate is [v11_effective_defect_13_certificate.json](v11_effective_defect_13_certificate.json).
Its SHA-256 is `f3b4334f1ed6865fd04cf4b1abe1b310a17f161cde3d1d77ce59577c945a2ec1`.
The verification source and output are
[v11_effective_defect_cf_checks.py](v11_effective_defect_cf_checks.py) and
[v11_effective_defect_cf_verification.json](v11_effective_defect_cf_verification.json).

## 5. Independent reproduction by transforming the cubic itself

The second implementation reads no saved prefix or certificate and imports
none of the primary verifier. It uses no integer cube-root algorithm.
Instead it follows the unique real root of an integral cubic directly.

Start with F(x)=78x^3-T. Once a=floor(alpha) has been determined by
exact polynomial signs, the next complete quotient is the unique real root
of
\[
F_{\rm next}(y)=y^3F(a+1/y).
\]
For F(x)=Ax^3+Bx^2+Cx+D, the new coefficient tuple is
\[
\bigl(F(a),\ 3Aa^2+2Ba+C,\ 3Aa+B,\ A\bigr).
\]
We multiply all coefficients by -1 if necessary to keep the leading
coefficient positive. The real fractional-linear substitution preserves
the single real root; its nonreal roots remain nonreal. The leading and
constant coefficients never vanish, because alpha and all its complete
quotients are irrational. Hence integer sign comparisons, doubling, and
bisection determine each partial quotient exactly.

This reproduction enumerates the union of the coefficient lists instead
of partitioning the two denominator halves. It tests gcd(a,b)=1 in the
unimodular convergent basis, which is equivalent to gcd(p,q)=1. Its modular
sieve uses the different modulus 12HT+1. These choices cover a somewhat
larger approximation set and protect against a shared implementation
error in the interval partition or the certificate generator.

The execution reproduced all **804 curves and 1,173,389 CF terms**.
It checked **7,346,437 reduced fractions**, required **909 exact cubic
calculations**, and found **zero surviving points**. The four small raw
points were identical to those in the table above.

Source: [v11_effective_defect_cf_reproduction.py](v11_effective_defect_cf_reproduction.py).
Actual output: [v11_effective_defect_cf_reproduction_verification.json](v11_effective_defect_cf_reproduction_verification.json).

## 6. Audit and formalization boundary

The fixed-cofactor reviewer independently audited the divisor lemma,
the complete primary code, and the algebraic reproduction. The audit
confirmed exact prefix authentication, every strict endpoint, the safe
divisor-residue rejection, the cubic transformation, and both complete
coefficient enumerations, and reported PASS. This is an independent AI
audit, not external peer review.

The bounded-divisor lemma is Lean-checked. The full CF completeness
argument, these 804 curves, and the height transfer are not claimed to
be Lean-formalized. Their status is a written proof with complete exact
certificates and independent reproduction. The original four-variable
equation remains unresolved.

Reproduce with:

```sh
python3 v11_effective_defect_cf_checks.py verify
python3 v11_effective_defect_cf_reproduction.py
```

Regenerate the full certificate with the `generate` argument to the first
script. The main certificate and both verification outputs are retained.
