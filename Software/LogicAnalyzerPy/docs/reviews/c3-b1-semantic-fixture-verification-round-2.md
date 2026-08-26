# C3-B1 semantic-fixture verification — round 2

## Identity and immutable subject

- Verifier identity/role: `c3-b1-semantic-fixture-verifier-1`
  (`/root/c3_b1_fixture_verify`), independent semantic-fixture verifier.
- Fixture candidate owners: `c3-b1-semantic-fixture-implementor-1` and
  `c3-b1-semantic-fixture-implementor-replacement-1`.
- Distinct fixture acceptance identity:
  `c3-b1-semantic-fixture-acceptance-1`.
- Distinct runner implementor/verifier/acceptance identities:
  `c3-b1-pre-execution-runner-implementor-1`,
  `c3-b1-pre-execution-runner-verifier-1`, and
  `c3-b1-pre-execution-runner-acceptance-1`.
- Governing commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Tested candidate commit/tree: `79be308bc0bcab6dcdd4568a099fc730fd4fc778` /
  `8c64cb86f34d57f77b02aec5927689fb86d78953`.
- Verification UTC: `2026-08-26T23:34:27Z`.
- Descendant/worktree qualification: verification began at HEAD
  `a0c0f7880549456a64af6906a5689668014d6226`, tree
  `655fa87112ef7c45a633b799f609b8d37247bdd5`, branch `python-rewrite`, with a
  clean worktree. `git diff 79be308..HEAD -- <all candidate paths>` returned no
  differences. This new review record is descendant evidence and does not
  alter the candidate.

## Authority, provenance, and prohibited execution

Expectations were freshly derived from the approved goal/orchestration/batch
contracts, the normative Step 5 discovery contract, and inert static AST/source
inspection of the exact nine-file snapshot. No round-1 pass transferred.
Candidate statements and implementation tests were not treated as behavioral
oracles. No decoder, approved snapshot, shim/helper, host, C#, .NET, pythonnet,
libsigrokdecode, `sigrok-cli`, external/reference runtime, hardware, server, or
browser was imported or executed. No executable enforcement exists or is
claimed by this candidate.

## Environment and exact commands

- macOS 15.7.7 (24G720), Python 3.12.13 from `.venv/bin/python`.
- `rtk git rev-parse HEAD HEAD^{tree} 79be308... 79be308...^{tree}` — exit 0;
  identities above.
- `rtk git status --short` and candidate-path `rtk git diff --name-status
  79be308..HEAD` — exit 0, empty.
- `rtk .venv/bin/python -m pytest -q
  tests/verification/test_c3_b1_semantic_fixture_candidate.py
  tests/implementation/test_cycle3_fixtures.py` — exit 0, `13 passed`, no
  skips. These round-1 checks do not cover predicate truth or full source-call
  fidelity.
- Independent static transition evaluator over all timeline waits — exit 0;
  found 57 claimed `matched` tuples inconsistent with the declared levels and
  edges among 89 waits.
- Independent boundary audit over every transition, wait, and record — exit 0;
  all stated coordinates are numerically below 256, but incomplete fixtures do
  not trace termination at sample 256 and full I2C waits lack supporting
  transitions after sample 91.
- Static AST/source audit of metadata, imports, registration order, `wait()`,
  `put()`, and protocol branches in exact candidate blobs — exit 0; findings
  below.
- `rtk .venv/bin/python scripts/generate_cycle3_fixtures.py --check` — exit 0.
- Independent `git show` SHA-256 recomputation over generator, six artifacts,
  and nine snapshot files — exit 0; manifest/source values matched.
- Canonical-byte recomputation with Python 3.12 `json.dumps` using the exact
  normative parameters — exit 0; all 12 v1 goldens matched.
- Static generator AST/import/no-oracle and scoped prohibited-runtime search —
  exit 0; no decoder/reference oracle or executable enforcement path found.
- `rtk git diff --check` — exit 0. No required check was skipped.

## Artifact digests

| Exact candidate artifact | SHA-256 |
| --- | --- |
| generator | `70743eb7256a2c6cacd33654734ff278be01b8cae25c5208e5759d8a154d0396` |
| `provenance.json` | `f044a1584c817d877441ef05e64c3be370257e9d1ac8d2164c697de0dc42d1c1` |
| `semantic-fixtures.json` | `a32adf7263e46149dec87ef8e2eccbbc6354b11163266bea8bcff400e62fba89` |
| `option-matrix.json` | `08e288aa7a2733b04b74ca973eef37da0e5a18c9e4be52fb01bb229a968a5b47` |
| `typed-vectors.json` | `3f3e31c40da00ae068bc286a000387c216b8a3a1342c95f4c3d684c4fb141a8d` |
| `experiment-caps.json` | `f82e5d9431de3cda11341fabe554db92378e4ca9e2ac1a8c4e315a5ad2669dc7` |
| `manifest.json` | `f0c8aae4d3ceffe92301f031d7bd81d7f6816138e64a07e509780c5aabd8eca2` |

The nine source digests again equal the approved discovery values and candidate
provenance. Per-file notice observations remain byte-accurate. The three
relative `.pd` imports are now listed, and the full closed import inventory
matches static AST inspection.

## Numbered findings and dispositions

1. **Pass — immutable provenance, notices, generator, declarations, and v1
   bytes.** Exact source and artifact digests match; the package/legal review is
   correctly pending without a legal conclusion. Static declarations retain
   decoder source order. The generator is stdlib-only static data processing,
   rebuilds deterministically, and contains no runtime oracle. The v1 vectors
   cover all nine Python tags and four record kinds with valid fields, rational
   times, canonical base64, canonical Python 3.12 bytes, and one LF.

2. **Changes required — normalized pins conceal 57 false wait matches.** The
   generator now overwrites each returned pin with the timeline level, so the
   round-1 pin-consistency test passes. It does not make the stated condition
   true. Independent edge evaluation found 57 invalid claimed matches across
   every timeline. Examples: UART repeatedly claims falling edges at declared
   rising or unchanged samples; SPI claims rising/falling clock matches on
   alternating opposite edges; the one-bit SPI fixture claims a simultaneous
   CS edge at sample 10 although CS changes at sample 11; I2C claims SCL rising
   or SDA edges where neither transition occurs. `matched` is therefore not a
   truthful result of the declared wait and transition data.

3. **Changes required — the traces do not contain the decoders' actual wait
   calls.** SPI statically calls initial `wait({})`, then alternatives
   `[{0:'e'}]` or `[{0:'e'},{3:'e'}]`; the fixtures instead list repeated
   single `r`/`f` calls and omit the initial empty wait. UART constructs
   alternative data-sample/edge/idle conditions, including skip conditions;
   its fixtures instead repeat a falling-edge dictionary. I2C incomplete data
   traces repeat a START conjunction rather than the source state machine's
   SCL-rise/data and alternative START/STOP calls. Thus first/later empty wait,
   current/next search, skip, conjunction/alternative priority, and exact
   decoder lifecycle behavior are not frozen by genuine calls.

4. **Changes required — `sample_count = 256` does not complete or justify the
   timelines.** All listed coordinates are less than 256 and triggers are in
   range, but the same unexplained count is mechanically assigned to all 11
   cases. Full I2C declares no clock transition after sample 80 and no SDA
   transition after 91 while claiming SCL-rise waits through 180 and STOP at
   191. The incomplete cases end their wait traces at 50, 20, or 91 rather than
   documenting the failed wait/termination at 256. Consequently 256 neither
   supports full traffic nor proves end-of-input suppression/preservation or a
   boundary coordinate at capture count.

5. **Changes required — completed SPI records remain impossible and
   incomplete.** The mode-0 and mode-3 timelines contain only four actual
   sampling edges, not the eight needed for an 8-bit word, yet claim complete
   outputs. Their Python `BITS` records use an empty list rather than the eight
   source-created `Data(ss, es, val)` elements and put the present-side list in
   the wrong position for MOSI. Their synthetic per-bit coordinates do not
   follow the source's bit-boundary calculation. Although binary/BITS/DATA/bit/
   word kind order was added, the exact tags, values, coordinates, and source
   emissions are still not authoritative.

6. **Changes required — UART/I2C outputs were appended without a consistent
   protocol execution.** The new UART PACKET records are placed after FRAME
   even though static source calls packet handling while finishing data, before
   later parity/stop/frame processing. At 1 MHz with default 115200 baud the
   UART sample spacing is about 8.68 samples, while transitions and records use
   nominal 10-sample slots and even begin record coordinates at 0 despite the
   start edge at 1. The I2C repeated-start records are appended at sample 16,
   where the declared SCL is low, so the required high-SCL/SDA-falling
   condition is false. The full I2C data/NACK outputs similarly lack a matching
   clock/data timeline after sample 91. Names and isolated tags do not prove
   genuine output classes/order/coordinates.

7. **Changes required — option equivalence reasoning remains generic rather
   than source/value specific.** Forty equivalence rows still share two generic
   arguments; appending `Option <name> value <repr> is the reviewed source
   branch` makes strings unique but supplies no branch, line, invariant, or
   proof. It remains false that baudrate, data width, parity, stop width,
   inversion, sampling point, format, delimiter, and packet length all preserve
   the same sampled frame or merely affect rendering. Direct rows materialize
   their values and row IDs/rejection tuples are unique, but the complete
   accepted matrix lacks the required static-equivalence justification.

8. **Changes required — exact cap values remain unjustified.** All 17 required
   finite categories, units, domains, values, accept/reject boundaries, and the
   explicit no-enforcement disposition are present. Each rationale now repeats
   the value and unit, but otherwise uses the same assertion that it is
   conservative and “independently bounded.” No derivation, fixture maximum,
   relationship calculation, macOS constraint, safety margin, or reason for
   choosing that exact value is recorded. Internal consistency and independent
   derivation therefore remain claims rather than evidence.

9. **Pass with no transfer — bounded portions corrected.** Integer `0xFF`
   slots and `has_channel` booleans are correctly ordered; relative imports are
   now inventoried; direct option rows point to fixtures materializing the row
   value; UART packet and I2C repeated-start tag/class literals now exist; and
   cap enforcement remains expressly deferred. These local corrections do not
   overcome findings 2-8 or authorize the next B1 internal gate.

## Discrepancies, deferrals, scope, and approval

Findings 2-8 are exact-candidate discrepancies and require a new corrected
semantic-fixture candidate with fresh verification; they are not deferrals.
Project/legal disposition, runner/enforcement probes, snapshot execution,
characterization, raw observations, thresholds, operator approval, and later
B1 gates remain contractually deferred. The verifier did not repair the
candidate or modify the round-1 artifacts, product, runner, method, probe,
enforcement, raw, governance, schema/validator/manifest, decoder, package/lock/
workflow, Cycle 1/2, browser, firmware, hardware, C#, or Cycle 4 paths.

- Approval need: none.

changes_required
