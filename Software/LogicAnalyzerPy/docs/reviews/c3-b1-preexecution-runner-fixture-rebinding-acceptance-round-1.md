# C3-B1 pre-execution runner fixture rebinding — acceptance round 1

## Identity, subject, and verdict

- Acceptance identity:
  `c3-b1-pre-execution-runner-rebinding-acceptance-1`
  (`/root/c3_b1_runner_rebind_accept_r1`).
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Exact runner-rebinding candidate/tree:
  `ca0ee7514c157c145bb3970fd2b884fbc8d9ea8a` /
  `457240c481afcdf20ef41a74208749e112efa9b6`.
- Fresh independent verification descendant/tree:
  `6a9f8a1451e7d887ba0dbe7fac1695ea0b55169c` /
  `f3a97c27d21a5d70856707726ac284700399a641`.
- Accumulated-validation descendant/tree:
  `a1f987f4d2651eeeebb4f61e16bd3499fbf142e3` /
  `cada42076901e6f27558e4224045c08fce624da6`.
- Verdict: `pass`.

This acceptance is an independent audit of the immutable candidate and its
committed evidence descendants. I did not repair or execute the candidate. I
created only this acceptance record.

## Acceptance findings

1. **Pass — immutable chain and candidate scope.** All four named commits and
   trees resolve exactly, and each descendant has the required direct parent.
   The candidate changes exactly five paths relative to its parent: the method,
   implementation record, focused implementation test, binding JSON, and
   runner. The verification descendant adds only its verifier record and
   verifier-owned test; the accumulated descendant adds only its accumulated
   record. The runner correction does not change a decoder snapshot, fixture
   generator, compatibility helper, worker, snapshot host, launch document,
   accounting implementation, probe source, product source, raw observation,
   threshold, manifest, checkpoint, or B2 path.

2. **Pass — role separation.** Runner implementor
   `c3-b1-pre-execution-runner-implementor-replacement-3`, independent verifier
   `c3-b1-pre-execution-runner-rebinding-verifier-1`, this acceptance identity,
   semantic-fixture implementor replacement 7, semantic-fixture correction
   verifier 1, semantic-fixture correction acceptance 1, the primary
   orchestrator, and the B2 implementor remain distinct in their governing
   roles. No prior runner, fixture, raw, proposal, final-binder, manifest, or B2
   pass is transferred.

3. **Pass — corrected fixture binding is exact and fail-closed.** The candidate
   binds corrected fixture candidate/tree
   `a98d328aab92f3dad66988fb70cc567946dc89d0` /
   `450aadcf26bd6c74860872bfbf0a0a1b32d94f3b`. Independently recomputed
   SHA-256 values are:

   - semantic fixture:
     `1d97cf3ff4fb560e7dd73b621da0e40d7f1fb310b60c2d43fcb59f3ebf91a329`;
   - experiment caps:
     `6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d`;
   - fixture manifest:
     `ce8eceb72480d042ef298cb6fe6944a4808fed0644e729c8c2de9fa1955ec37f`;
   - candidate binding:
     `144c08036cb3eca490586d8af33b223fc9abfe905182cec102248ccce2108f98`.

   The closed binding names all four accepted-fixture identities and exactly
   covers the method, runner/configuration files, accepted fixture artifacts,
   and nine pinned snapshot sources. The runner checks stale candidate commit,
   candidate tree, cap, semantic-fixture, and manifest identities before pipe
   or process creation. The corrected cap profile has exactly 17 positive
   values; its corpus-derived values include `request_bytes = 46456256`,
   `retained_result_bytes = 185825024`, and
   `worker_address_space_bytes = 68719476736`.

4. **Pass — fresh verification is independent and applicable.** The verifier
   record SHA-256 is
   `59bed0b1b0aac89b686425bf98e7b63b106b80b31a71c0e48b9dc5e6204a9031`;
   its test SHA-256 is
   `14793a958bdfa4bc92cb8a46115b413d70f8d0cd9e7fb28fb65ef0f8197f0562`.
   The verifier independently checked every stale fixture identity before
   process setup, all 17 cap value/value-plus-one boundaries, source-map
   equality, binding recomputation, and the retained inert/hostile runner
   controls. Candidate-owned bytes are unchanged in the verifier descendant.
   The record reports no decoder or approved snapshot execution and no open
   finding.

5. **Pass — accumulated validation is complete and candid.** The accumulated
   record SHA-256 is
   `8b25ddb7cabed91b4fa85d95a650685023048e9a2037e9415271a0d9e261eb6c`.
   It records a clean Python 3.12.13 hash-locked installation, dependency check,
   whole-project Ruff, strict mypy, CLI, generator and binding checks, six
   Cycle 2 validators, exact 64-GiB resource-limit readback, and exact Node
   22.14.0 install/lint/type/unit/build/assets/browser/performance gates. The
   focused implementation plus verifier suite passed 180 tests. This acceptance
   reran that inert suite and the binding check: 180 tests passed and the
   binding recomputed without drift.

6. **Pass — full-suite accounting and invalidations are exact.** The unfiltered
   clean suite is not represented as green: 650 tests passed and 44 failed.
   One failure is the historical exact-six-file fixture-inventory assertion.
   The other 43 failures are confined to exactly five deliberately invalidated
   downstream B1 modules: the former runner-candidate verifier, raw-baseline
   verifier, both threshold-proposal verifier generations, and final-candidate
   verifier. The applicable rerun ignored exactly those five modules and
   deselected exactly that historical inventory assertion; it passed 603 tests
   with one deselection. These are dependency-order invalidations, not waivers.

7. **Pass — reusable approval handling is bounded.** The accumulated record
   reports that the initial network-restricted locked-install attempt failed
   before installing a package and root retried the same stable, hash-locked
   pip command class once through the central approval broker. No broad
   interpreter approval, package-by-package request, or subagent escalation was
   used. Exact stable Node 22 browser and performance command classes were
   reused separately. Failed setup attempts supplied no evidence.

8. **Pass — scope and safety remain closed.** This audit used immutable Git
   inspection, SHA-256 recomputation, the existing inert/hostile test suite,
   and binding recomputation only. It did not run a decoder, compatibility
   helper, snapshot host with decoder input, worker with decoder input, fixture
   generator write, raw collection, threshold execution, browser, hardware,
   product host, B2 test, or excluded runtime. The untracked B2 paths
   `src/pico_logic_analyzer/_decode/` and
   `tests/implementation/test_c3_b2_private_host.py` were neither inspected nor
   modified.

## Invalidation boundary and next authorized gate

This pass accepts only the exact unchanged runner-rebinding candidate and its
fresh verification and accumulated evidence. It replaces the invalidated old
runner gate but does not revive or transfer any old raw-baseline, threshold,
operator-approval, final-B1, manifest, checkpoint, or B2 result.

Under C3-B1 mandatory gate order, this pass authorizes the exact unchanged
runner at `ca0ee751...` to execute only the approved checked-in UART, SPI, and
I2C snapshots under the accepted caps for a new raw-baseline candidate. Any
runner, method, launch/import, binding, digest, cap-plumbing, cleanup,
environment-class, or worker-model change creates another runner candidate and
repeats runner verification, accumulation, and acceptance before execution.

The mandatory downstream sequence is: fresh raw collection and immutable raw
candidate; fresh raw verification, accumulation, and acceptance; fresh
threshold proposal verification, accumulation, and acceptance; renewed
explicit operator approval even if all 29 product values are proposed
unchanged; a new final B1 binder with fresh verification, complete accumulated
validation, and acceptance; atomic replacement-manifest assembly plus distinct
manifest verification and joint commit; and a replacement B1 checkpoint. Only
that replacement checkpoint permits B2 to resume and rerun its focused proof.

Open findings: none.

## Verdict

`pass`
