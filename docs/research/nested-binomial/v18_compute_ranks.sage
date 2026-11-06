"""
v18 residual elliptic curve rank and conductor computation.
Run with: sage v18_compute_ranks.sage
Requires SageMath.
"""

from sage.all import EllipticCurve, ZZ

def admissible_pairs(max_a=10):
    divs = [1, 2, 3, 6, 9, 18, 27, 54, 81, 162, 243, 486]
    pairs = []
    for a in range(1, max_a + 1):
        for b in divs:
            if gcd(a, b) == 1 and 27 * a < 31 * b:
                pairs.append((a, b))
    return pairs

def weierstrass_coeffs(a, b):
    A4 = -3 * b**2 * (72 * a**2 + b**2)
    A6 = 2 * b**2 * (648 * a**4 + 180 * a**2 * b**2 - b**4)
    return A4, A6

def residual_bound(a, b):
    return (216 * a**2 + 760 * b**2) // 1377

print("a\tb\tconductor\trank\tj_max\tintegral_points_in_bound")
for a, b in admissible_pairs(5):  # start small
    A4, A6 = weierstrass_coeffs(a, b)
    if A4 == 0 and A6 == 0:
        continue
    try:
        E = EllipticCurve([0, 0, 0, A4, A6])
        N = E.conductor()
        r = E.rank()
        jmax = residual_bound(a, b)
        # count integral points with |X| roughly bounded by residual
        # (full search may be slow; this is a placeholder filter)
        pts = E.integral_points()
        in_bound = sum(1 for P in pts if abs(P[0]) < 4 * jmax + 1000)
        print(f"{a}\t{b}\t{N}\t{r}\t{jmax}\t{in_bound}")
    except Exception as e:
        print(f"{a}\t{b}\tERROR\t{e}")
