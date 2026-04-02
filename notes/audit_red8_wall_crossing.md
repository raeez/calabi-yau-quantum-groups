# Adversarial Audit: physics_wall_crossing_mc.tex

**Date**: 2026-04-02
**Auditor**: Red Team Agent 8 (Wall-Crossing / MC Gauge Equivalence)
**Target**: `notes/physics_wall_crossing_mc.tex`
**Scope**: The central thesis that KS wall-crossing = gauge equivalence of MC elements in the modular convolution algebra

---

## Summary Verdict

The note is honest about its status ("expository," "proof strategy" rather than proof), and the high-level dictionary is plausible. But it papers over five structural gaps, three of which are genuine mathematical problems that cannot be resolved by future work in the programme without significant new ideas. The other two are serious expository failures that could mislead the reader into thinking more has been established than actually has.

---

## Finding 1: SYMPLECTOMORPHISMS vs. GAUGE TRANSFORMATIONS -- THE ALGEBRAIC STRUCTURE MISMATCH

**Severity: HIGH (genuine gap)**

### The problem

The KS wall-crossing formula (Theorem 3.2, eq. 3.5) involves an ordered product of *symplectomorphisms* $K_\gamma$ of the formal torus algebra $\mathbb{T}_\Gamma$. The exponent in eq. (3.3) acts via the *Poisson bracket* on $\mathbb{T}_\Gamma$ determined by the Euler form $\chi(\gamma, \gamma')$. These are elements of $\mathrm{Aut}(\mathbb{T}_\Gamma)$ as a *Poisson algebra*.

MC gauge equivalence (Section 2.2, eq. 2.3) involves the action of $\exp(\mathfrak{g}^0)$ on $\mathfrak{g}^1$ via the BCH formula for the *Lie bracket* of $\mathfrak{g}^{\mathrm{mod}}_A$.

These are *different* algebraic structures. A Poisson automorphism of a commutative algebra is not the same as a gauge transformation of a dgLa unless there is a specific identification between:

1. The Lie algebra of Hamiltonian vector fields on $\mathbb{T}_\Gamma$ (which generates the symplectomorphisms), and
2. The degree-zero part $(\mathfrak{g}^{\mathrm{mod}}_A)^0$ (which generates gauge transformations).

The note *asserts* this identification in the dictionary table (Section 3.3) but never constructs or proves it. The dictionary entry "KS factor $K_\gamma \longleftrightarrow$ Factor in bar-complex Euler product" is a *category error*: $K_\gamma$ is an automorphism of a ring, while a factor in the Euler product is a formal power series. These are objects of different types.

### What is needed

An explicit construction of a Lie algebra map

$$\mathrm{Ham}(\mathbb{T}_\Gamma, \{\cdot,\cdot\}_\chi) \longrightarrow (\mathfrak{g}^{\mathrm{mod}}_A)^0$$

that intertwines the Poisson bracket action on $\mathbb{T}_\Gamma$ with the gauge action on $\mathrm{MC}(\mathfrak{g}^{\mathrm{mod}}_A)$. This map must be shown to exist for the *specific* $L_\infty$-structure of $\mathfrak{g}^{\mathrm{mod}}_A$, not for an abstract dgLa.

Without this, the central claim of the note is a dictionary entry with no mathematical content.

### Mitigating factor

The Euler form $\chi(\gamma, \gamma')$ *is* antisymmetric (by Serre duality for CY3), so it does define a Poisson structure on $\mathbb{T}_\Gamma$. If $(\mathfrak{g}^{\mathrm{mod}}_A)^0$ can be identified with the Lie algebra of this Poisson structure, the dictionary could in principle work. But this identification is the *content* of the claim, not a consequence.

---

## Finding 2: THE ORDERING PROBLEM -- KS PRODUCTS ARE ORDERED, GAUGE GROUPS ARE NOT

**Severity: HIGH (genuine gap)**

### The problem

The KS product (eq. 3.5) is an *ordered* product:

$$\mathbf{A}_\ell(t) = \prod_{\gamma}^{\curvearrowleft} K_\gamma^{\Omega(\gamma;t)}$$

where $\curvearrowleft$ denotes clockwise ordering by $\mathrm{Arg}\, Z_t(\gamma)$. The *entire content* of the KS formula is that this ordered product is invariant. Change the order, and the product changes (the $K_\gamma$ do not commute in general).

Gauge transformations in a dgLa form a *group* under BCH composition. The gauge orbit $\exp(\mathfrak{g}^0) \cdot \Theta$ is a set, not an ordered product. The gauge equivalence relation $\Theta' \sim e^\alpha \cdot \Theta$ involves a *single* gauge element $\alpha$, not an ordered product of factors.

The note tries to bridge this gap in Construction 3.4 (eq. 3.9) by writing $\alpha_{12}$ as a *single* element determined by the BCH expansion of the KS factorization. This is legitimate in principle -- the BCH formula does produce a single Lie algebra element from an ordered product of exponentials. But there are two problems:

**Problem A**: The BCH series $\log(e^{a_1} e^{a_2} \cdots e^{a_N})$ converges only when the $a_i$ are sufficiently small. For the KS product, the factors are indexed by *all* $\gamma \in \Gamma_+$ with $\Omega(\gamma) \neq 0$ -- this is typically an infinite set. The BCH series for infinitely many factors requires a completion argument. What is the topology on $(\mathfrak{g}^{\mathrm{mod}}_A)^0$ in which $\alpha_{12}$ converges?

**Problem B**: The ordering in the KS product determines *which* gauge element $\alpha_{12}$ you get. Different orderings give different $\alpha_{12}$ (related by further BCH manipulations). The note presents the gauge element as if it is canonical, but it depends on the choice of half-plane $\ell$ (the reference ordering). This is not a contradiction, but it means the gauge element $\alpha_{12}$ is *not* intrinsic to the wall -- it depends on auxiliary data (the half-plane). The note should state this explicitly and explain why the dependence is harmless.

### What is needed

(A) A topology/filtration on $(\mathfrak{g}^{\mathrm{mod}}_A)^0$ for which the infinite BCH product converges. The natural candidate is the $\Gamma_+$-adic filtration (completed with respect to the positive cone), but this must be verified to be compatible with the $L_\infty$-structure.

(B) An explicit statement that $\alpha_{12}$ depends on the reference ordering, and that different orderings give gauge-equivalent MC elements (which is a consequence of the group structure of $\exp(\mathfrak{g}^0)$, hence tautological once convergence is established).

---

## Finding 3: THE GAUGE INVARIANCE OF THE DENOMINATOR IDENTITY -- ASSERTED, NOT PROVED

**Severity: MEDIUM-HIGH (missing proof)**

### The problem

Proposition 3.1 claims that the bar-complex Euler product $\Phi_X(x)$ is gauge-invariant. The "proof sketch" (lines 293-305) argues:

1. $\Phi_X$ is the graded character of $H^\bullet(B(A), d_B)$.
2. A gauge transformation induces a quasi-isomorphism $B(A; \Theta_A) \xrightarrow{\sim} B(A; e^\alpha \cdot \Theta_A)$.
3. Quasi-isomorphic complexes have the same Euler characteristic.

Step 2 is the load-bearing claim, and it is *asserted without proof*. Why does a gauge transformation of the MC element induce a quasi-isomorphism of bar complexes? In the classical dgLa setting, a gauge transformation $e^\alpha \cdot \Theta$ gives an equivalent deformation, and the associated twisted complexes are quasi-isomorphic -- this is the standard deformation theory fact. But $\mathfrak{g}^{\mathrm{mod}}_A$ is a *curved* $L_\infty$-algebra (the curvature $\ell_0 \neq 0$, as stated in Section 2.1). For curved $L_\infty$-algebras:

- The bar complex $B(A; \Theta_A)$ is *not* a standard bar construction -- the differential includes the curvature term.
- Gauge equivalence in the curved setting is more delicate: the gauge group must preserve the curvature class.
- The standard theorem "gauge-equivalent MC elements give quasi-isomorphic twisted complexes" does NOT automatically hold for curved $L_\infty$-algebras. The obstruction is that the curvature may prevent the gauge transformation from being a chain map.

The note needs to either (a) cite a specific theorem for curved $L_\infty$-algebras that establishes step 2, or (b) prove it. Positselski's work on curved A-infinity algebras shows that the theory of curved structures has many traps -- naive generalizations from the uncurved case often fail.

### What is needed

A precise reference or proof that gauge equivalence in the *curved* $L_\infty$-algebra $\mathfrak{g}^{\mathrm{mod}}_A$ induces a quasi-isomorphism of the associated bar complexes. This is not a trivial extension of the uncurved case.

---

## Finding 4: THE ATTRACTOR MECHANISM DOES NOT APPLY TO MULTI-CENTER CONFIGURATIONS

**Severity: MEDIUM (overclaim in physical interpretation)**

### The problem

Section 5 identifies the attractor MC element $\Theta_A^*$ (Definition 5.1) as the canonical gauge, using attractor flow in $\mathcal{N}=2$ supergravity. The note states (eq. 5.3):

$$\Theta_A(t) = e^{\alpha(t, t_*)} \cdot \Theta_A^*$$

where $\alpha(t, t_*)$ encodes the "binding data" and is "determined by the split attractor flow of Denef (2000)."

The problem: the Ferrara-Kallosh-Strominger attractor mechanism applies to *single-center* extremal black holes. For a charge $\gamma$ with a single-center attractor point $t_*(\gamma)$, the moduli flow to $t_*(\gamma)$ near the horizon. But for a charge $\gamma = \gamma_1 + \gamma_2$ that is realized as a *multi-center bound state*, there is no single attractor point. Instead:

- The multi-center solution has moduli that are *spatially varying* -- different centers have different attractor points $t_*(\gamma_i)$.
- The "split attractor flow" of Denef is a *tree* of attractor flows, not a single flow. The tree structure depends on the stability condition.
- At walls of marginal stability, the multi-center solution ceases to exist (the centers fly apart). The "attractor MC element" $\Theta_A^*$ uses $\Omega_*(\gamma)$ -- the *single-centered* index -- which *discards* all multi-center contributions by definition.

This means:

(a) The attractor MC element $\Theta_A^*$ is well-defined only as a formal object (a specific representative of the MC class using single-center indices). It does NOT correspond to the physical attractor mechanism for multi-center states.

(b) The gauge element $\alpha(t, t_*)$ of eq. (5.3) is NOT literally the attractor flow tree datum, because the attractor flow tree depends on the *final* stability condition $t$, not just on the distance from $t_*$. The flow tree changes topology at walls of marginal stability, and identifying it with a *single* gauge element requires showing that different tree topologies give the same gauge orbit. This is essentially the KS wall-crossing formula again, so the argument is circular.

(c) Remark 5.2 claims "Different attractor points (for different total charges $\gamma$) give different canonical representatives, but they all lie in the same gauge orbit." This is false as stated. The attractor point $t_*(\gamma)$ depends on $\gamma$, and for different $\gamma$, the MC elements $\Theta_A^*$ are *different*. They lie in the same gauge orbit only if they define the same MC class -- which is the *content* of the claim, not a consequence. For the statement to make sense, you need to specify *which* total charge $\gamma$ determines the attractor point used as basepoint.

### What is needed

(a) Clearly delineate the domain of validity: the attractor interpretation applies cleanly to single-center charges. For multi-center bound states, the "attractor gauge" is a convenient formal choice, not a physical attractor mechanism.

(b) Acknowledge that the identification of $\alpha(t, t_*)$ with the Denef flow tree datum is a *conjecture* (it is listed as Q1 in Section 7.2, but it is also asserted as fact in Section 5.2). The two claims are contradictory -- either it is a proved identification or an open question.

(c) Fix Remark 5.2: the statement about different attractor points lying in the same gauge orbit needs a precise formulation. What is meant is that for a *fixed* total charge $\gamma$, the MC elements at different stability conditions are gauge-equivalent. The attractor point $t_*(\gamma)$ provides one canonical representative.

---

## Finding 5: FINITE-ORDER DISCONTINUITY -- THE COMPUTABILITY PROBLEM

**Severity: MEDIUM (expository/conceptual gap, not mathematical error)**

### The problem

Proposition 6.1 proves that the truncation $\Theta^{\leq r}_A(t)$ is discontinuous at walls for $r < \infty$. Section 6.3 then presents this as a *feature*, analogizing it with renormalization scheme dependence. But this framing obscures a serious conceptual problem:

**The full MC element $\Theta_A$ is the only gauge-invariant object, and it cannot be computed.**

The shadow tower is the computational handle on $\Theta_A$ -- one computes $\Theta^{\leq r}_A$ order-by-order and hopes the tower converges. But Proposition 6.1 says that every finite truncation is discontinuous at walls. This means:

(a) Any finite-order computation of the MC element *depends on the chamber* -- you must choose a stability condition before computing. The result is not intrinsic.

(b) The "UV completion" $\Theta_A$ that restores gauge invariance requires *infinitely many* arity contributions. In practice, only arities 2-4 are computable (the moduli spaces $\overline{\mathcal{M}}_{g,n}$ become intractable beyond small $g$ and $n$).

(c) The renormalization group analogy (Section 6.3) is misleading. In QFT, the running coupling at a given energy scale is a *measurable* quantity -- scheme-dependent but physically meaningful. Here, the truncation $\Theta^{\leq r}_A$ at a given arity is *not* physically meaningful because it jumps discontinuously. A quantity that is discontinuous as a function of moduli is not "scheme-dependent" -- it is simply not well-defined as a function on moduli space.

The honest statement is: the MC gauge equivalence interpretation of wall-crossing is a beautiful structural observation, but it converts a *computational* problem (determine BPS degeneracies) into a *non-computational* one (compute the full MC element). The denominator identity $\Phi_X$ is the gauge-invariant datum, but it is *already known* independently (it is the DT partition function / automorphic form). The MC framework does not produce $\Phi_X$ -- it *assumes* it.

### What is needed

(a) Acknowledge explicitly that the MC gauge equivalence framework, in its current form, does not provide a new method for computing BPS degeneracies or the denominator identity.

(b) Replace or qualify the RG analogy. In the RG analogy, scheme independence holds because the beta function is universal at leading order. Here, there is no analogue: the leading-order truncation ($\kappa$, the modular characteristic) is gauge-invariant, but the first correction (the cubic shadow $C$) is already discontinuous. The analogy would require $\Theta^{\leq r}_A$ to be "approximately" gauge-invariant for large $r$, with errors decreasing as $r$ increases. Is this true? If so, state and prove it. If not, the analogy fails.

(c) Question Q5 (Section 7.2) asks about a "regularized truncation" that is continuous across walls. This is the right question, but it should be elevated from "open question" to "essential for the programme to have computational content."

---

## Finding 6: THE "PROOF" OF THEOREM 3.5 IS A TAUTOLOGY

**Severity: MEDIUM (circular reasoning)**

### The problem

Theorem 3.5 ("Wall-crossing = MC gauge equivalence") is the central result. Its "proof strategy" (lines 447-464) proceeds:

**Part (i)**: "$[\Theta_A]$ is intrinsic because $A_\mathcal{C}$ is defined intrinsically (it depends on $\mathcal{C}$, not on a stability condition)."

This is *tautological*. The claim is that $\Theta_A(t_+)$ and $\Theta_A(t_-)$ are gauge-equivalent. The "proof" says: the underlying object $A_\mathcal{C}$ doesn't depend on $t$, so the MC class doesn't depend on $t$. But this *assumes* that $A_\mathcal{C}$ determines a unique MC class -- which requires showing that the construction $t \mapsto \Theta_A(t)$ produces MC elements in the same class. That is *the claim being proved*.

The issue: $\Theta_A(t)$ is not just "the MC element of $A_\mathcal{C}$ in the $t$-presentation." It is defined (eq. 3.2) as a formal sum involving BPS indices $\Omega(\gamma; t)$ and "primitive contributions" $\Theta_\gamma^{\mathrm{prim}}(t)$, both of which depend on $t$. Showing that this $t$-dependent expression satisfies the MC equation for each $t$ is one thing; showing that different $t$ give gauge-equivalent MC elements is another. The latter requires an explicit gauge element connecting them, which is the content of Construction 3.4. So part (i) actually depends on part (ii), making the claimed proof structure incoherent.

**Part (ii)**: "An explicit computation: the BCH formula applied to the $L_\infty$-structure reproduces the KS factorization algorithm."

This is the only substantive claim, and it is *unproved*. The note says the key input is that the $L_\infty$-brackets encode boundary strata of $\overline{\mathcal{M}}_{g,n}$ and the KS scattering diagram is the tropical limit. But this tropical limit identification is itself a deep result (related to the Gross-Siebert programme) that is not proved here and not established in the main monograph.

**Part (iii)**: Follows from Proposition 3.1, which itself has gap (Finding 3).

### What is needed

Restructure the argument. The honest proof strategy is:

1. Construct the $L_\infty$-algebra $\mathfrak{g}^{\mathrm{mod}}_A$ and show it has the properties claimed (curved, with brackets from boundary strata).
2. Construct the map from KS symplectomorphisms to gauge transformations (Finding 1).
3. Show the BCH expansion of the KS product gives a well-defined gauge element in $(\mathfrak{g}^{\mathrm{mod}}_A)^0$ (Finding 2).
4. Verify that this gauge element connects $\Theta_A(t_+)$ to $\Theta_A(t_-)$.

Steps 1-4 are all non-trivial and all unproved. The note should present them as a research programme, not as a theorem with a "proof strategy."

---

## Finding 7: THE CONIFOLD EXAMPLE IS MISLEADING

**Severity: LOW (expository)**

### The problem

Example 6.3 (the resolved conifold) claims that $\Theta^{\leq 2}_A$ jumps at the wall: "on one side, it includes the $\gamma_1 + \gamma_2$ contribution; on the other, it does not."

But $\Theta^{\leq 2}_A$ is the *arity-2* truncation, identified with the modular characteristic $\kappa$ in Section 6.1. The charge $\gamma_1 + \gamma_2$ is a *composite* charge with two constituents -- this is an arity-2 datum (it takes two BPS particles to form it). So the jump of $\Omega(\gamma_1 + \gamma_2)$ *is* a jump at arity 2, and $\Theta^{\leq 2}_A$ should indeed see it.

The confusion is that the example seems to equate "arity" with "number of constituents in a bound state," but the shadow tower arity decomposition (eq. 6.1) is indexed by the moduli space $\overline{\mathcal{M}}_{g,n}$ -- arity $r$ means $n = r$ marked points. The relationship between "number of BPS constituents" and "number of marked points on a curve" is not explained in the note. If a 2-center bound state corresponds to arity 2, then yes, $\Theta^{\leq 2}_A$ jumps. But the claim in Section 6.1 is that $\Theta^{\leq 2}_A = \kappa$, the modular characteristic -- which is a tree-level (genus-zero) datum that should NOT depend on bound state formation.

Either the identification $\Theta^{\leq 2}_A = \kappa$ is wrong, or the example is wrong. They are inconsistent.

### What is needed

Clarify the relationship between arity and BPS constituents. If the arity-$r$ piece of $\Theta_A$ encodes $r$-center BPS states, then $\Theta^{\leq 2}_A \neq \kappa$ (it also includes 2-center data). If $\Theta^{\leq 2}_A = \kappa$, then the conifold jump must appear at arity 3 or higher, and the example must be corrected.

---

## Summary Table

| # | Finding | Severity | Type | Action |
|---|---------|----------|------|--------|
| 1 | Symplectomorphism vs. gauge transformation mismatch | HIGH | Genuine gap | Construct explicit Lie algebra map or demote to conjecture |
| 2 | Ordering problem + convergence of infinite BCH | HIGH | Genuine gap | Specify topology, prove convergence, clarify ordering dependence |
| 3 | Gauge invariance of denominator in curved setting | MED-HIGH | Missing proof | Cite/prove curved $L_\infty$ gauge invariance theorem |
| 4 | Attractor mechanism for multi-center states | MED | Overclaim | Delineate domain of validity, fix circular Q1/assertion |
| 5 | Computability of gauge-invariant MC element | MED | Conceptual gap | Acknowledge non-computability, qualify RG analogy |
| 6 | Theorem 3.5 proof is tautological/circular | MED | Circular reasoning | Restructure as research programme, not proved theorem |
| 7 | Conifold example inconsistent with arity identification | LOW | Expository error | Clarify arity vs. constituent count |

---

## Overall Assessment

The note presents a beautiful and physically well-motivated *analogy* between KS wall-crossing and MC gauge equivalence. As a physics note signposting future mathematical development, it is valuable. But it consistently presents conjectural identifications as established facts, proof strategies as proofs, and analogies as theorems.

The two HIGH-severity findings (1 and 2) identify genuine mathematical gaps that are not merely "details to be filled in later" -- they concern the fundamental algebraic compatibility between the KS formalism (symplectomorphisms of a Poisson algebra, with ordering) and the MC formalism (gauge transformations of an $L_\infty$-algebra, without ordering). Resolving these requires constructing a specific map with specific properties, and it is not clear that such a map exists for the curved $L_\infty$-structure in question.

Recommendation: The note should be reframed as a *conjecture note* rather than an expository proof. The central claim should be stated as a precise conjecture (with all the conditions from Findings 1-3 as hypotheses), the attractor interpretation should be flagged as heuristic for multi-center states, and the computational implications should be honestly assessed.
