# Cycle 2 final-round-1 review — Reviewer 3: delivery, web security, verification, and orchestration

- **Reviewer:** `/root/cycle2_review_delivery` — delivery, web security, verification, and orchestration
- **Reviewed commit:** `f115bff194c812eb1d55f5adfcf2afabd8b54589`
- **Reviewed tree:** `a0db51794c29e2b88dd14254dc8da74b0ccaced3`
- **UTC timestamp:** `2026-08-22T20:04:05Z`
- **Verdict:** `changes_required`

## Prior round-1 findings and dispositions

1. **Web capability-token and same-origin enforcement lacked a security contract.**
   - **Disposition:** resolved in `f115bff194c812eb1d55f5adfcf2afabd8b54589` and verified in this review.
   - **Evidence:** The `Local web application boundary` now fixes a canonical origin from the configured literal loopback address and actual port, rejects alternate Host forms, places the per-launch capability only in a host-only `HttpOnly`, `SameSite=Strict` cookie, rejects absent/null/opaque/foreign Origin and invalid cookies before work, applies the same checks to WebSocket upgrades, emits no CORS policy, requires constant-time comparison, and requires token-redaction scans. C2-B1/B4/B5/B6 acceptance explicitly includes independent Host/Origin/cookie/WebSocket and non-disclosure checks.

2. **The optional web runtime had no reproducible hash-locked installation path.**
   - **Disposition:** resolved in `f115bff194c812eb1d55f5adfcf2afabd8b54589` and verified in this review.
   - **Evidence:** The required surface and C2-B1 now require a complete hash-checked `requirements-web.lock`, followed by `pip install --no-build-isolation --no-deps -e '.[web]'`; macOS and Linux CI must use that path, run `pip check`, and record its digest separately from `requirements-dev.lock`. The core-only and missing-extra paths remain required checks.

3. **Filesystem import/export safety was underspecified.**
   - **Disposition:** resolved in `f115bff194c812eb1d55f5adfcf2afabd8b54589` and verified in this review.
   - **Evidence:** The local-web contract now limits import to bounded multipart bytes with pre-stream and streaming accounting, no persistent server-side file, and cleanup on malformed input/cancellation/disconnect. Export is a bounded HTTP download with server-generated safe headers and filename, accepts no server path or overwrite target, creates no persistent file, and has traversal, quota, cancellation, header, and zero-residue test requirements. C2-B4 and C2-B6 make those checks acceptance gates.

4. **Cycle 2 did not freeze a machine-readable evidence schema capable of proving final completion.**
   - **Disposition:** resolved in `f115bff194c812eb1d55f5adfcf2afabd8b54589` and verified in this review.
   - **Evidence:** `CYCLE2_ORCHESTRATION.md` now fixes a draft-2020-12 Cycle 2 schema, `schema_version: 2`, C2 checkpoint pattern, recursive `additionalProperties: false`, a validator command, secret rejection, separate development/web-runtime/JavaScript/asset digests, CI and environment fields, three mutually distinct roles/verdicts, and explicit coverage/digests for all fourteen stopping conditions. Schema validation is a checkpoint and final-completion gate; C2-B1 must demonstrate accept/reject cases.

## New findings

5. **C2-B1 is directed to create future checkpoint manifests before their evidence exists, conflicting with the atomic, per-batch evidence rule.**
   - **Severity:** medium
   - **Evidence:** In `CYCLE2_ORCHESTRATION.md` under `Progress and evidence`, C2-B1 is required to create `testdata/evidence/c2-b1.json` **through** `c2-b6.json`. In contrast, `CYCLE2_BATCH_EXECUTION.md` standard procedure step 7 requires the orchestrator to write the machine-readable batch manifest atomically after that batch's verification and acceptance, while the checkpoint record is appended only after its complete acceptance gate passes. C2-B2 through C2-B6 cannot yet truthfully provide their tested commit/tree, role verdicts, command outcomes, CI evidence, artifacts, stopping-condition coverage, or (for B5/B6) approved threshold digest. Precreating final-looking manifest files makes their lifecycle and immutability ambiguous and invites placeholder or future-evidence mutation.
   - **Requested resolution:** Change the C2-B1 requirement to create only the Cycle 2 schema, validator, and the C2-B1 manifest (plus empty reviewed directories or a clearly non-manifest template if useful). Require C2-B2 through C2-B6 manifests to be created atomically only by their owning batch after its acceptance evidence exists; each must validate before the checkpoint record is appended. State that a future manifest filename is not evidence and may not be pre-populated as an accepted manifest.
   - **Disposition:** open.

## Reviewed no-change observations

- The bounded objective, ordered stopping-condition ownership, three distinct batch identities, common-commit final-review requirement, threshold approval sequence, rollback rules, hosted-CI approval gate, and qualified macOS-native/Linux-CI claims remain coherent.
- The contracts continue to prohibit firmware mutation, .NET, `.lac`, public serving, runtime Node/CDN use, packaging/publication, native Linux hardware claims, and Cycle 3.
