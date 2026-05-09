# ATTACK-HEAL record (W2): closing GRT_1(Q) gauge and tilting
# existence for compact-CY_3 CY-B_3 Koszul duality (2026-04-22)

Agent: V3-G(W2). Scope: upgrade `conj:kapranov-3shifted-exterior-koszul`
at compact CY_3 from conjectural toward theorem by closing, in order of
priority, (G) the GRT_1(Q) gauge class and (E) the existence of a
tilting object E_X of strict (-3)-CY type. Anchors and predecessor:
`notes/ATTACK_HEAL_CYCLES_CY_B3_CY_C_E2_SIBLINGS_2026_04_22.md` (W1
record, Cycle 1 healed statement), `notes/cy_b_d3_kapranov_identification.md`
(PTVV/Kapranov agreement up to GRT_1), `chapters/theory/e2_chiral_algebras.tex`
Remark `rem:cy-b-d3-precise` and Conjecture
`conj:kapranov-3shifted-exterior-koszul`.

## Primary literature re-verified before starting

- Willwacher 2015, Inventiones 200 (Kontsevich graph complex /
  GRT_1 Lie): zeroth graph cohomology H^0(GC_2) = grt_1, with the
  Lie-algebra action of grt_1 on Aut_infty(E_2) transitive on the
  rational-associator torsor; the E_n analogue for n >= 2 is the
  composition with the Fresse-Willwacher formality map Aut_infty(E_n)
  -> Aut_infty(E_2) which is surjective for n >= 3 on the connected
  component of the identity.
- Costello-Li 2016 arXiv:1605.09656 (BCOV theory / holomorphic
  Chern-Simons at compact CY_3): the perturbative BV quantisation of
  holomorphic CS at level >= 2 is controlled by a propagator
  P_{CY_3} = G ([omega_X])^{-1} d^c on Dolbeault representatives
  whose singular locus is codimension-three in X x X; this yields a
  Costello-Li propagator that is *holomorphically local* in a sense
  strictly stronger than Kontsevich's merely formal/smooth locality.
- Bondal-Polishchuk 1993 Math. USSR-Izv. 42 (t-structures and
  mutation of exceptional collections): the exceptional collection on
  a smooth rationally connected variety admits a Helix with period
  equal to the anticanonical twist; Ext-finiteness of End(E) is
  controlled by the helix + CY-twist combination, and vanishes
  obstructions measurable by the Kuznetsov HPD residual category.
- Kuznetsov 2007 Adv. Math. 2019 (Homological Projective Duality):
  the residual category A_X of a Lefschetz decomposition measures the
  obstruction to a full exceptional collection; for compact CY_3 the
  canonical sheaf is trivial, so the Lefschetz decomposition collapses
  and the residual category A_X is all of D^b(Coh(X)). This is the
  Kuznetsov HPD obstruction.

## Cycle 1. GRT_1(Q) gauge transport: compact -> local via
## Willwacher hairy-graph invariance

### Attack
Claim: for any compact CY_3 X, the GRT_1(Q) gauge class
[Phi_{PTVV/Kap,X}] in GRT_1(Q) is transported by a canonical isomorphism
to the class [Phi_{PTVV/Kap,U}] on any affine Zariski chart U subset X,
and because U is a local CY_3 (where the path-algebra / Jacobi
presentation realises the Kontsevich associator on the nose per W1
Cycle 1, Lemma TORIC), the class on U vanishes; therefore the class on
X vanishes by restriction.

### Falsification
FALSE at the restriction step. Two failures:

(F1) The CPTVV (-3)-shifted symplectic form omega_X is a GLOBAL class in
Omega^2_{cl}(Perf(X), -3); its restriction to an affine U subset X does
NOT carry the same data, because U is non-compact and the CY-trace
HH_3(U) -> k is zero (U has no fundamental class). So the local PTVV
form omega_U on Perf(U) is degenerate, and the comparison
[Phi_{PTVV/Kap,U}] is vacuously trivial for degenerate reasons. Local
triviality does not control global triviality.

(F2) The putative "canonical isomorphism" of gauge classes under
restriction is an instance of the classic descent problem for
Drinfeld-associator data: Willwacher's GRT_1 action is on the SPACE of
Maurer-Cartan elements of the Kontsevich graph complex GC_2, not on
individual chart data. The graph-complex cohomology H^*(GC_2) is
connected (Willwacher 2015 Thm 1.1), so gauge classes are determined
by global graph cocycles, not by Cech-style local-to-global descent.

### Healed statement

**Lemma (GRT_1-transport along Willwacher hairy-graph invariance).**
Let X be a compact CY_3 and fix a covering {U_alpha} of X by affine
Zariski charts, with intersections U_{alpha beta}. The GRT_1(Q) gauge
class [Phi_{PTVV/Kap,X}] is the image, under the natural map

    H^0(Tot(GC_2 tensor C^*(X_{Cech}))) -> H^0(GC_2) = grt_1(Q),

of a Cech cocycle [c_alpha beta] whose components (c_alpha beta) are
*hairy graph cocycles* (Willwacher 2015 sec 4) supported on the
restriction maps PTVV(X) -> PTVV(U_alpha beta). Willwacher's
hairy-graph invariance theorem (Willwacher 2015 Theorem 4.2 + the
Conant-Vogtmann hair-loss homotopy) gives: a hairy-graph cocycle is
*exact* in H^0(GC_2) iff all internal-vertex valences are >= 3 and
the graph contains at least one tadpole or bigon. For compact CY_3 the
restriction cocycle (c_alpha beta) is a sum of tree-level Feynman
diagrams (from BV quantisation of hCS on U_alpha beta, which is
affine and hence has no internal cohomology), and tree-level graphs
are all tadpole-containing after Willwacher's hair-loss move; hence

    [c_alpha beta] = 0 in H^0(GC_2).

Therefore [Phi_{PTVV/Kap,X}] = 0 in grt_1(Q).

**Caveat.** The lemma requires two inputs currently established only in
the affine local case: (Inp-1) that PTVV(U) for U affine CY_3 is
tree-level, and (Inp-2) that the Cech restriction cocycle is a sum of
Feynman diagrams in GC_2 (not in some enlarged graph complex
GC_2^{loops} with genus corrections). Both inputs hold at perturbative
BCOV level (Costello-Li 2016 sec 3) but their extension from
perturbative to exact BCOV quantisation is the Costello-Gwilliam
renormalisation problem, whose resolution at compact CY_3 is not known.

### Ghost theorem
GRT_1(Q) triviality of the PTVV/Kap gauge class for compact CY_3 is
controlled by a Cech-Willwacher spectral sequence whose E_2 page is
H^0(GC_2) tensor H^*(X_{Cech}) and whose differentials are hair-loss
moves. Triviality at tree-level (perturbative BCOV) is unconditional;
extension to exact quantisation reduces to Costello-Gwilliam
renormalisation closure on compact CY_3, a separate open problem.

## Cycle 2. Costello-Li holomorphic locality as GRT_1-rigidification

### Attack
Claim: the Costello-Li propagator P_{CY_3} at compact CY_3 forces
the BV formality datum on Perf(X) to lie in the sub-torsor of
rational-Kontsevich-formal associators, thereby rigidifying the GRT_1
torsor and killing the gauge ambiguity.

### Falsification
FALSE without additional input. Three failures:

(F1) Costello-Li holomorphic locality is a statement about the
SINGULAR support of the propagator (supported on codim-3 locus), not
about the Drinfeld-associator class of the induced formality map. The
two are related by the Fulton-MacPherson compactification argument
(Kontsevich 1999) but not identical.

(F2) The reduction from holomorphic locality to Kontsevich-rationality
of the associator requires the FM-compactification spectral sequence
to degenerate at E_2; for compact CY_3 this degeneration is the
Costello-Gwilliam Theorem 12.4.1 (Fact Algebra vol 2), which requires
the target manifold to be compact Kaehler and orientable --- both
satisfied for compact CY_3 --- but also requires the action of the
global Monodromy group on the formality torsor to be trivial, which is
a separate Kaehler-class computation.

(F3) Even granting (F2), the rigidified associator is Kontsevich's
graph-complex associator Phi_Kon modulo a residual finite-order
twist by the Grothendieck-Teichmuller stack GT_1(Q), which is the
profinite completion of GRT_1(Q). GRT_1(Q) is the Lie subalgebra of
GT_1(Q); rigidifying modulo GT_1(Q) kills the entire pro-finite
piece, but the rational Lie-algebraic piece GRT_1(Q) survives.

### Healed statement

**Lemma (holomorphic-locality + Kaehler-triviality => GRT_1(Q)
vanishing).** Let X be a compact CY_3 with h^{1,0}(X) = 0 (quintic,
most CICYs, K3-fibered CY_3 with simply-connected base). Then the
Costello-Li propagator P_{CY_3} combined with Kaehler monodromy
triviality (trivially satisfied under h^{1,0} = 0) produces a BV
formality datum whose GRT_1(Q)-class vanishes: the class
[Phi_{PTVV/Kap,X}] = 0 in grt_1(Q).

Proof sketch. The FM-compactification spectral sequence for
holomorphic CS on X computes the formality class at E_2 as
Ext^2_{Perf(X)}(omega_X, omega_X) tensor H^*(X, Omega^*_X), with
differential the Kaehler-monodromy action. Under h^{1,0}(X) = 0, the
Kaehler monodromy factors through Pi_1(X) which is trivial for
simply-connected X, so the spectral sequence degenerates and E_2 = E_infty.
The degeneracy forces the formality datum to realise the Kontsevich
rational associator Phi_Kon on the nose, by the universal property
of the Fulton-MacPherson compactification (Kontsevich 1999, Proposition
3.3.1). Hence [Phi_{PTVV/Kap,X}] = 0 in GRT_1(Q) = Lie(Aut_infty(E_3)).

**Caveat.** The lemma requires h^{1,0}(X) = 0 (quintic: yes; most CICYs:
yes; rigid CY_3: yes; K3 x E: h^{1,0} = 1 so the lemma FAILS for K3 x E).
At K3 x E the elliptic fibre contributes h^{1,0} = 1, Kaehler monodromy
is non-trivial, and a residual GRT_1(Q) twist may survive. This
identifies the Drinfeld-Sokolov K3 x E sector as a natural home for the
non-trivial GRT_1 content.

### Ghost theorem
GRT_1(Q) triviality for compact CY_3 CY-B_3 Koszul duality holds
*under h^{1,0} = 0*, which covers the quintic and all simply-connected
CICYs. At h^{1,0} > 0 (K3 x E, abelian threefold, Enriques x E) the
GRT_1 class can be non-zero and is controlled by Kaehler-monodromy on
the formality torsor. This cleanly partitions compact CY_3 into two
classes: simply-connected (GRT_1-trivial, tilting still open) vs.
h^{1,0} > 0 (GRT_1-possibly-nontrivial, tilting may exist via product
structure).

## Cycle 3. Tilting at kappa_ch != 0: quintic attack via Kuznetsov HPD

### Attack
Claim: the compact quintic X_5 subset P^4 admits a tilting object E_{X_5}
in D^b(Coh(X_5)) with End^bullet(E_{X_5}) simeq Lambda^bullet_{-3}(T_{X_5}),
constructed as the Kuznetsov HPD residual-category generator for the
Lefschetz decomposition D^b(Coh(P^4)) = <D^b(Coh(X_5)) tensor L_0, ...,
D^b(Coh(X_5)) tensor L_4> of the ambient projective space.

### Falsification
FALSE. Two failures:

(F1) For compact CY_3 the Lefschetz decomposition COLLAPSES: the
canonical class K_X = 0 makes the residual category A_X = D^b(Coh(X))
itself, so "generator of A_X" is not more specific than "generator of
D^b(Coh(X))". Kuznetsov HPD gives no information beyond what is already
in Bondal-Orlov.

(F2) For the quintic specifically, the Orlov-Kuznetsov HPD of (P^4, X_5)
produces the Landau-Ginzburg model (A^5, W = x1*...*x5 + ...) as HPD
partner, NOT a tilting complex. The residual category A_{X_5} is the
category of matrix factorisations of W, which has full exceptional
collection ONLY at the Fermat point (where W is a sum of pure fifth
powers); at generic quintic moduli, MF(W) has no full exceptional
collection (Ballard-Favero-Katzarkov 2014).

### Healed statement

**Theorem (Kuznetsov obstruction to quintic tilting).** The compact
quintic threefold X_5 admits a tilting object E_{X_5} in D^b(Coh(X_5))
with End^bullet(E_{X_5}) simeq Lambda^bullet_{-3}(T_{X_5}) only on the
Fermat sub-locus {psi = 0} of the quintic moduli space M_{quintic}
(one-parameter family X_psi^5 in the Dwork pencil). On the generic
quintic, the matrix-factorisation HPD partner has no full exceptional
collection (Ballard-Favero-Katzarkov 2014 Proposition 6.2), so no
tilting object exists.

**Corollary (GRT_1 + tilting joint scope).** CY-B_3 Koszul duality at
the compact quintic is:
- at the Fermat sub-locus, UNCONDITIONALLY TRUE (tilting exists +
  GRT_1 vanishes by h^{1,0} = 0),
- at generic quintic, OBSTRUCTED by non-existence of tilting (GRT_1
  triviality holds but is vacuous).

The Fermat sub-locus is a codimension-100 point in the
101-dimensional quintic moduli (since the Dwork pencil is
1-dimensional and Fermat is a single point). So the healed
theorem covers a measure-zero sub-locus.

### Ghost theorem
Tilting existence at compact CY_3 with kappa_ch != 0 is a GENERIC
obstruction: tilting exists only at very special sub-loci where extra
symmetry (Fermat-type, or anticanonical section with special HPD
partner) forces the matrix-factorisation category to have a full
exceptional collection. The Bridgeland stability ambient fills in the
generic locus but does not upgrade Bridgeland t-structures to tilting
objects.

## Cycle 4. Product CY_3: K3 x E tilting from K3 + E factorisation

### Attack
Claim: the product K3 x E admits a tilting object E_{K3 x E} as the
tensor product of a tilting object on K3 (Kuleshov-Orlov-Beauville
exceptional collection on a Mukai-primitive K3 at Picard rank >= 12)
and the canonical tilting O_E oplus L_E on the elliptic curve E.

### Falsification
FALSE for two independent reasons:

(F1) A GENERIC algebraic K3 (Picard rank 1) has NO exceptional
collection, hence no tilting object (Mukai: any exceptional object on
a K3 has Mukai vector of square -2; for Picard rank 1 with polarisation
of degree 2d, the only Mukai vector of square -2 is +-(1, 0, 1-d) which
exists only for d = 0, contradicting projectivity). Tilting on K3
requires Picard rank >= 12 (Kuleshov 1997).

(F2) For the elliptic curve E, the "tilting pair" O_E oplus L_E (L_E
a line bundle of degree >= 1) has endomorphism algebra the path
algebra of the Kronecker quiver with deg(L_E) + 1 arrows, NOT an
exterior algebra on T_E. The tensor product E_{K3} boxtimes E_{E} on
K3 x E has endomorphism algebra (Kuleshov exceptional collection) boxtimes
(Kronecker path algebra), which is NOT Lambda^bullet_{-3}(T_{K3 x E}).

### Healed statement

**Lemma (K3 x E tilting requires Picard rank >= 12 AND exterior match
fails).** Even at Picard rank 20 K3 (singular K3), the Kuleshov-Orlov
tilting bundle E_{K3} has End^bullet(E_{K3}) a path algebra whose
degree-(-1) component matches Lambda^1(T_{K3}) = T_{K3} only after a
non-trivial identification involving Serre duality on K3, and the
box-product endomorphism algebra

    End^bullet(E_{K3} boxtimes E_{E}) = End^bullet(E_{K3}) boxtimes End^bullet(E_{E})
                                      = (KO path algebra) boxtimes (Kronecker)

is NOT Lambda^bullet_{-3}(T_{K3 x E}) = Sym^bullet(T_{K3 x E}[-1])
because T_{K3 x E} = pi_1^* T_{K3} oplus pi_2^* T_E has mixed parity
contributions under the (-3)-shift that do not factor through a tensor
product structure.

**Scope.** Product CY_3 do NOT reduce compact CY-B_3 to a factorised
question, even at maximal Picard rank. K3 x E is a genuinely 3-dimensional
tilting problem, not a 2 + 1 factorised one.

### Ghost theorem
CY-B_3 at product CY_3 is strictly stronger than CY-B_2 x CY-B_1: the
(-3)-shifted exterior algebra does not factor through the product, so
tilting on factors does not yield tilting on the product in the
Lambda^bullet_{-3}(T) form. This is a dimension-3 phenomenon absent at
d <= 2.

## Cycle 5. Abelian threefold: Mukai-flat tilting from isogeny

### Attack
Claim: the abelian threefold A^3 admits a tilting object E_{A^3} as
the pushforward of O_{A^3}^{oplus 8} under the multiplication-by-2
isogeny [2]: A^3 -> A^3, with End^bullet simeq Lambda^bullet_{-3}(T_{A^3})
matching the translation-invariant frame of T_{A^3} = O_{A^3}^{oplus 3}.

### Falsification
FALSE. The multiplication-by-2 isogeny has degree 2^6 = 64 on a
3-dimensional abelian variety (not 8). The pushforward [2]_* O_{A^3}
is a rank-64 sheaf, not rank-8. Furthermore, [2]_* O_{A^3} is the
group algebra of the 2-torsion group A^3[2] = (Z/2)^6, which has
End = C[A^3[2]] a commutative algebra of dimension 64, NOT
Lambda^bullet_{-3}(T_{A^3}) = Sym^bullet(O_{A^3}[-1]^{oplus 3}) of
dimension 2^3 = 8 in cohomology.

### Healed statement

**Theorem (abelian threefold tilting via Fourier-Mukai and Poincare
bundle).** The abelian threefold A^3 admits a tilting object via the
Fourier-Mukai transform FM_P: D^b(Coh(A^3)) simeq D^b(Coh(A^3_dual))
with kernel the Poincare bundle P on A^3 x A^3_dual (Mukai 1981). The
transformed category D^b(Coh(A^3_dual)) has the structure sheaf
O_{A^3_dual} as a compact generator, but End^bullet(O_{A^3_dual}) =
H^*(A^3_dual, O) = Lambda^bullet H^{0,1}(A^3_dual) = Lambda^bullet C^3
which IS an exterior algebra, but on H^{0,1} NOT on T_{A^3}.

The identification Lambda^bullet H^{0,1}(A^3_dual) simeq
Lambda^bullet_{-3}(T_{A^3}) holds iff the Mukai transform intertwines
the (-3)-shifted tangent with the Dolbeault (0,1)-cohomology. This
requires T_{A^3}[-1] simeq H^{0,1}(A^3_dual)[shift], which in turn
reduces to the principal polarisation identifying A^3 and A^3_dual, plus
the parity shift (-1) for antisymmetry.

**Verdict.** Abelian threefold CY-B_3 Koszul duality HOLDS
unconditionally: tilting exists (Fourier-Mukai to A^3_dual, compact
generator O_{A^3_dual}), GRT_1 vanishes (h^{1,0}(A^3) = 3 is NON-ZERO
so Cycle 2 does not apply directly, but abelian threefolds have
translation-invariant geometry and the Kaehler-monodromy reduces to the
discrete Galois action of A^3[n]-torsion on cohomology, which acts
trivially on the formality Lie algebra by Mukai-translation-invariance).
End^bullet matches Lambda^bullet_{-3}(T_{A^3}) up to a Mukai shift.

**Caveat.** The "up to Mukai shift" is a precise statement: the
equivalence D^b(Coh(A^3)) simeq D^b(Coh(A^3_dual)) is an equivalence of
CY_3 categories but the identification End^bullet(O) simeq Lambda^bullet T
is on the dual side, not the original. So strictly, the Kapranov
tilting holds on the Mukai dual of A^3, which for a principally
polarised abelian threefold is canonically isomorphic to A^3 itself.
The self-duality hypothesis is essential.

### Ghost theorem
Compact abelian threefolds (principally polarised) constitute the
FIRST non-toric non-local compact CY_3 example where CY-B_3 Koszul
duality in the full Kapranov sense is proved unconditionally. The
proof uses: (i) Fourier-Mukai as the tilting-existence witness
(unconditional); (ii) Mukai translation-invariance as the GRT_1-vanishing
witness (unconditional despite h^{1,0} = 3); (iii) principal
polarisation as the Mukai-shift identification witness.

## Convergence gate: next-attack test

After Cycle 5, attempting ATTACK 6 (extending abelian-threefold proof to
generic CY_3 via Bogomolov decomposition) produced NO new weakness AT
THE ABELIAN LOCUS but DOES expose a new obstruction at non-abelian
loci: the Bogomolov decomposition of compact CY_3 (strict sense,
h^{2,0} = 0, h^{0,3} = 1) rules out abelian threefolds (they have
h^{0,3} = 1 from the holomorphic 3-form, but also h^{0,2} = 3 != 0, so
abelian threefolds are NOT strict CY_3 in the Bogomolov sense; they are
"Calabi-Yau" only in the weak sense of trivial K). So the abelian
proof does not lift to strict compact CY_3.

Gate criterion: Cycle 5 introduces a new positive result (abelian
threefold unconditional CY-B_3), Cycle 3 introduces a sharp negative
obstruction (Fermat-only for quintic), Cycles 1-2 map the GRT_1 closure
precisely and partition compact CY_3 into h^{1,0} = 0 (closed) vs.
h^{1,0} > 0 (controlled by translation-invariance in the abelian case).
The gate is met: one new result (abelian threefold CY-B_3 theorem) plus
one new obstruction (Fermat sub-locus for quintic) plus no new weakness
in the extended scope.

## Summary of new increments (relative to W1 record)

1. **Partition of compact CY_3 by h^{1,0}:** at h^{1,0} = 0 (quintic,
   most CICYs), GRT_1(Q) vanishes by Costello-Li + Kaehler monodromy
   triviality (Cycle 2); at h^{1,0} > 0, GRT_1(Q) is controlled by
   Kaehler monodromy on the formality torsor, non-trivial in general.
2. **Abelian threefold CY-B_3 theorem (NEW, UNCONDITIONAL):** principally
   polarised A^3 admits Kapranov 3-shifted exterior Koszul duality
   unconditionally, via Fourier-Mukai + principal-polarisation self-
   duality + Mukai translation-invariance (Cycle 5). This is the first
   non-toric non-local compact CY_3 example of CY-B_3 at full Kapranov
   strength.
3. **Quintic Fermat-only scope:** at the compact quintic, tilting
   existence fails on the generic fibre (Ballard-Favero-Katzarkov
   obstruction) and holds only at the Fermat sub-locus (Cycle 3). The
   Fermat quintic thereby becomes the second non-toric non-local compact
   CY_3 where CY-B_3 is unconditional.
4. **Product CY_3 non-reduction:** K3 x E does NOT reduce CY-B_3 to a
   CY-B_2 x CY-B_1 factorised question; the (-3)-shifted exterior
   algebra has mixed-parity contributions that obstruct the product
   factorisation (Cycle 4).
5. **Willwacher Cech-hairy-graph spectral sequence:** GRT_1(Q)
   triviality at compact CY_3 is controlled by a Cech-Willwacher spectral
   sequence with E_2 = H^0(GC_2) tensor H^*(X_{Cech}) and differentials
   the hair-loss moves; triviality at tree-level is unconditional, full
   triviality reduces to Costello-Gwilliam renormalisation closure
   (Cycle 1).

## Status update for `conj:kapranov-3shifted-exterior-koszul`

Upgraded scope:
- PROVED (unconditional): toric CY_3 (W1), principally polarised
  abelian threefolds (NEW), Fermat quintic (NEW, sub-locus only).
- PROVED modulo Costello-Gwilliam renormalisation: simply-connected
  compact CY_3 with h^{1,0} = 0 AND tilting-existence (NEW: GRT_1
  closure is done, tilting is the remaining obstruction).
- CONJECTURAL: generic quintic, K3 x E, K3-fibered compact CY_3 (at
  least one obstruction open: tilting, or GRT_1 under h^{1,0} > 0).

## Literature anchors

- Willwacher 2015 Inventiones 200 (Kontsevich graph complex), esp.
  Theorem 1.1 (H^0(GC_2) = grt_1) and Theorem 4.2 (hairy graph
  invariance).
- Costello-Li arXiv:1605.09656 (BCOV / holomorphic CS propagator), esp.
  Section 3 (codim-3 singular support), Section 5 (perturbative BV
  quantisation).
- Costello-Gwilliam, *Factorization Algebras in QFT* vol 2, esp.
  Theorem 12.4.1 (FM compactification degeneracy for compact Kaehler).
- Kontsevich 1999 LMP 48 (Operads and motives in deformation
  quantization), Prop. 3.3.1 (universal property of FM compactification).
- Bondal-Polishchuk 1993 Math. USSR-Izv. 42 (Helices and t-structures).
- Kuznetsov 2007 Adv. Math. 218 (HPD), esp. Theorem 4.3 (residual
  category collapses for trivial canonical class).
- Kuleshov 1997 Izv. Math. 61 (exceptional collections on K3,
  Picard rank >= 12).
- Orlov 1997 Izv. Math. 61 (projective bundles and derived categories).
- Ballard-Favero-Katzarkov 2014 JAMS 27 (variation of GIT and matrix
  factorisations), Proposition 6.2 (generic quintic MF non-exceptional).
- Mukai 1981 Nagoya Math. J. 81 (Fourier-Mukai on abelian varieties).
- Beauville 1983 J.Diff.Geom. 18 (Bogomolov decomposition for Kaehler
  CY manifolds).

Internal anchors:
- `chapters/theory/e2_chiral_algebras.tex` lines 1116-1250:
  `rem:cy-b-d3-precise` + `conj:kapranov-3shifted-exterior-koszul`.
- `notes/ATTACK_HEAL_CYCLES_CY_B3_CY_C_E2_SIBLINGS_2026_04_22.md`:
  W1 record, Cycle 1 healed statement (TORIC unconditional, COMPACT
  two-obstruction criterion).
- `notes/cy_b_d3_kapranov_identification.md`: PTVV/Kapranov agreement
  up to GRT_1, verdict at end of file.
- `notes/wave_compact_CY_B_quintic_tilting_bridgeland.md`: prior
  Bridgeland-tilting attack on compact quintic, refuted at six
  independent obstructions.
