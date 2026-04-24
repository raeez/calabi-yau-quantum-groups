# ATTACK-HEAL record: CY-B_3 Koszul, CY-C E_2-braided convergence,
# sibling Sigma_2-cycle zoo (2026-04-22)

## Scope and relation to existing material

This record documents five attack-heal cycles performed against the
scope items of the 2026-04-22 Opus-4.7 research sweep. It does
not introduce manuscript prose; manuscript results live in
`chapters/theory/e2_chiral_algebras.tex` (Conjecture
`conj:kapranov-3shifted-exterior-koszul`, Theorems
`thm:cy-b-d3-conductor-coincidence`, `thm:cy-b-d3-lp2-koszul`,
Remark `rem:cy-b-d3-precise`), `chapters/theory/braided_factorization.tex`
(Remark `rem:braided-fact-scope`, Proposition
`prop:specialisation-consumes-e2`), `chapters/examples/cy_c_six_routes_convergence.tex`
(Conjecture `thm:six-routes-isomorphism`, Remark on E_2 braided upgrade),
`chapters/examples/cy_c_pentagon_hypothesis_closures_platonic.tex`
(Theorem `thm:cy-c-pentagon-convergence-unconditional`),
`chapters/examples/cy_c_beyond_k3e_existence_obstruction.tex`
(Theorem `thm:cy-c-leech-rank-obstruction` forbidding Fake Monster from d=3),
and the prior note `notes/cy_b_d3_kapranov_identification.md`
(PTVV/Kapranov agreement up to GRT_1-gauge).

Siblings already covered in `notes/wave15_a13_fake_monster_sibling_costello.tex`
(Niemeier-index lock, Fake-Monster as d=5 sibling).

## Cycle 1. Chain-level Kapranov 3-shifted Koszul: strict quasi-inverse vs GRT-ambiguity

### Attack
Claim under attack: the CY-B_3 Koszul pair
(K, K^{-1}) with K(M) = RHom(E_X, M), K^{-1}(N) = E_X otimes^L_{End(E_X)} N
is a *strict* quasi-inverse pair on D^b(Coh(X)) for every compact CY_3 X.

### Falsification
FALSE in general. Two failure modes:

(F1) For compact CY_3 X (quintic, K3-fibered, abelian), no tilting object
E_X in D^b(Coh(X)) with End^bullet(E_X) isomorphic to Lambda^bullet_{-3}(T_X)
is known. Attack refuted on existence grounds, not on strictness.

(F2) Even assuming E_X exists, the PTVV presentation of Lambda^bullet_{-3}(T_X)
(BV/CPTVV (-3)-symplectic quantisation chain) and the Kapranov endomorphism
presentation differ by a class in GRT_1(Q) (Drinfeld-associator gauge).
The two differentials d_CPTVV = iota_{omega_X} and d_Kap = delta_Kosz coincide
on the cohomology of the bar complex but are connected by a homotopy of
infty-quasi-isomorphisms parametrised by the GRT_1-torsor of Drinfeld
associators (prior note, verdict).

### Healed statement
**Lemma (strict-inverse criterion, TORIC).**
Let X be a toric CY_3 (resolved conifold, Tot(K_S) for S a toric del Pezzo,
C^3). Let E_X = oplus_sigma O(D_sigma) be the Bondal-Orlov tilting bundle
over the toric divisors. Then K(M) = RHom(E_X, M) and K^{-1}(N) =
E_X otimes^L_{End(E_X)} N are a strict pair of inverse equivalences
D^b(Coh(X)) simeq D^b(End(E_X)-mod), with End(E_X) the Jacobi algebra
CQ/(partial W) of the toric quiver-with-potential, and the GRT_1-gauge
class vanishes because the path-algebra presentation realises the
Kontsevich associator on the nose. *Unconditional.*
(This is layer (c) of `rem:cy-b-d3-precise` for toric, already
`thm:cy-b-d3-lp2-koszul`.)

**Conjecture (strict-inverse criterion, COMPACT).**
For X a compact CY_3 admitting a tilting object E_X of strict
(-3)-CY type, the GRT_1(Q) obstruction class
[Phi_{PTVV/Kap}] in GRT_1(Q) vanishes iff the BV-formality choice on
Perf(X) is realised by an associator lying in the closure of
rational associators. Expected TRUE by Willwacher 2015 (Kontsevich-
graph-complex/GRT_1 surjection); UNPROVED without existence of E_X.

### Ghost theorem
CY-B_3 has two logically independent obstructions: (E) existence of a
tilting object with the correct endomorphism algebra, (G) vanishing
of the GRT_1 gauge class. (E) is geometric and open for compact CY_3;
(G) is formal and automatic on cohomology but non-trivial at the chain
level. The compact-CY_3 programme needs BOTH.

## Cycle 2. Pentagon colimit at (infty,1)-level: universality vs naive pushout

### Attack
Claim: the pentagon colimit of (`thm:cy-c-pentagon-convergence-unconditional`)
is the naive chain-level pushout in Alg_{E_1}^{ch} of the five chiral
algebras A_X^{R_1}, A_X^{R_3}, A_X^{R_4}, A_X^{R_5}, A_X^{R_6}
along the pentagon intertwiners.

### Falsification
FALSE. The naive chain-level pushout is the 1-categorical coequaliser of
the pentagon bridges, which is generically strictly larger than the
(infty,1)-colimit (it forgets higher coherence data encoded in the
tetrahedral 2-cells of the pentagon). The Francis-Gaitsgory machinery
(prop:cy-c-pentagon-colimit) computes the (infty,1)-colimit as
`colim^{(infty,1)} = |B_*(A_X^{R_1}, ...)|` with B_* the bar simplicial
object of the pentagon diagram, which has strictly more relations than
the naive pushout.

### Healed statement
The pentagon colimit identification with G(K3 x E) is an
(infty,1)-categorical statement (per
`chapters/examples/cy_c_pentagon_hypothesis_closures_platonic.tex` lines
605-610). The chain-level refinement is CONDITIONAL on the four
hypotheses (H1)--(H4) each of which supplies chain-level Phi_3 data
at a different boundary. CG north star: every theorem is stated in the
lane in which its proof actually works. The (infty,1) statement is
proved modulo CY-A_3 (Theorem `thm:cy-to-chiral-d3`, infty-categorical
scope); the chain-level statement requires H1-H4 closure. Both lanes
load-bearing; neither reduces to the other.

### Ghost theorem
Pentagon colimit = (infty,1)-colimit, not 1-colimit. The difference is
witnessed by the Bar simplicial object of the pentagon diagram; the
chain-level realisation requires the four hypotheses to collapse the
higher coherence.

## Cycle 3. E_2-braided six-route convergence

### Attack
Claim: the six routes of `def:cy-c-six-routes` converge to a single
E_2-braided object G(K3 x E), with the braiding (half-braiding data
on Z(Rep^{E_1}(A_X^{R_i}))) matching across all six routes.

### Falsification
FALSE at the naive level for three reasons:

(F1) Six routes are six DIFFERENT constructions, not six Phi_3 applications
(CLAUDE.md AP-CY: "Six routes to G(K3 x E) are six DIFFERENT constructions,
NOT six Phi applications"). Only R_1 is a canonical Phi_3 application;
R_2-R_6 are independent constructions; convergence is conditional.

(F2) E_1-convergence is conjectural (`thm:six-routes-isomorphism`);
the E_2-braided upgrade is STRICTLY STRONGER, requiring compatibility
of the half-braidings sigma_M(N) across six routes.

(F3) The BZFN equivalence Z(Rep^{E_1}(A)) simeq Rep^{E_2}(Z^{der}_{ch}(A))
(`prop:cy-c-BZFN`) is a per-route statement; compatibility across routes
requires a pentagon of equivalences.

### Healed statement
**Reduction Lemma (E_2-braided <- E_1 + three cocycle compatibilities).**
Suppose (C1) Conjecture `thm:six-routes-isomorphism` is proved
(E_1-chiral convergence of the six routes), and (C2) the
half-braiding cocycle sigma^{R_i}_M(N) on Z(Rep^{E_1}(A_X^{R_i}))
is compatible with each of the six pairwise bridges alpha_{ij} under
BZFN transport, namely:
  (i)   alpha_{12}-compatibility:   sigma^{R_1} compatible with sigma^{R_2}
        via derived-Fourier-Mukai + elliptic-genus refinement
        (Caldararu-Willerton Mukai pairing on HKR);
  (ii)  alpha_{23}-compatibility:   sigma^{R_2} compatible with sigma^{R_3}
        via Borcherds denominator theorem (unconditional per
        `prop:route2-route3-bridge`);
  (iii) alpha_{56}-compatibility:   sigma^{R_5} compatible with sigma^{R_6}
        via Costello-Gaiotto holomorphic-twist comparison.
Then by transitivity around the 6-cycle
(`prop:route6-route1-closure`), six-route E_2-braided convergence holds
and G(K3 x E) carries a canonical E_2-braided structure inherited from
each of the six Z(Rep^{E_1}(A_X^{R_i})).

**Status.** (C2)(ii) is unconditional. (C2)(i) and (C2)(iii) are
conjectural; (C2)(i) depends on a higher-genus extension of the EOT
identity plus Caldararu-Willerton; (C2)(iii) depends on a BV-chain-level
comparison.

### Ghost theorem
E_2-braided convergence is controllable by three independent half-braiding
cocycle conditions, one per pair of adjacent routes in the 6-cycle after
modding by Borcherds. The reduction cleanly separates the unconditional
ingredient (Borcherds) from the conjectural ones (higher-genus EOT,
Costello-Gaiotto BV).

## Cycle 4. Sibling Sigma_2-cycle zoo classification

### Attack
Claim: every primitive Sigma_2-cycle in a compact CY_3 X is exhausted by
the five classes (K3-fibre, abelian-surface, Humbert-divisor-in-Hilb^2(K3),
Niemeier-sector-in-K3xE, Enriques-quotient).

### Falsification
FALSE without restriction. Two counterexamples:

(F1) Hyperkähler-fourfold sub-fibration. On X_4 = K3^{[2]} (which is not
CY_3; included for scope-sanity), twistor-P^1 families give Sigma_2-cycles
not in the five classes. Restricting to CY_3 rules this out (K3^{[2]} is
not CY_3), so the failure is only scope-compatible.

(F2) Conifold-transition isolated Sigma_2-cycles. On a conifold transition
X ~> X' with X' a smooth CY_3, ruled-surface exceptional Sigma_2-cycles
(over the vanishing S^3 cycles) can appear in X that do not descend to
the Bogomolov decomposition strata of X'.

### Healed statement
**Classification (primitive, lattice-polarised, h^{2,0}=1 stratum).**
Let X be a compact CY_3 whose Neron-Severi lattice is primitively
embedded in II_{3,19} and h^{2,0}(X) = 1 (equivalently X lies in the
Bogomolov-decomposition strict stratum or isotrivially fibred K3 x E
stratum). A primitive Sigma_2-cycle Sigma subset X is one of:
(a) K3-fibre class (Bogomolov-decomposition Type-II);
(b) abelian-surface fibre class (Bogomolov-decomposition Type-III, excluded
at d=3 by h^{0,3}=1 mismatch);
(c) Humbert-divisor class in Hilb^2(K3) pulled back under a rational
Hilb-to-X map (exists only when X is birational to Hilb^2 of a K3);
(d) Niemeier-sector class in K3 x E (at X = K3 x E, under Niemeier-index
lock per `notes/wave15_a13_fake_monster_sibling_costello.tex`);
(e) Enriques-quotient class (at X = K3/involution x E).
The Leech-rank obstruction (`thm:cy-c-leech-rank-obstruction`)
forbids the Fake-Monster / Leech-Niemeier sector from d=3; the
Niemeier-twin sector at d=3 is restricted to the 23 non-Leech
Niemeier classes.

**Note.** Classes (a), (d), (e) intersect (Enriques is a K3 quotient,
hence fits both (a) and (e)); (b) is vacuous at d=3 under h^{0,3}=1;
(c) requires a rational map X --> Hilb^2(K3) which is itself a strong
geometric condition.

### Ghost theorem
Under the Bogomolov-stratification plus h^{0,3}=1 (strict-CY_3) plus
lattice-polarisation, the Sigma_2-cycle zoo in X is finite and
Niemeier-enumerated (23 classes at d=3 after Leech-exclusion, plus
Humbert and Enriques). The zoo is richer than five classes but not
infinite.

## Cycle 5. CY-C three-route convergence on generic K3 (beyond Mukai sub-locus)

### Attack
Claim: the three routes R_1 (Phi_3 functor), R_3 (lattice VOA on Mukai
lattice), R_4 (Kummer orbifold) agree on a generic algebraic K3 surface
(Picard rank 1), not just on the Mukai-lattice sub-locus (Picard rank 20).

### Falsification
FALSE in a precise sense. The Mukai-lattice lattice VOA V_{Lambda_Muk}
requires a signature-(4,20) or signature-(3,19) lattice; on a generic
Picard-rank-1 K3 the Mukai lattice degenerates to rank 4 (2 from U plus
2 from the polarization) and the VOA construction produces V_{II_{2,2}}
tensored with a rank-0 factor, which is a genuinely different object
than the generic-K3 Phi_3 output.

### Healed statement
Three-route convergence on a generic algebraic K3 holds only after
transport along the K3 period domain from the singular-K3 fibre
(Picard rank 20, where Mukai lattice is full rank 24) to the generic
fibre. The transport is controlled by the global Torelli theorem
(Piatetski-Shapiro-Shafarevich) plus the deformation-flatness of
derived Fourier-Mukai (Mukai 1984). At the generic fibre the three
routes converge up to a finite-index sublattice ambiguity of order
|O(Lambda_Muk)/O(Lambda_K3_generic)|, which is generally non-trivial.

### Ghost theorem
Three-route convergence is GENERIC-Picard-rank-stable under deformation
of K3 period, but the group of sublattice ambiguities is non-trivial off
the Mukai sub-locus; Schottky ambiguity at genus g >= 3 has an analogous
mod-Torelli-group ambiguity.

## Convergence gate: next-attack test

After Cycle 5, attempting ATTACK 6 (three-route convergence via direct
arithmetic comparison of N=1 partition functions) produced no new
weakness: the arithmetic-genus-1 match (Harvey-Moore rank-level Phi_10
identity, cited in `prop:route2-route3-bridge`) handles it cleanly.
Gate criterion met.

## Summary of new increments (relative to prior manuscript and notes)

1. Strict-inverse criterion for Kapranov 3-shifted Koszul: strictly
   satisfied for toric CY_3 (path-algebra/Jacobi-algebra realisation
   of the Kontsevich associator), conditionally satisfied for compact
   CY_3 under two independent obstructions (tilting existence +
   GRT_1-gauge vanishing).
2. Reduction of E_2-braided six-route convergence to E_1-convergence
   plus three half-braiding cocycle compatibilities, separating the
   unconditional Borcherds-denominator ingredient from the two
   conjectural ones (higher-genus EOT, Costello-Gaiotto BV).
3. Classification of the primitive Sigma_2-cycle zoo in the
   lattice-polarised strict-CY_3 stratum: 23 Niemeier classes
   (Leech excluded) + Humbert + Enriques, consolidating prior partial
   results.

## Literature anchors

- PTVV 2013 Publ.IHES 117; CPTVV 2017 J.Topology 10.
- Kapranov 1988 Inventiones 92 (Koszul), Kapranov 1991 (derived-category
  Koszul duality).
- Bondal-Orlov 2001 Compositio Math. 125.
- Ben-Zvi-Francis-Nadler 2010 JAMS 23:909-966 Theorem 6.4.
- Willwacher 2015 Inventiones 200 (Kontsevich graph complex = GRT_1 Lie).
- Borcherds 1992 Inventiones 109 Theorem 10.4 (denominator theorem).
- Harvey-Moore arXiv:hep-th/9510182 (rank-level Phi_10).
- Conway-Sloane 1988 Sphere Packings Lattices Groups Chapter 10 (Niemeier).
- Piatetski-Shapiro-Shafarevich 1971 (K3 global Torelli).
- Dabholkar-Murthy-Zagier arXiv:1208.4074 (Gritsenko-Nikulin automorphy).

Internal anchors listed at top of file.
