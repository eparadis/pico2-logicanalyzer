# Narrow V2 device protocol (Cycle 1)

This is a narrow implementation note, not a claim of full firmware support.
It distinguishes source-derived behavior from hardware-observed behavior. No
known-good C#/board trace was available during C1-B1; a C1-B3 trace is required
before physical acceptance.

## Evidence and framing

Source-derived from `Firmware/LogicAnalyzer_V2/LogicAnalyzer.c` and
`SharedDriver/AnalyzerDriverBase.cs`: each request starts `55 aa`, ends `aa 55`,
and has an unescaped command byte followed by payload. Escape each payload byte
equal to `aa`, `55`, or `f0` as `f0` followed by `byte ^ f0`. The delimiters are
not escaped. Identity is command `00`, hence its complete request is
`55 aa 00 aa 55`.

The firmware's source comments call responses newline-terminated strings;
actual host parsing must use one byte-oriented receive buffer for text and
binary phases. Do not combine text and binary buffered readers.

## Identity exchange

Source-derived response: exactly five ASCII LF-terminated fields, in order:

```text
LOGIC_ANALYZER_<BOARD_NAME>_V<major>_<minor>\n
FREQ:<positive decimal>\n
BLASTFREQ:<positive decimal>\n
BUFFER:<positive decimal>\n
CHANNELS:<positive decimal>\n
```

Each field, including LF, is capped at 128 bytes. The existing C# validator
accepts V6_0 or newer; C1-B3 must record the attached board's actual identity
and decide compatibility rather than infer it from source alone.

## Cycle 1 capture request

Command `01` contains one explicit 48-byte little-endian payload. This is the
settled Python contract, derived from the RP2040/C field order and the C#
sequential structure but intentionally not native-packed:

| Offset | Size | Field | Cycle 1 value |
|---:|---:|---|---|
| 0 | 1 | trigger type | `0` (edge) |
| 1 | 1 | trigger | `0..7` |
| 2 | 1 | inverted | `0` rising, `1` falling |
| 3 | 1 | explicit pad | `00` |
| 4 | 2 | trigger value | `0000` |
| 6 | 24 | channels | `00 01 02 03 04 05 06 07` then sixteen `00` |
| 30 | 1 | channel count | `08` |
| 31 | 1 | explicit pad | `00` |
| 32 | 4 | frequency | unsigned LE Hz |
| 36 | 4 | pre samples | unsigned LE |
| 40 | 4 | post samples | unsigned LE, at least one |
| 44 | 1 | loop count | `00` |
| 45 | 1 | measure timestamps | `00` |
| 46 | 1 | capture mode | `00` (8-bit) |
| 47 | 1 | explicit tail pad | `00` |

The pre/post and frequency bounds come from negotiated capabilities in the
later driver; no request may be sent before validation. `requested_count` is
exactly `pre + post`. Golden rising/falling vectors and independent expected
bytes belong to verifier-owned `testdata/protocol/`.

## Capture response and recovery

Source-derived response starts `CAPTURE_STARTED\n`, then a 4-byte little-endian
sample count, that many 8-bit sample words, and a required trailing timestamp
count byte of zero for non-burst Cycle 1. Coalesced status and binary bytes are
valid. Count must equal the validated request and be bounded before allocation.

The source and current C# client characterize a single `ff` byte while a capture
is in flight as cancellation input. The C# client waits about two seconds then
closes/reopens; firmware polls cancellation in a one-second loop. Cycle 1's
later driver must use finite timeouts, send exactly one `ff` only for in-flight
normal-capture timeout/Ctrl-C, drain with bounded timing, close/reopen, then
re-identify. This is internal recovery, not a public abort API.

## Serial settings and unresolved confirmation

Source-derived from C#: 115200 baud, 8N1, no flow control, DTR and RTS asserted.
Open/configure, stabilize, bounded drain, and reopen timing require C1-B3
physical confirmation. USB CDC targets may ignore line settings. Malformed,
overlong, missing, or extra identity fields and malformed capture status fail
the protocol; they never fall through into binary parsing.
