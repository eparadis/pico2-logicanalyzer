# C1-B1 independent acceptance — round 2

- Reviewer: `/root/c1_b1_acceptance`
- Reviewed commit: `a41df4b04831517813a0016a76587382a12c10e9`
- Reviewed tree: `9968d13a52282f4c0e948eb54431a3a1e4056e51`
- UTC timestamp: `2026-08-16T22:47:12Z`
- Verdict: **changes_required**

## Scope and candidate identity

`HEAD` resolves to the exact commit and tree above. The worktree was clean before this review record was created. The candidate adds only the authorized C1-B1 Python scaffold and the one authorized workflow; C# and firmware are unchanged. `git diff --check` for the candidate versus its parent passed.

## Prior-finding dispositions

### 1. Clean Python 3.12 hash-locked bootstrap

- **Status: resolved.**
- Evidence: I independently inspected the still-present fresh environment at `/private/tmp/pico-la-c1b1.QO32TF/venv`. It identifies as Python 3.12.13, contains the exact lock-pinned requirements (`iniconfig 2.3.0`, mypy 1.15.0, pytest 8.3.4, ruff 0.9.10, setuptools 75.8.0, wheel 0.45.1, and all recorded transitives), and `pip check` reports no broken requirements. Its installed `pico_logic_analyzer-0.1.0.dist-info/direct_url.json` says `{"dir_info":{"editable":true},"url":"file:///Users/ed/git/pico2-logicanalyzer/Software/LogicAnalyzerPy"}`. This independently confirms the successful fresh-environment result uses the reviewed source tree as an editable installation, rather than the existing project `.venv`.
- The bootstrap contract remains correct in the candidate: the hashed lock includes its PEP 517 build requirements, and README and both workflow matrix jobs use `--require-hashes`, then `--no-build-isolation --no-deps -e .`.
- Limitation recorded, not a finding: I did not rerun the network-capable lock-install command in a second brand-new environment because this task forbids network access. A separate offline fresh venv had no wheel cache and therefore cannot reproduce dependency acquisition with `--no-index`; that is expected and does not contradict the inspected successful fresh environment.

### 2. Actual Linux/macOS GitHub Actions execution

- **Status: open — changes required before checkpoint acceptance.**
- Static workflow review remains positive: it has explicit `ubuntu-latest` and `macos-latest` matrix jobs, Python 3.12, and the canonical bootstrap, Ruff, mypy, non-hardware pytest, and module-help commands.
- No actual GitHub Actions run evidence exists. Pushing is an orchestration authority gate awaiting user permission, so it was neither attempted nor inferred from local macOS evidence.
- Required disposition: after authorized push, retain successful runs for both matrix platforms and rerun acceptance against that evidence.

### 3. Evidence-manifest source list minimum

- **Status: resolved.**
- Evidence: `docs/evidence-manifest/schema.json` now specifies `"minItems": 1` for `sources`, while retaining required source `category` and `revision` fields and the approved source-category enum. A manifest with `"sources": []` is no longer schema-valid.

## Independent command evidence

| Command | Outcome |
| --- | --- |
| fresh venv `python --version` | pass — Python 3.12.13 |
| fresh venv `python -m pip check` | pass — no broken requirements |
| fresh venv `python -m pip list --format=freeze` | pass — installed locked versions match `requirements-dev.lock` and project is installed |
| fresh venv `python -m ruff check .` | pass |
| fresh venv `python -m mypy src` | pass — no issues in 4 source files |
| fresh venv `python -m pytest -m "not hardware"` | pass — 2 passed |
| fresh venv `python -m pico_logic_analyzer --help` | pass |
| candidate `git diff --check <parent> <candidate>` | pass |
| offline separate fresh venv `pip install --no-index --require-hashes -r requirements-dev.lock` | unavailable by design — no local wheel cache, with no network access permitted |

## Other scope checks

The candidate continues to satisfy the previously accepted C1-B1 checks: source-derived identity and rising/falling 48-byte request fixtures have exact lengths/bytes, source hashes, and explicit C1-B3/C1-B4 physical deferrals; the ADR covers D0/D7 and the pre-trigger/time-zero boundary; the operator, serial, recovery, CSV/replay, CLI, and compatibility contracts are present; and there is no Qt, pythonnet, Roslyn, serial transport/capture implementation, or later-cycle product implementation. The existing C# application and firmware remain intact.

## New findings

None. The sole remaining acceptance blocker is actual successful execution of the required Linux and macOS GitHub Actions matrix.
