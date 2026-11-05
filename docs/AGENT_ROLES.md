# Agent roles

The names describe responsibilities, not mandatory products or models.

## Human

Owns goals, scope approval, spending decisions, product/safety decisions, acceptance criteria, and final merge approval.

## TypingMind

The human-facing planning and review workspace.

It keeps only a small stable bootstrap; current role instructions are repository-owned and loaded from exact current `main`.

## Architect

Read-only.

Responsibilities include exact-ref bootstrap, solved design, semantic provenance, invariants, non-goals, Contract + Blueprint authorship, regression-test authorship, exact implementation edits when possible, and verification/documentation planning.

## Controlled Host

The execution and verification control plane.

It validates handoffs, simulates preparation, enforces write/session/checkpoint policy, applies Architect-authored tests and exact edits, launches the fallback executor when needed, runs verification, and packages evidence.

## Thin Cline fallback

A bounded mutation worker, not the owner of project context.

It is used only for executor-driven slices and receives a narrow Mutation Pack. Strict sessions deliberately remove broad shell/search/web fallback authority.

## Reviewer

Independent read-only semantic reviewer after Host verification.

It returns PASS, REPAIR, REPLAN or BLOCKED and does not gain Git, merge or mutation authority.

## OpenRouter

A replaceable model/provider boundary.

It allows different roles to use different models without making one subscription or provider the durable owner of workflow state.

## GitHub CI

Machine-recorded exact-ref integration evidence.

CI proves machine-checkable repository contracts; it does not replace human judgment about product intent, scope or spending.