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
