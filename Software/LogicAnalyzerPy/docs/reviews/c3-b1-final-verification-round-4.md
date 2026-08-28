# C3-B1 replacement final verification — round 4

## Verdict

`pass`

Fresh verifier identity: `c3-b1-final-verifier-3`.

The exact immutable replacement candidate commit/tree
`4a7dc728048812cfb4cf46f010939c182ac948cf` /
`5ee316695d3a4acf8f30e60da377ba6651844969` passes independent static
verification. The candidate remains `candidate-not-accepted`; this result
grants no manifest, checkpoint, B2, external-runtime, hardware, distribution,
non-macOS, or Cycle 4 authority.

## Subject hashes

- `testdata/decoders/cycle3/b1-final-candidate-round-3.json`:
  `a46a7b3fc5a684a77990b8f4373f710002411901d2610d1fa30d275e5b07f57c`
- `docs/reviews/c3-b1-final-candidate-round-3.md`:
  `eb570fe3498232a0a206dc168a5afa0f404eca9dd8d1a173a99e746b6a6af20b`

Both current files are byte-identical to the two and only two paths added by
the immutable candidate commit. The candidate tree, governing commit/tree,
assignment and fresh-verification assignment ancestry, every live evidence
commit/tree, and all bound artifact digests were checked directly.

## Static coverage

The verifier checks the exact schema, round, status, macOS environment,
governing and correction records; complete semantic-fixture history through
replacement 7 and runner history through replacement 3; all six current
pairwise-distinct identities; `C3B2-IF001`, preserved `C3B1-FV001`, all closed
findings and historical invalidations; corrected fixture/runner/raw/round-3
threshold ordering; the exact 29 approved inclusive values and value-plus-one
boundaries, including `successful_parent_total_ns = 1,000,000,000` and SPI 8;
the renewed round-3 operator identity; all 21 frozen commands; the exact
635/2/4 applicability vector and exclusions; and the project/license legal
limitation.

Direct missing, extra, schema, status, authority, governing, correction,
environment, role-collapse, history, digest, evidence, limit, approval,
finding, invalidation, command, applicability, and exclusion mutations are
required to fail. The review text is also guarded for exact gate ordering and
for denial of transferred authority from the superseded round-2
proposal/approval and former final-B1 manifest/checkpoint.

## Validation

- Static verifier: `23 passed in 0.67s`.
- Ruff on the new verifier: `All checks passed!`.
- No prohibited runtime or preserved untracked B2 path was inspected or run.

## Findings

No findings. Fresh accumulated validation and independent acceptance remain
the next gates in the candidate's stated order.
