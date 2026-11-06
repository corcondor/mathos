import Mathlib.Tactic
import CFContinuantBridge


namespace NestedBinomialV10
theorem certificate_cylinder_supply (a : ℕ → ℤ) (ha : ∀ i, 1 ≤ a i) (ha1 : 2 ≤ a 1) (alpha : ℝ) (M : ℕ) (hbetween : (alpha - ((contsZ a (M + 1)).1 : ℝ) / ((contsZ a (M + 1)).2 : ℝ)) * (alpha - (((contsZ a (M + 1)).1 + (contsZ a M).1 : ℤ) : ℝ) / (((contsZ a (M + 1)).2 + (contsZ a M).2 : ℤ) : ℝ)) < 0) : ∃ u : ℝ, 1 < u ∧ alpha * (((contsZ a (M + 1)).2 : ℝ) * u + ((contsZ a M).2 : ℝ)) = ((contsZ a (M + 1)).1 : ℝ) * u + ((contsZ a M).1 : ℝ) := by
  let P1 : ℤ := (contsZ a (M + 1)).1
  let Q1 : ℤ := (contsZ a (M + 1)).2
  let P0 : ℤ := (contsZ a M).1
  let Q0 : ℤ := (contsZ a M).2
  have hord : 0 ≤ Q0 ∧ Q0 < Q1 := by
    simpa [P0, Q0, P1, Q1] using contsZ_den_ordering a ha ha1 M
  have hQ1pos : (0 : ℤ) < Q1 := lt_of_le_of_lt hord.1 hord.2
  have hQ0nonneg : (0 : ℤ) ≤ Q0 := hord.1
  have hQsumpos : (0 : ℤ) < Q1 + Q0 := by linarith
  have hQ1posR : (0 : ℝ) < (Q1 : ℝ) := by exact_mod_cast hQ1pos
  have hQsumposR : (0 : ℝ) < ((Q1 + Q0 : ℤ) : ℝ) := by exact_mod_cast hQsumpos
  have hQ1ne : (Q1 : ℝ) ≠ 0 := ne_of_gt hQ1posR
  have hQsumne : ((Q1 + Q0 : ℤ) : ℝ) ≠ 0 := ne_of_gt hQsumposR
  have hbetween' :
      (alpha - (P1 : ℝ) / (Q1 : ℝ)) *
        (alpha - ((P1 + P0 : ℤ) : ℝ) / ((Q1 + Q0 : ℤ) : ℝ)) < 0 := by
    simpa [P1, Q1, P0, Q0] using hbetween
  let A : ℝ := alpha * (Q1 : ℝ) - (P1 : ℝ)
  let C : ℝ := alpha * ((Q1 + Q0 : ℤ) : ℝ) - ((P1 + P0 : ℤ) : ℝ)
  have hAeq : A = (Q1 : ℝ) * (alpha - (P1 : ℝ) / (Q1 : ℝ)) := by
    dsimp [A]
    field_simp [hQ1ne] <;> ring
  have hCeq : C = ((Q1 + Q0 : ℤ) : ℝ) *
      (alpha - ((P1 + P0 : ℤ) : ℝ) / ((Q1 + Q0 : ℤ) : ℝ)) := by
    dsimp [C]
    field_simp [hQsumne] <;> ring
  have hAC : A * C < 0 := by
    have hprod := mul_lt_mul_of_pos_left hbetween' (mul_pos hQ1posR hQsumposR)
    have hprod' : ((Q1 : ℝ) * (alpha - (P1 : ℝ) / (Q1 : ℝ))) *
        (((Q1 + Q0 : ℤ) : ℝ) *
          (alpha - ((P1 + P0 : ℤ) : ℝ) / ((Q1 + Q0 : ℤ) : ℝ))) < 0 := by
      calc
        ((Q1 : ℝ) * (alpha - (P1 : ℝ) / (Q1 : ℝ))) *
            (((Q1 + Q0 : ℤ) : ℝ) *
              (alpha - ((P1 + P0 : ℤ) : ℝ) / ((Q1 + Q0 : ℤ) : ℝ)))
            = ((Q1 : ℝ) * ((Q1 + Q0 : ℤ) : ℝ)) *
                ((alpha - (P1 : ℝ) / (Q1 : ℝ)) *
                  (alpha - ((P1 + P0 : ℤ) : ℝ) / ((Q1 + Q0 : ℤ) : ℝ))) := by ring
        _ < 0 := by
          simpa using hprod
    rw [hAeq, hCeq]
    exact hprod'
  have hA_ne : A ≠ 0 := by
    intro hA0
    have hzero : (0 : ℝ) < 0 := by simpa [hA0] using hAC
    exact (lt_irrefl (0 : ℝ)) hzero
  have hA2pos : 0 < A ^ 2 := sq_pos_of_ne_zero hA_ne
  have hxmul : 0 < ((-C) / A) * A ^ 2 := by
    have hEq : ((-C) / A) * A ^ 2 = -(A * C) := by
      field_simp [hA_ne] <;> ring
    rw [hEq]
    linarith [hAC]
  have hratio : 0 < (-C) / A := (mul_pos_iff_of_pos_right hA2pos).mp hxmul
  let u : ℝ := 1 + (-C) / A
  have hu : 1 < u := by
    dsimp [u]
    linarith [hratio]
  refine ⟨u, hu, ?_⟩
  have hC_rel : C = A + (alpha * (Q0 : ℝ) - (P0 : ℝ)) := by
    dsimp [A, C]
    push_cast
    ring
  have hAu : A * u = -(alpha * (Q0 : ℝ) - (P0 : ℝ)) := by
    dsimp [u]
    have hEq : A * (1 + (-C) / A) = A - C := by
      field_simp [hA_ne] <;> ring
    rw [hEq, hC_rel]
    ring
  have hdiff :
      alpha * ((Q1 : ℝ) * u + (Q0 : ℝ)) - ((P1 : ℝ) * u + (P0 : ℝ))
        = A * u + (alpha * (Q0 : ℝ) - (P0 : ℝ)) := by
    dsimp [A]
    ring
  have hzero :
      alpha * ((Q1 : ℝ) * u + (Q0 : ℝ)) - ((P1 : ℝ) * u + (P0 : ℝ)) = 0 := by
    rw [hdiff, hAu]
    ring
  have htarget : alpha * ((Q1 : ℝ) * u + (Q0 : ℝ)) = (P1 : ℝ) * u + (P0 : ℝ) := by
    linarith
  simpa [P1, Q1, P0, Q0] using htarget

theorem cylinder_step (a : ℕ → ℤ) (alpha u : ℝ) (m : ℕ) (hm : 1 ≤ m) (hu : 1 < u) (hcyl : alpha * (((contsZ a (m + 1)).2 : ℝ) * u + ((contsZ a m).2 : ℝ)) = ((contsZ a (m + 1)).1 : ℝ) * u + ((contsZ a m).1 : ℝ)) : ∃ v : ℝ, (a m : ℝ) < v ∧ v < (a m : ℝ) + 1 ∧ alpha * (((contsZ a m).2 : ℝ) * v + ((contsZ a (m - 1)).2 : ℝ)) = ((contsZ a m).1 : ℝ) * v + ((contsZ a (m - 1)).1 : ℝ) := by
  rcases m with _ | k
  · omega
  · let v : ℝ := (a (k + 1) : ℝ) + 1 / u
    have hu_pos : 0 < u := by linarith
    have hu_ne : u ≠ 0 := ne_of_gt hu_pos
    have hinv_pos : 0 < 1 / u := div_pos zero_lt_one hu_pos
    have hinv_lt_one : 1 / u < 1 := by
      rw [div_lt_iff₀ hu_pos]
      simpa using hu
    refine ⟨v, ?_, ?_, ?_⟩
    · dsimp [v]
      linarith
    · dsimp [v]
      linarith
    · have hcyl' : alpha * (((contsZ a (k + 1 + 1)).2 : ℝ) * u + ((contsZ a (k + 1)).2 : ℝ)) = ((contsZ a (k + 1 + 1)).1 : ℝ) * u + ((contsZ a (k + 1)).1 : ℝ) := by
        simpa using hcyl
      have hP : (contsZ a (k + 1 + 1)).1 = a (k + 1) * (contsZ a (k + 1)).1 + (contsZ a k).1 := by
        rfl
      have hQ : (contsZ a (k + 1 + 1)).2 = a (k + 1) * (contsZ a (k + 1)).2 + (contsZ a k).2 := by
        rfl
      let P : ℝ := ((contsZ a (k + 1)).1 : ℝ)
      let Q : ℝ := ((contsZ a (k + 1)).2 : ℝ)
      let Pm : ℝ := ((contsZ a k).1 : ℝ)
      let Qm : ℝ := ((contsZ a k).2 : ℝ)
      let am : ℝ := (a (k + 1) : ℝ)
      have hcyl_real : alpha * ((am * Q + Qm) * u + Q) = (am * P + Pm) * u + P := by
        have h := hcyl'
        rw [hP, hQ] at h
        push_cast at h
        simpa [P, Q, Pm, Qm, am] using h
      have hmul : u * (alpha * (Q * (am + 1 / u) + Qm)) = u * (P * (am + 1 / u) + Pm) := by
        calc
          u * (alpha * (Q * (am + 1 / u) + Qm))
              = alpha * ((am * Q + Qm) * u + Q) := by
                field_simp [hu_ne] <;> ring
          _ = (am * P + Pm) * u + P := hcyl_real
          _ = u * (P * (am + 1 / u) + Pm) := by
                field_simp [hu_ne] <;> ring
      have hmain : alpha * (Q * (am + 1 / u) + Qm) = P * (am + 1 / u) + Pm :=
        mul_left_cancel₀ hu_ne hmul
      simpa [v, P, Q, Pm, Qm, am] using hmain

theorem terminal_cylinder_descends (a : ℕ → ℤ) (ha : ∀ i, 1 ≤ a i) (alpha u : ℝ) (M : ℕ) (hu : 1 < u) (hcyl : alpha * (((contsZ a (M + 1)).2 : ℝ) * u + ((contsZ a M).2 : ℝ)) = ((contsZ a (M + 1)).1 : ℝ) * u + ((contsZ a M).1 : ℝ)) : ∀ i : ℕ, i < M → ∃ v : ℝ, (a (i + 1) : ℝ) < v ∧ v < (a (i + 1) : ℝ) + 1 ∧ alpha * (((contsZ a (i + 1)).2 : ℝ) * v + ((contsZ a i).2 : ℝ)) = ((contsZ a (i + 1)).1 : ℝ) * v + ((contsZ a i).1 : ℝ) := by
  intro i hi
  have main : ∀ M : ℕ, ∀ u : ℝ, 1 < u →
      alpha * (((contsZ a (M + 1)).2 : ℝ) * u + ((contsZ a M).2 : ℝ)) =
        ((contsZ a (M + 1)).1 : ℝ) * u + ((contsZ a M).1 : ℝ) →
      ∀ i : ℕ, i < M → ∃ v : ℝ, (a (i + 1) : ℝ) < v ∧ v < (a (i + 1) : ℝ) + 1 ∧
        alpha * (((contsZ a (i + 1)).2 : ℝ) * v + ((contsZ a i).2 : ℝ)) =
          ((contsZ a (i + 1)).1 : ℝ) * v + ((contsZ a i).1 : ℝ) := by
    intro M
    induction M with
    | zero =>
        intro u hu hcyl i hi
        omega
    | succ M ih =>
        intro u hu hcyl i hi
        obtain ⟨v, hvlo, hvhi, hvcyl⟩ :=
          cylinder_step a alpha u (M + 1) (by omega) hu hcyl
        have hv1 : 1 < v := lt_of_le_of_lt (by exact_mod_cast ha (M + 1)) hvlo
        by_cases hiM : i = M
        · subst i
          refine ⟨v, ?_, ?_, ?_⟩
          · exact hvlo
          · exact hvhi
          · simpa using hvcyl
        · have hiM' : i < M := by omega
          have hvcylM :
              alpha * (((contsZ a (M + 1)).2 : ℝ) * v + ((contsZ a M).2 : ℝ)) =
                ((contsZ a (M + 1)).1 : ℝ) * v + ((contsZ a M).1 : ℝ) := by
            simpa using hvcyl
          exact ih v hv1 hvcylM i hiM'
  exact main M u hu hcyl i hi

theorem certificate_prefix_coverage (a : ℕ → ℤ) (ha : ∀ i, 1 ≤ a i) (ha1 : 2 ≤ a 1) (alpha : ℝ) (M : ℕ) (hbetween : (alpha - ((contsZ a (M + 1)).1 : ℝ) / ((contsZ a (M + 1)).2 : ℝ)) * (alpha - (((contsZ a (M + 1)).1 + (contsZ a M).1 : ℤ) : ℝ) / (((contsZ a (M + 1)).2 + (contsZ a M).2 : ℤ) : ℝ)) < 0) (p q : ℤ) (hq : 0 < q) (hq_lt : q < (contsZ a (M + 1)).2) (hred : Nat.Coprime (Int.natAbs p) (Int.natAbs q)) (happrox : |alpha - (p : ℝ) / (q : ℝ)| < 3 / (2 * (q : ℝ) ^ 2)) : ∃ i : ℕ, i < M ∧ (contsZ a (i + 1)).2 ≤ q ∧ q < (contsZ a (i + 2)).2 ∧ ∃ a' b c : ℤ, p = a' * (contsZ a (i + 1)).1 + b * (contsZ a i).1 ∧ q = a' * (contsZ a (i + 1)).2 + b * (contsZ a i).2 ∧ c = a' - b * a (i + 1) ∧ p = b * (contsZ a (i + 2)).1 + c * (contsZ a (i + 1)).1 ∧ q = b * (contsZ a (i + 2)).2 + c * (contsZ a (i + 1)).2 ∧ (a', b) ∈ coefficientCandidates (a (i + 1)) := by
  have hMpos : 0 < M := by
    by_contra hM
    have hM0 : M = 0 := by omega
    have hq_lt1 : q < 1 := by
      simpa [hM0, contsZ] using hq_lt
    omega
  let Q : ℕ → ℕ := fun k => ((contsZ a (k + 1)).2).toNat
  let H : ℕ := ((contsZ a (M + 1)).2).toNat
  let qn : ℕ := q.toNat
  have hq_nonneg : 0 ≤ q := le_of_lt hq
  have hq_cast : (qn : ℤ) = q := by
    dsimp [qn]
    exact Int.toNat_of_nonneg hq_nonneg
  have hH_cast : (H : ℤ) = (contsZ a (M + 1)).2 := by
    dsimp [H]
    exact Int.toNat_of_nonneg (NestedBinomialV10.contsZ_den_ordering a ha ha1 (M + 1)).1
  have hQ_cast : ∀ k : ℕ, (Q k : ℤ) = (contsZ a (k + 1)).2 := by
    intro k
    dsimp [Q]
    exact Int.toNat_of_nonneg (NestedBinomialV10.contsZ_den_ordering a ha ha1 (k + 1)).1
  have hq1 : 1 ≤ qn := by
    have h : (1 : ℤ) ≤ (qn : ℤ) := by
      rw [hq_cast]
      omega
    exact_mod_cast h
  have hqH : qn < H := by
    have h : (qn : ℤ) < (H : ℤ) := by
      rw [hq_cast, hH_cast]
      exact hq_lt
    exact_mod_cast h
  have hQstrict : ∀ i, i < M → Q i < Q (i + 1) := by
    intro i _hi
    have hord := NestedBinomialV10.contsZ_den_ordering a ha ha1 (i + 1)
    have hidx : (i + 1) + 1 = i + 2 := by omega
    have hlt : (contsZ a (i + 1)).2 < (contsZ a (i + 2)).2 := by
      simpa [hidx] using hord.2
    have h1 : (Q i : ℤ) = (contsZ a (i + 1)).2 := hQ_cast i
    have h2 : (Q (i + 1) : ℤ) = (contsZ a (i + 2)).2 := by
      simpa [hidx] using hQ_cast (i + 1)
    have h : (Q i : ℤ) < (Q (i + 1) : ℤ) := by
      rw [h1, h2]
      exact hlt
    exact_mod_cast h
  have hQ0 : Q 0 = 1 := by
    dsimp [Q]
    simp [contsZ]
  have hQn : H ≤ Q M := by
    dsimp [H, Q]
    exact le_rfl
  obtain ⟨i, hiM, hQi, hqi⟩ :=
    NestedBinomialV10.finite_prefix_interval Q M H qn hMpos hQstrict hQ0 hQn hq1 hqH
  have hQ_le_q : (contsZ a (i + 1)).2 ≤ q := by
    have h : (Q i : ℤ) ≤ (qn : ℤ) := by exact_mod_cast hQi
    rwa [hQ_cast i, hq_cast] at h
  have hq_lt_Q : q < (contsZ a (i + 2)).2 := by
    have hidx : (i + 1) + 1 = i + 2 := by omega
    have h2 : (Q (i + 1) : ℤ) = (contsZ a (i + 2)).2 := by
      simpa [hidx] using hQ_cast (i + 1)
    have h : (qn : ℤ) < (Q (i + 1) : ℤ) := by exact_mod_cast hqi
    rwa [hq_cast, h2] at h
  obtain ⟨u, hu, hcyl⟩ :=
    NestedBinomialV10.certificate_cylinder_supply a ha ha1 alpha M hbetween
  have hdesc :=
    NestedBinomialV10.terminal_cylinder_descends a ha alpha u M hu hcyl
  obtain ⟨v, hvlo, hvhi, hvcyl⟩ := hdesc i hiM
  obtain ⟨a', b, c, h1, h2, h3, h4, h5, h6⟩ :=
    NestedBinomialV10.certificate_coverage_bridge a ha ha1 alpha v i p q
      hvlo hvhi hvcyl hq hQ_le_q hq_lt_Q hred happrox
  exact ⟨i, hiM, hQ_le_q, hq_lt_Q, a', b, c, h1, h2, h3, h4, h5, h6⟩

#print axioms certificate_cylinder_supply
#print axioms cylinder_step
#print axioms terminal_cylinder_descends
#print axioms certificate_prefix_coverage

end NestedBinomialV10
