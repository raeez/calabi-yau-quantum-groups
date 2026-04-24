# Agent A1 - Total-resolution attack on `Theta_{hCS->Hall}^{or}`

Date: 2026-04-24.

Scope: issue 1 of the total-resolution swarm.  I attacked the construction of
the oriented comparison
\[
  \Theta_{\hCS\to\Hall}^{\mathrm{or}}\colon
  \Obs_{\hCS}^{q}(-,\mathfrak g)
  \longrightarrow
  \CoHA_{\mathrm{crit}}^{\mathrm{or}}(-)
\]
from the live manuscript, especially
`chapters/theory/cy3_chain_level_bridge.tex`, and from the previous A1/A2/A3
frontier reports.  I made no manuscript edits.

## Verdict

The current tree does not contain enough mathematics to construct
`Theta_{hCS->Hall}^{or}`.  The manuscript now has the correct controller:
the completed Cech convolution dg Lie algebra
\[
  \mathfrak M_{\hCS,\Hall}(\mathfrak U)
  =
  \Tot\,\Cech^\bullet(\mathfrak U,
  \Hom_{\mathrm{cont}}^\bullet(\Obs_{\hCS}^{q},
  \CoHA_{\mathrm{crit}}^{\mathrm{or}}))
\]
and the five obstruction components
\[
  (o_{\mathrm{MC}},o_{\mathrm{or}},o_{\mathrm{gr}},
    o_{\mathrm{TS}},o_{\mathrm{fact}}).
\]
What is missing is not a descent formalism.  What is missing is the
degree-zero chartwise map
\[
  \theta_U:
  \Obs_{\hCS}^{q}(U,\mathfrak g)
  \to
  \CoHA_{\mathrm{crit}}^{\mathrm{or}}(U)
\]
itself, before any global obstruction can be killed.

The strongest true upgrade is therefore:

1. on a one-chart contractible normalised critical chart, the four
   discrete/coherent obstructions `o_or`, `o_gr`, `o_TS`, and `o_fact`
   vanish tautologically after the orientation, shifts, Tate twists,
   completions, and Hall Thom-Sebastiani isomorphisms are chosen as part
   of the local datum;
2. the Maurer-Cartan obstruction `o_MC` is still undefined until an
   actual chartwise chain map `theta_U` is supplied, and nonzero unless
   that map is a chain-level multiplicative comparison;
3. for a real DWR cover, none of the five global vanishings is proved by
   the existing sources.

So `Theta_{hCS->Hall}^{or}` must remain open.  The descent criterion can
stay as a formal theorem, but it must not be read as the construction of
the comparison map.

## Exact local model

The source is not `C^*(g)`.  On a holomorphic polydisc
`P = D_1 x D_2 x D_3`, the live many-variable source is the quantum BV
observable complex on compact-support hCS fields
\[
  \Obs_{\hCS}^{q}(P,\mathfrak g)
  =
  \left(
    \mathcal O(\Omega_c^{0,\bullet}(P,\mathfrak g)[1])[[\hbar]],
    \bar\partial+\{I[L],-\}_{\BV}+\hbar\Delta_L
  \right),
\]
with the quantum master equation imposed as anomaly-cancellation data.
For a CY3 category chart, the classical many-variable model is
\[
  \mathfrak L_{\mathcal C}(P)
  =
  \Omega_c^{0,\bullet}
  (P,J^\infty_{\mathrm{hol},z_1,z_2,z_3}\mathfrak l_{\mathcal C})[1],
\]
topologised as a strict nuclear LF space, with completed projective
tensors and strong continuous duals.  The CE/bar relation is the
continuous-duality statement
\[
  \Obs_{\mathcal C}^{\mathrm{cl}}(P)
  \simeq
  \left(B_{E_3}U^{\mathrm{fact},E_3}_P(\mathfrak L_{\mathcal C})\right)^\vee_b,
\]
conditional on Stage-1 `E_3` formality and the Costello-Li holomorphic
witness.

The target is not an unshifted cohomology group and not
`\mathcal W_{1+\infty}`.  A local Hall summand is
\[
  H^{\mathrm{BM}}_{G_{\mathbf d}}
  \left(
    \mathrm{Crit}(\mathrm{Tr}W_{\mathbf d}),
    \phi_{\mathrm{Tr}W_{\mathbf d}}\otimes\mathscr L_{o_U}
  \right)
  [s(U,\mathbf d)](t(U,\mathbf d)),
\]
with orientation local system, perverse/cohomological shift, Tate twist,
charge/HN and equivariant completions, and Hall Thom-Sebastiani
coherences.  On `C^3`, the proved Hall-side core is
\[
  \CoHA(\mathbb C^3)\cong Y^+(\widehat{\mathfrak{gl}}_1),
\]
with `W_{1+infty}` reached only after Drinfeld doubling and
Fock/evaluation.

## Attack cycles

### Attack 1: `CoHA(C^3)=Y^+` is not a map from hCS observables

The Schiffmann-Vasserot/Kontsevich-Soibelman theorem identifies the
Hall-side algebra on the affine toric chart.  It does not construct a
continuous chain map from renormalised hCS observables to
vanishing-cycle BM chains.  The source is a completed dg algebra of
functionals on infinite-dimensional Dolbeault fields.  The target is
formed by critical loci of finite-dimensional representation spaces and
vanishing cycles.  A comparison needs an integration/renormalisation
bridge between these two constructions; the manuscript does not contain
one.

Heal: keep the local Hall theorem as the target normal form only.  It
may certify the right-hand value of a future `theta_U`; it cannot define
`theta_U`.

### Attack 2: CFG ordinary Chern-Simons does not construct the CY3 Hall map

CFG supplies the grammar of `E_3` factorisation envelopes and traces for
ordinary real 3-dimensional Chern-Simons.  The live CY3 source keeps
three holomorphic variables, compact-support Dolbeault complexes,
continuous duals, BV renormalisation, and multidirectional residues.
CFG has no vanishing-cycle target and no orientation datum for critical
CoHA.

Heal: use CFG only as the Stage-1 factorisation-envelope analogue.  The
hCS-to-Hall comparison remains an additional datum controlled by
`\mathfrak M_{\hCS,\Hall}`.

### Attack 3: Joyce/KPS orientation data do not kill comparison orientation

The local literature anchors in the manuscript give orientation data for
derived CY3 moduli: Joyce vertex algebras use orientation data, PTVV
supplies the shifted symplectic form, and Kinjo-Park-Safronov supplies
canonical orientability under their hypotheses.  This is Hall-side
orientability.  The comparison obstruction is stronger: it asks for
transport of determinant-line square roots through the hCS-to-Hall map
on every overlap and through every extension correspondence.

Heal: on a single contractible critical chart with an orientation chosen
as part of the datum, `o_or=0`.  On a genuine cover,
\[
  o_{\mathrm{or}}=[\epsilon_{ijk}]\in \check H^2(\mathfrak U,\mathbb Z/2),
  \qquad
  \phi_{jk}\phi_{ij}=\epsilon_{ijk}\phi_{ik},
\]
and no source currently proves this class vanishes for the comparison.

### Attack 4: shifts and Tate twists are named, not derived from hCS

The target contains `[s(U,d)](t(U,d))`.  The source has ghost number,
Dolbeault degree, BV degree, and `hbar` degree.  A degree-zero comparison
requires a formula matching these gradings for every chart and dimension
vector.  The manuscript fixes the need for `s` and `t`, but not a
derivation from the hCS side.

Heal: `o_gr=0` only after the functions `s(U,d)` and `t(U,d)` are chosen
globally and checked against the BV grading.  On a one-chart normalised
test chart this is convention; on overlaps it is the Cech mismatch
class of those integer/Tate functions.

### Attack 5: Thom-Sebastiani associativity is internal to Hall, not relative to hCS

Critical CoHA associativity uses vanishing cycles and
Thom-Sebastiani isomorphisms for extension correspondences.  hCS
factorisation associativity uses disjoint support, BV products, and
collision/residue operations.  These are different mechanisms.  Internal
associativity on both sides does not imply the comparison intertwines
them.

Heal: `o_TS=0` is proved only in the one-chart Hall target after fixing
the Hall TS associator.  The relative comparison class is the ratio
between the two parenthesised composites
\[
  ((\theta a)*(\theta b))*(\theta c)
  \quad\text{and}\quad
  (\theta a)*((\theta b)*(\theta c))
\]
after transporting the source triple product through `theta`.  Without
`theta`, this ratio is not defined.

### Attack 6: factorisation multiplicativity is not automatic

The source is multiplicative for disjoint compact supports.  The target
is multiplicative by Hall extension product.  A map preserving both must
make
\[
  \theta_{U\sqcup V}\circ m_{\hCS}
  =
  m_{\Hall}\circ(\theta_U\widehat\otimes\theta_V)
\]
in the completed category.  No current source proves this identity.

Heal: `o_fact=0` in the trivial one-chart/no-disjoint-test situation.
For the real DWR/Ran site it is a separate multiplicativity obstruction,
not a consequence of source and target products existing.

## Obstruction complex and classes

For a DWR-good cover `U`, set
\[
  \mathcal M^q(U_I)=
  \Hom_{\mathrm{cont}}^q
  \bigl(
    \Obs_{\hCS}^{q}(U_I,\mathfrak g),
    \CoHA_{\mathrm{crit}}^{\mathrm{or}}(U_I)
  \bigr),
\]
and
\[
  \mathfrak M_{\hCS,\Hall}(\mathfrak U)
  =
  \Tot\,\check C^\bullet(\mathfrak U,\mathcal M^\bullet).
\]
The differential is the sum of the Cech differential and the two
internal differentials.  The bracket is the convolution commutator built
from the BV/factorisation product on the source and Hall convolution on
the target.

Given chartwise candidates `theta_i`, the five classes are:

- `o_MC`: the cohomology class of
  \[
    d\theta+\frac12[\theta,\theta]
  \]
  in `H^1(M_hCS,Hall)`.  This is the first real obstruction.
- `o_or`: the orientation-gerbe class in
  `Cech^2(U,Z/2)` measuring failure of determinant-line square-root
  transports to satisfy the triple-overlap cocycle identity.
- `o_gr`: the integer/Tate mismatch of `s(U,d)` and `t(U,d)`, valued in
  the discrete grading sheaf determined by cohomological degree and Tate
  weight.
- `o_TS`: the associator ratio between the two Thom-Sebastiani
  parenthesisations for iterated Hall extensions, after comparison with
  the hCS triple product.
- `o_fact`: the failure of the comparison to preserve disjoint-union
  factorisation products in the completed tensor category.

The descent theorem in the manuscript is correct as a criterion:
`Theta` exists exactly when chartwise quasi-isomorphisms exist and this
five-component obstruction tuple vanishes.  It is not evidence that the
chartwise quasi-isomorphisms exist.

## Actual vanishings proved from the current sources

The following vanishing is genuinely derivable.

**Single-chart normalisation vanishing.**  Let `U ~= C^3` be one
contractible critical chart, take the one-object cover `{U}`, choose an
orientation square root `o_U`, choose the shift/Tate functions
`s(U,d), t(U,d)`, choose the Hall completion and the hCS completion, and
take the Hall Thom-Sebastiani associator as part of the target datum.
Then
\[
  o_{\mathrm{or}}=o_{\mathrm{gr}}=o_{\mathrm{TS}}=o_{\mathrm{fact}}=0
\]
for the one-chart descent problem.  The proof is formal:
there are no nontrivial Cech triple overlaps, no grading transition
functions, no cross-chart orientation transports, and the one-chart
Hall TS/factorisation coherences are part of the target definition.

This does not prove `Theta_U`.  The Maurer-Cartan class is still the
condition that a proposed `theta_U` is a chain map and multiplicative:
\[
  d\theta_U+\frac12[\theta_U,\theta_U]=0.
\]
No such `theta_U` is constructed in the live sources.

No nontrivial global vanishing is proved.  In particular:

- `o_MC` remains open because no chartwise comparison map is available;
- `o_or` remains open beyond Hall-side orientability, because comparison
  transport across hCS/Hall charts is not constructed;
- `o_gr` remains open until `s,t` are derived from the BV grading and
  checked on overlaps;
- `o_TS` remains open relative to hCS, even though Hall associativity is
  known internally;
- `o_fact` remains open because no multiplicative comparison map exists.

## Strongest true theorem package to inscribe

If the integration owner wants a manuscript upgrade, the theorem should
be local and diagnostic, not a false construction claim.

```tex
\begin{proposition}[Single-chart vanishing for the oriented hCS--Hall obstruction]
Let \(U\simeq \mathbb C^3\) be a single holomorphic critical chart with
fixed quiver-with-potential presentation, fixed orientation square root,
fixed shift and Tate functions, fixed hCS and Hall completions, and fixed
Hall Thom--Sebastiani coherences.  For the one-object DWR cover
\(\{U\}\), the discrete/coherent obstruction components
\[
  o_{\mathrm{or}},\quad o_{\mathrm{gr}},\quad
  o_{\mathrm{TS}},\quad o_{\mathrm{fact}}
\]
vanish.  The remaining obstruction is exactly the Maurer--Cartan
equation for a degree-zero continuous map
\[
  \theta_U:\Obs_{\hCS}^{q}(U,\mathfrak g)
  \to \CoHA_{\mathrm{crit}}^{\mathrm{or}}(U).
\]
Thus the first unproved datum in
\(\Theta_{\hCS\to\Hall}^{\mathrm{or}}\) is the chartwise
chain-level, multiplicative quasi-isomorphism \(\theta_U\), not the
orientation, grading, Thom--Sebastiani, or factorisation descent
formalism on a single normalised chart.
\end{proposition}
```

Proof: the one-object Cech nerve has no nonidentity overlap cochains, so
orientation and grading transition cocycles vanish after the local
choices.  Hall TS and disjoint-union factorisation coherences are
components of the one-chart target datum.  A comparison map exists
precisely when a degree-zero continuous map solves the Maurer-Cartan
equation in the local convolution dg Lie algebra and is a
quasi-isomorphism.  That last condition is not supplied by
Schiffmann-Vasserot, Kontsevich-Soibelman, Joyce, KPS, CFG, A2, or A3.

## Claim-status recommendation

- Keep `op:cy3-hcs-hall-comparison` as `ClaimStatusOpen`.
- Keep `thm:hcs-hall-descent-criterion` as a formal `ProvedHere`
  criterion only if surrounding prose states that it assumes chartwise
  quasi-isomorphisms.
- Add, at most, the single-chart vanishing proposition above as
  `ClaimStatusProvedHere`.
- Do not state that `Theta_{hCS->Hall}^{or}` has been constructed on
  `C^3`; the live theorem is only `CoHA(C^3)=Y^+` on the Hall side.
- Do not use CFG as a substitute for the CY3 hCS-to-Hall map.
- Do not let holography, K3xE Hall-Borcherds closure, or defect traces
  cite `Theta` except as a conditional hypothesis.

## File anchors

- `chapters/theory/cy3_chain_level_bridge.tex:73`: quantum hCS
  observables as renormalised BV complexes.
- `chapters/theory/cy3_chain_level_bridge.tex:101`: many-variable
  Dolbeault/chiral CE model.
- `chapters/theory/cy3_chain_level_bridge.tex:216`: continuous dual
  `E_3` bar/CE theorem; explicitly not Hall comparison.
- `chapters/theory/cy3_chain_level_bridge.tex:291`: typed bridge with
  dashed `Theta`.
- `chapters/theory/cy3_chain_level_bridge.tex:316`: Hall-valued
  factorisation-cosheaf target.
- `chapters/theory/cy3_chain_level_bridge.tex:355`: local critical-CoHA
  normalisation with shifts, Tate twist, and orientation local system.
- `chapters/theory/cy3_chain_level_bridge.tex:387`: proved local Hall
  core `CoHA(C^3)=Y^+`.
- `chapters/theory/cy3_chain_level_bridge.tex:418`: local-to-toric
  descent is conditional on the comparison map.
- `chapters/theory/cy3_chain_level_bridge.tex:602`: open problem
  defining `Theta_{hCS->Hall}^{or}`.
- `chapters/theory/cy3_chain_level_bridge.tex:660`: obstruction complex
  and five obstruction components.
- `chapters/theory/cy3_chain_level_bridge.tex:713`: descent criterion.
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:4091`: Joyce/KPS
  vertex-algebra and orientation anchors for CY3 moduli.
- `chapters/examples/coha_wall_crossing_platonic.tex:120`: critical
  CoHA as associative graded Hall algebra after vanishing-cycle
  cohomology, separate from a dg differential.

## Commands run

```bash
sed -n '1,220p' .agents/skills/vol3-frontier-research/SKILL.md
sed -n '1,220p' .agents/skills/vol3-swarm-orchestration/SKILL.md
sed -n '1,220p' CLAUDE.md
git status --short
rg -n "Theta|hCS|Hall|critical|CoHA|obstruction|orientation|Tate|Thom|Sebastiani|factorisation|factorization|continuous|E_3|bar" chapters/theory/cy3_chain_level_bridge.tex
sed -n '1,260p' notes/adversarial_swarm_20260424_frontier_resolution/agent_A1_theta_hcs_hall.md
sed -n '1,260p' notes/adversarial_swarm_20260424_frontier_resolution/agent_A2_ce_bar.md
sed -n '1,260p' notes/adversarial_swarm_20260424_frontier_resolution/agent_A3_spch_functoriality.md
nl -ba chapters/theory/cy3_chain_level_bridge.tex | sed -n '70,170p'
nl -ba chapters/theory/cy3_chain_level_bridge.tex | sed -n '216,450p'
nl -ba chapters/theory/cy3_chain_level_bridge.tex | sed -n '602,775p'
nl -ba chapters/examples/k3_chiral_bialgebra_platonic.tex | sed -n '4091,4215p'
nl -ba chapters/examples/coha_wall_crossing_platonic.tex | sed -n '120,250p'
```

No tests were run.  This lane is a proof-obligation and source-audit
lane; it adds no executable model beyond the already existing obstruction
formalism.

## Files changed

- `notes/adversarial_swarm_20260424_total_resolution/agent_A1_theta_hcs_hall.md`
