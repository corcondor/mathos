#!/usr/bin/env python3
"""Render every frozen Python certificate as kernel-checked Lean arithmetic.

This does not formalize the analytic/valuation reduction or domain coverage.
The list itself is independently checked against the JSON, whose SHA is pinned.
"""
from hashlib import sha256
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
CERT = HERE.parent / "v9_cofactor_two_certificates.json"
EXPECTED = "03e778865211a34c8f3a0caa42368839f9f0fdee97b595f4f04627a4ed59175d"

def main():
    data = CERT.read_bytes()
    assert sha256(data).hexdigest() == EXPECTED
    rows = json.loads(data)["cases"]
    assert len(rows) == 2592
    source = HERE.joinpath("CubeCertificateLemmas.txt").read_text()
    source += "\nset_option maxRecDepth 20000\nset_option maxHeartbeats 0\n\n"
    source += "/- Frozen certificate SHA-256: " + EXPECTED + " -/\n"
    names = []
    for offset in range(0, len(rows), 50):
        name = f"batch{offset // 50:03d}"
        names.append(name)
        source += f"\ndef {name} : List CubeWitness := [\n"
        source += ",\n".join(
            "  ⟨{prime}, {exponent}, {quotient}, {lower_cube_root}⟩".format(**row)
            for row in rows[offset:offset + 50]
        )
        source += "\n]\n"
        source += f"\ntheorem {name}_checked : checkRows {name} = true := by decide\n"
    source += "\ndef allRows : List CubeWitness :=\n  " + " ++\n  ".join(names) + "\n"
    proof = names[-1] + "_checked"
    for name in reversed(names[:-1]):
        proof = f"checkRows_append {name}_checked ({proof})"
    source += "\ntheorem allRows_checked : checkRows allRows = true := by\n  unfold allRows\n  exact " + proof + "\n"
    source += "\ntheorem allRows_count : allRows.length = 2592 := by decide\n"
    source += """
theorem every_recorded_value_not_cube (w : CubeWitness) (hw : w ∈ allRows) :
    ¬ ∃ v : ℕ, v ^ 3 = value w :=
  valid_not_cube w (of_checkRows allRows_checked hw)

#print axioms numerical_gap_constant
#print axioms quotient_interval_has_no_integer
#print axioms allRows_checked
#print axioms allRows_count
#print axioms every_recorded_value_not_cube

end NestedBinomialV9
"""
    HERE.joinpath("CubeCertificates.lean").write_text(source)
    print(json.dumps({"rows": len(rows), "batches": len(names),
                      "source_bytes": len(source.encode()),
                      "source_sha256": sha256(source.encode()).hexdigest()}))

if __name__ == "__main__":
    main()
