# C3-B4 public library and installed CLI implementation, round 2

- Identity and role: `c3-b4-public-implementor-1`; bounded B4 correction
  implementor
- Timestamp: `2026-09-01T10:50:53Z`
- Immutable failed verification evidence commit/tree:
  `fed87a058e88329790d460977df9ee8a04f83e44` /
  `8e7e829f6ea0bacf13d09cb0429123b8ffdb4406`
- Governing contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`
- Accepted B3 checkpoint: `233b3b0667add740cee96ce3c9ee266c8a639067`

## Corrected findings

1. `C3B4-V001` is corrected. `AnnotationRecord.value`, `BinaryRecord.value`,
   and `MetadataRecord.value` are now closed, validated immutable mappings
   whose keys and scalar/tuple values match the version-1 schema. The three
   unlisted payload dataclasses no longer exist or appear in a public type
   hint. Mapping proxies prevent caller mutation; binary text is canonical
   padded base64. The normative public dataclass set and all 12 B1 literal
   object/UTF-8 vectors remain exact.
2. `C3B4-V002` is corrected. A selected SPI word-size ceiling is checked
   against the fully materialized option before public host delegation and
   again in private-host preflight before identity verification or process
   launch. A diagnostic ceiling too small to encode the closed stable failure
   messages is rejected before delegation; accepted tighter ceilings bound the
   resulting `DecodeError` message. No hard ceiling or containment control was
   weakened.
3. `C3B4-V003` is corrected. Decode-only CSV physical-channel parsing now
   classifies empty, malformed, duplicate, non-distinct, out-of-range, and
   header-count-mismatched metadata as input validation/exit 5 before decoder
   mapping or worker launch. Replay and decoder mapping/option failures retain
   their existing exit-2 taxonomy.
4. `C3B4-V004` is corrected. One 8,192-byte budget now covers the aggregate
   stderr emitted during a CLI invocation. The bounded parser class accounts
   for separate argparse usage and error writes, and every handled usage,
   connection, capture/input, output, decoder, web-extra, cancellation, and
   not-implemented diagnostic routes through the same writer. Failure stdout
   remains empty and exits remain 2/3/4/5/6/7 as applicable.

## Changed paths

- `src/pico_logic_analyzer/decode/__init__.py`
- `src/pico_logic_analyzer/_decode/host.py`
- `src/pico_logic_analyzer/cli/main.py`
- `tests/implementation/test_c3_b4_public.py`
- `docs/reviews/c3-b4-implementation-round-2.md`

The immutable round-1 verifier test and review were read but not edited. No
B1/B2/B3 fixture, expectation, evidence, manifest, decoder snapshot, semantic
code, limit value, contract, workflow, dependency, or lock changed.

Changed-file SHA-256 values before this record's final self-hash are:

- public module:
  `d5cd8b843bf2bd847dc42a7fa550d5756615177d77e80912472d088b9e6519db`;
- private host:
  `b81d3c1b4ded37bc665cb074d81de0620b6030435aae4b1ce0122a69c56315b6`;
- CLI:
  `adc19545b0b02203aa73ecccc8600c3ee97259b5ea3f116fae2e2ae33d88d51e`;
  and
- focused implementation test:
  `c6b88a82c0466070d8b7628caba6337eb5855747ab6f07fe8861cf2f4d35468d`.

## Commands and exact results

- Focused new regressions before correction:
  `.venv/bin/python -m pytest -q tests/implementation/test_c3_b4_public.py
  -k 'record_values or tightened_spi or invalid_csv or all_cli'`:
  `5 failed, 3 passed, 14 deselected`; failures reproduced V001, both V002
  cases, V003's empty/malformed cases, and V004.
- The same focused regression selection after correction:
  `8 passed, 14 deselected in 1.10s`.
- Immutable failed-candidate verifier module after correction:
  `.venv/bin/python -m pytest -q
  tests/verification/test_c3_b4_public_round1.py`: `10 passed in 1.47s`.
- Final public implementation plus immutable verifier module after the added
  exact diagnostic-boundary and mapping-immutability checks: `33 passed in
  5.03s`.
- B4 implementation, immutable verifier, existing CLI, accepted private host,
  and workflow regression modules: `273 passed in 29.54s`.
- All eight accepted B3 implementation/verification conformance modules:
  `421 passed in 60.13s`.
- Focused Ruff over all changed production/test files: pass.
- `mypy src`: `Success: no issues found in 31 source files`.
- Strict external consumer: `Success: no issues found in 1 source file`.
- `git diff --check`: pass.

No required test skipped. Tests exercised only inert replay/CSV captures and
the already accepted isolated host. No web, serial, hardware, firmware,
external decoder runtime, publication, or hosted-CI action was taken.

## Remaining risk and verdict

The implementation correction has no known open product finding. Independent
round-2 verification, immutable candidate integration, accumulated gates, and
orchestrator-owned hosted macOS proof remain required; this identity does not
accept its own work.

The B1 rights-holder/counsel limitation remains unchanged: the shim's ownership
and licensing, the historical MIT label, and combined-work treatment require
counsel/rights-holder confirmation before conveyance. This correction performs
and authorizes no wheel/sdist build, upload, conveyance, or publication.

Verdict: `candidate-not-accepted`. `APPROVAL_NEEDED`: none. The worktree is
intentionally unstaged and uncommitted.
