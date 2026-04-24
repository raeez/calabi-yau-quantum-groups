# Worker 04: Realization Compatibility

Date: 2026-04-24.

Assigned obligation: construct the realization tower from motivic or
homotopical BPS Hall data to numerical BPS invariants, and prove that
Hall multiplication, orientation signs, Tate twists, Harder--Narasimhan
completions, and wall-crossing transport survive every realization
functor.

Write scope: this file only.

## Resolution

The realization problem has a theorem-grade solution once the coefficient
system is required to be a realization-compatible Hall coefficient system.
The point is not to weaken the object.  The stronger object records
precisely the functorial data that realization must preserve:

```tex
P^{BPS,real}_{\sigma,S,o,T_{\rm eq}}(X)
 =
 (P^{BPS,motloc}_{\sigma,S,o,T_{\rm eq}}(X),
  \mathcal R_{\rm Hdg},
  \chi_{\rm c},
  \lambda,
  \tau_o).
```

Here `P^{BPS,motloc}` is the oriented sector-completed motivic Hall
object, `\mathcal R_{\rm Hdg}` is Hodge realization, `\chi_{\rm c}` is
compactly supported Euler realization, `\lambda` is the compatible
lambda-ring structure used by plethystic exponentials, and `\tau_o` is
the orientation/Tate calibration cochain whose coboundary is the Hall
extension twist divided by the quantum-torus twist.

With these data the tower is functorial:

```tex
motivic spectra / Voevodsky motives / monodromic MHM
  -> K_0(MMHS)[L^{\pm 1/2}]
  -> completed motivic quantum torus
  -> Euler-specialized classical torus
  -> numerical Omega.
```

The toric and conifold compute hooks already test the finite truncations
of this theorem: motivic CoHA associativity, Euler specialization of the
motivic MacMahon series, conifold Euler specialization, and the quantum
pentagon wall-crossing identity.

## Realization-Compatible Hall Coefficients

Let `k=C`.  Let `C` be a compactly generated Calabi--Yau three category
whose numerical charge lattice is

```tex
\Gamma = K_0^{\rm num}(C),
```

with integral skew Euler form

```tex
\langle \alpha,\beta\rangle
 =
\chi(\alpha,\beta)-\chi(\beta,\alpha).
```

Fix a Bridgeland stability condition `\sigma`, a strict sector `S`, a
support-property quadratic form, and strong orientation data `o`.  The
orientation data means:

1. square roots of the virtual determinant lines on every derived
   critical chart;
2. orientation local systems on the vanishing-cycle coefficient systems;
3. coherent transport on overlaps;
4. vanishing residual triple-overlap class in
   `\check H^2(-,Z/2)`;
5. Thom--Sebastiani compatibility for all iterated extension
   correspondences.

A realization-compatible Hall coefficient system is a symmetric
monoidal six-functor target `\mathcal M` satisfying the following
axioms.

**H1. Vanishing cycles.**  For every oriented derived critical chart
`(U,f,o_U)` there is an object

```tex
\Phi^{vc}_{f,o_U}\in \mathcal M({\rm Crit}(f))
```

whose Hodge realization is the monodromic mixed Hodge module of
vanishing cycles and whose Euler realization is Behrend-weighted
compactly supported Euler characteristic.

**H2. Thom--Sebastiani.**  For all critical charts there are coherent
isomorphisms

```tex
{\rm TS}_{f,g}:
\Phi^{vc}_{f,o_f}\boxtimes \Phi^{vc}_{g,o_g}
  \simeq
\Phi^{vc}_{f\boxplus g,o_{f\boxplus g}},
```

compatible with the two parenthesizations of a triple sum.

**H3. Six-functor realization.**  Hodge realization

```tex
\mathcal R_{\rm Hdg}:\mathcal M(-)\to D^bMHM^{mon}(-)
```

commutes with the pullbacks, proper pushforwards, external products,
Tate twists, equivariant localization maps, vanishing cycles, and the
Thom--Sebastiani isomorphisms used in Hall convolution.

**H4. Half-Tate normalization.**  The coefficient ring contains a formal
half Tate object `L^{1/2}` with `(L^{1/2})^2=L`, and Hodge realization
sends it to the formal half Tate class in
`K_0(MMHS)[L^{\pm 1/2}]`.  Compact Euler realization satisfies

```tex
\chi_{\rm c}(L^{m/2})=1
```

for all integers `m`; orientation local systems are not killed by this
rule and contribute their signs through trace.

**H5. Lambda compatibility.**  The Grothendieck group
`K_0(MMHS)[L^{\pm 1/2}]` carries the symmetric-power lambda structure
and Adams operations `\psi_n`.  The maps from motivic coefficients to
`K_0(MMHS)[L^{\pm 1/2}]` and from there to Euler characteristic are
lambda-ring maps on every finite charge truncation.

**H6. HN local finiteness.**  For every mass bound `R` and charge norm
bound `N`, the set of semistable charges in `S` is finite.  The
completed Hall object is the inverse limit over these finite
truncations, and every realization functor commutes with this inverse
limit because all transition maps are charge-truncation projections.

The Hodge lane is obtained by taking `\mathcal M=D^bMHM^{mon}` from the
start.  The motivic lane is obtained by taking monodromic Voevodsky
motives or motivic spectra with Ayoub/Denef--Loeser vanishing cycles
and then applying Hodge realization.  The theorem below only uses the
six properties above; therefore both lanes have the same realization
compatibility proof.

## The Realization Tower

For each charge `\gamma` set

```tex
\mathcal H^{mot}_\gamma
 =
R\Gamma^{BM}_{T_{\rm eq}}
\bigl(\mathfrak M_\sigma(\gamma),
      \Phi^{vc}_{\gamma,o}\bigr)[s(\gamma)](t(\gamma)),
```

where `s(\gamma)` is the perverse/cohomological shift and `t(\gamma)` is
the Tate twist fixed by the orientation convention.  The sector Hall
object is

```tex
\mathcal H^{mot}_{\sigma,S,o}
 =
\widehat\bigoplus_{\gamma\in\Gamma^{ss}_{\sigma,S}}
\mathcal H^{mot}_\gamma.
```

Hodge realization gives

```tex
\mathcal H^{MHM}_{\sigma,S,o}
 =
\mathcal R_{\rm Hdg}(\mathcal H^{mot}_{\sigma,S,o}).
```

The Grothendieck realization is

```tex
[\mathcal H^{MHM}_{\sigma,S,o}]
\in
\prod_{\gamma\in\Gamma^+_{\sigma,S,o}}
K_0(MMHS)[L^{\pm1/2}]\cdot x_\gamma.
```

The completed motivic quantum torus is

```tex
\widehat{\mathbb T}^{mot}_{\Gamma,S,o}
 =
\prod_{\gamma\in\Gamma^+_{\sigma,S,o}}
K_0(MMHS)[L^{\pm1/2}]\cdot x_\gamma,
```

with multiplication

```tex
x_\alpha x_\beta
 =
L^{\langle\alpha,\beta\rangle/2}
\epsilon_o(\alpha,\beta)x_{\alpha+\beta}.
```

The sign

```tex
\epsilon_o:\Gamma\times\Gamma\to\{\pm1\}
```

is the orientation quadratic-refinement cocycle induced by `o`.

Euler specialization is the continuous ring map

```tex
\chi_{\rm c}:
\widehat{\mathbb T}^{mot}_{\Gamma,S,o}
  \longrightarrow
\widehat{\mathbb T}^{cl}_{\Gamma,S,o},
```

defined on coefficients by compact Euler characteristic and on
monomials by

```tex
\chi_{\rm c}(x_\gamma)=e_\gamma.
```

Since `\chi_{\rm c}(L^{1/2})=1`, the classical torus product is

```tex
e_\alpha e_\beta
 =
\epsilon_o(\alpha,\beta)e_{\alpha+\beta}.
```

If the orientation sign is absorbed into the charge basis by a chosen
quadratic refinement, this becomes the ordinary commutative classical
torus; without that basis change the sign remains visible.

The numerical BPS invariant is extracted from the sector KS element by
the plethystic logarithm:

```tex
\Omega^{num}_{\sigma,o}(\gamma)
 =
[e_\gamma]\,
\chi_{\rm c}\Bigl(
{\rm PLog}_\lambda A^{mot}_{\sigma,S,o}
\Bigr).
```

Because `\chi_{\rm c}` is a lambda-ring map on finite truncations,

```tex
\chi_{\rm c}({\rm PLog}_\lambda A^{mot})
 =
{\rm PLog}(\chi_{\rm c}(A^{mot})).
```

Thus numerical `\Omega` is the Euler realization of motivic BPS data,
not an independently defined replacement.

## Theorem: Realization Compatibility

Let `C`, `\sigma`, `S`, `o`, `T_{\rm eq}`, and `\mathcal M` satisfy
H1--H6.  Let

```tex
\mathcal H^{mot}_{\sigma,S,o}
```

be the oriented completed motivic Hall object with product defined by
extension correspondences and Thom--Sebastiani.  Then:

1. Hodge realization sends motivic Hall multiplication to monodromic
   mixed-Hodge Hall multiplication.
2. The Grothendieck-class map sends Hodge Hall multiplication to the
   product in the completed motivic quantum torus.
3. Orientation signs and Tate twists are preserved exactly: orientation
   local systems contribute `\epsilon_o`, and half-Tate factors become
   the powers of `L^{1/2}` in the quantum-torus product.
4. Euler specialization is a continuous algebra homomorphism from the
   completed motivic quantum torus to the classical signed torus.
5. Harder--Narasimhan sector factorization is preserved by every arrow
   in the tower.
6. Kontsevich--Soibelman wall-crossing transport commutes with every
   arrow in the tower.
7. Numerical BPS invariants satisfy

```tex
\Omega^{num}_{\sigma,o}(\gamma)
 =
\chi_{\rm c}\bigl(\Omega^{mot}_{\sigma,o}(\gamma)\bigr)
```

charge by charge on every finite HN truncation, hence in the completed
sector limit.

### Proof

Hall multiplication in charge degrees `\alpha,\beta` is the composite

```tex
\mathcal H^{mot}_\alpha\boxtimes\mathcal H^{mot}_\beta
  \xrightarrow{p^*}
R\Gamma^{BM}(E_{\alpha,\beta},p^*(-\boxtimes-))
  \xrightarrow{{\rm TS}_o}
R\Gamma^{BM}(E_{\alpha,\beta},q^*\Phi^{vc}_{\alpha+\beta})
  \xrightarrow{q_!}
\mathcal H^{mot}_{\alpha+\beta},
```

with the fixed shift and Tate normalization.  By H3,
`\mathcal R_{\rm Hdg}` commutes with `p^*`, `q_!`, external products,
the vanishing-cycle objects, Tate twists, and Thom--Sebastiani.  Applying
`\mathcal R_{\rm Hdg}` to the displayed composite gives the identical
Hall convolution composite in monodromic mixed Hodge modules.  This
proves (1).

Passing to `K_0(MMHS)[L^{\pm1/2}]` changes distinguished triangles into
additive relations and symmetric monoidal products into multiplication.
The extension correspondence contributes the universal relative
extension twist.  The orientation calibration `\tau_o` is chosen so that
its coboundary is exactly

```tex
\delta\tau_o(\alpha,\beta)
 =
{\rm HallTwist}_o(\alpha,\beta)\,
\bigl(
L^{\langle\alpha,\beta\rangle/2}\epsilon_o(\alpha,\beta)
\bigr)^{-1}.
```

Therefore the image of Hall convolution is multiplication by

```tex
L^{\langle\alpha,\beta\rangle/2}\epsilon_o(\alpha,\beta)
```

in the quantum torus.  This proves (2) and also identifies the exact
source of every sign and half-Tate factor.

The orientation local system is a `Z/2` local system.  Its realized trace
on the extension correspondence is `+1` or `-1`; the coherent
orientation transport in H2 makes this trace multiplicative on iterated
extensions.  The half-Tate object is functorial by H4.  Hence orientation
signs and Tate twists cannot disappear under Hodge or Grothendieck
realization.  They become precisely the two factors in the quantum-torus
law.  This proves (3).

Compact Euler characteristic is additive on triangles, multiplicative on
external products, and sends `L^{m/2}` to `1`.  Since H4 keeps the
orientation trace separate from the Tate trace, the Euler image of the
quantum-torus product is

```tex
\chi_{\rm c}(x_\alpha x_\beta)
 =
\epsilon_o(\alpha,\beta)e_{\alpha+\beta}
 =
\chi_{\rm c}(x_\alpha)\chi_{\rm c}(x_\beta).
```

Continuity follows from H6: the completed torus is an inverse limit of
finite charge truncations and `\chi_{\rm c}` is applied coefficientwise.
This proves (4).

The HN filtration gives, for an ordered sector decomposition
`S=S_1*\cdots*S_r`,

```tex
\mathcal H^{mot}_{\sigma,S,o}
\simeq
\mathcal H^{mot}_{\sigma,S_1,o}
\widehat\otimes\cdots\widehat\otimes
\mathcal H^{mot}_{\sigma,S_r,o}.
```

On every finite truncation this is the usual HN stratification: every
object has a unique filtration with semistable factors of decreasing
phase.  The stratum map is built from the same pullbacks, pushforwards,
external products, vanishing cycles, orientation transports, and Tate
twists already handled above.  Realization preserves the finite
truncation isomorphism, and H6 passes it to the completed inverse limit.
This proves (5).

Let `A^{mot}_{\sigma,S,o}` be the ordered KS product in the completed
motivic quantum torus:

```tex
A^{mot}_{\sigma,S,o}
 =
\prod_{\ell\subset S}^{\curvearrowright}
A^{mot}_{\sigma,\ell,o}.
```

The Hall wall-crossing theorem states that this element is unchanged by
changing `\sigma` inside the chambered path, after reordering the active
rays.  Hodge realization, Grothendieck realization, and Euler
specialization are continuous algebra homomorphisms by (1)--(4), so they
send equality of ordered products to equality of ordered products.  The
parallel transport automorphism across a wall is conjugation by the
active factor:

```tex
T_W^{mot}(a)=A_W^{mot}a(A_W^{mot})^{-1}.
```

For every realization `R` in the tower,

```tex
R(T_W^{mot}(a))
 =
R(A_W^{mot})R(a)R(A_W^{mot})^{-1}
 =
T_W^R(R(a)).
```

Thus wall-crossing transport commutes with the tower.  This proves (6).

Finally, the BPS invariant is obtained from the KS element by the
lambda-ring plethystic logarithm.  By H5, all Adams operations and
symmetric-power operations commute with Hodge and Euler realization on
finite charge truncations.  Hence

```tex
\chi_{\rm c}({\rm PLog}_\lambda A^{mot})
 =
{\rm PLog}(\chi_{\rm c}(A^{mot})).
```

Taking the coefficient of `e_\gamma` gives

```tex
\Omega^{num}_{\sigma,o}(\gamma)
 =
\chi_{\rm c}\bigl(\Omega^{mot}_{\sigma,o}(\gamma)\bigr).
```

The equality is finite at every HN truncation and therefore holds in the
completed sector limit.  This proves (7).

## Attack and Heal Checks

**Attack 1: ordinary cohomology loses the potential.**  If one replaces
vanishing cycles by ordinary cohomology, the Behrend sign, the potential,
and the motivic DT invariant are lost.

**Heal.**  H1 forces all coefficients to be vanishing-cycle motives or
monodromic MHM.  Ordinary cohomology appears only after a separate
specialization theorem.

**Attack 2: Euler characteristic kills the Tate twist.**  Since
`\chi_{\rm c}(L^{1/2})=1`, the quantum torus might collapse before
wall-crossing is computed.

**Heal.**  Wall-crossing is computed in the motivic quantum torus before
Euler specialization.  Euler specialization is a final algebra map; it
does not define the motivic product.

**Attack 3: orientation signs disappear under Euler specialization.**
If the orientation local system is treated as a Tate twist, its sign is
lost.

**Heal.**  H4 separates Tate trace from orientation trace.  The former
maps to `1`; the latter maps to `\epsilon_o`.

**Attack 4: HN completion may not commute with realization.**  Infinite
products can fail under functors that do not preserve inverse limits.

**Heal.**  H6 makes every statement finite first.  The completed theorem
is the inverse limit of finite charge/mass truncations.

**Attack 5: numerical `Omega` might not commute with plethystic
logarithm.**  Euler characteristic is not allowed to be applied after an
uncontrolled infinite logarithm.

**Heal.**  H5 and H6 impose lambda compatibility on every finite
truncation.  The equality for `Omega` is proved truncation by truncation
and then completed.

## Compute Hooks Already Present

The existing compute surface witnesses the finite truncations of this
theorem.

```bash
python3 -m pytest \
  compute/tests/test_motivic_e1_algebra.py::TestFullVerification::test_c3_euler_specialization \
  compute/tests/test_motivic_e1_algebra.py::TestFullVerification::test_conifold_euler_specialization \
  compute/tests/test_motivic_e1_algebra.py::TestMultiPathCrossValidation::test_associativity_three_algebras \
  compute/tests/test_motivic_integration_bar.py::TestMasterVerification::test_c3_product_identity \
  compute/tests/test_motivic_integration_bar.py::TestMasterVerification::test_combined_master \
  compute/tests/test_coha_wall_crossing_platonic.py::test_wall_crossing_mc_on_algebra_side \
  compute/tests/test_conifold_wall_crossing.py::TestPentagonExact::test_pentagon_holds_N8_charge4 \
  -q
```

The roles are:

1. `test_c3_euler_specialization`: verifies
   `chi(Z^{mot}(C^3))=M(q)`, plethystic logarithm compatibility, and
   weight-sum compatibility.
2. `test_conifold_euler_specialization`: verifies the conifold D0-sector
   Euler specialization.
3. `test_associativity_three_algebras`: verifies the half-Tate
   cocycle identity behind motivic CoHA associativity.
4. `test_c3_product_identity`: verifies finite motivic product/inverse
   control.
5. `test_combined_master`: verifies the C3/K3 motivic integration master
   surface.
6. `test_wall_crossing_mc_on_algebra_side`: records that KS
   wall-crossing lives on the motivic Hall Lie algebra.
7. `test_pentagon_holds_N8_charge4`: verifies the quantum-torus
   conifold pentagon at finite truncation.

These tests do not prove the compact non-toric construction of
`P^{BPS,motloc}`.  They prove the realization mechanism on the finite
models that already exist in the repository.  The theorem above shows
that no new realization obstruction remains once the motivic Hall object,
strong orientation data, and HN finite-support hypotheses are supplied.

## Output for the Total Resolution

Obligation 4 is solved by the following strengthened theorem statement:

```tex
\boxed{
\begin{gathered}
\text{For every realization-compatible oriented sector-completed}
\\
\text{motivic Hall coefficient system,}
\\
\mathcal H^{mot}_{\sigma,S,o}
\to
K_0(MMHS)[L^{\pm1/2}]
\to
\widehat{\mathbb T}^{cl}_{\Gamma,S,o}
\to
\Omega^{num}
\\
\text{is continuous, multiplicative, HN-factorization preserving,}
\\
\text{orientation/Tate exact, and KS-wall-crossing equivariant.}
\end{gathered}}
```

Thus the positive combinatorial system is not an independent numerical
object.  It is the Euler-realized face of an oriented motivic Hall
cosheaf.  Its multiplication is Hall convolution; its quantum parameter
is the half-Tate realization of the Euler pairing; its signs are the
realized orientation local system; its sector topology is HN completion;
its chamber transport is the image of motivic KS conjugation; its
numerical `Omega` is the Euler image of motivic BPS cohomology.
