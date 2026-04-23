# Closure 3B-C11 (Opus 4.7 relaunch) — mvKY route for anti-diagonal $\mathrm{Hilb}^{n_1,n_2}(K3\times K3)$

## Terminal state

**C** (Gap).

The candidate multi-variable-Kawai–Yoshioka factorisation

$$
\sum_{n_1, n_2, \beta_1, \beta_2, d} \chi\!\bigl(\mathrm{Hilb}^{n_1, n_2}_{\mathrm{anti\text{-}diag}}(K3\times K3)\bigr)\, q_1^{n_1} q_2^{n_2} y_1^{\langle \gamma_1, \gamma_1 \rangle/2} y_2^{\langle \gamma_2, \gamma_2 \rangle/2} p^{d}
\;\stackrel{?}{=}\;
\phi_{0,1}(q_1, y_1)\,\phi_{0,1}(q_2, y_2)\cdot \prod_{n\geq 1}(1 - p^n)^{-24}
$$

of the prior C11 memo **cannot be verified as a Euler-characteristic identity for a concrete moduli stack at small $(n_1, n_2)$** from first principles. The factorisation as stated is **mathematically inconsistent at $y_1 = y_2 = 1$** (the Euler-characteristic specialisation): on the RHS, $\phi_{0,1}(q, 1) = 12$ identically, forcing the RHS to collapse to a $q_1, q_2$-independent constant $144/\prod(1-p^n)^{24}$, whereas any genuine Euler-characteristic generating function on a bi-K3 Hilbert structure must be $q_1, q_2$-non-constant.

The gap is structural, not computational: the "anti-diagonal $\mathrm{Hilb}^{n_1, n_2}(K3\times K3)$" is not a standard geometric object in the primary literature, and the factorisation belongs to the *Jacobi-form input* layer of the Borcherds singular theta correspondence, not to the *Euler-characteristic* layer of a Kawai–Yoshioka-type Hilbert-scheme formula.

## First-principles computations performed

### (A) Göttsche's formula (verified independently).

The generating function quoted in the task,
$$
\sum_{n\geq 0} \chi(\mathrm{Hilb}^n K3)\, q^n = \prod_{n\geq 1}(1 - q^n)^{-24},
$$
is Göttsche 1990 *Math. Ann.* **286** Theorem 1 applied to $K3$ (using $\chi(K3) = 24$). I verified it by direct product expansion to $n=6$:

| $n$ | $\chi(\mathrm{Hilb}^n K3) = p_{24}(n)$ |
|---:|---:|
| 0 | 1 |
| 1 | 24 |
| 2 | 324 |
| 3 | 3 200 |
| 4 | 25 650 |
| 5 | 176 256 |
| 6 | 1 073 720 |

These are the standard values of $p_{24}(n)$ (the number of $24$-coloured partitions of $n$), matching the coefficients of $1/\eta(q)^{24}$ up to the $q^{-1}$ shift. The Künneth product for $\mathrm{Hilb}^{n_1}(K3_1) \times \mathrm{Hilb}^{n_2}(K3_2)$ is
$$
\chi\!\bigl(\mathrm{Hilb}^{n_1}(K3_1) \times \mathrm{Hilb}^{n_2}(K3_2)\bigr) = p_{24}(n_1)\, p_{24}(n_2).
$$
For example: $(n_1, n_2) = (2, 3) \Rightarrow 324 \cdot 3200 = 1\,036\,800$; $(n_1, n_2) = (3, 3) \Rightarrow 3200^2 = 10\,240\,000$.

### (B) $\phi_{0,1}(q, y)$ computed from Jacobi-theta realisation.

Using $\phi_{0,1}(\tau, z) = 4\,\sum_{i=2,3,4} \theta_i(\tau, z)^2 / \theta_i(\tau, 0)^2$ and direct theta-series expansion, I computed (verifying against Eguchi–Ooguri–Tachikawa 2010 arXiv:1004.0956 for the $K3$ elliptic genus $2\,\phi_{0,1}$):

$$
\phi_{0,1}(q, y)
= (y^{-1} + 10 + y)
+ q\,(10 y^{-2} - 64 y^{-1} + 108 - 64 y + 10 y^2)
+ q^2\,(y^{-3} + 108 y^{-2} - 513 y^{-1} + 808 - 513 y + 108 y^2 + y^3)
+ q^3\,(-64 y^{-3} + 808 y^{-2} - 2752 y^{-1} + 4016 - 2752 y + 808 y^2 - 64 y^3)
+ q^4\,(10 y^{-4} - 513 y^{-3} + 4016 y^{-2} - 11775 y^{-1} + 16524 - 11775 y + 4016 y^2 - 513 y^3 + 10 y^4)
+ O(q^5).
$$

**Pivotal identity.** $\phi_{0,1}(q, 1) = 12$ as a formal power series in $q$. That is, every coefficient of $q^n$ in $\phi_{0,1}(q, 1)$ for $n \geq 1$ vanishes:
$$
q^0: 1 + 10 + 1 = 12,\quad q^1: 10 - 64 + 108 - 64 + 10 = 0,\quad q^2: 2 + 216 - 1026 + 808 = 0,\quad \ldots
$$
This is a consequence of the Witten index of $K3$ being $24$ at all $\tau$, so $\chi_y(K3)\bigr|_{y=1} = 24$ for all $\tau$, giving $\phi_{0,1}(\tau, 0) = 12$ for all $\tau$ (Eichler–Zagier 1985 Thm 9.3; see also Eguchi–Ooguri–Tachikawa 2010).

### (C) Collapse at $y_1 = y_2 = 1$ of the candidate factorisation.

The candidate RHS at $y_1 = y_2 = 1$ equals
$$
\phi_{0,1}(q_1, 1)\,\phi_{0,1}(q_2, 1)\,\prod_{n\geq 1}(1 - p^n)^{-24} = 12 \cdot 12 \cdot \prod(1 - p^n)^{-24} = \frac{144}{\prod_{n\geq 1}(1 - p^n)^{24}}.
$$
**The RHS is independent of $(q_1, q_2)$ at $y_1 = y_2 = 1$.**

Any Euler-characteristic generating function $\sum \chi(\mathcal M_{n_1, n_2, \bullet})\, q_1^{n_1} q_2^{n_2} \cdots$ for a $(n_1, n_2)$-indexed family of bi-K3 moduli spaces (Hilbert or otherwise) cannot collapse to a $(q_1, q_2)$-independent constant unless $\chi(\mathcal M_{n_1, n_2, \bullet}) = 0$ for $(n_1, n_2) \neq (0, 0)$ at the $y_1 = y_2 = 1$ specialisation — an implausible configuration for any natural anti-diagonal reduction.

Specifically, the Künneth–Göttsche product $\bigl(\sum p_{24}(n) q^n\bigr)^2$ has all coefficients positive and grows rapidly:
$$
\bigl(\text{Künneth–Göttsche}\bigr)\bigr|_{(q_1 = q_2 = 0)} = 1,\quad \bigl|_{(q_1^1 q_2^0)} = 24,\quad \bigl|_{(q_1^1 q_2^1)} = 576,\quad \ldots
$$
versus $\bigl(\text{candidate RHS}\bigr)\bigr|_{y_1 = y_2 = 1, p = 0} = 144$ (constant). These two series are incompatible as Euler-characteristic generating functions for any common geometric object.

### (D) The real Kawai–Yoshioka 2000 formula.

Kawai–Yoshioka 2000 (arXiv:hep-th/0002169, Theorem 1) computes the generating function for the Hirzebruch $\chi_y$-genus of moduli spaces of *stable sheaves* on $K3$ with fixed Mukai vector (not Hilbert schemes of points). In their eq.(1.9), summing over Mukai vectors $v = (r, c_1, c_2)$ at $r = 1$ gives
$$
\sum_v \chi_y\!\bigl(M_H(v)\bigr)\, q^{\langle v, v\rangle/2 + 1} y^{c_1 \cdot \alpha} \;=\; \frac{\phi_{0,1}(q, y)}{\eta(q)^{24}}
\;=\; \phi_{0,1}(q, y)\, q^{-1}\, \prod_{n\geq 1} (1 - q^n)^{-24}.
$$

**The $\eta^{-24}(q)$ factor is essential.** At $y = 1$: RHS $= 12\, q^{-1} \prod(1 - q^n)^{-24}$, non-constant in $q$, recovering $12\, p_{24}(n+1)$ at the $q^n$ coefficient. This is NOT what appears in the C11-memo mvKY hypothesis, which writes $\phi_{0,1}(q_1, y_1)\phi_{0,1}(q_2, y_2)/\prod(1 - p^n)^{24}$ *without* the $\eta^{-24}(q_1)\eta^{-24}(q_2)$ K3-elliptic factors.

A correctly-normalised bi-KY generating function would read
$$
Z_{\text{bi-KY}}(q_1, q_2, y_1, y_2, p)
\;=\;
\frac{\phi_{0,1}(q_1, y_1)}{\eta^{24}(q_1)} \cdot \frac{\phi_{0,1}(q_2, y_2)}{\eta^{24}(q_2)} \cdot (\text{elliptic factor in } p),
$$
which at $y_1 = y_2 = 1$ has non-trivial $(q_1, q_2)$ dependence via the $\eta^{-24}$ factors. The C11-memo form obscures this by dropping the single-K3 $\eta^{-24}$ factors.

### (E) The intended reading of "mvKY" in the Borcherds-lift architecture.

The Borcherds 1995 alg-geom/9506003 §7 singular theta correspondence (Theorem 7.1) constructs $\Phi_{12}$ as the automorphic product attached to the weak Jacobi form
$$
\frac{\theta_{\Lambda_{24}}(\tau, z)}{\eta^{24}(\tau)}
$$
on the rank-$26$ even unimodular lattice $\mathrm{II}_{26,2}$, where $\theta_{\Lambda_{24}}$ is the Leech-lattice theta series and $\eta^{-24}$ supplies the $q^{-1}$ weight-$(-12)$ normalisation.

The C11-memo "mvKY" hypothesis is not literally a Kawai–Yoshioka Hilbert-scheme generating function. It is a claim at the *Jacobi-form-input* layer of the Borcherds lift: that the doubly-reduced equivariant virtual Euler characteristic of $\mathcal M^{\mathrm{red},\mathrm{red}}_{\mathrm{DT}}(K3\times K3\times E)$, after Niemeier projection onto the Leech slice $\Lambda_{24}$, produces a *single* weak Jacobi form on $\mathrm{II}_{26,2}$ equivalent to $\theta_{\Lambda_{24}}/\eta^{24}$. The decomposition
$$
\Theta_{\Lambda_{24}}(\tau, z_1, z_2) \;\mapsto\; \phi_{0,1}(\tau, z_1)\, \phi_{0,1}(\tau, z_2) \cdot (\text{lattice-twist factor})
$$
is a *formal identity* among Jacobi forms on a rank-$24$ Niemeier slice — specifically, the decomposition of the Leech theta series under a splitting $\Lambda_{24} \supset \Lambda_{K3}^{\mathrm{sym}} \oplus \Lambda_{K3}^{\mathrm{asym}}$ coming from the K3-K3 anti-diagonal embedding.

**This is a statement about modular forms, not about Euler characteristics of Hilbert schemes.** The C11-memo writes it with $(q_1, q_2, y_1, y_2)$ variables as though it were a two-step bi-Kawai–Yoshioka generating function, conflating the two layers.

## Why the claim fails the leading-order test

At leading order $q_1 = q_2 = 0$ and $y_1 = y_2$ arbitrary, the candidate RHS gives
$$
\phi_{0,1}(0, y_1)\,\phi_{0,1}(0, y_2) = (y_1^{-1} + 10 + y_1)(y_2^{-1} + 10 + y_2),
$$
with Laurent coefficients in $(y_1, y_2)$:
$$
\begin{array}{|c|c|c|c|}
\hline (y_1, y_2) & y_1^{-1} & 1 & y_1 \\ \hline
y_2^{-1} & 1 & 10 & 1 \\ \hline
1 & 10 & 100 & 10 \\ \hline
y_2 & 1 & 10 & 1 \\ \hline
\end{array}
$$

For this to match a bi-K3 Hilbert-scheme Euler-characteristic table at $(n_1, n_2) = (0, 0)$, we would need exactly one geometric object (the empty bi-punctual scheme) with nine distinct Mukai-weight decompositions producing precisely the $9$-entry table above. No such decomposition is published. In particular:

- The lone $(n_1, n_2) = (0, 0)$ Hilbert scheme is a single point $\mathrm{Spec}\,\mathbb{C}$, $\chi = 1$, with no natural $9$-dimensional Mukai-charge stratification.
- The coefficient $100 = 10 \cdot 10$ at $(y_1^0, y_2^0)$ matches neither $\chi(K3)^2 = 576$ nor $\chi(\mathcal{O}_{K3})^2 = 4$.
- The values $c(0, 0)_{\phi_{0,1}} = 10$ identify with the Mukai-lattice "signature-$10$" from the $\langle \gamma, \gamma \rangle = 0$ stratum of $\Lambda_{K3}$, not with any Hilbert-scheme Euler count.

## Why the C11 memo's B (conditional closure) status is not A (verified).

Closure 3B asked whether the B-status theorem of C11 can be upgraded to A (verified) via the mvKY route. The answer is **no**:

1. The mvKY hypothesis as written in the prior C11 memo is not a published theorem of Kawai–Yoshioka or anyone else; Kawai–Yoshioka 2000 proves a *single-K3* $\chi_y$-generating function for *stable-sheaf moduli* (not Hilbert schemes), with a $\phi_{0,1}/\eta^{24}$ formula, not a $\phi_{0,1}$ formula without the $\eta^{24}$ denominator.
2. The "anti-diagonal $\mathrm{Hilb}^{n_1, n_2}(K3\times K3)$" is undefined in the primary literature; Hilbert schemes of points on a $4$-fold are singular from length $4$ onwards (Iarrobino 1972), so a direct Euler-characteristic computation requires either (a) passing to relative Hilbert schemes over a base (as in Oberdieck–Pixton's $K3\times E$ setup, which does not generalise to $K3\times K3$), or (b) passing to virtual/perfect-obstruction-theory Euler characteristics (the true Donaldson–Thomas setup, which is precisely the MPT$^{\otimes 2}$ hypothesis — exactly what is *not* established).
3. The factorisation as stated collapses at $y_1 = y_2 = 1$, which is the Euler-characteristic specialisation. No naive Euler-characteristic generating function can equal the C11-memo candidate.

The C11 B-status is therefore **stable**: the Fake-Monster character formula $\chi(Y^+(K3_1\times K3_2\times E))\cdot\pi_{\mathrm{Niem}, *} = 1/\Phi_{12}$ remains conditional on two non-published hypotheses (MPT$^{\otimes 2}$ for the virtual-cycle side, and the Leech-theta decomposition identity for the Jacobi-form-input side). The mvKY route as formulated in the prior memo does not constitute a route to A.

## Corrected formulation of the Jacobi-form-input hypothesis (for future work)

The hypothesis that *would* close the gap is:

**(JFI-Leech).** The Niemeier-projected doubly-reduced equivariant virtual Euler characteristic of $\mathcal M^{\mathrm{red},\mathrm{red}}_{\mathrm{DT}}(K3_1\times K3_2\times E)$ at bi-primitive Mukai charge $(\gamma_1, \gamma_2)$ produces a weak Jacobi form on $\mathrm{II}_{26,2}$ equivalent to
$$
\frac{\theta_{\Lambda_{24}}(\tau, Z)}{\eta^{24}(\tau)},
$$
where $\theta_{\Lambda_{24}}$ is the Leech-lattice theta series (Conway–Sloane 1988 Chapter 4) and $Z$ runs over the rank-$24$ Leech slice of $\mathrm{II}_{26,2}$.

This is an honest single-Jacobi-form identity, not a bi-Jacobi product, and it is the correct Jacobi input for Borcherds' singular theta lift to $\Phi_{12}$. The relation to $\phi_{0,1}(q_1, y_1)\phi_{0,1}(q_2, y_2)$ is indirect: under a K3–K3 anti-diagonal decomposition
$$
\Lambda_{24} \;\cong\; \Lambda_{K3}^{\mathrm{sym}}(-1) \oplus \Lambda_{K3}^{\mathrm{asym}}(-1) \oplus U
$$
(conjectural at this scope; not established in Conway–Sloane 1988), $\theta_{\Lambda_{24}}$ factors as a theta series on $\Lambda_{K3}^{\mathrm{sym}}$ times a theta series on $\Lambda_{K3}^{\mathrm{asym}}$, each of which may be related to a $\phi_{0,1}$-type Jacobi form via individual-K3 elliptic-genus identifications. **The decomposition does *not* naively factor into $\phi_{0,1}(q_1, y_1)\phi_{0,1}(q_2, y_2)$** — that is the content of the gap.

## Route forward

To push C11 from B to A, the correct sequence is:

1. **State (JFI-Leech)** as the precise Jacobi-form input hypothesis (not the C11-memo's bi-Jacobi factorisation).
2. **Verify (JFI-Leech)** via the Niemeier–Leech lattice-theta identity and the Schiffmann–Vasserot K3 CoHA character as Mukai-lattice theta function.
3. **Maintain MPT$^{\otimes 2}$** as the (still open) virtual-cycle hypothesis.

Neither step 1 nor step 2 is completed here. The closure terminates at C.

## Inscription: revised conditional theorem

```tex
\begin{theorem}[Fake-Monster doubly-reduced DT integrand, Jacobi-form-input conditional]
\label{thm:fake-monster-doubly-reduced-DT-JFI}
\ClaimStatusConjectured
Let $X = K3_1 \times K3_2 \times E$ be the compact projective Calabi--Yau
fivefold with holomorphic volume form
$\Omega_5 = \sigma_{K3_1} \wedge \sigma_{K3_2} \wedge dz_E$,
$\mathcal{M}^{\mathrm{red},\mathrm{red}}_{\mathrm{DT}}(X; \gamma)$
the doubly-reduced DT moduli stack at $K3\times K3$-bi-primitive Mukai
charge $\gamma$, and $A^{\mathrm{FM}}_E = H^\bullet_{\mathrm{eq}}(
\mathcal{M}^{\mathrm{red},\mathrm{red}}_{\mathrm{DT}}(X), \phi_W)$ its
positive-half cohomological Hall algebra. Let
$\pi_{\mathrm{Niem}}\colon \mathrm{II}_{3,27} \twoheadrightarrow
\mathrm{II}_{25,1} = \Lambda_{24} \oplus U$ be the Niemeier projection
onto the Leech slice. Under two hypotheses
\textup{(MPT$^{\otimes 2}$)} --- iterated MPT obstruction reduction on
$K3_1\times K3_2\times E$ ---
and \textup{(JFI-Leech)} --- the Jacobi-form-input identification
$\pi_{\mathrm{Niem}, *}\,\chi_{A^{\mathrm{FM}}_E} = \theta_{\Lambda_{24}}/\eta^{24}$
as a weak Jacobi form on $\mathrm{II}_{26,2}$ ---
the equivariant character of $A^{\mathrm{FM}}_E$ after
$\pi_{\mathrm{Niem}}$-pushforward satisfies
$\pi_{\mathrm{Niem}, *}\,\chi_{A^{\mathrm{FM}}_E}(q, Z) = 1/\Phi_{12}(Z)$
with $\kappa_{\mathrm{BKM}}(\Phi_{12}) = c(0)/2 = 12$.
\end{theorem}
```

(The revised hypothesis (JFI-Leech) replaces the C11-memo (mvKY) hypothesis; the two are distinct, and only (JFI-Leech) is compatible with the Borcherds singular theta correspondence at rank-$24$.)

## Primary sources consulted

- Göttsche 1990 *Math. Ann.* **286** Theorem 1 (Hilbert-scheme Euler generating function on surfaces).
- Kawai–Yoshioka 2000 arXiv:hep-th/0002169 Theorem 1 / eq. (1.9) (single-K3 stable-sheaf $\chi_y$-generating function $= \phi_{0,1}/\eta^{24}$).
- Eichler–Zagier 1985 *Theory of Jacobi Forms* Theorem 9.3 ($\phi_{0,1}$ weak-Jacobi-form structure).
- Eguchi–Ooguri–Tachikawa 2010 arXiv:1004.0956 (K3 elliptic genus $= 2\phi_{0,1}$, Mathieu moonshine decomposition).
- Borcherds 1995 alg-geom/9506003 §7 Theorem 7.1 (singular theta correspondence for $\Phi_{12}$ from $\theta_{\Lambda_{24}}/\eta^{24}$).
- Borcherds 1998 *J. reine angew. Math.* **494** Theorem 13.3 (Borcherds-lift weight identity $\kappa_{\mathrm{BKM}}(\Phi_{12}) = c(0)/2 = 12$).
- Conway–Sloane 1988 *Sphere Packings* Chapters 4, 10, 18, 27 (Leech theta series; Niemeier no-roots condition; M$_{23} \subset M_{24} \subset \mathrm{Co}_1$).
- Maulik–Pandharipande–Thomas 2010 arXiv:1001.2719 Theorem 1 (single-$\sigma$-symplectic MPT reduction on K3).
- Iarrobino 1972 *Amer. J. Math.* **94** (Hilbert scheme of points on $\geq 3$-fold singular from length $4$).

## Cross-references

- Prior closure: `/Users/raeez/calabi-yau-quantum-groups/.swarm_outputs/wave3/C11_fake_monster_DT_integrand.md` (B-status, with the mvKY hypothesis as-written).
- Related notes: `/Users/raeez/calabi-yau-quantum-groups/notes/wave18_g1_K3K3E_d5_gluing.tex` (attack-heal cycles for the same character formula; reaches B-status without the mvKY route).
- K3-fibre machinery: `/Users/raeez/calabi-yau-quantum-groups/notes/wave18_f4_Hilb_K3E_equivariant.tex` (Göttsche-type survival on $\mathbb{C}^\times_E$-equivariant reduction for the $K3\times E$ case; does *not* extend to $K3\times K3$ for the reason above — no residual $\mathbb{C}^\times$ on the bi-K3 side).
- Supporting computation: `/Users/raeez/calabi-yau-quantum-groups/notes/elliptic_K3K3_bigraded_Lefschetz.md` (K3$\times$K3 bigraded Lefschetz matrix; confirms no Drinfeld-coupling correction for K3$\times$K3 under the Klein-four convolution, unrelated to the present Euler-characteristic question).

— Raeez Lorgat, 2026-04-22.
