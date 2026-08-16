# C1-B1 independent acceptance

- Acceptance agent: `/root/c1_b1_acceptance`
- Review time: 2026-08-16
- Verdict: **changes_required**

## Scope and separation

I independently reviewed the uncommitted C1-B1 scaffold integrated from
`/root/c1_b1_implementation`, verifier-owned protocol fixtures/provenance, and
the workflow/progress integration.  I did not edit product behavior, fixtures,
contracts, lock files, CI, progress state, firmware, or C#.

The uncommitted scope is limited to the authorized new
`Software/LogicAnalyzerPy/` scaffold and
`.github/workflows/logic-analyzer-python-cycle1.yml`.  No tracked C# or
firmware change is present.  The scaffold contains no production serial,
capture, Qt, pythonnet, Roslyn, decoder, TCP, or later-cycle implementation;
the declared operational CLI commands intentionally stop at their owning later
batch.

## Findings and disposition

### 1. Clean Python 3.12 hash-locked bootstrap is not independently proven

- Status: **open — changes required before checkpoint acceptance**.
- Evidence: the configured bootstrap is correct in form: the lock has hashes
  for runtime/dev and PEP 517 requirements, `pyproject.toml` pins setuptools
  and wheel in `build-system`, and README plus the Linux/macOS workflow use
  `pip install --require-hashes -r requirements-dev.lock` followed by
  `pip install --no-build-isolation --no-deps -e .`.
- Independent attempt: a newly created isolated Python 3.12.13 environment at
  `/private/tmp/c1-b1-acceptance.RP4ZVW` could not install the hash lock because
  this acceptance task prohibits network access and no local wheel cache was
  available.  Pip failed resolving `iniconfig==2.3.0`; the subsequent editable
  install correctly failed because `setuptools.build_meta` was not installed.
- A pre-existing project `.venv` is Python 3.12.13 and successfully ran the
  locked install and no-build-isolation editable install, but that is not clean
  bootstrap evidence.  It cannot substitute for the required clean run.
- Required disposition: run the canonical bootstrap successfully in a fresh
  Python 3.12 environment with approved dependency access, retain its output in
  the checkpoint evidence, then rerun this acceptance gate.

### 2. Linux/macOS CI execution is not proven

- Status: **open — changes required before checkpoint acceptance**.
- Evidence: static review confirms one matrix covers `ubuntu-latest` and
  `macos-latest`, selects Python 3.12, and repeats the canonical install,
  Ruff, mypy, pytest, and module-help commands verbatim.
- No GitHub Actions run was available or triggered by this acceptance task;
  actual execution on both runners therefore cannot honestly be claimed.
- Required disposition: commit/push through the authorized workflow and retain
  successful Linux and macOS run evidence before marking C1-B1 complete.

### 3. Evidence-manifest schema permits an empty source-evidence list

- Status: **open — changes required**.
- Evidence: `docs/evidence-manifest/schema.json` requires the `sources` key
  but does not require any items.  This permits a checkpoint manifest with
  `"sources": []`, contrary to the orchestration contract that each manifest
  contains fixture/evidence source category and source revision.
- Required disposition: make the schema enforce at least one source entry (and
  validate any resulting fixture/schema test independently) without weakening
  the source-category/revision contract.

## Accepted evidence and dispositions

- **CLI/help and declared interface:** pass locally.  Both module and installed
  entry-point help list all settled commands, required capture options, and
  `{rising,falling}`.  The CLI contract documents the settled syntax, stdout /
  stderr routing, and exit-code mapping; implementation is correctly deferred.
- **Static and test gate:** pass locally in the existing Python 3.12.13 venv:
  Ruff reported `All checks passed!`; mypy reported `Success: no issues found
  in 4 source files`; pytest collected two non-hardware tests and passed both.
- **Lock/install contract:** form is accepted, subject to Finding 1.  The lock
  pins/hashes setuptools and wheel as PEP 517 build requirements, and editable
  installation disables both isolation and dependency resolution.
- **Workflow parity:** workflow content is accepted, subject to Finding 2.  It
  has explicit Linux/macOS Python 3.12 matrix jobs and uses the canonical
  bootstrap/validation sequence.
- **Protocol fixtures/provenance:** accepted.  The identity vector is exactly
  `55 aa 00 aa 55`; rising and falling vectors document a 48-byte capture
  struct, command-plus-payload length 49, framed length 55, offsets 3/31/47
  zero padding, and independent `aa`/`55` escape examples.  Source hashes in
  the provenance file exactly match the current named firmware and C# sources.
  The files explicitly label all deployed-wire/layout/padding/polarity facts as
  source-derived and defer physical C#/board confirmation to C1-B3/C1-B4.
- **Capture/data boundary:** accepted.  ADR 0001 explicitly covers D0, D7,
  ascending D0-D7 request order, raw bit mapping, last pre-trigger instant
  `-1/sample_rate_hz`, first post-trigger time zero, and the sole trigger flag.
  Compatibility and replay-security notes preserve the settled CSV and bounded
  provisional-NPZ contracts while deferring their implementation to C1-B4.
- **Serial/electrical/recovery documentation:** accepted for C1-B1.  The
  protocol note specifies framing, byte-oriented text/binary receive ownership,
  five LF-terminated identity fields, 115200/8N1/no-flow-control/DTR/RTS,
  bounded recovery, and the internal one-byte `0xff` sequence.  The operator
  template blocks unknown electrical details and prohibits 5 V on bare Pico
  GPIO.  Physical confirmation is explicitly deferred, not implied.
- **C#/firmware preservation:** accepted.  No tracked change under
  `Firmware/` or `Software/LogicAnalyzer/` was found; the compatibility note
  retains both as rollback/comparison paths.

## Commands and outcomes

Run from `Software/LogicAnalyzerPy` unless stated otherwise:

| Command | Outcome |
| --- | --- |
| `.venv/bin/python --version` | pass — Python 3.12.13 |
| `.venv/bin/python -m pip install --require-hashes -r requirements-dev.lock` | pass in pre-existing venv; all pinned requirements already satisfied |
| `.venv/bin/python -m pip install --no-build-isolation --no-deps -e .` | pass |
| `.venv/bin/python -m ruff check .` | pass |
| `.venv/bin/python -m mypy src` | pass |
| `.venv/bin/python -m pytest -m "not hardware"` | pass — 2 passed |
| `.venv/bin/python -m pico_logic_analyzer --help` | pass |
| `.venv/bin/pico-la --help` | pass |
| fresh-venc `pip install --require-hashes -r requirements-dev.lock` | not pass — offline DNS/network restriction; no cached distributions |
| fresh-venc `pip install --no-build-isolation --no-deps -e .` | not pass, expected after prior failed lock install (`setuptools.build_meta` unavailable) |
| `rg` scan for serial/Qt/pythonnet/Roslyn/TCP imports in scaffold source/dependency files | pass — no matches |
| `git diff --check` from repository root | pass — no whitespace errors |

`fresh-venc` above means the isolated temporary Python 3.12.13 virtual
environment described in Finding 1; it is not a product artifact.

## Files inspected

- `ORCHESTRATION.md`; `BATCH_EXECUTION.md`; Cycle 1/C1-B1 portions of
  `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md`.
- All three `docs/rewrite-reviews/final-round-3/` records (all pass for commit
  `2f128632c9718a32b8b01f184ad0c80632ce7853`).
- All current uncommitted C1-B1 project and workflow files, including package
  metadata, lock/input, CLI/tests, all C1-B1 docs/contracts/schema, and all
  three protocol fixture JSON files.
- `Firmware/LogicAnalyzer_V2/LogicAnalyzer_Structs.h`,
  `Firmware/LogicAnalyzer_V2/LogicAnalyzer.c`, and the named C# shared-driver
  sources in the provenance record.

## Gates not honestly proven

1. A successful clean, hash-locked Python 3.12 bootstrap: blocked by the
   task's no-network restriction and absent local wheel cache.
2. Actual GitHub Actions execution on both Linux and macOS: not available to
   this local acceptance task.
3. Any physical board/serial/capture evidence: intentionally not attempted;
   it is C1-B3/C1-B4/C1-B5 work and requires completed operator safety inputs.
