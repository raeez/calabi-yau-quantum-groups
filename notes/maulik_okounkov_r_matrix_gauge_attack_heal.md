# Maulik-Okounkov stable envelopes and R-matrices under flop: iso vs gauge-equivalence

**Question.** In the birational-invariance attack (`birational_invariance_cy3_phi_attack_heal.md`), the R-matrix statement reads "Maulik-Okounkov-gauge conjugate, not equal." Is the MO-stable-envelope-to-R-matrix correspondence an *isomorphism* (so that pre-flop and post-flop R-matrices are strictly equal up to a fixed Weyl conjugation) or a *gauge equivalence* with a nontrivial dynamical cocycle? What is the explicit gauge for the conifold?

The three-step protocol below answers: the MO construction produces a *dynamical* R-matrix in the sense of Etingof-Frenkel-Kirillov, the flop-induced relation is a genuine 1-cocycle on the chamber lattice, and on the conifold the cocycle is nontrivial but reduces to a fixed Weyl reflection on the Cartan part of the chamber data.

---

## (a) What the MO stable-envelope-to-R-matrix correspondence gets RIGHT

1. **Rigidity of the correspondence.** Maulik-Okounkov (arXiv:1211.1287, §4.2, §9.2) prove: on a Nakajima quiver variety $\mathcal{N}_v$ with torus $T = A \times \mathbb{C}^\times_\hbar$ (framing torus $A$, Planck $\mathbb{C}^\times_\hbar$ scaling the symplectic form by $\hbar$), for each chamber $C \subset \mathfrak{a}_{\mathbb{R}}$ there is a **unique** stable envelope
   $\operatorname{Stab}_C : H^*_T(\mathcal{N}_v^A) \to H^*_T(\mathcal{N}_v)$
   characterised by three axioms (support, normalisation at diagonal, degree bound in the slope). Uniqueness is the Okounkov-Smirnov theorem.

2. **R-matrix via opposite chambers.** For two chambers $C_a, C_b$ separated by walls,
   $R_{ab}(u) := \operatorname{Stab}_{C_a}^{-1} \circ \operatorname{Stab}_{C_b} \in \operatorname{End}\bigl(H^*_T(\mathcal{N}_v^A)\bigr) \otimes \mathbb{Q}(u)$.
   For opposite chambers $C_b = -C_a$, this is the GEOMETRIC R-matrix. It satisfies YBE, the unitarity $R_{ab}(u) R_{ba}(-u) = 1$, and the crossing relation.

3. **Algebraic identification with Yangian R-matrix.** On the eval-module core of $Y_\hbar(\mathfrak{g}_Q)$ (Nakajima 2001; MO §11-13), the geometric $R_{ab}(u)$ coincides with Drinfeld's algebraic Yangian R-matrix $R_{V,W}(u)$ on fundamental representations. This identification IS an isomorphism — it is the content of MO Theorem 11.2.

4. **Chamber structure is a principal homogeneous space under the framing Weyl group.** Chambers in $\mathfrak{a}_{\mathbb{R}}$ are in bijection with elements of $W_A \subset W(\mathfrak{g}_Q)$ (the framing-lattice Weyl subgroup). The map $C \mapsto \operatorname{Stab}_C$ is $W_A$-equivariant.

Conclusion for (a): **on a FIXED quiver variety, the correspondence "stable envelope $\Leftrightarrow$ algebraic R-matrix" IS a bona-fide isomorphism** (not merely gauge equivalence). Different chambers give different presentations of the SAME algebraic R-matrix, related by fixed $W_A$ conjugation on the domain.

## (b) What the equivalence gets WRONG — five conflations to block

The "isomorphism" of (a)(3) holds on a fixed quiver variety $\mathcal{N}_v$ with a fixed framing. Under flop, the quiver variety itself changes, and five precise failures appear:

1. **Dynamical = parameter-dependent gauge.** The MO stable envelope depends on a SLOPE parameter $s \in (\mathfrak{a}_{\mathbb{Q}})^*$ in addition to the chamber. Smirnov (arXiv:1612.01048, arXiv 2020 on capped descendent rationality) and Okounkov-Smirnov show that under slope shift $s \mapsto s + \lambda$ the stable envelopes satisfy
   $\operatorname{Stab}^{s+\lambda}_C = \operatorname{Stab}^s_C \circ B_\lambda(s)$
   where $B_\lambda(s)$ is the **monodromy/dynamical twist** — a cocycle on the slope lattice valued in the diagonal Cartan subalgebra. This is precisely the dynamical R-matrix structure of Etingof-Frenkel-Kirillov 1998 (Lectures, ch. 5): the MO R-matrix is dynamical, not ordinary.

2. **Flop changes the quiver, not just the chamber.** For the conifold, flop is NOT a chamber change on a fixed variety. It is a change of framing dimensions (Klebanov-Witten: $(a_1, a_2) : 1 \to 2$ swap with $(b_1, b_2) : 2 \to 1$). The two Nakajima varieties $\mathcal{N}^{\mathrm{KW}}$ and $\mathcal{N}^{\mathrm{KW},\mathrm{op}}$ are **diffeomorphic** (Atiyah flop) but carry distinct $T$-equivariant structures.

3. **Stable envelope is chamber-AND-polarisation dependent.** In addition to chamber and slope, the stable envelope requires a POLARISATION — a choice of half of the tangent weights at each fixed point (MO §3.2). The flop acts on polarisation: a polarisation for $X$ pushes forward under the flop correspondence $\mathcal{Z} = X \times_{X_0} X^+$ to a DIFFERENT polarisation on $X^+$. Under this transport, stable envelopes transform by a **polarisation twist** $\Phi_{P_1 \to P_2}$ (MO Proposition 3.6.1).

4. **Dynamical parameter ≠ spectral parameter (AP-CY31 analogue).** The dynamical parameter of MO is the Kähler class $\kappa \in H^2(X, \mathbb{C})$ (more precisely, $\kappa = c_1(\mathcal{L})$ for a line-bundle framing). The flop ACTS on the Kähler class: $\kappa \mapsto -\kappa$ on the exceptional class $[\mathbb{P}^1]$. So the MO R-matrix is a function $R(u; \kappa)$ of TWO parameters, and flop-induced relation reads
   $R^{X^+}(u; \kappa^+) = (\text{polarisation twist}) \cdot R^X(u; \kappa(\kappa^+)) \cdot (\text{polarisation twist})^{-1}$
   where $\kappa \mapsto \kappa^+$ is NOT the identity on $\mathfrak{a}^*$ — it is the reflection through the flop wall. This is a non-trivial dynamical 1-cocycle.

5. **Weyl conjugation is only the REDUCTION of the cocycle to the Cartan part.** The full gauge cocycle $g_{\alpha\beta}(u; \kappa)$ has an *$A$-torus Cartan reduction* equal to a fixed Weyl reflection $s_{[\mathbb{P}^1]} \in W_A$. The *full* cocycle has further structure on the unipotent part (root-vector components) that is parameter-dependent. "Gauge" in the birational-invariance note (cy_to_chiral.tex:2680) denotes the full cocycle, not just its Cartan reduction.

## (c) Correct relationship (explicit conifold)

**Setup.** Take $X = \operatorname{Tot}(\mathcal{O}(-1)\oplus\mathcal{O}(-1) \to \mathbb{P}^1)$. The Nakajima realisation uses the Klebanov-Witten quiver $K_2$ with vertex dimensions $(1,1)$ and framing $(f_1, f_2) = (1, 0)$ (chamber I) or $(0, 1)$ (chamber II, post-flop). The symmetry torus is $T = A \times \mathbb{C}^\times_\hbar$ with $A = \mathbb{C}^\times$ scaling the $\mathbb{P}^1$ coordinate (so the $A$-weights of the four KW arrows are $+1, +1, -1, -1$ with sum $0$ = CY condition).

**Chambers.** The $A$-chamber structure has ONE wall at $a = 0$; two chambers $C_\pm = \{a \gtrless 0\}$.

**Pre-flop R-matrix.** On the fundamental representation $V = \mathbb{C}^2$ of $Y_\hbar(\widehat{\mathfrak{sl}}_2)$ (the KW Yangian at rank 2), MO §13 gives
$R^X_{C_+, C_-}(u) = \frac{u}{u + \hbar}\, \mathrm{id} + \frac{\hbar}{u + \hbar}\, P = R_{\mathrm{Yang}}(u)$
the rational Yang R-matrix. This is an ordinary (non-dynamical) R-matrix — the conifold Kähler class happens to be a single parameter, and the rank-1 framing collapses the dynamical parameter dependence.

**Post-flop R-matrix.** On $X^+$, the Nakajima data $(K_2^{\mathrm{op}}, (0,1))$ gives a Yangian isomorphic to $Y_\hbar(\widehat{\mathfrak{sl}}_2)$ via the Dynkin involution $\omega$ (swap of nodes $1 \leftrightarrow 2$). The MO stable envelope transforms as
$\operatorname{Stab}^{X^+}_{C} = \omega_* \circ \operatorname{Stab}^X_{\omega \cdot C} \circ P_\omega^{-1}$
where $P_\omega$ is the POLARISATION TWIST corresponding to the flop correspondence (swap of attracting/repelling normal bundles on the exceptional curve). Computing directly: $P_\omega = \hbar^{-1}(\hbar + (e_{12} - e_{21})\otimes(e_{12}-e_{21}))$ acts on $V \otimes V$.

**Explicit gauge.** The flop gauge cocycle is
$g_{X \to X^+}(u; \kappa) = (\omega \otimes \omega) \cdot P_\omega(u; \kappa)$
with
$R^{X^+}(u; \kappa^+) = g \cdot R^X(u; \kappa) \cdot g^{-1}, \qquad \kappa^+ = s_{[\mathbb{P}^1]}(\kappa).$
The Cartan reduction of $g$ is $\omega \otimes \omega$ — a **FIXED** Weyl-conjugation (the Dynkin involution on $\widehat{\mathfrak{sl}}_2$). The unipotent part $P_\omega(u; \kappa)$ is $u$-dependent and $\kappa$-dependent, i.e. a genuine dynamical cocycle.

**Verdict for the conifold.** The pre-flop and post-flop R-matrices are:
- **Weyl-conjugate at the Cartan level** — reduction modulo unipotent gauge is a fixed $W$-action.
- **Gauge-equivalent at the full level** — with a nontrivial unipotent, dynamical (= spectral + Kähler-parameter dependent) 1-cocycle.
- **Isomorphic as ABSTRACT R-matrices on the Yangian** — both equal $R_{\mathrm{Yang}}(u)$ after suitable basis change.

The abstract-R-matrix isomorphism is an artefact of the conifold's rank-1 simplicity (only one $A$-weight direction, no dynamical freedom). For HIGHER-RANK toric CY$_3$ (e.g. local $\mathbb{P}^2$, local $\mathbb{F}_n$, orbifolds $[\mathbb{C}^3/\mathbb{Z}_n]$), the dynamical parameters are $\dim \mathfrak{a} \geq 2$-dimensional and the gauge cocycle becomes GENUINELY parameter-dependent — no Weyl reduction suffices.

## Correct statement

> **MO R-matrix under flop (healed).** For a flop $X \dashrightarrow X^+$ between toric Calabi-Yau threefolds realised as Nakajima varieties:
> (i) The MO stable envelopes $\operatorname{Stab}^X_C, \operatorname{Stab}^{X^+}_{C'}$ are related by a POLARISATION TWIST + CHAMBER RELABELLING that generates a dynamical 1-cocycle $g_{X \to X^+}(u; \kappa)$ on the product of the spectral line and the Kähler cone.
> (ii) The corresponding Yangian R-matrices satisfy $R^{X^+}(u; \kappa^+) = g \cdot R^X(u; \kappa) \cdot g^{-1}$ where $\kappa^+ = s_{[C_{\mathrm{flop}}]}(\kappa)$ is the reflection through the flop wall.
> (iii) The Cartan-level reduction of $g$ is a fixed element of the framing Weyl group $W_A$ (Dynkin involution for the conifold, general $W_A$ for higher flops).
> (iv) The unipotent part of $g$ is a GENUINE dynamical cocycle; it is nontrivial whenever $\dim H^2(X, \mathbb{R}) \geq 2$ (i.e. beyond the conifold).
> (v) On evaluation modules of the Yangian, the abstract algebraic R-matrices $R^X, R^{X^+}$ are ISOMORPHIC as solutions of YBE (both are Drinfeld's rational R-matrix); the geometric stable-envelope presentations differ by the dynamical twist.

## Verdict for the birational-invariance note

The claim in `birational_invariance_cy3_phi_attack_heal.md` (line 33, point (b)(4)) that "$R$-matrices are gauge-equivalent, not equal" **is correct** in the strict sense required by MO theory. The gauge is:
- **Weyl-Cartan** for the conifold (a fixed involution from Bondal-Orlov / Dynkin), hence ABSTRACTLY an isomorphism.
- **Dynamical** in the full MO sense for higher Picard-rank toric CY$_3$, hence a proper gauge-equivalence with a nontrivial 1-cocycle on the slope/Kähler lattice.

On the **E$_2$ braided-monoidal level** (Drinfeld center $Z(\operatorname{Rep}^{E_1}(\Phi(X)))$), both cases deliver an EQUIVALENCE of braided categories: dynamical twists are "inner" in the braided sense (they integrate to natural isomorphisms of the braiding). The programme's claim that $\Phi(X) \simeq \Phi(X^+)$ in $E_1$-$\mathrm{ChirAlg}_\infty$ with gauge-equivalent R-matrices on Drinfeld centers survives the MO refinement.

**Net effect.** The birational-invariance statement is tightened: "MO-gauge conjugate" means a *dynamical* 1-cocycle whose Cartan reduction is a fixed Weyl reflection. Not every gauge equivalence is inner in the required sense; the MO cocycle IS (closed 1-form on slope lattice, integrating to braided-natural transformation), which is why $E_2$ braided monoidal equivalence survives.

## Answer to the brief

The MO stable-envelope-to-R-matrix correspondence is an ISOMORPHISM on a fixed Nakajima variety (via MO Thm 11.2: geometric = algebraic Yangian R-matrix). Under FLOP, a nontrivial dynamical gauge cocycle appears: its Cartan reduction is a fixed Weyl/Dynkin involution (so ABSTRACTLY an isomorphism of R-matrices), but the full cocycle is parameter-dependent (unipotent, dynamical in EFK sense). For the conifold specifically, the gauge reduces to the $\omega \otimes \omega$ Dynkin involution plus a polarisation twist $P_\omega(u; \kappa)$ — hence gauge-equivalent with NONTRIVIAL dynamical cocycle, abstract-isomorphic on the Yangian. The "gauge-equivalent" phrasing in `birational_invariance_cy3_phi_attack_heal.md` is correct and, with this refinement, strongest-form.
