import Mathlib.Tactic
import ThirtyCofactorInputs
import ThirtyCofactorQDivisibility
import ThirtyCofactorCubePrimeExtraction
import ThirtyCofactorCubeLocalization


namespace NestedBinomialV10
theorem target_cube_localization (w p a i k : ℕ) (hw : 1 ≤ w) (hp : Nat.Prime p) (ha : 1 ≤ a) (hi : i = w * p ^ a + 2) (hk : 1 ≤ k) (heq : Nat.choose (Nat.choose i (i - 3)) (Nat.choose k 1) = Nat.choose (i ^ 2) ((i - 3) ^ 2) + Nat.choose (k ^ 2) (1 ^ 2)) (hnot : ¬ ((i / Nat.gcd i 3) * ((i - 1) / Nat.gcd (i - 1) 6)) ∣ (min k (Nat.choose i (i - 3) - k)) ^ 2) : ∃ q : ℕ, Nat.Prime q ∧ (q ^ 3 ∣ i ∨ q ^ 3 ∣ i - 1) ∧ (q = 2 ∨ Nat.Coprime q (w * p)) := by
  have hi3 : 3 ≤ i := by
    rw [hi]
    have hwpos : 0 < w := by omega
    have hppos : 0 < p ^ a := pow_pos hp.pos a
    have hprod : 0 < w * p ^ a := Nat.mul_pos hwpos hppos
    omega
  have heq' : Nat.choose (Nat.choose i (i - 3)) k =
      Nat.choose (i ^ 2) ((i - 3) ^ 2) + k ^ 2 := by
    exact (target_equation_iff_normalized i k).mp heq
  have hkA : k ≤ Nat.choose i (i - 3) :=
    target_k_le_choose i k heq'
  have hQdvd :
      (i / Nat.gcd i 3) * ((i - 1) / Nat.gcd (i - 1) 6) ∣
        (min k (Nat.choose i (i - 3) - k)) ^ 3 :=
    Q_cube_dvd i k hi3 hkA heq'
  have hr : 0 < min k (Nat.choose i (i - 3) - k) := by
    by_contra h
    have hr0 : min k (Nat.choose i (i - 3) - k) = 0 :=
      Nat.eq_zero_of_not_pos h
    apply hnot
    simpa [hr0] using
      (dvd_zero ((i / Nat.gcd i 3) * ((i - 1) / Nat.gcd (i - 1) 6)))
  exact cube_prime_localization w p a i
    (min k (Nat.choose i (i - 3) - k)) hw hp ha hi hr hQdvd hnot

theorem delta_gt_one_imp_not_dvd_sq (Q r : ℕ) (hQ : 0 < Q) (h : 1 < Q / Nat.gcd Q (r ^ 2)) : ¬ Q ∣ r ^ 2 := by
  intro hdvd
  have hgdvd : Nat.gcd Q (r ^ 2) ∣ Q := Nat.gcd_dvd_left Q (r ^ 2)
  have hQdvd : Q ∣ Nat.gcd Q (r ^ 2) := Nat.dvd_gcd (dvd_refl Q) hdvd
  have hg : Nat.gcd Q (r ^ 2) = Q := Nat.dvd_antisymm hgdvd hQdvd
  rw [hg, Nat.div_self hQ] at h
  omega

#print axioms target_cube_localization
#print axioms delta_gt_one_imp_not_dvd_sq

end NestedBinomialV10
