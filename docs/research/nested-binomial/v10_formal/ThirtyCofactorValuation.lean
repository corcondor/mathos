import Mathlib.Tactic
import ThirtyCofactorCubePrimeExtraction


namespace NestedBinomialV10
theorem factorization_mul_prime_pow (w p a : ℕ) (hw : 0 < w) (hp : Nat.Prime p) (hpa : ¬ p ∣ w) : (w * p ^ a).factorization p = a := by
  rw [Nat.factorization_mul hw.ne' (pow_ne_zero a hp.ne_zero), Finsupp.add_apply,
    Nat.factorization_eq_zero_of_not_dvd hpa, Nat.factorization_pow_self hp, zero_add]

theorem factorization_two_of_odd (m : ℕ) (hm : Odd m) : m.factorization 2 = 0 := by
  exact Nat.factorization_eq_zero_of_not_dvd hm.not_two_dvd_nat

theorem six_mul_choose_three (i : ℕ) (hi : 3 ≤ i) : 6 * Nat.choose i 3 = i * (i - 1) * (i - 2) := by
  have h : i.descFactorial 3 = 6 * Nat.choose i 3 := by
    rw [Nat.descFactorial_eq_factorial_mul_choose i 3]
    norm_num
  have hdesc : i.descFactorial 3 = i * (i - 1) * (i - 2) := by
    simp only [Nat.descFactorial_succ, Nat.descFactorial_zero]
    ac_rfl
  rw [← h, hdesc]

theorem factorization_choose_three (w p a i : ℕ) (hw : 1 ≤ w) (hp : Nat.Prime p) (hpa : ¬ p ∣ w) (ha : 1 ≤ a) (hi : i = w * p ^ a + 2) (hq : 4 * w < p ^ a) : (Nat.choose i 3).factorization p = a - (if p = 3 then 1 else 0) := by
  rw [hi]
  have hwpos : 0 < w := by omega
  have hNpos : 0 < w * p ^ a := Nat.mul_pos hwpos (pow_pos hp.pos a)
  have hNne : w * p ^ a ≠ 0 := hNpos.ne'
  have hN1ne : w * p ^ a + 1 ≠ 0 := by omega
  have hN2ne : w * p ^ a + 2 ≠ 0 := by omega
  have hi3 : 3 ≤ w * p ^ a + 2 := by omega
  have hsix := six_mul_choose_three (w * p ^ a + 2) hi3
  have hsub1 : w * p ^ a + 2 - 1 = w * p ^ a + 1 := by omega
  have hsub2 : w * p ^ a + 2 - 2 = w * p ^ a := by omega
  rw [hsub1, hsub2] at hsix
  have hchoose_ne : Nat.choose (w * p ^ a + 2) 3 ≠ 0 := Nat.choose_ne_zero hi3
  have hNfac : (w * p ^ a).factorization p = a :=
    factorization_mul_prime_pow w p a hwpos hp hpa
  have hpdvd : p ∣ w * p ^ a :=
    dvd_mul_of_dvd_right (dvd_pow_self p (by omega : a ≠ 0)) w
  have hN1fac : (w * p ^ a + 1).factorization p = 0 := by
    apply Nat.factorization_eq_zero_of_not_dvd
    intro hd
    have h1 : p ∣ (w * p ^ a + 1) - w * p ^ a := Nat.dvd_sub hd hpdvd
    have h2 : (w * p ^ a + 1) - w * p ^ a = 1 := by omega
    rw [h2] at h1
    have hle : p ≤ 1 := Nat.le_of_dvd (by norm_num) h1
    have hp2le : 2 ≤ p := hp.two_le
    omega
  have hA : (w * p ^ a + 2).factorization p = if p = 2 then 1 else 0 := by
    by_cases hp2 : p = 2
    · rw [hp2] at hq
      rw [hp2]
      have ha2 : 2 ≤ a := by
        have h4 : 4 < 2 ^ a := by omega
        have h : 2 ^ 2 < 2 ^ a := by simpa using h4
        have h2a : 2 < a := (Nat.pow_lt_pow_iff_right (by norm_num : 1 < 2)).mp h
        omega
      have hb : a = (a - 1) + 1 := by omega
      have h2a : 2 ^ a = 2 ^ (a - 1) * 2 := by
        conv_lhs => rw [hb]
        rw [pow_succ]
      have hAeq : w * 2 ^ a + 2 = 2 * (w * 2 ^ (a - 1) + 1) := by
        rw [h2a]
        ring
      have hodd0 : (w * 2 ^ (a - 1) + 1).factorization 2 = 0 := by
        apply Nat.factorization_eq_zero_of_not_dvd
        intro hd
        have h2dvd : 2 ∣ w * 2 ^ (a - 1) :=
          dvd_mul_of_dvd_right (dvd_pow_self 2 (by omega : a - 1 ≠ 0)) w
        have h1 : 2 ∣ (w * 2 ^ (a - 1) + 1) - w * 2 ^ (a - 1) := Nat.dvd_sub hd h2dvd
        have h2 : (w * 2 ^ (a - 1) + 1) - w * 2 ^ (a - 1) = 1 := by omega
        rw [h2] at h1
        have hle : 2 ≤ 1 := Nat.le_of_dvd (by norm_num) h1
        omega
      have hA2 : (w * 2 ^ a + 2).factorization 2 = 1 := by
        rw [hAeq]
        rw [Nat.factorization_mul (by norm_num : (2:ℕ) ≠ 0) (by omega : w * 2 ^ (a - 1) + 1 ≠ 0)]
        rw [Finsupp.add_apply, Nat.Prime.factorization_self Nat.prime_two, hodd0]
      simpa using hA2
    · rw [if_neg hp2]
      apply Nat.factorization_eq_zero_of_not_dvd
      intro hd
      have h1 : p ∣ (w * p ^ a + 2) - w * p ^ a := Nat.dvd_sub hd hpdvd
      have h2 : (w * p ^ a + 2) - w * p ^ a = 2 := by omega
      rw [h2] at h1
      have hp_eq : p = 2 := (Nat.prime_dvd_prime_iff_eq hp Nat.prime_two).mp h1
      exact hp2 hp_eq
  have hfac : (6 : ℕ).factorization p + (Nat.choose (w * p ^ a + 2) 3).factorization p
      = (w * p ^ a + 2).factorization p + (w * p ^ a + 1).factorization p + (w * p ^ a).factorization p := by
    have h := congrArg (fun n : ℕ => n.factorization p) hsix
    rw [Nat.factorization_mul (by norm_num : (6:ℕ) ≠ 0) hchoose_ne, Finsupp.add_apply] at h
    rw [Nat.factorization_mul (mul_ne_zero hN2ne hN1ne) hNne, Finsupp.add_apply,
        Nat.factorization_mul hN2ne hN1ne, Finsupp.add_apply] at h
    exact h
  have hval : (Nat.choose (w * p ^ a + 2) 3).factorization p
      = (if p = 2 then 1 else 0) + a - (6 : ℕ).factorization p := by
    have h := hfac
    rw [hA, hN1fac, hNfac] at h
    have h1 : (6 : ℕ).factorization p + (Nat.choose (w * p ^ a + 2) 3).factorization p
        = (if p = 2 then 1 else 0) + a := by
      rw [h]
      rw [Nat.add_zero]
    rw [← h1, Nat.add_sub_cancel_left]
  by_cases hp2 : p = 2
  · rw [hp2] at hval
    rw [hp2]
    have h6 : (6 : ℕ).factorization 2 = 1 := by
      rw [show (6:ℕ) = 2 * 3 by norm_num,
          Nat.factorization_mul (by norm_num : (2:ℕ) ≠ 0) (by norm_num : (3:ℕ) ≠ 0),
          Finsupp.add_apply, Nat.Prime.factorization_self Nat.prime_two,
          Nat.factorization_eq_zero_of_not_dvd (by norm_num : ¬ (2:ℕ) ∣ 3)]
    rw [h6] at hval
    rw [if_pos rfl] at hval
    rw [if_neg (by norm_num : ¬ (2:ℕ) = 3)]
    omega
  · by_cases hp3 : p = 3
    · rw [hp3] at hval
      rw [hp3]
      have h6 : (6 : ℕ).factorization 3 = 1 := by
        rw [show (6:ℕ) = 2 * 3 by norm_num,
            Nat.factorization_mul (by norm_num : (2:ℕ) ≠ 0) (by norm_num : (3:ℕ) ≠ 0),
            Finsupp.add_apply,
            Nat.factorization_eq_zero_of_not_dvd (by norm_num : ¬ (3:ℕ) ∣ 2),
            Nat.Prime.factorization_self (by norm_num : Nat.Prime 3)]
      rw [h6] at hval
      rw [if_neg (by norm_num : ¬ (3:ℕ) = 2)] at hval
      rw [if_pos rfl]
      omega
    · rw [if_neg hp2] at hval
      rw [if_neg hp3]
      have hp_dvd2 : ¬ p ∣ 2 := by
        intro hd
        exact hp2 ((Nat.prime_dvd_prime_iff_eq hp Nat.prime_two).mp hd)
      have hp_dvd3 : ¬ p ∣ 3 := by
        intro hd
        exact hp3 ((Nat.prime_dvd_prime_iff_eq hp (by norm_num : Nat.Prime 3)).mp hd)
      have h6 : (6 : ℕ).factorization p = 0 := by
        rw [show (6:ℕ) = 2 * 3 by norm_num,
            Nat.factorization_mul (by norm_num : (2:ℕ) ≠ 0) (by norm_num : (3:ℕ) ≠ 0),
            Finsupp.add_apply,
            Nat.factorization_eq_zero_of_not_dvd hp_dvd2,
            Nat.factorization_eq_zero_of_not_dvd hp_dvd3]
      rw [h6] at hval
      omega

#print axioms factorization_mul_prime_pow
#print axioms factorization_two_of_odd
#print axioms six_mul_choose_three
#print axioms factorization_choose_three

end NestedBinomialV10
