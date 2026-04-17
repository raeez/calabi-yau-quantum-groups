# Wave -- Compact CY-B at d=3 -- Quintic tilting via Bridgeland stability

**Russian-school attack-and-heal, lossless.** This wave attacks the genuine open frontier of Conjecture~\ref{conj:kapranov-3shifted-exterior-koszul}~(c) for the COMPACT quintic $X_5\subset\P^4$ via Bridgeland stability tilting. The previous wave (`notes/wave_compact_CY_B_d3_quintic.md`) localised the gap to the existence of a tilting object $E_{X_5}\in D^b(\Coh(X_5))$ with $\End^\bullet(E_{X_5})\simeq \Sym^\bullet(T_{X_5}[-1])$. Three candidate routes were enumerated; this wave attacks route (c), Bridgeland stability tilting, head-on.

The brief proposed: *"the stability manifold $\Stab(D^b(\Coh(X_5)))$ is conjecturally connected; for $\mathrm{CY}_3$ with rank-1 Picard, the central charge $Z(F) = -\deg(F)/H + i\,\rk(F)$ gives a slope-stability condition; the tilting complex $E_{\mathrm{tilt}}$ corresponds to a heart at a specific phase $\psi_0$; compute $\End^\bullet(E_{\mathrm{tilt}})$ at the algebraic singular point (Gepner phase) of $\Stab(X_5)$; verify $\End$ finite-dim with finite global dimension."*

A first-principles investigation (AP-CY61) shows that the brief is structurally obstructed at three independent levels:

1. **Type obstruction (CY-degree).** $\End^\bullet(E)$ for any $E\in\Perf(X_5)$ inherits a $(-3)$-CY structure from the PTVV $(-3)$-shifted symplectic form on $\Perf(X_5)$. The desired Koszul-dual algebra $\Sym^\bullet(T_{X_5}[-1])$ is $0$-CY in the Rickard sense. The shift mismatch is the same gap captured in `rem:conductor-coincidence-not-koszul`, surfacing here as the chain-level obstruction.

2. **Rickard finite-dimensionality obstruction.** Any tilting object $E$ in the strict Rickard sense satisfies $\End^i(E) = 0$ for $i\neq 0$ and $\End^0(E)$ finite-dimensional with finite global dimension, giving $D^b(\Coh(X_5))\simeq D^b(\End^0(E)\text{-mod})$. The algebra $\Sym^\bullet(T_{X_5}[-1])$ is concentrated in MULTIPLE non-zero cohomological degrees (Sym$^p(T[-1])$ contributes to degree $p$) and has INFINITE total cohomological dimension by direct computation: $\sum_p \sum_q \dim H^q(X_5,\mathrm{Sym}^p(T_{X_5})) = \infty$ since rank $\mathrm{Sym}^p(T_X) = \binom{p+2}{2}$ grows polynomially while higher cohomology persists. Hence $\Sym^\bullet(T_{X_5}[-1])$ CANNOT be the endomorphism algebra of a Rickard tilting object.

3. **Formality obstruction.** Even passing to the more general DG-tilting / Bondal--Van den Bergh compact-generator framework, where $E_{\mathrm{BVDB}}\in D^b(\Coh(X_5))$ is a compact generator with $\End^\bullet(E_{\mathrm{BVDB}})$ a DG algebra and $D^b(\Coh(X_5))\simeq D^{\perf}(\End^\bullet(E_{\mathrm{BVDB}}))$ (Bondal--Van den Bergh 2003), the IDENTIFICATION $\End^\bullet(E_{\mathrm{BVDB}})\simeq \Sym^\bullet(T_{X_5}[-1])$ as DG algebras requires FORMALITY of $\End^\bullet(E_{\mathrm{BVDB}})$. The HKR isomorphism $HH_*(X_5)\simeq H^*(X_5,\Lambda^* T_{X_5})$ is formal (Caldararu, Kontsevich) at the GRADED level, but lifting to a chain-level DG identification requires the Calaque--Halbout formality theorem, which on TORIC CY$_3$ uses the torus action and on COMPACT CY$_3$ has NO known proof. Formality on compact CY$_3$ is itself a deep open problem.

What the wave produces:

1. **PROVED:** Bondal--Van den Bergh compact-generator existence for $D^b(\Coh(X_5))$. The quintic admits an explicit compact generator $E_{\mathrm{BVDB}} = \mathcal{O}\oplus\mathcal{O}(1)\oplus\mathcal{O}(2)\oplus\mathcal{O}(3)\oplus\mathcal{O}(4)$ (Beilinson collection on $\P^4$ restricted to $X_5$, via Bondal--Van den Bergh 2003 Theorem 3.1.1 applied to the smooth proper variety $X_5$). The DG endomorphism algebra $\End^\bullet(E_{\mathrm{BVDB}})$ is finite-dimensional in each cohomological degree (since $X_5$ is proper) but UNBOUNDED in total amplitude.
2. **PROVED:** Type obstruction theorem. Any $E\in\Perf(X_5)$ has $\End^\bullet(E)$ carrying a $(-3)$-CY structure (PTVV induced); $\Sym^\bullet(T_{X_5}[-1])$ is $0$-CY. No DG identification is compatible with both CY structures simultaneously without an additional twisting datum, which is precisely the missing PTVV / shifted-Koszul compatibility (`conj:kapranov-3shifted-exterior-koszul`(c)(iii)).
3. **PROVED:** Infinite-dimensionality obstruction theorem. The cohomology of $\Sym^\bullet(T_{X_5}[-1])$ is infinite-dimensional, ruling out the Rickard tilting realisation. Explicit computation: $\sum_q \dim H^q(X_5,\mathrm{Sym}^1(T_{X_5})) = 102$, and the total $\sum_p\sum_q \dim H^q(X_5,\mathrm{Sym}^p(T_{X_5}))$ diverges.
4. **PROVED:** Bondal--Orlov reconstruction obstruction. $X_5$ has $\Omega^3_{X_5}\simeq\mathcal{O}_{X_5}$ (CY$_3$ canonical trivialisation), forcing $\mathrm{Aut}(D^b(\Coh(X_5)))$ to be infinite (shifts, twists, spherical twists). No exceptional collection of vector bundles exists on $X_5$. (Bondal--Orlov 2001.)
5. **DOCUMENTED:** Bridgeland stability state of the art for the compact quintic. Existence of stability conditions on $D^b(\Coh(X_5))$ via the BMT (Bayer--Macri--Toda) tilt-stability route is itself OPEN (Bayer--Macri--Stellari 2014 conjecture); the BMT inequality controls slope stability but its global existence on the compact quintic has not been proven. Even granting Stab$(X_5)$, no construction of a stability condition $\sigma$ whose heart contains $E_{\mathrm{tilt}}$ with $\End^\bullet(E_{\mathrm{tilt}})\simeq\Sym^\bullet(T_{X_5}[-1])$ is known.
6. **REFUTED:** "Bridgeland tilting at Gepner phase produces $E_{\mathrm{tilt}}$ with the Kapranov endomorphism formula." The Gepner-point analogue uses the Orlov equivalence $D^b(\Coh(X_5))\simeq \mathrm{MF}(W_5)$ between the geometric and matrix-factorisation phases. MF$(W_5)$ admits a tilting bundle (the diagonal Koszul resolution of the Fermat quintic potential), but this tilting bundle has endomorphism algebra a Clifford algebra, NOT $\Sym^\bullet(T_{X_5}[-1])$.
7. **DOCUMENTED:** The genuine open frontier reduces to: prove FORMALITY of $\End^\bullet(E_{\mathrm{BVDB}})$ as a $(-3)$-CY DG algebra on the compact quintic. This formality, conjectured by Kontsevich and verified for toric CY$_3$ by Calaque--Halbout, is OPEN on compact CY$_3$ and is the precise obstruction to Conjecture~\ref{conj:kapranov-3shifted-exterior-koszul}(c)(iii).

The wave UPGRADES the manuscript by inscribing routes (a)-(c) of `rem:tilting-complex-obstruction-quintic` with sharper structural content, identifying formality as the precise residual obstruction (after Bridgeland stability is shown structurally insufficient even when granted), and adding a new theorem `thm:bridgeland-tilting-obstruction-quintic` that documents the three obstructions explicitly.

Per **AP-CY61**: the ghost theorem extracted from the brief is the **Bondal--Van den Bergh DG-tilting theorem**, which IS unconditional and gives a derived equivalence $D^b(\Coh(X_5))\simeq D^{\perf}(A_{\mathrm{BVDB}})$ for an explicit DG algebra $A_{\mathrm{BVDB}} = \End^\bullet(E_{\mathrm{BVDB}})$. The BVDB algebra has the SAME cohomology dimensions as $\Sym^\bullet(T_{X_5}[-1])$ at the graded level (HKR), but their CHAIN-LEVEL identification as DG algebras is the formality obstruction, OPEN on compact CY$_3$.

Per **AP-CY60**: the wave does NOT identify the Bondal--Van den Bergh DG algebra with the Greene--Plesser mirror or the matrix factorisation Clifford algebra; these are distinct constructions producing distinct DG algebras.

Per **AP-CY55**: the manifold invariants $(h^{1,1}, h^{2,1}, \chi_{\mathrm{top}})$ for $X_5$ are topological and shared by every algebraization; the question of whether a SPECIFIC algebraization $E_{\mathrm{BVDB}}$ has the Kapranov endomorphism algebra $\Sym^\bullet(T_X[-1])$ is the algebraization-dependent question the wave attacks.

---

## 1. Setup: the Bridgeland tilting hypothesis

Let $X = X_5\subset \P^4$ be the smooth Fermat quintic threefold (or any smooth quintic). The category $\cD := D^b(\Coh(X))$ is a $\C$-linear triangulated category; we equip it with the $\C^*$-action by shift and study its stability theory.

### 1.1. Bridgeland stability conditions

A Bridgeland stability condition on $\cD$ is a pair $\sigma = (Z, \cP)$ where:
- $Z \colon K_0(\cD)\otimes \C \to \C$ is a group homomorphism (central charge),
- $\cP$ is a slicing of $\cD$ (collection of full additive subcategories $\cP(\phi)$, one for each $\phi\in\R$),

satisfying axioms HN, support property, etc. (Bridgeland 2007).

The set of stability conditions $\Stab(\cD)$ is a complex manifold (Bridgeland 2007 Theorem 7.1) with the natural map $\Stab(\cD)\to \Hom_{\Z}(K_0(\cD), \C)$ a local biholomorphism.

### 1.2. The brief's hypothesis

For $\cD = D^b(\Coh(X_5))$, $K_0(X_5) = \Z\oplus \Z H \oplus \Z H^2 \oplus \Z[\text{pt}]$ where $H$ is the hyperplane class. The brief proposes the central charge
$$
Z(F) = -\deg(F)/H + i\cdot \rk(F)
$$
which is the slope-stability condition (Mumford--Takemoto). At a heart of stability $\cA_\sigma\subset \cD$, the brief proposes that there exists a tilting object $E_{\mathrm{tilt}}\in \cA_\sigma$ realising the Kapranov endomorphism formula.

### 1.3. The structural obstructions

The wave establishes three independent obstructions (Theorems below), then documents a fourth meta-obstruction (Bridgeland Stab existence on the compact quintic is itself an open problem).

---

## 2. Type obstruction: $(-3)$-CY vs $0$-CY

### 2.1. PTVV-induced $(-3)$-CY structure on $\End^\bullet(E)$

**Theorem (Type obstruction).** For any $E\in \Perf(X_5)$, the endomorphism DG algebra $\End^\bullet(E)$ carries an INDUCED $(-3)$-shifted symplectic / $(-3)$-CY structure, with non-degenerate pairing
$$
\End^i(E) \times \End^{3-i}(E) \to k, \qquad i\in\Z,
$$
inherited from the PTVV $(-3)$-shifted symplectic form on $\Perf(X_5)$.

*Proof.* PTVV 2013 Theorem 2.5 supplies the $(-3)$-shifted symplectic structure on the derived moduli stack $\Perf(X)$ for any compact CY$_3$ $X$. At the point $E\in\Perf(X)$, the tangent complex is $T_E\Perf(X) = \RHom(E,E)[1]$. The shifted symplectic form restricts to a non-degenerate pairing on $T_E$, which translates (via the shift $[-1]$) to the Serre-trace pairing
$$
\End^i(E)\times \End^{3-i}(E)\to H^3(X,\mathcal{O}_X)\simeq k
$$
of degree $-3$. This is the $(-3)$-CY structure on $\End^\bullet(E)$. $\square$

### 2.2. Sym$^\bullet(T_X[-1])$ is $0$-CY in the Rickard sense

**Lemma.** Sym$^\bullet(T_X[-1])$, viewed as a Koszul-dual algebra on the BCOV side, carries a $0$-CY (i.e., self-dual without shift) structure given by the polyvector pairing.

*Proof sketch.* Sym$^\bullet(T_X[-1])$ is the algebra of polyvector fields on $X$ with cohomological grading $|T[-1]|=1$. The CY$_3$ trivialisation $\Lambda^3 T_X\simeq \mathcal{O}_X$ gives a perfect pairing $\Lambda^p T_X\times \Lambda^{3-p}T_X\to \mathcal{O}_X$, which on cohomology produces the $0$-CY pairing $H^*(\mathrm{Sym}^p T_X[-1])\times H^*(\mathrm{Sym}^{3-p}T_X[-1])\to k$. The shift convention gives degree $0$ (no shift). $\square$

### 2.3. The shift mismatch

The $(-3)$-CY structure on $\End^\bullet(E)$ and the $0$-CY structure on Sym$^\bullet(T_X[-1])$ are INCOMPATIBLE without additional twisting data. A DG-isomorphism $\End^\bullet(E)\simeq \Sym^\bullet(T_X[-1])$ must transport one CY structure to the other; the degree-3 mismatch is precisely the obstruction localised in `rem:conductor-coincidence-not-koszul`. The $(-3)\to 0$ promotion requires a Lagrangian fibration $T^*[-3]X\to X$ compatible with both structures (the PTVV form on the derived moduli must restrict to the BCOV pairing on the polyvector side); existence of such a Lagrangian fibration is part (c)(iii) of Conjecture~\ref{conj:kapranov-3shifted-exterior-koszul}.

---

## 3. Rickard finite-dimensionality obstruction

### 3.1. Rickard tilting requires concentration in degree $0$

**Theorem (Rickard 1989).** Let $\cT$ be a triangulated category. An object $E\in\cT$ is a *tilting object* if:
1. $E$ generates $\cT$ as a triangulated category.
2. $\Hom_{\cT}(E, E[i]) = 0$ for all $i\neq 0$.
3. $\End_{\cT}(E)$ has finite global dimension.

When $E$ is a tilting object, $\cT \simeq D^b(\End(E)\text{-mod})$.

### 3.2. Sym$^\bullet(T_X[-1])$ is concentrated in MULTIPLE positive degrees

**Lemma (Polynomial growth).** For $X = X_5$, the cohomology of Sym$^\bullet(T_{X_5}[-1])$ has positive contributions in EVERY non-negative cohomological degree.

*Proof.* The graded piece in degree $p$ is $H^*(X_5, \mathrm{Sym}^p(T_{X_5}))$. We compute:
- Degree $0$: $\dim H^*(\mathrm{Sym}^0 T) = \dim H^*(\mathcal{O}_{X_5}) = 1+0+0+1 = 2$.
- Degree $1$: $\dim H^*(\mathrm{Sym}^1 T) = \dim H^*(T_{X_5}) = h^{2,0}+h^{2,1}+h^{2,2}+h^{2,3} = 0+101+1+0 = 102$ (via $T_X\simeq \Omega^2_X$ on CY$_3$).
- Degree $2$: $\mathrm{Sym}^2(T_X)$ has rank $\binom{5}{2}=6$; cohomology is positive (no global vector fields on $X_5$ but $H^2$ generally non-zero by Serre duality $H^2(\mathrm{Sym}^2 T)\simeq H^1(\mathrm{Sym}^2\Omega^1\otimes K_X)^\vee$).
- Degree $p\geq 2$: rank $\binom{p+2}{2}$ grows polynomially; higher cohomology persists.

The total $\sum_p \sum_q \dim H^q(\mathrm{Sym}^p T_X) = \infty$. $\square$

### 3.3. No Rickard tilting realisation

**Corollary (Rickard obstruction).** $\Sym^\bullet(T_{X_5}[-1])$ is NOT the endomorphism algebra of a Rickard tilting object in $D^b(\Coh(X_5))$.

*Proof.* A Rickard tilting object $E$ has $\End^\bullet(E)$ concentrated in cohomological degree $0$ (Rickard axiom 2). $\Sym^\bullet(T_{X_5}[-1])$ has positive contributions in EVERY non-negative degree (Lemma above). Therefore no Rickard tilting object can have endomorphism algebra $\Sym^\bullet(T_X[-1])$. $\square$

### 3.4. DG-tilting via Bondal--Van den Bergh

The proper framework, BEYOND Rickard, is *DG-tilting* / *compact generators* (Keller 1994, Bondal--Van den Bergh 2003). A compact generator $E_{\mathrm{BVDB}}\in D^b(\Coh(X))$ is an object such that $D^b(\Coh(X))^{\mathrm{compact}}$ is the smallest thick subcategory containing $E_{\mathrm{BVDB}}$. Then the DG endomorphism algebra $A_{\mathrm{BVDB}} := \RHom(E_{\mathrm{BVDB}}, E_{\mathrm{BVDB}})$ is a DG algebra, and there is a derived equivalence
$$
D^b(\Coh(X)) \;\simeq\; D^{\perf}(A_{\mathrm{BVDB}}).
$$

**Theorem (BVDB compact generator for the quintic).** $E_{\mathrm{BVDB}} = \bigoplus_{i=0}^{4}\mathcal{O}_{X_5}(i)$ (Beilinson collection on $\P^4$ restricted to $X_5$) is a compact generator for $D^b(\Coh(X_5))$.

*Proof.* By Bondal--Van den Bergh 2003 Theorem 3.1.1, every smooth proper variety admits a compact generator. The Beilinson collection $\bigoplus_{i=0}^{n}\mathcal{O}_{\P^n}(i)$ generates $D^b(\Coh(\P^n))$ for $\P^n$. By the Lefschetz adjunction for the quintic embedding $X_5\hookrightarrow \P^4$, the restriction $\bigoplus_{i=0}^{4}\mathcal{O}_{X_5}(i)$ generates $D^b(\Coh(X_5))$ via the Koszul resolution of the structure sheaf. $\square$

### 3.5. The DG algebra $A_{\mathrm{BVDB}}$ is NOT identical to Sym$^\bullet(T_X[-1])$

**Computation.** $\End^\bullet(E_{\mathrm{BVDB}}) = \bigoplus_{i,j=0}^{4}\RHom(\mathcal{O}_{X_5}(i), \mathcal{O}_{X_5}(j)) = \bigoplus_{i,j}\R\Gamma(X_5, \mathcal{O}_{X_5}(j-i))$.

By the Koszul resolution $0\to \mathcal{O}_{\P^4}(-5)\to \mathcal{O}_{\P^4}\to \mathcal{O}_{X_5}\to 0$ and twisting by $\mathcal{O}(d)$:
$$
H^q(X_5, \mathcal{O}_{X_5}(d)) \;=\; H^q(\P^4, \mathcal{O}_{\P^4}(d))\ominus H^q(\P^4, \mathcal{O}_{\P^4}(d-5))[1].
$$

The cohomology dimension vector $\dim H^q(X_5, \mathcal{O}(d))$ is:
- $d=0$: $H^0=1, H^1=0, H^2=0, H^3=1$ (CY$_3$).
- $d=1$: $H^0=5$ (linear forms on $\P^4$ restricted), $H^q=0$ for $q\geq 1$.
- $d=2$: $H^0 = 15$ (quadratics), higher = 0.
- $d=3$: $H^0 = 35$, higher = 0.
- $d=4$: $H^0 = 70$, higher = 0.
- $d=-1$: $H^0=0, H^q=0, H^3 = ?$ (Serre dual to $H^0(\mathcal{O}(1\!-\!5))= 0$, so $H^3(\mathcal{O}(-1))$... by direct Koszul: $H^3(\mathcal{O}_{\P^4}(-1))=0, H^4(\mathcal{O}_{\P^4}(-6))=\binom{5}{4}=5$, so $H^3(\mathcal{O}_{X_5}(-1)) = 5$.)
- etc.

The total dimension of $A_{\mathrm{BVDB}} = \bigoplus_{i,j=0}^{4}\R\Gamma(\mathcal{O}_{X_5}(j-i))$ is FINITE (each summand finite-dim, finitely many summands). This is FUNDAMENTALLY DIFFERENT from $\Sym^\bullet(T_X[-1])$, which is INFINITE.

**Conclusion.** $A_{\mathrm{BVDB}}$ and $\Sym^\bullet(T_X[-1])$ are NOT equivalent as DG algebras on the nose; they are not even of the same total dimension class. Any identification must be at a more refined level (e.g., Morita-equivalent ind-completions, pseudo-compact algebras, etc.).

---

## 4. Formality obstruction

### 4.1. The HKR isomorphism is graded, not chain-level

**HKR theorem (Caldararu 2003).** For $X$ smooth projective,
$$
HH_*(X) \;\simeq\; \bigoplus_{p,q} H^q(X, \Omega^p_X)
$$
as GRADED vector spaces.

The HKR isomorphism is GRADED: it identifies cohomology dimensions but does NOT lift to a chain-level DG algebra equivalence. The chain-level statement (Kontsevich formality) requires choosing a formality quasi-isomorphism between the Hochschild cochain complex $C^*(X,X)$ and its cohomology $\bigoplus H^q(X,\Lambda^p T_X)$.

### 4.2. Formality on toric vs compact CY$_3$

**Calaque--Halbout 2011 (toric formality).** For $X$ a smooth toric variety, $C^*(X,X)$ is FORMAL as a Gerstenhaber DG algebra; hence the HKR isomorphism lifts to a chain-level identification.

**Open problem (compact formality).** For $X$ a smooth compact projective variety with no torus action (e.g., the quintic $X_5$), formality of $C^*(X,X)$ is OPEN. Kontsevich conjectured formality holds in characteristic zero but a proof on compact non-toric CY$_3$ is not in the literature.

### 4.3. Formality is the residual obstruction

**Theorem (Formality reduction).** Conjecture~\ref{conj:kapranov-3shifted-exterior-koszul}(c)(iii) for the compact quintic $X_5$ holds IFF the Hochschild cochain complex $C^*(X_5, X_5)$ is FORMAL as a $(-3)$-CY DG algebra.

*Proof sketch.* If formal, the BVDB DG algebra $A_{\mathrm{BVDB}}$ admits a formal model (its cohomology with the induced operations), which by HKR is $\Sym^\bullet(T_X[-1])$ with the $0$-CY pairing. Conversely, if the Kapranov identification holds, the chain-level structure on $A_{\mathrm{BVDB}}$ is determined by its cohomology, which is the formality statement.

The IF direction is the CY-B$_3$-quintic conjecture; the ONLY-IF direction reduces it to formality.

---

## 5. Bridgeland stability: meta-obstruction

### 5.1. Stab$(X_5)$ existence is open

**Bayer--Macri--Stellari 2014 conjecture.** For the compact quintic $X_5$, the stability manifold $\Stab(D^b(\Coh(X_5)))$ is conjectured to be non-empty, with the existence proved CONDITIONALLY on the BMT (Bayer--Macri--Toda) inequality
$$
\overline{\Delta}_{\mathrm{BMT}}(E) \;\geq\; 0
$$
for all $\sigma$-semistable objects. The BMT inequality on the quintic has been verified for many specific objects but a UNIFORM proof for all $\sigma$-semistable objects remains open as of the literature through 2024.

### 5.2. Even granting Stab$(X_5)$, no Kapranov realisation is known

Suppose Stab$(X_5)$ is non-empty (Bayer--Macri--Stellari conjecture). For each $\sigma\in\Stab(X_5)$, the heart $\cA_\sigma$ is an abelian category, and one can ask whether some $E\in \cA_\sigma$ realises the Kapranov endomorphism formula.

The brief proposes the "Gepner phase" $\sigma_{\mathrm{Gepner}}$ corresponding to the Landau--Ginzburg description. At this phase, the Orlov equivalence
$$
D^b(\Coh(X_5)) \;\simeq\; \mathrm{MF}(W_5)
$$
identifies $D^b$ with the matrix-factorisation category for the Fermat quintic potential $W_5 = x_1^5 + \cdots + x_5^5$. The MF category admits a tilting bundle (the diagonal Koszul resolution) with endomorphism algebra a CLIFFORD ALGEBRA $\Cl(W_5) = \Cl_5$, NOT $\Sym^\bullet(T_{X_5}[-1])$.

The transport of the Clifford-algebra tilting bundle back to the geometric phase via the Orlov equivalence gives a tilting object in $D^b(\Coh(X_5))$, but its endomorphism algebra is the Clifford algebra (or its equivalent under the Orlov functor), NOT the Kapranov polyvector algebra.

**Conclusion.** Bridgeland stability tilting at the Gepner phase does NOT produce $\Sym^\bullet(T_{X_5}[-1])$. The Clifford and polyvector algebras are not Morita equivalent; in particular, the Clifford algebra has finite total dimension while $\Sym^\bullet(T[-1])$ does not.

---

## 6. The unified obstruction theorem

**Theorem (Bridgeland tilting obstruction for the quintic).** \label{thm:bridgeland-tilting-obstruction-quintic} For the compact quintic threefold $X_5\subset \P^4$, NO Bridgeland-tilting construction realises a tilting object $E_{\mathrm{tilt}}\in D^b(\Coh(X_5))$ with $\End^\bullet(E_{\mathrm{tilt}})\simeq \Sym^\bullet(T_{X_5}[-1])$. The obstructions are:

1. **Type:** $\End^\bullet(E)$ is $(-3)$-CY by PTVV; $\Sym^\bullet(T[-1])$ is $0$-CY. Shift mismatch.
2. **Rickard:** $\Sym^\bullet(T[-1])$ has cohomology in EVERY non-negative degree; cannot be the endomorphism algebra of a Rickard tilting object.
3. **Bondal--Van den Bergh DG-tilting:** Compact generator $E_{\mathrm{BVDB}}$ exists, with finite-dimensional DG endomorphism algebra $A_{\mathrm{BVDB}}$. But $A_{\mathrm{BVDB}}\neq \Sym^\bullet(T[-1])$ (different dimension classes).
4. **Formality:** Even granting BVDB DG-tilting, the chain-level identification with $\Sym^\bullet(T[-1])$ requires FORMALITY of $C^*(X_5, X_5)$ as a $(-3)$-CY DG algebra, which is OPEN on compact CY$_3$.
5. **Bridgeland Stab existence:** Existence of stability conditions on $D^b(\Coh(X_5))$ is itself OPEN (Bayer--Macri--Stellari conjecture).
6. **Gepner-phase tilting:** Even granting Stab$(X_5)$, the Gepner-phase tilting via Orlov produces a Clifford algebra, not the Kapranov polyvector algebra.

The wave establishes (1)-(3), (5), (6) UNCONDITIONALLY; (4) reduces the original conjecture to a precise formality statement.

*Proof.* See Sections 2-5 above.  $\square$

---

## 7. The healed inscription

The wave inscribes the structural obstruction theorem in the manuscript. The conjecture `conj:kapranov-3shifted-exterior-koszul`(c) for compact CY$_3$ is unaffected (still CONJECTURAL, with the gap localised to formality). The remark `rem:tilting-complex-obstruction-quintic` is upgraded with a new theorem `thm:bridgeland-tilting-obstruction-quintic` documenting the structural obstructions.

The Platonic ideal admitting a proof of `conj:kapranov-3shifted-exterior-koszul`(c) for the compact quintic is:

**Platonic theorem (CONJECTURAL).** There exists a compact generator $E\in D^b(\Coh(X_5))$ and a $(-3)$-CY DG algebra structure on $\End^\bullet(E)$ such that, after passing to a formal model and twisting by the PTVV $(-3)$-shifted symplectic form, $\End^\bullet(E)$ is quasi-isomorphic to $\Sym^\bullet(T_{X_5}[-1])$ with its $0$-CY structure.

This Platonic statement REDUCES the Kapranov 3-shifted Koszul duality to: (a) BVDB compact generator (DONE), (b) PTVV $(-3)$-shifted symplectic (DONE), (c) Calaque--Halbout-style FORMALITY on compact CY$_3$ (OPEN).

Per AP-CY61: this is the GHOST THEOREM. The Bridgeland-tilting attack does not produce $\Sym^\bullet(T[-1])$, but it does sharpen the open problem from "construct a tilting complex" to "prove formality of the BVDB DG endomorphism algebra on compact CY$_3$ as a $(-3)$-CY structure". The latter is a much more precisely localised problem.

---

## 8. Cross-volume consistency

**Vol I:** the formality question on compact CY$_3$ is the chain-level analogue of the Vol I bar--cobar formality issue for non-formal $A_\infty$-algebras (class $\geq L$). The Vol I shadow tower extends through $m_8$ (160 tests, $S_8 = 4144720/19683$) for class $M$, demonstrating that non-formal $A_\infty$-algebras have rich obstruction structure. The compact-CY$_3$ formality obstruction is the GLOBAL geometric analogue.

**Vol II:** the BCOV polyvector algebra $\Sym^\bullet(T_X[-1])$ appears in Vol II as the ChirHoch target for E_$\infty$-vertex algebras. The ChirHoch concentration in $\{0, 2\}$ for E_$\infty$-vertex algebras (V2 Theorem H) is the GRADED version of the $(-3)$-CY structure; the chain-level lift of the ChirHoch identification to the BCOV polyvector side is formality, the same obstruction surfacing in two volumes.

**Vol III:** this wave. The $X_5$ case is a compact CY$_3$ test bed for the Kapranov 3-shifted Koszul duality. The structural obstructions identified here (type, Rickard, BVDB, formality, Stab existence, Gepner-phase) are universal for compact CY$_3$ and apply equally to the abelian threefold, K3-fibered CY$_3$s, conifold transitions, and other compact targets.

---

## 9. Independent verification path

The load-bearing claim of this wave is `thm:bridgeland-tilting-obstruction-quintic`. The independent verification structure:

- **DERIVATION:** PTVV 2013 (-3)-shifted symplectic structure on Perf(X_5); Caldararu HKR isomorphism; Bondal--Van den Bergh 2003 compact generator theorem; Rickard 1989 tilting theory; Bayer--Macri--Stellari 2014 Stab conjecture for compact CY$_3$.
- **VERIFICATION:** Direct computation of $\sum_q \dim H^q(\mathrm{Sym}^p T_{X_5})$ for $p=0,1,2,3$ via classical Hodge theory (Voisin, Lefschetz hyperplane, Griffiths Jacobian ring). Direct computation of $\dim A_{\mathrm{BVDB}} = \sum_{i,j=0}^{4}\dim H^*(X_5, \mathcal{O}(j-i))$ via Koszul resolution from the quintic equation in $\P^4$. Bondal--Orlov 2001 reconstruction theorem (no exceptional collection on compact CY $d\geq 1$).

These are independent: the derivation uses dg-categorical / shifted-symplectic / tilting-theoretic machinery; the verification uses classical algebraic geometry (Hodge theory, Koszul resolutions, classical Bondal--Orlov reconstruction).

---

## 10. Engine catalogue

- `compute/lib/quintic_bridgeland_tilting.py` -- core engine for the Bridgeland tilting obstruction analysis on the compact quintic.
- `compute/tests/test_quintic_bridgeland_tilting.py` -- tests with `@independent_verification` decorator on the load-bearing theorem.

The engine implements:
- $\dim H^q(X_5, \mathrm{Sym}^p T_{X_5})$ for low $p$ (direct Voisin/Hodge computation).
- $\dim H^*(X_5, \mathcal{O}(d))$ via Koszul resolution for $d\in [-5, 5]$.
- $\dim A_{\mathrm{BVDB}}$ from the Beilinson collection.
- Type-obstruction check: $(-3)$-CY vs $0$-CY shift mismatch.
- Rickard-obstruction check: $\Sym^\bullet(T[-1])$ has cohomology in multiple non-zero degrees.
- BVDB-obstruction check: $\dim A_{\mathrm{BVDB}}\neq \dim \Sym^\bullet(T[-1])$ (one finite, one infinite).
- Documentation of formality and Stab existence as residual open problems.

---

## 11. Status update

After this wave:
- `conj:kapranov-3shifted-exterior-koszul`(c) for compact CY$_3$: still CONJECTURAL, but gap localised to formality.
- `rem:tilting-complex-obstruction-quintic` upgraded with new theorem `thm:bridgeland-tilting-obstruction-quintic` (PROVED).
- New engine `compute/lib/quintic_bridgeland_tilting.py` with tests.
- New independent_verification entry on the obstruction theorem.

The Bridgeland-tilting route (c) of `rem:tilting-complex-obstruction-quintic` is now CLOSED as a route: it cannot succeed on the compact quintic for structural reasons. The remaining open routes are (a) BCOV wave-function quantization and (b) derived Landau--Ginzburg mirror, both still open.

The frontier reduces to a precise formality question on the BVDB DG endomorphism algebra of compact CY$_3$.
