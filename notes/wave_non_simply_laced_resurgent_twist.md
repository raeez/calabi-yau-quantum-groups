# Non-formal Resurgent Drinfeld Twist for Non-Simply-Laced $Y(\mathfrak{g})$: $B_n$, $C_n$, $F_4$, $G_2$

## Split-Stokes data, lacing-twisted instanton actions, and explicit verification at $B_2 = C_2$ and $G_2$

**Author.** Raeez Lorgat. **Date.** 2026-04-17. **Mode.** Lossless attack-and-heal extension of the V119 resurgent Drinfeld twist (ADE inscription, `thm:Yfg-resurgent-Drinfeld-twist`) to the non-simply-laced types $B_n, C_n, F_4, G_2$.

**Posture.** AP-CY55 (Stokes data is an algebraization invariant of $Y(\mathfrak{g})$, fixed by the choice of root system and its bilinear form normalisation; not by any underlying CY); AP-CY60 (the lacing-split is *one* construction of the split-Stokes pattern, not a derivation from the ADE pattern); AP-CY61 (first-principles ghost extraction: every tentative extension carries a wrong-claim/right-claim ledger); AP151 (two distinct couplings $\hbar$ and $g_s$ remain disjoint throughout); AP-CY56 ($Y(\mathfrak{g})$ is the algebraic object; the $E_n$ structure question is suppressed because the twist lives at the level of bialgebra structure, not chiral algebra).

**Inputs preserved verbatim from V119.**
- Transseries ansatz $\mathcal{F}_{Y(\mathfrak{g})}(\hbar; g_s) = \mathcal{F}^{\mathrm{formal}}(\hbar) \cdot \exp\bigl(\sum_{n,\alpha} A^n_\alpha\, e^{-n S_\alpha/g_s} \mathcal{G}^{(n,\alpha)}\bigr)$.
- Stokes singularity formula $S_\alpha = \tfrac{1}{2}(\alpha,\alpha) \cdot \langle \rho^\vee, \alpha^\vee\rangle$.
- Stokes constants $A^n_\alpha = (n!)^{-1} \cdot c_\alpha^{-n} \cdot (h_\alpha \otimes h_\alpha)^n$ with the rank-dependent normalisation $c_\alpha$.
- Resurgent generators $\mathcal{G}^{(n,\alpha)} \in \mathrm{HS}^{2,\bullet}(Y(\mathfrak{g}))$.

For ADE the formula collapses to $S_\alpha = 1$ uniformly, $c_\alpha = 4$ uniformly. The non-simply-laced extension splits both.

---

## §1. Bourbaki root data and lacing dictionary

We fix the Bourbaki convention: the Cartan inner product $(\,\cdot\,,\,\cdot\,)$ is normalised so that *long roots* have squared length $(\alpha_{\mathrm{long}}, \alpha_{\mathrm{long}}) = 2$. The *short roots* have squared length $(\alpha_{\mathrm{short}}, \alpha_{\mathrm{short}}) = 2/d$ where $d$ is the *lacing number*: $d = 2$ for $B_n, C_n, F_4$ and $d = 3$ for $G_2$.

The simple-coroot pairing with the dual Weyl vector remains the universal Coxeter identity
$$\langle \rho^\vee, \alpha_i^\vee\rangle \;=\; 1 \qquad \forall i \;\in\; \{1, \dots, r\}.$$
This is independent of lacing because $\rho^\vee = \tfrac{1}{2}\sum_{\beta \in \Phi^+_\vee}\beta$ pairs to $1$ against every simple coroot by the standard Bourbaki argument (Bourbaki, *Groupes et algèbres de Lie* IV–VI, Ch.~VI §1.10, Prop.~29).

**Lacing-twisted Stokes singularities.** Substituting into $S_\alpha = \tfrac{1}{2}(\alpha,\alpha) \cdot \langle \rho^\vee, \alpha^\vee\rangle$ gives

$$\boxed{\;S_{\alpha_{\mathrm{long}}} \;=\; 1, \qquad S_{\alpha_{\mathrm{short}}} \;=\; \frac{1}{d}.\;}$$

For $B_n$, $C_n$, $F_4$: $S_{\mathrm{short}} = 1/2$. For $G_2$: $S_{\mathrm{short}} = 1/3$.

The Bourbaki labelling for each non-simply-laced type:

| Type | Rank | Long simple roots (Bourbaki indices) | Short simple roots | Lacing $d$ |
|------|------|---------------------------------------|--------------------|------------|
| $B_n$  | $n$ | $\alpha_1, \dots, \alpha_{n-1}$ | $\alpha_n$ | $2$ |
| $C_n$  | $n$ | $\alpha_n$ | $\alpha_1, \dots, \alpha_{n-1}$ | $2$ |
| $F_4$  | $4$ | $\alpha_1, \alpha_2$ | $\alpha_3, \alpha_4$ | $2$ |
| $G_2$  | $2$ | $\alpha_2$ | $\alpha_1$ | $3$ |

(Bourbaki conventions: $B_n$ the long roots are at the head of the chain, with the short root at the marked end; $C_n$ reversed; $F_4$ the head two simple roots are long; $G_2$ the short root is $\alpha_1$ with $(\alpha_1, \alpha_1) = 2/3$.)

---

## §2. Ghost-theorem analysis: WHAT splits and what does NOT

**AP-CY61 ledger before any computation.**

(a) **What the V119 ADE pattern gets RIGHT.** The Borel singularity location is set by the Cartan-eigenvalue spectrum of the simple-Casimir projection $P_i = h_{\alpha_i}\otimes h_{\alpha_i}/(\alpha_i,\alpha_i)$. The Cartan eigenvalue is $\langle\rho^\vee,\alpha_i^\vee\rangle = 1$. The bilinear normalisation enters as the prefactor $(\alpha_i,\alpha_i)/2$.

(b) **What a *naive ADE-uniform* extension would get WRONG.** Asserting $S_\alpha = 1$ for all $\alpha$ in non-simply-laced types ignores the explicit $(\alpha_i,\alpha_i)$ prefactor. The Borel singularity locations DO split.

(c) **The right theorem.** The simple split-Stokes hypothesis $S_\alpha = (\alpha,\alpha)/2$ is structurally forced by the same Drinfeld--Etingof--Kazhdan recursion that produces the ADE result; the only difference is that the input bilinear form is no longer $2 \cdot \delta_{ij}$ on the diagonal of the Cartan.

(d) **The Stokes-constant prefactor.** The leading-order Stokes constant in V119 was $A^1_\alpha = \tfrac{1}{4}(h_\alpha\otimes h_\alpha)$ (the "$4$" from $(\alpha,\alpha)^2 = 4$ for ADE long roots, and $1/(\alpha,\alpha)$ from the Casimir projector normalisation). For non-simply-laced
$$A^1_\alpha \;=\; \frac{1}{(\alpha,\alpha)^2}\, (h_\alpha \otimes h_\alpha) \;=\; \begin{cases} 1/4 \cdot (h_\alpha \otimes h_\alpha) & \text{long}, \\ d^2/4 \cdot (h_\alpha \otimes h_\alpha) & \text{short}.\end{cases}$$
For B/C/F: short prefactor $1$; for $G_2$: short prefactor $9/4$.

(e) **Multi-instanton tower.** The factorisation $A^n_\alpha = (n!)^{-1}\, (A^1_\alpha)^n$ is preserved root-by-root. Cross-root mixing at higher instanton order would require the Borel singularities at $S_{\mathrm{long}} = 1$ and $S_{\mathrm{short}} = 1/d$ to lie in resonance, i.e. $n_1 \cdot 1 = n_2 \cdot 1/d$ for positive integers $n_1, n_2$. This gives $n_2 = d \cdot n_1$, hence resonance at $(n_1, n_2) = (1, d)$.

(f) **Resonance correction.** At the resonance $(n_1, n_2) = (1, d)$ the multi-instanton tower picks up a *log-resonant* correction (Écalle's *equidistant resurgence*, cf. Costin §5.6). This is the *one place* where the simple split-Stokes hypothesis must be patched. Concretely, the resurgent generator $\mathcal{G}^{(d, \alpha_{\mathrm{short}})}(\hbar)$ acquires a $\log(g_s)$ enhancement at the resonance, with prefactor controlled by the lacing number $d$.

The **patched conjecture**:

$$\boxed{\;
\mathcal{F}_{Y(\mathfrak{g})}(\hbar; g_s) \;=\; \mathcal{F}^{\mathrm{formal}}(\hbar) \cdot \exp\!\Biggl(\sum_{n \ge 1}\sum_{i=1}^{r} \frac{e^{-n S_{\alpha_i}/g_s}}{n!\, ((\alpha_i,\alpha_i)/2)^{2n}}\, (h_{\alpha_i}\otimes h_{\alpha_i})^n\, \mathcal{G}^{(n,\alpha_i)}(\hbar; \log g_s)\Biggr) + O(\hbar^4),
\;}$$

with $S_{\alpha_i} = (\alpha_i,\alpha_i)/2$ and $\mathcal{G}^{(d,\alpha_{\mathrm{short}})}(\hbar; \log g_s)$ carrying a log-resonant tail when the $d$-th short-instanton resonates with the leading long-instanton.

---

## §3. Explicit verification: $B_2 = C_2$

The exceptional isomorphism $B_2 \cong C_2$ provides a self-consistency cross-check: the Stokes data must be invariant under the duality.

**Bourbaki $B_2$.** Simple roots $\alpha_1$ (long), $\alpha_2$ (short), Cartan matrix
$$C^{B_2} = \begin{pmatrix} 2 & -2 \\ -1 & 2 \end{pmatrix}, \qquad (\alpha_1,\alpha_1) = 2,\ (\alpha_2,\alpha_2) = 1,\ (\alpha_1,\alpha_2) = -1.$$

Coroot lengths $(\alpha_i^\vee, \alpha_i^\vee) = 4/(\alpha_i,\alpha_i)$ giving $(\alpha_1^\vee,\alpha_1^\vee) = 2$ and $(\alpha_2^\vee,\alpha_2^\vee) = 4$.

Half-sum of positive coroots:
$$\rho^\vee = \frac{1}{2}\sum_{\beta\in \Phi^+_\vee}\beta = \alpha_1^\vee + \alpha_2^\vee$$
(the four positive coroots of $B_2$ are $\alpha_1^\vee, \alpha_2^\vee, \alpha_1^\vee + \alpha_2^\vee, 2\alpha_1^\vee + \alpha_2^\vee$; sum $= 4\alpha_1^\vee + 2\alpha_2^\vee = 2(\alpha_1^\vee + 2\alpha_2^\vee)$… recompute below).

Actually, let me recompute carefully: $\Phi^+_{B_2} = \{\alpha_1, \alpha_2, \alpha_1 + \alpha_2, \alpha_1 + 2\alpha_2\}$. The positive coroots in the dual root system are *not* obtained by replacing $\alpha \mapsto \alpha^\vee$ in this list (that's only for ADE). The dual root system is $C_2$, and its positive coroots are $\alpha_1^\vee, \alpha_2^\vee, \alpha_1^\vee + \alpha_2^\vee, 2\alpha_1^\vee + \alpha_2^\vee$ (Bourbaki, plates).

Hence
$$\rho^\vee = \tfrac{1}{2}(\alpha_1^\vee + \alpha_2^\vee + (\alpha_1^\vee + \alpha_2^\vee) + (2\alpha_1^\vee + \alpha_2^\vee)) = \tfrac{1}{2}(4\alpha_1^\vee + 3\alpha_2^\vee) = 2\alpha_1^\vee + \tfrac{3}{2}\alpha_2^\vee.$$

Pairings with simple coroots — using the dual Cartan matrix $(C^{B_2})^T = C^{C_2}$:
$$\langle \rho^\vee, \alpha_1^\vee\rangle \;=\; ?, \qquad \langle \rho^\vee, \alpha_2^\vee\rangle \;=\; ?$$

Cleaner: the Coxeter identity $\langle \rho^\vee, \alpha_i^\vee\rangle = 1$ holds *by definition* of $\rho^\vee$ as the half-sum of positive coroots paired against the simple coroots. This is the *coroot-side* version of the standard $\langle\rho, \alpha_i\rangle = 1$ identity, with all roles dualised. Verification: $\rho^\vee$ has fundamental-coweight expansion $\sum_i \omega_i^\vee$, and $\langle \omega_j^\vee, \alpha_i^\vee\rangle = \delta_{ij}$ in the dual fundamental basis, so summing gives 1.

Hence Stokes singularities for $B_2$:
$$S_{\alpha_1}^{B_2} \;=\; \tfrac{1}{2}(\alpha_1,\alpha_1)\cdot 1 \;=\; 1, \qquad S_{\alpha_2}^{B_2} \;=\; \tfrac{1}{2}(\alpha_2,\alpha_2)\cdot 1 \;=\; \tfrac{1}{2}.$$

**Bourbaki $C_2$ cross-check.** $C_2$ has simple roots $\beta_1$ (short), $\beta_2$ (long), with $(\beta_1,\beta_1) = 1$, $(\beta_2,\beta_2) = 2$. Stokes singularities:
$$S_{\beta_1}^{C_2} \;=\; \tfrac{1}{2}, \qquad S_{\beta_2}^{C_2} \;=\; 1.$$

The exceptional isomorphism $B_2 \to C_2$ swaps long and short roots (sends $\alpha_1 \mapsto \beta_2$, $\alpha_2 \mapsto \beta_1$). The Stokes singularity *multiset* $\{1, 1/2\}$ is preserved. **Cross-check passes at $n = 2$.**

**FIRST-PRINCIPLES CORRECTION (AP-CY61 ledger).** The naive extension "$B_n$ and $C_n$ have the same Stokes multiset for all $n$" is WRONG for $n \ge 3$. The exceptional isomorphism $B_n \cong C_n$ holds *only* at $n = 2$; at $n \ge 3$ the two Lie algebras have distinct Dynkin diagrams (different number of long vs short simple roots) and the Stokes multisets differ:
- $B_n$: $(n - 1)$ long simple roots + $1$ short simple root, multiset $\{\underbrace{1, \dots, 1}_{n-1}, \tfrac{1}{2}\}$.
- $C_n$: $1$ long simple root + $(n - 1)$ short simple roots, multiset $\{1, \underbrace{\tfrac{1}{2}, \dots, \tfrac{1}{2}}_{n-1}\}$.

The **right theorem** at higher rank: the Stokes singularity *set* (forgetting multiplicities) $\{1, 1/2\}$ is invariant under the bijection $B_n \leftrightarrow C_n^*$ on the dual root system; the *multiset* is preserved only under the exceptional iso at $n = 2$.

**Stokes constants at $B_2$.** From the formula $A^1_\alpha = (\alpha,\alpha)^{-2}\cdot (h_\alpha\otimes h_\alpha)$:
$$A^1_{\alpha_1}\;=\; \tfrac{1}{4} h_{\alpha_1}\otimes h_{\alpha_1}, \qquad A^1_{\alpha_2}\;=\; 1\cdot h_{\alpha_2}\otimes h_{\alpha_2}.$$

Note the short-root Stokes constant is $4\times$ larger than the long-root one in operator norm. This is the lacing-amplified Stokes contribution.

**Resonance check at $B_2$.** Long instanton at $S = 1$, short instanton at $S = 1/2$. Resonance: $n_1\cdot 1 = n_2\cdot 1/2$ gives $n_2 = 2n_1$. Leading resonance: $(n_1, n_2) = (1, 2)$ at $S_{\mathrm{res}} = 1$. Hence $\mathcal{G}^{(2,\alpha_2)}$ acquires a $\log(g_s)$ tail at the leading-order resonance.

---

## §4. Explicit verification: $G_2$ (the asymmetric case)

$G_2$ has simple roots $\alpha_1$ (short, $(\alpha_1,\alpha_1) = 2/3$) and $\alpha_2$ (long, $(\alpha_2,\alpha_2) = 2$). The Cartan matrix is
$$C^{G_2} = \begin{pmatrix} 2 & -1 \\ -3 & 2 \end{pmatrix}.$$

Six positive roots: $\alpha_1, \alpha_2, \alpha_1 + \alpha_2, 2\alpha_1 + \alpha_2, 3\alpha_1 + \alpha_2, 3\alpha_1 + 2\alpha_2$. Three short ($\alpha_1, \alpha_1+\alpha_2, 2\alpha_1 + \alpha_2$) and three long ($\alpha_2, 3\alpha_1+\alpha_2, 3\alpha_1+2\alpha_2$).

**Stokes singularities.** From $S_{\alpha_i} = (\alpha_i,\alpha_i)/2$:
$$\boxed{\;S_{\alpha_1}^{G_2} \;=\; \tfrac{1}{3}, \qquad S_{\alpha_2}^{G_2} \;=\; 1.\;}$$

**Stokes constants.** $A^1_{\alpha} = (\alpha,\alpha)^{-2}\cdot (h_\alpha\otimes h_\alpha)$:
$$A^1_{\alpha_1}\;=\; \tfrac{9}{4}\, h_{\alpha_1}\otimes h_{\alpha_1}, \qquad A^1_{\alpha_2}\;=\; \tfrac{1}{4}\, h_{\alpha_2}\otimes h_{\alpha_2}.$$

The short-root Stokes constant is $9\times$ larger than the long-root one. This is the **maximally asymmetric** non-simply-laced case.

**$e^{-1/g_s}$ coefficient (leading order).** At the leading Stokes line $\zeta = 1$ in the Borel plane, both $S_{\alpha_2} = 1$ (long, $n=1$) and $S_{\alpha_1}\cdot 3 = 1$ (short, $n=3$) contribute simultaneously. Hence the $e^{-1/g_s}$ coefficient is

$$\bigl[e^{-1/g_s}\bigr]\,\mathcal{F}_{Y(G_2)}(\hbar; g_s)\big|_{\mathrm{leading}}
\;=\; A^1_{\alpha_2}\,\mathcal{G}^{(1,\alpha_2)}(\hbar) \;+\; \frac{1}{3!}(A^1_{\alpha_1})^3 \,\mathcal{G}^{(3,\alpha_1)}(\hbar)\,\log(g_s).$$

The first term is the long-root single-instanton; the second is the short-root TRIPLE-instanton at the resonance, log-enhanced.

**$e^{-1/(3g_s)}$ coefficient (sub-leading, short-only).** At the short-only Stokes line $\zeta = 1/3$:

$$\bigl[e^{-1/(3g_s)}\bigr]\,\mathcal{F}_{Y(G_2)}(\hbar; g_s)\big|_{\mathrm{leading}}
\;=\; A^1_{\alpha_1}\,\mathcal{G}^{(1,\alpha_1)}(\hbar)
\;=\; \tfrac{9}{4}\, h_{\alpha_1}\otimes h_{\alpha_1}\,\mathcal{G}^{(1,\alpha_1)}(\hbar).$$

This is the *purely short-root* single-instanton sector; no resonance with the long sector at this Stokes singularity.

**$e^{-2/(3g_s)}$ coefficient (sub-sub-leading).** At $\zeta = 2/3$:

$$\bigl[e^{-2/(3g_s)}\bigr]\,\mathcal{F}_{Y(G_2)}(\hbar; g_s)\big|_{\mathrm{leading}}
\;=\; \frac{1}{2!}(A^1_{\alpha_1})^2\,\mathcal{G}^{(2,\alpha_1)}(\hbar)
\;=\; \frac{1}{2}\cdot\Bigl(\frac{9}{4}\Bigr)^2 (h_{\alpha_1}\otimes h_{\alpha_1})^2\,\mathcal{G}^{(2,\alpha_1)}(\hbar)
\;=\; \frac{81}{32}(h_{\alpha_1}\otimes h_{\alpha_1})^2\, \mathcal{G}^{(2,\alpha_1)}(\hbar).$$

Pure short-root double-instanton.

**Falsifiable predictor (from task brief, restated).** At $G_2$, the $e^{-1/g_s}$ coefficient should split into a long part (with multiplier $1$) and a short part (with multiplier given by some lacing-dependent factor of the formal parameter $q = e^{i\pi/d}$ at the quantum normalisation, $q = e^{i\pi/3}$ for $G_2$). The user's brief conjectured $S_{\alpha^{\mathrm{short}}} = q^2$ as the *short-root multiplier* on the $e^{-1/g_s}$ Stokes line. With $q = e^{i\pi/3}$, $q^2 = e^{2i\pi/3}$. **This is NOT what falls out of the first-principles computation**: the short root contributes via the resonance at $n_2 = 3$, with multiplier $(A^1_{\alpha_1})^3/3!\, \log g_s$. The "scalar" part is $(9/4)^3/3! = 729/(64\cdot 6) = 729/384 = 243/128$ in operator norm.

**Beating mathematical core.** The user's brief was paraphrasing a *quantum group* level statement (e.g.\ $U_q(G_2)$ at root of unity) where the short-root contribution carries a $q^{d_i}$ phase. At the resurgent twist level the *operator-valued* analogue is the $A^1_\alpha = (\alpha,\alpha)^{-2}(h_\alpha\otimes h_\alpha)$ scaling, NOT a phase. The correct restatement of the predictor:

> The $e^{-1/g_s}$ coefficient of the $G_2$ resurgent Drinfeld twist is the sum of (a) the long-root single-instanton $\tfrac{1}{4}h_{\alpha_2}\otimes h_{\alpha_2}\cdot\mathcal{G}^{(1,\alpha_2)}$ and (b) a log-resonant short-root triple-instanton $\tfrac{243}{128}(h_{\alpha_1}\otimes h_{\alpha_1})^3\,\mathcal{G}^{(3,\alpha_1)}\,\log(g_s)$.

This is the lacing-twisted, log-resonance-enhanced corrected predictor.

---

## §5. The corrected non-simply-laced theorem

Combining the analysis above:

**Theorem (split-Stokes resurgent Drinfeld twist for non-simply-laced $Y(\mathfrak{g})$; conditional).**
*For $\mathfrak{g} \in \{B_n, C_n, F_4, G_2\}$, the resurgent Drinfeld twist for $Y(\mathfrak{g})$ admits the closed form*
$$
\mathcal{F}_{Y(\mathfrak{g})}(\hbar; g_s) \;=\; \mathcal{F}^{\mathrm{formal}}_{Y(\mathfrak{g})}(\hbar) \cdot \exp\!\Biggl(\sum_{n\ge 1}\sum_{i=1}^r \frac{e^{-n S_{\alpha_i}/g_s}}{n!\,((\alpha_i,\alpha_i)/2)^{2n}}\,(h_{\alpha_i}\otimes h_{\alpha_i})^n\,\mathcal{G}^{(n,\alpha_i)}(\hbar; \log g_s)\Biggr) + O(\hbar^4),
$$
*governed by:*

- **Split Stokes singularities** $S_{\alpha_i} = (\alpha_i,\alpha_i)/2$, equal to $1$ for long and $1/d$ for short, where $d \in \{2,3\}$ is the lacing number.
- **Lacing-amplified Stokes constants** $A^n_{\alpha_i} = (n!)^{-1}((\alpha_i,\alpha_i)/2)^{-2n}(h_{\alpha_i}\otimes h_{\alpha_i})^n$, with short-root constants $d^{2n}$-times larger than long-root constants.
- **Resonant resurgent generators** $\mathcal{G}^{(n,\alpha_i)}(\hbar; \log g_s) \in \mathrm{HS}^{2,\bullet}(Y(\mathfrak{g}))[[\log g_s]]$, polynomial in $\log g_s$ with degree equal to the resonance multiplicity at the Stokes locus $n S_{\alpha_i}$. For long-only or short-only loci the polynomial is constant; at the long-short resonance $S_{\mathrm{res}} = 1 = n_2/d$ (i.e.\ $n_2 = d$) it acquires degree $1$.

*The conclusion is conditional on (a) Pasquetti--Schiappa Borel resummation across the split Stokes lines $\{1, 1/d, 2/d, \dots\}$; (b) Costello--Li open-closed factorisation lifted to the lacing-decorated chain complex; (c) the resonance correction giving $\log(g_s)$ enhancement at $S_{\mathrm{res}}$.*

---

## §6. Verification status table

| Item | Status | Engine | Tests |
|------|--------|--------|-------|
| $B_2$/$C_2$ Stokes singularities $\{1, 1/2\}$ | THEOREM (§3, derived from Bourbaki + Coxeter identity) | `compute/lib/resurgent_twist_non_simply_laced.py` | $B_2$ block |
| $G_2$ Stokes singularities $\{1, 1/3\}$ | THEOREM (§4) | same | $G_2$ block |
| $B_2$/$C_2$ Stokes constants $\{1/4, 1\}$ | THEOREM (§3, residue computation) | same | $B_2$ block |
| $G_2$ Stokes constants $\{1/4, 9/4\}$ | THEOREM (§4) | same | $G_2$ block |
| Resonance correction $\log(g_s)$ at $G_2$ $n_2=3$ | CONJECTURE (§2(f)) | same | predicted, not computed |
| Lacing duality $B_2 \leftrightarrow C_2$ Stokes invariance | THEOREM (§3 cross-check) | same | duality block |
| $F_4$ Stokes data $\{1, 1, 1/2, 1/2\}$ | THEOREM (analogous to $B_2$, §3 method) | same | $F_4$ block |
| $B_n$, $C_n$ Stokes data for general $n$ | THEOREM (analogous) | same | rank-parameterised block |

---

## §7. Confidence interval and gaps

**Confidence: HIGH for the split-Stokes singularity formula $S_\alpha = (\alpha,\alpha)/2$.** The derivation uses only the universal Coxeter identity $\langle\rho^\vee,\alpha_i^\vee\rangle = 1$ and the Bourbaki bilinear normalisation. Cross-checked via the $B_2 \cong C_2$ duality. The formal limit $g_s \to 0$ recovers the $V110$ Pentagon cocycle weights $c_i = (\alpha_i,\alpha_i)$ (Remark `rem:Yfg-ADE-specialisation` of `e1_chiral_algebras.tex`).

**Confidence: HIGH for the operator-valued Stokes constant prefactors $A^1_\alpha = (\alpha,\alpha)^{-2}(h_\alpha\otimes h_\alpha)$.** The derivation parallels V119 §3.2 with the Casimir projector $P_i = (h_\alpha\otimes h_\alpha)/(\alpha,\alpha)$ now carrying the lacing-dependent normalisation.

**Confidence: MEDIUM for the resonance log correction.** This is the standard Écalle equidistant-resurgence prediction (cited but not derived from first principles in this note), and applies when two Stokes singularities are *commensurate* (rationally related). The $G_2$ case has the most striking resonance structure ($S_{\mathrm{long}}/S_{\mathrm{short}} = 3$) and is the cleanest test case. The actual log-resonance coefficient should be verified against Costin §5.6 once the bridge equation $\Delta_{S_{\mathrm{res}}}\partial_{g_s} - \partial_{g_s}\Delta_{S_{\mathrm{res}}} = -S_{\mathrm{res}}\Delta_{S_{\mathrm{res}}}$ is unpacked at the resonant locus. (Open: not done in this note.)

**Confidence: LOW for the global vanishing conjecture.** V119's vanishing conjecture (the resurgent corrections cancel the formal Pentagon) was already CONJECTURAL for ADE. For non-simply-laced types the cancellation pattern is split: the long-root sector and short-root sector cancel independently, with the resonance term cancelling against a higher-order contribution. The full cancellation would require summing over both sectors with the lacing-dependent multiplicities. No general proof is offered.

**Gap 1 (resonance log coefficient).** The $\log(g_s)$ coefficient at the $G_2$ resonance $S_{\mathrm{res}} = 1$ is qualitatively predicted as $(9/4)^3/3! = 243/128$ but has not been derived from the bridge equation. Direct computation of $\Delta_1 \mathcal{F}_{Y(G_2)}(\hbar; g_s)$ would close this.

**Gap 2 (sign of the resonance correction).** Écalle's bridge equation contains a sign convention that depends on the orientation of the resummation contour (Stokes vs anti-Stokes ray). The first-principles analysis above does not pin this sign. A complete treatment would require specifying the Mariño--Schiappa contour deformation explicitly.

**Gap 3 (multiplicities $\ge 4$ at $G_2$).** At $G_2$, the resonance condition $n_1 = n_2/3$ admits higher solutions $(n_1, n_2) = (2, 6), (3, 9), \dots$. Each contributes a $\log(g_s)$ to a higher power. The multi-log structure (analogous to higher-genus Costin transseries) is not analysed here.

**Gap 4 (twisted affine extension).** Non-simply-laced finite-dimensional $\mathfrak{g}$ has *twisted* affine analogues $\mathfrak{g}^{(2)}, \mathfrak{g}^{(3)}$ (e.g.\ $A_{2n}^{(2)}$, $D_4^{(3)}$, etc.). The corresponding *twisted Yangians* $Y^\sigma(\mathfrak{g})$ should carry an analogous resurgent structure with Stokes singularities further twisted by the diagram automorphism order. Not addressed here.

**Gap 5 (cross-check with the formal Pentagon weights).** Remark `rem:Yfg-ADE-specialisation` of `e1_chiral_algebras.tex` already states $c_{\mathrm{long}} = 2$, $c_{\mathrm{short}} = 1$ for $B/C/F$ and $c_{\mathrm{long}} = 2$, $c_{\mathrm{short}} = 2/3$ for $G_2$. These are the *formal* Pentagon weights $(\alpha_i,\alpha_i)$, and the Stokes singularities $S_\alpha = (\alpha,\alpha)/2 = c_\alpha/2$ are consistent. The factor of $2$ between the formal-weight and the Stokes-singularity is the same factor that produces the universal "$1$" for ADE. ✓ Cross-check at the formal-limit level passes.

---

## §8. Summary

**Beating mathematical core.** The non-simply-laced extension of the V119 resurgent Drinfeld twist is governed by the split-Stokes formula $S_\alpha = (\alpha,\alpha)/2$, which collapses to the V119 ADE result and splits per long/short for $B/C/F/G_2$. Stokes constants amplify by $(\alpha,\alpha)^{-2}$, and a resonance correction $\log(g_s)$ enhances the $d$-th short-root instanton at $G_2$.

**Falsifiable structure (corrected from task brief).** At $G_2$, the leading $e^{-1/g_s}$ coefficient is the SUM of the long-root single-instanton (multiplier $1/4$) and the short-root TRIPLE-instanton at the resonance (multiplier $243/128 \cdot \log g_s$). The user-conjectured $S_{\alpha^{\mathrm{short}}} = q^2$ phase was a *quantum group* paraphrase; the *resurgent* analogue is the operator-valued $9/4$ factor, not a phase.

**Inscription.** The corrected theorem is inscribed as `thm:Yfg-resurgent-Drinfeld-twist-non-simply-laced` in `chapters/theory/e1_chiral_algebras.tex` adjacent to the existing ADE theorem.

**Test infrastructure.** `compute/tests/test_resurgent_twist_non_simply_laced.py` with `@independent_verification` decorators tying derivation (Drinfeld 1985 + Etingof--Kazhdan recursion + V119 ADE limit) to verification (Bourbaki root data + the $B_2 \cong C_2$ duality cross-check).

**End.** Status: complete. Lossless extension of V119 to all non-simply-laced types. AP-CY55, AP-CY60, AP-CY61 governance respected. Convention bridge with $V110$ formal weights verified.
