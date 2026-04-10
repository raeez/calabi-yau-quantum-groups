# CLAUDE.md -- Volume III: CY Categories, Quantum Groups, and BPS Algebras

**Canonical reference for all shared content: ~/chiral-bar-cobar/CLAUDE.md. This file contains ONLY Vol III-specific material.**

## Identity

Volume III constructs the geometric source: the functor Phi: CY_d-Cat -> E_2-ChirAlg providing input data for the Vols I-II bar-cobar machine. Flow: CY category -> chiral algebra -> bar complex -> modular characteristic -> partition function.

~206pp, this repo, 17,199 tests. Five parts: I(CY Engine) II(CY Characteristic Datum) III(CY Landscape) IV(Seven Faces of r_CY(z)) V(CY Frontier).

**5 genuine stub chapters** (<50 lines, AP114): quantum_groups_foundations (24), derived_categories_cy (27), geometric_langlands (28), matrix_factorizations (29), modular_koszul_bridge (13). Develop or comment out. **3 thin chapters** (50-100 lines, may need development): cyclic_ainf (55), cy_categories (70), e1_chiral_algebras (90). **5 formerly listed stubs now developed** (>300 lines): hochschild_calculus, braided_factorization, drinfeld_center, fukaya_categories, quantum_group_reps.

## Main Theorems

| Theorem | Status | Notes |
|---------|--------|-------|
| **CY-A** (CY-to-chiral functor) | d=2 PROVED; d=3 PROGRAMME | d=3 conditional on chain-level S^3-framing |
| **CY-B** (E_2-chiral Koszul duality) | PROGRAMME | Depends on CY-A |
| **CY-C** (Quantum group realization) | CONJECTURAL | C(g,q) not constructed. Uses \begin{conjecture}. NEVER \begin{theorem} |
| **CY-D** (Modular CY characteristic) | PROGRAMME | kappa well-defined only when A_C exists |

## The kappa-Spectrum (AP113, CRITICAL)

Bare "kappa" is FORBIDDEN in Vol III. A CY manifold gives rise to MULTIPLE chiral algebraizations, each with its own kappa. ALWAYS subscript:

| Subscript | Meaning | K3 x E value |
|-----------|---------|--------------|
| kappa_ch | From chiral algebra A_C via Phi | 3 |
| kappa_BKM | From Borcherds-Kac-Moody algebra | 5 (weight of Delta_5) |
| kappa_cat | From categorical/holomorphic Euler char | 2 = chi(O_{K3}) |
| kappa_fiber | From lattice/fiber structure | 24 (lattice rank) |

kappa(K3 x E) = 3 vs 5 contradiction arose from conflating kappa_ch and kappa_BKM. Full spectrum: {2,3,5,24}.

## HOT ZONE -- Top 10 Vol III Repeat Offenders

Read this section BEFORE any Edit. These are the AP-CY patterns that fire repeatedly across waves despite being catalogued. Each entry is an operational template, not prose. If you only read 80 lines of Vol III CLAUDE.md, read these.

### HZ3-1. AP-CY6/AP-CY14 (unconstructed A_X in theorem environment)

Decision tree, answer BEFORE writing `\begin{theorem}`:

```
Q1: Does the proof chain pass through A_X for d=3, G(X), C(g,q), or any
    object whose existence is part of the d=3 programme?
    YES -> \begin{conjecture} + \ClaimStatusConjectured. STOP. NEVER theorem.
    NO  -> Q2
Q2: Does it pass through A_X for d=2 (CY-A proved)?
    YES -> \begin{theorem} or \begin{proposition} OK; cite CY-A explicitly.
    NO  -> Q3
Q3: Pure categorical / VOA / Yangian statement (no functor invocation)?
    YES -> \begin{theorem} or \begin{proposition} OK; classical proof.
UNCERTAIN -> default \begin{conjecture}. Downgrade is cheaper than retract.
```

Vol III default: `\begin{conjecture}` regardless. The 11+ instances fixed across 4 commits prove that the LLM pattern-matches on "if X then Y" logical form without checking whether X exists.

### HZ3-2. AP113 (bare kappa)

ZERO TOLERANCE in Vol III. Before writing ANY `\kappa`:

```
(i)  Subscript present?  Required: {ch, cat, BKM, fiber}
(ii) Forbidden subscripts: {global, BPS, eff, total, naive, MacMahon}
     If you wrote BPS, you mean BKM. Rename now.
(iii) Meta-naming "kappa-spectrum" / "kappa-value":
     write \kappa_\bullet to satisfy the grep regex (the bullet denotes
     the indexing variable across the approved set).
```

Decision tree:
- chiral algebra A_C / Phi(C) -> `\kappa_{\mathrm{ch}}`
- Borcherds-Kac-Moody / Igusa weight -> `\kappa_{\mathrm{BKM}}`
- Holomorphic Euler char chi(O_X) -> `\kappa_{\mathrm{cat}}`
- Lattice rank / fiber structure -> `\kappa_{\mathrm{fiber}}`

### HZ3-3. AP-CY11 (conditional propagation)

If a result depends on Conjecture X which depends on CY-A_3, the result IS conditional on CY-A_3. Use `\ClaimStatusConditional` and state the dependency chain. Pattern caught at Tier 2: `cor:kappa-from-charts` was `ProvedHere` despite chaining through `conj:e1-chart-gluing -> CY-A_3`. Fixed in cy_to_chiral.tex L1127.

Template before `\ClaimStatusProvedHere`:

```
Q: Does this result's proof chain reach back to CY-A_3 or any unconstructed object?
   NO  -> ProvedHere OK
   YES -> ClaimStatusConditional + name the chain in the body
```

### HZ3-4. AP-CY7 (CoHA vs E_1-chiral)

The Cohomological Hall Algebra is associative, NOT a chiral algebra. The slogan "the E_1-sector of G(X)" assumes G(X) exists (AP43). Forbidden conflations:

```
"CoHA = E_1-chiral algebra"  WRONG
"E_1-sector of G(X)"          assumes G(X), AP43 violation
"CoHA carries a vertex algebra structure"  WRONG (it carries a Hall product)
```

CoHA is the Hochschild cohomology of the quiver-with-potential category, with the Schiffmann-Vasserot-Yang-Zhao multiplication. The connection to chiral algebras is via the FUNCTOR Phi (CY-A), not by identification.

### HZ3-5. AP-CY3/AP-CY4 (E_2, Drinfeld center, derived center)

Three distinct objects:

```
1. E_2-monoidal category C  =  little 2-disks structure (NOT symmetric).
2. Drinfeld center Z(C)     =  monoidal-category center via half-braidings.
3. Derived center Z^der_ch(A) =  Hochschild cochains, the bulk algebra.
```

NEVER conflate. Drinfeld center Z(Rep^{E_1}(A)) is a category-theoretic operation; derived center Z^der_ch(A) is the bulk operator algebra. The relationship: Drinfeld center IS the categorification of derived center (modular envelope).

### HZ3-6. AP-CY8 (Borcherds denominator vs bar Euler product)

For K3 x E, the identification `Phi_10 = bar Euler product` is an OBSERVATION, not a theorem. It is conditional on:
- CY-A_2 (which IS proved at d=2)
- The Vol I Borcherds-lift identification of bar Euler products

Template: any sentence asserting equality between automorphic forms and bar Euler products MUST cite both CY-A and the Vol I anchor explicitly. Bare "the bar Euler product equals Phi_10" is forbidden.

### HZ3-7. AP-CY17 (MF(W) CY dimension)

For W: A^n -> A^1, the matrix factorization category MF(W) is CY of dimension `n-2`, NOT `n-1`. Mnemonic: ADE in 2 variables gives CY_0 (semisimple). Need 4 variables for CY_2. Need 5 variables for CY_3 (Fermat quintic).

Verification template before any MF(W) CY claim:

```
W: A^n -> A^1, n = ?
MF(W) is CY_{n-2}; check n-2 against the desired CY dimension.
n=2: CY_0 (ADE Lie algebras)
n=3: CY_1
n=4: CY_2 (compact K3 surfaces from quartic)
n=5: CY_3 (compact threefolds from quintic)
```

### HZ3-8. AP-CY10 (flop vs Koszul dual)

Birational flop X -> X^+ is a derived equivalence; it PRESERVES kappa_ch. Koszul dual A -> A^! has `kappa(A) + kappa(A^!) = K` (family-dependent conductor). Forbidden conflations:

```
"flop is the Koszul dual"          WRONG
"kappa(A_X) + kappa(A_{X^+}) = 0"  WRONG (flops preserve kappa)
"kappa(A_X) = kappa(A_{X^+})"      RIGHT (flop is autoequivalence)
```

Flop exchanges chambers in the Mukai motion; Koszul exchanges algebra/coalgebra. Different operations entirely.

### HZ3-9. AP-CY12 (shadow class from full tower)

The G/L/C/M classification of a CY chiral algebra MUST be computed from the full shadow tower, NOT from generator counting or non-formality alone. Template:

```
"X has m_3 != 0"  ->  necessary condition for class >= L; not sufficient.
"shadow tower terminates at depth 2"  ->  class L (verified by computation).
"m_n != 0 for all n"  ->  class M (full tower computation required).
"local P^2 has 3 generators"  ->  inadequate for class. Compute the tower.
```

local P^2 IS class M (infinite depth), not class L. Wrong classification was caught in compute/audit/cy_shadow_class_audit.

### HZ3-10. AP-CY13/V2-AP26 (cross-volume Part references)

NEVER hardcode `Part~IV`, `Chapter~12` in Vol III prose. Always use `\ref{part:...}`. Before any cross-volume reference:

```
(i)  Use \ref{part:foo}, never Part~N
(ii) After ANY restructuring, grep ALL THREE volumes for stale Part refs:
     grep -rn 'Part~[IVXL]' chapters/ appendices/ standalone/
(iii) Verify every match resolves to a current part label
```

Vol III's Tier 2 dnp_identification_master.tex Vol II edit caught a stale Part~II reference (Tier 2 Task E4); the canonical Vol I Parts list is in main.tex L822-1400.

## E_1/E_2 Chiral Hierarchy

E_1-chiral (Vol II): associative factorization on C x R. Monoidal rep categories. E_2-chiral (this vol): braided factorization on C x C. Braided monoidal rep categories: habitat of quantum groups. E_1 -> E_2 via Dunn additivity. d=2: S^2-framing of HH_*(C) gives E_2. d=3: holomorphic CS breaks E_2 to E_1; recover E_2 via Drinfeld center Z(Rep^{E_1}(A)) = Rep^{E_2}(Z^der_ch(A)). Drinfeld center is categorified av: E_1-Cat -> E_2-Cat. Quantum groups, Yangians, braided tensor categories natively E_1. E_2 derived.

## CY-Specific Anti-Patterns (AP-CY1 through AP-CY8)

AP-CY1: CY dimension d != complex dimension n. Fuk(X) is CY_n, D^b(Coh(X)) is CY_n. Not real dim 2n.
AP-CY2: CY trace is in HC^-_d(C), NOT just HH_d -> k. Negative cyclic refinement essential for S^d-framing.
AP-CY3: E_2 != commutative. E_2 braiding is NOT symmetric. E_2 -> E_inf loses quantum group structure.
AP-CY4: Drinfeld center Z(C) (monoidal category) != derived center Z^der_ch(A) (chiral). State which.
AP-CY5: Kazhdan-Lusztig requires root of unity. Generic q: Rep_q(g) semisimple.
AP-CY6: A_X for CY3 does NOT exist. It IS the d=3 programme. NEVER write as if defined. **Strengthened**: any result whose proof chain passes through A_X at d=3 MUST carry \ClaimStatusConditional and explicitly name CY-A_3 as dependency. Conditionality PROPAGATES through all downstream results.
AP-CY7: CoHA != E_1-chiral algebra. CoHA is associative. "E_1-sector of G(X)" assumes G(X) exists (AP43).
AP-CY8: Borcherds denominator != bar Euler product. Identification requires CY-to-chiral functor. For K3 x E: observation, not theorem.

### Empirical (AP-CY9-13, from 50-commit error archaeology)
AP-CY9: Jacobi form discriminant constraint. For phi_{k,m} of index m, only discriminants D with D=0 or D=3 mod 4 (m=1) can appear. NEVER fill coefficient table with sequential D-values. Verify discriminant constraint. c(-1)=2 for phi_{0,1} in EZ convention, NOT 1.
AP-CY10: Flop != Koszul dual. Birational flop X->X^+ is derived equivalence PRESERVING kappa. Koszul dual A^! has kappa(A)+kappa(A^!)=rho_K. Flop exchanges chambers; Koszul exchanges algebra/coalgebra. kappa(A_X)=kappa(A_{X+}) for flop, NOT kappa(A_X)+kappa(A_{X+})=0.
AP-CY11: Conditional d=3 transitivity. If Result B depends on Result A which depends on CY-A_3, then B is ALSO conditional on CY-A_3. Use \ClaimStatusConditional and state the dependency chain. DEFAULT environment for new Vol III formal statements is \begin{conjecture} unless proof is COMPLETE and UNCONDITIONAL.
AP-CY12: Shadow class from full computation. G/L/C/M must be determined by computing full shadow tower, NOT by counting generators. Non-formality (m_3!=0) does NOT by itself determine shadow depth. local P^2 is class M (infinite depth), not class L.
AP-CY13: Cross-volume Part number staleness. After ANY Part restructuring in ANY volume, grep ALL THREE volumes for stale Part references. Part numbers are the most fragile cross-reference. Use \ref{part:...} exclusively, never hardcode. **Strengthened**: run grep -rn 'Part~[IVXL]' chapters/ notes/ and verify EVERY match. 7+ stale refs survived a single restructuring.

### Deep Empirical (AP-CY14-19, from 100-commit deep archaeology)
AP-CY14: Unconstructed object inhabits theorem environment. ANY statement whose proof chain passes through G(X) at d=3, A_{K3xE}, or any unconstructed object MUST use \begin{conjecture}, NEVER \begin{theorem}/\begin{proposition}. The LLM pattern-matches on logical structure ("if X then Y") without checking whether X exists. 11+ instances fixed across 4 commits. DEFAULT in Vol III is \begin{conjecture}.
AP-CY15: README scope inflation beyond .tex ground truth. README must not claim "verified" or "proved" for structural analogies or pattern matches. The README accumulates stronger claims than the .tex supports because the LLM optimizes for impressiveness. After README edits, verify every "proved"/"verified" against corresponding \ClaimStatus tag.
AP-CY16: Matrix size conflation in group quotients. Sp_4 quotient by +/-I_4 (4x4), NOT +/-I_5. O(Lambda^{3,2}) quotient by +/-I_5 (5x5). When two groups of different rank appear in the same formula, the LLM harmonizes subscripts to whichever appears more frequently.
AP-CY17: MF(W) CY dimension is n-2, NOT n-1. For W: A^n -> A^1, MF(W) is CY_{n-2} (Dyckerhoff). ADE in 2 variables: CY_0 (semisimple). Need 4 variables for CY_2. The n-1 vs n-2 error changes which families are CY_2.
AP-CY18: Lattice theta series comparison. Verify q-power divergence by DIRECT COMPUTATION. Leech theta: minimum norm^2=4, first correction at q^2 not q^1. The match with 1/eta^24 extends through q^1. Never conflate j(tau) coefficients with V_Lambda character coefficients.
AP-CY19: A-hat genus argument halving. A-hat(x) = (x/2)/sinh(x/2). Convergence radius = 2*pi (first pole of sin(x/2) at x=2*pi). NEVER drop the /2 in the argument, which gives spurious radius pi. Appeared in 3+ independent computations.

## Dependencies on Vols I-II

| Volume | Provides | Used here |
|--------|----------|-----------|
| I | Bar-cobar machine, Theta_A, kappa, five theorems, G/L/C/M | CY bar complex, modular trace, shadow depth |
| II | SC^{ch,top}, PVA descent, DK bridge, E_1 sector, H(T) | E_1 chiral theory, braided structure, bulk-boundary |

## Build

```
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast    # Vol III
cd ~/chiral-bar-cobar && make fast                                # Vol I
cd ~/chiral-bar-cobar-vol2 && make                                # Vol II
make test                                                         # Vol III tests
```

## Session Entry (Vol III additions)

1. Read ~/chiral-bar-cobar/CLAUDE.md first (canonical).
2. Then this file (kappa-spectrum, AP-CY1-8).
3. Check AP113: bare kappa -> subscripted kappa_{ch,BKM,cat,fiber}.
4. Check AP114: do not cite theorems from 12 stub chapters.
5. CY-A: d=2 PROVED, d=3 PROGRAMME. Scope EVERY CY-A claim by dimension.
6. CY-C is CONJECTURE. NEVER \begin{theorem} for CY-C (AP40).

## Git

All commits authored by Raeez Lorgat. NEVER credit an LLM. git stash FORBIDDEN.
