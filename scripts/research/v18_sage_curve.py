"""One isolated Sage worker. Never loaded by the standard-library tests."""
import argparse
import json
import os
from pathlib import Path
import time

from sage.all import EllipticCurve, QQ, proof
from sage.env import SAGE_VERSION
from cysignals.alarm import alarm, cancel_alarm
from cysignals.signals import AlarmInterrupt
from v18_arithmetic import curve_coefficients


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--a', type=int, required=True)
    p.add_argument('--b', type=int, required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--stage-seconds', type=int, default=30)
    args = p.parse_args()
    record = {"a": args.a, "b": args.b, "sage_version": SAGE_VERSION,
              "stages": {}, "status": "running"}

    def save():
        tmp = args.output.with_suffix('.tmp')
        tmp.write_text(json.dumps(record, indent=2)+'\n')
        os.replace(tmp, args.output)

    def stage(name, fn):
        start = time.monotonic()
        try:
            alarm(args.stage_seconds)
            value = fn()
            record['stages'][name] = {"status": "ok", "value": value}
        except (Exception, AlarmInterrupt) as exc:
            record['stages'][name] = {"status": "timeout" if isinstance(exc, AlarmInterrupt)
                                     else "error", "error": type(exc).__name__+': '+str(exc)}
        finally:
            cancel_alarm()
        record['stages'][name]['seconds'] = round(time.monotonic()-start, 3)
        save()

    save()
    proof.all(True)
    c4, c6 = curve_coefficients(args.a, args.b)
    original = EllipticCurve(QQ, [0, 0, 0, c4, c6])
    minimal = original.minimal_model()
    record['original_ainvs'] = [str(x) for x in original.a_invariants()]
    record['minimal_ainvs'] = [str(x) for x in minimal.a_invariants()]
    record['minimal_discriminant'] = str(minimal.discriminant())
    record['isomorphism_original_to_minimal'] = str(original.isomorphism_to(minimal))
    save()
    stage('conductor', lambda: int(minimal.conductor(algorithm='pari')))
    stage('rank', lambda: int(minimal.rank(proof=True, use_database=False)))

    def generators():
        free = minimal.gens(proof=True, use_database=False)
        certain = bool(minimal.gens_certain())
        torsion = minimal.torsion_subgroup().gens()
        return {"basis_proven": certain,
                "free_basis_minimal": [[str(c) for c in point] for point in free],
                "torsion_generators_minimal": [[str(c) for c in point.element()]
                                                for point in torsion],
                "coordinate_convention": "projective [x,y,z] on minimal model"}

    stage('mordell_weil', generators)
    record['status'] = ('complete' if all(v['status'] == 'ok'
                                        for v in record['stages'].values()) else 'partial')
    # A successful call must also explicitly certify saturation/full basis.
    mw = record['stages'].get('mordell_weil', {})
    if mw.get('status') == 'ok' and not mw['value']['basis_proven']:
        record['status'] = 'partial'
    save()


if __name__ == '__main__':
    main()
