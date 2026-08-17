# C1-B4 normal capture and hardware smoke

The only approved Cycle 1 physical input is the installed integrated
LogicAnalyzerV2 protection board: VRef 3.3 V, a 3.3 V source, and common ground
at the labelled `GND`. The 1 kHz connection labelled `1` is logical D0 and Pico
2 GPIO2. Do not connect a 5 V source to this setup or a bare Pico input.

After confirming the physical configuration, use explicit values; no port,
rate, count, or output path is selected implicitly:

```console
pico-la capture --port <PORT> --sample-rate 100000 --trigger-channel 0 \
  --edge rising --pre-samples 2048 --post-samples 4096 \
  --csv <CAPTURE.csv> --replay <CAPTURE.npz>
```

`100000`, rising D0, 2048 pre, and 4096 post are operator examples, not CLI
defaults. `capture` requests exactly D0-D7 in normal 8-bit mode. Existing CSV
or replay paths are refused unless `--force` is supplied. Both outputs are
written, fsynced, replay-validated, and installed as one rollback-capable
transaction; a failure leaves no newly installed final pair.

For the physical gate, run the explicit smoke command and retain its sanitized
evidence file:

```console
pico-la hardware-smoke --port <PORT> --signal-hz 1000 --sample-rate 100000 \
  --trigger-channel 0 --edge rising --pre-samples 2048 --post-samples 4096 \
  --evidence <EVIDENCE.json>
```

It requires at least two transitions of the requested polarity and calculates
frequency using the first and last same-polarity transitions. The evidence
records their count and span. It passes when the relative error is at most the
sum of a named 2% allowance for an uncalibrated nominal source and conservative
endpoint quantization `2/span_samples` (one sample at each endpoint). An
operator-provided calibrated-source allowance may replace the 2% value before
candidate freeze. A span of two samples or fewer is insufficient for a frequency
validation and fails rather than treating a 100% quantization allowance as
evidence. This command does not send cancellation, flash firmware, or
change persistent board state. A timeout is exit code 4;
connection/protocol, replay validation, and output failures use 3, 5, and 6.

Validate a saved replay without hardware:

```console
pico-la replay-validate <CAPTURE.npz> --json
```
