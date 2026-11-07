"""Test real failure handling without using API calls or inventing proofs."""
import json
from pathlib import Path
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import deepseek_lean_harness as harness
from deepseek_proof_loop import digest


class HarnessTests(unittest.TestCase):
    def test_lint_is_distinct_from_proof_holes_and_untrusted_axioms(self):
        clean = "'t' depends on axioms: [propext, Classical.choice, Quot.sound]\n"
        lint = 'M.lean:3:2: warning: Variable name `h` is not explicitly referenced.\n'
        self.assertTrue(harness.accepted(0, clean + lint))
        self.assertFalse(harness.accepted(1, clean))
        self.assertFalse(harness.accepted(0, "'t' depends on axioms: [sorryAx]"))
        self.assertFalse(harness.accepted(0, "'t' depends on axioms: [My.customOracle]"))
        self.assertIn('unused_binding', harness.analyze(lint, 0)['categories'])

    def test_resource_error_retries_identical_source_with_bounded_heartbeats(self):
        error = 'M.lean:8:2: error: (deterministic) timeout at `isDefEq`, maximum number of heartbeats (400000) has been reached\n'
        calls = []
        def run(command, **kwargs):
            calls.append((command, kwargs['timeout']))
            return SimpleNamespace(returncode=1 if len(calls) == 1 else 0,
                                   stdout=error if len(calls) == 1 else '', stderr='')
        with patch.object(harness.subprocess, 'run', run):
            result = harness.compile_lean(['lean', '--root=R', 'M.lean'], {}, 180, harness.DEFAULTS)
        self.assertEqual(result['exit_code'], 0)
        self.assertEqual(len(calls), 2)
        self.assertIn('-DmaxHeartbeats=400000', calls[0][0])
        self.assertIn('-DmaxHeartbeats=800000', calls[1][0])
        self.assertEqual(calls[0][0][-2:], calls[1][0][-2:])
        self.assertLessEqual(calls[1][1], calls[0][1])

    def test_recursion_limit_escalates_depth_instead_of_heartbeats(self):
        output = 'M.lean:3:2: error: maximum recursion depth has been reached\n'
        with patch.object(harness.subprocess, 'run', return_value=SimpleNamespace(
                returncode=1, stdout=output, stderr='')) as run:
            result = harness.compile_lean(['lean', 'M.lean'], {}, 180, harness.DEFAULTS)
        self.assertEqual([r['max_rec_depth'] for r in result['resource_attempts']], [1024,2048,4096])
        self.assertEqual({r['heartbeats'] for r in result['resource_attempts']}, {400000})
        self.assertEqual(run.call_count, 3)

    def test_mixed_syntax_and_resource_errors_do_not_retry_unchanged_proof(self):
        for extra in ['No goals to be solved', 'unexpected token', 'Type mismatch: term has wrong type']:
            with self.subTest(extra=extra):
                output = 'M.lean:4:2: error: maximum number of heartbeats has been reached\n'
                output += 'M.lean:5:2: error: ' + extra + '\n'
                with patch.object(harness.subprocess, 'run', return_value=SimpleNamespace(
                        returncode=1, stdout=output, stderr='')) as run:
                    result = harness.compile_lean(['lean','M.lean'], {},180,harness.DEFAULTS)
                self.assertFalse(result['analysis']['resource_only'])
                self.assertEqual(run.call_count, 1)

    def test_wall_timeout_returns_diagnostic_without_resetting_deadline(self):
        with patch.object(harness.subprocess, 'run', side_effect=subprocess.TimeoutExpired(
                ['lean'], 180, output=b'partial output', stderr=b'partial error')) as run:
            result = harness.compile_lean(['lean','M.lean'], {},180,harness.DEFAULTS)
        self.assertEqual(result['exit_code'],124)
        self.assertIn('wall_timeout',result['analysis']['categories'])
        self.assertIn('partial output',result['output'])
        self.assertEqual(run.call_count,1)

    def test_failure_fingerprints_ignore_paths_and_positions_but_keep_error(self):
        a = harness.analyze('/tmp/a/M.lean:4:2: error: No goals to be solved')
        b = harness.analyze('/tmp/b/M.lean:20:7: error: No goals to be solved')
        self.assertEqual(a['fingerprint'],b['fingerprint'])
        context=harness.source_context('line1\nline2\nline3\nline4\nline5',a)
        self.assertIn('4: line4',context)
        self.assertEqual(a['locations'][0]['line'],4)

    def test_failed_attempt_memory_survives_restart_and_allows_resource_retry(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'memory.json'; memory=harness.FailureMemory(path)
            syntax=harness.analyze('M.lean:3:2: error: No goals to be solved')
            resource=harness.analyze('M.lean:3:2: error: maximum number of heartbeats has been reached')
            memory.record('t','bad',syntax,False,[])
            memory.record('t','bad2',syntax,False,[])
            memory.record('u','large',resource,False,[])
            restored=harness.FailureMemory(path)
            self.assertTrue(restored.repeated_nonresource_candidate('t','bad'))
            self.assertFalse(restored.repeated_nonresource_candidate('u','large'))
            self.assertEqual(restored.summary('t')['same_failure_streak'],2)
            restored.record('t','valid',harness.analyze('',0),True,[])
            self.assertEqual(restored.summary('t')['same_failure_streak'],0)

    def test_policy_rejects_unbounded_resource_settings(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'deepseek_harness.json'
            for value in [{'max_heartbeats':0},{'max_rec_depth':999999},{'initial_rec_depth':8192},
                          {'max_heartbeats':10000000},{'arbitrary_setting':1}]:
                path.write_text(json.dumps(value))
                with self.subTest(value=value),self.assertRaises(ValueError):harness.policy(tmp)

    def test_hash_matches_text_and_exact_bytes(self):
        self.assertEqual(digest('Lean定理'),digest('Lean定理'.encode()))


if __name__=='__main__':unittest.main()
