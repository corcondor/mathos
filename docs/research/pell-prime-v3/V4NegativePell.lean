import Mathlib

namespace PellPrimeResearch

def norm (x y : ℤ) : ℤ := x^2 - 2*y^2

theorem norm_step (x y : ℤ) :
    norm (x+2*y) (x+y) = -norm x y := by
  unfold norm
  ring

theorem norm_descend (x y : ℤ) :
    norm (3*x-4*y) (3*y-2*x) = norm x y := by
  unfold norm
  ring

theorem descend_inverse (x y : ℤ) :
    (3*(3*x-4*y)+4*(3*y-2*x), 2*(3*x-4*y)+3*(3*y-2*x)) = (x,y) := by
  congr <;> ring

theorem half_index (x y u v e : ℤ) (h : u^2 - 2*v^2 = e) :
    let X := (u+2*v)*u+2*(u+v)*v
    let Y := (u+2*v)*v+(u+v)*u
    X+e=2*(u+2*v)*u ∧ X-e=4*(u+v)*v ∧
    Y+e=2*(u+v)*u ∧ Y-e=2*(u+2*v)*v := by
  dsimp
  constructor
  · nlinarith
  constructor
  · nlinarith
  constructor <;> nlinarith

def coeff : Nat → ℤ × ℤ
  | 0 => (1,0)
  | n+1 => ((coeff n).1 + 2*(coeff n).2, (coeff n).1 + (coeff n).2)

theorem coeff_norm (n : Nat) : norm (coeff n).1 (coeff n).2 = (-1)^n := by
  induction n with
  | zero => norm_num [coeff, norm]
  | succ n ih =>
    simp only [coeff, norm_step, ih, pow_succ]
    ring

-- A generic positive descent lemma for the negative Pell equation.
theorem descend_pos (x y : ℤ) (hx : 0 < x) (hy : 3 ≤ y)
    (h : norm x y = -1) :
    0 < 3*x-4*y ∧ 0 < 3*y-2*x ∧ 3*y-2*x < y := by
  unfold norm at h
  have h1 : y < x := by
    by_contra! hh
    have hp := mul_nonneg (sub_nonneg.mpr hh) (show 0 ≤ y+x by omega)
    have hq := mul_nonneg (show 0 ≤ y-3 by omega) (show 0 ≤ y+3 by omega)
    nlinarith
  have h2 : 4*y < 3*x := by
    by_contra! hh
    have hp := mul_nonneg (sub_nonneg.mpr hh) (show 0 ≤ 4*y+3*x by omega)
    have hq := mul_nonneg (show 0 ≤ y-3 by omega) (show 0 ≤ y+3 by omega)
    nlinarith
  have h3 : 2*x < 3*y := by
    by_contra! hh
    have hp := mul_nonneg (sub_nonneg.mpr hh) (show 0 ≤ 2*x+3*y by omega)
    nlinarith [sq_nonneg y]
  omega

#print axioms coeff_norm
#print axioms half_index
#print axioms descend_pos
end PellPrimeResearch

namespace PellPrimeResearch

theorem coeff_two_step (n : ℕ) :
    coeff (n+2) = (3*(coeff n).1+4*(coeff n).2, 2*(coeff n).1+3*(coeff n).2) := by
  simp only [coeff]
  congr <;> ring

theorem small_negative_pell (x y : ℤ) (hx : 0 < x) (hy : 0 < y) (hy' : y < 3)
    (h : norm x y = -1) : x = 1 ∧ y = 1 := by
  unfold norm at h
  have hxy : y=1 ∨ y=2 := by omega
  rcases hxy with rfl | rfl
  · have hh : x=1 ∨ 2≤x := by omega
    rcases hh with h1|h2
    · exact ⟨h1,rfl⟩
    · exfalso
      have := mul_nonneg (show 0≤x-2 by omega) (show 0≤x+2 by omega)
      nlinarith
  · exfalso
    by_cases h2 : x ≤ 2
    · have := mul_nonneg (show 0≤2-x by omega) (show 0≤2+x by omega)
      nlinarith
    · have := mul_nonneg (show 0≤x-3 by omega) (show 0≤x+3 by omega)
      nlinarith

-- Complete positive integer classification, using the strict descent already proved in v3.
theorem negative_pell_complete (x y : ℤ) (hx : 0 < x) (hy : 0 < y)
    (h : norm x y = -1) : ∃ k : ℕ, coeff (2*k+1) = (x,y) := by
  by_cases hy3 : y < 3
  · obtain ⟨rfl,rfl⟩ := small_negative_pell x y hx hy hy3 h
    exact ⟨0, by norm_num [coeff]⟩
  · let u := 3*x-4*y
    let v := 3*y-2*x
    obtain ⟨hu,hv,hvy⟩ := descend_pos x y hx (by omega) h
    have hn : norm u v = -1 := (norm_descend x y).trans h
    have hv' : 0 < v := hv
    have hvlt : v < y := hvy
    obtain ⟨k,hk⟩ := negative_pell_complete u v hu hv hn
    refine ⟨k+1, ?_⟩
    rw [show 2*(k+1)+1=(2*k+1)+2 by omega, coeff_two_step, hk]
    exact descend_inverse x y
termination_by y.toNat
decreasing_by omega

theorem negative_pell_odd_index (k : ℕ) :
    norm (coeff (2*k+1)).1 (coeff (2*k+1)).2 = -1 := by
  rw [coeff_norm, pow_add, pow_mul]
  norm_num

#print axioms negative_pell_complete
#print axioms negative_pell_odd_index
end PellPrimeResearch
