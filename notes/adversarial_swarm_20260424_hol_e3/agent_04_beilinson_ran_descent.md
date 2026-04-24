# Agent 04: Beilinson/Ran Descent

## Scope

Claim attacked: the Ran/Dolbeault/Weiss descent needed to pass from the
local CY3 holomorphic Chern--Simons / Dolbeault CE model to a global
stage-one holomorphic \(E_3\)-factorisation object and then, when a Hall
comparison is invoked, to a global Hall-valued factorisation cosheaf.

Files and sources read:

- `CLAUDE.md` and `AGENTS.md`.
- `chapters/theory/cy3_chain_level_bridge.tex`.
- `chapters/theory/cy_to_chiral.tex`, especially
  `thm:toric-chart-gluing`, `thm:e1-descent-degeneration`, and the
  \(d=3\) status summary.
- `bibliography/references.tex`.
- Primary reference anchors: Beilinson--Drinfeld 2004; Costello--
  Gwilliam 2017/2021; Francis--Gaitsgory 2012; Costello--Li
  arXiv:1606.00365; Kontsevich--Soibelman arXiv:0811.2435;
  Schiffmann--Vasserot 2013; Lurie, `Higher Algebra`.

No chapters or compute files were edited. No build was run.

## Verdict

The local shape in `cy3_chain_level_bridge.tex` is mostly correct:
`def:cy3-many-variable-chiral-ce`,
`def:hall-valued-factorisation-cosheaf-target`,
`prop:cy3-local-to-toric-descent-package`, and
`op:cy3-hcs-hall-comparison` already name the right pieces. The false
global theorem to attack is the inference
\[
  \{\Theta_U \text{ on charts}\}
  \Longrightarrow
  \text{global hCS-to-Hall theorem}
\]
without a full DWR-site morphism, support/completion convention,
orientation cocycle trivialisation, and hypercover descent calculation.

The honest theorem is smaller:

1. On a holomorphic polydisc \(P\), the local model is the continuous
   Dolbeault--chiral CE object
   \[
     C^\bullet_{\mathrm{Lie,cont}}
     \bigl(\Omega_c^{0,\bullet}(P,J^\infty_{\mathrm{hol}}\mathfrak l_\cC)[1],
     \mathbb C\bigr),
   \]
   not ordinary \(C^\bullet(\mathfrak g)\) except after taking the
   locally constant shadow.
2. On a DWR-good Weiss cover, local data descends only if the maps
   \(\Theta_U\) extend to a continuous natural transformation on the
   whole Cech/Ran nerve, compatible with factorisation products,
   compact-support variance, completions, Hall correspondences,
   Thom--Sebastiani isomorphisms, and orientation local systems.
3. The global non-toric compact CY3 statement is still open. The toric
   Hall-side hocolim can be kept as a toric theorem only after splitting
   it from the hCS-to-Hall comparison, which remains conditional on
   `op:cy3-hcs-hall-comparison`.

## Required local-to-global hypotheses

A descent theorem in this lane must assume the following data.

- A DWR site \(\mathsf{DWR}(X)\) with a Weiss-cofinal basis of
  holomorphic Stein polydiscs and finite intersections refined by
  holomorphic polydiscs.
- A homotopy factorisation cosheaf of local observables on that site,
  not only a chartwise assignment.
- Continuous CE cochains with a fixed topological vector-space
  convention: nuclear Frechet/complete bornological, completed symmetric
  algebra, continuous dual, and \(\hbar\)-adic completion on the hCS
  side.
- Charge/HN-adic and equivariant-localised completion on the Hall side,
  with exactness strong enough to commute with the relevant finite
  homotopy colimits.
- A compact-support convention and variance convention: extension by
  zero for compactly supported fields, and the induced covariant or
  contravariant map on observables explicitly named.
- A comparison map \(\Theta\) on every level of the Cech/Ran nerve,
  not only on \(0\)-simplices.
- Compatibility on overlaps with holomorphic coordinate changes,
  orientation-torsor transport, and determinant-line square roots.
- Vanishing or chosen trivialisation of the residual \(\mathbb Z/2\)
  orientation cocycle on triple overlaps.
- Thom--Sebastiani compatibility for iterated extension
  correspondences, including signs, Tate twists, and orientation local
  systems.
- A final global status split: toric Hall-side hocolim, conditional
  hCS-to-Hall comparison, and open non-toric compact CY3 theorem.

## ATTACK -> HEAL cycles

### Cycle 1: Factorisation cosheaves

ATTACK. The phrase "the chartwise quasi-isomorphisms glue" is too weak.
A family of quasi-isomorphisms
\[
  \Theta_U:\Obs_{\hCS}^q(U,\mathfrak g)\to
  \CoHA_{\mathrm{crit}}^{\mathrm{or}}(U)
\]
on holomorphic charts does not imply global descent. It can fail on
binary factorisation products, on the \(U_i\cap U_j\) maps, or on the
triple-overlap orientation cocycle. A list of quasi-isomorphisms is not
a morphism in
\(\mathsf{FactCosh}_{\Hall}^{\mathrm{or},\wedge}(X)\).

HEAL. Require \(\Theta\) as a morphism of factorisation cosheaves on the
entire DWR Cech/Ran nerve. It must commute with disjoint-union products,
one-open Hall extension products, and all restriction/corestriction maps
on overlaps.

Patch text:

```tex
The comparison datum is not a family of chartwise quasi-isomorphisms.
It is a continuous natural transformation on the whole
Dolbeault/Weiss/Ran Cech nerve,
\[
  \Theta_\bullet:
  \Obs_{\hCS}^q(-,\mathfrak g)\longrightarrow
  \CoHA_{\mathrm{crit}}^{\mathrm{or}}(-),
\]
viewed in
\(\mathsf{FactCosh}_{\Hall}^{\mathrm{or},\wedge}(X)\).  Thus for every
finite string \(U_0,\ldots,U_p\) in the chosen DWR cover the map on
\(U_0\cap\cdots\cap U_p\) is specified, continuous, compatible with the
coface maps, and multiplicative for disjoint holomorphic polydiscs.
Only under this nerve-level hypothesis does Weiss codescent identify
the global object with the homotopy colimit of the local ones.
```

Status after heal: conditional, but correctly typed.

### Cycle 2: Holomorphic polydiscs

ATTACK. The local normal form on \(P=D_1\times D_2\times D_3\) is being
used as if every open in the descent cover were canonically a
\(\mathbb C^3\)-chart. That is false. Intersections of holomorphic
polydiscs need not be coordinate polydiscs without refinement, and
holomorphic coordinate changes act nontrivially on
\(J^\infty_{\mathrm{hol}}\mathfrak l_\cC\), residues, and the CY volume
form.

HEAL. Use a Weiss-cofinal holomorphic polydisc basis and formulate the
descent over refinements. On overlaps, the comparison map must be
invariant under holomorphic coordinate changes preserving the CY volume
form up to the named Jacobian/orientation factor.

Patch text:

```tex
The word "polydisc" is a basis condition, not a global coordinate
choice.  We choose a Weiss-cofinal holomorphic basis
\(\mathcal B_{\mathrm{poly}}\subset\mathsf{DWR}(X)\) such that every
finite intersection in the cover admits a refinement by elements of
\(\mathcal B_{\mathrm{poly}}\).  The Dolbeault--chiral CE model is
computed on this basis, and descent is taken after refinement.  On
overlaps, changes of coordinates act on
\(J^\infty_{\mathrm{hol}}\mathfrak l_\cC\), the iterated-residue
operations, and \(\Omega_X\); the comparison map \(\Theta\) is required
to intertwine these actions with the Hall-side orientation transport.
```

Status after heal: local theorem valid on the basis; global theorem
requires refined Weiss descent.

### Cycle 3: Continuous CE and completions

ATTACK. Ordinary CE cochains do not see the topological completion in
the hCS local Lie algebra. The object in
`def:cy3-many-variable-chiral-ce` is
\[
  C^\bullet_{\mathrm{Lie,cont}}(\mathfrak L_\cC(P),\mathbb C)
  =
  \widehat{\mathrm{Sym}}(\mathfrak L_\cC(P)^\vee[-1]).
\]
Replacing this by algebraic \(C^\bullet\), or moving hocolims through
duals without a topological hypothesis, produces a fake descent theorem.
The dual of a filtered colimit of compactly supported fields is not
automatically the limit of the duals in the category being used.

HEAL. State the topological category and the exactness of completion.
The hCS side uses \(\hbar\)-adic and continuous-dual completion; the
Hall side uses charge/HN-adic and equivariant-localised completion.
The comparison map must be continuous and filtration-preserving.

Patch text:

```tex
All CE complexes in the comparison are continuous CE complexes.  The
hCS side is taken in complete nuclear/locally convex chain complexes
with \(\hbar\)-adic completion and completed symmetric algebra
\(\widehat{\mathrm{Sym}}\).  The Hall side is completed in the
charge/HN-adic and equivariant-localised topology.  The comparison
\(\Theta\) is a filtered continuous map; the completion functors are
assumed exact on the finite DWR hypercover used for descent, so that the
homotopy colimit is computed after completion without changing the
quasi-isomorphism type.
```

Status after heal: the CE comparison is topologically meaningful.

### Cycle 4: Compact supports

ATTACK. Compact supports cannot be hidden inside the notation
\(\Omega_c^{0,\bullet}\). For an inclusion \(U\subset V\), compactly
supported fields have extension-by-zero maps \(L_c(U)\to L_c(V)\), while
observables built as functions or CE cochains have the induced variance
determined by the chosen convention. Calling every map a "restriction"
is ambiguous and may reverse the arrows in the Cech/Ran diagram.

HEAL. Name the variance convention before descent. The factorisation
product over disjoint opens uses extension by zero on compact supports;
overlap comparison must use the induced pullback/pushforward convention
on observables consistently with the Hall-side correspondences.

Patch text:

```tex
Compact support fixes the variance.  For \(U\subset V\) the local Lie
algebras of compactly supported Dolbeault fields are related by
extension by zero \(j_!: \mathfrak L_c(U)\to \mathfrak L_c(V)\).  The
observable maps are the maps induced from this convention on continuous
CE cochains.  In the DWR Cech nerve we write these maps explicitly
rather than calling all of them restrictions.  The Hall-side overlap map
is required to match the same variance through the extension
correspondence and its Borel--Moore push-pull map.
```

Status after heal: support does not silently flip the descent diagram.

### Cycle 5: Restrictions to overlaps

ATTACK. The phrase "compatible with restriction to overlaps" is not
strong enough. On a double overlap \(U_i\cap U_j\), the hCS side carries
coordinate-transition data and compact-support variance; the Hall side
carries derived critical charts, vanishing cycles, shifts, Tate twists,
and orientation local systems. On a triple overlap, the determinant-line
square roots may differ by a \(\mathbb Z/2\)-cocycle. A local
orientation datum \(o_U\) does not automatically glue.

HEAL. Replace "restriction to overlaps" by an explicit cocycle condition
in the orientation gerbe. The data must trivialise the residual
\(\mathbb Z/2\)-class on triple overlaps and commute with
Thom--Sebastiani for all iterated extension correspondences.

Patch text:

```tex
Overlap compatibility means the following cocycle equation.  On every
double overlap \(U_{ij}\), the two transported orientation data
\(o_i|_{U_{ij}}\) and \(o_j|_{U_{ij}}\) are identified by a specified
isomorphism of determinant-line square roots, compatible with shifts and
Tate twists.  On every triple overlap \(U_{ijk}\), the product of the
three transition isomorphisms is the identity in the orientation
\(\mathbb Z/2\)-gerbe.  The same transition data is required to commute
with Thom--Sebastiani isomorphisms for iterated extension
correspondences.  Without this condition the Hall product may be
associative chartwise but fail to define a global oriented Hall cosheaf.
```

Status after heal: orientation becomes a theorem hypothesis, not a
notation.

### Cycle 6: Weiss descent

ATTACK. "Weiss descent for factorisation algebras then identifies the
global observable algebra with the homotopy colimit" is true only after
the assignment is already a homotopy cosheaf for Weiss covers. It is not
automatic from \(E_1\)-algebra structure, nor from the contractibility of
ordered configuration spaces. The theorem
`thm:e1-descent-degeneration` in `cy_to_chiral.tex` overstates the
principle if read as "all \(E_1\)-Cech spectral sequences have no
higher Cech terms." Strictness of \(E_1\)-multiplication does not imply
acyclicity of an arbitrary cover.

HEAL. Keep a finite acyclic atlas theorem where the Cech nerve has been
computed; do not state a universal \(E_1\)-descent degeneration theorem.
For the hCS/Dolbeault lane, require the DWR cover to be Weiss-good and
cofinal for finite configurations, and compute descent in the target
\((\infty,1)\)-category.

Patch text:

```tex
Weiss descent enters only after both assignments have been shown to be
homotopy factorisation cosheaves on the chosen DWR site.  The
contractibility of ordered \(E_1\)-operation spaces removes braiding
coherences; it does not by itself annihilate higher Cech cohomology of
an arbitrary atlas.  The descent statement is therefore restricted to
finite DWR-good atlases whose Cech nerve is acyclic for the completed
observable complexes under consideration.  On that scope the global
object is computed by the homotopy colimit of the nerve-level diagram.
```

Status after heal: `thm:e1-descent-degeneration` should be scoped to
finite acyclic/tested atlases or made conditional.

### Cycle 7: Global descent status

ATTACK. The dangerous global claim is:
\[
  \text{toric/local CoHA gluing}
  =
  \text{global hCS-to-Hall comparison}
  =
  \text{compact CY3 theorem}.
\]
This conflates three statements. The toric Hall hocolim is a Hall-side
construction. The hCS-to-Hall map is the open comparison
`op:cy3-hcs-hall-comparison`. The non-toric compact CY3 theorem needs a
finite DWR atlas, a tilting/quiver-with-potential presentation, analytic
completion, and orientation descent. The status summary in
`cy_to_chiral.tex` is already honest that the hCS-to-critical-CoHA map
is not proved by the \(\mathbb C^3\) Hall verification.

HEAL. Split the theorem statements:

- proved/toric: Hall-side quiver-chart hocolim under explicit toric
  atlas and mutation equivalence hypotheses;
- conditional: Costello--Li/hCS comparison with that hocolim, assuming
  the oriented DWR-level \(\Theta\);
- open: arbitrary non-toric compact CY3 global descent.

Patch text:

```tex
The toric quiver-chart theorem is a theorem about the Hall-side
homotopy colimit on its toric atlas.  Its comparison with holomorphic
Chern--Simons observables is not part of the theorem unless the
orientation-preserving DWR-level map
\(\Theta_{\hCS\to\Hall}^{\mathrm{or}}\) of
Problem~\ref{op:cy3-hcs-hall-comparison} has first been supplied.
For non-toric compact CY$_3$ varieties the corresponding global descent
statement remains open: it requires a finite DWR-good atlas, compatible
critical charts or tilting data, completed continuous CE descent,
orientation-gerbe trivialisation, and Thom--Sebastiani coherence.
```

Status after heal: no fake global theorem remains.

## Recommended manuscript repairs

1. In `prop:cy3-local-to-toric-descent-package`, replace the sentence
   beginning "Weiss descent for factorisation algebras then identifies"
   by the Cycle 6 patch text, or add it immediately before that
   sentence.
2. In `op:cy3-hcs-hall-comparison`, expand "compact-support
   convention" using the Cycle 4 patch text.
3. In `def:hall-valued-factorisation-cosheaf-target`, add a sentence
   that the object is defined on the whole DWR Cech/Ran nerve, not only
   on chart objects.
4. In `thm:toric-chart-gluing`, split part (iv) into a conditional
   corollary depending on `op:cy3-hcs-hall-comparison`; otherwise it
   contradicts the local bridge chapter's status discipline.
5. In `thm:e1-descent-degeneration`, replace the universal claim
   "For \(E_1\)-algebras" by a finite acyclic atlas hypothesis. The
   proof's Step 3 should not infer vanishing of higher Cech cohomology
   from strict algebra maps alone.
6. Remove or conditionalise the \(K3\times E\) entry under "explicit
   degeneration for standard CY3 atlases" unless a finite atlas and
   orientation-compatible Cech calculation are supplied.

## Final status

CONVERGED as an adversarial note. The exact obstruction is not the local
Dolbeault CE model; it is global DWR descent with continuous completion,
compact-support variance, overlap orientation, and Hall-side comparison.
The local-to-toric package is salvageable as a conditional theorem. The
non-toric compact CY3 hCS-to-Hall global theorem remains open.
