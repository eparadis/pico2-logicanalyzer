# C3-B1 replacement final acceptance — round 4

## Verdict and independent identity

`pass`

Fresh acceptance identity:
`c3-b1-final-acceptance-replacement-1`. Assignment commit: `e288a97`.

I independently accept only the exact immutable replacement candidate
commit/tree `7246dcbe55a60ef7ee9196f4bf265c7c75141d55` /
`51e895a1e2c95580d04bc8a31ed8d58a85613e1a`, after fresh verifier
`c3-b1-final-verifier-replacement-1` and complete root accumulated validation.
This acceptance identity is distinct from the primary orchestrator, the six
current internal implementation/verification/acceptance identities, the fresh
final verifier, and the required later replacement-manifest verifier.

This pass authorizes only atomic replacement-manifest assembly. It does not
accept a manifest or checkpoint, resume B2, execute a decoder or external
runtime, access hardware, authorize distribution, broaden macOS-only support,
or begin Cycle 4.

## Immutable subject and byte checks

- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Candidate commit/tree:
  `7246dcbe55a60ef7ee9196f4bf265c7c75141d55` /
  `51e895a1e2c95580d04bc8a31ed8d58a85613e1a`.
- Candidate scope is exactly two added paths: the round-4 JSON binder and its
  rationale. Current bytes are identical to the immutable commit.
- JSON SHA-256:
  `a186af26805c804613271641e5f57b1393ae31d79fa800a29249e37efc0650fd`.
- Rationale SHA-256:
  `591459742b9453e94047438ec79a6e2bdd54ed3b6d0c71207bbae4c64b563d73`.
- Fresh verification descendant/tree:
  `e1b87533d09d716634095ebb8d5748cf4b857c98` /
  `a31ff03e22bc516f0d712c59fc8ab09aa6496464`.
- Verifier test SHA-256:
  `56a4892a9a25ace4a7cc6ec640ab12e1669ad56f7e345410c5e26eb9e9d8b32b`.
- Verification record SHA-256:
  `b3eb336c66ab35d1ef7981477bcc97267ad144f387b9b922547402fae7ad9378`.
- Complete root accumulation commit/tree:
  `64a0468ef0e04d21e758730b18bd7d87ee599c3b` /
  `3059396a6a7573ffe19d05fd4b6e1d9f8a95528f`.
- Accumulated-record SHA-256:
  `6cb1ea184e0a36151b25cb17b24ae797de5a52d5acbd8fb630d2db791680df6b`.

Git object, tree, exact scope, current-byte, digest, and ancestry checks closed
the governing, assignment, candidate, verifier, accumulation, and every live
bound evidence identity. Candidate-to-verifier-to-accumulation-to-acceptance
assignment ancestry is intact. The corrected fixture, replacement runner,
fresh raw, and round-4 threshold proposal trees resolve to the stated objects.

## Corrected evidence and authority chain

The accepted binder preserves the complete ordered replacement chain:

1. project/license disposition `538a4aa`, with its rights-holder or
   qualified-counsel limitation;
2. corrected semantic fixture candidate `3af6b9f`, verifier `3a29e46`,
   accumulation `efcc775`, and acceptance `9723221`;
3. replacement runner candidate `380d5dd`, current verifier `e95706f`,
   accumulation `e1e8bab`, and acceptance `01f059c`;
4. fresh raw candidate `d0d9dbe`, verifier `1739736`, accumulation `7295e4d`,
   and acceptance `72168f4`; and
5. round-4 threshold proposal `b680aa5`, verifier `46d57e4`, accumulation
   `62b67fe`, acceptance `f28643b`, and exact operator approval `afd4585`.

The corrected fixture history is complete from
`c3-b1-semantic-fixture-implementor-1` through replacements 1–8. The runner
history is complete from `c3-b1-pre-execution-runner-implementor-1` through
replacements 1–4. The six current identities are pairwise distinct:
`c3-b1-semantic-fixture-implementor-replacement-8`,
`c3-b1-semantic-fixture-correction-verifier-2`,
`c3-b1-semantic-fixture-correction-acceptance-2`,
`c3-b1-pre-execution-runner-implementor-replacement-4`,
`c3-b1-pre-execution-runner-rebinding-verifier-5`, and
`c3-b1-pre-execution-runner-rebinding-acceptance-3`.

The binder retains `C3B1-RI011`, `C3B1-RI013`, `C3B1-TPV001`,
`C3B1-FV001`, `C3B1-MP001`, `C3B1-MV001`, `C3B1-MV002`, `C3B2-IF001`,
`C3B1-RV001`, `C3B2-IF002`, `C3B1-RA001`, `C3B1-RV002`, and `C3B1-RV003`
as closed findings with their ordered invalidations. Superseded fixture,
runner-verifier, raw, threshold, final-candidate, manifest, and checkpoint
passes transfer no verdict or authority. In particular, four discarded
write-at-end raw attempts totaling 847 launches remain non-evidence, and only
the successful 486-launch fresh raw collection plus its two separate
486-launch reproductions support this chain.

## Threshold and verifier audit

The operator statement in approval commit `afd4585` binds exact proposal
`b680aa59fba4a18da2aeaacc8cbd7ad3a68784e0` / tree
`e8661f094ba0423ca08055ea785bbfcde8554d71`. Proposal and approval-record
SHA-256 values are
`98e48bb1882104d893a1d4d85659845ff20054f9b52f0b09fdf73efad2547e3c`
and
`ff1ba9665174b0912adea9eb4682d1a9e6839c6ec9b5efce073a9b055303aba6`.

All 29 values match the proposal and approval record. Each is an inclusive
maximum and rejects value plus one. Exactly 26 values are unchanged from round
3; the three replacements are `parent_retained_growth_bytes = 33,554,432`,
`successful_parent_total_ns = 1,300,000,000`, and `launch_ns = 50,000,000`.
The hard-limit inventory includes the 68,719,476,736-byte worker address-space
limit and eight-bit maximum SPI word size; the remaining regression ceilings
and hard boundaries also match exactly. Round-3 proposal `b260d9e` and approval
`63fdfee` transfer no authority.

Fresh verification is non-vacuous. Its direct checks cover exact schema,
status, macOS environment, authority, Git scope/bytes/trees/ancestry, all live
digests, role separation and histories, evidence groups, all limits and
boundaries, approval, findings, invalidations, 21 frozen commands, exact
applicability, exclusions, and downstream order. Twenty independent mutation
families must fail. My permitted static-only rerun completed with exactly
`22 passed in 0.67s`.

## Accumulated validation, scope, and cleanup

The accepted include-only Python 3.12 inventory classified exactly 57 tracked
test modules as 42 included and 15 excluded. It collected 630 tests and
completed with 624 passed, six inherited classified skips, 106 warnings, and
no mandatory Cycle 3 skip. It included the current corrected-fixture raw
verifier, a complete 486-launch reproduction, 30 threshold tests, and 22 final
verifier tests.

One earlier inventory-selection attempt incorrectly selected the superseded
raw verifier. Its 623 passes, six inherited skips, and expected stale-digest
failure are transparently recorded and discarded in full; they supply no
result or authority. Root corrected the one path and repeated collection and
the complete gate from the start without changing candidate bytes.

Repository-local Python dependency, whole-project Ruff, strict product and
characterization typing, deterministic fixture and runner binding, installed
CLI help, and all six Cycle-2 evidence checks passed. Exact Node 22 lint,
typecheck, five unit tests, production build/assets, isolated 1/1 maximum-width
browser, isolated 3/3 live/shell browser, and 1/1 frozen B6 performance checks
passed. The initial sandbox-blocked maximum-width launch supplied no evidence;
the unchanged approved isolated rerun passed.

The project/license disposition remains engineering review, not legal advice.
Package build, conveyance, publication, and distribution remain prohibited
without rights-holder or qualified-counsel confirmation. Clean-clone residue
is limited to documented validation-only links and browser results, and final
process checks found no survivor. The main-worktree preserved untracked B2
paths were excluded by pathname only and were neither inspected nor modified.
No decoder, runner, raw reproduction, product/B2/downstream suite, browser,
hardware, network, package, or Cycle 4 action ran during this acceptance.

## Findings and disposition

Findings: none.

The exact candidate is ready only for atomic replacement-manifest assembly,
followed by distinct fresh manifest verification, a joint
manifest/verification commit, and a replacement B1 checkpoint in the mandated
order. Only that checkpoint may resume B2.
