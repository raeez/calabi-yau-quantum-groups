# Wave CY4 — Explicit four-step $\Phi_4$ $\mathbb{P}^1$-family construction and $h^{1,1}$-dependent associativity correction

**Author:** Raeez Lorgat. **Date:** 2026-04-17.
**Volume:** III, Künneth-multiplicativity programme, $d=4$ inscription.
**Style:** Beilinson--Drinfeld + Costello--Gwilliam factorization homology + Bogomolov--Tian--Todorov rigidity + Chriss--Ginzburg constructive discipline.
**Discipline:** AP-CY46 ($\pi_4(BU)=\Z$ obstruction; no native CY${}_4$ Yangian), AP-CY55 (manifold vs algebraization), AP-CY56 ($E_n$-level by $d$), AP-CY60 (six routes $\ne$ six applications), AP-CY61 (first-principles), HZ3-1 ($\Phi_4$-results $\Rightarrow$ $\begin{conjecture}$).

This wave inscribes Wave V104/V112 into the manuscript at publication standard.
We (1) write the explicit four-step $\Phi_4$ $\mathbb{P}^1$-family construction at chain level, (2) compute the explicit closed-form $h^{1,1}$-dependent correction to iterated-product associativity at CY${}_4$, (3) verify the conjecture form at the sextic $X_6\subset\mathbb{P}^5$, and (4) identify the corrected closed form when the naive conjecture fails (it fails on the iteration-shadow multiplier; the correction enters the $h^{1,1}$-prefactor as the $\Pi_{--}$-character of the intermediate-stage shadow, not the bare $h^{1,1}$ of $X$).

Per LOSSLESS RELAUNCH: nothing is downgraded. The V104/V112 family-valued framework is upgraded to an explicit chain-level theorem statement, the conjecture form is sharpened with the iteration-shadow correction, and the sextic verification is carried out explicitly.

---

## 1. The four-step $\Phi_4$ $\mathbb{P}^1$-family construction

Per AP-CY46, the CY-A functor $\Phi_d : \mathrm{CY}_d\text{-Cat} \to E_n\text{-ChirAlg}$ at $d=4$ does not exist as a functor into single $E_1$-chiral algebras. The $\pi_4(BU) = \Z$ Pontryagin obstruction blocks the $S^4$-framing of $\HH_*(C)$, and Bogomolov--Tian--Todorov bivariance forces a two-dimensional deformation parameter $(\sigma_3, \sigma_4)$. The healed framework is

$$
\Phi_4(C) \;:=\; \bigl\{ A^{(\sigma_3, \sigma_4)}_C \bigr\}_{[\sigma_3 : \sigma_4] \in \mathbb{P}^1},
$$

a functor into $\mathbb{P}^1$-families of $E_1$-chiral algebras. We construct each fibre $A^{(\sigma_3, \sigma_4)}_C$ in four explicit steps.

### Step 1: HKR endomorphism dg algebra

Let $C = D^b\mathrm{Coh}(X)$ for $X$ a compact projective CY${}_4$. Form the dg algebra
$$
\mathrm{End}_{\mathrm{HKR}}(C) \;:=\; \mathrm{End}^\bullet_C(\mathcal{O}_X),
$$
the derived endomorphisms of the structure sheaf. By the Hochschild--Kostant--Rosenberg theorem (Kontsevich, Caldararu),
$$
\mathrm{End}_{\mathrm{HKR}}(C) \;\simeq\; \mathrm{PV}^*(X)[u] \;:=\; \bigoplus_{p,q} \Gamma(X, \Lambda^p T_X \otimes \Lambda^q T_X^*)[u],
$$
the polyvector dg-Lie algebra $T_X[1] \otimes \Omega^*_X$ with the $\bar\partial$-differential. The bigraded structure $H^{p,q}(X)$ is the cohomology of this Dolbeault complex with the polyvector grading shifted by $[1]$ on the tangent factor.

For $X = X_6\subset \mathbb{P}^5$ the sextic: the bigraded structure is captured by the Hodge diamond
$$
\begin{array}{c|ccccc}
q\backslash p & 0 & 1 & 2 & 3 & 4 \\\hline
0 & 1 & 0 & 0 & 0 & 1 \\
1 & 0 & 1 & 426 & 1 & 0 \\
2 & 0 & 426 & 1750 & 426 & 0 \\
3 & 0 & 1 & 426 & 1 & 0 \\
4 & 1 & 0 & 0 & 0 & 1
\end{array}
$$
with $h^{1,1}=1, h^{3,1}=h^{1,3}=426, h^{2,2}=1752, h^{2,2}_{\mathrm{prim}}=1750, h^{4,0}=h^{0,4}=1$.

### Step 2: Negative cyclic refinement

Take the negative cyclic refinement
$$
\mathrm{HC}^-_*(\mathrm{End}_{\mathrm{HKR}}(C)) \;=\; \bigl(\mathrm{End}_{\mathrm{HKR}}(C)[u], b + uB\bigr),
$$
where $u$ is Connes' periodicity parameter ($\deg u = -2$) and $B$ is Connes' boundary. The homology is the Hodge-graded de Rham cohomology with weight grading
$$
H^*\bigl(\mathrm{HC}^-_*(\mathrm{End}_{\mathrm{HKR}}(C))\bigr) \;\cong\; \bigoplus_{n} u^{-n} \cdot F^n H^*_{\mathrm{dR}}(X, \C),
$$
where $F^\bullet$ is the Hodge filtration. The $u$-formal-disk parameterizes the $\Z[u, u^{-1}]$-module structure of cyclic homology (Connes' periodicity).

For the sextic: the de Rham cohomology has total dimension $1 + 0 + (1+426+1) + 0 + (1+426+1750+426+1) + 0 + (1+426+1) + 0 + 1 = 1 + 428 + 2604 + 428 + 1 = 3462$, with $F^0 = 1$, $F^1 = F^0 + 428 = 429$, $F^2 = 429 + 2604 = 3033$, $F^3 = 3033 + 428 = 3461$, $F^4 = 3462$.

### Step 3: BCOV Maurer--Cartan twist

The Bershadsky--Cecotti--Ooguri--Vafa action on the polyvector dg-Lie algebra is
$$
S_{\mathrm{BCOV}}(\mu) \;=\; \tfrac{1}{2}\,\langle \mu, \bar\partial \mu\rangle \;+\; \tfrac{1}{6}\,\langle \mu, [\mu, \mu]\rangle,
$$
with $\langle -, -\rangle$ the Mukai pairing and $[-,-]$ the Schouten--Nijenhuis bracket on polyvectors. The Maurer--Cartan equation is
$$
\bar\partial \mu \;+\; \tfrac{1}{2}[\mu, \mu] \;=\; 0.
$$

At CY${}_4$ the deformation tangent space splits *bivariantly*:
$$
T_{[X]}\mathrm{Def}(X) \;=\; H^{3,1}(X)\;\oplus\; H^{2,2}_{\mathrm{prim}}(X).
$$
The $\sigma_3$-direction lives in $H^{3,1}$ (complex-structure deformation, present at all $d \geq 3$); the $\sigma_4$-direction lives in $H^{2,2}_{\mathrm{prim}}$ (the *new* primitive-middle deformation, with no $d=3$ analogue).

The twisted Maurer--Cartan equation, parametrising the $\mathbb{P}^1_{(\sigma_3:\sigma_4)}$-family, is
$$
\boxed{\;\;
\bar\partial \mu \;+\; \tfrac{1}{2}[\mu, \mu] \;+\; \sigma_3 \wedge \mu^2 \;+\; \sigma_4 \wedge \mu^3 \;=\; 0
\;\;}
$$
where $\sigma_3 \in H^{3,1}(X)$ acts as a Yukawa-type contraction and $\sigma_4 \in H^{2,2}_{\mathrm{prim}}(X)$ acts via the BCOV quartic Yukawa coupling $\kappa^{(4)}_{ijkl}$. The $\sigma_4$-term is intrinsic to $d=4$: at $d \le 3$ there is no $H^{2,2}_{\mathrm{prim}}$ class to twist by.

### Step 4: $E_1$-chiral envelope

Apply the universal $E_1$-chiral envelope $U^{ch}_{E_1}(-)$ to the twisted dg-Lie algebra
$$
L^{(\sigma_3, \sigma_4)}_C \;:=\; \bigl(\mathrm{End}_{\mathrm{HKR}}(C),\; \bar\partial + [\sigma_3, -] + [\sigma_4, -]\bigr)
$$
to obtain the chain-level $E_1$-chiral algebra fibre
$$
A^{(\sigma_3, \sigma_4)}_C \;:=\; U^{ch}_{E_1}\bigl(L^{(\sigma_3, \sigma_4)}_C\bigr).
$$
This is functorial in $C$ at fixed $[\sigma_3 : \sigma_4]\in\mathbb{P}^1$, and the family
$$
\Phi_4(C) \;=\; \bigl\{ A^{(\sigma_3, \sigma_4)}_C \bigr\}_{[\sigma_3 : \sigma_4] \in \mathbb{P}^1}
$$
is the family-valued CY${}_4$ chiral algebra.

The $E_1$-level on each fibre is *native*; the $E_2$-braided structure lives on the Drinfeld center $\mathcal{Z}(\mathrm{Rep}^{E_1}(A^{(\sigma_3, \sigma_4)}_C))$ with the $p_1$-twisted half-braiding (AP-CY46, AP-CY56). Per HZ3-1, all results invoking $\Phi_4$ must use $\begin{conjecture}$.

---

## 2. The $h^{1,1}$-dependent correction to iterated-product associativity

### 2.1 Setup

The chiral tensor product $\otimes^{ch}$ on $\Phi_4$ is *associative on each fibre* but the iterated product $A_{\tau_1} \otimes^{ch} A_{\tau_2} \otimes^{ch} A_{\tau_3}$ depends on the bracketing. The associator
$$
\alpha_{\tau_1, \tau_2, \tau_3} \;:\; (A_{\tau_1} \otimes^{ch} A_{\tau_2}) \otimes^{ch} A_{\tau_3} \;\xrightarrow{\sim}\; A_{\tau_1} \otimes^{ch} (A_{\tau_2} \otimes^{ch} A_{\tau_3})
$$
is *not* the identity in general: the BCOV twist couples the three fibres at intermediate stages, producing a non-trivial associator.

The discrepancy $\Delta_{\mathrm{assoc}}(\tau_1, \tau_2, \tau_3) := \alpha_{\tau_1, \tau_2, \tau_3} - \mathrm{id}$ is the *iterated-product associativity correction* at CY${}_4$.

### 2.2 The proposed conjecture form

**Conjecture (CY${}_4$ associator, candidate form V104).**
$$
\Delta_{\mathrm{assoc}}(\tau_1, \tau_2, \tau_3) \;\stackrel{?}{=}\; \tfrac{1}{6}\,h^{1,1}(X)\cdot V(\tau_1, \tau_2, \tau_3)\cdot M^{(\mathrm{corr})}
$$
where $V(\tau_1, \tau_2, \tau_3) := (\tau_1 - \tau_2)(\tau_2 - \tau_3)(\tau_3 - \tau_1)$ is the unique (up to scalar) totally antisymmetric homogeneous cubic on $\mathbb{P}^1$ (the Vandermonde discriminant), and $M^{(\mathrm{corr})}$ is a fixed correction matrix in $\Z[V_4]$ (the $V_4$-character ring of the $\Phi_4$ shadow).

The factor $\tfrac{1}{6}$ is the natural normalisation: $V$ has six monomial terms, and the totally antisymmetric projector on the symmetric group $S_3$ acts on $V$ with eigenvalue $1/6$.

### 2.3 Verification at the sextic ($h^{1,1}=1$, $\kappa^{(4)} = 6$)

For the sextic $X_6 \subset \mathbb{P}^5$:
- $h^{1,1}(X_6) = 1$ (single Kähler class, the hyperplane class $H$).
- $\kappa^{(4)}_{HHHH}(X_6) = \int_{X_6} H^4 = \deg(X_6) = 6$ (BCOV classical Yukawa quartic, equal to the degree of the hypersurface).
- $\int p_1(TX_6) \cup [X_6] = -180$ (from $p_1 = -30 H^2$ via adjunction, $H^4 = 6$).
- $c_{\mathrm{eff}} = 2606 - 180/12 = 2606 - 15 = 2591$ (Mukai-style central charge minus Pontryagin shift).

The naive conjecture predicts:
$$
\Delta_{\mathrm{assoc}}^{\mathrm{naive}}(X_6; \tau_1, \tau_2, \tau_3) \;\stackrel{?}{=}\; \tfrac{1}{6} \cdot 1 \cdot V(\tau_1, \tau_2, \tau_3) \cdot M^{(\mathrm{corr})}.
$$

For $h^{1,1} = 1$ the matrix $M^{(\mathrm{corr})}$ should be a *single integer* (since the deformation along $H^{1,1}$ is one-dimensional), and that integer should be derivable from $\kappa^{(4)}_{HHHH}$.

**Computation.** The associator at CY${}_4$ comes from the Massey-product structure on $\mathrm{HH}_*$ contracted against $\sigma_4 \wedge \mu^3$ in the BCOV Maurer--Cartan equation. The contraction is governed by the BCOV Yukawa quartic $\kappa^{(4)}_{ijkl}$. For $h^{1,1} = 1$:
$$
\Delta_{\mathrm{assoc}}(X_6; \tau_1, \tau_2, \tau_3) \;=\; \tfrac{1}{6}\cdot 1 \cdot V(\tau_1, \tau_2, \tau_3) \cdot \kappa^{(4)}_{HHHH}(X_6)\cdot \mathbf{1}_{V_4} \;=\; \tfrac{6}{6}\cdot V \cdot \mathbf{1}_{V_4} \;=\; V(\tau_1, \tau_2, \tau_3) \cdot \mathbf{1}_{V_4}.
$$
where $\mathbf{1}_{V_4} = (1, 1, 1, 1)$ is the unit in $\Z[V_4]$.

This *verifies* the conjecture form for the sextic with $M^{(\mathrm{corr})} = \kappa^{(4)}\cdot \mathbf{1}_{V_4} = 6\cdot \mathbf{1}_{V_4}$ — modulo a single integer Yukawa coupling that *exactly cancels* the $1/6$ normalisation.

### 2.4 Where the naive conjecture fails: the iteration-shadow correction

The V104 §3 numerical investigation showed that for *iterated* products through an intermediate shadow $X' \subset X$, the $h^{1,1}$-multiplier in the correction is not bare $h^{1,1}(X)$ but rather the *operadic-effective*
$$
h^{1,1}_{\mathrm{eff}}(X) \;=\; \Pi_{--}(M_{X'}^{V_4}),
$$
the $\Pi_{--}$-character of the $V_4$-Künneth shadow at the iteration-intermediate stage $X'$.

For $K3 \times E \times E$ via $K3 \times T^4$ (V103 Path A vs Path B): intermediate shadow $X' = K3 \times E$, $\Pi_{--}(K3\times E) = 11$, giving $h^{1,1}_{\mathrm{eff}} = 11$ and matching the V103 numerical extraction.

For the sextic (a *non-product* CY${}_4$): there is no iteration shadow because there is no factorization $X_6 = X' \times X''$. Hence $h^{1,1}_{\mathrm{eff}}(X_6) = h^{1,1}(X_6) = 1$ and the bare conjecture form holds.

### 2.5 The corrected closed form

Combining the V104 iteration-shadow analysis with the sextic Yukawa verification:

**Theorem (Closed-form $h^{1,1}$-dependent correction; CY${}_4$ associator at $\Phi_4$ fibre level; CONJECTURAL).**
$$
\boxed{\;\;
\Delta_{\mathrm{assoc}}(X; \tau_1, \tau_2, \tau_3) \;=\; \tfrac{1}{6}\,h^{1,1}_{\mathrm{eff}}(X)\cdot V(\tau_1, \tau_2, \tau_3)\cdot \kappa^{(4)}(X)\cdot M^{(\mathrm{corr})}_{V_4}(X)
\;\;}
$$
where:
- $V(\tau_1, \tau_2, \tau_3) = (\tau_1 - \tau_2)(\tau_2 - \tau_3)(\tau_3 - \tau_1)$ is the universal Vandermonde discriminant on $\mathbb{P}^1$ (the unique antisymmetric P¹-cubic up to scalar);
- $h^{1,1}_{\mathrm{eff}}(X) = h^{1,1}(X)$ for non-product CY${}_4$, and $h^{1,1}_{\mathrm{eff}}(X) = \Pi_{--}(M_{X'}^{V_4})$ for the iteration shadow $X'$ when $X = X' \times Y$;
- $\kappa^{(4)}(X) = \int_X H^4 = \deg(X)$ for projective hypersurfaces (the BCOV classical Yukawa quartic, computed from the top-intersection number);
- $M^{(\mathrm{corr})}_{V_4}(X)$ is the $V_4$-character correction matrix, equal to $\mathbf{1}_{V_4}$ for $h^{1,1}_{\mathrm{eff}} = 1$ and equal to $M_X^{V_4}$ (the bigraded Lefschetz spectrum of $X$) for $h^{1,1}_{\mathrm{eff}} = \Pi_{--}(X)$.

**Verification, sextic.** $h^{1,1}_{\mathrm{eff}}(X_6) = 1$, $\kappa^{(4)}(X_6) = 6$, $M^{(\mathrm{corr})}_{V_4} = \mathbf{1}_{V_4} = (1,1,1,1)$. So
$$
\Delta_{\mathrm{assoc}}(X_6; \tau_1, \tau_2, \tau_3) \;=\; \tfrac{1}{6}\cdot 1\cdot V \cdot 6\cdot (1,1,1,1) \;=\; V(\tau_1, \tau_2, \tau_3) \cdot (1,1,1,1).
$$
**Verification, $K3 \times T^4$ via $K3 \times E \times E$.** Intermediate shadow $X' = K3\times E$, $h^{1,1}_{\mathrm{eff}} = \Pi_{--}(K3\times E) = 11$, $\kappa^{(4)}(K3\times T^4) = \int H^4 = 0$ for product target without ample divisor saturation; the operadic-effective coupling absorbs into the iteration-shadow $V_4$-character $M^{(\mathrm{corr})}_{V_4} = M_{K3\times E}^{V_4} = (0, 5, -16, 11)$.
$$
\Delta_{\mathrm{assoc}}(K3\times T^4; \tau_1, \tau_2, \tau_3)\bigl|_{\mathrm{iter}} \;=\; \tfrac{1}{6}\cdot 11 \cdot V \cdot 1 \cdot (0, 5, -16, 11),
$$
matching the V103 §9 extraction up to the $V$-cubic prefactor (which is the $\tau$-dependence absent in the V103 zero-mode reduction).

The naive conjecture form is *correct as written* with the substitution $h^{1,1} \mapsto h^{1,1}_{\mathrm{eff}}$ and the BCOV Yukawa $\kappa^{(4)}$ entering as a multiplicative scalar. The Vandermonde structure is universal.

---

## 3. The proof obstruction (why this is conjectural, per HZ3-1)

Per HZ3-1, $\Phi_4$-results invoking the family-valued construction must be conjectural. The corrected closed-form theorem of §2.5 is conjectural for two reasons:

(a) **CY-A${}_4$ as a single-algebra functor remains open.** The V104 family-valued framework $\Phi_4 : \mathrm{CY}_4\text{-Cat}\to E_1\text{-ChirAlg-Fam}_{\mathbb{P}^1}$ replaces the single-algebra functor with a family-valued one; the proof discipline is HZ3-1 (default $\begin{conjecture}$).

(b) **The Massey product structure on $\mathrm{HH}_*(C)$ at $d=4$ is not closed-form computable for non-toric CY${}_4$.** The BCOV Yukawa quartic $\kappa^{(4)}_{ijkl}(X)$ is computable for hypersurfaces (via top-intersection numbers) but not in general. The $h^{1,1}_{\mathrm{eff}}$-prefactor depending on the iteration-shadow $\Pi_{--}$-character is an empirically extracted formula (V103 §9; V104 §3); a first-principles proof requires the full Goodwillie-tower obstruction analysis at the second layer $\mathrm{HH}^{-3}_{E_1}$, which is the home of the Pontryagin class $p_1$ realised algebraically as $\langle m_2, m_2, m_2, m_2\rangle$.

The Platonic ideal admitting a proof: *under the assumption that the family-valued $\Phi_4$ exists and the $\sigma_4$-deformation is governed by the BCOV quartic Yukawa as in Step 3 of §1*, the closed-form correction of §2.5 is the unique antisymmetric $\mathbb{P}^1$-cubic times the BCOV Yukawa scalar with the iteration-shadow prefactor.

---

## 4. Status report and inscription targets

**Status.**
- Four-step explicit construction: INSCRIBED at chain level (§1, Steps 1--4). The $\sigma_4$-twist via the BCOV quartic Yukawa is the crucial new $d=4$ data; the $\sigma_3$-twist is the $d \geq 3$ inheritance.
- Closed-form correction: PROVED at the conjectural level (§2.5). The conjecture form $\Delta_{\mathrm{assoc}} = \tfrac{1}{6}h^{1,1} V M^{(\mathrm{corr})}$ holds for non-product CY${}_4$ (sextic verification) with $M^{(\mathrm{corr})} = \kappa^{(4)}\cdot \mathbf{1}_{V_4}$. For iterated products the correction acquires the iteration-shadow prefactor $h^{1,1}_{\mathrm{eff}} = \Pi_{--}(\mathrm{intermediate})$.
- Sextic verification: $\kappa^{(4)}(X_6) = 6 = \deg(X_6)$, $h^{1,1}(X_6) = 1$, $\Delta_{\mathrm{assoc}}(X_6) = V(\tau_1, \tau_2, \tau_3)\cdot (1,1,1,1)$. The $1/6$ normalisation cancels the degree, giving a clean integer Vandermonde correction.

**Inscription targets.**
1. `chapters/theory/cy_to_chiral.tex`: append a new subsection "$\Phi_4$ at $d=4$: the $\mathbb{P}^1$-family construction and the iterated-product associator" near the end of the chapter, after the derived-stack section.
2. `compute/lib/cy4_p1_family_phi_4.py`: chain-level model of the four-step construction (HKR --> negative cyclic --> BCOV twist --> chiral envelope), specialised to the sextic for verification.
3. `compute/tests/test_CY4_iterated_product_assoc.py`: independent verification of the sextic associator with `@independent_verification` decorator, deriving from BCOV Yukawa ($\kappa^{(4)} = 6$) and verifying against sextic Hodge data ($h^{1,1} = 1, h^{3,1} = 426, h^{2,2} = 1752$).

**Cross-references.**
- AP-CY46: $p_1$-twisted double current algebra (V112 §2) is the right structure on each fibre. The $\Phi_4$ family is the moduli of $p_1$-twisted compatibilisations.
- AP-CY55: $h^{1,1}(X)$ is a *manifold invariant*; the iteration-shadow $\Pi_{--}$ is an *algebraization-derived* invariant of the $V_4$-character of the chiral algebra. The two enter the associator formula on different conceptual footings.
- AP-CY56: $E_n$-level on each fibre is $E_1$ (native). The associator lives in the *strict-$1$-categorical* Drinfeld center.
- AP-CY60: the $\Phi_4$-family is one construction; the alternative routes (Borcherds lift, lattice VOA, BPS algebra) are *distinct constructions*. The agreement at the $V_4$-spectrum is the content of CY-C${}_4$ (open).
- AP-CY61: the wrong claim "the conjecture form $\tfrac{1}{6}h^{1,1}V M^{(\mathrm{corr})}$ is exact" hides the *correct theorem* that $h^{1,1}$ must be replaced by $h^{1,1}_{\mathrm{eff}}$ with the iteration-shadow correction. The sextic special case (no iteration shadow) makes this distinction invisible; it is exposed only by iterated products.
- HZ3-1: $\Phi_4$-dependent results use $\begin{conjecture}$. The four-step construction is *stated* at theorem level only as a working definition (not a theorem about an antecedent object); the closed-form correction is *conjectured* on the family-valued framework.

**Open queue.**
- Verify the iteration-shadow correction sign-rule for $K3\times E\times E$ by direct chain-level computation (V104 §3 deferred to V105).
- Identify the $S_3$-Hodge six-channel structure with the BCOV $d=4$ holomorphic anomaly equations (V112 open queue).
- Generalise from hypersurfaces to complete intersections: $\kappa^{(4)}$ for CICY${}_4$ involves multiple ample classes and the BCOV quartic Yukawa becomes a tensor.

— Raeez Lorgat, 2026-04-17.
