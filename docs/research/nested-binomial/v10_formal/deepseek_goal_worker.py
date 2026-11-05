#!/usr/bin/env python3
"""Compile one fixed proof obligation at a time, retaining accepted prefixes.

All proof bodies, including repairs, come from DeepSeek. This worker only
assembles immutable declarations and sends real Lean diagnostics back.
"""

import argparse
import datetime
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

from deepseek_proof_loop import JOBS, MODEL, MATHLIB_COMMIT, ROOT, api, digest, render, retrieve_library_context, load_method_context, load_api_settings, completion_text


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("job", help="Built-in job name, or a label used with --job-config")
    parser.add_argument("--job-config", type=Path)
    parser.add_argument("--run-dir", required=True, type=Path)
    parser.add_argument("--methods-dir", type=Path, default=ROOT)
    parser.add_argument("--attempts", type=int)
    parser.add_argument("--library-reference", action="append", default=[], type=Path)
    parser.add_argument("--seed-proofs", type=Path)
    parser.add_argument("--extra-context", action="append", default=[], type=Path)
    args = parser.parse_args()
    settings = load_api_settings()
    if args.attempts is None:
        args.attempts = settings["max_attempts"]
    if args.attempts < 1:
        parser.error("--attempts must be positive")
    local_dependencies = []
    if args.job_config:
        config = json.loads(args.job_config.read_text())
        module = config["module"]
        if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", module):
            raise SystemExit("Invalid module name")
        definitions = config.get("definitions", "")
        if re.search(r"\b(sorry|admit|axiom|native_decide|unsafe|initialize|run_cmd|elab|macro|syntax)\b|#|\bIO\.", definitions):
            raise SystemExit("Unsupported code in fixed definitions")
        imports = config["imports"] + "\n" + definitions + "\n"
        goals = config["goals"]
        for name in config.get("local_dependencies", []):
            if not isinstance(name, str) or Path(name).name != name or not name.endswith(".lean"):
                raise SystemExit("Local dependencies must be Lean filenames in v10_formal")
            local_dependencies.append(ROOT / name)
    else:
        if args.job not in JOBS:
            parser.error("Unknown built-in job; use --job-config for new fixed goals")
        module, imports, goals = JOBS[args.job]
    if args.job == "crt" and not args.job_config:
        goals = [goals[1], goals[0], goals[2]]
    if (ROOT / (module + ".lean")).exists():
        raise SystemExit("Verified output already exists; do not overwrite it")
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    version = subprocess.check_output(["lean", "--version"], text=True).strip()
    if commit != MATHLIB_COMMIT or not version.startswith("Lean (version 4.35.0,"):
        raise SystemExit("Pinned Lean/mathlib required")
    args.run_dir.mkdir(parents=True, exist_ok=False)
    paths = [ROOT / "ValuationRecovery.lean", ROOT / "NormalizedCancellation.lean"] if args.job == "square" else []
    paths.extend(local_dependencies)
    context = "\n\n".join(p.name + "\n" + p.read_text() for p in paths)
    context += "\n\n" + "\n\n".join(p.name + "\n" + p.read_text() for p in args.extra_context)
    library = "\n\n".join(str(p) + "\n" + p.read_text() for p in args.library_reference)
    methods = load_method_context(args.methods_dir)
    accepted = {}
    seeds = json.loads(args.seed_proofs.read_text()) if args.seed_proofs else {}
    records = []
    with tempfile.TemporaryDirectory(prefix="deepseek-stagewise-") as build:
        env = os.environ.copy()
        env["LEAN_PATH"] = build + os.pathsep + env.get("LEAN_PATH", "")
        for dependency in paths:
            command = ["lean", f"--root={ROOT}", "-o", str(Path(build) / (dependency.stem + ".olean")), str(dependency)]
            result = subprocess.run(command, env=env, capture_output=True, text=True, timeout=settings["lean_timeout_seconds"])
            if result.returncode:
                raise SystemExit(result.stdout + result.stderr)
        for index, (name, statement) in enumerate(goals):
            prefix = render(imports, goals[:index], accepted)
            prompt = """You alone author all Lean proof code and all repairs. The host never edits your proofs.
Use the referenced fixed-goal checking and evaluator-optimizer workflows, one obligation at a time.
Lean 4.35.0, pinned mathlib. Return JSON {"proof":"by\\n ..."} for ONLY the NEW goal.
Do not alter the goal, imports, accepted proofs, or assumptions. Earlier accepted goals are available.
No holes, extra declarations, custom axioms, native_decide, side effects or unsafe tactics.
Read actual mathlib API source below instead of inventing lemma names or argument order.
If a prior strategy fails, reconsider the mathematical inference, not only its syntax.
Prefer direct reuse of a matching quantified theorem over deriving facts from insufficient inequalities.
In particular, a bound e<t+d alone does not imply e=t. The available critical_exponent_dichotomy supplies the missing disjunction.
Do not index a list by arbitrary Nat with an unproved bounds proof: CRT already accepts lists of modulus values.
Output the proof only in the JSON field; do not claim execution.
""" + "\nNEW FIXED GOAL:\n" + statement + "\nACCEPTED PREFIX:\n" + prefix + "\nAVAILABLE CONTEXT:\n" + context + "\nACTUAL PUBLIC MATHLIB SOURCE:\n" + library + "\nPUBLIC WORKFLOW REFERENCES:\n" + methods
            messages = [{"role": "user", "content": prompt}]
            seen = set()
            for attempt in range(1, args.attempts + 1):
                print(f"{module}/{name}: generation {attempt}", flush=True)
                if attempt == 1 and name in seeds:
                    response = {"model": MODEL, "choices": [{"finish_reason": "stop", "message": {
                        "content": json.dumps({"proof": seeds[name]}, ensure_ascii=False)}}],
                        "seed_source": str(args.seed_proofs)}
                else:
                    response = api(messages)
                (args.run_dir / f"{index+1}-{attempt}.response.json").write_text(json.dumps(response, ensure_ascii=False, indent=2))
                reply_content = response["choices"][0]["message"].get("content")
                content = ""
                try:
                    if response["choices"][0]["finish_reason"] != "stop":
                        raise ValueError("Incomplete model output")
                    content = completion_text(response)
                    body = json.loads(content)["proof"]
                    all_bodies = {**accepted, name: body}
                    candidate = render(imports, goals[:index+1], all_bodies)
                    if digest(candidate) in seen:
                        raise ValueError("Identical failed proof repeated. Choose a different argument using the exact available theorem signatures.")
                    seen.add(digest(candidate))
                    source = args.run_dir / (module + ".lean")
                    source.write_text(candidate)
                    (args.run_dir / f"{index+1}-{attempt}.lean").write_text(candidate)
                    command = ["lean", f"--root={args.run_dir}", "-o", str(Path(build) / (module + ".olean")), str(source)]
                    result = subprocess.run(command, env=env, capture_output=True, text=True, timeout=settings["lean_timeout_seconds"])
                    output = result.stdout + result.stderr
                    (args.run_dir / f"{index+1}-{attempt}.compiler.txt").write_text(output)
                    passed = result.returncode == 0 and "sorryAx" not in output and "warning:" not in output
                    for axiom_list in re.findall(r"depends on axioms:\s*\[([^\]]*)\]", output):
                        if set(re.findall(r"[A-Za-z_][\w.]*", axiom_list)) - {"propext", "Classical.choice", "Quot.sound"}:
                            passed = False
                    record = {"theorem": name, "attempt": attempt, "exit_code": result.returncode,
                              "accepted": passed, "source_sha256": digest(candidate), "usage": response.get("usage"),
                              "request_settings": response.get("research_request_settings")}
                    records.append(record)
                    print(f"{module}/{name}: Lean exit={result.returncode}, accepted={passed}", flush=True)
                    if passed:
                        accepted[name] = body
                        (args.run_dir / "accepted_proofs.json").write_text(json.dumps(accepted, ensure_ascii=False, indent=2))
                        break
                    feedback = output[-16000:]
                    retrieved = retrieve_library_context(output)
                    if retrieved:
                        (args.run_dir / f"{index+1}-{attempt}.retrieved.txt").write_text(retrieved)
                        feedback += "\nRetrieved from the pinned public mathlib source:\n" + retrieved
                except (ValueError, KeyError, TypeError, subprocess.TimeoutExpired) as error:
                    feedback = str(error)
                    records.append({"theorem": name, "attempt": attempt, "validation_error": feedback})
                messages.extend([{"role": "assistant", "content": reply_content}, {"role": "user", "content":
                    "Actual Lean feedback. Repair this proof only; preserve every hypothesis. Return JSON with proof only.\n" + feedback}])
                if attempt % 2 == 0:
                    diagnosis = api([{"role": "user", "content":
                        "Independent mathematical evaluator. Diagnose the failed proof below. Identify any false logical inference, "
                        "sign mistake, wrong witness, or API mismatch. Suggest a genuinely different repair strategy when needed. "
                        "Return JSON with a feedback field, no Lean code. Do not change the fixed theorem.\nGOAL:\n" + statement +
                        "\nFAILED PROOF:\n" + content + "\nACTUAL FEEDBACK:\n" + feedback +
                        "\nAVAILABLE CONTEXT:\n" + context + "\nLIBRARY SOURCE:\n" + library}])
                    (args.run_dir / f"{index+1}-{attempt}.diagnosis.json").write_text(json.dumps(diagnosis, ensure_ascii=False, indent=2))
                    messages.append({"role": "user", "content": "Your separate mathematical evaluator found:\n" +
                                     completion_text(diagnosis)})
            else:
                (args.run_dir / "result.json").write_text(json.dumps({"status": "UNRESOLVED", "accepted": list(accepted), "records": records}, indent=2))
                raise SystemExit("Goal remains open; accepted prefixes retained")
        final_source = render(imports, goals, accepted)
        review = api([{"role": "user", "content":
            "Act as a separate statement reviewer. Return JSON {verdict:PASS or ISSUES, feedback:...}. "
            "Lean compiled the following fixed-goal module without holes or warnings. Check its mathematical scope, "
            "nonzero/positive assumptions, and whether its names overstate what is proved. Do not demand unrelated new claims. "
            "Do not report interface or type mismatches that Lean has already checked. Do not mark generic names as ISSUES. "
            "Here is the actual imported context, so check signatures against it:\n" + context +
            "\nVERIFIED MODULE:\n" + final_source}])
        (args.run_dir / "review.json").write_text(json.dumps(review, ensure_ascii=False, indent=2))
        verdict = json.loads(completion_text(review))
        report = {"status": "PASS" if verdict.get("verdict") == "PASS" else "REVIEW_ISSUES",
                  "model": MODEL, "lean_version": version, "mathlib_commit": commit,
                  "checked_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  "module": module, "source_sha256": digest(final_source), "theorems": list(accepted),
                  "records": records, "review": verdict,
                  "proof_author": "DeepSeek API, all bodies and repairs; no manual proof edits",
                  "whole_equation_solved": False}
        (args.run_dir / "result.json").write_text(json.dumps(report, ensure_ascii=False, indent=2))
        if report["status"] != "PASS":
            raise SystemExit("Reviewer found issues; verified source retained in run directory")
        (ROOT / (module + ".lean")).write_text(final_source)
        print(f"{module}: verified module saved", flush=True)


if __name__ == "__main__":
    main()
