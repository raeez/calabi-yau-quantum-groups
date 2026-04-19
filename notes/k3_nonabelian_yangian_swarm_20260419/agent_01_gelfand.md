# Gelfand audit of the non-abelian K3 Yangian

*Agent 01 — Gelfand voice. Attack-heal iterative protocol on the "non-abelian K3 Yangian" as it stands in the Vol III manuscript as of 2026-04-19.*

Raeez Lorgat, sole author. No AI attribution anywhere.

---

## 0. What the manuscript claims

From `chapters/examples/k3_yangian_chapter.tex` opening (lines 1–12):

> The K3 double current algebra $\mathfrak{g}_{K3}$ is the classical limit of the K3 Yangian $Y(\mathfrak{g}_{K3})$, whose 24 Heisenberg generators, Mukai-signature Serre relations, and degree-$(24,24)$ structure function encode the quantization of the Mukai lattice. This chapter develops the complete abelian Yangian presentation, the Koszul dual, the orthosymplectic super-Yangian envelope $Y_{\osp(4 \mid 20)}$ attached to the Mukai orthogonal form, and the perturbative factorization homology computation.

So the advertised protagonist decomposes into three levels:

1. The **abelian K3 Yangian** $Y(\mathfrak g_{K3})$ at $\mathfrak g = \mathfrak{gl}_1$ — rank-24 Heisenberg Yangian with Mukai-signed pairing.
2. The **non-abelian K3 Yangian at ADE enhancement points** — a conjectural object whose sub-Yangians at $A_1, A_2, D_4, D_5, E_6, E_7, E_8$ can be named, and whose putative envelope is $Y_{\osp(4|20)}$.
3. The **orthosymplectic super-Yangian envelope** $Y_{\osp(4|20)}$ — the Mukai-signature adaptation of the super-Yangian of Arnaudon–Crampé–Doikou–Frappat–Ragoucy.

Level 1 is inscribed as `\ClaimStatusProvedHere` (Theorem on lines 877–1001). Level 2 is a patchwork of conditionals and conjectures. Level 3 is uniformly `\ClaimStatusConjectured` with the one exception of Definition 1919 which is `\ClaimStatusProvedElsewhere` (an attribution-style "definition" that merely evaluates the ACDFR presentation at rank $(4,20)$).

Here I attack each as Gelfand would: **what IS this, concretely, to the last sign?**

---

## 1. ROUND 1 ATTACK — Gelfand-style

### Attack 1.1 — Where is the non-abelian K3 Yangian *constructed*?

Search the entire 7078-line file. Everywhere the phrase "non-abelian" or "nonabelian" appears (lines 599, 1265, 1329, 1419, 1445, 1458, 1469, 1500, 1534, 1551, 1562, 1691, 1865, 2023, 3142), the construction is **announced, scoped, or conditionalised** — never written down.

Concrete roll-call:

- **Line 599** (Proposition `prop:k3-formality`): "$\mathfrak g$ non-abelian: class $\geq L$ (from the Lie bracket of $\mathfrak g$; the K3 geometry contributes no higher homotopical data)." — This is a *classification* statement, not a construction.
- **Line 1265** (Conjecture `conj:bkm-yangian-generators`): "whether the simple root vectors of the full BKM superalgebra $\mathfrak g_{\Delta_5}$ (Construction~\ref{constr:k3e-roots}) can be realised as generators of a \emph{non-abelian} K3 Yangian" — *conditional*, not constructive.
- **Line 1329** (same conjecture): "a subset of the Mukai directions merges into a non-abelian subalgebra" — refers to enhancement; no presentation given.
- **Line 1469** (Remark `rem:k3-yangian-obstruction-tests`, Attack A1): "genuine modified crossing for non-abelian $\mathfrak g$" — identifies an *obstruction*; no resolution presented as construction.
- **Line 1691** ($E_8 \times E_8$ discussion): "For the abelian ($\mathfrak{gl}_1$) case, all blocks are diagonal; for the non-abelian enhancement, the $E_8$ blocks acquire off-diagonal entries from the $\mathfrak{e}_8$ structure constants." — narrates what the $R$-matrix *would be*; does not construct the algebra.
- **Line 1865** (the super-Yangian subsection): "candidate for the non-abelian K3 Yangian is therefore $Y_{\osp(4 \mid 20)}$" — word "candidate".
- **Line 2023** (`conj:k3-super-yangian`): "The non-abelian K3 Yangian at ADE enhancement points \emph{is} the orthosymplectic super-Yangian $Y_{\osp(4 \mid 20)}$" — **conjecture**, not theorem.

**Verdict of Attack 1.1.** There is no place in the 7078 lines where a non-abelian K3 Yangian is constructed with its own generators-and-relations presentation. The manuscript is entirely honest about this: every claim is clearly marked conjectural, candidate, or conditional. But the advertised "crown jewel" (abstract line 4–7: "24 Heisenberg generators, Mukai-signature Serre relations, and degree-$(24,24)$ structure function") corresponds to Level 1 (abelian); the Serre relations are *abelian trivial*, and the word "non-abelian" is never backed by a presentation.

### Attack 1.2 — Complete list of generators: is it written out?

**For the abelian case (lines 877–1001, Theorem `thm:k3-abelian-yangian-presentation`):** Yes, to the standard of a Heisenberg Yangian at rank 24. Generators $J_i(z) = \sum J_{i,n} z^{-n-1}$, $i=1,\ldots,24$. OPE $J_i(z) J_j(w) \sim \omega^{ij}/(z-w)^2$. This is just $24$ commuting copies of $Y(\mathfrak{gl}_1)$ twisted by the Mukai sign pattern $\omega = \mathrm{diag}(+1^4, -1^{20})$. **Fine at rank 24**, but **not new**: it is Drinfeld 1985 + Chari–Pressley 1995 + Frenkel–Jing 1988 applied at rank 24 with a sign pattern. The manuscript says so at line 1068–1086 (classical attribution remark).

**For the non-abelian case:** No generator list is written. The closest thing is Conjecture 1267 (`conj:bkm-yangian-generators`), which enumerates *BKM root sectors*:

- 3 real simple roots ($\delta_1, \delta_2, \delta_3$) giving Cartan triples $(h_i, e_i, f_i)$
- 1 timelike imaginary root ($D=-1$) giving "a single current generator $e_W(u)$"
- 10 lightlike imaginary roots ($D=0$) giving "ten generators"
- $|c(D)|$ spacelike imaginary roots for each $D > 0$

The manuscript itself admits (line 1294): *"No Drinfeld presentation for $Y(\mathfrak g)$ exists for any BKM algebra $\mathfrak g$ with nontrivial imaginary simple roots."* So the 3 real-root generators have a textbook Drinfeld presentation, but the $1 + 10 + \sum |c(D)|$ imaginary-root generators have **no known presentation at all**, not in this manuscript, not in the literature.

### Attack 1.3 — Complete list of relations: is it written out?

For the abelian case, yes — but they are *commutation relations only* (all $\gl_1$'s commute; the Mukai signature enters only as signs in $[J_{i,m},J_{j,n}]=\omega^{ij} m \delta_{m+n,0}$). "Mukai-signature Serre relations" as advertised on line 6 is a misnomer: there are no Serre relations in the abelian regime, because $a_{ij}=0$ for all pairs (line 1324: "its $24$ copies of $\gl_1$ commute, so the quantum Serre element … is vacuous when $a_{ij}=0$"). The abstract's phrase is inaccurate against its own Theorem 877.

For the non-abelian case (`conj:k3-serre-enhanced`, lines 1332–1371), the relations are:

- $I_\mathfrak g$: standard simply-laced quantum Serre $E_i^2 E_j - [2]_q E_i E_j E_i + E_j E_i^2 = 0$ at each Dynkin edge — *classical*, not new.
- $I_{\mathrm{mix}} = 0$: mixing Serre between the enhanced block and the abelian complement is trivial by Mukai orthogonality — *asserted* on the basis that the enhancement decomposes the Mukai lattice into an orthogonal direct sum. This is a **lattice claim**, not a Yangian theorem.
- $I_{\mathrm{ab}}$: abelian commutativity on the complement.

Absent from this list: any relation involving the *imaginary roots* beyond the Cartan triples. The conjecture `conj:bkm-yangian-generators` (line 1267) enumerates the generator *classes* but imposes no closure condition. There is no "put generators in, turn the crank, and get relations" construction anywhere in the chapter.

### Attack 1.4 — A worked small-rank example showing non-abelianness?

The closest candidate is "$A_1$ enhancement: $\mathfrak{sl}_2$ inside $\osp(4|20)$" (lines 2153–2163):

> At an $A_1$ enhancement point (nodal K3 with a single rational $(-2)$-curve), the root vector sits in $V_- = \C^{20}$. The $\mathfrak{sl}_2$ subalgebra is the one generated by an $\mathfrak{sp}(2)$-triple inside $\mathfrak{sp}(20) \subset \osp(4 \mid 20)_{\bar 0}$. The $\mathfrak{sl}_2$ RTT is therefore the \emph{standard} (non-super) rational RTT.

This is **not a computation**: it says "the $\mathfrak{sl}_2$ RTT is the standard rational RTT." Which is to say: take the known $Y(\mathfrak{sl}_2)$, declare it is sitting inside a putative $Y_{\osp(4|20)}$. No structure constant of the inclusion is computed. The 8 fermionic entries from the $V_+ \otimes V_-$ coupling are *asserted* ("carry anticommutation relations") without display.

**Compute test backing.** The test file `compute/tests/test_k3_nonabelian_all_ade.py` contains 1196 lines testing an "ADE landscape" for the $R$-matrix, YBE, off-diagonal counts, Cartan matrices, Serre relations, $K3$ embedding. But inspection reveals these tests check **structural consistency of classical objects** (simply-laced ADE Lie-algebra data, Yang R-matrix unitarity $R(u) R(-u) = (1-u^2)\mathrm{Id}$, YBE for the standard Yang permutation at small $N$). They do **not** verify that a specific generator presentation for the non-abelian K3 Yangian closes. Lines 100–105:

```python
('A1', 48), ('A2', 144), ('D4', 294), ('D5', 510), ('E6', 810), ('E7', 1218), ('E8', 1764),
```

These off-diagonal counts come from a formula $d(d-1)(26-d) + \binom{d}{2}(\binom{d}{2}-1)$ (line 117) — a *combinatorial* count of matrix entries, not a verification of Jacobi or Serre.

The adversarial file `compute/lib/k3_yangian_adversarial.py` runs six "attack vectors" and concludes (line 786–794): "The K3 Yangian for $\mathfrak{gl}_1$ at generic moduli is INTERNALLY CONSISTENT." It does not construct the non-abelian case; it only identifies *obstructions* to constructing it.

### Attack 1.5 — The $Y(\mathfrak{sl}_2)$ analogue in the standard literature

For reference, Drinfeld's $Y(\mathfrak{sl}_2)$ has generators $\{e, f, h, J(e), J(f), J(h)\}$ (equivalently the "second Drinfeld presentation" with modes $e_r, f_r, h_r$ for $r \geq 0$), and the terminal closure condition is the relation
$$
[J(h), [J(e), J(f)]] - [h, [J(e), J(f)]] \cdot P(J(h), h) = 0,
$$
where $P$ is the cubic polynomial from Drinfeld's 1985 paper. The Yangian closes *because* this relation, together with deformed Serre, is consistent.

**The analogous list for $Y(\mathfrak g_{K3})$ is nowhere in the manuscript.** The manuscript does not exhibit:

- A distinguished generator $J$ beyond the classical $T$-matrix Lax entries.
- A closure relation analogous to the terminal cubic.
- A non-abelian structure constant computed to the last sign.

The analogue for $Y(\mathfrak{gl}_1)$ is degenerate (no $J$-cubic needed). The abelian K3 Yangian is $24$ copies of this degenerate case. So the manuscript contains, at crown-jewel level, exactly $24$ copies of a trivially degenerate Drinfeld presentation. Everything advertised beyond that is scope declaration.

### Attack 1.6 — The Jacobi identity of $\mathfrak g_{K3}$

Definition 276 (`def:k3-double-current-algebra`) gives the bracket (equation 316):
$$
[J^a_i, J^b_j] = f^{ab}{}_c \sum_k \mu^k_{ij} J^c_k + (T^a, T^b)_{\mathfrak g} \langle \alpha_i, \alpha_j \rangle_{\mathrm{Muk}} \mathbf c.
$$

Here $\mu^k_{ij}$ are the cup product structure constants on $H^*(S, \C)$, and the Mukai pairing is (equation 292):
$$
\langle \alpha, \beta \rangle_{\mathrm{Muk}} = \int_S \alpha \cup \beta \cup \mathrm{td}(S)^{1/2} = (c_1 \cdot c_1') - r \mathrm{ch}_2' - r' \mathrm{ch}_2.
$$

The manuscript's Jacobi-identity claim (line 336): *"The Jacobi identity follows from the Jacobi identity of $\mathfrak g$, the associativity of the cup product, and the $\mathfrak g$-invariance of the Killing form, by the same argument as for classical current algebras."*

**Here is where Gelfand would press.** The **cup product** $\mu^k_{ij}$ and the **Mukai pairing** $\langle \alpha_i, \alpha_j \rangle_{\mathrm{Muk}}$ are **different pairings** on $H^*(S, \C)$:

- The cup product pairing (the "classical" Poincaré pairing) is $(\alpha, \beta)_{\mathrm{PD}} = \int_S \alpha \cup \beta$. On the K3 Mukai decomposition $H^0 \oplus H^2 \oplus H^4 = \C \oplus \C^{22} \oplus \C$, the PD form is $0$ on $H^0 \otimes H^2$, $0$ on $H^2 \otimes H^4$, pairs $H^0 \otimes H^4 \to \C$ with value $1$, and pairs $H^2 \otimes H^2 \to \C$ via the intersection form of signature $(3,19)$. **Note: $(H^0, H^0)_{\mathrm{PD}} = 0$** (since $H^0 \cup H^0 = H^0 \neq H^4$), and **$(H^4, H^4)_{\mathrm{PD}} = 0$** (out of range).
- The Mukai pairing has an **extra sign flip** between $H^0$ and $H^4$: $\langle (r, 0, 0), (0, 0, s) \rangle_{\mathrm{Muk}} = -rs$ (from the $-r \mathrm{ch}_2' - r' \mathrm{ch}_2$ term), and $\langle (r, 0, 0), (r', 0, 0) \rangle = 0$. Integrated against $\mathrm{td}^{1/2}$, the Mukai form on the $U$-plane spanned by $H^0, H^4$ is **hyperbolic** (signature $(1,1)$), *not* the classical PD form (which has signature $(0,0) = $ null on that $U$-plane — it only pairs $H^0$ with $H^4$).

These are **both** hyperbolic forms on the $U = H^0 \oplus H^4$ plane up to basis change. OK. Now the question:

**Does the bracket satisfy Jacobi with the Mukai pairing (not the PD pairing) in the central term?**

The standard central-extension argument requires:

- Cocycle condition: $\omega([x,y], z) + \omega([y,z], x) + \omega([z,x], y) = 0$ where $\omega$ is the cocycle.

In the current-algebra case, $\omega(T^a \otimes r, T^b \otimes s) = (T^a, T^b)_{\mathfrak g} \cdot \chi(r, s) \cdot \mathbf c$ for a pairing $\chi$ on the commutative algebra $R$. The 2-cocycle condition on $\mathfrak g \otimes R$ requires

$$
\chi(rs, t) + \chi(st, r) + \chi(tr, s) = 0
$$

(the "trace" condition). For $R = H^*(S, \C)$ with $\chi = \langle \cdot, \cdot \rangle_{\mathrm{Muk}}$ and multiplication $=$ cup product:

- For $r \in H^p, s \in H^q, t \in H^{p'}$ with $p + q + p' + \deg(\chi) = \deg_{\mathrm{total}}$, the cocycle condition holds by degree counting and the symmetry/gradedness of the pairing. The Mukai pairing $\int_S (\cdot) \cup (\cdot) \cup \mathrm{td}^{1/2}$ is nondegenerate on $H^{\mathrm{even}}$ and picks out the top-degree piece after multiplying by $\mathrm{td}^{1/2}$. Because $\mathrm{td}(S)^{1/2} = 1 + \tfrac{1}{2} c_1 + \tfrac{1}{24}(c_1^2 + 2 c_2) + \cdots$ and $c_1(K3) = 0$, we have $\mathrm{td}^{1/2}(K3) = 1 + \tfrac{1}{12} c_2 = 1 + 2 \cdot [\mathrm{pt}]$ (since $c_2(K3) = 24 [\mathrm{pt}]$ is the Euler class, and so $\tfrac{1}{12} c_2 = 2[\mathrm{pt}]$). Thus on K3, $\mathrm{td}^{1/2}$ equals $1 + 2[\mathrm{pt}]$, and the Mukai pairing is the Poincaré pairing **plus** a correction $-2 r r'$ (from the $1 \cdot 2[\mathrm{pt}]$ cross term). So the Mukai form differs from the PD form by a rank-$1$ shift on the $H^0$-block; both are integral symmetric forms, both are nondegenerate, and the trace-condition computation comes down to the graded Frobenius property: $\int_S (a \cup b) \cdot c = \int_S a \cdot (b \cup c)$. Since cup product is associative, this trace condition holds for *both* the PD pairing and the Mukai pairing.

So Jacobi holds. **The programme survives this attack.** But the manuscript's two-sentence "follows from Jacobi of $\mathfrak g$, associativity of cup product, $\mathfrak g$-invariance of the Killing form" is incomplete: **the trace condition on the $R$-pairing is the *fourth* required input**, and it happens to hold for the Mukai pairing on $H^*(K3)$ by the graded-Frobenius property of Poincaré duality. The proof body should name this ingredient explicitly (as "(iv) graded Frobenius trace condition on $(H^*(S), \cup, \langle,\rangle_{\mathrm{Muk}})$").

This is a **recoverable flaw** (healed below).

### Attack 1.7 — Is $\mathfrak g_{K3}$ actually a Lie algebra at the non-abelian level?

The Definition 276 bracket is:
$$
[J^a_i, J^b_j] = f^{ab}{}_c \sum_k \mu^k_{ij} J^c_k + (T^a, T^b)_{\mathfrak g} \cdot \langle \alpha_i, \alpha_j \rangle_{\mathrm{Muk}} \cdot \mathbf c.
$$

For $\mathfrak g$ simple non-abelian, this requires Jacobi on triples $([J^a_i, J^b_j], J^c_k)$. Expanding:
$$
[[J^a_i, J^b_j], J^c_k] = f^{ab}{}_d \mu^e_{ij} [J^d_e, J^c_k] = f^{ab}{}_d f^{dc}{}_{d'} \mu^e_{ij} \mu^{e'}_{ek} J^{d'}_{e'} + (\text{central part}).
$$

Cycling $(a,i), (b,j), (c,k)$ and summing, the Lie-algebra (structure-constant) part vanishes by the **simultaneous** Jacobi of $f$ (for $\mathfrak g$) and **associativity** of $\mu$ (for cup product), both of which are classical. The central part requires the graded trace condition on $(\mu, \langle,\rangle)$. So the Jacobi identity *does* hold.

**But is $\mathfrak g_{K3}$ *non-abelian*?** The answer is **yes**, provided $\mathfrak g$ is non-abelian and $\mu^k_{ij}$ is nonzero. Concretely:

- $\mathfrak g = \mathfrak{sl}_2$ has $f^{+-}{}_h = 1$, $f^{h \pm}{}_\pm = \pm 2$.
- $\mu^k_{ij}$ on $H^*(K3)$: the only nontrivial cup products are $H^0 \cup H^p = H^p$ (trivial, tautological), and $H^2 \otimes H^2 \to H^4$ via the intersection form $Q_{ij}$ of signature $(3,19)$.

So $[\mathfrak{sl}_2 \otimes H^2, \mathfrak{sl}_2 \otimes H^2] \to \mathfrak{sl}_2 \otimes H^4 \oplus (\text{central})$. A genuine **non-abelian** bracket requires at least one non-zero cup product on $H^{\geq 2}$ AND $\mathfrak g$-bracket non-zero. E.g.
$$
[T^+ \otimes \omega_i, T^- \otimes \omega_j] = f^{+-}{}_h \cdot Q_{ij} \cdot (T^h \otimes [\mathrm{pt}]) + (T^+, T^-)_{\mathfrak g} \cdot (\omega_i, \omega_j)_{\mathrm{Muk}} \cdot \mathbf c.
$$

This is a non-trivial element of $\mathfrak g \otimes H^4$. The first non-abelian structure constant I will compute in the HEAL below is exactly this.

### Attack 1.8 — The $\osp(4|20)$ claim is type-mismatched

The super-Yangian subsection (line 1855–2217) says the Mukai form has signature $(4,20)$, and because the automorphism group is $\mathrm{O}(4,20)$ (not the general linear supergroup), the super-Yangian attached is orthosymplectic. This argument is **partially correct and partially wrong**.

Concretely (see Remark 2055, `rem:so-4-20-alternative`, which the manuscript itself flags):

- If we want the *non-super* Yangian preserving the Mukai form $\omega$ on $\C^{24}$ of signature $(4,20)$, the answer is $Y(\mathfrak{so}(4,20))$, a real form of $Y(\mathfrak{so}_{24}(\C))$. This is a **well-defined classical Yangian** with a textbook Drinfeld presentation.
- If we want a *super* Yangian on the super-vector space $V = \C^4 \oplus \Pi \C^{20}$ (even + parity-reversed odd), the answer is $Y(\mathfrak{osp}(4|20))$. This is a **different** algebra: its underlying super-Lie algebra $\mathfrak{osp}(4|20)$ has bosonic part $\mathfrak{so}(4) \oplus \mathfrak{sp}(20)$ (dim $6 + 210 = 216$) and fermionic part $\C^4 \otimes \C^{20}$ (dim $80$), total dim $296$.
- These two are **not isomorphic as Yangians.** The manuscript acknowledges this at line 2061: "The $\mathfrak{so}(4,20)$ and $\mathfrak{osp}(4|20)$ Yangians are distinct algebras: the former is a real form of $Y(\mathfrak{so}_{24})$, the latter is a super-Yangian with a Berezinian centre."

The manuscript's choice of $\mathfrak{osp}(4|20)$ over $\mathfrak{so}(4,20)$ is **not forced** by the Mukai signature. The argument at Remark 2002 ("Signature-type discipline: orthosymplectic, not general-linear") argues against $\mathfrak{gl}(4|20)$ but **does not** justify the super-structure over the non-super $\mathfrak{so}(4,20)$. The manuscript's own Remark 2055 admits this: *"Which is physically correct is determined by the N=(2,2) worldsheet boundary algebra of K3 at the ADE enhancement point: the BRST-invariant boundary sector is super-graded, favouring $\mathfrak{osp}(4|20)$, but this is conjectural."*

**So the super-envelope is a physics-motivated guess, not a mathematical necessity.** The non-super $Y(\mathfrak{so}(4,20))$ is a more conservative, fully-classical candidate.

---

## 2. ROUND 1 HEAL — the smallest defensible non-abelian core

Stripping away every conjectural layer, here is what the manuscript actually *proves* (or can be brought to proof status with at most minor polishing):

### H1.1 The classical K3 double current algebra $\mathfrak g_{K3}$

**Definition** (lossless rewording of `def:k3-double-current-algebra`).
Let $\mathfrak g$ be a finite-dimensional simple Lie algebra over $\C$ with basis $\{T^a\}_{a=1}^{\dim \mathfrak g}$, structure constants $[T^a, T^b] = f^{ab}{}_c T^c$, and invariant form $(T^a, T^b)_{\mathfrak g} = \mathrm{tr}(\mathrm{ad}_{T^a} \mathrm{ad}_{T^b})$ (the Killing form up to normalization). Let $S$ be a K3 surface and $H^*(S, \C) = H^0 \oplus H^2 \oplus H^4$ (dimensions $1, 22, 1$). Choose a basis $\{\alpha_i\}_{i=0}^{23}$ with $\alpha_0 = 1 \in H^0$, $\alpha_1, \ldots, \alpha_{22}$ a basis of $H^2$, $\alpha_{23} = [\mathrm{pt}] \in H^4$. Write $\alpha_i \cup \alpha_j = \sum_k \mu^k_{ij} \alpha_k$.

The Mukai pairing $\langle \cdot, \cdot \rangle_{\mathrm{Muk}}$ on $H^*(S, \C)$ is the bilinear form
$\langle \alpha, \beta \rangle_{\mathrm{Muk}} = \int_S \alpha \cup \beta \cup \sqrt{\mathrm{td}(S)}$,
which on $K3$ (where $c_1 = 0$, $\sqrt{\mathrm{td}(S)} = 1 + 2 [\mathrm{pt}]$) reduces in coordinates $(r, c_1, \mathrm{ch}_2)$ to $\langle \alpha, \beta \rangle = (c_1 \cdot c_1') - r \mathrm{ch}_2' - r' \mathrm{ch}_2$. This form has signature $(4, 20)$ on the integral lattice $\widetilde{\Lambda}_{K3} = U^3 \oplus E_8(-1)^2$.

Define $\mathfrak g_{K3} := (\mathfrak g \otimes H^*(S, \C)) \oplus \C \mathbf c$ with generators $J^a_i := T^a \otimes \alpha_i$ and central element $\mathbf c$, subject to
$$
[J^a_i, J^b_j] = f^{ab}{}_c \sum_k \mu^k_{ij} J^c_k + (T^a, T^b)_{\mathfrak g} \langle \alpha_i, \alpha_j \rangle_{\mathrm{Muk}} \mathbf c.
$$

**Theorem (Jacobi).** The bracket above makes $\mathfrak g_{K3}$ into a $\bZ$-graded Lie algebra of total dimension $24 \dim \mathfrak g + 1$.

**Proof.** Four ingredients (the manuscript lists three; I add the fourth):

1. Jacobi of $\mathfrak g$: $\sum_{\mathrm{cyclic}} f^{ab}{}_d f^{dc}{}_e = 0$.
2. Associativity of cup product: $\mu^k_{ij} \mu^\ell_{km} = \mu^k_{jm} \mu^\ell_{ik}$ (after symmetrization).
3. $\mathfrak g$-invariance of $(\cdot,\cdot)_{\mathfrak g}$: $f^{ab}{}_c (T^c, T^d) + f^{ad}{}_c (T^b, T^c) = 0$.
4. **Graded Frobenius trace on $H^*(S)$:** $\int_S (\alpha \cup \beta) \cup \gamma \cdot \sqrt{\mathrm{td}(S)} = \int_S \alpha \cup (\beta \cup \gamma) \cdot \sqrt{\mathrm{td}(S)}$ (i.e. the pairing $\langle\cdot,\cdot\rangle_{\mathrm{Muk}}$ is the trace of a commutative Frobenius algebra). This holds because $\sqrt{\mathrm{td}(S)}$ is a central element of $H^*(S)$ (it is a polynomial in cohomology classes), so multiplying by it commutes with cup product.

Combining, the structure-constant part vanishes by (1)+(2), and the central-extension part vanishes by (3)+(4). $\square$

This upgrades the manuscript's proof body by naming the fourth ingredient explicitly. Status: **ProvedHere after healing.**

### H1.2 The rank-24 **abelian** Heisenberg Yangian

At $\mathfrak g = \mathfrak{gl}_1$, the above gives $H_{\mathrm{Muk}}$, a rank-24 Heisenberg algebra with pairing $\omega = \mathrm{diag}(+1^4, -1^{20})$ in a Mukai-diagonal basis. The Yangian $Y(H_{\mathrm{Muk}}) = 24$ commuting copies of $Y(\mathfrak{gl}_1)$ with signed OPE. This **is** a rank-24 abelian Yangian in the Drinfeld–Chari–Pressley sense, and matches the manuscript's Theorem 877. Status: **Proved (classical)**.

### H1.3 The non-abelian K3 Yangian Y(\mathfrak g_{K3}) — what survives

Defining $Y(\mathfrak g_{K3})$ as "the canonical Yangian deformation of $U(\mathfrak g_{K3})$" is a **definition by invocation**, not a construction. The standard Drinfeld construction of $Y(\mathfrak g)$ for simple $\mathfrak g$ uses the minimalist $J$-presentation with a terminal cubic relation. For $\mathfrak g_{K3}$ (non-simple, $\bZ$-graded, 2-step-nilpotent in the $\mathbf c$-direction):

- The **first Drinfeld presentation** (generators $J^a_i$ for $|0\rangle$-level, $J(J^a_i)$ for $|1\rangle$-level, with quadratic relations encoding the Lie structure plus a single cubic terminal relation) generalises formally but requires the input Lie algebra to carry an $\mathfrak g$-invariant non-degenerate form. $\mathfrak g_{K3}$ does: the bilinear form is $(J^a_i, J^b_j)_{\mathfrak g_{K3}} = (T^a, T^b)_{\mathfrak g} \cdot \langle \alpha_i, \alpha_j\rangle_{\mathrm{Muk}}$, which is non-degenerate because both factors are.
- The **terminal cubic** $[J(J^a_i), J(J^b_j)] - J([J^a_i, J^b_j]) = (\text{cubic in } J^c_k)$ with coefficients from the Killing form, cup product, and Mukai pairing, can be formally written down. Its consistency (the Jacobi-type check for the cubic obstruction) reduces to the same four ingredients as Round 1.6.
- Result: $Y(\mathfrak g_{K3})$ has a formal Drinfeld-1985 presentation. **This is the smallest defensible non-abelian core.**

**Status after healing:** `\ClaimStatusConjectured` upgrades to `\ClaimStatusProvedElsewhere(stretched)` by invoking Chari–Pressley 1995 Thm 12.1.1 at full generality — which applies because $\mathfrak g_{K3}$ has a non-degenerate invariant form. **But the explicit presentation (generators + relations to the last sign) is nowhere written in the manuscript.** That is the specific gap.

---

## 3. ROUND 2 ATTACK — attack the heal

### Attack 2.1 — Is $\mathfrak g_{K3}$ really non-abelian?

For $\mathfrak g = \mathfrak{sl}_2$, consider the sub-Lie-algebra spanned by $\{J^\pm_i, J^h_i, \mathbf c\}$ for $i = 1, \ldots, 22$ (the $H^2$-sector). The bracket
$$
[J^+_i, J^-_j] = f^{+-}{}_h \sum_k \mu^k_{ij} J^h_k + (T^+, T^-) \langle \alpha_i, \alpha_j \rangle \mathbf c.
$$

For $\alpha_i, \alpha_j \in H^2$: $\alpha_i \cup \alpha_j \in H^4 = \C \cdot [\mathrm{pt}]$. So $\mu^k_{ij} = Q_{ij} \delta_{k, 23}$ where $Q_{ij}$ is the intersection form of signature $(3,19)$. Then:
$$
[J^+_i, J^-_j] = Q_{ij} J^h_{23} + (T^+, T^-) \langle \alpha_i, \alpha_j \rangle_{\mathrm{Muk}} \mathbf c.
$$

For $i, j \in H^2$, $\langle \alpha_i, \alpha_j \rangle_{\mathrm{Muk}} = \int_S \alpha_i \cup \alpha_j \cup (1 + 2[\mathrm{pt}]) = \int_S \alpha_i \cup \alpha_j = Q_{ij}$ (the $[\mathrm{pt}]$ correction is killed by degree: $\alpha_i \cup \alpha_j \in H^4$, and $H^4 \cdot H^4 = 0$).

So
$$
\boxed{[J^+_i, J^-_j] = Q_{ij} J^h_{23} + (T^+, T^-)_{\mathfrak{sl}_2} \cdot Q_{ij} \cdot \mathbf c.} \quad (i, j \in \{1, \ldots, 22\})
$$

With $(T^+, T^-)_{\mathfrak{sl}_2} = 1$ in the standard Killing-form normalization (Killing: $(T^+, T^-) = 4$, trace form: $(T^+, T^-) = 1$; we take the trace form for simplicity). Then:
$$
[J^+_i, J^-_j] = Q_{ij}(J^h_{23} + \mathbf c).
$$

This is **non-zero** whenever $Q_{ij} \neq 0$, and **non-abelian** because $J^h_{23}$ is a distinguished generator. Let $H := J^h_{23} + \mathbf c$ (rescale). The pattern is:
$$
[J^+_i, J^-_j] = Q_{ij} H, \qquad [H, J^\pm_i] = ?
$$

For the second bracket: $[J^h_{23}, J^\pm_i] = f^{h\pm}{}_\pm \sum_k \mu^k_{23,i} J^\pm_k + (T^h, T^\pm) \langle \alpha_{23}, \alpha_i\rangle_{\mathrm{Muk}} \mathbf c$. Now $f^{h+}{}_+ = 2$, $f^{h-}{}_- = -2$; $\mu^k_{23,i} = \delta_{k,i}$ (since $[\mathrm{pt}] \cup \alpha_i = 0$ for $\alpha_i \in H^{2}$ or $H^4$, and $= \alpha_i$ only when $\alpha_i \in H^0$, i.e. $i=0$; but $i \in \{1,\ldots,22\}$, so $\mu^k_{23,i} = 0$). And $\langle \alpha_{23}, \alpha_i\rangle_{\mathrm{Muk}} = -r \delta_{i,0}$ for $\alpha_i = r \cdot \alpha_0 + (\text{rest})$; for $i \in \{1,\ldots,22\}$ with $\alpha_i \in H^2$, the Mukai pairing vanishes by degree.

**So $[H, J^\pm_i] = 0$ for $i \in \{1, \ldots, 22\}$.**

Interpretation: $H$ commutes with the $J^\pm_i$. So we have a Heisenberg-like subalgebra with bracket $[J^+_i, J^-_j] = Q_{ij} H$ and $[H, J^\pm_i] = 0$. That's **not** abelian — it's a **central extension** of $\mathbb C^{22}_+ \oplus \mathbb C^{22}_-$ by $H$, with cocycle the intersection form $Q$ of signature $(3, 19)$.

This is the **Heisenberg algebra of the $\mathrm{II}_{3,19}$ lattice** — a classical object — but dressed with an $\mathfrak{sl}_2$-valued structure that is non-trivially non-abelian.

### Attack 2.2 — Is this "just the Heisenberg"? Where is the genuine Lie-bracket action?

The bracket in 2.1 is Heisenberg-like because only the $J^\pm_i \otimes J^\mp_j$ pair generates the $H^4$-piece. But if we go to $H^0$-level, there is a **non-trivial Lie-bracket action**:
$$
[J^a_0, J^b_j] = f^{ab}{}_c \sum_k \mu^k_{0,j} J^c_k + (T^a, T^b) \langle \alpha_0, \alpha_j\rangle \mathbf c.
$$

Now $\mu^k_{0,j} = \delta_{k,j}$ (since $1 \cup \alpha_j = \alpha_j$), and $\langle \alpha_0, \alpha_j\rangle_{\mathrm{Muk}} = -\mathrm{ch}_2(\alpha_j) = -\delta_{j, 23}$ (since $\alpha_{23} = [\mathrm{pt}]$). So:
$$
[J^a_0, J^b_j] = f^{ab}{}_c J^c_j + (T^a, T^b) (-\delta_{j, 23}) \mathbf c.
$$

**This is genuinely non-abelian**: the $H^0$-sector $\{J^a_0\}$ acts on every $\{J^b_j\}$ by the full Lie algebra $\mathfrak g$.

**The $H^0$-sector is a copy of $\mathfrak g$ embedded in $\mathfrak g_{K3}$**: $[J^a_0, J^b_0] = f^{ab}{}_c J^c_0$. And this copy of $\mathfrak g$ acts on every $J^b_j$ by the adjoint. Explicitly, $J^a_0$ is the generator of the "constant" part of $\mathfrak g \otimes H^0$, and the whole $\mathfrak g_{K3}$ splits as
$$
\mathfrak g_{K3} = \mathfrak g \oplus (\mathfrak g \otimes H^2(S)) \oplus (\mathfrak g \otimes H^4(S)) \oplus \C \mathbf c
$$
as a $\mathfrak g$-module (where $\mathfrak g$ means $\mathfrak g \otimes H^0 = \mathfrak g \otimes \C \cdot \alpha_0$), with the non-trivial Lie-algebra structure enters through (i) the $\mathfrak g$-action on each piece via $[J^a_0, J^b_j]$, (ii) the $H^2 \otimes H^2 \to H^4$ pairing via $[J^a_i, J^b_j]$ for $i, j \in \{1, \ldots, 22\}$, and (iii) the central charge from $\langle\cdot,\cdot\rangle_{\mathrm{Muk}}$.

### Attack 2.3 — The first genuine non-abelian structure constant, to the last sign

Take $\mathfrak g = \mathfrak{sl}_2$, standard basis $(e, f, h)$ with $[e, f] = h$, $[h, e] = 2e$, $[h, f] = -2f$. Trace form $(e, f) = 1$, $(h, h) = 2$, $(e, e) = (f, f) = (h, e) = (h, f) = 0$.

Take two orthogonal $(-2)$-classes $\alpha_1, \alpha_2 \in H^{1,1}(S, \bZ)$ with $Q(\alpha_1, \alpha_2) = Q_{12}$. Compute:
$$
[J^e_1, J^f_2] = f^{ef}{}_h \cdot \mu^k_{12} \cdot J^h_k + (e, f) \cdot \langle \alpha_1, \alpha_2\rangle \cdot \mathbf c.
$$

We have $f^{ef}{}_h = 1$; $\mu^k_{12} = Q_{12} \delta_{k, 23}$ (from $H^2 \cup H^2 \to H^4$); $(e, f) = 1$; $\langle \alpha_1, \alpha_2\rangle_{\mathrm{Muk}} = Q_{12}$ (since the Todd correction drops out by degree for $H^2$-classes). So:
$$
\boxed{[J^e_1, J^f_2] = Q_{12} J^h_{23} + Q_{12} \mathbf c = Q_{12} (J^h_{23} + \mathbf c).}
$$

**First non-trivial non-abelian structure constant:** $c^{e \otimes \alpha_1, f \otimes \alpha_2}_{h \otimes \alpha_{23}} = Q_{12}$. $c^{e \otimes \alpha_1, f \otimes \alpha_2}_{\mathbf c} = Q_{12}$.

Now the Jacobi test on $(J^e_1, J^f_2, J^e_3)$ for $\alpha_3 \in H^2$:
- $[[J^e_1, J^f_2], J^e_3] = Q_{12} [J^h_{23}, J^e_3] + Q_{12} [\mathbf c, J^e_3] = Q_{12} \cdot 0 + 0 = 0$ (since $[\mathrm{pt}] \cup \alpha_3 = 0$, killing the first term; second term vanishes by centrality).
- $[[J^f_2, J^e_3], J^e_1] = -[[J^e_3, J^f_2], J^e_1] = -Q_{23} [J^h_{23}, J^e_1] = 0$ (same reason).
- $[[J^e_3, J^e_1], J^f_2] = [0 + 0, J^f_2] = 0$ (since $f^{ee}{}_* = 0$).

Sum $= 0$. **Jacobi passes on this triple.** ✓

Do another: $(J^e_1, J^f_2, J^h_0)$:
- $[[J^e_1, J^f_2], J^h_0] = Q_{12} [J^h_{23}, J^h_0]$. Now $[J^h_{23}, J^h_0] = f^{hh}{}_c \sum_k \mu^k_{23,0} J^c_k + (h,h) \langle \alpha_{23}, \alpha_0\rangle \mathbf c = 0 + 2 \cdot (-1) \mathbf c = -2\mathbf c$ (since $f^{hh}{}_c = 0$ for $\mathfrak{sl}_2$, and $\langle [\mathrm{pt}], 1\rangle_{\mathrm{Muk}} = -1$). So this term $= -2 Q_{12} \mathbf c$.
- $[[J^f_2, J^h_0], J^e_1] = [-f^{fh}{}_f \mu^k_{2,0} J^f_k + (f, h) \cdots, J^e_1] = [-(-2) J^f_2 + 0, J^e_1]$ (since $\mu^k_{2,0} = \delta_{k,2}$, $f^{fh}{}_f = -f^{hf}{}_f = -(-2) = 2$... let me recompute signs carefully). We have $[h, f] = -2 f$, so $f^{hf}{}_f = -2$ (with $[T^a, T^b] = f^{ab}{}_c T^c$). Hence $[J^h_0, J^f_2] = f^{hf}{}_c \mu^k_{02} J^c_k = -2 \cdot \delta_{k,2} \cdot J^f_2 = -2 J^f_2$. So $[J^f_2, J^h_0] = 2 J^f_2$. Then $[[J^f_2, J^h_0], J^e_1] = [2 J^f_2, J^e_1] = -2 [J^e_1, J^f_2] = -2 Q_{12}(J^h_{23} + \mathbf c)$.
- $[[J^h_0, J^e_1], J^f_2]$: $[J^h_0, J^e_1] = f^{he}{}_c \mu^k_{01} J^c_k = 2 \cdot \delta_{k,1} \cdot J^e_1 = 2 J^e_1$. Then $[2 J^e_1, J^f_2] = 2 Q_{12}(J^h_{23} + \mathbf c)$.

Sum: $-2 Q_{12} \mathbf c + (-2 Q_{12})(J^h_{23} + \mathbf c) + 2 Q_{12}(J^h_{23} + \mathbf c) = -2 Q_{12} \mathbf c + 0 = -2 Q_{12} \mathbf c$.

**This is non-zero.** The Jacobi identity is **violated** on this triple??

Let me recompute. The Jacobi identity is
$$
[[X, Y], Z] + [[Y, Z], X] + [[Z, X], Y] = 0.
$$

Take $X = J^e_1$, $Y = J^f_2$, $Z = J^h_0$.

- $[X, Y] = [J^e_1, J^f_2] = Q_{12}(J^h_{23} + \mathbf c)$.
- $[[X,Y], Z] = [Q_{12}(J^h_{23} + \mathbf c), J^h_0] = Q_{12} [J^h_{23}, J^h_0] + 0$. And $[J^h_{23}, J^h_0] = f^{hh}{}_c \mu^k_{23,0} J^c_k + (h,h)\langle \alpha_{23}, \alpha_0\rangle \mathbf c = 0 + 2 \cdot (-1) \mathbf c = -2\mathbf c$. So $[[X,Y],Z] = -2 Q_{12} \mathbf c$.
- $[Y, Z] = [J^f_2, J^h_0] = -[J^h_0, J^f_2] = -(-2 J^f_2) = 2 J^f_2$ using $[J^h_0, J^f_2] = f^{hf}{}_c \mu^k_{02} J^c_k = -2 \delta_{k,2} J^f_2 = -2 J^f_2$.
- $[[Y,Z], X] = [2 J^f_2, J^e_1] = -2 [J^e_1, J^f_2] = -2 Q_{12}(J^h_{23} + \mathbf c)$.
- $[Z, X] = [J^h_0, J^e_1] = 2 \delta_{k,1} J^e_1 = 2 J^e_1$.
- $[[Z,X], Y] = [2 J^e_1, J^f_2] = 2 Q_{12}(J^h_{23} + \mathbf c)$.

Sum: $-2 Q_{12} \mathbf c - 2 Q_{12}(J^h_{23} + \mathbf c) + 2 Q_{12}(J^h_{23} + \mathbf c) = -2 Q_{12} \mathbf c$.

**Jacobi fails by $-2 Q_{12} \mathbf c$.**

This is a **precise numerical anomaly**. It means the bracket as written in `def:k3-double-current-algebra` equation 316 does not quite define a Lie algebra. There must be a sign or normalization convention that fixes this.

Let me audit my computation. The bracket is
$$
[J^a_i, J^b_j] = f^{ab}{}_c \sum_k \mu^k_{ij} J^c_k + (T^a, T^b)_{\mathfrak g} \langle \alpha_i, \alpha_j\rangle_{\mathrm{Muk}} \mathbf c.
$$

Check if this is antisymmetric. $[J^b_j, J^a_i] = f^{ba}{}_c \mu^k_{ji} J^c_k + (T^b, T^a)\langle \alpha_j, \alpha_i\rangle \mathbf c = -f^{ab}{}_c \mu^k_{ij} J^c_k + (T^a, T^b)\langle\alpha_i, \alpha_j\rangle \mathbf c$ (using $\mu$ symmetric in $i,j$: graded-commutative cup product on even cohomology is commutative). So antisymmetry requires $\langle\alpha_i, \alpha_j\rangle = -\langle \alpha_j, \alpha_i\rangle$, i.e. the Mukai pairing is *antisymmetric*. But the Mukai pairing is **symmetric** on $H^*(K3)$ (as a genuine orthogonal form of signature $(4,20)$)!

**So the bracket as written in equation 316 is not antisymmetric and does not define a Lie algebra.**

Wait — let me re-check. $\mu^k_{ij}$ for cup product is symmetric in $(i,j)$ because cup on even-degree classes is commutative. $f^{ab}{}_c$ is antisymmetric in $(a,b)$. $(T^a, T^b)$ is symmetric. So
$$
[J^a_i, J^b_j] - (-[J^b_j, J^a_i])
= 2[(T^a, T^b) \langle\alpha_i, \alpha_j\rangle \mathbf c]
$$
when $\langle \cdot, \cdot \rangle$ is *symmetric* (not antisymmetric). This means the central term fails antisymmetry.

**The DCA bracket of equation 316 as written is not a Lie bracket.**

For a central extension to define a Lie algebra on $(\mathfrak g \otimes R) \oplus \C \mathbf c$, one needs the cocycle $\omega \colon (\mathfrak g \otimes R)^{\otimes 2} \to \C$ to be *antisymmetric*. With $\omega(T^a \otimes r, T^b \otimes s) = (T^a, T^b)_{\mathfrak g} \langle r, s\rangle_R$, antisymmetry requires:
- $(T^a, T^b)$ symmetric $\times$ $\langle r, s\rangle$ antisymmetric ⟹ antisymmetric product: ✓ if $\langle\cdot,\cdot\rangle$ is antisymmetric, or
- $(T^a, T^b)$ antisymmetric $\times$ $\langle r, s\rangle$ symmetric ⟹ antisymmetric product: would need antisymmetric Killing form (impossible for semisimple $\mathfrak g$).

For the classical DDCA $\mathfrak g \otimes \C[u,v]$ with residue pairing $\langle f,g\rangle = \mathrm{Res} fg \, du\wedge dv$: the residue pairing **is antisymmetric** (it's the residue of a 2-form at the origin, which is a skew-symmetric pairing on test functions modulo constants).

For the K3 analogue with the **symmetric** Mukai pairing: the central term of equation 316 **cannot** be the cocycle. The correct analogue is to replace the Mukai pairing by an antisymmetric form — which on an orthogonal space of signature $(4,20)$ **does not exist canonically**.

Options:
1. **Differentiate:** replace $\langle \alpha_i, \alpha_j\rangle$ with $\langle \alpha_i, d\alpha_j\rangle$ for some exterior derivative $d$ — but $H^*(S)$ is a ring, not a DGA with interior structure on $K3$.
2. **Use the graded Poincaré pairing instead:** $\langle \alpha, \beta\rangle_{PD} = \int_S \alpha \wedge \beta$. For even-degree classes on K3, this is symmetric too. Not helpful.
3. **Introduce parity:** grade cohomology classes and use a graded antisymmetric pairing. On $H^{\mathrm{even}}$ of K3, $(\alpha, \beta) \mapsto (-1)^{|\alpha||\beta|}$ is always $+1$, so no help.
4. **Accept that $\mathfrak g_{K3}$ is a super-Lie algebra, not a Lie algebra.** If we put $H^0 \oplus H^4$ in even grade and $H^2$ in odd grade (or vice versa), then the pairing becomes graded-antisymmetric on the odd piece. But then $\mathfrak g \otimes H^2$ is **odd**, and we're looking at the super version.
5. **The manuscript's bracket has a sign error or implicit $\sqrt{\mathrm{td}}$-twist:** A different version of the bracket might be antisymmetric.

Let me check option 4 carefully. If $\alpha_i \in H^2$ is assigned odd grade (call this $|\alpha| = 1$), then $J^a_i = T^a \otimes \alpha_i$ is odd. The (super-)bracket becomes
$$
[J^a_i, J^b_j] = (-1)^{|J^a_i||J^b_j|} \cdot (\text{stuff})
$$
and the super-antisymmetry $[X, Y] = -(-1)^{|X||Y|} [Y, X]$ on odd$\otimes$odd elements gives **symmetric** bracket (since $(-1)^{1 \cdot 1} = -1$ and $-(-1)^{1 \cdot 1} = +1$). That flips exactly the relevant sign.

So: **$\mathfrak g_{K3}$ is a super-Lie algebra with the even/odd grading from cohomological parity** ($H^0, H^4$ even; $H^2$ odd), and the bracket of equation 316 is then a **super-Lie bracket**. In that case:

- $[J^a_i, J^b_j] + (-1)^{|i||j|} [J^b_j, J^a_i]$ should be $0$.
- For $i, j$ both in $H^2$ (both odd): $(-1)^{|i||j|} = -1$, super-antisymmetry gives $[J^a_i, J^b_j] = +[J^b_j, J^a_i]$, i.e. the bracket is **symmetric** on odd$\otimes$odd.
- Classical antisymmetry: $f^{ab}{}_c \mu^k_{ij}$ is antisymmetric in $(a,b)$ but symmetric in $(i,j)$. On odd$\otimes$odd, we want *symmetric* in $(a,b,i,j)$-swap: $f^{ab}{}_c \mu^k_{ij} \mapsto -f^{ab}{}_c \mu^k_{ji} = -f^{ab}{}_c\mu^k_{ij}$, with super-swap sign $-1$ gives $+f^{ab}{}_c \mu^k_{ij}$. Hmm. This requires careful tracking.

**The upshot:** the manuscript's bracket of equation 316 works **only** if the grading is adjusted so that cohomology classes carry cohomological parity. The manuscript at equation 316 does *not* write this explicitly, but the discussion of $\mathfrak{osp}(4|20)$ at Section 1855 onward implicitly relies on exactly this kind of super-structure.

**Gelfand would shout: "Write down the grading! Are the $J^a_i$ even or odd? Make the super-Jacobi identity explicit!"** The manuscript does not.

### Attack 2.4 — So what is it really?

Without the super-structure, $\mathfrak g_{K3}$ as defined in equation 316 fails antisymmetry on $\mathrm{central} \otimes (\text{odd-cohomology pair})$. With the super-structure from cohomological parity, it works — but then $\mathfrak g_{K3}$ is a **super-Lie algebra**, not a Lie algebra. The manuscript is silent on this. **This is a real, precise, currently-present error in the proof body of Definition 276 / Proposition 458 / the Jacobi-identity remark on line 336.**

---

## 4. ROUND 2 HEAL

### H2.1 The corrected $\mathfrak g_{K3}$: cohomological-parity super-Lie algebra

**Corrected Definition.** Let $\mathfrak g$ be a simple Lie algebra. Assign cohomological parity: $H^0, H^4$ have parity $\bar 0$ (even), $H^2$ has parity $\bar 1$ (odd). Define $\mathfrak g_{K3}$ as the super-vector space $(\mathfrak g \otimes H^*(S, \C)) \oplus \C \mathbf c$ with $\bZ/2$-grading inherited, with the super-bracket
$$
[J^a_i, J^b_j]_{\mathrm{super}} = f^{ab}{}_c \sum_k \mu^k_{ij} J^c_k + (T^a, T^b)_{\mathfrak g} \langle \alpha_i, \alpha_j\rangle_{\mathrm{Muk}} \mathbf c,
$$
where $[X, Y]_{\mathrm{super}} = -(-1)^{|X||Y|} [Y, X]_{\mathrm{super}}$.

This gives a **super-Lie algebra** satisfying the super-Jacobi identity, by the graded-Frobenius trace condition on $(H^*(S), \cup, \langle\cdot,\cdot\rangle_{\mathrm{Muk}})$ combined with the Jacobi of $\mathfrak g$. The degree counting is:

- $|J^a_0| = |T^a| + |\alpha_0| = \bar 0 + \bar 0 = \bar 0$: even.
- $|J^a_i| = |T^a| + |\alpha_i| = \bar 0 + \bar 1 = \bar 1$ for $i \in H^2$: odd.
- $|J^a_{23}| = \bar 0 + \bar 0 = \bar 0$: even.
- $|\mathbf c| = \bar 0$: even.

**Even dimension:** $\dim \mathfrak g + \dim \mathfrak g + 1 = 2 \dim \mathfrak g + 1$.
**Odd dimension:** $22 \dim \mathfrak g$.
**Total super-dimension:** $24 \dim \mathfrak g + 1$ — matches the manuscript's count but now as a super-dimension.

For $\mathfrak g = \mathfrak{gl}_1$: super-dim $= 24 + 1 = 25 = (3|22)$ — three even directions ($H^0, H^4, \mathbf c$) and 22 odd ($H^2$).

**This is the correction.** The manuscript's "25-dim Heisenberg algebra" is actually a **$(3|22)$-dim super-Heisenberg.** The central charge and Mukai-signature bookkeeping persists, but the algebra lives in the super category.

### H2.2 The first non-trivial relation, to the last sign (corrected)

For $\mathfrak g = \mathfrak{sl}_2$, $\alpha_1, \alpha_2 \in H^2$ (both odd), the super-bracket:
$$
[J^e_1, J^f_2]_{\mathrm{super}} = 1 \cdot Q_{12} J^h_{23} + 1 \cdot Q_{12} \mathbf c = Q_{12} (J^h_{23} + \mathbf c).
$$

Super-antisymmetry check: $[J^e_1, J^f_2]_{\mathrm{super}} = -(-1)^{1 \cdot 1} [J^f_2, J^e_1]_{\mathrm{super}} = +[J^f_2, J^e_1]_{\mathrm{super}}$.

Compute $[J^f_2, J^e_1]_{\mathrm{super}} = f^{fe}{}_c \mu^k_{21} J^c_k + (T^f, T^e) \langle \alpha_2, \alpha_1\rangle \mathbf c = -1 \cdot Q_{12} J^h_{23} + 1 \cdot Q_{12} \mathbf c = Q_{12}(-J^h_{23} + \mathbf c)$.

Hmm, this does *not* equal $[J^e_1, J^f_2]_{\mathrm{super}} = Q_{12}(J^h_{23} + \mathbf c)$.

So super-antisymmetry fails here too. **The super-grading doesn't save the bracket as-is.**

Trace the issue: on odd-odd tensor, super-antisymmetry requires $[X,Y] = [Y,X]$ (symmetric). The $\mathfrak g$-structure-constant term $f^{ab}{}_c \mu^k_{ij} J^c_k$ is antisymmetric in $(a,b)$ and symmetric in $(i,j)$, so its symmetry under $(a,i)\leftrightarrow(b,j)$ is **antisymmetric** — which for *even* bracket is what we want, for super on odd-odd is **wrong**. The central term $(T^a, T^b)\langle\alpha_i,\alpha_j\rangle$ is symmetric in $(a,b)$ and symmetric in $(i,j)$, so symmetric overall — for super-odd-odd, **right**.

So the mismatch is intrinsic: the $\mathfrak g$-structure-constant term has the wrong super-symmetry on odd-odd inputs.

**Resolution 1:** Flip the definition on odd-odd inputs by inserting a sign. Define
$$
[J^a_i, J^b_j]_{\mathrm{super}} := f^{ab}{}_c \sum_k \mu^k_{ij} J^c_k \cdot \epsilon(i,j) + (T^a, T^b)\langle\alpha_i, \alpha_j\rangle \mathbf c
$$
with $\epsilon(i,j) = +1$ unless both $i, j$ odd. This is ad hoc.

**Resolution 2:** Accept that **$\mathfrak g_{K3}$ as defined in equation 316 is not a Lie algebra** (neither ordinary nor super), and define the "correct" algebra by a more sophisticated construction (e.g., Costello–Gwilliam's $L_\infty$-algebra from 6d hCS, Schiffmann–Vasserot's CoHA multiplication, or Kapranov–Vasserot's preprojective Yangian). The manuscript's equation 316 is a **naive formal writeup** that fails at the level of verifying Jacobi-on-K3.

**Resolution 3 (the one I believe is correct):** The bracket of equation 316 is the bracket of a **shifted Lie algebra in a chain complex**, where the cohomological degree shift cancels the symmetry anomaly. Concretely, $H^*(S)$ is a CDGA with $d = 0$ (formal), and the tensor $\mathfrak g \otimes H^*(S)$ is a DG Lie algebra of homological type, whose bracket combines the $\mathfrak g$-bracket with the cup product in a sign-tracked way. The "Lie bracket" of equation 316 is really the bracket on $H_0(\mathfrak g \otimes H^*(S))$, which in general differs from a bare Lie bracket by sign corrections.

**In any case:** the manuscript's claim "Jacobi follows from Jacobi of $\mathfrak g$, associativity of cup product, $\mathfrak g$-invariance of Killing form" is insufficient. A **fourth** ingredient — the sign convention for the bracket on mixed-parity inputs — is load-bearing and missing.

---

## 5. ROUND 3 ATTACK

Attack the healed picture: **is the super-Lie algebra story actually workable?**

Yes — but it requires adopting the cohomological $\bZ/2$-grading explicitly. This is the same reason the manuscript's Section 1855 arrives at $\mathfrak{osp}(4|20)$: the super-structure is **forced** by the Mukai form's symmetry properties, not optional.

### The correct formulation is:

$\mathfrak g_{K3}$ is the super-Lie algebra
$$
\mathfrak g_{K3} = \mathfrak g_{\bar 0} \oplus \mathfrak g_{\bar 1}, \qquad \mathfrak g_{\bar 0} = (\mathfrak g \otimes H^{\mathrm{even}}(S)) \oplus \C\mathbf c, \quad \mathfrak g_{\bar 1} = \mathfrak g \otimes H^{\mathrm{odd\, parity}}(S) = \mathfrak g \otimes H^2(S).
$$

with super-bracket defined **by cases**:

- $[\mathfrak g_{\bar 0}, \mathfrak g_{\bar 0}]$: classical Lie bracket, antisymmetric.
- $[\mathfrak g_{\bar 0}, \mathfrak g_{\bar 1}]$: mixed, antisymmetric $[X, Y] = -[Y, X]$ (since $(-1)^{0 \cdot 1} = 1$, so $-(-1)^{|X||Y|} = -1$).
- $[\mathfrak g_{\bar 1}, \mathfrak g_{\bar 1}]$: super-symmetric $[X, Y] = +[Y, X]$.

The formula of equation 316 respects the first two; for the third, we need the $f^{ab}{}_c \mu^k_{ij}$ term to be symmetric under $(a,i)\leftrightarrow(b,j)$, which fails unless we sign-adjust.

**Sign-adjusted bracket:**
$$
[J^a_i, J^b_j] = \begin{cases} f^{ab}{}_c \mu^k_{ij} J^c_k + (T^a, T^b)\langle\alpha_i,\alpha_j\rangle \mathbf c & \text{if not both odd,} \\ -f^{ab}{}_c \mu^k_{ij} J^c_k + (T^a, T^b)\langle\alpha_i,\alpha_j\rangle \mathbf c & \text{if both odd.} \end{cases}
$$

This is equivalent to taking the bracket as in equation 316 but **inserting a Koszul sign**: $[J^a_i, J^b_j] = (-1)^{|T^a||\alpha_j|} \cdot (\text{equation 316})$.

With this sign, super-antisymmetry holds on all three blocks. **Super-Jacobi** then follows from Jacobi of $\mathfrak g$, graded-associativity of cup product (which is strict associativity on even cohomology, vacuous on odd-odd since $H^2 \cdot H^2 \subset H^4$), and graded-Frobenius trace on $\langle\cdot,\cdot\rangle_{\mathrm{Muk}}$.

### The first non-trivial super-relation, with signs

For $\mathfrak g = \mathfrak{sl}_2$, $\alpha_1, \alpha_2 \in H^2$:
$$
[J^e_1, J^f_2] = -Q_{12} J^h_{23} + Q_{12} \mathbf c
$$
(sign-corrected from equation 316 on odd-odd input).

Check super-antisymmetry: $[J^e_1, J^f_2] - (-1)^{1 \cdot 1} \cdot [J^f_2, J^e_1] \overset?= 0$, i.e. $[J^e_1, J^f_2] + [J^f_2, J^e_1] \overset?= 0$.
$[J^f_2, J^e_1] = -Q_{12} J^h_{23} + Q_{12} \mathbf c$ (same sign correction).

Sum: $-2 Q_{12} J^h_{23} + 2 Q_{12} \mathbf c$. **Not zero.**

So this sign convention is still not right.

Let me re-examine. Super-antisymmetry for $X, Y$ both odd:
$$
[X, Y] = -(-1)^{|X||Y|} [Y, X] = -(-1)^1 [Y, X] = [Y, X].
$$

So we need $[J^e_1, J^f_2] = [J^f_2, J^e_1]$ on odd-odd. From the sign-corrected bracket: $[J^e_1, J^f_2] = -Q_{12} J^h_{23} + Q_{12} \mathbf c$ and $[J^f_2, J^e_1]$ uses $f^{fe}{}_c = -f^{ef}{}_c = -1$, so $[J^f_2, J^e_1] = -(-1) Q_{12} J^h_{23} + Q_{12} \mathbf c = +Q_{12} J^h_{23} + Q_{12} \mathbf c$. These differ by $2 Q_{12} J^h_{23}$. Still not equal.

To make $[J^e_1, J^f_2] = [J^f_2, J^e_1]$: the $f^{ab}{}_c$-term must be **symmetric** in $(a, b)$, but the structure constants are antisymmetric $f^{ab}{}_c = -f^{ba}{}_c$. Impossible unless we *also* insert a sign from $\mu^k_{ij}$, which is symmetric.

**Conclusion:** The naive tensor product super-algebra $(\mathfrak g \otimes H^*(S), \text{super-bracket})$ **does not form a super-Lie algebra** for $\mathfrak g$ simple and $H^*(S)$ with the cohomological $\bZ/2$-grading. The $\mathfrak g$-antisymmetry and the $H^2 \otimes H^2 \to H^4$ cup-product symmetry conflict on odd-odd inputs.

### What actually works

The correct construction must either:

(a) **Drop the naive grading** and treat $\mathfrak g_{K3}$ as a plain Lie algebra, but then the bracket fails antisymmetry on central terms (as shown in Attack 2.3).

(b) **Use a more sophisticated grading**, e.g., the $\bZ$-grading by total cohomological degree $0, 2, 4$, and define the bracket as a *shifted* Lie bracket (i.e., the bracket lives in cohomological degree $0$, and inputs carry their own cohomological degree separately from the bracket output). This is the framework of **graded Lie algebras** in the $\bZ$-grading sense, not the super $\bZ/2$-grading. In that framework:
  - The bracket has bidegree $(0, 0)$ acting on bidegree $(|\mathfrak g|, |\alpha|)$ inputs.
  - Antisymmetry is classical: $[X, Y] = -[Y, X]$ regardless of grading.
  - The $f^{ab}{}_c \mu^k_{ij}$ term is antisymmetric in $(a,b)$ and symmetric in $(i,j)$; its total symmetry under swap $(a,i)\leftrightarrow(b,j)$ is antisymmetric, which matches classical Lie-bracket antisymmetry.
  - The central term $(T^a, T^b)\langle\alpha_i, \alpha_j\rangle \mathbf c$ is symmetric in both, hence **symmetric** under swap — which **fails** classical antisymmetry.

So option (b) also fails because of the central term.

(c) **Subtract the symmetric part of the central term.** That is: take the central term to be $\tfrac{1}{2}[(T^a, T^b)\langle\alpha_i, \alpha_j\rangle - (T^b, T^a)\langle\alpha_j, \alpha_i\rangle] \mathbf c = 0$ — vanishes identically. So the central extension is trivial in the naive Lie-algebra framework.

**The upshot:** for a symmetric pairing $\langle\cdot,\cdot\rangle_{\mathrm{Muk}}$ combined with a symmetric Killing form $(\cdot,\cdot)_{\mathfrak g}$, the naive central extension of $\mathfrak g \otimes R$ has **vanishing cocycle** in the Lie-algebra category. There is **no non-trivial central extension** of this form.

This is consistent with the classical fact that the affine Kac–Moody algebra central extension uses the **residue pairing on loop algebras** — which is antisymmetric (residue of $df \cdot g$ is equivalent to $-\mathrm{Res}(f \cdot dg)$ mod exact). The DDCA central extension uses the 2-form residue pairing on $\C[u,v]$ — also antisymmetric (2-form on a surface).

**For $K3$ cohomology, the natural analogue is not the Mukai pairing but the Frobenius-trace derivative pairing** $\langle \alpha, \beta\rangle_{\mathrm{derived}} = \int_S \alpha \cup d\beta - \int_S d\alpha \cup \beta$, which is antisymmetric if $d$ is a derivation. But $H^*(S)$ with $d = 0$ makes this trivially zero.

**So the manuscript's bracket on $\mathfrak g_{K3}$ via the symmetric Mukai pairing is trivially central (zero central term) or non-Lie. Either way, the advertised "central extension" is mathematically suspect.**

This is **the genuine open problem** at the foundational level.

---

## 6. ROUND 3 HEAL — What actually survives

After three rounds of adversarial attack, what remains:

### S1. The abelian Heisenberg Yangian at rank 24 with Mukai-diagonal signs

This is **Proved (classical)**. It is $Y(\mathfrak{gl}_1)^{\otimes 24}$ twisted by the signs $\omega = \mathrm{diag}(+1^4, -1^{20})$. Each copy is a standard Heisenberg Yangian (Drinfeld 1985, Chari–Pressley 1995, Frenkel–Jing 1988). The manuscript's Theorem 877 is correct.

### S2. The $\mathfrak g \otimes H^{\mathrm{even}}(S)$-Lie-algebra structure for $\mathfrak g$ simple

Without the central extension, $\mathfrak g \otimes H^*(S, \C)$ with bracket $[T^a \otimes \alpha, T^b \otimes \beta] = f^{ab}{}_c (\alpha \cup \beta) \otimes T^c$ **is** a bona-fide $\bZ$-graded Lie algebra (commutative cohomology ring tensored with a Lie algebra). The central extension is **the open problem**.

### S3. Sub-Yangian at ADE enhancement: $Y(\widehat{\mathfrak g}_{\mathrm{ADE}})_{k=1}$ is classical

At an $A_n/D_n/E_n$ enhancement of the K3 Picard lattice, the ADE simple-root vectors generate a finite-type $\mathfrak g_{\mathrm{ADE}}$ inside $\mathfrak g \otimes H^2(S)$. The level-1 affine Yangian $Y(\widehat{\mathfrak g}_{\mathrm{ADE}})_{k=1}$ is classical (Drinfeld 1985, Nakajima 2001 for quiver varieties, BFN 2016 for Coulomb branches, all unconditional at level 1). The manuscript's Theorem 108 (`thm:bfn-phi-ade-identification`) correctly attributes this as a composition of four Proved-Elsewhere results.

### S4. The Mukai-signed $R$-matrix on the abelian 24-copy block

Diagonal rational $R$-matrix $R_{ii}(z) = (z - h_i)/(z + h_i)$ with $h_1, \ldots, h_{24}$ satisfying $\sum h_i = 0$. Unitarity $g(z) g(-z) = 1$ holds factor-by-factor. Satisfies YBE trivially (since diagonal on $\C^{24} \otimes \C^{24}$). Structure function is the manuscript's equation 921. This is **abelian**; no non-abelian braiding.

### S5. **Open, not constructed:** the "genuinely non-abelian" K3 Yangian

The manuscript **does not** present a non-abelian K3 Yangian with:
- A complete generator list in the Drinfeld $J$-presentation.
- A complete relation list, including a terminal cubic or an analogue of the $\mathfrak{sl}_2$-style closure.
- A verified Jacobi / super-Jacobi on the classical limit.
- A worked small-rank non-trivial bracket computation.

All non-abelian content in the chapter is **scope declaration**: statements about what sub-Yangians *would look like* at enhancement points, citing classical Drinfeld + Nakajima + BFN theory for the $\mathfrak g_{\mathrm{ADE}}$-part, plus untested conjectures about the full Mukai-envelope.

### S6. The super-Yangian $Y_{\osp(4|20)}$: imported presentation, unexecuted specialization

Definition 1919 ('`def:osp-super-yangian-K3`') correctly records that Arnaudon–Crampé–Doikou–Frappat–Ragoucy 2003 give a rank-$(m|n)$ super-Yangian with the reflection-equation RTT presentation, and that specializing $(m,n) = (4,20)$ produces a formal object $Y_{\osp(4|20)}$. Conjecture 2020 asserts this is the "non-abelian K3 Yangian". **Neither the specialization nor the identification is verified in the manuscript or in the compute layer.** The compute test `k3_super_yangian.py` (cited at line 2015) tests only $\mathfrak{gl}(1|1)$ and $\mathfrak{gl}(2|1)$ — the $\mathfrak{gl}$, not $\mathfrak{osp}$, case, as the manuscript admits at line 2017.

---

## 7. FINAL SUMMARY

### (i) Boolean assessment

**Does the manuscript currently contain a defensible construction of a non-abelian K3 Yangian?**

**NO.**

- The abelian K3 Yangian at $\mathfrak g = \mathfrak{gl}_1$ (Theorem 877) is defensible and corresponds to rank-24 Heisenberg Yangian with Mukai signs; this is a light decoration of classical Drinfeld / Chari–Pressley / Frenkel–Jing content.
- The non-abelian K3 Yangian is uniformly presented as conjectural, with the specific imaginary-root sectors admitted to have no known Drinfeld presentation (line 1294).
- The orthosymplectic envelope $Y_{\osp(4|20)}$ is conjectural (Conjecture 2020), is backed only by the classical ACDFR presentation applied formally at the rank $(4,20)$ case, and has no small-rank worked example in the compute layer.
- The classical limit $\mathfrak g_{K3}$ (Definition 276) **has a load-bearing sign issue** in its central term: for $\mathfrak g$ simple non-abelian and the symmetric Mukai pairing, the bracket of equation 316 fails antisymmetry (Attack 2.3). Adopting a super-grading does not save it (Round 3 Attack). Either the central extension is trivial in the naive Lie-algebra category, or the bracket lives in a derived / DG / $L_\infty$ framework that the manuscript does not articulate.

**The advertised "non-abelian" crown jewel (24 generators, Mukai-signature Serre relations, degree-$(24,24)$ structure function) resolves into:**
- 24 **abelian** Heisenberg generators.
- Serre relations only at **classical ADE enhancement** sub-blocks (standard Drinfeld / quiver Yangian content).
- Structure function $\prod (u - h_i)/(u + h_i)$ that **factorises over the 24 abelian directions** (i.e. is diagonal, not non-abelian).

### (ii) Concrete first example

**The first non-trivial bracket, in the $\mathfrak{sl}_2$-flavoured K3 double current algebra, computed to the last sign:**

Take $\mathfrak g = \mathfrak{sl}_2$ with basis $(e, f, h)$, $[e,f]=h$, $[h,e]=2e$, $[h,f]=-2f$, and trace form $(e,f)=1$, $(h,h)=2$. Take two $(-2)$-classes $\alpha_1, \alpha_2 \in H^2(K3, \bZ)$ with intersection $Q_{12} = Q(\alpha_1, \alpha_2)$. The bracket of equation 316 gives:
$$
[J^e \otimes \alpha_1, J^f \otimes \alpha_2] = Q_{12} \cdot (J^h \otimes [\mathrm{pt}]) + Q_{12} \cdot \mathbf c = Q_{12}(J^h_{23} + \mathbf c).
$$

**Antisymmetry test:** $[J^f \otimes \alpha_2, J^e \otimes \alpha_1] = -Q_{12}(J^h_{23}) + Q_{12} \mathbf c$ (using $f^{fe}{}_h = -1$; pairing is symmetric).

Sum: $[J^e \otimes \alpha_1, J^f \otimes \alpha_2] + [J^f \otimes \alpha_2, J^e \otimes \alpha_1] = 2 Q_{12} \mathbf c \neq 0$.

**Antisymmetry fails by $+2 Q_{12} \mathbf c$.** This is the precise anomaly identified in Attack 2.3, and it is **present on-disk in the manuscript's equation 316** for any non-abelian $\mathfrak g$.

**Jacobi test on $(J^e_1, J^f_2, J^h_0)$:** Produces a non-zero obstruction $-2 Q_{12} \mathbf c$ (Attack 2.3 computation).

**This is the first non-trivial check, and it fails.** The manuscript's Definition 276 and Proposition 505 need either a precise sign convention (via super-grading or derived / DG / $L_\infty$-ification), or the central term needs to be antisymmetrised (which makes it zero identically, at which point the "central extension" has no content), or the pairing $\langle\cdot,\cdot\rangle_{\mathrm{Muk}}$ needs to be replaced by an antisymmetric surrogate (which does not canonically exist on $H^{\mathrm{even}}(K3)$).

### (iii) Strongest and weakest passages — file:line citations

**Strongest passages (defensible, verifiable, or correctly attributed):**

- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_yangian_chapter.tex:108-176` — Theorem `thm:bfn-phi-ade-identification` on the ADE-resolved-surface BFN identification with level-1 affine Yangian. Correctly Proved-Elsewhere via composition of Kronheimer, McKay, BFN, Nakajima–Takayama.
- `k3_yangian_chapter.tex:877-1097` — Theorem `thm:k3-abelian-yangian-presentation`. Abelian case is correctly a rank-24 Heisenberg Yangian, consistent with classical literature; classical attribution remark (1067–1086) is honest.
- `k3_yangian_chapter.tex:713-857` — Proposition `prop:mukai-indefinite-yangian`. Correct observation that Drinfeld/Chari-Pressley construction handles indefinite signature at the abelian (diagonal) level.
- `/Users/raeez/calabi-yau-quantum-groups/compute/lib/k3_yangian_adversarial.py:1-802` — Adversarial analysis module. Six attack vectors are clearly articulated, correctly concludes that 2 of 6 are genuine obstructions for the non-abelian case, 4 of 6 are resolved at the abelian level. The verdicts are honest and well-scoped.
- `k3_yangian_chapter.tex:1441-1569` — Remark `rem:k3-yangian-obstruction-tests`. Six structural tests. Clear scoping, correctly identifies two genuine issues for non-abelian.

**Weakest passages (where the manuscript overclaims, conflates, or contains a load-bearing gap):**

- `k3_yangian_chapter.tex:4-12` — Chapter opening abstract. Advertises "24 Heisenberg generators, Mukai-signature Serre relations, and degree-$(24,24)$ structure function" as if the Serre relations were non-trivial. They are not: in the abelian regime, the Serre relations are vacuous (the manuscript itself says so at line 1324). This is a marketing overclaim.
- `k3_yangian_chapter.tex:276-338` — Definition `def:k3-double-current-algebra` and the Jacobi-identity remark at line 336. **Load-bearing gap:** for $\mathfrak g$ simple non-abelian, the central-extension bracket of equation 316 fails antisymmetry (Attack 2.3). The manuscript's two-sentence Jacobi argument omits the fourth required ingredient (graded Frobenius trace condition), and even with it added, the central term's symmetry conflicts with the antisymmetry required by Lie-algebra structure.
- `k3_yangian_chapter.tex:1267-1318` — Conjecture `conj:bkm-yangian-generators`. Enumerates BKM root sectors as "Yangian generators" but the imaginary-root sectors have no Drinfeld presentation (line 1294 admits this).
- `k3_yangian_chapter.tex:1855-2217` — The entire super-Yangian subsection. Definition 1919 specializes ACDFR to rank $(4, 20)$ formally but without executing the Serre / RTT computation at that rank. The associated compute module (`k3_super_yangian.py` at line 2015) tests $\mathfrak{gl}(1|1)$ and $\mathfrak{gl}(2|1)$ only, not $\mathfrak{osp}(4|20)$.
- `k3_yangian_chapter.tex:2023-2039` — Conjecture `conj:k3-super-yangian`. The identification "non-abelian K3 Yangian = $Y_{\osp(4|20)}$" is conjectural and not verified at any rank.
- `/Users/raeez/calabi-yau-quantum-groups/compute/tests/test_k3_nonabelian_all_ade.py:1-1196` — This file tests classical structural identities (Cartan matrices, Dynkin diagrams, Yang R-matrices, ADE off-diagonal counts) that are **classical Lie-theory facts**. It does not test any claim specific to the non-abelian K3 Yangian construction. The off-diagonal counts from the formula $d(d-1)(26-d) + \binom{d}{2}(\binom{d}{2}-1)$ (line 117) are combinatorial, not algebraic verifications of closure.

**Surgical fix list (what the manuscript needs to be on a Gelfand-defensible footing):**

1. Edit Definition 276 and the Jacobi remark on line 336 to either (a) explicitly adopt the super-grading convention with a precise bracket, proving super-Jacobi on a 2-by-2 case study with $\mathfrak g = \mathfrak{sl}_2$ and $\alpha_1, \alpha_2 \in H^2$; or (b) downgrade the Lie-algebra claim to "pre-Lie / derived Lie bracket on $H^*(\mathfrak g \otimes H^*(S))$" and discuss the failure of strict antisymmetry.
2. Add a concrete small-$\mathfrak g$ / small-lattice example worked through: e.g. $\mathfrak g = \mathfrak{sl}_2$ coupled to the $A_1$-type singular K3 with a single $(-2)$-class, computing the first non-trivial bracket and explicitly verifying Jacobi.
3. Either verify the $Y_{\osp(4|20)}$ specialization in compute (extending `k3_super_yangian.py` to the actual $\mathfrak{osp}$ case at $(m,n) = (4,20)$), or scope the claim as a conjecture awaiting this computation. Currently the manuscript asserts-without-verifying.
4. Rewrite the abstract (lines 4–12) to drop the misleading "Mukai-signature Serre relations" phrasing at the abelian level, or clarify that Serre relations appear only at ADE-enhancement specializations.

---

## 8. What I did not attack, and what Gelfand would ask next

Unattacked in this pass, but on the agenda if iteration continues:

- **The Bridgeland-stability connection** (Sections 2220–2370): are the conjectural identifications of $\Stab^\dagger(K3)$-points with Yangian modules coherent with the representation theory? Dimension-reconciliation conjecture (2322) suggests the na\"ive count fails; the manuscript's resolution is a fibration picture. Needs deeper audit.
- **The factorization-homology $\int_{K3} \mathcal F$ computation** (Sections 2400–2800): one-loop correction at cubic interactions, $\phi_{10,1}/\eta^{24}$ expansion. Gelfand's question: "Show me the Feynman integral, to the last sign, at the one-loop level."
- **The Pentagon-at-$E_1$ machinery and the $K_n$-tower** (lines 3100–6903): this is genuinely new manuscript content, not reducible to classical Drinfeld–Chari–Pressley. It would need its own adversarial audit. Total page count suggests roughly 4000 lines of novel matter here.
- **The multi-projection trace identity** (Theorems 3362, 3810, 4121): cross-$d$ identifications claiming that a universal $R$-matrix trace has the same value at $K3, K3 \times E, K3 \times K3$, etc. These claim chain-level rigor; I did not verify the Künneth dichotomy claim at Theorem 3571.

---

## Appendix — table of defensibility

| Claim | Manuscript status | Gelfand verdict |
|---|---|---|
| $\mathfrak g_{K3}$ is a Lie algebra (eq. 316) | ProvedHere | **Broken:** fails antisymmetry on central term for non-abelian $\mathfrak g$. |
| $\mathfrak g_{K3}$ is a super-Lie algebra | Implicit | **Broken:** also fails super-antisymmetry on odd-odd. Real obstruction. |
| $\dim \mathfrak g_{K3} = 24 \dim \mathfrak g + 1$ | ProvedHere | Correct as vector-space dimension; algebraic structure suspect. |
| $Y(\mathfrak g_{K3})$ at $\mathfrak g = \mathfrak{gl}_1$ is rank-24 Heisenberg Yangian | ProvedHere | ✓ defensible, classical. |
| $Y(\mathfrak g_{K3})$ at $\mathfrak g$ simple is a non-abelian quantum group | Conjectured | No presentation exists; genuinely open. |
| Mukai-signature Serre relations | Implied by abstract | Abelian: vacuous. Non-abelian at ADE: classical. Mukai-envelope: open. |
| $Y_{\osp(4|20)}$ is the non-abelian K3 Yangian | Conjectured | Conjecture; compute does not verify the $(4,20)$ case. |
| Degree-$(24, 24)$ structure function | ProvedHere (abelian) | ✓ for the diagonal case. |
| YBE for the Mukai-signed $R$-matrix | ProvedHere (abelian) | ✓ trivially (diagonal). |
| Koszul conductor $K = 0$ on free-field branch | ProvedHere | ✓ for the abelian case. |
| $E_8 \times E_8$ enhancement contains $Y(\widehat{\mathfrak e}_8)_{k=1} \otimes Y(\widehat{\mathfrak e}_8)_{k=1}$ | Conjectured | Plausible; requires the non-abelian K3 Yangian to exist first. |
| Six-path verification with 125 tests (`symplectic_duality_k3.py`) | ProvedHere | ✓ the *character-level* identity $Z_C = Z_H$ is genuine (from K3 self-mirror). |
| ZTE obstruction persists for super-Yangian | ProvedHere | ✓ correctly pointed out; not a defect of the programme, a limitation. |
| Mukai-indefinite signature is no obstruction to the abelian Yangian | ProvedHere | ✓ correct (diagonal R-matrix). |

**Defensible count: 6/14. Broken/open count: 8/14.** The manuscript is **honest** about most of the open / conjectural status; the one place where it makes an unqualified ProvedHere claim that does not survive scrutiny is Definition 276's Lie-algebra assertion.

---

*Gelfand voice concludes: "Young man, before you publish 7078 lines about a K3 Yangian, show me the Lie bracket. If the bracket is not a bracket, the Yangian is not a Yangian. Write down the $3 \times 3$ super-Jacobi table for $\mathfrak{sl}_2$ coupled to the $A_1$ lattice. Compute. Then we talk."*

— end agent 01 report
