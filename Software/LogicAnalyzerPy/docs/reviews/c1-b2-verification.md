# C1-B2 independent verification matrix

Status: verifier tests are bound to the current public model, protocol, fake
transport, recovery, and replay APIs. Expectations below are fixed by accepted
C1-B1 fixtures and the settled Cycle 1 contracts, not by production behavior.

| Surface | Independent input | Required observable result |
|---|---|---|
| Identity request | Literal `55 aa 00 aa 55` | Encoder emits exactly five bytes. |
| Rising/falling request | Literal accepted 49-byte payloads / 55-byte frames | Byte-for-byte equality; native offsets 3/31/47 are zero; only payload offset 3 differs (`00`/`01`). |
| Escaping | `aa` and `55` in pre/post values, plus standalone `f0` | Encode `f0 5a`, `f0 a5`, and `f0 00`; delimiters remain unescaped. |
| Identity parser | Five valid LF-terminated fields, one byte at a time | Parses identity/capabilities with no byte loss. |
| Identity rejection | Four/six fields; over-128-byte field; unterminated field; invalid ASCII/grammar | Bounded protocol error, never binary fall-through. |
| Capture parser | `CAPTURE_STARTED\n` + LE count + samples + zero timestamp count in one chunk and one-byte chunks | Same samples/count in both cases; no loss of coalesced bytes. |
| Capture rejection | Other status, count unequal to request, count above bound, truncation, timestamp count nonzero | Failure before unbounded allocation or false success. |
| Fake transport | Read timeout, disconnect, repeated close | Finite failure and idempotent close. |
| Recovery | In-flight capture timeout/cancellation then valid identity | Exactly one raw `ff`, bounded drain/close/reopen sequence, then identity succeeds. No `ff` outside in-flight recovery. |
| Capture model | D0 rising/falling; `pre=2`, `post=1` | D0 accepted/captured; `trigger_index=2`; index 1 is `-1/rate`; index 2 is zero/trigger. |
| Replay normal | Two-member `.npz`, rank-one `uint8`, UTF-8 JSON metadata | Loads with pickle disabled and validates all count/metadata invariants. |
| Replay hostile | Cases enumerated in `testdata/replay/README.md` | Reject before/while safely loading, with fixed archive/count bounds. |
| Dependency boundary | Walk core package imports | No core module imports `serial`, Qt/PySide, or CLI modules. |

## Evidence sources and deferrals

The frame, layout, escape, identity, and cancellation expectations are
source-derived from the C1-B1 protocol fixtures and provenance record, which in
turn cite `LogicAnalyzer_Structs.h`, `LogicAnalyzer.c`, `AnalyzerDriverBase.cs`,
`LogicAnalyzerDriver.cs`, `CaptureSession.cs`, and `VersionValidator.cs`.
They remain unobserved-wire expectations pending C1-B3/C1-B4 physical evidence.

The replay contract explicitly belongs to C1-B2/C1-B4. This verifier will create
the hostile NPZs in temporary storage, so no binary fixture can accidentally be
accepted merely because a writer and reader share the same defect.

## Findings resolved before final verification

- The `parse_identity` public API must reject an immediately coalesced
  sixth LF field; consuming five fields and leaving an extra field buffered does
  not meet the exact-five-field contract.
- Compatibility is V6.0-or-newer per `VersionValidator.cs`; a syntactically
  valid V5 identity is not sufficient.
- Recovery tests require the public recovery state machine to write exactly one
  raw `ff`, close the old transport, and invoke re-identification after the
  bounded drain. They do not accept an arbitrary public abort interface.

These cases were corrected before the final run, along with finite (not merely
positive) timeout validation, mandatory close on every recovery failure path,
explicit uint32 and negotiated-device bounds, canonical replay JSON, and replay
device/capability validation.

## Final independent result

Verdict: **pass** for the C1-B2 non-hardware evidence surface.

Run from `Software/LogicAnalyzerPy/` against the hash-locked project `.venv`
after the final implementation formatting pass:

- `python -m pytest tests/verification -q`: 76 passed. One expected `zipfile`
  warning is emitted while intentionally creating a duplicate-member hostile
  archive; the archive itself is rejected by the loader.
- `python -m pytest -m "not hardware"`: 91 passed, with that same fixture
  construction warning only.
- `python -m ruff check .`: pass.
- `python -m mypy src`: pass (`Success: no issues found in 14 source files`).
- `python -m pico_logic_analyzer --help`: pass.
- `git diff --check`: pass.

Replay-bound coverage includes a sparse >32 MiB archive; central-directory-only
claims above the 64 KiB metadata and 17 MiB samples limits; a central-directory
encrypted flag; and a valid NPY header declaring 16,777,217 `uint8` samples with
no payload. The latter safely proves rejection but does not claim an allocation
measurement. ZIP duplicate-member generation emits the warning stated above;
it is intentionally retained because it exercises the loader's duplicate
member rejection.

No hardware or network operation was performed. The V2 native layout/polarity
fixtures remain source-derived and require their separately documented C1-B3/
C1-B4 physical-wire confirmation.

## Qualified verifier handoff

- Completed at: `2026-08-16T23:40:07Z`
- Base HEAD / tree: `a5e09fc377dd51388c6649ad0a688901eeb65be6` /
  `bd21a329669a41b3802c73cf4a423849e6db4220`
- Worktree qualification: intentionally dirty C1-B2 implementation worktree.
  Modified tracked paths are `pyproject.toml`, `requirements-dev.in`, and
  `requirements-dev.lock`; untracked paths are the B2 production modules,
  implementation tests, verifier tests, replay test-data directory, and this
  review. No unrelated path was edited by this verifier.
- SHA-256 of `git diff --binary HEAD --` for exactly those three modified
  tracked project files: `1ff70aa06aa9015bc6709261adb02d8368d59679d973fea3e96a079c5affe07f`.
- Verifier test SHA-256s: `golden.py`
  `7f677e81f22be15ca0de75753d5c40e78fd53eab1fffef18be3cc53573ee05c8`,
  `test_protocol_blackbox.py`
  `f13fecddae741b4b7e9a55e82ee69fb100cace2c7eabb91b3c7e820c5a7702b0`,
  and `test_replay_blackbox.py`
  `48be95258b50ab6e6f1802637b4a092edaea405b3c49133770d150bcc9637a1d`.

Interim independent runs first reported `changes_required`: missing locked
NumPy, V5 identity acceptance, non-finite timeout acceptance, recovery cleanup
gaps, raw `struct.error` for uint32 overflow, absent negotiated-rate validation,
and replay JSON/device-capability validation gaps. The implementation corrected
each finding; the final commands above passed every C1-B2 acceptance surface.

## Correction review — expanded root audit

- Completed at: `2026-08-16T23:44:58Z`
- Base HEAD / tree: `a5e09fc377dd51388c6649ad0a688901eeb65be6` /
  `bd21a329669a41b3802c73cf4a423849e6db4220`
- Worktree qualification: the same intentional C1-B2 dirty worktree described
  above; its tracked project diff remains SHA-256
  `1ff70aa06aa9015bc6709261adb02d8368d59679d973fea3e96a079c5affe07f`.
- Expanded verifier: `python -m pytest tests/verification -q` — 107 passed;
  one expected duplicate-ZIP construction warning.
- Accumulated non-hardware suite: `python -m pytest -m "not hardware"` —
  122 passed; the same expected fixture-construction warning only.
- `python -m ruff check .`, `python -m mypy src`,
  `python -m pico_logic_analyzer --help`, and `git diff --check` all passed.

The correction suite proves NPY header rejection occurs before `np.load` for
oversized-count, object-dtype, and non-rank-one sample headers; validates all
requested replay negative/uint32/device/capability cases; requires exact typed
model fields and bounded result labels/mappings; rejects any already-buffered
trailing identity or capture bytes; and verifies a continuous drain respects
the fixed byte cap and one overall timeout budget before close/re-identification.
All 13 interim failures from the expanded audit were resolved. No new finding
was observed.

Correction verdict: **pass** for C1-B2 non-hardware verification. Physical-wire
confirmation remains deferred to C1-B3/C1-B4 as previously recorded.

## Post-integration recovery correction

- Completed at: `2026-08-16T23:45:44Z`
- Base HEAD / tree: `a5e09fc377dd51388c6649ad0a688901eeb65be6` /
  `bd21a329669a41b3802c73cf4a423849e6db4220`
- Recomputed SHA-256 of `git diff --binary HEAD --` for the three tracked B2
  metadata files is `1ff70aa06aa9015bc6709261adb02d8368d59679d973fea3e96a079c5affe07f`.
  It is unchanged because `driver/recovery.py` remains an untracked B2 file;
  its independently qualified SHA-256 after the integration correction is
  `dfd20e793a1075132d367cd92b7ac5f112f696eefea9fb1b36f3b72fbf18adfd`.
- Focused recovery verifier: `python -m pytest
  tests/verification/test_protocol_blackbox.py -q` — 57 passed.
- Full verifier: `python -m pytest tests/verification -q` — 107 passed with
  the expected duplicate-ZIP construction warning only.
- Accumulated non-hardware suite: `python -m pytest -m "not hardware"` — 122
  passed with that same expected warning only.
- `python -m ruff check .`, `python -m mypy src`,
  `python -m pico_logic_analyzer --help`, and `git diff --check` all passed.

The single-close/stable-`RecoveryError` integration correction preserved the
independently tested shared timeout deadline, fixed drain byte cap, close-before-
re-identify ordering, failure cleanup, and exactly-one cancellation byte.

Post-integration verdict: **pass**. No new finding.

## Final identity-encoder integration check

- Completed at: `2026-08-16T23:46:36Z`
- Base HEAD / tree: `a5e09fc377dd51388c6649ad0a688901eeb65be6` /
  `bd21a329669a41b3802c73cf4a423849e6db4220`
- Recomputed tracked metadata-diff SHA-256 remains
  `1ff70aa06aa9015bc6709261adb02d8368d59679d973fea3e96a079c5affe07f`.
  The untracked corrected recovery source SHA-256 is now
  `d8d6e0a4cc4be6ca738eb57d4908fcd530ffdef6aba8f5b48b5437b400de555b`;
  the untracked protocol source SHA-256 is
  `6c8c2cdcf975baaec917a8d075aaaa2f2f3f7a34540c9925be5c9d10058b9255`.
- Added black-box assertion: `encode_identity_request()` equals the literal
  accepted `IDENTITY_REQUEST` (`55 aa 00 aa 55`), without deriving the expected
  bytes through production code.
- `python -m pytest tests/verification -q`: 108 passed; expected duplicate-ZIP
  construction warning only.
- `python -m pytest -m "not hardware"`: 124 passed; same expected warning only.
- `python -m ruff check .`, `python -m mypy src`,
  `python -m pico_logic_analyzer --help`, and `git diff --check`: pass.

Final C1-B2 verifier verdict: **pass**. No new finding.
