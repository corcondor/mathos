import Mathlib.Tactic
import CFBoundedDivisorBridge

/-!
# v96: Algebraic bridge from CF positive-divisor recovery to twisted cubes

This module checks elementary identities at the end of the v95
squarefree decomposition. It does not prove existence of the
squarefree factorisation, nor enumerate all CF certificate cases.
-/

namespace NestedBinomialV10

/-- Remove a positive gcd factor from the v95 exact cubic identity. -/
theorem cf_twisted_cube_cancellation
    (T p h e s z C : ℕ) (hh : 0 < h)
    (heq : h * e + h * C * p ^ 3 = T * (h * s * z ^ 2) ^ 3) :
    C * p ^ 3 + e = T * h ^ 2 * s ^ 3 * z ^ 6 := by
  have hcancel : h * (C * p ^ 3 + e) = h * (T * h ^ 2 * s ^ 3 * z ^ 6) := by
    calc
      h * (C * p ^ 3 + e) = h * e + h * C * p ^ 3 := by ring
      _ = T * (h * s * z ^ 2) ^ 3 := heq
      _ = h * (T * h ^ 2 * s ^ 3 * z ^ 6) := by ring
  exact Nat.eq_of_mul_eq_mul_left hh hcancel

/-- The original (n-1) is a coefficient times a perfect cube. -/
theorem cf_twisted_cube_recover_n
    (g q h s A z n : ℕ)
    (hq : q = h * s * z ^ 2)
    (hg : g = A * s * z)
    (hn : n - 1 = g * q) :
    n - 1 = h * A * s ^ 2 * z ^ 3 := by
  calc
    n - 1 = g * q := hn
    _ = h * A * s ^ 2 * z ^ 3 := by
      rw [hg, hq]
      ring

/-- S|(n-2) restricts the cubic coefficient to residue 1 modulo S. -/
theorem cf_twisted_cube_mod_constraint
    (S n h A s z : ℕ) (hn : 2 ≤ n)
    (hdiv : S ∣ n - 2)
    (hform : n - 1 = h * A * s ^ 2 * z ^ 3) :
    (h * A * s ^ 2 * z ^ 3) % S = 1 % S := by
  obtain ⟨k, hk⟩ := hdiv
  have hn1 : n - 1 = S * k + 1 := by omega
  calc
    (h * A * s ^ 2 * z ^ 3) % S = (n - 1) % S := by rw [hform]
    _ = (S * k + 1) % S := by rw [hn1]
    _ = 1 % S := by simp

#print axioms cf_twisted_cube_cancellation
#print axioms cf_twisted_cube_recover_n
#print axioms cf_twisted_cube_mod_constraint

end NestedBinomialV10
