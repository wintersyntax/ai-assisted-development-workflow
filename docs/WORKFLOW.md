# Workflow

This is a sanitised description of the current staged workflow.

## 1. Bootstrap exact repository authority

The read-only Architect verifies repository identity, resolves current `main` to one exact SHA, loads repository-owned instructions from that SHA, and checks that the running context bridge matches the expected runtime/tool identity.

A stale or inconsistent runtime blocks instead of improvising.

## 2. Register durable task identity

Non-trivial work must have a stable task identity before substantive implementation.

Out-of-scope follow-up work is captured durably before it leaves active context. Capture preserves the idea; it does not widen the current task.

## 3. Architect solves globally

The Architect decides target behavior, semantics, invariants, non-goals, failure behavior, mutation scope, acceptance criteria, documentation impact and verification strategy.

The output is a SHA-bound Contract + multi-slice Blueprint.

## 4. Validate mechanically

An executable validator checks the handoff shape, identities, path bindings, exact-edit uniqueness, regression-test placement, slice ordering and command constraints.

Mechanical validity does not prove semantic correctness.

## 5. Check preparation before mutation

The controlled Host can simulate the Blueprint in a disposable copy.

For Host-applied slices it can place Architect-authored tests, prove expected RED/GREEN behavior, apply exact edits, run diff hygiene, execute focused/impacted tests and evaluate declared oracles.

The operator working tree is not touched by this simulation.

## 6. Execute each slice

### Preferred path: Host exact edits

If the Architect supplied exact edits, the Host applies them with **0 executor provider turns**.

A verification failure on a Host-applied exact-edit slice is treated as a handoff/design defect and returns to the Architect rather than asking Cline to improvise.

### Fallback path: thin Cline

If a slice cannot be expressed safely as exact edits, a bounded ClineCore session receives only the current slice, declared mutation targets, solved facts, preserve rules and Host-owned verification requirements.

Strict executor sessions do not receive broad shell/web/search authority.

## 7. Micro verification and bounded repair

The Host runs fixed diff hygiene and focused tests.

One ordinary focused-test RED may qualify for one bounded same-slice repair on the already-authorized Mutation Pack.

A second RED, timeout, identity drift, scope escape, unexpected verification mutation or structural failure stops fail-closed.

## 8. Final Verification

After all slices verify, documentation is reconciled and the canonical local pre-PR gate runs.

Commit, push, PR and merge remain outside automatic Host authority.

## 9. Independent review

A separate read-only Reviewer checks Architect intent against the actual diff, test quality, edge cases, authority/data-flow changes, documentation reconciliation and Host evidence.

Verdicts are PASS, REPAIR, REPLAN or BLOCKED.

## 10. Exact-PR-head CI

The source project records Documentation, Dependency and Application checkpoints on the exact PR head.

Local development remains the iteration loop; Actions are not used as trial-and-error development.

## 11. Human merge approval

Merge remains explicit human authority.

## 12. Exact-main acceptance

After merge, exact new `main` must prove Documentation, Main-write provenance, Dependency and Application checkpoints.

## 13. Reconcile durable memory

Ledger state, follow-ups, changelog, architecture/topic docs and schema/policy docs are reconciled so the next session can reconstruct state from the repository.