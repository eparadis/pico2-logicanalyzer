# C3-B1 semantic-fixture verification — round 8

## Identity and immutable subject

- Verifier identity/role: `c3-b1-semantic-fixture-verifier-1`
  (`/root/c3_b1_fixture_verify`), independent semantic-fixture verifier.
- Exact candidate owner: `c3-b1-semantic-fixture-implementor-replacement-6`;
  prior fixture authorship, candidates, and verdicts remain immutable history.
- Distinct fixture acceptance identity:
  `c3-b1-semantic-fixture-acceptance-1`.
- Distinct pre-execution runner implementor/verifier/acceptance identities:
  `c3-b1-pre-execution-runner-implementor-1`,
  `c3-b1-pre-execution-runner-verifier-1`, and
  `c3-b1-pre-execution-runner-acceptance-1`.
- Governing commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Tested candidate commit/tree: `c1420ad9b4309fc7417acbc228085b68237c24d0` /
  `26ef344bfb76bec4a8e68be06a411b4d27d20de1`.
- Verification UTC: `2026-08-27T01:52:51Z`.
- Descendant qualification: verification began at HEAD
  `99ee255856cb2fddcc6c96645a46ab5def4b9f67`, tree
  `cd68714b8188c3c0da9bf76178d72bcd3df5928c`, branch `python-rewrite`,
  with a clean worktree. `git diff c1420ad..HEAD` names only
  `Software/LogicAnalyzerPy/docs/cycle-3-orchestration-progress.md`; an exact
  candidate-path quiet diff passed. This new record is descendant evidence
  and cannot change the tested identity.

## Authority, method, and prohibited execution

No prior pass transferred. I freshly inspected the governing goal,
orchestration and B1 batch contracts, normative discovery option/output
contract, current round-8 assignment, prior immutable records as historical
leads only, the exact candidate commit/diff, and the complete checked-in UART,
SPI, I2C, shim, initializer, and helper source as inert text. Expectations came
from those approved contracts, static ASTs, literal state transitions, and
independent integer/canonical-byte calculations—not candidate assertions or
runtime output.

No decoder, host, helper runtime, approved snapshot, C#, .NET, pythonnet,
libsigrokdecode, `sigrok-cli`, external/reference runtime, hardware, network,
installation, server, or browser was imported or executed. No executable cap
enforcement is present or claimed.

## Environment and exact commands

- macOS 15.7.7 (24G720), Darwin 24.6.0 x86_64; Python 3.12.13 from
  `.venv/bin/python`; pytest 8.3.4; Ruff 0.9.10.
- `rtk git rev-parse HEAD 'HEAD^{tree}' c1420ad...
  'c1420ad...^{tree}'`, `rtk git status --short`, `rtk git show --stat
  --oneline --no-renames c1420ad...`, and `rtk git diff --name-status
  c1420ad..HEAD` — exit 0; identities and descendant qualification above.
- `rtk git diff c1420ad^ c1420ad -- <generator and implementation test>` and
  `rtk git show c1420ad:testdata/.../experiment-caps.json` — exit 0; exact
  source correction and dependent static rebuild inspected. The candidate
  commit changes only generator, three dependent JSON artifacts plus manifest, and
  the implementation fixture test; it changes no product, runner, governance,
  decoder, dependency, or workflow path.
- `rtk .venv/bin/python -m pytest -q
  tests/verification/test_c3_b1_semantic_fixture_candidate.py
  tests/implementation/test_cycle3_fixtures.py` — exit 0, `18 passed in
  0.50s`, no skips. The implementation test's only subprocess runs the inert
  fixture generator and leaves byte-identical artifacts.
- `rtk .venv/bin/python scripts/generate_cycle3_fixtures.py --check` — exit 0.
- `rtk .venv/bin/ruff check scripts/generate_cycle3_fixtures.py
  tests/implementation/test_cycle3_fixtures.py
  tests/verification/test_c3_b1_semantic_fixture_candidate.py` — exit 0,
  `All checks passed!`.
- `rtk git diff --check c1420ad^ c1420ad` — exit 0.
- Independent static source-declaration AST evaluator — exit 0. It compared
  every annotation ID/description/index, row ID/description/index/member,
  binary ID/description/index, and metadata output/type/name/description:
  UART `18/10/3/0`, SPI `7/7/2/1`, and I2C `11/3/4/1`. All 54 UART, six SPI,
  and three I2C timeline declarations and all 12 v1 roots matched source.
- Independent finite timeline evaluator — exit 0: 63 unique timelines, 1,058
  waits, and 1,049 records. It checked every transition, trigger, earliest
  `r/f/e/h/skip` truth, simultaneous match vector, returned pin, terminal
  failed wait, EOI bound, record coordinate, output ID, rational time, and
  emission index; maximum sample count was 372.
- Independent source-order/value audit of UART/SPI/I2C core and direct cases —
  exit 0. It statically followed source call shapes and state order, including
  UART integral centers and packet/error/BREAK/IDLE behavior, SPI initial
  no-CS output plus newest-first `insert(0)` BITS recurrence, and I2C
  address/data/ACK/NACK/repeated-START/STOP and `pdu_bits` arithmetic.
- Independent option/source-context audit — exit 0: 165 unique rows, 62 direct
  and 103 unsupported, 40 contextual delimiter rows, 57 distinct direct
  witnesses, and no generic equivalence. Every accepted source/default/domain
  representative and every required type/boundary/sentinel/unknown/duplicate
  rejection matched the approved option contract.
- Independent nine-file AST import, byte digest, per-file notice, ordered
  file-set, and manifest recomputation — exit 0. The exact four relative
  initializer edges, including helper `.mod`, local imports, and stdlib symbol
  imports matched provenance.
- Independent v1 audit — exit 0: all 12 roots, fully materialized source
  defaults, decoder file-set identities, declarations, mappings, capture
  bounds, actual output IDs, four record kinds, nine Python tags, base64,
  coordinates, rational times, and compact sorted UTF-8 plus LF bytes matched.
- Independent cap audit — exit 0: all 17 schemas, bases, structured operations,
  multipliers, floors, cross-cap references, units, domains, rationales, and
  accept/reject boundaries recomputed to the values below.
- Static generator AST and scoped prohibited-runtime/oracle/enforcement scan —
  exit 0. Generator imports are exactly `__future__`, `argparse`, `copy`,
  `hashlib`, `json`, and `pathlib`; no dynamic import, oracle, decoder/host
  execution, or enforcement path exists.
- `rtk git diff --quiet c1420ad..HEAD -- <all candidate paths>`, candidate
  descendant name-only diff, and final status/diff checks — exit 0; candidate
  paths are unchanged. No required check was skipped.

## Exact candidate digests

| Artifact | SHA-256 |
| --- | --- |
| generator | `2fc53874e8f9539f37850da45a09e9d740f7997ee41a9435ba2f17b41ce4f800` |
| provenance/license document | `3155b8ea00e54fc8facd86d6a28604e9a0f3cf1097751392e6a12380ad9ddc4c` |
| semantic-fixture document | `a78e3a6675427e6ddc650de624ed492d18901d90e35353bce6f5645c0207240d` |
| `provenance.json` | `e0a6082869cdf51e7abf74441065b080b8e1d6614a45ad52f034ef95f4f4c8e4` |
| `semantic-fixtures.json` | `8da1d2aa2256cce5c56ac2df4a629d90a95c21cb84d633522780394439888e64` |
| `option-matrix.json` | `5d84b9d9855e9e2e75d45d5cd9560fbcfd1ac6ff88abfcf1c1326d3427ffc209` |
| `typed-vectors.json` | `b5cc317ff476fcb2446eaf6b376c346210f63fbca8d0df84984b7990a528ffbf` |
| `experiment-caps.json` | `fc5f3b0de17ae9f74b363ee5d4847ea2f9a88b9e0918cba8e848305ebbda05a1` |
| `manifest.json` | `6a5b26f73ff3ae5e4ec64962acc43d08d52dbf8b7ab2e574b976ceab5d8f9a43` |
| implementation fixture test | `6349a196381e7672b7a21cf73498ec8df9dd9309a69d5c89e947463f4748c857` |
| immutable corrected verifier | `e7081c043c790223d07b76724d6b5f73cca6c1d185635b0ad18f591bbd7a5cf9` |

The unchanged source digests independently recompute as shim
`385124002ec16379a2542f2905c5ce41f3402032458d89f49617623ab7aaf01a`;
UART initializer/decoder
`351098a23f5caa205068688550af53bd44a63776e1d02921ba32487ce720b92f` /
`67655f53162c531bc6eb77d9d29b384edec80a2dd5bd741897b4aa2afc52ffcc`;
SPI initializer/decoder
`91b207f82c59fe1c12ad1458ef669c4293c7e4c8dd19bec14e78b455305af56c` /
`ef9cac5098404dc164094712e9175ba3715233248d8bbc23cb85ed3fc51d5d3d`;
I2C initializer/decoder
`37931874732ea0b3ca13784b8df4cd90949a2c1b5822feae5d5df6da81ee886f` /
`b6899137fb5b505433e696d319b7f3cc88519b43e2a2e7fea1a9f770ba10a305`;
and helper initializer/implementation
`125b0616dfdd974c2f6e0e83e61cf9cdd21340f9ab11ac7b97b648792dad05d1` /
`602b27901820a27af5fcf317b34af1a17d1449fa1ad21279507d1d5ab8acebd6`.
The ordered UTF-8 `path + NUL + lowercase source digest + LF` algorithm
reproduces UART
`eb9ee54a167e01c1a40830804912c18f8ebe700e41d9b1ee27707afd4c50d3f3`,
SPI `96bbaf9f3325196e9a4cea856194355a1b788022ed7457781371cdd4de38c193`,
and I2C `dd85b78a9d016cea24e69509eeb6a40fb8552e31af08e948fb750d9e03b216ae`.

## Independently recomputed cap values

Corpus bases are canonical semantic-fixture bytes `724292`, maximum capture
`372`, maximum records `34`, largest record bytes `1509`, maximum tagged depth
`5`, and scheduling-policy quantum `50` milliseconds.

| Cap | Value |
| --- | ---: |
| `wall_deadline_ms` | 5000 |
| `terminate_grace_ms` | 250 |
| `input_samples` | 100000 |
| `request_bytes` | 46354688 |
| `output_records` | 69632 |
| `encoded_bytes` | 6180864 |
| `decoded_bytes` | 6180864 |
| `stdout_bytes` | 193152 |
| `stderr_bytes` | 96576 |
| `diagnostic_bytes` | 12072 |
| `text_bytes` | 3090432 |
| `binary_bytes` | 3090432 |
| `nested_depth` | 40 |
| `nested_items` | 69632 |
| `retained_result_bytes` | 185418752 |
| `recursion_limit` | 320 |
| `worker_address_space_bytes` | 2966700032 |

Every cap is a positive finite integer with exact unit/domain,
accept-at-value/reject-at-value-plus-one boundary, structured operation,
source basis, multiplier/floor, and value-specific rationale. `stderr_bytes`
correctly references the computed diagnostic cap. The file expressly disclaims
runtime observation, enforcement, operator approval, and product-threshold
status.

## Numbered findings and dispositions

1. **Pass — exact candidate, scope, independence, and deterministic rebuild.**
   Candidate/tree and descendant qualification are exact; candidate paths are
   unchanged. Generated bytes reproduce deterministically and manifest hashes
   bind all five generated inputs plus generator. The verifier authored only
   this descendant record and did not repair candidate or immutable tests.

2. **Pass — provenance, imports, notices, and file sets.** Import commit
   `407b5ef039aa0474c400c0721749baa126e53270`, prior gitlink
   `0235970293590f673a253950e6c61017cefa97df`, all nine bytes/digests, the
   UART/SPI/I2C `.pd` and helper `.mod` relative edges, local helper/shim, exact
   stdlib symbols, and three file-set hashes match. The shim has no observed
   in-file notice; the other eight sources retain GPLv2-or-later notices.
   Project/legal disposition remains correctly pending without a legal or
   distribution conclusion.

3. **Pass — all declaration metadata is source exact.** Static AST comparison
   covers every field, not only the two repaired strings. UART registration is
   Python 0, binary 1, annotation 2; SPI/I2C registration is Python 0,
   annotation 1, binary 2, metadata 3. Source annotation, row, binary, and
   metadata order/IDs/descriptions/members/types all match every applicable
   timeline and v1 object. In particular, source and generator lines 141-142 /
   339-340 now both say `RX parity error bit` and `TX parity error bit`.

4. **Pass — all 63 timelines are genuine finite source transcriptions.** The
   five API-edge decisions, exact integer `0xFF` optional pins, directions,
   transitions, earliest waits, skip/edge predicates, all simultaneous
   matches, pins, half-open coordinates, output IDs, record order, and EOI
   suppression/preservation are internally and source consistent. Every
   terminal failed wait is at its exact sample count and no predicate matches
   an earlier remaining real sample. UART integral timing and complete
   DATA/error/parity/stop/frame/annotation-only-packet/BREAK/IDLE records pass.
   SPI no-CS `CS-CHANGE` precedes waits/output, BITS are newest-first with
   final spans 170/180, and binary/Python/annotation/metadata/CS transfer order
   passes. I2C includes reversed ordinary-list BITS, complete address/data,
   ACK/NACK, genuine repeated START, STOP, partial EOI, and bitrate
   `int(1_152_000 * 17 / 371) = 52787`.

5. **Pass — all 165 option rows and direct witnesses are closed.** Exact
   checked-in defaults/enums and contract numeric domains yield the 62 direct
   rows; 103 unsupported rows cover exclusive bounds, invalid types,
   sentinels, unknown keys, duplicate CLI assignments, and SPI's unapproved
   beyond-default width. All accepted rows name truthful finite witnesses; no
   generic static equivalence remains. RX/TX delimiter maxima
   31/63/127/255/511 and max-plus-one/`-2`/string rejections retain the real
   option key and selected widths 5-9. Each direct delimiter fixture binds
   direction, width, all-one input bits, scalar, binary bytes, packet
   annotation, waits, values, order, and coordinates.

6. **Pass — all 12 v1 objects and literal CLI bytes are authoritative.** The
   objects cover all four record kinds and all nine Python value tags, with
   source-exact declarations (including the corrected UART descriptions),
   source defaults, real file-set IDs, mappings, output IDs, values, times,
   and canonical UTF-8 bytes. Each literal golden independently equals compact
   sorted JSON plus exactly one LF; no runtime supplied or corroborated it.

7. **Pass — all 17 finite experiment caps are complete and non-enforcing.**
   The new 724292-byte corpus and every other basis independently reproduce
   the table. Structured arithmetic, floors, related-cap references, units,
   domains, exact boundaries, and rationales are consistent. These values are
   static pre-execution envelopes only; enforcement belongs to the separately
   owned runner candidate.

8. **Pass — no oracle, executable enforcement, or excluded expansion.** The
   generator and verification route are static data processing only. Candidate
   scope contains no decoder/host/reference execution, dynamic import,
   product/runner/method/probe/enforcement/raw path, prohibited dependency,
   package/lock/workflow change, browser/hardware/firmware action,
   distribution, unsupported-platform claim, or Cycle 4 work.

## Discrepancies, deferrals, scope, and approval

- Discrepancies: none.
- Deferrals: project/legal disposition, pre-execution runner implementation
  and enforcement, decoder characterization, raw observations, threshold
  proposal/review, explicit operator numeric approval, and subsequent B1 gates
  remain deferred in their contract order. This verdict does not approve or
  predict them.
- Prohibited-path audit: no candidate, verifier-test, prior-record, contract,
  progress, product, runner/method/probe/enforcement/raw, schema/validator,
  manifest, decoder, package/lock/workflow, Cycle 1/2 evidence, browser,
  firmware, hardware, C#, or Cycle 4 path was edited by this verifier.
- Approval needed: none.

pass
