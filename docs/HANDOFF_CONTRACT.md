# Handoff contract

The working workflow uses a versioned **Execution Contract + multi-slice Blueprint** rather than a flat task packet.

The public example is intentionally representative and sanitised. The private executable schema contains more mechanical checks, but the authority split is the same.

## Contract

The Contract defines what the task is allowed to mean and change.

Typical fields include:

- `task_id` — stable ledger identity;
- `base_main_sha` — exact `main` commit the plan was solved against;
- `objective`;
- `non_goals`;
- `relevant_paths`;
- `invariants`;
- `acceptance`;
- `verification`;
- `stop_conditions`;
- `risks`.

## Blueprint

The Blueprint defines how the solved task is executed.

It contains ordered slices with dependencies. A slice can declare:

- mutation paths and targets;
- Architect-authored regression tests;
- literal exact edits;
- facts the executor may rely on;
- preserve rules;
- focused verification commands;
- stop conditions;
- optional semantic bindings/oracles.

## Exact edits

When possible, the Architect writes the implementation as literal replacements copied from the pinned base. The controlled Host verifies the old span and applies the replacement deterministically. No implementation model call is required for that slice.

## Architect-authored regression tests

The regression test is part of the handoff rather than being delegated to the same mutation worker whose implementation it judges.

A regression declaration can specify the test path, symbol placement, exact test code, subject symbols, expected RED/GREEN state, and expected failure signal.

## Why the base SHA matters

A plan can become stale when another change lands. Binding the Contract to an exact `BASE_MAIN_SHA` makes drift explicit.

## Mechanical validation vs semantic authority

The executable validator can prove shape, identities, path bindings, edit uniqueness, test placement and command constraints. It cannot prove that the design itself is semantically correct; that remains the Architect/human responsibility.

See `examples/architect-handoff.example.json`.