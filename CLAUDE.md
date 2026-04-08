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

- **E_1-chiral algebras** (Vol II, Part III): associative factorization on C x R. Representation categories are monoidal.
- **E_2-chiral algebras** (this work): braided factorization on C x C. Representation categories are braided monoidal — the natural habitat of quantum groups.
- **The E_1 -> E_2 passage** via Dunn additivity: E_2 ~ E_1 tensor E_1.
- **The CY connection**: for d=2, the S^2-framing of HH_*(C) provides an E_2-algebra structure on cyclic homology — the braiding.

The Drinfeld center Z(Rep^{E_1}(A)) ~ Rep^{E_2}(Z^der_ch(A)) provides the categorical incarnation of the bulk-boundary correspondence: E_1 boundary -> E_2 bulk via the center construction.

## E₁/Ordered as Primitive (PERMANENT, 2026-04-08)

**The E₁/ordered story is the natural primitive across all three volumes.** In Vol III, this has a specific incarnation: the E₁-chiral algebra (boundary) is the primitive object; the E₂-chiral algebra (bulk) is obtained from it by the Drinfeld center construction; quantum groups (Rep_q(𝔤)) are the natural categorification of E₁ data. The averaging map av: g^{E₁} → g^mod from Vol I becomes the center construction Z: E₁-Cat → E₂-Cat in Vol III. The passage from E₁ to E₂ is the higher-categorical analogue of Σ_n-coinvariance.

**Consequence for Vol III architecture:** Quantum groups, Yangians, and braided tensor categories are NATIVELY E₁ objects. The E₂/braided structure arises via the Drinfeld center, which is the categorified averaging map. The CY-to-chiral functor Φ should be understood as lifting E₁ data (the boundary A∞-algebra from the CY category) to E₂ data (the bulk chiral algebra) — this is the center construction in the factorization setting. See Vol I `princ:e1-primacy` for the full architectural thesis.

## Main Theorems (Targets)

- **CY-A** (CY-to-chiral functor): Construction of Phi: CY_d-Cat -> E_2-ChirAlg via E_2-factorization envelope
- **CY-B** (E_2-chiral Koszul duality): Bar-cobar adjunction in the E_2-chiral setting, CY trace as curvature
- **CY-C** (Quantum group realization): Rep^{E_2}(A_C) is braided monoidal equivalent to C itself, when C arises from a quantum group (generalizing Kazhdan-Lusztig)
- **CY-D** (Modular CY characteristic): kappa(A_C) = chi^CY(C), genus-g obstruction recovers GW/Hochschild invariants

## Architecture (Five Parts)

**Part I — The CY Engine** (part:cy-categories)
- Introduction
- CY categories (smooth, proper, CY condition, trace)
- Cyclic A-infinity structures (cyclic bar complex, S^d-framing)
- Hochschild calculus (HH duality, categorical Hodge theory)
- E_1-chiral algebras (review from Vol II)
- E_2-chiral algebras (central innovation: braided factorization)
- E_n-factorization and higher chiral structure

**Part II — The CY Characteristic Datum** (part:bridge)
- CY-to-chiral functor (cyclic -> Lie conformal -> factorization envelope -> E_2 enhancement -> quantization)
- Quantum chiral algebras (R-matrix, quantum YBE, shadow depth)
- The modular trace (CY characteristic, genus expansion, shadow obstruction tower)
- Quantum groups foundations (U_q, R-matrix, YBE)
- Braided factorization (E_2 bar-cobar, braided Koszul duality)
- Drinfeld center and bulk algebras

**Part III — The CY Landscape** (part:examples)
- Toroidal and elliptic examples (includes K3 x E)
- Toric CY3 CoHA
- Fukaya categories (elliptic, K3, CY 3-folds, wrapped)
- Derived categories of CY manifolds (HMS, exceptional collections, stability)
- Matrix factorizations (LG models, ADE singularities, W-algebras)
- Quantum group representations (Rep_q(g), Kazhdan-Lusztig, Yangian/RTT)

**Part IV — The Seven Faces of r_CY(z)** (part:connections)
- Bar-cobar bridge to Volume I
- CY holographic datum
- Modular Koszul bridge

**Part V — The CY Frontier** (part:frontier)
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

**AP59-AP61 (from the seven-faces swarm, April 7 2026):**
- **AP59**: Three distinct invariants must never be conflated: p_max(A) (generator OPE pole order) ≠ k_max(A) (collision depth = p_max - 1) ≠ r_max(A) (shadow depth, arity at which the obstruction tower terminates). The βγ system is the archetypal witness: p_max(βγ) = 1, k_max(βγ) = 0, r_max(βγ) = 4 (class C). Conflation produces wrong classifications. Found in T6 first draft (CRITICAL F16/F17, 2026-04-07). **Rule: when discussing "depth", always specify which invariant. Formal definitions in Vol I chapters/theory/three_invariants.tex.**
- **AP60**: Status inflation when combining new and known content. When a theorem combines a new identification with classical results (Drinfeld 1985, STS 1983, FFR 1994), do NOT tag the entire theorem ProvedHere. Restrict the ProvedHere claim to genuinely new content; classical components are ProvedElsewhere with attribution. Found in T5 (Sklyanin theorem) first draft (SERIOUS F12, 2026-04-07).
- **AP61**: Hardcoded values from CLAUDE.md descriptions inherit conflations. Compute engines copying values from CLAUDE.md "shadow archetypes" can inherit semantic conflations. The βγ p_max=2 hardcoded value came from interpreting "betagamma=contact/quartic/terminates@4" as p_max=2 instead of r_max=4. **Rule: never copy a numerical invariant from a CLAUDE.md description without verifying against (1) the OPE table, (2) landscape_census.tex, (3) at least one cross-engine comparison.**

**Additional Vol III-specific pitfalls from the audit:**
- **AP-CY6**: A_X does NOT exist for CY3. The chiral algebra of a Calabi-Yau threefold is the single load-bearing gap. CY-A is proved for d=2; for d=3, A_X is conditional on chain-level S³-framing construction. NEVER write "A_X for CY3" as if it were a defined object.
- **AP-CY7**: CoHA ≠ E₁-chiral algebra. The critical CoHA (Schiffmann-Vasserot, RSYZ) is an associative algebra; calling it "the E₁-sector of G(X)" assumes G(X) exists and has a CoHA inside it. The correct statement: "the CoHA is the target that the E₁-sector of G(X) should match, IF G(X) exists."
- **AP-CY8**: Borcherds denominator identity ≠ bar Euler product. The identification requires the CY-to-chiral functor to exist in the relevant dimension. For K3 × E (d=3), Δ₅ is computed from the lattice, not from a chiral algebra (which doesn't exist yet). The "bar Euler product" interpretation is an OBSERVATION about the product formula, not a theorem derived from the bar complex.

## Anti-Patterns from the 2026-04-07 Frontier Research Swarm (AP62-AP80)

From the 125-agent session. See Vol I CLAUDE.md for FULL descriptions with examples and derivations. Summary:
- **AP62**: Bar cohomology "depends only on dim(g)" TRUE for Euler char, FALSE for individual dims
- **AP63**: CE(g_-) ≠ chiral bar for multi-generator algebras (Orlik-Solomon correction)
- **AP64**: Same cohomology, different gradings → different sequences (CE weight vs PBW degree)
- **AP65**: ORDERED (E1) bar is PRIMITIVE; unordered is derived quotient losing quantum group data
- **AP66**: Partition-type GFs (free fields) are NOT D-finite; interacting algebras ARE
- **AP67**: Strong generation ≠ FREE strong generation (W(p) Koszulness OPEN)
- **AP68**: PVA slab ghost c ≠ chiral algebra κ (SVir κ = (3c-2)/4, NOT (c+11)/2)
- **AP69**: τ_shadow satisfies κ-DEFORMED KdV, NOT standard KdV. Obstruction κ(κ-1)
- **AP70**: Shadow L^sh(s) has POLES at s=1,2; negative integers are trivial zeros
- **AP71**: Shadow κ ≠ Dyson β ≠ Painlevé parameter
- **AP72**: W-algebra NOP bar does NOT have d²=0; needs full singular OPE + Orlik-Solomon
- **AP73**: BV=bar chain-level: PROVED G/L, CONDITIONAL C/M
- **AP74**: Shadow Eisenstein proof cites FALSE Bernoulli-Dirichlet identity
- **AP75**: Koszulness ≠ H^k=0 in conformal weight grading (only PBW degree)
- **AP76**: Y_{1,1,1} has c=0 (NOT 3); κ=Ψ from Heisenberg channel
- **AP77**: Stokes ratio tests on convergent series give spurious instanton actions
- **AP78**: Hardy-Ramanujan 1729 "coincidence" in δF₂ is illusory
- **AP79**: W(p) has 4 strong generators, not 2
- **AP80**: Agents can produce engine without test file

## Anti-Patterns from the 2026-04-08 Bar/SC/E_1 Primacy Research (AP81-AP104)

From the 22-agent bar construction / Swiss-cheese / E_1 primacy investigation. See Vol I CLAUDE.md for FULL descriptions with proofs and derivations. These arise at the OPERADIC LAYER.
- **AP81**: Operadic bar of P-algebra ≠ operadic bar of operad P. Use B_P(A) vs BP.
- **AP82**: Three coalgebra structures on bar: Lie^c (Harrison/coLie), Sym^c (coshuffle/cocommutative), T^c (deconcatenation/coassociative). NEVER conflate.
- **AP83**: Coshuffle (2^n terms) ≠ deconcatenation (n+1 terms). Found at bar_construction.tex line 1563.
- **AP84**: B_{Com}(A) is cofree coLie, NOT cocommutative. CE complex is cocommutative; operadic bar is coLie.
- **AP85**: Factorization coproduct (Vol I, Sym^c) ≠ deconcatenation coproduct (Vol II, T^c). Different objects, different geometries.
- **AP86**: FM_n(X) connected; only boundary strata factor as FM_{|S|} × FM_{n-|S|+1}.
- **AP87**: SC^{ch,top,!} mixed-sector dim = (k-1)!·C(k+m,m), NOT (k-1)!·m!.
- **AP88**: Cooperad P¡ vs operad P^! notation collision. P¡ = cooperad; P^! = (P¡)^∨.
- **AP89**: B_{SC}(A) for one-coloured A is ill-formed. SC requires two-coloured (V_c, V_o).
- **AP90**: Promotion functor A ↦ (A,A): self-action gives SC input. Closed = B_{Com}(A), open = B_{Ass}(A).
- **AP91**: Curved d² = κ·ω_g NOT a coderivation at g ≥ 1. Factor-2 cross-term discrepancy. Period-corrected D^{(g)} required.
- **AP92**: Algebra-level μ_0 (genus 0, strict) vs fiberwise d_fib² = κ·ω_g (genus ≥ 1, Hodge). Different scales.
- **AP93**: δF_g^cross in CLOSED sector, NOT mixed sector. "Mixed channels" ≠ "mixed sector."
- **AP94**: Polynomial Hilbert series ≠ polynomial RING. ChirHoch^*(Vir_c) total dim ≤ 4. NEVER write ℂ[Θ].
- **AP95**: ChirHoch ≠ Gel'fand-Fuchs of Diff(S¹). Unrelated invariants at different categorical levels.
- **AP96**: Shadow algebra A^sh is bigraded LIE ALGEBRA, NOT ring. Bracket of degree 0, arity map -2.
- **AP97**: Averaging av: g^{E_1} → g^mod is LOSSY. av(r(z)) = κ; R-matrix strictly richer.
- **AP98**: κ Eulerian weight parity-dependent. Even desuspension → symmetric weight 2. Odd → Harrison weight 1.
- **AP99**: K11 Lagrangian criterion CONDITIONAL on perfectness + bar-cobar normal-complex identification.
- **AP100**: Theorem C: eigenspace (C1) unconditional; scalar F_g = κ·λ_g (C2) uniform-weight only.
- **AP101**: "qi, not merely iso on cohomology" is tautological. Use "qi of A∞-algebras" vs "chain qi."
- **AP102**: Theorems MUST specify which bar: B^ord, B^Σ, or B^Lie.
- **AP103**: Cotriple bar (monadic, always defined) ≠ operadic bar (P¡-coalgebra, Koszul locus).
- **AP104**: E_1/ordered is PRIMITIVE; modular/symmetric is av-image. NEVER present ordered as "auxiliary." (Particularly relevant for Vol III CY/DT structures where the CoHA is naturally E_1.)

**Meta^5-rule (from AP81-AP104):** the same error can recur at the OPERADIC-ARCHITECTURAL level. AP81-AP104 catch errors in the categorical level at which bar-cobar operates — confusing which operad, cooperad, coalgebra structure, and colour an operation lives in.

## Agent Anti-Patterns (AAP1-AAP18)

Cross-volume agent workflow anti-patterns. See Vol I CLAUDE.md for full descriptions. Summary: AAP1 (tool-markup leak), AAP2 (fragmented renames), AAP3 (formula duplication), AAP4 (proof after conjecture), AAP5 (artifact noise), AAP6 (status oscillation), AAP7 (intra-file inconsistency), AAP8 (README drift), AAP9 (premature relaunch → cascading rate limits), AAP10 (engine without test file), AAP11 (test expectations encode AP10), AAP12 (asymptotic tolerance too tight), AAP13 (silent model downgrade without testing), AAP14 (worktree branch collisions), AAP15 (parallel pdflatex SIGKILL races), AAP16 (git stash FORBIDDEN), AAP17 (truncated agent reports — verify via diff), AAP18 (confabulating operadic theory — compute or cite).

## Build

```
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
```

Same engine as Volumes I-II: memoir, EB Garamond, newtxmath, thmtools, microtype.

## The Symphonic Standard (PERMANENT)

**The monograph must move like the greatest symphony the world has ever known.** Every sentence carries mathematical weight. Every construction is inevitable. Every theorem earns its place by solving a problem the reader already feels. This standard applies to ALL writing: manuscript, standalone papers, working notes, concordance, preface, introduction, appendices. No exceptions.

### The Voices and What They Demand

**Gelfand** (functorial inevitability): Every definition is a theorem in disguise. The right level of generality is natural, not maximal. Constructions have a "could not be otherwise" quality.

**Beilinson** (falsification and depth): No false ideas survive. Sparse, surgical prose. The epistemic hierarchy is always visible.

**Drinfeld** (deformation-theoretic soul): Quantum groups emerge from geometry. The R-matrix is a shadow of the MC element. Every construction has a deformation-theoretic origin.

**Kazhdan** (D-modules as language): The correct categorical framework is substance, not decoration. No shortcuts in geometric arguments.

**Etingof** (crystal clarity): Every fact earns its keep through computation. A graduate student can follow the argument on first reading.

**Nekrasov** (partition functions as algebra): The generating function IS the mathematical object. No gap between physics and mathematics.

**Polyakov** (the functional integral is real): The OPE is a consequence of locality. Physical reasoning is the deepest layer.

**Kapranov** (higher categories as substance): Operads have geometric content. Categorical structures solve problems, never invoked for their own sake.

**Ginzburg** (the Chriss-Ginzburg standard): Every object solves a problem. Every paragraph forces the next. No dead weight. The architecture of text mirrors mathematics.

**Costello** (factorization algebras as rigorous physics): Perturbative QFT is a theorem. The physical story comes first, then framework, then results.

**Gaiotto** (dualities as tools): Dualities compute invariants. Worked examples are where the theory proves itself.

**Witten** (physical insight precedes proof): The deep structure is geometric. The introduction states what is true in three pages, not thirty. No hedging.

### Prose Laws (apply to ALL writing in the programme)

1. **No AI slop.** Zero tolerance for: "notably", "crucially", "remarkably", "it is worth noting", "interestingly", "this is particularly significant." Delete them.
2. **No hedging where the mathematics is clear.** Proved → state it. Open → state it. No "we believe that" when the status is known.
3. **No em dashes for subordinate clauses.** Use colons, semicolons, or separate sentences.
4. **No passive voice hedging.** "It can be shown that" → state the theorem.
5. **Every paragraph forces the next.** Momentum from mathematical necessity.
6. **State once, prove once, use everywhere.** No duplication.
7. **Every chapter opens with the problem it solves.** Not "In this chapter we study..."
8. **Scope is always explicit.** "For all" specifies the universe. "Proved" specifies hypotheses.
9. **The physical and mathematical are unified.** Not separate sections but woven together.
10. **Comparison with prior work is surgical.** One sentence per paper.

## LaTeX Rules

- All macros in main.tex preamble — NEVER \newcommand in chapter files (use \providecommand)
- Document class: memoir; fonts: EB Garamond via newtxmath + ebgaramond
- Claim status: \ClaimStatusProvedHere, \ClaimStatusProvedElsewhere, \ClaimStatusConjectured, \ClaimStatusHeuristic, \ClaimStatusOpen
- Label everything: \label{def:}, \label{thm:}, etc. Cross-reference with \ref.
- Do not add packages without checking preamble compatibility
- Do not create new .tex files when content belongs in existing chapter

## Git — HARD RULE

All commits authored by Raeez Lorgat. **Never credit an LLM.** No "co-authored-by", no "generated by", no AI attribution anywhere.
