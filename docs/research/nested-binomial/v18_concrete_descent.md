# v18 concrete descent plan: residual elliptic curves

Date: 2026-11-07.

This note turns the v18 outline into an explicit, executable plan for the residual Weierstrass models arising from the square-root gap analysis in v17. No complete non-existence proof is claimed; the goal is a finite, certifiable reduction for small reduced numerators a.

## 1. Explicit residual models for small a

From v17, for each coprime pair (a, b) with b | 486 and 27a < 31b we have the model

\[
E_{a,b}:\quad Y^2 = X^3 - 3b^2(72a^2 + b^2)X + 2b^2(648a^4 + 180a^2b^2 - b^4).
\]

The residual j satisfies 0 < j < (216a^2 + 760b^2)/1377 and j ≡ a^2 (mod b). Only points that recover an integer j in this range and pass the reconstruction (22)–(19) of v17 are relevant.

### Small a examples (selected)

| a | b | A_4 coefficient | A_6 coefficient | Notes |
|---:|---:|:---:|:---:|:---|
| 1 | 1 | -3(72+1) = -219 | 2(648+180-1) = 1654 | Singular? No |
| 1 | 2 | -3*4*(72+4) = -912 | 2*4*(648+720-16) = 10816 | |
| 1 | 3 | -3*9*(72+9) = -2187 | 2*9*(648+1620-81) = 39366 | Special case already checked |
| 2 | 3 | -3*9*(288+9) = -8019 | 2*9*(10368+1620-81) = 214434 | |
| 5 | 6 | -3*36*(1800+36) = -198288 | 2*36*(405000+16200-1296) = 30283200 | |

(Full coefficient formulas are those of equation (26) in v17_square_root_gap.md.)

For each such pair the conductor of E_{a,b} is finite and computable. Because there are only 12 possible b, fixing a reduces the problem to a finite list of curves.

## 2. Concrete computational steps

### Step A: Rank and torsion (Sage / Magma)

For each fixed a ≤ 20 and each admissible b:

1. Construct the minimal Weierstrass model.
2. Compute the conductor N(E_{a,b}).
3. Compute the rank and generators of the Mordell–Weil group over Q (or a rigorous upper bound).
4. List all integral points with |X| bounded by the residual constraint on j (since X = 4a^2 - b^2 - 4j).

The residual bound on j gives an explicit polynomial bound on |X| of degree 2 in a and b, so the integral-point search is finite and does not rely on a general solver’s completeness.

### Step B: Modular constraint

If the rank is positive, form the Frey-type curve or use the existing model to obtain a Galois representation ho_{E,p} for a prime p of good reduction not dividing the residual denominator.

- Bound the conductor of the representation by a function of a and b only.
- Compare against the finite list of newforms of that level (LMFDB or Magma’s modular forms package).
- A non-congruence for sufficiently large p excludes the curve, hence the corresponding residual.

Because b is restricted to the 12 divisors of 486, the possible conductors grow at most polynomially in a, making the modular check feasible for moderate a.

### Step C: Local Chabauty-style filter

For curves of rank 1, choose a prime p of good reduction with p > residual bound and compute the p-adic closure of the known generators. The residual interval for j translates into a p-adic condition on X, which can be checked by a finite Coleman integral or by direct power-series comparison. This gives an independent certificate that no rational point in the residual range exists, without enumerating all integral points.

## 3. Strengthening H ≥ 21 (parallel track)

The continued-fraction covering of v12 can be re-run for H = 21 to 30 exactly as before. The number of curves is still finite (order of thousands). An independent dyadic verifier already exists; extending the certificate generation script produces the same style of audit trail.

## 4. Immediate executable checklist

- [ ] For a = 1,2,5,7 generate the 12 (or fewer) models and record conductor, rank, and number of integral points inside the residual box.
- [ ] Verify that the singular case (a,b) = (1,3) produces no residual points (already done in v17).
- [ ] Implement a short Sage script that, given a and b, outputs the minimal model and the bound on |X|.
- [ ] Cross-check one modular exclusion for a small a against LMFDB.
- [ ] Update the Japanese progress note once the first batch of ranks is known.

## 5. Relation to existing constraints

Any point that survives the residual curve check must still satisfy:

- P^+(n) < 3√n and P^+(n-1)^2 ≤ 6n-9,
- the quadratic prime-power restrictions of v17,
- w = (n^2+2)/p ≥ 65,
- δ ≥ 13 and H ≥ 21.

These local and global conditions can be imposed as additional filters after the elliptic-curve search, further reducing the candidates that need modular or Chabauty treatment.

## Status

This is a concrete plan with explicit models and finite checks. No new certificates have been generated in this commit. The four-variable equation and the full offset-three branch remain open.
