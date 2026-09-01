# C3-B4 public library and hosted correction verification, round 4

- Identity and role: `c3-b4-public-verifier-1`; fresh independent B4 verifier round
- Timestamp: `2026-09-01T22:37:36Z`
- Governing contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`
- Accepted B3 checkpoint: `233b3b0667add740cee96ce3c9ee266c8a639067`
- Prior passing B4 product candidate/tree: `e93b0d85bb57c014979c648373e48af845e7b01f` /
  `fa428dd9a43bba52eb6dd7ce345fde883dc88af8`
- Tested candidate/tree: `afa015727a791e03071b6fb6607cdb1fd231727a` /
  `ea19d3e2e95071c06ee7bf9fbb152e9571f72ce0`
- Candidate branch/worktree: `python-rewrite`; candidate was clean. The qualified
  descendant worktree contains only this review and
  `tests/verification/test_c3_b4_public_round4.py`; neither changes product identity.
- Environment: Darwin 24.6.0 x86_64, Python 3.12.13; stable clean environments
  `/private/tmp/cycle3-clean-core` and `/private/tmp/cycle3-clean-web`.
- Hosted CI: not launched by this verifier. Exact-candidate hosted execution remains an
  orchestrator-owned accumulated gate and is not inferred from structural verification.

## Independent method and official runner evidence

The verifier bound the exact commit and tree, independently compared the workflow to
the prior passing product candidate, executed both branches of the architecture guard,
and reran all prior V001-V004 checks plus proportional B2/B3/B4 regression and static,
manifest, resource, lock, metadata, and process audits.

As retrieved on 2026-09-01, GitHub's official
[`actions/runner-images` inventory](https://github.com/actions/runner-images/blob/main/README.md)
maps macOS 15 x64 to `macos-15-large` or `macos-15-intel`, and distinguishes it
from macOS 15 arm64. GitHub's official
[`macos-15-intel` announcement](https://github.com/actions/runner-images/issues/13045)
also identifies that label as the macOS 15 x86_64 image. Therefore the candidate's
explicit `macos-15-intel` selection is an official current x64 mapping rather than a
moving architecture alias.

The job's first step is exactly `Verify governed macOS x86_64 runner`. It invokes
`uname -m`, accepts only `x86_64`, and precedes checkout, Python/Node setup, virtual
environment creation, dependency installation, and every product gate. A simulated
`arm64` result emitted only
`unsupported runner architecture: arm64 (required: x86_64)` on stderr and exited 2;
the verification host's actual x86_64 result exited 0 with empty stdout and stderr.

After replacing only `macos-15-intel` with the prior `macos-latest` label and removing
the new guard block, the workflow reproduced the prior candidate byte for byte. Its
ordered `name`/`uses` step sequence likewise reproduced every prior gate with only the
guard prepended. Triggers, permissions, action pins, language versions, hash-locked
core/web installs, Ruff, mypy, strict consumer, pytest/sanitizer, CLI, frontend, asset,
Playwright, and browser gates are preserved in their prior order.

## Commands and exact results

- Fresh round-4 verifier:
  `python -m pytest -q tests/verification/test_c3_b4_public_round4.py` —
  `5 passed in 0.33s`; no skip.
- B4 implementation, workflow, all four immutable verifier rounds, and CLI regression:
  `76 passed in 8.87s`; no skip. This rechecks every C3B4-V001 through V004 subcase,
  including malformed CSV metadata exit 5 versus replay exit 2 before read, mapping,
  or launch.
- Accepted B2 implementation and all eight B3 implementation/verification conformance
  modules: `653 passed in 85.35s`. All four immutable B2 verifier rounds:
  `81 passed in 15.95s`. Aggregate proportional B2/B3 result: `734 passed`; no skip.
- Focused Ruff over decode, private host, CLI, B4 implementation/workflow, and all four
  verifier modules: pass.
- Production mypy: `Success: no issues found in 31 source files`.
- Strict installed public consumer: `Success: no issues found in 1 source file`.
- Stable clean core and web `pip check`: `No broken requirements found` in both.
- Strict accepted-manifest validation for `c3-b1.json`, `c3-b2.json`, and `c3-b3.json`:
  all exited 0 without output.
- Installed outside-source `pico-la decode --help`: exact mutually exclusive replay/CSV
  grammar, decoder choices, channel/option spelling, and metadata metavariables retained.
- Prohibited-process audit found no active .NET, pythonnet, `sigrok-cli`, or external
  libsigrokdecode host. Scoped search found only the accepted bundled snapshot license
  notices and optional-web aiohttp declarations/guards; no prohibited dependency,
  import, or external decode command was introduced.
- `git diff --check`: pass.

The exact workflow SHA-256 is
`3df72bff1cde7fdd8619bc74e1f796d9f3d755a5e35a4d4ef2070327fa602f0e`.
The correction-relative path audit found only the workflow, its workflow regression,
and descendant review/verifier evidence; no `src`, decoder testdata, fixture,
`pyproject.toml`, dependency input, lock, or web lockfile changed.

Preserved product identities include public decode
`d5cd8b843bf2bd847dc42a7fa550d5756615177d77e80912472d088b9e6519db`, private host
`b81d3c1b4ded37bc665cb074d81de0620b6030435aae4b1ce0122a69c56315b6`, CLI
`c3acce4965faeff55c6177dfdfff840d7a2b9c65a6ae4b05b45f26974f1d3ddc`, typed vectors
`b5cc317ff476fcb2446eaf6b376c346210f63fbca8d0df84984b7990a528ffbf`, round-4
thresholds `98e48bb1882104d893a1d4d85659845ff20054f9b52f0b09fdf73efad2547e3c`, and option
matrix `5d84b9d9855e9e2e75d45d5cd9560fbcfd1ac6ff88abfcf1c1326d3427ffc209`.
Dev input/lock remain `5cecd687...a8` / `4efa0b1d...53`; web input/lock remain
`22673b4d...67` / `4b0feead...45`; package metadata remains `ead05ffb...cf`.

The exact nine accepted snapshot resources and every B1 resource digest passed again.
Installed core/web metadata remains `License-Expression: GPL-3.0-only`, with exact
`LICENSE`, `LICENSES/GPL-2.0-or-later.txt`, `LICENSES/MIT.txt`, and `ATTRIBUTION.md`
license-file entries. Base requirements remain numpy/pyserial and aiohttp remains
conditional only on the web extra. License/attribution hashes remain GPLv3
`3972dc97...986`, GPLv2+ `ab15fd52...6c6`, MIT `6115c1f0...2f6`, and attribution
`3765302c...c1e`.

## Findings and dispositions

1. **C3B4-V001 — remains resolved.** The exact immutable public class set, field/type
   surface, all 12 typed objects, literal canonical bytes, and closed copied record
   mappings pass unchanged. No unlisted payload class or extension field appeared.
2. **C3B4-V002 — remains resolved.** SPI and diagnostic tightening still fails before
   launch where required and remains enforced through parent/worker paths without
   weakening B2 containment or accepted decoder behavior.
3. **C3B4-V003 — remains resolved.** CSV malformed sample-rate, trigger-channel, and
   edge return exit 5; the same replay tokens return exit 2. Both classifications occur
   before read, mapping, or launch. Valid-but-forbidden replay metadata, duplicates,
   unknown/invalid values, precedence, identity, legacy-only inference, exclusion, and
   replay/CSV equivalence continue to pass.
4. **C3B4-V004 — remains resolved.** Aggregate ASCII/Unicode diagnostics remain valid
   UTF-8 and at or below 8,192 bytes with exact stdout/stderr and exit categorization.
5. **Hosted correction — verified structurally.** The current official Intel runner
   label, fail-fast x86_64 guard, and exact preservation/order of all existing gates
   pass. No product drift or new finding was identified. An actual hosted result is not
   claimed until the root-owned exact-candidate dispatch completes.

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
