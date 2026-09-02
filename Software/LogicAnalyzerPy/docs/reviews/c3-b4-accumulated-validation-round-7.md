# C3-B4 accumulated validation, round 7

- Orchestrator role: root accumulated-validation and hosted-dispatch owner
- Timestamp: `2026-09-02T01:43:00Z`
- Governing B1 contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`
- Round-9 implementation candidate/tree: `3b8de59f8fc5276a92d5ea5fef5b48b259374a52` /
  `aee4e77238ce2dfd8d311b47873dfe3ebb21d4d6`
- Independently verified evidence commit/tree exercised by this gate:
  `903226e40bc98bddc6003247044837e253d60b24` /
  `137a04d65a8f9a0952a79707b5876a7a60b44fc0`
- Prior failed accumulated evidence commit: `5cc615044c0bcaac6f640e5decc74503025745f3`

## Exact local verification

Fresh independent round-9 verification passed under the accepted uv-managed CPython
3.12.13 environment. The accepted raw-B1 replacement verifier remained selected and
matched the full recorded `sys.version`. The focused inherited-SIGTERM command passed
its three exact cases. Candidate-qualified collection selected 1,448 of 1,469 cases
with exactly 21 deselected through 20 ordered unique selectors. The retained raw-B1,
workflow, and all relevant B2/B3/B4 sweep passed 830 cases with 20 deselected.

V001 through V004, the 1,300-byte diagnostic, full-history checkout, bytecode
suppression, Intel runner guard, product/static, frontend, resources, manifests,
locks, metadata, CLI, licenses, and process/import audits all passed. No governed
product or prior evidence byte drifted.

## Exact hosted setup failure

The exact evidence commit was pushed to dedicated branch
`cycle3-b4-ci-903226e`. GitHub Actions run
[`33580345130`](https://github.com/eparadis/pico2-logicanalyzer/actions/runs/33580345130),
job
[`100093114545`](https://github.com/eparadis/pico2-logicanalyzer/actions/runs/33580345130/job/100093114545),
resolved exact head `903226e40bc98bddc6003247044837e253d60b24` on the governed
`macos-15-intel` runner and concluded `failure`.

The architecture guard and full-history checkout passed. `actions/setup-python@v5`
then rejected the exact request before any repository Python command ran:

> The version '3.12.13' with architecture 'x64' was not found for macOS 15.7.9.

The action linked its versions manifest. All subsequent setup, product, Python,
frontend, asset, and browser steps were skipped by normal fail-fast behavior. This is
not a test or decoder failure, and no local pass is substituted for the missing hosted
execution.

The accepted B1 environment uses uv-managed
`cpython-3.12.13-macos-x86_64-none`, while setup-python's hosted macOS x64 inventory
does not provide that patch release. Therefore the evidence supports provisioning the
same managed 3.12.13 runtime through a pinned uv bootstrap; it does not support falling
back to 3.12.10, editing the accepted raw evidence, or ignoring its verifier.

Status and annotation polling used the saved read-only `rtk curl` class with files
under repository-ignored `.tmp/`, followed by separate local JSON parsing. No workflow
rerun, repeated approval class, artifact publication, or conveyance occurred.

## Disposition

Local verification passes, but the mandatory exact-candidate hosted gate cannot start
its Python validation because setup-python lacks CPython 3.12.13 for this runner. B4 is
not accepted. A bounded managed-runtime bootstrap correction, fresh independent
verification, accumulated validation, and exact-candidate hosted dispatch remain
required.

The B1 rights-holder/counsel limitation remains controlling. Shim ownership,
historical MIT labeling, and combined-work treatment require counsel or rights-holder
confirmation before conveyance. No wheel, sdist, upload, publication, or conveyance
was performed.

Verdict: `fail`. `APPROVAL_NEEDED`: none.
