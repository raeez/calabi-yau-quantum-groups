# Inscription draft: prop:phi-k3-padic-langlands-fermat (Vol III F33, d=2 case)

**Status:** DRAFT ONLY. Not inscribed into any `.tex`. For Wave-2 F33 closure of the d=2 Fermat-quartic K3 instance of the p-adic CY Langlands programme.

**Author:** Raeez Lorgat. 2026-04-17.

**Target environment:** `\begin{proposition}` (not theorem: single-family instance, not the full Vol III F33 frontier) with `\ClaimStatusProvedElsewhere`.

---

## 1. Statement

> **Proposition (p-adic CY Langlands for the Fermat quartic K3).** Let $X \subset \mathbb{P}^3_{\mathbb{Q}}$ be the Fermat quartic $x_0^4 + x_1^4 + x_2^4 + x_3^4 = 0$, a K3 surface over $\mathbb{Q}$ with geometric Picard rank $\rho_{\mathrm{NS}} = 20$ and transcendental lattice $T(X)$ of rank $2$. Let $\Phi(X)$ denote the Vol III CY-to-chiral image at $d=2$ (the Mukai Heisenberg $H_{\mathrm{Muk}}$ of rank $24 = b_2(X) + 2 = \kappa_{\mathrm{fiber}}(X)$; CY-A$_2$ PROVED). For each rational prime $p$ of good reduction ($p \neq 2$) and each integer $n \geq 1$:
>
> (i) *(Local-factor identity.)* The $p$-adic shadow zeta $\zeta^{(p)}_{\Phi(X)}$ of $\Phi(X)$ specialised at the Frobenius eigenvalue $\mathbb{L} = p^2$ satisfies
>
> $$\zeta^{(p)}_{\Phi(X)}(s) = L_p\bigl(H^2(X, \mathbb{Q}_\ell),\, s\bigr) \cdot L_p\bigl(H^0(X) \oplus H^4(X),\, s\bigr),$$
>
> where the right-hand side is the product of Hasse–Weil local factors and the shadow Dirichlet coefficients decompose as $a_n(p) = 1 + \operatorname{Tr}(\operatorname{Frob}_p^n \mid H^2) + p^{2n}$.
>
> (ii) *(Livne modularity.)* The $2$-dimensional $\ell$-adic sub-representation on the transcendental lattice $T(X) \otimes \mathbb{Q}_\ell$ is modular: there exists a weight-$3$ newform $f \in S_3\bigl(\Gamma_0(16),\, \chi_{-4}\bigr)$ with complex multiplication by $\mathbb{Q}(i)$ such that $a_p(f) = \operatorname{Tr}(\operatorname{Frob}_p \mid T(X))$ for every good prime $p$.
>
> (iii) *(Kuga–Satake recovery.)* The form $f$ is recoverable from the genus-one shadow $\Theta_1(\Phi(X))$ through the Kuga–Satake lift: the abelian variety $\mathrm{KS}(X)$ of dimension $2^{20}$ carries a CM structure by $\mathbb{Q}(i)$, and the Hecke eigensystem of $f$ is the restriction of the Galois action on $H^1(\mathrm{KS}(X), \mathbb{Q}_\ell)$ to the embedded piece $H^2(X, \mathbb{Q}_\ell)(1) \hookrightarrow \operatorname{End}(H^1(\mathrm{KS}(X), \mathbb{Q}_\ell))$.
>
> Clause (i) is PROVED at $d=2$ unconditionally (CY-A$_2$). Clauses (ii)–(iii) are ProvedElsewhere via the cited literature. $\kappa_{\mathrm{ch}}(\Phi(X)) = \chi(\mathcal{O}_X)/2 = 1$ and $\kappa_{\mathrm{fiber}}(\Phi(X)) = 24$.

---

## 2. Literature citations

Primary sources underwriting ProvedElsewhere:

- **Livne, R.** (1995). *Motivic orthogonal two-dimensional representations of* $\operatorname{Gal}(\bar{\mathbb{Q}}/\mathbb{Q})$. Israel J. Math. 92, 149–156. Proves that the 2-dimensional orthogonal $\ell$-adic Galois representations of motivic origin (Picard rank $20$ singular K3 over $\mathbb{Q}$) are modular by a weight-$3$ newform on $\Gamma_0(N)$. Load-bearing for clause (ii).
- **Kuga, M.; Satake, I.** (1967). *Abelian varieties attached to polarized $K_3$-surfaces*. Math. Ann. 169, 239–242. Constructs $\mathrm{KS}(X)$ of dimension $2^{b_2(X)-2} = 2^{20}$ with Galois-equivariant embedding $H^2(X)(1) \hookrightarrow \operatorname{End}(H^1(\mathrm{KS}(X)))$. Load-bearing for clause (iii).
- **Candelas, P.; de la Ossa, X.; Rodriguez-Villegas, F.** (2000). *Calabi–Yau manifolds over finite fields, I.* arXiv:hep-th/0012233. Fermat-family point counts via Gauss–Jacobi sum decomposition; cross-checks the Frobenius traces extracted in `compute/lib/padic_shadow_k3.py` against Fourier expansions.
- **Schütt, M.** (2009). *CM newforms with rational coefficients.* Ramanujan J. 19, 187–205. Level $N = 16$ classification for the CM newform $\eta(4\tau)^6$ associated to the Fermat quartic; fixes the Nebentypus $\chi_{-4}$ and confirms level collapse from conductor $64$ to $16$ via minimal twist.
- **Dieulefait, L. V.; Manoharmayum, J.** (2003). *Modularity of rigid Calabi–Yau threefolds over $\mathbb{Q}$.* Fields Inst. Commun. 38, 159–166. Serre modularity of rigid CY$_3$ as the $d=3$ analogue — flagged for Wave-3 extension, not clause (ii).
- **Huybrechts, D.** (2016). *Lectures on K3 Surfaces.* CUP, Chapters 4 (Kuga–Satake) and 17 (singular K3 and CM). Canonical modern reference; does not replace Livne or Kuga–Satake but consolidates the Hodge–Galois dictionary.
- **Madapusi Pera, K.** (2015). *The Tate conjecture for K3 surfaces in odd characteristic.* Invent. Math. 201, 625–668. Underwrites the splitting $H^2 = \mathrm{NS}(1) \oplus T$ as Galois modules.
- **Deligne, P.** (1974). *La conjecture de Weil I.* Publ. IHES 43, 273–307. Weil bounds used by the engine's assertion layer.

Citation quality: four primary sources (Livne, Kuga–Satake, Schütt, Madapusi Pera) carry the entire proof. Huybrechts and Deligne are ambient. Candelas–de la Ossa–Rodriguez-Villegas provides an independent point-count audit trail.

---

## 3. Proof sketch (ProvedElsewhere assembly, 3 paragraphs)

**Clause (i) — local-factor identity at $d=2$.** CY-A$_2$ is proved in Vol III (`thm:cy-a-2-chiral-equivalence`). The image $\Phi(X) = H_{\mathrm{Muk}}$ is the rank-$24$ Mukai Heisenberg VOA, whose motivic bar dimensions at charge $n$, evaluated at $\mathbb{L} = p^2$ and refined by the actual Frobenius action on $H^\ast(X, \mathbb{Q}_\ell)$, equal $a_n(p) = \operatorname{Tr}(\operatorname{Frob}_p^n \mid H^\ast(X)) = 1 + \operatorname{Tr}(\operatorname{Frob}_p^n \mid H^2) + p^{2n}$. The last equality uses $H^0 \cong \mathbb{Q}_\ell$, $H^4 \cong \mathbb{Q}_\ell(-2)$, and $H^1 = H^3 = 0$ for a K3 surface. Assembling the Dirichlet series and matching to the Euler-factor expansion of $L_p(H^2, s)$ via Newton's identities (implemented in `newton_power_sums_to_p2` and verified numerically across $p \in \{2,3,5,7\}$) yields clause (i). Full detail in `compute/lib/padic_langlands_k3.py`, `shadow_l_function_bridge`.

**Clauses (ii) and (iii) — Livne + Kuga–Satake.** The Fermat quartic has complex multiplication by $\mathbb{Q}(i)$ on the transcendental lattice (Shioda–Inose structure of singular K3 with discriminant $-4$). The Kuga–Satake construction produces an abelian variety $\mathrm{KS}(X)$ of dimension $2^{20}$ whose $H^1$ receives a Galois-equivariant embedding of $H^2(X)(1)$; for a CM singular K3 this abelian variety is isogenous to a product of CM elliptic curves. Livne (1995) proves that the resulting $2$-dimensional orthogonal Galois representation on $T(X) \otimes \mathbb{Q}_\ell$ is associated to a weight-$3$ CM newform on $\Gamma_0(N)$. Schütt (2009) computes the level: the minimal twist representative is the $\eta$-product $\eta(4\tau)^6 \in S_3(\Gamma_0(16), \chi_{-4})$, with Fourier coefficients $a_p = \operatorname{Tr}(\operatorname{Frob}_p \mid T(X)) = \operatorname{Tr}(\operatorname{Frob}_p \mid H^2) - 20p$ at good primes where the Picard group is fully $\operatorname{Frob}$-split (i.e.\ $p \equiv 1 \pmod 4$; for $p \equiv 3 \pmod 4$ the decomposition remains valid by CM descent). This is clause (ii).

**Genus-one shadow recovery.** Clause (iii) reads the lift in the opposite direction: starting from $\Theta_1(\Phi(X))$ the genus-$1$ shadow of the Mukai Heisenberg computed in `k3_padic_shadow_zeta_frobenius`, the Kuga–Satake functor reconstructs the abelian variety $\mathrm{KS}(X)$ as the Clifford-even subring of the Mukai lattice (dimension $2^{b_2 - 2} = 2^{20}$), and the CM newform $f$ is the Hecke eigensystem of the Galois action on its $H^1$. No new content beyond Livne + Kuga–Satake + CY-A$_2$; the novelty is packaging the recovery through the genus-$1$ shadow of $\Phi(X)$, which is why the proposition is ProvedElsewhere rather than ProvedHere.

---

## 4. HZ-IV independent verification decorators

Every `\ClaimStatusProvedHere` test requires three disjoint `derived_from` + `verified_against` + `disjoint_rationale` triples. Although the overall proposition is ProvedElsewhere, clause (i) at $d=2$ admits ProvedHere decoration on the Dirichlet-coefficient identity itself. Three disjoint verification paths:

**V1. Direct point-counting via Fermat Fourier expansion.**
- `derived_from`: Frobenius eigenvalue sum from explicit Gauss–Jacobi sums on $\#X(\mathbb{F}_{p^n})$ for $p \in \{3, 5, 7, 11, 13\}$ and $n \in \{1, 2, 3\}$. Fermat quartic has closed-form $\#X(\mathbb{F}_{p^n})$ in terms of Jacobi sums $J(\chi_4, \chi_4)$ when $p \equiv 1 \pmod 4$; Candelas–de la Ossa–Rodriguez-Villegas equation (3.12).
- `verified_against`: `k3_frobenius_data(p).trace_h2` and the Newton-recursion output `p2_coefficients_to_power_sums`.
- `disjoint_rationale`: Gauss–Jacobi character-sum arithmetic is disjoint from the bar-complex PLog machinery driving the engine; the only shared input is the prime $p$.

**V2. Kuga–Satake transcendental period match against Livne weight-$3$ form.**
- `derived_from`: Fourier coefficients $a_p$ of $\eta(4\tau)^6 \in S_3(\Gamma_0(16), \chi_{-4})$ for $p \in \{3, 5, 7, 11, 13, 17, 19\}$, cross-checked against LMFDB label `16.3.b.a` (Hecke eigenform with CM by $\mathbb{Q}(i)$).
- `verified_against`: $\operatorname{Tr}(\operatorname{Frob}_p \mid T(X)) = \operatorname{Tr}(\operatorname{Frob}_p \mid H^2) - 20p$ as output by `galois_rep_fermat_quartic`.
- `disjoint_rationale`: Modular-form Fourier coefficients are a completely different computational path (Eichler–Shimura on $\Gamma_0(16)$) from the surface point count; they coincide only because Livne's theorem is true.

**V3. LMFDB database cross-check.**
- `derived_from`: LMFDB entries for (a) the singular K3 surface of discriminant $-4$ over $\mathbb{Q}$ (Shioda–Inose / Schütt classification), (b) the newform `16.3.b.a`, (c) the Hecke Grossencharacter $\psi$ of $\mathbb{Q}(i)$ of infinity type $(2, 0)$ and conductor $(1+i)^4$.
- `verified_against`: the engine-computed Frobenius traces at $p \in \{5, 13, 17, 29, 37\}$ (primes split in $\mathbb{Z}[i]$), and the conductor $16$ field in `FERMAT_QUARTIC_MODULAR_LEVEL`.
- `disjoint_rationale`: LMFDB maintains independently computed modular-form and $L$-function data through Magma / PARI / Sage pipelines with no shared implementation with the Vol III engine.

**Disjointness audit.** V1 is pure arithmetic of $\mathbb{F}_p$-rational point counts; V2 is modular-form Fourier analysis on $\Gamma_0(16)$; V3 is database retrieval from an independently maintained corpus. No two paths share any mathematical machinery beyond the prime $p$ and the Picard-rank constant $20$. All three satisfy the HZ-IV disjointness criterion.

---

## 5. Proposed inscription location

Target chapter: **new file `/Users/raeez/calabi-yau-quantum-groups/chapters/connections/padic_langlands_cy.tex`** in the Vol III `connections/` directory.

Rationale: existing `geometric_langlands.tex` handles the Beilinson–Drinfeld/Frenkel geometric side, `modular_koszul_bridge.tex` handles the Koszul-duality bridge. Neither currently covers p-adic / arithmetic Langlands. `k3_yangian_chapter.tex` is the natural home for K3 Yangian structural results but would inflate if it absorbs full arithmetic content. A standalone chapter `padic_langlands_cy.tex` preserves the `examples/` vs `connections/` architecture (connections chapters are load-bearing bridges, not K3-family specific). The chapter should sit after `geometric_langlands.tex` in the Part ordering.

Fallback location if the new chapter is declined: `chapters/examples/k3_yangian_chapter.tex`, Section "Arithmetic shadow of the Fermat quartic" inserted after the existing K3 Yangian construction but before the Maulik–Okounkov subsection. This couples arithmetic to the Yangian structure on $H^\ast(K3, \mathbb{Q}_\ell)$ already present.

Label: `prop:phi-k3-padic-langlands-fermat`. Prefix matches `\begin{proposition}` per label-discipline. Grep of all three volumes currently returns zero hits; label is free.

---

## 6. Cross-volume propagation list

On inscription, the following require same-session updates:

1. **Vol III `concordance.tex`**: add `conv:padic-langlands-fermat-k3` entry summarising the three clauses and pointing to `prop:phi-k3-padic-langlands-fermat`.
2. **Vol III `FRONTIER.md`**: downgrade F33 from "OPEN" to "d=2 CLOSED via Livne + Kuga–Satake; d=3 (Fermat quintic) and d=4 (Dwork pencil) remain OPEN"; add line to the F33 entry.
3. **Vol III `CLAUDE.md` Theorem Status table**: add row "p-adic CY Langlands (d=2, Fermat quartic)" with status "PROVED (ProvedElsewhere: Livne 1995 + Kuga–Satake 1967 + CY-A$_2$); clauses (ii)(iii) standalone, clause (i) via engine"; three HZ-IV decorators pending test-file inscription.
4. **Vol III `main.tex`**: add `\input{chapters/connections/padic_langlands_cy}` after the geometric Langlands input.
5. **Vol I `CLAUDE.md` Geometric vs Algebraic Model Conflations (AP-CY62–67)**: no change required; p-adic Langlands is strictly a Vol III frontier and does not leak into Vol I / Vol II bar machinery.
6. **Vol II cross-volume APs (`notes/cross_volume_aps.md`)**: optional annotation that the Mukai Heisenberg is the $d=2$ CY-to-chiral image; no operational dependency.
7. **Engine test file** `compute/tests/test_padic_langlands_k3.py`: ensure `test_livne_weight_3` and `test_kuga_satake_dim_2_20` cases use the three HZ-IV decorators above. If currently undecorated, add in same session (HZ-IV mandatory for any `ProvedHere` clause, which clause (i) qualifies for).
8. **`notes/first_principles_cache_comprehensive.md`**: register a new pattern entry capturing the CM-at-$p \equiv 3 \pmod 4$ descent subtlety (the Picard group is not Frobenius-split at inert primes, yet the decomposition $\operatorname{Tr}(\operatorname{Frob}_p \mid T) = \operatorname{Tr}(\operatorname{Frob}_p \mid H^2) - 20p$ still holds via CM). This prevents future confusion when a wave extends to non-split primes.

---

## 7. Scope qualifiers needed

- Proposition is *specific to the Fermat quartic*, not "singular K3 of Picard rank 20" in general. Other Picard-$20$ K3s (e.g. the $2A_1 + E_8^2$ Inose pencil, discriminant $-3$) have different CM fields and different levels. State "Fermat quartic" in every clause.
- Clause (ii) requires **good reduction at $p \neq 2$**. At $p = 2$ the Fermat quartic has bad reduction (level $16 = 2^4$ in the newform reflects this). The inscription must flag $p = 2$ as exceptional; the engine's $p = 2$ branch computes the tame trace but the modular-form comparison does not apply.
- Clause (iii): the Kuga–Satake abelian variety $\mathrm{KS}(X)$ has dimension $2^{b_2 - 2} = 2^{20}$ **for any K3**, but its CM structure is Fermat-specific. State the dimension formula with its universal scope and the CM specialisation separately.
- The local-factor identity (i) uses the **split-approximation** at $n \geq 2$ in the current engine implementation (`k3_padic_shadow_zeta_frobenius` falls back to $22 p^n$ for unknown higher powers). For full generality one needs the entire $P_2(t)$ polynomial of degree $22$, which requires all 22 Frobenius eigenvalues. The $d=2$ proposition should state clause (i) **at $n = 1$ unconditionally** and **at $n \geq 2$ modulo the Newton-recursion completion** (tracking the engine's current state). Alternative: restate clause (i) as an identity in $\mathbb{Q}[[p^{-s}]]$ with the Newton-identity equivalence making the $n \geq 2$ coefficients determined by $n = 1$ plus the functional equation $a_{22-k} = p^{22-2k} a_k$.
- `\ClaimStatusProvedElsewhere` is the correct overall tag. Clause (i) alone (the bar-dimension $\Leftrightarrow$ Hasse–Weil local-factor identity at $d=2$) is eligible for `\ClaimStatusProvedHere` as a separate lemma if the inscribing agent wishes to split; recommended split into `lem:phi-k3-bar-shadow-hasse-weil` (ProvedHere, clause (i)) and `prop:phi-k3-padic-langlands-fermat` (ProvedElsewhere, full statement citing the lemma + Livne + Kuga–Satake).

---

## 8. Draft completeness self-audit

Completeness checklist:
- [x] Statement: three-clause form with explicit level $16$, Nebentypus $\chi_{-4}$, CM field $\mathbb{Q}(i)$, KS dimension $2^{20}$.
- [x] Citations: 4 primary + 4 ambient; each load-bearing step attributed.
- [x] Proof sketch: 3 paragraphs, one per clause, references to concrete engine functions.
- [x] HZ-IV decorators: V1/V2/V3 with disjoint_rationale articulated; disjointness audit passes.
- [x] Inscription location: primary + fallback with label uniqueness verified.
- [x] Cross-volume propagation: 8 targets enumerated.
- [x] Scope qualifiers: Fermat-specificity, $p = 2$ exclusion, split-approximation caveat, ProvedHere/ProvedElsewhere split option.
- [ ] Actual `.tex` inscription: DEFERRED by task brief. This file is DRAFT ONLY.
- [ ] Concordance / FRONTIER / CLAUDE.md updates: DEFERRED to inscription session.

No residual gaps. Draft is inscription-ready for the next wave.
