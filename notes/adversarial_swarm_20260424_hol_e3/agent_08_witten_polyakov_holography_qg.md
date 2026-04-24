# Agent 08: Witten/Polyakov holography-QG adversarial report

Date: 2026-04-24.

Scope: topological holographic and quantum-gravity consequences claimed downstream of the holomorphic `E_3` construction. This note edits no chapter or compute file. The audit tests jumps from hCS/`E_3` to BKM, black-hole entropy, AdS3/CFT2, M-theory, and graviton counting.

## Verification surface

Core anchors:

- `chapters/theory/cy3_chain_level_bridge.tex:7`: the useful CY3 object is not the slogan "6d hCS gives a chiral algebra".
- `chapters/theory/cy3_chain_level_bridge.tex:55`: many-variable Dolbeault-chiral CE model.
- `chapters/theory/cy3_chain_level_bridge.tex:138`: typed bridge `PhiFA_3 -> CoHA_crit -> Y^+ -> D(Y^+) -> W_{1+infty}`.
- `chapters/theory/cy3_chain_level_bridge.tex:337`: open oriented hCS-to-Hall comparison `Theta_{hCS->Hall}^{or}`.
- `chapters/theory/cy3_chain_level_bridge.tex:511`: the `E_3` lift is extra Stage-1 data, not a consequence of BV alone.
- `chapters/theory/cy3_chain_level_bridge.tex:578`: Stage-1 envelope is conditional on the verified Stage-1 locus.
- `chapters/theory/cy_to_chiral.tex:226`: native `PhiFA_d` and specialisation `SpCh`.
- `chapters/theory/cy_to_chiral.tex:289`: Stage-1 three-step assembly with the `d=3` framing and Costello-Li witness imposed.
- `chapters/theory/cy_to_chiral.tex:404`: CFG is a topological analogue/test oracle, not the CY3 Dolbeault object.
- `chapters/theory/cy_to_chiral.tex:722`: K3-fibre/BKM output assumes the CY3 hCS-to-Hall comparison plus specialisation and Borcherds-product identification.
- `chapters/examples/k3e_bkm_chapter.tex:12852`: four distinct `kappa_*` values on `K3 x E`.
- `chapters/examples/k3e_bkm_chapter.tex:12887`: theorem-grade character `-Phi_10^{-1} = -Delta_5^{-2}`.
- `chapters/examples/k3e_bkm_chapter.tex:12938`: six routes to `G(K3 x E)` are six constructions, not six `Phi` applications.
- `chapters/examples/k3e_bkm_chapter.tex:12954`: M-theory parent stratified into theorem, heuristic, metaphor, synthesis, conjecture.
- `chapters/examples/k3e_cy3_programme.tex:1505`: BPS spectrum and black-hole entropy.
- `chapters/examples/k3e_cy3_programme.tex:1656`: Costello-Li twisted holography construction is heuristic.
- `chapters/examples/k3e_cy3_programme.tex:4038`: AdS3/CFT2 throat theorem as currently stated.
- `chapters/examples/k3e_cy3_programme.tex:4061`: graviton finiteness as `HH^2_{E_2}`-vanishing.
- `chapters/examples/cy_d_kappa_stratification.tex:2018`: universal `kappa_BKM(Phi_N) = c_N(0)/2`.

## RED/BLUE/GREEN verdict

RED: the direct implication
`holomorphic E_3 hCS => BKM => black holes => AdS3/CFT2 => M-theory protected algebra => graviton count`
is false. Every arrow after the Stage-1 object needs an additional comparison map.

BLUE: the strongest live collision is the CHL/GC index clash in the AdS3 claim. `k_N = 24/(N+1)-2` is the Jatkar-Sen/CHL law, while the displayed index set `{1,2,3,4,6}` is the Gritsenko-Clery/BKM slice; the two towers agree only at `{1,2,3}` in the local doctrine.

GREEN: the surviving spine is useful if each grade is named: Stage-1 theorem/conditional theorem, hCS-to-Hall open problem, BKM character theorem, black-hole/AdS physics theorem from external string theory, M-theory bialgebra conjecture, graviton finiteness conditional on an explicit `E_2` Hochschild computation and physical comparison functor.

## ATTACK->HEAL cycles

### Cycle 1: hCS/`E_3` to BKM

ATTACK. Declare that the holomorphic `E_3` Stage-1 construction already produces the BKM algebra `g_{Delta_5}`.

FAILURE. Stage 1 lands in `EdHolFA(X)`. The bridge to Hall is explicitly dashed, and `Theta_{hCS->Hall}^{or}` is open. The BKM endpoint also requires the fixed Stage-2 specialisation `SpCh_{K3,E}` and the Borcherds denominator identification.

HEAL. The theorem-grade statement is only:
`PhiFA_3(C)_F` exists on the verified Stage-1 locus. The conditional BKM statement is:
if `Theta_{hCS->Hall}^{or}` exists in `FactCosh_Hall^{or,wedge}(X)`, if `SpCh_{K3,E}` is fixed, and if the resulting Hall denominator is identified with the Gritsenko-Nikulin Borcherds product, then the `E_1` specialisation has BKM comparison target `U^ch(g_{Delta_5})`.

Required maps: `Theta_{hCS->Hall}^{or}`, `SpCh_{K3,E}`, Hall denominator character to `Delta_5`.

### Cycle 2: BKM to black-hole entropy

ATTACK. Use `kappa_BKM(Delta_5)=5` to claim black-hole entropy follows from the `E_3` construction.

FAILURE. Entropy uses the physical dyon partition function `1/Phi_10`, not the chiral-half denominator alone. At `N=1`, `Phi_10 = Delta_5^2`; the square is a separate physical dyonic pairing. The Rademacher/Cardy asymptotics depend on charge lattice, contour, discriminant convention, and the DVV/Sen theorem, none of which is supplied by the hCS `E_3` envelope.

HEAL. The surviving theorem is character-level:
`Z_DT^red(K3 x E) = -Phi_10^{-1} = -Delta_5^{-2}` by Oberdieck-Pandharipande plus Gritsenko-Nikulin. The entropy theorem is external string-theoretic/microscopic counting. The `E_3` bridge can only compare to it after a character map from the specialised Hall/CoHA object to the DT partition function is constructed.

Required maps: `ch(CoHA(K3 x E)) -> Z_DT^red`, square-root map `Delta_5 -> Phi_10`, and a charge-lattice/contour normalisation for the Rademacher expansion.

### Cycle 3: `E_3` to AdS3/CFT2

ATTACK. Treat Costello-Paquette/Costello-Li twisted holography on `AdS3 x S3 x K3` as a theorem-level route from `PhiFA_3` to the boundary CFT.

FAILURE. The six-route passage records Costello-Paquette twisted holography as one candidate construction among six. The `k3e_cy3_programme` boundary algebra construction is marked heuristic. It gives a free-boson boundary object with `c=24`; this cannot be used as `kappa_ch(K3 x E)`, `kappa_BKM`, or the BKM algebra without comparison maps.

HEAL. Keep the AdS3/CFT2 throat and dyon degeneracy as a physics theorem from DVV/Sen/Shih-Strominger-Yin/Brown-Henneaux, independent of `PhiFA_3`. A bridge to Vol III requires a boundary-VOA equivalence
`A_E^{HT/IIB} -> SpCh_{K3,E}(PhiFA_3(Perf(K3 x E)))`
as `E_1`-chiral algebras, plus equality of vacuum/DT/dyon characters.

Required maps: HT/IIB boundary algebra to `SpCh`, OPE level matrix to Mukai-lattice vertex operators, and Brown-Henneaux/DVV character comparison.

### Cycle 4: CHL/GC tower collision

ATTACK. Read the AdS3 theorem at `k3e_cy3_programme.tex:4038` literally for `N in {1,2,3,4,6}` with `k_N = 24/(N+1)-2` and tuple `(10,6,4,3,2)`.

FAILURE. The formula `24/(N+1)-2` gives the Jatkar-Sen/CHL tower, whose local doctrine is `N in {1,2,3,5,7,11}` with weights `(10,6,4,2,1,0)`. The BKM/Gritsenko-Clery slice is `N in {1,2,3,4,6}` with `kappa_BKM = c_N(0)/2`. At `N=4,6`, the displayed CHL formula gives non-integral values, not `(3,2)`. This is a tower conflation.

HEAL. Split the statement:

- CHL/AdS/dyon theorem: use `N in {1,2,3,5,7,11}` and `wt(Phi_N^JS)=24/(N+1)-2`.
- BKM/GC theorem: use `N in {1,2,3,4,6}` or the 8-form extension, with `kappa_BKM(Phi_N)=c_N(0)/2`.
- Intersection: `{1,2,3}` only. The `N=1` square `Phi_10=Delta_5^2` does not generalise to `N=2,3`.

Required maps: explicit tower selector `JS` vs `GC`, and separate symbols for `Phi_N^JS` and `Phi_N^GC`.

### Cycle 5: M-theory parent

ATTACK. Promote "M-theory on `R_t x (K3 x E) x R^4` produces the K3 super-Yangian" to a theorem because the character shadow is theorem-grade.

FAILURE. The manuscript already stratifies this: character-level theorem, 5D `N=2` reduction heuristic, M5 `(0,4)` sigma-model metaphor, synthesis-grade glue, and full bialgebra conjecture. The weakest link is heuristic/metaphor, so the full protected-operator algebra is not theorem-grade.

HEAL. Preserve only:
`Z_top,B(K3 x E) = -Phi_10^{-1} = -Delta_5^{-2}`
as theorem-grade character data. The full statement
`A^{M,Omega}_{prot}(K3 x E) ~= Y_hbar^super(g_{Delta_5}) = D(CoHA(K3 x E))`
is conjectural until the protected-sector QFT, Omega-deformation functor, and quasi-Hopf comparison are constructed.

Required maps: protected M-theory local operators to `D(CoHA)`, 5D SCFT construction, M5 worldvolume theory, and quasi-Hopf coproduct/R-matrix compatibility.

### Cycle 6: Graviton counting

ATTACK. Use the holomorphic `E_3` construction to prove that the near-horizon single-graviton algebra is finite at fixed mass level.

FAILURE. The graviton statement is formulated as `HH^2_{E_2}(A_K3,A_K3)=0`, which lives on the boundary K3 chiral algebra / derived-center lane, not directly on the CY3 Stage-1 `E_3` object. At `d>=3`, the native output is `E_1`; the `E_2` structure lives on the derived chiral centre of `Rep^{E_1}(A)`, not on `A` itself. No explicit `HH^2_{E_2}` calculation was found in the requested anchors.

HEAL. Make it conditional:
if a boundary algebra `A_K3` is constructed, if its `E_2` Hochschild bicomplex is computed and gives `HH^2_{E_2}=0`, and if a physical single-graviton-to-Hochschild comparison functor is built, then graviton finiteness follows. Without those inputs, it is a proposed dictionary entry, not a consequence of `PhiFA_3`.

Required maps: bulk single-particle/graviton BRST complex to `HH^2_{E_2}`, boundary algebra construction, and derived-centre placement.

### Cycle 7: Large-N holography as Koszul duality

ATTACK. Treat the brane/gravitational algebra Koszul duality statement as a theorem because Loday-Quillen-Tsygan identifies closed strings with cyclic homology.

FAILURE. LQT is theorem-grade for `H_*^{CE}(gl_infty(A)) ~= wedge HC_*(A)`. It does not prove the large-`N` equivalence between the brane algebra and the BCOV/Kodaira-Spencer gravitational algebra on `K3 x E`; that is stated as a conjecture in the local example.

HEAL. The theorem is the closed-string/chiral-centre algebraic shadow. The holography claim remains conjectural until the large-`N` limit, Koszul dual of the BCOV algebra, and compatibility with `Phi_3^{(Sigma_2,C)}` are constructed.

Required maps: `lim_N A_N -> B^!`, BCOV local operators to chiral derived centre, and compatibility with Stage-2 specialisation.

## Killed claims

1. `E_3 hCS` directly proves `g_{Delta_5}`.
2. `kappa_BKM(Delta_5)=5` directly proves black-hole entropy.
3. Costello-Paquette/Costello-Li holography is a theorem-level `PhiFA_3` route.
4. The AdS3 theorem can use the CHL weight formula on the GC index set `{1,2,3,4,6}`.
5. M-theory protected operators equal the K3 super-Yangian as a theorem.
6. Graviton finiteness follows from Stage-1 `E_3`.
7. LQT alone proves large-`N` brane/gravity Koszul duality.

## Surviving conditional spine

The honest spine is:

```text
PhiFA_3(C)_F
  -- Theta_{hCS->Hall}^{or} (open) -->
CoHA_crit^{or}(X)
  -- SV/KS/local Hall model -->
Y^+
  -- Drinfeld double -->
D(Y^+)
  -- fixed SpCh_{K3,E} + Borcherds/DT character -->
Delta_5, Phi_10, and the K3 x E BKM character package.
```

Character-level statements survive at `K3 x E`: `-Phi_10^{-1}=-Delta_5^{-2}` and `kappa_BKM(Delta_5)=c_1(0)/2=5`. Full algebra, holography, M-theory, and graviton statements survive only after their comparison maps are built.

## Proposed manuscript implications

1. Repair the AdS3/CHL statement by splitting `Phi_N^JS` from `Phi_N^GC`; do not put `N=4,6` under `24/(N+1)-2`.
2. Keep `Theta_{hCS->Hall}^{or}` visibly open wherever BKM, DT, or dyon counting is claimed downstream of hCS.
3. State the Costello-Li/Costello-Paquette holographic route as heuristic or conjectural unless the boundary VOA-to-`SpCh` equivalence is proved.
4. State graviton finiteness as a conditional theorem pending the explicit `HH^2_{E_2}` computation and the single-graviton comparison functor.
5. Preserve the M-theory stratification already present in `k3e_bkm_chapter.tex`; do not let the character theorem upgrade the full protected-operator algebra.

No tests or builds were run; this was a note-only adversarial audit.
