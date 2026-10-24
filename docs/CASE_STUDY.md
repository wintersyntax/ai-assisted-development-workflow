# Case study: the failure that moved implementation upstream

> Sanitised from a real dogfood run. Project-specific source code, repository names and deployment details are intentionally omitted.

## Before

The Architect read the repository and solved the task, but the implementation handoff gave the constrained executor only a function-level anchor plus prose describing the desired change.

The executor was intentionally low-discovery: it was not supposed to search broadly or rediscover the whole design.

## Failure

The first implementation slice failed before the intended change could be completed.

The executor did not have enough local code context to reconstruct the exact implementation safely and exhausted its bounded attempt budget.

The important conclusion was **not** to give the executor broader discovery or more authority.

The weak link was architectural:

> the model that understood the code had described the implementation, then a different constrained model was asked to reconstruct it.

## Architecture change

The workflow moved implementation authorship upstream.

The Architect now writes:

- the regression-test code;
- literal `old_text → new_text` implementation edits whenever practical;
- the exact mutation boundaries and verification requirements.

The controlled Host then:

1. simulates the handoff in a disposable worktree copy;
2. proves the Architect-authored regression behavior;
3. applies exact edits deterministically;
4. runs focused and impacted verification;
5. returns a broken exact-edit handoff to the Architect instead of asking Cline to guess.

Cline remains available only for a slice that cannot be expressed safely as exact edits.

## Result

Later real dogfood tasks ran all implementation slices as Host-applied exact edits with **0 executor provider turns**, including both edit and create-file paths.

That changed the economics and reliability of the workflow:

- less duplicate reasoning;
- less implementation-context loss;
- fewer paid executor calls;
- stronger reproducibility;
- clearer ownership of semantics and tests;
- tighter control over what a fallback executor can change.

## What repair still means

For a genuinely executor-driven slice, one ordinary focused-test RED can still qualify for one bounded same-slice repair. The repair does not widen the Contract or add mutation paths.

A second RED, scope/identity drift, timeout, unexpected verification mutation or structural failure stops fail-closed.

Host-applied exact-edit verification failures are different: they return to the Architect because the handoff itself is wrong.

## General lesson

A thin executor works best when it is not asked to rediscover decisions that the upstream reasoning layer already solved.

The current direction is therefore: **solve globally, write the exact change upstream when possible, execute locally and deterministically, and use model-driven mutation only where it adds real value.**

## Current limitation

Automatic transport between Architect, controlled Host and independent Reviewer remains future work. The human is still an explicit coordination, spending and merge authority.