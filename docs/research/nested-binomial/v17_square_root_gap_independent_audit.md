# Independent audit of the v17 square-root boundary certificate

Date: 2026-11-06 JST. Status: **PASS**.

This audit was implemented by a collaborator other than the producer.
It does not import or execute `v17_square_root_gap.py`. It reads the
producer source only to check its SHA-256 binding. This is an internal
independent calculation, not external peer review or a new Lean run.

## Inputs and the second encoding

The inputs are `v17_square_root_gap.md`, its generator, and the complete
`v17_square_root_gap_results.json`. The written proof supplies the finite
coefficient/residual bounds and their applicability to every necessary
pair in the claimed region. The audit does not substitute a finite
scan in n for that mathematical coverage argument.

The producer enumerates coprime pairs (a,b), b|486, 27a<31b, and their
normalized residual j. The auditor instead uses the fact that every
actual M in {1,2,3,6} divides 6. Rescale h/M to the artificial value M=6:

\[
H=6h/M\in\mathbb Z_{>0}.
\]

The complete range h/M<93 is exactly covered by H=1,...,557. Put
G=gcd(H,486); only for comparison with the stored certificate do we
map to a=H/G, b=486/G. This gives all 557 coefficient pairs exactly once.

The auditor enumerates the unnormalized residual \(\mathcal J\):

\[
\mathcal J\equiv H^2\pmod{486G},\qquad
0<\mathcal J<\frac{8H^2+184680\cdot36}{51}.
\]

Its normalized value is j=\(\mathcal J/G^2\). The arithmetic progressions,
first positive elements, and upper endpoints agree with every producer
family, including empty progressions.

To reconstruct t, the audit independently eliminates n from the raw
residual definition and

\[
Hn(n-1)=6\{(9t^2+27t+27)n+t^3\}.
\]

The resulting polynomial is constructed with exact integer coefficient
arithmetic. Its fourth- and third-degree terms cancel, leaving a
quadratic. Both rational roots are retained; repeated roots are counted
once. For an integer t>=4 the audit reconstructs n using the positive
root of the original h-quadratic, rather than the producer's linear
residual formula. The actual M is then recovered and checked.

## Exhaustive comparisons

Every per-residual negative/nonsquare/square disposition, every square
discriminant, both rational t roots and their classifications, and all
integer-n reconstructions agree exactly.

| Quantity | Independently reproduced count |
|---|---:|
| Coefficient pairs | 557 |
| Residual values | 94,710 |
| Square discriminants | 272 |
| Integer t>=4 | 30 |
| Integer n>=104 | 13 |
| Restored necessary pairs | 13 |
| Pairs with t^2=9n | 13 |
| Original k branches excluded | 26 |

The h<=81M subdomain was also exhaustively reproduced: 486 coefficient
pairs, 80,274 residual values, 199 square discriminants, 17 integer t,
and **0** integer n>=104.

Equality was independently classified by testing the proven divisor
condition s-1|324*gcd(s-1,2), over its complete divisor range s-1<=648.
It gives exactly s=13,19,25,28,37,55,73,82,109,163,217,325,649.
The recovered actual quadratic defects are at most 6.

For each of the 26 original branches, the auditor evaluates
binom(A,k) and binom(n^2,(n-3)^2) at the saved prime using a separately
implemented Pascal-table Lucas calculation. It uses the actual
complementary k and the original squared lower index. Every residue
matches. The largest prime is 13; 24 witnesses have both binomial
residues zero, and the two n=5329 witnesses instead have inner residue
3 modulo 5. All 26 are contradictions.

## Algebra and the stronger original-equation consequence

The independent coefficient arithmetic also verifies:

- The raw and normalized elimination polynomials.
- The cubic coordinate identity and its Weierstrass discriminant.
- The singular family F(1,3,j)=(j+8)^2(49-4j), including its two allowed
  residuals j=1,4; neither produces a square.
- The exact h/M value at t=3*sqrt(n), after the substitution n=s^2,t=3s.
- All rational constants in the residual upper bound.

The calculation does not filter by t^2<=9n during reconstruction.
Therefore the 26 original-equation contradictions exclude **all**
original solutions with h/M<93, and give h>=93M.

For the additional shifted lower bound, put u=t+3 and

\[
E=(9u^2-27u+27)n+(u-3)^3-93n(n-1),
\]

\[
B=n(120-50u/3)-9u^2+27u-27.
\]

The auditor checks the exact factored difference

\[
3(B-E)=(9n+u)(31n-3u^2).
\]

The already established h<4Mt and h>=93M force t>=24 and u>=27.
If u^2<=31n/3, then E<=B<0, whereas h>=93M implies E>=0.
Thus the written argument and the identity verify

\[
(t+3)^2>31n/3.
\]

## Reproduction

All published v17 files belong to the same directory. There, run:

```sh
python3 v17_square_root_gap_independent_audit.py --output reproduced_v17_gap_audit.json
```

For separated input locations, use `--input`, `--generator`, and `--note`.
Only the Python standard library is required. The audit JSON records the
input, generator, proof-note and auditor source hashes, all family
comparisons, the 30 integer-t records, the 13 recovered pairs and all
26 original-equation witnesses.

No complete elliptic-curve solver, new DeepSeek call, new Lean execution,
or solution of the full four-variable equation is claimed.
