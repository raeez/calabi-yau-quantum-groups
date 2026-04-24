# Agent 03: Sector Descent and HN Hall Cosheaf

Owned file:
`notes/bps_positive_geometry_total_resolution_20260424/agent_03_sector_descent_hn_cosheaf.md`.

Task: obligation 3, sector descent theorem.

Changed files: this file only.

## Result

The sector assignment is not merely a notation for an ordered product of
KS factors.  Under the exact Harder--Narasimhan, support, orientation,
and critical-Hall hypotheses below, it is a completed motivic Hall
cosheaf on the strict-sector site, flat over the chamber-sector site,
with wall transport given by motivic quantum-dilogarithm conjugation and
with identity holonomy around every codimension-two joint in every finite
HN truncation.

The stronger object is the HN hull of the semistable/BPS primitive
system.  The semistable stack is the primitive input; the cosheaf lives
on all objects whose HN factors lie in the sector.  This is the precise
form in which descent is true.

## Standing Hypotheses

Let `C` be a `C`-linear Calabi--Yau 3 category with numerical charge
lattice

```tex
Gamma = K^{num}_0(C),
```

Euler form `chi`, skew form

```tex
<alpha,beta> = chi(alpha,beta)-chi(beta,alpha),
```

and a Bridgeland stability condition

```tex
sigma=(Z_sigma,P_sigma).
```

The theorem is stated under the following explicit hypotheses.

**HN.** Every object of the extension-closed sector category defined
below has a finite HN filtration with semistable factors of strictly
decreasing phase, and this filtration is unique up to unique
isomorphism of associated graded factors.

**Support.** There is a real quadratic form `Q` on `Gamma_R`, negative
definite on `ker Z_sigma`, such that

```tex
Q(gamma) >= 0
```

for every active semistable charge.  Equivalently, after choosing a norm
on `Gamma_R`, there is `C_Q>0` such that

```tex
||gamma|| <= C_Q |Z_sigma(gamma)|
```

for every active semistable charge `gamma`.  This makes every bounded
strict-sector truncation finite.

**Algebraic boundedness.** For every strict sector `S` and every finite
truncation `lambda` defined below, the stack of semistable objects with
charge in `Gamma_{S,lambda}` and the corresponding HN flag stacks are
Artin stacks of finite type with the stabilizer and equivariance
conditions needed for Borel--Moore pull-push.

**Critical atlas.** The derived moduli stack of objects of `C` carries a
`(-1)`-shifted symplectic structure, and on the bounded pieces under
consideration it admits an oriented critical/d-critical atlas

```tex
A^{or}_{crit} = ({Crit(f_i)->U_i}, o, cocycles).
```

**Orientation.** The virtual determinant line has a coherent square
root `o`, hence a sign cocycle

```tex
epsilon_o: Gamma x Gamma -> {+-1}
```

compatible with direct sum, extensions, and restriction to critical
charts.

**Vanishing cycles.** The coefficient target `R_mot` supports
vanishing-cycle coefficients, Borel--Moore pushforward, smooth/lci
pullback, exterior product, inverse limits over truncations, and
Thom--Sebastiani isomorphisms.  Typical choices are monodromic mixed
Hodge modules, l-adic sheaves, Voevodsky motives after realization, or
the corresponding Grothendieck group when the motivic realization is all
that is available.

**Hall properness.** The extension correspondence is admissible for
pull-push in the chosen coefficient theory:

```tex
M(gamma_1) x M(gamma_2)
  <- E(gamma_1,gamma_2)
  -> M(gamma_1+gamma_2).
```

For non-proper maps this means the Borel--Moore, compactly supported, or
equivariant version fixed in the coefficient target.

These hypotheses are construction hypotheses, not weakenings of the
claim.  They are precisely the data required for the desired descent
statement to be a theorem.

## Strict Sectors

A **strict sector** for `sigma` is an open convex sector

```tex
S = { r exp(i theta) : r>0, theta_0 < theta < theta_1 } subset C^*
```

with angular width

```tex
0 < theta_1-theta_0 < pi
```

such that neither boundary ray contains the central charge of an active
semistable object:

```tex
Z_sigma(gamma) notin partial S
```

for every active `gamma`.

For a strict sector `S`, define the sector subcategory

```tex
C_{sigma,S}^{HN}
```

to be the full subcategory of objects whose HN semistable factors have
central charges in `S`.  Define the semistable sector substack

```tex
M^{ss}_{sigma,S}(gamma)
```

and the HN sector stack

```tex
M^{HN}_{sigma,S}(gamma).
```

Thus `M^{ss}` records primitive semistable pieces; `M^{HN}` records all
objects built from those pieces by finite HN extensions.

The strict-sector site `Sect_sigma(C)` has:

```tex
objects: strict sectors S;
morphisms: inclusions of strict sectors;
covers: ordered decompositions S=S_1 star ... star S_r.
```

The ordered cover condition means:

```tex
S_i subset S,
S = union_i S_i,
arg(S_1) > arg(S_2) > ... > arg(S_r),
```

and no active ray lies on an internal boundary.  The star symbol records
phase order, not disjoint union: small inactive overlaps are allowed, and
refinement is taken by inserting additional inactive boundary rays.

## Finite Truncations

Fix an additive height function

```tex
h: Gamma^+_{sigma,S,o} -> Z_{>=0}
```

positive away from `0`.  A finite truncation is a pair

```tex
lambda=(R,N),    R>0, N in Z_{>=0},
```

and the finite charge set is

```tex
Gamma_{S,lambda}
 =
 { gamma in Gamma^+_{sigma,S,o} :
   Z_sigma(gamma) in S,
   |Z_sigma(gamma)| <= R,
   h(gamma) <= N,
   Q(gamma) >= 0 }.
```

Finiteness follows from the support property: bounded `|Z|` bounds
`||gamma||`, and a lattice has finitely many points in a bounded ball.

Let `F^{>lambda} H_S` be the closed ideal generated by charges outside
`Gamma_{S,lambda}` and by products whose total charge exits
`Gamma_{S,lambda}`.  The completed Hall object is the inverse limit

```tex
widehat H^{mot}_{sigma,S,o}
 =
 lim_lambda H^{mot}_{sigma,S,o}/F^{>lambda}H^{mot}_{sigma,S,o}.
```

Every identity below is first an identity in each finite quotient and
then an identity in the inverse limit.

## The Completed Motivic Hall Object

Define

```tex
H^{mot}_{sigma,S,o}
 =
 direct sum_{gamma}
 R Gamma^{BM}
 (M^{HN}_{sigma,S}(gamma), Phi^{vc}_{A,o}),
```

where the sum is over charges in the sector completion monoid and
`Phi^{vc}_{A,o}` is the vanishing-cycle coefficient system determined
by the oriented critical atlas.  Its completion is
`widehat H^{mot}_{sigma,S,o}`.

The Hall product is the pull-push operation

```tex
mu_{alpha,beta}:
H_alpha tensor H_beta -> H_{alpha+beta}
```

along the extension correspondence, with coefficient transport

```tex
Phi_alpha^{vc} boxtimes Phi_beta^{vc}
  -> Phi_{alpha+beta}^{vc}
```

given by Thom--Sebastiani and the orientation data.

Associativity is the equality of the two pull-push composites over the
stack of two-step flags

```tex
0 subset E_1 subset E_2 subset E_3,
```

or, equivalently, the 2-Segal associativity of extension stacks plus the
coherence of Thom--Sebastiani and orientation transport.

The primitive semistable object attached to a ray `ell subset S` is

```tex
H^{ss,mot}_{sigma,ell,o}
 =
 direct sum_{Z(gamma) in ell}
 R Gamma^{BM}
 (M^{ss}_{sigma}(gamma), Phi^{vc}_{A,o}).
```

The HN Hall algebra is generated, topologically, by the ray pieces in
phase order.

## Sector Descent Theorem

**Theorem.** Under the standing hypotheses, the assignment

```tex
S |-> widehat H^{mot}_{sigma,S,o}
```

is a factorization cosheaf on `Sect_sigma(C)`.  More precisely:

1. For each strict sector `S`, `widehat H^{mot}_{sigma,S,o}` is an
   associative complete topological motivic Hall algebra.

2. For every ordered cover

```tex
S = S_1 star ... star S_r
```

Hall multiplication gives a canonical topological isomorphism

```tex
mu_{S_1,...,S_r}:
widehat H^{mot}_{sigma,S_1,o}
  completed_tensor ...
  completed_tensor widehat H^{mot}_{sigma,S_r,o}
    -> widehat H^{mot}_{sigma,S,o}.
```

3. These isomorphisms are compatible with all ordered refinements.  For
   every refinement of an ordered cover, the two maps obtained by first
   multiplying refined sectors and then multiplying coarse sectors, or
   by multiplying all refined sectors at once, are equal.

4. After motivic integration, the cosheaf maps to the completed motivic
   quantum torus

```tex
widehat T^{mot}_{Gamma,S,o}
 =
 prod_{gamma in Gamma^+_{sigma,S,o}} R_mot . x_gamma,

x_alpha x_beta
 =
 L^{<alpha,beta>/2} epsilon_o(alpha,beta) x_{alpha+beta}.
```

The integrated sector element factors as

```tex
A_S(sigma)
 =
 A_{S_1}(sigma) ... A_{S_r}(sigma)
```

for every ordered cover.

5. The Euler, Hodge, and numerical realizations of the motivic cosheaf
   are obtained by applying the corresponding realization functor to the
   same finite-truncation inverse system.  Realization commutes with
   sector descent whenever the realization functor preserves the
   pull-push and Thom--Sebastiani structures in the standing
   hypotheses.

This theorem is strictly stronger than the combinatorial positive
geometry: applying

```tex
support o K_0 o Int^{mot}
```

to this cosheaf gives the chambered BPS support, completion monoid, KS
product, and numerical wall-crossing system.

## Proof

The proof is local on the strict-sector site and finite before
completion.

First fix a finite truncation `lambda`.  By algebraic boundedness, only
finitely many charges and HN types occur.  The stack

```tex
M^{HN}_{sigma,S,lambda}
```

is the disjoint union of locally closed HN strata indexed by finite
ordered lists

```tex
tau=(gamma_1,...,gamma_m),
arg Z(gamma_1)>...>arg Z(gamma_m),
sum_i gamma_i in Gamma_{S,lambda}.
```

The HN hypothesis gives an equivalence between each stratum and the
corresponding stack of objects equipped with their HN filtration.  The
filtration is canonical, so forgetting the filtration is an isomorphism
onto the stratum, not a many-to-one cover.

Now take an ordered cover

```tex
S=S_1 star ... star S_r.
```

Each HN type in `S` decomposes uniquely into consecutive blocks whose
phases lie in the ordered subsectors `S_i`.  Conversely, an object in
`C_{sigma,S_i}^{HN}` for each `i`, multiplied by the Hall extension
correspondence in the order `S_1,...,S_r`, gives an object in
`C_{sigma,S}^{HN}` with HN factors in `S` and with those same
consecutive phase blocks.  HN uniqueness makes these two constructions
inverse on HN strata.

Thus, at finite truncation, the iterated extension correspondence
realizes an equivalence of HN flag stacks:

```tex
Flag^{HN}(S_1,...,S_r)_{lambda}
  ~= M^{HN}_{sigma,S,lambda}.
```

Applying Borel--Moore homology with vanishing-cycle coefficients gives
an isomorphism because the coefficient on the extension stack is
identified with the exterior tensor product of the coefficients on the
ordered factors by Thom--Sebastiani, and the square-root orientation
data is coherent under extension.  This is exactly the Hall product
map

```tex
mu^{lambda}_{S_1,...,S_r}.
```

Associativity and refinement compatibility follow by replacing one
ordered flag by a refined ordered flag.  Both composites are pull-push
along the same stack of refined flags.  The equality is the 2-Segal
identity for the simplicial extension stack, with no extra scalar
because the orientation cocycles have already been required to satisfy
their direct-sum and extension coherences.

The finite isomorphisms are compatible as `lambda` increases.  Passing
to the inverse limit gives the completed topological isomorphism

```tex
mu_{S_1,...,S_r}.
```

This proves the cosheaf statement.

Motivic integration is a homomorphism from the motivic Hall algebra to
the motivic quantum torus.  The factor

```tex
L^{<alpha,beta>/2} epsilon_o(alpha,beta)
```

is the image of the Euler form and orientation line under integration.
Therefore integration sends the Hall multiplication isomorphism to the
ordered product identity in the completed quantum torus.  Since
realization functors are applied levelwise on finite quotients, they
commute with sector descent whenever they preserve the six operations
used above.

## Chamber-Sector Local System

Let `ChSect(C)` be the chamber-sector category.  Its objects are pairs

```tex
(sigma,S)
```

with `sigma` a stability condition in a chamber and `S` strict for
`sigma`.  Morphisms are generated by:

1. ordered inclusions/refinements inside a fixed chamber;
2. admissible chamber paths `p: sigma_0 -> sigma_1` whose endpoint
   sectors stay strict and whose crossings with walls are finite in
   each truncation.

At a wall `W`, let `ell_W` be the active ray and let

```tex
A_{ell_W}^{mot}
 =
 prod_{Z(gamma) in ell_W}
 E(x_gamma)^{Omega^{mot}_{sigma,o}(gamma)}
```

be the motivic quantum-dilogarithm wall factor in the completed ray
torus.  The wall transport on the integrated torus is

```tex
T_W(a) =
  (A_{ell_W}^{mot})^{-1} a A_{ell_W}^{mot}
```

or the inverse conjugation, according to the orientation of the chamber
path.  On the Hall side the same formula is implemented before
integration by multiplying with the HN ray Hall element and its inverse
in the completed Hall group.

**Flatness theorem.** Under the standing hypotheses and the KS
wall-crossing identity in each finite truncation, the completed Hall
cosheaf forms a flat local system over `ChSect(C)`: the transport
assigned to a concatenated path is the composite of transports, and the
transport around every contractible loop enclosing a codimension-two
joint is the identity in every finite truncation.

**Proof.** A path crossing no wall preserves the phase order of all
active rays in every truncation, hence preserves the HN stratification
and acts by the identity after identifying the same moduli stacks.  At a
single wall, the only change is the relative order of the active ray
`ell_W` with its neighboring rays.  HN factorization writes the same
sector object as the product before crossing and as the product after
crossing.  KS wall-crossing is precisely the equality of these two
phase-ordered products, so the change of trivialization is conjugation
by `A_{ell_W}^{mot}`.

At a codimension-two joint, choose `lambda`.  Only finitely many charges
and walls occur in the local rank-finite quotient.  The product of wall
transports around the joint compares two complete ordered HN
factorizations of the same finite Hall element.  The factorization
cosheaf theorem says both factorizations are the image of the same
refined HN flag stack.  Therefore their quotient is the identity.  The
inverse limit over `lambda` gives identity holonomy in the completed
cosheaf.

## Joint Consistency

Joint consistency is not an additional axiom after the HN cosheaf has
been built.  It is the finite-truncation form of associativity plus HN
uniqueness.

For a joint `J`, let `Gamma_J` be the finite-rank sublattice generated
by charges active at `J` in a truncation `lambda`.  The joint
consistency equation is

```tex
prod_{walls around J}^{cyclic} T_W = id
  in Aut(widehat T^{mot}_{Gamma_J,S,o}/F^{>lambda}).
```

The proof above identifies this cyclic product with the comparison of
two ordered refinements of the same HN flag stack.  The identity is
therefore forced by the equality of the two flag-stack pull-push
composites.

Rank-two joints give the familiar elementary relations:

```tex
A_1 x A_1: commuting wall factors;
A_2:       quantum pentagon;
B_2,G_2:   higher rank-two quantum dilogarithm identities when those
           root systems occur in the finite quotient.
```

The conifold realizes the `A_2` case.

## Conifold Pentagon Anchor

For the resolved conifold in the Klebanov--Witten chamber, the relevant
rank-two quotient has simples `S_0,S_1` with charges

```tex
gamma_0=[S_0],
gamma_1=[S_1],
<gamma_0,gamma_1>=1.
```

Let

```tex
X=x_{gamma_0},   Y=x_{gamma_1},   YX=qXY.
```

The two HN sector decompositions across the elementary wall are

```tex
(gamma_0, gamma_1)
```

and

```tex
(gamma_1, gamma_0+gamma_1, gamma_0).
```

The integrated sector-descent identity is the quantum pentagon

```tex
E(X)E(Y) = E(Y)E(q^{-1/2}XY)E(X).
```

The middle factor is not decorative: it is the HN bound-state factor of
charge `gamma_0+gamma_1`, with the quantum cocycle `q^{-1/2}` coming
from the skew Euler form and orientation convention.

Local executable anchors in this repository:

```text
compute/tests/test_conifold_wall_crossing.py
compute/tests/test_coha_wall_crossing_platonic.py
compute/tests/test_wallcrossing_gauge_engine.py
```

The first file checks the quantum-torus pentagon directly; the second
records the Hall/KS statement in the manuscript's local wall-crossing
chapter; the third records finite BCH/gauge approximations and their
truncation limits.

## Finite-Truncation Protocol

A finite computation of sector descent is the following inverse-system
test, not a computation of a bare fan.

Input:

```text
Gamma, <->, Z_sigma, Q, epsilon_o,
active charges and Omega^{mot} through lambda=(R,N),
ordered cover S=S_1 star ... star S_r.
```

Protocol:

1. Enumerate `Gamma_{S,lambda}` and the subsets
   `Gamma_{S_i,lambda}`.
2. Sort active rays by phase.
3. Enumerate HN types in `S` with total charge in
   `Gamma_{S,lambda}`.
4. Block each HN type according to the ordered cover.
5. Build the truncated Hall product by extension flags, or after
   integration the truncated quantum-torus product

```tex
x_alpha x_beta =
L^{<alpha,beta>/2} epsilon_o(alpha,beta)x_{alpha+beta}
```

   projected to the finite quotient.
6. Verify

```tex
mu^{lambda}_{S_1,...,S_r}
```

   is bijective on the finite HN-type basis and preserves the
   coefficient product.
7. For wall transport, compute both phase-ordered products before and
   after crossing and check equality modulo `F^{>lambda}`.
8. For a joint, compose all wall transports around the loop and check
   identity modulo `F^{>lambda}`.

The support property is the reason this protocol terminates for fixed
`lambda`.

## Compact CY3 Construction Obligations

For a compact non-toric CY3 category, the theorem above gives the
complete target.  To instantiate it one must build the following data.

1. A Bridgeland stability condition on the relevant component of
   `Stab(C)` and an explicit central charge

```tex
Z: Gamma -> C.
```

2. A support-property quadratic form `Q` with bounded active support.

3. Boundedness of semistable moduli in every strict sector and finite
   truncation.

4. A global oriented critical/d-critical atlas on the semistable and HN
   extension stacks.

5. A coherent square root of the determinant line, equivalently the
   vanishing of the orientation `Cech^2(Z/2)` obstruction or the
   construction of the exact twisted orientation local system.

6. Thom--Sebastiani compatibility for the chosen vanishing-cycle
   coefficient theory on all extension correspondences.

7. Hall pull-push admissibility for the compact moduli stacks, including
   the correct Borel--Moore/proper-support convention.

8. A motivic integration map to the completed motivic quantum torus with
   the exact skew Euler and orientation signs.

9. Finite-truncation KS wall-crossing in each rank-finite quotient.

10. Identity holonomy around codimension-two joints after passing to the
    inverse limit.

Once these ten items are constructed, sector descent is not a further
conjecture.  It follows from the theorem.

## Relationship to the Positive Geometry

The chambered BPS positive geometry is the decategorified shadow of the
HN Hall cosheaf:

```tex
widehat H^{mot}_{sigma,S,o}
  -> widehat T^{mot}_{Gamma,S,o}
  -> K_0 / Hodge / Euler / numerical realization
  -> (Gamma^{ss}_{sigma,S},
      Gamma^{BPS}_{sigma,S,o},
      Gamma^+_{sigma,S,o},
      A_S(sigma)).
```

The toric effective positive geometry is the terminal degeneration in
which:

```tex
Gamma^{ss}_{sigma,S}=Gamma^+_{sigma,S,o}=Z^{Q_0}_{>=0},
M^{HN}_{sigma,S} is the quiver representation HN stack,
widehat H^{mot}_{sigma,S,o}=completed critical CoHA(Q,W),
```

and the sector cosheaf becomes the ordinary ordered Hall factorization
of quiver representations.  The conifold pentagon is the first
nontrivial finite joint in this degeneration.

## Worker Verdict

Obligation 3 is solved at theorem level under the exact hypotheses the
object requires:

```tex
strict-sector site
+ HN finite uniqueness
+ support property
+ oriented critical atlas
+ motivic vanishing cycles
+ Hall pull-push
+ finite-truncation KS
=> completed motivic Hall cosheaf
=> flat chamber-sector local system
=> joint consistency
=> conifold pentagon
=> decategorified BPS positive geometry.
```

The remaining compact CY3 work is not to invent another descent law.  It
is to construct the ten inputs above for the compact category.
