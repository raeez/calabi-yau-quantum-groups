# Agent 07 -- Costello axis: BV, derived critical atlases, factorisation

Scope: hostile audit of the local CY3 potential \(W\), vanishing cycles,
orientation data, Costello--Gwilliam locality, and the bridge from the
CoHA positive half to \(\PhiFA_3\).  No manuscript file is edited.

## Verdict

The local toric/C3 Hall statement is theorem-grade:
\[
  \CoHA(\mathbb C^3) \cong Y^+(\widehat{\mathfrak{gl}}_1)
\]
as an associative \(E_1\) Hall algebra / positive half.  The Costello
BV/factorisation side supplies a theorem-grade local observable grammar
only after its BV hypotheses are fixed.  The map identifying this hCS
factorisation object with the oriented critical CoHA is not proved in
general.  It is the open oriented comparison
\[
  \Theta_{\hCS\to\Hall}^{\mathrm{or}}
  \colon \Obs_{\hCS}^{q}(-,\mathfrak g)
  \longrightarrow \CoHA_{\mathrm{crit}}^{\mathrm{or}}(-).
\]
Consequently, every statement moving from \(\PhiFA_3\) to a Hall
positive half must either be restricted to the constructed \(\mathbb C^3\)
chart, or carry the hypotheses: oriented derived critical atlas, KS/Joyce
orientation data, anomaly-cancelled hCS BV observables, Dolbeault/Weiss
descent, Thom--Sebastiani compatibility, completion, and a nondegenerate
Hall pairing if a Drinfeld double is invoked.

## Local anchors

- `chapters/theory/quantum_groups_foundations.tex:15-60`: effective BPS
  positive geometry includes orientation data, a derived critical atlas,
  and the vanishing-cycle complex \(\phi_W\); without such an atlas the
  datum is not constructed.
- `chapters/theory/quantum_groups_foundations.tex:80-126`: positive half
  \(Y^+_\sigma(X)=H^\bullet_{\rm eq}(\Meff_\sigma(X),\phi_W)\);
  Drinfeld double conditional on oriented atlas, PBW integrality, and
  nondegenerate pairing.
- `chapters/theory/quantum_groups_foundations.tex:550-568`: C3 equality
  \(\CoHA(\mathbb C^3)=Y^+(\widehat{\mathfrak{gl}}_1)\), then double,
  then evaluation to the \(\mathcal W\)-vacuum module.
- `chapters/examples/coha_wall_crossing_platonic.tex:92-162`: path
  algebra, Ginzburg dg algebra, critical CoHA, and bar complex are
  distinct; \(\partial_W^2=0\) belongs to \(\Pi(Q,W)\), not to CoHA.
- `chapters/examples/coha_wall_crossing_platonic.tex:297-371`: chiralisation
  preserves algebra-side structure; CoHA embeds as a positive-half
  algebra only under the stated local CY3/toric hypotheses.
- `chapters/examples/coha_wall_crossing_platonic.tex:703-733`: the
  \((\PhiFA_3)_*\) bridge is constructed for \(\mathbb C^3\) and
  conjectural beyond the named toric/gluing locus.
- `chapters/theory/cy_to_chiral.tex:225-305`: \(\PhiFA_d\) is a three-step
  construction: formality, Costello--Gwilliam topological locality,
  Costello--Li holomorphic BV refinement.
- `chapters/theory/cy_to_chiral.tex:340-409`: Stage-1 \(\PhiFA_3\) is
  pinned only after a \(\mathrm{GRT}_1(\mathbb Q)\)-torsor point is fixed;
  CFG ordinary Chern--Simons is an analogue, not the hCS-to-Hall theorem.
- `chapters/theory/cy_to_chiral.tex:640-675`: 5d hCS BV observables give a
  Stage-1 realisation under their own hCS hypotheses and after topological
  compactification.
- `chapters/theory/cy_to_chiral.tex:2699-2758`: the C3 chain verifies the
  Hall/representation side and keeps the hCS-to-Hall comparison separate.
- `chapters/theory/cy3_chain_level_bridge.tex:337-385`: the open problem
  lists the six conditions for \(\Theta_{\hCS\to\Hall}^{\mathrm{or}}\).

## ATTACK/HEAL cycle 1: local potential \(W\)

ATTACK.  The notation \(W\) is dangerous if read as a global potential on
a smooth CY3.  The manuscript's proved Hall input is local: a quiver with
potential \((Q_U,W_U)\), trace potential \(\mathrm{Tr} W_{\mathbf d}\) on
representation spaces, and a critical locus.  For \(\mathbb C^3\), the
local quiver potential is explicitly the tripled Jordan/Klebanov--Witten
form \(W=\mathrm{tr}(abc-acb)\), also written
\(W=X_1[X_2,X_3]\).  General compact CY3 targets do not automatically
come with such a global \(W\).

HEAL.  State \(W\) only as local chart data in a derived critical atlas:
\[
  \Meff_\sigma(X)=
  \coprod_{\gamma\in\Gamma^+_{\rm eff,\sigma}}
  \mathcal M_\sigma(\gamma),
  \qquad
  \mathcal M_\sigma(\gamma)|_U
  \simeq [\mathrm{Crit}(\mathrm{Tr} W_{U,\mathbf d})/G_{\mathbf d}].
\]
The local C3 potential is theorem-grade; the existence of a compatible
critical atlas for non-toric compact CY3s is a hypothesis.  The phrase
"the local CY3 potential \(W\)" must mean this chartwise trace-potential
package, not a global function on \(X\).

Insertion text:

```tex
Here \(W\) denotes a chartwise quiver potential in an oriented derived
critical atlas.  On a chart \(U\) the Hall input is
\([\Crit(\Tr W_{U,\mathbf d})/G_{\mathbf d}]\); no global potential on
the smooth Calabi--Yau threefold is asserted.  The \(\mathbb C^3\) chart
is the tripled Jordan quiver with cubic potential, while a compact
non-toric \(X\) requires the atlas as an additional hypothesis.
```

## ATTACK/HEAL cycle 2: vanishing cycles

ATTACK.  Vanishing cycles are being asked to do two incompatible jobs:
they define the critical CoHA, but they do not give the CoHA an internal
differential.  The identity \(\partial_W^2=0\) lives in the Ginzburg dg
algebra \(\Pi(Q,W)\).  The critical CoHA is already the cohomology with
vanishing-cycle coefficients; it is a graded Hall algebra.

HEAL.  Keep three layers separate:
\[
  \Pi(Q,W) \quad \text{dg algebra with } \partial_W^2=0,
\]
\[
  \CoHA(Q,W)=\bigoplus_{\mathbf d}
  H^\bullet_{G_{\mathbf d}}(\mathrm{Rep}(Q,\mathbf d),\phi_{W_{\mathbf d}})
  \quad \text{graded associative Hall algebra},
\]
\[
  B^{\rm ord}(\CoHA) \quad \text{bar dg coalgebra}.
\]
Only the first and third carry differentials.  The positive half
\(Y^+_\sigma(X)\) is vanishing-cycle cohomology with Hall product when
the critical correspondence is available.

Insertion text:

```tex
The sheaf \(\phi_W\) is a coefficient system for the critical Hall
construction.  After Borel--Moore/equivariant cohomology is taken,
\(\CoHA(Q,W)\) is a graded associative algebra.  Differential identities
belong either to \(\Pi(Q,W)\) through \(\partial_W^2=0\), or to the bar
coalgebra \(B^{\rm ord}(\CoHA)\), not to an internal CoHA differential.
```

## ATTACK/HEAL cycle 3: orientation data

ATTACK.  The positive half is not well-defined with the signs needed for
Hall multiplication, Thom--Sebastiani, or the Drinfeld pairing unless
orientation data are part of the input.  Writing \(\phi_W\) without the
orientation line hides the KS/Joyce square root of the virtual determinant
line and its overlap coherences.

HEAL.  Build the orientation into the object.  The local target of the
hCS-to-Hall comparison must be
\[
  \CoHA_{\rm crit}^{\rm or}(U)=
  \bigoplus_{\mathbf d}
  H^{\rm BM}_{G_{\mathbf d}}
  \left(
    \Crit(\Tr W_{\mathbf d}),
    \phi_{\Tr W_{\mathbf d}}\otimes \mathscr L_{o_U}
  \right),
\]
with shifts and Tate twists fixed.  The orientation \(o_U\) must be a
determinant-line square root compatible with extensions and overlaps,
not a formal decoration.  This is exactly why
\(\Theta_{\hCS\to\Hall}^{\rm or}\) remains an open lemma in general.

Insertion text:

```tex
All Hall-positive-half statements are made in the oriented critical
normalisation.  The coefficient is
\(\phi_{\Tr W_{\mathbf d}}\otimes\mathscr L_{o_U}\), where \(o_U\) is a
KS/Joyce square root of the virtual determinant line, equipped with
extension and overlap coherences.  The comparison must kill the residual
\(\mathbb Z/2\) orientation cocycle on triple overlaps.
```

## ATTACK/HEAL cycle 4: Costello--Gwilliam locality

ATTACK.  Costello--Gwilliam locality can be overread as proving the whole
CY3 Hall bridge.  It does not.  It assembles local observables into a
factorisation algebra, and Costello--Li supplies the holomorphic BV
refinement under a Calabi--Yau form and anomaly hypotheses.  CFG ordinary
3d Chern--Simons is a topological analogue; it does not identify the
Dolbeault hCS object on a complex threefold with critical CoHA.

HEAL.  Record the precise three-step Stage-1 theorem:

1. Kontsevich--Tamarkin formality promotes the Hochschild/Gerstenhaber
   input to an \(E_3\)-algebra after choosing a formality/associator point.
2. Costello--Gwilliam locality assembles the \(E_3\)-algebra into a
   topological \(E_3\)-factorisation algebra on the underlying space.
3. Costello--Li holomorphic locality plus \(\Omega_X\) and BV data refine
   it to an \(E_3\)-holomorphic factorisation algebra on the verified
   \(d=3\) locus.

Theorem status: steps 1 and 2 are source-theorem inputs under the stated
H1--H4 hypotheses; step 3 is anomaly/framing-gated at \(d=3\); the
hCS-to-Hall comparison is a separate open map.

Insertion text:

```tex
Costello--Gwilliam locality supplies the factorisation-algebra
local-to-global step.  It does not, by itself, construct the Hall model.
The Hall comparison is the additional oriented quasi-isomorphism
\(\Theta_{\hCS\to\Hall}^{\rm or}\), required to identify the hCS
factorisation observables with the oriented critical CoHA.
```

## ATTACK/HEAL cycle 5: BV/factorisation hCS realisation

ATTACK.  The 5d hCS route can be misread as an unconditional proof of
\(\PhiFA_3(\Perf(X))=\CoHA(X)\).  The local BV action requires a
Calabi--Yau form, metric gauge dg-Lie algebra, compact-support convention,
anomaly cancellation, and a topological compactification along the
\(\mathbb R_t\)-direction before it is compared with the Stage-1 object.
Even then it gives the Costello side, not the Hall side.

HEAL.  The exact BV hypotheses are:

- \(X\) smooth complex CY3 with chosen \(\Omega_X\);
- a finite-dimensional metric or reductive gauge dg-Lie algebra
  \(\mathfrak g\) with invariant pairing;
- hCS superfield
  \(\mathcal A\in\Omega^{0,\bullet}(X)\otimes\Omega^\bullet(\mathbb R_t)
  \otimes\mathfrak g[1]\);
- action \(S=\int_{X\times\mathbb R_t}\Omega_X\wedge
  \operatorname{tr}(\mathcal A\bar\partial_X\mathcal A+
  \mathcal A d_t\mathcal A+\frac23\mathcal A^3)\);
- a cancelled local anomaly and defined quantum observables;
- factorisation homology over \(\mathbb R_t\) before Stage-2
  \(\SpCh_{\Sigma_2,C}\).

The theorem-grade conclusion is a Costello-side factorisation statement.
The Hall-positive-half conclusion requires \(\Theta_{\hCS\to\Hall}^{\rm or}\).

Insertion text:

```tex
The 5d hCS realisation is a Stage-1 Costello model: after
\(\int_{\mathbb R_t}\) it identifies the hCS holomorphic factor with the
same \(\PhiFA_3\)-type observable object.  It is not a proof that
\(\PhiFA_3\) equals the critical CoHA.  The latter is precisely the
oriented hCS-to-Hall comparison problem.
```

## ATTACK/HEAL cycle 6: CoHA positive half to \(\PhiFA_3\)

ATTACK.  The sentence "\(\CoHA(\mathbb C^3)=Y^+\), hence \(\PhiFA_3\)
produces \(Y^+\)" reverses the direction of the construction.  The
Schiffmann--Vasserot theorem is a Hall-side theorem.  The Stage-1
factorisation object lives on the hCS/CY-to-chiral side.  The arrow
between them is not formal; it is \(\Theta_{\hCS\to\Hall}^{\rm or}\).

HEAL.  Use the typed bridge:
\[
  \PhiFA_3(\mathcal C)
  \dashrightarrow \CoHA_{\rm crit}(X)
  \xrightarrow{\rm SV/KS} Y^+
  \xrightarrow{D} \mathcal D(Y^+)
  \xrightarrow{\rm eval} \mathcal W_{1+\infty}\text{-vacuum}.
\]
At \(\mathbb C^3\), the Hall-side equality \(\CoHA(\mathbb C^3)=Y^+\)
is proved elsewhere and the representation/evaluation chain is proved
elsewhere.  The dashed arrow is the missing comparison.  In toric charts
the bridge is conditional on RSYZ plus chart gluing; for compact non-formal
CY3s it is open.

Insertion text:

```tex
The equality \(\CoHA(\mathbb C^3)=Y^+(\widehat{\mathfrak{gl}}_1)\) is
the Hall-side terminal chart.  It becomes a \(\PhiFA_3\)-statement only
after the oriented comparison
\(\Theta_{\hCS\to\Hall}^{\rm or}\) identifies the hCS Stage-1
factorisation object with the critical Hall factorisation cosheaf.
```

## ATTACK/HEAL cycle 7: \(E_1\), \(E_2\), double, and \(\mathcal W\)

ATTACK.  The bridge can silently promote an associative positive half to
a vertex algebra or to an \(E_2\)-chiral object.  That is false at \(d=3\).
The direct output is \(E_1\)-chiral / associative.  The \(E_2\)-braiding
lives on the Drinfeld centre of the representation category, and the
\(\mathcal W_{1+\infty}\) comparison is an evaluation image of the full
double, not of \(Y^+\) alone.

HEAL.  State the layers:
\[
  \CoHA(\mathbb C^3)=Y^+(\widehat{\mathfrak{gl}}_1)
  \quad (E_1\text{-associative positive half}),
\]
\[
  D(Y^+) = Y^- \otimes Y^0 \otimes Y^+
  \quad (\text{full affine Yangian after Hopf pairing}),
\]
\[
  Y(\widehat{\mathfrak{gl}}_1)
  \to \mathrm{End}(\mathcal W_{1+\infty}[\lambda]\text{-vac})
  \quad (\text{evaluation representation}).
\]
For general \(X\), the Drinfeld double is conditional on a PBW theorem,
completion, and nondegenerate Hall/stable-envelope pairing.

Insertion text:

```tex
At \(d=3\) the positive half is an \(E_1\)-Hall algebra.  The braided
\(E_2\)-structure appears only after passing to
\(\mathcal Z(\Rep^{E_1}(A_X))\).  The \(\mathcal W_{1+\infty}\) comparison
is an evaluation representation of the Drinfeld double, not an
identification of \(\CoHA\) or \(Y^+\) with a vertex algebra.
```

## Status table

| Claim | Status | Exact boundary |
|---|---|---|
| Local C3 quiver potential and critical CoHA | proved elsewhere / locally used | tripled Jordan chart, trace potential, SV/KS model |
| \(\CoHA(\mathbb C^3)=Y^+(\widehat{\mathfrak{gl}}_1)\) | proved elsewhere | associative \(E_1\) positive half, not \(\mathcal W_{1+\infty}\) |
| \(\PhiFA_3\) Stage-1 construction | theorem on verified H1--H4/framed loci | formality point, CY form, Costello--Li BV witness required |
| Costello--Gwilliam locality | proved elsewhere as locality/factorisation input | not a Hall comparison theorem |
| 5d hCS BV route | theorem/conditional on hCS BV hypotheses | identifies Costello-side Stage-1 model after compactification |
| \(\Theta_{\hCS\to\Hall}^{\rm or}\) | open in general | requires orientation, descent, bracket/product, C3 reduction, double/evaluation compatibility, Thom--Sebastiani |
| Drinfeld double \(D(Y^+_\sigma(X))\) | conditional | PBW integrality, completion, nondegenerate pairing |
| Global \(G(X)\) for compact non-toric CY3 | conjectural / conditional | not produced by CY-A3 or by CFG |

## Consolidated insertion block

```tex
\paragraph{Costello--Hall comparison hypothesis.}
The Stage-1 object \(\PhiFA_3(\mathcal C)\) and the critical Hall
positive half live in different categories.  The former is a
holomorphic \(E_3\)-factorisation algebra obtained from Hochschild
cochains by Kontsevich--Tamarkin formality, Costello--Gwilliam locality,
and the Costello--Li BV refinement attached to \(\Omega_X\).  The latter
is the oriented vanishing-cycle Hall algebra
\[
  \CoHA_{\rm crit}^{\rm or}(U)
  =
  \bigoplus_{\mathbf d}
  H^{\rm BM}_{G_{\mathbf d}}
  \left(
    \Crit(\Tr W_{U,\mathbf d}),
    \phi_{\Tr W_{U,\mathbf d}}\otimes\mathscr L_{o_U}
  \right).
\]
Identifying them requires the orientation-preserving comparison
\[
  \Theta_{\hCS\to\Hall}^{\rm or}\colon
  \Obs_{\hCS}^{q}(-,\mathfrak g)\to
  \CoHA_{\rm crit}^{\rm or}(-),
\]
local for the Dolbeault topology, compatible with Weiss descent,
intertwining the BV bracket with the Hall correspondence product after
the CY3 shift, reducing on the \(\mathbb C^3\) chart to
\(\CoHA(\mathbb C^3)=Y^+(\widehat{\mathfrak{gl}}_1)\), compatible after
Drinfeld doubling with the Fock/evaluation representation, transporting
determinant-line square roots on overlaps, and respecting
Thom--Sebastiani for short exact sequences.  Without this comparison,
the Hall equality is a theorem on the Hall side and \(\PhiFA_3\) is a
theorem on the Costello side, but their identification is not a theorem.
```

## Files changed

- `notes/adversarial_bps_positive_geometry_20260424/agent_07_costello_bv_factorization.md`

## Verification

No build was run.  This is a notes-only adversarial report; manuscript
files were read but not edited.
