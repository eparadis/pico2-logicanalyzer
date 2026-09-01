# C3-B4 decode CSV taxonomy implementation, round 3

- Identity and role: `c3-b4-public-implementor-1`; bounded B4 correction
  implementor
- Timestamp: `2026-09-01T11:03:04Z`
- Immutable round-2 failed evidence commit/tree:
  `c01015e8439020cf87c042f11906912b8cefa947` /
  `6d8329f99a093e3014c093cbbff3761206e49c52`
- Governing contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`
- Accepted B3 checkpoint: `233b3b0667add740cee96ce3c9ee266c8a639067`

## C3B4-V003 correction

The decode subparser now retains `--sample-rate`, `--trigger-channel`, and
`--edge` as strings until the selected inert input mode is known. Decode CSV
mode converts and validates all three fields in the input validator, before
reading capture bytes, parsing decoder mappings/options, or delegating to the
worker. Malformed integers and an edge outside `rising`/`falling` therefore use
the settled input taxonomy: empty stdout, bounded stderr, exit 5.

Decode replay mode first performs the same narrow syntactic checks. A malformed
CSV-metadata token used with replay remains a usage/configuration error with
exit 2; a syntactically valid CSV-metadata option remains forbidden with replay
as input validation/exit 5. Other commands retain their existing argparse
integer/choice conversion and exit-2 behavior. The decode help metavariables
remain `HZ`, `PHYSICAL_CHANNEL`, and `{rising,falling}`.

Resolved V001 immutable exact public values, V002 caller tightening, and V004
aggregate 8,192-byte diagnostics are unchanged and remain covered by both
immutable verifier rounds.

## Changed paths and hashes

- `src/pico_logic_analyzer/cli/main.py` —
  `c3acce4965faeff55c6177dfdfff840d7a2b9c65a6ae4b05b45f26974f1d3ddc`
- `tests/implementation/test_c3_b4_public.py` —
  `34ff5abb41ff9040ed8fec72b2c4966b775aeaf0d607dac3fb7474718cb7f303`
- `docs/reviews/c3-b4-implementation-round-3.md` — this handoff record

Round-1 and round-2 verifier tests/reviews were read but not edited. No public
model, private host, decoder resource/semantics, fixture, limit, contract,
manifest, evidence, dependency, lock, workflow, hardware, firmware, web, or
serial path changed.

## Commands and exact results

- Focused new regression before correction:
  `.venv/bin/python -m pytest -q tests/implementation/test_c3_b4_public.py
  -k 'parser_invalid_decode_csv'`: `3 failed, 23 deselected in 0.70s`; all
  three CSV cases returned the old argparse exit 2.
- The same focused selection after correction: `3 passed, 23 deselected in
  1.04s`, including the equivalent replay exit-2 assertions.
- Immutable round-2 verifier:
  `.venv/bin/python -m pytest -q
  tests/verification/test_c3_b4_public_round2.py`: `13 passed in 1.76s`.
- Implementation public tests, both immutable B4 verifier rounds, existing CLI
  tests, and workflow regression: `57 passed in 7.72s`.
- Installed editable `pico-la decode --help` from `/private/tmp`, using the
  absolute environment entry point: exit 0 with the exact retained grammar and
  metavariables. An initial relative `.venv/bin/pico-la` wrapper invocation
  from `/private/tmp` returned 127 because that relative path does not exist;
  no product code ran, and the corrected absolute invocation passed.
- Focused Ruff over the two changed implementation/test files: pass.
- `mypy src`: `Success: no issues found in 31 source files`.
- Strict external consumer: `Success: no issues found in 1 source file`.
- `git diff --check`: pass.

No required test skipped. No external authority, hosted CI, prohibited runtime,
or external side effect was used.

## Verdict and boundary

The remaining C3B4-V003 implementation defect is corrected with no known open
product finding. Fresh independent verification, immutable candidate
integration, and orchestrator-owned accumulated/hosted gates remain required;
this identity does not accept its own work.

The B1 legal limitation remains unchanged: counsel or rights-holder
confirmation is still required before any conveyance, and this correction
builds, uploads, conveys, and publishes nothing.

Verdict: `candidate-not-accepted`. `APPROVAL_NEEDED`: none. The worktree is
intentionally unstaged and uncommitted.
