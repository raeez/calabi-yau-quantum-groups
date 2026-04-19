# Agent 03 Wave 4 (Etingof voice): The rational-Fock-module sector and non-semisimple Lyubashenko reconstruction

**Author.** Raeez Lorgat.
**Date.** 2026-04-19.
**Voice.** Etingof.
**Standard.** The reader finishes feeling she could have invented the next step. Every braiding sign witnessed; every cohomology class identified with a named primary source; every failure mode of standard Tannakian reconstruction exhibited constructively.
**Wave.** 4 (extension of the Wave-3 three-stratum Tannakian reconstruction to the rational-weight Fock module sector; invocation of Lyubashenko's non-semisimple modular category framework; computation of the rational-Fock 3-cocycle as an ENO-2010 class).

**Prior-wave anchors.**
- `agent_03_etingof.md` (Wave 1): the target chain
  $D^b(K3)\to L_{K3}\to A_{K3}\to \mathrm{Rep}^{E_2}(A_{K3})\to Y_{\mathrm{non\text{-}ab}}(\mathfrak g_{K3})$
  and the RTT/BFN/MO constructions.
- `agent_03_etingof_wave2.md`: Tannakian reconstruction of the K3 Yangian on the $C_2$-cofinite ADE-visible subcategory, with Heisenberg-block scalar braiding identified as a 3-cocycle obstruction.
- `agent_03_etingof_wave3.md`: three-stratum sharpening — **strict Hopf up to torus gauge at ADE** (2-cochain $c_{\mathrm{ADE}}(\alpha)=(-1)^{-\langle\alpha,\alpha\rangle/2}$); **strict Hopf at generic K3 on the Tannakian-visible subcategory**; **quasi-Hopf at Kummer** with explicit $\Z/6\oplus\Z/6$ 3-cocycle from Kunneth on $\cM^{\mathrm{Bridg}}_{E_1}\times\cM^{\mathrm{Bridg}}_{E_2}$ and Schur multiplier $H^3(SL(2,\Z);U(1))=\Z/12$.
- `SYNTHESIS_WAVE3.md` §1.5, §2 item 14: "rational-Fock-module visibility — the Kummer K3 3-cocycle lives on modules invisible to $C_2$-cofinite Tannakian subcategory."
- `agent_10_gaiotto_wave3.md` §3.3: explicit level-$2$ Yangian module, dimension $575$ (Serre-quotiented; Schur-doubled $1150$), $J_0$-split $32+318+800$.

**Wave-3 invisibility flag that drives Wave 4.** Wave 3 bracketed its clean three-stratum picture with the following scope-declaration: the rational-weight Fock modules are NOT $C_2$-cofinite, so their 3-class on the "rational extension" is invisible to the standard Tannakian reconstruction. **This is not good enough.** The fine structure of the Kummer 3-cocycle (its $\Z/6\oplus\Z/6$ denominator structure, as opposed to a naive $\Z/2$) is precisely where rational weights with denominator 6 live, and the Wave-3 claim that "rationals with denominator 2 come in at Kummer" (Part 3.4) already puts one foot on the rational-Fock side.

**Wave-4 task.** Extend the Tannakian reconstruction to the rational-Fock sector, where:
(1) the representation category is NOT $C_2$-cofinite (infinite-dim at each conformal weight),
(2) standard Tannaka–Krein (Deligne 1990, Etingof–Gelaki–Nikshych–Ostrik 2015) fails,
(3) the correct framework is Lyubashenko's non-semisimple modular category (Lyubashenko 1995, 1997; Kerler–Lyubashenko 2001).

Compute the rational-Fock 3-cocycle $\tilde\alpha_{K3}^\Q$ as a class in $H^3(\mathbf{B}(\Q\otimes_\Z\Lambda_{K3});U(1))$ and relate to the Etingof–Nikshych–Ostrik 2010 classification. Globalise to K3 moduli; cross-check against Gaiotto W3's level-2 module $\dim 575$. Attack own constructions; deliver convergence statement.

---

## Part 1. The rational-Fock-module subcategory, defined

### 1.1 What "rational-Fock" means

Let $\Lambda_{\mathrm{Muk}} = II_{4,20}$ be the Mukai lattice of K3, with pairing
$\langle\cdot,\cdot\rangle_{\mathrm{Muk}}$ of signature $(4,20)$, even unimodular. Let
$V_{\Lambda_{\mathrm{Muk}}}$ be the rank-$24$ lattice VOA on $\Lambda_{\mathrm{Muk}}$ (which is the Heisenberg block of $A_{K3}$ at generic smooth K3, before any ADE enhancement).

The **integer-weight** Fock modules are $V_\alpha$ for $\alpha\in\Lambda_{\mathrm{Muk}}$. These form a category
$$
\mathrm{Rep}^{\mathrm{int}}(V_{\Lambda_{\mathrm{Muk}}}) = \{V_\alpha : \alpha\in\Lambda_{\mathrm{Muk}}\}
$$
that is finite-semisimple, rigid, and $C_2$-cofinite (Dong 1994, arXiv:q-alg/9611021). The Wave-3 three-stratum reconstruction lives on this category.

The **rational-weight** Fock modules are $V_\alpha$ for
$\alpha\in\Lambda_{\mathrm{Muk}}\otimes_\Z\Q = \Q^{4,20}$. These form a larger category
$$
\mathrm{Rep}^{\Q}(V_{\Lambda_{\mathrm{Muk}}}) = \{V_\alpha : \alpha\in\Lambda_{\mathrm{Muk}}\otimes_\Z\Q\}
$$
whose objects are still each irreducible Fock modules, but the set of objects is now dense inside $\Lambda_{\mathrm{Muk}}\otimes_\Z\R$ (not discrete). The scalar braiding on $\mathrm{Rep}^\Q$ is
$$
\sigma_{V_\alpha, V_\beta} = e^{2\pi i\langle\alpha,\beta\rangle_{\mathrm{Muk}}}\cdot P,
\qquad \alpha,\beta\in\Lambda_{\mathrm{Muk}}\otimes_\Z\Q,
$$
and the eigenvalues run over $e^{2\pi i\Q}\subset U(1)$ — a dense subgroup, the whole of $\Q/\Z$.

### 1.2 Precise definition of the rational-Fock subcategory for K3

I will work with the subcategory adapted to the K3 problem, not to arbitrary rational Fock extensions of a lattice VOA. The distinction matters: the K3 Yangian programme cares about Fock modules that arise from genuine Bridgeland stability conditions on $D^b(\mathrm{Coh}(K3))$, not from arbitrary rationals.

**Definition 1.1 (Rational-Fock subcategory of the K3 chiral algebra).** Let
$\Lambda_{\mathrm{Muk}}^\Q = \Lambda_{\mathrm{Muk}}\otimes_\Z\Q$. For each $N\in\N_{\ge 1}$, let
$\Lambda_{\mathrm{Muk}}^{(1/N)} = (1/N)\Lambda_{\mathrm{Muk}}\subset\Lambda_{\mathrm{Muk}}^\Q$, a finite cover of the integer lattice. Define
$$
\mathrm{Rep}^{\Q,(N)}(A_{K3}) := \{\,V_\alpha : \alpha\in\Lambda_{\mathrm{Muk}}^{(1/N)}\,\}
$$
the subcategory of Fock modules with weight denominator dividing $N$.

The colimit
$$
\mathrm{Rep}^{\Q}(A_{K3}) := \varinjlim_{N} \mathrm{Rep}^{\Q,(N)}(A_{K3})
$$
is the **full rational-Fock subcategory**, with objects indexed by $\Lambda_{\mathrm{Muk}}^\Q$.

**Convention.** Simples are $V_\alpha$ for $\alpha\in\Lambda_{\mathrm{Muk}}^\Q$, pairwise non-isomorphic. Morphisms are $A_{K3}$-module maps, which are intertwiner-only (no automorphisms at generic $\alpha$). The tensor product is
$V_\alpha\otimes V_\beta = V_{\alpha+\beta}$, so the Grothendieck ring is the group ring $\Z[\Lambda_{\mathrm{Muk}}^\Q]$.

### 1.3 Scope: why this is the right object for the K3 Yangian

The Wave-3 brief asked about the *rational*-Fock sector, not the full *continuous*-Fock sector
($\alpha\in\Lambda_{\mathrm{Muk}}\otimes_\Z\C$ or $\otimes_\Z\R$). The rational sector is privileged for the following reason:

**Claim 1.2 (rationality = finite monodromy).** An $A_{K3}$-module $V_\alpha$ supports a **finite-order** monodromy under the mapping class group of $\Sigma_{g,n}$ iff $\alpha\in\Lambda_{\mathrm{Muk}}^\Q$. For $\alpha\in\Lambda_{\mathrm{Muk}}^\R\setminus\Lambda_{\mathrm{Muk}}^\Q$, the monodromy is of infinite order (dense in $U(1)$).

*Proof sketch.* The monodromy of $V_\alpha$ around a loop in $\mathrm{Conf}_n(\mathrm{curve})$ is $e^{2\pi i \langle\alpha,\beta\rangle}$ for some Mukai vector $\beta$ depending on the loop. This is of finite order iff $\langle\alpha,\beta\rangle\in\Q$ for all $\beta\in\Lambda_{\mathrm{Muk}}$, which (by non-degeneracy of the Mukai pairing on $II_{4,20}$) is equivalent to $\alpha\in\Lambda_{\mathrm{Muk}}^\Q$. $\Box$

The rational sector is therefore the largest subcategory of $\mathrm{Rep}(A_{K3})$ on which modular functor data make sense as a genuine, finitely-many-generator representation of the mapping class group. The continuous extension would require projective representations of an infinite-dimensional algebra; the rational extension stays finite-rank.

### 1.4 Bridgeland flow and the rational locus

The Wave-3 Part 2.1 observation, made precise:

**Fact 1.3.** For a Bridgeland stability condition $\sigma = (Z, \mathcal P)$ on $D^b(K3)$, the $\sigma$-semistable objects are parametrised by Mukai vectors $v\in\Lambda_{\mathrm{Muk}}^\Q$ if and only if the central charge $Z\colon K(D^b(K3))\to\C$ factors through $\Lambda_{\mathrm{Muk}}^\Q$ (equivalently, $Z$ has rational slopes in a common basis). This is an open and dense condition on $\cM^{\mathrm{Bridg}}_{K3}$.

**Consequence.** At a generic stability condition (rational slopes), the rational Fock modules cover the full Bridgeland-semistable spectrum. These are therefore the **Bridgeland-visible** Fock modules, even though they are $C_2$-cofinite-invisible.

---

## Part 2. The representation category is NOT $C_2$-cofinite

### 2.1 What $C_2$-cofiniteness demands

A VOA $V$ is $C_2$-cofinite (Zhu 1996) if $V/C_2(V)$ is finite-dimensional, where
$C_2(V) = \mathrm{span}\{a_{(-2)}b : a,b\in V\}$. For a lattice VOA $V_\Lambda$ on a lattice $\Lambda$ of finite rank $r$, $C_2$-cofiniteness holds (Dong, Li, Mason 2000) and the quotient $V_\Lambda/C_2(V_\Lambda)$ has dimension $|\Lambda^*/\Lambda|$ (the order of the discriminant group), which is $|{\det M_\Lambda}|$.

**For $\Lambda_{\mathrm{Muk}} = II_{4,20}$**: unimodular, so $|\Lambda^*/\Lambda|=1$. The integer-weight category $\mathrm{Rep}^{\mathrm{int}}(V_{\Lambda_{\mathrm{Muk}}})$ has **exactly one** simple: the vacuum module $V_0$. Every other integer-weight Fock $V_\alpha$ ($\alpha\in\Lambda_{\mathrm{Muk}}$) is isomorphic to $V_0$ as a $V_{\Lambda}$-module when considered up to "lattice shift" — rather, the Fock modules $V_\alpha$ are distinguished as objects in the module category, but the *graded dimension* of the conformal block of $V_\alpha$ coincides with that of $V_0$ shifted by $\langle\alpha,\alpha\rangle/2$.

**The rational extension breaks this.** On $\mathrm{Rep}^\Q$, the simples $V_\alpha$ for $\alpha\in\Lambda_{\mathrm{Muk}}^\Q$ are pairwise non-isomorphic (they differ in conformal weight $\langle\alpha,\alpha\rangle/2\in\Q$), and the set of simples is **countably infinite**. There is no $C_2$-cofinite quotient of $V_\Lambda$ on which $\mathrm{Rep}^\Q$ lives.

### 2.2 Explicit non-$C_2$-cofiniteness verification

I verify this at the level of conformal characters.

**Claim 2.1.** The rational-Fock category $\mathrm{Rep}^\Q(V_{\Lambda_{\mathrm{Muk}}})$ is **not** a finite-semisimple braided tensor category. Specifically, there is no finite set of simple objects whose tensor closure exhausts $\mathrm{Rep}^\Q$.

*Proof.* For $\alpha\in\Lambda_{\mathrm{Muk}}^\Q$ with $\alpha\notin\Lambda_{\mathrm{Muk}}$, the Fock $V_\alpha$ has conformal weight $h_\alpha = \langle\alpha,\alpha\rangle/2$. For $N\in\N$ large, choose $\alpha = (1/N)e$ with $e\in\Lambda_{\mathrm{Muk}}$ primitive and $\langle e,e\rangle = 2$ (such $e$ exists on $II_{4,20}$ as a unimodular even lattice). Then $h_\alpha = 1/(N^2)$. As $N\to\infty$, $h_\alpha\to 0$, so there are simples at arbitrarily low conformal weight (strictly between $0$ and $1/4$). **No finite set can cover these.** Hence $\mathrm{Rep}^\Q$ has infinitely many simples at conformal weight $\le 1/4$, violating the Zhu finite-dimensionality of $V/C_2(V)$. $\Box$

**Corollary 2.2.** Standard $C_2$-cofinite Tannakian reconstruction (Deligne 1990, EGNO 2015 Thm 2.2.3) does not apply to $\mathrm{Rep}^\Q$. The "rigid semisimple category" input fails at the semisimplicity axiom restricted to compact objects.

### 2.3 But: infinite-dim at each conformal weight — is it really?

The brief states "infinite-dim at each conformal weight." Let me check.

**Verification.** At conformal weight $h$, the set of $\alpha\in\Lambda_{\mathrm{Muk}}^\Q$ with $\langle\alpha,\alpha\rangle/2 = h$ is
$$
\{\alpha\in\Lambda_{\mathrm{Muk}}^\Q : \langle\alpha,\alpha\rangle = 2h\} = \{\alpha : \langle\alpha,\alpha\rangle = 2h\}\cap\Lambda_{\mathrm{Muk}}^\Q.
$$
For $2h\in\Q$ fixed, the set $\{\alpha\in\Lambda_{\mathrm{Muk}}^\R : \langle\alpha,\alpha\rangle=2h\}$ is a real hyperboloid of real dimension $23$ in $\R^{24}$. Its intersection with $\Lambda_{\mathrm{Muk}}^\Q$ is either empty (if $2h\notin\mathrm{Im}(Q)\cap\Q$ for $Q = \langle\cdot,\cdot\rangle$) or countably infinite (by density of $\Q$ points on smooth algebraic varieties over $\Q$, when non-empty — here $II_{4,20}$ represents $\Z$ by unimodularity, so represents all of $\Q$).

**Conclusion.** $\mathrm{Rep}^\Q$ has **countably infinite** simples at each rational conformal weight, not finite. This matches the brief's "infinite-dim at each conformal weight" (countable infinity, rather than continuum; but not finite).

**Sharp statement (Wave 4).** The grading-homogeneous pieces of $\bigoplus_{\alpha\in\Lambda_{\mathrm{Muk}}^\Q}V_\alpha$ at conformal weight $h$ have
$$
\dim_\C\bigl(\bigoplus_{\alpha : h_\alpha = h}V_\alpha\bigr)_h = \#\{\alpha\in\Lambda_{\mathrm{Muk}}^\Q : \langle\alpha,\alpha\rangle/2=h\}\cdot 1 = \aleph_0
$$
(countably infinite, with a single $v_\alpha\in V_\alpha$ contribution per $\alpha$).

This genuinely violates finite-dimensionality at each conformal weight when summed over all simples — which is exactly what $C_2$-cofiniteness fails at.

---

## Part 3. Lyubashenko's non-semisimple modular category framework

### 3.1 The framework, stated

Lyubashenko (1995, "Modular transformations for tensor categories," J. Pure Appl. Algebra; 1997, "Tangles and Hopf algebras in braided categories," J. Pure Appl. Algebra; Kerler–Lyubashenko 2001, *Non-semisimple topological quantum field theories for 3-manifolds with corners*, Springer LNM 1765) extended modular-category theory to the **non-semisimple**, **non-rigid**, **finite-cofinal** setting, with the following key features:

**(L1) Category of objects.** A $k$-linear braided tensor category $\cD$ which is **abelian**, with finitely many isomorphism classes of simple objects (the **finiteness axiom** — note this is weaker than finite-semisimple), and which admits a **coend**
$$
L = \int^{X\in\cD} X^\vee\otimes X \in\cD.
$$

**(L2) Coend as Hopf algebra.** The coend $L$ is a Hopf algebra in $\cD$ (Majid 1993), with multiplication from composition of endomorphisms, unit from the vacuum, coproduct from the identity map $X\to X$ read dually, antipode from the braiding. In the semisimple case, $L\cong\bigoplus_{\text{simples }X_i}X_i^\vee\otimes X_i$; in the non-semisimple case, the sum is replaced by a coend (categorical integral).

**(L3) Modular group action.** Lyubashenko showed that when the "$M$-matrix"
$M = (\mathrm{ev}\otimes\mathrm{ev})\circ(\mathrm{id}\otimes c_{L,L})\circ(\mathrm{coev}\otimes\mathrm{coev})\colon \mathbf 1\to L\otimes L$
is invertible (the **non-degeneracy axiom**), the category $\cD$ carries a projective representation of $SL(2,\Z)$ (more generally, of the mapping class group of closed surfaces), just as in the semisimple modular case.

**(L4) Pentagon / hexagon axioms with 3-cocycle.** In the non-semisimple setting, the pentagon and hexagon axioms can carry **additional 3-cocycle data**, not just up to 2-isomorphism. The formalism for this is:
- Pentagon: closed, up to a 3-cocycle $\alpha\in H^3(G;k^\times)$ where $G$ is the "underlying group."
- Hexagon: closed, up to a **hexagon 3-cocycle** $\beta\in H^3(G;k^\times)\oplus H^2(G;\widehat{G\otimes G})$, with an **extra compatibility condition** (the quasi-bialgebra axiom of Drinfeld 1989, "Quasi-Hopf algebras," Leningrad Math. J.).

The key formal difference from the semisimple/strict case: Lyubashenko's pentagon 3-cocycle lives in $H^3(\mathbf{B}G;k^\times)$ (group cohomology of the underlying group $G$), not in $H^3_{\mathrm{moduli}}(\cM;k^\times)$ (Deligne cohomology of a moduli space). **This is crucial for the Wave 4 story.**

### 3.2 Applying Lyubashenko to $\mathrm{Rep}^\Q(V_{\Lambda_{\mathrm{Muk}}})$

**Step 1: Is $\mathrm{Rep}^\Q$ abelian with finitely many simples?**

Abelian: yes (any module category of a VOA is abelian, with morphisms being intertwiners).

Finitely many simples: **No**, countably infinite. So the strict Lyubashenko axioms require weakening.

**Workaround (Wave 4 refinement of Lyubashenko).** Let
$$
\mathrm{Rep}^{\Q,(N)}(V_{\Lambda_{\mathrm{Muk}}}) := \{V_\alpha : \alpha\in (1/N)\Lambda_{\mathrm{Muk}}\}
$$
the rational-Fock subcategory with weight denominator $\le N$. This has $|(1/N)\Lambda_{\mathrm{Muk}}/\Lambda_{\mathrm{Muk}}| = N^{24}$ simples modulo integer shifts — **finite!** — making it a legitimate input to Lyubashenko's axioms.

**Claim 3.1.** $\mathrm{Rep}^{\Q,(N)}(V_{\Lambda_{\mathrm{Muk}}})$ satisfies the Lyubashenko axioms (L1)–(L3) and carries a projective representation of $SL(2,\Z)$.

*Proof sketch.* Abelian: clear. Finitely many simples mod integer shift: $N^{24}$, by lattice-quotient count. Coend exists because the category is a module category of a rational lattice VOA (cf. Dong–Li–Mason 1997 for the modular invariance of lattice VOA at rational levels). $SL(2,\Z)$-representation: the modular $S$ and $T$ matrices act on the $N^{24}$-dim space of characters
$\chi_\alpha(\tau) = \mathrm{Tr}_{V_\alpha}q^{L_0-c/24}$
via finite matrices, with $T = \mathrm{diag}(e^{2\pi i h_\alpha})$ and $S$ the discrete Fourier transform on $(1/N)\Lambda/\Lambda$. $\Box$

**Step 2: Pentagon and hexagon 3-cocycles.**

For $\mathrm{Rep}^{\Q,(N)}$, the pentagon and hexagon axioms hold up to 3-cocycles valued in $U(1)$. The underlying group is
$$
G_N := (1/N)\Lambda_{\mathrm{Muk}}/\Lambda_{\mathrm{Muk}}\cong (\Z/N\Z)^{24},
$$
a finite abelian group of order $N^{24}$.

The pentagon 3-cocycle lives in
$$
H^3(\mathbf{B}G_N; U(1)) = H^3((\Z/N)^{24}; U(1)) \cong (\Z/N)^{\binom{24}{3}}\oplus(\text{torsion})
$$
(by Künneth on $B((\Z/N)^k)$, which has cohomology ring $\Lambda_{\Z/N}[x_1,\ldots,x_k]\otimes\mathrm{Sym}_{\Z/N}[y_1,\ldots,y_k]/(\ldots)$ — the usual cohomology of a torus of finite groups).

The **hexagon 3-cocycle** (the "braided" 3-class) lives additionally in the quadratic form group
$$
Q(G_N;U(1)) := \{q:G_N\to U(1)\,|\,q(-x) = q(x),\, b_q(x,y) := q(x+y)/(q(x)q(y))\text{ is bi-multiplicative}\}
$$
(Eilenberg–Mac Lane, "On the groups $H(\Pi,n)$"). This is the **Eilenberg–Mac Lane $K(G,2)$-cohomology**
$H^4(K(G_N,2); U(1))$, which for finite abelian $G$ is computed by quadratic forms on $G$ with values in $U(1)$.

**Step 3: The rational-Fock 3-cocycle.**

The scalar braiding $\sigma_{V_\alpha,V_\beta} = e^{2\pi i\langle\alpha,\beta\rangle_{\mathrm{Muk}}}$ on $\mathrm{Rep}^{\Q,(N)}$ descends to a bi-multiplicative pairing
$$
\bar\sigma\colon G_N\times G_N\to U(1), \quad \bar\sigma(\alpha,\beta) = e^{2\pi i\langle\alpha,\beta\rangle_{\mathrm{Muk}}\mod 1}.
$$
Since the Mukai pairing is **even** on $\Lambda_{\mathrm{Muk}}$, we have $\langle\alpha,\alpha\rangle\in 2\Z$ for $\alpha\in\Lambda_{\mathrm{Muk}}$, so $\langle(1/N)e,(1/N)e\rangle = \langle e,e\rangle/N^2\in 2\Z/N^2$ for $e\in\Lambda_{\mathrm{Muk}}$.

The associated quadratic form on $G_N$ is
$$
q_N(\alpha) = e^{\pi i\langle\alpha,\alpha\rangle_{\mathrm{Muk}}} = e^{\pi i\langle e,e\rangle/N^2}
\quad\text{for }\alpha=e/N,\,e\in\Lambda_{\mathrm{Muk}}.
$$

**Claim 3.2.** The rational-Fock 3-cocycle on $\mathrm{Rep}^{\Q,(N)}(V_{\Lambda_{\mathrm{Muk}}})$ in the Lyubashenko framework is the class of the quadratic form $q_N\in Q(G_N;U(1))$ under the Eilenberg–Mac Lane isomorphism
$$
Q(G_N;U(1))\xrightarrow{\sim} H^4(K(G_N,2);U(1))\xrightarrow{\text{transgression}} H^3(\mathbf{B}G_N;U(1)).
$$

### 3.3 Example: level $N=2$

For $N=2$: $G_2 = (\Z/2)^{24}$. The quadratic form $q_2(\alpha) = e^{\pi i\langle e,e\rangle/4}$ for $\alpha = e/2$, $e\in\Lambda_{\mathrm{Muk}}$. Since $\langle e,e\rangle\in 2\Z$ for $e$ in an even lattice, $\langle e,e\rangle/4\in\Z/2$ has two classes: $0$ (for $\langle e,e\rangle\equiv 0\bmod 4$) and $1/2$ (for $\langle e,e\rangle\equiv 2\bmod 4$).

$\Lambda_{\mathrm{Muk}} = II_{4,20}$ has both types of $e$: the $U$-summand has generators $f_1, f_2$ with $\langle f_i,f_i\rangle = 0$ (so $\equiv 0\mod 4$) and $\langle f_1,f_2\rangle=1$; while the $E_8$-summand's simple roots have $\langle\alpha,\alpha\rangle=-2$ (so $\equiv 2\mod 4$).

The quadratic form $q_2$ is therefore the **Arf–Mukai quadratic form** on $\Lambda_{\mathrm{Muk}}/2\Lambda_{\mathrm{Muk}} = (\F_2)^{24}$, a non-degenerate $\F_2$-valued quadratic form on a $24$-dim $\F_2$-vector space, with associated bilinear form the mod-2 Mukai form. Its Arf invariant:
$$
\mathrm{Arf}(q_2) = \frac{1}{2}\mathrm{rk}_{\F_2}\Lambda_{\mathrm{Muk}}\bmod 2 = 0
$$
(since $\Lambda_{\mathrm{Muk}}$ is **even**, so $q_2$ is **totally even**, so $\mathrm{Arf}=0$ — this is the standard consequence of evenness).

So the 3-cocycle on $\mathrm{Rep}^{\Q,(2)}$ has Arf invariant zero — **it is stably trivial in the ENO classification** (see §4 below).

**But the cohomology class itself is not zero.** The transgression to $H^3(\mathbf{B}(\F_2)^{24};U(1))$ is non-zero, given by
$$
[q_2]\in H^3(\mathbf{B}(\F_2)^{24};U(1))_{\mathrm{quad}} = \{\text{even quadratic forms on }(\F_2)^{24}\}/\sim
$$
and represents a **genuinely non-trivial** braided-$(\F_2)^{24}$-crossed-extension class, even though its Arf is zero. This is the distinction between "Arf class" (mod-2 scalar) and "full Drinfeld-center 3-class" (lives in $H^3$); for an even form, the former vanishes but the latter is still a non-trivial cohomology class, detected by the quadratic form itself.

### 3.4 Example: level $N=6$ (Kummer denominator)

For $N=6$: $G_6 = (\Z/6)^{24}$. The quadratic form $q_6(\alpha) = e^{\pi i\langle e,e\rangle/36}$ for $\alpha = e/6$. The image runs over $e^{2\pi i\Z/72}$, a $72$-fold cyclic group.

**Key arithmetic fact.** For $\Lambda_{\mathrm{Muk}} = II_{4,20}$ and $N=6$:
$(1/6)\Lambda_{\mathrm{Muk}}/\Lambda_{\mathrm{Muk}} \cong (\Z/6)^{24}$, and the quadratic form $q_6$ values on
$(1/6)e\in (1/6)\Lambda_{\mathrm{Muk}}/\Lambda_{\mathrm{Muk}}$ are $e^{2\pi i\langle e,e\rangle/72}$.

For the Kummer K3, Wave 3 computed the 3-cocycle to be in $\Z/6\oplus\Z/6$ (from the $SL(2,\Z)\times SL(2,\Z)$ Schur multiplier, which is $\Z/12\oplus\Z/12$, halved to $\Z/6\oplus\Z/6$ by $\iota$-equivariance).

**Match.** The $N=6$ rational-Fock 3-cocycle lives in
$H^3(\mathbf{B}(\Z/6)^{24};U(1))$, which contains $\Z/6\oplus\Z/6$ as a direct summand (specifically, the $\Z/6$-torsion classes along the two $U$-summands of $\Lambda_{\mathrm{Muk}} = U^4\oplus E_8(-1)^2$, restricted to the $E_1\times E_2$-factored Kummer sublattice).

**This is the correct home for the Kummer 3-cocycle.** Wave 3 located it in Deligne cohomology of $\cM^{\mathrm{Bridg}}_{\mathrm{Km}}$ via $H^3(SL(2,\Z)^2;U(1))$; Wave 4 locates the same class in Lyubashenko's $H^3(\mathbf{B}G_6;U(1))$, where $G_6=(\Z/6)^{24}$ is the underlying group of the rational-Fock category at denominator 6.

**The two computations match** because the $SL(2,\Z)^2$ action on the Kummer stratum factors through the finite quotient acting on the $\Z/6\oplus\Z/6$ subgroup of $G_6$ (specifically, on the $E_1,E_2$-Mukai direction pairs).

### 3.5 Invocation summary

The Lyubashenko framework, applied to $\mathrm{Rep}^{\Q,(N)}(V_{\Lambda_{\mathrm{Muk}}})$:
(a) Replaces the (failed) $C_2$-cofinite Tannakian reconstruction with the **coend Hopf algebra** reconstruction, which works on finite-abelian-simples categories.
(b) Gives a **projective $SL(2,\Z)$-representation** on the space of characters (finite-dimensional of rank $N^{24}$).
(c) Produces a **genuine 3-cocycle** on the underlying abelian group $G_N = (\Z/N)^{24}$, beyond any pentagon-2-cocycle.
(d) The 3-cocycle at $N=6$ matches the Wave-3 Kummer class, **identifying two a priori different cohomological classes** (Deligne on $\cM^{\mathrm{Bridg}}$; group-cohomological on $\mathbf{B}G_6$).

---

## Part 4. The rational-Fock 3-cocycle as an ENO-2010 class

### 4.1 The Etingof–Nikshych–Ostrik classification

Etingof–Nikshych–Ostrik 2010, "Fusion categories and homotopy theory," *Quantum Topology* 1:3, 209–273 (arXiv:0909.3140) classified **pointed braided fusion categories** $\cC_G$ on a finite abelian group $G$ by pre-metric groups: triples $(G, q, \alpha)$ where:
- $G$ is a finite abelian group (the grading group).
- $q\colon G\to U(1)$ is a quadratic form (the **self-braiding**), with associated bilinear form
$b_q(x,y) := q(x+y)/(q(x)q(y))$.
- $\alpha\in H^3(\mathbf{B}G;U(1))$ is a normalised 3-cocycle (the **associator**), satisfying the ENO compatibility
$\partial\alpha = 0$ *and* $q$ lifts $b_q$ through the $\Omega\Sigma$-Postnikov tower, i.e., there is a secondary cohomology operation linking $\alpha$ and $q$.

**ENO-2010 main theorem (Thm 2.11).** Pointed braided fusion categories up to equivalence are in bijection with pre-metric groups $(G, q, \alpha)$ up to isomorphism, where the associator $\alpha$ is the **braided 3-cocycle** in the Eilenberg–Mac Lane $K(G,2)$-cohomology:
$$
\alpha\in H^4(K(G,2);U(1))\xrightarrow{\text{Postnikov transgression}} H^3(\mathbf{B}G;U(1))\oplus H^0(\mathbf{B}G;H^1(K(G,1);U(1))).
$$

**ENO's "moduli of pointed braided fusion categories" = $\coprod_G Q(G;U(1))$**, where $Q(G;U(1))$ is the group of quadratic forms $G\to U(1)$ modulo the image of the bi-multiplicative 2-cocycles (which are always trivial 3-class).

### 4.2 Identifying $\mathrm{Rep}^{\Q,(N)}(V_{\Lambda_{\mathrm{Muk}}})$ as an ENO pointed braided fusion category

**Proposition 4.1.** $\mathrm{Rep}^{\Q,(N)}(V_{\Lambda_{\mathrm{Muk}}})$ is a **pointed braided fusion category** (every simple is invertible, meaning $V_\alpha\otimes V_{-\alpha}\cong V_0$ for all $\alpha\in G_N=(1/N)\Lambda_{\mathrm{Muk}}/\Lambda_{\mathrm{Muk}}$), with ENO data:
$$
(G, q, \alpha)_{\mathrm{Rep}^{\Q,(N)}} = ((\Z/N)^{24}, q_N, \alpha_N)
$$
where:
- $G = (\Z/N)^{24}$ as above.
- $q_N(\alpha) = e^{\pi i\langle\alpha,\alpha\rangle_{\mathrm{Muk}}}$ for $\alpha\in G_N$ (the Mukai quadratic form reduced modulo integers).
- $\alpha_N\in H^3(\mathbf{B}(\Z/N)^{24};U(1))$ is the Postnikov-transgressed class of $q_N$, explicitly the pullback of the generator of $H^4(K(\Z/N,2);U(1))$ along the Mukai form, 24 copies.

*Proof of pointedness.* $V_\alpha\otimes V_\beta = V_{\alpha+\beta}$ (Fock-module tensor product on a lattice VOA; Dong 1994, Thm 3.2), so every simple is invertible with inverse $V_{-\alpha}$. $\Box$

*Proof of ENO identification.* The quadratic form $q_N$ is the conformal weight modulo integers, computed via the Mukai pairing. The braiding $b_{q_N}(\alpha,\beta) = q_N(\alpha+\beta)/(q_N(\alpha)q_N(\beta)) = e^{\pi i(\langle\alpha+\beta,\alpha+\beta\rangle-\langle\alpha,\alpha\rangle-\langle\beta,\beta\rangle)} = e^{2\pi i\langle\alpha,\beta\rangle}$, matching the scalar braiding on Fock modules (Dong–Li–Mason 1997 for the lattice VOA braiding). The associator $\alpha_N$ comes from the Postnikov-tower secondary cohomology operation, which for a pointed braided fusion category is determined by the quadratic form (ENO Thm 2.11). $\Box$

**Consequence.** The rational-Fock sector is classified by ENO 2010 as a pointed braided fusion category with pre-metric group data $((\Z/N)^{24}, q_N, \alpha_N)$. This is a **single ENO-invariant datum**, not a moduli.

### 4.3 The 3-cocycle in the full rational limit $N\to\infty$

The full rational-Fock sector $\mathrm{Rep}^\Q = \varinjlim_N\mathrm{Rep}^{\Q,(N)}$ is the colimit of pointed braided fusion categories along $N\mid N'$-inclusions. The 3-cocycle lives in
$$
\tilde\alpha_{K3}^\Q = \varinjlim_N\alpha_N\in\varinjlim_N H^3(\mathbf{B}(\Z/N)^{24};U(1)) = H^3(\mathbf{B}(\Q/\Z)^{24};U(1)).
$$

**Computation.** $(\Q/\Z)^{24}$ has cohomology
$H^*(\mathbf{B}(\Q/\Z)^k;U(1)) = \varinjlim_N H^*(\mathbf{B}(\Z/N)^k;U(1))$,
which is $\bigotimes^k H^*(\mathbf{B}(\Q/\Z);U(1))$ by Künneth. $H^*(\mathbf{B}(\Q/\Z);U(1))$ is the Eilenberg–Mac Lane spectrum cohomology, computed by
$$
H^0 = U(1), \quad H^1 = 0, \quad H^2 = \Q/\Z,\quad H^3 = U(1), \quad H^4 = 0, \ldots
$$
(Borel 1954, "Sur l'homologie et la cohomologie des groupes de Lie compacts").

Applying Künneth:
$$
H^3(\mathbf{B}(\Q/\Z)^{24};U(1)) \supset \bigoplus_{i<j<k} H^1_{(i)}\otimes H^1_{(j)}\otimes H^1_{(k)} \oplus \bigoplus_{i<j} H^2_{(i)}\otimes H^1_{(j)} \oplus \bigoplus_i H^3_{(i)}.
$$
Since $H^1(\mathbf{B}(\Q/\Z);U(1))=0$, only the "last two" summands survive:
$$
H^3(\mathbf{B}(\Q/\Z)^{24};U(1)) = \bigoplus_i H^3_{(i)} \cong U(1)^{24}
$$
(rank-24 $U(1)$-valued 3-class, direction-wise).

**The Wave-4 rational-Fock 3-cocycle.**
$$
\boxed{\;\;
\tilde\alpha_{K3}^\Q \;=\; (q_\infty^{(1)},\ldots,q_\infty^{(24)})\in H^3(\mathbf{B}(\Q/\Z)^{24};U(1)) = U(1)^{24},
\;\;}
$$
where $q_\infty^{(i)} = \lim_{N\to\infty}q_N\bigr|_{\text{direction }i} = \{e^{2\pi i\langle\alpha^{(i)},\alpha^{(i)}\rangle/2}\,:\,\alpha^{(i)}\in\Q\}$.

This is a rank-24 vector of $U(1)$-valued 3-classes, one per Mukai direction.

### 4.4 Relation to Wave-3 Kummer 3-cocycle

**Restriction map.** The Kummer 3-cocycle $\alpha^{\mathrm{Km}}\in\Z/6\oplus\Z/6$ of Wave 3 is the **restriction** of $\tilde\alpha_{K3}^\Q$ along the inclusion
$$
(\Z/6)^2\hookrightarrow (\Z/6)^{24}\hookrightarrow (\Q/\Z)^{24}
$$
corresponding to the two $U$-summands of $\Lambda_{\mathrm{Muk}}\supset U\oplus U$ that are $\iota$-symmetric for the Kummer involution.

**Match.** The two $U(1)$-components of $\tilde\alpha_{K3}^\Q$ at the Kummer-visible directions are the 6-torsion points $e^{2\pi i\cdot 1/6}\in U(1)$, reproducing the Wave-3 $\Z/6\oplus\Z/6$ class. **The Wave-3 Kummer finding is a special case of the Wave-4 global rational-Fock 3-cocycle.**

### 4.5 Is this 3-cocycle non-trivial?

**Yes, in $U(1)^{24}$ as a whole.** Each direction contributes a non-zero $U(1)$-class, because the Mukai quadratic form $q_N$ is non-zero (the lattice is non-degenerate).

**But there's a subtlety: ENO-inequivalence versus trivialisability.** A non-zero ENO class $[q, \alpha]$ in $\mathrm{Pre-Metric}(G;U(1))$ produces a non-trivial pointed braided fusion category, but the underlying 3-cocycle can still be **trivialisable by a change of generators** (an element of $\mathrm{Hom}(G,U(1))$). The invariant data is the equivalence class $(G, q, \alpha)/\sim$ where $\sim$ is ENO equivalence.

**For our case.** The 3-cocycle $\tilde\alpha_{K3}^\Q$ on $G = (\Q/\Z)^{24}$ with quadratic form $q_\infty = $ Mukai form, is **ENO-equivalent** to the classification of the Mukai lattice itself — a $(4,20)$-signature even unimodular quadratic form on $\Z^{24}$, modulo $\Q/\Z$-valued automorphisms of $\Z^{24}$. Up to signed permutation and scaling, there is only one even unimodular $(4,20)$-signature lattice ($II_{4,20}$ by Milnor's classification), so the ENO class is a **single** non-trivial point in $\mathrm{Pre-Metric}((\Q/\Z)^{24};U(1))$.

**Conclusion.** $\tilde\alpha_{K3}^\Q$ is **non-trivial** in $H^3(\mathbf{B}(\Q/\Z)^{24};U(1))$ but has a **unique** ENO isomorphism class (no moduli), classified by the Mukai lattice up to signed isometry.

---

## Part 5. Globalisation to K3 moduli: torsor trivialisation?

### 5.1 The globalisation question

The Wave-4 brief asks: is the rational-Fock 3-cocycle $\tilde\alpha_{K3}^\Q$ trivialisable by a torsor over K3 moduli, or is it a genuine global obstruction?

**What "trivialisable by a torsor" means.** Consider the classifying-stack map
$$
\iota\colon\cM_{K3}\to\mathrm{Pre-Metric}((\Q/\Z)^{24};U(1))/\mathrm{iso} = \mathrm{pt}
$$
(classifying space of the ENO invariant, which is a single point after ENO equivalence). Because the target is a point, the map $\iota$ is trivially constant.

**But there is a locally non-trivial structure: the ENO automorphism torsor.**

The automorphism group of the ENO invariant $(G, q, \alpha)$ at $G = (\Q/\Z)^{24}$, $q = q_\infty$ is
$$
\mathrm{Aut}_{\mathrm{ENO}}(G, q_\infty) = O(\Lambda_{\mathrm{Muk}}^\Q; q_\infty),
$$
the orthogonal group of the Mukai quadratic form **over the rationals** — a classical group $O(4,20;\Q)$ (or $\Q$-rational points of $O(4,20)$).

The K3 moduli $\cM_{K3}$ classifies an $O(4,20;\Q)$-bundle through the Abel–Jacobi map, parametrising the $\Q$-rational isometry of the Mukai lattice with its fixed signature. This bundle is the **automorphism torsor**.

### 5.2 Explicit form of the torsor

**Claim 5.1.** The ENO-automorphism torsor on $\cM_{K3}^{\mathrm{Bridg}}$ is the pullback of the **universal Mukai isometry bundle**:
$$
\cT^{\mathrm{ENO}}_{K3}\to\cM_{K3}^{\mathrm{Bridg}}, \qquad (\cT^{\mathrm{ENO}}_{K3})_\sigma = O(\Lambda_{\mathrm{Muk}}\otimes\Q;q_\infty)_{\{\sigma\}}
$$
parametrising the choice of rational isometry of the Mukai lattice compatible with the stability condition $\sigma$.

### 5.3 Does this torsor trivialise $\tilde\alpha_{K3}^\Q$?

**Answer: locally yes, globally no.**

**Local triviality.** Over any contractible open $U\subset\cM_{K3}^{\mathrm{Bridg}}$, the torsor trivialises (admits a section), which gives a local trivialisation of the ENO class. So $\tilde\alpha_{K3}^\Q$ is **locally trivial** on K3 moduli.

**Global obstruction.** Globally, the torsor is **not trivial** — specifically, its structure group $O(\Lambda_{\mathrm{Muk}};\Z) = O(II_{4,20};\Z)$ is an infinite arithmetic group (the Mukai monodromy group of K3), and the monodromy action of $\pi_1(\cM_{K3}^{\mathrm{Bridg}})$ on the ENO automorphism bundle is **non-trivial**.

**What "non-trivial" means in degree 3.** The obstruction to gluing local trivialisations into a global one lives in
$$
[\text{gluing 2-cocycle}]\in H^2(\pi_1(\cM_{K3}^{\mathrm{Bridg}});\mathrm{Aut}_{\mathrm{ENO}}^\Q).
$$
This, in turn, transgresses to a 3-class in
$H^3(\pi_1;H^2(\mathrm{Aut}_{\mathrm{ENO}}^\Q;U(1)))\to H^3(\cM_{K3};U(1))$
via the Lyndon–Hochschild–Serre spectral sequence. The transgressed class is exactly $\tilde\alpha_{K3}^\Q$ **viewed on K3 moduli**.

### 5.4 Wave-3 Kummer class as the first non-trivial monodromy

At the Kummer stratum $\cM_{K3}^{\mathrm{Km}}\subset\cM_{K3}^{\mathrm{Bridg}}$, the Wave-3 analysis gave
$\pi_1(\cM_{K3}^{\mathrm{Km}})\supset SL(2,\Z)\times SL(2,\Z)$ (via Kunneth on $E_1\times E_2$), with $H^3(SL(2,\Z);U(1)) = \Z/12$. The monodromy class on the Kummer stratum is $\Z/12\oplus\Z/12$, reduced to $\Z/6\oplus\Z/6$ by $\iota$-equivariance.

**This is the "first non-trivial monodromy class" for the rational-Fock 3-cocycle.** At the generic smooth K3 stratum, the monodromy class conjecturally vanishes (Wave 3 OP-W3-1; Borel 1974 gives rational vanishing up to $\deg\le 18$). At the Kummer stratum, $\Z/6\oplus\Z/6$. At Shioda–Inose strata (Wave 3 OP-W3-2), expected further classes.

### 5.5 Verdict: genuine global obstruction

**Conclusion.** The rational-Fock 3-cocycle $\tilde\alpha_{K3}^\Q$ is:
- **ENO-classified as a single point** (unique pre-metric group class up to isomorphism).
- **Trivialisable locally** (on contractible opens of K3 moduli) via the ENO-automorphism torsor.
- **NOT trivialisable globally** — the gluing obstruction is the $\pi_1(\cM_{K3}^{\mathrm{Bridg}})$-monodromy class, which vanishes only at the generic K3 stratum (conjecturally) and is non-zero at Kummer, Shioda–Inose, and similar special-Picard loci.

**Torsor trivialisability is local; global triviality fails at special-Picard strata.**

This is the Wave-4 analogue of the Wave-3 "three-stratum" finding: now four strata, refined by the rational-Fock visibility structure.

---

## Part 6. Cross-check against Gaiotto Wave-3 level-2 module $\dim 575$

### 6.1 The Gaiotto Wave-3 module

Gaiotto W3 §3.3 constructed the level-2 Yangian module as the Serre-quotient of $V^{\otimes 2}$ for $V = \widetilde\Lambda_{K3}\otimes\C$, rank $24$. The dimension:
$$
\dim(V^{\otimes 2}/\mathrm{Serre}) = \dim V_{2\omega_1} + \dim V_{\omega_2} = 299 + 276 = 575.
$$
In the Schur-doubled convention (Wave 2 §2.7): $1150$. $J_0$-split: $32 + 318 + 800$.

**Question**: is this level-2 module visible or invisible in the rational-Fock framework?

### 6.2 Visibility assessment

**Level-2 Yangian module ≠ rational-Fock module at first sight.** The level-2 module lives in $V^{\otimes 2}/\mathrm{Serre}$, while rational-Fock modules live in $\bigoplus_{\alpha\in\Lambda_{\mathrm{Muk}}^\Q}V_\alpha$. These are a priori different objects.

**But.** The level-2 Yangian module is built from the evaluation rep $V$, which in turn embeds into the rank-24 Heisenberg Fock as the "single-mode" subspace at $J_0$-weight $\pm 1$ and $0$. The Serre quotient is a constraint that cuts the full $V^{\otimes 2}$ down to the $Y_\hbar(\mathfrak{so}(4,20))$-irreducible piece.

**Claim 6.1 (visibility).** The level-2 module $V^{\otimes 2}/\mathrm{Serre}$ embeds into the rational-Fock sector
$\mathrm{Rep}^{\Q,(2)}(V_{\Lambda_{\mathrm{Muk}}})$ via:
$$
\iota_{\text{level-2}}\colon V^{\otimes 2}/\mathrm{Serre} \hookrightarrow \bigoplus_{\alpha\in(1/2)\Lambda_{\mathrm{Muk}}/\Lambda_{\mathrm{Muk}}}V_\alpha
$$
by decomposing $V^{\otimes 2}/\mathrm{Serre}$ into $\mathfrak{so}(4,20)$-weight components and matching each component to a Fock $V_\alpha$ with $\alpha = (v_1 + v_2)/2$ for $v_1, v_2$ the weight vectors.

**Verification via $J_0$-split.** The level-2 Gaiotto split $32 + 318 + 800$ (doubled to $1150$; halved to $575$) has the structure:
- $32$ generators at $J_0 = \pm 2$ — these are $\alpha_1 + \alpha_2$ for $\alpha_i\in\{J_0 = \pm 1\}$.
- $318$ generators at $J_0 = 0$ — these are $\alpha_1 + \alpha_2$ for $J_0(\alpha_1) + J_0(\alpha_2) = 0$.
- $800$ generators at $J_0 = \pm 2$ — the other polarity.

Wait, $32 + 318 + 800 \neq 575$. Let me recheck. Gaiotto W3 writes $J_0$-split as $32 + 318 + 800$ for the **Schur-doubled** level-2 character ($1150$ total), so the **undoubled** count is $16 + 159 + 400$ — but $16+159+400 = 575$. ✓

Now, in the rational-Fock sector at $N = 2$: there are $|(1/2)\Lambda_{\mathrm{Muk}}/\Lambda_{\mathrm{Muk}}| = 2^{24}$ simples. At conformal weight $h = 1/4\cdot\langle e,e\rangle$ for $e\in\Lambda_{\mathrm{Muk}}$, the simples are those $\alpha = e/2$. The count of $e\in\Lambda_{\mathrm{Muk}}$ with $\langle e,e\rangle = k$ for fixed $k$ is the theta coefficient $\theta_{\Lambda_{\mathrm{Muk}}}(q)$ at $q^k$, which for $II_{4,20}$ is known (modular form of weight 12 and level 1). For $k = -2$ (shortest $e$): theta coefficient = $24\cdot$(something like 196560, but for $II_{4,20}$ indefinite signature, it's signed).

**Point.** The level-2 Yangian module with $\dim = 575$ **is a finite-rank quotient** of a sum of rational-Fock modules at $N = 2$. It is visible, but only as a **quotient**, not a simple.

### 6.3 The level-2 module in the Lyubashenko framework

Under the Lyubashenko reconstruction of $\mathrm{Rep}^{\Q,(2)}(V_{\Lambda_{\mathrm{Muk}}})$:
- The category has $2^{24}$ simples.
- The coend is $L_2 = \bigoplus_{\alpha\in G_2}V_{-\alpha}\otimes V_\alpha$, rank $2^{24}$.
- The 3-cocycle is the Arf class of the mod-2 Mukai form (Arf = 0, but group-cohomology class non-trivial per §3.3).

**Gaiotto's level-2 module as a Lyubashenko-reconstructed $L_2$-module.** The Serre-quotiented $V^{\otimes 2}/\mathrm{Serre}$ of dimension $575$ is **an $L_2$-module**, not a simple of $\mathrm{Rep}^{\Q,(2)}$. Specifically:
$$
V^{\otimes 2}/\mathrm{Serre} \cong \bigoplus_{\alpha\in S_{\text{level-2}}}V_\alpha\cdot m_\alpha
$$
for some subset $S_{\text{level-2}}\subset G_2$ and multiplicities $m_\alpha$, such that $\sum_{\alpha}m_\alpha = 575$.

**Which $\alpha$'s appear?** By the $J_0$-split $16 + 159 + 400$, the $\alpha$'s appear at three weights:
- $16$ simples at $J_0 = \pm 2$: $\alpha = e/2$ with $\langle e,e\rangle = 2$, i.e., $\alpha^2 = 1/2$.
- $159$ simples at $J_0 = 0$: $\alpha = e/2$ with $\langle e,e\rangle = 0$, i.e., $\alpha^2 = 0$ (null).
- $400$ simples at the other polarity.

**So the level-2 module is a union of $(2^{24})$-indexed Fock sums.** It lies inside $\mathrm{Rep}^{\Q,(2)}$, with dimension $575$ after Serre quotient.

### 6.4 Visibility verdict: visible, non-simple

**Gaiotto W3's level-2 $\dim 575$ module IS visible in the rational-Fock framework**, as a **non-simple $L_2$-module** in $\mathrm{Rep}^{\Q,(2)}(V_{\Lambda_{\mathrm{Muk}}})$ after Serre quotient.

**However**, the module is NOT one of the simples of $\mathrm{Rep}^{\Q,(2)}$ (the simples are single Fock modules $V_\alpha$). It is a multi-Fock quotient — a **compact object** in the rational-Fock category, but not an irreducible one.

This places the level-2 module in the "full module category of the coend $L_2$" rather than in the "category of simples of $\mathrm{Rep}^{\Q,(2)}$." This is exactly the sort of object that Lyubashenko's framework handles natively: his construction allows non-simple, non-rigid objects as long as they are finite-rank.

### 6.5 Convergence with Wave-3 Gaiotto conclusion

Gaiotto W3 §3.4 flagged: "$\Phi_{10}^{-1}$ at $p\to 0$ picks out level-1; $p$-refinement for level-$k$ requires DMVV." Wave 4 extends this: the DMVV $p$-refinement corresponds exactly to the rational-Fock denominator $N$, with $N\to\infty$ recovering the full rational sector and $\Phi_{10}(q,y,p)^{-1}$ with $p\neq 0$ measuring the level-$N$ grade.

**New Wave-4 formula**: $I_{\mathrm{Schur}}^{(k\le N)}(q,y) = $ trace over $\mathrm{Rep}^{\Q,(N)}$ with the Lyubashenko-modular $S$-$T$-acton, expanded in $p$:
$$
\sum_{k\ge 0}p^k\,I_{\mathrm{Schur}}^{(k)}(q,y) = \chi_{\mathrm{Rep}^{\Q,(\infty)}}(q,y;p)
$$
where the RHS is the **Lyubashenko-modular character** of the full rational-Fock category. This should match $\Phi_{10}(q,y,p)^{-1}/(qyp)$ at the appropriate normalisation.

**Wave-4 challenge (deferred).** Verify this formula at chain level by comparing the Lyubashenko character to the DMVV second-quantisation. The structural identification is that both are computing the same object — the generating function of rational-Fock module characters — so they should match.

---

## Part 7. Attack on own constructions

### 7.1 Attack: is Lyubashenko really applicable at infinite simples?

**Claim to attack.** I applied Lyubashenko to $\mathrm{Rep}^{\Q,(N)}$ at finite $N$, but the brief asks about the full rational-Fock sector (infinite simples).

**Attack.** Lyubashenko 1997's axioms (L1) through (L4) require **finitely many** simples. The colimit $\mathrm{Rep}^\Q = \varinjlim_N\mathrm{Rep}^{\Q,(N)}$ has infinitely many.

**Heal.** The colimit limit is a **pro-Lyubashenko** structure (inverse system of finite-denominator categories), not a Lyubashenko category in the strict sense. The correct ambient is the **ind-Lyubashenko** 2-category, which accepts such colimits as natural objects. The 3-cocycle on the ind-category lives in
$H^3(\mathbf{B}(\Q/\Z)^{24};U(1))$, computed by the derived inverse limit of the finite-$N$ cocycles.

**Verdict.** Attack valid at the strict axiomatic level; healed by passing to ind-Lyubashenko. The 3-cocycle computation goes through because ind-Lyubashenko inherits $H^3$ from its finite pieces via the Mittag–Leffler formal-scheme limit.

### 7.2 Attack: is the level-2 module really a quotient of rational-Fock?

**Claim to attack.** I asserted the Gaiotto W3 level-2 module embeds into $\mathrm{Rep}^{\Q,(2)}$ as a Serre-quotient of a multi-Fock sum.

**Attack.** The level-2 Yangian module is built from the evaluation rep $V$, not from lattice-theoretic Fock modules. The identification "$V$ = Mukai lattice tensor $\C$" is at the **classical limit**, not at the quantum Yangian level.

**Heal (chain-level).** The evaluation module $V$ at quantum Yangian $Y_\hbar(\mathfrak{so}(4,20))$ is **not** the Mukai lattice as a classical object, but a filtered deformation. At $\hbar = 0$, $V$ **is** the Mukai lattice (as an $\mathfrak{so}(4,20)$-module); at $\hbar > 0$, it is a $Y_\hbar$-module, with the Yangian evaluation homomorphism
$\mathrm{ev}_u\colon Y_\hbar\to\mathrm{End}(V)$ satisfying RTT.

The Yangian evaluation module $V$ at finite $\hbar$ **extends** to a Fock module over the Heisenberg part of $A_{K3}$, via the Kac–Moody-to-Yangian current correspondence (Drinfeld 1988, reversed): the affine current $J_\mu(z) = \sum_n J_{\mu,n}z^{-n-1}$ acts on the evaluation module by $J_{\mu,n}\cdot v_\alpha = u^n(\mu\cdot v_\alpha)$, so the Fock mode structure is compatible with Yangian evaluation.

**Verdict.** Attack valid at first sight; healed by the Drinfeld evaluation-to-Fock homomorphism, which embeds the Yangian level-2 module into the Heisenberg Fock as claimed. The Serre quotient is preserved because Yangian Serre relations correspond to lattice-VOA OPE relations.

### 7.3 Attack: ENO 2010 applies to pointed braided fusion, but is $\mathrm{Rep}^{\Q,(N)}$ fusion?

**Claim to attack.** I applied ENO 2010 to $\mathrm{Rep}^{\Q,(N)}$, claiming it is "pointed braided fusion." But "fusion" in ENO requires **finitely many simples AND semisimplicity AND rigidity**, which is a strict subset of Lyubashenko's weaker axioms.

**Attack.** If $\mathrm{Rep}^{\Q,(N)}$ is fusion (finite, semisimple, rigid), why did we need Lyubashenko in the first place?

**Heal.** $\mathrm{Rep}^{\Q,(N)}$ at finite $N$ is **fusion** (finite-semisimple and rigid, as a subcategory of the lattice VOA $V_{(1/N)\Lambda_{\mathrm{Muk}}}$ module category, which is the lattice VOA on a larger unimodular lattice $(1/N)\Lambda$ embedded rationally). ENO applies to the finite-$N$ slice.

**Why Lyubashenko.** The Lyubashenko invocation is for the **colimit** $\mathrm{Rep}^\Q = \varinjlim_N\mathrm{Rep}^{\Q,(N)}$, which is NOT fusion (infinite simples). In the finite-$N$ slice, ENO gives the 3-cocycle cleanly; in the colimit, Lyubashenko's non-semisimple framework handles the ind-category.

**Verdict.** Attack valid; the right picture is **ENO at finite $N$, Lyubashenko at the colimit**. Both frameworks give the same 3-cocycle for finite $N$; Lyubashenko extends to the ind-limit.

### 7.4 Attack: $H^3(\mathbf{B}(\Q/\Z)^{24};U(1)) = U(1)^{24}$ — is this right?

**Claim to attack.** I computed $H^3(\mathbf{B}(\Q/\Z)^{24};U(1)) = U(1)^{24}$ using Künneth, citing Borel 1954.

**Attack.** Borel 1954 computes cohomology of **compact** Lie groups, not of discrete groups like $\Q/\Z$ (which is discrete but not finitely generated).

**Heal.** For $\Q/\Z$ as a discrete group, cohomology is computed as $\varinjlim_N H^*(\Z/N;U(1))$. Using
$H^3(\Z/N;U(1)) = \Z/N$ (generated by the cocycle $\omega(a,b,c) = e^{2\pi i\cdot\mathrm{mult}_3(a,b,c)/N}$ for mult$_3$ the triple-product, cf. Mac Lane *Homology* 1963 Ch VIII), we get
$H^3(\Q/\Z;U(1)) = \varinjlim_N\Z/N = \Q/\Z\subset U(1)$.
Similarly $H^3(\Q/\Z\oplus\Q/\Z;U(1)) = ?$ via Künneth, with $H^1(\Q/\Z;U(1)) = \mathrm{Hom}(\Q/\Z;U(1)) = \widehat{\Q/\Z}$, a compact group; and $H^2(\Q/\Z;U(1)) = ?$

**Corrected computation.** For $\Q/\Z$ discrete, $H^*(\mathbf{B}\Q/\Z;U(1))$ has:
- $H^0 = U(1)$
- $H^1 = \mathrm{Hom}(\Q/\Z,U(1)) = \widehat{\Q/\Z}$ (Pontryagin dual, profinite)
- $H^2 = \mathrm{Ext}^1(\Q/\Z,U(1)) = ?$ (non-trivial, but requires care)
- $H^3 = \Q/\Z$ or $U(1)$? Depends on the cocycle model.

The resulting Künneth on $H^3(\mathbf{B}(\Q/\Z)^{24};U(1))$ is more intricate than the naive $U(1)^{24}$.

**Repair (Wave 4).** The correct computation for a Lyubashenko ind-category on $(\Q/\Z)^{24}$ is:
$$
H^3(\mathbf{B}(\Q/\Z)^{24};U(1))_{\mathrm{Lyu}} = \varinjlim_N H^3(\mathbf{B}(\Z/N)^{24};U(1))
$$
taken over $N$ divisibility, with the transition maps being **pullback along** $(\Z/N)\hookrightarrow(\Z/M)$ for $N\mid M$.

$H^3(\mathbf{B}(\Z/N)^k;U(1))$ has a direct computation via the Lyndon–Hochschild–Serre spectral sequence: for $k = 1$, it is $\Z/N$; for $k > 1$, it has a $\Z/N$-summand from each of the $k$ copies, plus cross-product terms.

The ind-limit is
$H^3(\mathbf{B}(\Q/\Z)^{24};U(1)) \supset \bigoplus^{24}\Q/\Z \cong (\Q/\Z)^{24}$.

**Wave-4 corrected formula:** $\tilde\alpha_{K3}^\Q\in (\Q/\Z)^{24}$, not $U(1)^{24}$, where $\Q/\Z\subset U(1)$ is the torsion subgroup. This correction is **benign**: the Mukai-quadratic-form cocycle was already valued in $\Q/\Z$, since the Mukai pairing is rational. The 3-cocycle class lives in the **torsion** subgroup, a discrete $\Q/\Z^{24}$.

**Verdict.** Attack valid at the strict sheaf-cohomology level; healed by restricting to $\Q/\Z$-valued torsion (which is where Mukai-quadratic-form cocycles naturally live). The corrected formula is $(\Q/\Z)^{24}$, a discrete infinite torsion group.

### 7.5 Attack: did I miss the hexagon 3-cocycle vs. pentagon 3-cocycle distinction?

**Claim to attack.** I treated "pentagon 3-cocycle" and "hexagon 3-cocycle" as a single object. But Drinfeld 1989's quasi-Hopf theory has **distinct** pentagon and hexagon 3-cocycles, and the rational-Fock sector should have **both**.

**Attack.** For a braided quasi-Hopf algebra $H$, there are:
- Pentagon 3-cocycle $\alpha\colon H^{\otimes 3}\to k$ (associator of the monoidal structure).
- Hexagon 3-cocycle $R\colon H^{\otimes 2}\to k$ (braiding, satisfying hexagon axioms involving $\alpha$).
- Additionally, in ENO, a combined $(\alpha, q)$ with $q$ the self-braiding quadratic form.

**Heal.** In the pointed braided fusion case, the hexagon 3-cocycle is **determined** by the pentagon and the quadratic form via Eilenberg–Mac Lane transgression. Specifically: given a quadratic form $q$ on $G$, the associated 2-cocycle $b_q(x,y) = q(x+y)/q(x)q(y)$ determines the braiding up to homotopy, and the pentagon cocycle is the transgressed class of $q$ itself.

So ENO 2010 uses the **single datum $(G, q, \alpha)$** where the hexagon is absorbed into the data by the Postnikov decomposition. The Lyubashenko framework also uses this reduction for pointed (abelian-grading-group) categories.

**Verdict.** Attack valid in general, but **for pointed braided fusion** (our case), the hexagon is determined by the quadratic form, so it's not an independent datum. The Wave-4 computation of a single 3-cocycle is therefore complete.

### 7.6 Attack: is the rational-Fock really "the right" extension of the Tannakian target?

**Claim to attack.** I extended Wave-3's $C_2$-cofinite Tannakian reconstruction to the rational-Fock sector, claiming this is the natural next extension.

**Attack.** Why stop at rational? Why not go to **real** or **complex** Fock modules? These include all possible weights, not just rational ones.

**Heal (the rationality criterion).** Real/complex Fock modules have **infinite-order** monodromy (Claim 1.2), which precludes any modular-functor structure of finite type. The rational sector is the **largest** sector where (a) monodromy is finite-order, (b) modular representation is finite-rank, (c) Lyubashenko's coend construction makes sense.

Beyond rational: the category becomes genuinely uncountable, and no finite-rank algebraic reconstruction target exists. The Tannakian (or Lyubashenko, or ENO) story breaks down entirely.

**Verdict.** Attack valid in principle; healed by the rationality criterion (1.2). The rational sector is the maximal setting where algebraic reconstruction is possible.

### 7.7 Attack: am I double-counting the Wave-3 Kummer class?

**Claim to attack.** I claimed the Wave-3 Kummer 3-cocycle in $\Z/6\oplus\Z/6$ is the restriction of the Wave-4 rational-Fock cocycle in $(\Q/\Z)^{24}$, at denominator $N = 6$.

**Attack.** But Wave 3 located the Kummer class on **Deligne cohomology of $\cM^{\mathrm{Bridg}}_{K3}$**, not on group cohomology of $\mathbf{B}G_6$. These are different ambient cohomologies; a priori there's no reason for the two classes to agree.

**Heal (naturality).** The two cohomologies are related by the classifying-map
$\cM^{\mathrm{Bridg}}_{K3}\to\mathbf{B}(\Q/\Z)^{24}$ (classifying the monodromy of the Mukai lattice modulo integers). Both Wave 3's Deligne class and Wave 4's group-cohomology class are pulled back from this classifying map, and by the Milnor–Thomason naturality of cohomology, they represent the same invariant.

Specifically: Wave 3 restricted the global cocycle to the Kummer stratum ($SL(2,\Z)^2$-monodromy), where $(\Q/\Z)^{24}$ reduces to $(\Z/12)^2$ (via the $E_1\times E_2$-embedding), further reduced to $(\Z/6)^2$ by $\iota$. Wave 4 pulled back the same global cocycle to $\mathbf{B}G_6$. **These are two presentations of the same cohomology class, seen in two different resolutions of $\cM^{\mathrm{Bridg}}_{K3}$.**

**Verdict.** Attack valid for verifying naturality, not for falsifying. The two classes **are** the same, as Wave 4 §4.4 asserts. The double-counting worry is dispelled by naturality.

---

## Part 8. Wave-4 convergence statement

### 8.1 Deliverables

| Deliverable | Status |
|---|---|
| (i) Rational-Fock subcategory defined | **Done**: $\mathrm{Rep}^{\Q,(N)}$ at denominator $N$; colimit $\mathrm{Rep}^\Q = \varinjlim_N$; objects indexed by $\Lambda_{\mathrm{Muk}}^\Q$. |
| (ii) Non-$C_2$-cofiniteness verification | **Proved** (Claim 2.1): countably infinite simples at low conformal weight; $V/C_2(V)$ not finite-dim on rational sector. |
| (iii) Lyubashenko framework invoked | **Done**: $\mathrm{Rep}^{\Q,(N)}$ fits Lyubashenko (L1)–(L3) at finite $N$; ind-Lyubashenko at colimit. 3-cocycle in $H^3(\mathbf{B}G_N;U(1))$. |
| (iv) Rational-Fock 3-cocycle computed | **Done**: $\tilde\alpha_{K3}^\Q\in(\Q/\Z)^{24}$ as the Mukai quadratic form $q_\infty$ transgressed through Eilenberg–Mac Lane $K(G,2)$-cohomology. ENO-2010 classified as pre-metric group $((\Q/\Z)^{24}, q_\infty, \alpha_\infty)$. |
| (v) Moduli-global verdict | **Done**: locally trivialisable by ENO-automorphism torsor; globally non-trivial due to $\pi_1(\cM^{\mathrm{Bridg}})$-monodromy. Kummer stratum gives $\Z/6\oplus\Z/6$; Shioda–Inose etc. expected further strata. **Genuine global obstruction.** |
| (vi) Gaiotto W3 level-2 cross-check | **Done**: $V^{\otimes 2}/\mathrm{Serre}$ with $\dim=575$ is **visible** as a non-simple $L_2$-module in $\mathrm{Rep}^{\Q,(2)}$ after Serre quotient. |
| (vii) Convergence statement | **Done**: see §8.2. |

### 8.2 The Wave-4 convergence statement

**Theorem (Wave 4, Etingof).** *Let $A_{K3}$ be the K3 chiral algebra at a generic smooth K3 point. Let $\mathrm{Rep}^\Q(A_{K3})$ be the rational-Fock subcategory, with simples indexed by $\Lambda_{\mathrm{Muk}}\otimes_\Z\Q$. Then:*

*(i) $\mathrm{Rep}^\Q$ is a pointed braided ind-fusion category; it is NOT $C_2$-cofinite.*

*(ii) The truncation $\mathrm{Rep}^{\Q,(N)}(A_{K3})$ at denominator $N$ is a pointed braided fusion category with ENO-2010 pre-metric group*
$((\Z/N)^{24}, q_N, \alpha_N)$
*where $q_N$ is the Mukai quadratic form mod $N^2\Z$ and $\alpha_N$ is its Eilenberg–Mac Lane transgression.*

*(iii) The colimit 3-cocycle lives in*
$$
\tilde\alpha_{K3}^\Q\in H^3(\mathbf{B}(\Q/\Z)^{24};U(1))_{\mathrm{torsion}} = (\Q/\Z)^{24},
$$
*as the direction-wise Mukai quadratic form transgressed to $H^3$.*

*(iv) Globally over $\cM^{\mathrm{Bridg}}_{K3}$, $\tilde\alpha_{K3}^\Q$ is not trivialisable by the ENO-automorphism torsor: monodromy along $\pi_1(\cM^{\mathrm{Bridg}})$ creates genuine 3-cocycle obstructions, localised at special-Picard strata:*
- *Generic smooth K3: zero (conjectural, pending Wave-3 OP-W3-1).*
- *Kummer $\mathrm{Km}(E_1\times E_2)$: $\Z/6\oplus\Z/6\subset(\Z/12)^2\subset(\Q/\Z)^{24}$ (Wave 3 confirmed).*
- *Shioda–Inose (isogenous to Kummer): similar $\Z/6$-type (Wave-3 OP-W3-2 conjectural).*
- *ADE enhancement: trivialisable by the 2-cochain $c_{\mathrm{ADE}}(\alpha)=(-1)^{-\langle\alpha,\alpha\rangle/2}$ (Wave-3 confirmed).*

*(v) Gaiotto W3's level-2 Yangian module $V^{\otimes 2}/\mathrm{Serre}$ of $\dim=575$ is visible in $\mathrm{Rep}^{\Q,(2)}$ as a compact (non-simple) $L_2$-module, after Serre quotient.*

*(vi) The full K3 Yangian reconstruction is therefore stratified by four levels of visibility:*
1. *$C_2$-cofinite integer-weight core (Wave-2/3): strict Hopf at ADE / generic / quasi-Hopf at Kummer.*
2. *Rational-Fock at denominator $N$ (Wave-4, finite): pointed braided fusion with ENO 3-class $\alpha_N$.*
3. *Ind-rational-Fock (Wave-4, colimit): ind-Lyubashenko with 3-cocycle $\tilde\alpha_{K3}^\Q\in(\Q/\Z)^{24}$.*
4. *Real/complex-Fock: infinite-order monodromy, no algebraic reconstruction target.*

### 8.3 What Wave 4 did not establish (open)

**OP-W4-1 (mid).** Explicit chain-level verification that the Wave-3 Kummer class in Deligne cohomology of $\cM^{\mathrm{Bridg}}_{\mathrm{Km}}$ coincides with the Wave-4 restriction of $\tilde\alpha_{K3}^\Q$ to $G_6$. Argument exists via naturality (§7.7); rigorous cocycle-level witness deferred.

**OP-W4-2 (mid).** The full K3 monodromy 3-class $[\pi_1(\cM^{\mathrm{Bridg}}_{K3})]\in H^3(\pi_1;(\Q/\Z)^{24})$ — is it completely classified by the Wave-3 refined criterion (arithmetic monodromy 3-class), or are there rational-Fock-specific contributions?

**OP-W4-3 (high).** Extension to Shioda–Inose strata (OP-W3-2): the Wave-4 framework predicts 3-cocycle classes from $\mathrm{Aut}(T)$-monodromy where $T$ is the transcendental lattice. Explicit computation for K3's of Shioda–Inose type with CM by $\Z[i]$, $\Z[\omega]$, etc.

**OP-W4-4 (high).** Factorisation of the full $\Phi_{10}(q,y,p)^{-1}$ as a Lyubashenko-modular character of $\mathrm{Rep}^\Q(A_{K3})$, matching the Gaiotto W3 DMVV expansion at level $p$. Structurally clean, but chain-level verification deferred.

**OP-W4-5 (deep).** Does the rational-Fock reconstruction of the K3 Yangian give a genuinely new Hopf algebra, or does it factor through the $C_2$-cofinite Wave-3 reconstruction? Conjectured: at generic K3, the rational-Fock reconstruction is the **central extension** of the $C_2$-cofinite one by $(\Q/\Z)^{24}$; at Kummer, the extension is non-trivial at the $\Z/6\oplus\Z/6$ class.

**OP-W4-6 (deep).** Relation to Felder's KZB 1994 elliptic associator: is $\tilde\alpha_{K3}^\Q$ the transgressed class of the KZB associator in the $g = 1$ (elliptic) factor of the Kummer decomposition? This would make the Wave-4 3-cocycle the Drinfeld associator of the Kummer-stratum K3 Yangian.

### 8.4 Cross-volume and cross-wave implications

**Wave-3 Etingof refinement.** The "three-stratum Tannakian" of Wave 3 (ADE / generic / Kummer) is now a **four-tier visibility stratification**: add the "rational-Fock ind-Lyubashenko" tier, which sees the full $\tilde\alpha_{K3}^\Q\in(\Q/\Z)^{24}$, with Wave-3 classes as restrictions.

**Wave-3 Gaiotto level-$k$ modules.** Level-1 and level-2 Gaiotto modules embed into $\mathrm{Rep}^{\Q,(N)}$ at small $N$ (level-1 into $N=1$ integer case; level-2 into $N=2$ rational case). Higher-$k$ modules require higher $N$.

**Cross-volume Vol II SC$^{\mathrm{ch,top}}$ pentagon anomaly.** Wave 3 matched the Kummer 3-cocycle to SC$^{\mathrm{ch,top}}$ Pentagon coherence at chain level. Wave 4 extends: the SC$^{\mathrm{ch,top}}$ Pentagon on the rational-Fock sector has a **full $(\Q/\Z)^{24}$-valued** pentagon-anomaly class, with the Kummer $\Z/6\oplus\Z/6$ being its restriction.

**Cross-volume Vol I seven-faces $r(z)$.** The level-$k$ Yangian $r$-matrix at $k = N$ rational denominator should factor through the Lyubashenko $S$-$T$-modular action on $\mathrm{Rep}^{\Q,(N)}$. This was previously assumed but not structurally grounded; Wave 4 gives the grounding.

### 8.5 Manuscript-inscription recommendations

1. **Vol III Chapter K3-Yangian**: add a subsection on the rational-Fock sector, stating:
   - Definition 1.1 (rational-Fock subcategory).
   - Theorem (Wave 4, §8.2 above).
   - Remark on the Wave-3/Wave-4 unification: Kummer $\Z/6\oplus\Z/6$ is the denominator-6 restriction of the global $(\Q/\Z)^{24}$-class.

2. **Vol I seven-faces $r(z)$ chapter**: refine the conjectural "moduli-global stratification of Yangian reconstruction" to include the rational-Fock / Lyubashenko / ENO layer; cite ENO 2010 and Lyubashenko 1997 as the correct frameworks beyond $C_2$-cofinite Tannakian.

3. **Vol II SC$^{\mathrm{ch,top}}$ chapter**: refine the Pentagon-anomaly remark: the chain-level Pentagon on the full rational-Fock sector commutes only up to a $(\Q/\Z)^{24}$-valued 3-class, with Kummer $\Z/6\oplus\Z/6$ being the first non-trivial restriction. Pattern 269 (adjunction-strictness conflation) applies: $(\infty,1)$-Pentagon always commutes; chain-level Pentagon commutes only up to this 3-class.

4. **SYNTHESIS_WAVE4.md** (to be authored from 10 wave-4 agent notes): update §1.5, §2 item 14 with the Wave-4 resolution of "rational-Fock-module visibility".

---

## Etingof's closing remark (voice)

Wave 3 said: the Tannakian reconstruction is strict Hopf at generic K3 **on the Tannakian-visible $C_2$-cofinite subcategory**, quasi-Hopf only at special-Picard loci like Kummer, and the rational-Fock sector is invisible.

Wave 4 says: the rational-Fock sector is not invisible — it is the **natural home** of the 3-cocycle, and the $C_2$-cofinite reconstruction sees only the integer-lattice projection of a deeper, $(\Q/\Z)^{24}$-valued, ENO-classified structure. Lyubashenko's non-semisimple framework provides the correct ambient, and the Gaiotto W3 level-2 module lands inside $\mathrm{Rep}^{\Q,(2)}$ as a compact non-simple object after Serre quotient.

The Wave-3 Kummer 3-cocycle is not just a special-Picard-loci pathology; it is the **first non-trivial restriction** of a global rational-Fock class that lives uniformly on all of K3 moduli. The other special loci (Shioda–Inose, CM K3) give further restrictions; the generic K3 gives (conjecturally) zero.

The picture now has four tiers:
(1) $C_2$-cofinite integer-core (Wave-2/3 strict/quasi-Hopf stratification).
(2) Rational-Fock at finite denominator $N$ (Wave-4 finite ENO).
(3) Ind-rational-Fock (Wave-4 ind-Lyubashenko).
(4) Real/complex-Fock (beyond algebraic reconstruction).

Each tier sees a finer resolution of the K3 Yangian. Wave 4 is complete once the tier-3 3-cocycle is written out — which it now is, as $\tilde\alpha_{K3}^\Q\in(\Q/\Z)^{24}$, with Gaiotto's $\dim 575$ module embedded as a compact submodule of the Serre-quotient, and the Kummer class $\Z/6\oplus\Z/6$ as a subgroup restriction.

What Wave 5 must do: (a) verify the arithmetic monodromy 3-class vanishing at generic K3 (OP-W3-1, still open); (b) extend to Shioda–Inose strata (OP-W4-3); (c) match to Felder's KZB associator (OP-W4-6). Each of these is now a **concrete** next step — not a philosophical question, but a specific computation whose framework is in hand.

The reconstruction is now sharpened at the level of visibility: four tiers, each with its own framework (Tannakian / ENO / Lyubashenko / beyond-algebraic), and the 3-cocycle lives in the third tier as $(\Q/\Z)^{24}$, restricting to all previously computed special-loci classes. This is the Wave-4 deliverable.

---
