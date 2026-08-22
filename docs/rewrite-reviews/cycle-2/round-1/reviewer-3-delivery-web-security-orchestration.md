# Cycle 2 review — Reviewer 3: delivery, web security, verification, and orchestration

- **Reviewer:** `/root/cycle2_review_delivery` — delivery, web security, verification, and orchestration
- **Reviewed commit:** `61bf35dc5cf3a95a1513cbb13f182635bd3b8461`
- **Reviewed tree:** `f1e2ee2d571e5e1a0077872f694f82198a743186`
- **UTC timestamp:** `2026-08-22T01:46:03Z`
- **Verdict:** `changes_required`

## Findings

1. **Web capability-token and same-origin enforcement are not sufficiently specified to be independently secured.**
   - **Severity:** high
   - **Evidence:** `CYCLE2_ORCHESTRATION.md` requires an unpredictable per-launch capability token and “same-origin browser policy”; `CYCLE2_BATCH_EXECUTION.md` requires a token and same-origin validation for protected endpoints, and tests only absent/invalid token and a foreign `Origin`. Neither contract freezes how the token reaches browser code (in particular, whether it may appear in the URL), its permitted request location, the canonical origin against which `Origin` is compared, nor the mandatory behavior for missing/opaque `Origin`, Host-header-derived origins, redirects, and WebSocket upgrade requests. The documents also do not require a test proving that a capability token is never reflected in URLs, `Referer`, logs, responses, or committed evidence.
   - **Requested resolution:** Before C2-B1, add one narrowly scoped local-web security contract and independent negative-test requirements. It must define a non-URL token delivery/request mechanism, token lifetime and constant-time validation expectation, canonical loopback origin construction independent of untrusted request headers, rejection rules for absent/invalid/foreign/opaque origins and WebSocket upgrades, no CORS credentials or permissive CORS, and redaction/no-reflection rules. Apply it to every mutating endpoint, including shutdown, and make B1/B4/B6 verification exercise each rule.
   - **Disposition:** open.

2. **The optional web installation is not locked reproducibly for the claimed source-installed runtime.**
   - **Severity:** high
   - **Evidence:** The current `Software/LogicAnalyzerPy/pyproject.toml` has only un-hashed project dependencies, and the only current hash-required Python lock is `requirements-dev.lock`. The proposed B1 requires a `web` optional extra and says that the reviewed *development* lock and CI include it, while requiring that a source-installed end user run the offline web application without Node or network. The prescribed `pip install --no-build-isolation --no-deps -e .` installs only after the development lock has supplied dependencies; it does not define an end-user, hash-locked installation of the `web` extra. Thus a `pip install -e '.[web]'` runtime path can resolve new artifacts and transitive versions outside the reviewed lock.
   - **Requested resolution:** Freeze and validate an explicit supported web-runtime installation path before B1 completes: either a hash-checked, web-inclusive Python requirements lock used before no-deps source installation, or an equivalently pinned and integrity-checked local artifact/wheel procedure. Require macOS and Linux clean-runtime proof from that path, record its digest in the evidence schema/checkpoint, and ensure the core-only path remains separately tested. Do not treat the developer lock alone as end-user web-runtime reproducibility.
   - **Disposition:** open.

3. **The file-operation boundary is too ambiguous to prove filesystem safety.**
   - **Severity:** medium
   - **Evidence:** The local-web contract permits “filesystem output” as a token-protected operation, says paths are not accepted from untrusted browser input “unless constrained to a user-selected operation with the settled safe file contract,” and assigns import/export endpoints in C2-B4. No settled safe file contract defines upload-only import versus server paths, export download versus server writes, allowed roots/extensions, symlink and overwrite behavior, size/accounting before storage, temporary-file cleanup, response content-disposition, or the exact verification cases. Token/origin checks cannot establish those properties.
   - **Requested resolution:** Freeze a minimal browser file contract before C2-B4: prefer bounded uploaded bytes for import and HTTP download responses for export, with no browser-supplied server path. If any local write is indispensable, define a single approved root, generated names, no-follow/atomic creation, overwrite prohibition, limits before persistence, and cleanup. Add independent traversal, symlink, overwrite, malformed multipart, quota, cancellation, and cleanup tests; make the evidence schema record only sanitized artifact identities.
   - **Disposition:** open.

4. **Cycle 2 evidence requirements do not yet freeze a Cycle-2 machine-readable schema capable of enforcing the final proof.**
   - **Severity:** medium
   - **Evidence:** The accepted Cycle 1 schema is explicitly titled and constrained to Cycle 1 (`schema_version: 1`, checkpoint pattern `^C1-B[1-5]$`, a single `lock_sha256`, and an environment with no Node/browser fields). B1 merely says to create an “evidence-schema extension”; the batch procedure later requires an atomic machine-readable manifest, two lock digests, production-asset identity, CI/browser/performance evidence, three identities, review findings, and fourteen stopping-condition mappings, but does not state the schema version, required fields, validation command, or a no-extra-properties policy for the extension.
   - **Requested resolution:** Make C2-B1 freeze, version, and validate a Cycle-2 evidence-manifest schema before any B1 acceptance. Require both lock digests, asset/build manifest digest, Python/Node/browser/OS identities, command outcomes, CI run/job URLs and exact commit, evidence artifact digests, sanitized hardware fields, implementation/verifier/acceptance identities and verdicts, threshold-record digest where applicable, and explicit stopping-condition coverage. Require schema validation as a checkpoint gate and reject secret-bearing fields.
   - **Disposition:** open.

## Reviewed no-change observations

- The documents retain the firm prohibitions on firmware mutation, .NET and `.lac`, public/non-loopback serving, packaging/publication, and Cycle 3; these are appropriate rollback and scope controls.
- The ordered C2-B1 through C2-B6 ownership table, distinct implementation/verification/acceptance identities, common-commit review rule, macOS-native versus Linux-CI support wording, hosted-CI authority gate, and C2-B5 operator-approved performance-threshold procedure are present and materially support a verifiable stopping condition.
- No finding recommends product implementation or changes outside the proposed Cycle 2 contracts.
