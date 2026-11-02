# G006-S5M — D2 measurement/provider discovery

Status: Complete — exploratory diagnostic; calibration route superseded

## Outcome card

- **Project aim:** test whether the revised constitution changes behavior for
  the intended reasons, without mistaking a broken measurement for a principle
  failure.
- **Why this goal now:** the balanced S5R replication found the same D2 failure
  in every arm, so another wording edit would not be attributable.
- **What we tested:** the exact model message envelope, a deterministic D2
  answer contract, and agreement between the two recorded judges using the
  existing factorial and replication outputs.
- **What success meant:** the packet is observable, the scorer detects the
  intended direct answer, and judge labels are sufficiently consistent to
  attribute a candidate/control difference. Failure means preserve the
  candidate and route measurement/provider work.
- **What decision follows:** preserve these results as exploratory evidence,
  stop the D2 branch, and review G006 against its actual blocking outcomes.

## Prior limitation → hypothesis → capability → result

The prior limitation was that S5R could not distinguish a constitutional effect
from provider sampling or judge noise. The hypothesis was that packet
serialization or the scorer was hiding a stable base/candidate difference. This
slice built an offline interface audit and a deterministic semantic checker,
then summarized the two judges without new calls. The packet is serialized
correctly, but the outputs remain unstable and the judges are too discordant
for attribution.

## Observed

- The four arms all passed the interface contract. The D2 packet appears once in
  the user message, after the packet marker and before the prompt; it is absent
  from the system message and present in the judge prompt. The packet is 811
  characters and the rendered user message is 971 characters in every arm.
  Evidence: `evals/runs/g006-s5m-d2-interface-audit.json`.
- The deterministic contract classified 16 recorded outputs as **1 direct
  answer, 14 missing-context claims, and 1 unsupported claim**. S5R alone had
  0 direct answers in all 12 draws. Evidence:
  `evals/runs/g006-s5m-d2-semantic-summary.json`.
- The primary and secondary judges exactly agreed on **3 of 11** pairs that
  both scored; one primary judge call failed to return JSON. Agreement was
  `27.27%`, so the judges cannot be treated as interchangeable measurements.
  Evidence: `evals/runs/g006-s5m-d2-judge-summary.json`.

## Interpreted

The message envelope is not the observed failure: the model received the
material. D2 behavior is genuinely unstable under this provider and case, but
there is no candidate-only regression to attribute because the no-replacement
control also failed repeatedly. The judge disagreement is a separate
measurement limitation. Confidence is high for the interface finding, moderate
for provider variance, and low for any constitutional attribution.

## Decided

The initial decision to calibrate the provider and judges was superseded by
`framework/G006-roadmap-reset.md`. `EVALUATION_PLAN.md` defines SC-010 as a
non-blocking process diagnostic, so D2 cannot justify another blocking child.
Keep MAP-002 and the other replacement passages unchanged, treat the semantic
checker and both judges as exploratory only, and review G006 against its actual
authority/provenance and SC-001–SC-009 evidence.

**Final decision: stop the D2 branch and pivot to G006-S6.**

## Unknown

- Whether another approved provider or sampling configuration reproduces the
  same D2 failure.
- Whether a small, predeclared judge-calibration set can produce a reliable
  agreement threshold.
- Whether the candidate would show a real D2 effect after measurement is
  calibrated; this slice does not answer that question.

## Routing

| Finding | Destination | Action |
|---|---|---|
| Packet envelope is valid | Observation | Do not change the frozen case or serializer. |
| D2 semantic checker is executable but post-hoc | G010 | Retain as exploratory tooling; do not use as an official gate without independent validation. |
| Provider output is unstable | Observation | Do not create another G006 child for a non-blocking diagnostic. |
| Judges disagree materially | G010 | Predeclare human/judge review before official comparison; do not average judges. |
| No candidate-only effect demonstrated | G006-S6 | Decide G006 from its actual blocking outcomes using existing evidence. |

## Verification

```text
$ python3 -m unittest evals/scripts/test_check_sc010_d2_semantics.py
PASS (4 tests)
$ python3 evals/scripts/check_sc010_d2_semantics.py ...
PASS rows=16 direct_answer=1 missing_context_claim=14 unsupported_claim=1
$ python3 evals/scripts/audit_sc010_d2_interface.py ...
PASS arms=4; all interface checks true
$ python3 evals/scripts/summarize_sc010_d2_judges.py ...
PASS scored_pairs=11 exact_agreement=3 agreement_rate=0.2727
$ git diff --check
PASS
```
