# v3.1: N+1 certificate integration and exact trace-polynomial replay

Eight independent N+1 (Lucas/Morrison) certificates were generated locally, using the half-index factorization of N+1 and SymPy only to produce factor data; independent Python exact verifier established all 8 plus certificates and recursively certified child primes. The compact replay in external_followup.py does not require SymPy. It produces concrete PrimeFactorLean Step.check_sound proof terms for the +1 branch, not merely a probable-prime test.

For an odd prime divisor l of N, in F_l[sqrt(D)] the ratio alpha/conjugate(alpha) belongs to the multiplicative subgroup of order l-1 or l+1 (depending on whether D is split). The passed Lucas witnesses for q^e|N+1 force q^e to divide that order, for every q in the certified factor product F. Hence F|l-1 or F|l+1. If (F-1)^2>N, no prime factor <=sqrt(N) exists. See upstream PrimeFactorLean/Proofs/Pocklington.lean theorem plus_test and PrimeFactorLean/Proofs/PlusOne.lean.

Trace polynomial audit:
For h=(s-1)/2 and odd s, H_h(z)=1+sum_{k=1}^h C_k(z) with C_0=2, C_1=z, C_{k+1}=z C_k-C_{k-1}. The exact identities X_s=H_h(6), Y_s=(-1)^h H_h(-6) follow from the geometric sum H_h(w+w^-1)=sum_{k=-h}^h w^k with w=(1+sqrt(2))^2 and w=-(1+sqrt(2))^2. For prime s, H_h is the minimal polynomial of zeta_s+zeta_s^-1. This establishes the norm representation over the maximal real cyclotomic field. The independent integer recurrence check passed all 5000 odd indices 3..10001; this is an evaluation audit, not a Lean proof of the cyclotomic identification.

First CI (45489068111): PARI 8/8 and FLINT 8/8 PASS; hex-primality 8/8 kernel proofs PASS, axioms exactly propext, Classical.choice, Quot.sound; CoqPrime failed because packaged example module PocklingtonRefl is not installed. The followup imports the actual Pock library and standard Coq modules; CI must be inspected for its status. No finiteness or complete solution claim.
