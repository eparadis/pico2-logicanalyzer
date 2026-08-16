# C1-B2 hostile replay fixture matrix

Replay files are generated in verifier tests inside pytest temporary directories
once the B2 replay API is available. They are deliberately not committed as
opaque ZIP files: each test must name the attack/property it exercises and
construct only the minimum archive needed for that case.

Required cases are: missing/extra/duplicate/path-bearing members; encrypted or
unsupported compression; archive, metadata, sample-member, and sample-count
bounds; object/structured/string/non-`uint8` dtype; non-rank-one samples or
metadata; invalid UTF-8/JSON; unknown/missing/schema-major metadata; non-inert
metadata; and count/trigger/channel inconsistencies. The normal control archive
uses exactly `samples.npy` and `metadata.npy`, with `allow_pickle=False`.
