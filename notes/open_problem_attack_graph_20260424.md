# Open Problem Attack Graph, 2026-04-24

This note records the first-principles dependency graph for the live
Vol III gap surface.  It is not a status table.  Each row names the
primitive whose construction would turn a conditional or conjectural
surface into a theorem.

## Root Gate

The central obstruction is not the existence of local models.  The
local models exist in several lanes: toric CoHAs, the K3 Mukai
Heisenberg branch, Borcherds products, and finite normal forms.  The
root gate is promotion from local, numerical, or positive-half data to
global compact CY3 bridge data.

The manuscript now has a primitive criterion at
`chapters/theory/cy3_chain_level_bridge.tex`, Corollary
`cor:cy3-primitive-criterion`: a compact CY3 bridge theorem is
unconditional only after explicit primitives kill the obstruction
classes in the relevant deformation complex and satisfy the completion
and orientation compatibilities.

## Seven Primitive Families

| Family | First primitive | Main source anchor |
|---|---|---|
| Phi3 functoriality | Nullhomotopies for the triple-product class in the witnessed-kernel deformation dg Lie algebra, plus orientation, cyclic transfer, S3-framing, OPE completion, and convolution cells. | `chapters/theory/cy_to_chiral.tex`, Conjecture `conj:phi-d-functoriality`; `chapters/theory/cy3_chain_level_bridge.tex`, Proposition `prop:cy3-seven-first-obstruction-complexes`. |
| Compact Hall double / CY-C | Compact positive half, compact negative half, non-degenerate completed Hopf pairing after radical quotient, and continuous derived-centre transport. | `chapters/theory/cy3_chain_level_bridge.tex`, Proposition `prop:cy3-seven-first-obstruction-complexes`; `chapters/theory/gluing/sec_8_k3xe_master.tex`; `chapters/examples/k3e_bkm_chapter.tex`. |
| Oriented hCS-to-Hall | A continuous natural transformation on the whole DWR/Cech/Ran nerve whose Maurer-Cartan, orientation, grading, Thom-Sebastiani, and factorisation obstructions vanish. | `chapters/theory/cy3_chain_level_bridge.tex`, Problem `op:cy3-hcs-hall-comparison` and Theorem `thm:hcs-hall-descent-criterion`. |
| Quintic and strict compact CY3 | Compact analytic curved transfer absorbing the Yukawa component, plus actual S3-framing, OPE completion, and derived-centre comparison. | `chapters/examples/derived_categories_cy.tex`; `chapters/examples/cy_c_beyond_k3e_existence_obstruction.tex`; `chapters/theory/cy3_chain_level_bridge.tex`. |
| Hall-Drinfeld / Super-Yangian / BKM | PBW, coproduct, Borcherds-Serre ideal, centre, completion, and Hall-pairing primitives in the completed double-comparison complex. | `chapters/examples/k3_chiral_bialgebra_platonic.tex`; `chapters/examples/k3_yangian_chapter.tex`; `chapters/examples/k3_quantum_toroidal_chapter.tex`. |
| Holographic protected trace | A symmetric-monoidal protected-trace functor preserving products, orientations, and wall-crossing, not only a protected-index equality. | `chapters/connections/cy_holographic_datum_master.tex`; `chapters/theory/quantum_chiral_algebras.tex`. |
| Two-loop hCS counterterm | A Feynman/RG derivation of the same Yang-normalised counterterm computed by the algebraic oracle. | `chapters/theory/cy3_chain_level_bridge.tex`; compute engines for ZTE/YBE counterterms. |

## Quantitative Surface

The current metadata surface contains 632 non-final claims in Vol III:
312 Conditional, 310 Conjectured, and 10 Heuristic.  Keyword grouping of
those claims gives the following attack-density profile:

| Cluster | Count |
|---|---:|
| K3xE / BKM / double / Super-Yangian | 191 |
| kappa / BCOV / shadow / numerics | 67 |
| derived-centre / Hochschild / bar | 49 |
| Hall / hCS / CoHA bridge | 47 |
| holography / protected trace | 44 |
| Phi3 / functoriality / framing | 34 |
| higher-d CY4/CY5 | 12 |
| other geometric-Langlands/Yangian/frontier surfaces | 280 |

The high count in the last row is not independent of the root gate:
most of it factors through the same missing compact bridge primitives,
especially the Hall double, functorial Phi3, and protected-trace
comparisons.

## Explicit Open-Problem Layer

The source-level `openproblem` environments expose the hard endpoints.
Vol III has one open problem with an explicit `ClaimStatusOpen` tag:
the hCS-to-Hall comparison in
`chapters/theory/cy3_chain_level_bridge.tex`.  The remaining Vol III
`openproblem` environments are programme questions in
`chapters/theory/m3_b2_obstruction.tex` and
`chapters/examples/k3e_cy3_programme.tex`; they factor through the same
primitive families above.

The metadata registry is stale on this point: it reports no Vol III
`Open` claim because the generator does not currently extract
`openproblem` environments as claim records.  Vol I metadata records
three open Langlands gaps in `chapters/connections/concordance.tex`:
bar-cobar versus scattering, arithmetic descent, and formal versus
convergent.  Vol II metadata records one open Type-H existence problem
in `chapters/connections/relative_feynman_transform.tex`.

## Immediate Attack Rule

For any proposed repair, do not ask first whether the sentence should be
Conditional or Conjectured.  Ask which primitive is missing.  If the
primitive can be supplied in the current file, prove it.  If it cannot,
state the exact deformation complex and obstruction class, then route
the downstream claim through that named primitive.

## Platonic Integration Pointer

The post-lane integration graph is now in
`notes/platonic_ideal_resolution_20260424.md`.  It refines this attack
graph after the CY-A3, hCS-to-Hall, compact Hall double, `Y_osp`,
protected-trace, two-loop hCS, and CHL/Gritsenko normalization lanes.  The
surviving compact `K3 x E` obstruction vector is

```text
O_{K3xE} =
  (o_atlas, o_or, o_HN, o_TS,
   o_MC, o_gr, o_fact,
   o_prim, o_rad, o_Delta, o_pair, o_cent).
```

The critical overclaims named there have been repaired in the manuscript:
`thm:plat-Sp-K3E` is conditional at
`chapters/examples/k3e_bkm_chapter.tex:12718`, and
`thm:g-delta5-sp-k3-bialgebra` is conditional at
`chapters/theory/cy_to_chiral.tex:1566`.  The remaining work is not status
bookkeeping; it is construction of the named primitives: compact oriented
critical Hall cosheaf, oriented hCS-to-Hall transformation, finite-height
Hall radical/Serre/centre/associator vanishing, completed Hall-Drinfeld
double, protected trace functor, and the finite-renormalization principle
fixing the two-loop tangent term.
