# C3-B1 semantic-fixture verification — round 5

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
- Tested candidate commit/tree: `38276fcd8878da84c5e2b7f30e4de275f88a91b6` /
  `ca5b3e6489f3f0285c60e4374911ca4b2b1b39a1`.
- Verification UTC: `2026-08-27T01:03:25Z`.
- Descendant qualification: verification began at HEAD
  `73b995f27baad2d5054c8221fe5b688126ca7f1d`, tree
  `59d1a7afb9a7273f85df4fcbd07d2b649fe4f04c`, branch `python-rewrite`, with a
  clean worktree. Candidate-path `git diff 38276fc..HEAD` was empty. The only
  verifier changes are the expressly authorized two stale assertion updates
  and this new record; both are descendant evidence and do not alter the exact
  candidate identity.

## Authority, method, and prohibited execution

No prior result transferred. I re-read `RTK.md`, `SUBAGENT_POLICY.md`, the
approved Cycle 3 goal/orchestration/batch B1 gate, normative discovery Step 5,
all prior immutable verification records, the complete governing-to-candidate
diff, and the exact checked-in UART/SPI/I2C source. Expectations were derived
independently from static source and inert checked-in data, never from candidate
claims or decoder/runtime output.

No decoder, host, helper/shim, C#, .NET, pythonnet, libsigrokdecode,
`sigrok-cli`, external/reference runtime, hardware, network, installation,
server, or browser was imported or executed. No approved decoder snapshot ran.
No executable cap enforcement is present or claimed.

## Source-adjudicated verifier correction

Before auditing the candidate I corrected exactly two stale assertions in
`tests/verification/test_c3_b1_semantic_fixture_candidate.py`, as authorized:

- Before SHA-256:
  `5deaf1c8413d17466027d48b6e7073ba914654cf078acb20376080c4625009a9`.
- After SHA-256:
  `e7081c043c790223d07b76724d6b5f73cca6c1d185635b0ad18f591bbd7a5cf9`.
- SPI source lines 316-342 establish that absent CS, line 328 emits Python
  `['CS-CHANGE', None, None]` at `(0,0)` before the first `wait({})` and hence
  before binary/BITS/DATA output. The test now requires that exact prefix.
- UART source lines 288-310 establish that `handle_packet()` ends by invoking
  annotation helper `putx_packet()` and never emits a Python `PACKET` command.
  The test now rejects Python PACKET and requires annotation class 16.

No other verifier assertion changed. The candidate itself was not repaired.

## Environment and exact commands

- macOS 15.7.7 (24G720); Python 3.12.13 from `.venv/bin/python`.
- `rtk git rev-parse HEAD HEAD^{tree} 38276fc...
  38276fc...^{tree}` — exit 0; identities above.
- `rtk git status --short` and candidate-path `rtk git diff --name-status
  38276fc..HEAD` — exit 0; initially clean and candidate paths unchanged.
- `rtk .venv/bin/python -m pytest -q
  tests/verification/test_c3_b1_semantic_fixture_candidate.py
  tests/implementation/test_cycle3_fixtures.py` — exit 0, `17 passed`, no
  skips.
- `rtk .venv/bin/python scripts/generate_cycle3_fixtures.py --check` — exit 0.
- `rtk .venv/bin/python -m ruff check scripts/generate_cycle3_fixtures.py
  tests/implementation/test_cycle3_fixtures.py
  tests/verification/test_c3_b1_semantic_fixture_candidate.py` — exit 0.
- Independent static earliest-event evaluator over every timeline — exit 0;
  all transitions, wait alternatives, conditions, skips, edges, simultaneous
  `matched`, pin vectors, terminal waits, capture bounds, and EOI positions were
  internally consistent.
- Independent literal source-order/recurrence audit of every UART/SPI/I2C
  record and all matrix witnesses — diagnostic exit 0; findings below.
- Independent option matrix closure audit — diagnostic exit 0; 159 unique rows,
  56 accepted direct witnesses and 103 explicit unsupported rows.
- Independent v1 root/schema/type/time/base64/canonical-byte/declaration/file-
  set audit over all 12 vectors — diagnostic exit 0.
- Independent cap-schema and structured arithmetic recomputation over all 17
  entries — diagnostic exit 0; exact values, units, domains, operations,
  boundaries, margins, and cross-cap relationships recomputed.
- Independent `git show` SHA-256 recomputation for the generator, six fixture
  artifacts, and every closed-inventory decoder source file — exit 0.
- Static AST import/no-oracle and scoped prohibited-runtime/enforcement audit —
  exit 0.
- `rtk git diff --check` — exit 0. No required check was skipped.

## Artifact digests

| Exact candidate artifact | SHA-256 |
| --- | --- |
| generator | `77cd8e9cc5ab33aecf3c4a3e74f3044234bf78dec5831a5586f36b64f342ee8f` |
| `provenance.json` | `7b418d6fa8a188721ebcb3254f6eeff0b4867a0c63968a8db7c26a6b3ffb870e` |
| `semantic-fixtures.json` | `08467b770937d3636181f36912e2e5a0a71e6abf41b0f1240fb8b32e9555693d` |
| `option-matrix.json` | `0d36c7e8b1b7563b7a6de8a6b278324428ab96dbd3ae8896df8c6b179dbadf68` |
| `typed-vectors.json` | `675712484400c7f0461df2c46d3bb250ebbcaa2cf9af8f7fa3b66435d72881c2` |
| `experiment-caps.json` | `4a0e3289cf9a0e7f02d568965c96b26fbba5e77befa727d017c7042bd9dc9bb1` |
| `manifest.json` | `d0450773807ba12d6344d2fd380260dfaa73e8b486785f4bdde3621ee837775f` |

All closed-inventory source hashes, relative/local/stdlib imports, import
commit, prior gitlink, per-file notice observations, and pending project/legal
disposition match the approved static inventory. The manifest's file-set hash
algorithm and every artifact/source digest independently recompute.

## Numbered findings and dispositions

1. **Pass — provenance, notices, declarations, sentinels, and deterministic
   rebuild.** Decoder metadata, registration order, output IDs, classes, and
   tags match exact static source. Optional-channel vectors use integer `0xFF`
   and matching `has_channel` declarations. Imports are closed and stdlib-only
   outside the recorded local decoder graph. The generator rebuild is byte
   stable and contains no executable oracle, decoder import, or enforcement.

2. **Pass — the rewritten wait schedules satisfy earliest-event semantics.**
   A fresh evaluator searched from the next eligible sample after every return
   and independently checked every predicate shape, edge/level/skip alternative,
   simultaneous match vector, returned pin vector, transition, terminal empty
   wait, finite `sample_count=256` boundary, and EOI. All named UART/SPI/I2C
   fixtures and generated direct witnesses now retain intervening events and
   justify every record before the finite end.

3. **Changes required — the BREAK fixture's nested UART DATA bits contradict
   its all-low signal and scalar outputs.** `uart-break-low-interval` keeps RX
   low throughout its complete frame. Its scalar Python DATA value is zero,
   binary bytes are `AA==`, and annotation text describes zero, but its nested
   DATA bit triples remain the copied A5 pattern `[1,0,1,0,0,1,0,1]`. UART
   `get_data_bits()` appends the sampled signal itself to each ordinary
   `[signal, ss, es]` entry, so this schedule requires eight zero-valued triples.
   The fixture is internally contradictory and cannot be an authoritative
   complete UART oracle.

4. **Pass — SPI call shape, directions, recurrence, ordering, and coordinates.**
   No-CS Python CS-CHANGE is present before the first wait/output. Static
   `handle_bit()` inserts each bit newest-first and derives the newest end from
   the immediately previous newest sample; literal simulation gives MOSI
   `[150,170]` and MISO `[160,180]`, not the earlier 290/300 interpretation.
   BITS contents, binary/Python DATA, annotations, CS changes, active level,
   MISO/MOSI direction/classes, partial-word behavior, spans, and source order
   now agree with source.

5. **Changes required — the full I2C bitrate omits a processed partial data
   bit.** The schedule deliberately returns an SCL rising data event at sample
   370 before STOP at 371. Source `handle_address_or_data()` increments
   `pdu_bits` immediately on entry (I2C lines 181-182), including that partial
   byte bit. The total is therefore 8 address bits + 8 completed data bits + 1
   partial bit = 17; ACK/NACK slots do not increment it. `handle_stop()` lines
   298-307 uses inclusive elapsed samples, so at samplerate 1,152,000 the exact
   value is `int(1_152_000 * 17 / 371) = 52787`. The candidate's `49681` and
   generator comment that only two octets count use 16 bits and contradict the
   actual source branch. Address/data/NACK/repeated START/STOP order and the
   remaining I2C records otherwise pass.

6. **Pass — edge decisions and typed v1 bytes.** The five API-edge decisions
   cover first/later empty waits, zero/positive skips, simultaneous conditions,
   half-open capture endpoints, and EOI preservation and are demonstrated by
   the protocol schedules. All 12 v1 objects have complete materialized
   defaults, exact declarations/output IDs/tags, integral rational times,
   canonical compact sorted UTF-8 bytes plus one LF, and independently decoded
   base64. Their decoder file-set identities are computed from the declared
   ordered path/NUL/file-digest algorithm rather than placeholders.

7. **Pass for matrix structure and option-specific reasoning, contingent on
   fixture correction.** All 159 row IDs are unique. The 56 accepted rows each
   link directly to a literal fixture option/value and a source-specific
   observable, covering defaults, enums, numeric boundaries, widths, types,
   sentinels, unknowns, and duplicate rejection behavior; the 103 unsupported
   rows have exact semantic rejection tuples. Static-equivalence links state
   option/value-specific source reasoning rather than generic equivalence.
   The shifted I2C direct witness nevertheless inherits finding 5's incorrect
   metadata, so exact whole-fixture authority cannot transfer.

8. **Pass as a complete static cap specification, contingent on fixture
   correction.** All 17 categories have finite positive values, exact units and
   domains, accept-at-value/reject-at-value-plus-one boundaries, structured
   arithmetic, margins and rationales that independently recompute, including
   cross-cap relationships. The file expressly disclaims enforcement,
   product-threshold status, runtime observation, and operator approval. Values
   derived from fixture maxima must be rebuilt after findings 3 and 5 are
   corrected; this pass does not transfer to a future corpus.

9. **Pass — no fabricated generic records or executable authority remain.**
   Expected records use decoder-specific declarations, class/direction/tag/value
   shapes and coordinates. UART packet output is annotation-only, SPI alone
   uses `spi-data`, I2C data-NACK and repeated START traffic are retained, and
   earlier BREAK-frame records are no longer discarded. The artifacts remain
   inert evidence, not a runtime oracle or enforcement mechanism.

## Discrepancies, deferrals, scope, and approval

Findings 3 and 5 are exact candidate defects requiring a new immutable fixture
candidate and fresh verification; no prior or local pass transfers. Project/
legal disposition, runner and cap enforcement, snapshot characterization, raw
observations, threshold proposal/review, operator approval, and later B1 gates
remain deferred. I did not repair candidate fixtures/generator/tests/docs or
edit prior records, contracts, progress, product, runner/method/probe/
enforcement/raw, schema/validator/manifests, decoder, package/lock/workflow,
Cycle 1/2 evidence, browser, firmware, hardware, C#, or Cycle 4 paths.

- Discrepancies: UART BREAK nested bits; full-I2C bitrate.
- Approval need: none.

changes_required
