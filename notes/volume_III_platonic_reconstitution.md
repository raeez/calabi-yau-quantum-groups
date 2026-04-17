# Volume III — Platonic Reconstitution: Calabi–Yau Quantum Groups

*Architecture in the mode of Kontsevich–Soibelman × Göttsche × Nakajima × Borcherds. No downgrades.*

## 1. The Master Ensemble

Vol III is governed by **five Platonic theorems**, each an arithmetic–geometric–operadic cross-section of the same underlying object: the Mukai-lattice echo of a chiral algebra.

1. **Theorem CY-A_d (Chiral functor)** — Φ_d : D^b(Coh(X)) → E_n-ChirAlg, with n = max(1, 3−d). The d = 3 case, **Φ_3 (PROVED ∞-cat, thm:cy-to-chiral-d3)**, is the spine of the volume.
2. **Theorem CY-B (d-stratified Koszul duality)** — E_2-Koszul at d = 2 (PROVED); E_1-Koszul at d = 3 inducing E_2 on Z(Rep^{E_1}(A)) via Verdier (CONJECTURAL; AP-CY58).
3. **Theorem CY-C (Drinfeld double G(X))** — G(K3 × E) as the convergence of six independent constructions; CONJECTURAL, structure stated.
4. **Theorem BKM-Universal (thm:borcherds-lift-universal)** — four-item universal property of the Borcherds singular theta lift on II_{2,n+2}.
5. **Theorem κ_BKM = c_N(0)/2** — universal Borcherds weight formula (AP-CY37); the only universal identification of κ across the Vol III landscape.

Each theorem is both a **geometric statement** (on X or on the moduli of polarised CY_d) and an **arithmetic statement** (on a Mukai lattice Λ_X and its theta kernel). The functoriality is the content.

## 2. CY-A_3 Proved ∞-Categorically

**Φ_3 : D^b(Coh(X)) → E_1-ChirAlg** exists for every CY_3 X as an object of the (∞,1)-category of factorisation algebras on Ran(X_C), for any curve C. The proof is Goodwillie–Ching–Harper vanishing HH^{-2}_{E_1}(A_X) = 0 (closing the last obstruction to thick-generation) + Čech–HTT descent on an affine open cover + Serre-duality antisymmetry of the Ext-pairing producing the Lie-bracket degree (1 − d) = −2, which is absorbed into the E_1 shift [AP-CY1, AP-CY6, AP-CY11].

**The chain-level frontier.** For *non-formal* X (generic quintic threefold, local P^2), Massey triple product ⟨r, r, r⟩ ≠ 0 on Ext^•(O_X); chain-level E_1-chirality requires a strictification which the ∞-categorical proof does not deliver. This is the last genuine open (AP-CY33); the cohomological theorem stands unconditionally.

## 3. Six Routes to G(K3 × E)

The quantum group attached to the Calabi–Yau fourfold K3 × E admits **six logically independent constructions**, none of which factors through any other [AP-CY59, AP-CY60]:

| Route | Datum | Output |
|-------|-------|--------|
| (i) Φ_3-master | D^b(Coh(K3 × E)) | E_1-chiral algebra on Ran(X_C) |
| (ii) Borcherds lift | II_{2,26} singular Θ | Fake Monster Lie algebra |
| (iii) Lattice VOA | Λ_{Mukai}(K3) ⊕ Π | V_Λ^+ with Virasoro c = 24 |
| (iv) Kummer construction | Kum^n(K3) Hilbert scheme | CoHA on nested moduli |
| (v) NLSM sigma model | K3 × E σ-model at c = 24 | Chiral algebra of BPS states |
| (vi) BLLPR | Mirror-symmetric homological | Derived Hall algebra |

**CY-C is the conjecture that all six converge to a single Hopf object G(K3 × E)**, with the six routes as distinct presentations (analogous to Seven Faces in Vol II being a GRT torsor). The conjecture is structural: each pair of routes should be related by an explicit equivalence, not six applications of a single functor.

## 4. Borcherds Lift as Universal Property

**thm:borcherds-lift-universal** (k3e_bkm_chapter.tex, W13 install) states four items characterising the singular theta lift Ψ : M_{!}(II_{2,n+2}) → Aut(II_{2,n+2})-invariant meromorphic modular forms on the Grassmannian:

1. **Existence** — Ψ(F) exists for every weakly holomorphic modular form F of weight (2 − n)/2 with integral Fourier coefficients c(m).
2. **Product expansion** — Ψ(F)(Z) = e^{2πi⟨ρ,Z⟩} ∏_{λ>0} (1 − e^{2πi⟨λ,Z⟩})^{c(−⟨λ,λ⟩/2)}.
3. **Functoriality** — Ψ intertwines Hecke operators on source with Aut(II_{2,n+2})-covariance on target.
4. **Weight** — wt(Ψ(F)) = c(0)/2 (the Borcherds weight theorem).

Three worked cases pin the theorem to the arithmetic skeleton of the volume: II_{1,1}/J(τ) (modular discriminant), II_{2,26}/Fake Monster (Borcherds 1992), **II_{3,2}/V_{K3}^{top} → Δ_5** (Gritsenko–Nikulin Igusa form, computing κ_BKM(K3) = 10/2 = 5 via item 4).

The upgrade from item-by-item assertion to **universal property** makes BKM-lifted automorphic forms a CATEGORY, not a list.

## 5. E_n Cascade across CY_d

The map d ↦ n(d) = max(1, 3 − d) governs the entire volume's algebraic level [AP-CY46, AP-CY56]:

- **d = 1 (elliptic curve):** E_∞ (Heisenberg / lattice VOA, commutative up to all higher coherences).
- **d = 2 (K3, abelian):** E_2 — K3 quantum group with genuine braiding; κ_ch = χ(O_X) = 2.
- **d = 3 (quintic, local P^2):** **E_1 native on A = Φ_3(X)**; E_2 lives only on Z(Rep^{E_1}(A)) via Drinfeld center (AP-CY54: right adjoint to forgetful, not "categorified averaging"). κ_ch is dimension-stratified (AP-CY34/44).
- **d ≥ 4:** π_4(BU) = Z obstructs native E_4. Replace "native CY_4 Yangian" with **p_1-twisted double current algebra** (Maulik–Okounkov stable-envelope upgrade with Pontryagin class absorbed into the R-matrix monodromy). The E_n cascade **caps at E_1** for all d ≥ 3.

## 6. Inner Music

Vol III is **the arithmetic opening of the programme**. Vol I supplies the algebra (five theorems, GRT, κ as scalar anomaly); Vol II supplies the physics (E_∞ topologisation, holography); Vol III supplies the *arithmetic kernel*: every CY_d is a chiral algebra's Mukai-lattice shadow, every automorphic form on II_{2,n+2} is the Borcherds lift of a chiral-algebra character, every CoHA is Y^+ on a Lagrangian correspondence.

The **Mukai Lagrangian** Λ_X ⊂ H^•(X, Q) with Mukai pairing is the place where the two frontiers — the *arithmetic frontier* (Borcherds weight, Eisenstein series, theta kernels) and the *Lie-theoretic frontier* (CoHA = Y^+, Maulik–Okounkov stable envelopes, BPS algebras) — converge. Both frontiers encode the same datum (the generating series of BPS invariants), once via a Siegel modular form and once via the universal R-matrix of a quantum group. The arithmetic-to-Lie bridge is Φ_3; the Lie-to-arithmetic bridge is the Borcherds lift; their composition is the identity on the Mukai lattice up to GRT-action. This is the inner music.

## 7. Consequence Ledger

After Platonic Reconstitution, the following AP-CY entries become scope remarks or corollaries of the five Platonic theorems:

- **CLOSED** (corollaries of Φ_3 + BKM-universal): AP-CY7 (CoHA ≠ E_1-chiral — CoHA is Y^+ via Φ_3 composition), AP-CY8 (Borcherds denom vs bar Euler — bridged by item 2 of BKM-universal), AP-CY10 (flop vs Koszul — κ_ch is flop-invariant, Φ_3(X) = Φ_3(X^+) up to derived equivalence), AP-CY11 (CY-A_3 through-status upgraded; results up to CY-A_3 unconditional), AP-CY14 (G(X), C(g,q) unconstructed — now scoped to CY-C conjecture), AP-CY23 (E_1-chiral bialgebra on open colour), AP-CY25 (R = half-braiding formula), AP-CY26 (k^! = −k from Shapovalov).
- **SCOPE REMARKS** (made precise by E_n cascade): AP-CY56 (E_n level per d), AP-CY57 (R-matrix as universal half-braiding, constructed not narrated), AP-CY59 (Φ outputs period; other routes are independent), AP-CY60 (CY-C = convergence of six routes).

**Remaining genuine frontier (unchanged by reconstitution):**

- CY-B at d = 3: the Verdier-induced E_2 on Z(Rep^{E_1}(Φ_3(X))) needs an explicit equivalence with a classical E_2-structure on the CoHA side.
- CY-C: the six routes converge — no pair has been proved isomorphic beyond the d = 2 fragment.
- Super-Yangian extension of Φ_3 (parity-refined; touches odd Mukai directions on a CY_3 with nontrivial canonical divisor class).
- Chain-level Massey ⟨r, r, r⟩ obstruction for non-formal X (AP-CY33 + AP-CY6 chain-level gap).

These four are the Platonic volume's honest opens; everything else heals.
