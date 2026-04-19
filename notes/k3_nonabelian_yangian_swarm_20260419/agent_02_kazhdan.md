# Agent 02 — Kazhdan-voice audit of the K3 Yangian construction

**Target**: `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_yangian_chapter.tex`
**Frame**: Kac-school rigour. Every Serre relation exact; every structure constant verified; every sign accounted for.
**Attack protocol**: iterated attack/heal over the Lie-algebraic foundation, the Yangian presentation, the Cartan data, and the Serre ideal.

The audit below is written in the voice of David Kazhdan: terse, arithmetic, unforgiving of signs, and deeply suspicious of anything that moves from a stated form to an invoked universal property without a pointwise verification.

---

## Executive summary (a warning to the reader)

The chapter presents two distinct objects under the single label "K3 Yangian":

1. **An abelian object**, $Y(\mathfrak g_{K3})$ with $\mathfrak g_{K3} = \mathfrak{gl}_1$ specialisation. This is essentially the rank-$24$ Heisenberg Yangian of Drinfeld–Chari–Pressley endowed with Mukai-lattice parameters $h_1,\ldots,h_{24}$ constrained by $\sum h_i = 0$. **It is classical.** The chapter's presentation (Theorem at line 877–1001) is correct as stated, modulo cosmetic issues noted below.

2. **A non-abelian envelope** $Y_{\mathfrak{osp}(4|20)}$ (Definition at line 1919–2000). This is claimed as the "orthosymplectic super-Yangian attached to the Mukai orthogonal form". **It is not classical.** The existence of this super-Yangian at generic rank follows from Arnaudon–Crampé–Doikou–Frappat–Ragoucy (2003), but the definition as written contains (i) a sign/convention slip in $\kappa_{\mathfrak{osp}}$ that propagates to the crossing shift, (ii) a Cartan-data gap (the rank and simple roots are never stated), (iii) a Serre-relation gap (super-Serre relations for orthosymplectic series are structurally distinct from the simply-laced form stated at line 1355–1357), and (iv) a conflation of "orthogonal indefinite form of signature $(4,20)$" with "orthosymplectic super-form of rank $(4|20)$" — these are **different mathematical objects**.

The chapter explicitly flags (2) as conjectural (`\ClaimStatusConjectured` at line 2022). This is correct status. The mathematical statement to be rescued is: after replacing the headline "K3 Yangian" with the precise object that the construction actually delivers, the claim reduces to a statement about the Heisenberg Yangian on an indefinite lattice, plus a conjectural super-extension whose Cartan data is not exhibited.

---

## Round 1 — ATTACK

### A1.1. Is $\mathfrak g_{K3}$ defined precisely?

Reading Definition 2.1 at line 276–329:

> $\mathfrak g_{K3} := (\mathfrak g \otimes H^\ast(S,\mathbb C)) \oplus \mathbb C\cdot\mathbf c$

with bracket (line 316–324)
$$[J^a_i, J^b_j] = f^{ab}{}_c \sum_k \mu^k_{ij} J^c_k + (T^a,T^b)_{\mathfrak g}\,\langle\alpha_i,\alpha_j\rangle_{\rm Muk}\,\mathbf c.$$

This is the $R$-current algebra with $R = H^\ast(S,\mathbb C)$. The invariant bilinear form is the Mukai pairing. **The construction is precise.** The Lie algebra is $24\dim\mathfrak g + 1$-dimensional when $\mathfrak g$ is finite-dimensional simple, and the Jacobi identity reduces correctly to Jacobi on $\mathfrak g$ plus associativity of cup product plus invariance of the Killing form.

**Verdict 1.1**: the *classical* object $\mathfrak g_{K3}$ is well-defined. The grading is $\mathbb Z$-grading via $H^0, H^2, H^4$ (degrees $0, 2, 4$); the bilinear form is the Mukai pairing of signature $(4,20)$ on $\widetilde H(S,\mathbb Z)$. *No sign issue yet.*

### A1.2. The $\mathfrak{gl}_1$ specialisation

Line 458–473 ($\mathfrak g = \mathfrak{gl}_1$): brackets $[J_i,J_j] = \omega^{ij}\mathbf c$, two-step nilpotent, dimension $25$. **Correct.**

Block form of the Mukai pairing (line 486–497): $H^0$–$H^4$ block $= U$ (hyperbolic, signature $(1,1)$); the $22\times 22$ block $Q_{22}$ is the intersection form on $H^2$, signature $(3,19)$. Sum: $(1+3, 1+19) = (4,20)$. **Arithmetic correct.**

### A1.3. The abelian K3 Yangian — is it truly a Yangian?

The presentation at line 877–1001 writes the "Yangian" with:

- 24 Heisenberg currents $J_i(z)$,
- transfer matrix $T_{K3}(u) = \prod_i (u - \phi_i)$,
- "structure function" $g_{K3}(u) = \prod_i (u-h_i)/(u+h_i)$,
- RTT relation (trivial because diagonal).

But: the *Drinfeld Yangian* $Y_\hbar(\mathfrak g)$ of a Lie algebra $\mathfrak g$ is defined with Chevalley or current generators, Cartan, Serre. For $\mathfrak g = \mathfrak{gl}_1$ (abelian), the Drinfeld Yangian *degenerates*: the Serre ideal is vacuous, and the Yangian is (up to completion) the symmetric algebra on countably many generators $J_{i,n}$ with rational-$R$-matrix central extension. **What the chapter calls $Y(\mathfrak g_{K3})$ at $\mathfrak g = \mathfrak{gl}_1$ is the rank-$24$ Heisenberg Yangian**: a tensor product of $24$ rank-$1$ Heisenberg Yangians with independent spectral parameters, constrained only by $\sum h_i = 0$.

The attribution on line 832 is correct: *"Drinfeld's original definition of $Y_\hbar(\mathfrak g)$ depends only on the Killing form up to non-degeneracy, not on its signature."* So the name "Yangian" is acceptable; no Cartan matrix is needed because no non-abelian simple Lie algebra is present.

**Verdict 1.3**: no structural issue with the abelian case. The only genuine novelty is the *parameters* — 24 shifts $h_i$ with $\sum h_i = 0$ on a rank-$24$ Heisenberg — which is classical Chari–Pressley with Mukai-constrained moduli.

### A1.4. The non-abelian envelope — ATTACK

The super-Yangian $Y_{\osp(4|20)}$ at line 1855–2223 is where Kac-school rigour bites.

**Attack 1.4.a. Signature vs super-grading — categorical confusion.**

The manuscript correctly notes at line 1858–1868 that the Mukai form is *symmetric indefinite of signature $(4,20)$*, not a $\mathbb Z/2$-super-grading, and therefore states (line 1861–1864) that the automorphism group is $\mathrm{O}(4,20)$, not $\mathrm{GL}(4|20)$. Good. But then the "resolution" offered is $\mathfrak{osp}(4|20)$ — the orthosymplectic super-Lie algebra of rank-$(4|20)$. This is not the same object as $\mathfrak{so}(4,20)$ (which *is* the stabiliser of the Mukai form in the ordinary, non-super sense).

The chapter acknowledges this distinction at line 2055–2071 (Remark `rem:so-4-20-alternative`), noting:

> "The $\mathfrak{so}(4,20)$ and $\mathfrak{osp}(4|20)$ Yangians are distinct algebras: the former is a real form of $Y(\mathfrak{so}_{24})$, the latter is a super-Yangian with a Berezinian centre. They agree at the level of the split Cartan, which carries the $(4,20)$-signature data, but differ in their coproduct and reflection structure."

**This remark is the load-bearing caveat and it is correct.** But it is *hidden* after 130 lines of elaboration treating the orthosymplectic object as the canonical choice. The physical argument for picking $\mathfrak{osp}(4|20)$ over $\mathfrak{so}(4,20)$ at line 2067–2070 is *conjectural* ("the BRST-invariant boundary sector is super-graded") with a Frontier ticket F26. **The headline choice is not forced by the Mukai lattice; it is forced by a conjecture.**

**Attack 1.4.b. Dimension arithmetic of $\mathfrak{osp}(4|20)$.**

Line 1899–1900 claims:
> "Its even part is $\mathfrak{osp}(4|20)_{\bar 0} = \mathfrak{so}(4) \oplus \mathfrak{sp}(20)$, of dimension $\binom{4}{2} + \binom{21}{2} = 6 + 210 = 216$."

Verify:
- $\dim\mathfrak{so}(4) = \binom{4}{2} = 6$. Correct.
- $\dim\mathfrak{sp}(20)$: here convention matters. In Kac's convention (Kac, *Lie Superalgebras*, 1977, §2.1.3, Theorem 5), $\mathfrak{osp}(m|2n)$ has even part $\mathfrak{so}(m) \oplus \mathfrak{sp}(2n)$. So "$\mathfrak{sp}(20)$" in the manuscript must mean $\mathfrak{sp}(2n)$ with $2n = 20$, i.e. **$n = 10$**. Then $\dim\mathfrak{sp}(20) = n(2n+1) = 10 \cdot 21 = 210$. Correct, and this is what the formula $\binom{21}{2} = 210$ computes.
- Odd part: $\mathfrak{osp}(m|2n)_{\bar 1} = \mathbb C^m \otimes \mathbb C^{2n}$ of dimension $m \cdot 2n = 4 \cdot 20 = 80$. Correct.
- Total: $216 + 80 = 296$. Correct.

**Verdict 1.4.b**: the dimension count is arithmetically correct, but the *labelling* is conventionally dangerous. Writing "$\mathfrak{osp}(4|20)$" when you mean $\mathfrak{osp}(4|2n)$ with $2n = 20$ (i.e., $n = 10$) is standard in the physics literature (ACDF-R use it), but some mathematics references write $\mathfrak{osp}(m|2n)$ with $2n$ in the odd slot. **Pattern 269 discipline** (scope declaration): at every first use, declare the convention. The manuscript does not; a reader seeing "$\mathfrak{osp}(4|20)$" and applying the convention $\mathfrak{osp}(m|n)$ with $n$ odd-dimensional (not $2n$) would compute $\dim\mathfrak{sp}_n$ with $n = 20$ odd — which is not a simple Lie algebra and has no standard dimension, revealing an immediate type error.

**Attack 1.4.c. Rank and Cartan subalgebra of $\mathfrak{osp}(4|20)$ — THE GAP.**

Here Kac-school rigour breaks the manuscript.

Kac's classification (*Adv. Math.* 26, 1977) of finite-dimensional simple Lie superalgebras distinguishes **Type I** from **Type II**:
- Type I: $\mathfrak{sl}(m|n), \mathfrak{psl}(n|n), \mathfrak{osp}(2|2n)$ — admit a consistent $\mathbb Z$-grading.
- Type II: $\mathfrak{osp}(m|2n)$ for $m \geq 3$, $D(2,1;\alpha)$, $F(4), G(3)$ — only $\mathbb Z/2$-graded.

For $m = 2r$ even, $\mathfrak{osp}(2r|2n)$ is of type $D(r|n)$. For $(m,n) = (4, 20)$ with $m = 4 = 2\cdot 2$ and $2n = 20$, so $n = 10$: **$\mathfrak{osp}(4|20) = D(2|10)$.**

The **rank** of $D(r|n)$ is $r + n$. Hence:

$$\boxed{\operatorname{rank}\mathfrak{osp}(4|20) = 2 + 10 = 12.}$$

The **Cartan subalgebra** has dimension $12$, split as: $2$ from the $\mathfrak{so}(4)$ Cartan (since $\mathfrak{so}(4)$ has rank $2$, being $\mathfrak{sl}_2 \oplus \mathfrak{sl}_2$ at the level of the semisimple part), plus $10$ from the $\mathfrak{sp}(20)$ Cartan (which has rank $10$). **Nowhere in the manuscript is the rank stated, nor the Cartan identified.**

The **simple roots** of $D(r|n)$ in Kac's distinguished choice (Kac 1977, Table VI for basic classical Lie superalgebras, supplemented by Frappat–Sciarrino–Sorba *Dictionary on Lie Algebras and Superalgebras*, 2000, §2.41):

- $r + n - 1 = 11$ even simple roots: $\alpha_i = \varepsilon_i - \varepsilon_{i+1}$, $i = 1, \ldots, n - 1 = 9$, plus $\alpha_n = \varepsilon_n - \delta_1$ (mixed, usually the *odd* simple root in the distinguished choice) ... — wait, let me redo this carefully.

In Kac's distinguished simple-root system for $D(r|n) = \mathfrak{osp}(2r|2n)$: take basis $\delta_1,\ldots,\delta_n$ (from $\mathfrak{sp}$ side), $\varepsilon_1,\ldots,\varepsilon_r$ (from $\mathfrak{so}$ side). A distinguished simple-root system is
$$\alpha_1 = \delta_1 - \delta_2,\ \ldots,\ \alpha_{n-1} = \delta_{n-1} - \delta_n,\ \alpha_n = \delta_n - \varepsilon_1,\ \alpha_{n+1} = \varepsilon_1 - \varepsilon_2,\ \ldots,\ \alpha_{n+r-1} = \varepsilon_{r-1} - \varepsilon_r,\ \alpha_{n+r} = \varepsilon_{r-1} + \varepsilon_r.$$

Count: $n-1$ (from $\delta$ side) $+ 1$ (bridge) $+ r - 1$ (from $\varepsilon$ side) $+ 1$ (fork, $D_r$-type tail) $= n + r = 12$ simple roots. **Exactly one** is odd (the bridge $\alpha_n = \delta_n - \varepsilon_1$, with $(\alpha_n, \alpha_n) = 0$). The rest are even.

For $(r,n) = (2, 10)$, $n + r = 12$ simple roots; Dynkin diagram is the "$D$-tail attached to an $A$-chain" shape:

```
       o---o---...---o---x---o---o        (x = odd simple root)
      \alpha_{12}   \alpha_{11}  \alpha_n   \alpha_{n-1} ... \alpha_1
                    |
                    \alpha_{n+r}            (fork of the D_r-type tail; here r=2 so fork at alpha_{12})
```

Wait — for $r = 2$, the $D_r$-type tail is $D_2 = A_1 \times A_1$ (not simple). So the right end is a fork with two simple roots $\varepsilon_1 - \varepsilon_2$ and $\varepsilon_1 + \varepsilon_2$, both even, giving rank $2$ from the $\mathfrak{so}(4)$ side; correct.

**So the claimed "24 generators" = rank of $\widetilde\Lambda_{\rm Muk}$ is NOT the rank of the Lie superalgebra.** $\widetilde\Lambda_{\rm Muk}$ has rank $24$; $\mathfrak{osp}(4|20)$ has rank $12$.

The manuscript's phrase on line 6 — "whose 24 Heisenberg generators" — is *only* correct for the *abelian* $\mathfrak{gl}_1$-specialised K3 Yangian, where the 24 generators are the Heisenberg currents $J_i$, one per direction in $H^\ast(S,\mathbb C)$. It is **incorrect** to describe the non-abelian envelope $Y_{\mathfrak{osp}(4|20)}$ as having "24 generators" in any standard Yangian sense:

- In Drinfeld's first presentation (Chevalley): $Y_\hbar(\mathfrak{osp}(4|20))$ has $3 \cdot \operatorname{rank} = 36$ Chevalley-type generators $(e_i, f_i, h_i)$ — modulo that one $e_i, f_i$ is odd and the others even. Plus the "level-$1$" generators $J(x)$ shifting by $\hbar$. Plus a completed filtration.

- In Drinfeld's second (current) presentation: generators $\kappa_{i,r}$, $x_{i,r}^\pm$ for $i = 1, \ldots, 12$ (one for each simple root), $r \geq 0$. That is $3 \cdot 12 \cdot \aleph_0$ generators in the current picture.

- In the RTT (Faddeev–Reshetikhin–Takhtajan) presentation: generators $t^{(r)}_{ij}$ with $i,j \in \{1,\ldots,24\}$ (the defining $(4|20)$-dimensional representation) and $r \geq 1$. That's $24^2 \cdot \aleph_0 = 576\aleph_0$ generators, *before* imposing the orthosymplectic reflection relation. After the reflection relation and supertranspose constraint, the count reduces as noted at line 2128–2137 (296 independent generators per level). **This is consistent.**

**The integer 24 is the dimension of the defining representation, NOT the count of Chevalley or current-generator families.** The chapter's headline sentence conflates these.

**Verdict 1.4.c**: The Cartan data of $Y_{\mathfrak{osp}(4|20)}$ is never exhibited in the chapter. The chapter's single most-repeated numerical claim — "24 Yangian generators" — is a count of RTT *indices* (matching the defining representation dimension $\dim V = 4 + 20 = 24$), not a count of Chevalley or Drinfeld current generators. This is a Pattern 240 part/whole confusion (lattice rank vs Cartan rank vs defining-rep dim).

---

## Round 1 — HEAL

The correct statements are:

### H1.1. $\mathfrak g_{K3}$ (classical)
The classical K3 double current algebra at simple $\mathfrak g$ is
$$\mathfrak g_{K3} = (\mathfrak g \otimes H^\ast(S,\mathbb C)) \oplus \mathbb C\mathbf c, \qquad \dim = 24\dim\mathfrak g + 1.$$
At $\mathfrak g = \mathfrak{gl}_1$: the K3 Heisenberg algebra, $\dim = 25$, two-step nilpotent, with defining form the Mukai pairing on $H^\ast(S,\mathbb C)$ of signature $(4,20)$.

### H1.2. Abelian K3 Yangian
$Y(\mathfrak g_{K3})|_{\mathfrak g = \mathfrak{gl}_1}$ is the rank-$24$ Heisenberg Yangian of Drinfeld–Chari–Pressley with parameters $h_1,\ldots,h_{24} \in \mathbb C$ constrained by $\sum h_i = 0$ and living on a lattice of signature $(4,20)$. The structure function $g_{K3}(u) = \prod_{i=1}^{24}(u-h_i)/(u+h_i)$ is a degree-$(24,24)$ rational function. The RTT relation is trivialised by diagonality.

This object is classical. **The "K3" label marks the physical source but does not add mathematical content beyond the Mukai lattice** (cf. Remark at line 859–874: *"A reader seeking a K3-geometric theorem — one that invokes Kähler structure, a Ricci-flat metric, the holomorphic symplectic form, Bridgeland stability, or Hilbert schemes — should note that the present theorem does not use these."*).

### H1.3. The orthosymplectic super-Yangian $Y_\hbar(\mathfrak{osp}(4|20))$

Precise Lie-algebraic foundation:

- **Super-vector space**: $V = V_{\bar 0} \oplus V_{\bar 1} = \mathbb C^4 \oplus \mathbb C^{20}$ (even + odd).
- **Orthosymplectic form**: $\langle\cdot,\cdot\rangle$ on $V$, symmetric on $V_{\bar 0}$ (orthogonal form of signature $(4)$ — in the split form, signature $(2,2)$ over $\mathbb R$; over $\mathbb C$ non-degenerate of rank $4$), skew-symmetric on $V_{\bar 1}$ (symplectic, rank $20$), and zero between $V_{\bar 0}$ and $V_{\bar 1}$.
- **Lie superalgebra** $\mathfrak{osp}(4|20)$: endomorphisms $X$ of $V$ such that
$$\langle Xu, v\rangle + (-1)^{|X||u|}\langle u, Xv\rangle = 0.$$
- **Even part**: $\mathfrak{osp}(4|20)_{\bar 0} = \mathfrak{so}(4) \oplus \mathfrak{sp}(20)$, dimension $6 + 210 = 216$.
- **Odd part**: $\mathfrak{osp}(4|20)_{\bar 1} = \mathrm{Hom}(V_{\bar 1}, V_{\bar 0}) \oplus \mathrm{Hom}(V_{\bar 0}, V_{\bar 1}) \cong V_{\bar 0} \otimes V_{\bar 1}$ as $\mathfrak{osp}(4|20)_{\bar 0}$-module, dimension $4 \cdot 20 = 80$.
- **Total super-dimension**: $216|80$; ordinary dimension $296$; super-trace of identity $= \dim V_{\bar 0} - \dim V_{\bar 1} = 4 - 20 = -16$.
- **Type**: II, series $D(2|10)$ in Kac's classification.
- **Rank** (Cartan subalgebra dimension): $r + n = 2 + 10 = 12$.
- **Cartan subalgebra**: $\mathfrak h = \mathfrak h_{\mathfrak{so}(4)} \oplus \mathfrak h_{\mathfrak{sp}(20)}$ spanned by $H_{\varepsilon_1}, H_{\varepsilon_2}$ (from $\mathfrak{so}(4)$) and $H_{\delta_1}, \ldots, H_{\delta_{10}}$ (from $\mathfrak{sp}(20)$).

**Invariant bilinear form $B$ on $\mathfrak{osp}(4|20)$**: the supertrace on the defining representation,
$$B(X,Y) = \mathrm{str}(XY), \qquad X, Y \in \mathfrak{osp}(4|20).$$
This form is **non-degenerate, super-symmetric, $\mathfrak{osp}(4|20)$-invariant** — which is exactly the data needed for a Drinfeld–Yangian construction. (For Type I superalgebras like $\mathfrak{sl}(m|n)$ with $m \neq n$, the Killing form is non-degenerate; for $\mathfrak{osp}(m|2n)$ at general $(m,n)$ the supertrace on the defining rep is non-degenerate when $m - 2n - 2 \neq 0$, i.e., the dual-Coxeter-number-like invariant $\kappa_{\mathfrak{osp}} = m - 2n - 2$ must be non-zero. At $(4, 20)$: $\kappa_{\mathfrak{osp}} = 4 - 20 - 2 = -18 \neq 0$. **Good — the form is non-degenerate.**)

**Existence of the super-Yangian**: this is **standard** — Arnaudon–Crampé–Doikou–Frappat–Ragoucy (*Commun. Math. Phys.* 241, 2003) construct $Y_\hbar(\mathfrak{osp}(m|2n))$ for all $(m, 2n)$ with $m - 2n - 2 \neq 0$ via the super-RTT relation. No obstruction from the Type II nature. The chapter's line 1913–1916 correctly notes that existence is *structural* but rank-$(4,20)$ explicit construction is not carried out. **This is a writing-up gap, not a mathematical obstruction**: ACDF-R's general construction applies.

### H1.4. The Cartan matrix

For $D(r|n) = \mathfrak{osp}(2r|2n)$ in Kac's distinguished simple-root system, with simple roots ordered as
$$\alpha_1,\ldots,\alpha_{n-1}\text{ (sp-side)}, \quad \alpha_n\text{ (odd bridge)}, \quad \alpha_{n+1},\ldots,\alpha_{n+r-2}\text{ (so chain)}, \quad \alpha_{n+r-1}, \alpha_{n+r}\text{ (so fork)},$$
the Cartan matrix $A = (a_{ij})_{i,j=1}^{n+r}$ has entries $a_{ij} = 2(\alpha_i, \alpha_j)/(\alpha_i, \alpha_i)$ where $(\alpha_i, \alpha_i) = 0$ for the odd bridge gives a degenerate normalisation. The standard substitute is the **symmetrised Cartan matrix** $a_{ij} = (\alpha_i, \alpha_j)$ with:

- Even-even simple adjacent: $a_{ii} = 2, a_{i,i+1} = -1$ (as usual $A$-chain).
- Even-even fork (D-type end): $a_{r-1,r-1} = a_{r,r} = 2, a_{r-1,r} = 0, a_{r-2,r} = -1$.
- Odd-odd bridge: $a_{n,n} = 0$ (the bridge simple root is isotropic: $(\alpha_n, \alpha_n) = 0$).
- Bridge–adjacent even: $a_{n-1,n} = -1, a_{n,n+1} = -1$.

For $(r,n) = (2, 10)$, the $12 \times 12$ symmetrised Cartan matrix $A$ has:
- $a_{11} = \ldots = a_{9,9} = 2$ (even $A$-chain on $\mathfrak{sp}$ side),
- $a_{10,10} = 0$ (**odd bridge**),
- $a_{11,11} = a_{12,12} = 2$ (even $D$-fork on $\mathfrak{so}(4)$ side),
- $a_{i,i+1} = -1$ for $i = 1,\ldots, 9$,
- $a_{10,11} = -1$,
- $a_{10,12} = -1$ (or $a_{11,12} = 0, a_{10,12} = -1$ depending on convention — the $D_2 = A_1 \times A_1$ structure at the right end gives two disconnected simple roots attached to the bridge),
- all other entries zero.

A Dynkin diagram (with $\times$ = odd, $\circ$ = even, — = bond):

```
o — o — o — o — o — o — o — o — o — ×    (10 nodes: α_1,...,α_9 even + α_{10} odd bridge)
                                     \
                                      o — o          (α_{11}, α_{12}: the D_2 fork; but D_2 = A_1 x A_1,
                                                      so the "fork" is actually two disjoint bonds α_{10}—α_{11} and α_{10}—α_{12})
```

**(This is the load-bearing combinatorial datum that the chapter does not state anywhere.)**

### H1.5. Serre relations

For $\mathfrak{osp}(m|2n)$ with *one* odd simple root (the distinguished choice), the Serre relations are the **super-Serre relations** of Kac (*Infinite Dimensional Lie Algebras*, 3rd ed., §11.11) and for the Yangian lift, the **quantum super-Serre relations** of Zhang (*Lett. Math. Phys.* 25, 1992) and Stukopin (*J. Math. Sci.* 100, 2000).

**Schematically**: for two even simple roots $\alpha_i, \alpha_j$ adjacent in the Dynkin diagram ($a_{ij} = -1$):
$$(\operatorname{ad} e_i)^{1 - a_{ij}}(e_j) = (\operatorname{ad} e_i)^2(e_j) = [e_i, [e_i, e_j]] = 0.$$

For the even simple root $\alpha_i$ and the odd bridge $\alpha_n$ ($a_{i,n} = -1$ for $i = n-1$ or $i = n+1$, i.e., $i = 9$ or $i = 11$ in our case):
$$(\operatorname{ad} e_i)^2(e_n) = 0 \text{ and } [e_n, e_n] = \{e_n, e_n\} = 0 \text{ (odd generator, anticommutes with itself)}.$$

For the odd bridge $\alpha_n$: the super-Jacobi identity $\{e_n, e_n\} = 2 e_n^2 = 0$ means **the square of the odd generator vanishes as a symmetric bracket** — this is automatic since $(-1)^{|e_n|^2} = -1$ forces the anti-commutator rather than commutator.

The **quadratic super-Serre relation** (not a Chevalley cubic!) between two odd simple roots (absent here since we have only one odd simple root) and the **higher super-Serre** relations (relevant when three mutually non-commuting simple roots meet at an odd node, which again is not our configuration) are irrelevant for $(r,n) = (2,10)$ because the odd bridge has only two neighbours (one on each side — though in $D_r$ with $r = 2$, the "$\mathfrak{so}(4)$-side" has two disconnected even simple roots both adjacent to the bridge, giving the bridge **two even neighbours on the $\mathfrak{so}(4)$-side** and one on the $\mathfrak{sp}(20)$-side, total three neighbours).

**Three neighbours of the odd bridge $\alpha_{10}$**: $\alpha_9$ (from $\mathfrak{sp}$ chain), $\alpha_{11}$ and $\alpha_{12}$ (the two disconnected $A_1$'s of $\mathfrak{so}(4)$). All three are even. The super-Serre for each pair (odd bridge, even neighbour) is the standard quadratic:
$$[e_{10}, [e_{10}, e_j]] = 0 \text{ for } j \in \{9, 11, 12\}, \quad (-1)^{|e_{10}|^2} = -1,$$
with sign:
$$\{e_{10}, [e_{10}, e_j]\} - 0 \cdot [e_{10}, \{e_{10}, e_j\}] \stackrel{?}{=} 0,$$
i.e., the proper super-Serre reads
$$\boxed{\{e_{10}, [e_{10}, e_j]\} = 0 \qquad \text{for } j = 9, 11, 12.}$$
Here the outer bracket is anti-commutator (since $e_{10}$ is odd), and the inner is the ordinary commutator (since $e_{10}$ odd, $e_j$ even gives mixed bracket = commutator up to grading).

The **quartic super-Serre** that appears in some orthosymplectic series $\mathfrak{osp}$ with three odd simple roots meeting at a node is not relevant here.

For the quantum (Yangian) lift: Drinfeld's second presentation gives
$$[h_{i,r}, h_{j,s}] = 0, \qquad [h_{i,0}, x^\pm_{j,s}] = \pm a_{ij} x^\pm_{j,s},$$
$$[h_{i,r+1}, x^\pm_{j,s}] - [h_{i,r}, x^\pm_{j,s+1}] = \pm\tfrac{\hbar}{2} a_{ij}\{h_{i,r}, x^\pm_{j,s}\}_\pm,$$
$$[x^+_{i,r}, x^-_{j,s}] = \delta_{ij} h_{i,r+s},$$
$$[x^\pm_{i,r+1}, x^\pm_{j,s}] - [x^\pm_{i,r}, x^\pm_{j,s+1}] = \pm\tfrac{\hbar}{2} a_{ij} \{x^\pm_{i,r}, x^\pm_{j,s}\}_\pm,$$
**plus the quantum super-Serre** relations, which for the simply-laced bonds ($a_{ij} = -1$, $i,j$ both even) read $[x^\pm_{i,r}, [x^\pm_{i,s}, x^\pm_{j,t}]] + (r \leftrightarrow s) = 0$, and for the bridge–even adjacency read the *super*-version where the outer bracket becomes an anti-commutator when one factor is odd.

**The manuscript's Serre statement at line 1355–1357** — *"$E_i^2 E_j - [2]_q E_i E_j E_i + E_j E_i^2 = 0$"* — is:

1. The quantum-group ($U_q(\mathfrak g)$) quantum Serre relation, not the Yangian ($Y_\hbar(\mathfrak g)$) quantum Serre relation. **These are distinct**; the Yangian version involves spectral parameters and anticommutators on both sides.

2. Written as if all simple roots are even and simply-laced. For the K3 Yangian at an ADE enhancement (where the manuscript invokes it), this is consistent with the ADE sector being a subalgebra $\mathfrak g \subset \mathfrak{osp}(4|20)$ embedded purely on the $\mathfrak{so}(4)$-side or $\mathfrak{sp}(20)$-side — i.e., the ADE sub-Lie-algebra is even (not super).

3. Correct *only if* the ADE root lattice embeds entirely in the even part $\mathfrak{osp}(4|20)_{\bar 0}$. This is what the manuscript implicitly assumes (line 2156–2163: "The $\mathfrak{sl}_2$ subalgebra is the one generated by an $\mathfrak{sp}(2)$-triple inside $\mathfrak{sp}(20) \subset \osp(4|20)_{\bar 0}$"). **Fine**, but the scope should be stated at the Serre-relation stage (line 1355), not only far later at line 2156.

**Verdict H1.5**: the Serre relations in the chapter are correctly stated *for the even part* of $\mathfrak{osp}(4|20)$, and the chapter's restriction to ADE enhancements that embed in the even part is self-consistent. The **missing content** is the super-Serre treatment of the odd bridge $\alpha_{10}$, which would be needed for any non-abelian enhancement that mixes $\mathfrak{so}(4)$ and $\mathfrak{sp}(20)$ via the odd part. The chapter quietly does not invoke such a mixing anywhere.

---

## Round 2 — ATTACK (self-adversarial)

### A2.1. "24 generators" — what counting?

From Attack 1.4.c: the integer 24 is the dimension of the defining $\mathfrak{osp}(4|20)$-representation $V = \mathbb C^4 \oplus \mathbb C^{20}$. In any RTT presentation of the super-Yangian, the generators are $t^{(r)}_{ij}$ with $i, j \in \{1,\ldots,24\}$, $r \geq 1$. So 24 is the *matrix index range*, not the generator count.

In Drinfeld's first presentation, the generators are $3 \cdot \operatorname{rank} = 36$ Chevalley-type generators *plus* one set of degree-$1$ "level lifts" $J(x)$, indexed by the 12 simple roots (so $12$ additional). Total: $36 + 12 = 48$, modulo the relations, which generate the rest via the PBW theorem.

In Drinfeld's second presentation, $\aleph_0$ generators $\kappa_{i,r}, x^\pm_{i,r}$ for $i = 1,\ldots, 12$, $r \geq 0$ — so $3 \cdot 12 = 36$ "families" of generators.

**Reconciliation**: the number $24$ in the K3 Yangian literature is **always the lattice rank**, which equals the defining-representation dimension of the (conjectural) super-Yangian envelope. It is *not* the Chevalley, Drinfeld-current, or Kac–Moody generator count of the super-Yangian. The sentence on line 6 ("24 Heisenberg generators") is *accurate for the abelian $\mathfrak{gl}_1$-specialisation* (where there is no Lie-bracket generator beyond the 24 Heisenberg currents plus one central element), and *inaccurate as a description of the super-Yangian presentation* (where there are 12 Chevalley/Drinfeld simple roots plus many levels).

### A2.2. $\kappa_{\mathfrak{osp}}$ sign and numerical value

Manuscript line 1967:
$$\kappa_{\mathfrak{osp}} = m - n - 2 = 4 - 20 - 2 = -18.$$

But **conventions in the literature vary**:
- Arnaudon et al. 2003 use $\kappa = m - 2n - 2$ (with $2n$ being the symplectic dimension, so for $\mathfrak{osp}(m|2n)$).
- Molev (*Yangians and Classical Lie Algebras*, 2007) uses $\kappa = m/2 - n - 1$ or $m - 2n$, depending on section.
- Kulish–Reshetikhin (1986) use $\eta = (m - n - 2)/2$.

For $\mathfrak{osp}(4|20)$ with $m = 4, 2n = 20$ (so $n = 10$ in the ACDF-R convention):
- ACDF-R: $\kappa = 4 - 2 \cdot 10 - 2 = 4 - 20 - 2 = -18$. Matches the manuscript.

But the manuscript writes "$m - n - 2$" with "$n = 20$", implicitly using $n$ for the odd-space dimension (not for half-the-odd-dimension). **This is a notation slip but gives the correct final number by coincidence** — because ACDF-R's $m - 2n - 2$ with $2n_{\rm ACDF} = n_{\rm manuscript}$ gives $m - n_{\rm manuscript} - 2 = 4 - 20 - 2 = -18$. The coincidence is the factor-of-2 cancellation.

**Then line 2148**: "$\kappa_{\mathfrak{osp}} = (m - n - 2)\hbar/2$... at $(m,n) = (4, 20)$ gives $\kappa_{\mathfrak{osp}} = -9\hbar$".

Now we have a **factor-of-2 inconsistency inside the chapter**:
- Line 1967: $\kappa_{\mathfrak{osp}} = m - n - 2 = -18$ (no $\hbar$, no $/2$).
- Line 2148: $\kappa_{\mathfrak{osp}} = (m - n - 2)\hbar/2 = -9\hbar$.

These are **not equal**. One is twice the other (and one carries $\hbar$, the other doesn't). The crossing-shift identity $T(u)^{\rm st} = T(-u - \kappa_{\mathfrak{osp}})$ uses a specific convention that cannot simultaneously be $-18$ and $-9\hbar$.

**This is a sign-and-factor bug.** In ACDF-R's conventions, the crossing shift carries $\hbar$ explicitly (and equals $\hbar \cdot (m - 2n - 2)/2$). Converting to the manuscript's variables: $\hbar (4 - 20 - 2)/2 = -9\hbar$. So **line 2148 is correct; line 1967 is missing the $\hbar/2$ factor.** The bare integer $-18$ should be $-9\hbar$ throughout.

Alternatively, if $\hbar$ is normalised to $1$, one of $-9$ or $-18$ is the "true" integer; the choice depends on where the factor of $2$ gets absorbed. Either way, **writing both $-18$ and $-9\hbar$ in the same chapter is inconsistent and must be reconciled.**

### A2.3. Does $\mathfrak{osp}(4|20)$ admit a Yangian at all?

For a Lie superalgebra $\mathfrak g$ to admit a Yangian $Y_\hbar(\mathfrak g)$, the minimal requirement is a non-degenerate invariant super-symmetric bilinear form. For $\mathfrak{osp}(m|2n)$, the supertrace form is non-degenerate when $m - 2n \neq 2$ (from the "dual Coxeter number" vanishing condition; see Kac, *Adv. Math.* 26, 1977, Table II). At $(m, 2n) = (4, 20)$: $m - 2n = 4 - 20 = -16 \neq 2$. **Good — Yangian exists.**

ACDF-R explicitly construct the super-Yangian for $\mathfrak{osp}(m|2n)$ at all $(m, 2n)$ away from the critical value. The critical value is $m = 2n + 2$ (where the quadratic Casimir vanishes and the Yangian degenerates). For $(4, 20)$, we are far from critical.

**Verdict A2.3**: no obstruction. The super-Yangian $Y_\hbar(\mathfrak{osp}(4|20))$ exists. The chapter's claim of existence is defensible — but the claim is classical (ACDF-R 2003), not a programme contribution.

### A2.4. Is the "K3 Yangian" $= Y_\hbar(\mathfrak{osp}(4|20))$ or a proper sub?

Here is the delicate point that the manuscript does not resolve.

The K3 Yangian, as constructed in the abelian ($\mathfrak{gl}_1$) case, has structure function $g_{K3}(u) = \prod_{i=1}^{24}(u-h_i)/(u+h_i)$ with 24 free parameters $h_i$ modulo $\sum h_i = 0$ and $\mathrm{Aut}(\widetilde\Lambda)$. This corresponds to **24 copies of a rank-$1$ Heisenberg Yangian**, not to $Y_\hbar(\mathfrak{osp}(4|20))$, which is a *non-abelian* super-Yangian.

At an ADE enhancement $\mathfrak g \hookrightarrow \widetilde\Lambda$, some of the 24 directions merge into a non-abelian $\mathfrak g$-subalgebra. The non-abelian sub-Yangian $Y_\hbar(\mathfrak g)$ acts. The *envelope* containing all 24 directions plus all ADE-enhancements plus all cross-sector pieces is what the manuscript calls $Y_{\mathfrak{osp}(4|20)}$.

**Claim** (from the manuscript, conjectural): $Y(\mathfrak g_{K3}) \subset Y_\hbar(\mathfrak{osp}(4|20))$ as a sub-super-Yangian, with the Cartan subalgebra of $Y_\hbar(\mathfrak{osp}(4|20))$ containing all 24 Heisenberg currents $J_i$ and the 1 central element $\mathbf c$.

But: **the Cartan of $\mathfrak{osp}(4|20)$ has rank 12, not 24**. So at most 12 of the 24 Mukai directions can be Cartan generators of $\mathfrak{osp}(4|20)$. The other 12 must be root generators (positive or negative), i.e., nilpotent in the Lie-algebra presentation.

This is a **real tension** that the manuscript does not address. Either:

(a) $Y(\mathfrak g_{K3})|_{\rm abelian}$ is **not** a sub-super-Yangian of $Y_\hbar(\mathfrak{osp}(4|20))$ — it is a quite different object, built from 24 mutually-commuting Heisenberg currents (a commutative Cartan), whereas $Y_\hbar(\mathfrak{osp}(4|20))$ has rank-12 Cartan plus root generators.

(b) Or, $Y(\mathfrak g_{K3})|_{\rm abelian}$ is the abelianisation (trivial-Serre quotient) of $Y_\hbar(\mathfrak{osp}(4|20))$ along the **extended Cartan** (the 24-dimensional space $\mathfrak h \oplus \mathfrak h^\ast$ spanned by the full set of generators including both positive and negative roots in the Cartan weight-zero sector) — **but this is not a sub-object; it is a quotient / subquotient**.

The manuscript's language at line 1855–2071 vacillates between "the non-abelian K3 Yangian *is* $Y_{\mathfrak{osp}(4|20)}$" (so the abelian case would be a sub) and "$Y_{\mathfrak{osp}(4|20)}$ *is the envelope*" (so the abelian case would be the specialisation, perhaps quotient, perhaps degenerate limit).

**This is a load-bearing ambiguity** (Pattern 236 scope-ambient confusion). Resolving it requires a precise statement like:

> "There is a surjective map $Y_\hbar(\mathfrak{osp}(4|20)) \twoheadrightarrow Y(\mathfrak g_{K3})$ obtained by factoring through the abelianisation along the Cartan plus the trivial-Serre-ideal quotient. The K3 Yangian in the abelian sense is the image of the generators $\{J_i\}_{i=1}^{24}$ in the abelianised quotient."

Or:

> "$Y(\mathfrak g_{K3})$ is defined as the tensor product of 24 rank-1 Heisenberg Yangians with Mukai-constrained spectral parameters. It is not a subalgebra of $Y_\hbar(\mathfrak{osp}(4|20))$; rather, $Y_\hbar(\mathfrak{osp}(4|20))$ is a conjectural non-abelian enhancement."

**Neither statement appears in the chapter.** The chapter hedges on the relationship.

---

## Round 2 — HEAL

### H2.1. Corrected positioning

The correct scoping is:

1. **Classical object ($\mathfrak{gl}_1$, abelian)**: $Y(\mathfrak g_{K3})$ is the rank-$24$ Heisenberg Yangian with Mukai parameters. **Classical; no obstruction.**

2. **Non-abelian enhancement at a single ADE node $\mathfrak g$**: $Y_\hbar(\mathfrak g)$ acts on the directions within the ADE sublattice, and commutes with the Heisenberg currents on the orthogonal complement (by the lattice orthogonality claim at line 1400–1416 — **which is correct provided** the ADE sublattice is a *primitive* sublattice of $\widetilde\Lambda$, i.e., the inclusion splits as a direct sum of lattices; this fails for certain embeddings). **Semi-classical for individual ADE nodes; the claim of splitting / orthogonality is a lattice-theoretic lemma that should be stated precisely, with the scope "for primitive embeddings only".**

3. **Full non-abelian envelope $Y_\hbar(\mathfrak{osp}(4|20))$**: classical existence (ACDF-R 2003). Its relationship to the K3 Yangian is **conjectural**: one expects $Y_\hbar(\mathfrak{osp}(4|20))$ to be a non-abelian envelope that specialises, degenerates, or projects to the $\mathfrak{gl}_1$ abelian K3 Yangian on the Cartan, with the 12 Cartan generators absorbing 12 of the 24 Mukai Heisenberg currents and the other 12 appearing as non-trivial root generators. **This is the genuinely open mathematical question** — and it is not stated precisely anywhere in the chapter.

### H2.2. Corrected headline

The chapter's current headline (line 4–7):

> "The K3 double current algebra $\mathfrak g_{K3}$ is the classical limit of the K3 Yangian $Y(\mathfrak g_{K3})$, whose 24 Heisenberg generators, Mukai-signature Serre relations, and degree-$(24, 24)$ structure function encode the quantization of the Mukai lattice."

Should be rewritten to distinguish:

> "The abelian K3 Yangian $Y(\mathfrak g_{K3})|_{\mathfrak g = \mathfrak{gl}_1}$ is a rank-$24$ Heisenberg Yangian with 24 commuting Heisenberg currents, **trivial Serre relations**, and degree-$(24, 24)$ structure function $g_{K3}(u)$. The non-abelian envelope, conjecturally a super-Yangian $Y_\hbar(\mathfrak{osp}(4|20))$ attached to the Mukai orthogonal form, has rank $12$, with $11$ even simple roots and $1$ odd bridge simple root; its explicit Drinfeld presentation at rank $(4|20)$ is classical (ACDF-R 2003) but not carried out in this chapter."

**"Mukai-signature Serre relations"** is a slogan, not a precise statement. The actual Serre relations at enhancement points are the **standard simply-laced $A_n, D_n, E_n$ quantum-Serre relations** (line 1355–1357), **not** any new Mukai-signature-dependent relations. The Mukai signature enters the **$R$-matrix and the structure function**, not the Serre relations. Deleting "Mukai-signature Serre relations" from the headline is a correction.

### H2.3. Reconciliation of the $\kappa_{\mathfrak{osp}}$ factor-of-2

Line 1967 ("$\kappa_{\mathfrak{osp}} = m - n - 2 = -18$") should be corrected to either:
- $\kappa_{\mathfrak{osp}} = (m - n - 2)/2 = -9$ (if $\hbar$ is absorbed into the generator normalisation), or
- $\kappa_{\mathfrak{osp}} = \hbar(m - n - 2)/2 = -9\hbar$ (if $\hbar$ is explicit).

Whichever convention is chosen, it must be used consistently; the chapter cannot have $-18$ at one line and $-9\hbar$ at another. (Note: the ACDF-R paper, which the chapter cites, uses $m - 2n - 2$ where the "$2n$" refers to the symplectic dimension; in that convention, $-9\hbar$ — i.e., $(m - 2n - 2)/2 \cdot \hbar$ with $m = 4, 2n = 20$ — is the standard value.)

---

## Round 3 — final verification

### V1. Simple-root list for $D(2|10)$ explicitly

In basis $\delta_1, \ldots, \delta_{10}, \varepsilon_1, \varepsilon_2$ with pairings $(\delta_i, \delta_j) = -\delta_{ij}$ (negative, from $\mathfrak{sp}$), $(\varepsilon_i, \varepsilon_j) = +\delta_{ij}$ (positive, from $\mathfrak{so}$), and $(\delta_i, \varepsilon_j) = 0$:

Distinguished simple roots:
- $\alpha_1 = \delta_1 - \delta_2$ (even, norm $-2$)
- $\alpha_2 = \delta_2 - \delta_3$
- $\vdots$
- $\alpha_9 = \delta_9 - \delta_{10}$
- $\alpha_{10} = \delta_{10} - \varepsilon_1$ (**odd**, norm $-1 + 1 = 0$)
- $\alpha_{11} = \varepsilon_1 - \varepsilon_2$ (even, norm $+2$)
- $\alpha_{12} = \varepsilon_1 + \varepsilon_2$ (even, norm $+2$)

[$\alpha_{11}$ and $\alpha_{12}$ are the two simple roots of the $D_2 = A_1 \times A_1$ fork from the $\mathfrak{so}(4)$ side.]

**Pairings of adjacent simple roots**:
- $(\alpha_i, \alpha_{i+1}) = +1$ for $i = 1,\ldots, 8$ (both from $\mathfrak{sp}$ side)
- $(\alpha_9, \alpha_{10}) = (\delta_9 - \delta_{10}, \delta_{10} - \varepsilon_1) = -(-1) - 0 = +1$
- $(\alpha_{10}, \alpha_{11}) = (\delta_{10} - \varepsilon_1, \varepsilon_1 - \varepsilon_2) = 0 - 1 = -1$
- $(\alpha_{10}, \alpha_{12}) = (\delta_{10} - \varepsilon_1, \varepsilon_1 + \varepsilon_2) = 0 - 1 = -1$
- $(\alpha_{11}, \alpha_{12}) = (\varepsilon_1 - \varepsilon_2, \varepsilon_1 + \varepsilon_2) = 1 - 1 = 0$ [disconnected $A_1$'s].

**Cartan matrix** $(a_{ij})$ in the usual $a_{ij} = 2(\alpha_i,\alpha_j)/(\alpha_i,\alpha_i)$ form (with the understanding that $a_{i,i} = 0$ for the odd bridge replaced by the symmetrised form):

- For $i = 1, \ldots, 9$: $(\alpha_i, \alpha_i) = -2$, so $a_{ii} = 2$ in the symmetrised normalisation. Hmm wait — here the sign is tricky. $(\alpha_i, \alpha_i) = 2 \cdot (-1) = -2$, hence after rescaling to a positive form (via $-(\cdot, \cdot)$ on the $\mathfrak{sp}$ side): $a_{ii} = 2$.
- Adjacent pairs: $a_{i,i+1} = -1$ for $i = 1, \ldots, 8$. (After sign rescaling.)
- $a_{9,10}$: $(\alpha_9, \alpha_{10}) = +1$ and $(\alpha_9, \alpha_9) = -2 \Rightarrow a_{9, 10} = 2 \cdot 1 / (-2) = -1$. OK.
- $a_{10,10} = 0$ (odd bridge).
- $a_{10,11}$: $(\alpha_{10}, \alpha_{11}) = -1$, use $(\alpha_{11}, \alpha_{11}) = 2$: $a_{10,11} = 2(-1)/2 = -1$.
- $a_{10,12} = -1$ similarly.
- $a_{11, 12} = 0$.

$12 \times 12$ Cartan matrix (displaying nonzero entries only, with rows/columns indexed $1,\ldots,12$):

```
      1  2  3  4  5  6  7  8  9  10 11 12
  1 [ 2 -1  0  0  0  0  0  0  0   0  0  0 ]
  2 [-1  2 -1  0  0  0  0  0  0   0  0  0 ]
  3 [ 0 -1  2 -1  0  0  0  0  0   0  0  0 ]
  4 [ 0  0 -1  2 -1  0  0  0  0   0  0  0 ]
  5 [ 0  0  0 -1  2 -1  0  0  0   0  0  0 ]
  6 [ 0  0  0  0 -1  2 -1  0  0   0  0  0 ]
  7 [ 0  0  0  0  0 -1  2 -1  0   0  0  0 ]
  8 [ 0  0  0  0  0  0 -1  2 -1   0  0  0 ]
  9 [ 0  0  0  0  0  0  0 -1  2  -1  0  0 ]
 10 [ 0  0  0  0  0  0  0  0 -1   0 -1 -1 ]   <-- odd bridge: a_{10,10} = 0
 11 [ 0  0  0  0  0  0  0  0  0  -1  2  0 ]
 12 [ 0  0  0  0  0  0  0  0  0  -1  0  2 ]
```

(This is the explicit Cartan matrix that should appear in a Kac-school write-up of the K3 Yangian and does not appear anywhere in the chapter.)

### V2. Serre relations, symbolic, for one even simple root

For $\alpha_1 = \delta_1 - \delta_2$ (even, $A$-chain on $\mathfrak{sp}$-side) and $\alpha_2 = \delta_2 - \delta_3$ (even, adjacent): $a_{12} = -1$.

**Classical Lie-superalgebra Serre**:
$$(\operatorname{ad} e_1)^{1 - a_{12}}(e_2) = (\operatorname{ad} e_1)^2(e_2) = [e_1, [e_1, e_2]] = 0.$$

**Drinfeld-first Yangian Serre** (quantum deformation with $\hbar$):
$$\operatorname{Sym}_{s_1, s_2}[e_{1,s_1}, [e_{1,s_2}, e_{2, r}]] = 0 \qquad \forall r \geq 0,\ s_1, s_2 \geq 0.$$

**Drinfeld-second (current) Yangian Serre**:
$$\mathrm{Sym}_{s_1, s_2}[x^+_{1, s_1}, [x^+_{1, s_2}, x^+_{2, r}]] = 0 \qquad \forall r, s_1, s_2 \geq 0.$$

All three are correctly stated in the standard references (Drinfeld 1985, Chari–Pressley 1994 Chapter 12). **None** are written out in the K3 Yangian chapter.

### V3. Coproduct for Drinfeld-first $Y_\hbar(\mathfrak{osp}(4|20))$

On Chevalley generators $x \in \mathfrak g$ (either $e_i, f_i, h_i$):
$$\Delta(x) = x \otimes 1 + 1 \otimes x.$$
On level-$1$ generators $J(x)$ (the "level-shift" generators corresponding to quadratic Casimir images):
$$\Delta(J(x)) = J(x) \otimes 1 + 1 \otimes J(x) + \tfrac{\hbar}{2}[x \otimes 1, \Omega] + \text{super-corrections},$$
where $\Omega$ is the quadratic Casimir element and super-corrections come from the odd simple root. Specifically, for the odd bridge $\alpha_{10}$:
$$\Delta(J(e_{10})) = J(e_{10}) \otimes 1 + 1 \otimes J(e_{10}) + \tfrac{\hbar}{2}[e_{10} \otimes 1, \Omega_s],$$
where $\Omega_s$ is the super-symmetrised Casimir with a $(-1)^{|{\cdot}||{\cdot}|}$ sign correction.

(None of these coproduct formulas are written out in the chapter.)

---

## Falsifications with file:line citations

**F1. Line 6** (chapter header): *"24 Heisenberg generators, Mukai-signature Serre relations, and degree-$(24, 24)$ structure function encode the quantization of the Mukai lattice."*

- "24 Heisenberg generators": correct for $\mathfrak{gl}_1$-abelian; **inaccurate** for the non-abelian envelope (rank $12$ means 12 Cartan plus root-space generators).
- "Mukai-signature Serre relations": **vacuous**. The Serre relations at ADE enhancements are *standard simply-laced quantum-Serre*; the Mukai signature enters the structure function and $R$-matrix, not the Serre ideal. The phrase misleadingly suggests a novel signature-dependent Serre rule.
- "degree-$(24,24)$ structure function": correct for the abelian case.

**Recommended fix**: distinguish the abelian and non-abelian objects in the header.

**F2. Line 1967 vs line 2148**: $\kappa_{\mathfrak{osp}} = -18$ vs $\kappa_{\mathfrak{osp}} = -9\hbar$. **Factor-of-2 inconsistency.**

**Recommended fix**: unify conventions. The ACDF-R convention gives $-9\hbar$; the bare-integer form $-18$ should be written as $(m - n - 2) = -18$ with the understanding that the crossing shift in the $T$-matrix reflection is $(m - n - 2)\hbar/2 = -9\hbar$.

**F3. Lines 1855–2223 (entire super-Yangian section)**: the Cartan subalgebra, rank ($=12$, not $24$), simple-root system, and Cartan matrix of $\mathfrak{osp}(4|20)$ are **nowhere stated**.

**Recommended fix**: add a short subsection immediately after Definition `def:osp-super-yangian-K3` stating (i) rank $=12$, (ii) 11 even + 1 odd simple roots, (iii) the $12 \times 12$ Cartan matrix displayed in V1 above, (iv) the Dynkin-diagram drawing.

**F4. Line 1355–1357**: the "quantum Serre" $E_i^2 E_j - [2]_q E_i E_j E_i + E_j E_i^2 = 0$ is the **quantum-group** (Drinfeld–Jimbo $U_q(\mathfrak g)$) Serre, not the **Yangian** Serre. These are *distinct* relations. The Yangian Serre involves spectral parameters and an $\hbar$-graded symmetrisation.

**Recommended fix**: either change "quantum Serre" to "quantum-group Serre" (scope restriction), or replace with the Drinfeld-first Yangian Serre $\mathrm{Sym}_{s_1, s_2}[e_{1,s_1}, [e_{1,s_2}, e_{2,r}]] = 0$ and cite Drinfeld 1985 / Chari–Pressley 1994 §12.1.

**F5. Line 831–846 (Remark "Classical attribution")**: the attribution to Drinfeld 1985 + Chari–Pressley 1994 is *almost* right. But the statement "Drinfeld's original definition of $Y_\hbar(\mathfrak g)$ depends only on the Killing form up to non-degeneracy, not on its signature" is **imprecise**. Drinfeld 1985 works with a **complex** simple Lie algebra, where the Killing form is automatically non-degenerate and of indefinite signature over the reals. There is no "signature" in the complex case. The real-form subtlety (choosing $\mathfrak{so}(4, 20)$ vs $\mathfrak{so}(24)$) is what introduces signature. **The Mukai lattice's indefiniteness affects representation theory (Shapovalov form sign indefiniteness, unitarity of highest-weight modules) but not the algebra structure.** The manuscript is conflating these.

**Recommended fix**: clarify that the Yangian algebra $Y_\hbar(\mathfrak g_{\mathbb C})$ is defined over $\mathbb C$ and the signature enters only when one passes to real forms (for unitary representations) or to signature-sensitive Shapovalov inner products.

**F6. Lines 1400–1416 (Remark "Mechanism: orthogonality from the Mukai lattice")**: the claim $I_{\mathrm{mix}} = 0$ depends on the ADE sublattice embedding $\Lambda_{\mathfrak g} \hookrightarrow \widetilde\Lambda$ being **primitive and orthogonally split** (i.e., $\widetilde\Lambda = \Lambda_{\mathfrak g} \oplus \Lambda_{\mathfrak g}^\perp$ as lattices, not merely as rational vector spaces).

But: **not every ADE embedding in $\widetilde\Lambda$ splits orthogonally**. For example, an $A_1$ root $\alpha$ with $\alpha^2 = -2$ sitting in $\widetilde\Lambda$ has orthogonal complement of rank $23$, and this orthogonal complement need not itself be a lattice direct summand — its discriminant form can be non-trivial, obstructing splitting.

**Recommended fix**: state the scope "for *primitive orthogonal* embeddings $\Lambda_{\mathfrak g} \hookrightarrow \widetilde\Lambda$" and cite Nikulin (*Izv. Akad. Nauk* 14, 1980, §1.5) for the lattice-theoretic criterion. For non-primitive or non-split embeddings, $I_{\rm mix} \neq 0$ and the Serre ideal decomposition fails.

**F7. Line 2066–2070 (Remark "Alternative: non-super $Y(\mathfrak{so}(4, 20))$")**: the claim "$\mathfrak{so}(4,20)$ and $\mathfrak{osp}(4|20)$ Yangians ... agree at the level of the split Cartan" is technically correct only for a very specific identification. The Cartan of $Y(\mathfrak{so}(4,20))$ has rank $\lfloor(4+20)/2\rfloor = 12$ (from $\mathfrak{so}(24)_{\mathbb C}$ rank); the Cartan of $Y_\hbar(\mathfrak{osp}(4|20))$ also has rank $12$. **Ranks coincide, dimensions coincide.** But the Cartans sit inside larger algebras ($\mathfrak{so}(24)$ has dim $276$; $\mathfrak{osp}(4|20)$ has super-dim $296$), and the root systems are different (no super roots for $\mathfrak{so}(24)$; one odd simple root for $\mathfrak{osp}(4|20)$). **"Agreement at the level of the split Cartan" is accurate for dimension/rank but misleading for root-system structure.**

**Recommended fix**: state more carefully. "The Cartan subalgebras of $Y(\mathfrak{so}(4,20))$ and $Y_\hbar(\mathfrak{osp}(4|20))$ are both $12$-dimensional; the root systems differ in that the latter has one odd simple root (the bridge $\alpha_{10}$), absent in the former."

---

## Deliverable — synthesis

### (i) Precise Lie-algebraic foundation statement

**$\mathfrak g_{K3}$ (classical)**: the R-current algebra with $R = H^\ast(S,\mathbb C)$ and pairing $\langle\cdot,\cdot\rangle_{\rm Muk}$. At $\mathfrak g = \mathfrak{gl}_1$: the 25-dimensional K3 Heisenberg algebra $H_{\rm Muk}$ (24 abelian + 1 central), two-step nilpotent, with defining form Mukai pairing of signature $(4,20)$.

**$\mathfrak{osp}(4|20)$** (conjectural non-abelian envelope): orthosymplectic super-Lie algebra of type $D(2|10)$; Type II in Kac's classification; even part $\mathfrak{so}(4) \oplus \mathfrak{sp}(20)$ of dimension $216$; odd part $\mathbb C^4 \otimes \mathbb C^{20}$ of dimension $80$; total super-dim $296$; rank $12$; $11$ even + $1$ odd simple root; Cartan matrix as displayed in V1 above. Invariant bilinear form: supertrace on the defining $(4|20)$-dim rep; non-degenerate since $m - 2n - 2 = -18 \neq 0$.

### (ii) Yangian presentation

**Drinfeld first presentation** (for Chevalley generators of $Y_\hbar(\mathfrak{osp}(4|20))$):

Generators: $e_i, f_i, h_i$ for $i = 1,\ldots, 12$ (Chevalley generators of $\mathfrak{osp}(4|20)$), with $e_{10}, f_{10}$ **odd** (all others even); plus level-$1$ generators $J(e_i), J(f_i), J(h_i)$ that satisfy
$$[J(x), y] = [x, J(y)] \text{ for all } x, y \in \mathfrak g;$$
$$\Delta(J(x)) = J(x) \otimes 1 + 1 \otimes J(x) + \tfrac{\hbar}{2}[x \otimes 1, \Omega_s],$$
with $\Omega_s = \sum_a (-1)^{|T_a|} T^a \otimes T_a$ the super-symmetrised quadratic Casimir.

Relations:
- $\mathfrak{osp}(4|20)$-relations (on $(e, f, h)$): standard Chevalley-super relations with the Cartan matrix above.
- Super-Serre on $e$'s and $f$'s: $(\operatorname{ad} e_i)^{1-a_{ij}}(e_j) = 0$ for even $i$, $a_{ij}$ standard; super-version for adjacency with $i = 10$ (odd bridge): $\{e_{10}, [e_{10}, e_j]\} = 0$ for $j \in \{9, 11, 12\}$.
- Yangian commutation rules between $(J(x), y)$ and $(J(x), J(y))$ — the ACDF-R super-extension of Drinfeld 1985.

**Drinfeld second (current) presentation**: generators $\kappa_{i,r}, x^\pm_{i,r}$ for $i = 1,\ldots, 12$, $r \geq 0$, with $x^\pm_{10, r}$ odd; relations are the super-extension of Drinfeld's current relations (standard; see Stukopin 2000, Gow 2007).

**RTT presentation**: the reflection-equation presentation of the chapter (Def. `def:osp-super-yangian-K3`, line 1919–2000), with rational orthosymplectic $R$-matrix $R^{\osp}(u)$ (Kulish–Reshetikhin 1986) and reflection matrix $K(u)$ encoding the indefinite signature. **At $K = \mathrm{Id}$: reduces to super-RTT on the $\mathfrak{osp}$-invariant subspace.**

### (iii) Serre relations written out (for one simple-root pair)

**For even pair $(\alpha_1, \alpha_2)$** (both even, $a_{12} = -1$):

- Classical Lie superalgebra: $[e_1, [e_1, e_2]] = 0$.
- Drinfeld-first Yangian: $\mathrm{Sym}_{s_1, s_2 \geq 0}[e_{1,s_1}, [e_{1,s_2}, e_{2, r}]] = 0$ for all $r \geq 0$.
- Current presentation: $\mathrm{Sym}_{s_1, s_2 \geq 0}[x^+_{1, s_1}, [x^+_{1, s_2}, x^+_{2, r}]] = 0$.

**For odd bridge adjacency $(\alpha_9, \alpha_{10})$** (even-odd, $a_{9,10} = -1$):

- Classical: $\{e_9, [e_9, e_{10}]\}$ ... wait: $e_9$ is even, $e_{10}$ is odd. The super-Serre for an even generator acting on an odd one with $a_{ij} = -1$:
$$(\operatorname{ad} e_9)^2(e_{10}) = [e_9, [e_9, e_{10}]] = 0.$$
[Standard commutator on even-generator side.]

Conversely, $(\operatorname{ad} e_{10})^2(e_9)$ involves $\{e_{10}, [e_{10}, e_9]\}$ (outer anticommutator since $e_{10}$ odd, inner commutator since $e_{10}$ odd + $e_9$ even gives mixed = commutator up to graded sign):
$$\{e_{10}, [e_{10}, e_9]\} = 0.$$

Both of these are the super-Serre relations at the odd bridge. Yangian lift: replace commutators with $\hbar$-symmetrised bracket as in Drinfeld 1985 §6.

### (iv) Falsifications of over-claims

Summary table:

| ID | Location | Claim | Falsification |
|----|----------|-------|---------------|
| F1 | Line 6 | "24 Heisenberg generators, Mukai-signature Serre relations, degree-$(24,24)$ structure function" | Conflates abelian and non-abelian; "24 generators" ≠ rank of non-abelian envelope (= 12); "Mukai-signature Serre relations" is a misleading slogan (Serre relations are standard simply-laced ADE at enhancement points) |
| F2 | Line 1967 vs 2148 | $\kappa_{\mathfrak{osp}} = -18$ vs $-9\hbar$ | Factor-of-2 inconsistency; must be unified |
| F3 | Lines 1855–2223 | super-Yangian existence | Rank, Cartan subalgebra, simple roots, Cartan matrix never stated; the load-bearing combinatorial data is missing |
| F4 | Lines 1355–1357 | "simply-laced quantum Serre" | Mis-labeled as quantum-group Serre rather than Yangian Serre; correct relation in Yangian involves spectral parameters |
| F5 | Lines 831–846 | "depends only on the Killing form up to non-degeneracy, not on its signature" | Imprecise: signature is absent in complex Lie-algebra Yangian; appears only for real forms / Shapovalov unitarity |
| F6 | Lines 1400–1416 | "$I_{\rm mix} = 0$ by Mukai-lattice orthogonality" | Scope: requires primitive orthogonally-split sublattice embedding; non-split embeddings obstruct $I_{\rm mix} = 0$ |
| F7 | Lines 2066–2070 | $\mathfrak{so}(4,20)$ and $\mathfrak{osp}(4|20)$ Yangians "agree on split Cartan" | Correct for rank/dimension; misleading for root system (odd bridge absent on the non-super side) |

### Overall assessment

- **Classical claims (abelian $\mathfrak{gl}_1$ K3 Yangian)**: all load-bearing formulas are correct. The presentation is a Chari–Pressley-style Heisenberg Yangian with Mukai-constrained parameters. Classical modulo cosmetic issues (factor-of-2 in $\kappa_{\mathfrak{osp}}$; scope of "orthogonality" lemma).
- **Conjectural claims (non-abelian $Y_\hbar(\mathfrak{osp}(4|20))$)**: existence is classical (ACDF-R 2003); Cartan/Serre data is correctly delegated to the general orthosymplectic-super-Yangian literature but **never explicitly written out in the chapter**. The relationship to the abelian K3 Yangian (sub? quotient? specialisation?) is ambiguous and should be resolved by a single precise definition.
- **Kac-school sign count**: passes with two caveats. (i) The factor-of-2 in $\kappa_{\mathfrak{osp}}$ is inconsistent between two locations. (ii) The orthosymplectic supertranspose and the super-Serre at the odd bridge are not explicitly treated; the chapter implicitly restricts to even-subalgebra sectors ($\mathfrak{so}(4) \oplus \mathfrak{sp}(20)$), which is a scope restriction that should be made explicit.

A Kac-school rewrite would: (a) explicitly state rank = 12, Cartan matrix, simple-root system for $\mathfrak{osp}(4|20)$ as a dedicated proposition immediately after the definition; (b) unify the $\kappa_{\mathfrak{osp}}$ convention; (c) split the headline of the chapter to distinguish the abelian K3 Yangian (classical, proved) from the non-abelian $\mathfrak{osp}$-super-Yangian envelope (classical existence, conjectural as the non-abelian K3 Yangian); (d) state the super-Serre relations at the odd bridge explicitly to forestall the reader assuming only simply-laced ADE dynamics.

---

*Raeez Lorgat.*
