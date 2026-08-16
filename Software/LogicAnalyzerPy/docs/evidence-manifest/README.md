# Evidence manifests

Every accepted checkpoint records one sanitized JSON manifest under
`testdata/evidence/` that validates against `schema.json`. It anchors evidence
to the full tested commit/tree, qualified worktree state, UTC time, OS and
architecture, Python version, lock digest, normalized commands and exits,
stable verifier identity, provenance categories, and artifact digests.

Hardware manifests additionally use the literal `<PORT_SUPPLIED>` rather than
the host serial path and record sanitized board, firmware, front-end, and test
parameters. They contain no user name, laboratory secret, or raw unsanitized
device metadata. C1-B4/B5 own the atomic hardware-manifest writer and physical
procedure.
