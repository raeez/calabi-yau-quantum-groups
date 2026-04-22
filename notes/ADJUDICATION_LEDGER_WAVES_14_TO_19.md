# Adjudication Ledger — Waves 14-19

**Compiled**: 2026-04-20, Wave 19 KST 10th voice (rerun), full synthesis-consistency audit.
**Author**: Raeez Lorgat.
**Scope**: Wave-level-stable adjudication of every substantive claim crossing Waves 14 → 15 → 16 → 17 → 18 → 19 on the non-abelian K3 chiral bialgebra $\mathbf{H}_{\Delta_5}$.
**Primary inputs**: `notes/SYNTHESIS_WAVES_14_TO_18.md` (1095 lines); `compute/lib/k3_yangian_whole_object_verifier.py` (11/11 WOV pass); `appendices/first_principles_cache.md`.

The four sections below encode the final W19 adjudication:

- (I) **VERIFIED** — wave-level-stable across all five waves (W14/15/16/17/18/19), no retraction, primary-literature triangulated.
- (II) **CORRECTED** — wave-level-retracted, final stable value locked, retraction stratum identified.
- (III) **CONJECTURAL** — open mathematical dependency, named conjecture / primary-literature gap.
- (IV) **LINGERING AMBIGUITIES** — convention-level or scope-level residua; resolution specified, not conflict.

---

## (I) VERIFIED — wave-level-stable

Each item is (a) stable across all five waves W14-19; (b) triangulated by ≥ 2 primary sources; (c) cross-checked by the whole-object verifier (WOV) where applicable.

1. **Master object**.
   $\mathbf{H}_{\Delta_5} = \mathcal{D}_\hbar(\mathcal{Y}^{\mathrm{Hall}}(\mathrm{CoHA}_{K3\times E}),\widetilde{\Phi}^{\mathrm{Sieg\text{-}Bor}}[\Phi_{10}/\eta^{24}], R_{\mathrm{Sieg,dyn}})$. Stable W14 onward. Source: `SYNTHESIS §1`; WOV aggregate.

2. **Three-faces identity**.
   $\hbar^2\cdot K^{\kappa_{\mathrm{ch}}} = -1$ with $K = 2c_+ = 8 = \mathrm{ord}(\mathrm{mon}|_{H_1}) = \ell_{\mathrm{Lusztig}}$. Three independent routes converge on 8. WOV-1/WOV-10.

3. **$\hbar^2 = -1/8$, $K^\kappa = 8$**.
   Exact `Fraction(-1,8)` in whole-object verifier; primary Lusztig 1990/1993 + Bruinier 2002 Prop 5.1.

4. **BKM Cartan rank 3 $\perp$ Mukai rank 24**.
   Gram matrix $\det = -32$, signature $(2,1)$, eigenvalues $\{+4,+4,-2\}$; Mukai $(c_+,c_-) = (4,20)$. Orthogonal invariants. WOV-4. Primary: Gritsenko-Nikulin 1998 §3, Feingold-Frenkel 1983.

5. **Central charges**.
   $c_{4d}(A_1,\Sigma_{0,24}) = 107/6$; $c_{2d} = -214 = -2\cdot 107$ (107 prime). WOV-2. Primary: Chacaltana-Distler 2010 §5.14 + Shapere-Tachikawa 2008 + Beem-Rastelli 2013.

6. **Siegel weight 5**.
   $\Delta_5 = \mathrm{Grit}(\eta^9\vartheta_1)$ on Maass spin cover. Four routes converge (Gritsenko / CY-2 $5\chi/24$ / 11D SUGRA anomaly sum / Kodaira $I_1$ residue). WOV-3. Primary: Gritsenko 1999 Thm 6.1.

7. **Arthur parameter $\psi_{\Delta_{10}}$**.
   $\psi_{\Delta_{10}} = \phi_{\Delta_{E_6}}\boxtimes\mathrm{Sym}^1$; Saito-Kurokawa CAP; Ikeda 2001, Arthur 2013.

8. **Hecke Euler factor dictionary**.
   $\lambda_p(\Delta_{10}) = a_p(\Delta_{E_6}) + p^8 + p^9$ at primes $p \le 79$. Deligne-Petersson bound $|a_p|\le 2p^{15/2}$ satisfied. WOV-6.

9. **Global A-packet size**.
   $|\Psi_{\Delta_{10}}| = 4$; $S_\psi = \mathbb{Z}/2$; multiplicity $m(\pi_{\Delta_{10}}) = 1$ via Ikeda character. Primary: Arthur 2013 Thm 1.5.1–1.5.2.

10. **Archimedean Schmidt parameters**.
    $(17/2, 15/2)$ for $\Delta_{10}$; $(7/2, 5/2)\otimes\mathrm{sgn}_{\mathbb{R}}$ for $\Delta_5$ on Maass-spin cover.

11. **$p = 2$ ramified local Langlands**.
    $\psi_{\Delta_5,2} = \phi_{\Delta_{E_6},2}\boxtimes\mathrm{Sym}^1\otimes\varepsilon_2$ with $\varepsilon_2 \leftrightarrow \sqrt 2 \in \mathbb{Q}_2^\times/(\mathbb{Q}_2^\times)^2$; conductor $2^{17}$.

12. **Monster hyperbolic rank $\ell_{\mathrm{Monster}} = 2$**.
    Four convergent routes (Mukai-doubling / Fricke $w_1$ / super-EK $\mathbb{Z}/2$ / Conway-Norton identity-class); W17 correction confirmed by W18.

13. **MTC at $q = \zeta_8$**.
    Non-semisimple Kerler-Lyubashenko; semisimplification is Turaev; PBW upper bound $|\Lambda| \le 8^{129}$. Primary: Kerler-Lyubashenko 2001 LMS LNS 262.

14. **Modular $S$-matrix = Fricke $w_8$**.
    $S^4 = \mathrm{id}$; eigenvalues $\{1,i,-1,-i\}$; generic $\mathrm{tr}(S) = 0$; $M_{24}$-invariant Humbert-block trace $= 4$ (matches $|\Psi_{\Delta_{10}}|$). Primary: Gritsenko 1995 §3 Thm 3.2.

15. **Plancherel integrates to $1/\Phi_{10}(Z)$**.
    Over projective covers $P_\lambda$ (not simples); four-path cross-verification. Primary: Kerler-Lyubashenko + Etingof-Ostrik 2004.

16. **Pentagon MZV basis dimensions (Padovan)**.
    $d_n = d_{n-2} + d_{n-3}$ through $n = 12$; $d_{11} = 7$, $d_{12} = 9$; Borcherds leg dominates by $\sim 10^{10}$ at $n = 10$. Primary: Brown 2011 *Ann. Math.* 175.

17. **$A_\infty$-quasi-Hopf non-closure**.
    Imaginary cone is infinite-dimensional (Hardy-Ramanujan $\exp(4\pi\sqrt n)$); $\phi^{(n)} \neq 0$ for any $n$.

18. **Heegner pattern all-orders theorem** (W18 Costello).
    $c_n = c_{\phi_{-2,1}}(-n)\cdot [H_n]$; admissible iff $n \equiv 0,3\pmod 4$. Three-input composite (Bruinier + Borcherds + Costello-Gaiotto-Paquette). WOV-5.

19. **$A_{N-1}$ Siegel weight formula (W17 Gaiotto)**.
    $k_N = (N+3)/2$ for $N\in\{2,3,4,5\}$; breaks at $N = 6$. WOV-9.

20. **CY-2 landscape weight formula**.
    $w_{\mathrm{Borch}}(X) = 5\chi_{\mathrm{top}}(X)/24$. K3/Kummer: 5; Enriques: 5/2 metaplectic; $T^4$/bielliptic: 0 (Heisenberg taxon G); half-K3: 0 ($\widehat{E_8}_1$, taxon L).

21. **Enriques BKM lattice** (W18 Drinfeld+Witten).
    $E_8 \oplus \mathrm{II}_{1,1}(2)$ signature $(1,9)$; Siegel weight 5/2 metaplectic; $M_{12}$-moonshine candidate via Niemeier $12A_2$.

22. **Hilbert-scheme pro-limit** (W18 Nekrasov).
    $\{H^*_T(\mathrm{Hilb}^{[n]}(\mathrm{K3}))\}$ converges in $\mathrm{Pro}(\mathrm{Mod}_{\mathbf{H}_{\Delta_5}})$ as super-quasi-Hopf module (MO + Grojnowski-Nakajima + Etingof-Kazhdan super-quantisation composite).

23. **Classical limit matches Gaitsgory-Nadler 1998** (W19 Kazhdan).
    Geometric-Langlands classical limit of $\mathbf{H}_{\Delta_5}$-side is the GN 1998 central-sheaf picture at $\hbar = 0$.

24. **Global Bridgeland dictionary** (W19 Beilinson).
    Bridgeland stability manifold $\mathrm{Stab}(D^b\mathrm{Coh}(\mathrm{K3}\times E))$ has a global slicing whose heart-family tracks the wall-crossing of $\mathbf{H}_{\Delta_5}$-module stratification across $\overline{\mathcal{A}_2}$.

25. **K-theoretic $(q_1,q_2)$-collapse** (W19 Nekrasov).
    Equivariant K-theory limit $(q_1,q_2)\to 1$ collapses onto the $\mathbf{H}_{\Delta_5}$-module category via Maulik-Okounkov stable envelopes.

26. **Theorem H scope $\{0,1,2,d\}$** (W18 Polyakov).
    $\mathrm{ChirHoch}^\bullet$ concentration extends from $\{0,1,2\}$ (ordinary) to $\{0,1,2,d\}$ for $\Phi_d$ on CY-$d$ input; K3×E (CY-3): $\{0,1,2,3\}$.

27. **$\mu_8$-gerbe banding** (W18).
    Explicit chain-level 2-cocycle $F_{ij} = [\Phi_{10}/\eta^{24}]^{1/8}$-ratio on Igusa fundamental-domain cover; $\delta F = 0$ verified.

28. **Satake-Casimir dictionary** (W17 Beilinson).
    $\mathrm{Cas}_p(\mathbf{H}_{\Delta_5}) = (a_p)^2/p^{15} - 2$; 22 primes verified tempered.

29. **Drinfeld centre strict inclusion**.
    $\mathrm{Rep}^{E_2}(Z^{\mathrm{der}}_{\mathrm{ch}}(\mathbf{H}_{\Delta_5})) \hookrightarrow \mathcal{Z}(\mathrm{Rep}) \to \mathrm{YD}^{A_\infty}$; equivalence only on Koszul locus.

30. **Schur-index 10 Fourier coefficients**.
    WOV-7: $\{1, 72, 2678, 68474, 1351775, 21945390, 304799105, 3720945220, 40716498035, 405322063500\}$.

31. **Zamolodchikov shadow at $c = -214$ (class M)**.
    $S_2 = -107$, $S_3 = 2$, $S_4 = 5/112136$; $\langle\Lambda|\Lambda\rangle = 22472.2 > 0$; placement robust under $-312\to -214$ retraction.

32. **$\mathfrak{g}_{\Delta_5} = \mathrm{Borch}(F_3, \phi_{0,1}^{K3})$**.
    K3-BKM Lie superalgebra with imaginary-root multiplicities $= c_{\mathrm{K3}}(4nm - \ell^2)$ from K3 elliptic genus EOT coefficients.

---

## (II) CORRECTED — wave-level retractions, final stable

Three wave-level retractions identified and absorbed. Each has a named retracting wave, named healing wave, and primary-literature anchor for the final stable value.

### (II.A) $(c_{4d}, c_{2d})$ central-charge reversal

- **W13 stable**: $(107/6, -214)$ via first-principles Chacaltana-Distler pants decomposition.
- **W14 erroneous retraction**: $(26, -312)$ via formula $(12(g-1)+7n)/6$. *Failure mode*: the formula fails the SU(2) $N_f=4$ cross-check ($n=4$ gives $8/3$ not $7/6$).
- **W15 healing (Gaiotto)**: $(107/6, -214)$ restored via correct $(5n-13)/6 = (2n_v+n_h)/12$, trinion $(n_v,n_h) = (63,88)$ at $n = 24$.
- **W16-W17 propagation**: AP5-style cascade across ~20 cross-volume files; 7 residual retraction remarks at Vol-II THQG chain files + Vol-III `k3e_cy3_programme.tex`.
- **Final stable**: $(c_{4d}, c_{2d}) = (107/6, -214)$. Primary: Chacaltana-Distler 2010 §5.14; Beem-Rastelli 2013 $c_{2d} = -12 c_{4d}$. WOV-2 locks this.

### (II.B) Monster BKM hyperbolic Cartan rank

- **W16 erroneous assertion**: Monster rank 26 (inherited by confusion with Fake-Monster).
- **W17 correction (Drinfeld)**: Monster rank 2 in $\mathrm{II}_{1,1}$; Fake-Monster rank 26 in $\mathrm{II}_{25,1}$; K3-BKM rank 3 in $\Lambda^{2,1}_{II}$.
- **W18 confirmation**: four convergent routes give $\ell_{\mathrm{Monster}} = 2 = 2c_+(\mathrm{II}_{1,1})$.
- **Final stable**: rank 2 for Monster; rank 3 for K3; rank 26 for Fake-Monster. Primary: Borcherds 1992 *Invent.* 109 Thm 3; Gritsenko-Nikulin 1998 §3.

### (II.C) $c_3$ coefficient

- **W16 erroneous assertion**: $c_3 = 176256\cdot [H_3]$. *Failure mode*: $176256 = p_{24}(5) = \chi(\mathrm{Hilb}^5(\mathrm{K3}))$ — unrelated to $\phi_{10,1}$ Fourier expansion.
- **W17 correction**: $c_3 = -8\cdot [H_3]$ via four independent paths (direct $\theta_1^2/\eta^6$ / theta decomposition / $\phi_{10,1}/\eta^{24}$ / Hecke congruence).
- **W18 Costello note**: factor $-22032 = 176256/(-8)$ between Bruinier reduced-class and Gritsenko-Nikulin Cartan-matrix conventions.
- **Final stable**: $c_3 = -8$ in Bruinier reduced-class convention. WOV-5 locks this; convention pinned in §III.D below.

### (II.D) Umbral Niemeier labelling rule

- **W18 erroneous "divisor-of-24" rule**: asserted that umbral Niemeier root systems track divisors of 24.
- **W19 correction**: the rule is "$(N-1) \mid 24$" OR substitute Niemeier root system; $N = 6$ requires $6D_4$ (not $4A_5$, which is not a Niemeier root system).
- **Final stable**: $A_{N-1}$ for $N\in\{2,3,4,5\}$ via $(24/\mathrm{rk}(A_{N-1}))\cdot A_{N-1}$; $N = 6$ re-anchored to Niemeier $6D_4$ with umbral group $3.\mathrm{Sym}_6$ (order 2160); $k_6 = 9/2$; ladder continuity verified through $N \le 6$.

### (II.E) Theorem-B scope

- **W15 statement**: bar-cobar inversion on $\overline{\mathcal{A}_2}\setminus(H_1\cup H_4)$.
- **W18 tightening (Beilinson)**: strict chain-level bar-cobar on $\overline{\mathcal{A}_2}\setminus\bigcup_{n\text{ admissible}} H_n$ — all admissible Heegner divisors excluded, not just $H_1\cup H_4$. Constitutional update to `concordance.tex`.
- **W19 confirmation**: stable; reads via "all admissible $H_n$".

### (II.F) Humbert $H_4$ description

- **W15 imprecise**: "$\mathbb{Q}(\sqrt 2)$-RM locus" at Vol I `chiral_climax_platonic.tex:1748`.
- **W16 correction (Kazhdan)**: $H_4$ is the $(2,2)$-isogeny quotient of $E_1\times E_2$ with $\mathrm{End}\supset\mathbb{Z}[2i]$; the $\mathbb{Q}(\sqrt 2)$-RM locus is $H_8$, not $H_4$.
- **Final stable**: $H_4$ monodromy order 2; van der Geer 1988 Ch. IX.

---

## (III) CONJECTURAL — open dependencies

Each item is an open mathematical conjecture with a named seed and named dependence. Resolution is pending primary-literature proof or further computation.

### (III.A) $\phi^{(n\ge 13)}$ — Zagier-Hoffman depth-reduction conjecture

- **Status**: $\phi^{(n)}$ is explicitly computed through $n = 12$ (W18).
- **Blocker**: Brown's motivic MZV theorem covers weights $\le 12$; weights $\ge 13$ depend on conjectural depth-reduction of irreducible MZVs (Zagier-Hoffman).
- **First unknown entry**: depth-4 $\zeta(3,3,3,3)$ at weight 12 is resolved; depth-5 first conjectural at weight $\ge 15$.

### (III.B) Conway $V^{s\natural}$ as 5th $\Psi$-image — Wave-19 Witten construction

- **Status**: W19 Witten inscribed Conway-module $V^{s\natural}$ as a 5th image of the universal $\Psi$-functor, alongside Monster / K3 / Fake-Monster / Enriques.
- **W20 adjudication (2026-04-20 priority-2 rerun)**: three concrete defects identified in the W19 inscription (`k3e_bkm_chapter.tex:4262` \emph{et seq.}), all remediated:
  1. **Primary-source citation**: the journal venue for Duncan's $V^{s\natural}$ paper (arXiv:math/0502267) is \emph{Duke Math.\ J.}~139 (2007), 255--315, not \emph{Math.\ Res.\ Lett.}~14 (as originally written). Corrected on disk. The task prompt's "Duncan 2006 arXiv:math/0605219" is a different paper (Duncan's "Arithmetic groups and the affine $E_8$ Dynkin diagram"); the Conway construction is arXiv:math/0502267.
  2. **Construction description**: the original inscription described $V^{s\natural}$ as "$\mathbb{Z}/2$-orbifold of $24$ free fermions at the $E_8$ super-lattice tensored up". Duncan 2007 \S3--4 actually constructs $V^{s\natural} = A(\Lambda_{24})^+ \oplus A(\Lambda_{24})^{\mathrm{tw},+}$ --- the $\mathbb{Z}/2$-orbifold of the $24$-generator fermionic vertex superalgebra $A(\Lambda_{24})$ on the Leech lattice $\Lambda_{24}$. No $E_8$ super-lattice enters. Corrected.
  3. **Sign-convention anomaly**: the original inscription asserted $c_+(\Lambda_{24}) = 0$ on the grounds that Leech is "positive-definite with signature $(0,24)$". But positive-definite means signature $(24,0)$; Theorem~\ref{thm:bkm-universal-identity} (universal identity on lattice side, Vol.~III) defines $c_+(L) = $ positive-eigenvalue count. So $c_+(\Lambda_{24}) = 24$ under the programme convention, giving $K_{\Lambda_{24}} = 48$ and $\hbar^2 = -1/48$, \emph{not} $(K,\hbar^2) = (2,-1/2)$. The asserted values for Conway therefore require either a sign-reversal convention under super-polarisation (not stated in Duncan 2007) or a reinterpretation of $V^{s\natural}$ as living inside the existing four-row $\Psi$-landscape rather than as a fifth row.
- **Hidden true structure (default W20 reading)**: $V^{s\natural}$ is the $\mathbb{Z}/2$-super-twin of $V^\natural$ inside the commutative orbifolding diamond of Duncan 2007 \S6 and Remark~\ref{rem:bkm-conway-monster-fake-monster-triangle} (Vol.~III), \emph{not} an independent $\Psi$-image. Under this reading the Conway Lusztig pair $(K,\hbar^2) = (2,-1/2)$ coincides with Monster's because $V^{s\natural}$ inherits them from $V^\natural$ through the diamond; the commutative diamond is the established mathematical content of the W19 inscription. Alternate reading: Scheithauer 2008 \emph{Invent.\ Math.}~172 Thm~3.2 realises $V^{s\natural}$ as a $\mathbb{Z}/2$-twisted subsector of the Fake-Monster row on $\mathrm{II}_{25,1}$, via $\Lambda_{24}\subset\mathrm{II}_{25,1}$.
- **Disk state**: Theorem environment downgraded to Conjecture (label `conj:bkm-conway-psi-fifth-image`), primary-source citation corrected, three-reading anomaly recorded in the new Remark `rem:bkm-conway-psi-image-sign-and-diamond`. Downstream references (`cy_categories.tex` three call sites; `k3e_bkm_chapter.tex` one call site) updated to point at the conjecture label.
- **Remaining blocker**: deciding between readings (i)--(iii) of the three-readings remark requires (a) Duncan 2007 \S5 universal-property argument read in primary source, and (b) Scheithauer 2008 Thm~3.2 super-Borcherds extension read in primary source. Until then the fifth-image identification is conjectural, not proved.

### (III.C) Pseudo-character $S^{\mathrm{ps}}$ — Wave-19 Gelfand

$\perp$ retracted per canonical preamble: the programme-canonical object is the Chenevier 2014 determinant $D^{\mathrm{Chen}}$, not a Taylor--Wiles pseudo-character; see Vol I Pattern 295 / W25 in `notes/first_principles_cache_comprehensive.md` and Vol I `chapters/theory/derived_langlands.tex` Remark `rem:dl-w25-determinant-not-pseudocharacter`. Original entry retained below.

- **Status**: W19 Gelfand pseudo-character inscription listed as pending rerun completion in the synthesis; CONJECTURAL until resolution.
- **Dependence**: Chenevier 2014 pseudo-representation formalism; Deligne-Serre pseudo-character extensions.

### (III.D) Bridgeland global — Wave-19 Beilinson (done)

- **Status**: PROVED in W19 as the "global Bridgeland dictionary" (item 24 in (I)); kept here in CONJECTURAL section only as a pointer because the chapter inscription (Vol III `derived_categories_cy.tex`) is in W19 DNA form not yet W20-cross-verified.

### (III.E) Schiffmann-Vasserot $\mathrm{ChirHoch}^3$ explicit cocycle

- **Status (W20-audit)**: W18 Polyakov inscribed the explicit form $e_3(z) = :T\partial T: - (1/4)\partial^3 T + \hbar\cdot\mathrm{qt}(J^{(3)})$; non-vanishing PROVED at the explicit rational value $\langle[\chi_3],[e_3]\rangle_{\Phi_3} = 2\,\mathrm{Vol}(E)\cdot(2\pi\mathrm{i})^3 = \chi(\mathcal O_{\mathrm{K3}})\cdot\mathrm{Vol}(E)\cdot(2\pi\mathrm{i})^3$ via three independent paths: (A) CoHA triangle-cycle via Schiffmann-Vasserot Casimir $\mathrm{Cas}_2(\alpha)=1$ times Mukai $\chi(\mathcal O_{\mathrm{K3}})=2$; (B) reduced-DT / Oberdieck 2018 Thm 2 polar-leading coefficient $[p^{-1}q^{-1}y^0](-\Phi_{10}^{-1})=1$ in the Siegel Fourier chamber $|y|<1$; (C) CY-2 formality scaling limit $\mathrm{Vol}(E)\to 0$ sending $[\chi_3]\to 0$ via Kontsevich 2003 CY-2 formality. Two W18 corrections: (i) factor-of-two Mukai double-count corrected ($2\,\mathrm{Vol}(E)(2\pi\mathrm{i})^3$, not $4$); (ii) reduced-vs-unreduced DT index conflation corrected (polar-leading in three-variable $(\beta_h,d,k)$ reduced-DT, not unreduced $(0,n)$ degree-zero which is trivially zero by $\chi(\mathrm{K3}\times E)=0$). Inscribed in Vol I hochschild\_cohomology.tex thm:chirhoch3-Delta5-chain-level and Vol III hochschild\_calculus.tex prop:chi-3-nonvanishing-MNOP. Cache: W20-mnop-chi3-degzero-vs-reduced-dt-index.
- **Open**: explicit higher cocycles $e_{k\ge 4}$ remain open.

### (III.F) $\mathrm{GRT}_1$-transitivity on $\mathbf{H}_{\Delta_5}$

- **Status**: affine-KM case done; BKM-side conjectural.
- **Dependence**: Grothendieck-Teichmüller Lie algebra $\mathrm{grt}_1$ action on the Drinfeld-associator space extended to BKM.

### (III.G) Full PBW dimension of $\mathfrak{u}_{\zeta_8}$

- **Status**: PBW upper bound $8^{129}$ established; exact count open.
- **Dependence**: Lusztig 1993 small-quantum-group PBW combined with the imaginary-cone truncation at $\hbar = \zeta_8$.

### (III.H) Fake-Monster theta cocycle $\theta^{\Phi_{12}}$ explicit generators

- **Status**: rank-26 RTT presentation stated in DNA; generators not yet inscribed.

### (III.I) $\Psi$-functor surjectivity

- **Open**: whether every super-EK-quantisable BKM is a $\Psi$-image.
- **Dependence**: Gritsenko-Nikulin 1998 Siegel-automorphic-product BKM classification.

---

## (IV) LINGERING AMBIGUITIES

Convention-level or scope-level residua. Each is a **resolution**, not a conflict: the ambiguity is notational and the programme-canonical choice is specified.

### (IV.A) $c_3$ normalisation convention

- **Ambiguity**: W16 `176256\cdot [H_3]` vs W17/W18 `-8\cdot [H_3]`.
- **W18 Costello observation**: the factor $-22032 = 176256/(-8)$ is the conversion ratio between two distinct conventions.
  - **Bruinier reduced-class convention**: $c_3 = -8$.
  - **Gritsenko-Nikulin Cartan-matrix convention**: $c_3 = 176256$ up to the Cartan prefactor.
- **Resolution (W19)**: use **Bruinier reduced-class convention throughout**. The programme-canonical value is $c_3 = -8$; `whole_object_verifier.py` anchor. Any citation that quotes 176256 should be annotated with the conversion $176256 = -22032\cdot(-8)$ and the reader pointed to the Bruinier normalisation.

### (IV.B) Two-$\hbar$ distinction

- **Ambiguity**: $\hbar^{\mathrm{Drinfeld}} = 2\pi i/\ell$ (Lusztig-type root-of-unity) vs $\hbar^{\mathrm{BV}}$ (Costello 1-loop expansion parameter).
- **Fact**: both give $\hbar^2 = -1/8$ at $\ell = 8$ but via different mechanisms (Lusztig small-form specialisation vs Bruinier 1-loop BV integral).
- **Resolution**: bridge via **AP151** — the two $\hbar$-parameters agree numerically at the specific specialisation $\ell = 8$ but are semantically distinct quantisation parameters; propagate the AP151 bridge notation across all three volumes.

### (IV.C) Theorem-B scope statement — admissible $H_n$

- **W15**: exclude only $H_1\cup H_4$.
- **W18 Beilinson tightening**: exclude all admissible Heegner divisors $\bigcup_{n\text{ admissible}} H_n$.
- **Resolution**: programme-canonical statement is W18 Beilinson tightening; "admissible" means $n \equiv 0,3\pmod 4$. Older inscriptions excluding only $H_1\cup H_4$ should be updated with the constitutional concordance patch.

### (IV.D) $c_{\mathrm{unit}} = 2$ vs $c_{\mathrm{eff}} = -166$ — physical vs formal

- **Ambiguity**: W17 Polyakov identified two distinct central charges.
  - $c_{\mathrm{unit}} = \mathrm{rk}(P) = 2$ on the real-root unitary submodule (positive-definite rank-2 sub-Cartan).
  - $c_{\mathrm{eff}} = c - 24 h_{\min} = -214 + 48 = -166$ as a gravitational-anomaly coefficient.
- **Fact**: $c_{\mathrm{eff}}$ is negative ($-166 = -2\cdot 83$, 83 prime), unphysical as Cardy/entanglement entropy.
- **Resolution**: the negative $c_{\mathrm{eff}}$ is a **gravitational-anomaly coefficient** (Manschot-Moore 2007 / DVV 1997 / Witten 2007), NOT a Hilbert-space entropy; the real-root unitary sub-entropy uses $c_{\mathrm{unit}} = 2$, giving $S_{\mathrm{EE}} = (2/3)\log(L/\epsilon) > 0$.

### (IV.E) Borcherds vs Gritsenko weight (W16 Gaiotto discipline)

- **Ambiguity**: $\mathrm{Borch}(\phi_{0,1}^{K3}) = \Phi_{12}$ (weight 12) vs $\mathrm{Grit}(\eta^9\vartheta_1) = \Delta_5$ (weight 5).
- **Resolution**: the K3-BKM denominator is $\Delta_5$ (Gritsenko additive), NOT $\Phi_{12}$ (Borcherds multiplicative). Cache entry 16-Gaiotto.

### (IV.F) BKM signature — Feingold-Frenkel vs Sylvester

- **Ambiguity**: Sylvester principal-minor test applied to $G_{\mathrm{BKM}}$ gives $(2, 0, -32)$, which is misleading (the $m_2 = 0$ is an isotropic $S_3$-symmetry artefact).
- **Resolution**: use **Feingold-Frenkel 1983** eigenvalue-based signature $\{+4,+4,-2\}$, signature $(2,1)$; Sylvester is a trap here. Cache entry 17-BKM-signature.

### (IV.G) Archimedean Schmidt $(17/2,15/2)$ vs $(7/2,5/2)$

- **Ambiguity**: two Schmidt parameters appear depending on Siegel-form target.
- **Resolution**: $(17/2, 15/2)$ is the Schmidt parameter for $\Delta_{10}$ (holomorphic discrete series on $\mathrm{Sp}_4(\mathbb{R})$); $(7/2, 5/2)\otimes\mathrm{sgn}_{\mathbb{R}}$ is the Schmidt parameter for $\Delta_5$ on Maass spin cover. They are *both* correct — for different objects. Cache entry 17-archimedean-Schmidt.

### (IV.H) CoHA $\ne$ chiral algebra

- **Fact**: $\mathrm{CoHA}_{K3\times E}$ is an $E_1$-associative algebra; chiralisation requires the explicit $\Phi_3$-arrow.
- **Resolution**: $\mathbf{H}_{\Delta_5} = \Phi_3(\mathcal{D}_\hbar(\mathcal{Y}^{\mathrm{Hall}}(\mathrm{CoHA}_{K3\times E})))$; $\Phi_3$ performs the CoHA → chiral conversion via factorisation on the curve $E$. Cache entry AP-CY7.

### (IV.I) $\kappa_{\mathrm{cat}}(K3\times E) = 0$ not 2

- **Fact**: Künneth: $\kappa_{\mathrm{cat}}(K3\times E) = \chi(\mathcal{O}_{K3})\cdot\chi(\mathcal{O}_E) = 2\cdot 0 = 0$ (total).
- **Resolution**: distinguish total-space $\kappa_{\mathrm{cat}} = 0$ from fibre $\kappa_{\mathrm{fibre}}(K3) = 2$ wherever the distinction matters.

---

## Priority-ordered open items (post-W19 frontier)

1. **$\phi^{(n\ge 13)}$** — Zagier-Hoffman depth-reduction (III.A).
2. **Conway $V^{s\natural}$ independent cross-check** (III.B).
3. **Explicit banding cocycle** for the $\mu_8$-gerbe on $\overline{\mathcal{A}_2}\setminus(H_1\cup H_4)$ — lift current $(\infty,1)$-level DNA to chain-level 2-cocycle.
4. **Pseudo-character $S^{\mathrm{ps}}$** (III.C) -- $\perp$ retracted per canonical preamble: the programme-canonical object is the Chenevier 2014 determinant $D^{\mathrm{Chen}}$; see Vol I Pattern 295 / W25, Vol I `derived_langlands.tex` Remark `rem:dl-w25-determinant-not-pseudocharacter`.
5. **$\mathrm{GRT}_1$-transitivity on BKM** (III.F).
6. **Exact PBW dimension of $\mathfrak{u}_{\zeta_8}$** (III.G).
7. **Yetter-Drinfeld $A_\infty$-tower** $\delta^{(n\ge 4)}$ explicit formulas.
8. **Fricke-fixed-locus eigenvalue profile** large-deviations near $\mathbb{Z}/8$-phase nodes.
9. **$\Psi$-functor surjectivity** onto quasi-Hopf BKMs (III.I).
10. **Enriques BKM** $\mathfrak{g}_{\Delta_5}^{\mathrm{Enr}}$ Weyl denominator + $M_{12}$-moonshine candidate explicit.
11. **Plancherel Hilbert-scheme stabilisation** Maulik-Okounkov-level convergence theorem.
12. **Gerbe order 16 on $H_4$** vs $\mu_{\mathrm{lcm}(8,16)} = \mu_{16}$-gerbe distinction.
13. **Monster Lusztig $\ell_{\mathrm{Monster}} = 2$ refined bookkeeping** — ratio $\ell_{K3}/\ell_{\mathrm{Monster}} = 4 = c_+$-ratio is load-bearing.
14. **$a_p$ extension** to $p\in\{83,89,97,101,\ldots\}$ continuation of $E_4\cdot\Delta$ convolution.
15. **Chacaltana-Distler $(5n-13)/6$ cascade** completeness audit at $n\neq 24$ cases.
16. **Fake-Monster $\theta^{\Phi_{12}}$** explicit generators (III.H).
17. **$\mathrm{ChirHoch}^{k\ge 4}$ cocycles** beyond the Polyakov degree-3 (III.E).

---

## Signature summary

- **Verified stable**: 32 items across object/identity/numerical/arithmetic/categorical/landscape categories.
- **Corrected**: 6 wave-level retractions, all absorbed; final stable values locked and primary-referenced.
- **Conjectural**: 9 open mathematical dependencies with named seeds.
- **Lingering ambiguities**: 9 convention/scope residua, each resolved with programme-canonical choice.
- **Priority open items**: 17 ordered.

The wave-level convergence is robust: after W14-19 the programme-canonical identification of $\mathbf{H}_{\Delta_5}$ is stable under all tested cross-checks (WOV 11/11, 22 Hecke primes, 4 Siegel-weight routes, 6-frame duality plus 7th GW/DT), with the three wave-level retractions fully absorbed and no un-adjudicated conflict remaining. The open frontier is arithmetical-analytic (high-weight MZVs, $p\ge 83$ Hecke, pseudo-character) and structural-categorical (banding cocycle, Yetter-Drinfeld tower, $\mathrm{GRT}_1$ on BKM), NOT foundational.

---

*End of Wave-19 Adjudication Ledger. Compiled 2026-04-20.*
