# C3-B2 independent acceptance — round 1

Identity: `c3-b2-private-host-acceptance-replacement-1`.

Verdict: `changes_required`.

## Immutable subject and ordering

This fresh acceptance audit is bound only to governing contract
`ea83a403bb6f644d33069d3bebd41d5f1e0a60c0`, tree
`d9fb09345ab85580cd8c877745262d1b481e366f`; corrected B1 checkpoint
`d4f984d26ca45dcd0f70da51ad739da427e23be4`; B1 manifest commit
`885be61a2bbea8bf5261b3983cbc79fedde0f315`; approved round-4 proposal and
decision `b680aa59fba4a18da2aeaacc8cbd7ad3a68784e0` and
`afd45856ee261158521b902dabdf926e5f1f922a`; exact B2 candidate
`d8e14bbe490035894f3103a1289b27464a89d0d6`, tree
`0ca3d0aec612183e3da01b24f341580743489d38`; fresh verifier pass
`5178a63eeb56abc623d4bc10a0a5ae68eb868299`, tree
`3105c6cf683b3ba6ffb4f5198bcaeffba85d9608`; and complete accumulated pass
commit `bba6662e24a67fade4281083dea5d6d87dd9073e`.

The accumulated record is
`Software/LogicAnalyzerPy/docs/reviews/c3-b2-accumulated-validation-round-1.md`,
SHA-256 `357432e082180495aba64a6d9fdc58f03d4d849c4eb73a9421292fad83e87ae5`.
The ancestry chain B1 checkpoint -> candidate -> verifier pass -> accumulated
pass was independently confirmed. Candidate-to-verifier changes are limited to
progress plus the round-3 verifier test/record, and verifier-to-accumulated
changes are limited to progress plus the accumulated record; candidate product
and implementation-test bytes therefore remain bound to the audited tree.
Audit completed `2026-08-31T14:24:39Z` from clean branch `python-rewrite` at
`bba6662e24a67fade4281083dea5d6d87dd9073e`, before creation of this owned
record.

No verdict transfers from failed candidates or findings `C3B2-II001`,
`C3B2-V001`, and `C3B2-V002`. Their immutable history and later dispositions
were inspected and preserved. The fresh verifier identity, accumulated owner,
this acceptance identity, and successive replacement implementor identities
remain role-separated; this acceptance identity did not repair or rerun the
candidate.

## Acceptance audit

The candidate and complete accumulated record otherwise provide the required
R6-R12/R22 private-host scope: closed immutable request/result/value models;
host-owned `uart`/`spi`/`i2c` selection and exact file-set verification; fixed
isolated worker launch; mapping, option, sample, samplerate, and request
preflight; frozen API-v3 lifecycle; versioned framed IPC; request/result
projection and declaration/record-graph validation; typed failure conversion;
and no public library or CLI surface. The approved literal set of 18 hard
limits and the separate 11 unchanged macOS regression ceilings matches the
round-4 decision. Verification covers exact-limit and first-overrun behavior,
malformed types/fields/frames/graphs, worker metrics, cancellation and timeout
cleanup, forced kill/reap, descriptor equality, atomic failure, and subsequent
fresh success. Regression observations remain evidence-only and are not
product failures.

The accumulated pass records CPython 3.12.13/macOS 15.7.9 x86_64 with matching
lock/project identities; `pip check`; whole-project Ruff; production and
characterization mypy; deterministic fixture and characterization binding
checks; installed CLI help; six Cycle-2 and the corrected Cycle-3 B1 manifest
validations; 929 passed nonhardware tests with four classified inherited
optional physical-artifact skips and one governed historical deselection;
locked frontend lint/type/unit/build/asset checks; isolated browser checks; and
the unchanged Cycle-2 frontend performance threshold pass. It also records the
active dependency/import/process scan, clean residue handling, no prohibited
runtime or dependency, and no external/reference decoder, C#/.NET, hardware,
USB/serial, live capture, dependency/lock/workflow change, publication, public
decoder API/CLI, browser product work, B3+, or Cycle 4 action.

These passing areas cannot waive the containment finding below.

## Finding C3B2-A001 — request-pipe write is outside deadline and cancellation

Severity: blocking acceptance finding. Disposition: open; earliest owner B2
R8/R10/R11/R12/R22 containment and cleanup.

At exact candidate `host.py` lines 120-121, `_decode_with_factory` calls
`_spawn_fixed_worker(...)` before entering the `try` that translates timeout,
cancellation, worker, IPC, and host failures and before `_collect_response`
begins its selector deadline/cancellation loop at lines 144-146. Inside
`_spawn_fixed_worker`, lines 620-626 synchronously call `_write_all` on the
request pipe; lines 630-634 perform blocking `os.write` calls until the entire
payload is written. There is no nonblocking selector, deadline check, or
cancellation check on this path.

A request may validly approach the approved 4,194,304-byte request ceiling,
well above ordinary pipe capacity. If the fresh worker hangs, stalls, or exits
before draining the request pipe, the parent can block indefinitely in
`os.write`. The approved five-second parent deadline and cancellation cannot
run, `_terminate_reap` is reached only if the write itself raises, and the
parent cannot deterministically close/reap or return the stable `timeout` or
`cancelled` failure. Existing hang/timeout tests begin after request delivery
and therefore do not cover this request-streaming failure mode.

This contradicts the governing requirement that the parent stream and account
for request bytes under a parent-enforced deadline/cancellation boundary, and
that hangs and every failure deterministically terminate/kill, close, reap,
discard partial state, and permit recovery. It also means the accumulated claim
of full request/cancellation/hang containment is incomplete. The candidate is
not ready for atomic manifest assembly.

Required disposition: create a new immutable B2 candidate whose request write,
response/stdout/stderr drain, cancellation, deadline, and cleanup share one
parent-owned nonblocking lifecycle; independently test a worker that never
reads a request larger than pipe capacity, cancellation during partial request
delivery, early worker exit during delivery, deterministic close/reap, stable
failure, no partial success, and subsequent valid recovery. Then repeat fresh
verification, the complete accumulated gate, and fresh acceptance. No prior
pass transfers.

## Commands and limitations

Read-only commands used: `git status --short --branch`; `git rev-parse`; `git
show -s --format=...`; `git merge-base --is-ancestor`; candidate/descendant
`git diff --name-status`; `git log --ancestry-path`; `git show` of immutable
contracts, proposal/approval, implementation/verifier/accumulated records and
candidate source; `rg`; `sed`; `nl`; and `shasum -a 256` of the accumulated
record. The accumulated gate was audited as the authoritative complete run; no
focused rerun was substituted for it. Static inspection was sufficient to
prove the blocking control-flow defect, so no potentially hanging child was
launched and no approval was needed.

No manifest or checkpoint may be assembled from this candidate. After the
required new-candidate sequence passes, the only permitted next authority is
root B2 manifest assembly, followed by distinct manifest verification, joint
manifest/verification-record commit, and only then the B2 checkpoint. B3
remains unauthorized.

`changes_required`
