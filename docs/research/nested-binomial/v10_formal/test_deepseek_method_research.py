"""Check experimental provenance and attribution using actual result-file fixtures."""
import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from deepseek_method_research import MethodResearch
from deepseek_goal import rooted
from deepseek_goal_worker import persist_attempt_records


class MethodResearchTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name);self.notes=self.root/'notes';self.notes.mkdir()
        (self.notes/'reference.md').write_text('Research source fixture')
        self.state={'jobs':{},'status':'paused'}
        self.methods=MethodResearch(self.state,self.root/'private',self.notes,self.notes,lambda p:rooted(self.notes,p))

    def card(self,name='derive-before-search'):
        return {'id':name,'title':'A research-method hypothesis','kind':'mathematical_strategy',
                'hypothesis':'Derive the missing input before searching for candidate statements.',
                'procedure':['Locate the missing dependency.','Try a fixed statement on the same goal.'],
                'success_criterion':'A missing input is verified without assuming that input.',
                'failure_criterion':'The proposed statement assumes the missing input.',
                'references':['reference.md']}

    def job(self):
        config={'module':'Fixture','goals':[['a','fixed signature a'],['b','fixed signature b']]}
        job={'status':'failed','config':config,'config_sha256':hashlib.sha256(json.dumps(config,sort_keys=True).encode()).hexdigest(),'runs':[]}
        self.state['jobs']['job']=job;return job

    def add_run(self,job,records):
        path=self.root/f'run-{len(job["runs"])}';path.mkdir()
        (path/'result.json').write_text(json.dumps({'records':records}))
        job['runs'].append(str(path));return path

    def attempt(self,name='a',accepted=True,seed=False,tokens=10,code=0):
        return {'theorem':name,'accepted':accepted,'exit_code':code,'seed_recompile':seed,
                'usage':None if seed else {'completion_tokens':tokens,'completion_tokens_details':{'reasoning_tokens':tokens//2}},
                'lean_elapsed_seconds':1.5,'harness_diagnostics':{'categories':[],'untrusted_axioms':[]}}

    def test_cards_are_versioned_and_cannot_add_executable_or_budget_options(self):
        self.methods.propose(self.card())
        with self.assertRaisesRegex(ValueError,'immutable'):self.methods.propose(self.card())
        for value in [dict(self.card('other'),max_tokens=999999),dict(self.card('../escape')),
                      dict(self.card('other'),references=['../../private.txt'])]:
            with self.assertRaises(ValueError):self.methods.propose(value)

    def test_baseline_is_frozen_and_reused_proofs_are_not_new_method_successes(self):
        job=self.job();self.add_run(job,[self.attempt(tokens=20),self.attempt('b',False,tokens=50,code=1)])
        self.methods.propose(self.card());before=copy.deepcopy(job['config'])
        self.methods.use({'method_id':'derive-before-search','job_id':'job'})
        trial=job['method_trials'][0]
        self.assertEqual(trial['baseline_metrics']['reported_completion_tokens'],70)
        self.assertEqual(job['config'],before)
        bad=self.attempt('bad',True,tokens=5);bad['harness_diagnostics']['untrusted_axioms']=['sorryAx']
        self.add_run(job,[self.attempt(seed=True),self.attempt('b',tokens=40),bad])
        job['status']='verified'
        self.assertEqual(len(self.methods.planning_context()['pending_evaluations']),1)
        result=self.methods.evaluate({'method_id':'derive-before-search','job_id':'job','decision':'keep','conclusion':'Observed one new checked obligation; a sequential observation only.'})
        self.assertEqual(result['metrics']['newly_generated_verified_theorems_with_known_usage'],['b'])
        self.assertEqual(result['metrics']['seed_recompilations'],1)
        self.assertNotIn('bad',result['metrics']['accepted_theorems'])
        self.assertFalse(result['causal_effect_established'])
        self.assertEqual(result['contract_sha256'],job['config_sha256'])
        self.assertEqual(self.state['status'],'paused')
        self.assertEqual(self.methods.planning_context()['pending_evaluations'],[])
        with self.assertRaisesRegex(ValueError,'already been evaluated'):
            self.methods.evaluate({'method_id':'derive-before-search','job_id':'job','decision':'keep','conclusion':'Changed prose'})

    def test_pauses_and_missing_reports_are_not_counted_as_mathematical_failures(self):
        job=self.job();job['status']='interrupted'
        self.methods.propose(self.card());self.methods.use({'method_id':'derive-before-search','job_id':'job'})
        path=self.root/'interrupted-run';path.mkdir();job['runs'].append(str(path))
        summary=self.methods.overview()['historical_jobs'][0]
        self.assertEqual(summary['incomplete_runs'],1)
        self.assertEqual(summary['metrics']['attempt_records'],0)
        with self.assertRaisesRegex(ValueError,'No completed attempt evidence'):
            self.methods.evaluate({'method_id':'derive-before-search','job_id':'job','decision':'drop','conclusion':'Cannot judge'})

    def test_a_new_method_does_not_relabel_the_previous_methods_attempts(self):
        job=self.job();self.methods.propose(self.card('first'));self.methods.propose(self.card('second'))
        self.methods.use({'method_id':'first','job_id':'job'});self.add_run(job,[self.attempt(accepted=False,code=1)])
        self.methods.use({'method_id':'second','job_id':'job'});self.add_run(job,[self.attempt()])
        job['status']='verified'
        old=self.methods.evaluate({'method_id':'first','job_id':'job','decision':'revise','conclusion':'This trial did not verify the goal.'})
        new=self.methods.evaluate({'method_id':'second','job_id':'job','decision':'keep','conclusion':'A later trial passed; context changed.'})
        self.assertEqual(old['metrics']['accepted_theorems'],[])
        self.assertEqual(old['trial_end_status'],'failed')
        self.assertEqual(new['metrics']['newly_generated_verified_theorems_with_known_usage'],['a'])

    def test_contract_changes_invalidate_method_evaluation(self):
        job=self.job();self.methods.propose(self.card());self.methods.use({'method_id':'derive-before-search','job_id':'job'})
        self.add_run(job,[self.attempt()]);job['config']['goals'][0][1]='weaker signature'
        with self.assertRaisesRegex(ValueError,'Frozen contract changed'):
            self.methods.evaluate({'method_id':'derive-before-search','job_id':'job','decision':'keep','conclusion':'Should be rejected'})

    def test_running_and_verified_proofs_cannot_be_reassigned(self):
        job=self.job();self.methods.propose(self.card())
        for status in ['running','verified','published']:
            job['status']=status
            with self.assertRaises(ValueError):self.methods.use({'method_id':'derive-before-search','job_id':'job'})

    def test_public_records_survive_resume_and_exclude_private_result_paths(self):
        job=self.job();self.methods.propose(self.card());self.methods.use({'method_id':'derive-before-search','job_id':'job'})
        self.add_run(job,[self.attempt()]);job['status']='published'
        self.methods.evaluate({'method_id':'derive-before-search','job_id':'job','decision':'keep','conclusion':'One sequential observation.'})
        restored=MethodResearch(json.loads(json.dumps(self.state)),self.root/'private',self.notes,self.notes,lambda p:rooted(self.notes,p))
        restored.save_public()
        text=(self.notes/'DEEPSEEK_METHOD_RESEARCH.json').read_text()
        self.assertNotIn(str(self.root),text)
        self.assertIn('causal_effect_established',text)
        self.assertEqual(restored.planning_context()['active_method_id'],'derive-before-search')

    def test_unknown_usage_and_timing_are_not_attributed_as_zero_cost_success(self):
        record=self.attempt();record['usage']={};record.pop('lean_elapsed_seconds')
        m=self.methods.metrics([record])
        self.assertEqual(m['attempts_without_usage'],1)
        self.assertEqual(m['attempts_without_Lean_timing'],1)
        self.assertEqual(m['newly_generated_verified_theorems_with_known_usage'],[])
        self.assertIn('excludes planner',m['token_measurement_scope'])

    def test_durable_attempts_remain_measurable_when_the_later_api_review_fails(self):
        job=self.job();self.methods.propose(self.card());self.methods.use({'method_id':'derive-before-search','job_id':'job'})
        run=self.root/'review-failed';run.mkdir();job['runs'].append(str(run))
        persist_attempt_records(run,[self.attempt()])
        self.assertFalse((run/'result.json').exists())
        result=self.methods.evaluate({'method_id':'derive-before-search','job_id':'job','decision':'revise','conclusion':'The proof passed, but final review did not return.'})
        self.assertEqual(result['metrics']['newly_generated_verified_theorems_with_known_usage'],['a'])
        self.assertFalse(result['run_evidence'][0]['module_review_report_available'])
        self.assertIn('attempt_records_sha256',result['run_evidence'][0])
        self.assertFalse((run/'attempt_records.tmp').exists())


if __name__=='__main__':unittest.main()
