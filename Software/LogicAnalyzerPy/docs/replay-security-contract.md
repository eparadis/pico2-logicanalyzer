# Provisional replay format and security contract

Schema major version 1 is provisional. A replay artifact is a ZIP/NPZ with
exactly two unique members: `samples.npy` and `metadata.npy`. `samples.npy` is a
rank-one exact-`uint8` array. `metadata.npy` is a rank-one exact-`uint8` array
whose bytes are canonical UTF-8 JSON. Pickling is disabled on every load.

Before NumPy materialization, inspect the ZIP central directory. Reject
encrypted entries, duplicate/unexpected/path-bearing names, unsupported
compression, metadata above 64 KiB, samples above 17 MiB, total archive above
32 MiB, or more than 16,777,216 samples. Reject object, structured, string, and
nested sample dtypes.

Metadata is inert: it may not name, configure, import, or execute decoder code.
It has a flat bounded schema and no unknown top-level keys in Cycle 1. Required
keys are schema version/provisional marker, sample rate, requested/actual/pre/
post counts, trigger index/channel/edge, channel IDs/labels/mapping, and
sanitized device identity/capabilities. Counts must agree with samples. C1-B4
implements writer/reader validation and tests every bound.
