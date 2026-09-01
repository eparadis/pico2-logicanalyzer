# C3-B4 public library and installed CLI verification, round 3

- Identity and role: `c3-b4-public-verifier-1`; fresh independent B4 verifier round
- Timestamp: `2026-09-01T11:09:18Z`
- Governing contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`
- Accepted B3 checkpoint: `233b3b0667add740cee96ce3c9ee266c8a639067`
- Failed round-2 evidence commit/tree: `c01015e8439020cf87c042f11906912b8cefa947` /
  `6d8329f99a093e3014c093cbbff3761206e49c52`
- Tested candidate/tree: `e93b0d85bb57c014979c648373e48af845e7b01f` /
  `fa428dd9a43bba52eb6dd7ce345fde883dc88af8`
- Candidate branch/worktree: `python-rewrite`; candidate was clean. The qualified
  descendant worktree contains only this review and
  `tests/verification/test_c3_b4_public_round3.py`; neither changes product identity.
- Environment: macOS 15.7.9 build 24G830, x86_64, Python 3.12.13; stable clean
  environments `/private/tmp/cycle3-clean-core` and `/private/tmp/cycle3-clean-web`.
- Hosted CI: not launched by this verifier. Exact-candidate hosted macOS CI remains a
  mandatory orchestrator-owned accumulated gate after this independent pass.

## Independent method

This round derived expectations from the approved goal/orchestration/batch contract,
discovery's exact R17-R20 public representation and CLI taxonomy, accepted B1 literal
vectors/limits/project-license disposition, accepted B2/B3 manifests and reviews, both
prior verifier records, and the immutable correction. Expected bytes and classifications
were not generated from decoder or candidate output.

The new verifier directly instrumented capture-read, mapping-parse, and public-host
seams for each malformed CSV/replay sample-rate, trigger-channel, and edge case. It also
retested syntactically valid but forbidden replay metadata, the exact immutable public
record-value surface, caller SPI/diagnostic tightening, aggregate ASCII/Unicode
diagnostic bounds, the exact nine resources, and serial/aiohttp import exclusion.

## Commands and exact results

- `python -m ruff check tests/verification/test_c3_b4_public_round3.py`: pass.
- Fresh round-3 verifier: `14 passed in 0.82s`; no skip.
- B4 implementation, all three immutable verifier rounds, existing CLI tests, and
  workflow regression: `71 passed in 8.48s`; no skip.
- Accepted B2 private-host and all eight B3 implementation/verification conformance
  modules: `734 passed in 101.82s`; no inherited containment or decoder-conformance
  regression.
- Focused Ruff over the public model, private host, CLI, implementation tests, and all
  three verifier modules: pass.
- Production mypy: `Success: no issues found in 31 source files`.
- Strict installed public consumer: `Success: no issues found in 1 source file`.
- Stable clean core and web `pip check`: `No broken requirements found` in both.
- Installed `pico-la decode --help`: exact replay/CSV grammar and metavariables retained.
- Strict accepted-manifest validation for `c3-b1.json`, `c3-b2.json`, and `c3-b3.json`:
  all exited 0.
- Installed core/web metadata: `License-Expression: GPL-3.0-only`; exact four
  `License-File` entries; base numpy/pyserial requirements; aiohttp conditional only on
  the web extra. Installed license hashes remained attribution
  `3765302c...ac1e`, GPLv3 `3972dc97...6986`, GPLv2+
  `ab15fd52...6c6`, and MIT `6115c1f0...52f6`.
- Resource audit found exactly the accepted nine package snapshot files and reproduced
  every B1 SHA-256 with no extra file or byte drift.
- Scoped dependency/import/command search found only accepted optional-web aiohttp
  declarations/guards and no active C#/.NET, pythonnet, `sigrok-cli`, or external host.
  An initial local process-list observation transiently failed; immediate retry with the
  same stable `rtk proxy pgrep` shape succeeded with no prohibited-process match.
- `git diff --check`: pass.

The unchanged lock/package identities were dev input/lock
`5cecd68793af3366c94bebd5379e040404704ba0dc4f4d4edaa54946d05ed4a8` /
`4efa0b1d42e5162c7a20177d1dd5e78083d75a87d2405709e04b1bcbd4f33c53`, web
input/lock `22673b4d490d16e2226c8789da848e7f2d2c8544c517d421b8c3ef6351b7a567` /
`4b0feeadf92c0bcb9f2790cc62f6b6e2f7da8937f30ff50d0c9092fd003b8145`, and
package metadata
`ead05ffbfab1c046b43087993d7dbd1056cdc9d6ebbb87d481092bacfb30a6cf`.
The corrected CLI SHA-256 was
`c3acce4965faeff55c6177dfdfff840d7a2b9c65a6ae4b05b45f26974f1d3ddc`.

## Findings and dispositions

1. **C3B4-V001 — resolved.** The normative class set remains exact; annotation,
   binary, and metadata values are closed copied immutable mappings rather than
   unlisted payload models. All 12 independently public-constructed B1 objects and
   literal canonical bytes pass in immutable round 2.
2. **C3B4-V002 — resolved.** Tightened SPI maximum rejects before both public and
   private launch seams. Impossible diagnostic tightening rejects before delegation;
   every stable failure remains within an accepted tightened boundary. No approved
   ceiling or B2 security mechanism was weakened or disabled.
3. **C3B4-V003 — resolved.** Malformed CSV sample-rate, trigger-channel, and edge each
   return input exit 5, bounded stderr, and empty stdout before capture read, mapping
   parse, or host launch. The same malformed tokens with replay return usage exit 2 at
   the same pre-read/prelaunch boundary. Syntactically valid CSV metadata supplied with
   replay remains forbidden input and returns exit 5 before read. Empty, malformed,
   duplicate, non-distinct, out-of-range, and header-count-mismatched channel metadata
   remains exit 5. Existing replay/CSV success equivalence, explicit-metadata
   precedence/identity, and legacy-only D0-D7 rate inference continue to pass.
4. **C3B4-V004 — resolved.** Aggregate stderr remains at or below 8,192 bytes for
   hostile 20,000-character ASCII and Unicode argparse inputs, with valid UTF-8, empty
   stdout, and exit 2. Stable input and decoder diagnostic paths remain bounded.

No new finding was identified. The public API retains one synchronous delegation and
canonical version-1 shape; all literal bytes, error codes, no-live-capture behavior,
resource identities, optional-web separation, and inherited Cycle 1/2/B1-B3 behavior
covered by this proportional gate pass.

## License, scope, and gate disposition

Exact package bytes, PEP 639 metadata, attribution, and notices remain consistent with
the accepted engineering disposition. This is not a legal conclusion: the shim's
ownership/license, historical MIT label, and combined-work treatment still require
counsel or rights-holder confirmation before conveyance. This verifier built no wheel
or sdist and performed no upload, conveyance, publication, hardware, firmware, serial,
live capture, browser decoder behavior, dynamic selection, `.lac`, B5, or Cycle 4 work.

The candidate is eligible for the orchestrator's complete accumulated gate and
exact-candidate hosted macOS CI. This verifier does not claim those future results,
acceptance, manifest readiness, or checkpoint completion.

## Verdict

pass
