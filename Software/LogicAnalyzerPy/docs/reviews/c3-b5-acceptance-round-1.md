# C3-B5 pre-manifest acceptance — round 1

## Identity and boundary

- Acceptor: `c3-b5-final-acceptor-1`, distinct from every B5 implementation,
  verification, accumulated-validation, and later manifest/closure role.
- Governing contract/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Accepted B4 checkpoint: `9a8fc46ba4bc73cd007d678b85b6510bba0eeb87`.
- Exact corrected implementation candidate/tree:
  `f8f78c89655011e3ee3e74559ff9886c93eac690` /
  `e6b5d5f0afaf3023ec398cb9c42c6d42d5a1790b`.
- Fresh verifier evidence commit/tree:
  `2fb89fc8c36d93b4435032c07783532d6a8aa933` /
  `f155c06c8d61e9f454f2b7026afa0805999c4300`.
- Accumulated-validation commit/tree:
  `eab754f565dd53fa1ab1a0ba844297c4cbb2b075` /
  `ece2de011bdc7a1c81ec4ad2b6a61c6994baaf9a`; record SHA-256
  `8b3fa36966820f3d65819805be889d4fe54314d844b81b9cc12da8e8e8abcef4`.

This is strictly pre-manifest acceptance. I changed only this review. I did
not create, require, name, hash, or predict a B5 manifest or checkpoint,
completion proof, closure verdict/record, or completion seal.

## Independent audit and reproduction

I verified the complete ancestry and exact trees from the governing contract
and accepted B4 checkpoint through the corrected candidate, fresh verifier,
and accumulated record. Candidate and evidence digests recomputed exactly:

- implementation test:
  `8914ca125aa2ed132f7eabdff8d148045132bce447222d75ac9860b0175689f6`;
- final measurements:
  `980308fc3a144d1af70959793fb9e0b4476658b9856d56eb101876fc9fedb54e`;
- implementation review:
  `60c059d4c3878e5aa5726acc31f72170266064cb0d2243bc5ed339048dd186ea`;
- verifier test:
  `8bd21ab5ebd2f18bae0cae9ffdb702e97e5fb6e8638cfb1e66c0fa02be2f0b72`;
- verifier review:
  `95157008368c868c66d89b239ff7e8f206564e70836ec6c404384c120c6e6389`;
- hosted workflow:
  `12ff6bb2cd7e437b733f3aaeb9488c6926604572419468c60604f0dea1c6a990`.

All four accepted B1--B4 manifests independently passed the frozen Cycle 3
schema validator and retained exact SHA-256 values `3710e7fd...`,
`2af5bfc2...`, `4d17a6f0...`, and `699443c5...`. Their committed histories show
implementation, fresh verification, complete accumulation, fresh acceptance,
then unchanged manifest plus distinct verifier committed atomically before a
separate checkpoint. Failed findings and corrections precede each governing
pass. In particular, C3B5-V001 is preserved, the corrected collector has one
warm-up per protocol plus five retained repetitions per protocol, and the
round-2 verifier transfers no pass from round 1.

The raw final packet binds exact approved proposal `b680aa59...` and its
SHA-256 `98e48bb1...`, B1 method SHA-256 `f228f028...`, and semantic-fixture
SHA-256 `34d2a114...`. It records Darwin/x86_64 CPython 3.12.13, three
unrecorded warm-ups, 15 retained rows, and 18 launches total without retry or
outlier deletion. Five rows exist for each of UART, SPI, and I2C. Every one of
the 11 observed regression maxima is below its unchanged ceiling. The 18 hard
limits retain exact inclusive/rejected boundaries, including SPI eight/9;
together these are all 29 operator-approved values. Fresh verifier evidence
also covers the hostile timeout, cancellation, terminate, kill, close, reap,
recovery, IPC, and output-bound paths that successful final measurements
correctly represent as zero cleanup observations.

My proportional acceptance suite passed 696 tests across B5 final packet,
B2 private host, UART/SPI/I2C conformance, cross-source equivalence, and B4
public API/CLI implementation and final verification. Both current dependency
consistency and Ruff passed; strict mypy passed all 31 production source files.
One initial pytest selection named a nonexistent generic B4 verifier path and
collected no tests; the corrected explicit final-verifier selection produced
the reported 696-pass result. Likewise, an initial Ruff path typo was rejected
before the corrected source selection passed. Neither invocation changed a
file or supplied evidence.

Fresh GitHub API inspection confirms run `33655002746`, job `100331249147`,
exact head `2fb89fc8c36d93b4435032c07783532d6a8aa933` and tree
`f155c06c8d61e9f454f2b7026afa0805999c4300`, workflow path
`.github/workflows/logic-analyzer-python-cycle2.yml`, attempt 1, and final
`success`. The job ran on label `macos-15-intel` from
`2026-09-02T16:27:29Z` to `2026-09-02T16:44:30Z`; every recorded step passed,
including pinned CPython 3.12.13, locked core/web installs, dependency/static
gates, nonhardware tests, installed CLI, exact Node 22.14.0, frontend build,
asset drift, Chromium, and production browser smoke.

## Requirements, stopping conditions, and findings

- R1--R5 and R9 are bound by accepted B1 snapshot/provenance/license,
  independent fixtures/goldens, method/environment, and exact operator limits.
- R6--R12 and R22 are bound by accepted B2 closed-host, prelaunch validation,
  typed lifecycle, hostile IPC, parent-enforced limits, cleanup, and recovery.
- R13--R16 are bound by accepted B3 UART, SPI, I2C, and independently
  materialized in-memory/replay-1/replay-2/CSV equivalence evidence.
- R17--R20 are bound by accepted B4 installed typed library, CLI, single-host
  delegation, web/serial separation, clean locked validation, and hosted CI.
- Continuous R21 and R23--R25 are carried by every checkpoint and the complete
  B5 accumulated gate. R26 is established by the corrected final packet and
  independent verifier reproduction on the characterized environment class.

The same evidence maps stopping conditions 1--3 to B1, 4--8 to B2, 9--10 to
B3, 11--12 to B4, 13--14 and 16--17 continuously across accepted checkpoints,
and 15 to the unchanged-limit final measurements. Thus conditions 1--17 pass.
The already committed inputs are ready for the directed condition-18 chain;
no later link exists yet, which is the required pre-manifest state.

No unresolved implementation, verifier, accumulated, hosted, manifest-history,
source/license/support/rollback, repository, requirement, or stopping-condition
finding remains. The working tree was clean before this review. The
GPL-3.0-only engineering disposition and inherited notices are preserved; the
B1 rights-holder or qualified-counsel requirement remains controlling before
conveyance. This is no legal conclusion and authorizes no conveyance.

No external/reference decoder runtime, browser decoder, hardware, firmware,
serial/live capture, dynamic discovery, stacking, `.lac`, package build,
publication, unsupported-platform claim, excluded feature, or Cycle 4 action
occurred. `APPROVAL_NEEDED`: none.

## Verdict

`pass` for the exact corrected candidate and committed evidence identities
listed above. They are accepted as ready only for root assembly of the
post-acceptance B5 manifest and its distinct verification. No later terminal
artifact is accepted or authorized out of order by this verdict.
