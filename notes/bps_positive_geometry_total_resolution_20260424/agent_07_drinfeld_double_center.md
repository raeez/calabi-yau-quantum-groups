# Worker 07: Drinfeld Double, Hall Pairing, and `E_1` Center

Owned file:
`notes/bps_positive_geometry_total_resolution_20260424/agent_07_drinfeld_double_center.md`.

Obligation 8 is solved by replacing the slogan "double the positive
half" with a typed construction.  The positive half is the oriented
sector Hall algebra.  The quantum group is obtained only after adjoining
Cartan, constructing a Serre-dual negative half, proving a continuous
topological bialgebra structure, constructing the Hall pairing,
quotienting by its radical, and passing to the completed Drinfeld
double.  The braided object is not the positive half; it is the
categorical center of its `E_1` representation category, equivalently
the representation category of the reduced double under the hypotheses
below.

This is a monotone strengthening.  No theorem is weakened.  Every
failure mode is healed by extra structure whose absence was exactly the
obstruction.

## 1. The Double-Admissible Data

Let

```tex
P^{BPS,motloc}_{\sigma,S,o,T_{\rm eq}}(X)
```

be the localized motivic positive geometry supplied by the earlier
workers:

```tex
oriented (-1)-shifted critical moduli
  -> vanishing-cycle coefficients
  -> HN-completed motivic Hall cosheaf
  -> realization tower.
```

Write its completed sector Hall algebra as

```tex
H^+_{\sigma,S}
 =
\widehat{\bigoplus}_{\gamma\in\Gamma^+_{\sigma,S,o}}
H^+_\gamma,
\qquad
H^+_\gamma
 =
R\Gamma^{BM}_{T_{\rm eq}}
\bigl(\mathfrak M^{HN}_{\sigma,S}(\gamma),
      \Phi^{vc}_{\gamma,o}\bigr)[s(\gamma)](t(\gamma)).
```

The coefficient ring `R` is the chosen motivic or realized coefficient
ring with half Tate object `L^{1/2}` and orientation sign cocycle

```tex
\epsilon_o:\Gamma\times\Gamma\to\{\pm1\}.
```

The skew Euler form is

```tex
\langle\alpha,\beta\rangle
 =
\chi(\alpha,\beta)-\chi(\beta,\alpha).
```

The Drinfeld-double theorem requires the following stronger datum.

```tex
P^{BPS,double}_{\sigma,S,o,T_{\rm eq}}(X)
 =
(P^{BPS,motloc}_{\sigma,S,o,T_{\rm eq}}(X),
 H^+,H^0,H^-,
 \mu^\pm,\Delta^\pm,
 \langle-,-\rangle_{\Hall},
 {\rm Rad}^\pm,
 D^{red}(H^+),
 {\mathcal R}_{univ},
 {\mathcal Z}_{E_1}).
```

This datum is called **double-admissible** when conditions D0--D8 hold.

**D0. Finite truncations.**  There is a cofinal set of finite
HN/charge/radius truncations `lambda` such that every construction below
is first defined over a finite quotient

```tex
H^+_\lambda = H^+/F^{>\lambda}H^+
```

and all transition maps preserve product, coproduct, pairing, Cartan,
radical, and center actions.  The completed object is the inverse limit.

**D1. Hall product.**  The product

```tex
\mu^+_{\alpha,\beta}:H^+_\alpha\widehat\otimes H^+_\beta
  \longrightarrow H^+_{\alpha+\beta}
```

is the Borel--Moore pull-push along the extension stack, with
Thom--Sebastiani and orientation transport.  Associativity follows from
the two-Segal identity for two-step flags.

**D2. Hall coproduct.**  There is a continuous coproduct

```tex
\Delta^+:H^+\longrightarrow H^+\widehat\otimes H^+
```

whose charge component is

```tex
\Delta^+_{\alpha,\beta}:H^+_{\alpha+\beta}
  \longrightarrow H^+_\alpha\widehat\otimes H^+_\beta.
```

It is the pull-push along the same extension stack read with the opposite
variance:

```tex
\mathfrak M(\alpha)\times\mathfrak M(\beta)
  \xleftarrow{p_{12}}
\mathfrak E(\alpha,\beta)
  \xrightarrow{p_3}
\mathfrak M(\alpha+\beta).
```

The coefficient theory must supply the compact-support, equivariant, or
localized Borel--Moore functors that make this variance legal.  Green
compatibility holds:

```tex
\Delta^+(ab)=\Delta^+(a)\Delta^+(b)
```

in the braided tensor product twisted by
`L^{\langle-,-\rangle/2}\epsilon_o`.

**D3. Cartan.**  The Cartan algebra is the completed charge torus

```tex
H^0_{\sigma,S}
 =
R[[\Gamma_{\sigma,S}^{sat}]]
 =
\prod_{\eta\in\Gamma_{\sigma,S}^{sat}}R\,K_\eta,
```

with

```tex
K_\eta K_\xi = K_{\eta+\xi},\qquad
\Delta^0(K_\eta)=K_\eta\otimes K_\eta.
```

For `a in H^+_\gamma`,

```tex
K_\eta a K_\eta^{-1}
 =
L^{\langle\eta,\gamma\rangle}
\epsilon_o(\eta,\gamma)\epsilon_o(\gamma,\eta)^{-1}a.
```

The Cartan is not decoration.  It records the skew Euler form,
orientation quadratic refinement, equivariance weights, and the charge
grading on which the double is built.

**D4. Negative half.**  The negative half is the Serre--Verdier dual
Hall algebra

```tex
H^-_{-\gamma}
 =
\mathbb D_{SV}(H^+_\gamma)
```

with the opposite Hall product and co-opposite coproduct, shifted and
Tate-twisted by the same calibration functions `s(\gamma),t(\gamma)`.
Geometrically this is the Hall algebra of the dual critical chart:
the stack is the same derived critical stack, the charge is negated, and
the coefficient is Verdier-dual vanishing cycles with the dual
orientation line.

**D5. Continuous Hall pairing.**  There is a continuous bilinear pairing

```tex
\langle-,-\rangle_{\Hall}:
H^+_\gamma\widehat\otimes H^-_{-\delta}\longrightarrow R
```

which is zero unless `\gamma=\delta`.  On equal charges it is the
Verdier trace pairing

```tex
R\Gamma^{BM}(\mathfrak M_\gamma,\Phi_{\gamma,o}^{vc})
\otimes
R\Gamma_c(\mathfrak M_\gamma,\mathbb D\Phi_{\gamma,o}^{vc})
  \longrightarrow R,
```

after the shift/Tate normalization.  It satisfies the Hopf-pairing
identities

```tex
\langle ab,c\rangle_{\Hall}
 =
\langle a\otimes b,\Delta^-(c)\rangle_{\Hall},
\qquad
\langle a,bc\rangle_{\Hall}
 =
\langle\Delta^+(a),b\otimes c\rangle_{\Hall},
```

and the Cartan rule

```tex
\langle K_\eta,K_\xi\rangle
 =
L^{\langle\eta,\xi\rangle}.
```

**D6. Radical ideals.**  The left and right radicals

```tex
{\rm Rad}^+
 =
\{a\in H^+:\langle a,H^-\rangle_{\Hall}=0\},
\qquad
{\rm Rad}^-
 =
\{b\in H^-:\langle H^+,b\rangle_{\Hall}=0\}
```

are closed Hopf ideals.  The reduced halves are

```tex
\overline H^\pm = H^\pm/{\rm Rad}^\pm.
```

This quotient is part of the theorem, not a cleanup step: compact
critical stacks and equivariant localizations can create null classes.
The double is the reduced object on which the pairing is nondegenerate.

**D7. Completion.**  All tensor products are completed in the joint
HN/charge/equivariant topology.  Products and coproducts are continuous.
For every finite truncation, the formulas are finite; the completed
formulas are inverse limits of finite formulas.

**D8. Representation finiteness.**  The continuous representation
category used for the center is a complete monoidal category

```tex
{\rm Rep}^{E_1}_{cont}(H^+)
```

whose objects are complete modules with locally finite charge
decomposition and continuous action.  Duals, tensor products, and
half-braidings are computed as inverse limits from finite truncations.

## 2. The Reduced Drinfeld Double

For a double-admissible datum, define

```tex
D^{red}_{\sigma,S}(X)
 =
D^{red}(H^+_{\sigma,S})
 =
\overline H^-\widehat\bowtie H^0\widehat\bowtie\overline H^+.
```

As a completed `R`-module,

```tex
D^{red}_{\sigma,S}(X)
 \cong
\overline H^-\widehat\otimes H^0\widehat\otimes\overline H^+.
```

The algebra structure is determined by:

1. the products on `\overline H^+`, `\overline H^-`, and `H^0`;
2. the Cartan conjugation rule above;
3. the Drinfeld cross relation.  With Sweedler notation

```tex
\Delta^{(2)}(a)=\sum a_{(1)}\otimes a_{(2)}\otimes a_{(3)},
\qquad
\Delta^{(2)}(b)=\sum b_{(1)}\otimes b_{(2)}\otimes b_{(3)},
```

the relation is

```tex
b\,a
 =
\sum
\langle a_{(1)},S(b_{(1)})\rangle_{\Hall}
\langle a_{(3)},b_{(3)}\rangle_{\Hall}
\,a_{(2)}\,b_{(2)},
```

with the Cartan factors inserted by the charge rule in D3.  The formula
is interpreted in each finite quotient and then completed.

The universal element is

```tex
{\mathcal R}_{univ,\lambda}
 =
\sum_i e_i^\lambda\otimes e^{i,\lambda}
```

in every finite truncation, where `{e_i^\lambda}` and
`{e^{i,\lambda}}` are dual homogeneous bases for the reduced positive
and negative halves.  The completed universal `R`-matrix is

```tex
{\mathcal R}_{univ}
 =
\lim_\lambda {\mathcal R}_{univ,\lambda}
\in
D^{red}\widehat\otimes D^{red}
```

whenever the finite dual bases are compatible under truncation.  In that
case it satisfies

```tex
(\Delta\otimes 1){\mathcal R}_{univ}
 =
{\mathcal R}_{13}{\mathcal R}_{23},
\qquad
(1\otimes\Delta){\mathcal R}_{univ}
 =
{\mathcal R}_{13}{\mathcal R}_{12},
```

and hence the Yang--Baxter equation in the completed tensor cube.

## 3. Theorem 8A: Double Construction

**Theorem.**  A double-admissible chambered BPS positive geometry

```tex
P^{BPS,double}_{\sigma,S,o,T_{\rm eq}}(X)
```

canonically determines a complete topological Hopf algebra

```tex
D^{red}_{\sigma,S}(X)
 =
\overline H^-_{\sigma,S}
\widehat\bowtie
H^0_{\sigma,S}
\widehat\bowtie
\overline H^+_{\sigma,S}.
```

It has triangular decomposition, nondegenerate continuous Hopf pairing
between the reduced positive and negative halves, Cartan torus
`H^0_{\sigma,S}`, charge/HN-continuous coproduct, antipode, and
universal `R`-matrix whenever the finite reduced pairings admit
compatible dual bases.

The construction is functorial under inclusions of strict sectors and
compatible with Worker 03 sector descent:

```tex
S=S_1\star\cdots\star S_r
\quad\Longrightarrow\quad
D^{red}_{\sigma,S}
 \simeq
D^{red}_{\sigma,S_1}
\widehat\otimes^{HN}\cdots
\widehat\otimes^{HN}
D^{red}_{\sigma,S_r}
```

with the tensor product ordered by phase and twisted by the Cartan
Euler/orientation bicharacter.

### Proof Spine

Fix a finite truncation `lambda`.  Conditions D1--D2 give a bialgebra
`H^+_\lambda` in the braided category of `\Gamma`-graded `R`-modules
with braiding determined by

```tex
L^{\langle\alpha,\beta\rangle/2}\epsilon_o(\alpha,\beta).
```

D3 gives the group-like Cartan algebra.  D4 constructs a negative
bialgebra by Serre--Verdier duality.  D5 gives a Hopf pairing.
The standard Drinfeld double of a paired bialgebra is therefore defined
at the finite level.  D6 makes the pairing perfect by quotienting by
closed Hopf radicals; the quotient remains a bialgebra because the Hopf
pairing identities make the radicals stable under product, coproduct,
and antipode.  The finite reduced double has triangular decomposition
and universal finite `R`-element.

D7 makes every transition map a morphism of paired bialgebras preserving
Cartan and radicals.  Taking the inverse limit over `lambda` preserves
the algebra, coalgebra, pairing, and triangular decomposition because
all maps are continuous and all identities were finite before
completion.  The compatible finite `R`-elements converge to
`{\mathcal R}_{univ}` exactly when the finite dual bases are compatible.
This proves the completed Hopf algebra and universal `R`-matrix claims.

Sector functoriality follows from Worker 03: HN decomposition identifies
the Hall algebra of an ordered sector with the completed ordered tensor
product of the Hall algebras of the subsectors.  The coproduct,
Cartan, pairing, radical quotient, and universal `R`-element are all
defined on the same HN flag stacks, hence pass through the same sector
factorization isomorphism.

## 4. Theorem 8B: The `E_1` Categorical Center

**Theorem.**  Under D0--D8, the braided monoidal category

```tex
{\mathcal Z}\bigl({\rm Rep}^{E_1}_{cont}(H^+_{\sigma,S})\bigr)
```

is equivalent to the continuous representation category of the reduced
double:

```tex
{\mathcal Z}\bigl({\rm Rep}^{E_1}_{cont}(H^+_{\sigma,S})\bigr)
\simeq
{\rm Rep}^{E_2}_{cont}\bigl(D^{red}_{\sigma,S}(X)\bigr).
```

The half-braiding of a module `M` is the same datum as the compatible
action of the Serre-dual negative half and Cartan satisfying the
Drinfeld cross relation.  The braiding lives on the center, not on
`H^+` itself.

### Proof Spine

At finite truncation, the category of modules over a bialgebra `H` has
Drinfeld center equivalent to the category of Yetter--Drinfeld modules.
A Yetter--Drinfeld module is an `H`-module with a compatible coaction,
or equivalently an action of the dual bialgebra when the finite pairing
is perfect.  D5--D6 make the finite reduced pairing perfect, so the
Yetter--Drinfeld category is the module category of the finite reduced
Drinfeld double.

The finite equivalence sends a half-braiding

```tex
c_{M,N}:M\otimes N\longrightarrow N\otimes M
```

to the action of the dual basis element in the negative half.  The
hexagon identity for the half-braiding is exactly coassociativity of the
negative coaction, and naturality in `N` is exactly the Drinfeld cross
relation.  Cartan compatibility records the charge grading.

D8 ensures that continuous modules and half-braidings are inverse
limits of finite truncation modules and half-braidings.  Since the
finite equivalences commute with transition functors, their inverse
limit gives the displayed equivalence.  This proves that the `E_2`
structure is recovered by the center passage:

```tex
E_1\text{-Hall algebra}
  \longrightarrow
E_1\text{-module category}
  \longrightarrow
E_2\text{-center}.
```

## 5. Separation of the Four Outputs

The construction separates four objects that the programme must never
conflate.

**Positive half.**

```tex
Y^+_{\sigma,S}(X)=H^+_{\sigma,S}.
```

This is the oriented HN-completed Hall algebra.  PBW, when available,
describes its associated graded.  PBW does not construct the double.

**Reduced double.**

```tex
G^{Hall}_{\sigma,S}(X)=D^{red}_{\sigma,S}(X).
```

This is the complete quantum group object with Cartan, negative half,
coproduct, pairing, radical quotient, and universal `R`-matrix.

**Categorical center.**

```tex
{\mathcal Z}\bigl({\rm Rep}^{E_1}_{cont}(Y^+_{\sigma,S}(X))\bigr)
\simeq
{\rm Rep}^{E_2}_{cont}(G^{Hall}_{\sigma,S}(X)).
```

This is where the braided structure lives at `d=3`.

**Full-index or physical output.**

```tex
{\rm Tr}_{\mathcal Z}({\mathcal R}_{univ}\ \text{or}\ K_\rho)
```

is a trace on representations of the center or double.  It is not the
positive half and not the double as an algebra.  For `K3\times E`, this
is the source of the Igusa scalar-square phenomenon:

```tex
{\mathcal D}_X=\Delta_5,
\qquad
\Delta_{10}=\Delta_5^2,
\qquad
Z^X_{\square}=C_{\square}\Delta_5^{-2}.
```

The chiral denominator is the square root; the protected full index is
the scalar square.

## 6. Toric Terminal Normalization

For a toric quiver-critical CY3 chart `(Q,W)` satisfying the standard
critical CoHA hypotheses, the double-admissible data are supplied by
the known cohomological Hall bialgebra, equivariant localization,
stable-envelope transport, and Green pairing.  The theorem recovers:

```tex
X=\mathbb C^3:
\qquad
Y^+(X)=Y^+(\widehat{\mathfrak{gl}}_1),
\qquad
D^{red}(Y^+(X))=Y(\widehat{\mathfrak{gl}}_1),
```

and the centered representation output is the
`\mathcal W_{1+\infty}` side.  Thus

```tex
\CoHA(\mathbb C^3)=Y^+(\widehat{\mathfrak{gl}}_1)
```

is the positive half, not the full centered object.

For the conifold, the same package gives the quantum toroidal
`\mathfrak{gl}_{1|1}` double.  The conifold pentagon from Worker 03 is
the sector-gluing check; the double theorem adds Cartan, negative half,
pairing, radical quotient, and center equivalence.

For local `\mathbb P^2`, the positive half is the critical CoHA of the
`\mathbb Z/3` McKay quiver with potential, and the double is the
corresponding completed toroidal/orbifold double after the same
double-admissibility structures are installed.

These are terminal degenerations: the support monoid is rational
polyhedral, the critical charts are quiver charts, and the Cartan is the
charge torus of the quiver lattice.

## 7. Compact CY3 Theorem Target Beyond Toric Loci

For a smooth compact CY3 category `C`, the strengthened theorem is not
"there exists a familiar quantum toroidal algebra."  The theorem target
is sharper:

```tex
P^{BPS,motloc}_{\sigma,S,o,T_{\rm eq}}(X)
  + D0--D8
  \Longrightarrow
D^{red}_{\sigma,S}(X)
  \simeq
{\rm End}_{\mathcal Z({\rm Rep}^{E_1}_{cont}(H^+))}
({\bf 1})\text{-controlled quantum group}.
```

The output may be toroidal, Yangian, BKM, or a new compact-CY3 quantum
group.  The theorem does not classify the output by analogy.  It
constructs the output from the Hall bialgebra and its pairing.

The compact theorem target is therefore stronger than the toric one:
it does not require a quiver presentation.  It requires the geometric
data that replace the quiver presentation:

```tex
oriented derived critical atlas,
HN sector cosheaf,
compact-support Hall coproduct,
Serre--Verdier negative half,
continuous Hall pairing,
radical quotient,
center-finite representation category.
```

Once these are supplied, the double is a theorem by Sections 3--4.

## 8. `K3\times E` Lorentzian BKM Normalization

The `K3\times E` boundary fixes the non-toric normalization.  The
positive-half bridge has the form

```tex
H^+_{K3\times E}
  \longrightarrow
U(\mathfrak n_+(\mathfrak g_{\Delta_5}))
```

on the numerical or realized Hall side, with primitive seed
`\phi_{0,1}`, Lorentzian charge map

```tex
\alpha(n,l,m)=2n f_2-l f_3+2m f_{-2},
```

and signed root multiplicity

```tex
{\rm smult}(\alpha(n,l,m))=f(nm,l).
```

When the Hall--BKM bridge supplies this positive-half identification
and proves D0--D8 with Lorentzian Cartan

```tex
H^0_{\Delta_5}=R[[\Lambda^{2,1}_{II}]],
```

Theorem 8A gives

```tex
D^{red}(H^+_{K3\times E})
  \simeq
\widehat U(\mathfrak g_{\Delta_5})
```

in the completed BKM sense.  The denominator identity is then the
Cartan-character of the double:

```tex
{\rm den}(\mathfrak g_{\Delta_5})
 =
64^{-1}\Delta_5(2Z)
 =
e^{-2\pi i(\rho,z)}
\prod_{\alpha\in{\mathcal R}_+}
\left(1-e^{-2\pi i(\alpha,z)}\right)^{{\rm smult}(\alpha)}.
```

The Igusa square-root dictionary is:

```tex
primitive seed:        \phi_{0,1},
positive half:         U(\mathfrak n_+(\mathfrak g_{\Delta_5})),
Cartan:                \Lambda^{2,1}_{II},
double:                \widehat U(\mathfrak g_{\Delta_5}),
chiral denominator:    {\mathcal D}_X=\Delta_5,
BKM denominator:       64^{-1}\Delta_5(2Z),
full scalar index:     C_{\square}\Delta_5^{-2}.
```

The denominator determines signed root superdimensions.  It does not by
itself determine the Hall product, the coproduct, the pairing, or the
representation category.  Those are exactly the data supplied by
`P^{BPS,double}`.

## 9. Wall Transport and Double Invariance

Let `\sigma` and `\sigma'` be stability chambers separated by an
admissible wall.  Worker 03 gives motivic wall transport on the positive
Hall cosheaf by quantum-dilogarithm conjugation.  The double theorem
strengthens this to the paired bialgebra level when the wall transport
preserves D0--D8:

```tex
\Phi_{\sigma\to\sigma'}^+:
H^+_{\sigma,S}\longrightarrow H^+_{\sigma',S'}
```

extends uniquely to

```tex
\Phi_{\sigma\to\sigma'}^{D}:
D^{red}_{\sigma,S}(X)
  \longrightarrow
D^{red}_{\sigma',S'}(X)
```

provided it preserves:

```tex
coproduct,
Cartan charge torus,
Serre--Verdier negative half,
Hall pairing,
radical ideals,
completion topology.
```

The proof is formal: the double is generated topologically by
`H^-`, `H^0`, and `H^+` modulo the cross relation, and the listed
preservations are precisely the assertion that the cross relation is
carried to the cross relation.  Around a codimension-two joint, Worker
03 identity holonomy implies identity double holonomy in every finite
truncation, hence after completion.

## 10. Computational Finite-Truncation Oracle

The double is computable only through finite quotients.  For each
truncation `lambda`, store:

```tex
P_\lambda[\alpha,\beta;\gamma]
  = product matrices for H^+_\alpha\otimes H^+_\beta\to H^+_\gamma,

C_\lambda[\gamma;\alpha,\beta]
  = coproduct matrices for H^+_\gamma\to H^+_\alpha\otimes H^+_\beta,

G_\lambda[\gamma]
  = Hall-pairing Gram matrix between H^+_\gamma and H^-_{-\gamma},

K_\lambda[\eta,\gamma]
  = Cartan conjugation scalars,

R_\lambda
  = finite universal R-matrix after radical quotient.
```

The tests are:

```tex
associativity:          P(P\otimes 1)=P(1\otimes P),
coassociativity:        (C\otimes 1)C=(1\otimes C)C,
Green compatibility:    C(P)=P_{braided}(C\otimes C),
pairing compatibility:  <ab,c>=<a\otimes b,C(c)>,
radical stability:      Rad is closed under P and C,
cross relation:         negative-positive products match the pairing formula,
R identities:           (Delta\otimes1)R=R13 R23 and (1\otimes Delta)R=R13 R12,
center equivalence:     half-braiding matrices satisfy the hexagon,
wall transport:         conjugated matrices match in adjacent chambers.
```

For toric examples these tests reduce to known shuffle/stable-envelope
identities.  For the conifold, the wall test contains the quantum
pentagon.  For `K3\times E`, the Gram matrices must reproduce the
Lorentzian root pairing and the denominator exponent table
`{\rm smult}(\alpha(n,l,m))=f(nm,l)` after realization.

## 11. Failure Modes Healed into Stronger Data

**PBW implies the double.**  False.  PBW is an associated-graded theorem
for the positive half.  The stronger theorem requires D2--D6:
coproduct, Cartan, negative half, Hopf pairing, and radical quotient.

**The positive half is already braided.**  False at `d=3`.  The positive
Hall algebra is `E_1`.  Braiding lives in

```tex
{\mathcal Z}({\rm Rep}^{E_1}_{cont}(H^+)).
```

**The coproduct is automatic from the product.**  False.  Product and
coproduct use opposite variances of extension stacks.  The stronger
datum requires compact-support or localized Borel--Moore functoriality
and Green compatibility.

**The Hall pairing is automatically nondegenerate.**  False.  Critical
cohomology and equivariant localization can create null classes.  The
stronger object quotients by the closed Hopf radical.

**Cartan is optional.**  False.  Without Cartan the Euler form,
orientation bicharacter, equivariant weights, and charge grading have no
place to act.  The Cartan torus is part of the double.

**Completion is harmless.**  False.  Infinite BPS spectra require
finite truncations first.  All identities are finite identities before
they are completed identities.

**The Igusa denominator is the full physical index.**  False.  The
double theorem separates the chiral denominator, BKM denominator, and
full scalar square:

```tex
{\mathcal D}_X=\Delta_5,
\qquad
{\rm den}(\mathfrak g_{\Delta_5})=64^{-1}\Delta_5(2Z),
\qquad
Z^X_{\square}=C_{\square}\Delta_5^{-2}.
```

## 12. Final Form

The strict theorem is:

```tex
P^{BPS,motloc}_{\sigma,S,o,T_{\rm eq}}(X)
  + {\rm double\mbox{-}admissibility}
  \Longrightarrow
D^{red}_{\sigma,S}(X)
  =
\overline H^-\widehat\bowtie H^0\widehat\bowtie\overline H^+
```

and

```tex
{\mathcal Z}\bigl({\rm Rep}^{E_1}_{cont}(H^+_{\sigma,S})\bigr)
\simeq
{\rm Rep}^{E_2}_{cont}\bigl(D^{red}_{\sigma,S}(X)\bigr).
```

The toric effective positive geometry is the degenerate case where
`H^+` is a quiver critical CoHA over a rational-polyhedral monoid and
the reduced double is a known toroidal/Yangian object.  The compact
non-toric theory is the same construction with a genuinely global
critical Hall bialgebra and Hall pairing.  The `K3\times E` boundary is
the Lorentzian BKM specialization where the reduced double is
`\widehat U(\mathfrak g_{\Delta_5})` once the positive Hall--BKM bridge
has supplied the positive half and D0--D8.

Changed files:

```text
notes/bps_positive_geometry_total_resolution_20260424/agent_07_drinfeld_double_center.md
```
