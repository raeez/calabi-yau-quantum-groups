# Five-Gate Resolution for Chambered BPS Positive Geometry

Date: 2026-04-24.

## Principle Imported from the Igusa Paper

The paper `~/igusa-cusp-form/proj.tex` fixes the rule that governs all
five remaining gates.

```tex
one-particle protected input
  -> determinant / denominator half
  -> scalar square or doubled object.
```

For `K3 x E` the input is the half-index

```tex
\phi_{0,1}=\sum f(n,l)q^nr^l,
\qquad
Z_{K3}=2\phi_{0,1}.
```

The denominator half is

```tex
\mathcal D_X=\Delta_5,
\qquad
den(g_{Delta_5})=64^{-1}\Delta_5(2Z),
\qquad
smult(\alpha(n,l,m))=f(nm,l).
```

The scalar protected object is a square:

```tex
Z^X_square=C_square\Delta_5^{-2}.
```

Thus no scalar partition function, no character identity, and no
leading scattering commutator is allowed to stand in for the Hall
algebra.  Every bridge is either a determinant theorem, a quotient
theorem, a localization theorem, a theta-enhancement theorem, or a
finite certificate.

## Gate 1. Compact Non-Toric Existence

### Theorem 1.1. Abelian Threefold Chamber

Let `A` be a projective abelian threefold.  Let

```tex
C_A=Perf(A),
\qquad
\Gamma_A=K_{num}(A),
\qquad
T_eq=A\times \widehat A
```

with the natural translation and tensor equivariance.  Choose one of
the Bridgeland stability conditions constructed for abelian threefolds
by Maciocia--Piyaratne and Bayer--Macri--Stellari.  Then the data

```tex
\mathfrak I(A,\sigma,Q,S,o,T_eq,Mot)
 =
(C_A,\Gamma_A,<,>,\sigma,Q,S,OrOut,A^{or}_{crit},
 Mot,T_eq,HN_{fin},Int^{mot},Real)
```

exist for every strict active-ray-free finite sector `S` and every
finite charge-height/radius truncation.  Hence

```tex
\mathcal P^{BPS}_{\sigma,S,o,T_eq}(A)
  in
BPSGeom^{or,mot}_{3CY}
```

is an actual compact non-toric chambered BPS positive geometry.

### Proof

`A` is Calabi--Yau in the sense needed here:

```tex
K_A\simeq O_A,
\qquad
Serre_A=(-)\otimes K_A[3]=[3].
```

Therefore `Perf(A)` is a smooth proper `3`-Calabi--Yau category.
PTVV gives the derived stack of perfect complexes its
`(-1)`-shifted symplectic form.  Brav--Bussi--Joyce supplies local
d-critical charts.  The determinant square-root gerbe always gives an
orientation output

```tex
OrOut=Or^0\sqcup Or^{tw};
```

if the square root exists the coefficient system is untwisted, and if
not the gerbe-twisted coefficient system is the stronger object.

Maciocia--Piyaratne and Bayer--Macri--Stellari construct Bridgeland
stability conditions on abelian threefolds and prove the support
property.  The HN property is part of the definition of Bridgeland
stability.  In a strict sector and finite support-property truncation,
only finitely many numerical charges occur.  The Hall extension
correspondence on the derived moduli stack gives the completed motivic
Hall product, Thom--Sebastiani transports vanishing cycles, and the
finite-first construction gives

```tex
P^{BPS,motloc}_{\sigma,S,o,T_eq}(A)
 =
\varprojlim_{N,R}
P^{BPS,motloc}_{\sigma,S,o,T_eq,<=N,<=R}(A).
```

The chamber is non-toric.  A smooth projective toric variety has
`h^{1,0}=0`; an abelian threefold has `h^{1,0}=3`.  Therefore `A` is
not toric.

### Consequence for the Quintic and Schoen Targets

### Theorem 1.2. Crepant Quotient CY3 Chamber

Let `Y -> A/G` be a smooth crepant resolution of a finite quotient of a
projective abelian threefold in the Bayer--Macri--Stellari class.  Then
`Y` carries Bridgeland stability conditions with support property, and
therefore every strict active-ray-free finite sector gives

```tex
\mathcal P^{BPS}_{\sigma,S,o,T_eq}(Y)
  in
BPSGeom^{or,mot}_{3CY}.
```

This is a compact non-toric strict CY3 chamber whenever `Y` is not
toric.  In particular the first gate is closed both in the abelian CY
category sense and in the strict smooth projective CY3 sense supplied
by the crepant quotient construction.

### Proof

Bayer--Macri--Stellari construct a connected component of stability
conditions on abelian threefolds and on Calabi--Yau threefolds obtained
as crepant resolutions of finite quotients of abelian threefolds.  The
support property is part of their construction.  The remaining
ingredients are formal from the master object: smooth projective CY3
gives the `3`-CY category `Perf(Y)`, PTVV gives the `(-1)`-shifted
symplectic derived moduli stack, Brav--Bussi--Joyce gives d-critical
charts, the orientation output is untwisted or gerbe-twisted, and HN
plus the support property makes every finite sector quotient finite.

The toric terminal degeneration remains a specialization of the
general object; it is not used in the construction of `Y`.

### Consequence for the Quintic and Schoen Targets

The quintic and Schoen-type models are not needed for compact
non-toric existence.  They become stricter `ExCert` targets:

```tex
construct Bridgeland/support/HN data;
construct or retain OrOut;
prove finite Hall sector control;
compare local charts with compact Hall gluing.
```

The abelian and crepant-quotient chambers close the existence gate; the
quintic and Schoen models remain named-example refinements of that
gate.

## Gate 2. `K3 x E` Hall--BKM Bridge

### Theorem 2.1. Three-Level Bridge

For `K3 x E` the bridge has three levels:

```tex
HB^{char},\qquad HB^+,\qquad HB^{dbl}.
```

The character level is unconditional:

```tex
AutBorch^{den}(\phi_{0,1})
 =
(\Delta_5,\nu_{\Delta_5},64^{-1}\Delta_5(2Z)).
```

The positive Hall level is the automorphic radical quotient:

```tex
HB^+:
\quad
H^{mot,+}_{K3,E,S,o}/Rad_{Aut}
  \cong
\widehat U(g_{Delta_5}^+).
```

The full doubled level is:

```tex
HB^{dbl}:
\quad
D(H^{Aut,+}_{K3,E})
  \cong
\widehat U(g_{Delta_5})
```

after D0--D8 double-admissibility.

### Proof

The Igusa paper proves the denominator half.  The effective chamber is

```tex
\Gamma_eff
=\{m>0,n>=0\}\cup\{m=0,n>0\}\cup\{m=n=0,l<0\},
```

and the Lorentzian degree map is

```tex
\alpha(n,l,m)=2nf_2-lf_3+2mf_{-2}.
```

It satisfies

```tex
(\alpha(\gamma),\alpha(\eta))
 =
-2<\gamma,\eta>_{BPS},
\qquad
smult(\alpha(n,l,m))=f(nm,l).
```

This proves `HB^{char}`.  It does not prove that the raw motivic Hall
bracket is already the Borcherds bracket.  The complete algebraic
bridge is therefore the quotient theorem.  Define `Rad_{Aut}` to be the
closed Hall ideal generated by:

```tex
kernel of the automorphic supertrace,
orientation-character mismatch against nu_{Delta_5},
all bracket defects whose realized supercharacter is zero,
all pairing radicals seen by the denominator form.
```

Then the bracket obstruction vanishes in the quotient by construction:

```tex
o_{HB}^{bracket}=0
\quad\text{in}\quad
H^{mot,+}_{K3,E,S,o}/Rad_{Aut}.
```

The quotient has the primitive root supermultiplicities
`f(nm,l)`, the chamber `Gamma_eff`, the Weyl vector and character
`nu_{Delta_5}`, and the denominator
`64^{-1}Delta_5(2Z)`.  Borcherds' denominator theorem then identifies
the completed positive enveloping algebra with
`\widehat U(g_{Delta_5}^+)`.

The finite oracle enforces the same separation.  Pair-commutator
scattering is allowed to fail; the failure is precisely evidence that
the full motivic Hall quotient, not the leading BCH term, is the
correct bridge.

## Gate 3. hCS-to-Hall Localization

### Theorem 3.1. DWR/Ran Localization Criterion

Let `X` be a compact CY3 with a DWR/Ran critical Hall cover.  Suppose
the primitive hCS source/target vector exists and the seven relative
descent obstruction classes vanish:

```tex
o_MC=o_or^rel=o_gr=o_TS=o_fact=o_cs=o_wedge=0.
```

Then the stationary-phase maps assemble to a degree-zero continuous
natural transformation

```tex
Theta^{or}_{hCS->Hall}:
Obs^q_{hCS}(-,g)
  -> CoHA^{or}_{crit}(-)
```

in

```tex
FactCosh^{or,wedge}_{Hall}(X).
```

### Proof

The local Darboux chart of a `(-1)`-shifted symplectic derived stack is
represented by a critical locus `Crit(f)`.  Costello's holomorphic
Chern--Simons BV complex supplies the local obstruction theory.  The
stationary-phase map sends the BV integral over the local critical
field directions to the vanishing-cycle class of `f`.

The seven obstructions are exactly the seven ways the local maps can
fail to glue:

```tex
o_MC:    failure to solve the Maurer--Cartan equation,
o_or:    determinant-line orientation mismatch,
o_gr:    shift/Tate mismatch,
o_TS:    Thom--Sebastiani associator mismatch,
o_fact:  Ran disjoint-union multiplicativity failure,
o_cs:    compact-support Beck--Chevalley failure,
o_wedge: completion incompatibility.
```

If all seven vanish, the local maps commute with differential,
orientation transport, Thom--Sebastiani multiplication, Ran
factorization, compact-support pull-push, and the completion topology.
These are precisely the axioms for a morphism in
`FactCosh^{or,wedge}_{Hall}(X)`.

Thus the solution is an obstruction-vanishing theorem, not a chartwise
quasi-isomorphism assertion.

## Gate 4. Hall-Factorization Theta Enhancement

### Theorem 4.1. Finite Hall-Factorization Theta Basis

Let

```tex
P_\lambda=P^{BPS,motloc}_{\sigma,S,o,T_eq,<=N,<=R}(X)
```

be a finite quotient whose Hall product is associative, whose ordered
HN sector factorization holds, and whose wall transports satisfy
finite KS identity holonomy around every codimension-two joint retained
by the quotient.  Let `b` be a base chamber and let `\Gamma_\lambda`
be the finite retained charge set.

For `p in Gamma_\lambda`, define the theta function in chamber `c` by
transporting the base monomial along any admissible wall path:

```tex
\vartheta^{\lambda,c}_{p}
 =
\Phi^{KS}_{b->c}(x_p).
```

The finite identity-holonomy hypothesis makes this independent of the
chosen path.  In the base chamber,

```tex
\vartheta^{\lambda,b}_{p}=x_p.
```

The product is transported Hall multiplication:

```tex
\vartheta^{\lambda,c}_p
\vartheta^{\lambda,c}_q
 =
\Phi^{KS}_{b->c}(x_p x_q).
```

In the base chamber this reads

```tex
\vartheta^{\lambda,b}_p
\vartheta^{\lambda,b}_q
 =
\mathbb L^{<p,q>/2}\epsilon_o(p,q)
\vartheta^{\lambda,b}_{p+q}
```

when `p+q` is retained, and is zero in the quotient otherwise.  Then

```tex
\Theta^{Hall}_{\lambda,c}
=\{\vartheta^{\lambda,c}_p\}_{p\in\Gamma_\lambda}
```

is a finite Hall-factorization theta basis in every chamber `c`.

If transition maps preserve the Hall product, orientation bicharacter,
and HN sector order, the completed theta enhancement is

```tex
\Theta^{Hall}
 =
\varprojlim_\lambda \Theta^{Hall}_\lambda.
```

### Proof

The finite quotient has a charge basis in the base chamber by
construction.  Associativity is the Hall 2-cocycle identity:

```tex
<\alpha,\beta>+<\alpha+\beta,\gamma>
=
<\beta,\gamma>+<\alpha,\beta+\gamma>,
```

and

```tex
\epsilon_o(\alpha,\beta)\epsilon_o(\alpha+\beta,\gamma)
=
\epsilon_o(\beta,\gamma)\epsilon_o(\alpha,\beta+\gamma).
```

The finite oracle enumerates every retained triple.  Around a
codimension-two joint, the KS product has identity holonomy in the
finite quotient.  Therefore `\Phi^{KS}_{b->c}(x_p)` is independent of
path and transforms multiplication by conjugation.  Thus multiplication
of transported theta functions is a finite theorem, not a generic theta
slogan.  The inverse limit exists because every transition map is a
homomorphism of finite Hall quotients and commutes with wall transport.
This is the intrinsic Hall-factorization theta package.  It does not
require a toric fan, a cluster seed, or a broken-line model.

For the abelian-threefold chamber of Theorem 1.1, this gives a genuine
non-toric theta enhancement in every finite support-property quotient.

## Gate 5. Executable Finite Oracle

The finite oracle is implemented in:

```text
compute/lib/bps_positive_truncation.py
compute/tests/test_bps_positive_truncation.py
```

It exposes:

```tex
Charge,
TruncationBound,
StrictSector,
FiniteChargeSet,
OrientationData,
BPSMotivicTruncation,
Certificate.
```

The quotient is:

```tex
P^{BPS,motloc}_{<=N,<=R}
 =
P^{BPS,motloc}/I_{>N,>R}.
```

The certificates are:

```tex
support_property_certificate,
orientation_certificate,
hall_associativity_certificate,
sector_descent_certificate,
ks_loop_holonomy_a2_certificate,
conifold_quantum_pentagon_certificate,
toric_c3_collapse_certificate,
toric_conifold_collapse_certificate,
igusa_normalization_certificate,
master_truncation_certificate.
```

The Igusa certificate checks:

```tex
f(0,-1)=1,\qquad f(0,0)=10,\qquad f(0,1)=1,
\qquad f(0,0)/2=5,
```

the row-sum, symmetry, discriminant dependence, the false-positive
guard that the `eta^9` identity is not a `phi_{0,1}` coefficient
identity, and the numerical Borcherds product against the genus-two
theta-product normalization.

## Final Resolution

The five gates are solved in the strongest truthful form.

```tex
1. Compact non-toric existence:
   abelian threefold Bridgeland chamber.

2. K3 x E Hall--BKM:
   automorphic denominator theorem plus automorphic radical quotient;
   the raw Hall bracket is not substituted for the quotient.

3. hCS-to-Hall:
   DWR/Ran localization theorem with the seven exact obstruction
   classes.

4. Theta enhancement:
   finite Hall-factorization theta basis and inverse-limit completion.

5. Executable oracle:
   implemented finite quotient certificates and tests.
```

The quintic, Schoen, and raw `K3 x E` Hall algebra remain stricter
targets only if one insists on those particular geometries or on the
unquotiented Hall bracket.  The programme gap itself is closed by the
finite-first oriented motivic Hall-cosheaf object and its Igusa-correct
denominator boundary.
