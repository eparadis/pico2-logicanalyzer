# Cycle 3 offline decoding

Cycle 3 exposes the accepted private UART, SPI, and I2C compatibility host
through one synchronous public operation:

```python
from pico_logic_analyzer.decode import DecodeResult, decode_capture

result: DecodeResult = decode_capture(
    capture,
    "spi",
    {"clk": 0, "mosi": 1},
    {"cpol": 0, "cpha": 0, "wordsize": 8},
)
payload = result.json_bytes()
```

`capture` must already be a validated, non-empty `CaptureResult`. Physical
channel IDs are resolved through its ordered `channel_ids`; they are not bit
positions. Mapping and option keys are closed for the selected decoder and are
validated before a worker starts. The optional `limits` mapping accepts only
known positive integer ceilings at or below the installed values. It cannot
select an in-process mode or disable snapshot digests, closed imports,
validation, cancellation, cleanup, or the decoder allowlist.

Every call uses one fresh, single-request Python subprocess and exactly one of
the package-owned snapshots identified by import commit
`407b5ef039aa0474c400c0721749baa126e53270`. The supported security claim is
bounded process containment for the trusted, hash-pinned snapshots on macOS;
it is not a general Python or operating-system sandbox.

## Installed CLI

The complete offline grammar is:

```text
pico-la decode (--replay PATH | (--csv PATH --channels D0,D1,...
               [--sample-rate HZ] --trigger-channel PHYSICAL_CHANNEL
               --edge {rising,falling})) --decoder {uart,spi,i2c}
               --channel DECODER_CHANNEL=PHYSICAL_CHANNEL
               [--channel ...] [--option KEY=VALUE] [--option ...]
```

Replay metadata is authoritative, and all four CSV metadata flags are forbidden
with replay. CSV requires ordered physical IDs, a trigger channel, and an edge.
It also requires a sample rate except when the header and supplied identity are
exactly legacy D0-D7; in that one case the accepted time-column inference is
used. CSV metadata validates before decoder mappings or options and never comes
from them.

Success writes exactly one UTF-8, compact, sorted-key
`pico-logic-analyzer.decode-result/v1` JSON object and one LF to stdout.
Configuration or mapping errors use exit 2, inert replay/CSV errors use exit 5,
and decoder snapshot/import/IPC/exception/resource/deadline/cancellation errors
use exit 7. Failures write no machine output to stdout and emit only a bounded,
path-free diagnostic on stderr.

The decode path has no live capture, serial open, stdin input, dynamic decoder
path, plugin directory, stacking, output/export file, browser endpoint, or web
dependency. It is supported and accepted only on macOS with Python 3.12.

## Provenance and licensing

The installed distribution declares `GPL-3.0-only`; the eight marked snapshot
and helper files retain their GPL-2.0-or-later headers. See
[`../ATTRIBUTION.md`](../ATTRIBUTION.md) and the included license texts. The
compatibility shim has no in-file notice, so the accepted rights-holder/counsel
limitation remains: no conveyance or publication is authorized by Cycle 3 or
by this engineering record.
