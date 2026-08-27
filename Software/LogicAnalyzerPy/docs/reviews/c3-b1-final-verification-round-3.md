# C3-B1 final candidate verification — round 3

## Identity, correction context, and immutable subject

- Verifier: `c3-b1-final-verifier-2`
  (`/root/c3_b1_final_verify_fresh`). This fresh primary verification identity
  is distinct from the orchestrator, all six internal C3-B1 evidence roles,
  fresh final acceptance, and manifest verification.
- Corrected candidate commit/tree:
  `1f8793210a3298ed190ff30f97c84b6f9feb9b29` /
  `cbe33ca272ba1b452f6d87fb5e702134a471f702`.
- Fresh-verification assignment commit:
  `6ac1396dcbc12ed3076f4ddf9d6850c18814518e`.
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Binder SHA-256:
  `55983bbe9613c0deb0fe7f05a2e88b680b9cfed352f4cccfae9cdd01ca744adf`.
- Rationale SHA-256:
  `9577c4b268af5a4a8c6b7f59f934e8ba689a23d4bda66aa0e8662533acd82396`.

Finding `C3B1-MP001` invalidated the former primary verification and acceptance
identity separation because those records reused internal runner identities.
It did not alter this candidate or any accepted internal evidence. No former
primary-verifier pass transfers here: this record repeats the complete final
static verification under a fresh identity. A pass authorizes only a fresh
complete accumulated gate; fresh acceptance, manifest verification, manifest
commit, checkpoint, and B2 remain ordered later gates.

## Independent subject, identity, and correction audit

The candidate commit adds exactly the assigned round-2 binder JSON and
rationale. Its tree resolves exactly, both current paths are byte-identical to
their candidate-commit blobs, and the status remains
`candidate-not-accepted`. Schema, round, macOS-only support scope, exact
Python 3.12.13 / Node 22.14.0 / Chromium 133.0.6943.16 / Playwright 1.50.1
environment, governing identities, and next gate are exact.

All six final internal roles are present and pairwise distinct. The semantic
fixture implementation history explicitly and completely orders the original
identity followed by replacements 1 through 6, with replacement 6 as its
tail/final owner. The runner implementation history orders the original
identity followed by replacements 1 through 3, with replacement 3 as its
tail/final owner. This fresh verifier is not any of those identities.

The correction binds `C3B1-FV001`, the superseded candidate and assignment,
the failed-verification assignment and commit, and the enumeration-only
correction scope. After removing round-2 correction metadata, restoring the
round-1 governing block, and normalizing the two explicit ordered histories to
the former preservation booleans, the round-2 binder equals round 1 exactly.
No evidence, command, environment, finding, applicability, exclusion, status,
or authority meaning changed.

## Evidence, approved limits, and ordering

All 32 live artifact SHA-256 values independently recompute and match. The
five evidence groups bind the project/license disposition; corrected semantic
fixture candidate and its verification, accumulated validation, and
acceptance; corrected pre-execution runner and its three gates; raw baseline
and its three gates; and threshold proposal, verification, accumulated
validation, acceptance, and operator decision. Every referenced commit is
reachable, and the fixture, runner, raw, and proposal candidate commits resolve
to their exact bound trees. The historical invalidations and findings
`C3B1-RI011`, `C3B1-RI013`, and `C3B1-TPV001` remain preserved and closed in
the required order.

The exact operator-approved proposal contains 29 unique limits. For every
entry, `accept` equals the approved inclusive value and `reject` is exactly
value plus one. In particular, `successful_parent_total_ns` is exactly
900,000,000 accepted and 900,000,001 first rejected, and
`spi_max_word_size_bits` is exactly 8 accepted and 9 first rejected. The
approval commit and record digest are exact; no value is weakened, increased,
rebased, or inferred.

The project/license review remains an engineering disposition, not legal
advice. Its exact nine-file provenance and future packaging requirements are
bound, including the absent shim notice, mandatory rights-holder/counsel
confirmation before conveyance, and the prohibition on packaging or
distribution at this gate.

## Commands, applicability, negative checks, and exclusions

All 21 frozen command records have unique identities, exact working
directories and argument vectors, and retain their required Python 3.12 or
Node 22 qualification. The applicability record remains exactly 637 selected
at its bound stage plus three transparent historical deselections; the frozen
pytest vector names those same three nodes. The later accumulated inventory is
not transferred into this static pass and must be repeated after it.

The existing static verifier completed with 20 tests passed, and Ruff passed.
Before each of 17 mutations the unmodified binder passed validation; missing
or extra material and altered evidence, roles, digests, commits, status,
environment, commands, limit count, approval, findings, applicability,
exclusions, histories, correction provenance, or governing identity were each
rejected. This is a non-vacuous mutation matrix.

Exact candidate scope, immutable tree, candidate-path quiet diff, digest
recomputation, reachability/tree resolution, normalized correction-only
equivalence, and `git diff --check` passed. The root-brokered read-only process
audit found no pytest, Playwright, Vite, Cycle 3 characterization, tools-cycle3,
product web, or `server.main` process. No prohibited worker remains.

The six exclusions remain exact: no product decoder host/public decode API,
external decoder runtime or C#/.NET/pythonnet/libsigrokdecode/`sigrok-cli`,
hardware/USB/serial/firmware, wheel/sdist/upload/publication/distribution,
non-macOS support claim, or Cycle 4 authority. There is also no manifest,
checkpoint, or B2 authority.

All shell commands used RTK. Inspection and checks were static only. No
snapshot, decoder, characterization runner, hostile probe, product host,
browser server, hardware, network, install, package build/publication, B2, or
Cycle 4 action ran. No candidate, prior record, or verifier test was modified,
and no commit was created.

## Verdict

`pass`
