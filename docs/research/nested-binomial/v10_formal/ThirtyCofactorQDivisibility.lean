import Mathlib.Tactic
import ThirtyCofactorInputs
import ThirtyCofactorSecondDivisor


namespace NestedBinomialV10
theorem cofactor_two_cube_dvd (i k : ℕ) (hi : 3 ≤ i) (hk : k ≤ Nat.choose i (i - 3)) (heq : Nat.choose (Nat.choose i (i - 3)) k = Nat.choose (i ^ 2) ((i - 3) ^ 2) + k ^ 2) : (i - 1) / Nat.gcd (i - 1) 6 ∣ (min k (Nat.choose i (i - 3) - k)) ^ 3 := by
  let A := Nat.choose i (i - 3)
  let X := Nat.choose (i ^ 2) ((i - 3) ^ 2)
  let q := (i - 1) / Nat.gcd (i - 1) 6
  have hmain : q ∣ (min k (A - k)) ^ 3 := by
    have hkA : k ≤ A := by simpa [A] using hk
    have heqAX : Nat.choose A k = X + k ^ 2 := by simpa [A, X] using heq
    have top_dvd : ∀ n k : Nat, n ∣ k * Nat.choose n k := by
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
    have outer_other : ∀ (A B X Y q r : Nat),
        q ∣ A → q ∣ X → Nat.choose A B = X + Y →
        Nat.choose A r = Nat.choose A B → q ∣ r * Y := by
      intro A B X Y q r hA hX heq hsym
      have hleft : q ∣ r * Nat.choose A r :=
        hA.trans (top_dvd A r)
      rw [hsym, heq, Nat.mul_add] at hleft
      exact (Nat.dvd_add_iff_right (dvd_mul_of_dvd_right hX r)).mpr hleft
    have outer_cube : ∀ (A B X q : Nat), B ≤ A → q ∣ A → q ∣ X →
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
          exact Nat.choose_symm (n := A) (k := B) hBA
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
    have hA : q ∣ A := by
      have hq3 : q ∣ Nat.choose i 3 := by
        simpa [q] using NestedBinomialV10.cofactor_one_dvd_choose_three i (by omega : 1 ≤ i)
      have hsym : Nat.choose i (i - 3) = Nat.choose i 3 :=
        Nat.choose_symm (n := i) (k := 3) hi
      rw [show A = Nat.choose i 3 by simpa [A] using hsym]
      exact hq3
    have hX : q ∣ X := by
      by_cases hi5 : 5 ≤ i
      · simpa [q, X] using NestedBinomialV10.cofactor_one_dvd_squared_index_choose i hi5
      · have hi' : i = 3 ∨ i = 4 := by omega
        rcases hi' with rfl | rfl
        · have hq1 : q = 1 := by
            dsimp [q]
          rw [hq1]
          exact one_dvd _
        · have hq1 : q = 1 := by
            dsimp [q]
          rw [hq1]
          exact one_dvd _
    exact outer_cube A k X q hkA hA hX heqAX
  simpa [q, A] using hmain

theorem Q_cube_dvd (i k : ℕ) (hi : 3 ≤ i) (hk : k ≤ Nat.choose i (i - 3)) (heq : Nat.choose (Nat.choose i (i - 3)) k = Nat.choose (i ^ 2) ((i - 3) ^ 2) + k ^ 2) : (i / Nat.gcd i 3) * ((i - 1) / Nat.gcd (i - 1) 6) ∣ (min k (Nat.choose i (i - 3) - k)) ^ 3 := by
  let a := i / Nat.gcd i 3
  let b := (i - 1) / Nat.gcd (i - 1) 6
  have hcop_i : Nat.Coprime i (i - 1) := by
    rw [Nat.coprime_iff_gcd_eq_one]
    calc
      Nat.gcd i (i - 1) = Nat.gcd (i - 1) i := Nat.gcd_comm i (i - 1)
      _ = Nat.gcd (i - 1) (i - (i - 1)) :=
        (Nat.gcd_sub_self_right (m := i - 1) (n := i) (by omega)).symm
      _ = Nat.gcd (i - 1) 1 := by
        rw [show i - (i - 1) = 1 by omega]
      _ = 1 := by simp
  have ha_dvd_i : a ∣ i := by
    dsimp [a]
    refine ⟨Nat.gcd i 3, ?_⟩
    rw [Nat.mul_comm, Nat.mul_div_cancel' (Nat.gcd_dvd_left i 3)]
  have hb_dvd_i_sub : b ∣ i - 1 := by
    dsimp [b]
    refine ⟨Nat.gcd (i - 1) 6, ?_⟩
    rw [Nat.mul_comm, Nat.mul_div_cancel' (Nat.gcd_dvd_left (i - 1) 6)]
  have hcop : Nat.Coprime a b :=
    Nat.Coprime.of_dvd_right hb_dvd_i_sub
      (Nat.Coprime.of_dvd_left ha_dvd_i hcop_i)
  have h1 : a ∣ (min k (Nat.choose i (i - 3) - k)) ^ 3 := by
    simpa [a] using target_index_cube_dvd i k hi hk heq
  have h2 : b ∣ (min k (Nat.choose i (i - 3) - k)) ^ 3 := by
    simpa [b] using cofactor_two_cube_dvd i k hi hk heq
  have hprod : a * b ∣ (min k (Nat.choose i (i - 3) - k)) ^ 3 :=
    Nat.Coprime.mul_dvd_of_dvd_of_dvd hcop h1 h2
  simpa [a, b] using hprod

#print axioms cofactor_two_cube_dvd
#print axioms Q_cube_dvd

end NestedBinomialV10
