"""Exact finite remainder for adjacent_rows_exclusion.md.

The analytic lemma handles n >= 256. The earlier N=20 certificate
handles M <= 20, so the finite interval is proved, not experimental.
Only necessary conditions are tested; no approximate arithmetic is used.
"""

import json
from math import comb
from pathlib import Path


def above_phi(t, m):
    return 2 * t > m and (2 * t - m) ** 2 > 5 * m * m


def verify():
    checked_pairs = 0
    small_gap_pairs = 0
    exceptional_gaps = []
    possible_original_parameters = []
    for n in range(23, 256):
        row_n = [comb(n, a) for a in range(1, n // 2 + 1)]
        row_previous = [
            comb(n - 1, b) for b in range(1, (n - 1) // 2 + 1)
        ]
        for a, u in enumerate(row_n, start=1):
            for b, v in enumerate(row_previous, start=1):
                checked_pairs += 1
                t = abs(u - v)
                if not 0 < t < 10 * n:
                    continue
                small_gap_pairs += 1
                if (a, b) not in ((1, 1), (2, 2)):
                    exceptional_gaps.append([n, a, b, u - v])

                if u > v:
                    i, first_effective, k, second_effective = n, a, n - 1, b
                    smaller_coefficient = v
                else:
                    i, first_effective, k, second_effective = n - 1, b, n, a
                    smaller_coefficient = u
                for j in sorted({first_effective, i - first_effective}):
                    for ell in sorted({second_effective, k - second_effective}):
                        m = max(j, ell)
                        if not (1 <= j <= i - 2 and 1 <= ell <= k - 2):
                            continue
                        if not m >= 21:
                            continue
                        if not (t <= smaller_coefficient and t < 10 * m):
                            continue
                        if not above_phi(t, m):
                            continue
                        possible_original_parameters.append([i, j, k, ell])

    expected = [[23, 1, 2, -208], [24, 1, 2, -229]]
    assert exceptional_gaps == expected, exceptional_gaps
    assert not possible_original_parameters, possible_original_parameters
    return {
        "verification_passed": True,
        "scope": "Upper branch t <= B, |i-k|=1, M>=21, 23<=max(i,k)<256",
        "effective_pairs_checked": checked_pairs,
        "nonzero_gaps_below_10n": small_gap_pairs,
        "exceptions_to_effective_pairs_11_or_22": exceptional_gaps,
        "parameters_satisfying_all_necessary_conditions": possible_original_parameters,
        "arithmetic": "Exact arbitrary-precision integers; no floating point",
    }


if __name__ == "__main__":
    result = verify()
    destination = Path(__file__).with_name("verification_adjacent_rows.json")
    destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
