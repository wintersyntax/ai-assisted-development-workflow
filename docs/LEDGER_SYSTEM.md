# Ledger system

The source workflow uses a Markdown **Do-Not-Forget Ledger** with stable `TASK-###` identities.

The purpose is simple: AI chat memory is not durable project memory.

## Stable identity

Task IDs are stable identities, not display order. Moving a task between Current, Waiting and Deferred sections does not change its ID. Retired IDs are not reused.

## Typical sections

The live ledger separates work by lifecycle, for example:

- Current / Next Work;
- Blocked / Waiting / Production Proof Pending;
- Deferred / Triggered Later.

## Typical task record

A task may include Status, Priority, Goal, Trigger/evidence, Done when, Progress/evidence, and Related docs.

The exact fields vary with the task. Stable identity and explicit completion conditions matter more than forcing every task into one rigid database schema.

## Registration checkpoint

Before substantive non-trivial repository work, the work must already have a ledger task or be registered as one.

Two useful modes are:

- **normal work** — register/reuse the task and continue implementation in the same development cycle;
- **capture only** — record future work but do not treat the capture as authority to implement it.

## No verbal TODO without durable capture

If new out-of-scope follow-up work is discovered, it is captured before it leaves active context. Registration preserves the idea; it does **not** expand the current implementation scope.

## Why Markdown

Markdown keeps the ledger human-readable, diffable, reviewable in the same PR as code, linkable to architecture/tests, and independent of proprietary AI memory.

See `examples/do-not-forget-ledger.example.md`.