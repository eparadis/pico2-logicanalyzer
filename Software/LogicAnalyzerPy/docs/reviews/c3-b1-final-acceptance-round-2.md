# C3-B1 final acceptance — round 2

## Identity, immutable subject, and verdict scope

- Acceptance identity: `c3-b1-final-acceptance-2`
  (`/root/c3_b1_final_accept_fresh`), distinct from the primary orchestrator,
  all six internal C3-B1 evidence identities, fresh final verifier, and later
  manifest verifier.
- Corrected final candidate commit/tree:
  `1f8793210a3298ed190ff30f97c84b6f9feb9b29` /
  `cbe33ca272ba1b452f6d87fb5e702134a471f702`.
- Fresh final-verification pass: commit
  `a5fb09315064c49772d453ab5c1ba9d3a0200ba5`; record
  `docs/reviews/c3-b1-final-verification-round-3.md`; SHA-256
  `4f043b102e4d3b16c3475b6622535983ac2443d4d86bc7caa914b065a2a6dee8`.
- Fresh complete accumulated-validation pass: commit
  `421519d3f0a95a68ab8ee173083cf90006913244`; record
  `docs/reviews/c3-b1-final-accumulated-validation-round-2.md`; SHA-256
  `f33c24102a8bd02927424744f44df4c486071cf5be4fe6208c8631611ff6b28a`.
- Acceptance assignment commit: `fd7617cd2654698842e075cdc4108aa529622ce3`.
- Completed: `2026-08-27T19:21:55Z`.

This is a fresh static acceptance audit after `C3B1-MP001`. No former final
verification, accumulated-validation, or acceptance verdict transfers. I
repaired no candidate or evidence input, ran no product or test workload,
assembled no manifest, and created only this acceptance record.

## Findings and dispositions

1. **Exact candidate and scope — pass.** Candidate `1f87932` adds exactly the
   assigned round-2 binder JSON and rationale. Its tree resolves to the bound
   tree, its two paths remain byte-identical to the candidate blobs, and their
   SHA-256 values remain respectively
   `55983bbe9613c0deb0fe7f05a2e88b680b9cfed352f4cccfae9cdd01ca744adf`
   and
   `9577c4b268af5a4a8c6b7f59f934e8ba689a23d4bda66aa0e8662533acd82396`.
   Status remains `candidate-not-accepted`, support remains macOS-only, and no
   product, lock, workflow, prior evidence, or governing byte is part of the
   candidate change.

2. **`C3B1-FV001` correction and ordering — pass.** The superseded round-1
   candidate, its assignment, the failed-verification assignment, and immutable
   `changes_required` record are all named. The correction assignment precedes
   candidate `1f87932`. Normalizing the two explicit implementation histories
   back to the former preservation booleans and restoring the round-1 governing
   block makes round 2 equal round 1; no evidence, command, environment,
   applicability, exclusion, or authority meaning changed.

3. **`C3B1-MP001` correction and role separation — pass.** The manifest
   preflight finding correctly invalidated the former primary final-verifier
   and final-acceptance role reuse without changing the candidate or internal
   evidence. Fresh verifier `c3-b1-final-verifier-2` reviewed the unchanged
   candidate first; root then repeated the complete accumulated gate; this
   fresh acceptance followed both committed passes. The six internal final
   roles are pairwise distinct. Fixture implementation history explicitly
   orders the original implementor then replacements 1 through 6, ending in
   replacement 6; runner history orders the original implementor then
   replacements 1 through 3, ending in replacement 3. This identity and the
   fresh verifier are distinct from all six and from each other. The later
   manifest verifier must remain a fourth distinct primary identity.

4. **Evidence closure and internal gates — pass.** All 32 live artifact
   SHA-256 values independently recompute exactly. All 20 referenced commits
   are reachable, and the fixture, runner, raw, and proposal candidate commits
   resolve to their four bound trees. The five evidence groups preserve the
   project/license disposition; corrected semantic-fixture verification,
   complete accumulation, and acceptance; corrected pre-execution-runner
   verification, complete non-decoder accumulation, and acceptance; immutable
   raw-baseline reproduction, accumulation, and acceptance; and corrected
   threshold-proposal verification, accumulation, acceptance, and operator
   decision. Superseded fixture and runner candidates, discarded raw attempts,
   `C3B1-RI011`, `C3B1-RI013`, and `C3B1-TPV001` remain visible history rather
   than transferred evidence.

5. **Project/license disposition — pass with the recorded limitation.** The
   bound engineering review preserves exact nine-file provenance and planned
   private placement, unchanged component notices, package metadata and
   attribution obligations, and the prohibition on package build or
   distribution at this gate. It is not legal advice. The shim's missing
   in-file notice and existing MIT-label authority require rights-holder or
   qualified-counsel confirmation before conveyance; absent or negative
   confirmation continues to prohibit build and distribution.

6. **Operator-approved values and boundaries — pass.** The proposal has 29
   unique values matching the exact committed operator approval. Every value
   is an inclusive maximum and every first rejected integer is exactly value
   plus one. In particular, `successful_parent_total_ns` is
   `900000000`/`900000001` ns and `spi_max_word_size_bits` is `8`/`9` bits.
   Proposal, rationale, review-chain, and operator-decision identities and
   digests are exact. No value was weakened, increased, rebased, or inferred.

7. **Fresh final verification — pass.** The fresh verifier is independent and
   binds the exact candidate/tree, both candidate digests, complete identities
   and histories, correction-only equivalence, 32 digests and reachability, 29
   boundaries, 21 frozen commands, historical applicability, project/legal
   limitations, exclusions, and cleanup. Its 20 static checks and 17
   non-vacuous mutation families passed, it reports no finding, and its record
   remained unchanged at the bound digest.

8. **Fresh complete accumulated validation — pass.** The new post-MP001 gate
   records all 21 frozen command classes passing under repository-local CPython
   3.12.13 and exact Node 22.14.0. The unfiltered inventory transparently
   reproduced 657 passes plus the three immutable history-sensitive failures;
   the applicable run deselected only those exact nodes and passed all 657
   selected tests with 149 inherited warnings. Dependency health, Ruff, both
   strict mypy scopes, fixture and binding determinism, installed CLI help, six
   Cycle 2 validators, frontend lint/type/five unit/build/assets, four browser
   tests, and offline performance all passed. The malformed npm invocation
   that placed `--script-shell` after `--` exited 1 under the system Node and is
   transparently rejected as evidence; the accepted lint, typecheck, and unit
   reruns used the corrected npm option position and exact Node 22.

9. **Locks, retained evidence, scope, and cleanup — pass.** The two Python lock
   digests remain
   `6f78ec8f0219b919c44ed9b9f1d30c2337fcce7c911b8d3dc4c13edb707a6575`,
   package lock remains
   `d388a2668b3f65edeb62ee99da3ad37ffc56ab1ca3439b6d418a6bbe92e838d9`,
   and production asset manifest remains
   `00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9`.
   The ignored retained performance report recomputes to
   `b676ca953d3c989dbbc06e2ea68b3e63f0e117fab6929b5c6bd1693e065dd2a9`.
   Candidate quiet diff, tracked worktree, and whitespace checks were clean.
   The final targeted process audit found no pytest, Playwright, Vite, Cycle 3
   characterization, product-web, or `server.main` process.

10. **Limitations, exclusions, and next authority — pass.** No product decoder
    host or public decode API, external decoder runtime, hardware/USB/serial/
    firmware evidence, wheel/sdist/upload/publication/distribution, non-macOS
    support claim, B2 work, or Cycle 4 action is accepted or authorized. The
    exact corrected candidate is ready only for atomic C3-B1 manifest assembly,
    followed by independent verification under the separately assigned fresh
    manifest-verifier identity, joint manifest/verification commit, and later
    checkpoint commit. This verdict does not create any of those later facts.

No finding is open.

## Static acceptance checks

- Exact candidate commit/tree/two-path scope and current-byte comparison:
  passed.
- Candidate binder/rationale, fresh verifier, fresh accumulated record,
  approval, locks, assets, and retained performance digest recomputation:
  passed.
- All 32 live evidence digest recomputations: passed, zero mismatches.
- All 20 referenced commit ancestry checks and four candidate-tree
  resolutions: passed.
- Six-role and complete ordered-history audit, final-role separation, and
  normalized round-2/round-1 comparison: passed.
- Independent exact 29-value and value/value-plus-one comparison against the
  proposal and approval tables: passed.
- Final repository and prohibited-process quiet audit: passed.

## Safety statement

Only static Markdown, JSON, Git, digest, lock, artifact, and process inspection
occurred. No snapshot, decoder, runner, probe, product host, pytest, browser
server, hardware, network, install, build, publication, manifest assembly, B2,
or Cycle 4 action ran. No worker remains.

## Verdict

`pass`
