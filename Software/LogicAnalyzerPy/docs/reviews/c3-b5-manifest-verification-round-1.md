# C3-B5 manifest verification — round 1

## Identity and immutable input

- Verifier: `c3-b5-manifest-verifier-1`, distinct from the B5 implementation,
  final-proof verification, accumulated-validation, and acceptance roles.
- Governing contract/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Proposed manifest: `Software/LogicAnalyzerPy/testdata/evidence/c3-b5.json`.
- Manifest SHA-256 before verification:
  `c67031fa0f9590e9cc44134e382f2c3bec70e0744c91a4f26be6a559699e1532`.
- Exact tested verifier commit/tree:
  `2fb89fc8c36d93b4435032c07783532d6a8aa933` /
  `f155c06c8d61e9f454f2b7026afa0805999c4300`.
- Accumulated-validation commit:
  `eab754f565dd53fa1ab1a0ba844297c4cbb2b075`.
- Pre-manifest acceptance commit/tree:
  `41481e161f19c197927a34970ba16b2a46e5186c` /
  `c3d77a9b405d4523df33b637e821a1f8866da63c`.

I did not edit the proposed manifest. Before this record, it was the only
untracked path and no tracked path was modified.

## Independent validation

The frozen strict validator
`scripts/validate_cycle3_evidence.py` accepted the proposed manifest against
`docs/evidence-manifest/cycle3-schema.json` with exit status zero. I also
independently checked the validator's semantic constraints rather than relying
on schema acceptance alone.

- The checkpoint is exactly `C3-B5`; schema version, tested commit/tree,
  required B5 `hosted_ci`, and required `final_measurements` are present and
  correctly bound.
- Roles are exactly implementation
  `c3-b5-final-proof-implementor-1`, verification
  `c3-b5-final-proof-verifier-2`, acceptance
  `c3-b5-final-acceptor-1`, and manifest verifier
  `c3-b5-manifest-verifier-1`. All four are distinct.
- All 22 artifact paths exist and their current SHA-256 digests match. All 58
  command, requirement, stopping-condition, finding, decision, and audit
  evidence references exist and match their declared SHA-256 digests. All 13
  distinct declared revision/commit/tree objects exist. Lock and production
  asset digests also match.
- Requirements are exactly R1 through R26, once each, in order, with `pass`.
  Stopping conditions are exactly 1 through 17, once each, in order, with
  `pass`.
- Accepted manifest/checkpoint ancestry is ordered B1 manifest
  `885be61a...`, corrected B1 checkpoint `d4f984d...`, B2 manifest
  `0ece0492...`, B2 checkpoint `18614cc...`, B3 manifest `6f26cc8...`, B3
  checkpoint `233b3b0...`, B4 manifest `9178755...`, B4 checkpoint
  `9a8fc46...`, tested verification `2fb89fc...`, accumulated validation
  `eab754f...`, then acceptance `41481e1...`. Each adjacent identity is a Git
  ancestor of the next. The progress record contains the four completed B1-B4
  checkpoints in that order and leaves B5 in progress.
- The finding preserves C3B5-V001 and its correction: exactly one unrecorded
  warm-up per protocol followed by five retained observations per protocol,
  with no transferred earlier pass. Decisions, audits, limitations, legal
  boundary, rollback, and excluded scope agree with the accepted evidence.
- The GPL-3.0-only engineering disposition, retained GPL-2.0-or-later and MIT
  notices, attribution, non-conveyance boundary, and requirement for
  rights-holder or qualified-counsel confirmation before conveyance remain
  explicit. The manifest makes no legal conclusion and authorizes no package
  build, publication, or conveyance.
- The scope and prohibited-runtime audits exclude hardware, firmware, serial
  or live capture, browser decoding, dynamic discovery, stacking, `.lac`,
  unsupported-platform claims, external/reference decoder runtime, package
  construction, publication, conveyance, and Cycle 4.

## Final measurements and approved limits

The raw packet SHA-256 is
`980308fc3a144d1af70959793fb9e0b4476658b9856d56eb101876fc9fedb54e`.
It binds proposal commit `b680aa59fba4a18da2aeaacc8cbd7ad3a68784e0`,
proposal SHA-256
`98e48bb1882104d893a1d4d85659845ff20054f9b52f0b09fdf73efad2547e3c`,
method SHA-256
`f228f02892fc2ead00713606dc795850e14651baafc42a0974d1dbd48da86341`,
and fixture SHA-256
`34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094`.
It records Darwin x86_64 CPython 3.12.13, three warm-ups, 15 retained rows,
and 18 total launches. UART, SPI, and I2C each have repetitions zero through
four exactly once.

The independently recomputed 11 maxima exactly equal every manifest
`observed` value and remain below the unchanged round-4 ceilings:

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

The product's immutable `HARD_LIMITS` mapping exactly equals all 18 approved
hard-enforcement values, including SPI maximum word size eight bits with nine
rejected. Its `REGRESSION_LIMITS` mapping exactly equals all 11 approved
regression ceilings.

## Hosted and repository evidence

Fresh GitHub API inspection independently confirmed run `33655002746`, job
`100331249147`, attempt one, exact head
`2fb89fc8c36d93b4435032c07783532d6a8aa933`, workflow
`.github/workflows/logic-analyzer-python-cycle2.yml`, runner label
`macos-15-intel`, and final `success`. Every listed job step passed.

The focused final-packet and round-2 verifier selection produced three passes
and one expected historical phase assertion. The sole failure is
`test_b5_pre_manifest_packet_is_complete_and_b5_artifacts_are_absent`, whose
explicit pre-manifest invariant requires `c3-b5.json` not to exist. At this
authorized post-acceptance manifest-verification phase, the proposed manifest
must exist for immutable review. The strict validator and the remaining
measurement/verifier tests pass; this historical assertion is neither a
product defect nor contrary evidence about manifest contents.

Immediately before this record, only the unchanged proposed manifest was
untracked. There was no B5 checkpoint, Cycle 3 completion proof, closure
auditor verdict or record, completion seal, workflow/package/publication/
conveyance addition, or Cycle 4 material. The manifest text itself contains no
reference to any future checkpoint, completion proof, closure artifact, or
seal.

## Verdict

`pass`. The unchanged proposed C3-B5 manifest is strict-schema-valid,
semantically complete, digest- and revision-bound, correctly ordered, and
ready to be committed atomically with this distinct verifier record. Manifest
SHA-256 after verification remains
`c67031fa0f9590e9cc44134e382f2c3bec70e0744c91a4f26be6a559699e1532`.

`APPROVAL_NEEDED`: none.
