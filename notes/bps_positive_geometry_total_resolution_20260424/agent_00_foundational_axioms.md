# Foundational Axioms for Chambered BPS Positive Geometry

Date: 2026-04-24.

Scope.  This note axiomatizes the strengthened chambered BPS positive
geometry as a localized motivic-homotopical object.  It owns the
foundational layer: the exact object, its axioms, its functoriality,
local-to-global descent, decategorification, theorem/proof statuses, and
failure modes healed into stronger statements.

Local anchors.

```text
notes/master_synthesis_chambered_bps_positive_geometry_20260424.md:742
notes/master_synthesis_chambered_bps_positive_geometry_20260424.md:777
notes/master_synthesis_chambered_bps_positive_geometry_20260424.md:857
notes/master_synthesis_chambered_bps_positive_geometry_20260424.md:897
notes/master_synthesis_chambered_bps_positive_geometry_20260424.md:951
notes/master_synthesis_chambered_bps_positive_geometry_20260424.md:1104
notes/master_synthesis_chambered_bps_positive_geometry_20260424.md:1124
chapters/theory/cy_to_chiral.tex:9311
chapters/theory/cy_to_chiral.tex:10048
chapters/examples/cy_d_kappa_stratification.tex:2253
chapters/examples/cy_d_kappa_stratification.tex:2553
chapters/examples/cy_d_kappa_stratification.tex:2670
/Users/raeez/igusa-cusp-form/proj.tex:68
/Users/raeez/igusa-cusp-form/proj.tex:416
/Users/raeez/igusa-cusp-form/proj.tex:431
/Users/raeez/igusa-cusp-form/proj.tex:461
```

## 0. The Primitive Question

The toric effective positive geometry records a rational polyhedral cone,
a quiver critical stack, and a critical CoHA.  That object is too small
for a general BPS spectrum.  The missing primitive is not another cone.
It is the local motivic Hall cosheaf whose numerical shadow is the cone.

The sought object must remember:

```tex
derived critical geometry
orientation signs
vanishing-cycle coefficients
Harder--Narasimhan sectors
motivic Hall multiplication
Kontsevich--Soibelman transport
realization to numerical invariants
```

The strengthened answer is therefore the object

```tex
P^{BPS,motloc}_{\sigma,S,o,T_{\mathrm{eq}}}(X)
```

and not its Euler shadow.  The toric cone is recovered only after
decategorification.

## 1. Input Package

Let `C` be a proper or locally finite CY3 category attached to the target
`X`, with numerical charge lattice

```tex
\Gamma_C = K_0^{num}(C)
```

and Euler form

```tex
\langle \alpha,\beta\rangle
  = \chi_C(E_\alpha,E_\beta)-\chi_C(E_\beta,E_\alpha).
```

The input package is:

```tex
\mathfrak I(X,\sigma,S,o,T_{\mathrm{eq}})
 =
 (C,
  \Gamma_C,
  \langle-,-\rangle,
  Q,
  \sigma=(Z,\mathcal P),
  S,
  o,
  T_{\mathrm{eq}},
  \mathcal M_C^{(-1)},
  \mathcal A^{or}_{crit},
  \mathsf{Mot}).
```

Here:

```tex
Q:\Gamma_C\otimes\mathbb R\to\mathbb R
```

is a support-property quadratic form, negative definite on
`\ker Z` and nonnegative on active semistable classes.

`S \subset \mathbb C^*` is an open convex strict sector of angular width
`< pi`; no active BPS ray lies on `\partial S`.

`o` is orientation data: a square root of the virtual canonical line on
the oriented critical atlas, together with transition coherences.

`T_{\mathrm{eq}}` is the equivariance group: torus, reduced
automorphism group, orbifold inertia group, or lattice-polarized
automorphic group, depending on the stratum.

`\mathcal M_C^{(-1)}` is the derived moduli stack of objects of `C` with
its CY3 `(-1)`-shifted symplectic structure.  At an object `E`,

```tex
T_E\mathcal M_C = RHom_C(E,E)[1].
```

`\mathcal A^{or}_{crit}` is an oriented critical atlas:

```tex
\{(U_i,f_i,G_i,\iota_i,K_{vir,i}^{1/2})\}_{i\in I}
```

where `Crit(f_i)/G_i` presents the truncation locally, the charts agree
on overlaps by d-critical transition data, and the square roots glue.

`\mathsf{Mot}` is the strongest coefficient target available for the
geometry: motivic spectra, Voevodsky motives, monodromic mixed Hodge
modules, or a cohomological realization.  A weaker realization is a
functor out of `\mathsf{Mot}`, not a replacement for the object.

## 2. Exact Object

Definition.  The chambered localized motivic BPS positive geometry is
the tuple

```tex
P^{BPS,motloc}_{\sigma,S,o,T_{\mathrm{eq}}}(X)
 =
 (StabSite(C),
  Sect_\sigma(C),
  \mathcal M_C^{(-1)-symp},
  \mathcal A^{or}_{crit},
  \Phi^{vc}_{\mathcal A,o},
  \mathcal H^{mot}_{\sigma,S,o,T_{\mathrm{eq}}},
  \mu^{mot}_{Hall},
  Fil^{HN}_{\sigma,S},
  \widehat{\mathbb T}^{mot}_{\Gamma,S,o},
  Int^{mot},
  Real,
  Dec).
```

The sites are:

```tex
StabSite(C):
  objects = stability chambers;
  morphisms = chamber inclusions and admissible wall specializations.

Sect_\sigma(C):
  objects = strict sectors S;
  covers = finite ordered decompositions
           S = S_1\star\cdots\star S_r
           compatible with decreasing phase.
```

The vanishing-cycle coefficient system is

```tex
\Phi^{vc}_{\mathcal A,o}(\gamma)
  \in \mathsf{Mot}(\mathcal M_{\sigma}(\gamma))
```

obtained by gluing local vanishing cycles
`\phi_{f_i}` twisted by the orientation line.

The motivic Hall object is

```tex
\mathcal H^{mot}_{\sigma,S,o,T_{\mathrm{eq}}}
 =
\widehat{\bigoplus}_{\gamma\in\Gamma^{ss}_{\sigma,S}}
R\Gamma^{BM}_{T_{\mathrm{eq}}}
\bigl(\mathcal M_\sigma(\gamma),\Phi^{vc}_{\mathcal A,o}(\gamma)\bigr).
```

The completion is along the BPS-generated monoid

```tex
\Gamma^+_{\sigma,S,o}
 =
\mathbb N\langle
  \gamma\in\Gamma^{ss}_{\sigma,S}:
  \Omega^{mot}_{\sigma,o}(\gamma)\ne 0
\rangle.
```

This order is part of the definition: semistable support comes first,
BPS support comes after vanishing cycles and integration, and the
completion monoid comes last.

The motivic quantum torus is

```tex
\widehat{\mathbb T}^{mot}_{\Gamma,S,o}
 =
\prod_{\gamma\in\Gamma^+_{\sigma,S,o}}
R_{mot}\,x_\gamma,
```

with product

```tex
x_\alpha x_\beta
 =
\mathbb L^{\langle\alpha,\beta\rangle/2}
\epsilon_o(\alpha,\beta)x_{\alpha+\beta}.
```

The decategorification map is fixed, not optional:

```tex
Dec
 =
support\circ K_0\circ Int^{mot}.
```

The equality

```tex
Dec(P^{BPS,motloc}_{\sigma,S,o,T_{\mathrm{eq}}}(X))
 =
P^{BPS,\bullet}_{\sigma,S,o,T_{\mathrm{eq}}}(X)
```

is structure.  It prevents the combinatorial positive geometry from
floating free of derived critical geometry.

## 3. Axioms

### Axiom A0: Support Property

For every semistable object `E` of class `\gamma`,

```tex
Q(\gamma)\ge 0,
```

and `Q` is negative definite on `\ker Z`.  For every finite radius and
strict sector,

```tex
\{\gamma\in\Gamma^{ss}_{\sigma,S}: Q(\gamma)\ge 0,\ |Z(\gamma)|\le R\}
```

is finite modulo the chosen completion.

Proof role.  This axiom makes all finite truncations finite and makes
the completed Hall product meaningful.

### Axiom A1: Oriented Critical Descent

The derived moduli stack admits an oriented critical atlas
`\mathcal A^{or}_{crit}`.  On triple overlaps the determinant-line
transition functions have trivial obstruction class:

```tex
[\delta(K_{vir}^{1/2})]\in H^2(\mathcal M_C,\mathbb Z/2)
```

is zero after the specified orientation choice `o`.

Proof role.  Without A1 the sign
`\epsilon_o(\alpha,\beta)` in the quantum torus is not defined, and the
Igusa character `\nu_{\Delta_5}` cannot be recovered at the automorphic
boundary.

### Axiom A2: Vanishing-Cycle Coefficients

The local critical functions in `\mathcal A^{or}_{crit}` determine a
glued coefficient system

```tex
\Phi^{vc}_{\mathcal A,o}
```

in `\mathsf{Mot}`.  For direct sums and extensions, Thom--Sebastiani
gives coherent morphisms

```tex
\Phi^{vc}_{\gamma_1}\boxtimes\Phi^{vc}_{\gamma_2}
  \longrightarrow
\Phi^{vc}_{\gamma_1+\gamma_2}.
```

Proof role.  This is the coefficient-level origin of Hall
multiplication.

### Axiom A3: Hall Correspondence

For classes `\gamma_1,\gamma_2`, the extension stack fits into a
correspondence

```tex
\mathcal M_\sigma(\gamma_1)\times\mathcal M_\sigma(\gamma_2)
\xleftarrow{p}
\mathcal E_\sigma(\gamma_1,\gamma_2)
\xrightarrow{q}
\mathcal M_\sigma(\gamma_1+\gamma_2).
```

The Hall product is the pull--push operation

```tex
\mu^{mot}_{Hall}=q_!p^*
```

with the coefficient transport from A2.

Proof role.  The positive algebra is built by extensions, not by a
chosen basis of charges.

### Axiom A4: 2-Segal Associativity

The stacks of flags of extensions form a 2-Segal object.  The two
parenthesizations of a triple extension produce the same map

```tex
\mathcal H_{\gamma_1}^{mot}\otimes
\mathcal H_{\gamma_2}^{mot}\otimes
\mathcal H_{\gamma_3}^{mot}
\longrightarrow
\mathcal H_{\gamma_1+\gamma_2+\gamma_3}^{mot}.
```

Proof role.  Associativity is not imposed by hand; it is the shadow of
the geometry of flags.

### Axiom A5: Harder--Narasimhan Factorization

Every object in the sector has a unique HN filtration with semistable
factors of strictly decreasing phase.  For an ordered sector cover

```tex
S=S_1\star\cdots\star S_r
```

the multiplication map is an isomorphism after completion:

```tex
\mathcal H^{mot}_{\sigma,S}
 \cong
\mathcal H^{mot}_{\sigma,S_1}\widehat\otimes\cdots
\widehat\otimes
\mathcal H^{mot}_{\sigma,S_r}.
```

Proof role.  This axiom is the local meaning of positivity.  A chamber
is positive because it admits ordered HN multiplication.

### Axiom A6: Motivic Integration

There is a continuous algebra homomorphism

```tex
Int^{mot}:
\mathcal H^{mot}_{\sigma,S,o,T_{\mathrm{eq}}}
\longrightarrow
\widehat{\mathbb T}^{mot}_{\Gamma,S,o}
```

whose product formula is governed by the Euler pairing and orientation
sign:

```tex
Int^{mot}(a*b)=Int^{mot}(a)Int^{mot}(b).
```

Proof role.  This is the bridge from Hall geometry to
Kontsevich--Soibelman wall-crossing.

### Axiom A7: Realization Compatibility

Every realization

```tex
Real_\rho:\mathsf{Mot}\to\mathsf V_\rho
```

commutes with Hall product, HN completion, orientation signs,
Tate twists, and sector transport.  The realization tower is

```tex
motivic object
\to monodromic mixed Hodge object
\to K_0[\mathbb L^{\pm 1/2}]
\to motivic quantum torus
\to Euler-specialized torus
\to numerical BPS invariants.
```

Proof role.  Numerical invariants are shadows.  A realization that
does not preserve multiplication cannot define the positive geometry.

### Axiom A8: Kontsevich--Soibelman Flatness

For any wall crossing between adjacent stability chambers, the sector
objects are identified by conjugation with the ordered product of active
ray factors in the completed motivic torus.  Around every codimension-two
joint and every finite truncation,

```tex
\prod_{\partial \Delta}^{ordered} A_{\ell}=1.
```

Proof role.  This is the flatness condition for the chamber-sector
local system.

### Axiom A9: Boundary Realization

If the geometry has a Lorentzian automorphic boundary, the object admits
an additional realization

```tex
AutBorch:
K_0(BPS^{mot,prim})\longrightarrow M_*(G,\nu)
```

compatible with the chamber, orientation character, divisor, and
denominator product.

For `K3 x E`, the first boundary value is fixed by the Igusa package:

```tex
\phi_{0,1}=(1/2)Z_{K3},\qquad
\operatorname{Borch}(\phi_{0,1})=\Delta_5,
```

```tex
D_5=64^{-1}\Delta_5,\qquad
\operatorname{den}(\mathfrak g_{\Delta_5})=D_5(2Z),
```

```tex
\Delta_{10}=\Delta_5^2,\qquad
Z^X_{\square}=C_{\square}\Delta_5^{-2}.
```

Proof role.  The non-toric boundary is a theorem-grade constraint on
the axioms, not a decorative example.

## 4. Formal Theorems

### Theorem 4.1: Existence of the Axiomatic Object

Given an input package satisfying A0--A9, the tuple

```tex
P^{BPS,motloc}_{\sigma,S,o,T_{\mathrm{eq}}}(X)
```

is a well-defined completed motivic Hall cosheaf on the
chamber-sector site, equipped with motivic integration and
decategorification.

Proof.  A1 and A2 produce coefficient objects on the critical stack.
A3 defines multiplication by extension pull--push.  A4 proves
associativity.  A5 supplies sector gluing and the completion topology.
A6 maps the completed Hall object to the completed motivic quantum
torus.  A7 transports the construction through realizations.  A8 gives
flat chamber transport.  A9 adds the automorphic boundary when present.
The displayed tuple is therefore defined in every component, and all
structure maps commute by the axioms that define them.

Status: proved here as an axiomatic theorem.

### Theorem 4.2: Sector Descent

The assignment

```tex
S\longmapsto
\mathcal H^{mot}_{\sigma,S,o,T_{\mathrm{eq}}}
```

is a cosheaf on `Sect_\sigma(C)` after HN completion.  For an ordered
cover `S=S_1\star\cdots\star S_r`,

```tex
\mathcal H^{mot}_{\sigma,S}
 \cong
\mathcal H^{mot}_{\sigma,S_1}\widehat\otimes\cdots
\widehat\otimes
\mathcal H^{mot}_{\sigma,S_r}.
```

Proof.  HN uniqueness expresses every object in `S` as an ordered
extension of semistable factors lying in the smaller sectors.  The flag
stack of such filtrations is the iterated extension stack.  A3 gives
the multiplication map; A4 identifies all parenthesizations; A5 says
that the completed multiplication map is an isomorphism.  This is
exactly the cosheaf gluing axiom for ordered sector covers.

Status: proved here from A3--A5; theorem-grade for geometries satisfying
HN existence, support, and completion hypotheses.  The master synthesis
records this formal target at lines 897--922.

### Theorem 4.3: Decategorification

The decategorified chambered BPS positive geometry is

```tex
P^{BPS,\bullet}_{\sigma,S,o,T_{\mathrm{eq}}}(X)
 =
Dec(P^{BPS,motloc}_{\sigma,S,o,T_{\mathrm{eq}}}(X)).
```

It consists of:

```tex
(\Gamma_C^{or},
 Q,
 \Gamma^{ss}_{\sigma,S},
 \Gamma^{BPS,\bullet}_{\sigma,S,o},
 \Gamma^+_{\sigma,S,o},
 \Omega^\bullet_{\sigma,o},
 \widehat{\mathbb T}^{\bullet}_{\Gamma,S,o},
 D^{KS,\bullet}_{\sigma,S,o}).
```

Proof.  `Int^{mot}` sends motivic Hall classes to the motivic torus.
`K_0` records their motivic classes.  A realization `\bullet` gives
motivic, Hodge, cohomological, Euler, or numerical invariants.  The
support functor extracts the active classes:

```tex
\Gamma^{BPS,\bullet}_{\sigma,S,o}
 =
\{\gamma\in\Gamma^{ss}_{\sigma,S}:
  \Omega^\bullet_{\sigma,o}(\gamma)\ne 0\}.
```

The completion monoid is generated by this support.  A6 and A7 preserve
the product, and A8 preserves the wall product.  Hence the displayed
object is exactly the decategorified shadow.

Status: proved here from A6--A8.  The master synthesis fixes the same
decategorification structure at lines 951--977.

### Theorem 4.4: Toric Terminal Degeneration

For a quiver with potential `(Q,W)` in a standard toric CY3 chamber,
with standard critical CoHA orientation,

```tex
P^{BPS,motloc}_{\sigma,S,o,T_{\mathrm{eq}}}(Q,W)
```

exists and decategorifies to the toric effective positive geometry:

```tex
\Gamma^{ss}_{\sigma,S}=\mathbb Z_{\ge 0}^{Q_0},
```

```tex
\mathcal M^A_\sigma(d)
 =
[\operatorname{Crit}(\operatorname{Tr}W_d)/G_d],
```

```tex
\mathcal H^{mot}_{\sigma,S,o,T_{\mathrm{eq}}}
 =
CoHA^{mot}_{crit}(Q,W).
```

Proof.  The representation stack is smooth before imposing the trace
potential.  The trace potential gives global critical charts.  The
standard CoHA orientation supplies A1.  Vanishing cycles supply A2.
Short exact sequences of representations give A3, flag varieties give
A4, HN filtrations in the chosen chamber give A5, and the usual
motivic integration map gives A6.  Decategorification is Theorem 4.3.

Status: theorem-grade on quiver critical charts; this is the local
theorem recorded in the master synthesis at lines 857--895.

### Theorem 4.5: Functoriality for Admissible Morphisms

Let

```tex
F:
(X,\sigma,S,o,T_{\mathrm{eq}})
\longrightarrow
(X',\sigma',S',o',T'_{\mathrm{eq}})
```

be an admissible BPS morphism: an exact CY functor or correspondence
whose induced map on charges preserves the Euler form, sends active
sectors into active sectors, is compatible with support forms, carries
orientation data to orientation data, and makes the Hall extension
correspondences Cartesian after the chosen variance.

Then `F` induces a morphism of localized positive geometries

```tex
P^{BPS,motloc}_{\sigma,S,o,T_{\mathrm{eq}}}(X)
\longrightarrow
P^{BPS,motloc}_{\sigma',S',o',T'_{\mathrm{eq}}}(X')
```

and a commutative decategorification square

```tex
P^{BPS,motloc}(X)  ->  P^{BPS,motloc}(X')
       | Dec                  | Dec
       v                      v
P^{BPS,\bullet}(X) ->  P^{BPS,\bullet}(X').
```

Proof.  The charge map transports the completed torus.  The
orientation-compatible critical correspondence transports
`\Phi^{vc}`.  Cartesianity of extension correspondences identifies the
pull--push Hall products.  Support compatibility makes the completion
continuous.  A7 gives realization compatibility.  Thus the tuple maps
componentwise and preserves every structure map.

Status: proved here as a functoriality theorem for the strengthened
class of admissible morphisms.  The strength is in the hypotheses:
arbitrary exact functors are not admitted until they preserve the Hall,
orientation, support, and realization structures.

### Theorem 4.6: Igusa Boundary Constraint

For the `K3 x E` automorphic boundary, any realization of
`P^{BPS,motloc}` through `AutBorch` must recover:

```tex
\phi_{0,1}=(1/2)Z_{K3},\qquad
\operatorname{Borch}(\phi_{0,1})=\Delta_5,
```

```tex
\operatorname{wt}(\Delta_5)=f(0,0)/2=5,
```

```tex
\operatorname{den}(\mathfrak g_{\Delta_5})
 =
64^{-1}\Delta_5(2Z),
```

```tex
\epsilon_o|_{W^{(2)}(\Lambda^{2,1}_{II})}
 =
\nu_{\Delta_5},
\qquad
\nu_{\Delta_5}(s_{\delta_i})=-1,
```

and

```tex
Z^X_{\square}=C_{\square}\Delta_5^{-2}.
```

Proof.  The Igusa manuscript fixes the one-particle seed
`Z_{K3}=2\phi_{0,1}` and the determinant
`\mathcal D_X=\Delta_5`.  The Vol III stratification records the
Borcherds weight formula
`\operatorname{wt}(\Delta_5)=c_{\phi_{0,1}}(0,0)/2=5`.  The same local
surface records the denominator identity
`64^{-1}\Delta_5(2Z)` and the reflection sign discipline.  Therefore
any automorphic boundary functor compatible with A9 must have these
values.  A boundary failing any displayed identity is not a realization
of this positive geometry.

Status: theorem-grade as a boundary constraint, anchored at
`/Users/raeez/igusa-cusp-form/proj.tex:68`,
`/Users/raeez/igusa-cusp-form/proj.tex:431`,
`chapters/examples/cy_d_kappa_stratification.tex:2253`,
`chapters/examples/cy_d_kappa_stratification.tex:2553`, and
`chapters/examples/cy_d_kappa_stratification.tex:2670`.

## 5. Local-to-Global Descent

The local-to-global theorem has three levels.

### 5.1 Critical Descent

If the derived moduli stack has an oriented critical atlas satisfying
A1, then the local vanishing-cycle motives glue to
`\Phi^{vc}_{\mathcal A,o}`.

Proof obligation.  Verify the d-critical transition functions,
orientation square roots, and triple-overlap cocycle.  For quiver
critical charts this is global and theorem-grade.  For compact non-toric
CY3 categories, this is the orientation oracle.

### 5.2 Hall Descent

If the extension correspondences are compatible with the critical atlas
and Thom--Sebastiani maps, then the local Hall products glue to
`\mu^{mot}_{Hall}`.

Proof obligation.  Check that extension stacks preserve the chosen
critical charts, the coefficient systems, properness/constructibility
needed for pull--push, and flag-stack associativity.

### 5.3 Sector Descent

If HN filtrations exist in the strict sector and the support property
gives finite truncations, then sector gluing is completed tensor
product.  This is Theorem 4.2.

Proof obligation.  For compact CY3 categories, construct Bridgeland
stability conditions, prove the support property, and prove HN
boundedness in every strict sector used.

## 6. Decategorification and the Positive Combinatorial System

The positive combinatorial system is the image of the motivic object:

```tex
P^{BPS,motloc}
\xrightarrow{Int^{mot}}
\widehat{\mathbb T}^{mot}
\xrightarrow{K_0,Real}
\widehat{\mathbb T}^{\bullet}
\xrightarrow{support}
P^{BPS,\bullet}.
```

Its three supports are distinct:

```tex
\Gamma^{ss}_{\sigma,S}
 =
\{\gamma: Z_\sigma(\gamma)\in S,\
          \mathcal M_\sigma(\gamma)\ne\varnothing,\
          Q(\gamma)\ge 0\},
```

```tex
\Gamma^{BPS,\bullet}_{\sigma,S,o}
 =
\{\gamma\in\Gamma^{ss}_{\sigma,S}:
  \Omega^\bullet_{\sigma,o}(\gamma)\ne 0\},
```

```tex
\Gamma^+_{\sigma,S,o}
 =
\mathbb N\langle\Gamma^{BPS,\bullet}_{\sigma,S,o}\rangle.
```

The first is geometric, the second is motivic/cohomological, the third
is topological.  Collapsing them is the first false move in the subject.

The toric case is the terminal collapse:

```tex
\Gamma^{ss}_{\sigma,S}
=
\Gamma^+_{\sigma,S,o}
=
\mathbb Z_{\ge 0}^{Q_0}.
```

The `K3 x E` case is the automorphic boundary:

```tex
\Gamma_{\mathrm{eff}}
 =
\{m>0,n\ge 0,l\in\mathbb Z\}
\cup
\{m=0,n>0,l\in\mathbb Z\}
\cup
\{m=n=0,l<0\}.
```

This boundary is chamber-theoretic, not toric.

## 7. Placement of the Ten Obligations

1. Compact CY3 construction.

```tex
Theorem target:
Bridgeland stability + support + oriented critical atlas
+ HN completion + motivic realization
=> P^{BPS,motloc}_{\sigma,S,o,T_{\mathrm{eq}}}(X).
```

The target is stronger than a numerical invariant: it constructs the
localized motivic Hall cosheaf.

2. Orientation oracle.

```tex
critical atlas -> H^2(-,\mathbb Z/2) obstruction -> square root -> epsilon_o.
```

The target is stronger than choosing signs after integration: it
constructs signs before Hall multiplication.

3. Sector descent.

Theorem 4.2 gives the axiomatic result.  The geometric target is to
prove A5 in compact CY3 chambers.

4. Realization compatibility.

A7 is the required theorem shape.  The proof target is preservation of
Hall product, orientation signs, Tate twists, completions, and wall
transport for each realization functor.

5. hCS-to-Hall comparison.

The strengthened target is an oriented comparison map

```tex
\Theta^{or}_{hCS\to Hall}:
Obs^q_{hCS}(-,\mathfrak g)
\longrightarrow
CoHA^{or}_{crit}(-)
```

compatible with factorization, compact supports, Thom--Sebastiani,
orientation transport, and HN completion.  Naming the map is not a
construction.

6. `K3 x E` Hall--Borcherds bridge.

The target is not an equality of characters alone.  It is a Hall
positive half whose automorphic boundary has root multiplicities

```tex
\operatorname{smult}(\alpha(n,l,m))=f(nm,l).
```

7. Automorphic boundary functor.

A9 is the theorem shape:

```tex
AutBorch:
K_0(BPS^{mot,prim})\to M_*(G,\nu).
```

The first value is forced:

```tex
AutBorch(\phi_{0,1})=\Delta_5.
```

8. Drinfeld double theorem.

The strengthened target is

```tex
D(\mathcal H^{mot,+})
```

only after Cartan data, negative half, coproduct, topological
bialgebra, continuous pairing, radical quotient, and completion are
constructed.  This matches the Vol III restriction that `G(X)` is
constructed only on loci with positive half, pairing, and specialization
data.

9. Theta enhancement.

The theta basis is an enhancement

```tex
P^{BPS,motloc,+\vartheta}
 =
(P^{BPS,motloc},\Theta^{BPS})
```

only after broken lines, GMN transport, cluster charts, or
Hall-factorization theta functions are constructed.  It is not part of
the base object.

10. Compute layer.

The computable object is the compatible finite truncation

```tex
P^{BPS,motloc}_{\le N,\le R}.
```

The required tests are:

```tex
orientation cocycle = 0,
Hall associativity on flags,
sector descent for ordered covers,
KS loop holonomy = 1 modulo (N,R),
toric collapse to Z_{\ge 0}^{Q_0},
conifold quantum pentagon,
Igusa normalizations D_5, \mathcal D_X, den(\mathfrak g_{\Delta_5}).
```

## 8. Failure Modes Healed into Stronger Statements

Failure mode 1.  A positive geometry is a fan.

Healed statement.  A fan is the terminal toric decategorification of a
sector-completed oriented motivic Hall cosheaf.

Failure mode 2.  Effective support and BPS completion are the same.

Healed statement.  The construction has three supports:
`\Gamma^{ss}`, `\Gamma^{BPS,\bullet}`, and `\Gamma^+`, in that order.

Failure mode 3.  The classical dilogarithm is the wall-crossing object.

Healed statement.  The motivic quantum torus and quantum dilogarithm are
primary; the classical dilogarithm is the Euler-specialized shadow.

Failure mode 4.  PBW produces the quantum group.

Healed statement.  PBW describes the positive half.  The double requires
Cartan, negative half, coproduct, topological pairing, radical quotient,
and completion.

Failure mode 5.  `CoHA(C^3)` is `W_{1+infty}`.

Healed statement.  `CoHA(C^3)=Y^+(\widehat{\mathfrak{gl}}_1)`; the full
vertex-algebraic object appears only after the double/center passage.

Failure mode 6.  The `K3 x E` boundary is toric.

Healed statement.  `K3 x E` supplies a Lorentzian automorphic boundary
with chamber `\Gamma_{\mathrm{eff}}`, determinant `\Delta_5`,
denominator `64^{-1}\Delta_5(2Z)`, sign character `\nu_{\Delta_5}`,
and scalar square `C_{\square}\Delta_5^{-2}`.

Failure mode 7.  Orientation is cosmetic.

Healed statement.  Orientation is part of the object; it produces
`\epsilon_o`, controls motivic torus signs, and maps to
`\nu_{\Delta_5}` at the automorphic boundary.

Failure mode 8.  Compact CY3 existence follows from writing the tuple.

Healed statement.  The compact CY3 theorem requires the full input
package: Bridgeland stability, support, oriented critical atlas, HN
completion, motivic target, and realization compatibility.

Failure mode 9.  hCS and Hall are identical by physical intuition.

Healed statement.  They are related by the theorem target
`\Theta^{or}_{hCS\to Hall}`, which must preserve factorization,
vanishing cycles, orientation, and completion.

Failure mode 10.  The Igusa square root is the full index.

Healed statement.  `\Delta_5` is the chiral determinant; the scalar full
index is governed by `\Delta_5^2`.  The positive half precedes the
double.

## 9. Status Ledger

Proved here.

```tex
A0--A9 => P^{BPS,motloc} is defined.
Sector descent follows from HN factorization and 2-Segal Hall geometry.
Dec(P^{BPS,motloc})=P^{BPS,\bullet}.
Admissible morphisms induce functorial maps of P^{BPS,motloc}.
```

Proved on local quiver-critical charts.

```tex
P^{BPS,motloc}(Q,W) exists.
Dec(P^{BPS,motloc}(Q,W)) is the toric effective positive geometry.
CoHA(C^3)=Y^+(\widehat{\mathfrak{gl}}_1).
Conifold wall crossing satisfies the quantum pentagon.
```

Theorem-grade Igusa boundary constraints.

```tex
\operatorname{Borch}(\phi_{0,1})=\Delta_5.
\operatorname{wt}(\Delta_5)=f(0,0)/2=5.
D_5=64^{-1}\Delta_5.
\operatorname{den}(\mathfrak g_{\Delta_5})=D_5(2Z).
\nu_{\Delta_5}(s_{\delta_i})=-1.
Z^X_{\square}=C_{\square}\Delta_5^{-2}
  in the stated scalar-square scope.
```

Theorem targets with exact proof obligations.

```tex
Compact CY3 P^{BPS,motloc}:
  build stability, support, orientation, HN completion, motivic target.

\Theta^{or}_{hCS\to Hall}:
  build oriented factorization-to-Hall comparison.

Hall--BKM bridge for K3 x E:
  lift character identities to Hall positive half and double data.

AutBorch:
  construct the boundary functor from primitive BPS motives.

Drinfeld double:
  construct Cartan, negative half, coproduct, pairing, radical quotient.

Theta enhancement:
  construct theta functions from broken-line, GMN, cluster, or Hall data.

Compute truncations:
  implement P^{BPS,motloc}_{\le N,\le R} and verify the seven tests.
```

## 10. Foundational Conclusion

The foundational object is the following theorem target.

```tex
\boxed{
P^{BPS,motloc}_{\sigma,S,o,T_{\mathrm{eq}}}(X)
 =
\text{sector-completed oriented motivic Hall cosheaf on }
\mathcal M_C^{(-1)}
}
```

Its toric degeneration is a quiver critical CoHA over a rational
polyhedral monoid.  Its compact CY3 construction is the theorem obtained
by building the full input package.  Its decategorification is the
chambered BPS positive combinatorial system.  Its double, theta basis,
hCS comparison, and automorphic boundary are enhancements, each with its
own proof obligations.  Its first non-toric automorphic boundary is
`K3 x E`, where the determinant is `\Delta_5`, the denominator is
`64^{-1}\Delta_5(2Z)`, and the scalar square is governed by
`\Delta_5^2`.

The positive geometry is therefore not a replacement for motivic or
homotopical algebraic geometry.  It is their chambered BPS realization.
