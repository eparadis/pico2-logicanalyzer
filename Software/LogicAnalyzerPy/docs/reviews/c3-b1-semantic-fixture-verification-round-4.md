# C3-B1 semantic-fixture verification — round 4

## Identity and immutable subject

- Verifier identity/role: `c3-b1-semantic-fixture-verifier-1`
  (`/root/c3_b1_fixture_verify`), independent semantic-fixture verifier.
- Candidate owners: `c3-b1-semantic-fixture-implementor-1` and
  `c3-b1-semantic-fixture-implementor-replacement-1`.
- Distinct fixture acceptance identity:
  `c3-b1-semantic-fixture-acceptance-1`.
- Distinct runner implementor/verifier/acceptance identities:
  `c3-b1-pre-execution-runner-implementor-1`,
  `c3-b1-pre-execution-runner-verifier-1`, and
  `c3-b1-pre-execution-runner-acceptance-1`.
- Governing commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Tested candidate commit/tree: `f53c340f5896a768e4b67fd866030be9370db723` /
  `218a80a21c769cf8e11f37903b2c91df254e107c`.
- Verification UTC: `2026-08-27T00:40:14Z`.
- Descendant qualification: verification began at HEAD
  `3f5aab8b405a269e9a60ee692a1e61f86a286667`, tree
  `7e0561db47c4e1cfe9fac6b513aa5e89cf4c743c`, branch `python-rewrite`, with a
  clean worktree. Candidate-path `git diff f53c340..HEAD` was empty. This new
  record is descendant evidence and does not alter the candidate.

## Authority, method, and prohibited execution

No prior result transferred. I re-read `RTK.md`, `SUBAGENT_POLICY.md`, the
approved Cycle 3 goal/orchestration/batch B1 gate, normative discovery Step 5,
all prior immutable findings, the complete candidate diff, and the exact
checked-in decoder source. Expectations were independently calculated from
static source and declared timelines, never from decoder/runtime output or the
candidate's assertions.

No decoder, host, shim/helper, C#, .NET, pythonnet, libsigrokdecode,
`sigrok-cli`, external/reference runtime, hardware, network, installation,
server, or browser was imported or executed. No executable cap enforcement is
present or claimed.

## Environment and exact commands

- macOS 15.7.7 (24G720); Python 3.12.13 from `.venv/bin/python`.
- `rtk git rev-parse HEAD HEAD^{tree} f53c340... f53c340...^{tree}` — exit 0;
  identities above.
- `rtk git status --short` and candidate-path `rtk git diff --name-status
  f53c340..HEAD` — exit 0, empty.
- `rtk .venv/bin/python -m pytest -q
  tests/verification/test_c3_b1_semantic_fixture_candidate.py
  tests/implementation/test_cycle3_fixtures.py` — exit 0, `15 passed`, no
  skips. These checks do not prove earliest-match or exact nested values.
- `rtk .venv/bin/python scripts/generate_cycle3_fixtures.py --check` — exit 0.
- `rtk .venv/bin/python -m ruff check scripts/generate_cycle3_fixtures.py
  tests/implementation/test_cycle3_fixtures.py` — exit 0.
- Independent transition evaluator over all timeline conditions checked edge,
  level, skip, empty, matched, pins, finite EOI, and earliest intervening
  matches — diagnostic exit 0; it found widespread omitted UART edge returns,
  plus concrete I2C and CS intervening matches.
- Independent static recurrence/source-order audit of every named core fixture
  and all 51 matrix fixture IDs — diagnostic exit 0; findings below.
- Independent v1 field/type/time/base64/canonical-byte and decoder-identity
  audit — diagnostic exit 0; times and bytes pass, identity/declaration binding
  does not.
- Independent cap-schema arithmetic recomputation over all 17 entries — exit
  0; every operation/result and accept/reject boundary matches the checked-in
  structured data.
- Independent `git show` SHA-256 recomputation for the generator, six fixture
  artifacts, and nine source files — exit 0; all manifest/provenance digests
  matched.
- Static AST import/no-oracle and scoped prohibited-runtime audit — exit 0.
- `rtk git diff --check` — exit 0. No required check was skipped.

## Artifact digests

| Exact candidate artifact | SHA-256 |
| --- | --- |
| generator | `b737916e179f6be6478932edb2c0c278c512734e29956b2107e282ffc8a1041a` |
| `provenance.json` | `f044a1584c817d877441ef05e64c3be370257e9d1ac8d2164c697de0dc42d1c1` |
| `semantic-fixtures.json` | `2a053441fcafa212ca10d3dbc467cad25508458b225529ecdea39c76541d7048` |
| `option-matrix.json` | `0d36c7e8b1b7563b7a6de8a6b278324428ab96dbd3ae8896df8c6b179dbadf68` |
| `typed-vectors.json` | `c79a9acd10ee216d8422a7876ebc08b42f188f7cf6da066b20e8f77d1f258ba5` |
| `experiment-caps.json` | `20fbfccbfaa654b2d8f35847eb2a505031cac82fe7e7e16028d43e0e5d019e5d` |
| `manifest.json` | `a9cb277b022290104d89d03ad27e1567de7c4dbe3cbd5ac4f1252f9cbef7da43` |

All nine source hashes, relative/local/stdlib imports, import commit, prior
gitlink, per-file notice observations, and pending project/legal disposition
match the approved static inventory.

## Numbered findings and dispositions

1. **Pass — provenance, declarations, sentinels, deterministic rebuild, and
   static boundaries.** Exact source/artifact digests and notices match. The
   decoder declaration arrays and register/output IDs match static metadata and
   `start()` order. Optional pin vectors use exact integer `0xFF` and correct
   `has_channel` booleans for UART RX/TX and SPI MISO/MOSI/no-CS. Generator
   imports are stdlib-only, rebuild is byte-stable, and no runtime oracle or
   enforcement path exists.

2. **Changes required — UART wait traces omit earlier edge alternatives.**
   Each post-start wait is an alternative list containing the scheduled skip
   and `{line:'e'}`. The transition moves to the next bit at samples 11, 21,
   31, etc., before center skips at 16, 26, 36, etc. Therefore `wait()` returns
   at each intervening edge with `[False, True]`; the decoder calls
   `inspect_edge()`, recomputes a shorter skip, and only then reaches the bit
   center. The candidate omits those calls in the core UART cases and generated
   direct witnesses. This violates its frozen current-search/alternative
   semantics and makes wait history, matched order, samplenum, skip advancement,
   BREAK/IDLE processing, and terminal traces incomplete.

3. **Changes required — UART and I2C nested Python values use the SPI-only
   tag.** UART `databits` and I2C `data_bits` are ordinary Python lists whose
   elements are ordinary three-item lists. Only SPI's `Data(ss, es, val)`
   namedtuple may normalize to `tag:'spi-data'`. The candidate represents UART
   DATA bit entries and I2C BITS entries as `spi-data`, changing container kind
   and semantic type. This affects the two default UART directions, the full
   and repeated I2C cases, and generated direct UART witnesses.

4. **Changes required — UART expected output still contains impossible
   omissions/additions.** `uart-break-low-interval` drives a complete all-zero
   frame before the rising BREAK edge. Static source emits START, eight bit
   annotations, DATA, two binary records, invalid STOP, STOP, FRAME, and then
   BREAK; the fixture retains only BREAK records, contrary to the frozen rule
   preserving earlier emissions. The error fixture adds a Python `PACKET`
   record, but `handle_packet()` calls annotation-only `putx_packet()` and
   never emits Python PACKET. Hence source order/kinds remain false even where
   coordinates and A5 levels were corrected.

5. **Changes required — SPI newest-first recurrence is still wrong and no-CS
   output is absent.** For eight samples 10..150, source `handle_bit()` makes
   the newest bit `[150,290]`, not `[150,170]`; the completed word ends at 290.
   For mode 3 samples 20..160, it ends at 300. The candidate assigns uniform
   20-sample spans and ends at 170/180, so BITS entries, bit annotations,
   binary/Python/word spans, and capture boundary are wrong. Separately,
   `spi.decode()` emits Python `['CS-CHANGE', None, None]` at 0 before its first
   wait whenever CS is absent. Both completed no-CS fixtures and the incomplete
   no-CS fixture omit that mandatory record, so their emission order and EOI
   preservation are incomplete.

6. **Changes required — I2C and active-low SPI traces skip earlier bus
   events.** In the full I2C fixture, SCL rises at 370 before SDA rises at 371;
   the state machine's alternative wait must first return the data-bit match at
   370, but the trace jumps from NACK sample 350 to STOP 371. In the repeated-
   START fixture SDA rises while SCL is high at 205, which is an actual STOP;
   the trace instead skips it and claims repeated START at 216. The generated
   active-low SPI witness changes CS at 161, yet its wait trace jumps from clock
   160 to terminal 170 while expected records claim the missing CS/transfer
   event. These schedules cannot yield their expected records under the frozen
   earliest-match semantics. The full I2C bitrate is also wrong: static source
   computes `int(1152000 * 18 / 371) = 55892`, not `49676`.

7. **Changes required — direct option rows are named but not all genuine
   witnesses.** The matrix now has 56 accepted direct rows and 103 unsupported
   rows with unique IDs/rejection tuples, and every accepted row points to a
   fixture whose option mapping literally contains the value. That is useful
   structural closure. It is not semantic closure: the 48 UART witnesses share
   the omitted-edge and wrong nested-value defects; packet witnesses do not
   model the annotation-only source branch completely; and the generated
   active-low SPI witness omits the CS wait that makes the option meaningful.
   A direct label and changed output cannot substitute for exact source-shaped
   behavior. Thus defaults, enums, numeric boundaries, width-dependent packet
   values, and sentinels are not all authoritatively covered.

8. **Changes required — v1 bytes bind to a placeholder executable identity.**
   All 12 vectors now have correct root fields, sample/time numerators,
   denominators equal to 1,152,000, tag shapes, canonical base64, compact
   sorted UTF-8 bytes, and exactly one LF. However every decoder identity uses
   `file_set_sha256` equal to 64 zeroes; neither provenance nor another B1
   artifact freezes the actual ordered path/NUL/file-digest manifest hash.
   Moreover the vectors label the decoder `uart` while using generic output IDs
   inconsistent with UART registration order (UART is Python 0, binary 1,
   annotation 2 and has no metadata registration). Literal bytes for an
   internally misbound object are not authoritative R9/R17/R18 goldens.

9. **Pass as a static cap specification, contingent on fixture correction.**
   All 17 required categories have positive finite integer values, units,
   domains, exact accept/value-plus-one reject boundaries, structured
   operation/basis/multiplier/floor/result fields, and arithmetic that
   recomputes. Cross-cap relationships such as stderr eight times diagnostic
   are explicit, and the fixed deadline/grace policy basis is stated. The
   record correctly disclaims macOS observation, executable enforcement,
   product-threshold status, and operator approval. Because several bases are
   computed from the invalid semantic corpus, a corrected corpus must rebuild
   and reverify all dependent values; this local cap-schema pass cannot transfer
   to that future candidate.

10. **Pass — five edge decisions are explicitly stated, but not demonstrated
    by the protocol corpus.** The standalone vectors cover first/later empty
    wait, sample-zero/skip zero and positive skip, simultaneous matches,
    half-open capture-count endpoints, and EOI preservation. Findings 2, 4-6
    show that the actual decoder-specific timelines do not consistently apply
    those decisions, so R2/R3 and stopping condition 2 remain unsatisfied.

## Discrepancies, deferrals, scope, and approval

Findings 2-8 are candidate defects requiring a new immutable fixture candidate
and fresh verification; no pass transfers. Project/legal disposition, runner
and cap enforcement, snapshot characterization, raw observations, threshold
proposal/review, operator approval, and later B1 gates remain deferred. I did
not repair the candidate or edit tests, prior records, contracts, progress,
product, runner/method/probe/enforcement/raw, schema/validator/manifest,
decoder, package/lock/workflow, Cycle 1/2, browser, firmware, hardware, C#, or
Cycle 4 paths.

- Approval need: none.

changes_required
