import Mathlib.Tactic
import Mathlib.Data.Nat.Choose.Lucas

/-!
# v99: A genuine auxiliary cubic point that fails the original binomial equation

For S=31,T=6889,n=250,r=830 the *auxiliary* curve has a strict
positive point.  It is NOT a solution of the original nested-binomial
equation, for either k=830 or k=2573000-830.

Use Lucas' congruence modulo 83 to check the original squared-index
equation WITHOUT evaluating its enormous binomial coefficients.
This is independent of the unformalized general v17 prime-factor
bound, although that bound also excludes this same n=250 case.
-/

namespace NestedBinomialV10

private theorem cf_v99_outer_choose_mod83 :
    (Nat.choose 2573000 830) % 83 = 65 := by
  haveI : Fact (Nat.Prime 83) := ⟨by norm_num⟩
  have hfirst : Nat.choose 2573000 830 ≡ Nat.choose 31000 10 [MOD 83] := by
    simpa only [show 83 * 31000 = 2573000 by norm_num,
      show 83 * 10 = 830 by norm_num] using
      (Choose.choose_mul_mul_modEq_choose_nat (p := 83) (a := 31000) (b := 10))
  have hsecond : Nat.choose 31000 10 ≡ Nat.choose 41 10 [MOD 83] := by
    have h := Choose.choose_modEq_choose_mod_mul_choose_div_nat
      (n := 31000) (k := 10) (p := 83)
    simpa [show (31000 : ℕ) % 83 = 41 by decide,
      show (10 : ℕ) % 83 = 10 by decide,
      show (31000 : ℕ) / 83 = 373 by decide,
      show (10 : ℕ) / 83 = 0 by decide] using h
  have h := hfirst.trans hsecond
  change (Nat.choose 2573000 830) % 83 = (Nat.choose 41 10) % 83 at h
  simpa [show (Nat.choose 41 10) % 83 = 65 by decide] using h

private theorem cf_v99_inner_choose_mod83 :
    (Nat.choose 62500 61009) % 83 = 0 := by
  haveI : Fact (Nat.Prime 83) := ⟨by norm_num⟩
  have h := Choose.choose_modEq_choose_mod_mul_choose_div_nat
      (n := 62500) (k := 61009) (p := 83)
  change (Nat.choose 62500 61009) % 83 =
    (Nat.choose (62500 % 83) (61009 % 83) *
     Nat.choose (62500 / 83) (61009 / 83)) % 83 at h
  simpa [show (62500 : ℕ) % 83 = 1 by decide,
    show (61009 : ℕ) % 83 = 4 by decide] using h

/-- Lucas' prime-83 certificate rules out the ONLY strict auxiliary
point currently found at S=31, for both original k-branches. -/
theorem cf_v99_n250_r830_not_nested_binomial
    (k : ℕ)
    (hk : k = 830 ∨ k = 2572170)
    (heq : Nat.choose (Nat.choose 250 (250 - 3)) (Nat.choose k 1) =
      Nat.choose (250 ^ 2) ((250 - 3) ^ 2) +
      Nat.choose (k ^ 2) (1 ^ 2)) : False := by
  have hA : Nat.choose 250 (250 - 3) = 2573000 := by decide
  have hX : (Nat.choose (250 ^ 2) ((250 - 3) ^ 2)) % 83 = 0 := by
    simpa only [show (250 : ℕ) ^ 2 = 62500 by norm_num,
      show (250 : ℕ) - 3 = 247 by norm_num,
      show (247 : ℕ) ^ 2 = 61009 by norm_num] using
      cf_v99_inner_choose_mod83
  rcases hk with rfl | rfl
  · have hL : (Nat.choose 2573000 (Nat.choose 830 1)) % 83 = 65 := by
      simpa [Nat.choose_one_right] using cf_v99_outer_choose_mod83
    have hK : (Nat.choose (830 ^ 2) (1 ^ 2)) % 83 = 0 := by
      norm_num [Nat.choose_one_right]
    have hmod := congrArg (fun v : ℕ => v % 83) heq
    rw [hA] at hmod
    rw [Nat.add_mod] at hmod
    rw [hX, hK] at hmod
    norm_num [hL] at hmod
  · have hsym : Nat.choose 2573000 2572170 = Nat.choose 2573000 830 := by
      have h := Nat.choose_symm (show 830 ≤ 2573000 by decide)
      simpa only [show (2573000 : ℕ) - 830 = 2572170 by decide] using h
    have hL : (Nat.choose 2573000 (Nat.choose 2572170 1)) % 83 = 65 := by
      simpa [Nat.choose_one_right, hsym] using cf_v99_outer_choose_mod83
    have hK : (Nat.choose (2572170 ^ 2) (1 ^ 2)) % 83 = 0 := by
      norm_num [Nat.choose_one_right]
    have hmod := congrArg (fun v : ℕ => v % 83) heq
    rw [hA] at hmod
    rw [Nat.add_mod] at hmod
    rw [hX, hK] at hmod
    norm_num [hL] at hmod

#print axioms cf_v99_outer_choose_mod83
#print axioms cf_v99_inner_choose_mod83
#print axioms cf_v99_n250_r830_not_nested_binomial

end NestedBinomialV10
