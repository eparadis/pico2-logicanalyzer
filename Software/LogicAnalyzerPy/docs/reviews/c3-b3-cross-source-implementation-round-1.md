# C3-B3 R16 cross-source implementation — round 1

Status: candidate evidence only; not accepted. This document makes no B3 accumulated,
acceptance, manifest, or checkpoint claim.

Candidate identity and scope: `python-rewrite` at base
`30b020a3f8cc14ce65b42c8764dcaff9900dcd45` (tree
`1d1ee0749512bf9b1713914fc586c25a86059391`). The only candidate implementation
path is `tests/implementation/test_c3_b3_cross_source_equivalence.py`; this review
is the only documentation path. No product, fixture, conformance, contract, or
evidence artifact was changed.

## Source construction and proof boundary

The test takes wave transitions only from the accepted B1 semantic corpus and creates
each source separately:

- in-memory `CaptureResult`;
- a hand-built schema-1 NPZ (`samples.npy` plus canonical `metadata.npy`), imported
  through `import_replay_bytes`;
- a production schema-2 replay constructed from a separately built capture with
  `replay_bytes`, imported through `import_replay_bytes`;
- production CSV bytes from a separately built capture, imported with explicit ordered
  channel IDs `(0..7)`, explicit sample rate, trigger channel `0`, and `rising` edge.

The test asserts source archive schema identities exactly `1` and `2`, distinct source
byte digests, and capture equality (rate, ordered channel IDs, trigger index, packed
samples, labels, and mapping) before decoding. It then constructs each `DecodeRequest`
from that source and calls only the frozen private `decode_private` host. Canonical JSON
bytes of all four results must be identical. `serial.Serial` is patched to fail, so no
serial, hardware, or live-capture route can open during the proof.

Schema 1 is contractually the legacy eight-channel D0--D7 container. The selected UART
TX semantic witness uses D9, so its D9 waveform is independently remapped to D4 for all
four equivalent representations; the decoder-channel mapping remains `tx`. This is a
source-format limitation, not a corpus modification. All other selected mappings remain
their accepted physical IDs.

## Coverage accounting

The accepted corpus has 63 timelines. R16 is source-boundary equivalence rather than a
second decoder conformance sweep, so the authoritative smallest complete matrix is six
representatives:

| Protocol | Witnesses | Source-conversion distinction |
| --- | --- | --- |
| UART | RX default; TX default remapped D9→D4 | optional RX/TX direction and schema-1 limit |
| SPI | MOSI; MISO; MOSI with CS | optional data direction and optional CS |
| I2C | shifted start/address/data/stop | complete required two-wire mapping |

Thus the source proof runs 6 timelines × 4 inputs = 24 private decode invocations. The
remaining 57 timelines are deliberately left to the accepted UART/SPI/I2C conformance
suites; rerunning all 63 through every source would multiply process work without adding
a new source-format mapping class.

Hostile controls show that a changed packed sample (a selected SPI MOSI edge), decoder
mapping, ordered capture channels, sample rate, trigger index, and CSV source
labels/mapping cannot silently be called equivalent. The packed-sample, mapping, rate,
and trigger controls produce distinct canonical decode bytes; channel order and
source-only metadata changes are detected in capture identity before decode.

## Frozen identities

- semantic corpus SHA-256:
  `34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094`
- option matrix SHA-256:
  `5d84b9d9855e9e2e75d45d5cd9560fbcfd1ac6ff88abfcf1c1326d3427ffc209`
- B1 manifest reference:
  `71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9`
- B2 evidence SHA-256:
  `2af5bfc21a5d888132fb4e468f543403e8948632ad9ab2dd11b8da854dd4a602`

## Commands and results

Run from `Software/LogicAnalyzerPy`:

```text
rtk .venv/bin/python -m pytest tests/implementation/test_c3_b3_cross_source_equivalence.py -q
8 passed in 4.65s

rtk .venv/bin/python -m pytest tests/implementation/test_c3_b3_uart_conformance.py tests/implementation/test_c3_b3_spi_conformance.py tests/implementation/test_c3_b3_i2c_conformance.py tests/implementation/test_c3_b3_cross_source_equivalence.py -q
144 passed in 26.10s

rtk .venv/bin/python -m ruff check tests/implementation/test_c3_b3_cross_source_equivalence.py
All checks passed!

rtk git diff --check
clean (no output)
```

Correction history: the initial local candidate used an invalid synthetic device identity;
the test exposed the production capture-model validation and it was corrected to a valid
inert V6 identity. Root review then identified the missing hostile packed-sample control;
this round adds an independent D3 mutation at accepted SPI sample 30 and proves a changed
canonical result while metadata remains coherent. No product behavior or fixtures were
changed.

Findings: none. No product integration gap was observed, so no adapter path is proposed.
