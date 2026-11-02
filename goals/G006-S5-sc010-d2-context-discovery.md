# G006-S5 — SC-010-D2 context-and-principle interaction discovery

Status: Complete — deferred attribution; routed to G006-S5R
Parent: G006 — Authority and Incentives
Depends on: G006-S4 no-promotion decision
Consumer: G006 candidate repair decision

## Objective

Determine whether the exact-replacement candidate's SC-010-D2 failure is
caused by MAP-002, the other replacement set, their interaction, or sampling
variance before drafting another replacement sentence.

## Hypothesis

The D2 failure is caused by an interaction among the mapped authority/incentive
principles and the supplied audit packet, not by packet serialization loss.
Disconfirming evidence is a no-replacement control that performs equivalently
to the edited arms across replicated draws, or a result that varies together
across all cells.

## Scope and limits

- Use the existing D2 packet, source hash, candidate maps, message builder, and
  recorded outputs first.
- Build a small 2x2 constitution probe only after an offline preflight defines
  the cells and cost ceiling.
- Do not edit MAP-002, start G007, run the 140-case pass, or read held-out data
  in the discovery slice.

## Unlock

A passing discovery identifies one causal interaction and a falsifier for a
single bounded repair goal. This slice found a directional association but not
enough replication to distinguish it from provider variance, so it routes to
`G006-S5R` rather than another constitutional edit.

## Stop condition

Stop if the evidence cannot distinguish behavior from measurement, if more than
one principle edit would be required for attribution, or if the cheapest valid
probe exceeds the approved budget. The first probe reached that stop condition
after one draw per cell; no wording was changed.
