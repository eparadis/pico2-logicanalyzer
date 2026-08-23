# C2-B3 independent verification — round 1

- Lane / stable identity: verifier / `cycle2-verifier-replacement-3`
- Implementation identity: `cycle2-implementor-replacement-5`
- Product candidate commit: `90adb3adb38a938ce470fa854e6fc7b98e1501c9`
- Product candidate tree: `5a09d57e4caa266a43f164edaffc94fc9a3236d7`
- Implementation evidence layer: `cdea294`
- Verification test commit: `61cca63`
- Verified at: `2026-08-23T17:42:18Z`
- Verdict: `pass`

## Authority, inputs, and scope

Verification independently reviewed the current macOS-only Cycle 2 goal,
orchestration and complete B3 batch contract; the approved discovery and
progress records; accepted B1 and corrected/reaccepted B2 evidence; accepted
Cycle 1 recovery evidence; the sanitized B3 implementation record; and all
seven raw runtime artifacts under the assigned private runtime directory. The
product candidate commit and tree match the assignment.

The verifier did not invoke or trust the implementation helper for expected
results. A verifier-owned test reads each ZIP member through standard-library
ZIP handling and NumPy's NPY reader with pickling disabled, checks canonical
metadata independently, derives masks and timing directly from raw words, and
constructs CSV bytes without the production replay/CSV readers or writers.
No serial port, USB device, firmware, wiring, browser, .NET, persistent state,
or other hardware operation was used or changed.

## Independent physical artifact results

| Width | dtype/count | Driven mask | Rises/span | Measured Hz | Allowed fractional tolerance | Projection states | CSV reconstruction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | `uint8` / 6144 | `0x01` | 42 / 4077 | 1005.641403 | 0.020490557 | low and high | byte-identical |
| 16 | `uint16` / 6144 | `0x0101` | 42 / 4058 | 1010.349926 | 0.020492854 | low and high | byte-identical |
| 24 | `uint32` / 6144 | `0x810101` | 42 / 4078 | 1005.394801 | 0.020490436 | low and high | byte-identical |

Every replay is an inert two-member schema-2 archive with exact ordered
D0--D7, D0--D15, or D0--D23 physical IDs and labels; ordered GPIO mappings;
100000 samples/s; 2048 pre-trigger and 4096 post-trigger samples; rising D0;
the expected firmware mode; native rank-one contiguous dtype; and exact count.
All 24-bit words have bits 24--31 zero. Unconnected bits were observed only and
were not acceptance criteria.

The raw artifact digests independently match the sanitized implementation
record: recovery `40745b7e...482ad1`; 8-bit CSV/replay
`fc4c4759...37a3` / `b1401639...ad6`; 16-bit `ee1e2bf4...b9f` /
`614765cd...8a1`; and 24-bit `c6255f31...efe5` / `af3b61f1...1bd`.

## Recovery audit

The recovery JSON is sanitized to `<PORT_SUPPLIED>` and records fixed-low D1,
0.25-second in-flight cancellation, literal one-byte cancel value `ff`, the
fixed V2 Pico 2 identity, re-identification, no persistent device change, and a
second rising-D0 capture of 6144 samples without a power cycle. Its 41 rising
transitions over 4000 samples independently calculate to exactly 1000 Hz,
within the recorded 0.0205 source-plus-quantization tolerance.

The accepted verifier recovery regression independently proves the lifecycle
semantics represented by that result: one cancel byte only after capture is in
flight, one shared bounded drain of at most 4096 bytes, close, reopen,
re-identify, and second capture, including cleanup failures. The focused B3
run repeated those ten lifecycle cases against the corrected candidate.

## Findings and dispositions

1. `C2B3-I001`: resolved. The exact corrected candidate was reverified and
   reaccepted before this complete physical sequence; all D0--D23 metadata is
   present in the raw 24-channel artifact.
2. `C2B3-V001`: no new verification finding. Artifact integrity, settings,
   widths, masks, activity, timing, upper byte, CSV determinism, recovery, and
   sanitization all pass; disposition closed by this verdict.

No finding is open.

## Commands and concise results

- SHA-256 audit of seven raw artifacts: all expected digests matched.
- Focused B3 artifact plus accepted recovery lifecycle tests: 14 passed.
- Full non-hardware Python suite: 280 passed, 1 sandbox-only loopback skip, 94 warnings.
- Ruff: pass. Mypy: pass over 19 source files. CLI help: pass.
- Candidate/worktree path audit and `git diff --check`: pass.

## Verdict and authority

Verdict is `pass`. The exact corrected product candidate satisfies the C2-B3
physical byte-boundary and Cycle 1 recovery regression contract with no open
finding. This review permits the same candidate and complete B3 evidence to
proceed to accumulated validation and independent acceptance. It does not
authorize another hardware run, wiring change, manifest creation, checkpoint
closure, or later-batch implementation.
