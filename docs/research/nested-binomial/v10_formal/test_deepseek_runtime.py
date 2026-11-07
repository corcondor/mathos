"""Offline checks for the reasoning-enabled API adapter; no live credentials."""

import io
import json
import os
from pathlib import Path
import tempfile
import time
import unittest
from unittest.mock import patch
import urllib.error

import deepseek_proof_loop as runtime
from deepseek_goal_budget import GoalBudgetExceeded


class ReasoningRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.root_patch = patch.object(runtime, "ROOT", self.root)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)
        self.env_patch = patch.dict(os.environ, {"MISTRAL_API_KEY": "offline-test-key"})
        self.env_patch.start()
        self.addCleanup(self.env_patch.stop)
        self.write_settings(reasoning_effort="high", max_tokens=32768,
                            request_timeout_seconds=900, capacity_retries=2)

    def write_settings(self, **values):
        (self.root / "deepseek_settings.json").write_text(json.dumps(values))

    @staticmethod
    def response(content=None):
        if content is None:
            content = [{"type": "thinking", "thinking": "private model reasoning"},
                       {"type": "text", "text": '{"proof":"by simp"}'}]
        return io.BytesIO(json.dumps({"choices": [{"message": {"role": "assistant", "content": content},
                                                "finish_reason": "stop"}]}).encode())

    def test_high_settings_and_final_text_extraction(self):
        calls = []

        def fake(request, timeout):
            calls.append((json.loads(request.data), timeout))
            return self.response()

        with patch.object(runtime.urllib.request, "urlopen", fake):
            result = runtime.api([{"role": "user", "content": "proof request"}])
        self.assertEqual(calls[0][0]["reasoning_effort"], "high")
        self.assertEqual(calls[0][0]["max_tokens"], 32768)
        self.assertEqual(calls[0][1], 900)
        self.assertEqual(json.loads(runtime.completion_text(result)), {"proof": "by simp"})
        self.assertEqual(result["choices"][0]["message"]["content"][0]["type"], "thinking")

    def test_settings_are_reloaded_between_requests(self):
        calls = []

        def fake(request, timeout):
            calls.append(json.loads(request.data))
            return self.response()

        with patch.object(runtime.urllib.request, "urlopen", fake):
            runtime.api([])
            self.write_settings(reasoning_effort=None, max_tokens=512)
            runtime.api([])
        self.assertEqual(calls[0]["reasoning_effort"], "high")
        self.assertNotIn("reasoning_effort", calls[1])
        self.assertEqual(calls[1]["max_tokens"], 512)

    def test_max_research_profile_and_model_output_limit(self):
        self.write_settings(reasoning_effort="max", max_tokens=131072,
                            request_timeout_seconds=1800)
        calls = []
        def fake(request, timeout):
            calls.append((json.loads(request.data), timeout))
            return self.response()
        with patch.object(runtime.urllib.request, "urlopen", fake):
            result = runtime.api([])
        self.assertEqual(calls[0][0]["reasoning_effort"], "max")
        self.assertEqual(calls[0][0]["max_tokens"], 131072)
        self.assertEqual(calls[0][1], 1800)
        self.assertEqual(result["research_request_settings"]["reasoning_effort"], "max")
        self.write_settings(max_tokens=131073)
        with patch.object(runtime.urllib.request, "urlopen") as send:
            with self.assertRaises(ValueError):
                runtime.api([])
            send.assert_not_called()

    def test_chat_mode_changes_only_format_and_effort_for_this_request(self):
        calls = []
        def fake(request, timeout):
            calls.append(json.loads(request.data))
            return self.response()
        with patch.object(runtime.urllib.request, "urlopen", fake):
            runtime.api([], response_format=None, reasoning_effort=None)
            runtime.api([])
        self.assertNotIn("response_format", calls[0])
        self.assertNotIn("reasoning_effort", calls[0])
        self.assertEqual(calls[1]["response_format"], {"type": "json_object"})
        self.assertEqual(calls[1]["reasoning_effort"], "high")

    def test_goal_budget_is_shared_by_actual_api_adapter(self):
        budget = self.root / 'budget.json'
        budget.write_text(json.dumps({'max_completion_tokens': 5000, 'used_completion_tokens': 2000,
                                      'deadline': time.time()+60, 'api_calls': 0}))
        calls = []
        def fake(request, timeout):
            calls.append((json.loads(request.data), timeout))
            return io.BytesIO(json.dumps({'choices':[{'message':{'content':'{}'}}],
                                          'usage':{'completion_tokens':700}}).encode())
        with patch.dict(os.environ, {'DEEPSEEK_GOAL_BUDGET_FILE': str(budget)}), patch.object(runtime.urllib.request, 'urlopen', fake):
            runtime.api([])
        self.assertEqual(calls[0][0]['max_tokens'], 3000)
        self.assertLessEqual(calls[0][1], 60)
        self.assertEqual(json.loads(budget.read_text())['used_completion_tokens'], 2700)

    def test_capped_round_reserves_failed_attempt_and_counts_retry(self):
        self.write_settings(max_tokens=2000, capacity_retries=2)
        budget = self.root / 'budget.json'
        budget.write_text(json.dumps({'max_completion_tokens': 5000, 'used_completion_tokens': 0,
                                      'deadline': time.time() + 60, 'max_api_calls': 2, 'api_calls': 0}))
        gateway_error = urllib.error.HTTPError('https://api.mistral.ai', 503, 'gateway', {},
                                               io.BytesIO(b'offline-test-key'))
        response = io.BytesIO(b'{"usage":{"completion_tokens":700}}')
        with patch.dict(os.environ, {'DEEPSEEK_GOAL_BUDGET_FILE': str(budget)}), \
                patch.object(runtime.time, 'sleep'), \
                patch.object(runtime.urllib.request, 'urlopen', side_effect=[gateway_error, response]) as send:
            runtime.api([])
            with self.assertRaises(GoalBudgetExceeded):
                runtime.api([])
        self.assertEqual(send.call_count, 2)
        self.assertEqual(json.loads(budget.read_text())['used_completion_tokens'], 2700)
        request = send.call_args.args[0]
        self.assertEqual(request.get_header('Authorization'), 'Bearer offline-test-key')
        self.assertNotIn('Authorization', request.headers)

    def test_malformed_key_fails_without_exposing_it_or_sending(self):
        with patch.dict(os.environ, {'MISTRAL_API_KEY': 'offline-test-key\n'}), \
                patch.object(runtime.urllib.request, 'urlopen') as send:
            with self.assertRaisesRegex(RuntimeError, '^MISTRAL_API_KEY is missing or contains invalid characters$'):
                runtime.api([])
            send.assert_not_called()

    def test_explicit_capacity_failure_is_retried_without_downgrading(self):
        calls = []

        def fake(request, timeout):
            calls.append(json.loads(request.data))
            if len(calls) == 1:
                raise urllib.error.HTTPError(request.full_url, 429, "capacity", {},
                    io.BytesIO(b'{"type":"backend_out_of_capacity","code":"3505"}'))
            return self.response()

        with patch.object(runtime.urllib.request, "urlopen", fake), patch.object(runtime.time, "sleep") as sleep:
            result = runtime.api([])
        self.assertEqual(len(calls), 2)
        self.assertTrue(all(c["reasoning_effort"] == "high" for c in calls))
        self.assertEqual(result["research_capacity_retries_used"], 1)
        sleep.assert_called_once_with(5)

    def test_authentication_and_quota_failures_are_not_retried(self):
        for status, payload in [(401, b'{"message":"offline-test-key"}'),
                                (429, b'{"type":"rate_limited","code":"1300"}')]:
            with self.subTest(status=status):
                error = urllib.error.HTTPError("https://api.mistral.ai", status, "error", {}, io.BytesIO(payload))
                with patch.object(runtime.urllib.request, "urlopen", side_effect=error) as send, patch.object(runtime.time, "sleep") as sleep:
                    with self.assertRaises(RuntimeError) as raised:
                        runtime.api([])
                self.assertEqual(send.call_count, 1)
                sleep.assert_not_called()
                self.assertNotIn("offline-test-key", str(raised.exception))

    def test_transient_review_gateway_error_retries_without_model_downgrade(self):
        calls=[]
        def fake(request,timeout):
            calls.append(json.loads(request.data))
            if len(calls)==1:
                raise urllib.error.HTTPError(request.full_url,520,'gateway',{},io.BytesIO(b'error code: 520'))
            return self.response()
        with patch.object(runtime.urllib.request,'urlopen',fake),patch.object(runtime.time,'sleep'):
            result=runtime.api([])
        self.assertEqual(calls[0],calls[1])
        self.assertEqual(result['research_capacity_retries_used'],0)
        self.assertEqual(result['research_transient_retries_used'],1)
        self.assertTrue(result['research_retry_trace'][0]['failed_request_usage_unknown'])

    def test_gateway_retries_are_bounded_and_stop_at_the_shared_deadline(self):
        def failed(request,timeout):
            raise urllib.error.HTTPError(request.full_url,520,'gateway',{},io.BytesIO(b'gateway'))
        with patch.object(runtime.urllib.request,'urlopen',side_effect=failed) as send,patch.object(runtime.time,'sleep'):
            with self.assertRaises(RuntimeError):runtime.api([])
            self.assertEqual(send.call_count,3)
        path=self.root/'budget.json'
        path.write_text(json.dumps({'max_completion_tokens':5000,'used_completion_tokens':0,'deadline':time.time()+60}))
        def expired(_):
            data=json.loads(path.read_text());data['deadline']=time.time()-1;path.write_text(json.dumps(data))
        with patch.dict(os.environ,{'DEEPSEEK_GOAL_BUDGET_FILE':str(path)}),patch.object(runtime.urllib.request,'urlopen',side_effect=failed) as send,patch.object(runtime.time,'sleep',expired):
            with self.assertRaises(GoalBudgetExceeded):runtime.api([])
            self.assertEqual(send.call_count,1)

    def test_legacy_string_and_missing_final_text(self):
        self.assertEqual(runtime.completion_text({"choices": [{"message": {"content": "old output"}}]}), "old output")
        with self.assertRaises(ValueError):
            runtime.completion_text({"choices": [{"message": {"content": [{"type": "thinking", "thinking": "no final"}]}}]})

    def test_invalid_settings_fail_before_network_access(self):
        for settings in [{"reasoning_effort": "unverified-level"}, {"max_tokens": True},
                         {"request_timeout_seconds": 0}, {"endpoint": "unconfigured.example"}]:
            with self.subTest(settings=settings):
                self.write_settings(**settings)
                with patch.object(runtime.urllib.request, "urlopen") as send:
                    with self.assertRaises(ValueError):
                        runtime.api([])
                    send.assert_not_called()


if __name__ == "__main__":
    unittest.main()
