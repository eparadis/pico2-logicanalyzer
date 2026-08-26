# C3-B1 semantic-fixture verification — round 3

## Identity and immutable subject

- Verifier identity/role: `c3-b1-semantic-fixture-verifier-1`
  (`/root/c3_b1_fixture_verify`), independent semantic-fixture verifier.
- Fixture candidate owners: `c3-b1-semantic-fixture-implementor-1` and
  `c3-b1-semantic-fixture-implementor-replacement-1`.
- Distinct fixture acceptance identity:
  `c3-b1-semantic-fixture-acceptance-1`.
- Distinct runner identities: `c3-b1-pre-execution-runner-implementor-1`,
  `c3-b1-pre-execution-runner-verifier-1`, and
  `c3-b1-pre-execution-runner-acceptance-1`.
- Governing commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Tested candidate commit/tree: `882af78a2530879329e6525fae0c5b1f96883100` /
  `aedb51155a25720a79417d1a34112c6e171ec0f9`.
- Verification UTC: `2026-08-26T23:46:30Z`.
- Descendant/worktree qualification: verification began at HEAD
  `ab16ecbe5b47dce18782fc4ddd62ff48af0971ed`, tree
  `2cd61ce7d482cfc76df70411d726b96830ebca87`, branch `python-rewrite`, with a
  clean worktree. Candidate-path `git diff 882af78..HEAD` was empty. This new
  record is descendant evidence and does not alter the candidate.

## Authority, method, and execution exclusion

No earlier pass transferred. Expectations were freshly derived from the
approved goal/orchestration/batch contracts, normative discovery Step 5, and
static AST/source inspection of the exact checked-in decoder files. The audit
independently evaluated every transition and wait predicate, skip advancement,
matched tuple, finite boundary, record coordinate/value/order, option row, cap
rationale, import, notice, digest, and v1 byte. Candidate claims and passing
implementation tests were not behavioral oracles.

No decoder, approved snapshot, shim/helper, host, C#, .NET, pythonnet,
libsigrokdecode, `sigrok-cli`, external/reference runtime, hardware, server, or
browser was imported or executed. No executable cap enforcement is present or
claimed.

## Environment and exact commands

- macOS 15.7.7 (24G720); Python 3.12.13 from `.venv/bin/python`.
- `rtk git rev-parse HEAD HEAD^{tree} 882af78... 882af78...^{tree}` — exit 0;
  exact identities above.
- `rtk git status --short` and candidate-path `rtk git diff --name-status
  882af78..HEAD` — exit 0, empty.
- `rtk .venv/bin/python -m pytest -q
  tests/verification/test_c3_b1_semantic_fixture_candidate.py
  tests/implementation/test_cycle3_fixtures.py` — exit 0, `14 passed`, no
  skips. The independent deeper checks below expose uncovered contradictions.
- Independent static wait evaluator over all 107 waits, including true edge/
  level predicates, exact skip displacement, empty wait, simultaneous matches,
  and terminal out-of-input calls — exit 0; all rewritten wait predicates and
  claimed matches are internally consistent.
- Independent coordinate audit requiring
  `0 <= start <= end <= sample_count` — exit 0 as a diagnostic script; found
  five invalid records listed below.
- Independent data-line/source-state audit for UART, SPI, and I2C, plus static
  inspection of exact `wait/register/put` branches — exit 0; findings below.
- Independent v1 schema/time/base64/canonical-byte audit — exit 0; canonical
  bytes reproduce the checked-in objects but all 12 objects violate their own
  samplerate/time-denominator invariant.
- `rtk .venv/bin/python scripts/generate_cycle3_fixtures.py --check` — exit 0.
- Independent `git show` SHA-256 recomputation over generator, six artifacts,
  and nine source files — exit 0; digests matched.
- Static generator AST/import/no-oracle and scoped prohibited-runtime audit —
  exit 0; no runtime oracle or enforcement path found.
- `rtk git diff --check` — exit 0. No required check was skipped.

## Artifact digests

| Exact candidate artifact | SHA-256 |
| --- | --- |
| generator | `84caec2555e8af1dc8614d7375e27375ac64b5119aece7e0363022e1bdf61b77` |
| `provenance.json` | `f044a1584c817d877441ef05e64c3be370257e9d1ac8d2164c697de0dc42d1c1` |
| `semantic-fixtures.json` | `3ff8b6451a27c15455a31eef9df06831a4ccc76f028d9afbdbfa5d8a2d84fd01` |
| `option-matrix.json` | `0b5947c99f5e56b5ebe4e17cff4180bd063ce4a8035d07c45fa41a2108c9d737` |
| `typed-vectors.json` | `3c72777d8f9da29edd16b7796c201fe090a821e64af17113aa10d43021e46fb8` |
| `experiment-caps.json` | `1c0ccd0330a631885c02f1dbbadac9ced9b66236b2d22a2f3096d7d12c9f05f0` |
| `manifest.json` | `1daaceaf233adca37740765c3d38539b7104e5c3ff264e0bf11cd2afc3feb213` |

All nine source hashes equal the approved discovery/provenance values. The
closed import list, including relative `.pd` imports, and per-file notice
observations remain accurate.

## Numbered findings and dispositions

1. **Pass — wait predicate truth and call-shape correction.** The rewritten
   schedules now include SPI's initial `wait({})` and edge/CS alternatives,
   UART's start edge plus skip/edge alternatives, I2C's state-specific START,
   SCL-rise, and START/STOP alternatives, true simultaneous matches, and an
   explicit failed terminal wait. All nonterminal returned pins equal declared
   levels and all `matched` tuples are true exactly where asserted. This is a
   real correction of the round-2 predicate defect, not a transferred pass.

2. **Changes required — five records lie outside their capture.** The UART
   error fixture has BREAK records ending at 120 and IDLE ending at 130 with
   `sample_count=116`. Both completed SPI fixtures have the final bit
   annotation ending at 170 with `sample_count=161`. A half-open end may equal
   capture count, but cannot exceed it. These records cannot be valid output of
   the stated finite capture and contradict the fixture's own time boundary.

3. **Changes required — UART waveforms and records do not encode the claimed
   values or source coordinates.** Integral 1,152,000/115,200 timing correctly
   gives ten samples per bit and centers at 6, 16, ..., but the mechanically
   alternating data line yields alternating sampled bits rather than claimed
   `0xA5`. Expected START/DATA/STOP spans remain old 0/10 boundaries despite a
   start edge at 1 and source half-bit calculations around the actual sample
   centers. The combined error fixture's alternating line cannot create its
   claimed sustained BREAK and IDLE, has two identical packet annotations, and
   still cannot produce the complete claimed parity/stop/break/idle/frame
   sequence. Thus exact values, classes, order, and coordinates are not
   independently derived from the timeline.

4. **Changes required — SPI `BITS`, coordinates, and output sets remain
   incorrect.** Eight true sampling edges now exist. However source
   `handle_bit()` stores newest-first `Data` entries and extrapolates the last
   bit end from first-to-last sample spacing. Mode 0 therefore produces a word
   span ending at 290, and mode 3 starts at 20 and ends at 300; the candidate
   hard-codes 10..150 and per-bit 20-sample spans ending at 170. Its MOSI/MISO
   `BITS` entries and record spans do not match those source calculations.
   Both word-eight fixtures also omit the bitrate metadata emitted immediately
   after `putdata()`. The word-one fixture omits source-mandated `BITS`, bit
   annotation, and metadata and places DATA before binary even though binary is
   emitted first. Exact source order/classes/tags/values/coordinates are
   therefore incomplete.

5. **Changes required — I2C traffic records are disconnected from the bus.**
   The full fixture keeps SDA low for all 18 rising clock slots until STOP, so
   it encodes zero address/data/ACK bits, not shifted address `0x50`, data
   `0x33`, and NACK. Its records retain obsolete 10..191 coordinates while the
   rewritten bus spans through STOP at 351, and its Python `BITS` value is an
   empty list instead of the eight reversed source bit tuples. The repeated
   START condition at 176 is now genuine, but the preceding SDA sequence still
   does not demonstrate the claimed unshifted address behavior. The incomplete
   case has a genuine partial wait sequence, but isolated correctness cannot
   establish the full I2C oracle.

6. **Changes required — every v1 golden has inconsistent rational time.** The
   root of each of the 12 typed vectors says `samplerate_hz=1000000`, while all
   record start/end absolute and trigger-relative denominators are `1152000`
   because the generator's global record default changed. The canonical bytes
   faithfully encode invalid objects; byte reproducibility cannot substitute
   for the normative denominator-equals-root-samplerate requirement.

7. **Changes required — option-equivalence text is more specific but many
   dispositions remain semantically false.** The matrix is unique and complete
   in row shape, direct rows materialize their values, and arguments now cite
   source functions. But data widths 5/6/7/8/9 change loop termination and
   output; non-`none` parity choices enter a different state; stop widths alter
   stop collection; inversion changes edge/level interpretation; sample-point
   boundaries alter skip locations; and packet delimiter/length values alter
   emission. Linking these accepted values by static equivalence to a fixture
   that does not materialize them does not prove unchanged behavior. The
   phrase “named fixture directly fixes” cannot make a different option value
   equivalent. The exhaustive accepted option matrix remains without genuine
   direct or valid static-equivalence authority.

8. **Changes required — cap calculations do not support the stated exact
   margins.** Each cap repeats maxima `352 samples, 16 records, depth 3` and
   claims an 8x rounded margin. Values such as 100,000 input samples, 100,000
   records, 4,000,000 request bytes, 16,000,000 encoded bytes, 5,000 ms, 512
   recursion frames, and 536,870,912 address-space bytes are not 8x those
   maxima or derived from them. Text/binary/request/encoded/decoded/retention,
   time, recursion, and address-space caps require category-specific maxima and
   arithmetic; none is recorded. Exact finite values and boundaries exist and
   enforcement remains correctly unclaimed, but independent derivation and
   mutual consistency are not proven.

9. **Pass — provenance/no-oracle/no-enforcement portions.** Source/artifact
   hashes, imports, notice observations, pending project/legal disposition,
   deterministic rebuild, generator static imports, `0xFF` integer sentinel
   ordering, absence of prohibited execution/dependencies, and explicit lack
   of enforcement are correct for this exact candidate.

## Discrepancies, deferrals, scope, and approval

Findings 2-8 are candidate defects requiring a new immutable fixture candidate
and fresh verification; no pass transfers. Project/legal disposition, actual
runner/enforcement probes, decoder characterization, raw measurements,
threshold review/acceptance, operator approval, and later B1 gates remain
deferred. The verifier did not repair the candidate or edit prior immutable
tests/records, product, runner/method/probe/enforcement/raw, governance,
schema/validator/manifest, decoder, package/lock/workflow, Cycle 1/2, browser,
firmware, hardware, C#, or Cycle 4 paths.

- Approval need: none.

changes_required
