"""Offline tests for goal ownership, immutable targets and resumable limits."""
import copy
import gzip
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

    def test_observed_sources_survive_resume_and_duplicate_reads_replace_cache(self):
        action = {'action':'read_research','arguments':{'path':'notes.md','start':1,'count':100}}
        self.agent.remember(action, {'content':'observed source'})
        action['arguments']['count'] = 200
        self.agent.remember(action, {'content':'more complete source'})
        self.agent.save()
        restored = goal.GoalAgent(self.agent.run_dir, self.spec_path)
        memory = restored.snapshot()['working_memory']
        self.assertEqual(len(memory), 1)
        self.assertIn('more complete source', memory[0]['observed_tool_result'])
        self.assertTrue(memory[0]['not_a_verification'])

    def test_search_globs_are_relative_to_the_selected_source_root(self):
        base = self.repo/'Mathlib'; (base/'Algebra').mkdir(parents=True)
        (base/'Algebra'/'Fixture.lean').write_text('theorem needle_marker : True := by trivial\n')
        result = self.agent.search(base, {'query':'needle_marker','glob':'Algebra/**'})
        self.assertEqual(result['exit_code'], 0)
        self.assertIn('Algebra/Fixture.lean', result['output'])

    def test_pause_during_model_response_prevents_starting_another_tool(self):
        def decision():
            (self.agent.run_dir/'PAUSE').write_text('pause')
            return {'action':'checkpoint','arguments':{'summary':'must not execute'}}
        with patch.object(self.agent, 'decision', decision), patch.object(self.agent, 'execute') as tool:
            result = self.agent.run(max_actions=2)
        self.assertEqual(result['status'], 'paused')
        tool.assert_not_called()

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

    def test_seed_recovery_preserves_accepted_bodies_and_rechecks_lint_only_candidate(self):
        old=self.agent.run_dir/'old';new=self.agent.run_dir/'new'
        old.mkdir();new.mkdir()
        config=self.config();config['goals'].append(['next','theorem next : True'])
        original='by\n  exact True.intro'
        accepted='by\n  intro n\n  rfl'
        goal.write_json(new/'accepted_proofs.json',{'step':accepted})
        records=[]
        for index,name,proof in [(1,'step','older unused body'),(2,'next',original)]:
            source='Exact stored model source '+name
            prefix=old/f'{index}-1'
            prefix.with_suffix('.lean').write_text(source)
            prefix.with_suffix('.compiler.txt').write_text(
                "M.lean:2:2: warning: Variable name `h` is not explicitly referenced.\n"
                "'t' depends on axioms: [propext, Classical.choice, Quot.sound]\n")
            goal.write_json(prefix.with_suffix('.response.json'),{'choices':[{'message':{'content':json.dumps({'proof':proof})}}]})
            records.append({'theorem':name,'attempt':1,'exit_code':0,'source_sha256':goal.digest(source)})
        goal.write_json(old/'result.json',{'records':records})
        job={'config':config,'runs':[str(old),str(new)]}
        self.assertEqual(self.agent.recover_seeds(job),{'step':accepted,'next':original})
        (old/'2-1.lean').write_text('changed source')
        self.assertEqual(self.agent.recover_seeds(job),{'step':accepted})

    def test_disagreeing_accepted_prefixes_are_rejected(self):
        runs=[]
        for i in [1,2]:
            p=self.agent.run_dir/str(i);p.mkdir();runs.append(str(p))
            goal.write_json(p/'accepted_proofs.json',{'step':'different body '+str(i)})
        with self.assertRaisesRegex(ValueError,'prefix changed'):
            self.agent.recover_seeds({'config':self.config(),'runs':runs})

    def test_focused_context_updates_preserve_frozen_contract(self):
        response={'choices':[{'message':{'content':'{"verdict":"PASS"}'}}]}
        with patch.object(goal,'api',return_value=response):
            job_id=self.agent.propose({'config':self.config(),'why_needed':'Necessary fixed-target dependency'})['job_id']
        job=self.agent.state['jobs'][job_id]
        frozen=(self.agent.run_dir/'jobs'/job_id/'fixed_job.json').read_bytes()
        result=self.agent.update_context({'job_id':job_id,'extra_context':['notes.md']})
        self.assertEqual(result['unchanged_contract_sha256'],goal.digest(json.dumps(job['config'],sort_keys=True)))
        self.assertEqual((self.agent.run_dir/'jobs'/job_id/'fixed_job.json').read_bytes(),frozen)
        self.assertIn(str(self.notes/'notes.md'),job['extra_context'])
        with self.assertRaises(ValueError):
            self.agent.update_context({'job_id':job_id,'extra_context':['../../outside.txt']})

    def test_plan_cannot_self_declare_evidence_or_change_final_goal(self):
        plan=[{'id':'bridge','objective':'Bridge the remaining assumptions','depends_on':[],'modules':['Unproved']},
              {'id':'finish','objective':'Discharge frozen target','depends_on':['bridge'],'modules':['FinalGoal']}]
        result=self.agent.set_plan({'milestones':plan})
        self.assertTrue(result['final_targets_unchanged'])
        self.assertEqual(result['plan'][0]['module_evidence_present'],[])
        self.assertFalse(result['plan'][1]['semantic_goal_completion'])
        bad=copy.deepcopy(plan);bad[0]['depends_on']=['finish']
        with self.assertRaisesRegex(ValueError,'cyclic'):self.agent.set_plan({'milestones':bad})
        bad=copy.deepcopy(plan);bad[0]['status']='complete'
        with self.assertRaises(ValueError):self.agent.set_plan({'milestones':bad})
        self.assertEqual(self.agent.state['milestones'],plan)

    def test_unrecoverable_publication_failure_stops_without_spending_more_model_actions(self):
        action={'action':'publish','arguments':{}}
        for error in [goal.PublicationBlocked('actual git failure: permission denied'),
                      goal.subprocess.CalledProcessError(1,['git','commit'],stderr='permission denied')]:
            with self.subTest(error=type(error).__name__):
                before=self.agent.state['steps']
                with patch.object(self.agent,'decision',return_value=action) as model, patch.object(
                        self.agent,'execute',side_effect=error):
                    result=self.agent.run(max_actions=8,max_hours=.1,max_completion_tokens=4096)
                self.assertEqual(result['status'],'blocked')
                self.assertEqual(result['steps'],before+1)
                self.assertTrue(result['last_observation']['publication_blocked'])
                self.assertFalse(result['last_observation']['retry_in_this_round'])
                self.assertIn('permission denied',result['last_error'])
                self.assertEqual(model.call_count,1)

    def test_resume_clears_stale_error_but_retains_action_logs(self):
        self.agent.state['last_error']='old connection failure'
        with patch.object(self.agent,'decision',return_value={'action':'checkpoint','arguments':{'summary':'Continue verified work'}}):
            result=self.agent.run(max_actions=1,max_hours=.1,max_completion_tokens=4096)
        self.assertEqual(result['status'],'action_limit')
        self.assertIsNone(result['last_error'])
        self.assertTrue((self.agent.run_dir/'0001.action.json').exists())

    def test_method_is_inherited_without_mutating_a_new_frozen_job(self):
        card={'id':'input-first','title':'Derive inputs first','kind':'mathematical_strategy',
              'hypothesis':'First derive the missing input.','procedure':['Inspect the actual dependency.'],
              'success_criterion':'Input verified','failure_criterion':'Input assumed','references':['notes.md']}
        self.agent.execute({'action':'propose_method','arguments':card})
        self.agent.execute({'action':'use_method','arguments':{'method_id':'input-first'}})
        response={'choices':[{'message':{'content':'{"verdict":"PASS"}'}}]}
        with patch.object(goal,'api',return_value=response):
            result=self.agent.propose({'config':self.config(),'why_needed':'Required dependency for fixed target'})
        job=self.agent.state['jobs'][result['job_id']]
        frozen=json.loads((self.agent.run_dir/'jobs'/result['job_id']/'fixed_job.json').read_text())
        self.assertEqual(job['config'],frozen)
        self.assertEqual(job['method_trials'][0]['method_id'],'input-first')
        self.assertTrue(Path(job['method_context'][0]).is_file())

    def test_gzip_certificate_reads_are_bounded_and_not_allowed_as_job_context(self):
        path=self.notes/'certificate.json.gz'
        with gzip.open(path,'wb') as stream:stream.write(b'{\n  "value": 42\n}\n')
        result=self.agent.execute({'action':'read_research','arguments':{'path':path.name,'start':2,'count':1}})
        self.assertEqual(result['content'],'2:   "value": 42')
        self.assertIn(path.name,self.agent.execute({'action':'list_research','arguments':{}})['files'])
        with self.assertRaises(ValueError):goal.rooted(self.notes,path.name)
        with patch.object(goal,'MAX_COMPRESSED_CONTENT',8),self.assertRaisesRegex(ValueError,'bounded'):
            self.agent.execute({'action':'read_research','arguments':{'path':path.name}})

    def test_github_observations_use_only_the_authorized_pr_and_do_not_certify_Lean(self):
        self.agent.goal.update(repository='owner/research',pr=1,branch='research')
        pr={'html_url':'https://github.com/owner/research/pull/1','title':'Research','draft':True,
            'head':{'sha':'abcdef','ref':'research'}}
        checks={'check_runs':[{'name':'unit tests','status':'completed','conclusion':'success'}]}
        responses=[goal.subprocess.CompletedProcess([],0,json.dumps(v),'') for v in [pr,checks]]
        with patch.object(goal.subprocess,'run',side_effect=responses) as call:
            result=self.agent.execute({'action':'github_status','arguments':{}})
        self.assertEqual([c.args[0] for c in call.call_args_list],
                         [['gh','api','repos/owner/research/pulls/1'],['gh','api','repos/owner/research/commits/abcdef/check-runs']])
        self.assertTrue(result['not_Lean_proof_evidence'])
        with self.assertRaisesRegex(ValueError,'no overrides'):
            self.agent.execute({'action':'github_status','arguments':{'repository':'different/repository'}})


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
    def test_reuse_requires_matching_logs_and_dependencies(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "docs/research/nested-binomial/v10_formal"
            root.mkdir(parents=True)
            sources = [root / f"{name}.lean" for name in ("Base", "Dependent", "Unrelated")]
            report = {"status": "PASS", "lean_version": "pinned", "mathlib_commit": "pinned", "records": []}
            for source, text in zip(sources, ("def x := 1", "import Base", "def y := 2")):
                source.write_text(text)
                log = source.with_suffix(".additional_check.txt")
                log.write_text("checked")
                report["records"].append({
                    "source": source.name, "source_sha256": checker.sha256(source),
                    "log": log.name, "log_sha256": checker.sha256(log), "exit_code": 0,
                    "proof_hole_or_custom_axiom_detected": False,
                })
            with patch.object(checker, "ROOT", root), patch.object(
                    checker.subprocess, "check_output", side_effect=["commit", json.dumps(report)] * 2):
                cached, _ = checker.reusable_records(sources, "pinned", "pinned")
                self.assertEqual(set(cached), {source.name for source in sources})
                sources[0].with_suffix(".additional_check.txt").write_text("changed")
                cached, _ = checker.reusable_records(sources, "pinned", "pinned")
                self.assertEqual(set(cached), {"Unrelated.lean"})

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
