# v3.3: Montgomery progression search, independent verification receipts

Completed all 259 formerly unresolved indices, then four successive progression intervals, k=350000..4499999, excluding hit indices from later stages. 467,644,422 modular power probes; 37 new proper factors validated by independent matrix modular exponentiation. Total 787/1009 from the previously selected non-contiguous index set; 222 unresolved. All 5 stage counts and factors in montgomery_hits.json. The full local coverage CSVs and v2 data are in the companion v3 archive; the GitHub compact checker validates the 37 witnesses, not the complete previous CSV coverage. Single paired benchmark of 32 identical rows, four threads: 0.42s previous vs 0.22s Montgomery, every output row matched. Do not treat as a universal speedup or a proof of primality for survivors.

Montgomery correctness: all tested odd moduli m<2^48; doubled pair numerators <3m^2 < m*2^64, so the 128-bit reduction result lies below 2m. Modular zero is invariant under multiplication by R=2^64. Source inspired by the progression-filtering separation in https://github.com/s1rj1n/primepath, exact implementation is independent; the Metal app itself is not run.

Actual CI receipts:
- https://github.com/corcondor/mathos/actions/runs/45489068111 : PARI 8/8, FLINT 8/8, hex-primality 8/8 via decide +kernel, axioms propext/Classical.choice/Quot.sound only. Initial Coq module path and PFL decide attempts failed.
- https://github.com/corcondor/mathos/actions/runs/45489442996 : corrected CoqPrime proof replay PASS.
- https://github.com/corcondor/mathos/actions/runs/45489531579 : corrected CoqPrime, PFL N-1 and N+1 checker steps, Lean algebra and descent steps PASS. PFL uses native_decide, unlike strict Hex kernel replay. Check separate factor CLI step for final outcome.

Global finiteness and full original radical classification in Lean remain unsolved. The s=3 mod4 sufficient exclusion criterion does not assert infinitely many primes s for which 2s±1 is prime; that infinitude itself is unknown.
