import Mathlib.Tactic


namespace NestedBinomialV10
theorem prime_cube_dvd_of_dvd_cube_not_dvd_sq (Q r : ℕ) (hQ : 0 < Q) (hr : 0 < r) (hdvd : Q ∣ r ^ 3) (hnot : ¬ Q ∣ r ^ 2) : ∃ q : ℕ, Nat.Prime q ∧ q ^ 3 ∣ Q ∧ q ∣ r := by
  classical
  have hQ0 : Q ≠ 0 := hQ.ne'
  have hr0 : r ≠ 0 := hr.ne'
  have hr20 : r ^ 2 ≠ 0 := pow_ne_zero 2 hr0
  have hr30 : r ^ 3 ≠ 0 := pow_ne_zero 3 hr0
  have hnotle : ¬ (∀ p : ℕ, p.Prime → Q.factorization p ≤ (r ^ 2).factorization p) := by
    intro h
    exact hnot ((Nat.factorization_prime_le_iff_dvd hQ0 hr20).mp h)
  push_neg at hnotle
  obtain ⟨p, hp, hlt⟩ := hnotle
  have hle : Q.factorization p ≤ (r ^ 3).factorization p :=
    (Nat.factorization_prime_le_iff_dvd hQ0 hr30).mpr hdvd p hp
  have hsq : (r ^ 2).factorization p = 2 * r.factorization p := by
    rw [pow_two, Nat.factorization_mul hr0 hr0, Finsupp.add_apply]
    ring
  have hcube : (r ^ 3).factorization p = 3 * r.factorization p := by
    rw [show r ^ 3 = r ^ 2 * r by ring]
    rw [Nat.factorization_mul (pow_ne_zero 2 hr0) hr0, Finsupp.add_apply, hsq]
    ring
  rw [hsq] at hlt
  rw [hcube] at hle
  have hepos : 0 < r.factorization p := by omega
  have hQfact : 3 ≤ Q.factorization p := by omega
  have hq3 : p ^ 3 ∣ Q :=
    (hp.pow_dvd_iff_le_factorization hQ0).mpr hQfact
  have hpdvd : p ∣ r :=
    (hp.dvd_iff_one_le_factorization hr0).mpr (by omega)
  exact ⟨p, hp, hq3, hpdvd⟩

theorem cofactor_M_mul_Q (n : ℕ) : Nat.gcd n 3 * Nat.gcd (n - 1) 6 * ((n / Nat.gcd n 3) * ((n - 1) / Nat.gcd (n - 1) 6)) = n * (n - 1) := by
  have h1 : Nat.gcd n 3 * (n / Nat.gcd n 3) = n :=
    Nat.mul_div_cancel' (Nat.gcd_dvd_left n 3)
  have h2 : Nat.gcd (n - 1) 6 * ((n - 1) / Nat.gcd (n - 1) 6) = n - 1 :=
    Nat.mul_div_cancel' (Nat.gcd_dvd_left (n - 1) 6)
  calc
    Nat.gcd n 3 * Nat.gcd (n - 1) 6 * ((n / Nat.gcd n 3) * ((n - 1) / Nat.gcd (n - 1) 6))
        = (Nat.gcd n 3 * (n / Nat.gcd n 3)) *
            (Nat.gcd (n - 1) 6 * ((n - 1) / Nat.gcd (n - 1) 6)) := by
          ring
    _ = n * (n - 1) := by
          rw [h1, h2]

theorem cofactor_M_mul_sq (n r L : ℕ) (hL : L * ((n / Nat.gcd n 3) * ((n - 1) / Nat.gcd (n - 1) 6)) = r ^ 2) : Nat.gcd n 3 * Nat.gcd (n - 1) 6 * r ^ 2 = L * n * (n - 1) := by
  have hQ := cofactor_M_mul_Q n
  calc
    Nat.gcd n 3 * Nat.gcd (n - 1) 6 * r ^ 2
        = Nat.gcd n 3 * Nat.gcd (n - 1) 6 *
            (L * ((n / Nat.gcd n 3) * ((n - 1) / Nat.gcd (n - 1) 6))) := by
          rw [← hL]
    _ = (Nat.gcd n 3 * Nat.gcd (n - 1) 6 *
            ((n / Nat.gcd n 3) * ((n - 1) / Nat.gcd (n - 1) 6))) * L := by
          ac_rfl
    _ = (n * (n - 1)) * L := by
          rw [hQ]
    _ = L * n * (n - 1) := by
          ac_rfl

#print axioms prime_cube_dvd_of_dvd_cube_not_dvd_sq
#print axioms cofactor_M_mul_Q
#print axioms cofactor_M_mul_sq

end NestedBinomialV10
