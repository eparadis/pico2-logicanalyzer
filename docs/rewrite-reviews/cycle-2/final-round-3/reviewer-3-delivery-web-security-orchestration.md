# Cycle 2 final-round-3 review — Reviewer 3: delivery, web security, verification, and orchestration

- **Reviewer:** `/root/cycle2_review_delivery` — delivery, web security, verification, and orchestration
- **Reviewed commit:** `911c18882aecc6554ff0f49f149720c01d8cb409`
- **Reviewed tree:** `172c6e1f9332e2bcef8dc09b2cafc11deabfcc67`
- **UTC timestamp:** `2026-08-22T23:16:21Z`
- **Verdict:** `changes_required`

## Prior findings and dispositions

1. **Capability-token and canonical-Origin security:** resolved and retained. The contracts still require literal-loopback canonical origin/Host enforcement, a host-only HttpOnly SameSite cookie, exact Origin validation, no CORS, WebSocket checks, token redaction, bounded file transfer, and C2-B1/B4/B5/B6 negative tests.
2. **Reproducible web-runtime installation:** resolved and retained. The hash-checked `requirements-web.lock`, no-deps editable `.[web]` path, clean macOS/Linux CI proof, separate lock identities, core-only path, and missing-extra test remain required.
3. **Filesystem import/export safety:** resolved and retained. Import is bounded upload bytes without server paths or persistence; export is bounded download bytes without server-path input or persistence, with explicit cleanup and hostile-input checks.
4. **Cycle 2 evidence schema:** resolved and retained. The strict versioned schema, validator, secret scan, role/CI/lock/build/stopping-condition fields, and checkpoint/final validation gate remain required.
5. **Future-manifest lifecycle:** resolved and retained. The contracts prohibit pre-created future manifests; only the owning batch atomically creates and validates its own manifest after implementation, verification, and acceptance evidence, and accepted evidence is immutable with separate correction records.

## New findings

6. **The goal orders acceptance before accumulated validation, so acceptance cannot audit the required complete batch gate.**
   - **Severity:** high
   - **Evidence:** `CYCLE2_GOAL.md` per-batch loop step 6 gives the verified candidate to the acceptance agent; step 7 then runs the accumulated batch gates. Conversely, `CYCLE2_BATCH_EXECUTION.md` defines the acceptance agent as auditing accumulated validation and the checkpoint gate, and its standard procedure runs the validation loop (including accumulated gates) before recording findings and acceptance. The goal thereby makes an acceptance `pass` possible without the exact candidate's complete accumulated results. If step 7 fails, the goal says to diagnose it but does not require a corrected candidate to re-enter verification and acceptance before manifest/checkpoint work.
   - **Requested resolution:** Reorder the goal loop so the exact immutable candidate first passes focused and accumulated batch gates, with concise results recorded for acceptance; then give that candidate and results to the acceptance lane. State explicitly that any accumulated-gate failure or resulting correction creates a new candidate which must repeat verification, accumulated validation, and acceptance before its manifest is created. Preserve the primary's compact-handoff/no-content-review rule while allowing the acceptance agent to read durable evidence and exact gate results.
   - **Disposition:** open.

## Goal-specific observations

- The stated authority order correctly subordinates the goal to the approved contracts, locks their immutability during execution, and identifies the approved contracts and common-commit review passes.
- The fixed primary/three-worker model assignments, lane reuse, no role conversion, no worker subdelegation, compact handoffs, candidate/review loop, authority gates, blocked rule, evidence lifecycle, and final stopping condition are otherwise compatible with the governing contracts.
- The macOS-native/Linux-CI qualification and prohibitions on firmware mutation, .NET, `.lac`, public serving, packaging/publication, and Cycle 3 remain intact.
