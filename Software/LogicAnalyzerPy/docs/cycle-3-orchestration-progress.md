# Cycle 3 orchestration progress

This is the compact execution log for Cycle 3. Accepted Cycle 1 and Cycle 2
progress, completion records, manifests, and rollback identities remain
unchanged.

## Initial repository and launch state

- Recorded: `2026-08-26T22:53:40Z`.
- Branch: `python-rewrite`, tracking `origin/python-rewrite` with no divergence.
- Launch HEAD: `2af31d3445abb6fe3ba01360b38a0c3db4a88ea6`.
- Launch tree: `87e094f7a0034ed27a582fc8164d133bb448479d`.
- Worktree: clean; no tracked, staged, unstaged, untracked, or unrelated user
  change was observed.
- Approved contract: commit
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0`, tree
  `d9fb09345ab85580cd8c877745262d1b481e366f`; the six governing files are
  byte-for-byte equal to that commit and the three immutable
  `contract-final-round-5` passes are committed in
  `0d3755a2798cdfafd2a89ebaedcac40acc8c356a`.
- Approved goal: commit `6a2d09a444797bb0b73c94b259b1cbd826084129`,
  tree `b6e1441af95f4e4a3cc17adeb1681e94d06a2557`; the governing set and
  `CYCLE3_GOAL.md` are byte-for-byte equal to that commit and the three
  immutable `goal-final-round-4` passes are committed in
  `3ff24fcacd893869ddb717e6b130b528ff8fd931`.
- Step 10: the completed launch preflight is committed at
  `2af31d3445abb6fe3ba01360b38a0c3db4a88ea6`; its approved snapshot digests,
  macOS 15.7.7 / Python 3.12.13 qualification, regressions, exclusions, and
  absence findings are the launch baseline.
- Goal invocation: the operator invoked the exact approved Cycle 3 objective
  on 2026-08-26. This authorizes the governed execution sequence but does not
  waive any B1 internal gate, project/legal record, numeric-limit decision,
  dependency-install approval, or hosted-CI approval.
- Prohibited actions at activation: none performed. No decoder or C# code has
  executed for Cycle 3; no prohibited runtime/dependency, hardware, firmware,
  live capture, browser decoder, package publication, unsupported-platform,
  or Cycle 4 work has occurred.

## Frozen Cycle 3 paths and command classes

- Orchestrator governance: this progress record;
  `docs/evidence-manifest/cycle3-schema.json`;
  `scripts/validate_cycle3_evidence.py`; active-batch manifests under
  `testdata/evidence/c3-bN.json`; shared traceability, checkpoint, completion,
  and completion-seal records.
- B1 semantic fixtures: `docs/cycle-3-decoder-provenance-license.md`,
  `docs/cycle-3-semantic-fixtures.md`, `testdata/decoders/cycle3/`,
  `scripts/generate_cycle3_fixtures.py`, and
  `tests/implementation/test_cycle3_fixtures.py`.
- B1 characterization runner: `tools/cycle3_characterize/`,
  `docs/cycle-3-characterization-method.md`,
  `testdata/decoders/cycle3-raw/`, and focused runner tests whose exact paths
  will be recorded before that assignment. These paths contain no product or
  public host surface and are not installed.
- Evidence reviews: immutable Cycle 3 records under `docs/reviews/` with paths
  fixed in each assignment before authorship. Verification-only tests use
  `tests/verification/` and may not alter authoritative expected fixtures.
- Minimum accumulated command classes are the exact clean Python 3.12
  hash-locked bootstrap, no-build-isolation/no-dependency editable install,
  `pip check`, Ruff, strict mypy, all non-hardware pytest, installed CLI help,
  Cycle 1/2 evidence validation, Cycle 3 fixture rebuild and digest validation,
  prohibited dependency/import/process audit, and active focused/resource
  gates. B4 and B5 additionally require exact-candidate hosted macOS CI.
- Stable local environment path: `Software/LogicAnalyzerPy/.venv`; stable clean
  bootstrap path: `/private/tmp/cycle3-clean-python`. Dependency download and
  hosted-CI execution remain root-routed approval classes.

## C3-B1: provenance, semantic fixtures, and approved limits

- State: In progress.
- Objective: freeze the exact executable snapshot and project/license
  disposition, independently derived declarative UART/SPI/I2C semantic and
  stress fixtures, the five API-v3 edge decisions, the complete finite
  experiment-only cap specification, reproducible raw characterization, and
  independently reviewed/operator-approved numeric ceilings including maximum
  SPI word size.
- Prerequisites: approved contracts and goal with their common-commit passes;
  completed Step 10; accepted Cycle 1/2 baseline; exact goal invocation; clean
  macOS/Python 3.12 launch state. Present. Project/legal disposition, runner
  gate, raw evidence, proposal reviews, dependency-install authority, and the
  later operator numeric decision remain ordered B1 gates, not prerequisites
  that may be simulated.
- Governing commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Starting commit/tree: `2af31d3445abb6fe3ba01360b38a0c3db4a88ea6` /
  `87e094f7a0034ed27a582fc8164d133bb448479d`.
- Implementation agent: final B1 assembly remains orchestrator-owned; internal
  implementation identities are fixed below.
- Verification agent: `c3-b1-final-verifier-1` (planned canonical identity
  `/root/c3_b1_final_verify`).
- Acceptance agent: `c3-b1-final-acceptance-1` (planned canonical identity
  `/root/c3_b1_final_accept`).
- Manifest verifier: `c3-b1-manifest-verifier-1` (planned canonical identity
  `/root/c3_b1_manifest_verify`).
- B1 internal identity map: semantic-fixture implementor
  `c3-b1-semantic-fixture-implementor-1` (`/root/c3_b1_fixture_impl`), verifier
  `c3-b1-semantic-fixture-verifier-1` (`/root/c3_b1_fixture_verify`), and
  acceptance `c3-b1-semantic-fixture-acceptance-1`
  (`/root/c3_b1_fixture_accept`); pre-execution-runner implementor
  `c3-b1-pre-execution-runner-implementor-1` (`/root/c3_b1_runner_impl`),
  verifier `c3-b1-pre-execution-runner-verifier-1`
  (`/root/c3_b1_runner_verify`), and acceptance
  `c3-b1-pre-execution-runner-acceptance-1`
  (`/root/c3_b1_runner_accept`). All six are mutually distinct and distinct
  from the final B1 verifier/acceptance identities.
- In scope: R1-R5 and the B1 start of R9, R21, R23-R25; stopping conditions
  1-3 plus continuous scope/evidence preparation for 13-14, 16-17; only the
  governed static fixture gate, later non-decoder runner gate, approved snapshot
  characterization, proposal, explicit numeric decision, and B1 evidence
  sequence.
- Out of scope: public/private product host, library or CLI decode behavior;
  decoder snapshot edits; browser/API/frontend decoder work; hardware,
  firmware, serial/live capture; dynamic discovery, stacking, `.lac`;
  C#/.NET/pythonnet/libsigrokdecode/`sigrok-cli` or external runtime execution or
  dependency; packaging/publication; non-macOS claims; Cycle 4.
- Owned paths: orchestrator owns the frozen governance/schema/validator/shared
  evidence paths above. The semantic-fixture implementor owns only the five
  exact semantic-fixture paths above and may not author runner, method,
  launch/import, cap-enforcement, cleanup, or probe content. The runner
  implementor owns only the later characterization paths and may not author or
  change authoritative expected fixtures. Verifiers own their assigned
  verification tests and immutable records; acceptance identities own only
  their immutable records and never repair candidates.
- Authoritative evidence: approved governing sources and review records; exact
  checked-in decoder/shim/helper source and launch digests; accepted Cycle 1/2
  completion/manifests/tests; independently calculated timelines, literals,
  and version-1 object/CLI bytes. Decoder, host, C#, or external runtime output
  is never an expected-value oracle.
- Focused evidence: static file/import/provenance/license audit; deterministic
  fixture generation and byte rebuild; literal option/sentinel/output/tag and
  edge-semantic coverage; complete exact finite experiment-cap schema and
  boundary coverage; later immutable non-decoder runner enforcement/cleanup
  matrix; raw characterization/reproduction; proposal review/acceptance; and
  explicit operator decision.
- Accumulated evidence: fresh locked Python 3.12 environment; full Python Ruff,
  strict mypy, non-hardware tests, installed help; Cycle 1/2 evidence validation;
  decoder/helper closed-import and digest audit; Cycle 3 fixture rebuild;
  prohibited dependency/import/process and excluded-scope audit; all completed
  B1 focused gates.
- Authority notes: static fixture work is authorized now and must execute no
  decoder. Only the unchanged runner candidate may execute snapshots after its
  non-decoder verification, accumulated, and acceptance passes. Dependency
  downloads require root-routed approval. Project/legal review must settle
  package placement/notices/metadata before editable installation exposes
  snapshots. Exact numeric limits require later explicit operator approval.
- Prohibited runtime audit: inspect scoped active Python product, dependencies,
  locks, tests, scripts, fixtures, workflows, commands/evidence, and active
  process names for prohibited use while excluding preserved inert historical
  C# metadata from the absence claim. Expected result is no use or active
  process and no decoder execution before the runner gate.
- Risks and unknowns: the semantic-fixture candidate must independently settle
  all five edge semantics and all option/sentinel/tag rows without runtime
  corroboration; the project/license disposition must avoid presenting legal
  inference as fact; experiment caps must be conservative, finite, complete,
  and non-enforcement-only at this gate; later clean install and process
  observation may require narrowly scoped approval.

## Deferred work

- No deferred or unrelated Cycle 3 finding is recorded at B1 activation.

## C3-B1 semantic-fixture implementation assignment

- Assigned: `2026-08-26T22:55:00Z`.
- Identity: `c3-b1-semantic-fixture-implementor-1`
  (`/root/c3_b1_fixture_impl`), implementor lane, `gpt-5.6-terra`, low.
- Starting orchestration commit/tree:
  `98ecf5d916be96ad2d52fa3956f8ff0b7ee44759` /
  `ef1c0d4eec0fe2686d6289cf26997d257592b49b`; candidate not yet created.
- Prerequisite: approved goal invocation and Step 10 launch record; no prior
  Cycle 3 checkpoint.
- Earliest-owned proof: fixture/provenance portions of R1-R5 and the B1 start
  of R9, R21, R23-R25; stopping conditions 1-3 and static preparation for
  13-14 and 16-17.
- Bounded objective: statically inventory the exact frozen snapshot and create
  independently calculated, human-reviewable semantic/stress timelines,
  expected calls/records, all five edge decisions, sentinel/mapping fixtures,
  closed option matrix, version-1 object and literal CLI golden vectors, a
  deterministic rebuilder, and the complete finite experiment-cap
  specification without executing a decoder or claiming enforcement.
- May edit only `docs/cycle-3-decoder-provenance-license.md`,
  `docs/cycle-3-semantic-fixtures.md`, `testdata/decoders/cycle3/`,
  `scripts/generate_cycle3_fixtures.py`, and
  `tests/implementation/test_cycle3_fixtures.py` beneath
  `Software/LogicAnalyzerPy/`.
- Prohibited ownership: runner, method, launch/import configuration,
  cap-enforcement/cleanup, probes, raw observations, product source, locks,
  workflow, evidence schema/validator/manifests, reviews, acceptance, decoder
  snapshots, governing sources, Cycle 1/2 evidence, and every excluded action.
- Focused checks: initial missing-surface failure; deterministic rebuild and
  byte check; literal schema/default/option/sentinel/tag/edge/cap coverage;
  static provenance/import/license audit; Ruff on owned Python; and
  `git diff --check`. Existing local Python only; no dependency installation.
- Separation: this identity may never author or approve runner/method/probes or
  implement B2-B4 product behavior. Fixture verifier and acceptance are the
  distinct planned identities `/root/c3_b1_fixture_verify` and
  `/root/c3_b1_fixture_accept`.
- Approval policy: `/Users/ed/.codex/SUBAGENT_POLICY.md`; no direct escalation;
  none requested.

### Pre-candidate integration review round 1

- Recorded: `2026-08-26T23:02:55Z` at orchestration commit/tree
  `39e74a27638541b36b2845a8c6f1079bc0a3ae61` /
  `ab7ff229a58c35cb1019fac3e2d1e45341f3b184`.
- State: `changes_required`; no immutable semantic-fixture candidate or
  independent verdict exists, and no pass is transferred.
- C3B1-I001: option rows inferred “default” from list position, producing
  false UART/SPI defaults and incomplete accepted/rejected numeric boundaries.
- C3B1-I002: four generic timelines reused placeholder records and did not
  establish the required decoder/output/option/mapping/malformed/boundary
  fixture coverage or full version-1 record/time shape.
- C3B1-I003: the typed-vector corpus listed tags but its sole literal CLI
  golden was an empty result, so it did not provide literal bytes for every
  record/value tag.
- C3B1-I004: the cap set omitted required retained-result and separate
  text/bytes accounting categories and lacked per-cap units/domain rationale.
- C3B1-I005: focused tests mostly asserted set membership and would not reject
  the factual/default/reference/schema defects above.
- Disposition: returned by context-preserving follow-up to the same fixture
  identity within unchanged ownership. The correction must preserve the
  no-decoder/no-runtime-oracle boundary and provide exact row/fixture/vector/
  cap references plus stronger tests before root may create a candidate.

### Pre-candidate integration review rounds 2-3 and identity replacement

- State: `changes_required`; no semantic-fixture candidate exists and no pass
  transfers.
- C3B1-I006: round 2 corrected defaults, vector byte coverage, cap categories,
  per-file notice observations, and lint, but mechanically generated one-edge
  “direct fixtures” still carried fabricated shared annotation records rather
  than independently calculated decoder-specific behavior.
- C3B1-I007: the option matrix still omitted required invalid/type/width-
  dependent rows and linked direct coverage to those fabricated timelines.
- C3B1-I008: round 3 statically identified real stream registration ordering
  but did not implement the required hand-authored UART/SPI/I2C timelines,
  declarations, wait traces, or output records. The implementor returned
  `changes_required` again with the known candidate defect unchanged.
- Original identity: `c3-b1-semantic-fixture-implementor-1`
  (`/root/c3_b1_fixture_impl`). Its draft work and three handoffs are preserved
  as authorship/history but are not accepted evidence.
- Replacement identity: `c3-b1-semantic-fixture-implementor-replacement-1`
  (`/root/c3_b1_fixture_impl_r1`), same implementor lane,
  `gpt-5.6-terra`, low.
- Reason: the original identity exhausted multiple correction continuations
  while the same acknowledged substantive fixture defect remained. The
  replacement must inspect, replace, and validate the inherited uncommitted
  fixture-only work and begins with no inherited pass.
- Ownership and separation remain unchanged. Both fixture authorship
  identities are permanently barred from the runner/method/probes and B2-B4
  product implementation. Planned fixture verifier and acceptance identities
  remain distinct and unassigned until one immutable candidate exists.

### Replacement implementation review rounds 1-3

- Replacement round 1 removed the mechanical one-edge expansion, added named
  protocol timelines and source declarations, and retained static-only checks,
  but still had no directly classified option rows and reused wrong-direction
  UART/SPI records. State: `changes_required`.
- C3B1-I009: UART TX reused RX direction/classes; UART error/packet, SPI MISO/
  word-one, and I2C data/NACK claims were not represented by their expected
  records; short wait traces did not describe complete transactions.
- C3B1-I010: all option rows were static equivalences with no direct target;
  matrix rejection/type/width coverage remained incomplete.
- Replacement round 2 added direct/equivalence closure, typed rejection rows,
  direction-specific records, UART error tags, SPI MISO/word-one/CS records,
  and I2C data/NACK/STOP outputs, but correctly reported that per-edge traces
  and deep semantic audit remained incomplete. State: `changes_required`.
- Replacement round 3 expanded wait/match/pin traces and API-edge vectors and
  reported focused generator/check/pytest/Ruff/diff passes. Root independently
  reran those checks successfully, then found four duplicated matrix row IDs:
  `reject-i2c-address_format-str-wide`, `reject-spi-wordsize-int-9`,
  `reject-uart-rx_packet_len-int-0`, and
  `reject-uart-tx_packet_len-int--2`.
- C3B1-I011: duplicate matrix identities contradict a closed uniquely
  auditable option matrix, and existing focused tests did not reject them.
- Disposition: context-preserving correction assigned to the replacement
  fixture identity. It must remove semantic duplicates, assert ID and semantic-
  row uniqueness, regenerate, and rerun the full focused gate. No immutable
  candidate exists until this correction passes root integration.

### Immutable semantic-fixture candidate and verification assignment

- Candidate commit: `95ce93d8e1f504c6476cd8ab09ba35fe26082add`.
- Candidate tree: `7815d9a70a44dbef8042a921ccc10cfd9aebaa67`.
- Candidate worktree: clean; no unrelated change.
- Candidate authorship: original fixture implementor
  `c3-b1-semantic-fixture-implementor-1` and completing replacement
  `c3-b1-semantic-fixture-implementor-replacement-1`; both remain fixture-only
  identities and are barred from runner/method/probe and B2-B4 product work.
- Root focused integration: deterministic generator `--check`, 6 focused
  fixture tests, normal Ruff on owned Python, unique option IDs/semantic
  rejection rows, direct/equivalence closure, static prohibited-oracle search,
  artifact digest recomputation, and `git diff --check` passed. No decoder ran.
- Verification identity: `c3-b1-semantic-fixture-verifier-1`
  (`/root/c3_b1_fixture_verify`), verifier lane, `gpt-5.6-sol`, low; distinct
  from both implementors and every planned runner identity.
- Verification ownership: inspect only the exact candidate; independently
  derive expectations from governing contracts and inert source; add only
  `tests/verification/test_c3_b1_semantic_fixture_candidate.py` and immutable
  `docs/reviews/c3-b1-semantic-fixture-verification-round-1.md` in a descendant
  evidence commit. It may not repair fixtures, generator, docs, product, or
  governance.
- Required verdict: exactly `pass` or `changes_required`; all findings and
  dispositions remain immutable and candidate-specific. A correction creates
  a new fixture candidate and receives fresh verification.

### Semantic-fixture verification round 1

- Tested candidate/tree: `95ce93d8e1f504c6476cd8ab09ba35fe26082add` /
  `7815d9a70a44dbef8042a921ccc10cfd9aebaa67`.
- Verifier: `c3-b1-semantic-fixture-verifier-1`; verdict
  `changes_required`, committed immutably in `165917e` at
  `docs/reviews/c3-b1-semantic-fixture-verification-round-1.md` with its
  independent test `tests/verification/test_c3_b1_semantic_fixture_candidate.py`.
- Independent result: 6 failed, 1 passed; implementation-focused tests did not
  substitute for verification. No decoder ran.
- Findings: every timeline lacked `sample_count`; 56 wait pin values
  contradicted declared transitions; SPI output omitted/reordered source-
  required binary/BITS/DATA/bit annotations; named UART PACKET and I2C repeated-
  START outputs were absent; 40 static equivalences used generic frequently
  false arguments; all 17 cap rationales were tautological rather than value-
  derived; and relative `.pd` initializer imports were absent from the claimed
  closed import inventory.
- Passing facts retained only as diagnosis, not as a transferred pass: exact
  file/artifact digests, notice observations, static deterministic generator,
  v1 shape/tag/canonical bytes, finite cap categories/boundaries/no-enforcement
  claim, and unique direct-row materialization.
- Correction owner: `c3-b1-semantic-fixture-implementor-replacement-1` in its
  original fixture-only role. It may change only the previously assigned ten
  candidate paths, may consume but not edit the immutable verification test or
  record, and must create a new candidate. All round-1 verification is invalid
  for that corrected identity and fresh verification is required.

### Corrected semantic-fixture candidate and verification round 2

- Candidate commit/tree: `79be308bc0bcab6dcdd4568a099fc730fd4fc778` /
  `8c64cb86f34d57f77b02aec5927689fb86d78953`.
- Candidate worktree: clean; no unrelated change.
- Correction: added finite capture boundaries; made wait pins/transitions
  internally consistent; corrected complete SPI source output order; added
  UART packet and I2C repeated-start records; replaced generic matrix arguments
  with option/value-specific source reasoning; added exact-value cap rationales;
  and completed relative initializer imports. The immutable round-1 verifier
  test plus implementation suite reported 13 passes; Ruff and diff checks
  passed. No decoder ran.
- Verification identity: reuse
  `c3-b1-semantic-fixture-verifier-1` strictly in its original verifier role.
  It must independently audit this new exact candidate, create only
  `docs/reviews/c3-b1-semantic-fixture-verification-round-2.md`, and must not
  edit the corrected candidate, the immutable round-1 record/test, governance,
  runner, product, or acceptance paths.
- No round-1 pass transfers. The required new verdict is exactly `pass` or
  `changes_required` and remains candidate-specific.

### Semantic-fixture verification round 2

- Tested candidate/tree: `79be308bc0bcab6dcdd4568a099fc730fd4fc778` /
  `8c64cb86f34d57f77b02aec5927689fb86d78953`.
- Verifier/verdict: `c3-b1-semantic-fixture-verifier-1` /
  `changes_required`; immutable record committed at `cee0d2e` in
  `docs/reviews/c3-b1-semantic-fixture-verification-round-2.md`.
- Existing tests: 13 passed, but deeper independent predicate/source audit
  contradicted the candidate; test success did not replace semantic proof.
- Findings: 57 of 89 waits claimed false matches; traces omitted the decoders'
  actual call shapes; uniform sample count did not define real traffic or EOI;
  SPI word-eight fixtures had four sampling edges, empty/wrong BITS values, and
  synthetic coordinates; UART packet/I2C repeated-start records were appended
  at impossible source order/bus state; option equivalences and cap rationales
  were made string-unique/value-bearing without actual derivation.
- Correction rule: rebuild coherent finite protocol schedules first, then
  independently derive exact waits and outputs from inert source. Post-hoc pin
  normalization, appended tags, string variation, or mechanically uniform
  bounds cannot satisfy the gate. The same replacement fixture implementor may
  correct only its original paths and cannot edit immutable verifier artifacts.
  A new candidate and fresh verification are mandatory; no pass transfers.

### Second semantic-fixture implementor replacement

- Prior completing identity:
  `c3-b1-semantic-fixture-implementor-replacement-1`
  (`/root/c3_b1_fixture_impl_r1`). After consuming the round-2 immutable
  findings, it correctly reported that the remaining work required substantive
  state-machine reconstruction, but returned no correction and declined to
  continue. Its authored candidate history remains immutable and unaccepted.
- New identity: `c3-b1-semantic-fixture-implementor-replacement-2`
  (`/root/c3_b1_fixture_impl_r2`), same implementor lane,
  `gpt-5.6-terra`, low. No pass or correctness claim transfers.
- Bounded outcome: replace the failed protocol schedules, waits, expected
  records, option equivalences, cap derivations, generator, and focused tests
  within the same fixture-only paths until the immutable round-1 checks and new
  independent schedule/predicate/source-order checks pass. It may inspect but
  not edit either immutable verifier record/test.
- Separation: this and both prior fixture authorship identities remain barred
  from runner/method/probe and B2-B4 product implementation. Fixture verifier,
  fixture acceptance, and all runner identities remain distinct.

### Coherent semantic-fixture candidate and verification round 3

- Candidate commit/tree: `882af78a2530879329e6525fae0c5b1f96883100` /
  `aedb51155a25720a79417d1a34112c6e171ec0f9`.
- Candidate author: completing replacement
  `c3-b1-semantic-fixture-implementor-replacement-2`, with prior fixture authors
  preserved in history; worktree clean and no unrelated changes.
- Correction: rebuilt source-shaped UART/SPI/I2C schedules and waits; used an
  integral UART bit period; added full SPI sampling edges/BITS records and I2C
  repeated-START state; added terminal failed waits; strengthened owned
  predicate/source-order checks; replaced option equivalence and cap derivation
  records. Generator check, immutable round-1 tests, implementation tests (14
  total), Ruff, and diff checks passed. No decoder ran.
- Verification identity: reuse
  `c3-b1-semantic-fixture-verifier-1` only in its verifier role for a complete
  fresh round. It may create only
  `docs/reviews/c3-b1-semantic-fixture-verification-round-3.md`, cannot repair
  candidate or immutable history, and must issue exactly `pass` or
  `changes_required`. No earlier verdict transfers.

### Semantic-fixture verification round 3

- Tested candidate/tree: `882af78a2530879329e6525fae0c5b1f96883100` /
  `aedb51155a25720a79417d1a34112c6e171ec0f9`.
- Verifier/verdict: `c3-b1-semantic-fixture-verifier-1` /
  `changes_required`; immutable record committed at `11d1c39` in
  `docs/reviews/c3-b1-semantic-fixture-verification-round-3.md`.
- Passing correction: all 107 waits now use truthful predicates, matched
  tuples, pins, skip/empty/terminal behavior and source-shaped call forms;
  provenance, imports, notices, digests, rebuild, no-oracle, and no-enforcement
  audits also passed. These facts do not transfer to a changed candidate.
- Remaining findings: five records exceed capture bounds; UART data lines/
  coordinates do not encode claimed values and its combined error schedule is
  impossible; SPI BITS/spans/output sets remain inconsistent with source; I2C
  bus levels do not encode claimed address/data/NACK; all v1 vector time
  denominators conflict with their root samplerate; materially different
  accepted option values are falsely classified equivalent; and cap arithmetic
  does not derive the stated exact values.
- Correction owner: second replacement fixture implementor in its same role.
  It must correct protocol data/coordinates/outputs, v1 denominators, option
  dispositions, and cap calculations within original ownership, create a new
  candidate, and receive fresh verification. Immutable review history cannot
  be edited and no pass transfers.

### Third semantic-fixture implementor replacement

- Prior identity: `c3-b1-semantic-fixture-implementor-replacement-2`
  (`/root/c3_b1_fixture_impl_r2`). It corrected v1 samplerate/time invariants,
  per-case finite bounds, and SPI word-eight source math after round 3, then
  twice returned without completing UART/I2C, SPI word-one, option disposition,
  cap arithmetic, or strong-test corrections. It reported no external blocker.
- Preserved uncommitted fixture-only changes: generator, generated fixture
  manifest/semantic/v1 vectors, and implementation test. They pass the existing
  14 tests but are neither a candidate nor accepted evidence.
- New identity: `c3-b1-semantic-fixture-implementor-replacement-3`
  (`/root/c3_b1_fixture_impl_r3`), same implementor lane,
  `gpt-5.6-terra`, low. It must independently inspect and complete or replace
  the inherited changes; no pass transfers.
- Ownership/separation remains identical. All four fixture authorship
  identities remain barred from runner/method/probes and B2-B4 product work;
  verifier/acceptance/runner identities remain distinct.

### Fourth semantic-fixture implementor replacement

- Prior identity: `c3-b1-semantic-fixture-implementor-replacement-3`
  (`/root/c3_b1_fixture_impl_r3`). It reconstructed truthful default UART A5
  samples and source-order records, full shifted-I2C byte/ACK/NACK/STOP output,
  a coherent unshifted-I2C repeated START, and SPI one-bit/word records. Its
  fixture-only changes pass the generator check, 14 implementation and
  immutable verification tests, Ruff, and diff checks, but it returned before
  splitting the impossible combined UART error case, replacing false option
  equivalences with direct witnesses, or deriving exact experiment caps.
- Preserved uncommitted fixture-only changes remain neither a candidate nor
  accepted evidence. No decoder or prohibited runtime has executed.
- New identity: `c3-b1-semantic-fixture-implementor-replacement-4`, same
  implementor lane, `gpt-5.6-terra`, low. It must independently inspect and
  complete or replace the inherited changes, including strong tests for all
  three remaining round-3 findings; no pass or correctness claim transfers.
- Ownership/separation remains identical. Every fixture authorship identity is
  barred from runner/method/probes and B2-B4 product work; verifier,
  acceptance, and runner identities remain distinct.

### Fifth semantic-fixture implementor replacement

- Prior identity: `c3-b1-semantic-fixture-implementor-replacement-4`
  (`/root/c3_b1_fixture_impl_r4`). It added distinct coherent UART BREAK and
  IDLE timelines, reduced the combined error case to parity/invalid-stop/packet,
  replaced generic cap margins with category-specific corpus-max arithmetic and
  exact boundaries, and materialized option values in named direct rows. Its
  generator check, 14 focused tests, Ruff, and diff checks pass.
- The prior identity correctly withheld readiness because 40 new direct option
  witnesses still inherit baseline expected-output shapes instead of deriving
  value-specific source behavior. The partial fixture-only changes are
  preserved uncommitted and are not a candidate or accepted evidence; no
  decoder or prohibited runtime executed.
- New identity: `c3-b1-semantic-fixture-implementor-replacement-5`, same
  implementor lane, `gpt-5.6-terra`, low. Its bounded outcome is to replace
  every name-only direct witness with source-derived per-value transitions,
  waits, records, and assertions, retaining static equivalence only where a
  value-specific source proof is valid, then complete the full fixture audit.
  No pass or correctness claim transfers.
- Ownership/separation remains unchanged for all fixture authorship identities.

### Complete semantic-fixture candidate and verification round 4

- Candidate commit/tree: `f53c340f5896a768e4b67fd866030be9370db723` /
  `218a80a21c769cf8e11f37903b2c91df254e107c`; worktree clean immediately
  after commit. Candidate owner: completing replacement
  `c3-b1-semantic-fixture-implementor-replacement-5`, with all earlier fixture
  authors preserved in immutable history and barred from later product work.
- Correction: rebuilt every behavior-changing accepted UART/SPI option as a
  literal direct witness with source-derived waveform, waits, record order,
  values, and coordinates; separated UART error/BREAK/IDLE cases; rebuilt
  SPI/I2C records; corrected v1 rational times and bounds; and added all 17
  finite experiment caps with machine-readable exact derivations and boundary
  cases. The SPI bit recurrence follows the checked-in source's newest-first
  `insert(0)` behavior, correcting the contrary round-3 prose rather than
  transferring it as authority.
- Root focused gate: deterministic generator check, 15 implementation plus
  immutable-verification tests, Ruff, diff check, exact eight-path scope,
  record/capture bounds, terminal/capture equality, 57-timeline/159-option-row
  closure, and static prohibited-runtime scan passed. No decoder or prohibited
  runtime executed; no cap enforcement is present or claimed.
- Verification identity: reuse only
  `c3-b1-semantic-fixture-verifier-1` (`/root/c3_b1_fixture_verify`) in its
  original verifier role for a complete fresh audit of this exact candidate.
  It may create only
  `docs/reviews/c3-b1-semantic-fixture-verification-round-4.md`, cannot repair
  candidate/history, and must issue exactly `pass` or `changes_required`.
  No earlier verdict or finding transfers without fresh proof.

### Semantic-fixture verification round 4

- Tested candidate/tree: `f53c340f5896a768e4b67fd866030be9370db723` /
  `218a80a21c769cf8e11f37903b2c91df254e107c`.
- Verifier/verdict: `c3-b1-semantic-fixture-verifier-1` /
  `changes_required`; immutable record committed at `84c8327` in
  `docs/reviews/c3-b1-semantic-fixture-verification-round-4.md`.
- Passing evidence: exact provenance/import/notices/digests, declarations,
  integer absent-pin sentinels, deterministic rebuild/no-oracle, all 17 cap
  schemas/arithmetic/boundaries, and standalone five-edge-decision statements.
  These passes do not transfer to a corrected candidate.
- Required correction: include every earliest UART edge-alternative return;
  encode UART/I2C nested ordinary lists rather than SPI namedtuples; preserve
  pre-BREAK emissions and remove invented Python PACKET; add SPI no-CS output
  and active-CS waits; include intervening I2C data/STOP events and reconstruct
  a genuine repeated START; replace placeholder v1 file-set/output/declaration
  identities with exact decoder-bound objects; rebuild dependent caps/digests.
- Recorded discrepancy for fresh static resolution: round 4 repeats the prior
  claim that SPI's newest-first `insert(0)` extrapolates the final bit to
  290/300 and counts 18 I2C bitrate bits. Direct source inspection instead
  indicates a one-edge SPI extrapolation to 170/180 and `pdu_bits` increments
  only for 16 address/data bits, yielding 49676. The correction owner must
  preserve an explicit source-recurrence proof; no conversational conclusion
  or prior finding is authority, and the next verifier must adjudicate afresh.
- Correction owner remains
  `c3-b1-semantic-fixture-implementor-replacement-5` in the fixture-only lane.
  It may correct the generator, generated fixture artifacts, fixture docs, and
  focused implementation tests only. No decoder may execute and no pass
  transfers; immutable verifier records/tests and contracts remain untouched.

### Sixth semantic-fixture implementor replacement

- Prior identity: `c3-b1-semantic-fixture-implementor-replacement-5`
  (`/root/c3_b1_fixture_impl_r5`). After authoring candidate `f53c340` and
  consuming the complete round-4 findings, it classified the correction as a
  broad fixture-model rebuild and returned without editing. It reported no
  external blocker. Its committed authorship and failed candidate remain
  immutable; no pass transfers.
- New identity: `c3-b1-semantic-fixture-implementor-replacement-6`, same
  implementor lane, `gpt-5.6-terra`, low. Its bounded outcome is the complete
  round-4 correction: earliest-event UART/I2C/SPI traces, ordinary nested value
  tags, exact preserved/emitted records, decoder-bound v1 identities and
  declarations, dependent fixture/cap rebuild, and focused source-simulation
  tests. It must explicitly prove the disputed SPI recurrence and I2C bitrate
  from checked-in source rather than copying either prior conclusion.
- Ownership/separation remains unchanged. The new identity may edit only the
  fixture generator, generated Cycle 3 fixture artifacts, fixture documentation,
  and implementation fixture tests; it remains barred from runner/product work,
  verification, acceptance, immutable history, contracts, and Cycle 4.

### Corrected semantic-fixture candidate and verification round 5

- Candidate commit/tree: `38276fcd8878da84c5e2b7f30e4de275f88a91b6` /
  `ca5b3e6489f3f0285c60e4374911ca4b2b1b39a1`; worktree clean immediately
  after commit. Candidate owner:
  `c3-b1-semantic-fixture-implementor-replacement-6`, with all prior fixture
  authorship and failed candidates preserved.
- Correction: added earliest-event UART edge/skip returns and state-specific
  idle/EOI waits; ordinary nested UART/I2C list normalization; complete
  pre-BREAK emissions and annotation-only packet output; no-CS/active-CS SPI
  events; intervening I2C data/STOP/repeated-START events; real per-decoder
  ordered file-set identities; decoder-bound v1 declarations/output IDs and
  fully materialized defaults; dependent cap/digest rebuild. Static source
  recurrence proves SPI ends 170/180 and I2C bitrate is 49681.
- Root focused result: generator/check, 10 implementation tests, Ruff, diff,
  record/capture/terminal bounds, file-set hash recomputation, v1 output-ID
  binding, and prohibited-runtime scan passed. No decoder executed.
- Historical verification-artifact disposition: the round-1 verifier test has
  two source-disproven assertions—binary must precede the mandatory initial
  no-CS `CS-CHANGE`, and UART must emit Python `PACKET`. The approved batch
  contract makes the verdict record immutable while permitting separately
  owned verification artifacts in a descendant evidence commit. Therefore the
  old test blob/history remains preserved, but only the original verifier may
  correct those two assertions in the round-5 descendant; the implementor and
  orchestrator may not edit it. This supersedes earlier progress language that
  called the test itself immutable, without rewriting that history.
- Verification identity: reuse only
  `c3-b1-semantic-fixture-verifier-1` for a complete fresh round. It may edit
  only `tests/verification/test_c3_b1_semantic_fixture_candidate.py` to replace
  the two proven-stale assertions, and create only
  `docs/reviews/c3-b1-semantic-fixture-verification-round-5.md`. It cannot
  repair candidate paths. Its record binds candidate plus verification-test
  before/after digests and verdict exactly `pass` or `changes_required`; no
  earlier pass or finding transfers.

### Semantic-fixture verification round 5

- Tested candidate/tree: `38276fcd8878da84c5e2b7f30e4de275f88a91b6` /
  `ca5b3e6489f3f0285c60e4374911ca4b2b1b39a1`.
- Verifier/verdict: `c3-b1-semantic-fixture-verifier-1` /
  `changes_required`; immutable record and source-adjudicated verification
  artifact committed together at `5acf903`. The corrected verifier digest is
  `e7081c043c790223d07b76724d6b5f73cca6c1d185635b0ad18f591bbd7a5cf9`.
- Fresh passes: all earliest-event schedules; SPI no-CS/CS/order and literal
  newest-first recurrence at 170/180; provenance/declarations/sentinels;
  option-matrix structure and direct reasoning; per-decoder file-set identities;
  all v1 objects/bytes; all 17 cap derivations; generator/no-oracle/exclusions.
  None transfers to a changed candidate.
- Exact remaining defects: the all-low BREAK fixture's scalar/annotation/binary
  outputs say zero while its nested bit triples still encode A5; and full I2C's
  newly preserved partial data event at sample 370 increments `pdu_bits` to 17,
  making metadata `int(1152000 * 17 / 371) = 52787` rather than 49681.
- Correction owner remains
  `c3-b1-semantic-fixture-implementor-replacement-6`, limited to these two
  fixture defects and dependent generator/artifact/cap/test/doc rebuild. No
  decoder runs, no immutable verification artifact is edited, and no pass
  transfers. A new candidate and complete fresh verification are required.

### Corrected semantic-fixture candidate and verification round 6

- Candidate commit/tree: `9f0fe7e45cde49f69b22d266c36932407c3d4845` /
  `01c352da8e6d6807941e5a37434f02b53b973f20`; worktree clean immediately
  after commit. Candidate owner remains
  `c3-b1-semantic-fixture-implementor-replacement-6`; all prior candidates,
  verdicts, and the corrected round-5 verifier artifact remain immutable.
- Exact correction: the BREAK fixture's nested ordinary-list bit triples now
  encode eight zero values consistently with its scalar, annotation, and
  binary outputs. The full I2C fixture now includes the source-required
  post-NACK partial data bit in `pdu_bits`, yielding
  `int(1152000 * 17 / 371) = 52787`. Generator source, generated semantic
  fixture, manifest digests, and focused implementation assertions were
  updated; the cap artifact was deterministically unchanged.
- Root focused result: deterministic generator check, 17 implementation plus
  corrected-verifier tests, Ruff, diff check, exact four-path scope, direct
  generated-value inspection, and checked-in I2C source recurrence passed.
  No decoder, host/helper runtime, reference runtime, network, hardware, or
  prohibited dependency executed.
- Verification identity: reuse only
  `c3-b1-semantic-fixture-verifier-1` (`/root/c3_b1_fixture_verify`) in its
  original verifier role for a complete fresh audit of this exact candidate.
  It may create only
  `docs/reviews/c3-b1-semantic-fixture-verification-round-6.md`; the corrected
  verifier test is now immutable and candidate paths cannot be repaired. The
  record must bind the exact candidate commit/tree and issue exactly `pass` or
  `changes_required`. No earlier pass or finding transfers without fresh
  proof.

### Semantic-fixture verification round 6

- Tested candidate/tree: `9f0fe7e45cde49f69b22d266c36932407c3d4845` /
  `01c352da8e6d6807941e5a37434f02b53b973f20`.
- Verifier/verdict: `c3-b1-semantic-fixture-verifier-1` /
  `changes_required`; immutable record committed at `4193539` in
  `docs/reviews/c3-b1-semantic-fixture-verification-round-6.md`, record SHA-256
  `d7a4538b838e0467e4b6ca77b1d02878c058c5a9f2638308a192e5aa0695a42a`.
- Fresh passing evidence: both round-5 corrections; all 57 complete protocol
  timelines and waits; generator and every digest/file-set recomputation; all
  declarations, sentinels, v1 vectors and literal bytes; all 17 static cap
  derivations; five edge decisions; independence and exclusions. None
  transfers to a changed candidate.
- Required correction: add the exact helper-initializer relative `.mod` edge
  to the closed import inventory. Complete the UART delimiter matrix with
  accepted RX/TX maxima 31, 63, and 127 for selected widths 5, 6, and 7, and
  represent every width-dependent accepted/rejected boundary under the real
  checked-in option key with explicit selected-width context rather than a
  synthetic option name. Every accepted row needs its contract-valid named
  direct witness or source-justified static equivalence; rebuild all dependent
  fixtures, caps, digests, prose, and strong assertions.
- Correction owner remains
  `c3-b1-semantic-fixture-implementor-replacement-6`, confined to its original
  fixture-owned paths. It may not edit verification records/artifacts,
  progress/contracts, runner/product paths, or immutable history. No decoder
  or prohibited runtime may execute. A new candidate and complete fresh
  verification are mandatory; no pass transfers.

### Complete semantic-fixture candidate and verification round 7

- Candidate commit/tree: `6dfe8afae6b121902ce3fde4fe81d335581e6292` /
  `fc020d74e24646fc022f342dda8dafc72c929890`; worktree clean immediately
  after commit. Candidate owner remains
  `c3-b1-semantic-fixture-implementor-replacement-6`; immutable candidate and
  review history is preserved.
- Correction: the closed import inventory now explicitly records
  `common.srdhelper.mod (relative package import .mod)`. UART RX/TX delimiter
  maxima 31/63/127/255/511 now have real option keys, explicit selected
  `data_bits` 5-9 contexts, and ten source-derived direct witnesses; all
  contextual max-plus-one/type/sentinel rejections use the same real keys and
  contexts, with no synthetic width option. Dependent fixtures, cap bases and
  finite values, digests, prose, and strong assertions were rebuilt.
- Corpus/root focused result: 63 unique finite timelines, 165 unique matrix
  rows (62 direct, 103 unsupported), 40 contextual delimiter rows, all 17 cap
  derivations, deterministic generator/check, 17 implementation plus immutable
  corrected-verifier tests, Ruff, diff check, exact eight-path scope, and
  direct RX/TX scalar/bit/binary/packet-output inspection passed. No decoder or
  prohibited runtime executed.
- Verification identity: reuse only
  `c3-b1-semantic-fixture-verifier-1` in its verifier role for a complete fresh
  audit of this exact candidate. It may create only
  `docs/reviews/c3-b1-semantic-fixture-verification-round-7.md`; candidate and
  verifier-test paths are immutable. The record must bind the exact commit/tree
  and issue exactly `pass` or `changes_required`. No prior pass transfers.

### Semantic-fixture verification round 7

- Tested candidate/tree: `6dfe8afae6b121902ce3fde4fe81d335581e6292` /
  `fc020d74e24646fc022f342dda8dafc72c929890`.
- Verifier/verdict: `c3-b1-semantic-fixture-verifier-1` /
  `changes_required`; immutable record committed at `8659bab` in
  `docs/reviews/c3-b1-semantic-fixture-verification-round-7.md`, record SHA-256
  `e5dfa663264e1eae5885686982a7d2a0aa8525cb4d0e9f7746c1406c2568c3c5`.
- Fresh passing evidence: the exact import graph including helper `.mod`; all
  63 finite timelines and 165 contextual matrix rows; provenance/notices/file
  sets; sentinels; deterministic rebuild; all 17 rebuilt caps; no-oracle,
  prohibited-runtime, and scope audits. None transfers to a changed candidate.
- Exact remaining defect: checked-in UART annotation declarations say
  `RX parity error bit` and `TX parity error bit`, while the generator omits
  ` bit`. The mismatch propagates to declarations in all 54 UART timelines and
  all 10 UART-bound v1 objects/canonical goldens. IDs, indices, rows, and
  record classes are otherwise correct.
- Correction owner remains
  `c3-b1-semantic-fixture-implementor-replacement-6`, limited to the two exact
  declaration strings, all deterministically dependent fixture/v1/cap/digest
  outputs, and source-bound strong assertions within original fixture paths.
  It may not edit immutable review/verifier/governance or runner/product paths.
  No decoder runs and no pass transfers; a new candidate and full fresh
  verification are required.

### Source-bound semantic-fixture candidate and verification round 8

- Candidate commit/tree: `c1420ad9b4309fc7417acbc228085b68237c24d0` /
  `26ef344bfb76bec4a8e68be06a411b4d27d20de1`; worktree clean immediately
  after commit. Candidate owner remains the fixture-only replacement-6
  identity and all earlier candidates/verdicts remain immutable.
- Exact correction: generator declarations now transcribe source-exact
  `RX parity error bit` and `TX parity error bit`. All 54 UART timeline
  declarations and 10 UART-bound v1 roots/canonical bytes were regenerated.
  An AST-only implementation assertion reads the checked-in source as inert
  data and binds its indices 6/7 to every generated declaration. The updated
  724292-byte corpus deterministically rebuilds its three byte-derived cap
  values and manifest digests.
- Root focused result: generator/check; 18 implementation plus immutable
  corrected-verifier tests; Ruff; diff and exact six-path scope; source AST,
  timeline/v1 declaration, canonical-byte, digest, and cap arithmetic checks
  passed. No decoder or prohibited runtime executed.
- Verification identity: reuse only
  `c3-b1-semantic-fixture-verifier-1` for a complete fresh audit of this exact
  candidate. It may create only
  `docs/reviews/c3-b1-semantic-fixture-verification-round-8.md`, may repair
  nothing, and must bind the exact commit/tree with verdict exactly `pass` or
  `changes_required`. No prior pass transfers.

### Semantic-fixture verification round 8 and accumulated-gate assignment

- Tested candidate/tree: `c1420ad9b4309fc7417acbc228085b68237c24d0` /
  `26ef344bfb76bec4a8e68be06a411b4d27d20de1`.
- Verifier/verdict: `c3-b1-semantic-fixture-verifier-1` / `pass`; immutable
  record committed at `fa85b83` in
  `docs/reviews/c3-b1-semantic-fixture-verification-round-8.md`, record SHA-256
  `9e1ad275730f30ff1ccbaf3c8e0a59e06c98463d332f249e46b4242be2d18bd5`.
  All eight fresh audit areas passed with no discrepancy; no decoder ran.
- Accumulated subject remains exact candidate/tree above. Descendant review
  and progress commits may add evidence only; every candidate/fixture/test path
  must remain byte-identical. Root-owned result path is fixed as
  `docs/reviews/c3-b1-semantic-fixture-accumulated-validation-round-1.md`.
- Clean environment: managed CPython 3.12.13 creates/clears stable
  `/private/tmp/cycle3-clean-python`; install `requirements-dev.lock` with
  `--require-hashes`, then editable product with `--no-build-isolation
  --no-deps`. Dependency installation is a root-brokered approval class.
- Mandatory commands: clean bootstrap and `pip check`; full `ruff check .`;
  strict `mypy src`; all `pytest -m "not hardware"`; installed module help;
  deterministic Cycle 3 fixture rebuild plus focused implementation/verifier
  suite; all six accepted Cycle 2 evidence-validator invocations; accepted
  Cycle 1 manifest JSON/identity preservation; exact decoder/helper digests and
  closed AST imports; scoped dependency/import/command and active-process
  exclusion audit; candidate-path quiet diff, full repository diff check, and
  clean/qualified state.
- This gate tests no executable cap enforcement and runs no decoder, runner,
  reference runtime, hardware, browser, network service, or excluded action.
  A failure remains at the fixture accumulated gate; acceptance is assigned
  only after every mandatory result passes and the immutable result is
  committed.

### Semantic-fixture accumulated pass and acceptance assignment

- Recorded: `2026-08-27T02:19:17Z`.
- Exact fixture candidate/tree remains
  `c1420ad9b4309fc7417acbc228085b68237c24d0` /
  `26ef344bfb76bec4a8e68be06a411b4d27d20de1`; every candidate-owned path is
  unchanged in its review/progress descendants.
- Root accumulated validation passed with no failed or mandatory skipped gate.
  Its immutable record is committed at `ef43dc7` in
  `docs/reviews/c3-b1-semantic-fixture-accumulated-validation-round-1.md`,
  SHA-256
  `c4aec32157039cdcc3680d1bb430c2bc4d407a571c7e335f856f1f7c633241e6`.
  The clean hash-locked Python gate proves all 403 collected non-hardware
  tests; Ruff, strict mypy, installed help, deterministic fixture rebuild,
  focused fixture/verifier tests, Cycle 1/2 evidence validation, digest/import/
  dependency/process/scope audits, and unchanged frontend/browser/performance
  regressions all passed. No decoder or prohibited runtime executed.
- Assigned acceptance identity:
  `c3-b1-semantic-fixture-acceptance-1` (`/root/c3_b1_fixture_accept`), distinct
  from both fixture and runner implementors, the fixture verifier, the primary
  orchestrator, and every later manifest verifier. Lane/model/reasoning:
  acceptance, `gpt-5.6-sol`, low.
- The acceptance subject is only the exact fixture candidate/tree above, its
  immutable round-8 verification, accumulated-validation record, correction
  history, scope, provenance/notices, cap-specification completeness and finite
  values, evidence ordering, and readiness to begin the distinct runner
  candidate. Executable cap enforcement is explicitly outside this fixture
  review and remains unclaimed.
- The acceptance identity may create only
  `docs/reviews/c3-b1-semantic-fixture-acceptance-round-1.md`, may repair
  nothing, must not edit candidate/tests/progress/contracts, and must report
  exactly `pass` or `changes_required`. It must not run a decoder, runner,
  C#/.NET/pythonnet/libsigrokdecode/sigrok runtime, hardware, network install,
  or any excluded action. A `pass` authorizes only the next ordered internal
  B1 runner candidate; it does not authorize decoder execution, create a B1
  manifest/checkpoint, or transfer to a changed fixture candidate.

### Semantic-fixture acceptance pass and pre-execution-runner assignment

- Recorded: `2026-08-27T02:23:55Z`.
- Fixture acceptance identity/verdict:
  `c3-b1-semantic-fixture-acceptance-1` / `pass`; immutable record committed at
  `5d2f800a3c4e0912031eb27580d8c858ba92c4c9` in
  `docs/reviews/c3-b1-semantic-fixture-acceptance-round-1.md`, SHA-256
  `99a209b07078913cd6a741485e97c863c5e1505cef1e0e581bc5b09807259598`.
  It found no discrepancy and accepts only exact fixture candidate/tree
  `c1420ad9b4309fc7417acbc228085b68237c24d0` /
  `26ef344bfb76bec4a8e68be06a411b4d27d20de1` for entry into the distinct
  runner phase. It makes no executable-enforcement, decoder-execution,
  characterization, legal, threshold, manifest, or checkpoint claim.
- Runner assignment starts from committed acceptance descendant/tree
  `5d2f800a3c4e0912031eb27580d8c858ba92c4c9` /
  `4890d67e2907dc515e089d94dadd917b71cad274`; worktree is clean.
- Assigned implementation identity:
  `c3-b1-pre-execution-runner-implementor-1` (`/root/c3_b1_runner_impl`),
  distinct from the fixture implementor/verifier/acceptance identities and all
  planned runner verifier/acceptance identities. Lane/model/reasoning:
  implementor, `gpt-5.6-terra`, low.
- Bounded objective: create the actual non-installed characterization runner,
  measurement method, exact launch/import configuration, cap/cleanup plumbing,
  and closed internal inert/hostile probe surface. The immutable candidate must
  bind the accepted fixture/cap digests; runner/method/config/probe digests;
  exact Python executable and arguments, environment and working directory;
  closed import root/allowlist and pre-launch digest checks; length-framed
  request/result transport; all 17 accepted experiment-cap values and every
  enforcement path; graceful terminate then force-kill order; pipe/descriptor
  closure; exact-child reap; and a valid probe after failure. Probe mode must
  not be caller-selectable and must be disabled for later characterization.
- Owned paths are only `tools/cycle3_characterize/`,
  `docs/cycle-3-characterization-method.md`, and
  `tests/implementation/test_cycle3_preexecution_runner.py` beneath
  `Software/LogicAnalyzerPy/`. No raw observation may be created yet; the
  separately ordered `testdata/decoders/cycle3-raw/` surface remains unopened.
  The implementor must not change accepted fixture/cap/generator/test bytes,
  decoder/shim/helper snapshots, product source/API/CLI, locks, workflows,
  reviews, progress/contracts, evidence schema/manifest, or Cycle 1/2 evidence.
- Focused implementation proof may execute only the candidate's inert/hostile
  non-decoder probes. It must cover all cap categories and accept/reject
  boundaries; digest/import-root/file/symlink/shadow/environment/CWD rejection;
  framing/malformed/partial/extra/non-finite data rejection; graceful and
  forced termination; stdout/stderr/diagnostic containment; pipe/descriptor
  close; exact-child reap; retained-result cleanup; and recovery with a valid
  probe after every failure. It must statically prove the decoder/helper files
  remain inert and no probe imports fixture generation or expected outputs.
- This assignment authorizes no decoder, compatibility shim/helper, product
  host, C#, .NET, pythonnet, libsigrokdecode, sigrok runtime, hardware,
  network install, raw characterization, threshold proposal, package placement,
  publication, excluded scope, or Cycle 4 action. A clean local stdlib-only
  Python 3.12 command shape and existing reusable root-broker approvals must be
  used; the implementor may not request escalation directly.
- Handoff requires a focused failing check, smallest owning implementation,
  Ruff and focused tests passing, explicit command/results and digest map,
  exact scope/status, no-decoder/process audit, and no open finding. The root
  orchestrator alone integrates and commits the immutable runner candidate;
  afterward a fresh distinct runner verifier receives only one fixed
  verification-record path and may repair nothing. No fixture pass transfers
  to runner enforcement.

### B1 project/license disposition review assignment

- Assigned: `2026-08-27T02:26:31Z` from clean orchestration commit `cac51ef`.
- Identity: `c3-b1-project-license-reviewer-1`
  (`/root/c3_b1_legal_review`), independent review lane, `gpt-5.6-sol`, low;
  distinct from every B1 implementation, verification, acceptance, manifest,
  and orchestration identity.
- Bounded objective: settle the repository's engineering package-placement,
  notice, attribution-manifest, license-text, and Python metadata disposition
  for the exact nine-file GPL-2.0-or-later decoder/shim/helper set, while
  preserving every observed source notice and the repository's existing GPLv3
  text. The review must use authoritative primary licensing and Python
  packaging sources, separate factual compatibility/metadata requirements from
  legal advice, and make no publication or distribution claim.
- The reviewer owns only
  `docs/reviews/c3-b1-project-license-review-round-1.md`. It may inspect exact
  source bytes, history, current metadata, accepted provenance artifacts, and
  authoritative public documentation; it may repair nothing and may not edit
  package/product/fixture/runner/test/lock/workflow/governance/evidence paths.
  The record must bind exact file/digest identities, state the precise future
  private package placement, retained notices/attribution/license files and
  metadata changes required before snapshots enter an installed distribution,
  list unresolved external-counsel limitations without using them to simulate
  a conclusion, and end exactly `pass` or `changes_required`.
- No decoder, runner, C#/.NET/pythonnet/libsigrokdecode/sigrok runtime,
  dependency install, hardware, package build/publication, or Cycle 4 action is
  authorized. This static review can proceed in parallel with the non-decoder
  runner implementation; neither result transfers to the other.

### Pre-candidate runner integration review round 1

- Recorded: `2026-08-27T02:30:55Z`. State: `changes_required`; no immutable
  pre-execution-runner candidate, verifier, accumulated, or acceptance result
  exists, and no fixture pass transfers to runner enforcement.
- Initial bounded implementation stayed within the three assigned path
  families and executed only inert probes. Focused pytest reported 11 passes;
  focused Ruff and diff check passed. No decoder or prohibited runtime ran.
- C3B1-RI001: `FIXTURE_MANIFEST_SHA256` is empty and launch validates only the
  cap artifact. It does not pre-launch validate the accepted fixture manifest,
  nine exact decoder/helper files and ordered file sets, runner, worker,
  method, launch configuration, or probe-inventory digests.
- C3B1-RI002: `launch.json` does not bind the exact executable/`-I` arguments,
  worker, closed file/import root and allowlist, accepted artifact identities,
  digest map, probe-source identities, or characterization-disabled probe
  state. Root/symlink/traversal/shadow/namespace/bytecode/environment/CWD
  rejection is absent.
- C3B1-RI003: only framing, record count, text/binary string bytes, process
  deadline/grace, and post-capture stdout/stderr checks are partial. Input
  samples, decoded bytes, diagnostic accounting, nesting/items, recursion,
  retained result, worker address space, and concrete output/value categories
  lack enforcement. `communicate()` accumulates output before size checks, so
  stdout/stderr and related memory caps do not contain a hostile worker.
- C3B1-RI004: the inert/hostile matrix has nine probes and no exact accept/
  reject boundary for every cap, digest/import/file/root/environment/CWD case,
  malformed request/result family, resource path, descriptor path, graceful
  versus forced termination proof, exact-child reap proof, or retained-state
  recovery assertion. The method overstates all-17-cap enforcement while
  acknowledging five categories as merely reserved.
- Disposition: return to the same runner implementor because no candidate has
  been committed and role ownership remains intact. Complete the exact
  candidate binding and bounded streaming/resource enforcement; strengthen
  focused assertions so each required invariant fails independently; correct
  method claims; rerun the full focused matrix and static no-decoder/process/
  scope audits. The corrected work remains pre-candidate and may run only
  non-decoder probes. No verifier is assigned until root integration finds no
  open requirement.

### B1 project/license disposition review result

- Recorded: `2026-08-27T02:32:32Z`.
- Reviewer/verdict: `c3-b1-project-license-reviewer-1` / `pass`; immutable
  record committed at `538a4aa669a782919dafefb26a81d7346ed45f5c` in
  `docs/reviews/c3-b1-project-license-review-round-1.md`, SHA-256
  `b7afc4df18ba9bf5e40ee5a795e4544e54a59be27b1fea9a8617681ea82919cf`.
- The engineering disposition binds all nine exact source digests, import
  commit/prior gitlink, observed notices, current MIT metadata, and repository
  GPLv3 text. Authoritative GNU/FSF, SPDX, and PyPA sources support a future
  private commit-pinned snapshot-data root; retained source headers; exact
  attribution manifest; GPLv2/GPLv3/MIT component texts; distribution-level
  `GPL-3.0-only` metadata; bounded package-data patterns; and clean artifact/
  install verification before any installed exposure.
- No source/package/metadata change, editable snapshot exposure, build, wheel,
  sdist, upload, publication, or decoder execution is authorized or claimed by
  the record. The shim's missing in-file notice and present MIT authority must
  receive rights-holder or qualified-counsel confirmation before conveyance;
  absent or negative confirmation keeps build/distribution prohibited. This is
  an explicit engineering compliance disposition and limitation, not a legal
  guarantee.
- The record is an accepted ordered B1 input. Its prescribed source-side
  placement/metadata changes and static validation belong to the later owning
  product/package gate before snapshots can enter an installed distribution;
  they do not alter or unblock the current non-installed, non-decoder runner
  probe gate.

### Pre-candidate runner integration review round 2 and identity replacement

- Recorded: `2026-08-27T02:37:05Z`. State remains `changes_required`; no
  candidate or runner-gate verdict exists. Initial implementor
  `c3-b1-pre-execution-runner-implementor-1` remained in scope and correctly
  declined candidate readiness, but exhausted its implementation turns before
  completing RI003/RI004.
- C3B1-RI005: the protocol currently shares stdout even though accepted
  `stdout_bytes=193152` is smaller than `encoded_bytes=6180864`; that makes the
  encoded-result domain unreachable and conflates protocol with diagnostic
  containment. The corrected design requires a separately inherited bounded
  protocol pipe/descriptor, with stdout and stderr independently captured and
  bounded, explicit diagnostic accounting, and all streams closed/reaped.
- C3B1-RI006: the surface exposes only `run_internal_probe`; it lacks the exact
  later characterization entry point/request shape that will execute only the
  closed approved snapshot set after the runner gate passes. The immutable
  candidate must contain and bind that real path with internal probe mode
  disabled, even though only probes may execute before acceptance.
- Replacement identity:
  `c3-b1-pre-execution-runner-implementor-replacement-1`
  (`/root/c3_b1_runner_impl_r2`), implementor lane, `gpt-5.6-terra`, low. It is
  distinct from every fixture/verifier/acceptance/manifest/orchestration role,
  inherits only the original three path families, and may replace incomplete
  uncommitted runner work. The original identity remains immutable history and
  authors no expected fixture.
- The replacement must close RI001-RI006, remove incomplete/dead paths and
  overclaims, and produce strong focused proof for every candidate invariant.
  It may run only inert/hostile non-decoder probes and may not create a raw
  observation. Root will not commit or assign verification until the complete
  worktree is independently integration-reviewed with no open requirement.

### Pre-candidate runner integration review round 3

- Recorded: `2026-08-27T02:45:38Z`. State remains `changes_required`; the
  replacement produced a useful dedicated-protocol prototype with 15 focused
  passes but explicitly withheld candidate readiness. No verifier is assigned.
- C3B1-RI007: binding v2 lists only launch/runner/worker. It omits method,
  probes, accepted cap/fixture/provenance artifacts, and all nine exact source
  files; it permits an empty launch allowlist, does not verify the configured
  executable, and trusts binding-selected paths instead of requiring one exact
  closed set. Directory-component symlink/root/shadow/bytecode constraints are
  not proven.
- C3B1-RI008: worker recursion and address-space limits remain unset. Decoded
  bytes are treated as a canonical re-encoding, retained memory as raw frame
  length, binary bytes as UTF-8 string length, and diagnostics as a truncated
  stderr copy rather than distinct enforced counters. Production-only caps
  still lack safe exact-boundary profiles and independent assertions.
- C3B1-RI009: the deep probe adds an unknown top-level field and is rejected by
  shape before depth is audited; the item probe primarily tests record count.
  No recursion/address-space/input/request/decoded/retained/text/binary/
  diagnostic accept-plus-one matrix exists. The future `characterize()` path
  validates only five shallow request fields then unconditionally fails; it
  does not yet define the closed exact file-set launch request consumed by the
  same worker with probe selection absent.
- C3B1-RI010: `# ruff: noqa`, dense one-line implementation, dead `_collect`,
  and missing focused type coverage hide defects, including the invalid
  `float.is_finite()` call. Passing Ruff under a file-wide waiver is not an
  acceptable gate. The corrected candidate must be maintainable, type-checked,
  and contain no broad lint suppression or dead pre-candidate path.
- Disposition: keep the same replacement identity for a fresh correction turn;
  finish RI001-RI010, refresh all non-self digests only after stable code/docs,
  and rerun the expanded matrix. The work may execute only non-decoder probes
  and remains uncommitted until root finds no open requirement.

### Runner enforcement discovery reopens semantic-fixture cap candidate

- Recorded: `2026-08-27T02:56:04Z`. State: semantic-fixture correction in
  progress; runner work paused before any candidate. Exact fixture candidate
  `c1420ad9b4309fc7417acbc228085b68237c24d0` remains immutable history, but its
  round-8 verification, accumulated, and acceptance passes no longer authorize
  subsequent work because one accepted cap is not enforceable on the governed
  environment class.
- C3B1-RI011: accepted `worker_address_space_bytes=2966700032` is below the
  freshly launched managed CPython 3.12.13 macOS-x86_64 virtual-address-space
  baseline. A clean inert Python child measured `34272160` KiB VSZ
  (`35094691840` bytes) and 9440 KiB RSS before importing any decoder. Exact
  `resource.setrlimit(RLIMIT_AS, (2966700032, 2966700032))` fails before request
  parsing with `ValueError: current limit exceeds maximum limit`; silently
  skipping, relabelling as RSS/data/growth, or accepting cap termination would
  weaken/change the frozen cap and is prohibited.
- Feasibility boundary: exact `RLIMIT_AS` of `68719476736` bytes (64 GiB) sets
  successfully in the same managed Python environment. This is discovery input
  only, not an approved replacement cap. The fixture owner must derive one
  conservative exact finite macOS-x86_64 address-space floor, regenerate every
  dependent cap/manifest/digest/prose/assertion, and preserve accept-at-value /
  reject-at-value-plus-one semantics. The corrected cap still makes no runtime
  or product-threshold claim.
- Ordered invalidation: semantic-fixture verification round 8, accumulated
  round 1, and acceptance round 1 remain historically accurate for their exact
  old candidate but transfer no pass. Project/license review remains an
  independent unchanged static input. No pre-execution-runner candidate,
  verifier, accumulated result, acceptance, decoder execution, raw observation,
  or threshold exists.
- Correction owner is the existing fixture-only identity
  `c3-b1-semantic-fixture-implementor-replacement-6`; it may edit only its
  original fixture-owned paths and may not touch runner/review/progress/product/
  contract paths. A fresh immutable fixture candidate, complete independent
  verification, accumulated validation, and acceptance are mandatory before
  runner implementation resumes.
- The uncommitted runner prototype was moved intact outside the repository for
  later adaptation; the repository is clean. It is not evidence, a candidate,
  or an accepted implementation, and none of its old-cap digests/results may
  transfer.

### Enforceable semantic-fixture cap candidate and verification round 9

- Recorded: `2026-08-27T03:02:17Z`.
- New immutable candidate commit/tree:
  `7c57a347bbe575e3f451383ea498f56abc362f26` /
  `02a408895dd834e6e6885218cb7323f46439e880`; worktree clean immediately after
  commit. Owner remains fixture-only implementor replacement-6. All earlier
  candidate/verdict history is preserved and no old pass transfers.
- Exact correction: `worker_address_space_bytes` is now `68719476736` bytes
  (64 GiB), derived as `max(724292 * 4096, 68719476736)`. Its JSON and prose
  identify an absolute macOS-x86_64 managed-CPython `RLIMIT_AS` compatibility
  ceiling, not RSS/data/growth, runtime baseline, product threshold, or
  enforcement claim; boundary remains accept=value/reject=value+1. Exact
  64-GiB setrlimit feasibility passed on the governed managed Python while the
  old value is a strong rejected regression.
- Only semantic-fixture prose, generator, cap artifact, fixture manifest, and
  implementation assertions differ from candidate `c1420ad`; all semantic
  timelines, expected records, option matrix, typed vectors/goldens,
  provenance/file sets/notices, and immutable verifier tests are byte-identical.
  Updated SHA-256: generator
  `6fc5289ba1076413283942be0374bd97def08b284bf7a7cef4e7b6105636be63`, cap
  `63cde36892a15a390be0c27c50eac18431d7a4b11381b0e4b82c0fe64f808cd8`,
  fixture manifest
  `0f5f1d9a01fc807dd0f4078ac84b20158f515a76ae4f1f83cc74651c4797413a`.
- Root focused results: deterministic generator check; 18 implementation plus
  immutable verifier tests; focused Ruff; exact five-path scope; and repository
  diff check passed. Only inert Python/RLIMIT feasibility and static fixture
  processing ran; no decoder, runner candidate, helper/product/prohibited
  runtime, raw characterization, hardware, or excluded action executed.
- Verification assignment: reuse only
  `c3-b1-semantic-fixture-verifier-1` (`/root/c3_b1_fixture_verify`) for a
  complete fresh audit of this exact candidate. It must independently re-audit
  every prior semantic/provenance/coverage/determinism area plus RI011's
  platform-floor derivation, exact setrlimit feasibility, absolute address-space
  semantics, boundary, and non-claim wording. It may create only
  `docs/reviews/c3-b1-semantic-fixture-verification-round-9.md`, may repair
  nothing, and must end exactly `pass` or `changes_required`. No decoder or
  prohibited runtime may execute and no prior verifier result transfers.

### Semantic-fixture verification round 9 and accumulated-gate reassignment

- Recorded: `2026-08-27T03:11:46Z`.
- Tested candidate/tree: `7c57a347bbe575e3f451383ea498f56abc362f26` /
  `02a408895dd834e6e6885218cb7323f46439e880`.
- Verifier/verdict: `c3-b1-semantic-fixture-verifier-1` / `pass`; immutable
  round-9 record committed at `8b08f7d` in
  `docs/reviews/c3-b1-semantic-fixture-verification-round-9.md`, SHA-256
  `3e2f507332fdfc82e8e49df016b66db223508144677cc5166d8a4e090d0378c6`.
  Complete fresh semantic/provenance/option/vector/cap/scope audit passed with
  no discrepancy: 63 timelines, 1,058 waits, 1,049 records, 165 option rows,
  12 v1 roots/goldens, 17 caps, and nine source files. Managed-CPython inert
  feasibility independently proved VSZ `35113566208`, exact old-cap failure,
  and exact corrected 64-GiB `RLIMIT_AS` set/readback. No decoder ran.
- Root accumulated validation is reassigned to this exact candidate. All
  mandatory clean Python, fixture, Cycle 1/2 evidence, frontend/browser/
  performance regression, dependency/import/process/scope, candidate-path,
  and clean/qualified worktree gates from round 1 must run freshly; no old
  result transfers merely because only cap-owned bytes changed.
- Root result path is fixed as
  `docs/reviews/c3-b1-semantic-fixture-accumulated-validation-round-2.md`.
  It must bind the new cap/manifest/generator/test/document digests, prove exact
  64-GiB setrlimit feasibility without executing a decoder, record every
  command/result and old-pass invalidation, and issue only `pass` or failure.
  Fixture acceptance is assigned only after this immutable accumulated result
  passes and is committed.
