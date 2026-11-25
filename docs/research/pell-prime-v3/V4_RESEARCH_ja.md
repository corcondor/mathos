# v4: formal radical reduction, descent and real-cyclotomic trace

No new assertion of finiteness. The real odd root convention is essential: a^s=p+q√r, b^s=p−q√r; even s uses nonnegative real roots. v4 starts with three separate Lean modules; successful CI must be checked before marking results formalized.

## Algebraic bridge

Let u=ab, t=a+b. The Newton power sums P_0=2, P_1=t, P_(n+2)=t P_(n+1)−U P_n satisfy P_n(u)=a^n+b^n, deg P_n≤floor(n/2). Also P_n(0)=t^n for n≥1. For odd prime s, u^s=p²−rq² is an integer, and P_s(u)=2p. The polynomial P_s−2p is nonzero: t^s=2p is impossible for prime t,p and s≥3, since t|2p implies t=2 or t=p, neither permits the equality (if t=2 then p=2^(s−1)). If x^s−c were irreducible over Q it would be the minimal polynomial of u of degree s, contradicting the smaller annihilator. Capelli's prime-exponent binomial theorem gives a rational q with q^s=c. Odd real powers are injective and Q is the fraction field of integrally closed Z, hence u=q∈Z. For s=2, u=(t²−2p)/2 is rational directly, then integrality follows from u²∈Z.

Remaining written reduction: s=2 implies t even (t²=2p+2u), t=2, p≤2 since a,b≥0; u=0 forces p²=rq², impossible for primes. For odd s, t divides 2p by the recurrence and odd index. If t=p≥3, then (a+b)^s/(2^(s−1))≤a^s+b^s=2p gives (p/2)^(s−1)≤2, impossible for p≥3,s≥3. The inequality follows by expanding at t/2; all even powers of (a−b)/2 have nonnegative coefficients. Thus t=2. D=1−u=(a−b)^2/4 is a positive integer. Write D=d k² squarefree, a=1+√D and b=1−√D (a>b). The binomial expansion yields p=A_s(D), q√r=B_s(D)√D with B_s(D)≥s. Comparing squarefree parts gives d=r and q=k B_s(D); prime q implies k=1. If r odd, A_s(r)≡2^(s−1)≡0 mod2 while A_s(r)>2. Thus r=2. These last implications are a written proof, not yet end-to-end Lean.

## Negative Pell classification

For x²−2y²=−1, x,y>0, if y≥3 the transform (3x−4y,3y−2x) preserves the norm and strictly decreases positive y. For y=1,2 the only solution is (1,1). Its inverse is multiplication by 3+2√2. Thus x+y√2=(1+√2)^(2k+1). v4 source attempts a complete well-founded Lean proof using v3 descent.

## Trace bridge

H_0=1, H_1=z+1, H_(n+2)=z H_(n+1)−H_n. For w nonzero in any field,
(w−1) w^n H_n(w+w^−1)=w^(2n+1)−1.
This universal identity makes any nontrivial (2n+1)-st root of unity yield a root of H_n. For prime s=2n+1, standard cyclotomic degree [Q(ζ):Q]=s−1 and quadratic equation for ζ over Q(ζ+ζ^−1) identify H_n with the real cyclotomic minimal polynomial (monicity and degree n still to be proved in Lean). The recurrences A_n=H_n(6), B_n=(−1)^n H_n(−6) coincide with X_(2n+1),Y_(2n+1), by identical second-order recurrences and initial terms 1,7 and 1,5. The new cross invariant A_(n+1)A_n−2B_(n+1)B_n=−3 closes an induction for the norm. This is not a proof of simultaneous-prime finiteness.

## Literature and exact use / limitations

1. A. Schinzel, "Solved and unsolved problems on polynomials", Banach Center Publ. 34 (1995), Capelli theorem stated explicitly: https://bibliotekanauki.pl/articles/1359644.pdf ; use prime-exponent irreducibility, implemented at mathlib v4.24.0 Mathlib/FieldTheory/KummerPolynomial.lean, https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/FieldTheory/KummerPolynomial.lean.
2. W. Watkins, J. Zeitlin, "The Minimal Polynomial of cos(2π/n)", Amer. Math. Monthly 100 (1993) 471–474, https://doi.org/10.1080/00029890.1993.11990434 ; real trace polynomials, compare FLINT fmpz_poly_cos_minpoly, https://flintlib.org/doc/fmpz_poly/_fmpz_poly_cos_minpoly.html.
3. J. H. Jaroma, "On the appearance of primes in linear recursive sequences", Adv. Differ. Equ. (2005), https://doi.org/10.1155/ADE.2005.145 ; rank of apparition, candidate congruences, does not prove simultaneous-prime finiteness.
4. P. Moree, "On the prime density of Lucas sequences", JTNB 8 (1996) 449–459, https://doi.org/10.5802/jtnb.181 ; density of prime divisors across all indices, distinct from density of prime-valued terms.
5. P. Moree and P. Stevenhagen, "Prime divisors of the Lagarias sequence", JTNB 13 (2001), https://doi.org/10.5802/jtnb.318 ; Kummer/Chebotarev approach under GRH; does not constrain every prime index in our problem.
6. P. M. Voutier, "Primitive divisors of Lucas and Lehmer sequences, III", Math. Proc. Camb. Phil. Soc. 123 (1998), https://doi.org/10.1017/S0305004197002223 ; precursor to BHV; existence is weaker than existence of a proper divisor.
7. Y. Bilu, G. Hanrot, P. M. Voutier, "Existence of primitive divisors of Lucas and Lehmer numbers", J. reine angew. Math. 539 (2001), https://doi.org/10.1515/crll.2001.080 ; primitive divisors for index >30, still possibly the full term.
8. Y. Bugeaud, M. Mignotte, S. Siksek, "Classical and modular approaches to exponential Diophantine equations I", Ann. Math. 163 (2006), https://doi.org/10.4007/annals.2006.163.969 ; perfect power method not valid as a bound when exponent=1 and prime base varies.
9. Same authors, part II, https://doi.org/10.1112/S0010437X05001739 ; fixed-D Lebesgue–Nagell comparison, no direct application to variable prime p,q here.
10. J.-H. Evertse, H. P. Schlickewei, W. M. Schmidt, "Linear equations in variables which lie in a multiplicative group", Ann. Math. 155 (2002), https://doi.org/10.2307/3062133 ; finite-rank group solution bounds; variable p,q prevent assuming all pairs lie in a fixed finite-rank group.
11. Mathlib Pell, https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/NumberTheory/Pell.lean ; standard norm +1 theory. Its documentation explicitly leaves norm −1 extension as TODO; we instead give direct descent specialized to d=2.
12. A. Schinzel, "An extension of the theorem on primitive divisors in algebraic number fields", Math. Comp. 61 (1993), https://www.ams.org/mcom/1993-61-203/S0025-5718-1993-1189523-2/ ; ideal primitive divisors of twisted differences, no proper-divisor guarantee.

The first two references are used as concrete proof bridges; rank and primitive-divisor references guide the existing sieve; the rest are documented comparison routes, not imported as unjustified hypotheses. Bibliography is selective, not exhaustive. Master unchanged.


## Verified status (v4.2)

- Structural modules (Newton power sum, Capelli reduction, trace identity, negative Pell completeness): PASS, https://github.com/corcondor/mathos/actions/runs/45492120163 .
- Odd-sum and coefficient reduction (t=2, square factor, r=2): PASS, https://github.com/corcondor/mathos/actions/runs/45491945611 .
- Composed original equivalence: source V42Full.lean, repaired in 677adf1; CI not yet confirmed at time of recording, https://github.com/corcondor/mathos/actions/runs/45492500844 .
- The above passing audits use only propext, Classical.choice, Quot.sound. Full simultaneous-prime finiteness remains unproved.
