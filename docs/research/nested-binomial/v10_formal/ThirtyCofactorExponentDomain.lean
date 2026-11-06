import Mathlib.Tactic


namespace NestedBinomialV10
theorem exponent_domain_iff (α b : ℕ) (hb : 1 ≤ b) : (∃ k : ℕ, α = b + 2 * k ∧ k < b) ↔ (∃ x k : ℕ, α = b + x ∧ x = 2 * k ∧ 3 * x < 2 * α) := by
  constructor
  · rintro ⟨k, hα, hk⟩
    refine ⟨2 * k, k, ?_, rfl, ?_⟩
    · exact hα
    · omega
  · rintro ⟨x, k, hα, hx, hineq⟩
    subst x
    refine ⟨k, hα, ?_⟩
    omega

theorem q_bound_ge_five (p w b a : ℕ) (hp : 5 ≤ p) (hb : 1 ≤ b) (hpb : p ^ b ≤ 6 * w) (ha : a ≤ 3 * b - 2) : 25 * p ^ a ≤ 216 * w ^ 3 := by
  have h25eq : 25 = 5 ^ 2 := by norm_num
  rw [h25eq]
  have h52 : 5 ^ 2 ≤ p ^ 2 := by gcongr
  have hsum : 2 + (3 * b - 2) = 3 * b := by omega
  have hpa : p ^ a ≤ p ^ (3 * b - 2) := by gcongr <;> omega
  have hpb3 : (p ^ b) ^ 3 ≤ (6 * w) ^ 3 := by gcongr
  calc 5 ^ 2 * p ^ a ≤ 5 ^ 2 * p ^ (3 * b - 2) := by gcongr
    _ ≤ p ^ 2 * p ^ (3 * b - 2) := by gcongr
    _ = p ^ (2 + (3 * b - 2)) := (pow_add p 2 (3 * b - 2)).symm
    _ = p ^ (3 * b) := by rw [hsum]
    _ = (p ^ b) ^ 3 := by rw [mul_comm 3 b, pow_mul]
    _ ≤ (6 * w) ^ 3 := hpb3
    _ = 216 * w ^ 3 := by ring

theorem q_bound_two (w b a : ℕ) (hb : 1 ≤ b) (hpb : 2 ^ b ≤ 3 * w) (ha : a ≤ 3 * b - 2) : 4 * 2 ^ a ≤ 27 * w ^ 3 := by
  have h4 : 4 = 2 ^ 2 := by norm_num
  rw [h4]
  have hsum : 2 + (3 * b - 2) = 3 * b := by omega
  have hpa : 2 ^ a ≤ 2 ^ (3 * b - 2) := by gcongr <;> omega
  have hpb3 : (2 ^ b) ^ 3 ≤ (3 * w) ^ 3 := by gcongr
  calc
    2 ^ 2 * 2 ^ a ≤ 2 ^ 2 * 2 ^ (3 * b - 2) := by gcongr
    _ = 2 ^ (2 + (3 * b - 2)) := (pow_add 2 2 (3 * b - 2)).symm
    _ = 2 ^ (3 * b) := by rw [hsum]
    _ = (2 ^ b) ^ 3 := by rw [mul_comm 3 b, pow_mul]
    _ ≤ (3 * w) ^ 3 := hpb3
    _ = 27 * w ^ 3 := by ring

theorem q_bound_three (w b a : ℕ) (hb : 1 ≤ b) (hpb : 3 ^ b ≤ 2 * w) (ha : a ≤ 3 * b - 1) : 3 * 3 ^ a ≤ 8 * w ^ 3 := by
  have hpa : 3 ^ a ≤ 3 ^ (3 * b - 1) := by gcongr <;> omega
  have hsum : 1 + (3 * b - 1) = 3 * b := by omega
  have hpb3 : (3 ^ b) ^ 3 ≤ (2 * w) ^ 3 := by gcongr
  calc
    3 * 3 ^ a ≤ 3 * 3 ^ (3 * b - 1) := Nat.mul_le_mul_left 3 hpa
    _ = 3 ^ (1 + (3 * b - 1)) := by
      rw [pow_add]
      norm_num
    _ = 3 ^ (3 * b) := by rw [hsum]
    _ = (3 ^ b) ^ 3 := by rw [mul_comm 3 b, pow_mul]
    _ ≤ (2 * w) ^ 3 := hpb3
    _ = 8 * w ^ 3 := by ring

#print axioms exponent_domain_iff
#print axioms q_bound_ge_five
#print axioms q_bound_two
#print axioms q_bound_three

end NestedBinomialV10
