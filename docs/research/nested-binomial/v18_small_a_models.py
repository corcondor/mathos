#!/usr/bin/env python3
"""
Generate residual Weierstrass models for small a and admissible b.
Uses only the Python standard library.
"""

import math

def admissible_pairs(max_a=20):
    divs = [1, 2, 3, 6, 9, 18, 27, 54, 81, 162, 243, 486]
    pairs = []
    for a in range(1, max_a + 1):
        for b in divs:
            if math.gcd(a, b) == 1 and 27 * a < 31 * b:
                pairs.append((a, b))
    return pairs

def weierstrass_coeffs(a, b):
    # Y^2 = X^3 + A4 X + A6
    A4 = -3 * b**2 * (72 * a**2 + b**2)
    A6 = 2 * b**2 * (648 * a**4 + 180 * a**2 * b**2 - b**4)
    return A4, A6

def residual_bound(a, b):
    return (216 * a**2 + 760 * b**2) // 1377

if __name__ == "__main__":
    print("a\tb\tA4\tA6\tj_max")
    for a, b in admissible_pairs(10):
        A4, A6 = weierstrass_coeffs(a, b)
        jmax = residual_bound(a, b)
        print(f"{a}\t{b}\t{A4}\t{A6}\t{jmax}")
