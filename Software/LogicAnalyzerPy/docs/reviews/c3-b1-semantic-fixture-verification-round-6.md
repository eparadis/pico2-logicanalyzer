# C3-B1 semantic-fixture verification — round 6

## Identity and immutable subject

- Verifier identity/role: `c3-b1-semantic-fixture-verifier-1`
  (`/root/c3_b1_fixture_verify`), independent semantic-fixture verifier.
- Exact candidate owner: `c3-b1-semantic-fixture-implementor-replacement-6`;
  prior fixture implementor/replacement authorship remains preserved in the
  orchestration history and transfers no pass.
- Distinct fixture acceptance identity:
  `c3-b1-semantic-fixture-acceptance-1`.
- Distinct pre-execution runner implementor/verifier/acceptance identities:
  `c3-b1-pre-execution-runner-implementor-1`,
  `c3-b1-pre-execution-runner-verifier-1`, and
  `c3-b1-pre-execution-runner-acceptance-1`.
- Governing commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Tested candidate commit/tree: `9f0fe7e45cde49f69b22d266c36932407c3d4845` /
  `01c352da8e6d6807941e5a37434f02b53b973f20`.
- Verification UTC: `2026-08-27T01:19:54Z`.
- Descendant qualification: verification began at HEAD
  `03ece2e9adc57c95324e3bca1e5b03dfaecff822`, tree
  `ce127952324c39ca327778f97a2c207d9d48f93c`, branch `python-rewrite`, with
  a clean worktree. `git diff 9f0fe7e..HEAD -- <all fixture, generator,
  implementation-test, and corrected-verifier paths>` was empty. This record
  is descendant evidence and does not alter the tested candidate.

## Authority, provenance, and prohibited execution

No earlier finding or pass transferred. I re-read `RTK.md`,
`SUBAGENT_POLICY.md`, `CYCLE3_GOAL.md`, the governing orchestration and batch
B1 contracts, normative discovery Step 5 and the stopping conditions, the
current round-6 assignment, all five prior immutable records as historical
leads only, the complete candidate diff, and the checked-in UART/SPI/I2C,
shim, initializer, and helper source. Expectations came from those inert
sources and independent calculations, not candidate prose, implementation
tests, or runtime output.

No decoder, host/helper runner, approved snapshot, C#, .NET, pythonnet,
libsigrokdecode, `sigrok-cli`, external/reference runtime, hardware, network,
installation, server, or browser was imported or executed. Static reading of
the shim/helper/decoder files supplied no runtime output. No executable cap
enforcement is present or claimed.

## Environment and exact commands

- macOS 15.7.7 (24G720); Python 3.12.13 from `.venv/bin/python`.
- `rtk git rev-parse HEAD HEAD^{tree} 9f0fe7e...
  9f0fe7e...^{tree}` — exit 0; identities above.
- `rtk git status --short` and candidate-path `rtk git diff --name-status
  9f0fe7e..HEAD -- <candidate paths>` — exit 0, empty.
- `rtk git show --format=fuller --stat 9f0fe7e...` and exact four-path
  `rtk git show` — exit 0; the candidate changes only the generator,
  semantic fixture, fixture manifest, and implementation fixture test.
- `rtk .venv/bin/python -m pytest -q
  tests/verification/test_c3_b1_semantic_fixture_candidate.py
  tests/implementation/test_cycle3_fixtures.py` — exit 0, `17 passed`, no
  skips. The implementation test's generator rewrite remained byte-identical.
- `rtk .venv/bin/python scripts/generate_cycle3_fixtures.py --check` — exit 0.
- `rtk .venv/bin/python -m ruff check scripts/generate_cycle3_fixtures.py
  tests/implementation/test_cycle3_fixtures.py
  tests/verification/test_c3_b1_semantic_fixture_candidate.py` — exit 0,
  `All checks passed!`.
- Independent static earliest-event and finite-bound evaluator over all 57
  timelines — exit 0; it checked transition ordering, pin levels, every
  `r/f/e/h/skip` predicate, simultaneous `matched`, earliest return, terminal
  failed wait, trigger/capture bounds, EOI, output IDs, coordinates, time, and
  emission order.
- Independent literal UART/SPI/I2C source-state, recurrence, declaration, and
  complete-record audit — diagnostic exit 0; the round-5 defects are fixed and
  finding 2 records the result.
- Independent option matrix inventory over 159 rows — diagnostic exit 0; IDs
  and rejection tuples are unique, but six required accepted width maxima are
  absent (finding 4).
- Independent AST import inventory over all nine source files — diagnostic
  exit 0; it found the unlisted helper initializer `.mod` edge (finding 3).
- Independent SHA-256 and ordered path/NUL/file-digest recomputation — exit 0;
  all file, decoder-file-set, artifact, generator, and manifest hashes match.
- Independent v1 exact-root/type/declaration/output/time/base64/canonical-byte
  audit over all 12 vectors — diagnostic exit 0.
- Independent cap-basis and structured-arithmetic recomputation over all 17
  caps — diagnostic exit 0; corpus bytes `659426`, maximum capture `372`,
  maximum records `34`, largest record `1509` bytes, and maximum tagged depth
  `5` reproduce all values and boundaries.
- Scoped static AST/no-oracle and prohibited-runtime/enforcement search — exit
  0; the only subprocess use is the implementation test invoking the inert
  static generator.
- `rtk git diff --check` — exit 0. No required check was skipped.

## Exact candidate digests

| Artifact | SHA-256 |
| --- | --- |
| generator | `1626a28894ba3beecd9097db1e8e2b6b84bd23d4309cc620758ffca549e3b5c7` |
| `provenance.json` | `7b418d6fa8a188721ebcb3254f6eeff0b4867a0c63968a8db7c26a6b3ffb870e` |
| `semantic-fixtures.json` | `ecdb5bc841d81ac5c699f7debd771121e14f9ba853e3e43b57906d2220a90b57` |
| `option-matrix.json` | `0d36c7e8b1b7563b7a6de8a6b278324428ab96dbd3ae8896df8c6b179dbadf68` |
| `typed-vectors.json` | `675712484400c7f0461df2c46d3bb250ebbcaa2cf9af8f7fa3b66435d72881c2` |
| `experiment-caps.json` | `4a0e3289cf9a0e7f02d568965c96b26fbba5e77befa727d017c7042bd9dc9bb1` |
| `manifest.json` | `a5fae287af8fb31e06ff52d56075ea631cad6e900e49269e4383c88a2396ec39` |
| corrected immutable verifier | `e7081c043c790223d07b76724d6b5f73cca6c1d185635b0ad18f591bbd7a5cf9` |

The nine independently recomputed source hashes are: shim
`385124002ec16379a2542f2905c5ce41f3402032458d89f49617623ab7aaf01a`;
UART initializer `351098a23f5caa205068688550af53bd44a63776e1d02921ba32487ce720b92f`
and decoder `67655f53162c531bc6eb77d9d29b384edec80a2dd5bd741897b4aa2afc52ffcc`;
SPI initializer `91b207f82c59fe1c12ad1458ef669c4293c7e4c8dd19bec14e78b455305af56c`
and decoder `ef9cac5098404dc164094712e9175ba3715233248d8bbc23cb85ed3fc51d5d3d`;
I2C initializer `37931874732ea0b3ca13784b8df4cd90949a2c1b5822feae5d5df6da81ee886f`
and decoder `b6899137fb5b505433e696d319b7f3cc88519b43e2a2e7fea1a9f770ba10a305`;
helper initializer `125b0616dfdd974c2f6e0e83e61cf9cdd21340f9ab11ac7b97b648792dad05d1`;
and helper implementation
`602b27901820a27af5fcf317b34af1a17d1449fa1ad21279507d1d5ab8acebd6`.

The decoder file-set hashes independently reproduce as UART
`eb9ee54a167e01c1a40830804912c18f8ebe700e41d9b1ee27707afd4c50d3f3`,
SPI `96bbaf9f3325196e9a4cea856194355a1b788022ed7457781371cdd4de38c193`,
and I2C `dd85b78a9d016cea24e69509eeb6a40fb8552e31af08e948fb750d9e03b216ae`.

## Numbered findings and dispositions

1. **Pass — candidate identity, hashes, notices, declarations, sentinels, and
   deterministic rebuild.** All artifact/source/file-set digests recompute.
   Import commit `407b5ef039aa0474c400c0721749baa126e53270` and prior gitlink
   `0235970293590f673a253950e6c61017cefa97df` match. The shim accurately says
   no in-file notice; the other eight files retain GPLv2-or-later headers.
   Project/legal review remains explicitly pending with no distribution or
   legal conclusion. Decoder declarations, registration/output IDs, metadata,
   classes, directions, and integer `0xFF`/`has_channel` vectors match source.

2. **Pass — both round-5 corrections and every protocol timeline are now
   source-consistent.** UART `get_data_bits()` stores ordinary
   `[signal, ss, es]` lists; the all-low BREAK fixture now has eight zero bit
   triples after non-SPI normalization, scalar zero, `AA==` binaries, zero
   annotations, invalid STOP/FRAME, then BREAK in exact source order. I2C
   `handle_address_or_data()` increments at entry: address 8 + data 8 + the
   retained sample-370 partial bit gives 17, while ACK/NACK do not increment;
   inclusive elapsed `371` at 1,152,000 Hz gives
   `int(1_152_000 * 17 / 371) = 52787` before STOP records. The cap bases are
   unchanged because this correction changes neither corpus byte length nor
   its maxima.

   Static re-proof also confirms that SPI without CS emits Python
   `CS-CHANGE(None,None)` at `(0,0)` before line 342's first `wait({})`, and
   UART `handle_packet()` lines 288-310 emits only packet annotation through
   `putx_packet()`. Literal newest-first SPI recurrence ends at 170/180, not
   290/300. All UART/SPI/I2C transitions, waits, skips, `matched`, pins,
   repeated START, partial-unit EOI, declarations, binary/Python/annotation/
   metadata values, classes, tags, coordinates, directions, and emission order
   agree with the checked-in source across all 57 timelines.

3. **Changes required — the claimed closed relative-import inventory omits
   `common.srdhelper.mod`.** Static AST inspection finds four initializer
   edges: UART, SPI, and I2C each import `.pd`, and
   `Software/decoders/common/srdhelper/__init__.py` imports `.mod`. Provenance
   lists the three `.pd` edges but no
   `common.srdhelper.mod (relative package import .mod)` entry. Inventorying
   and hashing `mod.py` as a file does not make the explicitly enumerated
   import graph exact. R1 and stopping condition 1 therefore remain open.

4. **Changes required — the option matrix is not exhaustive at UART packet-
   delimiter width boundaries.** The governing matrix requires every inclusive
   and exclusive numeric boundary, explicitly including packet delimiters for
   every selected data width. Both directions have direct accepted maxima only
   for 8 and 9 bits (`255`, `511`). They lack accepted direct/static-equivalent
   rows and fixtures for 5-, 6-, and 7-bit maxima (`31`, `63`, `127`): six
   missing accepted witnesses in total. The candidate does include max-plus-one
   rejections `32/64/128`, but records them under synthetic option names such
   as `rx_packet_delim_width_5`, rather than the checked-in option key with an
   explicit selected-width context. Rejected boundaries cannot prove their
   accepted inclusive neighbors. Thus the otherwise unique 159-row matrix and
   its 56 direct witnesses do not satisfy the closed width-dependent option
   contract or stopping condition 2.

5. **Pass — the five API-edge decisions and finite protocol bounds are
   internally demonstrated.** The corpus fixes first/later empty waits, host-
   cursor search and zero/positive skip behavior, simultaneous alternatives,
   half-open intervals with legal capture-count endpoints, and EOI suppression
   of partial units while preserving prior emissions. Every protocol wait uses
   the first eligible matching sample, and every terminal failed wait and
   record is justified within its per-fixture finite `sample_count`.

6. **Pass — all 12 version-1 objects and literal CLI bytes are exact.** Every
   required root is complete; options are fully materialized; mapping order,
   actual declarations/output IDs, all four record kinds, all nine Python
   value tags, canonical padded base64, coordinates, and rational absolute/
   trigger-relative times validate. The declared ordered path/NUL/file-digest
   algorithm reproduces each real decoder file-set identity. Compact sorted
   UTF-8 canonicalization with `ensure_ascii=False`, `allow_nan=False`, and
   exactly one LF independently reproduces every golden byte string.

7. **Pass — all 17 caps form a complete, finite, non-enforcing static
   specification.** Exact positive values, units, domains, accept-at-value and
   reject-at-value-plus-one boundaries, structured basis/operation/multiplier/
   floor/result arithmetic, value-specific rationales, and cross-cap links
   recompute from the candidate corpus. Deadline/grace policy quantities and
   corpus margins are explicit. The artifact correctly disclaims macOS
   observation, executable enforcement, operator approval, and product-
   threshold status. This pass cannot transfer to a corrected matrix/provenance
   corpus; dependent values and bytes require fresh rebuilding and review.

8. **Pass — independence and exclusions.** The generator imports only
   `argparse`, `copy`, `hashlib`, `json`, `pathlib`, and `__future__`, performs
   static data generation, and contains no decoder/host/reference oracle,
   dynamic import, runtime enforcement, or product runner. The scoped scan
   found no prohibited dependency/action, executable authority, candidate-path
   drift, browser/hardware/firmware/C#/Cycle 4 change, or unauthorized file.

## Discrepancies, deferrals, scope, and approval

Findings 3 and 4 require a corrected immutable semantic-fixture candidate and
complete fresh verification; no pass transfers. Project/legal disposition,
pre-execution runner/enforcement, decoder characterization, raw observations,
threshold proposal/review, operator approval, and later B1 gates remain
deferred in their governing order. I did not repair the candidate or edit the
corrected verifier, implementation tests, prior records, contracts, progress,
product, runner/method/probe/enforcement/raw, schema/validator/evidence
manifests, decoder, package/lock/workflow, Cycle 1/2 evidence, browser,
firmware, hardware, C#, or Cycle 4 paths.

- Discrepancies: missing relative `.mod` import edge; six missing accepted
  packet-delimiter width maxima.
- Approval needed: none.

changes_required
