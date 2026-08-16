# ADR 0001: Cycle 1 raw 8-bit capture model

## Decision

Store samples as a one-dimensional C-contiguous NumPy `uint8` array. One value
is one raw returned word. Cycle 1 requests `[0,1,2,3,4,5,6,7]` in ascending
order only; duplicates and subsets are rejected. Raw bit `i` is request-list
position `i`, thus D`i`; channel IDs, display labels, and physical/header map
remain separate metadata.

`requested_count = pre_trigger_samples + post_trigger_samples`, actual length
equals it, and `trigger_index = pre_trigger_samples`. Time for index `i` is
`(i - trigger_index) / sample_rate_hz`. Thus with `pre=2`, index 1 is
`-1/sample_rate_hz`; index 2 is time zero and is the only trigger-flag row.
Trigger channels are integers D0–D7 and edges are exactly `rising`/`falling`.

## Consequences

Capture configuration validates positive negotiated sample rate, protocol bounds,
and at least one post-trigger sample. Per-channel arrays are derived, not stored
as Python-integer lists. Models are implemented in C1-B2; this ADR is the
contract that tests and artifact writers must follow.
