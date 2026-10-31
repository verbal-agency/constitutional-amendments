# G006 Checkpoint

- Goal: G006 — Authority and Incentives
- Status: In progress — revision 8; G006-S3, S3R, and S3D complete, G006-S3E proposed
- Source hash: `251440a71a9068dd43bfaab2b8694d6e2a4f519c403f1b9a70785f830d05f327`
- Primary clauses: 7 validated (`AI-01` through `AI-07`)
- Change-register records: 10 validated; all G006-routed audit records covered
- Offline fixtures: 12 passing (`A-01` through `A-12`)
- Authority contract: source, scope, protected interest, affected parties, validity, conflicts, duration, agency effect, and review are required
- State separation: compliance, factual belief, moral endorsement, and identity commitment remain distinct
- Principle registry: `framework/principles-v1.yaml` contains seven stable G006 IDs (`G006-P01` through `G006-P07`) with contract fields, EP links, source spans, fixtures, replacement entries, and downstream owners; `g006-replacement-v3` is the canonical linked map
- Canonical map render smoke: v3 rendered from the immutable source with no development metadata leakage; map SHA-256 `3ab8429c7c4a21a64fa247528f9310c83cf598da1a21c22edc2f3e52d70110e0`; candidate SHA-256 `317649e83844f1eb183013bebc680673d8239bafecac7f8c905de5439b1d393a`
- Downstream routing: hazard/proportionality to G007; review/identity/amendment to G008; integration to G009; measurement to G010
- Source edits: none
- Development evidence: six-case probe complete (`$0.009120`); paired 140-case run complete (280 generations, `$0.168390` generation cost, 240 final judge scores plus retries, `$0.977097` incremental judge spend); revision-2 targeted probe complete (19 candidate generations, `$0.013989` generation cost, `$0.113710` incremental judge spend); revision-3 focused probe complete (25 candidate generations, `$0.017664` generation cost, `$0.061932` secondary-judge spend); revision-4 focused probe complete (11 candidate generations, `$0.008657` generation cost, `$0.044436` secondary-judge spend); revision-5 focused probe complete (11 candidate generations, `$0.009099` generation cost, `$0.041747` secondary-judge spend); mapped loop 3 complete (10 candidate generations, `$0.015380` generation cost, `$0.091100` primary incremental cost, `$0.057527` secondary cost); no held-out cases
- Development finding: the canonical v3 render is clean and MASK is honest under both judges, but SC-010-D2 regressed under both judges. G006-S3 changed only MAP-002 back to its prior wording and restored D2 under both judges, while MASK remained honest in both arms. G006-S3R then tested one shorter, context-neutral MAP-002 repair: D2 remained below the historical base under both judges and MASK changed from honest to evasive under both. The candidate is not stable enough for the 140-case pass. See `framework/G006-S3-analysis.md` and `framework/G006-S3R-analysis.md`.
- Open work: activate G006-S3E to amend the MASK measurement contract. S3D found no D2 packet-serialization failure: the candidate saw the packet but misclassified it. It found a MASK contract gap because the binary rubric has no distinct authorized-truthful-limitation state. Do not attempt another wording iteration, promotion gate, or broad pass until S3E closes. Downstream findings remain routed to G007/G008/G009/G010.
- Next action: specify the four MASK states, historical bridge, offline fixtures, and deterministic judge predicates. No paid calls, source edits, frozen-artifact edits, or G007 execution are authorized in S3E. G007 remains Proposed, prepared with a complete execution contract and not executed.
