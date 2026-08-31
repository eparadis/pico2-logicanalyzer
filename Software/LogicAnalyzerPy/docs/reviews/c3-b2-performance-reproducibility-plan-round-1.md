# C3-B2 C3B2-A002 performance reproducibility plan — round 1

## Predeclared subject and purpose

- Owner: primary Cycle 3 orchestrator (`/root`).
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Exact unchanged candidate/tree:
  `959edf77945176b26c7cec86bcdd806d7e5769ea` /
  `bca2c9d482e690d5bd5fa23822f96336bf6aa0b8`.
- Fresh verifier pass: `ed39a653612b5e879aa08391fcb264f43f09a956`.
- Blocking proof finding: `C3B2-A002` at acceptance commit `d5d77a8`.
- State: **predeclared before execution**. This file contains no result.

The valid failed report
`e2602ab8c3dd02e56b1a8492bd85e12f5d6215e8254e2f9462ae5aed32ebd131`
and later passing report
`460b28250af8d8d5fa899dd426c1bf6b61b1791444215cbc2c87a471d940f7b0`
remain conflicting immutable history. Neither is invalidated or selected by
this plan. The purpose is to replace ad hoc retry evidence with one bounded,
precommitted reproducibility gate before repeating the complete owning
accumulation.

## Exact no-retry rule

1. Confirm a clean worktree, exact repository-local Node v22.14.0, unchanged
   package-lock, production-asset-manifest, benchmark-script, and checker
   digests, and no surviving repository pytest, Vite, Playwright, or private
   decoder worker process.
2. Run exactly **five** consecutive invocations of the unchanged frozen command
   `npm run benchmark:b6` using the already approved exact pinned-Node command
   shape. Do not alter product, dependencies, environment path, browser,
   viewport, fixture, warm-up, iterations, statistics, method, checker, or any
   absolute/regression ceiling between invocations.
3. Every invocation must independently complete its governed Playwright test
   and unchanged checker with exit 0. There is no averaging, best-of selection,
   dropped outlier, retry, replacement, or sixth invocation. If any of the five
   fails or is interrupted, stop immediately and record this reproducibility
   gate `changes_required`.
4. After each passing invocation, hash its complete report and move the
   generated `test-results` directory intact to a distinct
   `/private/tmp/c3-b2-a002-series-N` evidence location before the next
   invocation. Record all six timing-group p95 values and both approved
   ceilings. Preserve every result rather than overwriting it.
5. If and only if all five pass, rerun the rest of the complete B2 accumulated
   gate from the beginning against the same candidate/verifier descendant,
   create a new immutable accumulated record binding this predeclared plan and
   all five reports, and obtain a new independent acceptance identity. The new
   acceptance must audit the original failure, this rule, every report, and all
   repeated accumulated evidence; no prior acceptance verdict transfers.

This is a stricter validation-only proof requirement, not an amendment to the
frozen benchmark method or an aggregation/retry semantic. Each original
invocation remains independently judged by the unchanged checker. The rule
does not weaken or rebase any approved value and adds no product behavior.

## Scope and terminal outcome

No B1, product, frontend, fixture, threshold, dependency, workflow, manifest,
or contract byte may change. No external/reference decoder, C#/.NET,
hardware, USB/serial, live capture, publication, B3+, or Cycle 4 action is
authorized. A five-pass series permits only repeated complete accumulation and
fresh acceptance; it does not itself create a manifest/checkpoint or close
`C3B2-A002`. Any series failure leaves B2 at `changes_required` and requires an
earliest-owner correction or authority decision rather than more reruns.

`predeclared-no-result`
