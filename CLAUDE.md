# CLAUDE.md — Calabi-Yau Quantum Groups

## What This Is

Research monograph by Raeez Lorgat. Volume III of the modular Koszul duality programme. Volumes I (~2,200pp, ~/chiral-bar-cobar) and II (~900pp, ~/chiral-bar-cobar-vol2) built the bar-cobar machine for chiral algebras and its 3D HT QFT interpretation. This volume asks: in what precise sense is a Calabi-Yau category — or a more general category with the appropriate structures generalizing CY geometry — actually a Calabi-Yau quantum chiral algebra?

**Title**: *Calabi-Yau Quantum Groups: Chiral Algebras from Calabi-Yau Categories via E_1/E_2 Factorization*

## The Central Question

A CY category C of dimension d carries a cyclic A-infinity structure: a non-degenerate trace Tr: HH_*(C) -> k[-d] on Hochschild homology. The cyclic bar complex CC_*(C) with its S^d-framing is the primary invariant.

A chiral algebra A carries a bar complex B(A), a factorization coalgebra on Ran(X), with the full modular structure controlled by Theta_A (Vol I).

**The programme**: construct a precise functor Phi: CY_d-Cat -> E_2-ChirAlg that:
1. Takes a CY category (Fukaya, derived, matrix factorization, or more general) as input
2. Extracts the E_2-monoidal structure (braided tensor product, quantum group action)
3. Produces a chiral algebra A_C whose bar complex encodes the CY cyclic homology
4. Realizes the CY trace as the modular characteristic kappa(A_C)

## The E_1/E_2 Chiral Hierarchy

The key structural ingredient, extending the E_1 theory from Vol II:

- **E_1-chiral algebras** (Vol II, Part VII): associative factorization on C x R. Representation categories are monoidal.
- **E_2-chiral algebras** (this work): braided factorization on C x C. Representation categories are braided monoidal — the natural habitat of quantum groups.
- **The E_1 -> E_2 passage** via Dunn additivity: E_2 ~ E_1 tensor E_1.
- **The CY connection**: for d=2, the S^2-framing of HH_*(C) provides an E_2-algebra structure on cyclic homology — the braiding.

The Drinfeld center Z(Rep^{E_1}(A)) ~ Rep^{E_2}(Z^der_ch(A)) provides the categorical incarnation of the bulk-boundary correspondence: E_1 boundary -> E_2 bulk via the center construction.

## Main Theorems (Targets)

- **CY-A** (CY-to-chiral functor): Construction of Phi: CY_d-Cat -> E_2-ChirAlg via E_2-factorization envelope
- **CY-B** (E_2-chiral Koszul duality): Bar-cobar adjunction in the E_2-chiral setting, CY trace as curvature
- **CY-C** (Quantum group realization): Rep^{E_2}(A_C) is braided monoidal equivalent to C itself, when C arises from a quantum group (generalizing Kazhdan-Lusztig)
- **CY-D** (Modular CY characteristic): kappa(A_C) = chi^CY(C), genus-g obstruction recovers GW/Hochschild invariants

## Architecture

**Part I — CY Categories and Cyclic Structures**
- CY categories (smooth, proper, CY condition, trace)
- Cyclic A-infinity structures (cyclic bar complex, S^d-framing)
- Hochschild calculus (HH duality, categorical Hodge theory)

**Part II — E_1 and E_2 Chiral Theories**
- E_1-chiral algebras (review from Vol II)
- E_2-chiral algebras (central innovation: braided factorization)
- E_n-factorization and higher chiral structure

**Part III — The Bridge: CY Categories as Quantum Chiral Algebras**
- CY-to-chiral functor (cyclic -> Lie conformal -> factorization envelope -> E_2 enhancement -> quantization)
- Quantum chiral algebras (R-matrix, quantum YBE, shadow depth)
- The modular trace (CY characteristic, genus expansion, shadow obstruction tower)

**Part IV — Quantum Groups and Braided Monoidal Structure**
- Quantum groups foundations (U_q, R-matrix, YBE)
- Braided factorization (E_2 bar-cobar, braided Koszul duality)
- Drinfeld center and bulk algebras

**Part V — The Standard Landscape**
- Fukaya categories (elliptic, K3, CY 3-folds, wrapped)
- Derived categories of CY manifolds (HMS, exceptional collections, stability)
- Matrix factorizations (LG models, ADE singularities, W-algebras)
- Quantum group representations (Rep_q(g), Kazhdan-Lusztig, Yangian/RTT)

**Part VI — Connections and Frontier**
- Bar-cobar bridge to Volume I
- Modular Koszul duality and CY geometry
- Geometric Langlands and CY quantum groups

## Dependencies on Volumes I and II

| Volume | Provides | Used here |
|--------|----------|-----------|
| I (Modular Koszul Duality) | Bar-cobar machine, Theta_A, kappa(A), five theorems (A-D+H) | CY bar complex, modular trace, shadow obstruction tower |
| II (3D HT QFT) | SC^{ch,top}, PVA descent, DK bridge, E_1 sector | E_1 chiral theory, braided structure, bulk-boundary |

## The Multi-Path Verification Mandate

Inherited from Vol I. **Every computational result must be supported by multiple independent computations that all point to the same result.** Minimum: 3 genuinely independent verification paths per numerical claim. See Vol I CLAUDE.md for the full verification path taxonomy (8 methods). The compute/ layer is the verification engine; every formula needs corresponding multi-method tests. Cross-volume propagation (AP49) is especially critical: Vol III uses motivic/categorical conventions that differ from both Vol I (OPE modes) and Vol II (λ-brackets). NEVER paste a formula between volumes without explicit convention conversion and independent numerical verification.

## The Beilinson Principle

Inherited from Vol I. Every claim is false until independently verified. The six hostile examiners (Beilinson, Witten, Costello, Gaiotto, Drinfeld, Kontsevich) apply. All anti-patterns AP1-AP34 from Vol I carry over.

**Additional CY-specific pitfalls**:
- **AP-CY1**: CY dimension d != complex dimension n. For a CY manifold X of complex dimension n, Fuk(X) is CY of dimension n, D^b(Coh(X)) is CY of dimension n. Do not confuse with real dimension 2n.
- **AP-CY2**: The CY trace is a class in HC^-_d(C), NOT just a map HH_d -> k. The negative cyclic refinement is essential for the S^d-framing.
- **AP-CY3**: E_2 != commutative. E_2-algebras have a braiding but it is NOT symmetric in general. The symmetrization E_2 -> E_infty loses the quantum group structure.
- **AP-CY4**: Drinfeld center != derived center in general. Z(C) (Drinfeld center of a monoidal category) and Z^der_ch(A) (chiral derived center) agree under specific hypotheses. State which center you mean.
- **AP-CY5**: Kazhdan-Lusztig equivalence requires q a root of unity (or specific rationality conditions on k). At generic q, Rep_q(g) is semisimple and the story simplifies; the interesting structure is at roots of unity.

## Anti-Patterns (inherited from Vols I-II + Vol III-specific)

All anti-patterns AP1-AP43 from Vol I CLAUDE.md apply here. The following are the most frequently triggered in this volume:

**AP38 — Literature normalization convention in hardcoded values.** The BKM shadow obstruction tower engine hardcoded phi_{0,1} Fourier coefficients in the DVV convention (f(0,0)=20, f(1,0)=-252) instead of the Eichler-Zagier convention (f(0,0)=10, f(1,0)=108). The BKM identity was documented as FALSE for phi_{0,1}. **Rule: when hardcoding values from the literature, ALWAYS record the source paper and normalization convention.**

**AP42 — Correct at sophisticated level, false at naive level.** "Scattering diagram = shadow obstruction tower" holds at the motivic Hall algebra level, but naive BCH pair-commutator does NOT reproduce phi_{0,1} multiplicities (commit 72ba062). The gap measures higher BPS bound-state contributions. **Rule: state the level of validity explicitly.**

**AP43 — Central object defined by aspiration, not by axioms.** G(X) ("quantum vertex chiral group") used in ~20 locations without formal definition. "Quantum chiral algebra" defined as "equivalent to quantum group representation category" — a prayer, not a definition. **Rule: MUST formally define before use. The central object of a volume MUST have a \\begin{definition}.**

**AP35 — Accidentally correct theorem.** The [d_X, d_Y] = 0 identity was stated for all genera but qualified to genus 0 (commit a0ff317). Check whether genus-extension claims rest on genus-0 proofs. **Rule: verify proof steps independently of the conclusion.**

**AP36 — Biconditional overclaim.** CY-C was stated as "Theorem" but is a conjecture — the CY category C(g,q) is not constructed in general. CY-A was stated for all d but only d=2 is proved. **Rule: before writing "Theorem," verify the proof exists in THIS manuscript.**

**AP40 — LaTeX environment contradicts claim status.** CY-C was in a theorem environment despite being conjectural. Each claim in k3_times_e.tex was relabeled Theorem/Conjecture/Observation (commit a0ff317). **Rule: environment MUST match status.**

**Vol III-specific pitfalls** (from Vol III CLAUDE.md AP-CY1 through AP-CY5):
- **AP-CY1**: CY dimension d ≠ complex dimension n.
- **AP-CY2**: CY trace is HC^-_d(C), NOT just HH_d → k.
- **AP-CY3**: E₂ ≠ commutative. E₂ has braiding, NOT symmetric.
- **AP-CY4**: Drinfeld center ≠ derived center in general.
- **AP-CY5**: Kazhdan-Lusztig requires q root of unity (or specific rationality).

**AP44-AP49 (from the 139-fix three-volume rectification swarm, April 2026):**
- **AP44**: OPE mode ≠ λ-bracket coefficient (divided-power 1/n! factor). T_{(3)}T=c/2 → {T_λ T}=(c/12)λ³.
- **AP45**: Desuspension LOWERS degree: |s⁻¹v| = |v|-1, not |v|+1.
- **AP46**: η(q) = q^{1/24}∏(1-qⁿ). The q^{1/24} is NOT optional.
- **AP47**: MC3 proved on evaluation-generated core. DK-4/5 is downstream, not part of MC3.
- **AP48**: κ depends on the full algebra, not the Virasoro subalgebra. κ=c/2 only for Virasoro. Lattice: κ=rank. General VOAs: compute from bar complex.
- **AP49**: Cross-volume formula paste without convention conversion. Vol I=OPE modes, Vol II=λ-brackets, Vol III=motivic/categorical.

**Additional Vol III-specific pitfalls from the audit:**
- **AP-CY6**: A_X does NOT exist for CY3. The chiral algebra of a Calabi-Yau threefold is the single load-bearing gap. CY-A is proved for d=2; for d=3, A_X is conditional on chain-level S³-framing construction. NEVER write "A_X for CY3" as if it were a defined object.
- **AP-CY7**: CoHA ≠ E₁-chiral algebra. The critical CoHA (Schiffmann-Vasserot, RSYZ) is an associative algebra; calling it "the E₁-sector of G(X)" assumes G(X) exists and has a CoHA inside it. The correct statement: "the CoHA is the target that the E₁-sector of G(X) should match, IF G(X) exists."
- **AP-CY8**: Borcherds denominator identity ≠ bar Euler product. The identification requires the CY-to-chiral functor to exist in the relevant dimension. For K3 × E (d=3), Δ₅ is computed from the lattice, not from a chiral algebra (which doesn't exist yet). The "bar Euler product" interpretation is an OBSERVATION about the product formula, not a theorem derived from the bar complex.

## Agent Anti-Patterns (AAP1-AAP8)

Cross-volume agent workflow anti-patterns from 300-commit archaeology. See Vol I CLAUDE.md for full descriptions. Summary: AAP1 (tool-markup leak), AAP2 (fragmented renames), AAP3 (formula duplication in compute), AAP4 (proof after conjecture), AAP5 (artifact commit noise), AAP6 (status oscillation), AAP7 (intra-file inconsistency), AAP8 (README drift).

## Build

```
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
```

Same engine as Volumes I-II: memoir, EB Garamond, newtxmath, thmtools, microtype.

## LaTeX Rules

- All macros in main.tex preamble — NEVER \newcommand in chapter files (use \providecommand)
- Document class: memoir; fonts: EB Garamond via newtxmath + ebgaramond
- Claim status: \ClaimStatusProvedHere, \ClaimStatusProvedElsewhere, \ClaimStatusConjectured, \ClaimStatusHeuristic, \ClaimStatusOpen
- Label everything: \label{def:}, \label{thm:}, etc. Cross-reference with \ref.
- Do not add packages without checking preamble compatibility
- Do not create new .tex files when content belongs in existing chapter

## Git — HARD RULE

All commits authored by Raeez Lorgat. **Never credit an LLM.** No "co-authored-by", no "generated by", no AI attribution anywhere.
