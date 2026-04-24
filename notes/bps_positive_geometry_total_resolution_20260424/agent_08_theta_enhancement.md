# Obligation 9. Theta Enhancement of Chambered BPS Positive Geometry

Date: 2026-04-24.

Owned file:
`notes/bps_positive_geometry_total_resolution_20260424/agent_08_theta_enhancement.md`.

Task: construct the theta-enhancement layer.  The base object remains
the oriented sector-completed motivic Hall cosheaf

```tex
P^{BPS,motloc}_{\sigma,S,o,T_{\rm eq}}(X).
```

Theta functions are not part of this base object.  They are additional
framed, broken-line, spectral-network, cluster, or Hall-factorization
sections of its integrated quantum-torus local system.  This separation
is structural: a positive geometry may exist before a theta basis exists,
but whenever one of the exact packages below is supplied the enhancement
is constructed by theorem, not by analogy.

## Resolution

The strengthened theta object is

```tex
P^{BPS,motloc,+\vartheta}_{\sigma,S,o,T_{\rm eq},\mathfrak T}(X)
 =
\bigl(
P^{BPS,motloc}_{\sigma,S,o,T_{\rm eq}}(X),
\mathfrak T,
\Theta^{BPS,mot}_{\sigma,S,o,T_{\rm eq},\mathfrak T},
\mathsf{Loc}_\vartheta,
\mathsf{Mult}_\vartheta,
\mathsf{Ob}_\vartheta
\bigr).
```

Here `\mathfrak T` is one of four theta packages:

```tex
\mathfrak T \in
\{
 \mathfrak T_{\rm bl},
 \mathfrak T_{\rm GHKK},
 \mathfrak T_{\rm GMN},
 \mathfrak T_{\rm Hall}
\}.
```

The output is a compatible inverse system of finite-truncation theta
sets

```tex
\Theta^{BPS,mot}_{\lambda,b}
 =
\{\vartheta^{\lambda,b}_p:
  p\in P_\lambda^{\vartheta}\}
\subset
\widehat{\mathbb T}^{mot}_{\Gamma,S,o}/F^{>\lambda},
```

indexed by a charge truncation `\lambda=(N,R)` and a basepoint `b` in
the complement of the active walls.  Passing to the inverse limit gives

```tex
\vartheta^b_p
 =
\lim_{\lambda}\vartheta^{\lambda,b}_{p,\lambda}
\in
\widehat{\mathbb T}^{mot}_{\Gamma,S,o}.
```

The theorem targets below are monotone strengthenings of the informal
phrase "general compact-CY3 theta basis": each one gives exact
sufficient hypotheses, a construction, an obstruction complex, and a
localization rule over the motivic Hall cosheaf.

## Source Anchors

Local anchors:

```text
notes/bps_positive_geometry_total_resolution_20260424/integration_spine.md:137
notes/bps_positive_geometry_total_resolution_20260424/agent_00_foundational_axioms.md:874
notes/bps_positive_geometry_total_resolution_20260424/agent_01_compact_cy3_construction.md:716
notes/bps_positive_geometry_total_resolution_20260424/agent_03_sector_descent_hn_cosheaf.md:1
notes/bps_positive_geometry_total_resolution_20260424/agent_04_realization_compatibility.md:1
notes/bps_positive_geometry_total_resolution_20260424/agent_05_hcs_hall_dwr_ran.md:1
notes/master_synthesis_chambered_bps_positive_geometry_20260424.md:712
```

External theorem anchors:

```text
Kontsevich--Soibelman, Stability structures, motivic Donaldson-Thomas
invariants and cluster transformations, arXiv:0811.2435.

Bridgeland, Scattering diagrams, Hall algebras and stability
conditions, arXiv:1603.00416.

Gross--Hacking--Keel--Kontsevich, Canonical bases for cluster
algebras, arXiv:1411.1394; JAMS 31 (2018).

Gaiotto--Moore--Neitzke, Spectral networks, arXiv:1204.4824.

Gaiotto--Moore--Neitzke, Wall-crossing, Hitchin systems, and the WKB
approximation, arXiv:0907.3987.
```

Only the first three are imported as theorem technology.  The GMN lane
is imported as an exact spectral-network axiom package: when a
non-class-S geometry supplies the same detour, abelianization, and
wall-crossing identities, the theta construction below is theorem-grade
for that geometry.

## 1. Base Object and Enhancement Object

The base object is

```tex
P^{BPS,motloc}_{\sigma,S,o,T_{\rm eq}}(X)
 =
(StabSite(C),
 Sect_\sigma(C),
 \mathcal M_C^{(-1)-symp},
 \mathcal A^{or}_{crit},
 \Phi^{vc}_{\mathcal A,o},
 \widehat{\mathcal H}^{mot}_{\sigma,S,o,T_{\rm eq}},
 \mu^{mot}_{Hall},
 Fil^{HN}_{\sigma,S},
 \widehat{\mathbb T}^{mot}_{\Gamma,S,o},
 Int^{mot},
 Real,
 Dec).
```

It contains no theta basis.  A theta basis requires one more datum:
framed asymptotic conditions.  These conditions are not determined by
the unframed Hall cosheaf alone.  They may come from:

```tex
broken-line asymptotic monomials,
GHKK cluster seed tori,
GMN line defects and detour rules,
Hall-factorization framed modules.
```

Thus the enhancement functor is partially defined:

```tex
\mathsf{ThetaEnh}_{\mathfrak T}:
P^{BPS,motloc}_{\sigma,S,o,T_{\rm eq}}(X)
\dashrightarrow
P^{BPS,motloc,+\vartheta}_{\sigma,S,o,T_{\rm eq},\mathfrak T}(X).
```

It becomes an honest functor on the subcategory of base objects equipped
with the chosen package `\mathfrak T`.  The theorem targets below give
four disjoint sufficient domains for this functor.

## 2. Finite Truncations

Let

```tex
\lambda=(N,R)
```

be a height and central-charge truncation.  The finite charge set is

```tex
\Gamma_{S,\lambda}
 =
\{
\gamma\in\Gamma^+_{\sigma,S,o}:
h(\gamma)\le N,\ |Z_\sigma(\gamma)|\le R,\ Q(\gamma)\ge 0
\}.
```

The finite Hall object is

```tex
\widehat{\mathcal H}^{mot}_{S,\lambda}
 =
\widehat{\mathcal H}^{mot}_{\sigma,S,o,T_{\rm eq}}
/F^{>\lambda},
```

and the finite quantum torus is

```tex
\widehat{\mathbb T}^{mot}_{S,\lambda}
 =
\widehat{\mathbb T}^{mot}_{\Gamma,S,o}/F^{>\lambda}.
```

Every theta construction below is first defined in
`\widehat{\mathbb T}^{mot}_{S,\lambda}` and is required to satisfy

```tex
\pi_{\lambda'\lambda}(\vartheta^{\lambda',b}_p)
 =
\vartheta^{\lambda,b}_p
\qquad
(\lambda'\ge \lambda).
```

The inverse limit is the completed theta enhancement.  This rule is the
localization principle: theta functions live over the same finite
motivic Hall truncations as the base positive geometry.

## 3. The Hall Scattering Diagram Attached to the Base Object

For a finite truncation, define the pronilpotent Lie algebra

```tex
\mathfrak g_{S,\lambda}^{Hall}
 =
\bigoplus_{\gamma\in\Gamma_{S,\lambda}\setminus\{0\}}
\widehat{\mathcal H}^{mot}_{\gamma}
```

with bracket the Hall commutator after orientation, Thom--Sebastiani,
and Tate normalization:

```tex
[a,b]_{Hall}=a*b-(-1)^{|a||b|}b*a.
```

Integration gives the motivic tropical Lie algebra

```tex
Int^{mot}_\lambda:
\mathfrak g^{Hall}_{S,\lambda}
\longrightarrow
\mathfrak g^{mot}_{\Gamma,S,\lambda}
\subset
\widehat{\mathbb T}^{mot}_{S,\lambda}.
```

A wall is a pair

```tex
(\gamma^\perp,\Phi_\gamma)
```

where `\gamma^\perp` is the real codimension-one locus on which the
phase of `\gamma` is aligned with the chosen test direction, and

```tex
\Phi_\gamma
 =
\exp\left(
\sum_{k\ge 1}
\frac{\Omega^{mot}(k\gamma)}
     {k(\mathbb L^{k/2}-\mathbb L^{-k/2})}
x_{k\gamma}
\right)
```

is the motivic quantum-dilogarithm wall factor in the finite quotient.
The denominator is interpreted in the chosen motivic coefficient ring;
in the Euler specialization it becomes the classical KS factor after
the standard limiting procedure.

The finite Hall scattering diagram is

```tex
\mathfrak D^{Hall}_{S,\lambda}
 =
\{(\gamma^\perp,\Phi_\gamma):
\gamma\in\Gamma_{S,\lambda}^{BPS}\}.
```

Its consistency is not an assumption external to the base object.  It is
the finite-truncation form of HN uniqueness, Hall associativity, and
sector descent:

```tex
PathProd_{\mathfrak D^{Hall}_{S,\lambda}}(\ell)=1
```

for every contractible loop `\ell` avoiding joints.  This is the common
input for broken-line, GHKK, and Hall-factorization theta functions.

## 4. The Broken-Line Theta Theorem

### Package `\mathfrak T_{\rm bl}`

The broken-line package consists of:

```tex
\mathfrak T_{\rm bl}
 =
(B_\mathbb Z,
 \iota:\Gamma^+_{\sigma,S,o}\hookrightarrow B_\mathbb Z,
 \Sigma^{sc},
 \mathfrak D^{Hall}_{S,\lambda},
 \mathsf{Asymp},
 \mathsf{Bend}).
```

Here `B_\mathbb Z` is an integral affine lattice containing the active
charges; `\Sigma^{sc}` is a strictly convex support cone containing
`\iota(\Gamma^+_{\sigma,S,o})`; `\mathsf{Asymp}` assigns to every
`p\in B_\mathbb Z` an initial monomial `z^p`; and `\mathsf{Bend}` is
the rule that a crossing of a wall with factor `\Phi_\gamma` changes a
monomial by multiplying by the corresponding term of `\Phi_\gamma`.

The package is beyond toric because `B_\mathbb Z` is not required to be
the lattice of a fan, and `\mathfrak D^{Hall}` is produced by the
motivic Hall cosheaf, not by toric boundary divisors.

### Theorem Target A: Broken-Line Theta Basis

Assume:

1. finite local scattering: for every `\lambda`, the support of
   `\mathfrak D^{Hall}_{S,\lambda}` is locally finite in the complement
   of joints;
2. consistency: all finite path-ordered products around contractible
   loops are identity;
3. strict convexity: every bend increases the height filtration;
4. finite bending: for fixed `p`, basepoint `b`, and `\lambda`, only
   finitely many broken lines of total charge in `\Gamma_{S,\lambda}`
   reach `b`;
5. orientation compatibility: the bending coefficients use the same
   `\epsilon_o` and half-Tate normalization as
   `\widehat{\mathbb T}^{mot}_{S,\lambda}`;
6. triangular asymptotics: each theta function has leading term `z^p`
   with coefficient `1`, and all other terms have strictly larger
   height with respect to the scattering order.

Then for every finite truncation and basepoint `b` outside the walls,

```tex
\vartheta^{\lambda,b}_p
 =
\sum_{\beta\in BL_\lambda(p,b)}
{\rm Mono}(\beta)
\in
\widehat{\mathbb T}^{mot}_{S,\lambda}
```

is well-defined and independent of deformation of `b` inside a chamber.
The set

```tex
\Theta^{bl}_{\lambda,b}
 =
\{\vartheta^{\lambda,b}_p:p\in P^\vartheta_\lambda\}
```

is a topological basis of the theta algebra

```tex
\mathcal A^{bl}_{S,\lambda}
 =
\overline{\mathrm{span}}_{R_{mot}}\Theta^{bl}_{\lambda,b}
\subset
\widehat{\mathbb T}^{mot}_{S,\lambda}
```

whenever `P^\vartheta_\lambda` is saturated under addition of charges
appearing in broken-line multiplication.  Multiplication has positive
motivic structure constants

```tex
\vartheta^{\lambda,b}_{p_1}
\vartheta^{\lambda,b}_{p_2}
 =
\sum_{p_3}
c^{p_3}_{p_1,p_2}(\lambda,b)
\vartheta^{\lambda,b}_{p_3},
```

where `c^{p_3}_{p_1,p_2}` is the motivic count of pairs of broken lines
with outgoing total exponent `p_3`, including the orientation sign and
Tate factor inherited from `P^{BPS,motloc}`.

### Proof Spine

In a finite truncation, nilpotence of the height filtration makes all
wall factors finite.  Local finiteness gives a finite set of bends
intersecting a compact path.  Consistency identifies broken-line sums
at two basepoints by path-ordered transport.  Strict convexity prevents
infinite descending chains.  Triangularity gives linear independence
and spanning in the completed algebra by induction on height.
Multiplication is computed by multiplying the two broken-line sums and
re-expanding the result by the same triangular induction.

### Obstruction

The obstruction complex is

```tex
\mathsf{Ob}_{bl}
 =
(
o_{locfin},
o_{joint},
o_{height},
o_{orient},
o_{tri}
).
```

Here `o_{locfin}` is wall accumulation in finite truncation; `o_{joint}`
is nontrivial path-ordered product around a joint; `o_{height}` is a
bend that does not raise filtration; `o_{orient}` is mismatch with
`\epsilon_o`; and `o_{tri}` is failure of unit-leading triangularity.
The strengthened theorem does not collapse when an obstruction is
nonzero: the output is the largest strict subcone and truncation on
which all five obstructions vanish, together with the obstruction class
on the complement.

## 5. The Cluster/GHKK Theta Theorem

### Package `\mathfrak T_{\rm GHKK}`

The cluster package consists of:

```tex
\mathfrak T_{\rm GHKK}
 =
(\mathcal X^{cl},
 \mathcal A^{cl},
 {\rm Seed},
 \mathfrak D^{cl},
 \Psi_{\rm Hall-cl},
 EGM,
 \mathsf{can}).
```

Here `(\mathcal A^{cl},\mathcal X^{cl})` is a cluster pair over a
finite sector of the BPS charge lattice; `{\rm Seed}` is a mutation
class of seed tori; `\mathfrak D^{cl}` is the GHKK cluster scattering
diagram; `\Psi_{\rm Hall-cl}` is an isomorphism between the integrated
Hall scattering diagram and `\mathfrak D^{cl}` after the chosen seed
identification; `EGM` is the enough-global-monomials condition or any
stronger hypothesis ensuring the GHKK theta algebra agrees with the
regular function algebra under consideration; and `\mathsf{can}` is the
canonical GHKK broken-line construction.

The package is beyond toric because a cluster atlas may exist on a
non-toric open locus of a compact or local CY3 chamber; the fan is
replaced by seed mutation and Hall scattering.

### Theorem Target B: Cluster Theta Transfer from Hall Scattering

Assume:

1. there is a cluster atlas on the theta locus of the BPS chamber, with
   unfrozen charge lattice identified with a primitive sublattice of
   `\Gamma`;
2. the Hall scattering diagram and the GHKK cluster scattering diagram
   are equivalent under `\Psi_{\rm Hall-cl}` in every finite truncation;
3. the orientation quadratic refinement becomes the cluster skew form
   sign after the half-Tate calibration cochain;
4. the cluster algebra satisfies `EGM` or a stronger theta-basis
   existence condition;
5. the upper cluster algebra, regular-function algebra, or selected
   partial compactification ring is the algebra to be enhanced;
6. the finite truncation transition maps commute with mutation and with
   the Hall-to-cluster identification.

Then the GHKK theta functions

```tex
\vartheta^{GHKK}_{q,\lambda}
```

pull back to Hall theta functions

```tex
\vartheta^{Hall-cl}_{q,\lambda}
 =
\Psi_{\rm Hall-cl}^{-1}(\vartheta^{GHKK}_{q,\lambda})
\in
\widehat{\mathbb T}^{mot}_{S,\lambda}.
```

They form a canonical positive basis of the Hall-cluster theta algebra

```tex
\mathcal A^{Hall-cl}_{S,\lambda}
\subset
\widehat{\mathbb T}^{mot}_{S,\lambda},
```

with multiplication constants equal to GHKK broken-line counts transported
through the motivic Hall integration map.  The inverse limit over
`\lambda` gives

```tex
\Theta^{GHKK}_{S,b}
\subset
\widehat{\mathbb T}^{mot}_{\Gamma,S,o}.
```

### Proof Spine

GHKK gives theta functions from the cluster scattering diagram under
the stated basis hypotheses.  The isomorphism `\Psi_{\rm Hall-cl}`
identifies walls, wall functions, exponents, skew forms, and broken-line
bending rules.  Therefore every GHKK broken line is the image of a Hall
broken line and every Hall broken line in the cluster sublattice is the
preimage of a GHKK broken line.  Structure constants agree because both
are computed by the same broken-line pairs.  Completion compatibility
passes the statement to the inverse limit.

### Obstruction

The obstruction complex is

```tex
\mathsf{Ob}_{GHKK}
 =
(
o_{atlas},
o_{scatter},
o_{EGM},
o_{upper},
o_{orient},
o_{mut}
).
```

The terms mean: no cluster atlas; Hall scattering not equivalent to
cluster scattering; failure of the chosen GHKK basis hypothesis; mismatch
between upper and regular function algebras; orientation sign not
absorbed by the cluster skew form; mutation incompatible with truncation.
The strengthened output is the maximal cluster sublattice and partial
compactification on which these obstructions vanish.

## 6. The GMN/Spectral-Network Theta Theorem

### Package `\mathfrak T_{\rm GMN}`

The spectral-network package abstracts the GMN mechanism away from
class-S without weakening it.  It consists of:

```tex
\mathfrak T_{\rm GMN}
 =
(\pi:\Sigma\to C_{aux},
 \lambda_{SW},
 \Gamma_{rel},
 \mathcal W_\zeta,
 \mathsf{Ab},
 \mathsf{Detour},
 \mathsf{Line},
 \mathsf{Halo},
 \Psi_{\rm GMN-Hall}).
```

The data are:

1. a branched spectral cover `\pi:\Sigma\to C_{aux}` equipped with a
   differential `\lambda_{SW}` whose periods give the central charge;
2. a relative charge lattice `\Gamma_{rel}` identified with the active
   Hall charge lattice after quotienting null cycles;
3. a family of spectral networks `\mathcal W_\zeta`;
4. an abelianization functor `\mathsf{Ab}` from flat nonabelian data on
   `C_{aux}` to twisted abelian local systems on `\Sigma`;
5. detour rules `\mathsf{Detour}` producing finite sums indexed by
   soliton paths in every truncation;
6. framed line defects `\mathsf{Line}_p`;
7. halo gluing rules matching 2d-4d wall crossing;
8. an identification `\Psi_{\rm GMN-Hall}` between spectral-network
   wall crossing and the motivic Hall KS wall factors after realization
   or at motivic level when soliton categories are motivic.

No Hitchin or class-S origin is assumed.  A class-S theory is a source
of this package; it is not the definition.  Any compact CY3 chamber that
supplies the eight pieces above belongs to the theorem domain.

### Theorem Target C: Spectral-Network Framed Theta Functions

Assume:

1. periods of `\lambda_{SW}` reproduce the Hall central charge on the
   active sector;
2. for every `\lambda`, the spectral network has finitely many detours
   contributing to each charge in `\Gamma_{S,\lambda}`;
3. detour composition satisfies the 2d-4d wall-crossing identity;
4. halo gluing is identified by `\Psi_{\rm GMN-Hall}` with conjugation
   by motivic Hall quantum dilogarithms;
5. framed line defects `\mathsf{Line}_p` are enough and triangular:
   each has a unique core charge `p` with coefficient `1`, and all halo
   corrections have larger height;
6. the orientation sign and spin refinement in the spectral network
   equal the Hall orientation cocycle `\epsilon_o`;
7. abelianization is compatible with sector restriction and finite
   truncation.

Then the framed generating function of a line defect

```tex
F^{\lambda,\zeta}_p
 =
\sum_{\gamma\in\Gamma_{S,\lambda}}
\underline{\Omega}^{mot}_{p,\zeta}(\gamma)x_{p+\gamma}
```

is a theta function

```tex
\vartheta^{GMN,\lambda,\zeta}_p
 =
F^{\lambda,\zeta}_p
\in
\widehat{\mathbb T}^{mot}_{S,\lambda}.
```

The collection

```tex
\Theta^{GMN}_{\lambda,\zeta}
 =
\{\vartheta^{GMN,\lambda,\zeta}_p\}
```

is flat under variation of `\zeta` away from active walls, and across an
active wall it transforms by the same KS automorphism as the Hall
scattering diagram:

```tex
\vartheta^{GMN,\lambda,\zeta_+}_p
 =
{\rm Ad}_{\Phi_\gamma}
\bigl(\vartheta^{GMN,\lambda,\zeta_-}_p\bigr).
```

If the framed line defects are saturated under OPE, then
`\Theta^{GMN}_{\lambda,\zeta}` is a basis of the framed theta algebra,
and multiplication is the OPE of framed line defects transported through
`\Psi_{\rm GMN-Hall}`.

### Proof Spine

The detour rule writes each framed line defect as a finite sum in the
abelian torus at truncation `\lambda`.  2d-4d wall crossing identifies
the jump of detour sums with halo conjugation.  The Hall comparison
identifies halo conjugation with the KS automorphism of
`\mathfrak D^{Hall}`.  Triangularity gives independence and spanning by
height induction.  OPE compatibility gives multiplication.  Completion
follows from the truncation transition maps.

### Obstruction

The obstruction complex is

```tex
\mathsf{Ob}_{GMN}
 =
(
o_{cover},
o_{period},
o_{detour},
o_{2d4d},
o_{halo},
o_{framed},
o_{spin},
o_{abel}
).
```

These record failure of a spectral cover, period mismatch, infinite
detour sums in finite truncation, broken 2d-4d wall crossing, halo/Hall
mismatch, insufficient line defects, spin/orientation mismatch, and
failure of abelianization descent.  The strengthened theorem domain is
the full subcategory where these obstructions vanish.  Outside it the
base positive geometry remains intact; only the GMN theta enhancement
is absent.

## 7. The Hall-Factorization Theta Theorem

### Package `\mathfrak T_{\rm Hall}`

The Hall-factorization package is intrinsic to
`P^{BPS,motloc}` and therefore gives the broadest non-toric target.  It
consists of framed Hall modules

```tex
\mathfrak T_{\rm Hall}
 =
(\mathcal F_p,
 \mathcal M^{fr}_{p,\gamma},
 \Phi^{vc,fr}_{p,\gamma},
 \mu^{fr},
 \mathsf{Core},
 \mathsf{Tri},
 \mathsf{OPE}).
```

Here `\mathcal F_p` is a framing or defect object of core charge `p`;
`\mathcal M^{fr}_{p,\gamma}` is the oriented derived critical moduli
stack of pairs `(E,\eta:\mathcal F_p\to E)` or the dual framed problem,
depending on variance; `\Phi^{vc,fr}_{p,\gamma}` is its oriented
vanishing-cycle coefficient; `\mu^{fr}` is the framed Hall action of
unframed objects; `\mathsf{Core}` extracts the leading core monomial;
`\mathsf{Tri}` is the triangularity order; and `\mathsf{OPE}` is the
factorization product of framed defects.

This package does not require a fan, a cluster atlas, or a spectral
curve.  It is the correct theorem target for compact non-toric CY3
categories once framed defects are constructed.

### Theorem Target D: Intrinsic Hall-Factorization Theta Basis

Assume:

1. for each allowed core `p`, the framed moduli stacks
   `\mathcal M^{fr}_{p,\gamma}` are oriented derived critical stacks
   compatible with the unframed orientation data `o`;
2. the forgetful map
   `\mathcal M^{fr}_{p,\gamma}\to\mathcal M_{\gamma}` is admissible for
   the same Borel-Moore pull-push theory as the Hall product;
3. framed Hall action is associative:

   ```tex
   (m*a)*b=m*(a*b)
   ```

   on the stack of framed two-step flags;
4. framed finite truncations are finite under the same support-property
   bounds as the unframed HN truncations;
5. triangularity holds:

   ```tex
   \vartheta^{Hall,\lambda}_p
    =
   x_p+\sum_{\gamma>0} a^{mot}_{p,\gamma}x_{p+\gamma};
   ```

6. the framed cores `p` form a saturated monoid under the OPE product;
7. the OPE of framed defects is compatible with Hall convolution and
   Thom--Sebastiani orientation transport;
8. the coefficient target satisfies the realization compatibility
   axioms of the realization package.

Define

```tex
\vartheta^{Hall,\lambda}_p
 =
\sum_{\gamma\in\Gamma_{S,\lambda}}
Int^{mot}_{fr}
\left(
R\Gamma^{BM}_{T_{\rm eq}}
(\mathcal M^{fr}_{p,\gamma},
 \Phi^{vc,fr}_{p,\gamma})
\right)
x_{p+\gamma}.
```

Then

```tex
\Theta^{Hall}_{\lambda}
 =
\{\vartheta^{Hall,\lambda}_p\}
```

is a basis of the intrinsic Hall theta algebra

```tex
\mathcal A^{Hall,\vartheta}_{S,\lambda}
 =
\overline{\mathrm{span}}_{R_{mot}}
\Theta^{Hall}_{\lambda}
\subset
\widehat{\mathbb T}^{mot}_{S,\lambda},
```

and multiplication is computed by the framed OPE correspondence:

```tex
\vartheta^{Hall,\lambda}_{p_1}
\vartheta^{Hall,\lambda}_{p_2}
 =
\sum_{p_3}
N^{p_3}_{p_1,p_2}(\lambda)
\vartheta^{Hall,\lambda}_{p_3}.
```

The coefficients `N^{p_3}_{p_1,p_2}(\lambda)` are motivic Borel-Moore
classes of framed pair-of-pants extension stacks, pushed through the
same integration map as the base object.

### Proof Spine

The framed moduli stacks define a right module over the unframed Hall
algebra by pull-push along framed extension correspondences.
Associativity follows from the equality of the two maps from the
framed two-step flag stack.  The theta function is the integrated
framed module character.  Triangularity gives a basis by induction on
height.  OPE compatibility identifies multiplication of theta functions
with the factorization product of framed defects.  Realization
compatibility follows because every map is built from the same
six-functor operations, vanishing cycles, Thom--Sebastiani isomorphisms,
orientation transports, and inverse limits used by
`P^{BPS,motloc}`.

### Obstruction

The obstruction complex is

```tex
\mathsf{Ob}_{Hall}
 =
(
o_{fr},
o_{crit}^{fr},
o_{or}^{fr},
o_{act},
o_{finite}^{fr},
o_{tri}^{fr},
o_{OPE},
o_{real}^{fr}
).
```

These record failure of framings, failure of derived critical framed
charts, failure of orientation transport, non-associative framed Hall
action, failure of finite truncation, non-triangular cores, OPE/Hall
mismatch, and realization incompatibility.  The strong theorem states
that vanishing of this tuple constructs the theta enhancement.

## 8. Localization over the Motivic Hall Cosheaf

Let `S' subset S` be a strict subsector and let `\lambda` be a finite
truncation.  The sector cosheaf gives a restriction/projection map on
finite integrated tori:

```tex
\rho_{S,S'}^\lambda:
\widehat{\mathbb T}^{mot}_{S,\lambda}
\longrightarrow
\widehat{\mathbb T}^{mot}_{S',\lambda}.
```

It is defined by:

1. transporting across inactive internal rays by the identity;
2. transporting across active rays by the finite KS automorphism;
3. projecting away monomials whose charge has no HN support in `S'`;
4. applying the truncation quotient.

A theta package is localized over the Hall cosheaf when

```tex
\rho_{S,S'}^\lambda
(\vartheta^{S,\lambda}_p)
 =
\begin{cases}
\vartheta^{S',\lambda}_{p|_{S'}} & \text{if the core survives in } S',\\
0 & \text{if the core has no sector-supported realization.}
\end{cases}
```

for broken-line, GHKK, GMN, and Hall-factorization constructions.

### Theorem Target E: Theta Localization

Assume one of the four packages `\mathfrak T` satisfies its theorem
hypotheses on `S`, on every strict subsector `S'`, and on every ordered
sector cover

```tex
S=S_1\star\cdots\star S_r.
```

Assume also that its obstruction tuple is natural under sector
restriction.  Then the assignment

```tex
S\longmapsto
\Theta^{BPS,mot}_{S,\lambda,\mathfrak T}
```

is a constructible cosheaf of theta sets over `Sect_\sigma(C)` after
linear extension to theta algebras:

```tex
\mathcal A^\vartheta_{S,\lambda}
 =
\mathcal A^\vartheta_{S_1,\lambda}
\widehat\otimes
\cdots
\widehat\otimes
\mathcal A^\vartheta_{S_r,\lambda}
```

with tensor product ordered by decreasing phase and with multiplication
twisted by the same orientation quantum-torus cocycle as the base Hall
object.  The inverse limit over `\lambda` gives a completed
constructible theta cosheaf

```tex
S\longmapsto
\mathcal A^\vartheta_{S}
\subset
\widehat{\mathbb T}^{mot}_{\Gamma,S,o}.
```

### Proof Spine

All four theta packages define finite sums in the same finite quantum
torus.  Sector descent for `P^{BPS,motloc}` identifies the Hall object
on an ordered sector cover with the completed tensor product of the
sector pieces.  Wall transport is KS conjugation.  Broken-line,
cluster, GMN, and framed-Hall theta functions are all defined by
transport-invariant sums whose jumps are exactly those KS
automorphisms.  Therefore the theta sets glue and restrict along the
same cosheaf maps as the base Hall object.  The finite-truncation
statement passes to the inverse limit by compatibility of transition
maps.

## 9. Comparison Theorem for the Four Theta Packages

When two packages exist on the same sector, the comparison is not a
choice of names.  It is a theorem target with a finite obstruction
class.

### Theorem Target F: Compatibility of Theta Constructions

Let `\mathfrak T_i` and `\mathfrak T_j` be two theta packages among
broken-line, GHKK, GMN, and Hall-factorization.  Suppose there is a
comparison datum

```tex
\Psi_{ij}:
\mathfrak T_i\to\mathfrak T_j
```

that identifies:

```tex
core charges,
wall factors,
orientation signs,
half-Tate normalizations,
finite truncations,
sector restriction maps,
and multiplication correspondences.
```

Then

```tex
\Psi_{ij}
(\vartheta^{\lambda}_{p,\mathfrak T_i})
 =
\vartheta^{\lambda}_{\Psi_{ij}(p),\mathfrak T_j}
```

for every finite truncation.  If the comparison is bijective on core
charges and saturated under multiplication, the two theta algebras are
canonically isomorphic:

```tex
\mathcal A^\vartheta_{S,\lambda,\mathfrak T_i}
\simeq
\mathcal A^\vartheta_{S,\lambda,\mathfrak T_j}.
```

### Proof Spine

The comparison sends each elementary generator of the finite
construction to the corresponding elementary generator: walls to walls,
detours to broken-line bends, cluster mutations to Hall wall crossing,
and framed extension correspondences to OPE pair-of-pants
correspondences.  Since every theta function is a finite sum of such
elementary contributions in truncation `\lambda`, equality follows term
by term.  Multiplication follows from the comparison of pair
correspondences.

### Obstruction

The comparison obstruction is

```tex
\mathsf{Ob}_{ij}
 =
(
o_{core},
o_{wall},
o_{orient},
o_{Tate},
o_{loc},
o_{mult}
).
```

The output is the maximal common subpackage on which
`\mathsf{Ob}_{ij}=0`.  This is stronger than declaring unrelated theta
bases: it produces the exact overlap and the exact obstruction to
identification.

## 10. Toric, Conifold, Cluster, GMN, and Igusa Boundaries

### Toric Terminal Degeneration

For a quiver with potential representing a toric CY3 chamber,

```tex
\Gamma^+=\mathbb Z_{\ge 0}^{Q_0},
\qquad
\widehat{\mathcal H}^{mot}=CoHA(Q,W),
```

and `\mathfrak D^{Hall}` is the usual stability scattering diagram.
If a cluster seed exists, the broken-line and GHKK packages agree with
the standard cluster theta basis.  For `\mathbb C^3`, the positive half
is

```tex
CoHA(\mathbb C^3)=Y^+,
```

not the Drinfeld double and not `\mathcal W_{1+\infty}`.

### Conifold

The conifold is the first nontrivial finite check: the two primitive
charges produce the `A_2` pentagon.  The theorem package predicts that
broken-line, Hall-scattering, and cluster theta functions coincide on
the conifold cluster sector, with multiplication controlled by the same
pentagon identity used in the sector-descent tests.

### Non-Toric Cluster Loci

Whenever a non-toric CY3 chamber admits a cluster atlas whose scattering
diagram is the integrated Hall scattering diagram, the GHKK theorem
constructs theta functions without imposing a toric fan.  The lattice of
theta labels is the tropical cluster lattice identified with a charge
sublattice of `\Gamma`, not a fan lattice.

### Non-Class-S Spectral-Network Loci

Whenever a non-class-S CY3 chamber supplies a spectral cover,
abelianization, detour rules, enough framed line defects, and
Hall-compatible halo wall crossing, the GMN theorem constructs framed
theta functions.  The surface is auxiliary data in `\mathfrak T_{\rm
GMN}`; it is not a replacement for the CY3 category or the motivic Hall
cosheaf.

### Igusa and Automorphic Boundary

At the `K3 x E` automorphic boundary, the Borcherds denominator
`\Delta_5` is not by itself a GHKK theta basis.  It is the automorphic
denominator obtained from the primitive one-particle seed.  It becomes
a theta enhancement only after one constructs a compatible framed Hall
or spectral-network package whose finite theta characters specialize to
the Borcherds product coefficients.  The exact theorem target is:

```tex
\Theta^{Hall}_{K3\times E,\lambda}
\xrightarrow{\ AutBorch\ }
\{\text{finite Borcherds denominator coefficients of }\Delta_5\}
```

with orientation character, Weyl chamber, and denominator normalization
matching the automorphic boundary functor.  This keeps the Igusa physics
in its correct place: it controls an automorphic boundary realization of
the theta-enhanced Hall object, not the definition of the base positive
geometry.

## 11. Master Theorem Target

Let `X` be a smooth compact or locally finite CY3 source equipped with
the data constructing

```tex
P^{BPS,motloc}_{\sigma,S,o,T_{\rm eq}}(X).
```

Let `\mathfrak T` be one of

```tex
\mathfrak T_{\rm bl},
\mathfrak T_{\rm GHKK},
\mathfrak T_{\rm GMN},
\mathfrak T_{\rm Hall}
```

and assume the corresponding obstruction tuple vanishes on every finite
truncation and is natural under strict-sector restriction.  Then:

1. the theta functions `\vartheta^{\lambda}_p` are constructed in
   `\widehat{\mathbb T}^{mot}_{S,\lambda}`;
2. they are compatible with truncation transition maps;
3. they localize over the motivic Hall cosheaf on strict sectors;
4. they multiply with motivic structure constants computed by the
   package-specific finite correspondence;
5. their Euler realizations give numerical theta functions with the
   same KS wall-crossing transport;
6. toric effective positive geometry is recovered as the terminal
   quiver/cluster degeneration;
7. conifold, cluster, GMN, Hall-framed, and Igusa boundary realizations
   are all specializations of the same enhancement formalism when their
   exact packages are supplied.

Equivalently,

```tex
\mathsf{ThetaEnh}_{\mathfrak T}
\bigl(
P^{BPS,motloc}_{\sigma,S,o,T_{\rm eq}}(X)
\bigr)
 =
P^{BPS,motloc,+\vartheta}_{\sigma,S,o,T_{\rm eq},\mathfrak T}(X)
```

is a theorem on the full subcategory where

```tex
\mathsf{Ob}_\vartheta(\mathfrak T)=0.
```

This is the monotone-strength resolution of obligation 9.  The base
positive geometry is the motivic Hall cosheaf.  The theta enhancement is
a functorial layer of framed or transported functions over that cosheaf.
The frontier is not the existence of a slogan called a theta basis; it
is the construction of one of the four exact theta packages and the
vanishing of its obstruction tuple.

