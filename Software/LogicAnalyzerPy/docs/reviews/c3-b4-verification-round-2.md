# C3-B4 public library and installed CLI verification, round 2

- Identity and role: `c3-b4-public-verifier-1`; fresh independent B4 verifier round
- Timestamp: `2026-09-01T10:59:27Z`
- Governing contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`
- Accepted B3 checkpoint: `233b3b0667add740cee96ce3c9ee266c8a639067`
- Failed round-1 evidence commit/tree: `fed87a058e88329790d460977df9ee8a04f83e44` /
  `8e7e829f6ea0bacf13d09cb0429123b8ffdb4406`
- Tested corrected candidate/tree: `bd1bd07c2501c0c28ed6ae494c4fa298571e058f` /
  `bd544dee2b19a44ee256e44f2f6afc2371142afd`
- Candidate branch/worktree: `python-rewrite`; candidate was clean. The qualified
  descendant worktree contains only this review and
  `tests/verification/test_c3_b4_public_round2.py`; neither changes product identity.
- Environment: macOS 15.7.9 build 24G830, x86_64, Python 3.12.13; stable clean
  environments `/private/tmp/cycle3-clean-core` and `/private/tmp/cycle3-clean-web`.
- Hosted CI: deliberately not launched. It remains an orchestrator-owned accumulated
  gate and cannot pass or transfer for a candidate whose independent verification fails.

## Independent method and authoritative expectations

This round reread the immutable correction and derived expectations from the approved
goal/orchestration/batch contract, discovery's exact public representation and CLI
taxonomy, B1 literal vectors/limits/project-license record, accepted B2/B3
manifests/reviews, and round-1 findings. It did not use decoder or corrected-candidate
output to generate expected bytes.

The new verifier module independently constructs all 12 B1 vectors using only public
classes, checks their literal canonical UTF-8 bytes, tests deep immutable record values,
probes both public and private prelaunch SPI ceilings, enumerates all stable diagnostic
codes at a tightened boundary, exercises semantic and syntactic CSV metadata errors,
and bounds hostile ASCII/Unicode argparse output. Round-1 evidence was not edited.

## Commands and exact results

- `python -m ruff check tests/verification/test_c3_b4_public_round2.py`: pass.
- Full round-2 verifier: `10 passed, 3 failed in 1.82s`. All three failures are the
  sample-rate/trigger-channel/edge instances of the single unresolved V003 taxonomy
  finding below; no test skipped.
- Passing round-2 subset: `10 passed, 3 deselected in 1.25s`.
- Corrected implementation, immutable round-1 verifier, existing CLI, and workflow
  checks: `41 passed in 5.05s`.
- Accepted B2 host and all eight B3 implementation/verification conformance modules:
  `734 passed in 102.49s`; no containment or decoder-conformance regression was found.
- Focused Ruff over corrected production/tests and the round-2 artifact: pass.
- Production mypy: `Success: no issues found in 31 source files`.
- Strict installed public consumer: `Success: no issues found in 1 source file`.
- Core and web `pip check`: `No broken requirements found` in both stable clean
  environments.
- Installed `pico-la decode --help`: the exact replay/CSV, capture metadata, decoder,
  mapping, and option arguments remained present.
- Strict accepted-manifest validation for `c3-b1.json`, `c3-b2.json`, and `c3-b3.json`:
  all exited 0.
- Installed core/web metadata: `License-Expression: GPL-3.0-only`, exact four
  `License-File` entries, numpy/pyserial base dependencies, and aiohttp conditional only
  on the web extra.
- Resource audit found exactly nine packaged snapshot files and reproduced every B1
  SHA-256; no extra resource or byte drift was present.
- Scoped dependency/import/command search found only accepted optional-web aiohttp
  declarations/guards and no active C#/.NET, pythonnet, `sigrok-cli`, or
  external/reference-host use. A transient local process-list observation failure was
  immediately retried with the same stable `rtk proxy pgrep` shape; the retry succeeded
  with no prohibited-process match.
- `git diff --check`: pass.

Unchanged identities were dev input/lock
`5cecd68793af3366c94bebd5379e040404704ba0dc4f4d4edaa54946d05ed4a8` /
`4efa0b1d42e5162c7a20177d1dd5e78083d75a87d2405709e04b1bcbd4f33c53`, web
input/lock `22673b4d490d16e2226c8789da848e7f2d2c8544c517d421b8c3ef6351b7a567` /
`4b0feeadf92c0bcb9f2790cc62f6b6e2f7da8937f30ff50d0c9092fd003b8145`, and
package metadata
`ead05ffbfab1c046b43087993d7dbd1056cdc9d6ebbb87d481092bacfb30a6cf`.

## Round-1 finding dispositions

1. **C3B4-V001 — resolved.** The three unlisted payload dataclasses are gone. Record
   value fields are closed copied mapping proxies with exact schema keys, immutable
   tuple arrays, canonical padded base64, validation, and no extension field. Source
   mapping mutation cannot affect a record. All 12 independently constructed public
   object vectors reproduce the accepted literal bytes.
2. **C3B4-V002 — resolved.** A tightened SPI word-size ceiling rejects before public
   delegation and before private identity verification/process creation. Diagnostic
   selections below the maximum stable message are rejected before delegation; every
   closed host code fits the accepted 28-byte tightened boundary. Full/partial limit
   plumbing retains every B1 hard ceiling and B2 isolation mechanism.
3. **C3B4-V003 — incomplete; changes still required.** Empty, malformed, duplicate,
   non-distinct, out-of-range, and header-count-mismatched `--channels` values now use
   input exit 5. However, syntactically invalid CSV `--sample-rate`,
   `--trigger-channel`, and `--edge` values are still converted/choice-checked by
   argparse before input classification and return exit 2. The settled discovery text
   requires duplicate, empty, out-of-range, mismatched-label, non-distinct, **or
   otherwise parser-invalid metadata** to fail as input/exit 5 before decoder mapping
   or worker launch. Required disposition: retain strings for all decode CSV metadata
   until the decode-input validator can classify them as exit 5, while preserving
   replay exclusion, normal grammar/configuration exit 2, validation order, bounded
   stderr, and no launch. Add installed black-box cases for all three fields.
4. **C3B4-V004 — resolved.** Hostile 20,000-character ASCII and Unicode decoder tokens
   each produce valid UTF-8 stderr no larger than the aggregate 8,192-byte ceiling,
   empty stdout, and exit 2. Handled diagnostic paths share the same reset budget.

## License, scope, and gate disposition

The exact package bytes, SPDX/PEP 639 metadata, attribution, and notices remain
consistent with the accepted engineering disposition. This is not a legal conclusion:
the shim's ownership/license, historical MIT label, and combined-work treatment still
require counsel or rights-holder confirmation before conveyance. No wheel, sdist,
upload, conveyance, publication, hardware, firmware, live capture, serial operation,
browser decoder behavior, dynamic decoder selection, `.lac`, B5 artifact, or Cycle 4
work was performed or authorized.

V003 is an exact B4 installed-CLI contract defect. This candidate cannot advance to
accumulated validation, hosted CI, acceptance, manifest creation, or checkpoint. A new
immutable correction candidate and fresh independent verification are required; no
round-2 pass transfers.

## Verdict

changes_required
