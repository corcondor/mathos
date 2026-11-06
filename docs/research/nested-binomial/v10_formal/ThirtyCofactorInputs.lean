import Mathlib.Tactic


namespace NestedBinomialV10
theorem target_equation_iff_normalized (i k : ℕ) : (Nat.choose (Nat.choose i (i - 3)) (Nat.choose k 1) = Nat.choose (i ^ 2) ((i - 3) ^ 2) + Nat.choose (k ^ 2) (1 ^ 2)) ↔ (Nat.choose (Nat.choose i (i - 3)) k = Nat.choose (i ^ 2) ((i - 3) ^ 2) + k ^ 2) := by
  simp

theorem target_k_le_choose (i k : ℕ) (heq : Nat.choose (Nat.choose i (i - 3)) k = Nat.choose (i ^ 2) ((i - 3) ^ 2) + k ^ 2) : k ≤ Nat.choose i (i - 3) := by
  by_contra h
  have hk : Nat.choose i (i - 3) < k := Nat.lt_of_not_ge h
  have hleft : Nat.choose (Nat.choose i (i - 3)) k = 0 :=
    Nat.choose_eq_zero_of_lt hk
  rw [hleft] at heq
  have hkpos : 0 < k := lt_of_le_of_lt (Nat.zero_le _) hk
  have hk2 : 0 < k ^ 2 := pow_pos hkpos 2
  have hsumpos : 0 < Nat.choose (i ^ 2) ((i - 3) ^ 2) + k ^ 2 :=
    lt_of_lt_of_le hk2 (Nat.le_add_left _ _)
  have hsumzero : Nat.choose (i ^ 2) ((i - 3) ^ 2) + k ^ 2 = 0 := heq.symm
  exact Nat.lt_irrefl 0 (hsumzero ▸ hsumpos)

theorem gcd_index_sub_three (i : ℕ) (hi : 3 ≤ i) : Nat.gcd i (i - 3) = Nat.gcd i 3 := by
  calc
    Nat.gcd i (i - 3) = Nat.gcd (i - 3) i := Nat.gcd_comm i (i - 3)
    _ = Nat.gcd (i - 3) (i - (i - 3)) := (Nat.gcd_sub_self_right (m := i - 3) (n := i) (by omega)).symm
    _ = Nat.gcd (i - 3) 3 := by rw [show i - (i - 3) = 3 by omega]
    _ = Nat.gcd i 3 := Nat.gcd_sub_self_left (m := 3) (n := i) hi

theorem target_index_cube_dvd (i k : ℕ) (hi : 3 ≤ i) (hk : k ≤ Nat.choose i (i - 3)) (heq : Nat.choose (Nat.choose i (i - 3)) k = Nat.choose (i ^ 2) ((i - 3) ^ 2) + k ^ 2) : i / Nat.gcd i 3 ∣ (min k (Nat.choose i (i - 3) - k)) ^ 3 := by
  let A := Nat.choose i (i - 3)
  let X := Nat.choose (i ^ 2) ((i - 3) ^ 2)
  let q := i / Nat.gcd i (i - 3)
  have hi0 : 0 < i := by omega
  have top_dvd : ∀ n k : ℕ, n ∣ k * Nat.choose n k := by
    intro n k
    cases n with
    | zero => cases k <;> simp [Nat.choose]
    | succ n =>
      cases k with
      | zero => simp
      | succ k =>
        refine ⟨Nat.choose n k, ?_⟩
        simpa [Nat.succ_eq_add_one, Nat.mul_comm] using
          (Nat.add_one_mul_choose_eq n k).symm
  have div_gcd_dvd_of_dvd_mul : ∀ (i j a : ℕ), 0 < i → i ∣ j * a → i / Nat.gcd i j ∣ a := by
    intro i j a hi h
    have hg : 0 < Nat.gcd i j := Nat.gcd_pos_of_pos_left j hi
    have hmul : Nat.gcd i j * (i / Nat.gcd i j) ∣
        Nat.gcd i j * ((j / Nat.gcd i j) * a) := by
      simpa only [← Nat.mul_assoc, Nat.mul_div_cancel' (Nat.gcd_dvd_left i j),
        Nat.mul_div_cancel' (Nat.gcd_dvd_right i j)] using h
    exact (Nat.coprime_div_gcd_div_gcd hg).dvd_of_dvd_mul_left
      ((Nat.mul_dvd_mul_iff_left hg).mp hmul)
  have div_gcd_dvd_choose : ∀ (i j : ℕ), 0 < i → i / Nat.gcd i j ∣ Nat.choose i j := by
    intro i j hi
    exact div_gcd_dvd_of_dvd_mul i j (Nat.choose i j) hi (top_dvd i j)
  have hA : q ∣ A := by
    change i / Nat.gcd i (i - 3) ∣ Nat.choose i (i - 3)
    exact div_gcd_dvd_choose i (i - 3) hi0
  have hX2 : q ^ 2 ∣ X := by
    change (i / Nat.gcd i (i - 3)) ^ 2 ∣ Nat.choose (i ^ 2) ((i - 3) ^ 2)
    have h := div_gcd_dvd_choose (i ^ 2) ((i - 3) ^ 2) (pow_pos hi0 2)
    simpa only [Nat.pow_gcd_pow, ← Nat.div_pow (Nat.gcd_dvd_left i (i - 3))] using h
  have hX : q ∣ X := by
    have hqq : q ∣ q ^ 2 := by
      simpa [pow_two] using dvd_mul_right q q
    exact dvd_trans hqq hX2
  have outer_other : ∀ (A B X Y q r : ℕ),
      q ∣ A → q ∣ X → Nat.choose A B = X + Y →
      Nat.choose A r = Nat.choose A B → q ∣ r * Y := by
    intro A B X Y q r hA hX heq hsym
    have hleft : q ∣ r * Nat.choose A r :=
      hA.trans (top_dvd A r)
    rw [hsym, heq, Nat.mul_add] at hleft
    exact (Nat.dvd_add_iff_right (dvd_mul_of_dvd_right hX r)).mpr hleft
  have outer_cube : ∀ (A B X q : ℕ), B ≤ A → q ∣ A → q ∣ X →
      Nat.choose A B = X + B ^ 2 → q ∣ (min B (A - B)) ^ 3 := by
    intro A B X q hBA hA hX heq
    by_cases hmin : B ≤ A - B
    · rw [min_eq_left hmin]
      have h := outer_other A B X (B ^ 2) q B hA hX heq rfl
      simpa [pow_succ, Nat.mul_comm] using h
    · rw [min_eq_right (by omega : A - B ≤ B)]
      let r := A - B
      change q ∣ r ^ 3
      have hAB : A = B + r := by dsimp [r]; omega
      have hsym : Nat.choose A r = Nat.choose A B := by
        dsimp [r]
        exact Nat.choose_symm hBA
      have h := outer_other A B X (B ^ 2) q r hA hX heq hsym
      have hAr : q ∣ 2 * A * r ^ 2 := by
        simpa [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using
          (dvd_mul_of_dvd_left hA (2 * r ^ 2))
      have hAAr : q ∣ A ^ 2 * r := by
        simpa [pow_two] using
          (dvd_mul_of_dvd_left (dvd_mul_of_dvd_left hA A) r)
      have hid : r * B ^ 2 + 2 * A * r ^ 2 = r ^ 3 + A ^ 2 * r := by
        rw [hAB]
        ring
      have hsum := dvd_add h hAr
      rw [hid] at hsum
      exact (Nat.dvd_add_iff_left hAAr).mpr hsum
  have hmain : q ∣ (min k (A - k)) ^ 3 := by
    have hkA : k ≤ A := by simpa [A] using hk
    have heqAX : Nat.choose A k = X + k ^ 2 := by simpa [A, X] using heq
    exact outer_cube A k X q hkA hA hX heqAX
  rw [← NestedBinomialV10.gcd_index_sub_three i hi]
  simpa [q, A] using hmain

#print axioms target_equation_iff_normalized
#print axioms target_k_le_choose
#print axioms gcd_index_sub_three
#print axioms target_index_cube_dvd

end NestedBinomialV10
