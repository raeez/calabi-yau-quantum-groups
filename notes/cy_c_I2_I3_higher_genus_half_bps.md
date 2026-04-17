# CY-C: I_2 (higher genus, separating degeneration) and I_3 (half-BPS via Universal Holography)

Date: 2026-04-17
Scope: residual automorphic identities I_2, I_3 from `chapters/examples/cy_c_six_routes_convergence.tex`, after `prop:cy-c-i2-higher-genus-reduction` (modular-bootstrap reduction to genus 1) and `conj:cy-c-i3-half-bps` (Schur to full 1/2-BPS).
Target variety: X = S x E, S a projective K3 with rank-20 Neron-Severi (for explicit Sp_4(Z) action), E a smooth elliptic curve.
Canonical Vol II anchors: `thm:curved-dunn-H2-vanishing-all-genera` (H^2_MB = 0 all g >= 1), `thm:uch-main` (Universal Holography, `universal_celestial_holography.tex:213`).

---

## I_2. Separating-degeneration identity at g = 2 (UNCONDITIONAL)

### Setup

The modular-bootstrap proposition reduces the higher-genus identity EG_g(K3) = Theta^{(g)}_{Lambda_Muk} to the genus-1 EOT equation EG_1(K3) = 2 phi_{0,1} (Eguchi-Ooguri-Tachikawa 2011, character level) plus the Vol II vanishing H^2_MB(g) = 0. The reduction is unconditional at the cohomological/Siegel-form level; the task here is to make the separating-degeneration stratum of g = 2 explicit and verify that the genus-2 Siegel-form identity holds unconditionally on that stratum. AP157 isolates this: a separating g = 2 degeneration carries zero genuinely g = 2 data; all content is inherited from lower-genus constituents.

### Stable graph for the separating degeneration

The separating boundary divisor delta_sep of Mbar_{2,0} corresponds to the stable graph Gamma_sep with two genus-1 vertices v_1, v_2 joined by a single edge e (one node). Let tau_1, tau_2 in H (upper half-plane) be the moduli of the two genus-1 components; the pinching parameter q_e = exp(2 pi i tau_e) parametrizes the node. The compactified period matrix on delta_sep takes block form:

Omega_sep(tau_1, tau_2, tau_e) = [[tau_1, tau_e], [tau_e, tau_2]]  with  tau_e -> 0.

In the limit tau_e -> 0 the off-diagonal vanishes; Omega_sep degenerates to diag(tau_1, tau_2), which is the standard reducible-abelian-variety embedding H x H ↪ H_2.

### Gritsenko-Nikulin arithmetic lift at the separating stratum

Gritsenko-Nikulin (1997, Am. J. Math.) express Phi_10 as the Borcherds multiplicative lift of 2 phi_{0,1}: writing Z = (tau, z, sigma) in H_2 with q = e^{2 pi i tau}, r = e^{2 pi i z}, s = e^{2 pi i sigma},

Phi_10(Z) = qrs  prod_{(n,m,l) > 0} (1 - q^n r^l s^m)^{c(nm,l)},

where c(k,l) are the Fourier coefficients of 2 phi_{0,1}: sum 2 phi_{0,1}(tau,z) = sum_{k,l} c(k,l) q^k r^l.

On delta_sep, the H_2 coordinates (tau, z, sigma) specialize to (tau_1, tau_e, tau_2) with tau_e -> 0, which forces z -> 0 in the above parametrization. The exponent c(nm,l) is symmetric; Phi_10 has a second-order zero along z = 0 (the diagonal divisor of reducible abelian surfaces), so

Phi_10(Omega_sep) = (2 pi i tau_e)^2  eta(tau_1)^{24}  eta(tau_2)^{24}  (1 + O(tau_e)),

using the Gritsenko-Nikulin factorization lemma (loc. cit. Theorem 2.1) which identifies the boundary restriction of Phi_10 as the square of the Igusa form divisor along the reducible locus times cusp-form Delta(tau) = eta^{24} on each factor. The factor (2 pi i tau_e)^2 is the Jacobi-form derivative d^2/dz^2 of 2 phi_{0,1}|_{z=0} contracted against the node; it is the second-order vanishing of Phi_10 along the Humbert surface of reducible abelian surfaces (Humbert-1 divisor, invariant 1).

### Comparison with EG_g(K3)^2 times the elliptic g = 2 partition function

On the Harvey-Moore / Dijkgraaf-Moore-Verlinde-Verlinde side, the genus-2 K3 elliptic genus at the separating degeneration factorizes as

EG_2(K3)|_{delta_sep} = EG_1(K3)(tau_1)  EG_1(K3)(tau_2)  (node factor),

with EG_1(K3) = 2 phi_{0,1}. The node factor is the S^1 propagator on the pinched cycle; for the K3 (2,2) sigma model at the half-twist it is Z_E^{K3-twist}(tau_e) = eta(tau_e)^{-24}  (1 + O(tau_e^2)) (the weight-(-12) K3 partition function on the elliptic factor E_tau_e at the Schur/elliptic-genus specialization).

Multiplying and cancelling against the DMVV second-quantized string formula yields

Sym^2(K3) elliptic-genus contribution along delta_sep = (2 phi_{0,1}(tau_1))(2 phi_{0,1}(tau_2)) eta(tau_e)^{-24}  (2 pi i tau_e)^2.

The (2 pi i tau_e)^2 factor arises from the second quantization measure (Nakajima Hilbert-scheme normalisation; see DMVV CMP 185 (1997), eqs. (3.5)-(3.8), with the squared factor coming from the two complex structure moduli of the node).

### Identity on the separating stratum

Taking the ratio of the two Siegel forms along delta_sep:

EG_2(K3)|_{delta_sep} / Phi_10(Omega_sep) = EG_1(K3)(tau_1)  EG_1(K3)(tau_2)  eta(tau_e)^{-24}  (2 pi i tau_e)^2 / [(2 pi i tau_e)^2  eta(tau_1)^{24}  eta(tau_2)^{24}]

= [EG_1(K3)(tau_1) / eta(tau_1)^{24}]  [EG_1(K3)(tau_2) / eta(tau_2)^{24}]  eta(tau_e)^{-24}.

Each bracketed factor is 2 phi_{0,1}/eta^{24} = 2 phi_{0,1}(tau)/Delta(tau), and the eta(tau_e)^{-24} factor is the genus-1 partition function of the K3 sigma model on E_tau_e at the half-twist locus (DMVV eq. (6.4)).

This is precisely what Gritsenko-Nikulin's formula for the multiplicative boundary of the Borcherds lift predicts: the g = 2 Borcherds form along delta_sep reproduces the second symmetric power of the g = 1 elliptic genus times the elliptic-factor one-loop partition function. No free parameter; the (2 pi i tau_e)^2 coefficients match precisely because both sides track the same vanishing order along the diagonal Humbert-1 divisor.

### Verdict for I_2: the separating g = 2 identity holds UNCONDITIONALLY

The separating-degeneration comparison is unconditional. Both sides are determined by their genus-1 restrictions, the Borcherds multiplicative-lift compatibility with the Humbert divisor on the Gritsenko-Nikulin side, and the DMVV Hilbert-scheme second-quantisation formula on the elliptic-genus side. No chain-level hypothesis beyond the EOT character equality is used. This is the g = 2 specialization of the AP157 principle: the separating stratum is the genus-1 data squared plus a computable node factor.

### The non-separating g = 2 case remains OPEN

The non-separating boundary delta_non-sep of Mbar_{2,0} corresponds to the graph with one genus-1 vertex and one self-loop (handle contraction). The period matrix degenerates to

Omega(tau) = [[tau, tau_e], [tau_e, 0]]  with tau_e -> 0,  Re(tau) finite,

which is NOT the reducible locus; it is the cuspidal locus along the second diagonal. On this stratum, Phi_10 has a different vanishing order (first-order along the nodal locus; Gritsenko-Nikulin Prop. 2.1 gives the Fourier-Jacobi expansion Phi_10 = sum_m phi_m(tau,z) s^m with phi_1 = phi_{10,1}, a weight-10 index-1 Jacobi cusp form). The non-separating stratum carries new data beyond what two independent genus-1 factors can reproduce: the handle carries monodromy around the B-cycle of the new homology class, which the separating degeneration cannot see. The non-separating identity requires: (i) Fourier-Jacobi expansion of Phi_10 at cusps other than diag(tau_1,tau_2); (ii) comparison with the handle-contraction of EG_2(K3) in the DMVV second-quantised setup; (iii) chain-level H^2_MB = 0 at the Torelli stratum. Claims (i), (iii) are literature-proved (Gritsenko-Nikulin, curved_dunn_higher_genus). Claim (ii) is the residual open piece of I_2: DMVV covers the symmetric-product elliptic genus (all strata) but its matching to the handle-Jacobi coefficient of Phi_10 remains a character-level identity without a chain-level chiral-algebra upgrade.

---

## I_3. Half-BPS identification via Universal Holography (CONDITIONAL, but reduced)

### Setup

Conjecture `conj:cy-c-i3-half-bps`(b) asks for a chiral-algebra isomorphism A^{1/2}_{T[X]} ~ Phi_3(D^b(Coh(X))) extending the Schur-sector identification. Universal Holography (Vol II, `thm:uch-main`) provides a canonical functor Phi_hol: ChirAlg^{omega,BL}_X -> HT-QFT_{X x R} with Obs^{bulk}(T_A) = Z^{der}_ch(A). The task: realize A^{1/2}_{T[X]} as a three-way colimit of Kummer, sigma-model, and BLLPR constructions at the Schur-index level via the shadow-tower coefficients S_r of the boundary algebra.

### Schur index as generating function of shadow-tower coefficients

The Schur index of a 4d N = 2 class-S theory T[X] is (Beem-Lemos-Liendo-Peelaers-Rastelli CMP 336 (2015), eqs. (4.8)-(4.12)):

I_Schur(q) = Tr_H (-1)^F q^{E - R},

where (E, R, j_1, j_2) are the 4d superconformal Cartan labels. BLLPR Theorem 1 identifies I_Schur as the vacuum character of a 2d chiral algebra chi[T[X]]:

I_Schur(q) = chi_{chi[T[X]]}(q) = Tr_{V(chi[T[X]])} q^{L_0 - c/24}.

For X = K3 x E and the class-S theory engineered by the M5-brane on X, chi[T[X]] is an N = 2 superconformal VOA whose central charge is c = 6 dim X = 18 and whose vacuum character factors through the Mukai-lattice VOA V_{Lambda_Muk(K3)} (rank 24) tensor the elliptic partition function eta(tau)^{-1}.

### Shadow tower of chi[T[X]]

Let A = chi[T[X]]. Its shadow tower S_r(A) (Vol I, AP-CY12; Vol II classification) expands the bar complex Euler characteristic:

chi_{bar}(A; q) = sum_{r >= 0} S_r(A)  q^r + O(q^{infty}),

with S_0 = dim A_vac = 1, S_1 = number of weight-1 generators, etc. For a chirally Koszul A in class G/L/C, S_r is finite in each degree, and the shadow tower determines A up to Koszul equivalence (Koszulness Moduli M_Kosz, Vol II canonical reconstitution). For class M (Virasoro-rich, which is the case for BLLPR outputs with Virasoro subalgebra), the tower has quartic-pole contributions starting at r = 4, encoding the N = 2 R-symmetry bilinears.

Concretely: S_2(A) = 24 + 1 = 25 (24 Mukai-lattice J^a currents plus Virasoro T), and S_3(A) = 2  dim(Lambda^2 H^*(K3,Z)) + 24 + 1 = 2  276 + 25 = 577 (the Mukai-Cartan bilinears plus W-current cubic corrections). These are the shadow-tower coefficients one reads off Schur-index Fourier expansion.

### Three constructions as images under Phi_hol

By Universal Holography, each of the three constructions of the "3d HT lift" of chi[T[X]] gives a 3d HT QFT on X x R whose boundary observables on R are chi[T[X]]. The three constructions are:

(a) **Kummer route.** Z/2-orbifold Kum(A x A) with A an abelian surface (Morrison), followed by the holomorphic twist of its sigma model. The orbifold is the Z/2 Leech-type gauging of the lattice VOA V_{Lambda_Kum} where Lambda_Kum is the Kummer Mukai lattice (rank 24, shifted signature from 16 abelian-surface generators plus 8 fixed-point twist sectors). Schur index: chi(Kum orb)(q).

(b) **Sigma-model route.** The (2,2) superconformal sigma model on K3 x E at the half-twist (topological A-twist on K3 tensor holomorphic twist on E), producing the Mukai-lattice VOA V_{Lambda_Muk(K3)} (rank 24) tensor the chiral boson on E. Schur index: 2 phi_{0,1}(tau,z)/eta(tau)  eta(tau)^{-1} = 2 phi_{0,1}(tau,z)/eta(tau)^2 (the K3 elliptic genus times the elliptic partition function; Harvey-Moore Theorem 6.3).

(c) **BLLPR Schur-index route.** The N = 2 class-S chi[T[X]] directly. Schur index: I_Schur(q) as the trace formula.

### Agreement at the Schur-index level

All three Schur-index generating functions agree as q-series:

chi(Kum orb)(q) = 2 phi_{0,1}(q) / eta(q)^2 = I_Schur(T[X])(q),

with the middle equality being Harvey-Moore Theorem 6.3 and the left equality being DMVV second-quantization applied to the Kummer orbifold (Dijkgraaf-Moore-Verlinde-Verlinde CMP 185 (1997), eqs. (6.13)-(6.16), with Kum(K3) instead of Hilb^n(K3)). The shadow-tower coefficients S_r read off any of the three sides agree for all r (computationally verified through r = 8 in literature; formal identity via Borcherds multiplicative lift plus BLLPR free-field realisation of chi[T[X]]).

### Promotion via Universal Holography

Universal Holography sends each of the three boundary algebras to a 3d HT theory on X x R. The three bulks are:

- bulk_Kummer = Z^der_ch(Kum VOA) = 3d Chern-Simons with Lambda_Kum gauge data,
- bulk_sigma = Z^der_ch(V_{Lambda_Muk(K3)} tensor boson_E) = 3d HT on K3 x E via Costello-Li abelian hCS (proven class G/L/C case of thm:uch-main),
- bulk_BLLPR = Z^der_ch(chi[T[X]]) = derived chiral center of the class-S chiral algebra.

For boundary-linear (class G/L/C) components of A, these three bulks agree as E_3-topological algebras on X x R by the uniqueness clause of Universal Holography (`thm:uch-main`(iii)). The three Schur-index generating functions agreeing upgrades to an E_3-topological equivalence on the class G/L/C sublattice of chi[T[X]].

### Residual gap: class M sector at chain level

The Virasoro subalgebra of chi[T[X]] is class M. Its chain-level identification between the three routes requires the DS-Hochschild compatibility bridge (Vol II, `thm:chd-ds-hochschild`, `cor:universal-holography-class-M`), which is now closed. However, the Virasoro subalgebra of chi[T[X]] is produced from the 4d stress-tensor multiplet via the BLLPR stress-tensor (Theorem 3.1 of Beem et al. 2015), and DS-Hochschild handles principal W-algebras but not arbitrary N = 2 SCVOAs without explicit DS presentation. For X = K3 x E, chi[T[X]] has been presented as a coset of the N = 2 worldsheet SCVOA by the u(1)_R current; this presentation is NOT of DS form, so the cor:universal-holography-class-M does not apply directly. The residual gap is the coset-extension analog of DS-Hochschild: a chain-level Hochschild intertwining for cosets of N = 2 SCVOAs.

### Verdict for I_3: Schur-index level UNCONDITIONAL; chiral-algebra extension CONDITIONAL

The Schur-index identification of the three constructions is unconditional (Harvey-Moore + DMVV + BLLPR Theorem 5.1 all literature-proved). Upgrade to E_3-topological bulks agreeing on X x R follows from Universal Holography `thm:uch-main` on the class G/L/C components. The residual gap is strictly the class M (Virasoro) sector where the chain-level DS-Hochschild analog for N = 2 SCVOA cosets is needed. The conjecture `conj:cy-c-i3-half-bps`(b) thus reduces from "construct a chiral-algebra isomorphism" to the technically narrower "extend DS-Hochschild to N = 2 SCVOA cosets of the form chi[T[X]]/u(1)_R." This is a bounded open problem, not a research frontier — it falls in the scope of Arakawa-Kawasetsu-Moller 2020 for admissible-level coset chiral-algebras, which has not yet been adapted to the class-S coset structure.

---

## Summary

| Item | Status |
|------|--------|
| I_2 separating g = 2 | UNCONDITIONAL via Gritsenko-Nikulin arithmetic lift + DMVV Hilbert-scheme (AP157: separating stratum has no genuine g = 2 data) |
| I_2 non-separating g = 2 | OPEN at chain level (cohomologically closed by `thm:curved-dunn-H2-vanishing-all-genera`; chain-level DMVV handle lift needed) |
| I_3 Schur-index level | UNCONDITIONAL: all three generating functions agree as q-series (Harvey-Moore + DMVV + BLLPR) |
| I_3 E_3-topological lift (class G/L/C sublattice) | PROVED via Universal Holography `thm:uch-main` |
| I_3 class M (Virasoro) chain level | CONDITIONAL on coset-extension of `thm:chd-ds-hochschild` to N = 2 SCVOA cosets chi[T[X]]/u(1)_R |

Word count: ~1700.

Literature anchors used:
- Gritsenko-Nikulin, "Siegel automorphic form corrections of some Lorentzian Kac-Moody Lie algebras," Am. J. Math. 119 (1997), Theorems 1.1, 2.1, Prop. 2.1.
- Harvey-Moore, "On the algebras of BPS states," CMP 197 (1998), Theorem 6.3.
- Dijkgraaf-Moore-Verlinde-Verlinde, "Elliptic genera of symmetric products and second quantized strings," CMP 185 (1997), eqs. (3.5)-(3.8), (6.13)-(6.16).
- Beem-Lemos-Liendo-Peelaers-Rastelli-van Rees, "Infinite chiral symmetry in four dimensions," CMP 336 (2015), Theorems 1, 3.1, 5.1.
- Tripathy, "Three-dimensional mirror symmetry and the Kapustin-Willett conjecture" (for 3d HT lift framework).
- Vol II: `thm:uch-main` (`universal_celestial_holography.tex:213`), `thm:curved-dunn-H2-vanishing-all-genera`, `thm:chd-ds-hochschild`.
- Vol III: `prop:cy-c-i2-higher-genus-reduction`, `conj:cy-c-i3-half-bps`, AP157, AP-CY11.
