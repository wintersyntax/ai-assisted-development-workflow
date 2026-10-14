# Checkpoints and focused repair

## Principle

A failed checkpoint is a signal to **reduce uncertainty**, not permission to broaden mutation scope.

## Process-owned checkpoint state

Long-lived executor-triggered tests and canonical checks are wrapped by a repository helper that stores local interlock state outside the tracked worktree.

The state is conceptually RUNNING, GREEN or FAILED.

A FAILED result remains blocking until it is explicitly acknowledged through the allowed recovery path. GREEN only removes the negative interlock; it does not grant merge or repository authority.

## Why this exists

Without a process-owned interlock, an executor could continue mutating while a long test is still running or after a UI lost track of that process.

Checkpoint state makes later mutation fail closed even when the presentation layer is imperfect.

## Bounded repair

For an executor-driven slice, the Host may allow **one** same-slice repair after an ordinary focused-test RED when the required conditions hold.

The repair:

- receives bounded failure evidence;
- may change only the existing authorized Mutation Pack;
- does not widen the Contract;
- reruns diff hygiene and focused verification.

A second RED is terminal.

## Fail-closed cases

Examples that do not become an ordinary repair turn include:

- timeout;
- abnormal process exit;
- branch or identity drift;
- unexpected workspace mutation during verification;
- out-of-scope diff;
- stale or malformed checkpoint state;
- structural verification failure;
- Host-applied exact-edit verification failure.

That last case returns to the Architect because the solved handoff is wrong; it is not an invitation for Cline to reinterpret an Architect-written exact edit.

## Completion

A repair is complete only when the original focused check passes, the original Contract remains satisfied, and no new scope has been introduced.