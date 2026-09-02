# C3-B4 manifest verification — round 1

## Identity, subject, and verdict

- Manifest verifier: `c3-b4-manifest-verifier-1`
  (`/root/c3_b4_manifest_verify_r1`), fresh and distinct from the B4
  implementor, verifier, accumulated-validation owner, acceptor, and root
  evidence assembler.
- Timestamp: `2026-09-02T09:42:27Z`.
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Assigned acceptance HEAD/tree:
  `2c98a6a78af5555473719b612812343d0296bc20` /
  `f0aad54498f48229bc992edf7c119aaa7026e4fe`.
- Untracked post-acceptance manifest:
  `Software/LogicAnalyzerPy/testdata/evidence/c3-b4.json`.
- Exact manifest SHA-256:
  `699443c5ed9cb2ddd668b4b486311e251647cadf5aeb3a435263dd2597e0f72c`.
- Manifest-tested verifier commit/tree:
  `5c3427f0a176ba4db8f48b17521d9482f42ead8b` /
  `43f1b950ade7d2ebb1ce82941c71be8ec23e7171`.
- Immutable B4 product candidate/tree:
  `921f8984b45d78d544494733c9fcd043a788f866` /
  `0b0ea4529e6c2279cdd5b6b766377ea5e75a73e7`.
- Environment: macOS 15.7.9 build 24G830, x86_64, CPython 3.12.13.
- Verdict: **pass**.

This record independently verifies the exact unchanged post-acceptance
manifest bytes. It does not create or predict the separate B4 checkpoint and
does not authorize B5 or Cycle 4.

## Repository, identity, and ordering audit

Before this record was written, `git status --porcelain=v1
--untracked-files=all` reported only the proposed manifest. `HEAD`, its tree,
and the manifest digest matched the assigned values above; the manifest was
not tracked. Git ancestry proves the accepted B3 checkpoint `233b3b0` precedes
the B4 product candidate `921f898`, which precedes independent verifier
`5c3427f`, accumulated-validation record `63af13b`, and independent acceptance
`2c98a6a`. The acceptance commit timestamp precedes the manifest timestamp and
filesystem creation. No pass crosses a later product, test, or workflow
candidate.

The candidate-to-verifier diff adds only
`tests/verification/test_c3_b4_public_round15.py` and
`docs/reviews/c3-b4-verification-round-15.md`. The next two ordered commits add
only `docs/reviews/c3-b4-accumulated-validation-round-8.md` and then
`docs/reviews/c3-b4-acceptance-round-1.md`. Therefore the tested verifier SHA
contains the immutable product candidate plus its independent hosted-safe test,
while no product, fixture, threshold, limit, dependency, lock, workflow, or
accepted B1-B3 byte changes afterward.

The four manifest roles are distinct and exact:
`c3-b4-public-implementor-1`, `c3-b4-public-verifier-1`,
`c3-b4-public-acceptor-1`, and assigned
`c3-b4-manifest-verifier-1`. The implementor did not author B1 authoritative
expected output, the root-owned accumulated and hosted dispatch roles are not
represented as independent lane roles, and no identity is converted or reused.

## Strict validation and complete digest audit

The authoritative command

`rtk Software/LogicAnalyzerPy/.venv/bin/python
Software/LogicAnalyzerPy/scripts/validate_cycle3_evidence.py
Software/LogicAnalyzerPy/docs/evidence-manifest/cycle3-schema.json
Software/LogicAnalyzerPy/testdata/evidence/c3-b4.json`

returned exit 0 with no diagnostic. Independent schema inspection confirmed
draft 2020-12, a strict root, the complete required root field set, and
`additionalProperties: false` on every object definition. The schema and
custom validator resolve at their declared revisions and hashes.

An independent traversal of all locks, artifacts, and command, requirement,
stopping-condition, finding, decision, and audit evidence references found 25
unique paths, zero missing files, and zero digest mismatches. For all 21
artifact entries, SHA-256 over `REVISION:PATH` bytes exactly equals the declared
digest. The recomputed principal identities are:

- locks: requirements-dev
  `4efa0b1d42e5162c7a20177d1dd5e78083d75a87d2405709e04b1bcbd4f33c53`,
  requirements-web
  `4b0feeadf92c0bcb9f2790cc62f6b6e2f7da8937f30ff50d0c9092fd003b8145`,
  package lock
  `d388a2668b3f65edeb62ee99da3ad37ffc56ab1ca3439b6d418a6bbe92e838d9`,
  and production assets
  `00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9`;
- schema/validator:
  `779d313ee79fabe8e98e627f7d6e27f0e436873ee2b8e118c0a3cac89e6bf3a3` /
  `6b677cbc01f2ee27df4b8aaf83ab4f51465f170f2b69baa3706fe7c6a4dffdca`;
- inherited manifests C3-B1/B2/B3:
  `3710e7fde7523096b70607b3a7da217b1e71fdb46492b83b72861e3eaa48cfae`,
  `2af5bfc21a5d888132fb4e468f543403e8948632ad9ab2dd11b8da854dd4a602`,
  and `4d17a6f0a1401799f1d7c0c65870744aada26eb2a3b1b8d5c723d447ceb4fac1`;
- B4 implementation public module/CLI:
  `d5cd8b843bf2bd847dc42a7fa550d5756615177d77e80912472d088b9e6519db` /
  `c3acce4965faeff55c6177dfdfff840d7a2b9c65a6ae4b05b45f26974f1d3ddc`;
- workflow:
  `12ff6bb2cd7e437b733f3aaeb9488c6926604572419468c60604f0dea1c6a990`;
- verification, accumulated validation, and acceptance reviews:
  `f131d75e72a27dbf99acf77b0e70ac95be8daa5edfab1b1067e6d6939e1b34f7`,
  `f80004c42a1cefa8944ec5e8fc451aa687ace3ccfecdbb42cac2e06d351f1b79`,
  and `59b21b36338d103a1984c42afd1732092879bb2c2b6efed2ec7cb6a397844503`.

## Contract, evidence, and hosted audit

The manifest maps exactly B4-owned R17-R20 and continuous R21, R23, R24, and
R25. It maps exactly applicable stopping conditions 11, 12, 13, 14, 16, and
17, without claiming condition 16's final five-checkpoint outcome. Every map
entry is `pass`, has committed digest-valid evidence, and agrees with the
governing ownership table and accepted B4 record.

The five command entries are all successful, non-skipped, and bound to exact
tested commit `5c3427f`. Their evidence supports the 70-test public-contract
acceptance; 1,472 passes, seven classified skips, and 38 transparent
deselections from 1,517 collected/1,479 selected cases; static, dependency,
frontend, resource, and binding gates; inherited evidence/scope/legal gates;
and exact-candidate hosted macOS execution. The count arithmetic is exact.

The retained GitHub Actions response under repository-ignored `.tmp` confirms
run `33612103404`, job `100189420170`, head
`5c3427f0a176ba4db8f48b17521d9482f42ead8b`, label
`macos-15-intel`, and conclusion `success`. Every recorded job step concluded
success without retry. This independently corroborates the manifest's
`hosted_ci` binding and the accumulated record rather than substituting a new
dispatch.

Findings C3B4-V001 through C3B4-V004 are present exactly once and closed with
digest-valid acceptance evidence: the public model surface is closed; public
limits only tighten; CSV physical metadata remains separate from decoder
mappings with exact failure taxonomy; and aggregate CLI diagnostics remain
bounded to 8,192 bytes. No unresolved manifest or candidate finding remains.

## Audits, limitations, and future-value exclusion

The manifest carries all eight required audit categories: prohibited runtime,
dependency, process, import, scope, license, rollback, and repository. Their
claims agree with the immutable verification, accumulated, and acceptance
records. Current static inspection found only inert historical
`libsigrokdecode` notice text in the accepted snapshots, not an import,
dependency, command, or external runtime path. Package metadata remains
`GPL-3.0-only` with exactly `LICENSE`, `LICENSES/GPL-2.0-or-later.txt`,
`LICENSES/MIT.txt`, and `ATTRIBUTION.md`; all four hashes match. The committed
process audit is digest-valid and no fresh live inventory is required by the
manifest-verification contract.

The limitations accurately preserve macOS/Python 3.12 support, the transparent
test partition, classified optional physical-artifact skips, and the controlling
non-conveyance limitation. Shim ownership, historical MIT labeling, and
combined-work treatment still require qualified-counsel or rights-holder
confirmation before conveyance. This is engineering evidence, not a legal
conclusion; no wheel, sdist, upload, publication, or conveyance is authorized.

The deferred-work and scope statements keep the B4 checkpoint pending and B5,
terminal closure, hardware, firmware, serial/live capture, browser decoder
behavior, dynamic discovery, stacking, `.lac`, unsupported platforms,
publication, conveyance, and Cycle 4 excluded. Static and structural checks
found no self-dependent manifest digest, manifest-verification command/result
or review path, future verifier verdict, checkpoint artifact, B5 artifact,
completion proof, or seal. Naming the assigned manifest-verifier role and
describing deferred future work do not claim those future results.

## Commands, findings, and authorization

Every shell command used the required `rtk` prefix, and all scratch/input API
responses stayed below repository-ignored `.tmp`. The audit used the strict
validator; independent JSON/schema traversal; SHA-256 recomputation; historical
`REVISION:PATH` hashing; `git rev-parse`, `merge-base`, `log`, diff, tree,
status, and whitespace checks; environment identity; hosted-response parsing;
and scoped license/prohibited-runtime/future-value inspection.

Three exploratory probes were non-authoritative and caused no file change: a
generic `jsonschema` module was absent from the locked environment, an initial
`.venv-web` location did not exist, and initial ad-hoc digest/schema one-liners
had syntax errors. The repository's dependency-free strict validator and
corrected independent checks above all passed. A current `rtk ps` probe was
sandbox-denied; the governing contract does not require a fresh live inventory
at manifest verification, and the committed digest-valid process evidence was
audited instead.

Findings: none. `APPROVAL_NEEDED`: none.

This pass authorizes only the root orchestrator's atomic commit of the exact
unchanged manifest with SHA-256
`699443c5ed9cb2ddd668b4b486311e251647cadf5aeb3a435263dd2597e0f72c`
and this immutable verification record, followed by a separate B4 checkpoint
record. Any manifest byte change invalidates this authorization.

`pass`
