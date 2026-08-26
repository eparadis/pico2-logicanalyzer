# Cycle 3 contract review — capture, annotations, library, and CLI

- Gate and round: `contract`; `contract-round-1`
- Reviewer: `/root/c3_contract_review_workflows` (capture, annotation, CLI, and workflows)
- Reviewed commit: `8bd6ba06a42ea190f50c7b15789638938c8716d2`
- Reviewed tree: `19fc91d2cfaa526f2bee7ee2835423e5ccbd50ee`
- UTC timestamp: `2026-08-26T06:05:26Z`
- Verdict: `changes_required`

## Set-completeness declaration

I inspected every path in the exact six-file Step 8 contract-review set at the
commit and tree above, with no worktree file substituted: the roadmap,
discovery review, orchestration contract, batch procedure, Cycle 3 review
README, and architectural-domain charters.

## Findings and dispositions

### C3-CR1-R2-001 — High — the decode CSV grammar cannot reconstruct accepted metadata

- Evidence: `pico-la decode --csv PATH` does not carry the ordered physical
  channel IDs, samplerate, trigger channel, and trigger edge required by the
  accepted explicit-metadata CSV parser for non-legacy CSV.
- Violated invariant: in-memory, replay, and explicit-metadata CSV inputs must
  converge on one exact capture identity before decoder mapping.
- Requested resolution: add exact inert CSV metadata arguments (or an equally
  explicit reviewed inert carrier), freeze their precedence and validation,
  and keep decoder-channel mapping a separate namespace.
- Disposition: open.

### C3-CR1-R2-002 — High — public result and canonical JSON are underspecified

- Evidence: `DecodeResult`, canonical JSON, tagged values, rational time,
  bytes, declarations, record shapes, and failure classes lack a separately
  versioned normative schema with exact fields and types.
- Violated invariant: independent library and installed-CLI proof cannot
  produce byte-exact expected results from prose alone.
- Requested resolution: freeze a versioned normative schema and failure
  taxonomy, require independently authored expected library objects and CLI
  golden bytes before implementation, and update R9/R17/R18 and their proof
  gates to consume those immutable identities.
- Disposition: open.

## Prior-round reconciliation

No earlier contract-review round or finding exists for this gate/domain.
