# Agent 02 - Beilinson status audit

Scope: chambered effective BPS positive geometry, with emphasis on constructed vs conditional vs conjectural status, $d=3$ functoriality, unconstructed $G(X)$, CoHA as associative evidence, the theta/positive basis, and compact CY$_3$ Bridgeland gaps.

Files read:

- `CLAUDE.md`
- `AGENTS.md`
- `chapters/theory/quantum_groups_foundations.tex`
- `chapters/examples/coha_wall_crossing_platonic.tex`

No manuscript files were edited. This note is the only file owned by this agent.

## Verdict

The current positive-geometry spine has the right intended hierarchy, but several surrounding sentences still speak as if conditional constructions were already global objects. The main repair is not to lower everything. The sharp hierarchy is:

1. Constructed/proved: $\mathrm{CoHA}(\mathbb C^3)=Y^+(\widehat{\mathfrak{gl}}_1)$ as an associative positive half; standard toric/no-compact-$4$-cycle CoHA positive halves under RSYZ hypotheses; KS/Joyce/Bridgeland wall-crossing in its stated Hall-algebra ambient; conifold cluster wall-crossing before chiralisation; $K3\times E$ reduced primitive DT/Borcherds denominator identities.
2. Conditional: $\mathfrak P^{\mathrm{BPS}}_\sigma(X)$ when Bridgeland stability, orientation data, and an oriented derived critical atlas exist; $G_\sigma(X)=D(Y^+_\sigma(X))$ when PBW integrality and non-degenerate Hall pairing exist; $G^T(X)$ by representability only on MO-accessible equivariant loci; $(\Phi^{\mathrm{FA}}_3)_*$ on MC elements outside $\mathbb C^3$; conifold/global toric $E_1$ chiralisation by chart gluing.
3. Conjectural: global $G(X)$ for arbitrary compact CY$_3$; CY-C at $d=3$; compact CY$_3$ Bridgeland stability and DT/PT wall paths in the required generality; positive theta basis for a general compact CY$_3$ chamber; global Bridgeland-to-$R$ dictionary beyond the explicitly constructed K3 quotient hypotheses.

## Dependency DAG

```text
Bridgeland chamber + orientation data + derived critical atlas
  -> P_BPS_sigma(X)
  -> M_eff_sigma(X), phi_W, Omega_sigma, D_KS, Theta_BPS
  -> Y^+_sigma(X) = H^bullet_eq(M_eff_sigma(X), phi_W)
  -> [Davison-Meinhardt PBW] + [non-degenerate Serre/Hall pairing]
  -> G_sigma(X) = D(Y^+_sigma(X))
  -> [CY-C identification] G_sigma(X) ?= C(D^b Coh(X), q) ?= framed Phi_3 shadow
```

```text
Toric QP / C^3 chart
  -> critical CoHA H(Q,W), associative E_1 algebra
  -> H(C^3)=Y^+(widehat gl_1), standard toric H(Q,W)=Y^+(g_Q) under RSYZ
  -> Hopf pairing
  -> Drinfeld double D(H)
  -> full Yangian / affine super Yangian only where pairing and identification are proved
```

```text
d=3 Phi lane
  -> Phi_3 = Sp^ch_{Sigma_2,C} o PhiFA_3
  -> framed object-level output on stated CY-A_3 locus
  -> explicit chain-level (PhiFA_3)_* on MC elements proved for C^3
  -> toric/no-compact-4-cycle chart gluing conditional
  -> arbitrary CY_3 morphism functoriality not available
```

```text
Compact CY_3 lane
  -> Bridgeland stability/orientation/critical atlas generally open
  -> DT/PT/GW identities theorem in listed loci, conjectural generically
  -> positive basis / theta basis conjectural generically
  -> global G(X) conjectural generically
```

## Five ATTACK/HEAL cycles per scoped status claim

The same five tests were run against every scoped status claim:

- ATTACK 1: Does the claim silently assume a constructed Bridgeland chamber, orientation datum, or critical atlas?
- ATTACK 2: Does it upgrade framed $d=3$ object-level $\Phi_3^{(\Sigma_2,C)}$ to arbitrary CY$_3$ functoriality?
- ATTACK 3: Does it construct global $G(X)$ where only $G^T(X)$ or a conditional double is available?
- ATTACK 4: Does it use CoHA evidence beyond its associative positive-half status, or treat theta bases as constructed?
- ATTACK 5: Does it use compact CY$_3$ Bridgeland/DT/PT/GV facts beyond known loci?

| ID | Claim and anchor | Current status | Five-cycle result | Healed status |
|---|---|---:|---|---|
| C1 | Effective BPS positive geometry, `quantum_groups_foundations.tex:15-78` | definition | A1/H1: definition is valid only after chamber, orientation, and critical atlas are fixed. A2/H2: no $\Phi_3$ functoriality implied. A3/H3: no $G(X)$ constructed. A4/H4: $\Theta^{\mathrm{BPS}}_\sigma$ is theorem-grade only in cluster/toric charts. A5/H5: compact CY$_3$ chambers remain conditional. | Definitional conditional datum. |
| C2 | $G_\sigma(X)=D(Y^+_\sigma(X))$, `quantum_groups_foundations.tex:96-127` | conditional | A1/H1: atlas required. A2/H2: independent of $\Phi_3$ unless CY-C is added. A3/H3: double exists only after PBW plus pairing. A4/H4: CoHA is positive half, not full group. A5/H5: no global compact CY$_3$ conclusion. | Keep `ClaimStatusConditional`. |
| C3 | Toric terminal degeneration, `quantum_groups_foundations.tex:129-170` | proved elsewhere with condition | A1/H1: toric QP supplies atlas. A2/H2: no $d=3$ functoriality needed. A3/H3: gives $Y^+$, not global $G(X)$. A4/H4: valid as CoHA positive half. A5/H5: exotic compact-$4$-cycle cases stay conditional. | Proved on standard toric Hall loci; "terminal" should mean degeneration, not categorical terminal object. |
| C4 | Effective BPS cone and positive basis, `quantum_groups_foundations.tex:172-187` | conjectured | A1/H1: assumes chamber and oriented critical semistable moduli. A2/H2: $\PhiFA_3$ specialisation is conjectural outside constructed charts. A3/H3: no global $G(X)$. A4/H4: theta basis is conjectural for compact CY$_3$. A5/H5: compact support/local finiteness open. | Keep `ClaimStatusConjectured`. |
| C5 | CY-C at $d=3$, `quantum_groups_foundations.tex:502-537` | conjectured | A1/H1: requires CY category data. A2/H2: line 535 correctly restricts to framed object-level assignment. A3/H3: $C(\mathcal C,q)$ not constructed generally. A4/H4: $\mathbb C^3$ positive half is evidence only. A5/H5: compact CY$_3$ not covered. | Keep `ClaimStatusConjectured`; use as controlling status for $G(X)$ claims. |
| C6 | Representability of $G^T(X)$, `quantum_groups_foundations.tex:714-798` | conditional | A1/H1: needs torus-fixed MO/KV data. A2/H2: not a $\Phi_3$ theorem. A3/H3: produces equivariant $G^T(X)$ only on MO-accessible loci. A4/H4: CoHA-site and FRT paths are not global presentations. A5/H5: quintic/generic $K3\times E$ excluded by line 770. | Conditional MO-accessible representability; global $G(X)$ remains conjectural. |
| C7 | CoHA algebra/not coalgebra, `coha_wall_crossing_platonic.tex:209-268` | proved here | A1/H1: no Bridgeland chamber needed. A2/H2: no $\Phi_3$ claim. A3/H3: no $G(X)$ construction. A4/H4: exactly associative positive evidence. A5/H5: local QP scope. | Status upheld. |
| C8 | Chiralisation preserves algebra structure, `coha_wall_crossing_platonic.tex:297-361` | conditional | A1/H1: local QP required. A2/H2: proof line 325 overstates symmetric-monoidal $d=3$ functoriality. A3/H3: embedding into $A_X$ is not global $G(X)$. A4/H4: CoHA embeds as $Y^+$ only on constructed C3/toric loci. A5/H5: compact CY$_3$ not covered. | Conditional; split into proved local positive-half statement plus conditional $\PhiFA_3$ embedding. |
| C9 | KS wall-crossing MC gauge, `coha_wall_crossing_platonic.tex:414-547` | proved here | A1/H1: should explicitly require KS orientation/stability data. A2/H2: no $\Phi_3$ bridge in theorem. A3/H3: no global $G(X)$. A4/H4: Hall Lie algebra, not CoHA differential. A5/H5: "local CY$_3$" should mean KS CY$_3$ category with data. | Proved reformulation under KS/Joyce/Bridgeland hypotheses. |
| C10 | Conifold cluster wall-crossing, `coha_wall_crossing_platonic.tex:739-858` | conditional | A1/H1: conifold chamber data known. A2/H2: chiralisation clause conditional. A3/H3: no global $G(X)$. A4/H4: bar counts are computed evidence, not general theorem. A5/H5: non-compact conifold, not compact CY$_3$. | Split status: cluster/KS part theorem, chiral lift conditional. |
| C11 | CoHA chamber-independence via DM, `coha_wall_crossing_platonic.tex:860-925` | proved here | A1/H1: chamber subalgebras depend on stability. A2/H2: no $\Phi_3$. A3/H3: no $G(X)$. A4/H4: ambient algebra independent; BPS sheaf stratification not literally invariant. A5/H5: toric no-compact-$4$-cycle scope. | Proved as ambient CoHA invariance; not invariance of each BPS sheaf. |
| C12 | MNOP three-segment homotopy, `coha_wall_crossing_platonic.tex:951-1065` | conjectured with theorem loci | A1/H1: compact Bridgeland stability/DT/PT path not generally constructed. A2/H2: $\mathcal F_X=\PhiFA_3(D^bCoh(X))$ assumes CY-A$_3$. A3/H3: no $G(X)$. A4/H4: q-dilog gives Hall side, not theta basis. A5/H5: generic compact CY$_3$ remains conjectural. | Keep conjectural generic; theorem only in listed loci. |
| C13 | $Y^+$ vs full Yangian, `coha_wall_crossing_platonic.tex:1349-1417` | conditional | A1/H1: toric QP. A2/H2: no $\Phi_3$ overclaim. A3/H3: full double only after pairing. A4/H4: correctly distinguishes positive half. A5/H5: not compact generic. | Status upheld; clause (iv) conditional. |
| C14 | Non-toric positive-geometry paragraph, `coha_wall_crossing_platonic.tex:1500-1518` | prose | A1/H1: must inherit construction conditions from definition. A2/H2: no $\Phi_3$ functoriality. A3/H3: double conditional. A4/H4: "BPS positive basis" overstates general theta basis. A5/H5: compact CY$_3$ remains conjectural. | Replace "the BPS positive basis" by "a BPS positive basis where constructed, conjectural otherwise." |
| C15 | $K3\times E$ Hall-Drinfeld remark, `coha_wall_crossing_platonic.tex:1533-1535` | no status | A1/H1: Bridgeland variation on $K3\times E$ not fully constructed. A2/H2: "maps via $\Phi$" needs framed $\Phi_3$ bridge. A3/H3: Hall-Drinfeld double not global $G(X)$. A4/H4: Davison integrality is not SV shuffle extension. A5/H5: compact CY$_3$ gap present. | Add status: conditional/conjectural; theorem-grade only for reduced/abelian or listed loci. |
| C16 | $\Phi(\mathcal H_{K3})=H_{\mathrm{Muk}}$, `coha_wall_crossing_platonic.tex:1578-1603` | proved here | A1/H1: K3 CY$_2$ moduli exists in known setup. A2/H2: not $d=3$. A3/H3: no $G(X)$. A4/H4: CoHA-to-Heisenberg embedding needs precise KV/Negut/Nakajima route. A5/H5: not compact CY$_3$. | Conditional on CY-A$_2$ and cited K3 CoHA construction, unless proof gives explicit embedding. |
| C17 | K3 Bridgeland-to-$R$ dictionary package, `coha_wall_crossing_platonic.tex:1628-2324` | mixed, often proved here | A1/H1: K3 stability is known, but global quotient and period-to-Igusa map hypotheses are special. A2/H2: no $d=3$ global functoriality. A3/H3: $\mathbf H_{\Delta_5}$ is not generic $G(X)$. A4/H4: theta/R-matrix factorisations are conditional outside cited theorem loci. A5/H5: product $K3\times E$ mixed-charge and higher-genus Bridgeland extensions remain open. | Downgrade global dictionary and cross-verification from `ProvedHere` to conditional/conjectural unless every standing hypothesis is restated in the theorem. |
| C18 | Physical attractor/scattering propositions, `coha_wall_crossing_platonic.tex:2349-2484` | missing status | A1/H1: depends on physical BPS attractor data. A2/H2: no $\Phi_3$ bridge proved. A3/H3: no $G(X)$. A4/H4: MC/scattering equivalence theorem-grade only in constructed scattering diagram settings. A5/H5: compact CY$_3$ attractor flow not a manuscript theorem. | Mark heuristic/conditional; conifold example can remain computed. |
| C19 | Stable GV/PT equivalence, `coha_wall_crossing_platonic.tex:2557-2633` | conjectured with theorem loci | A1/H1: PT data exist, BPS sheaf package conditional in full generality. A2/H2: no $\Phi_3$. A3/H3: no $G(X)$. A4/H4: not a CoHA theorem. A5/H5: generic compact CY$_3$ is conjectural. | Keep `ClaimStatusConjectured`; special loci theorem-grade. |
| C20 | Generalized CY$_3$ root data and MO base case, `quantum_groups_foundations.tex:6143-6473` | mostly proved here | A1/H1: BPS spectrum/root datum is not unconditional for all CY$_3$. A2/H2: no $\Phi_3$ functoriality. A3/H3: root datum does not construct $G(X)$. A4/H4: $\mathbb C^3$ CoHA wall is not BKM wall, correctly separated. A5/H5: compact CY$_3$ non-toric $\kappa_{\mathrm{BKM}}$ claim too broad. | Definitions stay; global "unconditional geometric data", "terminal object", and compact non-toric-only statements need downgrades. |

## Overclaim ledger and proposed replacement text

1. `quantum_groups_foundations.tex:718`
   - Overclaim: "its existence is a theorem in presentable $(\infty,1)$-category theory, not a construction."
   - Problem: contradicts the theorem's own `ClaimStatusConditional` at line 744 and the scope remark at lines 793-798.
   - Replacement: "On MO-accessible equivariant loci, a representing object $G^T(X)$ is conditional on the accessibility and limit-preservation hypotheses below; for general compact CY$_3$, global $G(X)$ remains part of Conjecture~CY-C."

2. `quantum_groups_foundations.tex:767`
   - Overclaim: "its limit ... recovers the non-compact quantum vertex chiral group."
   - Problem: pro-corepresentability does not by itself prove convergence to an honest object in the ambient category.
   - Replacement: "The pro-object represents $F_X$ in $\mathrm{Pro}(\mathrm{QChirGrp}_\kk)$; identifying a convergent limit with a non-compact quantum vertex chiral group is an additional completion hypothesis."

3. `quantum_groups_foundations.tex:775-783`
   - Overclaim: "three paths ... converge on the same object"; CoHA-site "extending ... to general $X$"; FRT "extracts ... the positive half of $G(X)$."
   - Problem: paths (B) and (C) are constructed only on MO/KV accessible loci, with extra PBW/pairing input.
   - Replacement: "Three checks agree in the constructed examples. Outside $\mathbb C^3$ and the ADE/Kummer or standard toric loci, the CoHA-site and FRT paths are conditional presentations of the expected object."

4. `quantum_groups_foundations.tex:788`
   - Overclaim: "The representing object $G(X)$ carries a canonical $(-1)$-shifted Poisson structure."
   - Problem: only $G^T(X)$ on an accessible locus exists conditionally; shifted Poisson transfer needs its own hypotheses.
   - Replacement: "When the conditional representing object is realised as a Hopf object in the required derived symplectic setting, the expected Poisson shift is $2-d$, hence $-1$ at $d=3$."

5. `quantum_groups_foundations.tex:6147-6151`
   - Overclaim: "The combinatorics of a CY$_3$ $X$ ... constitute ... $\mathcal R(X)$"; "axioms below are unconditional geometric data."
   - Problem: BPS spectrum, automorphic denominator, and integrality are not unconditional for arbitrary CY$_3$.
   - Replacement: "When the lattice, intersection form, and BPS spectrum of a CY$_3$ are constructed and satisfy the axioms below, they define a generalized root datum $\mathcal R(X)$; the associated quantum vertex chiral group remains the target of CY-C."

6. `quantum_groups_foundations.tex:6285-6290`
   - Overclaim: "catalogue ... has a terminal object."
   - Problem: no categorical terminal morphism property is proved; the statement proves a base degeneration.
   - Replacement: "The trivial-lattice datum attached to $\Perf(\mathbb C^3)$ is the terminal degeneration of the catalogue, not a terminal object unless the relevant morphism category is supplied."

7. `quantum_groups_foundations.tex:6445-6460`
   - Overclaim: "For a compact or quasi-compact toric CY$_3$" and "Non-trivial $\kappa_{\mathrm{BKM}}$ on a compact CY$_3$ arises only..."
   - Problem: compact toric CY$_3$ is essentially absent in the usual smooth Calabi-Yau sense; the universal compact claim is broader than the proof.
   - Replacement: "For quasi-compact toric CY$_3$ with finite affine $\mathbb C^3$ fixed-chart cover, the affine-chart contribution to $\kappa_{\mathrm{BKM}}^{\mathrm{MO}}$ vanishes. The K3$\times E$ value $5$ comes from the Lorentzian Mukai/Borcherds face, not from a toric atlas."

8. `coha_wall_crossing_platonic.tex:66-72`
   - Overclaim: "Wall-crossing automorphisms ... therefore give automorphisms of ... $A_X$."
   - Problem: prior clause says bridge is proved only for $\mathbb C^3$ and conditional outside it.
   - Replacement: "Where the bridge $(\PhiFA_3)_*$ is constructed, wall-crossing automorphisms induce automorphisms of $A_X$; outside $\mathbb C^3$ this remains conditional on CY-A$_3$ and chart gluing."

9. `coha_wall_crossing_platonic.tex:297-318` and `325-360`
   - Overclaim: "$\Phi\colon D^b\mathrm{Coh}(X)\to\mathrm{ChirAlg}$" as if fully functorial at $d=3$; "CoHA embeds" for every local CY$_3$.
   - Problem: $d=3$ output is framed object-level on stated locus; embedding is constructed for $\mathbb C^3$ and conditional toric/no-compact-$4$-cycle charts.
   - Replacement: "Let $A_X^{(\Sigma_2,C)}=\SpCh_{\Sigma_2,C}(\PhiFA_3(D^b\mathrm{Coh}(X)))$ be the framed CY-A$_3$ output where defined. On the constructed $\mathbb C^3$ chart, and conditionally on RSYZ plus chart gluing for toric no-compact-$4$-cycle $X$, the CoHA maps to the positive-half algebra inside $A_X$."

10. `coha_wall_crossing_platonic.tex:717-732`
    - Overclaim: "wall-crossing automorphisms ... induce automorphisms" without repeating the constructed locus.
    - Replacement: "For $X=\mathbb C^3$ this compatibility is realised by an explicit chain-level map. For toric CY$_3$ without compact $4$-cycles it is conditional on RSYZ and local chart gluing; outside this locus it is part of the non-formal chain-level CY-A$_3$ problem."

11. `coha_wall_crossing_platonic.tex:860-925`
    - Overclaim: "BPS sheaves ... invariant under Bridgeland stability variation" and "lifts this to motivic level" read too strongly.
    - Problem: the ambient algebra is chamber-independent; the semistable strata/BPS sheaf presentations vary.
    - Replacement: "The ambient critical CoHA is independent of the chamber. A chamber selects a Harder-Narasimhan filtration and chamber subalgebras; wall-crossing identifies their integrated DT series and associated graded decompositions, not each BPS sheaf as a fixed object."

12. `coha_wall_crossing_platonic.tex:951-1065`
    - Overclaim: "Let $X$ be smooth projective CY$_3$ and let $\mathcal F_X=\PhiFA_3(D^b\Coh(X))$ be canonical"; finite DT/PT path for all compact $X$.
    - Problem: compact CY-A$_3$ stage-one output and Bridgeland path are not generally constructed.
    - Replacement: "Assume the CY-A$_3$ stage-one output and the required DT/PT Bridgeland wall path exist. The three-segment homotopy is theorem-grade in the listed toric/conifold/reduced-primitive $K3\times E$ loci and conjectural for a generic smooth projective CY$_3$."

13. `coha_wall_crossing_platonic.tex:1500-1518`
    - Overclaim: "the BPS positive basis."
    - Replacement: "the BPS positive basis where broken-line or Hall-factorisation constructions exist, and the conjectural BPS positive basis otherwise."

14. `coha_wall_crossing_platonic.tex:1533-1535`
    - Overclaim: entire remark states a theorem-level $K3\times E$ Hall-Drinfeld/R-matrix bridge with no status marker.
    - Replacement: "Conditional/conjectural. The reduced and abelian inputs are theorem-grade in the cited loci; extending the Hall-Drinfeld double to full $K3\times E$ and mapping Bridgeland wall-crossing via framed $\Phi_3$ to $R_{\mathrm{Sieg,dyn}}$ requires the Hall-BKM, pairing, and CY-C hypotheses."

15. `coha_wall_crossing_platonic.tex:1578-1603`
    - Overclaim: `ClaimStatusProvedHere` for $\Phi(\mathcal H_{K3})$ embedding and Drinfeld double recovery.
    - Replacement: "Conditional on CY-A$_2$ and the cited K3 CoHA/Nakajima-Grojnowski-Lehn identifications; the positive-mode embedding is theorem-grade where those inputs are explicitly assembled, while the Drinfeld double recovery requires the stated pairing."

16. `coha_wall_crossing_platonic.tex:1668-1678`
    - Overclaim: "The two walls coincide ... this is the Etingof-Beilinson convergence."
    - Problem: coincidence of Bridgeland Gepner monodromy and chiral $R$ self-duality needs an explicit comparison map.
    - Replacement: "The two loci are expected to correspond under the proposed Bridgeland-to-Siegel comparison; theorem-grade coincidence requires the map and monodromy comparison stated in the global dictionary hypotheses."

17. `coha_wall_crossing_platonic.tex:1729-1807`
    - Overclaim: `ClaimStatusProvedHere` for chamber-specific Hall-Drinfeld double isomorphic to $\mathbf H_{\Delta_5}$.
    - Replacement: "Conditional on the K3 CoHA construction, the chamber Manin-pair package, $H^2(\mathfrak g_{\Delta_5})^{\mathbb Z/2,K(1)}=\mathbb C\cdot\Delta_5$, and the EK quantisation comparison. The chamber-specific CoHA is theorem-grade; the identification with $\mathbf H_{\Delta_5}$ is conditional."

18. `coha_wall_crossing_platonic.tex:1809-1853`
    - Overclaim: `ClaimStatusProvedHere` for KS wall-crossing as $R$-matrix gauge conjugation.
    - Replacement: "Conditional on the functor from KS wall-crossing automorphisms to EK gauge transformations of the chamber Manin pair. In constructed cases the formula is $R'=F R F^{-1}$; globally it is a compatibility conjecture."

19. `coha_wall_crossing_platonic.tex:1855-1885`
    - Overclaim: `ClaimStatusProvedHere` for Bayer-Macri-to-Igusa period map as dynamical parameter.
    - Replacement: "Conditional construction of a period comparison on the stated quotient. Do not claim a global functor on $\Stab^\dagger$ or all of $\overline{\mathcal A_2}$ without the full autoequivalence and Picard-rank-zero cases."

20. `coha_wall_crossing_platonic.tex:1888-1931`
    - Overclaim: "valid on all of $\Stab^\dagger/\Gamma$; equivalently, on all of $\overline{\mathcal A_2}$"; `ClaimStatusProvedHere`.
    - Replacement: "Under the standing K3 quotient, EK, and period-comparison hypotheses, the formula defines the expected Bridgeland-to-$R$ dictionary on the constructed image of $\iota$. Its extension to all $\overline{\mathcal A_2}$ and to the full autoequivalence quotient is conditional."

21. `coha_wall_crossing_platonic.tex:1977-2008`
    - Overclaim: "promotes this ... to a functor on the full quotient."
    - Replacement: "organises the expected degenerations along the proposed quotient; functoriality is conditional on Theorem~\ref{thm:cwc-global-dictionary}'s hypotheses."

22. `coha_wall_crossing_platonic.tex:2044-2213`
    - Overclaim: `ClaimStatusProvedHere` for cross-verification, especially codimension-$22$ mixed-charge sector.
    - Problem: the rank computation is internally unstable. For a K3 with Picard rank $\rho$, $\operatorname{rk}T_{K3}=22-\rho$ in $H^2$, and the extended Mukai transcendental complement has rank $24-(2+\rho)=22-\rho$. At $\rho=1$ this is $21$, not automatically $22$. The text's line 2196 "22-\rho=21 plus extra 2-shift gives 22" is not a standard identity.
    - Replacement: "Cross-verification is conditional. The Humbert/DT paths support the dictionary on the $g=2$ quotient; the mixed-charge codimension must be recomputed with the convention $\operatorname{rk}T_{K3}=22-\rho$ (or a clearly defined extended-Mukai variant) before any `ProvedHere` status."

23. `coha_wall_crossing_platonic.tex:2226-2284`
    - Overclaim: "$\iota$ sends each Bridgeland wall..." and "is an isomorphism onto its image..."
    - Replacement: "The proposed map $\iota$ is expected to identify the listed admissible Humbert walls on the constructed quotient; full wall-by-wall surjectivity and isomorphism onto image require proof."

24. `coha_wall_crossing_platonic.tex:2349-2356`
    - Overclaim: proposition lacks status and states all compatible stability conditions lie in one gauge orbit.
    - Replacement: "Mark as heuristic/conditional. For a fixed charge and a constructed split-attractor flow tree, the corresponding MC representatives are expected to be gauge-equivalent; different charges need not lie in one universal orbit without extra data."

25. `coha_wall_crossing_platonic.tex:2472-2480`
    - Overclaim: theorem lacks status and states pentagon equals Jacobi at degree 3 generally.
    - Replacement: "Proved in the resolved conifold/A2 calculation; expected for scattering diagrams controlled by the specified tropical dgLA. Mark conditional outside the computed case."

26. `coha_wall_crossing_platonic.tex:2557-2633`
    - Status mostly correct: `ClaimStatusConjectured`.
    - Needed sharpening: proof line 2610 should not read as full compact-CY$_3$ theorem unless tied to the listed theorem loci.
    - Replacement: "Integrality and stable GV identification are theorem-grade in the listed toric, conifold, and primitive reduced K3-fibre cases; for a generic compact CY$_3$ the statement remains conjectural."

## Sharp replacement hierarchy

Use these labels in manuscript repairs:

- `Constructed`: $\mathbb C^3$ CoHA positive half; standard toric/no-compact-$4$-cycle positive half under RSYZ; conifold cluster wall-crossing before chiral lift; K3 surface Bridgeland chamber structure in the classical K3 setting; reduced primitive $K3\times E$ denominator identities.
- `Conditional`: $\mathfrak P^{\mathrm{BPS}}_\sigma(X)$ for any non-toric $X$; $G_\sigma(X)=D(Y^+_\sigma(X))$; $G^T(X)$ representability; any FRT/Drinfeld-double identification outside proved pairings; $(\PhiFA_3)_*$ outside $\mathbb C^3$; global K3 Bridgeland-to-$R$ dictionary under the listed EK/period hypotheses.
- `Conjectural`: global $G(X)$ for arbitrary compact CY$_3$; CY-C at $d=3$; compact CY$_3$ theta basis; compact CY$_3$ MNOP-as-homotopy in $\PhiFA_3$; $K3\times E$ full Hall-BKM comparison beyond reduced/abelian loci; higher-genus $\overline{\mathcal A_g}$ Bridgeland extension.

## Minimal manuscript actions proposed

1. Replace the global-existence prose at `quantum_groups_foundations.tex:718` before touching theorem statements.
2. Downgrade or split `coha_wall_crossing_platonic.tex:1729`, `1812`, `1858`, `1890`, and `2074` into theorem-grade K3 inputs plus conditional/global-dictionary hypotheses.
3. Insert status markers on the theorem-like physical section at `coha_wall_crossing_platonic.tex:2349-2484`.
4. Recompute the mixed-charge codimension in `coha_wall_crossing_platonic.tex:2044-2260` before preserving the number $22$.
5. Keep CoHA as associative evidence throughout: $\mathrm{CoHA}=Y^+$ is a positive-half statement; full Yangian/BKM claims require pairing plus Drinfeld double plus identification.

