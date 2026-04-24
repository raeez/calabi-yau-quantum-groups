# Homotopy Gluing and Positive-Cone Geometry

Date: 2026-04-24.

## Thesis

The homotopy-gluing side and the positive-cone side are not two
competing constructions.  They are two truncations of one typed object.

The live object is a completed oriented motivic Hall cosheaf on a
Dolbeault--Weiss--Ran/Cech descent site:

```tex
\mathcal P^{BPS}_{\sigma,S,o,T_{\mathrm{eq}}}(X)
 =
(\mathcal H^{mot,or}_{\sigma,-}, Int^{mot}, Real, Dec, Enh).
```

The homotopy-gluing side is the construction of
`\mathcal H^{mot,or}_{\sigma,-}` from local critical Hall charts,
orientation data, Cech/Ran descent, and sector factorisation.  The
positive-cone side is the decategorified chamber data extracted by
`Dec`: support, completion monoid, wall product, orientation character,
and automorphic boundary.  Thus the positive cone is not a replacement
for Cech descent; it is the chamber-completion index on which descent
becomes computable.

## First-Principles Object

Fix a smooth CY3 category `C`, a Bridgeland chamber `sigma`, a strict
central-charge sector `S`, orientation output `o`, and equivariance
data `T_eq`.  A finite truncation of the object is constructed before
completion:

```tex
\mathsf F_{N,R}\mathcal P^{BPS}_{\sigma,S,o,T_{\mathrm{eq}}}(X).
```

Here `N` is a charge-height cutoff and `R` is a central-charge-radius
cutoff.  The completed object is the inverse limit

```tex
\mathcal P^{BPS}_{\sigma,S,o,T_{\mathrm{eq}}}(X)
 =
\varprojlim_{N,R}
\mathsf F_{N,R}\mathcal P^{BPS}_{\sigma,S,o,T_{\mathrm{eq}}}(X).
```

This finite-first rule is load-bearing.  Hall products, motivic
integrals, KS wall-crossing factors, theta enhancements, Drinfeld
doubles, and Borcherds products must commute with the transition maps.
Without this rule the same infinite product can mean a formal product,
a topological completion, or an analytic convergence statement.

The Hall cosheaf is

```tex
\mathcal H^{mot,or}_{\sigma,-}:
\mathsf{Sect}_{\sigma}(C)
  \longrightarrow
\mathsf{CAlg}^{\wedge}_{\mathsf{Mot}},
```

where a sector `V` is sent to the completed oriented critical Hall
algebra

```tex
\widehat{\bigoplus}_{\gamma\in\Gamma_{\sigma,V}}
H^{BM}_{G_\gamma}
(\operatorname{Crit}(f_{\gamma}),\phi_{f_\gamma}\otimes \mathscr L_o).
```

The multiplication is the usual Hall pull-push along the stack of short
exact sequences, followed by Thom--Sebastiani transport of vanishing
cycles, orientation-line transport, the normalising shift and Tate
twist, and HN completion.

The decategorification map is

```tex
Dec=support\circ K_0\circ Int^{mot}\circ Real_\bullet.
```

It produces the chambered positive data:

```tex
P^{BPS,\bullet}_{\sigma,S,o,T_{\mathrm{eq}}}(X)
 =
(\Gamma^{ss}_{\sigma,S},
 \Gamma^{BPS,\bullet}_{\sigma,S,o},
 \Gamma^+_{\sigma,S,o},
 \widehat{\mathbb T}^{mot}_{\Gamma,S,o},
 A_S(\sigma),
 \epsilon_o).
```

The separation is:

```tex
\Gamma^{ss}_{\sigma,S}
  = charges whose semistable moduli are nonempty in S,

\Gamma^{BPS,\bullet}_{\sigma,S,o}
  = charges with nonzero realized BPS invariant,

\Gamma^+_{\sigma,S,o}
  = \mathbb N\langle \Gamma^{BPS,\bullet}_{\sigma,S,o}\rangle.
```

The stack is indexed by semistable support.  The topology of the Hall
algebra and the KS product is completed along the BPS-generated monoid.

## Homotopy Gluing

Let `U` be a DWR-good Stein-polydisc cover of `X`, closed under finite
intersections and Weiss refinements.  The descent category has objects

```tex
\sigma=(S,\{P_s\Subset U_{i_{s,0}}\cap\cdots\cap U_{i_{s,p}}\}_{s\in S})
```

with pairwise disjoint polydiscs.  Faces forget Cech indices,
refinements shrink polydiscs, and Ran multiplication is disjoint union.

On the hCS side one has Costello--Gwilliam observables

```tex
\Obs^q_{\hCS}(\sigma,\mathfrak g)
 =
\widehat{\bigotimes}_{s\in S}
\Obs^q_{\hCS}(P_s,\mathfrak g).
```

On the Hall side one has

```tex
\CoHA^{or}_{crit}(\sigma)
 =
\widehat{\bigoplus}_{\gamma\in\Gamma^S}
\widehat{\bigotimes}_{s\in S}
H^{BM}_{G_{\gamma_s}}
(\operatorname{Crit}(f_{P_s,\gamma_s}),
 \phi_{f_{P_s,\gamma_s}}\otimes\mathscr L_{o_{P_s,\gamma_s}})
[s(P_s,\gamma_s)](t(P_s,\gamma_s)).
```

The bridge is not a map on one open set.  It is a degree-zero
continuous natural transformation on the full DWR/Cech/Ran nerve:

```tex
\Theta^{or}_{\hCS\to\Hall}:
\Obs^q_{\hCS}(-,\mathfrak g)
  \longrightarrow
\CoHA^{or}_{crit}(-).
```

Its seven required compatibilities are: chain condition, compact-support
Beck--Chevalley, Cech/Ran naturality, Hall convolution, orientation
transport, HN-sector completion, and wall-crossing transport.  When
these hold, the global map is the induced map on the homotopy colimit of
the DWR nerve.  This is the homotopy-gluing construction.

## Positive Cone

The positive cone is the decategorified completion datum of the same
object.  In a toric standard chamber it collapses to the familiar
quiver cone:

```tex
\Gamma^{ss}_{\sigma,S}
 =
\Gamma^+_{\sigma,S,o}
 =
\mathbb Z_{\ge 0}^{Q_0},

\mathcal H^{mot,or}_{\sigma,S}(X_\Sigma)
 =
\CoHA(Q_\Sigma,W_\Sigma).
```

This is the terminal rational-polyhedral degeneration.  It is not the
general pattern.  For compact or lattice-polarised CY3s the replacement
for a fan is the tuple

```tex
(\Gamma,\ S,\ \Gamma^+,\ \epsilon_o,\ A_S,\ \operatorname{Wall},\
 \operatorname{AutBorch}).
```

Wall-crossing is then the equality of sector products in the completed
motivic quantum torus:

```tex
A_S(\sigma)
 =
\prod_{\ell\subset S}^{clockwise}
\prod_{Z_\sigma(\gamma)\in\ell}
\mathbb E(x_\gamma)^{\Omega^{mot}_{\sigma,o}(\gamma)}.
```

The classical dilogarithm formula is only the Euler-realized shadow.
The quantum-torus-valued product is primary.

## Igusa Boundary for `K3 x E`

The dirty positive-cone work in `~/igusa-cusp-form` supplies the first
non-toric automorphic boundary that the Vol III object must recover.
The boundary data are:

```tex
\Gamma_{\mathrm{BPS}}=\mathbb Z^3,\qquad
\gamma=(n,l,m),
```

```tex
\Gamma_{\mathrm{eff}}
 =
\{m>0,\ n\ge0,\ l\in\mathbb Z\}
\cup
\{m=0,\ n>0,\ l\in\mathbb Z\}
\cup
\{m=n=0,\ l<0\}.
```

The Lorentzian degree map is

```tex
\alpha(n,l,m)=2n f_2-l f_3+2m f_{-2}
\in \Lambda^{2,1}_{II}.
```

With bilinear form

```tex
(f_2,f_{-2})=-1,\qquad (f_3,f_3)=2,
```

one has

```tex
(\alpha(\gamma),\alpha(\eta))
 =
-2\langle\gamma,\eta\rangle_{\mathrm{BPS}},
\qquad
(\alpha(\gamma),\alpha(\gamma))=-2(4nm-l^2).
```

The three real simple roots are

```tex
\delta_1=2f_2-f_3,\qquad
\delta_2=2f_{-2}-f_3,\qquad
\delta_3=f_3,
```

with Gram matrix

```tex
\begin{pmatrix}
2&-2&-2\\
-2&2&-2\\
-2&-2&2
\end{pmatrix}.
```

The finite-volume chamber is

```tex
\Poly_{II}=\{x:(x,\delta_i)\le0,\ i=1,2,3\}/\mathbb R_{>0},
```

and the Weyl vector is

```tex
\rho=f_2-\frac12 f_3+f_{-2},\qquad
(\rho,\delta_i)=-1.
```

The primitive one-particle seed is

```tex
\phi_{0,1}=\sum_{n,l}f(n,l)q^n r^l
          =r^{-1}+10+r+O(q),
```

and the Borcherds product is

```tex
\mathcal D_X(Z)
 =
64 q^{1/2}r^{1/2}s^{1/2}
\prod_{\Gamma_{\mathrm{eff}}}
(1-q^n r^l s^m)^{f(nm,l)}
 =
\Delta_5(Z).
```

The denominator algebra reads the same object in Weyl--Kac--Borcherds
normalisation:

```tex
\operatorname{den}(\mathfrak g_{\Delta_5})
 =
64^{-1}\Delta_5(2Z).
```

The invariant is

```tex
\kappa_{\mathrm{BKM}}(\mathfrak g_{\Delta_5})
 =
\operatorname{wt}(\Delta_5)
 =
c_1(0)/2
 =
10/2
 =
5.
```

This is not `\chi_{\mathrm{top}}(K3\times E)/24`, not
`\kappa_{\mathrm{cat}}(K3\times E)`, not a Kunneth product, and not the
full scalar-square index.  The square is

```tex
Z^X_{\square}=C_{\square}\Delta_5^{-2},
```

while `\Delta_5` is the chiral half and
`\Delta_{10}=\Delta_5^2` is the scalar square.

## The Dictionary

```tex
Homotopy gluing                         Positive-cone / Igusa boundary
-------------------------------------------------------------------------------
DWR/Cech/Ran nerve                      chambered sector site
oriented critical Hall cosheaf          completed motivic quantum torus
HN sector                               Gamma_eff product chamber
orientation local system                Maass character nu_{Delta_5}
KS wall transport                       Weyl-chamber / divisor transport
BPS primitive motive                    phi_{0,1}
support + completion                    Gamma_eff and alpha(Gamma_eff)
Hall product                            Borcherds product
hCS-to-Hall comparison                  stationary-phase realization of seed
AutBorch enhancement                    phi_{0,1} |-> Delta_5
Drinfeld double enhancement             full BKM/quantum-group output
```

The last two rows are enhancements.  They do not exist automatically
from the positive half.  In particular:

```tex
\CoHA \neq \mathcal W_{1+\infty},
\qquad
D(\operatorname{hocolim}Y^+)
\neq
\operatorname{hocolim}D(Y^+)
```

without a completed coproduct, continuous Hopf pairing, Cartan, negative
half, and radical quotient.

## Synthesis Theorem

**Theorem.**  Let `X` be a CY3 datum for which the oriented critical
Hall cosheaf exists on a DWR/Cech/Ran site and satisfies HN-sector
descent.  Then the chambered positive geometry of `X` is the
decategorified completion system of that cosheaf:

```tex
Dec(\mathcal H^{mot,or}_{\sigma,-})
 =
(\Gamma^{ss}_{\sigma,-},
 \Gamma^{BPS,\bullet}_{\sigma,-,o},
 \Gamma^+_{\sigma,-,o},
 A_{-}(\sigma),
 \epsilon_o).
```

Admissible wall paths act on the left by descent transport of the Hall
cosheaf and on the right by KS conjugation in the completed motivic
quantum torus.  For `K3 x E` in the Igusa chamber, the automorphic
boundary enhancement of this decategorified object is the Lorentzian
Borcherds chamber above, with

```tex
\operatorname{AutBorch}(\phi_{0,1})=\Delta_5,\qquad
\kappa_{\mathrm{BKM}}(\mathfrak g_{\Delta_5})=5.
```

**Status.**  The descent statement is formal once the oriented Hall
cosheaf and its DWR/Cech/Ran comparison data exist.  The Igusa
denominator arithmetic is proved in the `~/igusa-cusp-form` boundary.
The full compact `K3 x E` Hall--Drinfeld double and the global
`\Theta^{or}_{\hCS\to\Hall}` remain conditional frontier data.

## Proof Spine

1.  The DWR/Cech/Ran site turns local polydisc data into a simplicial
    descent object.  Homotopy colimits over this site compute global
    factorisation observables when the descent axioms hold.

2.  The oriented critical Hall charts form a cosheaf on strict
    HN sectors.  Sector concatenation gives completed tensor products;
    wall paths give KS transport.

3.  Motivic integration sends the Hall cosheaf to the completed quantum
    torus.  Applying `K_0`, realization, and support extraction gives
    the semistable support, the BPS support, and the BPS-generated
    completion monoid.

4.  The positive cone is therefore not extra geometry.  It is the
    support/completion side of the same descent object.

5.  In toric examples, this support is `\mathbb Z_{\ge0}^{Q_0}` and the
    Hall algebra is a quiver CoHA.  In `K3 x E`, the support is the
    Igusa `\Gamma_{\mathrm{eff}}`, mapped by `\alpha` into the
    Lorentzian chamber `\Poly_{II}`.

6.  The Maass character `\nu_{\Delta_5}` realizes the determinant-line
    orientation on the automorphic boundary.  The product chamber
    expansion of `\Delta_5` is the boundary value of the same Hall
    scattering datum after applying the `AutBorch` enhancement.

## Non-Conflation Rules

1.  `\Gamma^{ss}` indexes the stack; `\Gamma^+` completes the Hall
    algebra.  They coincide only in toric terminal degenerations.

2.  `\CoHA` is the positive half.  The quantum group requires double,
    Cartan, pairing, completion, negative half, and radical quotient.

3.  The Igusa positive cone is Lorentzian Weyl-chamber positivity, not a
    toric fan or Mori cone.

4.  `\Delta_5` is the chiral determinant / Borcherds denominator half.
    `\Delta_5^2` is the scalar square.

5.  `\kappa_{\mathrm{BKM}}=5` is a Borcherds weight.  It is not
    `\kappa_{\mathrm{cat}}`, not `\chi_{\mathrm{top}}/24`, and not an
    additive fibre formula.

## Compute Witness

The exact arithmetic surface is recorded in
`compute/lib/positive_cone_gluing_bridge.py` and tested by
`compute/tests/test_positive_cone_gluing_bridge.py`.  The tests verify:

```tex
(\delta_i,\delta_j)=
\begin{pmatrix}
2&-2&-2\\
-2&2&-2\\
-2&-2&2
\end{pmatrix},

(\rho,\delta_i)=-1,

(\alpha(\gamma),\alpha(\eta))
=-2\langle\gamma,\eta\rangle_{\mathrm{BPS}},

\kappa_{\mathrm{BKM}}(\Delta_5)=10/2=5.
```

Targeted verification:

```text
pytest compute/tests/test_positive_cone_gluing_bridge.py -q
```

returned `8 passed`.
