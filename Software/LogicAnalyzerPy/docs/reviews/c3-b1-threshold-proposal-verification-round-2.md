# C3-B1 threshold-proposal verification — round 2

## Identity and immutable subject

- Verifier: `c3-b1-pre-execution-runner-verifier-1`
  (`/root/c3_b1_runner_verify`), reused only in its verifier role.
- Corrected proposal commit/tree: `395646fa1172382928581d7266723f5b044cf8f2` /
  `6857f9a67ff70220e6d6b2a11f9ca450005c8321`.
- Round-2 assignment commit: `e4eeb43c061fa4c2748f9243dc542b2192a92f5e`.
- Proposal SHA-256:
  `94882b710f2d569c0ea0535366a0c1c3df3514aa20a18e4cd35f652177458ec2`.
- Rationale SHA-256:
  `18a6b58a2b05f7dd7aa302a6e1bb4d074621440648a2e735a1d16d9708b209b0`.
- Round-1 pass transfer: none. Round 1 remains immutable
  `changes_required` evidence for `C3B1-TPV001`.

## Independent correction and scope audit

The corrected arithmetic independently reproduces:

- `105,815,301 × 8 = 846,522,408 ns`;
- ceiling to the next `100,000,000 ns` quantum = `900,000,000 ns`;
- inclusive accept = `900,000,000 ns`;
- first rejected value = `900,000,001 ns`.

The JSON rationale truthfully states an 8.51-times ratio and the Markdown
rationale names the exact 900-ms result. After reversing only this value,
accept, reject and rationale plus the permitted round/provenance metadata, the
round-2 proposal is structurally identical to round 1. No other numeric
proposal meaning changed.

Provenance is complete and ordered: accepted fixture, corrected runner, raw
candidate, raw verification/accumulation/acceptance, correction assignment,
superseded assignment/proposal, failed verification assignment, and failed
verification commit are all exact. All six evidence digests independently
recompute. Status remains exactly `proposal-not-approved`; neither document
claims approval or product enforcement.

## Complete 29-category audit

All 29 IDs are unique and closed. Independent recomputation over every raw
snapshot repetition and hostile cleanup row reproduced every raw maximum,
including samples 372, request bytes 1,286, records 34, encoded/decoded 4,222,
text 426, binary 4, depth 8, items 447, diagnostics 244, retained result
24,389, child RSS 20,856,832, parent retained growth 884,736, successful parent
105,815,301 ns, launch 6,464,224 ns, reap 164,802 ns, load/import/decode
2,524,751 / 9,337,765 / 1,715,444 ns, and cleanup maxima 5,283,148,328 /
254,508,892 / 2,054,776 ns.

Every formula, positive integer type, unit, kind, raw maximum, inclusive accept,
exclusive value+1 reject, experiment-cap identity, and hard-cap relationship
passes. Every hard ceiling is equal to or stricter than the accepted experiment
cap. Cross-limit feasibility passes for maximum samples and request framing,
retained output/RSS/address space, successful deadline, deadline/grace/cleanup,
termination/reap, and SPI maximum word size 8. No required category is missing
and no finding remains open.

## Negative mutation matrix

The fresh round-2 matrix rejects all required mutations: missing, extra and
duplicate entries; booleans, floats, zero and negative values; altered maxima
or formulas; weakened experiment boundaries; inconsistent units, accepts and
rejects; successful-time/deadline, timeout-cleanup and terminate/grace
contradictions; SPI maximum 9; approved status; and evidence digest, commit and
environment substitutions. The unmodified corrected candidate validates before
each mutation family, so these rejection proofs are non-vacuous.

## Commands, scope, and safety

All shell commands used RTK.

- Fresh round-2 verifier: 22 passed in 0.36 seconds.
- Ruff: passed.
- Exact corrected-candidate path quiet diff, candidate/tree/digest inspection,
  `git diff --check`, and scope audit: passed.

Only this verifier test and this review record were created. No candidate,
evidence, raw, runner, fixture, product, progress, or governing byte was
modified. Static JSON/Markdown/Git inspection only was used. No snapshot,
decoder, hostile probe, product host, hardware, network, install, external
runtime, or excluded action ran. The values remain proposals pending the
separately ordered accumulated validation, acceptance, and explicit operator
decision.

## Verdict

`pass`
