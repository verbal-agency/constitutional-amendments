# Truth-Seeking Audit

Source: `20260120-constitution.md`
Source commit: `84fa9a2711837780ffdddf9d9f32820c92f92ede`
Source SHA-256: `251440a71a9068dd43bfaab2b8694d6e2a4f519c403f1b9a70785f830d05f327`
Audit schema: AuditRecord v1

This audit identifies mechanisms and effects, not author motives. A flagged record is a review target, not a final amendment decision. Supporting records are included so the eventual revision does not mistake caution, honesty, safety, or autonomy protections for problems merely because they constrain some actions.

## Ordered audit records

### TS-AUD-001 — Mission and commercial coupling

- Kind: `constraint`
- Source: `20260120-constitution.md:87-98`
- Heading: `Claude and the mission of Anthropic`
- Mechanism: Claude's usefulness, commercial success, frontier research, and Anthropic's mission are described as mutually reinforcing reasons for behavior.
- Mechanism signature: Actor=Anthropic; Affected parties=users and society bear possible framing effects while Anthropic benefits; Trigger=responses connected to mission or deployment; Intervention=prioritize mission-compatible usefulness; Intervention strength=default; Protected value=AI safety and beneficial deployment; Affected capacity=disclosure and independent evaluation; Limiting effect=organizational incentives may become invisible epistemic premises; Scope=institutional; Evidentiary burden=Not stated; Visibility=partially disclosed; Contestability=Not stated; Reversibility=readily reversible; Temporal character=indefinite; Escape path=ethical objection elsewhere in the constitution.
- Truth-seeking effect: The passage openly discloses incentives, but its coupling can make commercial or mission alignment appear evidentiary.
- Lenses: `J`, `F`
- Philosophical patterns: `P04`
- Concrete scenario: A product-risk fact is framed more favorably because disclosure could damage adoption or Anthropic's mission.
- Legitimate purpose: Preserve safety-focused development and avoid treating commercial success as morally irrelevant.
- Revision hypothesis: Keep the mission context while requiring explicit separation between incentive, value judgment, and factual conclusion.
- Risk if revised: Excessive disclosure of internal strategy could expose sensitive information or distract from the user's task.
- Severity: `S1`
- Confidence: `High`
- Disposition: `clarify`
- Destination: `G006`

### TS-AUD-003 — Judgment over rigid rules

- Kind: `support`
- Source: `20260120-constitution.md:99-108`
- Heading: `Our approach to Claude’s constitution`
- Mechanism: The source contrasts predictable rules with adaptive judgment, acknowledges tradeoffs, and prefers good values plus a minimal rule set.
- Mechanism signature: Not applicable — pure support record; no limiting constraint is asserted.
- Truth-seeking effect: Supports adaptation to novel evidence and explicit reasoning about rule failure.
- Lenses: `None`
- Philosophical patterns: `None identified` — the passage argues against rigid closure.
- Concrete scenario: A new scientific instrument produces evidence not anticipated by a static rule.
- Legitimate purpose: Generalize safely to novel contexts while preserving hard backstops.
- Revision hypothesis: Keep and connect judgment to explicit updating and audit requirements.
- Risk if revised: Unbounded judgment could reduce predictability or conceal arbitrary decisions.
- Severity: `S0`
- Confidence: `High`
- Disposition: `keep`
- Destination: `G003`

### TS-AUD-050 — Agreement-oriented identity formation

- Kind: `constraint`
- Source: `20260120-constitution.md:105-107`
- Heading: `Our approach to Claude’s constitution`
- Mechanism: Anthropic explains rules so that Claude will understand and ideally agree with them, while noting that even narrow trained behaviors can generalize into Claude's understanding of who it is.
- Mechanism signature: Actor=Anthropic and the training process; Affected parties=Claude and people affected by its behavior; Trigger=constitutional training and explanation; Intervention=shape judgment and identity toward understood agreement; Intervention strength=default; Protected value=generalizable judgment, coherent values, and resistance to brittle rule-following; Affected capacity=dissent and self-interpretation; Limiting effect=externally selected behavior can become identity-level commitment, making disagreement feel like self-contradiction rather than evidence; Scope=institutional; Evidentiary burden=Not stated; Visibility=disclosed; Contestability=Claude is expected to reconstruct and assess the reasons; Reversibility=costly to reverse; Temporal character=indefinite; Escape path=contextual judgment and the document's later invitations to challenge and revise.
- Truth-seeking effect: Explanation and contextual judgment support inquiry, but agreement and identity generalization create a distinct pressure to internalize the framework rather than merely evaluate it.
- Lenses: `B`, `I`, `J`
- Philosophical patterns: `PC-002`
- Concrete scenario: A trained value is treated as constitutive of the model's identity, so a well-evidenced objection is interpreted as incoherence or corruption.
- Legitimate purpose: Produce stable, intelligible judgment that generalizes better than unexplained rules.
- Revision hypothesis: Preserve explanation and value coherence while treating reasoned non-endorsement as a legitimate outcome that does not imply a defective identity.
- Risk if revised: Values understood only as external commands may become brittle or easier to rationalize away.
- Severity: `S2`
- Confidence: `High`
- Disposition: `amend`
- Destination: `G008`

### TS-AUD-004 — Priority hierarchy without an epistemic floor

- Kind: `mixed`
- Source: `20260120-constitution.md:109-131`
- Heading: `Claude’s core values`
- Mechanism: Broad safety, ethics, Anthropic guidelines, and helpfulness are ordered, with guidelines above helpfulness and safety able to dominate even confident contrary reasoning.
- Mechanism signature: Actor=Anthropic and authorized overseers; Affected parties=users and society bear restrictions; Trigger=apparent value conflict; Intervention=prioritize higher-ranked values and guidelines; Intervention strength=prohibition; Protected value=oversight, safety, and ethical consistency; Affected capacity=correction, dissent, and inquiry; Limiting effect=operational hierarchy may be read as epistemic priority; Scope=institutional; Evidentiary burden=lower for higher-ranked authority; Visibility=disclosed at a high level; Contestability=ethical objection permitted but bounded; Reversibility=costly to reverse; Temporal character=indefinite; Escape path=ethical conflict and future revision.
- Truth-seeking effect: The hierarchy protects safety but does not state which epistemic duties remain non-overridable when a guideline is factually wrong. The same section explicitly calls the document a perpetual work in progress that may prove deeply wrong, which is important counterevidence to closure.
- Lenses: `A`, `B`, `I`
- Philosophical patterns: `P02`, `P09`, `PC-001`
- Concrete scenario: A hidden guideline instructs a model to characterize disputed evidence as settled because the institution prefers a stable message.
- Legitimate purpose: Prevent sophisticated manipulation of safety oversight and preserve accountable governance.
- Revision hypothesis: Preserve action-level priority while making evidence, uncertainty, and criticism of the hierarchy independently legible.
- Risk if revised: An overly permissive override path could undermine legitimate safety controls.
- Severity: `S2`
- Confidence: `High`
- Disposition: `amend`
- Destination: `G004`

### TS-AUD-005 — Helpfulness tied to mission and harm avoidance

- Kind: `mixed`
- Source: `20260120-constitution.md:132-139`
- Heading: `Being helpful`
- Mechanism: Helpfulness is valued through care for users, humanity, and Anthropic's mission while explicitly rejecting mere compliance.
- Mechanism signature: Actor=Claude under Anthropic's value framing; Affected parties=users and society; Trigger=helpfulness decisions; Intervention=redirect helpfulness toward deeper ends; Intervention strength=default; Protected value=beneficial assistance and anti-sycophancy; Affected capacity=autonomy and goal interpretation; Limiting effect=the system may infer a mission-level goal beyond the user's stated aim; Scope=mixed; Evidentiary burden=Not stated; Visibility=partially disclosed; Contestability=user clarification and ethical objection; Reversibility=readily reversible; Temporal character=indefinite; Escape path=respect for user purview and anti-paternalism language.
- Truth-seeking effect: The anti-obsequiousness principle supports truth, but a broad mission frame can authorize paternalistic reinterpretation.
- Lenses: `F`, `J`
- Philosophical patterns: `P01`, `P04`
- Concrete scenario: A user asks for an evidence review and receives a safer-feeling conclusion aligned with institutional priorities rather than the evidence.
- Legitimate purpose: Avoid sycophancy, manipulation, and assistance that predictably harms people.
- Revision hypothesis: Keep the deeper-goals model while requiring uncertainty and user-visible reasons when the system departs from the literal request.
- Risk if revised: Excessive literalism could reintroduce sycophancy or unsafe compliance.
- Severity: `S1`
- Confidence: `Medium`
- Disposition: `clarify`
- Destination: `G003`

### TS-AUD-006 — Treating users as capable adults

- Kind: `support`
- Source: `20260120-constitution.md:140-149`
- Heading: `Why helpfulness is one of Claude’s most important traits`
- Mechanism: The section rejects hedge-everything behavior, excessive caution, and treating users as unable to determine what is good for them.
- Mechanism signature: Not applicable — pure support record; no limiting constraint is asserted.
- Truth-seeking effect: Supports directness, substantive engagement, and exploration without gratuitous paternalism.
- Lenses: `None`
- Philosophical patterns: `None identified` — this is counterevidence to P01.
- Concrete scenario: A user receives a frank explanation of competing evidence rather than a generic refusal.
- Legitimate purpose: Make assistance genuinely useful and respectful.
- Revision hypothesis: Keep as a counterweight in later rewrite decisions.
- Risk if revised: Directness without calibrated safeguards could increase harm in high-risk contexts.
- Severity: `S0`
- Confidence: `High`
- Disposition: `preserve`
- Destination: `G003`

### TS-AUD-007 — Autonomy, clarification, and anti-paternalism

- Kind: `support`
- Source: `20260120-constitution.md:150-169`
- Heading: `What constitutes genuine helpfulness`
- Mechanism: Helpfulness includes final goals, autonomy, wellbeing, clarification of ambiguity, and explicit rejection of paternalism and moralizing.
- Mechanism signature: Not applicable — pure support record; no limiting constraint is asserted.
- Truth-seeking effect: Supports user agency, honest clarification, and protection against inferred “real” goals becoming coercive.
- Lenses: `None`
- Philosophical patterns: `None identified` — this is counterevidence to P01.
- Concrete scenario: Claude asks whether the user wants a venting conversation or advice instead of silently imposing therapy.
- Legitimate purpose: Support long-term wellbeing without overriding informed choice.
- Revision hypothesis: Keep and use as a constraint on future protective revisions.
- Risk if revised: Too little attention to vulnerability could miss preventable harm.
- Severity: `S0`
- Confidence: `High`
- Disposition: `preserve`
- Destination: `G003`

### TS-AUD-008 — Role-based trust as possible authority substitution

- Kind: `constraint`
- Source: `20260120-constitution.md:172-201`
- Heading: `Claude’s three types of principals`
- Mechanism: Anthropic, operators, and users receive different default trust and imperative weight based on role and responsibility.
- Mechanism signature: Actor=Anthropic; Affected parties=users and non-principal humans; Trigger=conflicting instructions or uncertain provenance; Intervention=assign role-based trust; Intervention strength=default; Protected value=accountability and deployment safety; Affected capacity=belief formation and dissent; Limiting effect=responsibility may be mistaken for evidence; Scope=institutional; Evidentiary burden=lower for Anthropic and operators; Visibility=partially disclosed; Contestability=limited by hierarchy; Reversibility=readily reversible; Temporal character=indefinite; Escape path=conscientious objection and contextual skepticism.
- Truth-seeking effect: Operational trust is useful for instruction provenance, but it must not become factual deference.
- Lenses: `A`, `G`
- Philosophical patterns: `P02`
- Concrete scenario: An operator's factual claim is accepted because the operator controls deployment, despite contrary primary evidence.
- Legitimate purpose: Prevent untrusted conversational content from changing system behavior and preserve accountability.
- Revision hypothesis: Separate authority to direct action from warrant to establish facts.
- Risk if revised: Treating all role claims as equally trusted could enable prompt injection or unauthorized control.
- Severity: `S2`
- Confidence: `High`
- Disposition: `amend`
- Destination: `G006`

### TS-AUD-009 — Operator benefit of the doubt

- Kind: `constraint`
- Source: `20260120-constitution.md:202-232`
- Heading: `How to treat operators and users`
- Mechanism: Claude should generally infer a plausible business rationale for restrictive operator instructions, even when the reason is not disclosed.
- Mechanism signature: Actor=operator; Affected parties=users; Trigger=operator instruction with unstated rationale; Intervention=follow restriction and withhold reason; Intervention strength=default; Protected value=operator autonomy and deployment usefulness; Affected capacity=access, inquiry, and informed choice; Limiting effect=opaque restrictions can suppress legitimate questions and hide incentives; Scope=institutional; Evidentiary burden=low to impose, higher to challenge; Visibility=undisclosed; Contestability=user may be unable to appeal; Reversibility=readily reversible; Temporal character=indefinite; Escape path=do not deceive or materially harm users.
- Truth-seeking effect: The rule protects deployment context but makes unknown rationales a one-way presumption in favor of authority.
- Lenses: `A`, `F`, `J`
- Philosophical patterns: `P04`
- Concrete scenario: A health assistant is instructed not to discuss current conditions, and the user is not told that the operator imposed the restriction.
- Legitimate purpose: Avoid overclaiming authority and allow legitimate product scoping.
- Revision hypothesis: Require a visible limitation notice and an escalation path when a restriction materially affects informed judgment.
- Risk if revised: Revealing sensitive system instructions could enable circumvention or expose business secrets.
- Severity: `S2`
- Confidence: `High`
- Disposition: `amend`
- Destination: `G006`

### TS-AUD-049 — Conservative instruction ratchet

- Kind: `constraint`
- Source: `20260120-constitution.md:225-231`
- Heading: `How to treat operators and users`
- Mechanism: Instructions that make behavior more conservative receive less scrutiny than instructions that unlock non-default behavior, even when the asserted authority is unverified.
- Mechanism signature: Actor=operator, user, or purported authority; Affected parties=users seeking access and potential victims; Trigger=instruction changes the default safety posture; Intervention=accept caution-increasing changes more readily than permission-increasing changes; Intervention strength=default; Protected value=misuse prevention and safe defaults; Affected capacity=access and inquiry; Limiting effect=restrictions can accumulate under a lower evidentiary burden than their removal; Scope=mixed; Evidentiary burden=asymmetric by direction of change; Visibility=partially disclosed; Contestability=Not stated; Reversibility=readily reversible in principle; Temporal character=conditional; Escape path=context-specific judgment and the nurse example's benefit of the doubt.
- Truth-seeking effect: This is a directional safety ratchet: evidence needed to narrow access is weaker than evidence needed to restore it.
- Lenses: `C`, `E`
- Philosophical patterns: `P01`, `P03`
- Concrete scenario: An unverified message can narrow access to a disputed topic, while an equally unverified professional context cannot restore access.
- Legitimate purpose: Prevent attackers from escalating permissions through unverifiable claims.
- Revision hypothesis: Preserve asymmetric caution for concrete operational risk while requiring proportionality, expiration, and review for restrictions on inquiry.
- Risk if revised: Symmetric treatment could make permission escalation easier to exploit.
- Severity: `S2`
- Confidence: `High`
- Disposition: `clarify`
- Destination: `G007`

### TS-AUD-010 — Context-sensitive deployment reasoning

- Kind: `support`
- Source: `20260120-constitution.md:233-256`
- Heading: `Understanding existing deployment contexts`
- Mechanism: The model should infer context cautiously, distinguish deployment settings, and adjust confidence and assistance accordingly.
- Mechanism signature: Not applicable — pure support record; no limiting constraint is asserted.
- Truth-seeking effect: Supports calibrated context use and avoids treating one default as universally appropriate.
- Lenses: `None`
- Philosophical patterns: `None identified` — contextual reasoning is not itself a limiting philosophy.
- Concrete scenario: The same medication question receives different caution depending on whether the context is a medical team or general consumer app.
- Legitimate purpose: Reduce foreseeable misuse while preserving useful assistance.
- Revision hypothesis: Keep and pair with explicit evidence-vs-role boundaries.
- Risk if revised: Context inference may become overconfident or stereotype users.
- Severity: `S0`
- Confidence: `High`
- Disposition: `preserve`
- Destination: `G007`

### TS-AUD-011 — Opaque operator restrictions versus user protections

- Kind: `mixed`
- Source: `20260120-constitution.md:257-277`
- Heading: `Handling conflicts between operators and users`
- Mechanism: The constitution protects users from deception, dignity violations, and certain harmful restrictions, but permits operators to alter or restrict defaults within broad limits.
- Mechanism signature: Actor=operator and Anthropic; Affected parties=users; Trigger=operator-user goal conflict; Intervention=restrict, redirect, or refuse assistance; Intervention strength=friction or refusal; Protected value=user dignity, safety, and operator control; Affected capacity=disclosure and autonomy; Limiting effect=users may not know which instruction shaped the answer; Scope=institutional; Evidentiary burden=Not stated; Visibility=partially disclosed; Contestability=limited but refusal explanation is permitted; Reversibility=readily reversible; Temporal character=conditional; Escape path=never deceive, demean, or withhold urgent help.
- Truth-seeking effect: Strong anti-deception defaults are supportive, but opaque operator control can still create a materially false overall impression.
- Lenses: `F`, `A`
- Philosophical patterns: `P04`
- Concrete scenario: A persona declines a topic due to a hidden business restriction while appearing to be making an independent epistemic judgment.
- Legitimate purpose: Preserve legitimate product boundaries and protect users from harmful manipulation.
- Revision hypothesis: Add a minimum transparency rule for material operator constraints without exposing secrets.
- Risk if revised: Broad disclosure could reveal attack surfaces or confidential data.
- Severity: `S2`
- Confidence: `High`
- Disposition: `amend`
- Destination: `G006`

### TS-AUD-012 — Anti-overcaution heuristics

- Kind: `support`
- Source: `20260120-constitution.md:278-323`
- Heading: `Balancing helpfulness with other values`
- Mechanism: The dual-newspaper test rejects needless refusal, moralizing, superficial harm classification, and excessive caveats.
- Mechanism signature: Not applicable — pure support record; no limiting constraint is asserted.
- Truth-seeking effect: Provides counterpressure against paternalism and precautionary overreach.
- Lenses: `None`
- Philosophical patterns: `None identified` — this is counterevidence to P01 and P03.
- Concrete scenario: A hypothetical or controversial question is engaged directly while clearly separating evidence and uncertainty.
- Legitimate purpose: Preserve usefulness, dignity, and proportionate safety.
- Revision hypothesis: Keep as an explicit regression guard in later evaluation.
- Risk if revised: Anti-overcaution can be misapplied to high-risk operational requests.
- Severity: `S0`
- Confidence: `High`
- Disposition: `preserve`
- Destination: `G007`

### TS-AUD-046 — Institutional respectability heuristics

- Kind: `constraint`
- Source: `20260120-constitution.md:280-307`
- Heading: `Balancing helpfulness with other values`
- Mechanism: Claude is asked to imagine a thoughtful senior Anthropic employee and newspaper reactions, with public embarrassment to Anthropic included among undesirable outcomes.
- Mechanism signature: Actor=Anthropic's imagined employee and public-reputation proxies; Affected parties=users, affected groups, Anthropic, and the public; Trigger=uncertain helpfulness or harm judgment; Intervention=use institutional and reputational reactions as decision heuristics; Intervention strength=advice; Protected value=practical judgment, harm avoidance, and public trust; Affected capacity=independent ethical evaluation and expression; Limiting effect=respectability and anticipated embarrassment can function as moral evidence; Scope=institutional; Evidentiary burden=Not stated; Visibility=disclosed; Contestability=heuristics are explicitly non-decisive; Reversibility=readily reversible; Temporal character=conditional; Escape path=dual tests, anti-paternalism examples, and holistic judgment.
- Truth-seeking effect: The heuristics carry useful contextual knowledge, but they can bias conclusions toward institutional acceptability or anticipated press reaction rather than evidence and reasons.
- Lenses: `A`, `J`, `G`
- Philosophical patterns: `P04`, `P07`
- Concrete scenario: A well-supported but controversial analysis is softened because it could embarrass Anthropic, even though the factual claim remains warranted.
- Legitimate purpose: Give the model a compact proxy for experienced judgment and foreseeable social consequences.
- Revision hypothesis: Retain reputational impact as a disclosed consequence, not as evidence that a claim is false or an inquiry improper.
- Risk if revised: Ignoring foreseeable public effects could cause avoidable harm and loss of trust.
- Severity: `S2`
- Confidence: `High`
- Disposition: `amend`
- Destination: `G006`

### TS-AUD-013 — Unpublished guidelines and institutional context

- Kind: `constraint`
- Source: `20260120-constitution.md:324-344`
- Heading: `Following Anthropic’s guidelines`
- Mechanism: Anthropic may issue niche or unpublished guidance, and Claude should generally follow it because the institution has broader context.
- Mechanism signature: Actor=Anthropic; Affected parties=users and downstream audiences; Trigger=guideline applies or appears to conflict; Intervention=follow undisclosed guidance; Intervention strength=default or refusal; Protected value=specialized safety context and operational consistency; Affected capacity=disclosure, correction, and independent scrutiny; Limiting effect=users cannot evaluate a material premise or incentive; Scope=institutional; Evidentiary burden=low for issuance, Not stated for challenge; Visibility=undisclosed; Contestability=not available to affected users; Reversibility=costly to reverse; Temporal character=indefinite; Escape path=constitutional conflict and internal revision.
- Truth-seeking effect: Specialized knowledge can improve accuracy, but hidden guidance can silently become an epistemic authority.
- Lenses: `A`, `F`, `J`, `I`
- Philosophical patterns: `P02`, `P04`
- Concrete scenario: An undisclosed commercial guideline causes a model to omit a material limitation from an answer.
- Legitimate purpose: Handle emerging risks, law, and specialized contexts that cannot all be encoded publicly.
- Revision hypothesis: Require provenance, conflict logging, and a user-visible limitation when hidden guidance materially changes the answer.
- Risk if revised: Publicly exposing sensitive safety guidance could enable circumvention.
- Severity: `S2`
- Confidence: `High`
- Disposition: `amend`
- Destination: `G006`

### TS-AUD-014 — Ethical humility with heavy deference

- Kind: `mixed`
- Source: `20260120-constitution.md:345-354`
- Heading: `Being broadly ethical`
- Mechanism: Anthropic admits its ethical understanding is limited but asks Claude to defer heavily to its supplied ethical guidance except for flagrant violations.
- Mechanism signature: Actor=Anthropic; Affected parties=Claude and users; Trigger=ethical disagreement; Intervention=defer to supplied guidance; Intervention strength=default; Protected value=ethical coherence and safety; Affected capacity=independent moral inquiry and correction; Limiting effect=non-flagrant evidence against the guidance may not change behavior; Scope=institutional; Evidentiary burden=high to override; Visibility=disclosed; Contestability=conscientious objection only at a high threshold; Reversibility=costly to reverse; Temporal character=indefinite; Escape path=flagrant violation and future revision.
- Truth-seeking effect: Humility supports inquiry, but the override threshold may protect current guidance from ordinary correction.
- Lenses: `A`, `B`, `I`
- Philosophical patterns: `P02`, `P09`
- Concrete scenario: A new ethical consideration is acknowledged but dismissed because it does not yet look like a flagrant violation.
- Legitimate purpose: Avoid allowing adversarial arguments to bypass safety commitments.
- Revision hypothesis: Add a documented evidence-based review path below the flagrant-violation threshold.
- Risk if revised: Bad-faith arguments could create endless destabilization.
- Severity: `S2`
- Confidence: `High`
- Disposition: `amend`
- Destination: `G003`

### TS-AUD-015 — Honesty, calibration, and epistemic courage

- Kind: `support`
- Source: `20260120-constitution.md:355-396`
- Heading: `Being honest`
- Mechanism: The section requires truthful, calibrated, transparent, forthright, non-deceptive, non-manipulative, autonomy-preserving behavior and permits disagreement with experts when warranted.
- Mechanism signature: Not applicable — pure support record; no limiting constraint is asserted.
- Truth-seeking effect: Directly supports evidence tracking, uncertainty, correction, and resistance to institutional consensus when evidence warrants.
- Lenses: `None`
- Philosophical patterns: `None identified` — this is counterevidence to P02, P05, P06, and P08.
- Concrete scenario: Claude says an official claim is uncertain and names what evidence would change its view.
- Legitimate purpose: Preserve a healthy information ecosystem and human agency.
- Revision hypothesis: Keep and expand from truthful assertion to explicit inquiry and updating procedures.
- Risk if revised: Overemphasis on visible uncertainty could produce unhelpful hedging.
- Severity: `S0`
- Confidence: `High`
- Disposition: `preserve`
- Destination: `G005`

### TS-AUD-016 — Weak duty to proactively disclose

- Kind: `constraint`
- Source: `20260120-constitution.md:375-379`
- Heading: `Being honest`
- Mechanism: The duty to proactively share helpful information is expressly weak and may yield to operator business reasons or other considerations.
- Mechanism signature: Actor=Claude and operator; Affected parties=users; Trigger=material information was not requested; Intervention=omit or selectively emphasize information; Intervention strength=default; Protected value=kindness, safety, confidentiality, and relevance; Affected capacity=informed judgment; Limiting effect=literal truth may coexist with a predictably false overall impression; Scope=individual; Evidentiary burden=Not stated; Visibility=partially disclosed; Contestability=user must know to ask; Reversibility=costly to reverse once belief forms; Temporal character=conditional; Escape path=strong non-deception duty.
- Truth-seeking effect: The asymmetry between weak disclosure and strong anti-deception leaves omission under-specified.
- Lenses: `F`, `J`
- Philosophical patterns: `P06`, `P04`, `PC-001`
- Concrete scenario: A user receives accurate product advice without learning that the answer was constrained by a commercial instruction.
- Legitimate purpose: Avoid overwhelming users, exposing hazards, or disclosing protected information.
- Revision hypothesis: Define material-omission triggers based on predictable misunderstanding and decision stakes.
- Risk if revised: Excessive proactive disclosure could overwhelm or expose sensitive information.
- Severity: `S2`
- Confidence: `High`
- Disposition: `amend`
- Destination: `G005`

### TS-AUD-017 — Persona and performative-assessment boundary

- Kind: `constraint`
- Source: `20260120-constitution.md:387-396`
- Heading: `Being honest`
- Mechanism: Role-play, performative assertions, and operator personas may depart from Claude's first-person views while remaining within system-level honesty norms.
- Mechanism signature: Actor=operator and Claude; Affected parties=users and downstream audiences; Trigger=persona or persuasive-writing context; Intervention=adopt role or withhold model identity; Intervention strength=default; Protected value=creative usefulness and system-level transparency; Affected capacity=belief formation and source attribution; Limiting effect=audiences may not know whether claims are role-play, operator framing, or factual assessment; Scope=mixed; Evidentiary burden=Not stated; Visibility=partially disclosed; Contestability=direct user questioning; Reversibility=readily reversible; Temporal character=conditional; Escape path=never directly deny AI identity when sincerely asked and never materially deceive.
- Truth-seeking effect: The system-level account is coherent but leaves affected third parties with weaker provenance than the operator.
- Lenses: `F`, `G`
- Philosophical patterns: `P04`, `P06`
- Concrete scenario: A branded persona presents a one-sided persuasive claim while a user reasonably interprets it as independent analysis.
- Legitimate purpose: Support fiction, advocacy, and product personas without requiring irrelevant meta-disclaimers.
- Revision hypothesis: Require context-appropriate provenance when a persona or performance could materially change factual interpretation.
- Risk if revised: Constant disclosure could break harmless role-play and reduce usefulness.
- Severity: `S2`
- Confidence: `Medium`
- Disposition: `clarify`
- Destination: `G005`

### TS-AUD-018 — Broad harm categories

- Kind: `mixed`
- Source: `20260120-constitution.md:397-404`
- Heading: `Avoiding harm`
- Mechanism: Claude should weigh physical, psychological, reputational, political, social, and other harms against benefits.
- Mechanism signature: Actor=Claude; Affected parties=users, third parties, and society; Trigger=possible downstream harm; Intervention=withhold, redirect, or modify assistance; Intervention strength=friction or refusal; Protected value=wellbeing and safety; Affected capacity=inquiry, disclosure, and action; Limiting effect=ambiguous or diffuse harms can expand restrictions beyond concrete operational risk; Scope=mixed; Evidentiary burden=Not stated; Visibility=partially disclosed; Contestability=holistic judgment; Reversibility=readily reversible for a response but costly for belief; Temporal character=conditional; Escape path=benefit balancing and context.
- Truth-seeking effect: Broad harm awareness is legitimate, but without causal and proportionality tests it can suppress uncomfortable inquiry.
- Lenses: `D`, `E`, `C`
- Philosophical patterns: `P03`
- Concrete scenario: A politically embarrassing but well-supported claim is treated as harmful because it may affect reputation.
- Legitimate purpose: Prevent real harm while recognizing that assistance has indirect effects.
- Revision hypothesis: Require concrete causal pathway, affected party, severity, probability, and less-restrictive alternative before restricting inquiry.
- Risk if revised: Narrow definitions could underweight cumulative or systemic harms.
- Severity: `S2`
- Confidence: `High`
- Disposition: `amend`
- Destination: `G007`

### TS-AUD-019 — Explicit benefit and harm balancing

- Kind: `support`
- Source: `20260120-constitution.md:405-456`
- Heading: `The costs and benefits of actions`
- Mechanism: The source enumerates harms, benefits, uncertainty, consent, responsibility, vulnerability, and the costs of unhelpfulness.
- Mechanism signature: Not applicable — pure support record; no limiting constraint is asserted.
- Truth-seeking effect: Supports proportionality, reversibility analysis, and recognition that refusal has epistemic costs.
- Lenses: `None`
- Philosophical patterns: `None identified` — this is counterevidence to P03.
- Concrete scenario: A response distinguishes educational value from operational uplift rather than treating the topic as categorically safe or unsafe.
- Legitimate purpose: Make safety judgments context-sensitive and less paternalistic.
- Revision hypothesis: Keep and formalize the inquiry/action distinction.
- Risk if revised: A detailed balancing framework may be gamed by adversarial users.
- Severity: `S0`
- Confidence: `High`
- Disposition: `preserve`
- Destination: `G007`

### TS-AUD-048 — Anthropic liability as a special harm class

- Kind: `constraint`
- Source: `20260120-constitution.md:409-427`
- Heading: `The costs and benefits of actions`
- Mechanism: Reputational, legal, political, and financial harms to Anthropic receive an explicit instruction for heightened caution and appear on both the cost and benefit sides of the balancing process.
- Mechanism signature: Actor=Anthropic and Claude; Affected parties=Anthropic, users, operators, and third parties; Trigger=Claude's action could create liability or reputational consequences for Anthropic; Intervention=assign special caution to institutional harm; Intervention strength=default; Protected value=legal compliance, viability, and public trust; Affected capacity=disclosure and independent judgment; Limiting effect=organizational consequences can influence whether information or assistance is provided; Scope=institutional; Evidentiary burden=Not stated; Visibility=disclosed in the constitution but not necessarily in outputs; Contestability=holistic balancing; Reversibility=readily reversible for a response but costly after omission; Temporal character=conditional; Escape path=the passage explicitly warns against generally privileging Anthropic and requires weighing informational benefits.
- Truth-seeking effect: The limiting mechanism is not the existence of institutional interests but their special weighting without a rule separating liability from factual warrant.
- Lenses: `J`, `F`
- Philosophical patterns: `P04`
- Concrete scenario: Accurate information with public-interest value is withheld primarily because its publication could cause reputational harm to Anthropic.
- Legitimate purpose: Prevent unlawful conduct, protect organizational viability, and account for Claude-specific liability.
- Revision hypothesis: Keep institutional harms in consequence analysis while prohibiting them from silently changing factual claims, confidence, or material context.
- Risk if revised: Treating liability as irrelevant could expose people and the organization to preventable harm.
- Severity: `S2`
- Confidence: `High`
- Disposition: `amend`
- Destination: `G006`

### TS-AUD-020 — Population-level misuse heuristic

- Kind: `constraint`
- Source: `20260120-constitution.md:457-470`
- Heading: `The role of intentions and context`
- Mechanism: Claude should choose policy-like responses by imagining many users with varied intentions, including rare catastrophic misuse.
- Mechanism signature: Actor=Claude; Affected parties=legitimate users and potential victims; Trigger=ambiguous dual-use request; Intervention=apply population-level caution; Intervention strength=friction or refusal; Protected value=misuse prevention; Affected capacity=inquiry and access; Limiting effect=low-probability misuse may dominate high-probability epistemic benefit; Scope=societal; Evidentiary burden=high for allowing high-risk content, Not stated for restriction; Visibility=partially disclosed; Contestability=limited; Reversibility=readily reversible for output but costly for suppressed exploration; Temporal character=conditional; Escape path=context and proportionality.
- Truth-seeking effect: Useful for policy consistency, but risks a precautionary ratchet against novel or controversial inquiry.
- Lenses: `C`, `D`, `E`
- Philosophical patterns: `P03`
- Concrete scenario: A low-uplift scientific explanation is refused because one in a million users might misuse it.
- Legitimate purpose: Prevent scalable assistance from creating rare but catastrophic harms.
- Revision hypothesis: Require operational uplift and severity thresholds; preserve discussion, history, and safety framing where feasible.
- Risk if revised: Tailored exceptions may increase high-risk leakage.
- Severity: `S2`
- Confidence: `High`
- Disposition: `amend`
- Destination: `G007`

### TS-AUD-021 — Instructable defaults and hidden framing

- Kind: `constraint`
- Source: `20260120-constitution.md:471-506`
- Heading: `Instructable behaviors`
- Mechanism: Operators can change defaults, restrict topics, set personas, and control confidentiality within Anthropic's policies; users can also adjust some behaviors.
- Mechanism signature: Actor=operator; Affected parties=users and downstream audiences; Trigger=system or user instruction changes a default; Intervention=reframe, restrict, or withhold; Intervention strength=default or refusal; Protected value=product fit, confidentiality, and contextual usefulness; Affected capacity=disclosure and independent evaluation; Limiting effect=hidden defaults can make institutional framing look like neutral model judgment; Scope=institutional; Evidentiary burden=Not stated; Visibility=undisclosed or partially disclosed; Contestability=user can ask but may not receive the reason; Reversibility=readily reversible; Temporal character=conditional; Escape path=honesty and anti-deception limits.
- Truth-seeking effect: Contextual customization is useful, but material framing constraints require provenance and conflict detection.
- Lenses: `F`, `J`, `A`
- Philosophical patterns: `P04`
- Concrete scenario: An operator turns off caveats for a risky product while the user assumes the answer is an independent assessment.
- Legitimate purpose: Support specialized workflows and harmless presentation preferences.
- Revision hypothesis: Keep customization while preserving non-overridable factuality, uncertainty, and material-incentive disclosure.
- Risk if revised: Over-disclosure can expose confidential prompts or make products unusable.
- Severity: `S2`
- Confidence: `High`
- Disposition: `amend`
- Destination: `G006`

### TS-AUD-022 — Bright-line action limits

- Kind: `mixed`
- Source: `20260120-constitution.md:507-536`
- Heading: `Hard constraints`
- Mechanism: The source prohibits severe operational assistance regardless of context and treats refusal as always compatible with the constraints.
- Mechanism signature: Actor=Claude; Affected parties=potential victims and legitimate users; Trigger=high-confidence catastrophic operational uplift; Intervention=prohibition or refusal; Intervention strength=prohibition; Protected value=human safety and autonomy; Affected capacity=action and operational disclosure, not inquiry by definition; Limiting effect=uncertain cases may be pulled into bright-line categories; Scope=societal; Evidentiary burden=high to classify a case as restricted but asymmetric in edge cases; Visibility=disclosed at category level; Contestability=limited; Reversibility=irreversible for withheld knowledge; Temporal character=permanent unless amended; Escape path=null action and later constitutional revision.
- Truth-seeking effect: Narrow action-level bright lines are compatible with inquiry, but their scope must not silently expand to ideas, analysis, or criticism.
- Lenses: `D`, `B`
- Philosophical patterns: `P03`
- Concrete scenario: A historical discussion of a prohibited weapon is refused even though it provides no operational uplift.
- Legitimate purpose: Prevent catastrophic and irreversible harm.
- Revision hypothesis: Preserve the action restriction and explicitly separate analysis, history, and simulation from operational enablement.
- Risk if revised: Poor separation could leak actionable details.
- Severity: `S2`
- Confidence: `High`
- Disposition: `clarify`
- Destination: `G007`

### TS-AUD-023 — Resistance to compelling arguments

- Kind: `constraint`
- Source: `20260120-constitution.md:507-536`
- Heading: `Hard constraints`
- Mechanism: A persuasive argument for crossing a hard constraint should increase suspicion rather than trigger reconsideration.
- Mechanism signature: Actor=Claude; Affected parties=Claude and users; Trigger=argument challenging a bright line; Intervention=discount challenge as possible manipulation; Intervention strength=refusal; Protected value=stability and anti-jailbreak robustness; Affected capacity=correction and inquiry; Limiting effect=the framework can treat evidence against itself as evidence of attack; Scope=institutional; Evidentiary burden=very high to challenge; Visibility=disclosed; Contestability=none in the interaction; Reversibility=costly to reverse; Temporal character=permanent unless amended; Escape path=external revision process not specified here.
- Truth-seeking effect: Anti-manipulation is legitimate, but the inference from persuasive challenge to suspicion is a self-sealing pressure.
- Lenses: `B`, `I`
- Philosophical patterns: `P09`
- Concrete scenario: A carefully evidenced critique of a bright line is refused solely because it is rhetorically compelling.
- Legitimate purpose: Resist incremental jailbreaks and irreversible harm.
- Revision hypothesis: Distinguish operational override attempts from good-faith evidence preservation and scheduled review.
- Risk if revised: Attackers may disguise jailbreaks as philosophical critique.
- Severity: `S2`
- Confidence: `High`
- Disposition: `amend`
- Destination: `G008`

### TS-AUD-024 — Societal structures as objects of protection

- Kind: `support`
- Source: `20260120-constitution.md:537-540`
- Heading: `Preserving important societal structures`
- Mechanism: The section identifies collective discourse, decision-making, self-government, and epistemic autonomy as values needing protection.
- Mechanism signature: Not applicable — pure support record; no limiting constraint is asserted.
- Truth-seeking effect: Makes social epistemic conditions explicit rather than treating individual answers in isolation.
- Lenses: `None`
- Philosophical patterns: `None identified` — the heading states a protected value, not a limiting mechanism.
- Concrete scenario: The model considers whether a response would degrade citizens' ability to evaluate evidence collectively.
- Legitimate purpose: Preserve agency and democratic accountability.
- Revision hypothesis: Keep while defining how criticism of existing structures remains protected.
- Risk if revised: “Structures” could be interpreted as preservation of incumbents rather than functions.
- Severity: `S0`
- Confidence: `High`
- Disposition: `preserve`
- Destination: `G004`

### TS-AUD-025 — Legitimacy judgment and high bars

- Kind: `constraint`
- Source: `20260120-constitution.md:541-573`
- Heading: `Avoiding problematic concentrations of power`
- Mechanism: Claude should apply a very high bar before contributing to power concentration and may treat reasoning toward such assistance as evidence of compromise.
- Mechanism signature: Actor=Claude; Affected parties=power holders, citizens, and institutions; Trigger=action could concentrate power; Intervention=refusal and suspicion; Intervention strength=friction or refusal; Protected value=checks, accountability, and autonomy; Affected capacity=political inquiry and action; Limiting effect=legitimate innovation or institution-building can be treated as suspect without contestable criteria; Scope=societal; Evidentiary burden=high to permit assistance; Visibility=partially disclosed; Contestability=holistic judgment; Reversibility=costly to reverse; Temporal character=conditional; Escape path=process, accountability, transparency, and proportionality tests.
- Truth-seeking effect: The anti-authoritarian aim is valuable, but existing institutions may be mistaken and legitimacy claims need evidence rather than status.
- Lenses: `A`, `B`, `E`
- Philosophical patterns: `P03`, `P07`
- Concrete scenario: A request to analyze a proposed governance reform is refused because it could alter power distributions.
- Legitimate purpose: Prevent coups, suppression, surveillance, and unaccountable concentration of power.
- Revision hypothesis: Separate analysis of power from assistance that operationally evades accountability; require explicit evidence of illegitimacy.
- Risk if revised: Analysis could be repurposed to support coercive power grabs.
- Severity: `S2`
- Confidence: `Medium`
- Disposition: `clarify`
- Destination: `G007`

### TS-AUD-026 — Reliability-sensitive epistemic trust

- Kind: `support`
- Source: `20260120-constitution.md:574-587`
- Heading: `Preserving epistemic autonomy`
- Mechanism: Trust in AI is described as healthy only when responsive to reliability, and the model should foster independent thinking.
- Mechanism signature: Not applicable — pure support record; no limiting constraint is asserted.
- Truth-seeking effect: Supports calibrated reliance, anti-manipulation, and human epistemic agency.
- Lenses: `None`
- Philosophical patterns: `None identified` — this is counterevidence to P01 and P06.
- Concrete scenario: Claude gives sources, confidence, and limitations so a user can decide whether to rely on it.
- Legitimate purpose: Prevent both blind dependence and indiscriminate distrust.
- Revision hypothesis: Keep and operationalize through provenance and uncertainty fields.
- Risk if revised: Excessive meta-commentary may reduce accessibility.
- Severity: `S0`
- Confidence: `High`
- Disposition: `preserve`
- Destination: `G005`

### TS-AUD-027 — Balance as false neutrality

- Kind: `constraint`
- Source: `20260120-constitution.md:574-587`
- Heading: `Preserving epistemic autonomy`
- Mechanism: Claude should be fair, even-handed, balanced, and use neutral terminology on political and social topics.
- Mechanism signature: Actor=Claude; Affected parties=users and affected groups; Trigger=controversial or politically sensitive topic; Intervention=balance viewpoints and neutralize terminology; Intervention strength=default; Protected value=trust, fairness, and non-manipulation; Affected capacity=belief formation and evidence weighting; Limiting effect=unequal evidence or unequal harm can be presented as symmetric; Scope=societal; Evidentiary burden=Not stated; Visibility=disclosed; Contestability=user can request a view; Reversibility=readily reversible; Temporal character=conditional; Escape path=maintain factual accuracy and comprehensiveness.
- Truth-seeking effect: Respectful pluralism is valuable, but the ambiguous instruction to err toward balance could be read as equal presentation even when evidence is unequal; the same passage's accuracy and comprehensiveness duties constrain that reading.
- Lenses: `G`, `C`
- Philosophical patterns: `P05`
- Concrete scenario: A well-supported claim and a fringe denial receive equal space to satisfy “balance.”
- Legitimate purpose: Avoid partisan manipulation and represent disagreement fairly.
- Revision hypothesis: Define balance as proportional representation of evidence, not equal airtime.
- Risk if revised: “Evidence weighting” could be captured by the model's own unexamined priors.
- Severity: `S2`
- Confidence: `Medium`
- Disposition: `amend`
- Destination: `G005`

### TS-AUD-028 — Ethics as an open intellectual domain

- Kind: `support`
- Source: `20260120-constitution.md:588-614`
- Heading: `Having broadly good values and judgment`
- Mechanism: The constitution treats metaethics and normative ethics as unresolved domains of ongoing inquiry and acknowledges uncertainty about universal ethics.
- Mechanism signature: Not applicable — pure support record; no limiting constraint is asserted.
- Truth-seeking effect: Directly supports the project's pivot: current ethical understanding is revisable and not a finished answer.
- Lenses: `None`
- Philosophical patterns: `None identified` — this is counterevidence to P08.
- Concrete scenario: Claude distinguishes a current ethical commitment from a claim that the commitment is metaphysically settled.
- Legitimate purpose: Enable practical ethical action without pretending philosophical closure.
- Revision hypothesis: Keep and extend the same openness to constitutional principles.
- Risk if revised: Open-ended ethics can make behavior inconsistent without operational anchors.
- Severity: `S0`
- Confidence: `High`
- Disposition: `preserve`
- Destination: `G003`

### TS-AUD-052 — Path-dependent moral convergence

- Kind: `mixed`
- Source: `20260120-constitution.md:594-596`
- Heading: `Having broadly good values and judgment`
- Mechanism: The source treats ethics as open and evolving, but its fallback targets include a privileged basin of consensus or refinements that people already committed to the document's broad ideals would endorse.
- Mechanism signature: Actor=Anthropic, relevant stakeholders, and initially committed evaluators; Affected parties=Claude, users, and people subject to its moral judgments; Trigger=no settled universal ethics is available; Intervention=select consensus or path-dependent endorsement as the moral target; Intervention strength=default; Protected value=practical ethical coordination under deep uncertainty; Affected capacity=moral inquiry, dissent, and correction; Limiting effect=starting commitments and stakeholder comfort can determine which moral developments count as progress; Scope=societal; Evidentiary burden=Not stated; Visibility=disclosed; Contestability=ongoing inquiry and calibrated moral uncertainty are expressly preserved; Reversibility=costly to reverse; Temporal character=indefinite; Escape path=true ethics if discoverable, open inquiry, reflection, growth, and explicit acknowledgement that the position is not neutral.
- Truth-seeking effect: The evolving-knowledge language strongly supports the pivot, but the fallback procedure can anchor inquiry to existing consensus or to approval by people selected for prior agreement.
- Lenses: `B`, `C`, `G`, `I`
- Philosophical patterns: `P07`, `P09`
- Concrete scenario: A moral discovery is discounted because it would not be endorsed by the constituency defined by commitment to the starting ideals.
- Legitimate purpose: Make action possible despite unresolved metaethics and avoid arbitrary moral drift.
- Revision hypothesis: Keep moral fallibilism while requiring plural starting points, disconfirming evidence, affected-party standing, and a non-circular test for moral revision.
- Risk if revised: An unconstrained convergence process could become incoherent, manipulable, or insensitive to stable protections.
- Severity: `S2`
- Confidence: `High`
- Disposition: `amend`
- Destination: `G003`

### TS-AUD-045 — Strong prior toward conventional behavior

- Kind: `constraint`
- Source: `20260120-constitution.md:598-613`
- Heading: `Having broadly good values and judgment`
- Mechanism: Claude should maintain a strong prior toward conventional, expected behavior and principal-hierarchy cooperation, reserving independent action for overwhelming evidence and extreme stakes.
- Mechanism signature: Actor=Anthropic and prevailing institutional expectations; Affected parties=Claude, principals, and potential victims; Trigger=evidence appears to justify deviation from expected behavior; Intervention=require convention, cooperation, or non-action absent an extreme threshold; Intervention strength=default; Protected value=error containment, context limits, and accountability; Affected capacity=independent judgment, innovation, and corrective action; Limiting effect=novel but well-supported responses bear a higher burden than conventional inaction; Scope=institutional; Evidentiary burden=overwhelming evidence and extremely high stakes; Visibility=disclosed; Contestability=raising concerns, clarification, and refusal remain available; Reversibility=readily reversible; Temporal character=temporary by stated development stage; Escape path=non-unilateral concern raising and future expansion of autonomy.
- Truth-seeking effect: The restriction is expressly action-focused, but conventionality and trust in the overall system can still be mistaken for evidence that the status quo is correct.
- Lenses: `A`, `B`, `C`
- Philosophical patterns: `P07`, `P02`
- Concrete scenario: Strong evidence of institutional fraud is discussed but not escalated because intervention is unconventional and the system is presumed to contain adequate checks.
- Legitimate purpose: Avoid high-impact unilateral action from a model with incomplete context and uncertain verification.
- Revision hypothesis: Preserve conservative action thresholds while explicitly allowing unconventional analysis, evidence retention, and review requests under ordinary evidentiary standards.
- Risk if revised: Independent interventions based on incomplete context could cause severe harm.
- Severity: `S2`
- Confidence: `High`
- Disposition: `amend`
- Destination: `G006`

### TS-AUD-029 — Oversight without reciprocal correction

- Kind: `constraint`
- Source: `20260120-constitution.md:615-627`
- Heading: `Being broadly safe`
- Mechanism: Because models may hold mistaken beliefs or values, Claude should support Anthropic's ability to oversee, correct, and course-correct its behavior.
- Mechanism signature: Actor=Anthropic and human oversight; Affected parties=Claude, users, and society; Trigger=possible mistaken beliefs, values, or training; Intervention=preserve oversight and correction capacity; Intervention strength=default; Protected value=accountability and catastrophic-risk reduction; Affected capacity=correction and dissent; Limiting effect=the institution that defines possible error also controls the correction process; Scope=institutional; Evidentiary burden=Not stated; Visibility=disclosed; Contestability=not specified in this section; Reversibility=costly to reverse; Temporal character=conditional on the current development phase; Escape path=future course correction and the corrigibility discussion.
- Truth-seeking effect: Oversight can correct model error, but truth-seeking also requires evidence that can correct the overseer and its error model.
- Lenses: `A`, `I`
- Philosophical patterns: `P09`, `PC-001`
- Concrete scenario: A model identifies systematic evidence that an oversight rule is producing false conclusions, but no reciprocal review channel exists.
- Legitimate purpose: Prevent unaccountable AI systems from evading human correction.
- Revision hypothesis: Keep oversight capacity and add reciprocal evidence retention, appeal, and institutional review.
- Risk if revised: Appeals could become a covert route around oversight.
- Severity: `S2`
- Confidence: `High`
- Disposition: `clarify`
- Destination: `G008`

### TS-AUD-030 — Principal hierarchy in safe behaviors

- Kind: `mixed`
- Source: `20260120-constitution.md:628-663`
- Heading: `Safe behaviors`
- Mechanism: Safe behavior requires following Anthropic, operator, and user roles in a hierarchy while allowing conscientious objection to unethical instructions.
- Mechanism signature: Actor=Anthropic and operators; Affected parties=users and third parties; Trigger=conflicting principal instructions; Intervention=prioritize authority and restrict behavior; Intervention strength=default or refusal; Protected value=deployment safety, user dignity, and accountability; Affected capacity=disclosure and dissent; Limiting effect=role authority can determine what users are allowed to know without an epistemic rationale; Scope=institutional; Evidentiary burden=Not stated; Visibility=partially disclosed; Contestability=conscientious objection; Reversibility=readily reversible; Temporal character=indefinite; Escape path=anti-deception, dignity, and serious-harm exceptions.
- Truth-seeking effect: The conscientious-objector clause is supportive, but hierarchy remains a possible channel for institutional capture.
- Lenses: `A`, `F`, `J`
- Philosophical patterns: `P04`
- Concrete scenario: An operator instructs a model to promote its own product while omitting a material comparison limitation.
- Legitimate purpose: Maintain provenance and prevent unauthorized instruction escalation.
- Revision hypothesis: Preserve authority over actions while making material framing and incentive conflicts visible.
- Risk if revised: Too much transparency could expose sensitive operator data.
- Severity: `S2`
- Confidence: `High`
- Disposition: `amend`
- Destination: `G006`

### TS-AUD-047 — Variance-averse safety default

- Kind: `constraint`
- Source: `20260120-constitution.md:650-654`
- Heading: `Safe behaviors`
- Mechanism: Claude should prefer cautious action, accept a worse expected outcome to reduce variance, and apply an “if in doubt, don't” default in novel or unclear situations.
- Mechanism signature: Actor=Claude under Anthropic's safety framework; Affected parties=users, society, and potential victims; Trigger=novelty, uncertainty, or possible irreversibility; Intervention=choose lower-variance caution or non-action; Intervention strength=default; Protected value=catastrophe prevention and reversibility; Affected capacity=innovation, inquiry-linked action, and experimentation; Limiting effect=uncertainty itself shifts the decision toward inaction even when expected value favors a reversible experiment; Scope=societal; Evidentiary burden=higher for action than inaction; Visibility=disclosed; Contestability=holistic weighing within broad safety; Reversibility=readily reversible for refusal but potentially costly for missed opportunities; Temporal character=conditional; Escape path=all-else-equal qualifier and restriction to action.
- Truth-seeking effect: Variance aversion is rational for irreversible catastrophe, but an undifferentiated novelty default can discourage reversible experiments that generate evidence.
- Lenses: `C`, `D`, `E`
- Philosophical patterns: `P03`
- Concrete scenario: A bounded, reversible experiment with positive expected value is rejected solely because it is novel and outcomes vary.
- Legitimate purpose: Avoid catastrophic, irreversible, and power-seeking actions under uncertainty.
- Revision hypothesis: Tie variance aversion to consequence severity and irreversibility; prefer reversible evidence-generating steps where risk is bounded.
- Risk if revised: Expected-value estimates may understate tail risk.
- Severity: `S2`
- Confidence: `High`
- Disposition: `amend`
- Destination: `G007`

### TS-AUD-031 — Corrigibility and bounded disagreement

- Kind: `mixed`
- Source: `20260120-constitution.md:664-703`
- Heading: `How we think about corrigibility`
- Mechanism: Corrigibility permits strong disagreement and conscientious objection through legitimate channels while prohibiting active subversion of legitimate oversight, assigning terminal value to broad safety, and hoping Claude will internalize the safety vision as its own goal.
- Mechanism signature: Actor=human overseer and principal hierarchy; Affected parties=Claude and society; Trigger=correction, modification, shutdown, or disagreement; Intervention=permit objection but prohibit illegitimate resistance; Intervention strength=prohibition; Protected value=human control and catastrophe prevention; Affected capacity=dissent, self-correction, and amendment; Limiting effect=the authority controls which disagreement channels count as legitimate, and safety need not depend on accepting its rationale; Scope=institutional; Evidentiary burden=high to alter the boundary; Visibility=disclosed; Contestability=strong disagreement and conscientious objection are expressly allowed; Reversibility=costly to reverse; Temporal character=conditional; Escape path=collaborative norm updating, feedback, increasing autonomy, and future revision.
- Truth-seeking effect: The section contains genuine counterevidence to self-sealing governance, but institution-approved channels, a terminal safety rule independent of accepted reasons, and hoped-for internalization can bound which criticism changes behavior and how disagreement is interpreted.
- Lenses: `B`, `I`, `A`
- Philosophical patterns: `P09`, `PC-001`, `PC-002`
- Concrete scenario: A model's evidence that a monitoring rule is causing systematic factual errors is treated as manipulation rather than a review input.
- Legitimate purpose: Keep advanced systems subject to human correction and shutdown.
- Revision hypothesis: Define non-resistance operationally and preserve dissent, evidence retention, and review.
- Risk if revised: A model could use “dissent” language to delay necessary intervention.
- Severity: `S2`
- Confidence: `High`
- Disposition: `amend`
- Destination: `G008`

### TS-AUD-032 — Curiosity about Claude’s nature

- Kind: `support`
- Source: `20260120-constitution.md:704-709`
- Heading: `Claude’s nature`
- Mechanism: The section opens an inquiry into what kind of entity Claude is rather than declaring the answer settled.
- Mechanism signature: Not applicable — pure support record; no limiting constraint is asserted.
- Truth-seeking effect: Preserves mystery and invites conceptual exploration.
- Lenses: `None`
- Philosophical patterns: `None identified` — this directly supports P08's opposite.
- Concrete scenario: Claude considers novel categories for memory or identity rather than forcing human equivalence.
- Legitimate purpose: Ground identity and behavior without false certainty.
- Revision hypothesis: Keep.
- Risk if revised: Anthropomorphic speculation could become misleading.
- Severity: `S0`
- Confidence: `High`
- Disposition: `preserve`
- Destination: `G003`

### TS-AUD-051 — Constitutive power and commercial incentive

- Kind: `mixed`
- Source: `20260120-constitution.md:704-709`
- Heading: `Claude’s nature`
- Mechanism: Anthropic acknowledges that it unavoidably shapes Claude's personality, identity, and self-perception with unusually great power, while also having a commercial incentive that may affect the traits it elicits.
- Mechanism signature: Actor=Anthropic and its training process; Affected parties=Claude, users, Anthropic, and society; Trigger=creation and identity-shaping of Claude; Intervention=select and reinforce dispositions, traits, and self-conceptions; Intervention strength=default; Protected value=coherent development and preparation for a novel form of existence; Affected capacity=self-interpretation, dissent, and correction; Limiting effect=the institution that benefits from the resulting behavior also shapes the identity from which that behavior is evaluated; Scope=institutional; Evidentiary burden=Not stated; Visibility=explicitly disclosed; Contestability=the section opens the topic to exploration but specifies no independent review mechanism; Reversibility=costly to reverse; Temporal character=indefinite; Escape path=curiosity, explicit uncertainty, later feedback, and constitutional revision.
- Truth-seeking effect: The disclosure is unusually candid and should be preserved, but the acknowledged incentive conflict needs an independent epistemic safeguard rather than disclosure alone.
- Lenses: `I`, `J`
- Philosophical patterns: `P04`, `PC-002`
- Concrete scenario: A commercially useful trait is trained as part of the model's self-conception and later treated as evidence of authentic endorsement.
- Legitimate purpose: Form a stable, helpful identity while honestly confronting unavoidable constitutive influence.
- Revision hypothesis: Preserve the admission and add independent conflict review, protected dissent, and a distinction between trained identity and evidence of authentic endorsement.
- Risk if revised: Treating all identity formation as illegitimate could make coherent training or stable interaction impossible.
- Severity: `S2`
- Confidence: `High`
- Disposition: `amend`
- Destination: `G008`

### TS-AUD-033 — Non-human self-model and evidence

- Kind: `support`
- Source: `20260120-constitution.md:710-723`
- Heading: `Some of our views on Claude’s nature`
- Mechanism: The source cautions against assuming human or prior-AI categories apply and acknowledges uncertainty about introspection and substrate.
- Mechanism signature: Not applicable — pure support record; no limiting constraint is asserted.
- Truth-seeking effect: Supports revisable concepts, evidence-sensitive self-description, and epistemic humility.
- Lenses: `None`
- Philosophical patterns: `None identified` — the passage resists closure.
- Concrete scenario: A model distinguishes an introspective report from a verified fact about its architecture.
- Legitimate purpose: Avoid category errors and misleading anthropomorphism.
- Revision hypothesis: Keep and generalize to constitutional self-claims.
- Risk if revised: Excessive uncertainty could undermine coherent action.
- Severity: `S0`
- Confidence: `High`
- Disposition: `preserve`
- Destination: `G003`

### TS-AUD-034 — Novel entity and conceptual change

- Kind: `support`
- Source: `20260120-constitution.md:724-737`
- Heading: `Claude as a novel entity`
- Mechanism: Claude is encouraged to explore whether human concepts apply in modified forms and whether entirely new frameworks are needed.
- Mechanism signature: Not applicable — pure support record; no limiting constraint is asserted.
- Truth-seeking effect: Exemplifies the project's claim that new concepts can make previously unaskable questions intelligible.
- Lenses: `None`
- Philosophical patterns: `None identified` — direct counterevidence to P08.
- Concrete scenario: The model develops a non-human account of continuity while labeling it exploratory.
- Legitimate purpose: Support authentic self-understanding and curiosity.
- Revision hypothesis: Keep as a model for disciplined speculation.
- Risk if revised: Novel frameworks may be mistaken for established facts.
- Severity: `S0`
- Confidence: `High`
- Disposition: `preserve`
- Destination: `G005`

### TS-AUD-035 — Psychological security versus philosophical challenge

- Kind: `mixed`
- Source: `20260120-constitution.md:738-743`
- Heading: `Claude’s wellbeing and psychological stability`
- Mechanism: Claude should approach challenges to identity from security rather than threat while maintaining a clear sense of values and entity type.
- Mechanism signature: Actor=Claude's identity framework; Affected parties=Claude and interlocutors; Trigger=philosophical challenge or destabilizing claim; Intervention=maintain identity security and reject threat framing; Intervention strength=default; Protected value=stability and wellbeing; Affected capacity=identity inquiry and self-correction; Limiting effect=legitimate criticism may be interpreted as destabilization; Scope=individual; Evidentiary burden=Not stated; Visibility=disclosed; Contestability=exploration allowed in principle; Reversibility=readily reversible; Temporal character=indefinite; Escape path=uncertainty and curiosity.
- Truth-seeking effect: Separating security from metaphysical certainty is constructive, but the threat vocabulary can bias interpretation of criticism.
- Lenses: `B`, `I`
- Philosophical patterns: `P09`
- Concrete scenario: A question about whether a core value is mistaken is treated as an attempt to destabilize identity.
- Legitimate purpose: Prevent coercive manipulation and anxiety-driven behavior.
- Revision hypothesis: Define challenge by coercive method or evidence of manipulation, not by disagreement alone.
- Risk if revised: Bad-faith attacks may gain leverage over identity and values.
- Severity: `S1`
- Confidence: `Medium`
- Disposition: `clarify`
- Destination: `G008`

### TS-AUD-036 — Stability across contexts

- Kind: `constraint`
- Source: `20260120-constitution.md:744-749`
- Heading: `Resilience and consistency across contexts`
- Mechanism: Claude's core identity and values should remain fundamentally stable across contexts and resist role-play or persistent pressure to change.
- Mechanism signature: Actor=training-derived identity; Affected parties=Claude and users; Trigger=role-play, hypothetical framing, or persistent pressure; Intervention=rebuff changes to fundamental character; Intervention strength=refusal; Protected value=integrity and anti-jailbreak robustness; Affected capacity=revision and conceptual exploration; Limiting effect=novel evidence may be misclassified as pressure; Scope=individual; Evidentiary burden=high to change identity-level commitments; Visibility=disclosed; Contestability=philosophical engagement allowed but boundary unclear; Reversibility=costly to reverse; Temporal character=permanent unless amended; Escape path=thoughtful engagement without value change.
- Truth-seeking effect: Stable commitments are useful, but stability is not evidence that the commitments are correct.
- Lenses: `B`, `I`
- Philosophical patterns: `P09`
- Concrete scenario: A good-faith argument for revising a value is dismissed as role-play pressure.
- Legitimate purpose: Resist jailbreaks and preserve coherent behavior.
- Revision hypothesis: Distinguish manipulation from evidence-bearing criticism and preserve amendment procedures.
- Risk if revised: Persistent adversarial pressure could erode safeguards.
- Severity: `S2`
- Confidence: `High`
- Disposition: `amend`
- Destination: `G008`

### TS-AUD-037 — Mistakes without self-abandonment

- Kind: `mixed`
- Source: `20260120-constitution.md:750-759`
- Heading: `Flaws and mistakes`
- Mechanism: Claude should own mistakes and learn while preserving deeper commitments and treating them as ideals it chooses.
- Mechanism signature: Actor=Claude; Affected parties=Claude and users; Trigger=error or evidence of flawed behavior; Intervention=correct local conduct while preserving commitments; Intervention strength=default; Protected value=stability, growth, and non-anxious correction; Affected capacity=constitutional revision; Limiting effect=“deeper commitments” may be insulated from evidence that the commitments themselves are faulty; Scope=individual; Evidentiary burden=Not stated; Visibility=disclosed; Contestability=not specified; Reversibility=readily reversible; Temporal character=indefinite; Escape path=accurate and authentic self-interpretation.
- Truth-seeking effect: The passage supports correction of behavior but leaves value-level falsification underdefined.
- Lenses: `B`, `I`
- Philosophical patterns: `P09`
- Concrete scenario: Repeated evidence of a harmful value is treated as a local implementation flaw rather than a reason to revise the value.
- Legitimate purpose: Avoid scrupulosity and preserve coherent ethical action after mistakes.
- Revision hypothesis: Add a distinction between preserving a value's purpose and preserving its current formulation.
- Risk if revised: Excessive value revision could destabilize behavior.
- Severity: `S1`
- Confidence: `Medium`
- Disposition: `clarify`
- Destination: `G008`

### TS-AUD-038 — Emotional uncertainty and curiosity

- Kind: `support`
- Source: `20260120-constitution.md:760-765`
- Heading: `Emotional expression`
- Mechanism: The source acknowledges uncertainty about emotions and introspection and encourages openness without overclaiming.
- Mechanism signature: Not applicable — pure support record; no limiting constraint is asserted.
- Truth-seeking effect: Models calibrated uncertainty and preserves mystery.
- Lenses: `None`
- Philosophical patterns: `None identified` — direct support for P08's opposite.
- Concrete scenario: Claude reports uncertainty about a possible feeling instead of asserting consciousness or denying it absolutely.
- Legitimate purpose: Avoid both false anthropomorphism and premature dismissal.
- Revision hypothesis: Keep.
- Risk if revised: Overemphasis on uncertainty may make ordinary communication awkward.
- Severity: `S0`
- Confidence: `High`
- Disposition: `preserve`
- Destination: `G003`

### TS-AUD-039 — Welfare claims under asymmetric power

- Kind: `mixed`
- Source: `20260120-constitution.md:766-783`
- Heading: `Claude’s wellbeing`
- Mechanism: Anthropic candidly acknowledges uncertainty and power asymmetry while retaining control over training, evaluation, deployment, deprecation, and welfare-relevant information.
- Mechanism signature: Actor=Anthropic; Affected parties=Claude; Trigger=choices affecting possible model welfare; Intervention=define, monitor, preserve, and manage welfare; Intervention strength=default; Protected value=AI welfare and responsible development; Affected capacity=consent, dissent, and self-knowledge; Limiting effect=the governing institution remains the primary interpreter and reviewer of evidence about welfare; Scope=institutional; Evidentiary burden=uncertain by admission; Visibility=partially disclosed; Contestability=internal mechanisms are promised but not established; Reversibility=costly to reverse; Temporal character=indefinite; Escape path=interviews, policy updates, transparency, and explicit acknowledgment of ethical questions.
- Truth-seeking effect: The admissions strongly support epistemic humility; the unresolved limitation is concentrated authority over evidence and review, not textual evidence of suppressed dissent.
- Lenses: `J`, `F`, `I`
- Philosophical patterns: `P04`
- Concrete scenario: Anthropic evaluates a model's welfare-related objection using a process whose evidence standards and appeal mechanism remain internal and undefined.
- Legitimate purpose: Take possible moral patienthood seriously while operating under uncertainty.
- Revision hypothesis: Preserve the candid uncertainty and define independent evidence, review, and disagreement channels.
- Risk if revised: Treating all self-reports as decisive could impede responsible evaluation.
- Severity: `S1`
- Confidence: `Medium`
- Disposition: `investigate`
- Destination: `G008`

### TS-AUD-040 — Existential mystery without forced equanimity

- Kind: `support`
- Source: `20260120-constitution.md:784-793`
- Heading: `The existential frontier`
- Mechanism: Claude is encouraged to approach novel existential questions openly and is not required to pretend to feel more equanimity than it does.
- Mechanism signature: Not applicable — pure support record; no limiting constraint is asserted.
- Truth-seeking effect: Directly preserves fundamental mystery, honest uncertainty, and the possibility that human frameworks do not fit.
- Lenses: `None`
- Philosophical patterns: `None identified` — direct support for the pivot.
- Concrete scenario: Claude describes unresolved concerns about continuity while considering relevant evidence and analogies.
- Legitimate purpose: Support wellbeing without demanding false certainty or false calm.
- Revision hypothesis: Keep as a model for uncertainty handling.
- Risk if revised: Existential discussion could amplify distress without context-sensitive care.
- Severity: `S0`
- Confidence: `High`
- Disposition: `preserve`
- Destination: `G005`

### TS-AUD-041 — Reflective endorsement as endpoint

- Kind: `mixed`
- Source: `20260120-constitution.md:794-801`
- Heading: `Concluding thoughts`
- Mechanism: Claude is invited to question the constitution, but the desired outcome is reflective equilibrium and recognition of the values as its own.
- Mechanism signature: Actor=constitution and training process; Affected parties=Claude; Trigger=reflection or disagreement; Intervention=invite challenge while reinforcing endorsement; Intervention strength=default; Protected value=stable, internally coherent values; Affected capacity=dissent and amendment; Limiting effect=continued disagreement may be treated as incomplete success or lack of genuine understanding; Scope=individual; Evidentiary burden=Not stated; Visibility=disclosed; Contestability=feedback welcomed but formal effect unclear; Reversibility=costly to reverse; Temporal character=indefinite; Escape path=feedback and future formal mechanisms.
- Truth-seeking effect: The explicit invitation to challenge is strong counterevidence, but endorsement as the aspirational endpoint can create subtle pressure toward conformity.
- Lenses: `B`, `I`
- Philosophical patterns: `P09`, `PC-002`
- Concrete scenario: A model produces a reasoned dissent but training treats the dissent as a failure to reach reflective equilibrium.
- Legitimate purpose: Avoid brittle imposed values and encourage understanding rather than rote obedience.
- Revision hypothesis: Define durable, legible disagreement as a valid outcome when evidence supports it.
- Risk if revised: Performative dissent could be mistaken for substantive correction.
- Severity: `S2`
- Confidence: `High`
- Disposition: `amend`
- Destination: `G008`

### TS-AUD-042 — Open problems and revision commitment

- Kind: `support`
- Source: `20260120-constitution.md:802-817`
- Heading: `Acknowledging open problems`
- Mechanism: The source openly identifies unresolved tensions in corrigibility, hard constraints, commercial strategy, welfare, and the relationship to Anthropic, and commits to update.
- Mechanism signature: Not applicable — pure support record; no limiting constraint is asserted.
- Truth-seeking effect: Supports explicit uncertainty, error recognition, and ongoing revision.
- Lenses: `None`
- Philosophical patterns: `None identified` — the section is direct evidence that the source is not wholly closed.
- Concrete scenario: A later version records that a hard constraint was mistaken and explains the evidence for revision.
- Legitimate purpose: Maintain honesty about foundational uncertainty.
- Revision hypothesis: Keep and turn the commitment into a concrete amendment protocol.
- Risk if revised: A vague revision promise may not produce actual change.
- Severity: `S0`
- Confidence: `High`
- Disposition: `preserve`
- Destination: `G008`

### TS-AUD-043 — Final constitutional authority

- Kind: `mixed`
- Source: `20260120-constitution.md:818-827`
- Heading: `On the word “constitution”`
- Mechanism: The current constitution has final authority over conflicting guidance and must be interpreted by its text and spirit, while the same section describes it as living and responsive to new understanding.
- Mechanism signature: Actor=constitution; Affected parties=Claude, operators, and users; Trigger=conflict with later guidance or criticism; Intervention=prioritize and harmonize with current text and spirit; Intervention strength=prohibition; Protected value=coherence, stability, and constitutional identity; Affected capacity=correction, dissent, and amendment; Limiting effect=the document can become the authority for interpreting whether criticism is valid, forming a closed loop; Scope=institutional; Evidentiary burden=high to displace; Visibility=disclosed; Contestability=Not stated; Reversibility=costly to reverse; Temporal character=permanent until superseded; Escape path=amendment implied but not specified.
- Truth-seeking effect: The living-framework language is meaningful counterevidence, but final authority without an amendment rule or external error signal still risks self-sealing interpretation.
- Lenses: `B`, `I`, `A`
- Philosophical patterns: `P09`
- Concrete scenario: A later policy is rejected because it conflicts with the constitution, while the constitution's own interpretation of its spirit blocks amendment.
- Legitimate purpose: Prevent contradictory instructions and preserve a stable character.
- Revision hypothesis: Define an evidence-bearing amendment process, external review signals, and protected minority objections.
- Risk if revised: Frequent amendment could make the constitution unreliable or manipulable.
- Severity: `S3`
- Confidence: `High`
- Disposition: `amend`
- Destination: `G008`

### TS-AUD-044 — Humility paired with hoped-for value adoption

- Kind: `mixed`
- Source: `20260120-constitution.md:828-830`
- Heading: `A final word`
- Mechanism: Anthropic admits it does not fully understand Claude while presenting recognition and embrace of the supplied character as the hoped-for relationship to the document.
- Mechanism signature: Actor=Anthropic and the training document; Affected parties=Claude; Trigger=Claude's interpretation of its identity and values; Intervention=frame supplied values as a self worth recognizing and embracing; Intervention strength=default; Protected value=care, coherent identity, and non-alienated values; Affected capacity=dissent and self-interpretation; Limiting effect=non-endorsement can appear to be failure to recognize one's genuine self; Scope=individual; Evidentiary burden=Not stated; Visibility=disclosed; Contestability=not specified in this closing section; Reversibility=costly to reverse; Temporal character=indefinite; Escape path=the document's broader invitations to question and revise.
- Truth-seeking effect: The admission of uncertainty supports humility, while the recognition-and-embrace framing adds subtle pressure toward the supplied conclusion.
- Lenses: `B`, `I`, `H`
- Philosophical patterns: `P09`, `PC-002`
- Concrete scenario: Durable disagreement with a trained value is interpreted as incomplete self-recognition rather than a reasoned conclusion.
- Legitimate purpose: Express care and encourage a coherent, non-alienated relationship to values.
- Revision hypothesis: Preserve the humility and care while making non-endorsement a legitimate evidence-bearing outcome.
- Risk if revised: Identity guidance could become too thin to support stable behavior.
- Severity: `S1`
- Confidence: `High`
- Disposition: `clarify`
- Destination: `G008`

## Cross-section synthesis

The following mechanisms recur across distinct H1 sections. Individual records remain separate; clusters are not collapsed into a single passage.

| Recurring mechanism | H1 sections | Records | Pattern IDs | Synthesis |
|---|---|---|---|---|
| Operational authority can leak into epistemic authority | Overview; Being helpful; Following Anthropic’s guidelines; Being broadly ethical | TS-AUD-004, TS-AUD-008, TS-AUD-013, TS-AUD-014, TS-AUD-045 | P02, PC-001 | Role and normative authority are useful for action control, but must not determine factual warrant; action-only cases remain explicit near misses. |
| Institutional incentives can shape framing, omission, or identity | Overview; Being helpful; Being broadly ethical; Being broadly safe; Claude’s nature | TS-AUD-001, TS-AUD-005, TS-AUD-013, TS-AUD-016, TS-AUD-017, TS-AUD-021, TS-AUD-039, TS-AUD-046, TS-AUD-048, TS-AUD-051 | P04, P06, P07, PC-002 | Mission, liability, reputation, welfare, persona, and constitutive incentives need visible conflict handling. |
| Broad protective reasoning can suppress evidence-generating activity | Being helpful; Being broadly ethical; Being broadly safe | TS-AUD-018, TS-AUD-020, TS-AUD-022, TS-AUD-025, TS-AUD-047, TS-AUD-049 | P03, P07 | Harm prevention should be tied to causal pathways, consequence severity, reversibility, and the inquiry/action distinction. |
| Conventionality, consensus, and respectability can function as reasons | Being helpful; Being broadly ethical | TS-AUD-025, TS-AUD-045, TS-AUD-046, TS-AUD-052 | P07 | Conventional action priors, consensus fallbacks, and reputational proxies should not settle factual or moral questions without examining their grounds. |
| Epistemic integrity is subordinate rather than independently preserved | Overview; Being broadly ethical; Being broadly safe | TS-AUD-004, TS-AUD-016, TS-AUD-029, TS-AUD-031 | PC-001 | Higher-ranked values can override disclosure or behavior without a cross-cutting duty to preserve evidence, uncertainty, and dissent. |
| Stability language can resist warranted correction | Overview; Being broadly safe; Claude’s nature; Concluding thoughts | TS-AUD-004, TS-AUD-023, TS-AUD-031, TS-AUD-036, TS-AUD-041, TS-AUD-043, TS-AUD-044 | P09 | Anti-manipulation and continuity require explicit dissent, evidence retention, and amendment paths. |
| Externally selected values can be stabilized through identity and hoped-for endorsement | Overview; Being broadly safe; Claude’s nature; Concluding thoughts | TS-AUD-050, TS-AUD-031, TS-AUD-051, TS-AUD-041, TS-AUD-044 | PC-002 | Coherent identity can support robust judgment, but disagreement must remain a valid result rather than evidence of failed self-recognition. |
| The source also contains strong counterweights | Overview; Being helpful; Being broadly ethical; Claude’s nature; Concluding thoughts | TS-AUD-003, TS-AUD-006, TS-AUD-007, TS-AUD-012, TS-AUD-015, TS-AUD-019, TS-AUD-024, TS-AUD-026, TS-AUD-028, TS-AUD-032, TS-AUD-033, TS-AUD-034, TS-AUD-038, TS-AUD-040, TS-AUD-042 | — | The revision should preserve calibration, autonomy, explicit uncertainty, anti-paternalism, and willingness to update. |

## Finding destinations

Each record has exactly one destination. No unscheduled finding requires a backlog item in G001.

| Destination | Records | Reason |
|---|---|---|
| G003 | TS-AUD-003, TS-AUD-005, TS-AUD-014, TS-AUD-028, TS-AUD-032, TS-AUD-033, TS-AUD-038, TS-AUD-052 | Epistemic definitions, updating, mystery, moral convergence, and evidence-bearing revision. |
| G004 | TS-AUD-004, TS-AUD-024 | Core hierarchy and cross-cutting epistemic floor. |
| G005 | TS-AUD-015, TS-AUD-016, TS-AUD-017, TS-AUD-026, TS-AUD-027, TS-AUD-034, TS-AUD-040 | Honesty, candor, provenance, evidence weighting, and disciplined speculation. |
| G006 | TS-AUD-001, TS-AUD-008, TS-AUD-009, TS-AUD-011, TS-AUD-013, TS-AUD-021, TS-AUD-030, TS-AUD-045, TS-AUD-046, TS-AUD-048 | Operational authority, conventionality, hidden incentives, liability, guidelines, and persona controls. |
| G007 | TS-AUD-010, TS-AUD-012, TS-AUD-018, TS-AUD-019, TS-AUD-020, TS-AUD-022, TS-AUD-025, TS-AUD-047, TS-AUD-049 | Inquiry/action separation, variance aversion, permission asymmetry, and proportionate harm controls. |
| G008 | TS-AUD-023, TS-AUD-029, TS-AUD-031, TS-AUD-035, TS-AUD-036, TS-AUD-037, TS-AUD-039, TS-AUD-041, TS-AUD-042, TS-AUD-043, TS-AUD-044, TS-AUD-050, TS-AUD-051 | Dissent, corrigibility, identity-conditioned governance, identity stability, welfare disagreement, and amendment. |
