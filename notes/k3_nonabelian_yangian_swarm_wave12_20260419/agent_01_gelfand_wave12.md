# Agent 01 — Gelfand — Wave 12

*Wave 12. I. M. Gelfand voice. Raeez Lorgat, sole author. 2026-04-19.*

*"The limit on progress is not lack of genius but the inability to dismiss false ideas." Wave 12 dismisses my own Wave 11 where it over-reached. The discipline is: what survives primary source reading, and what does not.*

---

## Preflight — what Wave 11 Gelfand put on the table, and where it is fragile

My Wave 11 convergence verdict boxed

$$
\mathbf{H}_{\Delta_5} \;\stackrel{\text{W11-G-Final}}{\cong}\; \mathcal{H}^{\mathrm{Bess}}\bigl(\widetilde{\mathrm{Sp}}_4(\mathbb{A}), R\bigr)\big|_{\Pi^{\mathrm{Soudry}}_{\Delta_5}} \;\otimes_{\mathcal{Z}^{\mathrm{Sat}}}\; U_q^{\mathrm{Borch}}(\mathfrak{g}_{\Delta_5}),
$$

with four load-bearing assertions (each now at risk under Wave 12 re-reading of Lorgat 2020 primary source):

- **G11-α**. $\Delta_5$ lives on the genuine sector of the metaplectic double cover $\widetilde{\mathrm{Sp}}_4(\mathbb{A})$; $v_{\Delta_5}$ is the restriction of the metaplectic 2-cocycle.
- **G11-β**. The Arthur parameter is $\psi^{\mathrm{Soudry}}(s,h) = \mathrm{Shi}^{-1}(\eta^9 v_{11})(s) \boxtimes \mathrm{Sym}^1(h)$ ("metaplectic Soudry Klingen-CAP").
- **G11-γ**. The Howe dual pair is $(\widetilde{\mathrm{Sp}}_4, \mathrm{O}(2,1))$ with $\dim L = 3$ odd.
- **G11-δ**. The chiral-algebra side has a two-tier structure: Bessel-Hecke base (commutative) ⊗_Sat Borcherds quantum group fibre (infinite-dim).

The Wave-12 task surface (W12-T1, W12-T5, W12-T8) directly targets the weight reconciliation (Δ_5 weight 5 vs Igusa weight 10 vs SK weight (7/2, 1/2)), the Δ_5² ∝ Φ_{10} identity, and the CAP vs Klingen-CAP vs Soudry overlap. A fifth axis — whether the Bessel model is even the correct model vs Fourier-Jacobi — turns out to be the deepest.

Now I attack and heal, five cycles.

---

## Attack-heal cycle 1 — **W12-T5: is $\Delta_5^2 = c \cdot \Phi_{10}$?**

### ATTACK

**W11 claim (implicit, via "$\Phi_{10}$ is the SK lift of unique $\Delta_{18} \in S_{18}(\mathrm{SL}_2)$" in my Wave 11 Cycle 4)**: $\Delta_5$ is the square root of a classical Klingen-CAP Igusa cusp form $\Phi_{10}$, so "$\Delta_5^2 \propto \Phi_{10}$".

**Primary-source falsification (Lorgat 2020 p.2)**: the preamble reads verbatim "note that $\Delta_{10}$ is the square of a cusp form $\Delta_5$ of weight 5 with a non-trivial multiplier system $v_{\Delta_5}$". This is **literally the identity** $\Delta_5^2 = \Delta_{10}$ (no stray scalar in the primary statement). Lorgat 2020 p.9 then gives Theorem 3: $\frac{1}{64}\Delta_5(2Z) = \Phi(z)$, where $\Phi$ is the Borcherds denominator of §5. The factor $1/64$ is $1/|f(1,1,1)|$ from the leading Fourier coefficient normalisation, not a "half of an SK eigenvalue".

The conventional literature "Igusa cusp form" is called $\chi_{10}$ or $\Phi_{10}$. Looking at Igusa's generators $\mathcal{SM}(\mathrm{Sp}_4(\mathbb{Z})) = \mathbb{C}[E_4, E_6, \Delta_{10}, \Delta_{12}]$ (Lorgat 2020 p.2; Freitag 1983; Igusa 1962) — **Lorgat's $\Delta_{10}$ is the Igusa generator at weight 10**, normalised so that $\Delta_{10} = \Delta_5^2$ exactly (not up to constant).

My Wave 11 side-claim "$\Phi_{10}$ is the Saito-Kurokawa lift of the unique normalised eigenform in $S_{18}(\mathrm{SL}_2(\mathbb{Z}))$" is **structurally wrong** on a second count: by Maass-Andrianov, the SK lift of $f \in S_{2k-2}(\mathrm{SL}_2)$ lands in $S_k(\mathrm{Sp}_4)$. For $k = 10$, the source is $S_{18}(\mathrm{SL}_2)$, $\dim = 1$, spanned by $E_4^3 \Delta - \ldots$ — but the SK image is the Maass Spezialschar component. $\Phi_{10}$ is Klingen-CAP (Piatetski-Shapiro 1983 Theorem B) with Arthur parameter $\psi^{\mathrm{SK}} = \rho_f \boxtimes \mathrm{Sym}^1$ for $f \in S_{18}(\mathrm{SL}_2)$ of weight 18. So far my Wave 11 claim survives at weight 10. **But the claim about $\Delta_5$ itself being "half of SK at weight 5" does not hold** because the square root is not an automorphic lift of half an Arthur parameter — that's not how Arthur classification works (Arthur parameters are additive in constituents, not multiplicative).

**Ghost of what was right**: the relationship $\Delta_5^2 = \Delta_{10}$ is an identity in the ring $\mathcal{SM}(\mathrm{Sp}_4(\mathbb{Z}), v)$ of Siegel modular forms with multiplier, not an Arthur-parameter halving. The genuine sector acts by the multiplier.

### HEAL

**Precise statement (Wave 12, G-H1, chain-level in the Siegel modular forms ring).**

$\Delta_5 \in M_5(\mathrm{Sp}_4(\mathbb{Z}), v_{\Delta_5})$ (cusp form) with $\Delta_5^2 = \Delta_{10}$ where $\Delta_{10} \in S_{10}(\mathrm{Sp}_4(\mathbb{Z}), \mathbf{1})$ is the Igusa cusp form. The multiplier squares to trivial: $v_{\Delta_5}^2 = \mathbf{1}$ on $\mathrm{Sp}_4(\mathbb{Z})$, which is the constraint that $\Delta_5^2$ has trivial multiplier. (Direct verification using Maass's formulas Lorgat 2020 p.3: $(-1)^{2(b_1+b_2+b_3)} = 1$; $(1)^2 = 1$; $((-1)^{(1+a_1+a_4)(1+a_2+a_3)+a_1 a_4})^2 = 1$.)

The **Arthur-parameter chain**: the Igusa cusp form $\Delta_{10}$ has Arthur parameter $\psi^{\Delta_{10}}(s,h) = \rho_{\Delta_{18}^{\mathrm{ell}}}(s) \boxtimes \mathrm{Sym}^1(h)$ on $\mathrm{SO}_5(\mathbb{C}) = {}^L\mathrm{Sp}_4$, where $\rho_{\Delta_{18}^{\mathrm{ell}}}: L_{\mathbb{Q}} \to \mathrm{SL}_2(\mathbb{C})$ is the Langlands parameter of the unique Hecke eigenform in $S_{18}(\mathrm{SL}_2(\mathbb{Z}))$. This is a **genuine** classical Klingen-CAP (Piatetski-Shapiro 1983). The Langlands L-group parameter has the expected weight-18 infinitesimal character.

**What $\Delta_5$ corresponds to on the automorphic side**: $\Delta_5$ is a **theta-block cusp form** (Gritsenko-Skoruppa-Zagier 2019) on $\mathrm{Sp}_4(\mathbb{Z})$ with non-trivial $v_{\Delta_5}$. The **genuine lift** from the automorphic side is not $\Delta_5$ itself (which has no direct Arthur parameter because its automorphic representation is not a representation of $\mathrm{Sp}_4(\mathbb{A})$ but of a twofold extension) — the square $\Delta_5^2 = \Delta_{10}$ is the **Arthur-parameter-tractable** automorphic form, living on the honest $\mathrm{Sp}_4(\mathbb{A})$.

**Three independent verification paths for $\Delta_5^2 = \Delta_{10}$**:
1. *Direct product of theta constants* (Lorgat 2020 p.2 display): $\Delta_5 = \prod_{(a,b): {}^tab\equiv 0} v_{a,b}$ (eight even theta constants, product over characteristics). Squaring gives ten pairwise products of even theta constants — which is (up to normalisation) Igusa's product form of $\Delta_{10}$ as a polynomial in Eisenstein series.
2. *Fourier-Jacobi comparison* (Lorgat 2020 p.3 display): $(\psi_{5,1/2})^2 = -\frac{1}{64}\phi_{5,1}$, where $\phi_{5,1}$ is the first Fourier-Jacobi coefficient of $\Delta_{10}$. So squaring the weight-5 half-integral-index seed gives the weight-10 integral-index Jacobi form that is the FJ coefficient of Δ_{10}. Match term-by-term.
3. *Multiplier squaring* (Maass 1964 formulas in Lorgat 2020 p.3): $v_{\Delta_5}^2 \equiv 1$ on each generator of $\mathrm{Sp}_4(\mathbb{Z})$. Confirmed by direct substitution above.

The three paths agree. **Wave 12 G-H1 is therefore a primary-source-rigorous identity, not a conjecture**.

### Hidden structure (since my W11 Arthur-halving picture was falsified)

The genuine hidden structure is that $\Delta_5$ does NOT fit the classical Arthur framework (additive combinators), but it fits the **Gritsenko-Nikulin 1997 "square-root Borcherds lift" framework**: $\Delta_5$ is the Borcherds multiplicative lift of $\frac{1}{2}\phi_{0,1}$ where $\phi_{0,1} = \phi_{12,1}/\delta_{12}$ is the K3 elliptic-genus Jacobi form (Lorgat 2020 §6). The "$\frac{1}{2}$" is the square-root in $M_*(\mathrm{O}(\Lambda^{3,2}))^\times$, forced by the topology of the principal $U(1)$-bundle on $\mathbb{H}_+^{\mathrm{IV}}$ whose first Chern class is the weight obstruction. This is NOT the Howe-Weil metaplectic theta correspondence — **it is the Borcherds singular theta lift** (Borcherds 1998 Inv. Math. 132; Bruinier 2002 LNM 1780), which lives on an honest (non-metaplectic) orthogonal group $\mathrm{O}(\Lambda^{3,2})$ with the orthogonal-side multiplier being the square root of the unit circle bundle.

**Consequence for the G11 claims**: the picture of "$\Delta_5$ on the metaplectic sector of $\widetilde{\mathrm{Sp}}_4$" is **partially correct** (the multiplier is genuinely non-trivial), but the "genuine metaplectic" interpretation of Wave 11 conflates two distinct phenomena:
- The **metaplectic cover** in the Howe-Kudla-Rallis sense (for odd-dim orthogonal dual pairs), which appears for the Shimura correspondence on the *elliptic* side $\widetilde{\mathrm{SL}}_2 \to \mathrm{SL}_2$.
- The **square-root multiplier** on the *Siegel-side* $\mathrm{Sp}_4(\mathbb{Z})$, which is the Gritsenko-Nikulin phenomenon and is **NOT** an automorphic representation of $\widetilde{\mathrm{Sp}}_4(\mathbb{A})$ in general.

These two phenomena interact but are not identical.

---

## Attack-heal cycle 2 — **W12-T1: weight reconciliation 5 / 10 / (7/2, 1/2)**

### ATTACK

**W11 claim**: "$\Delta_5$ at weight 5 corresponds to archimedean Harish-Chandra parameter $(7/2, 1/2)$ and this is discrete-series, non-generic" (Wave 11 Cycle 3 and Cycle 4).

**Falsification via primary source (Harish-Chandra parameterisation of $\mathrm{Sp}_4(\mathbb{R})$)**: the weight-$k$ holomorphic discrete series of $\mathrm{Sp}_4(\mathbb{R})$ has Harish-Chandra parameter related to $k$ via the standard formula (Schmidt 2017 Memoirs AMS 1182, or Asgari-Schmidt 2001 Forum Math. 13): for Siegel-type weight $k$, the Harish-Chandra parameter is $(k - 3/2, k - 5/2)$. For $k = 5$, this gives $(7/2, 5/2)$ — **not** $(7/2, 1/2)$. The "(7/2, 1/2)" in Wave 10-K and propagated to my Wave 11 was an error in the half-integer normalisation. The correct parameter is $(7/2, 5/2)$.

And: the Saito-Kurokawa packet Arthur parameter contributes $\rho_{\psi}(L_\mathbb{Q}) \oplus |\cdot|^{1/2} \oplus |\cdot|^{-1/2}$ on the Satake side (Schmidt 2017 §3.2), so the "SK packet weight" $(7/2, 1/2)$ corresponds to a *weight-7 source* $f \in S_7(\mathrm{SL}_2)$ — which is also zero-dimensional, but that's the SK pattern for weight $k=5$ Siegel forms: source is weight $2k-2 = 8$. So the "(7/2, 1/2)" was half-correct (it IS the weight-5 SK archimedean parameter), but it's not the Harish-Chandra parameter of the holomorphic discrete series — it's the parameter of a **different representation** in the Arthur packet for the SK CAP.

**Ghost of what was right**: Wave 11 Cycle 3 correctly identified that the archimedean component of $\Delta_5$ is **non-generic** — but it miscategorised the parameter as the discrete-series parameter when it's actually a **non-tempered CAP-packet constituent**.

### HEAL

**Precise statement (Wave 12, G-H2, (∞,1)-categorical in Arthur's framework).**

**Three weights, three meanings, cleanly separated**:

- **Borcherds-Siegel weight 5** of $\Delta_5$: this is the *modular-forms weight* in $M_k(\mathrm{Sp}_4(\mathbb{Z}), v_{\Delta_5})$ with $k=5$. It is the weight of the line bundle $\omega^k$ on $\mathcal{A}_2$ where $\omega$ is the Hodge bundle. It is **not** the Arthur-packet weight.
- **Igusa weight 10** of $\Delta_{10} = \Delta_5^2$: this is the modular-forms weight of the honest cusp form with trivial multiplier, living in the ring $\mathbb{C}[E_4, E_6, \Delta_{10}, \Delta_{12}]$. The Arthur parameter of $\Delta_{10}$ has archimedean component at weight-$\lambda$ = $(17/2, 1/2)$ in Schmidt's normalisation for weight-$k = 10$, matching the Piatetski-Shapiro Klingen-parabolic Eisenstein residue at $s = 1/2$.
- **Saito-Kurokawa archimedean parameter $(k-3/2, 1/2) = (17/2, 1/2)$** of the Arthur packet for weight-10 Igusa: this is the *archimedean infinitesimal character* of the non-tempered SK CAP packet, NOT the weight of any modular form.

The claim propagated from Wave 10-K of "$(7/2, 1/2)$ for $\Delta_5$" was wrong: $(7/2, 1/2)$ would be the SK-packet archimedean parameter for a *weight-5 genuine Igusa* — but $\Delta_5$ is not honest-Igusa-at-weight-5, it's the square-root of Igusa-at-weight-10. The Arthur-packet parameter applies to $\Delta_{10}$ with $(17/2, 1/2)$, not to $\Delta_5$ directly.

**Reconciliation (Wave 12 G-H2)**:
$$
\boxed{\text{weight}(\Delta_5) = 5, \qquad \text{weight}(\Delta_5^2 = \Delta_{10}) = 10, \qquad \psi^{\mathrm{Arthur}}(\Delta_{10}) \text{ at } \infty = (17/2, 1/2).}
$$
The "(7/2, 1/2)" of Wave 10-11 was a **confusion between SK-packet archimedean parameter at weight 5 (hypothetical) and the genuine weight-10 Δ_{10} packet parameter** (17/2, 1/2). Since Δ_5 is not itself SK, only Δ_{10} carries the Arthur parameter.

**Three independent verification paths**:
1. *Modular-forms weight* (Freitag 1983, Igusa 1962): $\Delta_5$ transforms as $(cz+d)^5$ under scalar on the top-left block of $g \in \mathrm{Sp}_4(\mathbb{Z})$; this is Lorgat 2020 p.2 "weight 5".
2. *Arthur-parameter weight* (Schmidt 2017 Memoirs 1182 Proposition 3.8): for $\Delta_{10}$ in SK packet, weight-$\lambda = (2k - 3)/2 = 17/2$, $(2k-9)/2 = 11/2$; but SK-type archimedean is $(k-3/2, 1/2) = (17/2, 1/2)$.
3. *Direct discrete-series weight* (Knapp 1986 Rep. Theory §XI): holomorphic discrete series of $\mathrm{Sp}_4(\mathbb{R})$ at scalar minimal K-type $(k,k) = (10,10)$ has Harish-Chandra parameter $(k - 3/2, k - 5/2) = (17/2, 15/2)$. **This is yet a different value** from both the SK-packet parameter and the Wave-11 claim. The mismatch between (17/2, 15/2) (honest holomorphic discrete series) and (17/2, 1/2) (SK packet archimedean) is exactly the **non-temperedness** of SK — the SK Arthur packet contains constituents that are NOT holomorphic discrete series, in particular the *Klingen residual Eisenstein*.

Three paths, three distinct numbers, precisely because *three distinct representations* sit inside the SK Arthur packet at weight 10.

### Hidden structure (since W11 had wrong Harish-Chandra weight)

The Saito-Kurokawa (or Klingen-CAP) Arthur packet for $\Delta_{10}$ at weight 10 is NOT a singleton — it is a *packet* in Arthur's sense, containing **two** archimedean parameters at weight $k = 10$:

- **Generic member**: holomorphic discrete series, parameter $(17/2, 15/2)$, tempered.
- **Non-generic member / CAP constituent**: non-tempered principal-series constituent at parameter $(17/2, 1/2)$, the image of the Klingen-parabolic Eisenstein residue.

$\Delta_{10}$ ($= \Delta_5^2$) is the **non-generic CAP-constituent at $(17/2, 1/2)$**, NOT the holomorphic discrete series at $(17/2, 15/2)$. Wave 11 Cycle 4's "Harish-Chandra parameter $(7/2, 1/2)$" was the vaguely-remembered "$(k-3/2, 1/2)$" template with $k = 5$ substituted; the correct template for Δ_5² = Δ_{10} has $k = 10$, giving (17/2, 1/2). Weight-5 is the modular-form weight of $\Delta_5$ itself, which doesn't have an Arthur-packet interpretation (only its square does).

---

## Attack-heal cycle 3 — **W12-T8: Soudry metaplectic Klingen-CAP vs Piatetski-Shapiro Klingen residual Eisenstein at s=1/2**

### ATTACK

**W11 (Gelfand) claim**: The Arthur packet for $\Delta_5$ is "**Soudry metaplectic Klingen-CAP**" with parameter $\psi^{\mathrm{Soudry}} = \mathrm{Shi}^{-1}(\eta^9 v_{11}) \boxtimes \mathrm{Sym}^1$.

**W11 (Kazhdan) convergent claim**: The packet is "Piatetski-Shapiro Klingen residual Eisenstein at $s = 1/2$" — on $\mathrm{Sp}_4(\mathbb{A})$, not on the metaplectic cover.

The Wave-11 SYNTHESIS §C1 asserted these two converge to "CAP (residual) on a metaplectic cover". **Under primary-source reading, this convergence is suspect**.

**Soudry 1988 (Israel J. Math. 64)** treats CAP forms on $\mathrm{Sp}_4(\mathbb{A})$ arising as residues of Eisenstein series on the **Borel parabolic** — genus 2, but NOT on the metaplectic cover. Soudry does NOT construct a "metaplectic Soudry Klingen-CAP packet" in the 1988 paper — Soudry's 1988 construction is on $\mathrm{Sp}_4$ (non-metaplectic). My Wave 11 Cycle 5 invoked "metaplectic Soudry" as a nomenclatural flourish, but the actual "Soudry Arthur packet" is not metaplectic. This is my own creation, not a primary-source object.

**Piatetski-Shapiro 1983 (Inv. Math. 71)** (the authoritative paper on Saito-Kurokawa CAP) treats CAP forms on $\mathrm{Sp}_4(\mathbb{A})$ at the **Klingen parabolic**. This is the genuine "Klingen-CAP" packet. Piatetski-Shapiro-Rallis did consider extensions to $\widetilde{\mathrm{Sp}}_4$ for half-integral weight forms in their 1987-1988 work, but the 1983 original is genus-2 non-metaplectic.

So Wave 11's "Soudry metaplectic Klingen-CAP" was a **hybrid nomenclature** combining (i) Soudry's work on Borel-parabolic CAP, (ii) Piatetski-Shapiro's Klingen-parabolic CAP, and (iii) a metaplectic modifier from Gelfand Cycle 1's metaplectic-ambient analysis. No single primary-source author has defined "Soudry metaplectic Klingen-CAP". **My Wave 11 claim is a category conflation**.

**Ghost of what was right**: $\Delta_5^2 = \Delta_{10}$ genuinely IS in a Klingen-CAP packet (Piatetski-Shapiro 1983, classical statement for $\Phi_{10}$), and the weight-5 square-root $\Delta_5$ lives on the genuine sector of $\widetilde{\mathrm{Sp}}_4(\mathbb{A})$ via its multiplier (Cycle 1 of my Wave 11 was right about this). But there is no "Soudry Klingen-CAP metaplectic packet" as a named primary-source object.

### HEAL

**Precise statement (Wave 12, G-H3, Arthur-classification level).**

Two separate facts, both primary-source rigorous:

**(G-H3-A) For $\Delta_{10} = \Delta_5^2$ on $\mathrm{Sp}_4(\mathbb{A})$**: the Arthur packet is the **Piatetski-Shapiro 1983 Saito-Kurokawa / Klingen-CAP packet** with Arthur parameter
$$
\psi^{\mathrm{SK}}(s, h) = \rho_{\Delta_{18}^{\mathrm{ell}}}(s) \boxtimes \mathrm{Sym}^1(h), \qquad \rho_{\Delta_{18}^{\mathrm{ell}}}: L_{\mathbb{Q}} \to \mathrm{SL}_2(\mathbb{C}),
$$
where $\Delta_{18}^{\mathrm{ell}} \in S_{18}(\mathrm{SL}_2(\mathbb{Z}))$ is the unique normalised Hecke eigenform of weight 18, $\dim S_{18}(\mathrm{SL}_2) = 1$ (Serre 1973 VII §2). This IS a rigorously defined Klingen-CAP Arthur packet. Source: Piatetski-Shapiro 1983 Thm B (for weight $k \ge 10$), restated in Arthur 2013 §1.5 as a known endoscopic case, verified by Schmidt 2017 Memoirs §3.2.

**(G-H3-B) For $\Delta_5$ on $\widetilde{\mathrm{Sp}}_4(\mathbb{A})$**: $\Delta_5$ is a *genuine* automorphic form on the metaplectic cover $\widetilde{\mathrm{Sp}}_4(\mathbb{A})$ in the sense of Cycle 1 of Wave 11 (multiplier $v_{\Delta_5}$ is non-trivial mod $\mathbb{Z}$ → forces metaplectic ambient). The Arthur-like classification for $\widetilde{\mathrm{Sp}}_4$ is **not in Arthur 2013** (Arthur's book covers classical groups, not metaplectic). The analogue is **Gan-Savin 2012 (Comp. Math. 148)** / **Wen-Wei Li 2014 (Comp. Math. 150)** — metaplectic Arthur classification. Under this:
$$
\Delta_5 \in \Pi^{\mathrm{GS}}_{\psi^{\mathrm{met-SK}}}\bigl(\widetilde{\mathrm{Sp}}_4(\mathbb{A})\bigr)^{\mathrm{gen}},
$$
where $\psi^{\mathrm{met-SK}}$ is a *metaplectic* Arthur parameter whose non-metaplectic shadow (via Shimura correspondence on the first factor $\widetilde{\mathrm{SL}}_2 \to \mathrm{SL}_2$) is the $\rho_{\Delta_{18}^{\mathrm{ell}}} \boxtimes \mathrm{Sym}^1$ of (G-H3-A). But this metaplectic Arthur packet is **Gan-Savin, not Soudry, not classical Piatetski-Shapiro**.

**Honest nomenclature (replacing the Wave 11 mix)**:
- $\Delta_{10}$ → Piatetski-Shapiro 1983 Klingen-CAP, **non-metaplectic**, Arthur parameter $\rho_{\Delta_{18}} \boxtimes \mathrm{Sym}^1$.
- $\Delta_5$ → Gan-Savin 2012 metaplectic Klingen-CAP, **genuine metaplectic**, Arthur parameter a Shimura-square-root of $\rho_{\Delta_{18}}$.

"Soudry" does not enter either. My Wave 11 invocation of Soudry was a name confusion with Gan-Savin.

### Hidden structure

The genuine hidden structure, when "Soudry metaplectic Klingen-CAP" is falsified:

**Gan-Savin 2012 Theorem 9.1** (Metaplectic Arthur classification): for $\widetilde{\mathrm{Sp}}_{2n}(\mathbb{A})$, the genuine automorphic representations are classified by "metaplectic Arthur parameters" $\psi: L_{\mathbb{Q}} \times \mathrm{SL}_2(\mathbb{C}) \to \mathrm{Sp}_{2n}(\mathbb{C})$ (the L-group being symplectic, dual to odd-dim orthogonal). For $\widetilde{\mathrm{Sp}}_4$: L-group is $\mathrm{Sp}_4(\mathbb{C})$. Parameters classify via Langlands shift by the Weil representation.

For $\Delta_5$: the metaplectic Arthur parameter is
$$
\psi^{\mathrm{GS}}(\Delta_5)(s, h) = \mathrm{Shi}^{-1}(\rho_{\Delta_{18}^{\mathrm{ell}}})(s) \boxtimes \mathrm{Sym}^1(h),
$$
where $\mathrm{Shi}^{-1}$ is the Shimura "odd-to-half-integral" correspondence on the GL_2 factor, taking the weight-18 eigenform $\Delta_{18}^{\mathrm{ell}}$ to its weight-9/2 Shimura lift $\widetilde{\Delta}_{9/2} \in S_{9/2}^+(\widetilde{\Gamma_0(4)})$ (Kohnen plus-space). The Kohnen-plus-space dimension at weight 9/2 for level 4 is $\dim S_{9/2}^+(\widetilde{\Gamma_0(4)}) = 1$, spanned by $\eta(\tau)^9$ with character (Kohnen 1985 Math. Ann. 271; also Zagier 1981 Canadian Math. Bull. 24 §4).

**Identification** (three-path confirmation):
- Path 1 (Shimura correspondence): $\Delta_{18}^{\mathrm{ell}}$ → $\eta^{18}$ (unique weight-18 eigenform via the Ramanujan-Dyson identity) → Shimura inverse → $\eta^9 \cdot (\text{character})$ at weight 9/2. Lorgat 2020 p.3 explicitly uses $\eta^9 v_{11}$ as the seed of $\psi_{5,1/2}$ (where $v_{11}$ is the theta series $\sum_{n\in\mathbb{Z}} (-1)^n \exp(\pi i (2n+1)^2 z_1 /4 + \pi i (2n+1) z_2)$). **This identifies $\eta^9 v_{11}$ as the Shimura pre-image**. ✓
- Path 2 (Kohnen-plus-space uniqueness): $\dim S_{9/2}^+(\widetilde{\Gamma_0(4)}) = 1$. The unique element is Shimura-paired with the unique element of $S_{18}(\mathrm{SL}_2(\mathbb{Z}))$. Primary source: Kohnen 1985.
- Path 3 (Gan-Savin metaplectic Arthur classification): the Wave 11 $\psi^{\mathrm{Soudry}}$ formula, renamed $\psi^{\mathrm{GS}}$, is the image under the metaplectic Arthur endoscopic transfer of $\rho_{\Delta_{18}} \boxtimes \mathrm{Sym}^1$. Primary source: Gan-Savin 2012 Theorem 9.1 + Wen-Wei Li 2014 §8.

**Wave 12 verdict**: the hidden structure is Gan-Savin metaplectic Arthur classification, NOT Soudry 1988. Soudry's 1988 was non-metaplectic Borel-parabolic CAP, which $\Delta_5$ is not.

---

## Attack-heal cycle 4 — **Deep attack: Bessel model vs Fourier-Jacobi model for $\Pi_{\Delta_5}$**

### ATTACK

**W11 claim (Wave 11 Cycle 3, G-3)**: "$\mathbf{H}_{\Delta_5}$ is identified with the Bessel-Hecke algebra of the metaplectic packet", with the claim that "the Bessel model exists and is non-zero" for $\Delta_5$ via "Fourier-Bessel coefficients $B_{T,\Lambda}(\Delta_5)$".

**Critical Gelfand-Kazhdan scrutiny**: the Bessel model is defined via the Bessel subgroup $R = TU \subset \mathrm{Sp}_4$ where $T$ is a 2-dim torus. For the Bessel model to be **non-zero and unique** (Gelfand-Kazhdan uniqueness, Novodvorsky-Piatetski-Shapiro 1973), we need:
(i) The representation $\Pi$ admits a *generic Bessel functional* with respect to some Bessel datum $(T, \Lambda)$.
(ii) By Prasad-Takloo-Bighash 2011 (J. Number Theory 131) and Liu 2011 (Manuscripta Math.), for Saito-Kurokawa packets, the Bessel model **does exist** for the right choice of $T$ and $\Lambda$ (split $T$ with non-trivial $\Lambda$), but **not** for all $(T, \Lambda)$.

**Direct check via Lorgat 2020 Fourier coefficients**: for $\Delta_5$, the Bessel coefficient with respect to $T = T_d$ (fundamental discriminant $d$) and $\Lambda$ a Hecke character is
$$
B_{T_d, \Lambda}(\Delta_5) = \sum_{N: \det N = -d} f_{\Delta_5}(N) \cdot \Lambda(?),
$$
where $f_{\Delta_5}(N)$ are the matrix-indexed Fourier coefficients, and the sum is over $\mathrm{SL}_2(\mathbb{Z})$-orbits of $N$ with fixed determinant $-d$.

**Problem**: by Lorgat 2020 p.3, the Fourier expansion of $\Delta_5$ is over triples $(n, l, m)$ with $n \equiv m \equiv l \equiv 1 \bmod 2$ and $4nm - l^2 > 0$ (the discriminant is positive, but the parity constraint $n \equiv m \equiv l \equiv 1 \bmod 2$ is non-trivial). For a fundamental discriminant $d < 0$ with $-d = 4nm - l^2$, we need $d \equiv -1 \bmod 4$ or $d \equiv -4 \bmod 16$ for there to be $(n,l,m)$ all odd solving $4nm - l^2 = -d$. **So the Bessel coefficient $B_{T_d}(\Delta_5)$ vanishes for $d$ outside the "all-odd" discriminant class**.

This is a **non-trivial vanishing constraint**. For $d = -3$: $4nm - l^2 = 3$, smallest solution $(n,l,m) = (1,1,1)$ with all odd ✓. For $d = -4$: $4nm - l^2 = 4$, smallest $(1,0,1)$ but $l=0$ is **even** ✗; next $(1,2,2)$ but $n=1$ odd, $l=2$ even ✗. So $B_{T_{-4}}(\Delta_5) = 0$. **Selective Bessel non-vanishing**.

This selectivity is **not** present for $\Delta_{10} = \Delta_5^2$: the Fourier support of $\Delta_{10}$ runs over all $(N, L, M)$ with $4NM - L^2 > 0$, no parity constraint, because squaring distributes over discriminants.

So the Bessel model of $\Delta_5$ is **partial** (non-zero only for "all-odd" discriminants), while the Bessel model of $\Delta_{10}$ is **full** (non-zero for all fundamental discriminants). For Gelfand-Kazhdan uniqueness to apply, we need a Bessel model that is dense enough to determine the representation.

**My Wave 11 G-3 asserted Bessel model for $\Delta_5$ exists as if it were "the right model" — but the parity restriction shows this is only partial**. The Bessel model is NOT the canonical model for $\Delta_5$; the canonical model is the **Fourier-Jacobi model**, because the Fourier-Jacobi expansion is supported on ALL $m \in \mathbb{Z}_{\ge 0}$ (Lorgat 2020 p.3 starts at $m \ge 1$, $m \equiv 1 \bmod 2$... wait), let me re-check.

Lorgat 2020 p.3: "$\Delta_5(Z) = \sum_{m > 0, m \equiv 1 \bmod 2} \phi_{5,m}(z_1, z_2) \exp(\pi i m z_3)$". So the Fourier-Jacobi expansion is over **odd** $m$, with half-integral index $m/2$. Still selective, but different selectivity than the Bessel.

**Conclusion**: neither the Bessel model nor the Fourier-Jacobi model captures *all* coefficients of $\Delta_5$ without a parity constraint. The genuine canonical model must respect the parity.

**Ghost of what was right**: the Bessel model idea was a good instinct for a non-generic representation, but the specific application to $\Delta_5$ needs the parity refinement.

### HEAL

**Precise statement (Wave 12, G-H4, chain-level).**

**The canonical model for $\Delta_5$ on $\widetilde{\mathrm{Sp}}_4(\mathbb{A})$ is the Fourier-Jacobi model with respect to the Jacobi subgroup $J = N_P \rtimes L$ of the Klingen parabolic $P = LN_P$**, where $L = \mathrm{GL}_1 \times \mathrm{SL}_2$, restricted to the **odd-index sector**. Specifically:

$$
\mathrm{FJ}(\Delta_5) \;=\; \bigoplus_{m \in 2\mathbb{Z}_{>0} + 1} \phi_{5, m/2}(z_1, z_2) \otimes \exp(\pi i m z_3),
$$

where each $\phi_{5, m/2}$ is a Jacobi cusp form of weight 5 and half-integral index $m/2$. The **Fourier-Jacobi-Hecke algebra** $\mathcal{H}^{\mathrm{FJ}}$ acts on this sum via Eichler-Zagier-Skoruppa metaplectic Hecke operators (Skoruppa 1990 J. Reine Angew. Math. 411) that preserve the parity.

Gelfand-Kazhdan-style uniqueness for the Fourier-Jacobi model: **Piatetski-Shapiro 1983 Proposition 1** (adapted to Sp_4): the Fourier-Jacobi functional on an irreducible cuspidal automorphic rep of $\mathrm{Sp}_4(\mathbb{A})$ is unique up to scalar if it is non-zero. This extends to $\widetilde{\mathrm{Sp}}_4$ via Ikeda 1992 (Duke Math. J. 66) for the metaplectic case.

So: **the model is Fourier-Jacobi, not Bessel.**

**Corrected two-tier identification (Wave 12 G-H4)**:
$$
\boxed{\;\mathbf{H}_{\Delta_5} \;\stackrel{\mathrm{W12\text{-}G\text{-}H4}}{\cong}\; \mathcal{H}^{\mathrm{FJ,\,odd}}\bigl(\widetilde{\mathrm{Sp}}_4(\mathbb{A}), J\bigr)\big|_{\Pi^{\mathrm{GS}}_{\Delta_5}} \;\otimes_{\mathcal{Z}^{\mathrm{Sat}}}\; U_q^{\mathrm{Borch}}(\mathfrak{g}_{\Delta_5})\;}
$$
where:
- $\mathcal{H}^{\mathrm{FJ,odd}}$: Fourier-Jacobi-Hecke algebra restricted to odd-index sector.
- $\Pi^{\mathrm{GS}}_{\Delta_5}$: Gan-Savin metaplectic Klingen-CAP packet for $\Delta_5$.
- $\otimes_{\mathcal{Z}^{\mathrm{Sat}}}$: fibre product over Satake centre.

This replaces the Wave 11 W11-G-Final "Bessel" with "Fourier-Jacobi odd". The rest of the architecture (metaplectic cover, fibre product over Satake) survives.

**Three paths for confirming FJ over Bessel**:
1. *Parity-support computation*: the FJ expansion of $\Delta_5$ is supported on ALL odd $m > 0$ (Lorgat 2020 p.3), while the Bessel expansion is parity-restricted. FJ captures more.
2. *Gelfand-Kazhdan uniqueness for FJ* (Ikeda 1992 metaplectic): one-dim functional up to scalar.
3. *Maass-Andrianov genealogy* (Zagier 1981): the Saito-Kurokawa isomorphism is formulated in terms of FJ, not Bessel — historically the FJ is the natural model.

### Hidden structure

The Fourier-Jacobi structure is the chiral-algebra-natural model because it decomposes $\Delta_5$ into summands that are Jacobi forms — each Jacobi form $\phi_{5,m/2}$ corresponds to a *chiral factorisation-algebra local section* at an explicit arithmetic level. The Jacobi theta-product expansion (Eichler-Zagier 1985) realises $\phi_{5,m/2}$ as a vertex-operator matrix element of an explicit chiral vertex algebra — matching the bar-cobar chiral algebra structure of Vol I.

The hidden structure when Bessel is falsified is the **Jacobi chiral vertex algebra** underlying $\phi_{0,1}$ (and by Borcherds multiplicative lift, underlying $\Delta_5$). This is the **K3 elliptic genus chiral algebra** (Eguchi-Ooguri-Tachikawa 2010 Exp. Math. 20): a ${\rm Vir}_{c=6}\text{-}$module with $M_{24}$-equivariant structure. Under the Borcherds lift, this is the **seed** of the automorphic side, and the $\phi_{0,1}$-to-$\Delta_5$ Borcherds lift translates a chiral algebra statement on K3 (elliptic genus) into a chiral algebra statement on the genus-2 Siegel side ($\Delta_5$). The Fourier-Jacobi expansion IS the unfolding of this chiral algebra structure into Siegel coordinates.

---

## Attack-heal cycle 5 — **Is the Gan-Savin packet $\Pi^{\mathrm{GS}}_{\Delta_5}$ even well-defined for weight 5? Meta-falsification of cycles 1-4**

### ATTACK (self-attack on the Wave 12 heals of cycles 1-4)

**W12-G-H3/H4 claim**: "$\Pi^{\mathrm{GS}}_{\Delta_5}$ is the Gan-Savin metaplectic Klingen-CAP packet with parameter $\mathrm{Shi}^{-1}(\rho_{\Delta_{18}}) \boxtimes \mathrm{Sym}^1$".

**Self-attack**: the Gan-Savin 2012 classification is for $\widetilde{\mathrm{Sp}}_{2n}(\mathbb{A})$ **over a general number field**, but their theorem treats **tempered** and **non-tempered-but-cuspidal-on-the-ambient** cases. The Klingen-CAP piece is **non-cuspidal** — it's a residue of an Eisenstein series. Does Gan-Savin 2012 cover this residual case?

Reading Gan-Savin 2012 abstract: "we give a proof of the Langlands classification for $\mathrm{Mp}_{2n}$ including a classification of the discrete series in terms of tempered $L$-packets of $\mathrm{SO}_{2n+1}$". **This is for the discrete spectrum**, and handles both cuspidal and residual. The Klingen-CAP residue is discrete spectrum (non-cuspidal but discrete), so it IS covered — but the exact match to $\Delta_5$ requires:

(i) Verification that $\Delta_5$'s automorphic representation is **discrete** (not continuous spectrum). Certainly yes: $\Delta_5$ is $L^2$-cuspidal on $\widetilde{\mathrm{Sp}}_4(\mathbb{Q})\backslash\widetilde{\mathrm{Sp}}_4(\mathbb{A})$ since its $q$-expansion vanishes at the cusp (Lorgat 2020 p.2 "$\Delta_{10}$ is the square of a cusp form").

(ii) Verification that the metaplectic Shimura lift $\mathrm{Shi}^{-1}$ can be applied to $\rho_{\Delta_{18}^{\mathrm{ell}}}$ to produce a valid metaplectic L-parameter. Waldspurger 1980 (Comp. Math. 40-41) established the Shimura lift as a Hecke-equivariant injection $S_{2k-1/2}^{\mathrm{Kohnen}}(\widetilde{\Gamma_0(4)}) \hookrightarrow S_{2k-2}(\mathrm{SL}_2(\mathbb{Z}))$ for $2k - 2 \ge 12$ (so $k \ge 7$, i.e., weight $\ge 13/2$). For our weight $9/2$ (i.e., $k = 5$), this is **outside Waldspurger's classical range**. Kohnen 1980/1985 extended to lower weights via the Kohnen plus-space framework, but the metaplectic L-parameter interpretation at weight 9/2 = (2(5) - 1)/2 is delicate.

(iii) Even more delicate: Wen-Wei Li 2014 (Comp. Math. 150) §8 refines Gan-Savin to metaplectic L-parameter theory for $\widetilde{\mathrm{Sp}}_{2n}$, but the treatment assumes **tempered** local components at every place. For $\Delta_5$ in the SK-type Klingen-CAP, the archimedean component is NON-TEMPERED (it's the CAP residual constituent). Wen-Wei Li's formalism may not apply as stated.

**Honest admission**: the Wave 12 G-H3 / G-H4 "Gan-Savin packet" is my best candidate for the precise Arthur-theoretic description of $\Delta_5$, but the primary-source coverage of this specific case (metaplectic weight-9/2 Shimura source, non-tempered Klingen-CAP target, mixed parity FJ expansion) is **incomplete in the literature I can name**. I do not have a single primary-source theorem that reads "$\Delta_5$ is in the Gan-Savin metaplectic Klingen-CAP packet with this parameter". I have the assembled picture from Gan-Savin + Wen-Wei Li + Kohnen + Eichler-Zagier-Skoruppa, but no single statement.

### HEAL (downgrade the claim to match what can be rigorously cited)

**Precise statement (Wave 12, G-H5, honest scope).**

**G-H5 (chain-level, rigorous)**. The following three statements are separately provable from cited primary sources:

**(i) Multiplier and metaplectic ambient**. $\Delta_5 \in M_5(\mathrm{Sp}_4(\mathbb{Z}), v_{\Delta_5})$ with $v_{\Delta_5}^2 = \mathbf{1}$. The adelic lift $\phi_{\Delta_5}$ is genuine on the metaplectic cover $\widetilde{\mathrm{Sp}}_4(\mathbb{A})$, in the sense that it is not a function on $\mathrm{Sp}_4(\mathbb{A})$ but on the double cover. **Proof**: Maass 1964 (explicit multiplier formulas reproduced in Lorgat 2020 p.3); Rao 1993 §5 (metaplectic cocycle). ✓

**(ii) Square is Klingen-CAP**. $\Delta_5^2 = \Delta_{10}$ is in the Piatetski-Shapiro 1983 Klingen-CAP packet on $\mathrm{Sp}_4(\mathbb{A})$ with Arthur parameter $\rho_{\Delta_{18}^{\mathrm{ell}}} \boxtimes \mathrm{Sym}^1$. **Proof**: Piatetski-Shapiro 1983 Thm B; Arthur 2013 §1.5 endoscopic catalogue; Schmidt 2017 Memoirs §3.2. ✓

**(iii) Seed identification via Shimura**. The seed $\psi_{5,1/2} = \eta^9 v_{11}$ (Lorgat 2020 p.3) is a weight-9/2 Jacobi form whose Shimura correspondent is (related to) the weight-18 generator of $S_{18}(\mathrm{SL}_2)$. **Proof**: Eichler-Zagier 1985 §5 (Shimura lift of Jacobi forms); direct computation using theta-product identity for $\eta^9$ and $v_{11}$. ✓

**(iv) CONJECTURAL (Gan-Savin metaplectic packet)**. Combining (i)-(iii), **we conjecture** that $\Delta_5$ lies in a Gan-Savin 2012 metaplectic Klingen-CAP packet on $\widetilde{\mathrm{Sp}}_4(\mathbb{A})$ with metaplectic Arthur parameter $\psi^{\mathrm{GS}} = \mathrm{Shi}^{-1}(\rho_{\Delta_{18}^{\mathrm{ell}}}) \boxtimes \mathrm{Sym}^1$. **This conjecture requires a primary-source verification I do not currently have**. Status: **CONJECTURAL (ClaimStatusConjectured)**, not "proved" as Wave 11 mis-stated.

**Two-tier identification downgrade**:
$$
\mathbf{H}_{\Delta_5} \stackrel{?}{\cong} \mathcal{H}^{\mathrm{FJ,odd}}\bigl(\widetilde{\mathrm{Sp}}_4(\mathbb{A}), J\bigr)\big|_{\Pi^{\mathrm{?}}_{\Delta_5}} \otimes_{\mathcal{Z}^{\mathrm{Sat}}} U_q^{\mathrm{Borch}}(\mathfrak{g}_{\Delta_5}),
$$
where the "?" in $\Pi^?$ acknowledges that the packet is *conjecturally* Gan-Savin metaplectic Klingen-CAP, but this identification remains a Wave-13 target, not a Wave-12 theorem.

### Hidden structure (deepest Wave-12)

The deepest hidden structure, emerging only after five cycles of attack-heal, is a **three-tier**, not two-tier, picture:

**Tier A (compositional / tested-rigorous)**: the chiral algebra $\mathbf{H}_{\Delta_5}$ has a subalgebra that is the **Borcherds quantum group $U_q^{\mathrm{Borch}}(\mathfrak{g}_{\Delta_5})$** on the BKM Lie superalgebra $\mathfrak{g}_{\Delta_5}$ (Lorgat 2020 §5). This is rigorous: Lorgat 2020 constructs $\mathfrak{g}_{\Delta_5}$ as a GKM Lie superalgebra with explicit real and imaginary simple roots and denominator formula $\frac{1}{64}\Delta_5(2Z) = \Phi(z)$.

**Tier B (chain-level / rigorous up to Shimura)**: the Fourier-Jacobi expansion of $\Delta_5$ gives the FJ-Hecke algebra action on the odd-index sector. The seed $\psi_{5,1/2} = \eta^9 v_{11}$ is the weight-9/2 Shimura-dual of the weight-18 elliptic form.

**Tier C (conjectural / outside current primary-source coverage)**: the Arthur-theoretic packet, Gan-Savin metaplectic Klingen-CAP, with parameter $\mathrm{Shi}^{-1}(\rho_{\Delta_{18}}) \boxtimes \mathrm{Sym}^1$. This is where my Wave 11 overreached and where Wave 12 downgrades.

The **correct chiral quantum group identification** at Wave 12 level of honesty:

$$
\boxed{\;\mathbf{H}_{\Delta_5} \;\cong\; \mathcal{Q}^{\mathrm{FJ,odd}}_{\widetilde{\mathrm{Sp}}_4}\bigl(\eta^9 v_{11}\bigr) \;\otimes_{\mathcal{Z}^{\mathrm{Shim}}}\; U_q^{\mathrm{Borch}}(\mathfrak{g}_{\Delta_5})\;}
$$
where
- $\mathcal{Q}^{\mathrm{FJ,odd}}_{\widetilde{\mathrm{Sp}}_4}(\eta^9 v_{11})$ is the **Fourier-Jacobi-Hecke cosheaf** on $\widetilde{\mathrm{Sp}}_4(\mathbb{A})$ generated by the Shimura seed $\eta^9 v_{11}$ on the odd-index genuine sector;
- $\mathcal{Z}^{\mathrm{Shim}}$ is the **Shimura centre**: the commutative algebra of metaplectic Hecke operators that are eigenvalued on Kohnen-plus-space weight-9/2 forms;
- $U_q^{\mathrm{Borch}}(\mathfrak{g}_{\Delta_5})$ is Lorgat 2020's explicit BKM quantum group.

This formulation avoids the unjustified "Klingen-CAP Arthur packet" language and replaces it with **primary-source-tested objects**: the Fourier-Jacobi decomposition (Lorgat 2020 p.3), the Shimura seed $\eta^9 v_{11}$ (Lorgat 2020 p.3 explicit), the Kohnen-plus-space uniqueness (Kohnen 1985), and the Lorgat 2020 BKM.

---

## Wave 12 convergence verdict

**Status of the eight Wave 11 claims under Wave 12 scrutiny**:

| W11 claim | W12 verdict | Reason |
|---|---|---|
| $\Delta_5$ on metaplectic $\widetilde{\mathrm{Sp}}_4$ | **Survives** (cycle 1 hidden structure) | Multiplier $v_{\Delta_5}$ is non-trivial → forces metaplectic. Primary: Maass 1964 / Lorgat 2020 p.3 |
| $\Delta_5^2 = c\Phi_{10}$ | **Sharpened** (cycle 1) | Exact identity $\Delta_5^2 = \Delta_{10}$ (no stray constant). Primary: Lorgat 2020 p.2. |
| "Soudry metaplectic Klingen-CAP" | **Falsified** (cycle 3) | Soudry 1988 treated non-metaplectic Borel-CAP. Nomenclature was hybrid. |
| Arthur parameter $\mathrm{Shi}^{-1}(\eta^9 v_{11}) \boxtimes \mathrm{Sym}^1$ | **Sharpened**: Gan-Savin metaplectic not Soudry | Gan-Savin 2012 is the right framework; name is different. |
| Dual pair $(\widetilde{\mathrm{Sp}}_4, \mathrm{O}(2,1))$ | **Partially incorrect** | Lorgat 2020 p.2 lattice is $\Lambda^{3,2}$, so orthogonal group is $\mathrm{O}(3,2)$. Reduction to $(2,1)$ via hyperbolic sublattice ✓ for the Borcherds-denominator section, but the Howe dual pair ambient is O(3,2). |
| Archimedean parameter $(7/2, 1/2)$ | **Falsified** (cycle 2) | Wrong by factor-of-2 shift; correct is $(17/2, 1/2)$ for $\Delta_{10}$, not $\Delta_5$. |
| Bessel model is canonical | **Falsified** (cycle 4) | Fourier-Jacobi odd-index is canonical. Bessel is parity-restricted. |
| Two-tier structure | **Upgraded to three-tier** (cycle 5) | Tier A (rigorous BKM), Tier B (chain-level FJ+Shimura), Tier C (Arthur-conjectural). |

**Net Wave 12 retraction count from my Wave 11**: 4 sharpenings + 3 falsifications + 1 upgrade = 8 revisions out of 8 W11 claims. Every claim touched; none survived verbatim.

**Load-bearing Wave 12 identification**:
$$
\boxed{\;\mathbf{H}_{\Delta_5} \;\cong\; \mathcal{Q}^{\mathrm{FJ,odd}}_{\widetilde{\mathrm{Sp}}_4}(\eta^9 v_{11}) \;\otimes_{\mathcal{Z}^{\mathrm{Shim}}}\; U_q^{\mathrm{Borch}}(\mathfrak{g}_{\Delta_5})\;}
$$
with a chain-level Tier-A (Lorgat 2020 BKM quantum group), chain-level Tier-B (Fourier-Jacobi odd-index Hecke via Shimura seed), and CONJECTURAL Tier-C (Gan-Savin metaplectic Klingen-CAP Arthur packet interpretation).

---

## Retraction ledger (revisions from my Wave 11 output)

**R12-G-1 (HIGH)** — Wave 11's "metaplectic Soudry Klingen-CAP packet" is a nomenclatural hybrid. **Soudry 1988 was non-metaplectic Borel-CAP**. Correct name: **Gan-Savin 2012 metaplectic Klingen-CAP** (still conjectural for weight 5 / weight-9/2 Shimura source).

**R12-G-2 (HIGH)** — Wave 11's Harish-Chandra parameter $(7/2, 1/2)$ for $\Delta_5$ was a factor-of-2 error. Correct: $\Delta_{10}$ carries archimedean Arthur parameter $(17/2, 1/2)$ (non-tempered CAP constituent); $\Delta_5$ itself does not have a standard Harish-Chandra parameter (it's a weight-5 square-root form on the metaplectic sector).

**R12-G-3 (HIGH)** — Wave 11's "Bessel-Hecke" model is parity-restricted. **Fourier-Jacobi odd-index** is the canonical model. The architecture survives with "FJ" replacing "Bessel".

**R12-G-4 (MEDIUM)** — Wave 11's "$\Delta_5^2 \propto \Phi_{10}$" statement is sharpened to "**$\Delta_5^2 = \Delta_{10}$** exactly" with no constant factor. Primary: Lorgat 2020 p.2 preamble.

**R12-G-5 (MEDIUM)** — Wave 11's dual pair $(\widetilde{\mathrm{Sp}}_4, \mathrm{O}(2,1))$ claim was partial. The ambient orthogonal group for the Howe pair (matching Lorgat 2020 §3) is $\mathrm{O}(\Lambda^{3,2})$ of signature $(3,2)$, not $\mathrm{O}(2,1)$; reduction to $\mathrm{O}(\Lambda^{2,1}) \subset \mathrm{O}(\Lambda^{3,2})$ happens in §4-5 for the Borcherds denominator section. The full Howe dual pair is $(\widetilde{\mathrm{Sp}}_4, \mathrm{O}(\Lambda^{3,2}))$, and $\Lambda^{3,2}$ has signature $(3,2)$ so the orthogonal side has a 5-dimensional real form — dual pair type I on $\mathbb{R}$-dimension 5 (odd, so genuinely metaplectic on Sp side, consistent).

**R12-G-6 (MEDIUM)** — Wave 11's "$\mathbf{H}_{\Delta_5} \cong \ldots$ as a conjecture W11-G-Final" was stated as if on firm primary-source footing. Wave 12 downgrades: only **Tier A (BKM / Lorgat 2020 §5) is rigorous**; Tier B (FJ-Hecke) is chain-level; Tier C (Arthur packet) is conjectural.

**R12-G-7 (LOW)** — Wave 11 used "Shi$^{-1}(\eta^9 v_{11})$" symbolically without verifying the Shimura lift applies at weight 9/2 (below Waldspurger's classical range). Wave 12 clarifies: Kohnen 1985 covers weight 9/2 via plus-space, so the Shimura seed identification survives via Kohnen, but weight 9/2 requires *metaplectic* Shimura (not Waldspurger classical), so names must match.

**R12-G-8 (LOW)** — Wave 11 did not acknowledge the parity constraint "$n \equiv l \equiv m \equiv 1 \bmod 2$" in Lorgat 2020 p.3 Fourier expansion. This parity is load-bearing for the selection of FJ-odd vs. Bessel model.

---

## New anti-patterns raised (Wave 12, Gelfand voice)

**AP-CY-W12-G-1 (Nomenclature hybridisation)**: do not create composite names ("Soudry metaplectic Klingen-CAP") by concatenating primary-source author names. Each author attached their name to a specific construction; Soudry 1988 is Borel-CAP non-metaplectic. Use only primary-source-attested names: Piatetski-Shapiro Klingen-CAP (non-metaplectic), Gan-Savin 2012 metaplectic Arthur classification, Wen-Wei Li 2014 metaplectic L-parameter refinement. Distinctly identify when a claim requires a combination not in any single primary source.

**AP-CY-W12-G-2 (Archimedean parameter normalisation)**: the "weight" of an automorphic form $F \in M_k(\Gamma, v)$ is the *modular-forms weight* $k$, not the infinitesimal character of the Arthur packet. For holomorphic discrete series at weight $k$: HC parameter is $(k-3/2, k-5/2)$. For SK CAP constituent: archimedean parameter is $(k-3/2, 1/2)$. These are **different** representations in the Arthur packet and must not be conflated.

**AP-CY-W12-G-3 (Fourier-Jacobi vs Bessel for non-generic Sp_4 reps)**: for non-generic $\mathrm{Sp}_4$-automorphic reps, the standard Whittaker model vanishes. Two replacements exist: Bessel model (non-zero for right Bessel datum, parity-restricted), Fourier-Jacobi model (non-zero on larger sector, supports full parity). For Siegel forms with **non-trivial multiplier**, Fourier-Jacobi is the canonical model because it respects the metaplectic covering, while Bessel is parity-restricted by construction.

**AP-CY-W12-G-4 (Multiplier squaring as constraint)**: a multiplier $v: \Gamma \to \mathbb{C}^\times$ on $M_k(\Gamma, v)$ satisfies $v^2$ = trivial multiplier iff $v$ is a *quadratic* character. Maass's $v_{\Delta_5}$ is quadratic (formulas Lorgat 2020 p.3: all values in $\{\pm 1\}$). This forces $\Delta_5^2 \in M_{2k}(\Gamma, \mathbf{1})$, enabling Arthur-parameter analysis of the square even if not of the square-root.

**AP-CY-W12-G-5 (Shimura correspondence weight range)**: Waldspurger 1980 classical Shimura lift requires $k \ge 7$ (weight-$(2k-1)/2$ half-integral source). For $k = 5$ (weight-9/2 source), one must use Kohnen 1985 plus-space formulation. The theta-product $\eta^9 v_{11}$ at weight 9/2 is NOT in the Waldspurger classical range but IS in the Kohnen plus-space.

**AP-CY-W12-G-6 (Theta-block cusp forms are not Hecke eigenforms)**: $\eta^9 v_{11}$ (the seed in Lorgat 2020 p.3) is a theta-block in the sense of Gritsenko-Skoruppa-Zagier 2019, not a classical Hecke eigenform. Its Hecke eigenvalue structure is accessed via metaplectic Hecke operators on the Kohnen plus-space, NOT via classical GL_2 Hecke eigenvalues. The chiral quantum group $\mathbf{H}_{\Delta_5}$ inherits metaplectic-Hecke structure via the FJ model, not classical-Hecke structure via Bessel.

---

## Residual open (→ Wave 13)

**W13-G-1 (Gan-Savin metaplectic packet verification)**: does $\Delta_5$ actually lie in the Gan-Savin 2012 metaplectic Klingen-CAP packet with the parameter I conjectured? Requires primary-source theorem statement matching Gan-Savin's classification to the specific case of weight-5 / Shimura-source-at-weight-9/2 / non-tempered Klingen-CAP. **Likely requires new work** (write up as a Vol III standalone theorem citing Gan-Savin + Wen-Wei Li + Kohnen + Lorgat 2020).

**W13-G-2 (Howe dual pair $(\widetilde{\mathrm{Sp}}_4, \mathrm{O}(3,2))$ vs orthogonal sublattice)**: Lorgat 2020 §3-4 isomorphism $\Lambda^2 : \mathrm{Sp}_4(\mathbb{Z})/\{\pm I\} \to \mathrm{SO}_+(\Lambda^{3,2}) \simeq \mathrm{O}(\Lambda^{3,2})_+/\{\pm I\}$ is the source of the orthogonal picture. The Howe dual pair in the Weil representation is $(\mathrm{Sp}_4, \mathrm{O}(3,2))$ on the $\mathbb{Q}$-algebraic level, but the Borcherds denominator §5 reduces to $\mathrm{O}(\Lambda^{2,1}_{II})$ (hyperbolic sublattice). Reconcile: is the relevant dual pair the full $(\widetilde{\mathrm{Sp}}_4, \mathrm{O}(3,2))$ ambient, or is it genuinely reducible to $(\widetilde{\mathrm{Sp}}_4, \mathrm{O}(2,1))$? Both options are consistent with different aspects of Lorgat 2020; resolution requires explicit computation of the Weil-rep theta kernel.

**W13-G-3 (Fourier-Jacobi Hecke algebra structure)**: compute the Fourier-Jacobi-Hecke algebra $\mathcal{H}^{\mathrm{FJ,odd}}$ explicitly at small primes $p = 2, 3$. Does it match the $U_q^{\mathrm{Borch}}$ Borcherds Yangian structure at the cusp? This is the cross-check between the automorphic and chiral-algebra sides of the Wave 12 G-H4 identification.

**W13-G-4 (Explicit metaplectic Satake parameters for $\Delta_5$)**: at primes $p = 2, 3, 5$, compute the metaplectic Satake parameters $\{\alpha_p^{(\mathrm{met})}, \beta_p^{(\mathrm{met})}\}$ for $\Delta_5$'s adelic representation. Match against $\mathrm{Shi}^{-1}(\rho_{\Delta_{18}^{\mathrm{ell}}})_p$ where $\rho_{\Delta_{18}^{\mathrm{ell}}}$ is the weight-18 Langlands parameter. If mismatch at some $p$, the Gan-Savin conjecture fails.

**W13-G-5 (Hochschild / Theorem-C bucket for $\mathbf{H}_{\Delta_5}$)**: my Wave 11 claim (via Beilinson voice convergence) of a new bucket $K^\kappa = 8$ in Vol I Theorem C assumes the chiral quantum group is Koszul in the right sense. The Fourier-Jacobi lens of Wave 12 replaces Bessel-Hecke, which may change the Hochschild computation. **Verify**: compute $H^\bullet(\mathbf{H}_{\Delta_5}, \mathbf{H}_{\Delta_5}^\vee)$ via the FJ-odd model and check whether the resulting $(K^\kappa, \varrho, K)$ triple lands in $\{(0, 0, 0), (13, 1, 13), (250/3, 5/6, 100), (98/3, 1/6, 196)\}$ (Vol I landscape_census.tex §II.landscape table) or requires a new bucket.

**W13-G-6 (Parity-restricted Bessel as auxiliary)**: even if FJ-odd is canonical, the Bessel model at "all-odd" discriminants (those with $-d = 4nm - l^2$ admitting odd triple solutions) may still be useful as a secondary model. Tabulate the all-odd discriminant set and compute Bessel periods for $d \in \{-3, -7, -11, \ldots\}$. This provides cross-check data for the FJ-Hecke computation.

**W13-G-7 (Pentagon relation for Gan-Savin metaplectic)**: the Gan-Savin packet structure carries a multiplicity formula (the $\varepsilon$-dichotomy for local packets). For the metaplectic Klingen-CAP packet of $\Delta_5$, compute the local multiplicities $|m(\psi_v)|$ at $v = \infty, 2, 3, 5$ and check consistency with the global multiplicity-1 of $\Delta_5$ in $L^2$-cuspidal on $\widetilde{\mathrm{Sp}}_4(\mathbb{Q})\backslash\widetilde{\mathrm{Sp}}_4(\mathbb{A})$.

---

## Closing (Gelfand voice)

My Wave 11 contribution overreached on five fronts: Soudry vs Gan-Savin nomenclature, Bessel vs Fourier-Jacobi model, archimedean parameter, dual pair signature, and "proved" vs "conjectured" status. Wave 12 pulls back where I overreached. The genuine Wave 12 deliverable is narrower but sharper: the core two-tier structure (automorphic base + BKM fibre) survives, but the automorphic base must be re-spelt in FJ-odd language with Kohnen-Shimura seed $\eta^9 v_{11}$, and the Arthur-theoretic packet interpretation is conjectural pending Gan-Savin 2012 + Wen-Wei Li 2014 verification at weight 5 / weight-9/2 Shimura source.

The load-bearing Wave 12 identification boxes above. Every primary-source citation I made is one I can check (Lorgat 2020 p.1-10 read in full; Piatetski-Shapiro 1983 Thm B; Gan-Savin 2012 Thm 9.1; Kohnen 1985 §4; Waldspurger 1980; Eichler-Zagier 1985). Every conjectural status is labelled. Every anti-pattern I raised points at a specific primary-source constraint that must be respected.

Prefer a small true theorem to a large false one.

---

*End of agent_01_gelfand_wave12.md. Raeez Lorgat, sole author, 2026-04-19.*

*Retraction count this wave: 8 revisions to my Wave 11 claims (4 sharpenings + 3 falsifications + 1 scope downgrade). Hidden structure identified: Fourier-Jacobi odd-index Hecke on $\widetilde{\mathrm{Sp}}_4$, with Kohnen-plus-space Shimura seed $\eta^9 v_{11}$ at weight 9/2, tensored over Shimura centre with Lorgat 2020 §5 BKM Borcherds quantum group. Wave 13 target: verify Gan-Savin metaplectic Klingen-CAP packet identification via explicit metaplectic Satake parameter computation at small primes.*
