# C3-B4 hosted artifact and descendant proof implementation, round 15

- Identity and role: `c3-b4-public-implementor-1`; bounded evidence-test
  correction implementor
- Immutable failed verifier commit/tree:
  `082f27ead5972f7b021728164d51e8e9d9c6ba44` /
  `559240116a95e75cb3ed69d0af0969edddb34d0d`
- Governing B1 contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`
- Timestamp: `2026-09-02T08:51:00Z`

## Failed hosted evidence disposition

The preserved exact GitHub Actions run `33608601566`, job `100178223085`,
passed bootstrap and static gates. Its Python gate ended after 756.66 seconds
with `2 failed, 1472 passed, 4 skipped, 38 deselected`.

1. Round 12's hosted artifact-present proof overwrote the real workflow
   environment with verifier-private `.tmp/c3-b4-ci/round11` paths, which do
   not exist in a clean hosted checkout.
2. Round 14's descendant-interference proof required ignored local
   `.tmp/c3-b4-ci/r13-verifier-draft` state rather than using tracked
   descendant evidence.

## Implementation and validation

Round 12's artifact-present proof now reads the existing
`PICO_LA_PYTHON_ARCHIVE` and `PICO_LA_PYTHON` pair. If both are present, their
actual paths are passed unchanged to the nested round-11 artifact validator.
If both are absent, it uses the existing ignored local verifier archive and
interpreter as a fallback. If exactly one is present, the outer proof fails
closed before launching the nested test. The separate absent-environment and
partial-environment nested branch proofs remain selected and unchanged in
purpose.

Round 14's descendant-interference proof now uses tracked
`tests/verification/test_c3_b4_public_round14.py` as its descendant. It proves
that file exists in the current source tree and does not exist in immutable
candidate `c7650876544e477c277200c4f2fcbd23c67fe245`, then runs the immutable
archive collection and verifies no scratch leak. It has no ignored-draft or
other machine-local prerequisite.

An implementation regression requires hosted environment preference, paired
environment fail-closed logic, and forwarding of the selected paths. It also
requires the tracked round-14 descendant proof and rejects any
`r13-verifier-draft` or `.tmp` dependency in that proof.

Targeted hosted-style validation used the exact existing archive and
interpreter through the two workflow environment variables. Hosted preference,
the absent and partial nested branches, the tracked descendant proof, and the
new regression passed `5 passed in 4.38s`. The both-absent local fallback
separately passed `1 passed in 0.52s`.

Ruff on all changed Python tests, `git diff --check`, and the explicit
unchanged-workflow check passed. The full unchanged partition collected 1,517
items, deselected 38, and selected 1,479; result was `1472 passed, 7 skipped,
38 deselected, 106 warnings in 243.82s`. The skips remain classified loopback,
optional physical artifacts, and local absence of workflow-provisioned
artifact paths.

Changed paths and pre-commit hashes:

- `Software/LogicAnalyzerPy/tests/implementation/test_cycle2_workflow.py` —
  `1a2be50ebffa5b4fa1068773500690ad99d3436df804d88baf574e55b3a79262`;
- `Software/LogicAnalyzerPy/tests/verification/test_c3_b4_public_round12.py` —
  `303b8b7d61536bf976ca8e7c2f23500b3cb611370324124eb87d8cfd82323070`;
- `Software/LogicAnalyzerPy/tests/verification/test_c3_b4_public_round14.py` —
  `408c93f2ac448025977477cae1774dcd7cf983745afe6e516afc93c8e70025a7`;
- `Software/LogicAnalyzerPy/docs/reviews/c3-b4-implementation-round-15.md` —
  this implementation record.

The workflow remains unchanged at SHA-256
`12ff6bb2cd7e437b733f3aaeb9488c6926604572419468c60604f0dea1c6a990`
with exactly 15 ignores / 37 selector strings / 38 cases. No product, decoder,
B1/B2/B3 fixture, threshold, limit, lock, manifest, contract, or prior evidence
byte changed. No network, hosted retry/dispatch, or external mutation was
performed.

## Verdict and boundary

Hosted artifact validation now consumes the actual provisioned files, and the
descendant proof is self-contained in tracked repository state. The unchanged
full partition is green. Fresh independent verification and root-owned hosted
dispatch remain required, so the verdict is `candidate-not-accepted`.

The B1 rights-holder/counsel limitation remains controlling. Shim ownership,
historical MIT labeling, and combined-work treatment require counsel or
rights-holder confirmation before conveyance. No wheel, sdist, upload,
conveyance, or publication was performed or authorized.
