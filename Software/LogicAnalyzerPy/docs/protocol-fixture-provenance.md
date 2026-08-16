# C1-B1 protocol-fixture provenance

The three JSON fixtures in `testdata/protocol/` are immutable golden inputs for
the narrow Cycle 1 V2 identity and normal 8-channel edge-capture surface. They
are source-derived compatibility evidence, not captures from an attached board.
Their expected bytes must not be constructed by a production encoder or changed
to fit a later implementation.

## Source revision

- Repository commit: `b7a9f91962e952b5317b8239c794f3eed85955b4`
- Firmware struct source: `Firmware/LogicAnalyzer_V2/LogicAnalyzer_Structs.h`
  (`sha256:0180750a5b9327da346b730d58c044ddd9f24d8a9dc66c542aab5142e46c8b6b`)
- Firmware dispatch/framing source: `Firmware/LogicAnalyzer_V2/LogicAnalyzer.c`
  (`sha256:6039a08c07e364a2aaa519561ee80f02b7caa5707b5ce31512a15c59cf06e32e`)
- C# framing/layout source: `Software/LogicAnalyzer/SharedDriver/AnalyzerDriverBase.cs`
  (`sha256:cb6086ae139cf8848ac1f65a3b19a4da39e5d1e54575cd430f373f76e97cda0a`)
- C# request construction/identity/recovery source:
  `Software/LogicAnalyzer/SharedDriver/LogicAnalyzerDriver.cs`
  (`sha256:af021b2b49174bf8aae41584b6861245621917dff44f9c5e0d27bde5951aaa47`)
- C# session and trigger enum source:
  `Software/LogicAnalyzer/SharedDriver/CaptureSession.cs`
  (`sha256:771c95e057ba329a34807843961cc7803380e6d03ca899f8b198faf09122ebd1`)
- C# version acceptance source:
  `Software/LogicAnalyzer/SharedDriver/VersionValidator.cs`
  (`sha256:f8f0c7a7ce9e668f6cf5f9097b8ea41490a97c7ec8e14d7047550ffc7f4d3cac`)

## Facts derived from the named sources

- `OutputPacket.Serialize` puts `55 aa` before and `aa 55` after an unescaped
  command/payload. Within that payload it escapes `aa`, `55`, and `f0` as `f0`
  followed by the byte XOR `f0`. The firmware decodes the same convention.
- C# sends command `0` for identity. Firmware accepts it only at raw frame
  length five and responds with five newline-terminated fields in this order:
  `LOGIC_ANALYZER_<BOARD_NAME>_<FIRMWARE_VERSION>`, `FREQ:<n>`,
  `BLASTFREQ:<n>`, `BUFFER:<n>`, and `CHANNELS:<n>`.
- C# sends command `1` followed by `CaptureRequest`. The firmware casts the
  bytes after the command to `CAPTURE_REQUEST` and passes its fields to the
  simple capture routine when `triggerType` is zero.
- The normal Cycle 1 request is edge trigger type `0`, ordered channels
  `0..7`, count `8`, and capture mode `0`. `CaptureSession.TriggerInverted`
  is serialized at struct offset 2; the C# terminal UI calls that property
  `NegativeEdge`. Thus the fixtures use `0` for rising/positive and `1` for
  falling/negative.
- Natural alignment implied by the C fields and the C# sequential layout puts
  `triggerValue` at 4, the 24-byte channel list at 6, `channelCount` at 30,
  the three `uint32` values at 32/36/40, final byte fields at 44/45/46, and
  produces a 48-byte struct. Offsets 3 and 31 are alignment padding and 47 is
  tail padding. The fixture writes all three as `00` deliberately.

## Required physical confirmation and contradictions

No C#/board wire trace or compiled-layout probe is present. Therefore the
48-byte size, alignment offsets, zero values of the padding bytes, little-endian
representation, edge naming/polarity mapping, and actual firmware identity are
not observed-wire facts. C1-B3/C1-B4 must compare a captured known-good C# /
board exchange (or an equivalent C and .NET layout probe plus board trace) to
these fixture bytes before treating them as deployed-wire compatibility.

There are source risks that must not be hidden:

- Firmware trusts a cast of `messageBuffer[3]` as `CAPTURE_REQUEST` and does
  not validate the capture-request frame length before dereferencing it; C#
  instead relies on `Marshal.SizeOf` and native layout. The Python codec must
  emit an explicit 48-byte layout and reject every other request size.
- Firmware's `messageBuffer` is 128 bytes but `bufferPos` is `uint8_t` and the
  overflow condition is `bufferPos >= 256`, which cannot become true. This is
  not a safe parser bound and must not be copied.
- Firmware comments claim carriage-return-terminated responses, while actual
  response literals and C# `NewLine`/`ReadLine` use LF (`\n`). The fixtures use
  only requests; identity parsing should follow the actual LF-producing code.
- C# layers `StreamReader` and `BinaryReader` on the same stream. That is its
  compatibility reference, not a safe receive design; Cycle 1's one-buffer
  receive contract intentionally supersedes it.

## Fixture selection

The requests use a 1,000,000 Hz sample rate, `pre=170` (`aa 00 00 00`) and
`post=85` (`55 00 00 00`). Those ordinary non-burst counts make both reserved
payload bytes appear, so the golden frames prove `aa -> f0 5a` and
`55 -> f0 a5`. They are source-valid examples, not hardware-qualified limits
for an unknown attached board.
