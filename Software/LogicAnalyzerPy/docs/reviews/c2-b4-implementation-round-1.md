# C2-B4 implementation round 1

- Candidate: `296feec`; tree `660a1f3d7689002c588c583591d8bf30b589d09f`.
- Scope: pure Python transition/distinct-strobe bus analysis, bounded loopback
  REST/polling API, Python-owned OpenAPI 3.1 artifact, generated TypeScript
  API types, and focused fixtures.
- Focused gates: 17 passed, 1 sandbox loopback skip; full non-hardware Python:
  283 passed, 2 sandbox loopback skips; Ruff, mypy, OpenAPI checker, CLI help,
  Node lint/type/unit/build all passed.
- Security behavior: literal loopback/Host gate, exact Origin and capability
  cookie for mutations, no CORS or WebSockets, bounded request/upload/window/
  row/capture limits, redacted error envelope, in-memory opaque capture IDs,
  and direct safe CSV download headers.
- Contract digests: `openapi.json`
  `d4ed2aeb0c4181858002b057b3b44f1a90d14d3a4125a5bb6587f5b229a2c3a2`;
  `api.generated.ts`
  `acb72dad34116e7b562da3e5f6afea8f608aa73573b8127d433fba2f823de734`.
- No serial/device access, firmware, C#, workflow, public-server, browser, or
  persistent import/export files were used.
