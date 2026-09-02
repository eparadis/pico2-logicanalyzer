# Cycle 3 completion-closure audit — round 1

## Auditor and immutable inputs

- Auditor: `c3-completion-closure-auditor-1`, fresh and distinct from every
  Cycle 3 batch implementation, verification, acceptance, and manifest role.
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- B5 manifest and manifest-verification commit/tree:
  `5d5712477e41ee269f2828787c9fddc840c414b6` /
  `cfc45a42c0d6a45ce0fbbd34ca6e877421a10ff3`.
- B5 manifest SHA-256:
  `c67031fa0f9590e9cc44134e382f2c3bec70e0744c91a4f26be6a559699e1532`.
- B5 manifest-verification record SHA-256:
  `a866d5057c35b96a3e5f81bb1d8ac0e2a6329fe839eb90f73be353cb1320937a`.
- Closure-pending B5 checkpoint commit/tree:
  `d7e79e03cf9d1f461cc30f87a84fc5d21c2b62aa` /
  `40849b62bb543be07863743c2d6a8d615585abe4`.
- Completion-proof candidate commit/tree:
  `728d77f549b9686569f1a5cc2343935e7c747982` /
  `688d9c77adc2d887284b92c83ce093c54a1e8346`.
- Completion-proof SHA-256:
  `4c0902731615d2f417cc3b5141a1510c0518e1861d0ba80d60b9d318e783f69f`.

The repository was clean before this record was created. I did not edit any
input, product, test, fixture, expected value, method, threshold, manifest,
checkpoint, proof, progress, workflow, package, or previous evidence file.

## Independent structural and digest audit

Git object inspection reproduced every stated commit and tree. Ancestry checks
proved the accepted B1-through-B5 manifest/checkpoint chain, B5 verification,
accumulated validation, acceptance, manifest pair, separate checkpoint, and
completion proof are ordered. The B5 manifest commit precedes the separate B5
checkpoint, which precedes the proof. The checkpoint contains the literal
`Complete; Cycle 3 closure pending`.

The strict Cycle 3 validator accepted all five manifests. Independent recursive
inspection of B5 checked 95 path/digest references (26 unique pairs) against
repository bytes, all successfully. R1-R26 occur exactly once in order with
`pass`; stopping conditions 1-17 occur exactly once in order with `pass`.
All declared revisions exist, every accepted role is distinct as required,
superseded/correction histories transfer no pass, and all five checkpoint and
manifest identities and SHA-256 values agree with repository bytes.

The completion proof accurately describes the exact decoder inventory, private
host, public API/CLI, typed marker, fixtures, method/runner, threshold decision,
locks/assets, license/notices/attribution, commands and outcomes, batch role
histories and corrections, support boundary, process and cleanup behavior,
rollback, exclusions, and legal boundary. There is no missing or deferred
Cycle 3 finding. GPL-3.0-only remains an engineering disposition, not a legal
conclusion; rights-holder or qualified-counsel confirmation remains required
before conveyance.

The proof candidate predicts no future closure commit, tree, digest, role
verdict, audit artifact, or seal identity. No terminal completion seal existed
or was treated as an audit input.

## Limits, measurements, and hosted evidence

The product mappings equal all 18 approved hard limits and all 11 unchanged
round-4 regression ceilings exactly, including SPI maximum word size eight and
rejection of nine. The final packet SHA-256 is
`980308fc3a144d1af70959793fb9e0b4476658b9856d56eb101876fc9fedb54e`.
It contains exactly three warm-ups and 15 retained rows (five each for UART,
SPI, and I2C), hence 18 launches. Independently recomputed maxima equal all 11
manifest observations and remain within their ceilings:

- worker RSS `28,897,280 <= 134,217,728` bytes;
- parent retained growth `57,344 <= 33,554,432` bytes;
- successful parent total `153,574,907 <= 1,300,000,000` ns;
- launch `2,689,733 <= 50,000,000` ns;
- reap `22,638 <= 50,000,000` ns;
- child load `9,062,265 <= 100,000,000` ns;
- child import `91,613,460 <= 100,000,000` ns;
- child decode `2,347,729 <= 100,000,000` ns;
- timeout cleanup `0 <= 5,500,000,000` ns;
- terminate-to-reap `0 <= 300,000,000` ns;
- kill-to-reap `0 <= 50,000,000` ns.

Fresh GitHub API evidence confirmed run `33655002746`, job `100331249147`,
attempt one, exact head `2fb89fc8c36d93b4435032c07783532d6a8aa933`,
push event, label `macos-15-intel`, and `completed` / `success`. The job ran
from `2026-09-02T16:27:29Z` through `2026-09-02T16:44:30Z`; every non-skipped
step passed and there were no failed steps.

## Commands and results

- `git status --short`, `git show`, and `git merge-base --is-ancestor`:
  clean input state; exact objects, trees, parents, and complete order passed.
- `validate_cycle3_evidence.py` against `c3-b1.json` through `c3-b5.json`:
  five passes.
- SHA-256 verification plus an independent recursive manifest/path/revision/
  measurement audit: 95 references, 15 retained rows, 18 launches, and 14
  ordered commits passed.
- Corrected B5 final-packet selection: `3 passed`.
- Round-2/3/4 containment, IPC, cleanup, timing and hard-limit checks plus the
  public boundary selection: `86 passed`.
- UART/SPI/I2C conformance, cross-source equivalence, implementation public
  surface and final public verification selection: `454 passed`.
- Fresh GitHub run/job API inspection: exact SHA, runner, attempt, result, and
  step outcomes passed.
- Final `git diff --check`, index/path containment, digest recheck, and clean
  post-commit state are required immediately around this record's commit.

## Condition 18 and verdict

Condition 18 is correctly ordered through the immutable proof: verified B5
manifest pair, separate checkpoint with literal pending remainder, then proof.
This distinct closure audit uses only those committed inputs. The terminal seal
is not an input and must be created by the root orchestrator only after this
verdict commit.

Findings: none. Deferred findings: none. Input edits: none.

Verdict: `pass`.

`APPROVAL_NEEDED`: none.
