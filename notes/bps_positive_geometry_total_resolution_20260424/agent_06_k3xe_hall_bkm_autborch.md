# Worker 06: K3 x E Hall--Borcherds Bridge and AutBorch

Date: 2026-04-24.

Assigned obligation.  Solve obligation 6 and the automorphic part of
obligation 7 for the chambered BPS positive geometry:

```tex
CoHA^{or}_{crit}(K3 x E)
  -> U(Y^+(g_{Delta_5}))_{num}
```

and construct the functorial target

```tex
AutBorch:
K_0(BPS^{mot,prim}) -> automorphic denominators,
\qquad
AutBorch(phi_{0,1})=Delta_5.
```

The monotone repair is not to weaken the K3 x E theorem to a character
identity.  The stronger object is the automorphic radical quotient of
the sector-completed oriented Hall algebra, equipped with its primitive
motivic seed, Lorentzian chamber, orientation character, Borcherds
denominator, Cartan/negative-half extension, Hall pairing, and scalar
square.

Local anchors.

```text
notes/master_synthesis_chambered_bps_positive_geometry_20260424.md:232
notes/master_synthesis_chambered_bps_positive_geometry_20260424.md:981
notes/master_synthesis_chambered_bps_positive_geometry_20260424.md:1206
notes/bps_positive_geometry_total_resolution_20260424/integration_spine.md:62
chapters/theory/cy3_chain_level_bridge.tex:1530
chapters/theory/cy3_chain_level_bridge.tex:2260
chapters/examples/k3e_bkm_chapter.tex:13089
chapters/examples/k3e_bkm_chapter.tex:13143
/Users/raeez/igusa-cusp-form/proj.tex:68
/Users/raeez/igusa-cusp-form/proj.tex:418
/Users/raeez/igusa-cusp-form/proj.tex:782
/Users/raeez/igusa-cusp-form/proj.tex:1216
/Users/raeez/igusa-cusp-form/proj.tex:1391
```

## 1. The Strong Object

Let

```tex
X = K3 x E.
```

The Hall--Borcherds bridge is the tuple

```tex
HB^+_{K3,E}
 =
(\mathcal H^{mot}_{K3,E,S,o},
 \mathbb U^{mot}_{K3},
 \Gamma_{BPS},
 \Gamma_eff,
 alpha,
 Lambda^{2,1}_{II},
 Poly_{II},
 rho,
 nu_{Delta_5},
 \mathfrak g_{Delta_5}^+,
 Rad_{Aut},
 \Psi^+_{HB},
 AutBorch).
```

Here

```tex
\mathcal H^{mot}_{K3,E,S,o}
```

is the sector-completed oriented motivic critical Hall algebra of
`K3 x E` in the Igusa chamber `S`.  The primitive seed is a graded
motivic class

```tex
\mathbb U^{mot}_{K3}
 =
\bigoplus_{n >= 0,\; l in Z}\mathbb U^{mot}_{n,l},
```

with Hodge/Euler supertrace

```tex
STr(\mathbb U^{mot}_{n,l})=f(n,l),
\qquad
phi_{0,1}(\tau,z)=sum_{n,l} f(n,l)q^n r^l.
```

The seed is a primitive BPS motive, not a chosen half of an actual K3
Hilbert space.  The exact theorem-grade normalization is

```tex
Z_{K3}=2phi_{0,1},
\qquad
phi_{0,1}=r^{-1}+10+r+O(q),
\qquad
f(0,0)/2=5.
```

The BPS charge lattice and chamber are

```tex
\Gamma_{BPS}=Z^3,\qquad \gamma=(n,l,m),
```

```tex
\Gamma_eff =
{(n,l,m): m>0,\ n>=0,\ l in Z}
\cup {(n,l,0): n>0,\ l in Z}
\cup {(0,l,0): l<0}.
```

The chamber is a Harder--Narasimhan sector on the Hall side and the
lexicographic Borcherds product chamber on the automorphic side.  It is
not auxiliary notation: it is the positivity datum.

The Lorentzian degree map is

```tex
alpha(n,l,m)=2n f_2 - l f_3 + 2m f_{-2}
             in Lambda^{2,1}_{II},
```

and the BPS pairing is transported by

```tex
<gamma,gamma'>_{BPS}
 =
2(nm' + n'm)-ll',
\qquad
(alpha(gamma),alpha(gamma'))=-2<gamma,gamma'>_{BPS}.
```

The real simple roots are

```tex
delta_1=2f_2-f_3,\qquad
delta_2=2f_{-2}-f_3,\qquad
delta_3=f_3,
```

with Gram matrix

```tex
[[ 2,-2,-2],
 [-2, 2,-2],
 [-2,-2, 2]].
```

The finite-volume Weyl chamber is

```tex
Poly_{II} =
{x : (x,delta_i) <= 0,\ i=1,2,3}/R_{>0},
```

and the Weyl vector is

```tex
rho = (delta_1+delta_2+delta_3)/2
    = f_2 - (1/2)f_3 + f_{-2},
\qquad
(rho,delta_i)=-1.
```

The orientation character is the Maass character

```tex
epsilon_det = nu_{Delta_5},
\qquad
Delta_5|_5 g = nu_{Delta_5}(g)Delta_5,
\qquad
nu_{Delta_5}(s_{delta_i})=-1.
```

This is the automorphic realization of the determinant-line orientation
on the Hall side.  It is not optional sign decoration: it is the square
root datum whose scalar square removes the character.

## 2. Primitive Seed to Hall Fock Object

For each effective BPS charge define the one-particle Hall primitive
class

```tex
\mathcal V_\gamma^{mot}
 =
\mathbb U^{mot}_{nm,l},
\qquad
\gamma=(n,l,m) in Gamma_eff,
```

so that

```tex
STr(\mathcal V_{n,l,m}^{mot})=f(nm,l).
```

Let

```tex
\mathcal P^{mot}_{K3,E}
 =
\widehat{\bigoplus}_{\gamma in Gamma_eff}
\mathcal V_\gamma^{mot}
```

be the primitive sector inside the completed Hall algebra.  The
second-quantized Hall Fock object is

```tex
\mathcal F(\mathcal P^{mot}_{K3,E})
 =
Sym(\mathcal P_{\bar 0}^{mot})
\otimes \wedge(\mathcal P_{\bar 1}^{mot}).
```

Its supercharacter is

```tex
sch \mathcal F(\mathcal P^{mot}_{K3,E})
 =
prod_{\gamma in Gamma_eff}
(1-x^\gamma)^{-STr(\mathcal V_\gamma^{mot})}
 =
prod_{(n,l,m) in Gamma_eff}
(1-q^n r^l s^m)^{-f(nm,l)}.
```

The Hall determinant is the inverse Fock character with the vacuum
line:

```tex
\mathcal D_X(Z)
 =
64 q^{1/2}r^{1/2}s^{1/2}
prod_{(n,l,m) in Gamma_eff}
(1-q^n r^l s^m)^{f(nm,l)}.
```

Borcherds--Gritsenko--Nikulin give the theorem-grade identity

```tex
\mathcal D_X(Z)=Delta_5(Z).
```

Thus the character-level Hall statement is not merely
`Delta_5` exists.  It is:

```tex
sch \mathcal F(\mathcal P^{mot}_{K3,E})
 =
64 q^{1/2}r^{1/2}s^{1/2} Delta_5(Z)^{-1}.
```

The positive-half theorem target must recover this character from a
Hall primitive algebra before taking the Drinfeld double.

## 3. The Automorphic Radical Quotient

The denominator identity determines a canonical numerical quotient of
the sector-completed Hall algebra.

Define the automorphic Hall integration map

```tex
Int_{Aut}:
\mathcal H^{mot}_{K3,E,S,o}
  -> \widehat{T}_{Gamma_eff}^{Aut}
```

by

```tex
[M_\gamma,\phi^{vc}_{o,\gamma}]
  -> STr(M_\gamma,\phi^{vc}_{o,\gamma}) x^\gamma
```

followed by the Lorentzian substitution

```tex
x^\gamma=q^n r^l s^m
        =exp(-pi i(alpha(gamma),z)).
```

Let `Rad_{Aut}` be the largest closed two-sided Hall ideal killed by all
automorphic denominator matrix coefficients:

```tex
Rad_{Aut}
 =
\cap_{\ell in DenCoeff(Delta_5)}
ker(\ell circ Int_{Aut}).
```

This is stronger than asserting an unstructured map of characters.  It
produces a typed algebra:

```tex
\mathcal H^{Aut,+}_{K3,E}
 =
\mathcal H^{mot}_{K3,E,S,o}/Rad_{Aut}.
```

The positive-half Hall--Borcherds theorem target is the isomorphism

```tex
\Psi^+_{HB}:
\mathcal H^{Aut,+}_{K3,E}
  \xrightarrow{\sim}
\widehat{U}(\mathfrak g_{Delta_5}^+)
```

of completed `Gamma_eff`-graded algebras with the following properties:

```tex
\Psi^+_{HB}(\operatorname{Prim}_\gamma)
  subset
(\mathfrak g_{Delta_5})_{alpha(gamma)},
```

```tex
sdim(\operatorname{Prim}_\gamma)
 =
smult(alpha(gamma))
 =
f(nm,l),
```

and the Hall PBW filtration is carried to the PBW filtration on the
positive enveloping algebra.

This is the required upgrade from identity of products to positive-half
construction.  The character identity follows by taking the PBW
supercharacter of `\widehat U(\mathfrak g_{Delta_5}^+)`; it is no
longer the theorem statement.

## 4. The BKM Positive Half

The generalized Borcherds--Kac--Moody superalgebra
`\mathfrak g_{Delta_5}` is specified by its denominator data:

```tex
den(\mathfrak g_{Delta_5})
 =
e^{-2pi i(rho,z)}
prod_{\alpha in R_+}
(1-e^{-2pi i(alpha,z)})^{smult(alpha)}
 =
64^{-1}Delta_5(2Z).
```

The root supermultiplicity is

```tex
smult(alpha)
 =
dim(\mathfrak g_{\alpha,\bar 0})
 -
dim(\mathfrak g_{\alpha,\bar 1}),
```

and the K3 x E charge formula is exact:

```tex
smult(alpha(n,l,m))=f(nm,l).
```

The positive half is

```tex
\mathfrak g_{Delta_5}^+
 =
\bigoplus_{\alpha in R_+}
(\mathfrak g_{Delta_5})_\alpha,
\qquad
\widehat U(\mathfrak g_{Delta_5}^+)
 =
\prod_{\beta in Q_+}
U(\mathfrak g_{Delta_5}^+)_\beta.
```

The real simple roots are `delta_1,delta_2,delta_3`; the imaginary
simple-root content is encoded by the Fourier seed

```tex
m(a)=-(1/64)f(n,l,m),
\qquad
a=(n-1)f_2-(l-1)(1/2)f_3+(m-1)f_{-2},
```

with `m(0)=-1` fixing the Weyl term.  This is the part that character
identities alone cannot supply: the positive half must remember which
Fourier coefficients are primitive generators, which are PBW monomials,
and how the real-root Serre relations act on them.

## 5. Cartan, Negative Half, Pairing

The positive-half construction is kept separate from the double.  The
double data are:

```tex
\mathfrak h_{Delta_5}
  =
(\widetilde H(K3,Z)/U) \oplus Z\lambda_{Leech},
\qquad
rk \mathfrak h_{Delta_5}=22+1=23,
```

```tex
\mathfrak g_{Delta_5}^-
 =
\omega(\mathfrak g_{Delta_5}^+),
```

where `\omega` is the Chevalley anti-involution compatible with the
orientation character, and

```tex
(-,-)_{Hall,Borch}:
\mathcal H^{Aut,+}_{K3,E}
  \widehat\otimes
\mathcal H^{Aut,-}_{K3,E}
  -> C((q,r,s))
```

is the continuous Hall pairing whose radical is exactly `Rad_{Aut}` on
the positive side and its opposite on the negative side.

The full double theorem target is therefore

```tex
D(\mathcal H^{Aut,+}_{K3,E})
  \simeq
\widehat U(\mathfrak g_{Delta_5})
```

only after Cartan, coproduct, negative half, continuous pairing, radical
quotient, and completion are supplied.  Worker 06 supplies the positive
half and the automorphic boundary functor; it records the double data so
that no one mistakes the positive half for the full algebra.

## 6. AutBorch

Define the source category `BPSSeed^{mot}_{Aut}` as follows.  An object
is

```tex
\mathfrak S =
(M^{mot}_{prim},
 Gamma,
 Gamma_eff,
 I,
 alpha,
 Lambda,
 Poly,
 rho,
 epsilon,
 J,
 o)
```

where:

```tex
M^{mot}_{prim} = completed direct sum of primitive BPS motives,
Gamma = charge lattice with integral BPS pairing,
Gamma_eff = strict effective chamber,
I: Gamma_eff -> Z_{\ge 0} x Z = coefficient-index map,
alpha: Gamma -> Lambda = Lorentzian degree map,
Poly = finite-volume Weyl chamber,
rho = Weyl vector,
epsilon = determinant/orientation character,
J(M^{mot}_{prim}) = weak Jacobi seed,
o = orientation data compatible with epsilon.
```

Morphisms preserve the charge lattice, chamber, orientation character,
Jacobi realization, and Lorentzian degree map.

The functor

```tex
AutBorch:
BPSSeed^{mot}_{Aut}
  -> DenBKM
```

where `DenBKM` is the category of automorphic BKM denominator packages
with morphisms given by isometric chamber embeddings preserving the
multiplier, Weyl vector, coefficient-index map, and denominator
normalization.

sends `\mathfrak S` to the automorphic denominator package

```tex
AutBorch(\mathfrak S)
 =
(F_{\mathfrak S},
 nu_{\mathfrak S},
 \mathfrak g_{\mathfrak S},
 \mathfrak g_{\mathfrak S}^+,
 den(\mathfrak g_{\mathfrak S}),
 Z_{\mathfrak S}^{square}).
```

The construction is:

```tex
M^{mot}_{prim}
  --J-->
phi_{\mathfrak S}(\tau,z)=sum c(n,l)q^n r^l
  --Borch-->
F_{\mathfrak S}(Z)
  =
v_{\mathfrak S}(Z)
prod_{\gamma in Gamma_eff}
(1-x^\gamma)^{c(I(\gamma))}
```

with `v_{\mathfrak S}` the Weyl/vacuum factor determined by `rho`.
The BKM root spaces are fixed by

```tex
smult_{\mathfrak S}(alpha(\gamma))=c(I(\gamma)),
```

and

```tex
den(\mathfrak g_{\mathfrak S})
 =
F_{\mathfrak S}(2Z)/F_{\mathfrak S,lead}.
```

For the K3 x E seed,

```tex
\mathfrak S_{K3,E}
 =
(\mathbb U^{mot}_{K3},
 Z^3,
 Gamma_eff,
 I(n,l,m)=(nm,l),
 alpha(n,l,m)=2n f_2-l f_3+2m f_{-2},
 Lambda^{2,1}_{II},
 Poly_{II},
 rho,
 nu_{Delta_5},
 phi_{0,1},
 o_{K3,E})
```

one obtains exactly

```tex
AutBorch(\mathfrak S_{K3,E})
 =
(Delta_5,
 nu_{Delta_5},
 \mathfrak g_{Delta_5},
 \mathfrak g_{Delta_5}^+,
 64^{-1}Delta_5(2Z),
 C_square Delta_5^{-2}).
```

The theorem-grade value is

```tex
AutBorch(phi_{0,1})=Delta_5.
```

The stronger Hall value is

```tex
AutBorch(\mathcal P^{mot}_{K3,E})
 =
(\widehat U(\mathfrak g_{Delta_5}^+),
  den(\mathfrak g_{Delta_5}),
  Z^X_square).
```

## 7. Normalization Ledger

The three normalizations are fixed and must remain separate:

```tex
D_5
 =
64^{-1}Delta_5
 =
q^{1/2}r^{1/2}s^{1/2}
prod_{\gamma in Gamma_eff}
(1-q^n r^l s^m)^{f(nm,l)}.
```

```tex
\mathcal D_X
 =
Delta_5.
```

```tex
den(\mathfrak g_{Delta_5})
 =
D_5(2Z)
 =
64^{-1}Delta_5(2Z).
```

The scalar square is

```tex
Z^X_square=C_square Delta_5^{-2}.
```

In the Oberdieck--Pixton primitive reduced normalization,

```tex
chi_{10}^{OP}=4096^{-1}Delta_5^2,
\qquad
Z^X_{OP}=-4096 Delta_5^{-2}.
```

Thus

```tex
Z^{ch}_{BPS}=Delta_5^{-1},
\qquad
(Z^{ch}_{BPS})^2=Z^X_square/C_square.
```

This is the square-root principle.  The Hall positive half and the
chiral determinant see `Delta_5`; the full scalar protected index sees
`Delta_5^2`.

## 8. Theorem Package

### Theorem A: Automorphic Positive-Half Quotient

Assume the following strong data for `X=K3 x E`.

```tex
(H1)  P^{BPS,motloc}_{sigma,S,o,T_eq}(X) exists in the Igusa chamber.
(H2)  The primitive Hall supertrace equals the K3 half-index seed:
      STr Prim_{n,l,m}=f(nm,l).
(H3)  The Hall orientation character transports to nu_{Delta_5}.
(H4)  The Lorentzian degree map alpha is Hall-additive and carries the
      Euler/BPS pairing to -1/2 of the Lambda^{2,1}_{II} form.
(H5)  The Hall product is compatible with Borcherds primitive/PBW
      decomposition after quotient by Rad_{Aut}.
(H6)  Int_{Aut} is a continuous Hall algebra homomorphism to the
      automorphic quantum torus and Rad_{Aut} is a closed Hopf ideal.
```

Then the automorphic radical quotient is the completed BKM positive
half:

```tex
\mathcal H^{mot}_{K3,E,S,o}/Rad_{Aut}
  \cong
\widehat U(\mathfrak g_{Delta_5}^+)
```

as a completed `Gamma_eff`-graded algebra, with

```tex
sdim Prim_\gamma
 =
smult(alpha(\gamma))
 =
f(nm,l).
```

The PBW supercharacter is

```tex
sch \widehat U(\mathfrak g_{Delta_5}^+)
 =
prod_{\gamma in Gamma_eff}
(1-q^n r^l s^m)^{-f(nm,l)}.
```

### Theorem B: AutBorch at the K3 x E Seed

For the motivic primitive seed whose Jacobi realization is
`phi_{0,1}`, AutBorch gives

```tex
AutBorch(phi_{0,1})=Delta_5,
\qquad
den(\mathfrak g_{Delta_5})=64^{-1}Delta_5(2Z),
\qquad
smult(alpha(n,l,m))=f(nm,l).
```

This is theorem-grade in the automorphic/Borcherds lane by the
Borcherds--Gritsenko--Nikulin product and denominator identity.

### Theorem C: Scalar-Square Compatibility

The automorphic positive half is compatible with the protected scalar
square:

```tex
\mathcal D_X=Delta_5,
\qquad
Z^{ch}_{BPS}=Delta_5^{-1},
\qquad
Z^X_square=C_square Delta_5^{-2}.
```

In the Oberdieck--Pixton primitive reduced scope,

```tex
Z^X_{OP}=-4096Delta_5^{-2}.
```

### Theorem D: Double Extension Criterion

If, in addition to Theorem A, the Cartan rank-23 extension, negative
half, coproduct, continuous Hall pairing, radical quotient, and
completion are supplied, then the positive-half isomorphism upgrades to

```tex
D(\mathcal H^{Aut,+}_{K3,E})
  \cong
\widehat U(\mathfrak g_{Delta_5}).
```

This is not used to prove the positive-half theorem.  It is the next
monotone target.

## 9. Proof Spine

Step 1.  The motivic primitive seed realizes the K3 weak Jacobi form:

```tex
J(\mathbb U^{mot}_{K3})=phi_{0,1}
=sum f(n,l)q^n r^l.
```

Step 2.  Sector completion along `Gamma_eff` turns the primitive seed
into Hall one-particle charges:

```tex
\mathcal V_{n,l,m}^{mot}=\mathbb U^{mot}_{nm,l}.
```

The Fock supercharacter and determinant are formal consequences of
super linear algebra:

```tex
sch F(V)=prod(1-x^\gamma)^{-sdim V_\gamma},
\qquad
sdet_V(1-x)=prod(1-x^\gamma)^{sdim V_\gamma}.
```

Step 3.  Borcherds--Gritsenko--Nikulin identify the determinant with
the Igusa square root:

```tex
64 q^{1/2}r^{1/2}s^{1/2}
prod_{\Gamma_eff}
(1-q^n r^l s^m)^{f(nm,l)}
=Delta_5.
```

Step 4.  The denominator polarization changes variables by

```tex
alpha(n,l,m)=2n f_2-l f_3+2m f_{-2},
\qquad
q^n r^l s^m=exp(-pi i(alpha(n,l,m),z)).
```

After `Z -> 2Z`, the product is the Weyl--Kac--Borcherds denominator:

```tex
den(\mathfrak g_{Delta_5})
 =
e^{-2pi i(rho,z)}
prod_{\alpha in R_+}
(1-e^{-2pi i(alpha,z)})^{smult(alpha)}
 =
64^{-1}Delta_5(2Z).
```

Step 5.  Comparing exponents gives the root-superdimension formula:

```tex
smult(alpha(n,l,m))=f(nm,l).
```

Step 6.  The Hall quotient by `Rad_{Aut}` kills exactly the classes
invisible to every automorphic denominator coefficient.  The quotient
therefore has primitive superdimensions equal to the BKM root
superdimensions and PBW character equal to the BKM positive-half
character.  Hypothesis H5 is the bracket-level strengthening: it
asserts that the Hall commutator, real-root Serre relations, and
imaginary primitive generators match the Borcherds presentation, not
only its character.

Step 7.  The orientation character transports the Hall determinant-line
square root to the Maass multiplier:

```tex
epsilon_o -> nu_{Delta_5}.
```

Consequently `Delta_5` is character-valued and its square
`Delta_5^2=Delta_{10}` is scalar.

Step 8.  The full protected scalar index is the scalar square of the
chiral inverse:

```tex
Z^X_square=C_square(Delta_5^{-1})^2.
```

This proves the compatibility of Hall positive half, BKM denominator,
and Igusa physics without identifying the positive half with the
Drinfeld double.

## 10. Computational and Formal Oracles

The finite truncation oracle for this bridge is:

```tex
HB^+_{<=N,<=R}(K3,E)
 =
(\Gamma_eff^{<=N,<=R},
 f(nm,l),
 alpha,
 epsilon_o,
 Rad_{Aut}^{<=N,<=R},
 PBW^{<=N,<=R}).
```

It must check:

```tex
1. phi_{0,1} coefficient normalization:
   r^{-1}+10+r+q(10r^{-2}-64r^{-1}+108-64r+10r^2)+...

2. chamber membership:
   gamma in Gamma_eff iff alpha(gamma) lies in the chosen positive cone.

3. pairing transport:
   (alpha(gamma),alpha(gamma'))=-2<gamma,gamma'>_{BPS}.

4. orientation:
   epsilon_o(s_{delta_i})=nu_{Delta_5}(s_{delta_i})=-1.

5. determinant truncation:
   [<=N,<=R] log Delta_5 =
   log(64q^{1/2}r^{1/2}s^{1/2})
   + sum_{\Gamma_eff}^{<=N,<=R} f(nm,l)log(1-q^n r^l s^m).

6. denominator truncation:
   den(\mathfrak g_{Delta_5})^{<=N,<=R}
   =64^{-1}Delta_5(2Z)^{<=N,<=R}.

7. PBW character:
   sch PBW(\mathfrak g^+)^{<=N,<=R}
   =prod_{\Gamma_eff}^{<=N,<=R}(1-x^\gamma)^{-f(nm,l)}.

8. scalar square:
   (Delta_5^{-1})^2=Delta_{10}^{-1}.
```

These tests do not prove the bracket.  They force every numerical
normalization that a bracket theorem can use.

## 11. Surviving Obstruction

The remaining non-character obstruction is precise:

```tex
o_{HB}^{bracket}
 in
H^2_{cont}
(
 \operatorname{Prim}(\mathcal H^{Aut,+}_{K3,E}),
 \operatorname{Prim}(\mathcal H^{Aut,+}_{K3,E})
)
```

measures the failure of the Hall commutator on primitive classes to
satisfy the Borcherds real-root Serre relations and imaginary
primitive-generator relations after the `alpha` collapse.

The monotone target is:

```tex
o_{HB}^{bracket}=0
```

together with a choice of null-homotopy compatible with Hall
associativity, Thom--Sebastiani, and `nu_{Delta_5}` orientation
transport.  Once this vanishes, Theorem A is no longer a character
shadow: it is the Hall/BKM positive-half construction.

## 12. Final Form

For `K3 x E`, the positive geometry has the automorphic boundary

```tex
primitive K3 motive
  -> phi_{0,1}
  -> Gamma_eff
  -> alpha(Gamma_eff) subset Lambda^{2,1}_{II}
  -> Delta_5
  -> g_{Delta_5}^+
  -> den(g_{Delta_5})
  -> Z^X_square.
```

The toric positive geometry is a rational-polyhedral Hall cone.  The
K3 x E boundary is a Lorentzian Hall--Borcherds chamber.  The
positive-half construction is the automorphic radical quotient of the
oriented critical Hall algebra:

```tex
CoHA^{or}_{crit}(K3 x E)^{wedge}_{S}/Rad_{Aut}
  =
\widehat U(\mathfrak g_{Delta_5}^+).
```

The determinant is

```tex
\mathcal D_X=Delta_5,
```

the denominator is

```tex
den(\mathfrak g_{Delta_5})=64^{-1}Delta_5(2Z),
```

the root supermultiplicity is

```tex
smult(alpha(n,l,m))=f(nm,l),
```

and the protected scalar square is

```tex
Z^X_square=C_square Delta_5^{-2}.
```

This is the strongest coherent construction target currently forced by
the Igusa manuscript, the local K3 x E chapters, and the chambered BPS
positive-geometry synthesis.
