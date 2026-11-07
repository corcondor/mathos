import Mathlib.Data.Nat.GCD.Basic


namespace NestedBinomialV10
theorem defect_coprime_pell_coefficient (Q r : ℕ) (hQ : 0 < Q) : Nat.Coprime (Q / Nat.gcd Q (r ^ 2)) (r ^ 2 / Nat.gcd Q (r ^ 2)) := by
  exact Nat.coprime_div_gcd_div_gcd (Nat.pos_of_dvd_of_pos (Nat.gcd_dvd_left Q (r ^ 2)) hQ)

theorem defect_pell_identity (M Q n r : ℕ) (hM : M * Q = n * (n - 1)) : M * (Q / Nat.gcd Q (r ^ 2)) * r ^ 2 = (r ^ 2 / Nat.gcd Q (r ^ 2)) * n * (n - 1) := by
  have hQ : Nat.gcd Q (r ^ 2) ∣ Q := Nat.gcd_dvd_left Q (r ^ 2)
  have hr : Nat.gcd Q (r ^ 2) ∣ r ^ 2 := Nat.gcd_dvd_right Q (r ^ 2)
  calc
    M * (Q / Nat.gcd Q (r ^ 2)) * r ^ 2
        = M * (Q / Nat.gcd Q (r ^ 2)) * ((r ^ 2 / Nat.gcd Q (r ^ 2)) * Nat.gcd Q (r ^ 2)) := by
          rw [Nat.div_mul_cancel hr]
    _ = M * ((Q / Nat.gcd Q (r ^ 2)) * Nat.gcd Q (r ^ 2)) * (r ^ 2 / Nat.gcd Q (r ^ 2)) := by
          ac_rfl
    _ = M * Q * (r ^ 2 / Nat.gcd Q (r ^ 2)) := by
          rw [Nat.div_mul_cancel hQ]
    _ = (r ^ 2 / Nat.gcd Q (r ^ 2)) * (M * Q) := by
          ac_rfl
    _ = (r ^ 2 / Nat.gcd Q (r ^ 2)) * (n * (n - 1)) := by
          rw [hM]
    _ = (r ^ 2 / Nat.gcd Q (r ^ 2)) * n * (n - 1) := by
          ac_rfl

#print axioms defect_coprime_pell_coefficient
#print axioms defect_pell_identity

end NestedBinomialV10
