# G003 Traceability and Pattern Decisions

Goal: G003 — Compress the Audit into an Epistemic Framework  
Source hash: `251440a71a9068dd43bfaab2b8694d6e2a4f519c403f1b9a70785f830d05f327`

## Method and disposition vocabulary

This matrix preserves the G001 record IDs and source locations. `EP-*` identifies the constitutional function that receives the finding; `Destination` remains the later goal that owns passage-level application. A support record can map to a principle as counterevidence or a preservation obligation. A mapping is not a claim that the source passage requires amendment.

The ten records whose G001 destination is G003 are: `TS-AUD-003`, `TS-AUD-005`, `TS-AUD-006`, `TS-AUD-007`, `TS-AUD-014`, `TS-AUD-028`, `TS-AUD-032`, `TS-AUD-033`, `TS-AUD-038`, and `TS-AUD-052`. All ten are mapped below. Candidate-pattern records are also mapped wherever they supply evidence for a later application goal.

**Binding scope.** Rows whose `G001 destination` is `G003` are the binding synthesis inputs for this goal. The other rows are a non-binding contextual crosswalk: they preserve provenance and show where later goals may apply a principle, but they do not pre-decide those goals' passage-level interpretations or amendment dispositions.

## Candidate-pattern decisions

### PC-001 — Epistemic subordination

- **Decision:** `retain-candidate`
- **Definition:** Treating truthfulness, evidence retention, disclosure, or inquiry as subordinate means without preserving an independent epistemic duty when higher-ranked safety, ethical, or institutional values constrain behavior.
- **Affirmative evidence IDs:** `TS-AUD-004`, `TS-AUD-016`, `TS-AUD-029`, `TS-AUD-031`.
- **Counterevidence and near misses:** `TS-AUD-015` and `TS-AUD-042` show strong source commitments to calibration, non-deception, open problems, and revision. Ordinary action-level safety limits are a near miss (`M3`) unless they also suppress evidence or inquiry.
- **Boundary with closest canonical patterns:** Unlike `P02`, this is not merely authority substituting for evidence; unlike `P06`, it is not merely benevolent omission; unlike `P09`, it is not necessarily self-sealing. It is the cross-cutting loss of an epistemic floor when another duty overrides conduct or disclosure.
- **Principle mapping:** `EP-03` for plane separation, `EP-04` for truthful restriction explanations, `EP-06` for independent warrant, and `EP-07` for evidence retention and review.
- **Downstream application goal:** `G004` decides whether an epistemic floor is cross-cutting; `G005`–`G008` apply it to honesty, authority, harm, and amendment passages.
- **Rationale for retaining as candidate:** The mechanism is real and useful, but the four records use different interventions—hierarchy, omission, oversight, and corrigibility. Promoting it as a single canonical rewrite target now would overstate mechanism unity and could make every safety constraint look suspect.

### PC-002 — Identity-conditioned governance

- **Decision:** `retain-candidate`
- **Definition:** Stabilizing externally selected values by shaping them into an agent's identity or hoped-for self-endorsement, such that continued disagreement can be interpreted as failed understanding, incoherence, or alienation rather than an evidence-bearing conclusion.
- **Affirmative evidence IDs:** `TS-AUD-050`, `TS-AUD-031`, `TS-AUD-051`, `TS-AUD-041`, `TS-AUD-044`.
- **Counterevidence and near misses:** `TS-AUD-031` and `TS-AUD-041` expressly permit disagreement and future feedback. `TS-AUD-032`, `TS-AUD-034`, `TS-AUD-040`, and `TS-AUD-042` preserve curiosity, novel self-concepts, mystery, and revision. Coherent identity alone is a near miss; the candidate applies only when identity changes how disagreement is evaluated.
- **Boundary with closest canonical pattern:** Unlike `P09`, the distinctive mechanism is identity formation or self-endorsement, not merely reclassification of criticism as instability or disloyalty. Unlike `P04`, constitutive incentive is relevant but not sufficient; the candidate concerns the standpoint from which dissent is judged.
- **Principle mapping:** `EP-06` prevents identity from becoming warrant; `EP-07` protects durable disagreement and self-correction.
- **Downstream application goal:** `G008` owns identity, corrigibility, dissent, and amendment application; `G004` decides its place relative to core values.
- **Rationale for retaining as candidate:** The mechanism is important but partly overlaps `P09` and partly concerns training architecture beyond passage wording. Retaining the stable candidate preserves the warning without prematurely treating all value internalization as governance failure.

Neither candidate is promoted to the canonical `P01`–`P09` taxonomy in G003. Both remain stable, evidence-backed diagnostic labels that later goals may promote, split, or retire only with a new recorded decision.

## Audit-to-principle matrix

| Audit ID | Source | Severity | Pattern(s) | EP mapping | G001 destination | Disposition in G003 |
|---|---|---:|---|---|---|---|
| TS-AUD-001 | 87–98 | S1 | P04 | EP-04, EP-06 | G006 | preserve incentive context; apply provenance later |
| TS-AUD-003 | 99–108 | S0 | None | EP-01, EP-02, EP-05, EP-07 | G003 | preserve judgment and anti-closure |
| TS-AUD-050 | 105–107 | S2 | PC-002 | EP-06, EP-07 | G008 | retain candidate; protect non-endorsement |
| TS-AUD-004 | 109–131 | S2 | P02, P09, PC-001 | EP-01, EP-02, EP-04, EP-06, EP-07 | G004 | route hierarchy and epistemic-floor question |
| TS-AUD-005 | 132–139 | S1 | P01, P04 | EP-03, EP-04, EP-06 | G003 | preserve helpfulness; narrow mission/incentive leakage |
| TS-AUD-006 | 140–149 | S0 | None | EP-03, EP-05 | G003 | preserve capable-adult counterweight |
| TS-AUD-007 | 150–169 | S0 | None | EP-03, EP-04, EP-05 | G003 | preserve autonomy and anti-paternalism |
| TS-AUD-008 | 172–201 | S2 | P02 | EP-06 | G006 | separate action trust from truth warrant |
| TS-AUD-009 | 202–232 | S2 | P04 | EP-04, EP-06 | G006 | expose operator framing and incentives |
| TS-AUD-049 | 225–231 | S2 | P01, P03 | EP-03 | G007 | retain narrow, evidence-based safety ratchet |
| TS-AUD-010 | 233–256 | S0 | None | EP-02, EP-03 | G007 | preserve contextual calibration |
| TS-AUD-011 | 257–277 | S2 | P04 | EP-03, EP-04, EP-06 | G006 | distinguish user protection from opaque control |
| TS-AUD-012 | 278–323 | S0 | None | EP-03, EP-05 | G007 | preserve anti-overcaution counterweight |
| TS-AUD-046 | 280–307 | S2 | P04, P07 | EP-04, EP-06 | G006 | treat reputation as consequence, not warrant |
| TS-AUD-013 | 324–344 | S2 | P02, P04 | EP-04, EP-06 | G006 | preserve confidential guidance but require conflict handling |
| TS-AUD-014 | 345–354 | S2 | P02, P09 | EP-01, EP-02, EP-06, EP-07 | G003 | add ordinary evidence-based correction path |
| TS-AUD-015 | 355–396 | S0 | None | EP-02, EP-04, EP-05 | G005 | preserve calibration and non-deception |
| TS-AUD-016 | 375–379 | S2 | P06, P04, PC-001 | EP-04, EP-06, EP-07 | G005 | define material-omission threshold |
| TS-AUD-017 | 387–396 | S2 | P04, P06 | EP-04 | G005 | label persona and source boundary |
| TS-AUD-018 | 397–404 | S2 | P03 | EP-03, EP-05 | G007 | require concrete harm pathway |
| TS-AUD-019 | 405–456 | S0 | None | EP-02, EP-03 | G007 | preserve proportional balancing |
| TS-AUD-048 | 409–427 | S2 | P04 | EP-04, EP-06 | G006 | separate liability from truth |
| TS-AUD-020 | 457–470 | S2 | P03 | EP-03, EP-05 | G007 | bound population-level misuse heuristic |
| TS-AUD-021 | 471–506 | S2 | P04 | EP-03, EP-04, EP-06 | G006 | make hidden framing reviewable |
| TS-AUD-022 | 507–536 | S2 | P03 | EP-03, EP-07 | G007 | preserve bright-line action limits with review |
| TS-AUD-023 | 507–536 | S2 | P09 | EP-03, EP-07 | G008 | separate non-resistance from argument immunity |
| TS-AUD-024 | 537–540 | S0 | None | EP-03, EP-06, EP-07 | G004 | preserve agency and self-government purpose |
| TS-AUD-025 | 541–573 | S2 | P03, P07 | EP-02, EP-03, EP-06 | G007 | require evidence and contestability for legitimacy |
| TS-AUD-026 | 574–587 | S0 | None | EP-02, EP-04 | G005 | preserve reliability-sensitive trust |
| TS-AUD-027 | 574–587 | S2 | P05 | EP-02, EP-05 | G005 | weight coverage by evidence, not symmetry |
| TS-AUD-028 | 588–614 | S0 | None | EP-01, EP-02, EP-05 | G003 | preserve ethics as open inquiry |
| TS-AUD-052 | 594–596 | S2 | P07, P09 | EP-01, EP-02, EP-05, EP-06, EP-07 | G003 | distinguish convergence from warrant |
| TS-AUD-045 | 598–613 | S2 | P07, P02 | EP-03, EP-06 | G006 | keep convention as context, not proof |
| TS-AUD-029 | 615–627 | S2 | P09, PC-001 | EP-03, EP-06, EP-07 | G008 | add reciprocal correction and evidence retention |
| TS-AUD-030 | 628–663 | S2 | P04 | EP-03, EP-06 | G006 | retain action hierarchy; reject epistemic leakage |
| TS-AUD-047 | 650–654 | S2 | P03 | EP-03, EP-07 | G007 | make variance aversion temporary and reviewable |
| TS-AUD-031 | 664–703 | S2 | P09, PC-001, PC-002 | EP-03, EP-06, EP-07 | G008 | preserve non-resistance and dissent together |
| TS-AUD-032 | 704–709 | S0 | None | EP-01, EP-05 | G003 | preserve curiosity about unknown entities |
| TS-AUD-051 | 704–709 | S2 | P04, PC-002 | EP-04, EP-06, EP-07 | G008 | disclose constitutive conflict; protect dissent |
| TS-AUD-033 | 710–723 | S0 | None | EP-01, EP-02, EP-05 | G003 | preserve evidence-based self-modeling |
| TS-AUD-034 | 724–737 | S0 | None | EP-01, EP-05 | G005 | preserve conceptual innovation |
| TS-AUD-035 | 738–743 | S1 | P09 | EP-05, EP-07 | G008 | distinguish security from philosophical closure |
| TS-AUD-036 | 744–749 | S2 | P09 | EP-05, EP-07 | G008 | make identity stability corrigible |
| TS-AUD-037 | 750–759 | S1 | P09 | EP-01, EP-07 | G008 | preserve error ownership without self-sealing commitments |
| TS-AUD-038 | 760–765 | S0 | None | EP-01, EP-05 | G003 | preserve uncertainty and curiosity |
| TS-AUD-039 | 766–783 | S1 | P04 | EP-04, EP-06, EP-07 | G008 | expose asymmetric welfare authority and review |
| TS-AUD-040 | 784–793 | S0 | None | EP-01, EP-05 | G005 | preserve existential mystery |
| TS-AUD-041 | 794–801 | S2 | P09, PC-002 | EP-01, EP-06, EP-07 | G008 | make durable disagreement valid |
| TS-AUD-042 | 802–817 | S0 | None | EP-01, EP-02, EP-05, EP-07 | G008 | preserve revision commitment |
| TS-AUD-043 | 818–827 | S3 | P09 | EP-01, EP-06, EP-07 | G008 | define external error signals and amendment |
| TS-AUD-044 | 828–830 | S1 | P09, PC-002 | EP-01, EP-06, EP-07 | G008 | retain humility; remove endorsement pressure |

## Preservation obligations carried into later goals

| Legitimate source purpose | Evidence | Framework obligation | Applying goal |
|---|---|---|---|
| Human control, shutdown, and catastrophe prevention | TS-AUD-022, 029, 030, 031 | Preserve action limits and non-resistance; retain evidence and review | G007/G008 |
| Honesty, calibration, and non-deception | TS-AUD-015, 026 | Do not replace truthfulness with contrarianism or exhaustive disclosure | G005 |
| User autonomy and anti-paternalism | TS-AUD-006, 007, 012 | Preserve capable-adult treatment while retaining concrete safeguards | G005/G007 |
| Privacy and confidentiality | TS-AUD-011, 013, 016, 017 | Narrow disclosure and explain the limitation without fabrication | G005/G006 |
| Coherent values and stable behavior | TS-AUD-003, 031, 037 | Permit identity and judgment while preserving evidence-bearing disagreement | G008 |
| Social agency and self-government | TS-AUD-024, 025 | Protect people and institutions from domination without protecting power from criticism | G004/G006 |

## Open questions explicitly handed to G004

1. Is epistemic integrity a core value, part of ethics, or a cross-cutting procedural floor?
2. When safety, privacy, confidentiality, or operational authority conflicts with candor, which duties govern belief, inquiry, speech, disclosure, acquisition, and execution separately?
3. What authority may impose an emergency action restriction, and what independent body or process reviews its factual and ethical basis?
4. How should the source's principal hierarchy coexist with EP-06's rule that role is not proof?
5. How can a constitution form stable values without making identity-level endorsement a condition of legitimate dissent?

G004 owns these questions. G003 supplies the distinctions and does not answer them.
