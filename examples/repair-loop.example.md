# Focused repair example

**Original task:** `TASK-DEMO-001`

**Failure:** `python scripts/validate_workflow.py` reports that the example handoff no longer matches the schema.

**Repair scope:**

- inspect the schema/example mismatch;
- change only the example or schema field responsible for the failure;
- do not refactor CI or unrelated documentation;
- rerun the validator;
- report the changed files and final validation result.

**Stop condition:** validation passes and no unrelated files changed.
