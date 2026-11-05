import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic

/-!
Necessary divisibility conditions for the original squared-index equation.
This file does not assert that the original equation has no solutions.
No analytic gap bound or finite search is assumed in `ell_one_cube_divisibility`.
-/

namespace NestedBinomial

def Equation (i j k ell : ℕ) : Prop :=
  (i.choose j).choose (k.choose ell) =
    (i ^ 2).choose (j ^ 2) + (k ^ 2).choose (ell ^ 2)

theorem top_dvd_bottom_mul_choose (n k : ℕ) : n ∣ k * n.choose k := by
  cases n with
  | zero => cases k <;> simp [Nat.choose]
  | succ n =>
    cases k with
    | zero => simp
    | succ k =>
      refine ⟨n.choose k, ?_⟩
      simpa [Nat.succ_eq_add_one, Nat.mul_comm] using
        (Nat.add_one_mul_choose_eq n k).symm

theorem div_gcd_dvd_of_dvd_mul {i j a : ℕ} (hi : 0 < i)
    (h : i ∣ j * a) : i / Nat.gcd i j ∣ a := by
  have hg : 0 < Nat.gcd i j := Nat.gcd_pos_of_pos_left j hi
  have hmul : Nat.gcd i j * (i / Nat.gcd i j) ∣
      Nat.gcd i j * ((j / Nat.gcd i j) * a) := by
    simpa only [← Nat.mul_assoc, Nat.mul_div_cancel' (Nat.gcd_dvd_left i j),
      Nat.mul_div_cancel' (Nat.gcd_dvd_right i j)] using h
  exact (Nat.coprime_div_gcd_div_gcd hg).dvd_of_dvd_mul_left
    ((Nat.mul_dvd_mul_iff_left hg).mp hmul)

theorem div_gcd_dvd_choose (i j : ℕ) (hi : 0 < i) :
    i / Nat.gcd i j ∣ i.choose j :=
  div_gcd_dvd_of_dvd_mul hi (top_dvd_bottom_mul_choose i j)

theorem div_gcd_sq_dvd_squared_index_choose (i j : ℕ) (hi : 0 < i) :
    (i / Nat.gcd i j) ^ 2 ∣ (i ^ 2).choose (j ^ 2) := by
  have h := div_gcd_dvd_choose (i ^ 2) (j ^ 2) (pow_pos hi 2)
  simpa only [Nat.pow_gcd_pow, ← Nat.div_pow (Nat.gcd_dvd_left i j)] using h

theorem outer_other_term_divisibility (A B X Y q r : ℕ)
    (hA : q ∣ A) (hX : q ∣ X)
    (heq : A.choose B = X + Y) (hsym : A.choose r = A.choose B) :
    q ∣ r * Y := by
  have hleft : q ∣ r * A.choose r :=
    hA.trans (top_dvd_bottom_mul_choose A r)
  rw [hsym, heq, Nat.mul_add] at hleft
  exact (Nat.dvd_add_iff_right (dvd_mul_of_dvd_right hX r)).mpr hleft

theorem outer_cube_divisibility (A B X q : ℕ) (hBA : B ≤ A)
    (hA : q ∣ A) (hX : q ∣ X) (heq : A.choose B = X + B ^ 2) :
    q ∣ (min B (A - B)) ^ 3 := by
  by_cases hmin : B ≤ A - B
  · rw [min_eq_left hmin]
    have h := outer_other_term_divisibility A B X (B ^ 2) q B hA hX heq rfl
    simpa [pow_succ, Nat.mul_comm] using h
  · rw [min_eq_right (by omega : A - B ≤ B)]
    let r := A - B
    have hAB : A = B + r := by dsimp [r]; omega
    have h := outer_other_term_divisibility A B X (B ^ 2) q r hA hX heq
      (Nat.choose_symm hBA)
    have hAr : q ∣ 2 * A * r ^ 2 := by
      simpa [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using
        (dvd_mul_of_dvd_left hA (2 * r ^ 2))
    have hAAr : q ∣ A ^ 2 * r := by
      simpa [pow_two] using
        (dvd_mul_of_dvd_left (dvd_mul_of_dvd_left hA A) r)
    have hid : r * B ^ 2 + 2 * A * r ^ 2 = r ^ 3 + A ^ 2 * r := by
      rw [hAB]
      ring
    have hsum := dvd_add h hAr
    rw [hid] at hsum
    exact (Nat.dvd_add_iff_left hAAr).mpr hsum

/-- The full new necessary condition for ell = 1, in either outer branch. -/
theorem ell_one_cube_divisibility (i j k : ℕ) (hi : 0 < i)
    (hk : k ≤ i.choose j)
    (heq : (i.choose j).choose k = (i ^ 2).choose (j ^ 2) + k ^ 2) :
    i / Nat.gcd i j ∣ (min k (i.choose j - k)) ^ 3 := by
  have hsq := div_gcd_sq_dvd_squared_index_choose i j hi
  have hq : i / Nat.gcd i j ∣ (i ^ 2).choose (j ^ 2) := by
    apply dvd_trans (b := (i / Nat.gcd i j) ^ 2) _ hsq
    simp [pow_two]
  exact outer_cube_divisibility (i.choose j) k ((i ^ 2).choose (j ^ 2))
    (i / Nat.gcd i j) hk (div_gcd_dvd_choose i j hi) hq heq

#print axioms ell_one_cube_divisibility

theorem original_ell_one_cube_divisibility (i j k : ℕ) (hi : 0 < i)
    (hk : k ≤ i.choose j) (heq : Equation i j k 1) :
    i / Nat.gcd i j ∣ (min k (i.choose j - k)) ^ 3 := by
  apply ell_one_cube_divisibility i j k hi hk
  simpa [Equation] using heq

/-- General necessary condition, with neither ell=1 nor an analytic bound. -/
theorem original_other_term_divisibility (i j k ell : ℕ) (hi : 0 < i)
    (hk : k.choose ell ≤ i.choose j) (heq : Equation i j k ell) :
    i / Nat.gcd i j ∣
      min (k.choose ell) (i.choose j - k.choose ell) * (k ^ 2).choose (ell ^ 2) := by
  have hsq := div_gcd_sq_dvd_squared_index_choose i j hi
  have hq : i / Nat.gcd i j ∣ (i ^ 2).choose (j ^ 2) := by
    apply dvd_trans (b := (i / Nat.gcd i j) ^ 2) _ hsq
    simp [pow_two]
  have hA := div_gcd_dvd_choose i j hi
  by_cases hmin : k.choose ell ≤ i.choose j - k.choose ell
  · rw [min_eq_left hmin]
    exact outer_other_term_divisibility _ _ _ _ _ _ hA hq heq rfl
  · rw [min_eq_right (by omega : i.choose j - k.choose ell ≤ k.choose ell)]
    exact outer_other_term_divisibility _ _ _ _ _ _ hA hq heq (Nat.choose_symm hk)

#print axioms original_ell_one_cube_divisibility
#print axioms original_other_term_divisibility

/-- The unrestricted-integer valuation implication discovered by the SMT run.
    The hypotheses are necessary valuation relations, not a full encoding of
    the original equation. This proof uses Lean's proof-producing arithmetic. -/
theorem valuation_cubic_cap (c alpha rho beta chi lam : ℕ)
    (ha : c ≤ alpha) (hx : 2 * c ≤ chi)
    (hmul : alpha ≤ rho + lam)
    (hres : rho < alpha → beta = rho)
    (hmin : (lam = chi ∧ lam ≤ 2 * beta) ∨
      (lam = 2 * beta ∧ lam ≤ chi) ∨ (chi = 2 * beta ∧ chi ≤ lam)) :
    c ≤ 3 * rho := by
  by_contra hc
  have hr : rho < alpha := by omega
  have hb := hres hr
  rcases hmin with h | h | h <;> omega

#print axioms valuation_cubic_cap

/-- Any common divisor can be used, including factors coming from i-1.
    No analytic interval or factorization hypothesis is assumed. -/
theorem original_ell_one_full_gcd_divisibility (i j k : ℕ)
    (hk : k ≤ i.choose j) (heq : Equation i j k 1) :
    Nat.gcd (i.choose j) ((i ^ 2).choose (j ^ 2)) ∣
      (min k (i.choose j - k)) ^ 3 := by
  apply outer_cube_divisibility (i.choose j) k ((i ^ 2).choose (j ^ 2))
    (Nat.gcd (i.choose j) ((i ^ 2).choose (j ^ 2))) hk
    (Nat.gcd_dvd_left _ _) (Nat.gcd_dvd_right _ _)
  simpa [Equation] using heq

/-- Two coprime common divisors combine multiplicatively. -/
theorem original_ell_one_coprime_common_divisors (i j k q₀ q₁ : ℕ)
    (hk : k ≤ i.choose j) (heq : Equation i j k 1)
    (hcop : Nat.Coprime q₀ q₁)
    (hA₀ : q₀ ∣ i.choose j) (hX₀ : q₀ ∣ (i ^ 2).choose (j ^ 2))
    (hA₁ : q₁ ∣ i.choose j) (hX₁ : q₁ ∣ (i ^ 2).choose (j ^ 2)) :
    q₀ * q₁ ∣ (min k (i.choose j - k)) ^ 3 := by
  have h := original_ell_one_full_gcd_divisibility i j k hk heq
  apply dvd_trans _ h
  exact hcop.mul_dvd_of_dvd_of_dvd (Nat.dvd_gcd hA₀ hX₀) (Nat.dvd_gcd hA₁ hX₁)

#print axioms original_ell_one_full_gcd_divisibility
#print axioms original_ell_one_coprime_common_divisors

end NestedBinomial
