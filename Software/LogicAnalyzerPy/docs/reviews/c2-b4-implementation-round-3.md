# C2-B4 implementation round 3

- Corrected product candidate: `c627cc33999e3d1caef03dd281f99ef0487e4c6a`; tree
  `81cbccda857122df7a7d51dba530d0c985c7d8be`.
- `C2B4-V001`: resolved. The Python-owned OpenAPI contract now specifies the
  asynchronous import `202 Operation` response and a recursively closed
  nullable `capture_id`; generated TypeScript models the same lifecycle.
- `C2B4-V004`: resolved. Imports reserve one owner before multipart consumption,
  expose pending/running/cancelling states, parse in bounded background offline
  work, reject active conflicts before upload allocation, honour cancellation,
  and clear task ownership on completion and app cleanup.
- `C2B4-V006`: resolved. A 4 MiB outer request boundary permits the bounded
  3 MiB aggregate multipart artifact boundary while JSON remains bounded.
- `C2B4-V009`: resolved. Schema-1 replay reads retain the 32 MiB archive and
  17 MiB sample-member bounds accepted by the frozen replay contract.
- `C2B4-V010`: resolved. Loopback requests have finite eight-in-flight owner
  and 32-per-second window limits with deterministic `429` responses and
  cleanup.
- Focused lifecycle and limits tests exercise real background blocking,
  pollable cancellation, conflict-before-body, terminal cleanup, and rate/
  connection rejection; they cannot pass with synchronous or fake cancellation.

## Validation

- B4/web focused tests: 23 passed, 1 sandbox loopback skip.
- Full Python suite: 294 passed, 72 warnings.
- Ruff: pass; mypy: pass over 21 source files; cached and working diff checks:
  pass.
- Node 22 lint, typecheck, Vitest: 1 passed, and production build: pass
  (26 modules). No real-loopback/browser run was needed after the safe gates;
  sandbox loopback coverage is explicitly reported above.

## Scope audit

No serial/device access, firmware, C#, public listener, persistent import or
export file, package/publish, B5/B6, governing-contract, manifest, or Cycle 3
change occurred. All round-2 findings are resolved in this candidate; fresh
independent verification remains required.

- Contract digests: OpenAPI
  `1792b49fac3a60bbf7d0188cafa7599e8ec48933c62797eb485f8d7341f290dd`; generated
  TypeScript `56032d85b25ffbf2ff33c5377efe125317966bbec953e8192cb1a02b4fc6fbcf`.
