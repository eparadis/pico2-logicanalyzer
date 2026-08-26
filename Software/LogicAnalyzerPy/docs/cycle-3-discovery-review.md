# Cycle 3 bounded discovery review

## Status, purpose, and authority boundary

- Status: Steps 1 through 4 are committed. This revision freezes the Step 5
  narrow contract surface and meets its content exit gate, subject to committing
  this record.
- Inspection date: 2026-08-25 (America/Los_Angeles).
- Authority: `CYCLE3_PREPARATION.md`, committed at
  `c163a8353550e0b80dd7f001b21147659ad307ff`.

This record contains the bounded Cycle 3 discovery required by
`CYCLE3_PREPARATION.md`: the exact inherited Cycle 2 evidence, the
post-completion repository delta, the reconciled roadmap, and static technical
discovery for a possible focused decoder cycle. Later preparation steps must
expand this same file with explicit operator decisions, the settled contract
surface, and proposed proof ownership.

This document does not authorize Cycle 3 implementation, dependency changes,
decoder execution, hardware or firmware action, persistent device changes, or
creation of Cycle 3 checkpoint evidence. A change accepted below as starting
input does not gain retroactive Cycle 2 acceptance. The accepted Cycle 2
candidate and immutable evidence remain unchanged.

## Step 1: starting-baseline reconciliation

### Accepted Cycle 2 identities

The authoritative completion record is
`Software/LogicAnalyzerPy/docs/cycle-2-completion.md`, added by completion-proof
commit `f558b58612f5c85f58791a850b3319d5dfaba14e`. It records:

- final accepted product candidate:
  `2d5484a73d881496cdf5a35c799dfb01eedad229`;
- final accepted product tree:
  `8c76bce79922263468cb6ceaa4f1990703a84bfc`;
- final B6 checkpoint commit:
  `7fe1f5c06b87c47285378b2144c4a3c4377a7238`;
- final B6 checkpoint tree:
  `68aa9ecbad96d324467e37b7bb3a2de37e53153b`;
- completion-proof commit:
  `f558b58612f5c85f58791a850b3319d5dfaba14e`;
- completion-proof tree:
  `45dc85e090aa7f84db4feadd022ece0ae66df4f1`;
- audited platform claim: macOS only; and
- final acceptance verdict: pass, with no open or deferred Cycle 2 finding.

The six active Cycle 2 manifests named by that completion proof are:

| Checkpoint | Manifest | Manifest commit | Recorded SHA-256 |
| --- | --- | --- | --- |
| C2-B1 | `Software/LogicAnalyzerPy/testdata/evidence/c2-b1.json` | `4bb2561` | `7c45f8b7f90965fbf9c67845f3b8a0113fe84261e8085665068e6f1980bf4de0` |
| C2-B2 | `Software/LogicAnalyzerPy/testdata/evidence/c2-b2.json` | `5f5eebb` | `d930bce4ae20576ea030e35cf0e993a3caf89e95f5eb5195638471c1790c2be4` |
| C2-B3 | `Software/LogicAnalyzerPy/testdata/evidence/c2-b3.json` | `4635bf4` | `9db03e119c6cacb40e87ef61d8f7ef1e24692ea45527f5e331e2103ecc59ff1b` |
| C2-B4 | `Software/LogicAnalyzerPy/testdata/evidence/c2-b4.json` | `ef74970` | `4876b781f4569ae1599b6c5df4d824fbd54223c736c87c96746e6bb821806fd0` |
| C2-B5 | `Software/LogicAnalyzerPy/testdata/evidence/c2-b5.json` | `f561d31` | `8fcdf9714e2ad94af845d9676227bf6750159075bb49416d9c78c16d5b3c14e9` |
| C2-B6 | `Software/LogicAnalyzerPy/testdata/evidence/c2-b6.json` | `354c299` | `ed8036ef48654efd98a5c3a852fb1f1dba847a34e12bf1c5dec253a2b9a83ffb` |

The C2-B6 manifest binds the same accepted product candidate and tree. The
implementation, verification, acceptance, manifest, checkpoint, and completion
commits after `2d5484a` are immutable evidence or governance descendants; they
do not alter the accepted product tree.

### Repository state inspected for Step 1

The repository was clean before this discovery record was created:

- HEAD: `c163a8353550e0b80dd7f001b21147659ad307ff`;
- tree: `45556769aab973c7671f58d57bae1878a46af9f2`;
- branch: `python-rewrite`;
- upstream relation: one commit ahead of `origin/python-rewrite`, with no
  behind commit;
- tracked, staged, unstaged, and untracked changes: none; and
- unrelated user changes: none observed.

Creation of this file is the only Step 1 worktree change. It is preparation
documentation, is not a product change, and remains outside the proposed input
baseline until it is reviewed and committed by the root orchestrator.

### Descendants of the accepted product candidate

Between the accepted product candidate and the completion proof, the following
commits add only the final B6 evidence and governance records:

| Commit | Tree | Path-level change | Classification |
| --- | --- | --- | --- |
| `a349cc5a855c4c73c74c2ca79d5058ec6a3f8c77` | `e7b6d05784346da0198d0f9997ea43a10ad5a914` | add `docs/reviews/c2-b6-implementation-round-4.md` | Accepted immutable Cycle 2 evidence; preserve. |
| `436e18735831e4db3501ff3bb1cc08c2761a0e1d` | `acc8d1a29fbaa9b1388cc0f531b9494712485330` | add `docs/reviews/c2-b6-verification-round-4.md` | Accepted immutable Cycle 2 evidence; preserve. |
| `605400422b4affbd84793686a8431769de9913ef` | `b9f14e106f1050e459678ecacd9bf768ce1af90e` | add `docs/reviews/c2-b6-acceptance-round-2.md` | Accepted immutable Cycle 2 evidence; preserve. |
| `354c299903ec73633e5762a2b65adaae1d44e8d7` | `6f67f22c5dcf8696b9df6883e13c3ae0e2b9cebc` | add `testdata/evidence/c2-b6.json` | Accepted immutable Cycle 2 manifest; preserve. |
| `7fe1f5c06b87c47285378b2144c4a3c4377a7238` | `68aa9ecbad96d324467e37b7bb3a2de37e53153b` | update `docs/cycle-2-orchestration-progress.md` | Accepted B6 checkpoint record; preserve. |
| `f558b58612f5c85f58791a850b3319d5dfaba14e` | `45dc85e090aa7f84db4feadd022ece0ae66df4f1` | add `docs/cycle-2-completion.md` | Accepted Cycle 2 completion proof; preserve. |

There are two commits after the Cycle 2 completion proof:

| Commit | Tree | Path-level change | Classification and disposition |
| --- | --- | --- | --- |
| `5b409a6384624bfb6b51bc323c97a54244477dde` | `74249d3dcb3eb414268d34f467164d90fd3b90b4` | modify `Software/LogicAnalyzerPy/README.md`; add executable `Software/LogicAnalyzerPy/start_web.sh` | Post-completion product/documentation delta. Include as Cycle 3 starting input after the focused checks below. This is not Cycle 2 acceptance. Runtime dependency installation, device discovery, live launch, SSH behavior, and hardware behavior were not exercised, so Step 1 makes no new acceptance claim for them. |
| `c163a8353550e0b80dd7f001b21147659ad307ff` | `45556769aab973c7671f58d57bae1878a46af9f2` | add `CYCLE3_PREPARATION.md` | Cycle 3 governance input. Include and preserve; it changes no product, accepted evidence, dependency, fixture, or workflow. |

No post-completion path is unrelated or excluded. No repository change remains
unclassified.

### Focused validation and results

The launcher can create a virtual environment, install locked dependencies,
inspect serial devices, and start a server. Those effects were deliberately not
invoked during preparation. Existing local dependencies were used only for
non-hardware regression tests.

The following safe checks were run against inspection HEAD `c163a83`:

| Command | Result |
| --- | --- |
| `git diff --check f558b58..5b409a6` | Exit 0; no whitespace errors in the post-completion launcher delta. |
| `bash -n Software/LogicAnalyzerPy/start_web.sh` | Exit 0; launcher shell syntax is valid. |
| `.venv/bin/python -m pytest -q tests/unit/test_cli.py tests/implementation/test_web_boundary.py tests/implementation/test_web_api.py` | Exit 0; 21 passed, 1 restricted-sandbox loopback test skipped, 14 existing `aiohttp` `NotAppKeyWarning` warnings. The skip is not presented as new live-loopback proof. |
| `.venv/bin/python scripts/validate_cycle2_evidence.py docs/evidence-manifest/cycle2-schema.json testdata/evidence/c2-b1.json testdata/evidence/c2-b2.json testdata/evidence/c2-b3.json testdata/evidence/c2-b4.json testdata/evidence/c2-b5.json testdata/evidence/c2-b6.json` | Exit 0; all six accepted Cycle 2 manifests validate. |

No dependency was installed or updated; no decoder code, hardware, firmware,
serial operation, browser, server, network, or SSH command was executed. These
checks establish that the narrow launcher/documentation delta is suitable for
preservation as starting input. They do not independently accept every runtime
claim added to the README or launcher.

### Proposed Cycle 3 input baseline and exit-gate result

The unambiguous proposed Cycle 3 technical and governance input baseline is:

- commit: `c163a8353550e0b80dd7f001b21147659ad307ff`;
- tree: `45556769aab973c7671f58d57bae1878a46af9f2`;
- branch: `python-rewrite`;
- inherited accepted product identity: Cycle 2 candidate `2d5484a73d881496cdf5a35c799dfb01eedad229`, tree `8c76bce79922263468cb6ceaa4f1990703a84bfc`;
- included post-completion product/documentation delta: `5b409a6384624bfb6b51bc323c97a54244477dde`, subject only to the focused Step 1 validation claim above; and
- included governance input: `CYCLE3_PREPARATION.md` at `c163a83`.

Later commits that contain only preparation records, including the commit that
will add this file, may descend from this baseline without silently changing the
technical input identity. The final Cycle 3 launch preflight must record its own
then-current clean HEAD and tree and must separately account for any later
product change.

Step 1's classification exit gate is met: one exact proposed baseline exists,
all accepted-candidate descendants, both post-completion commits, and the sole
Step 1 worktree change have explicit dispositions, and no unrelated or excluded
change is hidden. The reconciliation was committed at `cb877ed` and its
preparation checklist gate was recorded at `e466203`.

## Step 2: technical-roadmap reconciliation

The factual revision of
[`Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md`](../../LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md)
reconciles its original Cycle 1 planning assumptions with the accepted Cycle 2
contracts and completion proof. It preserves the older decision log and broad
work packages as history and later-cycle context, but makes explicit that they
are not current Cycle 3 authority.

The revision records these accepted facts:

- Cycle 2 delivered ordered one-to-24-channel normal capture with 8-, 16-, and
  24-channel transfer modes and mode-appropriate `uint8`, `uint16`, and
  `uint32` sample storage;
- replay schema 1 remains readable, replay schema 2 is the canonical native
  write format, and generalized deterministic self-timed CSV import/export is
  accepted;
- deterministic transition and distinct-strobe parallel-bus analysis is
  delivered through the shared Python core, CLI/API contracts, browser table,
  and export surfaces;
- the accepted interactive application is the loopback-only
  React/TypeScript/Vite browser application with bounded Canvas rendering,
  offline replay/CSV workflows, live serial capture, lifecycle/security proof,
  and governed performance thresholds;
- PySide6/Qt, `.lac` interoperability, .NET dependence, packaging, public
  serving, and protocol decoders were explicitly excluded from Cycle 2; and
- the audited accepted support claim is macOS only. Historical Linux tests and
  CI records do not establish current Linux support.

The revision also removes already-complete Cycle 2 work from the Cycle 3
sequence. The focused Cycle 3 direction remains only a proposal for the
checked-in UART, SPI, and I2C decoder versions. It does not decide decoder trust
or provenance, in-process versus isolated execution, resource limits,
authoritative expected annotations, library/CLI/browser surfaces, platform
support, or physical-proof requirements. Those are operator choices owned by
Steps 3 and 4. Broader decoder compatibility and stacking, `.lac`, advanced
capture and editing parity, additional platforms, connectivity/device work, and
packaging remain Cycle 4-or-later candidates unless later approved contracts
say otherwise.

Step 2's content exit gate is met in the proposed revision: no known roadmap
statement presents PySide6, `.lac`, Linux support, or an already delivered
Cycle 2 capability as current Cycle 3 authority or unmet Cycle 2 work. Step 2
becomes durably complete only when the roadmap and this linked record are
committed together by the root orchestrator.

Step 2 was committed at
`cefb386` after the linked discovery revision was committed at `cb877ed`.

## Step 3: bounded technical discovery

### Method and non-execution boundary

Discovery used source and document inspection only. No decoder module was
imported or executed; no Python, .NET, browser, server, serial, hardware, or
firmware runtime was started; no dependency was installed or changed; and no
network provenance lookup was performed. File digests and Git history were
read as inert data. Consequently, the decoder behavior below is a static
contract inventory, not runtime conformance evidence.

The technical input remains the Step 1 baseline `c163a8353550e0b80dd7f001b21147659ad307ff`,
tree `45556769aab973c7671f58d57bae1878a46af9f2`. The later Step 1/Step 2
documentation commits do not change the inspected product or decoder sources.

### Exact evidence inspected

The minimum read-only evidence set was:

- governance and accepted baselines: `CYCLE3_PREPARATION.md`,
  `CYCLE2_ORCHESTRATION.md`, `CYCLE2_BATCH_EXECUTION.md`,
  `Software/LogicAnalyzerPy/docs/cycle-1-completion.md`,
  `Software/LogicAnalyzerPy/docs/cycle-2-discovery-review.md`,
  `Software/LogicAnalyzerPy/docs/cycle-2-contracts.md`,
  `Software/LogicAnalyzerPy/docs/cycle-2-completion.md`, the six active Cycle
  2 evidence manifests, and the Cycle 2 performance method, threshold, and
  completion records;
- current Python contracts and seams:
  `Software/LogicAnalyzerPy/pyproject.toml`, both Python lock files,
  `src/pico_logic_analyzer/model/capture.py`,
  `src/pico_logic_analyzer/formats/{capture,replay}.py`,
  `src/pico_logic_analyzer/analysis/bus.py`,
  `src/pico_logic_analyzer/cli/main.py`,
  `src/pico_logic_analyzer/web/server.py`, `docs/cli-contract.md`,
  `docs/replay-security-contract.md`, `web/openapi-b6.json`, the frontend API,
  shell, waveform, and geometry sources, and their implementation,
  verification, browser, native, security, cancellation, evidence, and
  performance tests;
- deterministic inputs: `testdata/protocol/`, `testdata/replay/README.md`,
  `web/benchmarks/fixtures.json`, the eight checked-in benchmark NPZ files,
  and `web/benchmarks/generate_fixtures.py`;
- decoder snapshot: `Software/decoders/sigrokdecode.py`, the `__init__.py` and
  `pd.py` files under `Software/decoders/{uart,spi,i2c}/`, and
  `Software/decoders/common/srdhelper/{__init__,mod}.py`;
- provenance and licensing: repository `LICENSE`, Git history for the decoder
  paths, the pre-import `.gitmodules` entry and `Software/SigrokDecode` gitlink,
  and decoder copyright/license headers; and
- behavioral reference only:
  `Software/LogicAnalyzer/LogicAnalyzer/SigrokDecoderBridge/` including
  `SigrokDecoderBase.cs`, `SigrokProvider.cs`, `SigrokPythonEngine.cs`,
  `SigrokDecodingTree.cs`, data/enums/templates, its embedded
  `sigrokdecode.py`, the decoder manager/options controls, and
  `LogicAnalyzer.csproj`.

No other bundled decoder was treated as Cycle 3 scope. The wider decoder tree
was inspected only to establish that broad directory discovery exists and that
UART, SPI, and I2C are a small explicit subset.

### Decoder identity, provenance, and licensing

All seven focused files have been unchanged in repository history since import
commit `407b5ef039aa0474c400c0721749baa126e53270` on 2024-10-12. Immediately
before that restructuring, `.gitmodules` named
`git://sigrok.org/libsigrokdecode` and `Software/SigrokDecode` was a gitlink to
upstream commit `0235970293590f673a253950e6c61017cefa97df`. The import commit
deleted that gitlink and added the flattened `Software/decoders/` snapshot.
The upstream commit object is not present locally, and the repository contains
no copy manifest or local-patch record. It is therefore reasonable but not
proven from local evidence that the flattened files are verbatim versions from
that exact upstream commit.

The exact checked-in identities are:

| Component | Declared identity | SHA-256 |
| --- | --- | --- |
| host shim `Software/decoders/sigrokdecode.py` | local API-v3 compatibility shim | `385124002ec16379a2542f2905c5ce41f3402032458d89f49617623ab7aaf01a` |
| UART package initializer | libsigrokdecode UART | `351098a23f5caa205068688550af53bd44a63776e1d02921ba32487ce720b92f` |
| UART `pd.py` | `id='uart'`, API 3, `gplv2+` | `67655f53162c531bc6eb77d9d29b384edec80a2dd5bd741897b4aa2afc52ffcc` |
| SPI package initializer | libsigrokdecode SPI | `91b207f82c59fe1c12ad1458ef669c4293c7e4c8dd19bec14e78b455305af56c` |
| SPI `pd.py` | `id='spi'`, API 3, `gplv2+` | `ef9cac5098404dc164094712e9175ba3715233248d8bbc23cb85ed3fc51d5d3d` |
| I2C package initializer | libsigrokdecode I2C | `37931874732ea0b3ca13784b8df4cd90949a2c1b5822feae5d5df6da81ee886f` |
| I2C `pd.py` | `id='i2c'`, API 3, `gplv2+` | `b6899137fb5b505433e696d319b7f3cc88519b43e2a2e7fea1a9f770ba10a305` |

UART and I2C additionally import the checked-in `common.srdhelper` package.
Its initializer and implementation digests are respectively
`125b0616dfdd974c2f6e0e83e61cf9cdd21340f9ab11ac7b97b648792dad05d1`
and `602b27901820a27af5fcf317b34af1a17d1449fa1ad21279507d1d5ab8acebd6`.
UART otherwise uses only `math`; SPI only `collections.namedtuple`; I2C has no
other import. No focused decoder imports the filesystem, network, subprocess,
dynamic-import, native-extension, or third-party package APIs.

Each libsigrokdecode file carries a GPL version 2-or-later notice and copyright
attribution. The repository root contains GPLv3 text, while the Python package
currently declares `license = {text = "MIT"}`. There is no decoder-local
COPYING file, packaged attribution manifest, or documented conclusion about
how bundling GPLv2+ decoder sources/helper code with the MIT-labelled Python
distribution must be represented. Process isolation does not by itself settle
distribution licensing. Cycle 3 therefore needs an explicit license and
packaging policy; this discovery makes no legal conclusion.

### Statically required API-v3 surface

The three decoders exercise a much smaller surface than the complete bundled
tree. A focused host would need exactly the following behavior if all currently
declared outputs remain in scope:

- constants `SRD_CONF_SAMPLERATE`, `OUTPUT_ANN`, `OUTPUT_PYTHON`,
  `OUTPUT_BINARY`, and `OUTPUT_META`; `OUTPUT_LOGIC` exists in the shim but is
  not used by these decoders;
- class metadata for `id`, names/descriptions, license, inputs/outputs/tags,
  required and optional channels, options, annotations, annotation rows, and
  binary declarations;
- host-populated `options`; lifecycle calls to construction/reset, `start()`,
  samplerate `metadata()`, and zero-argument `decode()`;
- `has_channel(index)` for optional/required mapping;
- `register(output_type, proto_id=None, meta=None)`, including the decoders'
  keyword `meta=(type, name, description)` registration;
- `put(start_sample, end_sample, output_id, data)` for annotation, Python,
  binary, and integer bitrate-metadata values;
- monotonically advancing `samplenum`, ordered Boolean `matched`, and `wait()`
  returning a tuple in declared channel order;
- `wait({})` immediate initial-sample behavior used by SPI; single conjunction
  dictionaries and alternative-condition lists; channel conditions `r`, `f`,
  `e`, and `h`; combined level-and-edge conditions; and `{'skip': N}` including
  zero skip. The focused decoders do not exercise `l` or `s`, despite the C#
  bridge implementing them;
- end-of-input termination that cannot be swallowed into an infinite host loop;
  the current shim turns a null `Wait` result into generic `Exception("Terminated")`;
  and
- arbitrary nested Python output values limited here to scalars, strings,
  lists, tuples, bytes, and SPI's `Data(ss, es, val)` namedtuple.

Static inspection does not settle lifecycle ordering, inclusive/exclusive end
sample semantics, simultaneous-match priority, zero-skip behavior at sample
zero, output ordering across registered streams, or the externally accepted
normal form for nested Python outputs. Those details require an explicit
contract and focused conformance fixtures before implementation.

### Focused decoder metadata and output shapes

| Decoder | Channels | Options | Declared output behavior |
| --- | --- | --- | --- |
| UART | RX and TX are both optional, but at least one is required | baud rate; 5-9 data bits; parity; stop bits; bit order; display format; RX/TX inversion; sample point; packet delimiters and lengths | 18 annotation classes/10 rows; Python start/data/parity/stop/error/break/frame/idle/packet records; RX/TX binary bytes |
| SPI | CLK required; MISO, MOSI, CS optional, but at least one data line is required | CS polarity, CPOL, CPHA, bit order, and word size whose valid host bounds must be defined | 7 annotation classes/7 rows; Python bit/data/CS-change/transfer records; MISO/MOSI binary data; integer bitrate metadata |
| I2C | SCL and SDA required | shifted or unshifted displayed address | 11 annotation classes/3 rows; Python start/repeated-start/stop/address/data/ACK/NACK/bits; four binary classes; integer bitrate metadata |

The checked-in metadata supplies defaults and enumerated choices but does not
supply all semantic validation. For example, SPI `wordsize` is not bounded in
its metadata, UART numeric delimiter/length values use sentinel `-1`, and UART
sample point silently falls back to 50 for invalid values. A public host must
decide whether to preserve every permissive decoder behavior or reject invalid
or resource-hostile values before execution.

### Current Python integration seams

The accepted Python core has no decoder package, host, public annotation model,
decoder command, annotation API, or browser annotation renderer today. The
useful existing seams are nevertheless narrow and stable:

- `CaptureResult` binds samplerate, trigger index, ordered physical channel IDs,
  labels/mapping, a rank-one mode-appropriate NumPy array, and
  `channel_samples(channel_id)`. Packed bit position follows request order, so
  decoder channel mapping must name physical IDs explicitly and translate them
  through `CaptureResult`, not index raw words by physical ID.
- Replay schema 1/2 and CSV import both produce the same validated
  `CaptureResult`; decoder execution can therefore be capture-source agnostic.
  Existing formats are inert and explicitly prohibit decoder nomination or
  executable metadata. A decode request must remain separate from the capture
  artifact.
- Bus analysis demonstrates deterministic sample/time formatting, bounded row
  production, CLI/API/browser sharing, and CSV export, but bus rows are not a
  suitable decoder-annotation model: annotations may overlap, occupy multiple
  rows/classes, carry several text alternatives, and emit Python/binary/meta
  records.
- The CLI parser and exit-code contract can accept a new explicit decode
  command, but no decoder-specific option/channel grammar or output schema is
  reserved. Adding one would require updating CLI contract, tests, help,
  machine-readable output, and error mapping without regressing accepted
  commands.
- The loopback API already provides bounded imports, capture identity,
  channels, waveform/bus views, one-operation ownership, capability+Origin
  mutation protection, cancellation state, rate/connection/request bounds,
  shutdown cleanup, and a closed OpenAPI/type fingerprint. Browser decoder
  support would therefore be a real cross-surface expansion: new API schema,
  generated types, operation ownership, annotation geometry/rendering,
  frontend interaction, security negatives, native proof, and performance
  gates—not a free presentation layer.
- Existing cancellation is appropriate to its owners: serial capture uses a
  cancellation event and characterized device recovery; offline import checks
  cancellation around a worker thread. Neither can forcibly stop arbitrary
  Python decoder bytecode or reclaim memory held by it. Decoder cancellation
  needs its own execution boundary.
- Existing evidence schemas are Cycle-specific and strict. Cycle 3 must create
  new manifests only after evidence exists and must bind decoder/helper hashes,
  fixture provenance, candidate/tree, locks, commands, results, environment,
  and independent reviews.

### C# bridge as a behavioral reference

The existing application confirms the intended broad concepts: decoder
metadata discovery, required/optional channel selection, typed options,
samplerate metadata, API-v3 wait conditions, registered annotation/Python/
binary/meta outputs, annotation rows, and stacked decoder trees. It embeds the
same shim digest as `Software/decoders/sigrokdecode.py` and publishes the full
decoder directory. Its `Wait` implementation provides alternative and
conjunctive conditions, skip, `samplenum`, and `matched` semantics useful for
comparison.

It must not be copied as the Cycle 3 security or correctness contract. It:

- scans every decoder directory and dynamically imports each module;
- embeds Python in-process through pythonnet 3.0.5 and dynamically compiles C#
  wrapper types;
- supports stacking and broad discovery beyond the proposed focused scope;
- catches several decoder exceptions without structured reporting;
- has no decoder wall-time, memory, recursion, or output-volume limit and no
  forceful cancellation boundary;
- locates a machine Python runtime and writes initialization logs; and
- exposes UI-shaped annotation objects rather than a frozen Python public
  contract.

It is therefore a static code-inspection reference only. The operator has
prohibited executing the C# application or bridge for fixture generation,
differential output, verification, or any other Cycle 3 purpose. No runtime
result from it may be treated as evidence. Cycle 3 must not depend on .NET or
pythonnet merely because the reference uses them.

### Deterministic capture and annotation evidence

Available inputs are strong for capture regression but insufficient as decoder
acceptance oracles:

- accepted literal V2 identity/capture fixtures prove framing and 8/16/24-bit
  packing, not UART/SPI/I2C protocol conversations;
- replay and CSV tests generate deterministic inert captures, while the B5
  corpus supplies constant, sparse, dense, Gray-code-like, maximum, and
  parallel-bus patterns with frozen digests;
- physical Cycle 1/2 observations prove periodic square waves and byte-boundary
  packing, not expected decoder annotations; and
- no checked-in file identifies a UART frame, SPI transfer, or I2C transaction
  together with independently reviewed expected annotation/Python/binary/meta
  output and sample intervals.

Some existing NPZ patterns could exercise termination and output-volume
bounds, but using them as protocol truth would invent expectations after seeing
decoder output. Focused protocol fixtures must instead be generated from an
independent declarative description or hand-reviewed sample timeline, with
expected outputs derived independently of the host under test. Those reviewed
fixtures are authoritative. C# and upstream sources may inform static code
inspection, but neither C# nor an external/reference libsigrokdecode runtime may
be executed to generate, corroborate, differentially compare, verify, or accept
fixture outputs.

### Trust, isolation, resource, platform, dependency, and performance implications

Decoder files are executable Python even though the three inspected versions
have benign imports. Capture artifacts must never choose a module/path or add
code to `sys.path`; only a host-owned allowlist bound to the frozen hashes can
select code. Options and channel mappings are inert data but require exact-key,
type, enumeration, range, and size validation before crossing the execution
boundary.

An in-process host is the smallest implementation and avoids serialization,
but a stuck loop, excessive allocation, recursion failure, global mutation, or
interpreter crash shares the CLI/server process. Threads cannot forcibly stop
Python bytecode or reliably reclaim it. A dedicated subprocess per request (or
single-use bounded worker) gives the parent a kill/reap boundary and keeps
decoder imports out of the API/browser process. It requires a frozen IPC
schema, deterministic environment/import path, stderr/stdout handling, cleanup,
and tests for spawn failure, timeout, cancellation, partial/malformed output,
signal termination, and orphan prevention. This discovery recommends the
subprocess direction, but Step 4 must approve it and its precise security claim.

Independent limits are needed for input sample count, channel count, option
payload, wall deadline, cancellation latency, worker memory/address space,
recursion, annotation count, aggregate output bytes, per-text length, nested
container depth/items, and retained captures/results. Exact numeric ceilings
cannot responsibly be selected from static source alone. macOS process/memory
limit behavior and the chosen worker's cancellation/reaping behavior need a
bounded pre-threshold experiment. Parent-side output accounting and wall-time
termination remain necessary even if OS resource limits are available.

The accepted baseline is Python >=3.12 with NumPy, pyserial, optional aiohttp,
and a macOS-only support claim. The focused decoder imports require no new
third-party runtime package if a native compatibility host is written. The
decoder files are outside the Python package today, so packaging their exact
allowlisted files and helper is an explicit product/license choice. .NET,
pythonnet, and libsigrokdecode are prohibited as production, development, test,
fixture-generation, and verification dependencies or executables. The focused
native host must add none of them. Static source inspection is allowed;
`sigrok-cli` is likewise outside the focused host and is not an approved
reference executable.

The accepted CI has only a macOS support claim. Subprocess semantics, resource
measurement, and performance are platform-sensitive; historical Linux code or
CI cannot establish Linux support. Cycle 3 should retain macOS-only support
unless the operator deliberately funds and proves another platform.

No decoder performance baseline exists. Decoder work can emit more records
than input samples, and UART skip-heavy, SPI edge-heavy, and I2C mixed-condition
paths stress different host behavior. The Cycle 2 governance pattern remains
appropriate: first freeze fixtures, method, machine/environment identity, raw
observations, and deterministic resource counts; then independently review a
threshold proposal; only after explicit approval enforce regression and
absolute ceilings. Browser inclusion would also require annotation render and
interaction measurements integrated with the existing production benchmark.

### Candidate public workflows and material alternatives

The smallest coherent product surface is a headless library plus CLI:

1. caller supplies a validated `CaptureResult`, one allowlisted decoder ID,
   explicit decoder-channel-to-physical-channel mapping, and validated options;
2. a bounded worker receives only packed logic samples, samplerate, mapping,
   decoder ID, and inert options;
3. the host returns a deterministic, typed result containing decoder identity,
   annotation rows/segments, and whichever Python/binary/meta outputs the
   operator approves, with sample indices authoritative and time derived from
   capture samplerate/trigger; and
4. the CLI reads replay or explicit-metadata CSV and writes a canonical JSON
   representation (and only any separately approved annotation export), with
   existing exit-code and overwrite discipline.

Material alternatives are:

- **Library only:** smallest public contract, but lacks an end-to-end user
  workflow and independently exercisable installed entry point.
- **Library plus CLI (recommended):** proves practical offline use without
  expanding the local-web attack and rendering surfaces.
- **Library, CLI, and browser:** highest immediate utility, but owns new API,
  capability, operation, cancellation, UI, accessibility, native, and
  performance obligations. It should be selected only explicitly.
- **In-process execution:** less IPC work, but can claim only cooperative
  cancellation/failure handling and cannot isolate hangs or memory exhaustion.
- **Isolated subprocess (recommended):** supports a bounded kill/reap claim at
  the cost of an IPC and platform contract.
- **Checked-in files only (recommended):** exact allowlist and hashes; user
  decoder directories, capture-selected code, arbitrary module names, stacking,
  and broad decoder import compatibility remain later work.
- **Synthetic/replay proof (recommended):** sufficient for deterministic
  protocol semantics because decoding consumes digital samples; a physical
  live capture/decode demonstration adds integration confidence but also
  hardware authority, wiring, provenance, and repeatability obligations.
- **Independently reviewed fixtures (recommended):** avoids a circular oracle
  and supplies the sole authoritative expected output. Static C# or upstream
  source inspection may inform review, but runtime reference corroboration and
  differential execution are prohibited.

At Step 3 completion, all alternatives in this section were proposals only.
The Step 4 record below now approves, replaces, or defers the applicable
choices and governs any conflicting alternative.

### Uncertainty classification

| Topic | Classification | Discovery disposition |
| --- | --- | --- |
| Proposed starting baseline and accepted regression surfaces | Locally resolved | Step 1 exact identities and Cycle 1/2 completion evidence govern. |
| Focused file identities, imports, metadata, hashes, and API calls | Locally resolved | Static inventory above is exact for the checked-in baseline. |
| Whether any focused file changed after repository import | Locally resolved | No later path commit exists after `407b5ef`. |
| Whether flattened files exactly equal upstream gitlink `0235970` and what import-time patches exist | Bounded static comparison needed | If available without adding a prohibited dependency or executable, obtain that exact upstream source object from an approved source and compare inert bytes; never execute it. |
| Runtime conformance of wait/matched/skip/lifecycle/output ordering | Bounded experiment needed | Freeze independently derived, reviewed contract fixtures, then run only the future native host against them. |
| Authoritative expected-annotation source and role of reference output | Resolved by operator | Independently derived, reviewed fixtures are authoritative; no C# or external/reference libsigrokdecode runtime output is permitted. |
| Decoder scope and exact executable allowlist | Resolved by operator | Exact checked-in UART, SPI, and I2C decoders and their required helper only, pinned by hash. |
| Library/CLI/browser accepted surfaces and approved output classes | Resolved by operator | Typed headless library plus installed CLI; browser annotation display and interaction are deferred. |
| In-process versus subprocess execution and security claim | Resolved by operator | Use a single-use isolated subprocess with parent-enforced deadline, output bounds, cancellation, and kill/reap. |
| Numeric timeout, cancellation, memory, recursion, output, and retention ceilings | Approved procedure; bounded experiment then threshold approval needed | Measure frozen stress fixtures first and separately approve exact ceilings before enforcement. |
| macOS subprocess/resource-limit behavior and cancellation latency | Bounded experiment needed | Exercise only after the isolation choice is approved. |
| License/attribution/package metadata for GPLv2+ decoders in the currently MIT-labelled Python project | Resolved policy with required review | Retain notices and reconcile decoder packaging with the Python package's MIT metadata before distribution. |
| Production or non-production need for pythonnet, .NET, or libsigrokdecode | Resolved by operator | They are prohibited as dependencies and executables in production, development, testing, fixture generation, and verification; static source inspection alone is allowed. |
| Platform and CI support beyond macOS | Resolved by operator | Retain the accepted macOS-only support claim. |
| Replay/synthetic-only versus live physical decode acceptance | Resolved by operator | Deterministic offline fixtures suffice; no live physical capture/decode gate is required. |
| Decoder stacking, user discovery, all-decoder compatibility, `.lac`, decoder-selected files, and capture-selected code | Deferred outside focused Cycle 3 | Retain roadmap exclusions unless the operator expressly changes scope. |
| Packaging, release publication, additional OS support, advanced capture/editing/connectivity, and later parity | Deferred outside Cycle 3 | No discovery evidence requires pulling these into the decoder cycle. |

### Risks and recommended controls

1. **Executable-code escape:** prevent any capture, CSV, replay, API field, or
   user path from naming code; bind a host-owned ID allowlist to file hashes and
   a closed import root.
2. **Denial of service:** place execution behind the approved isolation
   boundary; enforce parent-side deadline/output limits, worker cleanup, and
   independently approved memory/recursion/retention bounds.
3. **Semantic drift:** freeze channel position mapping, sample intervals,
   simultaneous matches, output ordering, annotations, defaults, validation,
   and canonical serialization against independent fixtures.
4. **Circular evidence:** derive expected protocol events from reviewed sample
   timelines, not by copying implementation or reference runtime output; C# and
   upstream sources are static-inspection evidence only.
5. **License/provenance ambiguity:** retain notices and exact hashes, recover
   and compare the pinned upstream commit, document local deltas, and reconcile
   Python package metadata before distribution.
6. **Browser scope leakage:** if browser output is approved, treat decode as a
   bounded protected operation and update closed OpenAPI/types, security,
   cancellation, rendering, native, and performance proofs together.
7. **False portability:** keep macOS-only claims until exact worker and resource
   gates pass on any additional platform.
8. **Evidence lifecycle error:** do not create manifests before evidence;
   preserve exact candidate/tree and role-separated implementation,
   verification, accumulated validation, and acceptance ordering.

### Proposed completion evidence

Subject to Step 4 decisions and later batch ownership, a credible Cycle 3 final
proof set should contain:

- a committed provenance/license inventory binding every executable/helper file
  to SHA-256, upstream source/commit, verified local delta, notices, package
  placement, and approved license policy;
- a frozen API-v3 compatibility matrix and black-box tests for every condition,
  lifecycle field, output type, channel/option rule, termination case, and
  sample/order semantic actually exercised by the accepted decoders;
- independently derived UART, SPI, and I2C sample timelines covering defaults,
  material option modes, optional/required channels, valid traffic, malformed
  or incomplete traffic, simultaneous conditions, end-of-input, and exact
  annotation/Python/binary/meta results;
- deterministic repeatability across live-model, replay, and CSV-derived
  `CaptureResult` inputs where those sources are approved, proving that no file
  can nominate executable code;
- hostile worker/IPC tests for wrong decoder ID/hash, unknown imports, invalid
  options/mappings, exception, infinite loop, timeout, cancellation, recursion,
  memory pressure, excessive/nested/malformed output, worker crash, partial IPC,
  cleanup, and subsequent successful decode;
- public library typing and installed CLI black-box proof, plus closed
  OpenAPI/generated-type/security/browser/native proof only if the browser
  surface is approved;
- fresh clean Python 3.12 hash-locked install, dependency check, Ruff, strict
  mypy, all non-hardware regression, accepted CLI help, exact-candidate macOS
  hosted CI, and preservation of all Cycle 1/2 manifests and rollback paths;
- a frozen decoder performance/resource method, raw baseline, independently
  reviewed threshold proposal, explicit operator approval, and final
  enforcement on representative and worst focused fixtures; and
- immutable candidate/tree-bound implementation, verification, accumulated,
  security, performance, acceptance, manifest, checkpoint, and completion
  records in the ordering later frozen by the governing contracts.

Live physical proof is not part of the approved Cycle 3 acceptance boundary.
Any later proposal to add it would require new operator authority and an
operator-confirmed safe wiring/protocol source, sanitized capture/decode
evidence, replay of the exact captured bytes through the same host, and no
persistent device change.

### Recommendations presented for Step 4

At Step 3 completion these were proposals only. They are separated here into
the ten operator-decision topics required by `CYCLE3_PREPARATION.md`; the Step 4
record below is authoritative where it approves, replaces, or strengthens a
proposal.

1. limit Cycle 3 execution to the exact checked-in UART, SPI, and I2C files and
   their required helper, pinned by hash;
2. accept a typed headless library plus installed CLI, and defer browser
   annotation interaction unless the operator values it enough to own the
   additional API/security/native/performance scope;
3. execute only the host allowlist; prohibit user, capture, replay, CSV, or
   request-selected paths/modules and defer stacking/all-decoder discovery;
4. use a single-use isolated subprocess with parent-enforced deadline, output
   bounds, cancellation, kill/reap, and structured failure;
5. use independently reviewed synthetic/replay protocol timelines as the
   authoritative oracle; Step 3 also identified reference-runtime
   corroboration as an alternative for operator consideration;
6. freeze exact numeric resource and performance thresholds only after bounded
   baseline experiments, then obtain explicit threshold approval;
7. add no production .NET, pythonnet, or libsigrokdecode dependency;
8. retain GPLv2+ notices and reconcile decoder provenance, packaging, and the
   Python package's MIT license metadata before distribution;
9. retain the accepted macOS-only platform and CI support claim; and
10. accept deterministic offline proof without a mandatory live physical
    capture/decode workflow.

### Step 3 exit-gate assessment

Step 3's content exit gate is met in this revision. The inspected sources,
exact focused identities and API surface, current integration seams, evidence
gaps, security/isolation choices, dependency/license/platform/performance
implications, material alternatives, classified uncertainties, risks, and
proposed completion evidence are explicit. The operator can decide the Cycle 3
product, trust, platform, and proof boundaries without an implementor inventing
them.

This Step 3 assessment did not itself complete Step 4, approve any
recommendation, settle the final contract surface, authorize a bounded
experiment, or start Cycle 3. The following operator record now completes the
Step 4 decision gate without starting implementation.

## Step 4: operator decisions

On 2026-08-25, the operator resolved all ten presented decision topics as
follows:

1. **Focused decoder scope — approved as proposed.** Cycle 3 is limited to the
   exact checked-in UART, SPI, and I2C decoder versions and their required
   checked-in helper, all pinned by hash.
2. **Accepted product surface — approved as proposed.** The accepted surface is
   a typed headless Python library plus an installed CLI. Browser annotation
   display and interaction are deferred outside Cycle 3.
3. **Executable trust boundary — approved as proposed.** Only the host-owned,
   hash-pinned checked-in allowlist may execute. User-, capture-, replay-, CSV-,
   request-, or path-selected modules, stacking, and broad decoder discovery
   are prohibited or deferred.
4. **Execution isolation — approved as proposed.** Decoder execution must use a
   single-use isolated subprocess with parent-enforced deadline, bounded
   output, cancellation, structured failure, and kill/reap behavior. The later
   contract must state the precise bounded-process security claim and must not
   imply protection beyond that boundary.
5. **Expected-output authority — proposal replaced.** Independently derived,
   reviewed fixtures are the sole authoritative source for expected
   annotations and other outputs. C# is static code-inspection evidence only
   and must never be executed for Cycle 3; C# differential runtime output is
   prohibited. External/reference libsigrokdecode runtime output is likewise
   prohibited. Static upstream byte comparison may be considered for
   provenance only when it adds no prohibited executable or dependency, and it
   cannot replace the authoritative reviewed fixtures.
6. **Resource and performance thresholds — approved as proposed.** Freeze the
   fixture set, method, environment identity, raw baseline, and deterministic
   resource counts first; then obtain separate explicit operator approval for
   exact timeout, cancellation, memory, recursion, output, retention, and
   performance ceilings before enforcing them.
7. **Dependency boundary — proposal strengthened.** .NET, pythonnet, and
   libsigrokdecode are prohibited as production, development, test,
   fixture-generation, and verification dependencies or executables. Static
   source/code inspection is allowed. The focused native host must add none of
   them. This prohibition does not exclude the future native host from
   executing the three approved checked-in decoder snapshots; it excludes
   installing or invoking a libsigrokdecode host/runtime, library, CLI, package,
   or other external reference implementation.
8. **Provenance and licensing — approved as proposed.** Preserve the exact
   decoder/helper identities, hashes, attribution, and GPLv2+ notices, and
   reconcile decoder packaging with the Python package's MIT metadata before
   distribution. This is a required project/legal review gate, not a legal
   conclusion in this document.
9. **Platform and CI claim — approved as proposed.** Cycle 3 remains macOS-only;
   historical or incidental execution elsewhere establishes no additional
   support claim.
10. **Physical proof — approved as proposed.** Deterministic offline replay and
    synthetic fixtures suffice. Cycle 3 has no mandatory live physical
    capture/decode workflow.

These decisions supersede every unapproved Step 3 alternative, especially the
earlier possibility of C# or libsigrokdecode runtime corroboration and the
weaker production-only dependency exclusion. They do not authorize decoder
execution or implementation during preparation.

### Step 4 exit-gate assessment

All ten operator decisions are resolved. No remaining operator choice can
materially change the proposed Cycle 3 objective, executable trust boundary,
macOS-only platform claim, authoritative proof source, or stopping condition.
Step 4's content exit gate is met in this revision; committing this revision
will satisfy its required durable-output gate. Numeric thresholds deliberately
remain subject to the approved baseline-then-approval procedure and do not
reopen the Cycle 3 scope or trust decisions.

## Step 5: frozen narrow Cycle 3 contract surface

This section is normative input to the later Cycle 3 governing contracts. It
settles the product and trust decisions that implementation, verification, and
acceptance agents must not reinterpret. Where static inspection cannot prove an
API-v3 edge semantic or justify a numeric ceiling, the section names a closed
decision gate and its earliest owner instead of allowing an implementor to pick
an answer. Step 6 may rename or split the proposed batches, but it must preserve
their dependency order and the named gate before dependent implementation.

### Executable identity, provenance, license, and imports

The executable decoder allowlist is closed to these checked-in files at the
digests recorded in Step 3:

- `Software/decoders/sigrokdecode.py`;
- `Software/decoders/uart/{__init__.py,pd.py}`;
- `Software/decoders/spi/{__init__.py,pd.py}`;
- `Software/decoders/i2c/{__init__.py,pd.py}`; and
- `Software/decoders/common/srdhelper/{__init__.py,mod.py}`.

The public decoder IDs are exactly `uart`, `spi`, and `i2c`; an ID is resolved
through a host-owned constant table, never as an import name or path supplied by
a caller. Before every worker launch, the parent must verify every file required
by that decoder against the frozen digest table and fail closed before executing
anything on a missing, extra, replaced, unreadable, or mismatched file. Symlink,
path traversal, alternate package root, namespace-package merging, bytecode-only
substitution, environment `PYTHONPATH`, user-site, and current-directory module
shadowing are not valid resolution mechanisms.

The permitted import graph is also closed. Decoder code may import only the
frozen local `sigrokdecode` compatibility module, the frozen local
`common.srdhelper` package, and these Python-standard-library names statically
required by the frozen files: `math.floor`, `math.ceil`,
`collections.namedtuple`, `enum.Enum`, `enum.IntEnum`, `enum.unique`,
`itertools.chain`, and `re`. The worker must use an import root constructed by
the host and reject any other decoder-originated import. This is an allowlist
for the three trusted snapshots, not a general Python sandbox or a claim that a
subprocess makes arbitrary Python safe.

The provenance record must retain import commit `407b5ef`, prior gitlink
`0235970`, all file hashes, copyright attributions, and GPLv2-or-later notices.
An inert byte comparison with an approved source copy may establish the exact
upstream delta; neither that comparison nor an unavailable upstream object may
delay freezing the checked-in hashes as Cycle 3 identity. Before the decoder
files enter a distributable Python artifact, a recorded project/legal review
must reconcile their GPLv2+ terms and notices with the package's current MIT
metadata and state the package placement and resulting metadata. No governing
contract may claim that process isolation resolves licensing.

### Required API-v3 compatibility host

The native compatibility host implements only the following closed surface:

- constants `SRD_CONF_SAMPLERATE = 0`, `OUTPUT_ANN = 0`,
  `OUTPUT_PYTHON = 1`, `OUTPUT_BINARY = 2`, and `OUTPUT_META = 4`;
  `OUTPUT_LOGIC` is not supported;
- the focused decoder class metadata enumerated in Step 3, host-populated
  `options`, `samplenum`, and `matched`, plus `has_channel()`, `wait()`,
  `register()`, and `put()`; no other libsigrokdecode API is promised;
- one fresh decoder instance and fresh interpreter process per request, with
  constructor/reset initialization, host option injection, `start()`, exactly
  one samplerate `metadata(SRD_CONF_SAMPLERATE, positive_integer_hz)` call, and
  zero-argument `decode()` in that order; normal end of capture is a host-owned
  non-catchable termination path rather than a decoder-visible generic
  `Exception`, and all other decoder exceptions are failures;
- `has_channel(index)` returns a real `bool` and is true exactly for a decoder
  channel present in the validated mapping;
- every returned pin-tuple element is an exact built-in `int`. A mapped pin is
  `0` or `1`; an unmapped optional pin is the exact integer sentinel `0xFF`
  (`255`). The tuple always retains the full declared required-then-optional
  channel length and order. Required pins can never be absent. `has_channel()`
  is false exactly for an optional pin whose tuple slot is `0xFF`; the sentinel
  is never exposed in the public capture or result and is never interpreted as
  a logic level. This intentionally matches the inert inspected C# source;
- `register(output_type, proto_id=None, meta=None)` accepts only the four
  supported output constants, assigns monotonically increasing request-local
  integer output IDs in call order beginning at zero, preserves the supplied
  `meta` declaration, and otherwise ignores `proto_id` because stacking is
  excluded;
- `put(ss, es, output_id, value)` accepts only a registered request-local
  output ID and integer sample coordinates, validates the output-specific value
  shape, and appends one immutable record with a monotonically increasing
  request-wide emission index. It never sorts, merges, clips, repairs, or drops
  an accepted record; and
- `samplenum` is the zero-based index of the sample returned by the most recent
  `wait()`. The pin tuple always follows the decoder's declared required-then-
  optional channel order. An unmapped optional channel is represented only to
  the decoder compatibility layer by integer `0xFF` as frozen above and is
  never confused with a captured logic level.

`wait()` is limited to `wait({})`, one condition dictionary, or a non-empty
list of condition dictionaries. A dictionary is conjunction; the list is
alternatives. Supported channel predicates are `r`, `f`, `e`, and `h`, and the
only non-channel predicate is `{'skip': N}` for a non-negative integer `N`.
Predicates `l` and `s`, `None`, unknown keys/codes, mixed skip-and-channel
conditions, empty alternative lists, duplicate/invalid channel indexes, and
non-integer or negative skips are outside the focused API and fail validation.
For an alternative list, `matched` is a same-length tuple of real booleans;
every condition true at the returned sample is marked true, even when multiple
alternatives match simultaneously. For a single dictionary or `wait({})`,
`matched` is a one-element tuple.

The following API-v3 edge details cannot be established authoritatively by
static inspection alone and must be frozen by reviewed, independently derived
black-box fixtures in the earliest proposed provenance/API/fixture batch
(`C3-B1` unless Step 6 renames it), before any general host implementation:

1. whether the first `wait({})` returns sample 0 without advancement and the
   exact behavior of any later `wait({})` call;
2. whether condition searches begin at the current sample or the next sample,
   the previous-sample definition at index 0, and exact `skip: 0` and positive
   skip advancement;
3. priority when a level-and-edge conjunction and multiple alternatives become
   true on the same sample;
4. whether `put()` end coordinates are closed or half-open for presentation,
   and the accepted treatment of decoder-calculated coordinates at or beyond
   the capture boundary; and
5. whether normal end-of-input may preserve a final partial protocol unit and,
   if so, which already-emitted records remain visible.

The B1 fixture review must select one answer per item, based on the checked-in
decoder source, independently specified sample timelines, and API-v3
compatibility needs. It must record exact expected calls and results and obtain
independent verification and acceptance before the host batch consumes them.
No C#, .NET, pythonnet, libsigrokdecode, `sigrok-cli`, upstream decoder runtime,
or other reference executable may be run to make or corroborate these choices.
A correction after that gate requires a new reviewed fixture candidate, not an
implementation-local compatibility exception.

### Inputs, mappings, and options

The library accepts an already validated, non-empty `CaptureResult`, one closed
decoder ID, a mapping from decoder channel ID to physical channel ID, and an
option mapping. The samplerate comes only from the capture. Physical IDs are
resolved through the capture's ordered `channel_ids`; raw packed words are
never indexed by physical ID. Mapping keys must be known decoder channel IDs,
values must be distinct physical IDs present in the capture, all required
channels must be mapped, and no undeclared key is accepted. UART requires at
least one of `rx`/`tx`; SPI requires `clk` and at least one of `miso`/`mosi`,
with `cs` optional; I2C requires both `scl` and `sda`.

Options are a closed mapping. Omitted known keys receive the exact checked-in
defaults; unknown keys, duplicate CLI assignments, booleans presented as
integers, coercion from strings inside the library, NaN/infinity, and values
outside the rules below are configuration failures before worker launch:

- UART: `baudrate` is a positive integer; `data_bits` is one of 5, 6, 7, 8,
  or 9; `parity` is one of `none`, `odd`, `even`, `zero`, `one`, or `ignore`;
  `stop_bits` is one of 0.0, 0.5, 1.0, 1.5, or 2.0; `bit_order` is
  `lsb-first` or `msb-first`; `format` is `ascii`, `dec`, `hex`, `oct`, or
  `bin`; `invert_rx` and `invert_tx` are each `yes` or `no`; `sample_point`
  is an integer from 1 through 99 rather than relying on the decoder's silent
  fallback; each packet delimiter is `-1` or an integer representable by the
  selected data-bit width; and each packet length is `-1` or a positive
  integer. `-1` alone disables the respective delimiter or length rule.
- SPI: `cs_polarity` is `active-low` or `active-high`; `cpol` and `cpha` are
  integer 0 or 1; `bitorder` is `msb-first` or `lsb-first`; and `wordsize` is a
  positive integer. Its exact maximum is a resource ceiling owned by the B1
  baseline/threshold proposal and subsequent explicit operator approval; until
  approved, no SPI word size beyond the checked-in default of 8 is eligible for
  implementation or acceptance.
- I2C: `address_format` is exactly `shifted` or `unshifted`.

Input sample count and serialized option/mapping size also require numeric
ceilings under the threshold procedure below. Until those ceilings are
approved, B1 fixtures use only their reviewed finite sizes and no public host
surface may be declared complete.

B1 must commit a closed decoder-option coverage matrix before characterization.
For every checked-in option key it enumerates the default, every enumerated
choice, every inclusive/exclusive numeric boundary, and every sentinel. Each
entry has exactly one disposition: `direct-fixture` with a named fixture,
`static-equivalence` with the named directly covered fixture and a source-based
equivalence argument, or `unsupported` with the contract rule that rejects it
before launch. UART packet `-1` sentinels and width boundaries, sample-point
boundaries, every UART enumeration, every SPI enumeration and word-size
boundary, and both I2C choices are explicit rows. B3 audits the complete matrix
against the accepted fixture digests; B5 repeats that audit. “Material
options” alone is never a coverage disposition.

### Deterministic result, annotation, and time contract

The accepted output contains all four kinds emitted by the focused snapshots:
annotation, Python, binary, and integer metadata. A typed `DecodeResult` binds
the decoder ID and frozen file-set identity, integer samplerate, canonical
channel mapping, fully materialized options, capture sample count and trigger
index, declared annotation classes/rows and binary/meta declarations, and an
emission-ordered tuple of output records. Every record carries its emission
index, registered output ID and kind, start and end sample coordinates, and a
typed value. Annotation records preserve class index and ordered text
alternatives. Binary records preserve binary class and bytes. Metadata records
preserve the registered integer definition and integer value.

Python output is normalized at the worker boundary into a closed tagged value
tree containing only null, bool, integer, finite float, UTF-8 string, bytes,
list, tuple, and SPI `Data(ss, es, val)`. Container kind and order are
preserved; bytes use canonical base64 in JSON; the SPI namedtuple becomes a
tagged `spi-data` value with integer `ss`, `es`, and `val`. Dictionaries,
sets, arbitrary objects, non-finite floats, unknown namedtuples, cycles, and
values beyond approved depth/item/byte limits are protocol failures, not
stringified output.

Request-wide emission order is authoritative across output kinds and
registered streams. Per-row presentation may derive a stable view ordered by
`(start_sample, end_sample, emission_index)` but may not change the underlying
order. Repeated identical requests against identical capture bytes, mapping,
options, decoder hashes, and limits must produce byte-identical canonical
serialization or the same stable typed failure.

Sample coordinates, not floating-point timestamps, are authoritative. Derived
absolute seconds are `sample / samplerate`; trigger-relative seconds are
`(sample - trigger_index) / samplerate`. Canonical machine output carries
integer sample coordinates and rational time components (integer numerator and
positive integer samplerate denominator); decimal rendering is presentation
only and must use one frozen formatting rule inherited from the accepted
capture time contract. The B1 edge-semantic fixture gate above freezes interval
endpoint interpretation before any annotation presentation is implemented.

#### Normative decode-result schema version 1

The public semantic and JSON contract is separately versioned as
`pico-logic-analyzer.decode-result/v1`. Canonical JSON is UTF-8, contains no
BOM, uses no insignificant whitespace, sorts every object key by Unicode code
point, emits integers as base-10 JSON integers, emits booleans/null as JSON
literals, escapes strings by the standard JSON rules without ASCII-only
forcing, and ends in exactly one LF. Arrays preserve the order stated below.
No unlisted field, `null` substitute, float timestamp, or non-finite number is
accepted.

The byte encoder is exactly Python 3.12
`json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
allow_nan=False).encode("utf-8") + b"\n"`; no alternate canonicalizer is a
conforming CLI path. Thus finite floats, including signed zero and exponent
form, use Python 3.12's JSON rendering, while integer fields never pass through
a float.

The root is an object with exactly these fields and types:

- `schema`: the literal string `pico-logic-analyzer.decode-result/v1`;
- `decoder`: object `{id: string, file_set_sha256: string}` where `id` is the
  closed decoder ID and the digest is 64 lowercase hexadecimal characters over
  the ordered path/NUL/file-digest manifest frozen by B1;
- `samplerate_hz`: positive integer;
- `channels`: array in decoder declaration order of objects
  `{decoder_channel: string, physical_channel: integer}` containing mapped
  channels only;
- `options`: object whose keys are canonically sorted and whose values are only
  the fully materialized string, integer, or finite JSON number allowed by the
  frozen option table (booleans are not integers);
- `capture`: object `{sample_count: positive integer, trigger_index:
  non-negative integer}` with `trigger_index < sample_count`;
- `declarations`: object with `annotations`, `annotation_rows`, `binary`, and
  `metadata` arrays. Annotation entries are
  `{index: non-negative integer, id: string, description: string}`; row entries
  are `{index: non-negative integer, id: string, description: string,
  annotation_indices: array of non-negative integers}`; binary entries are
  `{index: non-negative integer, id: string, description: string}`; metadata
  entries are `{output_id: non-negative integer, value_type: "integer",
  name: string, description: string}`. Declaration arrays retain checked-in or
  registration order; and
- `records`: the request-wide emission-order array described next.

Every record has `emission_index`, `output_id`, `kind`, `start_sample`,
`end_sample`, `start_time`, `end_time`, and `value`. Indices and coordinates
are non-negative integers and emission indices are contiguous from zero. Each
`start_time`/`end_time` is exactly
`{absolute: {numerator: integer, denominator: positive integer},
trigger_relative: {numerator: integer, denominator: positive integer}}`.
Absolute numerator is the corresponding sample coordinate; trigger-relative
numerator is `sample - trigger_index`; every denominator is `samplerate_hz`,
without floating-point conversion or reduction. `kind` and `value` are exactly
one of:

- `annotation`: `{class_index: non-negative integer, texts: non-empty array of
  strings}`;
- `python`: one tagged value object. Tags are `null` (no `value` field),
  `bool`, `integer`, `float`, `string`, `bytes`, `list`, `tuple`, or
  `spi-data`. Scalar tags have exactly one `value` of the named JSON type; the
  float is finite; bytes value is canonical padded RFC 4648 base64; list/tuple
  value is an ordered array of tagged values; and `spi-data` has exactly
  integer fields `ss`, `es`, and `val` plus `tag`;
- `binary`: `{class_index: non-negative integer, data_base64: string}` using
  canonical padded RFC 4648 base64; or
- `metadata`: `{value_type: "integer", value: integer}` matching its registered
  metadata declaration.

The public immutable class set is exactly `DecodeResult`, `DecoderIdentity`,
`DecodeCaptureIdentity`, `DecodeDeclarations`, `AnnotationDeclaration`,
`AnnotationRowDeclaration`, `BinaryDeclaration`, `MetadataDeclaration`,
`RationalTime`, `RecordTime`, the closed `DecodeRecord` union of
`AnnotationRecord`, `PythonRecord`, `BinaryRecord`, and `MetadataRecord`, and
the closed tagged `PythonValue` variants named by the JSON tags above. Their
snake-case fields and scalar types match the schema fields exactly; every JSON
array is an immutable tuple in the library, `options` is an immutable sorted
tuple of `(str, scalar)` pairs that serializes to the JSON object, and no model
has an extension field. They serialize only through this one schema. B1's
independently authored
fixture candidate includes literal expected typed-object vectors and literal
CLI UTF-8 golden bytes for every record/value tag before product result or CLI
implementation. Those artifacts have independent verification and acceptance,
are identified by digest, and are consumed unchanged by R9, R17, and R18.

Host failures use the separately versioned taxonomy
`pico-logic-analyzer.decode-error/v1`. The immutable library failure has
exactly `schema`, `code`, and bounded path/traceback-free `message`; `code` is
one of `snapshot`, `import`, `ipc`, `decoder`, `recursion`, `memory`,
`process-exit`, `timeout`, `cancelled`, or `output-limit`. Configuration and
mapping failures remain the existing configuration class/CLI exit 2, and input
replay/CSV failures remain the existing input class/CLI exit 5. The ten host
codes map to CLI exit 7, emit no JSON to stdout, and use one stable bounded
stderr diagnostic line. Unknown failures may not be relabeled success or
serialized with an invented tag.

### Public library and installed CLI only

The public library surface is a typed module under
`pico_logic_analyzer.decode` exposing immutable request/result/value models and
one synchronous `decode_capture(capture, decoder_id, channels, options,
limits=None) -> DecodeResult` operation. `limits` may only select values no
weaker than the approved host ceilings; callers cannot disable isolation,
digest checks, output validation, cancellation/reaping, or the allowlist. The
governing contracts may refine Python type names for consistency, but may not
add a dynamic decoder path, an in-process mode, or a second semantic result
shape.

The installed `pico-la` entry point gains one offline command:

```text
pico-la decode (--replay PATH | (--csv PATH --channels D0,D1,...
               [--sample-rate HZ] --trigger-channel PHYSICAL_CHANNEL
               --edge {rising,falling})) --decoder {uart,spi,i2c}
               --channel DECODER_CHANNEL=PHYSICAL_CHANNEL
               [--channel ...] [--option KEY=VALUE] [--option ...]
```

It writes exactly one canonical compact, sorted-key JSON result plus LF to
stdout on success and no machine data to stdout on failure. Replay and explicit-
metadata CSV are mutually exclusive and use their already accepted inert
parsers; CLI strings are parsed to the same closed typed option rules before
calling the library. Duplicate channel/option keys, overwrite/export options,
stdin code or capture input, decoder paths, plugin directories, and implicit
live capture are not supported. Existing exit meanings remain unchanged;
configuration and mapping errors return 2, input replay/CSV validation returns
5, and a new documented exit 7 covers decoder digest/import/IPC/exception/
resource/deadline/cancellation failures. Diagnostics go only to stderr.

`--channels` is the ordered physical `channel_ids` tuple and is separate from
repeatable decoder mapping `--channel`. For CSV, `--channels`,
`--trigger-channel`, and `--edge` are always required. `--sample-rate` is also
required except for the exact accepted legacy D0-D7 header, where omission
selects only the accepted legacy time-column inference; supplying it always
overrides inference and its times must validate. All four CSV metadata options
are forbidden with `--replay`. CSV content never overrides supplied metadata,
and no decoder option or mapping can supply capture metadata. Duplicate,
empty, out-of-range, mismatched-label, non-distinct, or otherwise parser-
invalid metadata fails as input/exit 5 before decoder mapping or worker launch.

No browser endpoint, OpenAPI addition, generated web type, frontend renderer,
web operation, or annotation interaction is part of Cycle 3. The library and
CLI must not import or require the optional web dependency.

### Worker, IPC, cancellation, and failure isolation

Each decode uses a newly spawned, single-request Python worker launched through
an installed package-owned entry point, not a shell and not a caller-provided
command. The parent supplies a deterministic minimal environment and explicit
closed import root, disables user-site and inherited Python import paths, uses a
non-user-controlled working directory, and passes only inert validated request
data. The worker receives one length-framed, versioned request over a dedicated
pipe and returns length-framed, versioned records over a separate dedicated
pipe. Protocol stdout is not decoder stdout; incidental stdout and stderr are
separately captured under small parent-enforced limits and never parsed as IPC.
The worker accepts exactly one request and exits.

The parent accounts for request bytes, record count, aggregate encoded and
decoded output bytes, text/bytes length, nested items/depth, and all diagnostic
bytes while streaming; it must not first allocate an untrusted declared length.
It rejects wrong protocol versions, unknown fields/tags/output IDs, malformed
frames, truncated/extra data, invalid coordinates/types, limit overruns, and a
success result followed by abnormal worker exit. Partial output is never
returned as success.

Cancellation is parent-owned and race-safe. A cancellation request or deadline
expiry stops accepting output, terminates the worker, escalates to force-kill
when the approved grace expires, closes every pipe, reaps the exact child, and
returns one stable typed failure. Spawn/import failure, decoder exception,
recursion failure, memory/allocation failure, IPC corruption, signal exit,
unexpected exit, timeout, cancellation, and output-limit breach are distinct
typed failure categories but reveal no traceback or local path in canonical
machine output. After any failure, the parent must have no live worker, open
worker descriptor, retained partial result, or poisoned global decoder state;
an immediately subsequent valid request must succeed.

The worker must apply the independently approved address-space/allocation and
recursion ceilings before importing decoder code. The parent always retains its
own wall deadline and byte/count limits. The security claim is deliberately
narrow: this boundary contains ordinary Python exceptions, hangs, recursion,
bounded output, and worker-process allocation up to the characterized macOS
controls, and supplies deterministic kill/reap cleanup. It does not claim an OS
sandbox, privilege separation, protection from arbitrary malicious native code,
or portability beyond macOS. Decoder snapshots remain trusted, hash-pinned code.

### Inert capture/decoder boundary and fixture authority

Replay, CSV, capture metadata, channel labels, options, IPC values, and decoder
outputs are data only. None may supply or influence a module/package/path,
import root, code string, command, environment variable, working directory,
output file, or dynamic type lookup. Decoder identity is an explicit API/CLI
enum resolved solely by the parent allowlist. Decoder code has no supported
filesystem, network, subprocess, dynamic-import, native-extension, environment,
serial, firmware, or hardware capability. A test that merely stores a decoder-
like name or path in a capture must prove it remains inert.

Authoritative fixtures begin from a human-reviewable declarative protocol
timeline: samplerate, finite per-channel logic transitions, physical mapping,
options, and expected protocol meaning. Capture samples and every expected
annotation/Python/binary/meta record are derived independently of the host and
decoder output, checked in with generator/version/digests, and reviewed by a
verifier who did not implement the host. Expected data must cover each decoder's
complete accepted option-coverage matrix, required/optional mappings, valid and malformed or
incomplete traffic, simultaneous waits, start/end boundaries, normal
termination, and exact ordering. Equivalent live-model, replay, and CSV-derived
captures must produce the same result where those sources represent identical
samples and metadata.

C# source and upstream source may be inspected as inert explanatory material
only. C# must never run. .NET, pythonnet, libsigrokdecode, `sigrok-cli`, an
upstream/reference decoder host, or any other differential runtime must never
be installed, imported, linked, invoked, or used in production, development,
fixture generation, tests, verification, performance work, or acceptance.
Their output cannot corroborate a fixture. Dependency locks, clean-environment
proof, process inspection, and CI must demonstrate their absence.

That absence audit is scoped to every active Cycle 3 Python product,
development, test, fixture, characterization, verification, performance,
acceptance, CI, bootstrap, lock, distribution, import, active-process, command,
and evidence path. Preserved C# project/source metadata is an inert historical
rollback and inspection surface and may name a historical dependency; it is
never restored, built, installed, imported, loaded, or executed for Cycle 3
and never supplies evidence. Ambient installation or availability on a machine
alone is not Cycle 3 use and is not a reason to mutate the machine; invocation,
import, linkage, dependency resolution, active process, command reference, or
evidence reliance by any in-scope path is prohibited.

### Baseline-first thresholds and intentionally staged gates

No numeric resource or performance ceiling is frozen by this static review.
Before the first characterization runner or approved snapshot executes, B1
must commit an exact conservative experiment-only safety envelope covering
wall deadline, terminate-to-force-kill grace, input samples/request bytes,
output records and encoded/decoded bytes, stdout/stderr/diagnostic bytes,
nested depth/items, recursion, and worker memory/address space. A verifier
independently recomputes that the runner enforces every cap and an acceptance
identity passes the same envelope and fixture candidate. A capped termination
or limit breach is an observation, never a passing baseline; no cap may be
weakened to obtain data. The later explicitly operator-approved product
threshold record replaces this experiment-only envelope and may be stricter
but never authorizes rerunning the baseline with weaker experiment caps.

The earliest proposed B1 must then commit the reviewed semantic/stress fixture
set and measurement method, including machine/OS/Python identity, warm-up and
repetition rules, raw observations, deterministic input/output counts, and the
macOS mechanisms proposed for process memory, recursion, deadline, and reaping.
It must measure, without executing any prohibited runtime:

- input samples and request bytes;
- spawn/import and decode wall time plus cancellation/kill/reap latency;
- worker peak memory/address space and parent retained memory;
- recursion behavior;
- output record, encoded/decoded byte, per-text/per-bytes, nested depth/item,
  diagnostic, and retained-result counts; and
- representative UART skip-heavy, SPI edge-heavy/default-word-size, I2C mixed-
  condition, malformed, dense-output, and hostile-worker cases.

Only after those raw baselines and methods receive independent review may a
threshold proposal name exact input, timeout, cancellation grace, memory,
recursion, output, nesting, diagnostic, retention, and performance ceilings,
including the SPI maximum word size. Exact values require separate explicit
operator approval and a committed decision record. The later contracts must
make that approval a blocking prerequisite to the first public host batch and
must require final enforcement on the exact candidate. A changed fixture,
method, environment class, worker model, or weakened ceiling invalidates the
approval and requires a new proposal; an implementation may not silently tune
a gate to pass.

Thus the intentionally staged decisions are limited to numeric ceilings and the
five API-v3 fixture semantics listed above. Their choices are owned by reviewed
B1 artifacts and, for numeric thresholds, the operator; no implementor,
verifier, or acceptance agent may resolve them informally.

### Explicit exclusions

Cycle 3 excludes decoder stacking or decoder-to-decoder inputs, user/system
decoder discovery, arbitrary decoder import compatibility, capture/request-
selected executable code, decoder-selected files, output files or exports,
`.lac`, browser/API/frontend annotation integration, live physical proof,
firmware/hardware changes, packaging/publication, Linux or Windows support, and
all later capture/editing/connectivity/parity work. It also excludes every
production and non-production dependency on or execution of .NET, C#,
pythonnet, libsigrokdecode, `sigrok-cli`, and external/reference decoder hosts.
Static inspection of already available source is the sole permitted use of C#
or upstream/reference material.

### Step 5 exit-gate assessment

The narrow Cycle 3 surface is frozen: executable identity and imports, license
gate, API-v3 subset, mappings/options, typed outputs and ordering, sample/time
authority, library/installed-CLI workflows, single-use worker and IPC behavior,
cancellation/failure cleanup, inert-data boundary, independent fixture oracle,
baseline-then-approval procedure, and exclusions are explicit. The only
unfrozen values are the five statically unprovable API-v3 edge semantics and
numeric resource/performance ceilings; each has a named reviewed B1 gate, and
numeric choices additionally require explicit operator approval before public
host implementation. Independent implementation, verification, and acceptance
agents therefore have no authority to make a substantive product or trust
decision. Step 5's content exit gate is met in this revision; committing this
revision will satisfy its durable-output gate.

## Step 6: proposed batches, proof ownership, and stopping conditions

This section is normative input to the later governing contracts. It turns the
settled Step 5 surface into five dependency-ordered batches. A batch owns a
required behavior at the earliest point where that behavior can be proved; all
final accumulated proof is owned by C3-B5. Repetition by a later batch is a
regression gate, not a transfer of ownership. The contracts may refine command
names and owned paths, but may not reorder these dependencies, merge away an
independent gate, or move a requirement later without a new common-commit
review.

The sequence deliberately puts authoritative semantic fixtures, a
characterization method, raw baselines, an independently reviewed threshold
proposal, and explicit operator threshold approval in C3-B1. No public decoder
host, library entry point, or CLI decode command may be implemented before that
checkpoint. C3-B1 may contain a non-installed, characterization-only runner for
the exact approved snapshots. It is not a product host, is never selected by a
capture or caller, and may execute only after the approved Cycle 3 goal starts.
Its source, environment, and results must be immutable evidence so that the
later exact-candidate measurements can be compared with the same method.

### Common batch mechanics and role ownership

Every batch has one implementation identity, a different verification
identity, a third acceptance identity, and a post-acceptance manifest-verifier
identity distinct from the orchestrator and evidence assembler. The orchestrator
is another role:
it integrates changes, creates the immutable product candidate, runs the full
accumulated gate, assembles evidence only after it exists, and appends the
checkpoint. The verifier must derive expectations from the settled contract
and independently reviewed fixtures rather than from production output. The
acceptance agent audits the candidate, verifier findings, accumulated results,
scope, provenance, and evidence ordering and never repairs the candidate.
A B2-B4 product implementor must not have authored B1's authoritative expected
outputs. If an identity would cross that boundary, a fresh implementation
identity is assigned for the dependent product work.

The mandatory ordering for every batch is:

1. record a bounded active-batch entry and pass prerequisite/authority
   preflight;
2. create or identify a focused failing check, then implement only the owning
   surface;
3. pass implementation-focused checks and commit one immutable candidate;
4. have the independent verifier test that exact candidate and record exactly
   `pass` or `changes_required`;
5. have the orchestrator run the batch's complete accumulated gate against the
   same candidate commit and tree;
6. have the independent acceptance agent audit the exact candidate, all
   findings and dispositions, and accumulated evidence and record exactly
   `pass` or `changes_required`;
7. only then create that batch's manifest atomically; have the assigned
   manifest verifier independently recompute every digest, validate the schema,
   and create an immutable record naming candidate, manifest digest, commands,
   results, and verdict; then commit the manifest and verification record
   together and append the checkpoint;
   and
8. select the next batch only after the checkpoint is committed.

No future-batch manifest, placeholder, template presented as evidence, or
checkpoint record may be created. A manifest is a descendant of the tested
candidate and names that candidate's full commit and tree; evidence documents
and the manifest do not masquerade as part of the tested product tree. Any
product, fixture, method, dependency, limit, or test correction after candidate
creation produces a new candidate and invalidates every earlier verifier,
accumulated, and acceptance pass for that batch. Prior records remain immutable
history. A regression of a completed interface reopens its earliest owning
batch and every dependent accumulated gate.

The exact non-hardware command list is frozen in C3-B1 after clean-environment
characterization. At minimum, every accumulated gate includes a fresh
Python 3.12 hash-locked development install, no-dependency editable install,
`pip check`, Ruff, strict mypy, the complete non-hardware pytest suite, installed
CLI help, the Cycle 1/2 evidence validator, and a dependency/process audit for
the prohibited runtimes. Existing web regressions may be run only as unchanged
Cycle 2 regression coverage; no Cycle 3 browser source, endpoint, fixture,
dependency, launch, or browser evidence is added. Exact-candidate hosted macOS
CI is required at C3-B4 and C3-B5. A restricted local skip is not CI proof.

### Proposed batch boundaries

#### C3-B1: provenance, semantic fixtures, and approved limits

**Outcome:** The exact executable snapshot and license disposition are
recorded; independent declarative UART, SPI, and I2C fixtures freeze the five
API-v3 edge semantics; the characterization method and raw observations exist;
and all numeric resource/performance ceilings, including maximum SPI word size,
have independent review and explicit operator approval.

**Prerequisites and authority gates:** The Cycle 3 governing contracts and goal
have their required common-commit passes and the operator has invoked the goal.
Until then no decoder executes. Static work may not silently become execution
evidence. Any dependency download, hosted CI run, or capability requiring
environment approval is routed through the root orchestrator. Project/legal
review must record decoder source placement, notices, and project metadata
before the snapshots are exposed by the editable source installation. Building
a distributable artifact remains excluded.

**Settled interfaces:** The Step 5 file/digest and import allowlists, declarative
timeline format, typed output normal form, five edge-semantic questions,
measurement categories, and macOS-only claim. The timeline and expected-output
format is independent of the later host wire format.

**Internal gate order:** First commit an immutable semantic-fixture candidate
containing the declarative timelines, independently calculated expected calls
and records, exact sentinel/mapping fixtures, the closed option-coverage
matrix, version-1 typed-object/JSON golden vectors, all five API-edge decisions,
and the exact experiment-only safety envelope. A verifier and acceptance identity
must pass that exact fixture candidate before the characterization runner is
implemented or any snapshot is executed. A correction creates a new fixture
candidate and transfers no pass. Only the accepted fixture candidate may feed
the later characterization method. Raw results then precede the threshold
proposal; proposal verification precedes acceptance; and explicit operator
approval is last. The final B1 candidate binds every intermediate identity and
digest and receives the normal complete B1 verification and acceptance sequence
before its manifest exists.

**Implementation ownership:** Provenance/license inventory; human-reviewable
timeline schema and independently derived expected records; deterministic
fixture generator; characterization-only runner; frozen clean-environment and
measurement method; raw results and deterministic counts. The runner is not
installed or imported by the product and exposes no public API.

**Verification ownership:** Independently review every timeline and expected
record; prove the generator does not consume decoder/host output; inspect the
closed imports and hashes; recompute enforcement of the pre-execution envelope;
audit every option-matrix row and the RX-only/TX-only and MISO-only/MOSI-only/
no-CS sentinel fixtures; reproduce the method and raw observations; exercise
representative, boundary, dense-output, malformed, cancellation/reap, and
hostile-worker cases; and issue a distinct threshold-proposal verdict.

**Acceptance and operator ownership:** The acceptance identity audits fixture
independence, edge-semantic decisions, provenance/license disposition, method,
raw data, and verifier findings. Only after that review does the orchestrator
propose exact ceilings. The verifier reviews the proposal, the acceptance
identity records its verdict, and the operator explicitly approves or amends
the committed values. These values include input samples/request bytes,
deadline and cancellation grace, worker memory/address space, recursion,
record/encoded/decoded/text/bytes/item/depth/diagnostic/retention limits,
performance ceilings, and SPI maximum word size. No default of convenience is
an approval.

**Focused proof:** Fixture-schema/generator tests; byte-stable fixture rebuild;
literal review of defaults, options, mappings, all output kinds, ordering, and
the five edge cases; file/import/license audit; reproducible raw characterization
report; threshold-proposal review; acceptance verdict; and the explicit
operator decision record. Decoder execution uses only the approved checked-in
snapshots and never C#, .NET, pythonnet, libsigrokdecode, `sigrok-cli`, or an
external/reference runtime.

**Accumulated proof:** Accepted Cycle 1/2 non-hardware regression and evidence
validation, clean dependency audit, and the new B1 focused proof. B1 cannot
checkpoint with an unresolved numeric value, provisional SPI maximum, changed
method, or absent operator decision.

#### C3-B2: isolated compatibility host and containment

**Outcome:** A private native host consumes validated inert requests, executes
one hash-pinned focused decoder in one single-use process, returns the settled
typed result, and enforces the approved containment and cleanup behavior. It is
not yet a public library API or installed CLI command.

**Prerequisite:** C3-B1 complete, including the immutable fixture set and
operator-approved numeric ceilings. A fixture, method, worker model, or ceiling
change reopens C3-B1 before B2 proceeds.

**Settled interfaces:** Closed decoder ID/file/import tables; mapping and option
rules; lifecycle and API-v3 subset; wait/matched/samplenum/skip semantics;
register/put rules; output normal form and ordering; versioned length-framed
IPC; approved limits; typed failures; process launch, cancellation, kill, close,
and reap behavior; inert-data boundary; and the narrow macOS containment claim.

**Implementation ownership:** Internal immutable request/result/value models;
digest and import-root enforcement; input, mapping, and option validation;
API-v3 compatibility primitives; single-use worker and streaming IPC; output
validation; all approved counters/limits; parent-owned deadline/cancellation;
typed failure conversion; and deterministic cleanup. Product code must not
import a prohibited runtime or provide an in-process/dynamic-decoder mode.

**Verification ownership:** Black-box mutation of IDs, hashes, paths, symlinks,
environment/import shadowing, mappings, options, frames, lengths, tags, output
IDs, coordinates, nested values, diagnostics, exits, signals, exceptions,
hangs, memory/recursion pressure, output floods, cancellation races, and partial
IPC. Verify no partial success, traceback/path disclosure, descriptor/worker
leak, retained result, or poisoned subsequent request. Recompute limit
boundaries without production counters.

**Acceptance ownership:** Audit every Step 5 host primitive and containment
claim against the exact candidate, confirm no public surface was added early,
and confirm the approved limits were enforced without weakening or rebasing.

**Focused proof:** Internal host unit/contract tests, B1 API-edge fixtures,
adversarial IPC/process tests, deterministic repeated serialization, worker
lifecycle/process inspection, prohibited-import/dependency tests, and
post-failure successful decode.

**Accumulated proof:** B1 immutable fixture rebuild and threshold identities,
all B2 focused checks, and the canonical accepted Cycle 1/2 non-hardware and
evidence gates.

#### C3-B3: focused UART, SPI, and I2C conformance

**Outcome:** The private host produces every settled output kind for the exact
UART, SPI, and I2C snapshots across every accepted option-matrix row, mappings,
boundaries, malformed/incomplete traffic, and equivalent capture sources.

**Prerequisite:** C3-B2 complete. Decoder identities, fixture semantics, and
numeric ceilings remain byte-for-byte those accepted at B1.

**Settled interfaces:** B1 declarative timelines and expected records; B2
private request/result contract; capture channel/sample/time authority;
decoder-specific required/optional mappings and option domains; all annotation,
Python, binary, and metadata declarations; and request-wide emission order.

**Implementation ownership:** Only decoder-specific adapters or tables needed
to feed the generic B2 host and preserve exact metadata/results. Shared-host
exceptions, decoder-source edits, or fixture-derived hard-coded output are not
allowed.

**Verification ownership:** Independently materialize equivalent
`CaptureResult`, schema-1/schema-2 replay, and explicit-metadata CSV inputs from
reviewed timelines; compare complete typed results and canonical bytes; test
each row of the accepted closed option-coverage matrix, required and optional
channel combination,
noncontiguous/reordered physical mapping, start/end and simultaneous events,
incomplete/malformed traffic, and repeatability. Static source inspection is
the only allowed use of C# or upstream material.

**Acceptance ownership:** Audit complete focused-decoder coverage, confirm all
expected data remains fixture-owned, and confirm no decoder-specific behavior
expanded the host API or trust boundary.

**Focused proof:** Separate UART, SPI, and I2C conformance reports; full output
record comparisons; cross-source equality; option/mapping negative tests; exact
digest/import proof; and byte-identical repeat runs.

**Accumulated proof:** B1 fixtures/limits, B2 containment/failure matrix, B3
decoder conformance, and all inherited non-hardware/evidence regressions.

#### C3-B4: public library and installed CLI

**Outcome:** The settled synchronous typed library and offline installed CLI
expose the already accepted private host without adding a second semantic path,
dynamic code selection, optional-web dependence, or live capture.

**Prerequisite:** C3-B3 complete with all three focused decoders accepted.

**Settled interfaces:** `pico_logic_analyzer.decode` immutable models and
`decode_capture(...)`; non-weakenable caller limits; the exact `pico-la decode`
grammar; mutually exclusive replay/CSV input; canonical JSON plus LF; stderr
diagnostics; existing exits plus decoder failure exit 7; and no browser/API,
serial, stdin-code, export, or decoder-path surface.

**Implementation ownership:** Public type annotations and stable exports;
library delegation to the one B2 path; CLI parsing/mapping/options, inert
replay/CSV loading, canonical serialization, diagnostics, and exits;
documentation; package resource placement as allowed by the B1 license review;
and hash-locked dependency metadata with no prohibited dependency.

**Verification ownership:** Editable-install black-box library and CLI tests
from outside the source directory; success-byte and stderr/exit fixtures;
all duplicate/unknown/invalid input cases; replay/CSV equivalence; absence of
serial or web import/open; no caller limit weakening; clean installation and
dependency/process inspection; and exact-candidate hosted macOS CI.

**Acceptance ownership:** Audit public compatibility and documentation, package
notices/metadata, CLI machine contract, optional-web independence, lock
closure, macOS-only claim, and CI identity. No publication is authorized.

**Focused proof:** Strict mypy public-surface use, installed library examples,
installed CLI golden/negative tests, clean hash-locked bootstrap and `pip
check`, source-resource/license audit, prohibited-runtime/dependency/process
audit, and exact-candidate hosted CI.

**Accumulated proof:** All B1-B3 gates plus public black-box tests, full existing
CLI/core/web regression without Cycle 3 browser changes, clean lint/type/test
and evidence validation, and exact-candidate CI.

#### C3-B5: exact-candidate accumulated proof and completion

**Outcome:** One immutable final product candidate satisfies every Cycle 3
stopping condition and every inherited regression, security, resource,
performance, dependency, licensing, platform, and rollback claim has
independent evidence.

**Prerequisite:** C3-B4 complete; no unresolved finding, unexplained repository
delta, changed approved fixture/method/limit, or missing operator decision.

**Settled interfaces:** Every accepted B1-B4 checkpoint and the complete
requirement/proof map below. B5 introduces no new product behavior and may not
rebase fixtures or thresholds.

**Implementation ownership:** Only corrections in the reopened earliest owning
batch; otherwise assemble no product change. Any correction creates a new
candidate and reruns all dependent verification.

**Verification ownership:** Independently rerun the complete semantic,
decoder-conformance, containment/failure, public library/CLI, clean-install,
dependency, and exact-candidate performance/resource suites; verify every
artifact digest and the absence of excluded changes and processes.

**Acceptance ownership:** Audit the exact final candidate/tree, the completed
B1-B4 role sequences/manifests/checkpoints, the proposed B5 manifest inputs and
readiness (but not a nonexistent B5 manifest/checkpoint), every finding and
disposition, accumulated local and CI result, approved-limit enforcement,
support/rollback statement, repository state, and numbered stopping checklist.
Record one pre-manifest `pass` or `changes_required`. After a pass, a distinct
manifest-verifier identity recomputes the proposed B5 manifest's digests and
schema, records its candidate, commands, manifest digest, results, and verdict,
then the orchestrator commits the manifest and checkpoint. A separate
completion-closure auditor finally checks the committed B5 manifest,
verification record, checkpoint, and completion proof without changing them.

**Focused proof:** Final-review packet completeness, digest/schema audit,
repository/prohibited-action audit, and stopping-condition traceability.

**Accumulated proof:** Fresh clean Python 3.12 bootstrap; dependency check;
Ruff; strict mypy; all non-hardware tests; installed CLI help and black-box
decode; Cycle 1/2 evidence validation; B1 fixture regeneration; all three
decoder suites; full process/IPC/security/cancellation cleanup matrix; final
measurements against the unchanged approved thresholds on the characterized
macOS class; exact-candidate hosted macOS CI; license/resource audit; and a
second independent verification of the final evidence digests.

### Requirement-to-proof ownership map

The `R` identifiers below are stable proposed contract identifiers. Each row
has exactly one earliest owner and exactly one final accumulated owner. A batch
manifest may reference its row, but the table and a proposed filename are not
evidence.

| ID | Required outcome | Earliest owner and objective proof | Final accumulated owner |
| --- | --- | --- | --- |
| R1 | Exact UART/SPI/I2C/helper identities, provenance, hashes, closed imports, notices, and package-license disposition | C3-B1: independent file/import/provenance audit and project/legal decision record | C3-B5 |
| R2 | Independently derived declarative timelines and expected outputs are the sole oracle | C3-B1: literal fixture review, generator-independence audit, and byte-stable rebuild | C3-B5 |
| R3 | Five API-v3 edge semantics are frozen before host implementation | C3-B1: numbered expected-call fixtures with verifier and acceptance passes | C3-B5 |
| R4 | Measurement method, raw resource/performance baseline, and deterministic counts are reproducible | C3-B1: independently reproduced characterization report | C3-B5 |
| R5 | Every numeric ceiling and maximum SPI word size has independent review and explicit operator approval | C3-B1: committed proposal, verifier verdict, acceptance verdict, and operator decision | C3-B5 |
| R6 | Decoder ID, files, imports, environment, and input data cannot select executable code | C3-B2: allowlist/digest/path/symlink/shadowing and inert-metadata adversarial tests | C3-B5 |
| R7 | Capture, mapping, samplerate, and option validation is exact and occurs before worker launch | C3-B2: boundary/type/mapping/option tests with spawn counter | C3-B5 |
| R8 | Required API-v3 lifecycle, wait/matched/samplenum/skip/register/put behavior matches frozen semantics | C3-B2: B1 semantic fixtures against private host | C3-B5 |
| R9 | Typed outputs preserve the version-1 declarations, tags, values, coordinates, rational time, and request-wide emission order deterministically | C3-B1: independent typed-object and canonical-JSON golden identities; C3-B2 consumes them in shape/order/serialization/repeat tests | C3-B5 |
| R10 | Versioned framed IPC rejects malformed, oversized, partial, extra, or unknown data without partial success | C3-B2: independently generated hostile-frame matrix | C3-B5 |
| R11 | Deadline, cancellation, memory, recursion, output, diagnostic, and retention limits are parent-enforced | C3-B2: boundary/overrun tests against approved values and independent counters | C3-B5 |
| R12 | Every failure kills/closes/reaps cleanly and a subsequent valid decode succeeds | C3-B2: process/descriptor inspection and post-failure decode matrix | C3-B5 |
| R13 | UART defaults/options/mappings and annotation/Python/binary outputs conform | C3-B3: authoritative UART timeline/result comparisons | C3-B5 |
| R14 | SPI defaults/options/mappings and annotation/Python/binary/meta outputs conform through the approved word-size maximum | C3-B3: authoritative SPI timeline/result comparisons | C3-B5 |
| R15 | I2C defaults/options/mappings and annotation/Python/binary/meta outputs conform | C3-B3: authoritative I2C timeline/result comparisons | C3-B5 |
| R16 | Equivalent in-memory, replay-schema-1/2, and explicit-metadata CSV captures yield identical results | C3-B3: independently materialized cross-source comparisons; no physical I/O | C3-B5 |
| R17 | Public typed synchronous library implements the version-1 immutable models, delegates to the sole isolated host, and cannot weaken limits | C3-B4: installed black-box/type tests against B1 expected object vectors and limit-delegation audit | C3-B5 |
| R18 | Installed offline CLI grammar, explicit CSV metadata, version-1 canonical JSON, stderr, failure taxonomy, and exits are exact | C3-B4: installed golden/negative CLI suite against B1 literal bytes | C3-B5 |
| R19 | Core/library/CLI remain independent of optional web and never open serial or add browser behavior | C3-B4: import/open spies, dependency extras audit, and unchanged web regression | C3-B5 |
| R20 | Clean Python 3.12 locked installation, static checks, tests, and macOS CI pass | C3-B4: fresh bootstrap and exact-candidate hosted CI | C3-B5 |
| R21 | Prohibited runtimes/dependencies have no invocation, import, linkage, resolution, active process, command, or evidence reliance in any scoped active Cycle 3 path; preserved C# metadata remains inert | C3-B1: scoped fixture/provenance/dependency-method audit; enforced continuously from the first execution | C3-B5 |
| R22 | Approved resource/performance ceilings are enforced without rebasing | C3-B2: enforcement boundary tests; B1 owns values, B2 owns enforcement behavior | C3-B5 |
| R23 | Cycle 1/2 behavior, manifests, rollback paths, and macOS-only claim remain intact | C3-B1: inherited regression/evidence baseline; rerun by each batch | C3-B5 |
| R24 | Candidate, role separation, finding, manifest, checkpoint, and correction ordering is immutable and auditable | C3-B1: first completed role/evidence sequence under the approved schema | C3-B5 |
| R25 | Excluded browser, hardware, firmware, live capture, dynamic decoder, stacking, `.lac`, publication, and unsupported-platform work did not occur | C3-B1: scope/prohibited-action audit begun and carried by every checkpoint | C3-B5 |
| R26 | Final exact candidate meets all approved performance/resource thresholds on the characterized macOS environment class | C3-B5: fresh final measurements; this is final-only proof, not a new earlier product requirement | C3-B5 |

R21, R23, R24, and R25 begin in B1 and are mandatory accumulated audits in
every later batch. R22 deliberately separates value ownership (R5/B1) from
enforcement ownership (R22/B2), avoiding a circular gate. R26 is inherently a
final-candidate observation and therefore has B5 as both earliest and final
owner. No row has more than one earliest owner.

### Operator and execution gates

The following gates are blocking, not findings that an implementor may resolve:

1. decoder execution begins only after the approved goal is invoked;
2. only the Step 5 hash-pinned snapshots may execute, with no prohibited
   runtime or dependency in any role;
3. the B1 project/legal disposition precedes exposing decoder sources through
   the editable source installation; no distributable artifact is built;
4. raw B1 measurements precede the numeric proposal, independent proposal
   review precedes acceptance, and explicit operator approval precedes B1
   completion or any public host implementation;
5. maximum SPI word size is part of that same later explicit operator decision,
   not an implementation choice;
6. a changed fixture, method, environment class, worker model, or weakened
   ceiling reopens B1 and requires a new proposal/review/operator decision;
7. only the root orchestrator may arrange required dependency/network/hosted-CI
   execution authority; and
8. no hardware, firmware, serial, live capture, browser, .NET/C#, pythonnet,
   libsigrokdecode, `sigrok-cli`, or external/reference-runtime gate exists in
   Cycle 3. Encountering one is a scope violation, not a reason to request it.

Safe independent documentation, fixture review, and static inspection may
continue while an external execution approval is pending, but no checkpoint
may claim missing execution, CI, legal/project, threshold, or operator evidence.

### Numbered final stopping-condition checklist

Cycle 3 is complete only when one exact C3-B5 candidate satisfies all of the
following objective conditions:

1. The exact UART, SPI, I2C, shim, and helper files, digests, provenance,
   notices, closed imports, package placement, and license metadata match the
   accepted B1 record.
2. Independently derived, byte-reproducible fixtures cover the three decoders,
   all declared output kinds, the complete option-coverage matrix, integer
   `0xFF` optional-pin semantics including RX-only/TX-only and MISO-only/
   MOSI-only/no-CS, malformed/incomplete traffic, boundaries, simultaneous
   waits, ordering, the version-1 object/JSON goldens, and the five frozen
   API-v3 edge semantics.
3. The approved method, environment identity, raw B1 observations, numeric
   ceilings, maximum SPI word size, independent reviews, and explicit operator
   decision are immutable and mutually consistent.
4. The parent resolves only host-owned decoder IDs, verifies every required
   digest, constructs the closed import environment, and proves all capture and
   request metadata inert before each worker launch.
5. Exact capture, samplerate, channel mapping, and option validation rejects
   every invalid input before process creation.
6. One fresh worker implements only the frozen API-v3 subset and returns the
   complete deterministic typed result with authoritative sample coordinates,
   rational time, and request-wide emission order.
7. Versioned streaming IPC and output normalization reject malformed,
   oversized, unknown, partial, extra, cyclic, or non-finite data without
   returning partial success.
8. Approved deadline, cancellation, memory, recursion, output, nesting,
   diagnostic, retention, and performance ceilings are enforced; every failure
   closes and reaps the exact worker and a subsequent valid decode succeeds.
9. Authoritative UART, SPI, and I2C suites pass every accepted option-matrix row,
   required/optional and reordered physical mappings, boundary traffic, and all
   annotation/Python/binary/meta outputs applicable to each decoder.
10. Equivalent in-memory capture, replay schema 1/2, and explicit-metadata CSV
    inputs produce byte-identical canonical results without physical I/O.
11. The installed typed library and `pico-la decode` command satisfy their
    exact version-1 object/JSON/failure, explicit-CSV-metadata, stderr, exit,
    non-weakenable-limit, and
    no-live-capture contracts from outside the source tree.
12. Fresh Python 3.12 hash-locked installation, `pip check`, Ruff, strict mypy,
    every non-hardware test, installed CLI help, and exact-candidate hosted
    macOS CI pass with no required skip.
13. Static dependency, process, import, lock, command, and evidence audits prove
    no prohibited use in any active Cycle 3 path under the scoped-audit rule;
    preserved inert C# metadata is never restored, built, installed, imported,
    executed, or relied on as evidence.
14. Accepted Cycle 1/2 tests, evidence manifests, replay/CSV/CLI behavior,
    optional-web separation, rollback paths, and the macOS-only support claim
    remain intact.
15. Independent final measurements on the characterized macOS environment
    class meet every unchanged operator-approved resource/performance threshold
    and the approved SPI maximum is enforced.
16. Five ordered checkpoints contain distinct implementation, verification,
    acceptance, and manifest-verifier identities; exact candidate/tree
    evidence; immutable findings; schema-valid post-acceptance manifests; and
    correction history, with no future manifest or transferred pass.
17. The final scope audit finds no browser/API/frontend decoder work, hardware,
    firmware, serial/live capture, dynamic decoder discovery, stacking, `.lac`,
    packaging/publication, unsupported-platform claim, or other excluded work.
18. The B5 packet maps R1-R26 and conditions 1-17 to committed evidence and
    records a clean or qualified repository; verification and pre-manifest
    acceptance pass before manifest creation, the distinct manifest-verification
    pass precedes checkpointing, and the separate completion-closure audit
    passes over the committed manifest/checkpoint/completion proof.

Conditions 1-17 are product, proof, regression, and governance gates;
condition 18 proves their complete traceability and ordering. A command's exit
zero alone is insufficient where a condition requires independent artifacts,
operator approval, hosted CI, process inspection, or exact-candidate identity.

### Step 6 exit-gate assessment

The five proposed batches have settled prerequisites, interfaces, role
ownership, focused and accumulated proof, authority gates, and immutable
candidate/evidence ordering. R1-R26 assign every frozen Step 5 outcome to one
earliest batch and to C3-B5 final accumulated ownership; the 18-item final
checklist is objective and traceable. B1 owns semantics and value approval,
B2 owns enforcement, and B5 owns final measurement, so neither numeric limits
nor the SPI maximum form a circular implementation gate. No browser, hardware,
prohibited runtime/dependency, future manifest, or unapproved execution is
required. Step 6's content exit gate is met in this revision; committing the
approved revision will satisfy its durable-output gate.
