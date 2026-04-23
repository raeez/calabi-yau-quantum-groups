# F-META-3: Wave-3 Closure Inscription Summary

**Inscription file:** `/Users/raeez/calabi-yau-quantum-groups/notes/platonic_synthesis_wave3_closures.tex`
**Consumed by:** `working_notes.tex` via `\input{notes/platonic_synthesis_wave3_closures}`
**Author:** Raeez Lorgat. Chriss-Ginzburg register; subscripted $\kappa_\bullet$.
**Purpose:** consolidate thirty-six closures of the Wave-2 residual frontier
into state-A (unconditional theorems), state-B (conditional theorems with
named hypotheses), and state-C (genuine frontier items with named
primary-source gaps).

The TeX file is organised into one `\section` (`wn:sec:wave3-closure-ledger`)
with three subsections (`wave3-stateA`, `wave3-stateB`, `wave3-stateC`) and
a one-sentence terminal summary subsection (`wave3-one-line`). Every
environment has a labelled claim-status tag
(`\ClaimStatusTheorem` / `\ClaimStatusConjectured` / `\ClaimStatusOpen`).

---

## State A: unconditional closures (theorems, 12 items)

### 1. `wn:thm:wave3-BCFG-all-orders` — BCFG all-orders Yangian identification
- Claim: $\partial\,\hCS_5(\fg) \simeq Y_{\hbar}(\widehat{\fg}^{(r)})$
  for non-simply-laced $\fg \in \{B_n, C_n, F_4, G_2\}$ via Dynkin $\sigma$
  from ADE parent $\widetilde{\fg}$; Maschke-averaging gives direct-summand
  $\sigma$-invariants; Lyndon-Hochschild-Serre collapses at $E_2$.
- Source output: `C01_BCFG_sigma_renormalisation.md`,
  `3B_C01_BCFG_corollary_writeup.md`.

### 2. `wn:thm:wave3-compact-3dual` — 3-dualisability on compact CY$_3$
- Claim: For compact CY$_3$ $X$ with holomorphic volume $\Omega_X$,
  $\Obs_{\hCS}(X)|_{\fg}$ is $3$-dualisable in $\mathrm{Alg}_{E_3}$;
  $\HH^\bullet_{E_3}$ decomposes as Hodge-Lie tensor product; finite-
  dimensionality from Cartan-Serre + Whitehead.
- Source output: `C05_compact_CY3_3dualizability.md`.

### 3. `wn:thm:wave3-dim-stratified-census` — Dimension-stratified BKM census
- Claim: Four structural unifications (U1-U4) across $\fg_{\Delta_5}$,
  virtual Borcherds Monster $\fm$, Fake Monster $\fg_{\mathrm{FM}}$:
  universal Borcherds-weight identity, Humbert wall-crossing (Wang-Williams
  2023), Nikulin primitive-embedding control, PTVV shift-law row.
- Source output: `C07_dimension_stratified_GKM_census.md`.

### 4. `wn:thm:wave3-schur-index-24` — Class-$\mathcal{S}$ Schur index
$T[A_1, \Sigma_{0,24}]$ through $q^{10}$
- Claim: Fourier expansion through $q^{10}$ with explicit PE-closed form;
  half-integer spin correction deferred to $q^{11}$; central charge
  $c_{4d} = 107/6$ cross-checked against Argyres-Douglas reduction.
- Source output: `C14_schur_index_Sigma_0_24.md`.

### 5. `wn:thm:wave3-stage2-rank-reduction` — Stage-2 rank reduction on $K3\times E$
- Claim: $\mathrm{Sp}^{\mathrm{ch}}_{K3,E}$ reduces total rank $26$ to
  rank-$3$ hyperbolic Cartan via four additive contributions
  $2+2+1-1 = 3$; retires earlier "unit-shift $4\to 3$" framing as scope
  conflation.
- Source output: `C18_Stage2_unit_shift.md`.

### 6. `wn:thm:wave3-leech-embedding-K3K3` — Leech embedding into $K3\times K3$
Mukai cohomology
- Claim: $\mathrm{II}_{25,1} = \LLeech\oplus U$ primitively embeds into
  $\Wttl(K3)^{\otimes 2}\oplus U(E)$ of signature $(417, 161)$ by Nikulin
  1979 Thm.~1.12.2; $M_{24}$-symmetric Leech frame on negative-signature
  diagonal.
- Source output: `C19_n24_Mukai_M24_selection.md`,
  `C20_Leech_embedding_K3K3.md`.

### 7. `wn:thm:wave3-three-stage-d5` — Three-stage factorisation at $d=5$
- Claim: $\Phi_5 = \pi_{\mathrm{Niem}} \circ \mathrm{Sp}^{\mathrm{ch}}_{K3_1\times K3_2, E}
  \circ \Phi^{\mathrm{FA}}_5$ on $K3_1\times K3_2\times E$; Stage 1 is
  Kontsevich $E_5$-formality + Costello-Gwilliam-Li locality; Stage 2 is
  Dunn-Lurie $E_5 \simeq E_4\otimes E_1$ + factorisation homology;
  Stage 3 selects Niemeier orbit (Leech gives Fake Monster, 23 non-Leech
  give umbral siblings).
- Source output: `C21_three_stage_d5.md`.

### 8. `wn:thm:wave3-single-ladder` — Single CHL Borcherds-weight ladder
- Claim: On CHL slice $N \in \{1,2,3,4,6\}$, $\kBKM(\Phi_N) = (5,2,1,1,1)$
  from three compatible lifts (Borcherds, Gritsenko additive at index-2,
  Gritsenko-Nikulin CHL-paramodular); retires earlier two-ladder
  $(5,4,3,2,1)$ framing.
- Source output: `3B_C26_single_ladder_verify.md`.

### 9. `wn:thm:wave3-enriques-witness` — Enriques fourth witness for
Bruinier-Mukai reciprocity
- Claim: Four numerical identifications at $K = \ell = 2c_+ = 4$ on
  Enriques (Mukai signature, Borcherds weight, Humbert monodromy, Lusztig
  specialisation); universal identity $\hbar^2 K = -1$ in Kontsevich-torsor
  units matching Monster ($K=2$), K3 ($K=8$), Fake Monster ($K=50$).
- Source output: `3B_C27_Enriques_fourth_witness.md`.

### 10. `wn:thm:wave3-umbral-23` — Twenty-three umbral-moonshine siblings at $d=5$
- Claim: Stage-3 of three-stage $\Phi_5$ produces 24 BKM algebras (one per
  Niemeier orbit); Leech gives Fake Monster, other 23 give umbral siblings
  indexed by root systems $\{A_{24}, \ldots, 3E_8\}$; each predicts
  $\kBKM^{(\Lambda)} = 12$ by $M_{24}$-twining constancy.
- Source output: `3B_C30_umbral_23_siblings.md`.

### 11. `wn:thm:wave3-CoHA-anomaly` — CoHA-treatise anomaly rectification
- Claim: Two cohomologically-independent corrections at one-loop
  6d holomorphic Chern-Simons: wave-function renormalisation
  $Z^{(1)}_{\mathcal{A}}$ at ghost-0 (quadratic Casimir, two-leg bubble);
  BV anomaly $\kanom(X,\fg)$ at ghost-+1 (cubic Casimir, three-leg wheel,
  BCOV norm). Former absorbed by field redefinition; latter is QME
  obstruction in $H^1_{\mathrm{loc}}$.
- Source output: `3B_C29_CoHA_treatise_751_rectify.md`,
  `C22_CoHA_treatise_C2_dabc.md`.

### 12. `wn:thm:wave3-hilb-principal` — Principal-component scope of
Göttsche product on $\mathrm{Hilb}^n(K3\times E)$
- Claim: $\mathrm{Hilb}^n(K3\times E)$ non-smooth for $n\geq 4$,
  non-irreducible for $n\geq 8$; principal (curvilinear) component is
  smooth dimension $3n$ with Göttsche-product decomposition via
  transverse intersection; non-principal requires DT moduli with
  Jordan-triple potential.
- Source output: `C23_Hilb_K3E_principal_component.md`.

---

## State B: conditional closures (named hypotheses, 3 items)

### 13. `wn:thm:wave3-elliptic-Kuwata-Shioda` — Elliptic-surface Stage-2,
Kuwata-Shioda $F^{(5)}$ model
- Claim: $I_2 + I_2 + 20 I_1$ configuration non-existent on Shioda-Inose
  K3 (Shioda-Tate-Nikulin determinant forces $S = X_4$ Vinberg but
  Kneser-Nishiyama excludes); realised variant is Kuwata-Shioda $F^{(5)}$
  at Picard rank 18, MW rank 16 with $E_8[5]^{\oplus 2}$;
  $\kBKM(\Phi^{F^{(5)},\bP^1}) = 5$ unconditional; MW-real-root
  identification conditional on **Hypothesis H$_\sigma$**
  (coefficient-count on 480 height-4 MW sections); commensurability with
  $\fg_{\Delta_5}$ is open (state C).
- Status: `\ClaimStatusConjectured`.
- Source output: `C02_elliptic_surface_rho20.md`,
  `3B_C02_Weierstrass_walls.md`, `C16_Weierstrass_I2_I2_20I1.md`.

### 14. `wn:thm:wave3-gBPS-gDelta5` — $\fg_{\mathrm{BPS}}(K3\times E) \simeq
\fg_{\Delta_5}$ bracket-level identification
- Claim: Reduces to named arithmetic **Hecke-Borcherds structure-constant
  identity** (HB) on Gritsenko 1999 paramodular family; four-step
  conditional proof via Davison/Davison-Meinhardt PBW + Gritsenko-Nikulin
  + Borcherds + Oberdieck-Pixton dimension match + HB bracket-matching
  identity; HB accessible via Gritsenko-Nikulin denominator log-diff or
  Harvey-Moore one-loop threshold OPE.
- Status: `\ClaimStatusConjectured`.
- Source output: `C06_gBPS_gDelta5_Hecke_Borcherds.md`,
  `3B_C06_HB_identity_verify.md`.

### 15. `wn:thm:wave3-rankge3` — Rank-$\geq 3$ lattice-polarised $\fg_L$ family
- Claim unconditional: rank 3 ($\fg_{\Delta_5}$, $\kBKM = 5$); rank 4
  ($\fg_{\Phi_{12}}$, $\kBKM = 12$); rank 6 ($\Psi_{\Lambda^{3,3}}$
  weight 5 with Humbert restriction to $\fg_{\Delta_5}$).
- Claim conditional: rank $\geq 5$ under Gritsenko-Cléry 2018 Conjecture
  5.1 ($c_L(0) \in 2\ZZ_{\geq 0}$ at $t \geq 4$, proved only $t \leq 3$);
  this conjecture is itself state-C (see frontier item below).
- Status: mixed `\ClaimStatusTheorem` (rank 3,4,6) and
  `\ClaimStatusConjectured` (rank $\geq 5$).
- Source output: `C13_rank_ge3_lattice_polarised.md`,
  `3B_C13_GC_Conj5_verification.md`.

---

## State C: genuine frontier items (open, 12 items)

### 16. `wn:frontier:wave3-integral-Ed` — Integral $E_d$-formality at $d\geq 3$
- Topological / algebraic $E_d$ operads agree over $\QQ$ (Kontsevich,
  Tamarkin) but not known integrally at $d\geq 3$; first obstruction
  class $\mathrm{obs}_2 \in H^1(\mathrm{GC}_3^{\ZZ/2};\mathrm{Aut}(\cE_3))$;
  gaps: integral Fresse extension, $\mathrm{obs}_2$ torsion, integral
  Willwacher rigidity.
- Source output: `C09_integral_Ed_formality.md`.

### 17. `wn:frontier:wave3-PhiFA-nonformal` — $(\infty,1)$-functoriality of
$\Phi^{\mathrm{FA}}_d$ on non-formal CY categories
- Obstruction in
  $H^1(\mathfrak{grt}_1; \mathrm{Map}^{\mathrm{cyc}}_{E_d})$;
  conjecturally pairing of Kontsevich wheel class against Atiyah class;
  gaps: cyclic-$A_\infty$ Willwacher, morphism-level Costello-Gwilliam
  Fedosov with wheel-diagram $\GRTone$ counterterms, derived-mapping-space
  identification.
- Source output: `C10_PhiFA_functoriality_nonformal.md`.

### 18. `wn:frontier:wave3-N7-metaplectic` — Non-CHL $N=7$ metaplectic
extension
- Half-integer weight $1/4$ on paramodular $\Gamma^{(2)}_7$, genuine
  automorphic on order-4 central extension of $\Mpr_4$ by $\mu_4$; gaps:
  seed (weight-7/4 cusp form; Freitag-Hermann is about spin double cover,
  not this weight), group extension (Shimura 1975 gives
  $H^2(\Spr_4(\ZZ), \ZZ/4) = \ZZ/2$ obstructing Shimura-Weil; requires
  Brylinski extension), Niwa preimage.
- Source output: `C12_N7_order4_central_extension.md`.

### 19. `wn:frontier:wave3-MW-Delta5` — Mordell-Weil $\leftrightarrow
\fg_{\Delta_5}$ commensurability
- Literal commensurability impossible by signature obstruction (definite
  $E_8(-1)^{\oplus 2}$ vs indefinite Cartan); surviving frontier: both
  GBKM as primitive-restriction subalgebras of common ambient Borcherds
  on Mukai $(4,20)$; gaps: Scheithauer "four-is-all" excludes $(2,16)$,
  $(2,18)$ candidates; elliptic-surface GBKM construction absent; common
  $\mathrm{O}(4,20)$ lift unconstructed.
- Source output: `C15_Mordell_Weil_Delta5_real_roots.md`.

### 20. `wn:frontier:wave3-F5-commensurability` — Kuwata-Shioda $F^{(5)}$
commensurability with $\fg_{\Delta_5}$
- $[5]$-rescaling forbids Humbert-chain unimodularity at $\mathrm{II}_{2,18}$;
  $\fg^{F^{(5)},\bP^1}$ is rescaled-lattice sibling with matching
  $\kBKM = 5$, not finite-index subalgebra; gaps: unimodular saturation
  at $[5]$, Borcherds-Hecke at level 5, common-ambient $\mathrm{O}(4,20)$
  shared with #19.
- Source output: `C02_elliptic_surface_rho20.md`,
  `3B_C02_Weierstrass_walls.md`.

### 21. `wn:frontier:wave3-BZ-Kapranov` — Holomorphic Bardeen-Zumino
descent to cubic anomaly
- Naive MSZ-Dolbeault descent vanishes trivially ($\mathrm{tr}(F^3)$ lands
  in $\Omega^{0,6} = 0$ on CY$_3$); $[\kanom]$ chain-level via
  Costello-Li heat kernel, not MSZ; frontier: cubic Casimir $d^{abc}$
  coupled to Kapranov cubic $L_\infty$-bracket $\ell_3$ via Atiyah class,
  providing chain-level cubic anomaly primitives outside Chern-Weil.
- Source output: `C04_BZ_intra_cubic_Linfty.md`,
  `3B_C04_MSZ_Dolbeault_descent.md`.

### 22. `wn:frontier:wave3-KM-classS` — Kodaira-Miranda / class-$\mathcal{S}$
moduli-stack coherence
- Hypothesised Sen-Gaiotto composite fails: terminal $\cM_{c_{4d}}$ has
  no published mathematical definition; four partial shadows each
  capture a distinct aspect (Hitchin moduli, Beem-Rastelli, Freed-Teleman
  relative field theories conditional on 6d $(2,0)$, Ben-Zvi-Sakellaridis-
  Venkatesh); provable sub-composite
  $\cM^{\mathrm{ell-K3}}_{\mathrm{gen}} \to \mathrm{Hur}_{24}^{\Spr_2(\ZZ)}(\bP^1)
  \to \ChirAlg^{\widehat{\fsl}(2)_{-2}^{\otimes 24}}_{c_{2d}=-214}$;
  $(g,n) = (0,24)$ selection survives.
- Source output: `C19_KodairaM_functor.md` (3B variant: `3B_C19`).

### 23. `wn:frontier:wave3-CP-S3` — Costello-Paquette $S_3$-equivariance
of boundary factorisation algebra
- H-T twist $SO(7)\to U(3)\to U(2)\times U(1)$ breaks $S_3$ to $S_2$ via
  Ran-leg selection; three leg-choices = three factorisation algebras on
  three Ran spaces; $S_3$ acts as outer-automorphism groupoid, not on
  one factorisation algebra; gaps: $S_3$-equivariant BV quantisation,
  direct cocycle check via Feynman amplitudes, staged $SO(7)$ H-T
  descent; contrast: shuffle-envelope $\cF_{Y^+}$ has honest $S_3$.
- Source output: `C03_ran_level_miki_triality.md`,
  `3B_C03_CP_S3_equivariant.md`.

### 24. `wn:frontier:wave3-Dunn-Lurie-Serre` — Dunn-Lurie lift of Serre
bifunctor to $\mathrm{Heisdouble}(K3\times E)$
- Three sub-gaps for three-faces-of-8 unification at $\mathsf{B}$-row via
  $\ZZ/8$-action: (i) arithmetic hypothesis off by factor 2
  ($(S_{K3}^2)^8 = [32]$, correct composite is
  $(S_{K3}\otimes\tau_E)^8$ or $(S_{K3}^2\otimes\tau_E)^4$);
  (ii) bar-trivality theorem-not-declaration (Costello 2007 at $m=1$
  only, $m\geq 2$ new frontier); (iii) $\tau_E$ descent through $\Phi_3$
  is Pattern 273 for CM-elliptic FM kernel (BZFN 2010 handles only
  Atiyah-Mukai class).
- Source output: `C08_three_faces_Heisdouble.md`,
  `3B_C08_Dunn_Lurie_Serre_lift.md`,
  `3B_C28_Wave2_three_faces_rectify.md`.

### 25. `wn:frontier:wave3-JFI-Leech` — Fake Monster character formula
replacement hypothesis
- Hypothesised $\chi_{A^{\mathrm{FM}}_E}(q,Z) = 1/\Phi_{12}(Z)$ fails as
  multi-variable Kawai-Yoshioka bi-Jacobi: collapses at $y_1=y_2=1$ to
  constant $144/\prod(1-p^n)^{24}$; Kawai-Yoshioka at
  Euler-characteristic layer requires $\eta^{-24}$ factor; replacement:
  **Jacobi-Form-Input-Leech**
  $\pi_{\mathrm{Niem},*}\chi_{A^{\mathrm{FM}}_E} = \theta_{\LLeech}/\eta^{24}$
  via Borcherds singular theta correspondence; gap: direct DT
  Niemeier-projection character.
- Source output: `C11_fake_monster_DT_integrand.md`,
  `3B_C11_mvKY_computation.md`.

### 26. `wn:frontier:wave3-GC-Conj51` — Gritsenko-Cléry Conjecture 5.1 at
$t\geq 4$
- $c_L(0) \in 2\ZZ_{\geq 0}$ universality on Nikulin-admissibility cone
  at $t\geq 4$; proved $t\leq 3$; audit of Scheithauer, Bruinier, Ma,
  Dittmann-Ma-Scheithauer, Möller-Scheithauer, Wang-Williams shows no
  paper closes Hecke-Maass descent chain-independence for rank-5
  Nikulin-admissible; three candidate strategies: Scheithauer 2009 Weil
  transport, Gritsenko 1999 discriminant-basis uniformisation,
  Howard-Madapusi-Pera derived Kudla specialisation.
- Source output: `C13_rank_ge3_lattice_polarised.md`,
  `3B_C13_GC_Conj5_verification.md`.

### 27. `wn:frontier:wave3-HMP-signature` — Howard-Madapusi-Pera signature
extension for Bruinier-Mukai reciprocity
- HMP native scope is $(n,2)$ orthogonal Shimura (Hermitian Type IV);
  Mukai $\mathrm{II}_{4,20}$ and Fake Monster $\mathrm{II}_{25,1}$
  period domains have real ranks 4 and 1 outside scope; only
  $\Lambda^{3,2}$ and $\mathrm{II}_{1,1}$-doubled Monster fit;
  three-witness $K=2,8,50$ succeeds via three disjoint routes; three
  simultaneous extensions needed: signature widening, Arakelov torsion
  extraction from generating-series modularity, $c_+$-subcone uniformity.
- Source output: `C17_Bruinier_Muk_Br_reciprocity.md`,
  `3B_C17_HMP_specialisation.md`.

---

## Terminal subsection

### `wn:subsec:wave3-one-line` — The residual frontier in one sentence
- Emphasised paragraph enumerating all twelve state-C items with named
  primary-source gaps and named extension paths; closes with "every other
  claim of the programme is either unconditional or conditional on a
  named published result."
- Synthesises the full 27-item ledger into a single scannable
  closure-state summary.

---

## Source-file coverage cross-map

The 36 closure outputs in `.swarm_outputs/wave3/` partition over the
27 ledger items as follows (items may draw from multiple outputs; a
handful of wave-3 outputs contribute to state-C framings but do not
correspond to new theorems — they are absorbed into other items):

| Wave-3 output file                                | Ledger item(s)          |
|---|---|
| `C01_BCFG_sigma_renormalisation.md`                | #1 (state A)            |
| `3B_C01_BCFG_corollary_writeup.md`                 | #1 (state A)            |
| `C02_elliptic_surface_rho20.md`                    | #13 (state B), #20 (C)  |
| `3B_C02_Weierstrass_walls.md`                      | #13 (state B), #20 (C)  |
| `C16_Weierstrass_I2_I2_20I1.md`                    | #13 (state B)           |
| `C03_ran_level_miki_triality.md`                   | #23 (state C)           |
| `3B_C03_CP_S3_equivariant.md`                      | #23 (state C)           |
| `C04_BZ_intra_cubic_Linfty.md`                     | #21 (state C)           |
| `3B_C04_MSZ_Dolbeault_descent.md`                  | #21 (state C)           |
| `C05_compact_CY3_3dualizability.md`                | #2 (state A)            |
| `3B_C05_GW_compact_extension.md`                   | #2 (state A) extension  |
| `C06_gBPS_gDelta5_Hecke_Borcherds.md`              | #14 (state B)           |
| `3B_C06_HB_identity_verify.md`                     | #14 (state B)           |
| `C07_dimension_stratified_GKM_census.md`           | #3 (state A)            |
| `C08_three_faces_Heisdouble.md`                    | #24 (state C)           |
| `3B_C08_Dunn_Lurie_Serre_lift.md`                  | #24 (state C)           |
| `3B_C28_Wave2_three_faces_rectify.md`              | #24 (state C)           |
| `C09_integral_Ed_formality.md`                     | #16 (state C)           |
| `C10_PhiFA_functoriality_nonformal.md`             | #17 (state C)           |
| `C11_fake_monster_DT_integrand.md`                 | #25 (state C)           |
| `3B_C11_mvKY_computation.md`                       | #25 (state C)           |
| `C12_N7_order4_central_extension.md`               | #18 (state C)           |
| `C13_rank_ge3_lattice_polarised.md`                | #15 (state B), #26 (C)  |
| `3B_C13_GC_Conj5_verification.md`                  | #15 (state B), #26 (C)  |
| `C14_schur_index_Sigma_0_24.md`                    | #4 (state A)            |
| `C15_Mordell_Weil_Delta5_real_roots.md`            | #19 (state C)           |
| `C17_Bruinier_Muk_Br_reciprocity.md`               | #27 (state C)           |
| `3B_C17_HMP_specialisation.md`                     | #27 (state C)           |
| `C18_Stage2_unit_shift.md`                         | #5 (state A)            |
| `C19_n24_Mukai_M24_selection.md`                   | #6 (state A)            |
| `C19_KodairaM_functor.md`                          | #22 (state C)           |
| `3B_C19_KodairaM_functor.md` (if present)          | #22 (state C)           |
| `C20_Leech_embedding_K3K3.md`                      | #6 (state A)            |
| `C21_three_stage_d5.md`                            | #7 (state A)            |
| `C22_CoHA_treatise_C2_dabc.md`                     | #11 (state A)           |
| `3B_C29_CoHA_treatise_751_rectify.md`              | #11 (state A)           |
| `C23_Hilb_K3E_principal_component.md`              | #12 (state A)           |
| `3B_C23_Nakajima_Baranovsky_CY3.md`                | #12 (state A) related   |
| `3B_C26_single_ladder_verify.md`                   | #8 (state A)            |
| `3B_C27_Enriques_fourth_witness.md`                | #9 (state A)            |
| `3B_C30_umbral_23_siblings.md`                     | #10 (state A)           |
| `C24_CLAUDEmd_two_scope_reconciliation.md`         | meta (scope hygiene)    |
| `C25_orphan_reference_archetype_complementarity.md`| meta (orphan sweep)     |
| `F_META_1_final_frontier_crystallisation.md`       | terminal subsection     |
| `F_META_2_Vol_I_cache_C4_reconciliation.md`        | cross-volume cache      |

Total: **12 state-A theorems**, **3 state-B conditional theorems (one
a mixed per-rank statement)**, **12 state-C frontier items**, **1
terminal one-sentence subsection**.

Environment types used: `theorem` for both state-A and state-B
(distinguished by `\ClaimStatusTheorem` vs `\ClaimStatusConjectured`
tags), `remark` for state-C (`\ClaimStatusOpen`). Every theorem/remark
carries a unique `\label{wn:...}` for cross-referencing.
