# C3-B1 semantic-fixture verification — round 7

## Identity and immutable subject

- Verifier identity/role: `c3-b1-semantic-fixture-verifier-1`
  (`/root/c3_b1_fixture_verify`), independent semantic-fixture verifier.
- Exact candidate owner: `c3-b1-semantic-fixture-implementor-replacement-6`;
  prior fixture authorship and failed candidates remain immutable history.
- Distinct fixture acceptance identity:
  `c3-b1-semantic-fixture-acceptance-1`.
- Distinct pre-execution runner implementor/verifier/acceptance identities:
  `c3-b1-pre-execution-runner-implementor-1`,
  `c3-b1-pre-execution-runner-verifier-1`, and
  `c3-b1-pre-execution-runner-acceptance-1`.
- Governing commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Tested candidate commit/tree: `6dfe8afae6b121902ce3fde4fe81d335581e6292` /
  `fc020d74e24646fc022f342dda8dafc72c929890`.
- Verification UTC: `2026-08-27T01:34:34Z`.
- Descendant qualification: verification began at HEAD
  `801a2932e66d17b8f6d9a23319e5edfb92e25b5f`, tree
  `fb17a29788a58931addeb0fc8e6c1a88b1473dad`, branch `python-rewrite`, with
  a clean worktree. Candidate-path `git diff 6dfe8af..HEAD` was empty. HEAD
  adds only the immutable round-7 assignment progress after the candidate;
  this record is descendant evidence and does not alter the candidate.

## Authority, method, and prohibited execution

No prior pass transferred. I freshly inspected the governing goal,
orchestration and B1 batch contracts, normative discovery Step 5 and stopping
conditions, the current assignment, all prior records as historical leads
only, the complete candidate diff, and exact checked-in UART/SPI/I2C, shim,
initializer, and helper source. Expectations were derived from static source,
literal timelines, and independent arithmetic rather than candidate claims or
runtime output.

No decoder, host, helper runtime, approved snapshot, C#, .NET, pythonnet,
libsigrokdecode, `sigrok-cli`, external/reference runtime, hardware, network,
installation, server, or browser was imported or executed. No executable cap
enforcement is present or claimed.

## Environment and exact commands

- macOS 15.7.7 (24G720); Python 3.12.13 from `.venv/bin/python`.
- `rtk git rev-parse HEAD HEAD^{tree} 6dfe8af...
  6dfe8af...^{tree}` — exit 0; identities above.
- `rtk git status --short` and candidate-path `rtk git diff --name-status
  6dfe8af..HEAD -- <candidate paths>` — exit 0, empty.
- `rtk git show --stat --format=fuller 6dfe8af...` and exact eight-path
  candidate diff inspection — exit 0. Candidate scope is fixture prose,
  generator, five regenerated JSON artifacts/manifest, and the implementation
  fixture test only; no product/runner/governance path changed.
- `rtk .venv/bin/python -m pytest -q
  tests/verification/test_c3_b1_semantic_fixture_candidate.py
  tests/implementation/test_cycle3_fixtures.py` — exit 0, `17 passed`, no
  skips. Passing tests do not resolve finding 5.
- `rtk .venv/bin/python scripts/generate_cycle3_fixtures.py --check` — exit 0.
- `rtk .venv/bin/python -m ruff check scripts/generate_cycle3_fixtures.py
  tests/implementation/test_cycle3_fixtures.py
  tests/verification/test_c3_b1_semantic_fixture_candidate.py` — exit 0,
  `All checks passed!`.
- Independent static earliest-event evaluator over all 63 unique timelines —
  exit 0; every transition, `r/f/e/h/skip` predicate, earliest return,
  simultaneous `matched`, pin vector, terminal failed wait, finite EOI,
  capture/trigger bound, record coordinate, output ID, time, and emission index
  passed.
- Independent literal UART/SPI/I2C state/output audit — diagnostic exit 0;
  complete values/order/classes/tags/directions and the two prior arithmetic
  recurrences passed.
- Independent 165-row matrix/context audit — exit 0; all row IDs and semantic
  identities were unique; 62 direct and 103 unsupported rows were present.
  All ten accepted delimiter maxima and thirty contextual rejections used real
  keys and exact selected-width context.
- Independent static AST import audit over all nine files — exit 0; the exact
  four relative initializer edges, including helper `.mod`, and all frozen
  local/stdlib imports matched provenance.
- Independent static AST declaration comparison — diagnostic exit 0; binary
  and SPI/I2C annotation declarations matched, but two UART annotation
  descriptions differed (finding 5).
- Independent SHA-256, manifest, and ordered path/NUL/file-digest
  recomputation — exit 0; all recorded bytes matched.
- Independent v1 root/type/output/time/base64/canonical-byte audit over all 12
  objects — diagnostic exit 0 for shape and bytes; exact UART declaration
  semantics fail finding 5.
- Independent 17-cap corpus-basis/operation/multiplier/floor/result/boundary
  recomputation — exit 0; exact values below.
- Static generator AST/no-oracle and scoped prohibited-runtime/enforcement/
  excluded-action search — exit 0. The only test subprocess invokes the inert
  deterministic generator.
- `rtk git diff --check` — exit 0. No required check was skipped.

## Exact candidate digests

| Artifact | SHA-256 |
| --- | --- |
| generator | `26ebad2b60b5cf8122b1f522f691e13054d29fad9ee6c84435ce0b6891143089` |
| `provenance.json` | `e0a6082869cdf51e7abf74441065b080b8e1d6614a45ad52f034ef95f4f4c8e4` |
| `semantic-fixtures.json` | `193e014301780a133aee4fe962bae124727906873d7b962b765f099801db3589` |
| `option-matrix.json` | `5d84b9d9855e9e2e75d45d5cd9560fbcfd1ac6ff88abfcf1c1326d3427ffc209` |
| `typed-vectors.json` | `675712484400c7f0461df2c46d3bb250ebbcaa2cf9af8f7fa3b66435d72881c2` |
| `experiment-caps.json` | `0936f9f0a1d6ce27ef518b47b4e72c7cbe554e6e0004dfed53f54d351457cef0` |
| `manifest.json` | `87559f3ccb3cb94fb068c8fd1653b9be71fad40617fe9b19edd61cd8b1ff00fe` |
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
The file-set algorithm reproduces UART
`eb9ee54a167e01c1a40830804912c18f8ebe700e41d9b1ee27707afd4c50d3f3`,
SPI `96bbaf9f3325196e9a4cea856194355a1b788022ed7457781371cdd4de38c193`,
and I2C `dd85b78a9d016cea24e69509eeb6a40fb8552e31af08e948fb750d9e03b216ae`.

## Independently recomputed cap values

Corpus bases are canonical semantic-fixture bytes `723860`, maximum capture
`372`, maximum records `34`, largest record bytes `1509`, and maximum tagged
depth `5`. The exact 17 values are:

| Cap | Value |
| --- | ---: |
| `wall_deadline_ms` | 5000 |
| `terminate_grace_ms` | 250 |
| `input_samples` | 100000 |
| `request_bytes` | 46327040 |
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
| `retained_result_bytes` | 185308160 |
| `recursion_limit` | 320 |
| `worker_address_space_bytes` | 2964930560 |

Every value is a positive finite integer with an exact unit/domain,
accept-at-value/reject-at-value-plus-one boundary, structured operation and
rationale, conservative multiplier/floor, and consistent cross-cap reference.
The file expressly disclaims runtime observation, enforcement, operator
approval, and product-threshold status.

## Numbered findings and dispositions

1. **Pass — provenance, imports, notices, identities, and deterministic
   rebuild.** Import commit `407b5ef039aa0474c400c0721749baa126e53270`,
   prior gitlink `0235970293590f673a253950e6c61017cefa97df`, every file and
   file-set hash, manifest entry, and notice observation match. The relative
   imports are UART/SPI/I2C `.pd` and helper `.mod`; local helper/shim and exact
   stdlib symbols close the AST graph. The shim has no observed in-file notice;
   the other eight files retain GPLv2-or-later notices. Project/legal review is
   correctly pending with no distribution or legal conclusion.

2. **Pass — all 63 timelines are genuine finite source transcriptions.** The
   five edge decisions, integer `0xFF` optional pins, RX/TX and MISO/MOSI/CS
   directions, complete waits and earliest matches, transitions, sample-zero,
   skips, simultaneous conditions, half-open endpoints, sample-count EOI, and
   prior emissions all agree internally. UART includes correct ordinary bit
   lists, zero BREAK data, annotation-only packet, errors, idle, 5-9-bit and
   packet traffic. SPI includes initial no-CS Python output, newest-first BITS
   ending 170/180, binary/DATA/annotations/metadata, word-one, CS transfer, and
   partial EOI. I2C includes ordinary reversed BITS, address/data binary and
   annotations, ACK/NACK, genuine repeated START, STOP, partial EOI, and exact
   bitrate `int(1_152_000 * 17 / 371) = 52787`.

3. **Pass — the 165-row option matrix is closed and truthful.** All defaults,
   enums, numeric bounds, types, sentinels, unknowns, duplicates, and SPI
   preapproval limit are classified with unique IDs and semantic keys. There
   are 62 direct witnesses and 103 unsupported rows, with no generic
   equivalences. RX/TX delimiter maxima 31/63/127/255/511 use the real option
   key and selected widths 5-9; direct fixtures independently materialize the
   width, direction, all-one bit list, scalar, canonical binary bytes, packet
   annotation, waits, records, and coordinates. Max-plus-one, `-2`, and string
   rejection rows retain the same real key and width context.

4. **Pass — cap specification, generator independence, and exclusions.** All
   17 caps and boundaries recompute as listed. The generator imports only
   stdlib static-data modules, rebuilds byte-identically, and contains no
   decoder/host/reference oracle, dynamic import, enforcement, or product
   runner. Candidate scope contains no prohibited dependency/action, runtime,
   product/runner change, browser/hardware/firmware work, package publication,
   unsupported-platform claim, or Cycle 4 expansion.

5. **Changes required — UART annotation declarations are not exact checked-in
   source.** Static AST comparison of `Software/decoders/uart/pd.py` lines
   141-142 finds descriptions `RX parity error bit` and `TX parity error bit`.
   Generator lines 339-340 instead freeze `RX parity error` and
   `TX parity error`, omitting ` bit`. This mismatch appears in the declaration
   arrays of all 54 UART timelines and all 10 UART-bound v1 objects/canonical
   goldens. IDs, indices, rows, output IDs, and record classes remain correct,
   but the normative v1 declaration description is a promised semantic field;
   byte-repeatability of the wrong object cannot make it authoritative. R2/R9
   and stopping condition 2 remain open, and existing focused tests do not
   compare declaration text to static source.

6. **Pass with finding 5 qualification — v1 schema mechanics and bytes.** All
   12 objects otherwise have exact roots, materialized defaults, canonical
   mappings, actual output IDs, record kinds, nine Python tags, padded base64,
   integral coordinates, rational times, real file-set identities, and compact
   sorted UTF-8 plus one LF. Every checked-in golden byte string independently
   reproduces its object, but the ten UART objects inherit finding 5 and cannot
   yet serve as exact source-bound R9/R17/R18 authority.

## Discrepancies, deferrals, scope, and approval

Finding 5 requires a corrected immutable semantic-fixture candidate and full
fresh verification; no local or prior pass transfers. Project/legal
disposition, pre-execution runner/enforcement, decoder characterization, raw
observations, threshold proposal/review, operator approval, and later B1 gates
remain deferred in their governing order. I did not repair candidate data,
generator, tests, docs, declarations, or goldens, and did not edit the
corrected verifier, prior records, contracts, progress, product,
runner/method/probe/enforcement/raw, schema/validator/evidence manifests,
decoder, package/lock/workflow, Cycle 1/2 evidence, browser, firmware,
hardware, C#, or Cycle 4 paths.

- Discrepancy: two UART annotation descriptions omit source-required ` bit`.
- Approval needed: none.

changes_required
