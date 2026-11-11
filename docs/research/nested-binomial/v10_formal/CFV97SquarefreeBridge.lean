import Mathlib.Tactic
import CFV97CurvePrimitive

/-!
# v97: Squarefree-coefficient decomposition for the twisted-cube reduction

The v95 squarefree coefficient is NOT an unexplained external
certificate: it exists for every positive integer T/e.
The second theorem proves the exact squarefree square-lift identity
needed to conclude q/h=s*z², g=A*s*z once g²=(A²*s)*(q/h).

These theorems do not assume the result of Python's 5214-curve
enumeration and do not formalize that enumeration.
-/

namespace NestedBinomialV10

/-- Factor any divisor quotient T/e as a square times a squarefree
coefficient. This is an existence theorem, not a finite search claim. -/
theorem cf_v97_squarefree_coefficient
    (T e : ℕ) (heT : e ∣ T) :
    ∃ A s : ℕ, Squarefree s ∧ T = e * (s * A ^ 2) := by
  obtain ⟨A, s, hrep, hs⟩ :=
    exists_sq_mul_squarefree (T / e)
  refine ⟨A, s, hs, ?_⟩
  calc
    T = e * (T / e) := (Nat.mul_div_cancel' heT).symm
    _ = e * (A ^ 2 * s) := by rw [← hrep]
    _ = e * (s * A ^ 2) := by ring

/-- The squarefree obstruction to a square is itself square:
if g² = A²*s*v and s is squarefree, then v=s*z² and g=A*s*z.
This is the algebraic squarefree step required in v95. -/
theorem cf_v97_squarefree_square_lift
    (A s g v : ℕ)
    (hA : 0 < A) (hs : 0 < s) (hsq : Squarefree s)
    (heq : g ^ 2 = (A ^ 2 * s) * v) :
    ∃ z : ℕ, g = A * s * z ∧ v = s * z ^ 2 := by
  have hAdvd2 : A ^ 2 ∣ g ^ 2 := by
    refine ⟨s * v, ?_⟩
    calc
      g ^ 2 = (A ^ 2 * s) * v := heq
      _ = A ^ 2 * (s * v) := by ring
  have hAdvd : A ∣ g :=
    (Nat.pow_dvd_pow_iff (by decide : (2 : ℕ) ≠ 0)).mp hAdvd2
  obtain ⟨u, hgu⟩ := hAdvd
  have hA2 : A ^ 2 * u ^ 2 = A ^ 2 * (s * v) := by
    calc
      A ^ 2 * u ^ 2 = (A * u) ^ 2 := by ring
      _ = g ^ 2 := by rw [hgu]
      _ = (A ^ 2 * s) * v := heq
      _ = A ^ 2 * (s * v) := by ring
  have hu2 : u ^ 2 = s * v :=
    Nat.eq_of_mul_eq_mul_left (pow_pos hA 2) hA2
  have hsdvd2 : s ∣ u ^ 2 := ⟨v, hu2⟩
  have hsdvd : s ∣ u :=
    (Squarefree.dvd_pow_iff_dvd hsq (by decide : (2 : ℕ) ≠ 0)).mp hsdvd2
  obtain ⟨z, huz⟩ := hsdvd
  have hv : s * z ^ 2 = v :=
    Nat.eq_of_mul_eq_mul_left hs (by
      calc
        s * (s * z ^ 2) = (s * z) ^ 2 := by ring
        _ = u ^ 2 := by rw [huz]
        _ = s * v := hu2)
  refine ⟨z, ?_, hv.symm⟩
  calc
    g = A * u := hgu
    _ = A * (s * z) := by rw [huz]
    _ = A * s * z := by ring

#print axioms cf_v97_squarefree_coefficient
#print axioms cf_v97_squarefree_square_lift

end NestedBinomialV10
