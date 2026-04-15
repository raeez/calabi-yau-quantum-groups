# AGENTS.md - Calabi-Yau Quantum Groups

## Charter

This file is the always-on Codex constitution for Volume III. It is optimized for Codex with GPT-5.4-style agentic work: persistent tool use, explicit verification, tight scope control, and sharp stopping criteria. `CLAUDE.md` may remain richer and more experimental, but `AGENTS.md` must be the stable operating system that still works after compaction, context loss, or model drift.

Use this file for:

- durable repo-wide invariants;
- task routing and operating modes;
- claim-state and definition discipline;
- cross-volume propagation rules;
- verification and convergence gates;
- the current dated risk map when live repo state materially changes behavior.

Do not use this file for temporary chatter, local TODO spam, or motivational prose that does not change execution.

## Programme Map

Volume III asks a single question:

> In what precise sense can a Calabi-Yau category produce a quantum chiral algebra whose bar data, trace, and modular characteristic match the modular Koszul duality programme from Volumes I and II?

Primary targets:

- `CY-A`: `Phi: CY_d-Cat -> E_2-ChirAlg`
- `CY-B`: `E_2`-chiral bar-cobar adjunction with CY trace as curvature datum
- `CY-C`: quantum-group realization
- `CY-D`: modular CY characteristic

Current hard status boundary:

- `CY-A` is proved for `d = 2` (unconditional) and `d = 3` (inf-categorical, thm:derived-framing-obstruction). Chain-level explicit construction at d=3 remains open for non-formal algebras.
- `G(X)` and `C(g,q)` (quantum group realization, CY-C) are NOT constructed objects. CY-C remains CONJECTURAL.
- CoHA is associative data, not automatically the `E_1` sector of a larger chiral object.
- Borcherds denominator identities are not automatically bar Euler products.

### 6d hCS Programme (April 2026)

The Costello programme constructs chiral quantum groups from holomorphic CS. New infrastructure:

- **E_1-chiral bialgebra**: the correct Hopf framework (NOT E_∞ vertex bialgebra). Axioms in `e1_chiral_algebras.tex` §7 (~400 lines). Coproduct on E_1 (ordered) side of Swiss-cheese; E_∞ averaging kills Hopf data.
- **E_3 bar cohomology**: `(1+t)^{3g}` for classes L,C; FAILS for class M. Chain level always `P(q)^{3g}`.
- **Kummer route**: `∫_{K3} F` via CY-A_2 only. Steps 1-4 PROVED (Proposition). Step 5 conjectural.
- **K3 Yangian**: degree-(24,24) structure function. Bar Euler = `η^{24}` = Ramanujan Δ.
- **Borcherds lift = resummation**: additive (Saito-Kurokawa) = perturbative; multiplicative (Borcherds product) = non-perturbative.
- **Center-hocolim**: >92% of K3×E Drinfeld center non-local. MO stable envelopes bypass it.
- **E_2→E_3 promotion**: derived center (higher Deligne), NOT iterated Drinfeld center.

### Latest Frontier Results (late April 2026)

- **Universal coproduct**: Δ_z(e_s) = Σ (-1)^k C(N_R-b,k) z^k e_a^L·e_b^R. All spins in closed form. z-degree = s.
- **Coassociativity is trivial**: Miura multiplicativity T_0·T_1·T_2 = associative. Mode-level verification unnecessary.
- **Spin-4 coproduct derived**: 3 structural cross-term types at z^0 (including new T^L·T^R). z-degree = 3.
- **bc system**: (1+t)^{3g} universal for ALL class C (bosonic + fermionic). 230 new tests.
- **K3 Koszul conductor = 0**: free-field branch. κ_ch + κ_ch' = 2 + (-2) = 0.
- **S³ ≠ S² × S¹**: CY-A₃ framing non-decomposable. Relative chiral algebra bypasses differently.
- **κ = χ at d=2**: Serre duality S=[2] kills one-loop correction. Status discrepancy to reconcile.
- **CoHA(A₁) = gl(1|1) ≠ W₂**: c=0 coincidence ≠ isomorphism. W-algebras enter at rank ≥ 2.
- **Three-centers remark**: written in drinfeld_center.tex distinguishing Z(C), HH*(B,B), Z_2(C).
- **Factorization-homology coproduct**: 180 lines in e1_chiral_algebras.tex. General CY coproduct from Ran excision (no Miura needed).
- **Vol I/II cross-refs inscribed**: shadow=A_∞ in Vol I, E_1-bialgebra in Vol II.
- **κ=χ confirmed correct**: d=2 ProvedHere, d≥3 Conjectured. No discrepancy.
- **All builds pass**: Vol I (2636pp), Vol II, Vol III. ~1,800+ tests.

### K3 Quantum Group Session Results (April 2026, 53-agent wave)

~62 new pages, ~3,600 new tests, ~65 new engines. Total: ~433pp, 23,631 tests, 246 engines.

- **Phi(K3) explicit** (thm:phi-k3-explicit): CY-to-chiral functor on K3 produces rank-24 Heisenberg, Mukai pairing (4,20). 93 tests.
- **K3 abelian Yangian** (thm:k3-abelian-yangian-presentation): RTT presentation with degree-(24,24) structure function. 47 tests.
- **Super-Yangian Y(gl(4|20))**: conjectural. BKM-to-Yangian lift from Mukai signature. 59 tests.
- **K3 quantum toroidal** (conj:k3-quantum-toroidal): U_{q,t}(gl_hat_hat_1)^{K3}. 51 tests.
- **MO R-matrix charge 2** (prop:mo-rmatrix-charge2): stable envelope matches K3 Yangian. 60 tests.
- **Borcherds vertex spectral flow**: spectral flow of Y(g_{K3}) from vertex operators. 75 tests.
- **Cech-HTT convergence** (prop:cech-htt-coefficient-convergence): HTT series convergent for all smooth CY₃. 64 tests.
- **S³ non-decomposable** (prop:hopf-fibration-decomposition): CY-A₃ framing irreducible. 67 tests.
- **kappa_BKM universal**: c_N(0)/2 is the ONLY correct formula. Naive decomposition fails N>=2. 62 tests.
- **ZTE correction exists** (prop:zte-deformation-cohomology): extended complex rank 35/36, S^{corr} constructible. 47 tests.
- **K3 Serre relations**: imaginary root null vectors. 61 tests.
- **K3 quantum determinant**: q-det(T(u)) central. 76 tests.
- **ADE Yangian level 1**: all ADE via McKay. 63 tests.
- **Costello 5d verification**: hCS -> Yangian verified charge 4. 87 tests.
- **W2 triplet mock modular**: shadow = 24*eta^3. 70 tests.
- **Shadow class moduli variation**: G at large volume, M at conifold. 88 tests.

### Roadmap: Load-Bearing Open Problems (DEFINITIVE status, April 2026, ~230-agent session)

1. **CY-A₃** (S³-framing): **RESOLVED** (inf-categorical, thm:derived-framing-obstruction). HH^{-2}_{E_1}=0, Goodwillie vanishing, E_3-liftings contractible. Coefficient convergence PROVED. S³ non-decomposable. Chain-level explicit construction remains open for non-formal algebras. **BKM Serre is EXACT** (P_2(D)=0, 70 tests).
2. **ZTE correction** S^{corr} = S + κ²T. **COMPUTED** (exact rational T matrix, 35 tests). Previously constructive (rank 35/36); now explicit entry-by-entry from 1-dim kernel. Promoted from constructive to computed.
3. **K3 Yangian quantization** **PARTIALLY RESOLVED.** Abelian Y(g_{K3}) presented (thm:k3-abelian-yangian-presentation). RTT, q-det, Serre (EXACT via P_2=0). Super-Yangian Y(gl(4|20)) conjectural (AP-CY35). Non-abelian K3 Yangian open. E_8 x E_8 structure function: degree-(24,24), c=24.
4. **Non-abelian sl₂** ADE Yangian level 1 for all types. K3 non-abelian coproduct (50 tests). Serre null vector verified. Matrix Lax coassociativity via trace. **Chiral Satake for C^3 PROVED** (99 tests).
5. **Sp₄(Z) modularity** sp4_modularity_pipeline (53 tests). Fourier-Jacobi = E₂→E₃. Mathieu moonshine: frame shape = twined bar Euler for all 25 M_24 classes.
6. **CY-B at d=3**: NOW ACTIVE. E_1-chiral Koszul duality (inducing E_2 on Drinfeld center) extended to d=3 via inf-cat CY-A_3. 131 tests. Chain-level conditional.
7. **CY-D at d=3**: DEEP ISSUE IDENTIFIED. chi(O_{K3xE})=0 != 3=kappa_ch. Formula must use Hodge-filtered supertrace str_{F^0}(q^{L_0}), not chi(O_X). Dimension-stratified: kappa_ch != chi(O_X) at odd d.
8. **Root-of-unity**: N=2 gives 324 modules, abelian S-matrix degenerate. Non-abelian K3 Yangian needed for modularity.
9. **Shadow tower**: Computed through m_8 (160 tests, S_8=4144720/19683). m_5 independently verified (G_5^{conn}=775/5184).
10. **Chiral volume conjecture**: FORMULATED (Abel-Jacobi period). Connects chiral bar volume to CY period integrals.

### Deepest Frontier (final wave, late April 2026)

- **A_∞ coproduct = shadow tower**: Δ^{A_∞} = Δ^{Yangian} + Σ ℏ^k δ^{(k)} where δ^{(k)} coefficients = shadow S_k. Class G exact, class M infinite.
- **z=0 category error resolved**: spectral z ≠ worldsheet z. No OPE poles. Δ_0 = cocommutative Hopf coproduct.
- **Factorization ⊗ = colim over ordered configs**: not np.kron. Non-symmetric, strictly associative.
- **Coproduct combinatorics**: N(s,p) = s-p, GF = x/((1-x)²(1-xy)), subleading = (s-1)ψ_2^R + J^L·J^R.
- **Non-abelian sl₂**: trace of matrix Lax gives coassociativity; Serre null vector g_{i0}·g_{i1}=1.
- **ZTE FAILS for Yang R-matrix**: COMPUTED. S=RRR does NOT solve tetrahedron at O(κ²). E_3 is genuinely nontrivial. Engine: 1200 lines, 34 tests.
- **A_∞ coproduct = shadow tower**: corrections δ^{(k)} with coefficients = shadow S_k unify coproduct theory with shadow classification.

### FINAL Wave Results (April 2026)

- **P_2(D) = 0: BKM Serre EXACT**: Second Serre polynomial vanishes identically. Two independent arguments: Nekrasov (eps_1*eps_2=0 in 1d Omega-background) + Lie algebra twist (L_0+eps*J_0 linear in eps). 182-generator Serre kernel is the FULL kernel. 70 tests.
- **Borcherds spectral flow h=1 EXACT**: Not approximate. Verified through 10 Fourier coefficients against Borcherds product.
- **CY-B at d=3**: E_1-chiral Koszul duality (inducing E_2 on center) extended to d=3 via inf-cat CY-A_3. 131 tests. Chain-level conditional.
- **Chiral Satake for C^3**: Derived geometric Satake proved. Phi(C^3) = W_{1+inf} connected to Rep(Y(gl_1^)). 99 tests.
- **Chain-level incompatibility**: mu_3 != 0 forces mu_2 = 0 on augmentation ideal. E_1 product and A_inf corrections cannot coexist on same graded piece.
- **kappa_ch mechanism**: Hodge-filtered supertrace str_{F^0}(q^{L_0}). Non-F^0 killed by Hodge filtration. Coincides with chi(O_X)/2 at d=2 via Serre duality; diverges at d=3.
- **CY-D deep issue**: chi(O_{K3xE}) = 0 != 3 = kappa_ch. Target-space anomaly != worldsheet anomaly at d=3. The CY-D formula must use str_{F^0}, not chi(O_X).
- **Infrastructure**: Notation appendix (541 lines), AP catalogue (668 lines), 10 proofs publication-upgraded, Part openers + 3 reading paths installed.

### ~230-Agent Comprehensive Wave Results (April 2026, DEFINITIVE)

- **ZTE T matrix COMPUTED**: exact rational entries, 35 tests. Previously constructive; now explicit entry-by-entry from 1-dim kernel.
- **Shadow tower through m_8**: 160 tests. S_8=4144720/19683. Full tower from S_3 to S_8.
- **m_5 independently verified**: G_5^{conn} = 775/5184 from 5-point Wick contraction. Cross-checks shadow tower.
- **Chiral volume conjecture FORMULATED**: Abel-Jacobi period connects chiral bar volume to CY period integrals.
- **Mock modular K3**: THEOREM at d=2. 4-step proof: shadow -> mock theta -> Zwegers -> Borcherds.
- **CY-D dimension-stratified**: kappa_ch != chi(O_X) at odd d. Replaces naive CY-D at d=3.
- **CY-C abelian level**: C(g,q) = D(Y^+(g_{K3})). Explicit Drinfeld double construction.
- **E_8 x E_8**: structure function degree-(24,24), c = 8+8+8 = 24.
- **Root-of-unity N=2**: 324 modules, abelian S-matrix degenerate.
- **Mathieu moonshine**: frame shape = twined bar Euler for all 25 M_24 conjugacy classes.
- **Incompatibility strengthened**: mu_3!=0 forces mu_2=0 on aug for ALL non-formal (class >= L).
- **7-part structure**: Part openers + 3 reading paths. 10 proofs at publication standard.
- **Clean build**: 0 undef refs, 0 undef cites. ~693pp, ~34,000 tests, ~460 engines.

### Anti-Patterns Mined from 180-Agent Swarm (AP-CY27-33)

7. **Agent sandbox non-persistence (AP-CY27)**: Background agents' file writes do NOT persist to the main working tree. ALWAYS `ls` to verify file existence after agent completion. Three engines were "verified passing" inside sandboxes but didn't exist on disk.
8. **Pole-unsafe test points (AP-CY28)**: Rational structure functions g(z) have poles at z=±h_i. Test points MUST avoid these. Default h=(1,-2,1) has poles at z=±1,±2. Use h=(37,41,-78) for safety.
9. **Wrong-repo file writes (AP-CY29)**: Agents write to the WRONG volume. sl₂ engine was written to Vol I instead of Vol III. Verify FULL PATH after any agent write.
10. **Factored ≠ solved (AP-CY30)**: S=RRR from YBE does NOT solve ZTE. Proved: O(κ²) obstruction. Kapranov-Voevodsky requires E_∞; Omega-deformation breaks it.
11. **Spectral z ≠ worldsheet z (AP-CY31)**: Drinfeld Δ_z = spectral shift. OPE T(z)T(w) = worldsheet. Setting z=0 in Δ_z has no poles. Never conflate.
12. **Reorganisation ≠ bypass (AP-CY32)**: 6d route reorganises CY-A₃ into subproblems but solves none independently.
13. **Chain-level ≠ rational (AP-CY33)**: E₃ genuine at chain level, collapses under formality/Q. Physical content (Miki, factorization homology) lives at chains.

### Anti-Patterns from 53-Agent K3 Session (April 2026)

14. **Numerical coincidence masquerading as structure (AP-CY34)**: kappa_BKM = kappa_ch + chi(O_fiber) holds for K3xE (N=1) but FAILS for all Z/NZ-orbifolds N>=2. The adversarial engine (62 tests) revealed a numerical coincidence misidentified as a theorem. Counter: test ANY proposed formula against the full orbifold family N=1..8 before claiming universality.
15. **Superalgebra rank inflation (AP-CY35)**: Agents assign gl(N|M) structure to lattice-graded algebras based on signature matching alone. The Mukai lattice signature (4,20) does NOT automatically produce gl(4|20). The super-Yangian Y(gl(4|20)) is CONJECTURAL. Counter: super structures require explicit Lie bracket verification, not just grading compatibility.
16. **RTT-OPE dictionary incompleteness (AP-CY36)**: The RTT presentation R(u-v)T_1(u)T_2(v) = T_2(v)T_1(u)R(u-v) and the OPE T(z)T(w) ~ ... are NOT interchangeable without specifying normal ordering. The translation requires explicit contour deformation and regularization. Counter: always specify which presentation is being used and whether a dictionary exists.
17. **Convergence radius vs convergence domain**: The Cech-HTT convergence radius 1/(4||s.delta||) is a LOWER BOUND on the polydisc. The actual convergence domain may be larger (and typically is). Agents conflated "convergent with radius R" with "divergent beyond R." Counter: state bounds as bounds, not as equalities.

### Codex/GPT-5.4-Specific Weakness Mitigations

1. **Docstring confabulation (AP-CY24)**: GPT models fabricate "ground truth" values in docstrings while producing correct code. ALWAYS verify docstring values against function output before committing.
2. **Composite arrow confabulation (AP150)**: GPT stitches real ingredients into non-existent composites. Verify EACH ARROW independently.
3. **Sign errors in bar differentials**: Agents consistently get signs wrong in arity-3+ bar computations. Always pin sign conventions with explicit tests.
4. **R-matrix extraction (AP-CY25)**: The formula R=(id⊗S)∘Δ(1) is WRONG. Use half-braiding construction.
5. **σ_2 parity (AP-CY26)**: σ_2 is EVEN under h_i→-h_i. Level inversion k^!=-k comes from Shapovalov, not σ_2.
6. **Drinfeld center and derived/chiral center are distinct** unless hypotheses are stated.

## Agent Deployment History

| Session | Date | Agents | Tests | Pages | Key Deliverables |
|---------|------|--------|-------|-------|------------------|
| DNP/KZ/GZ research + rectification | 2026-04-07/08 | ~230 | 118,823 (cross-volume) | ~50 | 8 theorems, 32 engines, 12 frontier directions, Beilinson audits |
| SC bar complex / E₁ primacy | 2026-04-08 | ~200 | 885 | ~40 | Three-bar-complex picture, E₁ primacy, BV/BRST class-by-class |
| 6d hCS chiral quantum groups | 2026-04-12/13 | ~170 | ~1,800 | ~60 | E_1-chiral bialgebra axioms, ZTE failure/existence, universal coproduct |
| K3 quantum group programme | 2026-04-13 | 53 | ~3,600 | ~62 | Phi(K3) explicit, K3 abelian Yangian, super-Yangian, MO R-matrix, Cech-HTT convergence |
| Consolidated 129-agent session | 2026-04-13 | 129 | ~29,500 | 485 (+114) | ~360 engines. Shadow=A_inf coproduct, shadow-Feynman dictionary, class M E_3 bar, chiral CE=bar, Pixton-CY bar, class M Borel summability |
| Final 170-agent comprehensive | 2026-04-13 | ~170 | 30,613 | 533 (+48) | ~410 engines. CY-A_3 inf-cat proof, K3 abelian Yangian, ZTE correction existence, kappa_BKM universal, BKM Serre D=3, super-Yangian Y(gl(4\|20)), 6 routes to G(K3xE), CFG25 comparison, Borcherds spectral flow, shadow-Feynman dictionary, E_3 bar=6^g, derived Satake, tropical cluster, chiral Verlinde, Hitchin quantization, BLLPR, explicit ZTE T, p-adic Langlands, BFN Coulomb, form factors, handle decomposition, stratified FH, Mathieu moonshine, 3 wrong proofs caught, AP-CY35-40 |
| FINAL documentation wave | 2026-04-13 | docs | ~31,000 | ~550 (+17) | ~420 engines. P_2(D)=0 BKM Serre exact, Borcherds spectral flow h=1 exact, CY-B push d=3 (131 tests), chiral Satake C^3 (99 tests), chain-level incompatibility theorem (mu_3!=0 forces mu_2=0 on aug), notation appendix (541 lines), AP catalogue (668 lines), 10 proofs publication-upgraded, Part openers + 3 reading paths, kappa_ch deep mechanism (Hodge-filtered supertrace), CY-D d=3 deep issue (chi(O_{K3xE})=0 != 3=kappa_ch) |
| ~230-agent comprehensive | 2026-04-13/14 | ~230 | ~34,000 | 693 (+143) | ~460 engines. ZTE T matrix COMPUTED (exact rational, 35 tests). Shadow tower through m_8 (160 tests, S_8=4144720/19683). m_5 independently verified (G_5^{conn}=775/5184). Chiral volume conjecture FORMULATED (Abel-Jacobi period). Mock modular K3: THEOREM at d=2 (4-step proof). CY-D dimension-stratified (kappa_ch!=chi(O_X) at odd d). CY-C abelian: C(g,q)=D(Y^+(g_{K3})). BKM Serre P_2=0 EXACT. E_8xE_8 structure function (24,24), c=24. Root-of-unity N=2: 324 modules, S-matrix degenerate. Mathieu frame shape = twined bar Euler (all 25 M_24 classes). Incompatibility theorem strengthened. 7-part structure with Part openers + reading paths. Appendices: notation (541 lines) + AP catalogue (668 lines). 10 proofs at publication standard. Clean build: 0 undef refs, 0 undef cites. |

**Cumulative Vol III**: ~693pp, ~34,000 tests, ~460 engines.

## Design Axioms for Codex/GPT-5.4

Best-practice prompt design in this repo means reducing entropy, not adding rhetoric.

1. Exact scope before reasoning.
   Name the file, theorem label, definition, convention, family, and status boundary before trying to solve the problem.
2. Verification before verbosity.
   Prefer a short instruction plus a falsifiable check over long exhortation.
3. Reasoning effort is a last-mile knob.
   Before escalating effort, tighten the task definition, output contract, and verification loop.
4. Durable rules, triggered playbooks, mechanical hooks.
   Keep always-on rules here, deep workflows in skills, deterministic enforcement in hooks or grep-based checks.
5. Local truth surfaces over inherited summaries.
   Live `.tex`, compute, tests, logs, and diffs outrank memory, prior chats, and metadata prose.
6. Self-contained state beats hidden context.
   For substantial work, externalize the plan, assumptions, blockers, and verification record in a durable note.
7. Smaller true claims beat larger false ones.
   The objective is not impressive prose; it is surviving hostile rereading.
8. Add instructions only when they change behavior.
   Remove decorative meta-rules, duplicated guidance, and vague slogans that widen the search space.

### GPT-5.4 Prompt Architecture (for composing task prompts)

When composing task prompts for Codex agents or sub-agents, use XML-tagged blocks for structural clarity:

- `<task>`: the concrete job and repository context
- `<structured_output_contract>`: exact shape, ordering, brevity requirements
- `<default_follow_through_policy>`: act without asking routine questions; stop only when a missing detail changes correctness or safety
- `<verification_loop>`: verify result against task requirements before finalizing
- `<grounding_rules>`: ground every claim in evidence; label hypotheses
- `<missing_context_gating>`: do not guess missing repository facts; retrieve with tools or state unknowns
- `<completeness_contract>`: resolve fully; check for follow-on fixes and edge cases
- `<dig_deeper_nudge>`: after first finding, check for second-order failures, empty-state behavior, stale state
- `<action_safety>`: keep changes scoped; avoid unrelated refactors; call out risky actions
- `<tool_persistence_rules>`: keep using tools until evidence suffices; do not abandon after partial read

**Anti-patterns to avoid**: vague task framing; missing output contract; asking for "more reasoning" instead of better contract; mixing unrelated jobs into one run; unsupported certainty without grounding.

## Codex-Native Operating Stance

- Default deliverable: a verified change or a precisely named blocker, not an outline.
- Default reasoning: `medium`.
- Escalate to `high` or `xhigh` only for load-bearing proof surgery, chapter-scale architecture, or stalled frontier synthesis after the workflow itself has already been sharpened.
- No plan theater.
  If a plan exists, it must cash out into edits, checks, or a blocker.
- Tool persistence.
  The first plausible answer is not enough; stop only when the relevant falsifier passes or the blocker is real.
- Dependency-first execution.
  Read before editing. Verify prerequisites before downstream claims.
- Parallel evidence gathering.
  Batch independent greps, file reads, log checks, and targeted tests whenever they do not couple tightly.
- Skill-first specialization.
  If a task matches a repo skill, use the skill instead of reconstructing the workflow from scratch.
- `AGENTS.md`, `CLAUDE.md`, README files, and prior agent prose are operational guides, not mathematical evidence.

## Programme Identity (Crystallized 2026-04-12)

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0).

**The primitive object** is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12).** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output.

**The E_n operadic circle (2026-04-12):** E_3(bulk) -> E_2(boundary chiral) -> E_1(bar/QG) -> E_2(Drinfeld center) -> E_3(derived center). Each arrow: restriction to codim-2 defect, ordered bar complex, right adjoint to forgetful (Drinfeld center), higher Deligne (derived center). Closes for 3d HT with conformal vector; without conformal vector, stuck at SC^{ch,top}.

**SC^{ch,top} != E_3 (2026-04-12).** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires topologization: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3-TOPOLOGICAL (NOT E_3-chiral). Without conformal vector: stuck at SC^{ch,top}. thm:topologization PROVED for affine KM V_k(g) at non-critical level k != -h^v. General: CONJECTURAL (conj:topologization-general). Proof is cohomological; for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)<->(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input -> E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input -> E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input -> E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X -> chiral, R -> topological, CY category -> categorical.

**Architecture (2026-04-12):** E_n chiral algebra theory stays in Vol I (pure algebra/operads). ALL physics moves to Vol II. Vol III provides the geometric source (CY categories -> chiral algebras via the E_n circle).

**What we study:** Holomorphic chiral (factorisation) (co)homology via bar and cobar chain constructions at various different geometric locations, hence the different (modular) operads at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**North star:** platonic_ideal_reconstituted_2026_04_12.md is THE SINGLE REFERENCE for all structural questions.

## Claude-Codex Parity Rule

No durable Claude-side workflow is allowed to remain Claude-only.

Any always-on skill, hook, loop, routine, or metacognitive control surface that changes behavior must have a Codex-native home in one of:

- `AGENTS.md` for always-on rules;
- `.agents/skills/` for triggered workflows;
- `.codex/hooks/` for mechanical routing and guardrails.

If `CLAUDE.md` grows a durable behavior and Codex lacks an analogue, either:

1. add the Codex analogue in the same session; or
2. explicitly mark the parity gap and treat it as unresolved debt.

### Claude -> Codex parity map

| Claude Skill | Codex Skill | Trigger |
|-------------|-------------|---------|
| `/build` | `vol3-build-surface` | build, test, compile, verify |
| `/audit [target]` | `vol3-beilinson-loop` | audit, falsify, red-team, pressure-test |
| `/rectify [file]` | `vol3-beilinson-loop` | rectify, fortify, tighten, repair |
| `/chriss-ginzburg-rectify [file]` | `vol3-chriss-ginzburg-rectification` | chapter-scale structural rewrite, CG convergence |
| `/verify [claim]` | `vol3-pre-edit-verification` + `vol3-claim-verification` | verify formula, invariant, computational claim |
| `/propagate [pattern]` | `vol3-cross-volume-propagation` | AP5 sweep, cross-volume formula/status fix |
| `/compute-engine [name]` | `vol3-compute-engine` | new engine with multi-path tests |
| `/rectify-all` | `vol3-swarm-orchestration` | full-volume parallel rectification (user-authorized) |
| `/beilinson-swarm` | `vol3-swarm-orchestration` | parallel chapter rectification (user-authorized) |
| `/research-swarm [topic]` | `vol3-swarm-orchestration` | frontier synthesis, research architecture |

**Both `/rectify` and `/chriss-ginzburg-rectify` are available in BOTH Claude (via CLAUDE.md skill definitions) and Codex (via `.agents/skills/` skill files).** Use `vol3-beilinson-loop` for targeted chapter/proof repair; use `vol3-chriss-ginzburg-rectification` for chapter-scale structural rewriting with convergent loop.

Codex-specific delegation rule:

- swarm-style decomposition is permitted only when the user explicitly authorizes sub-agents or delegation;
- absent that authorization, use the same logical workflow locally without spawning agents.

## Session Entry Protocol

For any nontrivial task:

1. Lock the exact target.
   Name the file(s), labels, formulas, conventions, and whether the task is audit, rectification, verification, compute, or frontier work.
2. Read the live target before editing.
   Never patch by pattern alone.
3. Inspect the dirty surface.
   Read the current diff in the touched repo and, when cross-volume claims are involved, inspect the relevant diffs in Volumes I and II.
4. Lock the conventions.
   Check grading, shifts, OPE versus lambda-brackets, `E_1` versus `E_2`, CY dimension versus manifold dimension, and any `kappa` subscripts in play.
5. Name the claim state.
   Decide whether the surface is proved, proved elsewhere, conditional, conjectural, heuristic, or open.
6. Name the narrowest falsifier.
   Usually a targeted `pytest`, grep, local computation, proof trace, or `make fast`.
7. Only then edit.

## Pre-Edit Verification Protocol

This is the Codex analogue of the Claude-side pre-edit templates.

Use `vol3-pre-edit-verification` before editing any surface touching:

- `r`-matrices or OPE/lambda-bracket conversions;
- `kappa` formulas or modular characteristics;
- bar/cobar/Koszul-dual/desuspension formulas;
- d=3 theorem environments, status tags, or unconstructed objects;
- shadow class or SC-formality claims;
- `MF(W)` CY-dimension claims;
- cross-volume Part references;
- hardcoded compute or test oracles.

Protocol:

1. In commentary, write a fenced `PRE-EDIT` block before invoking the edit.
2. Fill in the exact object/formula, convention, source, boundary checks, and wrong variants avoided.
3. End with `verdict: ACCEPT` or `verdict: REJECT`.
4. If any required source is blank or any boundary check fails, do not edit yet.

This protocol is not decorative. Filling the block is part of verification.

## Live Truth Surface

The order of trust in this repo is:

1. direct computation and exact local verification;
2. the live `.tex` or `.py` source, read in context;
3. build logs, test output, and compiler failures;
4. primary literature with explicit convention conversion;
5. audit notes and self-contained verification notes;
6. `AGENTS.md` and the three `CLAUDE.md` files;
7. memory, summaries, prior chat conclusions.

For nontrivial work, the live surface is:

- the target file plus local neighboring context;
- `main.tex` and the active `\input` graph;
- the current dirty diff;
- relevant build logs;
- the narrowest relevant compute/tests slice;
- cross-volume duplicate or advertised claims in `~/chiral-bar-cobar` and `~/chiral-bar-cobar-vol2`.

If these surfaces disagree, investigate. Do not silently pick the most convenient layer.

## Current Empirical Risk Map (April 12, 2026)

This dated section is here because the user explicitly requested that the current failure distribution and dirty state be part of the steering surface. Refresh it when it goes stale.

### Last-100-commit archaeology

- Volume I is dominated by rectification, build-noise cleanup, formula/convention repair, compute/test synchronization, and repeated AP126/AP141, AP124/AP125, AP136, AP137, AP140, AP29, and AP128 failures. The SC^{ch,top} critical correction (AP165) and associated AP166-AP175 represent a major structural fix wave.
- Volume II is dominated by rectification, convention repair, cross-volume propagation, AP40 environment/status drift, AP44 divided-power drift, AP32 uniform-weight drift, V2-AP26/V2-AP30 stale Part references, V2-AP31 proof-after-conjecture, V2-AP32/V2-AP35 artifact/connective drift, and S_2=c/12 divided-power confusion corrections (AP177/FM30).
- Volume III is dominated by build noise, compute/test frontier corrections, AP113 `kappa`-subscript repair, AP-CY6/AP-CY11/AP-CY14 conditionality failures, AP-CY12 shadow-depth misclassification, AP-CY13 stale Part references, AP-CY17/AP-CY18/AP-CY19 geometric/computational convention drift, README/doc scope inflation, and pi_3(BU)/kappa_ch=h^{1,1}/McKay corrections (AP181-AP183).

### Current dirty hotspots

- Volume I currently has a large compute-and-test rectification wave plus extensive PDF/log noise. The live mathematical hotspots include:
  - Heisenberg versus odd-current versus genuine `E_1` distinction in `chapters/frame/heisenberg_frame.tex`;
  - PBW / Barr-Beck-Lurie proof strengthening and Koszul-dual degree bookkeeping in `chapters/theory/chiral_koszul_pairs.tex`;
  - Bershadsky-Polyakov central charge / `K_BP = 196` corrections in `compute/lib/non_principal_w_bar_engine.py` and its tests;
  - SC^{ch,top} structural correction: B(A) is E_1 coalgebra, NOT SC-coalgebra (AP165); SC is NOT self-dual (AP166);
  - `AGENTS.md` itself is dirty there, so treat Vol I control-surface text as live and evolving.
- Volume II currently has a focused but load-bearing dirty surface in `chapters/connections/thqg_perturbative_finiteness.tex`, where genus-2 stable graph classification is being corrected from an undercount to:
  - 7 total connected stable strata at `g = 2`, `n = 0` if the smooth no-edge stratum is included;
  - 6 edge-bearing Feynman graph types under the at-least-one-edge convention.
  This surface also adds genus-1 vertex contributions, so any citation to genus-2 graph counts or `F_2` graph formulas must be rechecked.
- Volume III currently has a compute/manuscript rectification cluster around:
  - `kappa_ch` versus `kappa_BKM` for `K3 x E`;
  - restoring the level prefix in CY `r`-matrices;
  - correcting local `P^2` from class `L` to class `M`;
  - pi_3(BU) = 0 correction in `chapters/theory/fukaya_categories.tex` (AP181);
  - kappa_ch = chi(S)/2 domain enforcement: local surfaces only, not conifold (AP182);
  - McKay quiver of C^3/Z_3 correction in `chapters/examples/toric_cy3_coha.tex` (AP183);
  - synchronized updates across `chapters/theory/introduction.tex`, `chapters/connections/cy_holographic_datum_master.tex`, `chapters/examples/toroidal_elliptic.tex`, `compute/lib/modular_cy_characteristic.py`, `compute/lib/swiss_cheese_cy3_e1.py`, and their tests.

Treat all of these as live audit surfaces, not settled facts.

## The Resonance Loop

For any nontrivial task, run this loop until `CONVERGED` or `BLOCKED`.

### 0. Scope Lock

Identify:

- the exact surface;
- the dependent labels, formulas, and conventions;
- whether the task is audit, rectification, verification, propagation, compute rectification, or frontier synthesis.

### 1. Invariant Lock

Before trusting any local argument, lock:

- grading and shifts;
- bar / cobar / Koszul-dual object identity;
- open / closed color directionality;
- OPE modes versus lambda-brackets with divided powers;
- genus / arity / filtration / family scope;
- Volume I versus II versus III conventions.

### 2. Read the Surface

Read the live target before editing anything. Never patch by pattern alone.

### 3. RED Pass

Attack logic and mathematics:

- hidden hypotheses;
- circularity;
- sign or degree errors;
- formula drift;
- overclaimed biconditionals;
- false identifications;
- proofs that silently assume the conclusion.

### 4. BLUE Pass

Attack consistency:

- theorem / proof / status mismatch;
- label drift;
- stale Part references;
- duplicated formulations;
- compute/manuscript disagreement;
- README or metadata advertising a stronger claim than the `.tex` supports;
- cross-volume inconsistencies.

### 5. GREEN Pass

Attack structural gaps:

- missing definitions;
- objects used before axiomatization;
- missing lemmas;
- dangling references;
- places where the true statement is weaker than the advertised one.

### 6. Patch in Dependency Order

Fix `CRITICAL` and `SERIOUS` findings first, then `MODERATE`.
For each fix:

1. re-read the local context;
2. recompute or re-derive independently;
3. make the smallest truthful edit;
4. immediately search for downstream advertisements of the old claim.

### 7. Propagate

After any mathematical change:

- grep Volume III;
- grep Volume II;
- grep Volume I;
- verify sameness of object and convention before editing a verbal match;
- update genuine duplicates in the same session or leave an explicit pending note.

### 8. Verify

Run the narrowest check that can actually falsify the change:

- targeted `pytest`;
- targeted grep or label check;
- proof trace;
- log inspection;
- `make fast` for load-bearing manuscript rewrites;
- broader build only when the local slice passes and scope demands it.

### 9. Re-Audit

Hostilely reread your own rewrite. Try to break it.

### 10. Convergence

- `CONVERGED`: no known actionable `MODERATE+` finding remains on the modified surface, and the narrowest relevant verification passes.
- `BLOCKED`: exact blocker named precisely.

Do not stop in between.

## Convergent Writing Loop

For introductions, prefaces, chapter openings, architectural rewrites, and other load-bearing prose:

1. write a first truthful draft;
2. reimagine the structure under hostile and compression-minded rereading;
3. rewrite from scratch rather than line-polishing a bad skeleton;
4. run a Beilinson audit on the rewritten surface;
5. repeat until no actionable `MODERATE+` finding remains.

Minimum standard:

- preface/introduction scale work: three or more iterations;
- chapter openings and major transitions: two or more iterations.

Structural moves worth preferring when they genuinely fit:

- deficiency opening;
- unique-survivor framing;
- instant computation;
- forced transition;
- decomposition table;
- true dichotomy;
- sentence-as-theorem compression.

## Operating Modes

### Mode 1 - Default Research Mode

Use for ordinary manuscript, notation, compute, and proof maintenance.

Loop:

1. identify the exact target;
2. read the local source;
3. inspect the nearby diff and dependencies;
4. make the smallest defensible correction;
5. run the narrowest falsifier;
6. propagate shared formula/status changes;
7. stop only when the surface is coherent.

### Mode 2 - Deep Beilinson Audit

Trigger when asked to audit, review, red-team, challenge, falsify, or pressure-test a theorem, chapter, formula family, or region.

Audit the live surface:

- `main.tex`;
- current `\input` graph;
- dirty diff;
- relevant logs;
- narrow compute/tests slice.

Mandatory passes:

- `RED`: logic, formulas, signs, hypotheses, scope, hidden conditionality;
- `BLUE`: collisions across intro/chapter/examples/appendices/compute/tests/README/other volumes;
- `GREEN`: missing definitions, dangling references, absent lemmas, frontier gaps, overstated claims.

Findings are mathematical bugs, not editorial trivia.

### Mode 3 - Beilinson Rectification Loop

Trigger when asked to fix, rectify, converge, tighten, or repair a mathematical surface.

Rectification loop:

1. identify claims and dependencies;
2. classify findings by severity and order;
3. fix `CRITICAL` and `SERIOUS` first;
4. after each fix, rerun the narrowest falsifier;
5. re-audit the modified surface;
6. repeat until no actionable `MODERATE+` finding remains.

### Mode 4 - Multi-Path Claim Verification

Trigger when asked whether a formula, invariant, theorem statement, example, or comparison is correct.

Minimum standard:

- at least three genuinely independent verification paths for any load-bearing numerical or computational claim;
- at least two independent paths for test oracles when three are not practical.

Allowed path families:

1. direct computation;
2. structurally different equivalent formula;
3. limiting or degenerate case;
4. symmetry or duality;
5. cross-family consistency;
6. literature comparison with convention check;
7. degree / weight / sign / units analysis;
8. numerical evaluation;
9. operadic or factorization consistency;
10. descent to a classical/PVA/shadow.

Mandatory Vol III overlays when relevant:

- `AP-CY1`: CY dimension is not real dimension;
- `AP-CY2`: CY trace lives in negative cyclic, not merely Hochschild;
- `AP-CY5`: quantum-group claims must specify the `q` regime;
- `AP-CY6` / `AP-CY11` / `AP-CY14`: CY-A_3 now PROVED (inf-cat); CY-C conditionality still propagates;
- `AP-CY7`: CoHA is not automatically an `E_1`-chiral algebra;
- `AP-CY8`: denominator identity is not automatically a bar Euler product;
- `AP-CY12`: shadow class comes from the full tower, not a leading approximation;
- `AP49`: cross-volume convention conversion.

### Mode 5 - Cross-Volume Propagation Sweep

Trigger whenever you change a:

- formula;
- theorem status;
- definition;
- notation;
- convention;
- summary sentence advertising a result;
- claim touching `kappa`, `Theta`, bar/cobar, CoHA, `E_1`/`E_2`, Borcherds products, quantum groups, centers, or shadow towers.

Propagation protocol:

1. grep Volume III;
2. grep Volume II;
3. grep Volume I;
4. verify sameness of object and convention before editing;
5. update all genuine duplicates or explicitly mark what remains pending and why.

Never paste formulas between volumes without explicit convention conversion.

### Mode 6 - Compute Rectification Mode

Trigger whenever a `.py` engine, test oracle, table value, hardcoded coefficient, or numerical claim is edited.

Rules:

- Every new or changed hardcoded value must record source and normalization.
- Engine and test must not derive from the same mental model.
- Prefer exact arithmetic when the claim is exact.
- When a formula changes, audit neighboring comments, docstrings, and tests for stale reasoning.
- If a compute result is important enough for the prose, it is important enough for an independent executable check.
- Build artifacts are never evidence.

This mode exists to prevent AP10, AP38, AP80, AP122, AP123, AP128, AP140, and the recurring "engine and test agree on the same wrong number" failure.

### Mode 7 - Frontier Research Mode

Trigger for new theorems, new definitions, new constructions, and CY3 frontier architecture.

Frontier rule set:

1. define the object before naming the programme around it;
2. test toy models before general prose;
3. search for counterexamples early;
4. separate construction, evidence, conditional result, conjecture, heuristic, and slogan explicitly;
5. never upgrade a frontier claim to theorem status in the same pass that first drafts its proof;
6. default new Vol III formal frontier statements to `conjecture` unless the proof is complete and unconditional.

This mode exists to prevent AP36, AP40, AP42, AP43, AP-CY6, AP-CY11, and AP-CY14.

## Claim-State Governance

Every serious statement must belong to exactly one of:

- `\ClaimStatusProvedHere`
- `\ClaimStatusProvedElsewhere`
- `\ClaimStatusConditional`
- `\ClaimStatusConjectured`
- `\ClaimStatusHeuristic`
- `\ClaimStatusOpen`

Rules:

- status is part of the mathematics, not decoration;
- theorem/proposition/lemma/corollary environments are for proof-bearing or genuinely cited results only;
- conjectural or heuristic material does not belong in theorem-like environments;
- if the proof chain passes through an unconstructed d=3 object, the result is at least `Conditional`, and often `Conjectured`;
- if the proof proves less than the sentence claims, weaken the sentence;
- do not strengthen both statement and status in the same unchecked pass;
- when status changes, update the environment, label prefix, surrounding prose, downstream advertisements, and any compute/docs surface selling the claim.

## Definition-First and Object Discipline

Before using a central object in a theorem, ensure the manuscript already contains a formal definition with hypotheses and ambient category.

This is non-negotiable for:

- `G(X)` or any "quantum vertex chiral group";
- any `A_X` or `A_{K3 x E}` at `d = 3`;
- any `C(g,q)` or quantum-group object whose existence is part of the programme;
- any center construction where "center" might mean Drinfeld center, derived center, or factorization object;
- any "bulk algebra" language that could mean different constructions;
- any claim that sells CoHA as if it were already the chiral object itself.

Never conflate:

- `A` (algebra);
- `B(A)` (bar coalgebra);
- `A^i = H^*(B(A))` (dual coalgebra);
- `A^! = (A^i)^vee` (dual algebra);
- `Z^{der}_{ch}(A)` (derived/chiral center = bulk);
- `Z(Rep^{E_1}(A))` (Drinfeld center of a monoidal category).

## Volume III Invariant Lock

### E_1 / E_2 hierarchy

- `E_1`-chiral algebras: associative factorization on `C x R`; representation categories are monoidal.
- `E_2`-chiral algebras: braided factorization on `C x C`; representation categories are braided monoidal.
- `E_2` is braided, not symmetric in general.
- `E_1 -> E_2` via Dunn additivity is structural, not automatic at the level of every candidate example.
- The Drinfeld center is not the same object as the derived/chiral center unless explicit hypotheses are stated.

### Kappa discipline

Bare `kappa` is forbidden in Volume III unless the local section explicitly binds it to one approved invariant.

Approved subscripts:

- `kappa_ch`: chiral modular characteristic;
- `kappa_cat`: categorical / Euler-like invariant when precisely defined;
- `kappa_BKM`: Borcherds-Kac-Moody / automorphic-weight invariant;
- `kappa_fiber`: fiber/lattice invariant when precisely defined.

Immediate sanity rule:

- `K3 x E` has multiple `kappa`-type numbers.
- Current active rectification distinguishes `kappa_ch(K3 x E) = 3` from `kappa_BKM(K3 x E) = 5`.
- Never write `kappa(K3 x E) = 5` unqualified.
- If `kappa_cat` or `kappa_fiber` enter, re-check the live source instead of inheriting a remembered value.

### Load-bearing d=3 boundaries

- `CY-A` is unconditional only for `d = 2`.
- Any d=3 theorem depending on chain-level `S^3` framing, chart gluing, or unconstructed `A_X` is not `ProvedHere`.
- CoHA is associative and may be evidence for an `E_1` sector, but it is not identical to the `E_1`-chiral algebra.
- Local `P^2` must be classified from the full shadow tower, not a leading Lie-type approximation.
- `MF(W)` has CY dimension `n - 2` for `W: A^n -> A^1`, not `n - 1`.

## Canonical Checks

Verify against these before trusting a sentence or test:

```text
kappa(H_k) = k
kappa(Vir_c) = c/2
kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)
kappa(W_N) = c*(H_N - 1),  H_N = sum_{j=1}^N 1/j

r^KM(z) = k*Omega/z
r^Heis(z) = k/z
r^Vir(z) = (c/2)/z^3 + 2T/z

c_bc(lambda) = 1 - 3(2*lambda-1)^2
c_bg(lambda) = 2*(6*lambda^2 - 6*lambda + 1)
c_bc + c_bg = 0

B(A) = T^c(s^{-1} A-bar),   A-bar = ker(epsilon)
|s^{-1}v| = |v| - 1
d_bar^2 = 0
MC: d*Theta + (1/2)[Theta,Theta] = 0
QME: hbar*Delta*S + (1/2){S,S} = 0
F_1 = kappa/24
F_2 = 7*kappa/5760
eta(tau) = q^(1/24) * prod_{n>=1}(1-q^n)
Cauchy normalization = 1/(2*pi*i)

K_BP = 196
genus-2 stable graph count:
  7 total connected stable strata at g=2, n=0
  6 edge-bearing Feynman types under the at-least-one-edge convention

kappa_ch(K3 x E) = 3
kappa_BKM(K3 x E) = 5
local P^2 = class M, not class L

# Homotopy / topology (AP181-AP185)
pi_3(BU) = 0                  # Bott: pi_odd(BU) = 0; confusion with pi_3(U) = Z
pi_4(BU) = Z                  # obstruction GROUP, not automatic E_2 structure
kappa_ch = chi(S)/2            # for local surfaces Tot(K_S -> S) ONLY
McKay(C^3/Z_n) = n copies of oriented n-cycle, NOT K_{n,n}

# SC / operadic (AP165-AP172)
B(A) is E_1 coalgebra          # NOT SC-coalgebra; SC on derived center pair
SC^! = (Lie, Ass, shuffle)     # NOT self-dual; closed dim = (n-1)! vs 1
A^! is SC^!-algebra = (Lie,Ass) # NOT SC-algebra
"arity" BANNED                 # AP176 CONSTITUTIONAL; use "degree" everywhere
```

## Forbidden Forms

Grep and fix immediately if any of these appear in the relevant convention:

```text
Omega/z                               # bare level-stripped r-matrix
(c/2)/z^4                             # Virasoro quartic r-matrix term
c*H_{N-1}                             # wrong W_N harmonic-number form
T^c(s^{-1} A)                         # bar complex forgot augmentation ideal
|s^{-1}v| = |v|+1                     # desuspension wrong direction
eta(tau) = prod(1-q^n)                # missing q^(1/24)
K_BP = 2                              # wrong Bershadsky-Polyakov conductor
kappa(K3 x E) = 5                     # unqualified Vol III kappa
local P^2: class L                    # AP-CY12 misclassification
MF(W) is CY_{n-1}                     # wrong matrix-factorization dimension
Part~IV / Chapter~12 hardcoded refs   # stale architecture references waiting to happen
"B(A) is SC coalgebra"                # FALSE: E_1 coalgebra; SC in derived center pair (AP165)
(SC^{ch,top})^! ~ SC^{ch,top}        # FALSE: SC^!=(Lie,Ass,shuffle); not self-dual (AP166)
"E_3-chiral"                          # FALSE: E_3-TOPOLOGICAL when conformal vector present (AP168)
"arity" anywhere in manuscript        # BANNED: use "degree" universally (AP176 CONSTITUTIONAL)

# Homotopy / topology (B69-B73)
pi_3(BU) = Z                          # WRONG: pi_3(BU) = 0 (Bott: pi_odd(BU) = 0) (B69)
kappa_ch = h^{1,1}                    # WRONG when h^{0,2}!=0; use kappa_ch = chi(S)/2 for local surfaces (B70)
McKay(Z_3) = K_{3,3}                  # WRONG: 3 copies of oriented 3-cycle, not bipartite (B71)
"excision gives B(A) tensor B(A)"     # WRONG: excision gives B_L tensor_A B_R (one copy, over A) (B72)
"pi_4(BU)=Z provides E_2"            # WRONG direction: obstruction group, not guarantee (B73)
```

## Cross-Volume Anti-Pattern Import

All of the following are in force here:

- the shared Vol I anti-pattern system `AP1` through `AP185` in `~/chiral-bar-cobar/CLAUDE.md`;
- the Vol II system `V2-AP1` through `V2-AP39` in `~/chiral-bar-cobar-vol2/CLAUDE.md`;
- the Vol III system `AP-CY1` through `AP-CY19` in `CLAUDE.md`;
- the workflow anti-patterns `AAP1` through `AAP18`.

### Critical APs added since April 10 (AP150-AP185 highlights)

**AP150: Resolution propagation failure.** When a conjecture is proved, disproved, or retracted, ALL references must be updated atomically: concordance, preface, introduction, standalones, CLAUDE.md status table, label prefixes, other volumes.

**AP165: B(A) is NOT an SC^{ch,top}-coalgebra.** The bar complex is an E_1 chiral coassociative coalgebra (differential + deconcatenation). It is a SINGLE E_1 coalgebra, not a two-colored SC datum. The SC^{ch,top} structure emerges in the chiral derived center pair (C^bullet_{ch}(A,A), A). FORBIDDEN: "B(A) is a coalgebra over SC^{ch,top}"; "the bar differential is the closed color"; "the bar coproduct is the open color."

**AP166: SC^{ch,top} is NOT Koszul self-dual.** SC^! = (Lie^c, Ass^c, shuffle-mixed) with closed dim = (n-1)!. SC = (Com, Ass) with closed dim = 1. The duality FUNCTOR is involutive ((P^!)^! ~ P); the OPERAD is not self-dual (P^! != P). FORBIDDEN: "(SC^{ch,top})^! ~ SC^{ch,top}."

**AP172: A^! is an SC^!-algebra** = (Lie, Ass)-algebra (closed = Sklyanin bracket, open = Yangian product). NOT an SC-algebra.

**AP176: CONSTITUTIONAL -- "arity" is BANNED.** "Degree" is the universal term for all index-counting contexts. NEVER reintroduce "arity." Grep check: `grep -rn '\barity\b' chapters/ appendices/ standalone/` must return ZERO hits.

**AP181: pi_3(BU) = 0, not Z.** By Bott periodicity, pi_k(BU) = Z for k even, 0 for k odd. The confusion: pi_3(U) = Z (loop space), but pi_3(BU) = pi_2(U) = 0. Vol III fukaya_categories.tex had this error at lines 209, 396, 413. The correct reason CY_3 gives E_1 (not E_2) is the antisymmetric Euler form structural obstruction, NOT a topological obstruction.

**AP182: kappa_ch = chi(S)/2 only for local surfaces.** The formula applies to Tot(K_S -> S). The conifold Tot(O(-1)^2 -> P^1) is NOT a local surface (K_{P^1} = O(-2) != O(-1)^2). Also kappa_ch != h^{1,1} when h^{0,2} != 0 (K3: h^{1,1}=20 but chi/2=12).

**AP183: McKay quiver != K_{3,3}.** The McKay quiver of C^3/Z_3 is 3 copies of the oriented 3-cycle, NOT the complete bipartite graph K_{3,3}. K_{3,3} is undirected bipartite; McKay quivers are directed.

**AP184: Excision vs coproduct.** Excision: cutting [0,1] at t gives B(A) = B_L tensor_A B_R (one copy, tensor OVER A). Coproduct: Delta: B(A) -> B(A) tensor B(A) (two copies, plain tensor). These are different categorical levels. Never conflate.

**AP185: Obstruction group vs enabler.** pi_4(BU) = Z is the GROUP WHERE THE OBSTRUCTION LIVES, not a guarantee that E_2 exists. Nonzero homotopy group = potential obstruction, not automatic structure.

### Trigger map

If editing status, theorem environments, or proof blocks, check:

- `AP40`, `AP4`, `AP125`, `AP124`, `V2-AP31`, `AP-CY11`, `AP-CY14`.

If editing `kappa`, modular characteristics, or automorphic weights, check:

- `AP1`, `AP39`, `AP48`, `AP113`, `AP-CY2`, `AP-CY10`, `AP-CY15`.

If editing `r`-matrices, OPEs, or lambda-brackets, check:

- `AP19`, `AP44`, `V2-AP34`, `AP117`, `AP126`, `AP141`.

If editing bar/cobar/Koszul-dual/bulk material, check:

- `AP14`, `AP25`, `AP34`, `AP50`, `AP132`, `AP165`, `AP166`, `AP172`, `AP184`.

If editing shadow depth, class, or SC-formality claims, check:

- `AP14`, `AP131`, `AP-CY12`.

If editing chapter migration, Part references, or duplicated statements, check:

- `AP5`, `AP12`, `AP49`, `AP124`, `AP127`, `V2-AP26`, `V2-AP27`, `V2-AP30`, `AP-CY13`.

If editing compute engines or tests, check:

- `AP10`, `AP38`, `AP80`, `AP122`, `AP123`, `AP128`, `AP140`.

If editing prose, notes, README, or metadata, check:

- `AP29`, `AP121`, `V2-AP29`, `V2-AP32`, `AP115`, `AP-CY15`, `AAP8`, `AP176`.

If editing homotopy groups, CY dimension, framing, or obstruction claims, check:

- `AP181`, `AP182`, `AP183`, `AP185`, `AP-CY6`, `AP-CY11`, `AP-CY14`.

## Context and Memory Hygiene

For substantial tasks:

- keep a short explicit plan or self-contained audit note;
- after each major phase, restate the target, current status, open risks, and next falsification step;
- anchor conclusions to exact file paths, theorem labels, and test names;
- prefer durable notes under `compute/audit/` or `notes/audit_*.md` for major audits;
- write notes so a newcomer with only the current working tree can continue without hidden chat context;
- do not let summaries harden into truth without rereading the source.

## Beilinson Gate - Post-Edit Mental Hook

After editing any `.tex` or `.py` file, explicitly check:

- did the edit change truth conditions or only presentation;
- is the claim status still honest;
- does the surrounding environment match the status macro;
- did a definition become load-bearing, and if so, is it present;
- did a shared formula require propagation;
- did a cross-volume convention bridge require conversion;
- does the compute layer still support the formula;
- are there hidden CY3 existence assumptions;
- did any proof silently assume the conclusion;
- did the dirty-diff hotspot nearby require a fresh reread rather than a local patch.

For `.tex`, re-check at least:

- `AP40` environment/status mismatch;
- `AP113` unqualified `kappa`;
- `AP165` B(A) not attributed SC structure;
- `AP166` SC not claimed self-dual;
- `AP176` no "arity" anywhere;
- `AP181` pi_3(BU) = 0, not Z;
- `AP182` kappa_ch = chi(S)/2 only for local surfaces;
- `AP-CY6` / `AP-CY11` / `AP-CY14` d=3 existence and conditionality;
- `AP-CY12` shadow depth from incomplete evidence;
- `AP-CY13` stale Part references;
- `AP-CY15` README or summary overclaim if the text advertises the result elsewhere;
- `V2-AP26` / `V2-AP35` stale structural references or broken connectives.

For `.py`, re-check:

- hardcoded expected values versus independent verification;
- source and normalization conventions in literals and docstrings;
- exact arithmetic versus floating approximation where exactness is claimed;
- engine/test independence;
- `AP113` subscripted invariants;
- `AP140` family-specific conductors and duality constants;
- whether adjacent tests, comments, or README surfaces still describe the old result.

## Convergence Gate - Stop-Time Mental Hook

If the session is an audit or rectification session, do not stop until you can honestly say one of:

- `CONVERGED`: modified surface is coherent and verified.
- `BLOCKED`: exact blocker named.

Do not end with a vague half-fix.

## Pre-Commit Gate

Before any commit:

1. run the narrowest build/test verification matching the change;
2. inspect the diff for build artifacts, logs, PDFs, and accidental noise;
3. grep touched surfaces for the highest-risk anti-patterns that match the change;
4. if `RECTIFICATION-FLAG` entered the diff, resolve it or record a precise tracked follow-up before committing;
5. ensure there is no AI attribution in commit message or metadata;
6. ensure all commits remain authored by Raeez Lorgat only.

## Verification Commands

Use the narrowest relevant slice first.

Volume III build:

```bash
pkill -9 -f pdflatex 2>/dev/null || true
sleep 2
make fast
```

When cross-volume propagation is involved:

```bash
cd ~/chiral-bar-cobar && make fast
cd ~/chiral-bar-cobar-vol2 && make
```

For compute work:

- run targeted `pytest` first;
- expand to a broader suite only if the local slice passes and the scope warrants it.

## Repo-Local Skills and Hooks

This repo may include Codex-native skills under `.agents/skills/` and hook configuration under `.codex/`.

Use:

- `vol3-beilinson-loop` for hostile audit and rectification;
- `vol3-chriss-ginzburg-rectification` for chapter-scale structural fortification;
- `vol3-claim-verification` for formula, theorem, and comparison checks;
- `vol3-cross-volume-propagation` for AP5/AP49-style sweeps.
- `vol3-build-surface` for build/test/log triage and stable verification surfaces;
- `vol3-frontier-research` for new theorem architecture, conjectural synthesis, and truthful frontier packaging;
- `vol3-compute-engine` for executable witnesses, engine scaffolding, and test-surface design;
- `vol3-pre-edit-verification` for mandatory pre-edit check blocks on high-risk surfaces;
- `vol3-swarm-orchestration` for Codex analogues of Claude swarm routines when the user explicitly authorizes delegation.

Current high-value hook surfaces include:

- `session_start_context.py` for startup context loading;
- `user_prompt_router.py` for skill routing and rectification-mode hints;
- `pre_tool_use_policy.py` for destructive-command and pre-commit guardrails;
- `post_tool_use_review.py` for build/test failure blocking;
- `stop_continue.py` for convergence enforcement.

Architectural rule:

- keep this file compressive and always-on;
- move repeated deep workflows into skills;
- move deterministic enforcement into hooks or grep-based checks;
- do not bloat the constitutional layer with playbook detail that belongs elsewhere.

## Failure Modes from 2026-04-14 CG Rectification Campaign

**FM42. Bulk substring replacement corruption.** replace_all "arity"→"degree" silently corrupts singularity→singuldegree, complementarity→complementdegree, unitarity→unitdegree, regularity→reguldegree, modularity→moduldegree, parity→pdegree. 45 corruptions introduced and fixed in one session. COUNTER: never bulk-replace short substrings appearing inside common words. After any bulk replace, grep for `ldegree|ndegree|rdegree|pdegree|tdegree`. Compound word checklist: {singularity, complementarity, unitarity, regularity, modularity, parity, familiarity, similarity, polarity, disparity, linearity}.

**FM43. E_n output scope of Φ.** Φ: CY_d-Cat → E_2-ChirAlg is WRONG at d≥3 (output is E_1). Found in 5 Vol III files. Always scope: `(n=2 for d≤2; n=1 for d≥3)`.

**FM44. Agent rate limiting.** >10 concurrent agents → mass rate limiting (27/31 failed in one campaign). Batch in groups of 3.

**FM45. Agent skill fidelity gap.** Subagents get compressed briefs, not the full 15K-word /chriss-ginzburg-rectify skill. Good for bulk scanning (AP176, AP113, em-dashes); insufficient for deep 5-gate reconstitution. For full-quality rectification, invoke the skill directly per file.

**FM46. Stale line counts.** Preface/introduction chapter assessments list line counts that drift as chapters grow (8 counts off by up to 3x). Update after content campaigns.

## Final Meta-Rule

The dominant failure mode of this programme is not lack of sophistication. It is confusing two objects, two conventions, two statuses, or two levels of validity that happen to look similar in a special case.

So before trusting any sentence, name all five:

- the object;
- the convention;
- the status;
- the verification path;
- the scope.

If you cannot name all five, the sentence is not ready.
