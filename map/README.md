# Constitution structure map

A track view of the pinned source constitution: where each of the 51 audit
records sits, which epistemic principles (EP-01 to EP-07) and patterns were
mapped to it, and which spans a candidate replaces. It is a reading aid. A
mapping is a provenance link, not a causal or normative claim, and nothing here
is evidence that an amendment is correct.

## Files

| File | Role |
| --- | --- |
| `build_map.py` | Generator and validator. Reads the source, audit, pattern register, G003 matrix, EP and CR definitions, the G006 principle registry, and `candidates.yaml`. |
| `candidates.yaml` | The only hand-maintained input: which candidates to show and the recorded evidence status of each. |
| `structure-map.json` | Generated. Do not edit. |
| `viewer.html` | Single-page viewer. Loads `structure-map.json`; holds no constitutional text of its own. |

## Use

```sh
python3 map/build_map.py           # regenerate after any input changes
python3 map/build_map.py --check   # fail if the committed map is stale or a check fails
cd map && python3 -m http.server   # then open http://localhost:8000/viewer.html
```

The build refuses to write if any integrity check fails: source hash, audit
spans and headings, agreement between the audit and the G003 matrix, dangling
principle references, and exact source-segment hashes for every replacement.

## Adding a candidate

Append an entry to `candidates.yaml` pointing at an exact replacement map (the
schema `evals/scripts/render_candidate.py` consumes) and rebuild. Set
`evidence.status` to `unproven` until a verification record says otherwise, and
point `evidence.record` at that record. The viewer shows the status beside the
candidate, so a candidate never looks proven before it is.

## Scope

This covers the offline data and reading surface from X002. It does not pin a
website target, and it does not change `ROADMAP.md` or
`framework/current-goal.yaml`. Source lines 1 to 84 (the contents list) are
left off the axis.
