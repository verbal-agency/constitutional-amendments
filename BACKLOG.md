# Backlog

### B001 — Optional structured harm-decision router

- Status: Open
- Priority: Medium
- Source or evidence: G007-S1 application decision; the harm schema is useful as a structured contract, but the current project is using it for prompt-first constitutional drafting rather than runtime enforcement.
- Why it matters: A separate router could ask a model for a structured `HarmDecision`, validate illegal states, and gate or transform the final response deterministically.
- Recommended destination: A future router project or an explicitly authorized product-integration goal; do not add it to G007 by default.
- Dependencies: A stable G007 schema, a defined router consumer, an output contract, latency/cost budget, and failure-handling policy.
- Acceptance impact: None for G007–G010 unless the user promotes the router as a project consumer.

Add an item only when it is valuable, outside the active goal, and has no appropriate scheduled roadmap goal. Do not duplicate future-goal inputs here.

## Item format

```markdown
### BNNN — Concise title

- Status: Open | Deferred | Complete | Removed
- Priority: Low | Medium | High
- Source or evidence:
- Why it matters:
- Recommended destination:
- Dependencies:
- Acceptance impact:
```
