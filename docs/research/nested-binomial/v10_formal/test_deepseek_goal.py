"""Offline tests for goal ownership, immutable targets and resumable limits."""
import copy
import json
import os
from pathlib import Path
import tempfile
import time
import unittest
from unittest.mock import patch

import deepseek_goal as goal
import deepseek_goal_budget as budget
import check_additional_formalization as checker


class GoalTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name) / 'repo'
        self.notes = self.repo / 'notes'; self.formal = self.notes / 'formal'
        self.formal.mkdir(parents=True)
        self.skill = self.repo / 'SKILL.md'; self.skill.write_text('DeepSeek chooses each action.')
        (self.notes / 'notes.md').write_text('Real source supplied to the planner.')
        (self.formal / 'deepseek_generation_checks.json').write_text('{"accepted_theorem_count":35}')
        target = {'module': 'FinalGoal', 'name': 'final_goal',
                  'statement': 'theorem final_goal : forall n : Nat, n = n'}
        target['statement_sha256'] = goal.digest(target['statement'])
        self.spec = {'id': 'test', 'objective': 'Finish the exact frozen test contract',
                     'targets': [target], 'initial_research_files': ['notes.md']}
        self.spec_path = self.repo / 'goal.json'; goal.write_json(self.spec_path, self.spec)
        for name, value in [('REPO', self.repo), ('ROOT', self.formal), ('NOTES', self.notes),
                            ('SKILL', self.skill), ('PROGRESS', self.notes / 'progress.md')]:
            item = patch.object(goal, name, value); item.start(); self.addCleanup(item.stop)
        self.agent = goal.GoalAgent(Path(self.temp.name) / 'run', self.spec_path)

    def config(self, module='Step'):
        return {'module': module, 'imports': 'import Mathlib.Tactic', 'definitions': '',
                'goals': [['step', 'theorem step : forall n : Nat, n = n']]}

    def test_model_actions_drive_loop_and_checkpoints_do_not_finish(self):
        actions = [
            {'action': 'read_research', 'arguments': {'path': 'notes.md'}},
            {'action': 'checkpoint', 'arguments': {'summary': 'Next task selected by DeepSeek'}},
            {'action': 'request_completion', 'arguments': {}},
            {'action': 'done', 'arguments': {}},
        ]
        calls = []
        def fake(messages):
            calls.append(messages)
            return {'choices': [{'finish_reason': 'stop', 'message': {'content': json.dumps(actions[len(calls)-1])}}]}
        with patch.object(goal, 'api', fake):
            state = self.agent.run(max_actions=4, max_hours=.1, max_completion_tokens=4096)
        self.assertEqual(state['status'], 'action_limit')
        self.assertEqual(state['steps'], 4)
        self.assertEqual(len(calls), 4)
        self.assertIn('Real source supplied', calls[1][-1]['content'])
        self.assertEqual(calls[0][-1]['role'], 'user')
        self.assertFalse(state['last_observation']['goal_complete'])
        self.assertIn('no self-reported done', state['last_observation']['tool_error'])
        restored = goal.GoalAgent(self.agent.run_dir, self.spec_path)
        self.assertEqual(restored.state['steps'], 4)

    def test_final_target_cannot_be_weakened_or_shadowed(self):
        target = self.spec['targets'][0]
        config = {'module': target['module'], 'imports': 'import Mathlib.Tactic', 'definitions': '',
                  'goals': [[target['name'], target['statement']]]}
        self.assertEqual(goal.validate_job(config, [target])['goals'], config['goals'])
        for altered in [dict(config, goals=[['final_goal', 'theorem final_goal : True']]),
                        dict(config, definitions='def hidden := True'),
                        dict(config, imports='import Mathlib.Tactic\n#eval 1'),
                        dict(config, definitions='notation "bad" => True')]:
            with self.assertRaises(ValueError): goal.validate_job(altered, [target])

    def test_paths_reject_escape_symlinks_and_secret_types(self):
        outside = Path(self.temp.name) / 'outside.txt'; outside.write_text('private')
        (self.notes / 'link.txt').symlink_to(outside)
        (self.notes / '.env').write_text('private')
        for path in ['../../outside.txt', str(outside), 'link.txt', '.env']:
            with self.subTest(path=path), self.assertRaises(ValueError): goal.rooted(self.notes, path)

    def test_job_is_reviewed_and_frozen_before_proof_execution(self):
        response = {'choices': [{'message': {'content': '{"verdict":"PASS","feedback":"needed dependency"}'}}]}
        with patch.object(goal, 'api', return_value=response):
            accepted = self.agent.propose({'config': self.config(), 'why_needed': 'Required dependency for the frozen target',
                                           'extra_context': ['notes.md']})
        key = accepted['job_id']
        path = self.agent.run_dir / 'jobs' / key / 'fixed_job.json'
        modified = json.loads(path.read_text()); modified['goals'][0][1] = 'theorem step : True'
        goal.write_json(path, modified)
        with patch.object(goal.subprocess, 'Popen') as run:
            with self.assertRaisesRegex(ValueError, 'contract changed'): self.agent.worker(key)
            run.assert_not_called()

    def test_unverified_job_cannot_publish_or_complete(self):
        self.agent.state['jobs']['j'] = {'status': 'ready', 'config': self.config(), 'why_needed': 'test'}
        with patch.object(goal.subprocess, 'run') as execute:
            self.assertEqual(self.agent.publish()['published'], [])
            execute.assert_not_called()
        self.assertFalse(self.agent.completion()['complete'])
        self.assertNotEqual(self.agent.state['status'], 'complete')

    def test_goal_contract_changes_require_a_separate_goal(self):
        self.agent.save()
        changed = copy.deepcopy(self.spec); changed['objective'] = 'Weaker goal'
        goal.write_json(self.spec_path, changed)
        with self.assertRaisesRegex(ValueError, 'Goal changed'):
            goal.GoalAgent(self.agent.run_dir, self.spec_path)

    def test_status_reads_do_not_mark_live_workers_interrupted(self):
        self.agent.state['jobs']['j'] = {'status': 'running', 'config': self.config(), 'why_needed': 'test'}
        self.agent.save()
        restored = goal.GoalAgent(self.agent.run_dir, self.spec_path)
        self.assertEqual(restored.state['jobs']['j']['status'], 'running')

    def test_last_action_completion_is_not_overwritten_and_completed_goal_does_not_restart(self):
        response = {'choices':[{'finish_reason':'stop','message':{'content':'{"action":"request_completion","arguments":{}}'}}]}
        def finished():
            self.agent.state['status'] = 'complete'
            return {'complete':True}
        with patch.object(goal, 'api', return_value=response), patch.object(self.agent, 'completion', finished):
            self.assertEqual(self.agent.run(max_actions=1)['status'], 'complete')
        with patch.object(goal, 'api') as model:
            self.assertEqual(self.agent.run(max_actions=1)['status'], 'complete')
            model.assert_not_called()


class BudgetTests(unittest.TestCase):
    def test_shared_budget_caps_request_and_accounts_reported_usage(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'budget.json'
            goal.write_json(path, {'max_completion_tokens': 5000, 'used_completion_tokens': 2000,
                                   'deadline': time.time()+60, 'api_calls': 0})
            with patch.dict(os.environ, {'DEEPSEEK_GOAL_BUDGET_FILE': str(path)}):
                settings, selected = budget.before_call({'max_tokens': 131072, 'request_timeout_seconds': 1800})
            self.assertEqual(settings['max_tokens'], 3000)
            self.assertLessEqual(settings['request_timeout_seconds'], 60)
            budget.record_usage(selected, {'model': 'deepseek', 'usage': {'completion_tokens': 1200,
                'completion_tokens_details': {'reasoning_tokens': 1000}}}, settings)
            data = json.loads(path.read_text())
            self.assertEqual(data['used_completion_tokens'], 3200)
            self.assertEqual(data['api_calls'], 1)
            self.assertEqual(data['last_usage']['reasoning_tokens'], 1000)

    def test_limits_stop_without_marking_goal_complete_and_unknown_usage_is_charged(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'budget.json'
            goal.write_json(path, {'max_completion_tokens': 2000, 'used_completion_tokens': 0,
                                   'deadline': time.time()+60})
            budget.record_usage(path, {}, {'max_tokens': 2000})
            with patch.dict(os.environ, {'DEEPSEEK_GOAL_BUDGET_FILE': str(path)}):
                with self.assertRaises(budget.GoalBudgetExceeded):
                    budget.before_call({'max_tokens': 131072, 'request_timeout_seconds': 1800})
            goal.write_json(path, {'max_completion_tokens': 2000, 'used_completion_tokens': 0,
                                   'deadline': time.time()-1})
            with patch.dict(os.environ, {'DEEPSEEK_GOAL_BUDGET_FILE': str(path)}):
                with self.assertRaises(budget.GoalBudgetExceeded):
                    budget.before_call({'max_tokens': 131072, 'request_timeout_seconds': 1800})


class RegistryTests(unittest.TestCase):
    def test_registered_modules_include_dependencies_in_order(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root/'A.lean').write_text('import Mathlib.Tactic\n')
            (root/'B.lean').write_text('import A\n')
            (root/'goal_verified_modules.json').write_text('{"modules":["B"]}')
            with patch.object(checker, 'ROOT', root):
                self.assertEqual([p.stem for p in checker.include_goal_modules([])], ['A', 'B'])
                (root/'A.lean').write_text('import B\n')
                with self.assertRaisesRegex(ValueError, 'Cyclic'): checker.include_goal_modules([])


if __name__ == '__main__': unittest.main()
