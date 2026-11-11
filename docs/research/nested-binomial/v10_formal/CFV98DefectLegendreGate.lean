import Mathlib.Tactic
import CFV97FinalReduction

/-!
# v98: universal linear denominator threshold for a bounded cubic defect

For EVERY positive S (not just S<=12), a primitive solution to the
cubic curve has D | 6*S*T and hence 2*D < 6*S*27*q as soon as
q >= 17*S, under T < 229*S.

This is the exact integral inequality used in the Legendre
approximation theorem; the real-analytic Legendre implication and
per-curve certificate enumeration are separate obligations.
-/

namespace NestedBinomialV10

/-- The 17*S bound is uniform in S, not a finite S<=12 shortcut. -/
theorem cf_v98_linear_legendre_cutoff
    (S T q : ℕ)
    (hT : T < 229 * S)
    (hq : 17 * S ≤ q) :
    2 * T < 27 * q := by
  omega

/-- A primitive positive divisor D of 6*S*T is below the
integer upper bound needed for 1/(2*q^2)-approximation. -/
theorem cf_v98_bounded_defect_inequality
    (S T q D : ℕ)
    (hS : 0 < S) (hTpos : 0 < T)
    (hT : T < 229 * S)
    (hq : 17 * S ≤ q)
    (hD : D ∣ 6 * S * T) :
    2 * D < 6 * S * (27 * q) := by
  have hST : 0 < 6 * S * T := by positivity
  have hDle : D ≤ 6 * S * T := Nat.le_of_dvd hST hD
  have hTq : 2 * T < 27 * q :=
    cf_v98_linear_legendre_cutoff S T q hT hq
  calc
    2 * D ≤ 2 * (6 * S * T) := Nat.mul_le_mul_left 2 hDle
    _ = (6 * S) * (2 * T) := by ring
    _ < (6 * S) * (27 * q) :=
      Nat.mul_lt_mul_of_pos_left hTq (by positivity)

/-- Apply the *already-verified* v11 bounded-divisor bridge
directly to any primitive point of the original cubic curve. -/
theorem cf_v98_curve_gives_legendre_integral_gap
    (S T n r g p q : ℕ)
    (hS : 0 < S) (hTpos : 0 < T)
    (hn : 2 ≤ n) (hg : 0 < g)
    (hT : T < 229 * S)
    (hqCutoff : 17 * S ≤ q)
    (hr : r = g * p)
    (hnq : n - 1 = g * q)
    (hcop : p.Coprime q)
    (hcurve : 6 * S * r ^ 3 = T * n * (n - 1) * (n - 2)) :
    2 * (T * q ^ 3 - 6 * S * p ^ 3) < 6 * S * (27 * q) := by
  have hDdvd : (T * q ^ 3 - 6 * S * p ^ 3) ∣ 6 * S * T :=
    cf_curve_recovery_D_dvd_bounded_product
      S T n r g p q hn hg hTpos hr hnq hcop hcurve
  exact cf_v98_bounded_defect_inequality
    S T q (T * q ^ 3 - 6 * S * p ^ 3) hS hTpos hT hqCutoff hDdvd

#print axioms cf_v98_linear_legendre_cutoff
#print axioms cf_v98_bounded_defect_inequality
#print axioms cf_v98_curve_gives_legendre_integral_gap

end NestedBinomialV10
