"""Evidence-backed research on mathematical strategies and formalization methods.

DeepSeek authors hypotheses and conclusions. This module records assignments and
measures actual fixed-contract attempts; it does not judge mathematics or execute
method cards as code. Sequential observations are not controlled causal evidence.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import re


def bounded_text(value, label, maximum=3000):
    if not isinstance(value, str) or not 1 <= len(value) <= maximum:
        raise ValueError(label + ' must be nonempty bounded text')
    return value


class MethodResearch:
    def __init__(self, state, run_dir, notes, formal, resolve):
        self.state, self.run_dir = state, Path(run_dir)
        self.notes, self.formal, self.resolve = Path(notes), Path(formal), resolve
        state.setdefault('research_methods', {})
        state.setdefault('method_evaluations', [])

    def propose(self, args):
        keys = {'id','title','kind','hypothesis','procedure','success_criterion','failure_criterion','references'}
        if not isinstance(args,dict) or set(args)-keys:
            raise ValueError('Invalid method schema; method cards contain data, not executable actions')
        name = args.get('id')
        if not isinstance(name,str) or not re.fullmatch(r'[a-z][a-z0-9_-]{0,63}',name):
            raise ValueError('Use a short lowercase method id')
        methods = self.state['research_methods']
        if name in methods or len(methods)>=24:
            raise ValueError('Method cards are immutable; use a new id for a revision, at most 24 cards')
        if args.get('kind') not in {'mathematical_strategy','formalization','certificate_design'}:
            raise ValueError('Unsupported research method kind')
        for key in ['title','hypothesis','success_criterion','failure_criterion']:
            bounded_text(args.get(key),key,200 if key=='title' else 3000)
        procedure=args.get('procedure')
        if not isinstance(procedure,list) or not 1<=len(procedure)<=10:
            raise ValueError('Use 1..10 research steps')
        for step in procedure:bounded_text(step,'procedure step',1200)
        refs=args.get('references',[])
        if not isinstance(refs,list) or len(refs)>6:raise ValueError('Use at most six existing research references')
        for ref in refs:self.resolve(ref)
        methods[name]={**args,'references':refs,'status':'hypothesis','author':'DeepSeek',
                       'not_a_proof':True,'checker_or_budget_changes_allowed':False}
        return {'method_recorded':name,'status':'hypothesis','requires_actual_trial':True}

    def use(self,args):
        name=args['method_id'];card=self.state['research_methods'][name]
        job_id=args.get('job_id')
        if job_id is not None:
            job=self.state['jobs'][job_id]
            if job['status'] not in {'ready','failed','interrupted'}:
                raise ValueError('Assign methods before proof work or between unsuccessful runs; verified bodies stay immutable')
            trials=job.setdefault('method_trials',[])
            if trials and trials[-1].get('end_run_count') is None:
                if trials[-1]['method_id']==name:
                    self.state['active_method_id']=name
                    return {'already_assigned':True,'method_id':name,'job_id':job_id}
                trials[-1]['end_run_count']=len(job['runs'])
                trials[-1]['end_job_status']=job['status']
            baseline=self.records(job['runs'])
            trials.append({'method_id':name,'start_run_count':len(job['runs']),
                           'contract_sha256':job['config_sha256'],
                           'baseline_accepted_theorems':self.metrics(baseline)['accepted_theorems'],
                           'baseline_metrics':self.metrics(baseline)})
            directory=self.run_dir/'methods';directory.mkdir(parents=True,exist_ok=True)
            path=directory/(name+'.md')
            path.write_text('DeepSeek research-method hypothesis, not a proof or permission to change the contract:\n'+
                            json.dumps(card,ensure_ascii=False,indent=2)+'\n')
            path.chmod(0o600);job['method_context']=[str(path)]
            card['status']='experimental'
        self.state['active_method_id']=name
        return {'method_id':name,'job_id':job_id,'status':'experimental',
                'frozen_contract_unchanged':True,'causal_effect_established':False}

    @staticmethod
    def records(runs):
        records=[]
        for run in map(Path,runs):
            report=run/'result.json'
            if report.exists():
                records.extend(json.loads(report.read_text()).get('records',[]))
        return records

    @staticmethod
    def metrics(records,baseline=()):
        accepted=set();new=set();categories=Counter()
        completion=reasoning=unknown=seed_recompiles=0;seconds=0;timed=0
        for record in records:
            usage=record.get('usage')
            tokens=usage.get('completion_tokens') if isinstance(usage,dict) else None
            known_usage=type(tokens) is int and tokens>=0
            if known_usage:
                completion+=tokens
                reasoning+=(usage.get('completion_tokens_details') or {}).get('reasoning_tokens',0) or 0
            else:unknown+=1
            seeded=record.get('seed_recompile') is True
            seed_recompiles+=seeded
            trusted = record.get('exit_code') == 0 and not record.get('harness_diagnostics',{}).get('untrusted_axioms')
            if record.get('accepted') and record.get('theorem') and trusted:
                name=record['theorem'];accepted.add(name)
                if name not in baseline and record.get('seed_recompile') is False and known_usage:new.add(name)
            categories.update(record.get('harness_diagnostics',{}).get('categories',[]))
            duration=record.get('lean_elapsed_seconds')
            if duration is None and record.get('resource_attempts'):
                duration=record['resource_attempts'][-1].get('elapsed_seconds')
            if isinstance(duration,(int,float)) and duration>=0:seconds+=duration;timed+=1
        return {'attempt_records':len(records),'accepted_theorems':sorted(accepted),
                'newly_generated_verified_theorems_with_known_usage':sorted(new),
                'seed_recompilations':seed_recompiles,'reported_completion_tokens':completion,
                'reported_reasoning_tokens':reasoning,'attempts_without_usage':unknown,
                'recorded_Lean_seconds':round(seconds,3),'error_categories':dict(categories),
                'attempts_with_Lean_timing':timed,'attempts_without_Lean_timing':len(records)-timed,
                'token_measurement_scope':'Candidate response records only; excludes planner, scope/repair critics and final review',
                'completion_tokens_are_not_a_billing_guarantee':True}

    def evaluate(self,args):
        name=args['method_id'];self.state['research_methods'][name]
        job_id=args['job_id'];job=self.state['jobs'][job_id]
        if job['status']=='running':raise ValueError('Evaluate after the current fixed-job run returns')
        trials=[(i,t) for i,t in enumerate(job.get('method_trials',[])) if t['method_id']==name]
        if not trials:raise ValueError('No actual assignment for this method and job')
        index,trial=trials[-1]
        actual=hashlib.sha256(json.dumps(job['config'],sort_keys=True).encode()).hexdigest()
        if trial['contract_sha256']!=job['config_sha256'] or actual!=job['config_sha256']:
            raise ValueError('Frozen contract changed')
        runs=job['runs'][trial['start_run_count']:trial.get('end_run_count',len(job['runs']))]
        records=self.records(runs)
        if not records:raise ValueError('No completed attempt evidence; pauses and missing reports are not mathematical failures')
        decision=args.get('decision')
        if decision not in {'keep','revise','drop'}:raise ValueError('Use keep, revise or drop as an advisory decision')
        conclusion=bounded_text(args.get('conclusion'),'conclusion')
        evidence={'method_id':name,'job_id':job_id,'trial':index,
                  'contract_sha256':job['config_sha256'],
                  'baseline_metrics':trial['baseline_metrics'],
                  'run_evidence':[{'run':Path(r).name,'result_sha256':hashlib.sha256((Path(r)/'result.json').read_bytes()).hexdigest()}
                                  for r in runs if (Path(r)/'result.json').exists()],
                  'metrics':self.metrics(records,trial['baseline_accepted_theorems'])}
        evidence_id=hashlib.sha256(json.dumps(evidence,sort_keys=True).encode()).hexdigest()
        row={**evidence,'evidence_id':evidence_id,'actual_job_status':job['status'],
             'trial_end_status':trial.get('end_job_status',job['status']),
             'model_conclusion':conclusion,'advisory_decision':decision,'causal_effect_established':False,
             'comparison_limit':'Sequential, non-randomized observations on a frozen contract; context and attempts can differ'}
        history=self.state['method_evaluations']
        if any(e['evidence_id']==evidence_id for e in history):raise ValueError('This unchanged evidence has already been evaluated')
        history.append(row)
        self.state['research_methods'][name]['status']='observed; causal superiority unestablished'
        return row

    def overview(self):
        return {'active_method_id':self.state.get('active_method_id'),
                'methods':self.state['research_methods'],
                'evaluations':self.state['method_evaluations'][-8:],
                'historical_jobs':[{'job_id':key,'module':job['config']['module'],'status':job['status'],
                                    'contract_sha256':job.get('config_sha256'),
                                    'incomplete_runs':sum(not (Path(r)/'result.json').exists() for r in job.get('runs',[])),
                                    'metrics':self.metrics(self.records(job.get('runs',[])))}
                                   for key,job in self.state['jobs'].items()],
                'method_self_reports_are_not_verification':True}

    def planning_context(self):
        methods=self.state['research_methods'];active=self.state.get('active_method_id')
        selected=set(list(methods)[-3:]) | ({active} if active else set())
        return {'active_method_id':active,'cards':{k:v for k,v in methods.items() if k in selected},
                'other_cards':[{'id':k,'title':v['title'],'status':v['status']} for k,v in methods.items() if k not in selected],
                'recent_evaluations':self.state['method_evaluations'][-4:],
                'pending_evaluations':self.pending_evaluations()}

    def pending_evaluations(self):
        pending=[]
        for key,job in self.state['jobs'].items():
            if job['status']=='running':continue
            for index,trial in enumerate(job.get('method_trials',[])):
                runs=job['runs'][trial['start_run_count']:trial.get('end_run_count',len(job['runs']))]
                records=self.records(runs)
                if not records:continue
                hashes=[{'run':Path(r).name,'result_sha256':hashlib.sha256((Path(r)/'result.json').read_bytes()).hexdigest()}
                        for r in runs if (Path(r)/'result.json').exists()]
                if any(e['job_id']==key and e['trial']==index and e['run_evidence']==hashes
                       for e in self.state['method_evaluations']):continue
                pending.append({'job_id':key,'method_id':trial['method_id'],'trial':index,
                                'metrics':self.metrics(records,trial['baseline_accepted_theorems']),
                                'model_evaluation_pending':True})
        return pending[:8]

    def public_state(self):
        # No raw API responses, prompts, compiler source excerpts or private paths.
        return {'active_method_id':self.state.get('active_method_id'),
                'methods':self.state['research_methods'],'evaluations':self.state['method_evaluations'],
                'pending_trials':self.pending_evaluations(),
                'causal_effect_established':False,'proofs_require_the_unchanged_Lean_checker':True}

    def save_public(self):
        state=self.public_state()
        (self.notes/'DEEPSEEK_METHOD_RESEARCH.json').write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n')
        lines=['# DeepSeekによる数学研究手法の研究','',
               '手法の仮説・実験・実測結果を保持する。手法の自己申告は証明ではなく、固定型のLean検証を必要とする。',
               '同じ定理でも逐次試行は文脈が変わるため、因果効果や一般的優越性を証明したとは扱わない。','',
               '| 手法 | 種類 | 状態 |','| --- | --- | --- |']
        lines += [f"| {m['title']} | {m['kind']} | {m['status']} |" for m in state['methods'].values()]
        lines += ['','## 実測した試行','']
        for row in state['evaluations'][-16:]:
            metric=row['metrics']
            lines += [f"- {row['method_id']} / {row['job_id']}: {metric['attempt_records']}試行、"
                      f"新規検証 {len(metric['newly_generated_verified_theorems_with_known_usage'])}定理、"
                      f"報告出力 {metric['reported_completion_tokens']}トークン。判断: {row['advisory_decision']}。",
                      '  DeepSeekの評価: '+row['model_conclusion']]
        (self.notes/'DEEPSEEK_METHOD_RESEARCH.md').write_text('\n'.join(lines).rstrip()+'\n')
