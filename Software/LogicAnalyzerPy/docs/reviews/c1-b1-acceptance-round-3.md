# C1-B1 independent acceptance — round 3

- Reviewer: `/root/c1_b1_acceptance`
- Reviewed commit: `476c075891e50e5525b3aa3acc3430415ff018d3`
- Reviewed tree: `36712636d4cfdb0a6859c2b9160cc532d8d9deeb`
- UTC timestamp: `2026-08-16T22:54:05Z`
- Verdict: **pass**

## Candidate and scope

`HEAD` and `git rev-parse <commit>^{tree}` match the exact commit/tree above. The tracked worktree was clean before this review record. The candidate changes only the round-2 acceptance record relative to its predecessor; package, workflow, lock, fixture, contract, C#, and firmware contents are unchanged. `git diff --check` for the candidate against its parent passed.

## Finding dispositions

### 1. Clean Python 3.12 hash-locked bootstrap

- Status: **resolved**.
- Round-2 independent evidence remains applicable because its reviewed project contents are unchanged: the fresh Python 3.12.13 environment contained the exact hash-locked package set, passed `pip check`, and its installed `direct_url.json` proved an editable installation of this source tree. It passed Ruff, mypy, non-hardware pytest, and module help.
- This is now additionally proven on both clean GitHub-hosted matrix runners by the successful workflow evidence below. The workflow uses the required hash-locked installation followed by `--no-build-isolation --no-deps -e .` before the validation commands.

### 2. Evidence-manifest schema source list minimum

- Status: **resolved**.
- `docs/evidence-manifest/schema.json` is unchanged from round 2 and retains `"minItems": 1` for `sources`, in addition to requiring source category and revision. Empty source-evidence lists cannot validate.

### 3. Actual Linux/macOS CI execution

- Status: **resolved**.
- Authoritative GitHub REST API evidence for workflow run [`31977526293`](https://api.github.com/repos/eparadis/pico2-logicanalyzer/actions/runs/31977526293): workflow name `Logic analyzer Python Cycle 1`; workflow path `.github/workflows/logic-analyzer-python-cycle1.yml`; event `push`; head SHA `476c075891e50e5525b3aa3acc3430415ff018d3`; head tree `36712636d4cfdb0a6859c2b9160cc532d8d9deeb`; status `completed`; conclusion `success`; run attempt 1.
- The run's authoritative jobs response is [`.../actions/runs/31977526293/jobs`](https://api.github.com/repos/eparadis/pico2-logicanalyzer/actions/runs/31977526293/jobs), with exactly two completed successful jobs:
  - [job `95239134146`](https://github.com/eparadis/pico2-logicanalyzer/actions/runs/31977526293/job/95239134146), `validate (macos-latest)`, head SHA exact match, status `completed`, conclusion `success`.
  - [job `95239134210`](https://github.com/eparadis/pico2-logicanalyzer/actions/runs/31977526293/job/95239134210), `validate (ubuntu-latest)`, head SHA exact match, status `completed`, conclusion `success`.
- In each job, checkout, Python 3.12 setup, the single canonical shell step beginning `python3.12 -m venv .venv`, and job completion all report success.

## Retained C1-B1 evidence

The unchanged C1-B1 package still has the required CLI/help scaffold, hash lock including PEP 517 requirements, source-derived identity and rising/falling 48-byte fixture/provenance records with explicit physical deferrals, capture boundary ADR, operator/electrical and serial/recovery contracts, replay/CSV and compatibility contracts, and the authorized Linux/macOS workflow. No Qt, pythonnet, Roslyn, serial/capture implementation, or later-cycle product code is introduced. Existing C# and firmware rollback/comparison paths remain tracked and unchanged.

## Commands and outcomes

| Command | Outcome |
| --- | --- |
| `git status --short` | pass — clean tracked worktree before this review file |
| `git log -1 --format='%H %T'` | pass — exact reviewed commit/tree |
| `git rev-parse 476c075891e50e5525b3aa3acc3430415ff018d3^{tree}` | pass — exact reviewed tree |
| `git diff --stat a41df4b... 476c075...` | pass — only round-2 acceptance record differs |
| `git diff --check 476c075...^ 476c075...` | pass |
| `curl -sS .../actions/runs/31977526293` | pass — exact push workflow run completed/success on candidate SHA/tree |
| `curl -sS .../actions/runs/31977526293/jobs` | pass — exactly macOS and Ubuntu jobs, both completed/success on candidate SHA |
| fresh-environment Ruff/mypy/pytest/module-help evidence from round 2 | retained pass; product inputs unchanged |

## New findings

None. The full C1-B1 non-hardware gate, including actual Linux and macOS CI, is proven for the identified candidate.
