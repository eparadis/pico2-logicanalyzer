# C2-B2 independent verification — round 2

- Lane / stable identity: verifier / `cycle2-verifier-replacement-1`
- Implementor identity: `cycle2-implementor-replacement-3`
- Candidate commit: `b931a61c911905550a273ec73e329299411e366a`
- Candidate tree: `b6c6d6da85bdaf79794f3cb2a5dd1bd5961d1203`
- Date: 2026-08-23 America/Los_Angeles
- Prior-verdict transfer: none
- Verdict: `changes_required`

## Candidate, authority, and scope

The assigned commit exists and resolves to the assigned tree. Verification ran
from a clean product/test tree whose only descendant difference was the
orchestrator-owned verifier-identity append in
`docs/cycle-2-orchestration-progress.md`; no candidate product or test path
differed. The current macOS-only goal, orchestration and complete C2-B2 batch
contract; settled model, wire, replay, CSV and security contracts; B2 progress
and identity records; accepted B1 and Cycle 1 records/tests/artifacts; immutable
round-one review; and checked-in V2 firmware source were reviewed.

The firmware authority selects the Pico 2 buffer of 393216 bytes and 24
channels. Its native request structure independently confirms the 48-byte
payload, channel slots at 6--29, count at 30, padding at 31, little-endian
frequency/pre/post at 32/36/40, zero loop/measure at 44/45, and mode at 46.
The candidate remains confined to authorized Python model, protocol, device,
CLI, replay/CSV, focused tests, and durable review/progress paths. It makes no
firmware, C#, API/viewer, bus-analysis, decoder, hardware, packaging, public
serving, or Cycle 3 change.

## Complete independent result

Literal externally constructed 8-, 16-, and 24-bit requests and responses
confirm offsets, falling/rising mode, ordered and reordered slots, canonical
unused-slot and alignment zeros, frame escaping, counts, and little-endian
sample words. Exact-type, Boolean, range, uniqueness, trigger membership,
negotiated channel/frequency/buffer, byte-width multiplication, count, dtype,
rank, contiguity, labels/mappings, and 24-bit upper-byte boundaries are covered.
One-byte and coalesced receive paths, malformed status, truncation, extra data,
timeout/disconnect closure, and literal nonzero timestamp-count plus four
would-be payload bytes at every width reject; contamination invalidates the
receive owner and prevents reuse.

Schema-1 compatibility and hostile cases pass. Schema-2 all-mode ordered-subset
round trips are deterministic and retain the inert two-member NPZ design.
Archive/member, duplicate/path/encryption/compression, NPY version/header,
rank/dtype/shape/count/byte-order, canonical UTF-8 JSON, key/type/string/numeric,
device, word-mode, count, buffer, upper-byte and cross-field checks pass before
or during the appropriate bounded materialization stage; pickle loading is
disabled.

Generalized CSV exercises all word widths, reordered/noncontiguous subsets,
packed-position extraction, labels and RFC-4180 escaping, exact decimal
canonical timing including non-terminating periods, trigger/index/binary/time
syntax failures, explicit metadata validation, and deterministic re-export.
The exact legacy D0--D7 bytes remain compatible. A literal external legacy CSV
with `-0.01,0,0.01` uniquely infers 100 Hz, while zero/one-row, inconsistent,
noncanonical and no-unique-candidate cases reject. The new CLI command exposes
explicit input/output paths, channel order, optional legacy rate inference,
trigger metadata, overwrite control, deterministic artifacts, and established
exit classes. Findings below prevent acceptance of its complete boundary.

## Prior finding dispositions

- `C2B2-V001`: resolved. The verifier-owned artifact expectation now requires
  schema-2 writes while schema-1 reads remain covered.
- `C2B2-V002`: resolved. The verifier-owned boundary fixture now accepts the
  valid seven-channel subset.
- `C2B2-V003`: resolved. Exact-decimal legacy integer-rate inference is present
  and independently reproduces canonical cells before accepting a unique rate.
- `C2B2-V004`: resolved. The explicit `csv-import` CLI surface and deterministic
  output/exit behavior are present for valid and covered-invalid inputs.

## New findings

### C2B2-V005 — zero CSV sample rate bypasses metadata validation

Owner: implementor. A literal valid legacy CSV supplied through
`import_csv_bytes(..., sample_rate_hz=0, ...)` reaches `_canonical_time` before
`CaptureConfig` validates the explicit metadata and raises uncaught
`ZeroDivisionError`. The production `csv-import --sample-rate 0` path therefore
escapes `main` with the same exception instead of returning the deterministic
usage or validation exit and bounded diagnostic. Validate the complete explicit
metadata object, including exact integer type and `1..0xffffffff` rate, before
any timing arithmetic, and add direct-library plus CLI boundary tests for zero,
negative, Boolean/non-integer (library), and above-uint32 values.

### C2B2-V006 — CLI materializes an unbounded CSV path before its limit

Owner: implementor. `_csv_import` uses `Path.read_bytes()` and only afterward
passes the resulting allocation to the importer's 16 MiB limit. An arbitrarily
large or sparse input path is therefore fully read into memory before the
bounded CLI rejects it. Apply the frozen input-size bound from file metadata
and/or bounded streaming before full materialization, preserve deterministic
validation-versus-I/O exit behavior, and independently test exact-limit,
one-byte-over-limit, sparse/large, and read-failure cases without leaving output
or temporary artifacts.

No verifier-owned fixture or product file was changed in this round.

## Commands and results

- Focused wider/protocol/replay/artifact matrix: 149 passed; one expected
  duplicate-ZIP construction warning.
- Full `.venv` nonhardware suite: 256 passed; 94 existing warnings.
- Ruff: pass. Mypy: pass over 19 source files. Module help: pass and includes
  `csv-import`.
- Frontend shell: lint pass; typecheck pass; Vitest 1 passed; production build
  26 modules; production-asset drift check pass.
- Playwright production shell: initial sandbox loopback start failed; the
  required authorized loopback rerun passed 1 test in 1.6 seconds.
- Local frontend executable reported Node 26.5.0 rather than the locked
  22.14.0. No frontend/product path changed in B2, and accepted B1 plus its
  exact hosted macOS evidence retain the pinned clean-Node gate; this local run
  is regression evidence, not a replacement claim for the accepted pinned
  bootstrap.
- Independent zero-rate library and CLI probes: fail as described in
  `C2B2-V005` with uncaught `ZeroDivisionError`.

## Verdict and handoff

Verdict is `changes_required`. Open findings are `C2B2-V005` and
`C2B2-V006`, both owned by `cycle2-implementor-replacement-3`. No acceptance,
C2-B2 evidence manifest, or checkpoint is authorized. After the two bounded
CSV/CLI corrections and focused tests are committed, create a new exact
candidate and repeat independent C2-B2 verification and the complete
accumulated gate from scratch; no pass in this record transfers.
