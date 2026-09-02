# C3-B4 hosted focused-launch implementation, round 13

- Identity and role: `c3-b4-public-implementor-1`; bounded hosted-verifier
  correction implementor
- Immutable failed verifier commit/tree:
  `b716ae23f36a213067372cda618884365787c1e1` /
  `f6ed57c286ae5df4491ba78c265ee0aaf739d638`
- Governing B1 contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`
- Timestamp: `2026-09-02T07:49:18Z`

## Failed hosted evidence disposition

The preserved exact GitHub Actions run `33603126412`, job `100161055220`,
passed artifact/bootstrap and static gates. Its Python gate ended after 521.84
seconds with `2 failed, 1463 passed, 4 skipped, 38 deselected`.

Both failures were nested focused-gate verifier launches: round 11's
`test_raw_b1_focused_and_prior_hosted_guards_remain_green` and round 12's
`test_raw_b1_focused_and_hosted_guards_remain_green`. Their inner pytest output
showed `kill_to_reap_ns == 0`, while the actual workflow focused gate had
already passed under its `trap '' TERM` subshell. The verifier launches must
reproduce that inherited SIGTERM-ignore context.

## Implementation and validation

Both retained verifier functions now use the same explicit POSIX launch
contract:

```text
/bin/sh -c "trap '' TERM; exec \"$1\" -m pytest ..."
```

The shell installs `SIG_IGN` for SIGTERM before replacing itself with the
nested Python/pytest process. POSIX preserves an ignored disposition across
`exec`, matching the workflow's already-passing focused subshell. Round 12's
prior direct pytest subprocess is removed; round 11's launch is normalized to
the same absolute POSIX shell and shared command constant.

An implementation-owned regression checks the exact launch block in both
retained verifier sources, rejects the old direct launch, and executes a real
shell-to-Python `exec` whose Python child asserts
`signal.getsignal(SIGTERM) == SIG_IGN`.

Adding that one regression changed round 12's self-excluding collection by one
test. The collection assertion was updated from `1459/1497` to the observed
`1460/1498`, still with exactly 38 deselections. This is not a selector or
workflow change.

Focused validation from a normal parent ran the new signal-context regression
and both retained verifier functions: `3 passed in 1.67s`. After updating the
collection identity, the collection proof plus the same three focused checks
reported `4 passed in 2.46s`.

The first full broad run exposed only the expected one-test collection-literal
change: `1462 passed, 7 skipped, 38 deselected, 1 failed in 234.61s`. After the
literal correction, the final unchanged partition collected 1,508 items,
deselected 38, and selected 1,470; final result was `1463 passed, 7 skipped, 38
deselected, 106 warnings in 234.66s`. Both corrected retained functions passed.
The skips remain classified loopback, optional physical-artifact, and local
absence of workflow-provisioned artifact paths.

Ruff on all changed Python files and `git diff --check` passed. The workflow
has no diff, retains exactly 15 ignores / 37 selector strings / 38 cases, and
its SHA-256 remains
`12ff6bb2cd7e437b733f3aaeb9488c6926604572419468c60604f0dea1c6a990`.

Changed paths and pre-commit hashes:

- `Software/LogicAnalyzerPy/tests/implementation/test_cycle2_workflow.py` —
  `11fe16205bbc0edb24e4fb042a51315cb47c7e6969b411f9866f65073ad53198`;
- `Software/LogicAnalyzerPy/tests/verification/test_c3_b4_public_round11.py` —
  `857f2faac7ce67dba1eebc07687f9e69468bee2e081276cf703e9e5ea8cb692c`;
- `Software/LogicAnalyzerPy/tests/verification/test_c3_b4_public_round12.py` —
  `5135b12db0e77177f64280c75c089915c526eabb620f09c780b9b0f447f87b24`;
- `Software/LogicAnalyzerPy/docs/reviews/c3-b4-implementation-round-13.md` —
  this implementation record.

No workflow, product, decoder, B1/B2/B3 fixture, threshold, limit, selector,
dependency lock, manifest, contract, or prior evidence byte changed. No hosted
retry/dispatch or external mutation was performed by this identity. Scratch,
where needed, remained under ignored repository `.tmp/`.

## Verdict and boundary

The two hosted verifier launch defects now reproduce the governed focused-gate
signal context and the unchanged full partition is green. Fresh independent
verification and root-owned hosted dispatch remain required, so the verdict is
`candidate-not-accepted`.

The B1 rights-holder/counsel limitation remains controlling. Shim ownership,
historical MIT labeling, and combined-work treatment require counsel or
rights-holder confirmation before conveyance. No wheel, sdist, upload,
conveyance, or publication was performed or authorized.
