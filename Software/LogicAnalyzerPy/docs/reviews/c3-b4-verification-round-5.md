# C3-B4 hosted pytest partition verification, round 5

- Identity and role: `c3-b4-public-verifier-1`; fresh independent B4 verifier round
- Timestamp: `2026-09-01T23:07:46Z`
- Governing contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`
- Accepted B3 checkpoint: `233b3b0667add740cee96ce3c9ee266c8a639067`
- Prior passing B4 candidate/tree: `afa015727a791e03071b6fb6607cdb1fd231727a` /
  `ea19d3e2e95071c06ee7bf9fbb152e9571f72ce0`
- Tested candidate/tree: `8cd114fa316f10db4d403197f3204771ccd36638` /
  `5b4c8f46ca626861a3191282aa5e2b282f806246`
- Candidate branch/worktree: `python-rewrite`; candidate was clean. The qualified
  descendant worktree contains only this review and
  `tests/verification/test_c3_b4_public_round5.py`; neither changes product identity.
- Environment: Darwin 24.6.0 x86_64, Python 3.12.13; stable clean environments
  `/private/tmp/cycle3-clean-core` and `/private/tmp/cycle3-clean-web`.
- Hosted CI: not launched by this verifier. Exact-candidate hosted execution remains an
  orchestrator-owned accumulated gate and is not claimed here.

## Independent method and exact partition

The fresh verifier parsed the workflow without importing its implementation regression,
bound the exact candidate/tree/workflow digest, independently enumerated candidate-tree
B2/B3/B4 modules, checked every ignored file and deselected node exists, compared the
workflow byte-for-byte to round 4 after restoring only the pytest invocation, and
executed the exact collection and retained-module partitions.

The hosted pytest invocation contains exactly the accepted 15 superseded-B1 ignores,
in this order and each once:

1. `tests/verification/test_c3_b1_threshold_proposal_round2.py`
2. `tests/verification/test_c3_b1_final_candidate.py`
3. `tests/verification/test_c3_b1_raw_baseline_candidate.py`
4. `tests/verification/test_c3_b1_runner_fixture_rebinding.py`
5. `tests/verification/test_c3_b1_semantic_fixture_candidate.py`
6. `tests/verification/test_c3_b1_threshold_proposal_round3.py`
7. `tests/verification/test_c3_b1_preexecution_runner_candidate.py`
8. `tests/verification/test_c3_b1_runner_fixture_rebinding_round4.py`
9. `tests/verification/test_c3_b1_final_candidate_round3.py`
10. `tests/verification/test_c3_b1_runner_fixture_rebinding_round5.py`
11. `tests/verification/test_c3_b1_semantic_fixture_correction_round2.py`
12. `tests/verification/test_c3_b1_runner_fixture_rebinding_round2.py`
13. `tests/verification/test_c3_b1_runner_fixture_rebinding_round3.py`
14. `tests/verification/test_c3_b1_threshold_proposal.py`
15. `tests/verification/test_c3_b1_semantic_fixture_correction.py`

It contains exactly these three ordered, unique and transparent deselections:

1. `tests/implementation/test_cycle3_fixtures.py::test_cycle3_fixture_surface_is_present_and_rebuildable`
2. `tests/verification/test_c3_b4_public_round4.py::test_candidate_binding_and_exact_workflow_digest`
3. `tests/verification/test_c3_b4_public_round4.py::test_hosted_correction_preserves_every_prior_workflow_byte_and_gate_order`

The first is the accepted frozen historical fixture surface. The other two bind the
previous candidate's exact workflow digest and exact round-4-only byte transformation;
they correctly become obsolete when the authorized partition changes those workflow
bytes. No behavior, security, product-scope, decoder, or public-API assertion is
deselected. The other three round-4 tests—official Intel label/guard ordering, actual
x86_64 acceptance plus simulated arm64 rejection, and product/fixture/limit/lock drift
exclusion—remain collected and passed.

The candidate tree contains exactly 18 current B2/B3/B4 implementation/verifier modules.
All exist, none is ignored, and only the two named nodes within the round-4 verifier are
deselected. Candidate-qualified collection produced exactly
`1429/1432 tests collected (3 deselected) in 0.63s`. Collection in the descendant
verification worktree additionally included this seven-test round-5 module and produced
`1436/1439 tests collected (3 deselected) in 2.61s`.

## Commands and exact results

- Fresh round-5 verifier:
  `python -m pytest -q tests/verification/test_c3_b4_public_round5.py` —
  `7 passed in 0.12s`; no skip.
- Explicit fixture/workflow plus every current B2/B3/B4 module, the complete round-4
  file, and the fresh round-5 verifier under the exact three deselections:
  `819 passed, 3 deselected in 112.19s`; no skip. This proves every retained module and
  all remaining round-4 behavior/scope nodes are green.
- Prior C3B4-V001 through V004 checks all passed within that sweep: exact immutable
  class/value surface and 12 typed vectors; public/private tightening and bounds;
  CSV exit 5 versus replay exit 2 before read/mapping/launch; and aggregate bounded
  UTF-8 diagnostics.
- Focused Ruff over decode, private host, CLI, workflow/B4 implementation, and all five
  B4 verifier rounds: pass.
- Production mypy: `Success: no issues found in 31 source files`.
- Strict installed public consumer: `Success: no issues found in 1 source file`.
- Stable clean core and web `pip check`: `No broken requirements found` in both.
- Strict accepted-manifest validation for `c3-b1.json`, `c3-b2.json`, and `c3-b3.json`:
  all exited 0 without output.
- Installed outside-source `pico-la decode --help`: exact replay/CSV grammar,
  metadata/channel/option spelling, and UART/SPI/I2C decoder choices retained.
- Resource checks reproduced exactly the accepted nine decoder snapshot files and all
  B1 SHA-256 values, with no extra resource or root escape.
- Prohibited-process audit returned no active .NET, pythonnet, `sigrok-cli`, or external
  libsigrokdecode process. Scoped source/workflow search returned no prohibited import,
  dependency, or command; only the accepted optional-web aiohttp declaration/guard
  remains.
- `git diff --check`: pass.

The workflow SHA-256 is
`5c6b9cb1904d2096592bfc13e3854df24ddf84cba921df320556555b457eacff`.
After replacing the multiline governed partition with the prior one-line pytest
invocation, the complete workflow equals round 4 byte-for-byte. Thus
`macos-15-intel`, the first pre-checkout `uname -m`/exact `x86_64` guard, sanitizer,
failure annotation, all actions, versions, install gates, CLI/web/frontend/browser
checks, and their ordering remain unchanged.

The correction-relative path audit found only the workflow, its regression, and
descendant B4 evidence. No product, fixture, limit, threshold, dependency, lock,
manifest, or contract changed. Preserved SHA-256 identities include public decode
`d5cd8b84...19db`, private host `b81d3c1b...15b6`, CLI `c3acce49...3ddc`, typed vectors
`b5cc317f...fbf`, round-4 thresholds `98e48bb1...e3c`, option matrix
`5d84b9d9...209`, dev lock `4efa0b1d...53`, web lock `4b0feead...45`, and package
metadata `ead05ffb...cf`.

Installed core/web metadata remains `License-Expression: GPL-3.0-only`, with exact
`LICENSE`, `LICENSES/GPL-2.0-or-later.txt`, `LICENSES/MIT.txt`, and `ATTRIBUTION.md`
license-file entries. Base dependencies remain numpy/pyserial and aiohttp remains
conditional only on the web extra. Exact license/attribution digests are unchanged.

## Findings and dispositions

1. **Hosted partition — verified.** The 15 accepted ignores and three accepted
   deselections are exact, ordered, unique, and effective at collection. No current
   B2/B3/B4 module is ignored; only the two explicitly superseded round-4 candidate-byte
   nodes are deselected.
2. **C3B4-V001 through V004 — remain resolved.** All prior behavior, canonical bytes,
   validation ordering, limit enforcement, exit taxonomy, installed CLI/API, and
   diagnostic bounds pass unchanged.
3. **Hosted runner correction — preserved.** The official `macos-15-intel` selection
   and fail-fast pre-checkout x86_64 guard remain exact, as do all other workflow gates.
4. **Scope and identity — preserved.** No product, fixture, threshold, limit, manifest,
   dependency, or lock drift and no new finding was identified.

## License, scope, and gate disposition

Exact package bytes, PEP 639 metadata, attribution, and notices remain consistent with
the accepted engineering disposition. This is not a legal conclusion: shim ownership,
the historical MIT label, and combined-work treatment still require counsel or
rights-holder confirmation before conveyance. This verifier built no wheel or sdist and
performed no upload, conveyance, publication, hardware, firmware, serial, live capture,
or hosted CI dispatch.

The candidate is eligible for the orchestrator's accumulated gate and exact-candidate
hosted macOS dispatch. This verifier does not claim those future results, final
acceptance, manifest readiness, or checkpoint completion.

## Verdict

pass
