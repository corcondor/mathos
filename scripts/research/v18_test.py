"""Arithmetic tests independent of the optimized candidate generator."""
import json
from math import comb, gcd, isqrt
from pathlib import Path
import tempfile
import subprocess
import unittest
from unittest.mock import patch

from v18_arithmetic import (curve_coefficients, forced_r_divisor, lucas,
                           n_height_exclusive, pairs, residual_points, spf_sieve)
from v18_report import render
import v18_publish


class ArithmeticTests(unittest.TestCase):
    def test_domain_and_singular_curve(self):
        domain = pairs(20)
        self.assertEqual(len(domain), 83)
        self.assertEqual([p for p in domain if 3*p[0] == p[1]], [(1,3)])
        for a,b in domain:
            c4,c6 = curve_coefficients(a,b)
            self.assertEqual(-16*(4*c4**3+27*c6**2),
                             -995328*a*a*b**4*(3*a-b)**3*(3*a+b)**3)

    def test_finite_strip_against_residual_polynomial(self):
        for a,b in pairs(4):
            points = residual_points(a,b)
            found = {(p['rho'],p['Y']//4) for p in points['points']}
            for rho in range(a*a % b or b, points['rho_upper']+1,b):
                f = (4*a**6+24*a**4*b*b-12*a**4*rho+36*a*a*b**4
                     +60*a*a*b*b*rho+12*a*a*rho*rho-3*b*b*rho*rho-4*rho**3)
                if f >= 0 and isqrt(f)**2 == f:
                    self.assertTrue({(rho,isqrt(f)),(rho,-isqrt(f))} <= found)
                else:
                    self.assertFalse(any(r == rho for r,y in found))
            self.assertTrue(points['complete'])

    def test_forced_divisor_does_not_miss_any_r(self):
        spf = spf_sieve(500)
        for n in range(104,500):
            q = n*(n-1)//(gcd(n,3)*gcd(n-1,6))
            brute = [r for r in range(3*n+4,(10*n-1)//3+1) if r**3 % q == 0]
            f = forced_r_divisor(n,spf)
            generated = list(range(((3*n+4+f-1)//f)*f,(10*n-1)//3+1,f))
            self.assertEqual(generated,brute)

    def test_lucas_against_actual_binomial(self):
        for n in range(40):
            for k in range(n+1):
                for p in (2,3,5,7,11):
                    self.assertEqual(lucas(n,k,p),comb(n,k)%p)

    def test_strict_heights(self):
        for j in range(1,8):
            self.assertEqual(n_height_exclusive(j,0),16*j**6)
            h = n_height_exclusive(j,1)
            self.assertLess((h-1)**3,(1<<352)*j**33)
            self.assertGreaterEqual(h**3,(1<<352)*j**33)

    def test_missing_artifacts_cannot_report_success(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root/'in').mkdir()
            render(root/'in',root/'out','unit-test',20)
            report = json.loads((root/'out/v18_ranks_a20.json').read_text())
            self.assertFalse(report['cas_complete'])
            self.assertFalse(report['residual_enumeration_complete'])
            self.assertEqual(len(report['missing_pairs']),83)
            fixed = json.loads((root/'out/v18_fixed_J_search.json').read_text())
            self.assertEqual(fixed['status'],'missing_artifact')

    def test_interrupted_fixed_search_keeps_coverage_and_results(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root/'in').mkdir()
            checkpoint = {"status": "running", "n_scanned_through": 1023,
                          "j_max": {"small": 3, "complement": 1},
                          "counts": {}, "survivors": []}
            (root/'in/fixed-j.json').write_text(json.dumps(checkpoint))
            render(root/'in',root/'out','interrupted-test',20)
            report = json.loads((root/'out/v18_fixed_J_search.json').read_text())
            self.assertEqual(report['status'],'interrupted_checkpoint')
            self.assertTrue(report['coverage']['small'][1]['height_fully_covered'])
            self.assertFalse(report['coverage']['small'][2]['height_fully_covered'])
            self.assertFalse(report['coverage']['complement'][0]['height_fully_covered'])


class PublicationTests(unittest.TestCase):
    def test_only_generated_results_committed_with_dirty_lean_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            origin, work = root/'origin.git',root/'work'
            def command(*args, cwd=root):
                return subprocess.run(['git',*args],cwd=cwd,check=True,
                                      text=True,capture_output=True).stdout
            command('init','--bare',str(origin))
            command('clone',str(origin),str(work))
            command('config','user.name','Test',cwd=work)
            command('config','user.email','test@example.invalid',cwd=work)
            branch = 'research/v18-next-descent'
            command('checkout','-b',branch,cwd=work)
            (work/'Existing.lean').write_text('def fixedValue := 1\n')
            command('add','Existing.lean',cwd=work)
            command('commit','-m','existing proof',cwd=work)
            command('push','origin',branch,cwd=work)
            (work/'Existing.lean').write_text('def fixedValue := 2\n')
            report = work/'docs/research/nested-binomial/v18_fixed_J_search.json'
            report.parent.mkdir(parents=True)
            report.write_text('{"status":"partial"}\n')
            (report.parent/'unrelated.md').write_text('leave this untracked\n')
            with patch.object(v18_publish,'ROOT',work):
                v18_publish.publish(branch)
            changed = command('diff-tree','--no-commit-id','--name-only','-r','HEAD',cwd=work).strip()
            self.assertEqual(changed,str(report.relative_to(work)))
            self.assertEqual(command('show','HEAD:Existing.lean',cwd=work),'def fixedValue := 1\n')
            self.assertEqual((work/'Existing.lean').read_text(),'def fixedValue := 2\n')
            self.assertTrue(command('status','--short',cwd=work))
            self.assertEqual(command('rev-parse','HEAD',cwd=work),
                             command('rev-parse','refs/heads/'+branch,cwd=origin))

    def test_publication_rejects_default_branch(self):
        with self.assertRaises(ValueError):
            v18_publish.publish('master')


if __name__ == '__main__':
    unittest.main()
