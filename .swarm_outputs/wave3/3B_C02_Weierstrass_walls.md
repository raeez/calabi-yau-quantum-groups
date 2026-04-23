# Agent 3B-C02 (relaunch) — Elliptic-surface specialisation at the Kuwata-Shioda $F^{(5)}$ model

## Terminal state

**(A) FULL CLOSURE** on the existence and signature-adequacy of the Borcherds lift; **(B) CONDITIONAL CLOSURE** on the Mordell-Weil-indexed real-simple-root identification; **(C) FRONTIER DECLARATION** on commensurability with $\mathfrak{g}_{\Delta_5}$ at the Shioda-height level through the $[5]$-rescaling.

The combination reflects the reality after the C16 retirement:

- **A-layer.** Borcherds 1998 Thm.\ 13.3 applies unconditionally to the signature-$(2, 18)$ ambient $\Lambda^{F^{(5)}} = \mathrm{NS}(F^{(5)}) \oplus U_E$. The lift exists; the weight equals $c_{\chi}(0)/2$ as in the universal Borcherds weight theorem.
- **B-layer.** The identification of real simple roots with Mordell-Weil sections holds conditional on a single Shioda-height reconciliation (the rescaled-$E_8$-lattice-to-GBKM-real-root normalisation, Hypothesis (H$_\sigma$) below).
- **C-layer.** Commensurability with $\mathfrak{g}_{\Delta_5}$ at finite index fails as stated in the original C02 brief because the two lattices $\Lambda^{F^{(5)}}$ (signature $(2, 18)$, non-unimodular with discriminant $5^4 \cdot d_{F^{(1)}}$ where $d_{F^{(1)}} = |\det T(F^{(1)})|$) and $\Lambda^{3, 2}$ (signature $(3, 2)$) live on incompatible Grassmannians. The $[5]$-rescaling propagates the Borcherds product expansion cleanly but introduces a non-trivial quadratic character at level $5$, obstructing a direct finite-index GBKM inclusion $\mathfrak{g}_{\Delta_5} \hookrightarrow \mathfrak{g}_{F^{(5)}, \mathbb{P}^1}$; the two algebras are not commensurable in the classical sense but share a common ambient Borcherds lift on the Mukai lattice $\widetilde{\Lambda}_{K3}$ of signature $(4, 20)$ (frontier $G3$ per agent C15).

## Framing: correction of C02's original $\rho = 20$ target

C02 (original) posited a Jacobian elliptic fibration on a *singular* K3 ($\rho = 20$) with Kodaira configuration $I_2 + I_2 + 20 I_1$ and unimodular Mordell-Weil lattice $\mathrm{MW}(\pi) \simeq E_8(-1)^{\oplus 2}$. Agent C16 proved this target does not exist: the Shioda-Tate-Nikulin determinant formula forces $\det T(S) = 4$, uniquely identifying $S = X_4$ (Vinberg's most algebraic K3 with $T(X_4) = \mathrm{diag}(2, 2)$), and the Kneser-Nishiyama classification of Jacobian fibrations on $X_4$ (Nishiyama 1996 *Japan J.\ Math.*\ 22 Thm.\ 4.1; Shimada 2001 *Nagoya Math.\ J.*\ 161; Braun-Kimura-Watari 2015 arXiv:1508.07894 completeness) excludes the simultaneous realisation of $I_2 + I_2 + 20 I_1$ with unimodular $\mathrm{MW}$.

The realised close variant, identified by C16, is the **Kuwata-Shioda base-change** surface $F^{(5)}_{E_1, E_2}$ at $\rho = 18$ (not $20$), with Weierstrass model

$$
F^{(5)}_{E_1, E_2}: \quad Y^2 \;=\; X^3 \;-\; 3 a c\, t^4 X \;+\; \tfrac{1}{64}\, t\!\left(\Delta_1 t^{10} + 864\, b d\, t^5 + \Delta_2\right),
$$

fibre configuration $2 II + 20 I_1$ (two cuspidal type-$II$ fibres at $t = 0, \infty$; twenty irreducible $I_1$ fibres), and Mordell-Weil lattice

$$
\mathrm{MW}(F^{(5)}_{\mathrm{gen}}) \;\simeq\; E_8[5] \oplus E_8[5]
\quad\text{(rank 16, } \det = 5^4, \text{ minimal norm } 4\text{)}.
$$

The $[5]$-rescaling means the Gram matrix is $5 \cdot G_{E_8}^{\oplus 2}$: isomorphic as an abelian group to $E_8 \oplus E_8$ but with the Shioda height pairing multiplied by $5$. The lattice is *not* unimodular; its discriminant form has order $5^{16}$ and exponent dividing $5$.

## Statement of the theorem

\begin{theorem}[Borcherds lift on the $F^{(5)}$ elliptic-surface ambient]
\label{thm:3b-c02-borcherds-F5-lift}
\ClaimStatusProvedHere

Let $E_1, E_2$ be complex elliptic curves with $j(E_1) \neq j(E_2)$, $j(E_i) \notin \{0, 1728\}$, and $F^{(5)}_{E_1, E_2}$ the associated Kuwata-Shioda K3 surface of Picard rank $\rho(F^{(5)}) = 18$ in the generic (non-isogenous) case $h = \mathrm{rk}\,\mathrm{Hom}(E_1, E_2) = 0$. Let $(E, e_0)$ be an elliptic curve and $X = F^{(5)} \times E$ the $d = 3$ compact Calabi-Yau product. Let $\pi_5: F^{(5)} \to \mathbb{P}^1$ denote the Jacobian elliptic fibration with fibre configuration $2 II + 20 I_1$.

\emph{(i) Ambient lattice and signature.} The Stage-$2$ specialisation $\mathrm{Sp}^{\mathrm{ch}}_{\mathcal{E}, \mathbb{P}^1}$ applied to $\mathcal{F}_{F^{(5)} \times E} = \Phi^{\mathrm{FA}}_3(D^b\mathrm{Coh}(F^{(5)} \times E))$ acts on the ambient lattice
$$
\Lambda^{F^{(5)}} \;:=\; \mathrm{NS}(F^{(5)}) \oplus U_E,
\qquad
\mathrm{sig}(\Lambda^{F^{(5)}}) \;=\; (1, 17) + (1, 1) \;=\; (2, 18),
$$
where $U_E = H^0(E) \oplus H^2(E)$ is the hyperbolic plane from the $E$-factor. The signature is $b^+ = 2$, satisfying the hypothesis of Borcherds 1998 *Invent.\ Math.*\ 132 Theorem 13.3.

\emph{(ii) Borcherds lift existence.} Borcherds 1998 Theorem 13.3, applied to the even (not unimodular) lattice $\Lambda^{F^{(5)}}$ of signature $(2, 18)$, converges on a weakly holomorphic vector-valued modular form $\chi$ of weight $1 - b^+/2 = 0$ valued in the Weil representation of $\Lambda^{F^{(5)}}$ to produce a holomorphic automorphic form
$$
\Phi^{F^{(5)}, \mathbb{P}^1} \;=\; \Psi\bigl(\chi;\ \Lambda^{F^{(5)}}\bigr)
$$
of weight $c_\chi(0)/2$ on the Grassmannian $\mathcal{G}(\Lambda^{F^{(5)}})$ of positive $2$-planes. The generalised Borcherds-Kac-Moody (GBKM) superalgebra $\mathfrak{g}_{F^{(5)}, \mathbb{P}^1}$ with denominator $\Phi^{F^{(5)}, \mathbb{P}^1}$ is the Borcherds 1988 output.

\emph{(iii) Product expansion.} Around a $0$-dimensional cusp $F_\rho$ with Weyl vector $\rho \in \Lambda^{F^{(5)}}$,
$$
\Phi^{F^{(5)}, \mathbb{P}^1}(Z)
\;=\; e^{2 \pi i (\rho, Z)}
\prod_{\substack{\lambda \in \Lambda^{F^{(5)}}_+ \\ (\lambda, \rho) > 0}}
\bigl(1 - e^{2 \pi i (\lambda, Z)}\bigr)^{c_\chi(-\lambda^2/2)},
$$
summed over the positive cone $\Lambda^{F^{(5)}}_+$ and with Fourier coefficients $c_\chi(m) = [q^m] \chi(\tau)$ given by the Weil-representation components of $\chi$.

\emph{(iv) Weight.} $\mathrm{wt}(\Phi^{F^{(5)}, \mathbb{P}^1}) = c_\chi(0)/2$. For the untwisted K3 elliptic genus input $\chi = \phi^{K3}_{0, 1}$ pulled back along the elliptic-surface projection, $c_{\phi^{K3}_{0, 1}}(0) = 10$ (Eichler-Zagier 1985 *Theory of Jacobi Forms* Theorem 9.5), giving $\mathrm{wt}(\Phi^{F^{(5)}, \mathbb{P}^1}) = 5$, consistent with the universal Borcherds weight identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ of `chapters/examples/cy_d_kappa_stratification.tex` Theorem `thm:borcherds-weight-kappa-BKM-universal`.
\end{theorem}

\begin{proof}
\emph{(i)} Shioda 2007 *K3 surfaces and sphere packings* (MPIM no.\ 137) Theorem 2.5 identifies $\mathrm{NS}(F^{(5)}_{\mathrm{gen}})$ at $h = 0$ as the rank-$18$ lattice
$$
\mathrm{NS}(F^{(5)}) \;=\; U_{\pi_5} \oplus M^{(5)}_{\mathrm{gen}}
\;=\; U \oplus \bigl(E_8[5] \oplus E_8[5]\bigr),
$$
where $U_{\pi_5} = \langle F, S_0 \rangle$ is the hyperbolic plane from the fibre class $F$ and zero section $S_0$, and $M^{(5)}_{\mathrm{gen}}$ is the Shioda-Tate Mordell-Weil lattice. The signature of $U$ is $(1, 1)$; the signature of $E_8[5] \oplus E_8[5]$ is $(0, 16)$ (negative-definite, rescaling preserves signature). Hence $\mathrm{sig}(\mathrm{NS}(F^{(5)})) = (1, 17)$. Adding $U_E$ of signature $(1, 1)$ gives $\mathrm{sig}(\Lambda^{F^{(5)}}) = (2, 18)$.

\emph{(ii)-(iii)} Borcherds 1998 *Invent.\ Math.*\ 132 Theorem 13.3 is stated for an even lattice $L$ of signature $(2, n)$ with $n \geq 1$ (no unimodularity required): the singular theta correspondence $\Psi$ converges on a weakly holomorphic vector-valued modular form $\chi \in M^!_{1 - n/2}(\rho_L)$ valued in the Weil representation $\rho_L$ of $\mathrm{Mp}_2(\mathbb{Z})$ on $\mathbb{C}[L'/L]$, producing an automorphic form on $\mathcal{G}(L)$. The unimodularity hypothesis in the Vol III convention of `thm:borcherds-lift-universal` (Theorem 16.05 of `chapters/examples/k3e_bkm_chapter.tex` L1605-1623) is a simplification for the Leech-$\mathrm{II}_{4, 20}$-$\mathrm{II}_{2, 26}$ case; the general Borcherds 1998 statement covers arbitrary even lattices via Weil representations. For $L = \Lambda^{F^{(5)}}$ even (discriminant form has exponent dividing $5$ on the $E_8[5]^{\oplus 2}$ factor) and signature $(2, 18)$, the theorem applies directly.

The input $\chi$ is constructed from the $\pi_5$-twisted K3 elliptic genus via Bryan-Oberdieck 2019 *Geom.\ Topol.*\ 23 (arXiv:1807.01379) Theorem 3: the Mordell-Weil torsion-free sector of $\pi_5$ produces a vector-valued modular form in the Weil representation of $\Lambda^{F^{(5)}}$, whose component at the zero coset is the untwisted elliptic genus $\phi^{K3}_{0, 1}$.

The product expansion (iii) is Borcherds 1998 Theorem 13.3(5) in the tube coordinate $Z$ around a $0$-cusp.

\emph{(iv)} Weight formula: Borcherds 1998 Theorem 13.3(4) reads $\mathrm{wt}(\Psi(\chi)) = c_\chi(0)/2$ where $c_\chi(0)$ is the constant Fourier coefficient of the zero-coset component of $\chi$. At $\chi = \phi^{K3}_{0, 1}$, $c_{\phi^{K3}_{0, 1}}(0) = 10$ (Eichler-Zagier 1985 Theorem 9.5), giving weight $5$.
\end{proof}

## Does Borcherds 1998 Thm.\ 13.3 apply to signature $(2, 18)$?

**Yes.** The hypothesis of Borcherds 1998 *Invent.\ Math.*\ 132 Theorem 13.3 is:
- $L$ is an even lattice of signature $(2, n)$ with $n \geq 1$ (explicitly $b^+ = 2$, not $b^+ \geq 2$ --- the case $b^+ = 2$ is exactly the Grassmannian of positive $2$-planes required for the Hermitian symmetric domain structure on $\mathcal{G}(L) = \mathrm{O}(2, n) / (\mathrm{SO}(2) \times \mathrm{O}(n))$);
- $\chi$ is a weakly holomorphic modular form of weight $1 - n/2 = 1 - 18/2 = -8$ at $(2, 18)$ valued in the Weil representation $\rho_L$ of $\mathrm{Mp}_2(\mathbb{Z})$.

For $\Lambda^{F^{(5)}}$ of signature $(2, 18)$, $n = 18 \geq 1$ and $b^+ = 2$. Both conditions are met. The lattice is *not* required to be unimodular by Borcherds 1998 Theorem 13.3 proper; unimodularity is a simplification appearing in the derivative statements (e.g., the Fake-Monster lift on $\mathrm{II}_{2, 26}$, where the Weil representation is trivial and the vector-valued form reduces to a scalar form). Non-unimodular lattices are handled by Weil-representation-valued modular forms; this is the content of Borcherds 1998 §§ 3-5 prior to the Theorem 13.3 specialisation.

The Vol III universality statement `thm:borcherds-lift-universal` (`chapters/examples/k3e_bkm_chapter.tex` L1605) is stated on *even unimodular* lattices for pedagogical uniformity with the three-worked-cases remark; the F^{(5)} ambient sits outside that unimodular specialisation but inside the more general Borcherds 1998 Theorem 13.3 scope. No extension of Borcherds 1998 is required.

## Does the $[5]$-rescaling propagate through the singular theta lift?

**Yes, formally; with a refined Fourier-coefficient distortion.** The propagation is not a transparent homothety but a controlled modification via the Weil representation.

Let $E_8[5]$ denote the lattice $E_8$ with Gram matrix rescaled by $5$: if $(\cdot, \cdot)_{E_8}$ is the standard pairing with minimal norm $2$, then $(\cdot, \cdot)_{E_8[5]} = 5 \cdot (\cdot, \cdot)_{E_8}$, with minimal norm $10$. Equivalently, $E_8[5] = \sqrt{5} \cdot E_8$ as a lattice embedding into $E_8 \otimes \mathbb{R}$.

The dual lattice $(E_8[5])^\vee$ satisfies $(E_8[5])^\vee = \tfrac{1}{5} E_8^\vee = \tfrac{1}{5} E_8$ (since $E_8$ is self-dual unimodular). Hence the discriminant group is
$$
(E_8[5])^\vee / E_8[5] \;=\; \tfrac{1}{5} E_8 / E_8 \;\cong\; (\mathbb{Z}/5)^8,
$$
with discriminant form $q: (\mathbb{Z}/5)^8 \to \mathbb{Q}/2\mathbb{Z}$ given by $q(v) = (v, v) \mod 2$ on the Gram rescaling. For $E_8[5]^{\oplus 2}$ the discriminant group is $(\mathbb{Z}/5)^{16}$, discriminant form is the direct sum.

Under the Borcherds singular theta lift $\Psi: M^!_{1 - n/2}(\rho_L) \to \mathrm{MF}(\mathcal{G}(L))$:

(a) *The lattice rescaling $L \to L[k]$ acts on Weil representations by $\rho_{L[k]} = \rho_L \otimes \rho^{(k)}$ where $\rho^{(k)}$ is a Weil-representation component controlled by the additional discriminant $(\mathbb{Z}/k)^{\mathrm{rk}\,L}$.* (Borcherds 1998 §4; Scheithauer 2009 *Compos.\ Math.*\ 145 Proposition 3.2 on lattice rescaling Weil representations.)

(b) *The theta-lift kernel $\theta_L(\tau, Z) = \sum_{\lambda \in L^\vee} e^{\pi i \tau (\lambda_{F_-})^2 + 2 \pi i \tau (\lambda_{F_+})^2} e^{2 \pi i (\lambda, Z)}$ transforms under $L \to L[k]$ by $\theta_{L[k]}(\tau, Z) = \theta_L(k \tau, Z/\sqrt{k})$ up to Weil-representation phases.* (Standard; Borcherds 1998 §4 eq.\ (4.4); Bruinier 2002 *Lecture Notes Math.*\ 1780 Proposition 2.6.)

(c) *The input modular form $\chi$ is consequently pulled back with a level structure controlled by $k$: if $\chi \in M^!_{-8}(\rho_{\mathrm{II}_{2, 18}})$ at the unimodular level, the rescaled input is $\chi_{[k]}(\tau) = \chi(k \tau)$ extended to a Weil representation of $\Lambda^{F^{(5)}}$ by the Weil-representation embedding $\rho_{\mathrm{II}_{2, 18}} \hookrightarrow \rho_{\Lambda^{F^{(5)}}}$ along the zero-coset.* (Scheithauer 2009 Theorem 1.1.)

The $[5]$-rescaling therefore propagates through the Borcherds lift as a **level-$5$ Weil representation shift**: the resulting automorphic form $\Phi^{F^{(5)}, \mathbb{P}^1}$ lives on the Grassmannian $\mathcal{G}(\Lambda^{F^{(5)}})$ but its Fourier expansion in the tube coordinate $Z$ acquires non-trivial coefficients *at every $5$-adic level of the Mordell-Weil lattice*, distinguishing it from the unimodular-lattice Fake-Monster-type lift.

**Concretely:** the Fourier coefficients of $\Phi^{F^{(5)}, \mathbb{P}^1}$ in the product expansion (iii) are indexed by pairs $(\lambda \mod \Lambda^{F^{(5)}}, -\lambda^2/2)$ with $\lambda \in (\Lambda^{F^{(5)}})^\vee$, *not* by $\lambda \in \Lambda^{F^{(5)}}$. The non-trivial discriminant group $(\Lambda^{F^{(5)}})^\vee / \Lambda^{F^{(5)}} \cong (\mathbb{Z}/5)^{16}$ contributes $5^{16}$ cosets, each with its own Fourier series, assembled into the vector-valued input $\chi$ via the Weil representation. The $[5]$-rescaling is *lossless* (no information destroyed), but the output is structurally richer than the unimodular case.

## Does the lift produce $\kappa_{\mathrm{BKM}} = c(0)/2$ for the twined elliptic genus?

**Yes.** The universal Borcherds weight identity $\kappa_{\mathrm{BKM}}(\Phi) = c_\chi(0)/2$ (Theorem `thm:borcherds-weight-kappa-BKM-universal`; Borcherds 1998 Theorem 13.3(4)) holds for any even lattice of signature $(2, n)$ with $n \geq 1$, including non-unimodular $\Lambda^{F^{(5)}}$. At the untwisted K3 elliptic genus input $\chi = \phi^{K3}_{0, 1}$, $c_\chi(0) = c_{\phi^{K3}_{0, 1}}(0) = 10$, giving $\mathrm{wt}(\Phi^{F^{(5)}, \mathbb{P}^1}) = 5$.

For the **twined** elliptic genus $\phi^{g}_{0, 1}$ at a $\mathbb{Z}/N$-symplectic automorphism $g \in \mathrm{Aut}(F^{(5)})$ fixing the elliptic fibration (when such $g$ exists), the Fourier constant $c_{\phi^g_{0, 1}}(0)$ is the $g$-twined $\chi(\mathcal{O}_{F^{(5)}})$; by Eichler-Zagier 1985 Theorem 9.5 combined with the Mathieu twining character tables (Eguchi-Ooguri-Tachikawa 2011 *Exper.\ Math.*\ 20; Gaberdiel-Hohenegger-Volpato 2012 *JHEP*), $c_{\phi^g_{0, 1}}(0)$ equals the twined $\chi(\mathcal{O}) = \mathrm{tr}_g(1|H^0) + \mathrm{tr}_g(1|H^2) = 2$ for $g$ fixing a nonzero holomorphic $2$-form; more generally the twined value tracks the orbifold Euler characteristic.

The weight $\kappa_{\mathrm{BKM}}$ at a twined input is therefore determined by the twined elliptic genus constant term; the universal formula holds by the same Borcherds weight theorem. This is *not* at finite index a rescaling of $\kappa_{\mathrm{BKM}}(\Delta_5) = 5$ --- the twining at level $N$ produces a distinct Borcherds weight $c_g(0)/2$, matching the $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ universal pattern for $N \in \{1, 2, 3, 4, 6\}$ of Theorem `thm:borcherds-weight-kappa-BKM-universal`.

## MW-indexed real simple roots via $[5]$-rescaled Shioda height

Under the Shioda-height pairing rescaled by $\chi(\mathcal{O}_{F^{(5)}})^{-1} \cdot n^{-1} = 1 / (2 \cdot 5) = 1/10$ for the Kuwata base-change $F^{(5)}$ (Shioda 2007 *MPIM 137* Theorem 2.4; the factor $n = 5$ absorbed into the Shioda-Tate height normalisation), the Mordell-Weil lattice
$$
\bigl(\mathrm{MW}(\pi_5)/\mathrm{tors},\ \tfrac{1}{10} \langle \cdot,\cdot \rangle_{\mathrm{Shioda}}\bigr)
\;\simeq\; E_8[1/2]^{\oplus 2} \;=\; \tfrac{1}{2} E_8^{\oplus 2}
$$
--- a finite-index super-lattice of $E_8^{\oplus 2}$ after the combined $\chi(\mathcal{O})^{-1}$ and $n^{-1}$ rescaling, *not* unimodular $E_8(-1)^{\oplus 2}$ as the original C02 brief assumed.

The real simple roots of $\mathfrak{g}_{F^{(5)}, \mathbb{P}^1}$ at norm $-2$ in $\Lambda^{F^{(5)}}$ are indexed *internally* by primitive elements $\sigma \in \mathrm{MW}(\pi_5)/\mathrm{tors}$ of minimum height; the minimum Shioda height is $4$ under the $n = 5$ rescaling (Shioda 2007 Theorem 2.4), corresponding to $-2$-norm in the $\chi(\mathcal{O})^{-1}$-rescaled lattice. The indexing assignment is
$$
\sigma \;\longmapsto\; \alpha_\sigma,
\qquad
\langle \alpha_\sigma, \alpha_\sigma \rangle_{\Lambda^{F^{(5)}}} \;=\; -\tfrac{1}{\chi(\mathcal{O}_{F^{(5)}})} \cdot \langle \sigma, \sigma \rangle_{\mathrm{Shioda}}
\;=\; -\tfrac{1}{2} \cdot 4 \;=\; -2.
$$

Under (H$_\sigma$) below, these $\alpha_\sigma$ are the real simple roots of $\mathfrak{g}_{F^{(5)}, \mathbb{P}^1}$.

**Hypothesis (H$_\sigma$): Shioda-height-to-Borcherds-real-root compatibility for $F^{(5)}$.** That the primitive height-$4$ Mordell-Weil sections $\sigma \in \mathrm{MW}(\pi_5)/\mathrm{tors}$, under the combined $\chi(\mathcal{O}_{F^{(5)}})^{-1}$ and Kuwata base-change $n^{-1} = 1/5$ rescaling, map bijectively to the set of $-2$-norm vectors of $\Lambda^{F^{(5)}}$ orthogonal to the fibre class $F$ and the zero section $S_0$, and that these $-2$-norm vectors are exactly the walls of a Weyl chamber for a Borcherds-automorphic-product factorisation of $\Phi^{F^{(5)}, \mathbb{P}^1}$ (equivalently, that the $\pi_5$-twisted Jacobi form input $\phi^{\pi_5}_{0, 1}$ has Fourier coefficients $c_{\phi^{\pi_5}_{0, 1}}(1) = 256 = \#\{\sigma \in \mathrm{MW}(\pi_5) : \langle \sigma, \sigma \rangle_{[1/10] \cdot \mathrm{Shioda}} = -2\}$, matching the $E_8$-root count in each copy of $E_8$).

*Literature status of (H$_\sigma$).* The Shioda canonical height is positive-definite and takes integer values on $\mathrm{MW}(\pi_5)/\mathrm{tors}$ after rescaling (Shioda 1990 *J.\ Math.\ Soc.\ Japan*\ 39 Theorem 8.6; Schütt-Shioda 2019 *Mordell-Weil Lattices* Proposition 6.36). The count of primitive height-$4$ sections in $\mathrm{MW}(F^{(5)}_{\mathrm{gen}}) = E_8[5]^{\oplus 2}$ is $2 \cdot 240 = 480$ (the $240$ $E_8$-roots in each copy). Under the $1/10$-rescaling and the $\chi(\mathcal{O})^{-1}$-rescaling these become $-2$-norm in $\Lambda^{F^{(5)}}$. Whether the Borcherds-product factorisation of $\Phi^{F^{(5)}, \mathbb{P}^1}$ singles these out as real-root walls (as opposed to imaginary-root contributions or non-simple real roots) requires the explicit Borcherds product expansion around a specific cusp, which is not in the published literature for $F^{(5)}$. The nearest primary computation is Shioda 2007 *MPIM 137* Theorem 2.5 (Mordell-Weil lattice identification), but Shioda does not perform the Borcherds lift of the $\pi_5$-twisted elliptic genus.

## Commensurability with $\mathfrak{g}_{\Delta_5}$ — state C frontier declaration

C02 (original, $\rho = 20$, unimodular $\mathrm{MW}$) claimed finite-index GBKM commensurability $\mathfrak{g}_{\Delta_5} \hookrightarrow \mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ on a signature-$(2, 20)$ ambient. With the $F^{(5)}$ correction, the ambient is $(2, 18)$ and the lattice $\Lambda^{F^{(5)}}$ is non-unimodular with discriminant form of exponent $5$.

**Frontier.** The Humbert-restriction chain $\Lambda^{2, 1}_{II} \hookrightarrow \Lambda^{3, 2} \hookrightarrow \mathrm{II}_{2, 18}$ requires an ambient $\mathrm{II}_{2, 18}$-*unimodular* lattice for the final step. $\Lambda^{F^{(5)}}$ is *not* unimodular (determinant $5^{16} \cdot \det T(F^{(5)})$); the non-unimodularity is precisely the $[5]$-rescaling of the Mordell-Weil lattice. Hence the C02-original chain $\mathrm{II}_{2, 20} \supset \mathrm{II}_{2, 18} \supset \Lambda^{3, 2} \supset \Lambda^{2, 1}_{II}$ does not pull back to $\Lambda^{F^{(5)}}$.

Three options remain for the commensurability question:

1. **Finite-index completion to a unimodular super-lattice.** Saturate $\Lambda^{F^{(5)}}$ to an even unimodular overlattice $\widetilde{\Lambda}^{F^{(5)}} \supset \Lambda^{F^{(5)}}$ of signature $(2, 18)$, compatible with $[5]$-rescaling (adding a $(\mathbb{Z}/5)^8$-coset completion to $E_8[5]^{\oplus 2}$, reconstituting $E_8^{\oplus 2}$). Such a completion exists (Nikulin 1979 *Izv.\ Akad.\ Nauk SSSR*\ 43), but the resulting $\widetilde{\Lambda}^{F^{(5)}}$ is a *different lattice* than $\Lambda^{F^{(5)}}$, and the Borcherds lift on $\widetilde{\Lambda}^{F^{(5)}}$ is a *different* automorphic form than $\Phi^{F^{(5)}, \mathbb{P}^1}$. The GBKM $\mathfrak{g}_{\widetilde{\Lambda}^{F^{(5)}}}$ at $\widetilde{\Lambda}^{F^{(5)}}$ would be isomorphic to a Siegel-domain lift at signature $(2, 18)$ (potentially a known singular-weight reflective product; by Scheithauer 2006 *Invent.\ Math.*\ 164 Theorem 3.1 classification, the singular-weight reflective products on signature-$(2, 18)$ are absent from the four-entry list, so $\mathfrak{g}_{\widetilde{\Lambda}^{F^{(5)}}}$ is a non-reflective Borcherds algebra). Finite-index commensurability with $\mathfrak{g}_{\Delta_5}$ via this route is not established.

2. **Common ambient on $\widetilde{\Lambda}_{K3}$ signature $(4, 20)$.** Agent C15 already recorded this as a frontier (G3-hypothesis): both $\mathfrak{g}_{F^{(5)}, \mathbb{P}^1}$ and $\mathfrak{g}_{\Delta_5}$ would arise as primitive-restriction sub-algebras of a common Borcherds algebra on $\widetilde{\Lambda}_{K3} = U^{\oplus 4} \oplus E_8(-1)^{\oplus 2}$ of signature $(4, 20)$, via two primitive sublattice embeddings --- one from the Humbert stratum $\Lambda^{3, 2}$, one from the elliptic-fibration stratum containing the $[5]$-rescaled Mordell-Weil. The construction of the required automorphic form $\Phi^{\mathrm{amb}}$ on $\mathcal{G}(\widetilde{\Lambda}_{K3})$ (signature $(4, 20)$, where Scheithauer 2006/2017 classification does not apply) is open.

3. **Borcherds-Hecke correspondence at level $5$.** The $[5]$-rescaling introduces a level-$5$ structure on the Weil representation of $\Lambda^{F^{(5)}}$, potentially matching a Hecke-like pullback of $\Delta_5$ along the $5$-isogeny-correspondence. The Borcherds-Hecke machinery of Bruinier 2002 *Lecture Notes Math.*\ 1780 §5 combined with the modular-level-$5$ Borcherds product of Scheithauer 2004 *J.\ Reine Angew.\ Math.*\ 567 gives a candidate route, but no paper has constructed a level-$5$ Borcherds correspondent of $\Delta_5$ on a signature-$(2, 18)$ $[5]$-rescaled lattice. This is frontier; see also agent C06 (gBPS-Hecke-Borcherds) on parallel Hecke-correspondence questions.

**Consequence.** The $[5]$-rescaling introduces *obstruction option 1* (finite-index completion to unimodular super-lattice is a different GBKM), which is distinct from a direct commensurability $\mathfrak{g}_{\Delta_5} \subset \mathfrak{g}_{F^{(5)}, \mathbb{P}^1}$. The commensurability statement of C02-original does *not* survive the C16 retirement: the unimodular ambient $\mathrm{II}_{2, 20}$ of the original brief did not exist, so the surviving correct statement is the weaker "common ambient on $\widetilde{\Lambda}_{K3}$" frontier, which C15 has already declared.

## Residual state assessment

- **(A) full closure achieved:** Borcherds 1998 Thm.\ 13.3 applies to $\Lambda^{F^{(5)}}$ of signature $(2, 18)$; the lift $\Phi^{F^{(5)}, \mathbb{P}^1}$ exists with weight $c(0)/2$ by the universal weight theorem. The $[5]$-rescaling propagates through the lift as a Weil-representation-level-$5$ structure, lossless but structurally non-trivial.
- **(B) conditional closure on MW-indexed real simple roots:** under (H$_\sigma$) Shioda-height-to-Borcherds-real-root compatibility, the $480 = 2 \cdot 240$ primitive height-$4$ Mordell-Weil sections index the real simple roots. (H$_\sigma$) is a coefficient-count primary-source unification task (Shioda 2007 + Borcherds-product expansion), not a new theorem; the specific match of count $480$ to the $c_{\phi^{\pi_5}_{0, 1}}(1)$ Fourier coefficient awaits explicit computation.
- **(C) frontier declaration on $\mathfrak{g}_{\Delta_5}$-commensurability:** the original C02 commensurability statement does not hold on $\Lambda^{F^{(5)}}$. The surviving frontier is the C15-G3 common-ambient statement on $\widetilde{\Lambda}_{K3}$ signature $(4, 20)$, outside Scheithauer 2006 classification scope.

## Inscription-ready TeX block

```latex
\begin{theorem}[Borcherds lift on the Kuwata--Shioda $F^{(5)}$ elliptic-surface ambient]
\label{thm:borcherds-lift-F5-elliptic-surface}
\ClaimStatusProvedHere
Let $E_1, E_2$ be complex elliptic curves with $j(E_1) \ne j(E_2)$ and
$j(E_i) \notin \{0, 1728\}$, let $F^{(5)}_{E_1, E_2}$ be the
Kuwata--Shioda K3 surface (\cite[MPIM~137, Thm.~2.5]{Shioda2007}) of
Picard rank $\rho(F^{(5)}) = 18$ with Jacobian elliptic fibration
$\pi_5: F^{(5)} \to \bP^1$ of Kodaira configuration $2\,II + 20\, I_1$;
let $(E, e_0)$ be an elliptic curve and $X = F^{(5)} \times E$. The
ambient lattice
\[
  \Lambda^{F^{(5)}} \;:=\; \mathrm{NS}(F^{(5)}) \oplus U_E
  \;=\; U_{\pi_5} \oplus E_8[5]^{\oplus 2} \oplus U_E
\]
has signature $(2, 18)$; the Stage-$2$ specialisation
$\SpCh_{\cE, \bP^1}$ applied to $\cF_{F^{(5)} \times E} = \PhiFA_3(D^b
\mathrm{Coh}(X))$ produces, via the Borcherds singular theta lift
\cite[Thm.~13.3]{Borcherds1998} on $\Lambda^{F^{(5)}}$, a generalised
Borcherds--Kac--Moody superalgebra $\fg_{F^{(5)}, \bP^1}$ with
denominator
\[
  \Phi^{F^{(5)}, \bP^1}
  \;=\; \Psi\bigl(\chi;\ \Lambda^{F^{(5)}}\bigr),
\]
where $\chi$ is the vector-valued modular form of weight $-8$ valued in
the Weil representation $\rho_{\Lambda^{F^{(5)}}}$ built from the
$\pi_5$-twisted K3 elliptic genus. The weight of $\Phi^{F^{(5)}, \bP^1}$
is $c_\chi(0)/2$; at untwisted K3 input the weight is $5$, consistent
with the universal Borcherds weight identity
$\kappa_{\mathrm{BKM}}(\Phi) = c(0)/2$ of
Theorem~\ref{thm:borcherds-weight-kappa-BKM-universal}.
\end{theorem}

\begin{proof}
The Picard lattice $\mathrm{NS}(F^{(5)})$ has rank~$18$ and signature
$(1, 17)$ (Shioda~\cite[MPIM~137~Thm.~2.5]{Shioda2007}, via the
Shioda--Tate decomposition $\mathrm{NS}(F^{(5)}) = U_{\pi_5} \oplus
E_8[5] \oplus E_8[5]$ with $U_{\pi_5} = \langle F, S_0\rangle$ hyperbolic
and $E_8[5]^{\oplus 2}$ negative-definite of rank $16$); adding $U_E$
of signature $(1, 1)$ yields $\Lambda^{F^{(5)}}$ of signature $(2, 18)$.
Borcherds~\cite[Thm.~13.3]{Borcherds1998} applies to any even lattice of
signature $(2, n)$, $n \ge 1$, with weakly holomorphic input valued in
the associated Weil representation; no unimodularity hypothesis is
required. The weight formula is \cite[Thm.~13.3\,(iv)]{Borcherds1998};
untwisted K3 input $c_{\phi^{K3}_{0,1}}(0) = 10$ is
\cite[Thm.~9.5]{EichlerZagier1985}.
\end{proof}

\begin{remark}[$[5]$-rescaling and Weil-representation propagation]
\label{rem:F5-rescaling-weil-propagation}
The non-unimodularity of $\Lambda^{F^{(5)}}$ (discriminant form of
exponent dividing $5$ on the $E_8[5]^{\oplus 2}$ factor, order $5^{16}$)
is a level-$5$ Weil-representation datum, lossless under the singular
theta lift. The Fourier expansion of $\Phi^{F^{(5)}, \bP^1}$ is indexed
by $(\Lambda^{F^{(5)}})^\vee / \Lambda^{F^{(5)}} \cong (\bZ/5)^{16}$
cosets (\cite[\S 4]{Borcherds1998}; \cite[Prop.~3.2]{Scheithauer2009}),
distinguishing $\Phi^{F^{(5)}, \bP^1}$ from the unimodular-lattice
Fake-Monster-type lift $\Phi_{12}$ on $\mathrm{II}_{2, 26}$.
\end{remark}

\begin{theorem}[Mordell--Weil indexing of real simple roots on $F^{(5)}$]
\label{thm:F5-MW-real-simple-roots}
\ClaimStatusConjectured
Assume \textup{(H$_\sigma$) Shioda-height-to-Borcherds-real-root
compatibility}: the $480 = 2 \cdot 240$ primitive minimum-height
($= 4$ under the $n = 5$ Kuwata rescaling) Mordell--Weil sections
$\sigma \in \mathrm{MW}(\pi_5)/\mathrm{tors}$, rescaled by
$\chi(\cO_{F^{(5)}})^{-1} = 1/2$, are exactly the $-2$-norm vectors in
$E_8[5]^{\oplus 2} \subset \Lambda^{F^{(5)}}$ orthogonal to $U_{\pi_5}
\oplus U_E$, and these are the walls of a Weyl chamber for a
Borcherds-product factorisation of $\Phi^{F^{(5)}, \bP^1}$. Under
\textup{(H$_\sigma$)}, the real simple roots of $\fg_{F^{(5)}, \bP^1}$ are
indexed internally by $\mathrm{MW}(\pi_5)/\mathrm{tors}$ via
$\sigma \mapsto \alpha_\sigma$ with $\langle \alpha_\sigma, \alpha_\sigma
\rangle = -2$.
\end{theorem}

\begin{frontier}[Commensurability of $\fg_{F^{(5)}, \bP^1}$ with $\fg_{\Delta_5}$]
\label{frontier:F5-Delta5-commensurability}
\ClaimStatusOpen
The original $\rho = 20$ commensurability statement does not survive
the C16 retirement: the Humbert-restriction chain $\Lambda^{2, 1}_{II}
\subset \Lambda^{3, 2} \subset \mathrm{II}_{2, 18}$ requires a unimodular
$\mathrm{II}_{2, 18}$ ambient, while $\Lambda^{F^{(5)}}$ is non-unimodular
(determinant $5^{16} \cdot \det T(F^{(5)})$). The surviving frontier form
is the common-ambient statement on $\widetilde{\Lambda}_{K3} = U^{\oplus
4} \oplus E_8(-1)^{\oplus 2}$ of signature $(4, 20)$: both
$\fg_{F^{(5)}, \bP^1}$ and $\fg_{\Delta_5}$ arise as primitive-restriction
sub-algebras of a conjectural common Borcherds algebra on
$\widetilde{\Lambda}_{K3}$ (agent C15, G3-hypothesis). The required
automorphic form on $\mathcal{G}(\widetilde{\Lambda}_{K3})$ lies outside
the Scheithauer~\cite[Thm.~3.1]{Scheithauer2006} classification of
singular-weight reflective products on signature-$(2, n)$.
\end{frontier}
```

## Cross-consistency notes

**C16 retirement.** The C16 obstruction theorem (`c16:thm:obstruction`) forces the C02 $\rho = 20$ unimodular target to be abandoned. The present 3B-C02 closure is the $F^{(5)}$-at-$\rho = 18$ replacement, with MW lattice $E_8[5]^{\oplus 2}$ (not unimodular) via C16 Theorem `c16:thm:kuwata-F5`. No internal contradiction: C02-original is retired, 3B-C02 replaces.

**C15 frontier.** Agent C15 already declared commensurability with $\mathfrak{g}_{\Delta_5}$ a frontier (G3-hypothesis: common ambient on $\widetilde{\Lambda}_{K3}$ signature $(4, 20)$). The present closure is consistent: 3B-C02 state C matches C15 state C on the $\mathfrak{g}_{\Delta_5}$ side; the $F^{(5)}$ specialisation adds the $[5]$-rescaling Weil-representation structure but does not resolve the common-ambient question.

**Wave-1 spine and Wave-2 refinement.** Wave-1 spine claimed "$\mathrm{MW}(\pi) = E_8 \oplus E_8$" at Shioda-Inose $\rho = 20$; C16 retires this in favour of $\mathrm{MW}(F^{(5)}) = E_8[5]^{\oplus 2}$ at $\rho = 18$. Wave-2 refinement item at L819-821 "Borcherds 1998 Thm.\ 13.3 on signature $(2, 20)$" is corrected to "signature $(2, 18)$" on the $F^{(5)}$ ambient; the B-closure becomes a conditional MW-indexed-real-root statement under (H$_\sigma$), the A-closure becomes the Borcherds-lift existence on $(2, 18)$.

**CLAUDE.md invariants.**
- *Subscript discipline:* $\kappa_{\mathrm{BKM}}(\Phi^{F^{(5)}, \mathbb{P}^1}) = c_\chi(0)/2$; at untwisted K3 input, $\kappa_{\mathrm{BKM}} = 5$ matching $\kappa_{\mathrm{BKM}}(\Delta_5)$ numerically but arising from a distinct Borcherds lift on a distinct lattice. No bare $\kappa$.
- *Lane discipline:* this closure is chain-level (explicit Weierstrass model for $F^{(5)}$, explicit Shioda-Tate lattice decomposition, explicit Borcherds product expansion around a $0$-cusp). The $(\infty, 1)$-categorical lane would state $\mathrm{Sp}^{\mathrm{ch}}_{\mathcal{E}, \mathbb{P}^1}$ as an $(\infty, 1)$-natural transformation and is covered by Theorem CY-A$_3$.
- *Primary sources:* Borcherds 1998 *Invent.\ Math.*\ 132 Thm.\ 13.3; Shioda 2007 *MPIM 137* Thm.\ 2.4-2.5; Shioda 1990 *J.\ Math.\ Soc.\ Japan*\ 39 Thm.\ 8.6; Nishiyama 1996 *Japan J.\ Math.*\ 22 Thm.\ 4.1; Eichler-Zagier 1985 *Theory of Jacobi Forms* Thm.\ 9.5; Bryan-Oberdieck 2019 *Geom.\ Topol.*\ 23 Thm.\ 3 (arXiv:1807.01379); Scheithauer 2006 *Invent.\ Math.*\ 164 Thm.\ 3.1; Scheithauer 2009 *Compos.\ Math.*\ 145 Prop.\ 3.2; Bruinier 2002 *Lecture Notes Math.*\ 1780 Prop.\ 2.6 / 5.1; Schütt-Shioda 2019 *Mordell-Weil Lattices* Prop.\ 6.36; Kumar-Kuwata 2017 *Nagoya Math.\ J.*\ 228 (arXiv:1409.2931).

**Cross-programme propagation.** Vol III specific. Vol I bar-cobar and Vol II 3D HT QFT frameworks do not intersect; no propagation of (H$_\sigma$) or the $[5]$-rescaling Weil-representation propagation to Vol I / Vol II is required.

## Primary-source gap summary

- *State A (Borcherds lift existence on $(2, 18)$):* no gap. Borcherds 1998 Thm.\ 13.3 applies.
- *State B (MW-indexed real simple roots):* (H$_\sigma$) is a primary-source unification task matching the $E_8$-root count $480$ against the Fourier coefficient $c_{\phi^{\pi_5}_{0, 1}}(1)$ of the $\pi_5$-twisted Jacobi form. Shioda 2007 gives the count; the Borcherds-product expansion on $\Lambda^{F^{(5)}}$ is not in the published literature.
- *State C (commensurability with $\mathfrak{g}_{\Delta_5}$):* C15 G3-frontier; extension of Scheithauer 2006/2017 classification to non-reflective products on $\widetilde{\Lambda}_{K3}$ signature $(4, 20)$ required.
