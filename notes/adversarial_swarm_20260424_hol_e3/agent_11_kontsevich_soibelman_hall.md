# Agent 11 - Kontsevich-Soibelman / Hall

Date: 2026-04-24.

Scope: attack the Hall side of the CY3 holomorphic \(E_3\) bridge:
\(\Theta_{\hCS\to\Hall}^{\mathrm{or}}\), oriented critical CoHA,
vanishing cycles, shifts/Tate twists, Thom--Sebastiani compatibility, and
the \(\mathbb C^3\) core \(\CoHA(\mathbb C^3)=Y^+\). No chapters or
compute files were edited.

## Evidence Read

- `CLAUDE.md`; `AGENTS.md`; `vol3-beilinson-loop` skill.
- Target chapter: `chapters/theory/cy3_chain_level_bridge.tex`.
- Toric chapter: `chapters/examples/toric_cy3_coha.tex`.
- CoHA chapter: `chapters/examples/coha_wall_crossing_platonic.tex`.
- Cross-check chapters: `chapters/theory/cy_to_chiral.tex`,
  `chapters/theory/quantum_chiral_algebras.tex`,
  `chapters/examples/k3_quantum_toroidal_chapter.tex`.
- Bibliography anchors: Kontsevich--Soibelman 2011
  `arXiv:1006.2706`; Kontsevich--Soibelman 2008 `arXiv:0811.2435`;
  Schiffmann--Vasserot 2013 `arXiv:1202.2756`; Rapcak--Soibelman--Yang--
  Zhao 2020 `arXiv:2007.13365`; Davison--Meinhardt `arXiv:1601.02479`;
  Joyce--Song 2011; Brav--Bussi--Dupont--Joyce--Szendroi shifted
  symplectic/d-critical orientation package as cited in the tree; Kinjo--
  Park--Safronov orientation data where invoked locally.

Local anchors:

- `cy3_chain_level_bridge.tex:178-200`: typed bridge
  \(\PhiFA_3 \dashrightarrow \CoHA_{\mathrm{crit}}\to Y^+\to D(Y^+)\to
  \mathcal W_{1+\infty}\).
- `cy3_chain_level_bridge.tex:203-235`: Hall-valued factorisation
  cosheaf target already demands orientation, completion, and
  Thom--Sebastiani.
- `cy3_chain_level_bridge.tex:237-264`: local critical-CoHA
  normalisation with vanishing cycles, shifts, Tate twists, and
  orientation local system.
- `cy3_chain_level_bridge.tex:269-298`: \(\mathbb C^3\) core:
  \(\CoHA(\mathbb C^3)\cong Y^+\), not \(\mathcal W_{1+\infty}\).
- `cy3_chain_level_bridge.tex:383-431`: first missing comparison
  problem.
- `toric_cy3_coha.tex:15-27`: toric gluing is conditional on orientation
  gerbe trivialisation, not only KS wall-crossing.
- `toric_cy3_coha.tex:74-88`: raw critical CoHA display explicitly lacks
  the hCS comparison data until orientation, shifts, twists, and
  completion are fixed.
- `toric_cy3_coha.tex:93-128`: SV \(\mathbb C^3\) theorem and conditional
  Hall-valued comparison for \(\PhiFA_3(\Perf(\mathbb C^3))\).
- `toric_cy3_coha.tex:221-253`: evaluation chain separates
  \(Y^+\), full Yangian, and \(\mathcal W_{1+\infty}\).
- `coha_wall_crossing_platonic.tex:92-141` and `:209-260`: CoHA is an
  associative graded algebra; the dg object is the Ginzburg algebra or
  the bar complex, not CoHA itself.

## Verdict

The target chapter is correctly typed at the spine. The dangerous
inference is not present as a theorem there, but it remains the exact
failure mode future prose could reintroduce:
\[
  \Obs^q_{\hCS}(U,\mathfrak g)
  \simeq
  \CoHA_{\mathrm{crit}}(U)
  \quad\text{because}\quad
  \CoHA(\mathbb C^3)=Y^+
\]
or worse
\[
  \CoHA(\mathbb C^3)=\mathcal W_{1+\infty}.
\]
Both are false. The proved Hall core is only the algebraic positive-half
statement. The first missing lemma is an orientation-preserving,
shift-normalised, Thom--Sebastiani-compatible comparison
\(\Theta_{\hCS\to\Hall}^{\mathrm{or}}\) in the Hall-valued
factorisation-cosheaf category.

Status recommendation:

- \(\CoHA(\mathbb C^3)=Y^+(\widehat{\mathfrak{gl}}_1)\): proved elsewhere.
- \(Y^+\to D(Y^+)\to \mathcal W_{1+\infty}\): proved/represented only
  after Drinfeld doubling and Fock/evaluation.
- \(\Theta_{\hCS\to\Hall}^{\mathrm{or}}\): open in general; conditional on
  all data below.
- Toric descent from chartwise \(Y^+\): conditional on orientation-
  compatible overlap data and the comparison maps on the DWR nerve.
- \(K3\times E\) Hall--Borcherds algebra: character-level identities are
  evidence, not algebra-level construction.

## First Missing Lemma

Patch text for the target chapter, to replace or follow
`op:cy3-hcs-hall-comparison`:

```tex
\begin{lemma}[First missing lemma: oriented hCS--Hall comparison]
\label{lem:cy3-first-missing-oriented-hcs-hall}
\ClaimStatusOpen{}
Let \(X\) be a smooth Calabi--Yau threefold with holomorphic volume form
\(\Omega_X\), and fix a Dolbeault/Weiss/Ran-good Stein-polydisc cover
\(\mathfrak U\).  Assume:
\begin{enumerate}[label=\textup{(\roman*)}]
\item an anomaly-cancelled Costello--Li hCS quantisation
\(\Obs_{\hCS}^{q}(-,\mathfrak g)\), with compact-support convention and
\(\hbar\)-adic completion fixed;
\item a critical Hall atlas
\((\mathfrak M_{U,\mathbf d},f_{U,\mathbf d})\) for each
\(U\in\mathfrak U\), with
\[
  \CoHA^{\mathrm{or}}_{\mathrm{crit}}(U)_{\mathbf d}
  =
  H^{\mathrm{BM}}_{G_{\mathbf d}}
  \bigl(\Crit(f_{U,\mathbf d}),
        \phi_{f_{U,\mathbf d}}\otimes\mathscr L_{o_U}\bigr)
  [s(U,\mathbf d)](t(U,\mathbf d));
\]
\item strong orientation data \(o_U\), i.e. square roots of the virtual
determinant lines with overlap transport and vanishing residual
\(\check C^2(\mathfrak U,\mathbb Z/2)\) cocycle;
\item fixed perverse shifts \(s(U,\mathbf d)\), Tate twists
\(t(U,\mathbf d)\), HN/charge-adic completion, and equivariant
localisation;
\item coherent Thom--Sebastiani isomorphisms for every iterated
short-exact-sequence correspondence, compatible with the orientation
local systems and with the two parenthesisations of Hall multiplication.
\end{enumerate}
Then the comparison datum required by the CY3 bridge is a continuous
natural transformation on the whole DWR Cech/Ran nerve
\[
  \Theta_{\hCS\to\Hall}^{\mathrm{or}}:
  \Obs_{\hCS}^{q}(-,\mathfrak g)
  \longrightarrow
  \CoHA_{\mathrm{crit}}^{\mathrm{or}}(-)
\]
in \(\mathsf{FactCosh}^{\mathrm{or},\wedge}_{\Hall}(X)\), whose value on
each \(U\) is a quasi-isomorphism, which preserves factorisation
products, Hall convolution, completions, orientation transport, shifts,
Tate twists, and Thom--Sebastiani.  On \(U\simeq\mathbb C^3\) it reduces
to the Kontsevich--Soibelman/Schiffmann--Vasserot positive-half model
\(\CoHA(\mathbb C^3)=Y^+(\widehat{\mathfrak{gl}}_1)\); the
\(\mathcal W_{1+\infty}\) comparison is visible only after Drinfeld
doubling and Fock/evaluation.
\end{lemma}
```

This is the lemma whose proof would turn the local bridge into a
non-formal compact CY3 theorem. Without it, the target chapter should
keep the bridge conditional/open.

## ATTACK -> HEAL Cycles

### Cycle 1 - \(\Theta_{\hCS\to\Hall}^{\mathrm{or}}\)

ATTACK. A chartwise quasi-isomorphism
\[
  \Obs_{\hCS}^{q}(U,\mathfrak g)\to\CoHA_{\mathrm{crit}}(U)
\]
does not define the bridge. It may fail on binary factorisation
products, overlap restriction/corestriction maps, compact-support
variance, completions, or the residual orientation cocycle. The bridge
requires a morphism in
\(\mathsf{FactCosh}^{\mathrm{or},\wedge}_{\Hall}(X)\), not a list of
local vector-space identifications.

HEAL. State \(\Theta_{\hCS\to\Hall}^{\mathrm{or}}\) as a continuous
natural transformation on the full Dolbeault/Weiss/Ran Cech nerve. Its
source is the anomaly-gated Costello--Li observable cosheaf; its target
is the oriented completed critical-CoHA cosheaf. It must be compatible
with disjoint-union products, one-open Hall extension products, and all
overlap maps.

Patch text:

```tex
The datum \(\Theta_{\hCS\to\Hall}^{\mathrm{or}}\) is not a family of
chartwise quasi-isomorphisms.  It is a morphism in
\(\mathsf{FactCosh}^{\mathrm{or},\wedge}_{\Hall}(X)\), specified on
every simplex of the DWR Cech/Ran nerve and compatible with the
factorisation products, the Hall correspondence product, compact-support
variance, and the chosen completions.
```

### Cycle 2 - Oriented Critical CoHA

ATTACK. Writing \(\CoHA_{\mathrm{crit}}^{\mathrm{or}}\) as if
orientation were a decorative superscript loses the determinant-line
square root. In KS/Joyce motivic DT theory the orientation datum is a
real mathematical choice: it changes signs, the \(\mathbb L^{1/2}\)
normalisation, and the local systems on overlaps. Wall-crossing does
not trivialise this by itself. The toric chapter explicitly treats the
orientation-gerbe trivialisation as an independent hypothesis.

HEAL. The oriented critical-CoHA summand must be part of the comparison
datum:
\[
  H^{\mathrm{BM}}_{G_{\mathbf d}}
  \bigl(\Crit(f_{U,\mathbf d}),
        \phi_{f_{U,\mathbf d}}\otimes\mathscr L_{o_U}\bigr)
  [s(U,\mathbf d)](t(U,\mathbf d)).
\]
The orientation data \(o_U\) must transport on double overlaps and kill
the residual \(\mathbb Z/2\) cocycle on triple overlaps.

Patch text:

```tex
The orientation datum \(o_U\) is a square root of the virtual
determinant line on the derived critical chart, together with its
orientation local system and overlap coherences.  It is not shorthand
for \(K_{\mathfrak M_U}^{1/2}\).  A Hall comparison is not oriented
until the induced \(\mathbb Z/2\)-cocycle on triple overlaps is
trivialised or proved to vanish.
```

### Cycle 3 - Shifts and Tate Twists

ATTACK. The unshifted Borel--Moore group
\[
  H^{\mathrm{BM}}_{G_{\mathbf d}}(\Crit(f),\phi_f)
\]
is not yet a graded target for hCS observables. Perverse shifts, Tate
twists, and equivariant weights determine whether the comparison is
degree zero, whether the Hall product has the expected sign, and whether
the motivic \(\mathbb L^{1/2}\) normalisation matches the BV \(\hbar\)
normalisation. If these conventions are left implicit, the statement is
ungraded.

HEAL. Do not guess universal formulas for \(s(U,\mathbf d)\) or
\(t(U,\mathbf d)\). The manuscript already states that they are part of
the convention. The missing lemma must require them explicitly and
require \(\Theta_{\hCS\to\Hall}^{\mathrm{or}}\) to preserve the resulting
grading.

Patch text:

```tex
The shifts \(s(U,\mathbf d)\) and Tate twists \(t(U,\mathbf d)\) are not
normalisation noise: they are part of the target.  The comparison map is
a degree-zero quasi-isomorphism only after these choices are fixed, and
changing them changes the sign and weight conventions in Hall
convolution.
```

### Cycle 4 - Vanishing Cycles

ATTACK. Replacing the critical CoHA by ordinary equivariant cohomology
of a representation stack erases the potential \(W\), the Behrend sign,
and the perverse vanishing-cycle sheaf. That replacement is harmless
only in special degenerate loci where \(\phi_W\) has been proved to
reduce. The CY3 Hall product is built from critical loci and
vanishing-cycle coefficients.

HEAL. Keep the target as a critical CoHA:
\[
  \bigoplus_{\mathbf d}
  H^{\mathrm{BM}}_{G_{\mathbf d}}
  \bigl(\Crit(\mathrm{Tr}W_{\mathbf d}),
        \phi_{\mathrm{Tr}W_{\mathbf d}}\otimes\mathscr L_{o_U}\bigr)
  [s](t).
\]
For \(\mathbb C^3\), the Jordan quiver with
\(W=\mathrm{Tr}(X[Y,Z])\) is the input to the KS/SV theorem; the
positive-half result is not a license to drop \(\phi_W\) elsewhere.

Patch text:

```tex
The Hall target is the vanishing-cycle Borel--Moore complex of the
critical chart.  Ordinary cohomology of the representation stack appears
only after a separate reduction theorem for the chosen potential and
orientation datum.  In the CY3 bridge all Hall products are read with
the vanishing-cycle coefficient system present.
```

### Cycle 5 - Thom--Sebastiani and Hall Multiplication

ATTACK. Associativity of the Hall product is not just associativity of
extensions. With potentials, multiplication uses the
Thom--Sebastiani isomorphism for vanishing cycles along the extension
correspondence. The two parenthesisations of three extensions can differ
by signs, Tate twists, or transported orientation local systems. hCS
factorisation products over disjoint opens do not automatically supply
this TS coherence.

HEAL. The missing comparison must include a coherent TS system for all
iterated extension correspondences and require \(\Theta\) to preserve it.
Only then can the BV/factorisation product be compared to Hall
convolution.

Patch text:

```tex
For composable extension correspondences, the two Thom--Sebastiani
identifications of
\(\phi_{f_1}\boxtimes\phi_{f_2}\boxtimes\phi_{f_3}\)
with the vanishing-cycle sheaf of the total potential must agree after
the stated shifts, Tate twists, and orientation transports.  This
coherence is part of \(\Theta_{\hCS\to\Hall}^{\mathrm{or}}\), not a
consequence of the underlying extension stack alone.
```

### Cycle 6 - \(\mathbb C^3\): \(Y^+\), Not \(\mathcal W_{1+\infty}\)

ATTACK. The false shortcut
\[
  \CoHA(\mathbb C^3)=\mathcal W_{1+\infty}
\]
collapses three category changes: positive-half Hall algebra,
Drinfeld double/full Yangian, and vacuum-module vertex algebra. It
turns an associative algebra into a vertex algebra without the double or
evaluation map.

HEAL. Keep the exact chain:
\[
  \CoHA(\mathbb C^3)
  =
  Y^+(\widehat{\mathfrak{gl}}_1)
  \hookrightarrow
  D(Y^+)=Y(\widehat{\mathfrak{gl}}_1)
  \xrightarrow{\mathrm{ev}_\lambda}
  \mathrm{End}(\mathcal W_{1+\infty}[\lambda]\text{-vac}).
\]
The direct algebraic identification is only the first equality.

Patch text:

```tex
In the \(\mathbb C^3\) chart the reduction condition for
\(\Theta_{\hCS\to\Hall}^{\mathrm{or}}\) is
\(\CoHA(\mathbb C^3)=Y^+(\widehat{\mathfrak{gl}}_1)\).  The
\(\mathcal W_{1+\infty}\) object appears only after passing to the
Drinfeld double and then to a chosen Fock/evaluation representation.
No statement in the hCS--Hall comparison may identify the positive-half
CoHA directly with the vertex algebra.
```

### Cycle 7 - Toric Descent and \(K3\times E\) Character Evidence

ATTACK. The toric chapter has two tempting overpromotions. First,
chartwise toric \(Y^+\) can be misread as a global hCS--Hall theorem.
Second, the \(K3\times E\) identity
\[
  \chi_{\mathrm{gr}}(\CoHA_{K3\times E})=1/\Phi_{10}
\]
can be misread as an algebra-level construction of the Hall--Drinfeld
Borcherds object.

HEAL. Keep three levels distinct:

1. Toric Hall side: \(Y^+\) charts and shuffle products, with orientation
   and NCCR overlap hypotheses.
2. hCS comparison: \(\Theta_{\hCS\to\Hall}^{\mathrm{or}}\), open or
   conditional.
3. \(K3\times E\): DT/Igusa character identity, not construction of the
   positive half, Hopf pairing, completion, or Hall--Borcherds bracket.

Patch text:

```tex
The equality of graded characters is evidence for the Hall--Borcherds
endpoint, not the endpoint itself.  Transporting the CoHA object to
\(\mathbf H_{\Delta_5}\) still requires the oriented critical positive
half, a nondegenerate Hall pairing, the Drinfeld double completion, the
Hall--Borcherds bracket comparison, and the hCS--Hall comparison
\(\Theta_{\hCS\to\Hall}^{\mathrm{or}}\).
```

## Residual Open Obligations

1. Construct \(\Theta_{\hCS\to\Hall}^{\mathrm{or}}\) on the DWR nerve,
   not only on affine charts.
2. Prove or choose strong orientation data and trivialise the residual
   triple-overlap \(\mathbb Z/2\) cocycle.
3. Fix shifts and Tate twists in the critical-CoHA target and verify the
   comparison is degree zero.
4. Prove TS coherence for iterated extension correspondences with those
   twists and local systems.
5. Verify the \(\mathbb C^3\) reduction lands in \(Y^+\) and only then
   passes to \(D(Y^+)\) and evaluation.
6. Keep \(K3\times E\) character identities separate from algebra-level
   Hall--Borcherds construction.

## Compact Report

The Hall lane converges to a precise obstruction, not a contradiction.
The manuscript should preserve the current spine:
\[
  \PhiFA_3
  \dashrightarrow
  \CoHA_{\mathrm{crit}}^{\mathrm{or}}
  \to
  Y^+
  \to
  D(Y^+)
  \to
  \mathcal W_{1+\infty}.
\]
The first arrow is the missing theorem. The \(\mathbb C^3\) core proves
only the positive-half Hall statement. Orientation data, shifts/Tate
twists, vanishing cycles, and Thom--Sebastiani coherence are not
bookkeeping; they are exactly the data that make the arrow meaningful.
