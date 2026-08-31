# C3-B2 independent acceptance — round 3

Identity: `c3-b2-private-host-acceptance-replacement-3`.

Verdict: `pass`.

## Immutable subject and order

This fresh acceptance audit is bound only to governing contract
`ea83a403bb6f644d33069d3bebd41d5f1e0a60c0`, tree
`d9fb09345ab85580cd8c877745262d1b481e366f`; corrected B1 checkpoint
`d4f984d26ca45dcd0f70da51ad739da427e23be4`; corrected B1 manifest commit
`885be61a2bbea8bf5261b3983cbc79fedde0f315`; approved round-4 proposal and
decision `b680aa59fba4a18da2aeaacc8cbd7ad3a68784e0` and
`afd45856ee261158521b902dabdf926e5f1f922a`; exact B2 candidate
`959edf77945176b26c7cec86bcdd806d7e5769ea`, tree
`bca2c9d482e690d5bd5fa23822f96336bf6aa0b8`; fresh verifier pass
`ed39a653612b5e879aa08391fcb264f43f09a956`, tree
`dc94ec3af39363f6b6c9a41ce5f9a11b04bfe65e`; predeclared performance plan
commit `de470abdab63ebdf7014747b4a4e1fc2fb694a75`; performance result commit
`41cccdfce71482418ac01f14d6b7669e073b626b`; and complete replacement
accumulated record commit `a4f01afe3aaa10692a7aa79f742e46cdb24cfac3`.

The accumulated record is
`Software/LogicAnalyzerPy/docs/reviews/c3-b2-accumulated-validation-round-3.md`,
SHA-256 `cdd7e61972fa0eb3176be4b14fa5e8844229849d43362bd5c4ee5753692e43b6`.
The ancestry and all named commit/tree identities were independently
recomputed. Candidate-to-verifier changes are only the progress record and
round-4 verifier test/review; subsequent changes through accumulation are only
progress and immutable B2 acceptance, accumulation, and performance evidence.
Candidate product and implementation-test bytes remain unchanged. Audit
completed `2026-08-31T15:28:26Z` on branch `python-rewrite` at clean starting
HEAD `a4f01afe3aaa10692a7aa79f742e46cdb24cfac3`, before this owned record.

All predecessor candidates, verifier records, accumulated records, acceptance
records, and findings `C3B2-II001`, `C3B2-V001`, `C3B2-V002`, `C3B2-A001`,
and `C3B2-A002` remain immutable history. No result transfers from them. The
replacement implementor, fresh verifier, root accumulated owner, and this
acceptance identity are role-separated; this identity changed no audit input
and reran neither tests nor performance.

## Acceptance audit and finding dispositions

`C3B2-A001` is closed. The exact candidate streams nonblocking request writes
inside the same parent selector lifecycle as response, stdout, and stderr
draining, with inclusive deadline and cancellation checks during partial
delivery. Early request close/exit/signal, output failure, timeout, and
cancellation converge on stable atomic failure, descriptor closure, exact-child
terminate/kill/reap, partial-state discard, and fresh-process recovery. The
fresh independent round-4 verifier exercises slow and never-reading children,
large and partial request delivery, concurrent hostile output, early response,
close/exit/signal, readiness anomalies, cleanup, and real subsequent decode.

`C3B2-A002` is closed without invalidating or waiving the original exact-method
failure. Failed report
`e2602ab8c3dd02e56b1a8492bd85e12f5d6215e8254e2f9462ae5aed32ebd131`
and its representative distinct-strobe p95 of 140.5 ms against the unchanged
116.7250000052154 ms ceiling remain preserved, as does the later ad hoc pass
that failed acceptance could not select. Before new execution, root committed
a bounded objective reproducibility rule whose plan SHA-256 is
`c35079e6b2ba7bcf04c700b18e53d8f948387a56e2a13eff2084d879c331c1f6`:
exactly five unchanged invocations, independent pass required for each, stop on
any failure, and no retry, replacement, sixth run, aggregation, or outlier
selection. Exactly 5/5 passed. Their independently rechecked report SHA-256
values are `a02de4b65aa137840617b4948f7d1280984a666a2a1b88a895cccf55db8ef0c6`,
`508d1ad1f22e129c1c8c60a4868b059607c2efab5c2c80d4c88327a054f70ca5`,
`175008c92ab39f40d913d9bf1b72964588d826a4433f1632e421b2c02deb51c7`,
`a2f85b22f578cec4a5ca9074bcf986ef42f59b57ce8f8521c6e3779e5eaff1e1`,
and `80fb201f846849ab208fed5fc7da2f179bd78f07d42a30b59f4a961a09193f45`;
representative distinct-strobe p95 values were 62.8, 60.7, 66.6, 73.5, and
64.3 ms. Result-record SHA-256 is
`66442c98fff290626242146a315be1b24fc681bcd4ed93928255760383526369`.
This stronger precommitted proof establishes repeatable compliance under an
objective rule rather than choosing a favorable rerun. No product, method,
warm-up, iteration, statistic, checker, environment path, fixture, dependency,
or threshold byte changed. The original failure remains valid historical
evidence, but it no longer leaves the newly defined complete gate unpassed.

The exact candidate and fresh verifier evidence cover complete R6-R12/R22:
closed host-owned decoder identity/digest/import selection with inert request
and capture data; pre-spawn capture, samplerate, mapping, option, and request
validation; frozen API-v3 lifecycle; immutable version-1 request/result/value
models and deterministic serialization/order; single-use fixed subprocess;
versioned streaming length-framed IPC; complete request/result projection and
declaration/record graph validation; hostile malformed, oversized, partial,
extra, and unknown IPC; stable typed failures; parent-owned deadline and
cancellation; memory, recursion, output, diagnostic, retention, process, and
descriptor containment; atomic cleanup and successful recovery. The exact 18
approved hard limits are product-enforced and remain distinct from all 11
evidence-only macOS regression gates. Static inspection confirms no public
decoder API or installed decoder CLI and no B3 or later behavior.

After the five-run proof, root repeated the rest of the complete accumulated
gate from scratch on CPython 3.12.13, macOS 15.7.9 x86_64 with matching lock,
project, fixture, manifest, and limit identities. Results were 938 passed, four
classified inherited optional physical-artifact skips, one governed historical
deselection, and no skipped Cycle 3 mandatory gate. Dependency consistency,
whole-project Ruff, production and characterization mypy, deterministic
fixture/runner binding, installed existing CLI help, Cycle 2 and corrected B1
evidence validation, frontend lint/type/unit/build/assets, unchanged browser
regressions, prohibited-use scans, process cleanup, and `git diff --check` all
passed. The record establishes no external/reference decoder or C#/.NET use;
no prohibited runtime/dependency/process; and no hardware, USB/serial, live
capture, dependency/lock/workflow change, publication, public decoder API/CLI,
browser decoder, unsupported-platform claim, B3+, or Cycle 4 action.

## Commands, limitations, and next authority

Read-only commands used through RTK: instruction/contract/review inspection;
repository status and exact commit/tree/parent inspection; ancestry checks;
candidate-to-descendant name-status comparison; SHA-256 recomputation for the
accumulated, plan, result, candidate, verifier, and all five preserved raw
reports; static source and public-surface searches; and approved-limit review.
No test, benchmark, decoder, browser, C#/.NET, external/reference runtime,
hardware, or live-capture command was executed. No approval was needed. The
only worktree change is this authorized acceptance record; no process was
launched by this audit and there is no owned cleanup residue.

The candidate is ready for B2 manifest assembly. The sole next authority is
root atomic B2 manifest assembly, followed by distinct manifest verification,
joint commit of the unchanged manifest and verification record, and only then
the B2 checkpoint. B3 remains unauthorized until that checkpoint is committed.

`pass`
