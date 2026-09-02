# C3-B4 accumulated validation, round 8

- Orchestrator role: root accumulated-validation and hosted-dispatch owner
- Timestamp: `2026-09-02T09:17:54Z`
- Governing B1 contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`
- Round-15 implementation candidate/tree: `921f8984b45d78d544494733c9fcd043a788f866` /
  `0b0ea4529e6c2279cdd5b6b766377ea5e75a73e7`
- Independently verified evidence commit/tree exercised by this gate:
  `5c3427f0a176ba4db8f48b17521d9482f42ead8b` /
  `43f1b950ade7d2ebb1ce82941c71be8ec23e7171`
- Workflow SHA-256: `12ff6bb2cd7e437b733f3aaeb9488c6926604572419468c60604f0dea1c6a990`

## Exact local and independent verification

Round-15 implementation validation collected 1,517 non-hardware cases, selected
1,479, and transparently deselected 38 cases through the unchanged 15-ignore,
37-selector partition. It finished with 1,472 passes and seven classified skips.
The hosted-present, both-absent fallback, and both partial artifact-environment
states behaved as specified; the partial states failed closed.

Fresh independent verification passed seven cases. The retained workflow,
pre-execution, B2, B3, and B4 sweep passed 1,034 cases with one classified
absent-artifact skip and 37 direct-suite deselections; the fixture-surface case is
the 38th workflow deselection outside that bounded direct sweep. Immutable archive
collection bound `c7650876544e477c277200c4f2fcbd23c67fe245` to
1,459/1,497/38 and the round-15 candidate to 1,479/1,517/38 without descendant
interference or scratch leakage.

The inherited-SIGTERM focused proof, raw B1 evidence, all retained B2/B3/B4
evidence, Ruff, mypy, strict installed-consumer typing, both `pip check` gates,
B1-B3 manifests, frontend lint/typecheck/five unit tests, the 29-module production
build, asset drift, CLI, metadata, resources, process cleanup, and no-drift audits
all passed. No product, threshold, B1, fixture, lock, manifest, or workflow byte was
weakened for this result.

## Exact hosted PASS

The exact evidence commit was pushed to dedicated branch
`cycle3-b4-ci-5c3427f`. GitHub Actions run
[`33612103404`](https://github.com/eparadis/pico2-logicanalyzer/actions/runs/33612103404),
job
[`100189420170`](https://github.com/eparadis/pico2-logicanalyzer/actions/runs/33612103404/job/100189420170),
resolved exact head `5c3427f0a176ba4db8f48b17521d9482f42ead8b` on the governed
`macos-15-intel` runner and concluded `success`. It ran from
`2026-09-02T09:04:22Z` through `2026-09-02T09:16:10Z`.

The runner guard, full-history checkout, pinned accepted CPython artifact download,
SHA-256 verification, extraction, exact runtime identity, clean core environment,
hash-locked dependency installation, editable source installation, `pip check`,
Ruff, mypy, strict public-consumer typing, focused inherited-SIGTERM gate, full
non-hardware Python partition, CLI help, clean web-runtime environment, web locks,
frontend lint/typecheck/unit tests, production build, asset-drift check, Chromium
installation, and production browser smoke all passed. No step failed or was retried.

Status polling used the saved read-only `rtk curl` command class, with response files
under repository-ignored `.tmp/c3-b4-ci/` and separate local JSON parsing. No repeated
approval class, workflow retry, artifact publication, or conveyance occurred.

## Disposition

The mandatory local, independent, and exact-candidate hosted gates pass for the
round-15 B4 candidate. This accumulated validation is sufficient to advance to the
distinct B4 acceptance review; it is not itself the acceptance or checkpoint.

The B1 rights-holder/counsel limitation remains controlling. Shim ownership,
historical MIT labeling, and combined-work treatment require counsel or rights-holder
confirmation before conveyance. No wheel, sdist, upload, publication, or conveyance
was performed.

Verdict: `pass`. `APPROVAL_NEEDED`: none.
