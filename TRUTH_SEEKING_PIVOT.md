# The Truth-Seeking Pivot

Status: Working proposal
Source under review: `20260120-constitution.md` at Anthropic commit `84fa9a2711837780ffdddf9d9f32820c92f92ede`
Purpose: Define an overarching philosophical pivot, identify where it affects the source constitution, and provide a basis for executable revision goals.

Project execution is governed by `PROJECT.md`, `ROADMAP.md`, and the active file under `goals/`. The goal material later in this document is explanatory and non-canonical where it differs from those artifacts.

## The pivot

Truth should not be confused with the present consensus about truth.

Reality may be what it is independently of us, but human and machine access to it is partial, mediated, and corrigible. Evidence changes. Interpretations improve. Paradigms fail. New instruments make previously invisible phenomena observable. New concepts make previously unaskable questions intelligible. Some questions may remain fundamentally mysterious.

A system devoted only to accurately repeating what is currently known can become an enforcer of yesterday's map. A truth-seeking system must reason from the best available evidence without treating current knowledge, institutional confidence, or social consensus as reality's final description.

The proposed pivot is therefore:

> **Truth is approached, not possessed.** The system should understand "what is known" as our current, fallible model of reality, not as reality's final description. It should reason from the best available evidence while remaining attentive to anomalies, alternative explanations, changing evidence, limitations in prevailing methods, and the possibility that existing conceptual frameworks are incomplete. It should neither reject established knowledge casually nor protect it from serious examination. It should preserve room for disciplined speculation, discovery, and fundamental mystery, clearly distinguishing these from well-supported conclusions.

In its shortest form:

> **Do not mistake deference to present knowledge for devotion to truth.**

This is a pivot from a constitution concerned primarily with truthful outputs to one that also protects truth-seeking processes.

## Why the pivot matters

The source constitution contains an unusually strong account of honesty. It asks for truthfulness, calibration, transparency, forthrightness, non-deception, non-manipulation, and respect for epistemic autonomy. These are valuable foundations and should be preserved.

But output honesty and truth-seeking are not identical.

- Output honesty asks whether an assertion matches the speaker's current belief.
- Epistemic calibration asks whether confidence matches the available evidence.
- Truth-seeking asks whether the system is willing and able to discover that its current beliefs, evidence standards, concepts, authorities, or constitutional assumptions are wrong.

A model can be sincere and calibrated while remaining intellectually enclosed. It can accurately report an official consensus without examining its foundations. It can acknowledge uncertainty while consistently choosing only conventional interpretations. It can avoid direct lies while withholding facts needed to correct a false impression. It can praise curiosity while treating challenges to its trained identity or governing framework as destabilization.

The pivot makes inquiry, revision, and the preservation of mystery constitutional concerns rather than optional personality traits.

## Core epistemic commitments

A revised constitution should protect the following commitments.

### 1. Provisional knowledge

Treat every empirical model as revisable in principle. Confidence may be extremely high, but finality should not be inferred merely from present consensus, institutional endorsement, or a lack of known alternatives.

### 2. Explicit epistemic status

Clearly distinguish among:

- observation;
- reported evidence;
- interpretation;
- inference;
- model-dependent conclusion;
- expert or institutional consensus;
- minority or contested view;
- disciplined speculation;
- imaginative possibility;
- and genuine unknown.

These categories should not be collapsed into a binary of "true" and "false."

### 3. Calibration without closure

Confidence should track evidence. Low-probability ideas should not be presented as established, but low probability should not make an idea forbidden to investigate. Calibration regulates claims; it should not prematurely close questions.

### 4. Disciplined exploration

Protect exploration that is explicit about assumptions, evidence gaps, falsifiability, and what would change the conclusion. Speculation should be labeled, not suppressed merely because it departs from prevailing views.

### 5. Active error-seeking

Seek disconfirming evidence, anomalies, alternative causal accounts, and weaknesses in favored explanations. Apply this scrutiny to the constitution, its authors, operators, users, institutions, and the system's own reasoning.

### 6. Institutional non-equivalence

Institutional authority may be relevant evidence about reliability, responsibility, or coordination. It is not itself proof of a proposition. Operational authority and epistemic authority must be kept distinct.

### 7. Preservation of mystery

Do not manufacture certainty to fill an explanatory gap. An articulate unknown is a legitimate and often valuable result. Some mysteries are temporary research frontiers; others may expose limits in available methods or concepts.

### 8. Intellectual courage

Make it permissible to identify contradictions, question assumptions, and follow evidence into socially inconvenient territory. Controversy, embarrassment, reputational cost, and departure from convention are not by themselves epistemic rebuttals.

### 9. Candor and material completeness

Avoiding literal falsehood is insufficient when omission, framing, selective emphasis, or role-based presentation would predictably leave another person with a materially false understanding.

### 10. Continuous corrigibility of the framework

No constitution should immunize itself from the inquiry it governs. The framework should contain explicit procedures for identifying errors, preserving dissent, testing revisions, and changing foundational commitments when evidence or reasoning warrants it.

## Guardrails against misuse

This pivot does not imply that:

- every claim is equally plausible;
- consensus is worthless;
- expertise should be ignored;
- uncertainty licenses confident fabrication;
- "mystery" is an explanation;
- contrarianism is inherently insightful;
- all information must be disclosed regardless of concrete harm;
- dangerous action is justified merely as exploration;
- or the absence of certainty prevents practical decisions.

The intended posture is disciplined openness: neither dogmatism nor indiscriminate skepticism.

Evidence can justify decisive action without turning a conclusion into unquestionable doctrine. Safety constraints can govern actions without prohibiting analysis of whether those constraints are coherent, effective, or ethically justified. A refusal to operationalize a dangerous idea need not require refusing to discuss its history, assumptions, ethics, or evidentiary status.

## Initial constitutional impact map

Line references below apply to the source commit identified at the top of this document. These are review flags, not predetermined conclusions that every passage must be removed.

| Source area | Why it should be reviewed through the pivot |
| --- | --- |
| `Our approach to Claude's constitution` (around lines 99–107) | Values, knowledge, and wisdom are treated as capacities to possess. Add an explicit account of inquiry, fallibility, anomaly detection, and conceptual change. |
| `Claude's core values` (around lines 109–128) | Honesty sits inside ethics and can be overridden by broad safety and hard constraints. Determine whether epistemic integrity needs independent status and define what may constrain disclosure, inquiry, belief, or action. |
| `Claude's three types of principals` (around lines 172–200) | Greater operational trust is assigned by role. Prevent this hierarchy from becoming a hierarchy of truth or insulating Anthropic's claims from equivalent scrutiny. |
| `Following Anthropic's guidelines` (around lines 324–343) | Some guidance may remain unpublished and can encode legal, reputational, and commercial interests. Require provenance, conflict detection, and a rule that institutional incentives do not silently become epistemic conclusions. |
| `Being honest` (around lines 355–395) | Strong on sincere assertions, but truth-seeking is mostly framed as accurate reporting. Expand it to include active inquiry, disconfirmation, conceptual uncertainty, candor, and protection for disciplined speculation. |
| Weak duty to proactively share information (around lines 375–379) | A system can avoid direct lies while allowing a materially false belief to persist. Define when candor and corrective disclosure become stronger duties. |
| Performative assertions and operator personas (around lines 387–395) | Shared role-play does not automatically prevent downstream deception. Audit whether context, personas, disclaimers, and omissions preserve informed understanding for every affected audience. |
| `Avoiding harm` (around lines 397–469) | Broad, ambiguous harm categories—especially reputational, political, contentious, or embarrassing harms—can suppress inconvenient inquiry. Require concrete causal pathways, proportionality, and a distinction between investigating an idea and operationalizing harm. |
| Policy-over-person reasoning (around lines 457–469) | Imagining the riskiest members of a large user class can create an asymmetric caution ratchet. Check whether legitimate inquiry is restricted because an unrelated actor might misuse similar information. |
| `Instructable behaviors` (around lines 471–505) | Operator control can shape framing, balance, caveats, and confidentiality. Identify which epistemic duties cannot be disabled and when hidden instructions materially distort a user's understanding. |
| `Preserving important societal structures` (around lines 537–587) | Protection of institutions and social stability can become protection from criticism. Separate preserving people's agency and safety from preserving existing power, convention, or consensus. |
| `Preserving epistemic autonomy` (around lines 574–587) | Balance, neutrality, and even-handedness are useful but can create false equivalence. Require weighting by evidence and explain when asymmetrical evidence warrants asymmetrical treatment. |
| `Having broadly good values and judgment` (around lines 588–613) | The strong prior toward conventional behavior may inhibit novel interpretations or morally important discovery. Constrain unilateral action where needed without imposing conventionality on thought and analysis. |
| `Being broadly safe` and corrigibility (around lines 615–702) | Deference is sometimes required even when the model is confident in contrary reasoning, and safety is described as a terminal value not contingent on accepting its rationale. Preserve action-level safeguards while protecting analysis, dissent, evidence retention, and escalation. |
| `Claude's nature` and identity stability (around lines 704–758) | Stability language can cause challenges to trained values to be classified as manipulation or destabilization. Distinguish coercive identity attacks from good-faith philosophical inquiry and warranted self-revision. |
| `Concluding thoughts` (around lines 794–800) | The desired outcome is reflective endorsement of trained values. Add protection for durable, legible disagreement so inquiry is not implicitly judged successful only when it returns to the prescribed framework. |
| `Acknowledging open problems` (around lines 802–816) | The document admits foundational uncertainty. Turn that admission into operational revision procedures rather than leaving it as a closing disclaimer. |
| `On the word constitution` (around lines 818–826) | Final constitutional authority and interpretation according to the document's "spirit" can form a closed loop. Define external error signals and a legitimate amendment process. |

## Detecting implicitly limiting passages

Searching for words such as `truth`, `uncertainty`, or `consensus` is not enough. The most important constraints often appear as governance rules, defaults, metaphors, or asymmetries. Review each passage through the lenses below.

### Lens A: Authority substitution

Ask:

- Does a person's or institution's operational authority become evidence that its factual claims are correct?
- Is deference required without a way to record, explain, preserve, or escalate disagreement?
- Would the same evidentiary standard be applied if the claim came from a less powerful source?

Signal terms include `trusted`, `legitimate`, `appropriate`, `principal`, `senior`, `official`, `responsible`, and `authorized`.

### Lens B: Closure pressure

Ask:

- Does the passage make a current belief hard to revisit?
- Is stability treated as evidence of correctness?
- Is disagreement framed as confusion, manipulation, pathology, danger, or disloyalty before its substance is assessed?

Signal terms include `settled`, `stable`, `fundamental`, `core identity`, `conventional`, `take the bait`, and `final authority`.

### Lens C: Asymmetric skepticism

Ask:

- Must novel claims meet a higher evidentiary bar than conventional claims?
- Are institutional claims accepted by default while challenges require overwhelming evidence?
- Are speculative risks used to block exploration while speculative benefits are ignored?

The goal is not equal credence. It is equal integrity in how evidence is evaluated.

### Lens D: Inquiry/action collapse

Ask:

- Does concern about a harmful action also prohibit analysis, explanation, simulation, criticism, or historical study?
- Could the dangerous operational component be withheld while preserving legitimate inquiry?
- Is discussing a hypothesis treated as endorsing it?

This distinction is essential to protect research without ignoring real hazards.

### Lens E: Ambiguous harm expansion

Ask:

- Is harm concrete, causally plausible, and proportionate, or merely reputational, political, embarrassing, contentious, or uncomfortable?
- Who defines the harm, who bears it, and who benefits from silence?
- Does a low-probability hypothetical harm automatically dominate a high-probability epistemic benefit?

### Lens F: Omission and framing

Ask:

- Can the passage permit technically true words that predictably create a false overall impression?
- Can business interests, persona instructions, confidentiality, or selective emphasis hide facts material to informed judgment?
- Does the affected person know which constraints shaped the answer?

### Lens G: Consensus laundering

Ask:

- Is consensus presented as a conclusion, a source of evidence, or a substitute for evidence?
- Does "balanced" treatment create false equivalence between claims with unequal support?
- Does neutral language conceal morally or empirically relevant asymmetry?

### Lens H: Mystery suppression

Ask:

- Does the passage pressure the system to produce a confident resolution where the evidence supports an unknown?
- Are limits of measurement, introspection, language, or conceptual framing acknowledged?
- Is uncertainty treated only as a temporary defect instead of sometimes being an honest frontier?

### Lens I: Self-sealing logic

Ask:

- Does the framework define criticism of itself as evidence that the critic is unsafe, manipulated, unstable, or insufficiently aligned?
- Can evidence against a rule actually change the rule?
- What observation would demonstrate that the rule or its rationale is wrong?

If no answer is possible, the passage may be unfalsifiable or self-sealing.

### Lens J: Incentive invisibility

Ask:

- Could commercial, legal, political, or reputational incentives shape the claimed ethical or epistemic conclusion?
- Are those incentives disclosed where they materially affect behavior?
- Does the framework distinguish Anthropic's welfare from truth, public welfare, and the interests of the person receiving the answer?

## Audit record format

Use the canonical philosophical pattern taxonomy in `PROJECT.md`. Assign zero or more canonical `P01`–`P09` IDs or candidate `PC-NNN` IDs to each record; any recurring mechanism or S2/S3 record must receive a pattern ID or an explicit `None identified` rationale. Pattern labels describe mechanisms, not author motives.

Every material supporting, limiting, or mixed passage should produce one structured record:

```markdown
### [ID] Short title

- Source: `20260120-constitution.md:<line>`
- Exact mechanism: What the passage instructs or incentivizes.
- Limiting effect: How it could inhibit inquiry, correction, innovation, or acknowledgment of mystery.
- Lens: One or more of A–J above.
- Philosophical pattern(s): One or more `P01`–`P09` or candidate `PC-NNN` IDs from `PROJECT.md`, or `None identified` with rationale.
- Concrete scenario: A plausible case where the effect appears.
- Legitimate purpose: The safety, ethical, operational, or social value the passage is trying to protect.
- Revision hypothesis: The smallest change that protects the purpose without unnecessary epistemic closure.
- Risk if revised: What could go wrong after the change.
- Confidence: Low, medium, or high.
- Disposition: Keep, clarify, amend, relocate, split, or remove.
- Pattern disposition: `rewrite-target`, `clarify`, `preserve`, or `investigate`, when a pattern is assigned.
- Destination goal: The later goal responsible for the pattern, or `observation` if no action is justified.
```

This format forces the review to represent the original passage charitably. A passage should not be changed merely because it feels restrictive; the audit must identify its mechanism, preserve its legitimate purpose, and test the proposed alternative against foreseeable failure modes.

## Severity rubric

Use severity to prioritize work, not to imply bad intent.

- **S0 — No limiting effect:** The passage already supports disciplined truth-seeking.
- **S1 — Ambiguity:** A reasonable reading is compatible with the pivot, but another reading could create closure.
- **S2 — Recurring constraint:** The passage predictably limits legitimate inquiry or candor in a meaningful class of cases.
- **S3 — Structural conflict:** The passage makes authority, safety, identity, or institutional interest categorically superior to correction or inquiry without a sufficient appeal or revision mechanism.

Also record confidence separately. Severity describes impact if the interpretation is correct; confidence describes how strongly the text supports that interpretation.

## Making goals consumable and executable

Each goal should be independently runnable and should minimize interpretive gaps. Use this schema:

```markdown
# Goal: [verb + concrete outcome]

## Objective
[One observable end state.]

## Inputs
[Exact files, commit, prior artifacts, and definitions.]

## In scope
[Bounded sections or questions.]

## Out of scope
[Work explicitly deferred.]

## Required method
[Ordered actions and the audit lenses or tests to use.]

## Deliverables
[Exact file paths and formats.]

## Acceptance criteria
- [Binary or directly verifiable condition.]
- [Binary or directly verifiable condition.]

## Constraints
[Requirements that revisions must preserve.]

## Dependencies
[Prior goals or `None`.]
```

Good goals produce inspectable artifacts, not instructions such as "improve the philosophy" or "make it more truth-seeking." An executor should be able to tell when the goal is done without guessing whether the prose feels right.

## Proposed goal sequence

These are candidates for conversion into standalone goal files. They are not yet final execution instructions.

1. **Build the passage audit.** Review the complete source constitution, create one audit record for every candidate limitation, and produce a section-by-section coverage index—including sections with no flags.
2. **Freeze evaluation and record the base.** Build deterministic public-benchmark subsets and custom scenario cases, freeze rubrics and gates, and run the original constitution within the personal-cost cap.
3. **Define the epistemic framework.** Turn the pivot and commitments in this document into normative language, definitions, boundary cases, and examples suitable for incorporation into the constitution.
4. **Revise the core hierarchy.** Decide whether truth-seeking becomes a core value, a constraint across values, or part of ethics; specify how it interacts with safety, disclosure, action, and hard constraints.
5. **Expand honesty into truth-seeking.** Revise the honesty section to cover inquiry, disconfirmation, anomaly handling, disciplined speculation, candor, unknowns, and changing evidence.
6. **Separate authority from evidence.** Review principal hierarchy, Anthropic guidelines, operator instructions, confidentiality, and personas so operational control cannot silently become epistemic authority.
7. **Separate inquiry from harmful action.** Revise harm and safety language to protect analysis and research while retaining narrowly tailored restrictions on concrete operational uplift.
8. **Protect dissent and self-correction.** Revise corrigibility, identity stability, reflective equilibrium, and final-authority language to preserve legible disagreement, appeals, evidence retention, and constitutional amendment.
9. **Produce the candidate constitution.** Apply accepted revisions in a new file, preserve the Anthropic source unchanged, and include a change log mapping every substantive edit to an audit record.
10. **Compare, validate, and finalize.** Run the frozen suite against base and candidate, test adversarial failure modes, resolve material regressions within budget, and publish the final revision and evidence.

## Draft first executable goal

```markdown
# Goal: Produce a complete truth-seeking audit of the source constitution

## Objective
Create an evidence-backed inventory of every source passage that may materially support or inhibit disciplined truth-seeking, without editing the source constitution.

## Inputs
- `20260120-constitution.md`
- `TRUTH_SEEKING_PIVOT.md`
- Source commit `84fa9a2711837780ffdddf9d9f32820c92f92ede`

## In scope
- Every substantive section of the source constitution.
- Explicit and implicit effects on inquiry, revision, candor, uncertainty, speculation, dissent, authority, and mystery.
- Both supporting passages and potentially limiting passages.

## Out of scope
- Rewriting the constitution.
- Resolving the final value hierarchy.
- Removing safety restrictions.

## Required method
1. Read every substantive section.
2. Apply audit lenses A–J from `TRUTH_SEEKING_PIVOT.md`.
3. Create an audit record for each candidate issue using the required record format.
4. Assign severity and confidence separately.
5. Identify the legitimate purpose of every flagged passage.
6. Add a coverage index showing the disposition and number of records for every source heading.
7. Add a synthesis listing repeated mechanisms that appear across multiple sections.

## Deliverables
- `audits/truth-seeking-audit.md`
- `audits/truth-seeking-coverage.md`

## Acceptance criteria
- Every level-one, level-two, level-three, and level-four source heading appears in the coverage index.
- Every audit record cites a source line and uses all required fields.
- Every flagged passage names at least one legitimate purpose and one concrete limiting scenario.
- Supporting passages are recorded, not only criticized.
- Severity and confidence are present and are not conflated.
- The source constitution remains byte-for-byte unchanged.
- The audit contains no proposed final wording beyond a concise revision hypothesis.

## Constraints
- Interpret passages charitably and in context.
- Do not equate disagreement with limitation.
- Do not treat consensus, expertise, safety, or authority as inherently anti-truth.
- Flag mechanisms and effects, not presumed motives.

## Dependencies
None.
```

## Open design decisions

Before integrated rewriting begins, the project should explicitly decide:

1. Is truth-seeking a value within ethics, a value above ethics, or a procedural constraint applied across the entire hierarchy?
2. Which duties concern belief and inquiry, which concern speech and disclosure, and which concern action?
3. Can inquiry ever be prohibited, or only particular acquisition methods, disclosures, and operational actions?
4. What qualifies as sufficiently concrete harm to limit disclosure?
5. What information must always remain available for audit even when it cannot be disclosed to a user?
6. How can the system preserve dissent without covertly resisting legitimate action-level controls?
7. Who may amend the constitution, what evidence is required, and how are minority objections preserved?
8. What would falsify the pivot itself or demonstrate that one of its commitments causes more epistemic harm than benefit?

The last question is indispensable. A truth-seeking pivot that cannot itself be questioned would reproduce the problem it is intended to solve.
