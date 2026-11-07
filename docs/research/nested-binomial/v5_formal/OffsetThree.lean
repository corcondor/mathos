import Mathlib.Algebra.Squarefree.Basic
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

/-- The arithmetic end of the offset-three exclusion.
    The strict analytic window is an explicit hypothesis. -/
theorem squarefree_gap_contradiction (i g q r : ℕ)
    (hg : g ≤ 3) (hiq : i = g * q)
    (hsq : Squarefree q) (hdiv : q ∣ r ^ 3)
    (hlo : 3 * i < r) (hhi : 3 * r < 10 * i) : False := by
  have hqr : q ∣ r := (hsq.dvd_pow_iff_dvd (by decide : (3 : ℕ) ≠ 0)).mp hdiv
  have hqi : q ∣ i := by rw [hiq]; exact dvd_mul_left q g
  have hq3i : q ∣ 3 * i := dvd_mul_of_dvd_right hqi 3
  have hqdelta : q ∣ r - 3 * i := Nat.dvd_sub hqr hq3i
  have hpos : 0 < r - 3 * i := by omega
  have hqle : q ≤ r - 3 * i := Nat.le_of_dvd hpos hqdelta
  have hile : i ≤ 3 * q := by rw [hiq]; exact Nat.mul_le_mul_right q hg
  omega

/-- Applies the previously kernel-checked divisibility theorem to the
    original equation. The analytic window is not formalized here. -/
theorem original_offset_three_squarefree_contradiction (i j k : ℕ)
    (hij : i = j + 3) (hk : k ≤ i.choose j)
    (hsq : Squarefree (i / Nat.gcd i j))
    (hlo : 3 * i < min k (i.choose j - k))
    (hhi : 3 * min k (i.choose j - k) < 10 * i)
    (heq : Equation i j k 1) : False := by
  have hi : 0 < i := by omega
  have hg3 : Nat.gcd i j ∣ 3 := by
    have hd := Nat.dvd_sub (Nat.gcd_dvd_left i j) (Nat.gcd_dvd_right i j)
    simpa [hij] using hd
  have hg : Nat.gcd i j ≤ 3 := Nat.le_of_dvd (by decide) hg3
  have hiq : i = Nat.gcd i j * (i / Nat.gcd i j) :=
    (Nat.mul_div_cancel' (Nat.gcd_dvd_left i j)).symm
  exact squarefree_gap_contradiction i (Nat.gcd i j)
    (i / Nat.gcd i j) (min k (i.choose j - k)) hg hiq hsq
    (original_ell_one_cube_divisibility i j k hi hk heq) hlo hhi

#print axioms squarefree_gap_contradiction
#print axioms original_offset_three_squarefree_contradiction

/-- The final residue obstruction in the powers-of-three proof.
    Deriving this residue from the binomial equation is not formalized here. -/
theorem cube_mod_nine_ne_four_or_five (v : ℕ) :
    v ^ 3 % 9 ≠ 4 ∧ v ^ 3 % 9 ≠ 5 := by
  have hv : v % 9 < 9 := Nat.mod_lt v (by decide)
  rw [Nat.pow_mod]
  interval_cases h : v % 9 <;> norm_num

#print axioms cube_mod_nine_ne_four_or_five

end NestedBinomial
