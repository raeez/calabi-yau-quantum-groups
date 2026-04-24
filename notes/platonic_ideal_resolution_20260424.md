# Platonic Ideal Resolution: Remaining Primitive Obligation Graph

Date: 2026-04-24. Agent 6 integration scope only.

This note assumes the current swarm state: the framed CY-A3 object-level
construction, the hCS-to-Hall descent criterion, the compact Hall package,
the local `Y_osp` RTT presentation, and the CHL/Gritsenko normalization are
already on the table. It separates what is closed from the primitive data
still missing before the compact CY3 bridge and its BPS outputs can be stated
without hypotheses.

## Executive Verdict

The remaining frontier is not a new numerical normalization. It is the
construction of one compact oriented BPS datum on `K3 x E`:

```text
D_{K3xE} =
  (critical Hall cosheaf,
   oriented hCS-to-Hall transformation,
   primitive Hall seed and automorphic radical,
   completed Hall-Drinfeld double)
```

Equivalently, the exact obstruction vector

```text
O_{K3xE} =
  (o_atlas, o_or, o_HN, o_TS,
   o_MC, o_gr, o_fact,
   o_prim, o_rad, o_Delta, o_pair, o_cent)
```

must vanish. Every surviving chapter-level conditional theorem factors
through one or more entries of this vector.

## Absorbed Inputs

| Input lane | Current status | What it does not yet supply | Main anchors |
|---|---|---|---|
| CY-A3 / `Phi_3` | Framed object-level `E_1` construction on the witnessed locus. | Unrestricted morphism functoriality; compact non-formal CY3 strictification; global `G(C)`. | `chapters/theory/cy_to_chiral.tex:5968`, `chapters/theory/cy_to_chiral.tex:6047`, `chapters/theory/cy_to_chiral.tex:6073`, `chapters/theory/cy_to_chiral.tex:1959` |
| hCS-to-Hall | Descent criterion and obstruction complex are proved once chartwise data are supplied. | The global natural transformation `Theta^{or}_{hCS->Hall}` and nullhomotopies killing `(o_MC,o_or,o_gr,o_TS,o_fact)`. | `chapters/theory/cy3_chain_level_bridge.tex:1039`, `chapters/theory/cy3_chain_level_bridge.tex:1099`, `chapters/theory/cy3_chain_level_bridge.tex:1152`, `chapters/theory/cy3_chain_level_bridge.tex:1998` |
| Compact Hall package | Finite package and obstruction vector identified. | Oriented critical atlas, orientation branch, HN completion, Thom-Sebastiani coherence, negative half, Hopf pairing, radical quotient, center transport. | `notes/compact_k3e_hall_construction_package_20260424.md:7`, `notes/compact_k3e_hall_construction_package_20260424.md:24`, `notes/platonic_resolution_eight_obligations_20260424.md:41`, `notes/platonic_resolution_eight_obligations_20260424.md:258` |
| Local `Y_osp` completion | Local rank `(4,20)` RTT / theta-fixed presentation is explicit in the chapter. | Representation-theoretic identification with K3 CoHA and the compact Hall-Drinfeld completion. | `chapters/examples/k3_yangian_chapter.tex:3971`, `chapters/examples/k3_chiral_bialgebra_platonic.tex:5208`, `chapters/examples/k3_chiral_bialgebra_platonic.tex:5702` |
| CHL/Gritsenko normalization | Arithmetic normalization is closed: CHL `N in {1,2,3,4,6}` gives `\kappa_{\mathrm{BKM}}(\Phi_N)=c_N(0)/2`; Gritsenko-Clery triples are a separate scope, overlapping only at `Delta_5`. | Equivariant compact Hall realization for sibling `N>1` targets; no new correction to the weights is needed. | `chapters/examples/cy_d_kappa_stratification.tex:159`, `chapters/examples/cy_d_kappa_stratification.tex:2053`, `chapters/examples/cy_d_kappa_stratification.tex:4374`, `chapters/theory/cy_to_chiral.tex:1550` |

## Residual Six-Agent Consolidation

The second residual wave did not close the compact bridge. It sharpened the
primitive obstruction surface:

| Residual lane | Result | New anchor |
|---|---|---|
| Compact critical CoHA | Criterion only: a compact oriented critical Hall cosheaf on `K3 x E` exists exactly when `(o_atlas,o_or,o_HN,o_TS)=0`. Local PTVV/BBJ charts, product volume form, finite KS wall-crossing, and local Thom-Sebastiani do not imply it. | `chapters/theory/gluing/sec_9_obstructions.tex:1323`; `notes/platonic_compact_critical_coha_resolution_20260424.md` |
| hCS-to-Hall theta | The constructed witness is only the finite torus-fixed `C^3` positive-half map `theta^{fp,+}_{C3}`. The compact map still needs `o_theta^{ren}`, `o_theta^{des}`, `eta_MC`, `lambda_or`, `eta_gr`, `H_TS`, `H_fact`, and `Q`. | `notes/platonic_theta_hcs_hall_construction_20260424.md` |
| Finite-height Hall promotion | Character/PBW agreement is not enough. Promotion requires finite-height vanishing of Hall pairing radical, Serre kernel, primitive centre, and associator/completion defects `(R_H,S_H,C_H,A_H)` with compatible transitions. | `chapters/examples/k3e_bkm_chapter.tex:1572`; `notes/platonic_finite_height_hall_radical_20260424.md` |
| Super-Yangian all-order completion | Compute now separates finite evidence from the completed object: PBW flatness, continuous coproduct/antipode, universal `R`, all-order associator, reflection-centre-to-`Delta_5`, and the `zeta_8` divided-power integral form remain unproved. | `compute/lib/k3_super_yangian.py:306`; `notes/platonic_yosp_all_order_completion_20260424.md` |
| Protected trace | Protected-index equality is character-level only. A functorial bridge requires `P_X^{prot}`, an exact symmetric monoidal `Tr_X^{prot}`, Hall/OPE product compatibility, orientation coherence, KS-to-MC wall-crossing, and BKM denominator normalization. | `chapters/connections/cy_holographic_datum_master.tex:515`; `notes/platonic_protected_trace_functor_20260424.md` |
| Two-loop hCS counterterm | Local Feynman/RG subtraction recovers the pole-four `b=0` member only; it does not derive the Yang-normalised simple-pole tangent `b=A2`. A Ward/BRST/scheme principle fixing `b` is still missing. | `compute/lib/k3_hcs_6d_twoloop.py:600`; `notes/platonic_twoloop_hcs_counterterm_20260424.md` |

## Dependency Graph

### N0. Primitive Criterion

Status: proved as a criterion, not as a compact theorem.

First missing primitive: explicit primitives for every first obstruction in
the compact bridge deformation complexes.

Anchors:
- `chapters/theory/cy3_chain_level_bridge.tex:1882`
- `chapters/theory/cy3_chain_level_bridge.tex:1952`
- `chapters/theory/cy3_chain_level_bridge.tex:2116`

Outgoing dependencies: all nodes below.

### N1. Framed CY-A3 Object-Level Construction

Status: conditionally closed on framed, witnessed object-level inputs.

First missing primitive: a morphism-level `Phi_3` obstruction killer, namely
nullhomotopies for the triple-product class in
`g_{Phi3}(K)=Def(K;or,cyc,S3,OPE,circ)`, together with orientation,
cyclicity, `S_3`, OPE, and convolution cells.

Anchors:
- `chapters/theory/cy_to_chiral.tex:5985`
- `chapters/theory/cy_to_chiral.tex:5999`
- `chapters/theory/cy_to_chiral.tex:6082`
- `chapters/theory/cy3_chain_level_bridge.tex:1959`

Depends on: N0.

Feeds: N2, N6, N8. It does not by itself construct compact Hall data.

### N2. Oriented hCS-to-Hall Transformation

Status: open comparison; criterion proved.

First missing primitive: chartwise quasi-isomorphisms
`theta_i` on the DWR/Cech/Ran nerve and nullhomotopies killing

```text
(o_MC, o_or, o_gr, o_TS, o_fact).
```

The one-chart `C^3` normalization is insufficient; it only removes overlap
obstructions that do not exist on a one-chart cover.

Anchors:
- `chapters/theory/cy3_chain_level_bridge.tex:1039`
- `chapters/theory/cy3_chain_level_bridge.tex:1099`
- `chapters/theory/cy3_chain_level_bridge.tex:1152`
- `chapters/theory/cy3_chain_level_bridge.tex:1213`
- `notes/platonic_resolution_eight_obligations_20260424.md:104`
- `notes/platonic_theta_hcs_hall_construction_20260424.md`

Depends on: N0, N1, N3.

Feeds: N4, N5, N6, N8, N9.

### N3. Compact Oriented Critical Hall Cosheaf on `K3 x E`

Status: supplied-data conditional.

First missing primitive: an oriented `(-1)`-shifted critical atlas over the
DWR/Cech/Ran cover, with an orientation branch, HN sector completion, and
Thom-Sebastiani coherence:

```text
(o_atlas, o_or, o_HN, o_TS)=0.
```

Positive curve-stalk assembly is not this object.

Anchors:
- `notes/platonic_resolution_eight_obligations_20260424.md:41`
- `notes/compact_k3e_hall_construction_package_20260424.md:39`
- `chapters/theory/gluing/sec_9_obstructions.tex:1323`
- `notes/platonic_compact_critical_coha_resolution_20260424.md`
- `chapters/theory/gluing/sec_8_k3xe_master.tex:561`
- `chapters/theory/gluing/sec_8_k3xe_master.tex:592`
- `chapters/theory/gluing/sec_8_k3xe_master.tex:612`

Depends on: N0.

Feeds: N2, N4, N5, N9.

### N4. Hall-Borcherds / Primitive Automorphic Seed

Status: arithmetic/root-multiplicity side proved; Hall algebra comparison
conditional.

First missing primitive: a Hall-to-Borcherds bracket map identifying the
primitive compact Hall motive with the `phi_{0,1}` seed, plus the automorphic
radical quotient:

```text
(o_prim, o_rad)=0.
```

The denominator identity fixes the target root multiplicities; it does not
construct the source Hall primitive or the algebra map.

Anchors:
- `notes/platonic_resolution_eight_obligations_20260424.md:203`
- `notes/compact_k3e_hall_construction_package_20260424.md:51`
- `notes/compact_k3e_hall_construction_package_20260424.md:87`
- `chapters/examples/k3e_bkm_chapter.tex:1572`
- `notes/platonic_finite_height_hall_radical_20260424.md`
- `chapters/examples/cy_d_kappa_stratification.tex:2053`
- `chapters/examples/k3e_bkm_chapter.tex:13680`

Depends on: N2, N3, N7.

Feeds: N5, N6, N8, N9.

### N5. Compact Hall-Drinfeld Double / CY-C

Status: main compact CY-C frontier; not constructed by positive-half data.

First missing primitive: the completed negative half, Cartan completion,
continuous coproduct, nondegenerate Hopf pairing after radical quotient,
and continuous derived-center transport:

```text
(o_Delta, o_pair, o_cent)=0.
```

Anchors:
- `notes/platonic_resolution_eight_obligations_20260424.md:258`
- `notes/compact_k3e_hall_construction_package_20260424.md:63`
- `chapters/theory/cy3_chain_level_bridge.tex:1977`
- `chapters/theory/gluing/sec_8_k3xe_master.tex:598`

Depends on: N3, N4.

Feeds: N6, N8, N9.

### N6. `Y_osp` / Super-Yangian Completion

Status: local RTT model explicit; compact Hall-Drinfeld/Super-Yangian
identification conditional.

First missing primitive: a representation-theoretic identification of the
local rank `(4,20)` theta-fixed RTT algebra with the compact K3/K3xE Hall
object, including PBW linear independence and flatness in the completed Hall
quotient, coproduct, center, completion, and Hall-pairing compatibility.

Anchors:
- `chapters/examples/k3_yangian_chapter.tex:3971`
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:5208`
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:5404`
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:5702`
- `compute/lib/k3_super_yangian.py:306`
- `notes/platonic_yosp_all_order_completion_20260424.md`
- `chapters/theory/cy3_chain_level_bridge.tex:2032`

Depends on: N4, N5.

Feeds: N8, N9.

### N7. CHL/Gritsenko Normalization

Status: closed arithmetic normalization.

First missing primitive: none on the numerical side. The remaining primitive
for sibling `N>1` geometries is equivariant compact realization:

- `N=2`: equivariant hCS-to-Hall and `g_2`-equivariant specialization.
- `N=3,4,6`: equivariant CoHA/shuffle lift, cycle `Sigma_2^(N)`, and
  Hall-Borcherds denominator comparison.
- `N=5,7,8`: Gritsenko 1994 arithmetic exists, but the smooth CY3 host is
  still conjectural in this programme.

Anchors:
- `chapters/examples/cy_d_kappa_stratification.tex:159`
- `chapters/examples/cy_d_kappa_stratification.tex:199`
- `chapters/examples/cy_d_kappa_stratification.tex:2053`
- `chapters/examples/cy_d_kappa_stratification.tex:2228`
- `chapters/examples/cy_d_kappa_stratification.tex:4374`
- `chapters/theory/cy_to_chiral.tex:1550`
- `chapters/theory/cy_to_chiral.tex:1618`
- `notes/wave_residuals/agent_R_1_8form_reconciliation.tex:1416`

Depends on: no compact bridge primitive for the arithmetic claim.

Feeds: N4, N8, N9.

### N8. Bialgebra / Associator / R-Matrix Transport

Status: conditional on compact Hall comparison and double data.

First missing primitive: transport of coproduct, associator, universal
`R`-matrix, center, completion topology, and Borcherds grading through the
compact Hall-Drinfeld/BKM comparison.

Anchors:
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:5458`
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:5529`
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:5583`
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:5629`
- `notes/adversarial_swarm_20260424_total_resolution/agent_A6_k3e_hb_holography.md:111`

Depends on: N4, N5, N6.

Feeds: N9.

### N9. Holographic Protected Trace

Status: arithmetic coefficients and asymptotics are theorem-grade; physical
trace comparison remains conditional.

First missing primitive: a symmetric-monoidal protected-trace functor
preserving products, orientations, and wall-crossing, together with the
boundary/Hall trace comparison.

Anchors:
- `chapters/theory/cy3_chain_level_bridge.tex:2047`
- `chapters/examples/k3e_bkm_chapter.tex:13717`
- `chapters/examples/k3e_bkm_chapter.tex:13753`
- `notes/adversarial_swarm_20260424_total_resolution/agent_A6_k3e_hb_holography.md:186`
- `chapters/connections/cy_holographic_datum_master.tex:515`
- `chapters/connections/cy_holographic_datum_master.tex:598`
- `notes/platonic_protected_trace_functor_20260424.md`

Depends on: N2, N5, N8.

### N10. Two-Loop hCS Counterterm

Status: algebraic Yang-normalized counterterm can be checked separately;
hCS Feynman/RG derivation remains open.

First missing primitive: a local functional `CT2^{Feyn/RG}` whose image under
the YBE comparison equals the algebraic `CT2^{Yang}` class:

```text
[rho_YBE(CT2^{Feyn/RG}) - CT2^{Yang}] = 0.
```

Anchors:
- `chapters/theory/cy3_chain_level_bridge.tex:2062`
- `chapters/theory/cy3_chain_level_bridge.tex:2080`
- `compute/lib/k3_hcs_6d_twoloop.py:600`
- `compute/tests/test_k3_hcs_6d_twoloop.py:203`
- `notes/platonic_twoloop_hcs_counterterm_20260424.md`

Depends on: N2 only for global hCS-to-Hall use; local algebra can proceed
out of order.

## Proposed Attack Order

1. Lock N7 as the arithmetic normalization oracle. Do not reopen the
   CHL/Gritsenko weights unless a primary-source conflict appears.
2. Repair statements that currently claim algebra-level closure from
   character-level or conditional data. This is status repair, not a new
   mathematical primitive.
3. Construct N3 first: oriented compact critical Hall cosheaf on `K3 x E`.
   Without this, neither N2 nor N5 has a compact target.
4. Construct N2 on the same cover: local maps plus nullhomotopies for
   `(o_MC,o_or,o_gr,o_TS,o_fact)`.
5. Use N2 and N3 to attack N4: primitive Hall seed, automorphic radical, and
   Hall-to-Borcherds bracket map.
6. Build N5: negative half, Cartan completion, continuous Hopf pairing,
   radical quotient, coproduct, and center transport.
7. Only then promote N6/N8 from formal-current and local RTT statements to
   compact Hall-Drinfeld/Super-Yangian bialgebra statements.
8. After N8, attack N9. Holography should remain split into arithmetic
   theorem and conditional physical trace until this point.
9. Treat N10 as a parallel local computation lane. It can be solved early,
   but it does not close the compact bridge without N2.

## Out-of-Order Shortcuts

- The `C^3` and toric local hCS-to-Hall normalizations can be proved before
  compact `K3 x E`; they are useful regression tests for N2, not substitutes
  for N2.
- The `Delta_5`/`Phi_10` arithmetic lane is already strong enough to anchor
  N7 and constrain N4. It should not be used to infer N5.
- The local `Y_osp` RTT lane can continue independently of compact Hall data.
  Its deliverable is the explicit local algebra, not the compact Hall double.
- Pure protected-index asymptotics can be stated as arithmetic/holographic
  evidence before N9. The protected-trace functor must remain conditional.
- The two-loop algebraic YBE oracle can be verified before the hCS/RG
  derivation, provided the statement is labeled as algebraic.

## Contradictions and Overclaim Candidates Found

1. Repaired chapter inconsistency:
   `chapters/examples/k3e_bkm_chapter.tex:12718` now marks
   `thm:plat-Sp-K3E` conditional. The Mukai-Heisenberg factor remains
   theorem-grade; the BPS tensor factor is routed through the compact Hall
   comparison and finite-height promotion data.

2. Repaired bialgebra overclaim:
   `chapters/theory/cy_to_chiral.tex:1566` now marks
   `thm:g-delta5-sp-k3-bialgebra` conditional on the compact Hall promotion
   package: oriented hCS-Hall witness, finite-height Hall-Drinfeld promotion,
   and all-order bialgebra transport of the BL-2/4/6 comparison.

3. Tightened verification-surface watch:
   `chapters/examples/k3_yangian_chapter.tex:4004` and
   `chapters/examples/k3_yangian_chapter.tex:4057` now make the rank-`(4,20)`
   Gauss/Drinfeld-new extraction and MO residue comparison conditional on the
   local MO stable-envelope scope and the rank-`(4,20)` Mukai super-`R`
   verification of Theorem `thm:r10-super-YBE-ch`. The finite local RTT
   presentation remains a useful local algebra, not a compact Hall double.

## Exact Remaining Primitive Obligations

1. Produce the compact oriented critical Hall cosheaf on `K3 x E`:
   `(o_atlas,o_or,o_HN,o_TS)=0`.
2. Produce `Theta^{or}_{hCS->Hall}` on the DWR/Cech/Ran nerve:
   `(o_MC,o_or,o_gr,o_TS,o_fact)=0`.
3. Identify the primitive compact Hall motive with the `phi_{0,1}` seed and
   construct the automorphic radical quotient:
   `(o_prim,o_rad)=0`.
4. Construct the completed Hall-Drinfeld double:
   negative half, Cartan completion, coproduct, nondegenerate completed Hopf
   pairing after radical quotient, and center transport:
   `(o_Delta,o_pair,o_cent)=0`.
5. Prove the compact Hall-BKM/Super-Yangian PBW and bialgebra package:
   PBW linear independence, flatness, Borcherds-Serre ideal compatibility,
   coproduct, associator, `R`-matrix, completion, center, Hall-pairing.
6. Prove `Phi_3` morphism functoriality beyond the witnessed framed locus by
   killing the triple-product obstruction and higher convolution coherences.
7. For CHL siblings, add equivariant compact Hall/hCS realizations; do not
   change the already-normalized `\kappa_{\mathrm{BKM}}=c_N(0)/2` arithmetic.
8. Construct the protected-trace functor for the physical/holographic bridge.
9. Derive the two-loop hCS counterterm from Feynman/RG analysis, not only from
   the Yang-normalized algebraic oracle.
