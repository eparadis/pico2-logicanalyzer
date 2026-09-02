# C3-B5 verification round 2 — corrected final packet

## Identity and scope

- Verifier: `c3-b5-final-proof-verifier-2`; no pass transferred from round 1.
- Exact corrected candidate/tree: `f8f78c89655011e3ee3e74559ff9886c93eac690` /
  `e6b5d5f0afaf3023ec398cb9c42c6d42d5a1790b`.
- Governing contract/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Accepted B4 checkpoint: `9a8fc46ba4bc73cd007d678b85b6510bba0eeb87`.
- This verifier changed only its fresh verification test and this review. It
  performed no hosted dispatch and changed no product, fixture, method,
  threshold, prior evidence, manifest, checkpoint, workflow, package,
  completion, closure, seal, or Cycle 4 material.

## C3B5-V001 and independent measurement

The corrected collector has exactly two top-level collection loops: one call
to `observe` for each of the three UART/SPI/I2C timelines, followed by five
retained repetitions over those same three timelines. Its explicit invariant
is 18 launches and 15 retained rows. The committed raw packet says
`warmup=3`, `retained=15`, `total=18` and contains exactly one row for every
decoder/repetition pair. No retry, exception suppression, sorting by result,
or outlier deletion exists. C3B5-V001 is closed.

I independently invoked the corrected collector into ignored
`.tmp/c3-b5-verifier-r2-measurements.json`; it performed 18 launches and
retained 15 rows. Independent maxima versus unchanged round-4 ceilings were:

| Metric | Independent max | Ceiling |
| --- | ---: | ---: |
| worker peak RSS bytes | 30,105,600 | 134,217,728 |
| parent retained growth bytes | 77,824 | 33,554,432 |
| successful parent total ns | 149,191,671 | 1,300,000,000 |
| launch ns | 2,399,326 | 50,000,000 |
| reap ns | 18,914 | 50,000,000 |
| child load ns | 8,667,237 | 100,000,000 |
| child import ns | 90,275,798 | 100,000,000 |
| child decode ns | 2,343,182 | 100,000,000 |
| timeout cleanup total ns | 0 | 5,500,000,000 |
| terminate-to-reap ns | 0 | 300,000,000 |
| kill-to-reap ns | 0 | 50,000,000 |

The independent environment was Darwin/x86_64 CPython 3.12.13. The packet
binds proposal `b680aa59fba4a18da2aeaacc8cbd7ad3a68784e0`, proposal SHA-256
`98e48bb1882104d893a1d4d85659845ff20054f9b52f0b09fdf73efad2547e3c`,
method SHA-256
`f228f02892fc2ead00713606dc795850e14651baafc42a0974d1dbd48da86341`,
and semantic-fixture SHA-256
`34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094`.
All 18 hard limits retain exact accept/reject boundaries; SPI accepts 8 and
rejects 9. Hostile timeout, cancellation, graceful termination, forced kill,
pipe closure, reap, post-failure recovery, and separate cleanup-observation
tests passed, including the real SIGTERM-ignoring child.

## Accumulated focused evidence

- B5 final packet plus B1 fixture/binding, B2 private host, B3 UART/SPI/I2C and
  cross-source, and B4 public/API/CLI implementation modules: 593 passed.
- Direct pre-execution runner and hostile cleanup selection: 182 passed.
- Fresh final B1/B2/B3/B4 verifier selection: 336 passed plus one transparent
  historical candidate-bound digest failure. That assertion expects the old
  SHA-256 `1511083a...` for
  `test_cycle3_preexecution_runner.py`; accepted B4 commit `c765087` changed one
  test invocation to use the normal recovery profile and explicitly binds the
  current SHA-256 `9fa8f300...`. The underlying 178 runner tests and cleanup
  gates pass directly. This is the already documented candidate-bound
  deselection class, not a product or evidence defect and transfers no pass.
- Current environment `pip check`: no broken requirements; Ruff: pass;
  production mypy: no issues in 31 source files.
- All four B1-B4 evidence manifests validated independently against the Cycle
  3 schema and retained exact SHA-256 values `3710e7fd...`, `2af5bfc2...`,
  `4d17a6f0...`, and `699443c5...` in ordered complete checkpoints with four
  distinct role identities each.

The accepted B1-B4 packets plus fresh final measurements map R1-R26 and
stopping conditions 1-17. R26/condition 15 are established by the independent
final observation; the remaining requirements and conditions retain their
accepted earliest-owner evidence and were proportionally rerun here. No B5
manifest or checkpoint, completion proof, closure verdict/record, or seal
exists. Condition 18 therefore remains correctly pending for the directed
post-verification chain.

The B1 rights-holder or qualified-counsel limitation remains controlling
before conveyance. GPL-3.0-only engineering disposition and inherited notices
are unchanged. No external/reference decoder runtime, browser decoder,
hardware, firmware, serial/live capture, dynamic discovery, stacking, `.lac`,
package build, publication, conveyance, unsupported-platform claim, or Cycle 4
action occurred.

## Candidate files and verdict

- implementation test SHA-256:
  `8914ca125aa2ed132f7eabdff8d148045132bce447222d75ac9860b0175689f6`;
- raw final measurements SHA-256:
  `980308fc3a144d1af70959793fb9e0b4476658b9856d56eb101876fc9fedb54e`;
- implementation review SHA-256:
  `60c059d4c3878e5aa5726acc31f72170266064cb0d2243bc5ed339048dd186ea`.

Verdict: `pass` for exact corrected candidate
`f8f78c89655011e3ee3e74559ff9886c93eac690` / tree
`e6b5d5f0afaf3023ec398cb9c42c6d42d5a1790b`. No finding remains and no
`APPROVAL_NEEDED` capability exists. This pass authorizes only the next ordered
root-owned accumulated gate and exact-candidate hosted CI; it does not
authorize later terminal artifacts out of order or any excluded action.
