# C3-B2 corrected proposed-manifest verification — round 3

Identity: `c3-b2-manifest-verifier-replacement-3`.

Verdict: `pass`.

## Immutable subject and authority

This is a fresh independent verification of only the corrected proposed
manifest `Software/LogicAnalyzerPy/testdata/evidence/c3-b2.json`. No result or
verdict transfers from failed manifest-verification rounds 1 or 2.

- Subject SHA-256, recomputed before reading the manifest:
  `2af5bfc21a5d888132fb4e468f543403e8948632ad9ab2dd11b8da854dd4a602`.
- The same SHA-256 was recomputed after all inspection and remained exact.
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Corrected B1 checkpoint and manifest commits:
  `d4f984d26ca45dcd0f70da51ad739da427e23be4` and
  `885be61a2bbea8bf5261b3983cbc79fedde0f315`.
- Exact B2 candidate/tree:
  `959edf77945176b26c7cec86bcdd806d7e5769ea` /
  `bca2c9d482e690d5bd5fa23822f96336bf6aa0b8`.
- Fresh product verifier, complete accumulation, and acceptance commits:
  `ed39a653612b5e879aa08391fcb264f43f09a956`,
  `a4f01afe3aaa10692a7aa79f742e46cdb24cfac3`, and
  `536eac331904cd0149104ee4409f5b940344ff09`.
- Failed manifest findings are preserved at
  `f5069db5af6f99c8e990e517c13c6bc709707823` and
  `127398d3e3840bb841af9b080770d382209067ec`; the validator correction is
  `91b7a7c07f5202f5d7dc9af539f1810860725a4c`.

The pre-inspection status contained exactly the assigned untracked manifest.
The manifest role map is exact and pairwise distinct:
`c3-b2-private-host-implementor-replacement-6`,
`c3-b2-private-host-verifier-replacement-4`,
`c3-b2-private-host-acceptance-replacement-3`, and this verifier identity,
`c3-b2-manifest-verifier-replacement-3`.

## Commands and results

All shell invocations were made through `rtk`.

- `sha256sum Software/LogicAnalyzerPy/testdata/evidence/c3-b2.json`: exact
  assigned digest before inspection and unchanged after inspection.
- `git status --short`: before this record, only
  `?? Software/LogicAnalyzerPy/testdata/evidence/c3-b2.json`.
- `git rev-parse <commit>^{tree}`: contract and B2 trees matched exactly; the
  B1 checkpoint tree was independently resolved as
  `7ea1fc48a28413011dca4dc6f07c5f0312b9f584`.
- `.venv/bin/python scripts/validate_cycle3_evidence.py
  docs/evidence-manifest/cycle3-schema.json testdata/evidence/c3-b1.json`:
  exit 0.
- The same validator command for `testdata/evidence/c3-b2.json`: exit 0.
- An in-memory adversarial validation replacing non-role `worktree_state`
  with `token: definitely-sensitive`: rejected with `invalid or sensitive
  worktree_state`.
- `git merge-base --is-ancestor` over contract -> corrected B1 checkpoint ->
  B2 candidate -> fresh verifier -> complete accumulation -> acceptance ->
  failed manifest round 1 -> validator correction -> failed manifest round 2:
  every edge exited 0.
- Independent JSON/reference audit: 108 reference occurrences, 43 unique
  path/digest pairs, zero errors. Every referenced working-tree path exists and
  hashes exactly; every artifact also exists at its declared revision and its
  revision bytes hash exactly.
- `git show 885be61...:Software/LogicAnalyzerPy/testdata/evidence/c3-b1.json |
  sha256sum` and the same path at checkpoint `d4f984d...`: both produced
  `3710e7fde7523096b70607b3a7da217b1e71fdb46492b83b72861e3eaa48cfae`.
- `git diff --exit-code 959edf7... 536eac3... --
  Software/LogicAnalyzerPy/src Software/LogicAnalyzerPy/tests/implementation`:
  exit 0. Candidate product and implementation-test bytes are unchanged.
  The broader source/test comparison showed only the expected added fresh
  verifier file `tests/verification/test_c3_b2_private_host_round4.py`.
- Targeted `jq`, `rg`, contract, evidence, and review inspection confirmed the
  exact mappings, identities, commands/results, findings, limitations,
  deferrals, and audit claims described below.

## Validator correction audit

Commit `91b7a7c...` changes only
`scripts/validate_cycle3_evidence.py`. It adds a namespaced role-identity regex
and applies it to primary and B1-internal role fields, then omits only `roles`
from the generic free-text secret walk. Role identities must begin `c3-` or
`cycle3-`, contain only the bounded identity character set, and remain subject
to exact key and separation checks. The general `string()` secret rejection is
unchanged for all non-role fields, as the adversarial test above demonstrates.
This is a narrow correction for established role names, not a general secret
scan waiver.

## Evidence and contract audit

The corrected B1 manifest validates independently and retains exact bindings
for the fixture, runner, raw characterization, threshold proposal,
project/license disposition, and operator decision. Its six binding digests
match the B2 `b1_evidence` object. The approved threshold proposal has exactly
29 unchanged entries: 18 `hard-enforcement` product limits and 11
`regression-ceiling` evidence gates. R22 correctly proves enforcement of the
18 hard limits without rebasing values owned and approved in B1; the 11
regression gates remain distinct evidence controls.

The B2 mapping is exact for R6-R12, continuing R9 and R21/R23-R25, including
R22. It maps exactly stopping conditions 4-8. Evidence covers host-owned
decoder identity/digest/import closure and inert request data; validation
before launch; frozen lifecycle and deterministic typed results; hostile
framing; deadlines, cancellation and every approved product limit; exact
cleanup/reap/recovery; prohibited-runtime/dependency/import/process audits;
rollback and inherited regression; role/finding ordering; and excluded scope.

Recorded commands are all bound to tested commit `959edf7...`, have exit status
0, are not skipped, and cite digest-valid evidence. They preserve the focused
313-pass host gate, complete Python/static/nonhardware regression, fixture and
runner binding, inherited manifests, frontend unit/build/browser gates, exact
five-run performance disposition, prohibited-path/process audits, and clean
pre-manifest repository check. The complete accumulation and acceptance records
support those literal results; the manifest does not convert inherited optional
physical-artifact skips into mandatory success claims.

The complete ordered finding history is present with closing evidence and
accurate dispositions:

- `C3B2-II001`: rejected incomplete initial host; later implementation closes
  lifecycle, containment, and proof surfaces.
- `C3B2-V001`: parent-bound identity and request projections.
- `C3B2-V002`: closed-graph validation of declarations and returned records.
- `C3B2-A001`: nonblocking request delivery under the unified deadline,
  cancellation, drain, and cleanup lifecycle.
- `C3B2-A002`: original failure and inadmissible ad hoc pass retained; exactly
  five independently passing unchanged runs under the precommitted no-retry
  rule, followed by complete accumulation.
- `C3B2-MV001`: changed prior subject rejected; no verdict transfer.
- `C3B2-MV002`: exact acceptance identity restored, with narrow validator
  correction and retained non-role secret rejection.
- `C3B2-MV003`: failed round-1 verifier removed from the active role map; the
  corrected bytes name only fresh replacement-3.

The manifest contains the two failed manifest review records as immutable
historical evidence, but no future verifier verdict, future record path,
subject digest, committed B2 checkpoint, predictive pass, or self-dependent
reference. Text that explicitly denies such future evidence is descriptive and
does not claim it. Its limitations and deferred work keep public API/CLI, B3+,
final CI/measurements, physical/live/browser decoder work, publication, and
unsupported platforms outside this checkpoint.

## Conclusion

The fixed subject bytes are internally consistent, revision- and
digest-complete, correctly separated by role, faithful to the governing B1/B2
ownership and stopping conditions, and free of predictive or self-dependent
evidence. No correction is required.

`pass`
