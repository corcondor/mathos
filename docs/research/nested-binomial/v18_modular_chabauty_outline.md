# v18 outline: Modular and Chabauty-style approaches for residual curves

Date: 2026-11-07.

This note records a proposed next reduction for the \(\ell=1\), \(j=i-3\) branch of the nested binomial equation. It does not claim a complete proof.

## Residual elliptic curves from v17

From the square-root residual, for each coprime \((a,b)\) with \(b\mid 486\) we obtain the Weierstrass model

\[
Y^2 = X^3 - 3b^2(72a^2 + b^2)X + 2b^2(648a^4 + 180a^2b^2 - b^4).
\]

Discriminant \(-995328 a^2 b^4 (3a-b)^3 (3a+b)^3\). Singular only for \((a,b)=(1,3)\), already handled.

## Proposed directions

### 1. Modular method

- Reconstruct a Frey-type curve or use the existing model to bound the conductor in terms of the residual parameters.
- Since there are only 12 possible denominators \(b\), the set of curves is finite for each fixed \(a\).
- Compare against known modular forms of small level (using existing tables or Magma/Sage).

### 2. Local methods (Chabauty-Coleman)

- For curves of rank 1 (or low rank) over \(\mathbb{Q}\), apply p-adic integrals to constrain rational points.
- Combine with the already proved residual upper bound \(0 < j < (216a^2 + 760b^2)/1377\).
- This yields a finite check per curve, independent of global integer-point solvers.

### 3. Strengthening the primitive defect bound

- Extend the continued-fraction covering and three-descent from v12 to \(H = 21,22,\dots,30\).
- Generate certificates analogous to those for \(H\le 20\).

## Status

Outline only. No new certificates, Lean proofs, or complete computations are included in this commit. Existing v1–v17 materials remain unchanged.

Remaining open: full four-variable equation, the entire offset-three branch, and concrete solutions.
