# C3-B1 manifest verification — round 1

## Identity and immutable subject

- Manifest verifier: `c3-b1-manifest-verifier-2`
  (`/root/c3_b1_manifest_verify_fresh`), distinct from the root orchestrator and
  manifest assembler, all six C3-B1 internal identities,
  `c3-b1-final-verifier-2`, and `c3-b1-final-acceptance-2`.
- Candidate commit/tree:
  `1f8793210a3298ed190ff30f97c84b6f9feb9b29` /
  `cbe33ca272ba1b452f6d87fb5e702134a471f702`.
- Atomic manifest assignment commit:
  `134c5ba78a3729f717ada03cd8f6fbb3beb26744`.
- Manifest:
  `Software/LogicAnalyzerPy/testdata/evidence/c3-b1.json`.
- Manifest SHA-256 at intake and after all inspection:
  `c361a0e1c7c18147fbd0f9c87eb1b9c9b9358030e80ddb0fab381901ef183da8`.
- Verification completed: `2026-08-27T19:32:55Z`.
- Intake worktree: HEAD `134c5ba`; only the assigned manifest was untracked.
  The manifest remained byte-identical throughout this review.

This was static inspection only. I did not edit the manifest or any prior
artifact and did not run product, test, browser, characterization-runner,
decoder, hardware, network, install, build, publication, B2, or Cycle 4 work.

## Authoritative inputs and exact checks

The governing contract is commit/tree
`ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
`d9fb09345ab85580cd8c877745262d1b481e366f`. The accepted subject chain is the
fresh verifier record committed at `a5fb09315064c49772d453ab5c1ba9d3a0200ba5`,
the fresh accumulated record committed at
`421519d3f0a95a68ab8ee173083cf90006913244`, and the fresh acceptance record
committed at `792fec42fef2c0b37aab80bcb48231dff9949e8b`.

The following exact commands were run through RTK:

1. `rtk shasum -a 256 Software/LogicAnalyzerPy/testdata/evidence/c3-b1.json Software/LogicAnalyzerPy/docs/evidence-manifest/cycle3-schema.json Software/LogicAnalyzerPy/scripts/validate_cycle3_evidence.py`
   returned the manifest digest above, schema digest
   `779d313ee79fabe8e98e627f7d6e27f0e436873ee2b8e118c0a3cac89e6bf3a3`,
   and validator digest
   `39dd55f204e66e9ae2ff7519f43a2bf4053e7017eb8ad294f00ec654ae9b4c21`.
2. From `Software/LogicAnalyzerPy`,
   `rtk .venv/bin/python scripts/validate_cycle3_evidence.py docs/evidence-manifest/cycle3-schema.json testdata/evidence/c3-b1.json`
   exited 0.
3. A read-only Python JSON traversal independently collected every lock,
   artifact, and nested `{path, sha256}` reference, recomputed repository-file
   SHA-256 values, checked every hexadecimal revision for ancestry, resolved
   the candidate tree, and audited commands and role sets. It reported 78
   reference occurrences, 43 unique path/digest pairs, zero missing paths,
   zero digest mismatches, 21 reachable revision commits, the exact declared
   tree, 21 unique command names, all exit statuses zero, all `skipped` values
   false, one exact candidate binding, four distinct primary identities, six
   distinct internal identities disjoint from the final evidence roles, and no
   manifest self-reference.
4. A second read-only traversal compared each artifact blob with its declared
   hexadecimal revision. It exposed the three provenance-revision failures in
   `C3B1-MV001` below; all other revision/path/digest triples matched.
5. `rtk git cat-file -e ea83a403bb6f644d33069d3bebd41d5f1e0a60c0:Software/LogicAnalyzerPy/scripts/validate_cycle3_evidence.py`
   and the equivalent command for
   `Software/LogicAnalyzerPy/docs/evidence-manifest/cycle3-schema.json` each
   exited 128 because the path does not exist in that revision.
6. `rtk git show ea83a403bb6f644d33069d3bebd41d5f1e0a60c0:CYCLE3_GOAL.md | rtk shasum -a 256`
   exited 0 and returned
   `425b59c144bdd137f7477aa2de8ddf1785097bb6b106c1c1684091f6bd8a1031`,
   not the manifest's declared artifact digest.
7. Blob-introduction searches returned
   `6a2d09a444797bb0b73c94b259b1cbd826084129` for the current goal blob and
   `39e74a27638541b36b2845a8c6f1079bc0a3ae61` for both current schema and
   validator blobs.
8. A read-only comparison of all 21 manifest command strings with the exact
   `argv` records frozen in `b1-final-candidate-round-2.json` found identical
   ID sets and only the mismatch in `C3B1-MV002` below.

The schema/validator pass, candidate/tree binding, role separation, current
path/digest recomputation, revision reachability, fresh correction ordering,
B1-bounded requirement/stopping-condition mappings, findings/decisions/
limitations/deferred-work/audits, and `b1_evidence` structure otherwise pass.
The manifest contains no self-digest, future manifest-verifier verdict or
record path, checkpoint fact, B2 authority, or predictive closure claim.

## Findings and required dispositions

1. **`C3B1-MV001` — artifact revisions do not identify the declared bytes
   (`changes_required`).** The goal artifact declares revision
   `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` and current digest
   `4120b771ec36390a482671c8428d880bb2f60abe3fe154ef4e001efeaf3ddef7`,
   but that revision's goal blob hashes to `425b59c...`; the current blob was
   introduced at `6a2d09a444797bb0b73c94b259b1cbd826084129`. The schema and validator
   artifacts also declare revision `ea83a403...`, where neither path exists;
   both current blobs were introduced at
   `39e74a27638541b36b2845a8c6f1079bc0a3ae61`. Replace these three artifact
   revisions with truthful byte-owning revisions while retaining the governing
   contract identity separately. Then repeat manifest verification against the
   newly fixed manifest bytes; no result from this record transfers.

2. **`C3B1-MV002` — one frozen command is represented by prose rather than its
   exact command (`changes_required`).** The manifest records
   `.venv/bin/python -m pytest -m 'not hardware' with the three reviewed historical nodes deselected`.
   The frozen candidate instead binds the exact vector
   `.venv/bin/python -m pytest -m 'not hardware' --deselect tests/implementation/test_cycle3_fixtures.py::test_cycle3_fixture_surface_is_present_and_rebuildable --deselect tests/verification/test_c3_b1_raw_baseline_candidate.py::test_candidate_identity_digest_environment_schema_and_summary_arithmetic --deselect tests/verification/test_c3_b1_threshold_proposal.py::test_exact_candidate_hashes_evidence_environment_formulas_and_feasibility`.
   Replace the prose command with that exact normalized command. The result and
   applicability explanation may remain descriptive, but the command field
   must preserve the immutable executable vector.

These findings require only manifest correction under the orchestrator's
authority. They do not reopen or alter candidate `1f87932`, any internal B1
gate, fresh final verification, fresh accumulated validation, or fresh final
acceptance. No manifest commit, checkpoint, or B2 work is authorized by this
record.

## Verdict

`changes_required`
