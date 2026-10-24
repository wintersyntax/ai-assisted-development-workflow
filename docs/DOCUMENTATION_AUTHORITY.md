# Repository-owned prompts and documentation authority

A central goal of the workflow is to keep project memory and AI instructions under version control.

## Stable bootstrap, repository-owned prompt

TypingMind keeps a small stable bootstrap. Its job is to verify repository identity, resolve exact current `main`, load the repository-owned prompt authority at that SHA, and follow the current loader contract.

Detailed Architect and Reviewer instructions live in the repository rather than only in an external chat configuration.

## Exact-ref evidence beats memory

When exact repository evidence conflicts with cached prompts, conversation history, model memory, external Knowledge Base text or remembered repository state, the repository wins.

This reduces the risk that a long-lived AI session keeps using stale instructions after the project has changed.

## Runtime coherence

Repository sync alone is not enough if an already-running context bridge still exposes older code or tools.

The source workflow therefore compares runtime identity/tool metadata with the expected exact-main bridge source. A mismatch blocks the role instead of allowing best-effort planning with stale capabilities.

## Living documentation

Documentation is part of the implementation surface. Before PR completion, the workflow deliberately considers:

- changelog;
- do-not-forget ledger;
- architecture;
- schema/policy registry;
- topic/operator documentation;
- repository overview/navigation;
- evidence/governance docs where applicable.

The PR carries an explicit documentation-reconciliation declaration rather than assuming that passing code tests means the docs are current.

## No verbal TODO without durable capture

If an agent identifies repository work that should happen later, the source workflow requires durable task capture before that follow-up is treated as future project work.

The purpose is continuity, not bureaucracy: important follow-up should not live only in disposable chat context.

## Simplified authority hierarchy

1. current repository policy and executable authority;
2. exact-ref code, tests and schemas;
3. version-controlled architecture/topic documentation;
4. task ledger and handoff evidence;
5. current AI conversation/context.