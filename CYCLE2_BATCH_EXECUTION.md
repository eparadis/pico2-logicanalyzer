# Logic Analyzer Python Rewrite: Cycle 2 Batch Procedure

## Purpose and authority

This document is the mandatory per-batch operating procedure for Cycle 2. It is
subordinate to `CYCLE2_ORCHESTRATION.md` and operationalizes the approved
decisions in
`Software/LogicAnalyzerPy/docs/cycle-2-discovery-review.md`.

It defines how the primary orchestrator selects, assigns, integrates, verifies,
accepts, and records C2-B1 through C2-B6. It does not start a `/goal`, authorize
Cycle 3, or replace the required preparatory common-commit review.

## Required reading order

Before selecting C2-B1, the orchestrator reads:

1. `AGENTS.md` and every included instruction.
2. `CYCLE2_ORCHESTRATION.md` in full.
3. This document in full.
4. `Software/LogicAnalyzerPy/docs/cycle-2-discovery-review.md` in full.
5. `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md`, treating
   work outside Cycle 2 only as context.
6. `Software/LogicAnalyzerPy/docs/cycle-1-completion.md`, the accepted Cycle 1
   manifests, and the current Python implementation/tests.
7. `docs/rewrite-reviews/README.md`, the architectural-domain charters, and the
   three final common-commit passes approving these Cycle 2 contracts.

Every assigned agent receives its batch outcome, scope, owned paths, prohibited
work, authoritative sources, prerequisite checkpoint, required evidence, and
current repository status. “Continue the rewrite” is not an acceptable task.

## Batch state model

Each batch has exactly one state:

- **Pending:** a prerequisite, accepted checkpoint, contract, or operator input
  is absent.
- **Ready:** all prerequisites needed to begin bounded work are present.
- **In progress:** implementation or independent verification is active.
- **Verifying:** the integrated candidate is running the complete batch gate.
- **Awaiting approval:** objective evidence exists but the batch requires an
  external approval, such as hosted CI, physical wiring confirmation, or the
  C2-B5 performance-threshold decision.
- **Complete:** verification and acceptance both pass, the manifest is
  committed, and the checkpoint record is appended.
- **Blocked:** the same external blocker has persisted under the governing goal
  policy and no meaningful in-scope work remains.

Only one batch may be in `Verifying` or `Awaiting approval` at a time. Batches
become complete only in order. A later experiment never advances the checkpoint
sequence or consumes an unsettled interface.

## Required identities and ownership

Each batch uses three distinct identities:

- **Implementation agent:** owns the bounded production surface and focused
  implementation tests.
- **Verification agent:** independently derives boundary, negative,
  compatibility, security, performance, or physical checks from authoritative
  evidence. It owns separate fixtures/tests and reports exactly `pass` or
  `changes_required`.
- **Acceptance agent:** audits the integrated candidate, all findings and their
  dispositions, accumulated validation, scope, evidence, and checkpoint gate.
  It reports exactly `pass` or `changes_required`.

The primary orchestrator owns integration, shared-interface decisions,
accumulated validation, progress/evidence records, threshold proposals,
checkpoint acceptance, and final completion. These duties do not make the
orchestrator one of the three independent identities.

An agent may inspect all relevant sources but edits only its assigned paths. A
verifier does not approve production behavior or expected fixtures it authored.
An acceptance agent does not repair the candidate it is auditing. If ownership
overlaps or an agent changes roles, reassign the affected review to a fresh
identity. Separation may be sequential but may not be waived.

Parallelize only disjoint work against settled interfaces. Keep at most one
integration-changing agent active on a shared Python model, protocol, replay,
API schema, TypeScript API type, dependency lock, workflow, or generated-assets
path. The orchestrator preserves one available coordination slot when using
subagents.

## Active-batch progress entry

Before assigning work, update
`Software/LogicAnalyzerPy/docs/cycle-2-orchestration-progress.md` with:

```markdown
## C2-BN: <name>

- State: Ready
- Objective: <one bounded outcome>
- Prerequisites: <accepted checkpoints and required operator inputs>
- Implementation agent: <stable identity>
- Verification agent: <different stable identity>
- Acceptance agent: <third stable identity>
- In scope: <specific behavior and artifacts>
- Out of scope: <nearby tempting work>
- Owned paths: <non-overlapping ownership per identity>
- Authoritative evidence: <sources, fixtures, calculations, prior manifests>
- Acceptance evidence: <commands, artifacts, hardware/browser observations>
- Authority notes: <allowed actions and approvals required>
- Risks and unknowns: <resolve, defer, or request input>
```

For C2-B1, append this progress entry immediately after creating the new Cycle
2 progress file and before accepting any implementation. This entry is planning
state, not a machine-readable evidence manifest, and cannot satisfy a
checkpoint. Never rewrite the historical Cycle 1 progress record.

## Standard batch procedure

### 1. Select and bound

Select the earliest incomplete batch with satisfied prerequisites. Restate its
single outcome and apply the new-work scope test from
`CYCLE2_ORCHESTRATION.md`. Record unrelated or excluded findings in the Cycle 2
deferred list immediately.

### 2. Preflight

- Record `git status`, current branch, full HEAD, tree, and unrelated user
  changes.
- Confirm required sources, fixtures, tools, locks, prior manifests, and
  operator inputs.
- Rerun the narrow prior-checkpoint gate on which the batch depends.
- Resolve owned files and generated-file authority before assigning work.
- Identify dependency downloads, hosted CI, browser launch, and USB operations
  that may require normal execution approval.
- For hardware, recheck voltage, VRef, common ground, physical mapping,
  input/output direction, source loading, finite timeouts, and prohibited
  persistent operations.
- For the local server, confirm loopback-only binding, origin/token boundary,
  bounded requests, and cleanup before allowing device or filesystem actions.

If a prerequisite is absent, keep the batch pending or record the precise
blocker. Do not simulate CI, browser, operator, or hardware evidence.

### 3. Assign

Give each identity explicit:

- objective and acceptance criteria;
- files it may edit;
- files and features it must not edit or implement;
- authoritative sources and independently fixed literals;
- focused and accumulated commands;
- evidence record it must produce; and
- required handoff format.

Every handoff includes changed files, behavior, commands and exact results,
evidence provenance/digests, assumptions, discrepancies, deferrals, and
candidate/worktree state.

### 4. Implement and verify independently

The implementation agent first adds or identifies a focused failing test, then
makes the smallest in-scope change. The verification agent builds black-box or
independent checks without copying implementation algorithms into expected
results.

Examples of independent evidence include hard-coded wire bytes, separately
calculated masks, archive headers built without the production writer, browser
events observed through public UI/API behavior, and expected bus rows computed
from literal samples.

### 5. Integrate

The orchestrator checks:

- Cycle 2 scope and authority compliance;
- strict separation of physical channel IDs and packed request positions;
- explicit byte order, word width, padding, counts, and bounds;
- mode-appropriate dtype and zero upper byte for 24-channel words;
- deterministic replay/CSV/API schemas without executable metadata;
- loopback, canonical-Origin, capability-cookie, request-limit, and concurrency
  behavior;
- nonblocking server/browser lifecycle and cleanup;
- work proportional to visible transitions/pixels rather than all samples;
- no runtime Node/CDN, Qt, .NET, `.lac`, firmware, or excluded feature;
- tests that fail for the intended defect; and
- preservation of unrelated changes and accepted Cycle 1 behavior.

An interface change reopens its earliest owning checkpoint. Resolve conflicts
by preserving the approved contract and smallest behavior, never by weakening a
verifier expectation silently.

### 6. Run the validation loop

Run focused checks first, followed by the accumulated gates. Once C2-B1 freezes
the exact scripts, the canonical non-hardware gate is:

```bash
cd Software/LogicAnalyzerPy
python3.12 -m venv .venv
.venv/bin/python -m pip install --require-hashes -r requirements-dev.lock
.venv/bin/python -m pip install --no-build-isolation --no-deps -e .
.venv/bin/python -m pip check
.venv/bin/python -m ruff check .
.venv/bin/python -m mypy src
.venv/bin/python -m pytest -m "not hardware"
.venv/bin/python -m pico_logic_analyzer --help

cd web
npm ci
npm run lint
npm run typecheck
npm test -- --run
npm run build
npm run test:browser
```

If C2-B1 chooses different exact script names, it records the mapping and the
new canonical commands in the progress log and evidence schema. It may not
remove lint, type, unit/component, production-build, or headless-browser gates.

Run clean bootstraps for C2-B1, hosted CI, C2-B5, and C2-B6. A reused local
environment is valid only when Python/Node versions and both lock digests match
the checkpoint evidence. Production smoke uses prebuilt assets with network
access disabled and must not invoke Node.

Hardware and native-browser batches then run their explicit opt-in procedures.
Skipped required tests, manual inspection without recorded objective checks, or
an untested production build do not pass.

### 7. Record findings and acceptance

The verifier and acceptance agent each create an immutable review record under
`Software/LogicAnalyzerPy/docs/reviews/`. Every finding is numbered and records
evidence, requested resolution, and disposition. Corrections receive another
review; prior findings are not erased.

Only after the owning batch's implementation results, independent verification
evidence, and acceptance verdict exist, the orchestrator assembles and writes
that batch's machine-readable evidence manifest atomically and checks artifact
digests independently. The manifest must validate against the Cycle 2 schema
before the checkpoint record is appended. Mark the batch complete only after
all acceptance items pass, the validated manifest is committed, and the
checkpoint record is appended.

Do not create or pre-populate `c2-bN.json` for a future batch. A reserved
filename, placeholder, empty object, sample, or template is not evidence and
must not be described as accepted. C2-B1 creates only the schema, validator,
an optional explicitly non-evidence directory marker or template, and—after its
own evidence exists—its own atomic `c2-b1.json`. Each of C2-B2 through C2-B6
creates only its own manifest at the equivalent point in its owning batch.

### 8. Decide the next action

- Pass: checkpoint and select the next batch.
- Product defect: remain in the owning batch and iterate.
- Earlier regression: reopen the earliest owning checkpoint.
- Out of scope: record and defer.
- Authority or operator input needed: pause that path and continue only safe,
  independent in-scope work.

## Settled Cycle 2 contracts

These contracts are mandatory inputs to C2-B1/B2 documentation and tests.
Changing them substantively requires the preparatory review process or explicit
operator direction under the approved goal.

### Capture model and word modes

- `channel_ids` is an ordered tuple of 1-24 exact integers. Every ID is unique,
  within `0..23`, below the negotiated physical channel count, and serialized in
  that order. Boolean, float, string, duplicate, empty, and overlong values are
  rejected before transport construction or I/O.
- `trigger_channel` is an exact integer in `channel_ids`; edge is exactly
  `rising` or `falling`.
- Highest physical ID `0..7` selects firmware mode 0 and little-endian
  `uint8`; `8..15` selects mode 1 and little-endian `uint16`; `16..23` selects
  mode 2 and little-endian `uint32` carrying only 24 meaningful bits.
- Returned bit `i` represents request-list position `i`. Physical ID D`n` is
  never inferred from returned bit `n` unless the request order makes them
  equal. Capture results retain ordered physical IDs, labels, mappings, and
  packed bit positions independently.
- `samples` is rank-one, C-contiguous, native NumPy with the exact unsigned dtype
  for the selected mode. Every 24-channel word satisfies
  `word & 0xff000000 == 0`.
- Counts and timing retain Cycle 1 semantics:
  `requested_count = pre_trigger_samples + post_trigger_samples`, actual count
  and array length equal it, `trigger_index = pre_trigger_samples`, and time at
  index `i` is `(i - trigger_index) / sample_rate_hz`.
- Buffer validation uses bytes per word: the request and response must fit the
  negotiated byte buffer and applicable protocol count limits before allocation
  or reading. Do not compare a 16/24-bit word count directly with a byte count.
- Channel extraction is vectorized from packed request position. Do not
  materialize permanent per-channel Python integer lists.
- Labels and mappings are bounded exact strings, one per requested channel, and
  cannot alter physical identity or packed position.

### Wire codec

- The native capture payload remains the source-proven 48-byte structure and
  uses the accepted V2 frame delimiters and escaping.
- All 24 channel slots, count, mode, padding, trigger fields, frequency, pre,
  post, and other fixed fields have literal offset/byte fixtures. Firmware is
  authoritative for offsets, widths, and the fact that slots at or above the
  channel count are ignored. Canonical Python requests use host-defined zero
  bytes for every unused channel slot and explicit padding byte; fixtures prove
  that convention and frame escaping without claiming those zero values are
  firmware-required.
- Normal edge-trigger requests set `loopCount` at offset 44 and `measure` at
  offset 45 to zero. Timestamped and burst responses remain excluded.
- Capture responses consume a bounded status line, four-byte little-endian word
  count, exactly `count * bytes_per_word` payload bytes, and the accepted
  trailing non-burst timestamp-count byte, which must be exactly zero. Count and
  multiplication overflow are rejected before payload allocation/read. A
  nonzero timestamp count is a protocol error: reject it and any would-be
  timestamp payload before another request is permitted, then close/recover the
  transport so trailing binary bytes cannot contaminate a later exchange.
- One byte-oriented receive owner preserves coalesced ASCII/binary boundaries.
  Fragmentation from one byte through whole-response reads produces identical
  results.
- Recovery remains exactly the accepted Cycle 1 normal-capture path: one
  literal `0xFF` only after capture is in flight, a shared deadline and bounded
  drain, close, reopen, and re-identification. Wider support does not invent a
  new abort protocol.

### Replay schema 2

- The container retains the bounded inert NPZ design: exactly `samples.npy` and
  `metadata.npy`; metadata is rank-one `uint8` canonical UTF-8 JSON; samples are
  rank-one exact `uint8`, `uint16`, or `uint32`; `allow_pickle=False` always.
- Schema 2 records at least: schema version, sample dtype, firmware mode, sample
  rate, requested/actual/pre/post counts, trigger index/channel/edge, ordered
  physical channel IDs, labels, mappings, packed bit positions, and sanitized
  device identity/capabilities.
- Schema 2 keys, numeric/string/list limits, archive/member limits, compression,
  canonical JSON, NPY header versions, shape, byte order, dtype, counts, and
  cross-field invariants are frozen before implementation in C2-B1/B2.
- Limits accommodate the negotiated V2 Pico 2 maximum for each word width plus
  bounded metadata, without reverting to an arbitrary unbounded Cycle 1 sample
  maximum. Sparse ZIP claims, compression bombs, duplicate/path/encrypted
  members, oversized headers, unsupported byte order, object/structured/string
  dtypes, unknown required semantics, and noncanonical metadata are rejected
  before NumPy materialization where possible.
- New writes are schema 2. Valid schema 1 reads preserve their accepted Cycle 1
  meaning and produce the generalized in-memory model without rewriting the
  original file.
- Replay metadata cannot name, import, configure, or execute decoder/plugin
  code and contains no `.lac` compatibility payload.

### Self-timed CSV

- UTF-8, LF, RFC-4180-compatible comma separation, locale-independent numeric
  formatting, and deterministic row order remain required.
- The leading columns remain
  `sample_index,time_seconds,trigger`. Captured-channel columns then appear in
  request order and use their unique validated display labels under a frozen
  escaping/duplicate-label rule.
- Data values are `0` or `1` extracted by packed request position. The trigger
  flag and time-zero convention remain identical to Cycle 1.
- A generalized import is a CSV byte stream plus an explicit import-metadata
  object supplied by CLI options or the browser import form. The object contains
  exactly `channel_ids` in CSV column/request order, integer `sample_rate_hz`,
  `trigger_channel`, and `trigger_edge`. Display labels come from the CSV
  header; packed positions are `0..N-1`; firmware mode is derived from the
  highest physical ID; trigger index and pre/post/actual counts are derived from
  the sole trigger row and row count. The metadata object is subject to the same
  exact-type, uniqueness, membership, channel-count, string, and numeric bounds
  as a capture configuration. Neither a filename nor a label implies physical
  identity.
- The one legacy exception is the exact accepted Cycle 1 header
  `sample_index,time_seconds,trigger,D0,D1,D2,D3,D4,D5,D6,D7`: it supplies
  channel IDs D0-D7 in order. Its integer sample rate may be inferred as
  described below; trigger channel/edge must still be supplied because those
  facts are absent from CSV bytes. No other labels imply IDs.
- A browser CSV-open workflow uploads the bounded bytes, displays the header,
  and requires the operator to enter or confirm the metadata fields before
  import. It shows the physical-ID-to-packed-position mapping before accepting
  the import. CLI import requires equivalent explicit options.
- Import accepts only the exact supported self-timed contract. Decimal time
  cells use ASCII syntax `-?(0|[1-9][0-9]*)(\.[0-9]+)?([eE][+-]?[0-9]+)?` and
  must parse to finite values; leading plus, whitespace, `NaN`, and infinities
  are rejected. Indices are consecutive zero-based integers, there is exactly
  one trigger row whose parsed time is zero, and binary cells are `0` or `1`.
  For supplied rates, every time cell must equal the parsed value of
  `format((index - trigger_index) / sample_rate_hz, ".12g")`; validation uses
  exact decimal values rather than adjacent rounded-text differences. For the
  legacy header, form integer-rate candidates by rounding
  `abs(index-trigger_index)/abs(parsed_time)` for every nonzero row; exactly one
  in-range candidate must reproduce every canonical `.12g` time cell or import
  fails. Zero/one-row input therefore requires an explicit sample rate.
- Accepted imports are canonicalized on export using the frozen header/order,
  RFC-4180 escaping, LF, and `.12g` timing. Canonical exported CSV, including
  reordered/noncontiguous generalized captures and non-terminating sample
  periods, reimports and re-exports byte-identically. Noncanonical but otherwise
  accepted generalized input is not promised byte preservation.
- For the exact accepted D0-D7 configuration, Cycle 2 export remains
  byte-identical to Cycle 1.

### Parallel-bus analysis

- Data channels are a nonempty ordered tuple of captured physical IDs,
  interpreted least-significant bit first. They are unique and cannot include
  the distinct strobe channel.
- Transition mode emits a row at sample zero and whenever the packed bus value
  differs from the prior sample. Each row identifies its start sample/time,
  value, and the end sample/time or duration of the interval where applicable.
- Sampled mode emits a row only on the selected rising or falling transition of
  one distinct captured strobe channel. The bus value is taken from the sample
  at the selected edge index under the same trigger-relative timing convention.
  Sample index zero is never a sampled edge because there is no preceding
  captured strobe value; no synthetic prior level is assumed. Rising and
  falling transitions compare only samples `i-1` and `i` for `i >= 1`.
- Rows include sample index, trigger-relative time, binary with bus-width
  padding, fixed-width hexadecimal, unsigned decimal, and the mode-appropriate
  interval fields. Exact headers and numeric formatting are frozen in C2-B4.
- CLI/API CSV is deterministic and produced from the Python analysis core. The
  React client displays returned rows and does not independently reinterpret raw
  samples into a conflicting bus result.
- Empty captures, one-sample captures, no transitions, initial high and low at
  index zero for both selected polarities, later rising/falling edges, absent
  edge, noncontiguous/reordered channels, bus widths not divisible by four, and
  maximum bounded row counts have explicit tests.

### Local web application boundary

- The production command, exact startup/readiness output, shutdown behavior,
  browser URL, and exit codes are frozen in C2-B1. It binds an OS-assigned or
  explicit loopback port; wildcard and non-loopback addresses are rejected.
- Production serves checked-in or packaged Vite build assets. It neither starts
  a Vite development server nor invokes Node.
- At bind time the server constructs one canonical origin from its configured
  literal loopback address and actual port; it never derives that origin from
  `Host`, `Forwarded`, or `X-Forwarded-*` request headers. Requests with a Host
  authority different from that canonical authority are rejected and redirects
  never carry the capability. Wildcard, non-loopback, and alternate Host forms
  are not aliases.
- On the initial canonical top-level HTML response the server delivers the
  per-launch capability only as a host-only, `HttpOnly`, `SameSite=Strict`,
  `Path=/` cookie. It never places the capability in a URL, query, fragment,
  HTML/JavaScript body, browser storage, API body, error, redirect, log, or
  evidence. The cookie expires when the server process ends and is explicitly
  expired during orderly shutdown. Browser code uses same-origin credentials
  and cannot read the token.
- API paths are versioned under `/api/v1/`. Health/readiness and static reads are
  inert. Every state-changing endpoint, including capture, cancel, import,
  export generation, and shutdown, requires the cookie and an `Origin` exactly
  equal to the canonical origin. Token comparison is constant-time. Missing,
  malformed, duplicated, expired, or invalid cookies and missing, `null`,
  opaque, malformed, or foreign Origin values are rejected before work begins.
  WebSocket upgrades, if retained, require the same exact Host, Origin, and
  cookie checks before upgrade and on every new connection.
- No CORS headers or credentialed cross-origin policy are emitted. `OPTIONS`
  does not grant cross-origin access. Capability values are never echoed; test
  logs, exceptions, snapshots, URLs, Referer observations, API responses, and
  committed evidence are scanned for the launch value and must contain none.
- Tokens, machine paths, serial ports, and local URLs are not logged to committed
  evidence. Browser-visible errors are bounded and do not expose tracebacks or
  secrets; detailed diagnostics remain sanitized server-side.
- Only one physical capture/recovery operation owns a serial device at a time.
  Conflicting requests receive a deterministic bounded error rather than queue
  indefinitely. Disconnect/cancel closes resources and leaves the board
  recoverable under the accepted lifecycle.
- Browser file import accepts only bounded uploaded bytes using the frozen
  multipart field and media type; client filenames are ignored except for a
  bounded display label and never become paths. `Content-Length` is checked when
  present and streaming accounting aborts before the upload limit is exceeded;
  malformed multipart, extra parts, cancellation, and disconnect discard all
  buffered or temporary data. Import creates no persistent server-side file.
- Export returns bounded bytes as an HTTP download with a server-generated,
  sanitized filename and fixed safe `Content-Type`/`Content-Disposition`.
  Browser input cannot supply a server path, output directory, absolute name,
  traversal component, overwrite target, or symlink. Export creates no
  persistent server-side file; the browser's user-selected download destination
  is outside the server API contract. Tests cover traversal/symlink-like names,
  overwrite attempts, malformed multipart, declared and streamed quota excess,
  cancellation/disconnect, generated response headers, and zero temporary-file
  residue.
- JSON bodies, response sample windows, bus rows, request rates/connections, and
  server shutdown have explicit limits.
- Waveform data is windowed and transition-reduced. The server/browser boundary
  must not require transmitting every sample for every pan or creating a DOM
  object per sample/transition.
- TypeScript API request/response types are checked against Python-owned schema
  fixtures or generated from one reviewed machine-readable contract. Hand-
  maintained duplicate schemas require drift tests.

### Rendering and interaction

- React owns application state and controls; Canvas owns waveform pixels. DOM
  nodes scale with channels and controls, not samples or transitions.
- Pure viewport and geometry functions define sample/time/pixel transforms,
  visible windows, transition reduction, cursor-centered zoom, clamping, trigger
  marker, channel layout, and cursor value lookup.
- Rendering is bounded by visible channels, viewport pixels, and reduced visible
  transitions. Constant and dense captures remain defined at extreme zoom.
- Primary assertions use pure geometry, Canvas command invariants, DOM state,
  and browser-observed behavior. Pixel screenshots may supplement but do not
  replace deterministic assertions.
- Blocking serial/file work never runs on the browser event loop or blocks the
  Python server's request loop. Progress, cancellation, disconnect, and recovery
  have explicit states.

## Stopping-condition ownership

Every governing stopping condition has one earliest owning batch. Later batches
rerun dependent gates but do not silently take ownership from an incomplete
earlier batch.

| `CYCLE2_ORCHESTRATION.md` condition | Earliest owner | Final proof |
| --- | --- | --- |
| 1. Python/Cycle 1 installation and regression | C2-B1 | C2-B6 clean accumulated gate |
| 2. Locked frontend checks and production build | C2-B1 | C2-B6 clean build |
| 3. macOS/Linux CI matrix | C2-B1 | C2-B6 exact-candidate CI |
| 4. Literal 8/16/24 protocol fixtures | C2-B2 | C2-B6 fixture regression |
| 5. Adverse fake/replay/API/browser lifecycle | C2-B2, completed through B5 | C2-B6 accumulated gate |
| 6. Replay 1/2 and generalized CSV | C2-B2 | C2-B6 artifact audit |
| 7. Parallel-bus analysis | C2-B4 | C2-B6 API/UI/export audit |
| 8. D0/D8/D16/D23 physical masks | C2-B3 | C2-B6 live-display reuse |
| 9. Cycle 1 physical recovery regression | C2-B3 | C2-B6 lifecycle audit |
| 10. Offline browser workflow | C2-B5 | C2-B6 native regression |
| 11. Native macOS live workflow | C2-B6 | C2-B6 acceptance record |
| 12. Rendering baseline and thresholds | C2-B5 | C2-B6 enforcement result |
| 13. Final evidence and support claim | C2-B6 | Cycle 2 completion record |
| 14. Rollback paths and prohibited-action audit | C2-B1 onward | C2-B6 final audit |

## Cycle 2 batch sequence

### C2-B1: Contracts, dependencies, workflow, and web shell

**Outcome:** A reproducible Python/React development and CI foundation exists;
all Cycle 2 data/API/security contracts are frozen; a production-built,
loopback-only offline shell starts and stops without serial access.

**Prerequisites:** Approved Cycle 2 preparatory documents and common-commit
reviews; accepted Cycle 1 baseline; writable workspace.

**In scope:**

- Create the Cycle 2 progress log, evidence-schema extension, frontend
  directory, package metadata, lock, test configuration, and asset build/install
  path. Freeze the strict Cycle 2 schema version, required fields, validator
  command, recursive no-extra-properties policy, and secret scan specified by
  the orchestration contract before accepting any B1 evidence. Create the B1
  evidence manifest atomically only after B1 verification and acceptance
  evidence exists; do not create B2-B6 manifests.
- Select and pin the supported Node runtime and minimal Python HTTP/WebSocket
  stack after clean macOS/Linux probes. Use React, TypeScript, Vite, and a
  browser automation stack. Record licenses and direct/transitive lock digests.
- Expose the Python server stack as an optional `web` project extra while
  including the exact same versions in the reviewed development lock. Create a
  hash-checked `requirements-web.lock` containing the complete web runtime
  closure. The supported runtime installation is
  `pip install --require-hashes -r requirements-web.lock` followed by
  `pip install --no-build-isolation --no-deps -e '.[web]'`; it performs no
  dependency resolution after the lock. CLI/library installation without that
  extra remains valid; invoking `pico-la web` without it gives an actionable
  deterministic error.
- Commit deterministic production frontend assets plus a build manifest and
  make CI fail when a clean frontend rebuild differs from them. Production
  source execution uses those assets and requires neither Node nor network.
- Freeze capture/replay/CSV/bus/API/server/render/performance contracts in ADRs
  or focused documents matching the settled section above.
- Add a loopback-only `pico-la web` shell with readiness, the canonical-Origin
  and capability-cookie policy, inert health, production assets, and
  deterministic shutdown. It must not import/open serial or accept capture
  requests yet.
- Rename/replace the single Cycle 1 workflow with one Cycle 2 macOS/Linux matrix
  running the canonical clean Python and Node/frontend gates. Preserve Cycle 1
  tests and avoid duplicate full workflows.
- Correct stale Cycle 1 wording in project metadata and active documentation
  without rewriting historical completion/review records.

**Out of scope:** Wider codec/model implementation, replay schema 2 production
I/O, capture API, waveform behavior beyond an inert shell, hardware, Qt,
Electron, `.lac`, .NET, packaging, or public serving.

**Acceptance:**

- Clean Python 3.12 and pinned Node bootstraps succeed from both locks.
- `npm ci`, lint, typecheck, unit/component tests, production build, and a
  headless start/readiness/shutdown smoke pass.
- Production starts with network disabled, uses built local assets, and does not
  invoke Node or a development server.
- Non-loopback binds; alternate/forged Host; absent, duplicated, expired, or
  invalid capability cookie; absent/null/opaque/foreign Origin; invalid
  WebSocket upgrade; permissive preflight; oversized requests; and duplicate
  server ownership fail deterministically without serial I/O. Independent tests
  prove the token never appears in URLs, Referer, browser-visible state, logs,
  errors, responses other than its initial `Set-Cookie` header, snapshots, or
  evidence and that shutdown expires the cookie.
- Core/CLI installation remains possible without Node at runtime.
- Core/CLI installation remains possible without Python web dependencies; the
  `web` extra path and missing-extra diagnostic are tested.
- Clean macOS and Linux CI jobs install the web runtime through
  `requirements-web.lock`, perform the no-deps source install, run `pip check`,
  and record the runtime-lock digest separately from the development lock.
- The Cycle 2 evidence schema and secret scanner accept the complete B1
  manifest, reject extra/missing/secret-bearing fields, and require all three
  role identities even in B1.
- The exact Python/frontend canonical commands and supported versions are
  documented.
- The renamed/replaced workflow passes macOS and Linux jobs at the exact
  checkpoint commit; pushing to obtain CI evidence requires normal user
  authority.
- All accumulated Cycle 1 non-hardware tests pass.
- No Qt, embedded browser, `.lac`, .NET, firmware, or hardware operation occurs.

### C2-B2: Wider capture domain, codec, replay, and CSV core

**Outcome:** Pure Python code safely represents, encodes, parses, persists, and
reloads ordered 1-24-channel normal captures across all three word modes.

**Prerequisite:** C2-B1 complete.

**In scope:**

- Generalize `CaptureConfig`, `CaptureResult`, capability validation, and
  extraction utilities under the settled model.
- Generalize the 48-byte normal request and response parser for mode 0/1/2.
- Add literal request/response fixtures for contiguous and reordered subsets,
  reserved bytes, every word width, and invalid bounds. Host-defined canonical
  zero slots/padding are identified as such rather than source-derived.
- Implement canonical replay schema 2 writer/reader plus retained schema 1
  reads and all pre-materialization security checks.
- Generalize deterministic self-timed CSV export and add its exact importer.
- Update CLI capture/replay validation only as necessary to expose approved
  ordered channels and artifacts while preserving explicit port/output and exit
  contracts.

**Out of scope:** Physical I/O beyond fake transport, bus analysis, web capture
API, viewer, performance optimization, other firmware modes, or decoders.

**Acceptance:**

- Independent literal golden packets prove offsets, padding, modes, slot order,
  escaping, count, and little-endian sample bytes.
- Exact-type, uniqueness, range, trigger-membership, negotiated-channel,
  sample-rate, byte-buffer, multiplication-overflow, count, dtype, rank,
  contiguity, and upper-byte validation pass before unsafe I/O/allocation.
- One-byte and coalesced fragmentation, truncation, extra data, malformed status,
  timeout, disconnect, and cleanup tests pass for every word width. Literal
  adverse responses at every width include a nonzero timestamp-count byte plus
  its would-be four-byte-per-count payload; the parser rejects them, invalidates
  the receive owner, and cannot issue a subsequent request on the contaminated
  transport.
- Schema 1 reads still pass; schema 2 round-trips all modes and ordered subsets
  deterministically; hostile NPZ/NPY/JSON cases are bounded and inert.
- CSV imports/exports all widths/subsets deterministically; exact D0-D7 Cycle 1
  output remains byte-identical.
- Full accumulated Python/frontend shell gates pass without hardware.

### C2-B3: Physical byte-boundary capture gate

**Outcome:** The fixed real Pico 2 and Python implementation prove genuine
8/16/24-bit capture through the first and last upper-byte boundaries.

**Prerequisites:** C2-B2 complete; explicit port; operator confirms protected
3.3 V, common ground, D0/D8/D16/D23 mapping and input direction, and safe source
fan-out; D1/GPIO3 remains fixed low at analyzer ground or another explicit
fixed-level idle input is confirmed for recovery.

**In scope:**

- Re-run accepted Cycle 1 identity, D0 capture, fixed-idle recovery, close/reopen,
  re-identification, and second capture before or as part of the wiring change.
- Record the wiring transition and connect the approximately 1 kHz source to D0,
  D8, D16, and D23 simultaneously.
- Run D0-D7, D0-D15, and D0-D23 rising-edge captures using conservative valid
  parameters. Unless source/device evidence requires amendment, use the accepted
  Cycle 1 baseline of 100000 samples/s, 2048 pre, and 4096 post; record any
  change and rationale before I/O.
- Validate driven-bit projections, word width/dtype, counts, timing/frequency,
  artifacts, upper byte, close/reopen, and reuse without power cycle.

**Physical interpretation:**

- For D0-D7, driven mask is `0x01`.
- For D0-D15, driven mask is `0x0101`.
- For D0-D23, driven mask is `0x810101`.
- On the driven-bit projection, both all-low and all-high states occur and
  requested rising transitions are observed near 1 kHz within an independently
  calculated sampling/source tolerance.
- Other bits are ignored unless the operator has tied them to a fixed level.
  Floating activity is recorded, not treated as proof or failure.
- Every 24-channel raw word has bits 24-31 zero.

**Out of scope:** Firmware changes/reflash, probing unknown pins, requiring
floating inputs to be zero, performance-limit exploration, browser UI, or new
capture modes.

**Acceptance:**

- Operator/electrical/mapping confirmation is recorded before the request.
- Sanitized evidence records `<PORT_SUPPLIED>`, fixed firmware identity, exact
  settings, masks, counts, dtype, transitions, measured frequency/tolerance,
  upper-byte result, and artifact digests.
- Independent validation reads the raw schema-2 artifacts rather than trusting
  command success and reconstructs deterministic CSV.
- Accepted Cycle 1 recovery and second capture pass without a power cycle.
- All non-hardware gates remain green.
- No firmware, bootloader, Wi-Fi, power-cycle, or persistent device action
  occurs; the final wiring state is recorded.

### C2-B4: Parallel-bus core and versioned browser API

**Outcome:** Deterministic bus analysis and a bounded, secured API expose
offline captures without serial or UI-domain duplication.

**Prerequisite:** C2-B3 complete; B2 schemas and physical artifacts accepted.

**In scope:**

- Implement transition and distinct-strobe sampled bus analysis and CSV under
  the settled contract.
- Expose versioned endpoints for health/readiness, bounded replay/CSV import,
  capture metadata, channel state, waveform windows/transitions, bus tables,
  deterministic export, operation status/cancel, and shutdown.
- Share Python capture/replay/export/bus authority; TypeScript consumes the
  versioned contract rather than recomputing domain results.
- Add fake/replay tests for token/origin, bounds, malformed JSON/files,
  pagination/windowing, conflicts, disconnect, cancellation, cleanup, every
  capability-cookie/Host/Origin/WebSocket negative case, and the upload/download
  file boundary frozen above.
- Generate or validate TypeScript types against one reviewed API schema.

**Out of scope:** Real serial API, complete viewer interaction, performance
thresholds, remote serving, authentication for remote users, or decoders.

**Acceptance:**

- Independent bus fixtures prove LSB order, noncontiguous and reordered physical
  IDs, transitions, both strobe edges, trigger-relative time, formatting,
  intervals, empty/no-edge limits, and deterministic CSV.
- Browser API cannot mutate state without the valid capability cookie and exact
  canonical Origin; non-loopback/public access remains unreachable. Import and
  export accept no server paths and leave no persistent or temporary file.
- Uploads, JSON, sample windows, row counts, connections, and concurrent
  operations are bounded and return deterministic errors.
- Schema drift tests bind Python responses to TypeScript types.
- API replay/CSV results match direct Python-core results byte/value-for-value.
- Accumulated Python/frontend/headless shell gates pass; no serial device opens.

### C2-B5: Offline browser viewer and performance-threshold checkpoint

**Outcome:** The production React application provides a useful, bounded offline
8/16/24-channel waveform and bus workflow, and evidence-based performance
thresholds are frozen.

**Prerequisite:** C2-B4 complete.

**In scope:**

- Open schema-1/schema-2 replay and supported self-timed CSV through the bounded
  API.
- Display channel labels/visibility, digital waveforms, horizontal pan,
  cursor-centered zoom, trigger marker, cursor sample/time/value readout,
  transition/strobe bus table, and deterministic export.
- Implement explicit loading, ready, empty, error, disconnected, cancelling,
  and shutdown states.
- Test pure geometry, Canvas command invariants, React state/components, browser
  keyboard/pointer interaction, API failures, reconnect, and cleanup.
- Benchmark approved empty, constant, sparse, dense, maximum 8/16/24-channel,
  and bus-table fixtures on the primary macOS host and record comparable CI
  observations.

**Performance threshold procedure:**

1. Freeze fixture digests, viewport, device-pixel ratio, browser/version,
   machine/OS, production-build digest, warm-up, iteration count, and timing
   collection method before measuring.
2. Measure initial load/paint and repeated pan/zoom using multiple iterations;
   report median and a high percentile, sample/transition counts, payload size,
   and memory where reliable.
3. The orchestrator proposes absolute primary-macOS usability ceilings and
   regression tolerances for the stable measurements. Shared-CI timing is
   informational unless a repeatable relative method is demonstrated.
4. The verification agent independently reproduces the method and checks that
   fixtures include worst-case dense and maximum-width cases.
5. The acceptance agent records `pass` or `changes_required` for the proposal.
6. The operator approves or amends the threshold record. Commit the immutable
   approved record and digest before C2-B5 becomes complete.
7. C2-B6 enforces the approved thresholds without silently rebasing them.

**Out of scope:** Serial/live capture, arbitrary million-row DOM tables,
pixel-perfect screenshot gates, packaging, public server, or subjective-only
performance acceptance.

**Acceptance:**

- Offline user workflows pass in the production build on macOS/Linux headless
  CI, including all three widths and both bus modes.
- Browser data transfer and Canvas work are bounded by the visible window and
  reduced transitions; DOM size does not scale with raw sample count.
- Malformed/oversized files, server loss, failed export, and cancelled
  operations leave no false success or partial final artifact.
- Production runtime works without Node, CDN, serial import/open, or development
  server.
- Baseline evidence is reproducible and the operator-approved threshold record
  is committed.
- Clean accumulated Python/frontend/browser gates pass.
- Browser automation proves token non-disclosure in its location/Referer,
  storage, DOM, console/network logs, errors, and snapshots while protected
  requests still succeed through the host-only HttpOnly cookie.

### C2-B6: Live browser capture integration and final proof

**Outcome:** The production browser application completes the real macOS
capture/view/analyze/export/reconnect workflow and every Cycle 2 stopping
condition has independent evidence.

**Prerequisite:** C2-B5 complete with approved thresholds; physical setup and
explicit port remain operator-confirmed.

**In scope:**

- Connect the secured API to the existing explicit-port device service through
  nonblocking worker/task ownership.
- Identify, capture, cancel/recover where required by regression proof,
  close/reopen/re-identify, and capture again without a power cycle.
- Display and inspect the approved 8/16/24 physical pattern, bus table, trigger,
  cursor values, and deterministic exports in an installed native macOS browser.
- Enforce C2-B5 performance thresholds on the frozen reference method.
- Run clean accumulated local/CI gates at one final candidate.
- Complete independent implementation verification, acceptance, manifests,
  rollback audit, support qualification, and final handoff.

**Out of scope:** Feature polish unrelated to a stopping condition, native Linux
hardware claims, firmware tuning, remote access, packaging, decoders, Cycle 3,
or threshold rebasing.

**Acceptance:**

- The exact final commit/tree passes clean Python/Node bootstraps and every
  accumulated test on macOS/Linux CI.
- Native macOS production-build startup, browser interaction, real capture,
  waveform, bus, export, close/reopen, second capture, and shutdown pass with
  sanitized evidence.
- Device/API concurrency, browser disconnect, cancellation, timeout, server
  shutdown, and serial cleanup are independently verified.
- Final security regression repeats the canonical Host/Origin/cookie,
  WebSocket, token-redaction, bounded upload/download, cancellation, and
  zero-residue checks against the production build.
- The final candidate meets the approved rendering thresholds.
- Every stopping condition in `CYCLE2_ORCHESTRATION.md` maps to an immutable
  evidence path and digest.
- `docs/cycle-2-completion.md` accurately limits Linux support to CI and records
  native Linux hardware/desktop evidence as deferred.
- Firmware/C# sources and Cycle 1 regression paths remain; no prohibited action
  occurred; repository state is recorded; Cycle 3 has not begun.

## Checkpoint record template

Append one record after each accepted batch:

```markdown
### Checkpoint C2-BN — <name>

- State: Complete
- Completed at: <ISO-8601 UTC timestamp>
- Tested commit: <full commit hash>
- Tested tree: <tree hash>
- Worktree state: <clean or explicitly enumerated unrelated changes>
- Implementation agent: <stable identity>
- Verification agent and verdict: <different identity; pass>
- Acceptance agent and verdict: <third identity; pass>
- Environment: <OS/arch, Python, Node, browser as applicable>
- Dependency identity: <development Python lock SHA-256; web-runtime Python
  lock SHA-256; JS lock SHA-256>
- Build identity: <production asset manifest/digest as applicable>
- Objective evidence: <tests, artifacts, observations>
- Files changed: <paths or concise groups>
- Focused commands: <command and exact outcome>
- Accumulated commands: <command and exact outcome>
- CI evidence: <run/jobs/exact commit, or not applicable>
- Hardware evidence: <sanitized summary, or not applicable>
- Browser evidence: <sanitized summary, or not applicable>
- Performance evidence: <record/digest, or not applicable>
- Evidence manifest: <path and SHA-256; Cycle 2 schema-validation command/result>
- Findings and dispositions: <review record links>
- Decisions/discrepancies: <settled behavior and provenance>
- Deferred findings: <destination>
- Known limitations: <remaining constraints>
- Repository state: <commit/worktree summary>
- Next batch: <identifier and unmet inputs>
- Blocked: no
```

Failed attempts remain concise history under the active batch; they are not
false completed checkpoints.

## Independent verification expectations

Verification derives expected behavior independently:

- Hard-code reviewed 8/16/24 request and response bytes rather than using the
  encoder to create expected fixtures.
- Calculate packed request-position masks separately from model helpers.
- Feed status/count/payload/trailer in adversarial fragment boundaries and
  corrupt byte counts before allocation.
- Construct hostile ZIP/NPY/JSON and CSV cases without the production writers.
- Reload output through independent standard-library/NumPy paths with pickling
  disabled and verify canonical bytes/digests.
- Calculate physical masks and frequency tolerance from declared sample rate,
  source stability, and transition spans rather than trusting success JSON.
- Compare API responses with direct Python core results through independently
  parsed schema fixtures.
- Exercise the production Vite build in a browser with runtime network disabled.
- Verify pan/zoom/cursor transforms using fixed mathematical examples, not the
  same geometry function used by rendering.
- Inspect Canvas command counts and DOM size against viewport/channel bounds;
  do not rely solely on screenshots or human judgment.
- Reproduce the C2-B5 performance method before approving its thresholds.

Ambiguous evidence is reported before changing expected behavior. If a finding
requires an objective, scope, authority, batch, or stopping-condition change,
pause and use the common-commit document-review process.

## Regression and rollback procedure

When a completed checkpoint regresses:

1. Identify the earliest owning checkpoint.
2. Mark it `In progress` with the regression evidence; do not erase history.
3. Pause dependent interface expansion and acceptance.
4. Apply the smallest correction in the owning surface.
5. Obtain independent verification and acceptance again.
6. Rerun that checkpoint and every dependent accumulated gate.
7. Append a correction record and new evidence digest.

Rollback means returning to the prior accepted Python commit or using the
existing application/firmware operationally; it never authorizes modifying or
deleting firmware or the C# source tree.

## Hardware and external-action checklist

Before USB, native-browser, dependency, or hosted-CI action, confirm:

- [ ] The operation is within the active batch and has an explicit evidence
      owner.
- [ ] The exact port comes from the operator and will be sanitized as
      `<PORT_SUPPLIED>`.
- [ ] Board, firmware, protection, 3.3 V VRef, common ground, pin mapping,
      input direction, and source fan-out are confirmed for physical capture.
- [ ] A fixed-level, non-floating idle input is operator-confirmed before the
      Cycle 1 recovery regression.
- [ ] The only device commands reachable are identity, approved normal capture,
      and the accepted one-byte recovery sequence when capture is in flight.
- [ ] No bootloader, flash, Wi-Fi, persistent mutation, power-cycle demand, or
      firmware build path is reachable.
- [ ] Timeouts, cancellation, drain caps, close, and cleanup exist before I/O.
- [ ] The local server is loopback-only with token/origin checks and bounded
      inputs; no token/path/URL enters committed evidence.
- [ ] Dependency versions and locks are resolved; runtime assets need no CDN or
      Node process.
- [ ] Normal execution approval has been requested where the environment or
      user authority requires it.

## Cycle 2 final review packet

Before declaring C2-B6 complete, assemble links to:

- all fourteen `CYCLE2_ORCHESTRATION.md` stopping conditions;
- six checkpoint records and manifests;
- implementation, verification, and acceptance review records;
- literal protocol fixtures and provenance;
- schema-1/schema-2 replay and CSV determinism/security evidence;
- bus-analysis fixtures and exports;
- accumulated Python/React/API/browser results and exact macOS/Linux CI jobs;
- operator confirmation and sanitized D0/D8/D16/D23 physical evidence;
- Cycle 1 hardware recovery regression and Cycle 2 second-capture evidence;
- native macOS browser workflow evidence;
- rendering baselines, approved thresholds, and final measurements;
- dependency/build digests, repository status, rollback audit, limitations, and
  deferrals; and
- confirmation that firmware, .NET, `.lac`, public serving, packaging,
  publishing, native Linux hardware claims, and Cycle 3 remained untouched.

Preparatory review of this document and `CYCLE2_ORCHESTRATION.md` occurs before
the durable goal. The packet above is instead the final completion evidence; it
must pass before the Cycle 2 goal is marked complete.
