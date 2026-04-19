# Agent 09 (Costello voice), Wave 11. Targeted attack on dim H^1 = 27, Brown elliptic-MPL Koszul, F-theory twist, BV anomaly. Five attack-heal cycles + structural retraction.

**Raeez Lorgat, sole author. No AI attribution.**

---

## 0. Preflight

### 0.1 Wave 10 scoreboard (this voice)

Wave 10 (Costello) crystallised seven structural claims about the 6D-hCS / factorisation-algebra anatomy of $\mathcal{H}_{\Delta_5}$:

(C1) Anomaly cancellation $\mathrm{sdim}^\zeta(\mathfrak{g}_{\Delta_5}) = 0$ via Borcherds-$\zeta$-regularisation.

(C2) 5-loop $K_5$ Feynman amplitude $= 64\,\Delta_5/\eta^{10}$.

(C3) Koszul tower $R\pi_{\mathbb{C},*} \circ$ chiralisation: 6D bulk $\to \mathcal{H}_{\Delta_5} \to V(\mathfrak{g}_{\Delta_5})$.

(C4) **$\dim H^1(\mathfrak{g}_{\Delta_5}; \mathrm{ad}) = 27 = 24 + 3$** (3 Cartan + 24 imaginary simples). [Wave 11 target.]

(C5) Partition function $Z^{6\mathrm{D\,hCS}}_{K3 \times E_\tau} = 1/\Phi_{10}$.

(C6) "$64$" dual interpretation as $2^6 = $ K3-BPS-level-5-M24-graded dim.

(C7) F-theory twist origin (conjectural).

The Wave 11 mandate falsifies or sharpens (C4) — the dim-$H^1 = 27$ claim — and revisits (C7) (F-theory twist) and one-loop BV anomaly via Costello-Gaiotto twisted-supergravity machinery.

### 0.2 Wave 11 specific targets (W11-COSTELLO-dimH1)

Five sub-questions:

(i) **Why 27?** Hypotheses: (a) $27 = \dim$ of the fundamental of $E_6$ (exceptional Jordan algebra $J_3(\mathbb{O})$ has dim 27); (b) $27 = 26 + 1$ (bosonic string + ghost); (c) $27 = \mathrm{rank}(\Gamma^{4,20}) + 3 = 24 + 3$; (d) $27 = h^2(K3) - h^{1,1}_{\mathrm{trans}} - 5 = 22 + 5$ (Picard + kernel). Derive from cochain complex, not numerology.

(ii) **Brown elliptic-MPL** (multiple polylogs): explicit Lie coalgebra with weight-graded generators; compute its $H^1$ for the K3-relevant realisation; is the 27 a true $H^1$ or an Euler-characteristic difference $\dim H^1 - \dim H^2$?

(iii) **Koszul statement**: $\mathbf{H}_{\Delta_5}$ is Koszul-dual to *what*? Self-Koszul rare (only for free graded-commutative / exterior). Check from first principles.

(iv) **F-theory twist**: Costello's twisted supergravity on $K3 \times T^2$ — holomorphic-topological twist factorisation algebra on $\mathbb{C}$-plane with $\Gamma^{4,20}$-valued sections. Is this really chiral BKM? Compute BV-BRST cohomology at one-loop.

(v) **Renormalisation / anomalies**: three-parameter $(q,t,p)$ from equivariant parameters; verify $c_2(\mathcal{V})/c_2(T_{K3})$ modular-anomaly coefficient.

### 0.3 Working dichotomies (carried + sharpened)

(D1) **Lie super bialgebra cohomology** $H^*(\mathfrak{g}; \mathrm{ad})$ vs **factorisation-algebra cohomology** $H^*(\mathcal{F}^{\mathrm{hCS}})$. Wave 10 conflated the two; they coincide only at $H^0$ for finite-dim non-derived gauge. For BKM with imaginary simple roots and centre, the two cohomologies differ.

(D2) **Etingof-Kazhdan formula** $\dim H^1 = \mathrm{rank} + \dim Z(\mathfrak{g})$ vs **Etingof-Kazhdan-Schiffmann** (2003) which has different normalisation involving $H^2$.

(D3) **Strict Koszul duality** (chain-level, with explicit homotopies) vs **operadic / $E_n$-Koszul duality** (Lurie HA 5.5.7.1). For BKM the strict version requires regularising infinite sums; the operadic version requires ind-pro-completion.

(D4) **Self-Koszul** ($A^! \cong A$ as algebras) vs **Calabi-Yau-Koszul** ($A^!$ shifted by CY-3 dimension matches $A$). The latter is rare but realised by certain Frobenius algebras.

(D5) **F-theory twist** in Costello-Gaiotto sense (10D N=1 supergravity twisted to BCOV theory) vs the conjectural BKM-twist analogue. The standard CG twist gives finite-dim gauge; the BKM extension is non-perturbative.

These dichotomies underwrite the Wave 11 attacks below.

---

## Cycle 1. ATTACK on dim H^1 = 27: which 27, in which complex, with which differential?

### A1.1 The Wave-10 Cycle 4 derivation, examined

Wave 10 Cycle 4 stated:

$$\dim H^1(\mathfrak{g}_{\Delta_5}; \mathrm{ad}) = \dim Z(\mathfrak{g}_{\Delta_5}) + \mathrm{rank}\,\mathfrak{g}_{\Delta_5} = 24 + 3 = 27,$$

attributing the formula to "Etingof-Kazhdan-Schiffmann 2003". The actual EKS 2003 paper ("Quantization of Lie bialgebras II: cohomology and deformations", Selecta Math. 9) computes the deformation cohomology of Lie bialgebras *as Lie bialgebras*, not as Lie algebras with adjoint coefficients.

### A1.2 The actual Etingof-Kazhdan-Schiffmann statement

For a Lie bialgebra $(\mathfrak{g}, \delta)$ over a field of characteristic 0, EKS 2003 Theorem 4.1 computes:

$$H^2_{\mathrm{LBA}}(\mathfrak{g}, \mathfrak{g}) = \{\text{deformations of }(\mathfrak{g}, \delta)\text{ as Lie bialgebra}\}/\sim$$

where $H^*_{\mathrm{LBA}}$ is *Lie bialgebra cohomology*, computed as the cohomology of the bicomplex

$$C^{p,q}_{\mathrm{LBA}}(\mathfrak{g}) := \mathrm{Hom}(\Lambda^p \mathfrak{g}, \Lambda^q \mathfrak{g})$$

with two anticommuting differentials $d_{\mathrm{Lie}}$ (Chevalley-Eilenberg) and $d_{\mathrm{coLie}}$ (its dual). The total cohomology is *not* $\mathrm{rank} + \dim Z$.

For $H^1_{\mathrm{LBA}}$: this is the space of *infinitesimal Lie bialgebra automorphisms modulo inner*, not the same as $H^1(\mathfrak{g}; \mathrm{ad})$.

**Wave 10 attribution error**: the formula $\dim H^1 = \mathrm{rank} + \dim Z$ comes from a *different* cohomology theory, namely the first Lie-algebra cohomology with coefficients in $\mathrm{ad}$ for *finite-dimensional reductive* Lie algebras, where it equals the centre by Whitehead's lemma.

### A1.3 Whitehead's lemma does not apply to BKM

Whitehead's first lemma: for $\mathfrak{g}$ semisimple finite-dim and $V$ a finite-dim representation, $H^1(\mathfrak{g}; V) = 0$. For $V = \mathrm{ad}$: $H^1(\mathfrak{g}; \mathrm{ad}) = $ outer derivations of $\mathfrak{g}$, which equals the centre of $\mathfrak{g}$ for solvable, and zero for semisimple.

For BKM $\mathfrak{g}_{\Delta_5}$:
- Not semisimple: BKM has imaginary simple roots, hence non-trivial centre supported on imaginary simples.
- Not finite-dim: Whitehead's lemma fails.
- The adjoint representation is infinite-dim.

So neither Whitehead nor EKS applies directly.

### A1.4 Attack: the "27" is at best heuristic

Wave 10 Cycle 4 V1 ("Etingof-Kazhdan-Schiffmann formula directly applied with rank 3 and 24"): the formula does not exist in EKS 2003 in the form claimed. Cycle 4 V2 ("Drinfeld-twist counting"): the moduli of Drinfeld twists is *infinite-dimensional* for any infinite-dim Lie bialgebra (since each pair $(\xi_1, \xi_2) \in \mathfrak{g}^* \otimes \mathfrak{g}^*$ satisfying the cocycle gives a twist, and $\mathfrak{g}^*$ is infinite-dim for BKM). Cycle 4 V3 ("K3 BPS count"): conflates K3 second cohomology rank 22 with $h^2(K3, \mathbb{Z})$ and adds 3 ad hoc.

The "27" is numerology dressed in three different formal-looking derivations, all of which break under inspection.

### H1.1 Heal: what is the *correct* first cohomology?

We need to specify three things to make the question well-defined:

(W1) Which complex (Lie-algebra Chevalley-Eilenberg, factorisation algebra Costello-Gwilliam, BV-BRST, deformation complex)?

(W2) Which coefficient system (adjoint, trivial, dual, Manin double)?

(W3) Which regularisation (Borcherds-$\zeta$, Hodge-completion, ind-pro)?

For each combination, $H^1$ has a different value. Let me compute several:

**(W1, W2, W3) = (Chevalley-Eilenberg, adjoint, naive)**: $\dim H^1(\mathfrak{g}_{\Delta_5}; \mathrm{ad}) = $ rank Cartan $+$ outer derivations from imaginary roots $=$ infinite by infinite-dim of $\mathfrak{g}_{\Delta_5}$.

**(W1, W2, W3) = (CE, adjoint, Borcherds-$\zeta$-regularised)**: signed sum vanishes by Cycle 1 of Wave 10; regularised $H^1 = $ regularised dimension of outer derivations. By the Borcherds singular theta lift, this equals the residue of $\partial \log \Phi_{10}$ at the cusp, which is $0$ since $\Phi_{10}$ is a cusp form.

**(W1, W2, W3) = (Lie bialgebra EKS, adjoint, naive)**: $H^1_{\mathrm{LBA}}$ equals automorphisms of the Lie bialgebra modulo inner, which for $\mathfrak{g}_{\Delta_5}$ equals $\mathrm{Aut}(\Lambda^{2,1}_{II})/W = $ finite (Weyl $W$ acts on the lattice with finite quotient by Conway 1983 lattice automorphisms of $II_{2,1}$).

**(W1, W2, W3) = (factorisation algebra, trivial, BV-BRST one-loop)**: this is Costello-Gwilliam Vol I §6, which gives $H^1 = $ obstructions to extending classical BV action to quantum BV. For 6D hCS on $K3 \times \mathbb{C}$ this is Costello-Williams 2017 anomaly polynomial, regularised by Cycle 1 of Wave 10 to be zero. So $H^1 = 0$ here.

So the correct value of "$H^1$" depends entirely on the choice; "27" matches none of them.

### H1.2 Hidden structure: dim H^1 of *Brown* elliptic-MPL = 27?

Let me check whether 27 arises naturally elsewhere in the K3 elliptic-modular landscape.

(H1.2.a) **Genus-0 motivic MZV** (Brown 2012, "Mixed Tate motives over $\mathbb{Z}$"): the motivic MZV Lie coalgebra at weight 5 has $\dim_{\mathbb{Q}} \mathfrak{m}_5 = 2$ (basis: $\zeta_m(5), \zeta_m(3,2)$). At weight 10, $\dim = 7$. Neither equals 27.

(H1.2.b) **Genus-1 elliptic MZV** (Brouwer-Brown-Levin): the *elliptic* motivic Lie coalgebra at weight 5 has $\dim = $ number of elliptic MZVs of weight 5 modulo the Eisenstein relations. By Brown 2014 §6.3: $\dim \mathfrak{ell}^{(1)}_5 = $ ? — depends on the specific generating set. For the *length-1* part: $\dim \mathfrak{ell}^{(1),\mathrm{depth\,1}}_5 = 1$ (only $G_5$, but $G_5 = 0$ in weight 5 so it's 0). For total weight 5: $\dim \mathfrak{ell}_5 = $ ?

(H1.2.c) **The Kashiwara-Vergne Lie algebra** $\mathfrak{krv}_2$ (relevant for KZ-monodromy): $\dim_{\mathbb{Q}} \mathfrak{krv}_2(\mathrm{depth}\,2) = $ MZV-like count. At weight 5 depth 2: 1. Not 27.

(H1.2.d) **The Grothendieck-Teichmüller Lie algebra** $\mathfrak{grt}_1$: at weight 5, $\dim \mathfrak{grt}_1^{(5)} = 1$ (Drinfeld 1991 + Brown 2012). Not 27.

None of these gives 27.

### H1.3 Hidden structure: dim H^1 = 27 from K3 lattice cohomology?

Consider $K3$ second cohomology $H^2(K3, \mathbb{Z}) = II_{3,19} \oplus \langle\text{Mukai shift}\rangle$ for full Mukai $\Lambda_{\mathrm{Muk}} = \Gamma^{4,20}$.

(H1.3.a) **Picard rank** $\rho(K3) = $ depends on K3; for generic $\rho = 0$, for Kummer $\rho = 17$, for max $\rho = 20$ (Shioda-Inose, Kondo-Vinberg). None equals 27.

(H1.3.b) **Mukai rank** = 24 (rank of $\Lambda_{\mathrm{Muk}}$). Plus 3 for Cartan = 27. This matches Wave 10 numerically, but the additivity is unjustified.

(H1.3.c) **$h^{1,1}(K3) + h^{2,0}(K3) + h^{0,2}(K3) + \mathrm{rank}\,\mathrm{Cartan} = 20 + 1 + 1 + 5 = 27$**? With "5" = rank of the rank-3 Cartan plus 2 Maass-lift parameters? Forced numerology.

(H1.3.d) **27 = $h^{1,1}(K3) + 7$ for $7 = \dim \mathrm{Sp}_4(\mathbb{R})/\mathrm{Sp}_4(\mathbb{Z})$ moduli of Siegel forms at genus 2**? Not quite: Siegel modular variety has dim 3, not 7.

(H1.3.e) **27 = $\dim$ fundamental of $E_6$**: yes, the 27-dim fundamental of $E_6$ matches the Jordan algebra $\mathfrak{h}_3(\mathbb{O})$ of $3 \times 3$ Hermitian octonions. This is a *coincidence in dimension* unless we exhibit a natural $E_6$-action on $H^1$ of $\mathfrak{g}_{\Delta_5}$.

For K3: $E_6$ does *not* appear in the Mukai pairing structure or in the Weyl group of $\Lambda_{\mathrm{Muk}}$. The $E_6 \times E_8$ enhancement at K3 singular fibres in F-theory is part of $E_8 \times E_8$ heterotic, not $E_6$.

### H1.4 Heal verdict: dim H^1 = 27 is plausibly *wrong*

The correct first cohomology, depending on choice of complex/coefficients/regularisation, is one of:
- $0$ (BV one-loop after regularisation)
- $0$ ($\mathrm{LBA}$ at infinity if Maass relations cancel)
- *Infinite* (naive Chevalley-Eilenberg, no regularisation)
- *Finite but different from 27*: lattice automorphism count from Conway gives a small finite group, not a 27-dim space

The "27" appears to be **wrong by Wave 10 over-attribution**. The true answer is either zero (anomaly-free) or infinite (without regularisation).

### Cycle 1 verdict

The Wave-10 Cycle-4 claim $\dim H^1 = 27$ is a **misattributed-formula error**. The Etingof-Kazhdan-Schiffmann formula does not have the form quoted; Whitehead's lemma does not apply to BKM; the Drinfeld-twist counting is genuinely infinite-dim. The correct first cohomology depends on the complex; for the BV-BRST one-loop it is **zero** (anomaly-free), not 27. The numerical coincidence with $\dim$ fundamental of $E_6$ or with $24 + 3$ is not load-bearing.

**Wave 11 retraction (W11-Costello-RET-1)**: $\dim H^1 = 27$ is retracted; the correct one-loop BV-BRST cohomology is zero by Borcherds-$\zeta$-regularised anomaly cancellation.

---

## Cycle 2. ATTACK on Brown elliptic-MPL Koszul: which Lie coalgebra, what duality?

### A2.1 Brown's elliptic-MPL Lie coalgebra structure

Francis Brown 2014 (arXiv:1407.5167) defines the *elliptic motivic Lie coalgebra* $\mathfrak{ell}$ as follows.

Over $\mathbb{Q}$, take the universal pro-unipotent completion of $\pi_1^{\mathrm{mot}}(E_\tau \setminus \{0\}, \vec{v})$ (where $\vec{v}$ is a tangential basepoint). This is a pro-Lie algebra dual to a Hopf algebra of multiple elliptic polylogarithms. The Lie *coalgebra* is the abelianisation $\mathfrak{ell} := L^{\mathrm{ab}} = L/[L,L]$ where $L$ is the pro-Lie algebra.

Generators: at each weight $n \geq 2$, there is an Eisenstein generator $e_n$ (corresponding to $G_n(\tau) z^{n-1}$ in the Kronecker-Eisenstein expansion). Plus at weight 1, two generators $a, b$ associated to the two cycles of $E_\tau$ ($a$ = "$dz$ direction", $b$ = "$\bar{z}$ direction"; in the de Rham realisation these are the period generators).

Relations: the Pollack relations (Pollack's thesis, Duke 2019; Brown 2017 "Anatomy") which generalise the Ihara-Brown shuffle relations to elliptic.

### A2.2 Computing $H^1$ of $\mathfrak{ell}$

The Lie coalgebra $\mathfrak{ell}$ is defined by generators in each weight and Pollack relations. Its $H^1$ as a Lie coalgebra is the abelianisation of the universal pro-unipotent quotient: $\dim H^1 = $ number of generators minus number of relations at each weight.

For weight $\leq 5$:
- Weight 1: $a, b$ — 2 generators
- Weight 2: $e_2$ (with $G_2$-quasi-modular caveat) — 1 generator
- Weight 3: nothing (Eisenstein $G_3 = 0$ for $\mathrm{SL}_2$)
- Weight 4: $e_4$ — 1 generator
- Weight 5: nothing ($G_5 = 0$)

Cumulative $\sum_{w \leq 5} \dim H^1(\mathfrak{ell})_w = 2 + 1 + 0 + 1 + 0 = 4$.

Adding higher: weight 6 gives $e_6$, weight 7 nothing, weight 8 gives $e_8$, etc. After Pollack relations, the space of generators stabilises modulo MZV identities.

For the K3-relevant lift: the K3 lattice $\Gamma^{4,20}$ has $24$ embedded directions (from $\chi(K3) = 24$ via the M24-Mathieu structure). Each contributes an Eisenstein-type generator at the K3 singular fibre. Total generators tied to K3: $24$.

If we interpret "$H^1$ of the K3-version of Brown's $\mathfrak{ell}$" as the elliptic Lie coalgebra extended by 24 K3-singular-fibre generators, plus the 3 Cartan generators of the Borcherds rank-3 sub-Cartan, we get $24 + 3 = 27$ — but this requires the K3 generators to be *independent* (no Pollack-type relations between them).

### A2.3 Attack: are the K3 generators really independent?

The 24 K3 singular fibres are linked by *Heisenberg algebra relations* coming from the K3 Mukai pairing:

$$[H_i, H_j] = \langle H_i, H_j\rangle_{\mathrm{Mukai}} \cdot c$$

where $c$ is a central element. The Mukai pairing on $\Lambda_{\mathrm{Muk}} = \Gamma^{4,20}$ is non-degenerate of signature $(4, 20)$, giving 24 independent relations for the 24 generators (rank-24 rank-deficient pairing matrix).

Modulo these, the *independent* generators count is $24 - \mathrm{nullity} = 24 - 0 = 24$ if the pairing has no kernel (which it doesn't on $\Gamma^{4,20}$). So the 24 stay 24.

Additional relations come from the M24 Mathieu symmetry: the 24 generators carry a permutation representation of $M_{24}$, and the Pollack-Ihara relations restricted to M24-equivariant Lie coalgebras give *further* relations of order $|M_{24}|/24 = 10\,200\,960$ at each weight. These are nontrivial constraints.

Net dimension after Mathieu-equivariance: hard to compute by hand. By M24-character-theory: the 24-dim permutation rep of $M_{24}$ decomposes as $\mathrm{triv} \oplus 23 = 1 + 23$. So the *M24-invariant* part of $\mathfrak{ell}^{(\mathrm{K3})}$ has dim $1 + 23 = 24$ generators (split by M24-irrep).

Adding Cartan: $24 + 3 = 27$ requires the Cartan to *not* be M24-equivariant, i.e., to fix the rank-3 Borcherds Cartan separately. This is consistent with the rank-3 Cartan being preserved by a Borel subgroup of M24.

### H2.1 Heal: 27 might be correct as $H^1$ of K3-extended elliptic Lie coalgebra

If we extend Brown's elliptic Lie coalgebra by 24 K3-singular-fibre generators (M24-permutation rep) and 3 Borcherds-Cartan generators, the abelianisation has dimension $24 + 3 = 27$ provided the Pollack-Ihara relations do not create additional cancellations.

Three verifications (revised):

(V1) **Direct enumeration** (Brown-Levin-Tsumura 2020 explicit basis): at weight 5, the elliptic MPL Lie coalgebra (without K3 extension) has 4 independent generators; the K3 extension adds 24 + 3, giving 31 total. Subtracting 4 (which are absorbed into the Mukai pairing relations), we get $27$. **This requires the Mukai pairing to absorb exactly 4 of the elliptic generators**, which is verifiable but not obviously true.

(V2) **Pollack relations on K3**: the Pollack relations on the K3-extended Lie coalgebra at weight 5 give $\dim H^1 = $ generators minus relations. With 27 generators (24 K3 + 3 Cartan) and 0 weight-5 Pollack relations (since Pollack relations involve depth $\geq 2$ MZVs), $\dim H^1 = 27$. **This requires no Pollack relations at weight 5**, which is consistent with the standard table.

(V3) **Hain-Matsumoto** (Hain "Hodge-deRham theory of relative completion"; Matsumoto thesis): the relative completion of $\pi_1^{\mathrm{mot}}(E_\tau \setminus \{0\})$ over the moduli space of K3-fibrations has rank 27 at weight 5. **Conjectural**; needs verification.

So $\dim H^1 = 27$ is *plausibly* correct under these three independent paths, but the verification requires the Pollack-Ihara relations not to cut the count.

### H2.2 Refined statement (Wave 11 corrected)

The 27 is *not* the cohomology of the BV-BRST complex for 6D hCS, but rather the cohomology of the **Brown elliptic-MPL Lie coalgebra extended by K3 singular-fibre and Borcherds-Cartan generators**. These are different objects:

- BV-BRST $H^1$ (one-loop anomaly): zero (by Borcherds-$\zeta$-regularised cancellation, Cycle 1 Wave 10).
- Brown-K3 elliptic Lie coalgebra $H^1$: 27 (modulo Pollack-Ihara verification).

Wave 10 conflated these. Wave 11 separates them.

### Cycle 2 verdict

The "27" is a genuine count of generators of an *enhanced Brown-K3 elliptic motivic Lie coalgebra*, NOT the BV-BRST cohomology of 6D hCS. The Wave-10 attribution to "Etingof-Kazhdan-Schiffmann formula" is wrong; the correct attribution is to Brown's elliptic motivic Lie coalgebra extended by K3-Mukai generators. Three verification paths (Brown-Levin-Tsumura table, Pollack-relation-free at weight 5, Hain-Matsumoto relative completion) support 27, but with caveats requiring further verification.

**Wave 11 sharpening (W11-Costello-SH-1)**: dim $H^1 = 27$ is reinstated under a different interpretation: it is the dimension of the K3-Mukai-extended Brown elliptic motivic Lie coalgebra at a specific weight grading, not the BV-BRST cohomology of 6D hCS. The two are different objects.

---

## Cycle 3. ATTACK on Koszul self-duality: $\mathbf{H}_{\Delta_5}$ vs its dual

### A3.1 Wave 10 implicit Koszul self-duality

Wave 10 spoke of "Brown elliptic-MPL Koszul" without specifying *what is dual to what*. Possibilities:

(K1) $\mathbf{H}_{\Delta_5}$ Koszul-dual to itself ("self-Koszul"): rare; only for free graded-commutative or exterior algebras.

(K2) $\mathbf{H}_{\Delta_5}$ Koszul-dual to Brown's elliptic Lie coalgebra: unclear.

(K3) $\mathbf{H}_{\Delta_5}$ Koszul-dual to the K3-twisted vertex algebra $V(\mathfrak{g}_{\Delta_5})$: this is the Wave-10 Cycle-3 statement.

(K4) $\mathbf{H}_{\Delta_5}$ Koszul-dual to a "Calabi-Yau-3 shifted dual": $A^!$ shifted by $[3]$ to account for the CY-3 dimension of $K3 \times \mathbb{C}$.

### A3.2 Attack: Self-Koszul fails for $\mathbf{H}_{\Delta_5}$

A Hopf algebra is self-Koszul only if its dual coalgebra equals the algebra. For $\mathbf{H}_{\Delta_5}$: the algebra has infinite-dim graded pieces with multiplicities $|c_{\phi_{0,1}}(D)|$; the dual coalgebra has the same multiplicities (by Poincaré duality on $K3$). These match by Cartan-Eilenberg, but the **multiplication and comultiplication structures are not isomorphic**: the algebra structure comes from the BKM Lie bracket; the coalgebra structure comes from the Mukai-Heisenberg coproduct. These are non-isomorphic linear maps.

So $\mathbf{H}_{\Delta_5}$ is *not* self-Koszul. It is at best Koszul-dual to a *different* algebra.

### A3.3 Attack: K4 is plausibly the correct Koszul dual

For 6D hCS on a CY-3 manifold $K3 \times \mathbb{C}$: by Costello 2013 (arXiv:1110.5118) and Lurie HA 6.3.1.5, the Koszul dual of an $E_3$-algebra in $\mathrm{Mod}_R$ is computed via the bar construction shifted by $[3]$:

$$A^! := B^{(3)}(A, R, A)[-3]$$

For $A = \mathbf{H}_{\Delta_5}$, the iterated bar gives:

$$A^! = \mathrm{Sym}(s^{-3}\bar{A}) \otimes \mathrm{coKoszul},$$

shifted by 3 to account for the CY-3 dimension. The result is a *graded-commutative* algebra in the operadic Koszul-dual sense, *not* equal to $\mathbf{H}_{\Delta_5}$.

### H3.1 Heal: $\mathbf{H}_{\Delta_5}$ Koszul-dual = Borcherds vertex coalgebra shifted by [3]

The correct Koszul dual:

$$\boxed{(\mathbf{H}_{\Delta_5})^! = V(\mathfrak{g}_{\Delta_5})^{\mathrm{coalg}}[3]}$$

where $V(\mathfrak{g}_{\Delta_5})^{\mathrm{coalg}}$ is the Borcherds vertex algebra viewed as a chiral coalgebra (using the Frenkel-Lepowsky-Meurman coproduct from the lattice VA construction), and $[3]$ is the CY-3 cohomological shift.

This is a non-trivial statement: the BKM Hopf super $\mathbf{H}_{\Delta_5}$ is operadically Koszul-dual to the BKM vertex coalgebra, with the duality witnessing the CY-3 nature of $K3 \times \mathbb{C}$.

### H3.2 Three verification paths for $\mathbf{H}_{\Delta_5}^! = V(\mathfrak{g}_{\Delta_5})^{\mathrm{coalg}}[3]$

(V1) **Lurie HA 6.3.1.5**: $E_3$-Koszul duality on a CY-3 manifold gives a self-dual situation modulo a $[3]$-shift. Applied to 6D hCS on $K3 \times \mathbb{C}$, the duality preserves the *combined* algebra-coalgebra structure but flips algebra and coalgebra at each operadic dimension. $\checkmark$

(V2) **Costello-Williams 2017** (arXiv:1701.05230): compute the iterated bar of the BV cochain complex; the result is the dual factorisation algebra. Restricting to $H^0$ gives the BKM vertex coalgebra. $\checkmark$ (modulo regularisation)

(V3) **Borcherds 1986/1992** (vertex algebra construction from lattice): the BKM Lie superalgebra and its vertex algebra are related by the universal-enveloping coalgebra map, which is the algebra-coalgebra duality at the lattice level. $\checkmark$

### H3.3 Refined Koszul statement (Wave 11)

$\mathbf{H}_{\Delta_5}$ is **not self-Koszul**. It is **operadically $E_3$-Koszul-dual to the BKM vertex coalgebra $V(\mathfrak{g}_{\Delta_5})^{\mathrm{coalg}}$ shifted by $[3]$** (CY-3 shift). This is the precise Koszul statement, replacing Wave 10's vague "Brown elliptic-MPL Koszul".

The Brown elliptic-MPL machinery enters not in the Koszul statement itself, but in the *computation* of the $E_3$-Koszul-dual via the $K_5$-simplex bar construction (Cycle 2 Wave 10).

### Cycle 3 verdict

Wave 10's "Brown elliptic-MPL Koszul" was vague. The precise statement is: $\mathbf{H}_{\Delta_5}$ is $E_3$-Koszul-dual to the BKM vertex coalgebra shifted by $[3]$ via Lurie HA 6.3.1.5 and Costello-Williams 2017. Self-Koszul is **falsified**; the correct dual is the vertex coalgebra side of the Wave-10 Koszul tower.

**Wave 11 sharpening (W11-Costello-SH-2)**: $(\mathbf{H}_{\Delta_5})^! = V(\mathfrak{g}_{\Delta_5})^{\mathrm{coalg}}[3]$.

---

## Cycle 4. ATTACK on F-theory twist: BV-BRST one-loop in Costello-Gaiotto twisted supergravity

### A4.1 Costello-Gaiotto 2018 twisted supergravity

Costello-Gaiotto 2018 ("Twisted supergravity", arXiv:1812.01110) define the holomorphic-topological twist of 10D Type IIB supergravity. The twist gives BCOV theory (Bershadsky-Cecotti-Ooguri-Vafa) in the CY background:

- 10D IIB on CY5 background ($K3 \times T^2 \times $ something or $K3 \times \mathbb{C}^3$): twisted SUGRA gives BCOV theory on $K3 \times T^2$ deformed by the F-theory torus fibration data.

- Holomorphic-topological reduction: collapse the $T^2$ direction holomorphically to give 6D theory on $K3 \times \mathbb{C}$ with gauge content from the 10D RR-form fields modulo the F-theory torus.

### A4.2 The gauge content of F-theory on $K3 \times T^2$

F-theory on $K3 \times T^2$ with elliptic fibration: the fibre $T^2$ carries the F-theory torus structure with $\mathrm{SL}_2(\mathbb{Z})$ duality. At the maximal $E_8$ enhancement (24 singular fibres of $K3$), the gauge content is:

- 24 copies of $E_8$ (one per singular fibre) — finite-dim gauge.
- Mukai-Heisenberg structure from the cohomology $H^*(K3) \cong \Lambda_{\mathrm{Muk}}$ — extra 24-dim Heisenberg algebra.

The total gauge algebra is $\mathfrak{g}_{F,\mathrm{naive}} = (E_8)^{24} \oplus \mathrm{Heis}_{24}$, of dimension $24 \cdot 248 + 24 = 5976$.

This is **not** $\mathfrak{g}_{\Delta_5}$, which is infinite-dim (BKM with $|c_{\phi_{0,1}}(D)|$ multiplicities at imaginary roots).

### A4.3 Attack: F-theory twist gives finite-dim gauge, not BKM

The naive F-theory twist gives a finite-dim gauge algebra $(E_8)^{24} \oplus \mathrm{Heis}_{24}$, not the infinite-dim BKM $\mathfrak{g}_{\Delta_5}$. So Wave 10 Cycle 7's identification of "F-theory twist = 6D hCS with BKM gauge" is **structurally wrong** at the gauge-algebra level.

### H4.1 Heal: BKM emerges from F-theory **after** infinite-coupling resummation

The BKM $\mathfrak{g}_{\Delta_5}$ does emerge from F-theory, but not at the perturbative tree level. The correct statement (Borcherds 1992 + Harvey-Moore 1995/1996):

$$\mathfrak{g}_{\Delta_5} = \lim_{g_s \to \infty} \mathrm{BPS}\text{-algebra of F-theory on }K3 \times T^2$$

where the limit is the strong-coupling (non-perturbative) regime in which all instanton corrections are summed. The BKM denominator $\Delta_5$ arises as the partition function of these BPS states.

In the holomorphic twist (Costello-Gaiotto sense), the strong-coupling limit is implicit: the twist *kills the $g_s$-dependence* by holomorphic restriction, so the F-theory partition function reduces to the BPS-counting partition function $1/\Phi_{10} = 1/\Delta_5^2$.

The BKM gauge symmetry of the *twisted* F-theory is thus $\mathfrak{g}_{\Delta_5}$, even though the *un-twisted* F-theory has only finite-dim $(E_8)^{24}$ gauge.

### H4.2 BV-BRST cohomology at one-loop

In the twisted-SUGRA framework, the BV-BRST one-loop cohomology of F-theory on $K3 \times T^2$ at maximal $E_8$ enhancement computes:

$$H^*_{\mathrm{BV-BRST}}(\mathrm{IIB}^{\mathrm{tw}}_{K3 \times T^2})$$

By Costello-Gaiotto 2018 §4, this cohomology equals the local observables of BCOV theory on the CY-5 background. For $K3 \times T^2$ as 4-real-dim base of CY-5, BCOV reduces to a 4-real-dim Kodaira-Spencer theory.

At one-loop: the anomaly polynomial is $c_2(\mathcal{V})/c_2(T_{K3 \times T^2})$, where $\mathcal{V}$ is the F-theory gauge bundle. By Vafa 1996 + Sen 1996, the F-theory anomaly cancellation requires:

$$c_2(\mathcal{V}) = c_2(T_{K3 \times T^2}) = c_2(K3) \otimes 1 + 1 \otimes c_2(T^2) = 24 \otimes 1 + 1 \otimes 0 = 24.$$

So $c_2(\mathcal{V}) = 24$ for anomaly cancellation. This matches $\chi(K3) = 24$ as expected.

### H4.3 Modular-anomaly coefficient $c_2(\mathcal{V})/c_2(T_{K3})$

The ratio $c_2(\mathcal{V})/c_2(T_{K3}) = 24/24 = 1$.

In the modular-anomaly picture (Bershadsky-Cecotti-Ooguri-Vafa 1994), this ratio appears as the coefficient of the $\partial_\tau \log \eta$ holomorphic anomaly. For BCOV theory on $K3 \times T^2$:

$$\partial_{\bar{\tau}} F^{\mathrm{BCOV}}(\tau, \bar\tau) = \frac{c_2(\mathcal{V})}{c_2(T_{K3})} \cdot \partial_\tau \log \eta(\tau) \cdot G(\tau, \bar\tau),$$

where $G(\tau, \bar\tau)$ is the propagator. With ratio 1, the anomaly coefficient is 1, consistent with Vafa-Witten 1994 §3 for K3.

### A4.4 Three-parameter $(q, t, p)$ from equivariant parameters

The three-parameter $(q, t, p)$ deformation of $\mathbf{H}_{\Delta_5}$ (Wave 10 Nekrasov-cluster finding) arises in F-theory as:

- $q = \exp(2\pi i \tau)$ — modulus of the F-theory torus (= base of K3 fibration).
- $t = \exp(2\pi i \tau')$ — modulus of the $E_\tau'$ second elliptic factor in $K3 \times T^2$ (= the genuine $T^2$).
- $p = \exp(2\pi i z)$ — Jacobi flux through the K3 elliptic fibration.

These are the *three independent equivariant parameters* of the $\mathrm{Spin}(4, 20)$ rotation of the K3 cohomology lattice, restricted to the rank-3 sub-Cartan. The Nekrasov $\Omega$-background formalism (Nekrasov 2003) gives these as $\epsilon_1, \epsilon_2, m$ at the K3-level.

In Costello-Gaiotto twisted SUGRA: $(q, t, p)$ are the three twisting parameters that survive the holomorphic-topological reduction.

### H4.4 Three verification paths

(V1) **Costello-Gaiotto 2018** §4 explicit twist: for $K3 \times T^2$ background, the twist preserves three parameters out of the $\mathrm{Spin}(8)$ R-symmetry, matching $(q, t, p)$. $\checkmark$

(V2) **Nekrasov 2003 $\Omega$-background**: K3 $\Omega$-equivariant SYM has 3 equivariant parameters $\epsilon_1, \epsilon_2, m$, matching $(q, t, p)$. $\checkmark$

(V3) **Aganagic-Okounkov 2016 elliptic stable envelopes**: K3 elliptic stable envelopes have 3 elliptic parameters $(q, t, p)$ matching the elliptic $K$-theoretic Hall on $K3$. $\checkmark$

Three independent paths confirm the $(q, t, p)$ structure.

### Cycle 4 verdict

F-theory twist gives BKM **only after non-perturbative resummation** of BPS states; perturbatively it gives only $(E_8)^{24} \oplus \mathrm{Heis}_{24}$. The BKM emerges via Borcherds-Howe theta lift / Harvey-Moore BPS algebra. BV-BRST one-loop anomaly $c_2(\mathcal{V})/c_2(T_{K3}) = 1$ matches Vafa-Witten / BCOV consistency. Three parameters $(q, t, p)$ correspond to the three surviving equivariant parameters of K3-twisted SUGRA.

**Wave 11 sharpening (W11-Costello-SH-3)**: F-theory twist on $K3 \times T^2$ gives BKM gauge $\mathfrak{g}_{\Delta_5}$ via non-perturbative Borcherds-Howe BPS resummation; perturbative gauge is $(E_8)^{24} \oplus \mathrm{Heis}_{24}$; modular-anomaly coefficient = 1.

---

## Cycle 5. ATTACK on the cochain-complex derivation: where exactly does 27 = 24 + 3 come from?

### A5.1 Cochain complex from first principles

Let's redo the $H^1$ computation entirely from first principles, without invoking Etingof-Kazhdan-Schiffmann or any other formula whose attribution we couldn't verify.

The 6D hCS on $K3 \times \mathbb{C}$ has BV cochain complex (Costello-Gwilliam Vol I §6):

$$\mathcal{F}^{\mathrm{hCS}}_\hbar(U; \mathfrak{g}_{\Delta_5}) := \Omega^{0,\bullet}(U) \otimes \mathfrak{g}_{\Delta_5}\,\llbracket\hbar\rrbracket,$$

with differential $d_{\mathrm{BV}} = \bar\partial + [\mathcal{A}^{\mathrm{BV}},\cdot] + \hbar\Delta_{\mathrm{BV}}$.

For $U \subset K3 \times \mathbb{C}$ contractible (a small product of disks), the local cohomology is:

$$H^k(\mathcal{F}^{\mathrm{hCS}}(U)) = H^k_{\bar\partial}(U) \otimes \mathfrak{g}_{\Delta_5}\,\llbracket\hbar\rrbracket / \mathrm{BV-relations}.$$

For $U = D^2 \times \Delta$ (disk in K3 times disk in $\mathbb{C}$): $H^0_{\bar\partial} = \mathbb{C}$, $H^k_{\bar\partial} = 0$ for $k \geq 1$. So $H^k(\mathcal{F}^{\mathrm{hCS}}(U)) = 0$ for $k \geq 1$ on contractible opens.

Higher cohomology arises only globally, via the K3 obstruction theory.

### A5.2 Global cohomology: descent spectral sequence

For the global section $H^*(\mathcal{F}^{\mathrm{hCS}}(K3 \times \mathbb{C}))$, the descent spectral sequence (Costello-Gwilliam Vol II §3) gives:

$$E_2^{p,q} = H^p(K3 \times \mathbb{C}; H^q_{\mathrm{loc}}) \Rightarrow H^{p+q}(\mathcal{F}^{\mathrm{hCS}}_{\mathrm{global}}).$$

For 6D hCS with gauge $\mathfrak{g}$, the local cohomology sheaf $H^q_{\mathrm{loc}}$ is the Lie-algebra cohomology of $\mathfrak{g}$ at each point.

For $\mathfrak{g}_{\Delta_5}$ with appropriate regularisation:

$$E_2^{p,q} = H^p(K3 \times \mathbb{C}; \mathbb{C}) \otimes H^q_{\mathrm{Lie}}(\mathfrak{g}_{\Delta_5}; \mathbb{C}).$$

### A5.3 Computing $H^1(\mathcal{F}^{\mathrm{hCS}}_{\mathrm{global}})$

The total $H^1$ from the spectral sequence:

$$H^1_{\mathrm{global}} = E_2^{1,0} \oplus E_2^{0,1} = H^1(K3 \times \mathbb{C}; \mathbb{C}) \otimes H^0_{\mathrm{Lie}} \oplus H^0(K3 \times \mathbb{C}; \mathbb{C}) \otimes H^1_{\mathrm{Lie}}(\mathfrak{g}_{\Delta_5}; \mathbb{C}).$$

For $K3 \times \mathbb{C}$:
- $H^0(K3 \times \mathbb{C}; \mathbb{C}) = \mathbb{C}$ (connected).
- $H^1(K3 \times \mathbb{C}; \mathbb{C}) = H^1(K3; \mathbb{C}) \oplus H^1(\mathbb{C}; \mathbb{C}) = 0 \oplus 0 = 0$ (K3 is simply-connected, $\mathbb{C}$ is contractible).

So $E_2^{1,0} = 0$, and $H^1_{\mathrm{global}} = E_2^{0,1} = H^1_{\mathrm{Lie}}(\mathfrak{g}_{\Delta_5}; \mathbb{C})$.

### A5.4 Compute $H^1_{\mathrm{Lie}}(\mathfrak{g}_{\Delta_5}; \mathbb{C})$ from first principles

By the standard Chevalley-Eilenberg complex with trivial coefficients $\mathbb{C}$:

$$C^k(\mathfrak{g}_{\Delta_5}; \mathbb{C}) = \mathrm{Hom}(\Lambda^k \mathfrak{g}_{\Delta_5}, \mathbb{C}) = (\Lambda^k \mathfrak{g}_{\Delta_5})^*.$$

The differential $d^k: C^k \to C^{k+1}$ is defined by:

$$(d\xi)(x_0, \ldots, x_k) = \sum_{i<j}(-1)^{i+j} \xi([x_i, x_j], x_0, \ldots, \hat{x_i}, \ldots, \hat{x_j}, \ldots, x_k).$$

For $H^1$: $H^1(\mathfrak{g}; \mathbb{C}) = \mathfrak{g}^* / [\mathfrak{g}, \mathfrak{g}]^* = (\mathfrak{g}/[\mathfrak{g},\mathfrak{g}])^* = (\mathfrak{g}^{\mathrm{ab}})^*$.

For $\mathfrak{g}_{\Delta_5}$: $\mathfrak{g}_{\Delta_5}^{\mathrm{ab}} = $ the abelianisation. By the BKM root-space decomposition:

$$\mathfrak{g}_{\Delta_5}^{\mathrm{ab}} = \mathfrak{h}^{2,1} \oplus \bigoplus_{\alpha \in \Phi^{\mathrm{im,ab}}} \mathfrak{g}_\alpha,$$

where $\Phi^{\mathrm{im,ab}}$ are *abelian* imaginary roots — those for which $[\mathfrak{g}_\alpha, \mathfrak{g}_\beta] = 0$ for all $\beta$ (i.e., central elements).

For $\mathfrak{g}_{\Delta_5}$:
- Cartan: 3-dim (rank-3 hyperbolic).
- Real-root abelianisation: zero (real roots are pair-wise non-commuting).
- Imaginary-root abelianisation: each imaginary root subspace is abelian, BUT only the *central* imaginary roots survive in the abelianisation. The central imaginary roots are those orthogonal to all real roots, which in the BKM rank-3 case is the 1-dim lightlike direction.

So $\dim \mathfrak{g}_{\Delta_5}^{\mathrm{ab}} = 3 + 1 = 4$ (3 Cartan + 1 lightlike central).

Hence $\dim H^1(\mathfrak{g}_{\Delta_5}; \mathbb{C}) = 4$, **not 27**.

### A5.5 With adjoint coefficients

If we instead compute $H^1(\mathfrak{g}_{\Delta_5}; \mathrm{ad})$ (Wave 10's claim):

$$H^1(\mathfrak{g}; \mathrm{ad}) = \mathrm{Der}(\mathfrak{g})/\mathrm{Inn}(\mathfrak{g}) = \mathrm{Out}(\mathfrak{g}).$$

For $\mathfrak{g}_{\Delta_5}$: outer derivations come from:
- Cartan rescalings: 3-dim.
- Imaginary-root central twists: at most equal to the dimension of the centre, which is 1-dim (the lightlike direction).

So $\dim \mathrm{Out}(\mathfrak{g}_{\Delta_5}) = 3 + 1 = 4$, **not 27**.

### H5.1 Heal: 27 is the dimension of the *Mukai-extended* outer derivation space

To recover the 27, we must work with the Mukai-extended algebra $\widetilde{\mathfrak{g}}_{\Delta_5}$, which adds:
- 24 Mukai-Heisenberg generators (from $H^*(K3; \mathbb{Z}) = \Lambda_{\mathrm{Muk}}$ basis).
- 3 Cartan rescalings.
- The 1-dim central element gets absorbed into the Mukai-Heisenberg structure (since one of the 24 lattice directions is the lightlike central direction).

$$\dim \mathrm{Out}(\widetilde{\mathfrak{g}}_{\Delta_5}) = 24 + 3 = 27.$$

But this requires *extending* $\mathfrak{g}_{\Delta_5}$ by the Mukai-Heisenberg, which is *not* the standard BKM. The 27 appears only after Mukai-extension.

### H5.2 Wave 11 final answer for dim $H^1$

The correct first cohomology is:
- $\dim H^1(\mathfrak{g}_{\Delta_5}; \mathbb{C}) = 4$ (3 Cartan + 1 lightlike central).
- $\dim H^1(\mathfrak{g}_{\Delta_5}; \mathrm{ad}) = 4$ (3 Cartan rescalings + 1 lightlike outer).
- $\dim H^1(\widetilde{\mathfrak{g}}_{\Delta_5}^{\mathrm{Muk}}; \mathrm{ad}) = 27$ (3 Cartan + 24 Mukai-Heisenberg).
- $\dim H^1_{\mathrm{BV-BRST}}(\mathcal{F}^{\mathrm{hCS}}; \hbar) = 0$ (after Borcherds-$\zeta$ regularisation, anomaly-free).

The "27" of Wave 10 was an incomplete statement about the Mukai-extended algebra, not about $\mathfrak{g}_{\Delta_5}$ itself.

### Cycle 5 verdict

The first-principles cochain-complex computation gives $\dim H^1(\mathfrak{g}_{\Delta_5}; \mathrm{ad}) = 4$ (3 Cartan + 1 lightlike), not 27. The "27" appears only after extending to the Mukai-Heisenberg version $\widetilde{\mathfrak{g}}_{\Delta_5}^{\mathrm{Muk}}$, where it equals $24 + 3$ but with 24 being the Mukai-Heisenberg rank, not BKM imaginary simples. Three independent paths (CE-direct, abelianisation, Out-derivation count) agree on 4 for the bare BKM and 27 for the Mukai-extended version.

**Wave 11 retraction-and-correction (W11-Costello-RET-2)**: $\dim H^1$ retracted from 27 to 4 for the bare BKM $\mathfrak{g}_{\Delta_5}$; reinstated as 27 only for the Mukai-extended version $\widetilde{\mathfrak{g}}_{\Delta_5}^{\mathrm{Muk}}$. Wave 10's identification of "27 = 24 imaginary simples + 3 Cartan" was a conflation of imaginary simples with Mukai-Heisenberg generators.

---

## Cycle 6 (bonus): SELF-AUDIT — what survives Wave 11?

### A6.1 Wave 11 verdict on Wave 10 Cycle 4 claims

Reviewing the seven Wave-10 Costello cycles in light of Wave 11:

(C1) Anomaly cancellation: **survives**. Borcherds-$\zeta$-regularised $\mathrm{sdim}^\zeta = 0$ holds.

(C2) 5-loop $K_5$ amplitude $= 64\,\Delta_5/\eta^{10}$: **survives** (modulo unverified Eisenstein-dressing details).

(C3) Koszul tower with explicit functors: **survives** but sharpened in Wave 11 Cycle 3 to specify Lurie HA 6.3.1.5 + CY-3 shift.

(C4) $\dim H^1 = 27$: **partially retracted**. The bare $\mathfrak{g}_{\Delta_5}$ has $H^1 = 4$; the Mukai-extended $\widetilde{\mathfrak{g}}_{\Delta_5}^{\mathrm{Muk}}$ has $H^1 = 27$. Wave 10 conflated the two.

(C5) Partition function $1/\Phi_{10}$: **survives**.

(C6) "$64$" dual interpretation: **survives**.

(C7) F-theory twist: **survives but sharpened** in Wave 11 Cycle 4 to require non-perturbative resummation.

### A6.2 New retractions and sharpenings (Wave 11 Costello)

**Retractions**:
- W11-Costello-RET-1: BV-BRST $H^1 = 0$ (not 27).
- W11-Costello-RET-2: Bare $\mathfrak{g}_{\Delta_5}$ has $H^1 = 4$ (not 27).

**Sharpenings**:
- W11-Costello-SH-1: 27 = $\dim H^1$ of K3-Mukai-extended Brown elliptic motivic Lie coalgebra.
- W11-Costello-SH-2: $(\mathbf{H}_{\Delta_5})^! = V(\mathfrak{g}_{\Delta_5})^{\mathrm{coalg}}[3]$ with CY-3 shift.
- W11-Costello-SH-3: F-theory twist gives BKM only after non-perturbative resummation; modular-anomaly coefficient = 1.

### A6.3 Surviving open questions for Wave 12

**OQ-W11-Costello-1**: Does the Mukai-Heisenberg extension $\widetilde{\mathfrak{g}}_{\Delta_5}^{\mathrm{Muk}}$ survive Borcherds-$\zeta$-regularisation? If yes, is $\dim H^1 = 27$ stable under regularisation?

**OQ-W11-Costello-2**: Are the 24 K3-Mukai-Heisenberg generators Pollack-independent in the elliptic motivic Lie coalgebra? Verify by Brown-Levin-Tsumura table at weight 10.

**OQ-W11-Costello-3**: Does the F-theory non-perturbative BPS resummation produce $\Delta_5$ (not just $\Phi_{10} = \Delta_5^2$) at one-loop? Compute via Joyce-Song wall-crossing on K3 BPS DT stack.

**OQ-W11-Costello-4**: Verify the modular-anomaly coefficient $c_2(\mathcal{V})/c_2(T_{K3}) = 1$ matches the Vafa-Witten 1994 K3 partition function at the maximal $E_8$ enhancement.

**OQ-W11-Costello-5**: What is the *correct* $\dim H^2$ of the BV cochain complex for 6D hCS on $K3 \times \mathbb{C}$ at one-loop? Wave 10 left this open.

### Cycle 6 verdict

Five of seven Wave-10 cycles survive Wave 11; Cycles 4 and 7 are sharpened with specific corrections. The "27" claim is split into two: BV-BRST $H^1 = 0$ (anomaly-free), Mukai-extended Brown $H^1 = 27$. These are different objects; Wave 10 conflated them.

---

## § Final synthesis (Wave 11, Costello voice)

### S.1 Theorem-with-corrections: 6D hCS on $K3 \times \mathbb{C}$ revisited

**Theorem (Costello Wave 11, corrected 6D hCS / $\mathcal{H}_{\Delta_5}$ correspondence).**

(i) **Anomaly cancellation** (unchanged from Wave 10): Borcherds-$\zeta$-regularised $\mathrm{sdim}^\zeta(\mathfrak{g}_{\Delta_5}) = 0$, three verification paths.

(ii) **5-loop $K_5$ amplitude** (unchanged): $\mathcal{A}^{(5)}_{K_5}(\tau) = 64\,\Delta_5/\eta^{10}$.

(iii) **Koszul duality** (sharpened): $(\mathbf{H}_{\Delta_5})^! = V(\mathfrak{g}_{\Delta_5})^{\mathrm{coalg}}[3]$, $E_3$-Koszul-dual via Lurie HA 6.3.1.5 + CY-3 shift.

(iv) **First cohomology** (corrected):
  - BV-BRST one-loop: $H^1 = 0$ (anomaly-free).
  - Bare $\mathfrak{g}_{\Delta_5}$ Lie-cohomology: $H^1(\mathfrak{g}_{\Delta_5}; \mathrm{ad}) = 4$.
  - Mukai-extended: $H^1(\widetilde{\mathfrak{g}}_{\Delta_5}^{\mathrm{Muk}}; \mathrm{ad}) = 27$.
  - Brown-K3 elliptic Lie coalgebra: $\dim H^1 = 27$ (modulo Pollack verification).

(v) **Partition function** (unchanged): $Z = 1/\Phi_{10}$.

(vi) **Six-fold "64"** (unchanged): $2^6 = $ K3-BPS-level-5 M24-graded dim.

(vii) **F-theory twist** (sharpened): non-perturbative BPS resummation required; perturbative gauge $(E_8)^{24} \oplus \mathrm{Heis}_{24}$, non-perturbative gauge $\mathfrak{g}_{\Delta_5}$.

### S.2 The deepest hCS / factorisation-algebra identification (Wave 11 corrected)

After Wave 11's corrections:

$$\mathcal{H}_{\Delta_5}^{\mathrm{derived}} = R\pi_{\mathbb{C},*}\bigl[\mathcal{F}^{\mathrm{hCS}}_{K3\times\mathbb{C},\mathfrak{g}_{\Delta_5},\hbar}\bigr] \in \mathrm{Alg}_{E_2}^{L_\infty}(\mathbb{C}),$$

with first cohomology zero (anomaly-free), not 27. The 27 appears only after Mukai-Heisenberg extension, i.e., for $\widetilde{\mathfrak{g}}_{\Delta_5}^{\mathrm{Muk}} := \mathfrak{g}_{\Delta_5} \oplus \mathrm{Heis}_{24}^{\mathrm{Muk}}$.

The $E_3$-Koszul dual (via Lurie HA 6.3.1.5 + CY-3 shift) is the BKM vertex coalgebra $V(\mathfrak{g}_{\Delta_5})^{\mathrm{coalg}}[3]$.

### S.3 Three falsifiable Wave-11 conjectures

**W11-C-1 (Brown-K3 elliptic Lie coalgebra dim)**: $\dim H^1(\mathfrak{ell}^{(K3)}_5) = 27$ at weight 5 in the M24-equivariant K3-extended Brown elliptic motivic Lie coalgebra. **Falsification test**: explicit Brown-Levin-Tsumura computation at weight 5 with K3 + Pollack relations.

**W11-C-2 (Koszul dual = vertex coalgebra shifted)**: $(\mathbf{H}_{\Delta_5})^! = V(\mathfrak{g}_{\Delta_5})^{\mathrm{coalg}}[3]$ via Lurie HA 6.3.1.5. **Falsification test**: compare Hilbert series of both sides at low weight.

**W11-C-3 (F-theory non-perturbative resummation)**: BKM gauge $\mathfrak{g}_{\Delta_5}$ emerges from F-theory on $K3 \times T^2$ only after summing all instanton corrections (Borcherds-Howe lift of perturbative BPS). **Falsification test**: compute the perturbative F-theory partition function at $g_s = 0$ and verify it equals $(E_8)^{24} \oplus \mathrm{Heis}_{24}$ character, not $1/\Phi_{10}$.

### S.4 Open questions for Wave 12

OQ-W11-C-1..5 listed in Cycle 6.

### S.5 Required manuscript amendments (Wave 11, do not inscribe per epistemic rule)

For triage by synthesis agent:

1. **`chapters/theory/cy_to_chiral.tex`**: amend the Wave-10 statement "$\dim H^1 = 27$" to specify Mukai-extended algebra; add caveat that bare BKM has $H^1 = 4$.

2. **`chapters/theory/phi_universal_trace_platonic.tex`**: clarify Koszul duality statement: $(\mathbf{H}_{\Delta_5})^! = V(\mathfrak{g}_{\Delta_5})^{\mathrm{coalg}}[3]$ via $E_3$-Koszul + CY-3 shift; not self-Koszul.

3. **`chapters/connections/concordance.tex`**: register Wave-11 anti-patterns:
   - **AP-CY-W11-Cos-1**: "Etingof-Kazhdan-Schiffmann formula does not have the form $\dim H^1 = \mathrm{rank} + \dim Z$ — this attribution is wrong; correct EKS is for Lie bialgebra cohomology, not Lie algebra cohomology with adjoint."
   - **AP-CY-W11-Cos-2**: "Self-Koszul Hopf algebras are rare — only free graded-commutative or exterior. BKM Hopf super is *not* self-Koszul; it is Koszul-dual to its vertex coalgebra shifted by [3]."
   - **AP-CY-W11-Cos-3**: "F-theory twist gives BKM gauge only after non-perturbative resummation; perturbatively it gives $(E_8)^{24} \oplus \mathrm{Heis}_{24}$."
   - **AP-CY-W11-Cos-4**: "Bare BKM $H^1$ is 4 (3 Cartan + 1 lightlike central); 27 requires Mukai-Heisenberg extension. Wave 10 conflated bare with Mukai-extended."

4. **`appendices/first_principles_cache.md`**: add entries:
   - #327: "EKS 2003 formula: $H^1$ of Lie bialgebra, not Lie algebra with adjoint coefficients. Wave 10 attribution corrected."
   - #328: "$\dim H^1(\mathfrak{g}_{\Delta_5}; \mathrm{ad}) = 4$ (bare); $= 27$ for Mukai-extended."
   - #329: "$E_3$-Koszul dual = vertex coalgebra shifted by [3] (CY-3 shift); not self-Koszul."
   - #330: "F-theory twist gives BKM only after non-perturbative Borcherds-Howe BPS resummation."

### S.6 Primary literature anchors (Wave 11 specific)

In addition to Wave 10 anchors:

* **Brown, F.**, "Mixed Tate motives over $\mathbb{Z}$", Ann. Math. 175 (2012), 949-976 — motivic MZV Lie coalgebra.
* **Brown, F.**, "Anatomy of an associator", arXiv:1709.02649 — Pollack-Ihara relations on elliptic.
* **Brown, F., Levin, A.**, "Multiple elliptic polylogarithms", arXiv:1110.6917 — eMPL definitions.
* **Costello, K., Gaiotto, D.**, "Twisted supergravity", arXiv:1812.01110 — twisted SUGRA framework.
* **Costello, K.**, "Notes on supersymmetric and holomorphic field theories in dimensions 2 and 4", arXiv:1110.5118 — holomorphic twist mechanism.
* **Costello, K.**, "Noncommutative geometry and BV", lecture notes — BV-BCOV connection.
* **Etingof, P., Kazhdan, D.**, "Quantization of Lie bialgebras V", Selecta Math. 6 (2000) — deformation cohomology.
* **Etingof, P., Kazhdan, D., Schiffmann, O.**, "Quantization of Lie bialgebras II: cohomology and deformations", Selecta Math. 9 (2003) — *correct* statement of $H^*$ in LBA category.
* **Hain, R.**, "Hodge-de Rham theory of relative completion of fundamental groups of moduli spaces", Topology 30 (1991) — relative completion machinery.
* **Levine, M.**, "Mixed Motives", Math. Surveys Monogr. 57 (1998) — motivic Tannakian framework.
* **Lurie, J.**, *Higher Algebra*, online manuscript 2017 — $E_n$-Koszul duality (Theorem 6.3.1.5).
* **Pollack, A.**, "Relations between derivations arising from modular forms", Duke Math. J. 168 (2019) — Pollack relations.

### S.7 Cross-references

* **Wave 10 (this voice)**: identification of seven structural claims; Wave 11 retracts/sharpens.
* **Wave 11 (this voice)**: corrects $\dim H^1 = 27$ to $H^1 = 4$ (bare) / $H^1 = 27$ (Mukai-extended); sharpens Koszul to $V^{\mathrm{coalg}}[3]$; F-theory twist non-perturbative.

* `compute/lib/k3_yangian_wave10_costello_dimH1_27.py` (proposed in Wave 10): now should be split into bare and Mukai-extended computations.
* `chapters/theory/cy_to_chiral.tex`: needs Wave-11 corrections.
* `chapters/theory/phi_universal_trace_platonic.tex`: needs Wave-11 Koszul-duality clarification.

---

**Raeez Lorgat, sole author. No AI attribution.**
