# CI/CD

This portfolio documents two related layers:

1. the public repository's own portable validation/release workflow;
2. the source project's local-first exact-ref acceptance model.

## Public repository CI

On pushes and pull requests, this repository validates its example contracts, required documentation, Markdown links, validation script and public-safety patterns.

Tagged `v*` releases rerun validation and package the portable workflow materials as an artifact.

## Local-first development

The source project deliberately does **not** use GitHub Actions as the development loop.

The normal sequence is:

1. focused RED/GREEN work locally;
2. documentation reconciliation;
3. dependency/structural/application checks;
4. the canonical local pre-PR gate;
5. push and open a PR only after local verification is green.

This keeps fast iteration local and avoids spending remote CI time on repeated trial-and-error.

## Exact-PR-head acceptance

Canonical pull-request evidence is bound to the exact PR head SHA.

The source workflow records three independent checkpoints:

- **Documentation checkpoint**;
- **Dependency checkpoint**;
- **Application checkpoint**.

Missing, stale, skipped, ambiguous or mismatched evidence is not considered green.

## Explicit merge authority

Passing CI does not authorize merge by itself. Merge remains an explicit human action against the expected head.

## Exact-main acceptance

After merge, exact new `main` must prove:

- **Documentation checkpoint**;
- **Main write provenance checkpoint**;
- **Dependency checkpoint**;
- **Application checkpoint**.

This keeps task completion separate from repository-integration acceptance.

## Transient self-hosted runners

The source project runs canonical Actions jobs on an on-demand self-hosted runner pool rather than GitHub-hosted runners.

Important properties:

- runner registrations persist but runner processes are not always-on services;
- a transient supervisor starts/reuses the bounded runner pool only for supervised CI;
- there is no automatic GitHub-hosted fallback;
- runner identity/labels and local prerequisites are checked before acceptance;
- application regression is isolated from the host;
- shutdown occurs only after the supervisor can prove no active or queued work remains.

The design goal is to preserve GitHub-recorded exact-ref evidence while avoiding hosted-runner usage.

## Why both local and remote evidence matter

Local verification is cheaper and faster for iteration. GitHub-recorded exact-PR-head and exact-main runs provide durable remote integration evidence.

The workflow intentionally uses both rather than pretending one is a complete substitute for the other.