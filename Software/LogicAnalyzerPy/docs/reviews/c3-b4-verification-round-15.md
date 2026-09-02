# C3-B4 hosted portability verification, round 15

- Identity: `c3-b4-public-verifier-1`; independent bounded B4 round 15.
- Timestamp: `2026-09-02T09:02:11Z`.
- Governing B1 commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Failed hosted predecessor: run `33608601566`, job `100178223085`, verifier
  `082f27ead5972f7b021728164d51e8e9d9c6ba44`.
- Tested candidate/tree: `921f8984b45d78d544494733c9fcd043a788f866` /
  `0b0ea4529e6c2279cdd5b6b766377ea5e75a73e7`.
- Exact unchanged workflow SHA-256:
  `12ff6bb2cd7e437b733f3aaeb9488c6926604572419468c60604f0dea1c6a990`.
- Scratch stayed below ignored repository `.tmp/c3-b4-ci`; no archive collection
  directory leaked. The preserved ignored round-13 draft was restored byte-identically
  at SHA-256 `a2144b144b1bc9814538a6b99527ff3888f3bfa3b1f7e22fca840e10e36b0ab8`.

## Artifact environment portability

Round 12 now prefers the actual complete `PICO_LA_PYTHON_ARCHIVE` and
`PICO_LA_PYTHON` environment pair and forwards those paths unchanged to the round-11
byte/runtime validator. An independently supplied complete hosted-style pair beneath
ignored repository scratch passed. In the normal local environment, where both are
absent, the existing local fallback passed. Archive-only and Python-only states each
failed before nested validation and were never classified as skips.

The committed fresh verifier is hosted-safe: it obtains the complete workflow pair
when available, otherwise uses the local fallback only when both variables are absent.
It does not bake verifier-private machine paths into the hosted-present assertion.

## Descendant and immutable collection portability

The ignored round-13 draft directory was temporarily renamed out of its expected
location without deletion. With it unavailable, round 14's tracked descendant proof
passed; it uses tracked `test_c3_b4_public_round14.py`, proves that file is absent from
immutable c765, and contains no `.tmp` or draft dependency. The draft was then restored
unchanged.

Round 12 again archived immutable c765 with safe relative/root/no-`..` member checks,
tar `filter="data"`, extracted cwd/PYTHONPATH/TMPDIR, and `finally` cleanup. Its exact
result remained `1459/1497 tests collected (38 deselected)`. Round 14's immutable 423
proof also passed. The fresh verifier independently archived exact candidate 921f898,
using the same safety and cleanup properties, and obtained exactly
`1479/1517 tests collected (38 deselected)`. Committing descendant verifier evidence
cannot perturb any of these immutable counts.

One exploratory parallel invocation ran two c765 archive checks simultaneously; the
round-14 before/after set assertion observed the other test's temporary directory and
reported a mismatch after that directory was correctly removed. The governed workflow
is serial. The exact node rerun serially passed and left no directory, and the complete
retained serial sweep passed. This was an orchestration race, not a candidate finding.

## Commands and retained behavior

- Fresh verifier: `7 passed in 11.66s`; final Ruff passed after one verifier-only line
  wrap.
- Workflow, full pre-execution runner, all current B2/B3/B4 modules, retained B4
  rounds, and fresh verifier: `1034 passed, 1 skipped, 37 deselected in 151.76s`.
  Fixture-surface is the thirty-eighth workflow deselection outside the bounded direct
  sweep; the skip is classified local absence of the hosted artifact pair.
- Signal inheritance remained exact: both R11/R12 nested functions pass from a normal
  parent and an exec'd child observes `SIG_IGN`.
- Workflow remains byte-identical with 15 ordered unique ignores, 37 ordered unique
  selectors, and 38 cases. All 27 candidate B2/B3/B4 modules remain unignored.
- Raw B1, V001-V004, exact API/typed bytes, parent/worker tightening, CSV exit 5 versus
  replay exit 2, diagnostics, artifact checks, and B2/B3 behavior passed.
- Ruff over production and changed/evidence files: pass. Mypy: 31 source files clean;
  strict public consumer: one file clean. Both stable environments passed `pip check`.
- Strict B1, B2, and B3 manifest validation: pass without output.
- Frontend ESLint and TypeScript: pass; Vitest: three files/five tests; Vite: 29
  modules; production asset drift: pass.
- Installed CLI grammar and PEP 639 metadata remain exact: `GPL-3.0-only`, four license
  files, numpy/pyserial base dependencies, and aiohttp only for the web extra.
- Retained resource checks proved the closed nine-file decoder snapshot and B1
  digests. Scoped prohibited import/command search was empty. The process inventory
  contained no product .NET, pythonnet, `sigrok-cli`, or libsigrokdecode process; its
  sole text match was the verifier's own audit command.
- Candidate-relative changes are limited to portability tests/regression and evidence.
  No workflow, product, decoder/API, B1/B2/B3 fixture, threshold, limit, selector, lock,
  manifest, resource, or frontend byte changed. `git diff --check` passed.

## Findings and dispositions

1. **Hosted artifact pair — verified.** Complete pair wins, both absent use fallback,
   and either partial state fails closed.
2. **No ignored-draft dependency — verified.** The tracked descendant proof passes
   while the draft is unavailable and the draft is preserved unchanged.
3. **Immutable collection — verified.** c765, 423, and current 921f candidate arithmetic
   are stable, safely extracted, cleanup-bounded, and descendant-proof.
4. **Product and contract preservation — verified.** Partition, signal context, raw B1,
   V001-V004, B2/B3, resources, locks, manifests, frontend, and installed API pass.

## Legal and execution boundary

This is an engineering verification, not a legal conclusion. Shim ownership, the
historical MIT label, and combined-work treatment still require counsel or rights-holder
confirmation before conveyance. No wheel, sdist, upload, conveyance, publication,
hardware, serial, capture, Cycle 4 work, or hosted CI dispatch occurred. Exact-candidate
hosted execution remains a root-owned gate and is not claimed here.

APPROVAL_NEEDED: none.

## Verdict

pass
