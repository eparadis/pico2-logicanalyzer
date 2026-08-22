# Cycle 2 architectural reviewer charters

All three reviewers inspect the complete common-commit document set. Domain
ownership determines primary attention; cross-domain handoff defects are still
findings.

## Reviewer 1: device protocol and hardware boundary

Owns firmware framing and ABI, ordered-channel packing, word modes and bounds,
transport, timeout/cancellation/recovery, physical mapping, electrical safety,
and the D0/D8/D16/D23 proof.

Required invariants include source-backed literal bytes, bounds before
allocation/read, exact dtype and upper-byte handling, explicit port selection,
fixed firmware, deterministic cleanup, and real hardware evidence that cannot be
replaced by fake tests.

## Reviewer 2: capture data and browser workflow boundary

Owns generalized capture semantics, replay schema 1/2, self-timed CSV, bus
analysis, Python/API handoffs, React state and workflows, Canvas rendering,
interaction behavior, and performance evidence.

Required invariants include physical-ID versus packed-position separation,
deterministic inert formats, one Python analysis authority, bounded visible
render work, testable UI behavior, and useful 8-bit-SBC workflows without
decoder or editing scope expansion.

## Reviewer 3: delivery, web security, verification, and orchestration

Owns Python/Node dependency reproducibility, production assets, loopback/token/
Origin boundaries, request/concurrency limits, macOS/Linux claims, CI, agent
ownership, authority gates, review/checkpoint mechanics, evidence, performance-
threshold approval, rollback, and the verifiable stop.

Required invariants include one bounded objective, one owner for every proof,
three distinct batch identities, common-commit final review, no runtime CDN or
Node requirement, no .NET/`.lac`/firmware mutation, exact platform claims, and
no skipped stopping-condition evidence.

## Cross-domain seam rule

A reviewer records a finding whenever its domain cannot safely consume another
domain's promised output. Assign the technical repair to the owning domain, then
verify the handoff. A substantive repair triggers all-three review on a new
common commit.
