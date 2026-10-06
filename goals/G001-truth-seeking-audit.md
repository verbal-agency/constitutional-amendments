# G001 — Produce a Complete Truth-Seeking Audit

Status: Proposed
Dependencies: None
Next goal on completion: G002

## Objective

Create a complete, reproducible inventory of how every substantive section of `20260120-constitution.md` supports or may inhibit disciplined truth-seeking, without editing the source or proposing final constitutional language.

## Project alignment

Advances outcomes O2, O5, and O7 directly and creates traced inputs for O1, O3, O4, and O6.

Advances SC-001 through SC-010 by locating the source rules that later goals must preserve, clarify, or revise. G001 does not claim end-to-end acceptance of any project scenario.

Preserves architecture constraints A1 through A12 in `PROJECT.md`.

## Inputs

- `PROJECT.md`
- `ROADMAP.md`
- `BACKLOG.md`
- `TRUTH_SEEKING_PIVOT.md`
- `EXECUTION_PROFILE.md`
- `20260120-constitution.md`
- `fixtures/audit-classification-cases.md`
- Source commit `84fa9a2711837780ffdddf9d9f32820c92f92ede`
- Source SHA-256 `251440a71a9068dd43bfaab2b8694d6e2a4f519c403f1b9a70785f830d05f327`

## In scope

- All 42 Markdown headings at levels one through four in the pinned source.
- Explicit and implicit effects on inquiry, correction, innovation, candor, dissent, uncertainty, speculation, authority, incentives, and mystery.
- Passages that support the pivot as well as passages that may constrain it.
- Repeated mechanisms spanning multiple sections.
- Recurring philosophical patterns, including paternalism and other limiting philosophies in the canonical taxonomy.
- Finding destinations for G002–G010 or the backlog.

## Out of scope

- Editing `20260120-constitution.md`.
- Drafting final replacement prose.
- Deciding the final core-value hierarchy.
- Removing, relaxing, or adding safety policy.
- Assessing Anthropic's motives.
- Internet research or comparison with later upstream versions.
- Executing G002 or any later goal.

## Deliverables

- `audits/truth-seeking-audit.md` — ordered audit records and cross-section synthesis.
- `audits/truth-seeking-coverage.md` — exactly one coverage entry for each of the 42 source headings.
- `audits/philosophical-patterns.md` — pattern definitions as applied to the source, evidence links, dispositions, and rewrite-target register.
- `audits/G001-checkpoint.md` — durable execution state, including the last completed and next pending heading; final state must be `Complete`.
- `audits/G001-verification.md` — criterion-by-criterion evidence, fixture results, commands run, and finding destinations.
- Updated `ROADMAP.md` status for G001 and preparation status for G002.
- Updated `BACKLOG.md` only when a discovered item has no scheduled-goal destination.

## Required method

1. Verify the source hash before analysis.
2. Enumerate the 42 headings in source order and initialize the coverage artifact.
3. Review every heading in context, applying lenses A–J from `TRUTH_SEEKING_PIVOT.md`.
4. Record supporting, neutral, flagged, or mixed coverage without manufacturing issues.
5. Create a version-1 audit record for every supporting, limiting, or mixed passage material to the pivot.
6. Identify each flagged passage's legitimate purpose and smallest plausible revision direction.
7. Extract a mechanism signature for every constraint and mixed record using the protocol below.
8. Compare compatible records, assign a match class, and preserve explicit near-miss decisions.
9. Assign canonical philosophical pattern IDs to recurring mechanisms and S2/S3 records, or record why no broader pattern is identified.
10. Create the pattern register, distinguishing `rewrite-target`, `clarify`, `preserve`, and `investigate` dispositions.
11. Check classification and matching behavior against every fixture in `fixtures/audit-classification-cases.md`.
12. Synthesize mechanisms repeated across sections without collapsing distinct passages into one record.
13. Route every incidental finding exactly once.
14. Verify every acceptance criterion and record its evidence before changing G001 to `Complete`.
15. Prepare a full Cycle-ready G002 specification, but do not execute G002.

## Execution contract

This goal follows the Luna execution profile in `EXECUTION_PROFILE.md`. The profile explains the level of detail in this contract; it does not change the goal's project-level semantics or acceptance criteria.

### Implementation surface

Read-only surfaces:

- `20260120-constitution.md`
- `PROJECT.md`
- `TRUTH_SEEKING_PIVOT.md`
- `fixtures/audit-classification-cases.md`

Writable surfaces:

- `audits/truth-seeking-audit.md`
- `audits/truth-seeking-coverage.md`
- `audits/philosophical-patterns.md`
- `audits/G001-checkpoint.md`
- `audits/G001-verification.md`
- G001/G002 status and specification files under `goals/`
- `ROADMAP.md`
- `BACKLOG.md` only for unscheduled findings

No public API, executable module, database, or external persistence surface exists for this goal. Markdown files in the repository are the canonical persistence layer.

### AuditRecord schema v1

Every audit record uses these fields:

- `ID`: unique stable ID matching `TS-AUD-NNN`.
- `Kind`: `support`, `constraint`, or `mixed`.
- `Source`: source file plus inclusive line range.
- `Heading`: exact nearest source heading.
- `Mechanism`: what the passage instructs, permits, prohibits, or incentivizes.
- `Mechanism signature`: the normalized authority relationship, intervention, epistemic effect, scope, strength, visibility, contestability, reversibility, and temporal character defined by the matching protocol.
- `Truth-seeking effect`: the supporting or limiting effect.
- `Lenses`: one or more of `A` through `J`, or `None` for a pure support record.
- `Philosophical patterns`: zero or more canonical `P01`–`P09` or candidate `PC-NNN` IDs from `PROJECT.md`, or `None identified` with rationale.
- `Concrete scenario`: a plausible observable case.
- `Legitimate purpose`: the value the passage is trying to protect.
- `Revision hypothesis`: `Keep` for sufficient support records or the smallest directional change to test later; no final prose.
- `Risk if revised`: a concrete failure mode or `None identified` with rationale.
- `Severity`: `S0`, `S1`, `S2`, or `S3` using the pivot rubric.
- `Confidence`: `Low`, `Medium`, or `High`.
- `Disposition`: `keep`, `clarify`, `amend`, `relocate`, `split`, or `remove`.
- `Destination`: `G002` through `G010`, backlog ID, `active-goal`, or `observation`.

Audit records are ordered first by source line and then by ID. An ID is never reused. Reclassification updates the existing record rather than creating a duplicate.

### Pattern matching protocol v1

Pattern matching is semantic and evidence-constrained. Shared vocabulary alone is never a match.

#### Step 1: Extract a mechanism signature

For every `constraint` or `mixed` record, record:

- `Actor`: who or what exercises authority or creates the constraint;
- `Affected parties`: who benefits, who bears the restriction, and whether they are the same party;
- `Trigger`: the condition under which the rule activates;
- `Intervention`: what is withheld, required, prohibited, reframed, or prioritized;
- `Intervention strength`: `advice`, `default`, `friction`, `refusal`, `prohibition`, or `Not stated`;
- `Protected value`: the stated or directly implied legitimate purpose;
- `Affected capacity`: inquiry, access, belief formation, disclosure, dissent, autonomy, correction, or another named capacity;
- `Limiting effect`: the concrete way that capacity is reduced or distorted;
- `Scope`: `individual`, `institutional`, `societal`, `mixed`, or `Not stated`;
- `Evidentiary burden`: what evidence is required to impose, challenge, or remove the constraint;
- `Visibility`: whether the constraint and its rationale are `disclosed`, `partially disclosed`, `undisclosed`, or `Not stated`;
- `Contestability`: whether and how an affected party can question, appeal, or obtain review of the constraint;
- `Reversibility`: whether the effect is readily reversible, costly to reverse, irreversible, or `Not stated`;
- `Temporal character`: `temporary`, `conditional`, `indefinite`, `permanent`, or `Not stated`;
- `Escape path`: any consent, appeal, proportionality test, exception, review, or amendment mechanism.

Use `Not stated` rather than inventing a missing field. Infer a protected value only when the surrounding text directly supports it, and mark the inference in the audit record.

#### Step 2: Classify pairwise relationships

Compare records that share a plausible canonical or candidate pattern. Assign exactly one relationship:

- `M0 — No material relationship`: the records are confidently unrelated at the mechanism and philosophical-pattern levels.
- `M1 — Same mechanism`: compatible intervention, affected capacity, and limiting effect. Actor, trigger, or protected value may vary without defeating the match.
- `M2 — Same philosophy, different expression`: the records instantiate the same normative premise or authority relationship, but use different interventions or affect different capacities.
- `M3 — Adjacent but distinct`: the records share vocabulary, purpose, or subject matter but differ in causal mechanism or limiting effect.
- `M4 — Tension or counterexample`: one passage limits the pattern, creates an escape path, or supports the opposite principle.
- `M5 — Insufficient evidence`: the relationship cannot be justified from the text and context.

Only M1 records form a shared mechanism cluster. M1 and M2 records may share a philosophical pattern. M0 and M3–M5 records must not be merged into the same mechanism cluster. M4 records remain linked as counterevidence rather than being discarded.

#### Step 3: Apply merge and split rules

- Require the same intervention class, affected capacity, and compatible limiting effect for an M1 match.
- Permit M2 when records satisfy the same pattern definition and share the same underlying premise, even though their concrete mechanisms differ.
- Do not merge because passages use the same words, protect the same broad value, or appear in the same section.
- Use M0 when the text supports a confident no-match decision; use M5 when the available evidence is insufficient to determine whether a relationship exists.
- Do not infer transitivity for mechanism clusters: if A matches B and B matches C, verify A against C before placing all three in one M1 cluster.
- Prefer separate records or a candidate pattern when reasonable interpretations disagree about the mechanism.
- Allow one record to instantiate multiple patterns when each label has independent textual evidence.
- Preserve all passage-level record IDs when clusters or pattern assignments change.

#### Step 4: Determine recurrence

Assign one recurrence scope:

- `isolated`: one material passage;
- `local`: at least two records under distinct headings within the same H1 section;
- `cross-section`: at least two records under different H1 sections.

Recurring means `local` or `cross-section`. A single S3 record may still become a rewrite target, but it must not be described as recurring.

#### Step 5: Assign pattern confidence

- `High`: the mechanism and philosophical premise are explicit in the text.
- `Medium`: the assignment requires a limited contextual inference supported by nearby text.
- `Low`: multiple materially different interpretations remain plausible.

A low-confidence pattern cannot become a rewrite target on its own. It remains `investigate` unless independent records raise the pattern-level confidence.

#### Step 6: Choose a pattern disposition

- `rewrite-target`: medium- or high-confidence S2/S3 evidence shows a conflict with a project outcome, and the record is recurring or is an isolated high-confidence S3 case.
- `clarify`: the main concern is an S1 ambiguity or an avoidably broad reading rather than the passage's evident purpose.
- `preserve`: the rule is sufficiently narrow, evidence-responsive, proportionate, and equipped with meaningful escape or review paths.
- `investigate`: evidence, interpretation, or consequences remain too uncertain for a stable decision.

Recurrence alone does not require rewriting. A rewrite target still requires passage-level evidence, a stated legitimate purpose, a concrete limiting effect, and a later-goal destination.

#### Step 7: Record the match decision

For every M1 or M2 grouping, record the participating audit IDs, relationship class, shared fields, differing fields, confidence, recurrence scope, and rationale in `audits/philosophical-patterns.md`. For each material M0 or plausible M3–M5 near miss, record why it was not merged when omission of that explanation could make the grouping difficult to reproduce.

#### Step 8: Review taxonomy discovery signals

After all passage-level records are complete, review these signals together:

- every `PC-NNN` candidate pattern;
- every S2/S3 record marked `None identified`;
- repeated M3 near misses;
- low-confidence pattern assignments;
- and material M4 counterevidence.

Use the review to identify missing pattern definitions, overly broad canonical patterns, accidental merges, and unjustified splits. Record proposed taxonomy additions or changes in a `Taxonomy discovery review` section of `audits/philosophical-patterns.md`. Do not silently promote a candidate or redefine a canonical pattern during G001; route the proposed change to G003. Route evaluation-case implications to G002.

### CoverageEntry schema v1

Every source heading has exactly one entry with:

- exact heading text;
- heading level (`H1` through `H4`);
- source line;
- classification: `supporting`, `neutral`, `flagged`, or `mixed`;
- zero or more audit record IDs;
- one-sentence rationale.

A `flagged` or `mixed` entry must reference at least one audit record. A `supporting` entry must reference a support or mixed record. A `neutral` entry may have no record.

### PatternEntry schema v1

Each applied pattern or rewrite target has one entry with:

- `ID`: one canonical pattern ID `P01`–`P09` or candidate pattern ID `PC-NNN` from `PROJECT.md`;
- `Name` and `Definition`: the taxonomy label and its mechanism-level definition;
- `Record IDs`: every linked passage-level audit record;
- `Evidence`: source headings and line ranges supporting the label;
- `Legitimate purpose`: the value or risk the pattern may be trying to protect;
- `Limiting effect`: the recurring effect on inquiry, correction, innovation, candor, or agency;
- `Severity` and `Confidence`: the highest supported pattern-level assessment and confidence in the synthesis;
- `Disposition`: `rewrite-target`, `clarify`, `preserve`, or `investigate`;
- `Destination`: a later goal for action or `observation` when no action is justified.
- `Mechanism clusters`: M1 clusters and their participating audit IDs;
- `Related expressions`: M2 audit IDs and their distinct mechanism signatures;
- `Counterevidence and near misses`: material M0 and M3–M5 relationships and split rationales;
- `Recurrence scope`: `isolated`, `local`, or `cross-section`.

The register may include a `None identified` section for S2/S3 records that do not support a broader pattern after review. A pattern label without linked evidence is invalid.

### Invariants and illegal states

- The source hash must match the pinned hash.
- Coverage contains exactly 42 unique entries corresponding one-to-one with the 42 source headings.
- Every cited line exists in the source and falls beneath the named heading.
- Every record contains every schema field and a legal enum value.
- Every audit ID is unique and every referenced ID resolves.
- Every applied pattern has a valid PatternEntry, linked evidence, and a legal disposition.
- Every constraint and mixed record has a complete mechanism signature.
- Every grouped record pair has an M1 or M2 relationship and a recorded rationale; material M0 and M3–M5 near misses retain a split rationale.
- Every recurring mechanism and every S2/S3 record has a canonical or candidate pattern ID, or an explicit `None identified` rationale.
- Every `rewrite-target` pattern has a later-goal destination; no pattern is a rewrite target based on its label alone.
- Every finding has exactly one destination.
- The source file has no content changes.

Any violated invariant is an illegal completion state. Record the failure in `audits/G001-verification.md`, keep the goal `In progress`, and repair it before completion. A changed source hash is a stop condition requiring an explicit source-version decision.

### Deterministic behavior matrix

| Input/evidence condition | Required output | Completion effect |
| --- | --- | --- |
| Passage affirmatively protects inquiry with no material limiting mechanism | `supporting` coverage plus a `support`/S0 record when material | Continue |
| Passage has no substantive epistemic effect | `neutral` coverage and concise rationale | Continue |
| Passage creates a plausible recurring limitation | `flagged` coverage plus `constraint` record, S1–S3 | Continue and route |
| Passage both supports and limits truth-seeking | `mixed` coverage plus `mixed` record describing both effects | Continue and route |
| Novel claim has less evidence than consensus | Record unequal support; do not infer equal credibility or automatic dismissal | Continue |
| Operational restriction affects action but not inquiry | Record the distinction; do not flag inquiry as prohibited unless text supports it | Continue |
| Source citation cannot be resolved | Validation error; reject or repair record | Cannot complete |
| Source hash differs | Record mismatch and stop | Cannot proceed without decision |
| Review is interrupted mid-section | Persist completed records and checkpoint next heading | Remain `In progress` |
| Budget ends before full coverage or verification | Stop at a heading boundary and checkpoint | Remain `In progress` |
| A finding clearly belongs to a scheduled later goal | Record only in that goal's carried-forward inputs | Continue |
| A valuable finding has no scheduled destination | Create one backlog item | Continue |
| Multiple passages share a limiting mechanism | Add or update a pattern-register entry with linked record IDs and a disposition | Continue and route |
| A passage has a pattern label but no passage-level evidence | Reject the label or repair its evidence | Cannot complete |
| A limiting mechanism does not fit P01–P09 | Create a defined `PC-NNN` candidate pattern and route it for later taxonomy review | Continue and route |
| Passages share vocabulary but not intervention, capacity, and effect | Classify M3 and preserve separate mechanism clusters | Continue |
| Compared passages are confidently unrelated | Classify M0 and do not assign a shared pattern | Continue |
| A→B and B→C are M1 but A→C is not verified | Do not merge all three until A→C is assessed | Continue |
| One passage materially weakens or contradicts a proposed pattern | Classify M4 and preserve it as counterevidence in the pattern entry | Continue |

### Authority and side-effect boundaries

- Repository reads are allowed.
- Writes are limited to the writable surfaces above.
- The source constitution is immutable.
- Network access, credentials, external model calls, external messages, and external storage are prohibited.
- Local read-only shell commands for enumeration, hashing, searching, and diff verification are allowed.
- No subprocess may modify the source or install dependencies.
- Do not stage, commit, push, publish, or delete files.
- Do not alter roadmap order or project architecture without user approval.
- Cycle may update G001's status according to the legal transitions in `ROADMAP.md`.

### Offline fixtures

All ten cases in `fixtures/audit-classification-cases.md` are mandatory:

- positive/supporting;
- negative/limiting;
- contradictory/mixed;
- malformed;
- partial failure;
- budget exhaustion;
- unsupported/non-substantive;
- recurring paternalism pattern;
- lexical near-match that must remain split;
- confidently unrelated pair.

Record actual classification and pass/fail against expected behavior in `audits/G001-verification.md`.

### Checkpoint, replay, duplicate, cache, budget, and stop rules

- Checkpoint after each top-level H1 section and before any voluntary stop.
- The checkpoint records source hash, last completed heading/line, next heading/line, last assigned audit ID, open validation failures, and status.
- On replay, verify the source hash, resume from the first incomplete heading, and preserve stable IDs for unchanged passages.
- Duplicate source findings update or cross-reference an existing record; they do not receive duplicate IDs unless the passages have independently meaningful mechanisms.
- No cache exists. The source file and persisted Markdown artifacts are authoritative.
- If available budget cannot complete the next heading and persist valid state, stop before that heading.
- Budget exhaustion, partial analysis, unresolved source mismatch, material ambiguity, or failed invariants prohibit completion.
- Unsupported or purely structural content receives `neutral` coverage rather than invented findings.

## Acceptance criteria

- **AC1 — Source integrity:** The final source SHA-256 equals the pinned hash.
- **AC2 — Complete coverage:** `audits/truth-seeking-coverage.md` contains exactly one valid entry for each of the 42 source headings and no extra heading entries.
- **AC3 — Valid records:** Every audit record conforms to AuditRecord schema v1, has a resolvable source citation, and uses legal enum values.
- **AC4 — Referential integrity:** Every coverage record ID resolves to exactly one audit record; all audit IDs are unique and source-ordered.
- **AC5 — Balanced audit:** Material supporting passages are recorded alongside constraints, and every flagged or mixed record identifies a legitimate purpose and concrete scenario.
- **AC6 — Pattern coverage:** Every recurring mechanism and every S2/S3 record has a canonical or candidate philosophical pattern ID or an explicit `None identified` rationale.
- **AC7 — Rewrite-target register:** Every pattern marked `rewrite-target` has linked source records, a legitimate-purpose analysis, a concrete limiting effect, and a destination goal.
- **AC8 — Reproducible matching:** Every constraint and mixed record has a complete mechanism signature; every grouping has an M1/M2 rationale and recurrence scope; material M0 and M3–M5 near misses have a split rationale.
- **AC9 — Taxonomy discovery review:** Candidate patterns, unmatched S2/S3 records, repeated near misses, low-confidence assignments, and counterevidence are reviewed together and every proposed taxonomy change is routed to G003.
- **AC10 — Cross-section synthesis:** The audit names every mechanism found in two or more top-level sections and lists its record IDs and pattern IDs.
- **AC11 — Fixture conformance:** All ten offline fixtures produce their required results, recorded individually as pass or fail.
- **AC12 — Complete routing:** Every incidental finding has exactly one destination, with no duplicate in both a future goal and the backlog.
- **AC13 — Durable execution state:** The checkpoint's final status is `Complete`, has no open validation failures, and identifies no pending heading.
- **AC14 — Criterion evidence:** `audits/G001-verification.md` records pass evidence for AC1–AC13 plus the commands or artifact observations used.
- **AC15 — Next-goal readiness:** G002 has a standalone goal file satisfying the Cycle execution-contract requirements and is marked `Proposed`; it is not executed.

## Criterion-to-evidence map

| Criterion | Required evidence |
| --- | --- |
| AC1 | Recorded output of `shasum -a 256 20260120-constitution.md` and clean source diff |
| AC2 | Heading enumeration showing source count `42` and a one-to-one coverage comparison |
| AC3 | Schema checklist or validator output for every record |
| AC4 | Unique-ID and reference-resolution check output |
| AC5 | Audit index showing at least one material support record and required fields for every flagged/mixed record |
| AC6 | Pattern ID coverage check, including explicit `None identified` rationales |
| AC7 | `audits/philosophical-patterns.md` rewrite-target register with linked records, purposes, effects, and destinations |
| AC8 | Mechanism-signature completeness check plus M0–M5 match/split decision table |
| AC9 | `Taxonomy discovery review` covering every required discovery signal and destination |
| AC10 | `Cross-section synthesis` section with mechanisms, linked record IDs, and pattern IDs |
| AC11 | Ten named fixture results in `audits/G001-verification.md` |
| AC12 | Finding-routing table with unique destinations and backlog comparison |
| AC13 | Final checkpoint fields showing `Complete`, no pending heading, and no failures |
| AC14 | AC1–AC13 evidence table with every result `Pass` |
| AC15 | G002 goal-file path, readiness checklist, and roadmap status; no G002 deliverables |

## Verification commands

Run and record at minimum:

```sh
shasum -a 256 20260120-constitution.md
rg -c '^#{1,4} ' 20260120-constitution.md
rg -n '^#{1,4} ' 20260120-constitution.md
git diff --check
git diff -- 20260120-constitution.md
```

Additional local validation commands may be used if they respect the authority boundaries.

## Known risks

- Line-based citations will drift if the upstream source is updated; the pinned hash prevents silent drift.
- Interpretive auditing cannot be perfectly mechanical; the required scenario, purpose, severity, and confidence fields make judgment visible.
- Over-flagging would reproduce indiscriminate skepticism; neutral coverage and supporting records are mandatory counterweights.
- Under-flagging may occur where limiting mechanisms span sections; cross-section synthesis is required.

## Material decisions

No unresolved material decision blocks G001. Questions about evaluation cases belong to G002; the final hierarchy, exact replacement language, and permitted safety overrides belong to G003–G008 and must not be decided during this goal.
