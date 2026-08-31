# C3-B2 private-host implementation — round 1

Identity: `c3-b2-private-host-implementor-replacement-1`.

This implementation handoff is not a verification, acceptance, manifest, or
checkpoint verdict. It is bound to contract
`ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` / tree
`d9fb09345ab85580cd8c877745262d1b481e366f`, corrected B1 checkpoint
`d4f984d26ca45dcd0f70da51ad739da427e23be4`, semantic fixture `3af6b9f`,
runner `380d5dd`, and B1 joint manifest `885be61` / SHA-256
`3710e7fde7523096b70607b3a7da217b1e71fdb46492b83b72861e3eaa48cfae`.

The private `_decode` surface provides immutable request/result/failure models,
closed UART/SPI/I2C identity and hash checks, closed pre-spawn validation,
frozen API-v3 primitives, a fresh fixed `-I -B` FD-only worker, bounded v1
length-framed IPC, safe failure conversion, deadline and terminate/kill/reap
cleanup. It introduces no public decode API or CLI.

All 29 limits bind to round-4 proposal `b680aa5` and approval `afd4585`,
including parent retained growth `33554432`, successful parent total
`1300000000` ns, launch `50000000` ns, and SPI word size `8`; limits are
inclusive and focused tests exercise first rejection.

Focused results:

- private-host pytest: 110 passed;
- Ruff: passed;
- strict mypy: success, 9 source files;
- `git diff --check`: passed.

Coverage includes all semantic timelines through fresh workers, canonical
values, hostile malformed/oversize/truncated/extra IPC, cyclic/non-finite
values, mapping/options and SPI boundary negatives, identity/import-root
checks, lifecycle failure, worker reaping, and recovery after preflight
failure. Post-check inspection found no private worker or focused pytest
process remaining.

No prohibited runtime, external decoder, hardware, network, browser, public
surface, fixture/threshold/contract, B3+, or Cycle 4 change was made.
Independent B2 verification, accumulation, acceptance, and evidence remain.
