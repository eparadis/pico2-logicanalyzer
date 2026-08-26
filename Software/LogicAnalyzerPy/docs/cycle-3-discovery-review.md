# Cycle 3 bounded discovery review

## Status, purpose, and authority boundary

- Status: Steps 1 and 2 are committed, Step 3 bounded technical discovery is
  committed, and the operator has resolved all ten Step 4 decisions in this
  revision. Step 4's exit gate is met, subject to committing this record.
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
