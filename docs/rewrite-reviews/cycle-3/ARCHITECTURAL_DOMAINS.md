# Cycle 3 architectural reviewer charters

All three reviewers inspect the applicable complete common-commit document set
defined in `README.md`. Domain ownership determines primary attention, not a
license to skip another document or ignore a cross-domain defect. These
charters govern preparation document review only and grant no Cycle 3
implementation, decoder-execution, dependency, hardware, or durable-goal
authority.

## Common invariants for all reviewers

- Cycle 3 is limited to the exact hash-pinned checked-in UART, SPI, and I2C
  decoder snapshots, compatibility shim, and required helper files.
- Independently derived, human-reviewed fixtures are the sole authoritative
  oracle for expected annotations and all other decoder outputs. A fixture
  generator must not consume production-host output, decoder runtime output,
  C# output, libsigrokdecode output, or another reference executable's output.
- C# and upstream sources may be inspected as inert text only. C#, .NET,
  pythonnet, libsigrokdecode, `sigrok-cli`, and every external/reference decoder
  runtime must not execute or become a dependency in production, development,
  tests, fixture generation, verification, performance work, acceptance, or
  review.
- The prohibition on libsigrokdecode runtime/dependency does not prohibit the
  later approved native host from executing the three exact checked-in decoder
  snapshots after the approved goal starts. It prohibits installing, importing,
  or invoking an external libsigrokdecode host, runtime, library, package, CLI,
  or reference implementation.
- Preparation and document review execute no decoder. Numeric limits remain
  governed by the baseline, independent review, acceptance, and explicit
  operator-approval order frozen in discovery.
- Browser decoder UI/API work, physical capture proof, firmware/hardware/serial
  changes, live decode, dynamic decoder discovery, stacking, `.lac`, packaging
  or publication, and support beyond macOS are excluded.
- Every substantive correction receives all-three review on one new complete
  common commit and tree. No pass transfers across a candidate or gate.

## Reviewer 1: decoder API, runtime, fixtures, and provenance

### Scope

Owns the closed executable snapshot, provenance and hashes, decoder/helper
import graph, focused API-v3 compatibility semantics, declarative timelines,
fixture independence and correctness, decoder metadata/options/channels, and
UART/SPI/I2C conformance proof design. This reviewer follows the seam from a
validated decoder request into the compatibility layer and from emitted calls
into the typed raw output records, without owning process containment or the
public CLI workflow.

### Required inspection

- The applicable exact complete document set at the supplied commit and tree.
- `Software/decoders/sigrokdecode.py`, focused `uart`, `spi`, and `i2c`
  `__init__.py`/`pd.py` files, and required `common/srdhelper` files, by static
  inspection only.
- Relevant inert Git provenance, attribution/license headers, and frozen file
  digests.
- The accepted capture model and replay/CSV semantics needed to understand
  channel mapping, samplerate, sample indices, and fixture inputs.
- C# bridge or upstream source only when static inspection is necessary to
  evaluate a claim; never build, import, load, or execute it.

### Review invariants

- Public decoder IDs resolve through one host-owned constant table; caller,
  capture, path, environment, or metadata cannot nominate executable code.
- File/hash and import allowlists are exact and fail closed. The promised
  API-v3 surface is no broader than the calls used by the approved snapshots.
- Lifecycle, `has_channel()`, `wait()`/`matched`/`samplenum`/skip,
  `register()`, `put()`, termination, sample-coordinate, and emission-order
  semantics are explicit, internally consistent, and objectively testable.
- Decoder-specific mappings, option defaults/domains, declarations, and all
  annotation, Python, binary, and metadata output shapes are complete.
- The absent optional pin is exact integer `0xFF`; tuple and `has_channel()`
  semantics plus UART RX-only/TX-only and SPI MISO-only/MOSI-only/no-CS
  fixtures are explicit. A closed matrix classifies every option default,
  enumeration, numeric boundary, and sentinel as direct fixture, justified
  static equivalent, or unsupported pre-launch rejection.
- Expected results are independently calculated from declarative sample
  timelines and checked-in source semantics. Fixtures remain independent of
  implementation and runtime output and are byte-reproducible.
- The five unresolved API-edge choices are frozen by reviewed fixture content
  before general host implementation. No prohibited reference execution is a
  prerequisite or corroborating oracle.
- Provenance claims distinguish proven identity from inference, preserve
  notices, and require the project/legal packaging disposition without making
  an unsupported legal conclusion.

### Explicitly delegated

Reviewer 2 owns capture-to-public-result consumption, annotation presentation,
library/CLI contracts, and inherited workflow determinism. Reviewer 3 owns
worker containment, executable-code security, dependency/license delivery
gates, platform/CI, performance/resource governance, evidence mechanics, and
orchestration authority.

## Reviewer 2: capture, annotations, deterministic data, library, and CLI workflows

### Scope

Owns the handoff from accepted `CaptureResult` data through decoder request and
typed `DecodeResult` semantics to the public synchronous library and installed
offline CLI. It owns deterministic channel/time/result representation,
replay/CSV equivalence, canonical serialization, errors/exits, documentation,
and the absence of an unapproved API/browser decoder surface.

### Required inspection

- The applicable exact complete document set at the supplied commit and tree.
- Current Python capture, replay, CSV, analysis, CLI, and public type contracts,
  plus representative accepted tests and Cycle 1/Cycle 2 evidence interfaces.
- Existing web API/OpenAPI/frontend boundaries only to confirm unchanged Cycle
  2 regression coverage and that Cycle 3 adds no decoder endpoint, type,
  renderer, operation, interaction, fixture, dependency, or launch requirement.
- Focused decoder metadata and proposed authoritative fixture/result schemas by
  static inspection; no decoder or reference runtime execution.

### Review invariants

- Physical channel IDs remain distinct from packed positions; mapping is
  explicit, complete, validated, and capture-source independent. Samplerate and
  trigger/sample identity come only from the validated inert capture.
- Replay schema 1/2, explicit-metadata CSV, and in-memory captures converge on
  one semantic path and yield byte-identical canonical results for equivalent
  data.
- The CLI carries ordered CSV physical channel IDs, samplerate/legacy-inference
  rule, trigger channel, and edge explicitly and separately from decoder
  channel mappings, with exact presence, exclusion, precedence, and validation.
- The typed result preserves declarations, complete output kinds, immutable
  values, integer sample coordinates, rational time, and request-wide emission
  order. Presentation views cannot rewrite the authoritative record order.
- The separately versioned result/error schemas freeze every field, type, tag,
  ordering rule, rational-time representation, base64 representation, and
  failure class; independently authored expected typed objects and literal CLI
  bytes exist before product result/CLI implementation.
- Python-output normalization is closed, bounded, tagged, deterministic, and
  rejects unknown, cyclic, or non-finite values instead of stringifying them.
- The public library delegates to exactly one isolated host path and cannot
  weaken limits or select code. The CLI grammar, option coercion, stdout JSON,
  stderr diagnostics, and exit meanings are complete and machine-testable.
- Capture/replay/CSV artifacts remain inert and cannot name executable code.
  The CLI is offline only and does not silently open serial, start web, accept
  code from stdin, or add export/live-capture behavior.
- Independently derived reviewed fixtures, never production or reference
  runtime output, are the sole expected-output oracle used across library and
  CLI proof.
- Existing core/CLI/web behavior remains regression-protected, while browser
  annotation/API behavior stays explicitly excluded rather than ambiguously
  untested.

### Explicitly delegated

Reviewer 1 owns decoder-source/API-v3 correctness, snapshot provenance, and
literal fixture semantics. Reviewer 3 owns subprocess/IPC containment,
resource enforcement, prohibited dependencies/executables, licensing delivery,
platform/CI, evidence ordering, and orchestration governance.

## Reviewer 3: executable-code security, delivery, evidence, and orchestration

### Scope

Owns executable-code trust, single-use subprocess isolation, launch/import
environment, framed IPC, validation and failure isolation, parent-enforced
deadline/cancellation/resource/retention bounds, cleanup, dependency and
license delivery policy, macOS/CI claims, performance governance, immutable
evidence, role separation, batch/checkpoint mechanics, and the durable-goal
plan-to-proof seam.

### Required inspection

- The applicable exact complete document set at the supplied commit and tree.
- Repository instructions and the parent review protocol.
- Current Python/Node dependency and lock metadata, CI configuration, evidence
  schemas/validators, accepted Cycle 1/Cycle 2 manifests, performance method,
  and completion records.
- Decoder/import sources, C# project/bridge metadata, and upstream provenance
  only as inert text needed to audit boundaries; do not install or execute any
  prohibited runtime, dependency, project, package, or decoder.

### Review invariants

- Exactly one bounded objective, five dependency-ordered batches, R1-R26
  earliest/final ownership, and the 18-item objectively verifiable stop remain
  mutually traceable with no circular or missing gate.
- Only a host-owned hash/import allowlist can execute after goal authority.
  Isolation is described narrowly: one fresh worker per request is a bounded
  containment boundary, not a general Python sandbox.
- Worker launch avoids shell and caller commands; the environment/import root,
  working directory, framed IPC, streaming length checks, output validation,
  failure mapping, termination/kill/close/reap behavior, and post-failure
  recovery are explicit and independently adversarially testable.
- Raw characterization precedes a committed numeric proposal; independent
  review and acceptance precede explicit operator approval; enforcement and
  final unchanged-threshold measurement occur only in their owning later
  batches. No implementor invents or rebases a ceiling.
- Before the first snapshot execution, exact conservative experiment-only wall,
  kill-grace, input, output/diagnostic, recursion, and memory/address-space caps
  are accepted, then the actual non-installed runner, method, exact launch/
  import configuration, and cap/cleanup plumbing are committed as an immutable
  pre-execution candidate. Independent inert/hostile non-decoder probes prove
  every cap, digest/import boundary, termination, close, and reap path on that
  exact candidate; accumulated validation and acceptance pass, explicitly
  recording that no decoder ran. Only the unchanged runner may then execute an
  approved snapshot. A capped run is not a passing baseline, caps are never
  weakened for data, and expected-fixture ownership remains independent.
- C#, .NET, pythonnet, libsigrokdecode, `sigrok-cli`, and external/reference
  runtimes are absent from production and every non-production dependency and
  execution path, including development, tests, fixtures, verification,
  performance, acceptance, review, locks, bootstrap, CI, and evidence.
- That audit covers every active Cycle 3 Python product/development/test/
  fixture/characterization/verification/performance/acceptance/CI/bootstrap/
  lock/distribution/import/process/command/evidence path. Preserved C# metadata
  is inert history that may name dependencies but is never restored, built,
  installed, imported, loaded, executed, or evidence-producing; ambient
  availability alone is not use, while invocation/import/linkage/resolution/
  active process/command/evidence reliance is prohibited.
- Decoder license/attribution identity and a recorded project/legal packaging
  disposition precede source exposure through editable installation; process
  isolation is not presented as resolving licensing, and publication remains
  excluded.
- The platform claim is macOS only. Exact-candidate hosted macOS CI is required
  where assigned; a local skip or historical run is not CI proof.
- Each batch uses distinct implementation, verification, and acceptance
  identities in the mandatory order. Every correction creates a new immutable
  candidate and invalidates prior passes; accumulated validation precedes
  acceptance; manifests are created only after acceptance and independently
  checked before checkpointing.
- A manifest-verifier identity distinct from the orchestrator/assembler records
  recomputed digests and schema results before manifest commit/checkpoint. B5
  acceptance audits only B1-B4 committed manifests and B5 readiness. Its
  terminal chain is directed: manifest/verification record commit; checkpoint
  commit with closure pending; immutable completion-proof candidate naming the
  checkpoint and no future closure artifact; distinct closure audit and
  committed verdict over those inputs; terminal completion seal committed last.
  The seal is not an audit input and audited artifacts are never amended to add
  later identities or verdicts.
- Evidence binds full candidate commit/tree, commands, environment, artifact
  digests, findings/dispositions, role identities, and real results. No future
  manifest, placeholder, transferred pass, or command exit alone substitutes
  for required proof.
- Contract approval and goal approval remain separate all-three common-commit
  gates. The goal points to and cannot weaken or reorder approved contracts,
  and no review record or draft starts `/goal`.

### Explicitly delegated

Reviewer 1 owns focused decoder/API semantics and fixture correctness. Reviewer
2 owns capture/result consumption and public library/CLI workflow utility.
Reviewer 3 requires their committed evidence and cross-seam agreement but does
not substitute security or orchestration judgment for their technical reviews.

## Cross-domain seam rule

A reviewer records a finding whenever its domain cannot safely consume another
domain's promised output, even when the technical repair belongs to a different
charter. The finding identifies both owners and the exact broken handoff; the
owning reviewer assesses the repair and the consuming reviewer verifies that
the seam is explicit.

Required seams include:

- reviewed independent timelines and API-edge semantics into the compatibility
  host, without using implementation or prohibited runtime output as oracle;
- capture channel/sample/time authority into decoder mappings and deterministic
  typed records;
- decoder emissions into bounded IPC normalization, then into one public
  library/CLI serialization path;
- approved numeric values into parent enforcement and unchanged final
  measurements;
- provenance/license decisions into editable resource placement and dependency
  locks without adding a prohibited production or non-production dependency;
- focused proof into accumulated validation, acceptance, manifest, checkpoint,
  CI, and final stopping-condition traceability; and
- approved governing contracts into a durable goal that preserves authority,
  ordering, exclusions, and the exact stop.

Conflicting findings are resolved by the authority order in the approved Cycle
3 orchestration contract, without silently weakening the settled discovery
decisions. Any substantive seam repair requires all three reviewers to inspect
the complete applicable set at one new common commit and tree.
