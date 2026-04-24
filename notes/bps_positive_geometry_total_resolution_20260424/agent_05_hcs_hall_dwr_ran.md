# Obligation 5. The Oriented hCS-to-Hall Map on the DWR/Ran Nerve

## Resolution

The map

```tex
\Theta_{\hCS\to\Hall}^{\mathrm{or}}\colon
  \Obs_{\hCS}^{q}(-,\mathfrak g)
  \longrightarrow
  \CoHA_{\mathrm{crit}}^{\mathrm{or}}(-)
```

is not a map of two algebras written on a single open set.  It is a
degree-zero continuous natural transformation on the full
Dolbeault--Weiss--Ran Cech nerve, valued in completed oriented
Hall-factorisation cosheaves.  Its source remembers compactly supported
BV fields and disjoint-support factorisation.  Its target remembers
oriented derived critical moduli, vanishing cycles, Hall extension
correspondences, charge/HN completions, shifts, Tate twists, and
Thom--Sebastiani transport.  The correct theorem is therefore:

> Given an anomaly-free all-scale hCS package, an oriented critical Hall
> atlas, and local stationary-phase calibration maps satisfying the seven
> compatibilities below, there is a unique global
> `Theta^{or}_{hCS->Hall}` in
> `FactCosh^{or,wedge}_{Hall}(X)`, up to the gauge action of the
> degree-zero descent complex.  For compact CY3, the remaining work is
> exactly the vanishing of an explicit obstruction tuple; there is no
> additional informal bridge.

This strengthens the bridge of
`chapters/theory/cy3_chain_level_bridge.tex` rather than replacing it.
The live anchors are:

```tex
def:cy3-hcs-bv-complex
def:cy3-hcs-quantum-observables
def:hall-valued-factorisation-cosheaf-target
def:local-critical-coha-normalisation
def:cy3-oriented-hcs-hall-comparison-datum
thm:oriented-hcs-hall-comparison-from-dwr-datum
def:hcs-hall-descent-obstruction
thm:hcs-hall-descent-criterion
rem:r6-op-closed-at-c3
prop:r6-convolution-vs-bv-bracket
thm:r6-k3e-local-chart-qiso-inscribed
```

## First-Principles Construction

Let `X` be a smooth Calabi--Yau threefold with holomorphic volume form
`\Omega_X`.  Fix a DWR-good cover `\mathfrak U` by Stein polydiscs
closed under finite intersections and Weiss refinements.  The nerve
`\mathsf N_{\mathsf{DWR}}(\mathfrak U)` has a simplex

```tex
\sigma=(S,\{P_s\Subset U_{i_{s,0}}\cap\cdots\cap U_{i_{s,p}}\}_{s\in S}),
```

where `S` is finite and the polydiscs `P_s` are pairwise disjoint.
Faces forget Cech indices, refinements shrink polydiscs, and Ran
multiplication is disjoint union of finite sets.

On a polydisc `P`, the hCS side is the Costello--Gwilliam quantum BV
complex

```tex
\Obs_{\hCS}^{q}(P,\mathfrak g)
=
\left(
  \mathcal O_{\mathrm{ren,loc/multiloc}}
  (\Omega^{0,\bullet}_c(P,\mathfrak g)[1])[[\hbar]],
  Q_{\hCS}+\{I[L],-\}_{\BV}+\hbar\Delta_L
\right).
```

The compact-support convention is load-bearing.  For `P'\Subset P`, the
map on fields is extension by zero
`\Omega_c^{0,\bullet}(P')\to\Omega_c^{0,\bullet}(P)`; on observables the
factorisation-cosheaf map is the Costello--Gwilliam map induced by field
restriction and compact-support extension.  Disjoint polydiscs multiply
by disjoint-support factorisation:

```tex
\Obs_{\hCS}^{q}(P_1)\widehat\otimes\Obs_{\hCS}^{q}(P_2)
  \longrightarrow
\Obs_{\hCS}^{q}(P_1\sqcup P_2).
```

Thus

```tex
\Obs_{\hCS}^{q}(\sigma,\mathfrak g)
  =
\widehat{\bigotimes}_{s\in S}
\Obs_{\hCS}^{q}(P_s,\mathfrak g).
```

The Hall side begins with a charge monoid `\Gamma`, a stability sector,
and a critical atlas

```tex
(\mathfrak M_{P,\gamma}, f_{P,\gamma}, o_{P,\gamma})
```

for compactly supported objects of charge `\gamma` over `P`.  Here
`\mathfrak M_{P,\gamma}` is a derived Artin chart, `f_{P,\gamma}` is a
critical potential in a Brav--Bussi--Joyce local Darboux model for the
PTVV `(-1)`-shifted symplectic moduli stack, and `o_{P,\gamma}` is a
Joyce--Kontsevich--Soibelman orientation: a square root of the virtual
determinant line with coherent transports for restriction, direct sum,
and extension.  Its chain complex is

```tex
\mathcal H(P)
 =
\widehat{\bigoplus}_{\gamma\in\Gamma}
H^{\mathrm{BM}}_{G_\gamma}
\left(
  \mathrm{Crit}(f_{P,\gamma}),
  \phi_{f_{P,\gamma}}\otimes\mathscr L_{o_{P,\gamma}}
\right)
[s(P,\gamma)](t(P,\gamma)).
```

The shift `s(P,\gamma)` and Tate twist `t(P,\gamma)` are part of the
normalisation.  Without them there is no degree-zero comparison.
For a simplex,

```tex
\CoHA_{\mathrm{crit}}^{\mathrm{or}}(\sigma)
 =
\widehat{\bigoplus}_{\gamma\in\Gamma^S}
\widehat{\bigotimes}_{s\in S}
H^{\mathrm{BM}}_{G_{\gamma_s}}
\left(
  \mathrm{Crit}(f_{P_s,\gamma_s}),
  \phi_{f_{P_s,\gamma_s}}\otimes\mathscr L_{o_{P_s,\gamma_s}}
\right)
[s(P_s,\gamma_s)](t(P_s,\gamma_s)).
```

Hall multiplication is the pull--push operation along the stack of short
exact sequences

```tex
\mathfrak M_{\gamma_1}(P)\times\mathfrak M_{\gamma_2}(P)
  \xleftarrow{p_1\times p_2}
\mathfrak E_{\gamma_1,\gamma_2}(P)
  \xrightarrow{p_3}
\mathfrak M_{\gamma_1+\gamma_2}(P),
```

followed by:

```tex
Thom--Sebastiani for vanishing cycles,
orientation-line transport,
shift correction,
Tate-twist correction,
charge/HN-adic completion.
```

## The Calibration Datum

A calibration datum is a family of continuous chain maps

```tex
\theta_{P,\gamma}\colon
\Obs_{\hCS}^{q}(P,\mathfrak g)
  \longrightarrow
H^{\mathrm{BM}}_{G_\gamma}
\left(
  \mathrm{Crit}(f_{P,\gamma}),
  \phi_{f_{P,\gamma}}\otimes\mathscr L_{o_{P,\gamma}}
\right)
[s(P,\gamma)](t(P,\gamma))
```

indexed by DWR polydiscs and charges.  It is a stationary-phase
realisation of the same derived critical problem: the hCS BV integral
localises onto the critical locus, and the critical Hall chart records
the resulting vanishing-cycle class.  On `\mathbb C^3` this is the
explicit plane-partition localisation map of
`rem:r6-op-closed-at-c3`; in cohomology it recovers

```tex
\CoHA(\mathbb C^3)=Y^+(\widehat{\mathfrak{gl}}_1),
```

not `\mathcal W_{1+\infty}` before Drinfeld doubling.

The maps `\theta_{P,\gamma}` must satisfy seven axioms.

1. **Chain condition.**

```tex
d_{\Hall}\theta_{P,\gamma}
 =
\theta_{P,\gamma}
(Q_{\hCS}+\{I[L],-\}_{\BV}+\hbar\Delta_L).
```

2. **Compact-support Beck--Chevalley.**  For `P'\Subset P`, the square
formed by hCS compact-support extension and Hall extension-by-zero
Borel--Moore pushforward commutes after the named completion.

3. **Cech/Ran naturality.**  The same compatibility holds on every
higher intersection `U_{i_0}\cap\cdots\cap U_{i_p}` and every Ran
refinement.

4. **Hall convolution.**  For charges `\gamma_1,\gamma_2`,

```tex
\theta_{P,\gamma_1+\gamma_2}(\mu_{\BV}^{\mathrm{fact}}(a,b))
 =
\mu_{\Hall}^{\mathrm{TS},o}
(\theta_{P,\gamma_1}(a),\theta_{P,\gamma_2}(b)).
```

5. **CY3 bracket shift.**  The BV bracket is sent to the Hall
commutator after the CY3 shift fixed in
`def:local-critical-coha-normalisation`.  In the `\mathbb C^3` base
case this is the chain homotopy `h=O(\hbar)` of
`prop:r6-convolution-vs-bv-bracket`, strict at tree level and strict in
cohomology.

6. **Orientation, shifts, and Tate twists.**  The square root
`\ell_{P,\gamma}^{\otimes 2}\simeq K^{\mathrm{vir}}_{P,\gamma}` is
transported on overlaps and along extension stacks; the numerical
functions `s(P,\gamma)` and `t(P,\gamma)` are invariant under Cech
restriction and additive under Hall extension.

7. **Thom--Sebastiani associativity.**  For every triple of charges, the
two parenthesisations of iterated Hall convolution give the same
vanishing-cycle isomorphism after orientation transport and the
shift/Tate correction.

## Theorem A. Construction of `Theta`

Assume a DWR-good cover, an anomaly-free hCS quantisation, an oriented
critical Hall atlas, and a calibration datum satisfying the seven
axioms.  Then

```tex
\Theta_{\hCS\to\Hall}^{\mathrm{or}}\colon
  \Obs_{\hCS}^{q}(-,\mathfrak g)
  \longrightarrow
  \CoHA_{\mathrm{crit}}^{\mathrm{or}}(-)
```

is a morphism in
`\mathsf{FactCosh}_{\Hall}^{\mathrm{or},\wedge}(X)`.
On a simplex `\sigma=(S,\{P_s\})` it is

```tex
\Theta_\sigma
 =
\widehat{\bigoplus}_{\gamma\in\Gamma^S}
\widehat{\bigotimes}_{s\in S}
\theta_{P_s,\gamma_s}.
```

It preserves:

```tex
DWR Cech naturality,
Ran disjoint-union factorisation,
Hall convolution,
compact-support variance,
vanishing-cycle coefficients,
orientation local systems,
CY3 shifts,
Tate twists,
charge/HN and hbar completions,
Thom--Sebastiani parenthesisation.
```

### Proof

The formula for `\Theta_\sigma` is defined because both source and
target are completed tensor products over the same finite Ran set `S`
and completed direct sums over the same charge monoid.  Continuity
follows from the calibration datum and from the product topology:
`\hbar`-adic on hCS observables, charge/HN-adic and equivariant-localised
on Hall complexes.

The chain condition for each `\theta_{P,\gamma}` implies the chain
condition for the completed tensor product.  Cech and refinement
naturality are exactly axiom 3; compact-support variance is axiom 2.
Disjoint Ran multiplication is axiom 4 after tensoring over the
components of `S`.  The bracket statement is axiom 5, and the target
commutator is the commutator of Hall convolution with the CY3 shift
already built into `s(P,\gamma)`.

The target is not an unoriented CoHA.  Its coefficient system is
`\phi_f\otimes\mathscr L_o`, so a product is not defined until
Thom--Sebastiani, orientation transport, and grading/Tate corrections
have been inserted.  Axioms 6 and 7 are precisely the coherence
conditions required for the product square and the triple-product
associator in
`\mathsf{FactCosh}_{\Hall}^{\mathrm{or},\wedge}(X)`.  Therefore the
family `\Theta_\sigma` is a morphism in that category.

No further construction is hidden.  The proof is the Yoneda principle
for the typed target category: a morphism in the category is exactly a
continuous natural transformation on the full DWR/Ran nerve preserving
the listed structure.

## Theorem B. Obstruction-Theoretic Closure on a Compact CY3

Fix the source and target objects in
`\mathsf{FactCosh}_{\Hall}^{\mathrm{or},\wedge}(X)`.  Define the
complete filtered dg Lie algebra

```tex
\mathfrak M_{\hCS,\Hall}(\mathfrak U)
 =
\Tot\,\check C^\bullet
\left(
  \mathfrak U,\,
  \Hom_{\mathrm{cont}}^\bullet
  (\Obs_{\hCS}^{q},\CoHA_{\mathrm{crit}}^{\mathrm{or}})
\right),
```

with differential equal to Cech differential plus source and target
differentials, and bracket equal to the convolution bracket induced by
BV factorisation and Hall multiplication.  A chartwise calibration
family glues to `\Theta_{\hCS\to\Hall}^{\mathrm{or}}` if and only if
the obstruction tuple

```tex
\mathfrak o
=
(o_{\mathrm{MC}},
  o_{\mathrm{or}},
  o_{\mathrm{gr}},
  o_{\mathrm{TS}},
  o_{\mathrm{fact}},
  o_{\mathrm{cs}},
  o_{\wedge})
```

vanishes, where:

```tex
o_MC     = Maurer--Cartan defect in H^1(\mathfrak M_{\hCS,\Hall}),
o_or     = determinant-line square-root Cech Z/2 class,
o_gr     = integral shift and Tate-twist mismatch,
o_TS     = Thom--Sebastiani associator defect,
o_fact   = Ran/disjoint-union multiplicativity defect,
o_cs     = compact-support Beck--Chevalley defect,
o_wedge  = incompatibility of hbar, HN, charge, and equivariant completions.
```

If the tuple vanishes and the vertex maps are quasi-isomorphisms, then
the global `Theta` is a quasi-isomorphism on DWR/Weiss descent.  The
space of such global maps is the Maurer--Cartan gauge quotient

```tex
\mathrm{MC}(\mathfrak M_{\hCS,\Hall})/
\exp(F^1\mathfrak M_{\hCS,\Hall}^0),
```

and is a torsor under `H^0(\mathfrak M_{\hCS,\Hall})` when the
obstruction class is zero.

### Proof

Forgetting orientation, shifts, Tate twists, compact support, and
completion, gluing chartwise chain maps is the usual Cech descent
problem for morphisms of complexes.  Its obstruction is the
Maurer--Cartan defect in the total Cech convolution dg Lie algebra.
This gives `o_MC`.

Restoring the omitted structures adds exactly the six discrete or
coherent defects listed above.  Orientation data form a square-root
torsor, hence give `o_or`.  The shift and Tate functions are locally
constant integer data, hence give `o_gr`.  Thom--Sebastiani has two
parenthesisations over a triple extension stack, hence gives `o_TS`.
Ran factorisation over disjoint polydiscs gives `o_fact`.
Compact-support extension by zero on the hCS side and Borel--Moore
extension on the Hall side give the Beck--Chevalley square whose
failure is `o_cs`.  The comparison is continuous only if all completion
filtrations are preserved; the corresponding failure is `o_wedge`.

Vanishing of all seven classes is precisely the assertion that the
chartwise maps define the seven axioms of the calibration datum on the
whole nerve.  Theorem A then constructs `Theta`.  Conversely, a morphism
in the target category restricts to a Maurer--Cartan solution and
preserves every named structure, so all seven obstruction classes
vanish.

## Theorem C. The Toric Terminal Normalisation

On the affine toric chart `X=\mathbb C^3`, with the standard hCS
volume-form orientation and the standard critical CoHA of the
three-loop Jordan quiver, the calibration datum exists.  The resulting
map

```tex
\Theta_{\hCS\to\Hall}^{\mathbb C^3}\colon
\Obs_{\hCS}^{q}(\mathbb C^3;\widehat{\mathfrak{gl}}_1)
\longrightarrow
\CoHA_{\mathrm{crit}}^{\mathrm{or}}(\mathbb C^3)
```

is the `\mathbb C^3` edge of the five-way Rosetta:

```tex
\Obs_{\hCS}^{q}
  \simeq
E_3\text{-labelled configuration homology}
  \simeq
Y^+(\widehat{\mathfrak{gl}}_1)
  \simeq
\CoHA(\mathbb C^3).
```

It is compatible with the BV bracket and Hall convolution after the
CY3 shift, with chain homotopy `O(\hbar)` and strict equality in
cohomology.  Its doubled representation reaches
`\mathcal W_{1+\infty}`; the positive-half CoHA itself remains `Y^+`.

### Proof

This is the local core already inscribed in
`rem:r6-op-closed-at-c3` and
`prop:r6-convolution-vs-bv-bracket`.  Equivariant BV localisation sends
hCS Feynman graphs to fixed-point data indexed by plane partitions.
The Nakajima flag correspondence packages the fixed-point coefficients
into CoHA classes.  Schiffmann--Vasserot identifies the cohomological
Hall algebra of the `\mathbb C^3` chart with
`Y^+(\widehat{\mathfrak{gl}}_1)`.  Disjoint-support graphs localise to
disjoint fixed-point data, so the map is factorising.  The standard
orientation on `dz_1\wedge dz_2\wedge dz_3` trivialises the determinant
square-root torsor on the chart; Thom--Sebastiani is the ordinary
addition of critical potentials under direct sum.

## Theorem D. K3 x E DWR Closure

For `X=K3\times E` on the Kummer DWR cover, with abelian
`\widehat{\mathfrak{gl}}_1` gauge and the product holomorphic volume
form, the local `\mathbb C^3` calibration maps glue to a global

```tex
\Theta_{\hCS\to\Hall}^{K3\times E}
  \in
\Hom_{\mathsf{FactCosh}_{\Hall}^{\mathrm{or},\wedge}(X)}
(\Obs_{\hCS}^{q},\CoHA_{\mathrm{crit}}^{\mathrm{or}}).
```

This is exactly `thm:r6-k3e-local-chart-qiso-inscribed`: the anomaly
vanishes for abelian gauge, the orientation torsor trivialises on the
Kummer product orientation, the shift/Tate data glue, the
Thom--Sebastiani associator is trivial for the abelian chartwise
extension product, and factorisation multiplicativity follows from
disjoint-support Feynman graphs and the supportwise Hall correspondence.

## Compact CY3 Proof Obligations

For a general compact CY3, the theorem to prove is not a weaker
statement.  It is the same theorem with the following data constructed
rather than assumed.

1. **All-scale hCS package.**  Construct `I[L]`, propagators, RG flow,
and QME solution on the chosen DWR cover, with compact-support maps
compatible on all higher Cech intersections.

2. **Derived critical Hall atlas.**  Construct the stack of compactly
supported semistable objects in each DWR sector as a PTVV
`(-1)`-shifted symplectic derived stack and choose Brav--Bussi--Joyce
Darboux charts
`\mathfrak M_{P,\gamma}\simeq\mathrm{Crit}(f_{P,\gamma})`.

3. **Orientation oracle.**  Compute the Cech class of
`\ell_{P,\gamma}^{\otimes 2}\simeq K^{\mathrm{vir}}_{P,\gamma}` and
produce coherent square roots under restriction, direct sum, and Hall
extension.

4. **Stationary-phase calibration.**  Construct the maps
`\theta_{P,\gamma}` as localised BV integration classes in
vanishing-cycle Borel--Moore homology, with the `\mathbb C^3` plane
partition formula as terminal degeneration.

5. **Compact-support Beck--Chevalley.**  Prove that hCS extension by
zero and Hall Borel--Moore extension by zero commute for every
refinement `P'\Subset P` and for all higher Cech/Ran simplices.

6. **Shift and Tate normalisation.**  Fix explicit functions
`s(P,\gamma)` and `t(P,\gamma)` from the virtual dimension and prove
additivity under extensions and invariance under DWR restriction.

7. **Thom--Sebastiani coherence.**  Prove that the vanishing-cycle
Thom--Sebastiani isomorphism, with orientation transport, is
associative on all iterated short-exact-sequence stacks.

8. **Completion theorem.**  Prove continuity of every map for the
`\hbar`-adic, strong-dual, charge/HN-adic, and equivariant-localised
topologies, and prove that the completed tensor/direct-sum operations
commute with DWR descent.

9. **Cohomology-level quasi-isomorphism.**  Prove that every vertex map
is a quasi-isomorphism after the fixed completions.  Local toric charts
use `\CoHA(\mathbb C^3)=Y^+`; non-toric charts require the stationary
phase comparison with the corresponding critical Hall chart.

10. **Gauge uniqueness.**  Compute
`H^0(\mathfrak M_{\hCS,\Hall})` and `H^1(\mathfrak M_{\hCS,\Hall})`.
Vanishing of `H^1` gives unobstructed gluing; `H^0` records the residual
automorphism torsor.

These ten obligations are constructive.  When they are verified, the
compact CY3 theorem follows formally from Theorems A and B.

## Homotopical and Motivic Localisation

The Hall target localises the positive geometry into derived algebraic
geometry.  The chain is:

```tex
Perf_c(X) with PTVV (-1)-shifted symplectic form
  -> d-critical / Darboux critical charts
  -> orientation square roots
  -> vanishing-cycle motives or sheaves
  -> Borel--Moore realisation
  -> completed critical CoHA
  -> Hall-valued factorisation cosheaf on the DWR/Ran nerve.
```

The hCS source localises the same geometry into homotopical BV
geometry:

```tex
\Omega_c^{0,\bullet}(P,\mathfrak g)[1]
  -> renormalised BV observables
  -> all-scale QME/RG factorisation algebra
  -> DWR descent.
```

`Theta^{or}_{hCS->Hall}` is the comparison of these two localisations.
The source is analytic/homotopical; the target is motivic/cohomological.
The bridge exists only when stationary phase identifies the analytic BV
critical locus with the derived critical Hall chart and transports the
orientation, shifts, Tate twists, and completions.  This is why the map
is not an afterthought: it is the exact place where factorisation
geometry becomes BPS positive geometry.

## Attack-Heal Stability

**Attack: A single local quasi-isomorphism cannot be the compact CY3
map.**  Heal: the map is defined on every simplex of the DWR/Ran nerve;
globality is Cech/Ran naturality plus obstruction vanishing in
`\mathfrak M_{\hCS,\Hall}`.

**Attack: The Hall product is not the BV bracket.**  Heal: the BV
bracket maps to the Hall commutator after the CY3 shift.  On
`\mathbb C^3` the chain homotopy is `O(\hbar)` and cohomology is strict;
globally this is encoded by `o_MC`.

**Attack: Vanishing cycles introduce signs invisible to field theory.**
Heal: the target coefficient system is
`\phi_f\otimes\mathscr L_o`, and orientation transport is an axiom; the
residual sign is exactly `o_or`.

**Attack: Shifts and Tate twists can make the comparison non-degree-zero.**
Heal: the local critical-CoHA normalisation is part of the object; the
grading defect is exactly `o_gr`.

**Attack: Thom--Sebastiani can fail under triple convolution.**  Heal:
the two parenthesisations define `o_TS`; vanishing is equivalent to
associativity in the oriented Hall-valued factorisation category.

**Attack: Compact support changes variance.**  Heal: the compact-support
Beck--Chevalley square is named as `o_cs`; it is not absorbed into
ordinary Cech descent.

**Attack: Formal completions can destroy descent.**  Heal: `o_wedge`
records exactly whether the `\hbar`, strong-dual, charge/HN, and
equivariant completions commute with tensor products, direct sums, and
homotopy colimits.

## Final Form

The hCS-to-Hall map is a theorem of typed descent:

```tex
anomaly-free hCS BV factorisation cosheaf
+ oriented critical Hall atlas
+ stationary-phase calibration
+ compact-support Beck--Chevalley
+ orientation/shift/Tate/TS/completion coherence
----------------------------------------------------------------
Theta^{or}_{hCS->Hall}
  in FactCosh^{or,wedge}_{Hall}(X).
```

The `\mathbb C^3` case is the terminal toric normalisation.  The
`K3\times E` Kummer DWR case is the first non-toric global test already
coherent with the CY3 chain-level bridge.  A general compact CY3 is
settled by constructing the same data and killing the seven obstruction
classes; the theorem statement does not weaken when the geometry stops
being toric.
