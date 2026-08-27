@/Users/ed/.codex/RTK.md

Always read `/Users/ed/.codex/SUBAGENT_POLICY.md` before launching subagents.

## Approval request policy

- The root orchestrator is the only approval broker. Subagents must route any
  missing external authority to root and must not request it themselves.
- Before requesting approval, split work into stable command classes. Put only
  one privileged command class in each approval request; do not batch unrelated
  or differently prefixed privileged commands into one shell command.
- Request the narrowest reusable `prefix_rule` that covers the recurring class
  (for example an exact test, bootstrap, browser, or performance command), not
  a one-off full command and not a broad interpreter or shell prefix.
- After a prefix is approved, reuse it without supplying a new `prefix_rule` or
  presenting another approval request. Run unrelated sandbox-safe validation
  separately without escalation.
- If several steps need different privileged prefixes, request each stable
  class at most once, then invoke those saved classes separately. Never trigger
  package-by-package, test-process-by-test-process, or commit-by-commit prompts
  when an existing narrowly scoped approval covers the action.
- Prefer repository or `/private/tmp` working files and already-approved `rtk`
  command shapes. An approval grants command capability only; it does not widen
  product scope or waive evidence, ordering, or safety requirements.
