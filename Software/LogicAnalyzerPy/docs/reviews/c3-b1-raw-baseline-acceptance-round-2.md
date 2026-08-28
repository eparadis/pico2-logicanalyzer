# C3-B1 raw-baseline acceptance — round 2

## Identity, immutable subject, and verdict

- Acceptance identity:
  `c3-b1-pre-execution-runner-rebinding-acceptance-1`
  (`/root/c3_b1_runner_rebind_accept_r1`), continuing only in its independent
  acceptance lane.
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Accepted runner-chain descendant/tree:
  `bf1fc5eaa232bf09e66df77bd1c4be3e1ae4ffbd` /
  `5ec3ec00d09ab4ac5dd0d6ab258e19dcbb09ab64`.
- Exact raw candidate/tree:
  `2ae1e4335c38a5cf717491c7936f857292f71498` /
  `772b13476c97a976eb3a304e9b87aec8011260ec`.
- Superseded round-2 verification commit:
  `b76554ce2c28d83ea6f88fbfe4275ea07d517431`.
- Corrected round-3 verification descendant/tree:
  `10a6a1f72fc4973c112bd1da0877ffdc2590f3f8` /
  `bb555307abe49d95dd2eda54ce2621c2cb56949e`.
- Accumulated-validation descendant/tree:
  `68242a9b2a173432ad465b514dac9369821c3723` /
  `64140a0d318ab3a69aead626b86c665e6623203a`.
- Verdict: `pass`.

This is an acceptance audit of immutable evidence, not raw implementation or
reproduction. I did not repair the candidate or verifier and wrote only this
record.

## Acceptance findings

1. **Pass — ancestry, scope, and role separation.** The contract, accepted
   runner chain, raw candidate, both verifier rounds, and accumulated
   descendant resolve in the declared order with exact trees. The primary
   orchestrator owns raw collection and accumulation; independent verifier
   `c3-b1-pre-execution-runner-rebinding-verifier-1` owns only its verification
   evidence; this identity owns only acceptance. The runner implementor,
   semantic-fixture author/reviewers, raw author, verifier, acceptance auditor,
   B2 implementor, and later proposal roles retain their governing boundaries.
   No expected-output author implemented product behavior, and no old raw,
   proposal, operator-approval, final-B1, manifest, checkpoint, or B2 pass is
   transferred.

2. **Pass — exact five-file raw closure.** The candidate changes four raw files
   relative to the accepted runner parent and deliberately retains the existing
   request corpus as the fifth member of one closed raw set. All five are
   canonical newline-terminated JSON. Independently recomputed SHA-256 values
   are:

   - environment:
     `fd8b2cd798678d0b9c6cb6b1e71e02ec71738183a1e5b84ebd71fb90ee7c7b34`;
   - requests:
     `fe5b345270eced91298250032411b6a85112c55baf46d3b71afb424ef385f94c`;
   - observations:
     `28e1b9a2276eda2ca1c4cc1e8740b774e29125521aca5e45c31f3e4b1e8791cd`;
   - hostile observations:
     `d8ef77f4293ff1e49d5772b6bb44df61f3dc4cfa37ceda13dcb54a3cce74d080`;
   - raw manifest:
     `7c964750841e80d0c4bad606d2b76da8575a330d65836aaca8a9284a0668608e`.

   The manifest has an exact four-member content map excluding itself, names
   exactly UART, SPI, and I2C, records 63 timelines and five repetitions, and
   closes the accepted identities without an extra or missing raw path.

3. **Pass — identities, environment, caps, and provenance are exact.** Both
   environment and raw manifest bind runner candidate/tree
   `ca0ee7514c157c145bb3970fd2b884fbc8d9ea8a` /
   `457240c481afcdf20ef41a74208749e112efa9b6`, runner acceptance
   `bf1fc5e...` with record SHA-256
   `6dae8c73787dc7908e0ec311c84325251482d32073cc2fd6083147ead943e060`,
   corrected fixture candidate/tree `a98d328...` / `450aadcf...`, binding
   `144c08036cb3eca490586d8af33b223fc9abfe905182cec102248ccce2108f98`,
   semantic fixture
   `1d97cf3ff4fb560e7dd73b621da0e40d7f1fb310b60c2d43fcb59f3ebf91a329`,
   fixture manifest
   `ce8eceb72480d042ef298cb6fe6944a4808fed0644e729c8c2de9fa1955ec37f`,
   and caps
   `6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d`.
   The environment records all 17 exact caps and nine exact provenance source
   digests, CPython 3.12.13, macOS 15.7.7 build 24G720, x86_64 Macmini8,1, and
   the resource-observation mechanisms used during collection.

4. **Pass — request, observation, hostile, and summary accounting is closed.**
   The request set has exactly 63 unique ordered cases derived independently
   from static transitions, mappings, counts, samplerates, options, and
   provenance file sets. Observations have the same 63 IDs; each records one
   status-only unretained warm-up and five successful retained repetitions.
   The hostile set has exactly ten kinds: two designed successes (`limits` and
   `address_space_over`) and eight classified failures, each with one
   unretained warm-up and five retained observations. Every expected-failure
   retained observation has a successful recovery. Recomputed min/median/max
   triples match every count, timing, RSS, and cleanup summary; non-vacuous
   mutations of manifest, snapshot, and hostile-cleanup summaries are rejected.
   My static-only rerun passed the three identity/schema/arithmetic, mutation,
   and independent-request-derivation tests.

5. **Pass — corrected verification fully reproduces the evidence.** Round 3
   used the clean verifier environment and performed exactly 486 child
   launches: 63 snapshot warm-ups plus 315 retained snapshots; ten hostile
   warm-ups plus 50 retained hostile runs; and eight recovery warm-ups plus 40
   retained recoveries. All 63 snapshot semantics and stable counts matched
   five of five. Both designed hostile successes passed five of five, all eight
   expected failures failed as classified, and every recovery succeeded.
   Every child was exactly reaped and both raw protocol descriptors closed.
   The corrected verifier-test SHA-256 is
   `b29634ace872049ce275d93bc81274e0776236d688b6ef2cbbb243922b0db016`;
   the round-3 record SHA-256 is
   `8fdf25cd7da0b07deae21631709a1a5b76700f233af5590fae0cf1eee4f4c2eb`.

6. **Pass — `C3B1-RV001` is correctly resolved without weakening candidate
   proof.** Round-2 verification reproduced every case, but its test incorrectly
   required the immutable collection executable path to equal the clean
   verifier's `sys.executable`. The first clean accumulated attempt truthfully
   failed that assertion with 606 passed, one failed, and one deselected, so
   the round-2 portability claim and verifier-test SHA supply no pass. Round 3
   changed only verifier-owned test and record paths. It now checks the exact
   collection executable as collection provenance while separately checking
   exact recorded Python version and CPython implementation against the clean
   verifier. No raw byte, identity, schema, digest, request, semantic, count,
   arithmetic, mutation, cleanup, cap, resource, or process assertion was
   removed or weakened. The raw candidate remains unchanged.

7. **Pass — timing and RSS discrepancies are preserved as observations.** In
   the final round-3 reproduction, snapshot total-time relations versus the
   recorded ranges were three higher/non-overlapping, 44 lower/non-overlapping,
   and 16 overlapping; parent-total relations were the same. Launch relations
   were 14/2/47, reap 22/0/41, child import 0/16/47, child load 0/4/59, and
   child decode 1/2/60 for higher/lower/overlap. Child max-RSS had 18
   lower/non-overlapping and 45 overlapping cases. Parent cumulative
   `ru_maxrss` was higher/non-overlapping for all 63 comparisons because the
   verifier process had already loaded pytest and corpus data. These complete
   discrepancies are retained, do not change semantic or stable-count results,
   and are not treated as limits, thresholds, failures, or substituted
   measurements.

8. **Pass — accumulated validation is complete where applicable.** The
   accumulated record SHA-256 is
   `dc7901f4ffe82a8f1ff261a565025ccc607bb48fec84f8fd361bff1ae8030c09`.
   A clean exact corrected-verification clone passed hash-locked Python 3.12.13
   setup, dependency checks, whole-project Ruff, strict product and runner
   mypy, fixture and binding checks, CLI help, exact 64-GiB resource-limit
   readback, six Cycle 2 validators, and 607 applicable tests with one exact
   historical inventory deselection. That suite included a second complete
   486-launch reproduction; its report SHA-256 is
   `9c79b32e8488bd6aa9118cfa799f7442249b2fbf08a83f90348b0980e504b1f7`.

9. **Pass — downstream failure accounting is transparent.** The separately
   targeted invalidated set reported 43 failures and 45 passes. Failures are
   exactly one historical exact-six-file fixture assertion, 18 old final-
   candidate assertions, one superseded runner-candidate assertion, 22 old
   threshold-proposal assertions, and one old round-2 threshold assertion.
   The applicable suite ignored only those four downstream verifier modules
   and deselected only the historical inventory assertion. These are ordered
   invalidations, not waivers, and must be rebound by their owning gates.

10. **Pass — inherited Node regression and cleanup are complete.** Exact Node
    22.14.0 passed the locked 215-package install, ESLint, TypeScript, five
    Vitest tests, Vite build, asset drift check, one maximum-width browser test,
    three live/shell browser tests, frozen B6 performance test, and clean
    threshold check. The performance report SHA-256 is
    `9d72ea71b240367d75288da5cba94d021ccecf95fb842fa2f9a60b636292bb04`.
    Final process audits found no retained test, browser, Vite, pytest, runner,
    worker, or decoder process; raw reproduction boundaries left no tool
    bytecode cache. Validation-local clone symlinks and Playwright output are
    untracked and do not alter candidate bytes.

## Scope exclusions and next gate

This acceptance used immutable Git inspection, SHA-256 recomputation, JSON
inspection, and three static verifier tests only. It did not execute a decoder,
snapshot, worker reproduction, fixture-generator write, threshold, browser,
product host, hardware, C#/.NET/pythonnet/libsigrokdecode runtime, publication,
or B2 behavior. The two untracked B2 paths were neither inspected nor modified.

This pass accepts only exact raw candidate `2ae1e433...` with corrected
round-3 verification and accumulated evidence. It authorizes only preparation
of a fresh threshold-proposal candidate derived from this exact accepted raw
evidence. It approves no threshold, ceiling, performance value, product limit,
operator decision, final binder, manifest, checkpoint, or B2 resumption. The
proposal must receive fresh independent verification, complete accumulated
validation, and acceptance, followed by renewed explicit operator approval of
the committed values even if all proposed values remain numerically unchanged.

Open findings: none. `C3B1-RV001` is resolved.

## Verdict

`pass`
