# C3-B1 replacement final acceptance — round 3

## Verdict and independent identity

`pass`

Fresh acceptance identity: `c3-b1-final-acceptance-3`.

I independently accept only the exact immutable replacement candidate
commit/tree `4a7dc728048812cfb4cf46f010939c182ac948cf` /
`5ee316695d3a4acf8f30e60da377ba6651844969`, after fresh verifier
`c3-b1-final-verifier-3` and complete accumulated validation. This acceptance
identity is distinct from the primary orchestrator, all six current internal
implementation/verification/acceptance identities, the fresh final verifier,
and the later replacement-manifest verifier. The later manifest verifier must
remain a new identity and receives no result from this acceptance.

This pass authorizes only atomic replacement-manifest assembly. It does not
accept a manifest or checkpoint, resume B2, execute any decoder or external
runtime, access hardware, authorize distribution, broaden macOS-only support,
or begin Cycle 4.

## Immutable subject and byte checks

- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Candidate commit/tree:
  `4a7dc728048812cfb4cf46f010939c182ac948cf` /
  `5ee316695d3a4acf8f30e60da377ba6651844969`.
- Candidate scope is exactly two added paths: the round-3 JSON binder and its
  rationale; current bytes are identical to the immutable commit.
- JSON SHA-256:
  `a46a7b3fc5a684a77990b8f4373f710002411901d2610d1fa30d275e5b07f57c`.
- Rationale SHA-256:
  `eb570fe3498232a0a206dc168a5afa0f404eca9dd8d1a173a99e746b6a6af20b`.
- Fresh verification descendant/tree:
  `fdbbc120d8bfa4d57e10c5c0ebe3737b3b98a71f` /
  `8ef2194c11f1561ab79e5a766fa4c01d5c26ef94`.
- Verifier test SHA-256:
  `3fc6503e2273bfd24c4f908ffb08f0235b498e86913eca33137725224dc6118f`.
- Verification record SHA-256:
  `caadb30ef321413329cc4f9b976ace41232c4cf90df4f891239b082347ce7355`.
- Complete accumulated descendant:
  `a888cddc1a995eceb9cc4380af67fe246d4a12af`; accumulated-record
  SHA-256:
  `467a8264736b761c26c6bfea676f5852801cad0ab2ed9d3dd63011a2b99d6b34`.

Git object, tree, scope, byte, commit, and ancestry checks closed the governing,
candidate, verifier, accumulated-validation, and every live bound evidence
identity. Candidate-to-verifier-to-accumulation ancestry is intact. All bound
artifact digests and candidate/proposal trees resolve to the stated live
objects.

## Static acceptance checks

The audit confirmed:

1. `C3B2-IF001` correctly invalidates the old final candidate, manifest, and
   checkpoint and orders the independently derived incomplete-UART fixture
   correction before all rebound evidence. The earlier `C3B1-FV001` complete
   ordered-history correction and all other closed finding/invalidation history
   remain explicit.
2. The semantic-fixture implementation history is complete through replacement
   7 and the pre-execution-runner history through replacement 3. Their six
   current internal identities are pairwise distinct and separated from root,
   the final verifier, this acceptance, and the required later manifest
   verifier.
3. Project/license scope remains an engineering disposition, not legal advice;
   package build, conveyance, and distribution remain prohibited absent
   rights-holder or qualified-counsel confirmation.
4. The renewed operator approval binds exactly 29 round-3 values. Every value
   is an inclusive maximum with first rejection at value plus one. The corrected
   `successful_parent_total_ns` is exactly `1,000,000,000`, and
   `spi_max_word_size_bits` is exactly `8`. Exactly 28 numeric values are
   unchanged from round 2; the superseded round-2 proposal/approval transfers
   no authority.
5. The former final candidate, manifest, and checkpoint transfer no pass or B2
   authority. Status remains `candidate-not-accepted` pending this independent
   gate and the later atomic manifest sequence.
6. Fresh verification is non-vacuous: its direct guards cover schema, status,
   authority, identities, histories, digests, live objects, limits, approval,
   commands, applicability, exclusions, gate ordering, and 21 mutation
   families. A fresh static-only rerun passed exactly `23 passed in 0.63s`.
7. Complete accumulated Python evidence is exact: `654 passed`, four explicitly
   optional inherited C2-B3 physical-artifact skips, two historical
   deselections, and 149 warnings. The four ignored modules are exact
   downstream/superseded-subject exclusions. The targeted invalidation audit is
   exactly 44 expected historical failures and 45 still-passing negative
   checks.
8. Complete Node 22 evidence covers lint, typecheck, five unit tests, production
   build/assets, both Playwright suites, and frozen B6 performance. The first
   maximum-width browser launch failed before any test because the clean clone
   lacked its validation-only `.venv` link, supplied no evidence, and was
   correctly replaced by an unchanged-byte rerun that passed.
9. Clean-clone residue is limited to documented validation-only symlinks and
   browser results; process cleanup found no relevant survivor. Main-worktree
   preserved B2 paths were neither inspected nor modified.

## Findings and disposition

Findings: none.

The exact candidate is ready only for atomic replacement-manifest assembly,
followed by distinct fresh manifest verification, a joint manifest/verification
commit, and a replacement B1 checkpoint in the mandated order. Only that
checkpoint may resume B2.
