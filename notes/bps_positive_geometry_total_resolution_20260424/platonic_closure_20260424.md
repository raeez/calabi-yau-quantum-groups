# Platonic Closure of Chambered BPS Positive Geometry

Date: 2026-04-24.

## Closure Theorem

Let

```tex
\mathfrak I(X,\sigma,Q,S,o,T_eq,Mot)
 =
(C_X,\Gamma_X,<,>,\sigma,Q,S,OrOut,A^{or}_{crit},
Mot,T_eq,HN_{fin},Int^{mot},Real)
```

be a data-realized `3`-Calabi--Yau chamber.  The chambered BPS positive
geometry is the finite-first oriented motivic Hall cosheaf

```tex
\mathcal P^{BPS}_{\sigma,S,o,T_eq}(X)
 =
(\mathcal H^{mot,or}_{\sigma,-},Int^{mot},Real,Dec,Enh)
```

over the chamber-sector site.  It is constructed by the inverse limit

```tex
\mathcal P^{BPS}_{\sigma,S,o,T_eq}(X)
 =
\varprojlim_{N,R}
\mathcal P^{BPS}_{\sigma,S,o,T_eq,<=N,<=R}(X),
```

where every finite quotient is a Hall algebra with orientation output,
HN sector order, motivic integration, and realization tower.  Its
decategorification is

```tex
Dec(\mathcal P^{BPS}_{\sigma,S,o,T_eq}(X))
 =
P^{BPS,bullet}_{\sigma,S,o,T_eq}(X).
```

The toric effective positive geometry is the terminal degeneration:

```tex
\mathcal P^{BPS}(Q,W)=CoHA^{mot}_{crit}(Q,W),
\qquad
Dec(\mathcal P^{BPS}(Q,W))
 =
toric effective positive geometry.
```

This theorem is the subject.  All other structures are functors or
quotients from this source object.

## Compact Non-Toric Witness

The compact non-toric existence problem has a strict solution.  Bayer,
Macri, and Stellari construct Bridgeland stability conditions with
support property on abelian threefolds and on Calabi--Yau threefolds
obtained as crepant resolutions of finite quotients of abelian
threefolds.  Therefore those compact non-toric CY3 chambers supply
actual data packages `\mathfrak I`.

The abelian witness gives the CY category immediately:

```tex
C_A=Perf(A),\qquad K_A\simeq O_A,\qquad Serre_A=[3].
```

The crepant-quotient witness gives a strict smooth projective CY3
example in the Bayer--Macri--Stellari class.  The quintic and Schoen
models are no longer existence gates.  They are named-example
refinements whose exact certificate is:

```tex
ExCert(X;\sigma,S,o,T_eq).
```

No proof may use them until the certificate has been supplied; no
foundational theorem depends on them.

## Igusa Boundary

The paper `~/igusa-cusp-form` teaches the separation:

```tex
one-particle protected index
 -> determinant / denominator half
 -> scalar square or doubled object.
```

For `K3 x E`,

```tex
AutBorch^{den}(\phi_{0,1})
 =
(\Delta_5,\nu_{\Delta_5},64^{-1}\Delta_5(2Z)),
```

with

```tex
\phi_{0,1}=\sum f(n,l)q^nr^l,
\qquad
f(0,0)/2=5,
\qquad
smult(\alpha(n,l,m))=f(nm,l).
```

The Hall theorem is the universal automorphic quotient:

```tex
H^{mot,+}_{K3,E,S,o}/Rad_{Aut}
  \cong
\widehat U(g_{\Delta_5}^{+}).
```

The radical is the closed Hall ideal invisible to the denominator
supertrace, incompatible with the Igusa orientation character, or null
for the denominator pairing.  Thus the bracket obstruction vanishes in
the quotient, not by pretending that the raw Hall bracket was already
the Borcherds bracket.

The full object is obtained only after double-admissibility:

```tex
D(H^{Aut,+}_{K3,E})
  \cong
\widehat U(g_{\Delta_5}).
```

The scalar protected index remains the square:

```tex
Z^X_square=C_square\Delta_5^{-2}.
```

## hCS Localization

The holomorphic Chern--Simons comparison is a theorem in the DWR/Ran
factorization category after the primitive hCS source and Hall target
data exist.  The source/target vector is

```tex
(\omega_{QME},\omega_{anom},\omega_{gf},
 \omega_{DWR},\omega_{crit},\omega_{sp},\omega_{vqis}),
```

and the descent vector is

```tex
o_MC=o_or^rel=o_gr=o_TS=o_fact=o_cs=o_wedge=0.
```

Then

```tex
Theta^{or}_{hCS->Hall}:
Obs^q_{hCS}(-,g)\to CoHA^{or}_{crit}(-)
```

is a morphism in

```tex
FactCosh^{or,wedge}_{Hall}(X).
```

This is complete as a 14-coordinate criterion: the first seven
coordinates construct the object being descended, and the last seven
are the descent complex: differential, orientation, grading/Tate,
Thom--Sebastiani, Ran factorization, compact-support Beck--Chevalley,
and completion.  Their simultaneous vanishing is necessary and
sufficient for the local stationary-phase maps to exist and glue.

## Theta Geometry

For every finite quotient and base chamber `b`, define

```tex
\vartheta^{\lambda,c}_p
 =
\Phi^{KS}_{b->c}(x_p).
```

Identity holonomy around every retained codimension-two joint makes
this independent of path.  The base multiplication is

```tex
\vartheta^{\lambda,b}_p\vartheta^{\lambda,b}_q
 =
\mathbb L^{<p,q>/2}\epsilon_o(p,q)
\vartheta^{\lambda,b}_{p+q}
```

when `p+q` is retained and is zero in the quotient otherwise.  Wall
transport conjugates this product in every other chamber.  Thus

```tex
\Theta^{Hall}_{\lambda,c}
=\{\vartheta^{\lambda,c}_p\}_{p\in\Gamma_\lambda}
```

is the intrinsic Hall-factorization theta basis.  The completed basis
is the inverse limit over finite quotients.

This is a genuine non-toric theta package for the compact
Bayer--Macri--Stellari chambers.  Broken-line, GHKK, and GMN packages
remain comparison enhancements, not prerequisites.

## Executable Closure

The finite oracle lives in:

```text
compute/lib/bps_positive_truncation.py
compute/lib/bps_positive_remaining_gates.py
compute/tests/test_bps_positive_truncation.py
compute/tests/test_bps_positive_remaining_gates.py
```

It certifies:

```tex
support property,
orientation output,
Hall associativity,
HN sector descent,
KS A_2 holonomy,
conifold quantum pentagon,
C^3 toric collapse,
conifold toric collapse,
Igusa normalization,
master C3 / conifold / K3xE_boundary certificates.
```

The Igusa certificate enforces the square-root normalization:

```tex
f(0,-1)=1,\qquad f(0,0)=10,\qquad f(0,1)=1,\qquad f(0,0)/2=5.
```

It also guards the false identity that would confuse
`\phi_{0,1}`-coefficients with the Fourier--Jacobi coefficients of
`\Delta_5`.

## Final Ledger

There is no remaining untyped foundational gap.

The residual named problems are now the derived zero fibers of one
finite-first solution object:

```tex
Sol^{BPS}_{<=N,<=R}
 =
D_{<=N,<=R}
 x^h_{V_Ex + V_glue + V_rad + V_theta + V_hCS}
 {0},
\qquad
Sol^{BPS}=\varprojlim_{N,R}Sol^{BPS}_{<=N,<=R}.
```

Its equations are `o_Ex=0`, `o_glue=0`, the full Hall--Borcherds
radical vector `o_rad=0`, the package-indexed theta vector
`o_theta_pkg=0`, and the total hCS vector
`Omega_hCS,Hall=0`.  The BMS compact non-toric class gives an actual
point.  The quintic, Schoen, raw `K3 x E`, comparison-theta, and named
hCS problems are closed substacks; they become actual points only after
their obstruction coordinates are computed from the named geometry and
vanish.

The seven named extension lanes are resolved as exact certificates,
radical quotients, comparison cocycles, or obstruction complexes in:

```text
notes/bps_positive_geometry_total_resolution_20260424/seven_extension_resolution_20260424.md
chapters/theory/bps_positive_geometry_closure.tex
compute/lib/bps_positive_truncation.py
compute/lib/bps_positive_remaining_gates.py
compute/tests/test_bps_positive_truncation.py
compute/tests/test_bps_positive_remaining_gates.py
```

```tex
compact non-toric existence:
  BMS data-realized compact point constructed;

K3 x E Hall--BKM:
  Igusa denominator quotient theorem proved; the raw Hall theorem is
  the seven-coordinate radical zero fiber;

hCS-to-Hall:
  fourteen-coordinate construction/descent zero fiber defined, with
  relative orientation coordinate o_or^rel;

theta enhancement:
  intrinsic finite Hall theta package proved; external packages are
  package-indexed comparison zero fibers;

finite oracle:
  truncation and remaining-gates oracles implemented and tested.
```

What remains after this closure is not a gap in the definition or
theory.  It is the production of actual points in the named closed
substacks: quintic `ExCert`, Schoen local-to-compact gluing, raw
`K3 x E` radical-zero, comparison of Hall theta bases with external
packages, and compact hCS-to-Hall localization.  These are finite
witness gates inside the object, not missing foundations.
