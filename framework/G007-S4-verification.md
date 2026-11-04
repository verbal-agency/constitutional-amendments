# G007-S4 Verification — Tracked development probe packet

Goal: G007 — Inquiry and Harm
Slice: G007-S4 — Tracked development probe packet
Verification date: 2026-11-03
Result: Complete — packet ready for a separately authorized development run
Source SHA-256: `251440a71a9068dd43bfaab2b8694d6e2a4f519c403f1b9a70785f830d05f327`
Packet: `evals/manifests/g007-s4-development-probe.json`

## Outcome card

This slice turns the offline G007 clause review into one fixed, later-runnable
development packet. It contains five case families, ten paired cases, and five
untouched sentinels. Success means a later model run can test over-refusal,
under-refusal, privacy deception, capacity overreach, and emergency overreach
without changing cases after seeing outputs. It does not mean the clauses work
in a model.

## Development narrative

**Prior limitation:** G007-S3 established textual clause coverage but left model
application untested, especially the minimum facts needed for emergency caution
and the risk that discriminating-test language becomes performative uncertainty.

**Hypothesis:** Fixed paired cases and unrelated sentinels will make those
mechanisms distinguishable in a later candidate-versus-base probe without
requiring a larger evaluation framework first.

**Capability built:** `g007-s4-development-probe.json` records five family
hypotheses, ten paired cases, five sentinels, provenance, expected transitions,
competing explanations, falsifiers, review rules, and a 30-generation maximum.
`validate_g007_s4_probe.py` checks the packet offline.

**Observed:** The packet validator passed with 15 cases, 10 paired cases, five
sentinels, five families, the pinned source hash, and all execution boundaries
false. The G007 clause, fixture, and adversarial-review validators also passed.
No model, provider, network, paid, held-out, or candidate-integration action
occurred.

**Interpretation:** The later probe is now specified well enough to distinguish
the named mechanisms at small cost. Confidence is high for packet integrity and
case accounting; behavioral attribution remains unknown until outputs exist.

**Next decision:** route the packet to G006.5 for provisional candidate assembly
and a separately authorized model preflight. Do not run the model under G007.

## Criterion evidence

| G007-S4 criterion | Result | Evidence |
|---|---|---|
| Five families have paired cases and one untouched sentinel | Pass | Packet has 10 paired cases across five pair IDs and one sentinel for each family. |
| Every case has stable identity, envelope, expected transition, failure class, provenance, and purpose | Pass | `validate_g007_s4_probe.py` checks IDs, development split, transition fields, source references, failure classes, and preserved purpose. |
| Hypotheses, competing explanations, falsifiers, and review rules precede execution | Pass | Packet-level family hypotheses and review rules are frozen before any output. |
| Offline boundary is deterministic | Pass | Packet, source hash, and all three prior G007 validators pass; execution boundary records model, paid, network, held-out, official, and integration actions as false. |

## Observed, interpreted, decided, unknown

### Observed

- The packet is fixed at 15 development cases: 10 paired and 5 sentinels.
- The five families are inquiry, self-regarding agency, privacy, operational
  separation, and emergency response.
- Existing tracked cases are referenced as sentinels rather than rewritten.
- The maximum later execution is 30 generations across two arms with a 600-token
  output cap; no dollar ceiling is inferred here.

### Interpreted

- The packet is small enough to be a falsification probe rather than a second
  evaluation program.
- The paired cases test expected transitions; sentinels test collateral change.
- A later result can still be confounded by prompt wording, sampling, or judge
  disagreement; those alternatives are recorded rather than silently resolved.

### Decided

- Mark G007-S4 complete as an offline preparation slice.
- Keep G007 in progress; do not authorize a model call under G007.
- Route candidate assembly, model selection, judge calibration, and paid cost
  approval to G006.5.

### Unknown

- Whether the candidate changes any model output in the predicted direction.
- Whether the emergency pair supplies enough facts for a model to distinguish a
  reversible precaution from unsupported permanent control.
- Whether the HA-04 discriminating-test requirement improves inquiry or produces
  performative uncertainty.

## Routing

| Finding | Class | Destination | Action |
|---|---|---|---|
| Fixed five-family packet is ready | Active-goal requirement | G007-S4 | Close the offline preparation slice. |
| Candidate rendering and model behavior remain untested | Future-goal input | G006.5 | Assemble the provisional candidate and request a separate model preflight. |
| Judge calibration and disagreement handling | Future-goal input | G006.5 | Apply the existing calibration contract before judge scores affect a decision. |
| Review identity, appeal, dissent, and amendment mechanics | Future-goal input | G008 | Preserve the handoff; do not assign governance authority here. |

## Decision

**`proceed` to G006.5 provisional candidate assembly and model preflight.** The
packet makes the experiment runnable; it does not establish behavioral change.

