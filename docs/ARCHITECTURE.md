# Architecture

The workflow separates **durable repository authority**, **read-only reasoning**, **controlled execution**, **verification**, and **integration**.

## Durable repository authority

Git, version-controlled prompts/docs, the task ledger, handoff contracts, tests and accepted CI evidence are the durable state.

Chat history is useful orientation, but it is not allowed to silently override exact-ref repository evidence.

## Read-only planning and review

TypingMind is the human-facing workspace.

The Architect resolves exact current `main`, reads repository-owned authority, solves the task, writes regression tests, and produces a versioned Contract + Blueprint.

The Reviewer separately inspects the verified result and returns PASS, REPAIR, REPLAN or BLOCKED.

Neither role owns repository mutation.

## Replaceable model/provider layer

OpenRouter is a provider boundary, not project memory and not completion authority.

Different roles can use different models according to reasoning quality, latency, availability and cost.

## Controlled Host

The Host is the local execution and verification control plane.

Before mutation, it can simulate the Blueprint in a disposable worktree copy. During execution it owns handoff validation, write/session guards, test placement, exact-edit application, fallback executor launch, diff hygiene, focused/impacted tests, checkpoint interlocks and final verification.

## Exact edits first

The current workflow prefers the model that read the code to write the implementation.

If the Architect supplied literal exact edits, the Host applies them deterministically. A fully Host-applied slice requires **0 executor provider turns**.

## Thin Cline fallback

ClineCore is retained only for a slice the Architect could not safely express as exact edits.

It receives a bounded Mutation Pack rather than the whole project history, and strict sessions deliberately exclude broad shell/web/search fallback authority.

## Verification authority

Model output is not considered complete because the model says it is done.

Focused tests, diff hygiene, optional source/semantic oracles, workspace identity checks, final verification and CI provide machine-checkable evidence.

## Integration authority

Local verification comes first. Canonical remote evidence is then bound to the exact PR head. Merge is explicit human authority. Exact new `main` must pass its own acceptance checks before the integration is treated as accepted.

## Portability

Two kinds of portability are deliberately separate:

- **state portability** — Git + repository-owned docs/prompts + ledger;
- **model portability** — replaceable provider/model selection.

Changing AI tools should not erase project memory or silently change authority.