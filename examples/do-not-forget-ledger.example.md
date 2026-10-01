# Example Do-Not-Forget Ledger

> Synthetic portfolio example. Task IDs are stable identities, not display order.

## Current / Next Work

### TASK-001 — Prove exact-edit handoff validation

**Status:** IN PROGRESS

**Priority:** High

**Goal:** Validate a SHA-bound Contract + Blueprint before controlled execution.

**Done when:** The synthetic handoff passes repository validation and a malformed base SHA fails closed.

**Related docs:** `docs/HANDOFF_CONTRACT.md`

## Blocked / Waiting / Evidence Pending

### TASK-002 — Record a tagged release

**Status:** WAITING FOR TRIGGER

**Priority:** Medium

**Trigger:** The repository is ready for a tagged release.

**Goal:** Produce one validated release bundle through the checked-in release workflow.

**Done when:** A `v*` tag produces a successful validation run and artifact.

**Related docs:** `docs/CI_CD.md`

## Deferred / Triggered Later

### TASK-003 — Automate Architect-to-Host transport

**Status:** DEFERRED

**Priority:** Medium

**Trigger:** Manual handoff remains stable across enough real tasks and further automation is explicitly approved.

**Goal:** Reduce copy/paste coordination without weakening exact-ref bootstrap, durable task identity, bounded scope, human merge authority or fail-closed review.

**Done when:** A reviewed design defines transport/session identity and deterministic tests cover repair and replan routing.

**Related docs:** `docs/ARCHITECTURE.md`