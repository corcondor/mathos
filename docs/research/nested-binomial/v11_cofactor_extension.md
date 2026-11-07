# A binary refinement and complete exclusion of ninety-four cofactors

## Theorem and scope

The equation under consideration is the squared-index equation

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

**Theorem.** There is no solution in any of the families

\[
\boxed{\ell=1,\qquad j=i-3,\qquad i=wp^a+2,
\qquad p\text{ prime},\quad a\ge1,\qquad
\frac{w}{\gcd(w,192)}\le13.}
\tag{1}
\]

The prescribed cofactor w need not be coprime to p. Both choices
\(k=r\) and \(k=A-r\) are included. There are exactly ninety-four
cofactors in (1):

\[
\boxed{\begin{gathered}
1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,20,21,22,24,\\
26,27,28,30,32,33,36,39,40,42,44,48,52,54,56,60,64,66,72,\\
78,80,84,88,96,104,108,112,120,128,132,144,156,160,168,176,\\
192,208,216,224,240,256,264,288,312,320,336,352,384,416,432,448,\\
480,512,528,576,624,640,672,704,768,832,864,960,1056,1152,1248,\\
1344,1536,1728,1920,2112,2304,2496.
\end{gathered}}
\tag{2}
\]

This contains the thirty cofactor families of v10 and adds
sixty-four prescribed cofactors. Different parametrizations can
represent the same index; the families are not asserted to be
disjoint.

The proof has two new inputs. First, a binary carry argument
improves the universal recovered-defect constraint from a denominator
6 to a denominator 192. Second, `v11_effective_defect_cf.md` excludes
the effective defect H=13, extending the complete v9 result H<=12.
Together these facts force an explicit finite set of prime bases
and exponents. All 28,316 parameter records in this finite set are
excluded by exact certificates, representing 28,133 distinct indices.
No empirical upper cutoff for i is introduced.

The theorem concerns the displayed branch. The unrestricted original
equation remains unsolved.

## 1. Local recovery and the actual effective defect

Put

\[
n=i,\quad A=\binom n3,\quad
X=\binom{n^2}{6n-9},\quad
r=\min(k,A-k),\quad G=\gcd(A,X),\quad S=A/G.
\]

The established endpoint and small-index reductions leave n>=104.
The gap theorems in `v5_offset_three_structure.md` and
`v6_offset_composite.md` give

\[
3n<r<10n/3,
\tag{3}
\]

and, when n>=1024,

\[
r<3n+\frac{3n}{4\log n}.
\tag{4}
\]

The original equation and the choose identity imply

\[
A\mid r(X+r^2).
\tag{5}
\]

This formulation applies directly to both outer branches: replacing
k by A-k changes k(X+k^2) to its negative modulo A. The complete
local proof is in `v10_valuation_recovery.md`.

For each prime p dividing A write
\(\alpha=v_p(A)\), \(x=v_p(X)\), and \(e=v_p(r)\).
If 3e<alpha, the two terms rX and r^3 in (5) must have equal
valuations; otherwise their sum has valuation below alpha. Hence

\[
3e<\alpha\quad\Longrightarrow\quad x=2e.
\tag{6}
\]

Define

\[
d_p=\begin{cases}
\alpha-3x/2,&x\text{ even and }3x<2\alpha,\\
0,&\text{otherwise},
\end{cases}
\qquad
E=\prod_{p\mid A}p^{d_p},\qquad B=A/E,
\]

\[
F=\prod_{p\mid A}p^{\lceil v_p(B)/3\rceil}.
\tag{7}
\]

The alternatives in (6) give

\[
G\mid B\mid A,\qquad B\mid r^3,\qquad F\mid r,
\qquad E\mid S.
\tag{8}
\]

In particular the v9 divisor theorem gives

\[
E\mid\frac{n-2}{\gcd(n-2,6)}.
\tag{9}
\]

It is important to distinguish E, which is computed solely from n,
from the effective defect of a particular r:

\[
H=\frac{A}{\gcd(A,r^3)}.
\tag{10}
\]

Because B divides both A and r^3, H divides E. If r=Fu, the
stronger local dichotomy from v10 gives

\[
H=\frac{E}{\gcd(E,u)},\qquad u^3<229E.
\tag{11}
\]

For C=gcd(A,r^3), the associated integer T=r^3/C is coprime to H.
The v9 complete continued-fraction proof excludes H=1,...,12;
`v11_effective_defect_cf.md` excludes H=13 using this actual H and
the additional condition gcd(T,H)=1. Therefore

\[
\boxed{H\ge14,\qquad E\ge14.}
\tag{12}
\]

We do not assume that the arbitrary recovered defect E itself is
coprime to the associated r^3/B. The implication E<=13 would give
H<=13 via H|E, which is the precise contradiction used below.

## 2. Three forced binary carries

**Lemma.** For every solution in this branch,

\[
\boxed{E\mid\frac{n-2}{\gcd(n-2,192)}.}
\tag{13}
\]

Write N=n-2 and h=v2(N). If h=0 or h=1, (9) already says
v2(E)=0, which is the required exponent in (13). Suppose h>=2,
and write n=2+2^h z with z odd. Then n is 2 modulo 4, and

\[
v_2(A)=v_2(n)+v_2(n-1)+v_2(n-2)-1=h.
\tag{14}
\]

Because 2h>=h+2, expansion of the three relevant integers gives

\[
\begin{aligned}
n^2&\equiv4,\\
6n-9&\equiv3+2^{h+1},\\
(n-3)^2&\equiv1+2^{h+1}
\end{aligned}
\qquad\pmod{2^{h+2}}.
\tag{15}
\]

In adding (6n-9)+(n-3)^2=n^2 in base 2, these residues force
carries from positions 0, 1, and h+1. The first two arise from
adding the low patterns 3 and 1; the carry stops at position 2.
At position h+1, both summands have a digit 1, causing another
carry. The three positions are distinct because h>=2, including
the boundary case h=2. Kummer's carry formula therefore yields
x=v2(X)>=3.

If x is odd, d2=0 by (7). If x is even, x>=4, so

\[
d_2\le\max(h-6,0).
\tag{16}
\]

Since 192=2^6*3, this is exactly the exponent of 2 in
N/gcd(N,192). For every odd prime, the exponents in the quotients
with denominators 6 and 192 are equal. Combining (9) and (16)
proves (13).

For reference, put

\[
c_{192}(w)=\frac{w}{\gcd(w,192)}.
\tag{17}
\]

The proof works independently of the cofactor parametrization;
(13) is a necessary condition for every remaining mixed-factor N.
This refinement uses three guaranteed low-bit carries and the
odd/even valuation dichotomy, not numerical observations about a
bounded range of n.

## 3. From an infinite family to an exact finite domain

First normalize any prescribed parametrization. If p^h exactly
divides w, put w0=w/p^h and replace a by a+h. Multiplication by
a prime cannot decrease c192:

\[
\frac{c_{192}(pv)}{c_{192}(v)}
=\frac{p\gcd(v,192)}{\gcd(pv,192)}\ge1.
\tag{18}
\]

Indeed, gcd(pv,192) divides p*gcd(v,192). Thus c192(w0)<=c192(w),
and w0 is again in (2). It suffices to treat p not dividing w.

Put q=p^a and define the coefficient used in the v9 exact formulas:

\[
D_w=\frac{\binom{6w}{2w}}
{\gcd\left(\binom{6w}{2w},6\right)},
\qquad b=v_p(D_w).
\tag{19}
\]

If q<=4w, there are already only finitely many possibilities, with
p<=4w and n<=4w^2+2. Now suppose q>4w. The exact fixed-cofactor
formulas from `v9_gcd_structure.md` and
`v9_gcd_defect_continued_fractions.md` give

\[
\alpha=v_p(A)=a-\mathbf1_{p=3},\qquad v_p(S)=b.
\tag{20}
\]

If b=0, the p-component of E is also absent, since E|S. If b>0,
the second equality in (20) gives

\[
x=v_p(X)=\alpha-b.
\tag{21}
\]

For either case, (13) says that the part of E coprime to p divides
c192(w). This holds also when p=2 or 3: removing the p-part from
N/gcd(N,192), with N=wp^a and p not dividing w, leaves precisely
w/gcd(w,192).

As c192(w)<=13, (12) therefore forces a positive p-component of E.
In particular b>0, x must be even, and 3x<2alpha. By (21), this
is equivalent to

\[
\boxed{\alpha=b,b+2,\ldots,3b-2,
\qquad a=\alpha+\mathbf1_{p=3}.}
\tag{22}
\]

Moreover p divides D_w, and so p<=6w. We have proved that every
hypothetical solution of (1) belongs to the following finite domain:

- w is one of the ninety-four numbers in (2);
- p<=6w is prime and p does not divide w;
- either p^a<=4w, or a satisfies the finite progression (22);
- n=wp^a+2>=104.

The generator uses the union of the two exponent sets. If a value
from (22) also has q<=4w, it is recorded only once and is labelled
as a small-power case. No exact large-q formula is assumed for
the small-power cases.

### A polynomial bound derived from the same argument

Each summand in the Legendre floor formula for C(6w,2w) is zero
or one. Hence p raised to its valuation in this coefficient is
at most 6w. After dividing by gcd(C(6w,2w),6), this gives

\[
p^b\le6w\ (p\ge5),\qquad
2^b\le3w\ (b>0),\qquad
3^b\le2w\ (b>0).
\]

Using the last exponent in (22),

\[
q\le\begin{cases}
216w^3/25,&p\ge5,\\
27w^3/4,&p=2,\\
8w^3/3,&p=3.
\end{cases}
\tag{23}
\]

The small-power case is smaller as well. Consequently the finite
remainder is contained in

\[
\boxed{p\le6w,\qquad q<9w^3,\qquad n<9w^4+2.}
\tag{24}
\]

The primary checker uses (22), which is sharper. Bound (24) also
permits an independent reproduction without knowing D_w or its
valuation progression. Neither route scans the full interval of n.

## 4. Complete certificates for the finite remainder

The exact domain above contains 28,316 parameter records and
28,133 distinct n. Its largest index is

\[
(w,p,a,n,b)=(2304,23,7,7844717829890,3).
\tag{25}
\]

For each distinct n the complete certificate records the full
prime factorization of A, every valuation v_p(X) for p|A, the
minimal forced exponent of p in r, E, F, and the first possible
multiple of F above the strict lower gap:

\[
r_0=\left(\left\lfloor\frac{3n}{F}\right\rfloor+1\right)F.
\tag{26}
\]

Each record is excluded in exactly one of the following ways:

| Exclusion | Parameter records | Distinct indices |
|---|---:|---:|
| E<=13, contradicting (12) | 11,749 | 11,568 |
| 3r0>=10n, contradicting F|r and (3) | 16,566 | 16,564 |
| The logarithmic gap at n=6860 | 1 | 1 |
| Total | **28,316** | **28,133** |

The second test uses only the first admissible multiple: if r0
already reaches the strict upper endpoint, every larger multiple
also fails. It does not enumerate r.

### The one logarithmic-gap record

The only remaining record after the first two tests is

\[
(w,p,a,n)=(54,127,1,6860),\qquad
F=1330,\quad E=1143,\quad r_0=21280.
\]

This is the same boundary record already present in v10. Its
complete factorization and relevant valuations are

\[
A=2^2\,3^2\,5\,7^3\,19^3\,127,
\qquad
\begin{array}{c|rrrrrr}
p&2&3&5&7&19&127\\ \hline
v_p(X)&13&0&5&6&6&0.
\end{array}
\]

Since e<11/4 and

\[
6860\cdot4^8-11^8=235218079>0,
\]

we have log(6860)>8. Equation (4) therefore gives

\[
r<3n+\frac{3n}{32}=\frac{99n}{32}<21280,
\]

where the last strict inequality is

\[
32\cdot21280-99\cdot6860=1820>0.
\]

This excludes the last possible record. Together with the separately
verified H<=13 theorem and the established gap and small-index
results, it proves (1). The H=13 primary certificate and the separate
algebraic continued-fraction reproduction have both passed; their
methods and verification scope are recorded in
`v11_effective_defect_cf.md`.

## 5. Consequences for arbitrary mixed factorizations

Let p^a be any exact prime-power factor of n-2 in a hypothetical
solution, and write w=(n-2)/p^a. The complete family theorem gives

\[
\boxed{\frac{w}{\gcd(w,192)}\ge14.}
\tag{27}
\]

In particular every exact prime-power factor satisfies

\[
\boxed{p^{v_p(n-2)}\le\frac{n-2}{14}.}
\tag{28}
\]

Retaining gcd(w,192) gives a stronger bound whenever w is divisible
by 2 or 3. There is no hypothesis that p exceeds 6w.

For example, if n-2 has exactly two distinct prime divisors, each
exact prime power is the complementary cofactor for the other.
Then an exact power of 2 must be at least 1024, an exact power of
3 at least 81, and each of the primes 5, 7, 11, 13 must occur
with exponent at least two if it occurs. These are necessary
conditions; they do not assert that the surviving forms give solutions.

### The logarithmic bound with the improved cofactor

The binary lemma also strengthens the all-cofactor height result,
without the restriction c192(w)<=13. For every hypothetical solution
n=wp^a+2,

\[
\boxed{\log n<128c_{192}(w),\qquad n<2^{192c_{192}(w)}.}
\tag{29}
\]

To prove this, first normalize as in (18). For q>4w, if the main
prime p is absent from E, then E|c192(w). The v10 height theorem
for the recovered divisor B gives log(n)<128E<=128c192(w).
If p is present in E, (20)-(22) hold without any assumption on
c192(w), so (23) yields n<16w^4. The case q<=4w also gives
n<=4w^2+2<16w^4. Put c=c192(w), so w<=192c and c>=1.
In these latter cases,

\[
\begin{aligned}
\log n&<4\log(2w)\le4\log(384c)\\
&<36+4\log c\le32+4c\le36c<128c.
\end{aligned}
\]

Here log(384)<9 follows from 384<512 and e>2, while
log(c)<=c-1 for c>=1. The base-2 version follows from
log(2)>2/3, exactly as in the earlier height theorem.
Finally normalization can only decrease c192, so (29) holds for
the originally prescribed cofactor as well.

For an arbitrary exact prime-power factor q of n-2, let
w=(n-2)/q and d=gcd(w,192). Combining (27) and (29) gives

\[
\frac wd\ge14,\qquad \frac wd>\frac{\log n}{128},
\qquad
q<\frac{128(n-2)}{d\log n}.
\tag{30}
\]

## 6. Reproduction and certificate format

Run, from the research directory,

```sh
python3 v11_cofactor_extension_checks.py generate
python3 v11_cofactor_extension_checks.py verify
```

The first command generates the entire finite domain and every
certificate, then verifies them. The second reads the saved
certificates and reconstructs the domain independently.

The approaches differ at the following points:

- The generator lists w<=2496 satisfying c192(w)<=13. The verifier
  instead reconstructs w=cg, with c=1,...,13 and g dividing 192,
  and checks gcd(cg,192)=g.
- The generator uses a prime sieve and the exact binomial C(6w,2w)
  to obtain D_w. The verifier uses deterministic trial primality
  and factorial valuation sums, then checks each complete factor
  product against its factorial-ratio value.
- The generator uses the progression (22). The verifier examines
  every exponent up to its proved maximum and directly checks
  x>=0, x even, and 3x<2alpha, also retaining all q<=4w.
- The generator computes v_p(X) by factorial-floor sums. The
  verifier counts carries in (6n-9)+(n-3)^2 in base p.
- The generator uses the closed formula (7). The verifier directly
  enumerates the local alternatives 3e>=alpha or 2e=x and takes
  the smallest permitted e. It then reconstructs B, E and F.

All 202,482 prime-factor records are verified by deterministic
primality tests and exact multiplication, and all 202,482 independent
carry valuations agree. The verifier also checks (13) for every
finite candidate. No original outer or squared-index binomial
coefficient is constructed.

`v11_cofactor_extension_certificates.json` is a complete lossless
JSON certificate encoded as zlib-compressed UTF-8 JSON and base64.
Its wrapper includes SHA-256 hashes and lengths of both the raw
and compressed payloads. The full decoded payload is 13,643,226
bytes; the compressed payload is 1,754,846 bytes. It includes every
cofactor coefficient, all 28,316 parameter records, and every one
of the 28,133 index certificates. Compression removes no mathematical
data. The checker validates the hashes before reading the payload.

The report in `v11_cofactor_extension_verification.json` records
all counts, hashes and exclusions. It explicitly identifies the
H=13 theorem as a dependency and does not claim to prove that
continued-fraction theorem by this finite-cofactor calculation.

### Reproduction over a larger, independently derived domain

The separate source `v11_cofactor_extension_independent_reproduction.py`
reads neither the primary certificate nor its checker. It does
not calculate D_w or use the exponent progression (22). Instead
it uses only the proved bounds p<=6w and p^a<9w^3, then computes
the binomial valuations using base-p digit sums, distinct from
both the factorial-floor generator and the carry-count verifier.

This larger domain contains 69,223 parameter records and 69,003
distinct indices. Its maximum is

\[
(w,p,a,n)=(2496,5189,3,348735045407426).
\]

All 532,883 digit-sum valuations were checked. The exclusions are:

| Exclusion | Parameter records | Distinct indices |
|---|---:|---:|
| E<=13 | 52,656 | 52,438 |
| No forced multiple in the broad gap | 16,566 | 16,564 |
| The same n=6860 logarithmic gap | 1 | 1 |
| Total | **69,223** | **69,003** |

The extra candidates vanish at the recovered-defect test, as
predicted by the critical-exponent theorem. The larger-domain
calculation therefore checks the finite conclusion without
depending on the primary generator's short exponent list.
Its report is `v11_cofactor_extension_independent_reproduction.json`.
Both implementations were prepared by the fixed-cofactor agent;
their independence is algorithmic, not a claim of different human
authors or external review. The separate mathematical and code
audit described below distinguishes review by another agent from
this algorithmic reproduction.

## 7. Verification boundaries

The finite exclusion is exact integer arithmetic. The completeness
of its domain uses the written normalization, binary lemma, exact
fixed-cofactor valuations, and local recovery theorem; its validity
does not depend on extrapolating from examples.

The shared v10 Lean source `v10_formal/ValuationRecovery.lean`
was actually kernel-checked and covers the outer-binomial cubic
divisibility, local valuation recovery and finite-exponent
parametrization under their stated assumptions. This note does
not claim that its complete ninety-four-family theorem, its
28,316-record certificate, or the whole original equation has
been formalized in Lean. New v11 formalization, if recorded
separately, has only the scope stated in its execution report.

Independent audit and reproduction records are to be read as
computational and mathematical checks by separate AI calculations,
not as external peer review. The remaining mixed-factor cases
outside (1) remain open in this work.

### Independent review of the final ninety-four-cofactor version

On 2026-11-05, the local-square reviewer independently audited the
entire final proof and both source implementations and reported
PASS without mathematical corrections. The review covered the
three-carry lemma, normalization, the p-free part of E, the exact
critical-exponent progression, the polynomial bound, the general
height refinement, and the two-prime consequence for a power of 2.

The reviewer checked the complete primary certificate's factor
products, E and F reconstruction, interval exclusions, the listed
ninety-four cofactors, the 202,482-row accounting and the report
hashes. Separately reconstructing the larger domain with trial
primality and the divisor list for 192 reproduced all 69,223
parameter records, 69,003 indices and the same maximum index.
This review did not repeat the entire large-domain valuation
calculation or every primality test; those executions are recorded
in the primary and independent reproduction reports.

The root reviewer also independently read the entire final proof,
the primary generator/verifier, and the broader-domain reproduction
and reported PASS on the same date. This review confirmed the
local exponents, the p-free cofactor argument including bases 2
and 3, normalization, the all-cofactor logarithmic bound, the
power-of-2 consequence, and the completeness and arithmetic logic
of both finite domains. It was a mathematical and source-code
review, not another full numerical run. Neither reviewer requested
a mathematical correction to the final version.
