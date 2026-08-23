# C2-B1 independent verification

- Lane / identity: verifier / `cycle2-verifier`
- Reviewed candidate commit: `cdcdb4f7e5973ad0aa06c8ece792df07f7e25fc6`
- Reviewed candidate tree: `16cb4a2cb62a5a3185550f641a8b871fd50bf5bf`
- Review date: 2026-08-22 America/Los_Angeles
- Verdict: `changes_required`
- Verification fixture: `tests/verification/test_c2_b1_foundation_blackbox.py`

## Scope and method

The review independently checked C2-B1 against `CYCLE2_ORCHESTRATION.md`,
`CYCLE2_BATCH_EXECUTION.md`, the approved discovery and preparatory records,
the accepted Cycle 1 baseline, and the exact candidate. Checks exercised the
production CLI over HTTP, constructed evidence objects independently of the
candidate validator, built a wheel from a clean `git archive`, audited the
locked-runtime closure and workflow, ran the accumulated non-hardware suite,
and audited prohibited/rollback paths. No serial, hardware, firmware, C#,
.NET, public-server, or Cycle 3 operation occurred.

## Findings

### C2B1-V001 — The supported web-runtime lock is incomplete

Evidence: `requirements-web.lock` contains the aiohttp closure but omits the
project's mandatory `numpy==2.2.2` and `pyserial==3.5` dependencies. The
workflow creates a fresh `.venv-web`, installs only this lock, installs
`.[web]` with `--no-deps`, and then runs `pip check`; that prescribed clean job
cannot satisfy the installed distribution. The verifier-owned lock-closure
check fails with both names absent.

Requested resolution: make `requirements-web.lock` the complete hash-checked
application/web runtime closure and prove the exact clean no-deps installation
and `pip check` path.

Disposition: open.

### C2B1-V002 — Built distributions omit the hashed JavaScript and CSS

Evidence: the package-data rule is only `web/assets/*`. An independent wheel
built from a clean archive contains `web/assets/index.html` but neither
`web/assets/assets/index-D52kpctL.js` nor
`web/assets/assets/index-CIUDlNME.css`. The installed HTML therefore references
missing resources even though editable source execution masks the defect.

Requested resolution: include nested production assets in built source/wheel
metadata and add a clean installed-distribution production smoke that fetches
every manifest asset.

Disposition: open.

### C2B1-V003 — Successful shutdown does not stop the production server

Evidence: the black-box process test obtains the initial HttpOnly capability
cookie, sends the canonical Origin and cookie to `/api/v1/shutdown`, receives
204 plus cookie expiry, and observes that the process remains alive beyond the
bounded shutdown interval. The handler only mutates application flags; it does
not stop aiohttp.

Requested resolution: connect the protected endpoint to orderly runner/process
termination, retain expiry, release ownership, and prove deterministic exit
and immediate bounded reuse.

Disposition: open.

### C2B1-V004 — Evidence validation is not recursively strict and misses secrets

Evidence: independently constructed otherwise-valid manifests are accepted by
`validate_cycle2_evidence.py` after an unknown nested stopping-condition field
is added. The validator does not inspect stopping-condition or artifact
members. It also accepts a loopback browser URL in a free-text findings array;
the free-text arrays are type-checked only as arrays and are never scanned.
Timestamp syntax and several schema constraints are likewise not enforced by
the executable validator. This diverges from the checked-in JSON schema and
the required recursive no-extra-properties/secret scan.

Requested resolution: validate every nested object/value against the frozen
schema (including formats where claimed), scan all string leaves for every
prohibited secret/machine-local class, and add missing/extra/type/secret tests
at each recursive level.

Disposition: open.

### C2B1-V005 — The browser gate does not launch or test a browser

Evidence: `test:browser` expands to `playwright ... --list`; its sole test is
the in-process assertion that the literal string `"pico-la"` equals itself.
The Playwright configuration defines neither a browser project nor production
web-server startup. Thus the reported successful command merely lists one test
and provides no installed-browser, production start/readiness/shutdown,
asset-load, offline, cookie, or serial-absence observation.

Requested resolution: create an actual headless installed-browser production
smoke and make the canonical/CI command execute it, including startup,
readiness, local asset loading, protected shutdown, and objective token
non-disclosure checks owned by B1.

Disposition: open.

### C2B1-V006 — Workflow omits mandatory reproducibility gates and has no hosted result

Evidence: the macOS/Linux workflow runs a frontend build but never invokes
`scripts/check_web_assets.py` or otherwise compares the clean rebuild to the
committed assets. Its nominal browser step has the V005 `--list` behavior. No
hosted macOS/Linux exact-candidate run identity/result exists for this review.
Local frontend commands ran under Node `v26.5.0`, not the supported Node
`22.14.0`, so they cannot substitute for the accumulated pinned-runtime gate.

Requested resolution: make both matrix jobs enforce asset drift and a real
headless browser smoke, then provide an exact-candidate hosted macOS/Linux pass.
Also retain clean Node 22.14.0 bootstrap evidence rather than treating the
local Node 26 run as acceptance evidence.

Disposition: open; hosted CI and a Node 22.14.0 runtime are accumulated external
gates requiring operator/CI availability.

### C2B1-V007 — OS-assigned loopback ports and exact lifecycle output are not implemented/frozen

Evidence: the governing local-web boundary permits an OS-assigned or explicit
loopback port. `create_app`, `canonical_authority`, and the CLI reject port 0.
The only startup text is `pico-la web: ready`; it does not report a usable
sanitized browser URL or actual assigned authority, and the active documents do
not freeze exact startup/readiness/shutdown output, supported browser version,
or the complete frontend canonical commands as required by B1.

Requested resolution: implement OS-assigned loopback binding with canonical
authority determined after bind, freeze the exact lifecycle/output and
supported tool/browser versions in active B1 documentation, and cover both
IPv4 and IPv6 literal loopback authority formatting where supported.

Disposition: open.

## Command evidence

- Candidate identity/status: pass — exact commit/tree; candidate worktree clean
  before verifier-owned artifacts.
- Focused verifier suite with loopback authority: 7 checks; 6 fail, 1 pass
  (the first run before the port-0 check was added was 5 fail, 1 pass).
- Accumulated Python non-hardware gate after adding verifier tests: 218 pass,
  2 fail, 1 sandbox-skip; the separately authorized loopback run reproduces the
  shutdown failure. Candidate tests excluding verifier additions were green.
- Frontend local gate: lint pass; typecheck pass; Vitest 1 pass; build pass;
  Playwright command listed 1 and executed 0; runtime Node v26.5.0.
- Production asset manifest check: pass after local build.
- Clean archive wheel audit: wheel built; 1 HTML asset present; 2 referenced
  nested assets absent.
- Prohibited-scope/rollback audit: pass — no firmware/C# paths differ from the
  approved preparatory commit; accepted Cycle 1 paths/tests remain present.

## Required re-verification

All open findings affect the same C2-B1 foundation and require a new immutable
candidate. Re-run the focused verifier suite, clean core/web installs, actual
Node 22/browser production smoke, full accumulated gate, archive wheel audit,
and exact-candidate hosted macOS/Linux matrix before acceptance.
