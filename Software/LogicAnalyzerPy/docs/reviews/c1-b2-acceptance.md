# C1-B2 independent acceptance

- Reviewer: `/root/c1_b1_acceptance`
- Reviewed commit: `37bdd50da4c85f32eb0055ca2a34be92e7edb2f0`
- Reviewed tree: `ba16e00fdc4a4bc88d9e02dcdf6742d840ee7a9c`
- UTC timestamp: `2026-08-16T23:49:05Z`
- Verdict: **pass**

## Candidate and scope

`HEAD` and `git rev-parse <commit>^{tree}` matched the exact candidate. The tracked worktree was clean before this acceptance record. The C1-B2 delta adds only the authorized typed model, V2 codec/parser, fake transport, bounded internal recovery, replay loader, NumPy lock/runtime dependency, verifier-owned tests/replay notes, and B2 progress/review records. No changed path exists under `Firmware/` or `Software/LogicAnalyzer/`; no pySerial, hardware I/O, hardware CLI behavior, wider mode, GUI/Qt, pythonnet/Roslyn, TCP, or later-cycle implementation was introduced.

## Acceptance dispositions

### Golden protocol, parsing, and model boundary

- **Pass.** Independently inspected the literal verifier golden vectors and production codec. Identity is exactly `55 aa 00 aa 55`; rising/falling requests match the accepted 49-byte command-plus-payload/55-byte framed fixtures, retain the explicit 48-byte struct layout, reserved-byte escaping, and differ only at native inverted offset 2 (literal payload index 3).
- **Pass.** `ByteParser` is the sole byte owner for ASCII/binary phases. Verification covers one-byte identity and capture fragmentation; lossless coalesced `CAPTURE_STARTED` + LE count + samples + timestamp-count parsing; exact five identity fields; malformed/overlong/unterminated/extra input; invalid status/count/truncation/timestamp data; and negotiated count/rate bounds before NumPy sample materialization.
- **Pass.** Typed `DeviceInfo`, `CaptureConfig`, and `CaptureResult` enforce V6.0-or-newer identity, exact D0-D7 ordering, typed `uint32` fields, positive rate/post count, negotiated device bounds, rank-one C-contiguous `uint8` samples, D0 trigger acceptance, and trigger-time boundary semantics (`pre=2`: index 1 is `-1/rate`, index 2 is time zero).

### Fake transport and recovery

- **Pass.** Fake transport has finite timeout validation, exact reads, disconnect behavior, and idempotent close. Recovery sends exactly one raw `0xff`, uses a single deadline across the bounded drain, caps continuous drain at 4096 bytes, closes before the reopen/re-identify callback, and closes on write/drain/identity failure. Tests prove successful re-identification after recovery and stable `RecoveryError` on a second recovery attempt.
- **Pass.** Domain failure surfaces remain stable and scoped: `ValidationError`, `ProtocolError`, `TransportTimeout`, `TransportClosed`, and `RecoveryError`; malformed integer packing and replay inputs are converted to domain errors rather than accepted or left as raw success paths.

### Hostile replay contract

- **Pass.** The loader first bounds archive/member metadata and inspects NPY headers before `np.load`, then loads with `allow_pickle=False`. Tests cover exact two-member naming, duplicate/missing/extra/path members, encrypted and unsupported-compression central-directory claims, archive/member/count limits, object/float/non-rank-one header rejection before `np.load`, invalid UTF-8/canonical JSON/schema, unknown keys, all count relations, exact `uint8` shape, bounded labels/mappings, and device/capability/type/negotiated-limit validation.
- **Duplicate-ZIP warning disposition: accepted.** The focused and accumulated suites emit one `zipfile` `UserWarning` while the verifier deliberately creates `samples.npy` twice to test duplicate-member rejection. The warning arises in test fixture construction; `load_replay` rejects that archive, and the warning does not indicate an accepted replay or production behavior defect.

### Dependencies and import boundary

- **Pass.** `pyproject.toml` pins runtime `numpy==2.2.2`; `requirements-dev.in` and hash-locked `requirements-dev.lock` contain the same version (lock SHA-256 `1dd0a6e018394c276bc8a5e7939e7380b1a3ab3ac67fd306e53cfb75130c44c6`). The reused Python 3.12.13 environment passed `pip check`, hashed lock installation, and no-build-isolation/no-deps editable installation. AST import-boundary checks pass; core modules do not import serial, Qt, or CLI modules.

## Commands and results

Run from `Software/LogicAnalyzerPy` using Python 3.12.13:

| Command | Result |
| --- | --- |
| `.venv/bin/python -m pip check` | pass — no broken requirements |
| `.venv/bin/python -m pip install --require-hashes -r requirements-dev.lock` | pass |
| `.venv/bin/python -m pip install --no-build-isolation --no-deps -e .` | pass |
| `.venv/bin/python -m pytest tests/verification -q` | pass — 108 passed; one expected duplicate-member construction warning |
| `.venv/bin/python -m ruff check .` | pass |
| `.venv/bin/python -m mypy src` | pass — no issues in 14 source files |
| `.venv/bin/python -m pytest -m "not hardware"` | pass — 124 passed; same expected warning only |
| `.venv/bin/python -m pico_logic_analyzer --help` | pass |
| `git diff --check <candidate>^ <candidate>` | pass |
| changed-path check under `Firmware/` and `Software/LogicAnalyzer/` | pass — no paths |

## Limitations and deferrals

This acceptance proves only the C1-B2 pure/fake/replay surface. It does not claim a physical board trace, actual serial/pySerial behavior, operator wiring, capture export, or hardware recovery. The native 48-byte ABI, padding, edge polarity, and V2 identity remain source-derived until C1-B3/C1-B4 physical confirmation. C1-B3 owns serial transport/identity; C1-B4 owns physical capture and artifact writing; C1-B5 owns final lifecycle and physical recovery proof.

## New findings

None.
