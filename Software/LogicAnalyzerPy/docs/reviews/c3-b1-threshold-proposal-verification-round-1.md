# C3-B1 threshold-proposal verification — round 1

## Identity and immutable subject

- Verifier: `c3-b1-pre-execution-runner-verifier-1`
  (`/root/c3_b1_runner_verify`), verifier role distinct from proposal authorship
  and acceptance.
- Proposal candidate commit/tree: `e3a1d7c28a88a037e694d81c8c3406589fba040e` /
  `38eda7b580d505d3966f765bcffaf7297cb539f4`.
- Assignment commit: `8762de1`.
- Proposal SHA-256:
  `61d1273114d98bf6652b5401bf146e8d44fd6a51242c317a502719dfb036e080`.
- Rationale SHA-256:
  `112d5606b7912cce2e99bc16189d1783829eb79733b72d1d469d0beab1ca42b0`.
- The status remains exactly `proposal-not-approved`. No earlier verdict or
  numeric approval transfers.

## Finding

### C3B1-TPV001 — Successful-parent ceiling contradicts its stated formula

The bound raw maximum for `successful_parent_total_ns` is correctly
`105,815,301 ns`. The proposal states the derivation is
`ceil_to_100ms(raw_max * 8)`. Independent arithmetic gives:

1. `105,815,301 × 8 = 846,522,408 ns`;
2. ceiling to the next `100,000,000 ns` quantum is `900,000,000 ns`.

The proposed `value` and `accept` are instead `1,000,000,000 ns`, with reject
`1,000,000,001 ns`. The rationale likewise describes a rounded ceiling above
raw × 8 and does not declare a separate one-second scheduling floor. Therefore
the numeric boundary, machine-readable derivation, and prose rationale are not
mutually reproducible.

This is not a claim that 1 second is infeasible or unsafe. The value is below
the 5-second wall deadline. It is an exact-candidate formula defect: either the
value/boundaries must become 900,000,000 / 900,000,001, or a new candidate must
truthfully define and justify the intended one-second floor. Any correction is
a new immutable proposal candidate and receives fresh proposal verification;
this verifier repaired no proposal byte.

## Independent audit otherwise completed

The verifier independently recomputed all 29 unique categories from every raw
snapshot repetition, hostile cleanup row, request count, environment record,
and experiment cap. All raw maxima have no discrepancy, including input
372, request 1,286, records 34, encoded/decoded 4,222, text 426, binary 4,
depth 8, items 447, diagnostics 244, retained result 24,389, child RSS
20,856,832, parent retained growth 884,736, successful parent
105,815,301 ns, launch/reap/load/import/decode, and all cleanup maxima, match.

All 29 required IDs are present once. Types, units, positive integer values,
inclusive accept boundaries, exclusive value+1 reject boundaries, experiment-
cap relationships, evidence commits/digests, and macOS/Python environment bind
correctly. Every hard ceiling is equal to or stricter than its experiment cap.
Cross-limit feasibility is coherent for maximum samples/request framing,
retained output/RSS/address space, deadline/grace/cleanup, and SPI size 8.
No required category is missing and no second discrepancy was found.

The negative matrix independently rejects missing, extra and duplicate entries;
boolean, float, zero and negative values; changed raw maxima and formulas;
weakened experiment caps; inconsistent units/accept/reject boundaries;
deadline, cleanup and terminate-policy contradictions; SPI size 9; approved
status; and digest, commit and environment substitutions. To keep these tests
non-vacuous, the negative matrix first creates an in-memory formula-correct
900-ms baseline and validates it before applying each mutation. It never writes
that correction to the proposal.

## Commands and safety

All shell commands used RTK. The verifier suite reports 21 mutation/schema
passes and the one intentional exact-candidate failure at `formula boundary`.
Ruff passed. Exact proposal/rationale quiet diff, SHA recomputation,
`git diff --check`, and scope audit passed.

Static JSON/Markdown/source inspection only was used. No snapshot, decoder,
hostile probe, product host, hardware, network, install, external runtime, or
excluded action ran. The proposal is not approved and cannot advance to
accumulated validation or acceptance in this form.

## Verdict

`changes_required`
