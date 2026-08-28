# C3-B1 replacement manifest verification — round 4

## Verdict and immutable subject

`changes_required`

- Independent identity: `c3-b1-manifest-verifier-replacement-1`.
- Assignment commit: `eafd0cc`.
- Exact accepted candidate commit/tree:
  `7246dcbe55a60ef7ee9196f4bf265c7c75141d55` /
  `51e895a1e2c95580d04bc8a31ed8d58a85613e1a`.
- Proposed replacement manifest:
  `Software/LogicAnalyzerPy/testdata/evidence/c3-b1.json`.
- Manifest SHA-256 at intake and after inspection:
  `d1a9c7fee237bc4bcf7773c9cdebdaa2035c827ef5b3499ea2b4b5d61852dcad`.
- The proposed manifest remains unchanged and uncommitted. This verifier made
  no repair and supplies no manifest acceptance, checkpoint, B2, product,
  distribution, hardware, network, downstream, or Cycle 4 authority.

Verification stopped once the two mandatory defects below made a passing
verdict impossible. Checks not listed as completed here are not claimed.

## Findings

### C3B1-MV003 — six live round-4 threshold artifacts retain stale round-3 provenance

Status: **open**.

Six artifact entries bind round-4 paths, revisions, and SHA-256 values but
describe those artifacts as round 3:

1. `threshold-proposal-round-4.json` — `approved round-3 threshold proposal`;
2. `c3-b1-threshold-proposal-rationale-round-4.md` —
   `round-3 threshold rationale`;
3. `test_c3_b1_threshold_proposal_round4.py` —
   `round-3 threshold verification test`;
4. `c3-b1-threshold-proposal-verification-round-4.md` —
   `round-3 threshold verification pass`;
5. `c3-b1-threshold-proposal-accumulated-validation-round-4.md` —
   `round-3 threshold accumulated pass`; and
6. `c3-b1-threshold-approval-round-4.md` —
   `explicit operator approval of all round-3 values`.

These descriptions contradict the corrected round-4 proposal and explicit
round-4 operator authority that the manifest is intended to bind. Replace
only these six stale provenance strings with accurate round-4 descriptions,
then submit the resulting exact manifest for fresh independent verification.

### C3B1-MV004 — final accumulated artifact uses an abbreviated revision

Status: **open**.

The artifact for
`c3-b1-final-accumulated-validation-round-4.md` records revision `64a0468`.
The live immutable accumulation commit is
`64a0468ef0e04d21e758730b18bd7d87ee599c3b`. The frozen Cycle 3 schema permits
an arbitrary nonempty revision string, but the checkpoint contract requires
every live artifact revision/path/SHA-256 triple to identify an exact Git
object. Replace the abbreviation with the full 40-character commit identity,
then reverify the triple through Git.

## Completed static checks

- `git status --short --branch` — the manifest was the sole tracked modified
  path; the three preserved untracked B2 paths were identified by pathname
  only and excluded.
- `git log --oneline --decorate -40` — confirmed candidate `7246dcb`, verifier
  `e1b8753`, accumulation `64a0468`, acceptance `88cb142`, and assignment
  `eafd0cc` occur in that order.
- `shasum -a 256 Software/LogicAnalyzerPy/testdata/evidence/c3-b1.json` —
  produced the assigned digest
  `d1a9c7fee237bc4bcf7773c9cdebdaa2035c827ef5b3499ea2b4b5d61852dcad`.
- `git show --stat --oneline` over `7246dcb`, `e1b8753`, `64a0468`,
  `88cb142`, and `eafd0cc` — confirmed the expected two-path candidate,
  two-path verifier, one-record accumulation, one-record acceptance, and
  one-record assignment scopes.
- Static inspection of the frozen Cycle 3 schema and validator confirmed the
  required root fields, distinct role surfaces, exact-candidate command
  binding, repository-relative references, R1–R26 and stopping-condition
  structures, artifact revision field, and sensitive-value rejection.
- Static inspection of the round-4 binder, final verifier, accumulated record,
  and final acceptance confirmed the intended corrected fixture, runner, raw,
  exact round-4 threshold/operator chain, 21 command classes, role separation,
  and required downstream ordering at the source-record level. This does not
  override the manifest defects above.
- `sed -n '560,690p' Software/LogicAnalyzerPy/testdata/evidence/c3-b1.json` —
  confirmed all six stale provenance strings and the abbreviated accumulation
  revision directly in the unchanged proposed manifest.

No schema-validator execution, full reference/digest sweep, artifact Git-object
sweep, decoder, runner, raw reproduction, product or B2 test, browser, hardware,
network, package, downstream, or Cycle 4 command was run after the decisive
findings. No preserved untracked B2 content was opened, imported, or modified.

## Disposition

The proposed manifest is not eligible for the joint manifest/verifier commit
or replacement B1 checkpoint. Root must correct `C3B1-MV003` and
`C3B1-MV004` atomically without changing the accepted candidate or evidence
chain, then assign a fresh distinct manifest verifier. The current manifest
remains byte-identical at the intake SHA-256 above.
