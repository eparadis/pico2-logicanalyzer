# C2-B1 independent verification, round 2

- Lane / identity: verifier / `cycle2-verifier`
- Reviewed candidate commit: `e4e9212e1bb03fe914f56c445b79a72a7c4147e9`
- Reviewed candidate tree: `5ac271a0c36b20ff8c12afc58f71dd3a60e751c6`
- Review date: 2026-08-22 America/Los_Angeles
- Prior verdict transfer: none
- Verdict: `changes_required`

## Scope and method

This round re-read the exact candidate and independently re-exercised every
round-1 finding. It used the verifier-owned seven-check suite, direct inspection
of the changed runtime lock, package metadata, executable validator, server
lifecycle, browser configuration/test, workflow, and active CLI contract, plus
an escalated real loopback process check. No product file, governing contract,
firmware, C# application, hardware, .NET surface, or Cycle 3 surface was
modified or exercised.

## Prior finding dispositions

### C2B1-V001 — closed

`requirements-web.lock` now contains the pinned core dependencies as well as
the aiohttp closure. The independent project-metadata-to-lock closure check
passes. A clean Node/Python/CI bootstrap remains part of C2B1-V008 rather than
being inferred from this structural check.

### C2B1-V002 — closed

Package data now explicitly includes `web/assets/assets/*`; the verifier-owned
nested-production-asset rule passes. The earlier clean-wheel omission has been
addressed structurally.

### C2B1-V003 — closed

The escalated black-box test starts the production CLI, obtains its initial
capability cookie, submits exact canonical Origin/cookie shutdown, receives
204/cookie expiry, and observes bounded process exit status 0. The test passes.

### C2B1-V004 — closed

The executable validator now walks stopping-condition/artifact structures,
rejects nested extras, scans free-text leaves, checks bounded worktree text and
UTC timestamp syntax, and retains distinct-role checks. Both independently
constructed adverse manifests are rejected and all seven verifier checks pass.

### C2B1-V005 — closed as a candidate implementation defect

The browser command now executes Playwright rather than `--list`; configuration
starts the production Python server and the test opens the shell, observes the
heading/cookie/readiness, performs protected shutdown, and checks console token
non-disclosure. Actual installed-browser execution is unresolved under
C2B1-V008.

### C2B1-V006 — closed as a workflow-definition defect

The macOS/Linux workflow now invokes the committed-asset drift checker and the
real Playwright command in addition to the clean web-runtime installation.
Hosted exact-candidate execution and pinned Node runtime evidence are unresolved
under C2B1-V008.

### C2B1-V007 — closed

The server accepts port 0, derives its canonical authority after bind, brackets
IPv6 literals, flushes the exact ready URL, and the active CLI contract freezes
the lifecycle output, Node/Playwright versions, and canonical frontend
commands. The independent port-0 check passes.

## New finding

### C2B1-V008 — Required installed-browser, Node 22, and hosted matrix evidence is unavailable

Evidence: the exact candidate's verifier regression suite passes 7/7,
including real loopback process shutdown. Two separately authorized attempts
to execute the real Playwright gate produced no test result and did not return
before external termination after approximately 731.9 and 555.4 seconds. The
local Node runtime previously observed is v26.5.0, not the frozen v22.14.0.
No exact-candidate hosted macOS/Linux workflow result was supplied. Because the
commands yielded no Playwright failure, assertion, trace, or browser result,
this round cannot truthfully classify the browser non-result as a candidate
product defect; it is an unavailable external runtime gate. It also cannot be
treated as a pass.

Requested resolution: provide a bounded successful execution of the real
installed-browser smoke under the supported Node 22.14.0 environment and the
exact-candidate hosted macOS/Linux matrix identities/results. If a bounded run
then produces a product failure, open a new product finding against that exact
evidence rather than inferring one from these externally terminated attempts.

Disposition: open; requires browser/runtime and hosted-CI availability plus
normal execution/push authority.

## Command evidence

- Candidate identity/status: pass — exact commit/tree and clean starting
  worktree.
- `pytest tests/verification/test_c2_b1_foundation_blackbox.py -q` with
  loopback authority: pass — 7 passed in 0.72 seconds.
- `npm run test:browser`: no result; externally terminated after 731.9 seconds.
- bounded diagnostic Playwright invocation with a 10-second per-test timeout:
  no result; externally terminated after 555.4 seconds before a Playwright
  report was returned. No further long browser command was attempted.

## Required next evidence

Do not submit this candidate to acceptance as a complete C2-B1 gate. Retain the
candidate while the orchestrator obtains bounded Node 22.14.0 installed-browser
and exact-candidate hosted macOS/Linux evidence. A product correction is not
requested by this record unless that evidence identifies an actual failure.
