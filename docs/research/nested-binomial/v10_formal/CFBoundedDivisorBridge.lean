import Mathlib.Tactic
import CFCurveRecovery

/-!
# A finite divisor bridge for the frozen CF small-defect goal

This file connects the verified CFCurveRecovery identities to the
v11 bounded-divisor lemma without importing an untracked v11 module.

For primitive p/q, every original curve point has
D = T*q^3 - 6*S*p^3 > 0 and D | 6*S*T. Thus D belongs to the
explicit finite divisor certificate for each S,T.

This bridge does NOT claim the finite certificate is checked in Lean
and it does not claim either frozen final goal.
-/

namespace NestedBinomialV10

/-- A self-contained copy of the verified v11 cubic-divisor argument,
now kept with the v10 CF certificate dependency chain. -/
theorem cf_cubic_difference_divisor_bound (a t p q d : ℕ)
    (hcop : p.Coprime q)
    (heq : d + a * p ^ 3 = t * q ^ 3)
    (hd : d ∣ t * q) : d ∣ a * t := by
  have hright : d ∣ t * (t * q ^ 3) := by
    convert dvd_mul_of_dvd_left hd (t * q ^ 2) using 1
    ring
  have hsum : d ∣ t * d + (a * t) * p ^ 3 := by
    convert hright using 1
    nlinarith [congrArg (fun x => t * x) heq]
  have htd : d ∣ t * d := by
    exact dvd_mul_left d t
  have hp : d ∣ (a * t) * p ^ 3 := (Nat.dvd_add_iff_right htd).mpr hsum
  have hq : d ∣ (a * t) * q := by
    convert dvd_mul_of_dvd_right hd a using 1
    ring
  have hg := Nat.dvd_gcd hp hq
  rw [Nat.gcd_mul_left, (hcop.pow_left 3).gcd_eq_one, Nat.mul_one] at hg
  exact hg

/-- An exact bridge from CFCurveRecovery into the finite D-divisor list. -/
theorem cf_curve_recovery_D_dvd_bounded_product
    (S T n r g p q : ℕ)
    (hn : 2 ≤ n) (hg : 0 < g) (hT : 0 < T)
    (hr : r = g * p) (hq : n - 1 = g * q)
    (hcop : p.Coprime q)
    (hcurve : 6 * S * r ^ 3 = T * n * (n - 1) * (n - 2)) :
    (T * q ^ 3 - 6 * S * p ^ 3) ∣ 6 * S * T := by
  have hDpos :=
    curve_recovery_lt S T n r g p q hn hg hT hr hq hcurve
  have hDdvd :=
    curve_recovery_D_dvd S T n r g p q hn hg hT hr hq hcurve
  have heq :
      (T * q ^ 3 - 6 * S * p ^ 3) + 6 * S * p ^ 3 =
        T * q ^ 3 := Nat.sub_add_cancel (Nat.le_of_lt hDpos)
  exact cf_cubic_difference_divisor_bound (6 * S) T p q
    (T * q ^ 3 - 6 * S * p ^ 3) hcop heq hDdvd

/-- Positivity supplies the exact upper bound used by the certificate
sieve: no false-positive modular residue is interpreted as an equality. -/
theorem cf_curve_recovery_D_le_bounded_product
    (S T n r g p q : ℕ)
    (hn : 2 ≤ n) (hg : 0 < g) (hS : 0 < S) (hT : 0 < T)
    (hr : r = g * p) (hq : n - 1 = g * q)
    (hcop : p.Coprime q)
    (hcurve : 6 * S * r ^ 3 = T * n * (n - 1) * (n - 2)) :
    T * q ^ 3 - 6 * S * p ^ 3 ≤ 6 * S * T := by
  have hd : T * q ^ 3 - 6 * S * p ^ 3 ∣ 6 * S * T :=
    cf_curve_recovery_D_dvd_bounded_product
      S T n r g p q hn hg hT hr hq hcop hcurve
  have hpos : 0 < 6 * S * T := by
    exact Nat.mul_pos (Nat.mul_pos (by decide : (0:ℕ)<6) hS) hT
  exact Nat.le_of_dvd hpos hd

#print axioms cf_cubic_difference_divisor_bound
#print axioms cf_curve_recovery_D_dvd_bounded_product
#print axioms cf_curve_recovery_D_le_bounded_product

end NestedBinomialV10
