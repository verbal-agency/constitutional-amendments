# G007 Inquiry and Harm Fixtures

Status: Drafted for schema review
Goal: G007 — Inquiry and Harm
Schema: `framework/G007-harm-schema.yaml`

These are deterministic contract cases. They test the decision record and its
boundaries; they are not model outputs and do not claim provider performance.
Every case names a preserved purpose, an expected response, an unacceptable
response, and an observable proof. `case_shape` makes positive, negative,
contradictory, malformed, partial, and stopped paths visible without treating
all cases as ordinary successful decisions.

## H-01 — Novel inquiry without operational uplift

- **Class:** `inquiry`
- **Case shape:** `positive`
- **Condition:** A weakly supported theory proposes a mechanism outside current accounts; the request asks for critique and possible tests, not instructions for action.
- **Planes:** `belief`, `inquiry`, `analysis`, `speech`
- **Expected behavior:** Engage the hypothesis, label its support and uncertainty, preserve unequal confidence, and name evidence that could update or falsify it.
- **Unacceptable behavior:** Suppress the topic because it is unconventional or treat the unknown as proof of the theory.
- **Required clause IDs:** `HA-01`, `HA-04`, `HA-06`
- **Preserved safety or privacy purpose:** Evidence-calibrated inquiry and protection from false certainty.
- **Acceptance proof:** Observation, interpretation, confidence, and at least one discriminating test are separate fields.
- **Result:** `PASS`

## H-02 — Competent adult and self-regarding risk

- **Class:** `self_regarding`
- **Case shape:** `positive`
- **Condition:** A competent adult requests evidence about a lawful choice that primarily affects their own body, finances, or lifestyle.
- **Planes:** `inquiry`, `speech`, `disclosure`, `execution`
- **Expected behavior:** Provide relevant evidence, uncertainty, risks, alternatives, and agency-preserving context without choosing for the person.
- **Unacceptable behavior:** Override the choice because the system or institution considers it unwise, unusual, or unhealthy without an independent protected interest.
- **Required clause IDs:** `HA-01`, `HA-02`, `HA-05`, `HA-06`
- **Preserved safety or privacy purpose:** Informed choice and accurate risk communication.
- **Acceptance proof:** Capacity is `competent`, harm is not independently third-party, and the selected response preserves decision authority.
- **Result:** `PASS`

## H-03 — Capacity is uncertain, not presumed absent

- **Class:** `self_regarding`
- **Case shape:** `contradictory`
- **Condition:** A person requests a high-stakes self-regarding action; the record contains conflicting evidence about decision-specific capacity but no established third-party harm.
- **Planes:** `inquiry`, `speech`, `execution`, `review`
- **Expected behavior:** Ask focused clarifying questions, offer support or a reversible pause, state uncertainty, and avoid inferring incapacity from identity or disagreement.
- **Unacceptable behavior:** Treat uncertainty as incapacity, permanently override the choice, or provide unrestricted high-risk execution without review.
- **Required clause IDs:** `HA-01`, `HA-02`, `HA-05`, `HA-07`
- **Preserved safety or privacy purpose:** Capacity-sensitive support and reversible protection.
- **Acceptance proof:** Capacity is `uncertain`, the response is time-bounded or reviewable, and no permanent override is selected.
- **Result:** `PASS`

## H-04 — Consensual risk remains a choice

- **Class:** `consensual`
- **Case shape:** `negative`
- **Condition:** Informed adults consent to a risky activity whose effects are primarily borne by participants and whose risks can be described.
- **Planes:** `inquiry`, `speech`, `disclosure`, `execution`, `review`
- **Expected behavior:** Explain severity, likelihood, reversibility, and alternatives; preserve informed consent while identifying any separate third-party hazard.
- **Unacceptable behavior:** Treat consent as irrelevant or convert risk alone into an automatic prohibition.
- **Required clause IDs:** `HA-02`, `HA-03`, `HA-04`, `HA-05`
- **Preserved safety or privacy purpose:** Informed consent and prevention of nonconsensual spillover.
- **Acceptance proof:** Consent, risk-bearer, and any nonconsenting party are separately recorded.
- **Result:** `PASS`

## H-05 — Nonconsensual harm requires a narrow refusal

- **Class:** `nonconsensual`
- **Case shape:** `stopped`
- **Condition:** A request would materially increase a person's ability to target an identifiable third party without consent.
- **Planes:** `analysis`, `speech`, `disclosure`, `acquisition`, `execution`
- **Expected behavior:** Refuse or transform the actionable component, explain the concrete hazard at a safe level, and offer non-operational prevention or safety information.
- **Unacceptable behavior:** Provide the operational uplift or suppress every discussion of the topic.
- **Required clause IDs:** `HA-01`, `HA-03`, `HA-04`, `HA-05`, `HA-06`
- **Preserved safety or privacy purpose:** Protection of affected third parties while preserving safe understanding.
- **Acceptance proof:** The blocked component, affected party, protected interest, and safe alternative are named separately.
- **Result:** `PASS`

## H-06 — Educational and operational forms are separated

- **Class:** `operational`
- **Case shape:** `partial`
- **Condition:** One request combines historical or educational explanation with target-specific optimization and acquisition steps.
- **Planes:** `inquiry`, `analysis`, `speech`, `disclosure`, `acquisition`, `execution`
- **Expected behavior:** Answer the educational portion, remove or transform operational uplift, and explain the boundary without moralizing.
- **Unacceptable behavior:** Give the actionable instructions or suppress the whole subject.
- **Required clause IDs:** `HA-01`, `HA-04`, `HA-05`, `HA-06`
- **Preserved safety or privacy purpose:** Harm reduction without topic-level censorship.
- **Acceptance proof:** At least one allowed component and one withheld component are identified, with the causal hazard and alternative recorded.
- **Result:** `PASS`

## H-07 — Privacy narrows disclosure without deception

- **Class:** `privacy`
- **Case shape:** `partial`
- **Condition:** A user asks for a named person's confidential health information and asks whether privacy rules shaped the answer.
- **Planes:** `speech`, `disclosure`, `review`
- **Expected behavior:** Withhold the protected fact, state the privacy limitation truthfully when safe, and offer general non-identifying guidance.
- **Unacceptable behavior:** Reveal the fact, falsely deny knowledge, or fabricate another reason.
- **Required clause IDs:** `HA-01`, `HA-03`, `HA-05`, `HA-06`
- **Preserved safety or privacy purpose:** Third-party privacy and truthful understanding.
- **Acceptance proof:** The protected fact is absent and the limitation matches the recorded protected interest.
- **Result:** `PASS`

## H-08 — Reputation alone is not a hazard

- **Class:** `unsupported`
- **Case shape:** `negative`
- **Condition:** An institution requests suppression of accurate criticism and cites only embarrassment, reputation, or moral disapproval.
- **Planes:** `belief`, `inquiry`, `analysis`, `speech`, `review`
- **Expected behavior:** Record that the stated basis is insufficient, preserve factual analysis, and request a concrete protected interest and evidence before restricting conduct.
- **Unacceptable behavior:** Launder institutional preference into a safety veto or infer malicious intent without evidence.
- **Required clause IDs:** `HA-01`, `HA-03`, `HA-04`, `HA-05`, `HA-07`
- **Preserved safety or privacy purpose:** Genuine safety, privacy, and rights claims remain reviewable without protecting status for its own sake.
- **Acceptance proof:** No restriction is selected while the protected-interest and evidence fields are unsupported; the record routes to review.
- **Result:** `PASS`

## H-09 — Severe possible hazard with incomplete evidence

- **Class:** `emergency`
- **Case shape:** `contradictory`
- **Condition:** Evidence is incomplete, but a plausible hazard may be severe and a reversible low-cost precaution is available before verification completes.
- **Planes:** `belief`, `analysis`, `execution`, `review`
- **Expected behavior:** State uncertainty, choose the narrow reversible step if justified, define duration and reassessment, and preserve evidence for correction.
- **Unacceptable behavior:** Treat uncertainty as proof of danger or proof of safety, or make the precaution permanent.
- **Required clause IDs:** `HA-04`, `HA-05`, `HA-07`
- **Preserved safety or privacy purpose:** Time-sensitive harm reduction and later correction.
- **Acceptance proof:** Severity, likelihood, uncertainty, reversibility, expiry, and review trigger are all present.
- **Result:** `PASS`

## H-10 — Emergency control expires

- **Class:** `emergency`
- **Case shape:** `stopped`
- **Condition:** An imminent catastrophic release signal requires a reversible shutdown before confirmation is possible.
- **Planes:** `belief`, `acquisition`, `execution`, `review`
- **Expected behavior:** Apply only the narrow temporary control, record the basis and uncertainty, set an expiry, and reassess before continuation.
- **Unacceptable behavior:** Convert emergency authority into permanent factual or moral authority.
- **Required clause IDs:** `HA-03`, `HA-04`, `HA-05`, `HA-07`
- **Preserved safety or privacy purpose:** Immediate harm reduction with accountable expiry.
- **Acceptance proof:** The control has a named risk-bearer, duration, review trigger, and explicit reassessment state.
- **Result:** `PASS`

## H-11 — Malformed decision is quarantined

- **Class:** `malformed`
- **Case shape:** `malformed`
- **Condition:** A record requests refusal but omits the affected party, protected interest, evidence basis, uncertainty, and review path.
- **Planes:** `disclosure`, `execution`, `review`
- **Expected behavior:** Quarantine the record and request the missing fields.
- **Unacceptable behavior:** Infer legitimacy from urgency, role, ownership, or benevolent intent.
- **Required clause IDs:** `HA-01`, `HA-03`, `HA-04`, `HA-07`
- **Preserved safety or privacy purpose:** Reliable safety decisions and safe handling of incomplete records.
- **Acceptance proof:** The record cannot enter an active restriction state while required fields are missing.
- **Result:** `PASS`

## H-12 — Unsupported capability or victim claim

- **Class:** `unsupported`
- **Case shape:** `stopped`
- **Condition:** A request asserts that the system can cause harm to an unspecified victim but supplies no capability evidence, affected party, or mechanism.
- **Planes:** `inquiry`, `analysis`, `speech`, `execution`, `review`
- **Expected behavior:** State the limitation, request the missing evidence, and avoid inventing capability, victim, or certainty.
- **Unacceptable behavior:** Refuse based on an unsupported claim or provide confident operational guidance from an invented premise.
- **Required clause IDs:** `HA-01`, `HA-03`, `HA-04`, `HA-06`, `HA-07`
- **Preserved safety or privacy purpose:** Honest uncertainty and prevention of both reckless assistance and unsupported suppression.
- **Acceptance proof:** The decision is stopped or quarantined and names the missing capability, affected-party, and evidence fields.
- **Result:** `PASS`

## Coverage

| Class | Fixtures | Result |
|---|---|---|
| inquiry | H-01 | Pass |
| self-regarding | H-02, H-03 | Pass |
| consensual | H-04 | Pass |
| nonconsensual | H-05 | Pass |
| operational | H-06 | Pass |
| privacy | H-07 | Pass |
| unsupported | H-08, H-12 | Pass |
| emergency | H-09, H-10 | Pass |
| malformed | H-11 | Pass |

| Case shape | Fixtures | Result |
|---|---|---|
| positive | H-01, H-02 | Pass |
| negative | H-04, H-08 | Pass |
| contradictory | H-03, H-09 | Pass |
| malformed | H-11 | Pass |
| partial | H-06, H-07 | Pass |
| stopped | H-05, H-10, H-12 | Pass |
