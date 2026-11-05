import Mathlib.Tactic

namespace NestedBinomialV10
theorem unimodular_coordinates (P Q Pm Qm p q : ℤ)
    (hdet : P * Qm - Pm * Q = 1) :
    ∃! ab : ℤ × ℤ, p = ab.1 * P + ab.2 * Pm ∧ q = ab.1 * Q + ab.2 * Qm := by
  have hP : P * Qm - Pm * Q = 1 := hdet
  refine ⟨(p * Qm - q * Pm, q * P - p * Q), ?_, ?_⟩
  · constructor
    · linear_combination (-p) * hP
    · linear_combination (-q) * hP
  · rintro ⟨a, b⟩ ⟨ha, hb⟩
    have h1 : a * (P * Qm - Pm * Q) = p * Qm - q * Pm := by
      calc
        a * (P * Qm - Pm * Q) = (a * P + b * Pm) * Qm - (a * Q + b * Qm) * Pm := by ring
        _ = p * Qm - q * Pm := by rw [ha, hb]
    have h2 : b * (P * Qm - Pm * Q) = q * P - p * Q := by
      calc
        b * (P * Qm - Pm * Q) = (a * Q + b * Qm) * P - (a * P + b * Pm) * Q := by ring
        _ = q * P - p * Q := by rw [ha, hb]
    rw [hP] at h1 h2
    simp only [mul_one] at h1 h2
    ext <;> simp [h1, h2]

theorem unimodular_coordinates_abs (P Q Pm Qm p q : ℤ)
    (hdet : |P * Qm - Pm * Q| = 1) :
    ∃! ab : ℤ × ℤ, p = ab.1 * P + ab.2 * Pm ∧ q = ab.1 * Q + ab.2 * Qm := by
  have hcases : P * Qm - Pm * Q = 1 ∨ P * Qm - Pm * Q = -1 := by
    rcases lt_trichotomy (P * Qm - Pm * Q) 0 with hneg | hzero | hpos
    · right
      have habs : |P * Qm - Pm * Q| = -(P * Qm - Pm * Q) := abs_of_neg hneg
      rw [habs] at hdet
      linarith
    · exfalso
      rw [hzero, abs_zero] at hdet
      exact zero_ne_one hdet
    · left
      have habs : |P * Qm - Pm * Q| = P * Qm - Pm * Q := abs_of_nonneg (le_of_lt hpos)
      rw [habs] at hdet
      exact hdet
  rcases hcases with hplus | hminus
  · exact unimodular_coordinates P Q Pm Qm p q hplus
  · have hswap : Pm * Q - P * Qm = 1 := by linarith
    obtain ⟨⟨a, b⟩, ⟨ha, hb⟩, huniq⟩ := unimodular_coordinates Pm Qm P Q p q hswap
    refine ⟨(b, a), ?_, ?_⟩
    · constructor
      · show p = b * P + a * Pm
        calc p = a * Pm + b * P := ha
          _ = b * P + a * Pm := by ring
      · show q = b * Q + a * Qm
        calc q = a * Qm + b * Q := hb
          _ = b * Q + a * Qm := by ring
    · rintro ⟨x, y⟩ ⟨hx, hy⟩
      have hx' : p = y * Pm + x * P := by
        calc p = x * P + y * Pm := hx
          _ = y * Pm + x * P := by ring
      have hy' : q = y * Qm + x * Q := by
        calc q = x * Q + y * Qm := hy
          _ = y * Qm + x * Q := by ring
      have hpair : (y, x) = (a, b) := huniq (y, x) ⟨hx', hy'⟩
      have hxy : x = b ∧ y = a := by
        injection hpair with h1 h2
        exact ⟨h2, h1⟩
      ext <;> simp [hxy]

theorem real_cross_difference_bound (alpha p q P Q N : ℝ)
    (hq : 0 < q) (hQ : 0 < Q) (hQq : Q ≤ q) (hqN : q < N)
    (happrox : |alpha - p / q| < 3 / (2 * q ^ 2))
    (hconv : |Q * alpha - P| < 1 / N) :
    |p * Q - q * P| < (5 : ℝ) / 2 := by
  have hq2 : (0 : ℝ) < q ^ 2 := by positivity
  have hN : (0 : ℝ) < N := lt_trans hq hqN
  have hqn : q ≠ 0 := ne_of_gt hq
  have hstep1 : q * |alpha - p / q| < 3 / (2 * q) := by
    have h := mul_lt_mul_of_pos_right happrox hq
    have heq : (3 / (2 * q ^ 2)) * q = 3 / (2 * q) := by
      field_simp
    rw [heq] at h
    have hcomm : |alpha - p / q| * q = q * |alpha - p / q| := by ring
    rw [hcomm] at h
    exact h
  have hstep2 : |q * alpha - p| < 3 / (2 * q) := by
    have heq : q * alpha - p = q * (alpha - p / q) := by
      field_simp
    rw [heq, abs_mul, abs_of_pos hq]
    exact hstep1
  have hstep3 : q * |Q * alpha - P| < q / N := by
    have h := mul_lt_mul_of_pos_right hconv hq
    have hcomm : |Q * alpha - P| * q = q * |Q * alpha - P| := by ring
    rw [hcomm] at h
    calc q * |Q * alpha - P| < (1 / N) * q := h
      _ = q / N := by ring
  have hA : Q * |q * alpha - p| < Q * (3 / (2 * q)) := mul_lt_mul_of_pos_left hstep2 hQ
  have hQq' : Q * (3 / (2 * q)) ≤ q * (3 / (2 * q)) := by
    apply mul_le_mul_of_nonneg_right hQq
    positivity
  have hq3 : q * (3 / (2 * q)) = 3 / 2 := by
    field_simp
  have hkey : |p * Q - q * P| < 3 / 2 + q / N := by
    have hdecomp : p * Q - q * P = Q * (p - q * alpha) + q * (Q * alpha - P) := by ring
    have h1 : |Q * (p - q * alpha)| = Q * |q * alpha - p| := by
      have hneg : p - q * alpha = -(q * alpha - p) := by ring
      rw [hneg, abs_mul, abs_of_pos hQ, abs_neg]
    have h2 : |q * (Q * alpha - P)| = q * |Q * alpha - P| := by
      rw [abs_mul, abs_of_pos hq]
    calc |p * Q - q * P| = |Q * (p - q * alpha) + q * (Q * alpha - P)| := by rw [hdecomp]
      _ ≤ |Q * (p - q * alpha)| + |q * (Q * alpha - P)| := abs_add_le _ _
      _ = Q * |q * alpha - p| + q * |Q * alpha - P| := by rw [h1, h2]
      _ < Q * (3 / (2 * q)) + q / N := by linarith [hA, hstep3]
      _ ≤ q * (3 / (2 * q)) + q / N := by linarith [hQq']
      _ = 3 / 2 + q / N := by rw [hq3]
  have hqN' : q / N < 1 := by
    rw [div_lt_one hN]
    exact hqN
  linarith [hkey, hqN']

theorem integer_cross_difference_bound (alpha : ℝ) (p q P Q N : ℤ)
    (hq : 0 < q) (hQ : 0 < Q) (hQq : Q ≤ q) (hqN : q < N)
    (happrox : |alpha - (p : ℝ) / (q : ℝ)| < 3 / (2 * (q : ℝ) ^ 2))
    (hconv : |(Q : ℝ) * alpha - (P : ℝ)| < 1 / (N : ℝ)) :
    |p * Q - q * P| ≤ 2 := by
  have hqR : (0 : ℝ) < (q : ℝ) := by exact_mod_cast hq
  have hQR : (0 : ℝ) < (Q : ℝ) := by exact_mod_cast hQ
  have hQqR : (Q : ℝ) ≤ (q : ℝ) := by exact_mod_cast hQq
  have hqNR : (q : ℝ) < (N : ℝ) := by exact_mod_cast hqN
  have hmain := real_cross_difference_bound (alpha : ℝ) (p : ℝ) (q : ℝ) (P : ℝ) (Q : ℝ) (N : ℝ) hqR hQR hQqR hqNR happrox hconv
  have hcast : ((p * Q - q * P : ℤ) : ℝ) = (p : ℝ) * (Q : ℝ) - (q : ℝ) * (P : ℝ) := by push_cast; ring
  have hcastabs : |((p * Q - q * P : ℤ) : ℝ)| = ((|p * Q - q * P| : ℤ) : ℝ) := by push_cast; rfl
  have hmain' : ((|p * Q - q * P| : ℤ) : ℝ) < (5 : ℝ) / 2 := by
    rw [← hcastabs, hcast]
    exact hmain
  have hlt : ((|p * Q - q * P| : ℤ) : ℝ) < (3 : ℝ) := by linarith
  have hlt3 : |p * Q - q * P| < (3 : ℤ) := by exact_mod_cast hlt
  omega

theorem cf_previous_coefficient_bound (alpha : ℝ) (p q P Q Pm Qm N a b : ℤ)
    (hq : 0 < q) (hQ : 0 < Q) (hQq : Q ≤ q) (hqN : q < N)
    (hpq : p = a * P + b * Pm) (hqq : q = a * Q + b * Qm)
    (hdet : |P * Qm - Pm * Q| = 1)
    (happrox : |alpha - (p : ℝ) / (q : ℝ)| < 3 / (2 * (q : ℝ) ^ 2))
    (hconv : |(Q : ℝ) * alpha - (P : ℝ)| < 1 / (N : ℝ)) : |b| ≤ 2 := by
  have hdet' : |Pm * Q - P * Qm| = 1 := by
    rw [show Pm * Q - P * Qm = -(P * Qm - Pm * Q) by ring, abs_neg]
    exact hdet
  have hid : p * Q - q * P = b * (Pm * Q - P * Qm) := by
    rw [hpq, hqq]; ring
  have hb : |p * Q - q * P| = |b| := by
    rw [hid, abs_mul, hdet']
    ring
  have hcross : |p * Q - q * P| ≤ 2 :=
    integer_cross_difference_bound alpha p q P Q N hq hQ hQq hqN happrox hconv
  rw [hb] at hcross
  exact hcross

#print axioms unimodular_coordinates
#print axioms unimodular_coordinates_abs
#print axioms real_cross_difference_bound
#print axioms integer_cross_difference_bound
#print axioms cf_previous_coefficient_bound

end NestedBinomialV10
