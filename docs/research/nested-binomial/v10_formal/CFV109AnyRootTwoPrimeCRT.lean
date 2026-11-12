import Mathlib.Tactic
import Mathlib.Data.Nat.Choose.Lucas

/-!
# v109: exact two-prime CRT exclusions even if both primes have extra roots

Each theorem assumes the already established non-formalized cubic height
i < k^3 and proves the original fixed-j=1,ell=k-1 equation false.

No global search over the original integer i. Root classifications are
verified by kernel decision over the complete finite field Fin q.
The 4-variable equation and the general cubic-height theorem
are NOT formalized in this file.
-/

namespace NestedBinomialV109

private theorem choose_mod_6_29 (i : ℕ) :
    (Nat.choose i 6) % 29 = (Nat.choose (i % 29) 6) % 29 := by
  haveI : Fact (Nat.Prime 29) := ⟨by norm_num⟩
  have h := Choose.choose_modEq_choose_mod_mul_choose_div_nat
    (n := i) (k := 6) (p := 29)
  change (Nat.choose i 6) % 29 =
    (Nat.choose (i % 29) (6 % 29) *
      Nat.choose (i / 29) (6 / 29)) % 29 at h
  simpa using h

private theorem rhs_mod_6_29 :
    (Nat.choose 36 11) % 29 = 0 := by decide

private theorem roots_6_29 :
    ∀ x : Fin 29,
      (Nat.choose (x : ℕ) 6) % 29 = (x : ℕ) ^ 2 % 29 →
      (x : ℕ) = 0 ∨ (x : ℕ) = 28 := by
  decide

private theorem choose_mod_6_31 (i : ℕ) :
    (Nat.choose i 6) % 31 = (Nat.choose (i % 31) 6) % 31 := by
  haveI : Fact (Nat.Prime 31) := ⟨by norm_num⟩
  have h := Choose.choose_modEq_choose_mod_mul_choose_div_nat
    (n := i) (k := 6) (p := 31)
  change (Nat.choose i 6) % 31 =
    (Nat.choose (i % 31) (6 % 31) *
      Nat.choose (i / 31) (6 / 31)) % 31 at h
  simpa using h

private theorem rhs_mod_6_31 :
    (Nat.choose 36 11) % 31 = 0 := by decide

private theorem roots_6_31 :
    ∀ x : Fin 31,
      (Nat.choose (x : ℕ) 6) % 31 = (x : ℕ) ^ 2 % 31 →
      (x : ℕ) = 0 ∨ (x : ℕ) = 11 ∨ (x : ℕ) = 30 := by
  decide

/-- With only the two stated modular primes, every positive i<216 is
excluded from the ORIGINAL j=1,ell=5,k=6 equation.
The global bound i<216 is an explicit hypothesis. -/
theorem k6_no_original_solution_below_cubic
    (i : ℕ) (hpos : 0 < i) (hsmall : i < 216)
    (heq : Nat.choose i 6 = i ^ 2 + Nat.choose 36 11) :
    False := by
  have h29 : (Nat.choose i 6) % 29 = (i ^ 2) % 29 := by
    have h := congrArg (fun t : ℕ => t % 29) heq
    simpa [Nat.add_mod, rhs_mod_6_29] using h
  have h29prime : (Nat.choose (i % 29) 6) % 29 =
      ((i % 29) ^ 2) % 29 := by
    calc
      _ = (Nat.choose i 6) % 29 := (choose_mod_6_29 i).symm
      _ = (i ^ 2) % 29 := h29
      _ = ((i % 29) ^ 2) % 29 := by simp [Nat.pow_mod]
  have hres29 : i % 29 = 0 ∨ i % 29 = 28 := by
    exact roots_6_29
      ⟨i % 29, Nat.mod_lt i (by decide)⟩ h29prime
  have h31 : (Nat.choose i 6) % 31 = (i ^ 2) % 31 := by
    have h := congrArg (fun t : ℕ => t % 31) heq
    simpa [Nat.add_mod, rhs_mod_6_31] using h
  have h31prime : (Nat.choose (i % 31) 6) % 31 =
      ((i % 31) ^ 2) % 31 := by
    calc
      _ = (Nat.choose i 6) % 31 := (choose_mod_6_31 i).symm
      _ = (i ^ 2) % 31 := h31
      _ = ((i % 31) ^ 2) % 31 := by simp [Nat.pow_mod]
  have hres31 : i % 31 = 0 ∨ i % 31 = 11 ∨ i % 31 = 30 := by
    exact roots_6_31
      ⟨i % 31, Nat.mod_lt i (by decide)⟩ h31prime
  rcases hres29 with ha | ha
  · rcases hres31 with hb | hb | hb <;> omega
  · rcases hres31 with hb | hb | hb <;> omega

private theorem choose_mod_9_23 (i : ℕ) :
    (Nat.choose i 9) % 23 = (Nat.choose (i % 23) 9) % 23 := by
  haveI : Fact (Nat.Prime 23) := ⟨by norm_num⟩
  have h := Choose.choose_modEq_choose_mod_mul_choose_div_nat
    (n := i) (k := 9) (p := 23)
  change (Nat.choose i 9) % 23 =
    (Nat.choose (i % 23) (9 % 23) *
      Nat.choose (i / 23) (9 / 23)) % 23 at h
  simpa using h

private theorem rhs_mod_9_23 :
    (Nat.choose 81 17) % 23 = 0 := by decide

private theorem roots_9_23 :
    ∀ x : Fin 23,
      (Nat.choose (x : ℕ) 9) % 23 = (x : ℕ) ^ 2 % 23 →
      (x : ℕ) = 0 := by
  decide

private theorem choose_mod_9_79 (i : ℕ) :
    (Nat.choose i 9) % 79 = (Nat.choose (i % 79) 9) % 79 := by
  haveI : Fact (Nat.Prime 79) := ⟨by norm_num⟩
  have h := Choose.choose_modEq_choose_mod_mul_choose_div_nat
    (n := i) (k := 9) (p := 79)
  change (Nat.choose i 9) % 79 =
    (Nat.choose (i % 79) (9 % 79) *
      Nat.choose (i / 79) (9 / 79)) % 79 at h
  simpa using h

private theorem rhs_mod_9_79 :
    (Nat.choose 81 17) % 79 = 0 := by decide

private theorem roots_9_79 :
    ∀ x : Fin 79,
      (Nat.choose (x : ℕ) 9) % 79 = (x : ℕ) ^ 2 % 79 →
      (x : ℕ) = 0 := by
  decide

/-- With only the two stated modular primes, every positive i<729 is
excluded from the ORIGINAL j=1,ell=8,k=9 equation.
The global bound i<729 is an explicit hypothesis. -/
theorem k9_no_original_solution_below_cubic
    (i : ℕ) (hpos : 0 < i) (hsmall : i < 729)
    (heq : Nat.choose i 9 = i ^ 2 + Nat.choose 81 17) :
    False := by
  have h23 : (Nat.choose i 9) % 23 = (i ^ 2) % 23 := by
    have h := congrArg (fun t : ℕ => t % 23) heq
    simpa [Nat.add_mod, rhs_mod_9_23] using h
  have h23prime : (Nat.choose (i % 23) 9) % 23 =
      ((i % 23) ^ 2) % 23 := by
    calc
      _ = (Nat.choose i 9) % 23 := (choose_mod_9_23 i).symm
      _ = (i ^ 2) % 23 := h23
      _ = ((i % 23) ^ 2) % 23 := by simp [Nat.pow_mod]
  have hres23 : i % 23 = 0 := by
    exact roots_9_23
      ⟨i % 23, Nat.mod_lt i (by decide)⟩ h23prime
  have h79 : (Nat.choose i 9) % 79 = (i ^ 2) % 79 := by
    have h := congrArg (fun t : ℕ => t % 79) heq
    simpa [Nat.add_mod, rhs_mod_9_79] using h
  have h79prime : (Nat.choose (i % 79) 9) % 79 =
      ((i % 79) ^ 2) % 79 := by
    calc
      _ = (Nat.choose i 9) % 79 := (choose_mod_9_79 i).symm
      _ = (i ^ 2) % 79 := h79
      _ = ((i % 79) ^ 2) % 79 := by simp [Nat.pow_mod]
  have hres79 : i % 79 = 0 := by
    exact roots_9_79
      ⟨i % 79, Nat.mod_lt i (by decide)⟩ h79prime
  have ha : i % 23 = 0 := hres23
  rcases hres79 with hb <;> omega

private theorem choose_mod_14_191 (i : ℕ) :
    (Nat.choose i 14) % 191 = (Nat.choose (i % 191) 14) % 191 := by
  haveI : Fact (Nat.Prime 191) := ⟨by norm_num⟩
  have h := Choose.choose_modEq_choose_mod_mul_choose_div_nat
    (n := i) (k := 14) (p := 191)
  change (Nat.choose i 14) % 191 =
    (Nat.choose (i % 191) (14 % 191) *
      Nat.choose (i / 191) (14 / 191)) % 191 at h
  simpa using h

private theorem rhs_mod_14_191 :
    (Nat.choose 196 27) % 191 = 0 := by decide

private theorem roots_14_191 :
    ∀ x : Fin 191,
      (Nat.choose (x : ℕ) 14) % 191 = (x : ℕ) ^ 2 % 191 →
      (x : ℕ) = 0 ∨ (x : ℕ) = 62 ∨ (x : ℕ) = 190 := by
  decide

private theorem choose_mod_14_181 (i : ℕ) :
    (Nat.choose i 14) % 181 = (Nat.choose (i % 181) 14) % 181 := by
  haveI : Fact (Nat.Prime 181) := ⟨by norm_num⟩
  have h := Choose.choose_modEq_choose_mod_mul_choose_div_nat
    (n := i) (k := 14) (p := 181)
  change (Nat.choose i 14) % 181 =
    (Nat.choose (i % 181) (14 % 181) *
      Nat.choose (i / 181) (14 / 181)) % 181 at h
  simpa using h

private theorem rhs_mod_14_181 :
    (Nat.choose 196 27) % 181 = 0 := by decide

private theorem roots_14_181 :
    ∀ x : Fin 181,
      (Nat.choose (x : ℕ) 14) % 181 = (x : ℕ) ^ 2 % 181 →
      (x : ℕ) = 0 ∨ (x : ℕ) = 170 ∨ (x : ℕ) = 180 := by
  decide

/-- With only the two stated modular primes, every positive i<2744 is
excluded from the ORIGINAL j=1,ell=13,k=14 equation.
The global bound i<2744 is an explicit hypothesis. -/
theorem k14_no_original_solution_below_cubic
    (i : ℕ) (hpos : 0 < i) (hsmall : i < 2744)
    (heq : Nat.choose i 14 = i ^ 2 + Nat.choose 196 27) :
    False := by
  have h191 : (Nat.choose i 14) % 191 = (i ^ 2) % 191 := by
    have h := congrArg (fun t : ℕ => t % 191) heq
    simpa [Nat.add_mod, rhs_mod_14_191] using h
  have h191prime : (Nat.choose (i % 191) 14) % 191 =
      ((i % 191) ^ 2) % 191 := by
    calc
      _ = (Nat.choose i 14) % 191 := (choose_mod_14_191 i).symm
      _ = (i ^ 2) % 191 := h191
      _ = ((i % 191) ^ 2) % 191 := by simp [Nat.pow_mod]
  have hres191 : i % 191 = 0 ∨ i % 191 = 62 ∨ i % 191 = 190 := by
    exact roots_14_191
      ⟨i % 191, Nat.mod_lt i (by decide)⟩ h191prime
  have h181 : (Nat.choose i 14) % 181 = (i ^ 2) % 181 := by
    have h := congrArg (fun t : ℕ => t % 181) heq
    simpa [Nat.add_mod, rhs_mod_14_181] using h
  have h181prime : (Nat.choose (i % 181) 14) % 181 =
      ((i % 181) ^ 2) % 181 := by
    calc
      _ = (Nat.choose i 14) % 181 := (choose_mod_14_181 i).symm
      _ = (i ^ 2) % 181 := h181
      _ = ((i % 181) ^ 2) % 181 := by simp [Nat.pow_mod]
  have hres181 : i % 181 = 0 ∨ i % 181 = 170 ∨ i % 181 = 180 := by
    exact roots_14_181
      ⟨i % 181, Nat.mod_lt i (by decide)⟩ h181prime
  rcases hres191 with ha | ha | ha
  · rcases hres181 with hb | hb | hb <;> omega
  · rcases hres181 with hb | hb | hb <;> omega
  · rcases hres181 with hb | hb | hb <;> omega

#print axioms NestedBinomialV109.k6_no_original_solution_below_cubic
#print axioms NestedBinomialV109.k9_no_original_solution_below_cubic
#print axioms NestedBinomialV109.k14_no_original_solution_below_cubic

end NestedBinomialV109
