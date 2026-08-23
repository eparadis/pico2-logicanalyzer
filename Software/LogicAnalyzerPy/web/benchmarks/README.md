# C2-B5 rendering benchmark

`fixtures.json` freezes the empty, constant, sparse, dense, maximum-width, and
bus fixture corpus. Run `generate_fixtures.py` only when deliberately replacing
the corpus; byte digests are part of the benchmark identity.

The Playwright performance test uses the checked-in production assets and real
bounded B4 import, polling, metadata, channels, waveform, bus, and export API.
It fixes a 1280×900 viewport at device-pixel ratio 1, records the Chromium and
Playwright versions, production asset digest, host/OS, fixture payload and
sample counts, visible transition count, DOM count, and Canvas command count.
After three warm-up interactions it measures two initial ready/paint iterations
for each of eight required roles (16 total), plus 30 repeated keyboard pan/zoom
interaction sequences with `performance.now()`, waiting for the next animation
frame and the bounded waveform response each time. For both the representative
and worst bus fixtures it also measures two real table renders in transition
mode and two in distinct-strobe mode. The durable report retains every raw
timing sample and derives median and p95 with deterministic nearest-rank
selection: sort ascending and select index `max(0, ceil(p * n) - 1)`, without
rounding. This permits independent recomputation of every reported statistic.
Browser heap data is recorded only when Chromium exposes a finite
`performance.memory.usedJSHeapSize`; otherwise memory is explicitly
unavailable. CI observations are informational until a separately reviewed
relative method is demonstrated. No threshold is encoded in this method.
