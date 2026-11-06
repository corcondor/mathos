#!/usr/bin/env python3
"""Reduce available artifacts, including failed/partial shards, to branch reports."""
import argparse
import json
import os
from pathlib import Path
import shutil

from v18_arithmetic import pairs
from v18_compute import ROOT, NOTES, sha, write


def stage_value(curve, name):
    stage = curve.get('sage', {}).get('stages', {}).get(name, {})
    return stage.get('value') if stage.get('status') == 'ok' else None


def render(inputs, out, run_key, a_max):
    out.mkdir(parents=True, exist_ok=True)
    run = out/'v18_actions'/run_key
    if run.exists():
        raise ValueError('Refusing to overwrite an existing run certificate directory')
    run.mkdir(parents=True)
    # Preserve artifacts verbatim. Only .json certificates enter git; full logs
    # remain downloadable Actions artifacts. Names include artifact subdirectory.
    for file in inputs.rglob('*.json'):
        target = run/file.relative_to(inputs)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(file, target)
    shards = [json.loads(p.read_text()) for p in inputs.rglob('ranks-*.json')]
    expected = set(pairs(a_max))
    curves = {}
    for shard in shards:
        if shard['a_max'] != a_max:
            raise ValueError('Mixed a limits in artifacts')
        for c in shard['curves']:
            key = c['a'], c['b']
            if key not in expected or key in curves:
                raise ValueError('Unexpected or duplicate coefficient pair')
            curves[key] = c
    missing = sorted(expected-set(curves))
    ordered = [curves[k] for k in sorted(curves)]
    levels = []
    for c in ordered:
        rank = stage_value(c, 'rank')
        conductor = stage_value(c, 'conductor')
        mw = stage_value(c, 'mordell_weil')
        if conductor is not None and ((rank is not None and rank > 0)
                                     or (mw and len(mw['free_basis_minimal']) > 0)):
            levels.append({"a": c['a'], "b": c['b'], "conductor": conductor,
                           "rank": rank, "lmfdb_level": conductor,
                           "search_url": f'https://www.lmfdb.org/EllipticCurve/Q/?conductor={conductor}',
                           "newform_match_performed": False})
    prefix = f'v18_ranks_a{a_max}'
    complete_mw = sum(c['sage']['status'] == 'complete' for c in ordered)
    singular = sum(c['sage']['status'] == 'singular' for c in ordered)
    rank_report = {"run": run_key, "a_max": a_max, "expected_pair_count": len(expected),
                   "missing_pairs": missing, "curves": ordered,
                   "residual_enumeration_complete": not missing and all(c['residual']['complete'] for c in ordered),
                   "cas_complete": not missing and complete_mw+singular == len(expected),
                   "certainty": "proof=True rank and proven MW basis required; timeouts remain unknown",
                   "source_provenance": [s['provenance'] for s in shards]}
    write(out/(prefix+'.json'), rank_report)
    write(out/'v18_modular_levels.json', {"run": run_key, "positive_rank_curves": levels,
          "levels": sorted({x['conductor'] for x in levels}), "newform_matching": "not performed"})
    md = [f'# v18: a ≤ {a_max} の残差曲線 — GitHub Actions', '', f'実行: `{run_key}`。', '',
          f'許容係数対 {len(expected)}、記録 {len(ordered)}、未着 {len(missing)}、'
          f'CAS全段階完了 {complete_mw}、特異曲線 {singular}。', '',
          '係数条件: a≥1, b|486, gcd(a,b)=1, 27a<31b。', '',
          '整数点は元の整数係数モデルで、ρ>0、ρ≡a² (mod b)、'
          '1377ρ<216a²+760b² の全ρを整数平方根で検査し、両符号を収録する。'
          'この残差区間の完全性はMordell–Weil計算に依存しない。区間外の整数点や元の方程式の全解は主張しない。', '',
          '最小モデル・同型・conductor・証明付きrank・自由部分の基底・ねじれ生成元はJSON参照。'
          '時間切れや未計算のrankは `?` と表示する。特異な (1,3) は楕円曲線ソルバに渡さない。', '',
          '|a|b|conductor|rank|MW基底の認証|残差整数点数|CAS状態|',
          '|--:|--:|--:|--:|:--|--:|:--|']
    for c in ordered:
        rank, cond, mw = stage_value(c,'rank'), stage_value(c,'conductor'), stage_value(c,'mordell_weil')
        md.append(f'|{c["a"]}|{c["b"]}|{cond if cond is not None else "?"}|'
                  f'{rank if rank is not None else "?"}|{mw["basis_proven"] if mw else "?"}|'
                  f'{len(c["residual"]["points"])}|{c["sage"]["status"]}|')
    if missing:
        md += ['', f'未着の係数対: `{missing}`。']
    md += ['', f'詳細: [{prefix}.json]({prefix}.json)。', '',
           '正rank曲線のconductorを `v18_modular_levels.json` にLMFDB用レベルとして保存。'
           'LMFDB照会・newform照合は未実施。新しいLean検証ではない。', '']
    (out/(prefix+'.md')).write_text('\n'.join(md))

    fixed_files = list(inputs.rglob('fixed-j.json'))
    if len(fixed_files) > 1:
        raise ValueError('Duplicate fixed-J reports')
    if fixed_files:
        fixed = json.loads(fixed_files[0].read_text())
        write(out/'v18_fixed_J_search.json', fixed)
        text = ['# v18: 固定Jの有限探索', '', f'実行 `{run_key}`、状態 `{fixed["status"]}`。', '',
                f'n=104 から **{fixed["n_scanned_through"]:,}** までを検査。', '',
                '各nで Q|r³ と同値な強制約数F|rを使い、3n<r<10n/3内の全候補を生成。'
                'v17のt²≥9n、v18の(96(t+3))¹¹>n⁷、canonical J、'
                'δ≥13とgcd(δ,J)の制約で絞り、残った枝は元の二項係数等式をLucas合同式で検査する。', '',
                '負の二次式／n²+2の過剰な平方素因数が**実在すると確認した場合だけ**、'
                'v18の条件付きδ⁴高さと分岐制約を適用する。', '',
                '|枝|要求J上限|高さ全域を検査済みのJ|', '|:--|--:|:--|']
        for name, label in [('small','k=r'),('complement','k=A-r')]:
            full = [x['J'] for x in fixed['coverage'][name] if x['height_fully_covered']]
            text.append(f'|{label}|{fixed["j_max"][name]}|{full or "なし"}|')
        text += ['', '**上記以外のJは高さ全域の探索が未完了。** '
                 'small枝は n<min(16J⁶, ceil((2³⁵²J³³)^(1/14)))、'
                 '補分岐は n<ceil((2³⁵²J³³)^(1/3))を用いる。', '',
                 f'集計: `{fixed["counts"]}`。合同式まで通過した未決候補: '
                 f'{len(fixed["survivors"])}。通過は解の証明ではない。', '',
                 '全Jごとの厳密な整数上限・候補・排除理由・法と剰余は '
                 '[JSON](v18_fixed_J_search.json) に収録。', '']
        (out/'v18_fixed_J_search.md').write_text('\n'.join(text))
    else:
        # Do not leave a previous successful report masquerading as this run.
        write(out/'v18_fixed_J_search.json', {"run": run_key, "status": "missing_artifact"})
        (out/'v18_fixed_J_search.md').write_text(f'# 固定J探索\n\n実行 `{run_key}`: 結果artifact未着。未検証。\n')
    audits = list(inputs.rglob('lcm-audit.json'))
    certificates = list(inputs.rglob('lcm-certificate.json'))
    lcm_status = 'missing_artifact'
    if len(audits) == len(certificates) == 1:
        audit = json.loads(audits[0].read_text())
        certificate = json.loads(certificates[0].read_text())
        if (audit['status'] != 'PASS' or len(certificate['records']) != 830
                or certificate['audit_sha256'] != sha(audits[0])):
            raise ValueError('LCM certificate/audit mismatch')
        lcm_status = 'PASS: 828 cubic + 2 seventh-power cases independently regenerated'
    (out/'v18_actions_lcm.md').write_text(
        f'# v18 短いLCMの再検証\n\n実行 `{run_key}`。\n\n{lcm_status}\n\n'
        f'証明書・独立監査・入力SHAは `v18_actions/{run_key}/` に保存。'
        '有限例外830件の検証であり、一般証明のLean化ではない。\n')
    files = [p for p in out.glob('v18_*.json') if p.name != 'v18_actions_latest.json']
    files += list(out.glob('v18_*.md'))
    files += list(run.rglob('*.json'))
    manifest = {"run": run_key, "source_commit": os.environ.get('GITHUB_SHA'),
                "run_url": (f'https://github.com/{os.environ.get("GITHUB_REPOSITORY")}/actions/runs/'
                            f'{os.environ.get("GITHUB_RUN_ID")}'),
                "cas_complete": rank_report['cas_complete'], "lcm_status": lcm_status,
                "files_sha256": {str(p.relative_to(out)): sha(p) for p in sorted(set(files))}}
    write(out/'v18_actions_latest.json', manifest)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--out', type=Path, default=NOTES)
    parser.add_argument('--run-key', required=True)
    parser.add_argument('--a-max', type=int, default=20)
    args = parser.parse_args()
    if not args.run_key.replace('-', '').isalnum():
        parser.error('run-key must contain only alphanumerics and hyphens')
    render(args.input, args.out, args.run_key, args.a_max)


if __name__ == '__main__':
    main()
