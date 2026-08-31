# C3-B2 proposed-manifest verification — round 1

Identity: `c3-b2-manifest-verifier-replacement-1`.

Verdict: `changes_required`.

## Immutable subject and authority

This independent audit is governed by contract commit/tree
`ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
`d9fb09345ab85580cd8c877745262d1b481e366f`, corrected B1 checkpoint
`d4f984d26ca45dcd0f70da51ad739da427e23be4`, corrected B1 manifest commit
`885be61a2bbea8bf5261b3983cbc79fedde0f315`, and exact B2 product
candidate/tree `959edf77945176b26c7cec86bcdd806d7e5769ea` /
`bca2c9d482e690d5bd5fa23822f96336bf6aa0b8`.

The assigned proposed-manifest subject was
`Software/LogicAnalyzerPy/testdata/evidence/c3-b2.json` at SHA-256
`8cf427f00d5d9b21241fcbf60859759e30c65a774098c662ba9de612b23c7d21`.
At verification time, the live untracked path instead had SHA-256
`84e251ba2c5561e417f6efe39b8a7aa160b4aa91eb12de0fd186800e6e8da6e8`.
The live bytes are therefore a different proposed manifest and cannot receive
a pass for the assigned immutable subject. This record nevertheless completed
the required checks against those live bytes to preserve all findings.

## Commands and results

All shell commands were invoked through `rtk`. Read-only inspection covered
the governing discovery/batch contract, corrected B1 manifest/checkpoint,
progress identity assignments, every referenced immutable review and artifact,
candidate ancestry, and the exact finding/correction sequence.

- `.venv/bin/python scripts/validate_cycle3_evidence.py docs/evidence-manifest/cycle3-schema.json testdata/evidence/c3-b2.json`: exit 0; the live file satisfies the frozen strict schema.
- `shasum -a 256 testdata/evidence/c3-b2.json`: live digest
  `84e251ba2c5561e417f6efe39b8a7aa160b4aa91eb12de0fd186800e6e8da6e8`,
  not the assigned digest.
- `git rev-parse ea83a403...^{tree}` and
  `git rev-parse 959edf7...^{tree}`: reproduced the governing tree
  `d9fb09345ab85580cd8c877745262d1b481e366f` and candidate tree
  `bca2c9d482e690d5bd5fa23822f96336bf6aa0b8`.
- An independent recursive digest/revision audit found 60 unique referenced
  `(revision, path, SHA-256)` identities. Every live digest matched, every path
  existed at its stated revision, every revision byte stream hashed to the
  claimed value, and every live byte stream equaled its stated revision.
- Ancestry checks passed in required order: candidate `959edf7` precedes fresh
  verification `ed39a65`, which precedes complete accumulated pass `a4f01af`,
  which precedes fresh acceptance `536eac3`.
- Candidate-to-acceptance comparison over product source, the accepted B2
  implementation test, B1 decoder fixtures/method, locks, and governed web
  assets returned no changed path. A live diff against the candidate also
  found no product or implementation-test change. Candidate product bytes are
  unchanged.
- Recursive structure/text inspection found no manifest SHA field, future
  manifest-verification verdict, verification-record identity/path/digest,
  checkpoint commit, owned record path, predictive pass, or self-dependent
  digest in the live manifest.
- `git diff --check`: exit 0. Before this record, repository status contained
  only the untracked proposed manifest.

## Coverage and supported claims

Subject to the findings below, the live manifest accurately binds fresh
verification commit `ed39a653612b5e879aa08391fcb264f43f09a956`, complete
replacement accumulated pass `a4f01afe3aaa10692a7aa79f742e46cdb24cfac3`,
and fresh acceptance pass `536eac331904cd0149104ee4409f5b940344ff09` to
the unchanged candidate. Its command results agree with the immutable records:
313 focused B2 tests; the from-scratch 938-pass, four-skip, one-deselection
Python gate; dependency, Ruff, mypy, fixture/binding, inherited evidence,
frontend, browser, prohibited-runtime/process, and repository gates; and the
precommitted no-retry five-of-five performance proof.

The complete ordered history is preserved: `C3B2-II001`, `C3B2-V001`,
`C3B2-V002`, `C3B2-A001`, and `C3B2-A002` are named with their original failed
records and later closing evidence. The original benchmark failure and
inadmissible ad hoc pass remain historical evidence; the accepted disposition
is the separately precommitted five-run proof followed by complete fresh
accumulation and acceptance.

The evidence mappings cover exactly B2-owned requirements R6-R12 and inherited
R21-R25, including R22's enforcement of the unchanged 18 hard product limits
separately from 11 evidence-only regression gates. Stopping conditions 4-8 are
mapped. Corrected B1 fixture, runner, raw-result, threshold, operator-decision,
and project/license digests all match their approved revisions. The manifest
does not claim a public decode API/CLI, B3 work, checkpoint, publication,
unsupported platform, or later-batch completion.

## Findings

### C3B2-MV001 — assigned manifest bytes changed before verification

Status: open. The authorized subject digest is
`8cf427f00d5d9b21241fcbf60859759e30c65a774098c662ba9de612b23c7d21`,
but the only live proposed manifest hashes to
`84e251ba2c5561e417f6efe39b8a7aa160b4aa91eb12de0fd186800e6e8da6e8`.
The governing mechanics require the manifest verifier to name and hash one
unchanged manifest. A changed subject cannot be accepted under the prior
authorization, regardless of the live file's schema and digest consistency.

### C3B2-MV002 — acceptance role identity is inaccurate

Status: open. The live manifest records role
`c3-b2-private-host-acceptance-replacement-3-role`. The immutable acceptance
record and orchestration assignment both name
`c3-b2-private-host-acceptance-replacement-3`; no immutable record supports
the added `-role` suffix. Role separation itself is otherwise present, but the
manifest's claimed identity is false and must not be silently normalized by a
verifier.

No manifest, product, test, prior evidence, progress, contract, or checkpoint
was repaired. These findings require a newly assembled proposed manifest and a
fresh, independently authorized verification of its exact digest. No manifest
commit, checkpoint, predictive pass, or B3 authority follows from this record.

`changes_required`
