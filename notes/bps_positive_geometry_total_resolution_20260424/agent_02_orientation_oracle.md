# Worker 02: Orientation Oracle for Chambered BPS Positive Geometry

Date: 2026-04-24.

Owned file:
`notes/bps_positive_geometry_total_resolution_20260424/agent_02_orientation_oracle.md`.

Task: obligation 2, orientation oracle.  The output below solves the
orientation layer as a first-principles construction, not as a sign
convention: determinant-line square roots, `Z/2` Cech cocycle,
orientation local systems, overlap transport, Thom--Sebastiani
compatibility, toric compute protocol, and compact-chart extension.

## Executive Theorem

Let `C` be a `3`-Calabi--Yau category whose derived moduli stack of
objects

```tex
M_C = RObj(C)
```

is locally geometric, locally of finite presentation on every chosen
charge truncation, and equipped with the `(-1)`-shifted symplectic form
induced by the CY pairing.  Let `M_C^cl` be its classical truncation with
the Joyce d-critical structure `s`.

The orientation oracle attached to `C` is the functorial datum

```tex
Or_C =
(
  { (R_i, U_i, f_i, i_i) },
  { O_i },
  { theta_ij },
  c_o in Cech^2(M_C^red, Z/2),
  L_o,
  T_ij,
  TS_o,
  Fus_o,
  q_o
).
```

It has the following meaning.

1. `(R_i, U_i, f_i, i_i)` is a d-critical Darboux atlas:
   `R_i subset M_C^cl`, `U_i` smooth, and
   `i_i: R_i -> Crit(f_i: U_i -> A^1)`.
2. `O_i` is the local square root of the d-critical canonical line:

   ```tex
   O_i = K_{U_i}|_{R_i},
   \qquad
   O_i^{\otimes 2} = K_{M_C,s}|_{R_i}.
   ```

3. `theta_ij: O_i|_{R_ij} -> O_j|_{R_ij}` are local transports.
4. The triple-overlap defect

   ```tex
   c_{ijk}
     =
   theta_ki theta_jk theta_ij
     in {+-1}
   ```

   is a `Z/2` Cech `2`-cocycle.  Its cohomology class

   ```tex
   [c_o] in H^2(M_C^red, Z/2)
   ```

   is the exact obstruction to an honest global square root.
5. If `[c_o]=0`, a choice of trivialising `1`-cochain produces a global
   orientation line `O` with `O^{\otimes 2}=K_{M_C,s}`.  The set of all
   choices is a torsor for `H^1(M_C^red, Z/2)`.
6. If `[c_o]` is not killed by the chosen atlas, the oracle does not
   collapse.  It outputs the stronger object: a `[c_o]`-twisted
   orientation gerbe, a gerbe-twisted vanishing-cycle coefficient system,
   and a `[c_o]`-twisted motivic Hall algebra.  In the smooth proper CY3
   cases where canonical strong orientation data is available, this
   twist is trivialised by the source theorem.
7. `L_o` is the `Z/2` orientation local system of square-root choices.
8. `T_ij` are the induced overlap transports on vanishing cycles.
9. `TS_o` is the Thom--Sebastiani compatibility for products of critical
   charts.
10. `Fus_o` is the strong Hall-fusion compatibility along extension
    correspondences.
11. `q_o: Gamma -> {+-1}` is the quadratic refinement controlling the
    signs in the motivic quantum torus:

    ```tex
    q_o(alpha+beta)
      =
    (-1)^{<alpha,beta>} q_o(alpha) q_o(beta).
    ```

This oracle is exactly the missing orientation input for

```tex
P^{BPS,motloc}_{sigma,S,o,T_eq}(X).
```

It strengthens the previous formulation: positivity is not defined over
bare vanishing cycles.  It is defined over oriented, or gerbe-twisted
oriented, vanishing cycles with Thom--Sebastiani and Hall-fusion
coherence.

## First Principles: The Determinant Line

At an object `E in C`, the tangent complex of the derived moduli stack is

```tex
T_E M_C = RHom_C(E,E)[1].
```

The determinant line of the perfect complex `RHom(E,E)` is

```tex
D_E
 =
sdet RHom(E,E)
 =
tensor_i det Ext^i(E,E)^{(-1)^i}.
```

For a CY3 category, Serre duality gives perfect pairings

```tex
Ext^i(E,E) x Ext^{3-i}(E,E) -> C.
```

Thus

```tex
Ext^3(E,E) = Ext^0(E,E)^*,
\qquad
Ext^2(E,E) = Ext^1(E,E)^*.
```

Substitution gives the square form

```tex
D_E
 =
det Ext^0(E,E)
otimes det Ext^1(E,E)^{-1}
otimes det Ext^2(E,E)
otimes det Ext^3(E,E)^{-1}
```

and hence

```tex
D_E
 =
(
det Ext^0(E,E)
otimes det Ext^1(E,E)^{-1}
)^{\otimes 2}.
```

For a simple stable object, `Ext^0(E,E)=C`; the local root is

```tex
O_E = det Ext^1(E,E)^{-1}.
```

This formula is local in families.  Globally, transition maps between
local presentations may change the root by a sign.  The obstruction is
not a mystery sign.  It is the Cech class `[c_o]` above.

## d-Critical Canonical Line

Let `(M,s)` be the classical d-critical stack under a `(-1)`-shifted
derived moduli stack.  On a critical chart

```tex
R subset M,
\qquad
i: R -> Crit(f: U -> A^1),
\qquad
U smooth,
```

the d-critical canonical line is locally

```tex
K_{M,s}|_R = K_U^{\otimes 2}|_R.
```

Therefore the canonical local square root is

```tex
O_R = K_U|_R.
```

The equality with the Ext-determinant description is the Darboux
translation of the same CY3 pairing.  The critical chart sees
`Ext^1` as tangent directions and `Ext^2` as cotangent obstruction
directions; Serre duality identifies the obstruction determinant with
the tangent determinant dual, forcing the square.

The orientation problem is exactly:

```tex
find O on M^red such that O^{\otimes 2} = K_{M,s}.
```

Equivalently, choose the local roots `K_{U_i}` and prove that their
triple-overlap sign defect vanishes.

## The `Z/2` Cech Cocycle

Choose a d-critical atlas

```tex
M^red = union_i R_i,
\qquad
R_i -> Crit(f_i: U_i -> A^1).
```

Put

```tex
O_i = K_{U_i}|_{R_i}.
```

On `R_ij = R_i cap R_j`, the Joyce coordinate-change formalism supplies
an isomorphism of the squares:

```tex
O_i^{\otimes 2}|_{R_ij}
  ~= K_{M,s}|_{R_ij}
  ~= O_j^{\otimes 2}|_{R_ij}.
```

Choose a square-root transport

```tex
theta_ij: O_i|_{R_ij} -> O_j|_{R_ij}.
```

Then

```tex
c_ijk = theta_ki theta_jk theta_ij in Aut(O_i)|_{R_ijk} = {+-1}.
```

The assignment `c=(c_ijk)` satisfies `delta c=1`, because it is the
boundary of square-root transports whose squares already glue to the
canonical line.  Hence

```tex
c_o in Z^2(Cech(R), Z/2).
```

Changing `theta_ij` by a sign cochain `lambda_ij` changes `c` by
`delta lambda`.  Thus the obstruction class is

```tex
ob_2(M,s) = [c_o] in H^2(M^red, Z/2).
```

The oracle solves the orientation problem by computing this class.

If `ob_2=0`, choose `lambda_ij` with `c=delta lambda` and replace

```tex
theta_ij by lambda_ij^{-1} theta_ij.
```

The new transports satisfy

```tex
theta_ki theta_jk theta_ij = 1.
```

They glue the local roots into a global orientation line `O`.  If
`O` and `O'` are two solutions, then `O' tensor O^{-1}` is a flat
`Z/2` line; orientations form a torsor for `H^1(M^red,Z/2)`.

If `ob_2` is nonzero on the chosen moduli problem, the healed object is
not an unoriented Hall algebra.  It is the `ob_2`-twisted Hall object
whose coefficients are modules over the orientation gerbe.  This keeps
the theorem monotone: the obstruction becomes part of the positive
geometry rather than a reason to erase the statement.

## Orientation Local Systems and Vanishing Cycles

On a critical chart `(R_i,U_i,f_i)`, the chartwise coefficient is

```tex
Phi_i
 =
phi_{f_i}(Q_{U_i}[dim U_i])|_{R_i}.
```

The orientation root `O_i` gives a principal `Z/2` local system of
square-root choices.  Write it as `L_{o_i}`.  The oriented chart
coefficient is

```tex
Phi_{i,o} = Phi_i tensor L_{o_i}.
```

On overlaps the transport is

```tex
T_ij:
Phi_{i,o}|_{R_ij}
  ->
Phi_{j,o}|_{R_ij}.
```

It is the product of:

1. the canonical Joyce/Brav--Bussi--Joyce comparison between vanishing
   cycles for equivalent d-critical charts;
2. the sign line induced by `theta_ij`.

On triple overlaps,

```tex
T_ki T_jk T_ij = c_ijk.
```

Thus honest perverse sheaves or motives glue exactly when `[c_o]=0`.
When `[c_o]` is nonzero, they glue as objects twisted by the orientation
gerbe.  This is the correct coefficient system for the motivic Hall
object:

```tex
H^{mot}_{sigma,S,o,T_eq}
 =
widehat{direct sum}_{gamma in Gamma^{ss}_{sigma,S}}
R Gamma^{BM}_{T_eq}
(
  M_sigma^A(gamma),
  Phi^{vc}_{gamma,o}
).
```

The Euler-specialized Behrend sign is a shadow of `Phi^{vc}_{gamma,o}`.
It is not a replacement for the orientation local system.

## Thom--Sebastiani Compatibility

Let

```tex
M = Crit(f: U -> A^1),
\qquad
N = Crit(g: V -> A^1).
```

Their product critical chart is

```tex
M x N = Crit(f boxplus g: U x V -> A^1),
\qquad
(f boxplus g)(u,v)=f(u)+g(v).
```

The canonical line satisfies

```tex
K_{U x V}
 =
K_U boxplus K_V,
```

so the local orientation root satisfies

```tex
O_{M x N}
 =
O_M boxplus O_N.
```

Thom--Sebastiani gives the coefficient isomorphism

```tex
TS:
phi_f(Q_U[dim U]) boxplus phi_g(Q_V[dim V])
  ->
phi_{f boxplus g}(Q_{U x V}[dim U + dim V]).
```

With orientation local systems this becomes

```tex
TS_o:
Phi_{M,o_M}^{vc} boxplus Phi_{N,o_N}^{vc}
  ->
Phi_{M x N,o_M boxplus o_N}^{vc}.
```

The overlap transports commute with `TS_o`:

```tex
T_{ii'} boxplus T_{jj'}
  =
T_{(i,j),(i',j')} under TS_o.
```

This identity is the first non-negotiable coherence.  Without it, Hall
convolution is not an algebra product; it is only a collection of
vector spaces.

## Strong Hall-Fusion Orientation

Hall multiplication is not the Cartesian product alone.  It uses the
extension correspondence

```tex
M_alpha x M_beta
  <- E_{alpha,beta}
  -> M_{alpha+beta}.
```

For objects `E_alpha` and `E_beta`, determinant lines obey the
first-principles factorisation

```tex
D_{E_alpha direct-sum E_beta}
 =
D_{E_alpha}
otimes D_{E_beta}
otimes sdet RHom(E_alpha,E_beta)
otimes sdet RHom(E_beta,E_alpha).
```

CY3 duality gives

```tex
sdet RHom(E_beta,E_alpha)
  ~= sdet RHom(E_alpha,E_beta).
```

Therefore the cross-term is a square:

```tex
sdet RHom(E_alpha,E_beta)
otimes sdet RHom(E_beta,E_alpha)
 =
(sdet RHom(E_alpha,E_beta))^{\otimes 2}.
```

The square-root fusion isomorphism is

```tex
Fus_o:
O_{alpha+beta}|_{E_{alpha,beta}}
  ~=
O_alpha boxplus O_beta
otimes sdet RHom(E_alpha,E_beta).
```

This is the strong orientation datum.  It is strictly stronger than a
global square root of `K_{M,s}`: it says the root is compatible with
extensions, hence with the Hall product.

Associativity for triples `alpha,beta,gamma` is the pentagon identity
for the two ways of fusing

```tex
((alpha,beta),gamma)
\qquad\text{and}\qquad
(alpha,(beta,gamma)).
```

At the determinant-line level both sides identify with

```tex
O_alpha boxplus O_beta boxplus O_gamma
otimes sdet RHom(E_alpha,E_beta)
otimes sdet RHom(E_alpha,E_gamma)
otimes sdet RHom(E_beta,E_gamma).
```

The oracle must verify equality of the two signs.  This is the
orientation part of Hall associativity.

## Quadratic Refinement and the Quantum-Torus Sign

Let `Gamma` be the numerical charge lattice and

```tex
<alpha,beta> = chi(alpha,beta)
```

the CY3 antisymmetric Euler form.  A strong orientation induces a
quadratic refinement

```tex
q_o: Gamma -> {+-1}
```

satisfying

```tex
q_o(alpha+beta)
 =
(-1)^{<alpha,beta>} q_o(alpha) q_o(beta).
```

Changing orientation by a flat `Z/2` line multiplies `q_o` by a
character

```tex
ell: Gamma -> {+-1}.
```

Thus the orientation torsor acts on refinements by

```tex
q_o -> ell q_o.
```

The motivic quantum torus is

```tex
T^{mot}_{Gamma,o}
 =
prod_{gamma in Gamma^+}
R_mot . x_gamma
```

with product

```tex
x_alpha x_beta
 =
L^{<alpha,beta>/2}
epsilon_o(alpha,beta)
x_{alpha+beta}.
```

The sign `epsilon_o` is computed from the chosen refinement.  In a basis
`e_1,...,e_r`, choose the upper-triangular representative

```tex
q_o(sum_i d_i e_i)
 =
(-1)^{sum_{i<j} b_ij d_i d_j},
\qquad
b_ij = <e_i,e_j> mod 2.
```

Then

```tex
q_o(d+e) q_o(d)^{-1} q_o(e)^{-1}
 =
(-1)^{<d,e>}.
```

This is the finite arithmetic test for orientation signs in every
charge truncation.

## Quotient-Stack Critical Charts

For a quiver with potential `(Q,W)` and dimension vector `d`, set

```tex
V_d = Rep(Q,d),
\qquad
G_d = prod_{i in Q_0} GL(d_i),
\qquad
Y_d = [V_d/G_d].
```

The critical moduli chart is

```tex
M_d = [Crit(Tr W_d)/G_d] subset Y_d.
```

The smooth quotient stack has canonical line

```tex
K_{Y_d}
 =
det(V_d^*) otimes det(g_d).
```

Since `det(g_d)` is trivial for the adjoint action of a product of
general linear groups, the computable character is the character of
`det(V_d^*)`.  For an arrow `a:i -> j`, the representation
`Hom(C^{d_i},C^{d_j}) = C^{d_j} otimes (C^{d_i})^*` contributes

```tex
det(Hom(C^{d_i},C^{d_j})^*)
 =
(det_i)^{d_j} (det_j)^{-d_i}.
```

Therefore the vertex-character vector of `K_{Y_d}` is

```tex
k_i(d)
 =
sum_{a:i -> j} d_j
 -
sum_{a:h -> i} d_h.
```

The d-critical canonical line on `M_d` is

```tex
K_{M_d,s} = K_{Y_d}^{\otimes 2}|_{M_d}.
```

The canonical chart root is

```tex
O_d = K_{Y_d}|_{M_d}.
```

This is why toric quiver charts have no orientation obstruction at the
single-chart level: the root is already present before imposing the
critical equation.  The nontrivial test is not existence of `O_d`; it is
whether `O_d` is transported compatibly under direct sums, extensions,
and chart changes.

## Computed Toric Protocol

The following exact finite tests were run in this worker pass on the
standard quiver charts for `C^3`, the conifold, and local `P^2`.

### Input quivers

```tex
C^3:
Q_0={0},
Q_1={0->0,0->0,0->0}.
```

```tex
conifold:
Q_0={0,1},
Q_1={0->1,0->1,1->0,1->0}.
```

```tex
local P^2:
Q_0={0,1,2},
Q_1={0->1 three times, 1->2 three times, 2->0 three times}.
```

### Test A: canonical-character additivity

For every tested pair of dimension vectors `d,e` with entries `<=2`,
the oracle checks

```tex
k(d+e)=k(d)+k(e).
```

This verifies that quotient-stack orientation roots tensor correctly
under direct sum at the character level.

Results:

```tex
C^3:       k(d)=0.
conifold:  k(d_0,d_1)=(0,0).
local P^2:
  k(d_0,d_1,d_2)
   =
  (3(d_1-d_2), 3(d_2-d_0), 3(d_0-d_1)).
```

The local `P^2` root is generally nontrivial as a `G_d`-character.
That is not a failure.  The root is the character line `K_{Y_d}` itself.
The false simplification would be to replace it by the trivial line.

### Test B: Cech obstruction on global quiver charts

Each of the three quiver models above is a single global critical chart
on the chosen representation stack.  Hence the Cech nerve has no
nontrivial triple-overlap obstruction:

```tex
ob_2(C^3)=0,
\qquad
ob_2(conifold)=0,
\qquad
ob_2(local P^2)=0
```

at the quiver-chart level.

This statement is local to the quiver critical chart.  It does not claim
that every compact CY3 moduli stack admits one global critical function.
The compact case is solved by the atlas Cech algorithm below.

### Test C: quadratic-refinement identity

Let

```tex
<d,e>
 =
sum_{a:i->j} (d_i e_j - d_j e_i).
```

For all dimension vectors with entries `<=2`, the oracle checks

```tex
q(d+e)=q(d)q(e)(-1)^{<d,e>}.
```

Results:

```tex
C^3:
  <d,e>=0,
  q(d)=1.
```

```tex
conifold:
  <d,e>=0,
  q(d_0,d_1)=1.
```

```tex
local P^2:
  <d,e>
   =
  3(d_0 e_1+d_1 e_2+d_2 e_0
    -d_1 e_0-d_2 e_1-d_0 e_2),
```

and the upper-triangular refinement is

```tex
q(d_0,d_1,d_2)
 =
(-1)^{d_0 d_1+d_0 d_2+d_1 d_2}.
```

The tested values include

```tex
q(1,0,0)=q(0,1,0)=q(0,0,1)=1,
```

and

```tex
q(1,1,0)=q(1,0,1)=q(0,1,1)=q(1,1,1)=-1.
```

These signs are the orientation-theoretic input to the local `P^2`
motivic quantum torus.

## Compact-Chart Oracle

For compact CY3 moduli there is usually no global quiver chart.  The
oracle uses the d-critical atlas.

### Input

For each charge `gamma` in a finite HN truncation, provide:

```tex
M_gamma^red = union_i R_{gamma,i},
R_{gamma,i} -> Crit(f_{gamma,i}: U_{gamma,i} -> A^1),
```

with smooth `U_{gamma,i}`, transition data on overlaps, and extension
correspondences

```tex
M_alpha x M_beta <- E_{alpha,beta} -> M_{alpha+beta}.
```

### Step 1: local determinant roots

Compute

```tex
O_{gamma,i}=K_{U_{gamma,i}}|_{R_{gamma,i}}.
```

Equivalently, if a universal family `E_univ` exists on the chart, compute

```tex
O_{gamma,i}
 =
det Ext^0(E_univ,E_univ)
otimes det Ext^1(E_univ,E_univ)^{-1}.
```

The equality follows from CY3 Serre duality.

### Step 2: square-root transports

On overlaps `R_{gamma,ij}`, compute the determinant of the coordinate
change between Darboux charts:

```tex
J_{ij} = det(d phi_{ij})
```

in the line

```tex
Hom(O_{gamma,i},O_{gamma,j}).
```

Choose `theta_{ij}` with

```tex
theta_{ij}^{\otimes 2}
 =
J_{ij}^{\otimes 2}.
```

The ambiguity is a sign.

### Step 3: Cech obstruction

On triple overlaps compute

```tex
c_{ijk}=theta_{ki} theta_{jk} theta_{ij} in {+-1}.
```

Encode signs as elements of `F_2`; `-1` is `1`, `+1` is `0`.  Then solve

```tex
delta lambda = c
```

over `F_2`.

If solvable, glue an honest orientation line.  If not, record the class
`[c]` and continue in the `[c]`-twisted orientation gerbe.

### Step 4: orientation local systems

For each connected component of each overlap, record the local system

```tex
L_{ij}=Isom_{sqrt}(O_i,O_j).
```

The oriented vanishing cycles are transported by

```tex
T_ij:
phi_{f_i} tensor L_{o_i}
  ->
phi_{f_j} tensor L_{o_j}.
```

The oracle verifies

```tex
T_ki T_jk T_ij = 1
```

after trivialisation, or equals the gerbe action if `[c]` is retained.

### Step 5: Thom--Sebastiani squares

For every pair of charts in charges `alpha,beta`, verify the square

```tex
(T_i i' boxplus T_j j') circ TS_o
 =
TS_o circ T_(i,j),(i',j')
```

on

```tex
R_{alpha,i} x R_{beta,j}.
```

This is an equality of maps of perverse sheaves, mixed Hodge modules, or
motivic vanishing-cycle objects, depending on the coefficient target.

### Step 6: Hall-fusion squares

On the extension correspondence, verify

```tex
O_{alpha+beta}
 =
O_alpha boxplus O_beta
otimes sdet RHom(E_alpha,E_beta).
```

The quotient of the two sides is a `Z/2` local system.  The oracle
requires it to be trivialised, or else records the corresponding
fusion-gerbe twist.

### Step 7: associativity pentagon

For triples `alpha,beta,gamma`, compare the two composite
trivialisations over the stack of two-step filtrations.  The target line
on both sides is

```tex
O_alpha boxplus O_beta boxplus O_gamma
otimes sdet RHom(E_alpha,E_beta)
otimes sdet RHom(E_alpha,E_gamma)
otimes sdet RHom(E_beta,E_gamma).
```

The sign difference is a `3`-cochain.  The strong-orientation condition
is that this cochain is zero.  If not zero, the healed output is a
higher gerbe-twisted Hall object; no untwisted CoHA is claimed.

### Step 8: quadratic refinement

On the numerical lattice, compute the mod-`2` Euler matrix

```tex
B_ij = <e_i,e_j> mod 2.
```

Set

```tex
q_o(sum_i d_i e_i)
 =
(-1)^{sum_{i<j} B_ij d_i d_j}
```

and compare it with the monodromy of the orientation line obtained from
Steps 1--7.  Agreement is the finite charge-level confirmation that the
orientation data produces the quantum-torus sign used by motivic
wall-crossing.

## The Strong Target Theorem

The correct theorem is not merely orientability.  It is the following
strong-orientation theorem.

Let `M_C` be the derived moduli stack of objects in a locally geometric
3CY category.  Suppose:

```tex
H0.  M_C has a d-critical Darboux atlas on every finite charge truncation.
H1.  The Cech obstruction ob_2(M_C,s) is trivialised, or retained as a
     fixed orientation-gerbe twist.
H2.  The oriented vanishing-cycle coefficients glue under the overlap
     transports T_ij.
H3.  Thom--Sebastiani is compatible with these transports.
H4.  The determinant roots satisfy Hall-fusion compatibility along
     extension correspondences.
H5.  The triple-extension associativity pentagon commutes.
H6.  The induced quadratic refinement q_o agrees with the motivic
     quantum-torus sign convention.
```

Then the sector-completed motivic Hall object

```tex
H^{mot}_{sigma,S,o,T_eq}
 =
widehat{direct sum}_{gamma in Gamma^{ss}_{sigma,S}}
R Gamma^{BM}_{T_eq}
(
  M_sigma^A(gamma),
  Phi^{vc}_{gamma,o}
)
```

is an associative oriented motivic Hall algebra.  Its integration map
lands in the completed oriented motivic quantum torus

```tex
x_alpha x_beta
 =
L^{<alpha,beta>/2}
epsilon_o(alpha,beta)
x_{alpha+beta}.
```

The same statement holds in the gerbe-twisted target if `H1` is retained
as a nonzero twist.  Under the canonical strong-orientation theorem for
smooth proper CY3 categories, the gerbe twist is canonically killed and
the untwisted Hall algebra is obtained.

This theorem is monotone relative to all weaker versions:

```tex
square root
  < oriented vanishing cycles
  < Thom--Sebastiani oriented vanishing cycles
  < strong Hall-fusion orientation
  < associative oriented motivic Hall algebra
  < oriented BPS positive geometry.
```

## Failure Modes Healed Into Stronger Data

### Failure 1: a local root is mistaken for a global orientation

Local Darboux charts always supply `K_U`, but different `K_U` may glue
with triple-overlap sign defect.  The healed data are:

```tex
c_o in Cech^2(Z/2),
\qquad
[c_o] in H^2(M^red,Z/2).
```

The orientation oracle computes the obstruction instead of suppressing
it.

### Failure 2: a numerical Behrend sign is used as orientation data

The Behrend sign is an Euler-specialized trace of vanishing cycles.  It
does not remember the square-root gerbe, monodromy, mixed Hodge
structure, or Thom--Sebastiani transport.  The healed data are:

```tex
Phi^{vc}_{gamma,o}
```

before applying Euler characteristic.

### Failure 3: quotient-stack orientation is trivialised by force

For local `P^2`, the quotient-stack canonical root has nontrivial
character

```tex
(3(d_1-d_2), 3(d_2-d_0), 3(d_0-d_1)).
```

The healed statement keeps `K_{[Rep/G]}` as the root.  Triviality is not
required; existence and fusion compatibility are required.

### Failure 4: Thom--Sebastiani is used without signs

The vanishing-cycle tensor product becomes Hall multiplication only
after orientation local systems are transported through
Thom--Sebastiani.  The healed data are the commuting `TS_o` squares.

### Failure 5: direct-sum compatibility is mistaken for extension
compatibility

Direct sum sees only the product chart.  Hall multiplication sees
extensions.  The healed data are

```tex
Fus_o:
O_{alpha+beta}
 =
O_alpha boxplus O_beta
otimes sdet RHom(E_alpha,E_beta)
```

plus the triple-extension pentagon.

### Failure 6: compact CY3 charts are forced into toric form

Compact CY3 moduli generally require an atlas, not one global potential.
The healed data are the Cech orientation algorithm and the KPS/CY3
strong-orientation input where applicable.

### Failure 7: a nonzero obstruction is treated as failure of the theory

The healed target is gerbe-twisted positive geometry.  A nonzero
orientation class changes the coefficient system and quantum torus; it
does not erase the BPS geometry.

## Interface With the Chambered Positive Geometry

The orientation oracle plugs into the master object as follows:

```tex
P^{BPS,motloc}_{sigma,S,o,T_eq}(X)
 =
(
  StabSite(C),
  Sect_sigma(C),
  M_C^{(-1)-symp},
  A^{or}_{crit},
  Phi^{vc}_{A,o},
  H^{mot}_{sigma,S,o,T_eq},
  mu_Hall^{mot},
  Fil^{HN}_{sigma,S},
  Int^{mot},
  Real
).
```

Worker 02 supplies

```tex
A^{or}_{crit},
\qquad
Phi^{vc}_{A,o},
\qquad
epsilon_o,
\qquad
q_o.
```

The old combinatorial positive cone is recovered only after applying
realisation:

```tex
oriented motivic Hall object
  -> motivic quantum torus
  -> Euler-specialized quantum torus
  -> numerical BPS support
  -> completion monoid Gamma^+.
```

Thus orientation precedes positivity.  It is not decoration on an
already-defined cone.

## Compute-Oriented Pseudocode

The finite truncation oracle is:

```text
input:
  charge basis Gamma_N
  d-critical chart cover {R_i -> Crit(f_i:U_i)}
  overlap coordinate changes phi_ij
  extension correspondences E_{alpha,beta}
  Euler matrix B=(<e_i,e_j>)

for each chart i:
  O_i := K_{U_i}|_{R_i}
  Phi_i := vanishing_cycles(f_i) tensor orientation_line(O_i)

for each overlap ij:
  theta_ij := chosen square-root determinant transport
  T_ij := vanishing-cycle comparison tensor theta_ij

for each triple ijk:
  c_ijk := theta_ki * theta_jk * theta_ij in F_2

solve delta lambda = c over F_2
if solvable:
  theta_ij := lambda_ij^{-1} theta_ij
  orientation_status := honest
else:
  orientation_status := gerbe_twisted
  record [c] in H^2(M^red,Z/2)

for each product chart pair:
  verify TS_o square

for each extension correspondence E_{alpha,beta}:
  verify O_{alpha+beta}
    = O_alpha boxplus O_beta tensor sdet RHom(E_alpha,E_beta)

for each triple alpha,beta,gamma:
  verify Hall-fusion pentagon

construct q_o(d)=(-1)^{sum_{i<j} (B_ij mod 2)d_i d_j}
verify q_o(d+e)=q_o(d)q_o(e)(-1)^{<d,e>}

output:
  orientation local systems
  Cech obstruction
  TS transports
  Hall-fusion signs
  quadratic refinement
  oriented or gerbe-twisted motivic Hall coefficient system
```

## Computational Checks Run

The worker ran a direct exact-arithmetic Python check of the quotient
character and quadratic-refinement identities for `C^3`, conifold, and
local `P^2`, with all dimension-vector entries `<=2`.

Results:

```text
C3
  K character samples: [(0,)] ... total 1
  Kchar additive through dimension 2: True
  quadratic refinement identity through dimension 2: True
  q samples: {(0,): 1, (1,): 1, (2,): 1}

conifold
  K character samples: [(0, 0)] ... total 1
  Kchar additive through dimension 2: True
  quadratic refinement identity through dimension 2: True
  q samples:
    {(0,0):1,(0,1):1,(0,2):1,
     (1,0):1,(1,1):1,(1,2):1,
     (2,0):1,(2,1):1,(2,2):1}

local_P2
  K character samples include:
    (-6,0,6), (-6,3,3), (-6,6,0),
    (-3,-3,6), (-3,0,3), (-3,3,0)
  total distinct character vectors through dimension 2: 19
  Kchar additive through dimension 2: True
  quadratic refinement identity through dimension 2: True
  q basis/pairs:
    (1,0,0): 1
    (0,1,0): 1
    (0,0,1): 1
    (1,1,0): -1
    (1,0,1): -1
    (0,1,1): -1
    (1,1,1): -1
```

These checks do not prove compact orientability.  They prove the exact
orientation formulas on the three standard critical quiver charts and
give the finite arithmetic oracle that compact chart computations must
generalise.

## Source Anchors

Local anchors read in this pass:

- `CLAUDE.md`, Vol III orientation and positive-geometry grammar.
- `notes/master_synthesis_chambered_bps_positive_geometry_20260424.md`,
  motivic-homotopical localization and quiver critical chart theorem.
- `chapters/examples/k3_chiral_bialgebra_platonic.tex`, Joyce--KPS
  vertex-algebra orientation discussion around the smooth projective
  CY3 moduli stack.
- `chapters/examples/k3e_cy3_programme.tex`, motivic DT lift,
  orientation-gerbe remarks, and Igusa/BKM boundary.
- `notes/adversarial_bps_positive_geometry_20260424/agent_13_compute_oracles.md`,
  toric chart and conifold/local `P^2` compute surface.

Primary literature anchors used for the theorem spine:

- Pantev--Toen--Vaquie--Vezzosi, shifted symplectic structures and
  the `(-1)`-shifted symplectic form on moduli of perfect complexes.
- Joyce, d-critical loci and d-critical canonical line.
- Brav--Bussi--Joyce and Ben-Bassat--Brav--Bussi--Joyce, Darboux
  charts, perverse sheaves, and motives for oriented d-critical stacks.
- Kontsevich--Soibelman, orientation data and motivic Donaldson--Thomas
  integration.
- Cao--Gross--Joyce, canonical orientation data for moduli of coherent
  sheaves on Calabi--Yau threefolds.
- Kinjo--Park--Safronov, cohomological Hall algebras for `3`-CY
  categories with strong orientation data.
- Davison--Meinhardt, cohomological DT theory and integrality.

## Final Worker 02 Output

The orientation oracle is the following upgrade:

```tex
Or_C:
(-1)-shifted CY3 critical atlas
  ->
(
  determinant square-root gerbe,
  Cech obstruction class,
  orientation local systems,
  vanishing-cycle transports,
  Thom--Sebastiani coherence,
  Hall-fusion coherence,
  quadratic refinement,
  oriented or gerbe-twisted motivic Hall coefficients
).
```

For `C^3`, conifold, and local `P^2`, the global quiver chart gives
`ob_2=0`; the quotient-stack canonical root is explicit; the quadratic
refinement is trivial for `C^3` and the conifold and is

```tex
q(d_0,d_1,d_2)
 =
(-1)^{d_0d_1+d_0d_2+d_1d_2}
```

for local `P^2`.

For compact CY3 charts, the oracle is a finite Cech and Hall-fusion
linear-algebra problem over `F_2` on every charge truncation, with a
source-theorem trivialisation when canonical strong orientation data is
available.  If the obstruction is not trivial in a future example, the
positive geometry is not downgraded; it is upgraded to the corresponding
gerbe-twisted oriented motivic positive geometry.
