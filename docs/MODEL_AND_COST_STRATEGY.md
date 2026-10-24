# Model, time and cost strategy

The workflow is designed partly to avoid dependence on one AI subscription's limits, one provider, or repeated expensive rediscovery.

## Separate reasoning from execution

The broad reasoning layer should understand the problem once.

The source workflow increasingly pushes semantics, design, tests and exact implementation edits into the Architect. When the Architect can express a slice as literal edits, the Host applies it with **0 executor provider turns**.

## Thin fallback executor

Cline remains useful for changes that are too large or awkward to express as exact edits, but it receives only a narrow slice instead of the whole project history.

That reduces duplicate reasoning, context size, accidental scope drift, and paid model time spent rediscovering decisions already recorded in documents.

## Check before spend

Preparation simulation can catch bad anchors, broken regression tests, exact-edit mistakes, diff hygiene failures, impacted-test failures and source-oracle failures before a fallback provider session begins.

## Model portability

OpenRouter is a replaceable provider/model boundary. Different roles can select models according to reasoning quality, latency, availability, price and task type.

The provider is replaceable; durable project state is not stored there.

## Explicit paid experimentation

The source project uses bounded approval for paid model experiments: selected model/provider, limited scope and a cost cap are established before physical sends.

This public portfolio does not reproduce private spend history. The design principle is that paid experimentation is a controlled resource, not an implicit side effect of planning.

## CI cost and time

The source project uses an on-demand self-hosted GitHub Actions runner pool. Local development happens before CI; Actions records exact-ref acceptance rather than acting as the development loop.

This preserves durable remote evidence while avoiding hosted-runner usage.

## Time control

Durable docs and SHA-bound handoffs reduce time lost to context resets. A later session can re-bootstrap from current main, the ledger, the handoff, Git history and verification evidence instead of reconstructing state from a long chat transcript.