# Worker 10: Compact Examples and Falsification Protocol

Date: 2026-04-24.

Owned file:
`notes/bps_positive_geometry_total_resolution_20260424/agent_10_compact_examples_and_falsification.md`.

Task.  Develop the compact and non-toric example strategy for
`P^{BPS,motloc}` and the falsification protocol for proposed examples:
the quintic, `K3 x E`, Borcea-Voisin and CHL rows, banana/Schoen, and
local-to-compact shadows.

Rule.  No theorem is weakened.  If an advertised example lacks an input,
the result is strengthened into an exact certificate theorem plus an
exact no-go lemma for the shortcut.

## 1. The Example Certificate

An example of chambered BPS positive geometry is not a name of a
Calabi-Yau threefold.  It is a realized input package

```tex
ExCert(X;sigma,S,o,T_eq)
 =
 (C_X,
  Gamma_X,
  < , >_X,
  sigma,
  Q,
  S,
  o,
  A^{or}_{crit},
  Mot,
  T_eq,
  HN_{fin},
  Int^{mot},
  Real,
  Boundary)
```

with the following meanings.

`C_X` is the `3`-Calabi-Yau category, usually `Perf(X)` or the
compactly supported subcategory in a local model.  `Gamma_X` is the
numerical charge lattice.  `< , >_X` is the skew Euler form.  `sigma`
is a stability condition or a named weak/polynomial stability structure
whose Hall theory is actually constructed.  `Q` is the support-property
quadratic form.  `S` is a strict active-ray-free sector.  `o` is strong
orientation data or a gerbe-twisted orientation output by the
orientation oracle.  `A^{or}_{crit}` is an oriented derived critical
atlas.  `Mot` is an admissible motivic or homotopical coefficient
target.  `T_eq` is the equivariance group preserving all the data.
`HN_{fin}` is finite Harder-Narasimhan control in every charge and mass
truncation.  `Int^{mot}` is motivic Kontsevich-Soibelman integration.
`Real` is the realization tower to Hodge, Euler, and numerical
invariants.  `Boundary` is optional: toric, theta, double, or
automorphic boundary data.

### Certification Theorem

If `ExCert(X;sigma,S,o,T_eq)` is supplied, then the compact or local
example realizes

```tex
P^{BPS,motloc}_{sigma,S,o,T_eq}(X)
```

and its decategorified chambered positive geometry

```tex
Dec(P^{BPS,motloc}_{sigma,S,o,T_eq}(X))
 =
P^{BPS,bullet}_{sigma,S,o,T_eq}(X).
```

The proof is formal from Workers 00--05: the certificate is precisely
the list of hypotheses needed for the foundational axioms, compact CY3
construction, orientation oracle, sector descent, realization
compatibility, and hCS-to-Hall comparison.

### Falsification Theorem

A proposed example fails exactly at the first missing item in
`ExCert`.  The failure does not weaken `P^{BPS,motloc}`.  It proves a
stronger statement:

```tex
not ExCert_i(X)  =>  no theorem of the claimed type can be true.
```

The missing input is then promoted to a theorem target.  Thus a failed
quintic Bridgeland chamber is not a downgraded quintic theorem; it is
the exact target

```tex
construct (sigma,Q,HN_{fin}) on Perf(X_5)
```

and a no-go for every proof that silently assumes it.

## 2. Universal Finite Falsifiers

Every compact or local-to-compact example must pass the same finite
tests before the full object is asserted.

### F0. Input Realization

For each finite truncation

```tex
Gamma_{<=N,<=R}
 =
{ gamma : ||gamma|| <= N, |Z(gamma)| <= R, Q(gamma) >= 0 },
```

verify:

```tex
finite active charges,
finite HN decompositions,
finite-type semistable stacks,
finite-type Hall extension stacks.
```

Failure falsifies the chamber, not the theory.

### F1. Orientation

Choose a finite d-critical atlas.  Compute the triple-overlap class

```tex
[c_o] in Cech^2(M^{red}_{<=N,<=R}, Z/2).
```

If `[c_o]=0`, the truncation is honestly oriented.  If not, the
stronger gerbe-twisted coefficient system must be used.  A calculation
with un-twisted vanishing cycles is then invalid.

### F2. Hall Pull-Push

For every pair of charges in the truncation, the correspondence

```tex
M(alpha) x M(beta) <- E(alpha,beta) -> M(alpha+beta)
```

must admit the pull-push operation in the chosen coefficient theory.
Associativity is tested on triples.  A missing properness or
Borel-Moore admissibility hypothesis falsifies the Hall algebra claim.

### F3. HN Descent

For every ordered sector cover

```tex
S=S_1 star ... star S_r
```

verify that the HN multiplication map identifies the completed sector
object with the completed ordered tensor product.  The conifold
pentagon is the minimal nontrivial model; compact examples must pass
the same identity in every finite truncation.

### F4. Realization

The diagram

```tex
Motivic Hall
  -> MHM / l-adic / motive realization
  -> K_0(MMHS)[L^{+-1/2}]
  -> motivic quantum torus
  -> Euler torus
  -> numerical Omega
```

must commute with Hall products, orientation signs, Tate twists,
sector completions, and KS wall transport.

### F5. Boundary Normalization

If an automorphic boundary is claimed, the certificate includes:

```tex
Jacobi seed phi,
constant term c(0),
weight c(0)/2,
product chamber Gamma_eff,
Weyl vector rho,
character or multiplier,
divisor,
charge-to-root map alpha,
normalization constant.
```

No scalar partition function alone supplies these data.

### F6. Local-to-Compact Gluing

Local quiver or dimer evidence becomes compact evidence only after a
gluing map is constructed:

```tex
local critical Hall charts
  -> compact derived critical stack
  -> compatible orientations
  -> compatible HN filtrations
  -> compatible motivic integration.
```

Without this map, the local model is a shadow, not the compact example.

## 3. The Quintic

Let

```tex
X_5 = {x_0^5+...+x_4^5=0} subset P^4
```

or a smooth quintic deformation.  The constructed input surface is:

```tex
C_X = Perf(X_5),
h^{1,1}(X_5)=1,
h^{2,1}(X_5)=101,
chi_{top}(X_5)=-200,
b_3(X_5)=204,
chi(O_{X_5})=0.
```

The local manuscript already records the Hochschild data and the
curved-formality obstruction:

```tex
HH^1(X_5)=0,
dim HH^2(X_5)=101,
dim HH^3(X_5)=4,
Y_3(X_5)=int_{X_5} H^3 = 5.
```

The equality `Y_3=5` is the first compact non-toric falsifier.  A
strict Kontsevich-formality proof for the quintic would force the
transferred cubic operation to vanish on cohomology; the large-volume
Yukawa coupling is nonzero.  Therefore the quintic cannot be realized
by a strict toric-style global quiver chart or by a formal affine
Calabi-Yau replacement.

### Quintic Certificate Ledger

Constructed:

```tex
Perf(X_5) as a proper CY3 category,
Gamma_{X_5}=K_0^{num}(X_5),
skew Euler form by Serre duality,
PTVV (-1)-shifted moduli stack of perfect complexes,
Brav-Bussi-Joyce local d-critical charts,
Joyce-Upmeier orientation data when the strong orientation theorem applies,
BCOV/hCS perturbative field theory,
Hodge and LG numerical tests.
```

Must be supplied for full `P^{BPS,motloc}`:

```tex
Bridgeland sigma on Perf(X_5),
support property Q,
strict sector S with active boundary avoidance,
finite HN-sector control,
finite-type semistable and extension stacks in the chosen sector,
explicit motivic coefficient target with vanishing cycles,
motivic integration to the completed quantum torus,
hCS-to-Hall calibration Theta^{or}_{hCS->Hall} on compact charts,
finite BPS seed oracle.
```

### Quintic Theorem Target

The correct strengthened theorem is:

```tex
If (sigma,Q,S,o,A^{or}_{crit},Mot,T_eq,HN_{fin})
is constructed for Perf(X_5), then
P^{BPS,motloc}_{sigma,S,o,T_eq}(X_5)
exists canonically from the data.
```

This is stronger than claiming a bare quintic positive cone.  It
specifies the exact data whose existence turns the quintic into a
realized compact non-toric example.

### Quintic No-Go Lemmas

1. **No toric terminal collapse.**  Since `Y_3(X_5)=5`, the quintic is
   not represented by a strict formal affine Calabi-Yau quiver chart
   whose transferred higher operations vanish.

2. **No automatic automorphic BKM boundary from the BCOV scalar.**  The
   BCOV scalar shadow `chi_{top}(X_5)/24=-25/3` is not a positive
   integral Borcherds weight.  Hence it cannot be the weight of a
   holomorphic BKM denominator.  Any automorphic boundary for the
   quintic must be built from a new seed and a new product chamber, not
   from this scalar.

3. **No theta basis without scattering data.**  A mirror/LG
   description of the quintic supplies finite-dimensional LG checks, not
   a broken-line or GMN theta basis for the compact BPS Hall object.

### Quintic Finite Checks

The existing compute surface gives the first finite witnesses:

```tex
h^{1,1}=1,
h^{2,1}=101,
chi_{top}=-200,
b_3=204,
dim Jac(W)^{Z/5Z}=204,
Y_3=5,
BCOV scalar = -25/3.
```

The falsification target is:

```tex
For every proposed sigma and sector S,
compute P^{BPS,motloc}_{<=N,<=R}(X_5)
and test F0--F4.
```

Disagreement at finite `(N,R)` falsifies the proposed chamber.  It does
not falsify the existence theorem from the completed certificate.

## 4. `K3 x E`

The product

```tex
X=S x E
```

with `S` a K3 surface and `E` an elliptic curve is the first compact
non-toric example whose automorphic boundary is theorem-grade.

The Igusa manuscript supplies:

```tex
Z_K3 = 2 phi_{0,1},
phi_{0,1} = sum f(n,l) q^n r^l,
f(0,0)=10,
wt(Borch(phi_{0,1}))=5,
mathcal D_X = Delta_5,
Delta_10 = Delta_5^2,
Z^{OP}_{S x E} = -4096 Delta_5^{-2},
den(g_{Delta_5}) = 64^{-1} Delta_5(2Z).
```

The BPS charge lattice in the boundary is

```tex
Gamma_BPS = Z^3,
gamma=(n,l,m),
<gamma,gamma'>_BPS = 2(nm'+n'm)-ll',
Gamma_eff = lexicographic cusp chamber.
```

The Lorentzian root map is

```tex
alpha(n,l,m)=2n f_2 - l f_3 + 2m f_{-2},
(alpha(gamma),alpha(gamma'))=-2<gamma,gamma'>_BPS.
```

The orientation character visible at the boundary is the Maass
character:

```tex
epsilon_det = nu_{Delta_5}.
```

### `K3 x E` Certificate Ledger

Constructed:

```tex
Perf(K3 x E) as a product CY3 category,
PTVV shifted moduli and d-critical charts,
product orientation source,
reduced OP primitive curve-counting scalar square,
Borcherds-Gritsenko-Nikulin product Delta_5,
Lorentzian denominator root lattice,
effective cusp chamber Gamma_eff,
normalization ledger D_5, mathcal D_X, den(g_{Delta_5}).
```

Must be supplied for full `P^{BPS,motloc}`:

```tex
Bridgeland or reduced stability chamber on the full category,
finite HN control in the reduced/equivariant sector,
orientation comparison o -> nu_{Delta_5},
critical Hall construction whose primitive realization is phi_{0,1},
Hall-to-BKM positive-half map,
Cartan/negative/pairing data for the double,
compatibility of reduced E-quotient DT theory with motivic Hall integration.
```

### `K3 x E` Theorem Targets

**Boundary theorem target.**

```tex
If the primitive reduced motivic BPS seed of P^{BPS,motloc}(K3 x E)
realizes phi_{0,1}, and if the orientation realization equals
nu_{Delta_5}, then
AutBorch(P^{BPS,motloc}(K3 x E)) = Delta_5.
```

**Positive-half theorem target.**

```tex
CoHA^{or}_{crit,red}(K3 x E)
  -> U(n_+(g_{Delta_5}))
```

must preserve charge grading, superdimension

```tex
sdim g_{alpha(n,l,m)} = f(nm,l),
```

and the Weyl chamber.

### `K3 x E` No-Go Lemmas

1. **No toric fan.**  The chamber is Lorentzian and automorphic.  It is
   not a rational polyhedral toric fan.

2. **No direct Yangian.**  The BKM-side object is the Hall-Drinfeld
   double or denominator closure.  It is not a Drinfeld Yangian of
   `g_{Delta_5}`.

3. **No scalar-root confusion.**  `Delta_5` is the chiral determinant.
   The full scalar protected square is governed by `Delta_5^{-2}`.

4. **No normalization collapse.**  The three objects

   ```tex
   D_5=64^{-1}Delta_5,
   mathcal D_X=Delta_5,
   den(g_{Delta_5})=D_5(2Z)
   ```

   have different normalizations and different roles.

5. **No additive weight formula.**  The BKM weight is

   ```tex
   wt(Delta_5)=c_1(0)/2=5.
   ```

   It is not obtained by adding a chiral scalar to a fibre Euler
   characteristic.

### `K3 x E` Finite Checks

Every proposed Hall-to-Igusa bridge must reproduce:

```tex
phi_{0,1}|_{q^0}=r^{-1}+10+r,
f(0,0)/2=5,
[q^{1/2}r^{1/2}s^{1/2}] Delta_5=64,
Delta_10=Delta_5^2,
Z^{OP}_{S x E}=-4096 Delta_5^{-2},
den(g_{Delta_5})=64^{-1}Delta_5(2Z),
nu_{Delta_5}(s_{delta_i})=-1,
div(Delta_5)=Sp_4(Z).H_diag with multiplicity 1.
```

Failure of any line falsifies the proposed normalization.

## 5. CHL and Borcea-Voisin Rows

The CHL/Borcea-Voisin layer is not a list of modular forms.  It is a
row-certificate problem.

For a row `j`, define

```tex
RowCert_j =
(X_j,G_j,sigma_j,S_j,o_j,
 phi_j,F_j,Gamma_j^+,rho_j,nu_j,L_j,alpha_j,
 Z^{red}_j).
```

Here `X_j` is the compact or orbifold Calabi-Yau host, `G_j` is the
finite symmetry group, `phi_j` is the Jacobi seed, `F_j` is the
automorphic product, `Gamma_j^+` is the product chamber, `rho_j` is the
Weyl vector, `nu_j` is the character or multiplier, `L_j` is the
Lorentzian lattice, `alpha_j` is the charge-to-root map, and
`Z^{red}_j` is the reduced scalar branch.

### Row Certification Theorem

If `RowCert_j` is supplied and the quotient/orbifold Hall theory has
orientation and finite HN control, then the row realizes an automorphic
boundary:

```tex
AutBorch_j(P^{BPS,motloc}(X_j/G_j))=F_j,
\qquad
Z^{red}_j=C_j F_j^{-2}
```

on the chosen scalar-square branch.

This theorem is stronger than saying "the row exists": it states all
data needed for a physical BPS positive geometry and separates them from
the automorphic classification.

### Constructed Row Data

The automorphic source material contains:

```tex
Gritsenko-Clery eight diagonal-divisor forms F_j,
their weights,
their divisor H_diag of multiplicity 1,
their characters or multiplier systems,
their Borcherds product inputs in the constructed rows.
```

The CHL ladder at elliptic-compatible orders has:

```tex
N in {1,2,3,4,6},
c_N(0)=(10,8,6,4,2),
c_N(0)/2=(5,4,3,2,1).
```

The `N=1` row is the theorem-grade `K3 x E` row:

```tex
F_1=Delta_5.
```

### Row Inputs Still Required

For each row beyond `N=1`, the following must be supplied before
claiming a compact BPS positive geometry:

```tex
Calabi-Yau host X_j or orbifold stack [X_j/G_j],
crepant resolution or stack-theoretic replacement,
derived moduli of objects on the quotient,
orientation descent across inertia sectors,
stability condition and support property,
HN finite sector control,
reduced/equivariant Hall integration,
charge-to-root map alpha_j,
identity between primitive BPS seed and the Jacobi input phi_j,
normalization of the scalar-square branch.
```

### CHL/Borcea-Voisin No-Go Lemmas

1. **Gritsenko-Clery is not CHL realization.**  The eight
   diagonal-divisor forms are automorphic source data.  A row becomes a
   BPS positive geometry only after `RowCert_j` is built.

2. **Orders `5,7,8` are not diagonal `K3 x E` CHL CY3 quotients.**  A
   complex elliptic curve fixing the origin has automorphism orders only

   ```tex
   {1,2,3,4,6}.
   ```

   Thus rows requiring orders `5,7,8` cannot be realized by the same
   free diagonal `K3 x E` quotient construction.

3. **Borcea-Voisin involution is not the whole CHL ladder.**  The
   Borcea-Voisin construction gives a powerful order-`2` compact
   quotient template.  Higher CHL rows require their own quotient,
   inertia, and reduced DT certificates.

4. **Half-integral and degenerate rows require multiplier control.**
   A half-integral, quarter-integral, or weight-zero boundary row cannot
   be imported into the motivic Hall theory unless the cover/multiplier
   system is identified with orientation and equivariant descent data.

5. **No row without a seed.**  A modular form `F_j` with the correct
   divisor is not enough.  The BPS theory needs the primitive Jacobi
   seed whose coefficients become root superdimensions.

### CHL Finite Checks

Every CHL row certificate must pass:

```tex
constant term c_N(0),
weight c_N(0)/2,
character order,
first product coefficients,
divisor multiplicity along H_diag,
orbifold Lefschetz trace or frame-shape check,
orientation character/multiplier comparison,
scalar-square normalization.
```

The finite check at `N=1` is the Igusa normalization ledger of the
previous section.  For `N>1`, any mismatch in weight, character,
divisor, or seed coefficient falsifies the claimed row certificate.

## 6. Banana, Schoen, and Local-to-Compact Shadows

The banana case is the cleanest warning that vanishing scalar shadows do
not imply trivial positive geometry.

There are two related but distinct inputs:

```tex
local banana model:
  two compact curve classes C_1,C_2,
  local quiver/CoHA charts,
  Bryan-Kool-Young GV data,
  quasi-Jacobi/mock-modular shadow.

compact Schoen container:
  fiber product of two rational elliptic surfaces over P^1,
  h^{1,1}=h^{2,1}=19,
  chi_{top}=0.
```

The local compute surface also uses a normalized two-parameter banana
Hodge model with `h^{1,1}=h^{2,1}=2` for the local curve sector.  That
normalization is not the global Schoen Hodge diamond.  The distinction
is load-bearing.

### Banana Certificate Ledger

Constructed:

```tex
local compact-curve charge lattice Z^2,
two banana curve classes,
local quiver charts and flopped chart,
local CoHA data in the charts,
GV values such as n^0_{1,0}=n^0_{0,1}=-2,
nontrivial quartic shadow tower,
quasi-Jacobi data for the local DT function,
compact Schoen container with chi_{top}=0.
```

Must be supplied for compact `P^{BPS,motloc}`:

```tex
embedding of local banana charts into the compact derived critical stack,
global stability chamber on the compact Schoen category or a reduced sector,
HN finite control,
global orientation and chart-overlap coherence,
gluing of local CoHA charts through the compact fibration,
compatibility of local GV/DT invariants with compact motivic integration,
realization of the mock/quasi-Jacobi shadow from motivic BPS data.
```

### Banana Theorem Target

```tex
If the local banana Hall charts glue into the compact Schoen
or reduced local-to-compact derived critical stack with compatible
orientation, stability, and HN finiteness, then the resulting
P^{BPS,motloc} has a nontrivial BPS completion monoid even when
chi(O_X)=0.
```

This is stronger than a scalar statement.  It says the first nonzero
structure is not the leading scalar but the higher Hall-shadow tower.

### Banana No-Go Lemmas

1. **Scalar-zero does not imply trivial.**  `chi(O_X)=0` and
   `chi_{top}=0` do not imply a trivial BPS positive geometry.  The
   local banana GV invariants already produce nonzero higher shadow
   terms.

2. **Local evidence is not compact realization.**  A local quiver chart
   or local GV table does not construct the compact Schoen
   `P^{BPS,motloc}` unless the gluing map F6 is supplied.

3. **Compact Hodge data and local charge data are different.**  The
   global Schoen values `(19,19)` and the local two-curve banana
   truncation `(2,2)` are compatible only after the local-to-compact
   projection is named.

4. **CM pinning is falsifiable.**  A predicted Shimura lift to the
   CM-by-`Z[i]` elliptic curve at conductor `32` is not a theorem until
   the first Hecke coefficients of the completed banana shadow are
   computed.  Inert primes `p congruent 3 mod 4` must give zero
   coefficients.

### Banana Finite Checks

Existing checks to retain:

```tex
local banana Euler characteristic = 0,
local banana Betti alternating sum = 0,
n^0_{1,0}=n^0_{0,1}=-2,
n^0_{1,1}=-2,
n^0_{2,2}=-6,
n^0_{3,3}=-32,
n^1_{1,1}=-4,
n^1_{2,2}=-32,
quartic shadow S_4=-44 in the local shadow normalization,
exchange symmetry C_1 <-> C_2.
```

The next compact falsifier is:

```tex
compute local-to-compact DT coefficients through the first
20 primes of the predicted CM Shimura lift.
```

Any nonzero coefficient at an inert prime, or any forced zero at a split
prime where the CM newform is nonzero, falsifies the CM pinning.

## 7. Other Local-to-Compact Shadows

The toric and dimer examples remain indispensable, but their role is
calibration.

```tex
C^3:
  terminal one-vertex quiver degeneration,
  CoHA(C^3)=Y^+(glhat_1).

conifold:
  two-charge chamber,
  quantum pentagon wall-crossing,
  first nontrivial KS transport test.

local P^2:
  three-charge McKay chart,
  fractional chiral scalar,
  strong local critical Hall check.

SPP:
  dimer/flop chart atlas,
  mutation and Seiberg-duality finite web.

banana:
  local nontrivial shadow with compact Schoen container.
```

The local-to-compact theorem target is:

```tex
For a compact CY3 X with a local model U,
local P^{BPS,motloc}(U) maps to compact P^{BPS,motloc}(X)
only through a constructed compact-support, orientation-preserving,
HN-compatible Hall restriction/extension correspondence.
```

No local calculation is lost.  It becomes a finite chart in the compact
certificate.

## 8. Example Partial Order

The examples form an increasing difficulty order by missing input:

```tex
C^3
  -> conifold
  -> local P^2 / SPP
  -> banana local charts
  -> banana/Schoen local-to-compact
  -> K3 x E automorphic boundary
  -> CHL/Borcea-Voisin rows
  -> quintic compact non-toric chamber.
```

This is not a hierarchy of importance.  It is the order in which finite
falsifiers become harder.

`C^3`, conifold, local `P^2`, and SPP test toric terminal degeneration.
Banana tests scalar-zero but higher-shadow nontriviality.  `K3 x E`
tests automorphic Lorentzian boundary.  CHL/Borcea-Voisin rows test
orbifold and multiplier descent.  The quintic tests the fully compact
non-formal Bridgeland/Hall input.

## 9. Master Falsification Table

```tex
Claim:
  "X has P^{BPS,motloc}."
Falsifier:
  Missing ExCert input.
Heal:
  Exact construction theorem for that input.

Claim:
  "X has a toric positive cone."
Falsifier:
  Nonzero compact Yukawa, infinite wall chamber, Lorentzian chamber,
  or missing global quiver critical chart.
Heal:
  Sector-completed Hall-scattering object.

Claim:
  "X has BKM boundary."
Falsifier:
  no Jacobi seed, no integral/nonnegative weight in the correct
  automorphic line, no charge-to-root map, no denominator identity.
Heal:
  RowCert or AutBorch theorem target.

Claim:
  "local chart proves compact example."
Falsifier:
  no compact-support Hall gluing map.
Heal:
  local-to-compact Hall correspondence theorem.

Claim:
  "scalar-zero means trivial."
Falsifier:
  banana higher shadow and GV invariants.
Heal:
  higher Hall-shadow tower.

Claim:
  "Delta_5 is the full K3 x E index."
Falsifier:
  OP scalar square is Delta_5^{-2}; Delta_5 is the determinant.
Heal:
  square-root/chiral-half theorem.
```

## 10. Deliverable for the Integrator

Worker 10 supplies the compact example strategy:

```tex
Example = ExCert + finite falsifiers.
```

The strongest current atlas is:

```tex
Quintic:
  compact non-formal target;
  full object awaits Bridgeland/support/HN data;
  no-go for toric/formal/BKM shortcut.

K3 x E:
  automorphic boundary theorem-grade at Delta_5;
  full object awaits Hall-BKM positive-half construction and
  reduced motivic Hall bridge.

CHL/Borcea-Voisin:
  row-certificate programme;
  automorphic rows exist, physical BPS rows require quotient,
  orientation, seed, and reduced DT certificates.

Banana/Schoen:
  local shadow and GV data constructed;
  compact realization awaits local-to-compact Hall gluing;
  scalar-zero triviality is falsified.

Toric/local shadows:
  calibration examples and finite wall-crossing oracles;
  not substitutes for compact certificates.
```

The frontier is now executable.  To realize `P^{BPS,motloc}` for any
compact/non-toric example, supply the certificate.  To refute a proposed
example, find the first missing certificate datum or the first failed
finite check.
