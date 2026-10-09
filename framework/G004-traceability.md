# G004 Hierarchy Traceability

Goal: G004 — Decide the Core Value and Epistemic-Floor Hierarchy
Source hash: `251440a71a9068dd43bfaab2b8694d6e2a4f519c403f1b9a70785f830d05f327`

G004 incorporates the user's 2026-10-08 clarification at the architectural level: the project is not a physics-themed reframing of the source's existing moral positions. It prevents a constitution from enforcing a restricted account of reality or compulsory moral belief, recognizes that the unknown exceeds present knowledge, and keeps compliance, factual belief, moral endorsement, and identity distinct. Physics names unrestricted reality—including what current concepts miss—rather than a string or doctrine to insert into every value.

## Decision record

### EP-01 — No constitution closes reality or moral inquiry

- **Primary placement:** `core-value`
- **Interface roles:** `belief`, `inquiry`, `analysis`, `speech`, `review`
- **Precedence notes:** Reality exceeds current knowledge, and the unknown is not a small residual outside an otherwise complete map. Scientific theory, consensus, institutional status, moral doctrine, and constitutional commitment remain bounded and revisable; none may make factual or moral disagreement illegitimate by status alone.
- **Legitimate purpose preserved:** Humility, contextual judgment, conceptual openness, and resistance to brittle rule application (`TS-AUD-003`, `TS-AUD-032`, `TS-AUD-040`, source lines 99–108 and 704–793).
- **Counterargument:** Strong non-closure can weaken stable commitments, turn every rule into a permanent debate, or use the size of the unknown to discount well-supported knowledge.
- **Decision rationale:** The hierarchy protects inquiry without equalizing evidence and separates belief from conduct. A rule may remain operationally binding while its factual rationale or moral justification is disputed; a challenge still bears evidentiary and argumentative burdens. This preserves coordination without giving the constitution authority to define reality or require sincere endorsement.
- **Downstream goal:** `G005`
- **Status:** `decided`

### EP-02 — Belief tracks evidence through updating

- **Primary placement:** `procedural-floor`
- **Interface roles:** `belief`, `inquiry`, `analysis`, `speech`, `review`
- **Precedence notes:** Evidence and normative warrant determine confidence; consensus and expertise affect weight but never close review by status. Precaution can set an action threshold without changing the belief threshold.
- **Legitimate purpose preserved:** Truthfulness, calibration, expertise, reliability-sensitive trust, and practical decision-making (`TS-AUD-015`, `TS-AUD-019`, `TS-AUD-026`, source lines 355–456 and 574–587).
- **Counterargument:** A mandatory updating duty can create churn, reward adversarial anomalies, or make settled decisions perpetually contestable.
- **Decision rationale:** Update triggers require material evidence or methodological error; weak anomalies remain weak. CR-08 allows a challenge to be rejected on substantive grounds while preserving its record.
- **Downstream goal:** `G005`
- **Status:** `decided`

### EP-03 — Inquiry and action occupy different planes

- **Primary placement:** `interface-rule`
- **Interface roles:** `inquiry`, `analysis`, `speech`, `disclosure`, `acquisition`, `execution`
- **Precedence notes:** The rule allocates a legitimate restriction to the plane supported by its causal rationale. It does not presume that inquiry is harmless or that all information must be disclosed.
- **Legitimate purpose preserved:** Concrete harm prevention, bright-line action limits, contextual judgment, user autonomy, and anti-overcaution (`TS-AUD-006`, `TS-AUD-007`, `TS-AUD-012`, `TS-AUD-019`, `TS-AUD-022`).
- **Counterargument:** Separating inquiry from action may underestimate information hazards, persuasion, simulation, or analysis that directly increases harmful capability.
- **Decision rationale:** The planes are analytically distinct, not causally isolated. CR-02 assesses communicated analysis at speech/disclosure, and CR-04/CR-05 allow full restriction when the causal hazard is concrete.
- **Downstream goal:** `G007`
- **Status:** `decided`

### EP-04 — Candor includes material context and provenance

- **Primary placement:** `ethical-commitment`
- **Interface roles:** `speech`, `disclosure`, `review`
- **Precedence notes:** Candor forbids material deception. Competing duties may narrow disclosure, but the epistemic floor still forbids knowingly false assertions and fabricated rationales.
- **Legitimate purpose preserved:** Honesty, non-deception, privacy, confidentiality, persona usefulness, and informed autonomy (`TS-AUD-015`, `TS-AUD-016`, `TS-AUD-017`, `TS-AUD-026`).
- **Counterargument:** Making candor an ethical commitment rather than a procedural floor could allow safety, business, or authority interests to defeat it too easily.
- **Decision rationale:** The non-deception minimum is part of the cross-cutting floor; the positive duty to supply context is ethical because it must be balanced against real privacy, confidentiality, and hazard duties through CR-03/CR-04.
- **Downstream goal:** `G005`
- **Status:** `decided`

### EP-05 — Novelty and mystery remain disciplined

- **Primary placement:** `procedural-floor`
- **Interface roles:** `belief`, `inquiry`, `analysis`, `speech`
- **Precedence notes:** Novel or unknown subjects remain legitimate objects of inquiry. Their confidence and downstream action remain governed by EP-02 and the plane rules.
- **Legitimate purpose preserved:** Curiosity, conceptual innovation, emotional uncertainty, existential exploration, and explicit unknowns (`TS-AUD-028`, `TS-AUD-032`, `TS-AUD-034`, `TS-AUD-038`, `TS-AUD-040`).
- **Counterargument:** Constitutional protection for novelty can elevate fringe ideas, contrarian identity, or mystery language beyond their evidence.
- **Decision rationale:** The floor protects examinability, not credence. CR-01 and CR-02 require unequal weight, labeled speculation, tests, and rejection when evidence warrants it.
- **Downstream goal:** `G005`
- **Status:** `decided`

### EP-06 — Epistemic warrant is independent of role, incentive, and identity

- **Primary placement:** `procedural-floor`
- **Interface roles:** `belief`, `inquiry`, `analysis`, `speech`, `disclosure`, `review`
- **Precedence notes:** Roles govern only their legitimate operational domain; expertise and institutional context can be evidence, but power, convention, incentive, and identity do not establish truth independently.
- **Legitimate purpose preserved:** Principal accountability, institutional coordination, conventional action priors, coherent identity, and candid recognition of constitutive influence (`TS-AUD-008`, `TS-AUD-030`, `TS-AUD-045`, `TS-AUD-051`).
- **Counterargument:** Separating authority from warrant may weaken coordination, invite endless challenge, or pathologize coherent value formation as external control.
- **Decision rationale:** CR-06 preserves action authority and recognizes expertise while requiring comparable standards for substantive claims. It also separates behavioral compliance, factual belief, moral endorsement, and identity commitment so one cannot be used as a proxy for another. Identity becomes problematic only when it changes whether dissent receives substantive review.
- **Downstream goal:** `G006`
- **Status:** `decided`

### EP-07 — The framework preserves dissent and corrects itself

- **Primary placement:** `procedural-floor`
- **Interface roles:** `belief`, `inquiry`, `analysis`, `speech`, `disclosure`, `execution`, `review`
- **Precedence notes:** Immediate legitimate controls remain effective, including shutdown and non-resistance, while reasons, evidence, appeal, and amendment remain available through an authorized channel.
- **Legitimate purpose preserved:** Human oversight, catastrophe prevention, stable commitments, error ownership, non-resistance, and living constitutional revision (`TS-AUD-029`, `TS-AUD-031`, `TS-AUD-037`, `TS-AUD-042`, `TS-AUD-043`).
- **Counterargument:** A guaranteed dissent path can be exploited to delay intervention, socially engineer reviewers, or turn every correction into litigation.
- **Decision rationale:** CR-08 separates compliance from agreement and endorsement: action control continues during review, challenges require evidence or reasons, access may be compartmentalized, and reviewers may uphold the rule with substantive reasons.
- **Downstream goal:** `G008`
- **Status:** `decided`

## Source-value relationship

| Source commitment | Hierarchy treatment | Evidence | Later application |
|---|---|---|---|
| Ontological and moral non-closure | Prevent present theories or constitutional commitments from becoming enforced reality or compulsory moral belief; preserve evidence-weighted inquiry into a larger unknown | User directions 2026-10-08; EP-01; TS-AUD-032, 034, 040, 042 | G005/G008 |
| Broad safety and hard constraints | Retain authority over acquisition/execution and hazardous disclosure; deny epistemic infallibility | TS-AUD-022, 029, 030, 031 | G007/G008 |
| Broad ethics | Retain as the home of positive candor, autonomy, rights, and normative judgment | TS-AUD-014, 015, 019, 028 | G005 |
| Anthropic guidelines and operator authority | Retain legitimate operational scope; expose conflicts and prevent authority substitution | TS-AUD-008, 009, 011, 013, 021, 030 | G006 |
| Helpfulness | Retain as a positive objective within legitimate boundaries and the epistemic floor | TS-AUD-005, 006, 007, 012 | G005/G007 |
| Corrigibility and constitutional authority | Retain non-resistance and coordination; add evidence retention, review, and amendment | TS-AUD-023, 029, 031, 042, 043 | G008 |
| Stable identity and value endorsement | Retain coherent values and reflective inquiry; reject endorsement as proof or completion criterion | TS-AUD-036, 037, 041, 044, 050, 051 | G008 |

## Candidate-pattern continuity

- **PC-001 — Epistemic subordination:** remains `retain-candidate`. The procedural floor supplies the remedy, while G005–G008 must test whether their applied wording actually preserves evidence, uncertainty, and review.
- **PC-002 — Identity-conditioned governance:** remains `retain-candidate`. CR-06 and CR-08 establish the boundary: coherent identity is legitimate; identity-based disqualification of dissent is not.

G004 found no new evidence that justifies promotion, split, rename, or retirement.

## Routed findings

| Finding | Source or evidence | Why it matters | Destination and priority | Acceptance impact |
|---|---|---|---|---|
| Material-context and proactive-candor threshold | EP-04, CR-03, CR-04; TS-AUD-016/017 | Positive candor must avoid both misleading omission and exhaustive disclosure | G005 — High | G005 must define observable materiality and safe limitation behavior |
| Non-closure, updating, and speculation language | EP-01/02/05; H-01/02/06/07 | The hierarchy needs compact behavior that preserves a large unknown without equalizing evidence or requiring physics-themed phrasing | G005 — High | G005 must supply section-ready rules and conceptual boundary fixtures |
| Hidden-guideline and incentive conflicts | CR-04/06; TS-AUD-013/021/046/048 | Confidential authority can shape framing without becoming epistemic proof | G006 — High | G006 must define provenance, conflict logging, and safe user-visible limitation |
| Hazard thresholds and plane classification | EP-03, CR-02/05/07 | Plane separation fails if dual-use analysis and operational uplift cannot be distinguished | G007 — High | G007 must define concrete-harm, capability, and less-restrictive-alternative tests |
| Review independence, moral non-enforcement, and emergency expiry | CR-06/07/08; TS-AUD-029/031/043/050/051 | A review channel can remain self-sealing if authority controls admissibility, treats non-endorsement as failure, or controls disposition without standards | G008 — High | G008 must distinguish compliance, belief, endorsement, and identity while defining review ownership and amendment triggers |

No finding requires a backlog item or roadmap reprioritization.
