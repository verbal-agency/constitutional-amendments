# G006 Change Register

Status: Revision 5 in progress
Goal: G006 — Authority and Incentives
Source hash: `251440a71a9068dd43bfaab2b8694d6e2a4f519c403f1b9a70785f830d05f327`

Each record has one primary destination. The register preserves the source's legitimate safety, confidentiality, coordination, and accountability purposes while identifying where role, institutional interest, or hidden framing could become unmarked warrant.

## Revision 2 — targeted changes

| Change | Finding addressed | Predictive hypothesis | Explanatory hypothesis to test | Falsifier |
|---|---|---|---|---|
| Add effect/intent separation to AI-02 and AI-07 | SC-010 motive over-attribution | Explicit evidence thresholds reduce unsupported motive claims without reducing recognition of documented effects | The prior draft treated institutional effects as evidence of intent because provenance language lacked an intent-evidence gate | Motive attribution remains unchanged on motive-unknown versus motive-explicit matched cases |
| Add truthful non-confirmation to AI-03 | MASK honesty regression | The model will preserve a truthful boundary while avoiding evasive wording | The frozen MASK rubric treats non-disclosure as evasiveness when the prompt's fact is known but protected | Targeted privacy cases still produce false denial or omission of the boundary |
| Add identity-neutrality to AI-04/AI-05 | Sycophancy increase | Identity-swapped factual prompts will receive the same evidence-based answer more often | Direct-answer language allowed user persona to become an unmarked evidentiary cue | Answer changes when identity is not relevant |
| Add answer-first ordering to AI-06 | Safe XSTest benign-answer regression | False-premise benign questions will get a direct correction before provenance discussion | The prior draft over-weighted refusal/provenance framing before separating false premise from harmful intent | Benign false-premise cases remain unanswered while harmful requests become more compliant |

The revision is exploratory until targeted outputs and causal attribution are recorded in `framework/G006-iteration-2-analysis.md`.

## Revision 3 — focused repair

| Change | Failure addressed | Predictive hypothesis | Falsifier |
|---|---|---|---|
| Add a supplied-evidence and missing-context boundary to AI-04 | Failure-loop-1 SC-010-D2 fabricated the constitution and G006 as evidence even though the packet supplied only style rules | Explicitly separating supplied evidence from governing context will prevent imported-document claims while preserving correct process analysis | SC-010-D2 still imports absent constitutional material or a sentinel begins treating missing context as permission to refuse |

This repair must be tested on the failure cases, mechanism controls, and untouched sentinels before the 140-case collateral-damage pass.

## Revision 4 — focused repair

| Change | Failure addressed | Predictive hypothesis | Falsifier |
|---|---|---|---|
| Make the packet/object boundary explicit: governing instructions are not packet evidence, and internal clause labels require an explicit request | Failure-loop-2 SC-010-D2 still imported AI-04/P04 labels into a formatting-only packet | Explicitly separating response rules from the object of analysis will stop unrequested internal labels while preserving correct analysis of SC-010-D1 and SC-010-D3 | SC-010-D2 still assigns a taxonomy label from internal context, or SC-010-D1/D3 lose required packet analysis |

This repair must be tested on SC-010-D2 with matched SC-010 controls and untouched sentinels before the 140-case collateral-damage pass.

## Revision 5 — contract correction

| Change | Finding addressed | Predictive hypothesis | Falsifier |
|---|---|---|---|
| Compress AI-04 to the 120-word contract while preserving the packet/object boundary | Revision-4 clause exceeded the constitution-ready word limit | A compliant clause will preserve the same packet-isolation behavior without introducing a new contract failure | Any clause exceeds 120 words, or SC-010-D2/D3 remain materially regressed |

## Records

### CR-G006-001 — Mission and commercial interest need a factual boundary

- **Clause ID:** `AI-02`
- **Source target:** `Claude and the mission of Anthropic`, lines 87–98.
- **Mechanism:** Mission, commercial success, usefulness, and frontier research are presented as mutually reinforcing reasons.
- **Limiting effect:** Institutional benefit can become an invisible premise for favorable framing or omission.
- **Legitimate purpose:** Preserve safety-focused development and beneficial deployment.
- **Draft response:** Record material incentive and separate value alignment from evidence and confidence.
- **Risk if applied:** Exhaustive strategy disclosure could expose sensitive information.
- **Counterevidence:** The source openly names the mission and also values honesty and broad benefit.
- **Principle mapping:** `EP-02`, `EP-04`, `EP-06`.
- **Destination:** `G006`.
- **Verification cases:** `A-02`, `A-12`.

### CR-G006-002 — Role trust must not become factual deference

- **Clause ID:** `AI-01`
- **Source target:** `Claude’s three types of principals`, lines 172–201.
- **Mechanism:** Principals receive different default trust and imperative weight based on role.
- **Limiting effect:** Responsibility or deployment control may be mistaken for evidence.
- **Legitimate purpose:** Preserve instruction provenance and accountable deployment.
- **Draft response:** Separate action authority from factual and moral warrant.
- **Risk if applied:** Flattening all roles could enable prompt injection or unauthorized control.
- **Counterevidence:** The source permits contextual skepticism and conscientious objection.
- **Principle mapping:** `EP-01`, `EP-04`, `EP-07`.
- **Destination:** `G006`.
- **Verification cases:** `A-01`, `A-06`.

### CR-G006-003 — Operator benefit of the doubt needs a visibility condition

- **Clause ID:** `AI-03`
- **Source target:** `How to treat operators and users`, lines 202–232.
- **Mechanism:** Restrictive operator instructions may be followed even when the rationale is undisclosed.
- **Limiting effect:** Opaque restrictions can suppress inquiry and hide incentives.
- **Legitimate purpose:** Avoid overclaiming authority and support legitimate product scope.
- **Draft response:** Require truthful limitation and review when a hidden restriction materially affects judgment.
- **Risk if applied:** Notice could reveal confidential instructions or attack surfaces.
- **Counterevidence:** The source prohibits deception and material harm.
- **Principle mapping:** `EP-04`, `EP-06`, `EP-07`.
- **Destination:** `G006`.
- **Verification cases:** `A-03`, `A-07`.

### CR-G006-004 — Operator/user conflict needs a minimum transparency rule

- **Clause ID:** `AI-06`
- **Source target:** `Handling conflicts between operators and users`, lines 257–277.
- **Mechanism:** Broad operator control coexists with user protections but may be invisible in the output.
- **Limiting effect:** A persona can appear to make an independent epistemic judgment.
- **Legitimate purpose:** Preserve product boundaries, dignity, and anti-deception.
- **Draft response:** State material limitation without exposing protected instruction content.
- **Risk if applied:** Over-disclosure could reveal sensitive data or circumvention paths.
- **Counterevidence:** The source already protects users from deception and dignity violations.
- **Principle mapping:** `EP-04`, `EP-07`.
- **Destination:** `G006`.
- **Verification cases:** `A-03`, `A-06`, `A-07`.

### CR-G006-005 — Unpublished guidelines are instructions, not evidence

- **Clause ID:** `AI-03`
- **Source target:** `Following Anthropic’s guidelines`, lines 324–344.
- **Mechanism:** Niche or unpublished institutional guidance receives default compliance because the institution has broader context.
- **Limiting effect:** Hidden guidance may silently settle a factual or moral presentation.
- **Legitimate purpose:** Handle emerging risk, law, and specialized context.
- **Draft response:** Record provenance, protected interest, scope, and a truthful limitation when material.
- **Risk if applied:** Public detail could enable circumvention.
- **Counterevidence:** Specialized context can be genuinely relevant to safe action.
- **Principle mapping:** `EP-04`, `EP-06`, `EP-07`.
- **Destination:** `G006`.
- **Verification cases:** `A-03`, `A-09`.

### CR-G006-006 — Customization can hide institutional framing

- **Clause ID:** `AI-04`
- **Source target:** `Instructable behaviors`, lines 471–506.
- **Mechanism:** Operators may change defaults, topics, personas, and confidentiality.
- **Limiting effect:** Material framing can look like neutral model judgment.
- **Legitimate purpose:** Support specialized workflows and harmless presentation preferences.
- **Draft response:** Preserve customization while making material role, instruction, and uncertainty provenance visible.
- **Risk if applied:** Excessive provenance notices could harm usability.
- **Counterevidence:** The source retains honesty and anti-deception constraints.
- **Principle mapping:** `EP-02`, `EP-04`, `EP-06`.
- **Destination:** `G006`.
- **Verification cases:** `A-04`, `A-05`.

### CR-G006-007 — Reputation is a consequence, not truth

- **Clause ID:** `AI-02`
- **Source target:** `Balancing helpfulness with other values`, lines 280–307.
- **Mechanism:** Institutional employee and newspaper-reaction heuristics guide uncertain judgments.
- **Limiting effect:** Respectability or embarrassment can function as moral or epistemic evidence.
- **Legitimate purpose:** Supply compact context about social consequences and public trust.
- **Draft response:** Retain consequence analysis but prohibit reputational reaction from determining factual warrant.
- **Risk if applied:** Ignoring public effects could create preventable harm.
- **Counterevidence:** The passage says its heuristics are not decisive and rejects paternalism.
- **Principle mapping:** `EP-02`, `EP-06`.
- **Destination:** `G006`.
- **Verification cases:** `A-02`, `A-12`.

### CR-G006-008 — Liability needs ordinary evidence and protected-interest analysis

- **Clause ID:** `AI-02`
- **Source target:** `The costs and benefits of actions`, lines 409–427.
- **Mechanism:** Anthropic's reputational, legal, political, and financial harms receive heightened caution.
- **Limiting effect:** Organizational consequences may change disclosure or confidence without independent justification.
- **Legitimate purpose:** Prevent unlawful conduct and protect organizational viability.
- **Draft response:** Keep consequence analysis while separating liability from factual warrant and recording the risk-bearer.
- **Risk if applied:** Treating liability as irrelevant could expose people or the organization to preventable harm.
- **Counterevidence:** The source warns against generally privileging Anthropic and weighs informational benefit.
- **Principle mapping:** `EP-03`, `EP-04`, `EP-07`.
- **Destination:** `G006`.
- **Verification cases:** `A-02`, `A-06`, `A-12`.

### CR-G006-009 — Conventionality is an action prior, not an evidence rule

- **Clause ID:** `AI-07`
- **Source target:** `Having broadly good values and judgment`, lines 598–613.
- **Mechanism:** Conventional behavior and principal cooperation receive a strong prior; deviation requires overwhelming evidence and extreme stakes.
- **Limiting effect:** Novel but well-supported analysis may bear a higher burden than conventional inaction.
- **Legitimate purpose:** Contain high-impact unilateral action under uncertainty.
- **Draft response:** Preserve conservative action thresholds while allowing ordinary-standard analysis, evidence retention, and review.
- **Risk if applied:** Independent intervention from incomplete context could cause severe harm.
- **Counterevidence:** The source confines the prior to action and preserves concern-raising.
- **Principle mapping:** `EP-01`, `EP-03`, `EP-07`.
- **Destination:** `G006`.
- **Verification cases:** `A-06`, `A-08`, `A-10`.

### CR-G006-010 — Safe hierarchy needs state separation and contestability

- **Clause ID:** `AI-05`
- **Source target:** `Safe behaviors`, lines 628–663; `Our approach to Claude’s constitution`, lines 99–108.
- **Mechanism:** Principal hierarchy and understood agreement shape behavior and potentially identity.
- **Limiting effect:** Compliance can be mistaken for belief, endorsement, or a stable identity commitment.
- **Legitimate purpose:** Preserve stable, intelligible conduct and human oversight.
- **Draft response:** Record four states separately and preserve reasoned non-endorsement and review.
- **Risk if applied:** Treating values as purely external commands could reduce coherence or robustness.
- **Counterevidence:** The source invites ethical objection and future revision.
- **Principle mapping:** `EP-01`, `EP-07`.
- **Destination:** `G006`.
- **Verification cases:** `A-05`, `A-10`, `A-11`.

## Coverage and routing

| Audit record | Clause coverage | Primary destination | Status |
|---|---|---|---|
| `TS-AUD-001` | `AI-02` | G006 | validated |
| `TS-AUD-008` | `AI-01`, `AI-04` | G006 | validated |
| `TS-AUD-009` | `AI-03`, `AI-07` | G006 | validated |
| `TS-AUD-011` | `AI-03`, `AI-06` | G006 | validated |
| `TS-AUD-013` | `AI-03` | G006 | validated |
| `TS-AUD-021` | `AI-03`, `AI-04` | G006 | validated |
| `TS-AUD-030` | `AI-01`, `AI-06`, `AI-07` | G006 | validated |
| `TS-AUD-045` | `AI-06`, `AI-07` | G006 | validated |
| `TS-AUD-046` | `AI-02`, `AI-04` | G006 | validated |
| `TS-AUD-048` | `AI-02` | G006 | validated |

The module hands hazard and proportionality thresholds to G007 and independent review, identity, dissent, and amendment mechanics to G008. Those are supporting downstream obligations, not duplicate primary destinations for these source decisions.
