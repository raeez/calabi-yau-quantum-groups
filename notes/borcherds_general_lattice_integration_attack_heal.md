# Borcherds general-lattice integration: attack then heal

Scope: promote the Φ_10 / Δ_5 / K3×E closure of CY-C I_2 to a general-lattice Borcherds-integration theorem within the programme. Russian school (Gritsenko–Nikulin), Borcherds 1992/1995, Harvey–Moore 1996, Kac–Peterson 1984, Fiorentino 2022 anchors. Conventions as in `k3e_bkm_chapter.tex` (Φ_10 = const · Δ_5² at K3×E).

## 1. Attack

Claim under attack: *The Φ_10-specific closure of CY-C at II_{4,20} = Mukai(K3)⊕II_{1,1} is a mere special case of a universal Borcherds-integration theorem internal to the programme, realising Φ(L) = BKM automorphic lift for every even Lorentzian L of signature (m+2,2).*

Test cases the attack wants to control:
- II_{2,2} (m=0, hyperbolic): heuristic Φ(L) should be a weight-0 modular form on SL_2(Z)×SL_2(Z).
- II_{10,2} (m=8, E_8⊕II_{2,2}): E_8 Borcherds product in 10+2 variables; candidate automorphic form of weight 4 on O(10,2).
- II_{18,2} (m=16, E_8²⊕II_{2,2}): weight 8 on O(18,2).
- II_{26,2} (m=24, Leech⊕II_{2,2}): Fake Monster denominator; weight 12; Borcherds 1992 Monster Lie Algebra.

If the programme's CY-A functor Φ_3 is the source of all these lifts uniformly, CY-C becomes an instance of a universal-lattice Borcherds theorem and the Monster moonshine identity is a CY-A-functorial consequence.

## 2. What does the Φ_10 CY-C closure get RIGHT for general lattices?

**(R1) The universal property is already recorded.** `thm:borcherds-lift-universal` (k3e_bkm_chapter.tex:692, `\ClaimStatusProvedElsewhere`, attributed to Borcherds 1998 Thms. 13.3 and 14.3) gives the four-item universal property for ARBITRARY even unimodular Lorentzian L with b^+ ≥ 2 and any conformal VOA V whose weight lattice admits a primitive isometric embedding L ↪ Lat(V): existence, product expansion e^{2πi(ρ,Z)} ∏_{λ∈L^+, (λ,ρ)>0}(1 − e^{2πi(λ,Z)})^{c_V(−λ²/2)}, functoriality under V- and L-embeddings, and Borcherds weight wt(Φ_V) = c_V(0)/2. This IS a general-lattice theorem — it lives in the chapter already.

**(R2) Three worked cases are already inside the manuscript.** `rem:borcherds-three-cases` (k3e_bkm_chapter.tex:712) pins the abstract universal property to three concrete instances: (1) II_{1,1}/trivial VA → J(τ) − 744; (2) II_{2,26}/Leech VOA → Fake Monster denominator (= Monster Lie Algebra); (3) II_{3,2}/V_{K3}^{top} → Δ_5. These three are exactly the Russian-school backbone (Borcherds 1992 cases + Gritsenko–Nikulin 1996/1997 Igusa form). So II_{2,26} / Monster / Leech IS covered, and the Vol II Monster chain-level closure via Leech orbifold BV (FM66/FM120/FM128) consumes item (2) of this theorem.

**(R3) Weight c_V(0)/2 generalises correctly.** κ_BKM = c_N(0)/2 is proved universal (kappa_bkm_universal.py + k3_times_e.tex + AP-CY37); the Borcherds-weight formula is not Φ_10-specific. For II_{2n+2,2}, the weight is m/2 when the VOA has central charge tuned so that c_V(0) = m. This is precisely the Borcherds 1995 "Automorphic forms on O_{s+2,2}(R) and infinite products" Thm. 10.1 statement, and the programme records it verbatim.

**(R4) Six-route CY-C framework already distinguishes the Φ_3 branch from the five independent branches.** `def:cy-c-six-routes` (cy_c_six_routes_convergence.tex:31) makes explicit that only R_1 is the application of Φ_3; R_2 (Borcherds lift) is an INDEPENDENT construction consuming a weak Jacobi form, not an output of Φ_3. This is the correct categorical posture for a general-lattice extension.

So: the Φ_10 closure is NOT the entirety of the programme's Borcherds theorem. The universal statement is already in the chapter. What is Φ_10-specific is the matching with Φ_3(D^b(Coh(K3×E))) — route R_1 — not the lift itself.

## 3. What does the Φ_10 closure get WRONG when naively generalised?

**(W1) CY-A functor is not defined on abstract lattices.** The functor Φ_3 consumes D^b(Coh(X)) of a CY_3 X, not an abstract even Lorentzian lattice L. The statement "for arbitrary L of sig (m+2,2), what is Φ(L)?" is CATEGORY-CONFUSED: Φ takes a CY-d geometry, not a lattice. `rem:cya3-borcherds-lift-compatibility` (k3e_bkm_chapter.tex:720) is explicit: Φ_3 gives Borcherds input only "on a K3-fibered CY_3 X with Mukai lattice Λ_Muk(X) even unimodular"; for quintic / local P², the second arrow IS UNDEFINED, the substitute is BCOV, not a theta lift. Generalising from "Φ_3 on K3×E" to "Φ on abstract lattices" runs against AP-CY8 (denominator ≠ automatic bar Euler product) and AP-CY59 (Φ outputs a specific period; the other routes are independent).

**(W2) Lattice-to-CY lift is not functorial in the attack direction.** For abstract L, there is no canonical CY_3 whose Mukai lattice is L. II_{26,2} does not arise as Mukai(X) of any compact CY_3: Mukai(K3) = II_{4,20}, and no compact CY_3 has rank-28 Mukai lattice with this signature. So while the Borcherds automorphic lift IS defined for II_{26,2} (that's Borcherds 1992), it cannot be hit by any CY-A output. The Monster Lie Algebra is NOT a CY-A-functorial derivation; it is an independent Borcherds construction living in R_2 space, consumed by the Vol II Monster chain-level closure through Leech orbifold BV, not produced by Φ_3.

**(W3) Vol II Monster chain-level consistency is via Leech VOA, not via Φ_3.** The Vol II Monster E_3-topological route (thm:E3-topological-km applied to V_Leech^+) uses the Leech lattice VOA directly and its Z/2 orbifold. This is route R_3 (lattice VOA) plus orbifold, not route R_1 (Φ_3). The Borcherds 1992 Monster Lie Algebra appears as item (2) in `rem:borcherds-three-cases` via L=II_{2,26} and V=V_Leech, not via CY geometry. Attempting to say "Monster = CY-A-functorial derivation" inverts the provenance: it is Leech-lattice-VOA-functorial, not CY-functorial.

**(W4) "Weight m/2 modular form" is an INPUT to Borcherds, not an output of Φ_3.** Borcherds 1995 Thm. 10.1 requires a weakly holomorphic modular form F of weight (2−n)/2 (i.e., weight −m/2 on the SOURCE, lifting to weight m/2 on the O(m+2,2) target — the Russian-school convention flip). The "modular form extraction" from Φ_3 is the K3 elliptic genus 2φ_{0,1} = vacuum character of V_{K3}^{top}; that extraction works only when the CY-3 has a K3 fibration. For a generic L of signature (m+2,2) with no K3-fibration provenance, the input Jacobi form is supplied by something OTHER than Φ_3 (Leech character / j-function / bespoke lattice VOA).

## 4. Correct relationship

**(C1) Two distinct theorems coexist.**
- **Theorem B̄ (Borcherds universal, programme-internal):** `thm:borcherds-lift-universal` — general-lattice, ProvedElsewhere[Borcherds 1998], applies to any even unimodular Lorentzian L with b^+≥2 and any conformal VOA V with L ↪ Lat(V). This is the general-lattice Borcherds theorem and it IS in the programme already.
- **Theorem R̄_1 (CY-A image, programme-content):** Route R_1 produces A_X^{R_1} = Φ_3(D^b(Coh(X))); this is defined only for K3-fibered CY_3's. On K3×E it lands on V_{K3}^{top}⊗V_E and Theorem B̄ applied there gives Δ_5 = Φ_10^{1/2} up to a constant.

**(C2) CY-C I_2 is route-specific.** The agreement of R_1 with R_2 at II_{4,20} / K3×E is the identification "Φ_3-output matches Leech-like Borcherds-input". The general-lattice extension of THIS identification would require a CY-A functor on lattice data; that functor does not exist, and asserting it would violate AP-CY59/AP-CY60.

**(C3) Monster is consumed, not produced.** The Vol II Monster E_3-topological closure runs through Leech VOA + Z/2 orbifold + II_{2,26} Borcherds denominator — all on the CY-side-independent ROUTE R_3 (lattice VOA), plus the Borcherds universal lift (Theorem B̄ item 2 in `rem:borcherds-three-cases`). DW anomaly vanishing uses II_{2,26}-even-unimodularity + SL_2(Z)-invariance of J(τ), both consequences of Theorem B̄(i)+(iii). This is logically consistent with W3: Vol II consumes the Borcherds lift; it does not CY-A-functorially derive it. AP-CY8 is honoured: the Borcherds denominator of g_{Δ_5} or of the Monster Lie Algebra is NOT automatically a bar Euler product of Φ_3(X); the bridging arrow is separate (HKR-Borcherds functorial lift, `prop:route1-route2-bridge` ClaimStatusConditional).

**(C4) Test cases restated correctly.**
- II_{2,2}, II_{10,2}, II_{18,2}, II_{26,2} all have their Borcherds lifts defined by Theorem B̄ applied to lattice VOAs (route R_3), not by Φ_3. These are lattice-VOA-functorial, not CY-A-functorial.
- II_{4,20} = Mukai(K3)⊕II_{1,1} is EXCEPTIONAL in that its Borcherds lift of 2φ_{0,1} (namely Δ_5 = Φ_10^{1/2}) hits the Φ_3-image of D^b(Coh(K3×E)). This matching — i.e., the CY-C I_2 closure — is Φ_10-specific, not the universal Borcherds theorem.

## 5. Verdict

The programme's CY-C closure does NOT extend to a general-lattice Borcherds-integration theorem INTERNAL to Φ_3, because Φ_3 is defined on CY_3 geometries, not on abstract lattices, and only K3-fibered CY_3's produce even-unimodular Mukai lattices matching the Borcherds hypothesis. The general-lattice Borcherds theorem (item-by-item: existence, product, functoriality, weight c_V(0)/2) IS internal to the programme as `thm:borcherds-lift-universal`, attributed Elsewhere to Borcherds 1998 + Gritsenko–Nikulin. The Φ_10 closure is the INTERSECTION of this universal theorem with the Φ_3 functor at the single point L = II_{4,20}, V = V_{K3}^{top}⊗V_E.

The Monster Lie Algebra case II_{26,2} is consumed by Vol II's E_3-topological Monster route through the Leech VOA, not derived from Φ_3; hence Vol II is consistent with AP-CY59/AP-CY60.

Heal: promote the honest separation into a named structural remark — "Theorem B̄ is universal (lattice-and-VOA-functorial); Theorem R̄_1 is CY-A-functorial only on K3-fibered CY_3's; CY-C I_2 is the matching of these two at L=II_{4,20}." This strengthens rather than downgrades: it exhibits Φ_10 as a COINCIDENCE of two independent universal constructions at a point, which is the strongest honest statement.

---

### Literature anchors (verified in manuscript)

- Borcherds 1992 "Monstrous moonshine and monstrous Lie superalgebras," Invent. Math. 109 (case II_{2,26} → Fake Monster / Monster Lie Algebra).
- Borcherds 1998 "Automorphic forms with singularities on Grassmannians," Invent. Math. 132, Thms. 13.3 and 14.3 (universal singular theta lift, cited via `thm:borcherds-lift-universal` attribution).
- Gritsenko–Nikulin 1997 "Siegel automorphic form corrections of some Lorentzian Kac–Moody Lie algebras," Am. J. Math. (II_{3,2} → Δ_5, Fourier–Jacobi expansion; cited by `cy_c_nonseparating_g2_borcherds_multiplicative_lift_platonic.md`).
- Harvey–Moore 1996 "Algebras, BPS states, and strings," Nucl. Phys. B 463 (BPS-algebra framing; route R_6).
- Kac–Peterson 1984 "Infinite-dimensional Lie algebras, theta functions and modular forms," Adv. Math. (theta-function side of denominator identities).
- Fiorentino 2022 PhD thesis (recent generalisations in Borcherds-product / BKM landscape).

### Programme anchors (manuscript ground truth)

- `thm:borcherds-lift-universal` (k3e_bkm_chapter.tex:692): general-lattice universal Borcherds theorem, four items.
- `rem:borcherds-three-cases` (k3e_bkm_chapter.tex:712): J(τ)−744, Fake Monster / Monster Lie, Δ_5 on II_{3,2}.
- `rem:cya3-borcherds-lift-compatibility` (k3e_bkm_chapter.tex:720): Φ_3 hits Borcherds input only on K3-fibered CY_3; BCOV is the substitute for non-fibered.
- `def:cy-c-six-routes` (cy_c_six_routes_convergence.tex:31): six-route framework separates Φ_3 from the five independent constructions.
- `prop:route1-route2-bridge` (cy_c_six_routes_convergence.tex:74): HKR-Borcherds bridge, ClaimStatusConditional.
- `appendices/first_principles_cache.md:895`: Vol II Monster E_3-top consumes `rem:borcherds-three-cases(2)`, not Φ_3-output.
- `notes/cy_c_nonseparating_g2_borcherds_multiplicative_lift_platonic.md`: prior I_2 non-separating stratum closure.
- AP-CY8 (denominator ≠ bar Euler product), AP-CY37 (κ_BKM = c_N(0)/2 universal), AP-CY59 (Φ outputs one period; other routes independent), AP-CY60 (CY-C = convergence of six routes).

Word count: ~1520.
