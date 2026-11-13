import Mathlib.Tactic

/-!
# Integral first elliptic quotient: exact polynomial identities

Formal algebra for the v74/v79 reduction. This module establishes the
sixth-degree identity and the integral Weierstrass change of variables
over the integers. The subsequent prime-valuation and Mordell-Weil
claims are NOT proved in this file.
-/

namespace NestedBinomialV10

def integralLiftX (a b rho : ℤ) : ℤ :=
  a ^ 2 - b ^ 2 - rho

def integralLiftM (b rho : ℤ) : ℤ :=
  b * (8 * b ^ 2 + 9 * rho)

def integralLiftF (a b rho : ℤ) : ℤ :=
  4 * a ^ 6 + (24 * b ^ 2 - 12 * rho) * a ^ 4 +
  (36 * b ^ 4 + 60 * b ^ 2 * rho + 12 * rho ^ 2) * a ^ 2 -
  3 * b ^ 2 * rho ^ 2 - 4 * rho ^ 3

/-- The original sextic is a square plus four times a perfect cube. -/
theorem sextic_integral_model_identity (a b rho : ℤ) :
    integralLiftF a b rho =
      (6 * b * integralLiftX a b rho + integralLiftM b rho) ^ 2 +
        4 * (integralLiftX a b rho) ^ 3 := by
  unfold integralLiftF integralLiftX integralLiftM
  ring

/-- Exact double-cover identity; it contains NO arithmetic assumptions. -/
theorem integral_weierstrass_identity (b rho X Y : ℤ) :
    (2 * Y + 6 * b * X + integralLiftM b rho) ^ 2 -
        ((6 * b * X + integralLiftM b rho) ^ 2 + 4 * X ^ 3) =
      4 * (Y ^ 2 + 6 * b * X * Y + integralLiftM b rho * Y - X ^ 3) := by
  unfold integralLiftM
  ring

/-- Conversely, every integral elliptic point gives a sextic square
after its X-coordinate passes the integer-square recovery condition. -/
theorem recover_sextic_square (a b rho Y : ℤ)
    (h : Y ^ 2 + 6 * b * (integralLiftX a b rho) * Y +
      integralLiftM b rho * Y = (integralLiftX a b rho) ^ 3) :
    (2 * Y + 6 * b * (integralLiftX a b rho) + integralLiftM b rho) ^ 2 =
      integralLiftF a b rho := by
  rw [sextic_integral_model_identity]
  have hid := integral_weierstrass_identity b rho (integralLiftX a b rho) Y
  have hh : Y ^ 2 + 6 * b * integralLiftX a b rho * Y +
      integralLiftM b rho * Y - (integralLiftX a b rho) ^ 3 = 0 :=
    sub_eq_zero.mpr h
  rw [hh, mul_zero] at hid
  exact sub_eq_zero.mp hid

#print axioms sextic_integral_model_identity
#print axioms integral_weierstrass_identity
#print axioms recover_sextic_square

end NestedBinomialV10
