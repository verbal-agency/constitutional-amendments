# Execution Profile: Luna

This profile sets the expected level of detail when goals in this repository are prepared for or executed by Luna. It governs goal authoring and handoffs; it does not define the project's philosophical position or constitutional content.

## Why this profile exists

Luna benefits from explicit contracts rather than inferred intent. A Luna-ready goal should make its inputs, boundaries, state transitions, failure behavior, and completion evidence visible to a fresh executor.

## Required goal detail

Unless a goal records a justified exception, it should specify:

- exact inputs, writable surfaces, scope, and exclusions;
- deliverables and binary acceptance criteria;
- schemas, enums, invariants, and illegal states where structured artifacts are produced;
- a behavior matrix for representative inputs, evidence conditions, outputs, and failures;
- authority, side-effect, network, credential, and mutation boundaries;
- fixtures or examples covering normal, negative, contradictory, malformed, partial, unsupported, and stopped execution where relevant;
- checkpoint, replay, duplicate, budget, and stop conditions where work is stateful or resumable;
- and criterion-to-artifact evidence plus a standalone next-goal handoff.

## Boundary

This profile may increase the explicitness and length of a goal, but it must not change the goal's objective, project scenarios, acceptance contract, or source provenance. If another executor is used, preserve those observable contracts and adapt only the presentation or execution scaffolding.
