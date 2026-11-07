# Independent review: canonical small-branch J <= 16

Reviewer: residual-geometry agent. Date: 2026-11-07 JST.
Targets: `v19_canonical_J_elimination.md`, `v19_canonical_J_checks.py`,
`v19_canonical_J_verify.py`, and `v19_canonical_J_certificate.json`.
Result: **PASS** for the final written coverage proof and all 110
finite-field certificates. The completed companion note was read in full
and checked against the previously reviewed implementations and data.

## 1. Coverage of w and n

For an original small-branch solution, inherited v17/v18 results give
n>=104, t>=3sqrt(n), canonical w>=65, gcd(w,J)=1, and
Q0²|c0³, Q1²|c1³, with
Q0=n/g, g=gcd(n,3) in {1,3}, Q1=(n-1)/d, d=gcd(n-1,6),
c0=10w+2J and c1=25w+3J. The inherited w>=65 statement explicitly
applies to the largest common divisor, not just to a prime cofactor
(v18_neighbor_cofactor_height.md, Section7).

T0=6n(t-1)+t²-10 > 18n^(3/2). Since n>=104,
n²+2 < (5001/5000)n². Hence

    w/J = (n²+2)/T0 < (1667/30000)sqrt(n).

Together with n²<=9c0³ this yields precisely

    30000^4 w^4 < 9*1667^4 J^4 (10w+2J)^3.

For each fixed J>0, w^4/(10w+2J)^3 is strictly increasing on w>0:
its logarithmic derivative is (10w+8J)/(w(10w+2J))>0. It tends to
infinity. Thus binary boundary detection in the producer and sequential
detection in the checker both cover the complete possible w interval;
there is no arbitrary search cutoff. Equality is excluded correctly
because the height inequality is strict.

If c0=product(p^e), the full set of positive Q0 with Q0²|c0³ is
product(p^f), 0<=f<=floor(3e/2). The producer enumerates exactly these
integers and both g values, retaining gcd(n,3)=g. This neither misses nor
duplicates an actual n. The independent checker reconstructs the same
set as the union of 3-free divisors and three times all divisors.
The height filter nJ²/w² > 30000²/1667² is also exact and necessary.

## 2. Two-adic omissions and the second divisor condition

For canonical small-branch J, the written two-adic argument gives
v2(J) in {0,2}. Indeed n even makes J odd after cancelling the unique
factor2 of N; n odd and J even imply r odd. Then Q|r³ makes Q odd,
forcing n=3 mod4, and T0=4 mod8. Since N is odd, v2(J)=2.
The skipped classes J mod8 in {0,2,6} are exactly the forbidden classes.
All remaining J between1 and16 are included.

Every possible n from the second divisibility has the form n=dv+1,
where v²|c1³ and d in {1,2,3,6}, with gcd(dv,6)=d. This condition
correctly recovers the actual d=gcd(n-1,6), including the primes2,3.
There is no assumption that w can be cancelled modulo Q0 or Q1.

## 3. Why the Bezout certificates prove exclusion

For each nonempty (J,w) group let P(x) be the product of x-n over the
first reconstructed n values, and H(x) the product over all second
divisor values. A common integer n would give a common root modulo every
prime. The certificates give a prime p, the exact remainder Hbar of H
modulo P over Fp, and polynomials U,V with U P+V Hbar=1. A common root
would evaluate this identity to0=1. Repeated roots modulo p do not
invalidate the argument. Different groups may use different primes.

I read both implementations and re-executed the standard-library
verifier without importing the producer or SymPy. It independently
reconstructs the domains, checks all prime moduli, recomputes both
products/remainders, and checks all 110 Bezout identities by coefficient
arithmetic. Observed totals agree: 6,620 primitive w values, 237,434 raw
divisor records, 136,852 normalized n values, 159 height-compatible rows,
110 certificates, maximal prime107, and no second-divisor survivor.
The saved execution result is `v19_canonical_J_independent_execution.json`.

These checks establish the claimed exclusion of J<=16 under the stated
inherited conditions, hence J>=17 for original solutions in the small
branch. The QQ Groebner/saturation observations are not needed for this
finite theorem. The result gives neither an upper bound on J nor an
exclusion of the complementary branch. No new Lean verification is claimed.

Final-note check: Sections 1–6 state the same inherited conditions, strict
height bounds and full finite domains reviewed above. The two-adic split,
quartic monotonicity, the J<=6 analytic subargument and the J=7,w=101
illustration are correct. The positive-dimensional QQ elimination is
properly distinguished from the zero-dimensional finite-domain certificate.
The final note is included in the review JSON SHA256 bindings.
