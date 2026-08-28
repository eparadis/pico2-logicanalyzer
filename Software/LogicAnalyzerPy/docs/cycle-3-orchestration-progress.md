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

### Corrected fixture accumulated pass and acceptance round 2 assignment

- Recorded: `2026-08-27T03:21:13Z`.
- Exact subject remains candidate/tree
  `7c57a347bbe575e3f451383ea498f56abc362f26` /
  `02a408895dd834e6e6885218cb7323f46439e880`; candidate-owned paths are
  unchanged in every descendant.
- Fresh root accumulated validation passed and is committed at `bdd5e5a` in
  `docs/reviews/c3-b1-semantic-fixture-accumulated-validation-round-2.md`,
  SHA-256
  `196b07bf214adddb70b094c30402d706415f183f4451beb82e6bf0ee2d6162ac`.
  A cleared hash-locked Python 3.12.13 environment produced 403/403 non-
  hardware passes with no skip, Ruff, strict mypy, installed help,
  deterministic fixtures and 18 focused passes; all Cycle 1/2 evidence,
  Node 22 lint/type/unit/build/browser/performance, exact 64-GiB setrlimit,
  dependency/import/process/scope, candidate-path, diff, and clean-state gates
  passed. No decoder or prohibited runtime executed.
- Reassigned acceptance identity is the same independent
  `c3-b1-semantic-fixture-acceptance-1` (`/root/c3_b1_fixture_accept`) for a
  complete fresh audit. It must bind the corrected candidate, round-9
  verification, accumulated round 2, RI011 discovery/correction, invalidation
  ordering, immutable prior history, project/license input, and runner-phase
  readiness. No old acceptance finding/pass transfers.
- The acceptance identity may create only
  `docs/reviews/c3-b1-semantic-fixture-acceptance-round-2.md`, may repair
  nothing, and must end exactly `pass` or `changes_required`. It must
  independently audit the 64-GiB absolute-address-space derivation/feasibility/
  qualification and all original fixture acceptance areas, execute no decoder
  or prohibited runtime, and make no runner-enforcement/characterization/
  threshold/manifest/checkpoint claim. Only a fresh `pass` may resume the
  quarantined distinct runner implementation.

### Corrected fixture acceptance pass and runner implementation resumption

- Recorded: `2026-08-27T03:25:21Z`.
- Acceptance identity/verdict: `c3-b1-semantic-fixture-acceptance-1` / `pass`;
  immutable round-2 record committed at `0074c67` in
  `docs/reviews/c3-b1-semantic-fixture-acceptance-round-2.md`, SHA-256
  `9b0a9fcabed2b1a3636bb1c32df8ecf3aca590732e728ee6aacb004c85b018af`.
  No discrepancy remains. Authority is limited to resuming the distinct
  pre-execution-runner candidate and transfers to no changed fixture.
- Active runner owner remains
  `c3-b1-pre-execution-runner-implementor-replacement-1`
  (`/root/c3_b1_runner_impl_r2`), distinct from all fixture, verifier,
  acceptance, manifest, and orchestration identities. Its original three path
  families and every prohibition remain unchanged.
- The quarantined uncommitted prototype may be restored only as non-evidence
  implementation input. No old cap digest, test result, feasibility failure,
  binding, or partial RI001-RI010 disposition transfers. The replacement must
  bind corrected candidate `7c57a347bbe575e3f451383ea498f56abc362f26`, cap SHA
  `63cde36892a15a390be0c27c50eac18431d7a4b11381b0e4b82c0fe64f808cd8`,
  fixture manifest SHA
  `0f5f1d9a01fc807dd0f4078ac84b20158f515a76ae4f1f83cc74651c4797413a`,
  and exact accepted 64-GiB absolute address-space ceiling.
- Correction objective remains the complete immutable runner candidate:
  maintainable closed binding/launch/request paths, separate bounded protocol/
  stdout/stderr/diagnostic streams, concrete enforcement and exact boundaries
  for all 17 production caps, internal small-profile proof without production
  weakening, macOS `RLIMIT_AS`/recursion, termination/kill/close/exact reap,
  hostile failure recovery, and a real hard-disabled characterization path.
  Every RI001-RI010 finding must be closed with strong focused assertions.
- Only inert/hostile non-decoder probes may execute. No decoder/helper/product
  runtime, raw characterization, package placement, hardware, network install,
  excluded action, or Cycle 4 work is authorized. Root will commit a candidate
  and assign its distinct verifier only after complete integration review finds
  no open requirement.

### Pre-candidate runner implementor replacement 2

- Recorded: `2026-08-27T03:30:02Z`. No immutable runner candidate or verdict
  exists. Replacement-1 correctly kept all work uncommitted and made material
  progress on the corrected-cap binding, dedicated protocol path, worker
  limits, and typed accounting, but exhausted repeated implementation turns
  before completing the proof surface.
- New identity:
  `c3-b1-pre-execution-runner-implementor-replacement-2`
  (`/root/c3_b1_runner_impl_r3`), implementor lane, `gpt-5.6-terra`, low. It is
  distinct from both prior runner implementors and every fixture,
  verification, acceptance, manifest, and orchestration identity. Prior
  implementors remain immutable correction history.
- Replacement-2 inherits only the original three runner path families and may
  freely replace the uncommitted pre-candidate work. It must bind the corrected
  accepted fixture/cap identities and close every RI001-RI010 finding. The
  current accounting module/production wiring, separate protocol stream,
  exact 64-GiB limit, and hard-disabled characterization request are leads,
  not accepted evidence or transferred tests.
- Immediate unfinished surface: complete closed binding/launch allowlists for
  every owned source; finish private derived small-profile execution while
  keeping characterization production-only; normal-format the implementation
  test; add exact value/+1 accounting tests for every cap; finish bounded
  process, termination/kill/descriptor/reap/recovery and hostile root/import/
  resource matrices; update truthful method; and pass focused pytest, Ruff,
  mypy, binding, scope, process, and no-decoder audits without suppression.
- All original prohibitions remain. Only inert/hostile non-decoder probes may
  run; no raw observation or future gate is authorized. Root will assign no
  verifier until a complete independent integration review finds no open
  requirement.

### Pre-candidate runner implementor replacement 3

- Recorded: `2026-08-27T04:12:48Z`. No immutable runner candidate, verifier,
  accumulated result, acceptance, or decoder execution exists. Replacement-2
  materially completed the 17-cap accounting/process boundary, dedicated
  protocol, termination/kill/close/reap evidence, hostile binding/import
  preflight, fixed launch environment, and static fixed-snapshot loader
  foundation, but repeated bounded turns did not finish the required actual
  characterization host or even its mechanically consistent launch binding.
- C3B1-RI012: root integration rejected the apparent 117-test completion
  because `characterize()` unconditionally failed and the worker accepted only
  inert probes. Such bytes cannot be the contract's exact unchanged runner that
  executes the approved snapshots after its non-decoder gate. The correction
  must contain the real fixed UART/SPI/I2C post-gate snapshot path before any
  candidate is committed; static request-builder or label-only tests do not
  close this finding.
- New identity:
  `c3-b1-pre-execution-runner-implementor-replacement-3`
  (`/root/c3_b1_runner_impl_r4`), implementor lane, `gpt-5.6-terra`, low. It
  inherits only the same runner/method/launch/probe/test path families and may
  freely replace the uncommitted pre-candidate work. Replacement-2 remains
  immutable correction history and transfers no pass.
- Immediate objective: finish and statically verify the exact nine-file pinned
  loader, fixed module graph, compatibility lifecycle/wait/register/put host,
  canonical raw observations/counts, closed non-probe characterization request,
  unchanged post-acceptance execution entrypoint, truthful measurement method,
  launch/inventory/binding consistency, and every still-open RI001-RI012
  assertion. It may inspect snapshot bytes only as inert text and may execute
  only inert/hostile non-decoder probes; it must not execute a decoder, expected
  fixture generator, helper/product runtime, hardware, or excluded capability.

### Immutable pre-execution runner candidate and verification assignment

- Recorded: `2026-08-27T04:51:38Z`.
- Candidate commit/tree: `11a8ade5d828830347095bf2580766c149cb8aef` /
  `61fa5ba18f3620188ee61dac7e3622803591aad9`; the candidate worktree was clean
  immediately after commit and contains only the 11 assigned runner/method/test
  paths. Accepted fixture candidate/tree
  `7c57a347bbe575e3f451383ea498f56abc362f26` /
  `02a408895dd834e6e6885218cb7323f46439e880` and every governing byte remain
  unchanged.
- Candidate authorship is the ordered runner-only implementation history
  `c3-b1-pre-execution-runner-implementor-1`, replacements 1 and 2, and final
  owner `c3-b1-pre-execution-runner-implementor-replacement-3`
  (`/root/c3_b1_runner_impl_r4`). Replacement-3 performed the final ownership
  audit and adopted the integrated bytes with no additional edit. No runner
  identity authored accepted expected fixtures.
- RI001-RI012 are closed in the candidate: explicit accepted fixture/cap
  identity, closed non-self binding and launch/source/stdlib inventories,
  exact nine-byte/ordered-set verification, fixed Python 3.12 isolated worker,
  separate bounded protocol/stdout/stderr, all 17 immutable cap paths and
  derived non-weakenable test profiles, exact address-space/recursion limits,
  parent deadline/terminate/kill/close/reap evidence, closed pre-spawn request
  validation, mixed skip/edge API-v3 behavior, deterministic result/count and
  timing evidence, and the real fixed snapshot route reachable only through
  the private post-gate entrypoint. Public `characterize` remains disabled.
- Root and final-implementor focused results: 166 inert/hostile tests passed;
  focused Ruff, strict mypy over seven tool modules, binding regeneration/check,
  source/import/option/wait/scope audits, and repository diff check passed.
  No decoder, snapshot route, helper, fixture generator, product runtime,
  hardware, network, or excluded action executed; no worker remained active.
- Key SHA-256 identities: binding
  `0b9fc2a02eef194c48392db2903c6296e764c0fe9a8368d51c2551c83ed60682`,
  launch `c6cf91ebc42d3770ffc239b531424a128a2cf06c5aa97ed99b980bc48a86c9f8`,
  runner `cd70e895794ace146be5830aeb5fff99a3aaf009c0049eb730e69ab53e5a9d32`,
  worker `69e8eaccad236c6ec746aa5fd2ca11c26ae47f4b7306323c9710e2603ed65be5`,
  snapshot host
  `0da598c3facd1af89d34d6a82996a09a24b0cc4d691eb5c79f0ac576e051ab67`,
  accounting
  `924f563067bb23fc838b9b63b05b7e209f656fab68ee9859df4839f270bbd2d5`,
  probes `be0da3bdc27e0a228b946a339ca278b55466c48d24170552ee8eac3150942f2e`,
  method `eb4349d60aad922381a64579e1584271ec035dfa80d52f16881709b5260e2837`,
  and focused test
  `c97cd9a66b1a5fff6ec72565ca41008bc8874f9a929d01e84b2e582a379a9f4d`.
- Verification is assigned to fresh identity
  `c3-b1-pre-execution-runner-verifier-1`
  (`/root/c3_b1_runner_verify`), verifier lane, `gpt-5.6-sol`, low, distinct
  from every fixture/runner implementor, fixture verifier/acceptance identity,
  project/legal reviewer, primary orchestrator, and later runner acceptance or
  manifest identity. It may add only
  `tests/verification/test_c3_b1_preexecution_runner_candidate.py` and
  `docs/reviews/c3-b1-preexecution-runner-verification-round-1.md`.
- The verifier must independently audit and exercise this exact unchanged
  candidate using only inert/hostile non-decoder probes: every cap at accepted
  and rejected boundaries; digest/import/root/file/symlink/shadow/environment/
  CWD boundaries; framing and result accounting; graceful termination, forced
  kill, every success/failure descriptor close and exact-child reap; recovery
  after each failure; fixed post-gate route structure; accepted option and
  API-v3 semantics; source/method truth; and candidate/scope identity. It may
  repair nothing and must end exactly `pass` or `changes_required`, explicitly
  stating that no decoder or approved snapshot ran. No prior pass transfers.

### Pre-execution runner verification and accumulated pass; acceptance assignment

- Recorded: `2026-08-27T05:05:10Z`.
- Exact runner candidate/tree remains
  `11a8ade5d828830347095bf2580766c149cb8aef` /
  `61fa5ba18f3620188ee61dac7e3622803591aad9`; every candidate-owned path is
  byte-identical in all descendants.
- Independent verifier/verdict:
  `c3-b1-pre-execution-runner-verifier-1` / `pass`; immutable record and 21-test
  independent matrix committed at `8464a049c0809c9f0338c1cf7ad7ac90d1ec19eb`.
  Record SHA-256 is
  `a1ca9a6c75b6bdca682ef00c07a4bb72e48c69d18cc493d05ba812a5bb241024`;
  verifier-test SHA-256 is
  `6dc7f48c7312a318f370c4e98de57aed72cec270e378339ccc44f05bbc15bf7a`.
  The verifier independently exercised the complete inert/hostile cap,
  binding/import, framing/accounting, resource, terminate/kill/close/reap,
  recovery, fixed-route, option, and API-v3 matrix. No decoder or snapshot ran.
- Root accumulated validation/verdict: `pass`, committed at
  `68529f97108f81d352d7a081068ec425719ee7bf` in
  `docs/reviews/c3-b1-preexecution-runner-accumulated-validation-round-1.md`,
  SHA-256
  `2d2fb0281dcf51ffae8c87e4989ca2eb4a9cdf3da91cad220ac836a33af2289d`.
  A fresh hash-locked Python 3.12.13 environment produced 590/590 non-hardware
  passes with no skip, 187 focused passes, Ruff, both mypy scopes, installed
  help, deterministic fixture rebuild, exact 64-GiB set/readback, all Cycle 1/2
  evidence, exact Node 22 lint/type/unit/build/browser/performance, dependency/
  package/import/process/scope, candidate-path, diff, and clean-state passes.
  No decoder, snapshot route, raw characterization, hardware, or prohibited
  runtime executed.
- Acceptance is assigned to fresh identity
  `c3-b1-pre-execution-runner-acceptance-1`
  (`/root/c3_b1_runner_accept`), acceptance lane, `gpt-5.6-sol`, low, distinct
  from every fixture/runner implementor, both fixture and runner verifiers,
  fixture acceptance, project/legal reviewer, primary orchestrator, and later
  manifest identity.
- The acceptance identity may create only
  `docs/reviews/c3-b1-preexecution-runner-acceptance-round-1.md`, may repair
  nothing, and must audit the exact candidate, implementation identity history,
  RI001-RI012 dispositions, verifier and accumulated records/tests, immutable
  ordering, candidate-path equality, complete 17-cap and cleanup proof, fixed
  post-gate route, method truth, accepted fixture/provenance binding, scope, and
  no-decoder claims. It must end exactly `pass` or `changes_required`.
- Acceptance may use only static inspection and inert/hostile non-decoder probes.
  It must not call the private post-gate route or execute a decoder, snapshot,
  helper, generator, product host, hardware, network install, or excluded
  capability. A `pass` authorizes only the exact unchanged runner to enter the
  separately ordered raw-baseline execution phase; no other authority transfers.

### Pre-execution runner acceptance pass and raw-baseline assignment

- Recorded: `2026-08-27T05:11:27Z`.
- Acceptance identity/verdict:
  `c3-b1-pre-execution-runner-acceptance-1` / `pass`; immutable round-1 record
  committed at `fdb3262202fbc8dca5d5115345ddaecdedd150b0` in
  `docs/reviews/c3-b1-preexecution-runner-acceptance-round-1.md`, SHA-256
  `85d6fa54fe9e07c9ed990361dbc1e0536ac1ef3cf5597b36e60e137fb41c3a74`.
  It found no discrepancy, independently reran 21 inert/hostile verifier tests,
  and confirmed exact candidate and fixture byte equality, complete 17-cap and
  cleanup proof, immutable ordering, scope, method truth, and no prior decoder
  or approved-snapshot execution.
- This pass authorizes only exact runner candidate/tree
  `11a8ade5d828830347095bf2580766c149cb8aef` /
  `61fa5ba18f3620188ee61dac7e3622803591aad9`, with its accepted method,
  launch/import configuration, binding, caps, cleanup, snapshot bytes, and
  Python 3.12 environment class unchanged, to enter raw characterization. Any
  change to those inputs reopens the pre-execution gate and invalidates every
  dependent observation. No product limit or public-host authority transfers.
- Raw-baseline collection is assigned to the final runner owner
  `c3-b1-pre-execution-runner-implementor-replacement-3`
  (`/root/c3_b1_runner_impl_r4`). It may create only data beneath
  `testdata/decoders/cycle3-raw/`; it may not modify the accepted runner,
  method, fixture, expected records, snapshot, product, test, review, progress,
  governance, lock, workflow, or evidence surface. No executable collector is
  added to the repository.
- The raw candidate must retain machine model, macOS build/version, CPU
  architecture, exact Python executable/build, resource-observation mechanisms,
  all accepted fixture/method/runner/cap/source digests, one explicitly
  unrecorded warm-up followed by five independent recorded repetitions, every
  canonical raw result, and min/median/max timing without averaging away a
  failure. It must derive requests only from timeline transitions, mapping,
  samplerate, options, and accepted provenance file sets; expected calls and
  records are forbidden as execution inputs or an output oracle.
- Coverage is all 63 approved UART/SPI/I2C semantic and stress timelines plus
  separately labelled production-cap hostile cases covering malformed framing,
  dense/output-cap behavior, deadline cancellation, graceful terminate, forced
  kill, descriptor close, exact-child reap, and post-failure recovery. The
  artifacts must retain deterministic input/request/output/encoded/decoded/
  text/binary/depth/item/diagnostic/retained counts, parent launch/reap/total
  time, child load/import/decode time, parent retained memory, child peak
  memory/address-space and recursion results, and cleanup latencies wherever
  applicable. A cap termination remains a raw failure observation and no cap
  may be weakened or rerun under a different profile to obtain passing data.
- Root will integration-audit the data, candidate scope and unchanged bindings
  before committing an immutable raw-baseline candidate. Only then may a fresh
  independent raw-baseline verifier be assigned; no pre-execution verifier or
  acceptance pass transfers.

### First authorized execution discovers runner self-mutation

- Recorded: `2026-08-27T05:18:30Z`. State: `changes_required`; raw-baseline
  collection is paused and no raw candidate exists. Runner candidate
  `11a8ade5d828830347095bf2580766c149cb8aef` remains immutable history, but its
  verification, accumulated, and acceptance passes no longer authorize further
  execution because the exact accepted launch is not repeatable in its own
  closed inventory.
- C3B1-RI013: launch arguments are `-I worker.py` while bytecode suppression is
  supplied only through `PYTHONDONTWRITEBYTECODE=1`. CPython isolated mode
  implies environment isolation and ignores that `PYTHON*` variable. The first
  characterization worker therefore imports the fixed sibling
  `snapshot_host.py` and creates
  `tools/cycle3_characterize/__pycache__/snapshot_host.cpython-312.pyc` after
  the parent's successful preflight. The next parent launch correctly rejects
  that extra path as `RunnerFailure: tool inventory rejected`. A standalone
  parent import with `python -B` leaves the inventory clean, proving the child
  launch, not bound source bytes or the RTK wrapper, is the cause.
- Exactly three controlled collection attempts were made while isolating the
  cause. In each attempt only the unrecorded warm-up for
  `uart-rx-valid-default` succeeded; it then created the cache, and all five
  recorded repetitions plus every later warm-up/repetition failed before a
  worker launch. Thus three authorized executions of the same accepted UART
  snapshot occurred after the ordered acceptance gate, but zero recorded
  baseline repetitions succeeded and no SPI or I2C snapshot ran. Earlier
  statements that no decoder ran applied before this authorized phase; the
  implementor's contemporaneous no-worker diagnosis was corrected by the
  retained warm-up status and cache timing evidence.
- The provisional uncommitted JSON was not a baseline and was not edited into
  a pass. It and each generated cache were moved intact to explicit
  `/private/tmp/cycle3-raw-invalidated-launch-v1-20260827T0518` and
  `/private/tmp/cycle3-characterize-pycache-failed-*` quarantine paths. The
  repository is clean and the frozen candidate bytes remain unchanged.
- Correction returns to final runner owner
  `c3-b1-pre-execution-runner-implementor-replacement-3`
  (`/root/c3_b1_runner_impl_r4`) within its original runner/method/launch/test
  ownership. It must make bytecode suppression an explicit isolated-child
  executable argument, update the exact launch/binding/method/test identities,
  and add a real consecutive characterization-route regression proving the
  worker creates no filesystem entry and the second launch reaches the worker.
  No cap, fixture, expected record, snapshot, product, or excluded surface may
  change.
- The correction creates a new immutable pre-execution runner candidate. A
  complete fresh independent inert/hostile verification, root accumulated
  non-decoder gate, and acceptance are mandatory before any fourth snapshot
  execution or raw-baseline retry. No prior pass or provisional observation
  transfers.

### Repeatable pre-execution runner candidate and verification round 2 assignment

- Recorded: `2026-08-27T05:25:32Z`.
- Corrected candidate commit/tree:
  `48d139f86aabcfa3e34567473c05ade13340107f` /
  `fc36f73089ee6d1c86e3bd6c922c44dffe15477b`; the worktree was clean
  immediately after the seven-path runner-owned commit. Accepted fixture/cap,
  expected-output, decoder snapshot, product, governing, and excluded-scope
  bytes are unchanged.
- RI013 correction is explicit and closed in candidate design: launch config,
  validation, and `Popen` arguments are exactly Python 3.12
  `-I -B worker.py`; the method records that identity; and a closed inert
  `bytecode` probe imports and exact-path-verifies only the bound runner probe
  sibling, reports `sys.dont_write_bytecode`, and cannot select a caller path.
  The focused regression makes two consecutive real shared worker launches,
  requires both diagnostics to report bytecode disabled, and rechecks the
  exact cache-free inventory after the second success.
- Root and final implementor non-decoder checks passed: 167 focused tests,
  focused Ruff, strict mypy over seven tool modules, binding regeneration and
  check, exact two-literal dynamic-import audit, candidate scope, repository
  diff, inventory, and process cleanup. No private snapshot route,
  `execute_snapshot`, decoder/helper/generator/product runtime, fourth snapshot
  execution, hardware, network, excluded action, or Cycle 4 work occurred.
- Corrected SHA-256 identities: binding
  `1d36da4a8e06707c5fad8830c7037fd5aa601fdc8854dc4f33b9aec4b2d992eb`,
  launch `3df74d88a1f013a7aa9f09c81d76a653159de09e9b42270137fb0f3956efbf27`,
  probes `dc0d5ba2e5c1ec1f3e805f9a41a92b29e5edce8a4bb6172ef6fc82dbf8848b2a`,
  runner `2f0d32ec2d2fea047cb5f78e6b3d32753e6d69d3f9d0f398bd589691011ef942`,
  worker `76124299334fc4fb5a7ea5d28750afff9b19f59b4fda0618dd0be215f59f890c`,
  method `8ef7bdac50554fb42ec97d3c5d685d3f6b55074c82478c750e4e62ff3d318325`,
  and implementation test
  `74e5c8d823f1f58ffc84e57bbae7264ee80c67586dec1e3e816e8ccce8f341c1`.
- Complete fresh verification is reassigned to the independent existing
  `c3-b1-pre-execution-runner-verifier-1`
  (`/root/c3_b1_runner_verify`) with no round-1 pass transfer. It may update
  only its verification test and create immutable
  `docs/reviews/c3-b1-preexecution-runner-verification-round-2.md`; it may
  repair no candidate byte.
- Round 2 must repeat the complete 17-cap, binding/import/root/file/symlink/
  shadow/environment/CWD, framing/accounting, termination/kill/close/reap,
  recovery, fixed-route, option, and API-v3 non-decoder matrix, and add an
  independent RI013 proof that isolated mode ignores the environment-only
  setting, explicit `-B` is present in both launch identities, two or more
  consecutive real inert sibling-import workers leave no cache or inventory
  drift, and a valid probe follows. It must explicitly preserve the three
  historical authorized UART warm-ups, execute no fourth snapshot, and end
  exactly `pass` or `changes_required`.

### Corrected runner verification pass and accumulated-gate assignment

- Recorded: `2026-08-27T05:29:21Z`.
- Exact subject remains corrected candidate/tree
  `48d139f86aabcfa3e34567473c05ade13340107f` /
  `fc36f73089ee6d1c86e3bd6c922c44dffe15477b`; every candidate-owned byte is
  unchanged in the verifier descendant.
- Independent verifier/verdict:
  `c3-b1-pre-execution-runner-verifier-1` / `pass`; fresh round-2 record and
  23-test matrix committed at `8bcd7ba19795633a9e0e215c1d9f2cc47a893b03`.
  Record SHA-256 is
  `0fc07aea133702352d0dee74d18e4287f707481b598773481d7c9d37501942dc`;
  verifier-test SHA-256 is
  `c6cec19e2e97a833315270d2ae9dbf1cd9b19433122cf545b1f5d2512204bf5b`.
- The complete fresh cap, binding/import, framing/accounting, resource,
  termination/kill/close/reap, recovery, fixed-route, option, and API-v3 matrix
  passed. Independent RI013 proof showed environment-only suppression is false
  under `-I`, both frozen launch identities contain explicit `-B`, consecutive
  real inert sibling-import workers remain cache-free, and a valid recovery
  follows. Fresh results were 23 independent and 190 combined focused passes;
  Ruff, mypy, binding, candidate equality, diff, inventory, and process checks
  passed. No fourth snapshot execution occurred.
- Root accumulated validation is now assigned freshly to this corrected
  candidate. No round-1 accumulated result transfers. It must rerun the exact
  clean hash-locked Python 3.12 bootstrap/install/check/Ruff/mypy/non-hardware
  pytest/help gate, all corrected focused suites, deterministic fixture rebuild,
  Cycle 1/2 evidence and quiet-scope checks, decoder/import/dependency/package/
  process/prohibited-runtime audits, exact 64-GiB resource feasibility, and the
  unchanged exact-Node-22 frontend/unit/build/browser/performance regressions.
- The immutable result path is fixed as
  `docs/reviews/c3-b1-preexecution-runner-accumulated-validation-round-2.md`.
  It must bind RI013, corrected candidate/verifier identities and digests,
  superseded round-1 passes, the three historical UART warm-ups, clean inventory
  repeatability, every corrected command/result, and issue only `pass` or a
  failure. Acceptance round 2 is assigned only after that result passes and is
  committed; no decoder/snapshot route may run during accumulation.

### Corrected runner accumulated pass and acceptance round 2 assignment

- Recorded: `2026-08-27T05:37:48Z`.
- Exact corrected candidate/tree remains
  `48d139f86aabcfa3e34567473c05ade13340107f` /
  `fc36f73089ee6d1c86e3bd6c922c44dffe15477b`; candidate-owned bytes are
  unchanged in every descendant.
- Fresh root accumulated validation passed and is committed at
  `d307c3059a4e35c6389304f4782b3d06776fae2b` in
  `docs/reviews/c3-b1-preexecution-runner-accumulated-validation-round-2.md`,
  SHA-256
  `4656a53c49f7abc93d5b68faa0e2689537c69221499193830c0c13882999d645`.
- A cleared hash-locked Python 3.12.13 environment produced 593/593
  non-hardware passes with no skip, 190 corrected focused passes, Ruff, both
  strict mypy scopes, installed help, deterministic fixtures, exact 64-GiB
  set/readback, all Cycle 1/2 evidence, package/import/process/scope and
  cache-free repeatability checks. Exact Node 22 produced clean install,
  lint/type/unit/build/assets, four browser, and one performance pass. No
  snapshot route, fourth decoder execution, hardware, or prohibited runtime ran.
- Fresh acceptance is reassigned to the same independent acceptance-role
  identity `c3-b1-pre-execution-runner-acceptance-1`
  (`/root/c3_b1_runner_accept`) with no round-1 pass transfer. It may create
  only immutable
  `docs/reviews/c3-b1-preexecution-runner-acceptance-round-2.md`, may repair
  nothing, and must end exactly `pass` or `changes_required`.
- Acceptance round 2 must audit the corrected candidate, RI013 discovery and
  three historical authorized UART warm-ups, old-pass and provisional-data
  invalidation, final implementor ownership, round-2 verifier record/test,
  accumulated round-2 completeness and corrected reruns, exact path equality,
  explicit isolated-child `-B` semantics, consecutive cache-free sibling-import
  proof, full 17-cap/cleanup/fixed-route/method/scope/provenance evidence, and
  immutable ordering. It may use only static inspection and inert/hostile
  non-decoder probes; no fourth snapshot execution or raw retry is authorized.
  A `pass` authorizes only the exact unchanged corrected runner to resume the
  separately ordered raw-baseline phase.

### Corrected runner acceptance pass and raw-baseline resumption

- Recorded: `2026-08-27T05:40:36Z`.
- Acceptance identity/verdict:
  `c3-b1-pre-execution-runner-acceptance-1` / `pass`; fresh round-2 record
  committed at `896c1bf050896c48cc6541bb7ad429ce4b6e74e0` in
  `docs/reviews/c3-b1-preexecution-runner-acceptance-round-2.md`, SHA-256
  `ce1baa3c102e933fb9b8c5ffa8fe8f199e125ef17d82e662aec880f095793aef`.
  It found no discrepancy in RI013 history/invalidation, corrected ownership,
  candidate equality, fresh verification/accumulation, explicit isolated-child
  bytecode semantics, repeatability, 17-cap/cleanup evidence, method,
  provenance, scope, or ordering. No fourth snapshot execution occurred.
- The complete corrected runner gate now authorizes only exact candidate/tree
  `48d139f86aabcfa3e34567473c05ade13340107f` /
  `fc36f73089ee6d1c86e3bd6c922c44dffe15477b` to resume the original raw-data
  assignment. Any change to its runner, method, launch/import, binding, caps,
  cleanup, snapshot, or environment class invalidates this authority.
- Raw collection returns to final runner owner
  `c3-b1-pre-execution-runner-implementor-replacement-3`
  (`/root/c3_b1_runner_impl_r4`) under the exact original data-only scope and
  method. It may create only non-executable JSON beneath
  `testdata/decoders/cycle3-raw/`; no provisional artifact or historical
  warm-up result transfers. Collection restarts with a new unrecorded warm-up
  and five recorded repetitions for every one of the 63 timelines and each
  selected production-profile hostile case.
- Requests remain derived only from transitions, mapping, sample count,
  samplerate, options, and accepted provenance source sets; expected calls,
  waits, records, and typed goldens remain forbidden inputs/oracles. The raw
  candidate must preserve every required deterministic count, timing, resource,
  cleanup, raw-result, environment, digest, mechanism, coverage, failure, and
  min/median/max field fixed in the original assignment. Caps remain unchanged;
  a termination remains an observation, not a passing baseline.
- Root will audit complete success/failure coverage, raw immutability, exact
  candidate equality, cache-free repeated execution, and process cleanup before
  committing the raw candidate and assigning independent reproduction. No
  threshold proposal or product-host work is authorized yet.

### Concurrent collector attempt invalidated before raw candidate

- Recorded: `2026-08-27T05:46:21Z`. State: raw collection restart required;
  corrected runner authority remains valid and unchanged, but no observation
  from this attempt may transfer.
- The implementor launched collector PID 8908 and, after its long no-output
  interval, launched a second collector PID 9980 instead of resuming the first
  command session. Root detected both exact collectors concurrently. Concurrent
  worker scheduling and shared parent/machine resource contention invalidate
  every timing and retained-memory observation from both processes; a shared
  output target also made eventual file replacement unsafe.
- Root interrupted the implementor and terminated only the four exact collector/
  wrapper PIDs 8906, 8908, 9957, and 9980. No worker remained. The collector was
  deliberately write-at-end, so no raw repository artifact or partial result
  was created; the number of completed snapshot calls before termination was
  not retained and no result can be represented as baseline evidence.
- Static root audit also rejected the temporary collector before reuse: success
  resource timestamps were evaluated before the runner call; empty valid-probe
  diagnostics were parsed as JSON; pin initialization was implicit; environment
  identities/digests were incomplete; and per-field and hostile summaries were
  incomplete. These are temporary orchestration-script defects, not changes to
  the frozen runner or caps.
- The same raw owner must correct only the temporary collector and hand it to
  root without execution. Root will start and monitor exactly one serialized
  process to completion, validate all required fields and counts before any
  repository write is accepted, and restart warm-up plus all five repetitions
  from zero. No concurrent or killed result transfers, and no threshold or
  product authority is created.

### First serialized raw run discarded before repository write

- Recorded: `2026-08-27T05:54:46Z`. The corrected temporary collector first
  rejected its own logical-to-physical request packer before any worker launch;
  root fixed it to maintain `D<number>` physical-pin state and require every
  mapped pin's explicit sample-zero transition.
- One and only one monitored collector session then completed the 63 timeline
  warm-up/five-repetition loops and all ten hostile warm-up/five-repetition plus
  required recovery loops: 378 snapshot-route calls and 100 inert/hostile probe
  calls. After collection, its metadata-only digest step incorrectly resolved
  repository-relative `Software/decoders/...` paths beneath
  `Software/LogicAnalyzerPy` and raised `FileNotFoundError`.
- The collector's write-at-end design created no repository raw file. Therefore
  none of that run's outputs, timings, counts, or resources can be audited or
  transferred, and the entire run is discarded rather than spliced or edited.
  The frozen runner, method, snapshots, caps, and environment class are
  unchanged; no cache, worker, or raw file remained.
- Root corrected only the temporary digest resolver to use repository root for
  `Software/...` paths. A new single monitored run must restart every warm-up
  and repetition from zero and pass all pre-write assertions before any raw
  candidate may exist.

### Second serialized raw run discarded at environment probe

- Recorded: `2026-08-27T05:58:50Z`. A second single monitored run again
  completed all 378 snapshot-route and 100 inert/hostile/recovery calls, then
  reached the write-at-end environment probe. Sandbox policy denied
  `sysctl -n hw.model`; the collector raised before assertions or any file
  write, so every measurement is again discarded and no raw candidate exists.
- Root independently obtained only the non-sensitive model identifier
  `Macmini8,1` through the read-only hardware profiler and explicitly excluded
  its serial, UUID, and provisioning fields. Accepted `sw_vers` values remain
  macOS 15.7.7 build 24G720. No sensitive hardware identifier is retained in
  repository evidence.
- All static identity/digest/environment construction and provenance assertions
  now execute before the first warm-up; the temporary collector contains no
  post-collection external command. A third serialized run must still restart
  all warm-ups and repetitions from zero. No prior timing, count, output, or
  resource value transfers.

### Immutable raw-baseline candidate and reproduction assignment

- Recorded: `2026-08-27T06:12:13Z`. The third serialized run began only after
  every environment, digest, and request-derivation preflight passed, used the
  exact corrected runner candidate/tree
  `48d139f86aabcfa3e34567473c05ade13340107f` /
  `fc36f73089ee6d1c86e3bd6c922c44dffe15477b`, and completed alone. Its
  write-at-end assertions passed before any raw file was created.
- Raw candidate commit/tree:
  `397981adf0f89115647203e749db1b1e5b3384cf` /
  `e4baf918c3de4b7df94ad51340bf5b5bfc8f16d2`. It adds exactly five canonical,
  non-executable JSON files beneath `testdata/decoders/cycle3-raw/`; no runner,
  method, fixture, snapshot, expected output, cap, product, or governing byte
  changed. The worktree was clean immediately after commit.
- Candidate SHA-256 values are environment
  `14da4608cf882286a8f62f0e59f596d91753244b619046d14d7f445a89012a4f`,
  hostile observations
  `c956be536fc1fd5c23ebfd33b6bb51377e0f806ace57dfc02fc8888521f801ad`,
  manifest
  `0706b84a0965a36e5b5d20c35c6d4ba9ab774f3bb7532e29f322dcd5a76d0efa`,
  observations
  `a282ccd92ffa27ceda4624d6138de61d48314a0b352f004e3d0770c8b3bc2f03`,
  and requests
  `fe5b345270eced91298250032411b6a85112c55baf46d3b71afb424ef385f94c`.
- Root independently recomputed canonical JSON and manifest hash closure,
  environment/source/collector identities, and all requests directly from the
  accepted transition/mapping/sample-count/samplerate/option/provenance inputs.
  The candidate contains 63 ordered timelines, one status-only unrecorded
  warm-up and five successful recorded repetitions each, stable canonical
  records and semantic diagnostics, complete count/resource/timing fields and
  exact min/median/max summaries. It also contains the ten production-profile
  hostile cases with five repetitions each: two expected successes and eight
  expected failures, with exact descriptor-close/reap evidence and a successful
  valid recovery after every recorded failure. `hang` terminated and reaped;
  `ignore_term` exhausted the 250-ms grace then killed and reaped. No worker or
  bytecode cache remained.
- Independent reproduction is assigned to the existing distinct verifier-role
  identity `c3-b1-pre-execution-runner-verifier-1`
  (`/root/c3_b1_runner_verify`). The runner implementor authored the raw data;
  the verifier authored neither raw request nor observation and remains
  distinct from fixture authors, runner implementors, acceptance, final B1,
  manifest, and orchestration identities. No earlier runner-gate verdict is a
  raw-baseline verdict or transfers to this candidate.
- The verifier may create only
  `tests/verification/test_c3_b1_raw_baseline_candidate.py` and
  `docs/reviews/c3-b1-raw-baseline-verification-round-1.md`; it may not repair
  or rewrite the candidate. It must independently derive all 63 requests from
  authoritative fixture inputs without consuming raw requests as an oracle,
  execute the unchanged private fixed-snapshot route in the exact recorded
  Python 3.12 environment with a fresh unrecorded warm-up plus five repetitions
  per case, and independently repeat all ten production-profile hostile cases
  with the same warm-up/repetition/recovery method.
- Verification must prove candidate/digest/environment equality, exact
  canonical record and stable semantic-count reproduction, every finite cap,
  complete timing/resource/count fields and summary arithmetic, expected
  hostile classifications, deadline/terminate/kill/close/exact-reap paths,
  recovery after every failure, cache/process cleanup, and a transparent
  per-case discrepancy report for non-deterministic timings and memory. It must
  not compare runtime output to expected fixture records or use expected output
  to generate/correct/accept raw results. It must report exactly `pass` or
  `changes_required`; no threshold proposal or product-host work is authorized.

### Raw-baseline reproduction pass and accumulated-gate assignment

- Recorded: `2026-08-27T06:24:05Z`. Exact raw candidate/tree remains
  `397981adf0f89115647203e749db1b1e5b3384cf` /
  `e4baf918c3de4b7df94ad51340bf5b5bfc8f16d2`; raw, runner, method, fixture,
  snapshot, and cap bytes are unchanged in every descendant.
- Independent verifier/verdict:
  `c3-b1-pre-execution-runner-verifier-1` / `pass`; the verifier-only test and
  immutable record are committed at
  `9ac10d77cf1e8c492e7b5dae564baa43b09ebf71`. Test SHA-256 is
  `08687a9bcc7fed1cfb55dbb6ec9b3c31f2ea486cfd389857916d6039b33567ca`;
  record SHA-256 is
  `c9c08720039de278c12c54501e09c71634f084408330af849011004a666441c2`.
- The final uninterrupted reproduction independently derived all 63 requests,
  then passed one fresh warm-up plus five repetitions per snapshot and the
  complete ten-case hostile warm-up/five-repetition/recovery matrix. Exact
  semantics and stable counts reproduced; every terminate/kill/descriptor-
  close/exact-reap/recovery path passed; focused runner tests, Ruff, binding,
  digest, summary, scope, cache, and process audits passed. No expected output
  was used as a runtime oracle and no worker remained.
- The discrepancy record is explicit: 61/63 fresh total-time ranges were lower
  and non-overlapping while two overlapped; child RSS overlapped for 58 cases
  and was lower for five, with none higher and non-overlapping. These remain
  observations and supply no threshold conclusion.
- Root accumulated validation is now assigned against this unchanged raw
  candidate. It must include the full clean hash-locked Python 3.12 bootstrap
  state, complete raw verifier/reproduction suite, corrected runner and fixture
  focused suites, Ruff, strict mypy, binding and deterministic fixture checks,
  all non-hardware tests without mandatory skips, installed help, Cycle 1/2
  evidence validators, exact resource feasibility, prohibited dependency/
  import/process/cache and quiet-scope audits, and unchanged exact-Node-22
  frontend/unit/build/browser/performance regressions.
- The accumulated result path is fixed as
  `docs/reviews/c3-b1-raw-baseline-accumulated-validation-round-1.md`. It must
  bind the raw/verifier candidate identities and all commands/results, preserve
  the timing/RSS discrepancies, and report only `pass` or a failure. Raw
  acceptance is assigned only after this accumulated record passes and is
  committed. No proposal, threshold decision, or product-host work is yet
  authorized.

### Raw-baseline accumulated pass and acceptance assignment

- Recorded: `2026-08-27T06:36:28Z`. Exact raw candidate/tree remains
  `397981adf0f89115647203e749db1b1e5b3384cf` /
  `e4baf918c3de4b7df94ad51340bf5b5bfc8f16d2`; every raw, runner, method,
  fixture, snapshot, and cap byte remains unchanged.
- Root accumulated validation/verdict: `pass`, committed at
  `b49bd4932c4c091529b6c93f45de1f3f807e83f2` in
  `docs/reviews/c3-b1-raw-baseline-accumulated-validation-round-1.md`, SHA-256
  `839bc5aae57a179007acbf405c7f1ce5c6484c51a7d997650e01e1cbcba879ee`.
- A freshly cleared, hash-locked Python 3.12.13 environment passed Ruff, both
  strict mypy scopes, deterministic fixtures, binding, 596 unrestricted
  non-hardware tests with no skip, installed help, 18 fixture and 190 runner
  focused tests, all six Cycle 2 validators, accepted Cycle 1 hashes, exact
  64-GiB resource feasibility, dependency/import/package/scope/cache audits,
  and the full raw reproduction again. Exact Node 22 passed clean install,
  lint, type, five unit tests, 29-module build/assets, four browser tests, and
  one B6 performance/threshold test.
- The independent timing/RSS discrepancy classification remains explicit and
  unchanged; no cap, raw value, or threshold was edited or inferred. An
  orchestration-only wrong asset-checker path was discarded and the governed
  Python checker passed. Generated browser results were moved intact to
  `/private/tmp/cycle3-raw-accumulated-web-20260827T0632`.
- During this gate the operator separately directed a repository instruction
  improvement. Commit `c936403` changes only root `AGENTS.md` to require one
  narrow reusable privileged command class per approval and prohibit repeated
  heterogeneous approval requests. It is not Cycle 3 candidate evidence,
  changes no scoped product/raw/governing byte, and must remain an explicit
  user-directed unrelated descendant rather than being silently absorbed.
- Fresh raw acceptance is assigned to the existing distinct acceptance-role
  identity `c3-b1-pre-execution-runner-acceptance-1`
  (`/root/c3_b1_runner_accept`). It may create only
  `docs/reviews/c3-b1-raw-baseline-acceptance-round-1.md`, may repair nothing,
  and must report exactly `pass` or `changes_required`.
- Acceptance must audit candidate immutability; raw authorship and verifier/
  acceptance separation; exact method/environment/digest/count/summary
  completeness; independent 63-case and hostile reproduction; every timing/
  RSS discrepancy; accumulated bootstrap/regression/resource/scope evidence;
  cleanup/cache/process state; governing ordering; the unrelated `AGENTS.md`
  instruction commit; and absence of expected-output oracle, threshold,
  product, hardware, external runtime, publication, or Cycle 4 work. It may use
  static inspection and existing immutable evidence only and must not execute a
  snapshot or hostile probe. A pass authorizes only threshold-proposal
  preparation; it does not approve any numeric value.

### Raw-baseline acceptance pass and threshold-proposal assignment

- Recorded: `2026-08-27T06:40:52Z`. Acceptance identity/verdict:
  `c3-b1-pre-execution-runner-acceptance-1` / `pass`; immutable record committed
  at `7baa53bf8efe3de66722220ce20b0042f27f3cab` in
  `docs/reviews/c3-b1-raw-baseline-acceptance-round-1.md`, SHA-256
  `87df517169c83c2c22a199fafcd9dec69e8197e5ee8e4d1f21fa9f6170056396`.
  It found no open issue in candidate immutability, role separation, method,
  environment, digest/count/summary completeness, 63-case and hostile
  reproduction, timing/RSS discrepancies, accumulated evidence, cleanup,
  scope, ordering, or the unrelated operator-directed `AGENTS.md` commit. It
  executed no snapshot or probe.
- All three raw-baseline gates now pass for exact candidate/tree
  `397981adf0f89115647203e749db1b1e5b3384cf` /
  `e4baf918c3de4b7df94ad51340bf5b5bfc8f16d2`. This authorizes only proposal
  preparation; no numeric value is approved and no B2 product work may begin.
- Root owns the immutable proposal candidate under exactly
  `testdata/decoders/cycle3/threshold-proposal-round-1.json` and
  `docs/reviews/c3-b1-threshold-proposal-rationale-round-1.md`. Neither path is
  an approved-limits file, operator record, product configuration, enforcement
  implementation, or future manifest.
- The proposal must bind the accepted fixture, corrected runner, raw candidate,
  verifier, accumulated, and acceptance commits/digests and exact characterized
  macOS/Python environment. It must independently recompute raw maxima and name
  every required exact ceiling: input samples, request bytes, wall deadline,
  cancellation grace, worker address space/memory, recursion, output records,
  encoded/decoded/text/binary/nested-item/nested-depth/diagnostic/retained-result
  bytes, parent retained memory, performance timings, and maximum SPI word size.
- Every value must show unit, accepted maximum observation or static boundary,
  arithmetic/rationale, inclusive accept and exclusive reject boundary, and
  relationship to the unchanged experiment cap. Timing/RSS discrepancies and
  missing/unreliable observations remain explicit. No raw value may be edited;
  no experiment cap may be weakened to obtain data; no convenient default may
  be presented as approval.
- After root commits the exact proposal candidate, the existing verifier-role
  identity receives a fresh proposal-specific assignment and verdict, followed
  by complete accumulated proposal validation and fresh acceptance. Only then
  will the exact committed values be presented to the operator for explicit
  approval or amendment. An amendment creates a new proposal candidate and
  repeats all three proposal gates.

### Immutable threshold-proposal candidate and verification assignment

- Recorded: `2026-08-27T06:47:52Z`. Proposal candidate commit/tree:
  `e3a1d7c28a88a037e694d81c8c3406589fba040e` /
  `38eda7b580d505d3966f765bcffaf7297cb539f4`. It adds exactly the assigned
  machine-readable proposal and rationale; status is explicitly
  `proposal-not-approved`. No approved-limit, product, fixture, raw, runner,
  snapshot, cap, governing, manifest, or operator-decision byte exists or
  changed.
- Proposal JSON SHA-256 is
  `61d1273114d98bf6652b5401bf146e8d44fd6a51242c317a502719dfb036e080`;
  rationale SHA-256 is
  `112d5606b7912cce2e99bc16189d1783829eb79733b72d1d469d0beab1ca42b0`.
  Root's independent pre-candidate audit passed 29 unique limits, every
  inclusive/exclusive boundary, all raw maxima, experiment-cap relationships,
  formulas, evidence/environment identities, and digest closure.
- The proposal names hard enforcement for 65,536 samples, 4-MiB requests,
  5,000-ms deadline, 250-ms grace, 64-GiB address space, 320 recursion frames,
  bounded outputs/nesting/retention, and SPI maximum 8; separate observed
  regression ceilings cover 128-MiB worker RSS, 16-MiB parent retained growth,
  successful/phase/cleanup timings, and reap latency. These are candidate
  values only and carry no operator approval.
- Fresh proposal verification is assigned to the existing verifier-role
  identity `c3-b1-pre-execution-runner-verifier-1`
  (`/root/c3_b1_runner_verify`), distinct from proposal authorship and all
  acceptance identities. It may create only
  `tests/verification/test_c3_b1_threshold_proposal.py` and
  `docs/reviews/c3-b1-threshold-proposal-verification-round-1.md`; it may repair
  nothing and must report exactly `pass` or `changes_required`.
- Verification must independently recompute all 29 required categories from
  accepted raw/hostile/request/environment/cap evidence; validate the proposal
  schema, unique closed IDs, positive integer types, units, exact accept/value
  and reject/value+1 boundaries, formulas, rationale, digests, commits, and
  macOS qualification; prove every hard ceiling is equal to or stricter than
  the experiment cap; and audit cross-limit feasibility for maximum samples,
  request framing, retained output, deadline/grace/cleanup, address space/RSS,
  and SPI evidence.
- Independent negative tests must reject missing/extra/duplicate entries,
  booleans/non-integers/non-positive values, altered raw maxima or formulas,
  weakened experiment boundaries, inconsistent units/bounds, performance
  ceilings that contradict deadline/cleanup policy, an SPI maximum above
  characterized evidence, status changed to approved, and any evidence/digest
  substitution. Static inspection only: no snapshot, decoder, hostile probe,
  product host, hardware, network, or excluded action is authorized.

### Threshold-proposal round-1 finding and round-2 correction assignment

- Recorded: `2026-08-27T13:32:10Z`. Fresh verifier identity/verdict:
  `c3-b1-pre-execution-runner-verifier-1` / `changes_required`; immutable
  evidence committed at `e47dc308ff3a7e22679d0bf1e9730f753eb29f47` in
  `tests/verification/test_c3_b1_threshold_proposal.py`, SHA-256
  `183803d54768c484d2dd8334795521f6eacea59f1bec1321577ede83ab259bd6`,
  and `docs/reviews/c3-b1-threshold-proposal-verification-round-1.md`,
  SHA-256
  `0ab6a4e897147b73fb4249eeecbadb08ec4cdd18a92ffc2ba713b6f9525a47ab`.
- Finding `C3B1-TPV001` is exact and singular: raw maximum
  `105,815,301 ns` multiplied by eight is `846,522,408 ns`, whose ceiling to
  a `100,000,000 ns` quantum is `900,000,000 ns`, not the proposed
  `1,000,000,000 ns`. The other 28 limits, all 29 raw maxima, evidence
  identities, experiment-cap relationships, feasibility checks, and negative
  tests passed. Round 1 remains immutable and transfers no pass or approval.
- Root is assigned a new immutable round-2 proposal at exactly
  `testdata/decoders/cycle3/threshold-proposal-round-2.json` and
  `docs/reviews/c3-b1-threshold-proposal-rationale-round-2.md`. The only
  numeric correction authorized is `successful_parent_total_ns`: value and
  inclusive accept become `900,000,000`, exclusive reject becomes
  `900,000,001`, and the stated `ceil_to_100ms(raw_max * 8)` derivation remains
  unchanged. Its prose ratio must become approximately `8.51 times`.
- Round 2 must identify the failed round-1 candidate, its assignment, the
  failed verification commit, and this correction assignment. No other value,
  raw observation, cap, fixture, runner, product, approved-limit, governing,
  manifest, or operator-decision byte may change. After root commits the new
  candidate, the existing verifier role receives a fresh round-2 assignment;
  accumulated validation and fresh acceptance remain forbidden until that
  new verdict passes.

### Immutable threshold-proposal round-2 candidate and verification assignment

- Recorded: `2026-08-27T13:33:55Z`. Corrected proposal candidate commit/tree:
  `395646fa1172382928581d7266723f5b044cf8f2` /
  `6857f9a67ff70220e6d6b2a11f9ca450005c8321`. Proposal JSON SHA-256 is
  `94882b710f2d569c0ea0535366a0c1c3df3514aa20a18e4cd35f652177458ec2`;
  rationale SHA-256 is
  `18a6b58a2b05f7dd7aa302a6e1bb4d074621440648a2e735a1d16d9708b209b0`.
- Root's pre-candidate audit passed JSON parsing, exactly 29 limits, unapproved
  status, exact 900-ms formula arithmetic and boundaries, and normalized
  equality with round 1 after reversing only the assigned correction and
  round/provenance metadata. No other numeric proposal meaning changed.
- Fresh round-2 verification is assigned to existing verifier-role identity
  `c3-b1-pre-execution-runner-verifier-1`
  (`/root/c3_b1_runner_verify`). It may create only
  `tests/verification/test_c3_b1_threshold_proposal_round2.py` and
  `docs/reviews/c3-b1-threshold-proposal-verification-round-2.md`; it may
  repair nothing and must report exactly `pass` or `changes_required`.
- The verifier must repeat the complete round-1 proposal audit and negative
  matrix against the new immutable candidate, independently recompute
  `ceil_to_100ms(105815301 * 8) == 900000000`, audit exact correction scope
  and complete provenance, and transfer no earlier pass. Static inspection
  only; no snapshot, decoder, hostile probe, product host, hardware, network,
  install, external runtime, or excluded action is authorized.

### Threshold-proposal round-2 verification and accumulated pass

- Recorded: `2026-08-27T13:51:58Z`. Fresh verifier identity/verdict:
  `c3-b1-pre-execution-runner-verifier-1` / `pass`; immutable evidence
  committed at `1cdedcae57e6233010410172196b23f6167ee675`. Verifier-test
  SHA-256 is
  `f146f0d58a65116825f6ee6b2e04e4fcf495fca89de9565bf70e26b662509c79`;
  record SHA-256 is
  `c160cc75238ab48479fb3cfe4d0c4d0c86ee052102a4fd2715050b285d4e50a0`.
  All 22 tests passed, including corrected formula/boundaries, all 29 limits,
  exact correction scope/provenance, feasibility, and the full fresh negative
  matrix. No earlier pass transferred and status remains unapproved.
- Root accumulated validation/verdict: `pass`, committed at
  `0d00fe4b88a1192b893afbf8e32c39bd6493b2fd` in
  `docs/reviews/c3-b1-threshold-proposal-accumulated-validation-round-2.md`,
  SHA-256
  `b3a1455aefb3044d1048d6e2253885ba9908a09e7bc5e24c287bb63b21723b4b`.
  Repository-local Python 3.12 and Node 22 tooling passed Ruff, strict mypy,
  deterministic fixture/binding checks, 637 applicable non-hardware tests,
  all six Cycle 2 validators, frontend lint/type/unit/build/assets, four browser
  tests, and offline performance plus the unchanged accepted-threshold checker.
- The accumulated record preserves an explicit three-node historical
  applicability classification: the pre-proposal fixture namespace assertion,
  raw evidence's former `/private/tmp` executable identity, and the immutable
  failed round-1 exact-formula assertion. Their current replacements passed;
  no historical test or evidence byte was edited. Local tooling resides only
  under ignored repository `.venv`, and one reusable loopback npm-script rule
  replaced per-process authorization.
- Fresh proposal acceptance is assigned to existing distinct acceptance-role
  identity `c3-b1-pre-execution-runner-acceptance-1`
  (`/root/c3_b1_runner_accept`). It may create only
  `docs/reviews/c3-b1-threshold-proposal-acceptance-round-2.md`, may repair
  nothing, and must report exactly `pass` or `changes_required`.
- Acceptance must statically audit immutable proposal `395646f`, fresh
  verification and accumulated evidence, formula arithmetic, all 29 values and
  boundaries, raw/cap/digest/environment/provenance closure, correction scope,
  the three transparent applicability classifications, local-tooling and
  authorization disposition, quiet candidate scope, ordering, and continued
  unapproved status. It must transfer no pass, execute no snapshot/decoder/
  probe, and make no operator decision. A pass authorizes only presentation of
  the exact committed values for explicit operator approval or amendment.

### Threshold-proposal round-2 acceptance pass and operator decision gate

- Recorded: `2026-08-27T13:54:53Z`. Acceptance identity/verdict:
  `c3-b1-pre-execution-runner-acceptance-1` / `pass`; immutable record
  committed at `91de257667fa819dd1c183d4ec112f106ed6742a` in
  `docs/reviews/c3-b1-threshold-proposal-acceptance-round-2.md`, SHA-256
  `f507f0225b9326cf1fd15cbcfe61415c2554ca44bcc491bf7b0f9250e058f102`.
- Acceptance found no open issue in candidate scope/status, `C3B1-TPV001`
  correction, all 29 values and boundaries, evidence/provenance closure, fresh
  verification, accumulated evidence, transparent historical applicability,
  local tooling/authorization, ordering, cleanup, or safety. Static inspection
  only occurred; no operator decision was made.
- Exact proposal `395646fa1172382928581d7266723f5b044cf8f2` has now passed
  fresh verification, complete accumulated validation, and fresh independent
  acceptance. It remains exactly `proposal-not-approved`.
- State: awaiting explicit operator approval or amendment of the exact round-2
  committed values. No approved-limit record, final B1 candidate, B1 manifest,
  checkpoint, or B2 product work is authorized before that decision. Any
  amendment creates a new immutable proposal candidate and repeats proposal
  verification, accumulated validation, and acceptance.

### Operator threshold approval and final B1 candidate assignment

- Recorded: `2026-08-27T16:48:28Z`. The operator explicitly stated
  `I approve the exact round-2 threshold value` in direct response to the
  request to approve the complete exact round-2 threshold values. This is an
  approval of all 29 committed entries, not a selection or amendment of one.
- The immutable decision record is committed at
  `b6d904064ab7b9e195eedded1c55efc306eeb925` in
  `docs/reviews/c3-b1-threshold-approval.md`, SHA-256
  `24665a2d63713275c9fc0a82243ee53852834cb36adbf8f6252221804d8b37bc`.
  It binds exact proposal `395646f`, its proposal/rationale digests, all three
  fresh proposal gates, every inclusive/first-rejected boundary, environment
  qualification, amendment procedure, and authority limitations.
- Numeric thresholds and maximum SPI word size are now frozen. No value may be
  silently increased, weakened, rebased, or reinterpreted. The approval is an
  input to final B1 assembly and later enforcement; it does not itself accept
  a final B1 candidate or authorize B2.
- Root is assigned the final B1 integration candidate at exactly
  `testdata/decoders/cycle3/b1-final-candidate.json` and
  `docs/reviews/c3-b1-final-candidate.md`. It must bind governing identities,
  the complete corrected semantic-fixture and pre-execution-runner identity
  histories and final six-role map, project/license disposition, raw candidate
  and three gates, proposal correction and three gates, operator approval,
  exact artifact digests, platform/environment limits, historical finding
  dispositions, exclusions, and exact frozen accumulated commands.
- The candidate may add only those two binder artifacts and must remain
  `candidate-not-accepted`. It may change no fixture, cap, generator, snapshot,
  runner, method, raw, proposal, approval, product, lock, workflow, governing,
  prior review/test, or Cycle 1/2 evidence byte. Root will commit it before
  assigning fresh final B1 verification; no internal pass transfers.

### Immutable final B1 integration candidate and verification assignment

- Recorded: `2026-08-27T16:55:13Z`. Final candidate commit/tree:
  `72e7b35bb3bb8412846caef5302892f9de209c3b` /
  `b30bd5837b7c9b320624b819c54cb11455f200c2`. It adds exactly
  `testdata/decoders/cycle3/b1-final-candidate.json` and
  `docs/reviews/c3-b1-final-candidate.md`; every bound earlier candidate,
  evidence, approval, product, governing, lock, workflow, and manifest path is
  unchanged.
- Binder JSON SHA-256 is
  `1c2cbaa7d99c247b9779b3f7f3654358fcc6e5219ddb030dfb5904faaa9aa29a`;
  rationale SHA-256 is
  `4203c2b2ea079d13a72cac3474299cf93d9f3d8b4f4ae6480fdb289674b3d30b`.
  Root pre-candidate checks passed JSON structure, six-role map, five evidence
  groups, 32 live artifact digest bindings, 21 frozen commands, 29 approved
  limits by exact proposal/approval identity, candidate status, scope, and
  repository diff. No product/runtime action occurred.
- Fresh final B1 verification is assigned to existing independent verifier-role
  identity `c3-b1-pre-execution-runner-verifier-1`
  (`/root/c3_b1_runner_verify`), reused only in its verifier role and distinct
  from root assembly, all implementors, acceptance, and later manifest
  verification. It may create only
  `tests/verification/test_c3_b1_final_candidate.py` and
  `docs/reviews/c3-b1-final-verification-round-1.md`; it may repair nothing and
  must report exactly `pass` or `changes_required`.
- Verification must independently prove the exact candidate commit/tree and
  two-path scope; schema/status/environment; complete six-role separation and
  implementation history; all commits/trees and 32 artifact digests; exact
  project/license disposition; corrected fixture/runner/raw/proposal gate
  ordering; 29 approved values and boundaries; operator-decision identity;
  closed findings and preserved invalidations; 21 executable command records,
  three-node applicability classification, exclusions, and no B2 authority.
  A non-vacuous mutation matrix must reject altered/missing/extra evidence,
  roles, digests, commits, status, environment, commands, limit count,
  approval, findings, applicability, or exclusions.
- Static inspection only is authorized. No snapshot, decoder, runner, hostile
  probe, product host, browser server, hardware, network, install, external
  runtime, package build/publication, B2 work, or Cycle 4 action may run. No
  internal pass transfers; accumulated validation waits for this exact fresh
  verdict.

### Final B1 verification round-1 finding and correction assignment

- Recorded: `2026-08-27T16:59:26Z`. Fresh verifier verdict is
  `changes_required`; immutable test/record committed at
  `a9627e6248cf7cd2642e558429dfbddd484d3f24`. Test SHA-256 is
  `789262b47d54265244ac757b77d06a463e1069432ef1341dca554d32bf66ff08`;
  record SHA-256 is
  `5140be9f7e724c6ffa0d010c6d708ed76eb77112c1844ec8e25a13720f916219`.
- Finding `C3B1-FV001` is exact and singular: the binder has all six final role
  identities but uses `history_is_preserved: true` instead of enumerating the
  complete ordered implementation histories. The progress log is not itself
  digest-bound, so the boolean cannot prove which identities it preserves.
  All other assigned areas passed, including two-path scope, 32 digests,
  commit/tree reachability, 29 approved values/boundaries, operator approval,
  ordering, command/applicability matrices, findings, exclusions, and no-B2
  authority. Round 1 remains immutable and transfers no pass.
- Root is assigned corrected round-2 binders at exactly
  `testdata/decoders/cycle3/b1-final-candidate-round-2.json` and
  `docs/reviews/c3-b1-final-candidate-round-2.md`. It must explicitly enumerate
  fixture identities in order: original `c3-b1-semantic-fixture-implementor-1`
  then replacements 1 through 6; and runner identities in order: original
  `c3-b1-pre-execution-runner-implementor-1` then replacements 1 through 3.
- The only authorized semantic correction is replacing each implementation
  history boolean with the exact ordered identity array and making the
  rationale enumerate the same arrays. Round/provenance metadata must bind the
  superseded candidate, failed verification assignment/commit, and this
  correction assignment. Every evidence value, digest, command, environment,
  status, finding, applicability rule, exclusion, and authority boundary must
  otherwise remain unchanged. Fresh verification is mandatory after commit.

### Corrected final B1 candidate and verification round-2 assignment

- Recorded: `2026-08-27T17:01:19Z`. Corrected candidate commit/tree:
  `1f8793210a3298ed190ff30f97c84b6f9feb9b29` /
  `cbe33ca272ba1b452f6d87fb5e702134a471f702`. Binder SHA-256 is
  `55983bbe9613c0deb0fe7f05a2e88b680b9cfed352f4cccfae9cdd01ca744adf`;
  rationale SHA-256 is
  `9577c4b268af5a4a8c6b7f59f934e8ba689a23d4bda66aa0e8662533acd82396`.
- Root proved the fixture array contains exactly original identity then
  replacements 1-6, the runner array contains exactly original identity then
  replacements 1-3, final identities equal each array's last entry, correction
  provenance is complete, and normalized round-2 equality with round 1 holds
  after reversing only those histories and allowed metadata. All 32 digest
  bindings and every other candidate meaning remain unchanged.
- Fresh verification round 2 is reassigned to the same independent verifier
  identity and original complete scope, with no round-1 pass transfer. It may
  update only `tests/verification/test_c3_b1_final_candidate.py` for the exact
  round-2 subject and create only
  `docs/reviews/c3-b1-final-verification-round-2.md`; it may repair nothing and
  must report exactly `pass` or `changes_required`.
- The verifier must repeat every round-1 audit and mutation family, prove exact
  history order/completeness and correction-only normalized equivalence, and
  bind the new candidate/tree/digests. All static-only prohibitions and the
  ban on accumulated validation or B2 before this verdict remain unchanged.

### Corrected final B1 verification pass and accumulated assignment

- Recorded: `2026-08-27T17:06:16Z`. Fresh verifier/verdict:
  `c3-b1-pre-execution-runner-verifier-1` / `pass`; immutable updated test and
  round-2 record committed at `42b6a185f183fe701e0037cbc6b4636196c96f34`.
  Test SHA-256 is
  `6f931ad8acbff9078e1f6ea125954c4861d4278aa5c0531b81b60ddd8fcb88d2`;
  record SHA-256 is
  `a1cadd1a09836680721418ff606af771b5a9b85f497b27c03d0f8cca64950eaf`.
- All 20 tests passed: exact two-path candidate/tree/digests, complete ordered
  histories and tails, correction provenance/equivalence, six roles, all 32
  evidence bindings, all 29 approved boundaries, all 21 frozen commands,
  applicability, exclusions, reachability, and a 17-family non-vacuous
  mutation matrix. Ruff, diff, quiet-scope, and centralized reusable process
  cleanup checks passed. No internal pass transferred.
- Root complete accumulated validation is now assigned against exact candidate
  `1f87932`. Result path is fixed as
  `docs/reviews/c3-b1-final-accumulated-validation-round-1.md`. It must execute
  all 21 frozen command records under the bound local Python 3.12 and exact
  Node 22 environment, validate all Cycle 1/2 evidence and current candidate
  digests/ordering/scope, retain the explicit three-node historical
  applicability classification, audit dependencies/imports/processes and all
  exclusions, and report only `pass` or a failure.
- The complete unfiltered test inventory must run first so every historical
  result remains visible; the applicable accumulated run may deselect only the
  exact three already reviewed historical nodes. No source or historical test
  may be edited to manufacture a pass. Fresh final B1 acceptance is assigned
  only after the immutable accumulated result passes and is committed. No B1
  manifest/checkpoint or B2 work is yet authorized.

### Final B1 accumulated pass and acceptance assignment

- Recorded: `2026-08-27T17:14:41Z`. Root accumulated verdict: `pass`, committed
  at `e9e75a722e76f7469f2708c56237243999b9169b` in
  `docs/reviews/c3-b1-final-accumulated-validation-round-1.md`, SHA-256
  `5f7bec8d92d99cd365a4588479ecf646b8c57bc0ed5c8eb6a0ef0c39b78e1c7b`.
- All 21 frozen command records passed under repository-local Python 3.12 and
  exact local Node 22: dependency, Ruff, both strict mypy scopes, deterministic
  fixture/binding, CLI, six Cycle 2 validators, 657 applicable non-hardware
  tests, lint/type/five unit/build/assets, four browser tests, and accepted-
  threshold performance. The complete 660-test inventory first reproduced
  exactly 657 passes plus the three transparent immutable historical failures.
- Candidate/digest/evidence/import/dependency/license/scope/exclusion/process
  audits passed. The accepted performance report records exact Node/browser/
  automation/method identities and SHA-256
  `315649da912bb92a012cab2c766935ce79c8af4a11245683dbb6aeed280935fa`;
  generated results are retained under ignored local `.venv/artifacts`. No
  package, product host, hardware, external runtime, B2, or prohibited process
  occurred or remains.
- Fresh final B1 acceptance is assigned to existing independent acceptance-role
  identity `c3-b1-pre-execution-runner-acceptance-1`
  (`/root/c3_b1_runner_accept`), distinct from root assembly/accumulation, all
  implementation identities, final verifier, and later manifest verification.
  It may create only `docs/reviews/c3-b1-final-acceptance-round-1.md`, may
  repair nothing, and must report exactly `pass` or `changes_required`.
- Acceptance must audit exact corrected candidate `1f87932`, round-1 failure
  and FV001 correction ordering, complete role histories/separation, all 32
  evidence digests, corrected fixture/runner/raw/proposal gates, operator
  approval and all 29 boundaries, final verifier and accumulated results,
  frozen command/applicability evidence, project/license limitations,
  candidate quiet scope, exclusions, cleanup, and readiness for atomic
  manifest assembly. Static inspection only; no internal pass transfers, no
  manifest may be created before acceptance, and no B2 work is authorized.

### Final B1 acceptance pass and atomic manifest assignment

- Recorded: `2026-08-27T17:19:10Z`. Fresh acceptance identity/verdict:
  `c3-b1-pre-execution-runner-acceptance-1` / `pass`; immutable record
  committed at `72e7bc0d34cc613b5d98798f963c942390a44b8f`. Record SHA-256 is
  `69cea8402993198bfadb88ed2a00710e8c21ba2754c18b681739587038cf7b8f`.
- Acceptance independently closed exact corrected candidate `1f87932`,
  FV001 correction ordering, complete role histories and separation, all 32
  live digests, five evidence groups, 29 operator-approved boundaries, final
  verification, accumulated validation, applicability, exclusions, and
  cleanup. No finding remains open and no internal pass transferred.
- Root is now assigned atomic assembly of exactly
  `testdata/evidence/c3-b1.json`. The manifest must bind accepted candidate
  commit/tree `1f8793210a3298ed190ff30f97c84b6f9feb9b29` /
  `cbe33ca272ba1b452f6d87fb5e702134a471f702`, name planned independent
  identity `c3-b1-manifest-verifier-1`, contain only already-existing evidence,
  and predict no verifier verdict, manifest digest, or verification record.
- After assembly, distinct manifest verification must independently recompute
  every referenced digest, validate the unchanged manifest against the frozen
  schema and strict validator, and create only
  `docs/reviews/c3-b1-manifest-verification-round-1.md`. The manifest and pass
  record are committed together; the checkpoint is appended only afterward.
  No B2 work, checkpoint, publication, or other expanded authority exists yet.

### Manifest preflight separation finding

- Recorded: `2026-08-27T17:19:10Z`. Finding `C3B1-MP001`:
  manifest preflight found that the final verification and final acceptance
  records reused internal runner identities
  `c3-b1-pre-execution-runner-verifier-1` and
  `c3-b1-pre-execution-runner-acceptance-1`.
- Frozen `cycle3-schema.json` requires all six C3-B1 internal identities to be
  distinct from the primary verification, acceptance, and manifest-verifier
  identities. The governing review likewise fixes the final B1 verifier and
  acceptance identities as separate from all six internal identities. A
  truthful manifest naming the actual reused identities therefore cannot pass
  the frozen validator; substituting planned identities that did not perform
  the reviews would be false evidence.
- Atomic manifest assembly is paused before creating `c3-b1.json`. The
  corrected ordering requires a fresh final verifier identity, a fresh complete
  accumulated gate, a fresh final acceptance identity, and then a third fresh
  manifest-verifier identity. Candidate `1f87932` and all prior records remain
  immutable; no B2 or checkpoint authority transfers from the invalid role
  separation.

### C3B1-MP001 fresh final-verification assignment

- Recorded: `2026-08-27T19:05:24Z`. The operator authorized three fresh
  subagents for corrected final verification, final acceptance, and manifest
  verification. Fresh final verification is assigned first to identity
  `c3-b1-final-verifier-2` (`/root/c3_b1_final_verify_fresh`).
- The immutable subject remains candidate commit/tree `1f8793210a3298ed190ff30f97c84b6f9feb9b29`
  / `cbe33ca272ba1b452f6d87fb5e702134a471f702`. The verifier may create only
  `docs/reviews/c3-b1-final-verification-round-3.md`, may repair nothing, and
  must independently repeat the complete final static verification scope and
  return exactly `pass` or `changes_required`.
- No prior final-verifier pass transfers. Root will rerun the complete
  accumulated gate only after this immutable fresh verdict is committed; the
  fresh acceptance and manifest-verifier identities remain ordered later.

### C3B1-MP001 fresh final-verification pass and accumulated assignment

- Recorded: `2026-08-27T19:09:17Z`. Fresh verifier identity/verdict:
  `c3-b1-final-verifier-2` / `pass`; immutable record committed at
  `a5fb09315064c49772d453ab5c1ba9d3a0200ba5`. Record SHA-256 is
  `4f043b102e4d3b16c3475b6622535983ac2443d4d86bc7caa914b065a2a6dee8`.
- The fresh pass independently repeated the complete final static scope:
  exact candidate/tree/two-path scope, six internal roles and full histories,
  correction-only equivalence, all 32 evidence digests and reachability, 29
  approved boundaries, operator decision, 21 commands and applicability,
  project/legal limitations, exclusions, 17 non-vacuous mutation families,
  and cleanup. It is distinct from every internal identity.
- Root is assigned a new complete accumulated validation against unchanged
  candidate `1f87932`, including the unfiltered inventory first and all 21
  frozen command records under repository-local Python 3.12 and exact local
  Node 22. Result path is fixed as
  `docs/reviews/c3-b1-final-accumulated-validation-round-2.md`. No previous
  accumulated result transfers; fresh acceptance waits for this record's
  immutable pass.

### C3B1-MP001 fresh accumulated pass and acceptance assignment

- Recorded: `2026-08-27T19:17:40Z`. Fresh complete accumulated verdict:
  `pass`, committed at `421519d3f0a95a68ab8ee173083cf90006913244` in
  `docs/reviews/c3-b1-final-accumulated-validation-round-2.md`, SHA-256
  `f33c24102a8bd02927424744f44df4c486071cf5be4fe6208c8631611ff6b28a`.
- The unfiltered inventory reproduced exactly 657 passes and the three
  reviewed historical failures; the applicable run passed 657 with only those
  three deselections. All 21 frozen command classes passed under local Python
  3.12 and exact Node 22, including browser and accepted-threshold performance.
  The rejected malformed npm option placement is transparently recorded and
  no result from it transfers.
- Fresh final acceptance is assigned to identity `c3-b1-final-acceptance-2`
  (`/root/c3_b1_final_accept_fresh`), distinct from root, all six internal
  identities, fresh final verifier, and later manifest verifier. It may create
  only `docs/reviews/c3-b1-final-acceptance-round-2.md`, may repair nothing,
  and must return exactly `pass` or `changes_required` after auditing the exact
  candidate, C3B1-MP001 correction, fresh verification, complete accumulated
  evidence, scope, findings, exclusions, cleanup, and manifest readiness.

### C3B1-MP001 fresh acceptance pass and atomic manifest assignment

- Recorded: `2026-08-27T19:23:28Z`. Fresh acceptance identity/verdict:
  `c3-b1-final-acceptance-2` / `pass`; immutable record committed at
  `792fec42fef2c0b37aab80bcb48231dff9949e8b`. Record SHA-256 is
  `3eaa4dfdfe0b5a3ab002eb10c2a06cfb65433521674a18d839fa153fdf361724`.
- Acceptance independently confirmed candidate `1f87932`, FV001 and
  C3B1-MP001 correction ordering, all six internal identities/histories, 32
  digests and 20 reachable commits, five evidence groups, project/legal
  limitation, 29 exact approved boundaries, fresh distinct verification,
  fresh complete accumulation, applicability, exclusions, and cleanup. No
  finding remains open.
- Root is assigned atomic creation of only `testdata/evidence/c3-b1.json`.
  It must bind candidate/tree `1f87932` / `cbe33ca`, the truthful fresh primary
  verifier/acceptance identities, all already-existing evidence, exact command
  results, B1 requirement/stopping-condition ownership, and assigned fresh
  manifest identity `c3-b1-manifest-verifier-2`. It must predict no manifest
  verifier verdict, record, or manifest digest.
- After assembly, that fresh manifest verifier alone may create
  `docs/reviews/c3-b1-manifest-verification-round-1.md`. Both uncommitted files
  are committed together only after its independent digest/schema pass; the
  checkpoint remains later. No B2 authority exists yet.

### C3-B1 manifest verification round-1 findings and correction assignment

- Recorded: `2026-08-27T19:35:02Z`. Distinct manifest verifier
  `c3-b1-manifest-verifier-2` returned `changes_required`; immutable round-1
  record committed at `96d80b61781640eab36430e94de44a3d345f3e11`, SHA-256
  `d0cb35ed59b9674645ce7f5036d4c7e803c9f5ee21d6d9cdbe384d0424220a78`.
- `C3B1-MV001`: the goal, schema, and validator artifact rows use governing
  revision `ea83a403` even though their declared current bytes belong to
  commits `6a2d09a444797bb0b73c94b259b1cbd826084129` (goal) and
  `39e74a27638541b36b2845a8c6f1079bc0a3ae61` (schema and validator).
- `C3B1-MV002`: `python_applicable_nonhardware.command` paraphrases the three
  deselections instead of preserving the exact frozen command vector.
- Root is assigned correction of only those four manifest fields. Every other
  manifest byte and meaning remains fixed. Round 1 transfers no pass; the same
  distinct manifest-verifier identity must independently verify the corrected
  unchanged manifest and create only
  `docs/reviews/c3-b1-manifest-verification-round-2.md`. No manifest commit,
  checkpoint, or B2 authority exists before that fresh pass.

### Checkpoint C3-B1 — provenance, semantic fixtures, and approved limits

- State: Complete.
- Completed at: `2026-08-27T19:39:02Z`.
- Tested candidate commit: `1f8793210a3298ed190ff30f97c84b6f9feb9b29`.
- Tested candidate tree: `cbe33ca272ba1b452f6d87fb5e702134a471f702`.
- Candidate worktree state: exact two-path candidate committed and clean;
  immutable review/evidence descendants followed without changing its tree.
- Candidate creation commit: `1f8793210a3298ed190ff30f97c84b6f9feb9b29`.
- Implementation agent: primary Cycle 3 orchestrator; internal owners below.
- Verification agent and verdict: `c3-b1-final-verifier-2`; `pass`; record
  `docs/reviews/c3-b1-final-verification-round-3.md`, SHA-256
  `4f043b102e4d3b16c3475b6622535983ac2443d4d86bc7caa914b065a2a6dee8`.
- Accumulated-validation owner/result: primary orchestrator; fresh `pass`;
  record `docs/reviews/c3-b1-final-accumulated-validation-round-2.md`, SHA-256
  `f33c24102a8bd02927424744f44df4c486071cf5be4fe6208c8631611ff6b28a`.
- Acceptance agent and verdict: `c3-b1-final-acceptance-2`; `pass`; record
  `docs/reviews/c3-b1-final-acceptance-round-2.md`, SHA-256
  `3eaa4dfdfe0b5a3ab002eb10c2a06cfb65433521674a18d839fa153fdf361724`.
- Manifest verifier and verdict: `c3-b1-manifest-verifier-2`; fresh round-2
  `pass`; record SHA-256
  `de2beb2b416b455ed13644b6fa843737c512970f3e310890b659032a4d728853`.
- B1 internal candidate identities: semantic fixture implementation
  `c3-b1-semantic-fixture-implementor-replacement-6`, verification
  `c3-b1-semantic-fixture-verifier-1`, acceptance
  `c3-b1-semantic-fixture-acceptance-1`; runner implementation
  `c3-b1-pre-execution-runner-implementor-replacement-3`, verification
  `c3-b1-pre-execution-runner-verifier-1`, acceptance
  `c3-b1-pre-execution-runner-acceptance-1`. Complete ordered implementation
  histories remain bound in the final candidate.
- Completion-closure state: not applicable.
- Governing contract/goal identities: commit/tree
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`; approved goal bytes are bound in
  the manifest to byte-owning revision `6a2d09a444797bb0b73c94b259b1cbd826084129`.
- Prior checkpoint/manifest identity: accepted C2-B6 manifest
  `testdata/evidence/c2-b6.json`, commit
  `354c299903ec73633e5762a2b65adaae1d44e8d7`, SHA-256
  `ed8036ef48654efd98a5c3a852fb1f1dba847a34e12bf1c5dec253a2b9a83ffb`.
- Environment: macOS 15.7.7 build 24G720, x86_64, Macmini8,1, CPython
  3.12.13, Node 22.14.0, Chromium 133.0.6943.16, Playwright 1.50.1.
- Dependency identity: development/web locks
  `6f78ec8f0219b919c44ed9b9f1d30c2337fcce7c911b8d3dc4c13edb707a6575`;
  npm lock `d388a2668b3f65edeb62ee99da3ad37ffc56ab1ca3439b6d418a6bbe92e838d9`;
  `pip check` passed.
- Decoder/fixture identity: exact accepted fixture manifest SHA-256
  `0f5f1d9a01fc807dd0f4078ac84b20158f515a76ae4f1f83cc74651c4797413a`;
  exact project/legal, generator, caps, runner, method, raw, proposal, and
  review-chain digests are bound in the evidence manifest.
- Approved-limit identity: `docs/reviews/c3-b1-threshold-approval.md`, commit
  `b6d904064ab7b9e195eedded1c55efc306eeb925`, SHA-256
  `24665a2d63713275c9fc0a82243ee53852834cb36adbf8f6252221804d8b37bc`;
  all 29 exact round-2 values approved, including 900 ms successful-parent
  total and eight-bit maximum SPI word size.
- Objective evidence: independently derived deterministic semantic fixtures;
  non-decoder runner enforcement; immutable reproduced raw observations;
  reviewed/accepted/operator-approved limits; fresh final verification,
  complete accumulation, fresh acceptance, and manifest verification.
- R identifiers and stopping conditions: R1-R5, R9, R21, and R23-R25 mapped;
  stopping conditions 1-3 passed. B1 begins continuous evidence for later
  conditions without claiming final C3-B5 ownership.
- Files changed: authoritative fixture/generator/caps; characterization-only
  runner/method/binding; immutable raw observations; threshold proposal and
  operator decision; tests/reviews; final binder; schema-valid B1 manifest.
- Focused commands: fixture rebuild/binding, internal verification matrices,
  raw reproduction, threshold boundaries, final 20-test/17-mutation static
  verification, and independent 43-path/39-revision manifest audit passed.
- Accumulated commands: all 21 frozen command classes passed; unfiltered 660
  tests exposed only three reviewed historical failures, applicable 657 passed;
  exact Node 22 lint/type/five unit/build/assets/four browser/performance passed.
- CI evidence: not applicable to C3-B1; exact-candidate hosted macOS CI begins
  at its approved later owner.
- Resource/performance evidence: accepted raw characterization and thresholds;
  fresh retained performance report SHA-256
  `b676ca953d3c989dbbc06e2ea68b3e63f0e117fab6929b5c6bd1693e065dd2a9`.
- Project/license evidence:
  `docs/reviews/c3-b1-project-license-review-round-1.md`, SHA-256
  `b7afc4df18ba9bf5e40ee5a795e4544e54a59be27b1fea9a8617681ea82919cf`;
  recorded rights-holder/qualified-counsel limitation remains controlling.
- Prohibited dependency/runtime/process audit: complete active-source,
  dependency, import, command, evidence, and centralized process audits passed;
  no prohibited process remained.
- Evidence manifest: `testdata/evidence/c3-b1.json`, joint manifest/verification
  commit `c34a2517472a443e9d8ad7b41be800b272db9833`, SHA-256
  `580bd6ac8603602f43f9f2ca04bed552073f3de2e43df4ac35df81c1e720743b`;
  frozen strict validator passed. Manifest-verification record is in the same
  commit.
- Findings and dispositions: C3B1-RI011, C3B1-RI013, C3B1-TPV001,
  C3B1-FV001, C3B1-MP001, C3B1-MV001, and C3B1-MV002 are closed with immutable
  history. Manifest round-1 `changes_required` record remains at commit
  `96d80b61781640eab36430e94de44a3d345f3e11`.
- Decisions/discrepancies: all 29 values are exact inclusive maxima;
  unsuccessful or malformed invocations never transfer evidence; artifact
  revisions identify byte-owning commits separately from governing identity.
- Deferred findings: none; later approved work remains ordinary deferred scope.
- Known limitations: macOS-only; non-installed characterization runner only;
  no package build, conveyance, or distribution pending the recorded legal
  confirmation; B2-B5 final proof remains outstanding.
- Repository state: joint manifest commit tree
  `7a5a19ded862304313c16fb2c671e049da254f7b`; checkpoint appends only this
  orchestration record after that clean committed state.
- Next batch: C3-B2, after its bounded active-batch prerequisite/authority
  preflight and role assignment.
- Blocked: no.

## C3-B2: isolated compatibility host and containment

- State: Pending. B2 implementation exposed post-checkpoint authoritative
  fixture finding `C3B2-IF001`; the governing correction rule reopens the B1
  semantic-fixture gate before this batch may consume that fixture again.
- Objective: implement one private native host that accepts only validated
  inert requests, executes exactly one hash-pinned focused decoder in one fresh
  single-use Python worker, returns the frozen typed result, and enforces every
  approved parent/worker containment and cleanup rule without exposing a public
  library or CLI surface.
- Prerequisites: C3-B1 checkpoint `06ca562558014dc0a32588493b8d92d55359ae74`
  and manifest/verification commit
  `c34a2517472a443e9d8ad7b41be800b272db9833`; manifest SHA-256
  `580bd6ac8603602f43f9f2ca04bed552073f3de2e43df4ac35df81c1e720743b`;
  all 29 exact operator-approved ceilings; accepted immutable fixture, runner,
  method, raw, proposal, role, and correction evidence. Present and rechecked.
- Governing commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Starting commit/tree: `06ca562558014dc0a32588493b8d92d55359ae74` /
  `ef9f31bae92cca56e3b295033b2e2b1a180a9fc3`.
- Implementation agent: `c3-b2-private-host-implementor-1`
  (`/root/c3_b1_runner_impl_r4`), continuing only its implementation lane. It
  did not author B1 authoritative expected fixtures.
- Verification agent: `c3-b2-private-host-verifier-1`
  (`/root/c3_b1_final_verify_fresh`), continuing only its verification lane.
- Acceptance agent: `c3-b2-private-host-acceptance-1`
  (`/root/c3_b1_final_accept_fresh`), continuing only its acceptance lane.
- Manifest verifier: `c3-b2-manifest-verifier-1`
  (`/root/c3_b1_manifest_verify_fresh`), continuing only its manifest lane.
  All four canonical agents and stable B2 identities are distinct; root remains
  the separate orchestrator/assembler.
- B1 internal identity map: not applicable to B2. The implementation identity
  is a former runner implementor, never a semantic-fixture author; all B1
  expected fixture paths remain read-only.
- In scope: R6-R12 and R22; continuing R9, R21, R23-R25 audits; stopping
  conditions 4-8. Closed decoder/file/import tables; immutable private request,
  result, declaration, record, value, time, limit, and failure models; exact
  pre-spawn validation; frozen API-v3 primitives; one fresh worker; versioned
  streaming length-framed IPC; output normalization/counters; approved limits;
  deadline/cancellation; typed failures; deterministic kill/close/reap.
- Out of scope: decoder-specific B3 conformance/adapters; public
  `pico_logic_analyzer.decode` exports or `decode_capture`; installed `pico-la
  decode`; replay/CSV integration; browser/API/frontend; serial/live capture;
  hardware/firmware; dynamic discovery/paths/stacking/`.lac`; package build or
  publication; non-macOS claim; external/reference runtime; Cycle 4.
- Owned paths: implementation may add only
  `src/pico_logic_analyzer/_decode/`,
  `tests/implementation/test_c3_b2_private_host.py`, and
  `docs/reviews/c3-b2-implementation-round-1.md`. Any need for package metadata,
  locks, existing product modules, shared fixtures, or a different path returns
  to root before editing. Verification later owns only
  `tests/verification/test_c3_b2_private_host.py` and its immutable review;
  acceptance and manifest verification own only their fixed review records.
- Authoritative evidence: Step 5 frozen contract; accepted B1 manifest/binder;
  semantic fixture manifest and literal typed/JSON goldens; option matrix;
  experiment caps and 29 approved product ceilings; runner enforcement lessons
  but no transferred pass or implementation byte.
- Focused evidence: implementation-first failure; private host unit/contract
  tests; B1 API-edge fixtures; exact schema/canonical-byte repeats; digest,
  import-root, symlink/shadowing and inert-data negatives; hostile framed IPC;
  every limit boundary/overrun; cancellation/terminate/kill/close/reap; process
  and descriptor cleanup; successful valid request after every failure class.
- Accumulated evidence: complete B1 manifest/fixture/limit identity; all B2
  focused checks; frozen 21-command non-hardware matrix; Cycle 1/2 evidence and
  regression gates; dependency/import/process/scope audits.
- Authority notes: exact B1-approved snapshots may now execute only through the
  accepted closed host path. Use repository-local Python 3.12. No dependency or
  network operation is expected. Process inspection is root-brokered through
  the existing reusable `rtk ps` class; any new external capability must return
  `APPROVAL_NEEDED` under the broker policy.
- Prohibited runtime audit: active source/metadata/locks/imports/commands plus
  centralized process inspection must prove no C#/.NET/pythonnet/
  libsigrokdecode/`sigrok-cli` or external/reference runtime use. Preserved C#
  content remains inert read-only history.
- Risks and unknowns: worker resource controls and streaming IPC must implement
  the exact approved values without reusing characterization-only plumbing as a
  product shortcut; package-owned module launch must not create the B4 public
  API early; macOS containment is deliberately narrow and must not be presented
  as an OS sandbox.
- Preflight: clean branch at the exact starting commit/tree; strict B1 manifest
  validation, deterministic fixture rebuild, runner binding check, final
  20-test static verifier, and the manifest/approval/fixture/proposal digest
  checks all passed. No prerequisite byte changed.
- Implementation checkpoint: the uncommitted owned-path B2 work has a
  functional fixed-worker UART route, closed pinned imports, lifecycle/result
  projection, strict framed IPC, and inert compatibility coverage. It remains
  deliberately uncommitted and is not a candidate while its authoritative
  fixture prerequisite is reopened.
- Open finding `C3B2-IF001`: timeline
  `uart-msb-9bit-boundary-incomplete` declares UART `sample_point: 99`, but its
  expected wait trace uses the default 50-percent schedule and its expected
  records contain only the start-bit Python/annotation pair. Independent
  inspection of the frozen UART source and declarative transitions shows that
  the selected 99-percent option changes the sample coordinates and that
  already-emitted incomplete-frame bit annotations cannot be omitted under the
  accepted end-of-input rule. The accepted raw observation also differs, but
  it is characterization evidence only and is not an expected-output oracle.
- Finding evidence: the real private worker produced its first record at
  samples `5..15`; the fixture specifies `0..10`. The focused implementation
  suite currently reports `42 passed, 2 failed`: this exact semantic mismatch
  and one superseded implementation-local wait assertion. No result has been
  coerced, rebased, dropped, or relabeled to make the fixture pass.
- Required disposition: Step 5 requires a new independently authored and
  reviewed fixture candidate after the B1 gate. A fresh fixture-only
  implementor must derive the corrected wait trace and complete expected
  record sequence from the frozen source and declarative timeline without
  consuming decoder/host/raw runtime output as an oracle. Independent fixture
  verification and acceptance, affected digest/binder/manifest correction,
  and prerequisite checkpoint repair must complete before B2 resumes.
- Authority state: no external capability or shell authorization is missing.
  The remaining authority need is one fresh semantic-fixture implementation
  identity; the assigned B2 implementor is permanently barred from authoring
  B1 expected output, and the primary orchestrator is not an evidence identity.

### C3B2-IF001 renewed threshold approval and replacement final-B1 assignment

- Recorded: `2026-08-28T12:57:17Z`. The operator explicitly stated
  `I approve the exact committed round-3 threshold values in proposal b260d9e`.
- The immutable decision record is committed at
  `63fdfee87159251cdf525eb608340e6bc08ad010` in
  `docs/reviews/c3-b1-threshold-approval-round-3.md`, SHA-256
  `2a1f9cdb175115a1bf34983695ee382c228924f39aab1ffffb8a2480dbd29b60`.
  It binds exact proposal `b260d9ecc0e74ed2502dda89beebb851ddfedb77`,
  its rationale and proposal digests, fresh verification `92de4e6`, complete
  accumulation `c3cc274`, fresh acceptance `d922ba3`, all 29 inclusive and
  first-rejected boundaries, and the superseded-approval prohibition.
- Exactly 28 values remain numerically unchanged from round 2. The only change
  is `successful_parent_total_ns`, from 900,000,000 to 1,000,000,000 ns. The
  eight-bit maximum SPI word size remains exact. No value may be silently
  increased, weakened, rebased, or reinterpreted.
- Root is assigned the replacement final B1 integration candidate at exactly
  `testdata/decoders/cycle3/b1-final-candidate-round-3.json` and
  `docs/reviews/c3-b1-final-candidate-round-3.md`. It must remain
  `candidate-not-accepted` and bind the governing contract, the complete
  ordered semantic-fixture history through implementor replacement 7, the
  corrected fixture verifier/acceptance identities, the complete runner
  history and fresh rebinding verifier/acceptance identities, project/license
  disposition, corrected raw candidate and three fresh gates, round-3 proposal
  and three fresh gates, renewed operator approval, exact artifact digests,
  environment qualification, historical findings/dispositions, applicability,
  exclusions, and exact frozen accumulated commands.
- The candidate may add only those two binder artifacts. It may change no
  fixture, cap, generator, snapshot, runner, method, raw, proposal, approval,
  product, lock, workflow, governing contract, prior review/test, Cycle 1/2
  evidence, or preserved untracked B2 byte. Root will commit the immutable
  candidate before assigning fresh final B1 verification; no prior final-B1,
  manifest, checkpoint, or B2 pass transfers.
- Required downstream order is fresh final verification, a complete
  accumulated gate against that exact candidate, fresh final acceptance,
  atomic creation of only the replacement `testdata/evidence/c3-b1.json`,
  distinct manifest verification, joint manifest/verification commit, and a
  replacement B1 checkpoint. Only that replacement checkpoint may resume the
  preserved B2 work. No Cycle 4 authority exists.
