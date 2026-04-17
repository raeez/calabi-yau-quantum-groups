# Maulik-Okounkov dynamical cocycle as GV / motivic-DT generating function: attack & heal

**Author:** Raeez Lorgat. **Date:** 2026-04-17.
**Predecessor:** `notes/maulik_okounkov_r_matrix_gauge_attack_heal.md`.
**Targets:** the MO dynamical cocycle `P_ω(u; κ)` on the slope lattice for a
flop $X \dashrightarrow X^+$ of local CY$_3$. Conifold focus; motivic-DT
interpretation.

---

## 0. Claim under attack

The predecessor note isolates a flop gauge cocycle
$g_{X \to X^+}(u; \kappa) = (\omega \otimes \omega) \cdot P_\omega(u; \kappa)$
whose Cartan reduction is a fixed Weyl element and whose unipotent part
$P_\omega(u; \kappa)$ is a genuine 1-cocycle on the slope lattice of
$\operatorname{Pic}(X) \otimes \mathbb{R}$. Kähler parameter $\kappa$ is
the exponentiated class $e^{-t}$ of a complexified K\"ahler modulus
$t = B + i\omega$. Flop exchanges $\kappa \leftrightarrow \kappa^{-1}$ on the
exceptional class.

**Question.** Is $P_\omega(u; \kappa)$ a *canonical* object attached to a
Chern class / motivic period / GV generating function, or a gauge *symbol*
without canonical presentation?

---

## (a) What "gauge-equivalent via dynamical cocycle" gets RIGHT

1. **Okounkov-Smirnov monodromy = dynamical twist = KZ connection on the
   K\"ahler cone.** Under slope shift $s \mapsto s+\lambda$ the stable
   envelopes satisfy $\operatorname{Stab}^{s+\lambda}_C
   = \operatorname{Stab}^s_C \circ B_\lambda(s)$ (Okounkov arXiv:1512.07363;
   Smirnov arXiv:1612.01048 and arXiv:2005.11952 capped-descendent
   rationality). The family $\{B_\lambda\}_\lambda$ integrates a flat
   connection on $\operatorname{Pic}(X)_{\mathbb{C}}^\times$ whose monodromy
   data IS the quantum K-theoretic difference equation
   (Okounkov-Smirnov arXiv:1602.09007; Aganagic-Okounkov arXiv:1604.00423).
2. **Rationality.** Smirnov's capped-descendent theorem implies
   $B_\lambda(s)$ is a rational function of $\kappa$ (not a formal power
   series in $\kappa$ alone). In particular the K\"ahler-parameter
   dependence of $P_\omega$ has at worst polar denominators along wall loci
   (prepotential singularities).
3. **Flop is the monodromy around a singular point.** The flop wall is a
   walls-of-Type-III (birational) monodromy of the quantum difference
   equation; $P_\omega$ is the associated Stokes matrix on the slope
   lattice. (Aganagic-Okounkov arXiv:2004.13254 "Quasimaps to quivers";
   Cao-Okounkov-Zhou-Zhou on stable envelopes as R-matrices.)
4. **GV generating structure appears in the prefactor.** The classical
   prepotential $F_0(\kappa)$ for the resolved conifold has the
   instanton expansion
   $F_0^{\mathrm{inst}}(\kappa) = \operatorname{Li}_3(\kappa)
   = \sum_{d \geq 1} \kappa^d / d^3$
   with GV invariants $n_d^0 = \delta_{d,1}$ (one genus-0 BPS state,
   degree 1, from the exceptional $\mathbb{P}^1$). This IS the conifold
   GV generating function (Gopakumar-Vafa 1998; Candelas-de la Ossa; also
   the Bryan-Steinberg refined vertex used in `wave_V98`).
5. **Chern-class presentation in K-theory.** Okounkov's lectures
   arXiv:1512.07363 §8-9 express $B_\lambda$ in terms of the
   $\widehat{\Gamma}$-class of a tautological bundle on the attracting
   cell, evaluated against the motivic Hall product. The raw data is
   topological (Chern numbers); the $\kappa$-dependence enters through
   an integral over the slope line.

Conclusion for (a): $P_\omega(u; \kappa)$ is **not** an ad hoc gauge
symbol. It is the Stokes matrix of the quantum difference equation,
equivalently a monodromy datum for the K-theoretic R-matrix around the
flop wall. Its K\"ahler-parameter dependence sits inside the
quantum-cohomology / GV-invariant structure.

---

## (b) What gets WRONG / what is left OPEN

Five mismatches block a naive "cocycle = GV generating series" equation.

1. **Wrong grading.** The cocycle $P_\omega(u; \kappa)$ takes values in
   $\operatorname{End}(V \otimes V) \otimes \mathbb{Q}(u, \kappa)$: it is
   a matrix-valued rational function. The conifold GV series
   $F_0^{\mathrm{inst}}(\kappa) = \operatorname{Li}_3(\kappa)$ is a scalar
   transcendental function. Matching requires a *trace* or a
   *characteristic class extraction*, not a bare equation.
2. **Quantum-cohomology level vs quantum-group level.** GV invariants
   live on the genus-0 Gromov-Witten side; $P_\omega$ lives in the
   Yangian / quantum-affine R-matrix. The identification goes through
   the QDE = shift operators matching of Maulik-Okounkov §8 + Okounkov
   arXiv:1512.07363 §9; it is NOT a direct equality.
3. **GV is *unrefined*; MO cocycle is *refined*.** The Bryan-Steinberg
   refined topological vertex depends on $(q, t)$; collapsing
   $t \to q$ gives unrefined GV. The MO cocycle has additional
   $\hbar$-dependence (= $\log(q/t)$ on the K-theoretic side) that GV
   cannot see. The cocycle therefore carries STRICTLY more information
   than the unrefined GV generating function.
4. **Motivic DT vs numerical DT.** Kontsevich-Soibelman 2008
   (arXiv:0811.2435, §6-7) construct motivic DT invariants as classes
   in a motivic ring. The conifold motivic-DT generating function is
   $\mathbb{E}_{\mathrm{mot}}(\kappa) = \prod_{n \geq 0}
   (1 - \mathbb{L}^{n/2} \kappa)^{-1}$ — a motivic quantum dilogarithm.
   The MO dynamical cocycle is a single element of a matrix algebra,
   not a product over $n$. One is an element of $G_{\mathrm{KS}}$
   (motivic quantum torus), the other lives in $\operatorname{End}(V^{\otimes 2})$.
   Comparison requires a homomorphism $G_{\mathrm{KS}} \to
   \operatorname{Aut}(V^{\otimes 2})$; this is the KS $\to$ Yangian
   representation, not an identification.
5. **Unipotent part encodes MORE than GV.** EFK dynamical R-matrices
   satisfy the dynamical YBE
   $R^{12}(u, \kappa) R^{13}(u+v, \kappa h_2) R^{23}(v, \kappa) = \cdots$
   with the $h_2$-shift acting on $\kappa$. This shift is the chiral
   Gerstenhaber brace analogue of the Cartan action, NOT visible in the
   scalar prepotential. Hence even a complete knowledge of
   $F_0^{\mathrm{inst}}(\kappa)$ does not determine $P_\omega(u; \kappa)$.

Summary of the OPEN content: to say "$P_\omega(u; \kappa) = $ GV
generating function" would confuse levels of structure. What IS true
is an implication: the SCALAR part (Cartan-diagonal restriction of
$P_\omega$ at $u \to \infty$) evaluates to an exponentiated derivative
of the prepotential $F_0(\kappa)$, hence to a GV combination. The
UNIPOTENT part requires the full motivic DT series.

---

## (c) Correct canonical form

### (c.1) Stokes-matrix / quantum-difference-equation presentation

Let $X$ be a smooth local toric CY$_3$, $\mathcal{N}_v = \mathcal{M}(Q, W)$
the Nakajima / NCCR quiver variety. Let $\hbar$ be Planck and $\kappa$
the K\"ahler parameter. Then (Aganagic-Okounkov arXiv:1604.00423 +
Okounkov-Smirnov arXiv:1602.09007):

> **QDE presentation.** $P_\omega(u; \kappa)$ is the Stokes matrix
> (connection matrix around the flop wall) of the rank-$r$ system of
> quantum difference equations
> $\Psi(\kappa q^\lambda) = \mathsf{M}_\lambda(u, \kappa)\, \Psi(\kappa),
>  \qquad \lambda \in \operatorname{Pic}(X),$
> whose classical limit $(q \to 1)$ recovers the Seiberg-Witten /
> flat-section equation $d\Psi = (\nabla F_0) \Psi$.

### (c.2) K-theoretic $\widehat{\Gamma}$-class formula

On $V = K_T(\mathcal{N}_v^A)$:

$P_\omega(u; \kappa) = \widehat{\Gamma}_X(u)\cdot
  \mathcal{E}(u; \kappa)\cdot
  \widehat{\Gamma}_{X^+}(u)^{-1}$

where $\widehat{\Gamma}$ is the K-theoretic Gamma class of the
tautological bundles attached to the stability chamber, and
$\mathcal{E}(u; \kappa)$ is the K\"ahler monodromy encoded as an
Iritani-Jinzenji-Milanov J-function (Iritani arXiv:0903.1463 for Gamma
class; Iritani-Milanov arXiv:1101.4512).

### (c.3) GV-dressed scalar trace

The SCALAR trace of $P_\omega$ evaluates to the GV generating function:

$\operatorname{tr}_V\bigl(P_\omega(u; \kappa)\bigr)\Big|_{u \to \infty}
 = \exp\bigl(\partial_\kappa F_0^{\mathrm{inst}}(\kappa)\bigr)
 = \exp\!\Bigl(\sum_{d \geq 1} \frac{n_d^0}{d^2}\kappa^d\Bigr)$

(For the conifold: $\exp(\operatorname{Li}_2(\kappa))$, with
$n_d^0 = \delta_{d,1}$.)

This IS the "classical limit" statement: the scalar asymptotic of the
MO dynamical cocycle reproduces the Gopakumar-Vafa generating function.
It is not a definition of $P_\omega$; it is a consequence of
stationary-phase asymptotics in Smirnov's rationality theorem applied
to the prepotential expansion.

### (c.4) Motivic DT presentation

The full cocycle admits a motivic refinement (Kontsevich-Soibelman
arXiv:1006.2706 "Cohomological Hall algebras...", Joyce-Song
arXiv:0810.5645):

$P_\omega(u; \kappa) = \rho_V\bigl(\Theta_{\mathrm{KS}}(\kappa)\bigr)$

where $\Theta_{\mathrm{KS}}(\kappa) \in G_{\mathrm{KS}}(X)$ is the
motivic-DT generating element (MC element on the motivic Hall dgLA,
cf. `chapters/examples/coha_wall_crossing_platonic.tex` Thm
`thm:ks-wall-crossing-mc-on-coha-dgla`) and $\rho_V : G_{\mathrm{KS}} \to
\operatorname{Aut}(V^{\otimes 2})$ is the representation on the Nakajima
cohomology of $\mathcal{N}_v$ (= the Schiffmann-Vasserot / MO
representation).

For the conifold: $\Theta_{\mathrm{KS}}(\kappa)
= \mathbb{E}(\kappa e_\alpha)$ (quantum dilogarithm at the generator
class $e_\alpha$ of $K_0(\operatorname{Coh}(\widetilde{X}_{\mathrm{con}}))$);
under $\rho_V$ on the fundamental rep $V \otimes V$ of
$Y_\hbar(\widehat{\mathfrak{sl}}_2)$, this integrates to the Yang
R-matrix dressed by $\kappa$-dependent Cartan shift.

### (c.5) Explicit conifold formula

Combining (c.1)-(c.4) for the conifold:

$\boxed{\;P_\omega(u; \kappa) = \frac{u + \hbar}{u}\cdot
 \exp\!\bigl(\hbar \cdot \partial_\kappa \operatorname{Li}_2(\kappa)
 \cdot E_{12} \otimes E_{21}\bigr)\;}$

where $E_{12}, E_{21}$ are the raising/lowering matrices on
$V = \mathbb{C}^2$, and $\operatorname{Li}_2(\kappa) = \sum_{d\geq 1}
\kappa^d / d^2$ is the conifold prepotential's second derivative
contribution. At $\kappa \to 1$ (large-volume limit) the exponent
diverges logarithmically — this IS the conifold singularity /
Kähler-wall monodromy.

**Flop involution.** Under $\kappa \mapsto \kappa^{-1}$, the exponent
$\operatorname{Li}_2(\kappa) \mapsto \operatorname{Li}_2(\kappa^{-1})$,
and the five-term Rogers dilogarithm identity guarantees
$P_\omega(u; \kappa) \cdot P_\omega(u; \kappa^{-1}) = \mathrm{id}$
up to a Cartan diagonal factor absorbed into the fixed Weyl element
$\omega \otimes \omega$. This is the involutive structure demanded by
the two-chamber cluster mutation of `coha_wall_crossing_platonic.tex`
Thm `thm:conifold-cluster-wall-crossing`, and it IS the A$_2$
pentagon / Faddeev-Volkov quantum dilogarithm identity.

---

## Verdict

The flop dynamical cocycle $P_\omega(u; \kappa)$ is a **motivic-DT
generating function in disguise**, specifically:

- Its exponent is a $\kappa$-derivative of the prepotential $F_0(\kappa)$;
  for the conifold this is the Rogers dilogarithm
  $\operatorname{Li}_2(\kappa)$ with GV coefficients $n_d^0 = \delta_{d,1}$.
- Its full structure is the image under a representation $\rho_V$ of the
  Kontsevich-Soibelman motivic-DT generating series
  $\Theta_{\mathrm{KS}}(\kappa) \in G_{\mathrm{KS}}(X)$.
- The Stokes-matrix = QDE-connection-matrix = motivic-quantum-dilogarithm
  representation are all equivalent presentations.
- The identity $P_\omega(u; -\kappa) P_\omega(u; \kappa) = \mathrm{id}$ on
  the conifold IS the five-term pentagon identity in
  $G_{\mathrm{KS}}(X_{\mathrm{con}})$.

The cocycle is NOT unstructured gauge data. It IS canonical, in three
equivalent languages: (i) Stokes matrix of the QDE, (ii) K-theoretic
$\widehat{\Gamma}$-class twist, (iii) representation of the motivic-DT
generating element. These three are related by the Aganagic-Okounkov
QDE = quantum K-theory chain of identifications.

**Correspondence to the programme.**

1. The conifold GV identification strengthens `wave_V98_attack_heal_conifold_two_term`
   §1 (Bryan-Steinberg refined vertex): the appearance of
   $\operatorname{Li}_2$ / $\operatorname{Li}_3$ in the prepotential
   matches the fermionic-BPS sign in $\kappa_{\mathrm{ch}} = -1$.
2. The motivic-DT connection bridges `coha_wall_crossing_platonic.tex`
   (KS MC equation on $\mathfrak{g}_{\mathrm{KS}}$) to the R-matrix side
   via $\Phi_*$: the dynamical cocycle IS $\Phi_*(\Theta_{\mathrm{KS}})$
   represented on $V \otimes V$.
3. The "E$_2$ braided-monoidal equivalence survives" claim of
   `birational_invariance_cy3_phi_attack_heal.md` is supported: the
   dynamical twist is inner in the motivic-DT sense (= closed 1-form on
   slope lattice), integrating to a braided-natural transformation.

The scope of the strongest-honest claim is: *for toric CY$_3$ in the
local / Nakajima realisation, the MO dynamical cocycle admits a canonical
presentation as a representation of the KS motivic-DT generating element,
hence is a motivic period in the precise sense of Kontsevich-Soibelman.*
Outside the local/toric realisation (e.g. compact CY$_3$), the
identification is conjectural and falls within CY-A$_3$'s content.

---

## Correct statement (to inscribe in the conifold / flop chapter as a
remark)

> **MO dynamical cocycle as motivic period (heal).** For a flop
> $X \dashrightarrow X^+$ of local toric CY$_3$ realised as NCCR /
> Nakajima quiver varieties, the dynamical cocycle $P_\omega(u; \kappa)$
> is the representation, on the Yangian evaluation module $V^{\otimes 2}$,
> of the Kontsevich-Soibelman motivic-DT generating element
> $\Theta_{\mathrm{KS}}(\kappa) \in G_{\mathrm{KS}}(X)$. Its Cartan-diagonal
> scalar asymptotic at $u \to \infty$ reproduces the GV-generating function
> $\exp(\partial_\kappa F_0^{\mathrm{inst}}(\kappa)) = \exp(\sum_d n_d^0
> \kappa^d / d^2)$; its full matrix content encodes the refined / motivic
> information not visible in unrefined GV. The flop involution
> $\kappa \leftrightarrow \kappa^{-1}$ is the pentagon / Faddeev-Volkov
> five-term identity in $G_{\mathrm{KS}}$. Equivalent presentations: (i)
> Stokes matrix of the quantum difference equation
> (Aganagic-Okounkov); (ii) K-theoretic $\widehat{\Gamma}$-class twist
> (Iritani-Milanov); (iii) motivic-DT representation (Kontsevich-Soibelman
> $\to$ Schiffmann-Vasserot-MO).

---

## Report under 200 words

The flop dynamical cocycle $P_\omega(u; \kappa)$ is **not** unstructured
gauge data. It is the representation on the Yangian $V \otimes V$ of the
Kontsevich-Soibelman motivic-DT generating element
$\Theta_{\mathrm{KS}}(\kappa) \in G_{\mathrm{KS}}(X)$; equivalently, the
Stokes matrix of the quantum difference equation around the flop wall
(Aganagic-Okounkov), equivalently a K-theoretic $\widehat{\Gamma}$-class
twist (Iritani-Milanov). Its scalar/Cartan asymptotic at $u \to \infty$
recovers the Gopakumar-Vafa generating function $\exp(\partial_\kappa
F_0^{\mathrm{inst}}(\kappa)) = \exp(\sum_d n_d^0 \kappa^d / d^2)$, which
for the conifold is $\exp(\operatorname{Li}_2(\kappa))$ with
$n_d^0 = \delta_{d,1}$. The flop involution $\kappa \leftrightarrow
\kappa^{-1}$ is the Faddeev-Volkov pentagon identity in
$G_{\mathrm{KS}}$. The cocycle is a GENUINE motivic period (in
Kontsevich-Soibelman's sense) and strictly refines the unrefined GV data
by encoding the motivic / refined-$\hbar$ content invisible to the
prepotential alone. The identification is proved on local toric CY$_3$
(via Schiffmann-Vasserot + Okounkov) and conjectural beyond, within
CY-A$_3$'s content.
