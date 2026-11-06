import Mathlib.Tactic
import ThirtyCofactorCubePrimeExtraction


namespace NestedBinomialV10
theorem cofactor_M_cases (n : ℕ) (hn : 1 ≤ n) : Nat.gcd n 3 * Nat.gcd (n - 1) 6 = 1 ∨ Nat.gcd n 3 * Nat.gcd (n - 1) 6 = 2 ∨ Nat.gcd n 3 * Nat.gcd (n - 1) 6 = 3 ∨ Nat.gcd n 3 * Nat.gcd (n - 1) 6 = 6 := by
  generalize hA : Nat.gcd n 3 = A
  generalize hB : Nat.gcd (n - 1) 6 = B
  have hA_dvd3 : A ∣ 3 := by
    simpa [hA] using Nat.gcd_dvd_right n 3
  have hB_dvd6 : B ∣ 6 := by
    simpa [hB] using Nat.gcd_dvd_right (n - 1) 6
  have hA_dvd_n : A ∣ n := by
    simpa [hA] using Nat.gcd_dvd_left n 3
  have hB_dvd_n1 : B ∣ n - 1 := by
    simpa [hB] using Nat.gcd_dvd_left (n - 1) 6
  have hApos : 0 < A := Nat.pos_of_dvd_of_pos hA_dvd3 (by norm_num)
  have hBpos : 0 < B := Nat.pos_of_dvd_of_pos hB_dvd6 (by norm_num)
  have hAle : A ≤ 3 := Nat.le_of_dvd (by norm_num) hA_dvd3
  have hBle : B ≤ 6 := Nat.le_of_dvd (by norm_num) hB_dvd6
  have hnot_both : ¬ (A = 3 ∧ (B = 3 ∨ B = 6)) := by
    rintro ⟨hA3, hB36⟩
    have h3n : 3 ∣ n := by
      simpa [hA3] using hA_dvd_n
    have h3n1 : 3 ∣ n - 1 := by
      rcases hB36 with hB3 | hB6
      · simpa [hB3] using hB_dvd_n1
      · have h6 : 6 ∣ n - 1 := by simpa [hB6] using hB_dvd_n1
        exact (by norm_num : 3 ∣ 6).trans h6
    have hcop : Nat.Coprime n (n - 1) := by
      rw [Nat.coprime_self_sub_right hn]
      simp
    have hgcd1 : Nat.gcd n (n - 1) = 1 := by
      simpa using hcop
    have h3gcd : 3 ∣ Nat.gcd n (n - 1) := Nat.dvd_gcd h3n h3n1
    rw [hgcd1] at h3gcd
    norm_num at h3gcd
  have hAge : 1 ≤ A := by omega
  have hBge : 1 ≤ B := by omega
  interval_cases A <;> interval_cases B <;> norm_num at *

theorem L_lower_bound (n r L M : ℕ) (hM : 0 < M) (h : M * r ^ 2 = L * n * (n - 1)) (hn : 2 ≤ n) (hr : 3 * n < r) : 9 * M + 1 ≤ L := by
  have hnpos : 0 < n := by omega
  have hn1pos : 0 < n - 1 := by omega
  have hcast : ((n - 1 : ℕ) : ℚ) = (n : ℚ) - 1 := by
    rw [Nat.cast_sub (by omega : 1 ≤ n)]
    norm_num
  have hQ : (M : ℚ) * (r : ℚ) ^ 2 = (L : ℚ) * (n : ℚ) * ((n : ℚ) - 1) := by
    have h' := congrArg (fun x : ℕ => (x : ℚ)) h
    simpa [Nat.cast_mul, Nat.cast_pow, hcast, mul_assoc] using h'
  have hrQ : (3 : ℚ) * (n : ℚ) < (r : ℚ) := by
    exact_mod_cast hr
  have hnQ : (0 : ℚ) < (n : ℚ) := by
    exact_mod_cast hnpos
  have hn1Q : (0 : ℚ) < (n : ℚ) - 1 := by
    have hn1 : (1 : ℚ) < (n : ℚ) := by
      exact_mod_cast (by omega : 1 < n)
    linarith
  have hMq : (0 : ℚ) < (M : ℚ) := by
    exact_mod_cast hM
  have hr2Q : 9 * (n : ℚ) ^ 2 < (r : ℚ) ^ 2 := by
    have h1 : 0 < (r : ℚ) - 3 * (n : ℚ) := by linarith
    have h2 : 0 < (r : ℚ) + 3 * (n : ℚ) := by linarith
    have h3 : 0 < ((r : ℚ) - 3 * (n : ℚ)) * ((r : ℚ) + 3 * (n : ℚ)) :=
      mul_pos h1 h2
    nlinarith [h3]
  have hmul : 9 * (M : ℚ) * (n : ℚ) ^ 2 < (M : ℚ) * (r : ℚ) ^ 2 := by
    have h4 : (M : ℚ) * (9 * (n : ℚ) ^ 2) < (M : ℚ) * (r : ℚ) ^ 2 :=
      mul_lt_mul_of_pos_left hr2Q hMq
    calc
      9 * (M : ℚ) * (n : ℚ) ^ 2 = (M : ℚ) * (9 * (n : ℚ) ^ 2) := by ring
      _ < (M : ℚ) * (r : ℚ) ^ 2 := h4
  have hmain : 9 * (M : ℚ) * (n : ℚ) ^ 2 < (L : ℚ) * (n : ℚ) * ((n : ℚ) - 1) := by
    rw [← hQ]
    exact hmul
  have hle : (L : ℚ) * (n : ℚ) * ((n : ℚ) - 1) ≤ (L : ℚ) * (n : ℚ) ^ 2 := by
    have h1 : (n : ℚ) - 1 ≤ (n : ℚ) := by linarith
    have h2 : (0 : ℚ) ≤ (L : ℚ) * (n : ℚ) := by positivity
    calc
      (L : ℚ) * (n : ℚ) * ((n : ℚ) - 1)
          = ((L : ℚ) * (n : ℚ)) * ((n : ℚ) - 1) := by ring
      _ ≤ ((L : ℚ) * (n : ℚ)) * (n : ℚ) := mul_le_mul_of_nonneg_left h1 h2
      _ = (L : ℚ) * (n : ℚ) ^ 2 := by ring
  have hsqlt : 9 * (M : ℚ) * (n : ℚ) ^ 2 < (L : ℚ) * (n : ℚ) ^ 2 :=
    lt_of_lt_of_le hmain hle
  have hn2pos : (0 : ℚ) < (n : ℚ) ^ 2 := pow_pos hnQ 2
  have hltQ : 9 * (M : ℚ) < (L : ℚ) := by
    by_contra hcon
    push_neg at hcon
    have h1 : (n : ℚ) ^ 2 * (L : ℚ) ≤ (n : ℚ) ^ 2 * (9 * (M : ℚ)) :=
      mul_le_mul_of_nonneg_left hcon (le_of_lt hn2pos)
    nlinarith [h1, hsqlt]
  have hltNat : 9 * M < L := by
    have hcastlt : ((9 * M : ℕ) : ℚ) < (L : ℚ) := by
      simpa [Nat.cast_mul] using hltQ
    exact_mod_cast hcastlt
  omega

theorem L_upper_bound (n r L M : ℕ) (hM : 0 < M) (h : M * r ^ 2 = L * n * (n - 1)) (hn : 104 ≤ n) (hr : 3 * r < 10 * n) : 927 * L < 10400 * M := by
  have hn104Q : (104 : ℚ) ≤ (n : ℚ) := by exact_mod_cast hn
  have hnQ : (0 : ℚ) < (n : ℚ) := by linarith
  have hn1Q : (0 : ℚ) < (n : ℚ) - 1 := by linarith
  have hMq : (0 : ℚ) < (M : ℚ) := by exact_mod_cast hM
  have hcast : ((n - 1 : ℕ) : ℚ) = (n : ℚ) - 1 := by
    rw [Nat.cast_sub (by omega : 1 ≤ n)]
    norm_num
  have hQ : (M : ℚ) * (r : ℚ) ^ 2 = (L : ℚ) * (n : ℚ) * ((n : ℚ) - 1) := by
    have h' := congrArg (fun x : ℕ => (x : ℚ)) h
    simpa [Nat.cast_mul, Nat.cast_pow, hcast, mul_assoc] using h'
  have hrQ : (3 : ℚ) * (r : ℚ) < 10 * (n : ℚ) := by
    exact_mod_cast hr
  have hsq : 9 * (r : ℚ) ^ 2 < 100 * (n : ℚ) ^ 2 := by
    have h1 : 0 < 10 * (n : ℚ) - 3 * (r : ℚ) := by linarith
    have hrnonneg : (0 : ℚ) ≤ (r : ℚ) := by positivity
    have h2 : 0 < 10 * (n : ℚ) + 3 * (r : ℚ) := by nlinarith [hnQ, hrnonneg]
    have hprod : 0 < (10 * (n : ℚ) - 3 * (r : ℚ)) *
        (10 * (n : ℚ) + 3 * (r : ℚ)) := mul_pos h1 h2
    nlinarith [hprod]
  have hmul : 9 * (M : ℚ) * (r : ℚ) ^ 2 < 100 * (M : ℚ) * (n : ℚ) ^ 2 := by
    have hmul0 : (M : ℚ) * (9 * (r : ℚ) ^ 2) <
        (M : ℚ) * (100 * (n : ℚ) ^ 2) :=
      mul_lt_mul_of_pos_left hsq hMq
    calc
      9 * (M : ℚ) * (r : ℚ) ^ 2 = (M : ℚ) * (9 * (r : ℚ) ^ 2) := by ring
      _ < (M : ℚ) * (100 * (n : ℚ) ^ 2) := hmul0
      _ = 100 * (M : ℚ) * (n : ℚ) ^ 2 := by ring
  have hQ9 : 9 * (M : ℚ) * (r : ℚ) ^ 2 =
      9 * (L : ℚ) * (n : ℚ) * ((n : ℚ) - 1) := by
    calc
      9 * (M : ℚ) * (r : ℚ) ^ 2 = 9 * ((M : ℚ) * (r : ℚ) ^ 2) := by ring
      _ = 9 * ((L : ℚ) * (n : ℚ) * ((n : ℚ) - 1)) := by rw [hQ]
      _ = 9 * (L : ℚ) * (n : ℚ) * ((n : ℚ) - 1) := by ring
  have hmain0 : 9 * (L : ℚ) * (n : ℚ) * ((n : ℚ) - 1) <
      100 * (M : ℚ) * (n : ℚ) ^ 2 := by
    rw [← hQ9]
    exact hmul
  have hmain : 9 * (L : ℚ) * ((n : ℚ) - 1) < 100 * (M : ℚ) * (n : ℚ) := by
    have hfac : (n : ℚ) * (9 * (L : ℚ) * ((n : ℚ) - 1)) <
        (n : ℚ) * (100 * (M : ℚ) * (n : ℚ)) := by
      calc
        (n : ℚ) * (9 * (L : ℚ) * ((n : ℚ) - 1)) =
            9 * (L : ℚ) * (n : ℚ) * ((n : ℚ) - 1) := by ring
        _ < 100 * (M : ℚ) * (n : ℚ) ^ 2 := hmain0
        _ = (n : ℚ) * (100 * (M : ℚ) * (n : ℚ)) := by ring
    exact lt_of_mul_lt_mul_left hfac (le_of_lt hnQ)
  have hnratio : 103 * (n : ℚ) ≤ 104 * ((n : ℚ) - 1) := by
    nlinarith [hn104Q]
  have h103 : 927 * (L : ℚ) * ((n : ℚ) - 1) < 10300 * (M : ℚ) * (n : ℚ) := by
    calc
      927 * (L : ℚ) * ((n : ℚ) - 1) =
          103 * (9 * (L : ℚ) * ((n : ℚ) - 1)) := by ring
      _ < 103 * (100 * (M : ℚ) * (n : ℚ)) := by
        exact mul_lt_mul_of_pos_left hmain (by norm_num)
      _ = 10300 * (M : ℚ) * (n : ℚ) := by ring
  have hmulratio : 10300 * (M : ℚ) * (n : ℚ) ≤
      10400 * (M : ℚ) * ((n : ℚ) - 1) := by
    have h100 : (0 : ℚ) ≤ 100 * (M : ℚ) := by positivity
    have hm : 100 * (M : ℚ) * (103 * (n : ℚ)) ≤
        100 * (M : ℚ) * (104 * ((n : ℚ) - 1)) :=
      mul_le_mul_of_nonneg_left hnratio h100
    calc
      10300 * (M : ℚ) * (n : ℚ) = 100 * (M : ℚ) * (103 * (n : ℚ)) := by ring
      _ ≤ 100 * (M : ℚ) * (104 * ((n : ℚ) - 1)) := hm
      _ = 10400 * (M : ℚ) * ((n : ℚ) - 1) := by ring
  have hchain : 927 * (L : ℚ) * ((n : ℚ) - 1) <
      10400 * (M : ℚ) * ((n : ℚ) - 1) :=
    lt_of_lt_of_le h103 hmulratio
  have htargetQ : 927 * (L : ℚ) < 10400 * (M : ℚ) :=
    lt_of_mul_lt_mul_right hchain (le_of_lt hn1Q)
  have hcastlt : ((927 * L : ℕ) : ℚ) < ((10400 * M : ℕ) : ℚ) := by
    simpa [Nat.cast_mul] using htargetQ
  exact_mod_cast hcastlt

theorem Q_dvd_sq_pair_covering (n r L : ℕ) (hn : 104 ≤ n) (hrlo : 3 * n < r) (hrhi : 3 * r < 10 * n) (hL : L * ((n / Nat.gcd n 3) * ((n - 1) / Nat.gcd (n - 1) 6)) = r ^ 2) : (Nat.gcd n 3 * Nat.gcd (n - 1) 6 = 1 ∧ 10 ≤ L ∧ L ≤ 11) ∨ (Nat.gcd n 3 * Nat.gcd (n - 1) 6 = 2 ∧ 19 ≤ L ∧ L ≤ 22) ∨ (Nat.gcd n 3 * Nat.gcd (n - 1) 6 = 3 ∧ 28 ≤ L ∧ L ≤ 33) ∨ (Nat.gcd n 3 * Nat.gcd (n - 1) 6 = 6 ∧ 55 ≤ L ∧ L ≤ 67) := by
  have hMcases := cofactor_M_cases n (by omega : 1 ≤ n)
  have hEq := cofactor_M_mul_sq n r L hL
  rcases hMcases with hM | hM | hM | hM
  · left
    have hMpos : 0 < Nat.gcd n 3 * Nat.gcd (n - 1) 6 := by
      rw [hM]
      norm_num
    have hlow := L_lower_bound n r L (Nat.gcd n 3 * Nat.gcd (n - 1) 6) hMpos hEq (by omega : 2 ≤ n) hrlo
    have hup := L_upper_bound n r L (Nat.gcd n 3 * Nat.gcd (n - 1) 6) hMpos hEq hn hrhi
    refine ⟨hM, ?_⟩
    refine ⟨?_, ?_⟩
    · have h := hlow
      rw [hM] at h
      norm_num at h
      exact h
    · have h := hup
      rw [hM] at h
      norm_num at h
      omega
  · right
    left
    have hMpos : 0 < Nat.gcd n 3 * Nat.gcd (n - 1) 6 := by
      rw [hM]
      norm_num
    have hlow := L_lower_bound n r L (Nat.gcd n 3 * Nat.gcd (n - 1) 6) hMpos hEq (by omega : 2 ≤ n) hrlo
    have hup := L_upper_bound n r L (Nat.gcd n 3 * Nat.gcd (n - 1) 6) hMpos hEq hn hrhi
    refine ⟨hM, ?_⟩
    refine ⟨?_, ?_⟩
    · have h := hlow
      rw [hM] at h
      norm_num at h
      exact h
    · have h := hup
      rw [hM] at h
      norm_num at h
      omega
  · right
    right
    left
    have hMpos : 0 < Nat.gcd n 3 * Nat.gcd (n - 1) 6 := by
      rw [hM]
      norm_num
    have hlow := L_lower_bound n r L (Nat.gcd n 3 * Nat.gcd (n - 1) 6) hMpos hEq (by omega : 2 ≤ n) hrlo
    have hup := L_upper_bound n r L (Nat.gcd n 3 * Nat.gcd (n - 1) 6) hMpos hEq hn hrhi
    refine ⟨hM, ?_⟩
    refine ⟨?_, ?_⟩
    · have h := hlow
      rw [hM] at h
      norm_num at h
      exact h
    · have h := hup
      rw [hM] at h
      norm_num at h
      omega
  · right
    right
    right
    have hMpos : 0 < Nat.gcd n 3 * Nat.gcd (n - 1) 6 := by
      rw [hM]
      norm_num
    have hlow := L_lower_bound n r L (Nat.gcd n 3 * Nat.gcd (n - 1) 6) hMpos hEq (by omega : 2 ≤ n) hrlo
    have hup := L_upper_bound n r L (Nat.gcd n 3 * Nat.gcd (n - 1) 6) hMpos hEq hn hrhi
    refine ⟨hM, ?_⟩
    refine ⟨?_, ?_⟩
    · have h := hlow
      rw [hM] at h
      norm_num at h
      exact h
    · have h := hup
      rw [hM] at h
      norm_num at h
      omega

#print axioms cofactor_M_cases
#print axioms L_lower_bound
#print axioms L_upper_bound
#print axioms Q_dvd_sq_pair_covering

end NestedBinomialV10
