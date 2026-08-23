# C2-B6 verification round 4

- Identity: `cycle2-verifier-replacement-3`, independent Verification lane.
- UTC: `2026-08-23T22:46:43Z`.
- Product candidate: `2d5484a73d881496cdf5a35c799dfb01eedad229`;
  tree `8c76bce79922263468cb6ceaa4f1990703a84bfc`.
- Implementation record: commit `a349cc5`, SHA-256
  `655c56b770e35e2bb4b4dbb6a78116b5e7842b714cf29c2e5f61d7dca3a379af`, evidence only.
- Verdict: `pass`.

## Findings and dispositions

1. `C2B6-A001` — closed. The repository contains exactly one active workflow, it is
   macOS-only, and its dispatch trigger does not alter product behavior. Top-level
   `contents: read` is the sole permission; no write permission, secret expression,
   `pull_request_target`, service, or privileged device access exists. Hash-locked Python
   installs, Ruff, mypy, the complete nonhardware suite, CLI help, hash-locked web runtime,
   locked Node install, frontend lint/type/unit/build, asset drift, and production browser smoke
   all remain mandatory.
2. `C2B6-A001-AVAILABILITY` — closed. Independent branch tests prove that total absence at the
   default machine-local location produces an explicit skip; a partial default set, an explicitly
   supplied missing/partial set, corrupt content, and digest mismatch fail. A complete set runs
   every original physical assertion: inert NPZ structure and metadata, 8/16/24 channel masks and
   frequency, deterministic CSV, and bounded recovery. The checked-in sanitized B3 evidence is
   separately mandatory and validates successfully.
3. `C2B6-A001-DIAGNOSTICS` — closed. The workflow preserves pytest's exit status while emitting a
   bounded 12,000-byte printable tail and a concise GitHub error annotation. Its sanitizer
   self-test requires token and device-path redaction before tests run; URL, user-home path,
   device path, capability-cookie, and token-shaped values are redacted. Temporary log/probe files
   are removed by an exit trap.
4. `C2B6-V001`, `C2B6-V002`, and `C2B6-V003` — remain closed. Diffing from the accepted round-3
   candidate shows no change to Python runtime, frontend source, benchmark producer, or native
   acceptance harness. Therefore the accepted 100,000 waveform ceiling, benchmark enforcement,
   strengthened native assertions, and bound physical/recovery evidence retain identical product
   semantics.

## Independent evidence

- Candidate identity resolved exactly to tree
  `8c76bce79922263468cb6ceaa4f1990703a84bfc`.
- Focused workflow, availability, and complete physical-artifact verification: 8 passed. The
  complete runtime artifacts matched all seven frozen digests; no machine-local value is copied
  here.
- Clean accumulated nonhardware Python: 383 passed, 2 documented sandbox-loopback skips,
  106 warnings. Ruff passed; strict mypy reported no issues in 21 source files; sanitized C2-B3
  evidence validation passed.
- Frontend lint and typecheck passed; unit tests passed 5/5; production build and asset-drift
  check passed.
- GitHub Actions API independently reports run `32671356406`, sole job `97272584254`, event
  `push`, exact head SHA and tree above, `macos-latest`, completed `success`. Every setup, install,
  dependency, static, nonhardware, CLI, frontend, asset, Chromium, browser, post, and completion
  step reports `success`.
- Workflow SHA-256:
  `ab0809523370ecfe308fe733be011c83f926315eeca12e7a0d3ab294b357ea22`;
  invariant test `434d7869c8ee94207afb79fc0dd7e44c0a0390eb005d790f4f8289443facf241`;
  availability test `852bfe65f98bfe00e3a8fb2e16aacf8dcdee27aea0cbb1f50ab96c7d73d536b2`;
  guarded physical verifier
  `94d794349fff256862c82e513e0e0e7d736fed46eafaf2aad2d1b65ea36f83ac`.
- Sanitized B3 evidence SHA-256:
  `9db03e119c6cacb40e87ef61d8f7ef1e24692ea45527f5e331e2103ecc59ff1b`;
  validator `d2bbddea9e1bb43f703e5873aa38a1f854b3a702e27b9808c63e381c57856ff0`.

## Scope and conclusion

Verification was read-only except for this record. No product, prior evidence, contract, progress,
manifest, workflow, test, firmware, wiring, device state, acceptance, B5, or Cycle 3 file was
changed. No hardware or serial device was opened.

Open findings: none. Deferred findings: none.
