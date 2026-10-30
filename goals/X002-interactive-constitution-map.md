# X002 — Interactive Constitution Map

Status: Discovery — exploratory website branch
Execution stage: Goal scaffold; website integration target not yet pinned
Mainline relationship: Non-blocking productization branch from G006 revision 6
Mainline successor: G007 remains the next numbered goal unless the user explicitly promotes this branch

## Objective

Build and integrate an interactive map of the constitution that lets a reader move through the pinned source passages and the corresponding amendments without confusing the two. The primary interaction is an exact, reversible toggle between original source text and replacement text for each mapped passage. The map must preserve source provenance, principle relationships, and the distinction between the immutable upstream constitution and this project's revisions.

The first release uses the validated G006 replacement map as its initial slice. It is a visualization and explanation surface, not a new constitutional authority and not evidence that an amendment is correct.

## Integration premise

The current repository contains the source, replacement map, and amendment modules, but it does not contain the user's website. Execution therefore begins by pinning the website repository, route or embed boundary, framework, build command, and deployment path. If the website remains outside this repository, the branch must produce a portable component and generated data package rather than copying constitutional text by hand into an unrelated site.

## Iteration loop

Follow `ITERATION_PROTOCOL.md` with a visualization-specific loop:

1. Generate the map data from the immutable source and replacement map.
2. Validate hashes, source spans, and replacement coverage offline.
3. Render a small representative slice in the target website.
4. Test original/amendment switching, provenance display, responsive layout, keyboard access, and reduced-motion behavior.
5. Review whether the interface makes the amendment look authoritative, hides uncertainty, or collapses source and candidate into one text.
6. Revise the data contract or component, then rerun the offline and browser checks.

A visual or wording improvement without a changed interaction or comprehension hypothesis is not evidence of progress by itself. Route source-integrity failures to the active branch, constitutional interpretation concerns to G006–G010, and website-platform constraints to the integration backlog.

## Project alignment

Advances O2, O5, O7, and O8 by making passage-level provenance, recurring patterns, and revision status inspectable. It supports SC-003, SC-006, SC-007, and SC-010 as an explanation and audit surface, but does not claim that the map itself satisfies those scenarios.

Preserves A1–A5, A8, A9, A11, and A12. The map must never edit or silently normalize `20260120-constitution.md`, infer author motives, or present a replacement as the upstream text.

## Inputs

- `PROJECT.md`, `ROADMAP.md`, and `EXECUTION_PROFILE.md`;
- immutable `20260120-constitution.md` and its pinned SHA-256;
- `evals/maps/g006-replacement-v3.json`;
- `amendments/G005-honesty-and-inquiry.md` and `amendments/G006-authority-and-incentives.md`;
- `framework/principles-v1.yaml`;
- `audits/philosophical-patterns.md` and relevant G006 traceability records;
- the website repository, route, framework, build command, and deployment contract, to be pinned before implementation.

No paid model call, held-out evaluation material, or live source retrieval is required for this branch.

## In scope

- A generated, versioned map-data contract derived from the immutable source and exact replacement map;
- the initial G006 slice, including source spans, replacement text, clause IDs, principle IDs, fixture IDs, and downstream obligations;
- a navigable section/node view with one selected record at a time;
- an original/amendment toggle that replaces the displayed text rather than appending both as if they were simultaneous rules;
- provenance and status details that remain visible without overwhelming the passage text;
- a clear visual distinction between `original`, `amendment`, `preserved purpose`, `limitation addressed`, and `status`;
- keyboard-accessible controls, semantic labels, responsive layout, readable contrast, and reduced-motion support;
- website integration at the pinned route or embed boundary;
- deterministic validation and a small browser smoke test for data integrity and primary interaction;
- an implementation note describing how future G007–G010 maps can be added without changing the UI contract.

## Out of scope

- Editing `20260120-constitution.md`;
- deciding whether a mapped amendment is philosophically or empirically correct;
- replacing the source or candidate constitution with the visualization's current selection;
- mapping every source section before the first release;
- live collaborative editing, comments, voting, or user-authored amendments;
- runtime fetching from unpinned external sources;
- automated claims that a visual relationship proves a causal or normative relationship;
- publication or deployment until the website target and content review are approved.

## Data contract

The generated map package must carry:

- `map_version`, `source_path`, `source_sha256`, `replacement_map_id`, `replacement_map_sha256`, and generator version;
- one record per mapped source span with stable `entry_id`, heading, source line bounds, exact original text, exact replacement text, and a deterministic text hash;
- `clause_ids`, `principle_ids`, `fixture_ids`, `downstream_obligations`, preserved purpose, prohibited interpretation, and review status;
- explicit `display_modes` containing `original` and `amendment`; a mode must never silently merge the two texts;
- a validation report proving every displayed original matches the pinned source span and every displayed amendment matches the replacement map.

The website component consumes this generated package. It must not parse the constitution or replacement map at runtime, and it must not contain a second hand-maintained copy of the passages.

## Interaction contract

The first release must make these states obvious:

1. **Original:** the selected passage as it appears in the pinned upstream source.
2. **Amendment:** the exact replacement text proposed by this project.
3. **Traceability:** source lines, map entry, principles, and status for the selected passage.

Selecting a different node changes the selected record but does not change the global source hash. Switching modes updates one main text region and its mode label. A reader must be able to return to the original with one action.

## Acceptance criteria

- **X2AC1 — Pinned website target:** The website repository, route or embed boundary, framework, build command, and deployment path are recorded.
- **X2AC2 — Source integrity:** The generator and validator prove that every original passage shown is byte-for-byte derived from the pinned source span and that the source hash is unchanged.
- **X2AC3 — Replacement integrity:** Every amendment shown is derived from the exact replacement-map entry; no map metadata or contradictory append-only module is rendered as constitution text.
- **X2AC4 — Reversible comparison:** A reader can select each initial mapped record and switch original ↔ amendment without losing the selected record or provenance.
- **X2AC5 — Traceability:** The selected view exposes stable entry, clause, principle, source-span, and status metadata without implying that metadata is part of the constitution.
- **X2AC6 — Epistemic framing:** The interface labels the source as immutable and the amendment as proposed/project-authored; it does not present the revision as Anthropic's constitution or as settled truth.
- **X2AC7 — Accessibility:** Automated checks and manual review cover keyboard operation, focus visibility, semantic labels, contrast, responsive widths, and reduced-motion behavior.
- **X2AC8 — Browser behavior:** A smoke test confirms initial render, node selection, original/amendment toggle, and recovery from an invalid or missing record.
- **X2AC9 — Deterministic build:** Regenerating the data package from unchanged inputs produces the same output and hashes.
- **X2AC10 — No hidden drift:** The website build fails or visibly warns when the source or replacement-map hash no longer matches the generated package.
- **X2AC11 — Extensibility:** The implementation note demonstrates how another replacement map can be added without changing the interaction contract or duplicating passage data.
- **X2AC12 — Review handoff:** The branch records a screenshot or browser review, test commands, known limitations, and a clear decision about whether to expand beyond the G006 slice.

## Expected artifacts

- `goals/X002-interactive-constitution-map.md`;
- `framework/X002-interactive-map-contract.md`;
- a generated map-data artifact with a stable version and hash;
- an offline generator and validator for source-span/replacement integrity;
- the website component or embed package;
- browser smoke and accessibility checks;
- `framework/X002-verification.md`;
- `framework/X002-checkpoint.md`;
- a website integration note with the pinned route/build/deployment details;
- updates to `ROADMAP.md` and, only if needed, `BACKLOG.md`.

## Stop conditions

Stop before integration if the website target cannot be pinned, the source or replacement-map hash drifts, a source span cannot be matched exactly, the component would require a hand-maintained duplicate of constitutional text, or the UI makes original and amendment indistinguishable. Stop after integration if the primary toggle is inaccessible, provenance is hidden, or the build cannot detect stale generated data.
