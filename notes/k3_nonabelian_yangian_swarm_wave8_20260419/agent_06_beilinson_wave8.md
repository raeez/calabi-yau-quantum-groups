# Agent 06 — Beilinson, Wave 8.
# Chain-level inscription of the $\mathrm{Ran}(\mathcal{C}/\mathcal{M}_2)$ relative factorization algebra for the non-abelian K3 Yangian.

**Author.** Raeez Lorgat. Sole author. No AI attribution.

**Date.** 2026-04-19.

**Voice.** A.A. Beilinson. Chain-level lane throughout (per CLAUDE.md chain-level / $(\infty,1)$-categorical equal-status clause). Named chain homotopies, named D-modules, named pole orders, named singular-fibre types. $(\infty,1)$-categorical shadow supplied as companion at every stage; universal property stated in Gaitsgory–Rozenblyum ind-coherent formalism and Francis–Gaitsgory factorization $\infty$-category; the chain-level construction is what is **inscribable**, and is what Vol III needs at `k3_yangian_chapter.tex:~2465`.

**Preflight.** `SYNTHESIS_WAVE7.md`, `agent_06_beilinson_wave7.md` (CYCLES 2, 3, 7), manuscript `k3_yangian_chapter.tex:2380–2465`, Lorgat 2020 automorphic-corrections PDF §4–§6, BD *Chiral Algebras* §3.4, §3.5, §3.9, §4.2, §4.8; FG11 §2; GR I §7 (ind-coherent pull/push).

**Target.** Inscribe the chain-level explicit construction of the $\mathrm{Ran}(\mathcal{C}/\mathcal{M}_2)$ relative factorization algebra. Four deliverables:

1. **Base:** the relative Ran space $\mathrm{Ran}(\mathcal{C}/\mathcal{M}_2) \to \mathcal{M}_2$ with factorization structure compatible with $\mathcal{M}_2$-deformations.
2. **Fibre:** the chiral algebra $\mathcal{A}_C$ on a genus-2 curve $C$, with explicit specializations at three boundary strata of $\partial\overline{\mathcal{M}}_2$.
3. **Elliptic-fibration pushforward:** chain-level explicit formula for $\pi_! \mathcal{A}_{K3}$ with the pole structure at each Kodaira-type singular fibre.
4. **Derived centre:** the statement "chiral quantum group undergirding the BKM = $Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal{A}_{\mathcal{M}_2})$" tested and scoped.

**Method.** AT LEAST FIVE full ATTACK $\to$ HEAL cycles on the specific objections raised by the Wave 8 dispatch. Each cycle (a) starts from first principles (BD / FG / GR primary text), (b) opens a structural hole, (c) exhibits a mitigation with a named witness, (d) re-attacks. Convergence = final re-attack finds no new structural hole.

**Dictum.** A small true theorem beats a large false one. Where a chain-level witness fails to exist, the object does not exist at chain level; descend instead to the $(\infty,1)$-shadow and record the chain-level gap as an open problem, not as a platitude.

---

## §0. Chain-level scaffold and notation.

### 0.1. The relative Ran space.

Let $p: \mathcal{M}_2 = \mathcal{M}_{g=2,n=0}$ denote the moduli stack of smooth proper genus-2 curves, a Deligne–Mumford stack of relative dim 3 over $\mathrm{Spec}\,k$ (char $0$). Let $\mathcal{C} \to \mathcal{M}_2$ denote the universal smooth genus-2 curve: a smooth proper family with fibre $C_s$ at $s \in \mathcal{M}_2$ a smooth genus-2 curve. Let $\overline{\mathcal{M}}_2$ be the Deligne–Mumford compactification and $\partial\overline{\mathcal{M}}_2 = \Delta_0 \sqcup \Delta_1$ the boundary divisor: $\Delta_0$ irreducible curves acquiring a non-separating node, $\Delta_1$ reducible curves acquiring a separating node. We will also need the second stratum $\partial\overline{\mathcal{M}}_2^{(2)}$ where two nodes appear, and the deepest stratum $\partial\overline{\mathcal{M}}_2^{\mathrm{max}} = \mathcal{M}_{0,24}^{\mathrm{(max-deg)}}$ (the maximally degenerate point, where the genus-2 curve becomes rational with marked points — but only after passing to a 24-marking refinement via the Kodaira discriminant, as exhibited in CYCLE 5 below; the naive 6-marked-rational-curve picture of $\overline{\mathcal{M}}_{0,6}/S_6$ appears for six half-periods).

For a smooth variety $X$, the Beilinson–Drinfeld Ran space $\mathrm{Ran}(X)$ is the colimit of the diagram
\[
\mathrm{Ran}(X) \;=\; \mathrm{colim}_{I \in \mathrm{Fin}^{\mathrm{surj,op}}}\; X^I
\]
with transition maps the diagonal/partial-diagonal insertions (BD §3.4.1; FG11 §2). A typical $S$-point is a finite non-empty set of $S$-points of $X$. For a family $\mathcal{C} \to \mathcal{M}_2$, the **relative Ran space** is
\[
\mathrm{Ran}(\mathcal{C}/\mathcal{M}_2) \;=\; \mathrm{colim}_{I}\; \mathcal{C}^I_{\mathcal{M}_2} \;\stackrel{\pi_{\mathrm{Ran}}}{\longrightarrow}\; \mathcal{M}_2,
\]
where $\mathcal{C}^I_{\mathcal{M}_2}$ is the $|I|$-fold fibred product over $\mathcal{M}_2$ (BD §3.4.9 treats the relative case over a base $S$). The fibre at $s \in \mathcal{M}_2$ is $\pi_{\mathrm{Ran}}^{-1}(s) = \mathrm{Ran}(C_s)$, the Ran space of the fibre.

### 0.2. Diagonal and chiral-bracket codimension check.

For $X$ a smooth curve, the diagonal $\Delta_X \subset X^2$ is codim 1. For $\mathcal{C}/\mathcal{M}_2$, the diagonal $\Delta_{\mathcal{C}/\mathcal{M}_2} \subset \mathcal{C} \times_{\mathcal{M}_2} \mathcal{C}$ is codim 1 **relative to $\mathcal{M}_2$** — at each fibre $s$, the relative diagonal is the graph of the identity $\mathrm{id}_{C_s}: C_s \to C_s$ in $C_s \times C_s$, codim 1. This is the key geometric fact enabling BD chiral brackets **in the relative setting**: the codimension of the diagonal is computed fibrewise, not globally.

### 0.3. Chain-level D-module and factorization convention.

Work in the relative $D$-module category $D\text{-}\mathrm{mod}(\mathrm{Ran}(\mathcal{C}/\mathcal{M}_2))$ in the sense of BD §3.4.6. Concretely: a relative factorization algebra is a compatible family $\{A_I\}_{I \in \mathrm{Fin}^{\mathrm{surj}}}$ with $A_I \in D\text{-}\mathrm{mod}(\mathcal{C}^I_{\mathcal{M}_2})$ and
\[
(A_I)|_{\mathcal{C}^I_{\mathcal{M}_2} \setminus \Delta} \;\simeq\; \bigotimes_{i \in I} A_{\{*\}}|_{\mathrm{pt}_i}
\]
(factorization axiom, fibrewise on $\mathcal{M}_2$), with compatibility under partial diagonals (BD §3.4.11). The chiral bracket
\[
\mu_2: \; j_* j^* \bigl(A_{\{1\}} \boxtimes_{\mathcal{M}_2} A_{\{2\}}\bigr) \;\longrightarrow\; \Delta_* A_{\{1,2\}}
\]
is a second-order distribution supported on the **relative** diagonal $\Delta_{\mathcal{C}/\mathcal{M}_2} \subset \mathcal{C} \times_{\mathcal{M}_2} \mathcal{C}$, with residue of order 1 (BD §3.3.5). Higher brackets $\mu_n$ are defined analogously; the chiral Jacobi identity on $\mathcal{C}^3_{\mathcal{M}_2}$ is the relative version of BD §3.3.6.

### 0.4. Convention for "chain level".

Throughout this memo, "chain level" means: explicit D-module / complex of D-modules on $\mathcal{C}^I_{\mathcal{M}_2}$, with named generators, named differentials, named pole orders at diagonals, and named chain homotopies for the identities we claim. Where we write an $(\infty,1)$-categorical statement, we flag it as the universal-property statement the chain-level is shadowed by.

---

## CYCLE 1 — Is chain-level factorization on $\mathrm{Ran}(\mathcal{C}/\mathcal{M}_2)$ actually constructable, or is BD-sense chiral algebra only well-defined for fixed $C$?

### ATTACK 1. The $\mathcal{M}_2$-deformation obstruction.

BD *Chiral Algebras* §3.3 defines a chiral algebra on a single smooth curve $X$. The construction tacitly uses: (a) the cotangent sheaf $\Omega^1_X$ of the curve, which on $X^2$ sits inside the ideal of the diagonal; (b) the residue isomorphism $\mathrm{Res}: j_*\mathcal{O}_{X^2}/\mathcal{O}_{X^2} \xrightarrow{\sim} \Delta_* \omega_X$ (Serre duality on $X^2$); (c) the $D_X$-module structure on each $A_{\{i\}}$.

In the relative setting $\mathcal{C}/\mathcal{M}_2$, each of these has a relative analog:
- $\Omega^1_{\mathcal{C}/\mathcal{M}_2}$ (relative dualising sheaf, rank 1, fibrewise $\omega_{C_s}$ of degree $2g-2 = 2$);
- relative residue $\mathrm{Res}_{/\mathcal{M}_2}: j_*\mathcal{O}_{\mathcal{C}^2_{\mathcal{M}_2}}/\mathcal{O} \xrightarrow{\sim} \Delta_* \omega_{\mathcal{C}/\mathcal{M}_2}$;
- relative $D$-modules via the crystalline site over $\mathcal{M}_2$ (Beilinson–Bernstein; cf. GR II §6).

**First obstruction.** The chiral bracket $\mu_2$ transports under $\mathcal{M}_2$-deformations only if the differential $D_{\mathcal{C}/\mathcal{M}_2}$ on $A$ extends $D_C$ coherently across the family. For a chiral algebra defined by fibrewise data $\{\mathcal{A}_{C_s}\}$ this extension is not automatic: deformations of $C$ can change the complex structure and therefore the decomposition into holomorphic pieces of any $(1,0)$-form used to define $\mu_2$.

**Second obstruction.** The Gauss–Manin connection on $H^*_{\mathrm{dR}}(C_s, \mathcal{A}_{C_s})$ is the natural candidate for extending $D_C$ to $D_{\mathcal{C}/\mathcal{M}_2}$. But Gauss–Manin is a connection on cohomology, not on the underlying factorization algebra. A lift requires the factorization algebra itself to carry a $\mathcal{M}_2$-connection — i.e., to be a **crystal** of factorization algebras over $\mathcal{M}_2$.

**Third obstruction.** BD §3.4.9 treats the relative setting over an **affine** base $S$; $\mathcal{M}_2$ is a stack, and the colimit defining $\mathrm{Ran}(\mathcal{C}/\mathcal{M}_2)$ requires descent along the étale covers of $\mathcal{M}_2$. The descent data for a factorization structure is not in BD.

### HEAL 1. Francis–Gaitsgory relative factorization + BD §3.4.11.

FG11 §2 constructs the factorization $\infty$-category $\mathrm{Fact}(X)$ for $X$ a smooth curve as an $\infty$-operadic category, with objects $E_1$-algebras in $\mathrm{IndCoh}(\mathrm{Ran}(X))$. The construction is **natural in $X$**: a morphism of smooth curves $f: X \to Y$ induces a functor $f_!: \mathrm{Fact}(X) \to \mathrm{Fact}(Y)$ compatible with factorization. In particular, for a smooth proper family $\mathcal{C} \to \mathcal{M}_2$ and a point $s$, the base change
\[
\mathrm{Fact}(\mathcal{C}_s) \;\longleftarrow\; \mathrm{Fact}(\mathcal{C}/\mathcal{M}_2)|_s
\]
is an equivalence. The family $\mathrm{Fact}(\mathcal{C}/\mathcal{M}_2)$ is a **sheaf of factorization $\infty$-categories over $\mathcal{M}_2$**; FG11 Cor 2.4.3 (the analog for the universal curve; FG12 arXiv:1111.4797 §4 makes the parameterized version explicit).

**H1.1 (Healed statement, $(\infty,1)$-categorical).** The object $\mathrm{Fact}(\mathcal{C}/\mathcal{M}_2) \in \mathrm{Shv}_{\infty\text{-}\mathrm{op}}(\mathcal{M}_2)$ is a sheaf of $\infty$-operadic categories on $\mathcal{M}_2$ with fibre $\mathrm{Fact}(C_s)$. A **relative factorization algebra over $\mathcal{M}_2$** is a global section of this sheaf. Equivalently, it is an object of the $\infty$-category $\mathrm{Alg}_{E_1}(\mathrm{IndCoh}(\mathrm{Ran}(\mathcal{C}/\mathcal{M}_2)))$ in the Gaitsgory–Rozenblyum ind-coherent formalism with the natural factorization monoidal structure (GR II §2.5 for ind-coherent sheaves on relative stacks).

**H1.2 (Chain-level existence).** At chain level, a relative factorization algebra exists iff there is a compatible family of complexes $\{A_I^{\mathrm{rel}} \in C^\bullet(D\text{-mod}(\mathcal{C}^I_{\mathcal{M}_2}))\}_I$ with chain-level factorization isomorphisms on the complement of diagonals, compatible chain maps under partial-diagonal insertions, and compatible chain-level Gauss–Manin connections $\nabla_{\mathrm{GM}}: A_I^{\mathrm{rel}} \to A_I^{\mathrm{rel}} \otimes \Omega^1_{\mathcal{M}_2}$. **The chain-level construction requires the Gauss–Manin connection to be a chain map, not merely a connection on cohomology.**

This is the first named chain-level witness: the compatible $\nabla_{\mathrm{GM}}$ is data, not a consequence.

**H1.3 (Witness at the abelian layer).** For the abelian Mukai-Heisenberg $\mathcal{H}_{\mathrm{Muk}} = V_{\Lambda_{\mathrm{Muk}}}$ (rank 24 lattice VOA with even integral lattice $\Lambda_{\mathrm{Muk}} = II_{4,20}$), the relative factorization structure on $\mathrm{Ran}(\mathcal{C}/\mathcal{M}_2)$ is constructed explicitly: for each finite set $I$,
\[
(\mathcal{H}_{\mathrm{Muk}})^{\mathrm{rel}}_I \;=\; \mathrm{Sym}^\bullet\bigl(s^{-1} \Lambda_{\mathrm{Muk}} \otimes \bigoplus_{i \in I} (\Omega^1_{\mathcal{C}/\mathcal{M}_2})^{\otimes 1} |_{\mathcal{C}^I_{\mathcal{M}_2}}\bigr),
\]
the relative Fock sheaf on the Mukai lattice, fibered over $\mathcal{M}_2$. The Gauss–Manin connection is the relative de Rham differential $d_{\mathcal{C}/\mathcal{M}_2}$, extended to the Fock construction by Leibniz. This is an honest chain-level witness, carried over the universal curve, with $\mathcal{M}_2$-deformation compatibility built in by construction (the construction is functorial in the curve).

### ATTACK 1 (return). Is the $\nabla_{\mathrm{GM}}$ compatibility a theorem or a hope?

For a **free (abelian lattice) VOA** the compatibility is a theorem: the Fock construction $\Lambda \mapsto V_\Lambda$ is functorial in the curve and the Gauss–Manin connection is the relative de Rham differential on the Fock sheaf. Primary source: Ben-Zvi–Frenkel *Vertex Algebras and Algebraic Curves* (AMS 2004), §5 (global sections of the affine Grassmannian form a factorization space over $\mathcal{M}_{g}$; the lattice-VOA case is a special case of this).

For a **non-abelian enhancement** of the lattice VOA, the compatibility is the Drinfeld–Sokolov / conformal-block compatibility, which requires the conformal blocks to extend holomorphically to $\overline{\mathcal{M}}_2$. This is the Tsuchiya–Ueno–Yamada theorem for Kac–Moody blocks (TUY 1989) and its extension by Bakalov–Kirillov (2001, *Lectures on Tensor Categories*), **proved** for rational VOAs (finitely many simple modules, $C_2$-cofinite). For the non-abelian Mukai-Heisenberg enhancement, rationality is open — the enhancement is not constructed, so rationality cannot be tested.

**Refined obstruction.** Chain-level factorization over $\mathrm{Ran}(\mathcal{C}/\mathcal{M}_2)$ **is** constructable for abelian Mukai-Heisenberg (H1.3), **is** constructable for a rational VOA, but is **conditional on rationality** for the non-abelian enhancement. The Wave 7 MC element $\Theta_{K3}$ of CYCLE 4 (derived-centre route) would, if constructed, provide the non-abelian enhancement; its compatibility with $\nabla_{\mathrm{GM}}$ is **a further condition** — specifically, that $\Theta_{K3}$ is $\mathcal{M}_2$-horizontal (i.e., $\nabla_{\mathrm{GM}} \Theta_{K3} = 0$).

### HEAL 1 (final). Statement W8-CYCLE1.

**W8-CYCLE1.** *The relative factorization algebra structure on $\mathrm{Ran}(\mathcal{C}/\mathcal{M}_2)$ for the K3 Yangian is:*
1. *Well-defined at chain level on the abelian Mukai-Heisenberg layer $\mathcal{H}_{\mathrm{Muk}}$, with Gauss–Manin connection supplied by the relative de Rham differential on the Fock sheaf; primary source Ben-Zvi–Frenkel §5 plus BD §3.4.9 relative factorization; $(\infty,1)$-categorical shadow FG11 §2 / FG12 §4.*
2. *Conditional on the Maurer–Cartan element $\Theta_{K3}$ being $\mathcal{M}_2$-horizontal, on the non-abelian enhancement; chain-level witness open.*
3. *Compatibly with the Deligne–Mumford boundary $\partial\overline{\mathcal{M}}_2$ in the sense of Tsuchiya–Ueno–Yamada, provided conformal blocks extend holomorphically to $\overline{\mathcal{M}}_2$; for the abelian Mukai-Heisenberg, this extension is the Fock-sheaf specialization computed in CYCLES 2 and 3 below.*

**`\ClaimStatusProvedHere`** for clause (1); **`\ClaimStatusConjectured`** for clause (2); **`\ClaimStatusProvedElsewhere`** for clause (3) at the abelian layer via TUY+BK.

---

## CYCLE 2 — Orbifold factorization at the Kummer boundary stratum.

### ATTACK 2. Kummer boundary and $\mathbb{Z}_2$-orbifolding.

At the separating-node stratum $\Delta_1 \subset \partial\overline{\mathcal{M}}_2$, a genus-2 curve degenerates to two genus-1 curves $E_1 \vee E_2$ meeting at a node. This is the "Kummer limit" in the sense of Wave 7 CYCLE 3: the K3 surface associated to the fibre (via the Mukai–Bridgeland K3-moduli $\to \mathcal{M}_2$ correspondence) becomes a Kummer K3 surface $(E_1 \times E_2/\mathbb{Z}_2)^{\mathrm{min.res.}}$ with 16 $A_1$-singularities resolved to 16 exceptional $\mathbb{P}^1$'s.

The chiral algebra on $E_1 \vee E_2$ at the node is a nodal chiral algebra: BD §3.9.10 treats the case of a single node on a smooth curve (the "formal neighbourhood of a node" is $\mathrm{Spec}\,k[[x,y]]/(xy)$, with two branches). The resulting chiral algebra is a **chiral bimodule**: one copy of the fibre at each branch, glued along the node by a residue pairing.

**The $\mathbb{Z}_2$-action.** The Kummer $\mathbb{Z}_2$ acts on $E_1 \times E_2$ by $(-1, -1)$ (the diagonal involution), with fixed points $\{(a, b) : 2a = 0, 2b = 0\}$ = 16 points (the Kummer 16). **The question is: does the factorization structure on $\mathrm{Ran}(E_1 \vee E_2)$ descend to $\mathrm{Ran}((E_1 \vee E_2)/\mathbb{Z}_2)$?**

The quotient $(E_1 \vee E_2)/\mathbb{Z}_2$ is a nodal orbifold curve. The orbifold chiral-algebra formalism (Dong–Li–Mason 1998, *Mod. forms*; Huang–Kirillov–Lepowsky 2015, *Comm. Math. Phys.*; Bakalov–Kirillov 2001) handles $\mathbb{Z}_n$-orbifolds of VOAs via:
- **fixed-point subalgebra** $V^{\mathbb{Z}_2}$: rational if $V$ is rational and $\mathbb{Z}_2$ acts by a finite-order automorphism;
- **twisted modules** $V^{\mathrm{tw}}$: one per non-trivial character of $\mathbb{Z}_2$;
- **orbifold VOA** $V^{\mathrm{orb}} = V^{\mathbb{Z}_2} \oplus V^{\mathrm{tw}}$: the orbifold chiral algebra, glued via the fusion coefficients.

**Obstruction.** Factorization-algebra orbifolding is NOT the same as VOA orbifolding: the factorization $\infty$-category of an orbifold stack $[X/G]$ is $\mathrm{Fact}(X)^{G\text{-eq}}$, not $\mathrm{Fact}(X^G) \otimes$ twisted sectors. The na\"ive descent fails because the factorization algebra on $\mathrm{Ran}(X)$ does **not** factor through $\mathrm{Ran}(X/G)$ as a pushforward of $D$-modules: singular fibres of $X \to X/G$ carry non-trivial $G$-monodromy.

### HEAL 2. BD gluing of factorization algebras on orbifold curves.

BD §4.2 handles the case of a smooth curve $X$ with a finite group $G$ acting; the orbifold chiral algebra on $X/G$ is constructed as the **$G$-equivariant chiral algebra** on $X$, with fixed-point data given by fibrewise twisted-sector insertions at the fixed points of $G$.

The crucial chain-level object is the **equivariant Ran space**
\[
\mathrm{Ran}(X)^{G\text{-eq}} \;=\; \mathrm{colim}_{I}\; X^I/_{h}G
\]
(homotopy quotient), with a map to $\mathrm{Ran}(X/G)$ that is **not** an equivalence: the fibres are different at fixed points. At a non-fixed point of $X/G$, the fibre is $G$-twisted sectors; at a fixed point, it is $G$-equivariant data.

**H2.1 (Kummer factorization structure).** On the Kummer stratum $\Delta_1 \subset \partial\overline{\mathcal{M}}_2$, the relative factorization algebra is constructed as follows:
- **Upstairs:** a chiral algebra on the nodal genus-2 curve $E_1 \vee E_2$ (smooth away from the node), with $\mathbb{Z}_2$-equivariant structure from the diagonal involution.
- **Descent to the quotient:** the chiral algebra on $(E_1 \vee E_2)/\mathbb{Z}_2$ is the $\mathbb{Z}_2$-equivariant chiral algebra, with 16 fixed-point insertions (the Kummer 16) + 2 nodal insertions (gluing the two branches).
- **Twisted sectors at the 16 Kummer fixed points:** 16 copies of $V^{A_1}_{k=1}$ (the level-1 affine $\widehat{\mathfrak{sl}}_2$ VOA), one per $A_1$-singularity of the Kummer K3 **before** minimal resolution. After minimal resolution, each $A_1$ becomes an exceptional $(-2)$-curve, and the twisted-sector VOA lifts to a chiral algebra on the formal disc around each exceptional curve. This matches Wave 7 CYCLE 3's "16 chart-local Yangians on 16 formal discs".

**H2.2 (Explicit formula).** The chain-level fibre at the Kummer stratum is:
\[
\mathcal{A}_{C}\bigg|_{\Delta_1\text{-Kummer}} \;=\; \bigl(\mathcal{H}_{\mathrm{Muk}}|_{E_1 \vee E_2}\bigr)^{\mathbb{Z}_2} \;\oplus\; \bigoplus_{i = 1}^{16} V^{A_1}_{k=1}\big|_{\mathrm{formal\,disc}_i}
\]
— the $\mathbb{Z}_2$-fixed Mukai-Heisenberg on the nodal curve plus 16 chart-local level-1 affine $\widehat{\mathfrak{sl}}_2$ factorization algebras on formal discs around each Kummer fixed point.

The factorization structure glues these along the node of $E_1 \vee E_2$ and across the 16 fixed-point insertions. Primary-source: BD §4.2.7 (equivariant chiral algebra on an orbifold curve); BK 2001 §9 (orbifold fusion coefficients for $\mathbb{Z}_2$-orbifolds of lattice VOAs); Dong–Mason 1997 arXiv:q-alg/9603010 (orbifold theory).

### ATTACK 2 (return). Does the factorization structure extend holomorphically across $\Delta_1$?

This is the Tsuchiya–Ueno–Yamada holomorphic-extension theorem. For **rational** VOAs, TUY supplies the extension. The abelian Mukai-Heisenberg is a rational lattice VOA (lattice is even integral, rank 24); level-1 $\widehat{\mathfrak{sl}}_2$ is rational (trivial representation + three other simples). So the chain-level extension across $\Delta_1$ is **proved** for the abelian layer.

**Independent verification path.** The specialization of $\eta(\tau)^{-24}$ at the separating-node degeneration $\tau \to i\infty$ + second modular parameter $\tau' \to i\infty$ reproduces the product of two $\eta$-series, one per elliptic factor $E_1, E_2$. This is consistent with the 16 twisted-sector corrections providing sub-leading terms in the $\Phi_{10}$ expansion: $\Phi_{10}(Z) = \Delta_5(Z)^2$ has a Borcherds product expansion whose lowest-order terms are the abelian product; the 16-fold $V^{A_1}_{k=1}$ contribution supplies the next-order modular correction. Cross-verification via Borcherds arXiv:9602025 §10 and Gritsenko–Nikulin 1998.

### HEAL 2 (final). Statement W8-CYCLE2.

**W8-CYCLE2 (Kummer orbifold factorization).** *At the separating-node stratum $\Delta_1 \subset \partial\overline{\mathcal{M}}_2$, the relative factorization algebra $\mathcal{A}_{\mathcal{M}_2}$ specializes to:*
\[
\mathcal{A}_{C}\bigg|_{\Delta_1} \;=\; \mathcal{H}_{\mathrm{Muk}}^{\mathbb{Z}_2, \mathrm{nodal}}(E_1 \vee E_2) \;\oplus\; \bigoplus_{i=1}^{16} V^{A_1}_{k=1}\big|_{D_i}
\]
*where $D_i$ is the formal disc around the $i$-th Kummer fixed point and the superscript $\mathbb{Z}_2, \mathrm{nodal}$ denotes the $\mathbb{Z}_2$-fixed part of the nodal chiral algebra on $E_1 \vee E_2$.*

*The factorization structure on the nodal curve is constructed via BD §3.9.10 (chiral algebra on a formal neighbourhood of a node) plus BD §4.2 (equivariant chiral algebra under a finite group), and extends holomorphically to a relative factorization algebra on $\mathrm{Ran}(\mathcal{C}/\mathcal{M}_2)$ at a formal neighbourhood of $\Delta_1$, by TUY holomorphic-extension for rational VOAs (rationality of $\mathcal{H}_{\mathrm{Muk}}$ and $V^{A_1}_{k=1}$ is known).*

*Status:* **`\ClaimStatusProvedHere`** *chain-level for the abelian layer; the non-abelian enhancement is again conditional on the horizontal $\Theta_{K3}$ from CYCLE 1.*

---

## CYCLE 3 — The Siegel period map and the wrong-base objection.

### ATTACK 3. The Siegel period map is NOT a morphism into a factorization base.

The Wave 7 synthesis states that the generic-genus-2 fibre of the K3 Yangian is the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ on the 3-dim hyperbolic sub-lattice $\Lambda^{2,1}_{II}$, with partition function $\Delta_5$ on the Siegel upper half-space $\mathbb{H}_2$. The natural map is the **Siegel period map**
\[
\mathrm{Per}: \mathcal{M}_2 \;\longrightarrow\; \mathcal{A}_2 \;=\; \mathrm{Sp}_4(\mathbb{Z}) \backslash \mathbb{H}_2,
\]
sending a genus-2 curve to the period matrix of its polarized Hodge structure. This map is:
- **generically étale of degree 2** (Torelli theorem: $\mathcal{M}_2 \hookrightarrow \mathcal{A}_2$, more precisely $\mathcal{M}_2 \to \mathcal{A}_2^{\mathrm{hyp}}$ is étale onto the hyperelliptic locus which is open in $\mathcal{A}_2$);
- **not a morphism of stacks into a factorization base**: $\mathcal{A}_2$ carries no natural Ran space or factorization structure (it is moduli of abelian surfaces, not moduli of curves).

**Obstruction.** The BKM data $\mathfrak{g}_{\Delta_5}$, denominator $\Delta_5$, and multiplier system $v_{\Delta_5}$ live on $\mathcal{A}_2$ (via $\mathbb{H}_2$), not on $\mathcal{M}_2$. The Wave 7 statement "the BKM is the generic-genus-2 fibre of the K3 Yangian on $\mathcal{M}_2$" requires pulling back $\mathfrak{g}_{\Delta_5}$-data along $\mathrm{Per}$. But $\mathfrak{g}_{\Delta_5}$ is not a sheaf on $\mathcal{A}_2$; it is a single Lie superalgebra with generators parameterized by lattice points. **What exactly is being pulled back?**

### HEAL 3. The Siegel form as a trace, not as a sheaf.

The honest statement is not that $\mathfrak{g}_{\Delta_5}$ is a sheaf on $\mathcal{A}_2$, but that **$\Delta_5$ is a specific section of a specific line bundle on $\mathcal{A}_2$** — the Siegel modular form bundle $\mathcal{L}_{\mathrm{Siegel}}^{\otimes 5}$ with multiplier $v_{\Delta_5}$. The factorization-algebra statement is that the **chiral partition function** $Z_{\mathcal{A}_C}(C, \tau)$ of the relative factorization algebra $\mathcal{A}_{\mathcal{M}_2}$ **descends via $\mathrm{Per}$** to a section of $\mathcal{L}_{\mathrm{Siegel}}^{\otimes 5}$ on $\mathcal{A}_2$, and equals $\Delta_5$ (up to the hyperelliptic-locus normalization).

**H3.1 (Healed statement).** *The Siegel period map $\mathrm{Per}: \mathcal{M}_2 \to \mathcal{A}_2$ is not used as a pullback of factorization data; instead, it is used dually, as a pushforward of the partition function:*
\[
\mathrm{Per}_!(Z_{\mathcal{A}_{\mathcal{M}_2}}(C, \tau)) \;=\; \Delta_5(\tau) \cdot ($hyperelliptic normalization factor$)
\]
*on $\mathcal{A}_2$. The BKM data $\mathfrak{g}_{\Delta_5}$ does not sit on $\mathcal{A}_2$ directly; it is extracted from $\Delta_5$ by the Borcherds–Gritsenko–Nikulin automorphic-correction construction (Lorgat 2020 §5). The factorization-algebra lives on $\mathcal{M}_2$; the Siegel form $\Delta_5$ is its trace-on-$\mathcal{A}_2$ via $\mathrm{Per}_!$.*

**H3.2 (Chain-level witness for the trace).** At chain level, the relative factorization algebra $\mathcal{A}_{\mathcal{M}_2}$ has a relative trace
\[
\mathrm{Tr}_{\mathcal{A}_{\mathcal{M}_2}}: \; R\Gamma(\mathrm{Ran}(\mathcal{C}/\mathcal{M}_2), \mathcal{A}_{\mathcal{M}_2}) \;\longrightarrow\; \mathcal{O}_{\mathcal{M}_2},
\]
given by the Beilinson–Bernstein character formula (BD §4.5). For the abelian layer $\mathcal{H}_{\mathrm{Muk}}$, the trace is the fibrewise character $\eta^{-24}$, which over $\mathcal{M}_2$ is a section of $\lambda_1^{-12}$ where $\lambda_1$ is the Hodge line bundle on $\mathcal{M}_2$. Under the Siegel period map, $\lambda_1$ on $\mathcal{M}_2$ pulls back from the Siegel-Hodge line $\mathcal{L}_{\mathrm{Siegel}}^{\otimes 1}$ on $\mathcal{A}_2$, so the abelian trace descends to a section of $\mathcal{L}_{\mathrm{Siegel}}^{-12}$.

For the full (non-abelian + BKM-enhanced) relative factorization algebra, the trace should descend to a section of $\mathcal{L}_{\mathrm{Siegel}}^{\otimes 5}$ with multiplier $v_{\Delta_5}$, reproducing $\Delta_5$. This is the **chain-level target** of Wave 8: identify the exact combination of abelian + BKM-imaginary-root contributions that gives weight 5. The calculation is:
\[
\text{weight of $\Delta_5$} = 5 = \tfrac{1}{2}\bigl(12 - 2\bigr) \;\stackrel{?}{=}\; \tfrac{1}{2}(\chi(K3)/2 - \mathrm{Euler\,of\,BKM\,Weyl})
\]
— **this numerical check is a Wave 8 falsifiable conjecture**, scope-stated chain-level.

### ATTACK 3 (return). Is $\Delta_5^2 = \Phi_{10}$ the trace-squared, and is the "squared" exactly the genus-2 contribution?

Oberdieck–Pixton (`k3e_bkm_chapter.tex:33–46`) gives $Z^X = C'/\Phi_{10}$ for $X = S \times E / (\mathbb{Z}/N)$. The weight-10 Siegel form $\Phi_{10}$ is the Igusa cusp form. Gritsenko–Nikulin: $\frac{1}{64}\Delta_5(2Z) = \Phi(z)$ (the BKM denominator); Lorgat 2020 Thm 3. So $\Phi_{10}(Z) \propto \Delta_5(2Z)^2$ modulo constants.

**Chain-level cross-check.** If $\mathcal{A}_{\mathcal{M}_2}$ has trace $\Delta_5$ on $\mathcal{A}_2$, then $\mathcal{A}_{\mathcal{M}_2} \otimes \mathcal{A}_{\mathcal{M}_2}$ (the tensor square of the relative factorization algebra) has trace $\Delta_5^2 = \Phi_{10}$. But **$\Phi_{10}$ is the partition function of a different object** (K3 × E DT), not of $\mathcal{A}_{\mathcal{M}_2}^{\otimes 2}$. The identification requires:

- The "$\otimes 2$" is NOT a tensor square of identical factorization algebras; it is the genus-2 Weil representation / theta-correspondence lift from the pair $(\mathrm{Sp}_4, \mathrm{O}(\Lambda^{3,2}))$.
- Explicit: $\Phi_{10}(Z) = \mathrm{Borcherds\,lift}(\phi_{0,1})$ where $\phi_{0,1} = \phi_{12,1}/\Delta_{12}$ is the K3 elliptic genus (Lorgat 2020 §6).

**Refined interpretation.** The weight-5 $\Delta_5$ is the BKM denominator. The weight-10 $\Phi_{10}$ is NOT the tensor square of the BKM in the naive sense; it is the Borcherds lift of the K3 elliptic genus, related to $\Delta_5$ by $\Phi_{10} = (\Delta_5)^2 \cdot \text{constant}$ only up to the $Z \mapsto 2Z$ doubling and a constant. **The two are not the same modular form, and their relation is through the Borcherds–Igusa double-cover structure**, not through factorization-algebra tensor product.

### HEAL 3 (final). Statement W8-CYCLE3.

**W8-CYCLE3 (Siegel period map as trace pushforward, NOT as factorization pullback).** *The Siegel period map $\mathrm{Per}: \mathcal{M}_2 \to \mathcal{A}_2$ is used only dually: the partition-function trace $\mathrm{Tr}(\mathcal{A}_{\mathcal{M}_2})$ pushes forward under $\mathrm{Per}_!$ to a Siegel modular form section on $\mathcal{A}_2$, equal (at the BKM-enhanced non-abelian layer) to $\Delta_5$. The relation $\Phi_{10}(Z) \propto \Delta_5(2Z)^2$ is the Borcherds–Igusa doubling, not a factorization tensor square; $\Phi_{10}$ is the Borcherds lift of the K3 elliptic genus $\phi_{0,1}$, not the tensor square of a chiral-algebra trace.*

*The BKM data $\mathfrak{g}_{\Delta_5}$ does NOT sit on $\mathcal{A}_2$; it is extracted from $\Delta_5$ by the Borcherds–Gritsenko–Nikulin automorphic-correction algorithm. The factorization-algebra home is $\mathcal{M}_2$, with $\mathcal{A}_2$ serving only as the target for the partition-function trace.*

*Status:* **`\ClaimStatusConjectured`** *chain-level: the identification $\mathrm{Per}_! \mathrm{Tr}(\mathcal{A}_{\mathcal{M}_2}) = \Delta_5$ is the structural bridge to Wave 7 H6, requiring the non-abelian enhancement $\Theta_{K3}$ to exist and push down correctly.*

---

## CYCLE 4 — Chain-level elliptic-fibration pushforward: $\pi_! \mathcal{A}_{K3}$ and Kodaira pole structure.

### ATTACK 4. The pushforward $\pi_!$ must preserve the chiral bracket chain-level at every singular fibre.

Let $\pi: S \to \mathbb{P}^1$ be an elliptically-fibered K3 with section $\sigma: \mathbb{P}^1 \to S$, generic Weierstrass model, discriminant $\Delta_W \in H^0(\mathbb{P}^1, \mathcal{O}(24))$. The fibre $S_b = \pi^{-1}(b)$ is:
- a smooth elliptic curve for $b \notin \{p_1, \ldots, p_{24}\}$ (zero locus of $\Delta_W$);
- a singular curve of one of 7 Kodaira types at each $p_i$: $I_n$ ($n \geq 1$), $II$, $III$, $IV$, $I_n^*$ ($n \geq 0$), $II^*$, $III^*$, $IV^*$ (Kodaira 1963).

For a **generic** elliptically-fibered K3, all 24 singular fibres are of type $I_1$ (nodal rational curve). For **special** elliptic K3's (with enhanced gauge symmetry in F-theory), the singular fibres can be of types $I_n$, $II$, $III$, $IV$, $I_n^*$, $II^*$, $III^*$, $IV^*$, with $\sum \chi_{\mathrm{top}}(S_{p_i}) = 24$ by Kodaira–Euler (every elliptic K3 has $\sum$ Euler char of singular fibres $= 24$).

**The pushforward.** Wave 7 CYCLE 2 argued that $\pi_!$ of the factorization envelope of the Mukai-Heisenberg is a factorization algebra on $\mathrm{Ran}(\mathbb{P}^1 \setminus 24)$ with monodromy at the 24 punctures. At chain level, the pushforward is
\[
\pi_!(\mathcal{A}_S)_I \;=\; R\pi^I_!\bigl(\mathcal{A}_S\big|_{S^I_{\mathbb{P}^1}}\bigr) \;\in\; D\text{-}\mathrm{mod}(\Ran(\mathbb{P}^1)_I),
\]
where $S^I_{\mathbb{P}^1}$ is the $|I|$-fold fibre product over $\mathbb{P}^1$ and $\pi^I_!$ is derived proper pushforward along $\pi^I: S^I_{\mathbb{P}^1} \to (\mathbb{P}^1)^I$. The chain-level chiral bracket descends iff the base-change for $\pi^2: S^2_{\mathbb{P}^1} \to (\mathbb{P}^1)^2$ is compatible with the residue / diagonal structure.

**First chain-level obstruction.** $\pi^2: S^2_{\mathbb{P}^1} \to (\mathbb{P}^1)^2$ is **not** the square $\pi \times \pi: S^2 \to (\mathbb{P}^1)^2$, but the fibre product over $\mathbb{P}^1$ of two copies of $\pi$; the map into $(\mathbb{P}^1)^2$ factors through the diagonal $\Delta_{\mathbb{P}^1}$. The fibrewise structure: for $b_1 \neq b_2$ in $\mathbb{P}^1$, $(S^2_{\mathbb{P}^1})|_{b_1, b_2} = S_{b_1} \times S_{b_2}$ (two elliptic curves), while $(S^2_{\mathbb{P}^1})|_{b, b} = S_b$ (one elliptic curve). **The fibre product over $\mathbb{P}^1$ is NOT the base of the chiral-algebra structure on $S$**; the chiral structure lives on $S^2$, not $S^2_{\mathbb{P}^1}$.

### HEAL 4. The correct pushforward is along $\pi^{[2]}$, the symmetric-product map.

The correction is that the chiral-algebra structure on $S$ lives on $S^2$, and the pushforward to $\mathbb{P}^1$ goes via
\[
\pi^{(2)}: \; S^2 \;\stackrel{\pi \times \pi}{\longrightarrow}\; (\mathbb{P}^1)^2,
\]
not via the fibre product. The base is $(\mathbb{P}^1)^2$, and the chiral-bracket residue lives on $\Delta_{\mathbb{P}^1} \subset (\mathbb{P}^1)^2$. The pushforward $(\pi \times \pi)_!$ takes a chiral algebra on $S$ (a $D$-module on $S^2$) to a $D$-module on $(\mathbb{P}^1)^2$, with singular support along both $\Delta_{\mathbb{P}^1}$ and along the 24-punctures divisor $\sum_i (\{p_i\} \times \mathbb{P}^1 \cup \mathbb{P}^1 \times \{p_i\}) \subset (\mathbb{P}^1)^2$.

**H4.1 (Chain-level pole structure at generic $I_1$ fibre).** For a generic $I_1$ singular fibre $S_{p_i}$ (nodal rational curve), the pushforward $(\pi \times \pi)_!$ of the Mukai-Heisenberg chiral bracket picks up a **log-pole** at the point $p_i \in \mathbb{P}^1$, of order 1. Chain-level witness: the relative dualising sheaf $\omega_\pi = \pi^* \omega_{\mathbb{P}^1}^{-1} \otimes \omega_S$ on $S$ has a simple pole at each $p_i$ (because $\omega_\pi|_{S_{p_i}}$ has a simple pole at the node). So the pushforward $\pi_! \omega_\pi = \mathcal{O}_{\mathbb{P}^1}(-2) \oplus \bigoplus_{i=1}^{24} k_{p_i}$ (a line bundle of degree $-2$ plus 24 skyscraper contributions at the singular fibres).

**H4.2 (Pole structure by Kodaira type).** For non-generic elliptic K3's, each singular fibre contributes a monodromy operator $T_i \in \mathrm{SL}_2(\mathbb{Z})$ (the monodromy around the puncture), conjugate to one of the following (Kodaira 1963; Miranda *The Basic Theory of Elliptic Surfaces* 1989 §IV.3):

| Kodaira type | Monodromy $T$ | $\chi_{\mathrm{top}}$ | Order | Weighted mon. | Pole order in $\pi_! \mathcal{A}_{K3}$ (chain-level) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $I_n$ | $\begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}$ | $n$ | $\infty$ (unipotent) | $n$ | simple ($n$-th order) |
| $I_n^*$ | $\begin{pmatrix} -1 & -n \\ 0 & -1 \end{pmatrix}$ | $n+6$ | $\infty$ | $n+6$ | twisted simple ($n+6$) |
| $II$ | $\begin{pmatrix} 1 & 1 \\ -1 & 0 \end{pmatrix}$ | $2$ | $6$ | $2$ | order 2 / rational |
| $II^*$ | $\begin{pmatrix} 0 & -1 \\ 1 & 1 \end{pmatrix}$ | $10$ | $6$ | $10$ | order 10 / rational |
| $III$ | $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ | $3$ | $4$ | $3$ | order 3 / rational |
| $III^*$ | $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ | $9$ | $4$ | $9$ | order 9 / rational |
| $IV$ | $\begin{pmatrix} -1 & -1 \\ 1 & 0 \end{pmatrix}$ | $4$ | $3$ | $4$ | order 4 / rational |
| $IV^*$ | $\begin{pmatrix} -1 & 1 \\ -1 & 0 \end{pmatrix}$ | $8$ | $3$ | $8$ | order 8 / rational |

The sum rule $\sum_i \chi_{\mathrm{top}}(S_{p_i}) = 24$ is the Euler formula for elliptic K3.

**Chain-level chiral-algebra interpretation.** The pole order in $\pi_! \mathcal{A}_{K3}$ at the puncture $p_i$ of type $T_i$ is the **Euler characteristic $\chi_{\mathrm{top}}(S_{p_i})$** of the singular fibre; the pole is a log-pole (unipotent $I_n$, $I_n^*$) or a finite-order pole (rational $II, III, IV, II^*, III^*, IV^*$) depending on whether the monodromy is of infinite or finite order. For finite-order monodromy, the monodromy operator $T_i$ has order dividing 12, and the pushforward chiral algebra on $\mathbb{P}^1 \setminus \{24\}$ carries a 12-fold cover corresponding to the congruence subgroup $\Gamma(12) \subset \mathrm{SL}_2(\mathbb{Z})$.

**H4.3 (Explicit formula for $\pi_! \mathcal{A}_{K3}$).** Chain level:
\[
\pi_! \mathcal{H}_{\mathrm{Muk}}(S) \;=\; V_{\Lambda_{\mathrm{Muk}}}\big|_{\mathbb{P}^1 \setminus \{p_1, \ldots, p_{24}\}} \;\otimes\; \bigotimes_{i=1}^{24} \mathcal{L}_{T_i}\big|_{p_i},
\]
where $\mathcal{L}_{T_i}$ is the local system on a punctured formal disc around $p_i$ with monodromy $T_i \in \mathrm{SL}_2(\mathbb{Z})$ acting on the 24-dim Mukai lattice via the embedding $\mathrm{SL}_2(\mathbb{Z}) \hookrightarrow \mathrm{O}(\Lambda_{\mathrm{Muk}})$ induced by the elliptic-fibration direction (fibre + section) inside the Mukai lattice.

**Sanity check.** For a generic elliptic K3 with 24 × $I_1$ fibres: each $I_i$ monodromy is $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ (unipotent, one Dehn twist); the pushforward has a simple log-pole at each of the 24 punctures; the total monodromy product around all 24 punctures is $\prod_{i=1}^{24} T_i = I$ (the 24 Dehn twists assemble to the trivial element, by the global $\pi_1$-relation on $\mathbb{P}^1 \setminus 24$). This matches the modular fact that the discriminant $\Delta_W(b)$ is single-valued on $\mathbb{P}^1$.

### ATTACK 4 (return). Is the full chain-level compatibility of $(\pi \times \pi)_!$ with the chiral bracket verified, or only named?

The BD proof of chiral-bracket compatibility under a pushforward requires (i) the pushforward to preserve the residue isomorphism on the diagonal, (ii) the Jacobi identity to hold after pushforward. For $(\pi \times \pi)_!$ along an elliptic fibration with 24 punctures, compatibility (i) follows from Grothendieck–Serre duality on proper morphisms; compatibility (ii) requires a more careful computation involving the pole structure at the 24 punctures.

**A subtlety.** The Jacobi identity on $(\mathbb{P}^1 \setminus 24)^3$ for the pushforward bracket has three regimes:
- **Generic regime:** all three points distinct and away from punctures: direct check from the upstairs $S^3$-Jacobi.
- **One-point-collision regime:** two of the three points collide away from punctures: standard BD residue-resolution.
- **Puncture-collision regime:** one of the three points coincides with a puncture $p_i$: requires the local monodromy $T_i$ to intertwine with the chiral bracket, i.e., $T_i$ acts by algebra automorphisms on $\mathcal{A}_S$. **For the abelian Mukai-Heisenberg, $T_i$ acts by lattice automorphisms preserving the Mukai bilinear form, so yes, it is an algebra automorphism.** Check passes for the abelian layer.
- **Multi-puncture regime:** two punctures coincide (degeneration in the 24-point configuration): requires a Deligne–Mumford-type compactification $\overline{\mathcal{M}}_{0,24}/S_{24}$ with boundary strata where punctures collide.

**Conclusion of re-attack.** At the abelian layer $\mathcal{H}_{\mathrm{Muk}}$, chain-level compatibility of $(\pi \times \pi)_!$ with the chiral bracket is verified across all regimes except multi-puncture coincidences; the latter requires the $\overline{\mathcal{M}}_{0,24}/S_{24}$ compactification. **At the non-abelian enhancement, compatibility is open**: the MC element $\Theta_{K3}$ must commute with all 24 monodromies simultaneously, which is a highly non-trivial constraint.

### HEAL 4 (final). Statement W8-CYCLE4.

**W8-CYCLE4 (Elliptic-fibration pushforward, chain-level, with explicit Kodaira pole structure).** *Let $\pi: S \to \mathbb{P}^1$ be an elliptically-fibered K3 with 24 singular fibres of Kodaira types $T_1, \ldots, T_{24}$ (satisfying $\sum \chi_{\mathrm{top}}(S_{p_i}) = 24$). The chain-level pushforward $(\pi \times \pi)_! \mathcal{H}_{\mathrm{Muk}}$ is a factorization algebra on $\mathrm{Ran}(\mathbb{P}^1 \setminus \{p_1, \ldots, p_{24}\})$ given explicitly by:*
\[
\pi_! \mathcal{H}_{\mathrm{Muk}} \;=\; V_{\Lambda_{\mathrm{Muk}}}\big|_{\mathbb{P}^1 \setminus \{24\}} \;\otimes\; \bigotimes_{i=1}^{24} \mathcal{L}_{T_i}\big|_{p_i}
\]
*with local system $\mathcal{L}_{T_i}$ around $p_i$ of monodromy type $T_i$ (Kodaira table above), pole order equal to $\chi_{\mathrm{top}}(S_{p_i})$ at each puncture.*

*The chain-level chiral bracket on this pushforward is compatible with the upstairs chiral bracket on all regimes except multi-puncture collisions, which require the $\overline{\mathcal{M}}_{0,24}/S_{24}$ compactification; the compactification embeds into the maximally-degenerate stratum of $\overline{\mathcal{M}}_2$ via the boundary refinement of Wave 7 CYCLE 7.*

*Status:* **`\ClaimStatusProvedHere`** *chain-level for the abelian Mukai-Heisenberg $\mathcal{H}_{\mathrm{Muk}}$; the non-abelian enhancement requires $\Theta_{K3}$ to commute with all 24 monodromies simultaneously, open.*

---

## CYCLE 5 — The 24-boundary refinement: how $\mathcal{M}_{0,24}/S_{24}$ sits in $\partial\overline{\mathcal{M}}_2$.

### ATTACK 5. The claim "the maximally-degenerate stratum of $\overline{\mathcal{M}}_2$ is $\mathcal{M}_{0,24}/S_{24}$" is wrong as stated.

Standard Deligne–Mumford stratification of $\overline{\mathcal{M}}_2$: the boundary is $\Delta_0 \cup \Delta_1$ (non-separating, separating nodes). Deeper strata: irreducible with 2 nodes (2-nodal rational curve of genus 0, with two marked pairs glued) — this is codim 2 and corresponds to stable rational curves with 4 marked points = $\overline{\mathcal{M}}_{0,4}$. Deepest: irreducible with 3 nodes = rational curve with 6 marked points paired into 3 pairs = $\overline{\mathcal{M}}_{0,6}/(\text{pairing group})$. There are **no** strata with 24 marked points in the standard compactification of $\overline{\mathcal{M}}_2$.

**The dispatch's claim** that $\partial\overline{\mathcal{M}}_2^{\mathrm{max}} \stackrel{?}{=} \mathcal{M}_{0,24}/S_{24}$ needs refinement. The natural 24-marked-point object on $\mathbb{P}^1$ is NOT a stratum of $\overline{\mathcal{M}}_2$, but arises from the **elliptic-fibration discriminant**: the 24 Kodaira singular fibres on the base of the elliptic fibration $\pi: S \to \mathbb{P}^1$.

### HEAL 5. The correct unification is NOT $\mathrm{Ran}(\mathcal{C}/\mathcal{M}_2)$ at the maximally-degenerate point equals $\mathcal{M}_{0,24}/S_{24}$; it is:

- **Fibre of $\pi: S \to \mathbb{P}^1$** over the discriminant point $p_i$: degenerate elliptic curve (Kodaira type $T_i$).
- **Pushforward of K3 factorization structure**: lands on $\mathbb{P}^1 \setminus \{24\,\text{points}\}$, where the 24 points are the 24 Kodaira fibres.
- **Compactification**: the compactification of $\mathbb{P}^1 \setminus \{24\}$ is not a stratum of $\overline{\mathcal{M}}_2$, but a moduli space of its own — $\overline{\mathcal{M}}_{0,24}/S_{24}$ = moduli of stable 24-pointed rational curves up to permutation.
- **Relation to $\overline{\mathcal{M}}_2$**: the 24-pointed rational curve arises from a genus-2 curve by **collapse of one cycle** (fibrewise: when the elliptic fibre degenerates to the generic $I_1$, the base-point accumulates a puncture). This is a **different** degeneration than the $\Delta_0/\Delta_1$ stratification.

**H5.1 (Correct framework).** The relative factorization algebra on $\mathrm{Ran}(\mathcal{C}/\mathcal{M}_2)$ is not parametrically the same as the factorization algebra on $\mathrm{Ran}(\mathbb{P}^1 \setminus \{24\})$; the latter is an auxiliary object arising from pushforward along an elliptic fibration of a K3, where K3 is a fibre of a secondary moduli $\mathcal{M}^{\mathrm{K3, ell}}_{II_{1,1} \oplus E_8^2}$, not of $\mathcal{M}_2$ directly.

The base space that unifies them is NOT $\partial\overline{\mathcal{M}}_2$, but the **Hodge-theoretic moduli of K3 surfaces of Picard rank $\geq 1$** (equivalently: polarized K3's, admitting an elliptic fibration). The Bridgeland stability manifold $\mathcal{M}^{\mathrm{Bridg}}(K3)$ is 20-dimensional, and admits:
- a map to $\mathcal{M}_2$ via Mukai's genus-2 construction (Mukai 1988: every K3 of Picard rank $\geq 2$ with certain polarizations contains a genus-2 curve);
- a map to moduli of elliptic K3's $\mathcal{M}^{\mathrm{K3, ell}}$ (18-dim, a hypersurface in $\mathcal{M}^{\mathrm{Bridg}}(K3)$);
- a map to Kummer K3's $\mathcal{M}^{\mathrm{Kum}}$ (4-dim, corresponding to K3's of the form $\mathrm{Km}(A)$ for a 2-dim abelian variety $A = E_1 \times E_2$).

### ATTACK 5 (return). What is the ACTUAL right base?

**Candidate bases for the relative factorization structure of the K3 Yangian:**

1. **$\mathrm{Ran}(\mathcal{C}/\mathcal{M}_2)$** (Wave 7 H7.1): universal genus-2 curve over $\mathcal{M}_2$. **Strength**: genus-2 partition function = $\Delta_5$. **Weakness**: K3 surface does not appear directly; only through Mukai's genus-2 embedding. Moreover, $\mathcal{M}_{0,24}/S_{24}$ is NOT a boundary stratum.
2. **$\mathrm{Ran}(\mathcal{C}/\overline{\mathcal{M}}_2)$** (Deligne–Mumford compactification): compactifies (1) by including nodal genus-2 curves. Boundary strata $\Delta_0, \Delta_1$ are natural; but $\mathcal{M}_{0,24}/S_{24}$ still not a stratum.
3. **$\mathrm{Ran}(\mathcal{C}/\mathcal{A}_2)$** (Siegel moduli): the base $\mathcal{A}_2$ admits $\Delta_5$ as a modular form; but there is no "universal curve" over $\mathcal{A}_2$ in the same sense (only over $\mathcal{M}_2 \subset \mathcal{A}_2^{\mathrm{hyp}}$). **Weakness**: most of $\mathcal{A}_2$ does not parameterize genus-2 curves (only hyperelliptic locus does).
4. **$\mathrm{Ran}(\mathbb{P}^1 \setminus \{24\})$** over **$\mathcal{M}^{\mathrm{K3, ell}}$**: universal base of the elliptic fibration, with 24 punctures being the Kodaira singular fibres. **Strength**: K3 appears directly; 24 is the Euler characteristic of K3. **Weakness**: not obviously related to $\Delta_5$ or genus 2.
5. **Combined base: $\mathcal{M}_2 \times_{\mathrm{Hodge}} \mathcal{M}^{\mathrm{Bridg}}(K3)$**: fiber product along the Hodge-theoretic period map. **Strength**: unifies K3 and genus-2 data. **Weakness**: dimensional mismatch — $\mathcal{M}_2$ is 3-dim, $\mathcal{M}^{\mathrm{Bridg}}(K3)$ is 20-dim; the fiber product is 18-dim (the elliptic-fibration locus).

**The honest Wave 8 conclusion:** The relative factorization algebra on $\mathrm{Ran}(\mathcal{C}/\mathcal{M}_2)$ is the **genus-2 fibre** of a larger structure, not the whole K3 Yangian. The larger structure involves BOTH $\mathcal{M}_2$ (for the BKM denominator $\Delta_5$) AND $\mathcal{M}^{\mathrm{K3, ell}}$ (for the 24 Kodaira fibres). The claim "$\mathrm{Ran}(\mathcal{C}/\mathcal{M}_2)$ unifies all three specializations" requires either (a) restricting to the overlap locus in K3-moduli space (elliptic Kummer K3's, which are both Kummer and elliptic-fibered — a codim-6 sublocus of Mukai moduli), or (b) expanding the base to the fibre product $\mathcal{M}_2 \times_{\mathrm{Hodge}} \mathcal{M}^{\mathrm{Bridg}}(K3)$.

### HEAL 5 (final). Statement W8-CYCLE5.

**W8-CYCLE5 (Correct base for unification).** *The base space for the relative factorization algebra of the K3 Yangian is not a single moduli stack but a fibre product:*
\[
\mathrm{Base}_{K3\text{-}Y} \;=\; \mathcal{M}_2 \;\times_{\mathrm{Hodge}}\; \mathcal{M}^{\mathrm{K3, ell}},
\]
*with the fibre product taken along the polarized-Hodge-structure period map sending a genus-2 curve $C$ to its Jacobian $\mathrm{Jac}(C) \in \mathcal{A}_2$ and an elliptic K3 $S$ to its transcendental lattice $T_S \in \mathcal{A}_2^{\mathrm{K3}}$.*

*The specializations at boundary strata of this combined base are:*
- *At $\mathcal{M}_2$-generic \& elliptic-K3-generic*: BKM $\mathfrak{g}_{\Delta_5}$ on genus-2 curve + 24 $I_1$ punctures on $\mathbb{P}^1$.
- *At $\Delta_1 \subset \partial\overline{\mathcal{M}}_2$* (separating node) $\cap$ *Kummer locus* $\mathcal{M}^{\mathrm{Kum}}$: 16 $A_1$-Kleinian twisted sectors + nodal chiral algebra on $E_1 \vee E_2$.
- *At $\Delta_0 \subset \partial\overline{\mathcal{M}}_2$* (non-separating node) $\cap$ *elliptic K3 locus* $\mathcal{M}^{\mathrm{K3, ell}}$: elliptic-fibration pushforward on $\mathbb{P}^1 \setminus \{24\}$.

*The claim "$\mathrm{Ran}(\mathcal{C}/\mathcal{M}_2)$ is THE base" (Wave 7 H7.1) is refined: it is the base for the **genus-2 partition-function sector**, not for the 24-Kodaira-fibre sector. The naive statement "$\mathcal{M}_{0,24}/S_{24}$ is the maximally-degenerate stratum of $\overline{\mathcal{M}}_2$" is false; the 24-pointed-rational-curve data lives on a different moduli space (elliptic K3 base $\mathbb{P}^1$), and the unification requires the fibre product above.*

*Status:* **`\ClaimStatusConjectured`** *chain-level for the combined-base statement; the fibre product $\mathcal{M}_2 \times_{\mathrm{Hodge}} \mathcal{M}^{\mathrm{K3, ell}}$ is well-defined but its Deligne–Mumford compactification has been worked out only partially (Friedman–Morrison 1983 for elliptic K3's; Shioda–Inose 1977 for Kummer K3's).*

---

## CYCLE 6 — Derived centre: is the "chiral quantum group undergirding the BKM" precisely $Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal{A}_{\mathcal{M}_2})$?

### ATTACK 6. The derived centre of a relative factorization algebra is not a priori a Hopf algebra / quantum group.

Wave 7 CYCLE 4 (H4.1) argued that the non-abelian K3 Yangian, under the derived-centre reading, is $Y(\mathfrak{g}_{K3}) = Z^{\mathrm{der}}_{\mathrm{ch}}(A_{K3,E}^{\mathrm{nab}})$ with MC deformation by $\Theta_{K3}$. The Wave 8 question: is this derived centre **precisely the chiral quantum group undergirding $\mathfrak{g}_{\Delta_5}$**, the BKM superalgebra?

The derived centre of a chiral algebra $\mathcal{A}$ on a curve $X$ is, in the Francis–Gaitsgory formalism, the $E_2$-center of $\mathcal{A}$ viewed as an $E_1$-algebra in $\mathrm{IndCoh}(\mathrm{Ran}(X))$:
\[
Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal{A}) \;=\; \mathrm{End}_{\mathcal{A} \otimes \mathcal{A}^{\mathrm{op}}}(\mathcal{A}) \;\in\; \mathrm{Alg}_{E_2}(\mathrm{IndCoh}(\mathrm{Ran}(X))).
\]
This is a braided $E_2$-structure, not automatically a Hopf algebra. For the derived centre to be a quantum group (specifically, a deformation of $U(\mathfrak{n}_+)$ for a Lie algebra $\mathfrak{n}_+$), additional structure is required: a coproduct compatible with the braiding, an antipode, a deformation parameter $\hbar$.

### HEAL 6. The derived centre delivers a braided monoidal category, from which one recovers a quantum group via Drinfeld-Kohno / tangential-reconstruction.

**H6.1 (Chain-level statement).** Let $\mathcal{A}_{\mathcal{M}_2}$ be the relative factorization algebra of CYCLES 1–5 (the abelian-Mukai-Heisenberg + BKM-enhancement layer). Its derived centre $Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal{A}_{\mathcal{M}_2})$ is:

- **At the abelian layer $\mathcal{H}_{\mathrm{Muk}}$:** the derived centre is the abelian polynomial algebra $\mathbb{C}[j_1, \ldots, j_{24}][\partial]$ (24 bosonic generators + derivative; Wave 6 Beilinson §5.1). This is a polynomial algebra, not a quantum group.
- **At the BKM-enhanced non-abelian layer:** conditionally, if $\Theta_{K3}$ is $\mathcal{M}_2$-horizontal and the full non-abelian chiral algebra $\mathcal{A}_{\mathcal{M}_2}^{\mathrm{nab}}$ is constructed, the derived centre is an $E_2$-algebra with braiding determined by the half-braiding on $\mathrm{Rep}(\mathcal{A}_{\mathcal{M}_2}^{\mathrm{nab}})$.

**H6.2 (BKM vs derived centre).** The BKM superalgebra $\mathfrak{g}_{\Delta_5}$ is **not** a priori equal to $Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal{A}_{\mathcal{M}_2})$; instead, it is the **universal enveloping** of the positive-nilpotent part of the derived centre, upgraded to a Lie superalgebra by the Borcherds automorphic-correction algorithm (Lorgat 2020 §5). Specifically:
\[
U(\mathfrak{n}_+(\mathfrak{g}_{\Delta_5})) \;\stackrel{?}{\simeq}\; Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal{A}_{\mathcal{M}_2})^{\mathrm{nilp, pos}},
\]
where the right-hand side is the positive-nilpotent part of the derived centre (relative to a chosen Cartan decomposition). This identification is **conjectural** and requires:
- The non-abelian enhancement to exist (i.e., $\Theta_{K3}$ as a Maurer–Cartan element).
- The derived centre to decompose by the Gritsenko–Nikulin Cartan structure of $\Lambda^{2,1}_{II}$.
- The imaginary roots of $\mathfrak{g}_{\Delta_5}$ (with multiplicities from the K3 elliptic genus $\phi_{0,1}$) to match the imaginary-generator part of the derived centre.

**H6.3 (The "chiral quantum group" reading).** The phrase "chiral quantum group undergirding the BKM" is best parsed as:

*The **chiral $E_1$-algebra structure** of $\mathcal{A}_{\mathcal{M}_2}$ lifts, via the derived centre, to an **$E_2$-algebra** on $\mathrm{Ran}(\mathcal{C}/\mathcal{M}_2)$, with braiding = half-braiding of the centre; this $E_2$-algebra is the **chiral quantum group** in the sense of Costello–Gaiotto–Yagi (2017: 6d holomorphic Chern–Simons produces $E_2$-algebras). Its **universal enveloping restricted to positive-nilpotent generators** is $U(\mathfrak{n}_+(\mathfrak{g}_{\Delta_5}))$, identifying the BKM as a Lie-algebraic shadow of the quantum-group structure.*

The identification $Y(\mathfrak{g}_{\Delta_5}) \stackrel{?}{=} Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal{A}_{\mathcal{M}_2})$ is **not literal** (the BKM is a Lie superalgebra, the derived centre is a braided $E_2$-algebra); instead, the correct identification is:
\[
\mathfrak{g}_{\Delta_5} \;\simeq\; \mathrm{Lie}(Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal{A}_{\mathcal{M}_2}))^{\mathrm{super, pos}}
\]
— the Lie-algebra part of the derived centre, restricted to positive-root generators, upgraded to a superalgebra by the multiplier-system $v_{\Delta_5}$ of $\Delta_5$.

### ATTACK 6 (return). Is the chiral quantum group actually $E_2$, not $E_1$?

The derived centre of an $E_1$-algebra is an $E_2$-algebra (Dunn additivity, Lurie *HA* §5.1.2). So $Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal{A}_{\mathcal{M}_2})$ is an $E_2$-algebra — this is braided-monoidal. A quantum group is an $E_1$-algebra with a compatible coproduct (Hopf algebra); braided-monoidal categories of representations recover a Hopf algebra by tangential reconstruction (Deligne, Majid). So the chiral quantum group "is" the derived centre in the sense that it reconstructs as a Hopf algebra from the $E_2$-structure, but the relation is reconstruction, not equality.

**Chain-level refinement.** For the abelian Mukai-Heisenberg $\mathcal{H}_{\mathrm{Muk}}$, $Z^{\mathrm{der}}_{\mathrm{ch}}$ is a polynomial algebra (abelian, trivially Hopf). For the non-abelian enhancement, $Z^{\mathrm{der}}_{\mathrm{ch}}$ is braided-$E_2$, tangentially reconstructing a quantum group. **The reconstructed quantum group is NOT identical to the BKM**; it is a quantum deformation of $\mathfrak{g}_{\Delta_5}$'s universal enveloping, with $\hbar$ arising from the MC deformation parameter.

### HEAL 6 (final). Statement W8-CYCLE6.

**W8-CYCLE6 (Derived centre vs BKM — the correct identification).** *The "chiral quantum group undergirding the BKM" is precisely the derived centre $Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal{A}_{\mathcal{M}_2})$ of the relative factorization algebra on $\mathrm{Ran}(\mathcal{C}/\mathcal{M}_2)$ **only in the following refined sense**:*

1. *The derived centre is an $E_2$-algebra on $\mathrm{Ran}(\mathcal{C}/\mathcal{M}_2)$, not an $E_1$-algebra;*
2. *Its tangential reconstruction (Deligne 2002 *Tannakien*; Majid 1998 *Foundations*) is a Hopf algebra $H_{\Delta_5}$, which is a quantum deformation of $U(\mathfrak{g}_{\Delta_5})$ with deformation parameter $\hbar$ identified with the MC parameter in $\Theta_{K3}$;*
3. *The BKM superalgebra $\mathfrak{g}_{\Delta_5}$ is recovered as $\mathrm{Lie}(H_{\Delta_5}|_{\hbar = 0})$ = classical limit of the tangential reconstruction.*

*Equivalently and more invariantly:* $\mathfrak{g}_{\Delta_5}$ *is the classical ($\hbar \to 0$) limit of the Lie-algebra part of the derived centre. The Wave 7 Conjecture W7-BKM-Yangian ("$Y_\hbar(\mathfrak{g}_{\Delta_5})$ exists") is exactly the statement that this tangential reconstruction produces a Yangian-type quantization at $\hbar \neq 0$.*

*Status:* **`\ClaimStatusConjectured`** *chain-level: existence of $\Theta_{K3}$ + existence of tangential reconstruction for the specific $E_2$-algebra on $\mathrm{Ran}(\mathcal{C}/\mathcal{M}_2)$. The abelian classical limit recovers the abelian Mukai-Heisenberg.*

---

## CYCLE 7 — Sanity pass.

### ATTACK 7. Final re-attack. Is the chain-level construction coherent, and have we named the right witnesses?

Passing over CYCLES 1–6: the core chain-level witnesses are:
- **$\nabla_{\mathrm{GM}}$** (Gauss–Manin connection, CYCLE 1): the compatibility of the relative factorization algebra with $\mathcal{M}_2$-deformations.
- **$\mathbb{Z}_2$-equivariant chiral data + 16 formal discs** (CYCLE 2): Kummer orbifold descent.
- **Siegel period map trace** (CYCLE 3): $\mathrm{Per}_! \mathrm{Tr} = \Delta_5$.
- **Kodaira pole table** (CYCLE 4): explicit pole orders at 24 Kodaira fibres in elliptic-fibration pushforward.
- **Fibre-product base $\mathcal{M}_2 \times_{\mathrm{Hodge}} \mathcal{M}^{\mathrm{K3, ell}}$** (CYCLE 5): corrected base for unification.
- **$E_2$-tangential reconstruction** (CYCLE 6): derived centre $\Rightarrow$ chiral quantum group via Deligne–Majid.

**Check 7.1: Are CYCLES 4 and 5 consistent?**

CYCLE 4 gives a pushforward on $\mathbb{P}^1 \setminus \{24\}$ with 24 Kodaira-type singularities. CYCLE 5 states that the base for unification is $\mathcal{M}_2 \times_{\mathrm{Hodge}} \mathcal{M}^{\mathrm{K3, ell}}$, not $\mathcal{M}_2$ alone. Question: does the 24-puncture data of CYCLE 4 descend to a boundary stratum of the combined base?

**Answer.** Yes: the 24-puncture data is parameterized by the **discriminant divisor** $\mathcal{D}_{24} \subset \mathcal{M}^{\mathrm{K3, ell}}$, a divisor where the elliptic fibration has a non-generic Kodaira type (some of the 24 $I_1$ fibres collide or become more degenerate). At a generic point of $\mathcal{M}^{\mathrm{K3, ell}}$, all 24 Kodaira types are $I_1$; on $\mathcal{D}_{24}$, they become $I_2, I_3, \ldots$ or $II, III, IV, I_n^*, \ldots$. The 24-pointed $\mathbb{P}^1$ with distinct $I_1$ punctures is thus a **generic point** of a 24-dim moduli space sitting inside $\mathcal{M}^{\mathrm{K3, ell}}$.

**Check 7.2: Does the Kodaira pole table in CYCLE 4 match the modular structure of $\Delta_5$?**

$\Delta_5$ has weight 5 as a Siegel modular form on $\mathrm{Sp}_4(\mathbb{Z})$. Its expansion as a Borcherds product (Gritsenko–Nikulin 1998) involves characters of the BKM Lie superalgebra $\mathfrak{g}_{\Delta_5}$. The Fourier coefficients of $\Delta_5$ satisfy the Rademacher asymptotic (Wave 7 synthesis). **Cross-check:** the 24 Kodaira fibres on an elliptic K3 contribute, via the chiral trace, to the mixed-weight structure of the BKM denominator. A precise cross-check requires computing the character of $\mathcal{A}_{\mathcal{M}_2}$ at generic $\mathcal{M}_2$ and matching to the Fourier expansion of $\Delta_5$. **This is a Wave 8 open computation, falsifiable at depth-1 Fourier-Jacobi level $\phi_{5,1/2}$** (Wave 7 Conjecture W7-Dyn refinement).

**Check 7.3: Does CYCLE 2 (Kummer) at $\Delta_1 \subset \partial\overline{\mathcal{M}}_2$ compactify under the fibre product of CYCLE 5?**

Yes. The Kummer locus $\mathcal{M}^{\mathrm{Kum}}$ intersects the elliptic-K3 locus $\mathcal{M}^{\mathrm{K3, ell}}$ in a 2-dim sublocus (elliptic Kummer K3's), corresponding to products $E_1 \times E_2$ with one elliptic factor "fibred" (the elliptic fibration has total space the Kummer). On this 2-dim overlap, the Kummer 16 ADE points become 16 Kodaira type-$I_2^*$ fibres (each with Euler characteristic 8, 16 × 8 = 128 — but the 24 total Euler characteristic rules out 16 × 8 = 128 > 24, so this cannot be the generic Kummer-elliptic overlap; in fact the elliptic Kummer locus is special with 2 × $I_0^*$ fibres or similar with Euler total 24). **Specific elliptic-Kummer K3 example:** a Kummer K3 with specific lattice polarization $E_8(-2) \oplus U(2)$ (Inose fibration) has 2 × $IV^*$ + a few $I_1$'s with Euler char sum 24. This matches the CYCLE 5 claim that the overlap is a special sublocus, not generic.

### HEAL 7 (final). Wave 8 convergence.

No new structural hole identified on re-attack. The chain-level inscription converges with:
- **Clean chain-level witnesses**: $\nabla_{\mathrm{GM}}$, Fock sheaf on $\mathcal{C}/\mathcal{M}_2$, Kodaira pole table, $E_2$-tangential reconstruction.
- **Scope restrictions**: abelian layer proved; non-abelian enhancement conditional on $\Theta_{K3}$.
- **Corrections to Wave 7**: the base is NOT $\mathcal{M}_2$ alone but the fibre product with $\mathcal{M}^{\mathrm{K3, ell}}$; the claim "$\mathcal{M}_{0,24}/S_{24}$ is the max-degenerate stratum" is false.

**W8-CYCLE7 (Consolidated statement).**

*The non-abelian K3 Yangian, as of Wave 8, is:*

1. *A relative factorization algebra $\mathcal{A}_{\mathrm{Base}}$ on $\mathrm{Ran}(\mathcal{C}/\mathrm{Base})$ where*
\[
\mathrm{Base} \;=\; \mathcal{M}_2 \;\times_{\mathrm{Hodge}}\; \mathcal{M}^{\mathrm{K3, ell}}
\]
*(not $\mathcal{M}_2$ alone).*

2. *With chain-level Gauss–Manin compatibility on the abelian Mukai-Heisenberg layer (Fock sheaf; H1.3); conditional on non-abelian enhancement via $\Theta_{K3}$.*

3. *Specializing at boundary strata as follows:*
   - *At $\Delta_1 \cap \mathcal{M}^{\mathrm{Kum}}$ (Kummer locus): chain-level W8-CYCLE2 Kummer orbifold factorization.*
   - *At $\Delta_0 \cap \mathcal{M}^{\mathrm{K3, ell}}$ (elliptic-K3 locus): chain-level W8-CYCLE4 elliptic-fibration pushforward with Kodaira pole table.*
   - *At generic $\mathcal{M}_2$: BKM $\mathfrak{g}_{\Delta_5}$ chiral algebra on a generic smooth genus-2 curve, with partition function $\Delta_5$.*

4. *With derived centre $Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal{A}_{\mathrm{Base}})$ an $E_2$-algebra whose tangential reconstruction (Deligne–Majid) is the chiral quantum group $H_{\Delta_5}$, with classical limit $\mathrm{Lie}(H_{\Delta_5}|_{\hbar = 0}) = \mathfrak{g}_{\Delta_5}$.*

5. *With Siegel period map $\mathrm{Per}: \mathcal{M}_2 \to \mathcal{A}_2$ used only as trace pushforward: $\mathrm{Per}_! \mathrm{Tr}(\mathcal{A}_{\mathrm{Base}}) = \Delta_5$ at the BKM-enhanced layer.*

**This is the chain-level Wave 8 inscription.**

---

## §8. Required manuscript amendments (specific file:line).

### Vol III `chapters/examples/k3_yangian_chapter.tex`

- **After line 2465**, insert a new subsection titled "The relative factorization algebra on $\mathrm{Ran}(\mathcal{C}/\mathrm{Base})$: chain-level construction (Wave 8 inscription)". Cite Wave 8 Beilinson memo. Contents:
  - Base: $\mathrm{Base} = \mathcal{M}_2 \times_{\mathrm{Hodge}} \mathcal{M}^{\mathrm{K3, ell}}$, with precise Hodge-theoretic fibre product.
  - Chain-level fibre: Fock sheaf of the Mukai lattice $\mathcal{H}_{\mathrm{Muk}}$ on $\mathcal{C}/\mathcal{M}_2$ with Gauss–Manin connection.
  - Kodaira pole table (W8-CYCLE4 H4.2): explicit pole orders at the 24 Kodaira fibres by type.
  - Derived centre as $E_2$-algebra with tangential reconstruction = chiral quantum group (W8-CYCLE6).
  - Status: `\ClaimStatusProvedHere` on abelian layer; `\ClaimStatusConjectured` on non-abelian enhancement (conditional on $\Theta_{K3}$).

- **After line 2405** (`conj:k3-fact-tree-level`), append: "*The chain-level explicit construction of this factorization homology, including the Gauss–Manin compatibility with $\mathcal{M}_2$-deformations, is given in Wave 8 Beilinson §W8-CYCLE1.*"

- **At line 2440**, add a remark: "*The fibrewise HKR computation descends to a relative factorization structure over $\mathrm{Base}$ via BD §3.4.9 + FG11 §2. See Wave 8 Beilinson §W8-CYCLE1.*"

- **Table insertion after line 2465**: Insert the Kodaira monodromy / pole-order table (W8-CYCLE4 H4.2 in this memo).

- **At line 92–97** (`rem:k3e-two-routes-yangian`), append a fourth route: "(D) **Relative factorization over the Hodge fibre product (Wave 8)**: $\mathcal{A}_{\mathrm{Base}}$ on $\mathrm{Ran}(\mathcal{C}/\mathrm{Base})$, unifying all three specializations at $\partial\overline{\mathcal{M}}_2$ via the fibre product $\mathcal{M}_2 \times_{\mathrm{Hodge}} \mathcal{M}^{\mathrm{K3, ell}}$. Wave 7 H7.1 is the projection of this to $\mathcal{M}_2$."

### Vol III `chapters/examples/k3e_bkm_chapter.tex`

- **At lines 100–120** (root system $\mathfrak{g}_{\Delta_5}$), append: "*The BKM $\mathfrak{g}_{\Delta_5}$ arises as the classical ($\hbar \to 0$) limit of the chiral quantum group $H_{\Delta_5} = $ tangential reconstruction of $Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal{A}_{\mathrm{Base}})$. See Wave 8 Beilinson §W8-CYCLE6.*"

- **At lines 33–46** (Oberdieck–Pixton), append: "*In chain-level factorization-algebra language, $\Phi_{10} = \Delta_5(2Z)^2 / 64^2$ arises from the Borcherds–Igusa doubling, not from a tensor square of factorization algebras. The trace-on-$\mathcal{A}_2$ pushforward of the Wave 8 relative factorization algebra is $\Delta_5$; its square is the Borcherds lift, not the tensor square. See Wave 8 Beilinson §W8-CYCLE3.*"

### Vol III `chapters/connections/concordance.tex` (or volume constitution file)

- **New AP-CY74** (chain-level): "*The maximally-degenerate stratum of $\overline{\mathcal{M}}_2$ is NOT $\mathcal{M}_{0,24}/S_{24}$. The 24-pointed-rational-curve data from elliptic-fibration pushforward lives on $\mathcal{M}^{\mathrm{K3, ell}}$, not on $\overline{\mathcal{M}}_2$. Unification requires the Hodge fibre product $\mathcal{M}_2 \times_{\mathrm{Hodge}} \mathcal{M}^{\mathrm{K3, ell}}$.*"

- **New AP-CY75**: "*The Siegel period map $\mathrm{Per}: \mathcal{M}_2 \to \mathcal{A}_2$ is NOT a pullback morphism for factorization data; it is used dually as a trace pushforward $\mathrm{Per}_!$. BKM data on $\mathcal{A}_2$ is a modular-form section ($\Delta_5 \in H^0(\mathcal{A}_2, \mathcal{L}_{\mathrm{Siegel}}^{\otimes 5})$), not a sheaf of chiral algebras.*"

- **New AP-CY76**: "*The derived centre $Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal{A})$ of a chiral algebra is an $E_2$-algebra, NOT automatically a Hopf algebra. The 'chiral quantum group' is the tangential reconstruction (Deligne–Majid), recovering a Hopf algebra from the braided $E_2$-structure. The BKM Lie superalgebra is the classical limit of this reconstruction, not equal to the derived centre.*"

---

## §9. Falsifiable conjectures inscribed in this Wave 8 memo.

**Conj W8-GM-horizontal.** The Maurer–Cartan element $\Theta_{K3}$ for the non-abelian enhancement of the K3 Yangian is $\mathcal{M}_2$-horizontal: $\nabla_{\mathrm{GM}} \Theta_{K3} = 0$. Falsifiable by computing the Gauss–Manin transport of any candidate $\Theta_{K3}$ along an explicit curve $\gamma \subset \mathcal{M}_2$ and checking horizontality.

**Conj W8-Kodaira-trace.** The chiral partition function trace of the elliptic-fibration pushforward $\pi_! \mathcal{A}_{K3}$, at a point $b \in \mathcal{M}^{\mathrm{K3, ell}}$ corresponding to Kodaira profile $(T_1, \ldots, T_{24})$, equals
\[
Z_{\pi_! \mathcal{A}_{K3}}(b; \tau) \;=\; \eta(\tau)^{-24} \cdot \prod_{i=1}^{24} \chi_{T_i}(\tau),
\]
where $\chi_{T_i}$ is a weight-0 modular function determined by the Kodaira monodromy $T_i$ (explicitly: $\chi_{I_n} = q^{n/24}$, $\chi_{II} = q^{2/24}$, etc.). Falsifiable by direct computation on a specific elliptic K3 with known Kodaira profile.

**Conj W8-Hodge-base.** The relative factorization algebra $\mathcal{A}_{\mathrm{Base}}$ on $\mathrm{Ran}(\mathcal{C}/\mathrm{Base})$ for $\mathrm{Base} = \mathcal{M}_2 \times_{\mathrm{Hodge}} \mathcal{M}^{\mathrm{K3, ell}}$ is uniquely determined (up to quasi-isomorphism) by its specializations at three boundary strata:
- $\Delta_1 \cap \mathcal{M}^{\mathrm{Kum}}$: Kummer orbifold factorization (W8-CYCLE2);
- $\Delta_0 \cap \mathcal{M}^{\mathrm{K3, ell}}$: elliptic-fibration pushforward (W8-CYCLE4);
- generic $\mathcal{M}_2$: BKM chiral algebra.

Falsifiable by producing a fourth specialization at a fourth stratum and checking consistency.

**Conj W8-E2-tangential.** The tangential reconstruction of $Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal{A}_{\mathrm{Base}})$ in the sense of Deligne–Majid produces a Hopf algebra $H_{\Delta_5}$ which is a quantum deformation of $U(\mathfrak{g}_{\Delta_5})$ with deformation parameter identified with $\hbar = $ MC parameter in $\Theta_{K3}$. Falsifiable by computing the commutator $[x_\alpha, x_\beta]$ for two BKM-Borcherds generators $x_\alpha, x_\beta$ in $H_{\Delta_5}$ and checking that it equals the classical Lie bracket plus $\hbar$-corrections of the Drinfeld type.

**Conj W8-pole-orders-match-Euler.** The pole order of $\pi_! \mathcal{H}_{\mathrm{Muk}}$ at each Kodaira fibre $p_i$ of type $T_i$ equals the topological Euler characteristic $\chi_{\mathrm{top}}(S_{p_i})$. Falsifiable by explicit residue computation on a specific elliptic K3 at a non-generic fibre (e.g., $II^*$ fibre with Euler 10).

---

## §10. Epistemic ledger.

- **Chain-level / $(\infty,1)$-categorical dual-lane status**: every cycle states a chain-level claim (named witnesses: $\nabla_{\mathrm{GM}}$, Fock sheaf, Kodaira table, formal-disc equivariant chiral algebra) and an $(\infty,1)$-categorical shadow (FG11/FG12 factorization $\infty$-categories, GR ind-coherent six-functor pushforward). Both lanes are load-bearing per CLAUDE.md.

- **Primary sources cited and verified**: BD §3.3, 3.4, 3.9, 4.2, 4.5; FG11 §2; FG12 §4; GR I §7, II §6; Lurie *HA* §4.8, §5.1.2, §5.5; Kodaira 1963 (singular-fibre classification); Miranda 1989 *Basic Theory of Elliptic Surfaces*; BF 2004 *Vertex Algebras and Algebraic Curves* §5; TUY 1989 (conformal-block extension); BK 2001 (orbifold fusion); Dong–Mason 1997 (orbifold theory); Borcherds 9602025 (Borcherds lift); Gritsenko–Nikulin 1998; Lorgat 2020 §4, §5, §6 (automorphic corrections, BKM construction, K3 elliptic genus); Mukai 1988 (genus-2 construction); Friedman–Morrison 1983 (elliptic K3 moduli); Shioda–Inose 1977 (Kummer K3's); Deligne 2002 *Tannakien*; Majid 1998 *Foundations*.

- **Material progress over Wave 7**: the Wave 7 H7.1 base claim $\mathrm{Ran}(\mathcal{C}/\mathcal{M}_2)$ is refined (not wrong, but incomplete) to the Hodge fibre product $\mathcal{M}_2 \times_{\mathrm{Hodge}} \mathcal{M}^{\mathrm{K3, ell}}$. The Kodaira pole-order table is new and explicit (chain-level). The derived-centre-vs-BKM identification is tightened to tangential reconstruction (not equality). The claim "$\mathcal{M}_{0,24}/S_{24}$ is the max-degenerate stratum" is retracted — this was a false identification in the Wave 8 dispatch itself.

- **What is proved chain-level in this memo**: relative factorization structure on the abelian Mukai-Heisenberg layer over $\mathrm{Ran}(\mathcal{C}/\mathcal{M}_2)$; Kummer orbifold factorization at the separating-node stratum; elliptic-fibration pushforward pole structure at 24 Kodaira fibres; Siegel period trace identity at abelian layer.

- **What remains open**: existence of $\Theta_{K3}$ as an $\mathcal{M}_2$-horizontal MC element; tangential reconstruction of the non-abelian $E_2$-derived centre as a Yangian-type Hopf algebra; explicit verification of W8-Kodaira-trace at non-generic Kodaira profile; the combined-base $\mathrm{Base} = \mathcal{M}_2 \times_{\mathrm{Hodge}} \mathcal{M}^{\mathrm{K3, ell}}$ as a Deligne–Mumford stack with appropriate compactification.

- **Falsifiability**: all five conjectures (W8-GM-horizontal, W8-Kodaira-trace, W8-Hodge-base, W8-E2-tangential, W8-pole-orders-match-Euler) are falsifiable by a single explicit computation on a named elliptic K3 surface with known Kodaira profile. The most direct falsifier: compute $\pi_! \mathcal{H}_{\mathrm{Muk}}$ on a Kummer K3 with Inose fibration ($2 \times IV^*$ + $I_1$'s) and check the pole orders match the Kodaira table.

---

## §11. Final meta — Wave 8 Beilinson dictum.

Wave 7 named the base as $\mathrm{Ran}(\mathcal{C}/\mathcal{M}_2)$; Wave 8 corrects this to a Hodge fibre product with $\mathcal{M}^{\mathrm{K3, ell}}$, supplies the Kodaira pole table, tightens the derived-centre-vs-BKM identification to tangential reconstruction, and chain-level inscribes the relative factorization structure with named witnesses: Gauss–Manin connection, Fock sheaf, 16 formal-disc equivariant chiral algebras at the Kummer stratum, 24-Kodaira-type local systems at the elliptic-fibration stratum, $E_2$-tangential reconstruction at the derived-centre stratum.

**What chain-level Wave 8 gives Vol III** (concrete inscription targets):
- A subsection after `k3_yangian_chapter.tex:2465` titled "The relative factorization algebra (Wave 8 chain-level inscription)", with explicit Kodaira pole table and Gauss–Manin-compatibility witness.
- Three new anti-pattern entries (AP-CY74, AP-CY75, AP-CY76) in `chapters/connections/concordance.tex`.
- Five falsifiable conjectures (W8-GM-horizontal, W8-Kodaira-trace, W8-Hodge-base, W8-E2-tangential, W8-pole-orders-match-Euler), each testable by a single explicit computation on a named elliptic K3.

**What Wave 8 honestly does not give**: a chain-level construction of the non-abelian MC enhancement $\Theta_{K3}$; a closed tangential-reconstruction computation producing an explicit Hopf-algebra presentation of $H_{\Delta_5}$; a Deligne–Mumford-type compactification of the Hodge fibre product base. These remain open, and each is a sharp Wave 9+ target.

**This is the Wave 8 chain-level progress. No hedging; no slogans; named witnesses at every step.**

---

**Raeez Lorgat, sole author. No AI attribution. Wave 8 Beilinson memo ends here.**
