# Cycle 3 bounded discovery review

## Status, purpose, and authority boundary

- Status: Step 1 baseline reconciliation complete; bounded technical discovery
  and operator decisions remain pending under Steps 2 through 6 of
  `CYCLE3_PREPARATION.md`.
- Inspection date: 2026-08-25 (America/Los_Angeles).
- Authority: `CYCLE3_PREPARATION.md`, committed at
  `c163a8353550e0b80dd7f001b21147659ad307ff`.

This record begins the bounded Cycle 3 discovery required by
`CYCLE3_PREPARATION.md`. At this stage it records only the exact inherited
Cycle 2 evidence, the post-completion repository delta, focused validation of
that delta, and the proposed Cycle 3 starting input. Later preparation steps
must expand this same file with roadmap reconciliation, decoder discovery,
operator decisions, the settled contract surface, and proposed proof ownership.

This document does not authorize Cycle 3 implementation, dependency changes,
decoder execution, hardware or firmware action, persistent device changes, or
creation of Cycle 3 checkpoint evidence. A change accepted below as starting
input does not gain retroactive Cycle 2 acceptance. The accepted Cycle 2
candidate and immutable evidence remain unchanged.

## Step 1: starting-baseline reconciliation

### Accepted Cycle 2 identities

The authoritative completion record is
`Software/LogicAnalyzerPy/docs/cycle-2-completion.md`, added by completion-proof
commit `f558b58612f5c85f58791a850b3319d5dfaba14e`. It records:

- final accepted product candidate:
  `2d5484a73d881496cdf5a35c799dfb01eedad229`;
- final accepted product tree:
  `8c76bce79922263468cb6ceaa4f1990703a84bfc`;
- final B6 checkpoint commit:
  `7fe1f5c06b87c47285378b2144c4a3c4377a7238`;
- final B6 checkpoint tree:
  `68aa9ecbad96d324467e37b7bb3a2de37e53153b`;
- completion-proof commit:
  `f558b58612f5c85f58791a850b3319d5dfaba14e`;
- completion-proof tree:
  `45dc85e090aa7f84db4feadd022ece0ae66df4f1`;
- audited platform claim: macOS only; and
- final acceptance verdict: pass, with no open or deferred Cycle 2 finding.

The six active Cycle 2 manifests named by that completion proof are:

| Checkpoint | Manifest | Manifest commit | Recorded SHA-256 |
| --- | --- | --- | --- |
| C2-B1 | `Software/LogicAnalyzerPy/testdata/evidence/c2-b1.json` | `4bb2561` | `7c45f8b7f90965fbf9c67845f3b8a0113fe84261e8085665068e6f1980bf4de0` |
| C2-B2 | `Software/LogicAnalyzerPy/testdata/evidence/c2-b2.json` | `5f5eebb` | `d930bce4ae20576ea030e35cf0e993a3caf89e95f5eb5195638471c1790c2be4` |
| C2-B3 | `Software/LogicAnalyzerPy/testdata/evidence/c2-b3.json` | `4635bf4` | `9db03e119c6cacb40e87ef61d8f7ef1e24692ea45527f5e331e2103ecc59ff1b` |
| C2-B4 | `Software/LogicAnalyzerPy/testdata/evidence/c2-b4.json` | `ef74970` | `4876b781f4569ae1599b6c5df4d824fbd54223c736c87c96746e6bb821806fd0` |
| C2-B5 | `Software/LogicAnalyzerPy/testdata/evidence/c2-b5.json` | `f561d31` | `8fcdf9714e2ad94af845d9676227bf6750159075bb49416d9c78c16d5b3c14e9` |
| C2-B6 | `Software/LogicAnalyzerPy/testdata/evidence/c2-b6.json` | `354c299` | `ed8036ef48654efd98a5c3a852fb1f1dba847a34e12bf1c5dec253a2b9a83ffb` |

The C2-B6 manifest binds the same accepted product candidate and tree. The
implementation, verification, acceptance, manifest, checkpoint, and completion
commits after `2d5484a` are immutable evidence or governance descendants; they
do not alter the accepted product tree.

### Repository state inspected for Step 1

The repository was clean before this discovery record was created:

- HEAD: `c163a8353550e0b80dd7f001b21147659ad307ff`;
- tree: `45556769aab973c7671f58d57bae1878a46af9f2`;
- branch: `python-rewrite`;
- upstream relation: one commit ahead of `origin/python-rewrite`, with no
  behind commit;
- tracked, staged, unstaged, and untracked changes: none; and
- unrelated user changes: none observed.

Creation of this file is the only Step 1 worktree change. It is preparation
documentation, is not a product change, and remains outside the proposed input
baseline until it is reviewed and committed by the root orchestrator.

### Descendants of the accepted product candidate

Between the accepted product candidate and the completion proof, the following
commits add only the final B6 evidence and governance records:

| Commit | Tree | Path-level change | Classification |
| --- | --- | --- | --- |
| `a349cc5a855c4c73c74c2ca79d5058ec6a3f8c77` | `e7b6d05784346da0198d0f9997ea43a10ad5a914` | add `docs/reviews/c2-b6-implementation-round-4.md` | Accepted immutable Cycle 2 evidence; preserve. |
| `436e18735831e4db3501ff3bb1cc08c2761a0e1d` | `acc8d1a29fbaa9b1388cc0f531b9494712485330` | add `docs/reviews/c2-b6-verification-round-4.md` | Accepted immutable Cycle 2 evidence; preserve. |
| `605400422b4affbd84793686a8431769de9913ef` | `b9f14e106f1050e459678ecacd9bf768ce1af90e` | add `docs/reviews/c2-b6-acceptance-round-2.md` | Accepted immutable Cycle 2 evidence; preserve. |
| `354c299903ec73633e5762a2b65adaae1d44e8d7` | `6f67f22c5dcf8696b9df6883e13c3ae0e2b9cebc` | add `testdata/evidence/c2-b6.json` | Accepted immutable Cycle 2 manifest; preserve. |
| `7fe1f5c06b87c47285378b2144c4a3c4377a7238` | `68aa9ecbad96d324467e37b7bb3a2de37e53153b` | update `docs/cycle-2-orchestration-progress.md` | Accepted B6 checkpoint record; preserve. |
| `f558b58612f5c85f58791a850b3319d5dfaba14e` | `45dc85e090aa7f84db4feadd022ece0ae66df4f1` | add `docs/cycle-2-completion.md` | Accepted Cycle 2 completion proof; preserve. |

There are two commits after the Cycle 2 completion proof:

| Commit | Tree | Path-level change | Classification and disposition |
| --- | --- | --- | --- |
| `5b409a6384624bfb6b51bc323c97a54244477dde` | `74249d3dcb3eb414268d34f467164d90fd3b90b4` | modify `Software/LogicAnalyzerPy/README.md`; add executable `Software/LogicAnalyzerPy/start_web.sh` | Post-completion product/documentation delta. Include as Cycle 3 starting input after the focused checks below. This is not Cycle 2 acceptance. Runtime dependency installation, device discovery, live launch, SSH behavior, and hardware behavior were not exercised, so Step 1 makes no new acceptance claim for them. |
| `c163a8353550e0b80dd7f001b21147659ad307ff` | `45556769aab973c7671f58d57bae1878a46af9f2` | add `CYCLE3_PREPARATION.md` | Cycle 3 governance input. Include and preserve; it changes no product, accepted evidence, dependency, fixture, or workflow. |

No post-completion path is unrelated or excluded. No repository change remains
unclassified.

### Focused validation and results

The launcher can create a virtual environment, install locked dependencies,
inspect serial devices, and start a server. Those effects were deliberately not
invoked during preparation. Existing local dependencies were used only for
non-hardware regression tests.

The following safe checks were run against inspection HEAD `c163a83`:

| Command | Result |
| --- | --- |
| `git diff --check f558b58..5b409a6` | Exit 0; no whitespace errors in the post-completion launcher delta. |
| `bash -n Software/LogicAnalyzerPy/start_web.sh` | Exit 0; launcher shell syntax is valid. |
| `.venv/bin/python -m pytest -q tests/unit/test_cli.py tests/implementation/test_web_boundary.py tests/implementation/test_web_api.py` | Exit 0; 21 passed, 1 restricted-sandbox loopback test skipped, 14 existing `aiohttp` `NotAppKeyWarning` warnings. The skip is not presented as new live-loopback proof. |
| `.venv/bin/python scripts/validate_cycle2_evidence.py docs/evidence-manifest/cycle2-schema.json testdata/evidence/c2-b1.json testdata/evidence/c2-b2.json testdata/evidence/c2-b3.json testdata/evidence/c2-b4.json testdata/evidence/c2-b5.json testdata/evidence/c2-b6.json` | Exit 0; all six accepted Cycle 2 manifests validate. |

No dependency was installed or updated; no decoder code, hardware, firmware,
serial operation, browser, server, network, or SSH command was executed. These
checks establish that the narrow launcher/documentation delta is suitable for
preservation as starting input. They do not independently accept every runtime
claim added to the README or launcher.

### Proposed Cycle 3 input baseline and exit-gate result

The unambiguous proposed Cycle 3 technical and governance input baseline is:

- commit: `c163a8353550e0b80dd7f001b21147659ad307ff`;
- tree: `45556769aab973c7671f58d57bae1878a46af9f2`;
- branch: `python-rewrite`;
- inherited accepted product identity: Cycle 2 candidate `2d5484a73d881496cdf5a35c799dfb01eedad229`, tree `8c76bce79922263468cb6ceaa4f1990703a84bfc`;
- included post-completion product/documentation delta: `5b409a6384624bfb6b51bc323c97a54244477dde`, subject only to the focused Step 1 validation claim above; and
- included governance input: `CYCLE3_PREPARATION.md` at `c163a83`.

Later commits that contain only preparation records, including the commit that
will add this file, may descend from this baseline without silently changing the
technical input identity. The final Cycle 3 launch preflight must record its own
then-current clean HEAD and tree and must separately account for any later
product change.

Step 1's classification exit gate is met: one exact proposed baseline exists,
all accepted-candidate descendants, both post-completion commits, and the sole
Step 1 worktree change have explicit dispositions, and no unrelated or excluded
change is hidden. Step 1 is not durably complete until this section is committed
as required by `CYCLE3_PREPARATION.md`.
