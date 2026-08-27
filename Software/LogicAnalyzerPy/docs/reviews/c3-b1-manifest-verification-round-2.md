# C3-B1 manifest verification — round 2

## Identity, immutable subject, and verdict scope

- Manifest verifier: `c3-b1-manifest-verifier-2`
  (`/root/c3_b1_manifest_verify_fresh`), distinct from the root orchestrator and
  manifest assembler, all six C3-B1 internal identities,
  `c3-b1-final-verifier-2`, and `c3-b1-final-acceptance-2`.
- Candidate commit/tree:
  `1f8793210a3298ed190ff30f97c84b6f9feb9b29` /
  `cbe33ca272ba1b452f6d87fb5e702134a471f702`.
- Round-1 immutable `changes_required` record: commit
  `96d80b61781640eab36430e94de44a3d345f3e11`; record SHA-256
  `d0cb35ed59b9674645ce7f5036d4c7e803c9f5ee21d6d9cdbe384d0424220a78`.
- Correction assignment commit:
  `364df69571e43c1ac6e23cf71fa0933f5f725336`.
- Corrected manifest:
  `Software/LogicAnalyzerPy/testdata/evidence/c3-b1.json`.
- Corrected manifest SHA-256 at intake and after all verification:
  `580bd6ac8603602f43f9f2ca04bed552073f3de2e43df4ac35df81c1e720743b`.
- Completed: `2026-08-27T19:37:36Z`.
- Intake state: HEAD `364df69571e43c1ac6e23cf71fa0933f5f725336`;
  only the assigned corrected manifest was untracked. Its bytes remained
  unchanged throughout this review.

This is a complete fresh audit; no round-1 result transfers. A pass permits
only the joint manifest/verification-record commit and the later checkpoint
sequence. It is not itself a manifest commit, checkpoint, or B2 authority.

## Exact checks and results

All commands ran through RTK and were static/read-only except creation of this
record.

1. `rtk shasum -a 256 Software/LogicAnalyzerPy/testdata/evidence/c3-b1.json Software/LogicAnalyzerPy/docs/reviews/c3-b1-manifest-verification-round-1.md Software/LogicAnalyzerPy/docs/evidence-manifest/cycle3-schema.json Software/LogicAnalyzerPy/scripts/validate_cycle3_evidence.py`
   returned respectively the manifest digest above, the immutable round-1
   digest above, schema digest
   `779d313ee79fabe8e98e627f7d6e27f0e436873ee2b8e118c0a3cac89e6bf3a3`,
   and validator digest
   `39dd55f204e66e9ae2ff7519f43a2bf4053e7017eb8ad294f00ec654ae9b4c21`.
2. From `Software/LogicAnalyzerPy`,
   `rtk .venv/bin/python scripts/validate_cycle3_evidence.py docs/evidence-manifest/cycle3-schema.json testdata/evidence/c3-b1.json`
   exited 0 with no output.
3. An independent read-only JSON traversal recursively collected every lock,
   artifact, and nested `{path, sha256}` reference and recomputed all current
   repository bytes. It found 78 occurrences, 43 unique path/digest pairs,
   zero missing paths, and zero digest mismatches. All 23 distinct hexadecimal
   artifact revision commits are ancestors of current HEAD.
4. A separate artifact-revision audit read every declared path directly from
   its declared revision using `git show REVISION:PATH` and recomputed its
   SHA-256. All 39 revision/path/digest triples matched; no path was absent and
   no digest differed.
5. Candidate resolution returned tree
   `cbe33ca272ba1b452f6d87fb5e702134a471f702`, exactly matching the manifest.
   All 21 command records have unique names, exit 0, `skipped: false`, and the
   single exact candidate binding
   `1f8793210a3298ed190ff30f97c84b6f9feb9b29`.
6. A complete command comparison formed normalized command strings from every
   exact `argv` in
   `testdata/decoders/cycle3/b1-final-candidate-round-2.json` and compared them
   with all manifest command records. The ID sets were equal and the mismatch
   list was empty, including the full three-node deselection vector for
   `python_applicable_nonhardware`.
7. A correction-only byte audit replaced in memory only the corrected goal,
   schema, and validator revisions and the exact pytest vector with their four
   round-1 values. The resulting SHA-256 was exactly
   `c361a0e1c7c18147fbd0f9c87eb1b9c9b9358030e80ddb0fab381901ef183da8`,
   proving that no other round-1 manifest byte changed.

## Independent semantic audit

- The four primary identities are distinct. The six internal identities are
  pairwise distinct and disjoint from final verification, acceptance, and
  manifest verification. The role map truthfully preserves the complete
  semantic-fixture and runner gate identities.
- The tested candidate/tree and all evidence descendants are ordered
  correctly. `C3B1-MP001` is preserved as closed; fresh verification commit
  `a5fb09315064c49772d453ab5c1ba9d3a0200ba5` precedes fresh complete
  accumulated commit `421519d3f0a95a68ab8ee173083cf90006913244`,
  which precedes fresh acceptance commit
  `792fec42fef2c0b37aab80bcb48231dff9949e8b`, atomic manifest assignment,
  round-1 findings, and the bounded correction assignment.
- The manifest contains exactly the 21 frozen command identities and matches
  the fresh accumulated evidence: every accepted result is successful and no
  mandatory gate is represented as skipped. The transparently rejected npm
  invocation is not claimed as evidence.
- Requirements are bounded to B1's accepted ownership: R1-R5 and the B1 start
  of R9, R21, and R23-R25. Stopping-condition mappings are limited to 1-3.
  The manifest explicitly limits these to earliest-owned B1 proof and defers
  final proof to C3-B5.
- Findings are the five closed B1 findings `C3B1-RI011`, `C3B1-RI013`,
  `C3B1-TPV001`, `C3B1-FV001`, and `C3B1-MP001`. Decisions preserve exact
  operator approval and the project/license non-conveyance limitation.
  Limitations, deferred work, all eight audit categories, and all six required
  `b1_evidence` references are present, digest-bound, and within accepted B1
  authority.
- No manifest self-reference, manifest-verification verdict or record path,
  checkpoint fact, B2 authority, future CI result, completion closure, or other
  predictive evidence appears.

No finding is open.

## Safety statement

No manifest, candidate, prior record, schema, validator, product, test,
fixture, method, lock, workflow, or evidence input was edited. No product/test
workload, browser, characterization runner, decoder, hostile probe, hardware,
network, install, build, publication, B2, or Cycle 4 action ran. I created only
this round-2 verification record and did not commit.

## Verdict

`pass`
