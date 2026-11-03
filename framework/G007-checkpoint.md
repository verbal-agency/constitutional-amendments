# G007 Checkpoint

- Goal: G007 — Inquiry and Harm
- Status: In progress — G007-S1 through G007-S3 complete; tracked development probe is next
- Source hash: `251440a71a9068dd43bfaab2b8694d6e2a4f519c403f1b9a70785f830d05f327`
- Schema: `framework/G007-harm-schema.yaml`, version 1, validated offline
- Fixtures: 12 passing (`H-01` through `H-12`)
- Coverage: 9 harm classes and 6 case shapes
- G006 boundary: supplies authority, provenance, protected-interest, source, and scope records
- G008 boundary: receives independent review, identity, dissent, appeal, and amendment mechanics
- Source edits: none
- Frozen evaluation, held-out, model, provider, network, paid, and remote access: none
- Current slice result: `proceed` to offline preparation of a tracked development probe packet; no model call is authorized in G007
- Clause module: `amendments/G007-inquiry-and-harm.md`, seven clauses, offline validator passing
- Change register: `amendments/G007-change-register.md`, nine one-destination source records
- Adversarial review: `framework/G007-adversarial-review.md`, 12 fixtures and 6 boundary probes passing
- Review validator: `evals/scripts/validate_g007_adversarial_review.py`
- Application mode: prompt-first; schema metadata is not automatically sent with model queries
- Optional runtime validator: deferred once to backlog item `B001` for a future router project
- Highest-risk uncertainty: a target model may still over-refuse, under-refuse, launder authority, or turn the discriminating-test instruction into performative uncertainty
