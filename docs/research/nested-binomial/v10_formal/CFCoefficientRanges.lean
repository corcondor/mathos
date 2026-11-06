import Mathlib.Tactic
import CFApproximationCore
def coefficientCandidates (aNext : ℤ) : Finset (ℤ × ℤ) := ((Finset.Icc (-1 : ℤ) 4).product (Finset.Icc (-2 : ℤ) 2)) ∪ (((Finset.Icc (-2 : ℤ) 2).product (Finset.Icc (-3 : ℤ) 3)).image (fun p : ℤ × ℤ => (p.1 * aNext + p.2, p.1)))

namespace NestedBinomialV10
theorem b_strict_bound (alpha : ℝ) (p q P Q Pm Qm N a b : ℤ) (hq : 0 < q) (hQ : 0 < Q) (hqN : q < N) (hpq : p = a * P + b * Pm) (hqq : q = a * Q + b * Qm) (hdet : |P * Qm - Pm * Q| = 1) (happrox : |alpha - (p : ℝ) / (q : ℝ)| < 3 / (2 * (q : ℝ) ^ 2)) (hconv : |(Q : ℝ) * alpha - (P : ℝ)| < 1 / (N : ℝ)) (hNpos : 0 < N) (hqNhalf : 2 * q < N) : |(b : ℝ)| < 3 * (Q : ℝ) / (2 * (q : ℝ)) + 1 / 2 := by
  have hqR : (0 : ℝ) < (q : ℝ) := by exact_mod_cast hq
  have hQR : (0 : ℝ) < (Q : ℝ) := by exact_mod_cast hQ
  have hNR : (0 : ℝ) < (N : ℝ) := by exact_mod_cast hNpos
  have hqNR : (q : ℝ) < (N : ℝ) := by exact_mod_cast hqN
  have hqne : (q : ℝ) ≠ 0 := ne_of_gt hqR
  have hqNhalfR : (2 : ℝ) * (q : ℝ) < (N : ℝ) := by exact_mod_cast hqNhalf
  have hqdivN : (q : ℝ) / (N : ℝ) < 1 / 2 := by
    rw [div_lt_iff₀ hNR]
    linarith [hqNhalfR, hqNR]
  have hdetneg : |Pm * Q - P * Qm| = (1 : ℤ) := by
    rw [show Pm * Q - P * Qm = -(P * Qm - Pm * Q) by ring, abs_neg, hdet]
  have hid : p * Q - q * P = b * (Pm * Q - P * Qm) := by
    rw [hpq, hqq]
    ring
  have hbabs_int : |p * Q - q * P| = |b| := by
    rw [hid, abs_mul, hdetneg, mul_one]
  have hbabs_real : |(b : ℝ)| = |((p * Q - q * P : ℤ) : ℝ)| := by
    calc
      |(b : ℝ)| = ((|b| : ℤ) : ℝ) := by rw [Int.cast_abs]
      _ = ((|p * Q - q * P| : ℤ) : ℝ) := by rw [hbabs_int]
      _ = |((p * Q - q * P : ℤ) : ℝ)| := by rw [Int.cast_abs]
  have hcross : |((p * Q - q * P : ℤ) : ℝ)| <
      3 * (Q : ℝ) / (2 * (q : ℝ)) + 1 / 2 := by
    have hcast : ((p * Q - q * P : ℤ) : ℝ) =
        (p : ℝ) * (Q : ℝ) - (q : ℝ) * (P : ℝ) := by
      push_cast
      ring
    rw [hcast]
    have hdecomp : (p : ℝ) * (Q : ℝ) - (q : ℝ) * (P : ℝ) =
        (Q : ℝ) * ((p : ℝ) - (q : ℝ) * alpha) +
          (q : ℝ) * ((Q : ℝ) * alpha - (P : ℝ)) := by
      ring
    rw [hdecomp]
    have hstep2 : |(q : ℝ) * alpha - (p : ℝ)| < 3 / (2 * (q : ℝ)) := by
      have h := mul_lt_mul_of_pos_left happrox hqR
      have hleft : (q : ℝ) * |alpha - (p : ℝ) / (q : ℝ)| =
          |(q : ℝ) * alpha - (p : ℝ)| := by
        have hqexpr : (q : ℝ) * alpha - (p : ℝ) =
            (q : ℝ) * (alpha - (p : ℝ) / (q : ℝ)) := by
          field_simp [hqne]
        rw [hqexpr, abs_mul, abs_of_pos hqR]
      have hright : (q : ℝ) * (3 / (2 * (q : ℝ) ^ 2)) =
          3 / (2 * (q : ℝ)) := by
        field_simp [hqne]
      rwa [hleft, hright] at h
    have hterm1 : (Q : ℝ) * |(q : ℝ) * alpha - (p : ℝ)| <
        3 * (Q : ℝ) / (2 * (q : ℝ)) := by
      have h := mul_lt_mul_of_pos_left hstep2 hQR
      have hright : (Q : ℝ) * (3 / (2 * (q : ℝ))) =
          3 * (Q : ℝ) / (2 * (q : ℝ)) := by ring
      rwa [hright] at h
    have hterm2 : (q : ℝ) * |(Q : ℝ) * alpha - (P : ℝ)| < 1 / 2 := by
      have h := mul_lt_mul_of_pos_left hconv hqR
      have hright : (q : ℝ) * (1 / (N : ℝ)) = (q : ℝ) / (N : ℝ) := by ring
      rw [hright] at h
      linarith [hqdivN]
    have h1 : |(Q : ℝ) * ((p : ℝ) - (q : ℝ) * alpha)| =
        (Q : ℝ) * |(q : ℝ) * alpha - (p : ℝ)| := by
      have hneg : (p : ℝ) - (q : ℝ) * alpha =
          -((q : ℝ) * alpha - (p : ℝ)) := by ring
      rw [hneg, abs_mul, abs_of_pos hQR, abs_neg]
    have h2 : |(q : ℝ) * ((Q : ℝ) * alpha - (P : ℝ))| =
        (q : ℝ) * |(Q : ℝ) * alpha - (P : ℝ)| := by
      rw [abs_mul, abs_of_pos hqR]
    calc
      |(Q : ℝ) * ((p : ℝ) - (q : ℝ) * alpha) +
          (q : ℝ) * ((Q : ℝ) * alpha - (P : ℝ))|
          ≤ |(Q : ℝ) * ((p : ℝ) - (q : ℝ) * alpha)| +
            |(q : ℝ) * ((Q : ℝ) * alpha - (P : ℝ))| := abs_add_le _ _
      _ = (Q : ℝ) * |(q : ℝ) * alpha - (p : ℝ)| +
            (q : ℝ) * |(Q : ℝ) * alpha - (P : ℝ)| := by rw [h1, h2]
      _ < 3 * (Q : ℝ) / (2 * (q : ℝ)) + 1 / 2 := by
        linarith [hterm1, hterm2]
  rw [hbabs_real]
  exact hcross

theorem smaller_half_a_bounds (a b q Qm Qm1 : ℤ) (hq : 0 < q) (hQm : 0 < Qm) (hQm1_nonneg : 0 ≤ Qm1) (hQm1_le : Qm1 ≤ Qm) (hq_ge : Qm ≤ q) (hb_abs : |b| ≤ 2) (hb_ne : b ≠ 0) (hb_strict : |(b : ℝ)| < 3 * (Qm : ℝ) / (2 * (q : ℝ)) + 1 / 2) (hq_eq : q = a * Qm + b * Qm1) : -1 ≤ a ∧ a ≤ 4 := by
  have hb_abs_pos : 0 < |b| := abs_pos.mpr hb_ne
  have hb_abs_ge_one : (1 : ℤ) ≤ |b| := by omega
  have hbR_ge_one : (1 : ℝ) ≤ |(b : ℝ)| := by
    rw [← Int.cast_abs]
    exact_mod_cast hb_abs_ge_one
  have hqR : (0 : ℝ) < (q : ℝ) := by exact_mod_cast hq
  have hhalf : (1 : ℝ) / 2 < 3 * (Qm : ℝ) / (2 * (q : ℝ)) := by
    linarith [hb_strict, hbR_ge_one]
  have hq_lt_three : (q : ℝ) < 3 * (Qm : ℝ) := by
    have hpos : (0 : ℝ) < 2 * (q : ℝ) := by positivity
    have hmul := mul_lt_mul_of_pos_right hhalf hpos
    have hleft : (1 / 2 : ℝ) * (2 * (q : ℝ)) = (q : ℝ) := by ring
    have hright : (3 * (Qm : ℝ) / (2 * (q : ℝ))) * (2 * (q : ℝ)) = 3 * (Qm : ℝ) := by
      rw [div_mul_cancel₀ _ (by positivity)]
    rw [hleft, hright] at hmul
    exact hmul
  have hq_lt_Qm : q < 3 * Qm := by exact_mod_cast hq_lt_three
  have hb_lower : -2 ≤ b := (abs_le.mp hb_abs).1
  have hb_upper : b ≤ 2 := (abs_le.mp hb_abs).2
  have hbQm1_lower : -2 * Qm ≤ b * Qm1 := by
    have h1 : -2 * Qm1 ≤ b * Qm1 := mul_le_mul_of_nonneg_right hb_lower hQm1_nonneg
    have h2 : -2 * Qm ≤ -2 * Qm1 := by linarith [hQm1_le]
    linarith
  have hbQm1_upper : b * Qm1 ≤ 2 * Qm := by
    have h1 : b * Qm1 ≤ 2 * Qm1 := mul_le_mul_of_nonneg_right hb_upper hQm1_nonneg
    have h2 : 2 * Qm1 ≤ 2 * Qm := by linarith [hQm1_le]
    linarith
  have hq_ge_expr : Qm ≤ a * Qm + b * Qm1 := by
    simpa [hq_eq] using hq_ge
  have hq_lt_expr : a * Qm + b * Qm1 < 3 * Qm := by
    simpa [hq_eq] using hq_lt_Qm
  have hle1 : Qm ≤ a * Qm + 2 * Qm := by
    linarith [hq_ge_expr, hbQm1_upper]
  have hle1' : (1 : ℤ) * Qm ≤ (a + 2) * Qm := by
    calc
      (1 : ℤ) * Qm = Qm := by ring
      _ ≤ a * Qm + 2 * Qm := hle1
      _ = (a + 2) * Qm := by ring
  have hle1'' : (1 : ℤ) ≤ a + 2 := by
    by_contra hcon
    have hcon' : a + 2 ≤ 0 := by omega
    have hmul : (a + 2) * Qm ≤ 0 * Qm := mul_le_mul_of_nonneg_right hcon' (le_of_lt hQm)
    have hzero : (0 : ℤ) * Qm = 0 := by ring
    rw [hzero] at hmul
    linarith [hle1', hmul]
  have hlt1 : a * Qm - 2 * Qm < 3 * Qm := by
    linarith [hq_lt_expr, hbQm1_lower]
  have hlt1' : (a - 2) * Qm < (3 : ℤ) * Qm := by
    calc
      (a - 2) * Qm = a * Qm - 2 * Qm := by ring
      _ < 3 * Qm := hlt1
  have hlt1'' : a - 2 < 3 := by
    by_contra hcon
    have hcon' : (3 : ℤ) ≤ a - 2 := not_lt.mp hcon
    have hmul : (3 : ℤ) * Qm ≤ (a - 2) * Qm := mul_le_mul_of_nonneg_right hcon' (le_of_lt hQm)
    linarith [hlt1', hmul]
  constructor <;> omega

theorem smaller_half_b_zero (p q Pm Qm a : ℤ) (hq : 0 < q) (hQm : 0 < Qm) (hpq : p = a * Pm) (hqq : q = a * Qm) (hred : Nat.Coprime (Int.natAbs p) (Int.natAbs q)) (hcop : Nat.Coprime (Int.natAbs Pm) (Int.natAbs Qm)) : a = 1 := by
  have hq' : 0 < a * Qm := by simpa [hqq] using hq
  have ha_pos : 0 < a := (mul_pos_iff_of_pos_right hQm).mp hq'
  have hp_abs : Int.natAbs p = Int.natAbs a * Int.natAbs Pm := by
    rw [hpq, Int.natAbs_mul]
  have hq_abs : Int.natAbs q = Int.natAbs a * Int.natAbs Qm := by
    rw [hqq, Int.natAbs_mul]
  have hgcd :
      Nat.gcd (Int.natAbs a * Int.natAbs Pm) (Int.natAbs a * Int.natAbs Qm) = 1 := by
    rw [← hp_abs, ← hq_abs]
    exact hred
  have hcop_gcd : Nat.gcd (Int.natAbs Pm) (Int.natAbs Qm) = 1 := hcop
  have ha1 : Int.natAbs a = 1 := by
    rw [Nat.gcd_mul_left, hcop_gcd, Nat.mul_one] at hgcd
    exact hgcd
  have hnonneg : (0 : ℤ) ≤ a := le_of_lt ha_pos
  have hcast : (Int.natAbs a : ℤ) = a := by
    rw [Int.natAbs_of_nonneg hnonneg]
  rw [ha1] at hcast
  omega

theorem larger_half_c_bounds (alpha : ℝ) (p q P Q Pn Qn N b c : ℤ) (hq : 0 < q) (hQn : 0 < Qn) (hqN : q < N) (hpq : p = b * Pn + c * P) (hqq : q = b * Qn + c * Q) (hdet : |P * Qn - Pn * Q| = 1) (happrox : |alpha - (p : ℝ) / (q : ℝ)| < 3 / (2 * (q : ℝ) ^ 2)) (hconv : |(Qn : ℝ) * alpha - (Pn : ℝ)| < 1 / (N : ℝ)) (hNpos : 0 < N) (hq_ge_half : Qn ≤ 2 * q) : -3 ≤ c ∧ c ≤ 3 := by
  have hqR : (0 : ℝ) < (q : ℝ) := by exact_mod_cast hq
  have hQnR : (0 : ℝ) < (Qn : ℝ) := by exact_mod_cast hQn
  have hNR : (0 : ℝ) < (N : ℝ) := by exact_mod_cast hNpos
  have hqNR : (q : ℝ) < (N : ℝ) := by exact_mod_cast hqN
  have hqne : (q : ℝ) ≠ 0 := ne_of_gt hqR
  have hQn_le : (Qn : ℝ) ≤ 2 * (q : ℝ) := by exact_mod_cast hq_ge_half
  have hqdivN : (q : ℝ) / (N : ℝ) < 1 := by
    rw [div_lt_iff₀ hNR]
    linarith [hqNR]
  have hid : p * Qn - q * Pn = c * (P * Qn - Pn * Q) := by
    rw [hpq, hqq]
    ring
  have hcabs_int : |p * Qn - q * Pn| = |c| := by
    rw [hid, abs_mul, hdet, mul_one]
  have hcabs_real_eq : |(c : ℝ)| = |((p * Qn - q * Pn : ℤ) : ℝ)| := by
    calc
      |(c : ℝ)| = ((|c| : ℤ) : ℝ) := by rw [Int.cast_abs]
      _ = ((|p * Qn - q * Pn| : ℤ) : ℝ) := by rw [hcabs_int]
      _ = |((p * Qn - q * Pn : ℤ) : ℝ)| := by rw [Int.cast_abs]
  have hstep2 : |(q : ℝ) * alpha - (p : ℝ)| < 3 / (2 * (q : ℝ)) := by
    have h := mul_lt_mul_of_pos_left happrox hqR
    have hleft : (q : ℝ) * |alpha - (p : ℝ) / (q : ℝ)| =
        |(q : ℝ) * alpha - (p : ℝ)| := by
      have hqexpr : (q : ℝ) * alpha - (p : ℝ) =
          (q : ℝ) * (alpha - (p : ℝ) / (q : ℝ)) := by
        field_simp [hqne]
      rw [hqexpr, abs_mul, abs_of_pos hqR]
    have hright : (q : ℝ) * (3 / (2 * (q : ℝ) ^ 2)) =
        3 / (2 * (q : ℝ)) := by
      field_simp [hqne]
    rwa [hleft, hright] at h
  have hterm1 : (Qn : ℝ) * |(q : ℝ) * alpha - (p : ℝ)| <
      3 * (Qn : ℝ) / (2 * (q : ℝ)) := by
    have h := mul_lt_mul_of_pos_left hstep2 hQnR
    have hright : (Qn : ℝ) * (3 / (2 * (q : ℝ))) =
        3 * (Qn : ℝ) / (2 * (q : ℝ)) := by ring
    rwa [hright] at h
  have hterm2 : (q : ℝ) * |(Qn : ℝ) * alpha - (Pn : ℝ)| < 1 := by
    have h := mul_lt_mul_of_pos_left hconv hqR
    have hright : (q : ℝ) * (1 / (N : ℝ)) = (q : ℝ) / (N : ℝ) := by ring
    rw [hright] at h
    linarith [h, hqdivN]
  have hfirst_le : 3 * (Qn : ℝ) / (2 * (q : ℝ)) ≤ 3 := by
    rw [div_le_iff₀ (by positivity : (0 : ℝ) < 2 * (q : ℝ))]
    nlinarith [hQn_le]
  have h1 : |(Qn : ℝ) * ((p : ℝ) - (q : ℝ) * alpha)| =
      (Qn : ℝ) * |(q : ℝ) * alpha - (p : ℝ)| := by
    have hneg : (p : ℝ) - (q : ℝ) * alpha =
        -((q : ℝ) * alpha - (p : ℝ)) := by ring
    rw [hneg, abs_mul, abs_of_pos hQnR, abs_neg]
  have h2 : |(q : ℝ) * ((Qn : ℝ) * alpha - (Pn : ℝ))| =
      (q : ℝ) * |(Qn : ℝ) * alpha - (Pn : ℝ)| := by
    rw [abs_mul, abs_of_pos hqR]
  have hcross : |((p * Qn - q * Pn : ℤ) : ℝ)| < 4 := by
    have hcast : ((p * Qn - q * Pn : ℤ) : ℝ) =
        (p : ℝ) * (Qn : ℝ) - (q : ℝ) * (Pn : ℝ) := by
      push_cast
      ring
    rw [hcast]
    have hdecomp : (p : ℝ) * (Qn : ℝ) - (q : ℝ) * (Pn : ℝ) =
        (Qn : ℝ) * ((p : ℝ) - (q : ℝ) * alpha) +
          (q : ℝ) * ((Qn : ℝ) * alpha - (Pn : ℝ)) := by
      ring
    rw [hdecomp]
    calc
      |(Qn : ℝ) * ((p : ℝ) - (q : ℝ) * alpha) +
          (q : ℝ) * ((Qn : ℝ) * alpha - (Pn : ℝ))|
          ≤ |(Qn : ℝ) * ((p : ℝ) - (q : ℝ) * alpha)| +
            |(q : ℝ) * ((Qn : ℝ) * alpha - (Pn : ℝ))| := abs_add_le _ _
      _ = (Qn : ℝ) * |(q : ℝ) * alpha - (p : ℝ)| +
            (q : ℝ) * |(Qn : ℝ) * alpha - (Pn : ℝ)| := by rw [h1, h2]
      _ < 4 := by linarith [hterm1, hterm2, hfirst_le]
  have hcabs_real_lt : |(c : ℝ)| < 4 := by
    rw [hcabs_real_eq]
    exact hcross
  have hc_abs_int_real : ((|c| : ℤ) : ℝ) < (4 : ℝ) := by
    rw [Int.cast_abs]
    exact hcabs_real_lt
  have hc_abs_lt_int : |c| < (4 : ℤ) := by
    exact_mod_cast hc_abs_int_real
  have hc_lt : -4 < c ∧ c < 4 := by
    exact abs_lt.mp hc_abs_lt_int
  constructor <;> omega

theorem coefficientCandidates_spec (a b aNext : ℤ) : (a, b) ∈ coefficientCandidates aNext ↔ (-2 ≤ b ∧ b ≤ 2) ∧ ((-1 ≤ a ∧ a ≤ 4) ∨ ∃ c : ℤ, -3 ≤ c ∧ c ≤ 3 ∧ a = b * aNext + c) := by
  constructor
  · intro h
    unfold coefficientCandidates at h
    rcases Finset.mem_union.mp h with h1 | h2
    · obtain ⟨ha, hb⟩ := Finset.mem_product.mp h1
      obtain ⟨ha1, ha2⟩ := Finset.mem_Icc.mp ha
      obtain ⟨hb1, hb2⟩ := Finset.mem_Icc.mp hb
      exact ⟨⟨hb1, hb2⟩, Or.inl ⟨ha1, ha2⟩⟩
    · obtain ⟨p, hp, hpeq⟩ := Finset.mem_image.mp h2
      obtain ⟨hp1, hp2⟩ := Finset.mem_product.mp hp
      obtain ⟨hp11, hp12⟩ := Finset.mem_Icc.mp hp1
      obtain ⟨hp21, hp22⟩ := Finset.mem_Icc.mp hp2
      change (p.1 * aNext + p.2, p.1) = (a, b) at hpeq
      injection hpeq with hx hy
      rw [hy] at hp11 hp12
      exact ⟨⟨hp11, hp12⟩, Or.inr ⟨p.2, hp21, hp22, by rw [← hx, hy]⟩⟩
  · rintro ⟨hb, h1 | h2⟩
    · unfold coefficientCandidates
      exact Finset.mem_union.mpr (Or.inl (Finset.mem_product.mpr ⟨Finset.mem_Icc.mpr h1, Finset.mem_Icc.mpr hb⟩))
    · obtain ⟨c, hc1, hc2, haeq⟩ := h2
      unfold coefficientCandidates
      refine Finset.mem_union.mpr (Or.inr ?_)
      refine Finset.mem_image.mpr ⟨(b, c), ?_, ?_⟩
      · exact Finset.mem_product.mpr ⟨Finset.mem_Icc.mpr hb, Finset.mem_Icc.mpr ⟨hc1, hc2⟩⟩
      · change (b * aNext + c, b) = (a, b)
        rw [← haeq]

theorem coefficientCandidates_card_le (aNext : ℤ) : (coefficientCandidates aNext).card ≤ 65 := by
  unfold coefficientCandidates
  let A : Finset (ℤ × ℤ) := (Finset.Icc (-1 : ℤ) 4).product (Finset.Icc (-2 : ℤ) 2)
  let B : Finset (ℤ × ℤ) := ((Finset.Icc (-2 : ℤ) 2).product (Finset.Icc (-3 : ℤ) 3)).image (fun p : ℤ × ℤ => (p.1 * aNext + p.2, p.1))
  change (A ∪ B).card ≤ 65
  have h1 : (Finset.Icc (-1 : ℤ) 4).card ≤ 6 := by
    have hsub : Finset.Icc (-1 : ℤ) 4 ⊆ ({-1, 0, 1, 2, 3, 4} : Finset ℤ) := by
      intro x hx
      obtain ⟨hx1, hx2⟩ := Finset.mem_Icc.mp hx
      interval_cases x <;> decide
    calc
      (Finset.Icc (-1 : ℤ) 4).card ≤ ({-1, 0, 1, 2, 3, 4} : Finset ℤ).card := Finset.card_le_card hsub
      _ = 6 := by decide
  have h2 : (Finset.Icc (-2 : ℤ) 2).card ≤ 5 := by
    have hsub : Finset.Icc (-2 : ℤ) 2 ⊆ ({-2, -1, 0, 1, 2} : Finset ℤ) := by
      intro x hx
      obtain ⟨hx1, hx2⟩ := Finset.mem_Icc.mp hx
      interval_cases x <;> decide
    calc
      (Finset.Icc (-2 : ℤ) 2).card ≤ ({-2, -1, 0, 1, 2} : Finset ℤ).card := Finset.card_le_card hsub
      _ = 5 := by decide
  have h3 : (Finset.Icc (-3 : ℤ) 3).card ≤ 7 := by
    have hsub : Finset.Icc (-3 : ℤ) 3 ⊆ ({-3, -2, -1, 0, 1, 2, 3} : Finset ℤ) := by
      intro x hx
      obtain ⟨hx1, hx2⟩ := Finset.mem_Icc.mp hx
      interval_cases x <;> decide
    calc
      (Finset.Icc (-3 : ℤ) 3).card ≤ ({-3, -2, -1, 0, 1, 2, 3} : Finset ℤ).card := Finset.card_le_card hsub
      _ = 7 := by decide
  have hA : A.card ≤ 30 := by
    dsimp [A]
    calc
      ((Finset.Icc (-1 : ℤ) 4).product (Finset.Icc (-2 : ℤ) 2)).card
          = (Finset.Icc (-1 : ℤ) 4).card * (Finset.Icc (-2 : ℤ) 2).card := Finset.card_product _ _
      _ ≤ 6 * 5 := Nat.mul_le_mul h1 h2
      _ = 30 := by norm_num
  have hB : B.card ≤ 35 := by
    dsimp [B]
    calc
      (((Finset.Icc (-2 : ℤ) 2).product (Finset.Icc (-3 : ℤ) 3)).image
        (fun p : ℤ × ℤ => (p.1 * aNext + p.2, p.1))).card
          ≤ ((Finset.Icc (-2 : ℤ) 2).product (Finset.Icc (-3 : ℤ) 3)).card := Finset.card_image_le
      _ = (Finset.Icc (-2 : ℤ) 2).card * (Finset.Icc (-3 : ℤ) 3).card := Finset.card_product _ _
      _ ≤ 5 * 7 := Nat.mul_le_mul h2 h3
      _ = 35 := by norm_num
  calc
    (A ∪ B).card ≤ A.card + B.card := Finset.card_union_le _ _
    _ ≤ 30 + 35 := Nat.add_le_add hA hB
    _ = 65 := by norm_num

#print axioms b_strict_bound
#print axioms smaller_half_a_bounds
#print axioms smaller_half_b_zero
#print axioms larger_half_c_bounds
#print axioms coefficientCandidates_spec
#print axioms coefficientCandidates_card_le

end NestedBinomialV10
