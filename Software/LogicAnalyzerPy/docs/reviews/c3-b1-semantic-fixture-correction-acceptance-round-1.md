# C3-B1 semantic-fixture correction acceptance — round 1

## Identity and subject

- Acceptance identity: `c3-b1-semantic-fixture-correction-acceptance-1`
  (`/root/c3_b1_final_accept_fresh`), independent of the implementor,
  verifier, B2 implementor, primary orchestrator, and later manifest verifier.
- Completed: `2026-08-28T04:23:23Z`.
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Exact correction candidate/tree:
  `a98d328aab92f3dad66988fb70cc567946dc89d0` /
  `450aadcf26bd6c74860872bfbf0a0a1b32d94f3b`.
- Finding: `C3B2-IF001`.
- Candidate owner:
  `c3-b1-semantic-fixture-implementor-replacement-7`.
- Fresh verification identity:
  `c3-b1-semantic-fixture-correction-verifier-1`
  (`/root/c3_b1_final_verify_fresh`).
- Verification descendant commit:
  `b708293ec7e2f4f938e6fb6c669304ee2dba8721`; record SHA-256
  `092dadbce88288a544b4c7c14253095a580765501cd60afc6ceaaa5cad3cf2e2`;
  verification-test SHA-256
  `d5a6a3f69fcdaf2b5d86e334d0091c758f7bb67c33b1e9b6bca2c056efe9a75d`.
- Accumulated-validation descendant commit/tree:
  `1054cf30aeb66248451ad5945fe89e8b2e92990c` /
  `7a94b55ff6536bddb91a9a82c946905537059d8e`; record SHA-256
  `6e9a6db5e9c4d93c889e6514fa1fec694d41c11892f1f71240711cab32f0139a`.

This acceptance is a static audit of the exact correction and its committed
evidence descendants. It did not repair the candidate or run a decoder,
worker, characterization runner, raw observation, B2 host/test, browser,
hardware, network, install, build, or publication action. The main worktree's
untracked B2 implementation paths were excluded and left untouched.

## Findings and dispositions

1. **Pass — exact candidate and role separation.** The candidate tree resolves
   exactly and changes only six tracked paths: its implementation record,
   deterministic generator, semantic fixture, experiment caps, fixture
   manifest, and focused implementation test. Candidate, fresh verifier, and
   accumulated commits are in that order. Implementor replacement 7, fresh
   verifier, this acceptance identity, the B2 implementor, orchestrator, and
   future manifest verifier are distinct. No pass transfers from the old B1
   fixture, runner, raw, proposal, binder, manifest, or checkpoint histories.

2. **Pass — `C3B2-IF001` is closed from static authority.** Independent review
   of the frozen UART formula and declarative transitions gives frame start 1,
   bit width 10, 99-percent centers 10, 20, 30, 40, and 50, with the next
   center 60 beyond sample count 56. Real post-start edges are 11, 21, 31, and
   41; `[51,0]` is not an edge. The candidate therefore has exact returns
   1, 10, 11, 20, 21, 30, 31, 40, 41, 50, and terminal 56, including idle
   alternatives 110/101 after the rising-edge candidates. It preserves exactly
   six request-ordered pre-EOI records: STARTBIT Python and annotation at
   `[5,15)`, then RX bit annotations 1, 0, 1, 0 at `[15,25)`, `[25,35)`,
   `[35,45)`, and `[45,55)`. It invents no DATA, binary, FRAME, completed, or
   partial-unit result. This conclusion uses inert source text and the settled
   Step 5 rules, never runtime output or the prior raw mismatch as oracle.

3. **Pass — deterministic artifacts and digest closure.** Recomputed SHA-256
   values are: implementation record
   `6f9b3c483d2324187ad9c3a571fdd6ff5979aaf5f21142c471ded1b021327b66`,
   generator
   `d872fe9f6c1cb3407a8d05d7b9e03e3bb34b10baee8fa47e55b57bb4b64574f6`,
   semantic fixture
   `1d97cf3ff4fb560e7dd73b621da0e40d7f1fb310b60c2d43fcb59f3ebf91a329`,
   experiment caps
   `6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d`,
   fixture manifest
   `ce8eceb72480d042ef298cb6fe6944a4808fed0644e729c8c2de9fa1955ec37f`,
   and implementation test
   `fccc9746dfd50766cb3f6fbae72f08dfd40d57c791792ead2c76cf2eb6d68f45`.
   Every manifest artifact and generator binding recomputes. Static AST review
   found only the closed standard-library imports and no dynamic execution,
   raw-characterization, subprocess, decoder-runtime, or external-runtime
   path into the oracle.

4. **Pass — cap correction is complete and remains experiment-only.** The
   canonical semantic corpus is 725,879 bytes. All 17 finite cap formulas,
   named bases, multiply/max-floor operations, results, inclusive accepts, and
   first rejected integers recompute. Corpus-dependent request bytes are
   46,456,256 and retained-result bytes are 185,825,024. The address-space
   value remains the 64-GiB floor, 68,719,476,736, with the corrected corpus
   basis. The files explicitly claim no enforcement and no operator-approved
   product threshold; executable enforcement belongs to the later runner
   correction.

5. **Pass — unaffected authority is byte-stable and coverage is preserved.**
   Provenance remains
   `e0a6082869cdf51e7abf74441065b080b8e1d6614a45ad52f034ef95f4f4c8e4`,
   option matrix
   `5d84b9d9855e9e2e75d45d5cd9560fbcfd1ac6ff88abfcf1c1326d3427ffc209`,
   and typed vectors
   `b5cc317ff476fcb2446eaf6b376c346210f63fbca8d0df84984b7990a528ffbf`.
   They are unchanged from the candidate parent. The corpus retains 63
   timelines, five edge decisions, and five optional-pin cases. All 165 unique
   option rows remain present: 62 direct fixtures and 103 unsupported rows.
   `uart-sample_point-99` still binds the separate
   `direct-uart-sample_point-99` fixture, so the corrected incomplete-boundary
   case neither captures nor weakens the option-matrix witness.

6. **Pass — fresh verification is applicable and independent.** The verifier
   derived the expected UART schedule and six emissions before inspecting the
   correction, excluded B2 work and runtime authority, recomputed artifact and
   cap closure, and passed 20 focused tests including 14 non-vacuous mutation
   families. Its one verifier-local E501 correction did not change candidate
   bytes. Its classified exact-six-file historical inventory failure and broad
   mypy non-gate are transparent and do not weaken any applicable correction
   gate. It reports no open candidate finding.

7. **Pass — the unfiltered failure set is exactly and transparently
   partitioned.** The clean unfiltered suite reported 512 passed and 149
   failed, not a false green. Independent parsing of its retained `lastfailed`
   inventory confirms exactly one historical inventory failure plus 148
   failures confined to the six necessarily invalidated downstream modules:
   85 runner implementation, 20 runner verification, two raw-baseline
   verification, 22 threshold-proposal round 1, one threshold-proposal round
   2, and 18 final-candidate verification failures. No unrelated module is in
   that inventory. The applicable rerun ignored exactly those six modules and
   deselected exactly the one historical inventory assertion; it passed 403
   tests with one deselection. This is a temporary dependency-order exclusion,
   not a waiver or reusable pass.

8. **Pass — complete accumulated validation is green where applicable.** A
   clean detached candidate clone passed the fresh hash-locked Python 3.12
   install, no-dependency editable install, dependency check, whole-tree Ruff,
   strict mypy over 21 source files, installed CLI help, deterministic
   generator check, 11 applicable fixture tests, 20 verifier tests, all six
   Cycle 2 evidence validators, and the precisely applicable 403-test suite.
   The clean exact Node 22.14.0 regression then passed install, lint, type,
   Vitest, Vite/assets, maximum-width, live/shell, performance, and threshold
   checks. The initial ambient Node 26.7.0 npm performance attempt failed its
   frozen method metadata and supplied no evidence; the final direct exact-
   Node-22 run passed with retained performance-report SHA-256
   `f623165d9a68e4af67c5872348f607618ae2d9ffcf1a53fc54725698e3808358`.

9. **Pass — scope, cleanup, and authority remain bounded.** The accumulated
   evidence records a root-visible clean process audit after browser and
   performance completion, with no retained browser server, decoder, worker,
   characterization runner, or prohibited runtime. This acceptance's attempted
   additional read-only process listing was sandbox-denied and supplied no new
   evidence; no escalation is needed because the committed accumulated audit
   is the owning cleanup evidence. No hardware, product-host, public API/CLI,
   distribution, B2 execution, or Cycle 4 authority is claimed.

10. **Pass — downstream invalidation and resumption order are explicit.** This
    fixture acceptance alone does not resume B2. The changed fixture, cap, and
    manifest identities require, in order: a new runner candidate/rebinding;
    fresh inert/hostile runner verification, accumulated validation, and
    acceptance; a new raw-baseline run with fresh raw verification,
    accumulation, and acceptance; a new threshold proposal with fresh
    verification, accumulation, and acceptance; renewed explicit operator
    approval even if all 29 product values are proposed unchanged; a new final
    B1 binder with complete histories/digests, fresh final verification,
    complete accumulated validation, and fresh final acceptance; then atomic
    replacement-manifest assembly, distinct manifest verification, their joint
    commit, and a replacement B1 checkpoint. Only after that checkpoint may B2
    resume and rerun its focused proof. No earlier B1 or B2 result transfers.

## Static inspection record

All shell commands used RTK. Inspection resolved commit trees and ancestry,
enumerated the exact candidate diff, recomputed all named SHA-256 values and
manifest bindings, parsed JSON corpus/matrix/cap structures and formula
boundaries, inspected the corrected timeline, statically parsed generator
imports/calls, reviewed governing Step 5/order text and all three correction
records, and parsed the accumulated suite's cached failure inventory. One
exploratory matrix count used the nonexistent key `coverage` and exited before
producing matrix evidence; the corrected read used `disposition` and confirmed
62/103. No executable product behavior was invoked.

Open correction-candidate findings: none.

## Verdict

`pass`
