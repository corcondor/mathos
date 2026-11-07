import Mathlib.Tactic

namespace NestedBinomialV11

/-- Integer recovery on a primitive cubic curve forces a bounded divisor. -/
theorem cubic_difference_dvd_product (a t p q d : ℕ)
    (hcop : p.Coprime q) (heq : d + a * p ^ 3 = t * q ^ 3)
    (hd : d ∣ t * q) : d ∣ a * t := by
  have hright : d ∣ t * (t * q ^ 3) := by
    convert dvd_mul_of_dvd_left hd (t * q ^ 2) using 1; ring
  have hsum : d ∣ t * d + (a * t) * p ^ 3 := by
    convert hright using 1; nlinarith [congrArg (fun x => t * x) heq]
  have htd : d ∣ t * d := by exact dvd_mul_left d t
  have hp : d ∣ (a * t) * p ^ 3 := (Nat.dvd_add_iff_right htd).mpr hsum
  have hq : d ∣ (a * t) * q := by
    convert dvd_mul_of_dvd_right hd a using 1; ring
  have hg := Nat.dvd_gcd hp hq
  rw [Nat.gcd_mul_left, (hcop.pow_left 3).gcd_eq_one, Nat.mul_one] at hg
  exact hg

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

/-- Any divisor of the upper argument coprime to the lower divides choose. -/
theorem divisor_of_top_dvd_choose (n k d : ℕ)
    (hdn : d ∣ n) (hcop : d.Coprime k) : d ∣ n.choose k := by
  exact hcop.dvd_of_dvd_mul_left (hdn.trans (top_dvd_bottom_mul_choose n k))

/-- Applied with upper=n^2 and odd lower=6n-9, this gives the first binary gain. -/
theorem four_dvd_choose_of_odd_bottom (n k : ℕ)
    (hfour : 4 ∣ n) (hodd : Odd k) : 4 ∣ n.choose k := by
  apply divisor_of_top_dvd_choose n k 4 hfour
  have htwo : (2 : ℕ).Coprime k := by
    rw [Nat.coprime_two_left]
    exact hodd
  simpa using htwo.pow_left 2

/-- Three forced binary carries suffice for a six-exponent recovered defect gain. -/
theorem binary_defect_gain (alpha x : ℕ) (hx : 3 ≤ x) :
    (if Even x then alpha - 3 * (x / 2) else 0) ≤ alpha - 6 := by
  split_ifs with he
  · obtain ⟨t, ht⟩ := he
    omega
  · omega

/-- Five distinct ordered integer values cannot fit in a real interval of length <4. -/
theorem integer_interval_span_four (a b : ℝ) (m n : ℤ)
    (hwidth : b - a < 4) (hm : a < m ∧ (m : ℝ) < b)
    (hn : a < n ∧ (n : ℝ) < b) : n - m ≤ 3 := by
  have hreal : (n : ℝ) - (m : ℝ) < 4 := by linarith
  have hint : n - m < 4 := by exact_mod_cast hreal
  omega

/-- A real interval of length <1 contains at most one integer. -/
theorem integer_interval_unique (a b : ℝ) (m n : ℤ)
    (hwidth : b - a < 1) (hm : a < m ∧ (m : ℝ) < b)
    (hn : a < n ∧ (n : ℝ) < b) : n = m := by
  have hu : (n : ℝ) - (m : ℝ) < 1 := by linarith
  have hl : (m : ℝ) - (n : ℝ) < 1 := by linarith
  have hu' : n - m < 1 := by exact_mod_cast hu
  have hl' : m - n < 1 := by exact_mod_cast hl
  omega

theorem cube_interval_constants :
    8 * (229 : ℕ) ^ 2 < 75 ^ 3 ∧
    8 * (162 : ℕ) ^ 2 > 59 ^ 3 ∧
    (8 : ℕ) ^ 3 < 4 ^ 3 * 14 ∧
    14 * (3 : ℕ) ^ 4 > 512 ∧
    14 * (2 : ℕ) ^ 4 > 64 := by norm_num

#print axioms cubic_difference_dvd_product
#print axioms divisor_of_top_dvd_choose
#print axioms four_dvd_choose_of_odd_bottom
#print axioms binary_defect_gain
#print axioms integer_interval_span_four
#print axioms integer_interval_unique
#print axioms cube_interval_constants

end NestedBinomialV11
