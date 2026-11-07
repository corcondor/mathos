import Mathlib.Tactic


namespace NestedBinomialV10
theorem alpha_gt_three (S T : ℕ) (alpha : ℝ) (hS : 0 < S) (hT : 162 * S < T) (halpha : alpha ^ 3 = (T : ℝ) / (6 * (S : ℝ))) : 3 < alpha := by
  have hSpos : (0 : ℝ) < (S : ℝ) := by exact_mod_cast hS
  have hTnat : ((162 * S : ℕ) : ℝ) < (T : ℝ) := by exact_mod_cast hT
  have hT' : (162 : ℝ) * (S : ℝ) < (T : ℝ) := by
    simpa using hTnat
  have h6 : (0 : ℝ) < 6 * (S : ℝ) := by
    exact mul_pos (by norm_num) hSpos
  have hratio : (27 : ℝ) < (T : ℝ) / (6 * (S : ℝ)) := by
    rw [lt_div_iff₀ h6]
    nlinarith [hT']
  have hcube : (27 : ℝ) < alpha ^ 3 := by
    rw [halpha]
    exact hratio
  by_contra hle
  have hle' : alpha ≤ 3 := le_of_not_gt hle
  have hquad : 0 ≤ alpha ^ 2 + 3 * alpha + 9 := by
    nlinarith [sq_nonneg (2 * alpha + 3)]
  have hmul : 0 ≤ (3 - alpha) * (alpha ^ 2 + 3 * alpha + 9) := by
    exact mul_nonneg (by linarith) hquad
  have hfactor : (3 - alpha) * (alpha ^ 2 + 3 * alpha + 9) = 27 - alpha ^ 3 := by
    ring
  rw [hfactor] at hmul
  linarith

theorem curve_approximation_bound (S T n r : ℕ) (alpha : ℝ) (hS : 0 < S) (hn : 104 ≤ n) (hr : 3 * n < r) (hcurve : 6 * S * r ^ 3 = T * n * (n - 1) * (n - 2)) (hTlow : 162 * S < T) (hThigh : T < 229 * S) (halpha : alpha ^ 3 = (T : ℝ) / (6 * (S : ℝ))) : 0 < alpha - (r : ℝ) / ((n : ℝ) - 1) ∧ alpha - (r : ℝ) / ((n : ℝ) - 1) < 3 / (2 * ((n : ℝ) - 1) ^ 2) := by
  let x : ℝ := (n : ℝ) - 1
  let y : ℝ := (r : ℝ) / x
  have hnR : (104 : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn
  have hxpos : 0 < x := by
    dsimp [x]
    linarith
  have hxne : x ≠ 0 := ne_of_gt hxpos
  have hx2pos : 0 < x ^ 2 := pow_pos hxpos 2
  have hx2ne : x ^ 2 ≠ 0 := ne_of_gt hx2pos
  have hSpos : (0 : ℝ) < (S : ℝ) := by exact_mod_cast hS
  have h6Spos : 0 < 6 * (S : ℝ) := mul_pos (by norm_num) hSpos
  have h6Sne : 6 * (S : ℝ) ≠ 0 := ne_of_gt h6Spos
  have hThighR : (T : ℝ) < 229 * (S : ℝ) := by exact_mod_cast hThigh
  have hrR : (3 : ℝ) * (n : ℝ) < (r : ℝ) := by exact_mod_cast hr
  have hy_gt3 : 3 < y := by
    dsimp [y]
    rw [lt_div_iff₀ hxpos]
    dsimp [x]
    linarith only [hrR, hnR]
  have halpha_gt3 : 3 < alpha := alpha_gt_three S T alpha hS hTlow halpha
  have halpha3_lt : alpha ^ 3 < (81 : ℝ) / 2 := by
    rw [halpha]
    rw [div_lt_iff₀ h6Spos]
    have h : (81 : ℝ) / 2 * (6 * (S : ℝ)) = 243 * (S : ℝ) := by ring
    rw [h]
    nlinarith [hThighR, hSpos]
  have hn1 : 1 ≤ n := by omega
  have hn2 : 2 ≤ n := by omega
  have hcast1 : ((n - 1 : ℕ) : ℝ) = (n : ℝ) - 1 := by
    rw [Nat.cast_sub hn1]
    norm_num
  have hcast2 : ((n - 2 : ℕ) : ℝ) = (n : ℝ) - 2 := by
    rw [Nat.cast_sub hn2]
    norm_num
  have hcurveR : 6 * (S : ℝ) * (r : ℝ) ^ 3 =
      (T : ℝ) * (n : ℝ) * x * ((n : ℝ) - 2) := by
    have h1 : ((6 * S * r ^ 3 : ℕ) : ℝ) = ((T * n * (n - 1) * (n - 2) : ℕ) : ℝ) := by
      exact_mod_cast hcurve
    push_cast at h1
    rw [hcast1, hcast2] at h1
    dsimp only [x]
    exact h1
  have hr3 : (r : ℝ) ^ 3 = (T : ℝ) * (n : ℝ) * x * ((n : ℝ) - 2) / (6 * (S : ℝ)) := by
    rw [eq_div_iff h6Sne]
    rw [mul_comm ((r : ℝ) ^ 3) (6 * (S : ℝ))]
    exact hcurveR
  have hy3a : y ^ 3 = alpha ^ 3 * (((n : ℝ) * ((n : ℝ) - 2)) / x ^ 2) := by
    calc
      y ^ 3 = (r : ℝ) ^ 3 / x ^ 3 := by
        dsimp [y]
        rw [div_pow]
      _ = ((T : ℝ) * (n : ℝ) * x * ((n : ℝ) - 2) / (6 * (S : ℝ))) / x ^ 3 := by
        rw [hr3]
      _ = (T : ℝ) / (6 * (S : ℝ)) * (((n : ℝ) * ((n : ℝ) - 2)) / x ^ 2) := by
        field_simp [h6Sne, hxne, hx2ne, pow_ne_zero 3 hxne] <;> ring
      _ = alpha ^ 3 * (((n : ℝ) * ((n : ℝ) - 2)) / x ^ 2) := by
        rw [halpha]
  have hnn : (n : ℝ) * ((n : ℝ) - 2) = x ^ 2 - 1 := by
    dsimp [x]
    ring
  have hy3' : y ^ 3 = alpha ^ 3 * (1 - 1 / x ^ 2) := by
    rw [hy3a, hnn]
    congr 1
    field_simp [hx2ne] <;> ring
  have hnum : alpha ^ 3 - y ^ 3 = alpha ^ 3 / x ^ 2 := by
    rw [hy3']
    field_simp [hx2ne] <;> ring
  have analytic : ∀ (x y alpha : ℝ), 0 < x → 3 < alpha → 3 < y →
      alpha ^ 3 - y ^ 3 = alpha ^ 3 / x ^ 2 → alpha ^ 3 < (81 : ℝ) / 2 →
      0 < alpha - y ∧ alpha - y < 3 / (2 * x ^ 2) := by
    intro x y alpha hx ha hy hnum ha3
    have hx2pos : 0 < x ^ 2 := pow_pos hx 2
    have hx2ne : x ^ 2 ≠ 0 := ne_of_gt hx2pos
    have ha_pos : 0 < alpha := by linarith
    have hy_pos : 0 < y := by linarith
    have hcube_lt : y ^ 3 < alpha ^ 3 := by
      have hpos : 0 < alpha ^ 3 / x ^ 2 := div_pos (pow_pos ha_pos 3) hx2pos
      linarith [hnum]
    have hdiff_pos : 0 < alpha - y := by
      by_contra h
      have hy_le : alpha ≤ y := by linarith
      have hle : alpha ^ 3 ≤ y ^ 3 := pow_le_pow_left₀ (le_of_lt ha_pos) hy_le 3
      linarith
    have hden_gt : 27 < alpha ^ 2 + alpha * y + y ^ 2 := by
      have ha2 : 9 < alpha ^ 2 := by
        have h1 : 0 < alpha - 3 := by linarith
        have h2 : 0 < alpha + 3 := by linarith
        have hprod : 0 < (alpha - 3) * (alpha + 3) := mul_pos h1 h2
        nlinarith only [hprod]
      have hy2 : 9 < y ^ 2 := by
        have h1 : 0 < y - 3 := by linarith
        have h2 : 0 < y + 3 := by linarith
        have hprod : 0 < (y - 3) * (y + 3) := mul_pos h1 h2
        nlinarith only [hprod]
      have hay : 9 < alpha * y := by
        have h1 : 0 < alpha - 3 := by linarith
        have h2 : 0 < y - 3 := by linarith
        have hprod : 0 < (alpha - 3) * (y - 3) := mul_pos h1 h2
        nlinarith only [hprod, ha, hy]
      linarith only [ha2, hy2, hay]
    have hDpos : 0 < alpha ^ 2 + alpha * y + y ^ 2 := by linarith
    have hprod : (alpha - y) * (alpha ^ 2 + alpha * y + y ^ 2) = alpha ^ 3 - y ^ 3 := by ring
    set N : ℝ := alpha ^ 3 / x ^ 2 with hNdef
    have hnumN : alpha ^ 3 - y ^ 3 = N := by
      rw [hNdef]
      exact hnum
    have hdiff_eq : alpha - y = N / (alpha ^ 2 + alpha * y + y ^ 2) := by
      rw [eq_div_iff (ne_of_gt hDpos)]
      exact hprod.trans hnumN
    have hN_lt : N < (3 / (2 * x ^ 2)) * (alpha ^ 2 + alpha * y + y ^ 2) := by
      rw [hNdef]
      rw [div_lt_iff₀ hx2pos]
      have hrhs : (3 / (2 * x ^ 2)) * (alpha ^ 2 + alpha * y + y ^ 2) * x ^ 2 =
          (3 / 2) * (alpha ^ 2 + alpha * y + y ^ 2) := by
        field_simp [hx2ne] <;> ring
      rw [hrhs]
      nlinarith [ha3, hden_gt]
    have hupper : alpha - y < 3 / (2 * x ^ 2) := by
      rw [hdiff_eq]
      rw [div_lt_iff₀ hDpos]
      exact hN_lt
    exact ⟨hdiff_pos, hupper⟩
  have hmain := analytic x y alpha hxpos halpha_gt3 hy_gt3 hnum halpha3_lt
  constructor
  · dsimp only [y, x] at hmain ⊢
    exact hmain.1
  · dsimp only [y, x] at hmain ⊢
    exact hmain.2

theorem reduced_approximation_bound (alpha : ℝ) (r x g p q : ℕ) (hg : 0 < g) (hq : 0 < q) (hr : r = g * p) (hx : x = g * q) (hbound : 0 < alpha - (r : ℝ) / (x : ℝ) ∧ alpha - (r : ℝ) / (x : ℝ) < 3 / (2 * (x : ℝ) ^ 2)) : 0 < alpha - (p : ℝ) / (q : ℝ) ∧ |alpha - (p : ℝ) / (q : ℝ)| < 3 / (2 * (q : ℝ) ^ 2) := by
  have hgR : (0 : ℝ) < (g : ℝ) := by exact_mod_cast hg
  have hqR : (0 : ℝ) < (q : ℝ) := by exact_mod_cast hq
  have hxR : (x : ℝ) = (g : ℝ) * (q : ℝ) := by
    rw [hx, Nat.cast_mul]
  have hrR : (r : ℝ) = (g : ℝ) * (p : ℝ) := by
    rw [hr, Nat.cast_mul]
  have hgq_ne : (g : ℝ) * (q : ℝ) ≠ 0 := mul_ne_zero (ne_of_gt hgR) (ne_of_gt hqR)
  have hratio : (r : ℝ) / (x : ℝ) = (p : ℝ) / (q : ℝ) := by
    rw [hrR, hxR]
    field_simp [ne_of_gt hgR, ne_of_gt hqR, hgq_ne] <;> ring
  have hpos : 0 < alpha - (p : ℝ) / (q : ℝ) := by
    rw [← hratio]
    exact hbound.1
  have hxposR : 0 < (x : ℝ) := by
    rw [hxR]
    exact mul_pos hgR hqR
  have hg1_nat : 1 ≤ g := Nat.succ_le_of_lt hg
  have hg1 : (1 : ℝ) ≤ (g : ℝ) := by exact_mod_cast hg1_nat
  have hx_ge_q : (q : ℝ) ≤ (x : ℝ) := by
    rw [hxR]
    have hmul : (1 : ℝ) * (q : ℝ) ≤ (g : ℝ) * (q : ℝ) :=
      mul_le_mul_of_nonneg_right hg1 (le_of_lt hqR)
    simpa using hmul
  have hsq : (q : ℝ) ^ 2 ≤ (x : ℝ) ^ 2 := by
    exact pow_le_pow_left₀ (le_of_lt hqR) hx_ge_q 2
  have hq2pos : 0 < (q : ℝ) ^ 2 := pow_pos hqR 2
  have hle : 3 / (2 * (x : ℝ) ^ 2) ≤ 3 / (2 * (q : ℝ) ^ 2) := by
    have hApos : 0 < 2 * (x : ℝ) ^ 2 := by
      exact mul_pos (by norm_num) (pow_pos hxposR 2)
    have hBpos : 0 < 2 * (q : ℝ) ^ 2 := by
      exact mul_pos (by norm_num) hq2pos
    rw [div_le_iff₀ hApos]
    have hrew : (3 / (2 * (q : ℝ) ^ 2)) * (2 * (x : ℝ) ^ 2) =
        (3 * (2 * (x : ℝ) ^ 2)) / (2 * (q : ℝ) ^ 2) := by
      field_simp [ne_of_gt hBpos] <;> ring
    rw [hrew]
    rw [le_div_iff₀ hBpos]
    nlinarith [hsq]
  have hupper : alpha - (p : ℝ) / (q : ℝ) < 3 / (2 * (q : ℝ) ^ 2) := by
    have h1 : alpha - (p : ℝ) / (q : ℝ) < 3 / (2 * (x : ℝ) ^ 2) := by
      rw [← hratio]
      exact hbound.2
    exact lt_of_lt_of_le h1 hle
  constructor
  · exact hpos
  · rw [abs_of_pos hpos]
    exact hupper

#print axioms alpha_gt_three
#print axioms curve_approximation_bound
#print axioms reduced_approximation_bound

end NestedBinomialV10
