#!/usr/bin/env python3
"""Opt-in, budget-capped Codespaces supervisor for an existing DeepSeek goal.

This does not wake a stopped Codespace. It never creates an API credential or
claims a theorem was proved. Each child uses the existing state.json and the
repository's guarded Lean verification/publication runner.
"""
from __future__ import annotations

import datetime as dt
import fcntl
import json
import os
from pathlib import Path
import subprocess
import sys
import time

REPO = Path(__file__).resolve().parents[1]
RUNTIME = REPO / ".mathos-codespaces"
RUN = RUNTIME / "goal"
ENABLED = RUNTIME / "autopilot.enabled"
LEDGER = RUNTIME / "autopilot-ledger.json"
LOCK = RUNTIME / "autopilot.lock"

# These defaults deliberately cap shared-API usage; no unbounded paid loop.
DAY_TOKEN_CAP = 350_000
DAY_CALL_CAP = 12
CYCLE_TOKEN_CAP = 250_000
CYCLE_CALL_CAP = 8
CYCLE_ACTION_CAP = 12
CYCLE_HOURS = 2
RETRY_SECONDS = 120

def read_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        return value if isinstance(value, dict) else {}
    except (OSError, ValueError):
        return {}

def save_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.chmod(tmp, 0o600)
    tmp.replace(path)

def utc_date() -> str:
    return dt.datetime.now(dt.timezone.utc).date().isoformat()

def read_budget() -> dict:
    b = read_json(RUN / "budget.json")
    return {
        "id": str(b.get("deadline", "")),
        "tokens": max(0, int(b.get("used_completion_tokens", 0))),
        "calls": max(0, int(b.get("api_calls", 0))),
    }

def account_progress() -> dict:
    """Count each budget checkpoint once, including after a supervisor crash."""
    now = utc_date()
    current = read_budget()
    ledger = read_json(LEDGER)
    if ledger.get("date") != now:
        # Existing manual-run checkpoints are not billed to this *new* opt-in
        # daily supervisor cap. A resumed automatic run is counted from its
        # latest observed checkpoint.
        ledger = {
            "date": now, "tokens": 0, "calls": 0,
            "budget_id": current["id"],
            "observed_tokens": current["tokens"],
            "observed_calls": current["calls"],
        }
    else:
        if current["id"] != ledger.get("budget_id"):
            delta_tokens, delta_calls = current["tokens"], current["calls"]
        else:
            delta_tokens = max(0, current["tokens"] - ledger.get("observed_tokens", 0))
            delta_calls = max(0, current["calls"] - ledger.get("observed_calls", 0))
        ledger["tokens"] += delta_tokens
        ledger["calls"] += delta_calls
        ledger["budget_id"] = current["id"]
        ledger["observed_tokens"] = current["tokens"]
        ledger["observed_calls"] = current["calls"]
    save_json(LEDGER, ledger)
    return ledger

def stop_state() -> str:
    return read_json(RUN / "state.json").get("status", "not_started")

def sync_safe() -> bool:
    """Reuse the existing proof-preserving publication synchronizer."""
    formals = REPO / "docs/research/nested-binomial/v10_formal"
    sys.path.insert(0, str(formals))
    try:
        from deepseek_goal import GoalAgent
        agent = GoalAgent(run_dir=RUN)
        observation = agent.sync_research()
        print("Autopilot sync:", observation.get("status", "checked"), flush=True)
        return True
    except Exception as error:
        # Preserve state and proofs; do not run stale inputs on a merge error.
        print("Autopilot halted: safe research sync failed:", str(error)[-1400:], flush=True)
        return False

def execute_cycle(tokens: int, calls: int) -> int:
    environment = os.environ.copy()
    environment["MATHOS_RESEARCH_MAX_ACTIONS"] = str(CYCLE_ACTION_CAP)
    environment["MATHOS_RESEARCH_MAX_HOURS"] = str(CYCLE_HOURS)
    environment["MATHOS_RESEARCH_MAX_COMPLETION_TOKENS"] = str(tokens)
    environment["MATHOS_RESEARCH_MAX_API_CALLS"] = str(calls)
    # Existing .devcontainer/research run manages workspace/run locks, Lean
    # pins, state recovery, and proof publication. Do not bypass those guards.
    with (RUNTIME / "autopilot-run.log").open("a", encoding="utf-8") as log:
        result = subprocess.run(
            ["bash", str(REPO / ".devcontainer/research"), "run"],
            cwd=REPO, env=environment, stdout=log, stderr=subprocess.STDOUT,
            check=False,
        )
    return result.returncode

def main() -> int:
    RUNTIME.mkdir(parents=True, exist_ok=True)
    with LOCK.open("a") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print("Autopilot already running; second copy exits.", flush=True)
            return 0
        if not os.environ.get("MISTRAL_API_KEY"):
            print("Existing Codespaces MISTRAL_API_KEY not available; stop without charge.", flush=True)
            return 1
        if not ENABLED.is_file():
            print("Autopilot not enabled; stop.", flush=True)
            return 0
        # Register the existing manual budget as baseline before any auto run.
        account_progress()
        print("Research autopilot started with bounded daily budgets.", flush=True)
        while ENABLED.is_file():
            ledger = account_progress()
            status = stop_state()
            if status in ("complete", "blocked") or (status == "paused" and (RUN / "PAUSE").is_file()):
                print("Autopilot stopped due to goal state:", status, flush=True)
                break
            if ledger["tokens"] >= DAY_TOKEN_CAP or ledger["calls"] >= DAY_CALL_CAP:
                print("Daily DeepSeek budget reached (UTC); waiting without API calls.", flush=True)
                time.sleep(RETRY_SECONDS)
                continue
            if not sync_safe():
                # A conflict needs review. Do not change immutable proofs.
                break
            tokens = min(CYCLE_TOKEN_CAP, DAY_TOKEN_CAP - ledger["tokens"])
            calls = min(CYCLE_CALL_CAP, DAY_CALL_CAP - ledger["calls"])
            if tokens < 1024 or calls < 1:
                time.sleep(RETRY_SECONDS)
                continue
            print("Resume bounded DeepSeek cycle:", "tokens", tokens, "calls", calls, flush=True)
            code = execute_cycle(tokens, calls)
            ledger = account_progress()
            print("Cycle finished:", code, "status", stop_state(),
                  "day_tokens", ledger["tokens"], "day_calls", ledger["calls"], flush=True)
            if code:
                print("Run exited nonzero; stopping rather than retrying indefinitely.", flush=True)
                break
            time.sleep(5)
        print("Research autopilot exited; saved goal state remains intact.", flush=True)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
