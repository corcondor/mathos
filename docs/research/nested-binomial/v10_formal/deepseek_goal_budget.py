"""Shared reported-token and wall-clock budget for a DeepSeek goal and workers."""
from contextlib import contextmanager
import fcntl
import json
import math
import os
from pathlib import Path
import time


class GoalBudgetExceeded(RuntimeError):
    pass


@contextmanager
def locked_budget(path):
    path = Path(path)
    with path.with_suffix(".lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        budget = json.loads(path.read_text())
        yield budget
        temporary = path.with_suffix(".tmp")
        temporary.write_text(json.dumps(budget, indent=2) + "\n")
        temporary.chmod(0o600)
        temporary.replace(path)


def before_call(settings):
    value = os.environ.get("DEEPSEEK_GOAL_BUDGET_FILE")
    if not value:
        return settings, None
    path = Path(value)
    with locked_budget(path) as budget:
        limit = budget["max_completion_tokens"]
        used = budget["used_completion_tokens"]
        deadline = budget["deadline"]
        if (type(limit) is not int or type(used) is not int or limit <= 0 or used < 0
                or not isinstance(deadline, (int, float)) or not math.isfinite(deadline)):
            raise ValueError("Invalid DeepSeek goal budget")
        remaining = limit - used
        seconds = int(deadline - time.time())
        if remaining < 1024 or seconds < 1:
            raise GoalBudgetExceeded("DeepSeek goal budget exhausted; checkpoint retained, goal not complete")
        adjusted = dict(settings)
        adjusted["max_tokens"] = min(settings["max_tokens"], remaining)
        adjusted["request_timeout_seconds"] = min(settings["request_timeout_seconds"], seconds)
    return adjusted, path


def record_usage(path, response, request_settings):
    if path is None:
        return
    usage = response.get("usage") or {}
    completion = usage.get("completion_tokens")
    if type(completion) is not int or completion < 0:
        # Do not treat an unknown usage report as free computation.
        completion = request_settings["max_tokens"]
    with locked_budget(path) as budget:
        budget["used_completion_tokens"] += completion
        budget["api_calls"] = budget.get("api_calls", 0) + 1
        budget["last_usage"] = {"completion_tokens": completion,
                                "reasoning_tokens": (usage.get("completion_tokens_details") or {}).get("reasoning_tokens"),
                                "model": response.get("model"), "time": time.time()}
