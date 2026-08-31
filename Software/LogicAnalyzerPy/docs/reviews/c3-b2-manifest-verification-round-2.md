# C3-B2 corrected proposed-manifest verification — round 2

Identity: `c3-b2-manifest-verifier-replacement-2`.

Verdict: `changes_required`.

## Immutable subject and authority

This is a fresh independent verification with no result transferred from
round 1. It is governed by contract commit/tree
`ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
`d9fb09345ab85580cd8c877745262d1b481e366f`, corrected B1 checkpoint
`d4f984d26ca45dcd0f70da51ad739da427e23be4`, corrected B1 manifest commit
`885be61a2bbea8bf5261b3983cbc79fedde0f315`, and exact B2 product
candidate/tree `959edf77945176b26c7cec86bcdd806d7e5769ea` /
`bca2c9d482e690d5bd5fa23822f96336bf6aa0b8`.

The sole subject is
`Software/LogicAnalyzerPy/testdata/evidence/c3-b2.json` at exact SHA-256
`0aadc0d57f2309fcffbc40091b975a1b49a4683b278af83ccf0aa21fc99df8d8`.
That digest was recomputed before any other verification and matched the
assignment exactly. The subject remained unchanged throughout this audit.

The immutable evidence sequence is fresh verifier pass
`ed39a653612b5e879aa08391fcb264f43f09a956`, complete accumulated pass
`a4f01afe3aaa10692a7aa79f742e46cdb24cfac3`, fresh acceptance pass
`536eac331904cd0149104ee4409f5b940344ff09`, failed manifest-verification
record `f5069db5af6f99c8e990e517c13c6bc709707823`, and narrow validator
correction `91b7a7c07f5202f5d7dc9af539f1810860725a4c`.

## Commands and results

Every shell command was invoked through `rtk`. The audit was read-only except
for temporary adversarial manifest copies under `/private/tmp` and this owned
record.

- `rtk shasum -a 256 Software/LogicAnalyzerPy/testdata/evidence/c3-b2.json`:
  reproduced the exact assigned subject digest above.
- `rtk .venv/bin/python scripts/validate_cycle3_evidence.py
  docs/evidence-manifest/cycle3-schema.json testdata/evidence/c3-b1.json` and
  the same command for `c3-b2.json`: both exited 0 under the current strict
  validator.
- `rtk git show 91b7a7c... -- scripts/validate_cycle3_evidence.py`: the
  correction adds only a namespaced role validator, applies it to top-level
  and B1-internal identities, and excludes only the structured `roles` object
  from the generic free-text scan. The `SECRET` expression and all other
  non-role scanning remain unchanged.
- The canonical exact 43-character identity
  `c3-b2-private-host-acceptance-replacement-3` passed in the subject. A
  temporary 43-character arbitrary safe-token string and a temporary
  non-`c3-`/non-`cycle3-` role identity each exited 1 with
  `invalid roles.acceptance`. A temporary non-role bearer credential exited 1
  with `invalid or sensitive limitations[0]`. Thus the correction accepts the
  exact role identity without reopening arbitrary token-like text or disabling
  non-role secret rejection.
- `rtk git rev-parse` reproduced governing tree
  `d9fb09345ab85580cd8c877745262d1b481e366f` and candidate tree
  `bca2c9d482e690d5bd5fa23822f96336bf6aa0b8`.
- Ordered `rtk git merge-base --is-ancestor` checks passed from corrected B1
  manifest through the candidate and from candidate through fresh verification,
  complete accumulation, fresh acceptance, failed manifest verification, and
  validator correction.
- An independent recursive audit found 110 references comprising 62 unique
  `(revision, path, SHA-256)` tuples. Every live path existed and hashed to its
  claim. Every revision-bearing path existed at its stated revision, its Git
  byte stream hashed to the claim, and its live bytes were identical.
- `rtk git diff` from the candidate through current `HEAD`, and from the
  candidate to the live worktree, found no change under
  `Software/LogicAnalyzerPy/src` or
  `Software/LogicAnalyzerPy/tests/implementation`. Product and accepted
  implementation-test bytes remain exactly the candidate bytes.
- Structural and literal searches found no future verifier verdict,
  verification-record path/digest, manifest digest, checkpoint, predictive
  pass, owned round-2 record reference, or self-dependent reference. The
  manifest names only already committed evidence.
- `rtk git diff --check` exited 0. Before this record, status contained only
  the assigned untracked proposed manifest.

## Independent claim audit

The manifest accurately binds candidate `959edf779...`, fresh verification
`ed39a653...`, complete replacement accumulation `a4f01afe...`, and fresh
acceptance `536eac331...`. Its command/result claims agree with the immutable
records: 313 focused B2 tests; the complete 938-pass, four-skip,
one-deselection Python gate; dependency, Ruff, both mypy scopes,
fixture/binding, inherited evidence, frontend static/unit/build, browser,
prohibited-runtime/import/process, repository, and cleanup gates; and the
predeclared no-retry five-of-five performance proof.

The complete correction history is retained. `C3B2-II001`, `C3B2-V001`,
`C3B2-V002`, `C3B2-A001`, and `C3B2-A002` preserve their failed evidence and
closing evidence. `C3B2-MV001` and `C3B2-MV002` preserve the failed round-1
record and accurately describe the new digest and exact acceptance-identity
correction. The original benchmark failure and inadmissible ad hoc pass remain
historical evidence; neither is silently replaced by the separately
precommitted five-run proof.

Mappings cover B2-owned R6-R12 and continuous R9/R21/R23-R25, including R22's
enforcement of the unchanged 18 hard product limits separately from 11
evidence-only regression gates. Stopping conditions 4-8 are present. Corrected
B1 fixture, runner, raw observation, threshold proposal, operator decision,
project/license, B1 manifest, locks, and production-asset bindings all match
their claimed immutable bytes. Limit ownership remains in B1; B2 claims only
enforcement. Scope and limitations remain macOS/Python 3.12, private-host only,
non-conveyance conditional, with B3+, public API/CLI, publication, browser
decoder behavior, hardware/live capture, unsupported platforms, and final
Cycle 3 closure deferred or excluded.

## Finding

### C3B2-MV003 — proposed manifest names the failed verifier identity

Status: open.

The corrected manifest's `roles.manifest_verifier` is
`c3-b2-manifest-verifier-replacement-1`. That identity already issued the
failed round-1 `changes_required` verdict committed at `f5069db5...` and cannot
own this no-transfer fresh verification. The assigned verifier of this exact
corrected subject is `c3-b2-manifest-verifier-replacement-2`.

The governing directed-manifest protocol permits a proposed manifest to name
the already assigned manifest-verifier identity and requires role and
correction ordering to be immutable and auditable. Retaining the failed
identity makes the proposed manifest's role map inaccurate and obscures the
required fresh role separation, even though the current validator correctly
accepts the string's syntax. This is a semantic authority defect, not a schema
defect.

No manifest, validator, product, test, prior evidence, progress, contract, or
checkpoint was repaired. A newly assembled proposed manifest must record the
fresh assigned verifier identity and receive a new exact digest and fresh
independent verification. This verdict authorizes no manifest commit,
checkpoint, B3 work, predictive pass, or result transfer.

`changes_required`
