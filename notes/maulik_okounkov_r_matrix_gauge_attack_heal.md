# Cohomological stable envelopes and the actual rational comparison

This note concerns ordinary equivariant cohomology of the cotangent surface
T*P1. It corrects the earlier use of a slope-dependent dynamical construction
and a smooth threefold as inputs to that cohomological theory.
The original note is preserved exactly in
`reports/research/CY3-YANGIAN-054-2026-09-15/native-note.original.md`, SHA-256
`e82a15943401c9af4cfc5f494f0aba70f984d9a73b21c3f49d96e86aec8d0cef`.
The paragraph dispositions below record the semantic replacement.

## The construction and its parameters

For a torus acting on T*P1, let u be the tangent character at0 and let -h be
its symplectic character. The tangent characters are (u,-u-h) at0 and
(-u,u-h) at infinity. The fibre polarization is (-u,u).

The zero section and fibre classes restrict as

    Z=(-u-h,u-h), F0=(u,0), F∞=(0,-u).

The positive stable classes are Z+F∞ and -F∞. The negative stable classes
are -F0 and Z+F0. Their supports, diagonal Euler classes and degree bounds
characterize them uniquely. These are classes of actual curves.
In the integral cohomology basis (1,F0), their matrices are

    A+=[[-h,u],[-1,-1]], A-=[[0,u-h],[-1,-1]].

Consequently A-^{-1}A+ is

    R(u)=1/(u-h) [[u,-h],[-h,u]].

Adding the gauge-dimension0 and2 point components gives
R(u)=(uI-hP)/(u-h) on C² tensor C². It is the normalized intertwiner of the
specified two evaluation modules. The complete construction and proof are in
`chapters/examples/collision_surface_intertwiner.tex`.

There is no slope or Kähler parameter in this cohomological construction.
The source theorem uses a chamber and polarization. Changing polarization
changes R by conjugation with a diagonal sign matrix. A construction in
K-theory or elliptic cohomology has different inputs and must be formulated
and checked in that category before importing any additional parameter.

The primary source is Maulik–Okounkov, arXiv1211.1287v3, Theorem3.3.4,
Example4.1.2 and equation4.1. Its section4.1.3 states the polarization sign
conjugation. The stated rational operator is already present there.
Molev, arXivmath/0211288v1, Proposition2.2, Proposition2.3 and Theorem2.8
supply the comparison conventions for evaluation and coproduct.
No novelty is claimed for those constructions.

## Why the threefold example does not apply

A nondegenerate alternating form exists only in even dimension over C.
For a3x3 skew matrix M, det(M)=det(-M^T)=-det(M), hence det(M)=0.
The smooth threefold Tot(O(-1) plus O(-1) over P1) therefore is not a
holomorphic symplectic Nakajima variety. Its being Calabi–Yau does not repair
this obstruction. The cotangent surface Tot(O(-2) over P1) is a different
variety of complex dimension two.

A surface arising from a specified critical or deformation chart can still
be used. The new chapter constructs the normal potential W=lambda*mu and
its oriented, normalized vanishing-cohomology comparison. That does not
identify an entire threefold category with the surface or provide stable
functors for every matrix-factorization category.

## The previously displayed gauge does not show a dynamical effect

Let J=E12-E21 and G=I+(J tensor J)/h, as in the earlier note.
Since P(J tensor J)=(J tensor J)P, G commutes with R(u).
Where G is invertible, G R(u) G^{-1}=R(u) exactly.
Also (J tensor J)^2=I and

    det(G)=(h²-1)²/h⁴.

Thus G is singular at h=1 and h=-1 and is undefined at h=0.
Its displayed formula has no u or Kähler parameter. It cannot establish the
claimed nontrivial parameter-dependent conjugation. These are exact matrix
statements, not a verdict on every possible geometric change of basis.

## Disposition of the earlier paragraphs

- (a)(1): retain uniqueness of the cohomological stable map, with the actual
  support, Euler and degree hypotheses. Remove the added slope input and
  replace the incorrect uniqueness locator by Theorem3.3.4.
- (a)(2): retain the definition Stab(C')^{-1}Stab(C) after the necessary
  inversions. Crossing relations require their own definitions and proof.
- (a)(3): the two-dimensional operator equality is now proved with its
  evaluation modules and coefficient map. An unspecified universal
  isomorphism is not implied. Section11.2 is not the claimed theorem11.2.
- (a)(4): a chamber/Weyl-group identification requires the actual torus and
  hyperplane arrangement. No general identification is adopted here.
- (b)(1) and (b)(4): the added slope/Kähler dependence is not part of this
  ordinary cohomological definition. A different cohomology theory must
  retain its own hypotheses and parameter shifts.
- (b)(2) and the conifold setup: the purported smooth threefold Nakajima
  realization fails the even-dimensional symplectic requirement. A change
  of stability is not established by merely changing framing labels.
- (b)(3): retain the polarization choice. On the present cohomological
  fixed-point space its change is the specified diagonal sign conjugation.
  A cross-variety polarization transport needs an actual correspondence.
- (b)(5) and the explicit gauge: the claimed unipotent dynamical effect is
  not established by the displayed G. Its commutation and determinant
  have been computed above.
- The five-part flop statement and final braided-category conclusion:
  the stated threefold example cannot meet the symplectic hypotheses.
  No coherent categorical functors or natural equivalences are supplied
  by this matrix calculation. Their construction remains a separate
  obligation, and a parameter-dependent matrix is not a substitute.

The constructive replacement preserves a geometric R-matrix, its actual
quantum intertwining relation, its normal critical comparison and its
resonant subquotients. It does not turn unsupported threefold or categorical
claims into accepted consequences. Fresh mathematical review of the new
candidate remains open.
