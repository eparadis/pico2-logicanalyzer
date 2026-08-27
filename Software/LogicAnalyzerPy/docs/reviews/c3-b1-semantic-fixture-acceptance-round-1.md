# C3-B1 semantic-fixture acceptance — round 1

## Identity and exact subject

- Acceptance identity/role: `c3-b1-semantic-fixture-acceptance-1`
  (`/root/c3_b1_fixture_accept`), independent semantic-fixture acceptance.
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Exact fixture candidate commit/tree:
  `c1420ad9b4309fc7417acbc228085b68237c24d0` /
  `26ef344bfb76bec4a8e68be06a411b4d27d20de1`.
- Immutable round-8 verification commit/record SHA-256:
  `fa85b83e6ded1a081480c1c0a66366bbc91711f0` /
  `9e1ad275730f30ff1ccbaf3c8e0a59e06c98463d332f249e46b4242be2d18bd5`.
- Immutable accumulated-validation commit/record SHA-256:
  `ef43dc7ca6b91c471ee0113ca8cf90ffc1359d43` /
  `c4aec32157039cdcc3680d1bb430c2bc4d407a571c7e335f856f1f7c633241e6`.
- Audit UTC: `2026-08-27T02:21:38Z`.
- Audit descendant before this record: HEAD
  `e5ce8bb47ed26480b664484ec3f12fc03977143e`, tree
  `681ec33298a933bfc42bbc1a1a19e958c5ae780c`, branch `python-rewrite`, clean
  worktree.

This acceptance covers only the immutable semantic fixtures and finite static
experiment-cap specification. It does not accept or claim executable cap
enforcement, a runner, decoder execution, characterization, threshold
approval, package placement, a project/legal conclusion, a B1 manifest or
checkpoint, or any later batch.

## Independent audit method and commands

I read the repository instructions and subagent policy, the durable goal, the
governing orchestration and batch contracts at the exact contract commit, the
latest committed B1 assignment, the complete correction history, the exact
candidate diff and artifacts, the round-8 verifier record, and the accumulated
validation record. Checked-in decoder/shim/helper files were treated only as
inert source/static data. I did not run a generator, test, decoder, runner,
helper runtime, C#/.NET, pythonnet, libsigrokdecode, sigrok runtime, hardware,
network install, browser, or Cycle 4 action.

All shell commands used the required `rtk` prefix. Results:

- `rtk git show -s --format='%H %T %s' <contract> <candidate> fa85b83
  ef43dc7` — exit 0; all required commit/tree identities matched.
- `rtk git diff-tree --no-commit-id --name-status -r <candidate>` — exit 0;
  the round-8 candidate changed only the fixture generator, four generated
  fixture/manifest artifacts, and the fixture implementation test.
- `rtk git diff --name-status <candidate>..HEAD -- <fixture and evidence
  scopes>` and `rtk git diff --quiet <candidate>..HEAD -- <all candidate
  paths>` — exit 0; descendant differences are only progress, verification,
  and accumulated evidence, while every candidate-owned path is byte-identical.
- `rtk shasum -a 256 <candidate artifacts and both evidence records>` — exit
  0; all candidate and evidence digests matched the immutable records.
- `rtk jq ... experiment-caps.json` — exit 0; exactly 17 unique caps, all
  positive finite integers, with required fields, derivation result equal to
  value, accept equal to value, and reject equal to value plus one.
- `rtk jq ... semantic-fixtures.json` — exit 0; 63 finite timelines and all
  five separately stated unresolved edge decisions are present.
- `rtk jq ... option-matrix.json` — exit 0; 165 unique closed rows: 19
  defaults, 43 accepted enumeration/inclusive-boundary rows, and 103 explicit
  prelaunch rejection rows.
- `rtk jq ... typed-vectors.json` — exit 0; 12 normative vectors, 12 literal
  CLI goldens, all four record kinds, and all nine closed Python-value tags.
- `rtk jq ... provenance.json` — exit 0; import commit, prior gitlink, nine
  source identities, closed imports including helper relative `.mod`, three
  ordered file sets, notices, and the pending project/legal disposition are
  explicit.
- `rtk git log --oneline --reverse -- <fixture and verifier history>` — exit
  0; eight immutable verification rounds and every corrected candidate remain
  ordered and preserved.
- `rtk git diff --check`, final `rtk git status --short`, and candidate-path
  quiet diff — exit 0; no pre-existing worktree change or candidate drift was
  present before this acceptance record.

## Bound identities and finite values

The independently recomputed candidate artifact SHA-256 values match round 8:
generator `2fc53874e8f9539f37850da45a09e9d740f7997ee41a9435ba2f17b41ce4f800`,
provenance document `3155b8ea00e54fc8facd86d6a28604e9a0f3cf1097751392e6a12380ad9ddc4c`,
semantic-fixture document
`a78e3a6675427e6ddc650de624ed492d18901d90e35353bce6f5645c0207240d`,
provenance JSON `e0a6082869cdf51e7abf74441065b080b8e1d6614a45ad52f034ef95f4f4c8e4`,
semantic JSON `8da1d2aa2256cce5c56ac2df4a629d90a95c21cb84d633522780394439888e64`,
option matrix `5d84b9d9855e9e2e75d45d5cd9560fbcfd1ac6ff88abfcf1c1326d3427ffc209`,
typed vectors `b5cc317ff476fcb2446eaf6b376c346210f63fbca8d0df84984b7990a528ffbf`,
experiment caps `fc5f3b0de17ae9f74b363ee5d4847ea2f9a88b9e0918cba8e848305ebbda05a1`,
fixture manifest `6a5b26f73ff3ae5e4ec64962acc43d08d52dbf8b7ab2e574b976ceab5d8f9a43`,
implementation test `6349a196381e7672b7a21cf73498ec8df9dd9309a69d5c89e947463f4748c857`,
and immutable verifier test
`e7081c043c790223d07b76724d6b5f73cca6c1d185635b0ad18f591bbd7a5cf9`.

The exact cap values are: wall deadline `5000 ms`; terminate grace `250 ms`;
input `100000 samples`; request `46354688 bytes`; output `69632 records`;
encoded and decoded `6180864 bytes` each; stdout `193152 bytes`; stderr
`96576 bytes`; diagnostic `12072 bytes`; text and binary `3090432 bytes`
each; nested depth `40`; nested items `69632`; retained result `185418752
bytes`; recursion `320 frames`; worker address space `2966700032 bytes`.
Every entry states its basis, structured operation, multiplier/floor, unit,
domain, value-specific rationale, exact boundary, and later-runner coverage.
The artifact expressly labels these as conservative pre-execution values with
no observation, enforcement, operator-approved threshold, or product claim.

## Findings and dispositions

1. **Pass — exact subject, immutability, scope, and role separation.** The
   candidate/tree is exact; all candidate-owned bytes remain unchanged in the
   verification and accumulated descendants. The fixture implementor, fixture
   verifier, this acceptance identity, primary orchestrator, and the separately
   assigned runner implementor/verifier/acceptance roles are distinct. This
   acceptance authored only this record and repaired nothing.

2. **Pass — correction history and finding disposition.** Rounds 1-7 and their
   corrected candidates remain immutable. Round 8 freshly closed the last
   source-declaration discrepancy and re-audited the full fixture, not merely
   the delta. No unresolved verifier finding is carried into this candidate.

3. **Pass — independent expected semantics and complete finite coverage.** The
   63 source-derived timelines cover the five frozen edge semantics, required
   optional-pin sentinel cases, UART RX/TX directions and delimiter widths,
   SPI MISO/MOSI/no-CS/active-CS behavior, I2C complete/partial/repeated-start
   behavior, record ordering, coordinates, and end-of-input rules. The 165-row
   matrix classifies every default, accepted enum/boundary, and unsupported
   type/boundary/sentinel/unknown/duplicate case with named finite witnesses or
   explicit prelaunch rejection. The 12 v1 vectors and literal bytes close all
   promised record/value tags and bind real decoder file sets, declarations,
   mappings, defaults, and output IDs. Evidence derives from contracts and
   inert source, not decoder or host output.

4. **Pass — provenance, imports, notices, and file sets.** Import commit
   `407b5ef039aa0474c400c0721749baa126e53270`, prior gitlink
   `0235970293590f673a253950e6c61017cefa97df`, all nine exact file digests,
   closed initializer/helper/local/stdlib imports, and UART/SPI/I2C ordered
   file-set hashes are recorded. Eight files retain GPLv2-or-later notices;
   the shim accurately says no in-file notice was observed.

5. **Pass — cap specification completeness and exact boundaries.** All 17
   required experiment-only cap categories have finite integer values,
   independently inspectable derivations, exact accept/reject boundaries, and
   cross-cap references. There is no missing schema field, duplicate cap ID,
   non-finite value, or disguised enforcement claim.

6. **Pass — evidence order and accumulated gate.** Round-8 verification `pass`
   precedes the root accumulated-validation `pass`; both bind the same exact
   candidate. The accumulated record contains the mandatory clean macOS Python
   3.12 hash-locked bootstrap, all 403 non-hardware tests without a mandatory
   skip, Ruff, strict mypy, installed help, fixture rebuild, focused tests,
   Cycle 1/2 evidence validation, browser/performance regressions, and scoped
   dependency/import/process/path audits. No wrong-candidate, failed, skipped,
   simulated, or out-of-order result is accepted.

7. **Pass — correctly bounded readiness.** The static fixture gate is ready
   for the distinct pre-execution-runner candidate only. Executable cap
   enforcement remains wholly unclaimed and must be implemented and reviewed
   in that runner gate using inert/hostile non-decoder probes before any
   decoder execution. This verdict neither transfers to the runner nor
   authorizes decoder execution, characterization, thresholds, manifest, or
   checkpoint creation.

8. **Pass — project/legal ordering is not overstated.** Provenance and notices
   are adequate inputs, while snapshot package placement and reconciliation
   with MIT package metadata remain explicitly pending as a later B1
   project/legal input. The editable accumulated installation exposed no
   decoder snapshot, and neither candidate nor evidence makes a legal,
   distribution, build, or publication conclusion.

## Discrepancies, deferrals, and approval

- Discrepancies: none.
- Deferred in governing order: distinct runner implementation/verification/
  accumulated validation/acceptance; project/legal snapshot-placement review;
  permitted snapshot execution; raw characterization and independent
  reproduction; numeric-limit proposal/review/acceptance and explicit operator
  approval; later B1 evidence, manifest verification, and checkpoint.
- Worktree scope: this acceptance creates exactly this one review record and
  changes no candidate, test, progress, contract, runner, product, decoder,
  package, lock, workflow, evidence manifest, hardware, browser, or Cycle 4
  path.
- Approval needed: none.

pass
