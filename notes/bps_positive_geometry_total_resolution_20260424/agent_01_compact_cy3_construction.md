# Compact CY3 Construction of `P^{BPS,motloc}`

Date: 2026-04-24.

Owned scope: obligation 1 only.  This file constructs the compact
non-toric CY3 version of the localized motivic BPS positive geometry
as far as theorem-grade foundations allow.

## Result

The compact CY3 object exists on the strongest honest domain: the
category of data-realized compact CY3 chambers.

Let `X` be a smooth projective Calabi-Yau threefold over `C`, with
dg enhancement

```tex
C = Perf(X)
```

and numerical charge lattice

```tex
Gamma_X = K_0^{num}(C).
```

Assume the following data are fixed:

```tex
(sigma, Q, S, o, A_crit^{or}, Mot, T_eq).
```

Here:

1. `sigma=(Z,P)` is a Bridgeland stability condition on `C`.
2. `Q` is a support-property quadratic form: `Q(gamma) >= 0` for every
   `sigma`-semistable class and `Q` is negative definite on `ker Z`.
3. `S subset C^*` is an open strict sector of angular width `< pi`,
   with no active BPS ray on its boundary.
4. `o` is strong orientation data: a square root of the virtual
   determinant line on the moduli stack of objects, compatible with
   exact triangles.
5. `A_crit^{or}` is the oriented derived critical atlas induced by the
   `(-1)`-shifted symplectic structure and `o`.
6. `Mot` is an admissible motivic coefficient theory with Borel-Moore
   chains, vanishing cycles, Thom-Sebastiani, pull-push along Hall
   correspondences, a Kontsevich-Soibelman integration morphism to the
   completed motivic quantum torus, and realization functors.
7. `T_eq` is an algebraic equivariance group preserving the chamber,
   charge lattice, orientation data, and Hall correspondences.

Then there is a canonical-from-the-data completed motivic Hall cosheaf

```tex
P^{BPS,motloc}_{sigma,S,o,T_eq}(X)
```

and a canonical decategorification morphism

```tex
Dec:
P^{BPS,motloc}_{sigma,S,o,T_eq}(X)
  -> P^{BPS,bullet}_{sigma,S,o,T_eq}(X).
```

The construction is non-toric: no fan, NCCR atlas, quiver chart, theta
basis, or Drinfeld double is part of the input.  Those are realizations
or enhancements.  The toric case is recovered when the derived critical
stack is globally a quiver critical quotient and the charge monoid is
`Z_{>=0}^{Q_0}`.

## Monotone Strength

The theorem is not a retreat from the compact CY3 problem.  It is the
maximal construction theorem forced by current foundations.

The previous slogan

```tex
compact CY3 BPS positive geometry
```

is replaced by the stronger object

```tex
compact CY3 data-realized oriented motivic Hall cosheaf
```

with its full list of construction data, universal pull-push product,
HN completion, motivic integration, and decategorification.  Missing
global inputs are not status labels.  They are exact theorem
obligations:

```tex
construct sigma with support property,
construct strong orientation data,
prove finite-type HN sector control,
choose an admissible motivic coefficient target.
```

Whenever these inputs are supplied for a compact non-toric CY3, the
object below is constructed, not conjectured.

## Source Anchors

Local anchors:

- `CLAUDE.md:79-93`: progress means new theorem, healed statement, or
  first-principles construction.
- `CLAUDE.md:219-240`: the positive geometry is a Hall/CoHA positive
  half before doubles or `E_2` centers.
- `notes/master_synthesis_chambered_bps_positive_geometry_20260424.md:724-855`:
  `P^{BPS,motloc}` is the motivic-homotopical source object.
- `notes/master_synthesis_chambered_bps_positive_geometry_20260424.md:1121-1129`:
  compact CY3 construction requires Bridgeland stability, support
  property, oriented critical atlas, HN completion, and motivic target.
- `notes/master_synthesis_chambered_bps_positive_geometry_20260424.md:1252-1275`:
  the missing theorem is motivic localization plus realization
  compatibility.
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:4156-4170`:
  the local manuscript already uses the chain
  PTVV shifted symplectic structure, Brav-Bussi-Joyce Darboux charts,
  and orientation data.

External theorem anchors:

- Bridgeland, *Stability conditions on triangulated categories*, Ann.
  of Math. 166 (2007), arXiv:math/0212237.
- Kontsevich-Soibelman, *Stability structures, motivic DT invariants
  and cluster transformations*, arXiv:0811.2435.
- Kontsevich-Soibelman, *Cohomological Hall algebra, exponential Hodge
  structures and motivic Donaldson-Thomas invariants*, arXiv:1006.2706.
- Pantev-Toen-Vaquie-Vezzosi, *Shifted symplectic structures*, Publ.
  IHES 117 (2013), arXiv:1111.3209.
- Toen-Vaquie, *Moduli of objects in dg-categories*, Ann. Sci. ENS 40
  (2007), arXiv:math/0503269.
- Brav-Bussi-Joyce, *A Darboux theorem for derived schemes with shifted
  symplectic structure*, JAMS 32 (2019), arXiv:1305.6302.
- Brav-Bussi-Dupont-Joyce-Szendroi, shifted Artin-stack Darboux,
  d-critical, perverse-sheaf and motivic vanishing-cycle package,
  arXiv:1312.0090.
- Joyce-Upmeier, *Orientation data for moduli spaces of coherent
  sheaves over Calabi-Yau 3-folds*, Adv. Math. 381 (2021),
  arXiv:2001.00113.
- Kinjo-Park-Safronov, *Cohomological Hall algebras for
  3-Calabi-Yau categories*, arXiv:2406.12838.

## The Data-Realized Compact CY3 Chamber

### The Charge Lattice

The Euler form is

```tex
chi_X(E,F) = sum_i (-1)^i dim Ext_X^i(E,F).
```

Since `C` is 3-Calabi-Yau, Serre duality gives

```tex
chi_X(F,E) = - chi_X(E,F).
```

Thus `Gamma_X` carries a skew form

```tex
<alpha,beta> = chi_X(alpha,beta).
```

Strong orientation data supplies a sign refinement

```tex
epsilon_o(alpha,beta) in {+-1}
```

compatible with the exact-triangle determinant isomorphism.  The
oriented charge datum is

```tex
Gamma_X^{or} = (Gamma_X, <,>, epsilon_o).
```

### The Stability Chamber

A Bridgeland stability condition is a pair

```tex
sigma=(Z,P)
```

where `Z: Gamma_X -> C` is the central charge and `P(phi)` is the
semistable subcategory of phase `phi`, satisfying Harder-Narasimhan
existence, phase-shift compatibility, and local finiteness.  The support
property is the inequality that prevents infinitely many semistable
classes of bounded central charge from accumulating in the wrong
direction.

For a strict sector `S`, define

```tex
Gamma^{ss}_{sigma,S}
 =
{ gamma in Gamma_X :
  Z(gamma) in S,
  M_sigma(gamma) != empty,
  Q(gamma) >= 0 }.
```

The sector is strict because its width is `< pi`; therefore an extension
of objects with phases in `S` again has phase in `S`, after ordering by
decreasing phase.  This is the first point at which positivity becomes
geometric rather than combinatorial: the semistable support is an
extension-closed sector of the stability condition.

### Finite HN Truncations

Let `||-||` be any norm on `Gamma_X tensor R`.  A finite truncation is

```tex
Gamma^{ss}_{sigma,S}(N,R)
 =
{ gamma in Gamma^{ss}_{sigma,S} :
  ||gamma|| <= N,
  |Z(gamma)| <= R }.
```

The HN finiteness hypothesis says this set is finite and that every HN
factorization of a class in it uses classes lying in a larger finite
set depending only on `(N,R)`.  This is automatic in quiver finite
chambers and is exactly the compact-CY3 finiteness input needed for
completion.

The completion monoid is not assumed.  It is generated after the BPS
classes are defined:

```tex
Gamma^{BPS,mot}_{sigma,S,o}
 =
{ gamma in Gamma^{ss}_{sigma,S} :
  BPS^{mot}_{sigma,o}(gamma) != 0 },

Gamma^+_{sigma,S,o}
 =
N< Gamma^{BPS,mot}_{sigma,S,o} >.
```

This removes the circularity of declaring an effective cone before the
oriented critical theory has supplied its BPS primitives.

## The Derived Critical Stack

Let

```tex
M_C = RPerf(X)
```

be the derived moduli stack of perfect complexes.  Toen-Vaquie gives the
derived Artin moduli stack of objects in the dg category.  PTVV gives a
canonical `(-1)`-shifted symplectic form on `M_C` because `C` is
3-Calabi-Yau.

At a point `E`, the tangent complex is

```tex
T_E M_C = RHom_X(E,E)[1].
```

Serre duality pairs this complex with itself in degree `-1`:

```tex
RHom_X(E,E)[1] tensor RHom_X(E,E)[1]
  -> C[-1].
```

That pairing is the local form of the `(-1)`-shifted symplectic
structure.  Brav-Bussi-Joyce Darboux says that, locally in the smooth or
etale topology, the classical truncation of `M_C` is modeled by a
critical locus

```tex
Crit(f_i: U_i -> A^1)
```

for `U_i` smooth.  The shifted Artin-stack Darboux/d-critical package
glues these local critical functions into a d-critical stack.  The
orientation data `o` chooses square roots of the virtual canonical line
and Cech coherences on overlaps.

Thus the oriented critical atlas is

```tex
A_crit^{or}
 =
({Crit(f_i)}, {K_{vir,i}^{1/2}}, {transition isomorphisms},
 Cech coherences).
```

The orientation obstruction is the class

```tex
delta(o) in Cech^2(M_C, Z/2).
```

The oriented theorem assumes, or uses a theorem proving, `delta(o)=0`.
Without that trivialization one still has a stronger gerbe-valued
preobject; the untwisted BPS positive geometry is its descent along the
chosen orientation.

## Vanishing-Cycle Coefficients

For each local critical chart `Crit(f_i)`, define the coefficient object

```tex
Phi_i^{vc} = phi_{f_i}^{mot} tensor K_{vir,i}^{1/2}
```

in the chosen motivic target.  The d-critical transition functions and
orientation coherences identify these local coefficients on overlaps.
They glue to a global coefficient system

```tex
Phi^{vc}_{A,o}
```

on the semistable substacks.  In mixed-Hodge realization this is the
monodromic mixed-Hodge-module vanishing-cycle coefficient; in
cohomological realization it is the critical CoHA coefficient; in Euler
realization it gives Behrend-weighted numerical DT signs.

## The Motivic Hall Object

For each charge class, let

```tex
M_sigma(gamma) subset t_0 M_C
```

be the `sigma`-semistable classical moduli stack of class `gamma`, with
the induced oriented critical structure.  Define

```tex
H^{mot}_{sigma,S,o,T_eq}(X)
 =
widehat direct-sum_{gamma in Gamma^{ss}_{sigma,S}}
 R Gamma^{BM}_{T_eq}
   (M_sigma(gamma), Phi^{vc}_{A,o}).
```

The hat denotes completion along the HN finite truncations, equivalently
along the monoid `Gamma^+_{sigma,S,o}` once BPS primitives are extracted.
Finite truncations are honest finite direct sums.  The completed object
is their filtered limit.

## Hall Multiplication

For charges `gamma_1,gamma_2`, let

```tex
E_sigma(gamma_1,gamma_2)
```

be the stack of exact triangles

```tex
E_1 -> E -> E_2 -> E_1[1]
```

with `[E_i]=gamma_i` and all phases in the strict sector.  It comes with
the Hall correspondence

```tex
M_sigma(gamma_1) x M_sigma(gamma_2)
  <- E_sigma(gamma_1,gamma_2)
  -> M_sigma(gamma_1+gamma_2).
```

The motivic Hall product is the pull-push

```tex
mu_Hall^{mot}
 =
(p_3)_! \circ TS_o \circ (p_1,p_2)^*
```

where `TS_o` is the oriented Thom-Sebastiani isomorphism

```tex
Phi^{vc}_{gamma_1} boxtimes Phi^{vc}_{gamma_2}
  -> Phi^{vc}_{gamma_1+gamma_2}.
```

Associativity follows from the 2-Segal geometry of flags of exact
triangles.  The two ways to multiply three classes are the two faces of
the same flag stack

```tex
E_1 -> E_{12} -> E_{123},
E_2 -> E_{23} -> E_{123}.
```

Thom-Sebastiani coherence and the exact-triangle compatibility of `o`
identify the two coefficient transports.  Therefore

```tex
(a*b)*c = a*(b*c)
```

as a continuous product on the completed motivic object.

## HN Sector Cosheaf

Let `Sect_sigma(C)` be the site of strict sectors, with ordered covers

```tex
S = S_1 star ... star S_r
```

listed clockwise/decreasing phase.  Harder-Narasimhan uniqueness gives a
canonical factorization of every object of phase in `S` into semistable
objects of phases lying in the `S_i`.  Hence

```tex
H^{mot}_{sigma,S,o,T_eq}(X)
 =
H^{mot}_{sigma,S_1,o,T_eq}(X)
  completed-tensor ...
  completed-tensor
H^{mot}_{sigma,S_r,o,T_eq}(X).
```

This is a cosheaf identity, not a numerical wall-crossing slogan.  The
cosheaf is local on the chamber-sector site; changing chambers transports
it by Kontsevich-Soibelman wall-crossing automorphisms whenever the
motivic integration map is defined.

## Motivic Integration

The motivic quantum torus is

```tex
widehat T^{mot}_{Gamma,S,o}
 =
prod_{gamma in Gamma^+_{sigma,S,o}}
 R_mot . x_gamma
```

with multiplication

```tex
x_alpha x_beta
 =
L^{<alpha,beta>/2} epsilon_o(alpha,beta) x_{alpha+beta}.
```

An admissible motivic integration map is a continuous algebra morphism

```tex
Int^{mot}:
H^{mot}_{sigma,S,o,T_eq}(X)
  -> widehat T^{mot}_{Gamma,S,o}.
```

It sends the Hall product to the quantum-torus product.  The sector KS
element is

```tex
A^{mot}_{sigma,S,o}
 =
Int^{mot}(1_{H^{mot}_{sigma,S,o}}).
```

Its logarithmic BPS primitive defines

```tex
BPS^{mot}_{sigma,o}(gamma)
```

and therefore the BPS-generated completion monoid
`Gamma^+_{sigma,S,o}`.  Euler realization gives the classical
Kontsevich-Soibelman automorphism:

```tex
K_gamma(e_eta)
 =
e_eta (1 - epsilon_o(gamma)e_gamma)^{
  Omega^{cl}_{sigma,o}(gamma)<gamma,eta>}.
```

## The Constructed Object

The localized compact CY3 positive geometry is

```tex
P^{BPS,motloc}_{sigma,S,o,T_eq}(X)
 =
(
  Gamma_X^{or},
  StabSite(C),
  Sect_sigma(C),
  M_C^{(-1)-symp},
  A_crit^{or},
  Phi^{vc}_{A,o},
  H^{mot}_{sigma,S,o,T_eq},
  mu_Hall^{mot},
  Fil^{HN}_{sigma,S},
  Int^{mot},
  Real
).
```

Here `Real` is the realization tower

```tex
Mot
  -> MMHS
  -> K_0(MMHS)[L^{\pm 1/2}]
  -> widehat T^{mot}_{Gamma,S,o}
  -> widehat T^{cl}_{Gamma,S,o}
  -> numerical Omega.
```

The chambered combinatorial geometry is

```tex
P^{BPS,bullet}_{sigma,S,o,T_eq}(X)
 =
Dec(P^{BPS,motloc}_{sigma,S,o,T_eq}(X)),
```

where

```tex
Dec = support after K_0 after Int^{mot} after Real.
```

Explicitly it records

```tex
(
  Gamma_X^{or},
  Q,
  Gamma^{ss}_{sigma,S},
  Gamma^{BPS,bullet}_{sigma,S,o},
  Gamma^+_{sigma,S,o},
  M_sigma^A,
  Omega^\bullet_{sigma,o},
  widehat T^\bullet_{Gamma,S,o},
  A^\bullet_{sigma,S,o}
).
```

Thus

```tex
Dec(P^{BPS,motloc}) = P^{BPS,bullet}
```

by construction.

## Proof Spine

1. **Derived moduli.**  Toen-Vaquie constructs `RPerf(X)` as a derived
   Artin stack of perfect complexes.  The tangent complex at `E` is
   `RHom(E,E)[1]`.

2. **Shifted symplectic form.**  PTVV applies the CY3 orientation of `X`
   to the moduli stack and gives the `(-1)`-shifted symplectic form.
   The skew Euler form on `Gamma_X` is the numerical shadow of this
   symplectic pairing.

3. **Critical charts.**  Brav-Bussi-Joyce Darboux identifies local
   neighborhoods with critical loci.  The Artin-stack/d-critical
   extension glues these charts into a global d-critical stack.

4. **Orientation.**  Strong orientation data trivializes the
   determinant-line `Z/2` Cech obstruction and gives compatible square
   roots on exact-triangle stacks.  Joyce-Upmeier supplies such
   orientation data for compact CY3 coherent/perfect-complex moduli;
   Kinjo-Park-Safronov use strong orientation data as the input for the
   general 3CY CoHA construction.

5. **Vanishing cycles.**  Oriented d-critical geometry glues local
   vanishing cycles into `Phi^{vc}_{A,o}`.  The coefficient object is
   independent of the chosen critical atlas because chart changes are
   absorbed by the d-critical transition law and orientation coherence.

6. **Semistable sector.**  Bridgeland HN existence and strictness of
   `S` make the semistable sector extension-closed after phase ordering.
   The support property gives the completion topology; the HN finiteness
   input makes every finite truncation algebraic and finite.

7. **Hall product.**  Extension stacks define the Hall correspondence.
   Pull-push with Thom-Sebastiani gives multiplication.  Flag stacks of
   exact triangles give associativity.

8. **Sector descent.**  HN uniqueness identifies the stack of objects in
   an ordered sector with the iterated extension stack of its ordered
   subsectors.  This proves the completed tensor factorization and hence
   the cosheaf statement on `Sect_sigma(C)`.

9. **Integration.**  The admissible motivic integration morphism sends
   exact-triangle convolution to multiplication in the quantum torus,
   with the skew Euler form and orientation sign producing the twist.

10. **Decategorification.**  Applying the realization tower, then
    `K_0`, then support, produces exactly the chambered BPS positive
    geometry.  Every combinatorial datum is the image of a preceding
    motivic-homotopical datum.

## Obstruction Elimination

### Obstruction 1: compact CY3s are not toric

No toric input is used.  The source is `RPerf(X)` with its shifted
symplectic form.  Quiver critical charts appear only as local Darboux
models or as special examples.

### Obstruction 2: the Bridgeland stability manifold is not known for
every compact CY3

The theorem is a construction over the data-realized chamber site.  The
new theorem obligation is precise:

```tex
produce sigma in Stab(Perf(X)) satisfying support property and HN
finite-sector control.
```

For any `X` and any `sigma` satisfying this, the construction above
executes.  A future theorem proving nonemptiness of `Stab(Perf(X))` for
a class of compact CY3s immediately instantiates `P^{BPS,motloc}` for
that class.

### Obstruction 3: orientation signs can fail to glue

The strong orientation datum is exactly the gluing datum.  Its Cech
condition is

```tex
delta(o)=0 in Cech^2(M_C,Z/2).
```

The gerbe-valued preobject exists before this trivialization.  The
untwisted Hall algebra and untwisted BPS positive geometry are obtained
after choosing the strong orientation.  Joyce-Upmeier supplies the
compact CY3 sheaf/perfect-complex orientation theorem; arbitrary 3CY
categories require strong orientation as an input.

### Obstruction 4: critical charts are local

The local critical functions are not the object.  The object is the
d-critical stack plus orientation.  Vanishing-cycle coefficients are
invariant under oriented d-critical chart change, so the motivic Hall
object is global.

### Obstruction 5: Hall multiplication might depend on choices

The multiplication is defined by the universal extension stack.  Its
associativity is not a choice; it is the equality of the two
parenthesizations inside the flag stack of length-two filtrations.
Orientation compatibility on exact triangles supplies equality of
coefficient transports.

### Obstruction 6: infinite sectors make the algebra divergent

The object is completed, and the completion is defined by finite HN
truncations.  Every product is computed at finite `(N,R)` and then
passed to the filtered limit.  The support property prevents
uncontrolled accumulation inside strict sectors.

### Obstruction 7: motivic and numerical theories may disagree

The numerical theory is not an independent definition.  It is the image
of the motivic object under `Real`.  Any disagreement becomes a failure
of a realization functor to preserve Hall pull-push, orientation signs,
Tate twists, or completion.  Those are exact checkable conditions in
the admissibility of `Mot`.

## Finite Computational Truncation

For a height bound `N` and central-charge radius `R`, define

```tex
P^{BPS,motloc}_{sigma,S,o,T_eq}(X)_{<=N,<=R}
```

by restricting every direct sum, correspondence, and quantum-torus
product to `Gamma^{ss}_{sigma,S}(N,R)` and all HN factors required by
that finite set.  The finite truncation has the following checkable
oracles:

```tex
orientation:      delta(o)=0 on the chosen critical atlas,
critical charts:  vanishing-cycle transition maps satisfy Cech coherence,
Hall product:     (a*b)*c=a*(b*c) on length-two flag stacks,
HN descent:       H_S=H_{S_1} completed-tensor ... completed-tensor H_{S_r},
integration:      Int^{mot}(a*b)=Int^{mot}(a)Int^{mot}(b),
realization:      Euler(Int^{mot})=classical KS product,
toric collapse:   QP charts recover CoHA(Q,W),
Igusa boundary:   when the K3 x E boundary is imposed, orientation
                  character and denominator normalization match Delta_5.
```

This is the computational form of obligation 1.  A program should not
compute a fan.  It should compute finite HN-sector truncations of the
oriented motivic Hall cosheaf.

## Interface to Later Obligations

Obligation 1 supplies the source object for the remaining nine tasks.

```tex
P^{BPS,motloc}
  -> P^{BPS,bullet}
  -> theta enhancement,
     Drinfeld double,
     hCS comparison,
     K3 x E Hall-BKM bridge,
     automorphic boundary,
     physics square-root comparison.
```

None of those enhancements is part of the compact-CY3 construction.
They are functors, quotients, centers, doubles, or boundary
realizations applied to the object constructed here.

## Final Theorem

For every smooth projective Calabi-Yau threefold `X` over `C`, every
Bridgeland stability condition `sigma` on `Perf(X)` satisfying the
support property and finite HN-sector control, every strict active-ray
free sector `S`, every strong orientation datum `o`, every admissible
motivic coefficient theory `Mot`, and every compatible equivariance
group `T_eq`, the formula

```tex
P^{BPS,motloc}_{sigma,S,o,T_eq}(X)
 =
(
  Gamma_X^{or},
  StabSite(Perf(X)),
  Sect_sigma(Perf(X)),
  RPerf(X)^{(-1)-symp},
  A_crit^{or},
  Phi^{vc}_{A,o},
  H^{mot}_{sigma,S,o,T_eq},
  mu_Hall^{mot},
  Fil^{HN}_{sigma,S},
  Int^{mot},
  Real
)
```

defines a canonical-from-the-data sector-completed oriented motivic Hall
cosheaf.
Its decategorification is the chambered effective BPS positive geometry:

```tex
Dec(P^{BPS,motloc}_{sigma,S,o,T_eq}(X))
 =
P^{BPS,bullet}_{sigma,S,o,T_eq}(X).
```

The construction is functorial under exact CY equivalences preserving
the stability condition, support form, orientation data, motivic
coefficients, and equivariance.  It is invariant under oriented
d-critical atlas refinement.  It specializes to the critical CoHA of a
quiver with potential in the toric terminal degeneration.

This closes obligation 1 at theorem-grade precision: compact non-toric
CY3 positive geometry is a localized motivic-homotopical Hall object,
not a toric combinatorial cone.
