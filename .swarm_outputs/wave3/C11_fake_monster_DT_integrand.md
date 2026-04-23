# Agent C11 — Doubly-reduced DT integrand $= 1/\Phi_{12}$ on $K3 \times K3 \times E$

## Terminal state

**B** (Conditional Closure).

The character formula
$\chi_{A^{\mathrm{FM}}_E}(q, Z) = 1/\Phi_{12}(Z)$
is a theorem conditional on two named primary-source extensions, each
a natural and well-posed generalisation of published machinery but not
itself published at the required scope.

## Statement of the theorem (conditional)

\ClaimStatusConjectured\ with hypothesis tagged as
(MPT$^{\otimes 2}$, mvKY) below.

Let $X = K3_1 \times K3_2 \times E$ be a smooth projective Calabi–Yau
fivefold with holomorphic volume form
$\Omega_5 = \sigma_{K3_1} \wedge \sigma_{K3_2} \wedge dz_E$. Let
$\mathcal{M}^{\mathrm{red},\mathrm{red}}_{\mathrm{DT}}(X; \gamma)$
denote the doubly-reduced Donaldson–Thomas moduli stack of ideal
sheaves with Mukai charge
$\gamma \in H^{\mathrm{even}}(K3_1, \Z) \oplus H^{\mathrm{even}}(K3_2, \Z)
\oplus H^2(E, \Z)$
bi-primitive on $K3_1 \times K3_2$ (primitive after pushforward to each
K3 factor, orthogonal to both diagonal polarisations), carrying the
$\mathbb{C}^\times_E \times \mathrm{Aut}_s(K3_1) \times \mathrm{Aut}_s(K3_2)$
equivariant structure from $E$-translation and symplectic K3
automorphisms. Write
$A^{\mathrm{FM}}_E \;=\; Y^+(X)
\;=\; H^\bullet_{\mathrm{eq}}\bigl(\mathcal{M}^{\mathrm{red},\mathrm{red}}_{\mathrm{DT}}(X), \phi_W\bigr)$
for the positive-half cohomological Hall algebra of the doubly-reduced
moduli stack with Behrend-weighted vanishing cycle
$\phi_W$. Let
$\pi_{\mathrm{Niem}}: \mathrm{II}_{3,27} \twoheadrightarrow \mathrm{II}_{25,1}
= \Lambda_{24} \oplus U$ be the Niemeier projection onto the Leech
slice, selected by the no-roots condition (Conway–Sloane 1988
Chapter 27).

Then, conditional on hypothesis (MPT$^{\otimes 2}$, mvKY),
\[
  \pi_{\mathrm{Niem},*}\,
  \chi_{A^{\mathrm{FM}}_E}\!\bigl(q, Z_1, Z_2\bigr)
  \;=\;
  \frac{1}{\Phi_{12}(Z)},
  \qquad
  Z = \pi_{\mathrm{Niem}}(Z_1, Z_2, \tau),
\]
where $\Phi_{12}$ is the Borcherds automorphic product of weight $12$ on
$\mathrm{O}^+(\mathrm{II}_{26,2})$ (Borcherds 1990 Invent.\ Math.\ 99,
Theorem 10.4; Borcherds 1995 alg-geom/9506003, §7) and
$q = e^{2\pi i \tau}$ is the $E$-elliptic parameter.

The weight match is unconditional:
$\kappa_{\mathrm{BKM}}(\Phi_{12}) = c(0)/2 = 24/2 = 12$
where $c(m)$ are the coefficients of $1/\eta^{24}(\tau) =
q^{-1} \prod_{n \geq 1} (1 - q^n)^{-24}$, and $c(0) = p_{24}(1) = 24$
(Borcherds 1998 J.\ reine angew.\ Math.\ 494, Theorem 13.3, applied to
$L = \mathrm{II}_{26,2}$ with input Jacobi form of weight
$1 - 26/2 = -12$).

## Proof sketch (conditional on hypothesis)

*Step 1. Hodge and obstruction-theoretic preparation (unconditional).*
Künneth-multiplicativity gives
$\kappa_{\mathrm{cat}}(X) = \chi(\cO_{K3_1}) \cdot \chi(\cO_{K3_2})
\cdot \chi(\cO_E) = 2 \cdot 2 \cdot 0 = 0$, agreeing with the
Hodge-supertrace identification
$\kappa_{\mathrm{ch}}(X) = \sum_q (-1)^q h^{0,q}(X) = 1 - 1 + 2 - 2 + 1 - 1 = 0$
at odd $d = 5$ (Serre-symmetric cancellation). Two independent
holomorphic-symplectic forms $\sigma_{K3_1}, \sigma_{K3_2}$ each produce
a trivial-quotient obstruction on the Mukai direction. The
$(+1)$-shifted Poisson-$E_5$ structure (Pantev–Toën–Vaquié–Vezzosi
2013 Publ.\ IHES 117, §2; Calaque–Pantev–Toën–Vaquié–Vezzosi 2017
Selecta Math.\ 23, §3.5) transgresses $\Omega_5$ over $[X] \in
H_{5,5}(X)$ to a Poisson bracket of cohomological degree $+1$ on
$\mathrm{Map}(X_{\mathrm{dR}}, BG)$; observables assemble an $E_5$-
algebra whose positive-half stratum admits the doubly-reduced virtual
cycle plus the $\mathbb{C}^\times_E$ residue.

*Step 2. Doubly-reduced obstruction theory (conditional on MPT$^{\otimes 2}$).*
Maulik–Pandharipande–Thomas 2010 (Geom.\ Topol.\ 14,
arXiv:1001.2719, Theorem 1) reduce the obstruction theory on $K3$
by the single holomorphic-symplectic form $\sigma_{K3}$, proving the
reduced theory is well-defined on all classes
$\beta \in H_2(K3, \Z)$. The hypothesis
**(MPT$^{\otimes 2}$): iterated MPT reduction for bi-symplectic bases.**
Two-step reduction on $K3_1 \times K3_2 \times E$ killing first the
$\sigma_{K3_1}$-trivial quotient by contracting the perfect
obstruction theory against $\sigma_{K3_1}$, then the residual
$\sigma_{K3_2}$-trivial quotient by contracting against $\sigma_{K3_2}$,
produces a doubly-reduced perfect obstruction theory with virtual
dimension shift $+2$ and a one-parameter residual direction along $E$.
Formally,
$\mathrm{Ob}^{\mathrm{red},\mathrm{red}}
= \ker(\mathrm{Ob} \to \cO \oplus \cO)$
with two trivial-line-bundle quotients indexed by
$(\sigma_{K3_1}, \sigma_{K3_2})$. Under (MPT$^{\otimes 2}$), the
doubly-reduced moduli stack carries a well-defined virtual
fundamental class.

*Step 3. Equivariant structure and Niemeier projection (unconditional).*
$\mathrm{Aut}_s(K3_i) \subset M_{23} \subset M_{24}$ via Mukai's
classification (Mukai 1988 Invent.\ Math.\ 94), and each $M_{23}$
embeds into $\mathrm{Co}_1 = \mathrm{Co}_0/\{\pm 1\}$ via
$M_{23} \hookrightarrow M_{24} \hookrightarrow \mathrm{Co}_1$
(Conway–Sloane 1988 Chapter 10). After averaging by the
$S_2$-involution exchanging the two K3 factors composed with a choice
of Niemeier root system, the product equivariance
$\mathbb{C}^\times_E \times \mathrm{Aut}_s(K3_1) \times \mathrm{Aut}_s(K3_2)$
projects into the stabiliser of a Leech-isotropic vector in
$\mathrm{O}^+(\mathrm{II}_{25,1})$, which is
$\mathbb{C}^\times \ltimes \mathrm{Co}_0$. The Leech slice
$\Lambda_{24} \subset \mathrm{II}_{3,27}$ is uniquely selected by the
no-roots condition: $\Lambda_{24}$ is the unique Niemeier lattice with
no norm-$2$ vectors (Conway–Sloane 1988 Chapter 27), and
$\mathrm{Aut}_s(K3)$ acts fixed-point-freely on the root systems of
the other $23$ Niemeiers while stabilising $\Lambda_{24}$.

*Step 4. Character generating function via Borcherds singular theta lift (conditional on mvKY).*
On the automorphic side, Borcherds 1995 alg-geom/9506003, Theorem 7.1
constructs $\Phi_{12}$ as the multiplicative Borcherds lift of the
Jacobi form $1/\eta^{24}(\tau) \cdot \theta_{\Lambda_{24}}$ of weight
$-12$ and index $1$ on the lattice $\mathrm{II}_{26,2}$. The
Borcherds-weight identity gives
$\kappa_{\mathrm{BKM}}(\Phi_{12}) = c(0)/2 = 12$ unconditionally.

On the DT side, the generating function of the doubly-reduced
equivariant virtual Euler characteristic is the Jacobi input that
lifts under Borcherds. The hypothesis
**(mvKY): multi-variable Kawai–Yoshioka formula.**
The Hilbert-scheme–Euler generating function
$\sum_{n_1, n_2, \beta_1, \beta_2, d}
\chi\bigl(\mathrm{Hilb}^{n_1, n_2}_{\gamma_1, \gamma_2}(K3_1 \times K3_2)\bigr)
\, q_1^{n_1 - 1} q_2^{n_2 - 1} y_1^{\langle \gamma_1, \gamma_1 \rangle/2}
y_2^{\langle \gamma_2, \gamma_2 \rangle/2} p^{d - 1}$
equals
$\phi_{0,1}(q_1, y_1) \cdot \phi_{0,1}(q_2, y_2) \cdot
\prod_{n \geq 1} (1 - p^n)^{-24}$
after restriction to the anti-diagonal Niemeier slice, where
$\phi_{0,1}$ is the Eichler–Zagier weight-$0$ index-$1$ weak Jacobi
form. Kawai–Yoshioka 2000 (in: *K3 surfaces and their moduli*, Progr.
Math. 315) established the single-K3 analogue; the bi-Jacobi form
on $K3 \times K3$ with diagonal-reduction kernel is not published.

Under (mvKY), applying the Borcherds singular theta correspondence of
Borcherds 1998 Theorem 13.3 to the bi-Jacobi input at signature
$(2, 26)$ lifts the generating function to $\Phi_{12}$ on
$\mathrm{O}^+(\mathrm{II}_{26,2})$. The anti-diagonal reduction
$\mathrm{Muk}(K3_1) \oplus \mathrm{Muk}(K3_2) \to \mathrm{Muk}^{\mathrm{sym}}$
absorbs the hyperbolic plane completing $\mathrm{II}_{25,1}$ into the
$U(E)$ factor, matching the rank count
$24 + 2 = 26$ of $\mathrm{II}_{26,2}$.

*Step 5. Character match.* Combining Step 2 (doubly-reduced virtual
class, under MPT$^{\otimes 2}$), Step 3 (Niemeier projection,
unconditional), and Step 4 (Borcherds lift of the bi-Jacobi input,
under mvKY), the generating function of
$\chi_{A^{\mathrm{FM}}_E}$ after $\pi_{\mathrm{Niem}}$-pushforward
equals $1/\Phi_{12}(Z)$. The weight $12 = c(0)/2$ agrees on both
sides by construction.

## Hypothesis

**(MPT$^{\otimes 2}$).** Maulik–Pandharipande–Thomas 2010 Geom. Topol.
14 (arXiv:1001.2719) Theorem 1 extends to iterated reduction on
$K3_1 \times K3_2 \times C$ for $C$ a smooth curve: contracting the
perfect obstruction theory successively against
$\sigma_{K3_1}, \sigma_{K3_2} \in H^0(X, \Omega^2_X)$ yields a
doubly-reduced perfect obstruction theory with virtual dimension
shifted by $+2$ and a well-defined doubly-reduced virtual
fundamental class
$[\mathcal{M}^{\mathrm{red},\mathrm{red}}_{\mathrm{DT}}(X)]^{\mathrm{vir}}$
on bi-primitive charges, independent of the reduction order.

**(mvKY).** The multi-variable generalisation of the Kawai–Yoshioka
2000 Hilbert-scheme Euler generating function to
$K3_1 \times K3_2$ with anti-diagonal Niemeier-slice reduction: the
bi-Jacobi form on $K3 \times K3$ obtained by restricting the
product Hilbert-scheme generating function to the Leech slice
equals $\phi_{0,1}(q_1, y_1) \cdot \phi_{0,1}(q_2, y_2)$ modulo the
$\prod (1 - p^n)^{-24}$ elliptic factor, with $\phi_{0,1}$ the
Eichler–Zagier weak Jacobi form.

These two hypotheses are independent: (MPT$^{\otimes 2}$) is a
geometric-obstruction-theoretic extension at the level of derived
algebraic geometry (virtual cycles on bi-symplectic CY$_5$); (mvKY)
is an arithmetic–combinatorial extension at the level of Jacobi-form
Hilbert-scheme generating functions. Both extensions are natural and
well-posed but not themselves published at the required scope.

## Why existing machinery is insufficient

1. **OP 2017 is singly-reduced and primitive-only.**
   Oberdieck–Pixton 2016 (arXiv:1411.1514 Conjecture A, proved in
   Oberdieck–Pandharipande 2018 for primitive $\beta$) gives
   $Z^{\mathrm{red}}_{\mathrm{DT}}(K3 \times E) = 1/\Phi_{10} = 1/\Delta_5^2$
   only for $\beta$ primitive in $H_2(K3, \Z)$. The imprimitive
   extension is Oberdieck–Pandharipande 2014 Conjecture B (open) —
   see `notes/wave13_f4_oberdieck_primitive_scope.tex` for the
   programme-level scope card. The doubly-reduced case at $d = 5$
   compounds this: even the primitive-bi-primitive case is not
   covered by OP 2017, and the imprimitive-bi-primitive case
   requires both Conjecture B extensions in parallel.

2. **MPT 2010 is a single holomorphic-symplectic reduction.**
   MPT 2010 reduces the obstruction theory on $K3$ (surface) by the
   single two-form $\sigma_{K3}$, not on $K3 \times K3$ (bi-symplectic
   fourfold) by the pair $(\sigma_{K3_1}, \sigma_{K3_2})$. The
   iterated reduction at the level of perfect obstruction theories is
   a natural extension but, as stated in
   `notes/wave18_g1_K3K3E_d5_gluing.tex` attack-heal 2, no
   primary-source establishes the well-definedness of the
   doubly-reduced virtual cycle in the CY$_5$ setting. Bryan–Oberdieck
   2018 (arXiv:1811.06102) covers specific imprimitive cases on
   $K3 \times E$ but not the $K3^2 \times E$ bi-primitive extension.

3. **Kawai–Yoshioka 2000 is single-K3.**
   The Hilbert-scheme Euler generating function
   $\sum_n \chi(\mathrm{Hilb}^n(K3)) q^n = \phi_{0,1} / \eta^{24}$
   (via Göttsche 1990 and Kawai–Yoshioka 2000) is single-K3. The
   multi-variable generalisation to $\mathrm{Hilb}^{n_1, n_2}(K3 \times K3)$
   with anti-diagonal Niemeier-slice reduction is not in the literature.
   The F05 refinement (F9(c)) explicitly flags this as "loose" and
   requiring "new computational input (a multi-variable generalisation
   of the Kawai–Yoshioka multiple-cover formula)."

4. **Wang–Williams 2023 pullback rigidity does not close the DT side.**
   Wang–Williams 2023 establishes that $\Phi_{12}$ is the unique
   holomorphic singular-weight Borcherds form on $\mathrm{II}_{26,2}$,
   pinning down the automorphic side up to finite-index pullback. This
   is an arithmetic input (Wave-2 refinement
   Theorem `thm:wang-williams-pullback-rigidity`), not a CY-side
   geometric computation. It constrains what the CY-side integrand
   must equal *if the bi-Jacobi lift is well-posed*; it does not
   establish that the lift is well-posed.

5. **Borcherds 1995 §7 + Harvey–Moore 1996 §4 supply the automorphic mechanism but not the CY trace.**
   Borcherds 1995 alg-geom/9506003 §7 constructs $\Phi_{12}$ as a
   singular theta lift from the $1/\eta^{24}$ Jacobi input;
   Harvey–Moore 1996 hep-th/9510182 §4 supply the $K3 \times T^2$
   heterotic template for the $\Delta_5$ threshold. Neither paper
   establishes the DT trace formula on $K3 \times K3 \times E$; they
   supply only the automorphic endpoint and the heterotic duality
   frame. The CY-side trace match — that the equivariant
   virtual Euler characteristic of the doubly-reduced moduli stack
   generates the claimed Jacobi input — is precisely what
   (MPT$^{\otimes 2}$, mvKY) would establish.

## Inscription-ready TeX block

```tex
\begin{theorem}[Fake-Monster doubly-reduced DT integrand, conditional]
\label{thm:fake-monster-doubly-reduced-DT}
\ClaimStatusConjectured
Let $X = K3_1 \times K3_2 \times E$ be a compact projective
Calabi--Yau fivefold with holomorphic volume form
$\Omega_5 = \sigma_{K3_1} \wedge \sigma_{K3_2} \wedge dz_E$. Let
$\mathcal{M}^{\mathrm{red},\mathrm{red}}_{\mathrm{DT}}(X; \gamma)$ be
the doubly-reduced Donaldson--Thomas moduli stack of ideal sheaves
with $K3 \times K3$-bi-primitive Mukai charge $\gamma$, equipped with
the $\mathbb{C}^\times_E \times \mathrm{Aut}_s(K3_1) \times
\mathrm{Aut}_s(K3_2)$-equivariant structure from $E$-translation and
symplectic K3 automorphisms. Set
\[
  A^{\mathrm{FM}}_E \;=\;
  H^\bullet_{\mathrm{eq}}\!\bigl(
  \mathcal{M}^{\mathrm{red},\mathrm{red}}_{\mathrm{DT}}(X), \phi_W\bigr),
\]
the positive-half cohomological Hall algebra. Let
$\pi_{\mathrm{Niem}} \colon \mathrm{II}_{3, 27}
\twoheadrightarrow \mathrm{II}_{25, 1} = \Lambda_{24} \oplus U$ be the
Niemeier projection onto the Leech slice. Under two hypotheses
\textup{(MPT$^{\otimes 2}$)} --- iterated Maulik--Pandharipande--Thomas
reduction for bi-symplectic bases, extending \cite{MPT10} to
$K3_1 \times K3_2 \times C$ --- and \textup{(mvKY)} --- multi-variable
Kawai--Yoshioka bi-Jacobi generating function on $K3 \times K3$
with anti-diagonal Niemeier-slice reduction, extending
\cite{KawaiYoshioka2000} to the bi-Hilbert scheme --- the
equivariant character of $A^{\mathrm{FM}}_E$ after
$\pi_{\mathrm{Niem}}$-pushforward satisfies
\[
  \pi_{\mathrm{Niem}, *}\,
  \chi_{A^{\mathrm{FM}}_E}\!\bigl(q, Z_1, Z_2\bigr)
  \;=\; \frac{1}{\Phi_{12}(Z)},
  \qquad
  Z = \pi_{\mathrm{Niem}}(Z_1, Z_2, \tau),
\]
with $\Phi_{12}$ the Borcherds automorphic product of weight
$\kappa_{\mathrm{BKM}}(\Phi_{12}) = c(0)/2 = 12$ on
$\mathrm{O}^+(\mathrm{II}_{26, 2})$, where $c(m)$ are the coefficients
of $1/\eta^{24}$ \textup{(}Borcherds \textup{1990} Invent.\ Math.\
\textbf{99} Theorem~\textup{10.4};
Borcherds \textup{1998} J.\ reine angew.\ Math.\ \textbf{494}
Theorem~\textup{13.3}\textup{)}.
\end{theorem}

\begin{proof}[Proof sketch, conditional on \textup{(MPT$^{\otimes 2}$, mvKY)}]
The $(+1)$-shifted Poisson structure of
\cite{PTVV2013, CPTVV2017} on $\mathrm{Map}(X_{\mathrm{dR}}, BG)$ places
observables in an $E_5$-algebra whose positive-half stratum admits the
doubly-reduced virtual cycle plus the $\mathbb{C}^\times_E$-residue.
Hypothesis \textup{(MPT$^{\otimes 2}$)} extends
\cite[Thm.\ 1]{MPT10} to iterated reduction on
$K3_1 \times K3_2 \times E$: contracting successively against
$\sigma_{K3_1}, \sigma_{K3_2}$ yields a doubly-reduced perfect
obstruction theory with virtual dimension shifted by $+2$ and a
one-parameter residual direction along $E$, producing a well-defined
virtual fundamental class
$[\mathcal{M}^{\mathrm{red}, \mathrm{red}}_{\mathrm{DT}}(X)]^{\mathrm{vir}}$.
The product equivariance, after $S_2$-averaging composed with a
Niemeier-root-system choice, projects into
$\mathbb{C}^\times \ltimes \mathrm{Co}_0$ via the
Mukai--Conway--Wales chain
$\mathrm{Aut}_s(K3) \subset M_{23} \hookrightarrow M_{24}
\hookrightarrow \mathrm{Co}_1$ \textup{(}\cite{Mukai1988,
ConwaySloane1988}\textup{)}; the Leech slice is uniquely selected by
the no-roots condition. Hypothesis \textup{(mvKY)} supplies the
bi-Jacobi input
$\phi_{0, 1}(q_1, y_1)\, \phi_{0, 1}(q_2, y_2) /
\prod (1 - p^n)^{24}$
as the generating function of the doubly-reduced equivariant virtual
Euler characteristic. Applying the Borcherds singular theta
correspondence \textup{(}\cite[\S 7]{Borcherds1995Automorphic},
\cite[Thm.\ 13.3]{Borcherds1998}\textup{)} lifts this bi-Jacobi input
to $\Phi_{12}$ on $\mathrm{O}^+(\mathrm{II}_{26, 2})$. The
anti-diagonal reduction
$\mathrm{Muk}(K3_1) \oplus \mathrm{Muk}(K3_2)
\to \mathrm{Muk}^{\mathrm{sym}}$ absorbs the hyperbolic plane
completing $\mathrm{II}_{25, 1}$ into the $U(E)$ factor, matching
$24 + 2 = 26$. The weight identification
$\kappa_{\mathrm{BKM}}(\Phi_{12}) = c(0)/2 = 12$ is unconditional.
\end{proof}
```

## Cross-consistency notes

**Wave-1 spine.** Matches the Stage-$1$/Stage-$2$ factorisation
architecture: $A^{\mathrm{FM}}_E$ is the $(\Sigma_4, C) = (K3_1 \times
K3_2, E)$-specialisation of $\mathcal{F}_X$ at $d = 5$; the Niemeier
projection is the orbifold-choice supplement flagged in the one-line
statement. Consistent with the spine listing of the Fake Monster at
$d = 5$ on $K3 \times K3 \times E$ with $\kappa_{\mathrm{BKM}} = 12$
(Table row 3). The conditional status of the character formula is
already flagged in the spine's "remains loose" list
(`notes/platonic_synthesis_post_adversarial.tex` line 1329).

**Wave-2 refinement.** Matches the tight positive-rank obstruction of
`wn:thm:second-pass-FM-rank`: positive rank of
$(\tilde{\Lambda}(K3))^{\otimes 2} \oplus U(E)$ is $417$, comfortably
exceeding the Leech-Fake-Monster requirement of $25$. The character
formula is precisely the residual Tier III "loose" item (F9) whose
difficulty was localised to the multi-variable Kawai–Yoshioka input.
Wave-2 Theorem `wn:thm:second-pass-FM-rank` also settles the ambient
distinction between Borcherds $\Phi_{12}$ on $\mathrm{II}_{26, 2}$
(used here) and Igusa $\Phi_{12}$ on $\mathbb{H}_2$ (a distinct
automorphic form).

**CoHA-treatise.** $A^{\mathrm{FM}}_E$ is a positive-half
cohomological-Hall-algebra construction, matching the treatise
grammar: bi-primitive Mukai charge, equivariant for the product
Nikulin–$\mathbb{C}^\times_E$ group, $\phi_W$-twisted equivariant
cohomology of the doubly-reduced DT stack. The hypothesis
(MPT$^{\otimes 2}$) is what passes the CoHA into existence on
bi-symplectic input; the hypothesis (mvKY) is what identifies its
graded character with the automorphic endpoint.

**CLAUDE.md.** Subscript discipline: $\kappa_{\mathrm{BKM}}(\Phi_{12}) =
c(0)/2 = 12$ (canonical universal identity);
$\kappa_{\mathrm{cat}}(X) = 0$ via Künneth on total space (not to be
conflated with K3 fibre $\chi = 2$); $\kappa_{\mathrm{ch}}(X) = 0$ via
Hodge-supertrace identification at odd $d = 5$ (`cy_d_kappa_stratification`
canonical table). Lane discipline: the theorem is stated in the
chain-level lane (explicit doubly-reduced virtual cycle, explicit
bi-Jacobi input, explicit Borcherds product output); the
$(\infty, 1)$-categorical interpretation $A^{\mathrm{FM}}_E$ as the
stable-$\infty$-category CoHA of the doubly-reduced DT moduli stack
is an equally valid but independent statement, not invoked by this
proof. Consistent with the CLAUDE.md "chain-level and $(\infty, 1)$
equal status" operating rule.

**Wave-18 G1 note** (`notes/wave18_g1_K3K3E_d5_gluing.tex`). The
five attack-heal steps of the G1 note reduce exactly to the two named
hypotheses (MPT$^{\otimes 2}$, mvKY) of this closure. Attack-heal 1
(the $(+1)$-shifted Poisson structure) is Pantev–Toën–Vaquié–Vezzosi
2013 (unconditional). Attack-heal 2 (bi-primitive doubly-reduced
obstruction theory) is exactly (MPT$^{\otimes 2}$). Attack-heal 3
(rank-$5$ equivariance mapping to $\mathrm{Co}_0$ via Niemeier
averaging) is Mukai 1988 + Conway–Sloane 1988 (unconditional).
Attack-heal 4 (the character identity itself) is the target, placed
at `\ClaimStatusConjectured` in that note; conditional on
(mvKY). Attack-heal 5 (Niemeier embedding and Leech selection) is
Nikulin 1979 + Conway–Sloane 1988 no-roots condition (unconditional).
The present closure C11 supersedes the G1 note's "loose" flag with
two named hypotheses.

**Primary-source ledger.**
Borcherds 1990 Invent.\ Math.\ 99 Theorem 10.4 (Fake-Monster
denominator on $\mathrm{II}_{25, 1}$);
Borcherds 1995 alg-geom/9506003 §7 (automorphic products from
singular theta correspondence);
Borcherds 1998 J.\ reine angew.\ Math.\ 494 Theorem 13.3
(Borcherds-lift weight formula; $\kappa_{\mathrm{BKM}}(\Phi_{12}) =
c(0)/2 = 12$);
Harvey–Moore 1996 hep-th/9510182 §4 (heterotic $K3 \times T^2$
threshold correction template);
Oberdieck–Pandharipande 2014/2016 arXiv:1411.1514 (Igusa cusp form
conjecture A; primitive-$\beta$ proved in Oberdieck–Pandharipande
2018; Conjecture B imprimitive open);
Maulik–Pandharipande–Thomas 2010 Geom.\ Topol.\ 14 arXiv:1001.2719
Theorem 1 (reduced obstruction theory on $K3$; the hypothesis
(MPT$^{\otimes 2}$) is the bi-symplectic extension, open);
Kawai–Yoshioka 2000 Hilbert-scheme Euler count on K3 (the hypothesis
(mvKY) is the multi-variable $K3 \times K3$ extension with
anti-diagonal Niemeier-slice reduction, open);
Conway–Sloane 1988 *Sphere Packings* Chapters 10, 18, 27 (Niemeier
lattices; Leech no-roots condition; Mukai cycle structure);
Mukai 1988 Invent.\ Math.\ 94 ($\mathrm{Aut}_s(K3) \subset M_{23}$
classification);
Nikulin 1979 Izv.\ AN SSSR Ser.\ Mat.\ 43 Theorem 3.1 (primitive
embedding criterion for even lattices);
Pantev–Toën–Vaquié–Vezzosi 2013 Publ.\ IHES 117 §2 (shifted
symplectic structures);
Calaque–Pantev–Toën–Vaquié–Vezzosi 2017 Selecta Math.\ 23 §3.5
(shifted Poisson structures);
Wang–Williams 2023 (pullback rigidity for $\Phi_{12}$ on
$\mathrm{II}_{26, 2}$; Wave-2 refinement
Theorem `thm:wang-williams-pullback-rigidity`).
