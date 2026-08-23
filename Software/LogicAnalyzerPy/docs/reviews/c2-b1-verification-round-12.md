# C2-B1 hosted CI diagnosis, verification round 12

- Lane / identity: verifier / `cycle2-verifier`
- Reviewed candidate commit: `8fd4d737be283d68a7cbe682225eb781fb58ef5a`
- Reviewed candidate tree: `fa98722af2c5992a40d54c0adc032e4e26f7ecaf`
- Hosted run: `32619189350`
- macOS job: `97144622863`
- Ubuntu job: `97144622939`
- Review date: 2026-08-22 America/Los_Angeles
- Verdict: `changes_required`

## Hosted evidence

The public jobs API confirms both jobs checked out the exact candidate SHA.
Both platforms passed checkout, Python 3.12 and Node setup, clean core virtual
environment creation, hash-locked dependency installation, no-deps source
installation, `pip check`, Ruff, and mypy. Both then failed the named
non-hardware Python-test step before any later step ran.

The macOS test step ran from `04:59:10Z` to `04:59:10Z`; Ubuntu ran from
`04:59:17Z` to `04:59:17Z`. Public check annotations identify workflow lines
45/46 and report `Process completed with exit code 2` on both platforms. This is
the sanitizer self-test's explicit failure status, not pytest's normal status.
The only other public annotation is a non-fatal GitHub Actions runtime
deprecation warning; it does not explain either job failure.

No sensitive hosted output was retrieved or recorded.

## Finding

### C2B1-V011 — Sanitizer self-test rejects its correct output on every platform

The fixed hostile input sanitizes correctly to text containing
`<TOKEN_REDACTED>` followed by `<PORT_REDACTED>`, with neither original hostile
literal present. The shell `case` nevertheless includes
`*'<TOKEN_REDACTED>'*'<PORT_REDACTED>'*` as a failure alternative alongside the
two genuine leak alternatives. Therefore correct output deterministically
enters the failure branch and exits 2 before pytest.

An independent local execution of the exact sanitizer and `case` produced:

```text
actual=<TOKEN_REDACTED> port=<PORT_REDACTED>
FAIL
```

This exactly explains both public annotations, their identical status, and the
zero-duration test steps. It also explains why local accumulated validation
that invoked pytest directly passed while the workflow wrapper failed.

Requested resolution: change the self-test logic so it fails when either
hostile original survives or either required redaction marker is absent. Keep
the fixed hostile literals, exact pytest command, captured pytest status,
sanitizer bounds, annotation escaping, temporary cleanup, and no-
`continue-on-error` semantics. Add or execute explicit positive and negative
self-test cases rather than expressing marker presence as a failure glob.

Disposition: open; workflow/implementor owner.

## Preserved evidence

Round 11 independently proved the sanitizer transform, seven verifier checks,
and pinned Node 22 browser behavior. Those observations diagnose this workflow
control-flow error but do not convert the failed exact-candidate hosted matrix
into a pass. A corrected immutable candidate must repeat independent
verification and the complete macOS/Linux hosted gate.

## Final state

The exact candidate cannot complete C2-B1 because both required hosted matrix
jobs fail before pytest. C2B1-V011 remains open.
