# C3-B4 public library and installed CLI verification, round 1

- Identity and role: `c3-b4-public-verifier-1`; independent B4 verifier
- Timestamp: `2026-09-01T10:38:02Z`
- Governing contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`
- Accepted B3 checkpoint: `233b3b0667add740cee96ce3c9ee266c8a639067`
- Tested immutable candidate/tree: `ce34d7972305aee1af0c7c0691b28adee3b13ca9` /
  `4e6d493edcf9fbc6abe10f04c18834b9d4e0736b`
- Candidate branch and worktree: `python-rewrite`; candidate was clean before
  verification. The qualified descendant worktree contains only this review and
  `tests/verification/test_c3_b4_public_round1.py`; neither changes product identity.
- Environment: macOS 15.7.9 build 24G830, x86_64, Python 3.12.13; stable clean
  environments `/private/tmp/cycle3-clean-core` and `/private/tmp/cycle3-clean-web`.
- Hosted CI: not run by this identity. Exact-candidate hosted macOS CI is an
  orchestrator-owned accumulated gate and must not be dispatched for this failed
  verification candidate as though it could transfer to a correction.

## Authority and independent expectations

The review used the approved goal/orchestration/batch contracts, the settled R17-R20
public representation/CLI/license sections, accepted B1 typed vectors and literal
goldens, round-4 limits and project/license disposition, accepted B2/B3 manifests and
reviews, and the candidate implementation record. Expected bytes came from the
accepted literal vectors, not decoder or candidate output. Static and black-box checks
were derived independently of the implementation tests.

The critical expectations were: the exact closed immutable public model set; one
synchronous delegation; complete and partial caller tightening without a weakened or
ignored selected ceiling; input metadata validation before mapping/launch with exit 5;
bounded stderr; canonical JSON plus one LF; byte-equal replay/explicit-CSV behavior;
exact nine resources; optional-web/serial isolation; PEP 639 metadata with the accepted
legal limitation; and preservation of B1-B3 behavior.

## Commands and results

- `python -m ruff check tests/verification/test_c3_b4_public_round1.py`: pass.
- Full independent verifier module from `/private/tmp`: `5 passed, 5 failed in
  1.51s`. The five failures reproduce findings V001-V004 below; no required test was
  skipped.
- Passing subset of that module: `5 passed, 5 deselected in 1.19s`. It bound the exact
  candidate/tree and B1 vector digest, independently reproduced all 12 literal JSON
  golden bytes, verified all nine resource bytes/digests, checked PEP 639 source
  metadata and legal caveat, proved external installed replay/CSV byte equality, and
  exercised decode with serial/aiohttp imports forbidden.
- Candidate B4 implementation, existing CLI, and workflow checks: `22 passed in
  3.19s`.
- Accepted B2 host plus all eight accepted B3 implementation/verification modules:
  `734 passed in 120.80s`; no inherited containment or decoder-conformance regression
  was found.
- Strict installed consumer: `Success: no issues found in 1 source file`.
- Production mypy from the project root: `Success: no issues found in 31 source files`.
- Core and web `pip check`: `No broken requirements found` in both environments.
- Installed `pico-la decode --help`: exact replay/CSV, decoder, channel, option, and CSV
  metadata arguments present.
- Strict Cycle 3 evidence validation for accepted `c3-b1.json`, `c3-b2.json`, and
  `c3-b3.json`: all exited 0.
- Core/web installed metadata inspection: `License-Expression: GPL-3.0-only`; exact
  four `License-File` entries; base requirements only numpy/pyserial with aiohttp
  conditional on the web extra. Installed license-resource SHA-256 values were
  `3765302c...ac1e`, `3972dc97...6986`, `ab15fd52...6c6`, and
  `6115c1f0...52f6`.
- Scoped dependency/import/command audit found no active C#/.NET, pythonnet,
  `sigrok-cli`, or external/reference-host use. Snapshot occurrences of the historical
  `libsigrokdecode` project name were inert retained notices. `rtk proxy pgrep` found
  no process matching `dotnet|sigrok-cli|libsigrokdecode|pythonnet`.
- `git diff --check`: pass.

Lock identities were dev input/lock
`5cecd68793af3366c94bebd5379e040404704ba0dc4f4d4edaa54946d05ed4a8` /
`4efa0b1d42e5162c7a20177d1dd5e78083d75a87d2405709e04b1bcbd4f33c53` and web
input/lock `22673b4d490d16e2226c8789da848e7f2d2c8544c517d421b8c3ef6351b7a567` /
`4b0feeadf92c0bcb9f2790cc62f6b6e2f7da8937f30ff50d0c9092fd003b8145`.
The public module SHA-256 was
`dafe3d4db7289adf57c299f4e8a2ade480addf3f7a624551ddc9779845eeba8c`.

## Findings and required dispositions

1. **C3B4-V001 — unlisted payload models leak through the exact public class set.**
   `AnnotationRecord.value`, `BinaryRecord.value`, and `MetadataRecord.value` are
   annotated and materialized as `_AnnotationPayload`, `_BinaryPayload`, and
   `_MetadataPayload`. These are additional immutable model classes absent from the
   normative exact class set, yet they are unavoidable types in public record fields.
   The candidate's B1-vector test reaches them through private
   `decode_result_from_dict()` and `_public_result()` rather than constructing an exact
   public object vector. Required disposition: represent these three schema values
   without an unlisted public-signature model, retain immutable exact fields, and rerun
   all 12 literal object/byte vectors plus strict external consumer checks.

2. **C3B4-V002 — two accepted caller tightenings are not enforced.** A partial
   `{"spi_max_word_size_bits": 4}` selection with SPI `wordsize=8` delegates to the
   host instead of rejecting before launch. A partial `{"diagnostic_bytes": 1}`
   selection returns the 23-byte `decoder failed: timeout` diagnostic. The public
   validator accepts both selections and the host has no effective-limit check for
   either path. Required disposition: enforce every accepted partial/full selected
   ceiling in its parent/worker/failure path, reject impossible selections before
   launch where needed, and add boundary/overrun/recovery checks without weakening B1's
   approved ceilings or B2 isolation.

3. **C3B4-V003 — empty CSV metadata has the wrong failure category.** Installed CLI
   `--channels ''` on a valid CSV returns exit 2 because `_channel_ids()` raises
   `ValueError`. The settled contract classifies empty and otherwise parser-invalid CSV
   metadata as input validation, exit 5, before decoder mapping or launch. Required
   disposition: keep the validation order but route all invalid CSV metadata through
   the input/exit-5 taxonomy; cover empty, malformed, duplicate, non-distinct,
   out-of-range, and mismatched-label cases independently.

4. **C3B4-V004 — argparse usage diagnostics are not bounded.** An invalid decoder
   token of 8,193 bytes produces 8,622 stderr bytes, exceeding the approved 8,192-byte
   diagnostic ceiling. Standard argparse includes caller-controlled values without a
   bounding layer. Required disposition: bound every usage/configuration/input/decoder
   stderr path while preserving no stdout on failure and exact exits 2/5/7.

The PEP 639 expression, exact staged/installed resources, attribution table, shim
caveat, and no-publication statement match the accepted engineering disposition. This
is not a legal conclusion: shim ownership/license, the historical MIT label, and
combined-work treatment still require counsel/rights-holder confirmation before any
conveyance; no wheel, sdist, upload, or publication was performed or authorized here.

## Scope and gate disposition

No browser/API/frontend decoder behavior, hardware, firmware, serial/live capture,
dynamic decoder selection, stacking, `.lac`, export, publication, unsupported-platform
claim, B5 artifact, or Cycle 4 work was observed. The exact decoder behavior continues
to pass its inherited suites. The defects are earliest-owned B4 public-interface
defects, so this candidate cannot proceed to accumulated validation, hosted CI,
acceptance, manifest creation, or checkpoint.

## Verdict

changes_required
