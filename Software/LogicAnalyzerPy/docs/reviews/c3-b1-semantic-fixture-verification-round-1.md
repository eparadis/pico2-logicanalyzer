# C3-B1 semantic-fixture verification — round 1

## Identity and immutable subject

- Verifier identity/role: `c3-b1-semantic-fixture-verifier-1`
  (`/root/c3_b1_fixture_verify`), independent semantic-fixture verifier.
- Fixture candidate ownership: original implementor
  `c3-b1-semantic-fixture-implementor-1` and replacement implementor
  `c3-b1-semantic-fixture-implementor-replacement-1`.
- Distinct planned fixture acceptance identity:
  `c3-b1-semantic-fixture-acceptance-1`.
- Distinct runner identities: `c3-b1-pre-execution-runner-implementor-1`,
  `c3-b1-pre-execution-runner-verifier-1`, and
  `c3-b1-pre-execution-runner-acceptance-1`.
- Governing commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Tested candidate commit/tree: `95ce93d8e1f504c6476cd8ab09ba35fe26082add` /
  `7815d9a70a44dbef8042a921ccc10cfd9aebaa67`.
- Verification UTC: `2026-08-26T23:27:02Z`.
- Current descendant qualification: verification began at descendant HEAD
  `ac1aed784f40c8b234f02aac72d20ddbca9a4a6d`, tree
  `d253487b6edc94308babd53af4190fb87ae489d1`, branch `python-rewrite`.
  `git diff 95ce93d..HEAD -- <all ten candidate paths>` was empty. The only
  verification worktree addition before this record was
  `tests/verification/test_c3_b1_semantic_fixture_candidate.py`; it does not
  alter the tested candidate.

## Authoritative sources and method

Expectations were derived from the approved `CYCLE3_GOAL.md`,
`CYCLE3_ORCHESTRATION.md`, `CYCLE3_BATCH_EXECUTION.md`, the normative Step 5
sections and stopping-condition checklist in
`docs/cycle-3-discovery-review.md`, and static AST/source inspection of the
exact candidate's nine checked-in shim/decoder/helper files. Candidate prose,
generator assertions, and implementation-test success were not treated as an
oracle. Files were read with `git show 95ce93d:<path>` or from descendant paths
proven byte-identical to the candidate. No decoder module was imported.

## Environment and commands

- macOS 15.7.7 (24G720); Python 3.12.13 from `.venv/bin/python`.
- `rtk git rev-parse 95ce93d... 95ce93d...^{tree}` — exit 0; exact tested
  identities above.
- `rtk git diff --name-status 95ce93d..HEAD -- <ten candidate paths>` — exit
  0, no output.
- Static Python using `git show`, `ast.parse`, `hashlib.sha256`, and
  `json.loads` over the exact candidate blobs — exit 0; nine source hashes and
  six artifact hashes independently recomputed; decoder metadata/imports and
  source `register`/`put`/`wait` branches were inspected without import or
  execution.
- `rtk .venv/bin/python scripts/generate_cycle3_fixtures.py --check` — exit 0.
- `rtk .venv/bin/python scripts/generate_cycle3_fixtures.py` followed by
  digest comparison and `--check` — exit 0; byte-identical rebuild.
- `rtk .venv/bin/python -m pytest -q
  tests/implementation/test_cycle3_fixtures.py` — exit 0, `6 passed`, no
  skips. This is implementation evidence only.
- `rtk .venv/bin/python -m pytest -q
  tests/verification/test_c3_b1_semantic_fixture_candidate.py` — exit 1,
  `6 failed, 1 passed`, no skips. Failures independently expose findings 2-7.
- Scoped `rtk rg` audit over the ten candidate paths for prohibited runtimes,
  dynamic import/eval/exec, and runner/host execution — exit 0. Matches were
  inert statements of prohibition and the implementation test's subprocess
  invocation of the static generator; no decoder/reference/runtime execution
  path or enforcement implementation was found.
- `rtk git diff --check` — exit 0.
- A preliminary `unittest discover` command collected zero tests because the
  suite uses pytest functions; it is not relied upon. No required check was
  skipped.

## Independently recomputed artifact digests

| Candidate artifact | SHA-256 |
| --- | --- |
| `provenance.json` | `1932b65ef9ab9b843e3fd07a1afcab9a564e2e31fcdb9ed15b0114481b80147d` |
| `semantic-fixtures.json` | `c034ba8c8eb8bbfde74f24bdf5cf73d383021262ea98e2e74855617d3f09ac59` |
| `option-matrix.json` | `8a89c88f849396bee78a192b7fd4684d3ca44fc076c6edb080585948d93f9e9d` |
| `typed-vectors.json` | `3f3e31c40da00ae068bc286a000387c216b8a3a1342c95f4c3d684c4fb141a8d` |
| `experiment-caps.json` | `b768f7214b797ef7acef4679affd9ea20c628601253f1dff3558411e2d90a057` |
| `manifest.json` | `dc1d1453b8594f10260520b009cc856fc536fa230690c0b0c5628f80ef579771` |

The independently recomputed nine source digests equal the approved discovery
values and candidate provenance values: shim `385124...01a`, UART initializer
`351098...92f`, UART decoder `67655f...fcc`, SPI initializer `91b207...f56c`,
SPI decoder `ef9cac...d5d3d`, I2C initializer `379318...86f`, I2C decoder
`b68991...a305`, helper initializer `125b06...05d1`, and helper implementation
`602b27...ceb6`.

## Findings and dispositions

1. **Pass — file identity, notices, deterministic generator, and v1 vectors.**
   All nine file digests, import commit, and prior gitlink match approved
   literals. Per-file header inspection supports the eight GPL-2.0-or-later
   observations and the shim's explicit no-in-file-notice observation. The
   project/legal placement decision is correctly still pending and no legal
   conclusion or distribution authority is claimed. The generator AST imports
   only stdlib static-data modules, contains no decoder/host/reference oracle,
   rebuilds byte-identically, and the manifest digests agree. All nine Python
   value tags, four record kinds, complete v1 root/record/time/declaration
   shapes, and 12 literal CLI values reproduce the required Python 3.12
   canonical bytes plus one LF.

2. **Changes required — no finite capture boundary exists in any semantic
   timeline.** Every one of the 11 timelines omits `sample_count`. Consequently
   end-of-input, trigger bounds, coordinates at `capture_count`, and whether a
   wait or record lies past the capture cannot be evaluated. The claimed
   incomplete/boundary fixtures therefore cannot freeze edge decisions 4-5.

3. **Changes required — wait traces contradict their own transition data.**
   Static reconstruction found 56 returned mapped-pin discrepancies. Examples
   include UART sample 10 declared high but returned low, SPI `{'0':'r'}`
   entries at samples where CLK is low/falling, I2C returned SCL/SDA values
   inconsistent with the declared bus, and I2C waits through sample 190 while
   the full fixture declares no corresponding transitions after sample 91.
   These are not genuine decoder-call timelines and cannot prove wait,
   matched, direction, ordering, or sample-coordinate semantics. The literal
   `0xFF` optional slots themselves are integers and ordered correctly, but the
   mapped levels beside them are often false.

4. **Changes required — SPI expected output is fabricated/incomplete and in
   the wrong source order.** Static inspection of `spi.Decoder.putdata()`
   establishes binary output first, Python `BITS`, Python `DATA`, eight bit
   annotations for the present line, then its dataword annotation; the caller
   later emits bitrate metadata. Each completed word fixture instead has only
   Python `DATA`, binary, one annotation, and metadata, in that incorrect
   order. This fails exact classes, values, records, coordinates, and
   request-wide order for both MOSI and MISO. It reproduces the prior
   generic-record defect despite corrected direction/class labels.

5. **Changes required — named UART and I2C branches remain absent.** The UART
   fixture named `...idle-packet` has parity/stop/break/idle/frame records but
   no packet record or packet annotation despite enabling delimiter/length.
   The I2C fixture named `i2c-unshifted-repeated-start` merely copies the first
   two ordinary START records and contains no `START REPEAT` Python record or
   repeated-start annotation. Thus the prior incomplete UART packet and I2C
   branch defect is not objectively resolved. The full I2C write case does
   contain its data/NACK records, but its contradictory wait timeline prevents
   acceptance.

6. **Changes required — the option matrix's static equivalences are generic,
   and frequently false.** Forty rows use only two repeated arguments across
   many unrelated options. The UART text claims baudrate, data width, parity,
   stop width, formatting, inversion, sampling point, delimiters, and lengths
   are all merely rendering or the same sampled-frame branch and says a
   “distinct rendering is asserted by the named source option,” while the
   named default fixture does not materialize those row values. These are not
   option-specific source equivalence proofs. Direct-row IDs are unique and
   the 16 direct rows do materialize their values, but that does not validate
   the remaining accepted matrix.

7. **Changes required — cap values have no independently derived rationale.**
   The 17 required categories, positive finite values, units, domains, and
   accept/value-plus-one reject boundaries are present, and the corpus
   correctly claims no executable enforcement. However every cap repeats the
   same tautology, `finite cap required before any runner exists`; none explains
   why its exact value is conservative, independently derived, internally
   consistent with related caps, or adequate for the finite fixtures. The
   required exact-value rationale gate is therefore unproved.

8. **Changes required — the closed import inventory is not exact.** Static AST
   parsing confirms the approved external/local roots used by the decoder and
   helper implementations, but each package initializer performs relative
   import `.pd`; these three imports are absent from `permitted_imports`.
   Inventorying their files elsewhere does not make the claimed exact import
   list complete.

## Discrepancies, deferrals, and prohibited audit

Findings 2-8 are candidate defects, not deferred work. The candidate was not
repaired. Project/legal disposition, actual cap enforcement, runner probes,
decoder characterization, raw observations, threshold proposal/approval, and
later B1 gates remain correctly deferred by contract; this verdict grants no
authority to begin them. No executable cap enforcement or runtime oracle is
present or claimed. No product/runner/method/probe/enforcement/raw, manifest,
governance, decoder, package/lock/workflow, Cycle 1/2, browser, firmware,
hardware, serial, C#, or Cycle 4 path was modified.

No decoder, approved snapshot, compatibility shim/helper, C#/.NET,
pythonnet, libsigrokdecode, `sigrok-cli`, host, reference runtime, hardware,
server, or browser was imported or executed during this verification.

## Approval need and verdict

- Approval need: none.
- Required disposition: create a corrected semantic-fixture candidate and
  repeat independent verification from the new immutable identity; no pass
  transfers.

changes_required
