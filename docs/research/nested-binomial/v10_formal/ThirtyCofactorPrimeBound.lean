import Mathlib.Tactic


namespace NestedBinomialV10
theorem pow_factorization_choose_six_w (p w : ℕ) (hw : 1 ≤ w) : p ^ (Nat.choose (6 * w) (2 * w)).factorization p ≤ 6 * w := by
  have hn : 0 < 6 * w := by omega
  exact Nat.pow_factorization_choose_le (p := p) (n := 6 * w) (k := 2 * w) hn

theorem factorization_div_gcd_le (p w : ℕ) : (Nat.choose (6 * w) (2 * w) / Nat.gcd (Nat.choose (6 * w) (2 * w)) 6).factorization p ≤ (Nat.choose (6 * w) (2 * w)).factorization p := by
  rw [Nat.factorization_div (Nat.gcd_dvd_left (Nat.choose (6 * w) (2 * w)) 6)]
  exact Nat.sub_le _ _

theorem prime_pow_bound (p w : ℕ) (hw : 1 ≤ w) : p ^ (Nat.choose (6 * w) (2 * w) / Nat.gcd (Nat.choose (6 * w) (2 * w)) 6).factorization p ≤ 6 * w := by
  by_cases hp0 : p = 0
  · subst hp0
    cases h : (Nat.choose (6 * w) (2 * w) / Nat.gcd (Nat.choose (6 * w) (2 * w)) 6).factorization 0 with
    | zero =>
        rw [pow_zero]
        omega
    | succ n =>
        rw [pow_succ, mul_zero]
        exact Nat.zero_le _
  · have hp1 : 1 ≤ p := Nat.succ_le_of_lt (Nat.pos_of_ne_zero hp0)
    exact (pow_right_mono₀ hp1 (factorization_div_gcd_le p w)).trans
      (pow_factorization_choose_six_w p w hw)

theorem height_bound_ge_five (p w a : ℕ) (hw : 1 ≤ w) (h : 25 * p ^ a ≤ 216 * w ^ 3) : w * p ^ a + 2 < 9 * w ^ 4 + 2 := by
  have hwpos : 0 < w := by omega
  have hw4pos : 0 < w ^ 4 := pow_pos hwpos 4
  have hmul : 25 * (w * p ^ a) ≤ 216 * w ^ 4 := by
    calc
      25 * (w * p ^ a) = (25 * p ^ a) * w := by ring
      _ ≤ (216 * w ^ 3) * w := by gcongr
      _ = 216 * w ^ 4 := by ring
  have h216 : 216 * w ^ 4 < 225 * w ^ 4 := by nlinarith [hw4pos]
  have h25 : 25 * (w * p ^ a) < 25 * (9 * w ^ 4) := by
    calc
      25 * (w * p ^ a) ≤ 216 * w ^ 4 := hmul
      _ < 225 * w ^ 4 := h216
      _ = 25 * (9 * w ^ 4) := by ring
  have hlt : w * p ^ a < 9 * w ^ 4 := by nlinarith [h25]
  omega

#print axioms pow_factorization_choose_six_w
#print axioms factorization_div_gcd_le
#print axioms prime_pow_bound
#print axioms height_bound_ge_five

end NestedBinomialV10
