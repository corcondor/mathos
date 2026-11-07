"""Exercise concurrent writers using real temporary Git repositories, with no network."""
import hashlib
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import deepseek_publication as publication


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name); self.remote = self.root/'remote.git'
        self.a = self.root/'a'; self.b = self.root/'b'; self.branch = 'research'
        self.command(self.root, 'init', '--bare', str(self.remote))
        self.command(self.root, 'clone', str(self.remote), str(self.a))
        self.identity(self.a); self.command(self.a,'switch','-c',self.branch)
        self.commit(self.a,'Proof.lean','-- fixed verified-input fixture\n')
        self.command(self.a,'push','origin',self.branch)
        self.command(self.root,'clone','--branch',self.branch,str(self.remote),str(self.b))
        self.identity(self.b)
        self.origins={str(self.remote)}
        self.protected=self.evidence()

    def command(self, directory, *args):
        return subprocess.run(['git',*args],cwd=directory,check=True,capture_output=True,text=True).stdout.strip()

    def identity(self, repo):
        self.command(repo,'config','user.email','test@example.invalid')
        self.command(repo,'config','user.name','Publication test')

    def commit(self, repo, name, text):
        (repo/name).write_text(text)
        self.command(repo,'add','--',name); self.command(repo,'commit','-m',name)
        return self.command(repo,'rev-parse','HEAD')

    def advance_remote(self, index=1, name=None):
        result=self.commit(self.b,name or f'remote-{index}.md',f'External research update {index}\n')
        self.command(self.b,'push','origin',self.branch)
        return result

    def evidence(self):
        return {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in self.a.glob('*.lean')}

    def test_diverged_research_histories_merge_without_changing_verified_source(self):
        local=self.commit(self.a,'local.md','Verified local result\n');remote=self.advance_remote()
        result=publication.synchronize(self.a,self.branch,self.origins,self.protected)
        self.assertEqual(result['status'],'merged')
        self.assertEqual(self.evidence(),self.protected)
        for ancestor in [local,remote]:self.command(self.a,'merge-base','--is-ancestor',ancestor,'HEAD')
        self.assertTrue((self.a/'local.md').exists());self.assertTrue((self.a/'remote-1.md').exists())

    def test_incoming_verified_source_edit_is_blocked_before_overwrite(self):
        original=(self.a/'Proof.lean').read_bytes();head=self.command(self.a,'rev-parse','HEAD')
        self.advance_remote(name='Proof.lean')
        with self.assertRaisesRegex(publication.PublicationBlocked,'verified source'):
            publication.synchronize(self.a,self.branch,self.origins,self.protected)
        self.assertEqual((self.a/'Proof.lean').read_bytes(),original)
        self.assertEqual(self.command(self.a,'rev-parse','HEAD'),head)

    def test_conflicting_notes_abort_merge_and_preserve_local_work(self):
        self.commit(self.a,'shared.md','local\n');self.advance_remote(name='shared.md')
        with self.assertRaisesRegex(publication.PublicationBlocked,'merge blocked'):
            publication.synchronize(self.a,self.branch,self.origins,self.protected)
        self.assertEqual((self.a/'shared.md').read_text(),'local\n')
        self.assertFalse((self.a/'.git/MERGE_HEAD').exists())
        self.assertEqual(self.command(self.a,'status','--porcelain'),'')

    def test_push_race_is_recovered_by_sync_without_force_push(self):
        self.commit(self.a,'local.md','local\n');actual_git=publication.git;pushes=[]
        def racing(repo,args,**kwargs):
            if args[0]=='push':
                pushes.append(args)
                if len(pushes)==1:self.advance_remote()
            return actual_git(repo,args,**kwargs)
        with patch.object(publication,'git',racing):
            result=publication.push_verified(self.a,self.branch,self.origins,self.protected,self.evidence)
        self.assertEqual(result['push_attempts'],2)
        self.assertEqual(self.evidence(),self.protected)
        self.assertEqual(self.command(self.remote,'rev-parse','refs/heads/research'),result['commit'])
        self.assertFalse(any('--force' in arg or arg.startswith('+') for args in pushes for arg in args))

    def test_non_race_push_failure_is_not_retried_or_misreported(self):
        actual_git=publication.git;pushes=[]
        def denied(repo,args,**kwargs):
            if args[0]=='push':
                pushes.append(args)
                return subprocess.CompletedProcess(['git',*args],128,'','permission denied')
            return actual_git(repo,args,**kwargs)
        with patch.object(publication,'git',denied),patch.object(publication,'synchronize') as sync:
            with self.assertRaisesRegex(publication.PublicationBlocked,'permission denied'):
                publication.push_verified(self.a,self.branch,self.origins,self.protected,self.evidence)
            sync.assert_not_called()
        self.assertEqual(len(pushes),1)

    def test_repeated_concurrent_writes_stop_at_three_push_attempts(self):
        self.commit(self.a,'local.md','local\n');actual_git=publication.git;pushes=[]
        def racing(repo,args,**kwargs):
            if args[0]=='push':
                pushes.append(args);self.advance_remote(len(pushes))
            return actual_git(repo,args,**kwargs)
        with patch.object(publication,'git',racing):
            with self.assertRaisesRegex(publication.PublicationBlocked,'3 attempt'):
                publication.push_verified(self.a,self.branch,self.origins,self.protected,self.evidence)
        self.assertEqual(len(pushes),3)
        self.assertEqual(self.evidence(),self.protected)

    def test_remote_append_after_successful_push_still_confirms_saved_commit(self):
        self.commit(self.a,'local.md','local\n');actual_git=publication.git
        def following(repo,args,**kwargs):
            result=actual_git(repo,args,**kwargs)
            if args[0]=='push' and result.returncode==0:
                self.command(self.b,'fetch','origin',self.branch)
                self.command(self.b,'merge','--ff-only','FETCH_HEAD')
                self.advance_remote()
            return result
        with patch.object(publication,'git',following):
            result=publication.push_verified(self.a,self.branch,self.origins,self.protected,self.evidence)
        self.assertNotEqual(result['commit'],result['observed_remote_commit'])
        self.command(self.a,'merge-base','--is-ancestor',result['commit'],result['observed_remote_commit'])

    def test_new_compiler_inputs_after_race_require_reverification(self):
        self.commit(self.a,'local.md','local\n');actual_git=publication.git
        def racing(repo,args,**kwargs):
            if args[0]=='push':self.advance_remote(name='Extra.lean')
            return actual_git(repo,args,**kwargs)
        with patch.object(publication,'git',racing):
            with self.assertRaisesRegex(publication.PublicationBlocked,'rerun Lean verification'):
                publication.push_verified(self.a,self.branch,self.origins,self.protected,self.evidence)

    def test_wrong_repository_and_staged_changes_are_not_merged(self):
        with self.assertRaisesRegex(publication.PublicationBlocked,'authorized repository'):
            publication.synchronize(self.a,self.branch,{'different-repository'},self.protected)
        self.advance_remote();(self.a/'private.txt').write_text('unstaged task data')
        self.command(self.a,'add','private.txt')
        with self.assertRaisesRegex(publication.PublicationBlocked,'staged changes'):
            publication.synchronize(self.a,self.branch,self.origins,self.protected)
        self.assertIn('private.txt',self.command(self.a,'diff','--cached','--name-only'))


if __name__=='__main__':unittest.main()
