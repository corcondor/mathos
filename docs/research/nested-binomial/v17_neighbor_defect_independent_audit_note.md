# Independent audit of the v17 neighbor-defect reduction

Date: 2026-11-06 JST. Internal independent review and exact reproduction;
not external peer review or new Lean verification.

## Written deductions reviewed

The original squared-index equation and the `ell=1, j=i-3` scope are
retained. Both k branches were checked separately.

1. From the congruence c_i = w*r*(r-2*epsilon) modulo Q_i, the divisor
   Q_i/delta_i = gcd(Q_i,r^2) divides c_i for epsilon=0, and divides
   c_i^2 for epsilon=1. The latter proof squares the congruence; it
   does not cancel r-2, w, 2 or 3. Coprimality of Q_0,Q_1 permits
   multiplication of the two divisibilities. Since delta^3|Q, the
   resulting delta^2 and delta divisibilities also follow exactly.
2. The constants 52,983,53,32 in the adaptive height and prime bounds
   have positive exact rational margins. The separate p<=6n-9 case
   satisfies n<6w and is covered. These bounds keep delta explicit;
   no unconditional new exponent for unbounded delta is claimed.
3. The identity
   Jp=6n(t-epsilon-1)+(t-epsilon)^2-10 has a positive right side for
   n>=104,t>=4 and both epsilon values. This proves J>=1 before the
   enumeration's lower limit z>9w is used.
4. Direct expansion verifies the two positive comparison identities.
   In the small branch, the v16 lower gap gives
   w<(224/9)J*n^(2/5). The inherited v15 inequality
   n-1<240*w^(3/2), together with n-1>(99/100)n, gives the lower bound
   w>(33/8000)^(2/3)*n^(2/3). The resulting exponent is 4/15, so
   n^4<2^150*J^15 and w^2<2^40*J^5 are correct. The corresponding
   complementary-branch inequality does not imply this height bound,
   and the note does not assert that it does.
5. For every w<=64, the proved z interval is finite. The normalized
   integer n/gcd(n,3) must divide c_0^3, or the smaller divisor with
   exponents floor(3*v_p(c_0)/2) in the small branch. This proves
   completeness of the divisor enumeration before any computation.
6. The finite calculation omits primality of the reconstructed p;
   excluding this larger necessary set is valid. In the small-p
   case the bound n<384 is derived, and all surviving pairs have
   delta<=12, contrary to the inherited v16 result.

No error requiring a change to the mathematical statements was found.

## Independent complete reproduction

The auditor does not import or execute `v17_neighbor_defect_checks.py`.
It finds divisors by the complete pairs d,N/d with d<=floor(sqrt(N)),
N=c_0^3; the producer uses prime-exponent products. The small-branch
condition is checked by d^2|N. It reverses the family enumeration
order, checks the second divisor by a gcd condition, and reconstructs
all square roots by integer binary search.

For 104<=n<=383, the auditor checks every integer r in the proved
interval, rather than generating only multiples of a forced divisor.
It checks source/note/certificate hashes and verifies all recorded
factorizations using exact trial division.

| Stage | Independently reproduced count |
|---|---:|
| Coefficient families | 8,712 |
| Divisor points | 590,028 |
| n>=104 with correct gcd(n,3) | 350,188 |
| Second divisor condition | 1,260 |
| Integral reconstructed p | 20 |
| p>6n-9 | 11 |
| Square reconstruction | 0 |
| Integers r checked in the bounded small-p case | 22,540 |

All family records, 1,260 second-divisor candidates, 20 integral-p
candidates and 11 consecutive-square witnesses match the certificate.
The largest generated n is 1,816,487,208; this is a divisor candidate,
not a scan cutoff or an original solution.

The four small-p pairs (n,r,delta) are exactly

```
(169, 546, 1)
(243, 792, 1)
(250, 830, 5)
(361, 1140, 1)
```

The full exact reproduction returned **PASS**. The auditor JSON
records its own source hash and the precise input certificate and
producer hashes.

## Reproduction

With all published files in the same directory:

```sh
python3 v17_neighbor_defect_independent_audit.py
```

When inputs are in a separate directory, pass `--input-dir PATH`.
The independent reproduction still depends on the inherited branch
theorems and the written completeness reductions reviewed above. It
does not formalize those deductions in Lean or solve the unbounded
four-variable equation.
