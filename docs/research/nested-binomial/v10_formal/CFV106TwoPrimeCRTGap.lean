import Mathlib.Tactic

/-!
# v106: abstract two-prime CRT height contradiction

This is only the exact **final integer algebra** of the new theorem:
two rational modular residues of opposite signs, at moduli q and q+h,
force an explicit *k-independent bound* on q.

The preceding Lucas-forced divisibility and the Wolstenholme/Wilson
binomial-unit congruence remain written proofs in the v106 research note.
Do NOT infer those analytic/combinatorial inputs from this Lean theorem.
-/

namespace NestedBinomialV106

/-- If two modular conditions lift to
    U*m+A=u*q and V*m-B=v*(q+h),
with positive denominators, residue representatives u<U, v<V,
then q is bounded only by U,V,h,A,B.  The proof is exact integer algebra,
not a computation on bounded integers. -/
theorem two_prime_crt_strict_bound
    (q h U V A B m u v : ℤ)
    (hq : 0 < q) (hh : 0 < h)
    (hU : 0 < U) (hV : 0 < V)
    (hA : 0 < A) (hB : 0 < B)
    (hv : 0 < v) (hvV : v < V)
    (heq1 : U * m + A = u * q)
    (heq2 : V * m - B = v * (q + h)) :
    q < U * V * h + V * A + U * B := by
  have hm1 := congrArg (fun z : ℤ => V * z) heq1
  have hm2 := congrArg (fun z : ℤ => U * z) heq2
  have hidentity :
      (V * u - U * v) * q = U * v * h + V * A + U * B := by
    nlinarith [hm1, hm2]
  have hr : 0 < U * v * h + V * A + U * B := by
    positivity
  have hc : 0 < V * u - U * v := by
    by_contra hn
    have hn' : V * u - U * v ≤ 0 := le_of_not_gt hn
    have hneg : (V * u - U * v) * q ≤ 0 :=
      mul_nonpos_of_nonpos_of_nonneg hn' (le_of_lt hq)
    omega
  have hc1 : 1 ≤ V * u - U * v := by omega
  have hmin : q ≤ (V * u - U * v) * q := by
    have hnon : 0 ≤ V * u - U * v - 1 := by omega
    have hmul := mul_nonneg hnon (le_of_lt hq)
    nlinarith
  have hgap : U * v * h < U * V * h := by
    have hdiff : 0 < V - v := by omega
    have hpos : 0 < U * (V - v) * h :=
      mul_pos (mul_pos hU hdiff) hh
    nlinarith
  calc
    q ≤ (V * u - U * v) * q := hmin
    _ = U * v * h + V * A + U * B := hidentity
    _ < U * V * h + V * A + U * B := by nlinarith [hgap]

#print axioms NestedBinomialV106.two_prime_crt_strict_bound

end NestedBinomialV106
