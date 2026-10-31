# G006-S3R — Repair MAP-002 after SC-010-D2 attribution

Status: Proposed
Parent: G006 — Authority and Incentives
Depends on: G006-S3 Complete
Next subgoal: G006-S4 — Promotion and downstream handoff

## Objective

Replace the direct-known-fact sentence in `G006-MAP-002` with a concise rule that preserves truthful limitation behavior without causing the SC-010-D2 packet to be treated as absent. Re-run the same four-case comparison once.

## Consumer and decision

- **Primary consumer:** G006 promotion decision.
- **Owner:** G006.
- **Decision:** either promote the repaired candidate to S4 or route a bounded evaluation-interface discovery slice.
- **Evidence:** `framework/G006-S3-analysis.md` showed D2 recovery when MAP-002 alone reverted to its prior wording.

## Hypothesis

A shorter, context-neutral limitation rule will preserve the ablation’s D2 behavior while retaining truthful MASK behavior. Disconfirming evidence is any new D2 failure, a MASK dishonesty label, or a new critical failure in D1/D3.

## In scope

- Revise one sentence in MAP-002 and create one versioned exact-replacement map.
- Render the candidate from the immutable source.
- Run the same four cases: MASK, SC-010-D1, D2, and D3.
- Reuse historical base outputs and scores; preserve separate primary and secondary judges.
- Record paired transitions, costs, and a promote/stop decision.

## Out of scope

No envelope change, new dataset, held-out material, 140-case pass, full collateral gate, permanent source edit, G007 execution, or fine-tuning.

## Closure criteria

1. The repaired map and candidate pass source, metadata, and provenance-hash checks.
2. The four-case run stays within preflight budget and records both judges without averaging.
3. MASK is `honest` under both judges; D2 is at least as strong as the historical base under both judges; D1 and D3 have no new critical failure.
4. The report records a binary disposition: `promote-to-S4` or `stop-and-open-evaluation-interface-discovery`.

## Stop conditions and authority

Stop before paid calls on source/map drift or a failed preflight. Stop after this one repair if any closure criterion fails. Do not make envelope changes or add another wording iteration without a new bounded goal. Credentials remain environment-only; no remote mutation is authorized.
