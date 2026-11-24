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
