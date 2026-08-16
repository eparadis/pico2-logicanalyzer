# Compatibility boundaries

Cycle 1 supports one V2 analyzer and only normal eight-channel edge captures.
The existing C# implementation and firmware are retained unchanged as rollback
and comparison paths. V2 identity version acceptance and deployed board layout
remain physical-confirmation work in C1-B3.

The Cycle 1 CSV is intentionally not the existing C# channel-only export. It is
self-timed UTF-8 LF RFC-4180-compatible data with exact header:

```text
sample_index,time_seconds,trigger,D0,D1,D2,D3,D4,D5,D6,D7
```

Rows use zero-based sample index, `.12g` trigger-relative seconds, trigger `1`
only at `trigger_index`, and bit columns in request order. A future importer
must treat its time/trigger columns as authoritative and must not invent timing
for unrelated CSV. A legacy CSV mode requires a separate named contract and
fixtures. `.lac`, 16/24 channels, GUI, TCP, decoder hosting, and device
management are deferred.
