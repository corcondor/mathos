import Mathlib.Tactic
import CFCylinderNesting
import CFAnalyticBounds


namespace NestedBinomialV10
theorem cube_lt_iff_int_cross_mul (P Q : ℤ) (T S : ℕ) (hQ : 0 < Q) (hS : 0 < S) : ((P : ℝ) / (Q : ℝ)) ^ 3 < (T : ℝ) / (6 * (S : ℝ)) ↔ P ^ 3 * (6 * (S : ℤ)) < (T : ℤ) * Q ^ 3 := by
  have hQpos : (0 : ℝ) < (Q : ℝ) := by exact_mod_cast hQ
  have hSpos : (0 : ℝ) < (S : ℝ) := by exact_mod_cast hS
  have h6Spos : (0 : ℝ) < 6 * (S : ℝ) := by
    exact mul_pos (by norm_num) hSpos
  have hQ3pos : (0 : ℝ) < (Q : ℝ) ^ 3 := pow_pos hQpos 3
  have hleft : ((P : ℝ) / (Q : ℝ)) ^ 3 * (6 * (S : ℝ)) =
      ((P : ℝ) ^ 3 * (6 * (S : ℝ))) / (Q : ℝ) ^ 3 := by
    rw [div_pow]
    field_simp [ne_of_gt hQpos, pow_ne_zero 3 (ne_of_gt hQpos)] <;> ring
  constructor
  · intro h
    have h1 : ((P : ℝ) / (Q : ℝ)) ^ 3 * (6 * (S : ℝ)) < (T : ℝ) :=
      (lt_div_iff₀ h6Spos).mp h
    have h2 : ((P : ℝ) ^ 3 * (6 * (S : ℝ))) / (Q : ℝ) ^ 3 < (T : ℝ) := by
      rw [← hleft]
      exact h1
    have hreal : (P : ℝ) ^ 3 * (6 * (S : ℝ)) < (T : ℝ) * (Q : ℝ) ^ 3 :=
      (div_lt_iff₀ hQ3pos).mp h2
    exact_mod_cast hreal
  · intro h
    have hreal : (P : ℝ) ^ 3 * (6 * (S : ℝ)) < (T : ℝ) * (Q : ℝ) ^ 3 := by
      exact_mod_cast h
    have h2 : ((P : ℝ) ^ 3 * (6 * (S : ℝ))) / (Q : ℝ) ^ 3 < (T : ℝ) :=
      (div_lt_iff₀ hQ3pos).mpr hreal
    have h1 : ((P : ℝ) / (Q : ℝ)) ^ 3 * (6 * (S : ℝ)) < (T : ℝ) := by
      rw [hleft]
      exact h2
    exact (lt_div_iff₀ h6Spos).mpr h1

theorem cube_between_implies_hbetween (alpha x y : ℝ) (h : (x ^ 3 - alpha ^ 3) * (y ^ 3 - alpha ^ 3) < 0) : (alpha - x) * (alpha - y) < 0 := by
  have hfac : ∀ t : ℝ, t ^ 3 - alpha ^ 3 =
      (t - alpha) * (t ^ 2 + t * alpha + alpha ^ 2) := by
    intro t
    ring
  have hquad_pos : ∀ t : ℝ, t ≠ alpha →
      0 < t ^ 2 + t * alpha + alpha ^ 2 := by
    intro t ht
    have hrepr : t ^ 2 + t * alpha + alpha ^ 2 =
        (3 / 4 : ℝ) * (t + alpha) ^ 2 + (1 / 4 : ℝ) * (t - alpha) ^ 2 := by
      ring
    rw [hrepr]
    have hsq : 0 < (t - alpha) ^ 2 := by
      exact sq_pos_of_ne_zero (sub_ne_zero.mpr ht)
    have hterm1 : 0 ≤ (3 / 4 : ℝ) * (t + alpha) ^ 2 :=
      mul_nonneg (by norm_num) (sq_nonneg (t + alpha))
    have hterm2 : 0 < (1 / 4 : ℝ) * (t - alpha) ^ 2 :=
      mul_pos (by norm_num) hsq
    linarith
  have hlt_iff : ∀ t : ℝ, t ≠ alpha →
      (t ^ 3 - alpha ^ 3 < 0 ↔ t < alpha) := by
    intro t ht
    constructor
    · intro hneg
      by_contra hnot
      have hle : alpha ≤ t := not_lt.mp hnot
      have hlt : alpha < t := lt_of_le_of_ne hle (Ne.symm ht)
      have hprod : 0 < (t - alpha) * (t ^ 2 + t * alpha + alpha ^ 2) :=
        mul_pos (sub_pos.mpr hlt) (hquad_pos t ht)
      rw [hfac t] at hneg
      linarith
    · intro hlt
      rw [hfac t]
      exact mul_neg_of_neg_of_pos (sub_neg.mpr hlt) (hquad_pos t ht)
  have hpos_iff : ∀ t : ℝ, t ≠ alpha →
      (0 < t ^ 3 - alpha ^ 3 ↔ alpha < t) := by
    intro t ht
    constructor
    · intro hpos
      by_contra hnot
      have hle : t ≤ alpha := not_lt.mp hnot
      have hlt : t < alpha := lt_of_le_of_ne hle ht
      have hprod : (t - alpha) * (t ^ 2 + t * alpha + alpha ^ 2) < 0 :=
        mul_neg_of_neg_of_pos (sub_neg.mpr hlt) (hquad_pos t ht)
      rw [hfac t] at hpos
      linarith
    · intro hgt
      rw [hfac t]
      exact mul_pos (sub_pos.mpr hgt) (hquad_pos t ht)
  have hAB_ne : (x ^ 3 - alpha ^ 3) * (y ^ 3 - alpha ^ 3) ≠ 0 := ne_of_lt h
  have hA_ne : x ^ 3 - alpha ^ 3 ≠ 0 := by
    intro hA
    exact hAB_ne (by simp [hA])
  have hB_ne : y ^ 3 - alpha ^ 3 ≠ 0 := by
    intro hB
    exact hAB_ne (by simp [hB])
  have hx_ne : x ≠ alpha := by
    intro hx
    exact hA_ne (by simp [hx])
  have hy_ne : y ≠ alpha := by
    intro hy
    exact hB_ne (by simp [hy])
  have hA_cases : x ^ 3 - alpha ^ 3 < 0 ∨ 0 < x ^ 3 - alpha ^ 3 :=
    lt_or_gt_of_ne hA_ne
  have hB_cases : y ^ 3 - alpha ^ 3 < 0 ∨ 0 < y ^ 3 - alpha ^ 3 :=
    lt_or_gt_of_ne hB_ne
  rcases hA_cases with hAx | hAx
  · rcases hB_cases with hBy | hBy
    · have hprod : 0 < (x ^ 3 - alpha ^ 3) * (y ^ 3 - alpha ^ 3) :=
        mul_pos_of_neg_of_neg hAx hBy
      linarith
    · have hxlt : x < alpha := (hlt_iff x hx_ne).mp hAx
      have hygt : alpha < y := (hpos_iff y hy_ne).mp hBy
      exact mul_neg_of_pos_of_neg (sub_pos.mpr hxlt) (sub_neg.mpr hygt)
  · rcases hB_cases with hBy | hBy
    · have hxgt : alpha < x := (hpos_iff x hx_ne).mp hAx
      have hylt : y < alpha := (hlt_iff y hy_ne).mp hBy
      exact mul_neg_of_neg_of_pos (sub_neg.mpr hxgt) (sub_pos.mpr hylt)
    · have hprod : 0 < (x ^ 3 - alpha ^ 3) * (y ^ 3 - alpha ^ 3) :=
        mul_pos hAx hBy
      linarith

theorem curve_data_supplies_happrox (S T n r g p q : ℕ) (alpha : ℝ) (hS : 0 < S) (hn : 104 ≤ n) (hr : 3 * n < r) (hcurve : 6 * S * r ^ 3 = T * n * (n - 1) * (n - 2)) (hTlow : 162 * S < T) (hThigh : T < 229 * S) (halpha : alpha ^ 3 = (T : ℝ) / (6 * (S : ℝ))) (hg : 0 < g) (hrg : r = g * p) (hxg : n - 1 = g * q) : 0 < q ∧ 0 < alpha - (p : ℝ) / (q : ℝ) ∧ |alpha - (p : ℝ) / (q : ℝ)| < 3 / (2 * (q : ℝ) ^ 2) := by
  have hn1 : 1 ≤ n := by omega
  have hq_ne : q ≠ 0 := by
    intro hq0
    have hzero : n - 1 = 0 := by
      calc
        n - 1 = g * q := hxg
        _ = g * 0 := by rw [hq0]
        _ = 0 := by rw [mul_zero]
    have hnsub : 0 < n - 1 := by omega
    omega
  have hq : 0 < q := Nat.pos_of_ne_zero hq_ne
  have hcur := NestedBinomialV10.curve_approximation_bound S T n r alpha hS hn hr hcurve hTlow hThigh halpha
  have hcast : ((n - 1 : ℕ) : ℝ) = (n : ℝ) - 1 := by
    rw [Nat.cast_sub hn1]
    norm_num
  have hbound : 0 < alpha - (r : ℝ) / ((n - 1 : ℕ) : ℝ) ∧
      alpha - (r : ℝ) / ((n - 1 : ℕ) : ℝ) <
        3 / (2 * ((n - 1 : ℕ) : ℝ) ^ 2) := by
    simpa [hcast] using hcur
  have hred := NestedBinomialV10.reduced_approximation_bound alpha r (n - 1) g p q hg hq hrg hxg hbound
  exact ⟨hq, hred⟩

theorem curve_data_to_coverage (a : ℕ → ℤ) (ha : ∀ i, 1 ≤ a i) (ha1 : 2 ≤ a 1) (alpha : ℝ) (M : ℕ) (S T n r g p q : ℕ) (hS : 0 < S) (hn : 104 ≤ n) (hr : 3 * n < r) (hcurve : 6 * S * r ^ 3 = T * n * (n - 1) * (n - 2)) (hTlow : 162 * S < T) (hThigh : T < 229 * S) (halpha : alpha ^ 3 = (T : ℝ) / (6 * (S : ℝ))) (hg : 0 < g) (hgeq : g = Nat.gcd r (n - 1)) (hrg : r = g * p) (hxg : n - 1 = g * q) (hbetween : (alpha - ((contsZ a (M + 1)).1 : ℝ) / ((contsZ a (M + 1)).2 : ℝ)) * (alpha - (((contsZ a (M + 1)).1 + (contsZ a M).1 : ℤ) : ℝ) / (((contsZ a (M + 1)).2 + (contsZ a M).2 : ℤ) : ℝ)) < 0) (hqB : (q : ℤ) < (2 : ℤ) ^ (192 * S)) (hBQ : (2 : ℤ) ^ (192 * S) ≤ (contsZ a (M + 1)).2) : ∃ i : ℕ, i < M ∧ (contsZ a (i + 1)).2 ≤ (q : ℤ) ∧ (q : ℤ) < (contsZ a (i + 2)).2 ∧ ∃ a' b c : ℤ, (p : ℤ) = a' * (contsZ a (i + 1)).1 + b * (contsZ a i).1 ∧ (q : ℤ) = a' * (contsZ a (i + 1)).2 + b * (contsZ a i).2 ∧ c = a' - b * a (i + 1) ∧ (p : ℤ) = b * (contsZ a (i + 2)).1 + c * (contsZ a (i + 1)).1 ∧ (q : ℤ) = b * (contsZ a (i + 2)).2 + c * (contsZ a (i + 1)).2 ∧ (a', b) ∈ coefficientCandidates (a (i + 1)) := by
  obtain ⟨hqpos, _, happroxNat⟩ :=
    NestedBinomialV10.curve_data_supplies_happrox S T n r g p q alpha hS hn hr hcurve hTlow hThigh halpha hg hrg hxg
  have hqZ : (0 : ℤ) < (q : ℤ) := by exact_mod_cast hqpos
  have hq_lt : (q : ℤ) < (contsZ a (M + 1)).2 := lt_of_lt_of_le hqB hBQ
  have hgcd : Nat.gcd (g * p) (g * q) = g := by
    rw [← hrg, ← hxg]
    exact hgeq.symm
  have hgd : g * Nat.gcd p q = g := by
    simpa [Nat.gcd_mul_left] using hgcd
  have hgcd1 : Nat.gcd p q = 1 := by
    have hgdR : (g : ℝ) * (Nat.gcd p q : ℝ) = (g : ℝ) := by
      exact_mod_cast hgd
    have hgR : (0 : ℝ) < (g : ℝ) := by exact_mod_cast hg
    have hgne : (g : ℝ) ≠ 0 := ne_of_gt hgR
    have h' : (g : ℝ) * (Nat.gcd p q : ℝ) = (g : ℝ) * 1 := by
      simpa using hgdR
    have hdR : (Nat.gcd p q : ℝ) = 1 := mul_left_cancel₀ hgne h'
    exact_mod_cast hdR
  have hcopNat : Nat.Coprime p q := Nat.coprime_iff_gcd_eq_one.mpr hgcd1
  have hpabs : Int.natAbs (p : ℤ) = p := by simp
  have hqabs : Int.natAbs (q : ℤ) = q := by simp
  have hred : Nat.Coprime (Int.natAbs (p : ℤ)) (Int.natAbs (q : ℤ)) := by
    simpa [hpabs, hqabs] using hcopNat
  have happrox : |alpha - ((p : ℤ) : ℝ) / ((q : ℤ) : ℝ)| < 3 / (2 * ((q : ℤ) : ℝ) ^ 2) := by
    simpa using happroxNat
  obtain ⟨i, hiM, hQle, hq_lt_Q, a', b, c, h1, h2, h3, h4, h5, h6⟩ :=
    NestedBinomialV10.certificate_prefix_coverage a ha ha1 alpha M hbetween (p : ℤ) (q : ℤ) hqZ hq_lt hred happrox
  exact ⟨i, hiM, hQle, hq_lt_Q, a', b, c, h1, h2, h3, h4, h5, h6⟩

#print axioms cube_lt_iff_int_cross_mul
#print axioms cube_between_implies_hbetween
#print axioms curve_data_supplies_happrox
#print axioms curve_data_to_coverage

end NestedBinomialV10
