# Logic Analyzer Python Rewrite: Cycle 3 Orchestration Contract

## Status and purpose

This is the proposed top-level contract for a future durable Cycle 3 `/goal`.
It governs the focused addition of a bounded native compatibility host for the
exact checked-in UART, SPI, and I2C decoder snapshots, exposed through a typed
headless Python library and an installed offline CLI. It does not start a goal
and does not authorize implementation, dependency installation, decoder
execution, hardware action, or creation of checkpoint evidence.

The Step 8 contract-review set is exactly the factual roadmap revision, the
approved Cycle 3 discovery record, this document, `CYCLE3_BATCH_EXECUTION.md`,
and both Cycle 3 review-framework documents listed under "Preparatory
common-commit review" below. That complete set must first be committed together
and receive three independent common-commit `pass` verdicts. The Step 9
goal-review set is exactly that complete contract-review set plus the separately
drafted `CYCLE3_GOAL.md`; it must receive its own three common-commit passes.
Cycle 3 implementation begins only after the final preparation preflight is
clean and the operator invokes the exact approved `/goal` command.

## Authority order

The governing sources have this order:

1. `AGENTS.md` and every included repository instruction govern agent
   behavior.
2. This document governs the Cycle 3 objective, scope, authority, validation,
   evidence, checkpoints, blocking, completion, and stopping conditions.
3. `CYCLE3_BATCH_EXECUTION.md` governs how C3-B1 through C3-B5 are assigned,
   implemented, independently verified, integrated, accepted, and recorded.
4. `Software/LogicAnalyzerPy/docs/cycle-3-discovery-review.md` records the
   approved operator decisions, settled contract surface, batch proposal,
   R1-R26 proof ownership, and staged decision gates that these contracts
   operationalize.
5. `CYCLE3_PREPARATION.md` governs only the work required before goal launch.
6. `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md` is broader
   roadmap context. Work outside this cycle is not authority.
7. The accepted Cycle 1 and Cycle 2 completion proofs, manifests, fixtures,
   contracts, and tests are regression baselines, not authority to weaken or
   expand Cycle 3.
8. `docs/rewrite-reviews/cycle-3/` defines the required common-commit review
   domains and immutable review protocol.

If these sources conflict, follow the higher source and record the conflict in
the Cycle 3 progress log before proceeding. An agent must not reinterpret a
settled product, trust, evidence, platform, or completion decision to resolve a
conflict locally.

## Durable objective

Build and verify, on the accepted macOS-only Python 3.12 platform, a native
focused decoder capability that:

- executes only the exact hash-pinned checked-in UART, SPI, and I2C decoder
  snapshots and their required checked-in shim/helper files;
- accepts an inert validated `CaptureResult`, one host-owned decoder ID,
  explicit decoder-channel-to-physical-channel mapping, and closed typed
  options;
- runs each request in one fresh, single-use Python subprocess with a closed
  import root, versioned bounded IPC, parent-enforced deadline, cancellation,
  output and resource limits, deterministic kill/close/reap, and structured
  failures;
- implements only the frozen API-v3 compatibility subset used by those three
  snapshots and returns deterministic typed annotation, Python, binary, and
  integer-metadata records with authoritative sample coordinates and
  request-wide emission order;
- exposes the one accepted semantic path through an immutable typed
  `pico_logic_analyzer.decode` library surface and the installed offline
  `pico-la decode` replay/CSV workflow; and
- preserves all accepted Cycle 1 and Cycle 2 behavior, evidence, rollback
  paths, optional-web separation, and the macOS-only support claim.

Independently derived and reviewed declarative fixtures are the sole authority
for expected decoder behavior. The existing C# application and upstream source
may be inspected only as inert source. C# must never run for Cycle 3. No .NET,
pythonnet, libsigrokdecode, `sigrok-cli`, or external/reference decoder host may
be installed, imported, linked, invoked, or used as a production or
non-production dependency or executable, including during development, fixture
generation, tests, verification, performance work, CI, or acceptance.

The audit covers every active Cycle 3 Python product, development, test,
fixture, characterization, verification, performance, acceptance, CI,
bootstrap, lock, distribution, import, active-process, command, and evidence
path. Preserved C# project/source metadata remains inert historical rollback
and inspection material and may name a historical dependency; it is never
restored, built, installed, imported, loaded, executed, or used as evidence.
Ambient installed availability alone is not Cycle 3 use and does not authorize
machine mutation. Invocation, import, linkage, dependency resolution, active
process, command reference, or evidence reliance from an in-scope path is use
and is prohibited.

## Approved Cycle 3 decisions

The following operator decisions are exact and may not be weakened by an
implementation, experiment, review, or environment limitation:

1. **Decoder scope:** only the checked-in UART, SPI, and I2C versions and their
   required checked-in compatibility shim/helper, all pinned by hash.
2. **Product surface:** typed headless Python library plus installed offline
   CLI. Browser annotation display and interaction are deferred.
3. **Executable trust:** only a host-owned hash-pinned allowlist may execute.
   User-, capture-, replay-, CSV-, request-, path-, or environment-selected
   modules are prohibited. Stacking and broad discovery are deferred.
4. **Isolation:** every decode uses a single-use subprocess with parent-owned
   deadline, output bounds, cancellation, structured failure, and kill/reap.
   The security claim is bounded process containment, not a general Python or
   OS sandbox.
5. **Expected-output authority:** independently derived and reviewed fixtures
   are the sole oracle. C# and external/reference decoder runtimes may not run
   even to generate, corroborate, compare, verify, or accept results.
6. **Numeric limits:** fixtures, method, environment identity, raw observations,
   and deterministic counts precede an independently reviewed threshold
   proposal; explicit operator approval then freezes every numeric ceiling.
7. **Dependencies and execution:** .NET, C#, pythonnet, libsigrokdecode,
   `sigrok-cli`, and external/reference decoder hosts are prohibited from every
   production and non-production dependency and execution path. Static source
   inspection alone is allowed. The native host adds none of them.
8. **Provenance and licensing:** preserve exact identities, hashes,
   attribution, and GPLv2-or-later notices. A recorded project/legal review
   must reconcile decoder packaging with the Python package's MIT metadata
   before distribution. This contract makes no legal conclusion.
9. **Platform:** macOS remains the only supported and accepted platform.
10. **Physical evidence:** deterministic offline replay and synthetic fixtures
    suffice. No live physical capture/decode gate is required or authorized.

## Required product and proof surface

### Executable identity and imports

The closed executable snapshot is exactly:

- `Software/decoders/sigrokdecode.py`;
- `Software/decoders/uart/{__init__.py,pd.py}`;
- `Software/decoders/spi/{__init__.py,pd.py}`;
- `Software/decoders/i2c/{__init__.py,pd.py}`; and
- `Software/decoders/common/srdhelper/{__init__.py,mod.py}`.

The authoritative SHA-256 values are those frozen in the approved discovery
record. Public decoder IDs are exactly `uart`, `spi`, and `i2c`, resolved by a
host-owned constant table. Before launch, the parent verifies every required
file and rejects missing, extra, replaced, unreadable, mismatched, symlinked,
traversed, shadowed, bytecode-only, alternate-root, namespace-merged,
`PYTHONPATH`, user-site, or current-directory substitutions.

Decoder imports are limited to the frozen local compatibility shim, the frozen
local helper, and the exact Python standard-library names statically required
by the approved snapshots and listed in the discovery record. This allowlist
supports trusted snapshots; it is not a claim that arbitrary Python is safe.
The provenance record retains import commit `407b5ef`, prior gitlink
`0235970`, all hashes, copyright attribution, notices, and any inert verified
upstream byte comparison.

### Compatibility behavior

The host supports only the constants, metadata, lifecycle, `has_channel()`,
`wait()`, `matched`, `samplenum`, `register()`, `put()`, samplerate metadata,
condition forms, skip behavior, termination behavior, and annotation/Python/
binary/integer-metadata outputs settled in Step 5 of the discovery record.
`OUTPUT_LOGIC`, broad API compatibility, decoder stacking, decoder-to-decoder
input, and dynamic discovery are not supported.

The compatibility pin tuple always retains declared required-then-optional
channel order and contains exact built-in integers: mapped samples are `0` or
`1`, while an unmapped optional channel is exactly `0xFF` (`255`). Required
channels cannot be absent. `has_channel()` returns a real `bool`, false exactly
for an optional slot represented by `0xFF`; the sentinel never crosses the
compatibility boundary as capture data or a decoded result. B1 includes UART
RX-only/TX-only and SPI MISO-only/MOSI-only/no-CS fixtures.

Before general host implementation, independently reviewed C3-B1 fixtures must
freeze the five unresolved edge semantics:

1. first and later `wait({})` behavior;
2. current-versus-next-sample searches, sample-zero history, and exact skip
   advancement;
3. simultaneous conjunction/alternative-match priority;
4. interval endpoint interpretation and boundary coordinates; and
5. end-of-input treatment of partial units and already-emitted records.

No reference runtime may be used to decide or corroborate these semantics. A
later correction creates a new reviewed fixture candidate and reopens every
dependent gate.

### Inputs, outputs, library, and CLI

The library accepts a validated non-empty `CaptureResult`, a closed decoder ID,
a validated decoder-channel-to-physical-channel mapping, and closed options.
The capture supplies samplerate and ordered physical identity; packed words are
never indexed by physical channel number. Mapping and exact option rules are
those frozen in the discovery record. All invalid mappings/options fail before
worker launch. Numeric ceilings, including maximum input size and SPI word
size, are owned by C3-B1's explicit threshold approval.

B1 freezes the closed option-coverage matrix defined by discovery. Every
default, enumerated choice, numeric boundary, and sentinel is classified only
as a named direct fixture, source-justified static equivalence to a named
fixture, or unsupported pre-launch rejection. B3 consumes and audits every row;
B5 repeats the matrix-to-fixture digest audit. The phrase “material options”
does not permit sampling or omission.

The typed `DecodeResult` contains decoder/file-set identity, samplerate,
canonical mapping, materialized options, capture count/trigger, declarations,
and an emission-ordered tuple of typed output records. It preserves annotation
text alternatives, bytes, integer metadata, the closed tagged Python-value
tree, sample coordinates, rational time, and request-wide emission order.
Machine serialization is canonical and byte-repeatable for identical inputs,
hashes, and limits.

The complete normative public representation is exactly discovery's separately
versioned `pico-logic-analyzer.decode-result/v1` schema and
`pico-logic-analyzer.decode-error/v1` taxonomy. No implementation may add,
remove, rename, coerce, or reorder a promised semantic field/tag. B1 freezes
independently authored expected immutable-object vectors and literal canonical
CLI bytes for every tag; B2, B4, and B5 consume those exact digests.

The public API is one synchronous typed path under
`pico_logic_analyzer.decode`, centered on
`decode_capture(capture, decoder_id, channels, options, limits=None)`. Caller
limits cannot weaken approved ceilings or disable isolation, digest/import
checks, validation, cancellation/reaping, or the allowlist.

The installed CLI adds only:

```text
pico-la decode (--replay PATH | (--csv PATH --channels D0,D1,...
               [--sample-rate HZ] --trigger-channel PHYSICAL_CHANNEL
               --edge {rising,falling})) --decoder {uart,spi,i2c}
               --channel DECODER_CHANNEL=PHYSICAL_CHANNEL
               [--channel ...] [--option KEY=VALUE] [--option ...]
```

Success writes one canonical compact sorted-key JSON value plus LF to stdout.
Failure writes no machine data to stdout and sends bounded diagnostics to
stderr. Existing exit meanings remain; configuration/mapping errors use 2,
replay/CSV validation uses 5, and decoder digest/import/IPC/exception/resource/
deadline/cancellation failures use documented exit 7. Replay and CSV remain
inert and mutually exclusive. For CSV, `--channels` carries ordered physical
IDs and is distinct from decoder mapping `--channel`; `--trigger-channel` and
`--edge` are required. `--sample-rate` is required except for the exact
accepted legacy D0-D7 header, where omission alone selects accepted inference.
These metadata options are forbidden with replay, CSV never overrides them,
and validation occurs before decoder mapping or launch exactly as frozen in
discovery. No live capture, serial, stdin code, decoder
path, plugin directory, export, browser, or second semantic route is added.

### Worker containment and inert-data boundary

Each decode launches a fresh package-owned worker entry point directly, never
through a shell or caller command. The parent supplies a deterministic minimal
environment, closed import root, non-user-controlled working directory, and
only validated inert data. The worker handles exactly one length-framed,
versioned request and exits. Protocol pipes are separate from bounded captured
stdout/stderr.

The parent streams and independently accounts for request bytes, frame sizes,
record counts, encoded/decoded bytes, text/bytes lengths, nested depth/items,
diagnostics, and retained results without trusting declared lengths. It rejects
unknown versions, fields, tags, output IDs, coordinates, types, malformed,
oversized, truncated, extra, cyclic, or non-finite data and never returns
partial success.

Cancellation and deadline handling stop output, terminate then force-kill at
the approved grace, close all pipes, reap the exact child, discard partial
state, and return one stable typed failure. Spawn/import failure, decoder
exception, recursion/allocation failure, IPC corruption, signal/unexpected
exit, timeout, cancellation, and output-limit breach remain distinguishable
without exposing a traceback or local path. After every failure no worker,
descriptor, partial result, or poisoned state remains, and a subsequent valid
decode succeeds.

Replay, CSV, capture metadata, labels, options, IPC, and output are inert data.
They cannot influence a package/module/path, import root, code, command,
environment, working directory, output file, or dynamic type. The snapshots
have no supported filesystem, network, subprocess, native-extension, serial,
firmware, or hardware capability.

The approved claim contains ordinary Python exceptions, hangs, recursion,
bounded output, and worker-process allocation up to characterized macOS
controls and supplies deterministic kill/reap cleanup. It does not claim an OS
sandbox, privilege separation, safety for arbitrary malicious native code, or
support outside macOS.

## Explicitly excluded

- Decoder stacking, decoder-to-decoder inputs, user/system decoder discovery,
  arbitrary decoder import compatibility, plugins, and capture/request-selected
  executable code.
- C# execution for any Cycle 3 purpose. Any production or non-production
  dependency on or execution of .NET, pythonnet, libsigrokdecode,
  `sigrok-cli`, or an external/reference decoder host.
- Browser/API/frontend decoder integration, annotation rendering, or
  interaction. Existing web tests may run only as unchanged Cycle 2 regression.
- Live capture, serial access, physical decode proof, hardware or firmware
  changes, builds, flashing, bootloader entry, Wi-Fi changes, or persistent
  device actions.
- `.lac`, decoder-selected files, annotation export files, advanced capture or
  editing parity, connectivity/device work, and CPU-specific decoding.
- Linux or Windows support claims, platform expansion, packaging, public
  distribution, release publication, signing, or notarization.
- Removal or material refactoring of the existing C# application or firmware.
- Threshold rebasing to make a candidate pass, silent fixture/method changes,
  future evidence manifests, and Cycle 4 or later work.

Excluded work remains deferred even if useful. Encountering a prohibited
runtime, hardware need, browser change, or scope expansion is a contract
violation or operator gate, not authority to request or perform it.

## Preconditions for the durable goal

Before implementation or decoder execution begins:

- all Steps 1-8 of `CYCLE3_PREPARATION.md` are complete;
- the exact Step 8 contract-review set is committed in one proposed governing-
  contract commit: `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md`,
  `Software/LogicAnalyzerPy/docs/cycle-3-discovery-review.md`,
  `CYCLE3_ORCHESTRATION.md`, `CYCLE3_BATCH_EXECUTION.md`,
  `docs/rewrite-reviews/cycle-3/README.md`, and
  `docs/rewrite-reviews/cycle-3/ARCHITECTURAL_DOMAINS.md`;
- three final contract-review records say exactly `pass` for that same full
  commit and tree after each reviewer inspects every file in that exact set;
- the exact Step 9 goal-review set is then committed: the complete Step 8 set
  above plus `CYCLE3_GOAL.md`; it receives three separate final `pass` records
  naming one same full goal-review commit and tree after each reviewer inspects
  every file in that exact set;
- launch preflight records exact HEAD/tree/branch/worktree, starting baseline,
  decoder and dependency digests, approvals, regression results, platform
  qualification, and absence of pre-created Cycle 3 manifests; and
- the operator invokes the exact approved `/goal` command.

Document drafting and static source inspection before launch are not decoder
execution evidence. No preparation artifact or review verdict starts Cycle 3.

## Preparatory common-commit review

For Step 8, three independent reviewers each inspect every file in this exact
contract-review set at one exact commit and tree:

- `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md`;
- `Software/LogicAnalyzerPy/docs/cycle-3-discovery-review.md`;
- `CYCLE3_ORCHESTRATION.md`;
- `CYCLE3_BATCH_EXECUTION.md`;
- `docs/rewrite-reviews/cycle-3/README.md`; and
- `docs/rewrite-reviews/cycle-3/ARCHITECTURAL_DOMAINS.md`.

The reviewers apply these independent domains to that complete set:

1. **Decoder API/runtime and fixture correctness:** exact snapshot/API subset,
   lifecycle, wait/match/skip/sample semantics, mapping/options, output models,
   deterministic fixtures, and conformance proof.
2. **Capture and public workflow:** capture/sample/time semantics, annotation
   models, replay/CSV equivalence, typed library, installed CLI, existing
   CLI/web regression, and exclusions.
3. **Security, delivery, and governance:** executable-code boundary,
   subprocess/IPC containment, cancellation/resources, prohibited dependencies
   and execution, licensing, macOS CI, performance, roles, evidence,
   checkpoints, correction ordering, and durable completion.

Each immutable record contains stable reviewer identity, exact full commit and
tree, UTC timestamp, verdict exactly `pass` or `changes_required`, numbered
findings, requested resolutions, and dispositions. Preserve failed and
superseded rounds. Any substantive objective, scope, authority, ownership,
security, fixture, batch, validation, evidence, checkpoint, platform, or
stopping-condition correction requires all three reviewers to inspect one new
common commit. Final approval cannot mix verdicts across commits or rounds.

After contract approval, Step 9 uses an exact goal-review set consisting of the
complete six-file Step 8 contract-review set above plus `CYCLE3_GOAL.md`. The
same three domains each inspect every file in that complete seven-file set at
one exact goal-review commit and tree. A Step 8 pass cannot be transferred to
Step 9. The goal may point to but cannot redefine, bypass, reorder, weaken, or
leave ambiguous an approved contract.

## Discovery and new-work model

### Evidence precedence

For decoder semantics and expected results:

1. Independently derived, human-reviewable declarative timelines and expected
   outputs accepted through the C3-B1 fixture gate.
2. The exact frozen checked-in decoder/shim/helper sources as static evidence.
3. Independently constructed calculations and inert accepted capture/replay/CSV
   fixtures.
4. Existing C# or upstream source as non-executed explanatory context only.

Production output cannot create its own oracle. C#, .NET, pythonnet,
libsigrokdecode, `sigrok-cli`, upstream/reference hosts, and differential
runtime output have no evidence precedence because running or depending on them
is prohibited.

### Uncertainty outcomes

Every uncertainty ends as:

- **resolved locally** by an approved source, fixture, or accepted contract;
- **resolved by the authorized C3-B1 fixture/characterization gate** without a
  prohibited executable or dependency;
- **resolved by explicit operator approval** for numeric thresholds and SPI
  maximum word size;
- **deferred** because it is outside the stopping condition; or
- **blocked on authority** while other independent in-scope work continues.

An implementor, verifier, or acceptance agent may not choose a substantive API
semantic, trust rule, limit, platform claim, or proof source informally.

### New-work scope test

New work enters the active batch only when all are true:

1. a stopping condition cannot be met without it;
2. it remains within the required Cycle 3 surface;
3. it crosses no authority or operator gate;
4. its earliest owner, objective proof, and accumulated owner are explicit; and
5. it does not add or execute a prohibited dependency/runtime.

Otherwise record and defer it. Do not begin browser, hardware, packaging,
platform, broad-decoder, or later-cycle work merely to keep an agent occupied.

## Batch sequence and ownership

Cycle 3 executes five batches in this dependency order:

1. **C3-B1 — provenance, semantic fixtures, and approved limits:** freeze the
   executable snapshot, provenance/license disposition, independently reviewed
   declarative fixtures and five API-edge semantics, characterization method,
   raw baselines, independently reviewed threshold proposal, and explicit
   operator-approved numeric limits including maximum SPI word size.
2. **C3-B2 — isolated compatibility host and containment:** implement the
   private single-use subprocess host, closed API-v3 subset, typed result,
   versioned streaming IPC, approved limits, cancellation/failure cleanup, and
   inert-code-selection boundary. No public API or CLI yet.
3. **C3-B3 — focused UART, SPI, and I2C conformance:** prove all settled output
   kinds, options, mappings, boundaries, malformed/incomplete traffic, ordering,
   and equivalent in-memory/replay/CSV inputs for the exact snapshots.
4. **C3-B4 — public library and installed CLI:** expose the sole accepted host
   through the typed synchronous library and exact offline CLI, with clean
   installation, dependency, documentation, regression, and exact-candidate
   macOS CI proof.
5. **C3-B5 — exact-candidate accumulated proof and completion:** add no new
   product behavior; rerun every semantic, containment, conformance, public,
   dependency, resource/performance, CI, evidence, regression, rollback, and
   scope gate against one final immutable candidate.

C3-B1 is an intentionally staged prerequisite. Its authoritative fixture
candidate receives independent verification and acceptance first. It then
commits a separate immutable pre-execution candidate containing the actual
non-installed characterization runner, measurement method, exact launch/import
configuration, and enforcement/cleanup plumbing for the accepted conservative
experiment-only deadline, kill-grace, input, output/diagnostic, recursion, and
memory/address-space caps. A verifier exercises that exact candidate solely
with inert/hostile non-decoder probes for every cap, digest/import boundary,
termination, pipe/descriptor close, and exact-child reap path; accumulated
validation and distinct acceptance must pass and state that no decoder ran.
Only that exact unchanged runner may then execute an approved snapshot. The
runner is not a product host. A semantic-fixture implementation identity owns
expected fixtures and cannot author the runner, method, or probes; a different
pre-execution-runner implementation identity owns those surfaces and cannot
author expected fixtures. Each internal candidate has separate verifier and
acceptance identities, and no pass transfers between candidates. A capped
failure is not a passing baseline, and the caps cannot be
weakened; later approved product thresholds replace them. Raw observations
precede the threshold proposal; independent proposal review precedes
acceptance; explicit operator approval is last. No public host implementation
begins until the complete C3-B1 checkpoint exists.

A checkpoint is valid only after the exact candidate's independent verification,
complete accumulated validation, and independent acceptance all pass; its
post-acceptance manifest is atomically created and independently validated; and
its checkpoint record is committed. Batches complete only in order. An earlier
interface regression reopens its earliest owner and every dependent gate.

## Requirement-to-proof ownership

Each required outcome has one earliest owner and C3-B5 final accumulated
ownership. Later repetition is regression proof, not transferred ownership.

| ID | Required outcome | Earliest owner and proof | Final owner |
| --- | --- | --- | --- |
| R1 | Exact snapshot identities, provenance, hashes, closed imports, notices, and license disposition | B1 file/import/provenance audit and project/legal record | B5 |
| R2 | Independent declarative timelines and expected outputs are the sole oracle | B1 literal review, independence audit, byte-stable rebuild | B5 |
| R3 | Five API-v3 edge semantics freeze before host implementation | B1 numbered fixtures plus verification/acceptance | B5 |
| R4 | Characterization method, raw baseline, and counts reproduce | B1 independent reproduction | B5 |
| R5 | Numeric ceilings and SPI maximum have review and operator approval | B1 proposal, verification, acceptance, operator decision | B5 |
| R6 | ID/files/imports/environment/data cannot select code | B2 digest/path/symlink/shadowing/inert-data adversarial proof | B5 |
| R7 | Capture/mapping/samplerate/options validate before launch | B2 exact boundary tests with spawn counter | B5 |
| R8 | Frozen lifecycle/wait/matched/samplenum/skip/register/put behavior | B2 B1 fixtures against private host | B5 |
| R9 | Version-1 typed declarations/tags/values, rational time, coordinates, and emission order are deterministic | B1 independent object/JSON golden identities; B2 consumes them in shape/order/serialization/repeat tests | B5 |
| R10 | Framed IPC rejects malformed/oversized/partial/extra/unknown data | B2 independent hostile-frame matrix | B5 |
| R11 | Approved deadline/cancel/memory/recursion/output/retention limits are parent-enforced | B2 boundary/overrun proof and independent counters | B5 |
| R12 | Failures cleanly kill/close/reap and subsequent decode succeeds | B2 process/descriptor and post-failure matrix | B5 |
| R13 | UART conforms for options/mappings and annotation/Python/binary output | B3 authoritative UART comparisons | B5 |
| R14 | SPI conforms through approved word size for all output kinds | B3 authoritative SPI comparisons | B5 |
| R15 | I2C conforms for all applicable output kinds | B3 authoritative I2C comparisons | B5 |
| R16 | In-memory, replay schema 1/2, and explicit CSV inputs agree | B3 independently materialized cross-source comparison | B5 |
| R17 | Typed library implements the version-1 immutable models, delegates to one isolated host, and cannot weaken limits | B4 installed black-box/type tests against B1 object vectors and delegation audit | B5 |
| R18 | Installed CLI grammar, explicit CSV metadata, version-1 JSON/failures, stderr, and exits are exact | B4 installed golden/negative suite against B1 literal bytes | B5 |
| R19 | Core/library/CLI remain web-independent and never open serial | B4 import/open spies, extras audit, unchanged web regression | B5 |
| R20 | Clean locked Python 3.12, static/test gates, and macOS CI pass | B4 fresh bootstrap and exact-candidate CI | B5 |
| R21 | Prohibited runtimes/dependencies have no use in any scoped active Cycle 3 path; preserved C# metadata remains inert | B1 scoped audit, enforced continuously from first execution | B5 |
| R22 | Approved resource/performance ceilings enforce without rebasing | B2 boundary enforcement; B1 owns values | B5 |
| R23 | Cycle 1/2 behavior, manifests, rollback, and macOS claim remain | B1 inherited baseline, rerun each batch | B5 |
| R24 | Candidate/role/finding/manifest/checkpoint/correction order is auditable | B1 first complete governed sequence | B5 |
| R25 | Excluded browser/hardware/firmware/dynamic/.lac/publication/platform work did not occur | B1 scope audit, carried by every checkpoint | B5 |
| R26 | Final candidate meets every approved threshold on characterized macOS class | B5 fresh final measurements | B5 |

R21, R23, R24, and R25 are continuous accumulated audits. R5 owns limit values,
R22 owns their enforcement, and R26 owns the final observation, avoiding a
circular threshold gate.

## Authority and operator gates

### Authorized only within the future approved goal

- Read repository sources, approved contracts, accepted evidence, and inert C#
  or upstream source.
- Edit only Cycle 3-owned Python product, tests, deterministic fixtures,
  dependency metadata, workflow, evidence schema/validator, and documentation
  under the paths assigned by the batch contract.
- Execute only the exact approved checked-in decoder snapshots after the B1
  fixture gate, through the active batch's approved characterization or native
  host path.
- Run deterministic offline format, lint, type, unit, integration, replay, CSV,
  subprocess/IPC, security, resource, performance, CLI, and unchanged
  non-hardware regression checks.
- Make the smallest active-batch correction and rerun every invalidated gate.
- Replace the existing Cycle 2 Python workflow only if the approved batch
  contract assigns that exact path and preserves the accepted macOS-only
  regression surface; redundant full workflows are not authorized.

### Requires normal execution approval when prompted

- Downloading or installing the approved hash-locked Python dependencies.
- Pushing an exact candidate to run required hosted macOS CI.
- Executing another environment-controlled capability explicitly assigned by
  the active contract and not otherwise prohibited.

Only the root orchestrator may route such approval. Approval expands execution
capability, never product scope, trust, dependencies, or evidence semantics.

### Requires explicit operator decision in the active goal

- The C3-B1 numeric ceiling and maximum-SPI-word-size record, after raw
  baselines and independent proposal review exist.
- A changed fixture, method, environment class, worker model, or weakened
  ceiling, which reopens B1 and requires a new proposal, reviews, and operator
  decision.
- Any proposed change to the durable objective, scope, trust boundary,
  platform, batch ownership, proof source, or stopping condition, which also
  requires the applicable common-commit contract review.

### Prohibited rather than approval-gated

- Running C# or installing, importing, linking, invoking, or depending on .NET,
  pythonnet, libsigrokdecode, `sigrok-cli`, or an external/reference decoder
  runtime in any role or environment.
- USB/serial/hardware/live-capture, firmware, browser decoder, non-macOS support,
  packaging/publication, dynamic decoder, stacking, `.lac`, or later-cycle work.
- Weakening fixtures, assertions, limits, or thresholds to make a candidate
  pass; transferring an earlier pass to a corrected candidate; or creating a
  future manifest.

Encountering a prohibited action does not justify requesting it. Stop that
path, record the scope violation, and continue only safe independent work.

## Roles, candidate sequence, and correction rules

Every batch uses five separate roles. B1 splits its implementation role into
the two separately owned internal candidate identities defined below:

- an **implementation identity** (two internally distinct implementors in B1)
  for the bounded owning surface and focused implementation checks;
- a different **verification identity** that derives independent black-box,
  boundary, security, conformance, or resource proof and reports exactly
  `pass` or `changes_required`;
- a third **acceptance identity** that audits the exact candidate, findings,
  accumulated results, scope, provenance, and evidence ordering and reports
  exactly `pass` or `changes_required`;
- a post-acceptance **manifest-verifier identity**, distinct from the
  orchestrator/evidence assembler, that independently recomputes all artifact
  digests, validates the manifest schema, and creates an immutable record
  naming candidate, manifest digest, commands, results, and verdict; and
- the **primary orchestrator**, which integrates, creates the immutable
  candidate, runs the complete accumulated gate, assembles post-acceptance
  evidence, appends checkpoints, and owns the terminal completion seal.

For B1, the **semantic-fixture implementor** owns timelines, independently
expected records, the fixture generator, and experiment caps and may not author
runner, measurement-method, launch/import, or probe content. A distinct
**pre-execution-runner implementor** owns the actual runner, method,
launch/import configuration, cap/cleanup plumbing, and inert/hostile probes and
may not author expected fixtures. The fixture candidate and runner candidate
each receive their own verifier and acceptance identities, all distinct from
both implementors; their passes are candidate-specific and never transfer. The
progress entry, assignments, handoffs, final B1 candidate identity map,
manifest, checkpoint, and completion proof name all six B1 internal identities.

An acceptance agent never repairs its candidate. A verifier cannot approve
production behavior or expected fixtures it authored. A B2-B4 product
implementor cannot have authored B1's authoritative expected outputs. If an
identity crosses a boundary, assign a fresh identity and repeat the affected
review. Role separation may be sequential but is never waived.

Every batch follows this exact order:

1. bounded active-batch entry and prerequisite/authority preflight;
2. focused failing check and smallest owning implementation;
3. focused checks pass and one immutable candidate commit/tree is created;
4. independent verification of that exact candidate records a verdict;
5. orchestrator runs the complete accumulated gate on the same candidate;
6. independent acceptance audits that candidate and all accumulated evidence;
7. only after both verdicts are `pass`, atomically create the batch manifest,
   which may name the assigned manifest verifier but no future verifier verdict,
   record identity/path, or self-dependent digest;
   have its manifest verifier recompute digests/schema and create the required
   immutable record naming and hashing the unchanged manifest, then commit the
   manifest and verification record together; and
8. append and commit the checkpoint, then select the next batch.

For B5, step 6 is expressly pre-manifest acceptance: it audits B1-B4 committed
manifests/checkpoints plus the exact final candidate and proposed B5 manifest
inputs/readiness, never a future B5 manifest or checkpoint. B5 then has this
single directed terminal order: (1) commit its manifest and manifest-
verification record; (2) commit its checkpoint with state `Complete; Cycle 3
closure pending`; (3) commit the immutable `cycle-3-completion.md` proof
candidate, which names the checkpoint and contains no future closure auditor,
verdict, record, or seal reference; (4) have a distinct completion-closure
auditor inspect only those already committed artifacts and commit its immutable
`pass` or `changes_required` verdict; and (5), only after `pass`, commit
`cycle-3-completion-seal.md` as the terminal stop. The seal is not an audit
input and adds no product or proof claim. A failed closure audit reopens the
earliest owning correction and all invalidated gates; a corrected artifact
requires a new proof candidate and closure audit before any seal.

Any product, fixture, method, dependency, workflow, limit, or test correction
after candidate creation makes a new candidate and invalidates all earlier
verification, accumulated, and acceptance passes for that batch. Preserve old
records as immutable history. A regression reopens the earliest owning batch
and every dependent accumulated gate. No manifest or evidence document is part
of the tested product tree merely because it descends from that candidate.

## Validation contract

C3-B1 freezes exact command names after clean-environment characterization.
Every accumulated gate must include at least:

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
```

It also includes the Cycle 1/2 evidence validator, decoder/helper digest and
closed-import audit, prohibited dependency/import/process audit, deterministic
B1 fixture rebuild, all completed Cycle 3 focused suites, and the active
batch's resource/performance gates. Existing frontend/web tests are unchanged
regression only and cannot add Cycle 3 web authority. C3-B4 and C3-B5 require
hosted macOS CI for the exact candidate; a restricted local skip is not proof.

Clean bootstraps are required for C3-B1, C3-B4, C3-B5, and hosted CI. A reused
local environment is evidence only when Python/OS and every lock digest match
the recorded identity. Focused tests never replace accumulated validation.
Expected values come from accepted fixtures and independent calculation, not
from production or prohibited reference output.

C3-B1's accepted fixture gate first freezes exact experiment-only caps for wall
deadline, termination/force-kill grace, input samples/request bytes, output
records and encoded/decoded bytes, stdout/stderr/diagnostic bytes, nesting,
recursion, and worker memory/address space. C3-B1 next commits the actual runner,
method, exact launch/import configuration, and cap/cleanup plumbing as an
immutable pre-execution candidate. Independent verification uses inert and
hostile non-decoder probes to prove every cap, digest/import boundary,
termination, close, and reap path on that unchanged candidate; accumulated
validation and acceptance pass and explicitly record that no decoder ran.
Limit termination is data, not a passing baseline, and no experiment cap may
be weakened. Only then does C3-B1 measure and
freezes the environment, fixture digests, warm-up/repetition
rules, raw observations, and deterministic counts for request size, spawn/
import/decode time, cancellation/kill/reap latency, worker and retained memory,
recursion, every output/count/byte/depth/item/diagnostic/retention category, and
representative/stress/hostile cases. Only the separately approved threshold
record supplies numeric gates. The exact B5 candidate must satisfy unchanged
approved values on the characterized macOS environment class.

## Progress, evidence, manifests, and checkpoints

C3-B1 creates, before accepting implementation evidence:

- `Software/LogicAnalyzerPy/docs/cycle-3-orchestration-progress.md`;
- a strict Cycle 3 JSON Schema draft 2020-12 evidence schema under
  `Software/LogicAnalyzerPy/docs/evidence-manifest/`;
- a Cycle 3 manifest validator under `Software/LogicAnalyzerPy/scripts/`; and
- only an explicitly labelled non-evidence template or directory marker if one
  is genuinely useful.

It must not pre-create C3-B2 through C3-B5 manifests. After C3-B1 evidence,
verification, accumulated validation, and acceptance exist, the orchestrator
atomically creates only `Software/LogicAnalyzerPy/testdata/evidence/c3-b1.json`,
then the distinct manifest verifier recomputes all digests, validates the
schema, and records its immutable verdict in a separate record that names and
hashes the unchanged manifest. The proposed manifest may name the assigned
manifest-verifier identity, but contains no future verifier verdict, verifier-
record identity/path, or self-dependent digest. The orchestrator commits the
manifest plus verification record and only then appends the checkpoint. Each
later batch
does the same only for its own `c3-bN.json`. A filename, placeholder, example,
empty object, or template is never evidence.

The schema uses `schema_version: 3`, checkpoint pattern `^C3-B[1-5]$`, and
`additionalProperties: false` recursively. Every manifest records, as
applicable:

- full tested candidate commit/tree and clean or qualified worktree;
- UTC timestamp, macOS/architecture, Python identity, and characterized
  environment class;
- SHA-256 values for Python locks, exact decoder/shim/helper files, fixture
  sources/generated outputs, method, approved thresholds, and owned artifacts;
- normalized command, status, stable verifier identity, and hosted-CI run/job
  identity bound to the exact candidate;
- evidence source/provenance, path, digest, and deterministic counts;
- mutually distinct implementation, verification, acceptance, and assigned
  manifest-verifier identities; for B1, the fixture and runner implementor,
  verifier, and acceptance identity map; existing candidate review verdicts,
  numbered findings/dispositions, decisions, limitations, and deferrals;
- every applicable R1-R26 identifier and stopping-condition identifier with
  evidence references and digests;
- prohibited-runtime/dependency/process and excluded-scope audit results; and
- for B1, the fixture/API-edge candidates, characterization/raw observations,
  project/legal record, threshold reviews, and operator decision; for B5, final
  measurements and the complete packet digest map.

The schema assigns manifest-verification commands/results, manifest SHA-256,
findings, and verdict exclusively to the separate immutable manifest-
verification record, not to the manifest. That record names and hashes the
unchanged manifest. The manifest and record are committed together; the later
checkpoint references both committed files and the recorded `pass`. This same
directed ownership applies to B1-B5.

The validator rejects secret, credential, user-home, machine-local path/URL,
or other sensitive values. Manifest schema validation and independent digest
verification are checkpoint gates, not best-effort documentation. An accepted
manifest is immutable; a reopened checkpoint creates a separately identified
replacement/correction record.

Final semantic, containment, conformance, dependency, performance, CI, and
public-interface proof must name one exact candidate with no uncommitted
product, test, fixture, method, lock, workflow, or threshold change. Unrelated
user changes are enumerated and excluded. No command's exit zero substitutes
for required artifact, review, operator, process, CI, or candidate identity.

## Verifiable stopping condition

Cycle 3 is complete only when one exact C3-B5 candidate satisfies every item:

1. Exact UART, SPI, I2C, shim, and helper files, digests, provenance, notices,
   closed imports, package placement, and license metadata match B1.
2. Independent byte-reproducible fixtures cover all three decoders, output
   kinds, every option-matrix row, exact optional-pin sentinel combinations,
   malformed/incomplete traffic, boundaries, simultaneous waits, ordering,
   version-1 object/JSON goldens, and five frozen API-v3 edge semantics.
3. Method, environment identity, raw B1 observations, numeric ceilings,
   maximum SPI word size, independent reviews, and operator decision are
   immutable and mutually consistent.
4. The parent resolves only host IDs, verifies all digests, constructs the
   closed import environment, and proves capture/request metadata inert before
   every worker launch.
5. Capture, samplerate, channel mapping, and option validation rejects every
   invalid input before process creation.
6. One fresh worker implements only the frozen API-v3 subset and returns the
   complete deterministic typed result with authoritative sample coordinates,
   rational time, and request-wide emission order.
7. Versioned streaming IPC/output normalization rejects malformed, oversized,
   unknown, partial, extra, cyclic, or non-finite data without partial success.
8. Approved deadline, cancellation, memory, recursion, output, nesting,
   diagnostic, retention, and performance ceilings are enforced; every failure
   closes/reaps the worker and a subsequent valid decode succeeds.
9. Authoritative UART, SPI, and I2C suites pass every accepted option-matrix row,
   required/optional and reordered mappings, boundary traffic, and every
   applicable annotation/Python/binary/meta output.
10. Equivalent in-memory, replay schema 1/2, and explicit-metadata CSV inputs
    produce byte-identical canonical results without physical I/O.
11. The installed typed library and `pico-la decode` command satisfy exact
    version-1 object/JSON/failure, explicit-CSV-metadata, stderr, exit,
    non-weakenable-limit, and
    no-live-capture contracts outside the source tree.
12. Fresh Python 3.12 hash-locked install, `pip check`, Ruff, strict mypy, all
    non-hardware tests, installed CLI help, and exact-candidate hosted macOS CI
    pass with no required skip.
13. Dependency, process, import, lock, command, and evidence audits prove no
    prohibited use in any active Cycle 3 path under the exact scoped-audit rule;
    preserved inert C# historical metadata is never built/restored/installed/
    imported/executed or relied on as evidence.
14. Accepted Cycle 1/2 tests, manifests, replay/CSV/CLI behavior, optional-web
    separation, rollback paths, and macOS-only claim remain intact.
15. Independent final measurements on the characterized macOS class meet every
    unchanged approved resource/performance threshold and enforce the approved
    SPI maximum.
16. Five ordered checkpoints contain distinct implementation, verification,
    acceptance, and manifest-verifier identities; exact candidate/tree proof;
    immutable findings; schema-valid post-acceptance manifests; and correction
    history, with no future manifest or transferred pass.
17. Final scope audit finds no browser/API/frontend decoder work, hardware,
    firmware, serial/live capture, dynamic discovery, stacking, `.lac`,
    packaging/publication, unsupported platform claim, or other excluded work.
18. The B5 packet maps R1-R26 and items 1-17 to committed evidence and records
    a clean or qualified repository. Verification and pre-manifest acceptance
    pass before manifest creation; the distinct manifest-verification pass and
    manifest commit precede the closure-pending checkpoint; the immutable
    completion-proof candidate then names that committed checkpoint and no
    future closure artifact; the distinct closure verdict passes over those
    committed inputs; and a terminal completion seal, which was not an audit
    input, is committed last.

A fake substitute, prohibited reference execution, skipped required gate,
unapproved numeric value, stale candidate pass, or command-only claim cannot
satisfy an item.

## Failure, retry, and blocking policy

- A normal implementation or test failure remains in the owning batch.
- A semantic fixture defect reopens B1 and all dependent work; a containment,
  decoder, or public-interface regression reopens B2, B3, or B4 respectively.
- A changed method, environment class, worker model, or weakened limit reopens
  B1 and requires new raw results, proposal review, acceptance, and operator
  approval before dependent implementation continues.
- Resource/performance variance is diagnosed under the approved method; it is
  not grounds to weaken or rebase a threshold silently.
- Missing dependency-download or hosted-CI authority, required project/legal
  review, or operator threshold decision is recorded precisely. Continue
  independent in-scope work where useful, but do not fabricate evidence.
- A request for C#, .NET, pythonnet, libsigrokdecode, reference runtime,
  hardware, browser decoder work, or another excluded capability is rejected as
  out of scope rather than treated as an execution blocker.
- The durable goal may be marked blocked only after the same external blocker
  persists for the number of consecutive goal turns required by the goal
  system and no meaningful in-scope work remains.

## Completion proof, rollback, and handoff

After the B5 manifest/verification record and closure-pending checkpoint are
committed, create and commit the immutable completion-proof candidate
`Software/LogicAnalyzerPy/docs/cycle-3-completion.md` containing:

- stopping conditions 1-17 and R1-R26 linked to immutable pass evidence, plus
  condition 18's completed manifest/verification/checkpoint ordering and
  literal `closure pending` remainder, without naming a future artifact;
- exact final candidate commit/tree and clean or qualified repository state;
- exact decoder/shim/helper, dependency-lock, fixture, method, threshold,
  evidence-manifest, and relevant package-resource digests;
- canonical clean-install, lint, type, test, CLI, fixture, containment,
  conformance, resource/performance, evidence-validation, and hosted macOS CI
  commands and results;
- B1 edge-semantic fixture identities, raw characterization, project/legal
  disposition, threshold reviews, and explicit operator decision;
- all five checkpoint, implementation, verification, acceptance, correction,
  manifest, and distinct manifest-verification records;
- the exact committed B5 checkpoint identity and literal state `Complete;
  Cycle 3 closure pending`, with no predicted closure auditor, verdict, record
  path, or terminal-seal identity;
- the exact macOS-only support and bounded-process-containment claims;
- known limitations and deferred work;
- rollback to the accepted pre-Cycle-3 Python candidate and preservation of the
  existing C# application/firmware as untouched operational paths; and
- confirmation that C#/.NET, pythonnet, libsigrokdecode, `sigrok-cli`, external
  decoder runtimes, browser decoder work, hardware/firmware/live capture,
  `.lac`, dynamic discovery, packaging/publication, unsupported-platform work,
  and Cycle 4 did not occur.

The completion-proof candidate is immutable once submitted to closure audit.
The distinct auditor inspects the committed B5 manifest and verification
record, closure-pending checkpoint, and completion-proof candidate, then
commits its verdict without repairing any input. After a `pass`, the
orchestrator commits
`Software/LogicAnalyzerPy/docs/cycle-3-completion-seal.md` containing only the
commits and SHA-256 digests of those already committed audit inputs and the
committed closure verdict, plus the statement that this seal is not an audit
input and adds no product/evidence claim. No future artifact is named by any
audited input.

Rollback never authorizes editing or deleting the C# application or firmware.
Stop successfully only when every condition is linked to objective evidence,
the final verification, pre-manifest acceptance, manifest-verification, and
post-proof completion-closure verdicts are `pass`, the directed B5 terminal
chain is committed without a future reference, the terminal completion seal is
the last Cycle 3 commit, and no implementation or evidence correction follows
the accepted candidate. Do not begin Cycle 4.
