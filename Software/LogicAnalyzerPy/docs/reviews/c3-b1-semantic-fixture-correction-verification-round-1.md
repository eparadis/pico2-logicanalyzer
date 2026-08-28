# C3-B1 semantic-fixture correction verification — round 1

## Identity and immutable subject

- Verification identity: `c3-b1-semantic-fixture-correction-verifier-1`
  (`/root/c3_b1_final_verify_fresh`).
- Completed: `2026-08-28T02:25:55Z`.
- Candidate commit/tree:
  `a98d328aab92f3dad66988fb70cc567946dc89d0` /
  `450aadcf26bd6c74860872bfbf0a0a1b32d94f3b`.
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Correction finding: `C3B2-IF001`.

The candidate changes exactly six tracked paths: the correction implementation
record, deterministic generator, semantic fixture, experiment caps, fixture
manifest, and focused implementation test. Every current candidate path is
byte-identical to its blob in the candidate commit. The untracked B2 paths
`src/pico_logic_analyzer/_decode/` and
`tests/implementation/test_c3_b2_private_host.py` were excluded completely;
they were neither read by this verification phase nor executed or modified.

The verification identity independently derived the expected result before it
inspected this committed correction. No implementation result or runtime
output transferred into the oracle.

## Independent source and fixture verification

The frozen UART source gives a ten-sample bit width and computes each sample
point as
`ceil(frame_start + (bit_width - 1) * sample_point / 100 + bitnum * bit_width)`.
For frame start 1 and sample point 99, the exact centers are 10, 20, 30, 40,
50, then 60 beyond the capture. Real level-changing edges occur at 1, 11, 21,
31, and 41; `[51, 0]` repeats the low level and is not an edge.

The candidate binds the exact successive returns 1, 10, 11, 20, 21, 30, 31,
40, 41, 50, then terminal sample 56. Conditions, matched tuples, and `[RX,TX]`
pins are exact. In particular, rising edges 11 and 31 start idle candidates,
so the following waits include idle alternatives 110 and 101 until the low
edges clear them. The terminal condition is exactly
`[{"skip": 10}, {"0": "e"}]`, both alternatives false, with pins
`[0, 255]`.

All six pre-termination emissions are exact and request-ordered:

1. Python STARTBIT/output 0 over half-open samples `[5,15)`;
2. start-bit annotation/output 2 over `[5,15)`;
3. RX data-bit `1` annotation/output 2 over `[15,25)`;
4. RX data-bit `0` annotation/output 2 over `[25,35)`;
5. RX data-bit `1` annotation/output 2 over `[35,45)`; and
6. RX data-bit `0` annotation/output 2 over `[45,55)`.

Every absolute time numerator equals its coordinate, every trigger-relative
numerator is coordinate minus trigger index 1, and every denominator is
1,152,000. Tags, annotation classes/texts, output IDs, emission indices, and
the complete source-ordered UART annotation/row/binary declarations are exact.
Only four of nine data bits exist, so no DATA, binary, formatted-data,
STOPBIT, FRAME, or other completed/partial-unit record is invented. Normal
end-of-input preserves the six already-emitted records.

Fourteen non-vacuous mutation families reject an old 50-percent center,
missing or reordered idle alternative, changed match/pin, missing or stale
emission set, invented completed output, shifted coordinate, changed tag,
altered option, transition, capture boundary, or declaration. The unmodified
candidate passes before those mutations.

## Static oracle, deterministic generation, and digest closure

The generator imports only `argparse`, `copy`, `hashlib`, `json`, `pathlib`,
and `__future__`. Its AST has no `exec`, `eval`, `compile`, `__import__`, or
`open` call and no raw-observation, characterization, subprocess, B2 runtime,
pythonnet, libsigrokdecode, or sigrok-cli dependency/reference. It retains the
literal oracle declaration `independently authored declarative timelines; no
runtime output`. No decoder or runtime output can enter its build graph.

The exact candidate digests are:

| Artifact | SHA-256 |
| --- | --- |
| implementation record | `6f9b3c483d2324187ad9c3a571fdd6ff5979aaf5f21142c471ded1b021327b66` |
| generator | `d872fe9f6c1cb3407a8d05d7b9e03e3bb34b10baee8fa47e55b57bb4b64574f6` |
| semantic fixtures | `1d97cf3ff4fb560e7dd73b621da0e40d7f1fb310b60c2d43fcb59f3ebf91a329` |
| experiment caps | `6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d` |
| fixture manifest | `ce8eceb72480d042ef298cb6fe6944a4808fed0644e729c8c2de9fa1955ec37f` |
| implementation test | `fccc9746dfd50766cb3f6fbae72f08dfd40d57c791792ead2c76cf2eb6d68f45` |
| independent verification test | `d5a6a3f69fcdaf2b5d86e334d0091c758f7bb67c33b1e9b6bca2c056efe9a75d` |

Every manifest artifact digest and the generator self-digest recompute. The
canonical semantic corpus is 725,879 bytes. Every cap's named basis,
operation, multiplier, floor, result, inclusive acceptance, and first rejected
integer recompute independently. The directly affected values are request
bytes 46,456,256, retained-result bytes 185,825,024, and the unchanged
floor-controlled 68,719,476,736-byte address-space cap with its updated corpus
basis.

`provenance.json`, `option-matrix.json`, and `typed-vectors.json` remain
byte-identical to the candidate parent at their accepted SHA-256 values. The
corpus retains exactly 63 timelines, five edge decisions, and five optional-pin
cases. All 165 unique option rows remain linked: 62 direct fixtures and 103
unsupported rows. The `uart-sample_point-99` row still points to the separate
`direct-uart-sample_point-99` witness, so this correction neither captures nor
weakens its option-coverage ownership.

## Commands and results

All shell commands used RTK and repository-local Python 3.12.

- `.venv/bin/python -m pytest tests/verification/test_c3_b1_semantic_fixture_correction.py -q`
  — exit 0; 20 passed.
- `.venv/bin/python -m pytest tests/implementation/test_cycle3_fixtures.py -q -k 'uart_msb_9bit_incomplete or hand_authored_protocol_cases or direct_option_witnesses or matrix_equivalence'`
  — exit 0; four passed, eight deselected.
- `.venv/bin/python -m pytest tests/implementation/test_cycle3_fixtures.py -q -k 'not cycle3_fixture_surface_is_present_and_rebuildable'`
  — exit 0; 11 passed, one deselected.
- `.venv/bin/python scripts/generate_cycle3_fixtures.py --check`
  — exit 0; deterministic byte rebuild check passed.
- `.venv/bin/ruff check scripts/generate_cycle3_fixtures.py tests/implementation/test_cycle3_fixtures.py tests/verification/test_c3_b1_semantic_fixture_correction.py`
  — final exit 0. An initial verifier-local run found one E501 in the new
  verification file; only that verifier-owned formatting was corrected before
  the final pass. No candidate byte changed.
- `git diff --check` — exit 0.

Static inspection only occurred. No decoder, worker, characterization runner,
B2 test/code, raw observation, C#/.NET/pythonnet/libsigrokdecode/sigrok-cli,
external/reference runtime, hardware, network, build, or publication action
ran.

## Numbered findings and dispositions

1. `C3B2-IF001`: **closed for this correction candidate**. The former 50-percent
   schedule, incomplete wait conditions, stale coordinates, and missing four
   preserved bit annotations are corrected exactly.
2. Exact-six-file inventory assertion: **transparent historical
   applicability, not a candidate failure**. Running only
   `test_cycle3_fixture_surface_is_present_and_rebuildable` reproduces exit 1
   solely because four later governing JSON files are present:
   `b1-final-candidate.json`, `b1-final-candidate-round-2.json`,
   `threshold-proposal-round-1.json`, and `threshold-proposal-round-2.json`.
   The candidate did not add, edit, hide, or deselect them. All 11 applicable
   fixture tests pass.
3. Broad strict mypy over the two pre-existing untyped fixture files:
   **non-gate, not weakened**. The candidate changes no mypy configuration,
   dependency lock, or type scope and adds no `type: ignore`. Required focused
   pytest, deterministic generation, Ruff, digest, formula, and mutation gates
   are green.
4. Downstream authority: **still invalidated and ordered later**. This fixture,
   experiment-cap, and manifest identity changed. Prior runner/raw/proposal/
   operator/final-B1/manifest/checkpoint passes do not transfer; fresh
   correction acceptance and the governed B1 re-binding/proposal/operator
   sequence remain mandatory. This pass grants no B2 authority.

Open candidate findings: none.

## Verdict

`pass`
