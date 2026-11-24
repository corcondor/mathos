# 根号と素数の方程式 v3 (2026-11-25)
Research only; not a complete solution. Local independent C++/GMP verifier completed all 1224 strong Miller–Rabin witnesses for prime indices 3..10000; exact Pocklington certificates checked for all eight surviving coefficients. Old 750 exclusions independently replayed. Four further proper divisors (189257 Y 728701147781; 189913 X 613336567759; 190669 X 699320504681; 191533 Y 923245370701) validated by independent matrix recurrence. 754/1009 excluded; 255 unresolved, the additional progression run covered only 65 of 259 rows. The compact DAG and four factors can be replayed with external_adapters.py. Prior v2 archive contains the full earlier CSVs; they are not included in this commit.

## New structural reduction: automatic prime-pair divisors
For an odd prime s>3 with s=3 mod 4:
* If l=2s+1 is prime, then l divides X_s. Indeed l=7 mod 8, so sqrt(2) exists in F_l and the ratio u=(1+sqrt(2))/(1-sqrt(2))=-(1+sqrt(2))^2 is a nonsquare, with u^s=-1. Thus X_s=0 mod l.
* If l=2s-1 is prime, then l divides Y_s. Indeed l=5 mod 8, sqrt(2) lies in F_(l^2), alpha^l=beta, alpha^(l+1)=-1, and u^s=(-1)^s alpha^(2s)=1. Thus Y_s=0 mod l.
Both divisors are proper since X_s,Y_s exceed 2s+1 for s>=5 (elementary recurrence). Thus a simultaneous prime pair with s=3 mod 4 and s>3 requires both 2s±1 composite. Exact sieve 5<=s<=1000000: 78496 prime indices, 39321 with residue 3 mod 4; 3911 exclusions via X, 3933 via Y, disjoint (for s>3 one of 2s±1 is divisible by 3). These 7844 exclusions are a structural family, not 7844 new exclusions in the previous 1009-row dataset. This is an explicit specialization of the previous order condition, not a claim of academic novelty.

## Actual external source integrations (CI, status must be checked)
- https://github.com/leanprover/hex-primality/tree/e89daa43f1c6f2038a59674598e2a5097e64c3df : literal Pocklington certificate adapter uses prime_of_checkPrimeAt; factor exponents are zero based and children sorted ascending.
- https://github.com/Vilin97/PrimeFactorLean/tree/d26f6a704ba83c311601b47ec183f465a309c6f7 : Certificate.check_sound and actual executable factor command; separate mathlib 4.24 environment. The algebra and descent lemmas are checked here, not a formalization of the complete radical equation.
- https://github.com/thery/coqprime/tree/ab9aea8e0a0a01a38549b96a6c211b1a8e93b239 : SPock_certif with common witness and vm_compute, Ubuntu packaged CoqPrime version (not upstream master build).
- https://github.com/SamuelMoulin/pell_norm_forms/tree/85c14649af9d221f859fec3038a5b7e743d83e45/scripts/Paper_01/generateur_certificats.gp : adapted matrix recurrence + PARI primecert/primecertisvalid. The upstream target P_k^2-2 is different; we do not claim its conjectures imply ours.
- https://github.com/s1rj1n/primepath/tree/b3148e5a2981f907135429f18ce7a1cfca9d3ba5 : CPU progression filtering methodology; upstream app is macOS/Metal and not a solver for these Pell pairs; not executed.
- https://github.com/flintlib/flint and https://pari.math.u-bordeaux.fr/ : actual external library checks in separate CI job.
- https://github.com/sympy/sympy and https://gmplib.org/ : previous local generator and verifier, independently replayed.
- https://doi.org/10.1515/crll.2001.080 : BHV primitive divisor theorem; a primitive divisor can be the entire prime term. Does not prove finiteness.
- https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Pell.html : positive Pell generator theorem, negative Pell descent bridge. 
- https://oeis.org/A331399 : simultaneous prime index reference; known four values, no completeness claim.

CI is an attempted execution, not proof of success. The full global finiteness of simultaneous primes, the cyclotomic norm formalization, complete radical reduction in Lean, and independent all-range classification remain open. No changes to master.
