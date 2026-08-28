# C3-B1 replacement final verification — round 5

## Verdict and immutable subject

- Verdict: **pass**.
- Independent identity: `c3-b1-final-verifier-replacement-1`.
- Assignment commit: `4299312`.
- Exact candidate commit: `7246dcbe55a60ef7ee9196f4bf265c7c75141d55`.
- Exact candidate tree: `51e895a1e2c95580d04bc8a31ed8d58a85613e1a`.
- Candidate JSON SHA-256:
  `a186af26805c804613271641e5f57b1393ae31d79fa800a29249e37efc0650fd`.
- Candidate review SHA-256:
  `591459742b9453e94047438ec79a6e2bdd54ed3b6d0c71207bbae4c64b563d73`.
- Verifier SHA-256:
  `56a4892a9a25ace4a7cc6ec640ab12e1669ad56f7e345410c5e26eb9e9d8b32b`.
- Candidate state remains exactly `candidate-not-accepted`. This verdict is
  verifier evidence only and supplies no acceptance, manifest, checkpoint, B2,
  or Cycle 4 authority.

## Independent static recomputation

The verifier recomputed the candidate's two-path commit scope, exact committed
bytes, tree, and Git ancestry. It independently resolved and hashed every live
bound artifact: governing contract, project/license record, corrected fixture
generator/data/manifest/caps and verification chain, portable runner binding,
launch/runner/worker/method and verification chain, fresh raw files and
collection/verification chain, and the complete round-4 threshold proposal,
verification, accumulation, acceptance, and operator-approval chain.

The corrected chain is ordered as fixture `3af6b9f`, runner `380d5dd`, raw
`d0d9dbe`, round-4 proposal `b680aa5`, and exact operator approval `afd4585`.
Their committed trees, record digests, and ancestry all match. The full fixture
implementation history through replacement 8 and full runner implementation
history through replacement 4 are present and ordered. The six current
implementation, verification, and acceptance identities are pairwise distinct.

All 29 approved values match the proposal and operator record exactly. Each
proposal boundary accepts the exact value and rejects value + 1. In particular,
the round-4 changes are 33,554,432 parent-retained-growth bytes, 1,300,000,000
successful-parent-total ns, and 50,000,000 launch ns; the remaining 26 values
are unchanged from round 3.

The frozen 21-command inventory, exact applicability inventory (56 modules,
41 included, 15 excluded, 608 collected, 602 passed, six inherited classified
skips), exclusions, macOS-only environment, legal and distribution limits, and
the mandatory downstream gate order are all exact. The preserved B2 work is
excluded from evidence and was not inspected.

## Mutation resistance

The 20-family mutation matrix starts from the valid binder and proves rejection
after each independent mutation: missing top-level member, extra member,
schema, status, authority, governing tree, correction/finding history,
environment, role collapse, incomplete role history, live digest, missing
evidence group, limit, approval authority, closed finding, historical
invalidation, frozen command, applicability, exclusion, and downstream order.
The verifier additionally freezes canonical component digests, so extra or
altered nested fields cannot bypass these direct guards.

## Commands and results

All commands were static and repository-local:

1. `.venv/bin/python -m pytest -q
   tests/verification/test_c3_b1_final_candidate_round4.py` — **22 passed in
   0.64s** after correcting one verifier-only review-wording assertion; the
   immutable candidate was not changed.
2. `.venv/bin/ruff check
   tests/verification/test_c3_b1_final_candidate_round4.py` — **all checks
   passed**.
3. `git diff --check --
   Software/LogicAnalyzerPy/tests/verification/test_c3_b1_final_candidate_round4.py`
   — **pass**, no output.

No decoder, runner, raw reproduction, product/B2/downstream suite, browser,
hardware, network, package, or Cycle 4 command ran. No candidate byte was
repaired. The three preserved untracked B2 paths were neither opened nor used.

## Findings and next gate

Findings: **none**. The candidate correctly preserves `C3B2-IF001`,
`C3B2-IF002`, `C3B1-RA001`, `C3B1-RV002`, `C3B1-RV003`, `C3B1-FV001`, and all
other recorded findings and invalidations without transferring superseded
authority.

The next gate is complete root accumulated validation of this exact candidate
plus this verifier. It must then be followed, in order, by fresh independent
acceptance, atomic replacement-manifest assembly, distinct manifest
verification, the joint manifest/verifier commit, and the replacement B1
checkpoint. Only that checkpoint may resume B2.
