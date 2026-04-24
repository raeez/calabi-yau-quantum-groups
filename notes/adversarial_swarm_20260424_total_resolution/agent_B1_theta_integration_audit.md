# Agent B1 - second-pass integration audit of `Theta_{hCS->Hall}^{or}`

Date: 2026-04-24.

Scope audited exactly as requested:

- `chapters/theory/cy3_chain_level_bridge.tex`
- `notes/adversarial_swarm_20260424_total_resolution/agent_A1_theta_hcs_hall.md`

No manuscript source was edited.

## Verdict

The integrated obstruction/descent block is correct as a criterion, but a later
local-chart/K3xE block still asserts construction and gluing of
`\Theta_{hCS->Hall}` without the missing chartwise datum
`\theta_U`.  This contradicts the A1 report's core finding: the present sources
do not construct a continuous chain-level, multiplicative quasi-isomorphism
from renormalised hCS observables to oriented critical-CoHA chains.

## Checks That Pass

- `cy3_chain_level_bridge.tex:371-409` states the quantum bar-to-Hall
  comparison as conditional on an oriented map and a vanishing obstruction
  tuple.
- `cy3_chain_level_bridge.tex:522-652`,
  `def:cy3-oriented-hcs-hall-comparison-datum`, defines the comparison datum
  as actual maps `\Theta_\sigma` on every DWR/Ran simplex, not as formal
  notation.
- `cy3_chain_level_bridge.tex:654-701`,
  `thm:oriented-hcs-hall-comparison-from-dwr-datum`, is a sufficiency theorem
  from a supplied datum.  Lines `670-673` and `699-701` explicitly say it
  constructs no such datum.
- `cy3_chain_level_bridge.tex:738-771`,
  `prop:cy3-local-to-toric-descent-package`, is correctly conditional on a
  supplied comparison datum and chartwise maps `\Theta_U`.
- `cy3_chain_level_bridge.tex:1039-1097`,
  `op:cy3-hcs-hall-comparison`, keeps construction of the comparison open.
- `cy3_chain_level_bridge.tex:1099-1150`,
  `def:hcs-hall-descent-obstruction`, correctly defines the controlling
  complete filtered dg Lie algebra and the five obstruction components.
- `cy3_chain_level_bridge.tex:1152-1211`,
  `thm:hcs-hall-descent-criterion`, is a criterion: it starts with a chartwise
  family of quasi-isomorphisms `\theta_i` and proves extension iff the
  obstruction tuple vanishes.
- `cy3_chain_level_bridge.tex:1213-1228`,
  `rem:hcs-hall-one-chart-normalisation`, correctly says one-chart
  normalisation is tautological for `o_or`, `o_gr`, `o_TS`, `o_fact` only after
  local choices, and does not construct `\Theta`.
- A1 agrees: `agent_A1_theta_hcs_hall.md:46-55`,
  `261-280`, and `334-344` say the only genuine current vanishing is
  one-chart tautological vanishing of the four discrete/coherent classes, while
  `o_MC` and the chartwise `\theta_U` remain missing.

## Findings

### B1-1 - Critical - C3 five-way theorem constructs the missing map

Anchor:

- `cy3_chain_level_bridge.tex:2013-2031`,
  `thm:r6-quad-equivalence-c3`
- `cy3_chain_level_bridge.tex:2090-2150`, especially `2111-2120`
- A1 contradiction anchors: `agent_A1_theta_hcs_hall.md:114-128`,
  `252-280`, `340-341`

Problem:

The theorem asserts a chain-level quasi-isomorphism edge
`\Theta_{\hCS\to\Hall}^{\C^3}` and the proof claims an explicit map via
BV-equivariant localisation and Nakajima pullback.  A1's audit says the
Schiffmann-Vasserot/Kontsevich-Soibelman theorem identifies the Hall-side
algebra only; it does not define a continuous chain map from renormalised hCS
observables to vanishing-cycle Borel-Moore chains.

Minimal patch:

Replace `thm:r6-quad-equivalence-c3` by a conditional local normal-form
statement:

```tex
\ClaimStatusConditional{}
Assume a degree-zero continuous multiplicative chart map
\theta_{\C^3}: \Obs_{\hCS}^q(\C^3;\ghat)
  \to \CoHA_{\mathrm{crit}}^{\mathrm{or}}(\C^3)
whose Maurer--Cartan obstruction vanishes and whose cohomology reduction is
the SV/KS positive-half identification. Then the remaining Hall-side and
envelope edges identify the target with \(Y^+\) and its doubled
\(\mathcal W_{1+\infty}\) representation.
```

Move the localisation formula to "candidate for `\theta_{\C^3}`" unless a
proof is added that it is a continuous chain map, multiplicative, compatible
with BV differential, and a quasi-isomorphism.

### B1-2 - Critical - C3 base case is declared closed

Anchor:

- `cy3_chain_level_bridge.tex:2177-2196`,
  `rem:r6-op-closed-at-c3`
- A1 contradiction anchors: `agent_A1_theta_hcs_hall.md:257-280`,
  `340-341`

Problem:

The remark says Problem `op:cy3-hcs-hall-comparison` is closed at
`X=\C^3` by an explicit chartwise chain-level quasi-isomorphism realising all
seven local conditions.  A1 says no `\theta_U` is constructed even on the
one-chart normalised problem; the only proved local result is tautological
vanishing of the four non-Maurer-Cartan classes after the target choices are
fixed.

Minimal patch:

Retitle to "C3 target normal form and remaining local comparison datum" and
replace "closes" by "would close after a supplied `\theta_{\C^3}`".  State
that `CoHA(C^3)=Y^+` is the Hall-side target normal form, not the hCS-to-Hall
map.

### B1-3 - High - K3xE global Theta theorem depends on the unsupported C3 edge

Anchor:

- `cy3_chain_level_bridge.tex:2396-2421`,
  `thm:r6-k3e-local-chart-qiso-inscribed`
- `cy3_chain_level_bridge.tex:2423-2439`, especially `2428-2435`
- A1 contradiction anchors: `agent_A1_theta_hcs_hall.md:282-291`,
  `334-344`

Problem:

The theorem asserts chartwise quasi-isomorphisms `\Theta_i`, vanishing of all
five obstruction classes, and a global morphism
`\Theta_{\hCS\to\Hall}^{K3\times E}`.  Its proof kills `o_MC` by citing the
C3 five-way pentagon.  Since the C3 `\theta_U` is not constructed, this is not
a valid proof of the Maurer-Cartan obstruction or of global descent.

Minimal patch:

Convert this theorem to the already-valid conditional form:

```tex
\ClaimStatusConditional{}
Assume a quasi-isomorphic oriented hCS--Hall comparison datum on the K3xE DWR
nerve, with chartwise maps \(\Theta_i\) and vanishing obstruction tuple.  Then
Theorem~\ref{thm:hcs-hall-descent-criterion} gives the global morphism.
```

Do not claim `o_MC=0` until the chartwise maps are constructed and checked
against restrictions and products.

### B1-4 - High - K3xE obstruction vanishings conflate Hall-side structure with comparison vanishings

Anchor:

- `cy3_chain_level_bridge.tex:2304-2336`,
  `prop:r6-orientation-torsor-k3e-inscribed`
- `cy3_chain_level_bridge.tex:2338-2364`,
  `prop:r6-grading-thom-sebastiani-fact-k3e-inscribed`
- `cy3_chain_level_bridge.tex:2366-2394`
- A1 anchors: `agent_A1_theta_hcs_hall.md:143-160`,
  `175-209`, `282-291`

Problem:

The propositions prove, at most, Hall-side availability of orientation data,
internal Hall Thom-Sebastiani associativity, and source/target factorisation
structures.  A1 distinguishes these from the relative comparison obstructions:
`o_or`, `o_TS`, and `o_fact` measure transport through `\theta`, not merely
the existence of internal structures on each side.  Lines `2361-2362` and
`2392-2393` explicitly use `\Theta_{\hCS\to\Hall}` to prove factorisation
compatibility, so the proof is circular unless `\Theta` is supplied first.

Minimal patch:

Retype these as preparatory lemmas:

- Hall-side orientation datum exists on the stated cover, subject to the
  stated Kummer/Kunneth hypotheses.
- Hall Thom-Sebastiani associativity is internally coherent.
- Source and target each factorise over disjoint opens.

Then add: "These lemmas do not imply vanishing of
`o_or`, `o_TS`, or `o_fact` for the hCS-to-Hall comparison until a chartwise
comparison map is fixed."

### B1-5 - Moderate - The normal-form theorem compresses away the supplied-map hypothesis

Anchor:

- `cy3_chain_level_bridge.tex:1629-1658`,
  `thm:seven-rigidification-normal-form`
- `cy3_chain_level_bridge.tex:1637-1640`
- comparison datum definition: `cy3_chain_level_bridge.tex:1301-1305`

Problem:

Item (1) says `\Theta` exists exactly when the obstruction tuple vanishes.
Read with Definition `def:complete-cy3-bridge-datum`, this may be intended to
include a supplied degree-zero Maurer-Cartan element whose vertex maps are
quasi-isomorphisms.  In isolation it omits the first A1 obstruction: the
chartwise maps must exist before the tuple is meaningful.

Minimal patch:

Change item (1) to: "For a supplied chartwise degree-zero family whose
0-simplex maps are quasi-isomorphisms, `\Theta` exists on the full DWR nerve
exactly when ..."  This keeps the theorem a normal-form criterion rather than
an existence theorem.

## Summary

The descent theorem is not the problem.  The manuscript now has a good
criterion and a good one-chart normalisation warning.  The overclaim is the
later assertion that the missing local map has already been built on `C^3` and
therefore glues on `K3\times E`.  The minimal repair is to make the C3 and
K3xE local-chart sections conditional on an explicit chartwise
`\theta_U`, while preserving all Hall-side normal forms and all internal
orientation/Thom-Sebastiani/factorisation lemmas as preparatory structure.

No tests were run; this was a scoped textual proof audit.
