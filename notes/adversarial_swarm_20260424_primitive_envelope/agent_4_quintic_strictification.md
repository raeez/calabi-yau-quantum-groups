# Agent 4 Report: Quintic Strictification Attack

## Attacked Claim

Target: the quintic component of
`thm:cy3-universal-primitive-envelope` in
`chapters/theory/cy3_chain_level_bridge.tex`.

Aggressive reading tested the following possible overclaim:

> The platonic ideal resolution already realizes the compact analytic
> curved \(L_\infty/A_\infty\) transfer for the quintic \(X_5\), absorbs
> \(Y_3=5\), supplies an actual \(S^3\)-framing, completes the OPE, and
> compares the derived centre.

## Verdict

Rejected as a global theorem. Accepted only as a formal normal-form and
obstruction-envelope theorem.

The current material proves the free formal primitive envelope:
\[
  \widetilde{\mathfrak g}_j
  =
  \mathfrak g_j
  \widehat\oplus
  \prod_a \mathbb C h_{j,a}[n_{j,a}-1],
  \qquad d h_{j,a}=o_{j,a}.
\]
It does not realize the four compact quintic primitives in analytic
geometry. The strongest truthful theorem is:

> For \(X_5\), the finite oracle supplies a target normal form and a
> formal primitive envelope. The compact quintic theorem is equivalent
> to constructing, inside
> \(\mathrm{Def}_{\mathrm{an}}(\Perf(X_5),Y_3,S^3,\mathrm{OPE},
> Z^{\mathrm{der}}_{\mathrm{ch}})\), explicit analytic primitives for
> the Yukawa curvature, the chain-level \(S^3\)-framing, the OPE
> completion, and the derived-centre comparison.

## Failure Mode

RED. The theorem statement is honest at the top level: it labels itself
as "formal obstruction resolution; analytic realisation is the exact
remaining condition" at
`chapters/theory/cy3_chain_level_bridge.tex:2149`.
The proof kills obstruction classes only by adjoining free formal
generators; see `chapters/theory/cy3_chain_level_bridge.tex:2158` and
`chapters/theory/cy3_chain_level_bridge.tex:2208`. This is algebraic
closure in an enlarged dg complex, not compact analytic transfer.

BLUE. The local quintic paragraph in the same chapter says the actual
first obstruction is the non-formal Yukawa component \(Y_3=5\) before a
compact analytic curved primitive is chosen, and that the global theorem
still needs analytic transfer, actual \(S^3\)-framing, OPE completion,
and derived-centre comparison:
`chapters/theory/cy3_chain_level_bridge.tex:2018`.
The ledger says the same at
`chapters/theory/cy3_chain_level_bridge.tex:1882` and
`chapters/theory/cy3_chain_level_bridge.tex:1903`.

GREEN. The compute oracle has two layers. The finite normal-form
function `quintic_curved_witness()` sets zero strictification residuals,
`ope_completion=True`, and `derived_centre_comparison=True`
(`compute/lib/cy3_platonic_bridge.py:418`). But the primitive-envelope
API freely adjoins formal primitives with `analytic_realisation=False`
(`compute/lib/cy3_platonic_bridge.py:720`), and
`analytic_global_primitive_closure()` is false while all analytic
obligations remain listed (`compute/lib/cy3_platonic_bridge.py:751`).
Therefore the `quintic_curved_witness().closes()` boolean is a finite
normal-form closure, not a compact analytic realization certificate.

## Local Anchors

- `chapters/theory/cyclic_ainf.tex:178`: the quintic is a CY3 cyclic
  \(A_\infty\) input; the framed output requires the CY-A3 hypotheses,
  chosen \(S^3\)-framing data, and admissible specialization.
- `chapters/theory/cyclic_ainf.tex:239`: the \(d=3\) cyclic input
  statement is conjectural and explicitly says the chain-level
  \(S^3\)-framing is not automatic.
- `chapters/theory/cy3_chain_level_bridge.tex:1412`: the
  strictification tower has five components
  \(\omega_{\mathrm{cyc}},\omega_{S^3},\omega_{A_\infty},
  \omega_{\mathrm{CL}},\omega_{\mathrm{des}}\).
- `chapters/theory/cy3_chain_level_bridge.tex:1450`: the
  strictification criterion is formal deformation theory: a Stage-1
  object exists iff that obstruction tower vanishes.
- `chapters/theory/cy3_chain_level_bridge.tex:2018`: the quintic
  controlling complex is
  \(\mathrm{Def}_{\mathrm{an}}(\Perf(X_5),Y_3,S^3,\mathrm{OPE},
  Z^{\mathrm{der}}_{\mathrm{ch}})\), with \(Y_3=5\) as first
  obstruction before an analytic primitive is chosen.
- `chapters/theory/cy3_chain_level_bridge.tex:2149`: the universal
  primitive envelope is formal and becomes geometric only when realized
  by the named analytic objects.
- `chapters/theory/cy_to_chiral.tex:6917`: the quintic has a conditional
  Gepner CoHA candidate, not an unconditional \(\Phi_3\) output.
- `chapters/theory/cy_to_chiral.tex:10541`: the curved quintic target is
  a conjecture; \(Y_3=5+\mathrm{GW}\) obstructs strict Hopf closure.
- `chapters/theory/cy_to_chiral.tex:11956`: scalar shadow calculations
  do not construct the quintic \(\Phi_3\) output.

## Compute Anchors

- `compute/lib/cy3_platonic_bridge.py:92`: global witness requirements
  for the quintic are exactly compact analytic curved transfer,
  \(S^3\)-framing, OPE completion, and derived-centre comparison.
- `compute/lib/cy3_platonic_bridge.py:173`: the invalid shortcut is
  treating a finite non-formal normal form as compact analytic quintic
  strictification.
- `compute/lib/cy3_platonic_bridge.py:397`: the finite
  `QuinticCurvedWitness` records \(Y_3=5\) and booleans for OPE/centre,
  but not analytic kernels or chain maps.
- `compute/lib/cy3_platonic_bridge.py:667`: the primitive certificate
  separates formal killing from analytic realization.
- `compute/lib/quintic_shadow_tower.py:312`: the quintic
  strictification audit says no strict chain-level framing witness is
  constructed by the elementary data.
- `compute/lib/quintic_shadow_tower.py:337`: required quintic witnesses
  are cyclic nullhomotopy or curvature absorbing \(m_3\), negative
  cyclic lift compatible with \(S^3\), OPE completion, and
  derived-centre comparison.
- `compute/lib/A_BVDB_quintic_formality.py:322`: \(m_3\) is the Yukawa
  coupling; classical value is \(5\), and it is non-zero.
- `compute/lib/A_BVDB_quintic_formality.py:472`: the healed curved
  formality statement is conjectural, with Costello-Li BCOV as framework
  and the chain-level quasi-isomorphism still open.
- `compute/lib/compact_geometric_koszul_d3.py:376`: HKR matching does
  not imply chain-level Koszul duality.
- `compute/lib/compact_geometric_koszul_d3.py:430`: BCOV, LG mirror, and
  Bridgeland routes to the needed tilting/Kapranov object are all open.

## Exact Missing Primitives

1. \(\eta_{Y_3}\): a compact analytic curved \(L_\infty/A_\infty\)
   transfer primitive with \(d\eta_{Y_3}=Y_3\) in the quintic analytic
   deformation complex, not merely a finite residual set to zero.
2. \(\eta_{S^3}\): a chain-level \(S^3\)-framing witness compatible with
   the chosen negative-cyclic CY3 class and \(E_3\) formality point.
3. \(\eta_{\mathrm{OPE}}\): an admissible \((\Sigma_2,C)\) specialization
   with completed ordered OPE residues on the chiral output.
4. \(\eta_Z\): a continuous derived-centre comparison for the resulting
   framed \(E_1\)-chiral object, not a generic Drinfeld-centre slogan.
5. Compatibility: the four primitives must respect orientation,
   completion/topology, and gauge homotopies inside the same filtered
   deformation problem.

## Recommended Claim Status

- `thm:cy3-universal-primitive-envelope`: keep as
  `ProvedHere (formal obstruction resolution; analytic realization is
  the exact remaining condition)`.
- Quintic compact analytic strictification: `Conditional/Open`.
- `quintic_curved_witness().closes()`: read as `proved_normal_form`
  only. It should not be cited as compact analytic transfer.
- Curved formality of the quintic \(A_{\mathrm{BVDB}}\): `Conjectural`.
- Strict formality of \(A_{\mathrm{BVDB}}\): refuted by \(Y_3\neq0\).

## Tests And Computations Run

- `python -m pytest ...` failed because `python` is not on PATH.
- `python3 -m pytest compute/tests/test_cy3_platonic_bridge.py compute/tests/test_quintic_shadow_tower.py compute/tests/test_A_BVDB_quintic_formality.py compute/tests/test_quintic_e1_universality.py compute/tests/test_compact_geometric_koszul_d3.py -q`
  passed: `268 passed in 0.84s`.
- Oracle query:
  `frontier_realisation_package().gate_status()["quintic_curved_witness"]`
  is `True`, but
  `analytic_global_primitive_closure()` is `False`, and the remaining
  quintic obligations are exactly compact analytic curved transfer,
  \(S^3\)-framing, OPE completion, and derived-centre comparison.
- Quintic audit query: `strict_framing_witness_constructed=False`,
  `transferred_m3_vanishes=False`, strict formality `False`, curved
  status `CONJECTURAL`, chain-level Kapranov/Koszul sufficiency `OPEN`.

## Remaining Open Questions

1. Can Costello-Li BCOV quantization be upgraded to an explicit compact
   chain-level curved \(A_\infty\) quasi-isomorphism for \(A_{\mathrm{BVDB}}\)?
2. Can one construct the negative-cyclic lift together with an actual
   \(S^3\)-framing on \(D^b(\Coh(X_5))\), not just topological
   obstruction vanishing?
3. Can the Gepner/LG chart and the large-volume chart be glued to a
   completed OPE model on an admissible \((\Sigma_2,C)\)?
4. Can the chiral derived centre of that completed object be compared
   continuously with the Drinfeld centre of its \(E_1\)-representation
   category?

## Files Changed

- `notes/adversarial_swarm_20260424_primitive_envelope/agent_4_quintic_strictification.md`
