import Mathlib.Tactic


namespace NestedBinomialV10
theorem cofactor_one_dvd_choose_three (n : ℕ) (hn : 1 ≤ n) : (n - 1) / Nat.gcd (n - 1) 6 ∣ n.choose 3 := by
  by_cases hn3 : n < 3
  · rw [Nat.choose_eq_zero_of_lt hn3]
    exact dvd_zero _
  · have hn3' : 3 ≤ n := by omega
    set g := Nat.gcd (n - 1) 6 with hg_eq
    set q := (n - 1) / g with hq_eq
    set h := 6 / g with hh_eq
    have hg_dvd_n1 : g ∣ n - 1 := by
      rw [hg_eq]
      exact Nat.gcd_dvd_left _ _
    have hg_dvd_6 : g ∣ 6 := by
      rw [hg_eq]
      exact Nat.gcd_dvd_right _ _
    have hg_pos : 0 < g := by
      rw [hg_eq]
      exact Nat.gcd_pos_of_pos_right _ (by norm_num)
    have hq_mul : g * q = n - 1 := by
      rw [hq_eq]
      exact Nat.mul_div_cancel' hg_dvd_n1
    have hh_mul : g * h = 6 := by
      rw [hh_eq]
      exact Nat.mul_div_cancel' hg_dvd_6
    have two_dvd_of_coprime : Nat.Coprime (n - 1) 2 → 2 ∣ n * (n - 2) := by
      intro hcop
      have hp2 : Nat.Prime 2 := by norm_num
      have hnot : ¬ 2 ∣ n - 1 := (hp2.coprime_iff_not_dvd).mp hcop.symm
      have hmod0 : (n - 1) % 2 ≠ 0 := by
        intro h0
        exact hnot ((Nat.dvd_iff_mod_eq_zero).mpr h0)
      have hmod : (n - 1) % 2 = 1 := by
        have hlt := Nat.mod_lt (n - 1) (by norm_num : 0 < 2)
        omega
      obtain ⟨k, hk⟩ : ∃ k, n - 1 = 2 * k + 1 := by
        refine ⟨(n - 1) / 2, ?_⟩
        have hdm := Nat.div_add_mod (n - 1) 2
        omega
      have hn : n = 2 * k + 2 := by omega
      have hn2' : 2 * k + 2 - 2 = 2 * k := by omega
      rw [hn, hn2']
      use 2 * k * (k + 1)
      ring
    have three_dvd_of_coprime : Nat.Coprime (n - 1) 3 → 3 ∣ n * (n - 2) := by
      intro hcop
      have hp3 : Nat.Prime 3 := by norm_num
      have hnot : ¬ 3 ∣ n - 1 := (hp3.coprime_iff_not_dvd).mp hcop.symm
      have hmod0 : (n - 1) % 3 ≠ 0 := by
        intro h0
        exact hnot ((Nat.dvd_iff_mod_eq_zero).mpr h0)
      have hmod : (n - 1) % 3 = 1 ∨ (n - 1) % 3 = 2 := by
        have hlt := Nat.mod_lt (n - 1) (by norm_num : 0 < 3)
        omega
      rcases hmod with h1 | h2
      · obtain ⟨k, hk⟩ : ∃ k, n - 1 = 3 * k + 1 := by
          refine ⟨(n - 1) / 3, ?_⟩
          have hdm := Nat.div_add_mod (n - 1) 3
          omega
        have hn : n = 3 * k + 2 := by omega
        have hn2' : 3 * k + 2 - 2 = 3 * k := by omega
        rw [hn, hn2']
        use k * (3 * k + 2)
        ring
      · obtain ⟨k, hk⟩ : ∃ k, n - 1 = 3 * k + 2 := by
          refine ⟨(n - 1) / 3, ?_⟩
          have hdm := Nat.div_add_mod (n - 1) 3
          omega
        have hn : n = 3 * k + 3 := by omega
        have hn2' : 3 * k + 3 - 2 = 3 * k + 1 := by omega
        rw [hn, hn2']
        use (k + 1) * (3 * k + 1)
        ring
    have hdiv : h ∣ n * (n - 2) := by
      have hg_le : g ≤ 6 := Nat.le_of_dvd (by norm_num) hg_dvd_6
      interval_cases g
      · have hcop6 : Nat.Coprime (n - 1) 6 := Nat.coprime_iff_gcd_eq_one.mpr hg_eq.symm
        have h2 : 2 ∣ n * (n - 2) := two_dvd_of_coprime (hcop6.of_dvd_right (by norm_num : 2 ∣ 6))
        have h3 : 3 ∣ n * (n - 2) := three_dvd_of_coprime (hcop6.of_dvd_right (by norm_num : 3 ∣ 6))
        have hh : h = 6 := by omega
        rw [hh]
        obtain ⟨a, ha⟩ := h2
        have h3a : 3 ∣ a := by
          have h3' : 3 ∣ 2 * a := by simpa [ha] using h3
          exact (by norm_num : Nat.Coprime 3 2).dvd_of_dvd_mul_left h3'
        obtain ⟨b, hb⟩ := h3a
        use b
        rw [ha, hb]
        ring
      · have h3not : ¬ 3 ∣ n - 1 := by
          intro h3dvd
          have h3dvdgcd : 3 ∣ Nat.gcd (n - 1) 6 := Nat.dvd_gcd h3dvd (by norm_num : 3 ∣ 6)
          rw [← hg_eq] at h3dvdgcd
          exact (by norm_num : ¬ 3 ∣ 2) h3dvdgcd
        have hcop3 : Nat.Coprime (n - 1) 3 := by
          have hp3 : Nat.Prime 3 := by norm_num
          exact ((hp3.coprime_iff_not_dvd).mpr h3not).symm
        have hh : h = 3 := by omega
        rw [hh]
        exact three_dvd_of_coprime hcop3
      · have h2not : ¬ 2 ∣ n - 1 := by
          intro h2dvd
          have h2dvdgcd : 2 ∣ Nat.gcd (n - 1) 6 := Nat.dvd_gcd h2dvd (by norm_num : 2 ∣ 6)
          rw [← hg_eq] at h2dvdgcd
          exact (by norm_num : ¬ 2 ∣ 3) h2dvdgcd
        have hcop2 : Nat.Coprime (n - 1) 2 := by
          have hp2 : Nat.Prime 2 := by norm_num
          exact ((hp2.coprime_iff_not_dvd).mpr h2not).symm
        have hh : h = 2 := by omega
        rw [hh]
        exact two_dvd_of_coprime hcop2
      · exfalso
        exact (by norm_num : ¬ 4 ∣ 6) hg_dvd_6
      · exfalso
        exact (by norm_num : ¬ 5 ∣ 6) hg_dvd_6
      · have hh : h = 1 := by omega
        rw [hh]
        exact one_dvd _
    have h6q : 6 * q = h * (n - 1) := by
      calc
        6 * q = (g * h) * q := by rw [← hh_mul]
        _ = h * (g * q) := by ring
        _ = h * (n - 1) := by rw [hq_mul]
    have hprod_dvd : 6 * q ∣ n * (n - 1) * (n - 2) := by
      rw [h6q]
      have := Nat.mul_dvd_mul_right hdiv (n - 1)
      simpa [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using this
    have hchoose_eq : 6 * n.choose 3 = n * (n - 1) * (n - 2) := by
      have hd := Nat.descFactorial_eq_factorial_mul_choose n 3
      simp [Nat.descFactorial] at hd
      norm_num at hd
      rw [← hd]
      ring
    have h6C_dvd : 6 * q ∣ 6 * n.choose 3 := by
      rw [hchoose_eq]
      exact hprod_dvd
    exact (Nat.mul_dvd_mul_iff_left (by norm_num : 0 < 6)).mp h6C_dvd

theorem choose_squared_two_dvd (n : ℕ) : (n - 1) ∣ (n ^ 2).choose 2 := by
  have hsq : n ^ 2 - 1 = (n - 1) * (n + 1) := by
    simpa [Nat.mul_comm] using Nat.sq_sub_sq n 1
  have heven : 2 ∣ n ^ 2 * (n + 1) := by
    rcases Nat.even_or_odd n with ⟨k, hk⟩ | ⟨k, hk⟩
    · rw [hk]
      exact ⟨2 * k ^ 2 * (k + k + 1), by ring⟩
    · rw [hk]
      exact ⟨(2 * k + 1) ^ 2 * (k + 1), by ring⟩
  obtain ⟨m, hm⟩ := heven
  have h2 : 2 ∣ n ^ 2 * (n ^ 2 - 1) := by
    rw [hsq]
    rw [show n ^ 2 * ((n - 1) * (n + 1)) = (n - 1) * (n ^ 2 * (n + 1)) by ring]
    rw [hm]
    exact ⟨(n - 1) * m, by ring⟩
  rw [Nat.choose_two_right, Nat.dvd_div_iff_mul_dvd h2]
  rw [hsq]
  rw [show n ^ 2 * ((n - 1) * (n + 1)) = (n - 1) * (n ^ 2 * (n + 1)) by ring]
  rw [hm]
  exact ⟨m, by ring⟩

theorem choose_shift_two_congruent_six (n : ℕ) (hn : 5 ≤ n) : (n - 1) ∣ ((n - 3) ^ 2).choose 2 - 6 := by
  set m := (n - 3) ^ 2 with hm
  have hm4 : 4 ≤ m := by
    rw [hm]
    have h2 : 2 ≤ n - 3 := by omega
    calc
      4 = 2 ^ 2 := by norm_num
      _ ≤ (n - 3) ^ 2 := Nat.pow_le_pow_left h2 2
  have h2dvd : 2 ∣ m * (m - 1) := by
    rcases Nat.even_or_odd m with ⟨k, hk⟩ | ⟨k, hk⟩
    · refine ⟨k * (m - 1), ?_⟩
      calc
        m * (m - 1) = (k + k) * (m - 1) := by rw [hk]
        _ = 2 * (k * (m - 1)) := by ring
    · have hm1 : m - 1 = 2 * k := by omega
      refine ⟨(2 * k + 1) * k, ?_⟩
      calc
        m * (m - 1) = (2 * k + 1) * (2 * k) := by rw [hm1, hk]
        _ = 2 * ((2 * k + 1) * k) := by ring
  have hC : 2 * m.choose 2 = m * (m - 1) := by
    rw [Nat.choose_two_right]
    exact Nat.mul_div_cancel' h2dvd
  have hpoly : m * (m - 1) - 12 = (m - 4) * (m + 3) := by
    set r := m - 4 with hr
    have hm' : m = r + 4 := by omega
    rw [hm']
    have h1 : r + 4 - 1 = r + 3 := by omega
    rw [h1]
    have hleft : (r + 4) * (r + 3) = r * (r + 7) + 12 := by ring
    have hright : r * (r + 4 + 3) = r * (r + 7) := by ring
    rw [hleft, hright]
    exact Nat.add_sub_cancel _ _
  have h2eq : 2 * (m.choose 2 - 6) = (m - 4) * (m + 3) := by
    calc
      2 * (m.choose 2 - 6) = 2 * m.choose 2 - 12 := by
        rw [Nat.mul_sub_left_distrib]
      _ = m * (m - 1) - 12 := by rw [hC]
      _ = (m - 4) * (m + 3) := hpoly
  have hchoose : m.choose 2 - 6 = ((m - 4) * (m + 3)) / 2 :=
    Nat.eq_div_of_mul_eq_right (by norm_num : (2 : ℕ) ≠ 0) h2eq
  have h2dvdN : 2 ∣ (m - 4) * (m + 3) := ⟨m.choose 2 - 6, h2eq.symm⟩
  have hm4eq : m - 4 = (n - 1) * (n - 5) := by
    rw [hm]
    have hsq := Nat.sq_sub_sq (n - 3) 2
    norm_num at hsq
    rw [hsq]
    have h1 : n - 3 - 2 = n - 5 := by omega
    have h2 : n - 3 + 2 = n - 1 := by omega
    rw [h1, h2]
  have hpar : 2 ∣ (n - 5) * (m + 3) := by
    rcases Nat.even_or_odd n with ⟨k, hk⟩ | ⟨k, hk⟩
    · have hk3 : 3 ≤ k := by omega
      set r := k - 3 with hr
      have hk' : k = r + 3 := by omega
      have hn5 : n - 5 = 2 * r + 1 := by omega
      have hmval : m = (2 * r + 3) ^ 2 := by
        rw [hm]
        have hn3 : n - 3 = 2 * r + 3 := by omega
        rw [hn3]
      rw [hn5, hmval]
      refine ⟨2 * (2 * r + 1) * (r ^ 2 + 3 * r + 3), ?_⟩
      ring
    · have hk2 : 2 ≤ k := by omega
      set r := k - 2 with hr
      have hk' : k = r + 2 := by omega
      have hn5 : n - 5 = 2 * r := by omega
      rw [hn5]
      refine ⟨r * (m + 3), ?_⟩
      ring
  rw [hchoose]
  rw [Nat.dvd_div_iff_mul_dvd h2dvdN]
  rw [hm4eq]
  obtain ⟨q, hq⟩ := hpar
  refine ⟨q, ?_⟩
  calc
    ((n - 1) * (n - 5)) * (m + 3) = (n - 1) * ((n - 5) * (m + 3)) := by ring
    _ = (n - 1) * (2 * q) := by rw [hq]
    _ = (2 * (n - 1)) * q := by ring

theorem cofactor_one_dvd_squared_index_choose (n : ℕ) (hn : 5 ≤ n) : (n - 1) / Nat.gcd (n - 1) 6 ∣ (n ^ 2).choose ((n - 3) ^ 2) := by
  set t := n - 1 with ht
  set m := (n - 3) ^ 2 with hm
  set X := (n ^ 2).choose m with hX
  set g := Nat.gcd t 6 with hg
  set q := t / g with hq
  have hgpos : 0 < g := by
    rw [hg]
    exact Nat.gcd_pos_of_pos_right t (by norm_num)
  have hgdvdt : g ∣ t := by
    rw [hg]
    exact Nat.gcd_dvd_left _ _
  have hgdvd6 : g ∣ 6 := by
    rw [hg]
    exact Nat.gcd_dvd_right _ _
  have ht_eq : g * q = t := by
    rw [hq]
    exact Nat.mul_div_cancel' hgdvdt
  have h6_eq : g * (6 / g) = 6 := Nat.mul_div_cancel' hgdvd6
  have hm4 : 4 ≤ m := by
    rw [hm]
    have h2 : 2 ≤ n - 3 := by omega
    calc
      4 = 2 ^ 2 := by norm_num
      _ ≤ (n - 3) ^ 2 := Nat.pow_le_pow_left h2 2
  have hm2 : 2 ≤ m := by omega
  have hC2dvd : t ∣ (n ^ 2).choose 2 := by
    rw [ht]
    exact choose_squared_two_dvd n
  have hshift : t ∣ m.choose 2 - 6 := by
    rw [ht, hm]
    exact choose_shift_two_congruent_six n hn
  have hchoose_mul :
      X * m.choose 2 = (n ^ 2).choose 2 * (n ^ 2 - 2).choose (m - 2) := by
    rw [hX]
    exact Nat.choose_mul (n := n ^ 2) (k := m) (s := 2) hm2
  have hXm : t ∣ X * m.choose 2 := by
    rw [hchoose_mul]
    exact dvd_mul_of_dvd_left hC2dvd _
  have hXdiff : t ∣ X * (m.choose 2 - 6) :=
    dvd_mul_of_dvd_right hshift X
  have hC_ge6 : 6 ≤ m.choose 2 := by
    have h4 : (4 : ℕ).choose 2 ≤ m.choose 2 := Nat.choose_le_choose 2 hm4
    have h4' : (4 : ℕ).choose 2 = 6 := by decide
    simpa [h4'] using h4
  have hX6 : t ∣ X * 6 := by
    have hdecomp : X * m.choose 2 = X * 6 + X * (m.choose 2 - 6) := by
      have hsum : 6 + (m.choose 2 - 6) = m.choose 2 := by omega
      calc
        X * m.choose 2 = X * (6 + (m.choose 2 - 6)) := by rw [hsum]
        _ = X * 6 + X * (m.choose 2 - 6) := by rw [Nat.mul_add]
    rw [hdecomp] at hXm
    exact (Nat.dvd_add_iff_left hXdiff).mpr hXm
  have hq_dvd_hX : q ∣ X * (6 / g) := by
    have hmul : g * q ∣ X * (g * (6 / g)) := by
      rw [ht_eq, h6_eq]
      exact hX6
    have hmul' : g * q ∣ g * (X * (6 / g)) := by
      simpa [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using hmul
    exact (Nat.mul_dvd_mul_iff_left hgpos).mp hmul'
  have hcop : Nat.Coprime q (6 / g) := by
    rw [hq, hg]
    exact Nat.coprime_div_gcd_div_gcd (Nat.gcd_pos_of_pos_right t (by norm_num))
  have hq_dvd_X : q ∣ X := by
    have hq_dvd_hX' : q ∣ (6 / g) * X := by
      simpa [Nat.mul_comm] using hq_dvd_hX
    exact hcop.dvd_of_dvd_mul_left hq_dvd_hX'
  exact hq_dvd_X

#print axioms cofactor_one_dvd_choose_three
#print axioms choose_squared_two_dvd
#print axioms choose_shift_two_congruent_six
#print axioms cofactor_one_dvd_squared_index_choose

end NestedBinomialV10
