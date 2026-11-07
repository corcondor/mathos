import Mathlib.Tactic
import CFApproximationCore
import CFCoefficientRanges


namespace NestedBinomialV10
theorem reduced_approximation_mem_coefficientCandidates (alpha : ℝ) (p q P Q Pm Qm Pn Qn aNext : ℤ) (hq : 0 < q) (hQ : 0 < Q) (hQm_nonneg : 0 ≤ Qm) (hQn : 0 < Qn) (hQm_le_Q : Qm ≤ Q) (hQ_le_q : Q ≤ q) (hq_lt_Qn : q < Qn) (hdet : |P * Qm - Pm * Q| = 1) (hPnext : Pn = aNext * P + Pm) (hQnext : Qn = aNext * Q + Qm) (hred : Nat.Coprime (Int.natAbs p) (Int.natAbs q)) (hcopPQ : Nat.Coprime (Int.natAbs P) (Int.natAbs Q)) (happrox : |alpha - (p : ℝ) / (q : ℝ)| < 3 / (2 * (q : ℝ) ^ 2)) (hconv_cur : |(Q : ℝ) * alpha - (P : ℝ)| < 1 / (Qn : ℝ)) (hconv_next : |(Qn : ℝ) * alpha - (Pn : ℝ)| < 1 / (Qn : ℝ)) : ∃ a b c : ℤ, p = a * P + b * Pm ∧ q = a * Q + b * Qm ∧ c = a - b * aNext ∧ p = b * Pn + c * P ∧ q = b * Qn + c * Q ∧ (a, b) ∈ coefficientCandidates aNext := by
  obtain ⟨⟨a, b⟩, ⟨hpq, hqq⟩, _⟩ :=
    unimodular_coordinates_abs P Q Pm Qm p q hdet
  have hb_abs : |b| ≤ 2 :=
    cf_previous_coefficient_bound alpha p q P Q Pm Qm Qn a b
      hq hQ hQ_le_q hq_lt_Qn hpq hqq hdet happrox hconv_cur
  have hb_bounds : -2 ≤ b ∧ b ≤ 2 := abs_le.mp hb_abs
  by_cases hsmall : 2 * q < Qn
  · have hmem : (a, b) ∈ coefficientCandidates aNext := by
      refine (coefficientCandidates_spec a b aNext).mpr ⟨hb_bounds, Or.inl ?_⟩
      by_cases hb0 : b = 0
      · have hp0 : p = a * P := by
          rw [hb0] at hpq
          simpa using hpq
        have hq0 : q = a * Q := by
          rw [hb0] at hqq
          simpa using hqq
        have ha1 : a = 1 :=
          smaller_half_b_zero p q P Q a hq hQ hp0 hq0 hred hcopPQ
        constructor <;> omega
      · have hbstrict : |(b : ℝ)| < 3 * (Q : ℝ) / (2 * (q : ℝ)) + 1 / 2 :=
          b_strict_bound alpha p q P Q Pm Qm Qn a b
            hq hQ hq_lt_Qn hpq hqq hdet happrox hconv_cur hQn hsmall
        exact smaller_half_a_bounds a b q Q Qm
          hq hQ hQm_nonneg hQm_le_Q hQ_le_q hb_abs hb0 hbstrict hqq
    refine ⟨a, b, a - b * aNext, hpq, hqq, rfl, ?_, ?_, hmem⟩
    · rw [hPnext]
      calc
        p = a * P + b * Pm := hpq
        _ = b * (aNext * P + Pm) + (a - b * aNext) * P := by ring
    · rw [hQnext]
      calc
        q = a * Q + b * Qm := hqq
        _ = b * (aNext * Q + Qm) + (a - b * aNext) * Q := by ring
  · have hlarge : Qn ≤ 2 * q := by omega
    have hp_bc : p = b * Pn + (a - b * aNext) * P := by
      rw [hPnext]
      calc
        p = a * P + b * Pm := hpq
        _ = b * (aNext * P + Pm) + (a - b * aNext) * P := by ring
    have hq_bc : q = b * Qn + (a - b * aNext) * Q := by
      rw [hQnext]
      calc
        q = a * Q + b * Qm := hqq
        _ = b * (aNext * Q + Qm) + (a - b * aNext) * Q := by ring
    have hdet_next : |P * Qn - Pn * Q| = 1 := by
      rw [hPnext, hQnext]
      have h : P * (aNext * Q + Qm) - (aNext * P + Pm) * Q =
          P * Qm - Pm * Q := by ring
      rw [h]
      exact hdet
    have hc_bounds : -3 ≤ a - b * aNext ∧ a - b * aNext ≤ 3 :=
      larger_half_c_bounds alpha p q P Q Pn Qn Qn b (a - b * aNext)
        hq hQn hq_lt_Qn hp_bc hq_bc hdet_next happrox hconv_next hQn hlarge
    have hmem : (a, b) ∈ coefficientCandidates aNext := by
      refine (coefficientCandidates_spec a b aNext).mpr
        ⟨hb_bounds, Or.inr ⟨a - b * aNext, hc_bounds.1, hc_bounds.2, ?_⟩⟩
      ring
    refine ⟨a, b, a - b * aNext, hpq, hqq, rfl, hp_bc, hq_bc, hmem⟩

theorem finite_prefix_interval (Q : ℕ → ℕ) (n H q : ℕ) (hn : 0 < n) (hQstrict : ∀ i, i < n → Q i < Q (i + 1)) (hQ0 : Q 0 = 1) (hQn : H ≤ Q n) (hq1 : 1 ≤ q) (hqH : q < H) : ∃ i : ℕ, i < n ∧ Q i ≤ q ∧ q < Q (i + 1) := by
  classical
  let P : Nat → Prop := fun i => q < Q i
  have hex : ∃ i, P i := by
    refine ⟨n, ?_⟩
    change q < Q n
    exact lt_of_lt_of_le hqH hQn
  let m := Nat.find hex
  have hm_spec : P m := by
    simpa [m] using Nat.find_spec hex
  have hm_pos : 0 < m := by
    by_contra h
    have hm0 : m = 0 := by omega
    have hq_lt_one : q < 1 := by
      simpa [P, hm0, hQ0] using hm_spec
    omega
  have hnP : P n := by
    change q < Q n
    exact lt_of_lt_of_le hqH hQn
  have hm_le_n : m ≤ n := by
    simpa [m] using Nat.find_min' hex hnP
  let i := m - 1
  have hi_lt_n : i < n := by
    dsimp [i]
    omega
  have hQi_le_q : Q i ≤ q := by
    by_contra hnot
    have hq_lt_Qi : q < Q i := by omega
    have hi_lt_m : i < m := by
      dsimp [i]
      omega
    have hnotP : ¬ P i := by
      intro hPi
      have hle : m ≤ i := by
        simpa [m] using Nat.find_min' hex hPi
      omega
    exact hnotP (by simpa [P] using hq_lt_Qi)
  have hQm : q < Q m := by
    simpa [P] using hm_spec
  have hQ_succ : q < Q (i + 1) := by
    have hi1 : i + 1 = m := by
      dsimp [i]
      omega
    rw [hi1]
    exact hQm
  have hstrong : ∃ j : Nat, j < n ∧ Q j ≤ q ∧ q < Q (j + 1) ∧ Q j < Q (j + 1) ∧ 0 < n := by
    refine ⟨i, hi_lt_n, hQi_le_q, hQ_succ, ?_, ?_⟩
    exact hQstrict i hi_lt_n
    exact hn
  obtain ⟨j, hj_lt_n, hQj_le_q, hq_lt_Qj1, _, _⟩ := hstrong
  exact ⟨j, hj_lt_n, hQj_le_q, hq_lt_Qj1⟩

#print axioms reduced_approximation_mem_coefficientCandidates
#print axioms finite_prefix_interval

end NestedBinomialV10
