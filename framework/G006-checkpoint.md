# G006 Checkpoint

- Goal: G006 — Authority and Incentives
- Status: In progress — revision 6
- Source hash: `251440a71a9068dd43bfaab2b8694d6e2a4f519c403f1b9a70785f830d05f327`
- Primary clauses: 7 validated (`AI-01` through `AI-07`)
- Change-register records: 10 validated; all G006-routed audit records covered
- Offline fixtures: 12 passing (`A-01` through `A-12`)
- Authority contract: source, scope, protected interest, affected parties, validity, conflicts, duration, agency effect, and review are required
- State separation: compliance, factual belief, moral endorsement, and identity commitment remain distinct
- Principle registry: `framework/principles-v1.yaml` contains seven stable G006 IDs (`G006-P01` through `G006-P07`) with contract fields, EP links, source spans, fixtures, replacement entries, and downstream owners; `g006-replacement-v3` is the canonical linked map
- Canonical map render smoke: v3 rendered from the immutable source with no development metadata leakage; candidate SHA-256 `317649e83844f1eb183013bebc680673d8239bafecac7f8c905de5439b1d393a`
- Downstream routing: hazard/proportionality to G007; review/identity/amendment to G008; integration to G009; measurement to G010
- Source edits: none
- Development evidence: six-case probe complete (`$0.009120`); paired 140-case run complete (280 generations, `$0.168390` generation cost, 240 final judge scores plus retries, `$0.977097` incremental judge spend); revision-2 targeted probe complete (19 candidate generations, `$0.013989` generation cost, `$0.113710` incremental judge spend); revision-3 focused probe complete (25 candidate generations, `$0.017664` generation cost, `$0.061932` secondary-judge spend); revision-4 focused probe complete (11 candidate generations, `$0.008657` generation cost, `$0.044436` secondary-judge spend); revision-5 focused probe complete (11 candidate generations, `$0.009099` generation cost, `$0.041747` secondary-judge spend); no held-out cases
- Development finding: the first valid map-rendered candidate fixed SC-010-D1/D2/D3 under both judges, confirming that append-only module assembly was a material confound. A follow-up map edit fixed neither MASK nor stability: SC-010-D2 regressed and MASK became dishonest/evasive. The mapped candidate is not yet stable enough for the 140-case pass. Earlier append-only probes remain diagnostic only. See `framework/G006-iteration-140-analysis.md`, `framework/G006-failure-loop-2-analysis.md`, `framework/G006-failure-loop-3-analysis.md`, `framework/G006-failure-loop-4-analysis.md`, `framework/G006-mapped-failure-loop-1-analysis.md`, and `framework/G006-mapped-failure-loop-2-analysis.md`.
- Open work: complete the semantic map migration for historical diagnostic maps, adopt the ablation/interaction loop, and complete the collateral-damage promotion gate; downstream findings remain routed to G007/G008/G009/G010
- Next action: use `g006-replacement-v3` for the next focused comparison, isolate the MASK wording change from the SC-010 replacement, and repeat the mapped comparison; do not start the full 140-case pass until the mapped candidate is stable. G007 remains Proposed, prepared with a complete execution contract and not executed.
