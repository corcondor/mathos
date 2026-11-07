# v20 reproduction

Run from `docs/research/nested-binomial` in the research branch.
The recorded environment is Python 3.12.14 and SymPy 1.14.0. The two
finite-domain verifiers and the residual verifier use only the standard
library. No external solver service or Lean runtime is needed for these
particular arithmetic checks.

## Check the saved artifacts

```sh
python v20_logarithmic_gap_checks.py
python v20_sharper_defect_height_checks.py --output v20_sharper_defect_height_checks.json
python v20_sharper_defect_height_independent_audit.py
python v20_binary_height_24.py
python v20_complement_J_verify.py
python v20_fixed_parameter_verify.py
python v20_root_isolation_checks.py
python v20_residual_integrality_verify.py
```

The v20 publication ran all eight commands in the assembled directory;
each returned exit code 0. Full output is saved in `v20_execution.json`.
The two complete finite-domain verifiers reconstruct every coefficient
family and divisor domain from the saved certificates. They do not
import their producers or rely on SymPy's factorization/primality verdict.

## Regenerate certificates

```sh
python v20_complement_J_cover.py
python v20_complement_J_verify.py
python v20_fixed_parameter_solver.py
python v20_fixed_parameter_verify.py
python v20_residual_integrality_checks.py
python v20_residual_integrality_verify.py
```

The complement producer covers every `1<=J<=32`, `65<=w<=383` in the
proved domain. The fixed-parameter solver's default queries are
`(delta,J,branch)=(25,17,small),(25,33,complement)`. These are separate
mathematical claims, not samples proving an all-parameter theorem.

The fixed-parameter producer uses SymPy only to discover factorizations,
then supplies complete recursive Lucas order certificates for every
factor prime. Its verifier checks those certificates, the full divisor
lists, and exact positive-root brackets. The primality certificates
are different from Lucas's binomial congruence; no original-equation
congruence witnesses were needed in either of the two default queries.

To run another fixed query:

```sh
python v20_fixed_parameter_solver.py --delta 25 --J 33 --branch complement --output query.json.gz
python v20_fixed_parameter_verify.py --certificate query.json.gz --output query_verification.json
```

The generator reports any candidates surviving its necessary conditions
as `undecided_after_moduli`; these are not asserted to be solutions.

## Integrity and scope

`v20_manifest.json` records SHA-256, Git blob SHA, and size for every
published v20 artifact and the two updated index files. The manifest
does not hash itself. Compressed JSON certificates preserve all records;
their summaries contain the compressed and uncompressed SHA-256 values.

The integral estimates, monotonicity, coefficient valuation arguments,
and transfer from the original binomial equation are written proofs.
The exact finite checks support those proofs and exhaust the explicitly
proved finite domains. This is not a claim of new Lean verification,
a complete Selmer/Mordell–Weil computation, external peer review, or a
solution of the full four-variable problem.
