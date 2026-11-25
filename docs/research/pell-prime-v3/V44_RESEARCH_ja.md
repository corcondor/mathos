# v4.4 — exact multiplicative order and reverse sieve

## Kernel verification (2026-11-26 JST)
Pinned Lean and mathlib v4.24.0, mathlib commit f897ebcf72cd16f89ab4577d0c826cd14afaafc7.
- v4.3 initial run failed only at quadratic_degree_bound (typeclass heartbeat limit). Corrected in c7a6851. The 11-theorem allowlist passed: https://github.com/corcondor/mathos/actions/runs/45700962034/job/139510622994
- v4.4 initial run failed at two integer cast rewrites. Explicit source type corrected in ce42f94. The 8-theorem allowlist passed: https://github.com/corcondor/mathos/actions/runs/45701038460/job/139510871144
- Every audited theorem depends only on propext, Classical.choice, Quot.sound. No sorryAx or native compiler trust.
- HP_spec establishes monicity and exact natural degree; HP_minpoly_cyclotomic establishes equality to minpoly of the trace of a primitive odd prime root in its cyclotomic field. radical_iff_trace composes the existing reduction with the trace recurrence.
- V44Order proves the exact field order criteria for w and -w given trace 6, and uniqueness/cross-sign obstruction. The concrete finite residue algebra corollaries below are written mathematical proofs, not all stated in Lean as standalone theorems.

## Order theorem and exact completeness of the inverse sieve
Let alpha=1+sqrt(2), u=alpha^2=3+2sqrt(2), and for odd s define alpha^s=X_s+Y_s sqrt(2). Work in R_l=F_l[T]/(T^2-2) for an odd prime l. Norm -1 gives
u^s=(2X_s^2+1)+2X_sY_s T=(4Y_s^2-1)+2X_sY_s T.
Thus X_s=0 iff u^s=1, and Y_s=0 iff u^s=-1 (use that coefficients lie in the field F_l). u is a unit, with inverse 3-2T, and u is neither 1 nor -1 because its T coefficient is 2.
For prime s this is exactly ord(u)=s and ord(u)=2s, respectively. In the latter direction ord(u)=2s gives u^s=-1: alternatively use the two field components in the split case, where u maps to inverse units with equal order, or the field in the inert case; both components then give -1. Hence one odd prime l can divide X_s Y_s at at most one odd prime index s. The coefficients are odd; gcd(X_s,Y_s)=1 by the Pell norm. Consequently gcd(X_s Y_s,X_t Y_t)=1 for distinct odd primes s,t.
Writing chi=(2/l), Frobenius gives u^l=u^chi, so ord(u) divides l-chi. Inverse scan: enumerate l, factor (l-chi)/2, test only odd prime factors s. No bound on multiplier k is imposed independently of l. l=3 mod 8 can be skipped, since X_s divisibility implies 2 is square and Y_s divisibility implies -1 is square. The conservative strict lower check l<Y_s does not omit any proper odd prime divisor of X_s: X_s<2Y_s and any proper prime divisor of odd X_s is at most X_s/3. All arithmetic fits in unsigned 64-bit for l<=1e8.

## Reproduction
g++ -O3 -std=c++17 reverse_sieve.cpp -o reverse_sieve
./reverse_sieve 1000000 100000000 > reverse_hits.csv
python3 verify_reverse.py reverse_hits.csv 100000000 1000000

Actual local run:
auxiliary_primes=5761454 modular_tests=6233450 proper_divisors=47586 excluded_indices=35907
Independent matrix-power verifier:
PASS: 47586 distinct verified proper divisors, 35907 excluded indices; sides={'X': 23900, 'Y': 23686}; k>32 indices=12261
All 33555 previous witnesses retained; new witnesses=14031, new indices=7636, survivors=42589.
CSV SHA256: 0e8c7a03b14578dc486119afc1b719a6dea405c1cf93b0569e6c930a62b9daaa.
This covers s in [5,10^6], auxiliary l<=10^8. It is not an all-index primality audit. No new prime pairs claimed.

## Global finiteness: precise remaining problem
Let P_j=U_j(2,-1) be the Pell sequence. Then P_s=Y_s, and P_{2s}=2 X_s Y_s. Thus for odd prime s, both coefficients are prime iff the number of prime factors counted with multiplicity of P_{2s}/2 is 2 (both factors exceed 1). Every prime factor of either odd-index coefficient has rank s or 2s for u, respectively. Primitive-divisor existence for s and 2s cannot imply three prime factors of P_{2s}/2, since the two whole coefficients can themselves be the primitive divisors. The missing result is a uniform proper-divisor or third-prime-factor theorem.
The norms of cyclotomic evaluations in Q(sqrt(2)) satisfy Phi_s(u)=u^((s-1)/2) X_s, Phi_{2s}(u)=u^((s-1)/2) Y_s, so their field norms equal X_s^2 and Y_s^2. This follows from the trace identity and Phi_{2s}(T)=Phi_s(-T). Norms being squares is not a compositeness certificate for X_s,Y_s.
A heuristic, not a proof: both values grow exponentially in s and have no odd prime factor less than 2s-1, so a random-integer model with local sieving would give marginal prime probabilities on the scale log(s)/s. Assuming sufficiently weak joint correlation gives a summable series of joint probabilities. The assumption is unproved; neither Mertens' theorem nor the primitive divisor theorem provides a deterministic uniform upper bound. Chebotarev for fixed Kummer extensions concerns varying l and cannot force an extra prime of exact rank s for every s.

## Additional sources and how they apply
- Fiebig, Mbirika, Spilker, Period Patterns, Entry Points, and Orders in the Lucas Sequences (Fibonacci Quarterly 63 (2025), 345–376), https://doi.org/10.1080/00150517.2024.2442591 and https://arxiv.org/abs/2408.14632 . Framework for entry points and periods of both Lucas sequences; motivates exact rank inversion. Their period/entry-point ratio is not the multiplicative order used here.
- Einsiedler, Everest, Ward, Primes in Sequences Associated to Polynomials (After Lehmer), LMS J Comput Math 3 (2000), 125–139, https://doi.org/10.1112/S1461157000000255 . Exponential norm-sequence growth, congruence restrictions and prime-distribution heuristics; not a proof of finiteness of joint primality.
- Cosgrave and Dilcher, Pairs of Reciprocal Quadratic Congruences Involving Primes, Fibonacci Quarterly 51 (2013), 98–111, https://doi.org/10.1080/00150517.2013.12427950 . Related Pell/Lucas reductions of pairs of prime congruences, not a theorem covering the exact asymmetric congruences here.
- Bilu, Komatsu, Luca, Pizarro-Madariaga, Stanica, On a divisibility relation for Lucas sequences, J Number Theory 163 (2016), 1–18, https://doi.org/10.1016/j.jnt.2015.11.011 . General Lucas divisibility comparisons.
- Bilu, Hanrot, Voutier, Existence of primitive divisors of Lucas and Lehmer numbers, https://doi.org/10.1515/crll.2001.080 . Existence of primitive divisors, not proper divisors.
- DeepMind formal-conjectures Pell-number primes problem: https://google-deepmind.github.io/formal-conjectures/src/FormalConjectures/Wikipedia/Pell/ . Infinitude of Pell primes remains marked research open. This is a different assertion from joint-prime finiteness.
- OEIS A096650 and A099088 give lists of Pell and half-companion Pell prime/probable-prime indices; their intersection among odd displayed entries is 3,5,29,59. These lists are not an unbounded proof of completeness.

Master is unchanged. No assertion of global finiteness.
