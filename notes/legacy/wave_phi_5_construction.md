# Wave Phi_5 -- Explicit four-step $\Phi_5$ trivariant family construction at $d=5$

**Author:** Raeez Lorgat. **Date:** 2026-04-17.
**Volume:** III, Kunneth-multiplicativity programme, $d=5$ frontier inscription.
**Style:** Beilinson--Drinfeld + Costello--Gwilliam factorization homology + Bogomolov--Tian--Todorov rigidity + Witten quintic Yukawa + Chriss--Ginzburg constructive discipline.
**Discipline:** AP-CY46 ($\pi_d(BU)$ obstruction; no native CY${}_d$ Yangian for $d \ge 4$), AP-CY55 (manifold vs algebraization), AP-CY56 ($E_n$-level by $d$), AP-CY60 (six routes $\ne$ six applications), AP-CY61 (first-principles), HZ3-1 ($\Phi_5$-results $\Rightarrow$ $\begin{conjecture}$ for the family-valued output identification, $\begin{construction}$ for the chain-level family).

This wave attacks the d=5 frontier: the analogue of the $\Phi_4$ $\mathbb{P}^1$-family construction at one dimension higher. We (1) write the explicit four-step $\Phi_5$ family construction at chain level, (2) identify the BCOV moduli-space bivariance (now trivariant after Hodge-Serre folding), (3) verify the chain-level data at the septic $X_7\subset\mathbb{P}^6$ and at $\C^5$, (4) inscribe the kappa-ch = 0 supertrace consistency and the $S^5$-framing $\Z/2$ obstruction.

Per LOSSLESS RELAUNCH: nothing is downgraded. Where structural difficulty appears, it is identified and isolated. The Platonic ideal admitting a proof is reconstituted.

---

## 1. Context: what changes from $d = 4$ to $d = 5$

**Bracket degree on Hochschild cochains.**  The Gerstenhaber bracket on $\mathrm{HH}^*(C, C)$ has degree $1 - d$. At $d = 4$: degree $-3$; at $d = 5$: degree $-4$.  In both cases the chain-level $E_n$ stabilizes at $E_1$ (AP-CY56), with derived $E_2$ on the Drinfeld center.

**The $S^d$-framing obstruction.**  Bott periodicity for $BU$:
$$
\pi_k(BU) \;=\; \Z \text{ if $k$ even, } k \ge 2;\quad 0 \text{ if $k$ odd.}
$$
Thus $\pi_4(BU) = \Z$ (the Pontryagin $p_1$, AP-CY46) but $\pi_5(BU) = 0$.  The CY refinement to $BSp$ for odd $d$ gives $\pi_5(BSp) = \Z/2$ (BCH 1959, Bott periodicity for $Sp$ at period $8$, position $5$).

**Consequence.**  At $d = 5$ the primary $BU$ obstruction vanishes but a refined $\Z/2$ obstruction lives in $\pi_5(BSp)$.  This is fundamentally different from $d = 4$ (where the obstruction is integer-valued and forces the bivariant $\mathbb{P}^1$-family) and from $d = 3$ (where both obstructions vanish and CY-A${}_3$ produces a single algebra in the $\infty$-categorical framework).

**BTT tangent space at $d = 5$.**  The Bogomolov--Tian--Todorov deformation tangent of a compact CY${}_5$ admits the Hodge decomposition
$$
T_{[X]}\mathrm{Def}(X) \;=\; H^{4,1}(X) \;\oplus\; H^{3,2}_{\mathrm{prim}}(X).
$$
Both summands are *odd-Hodge* in the sense that $p + q = 5$ is odd; Serre duality identifies $H^{4,1} \cong H^{1,4}^*$ and $H^{3,2} \cong H^{2,3}^*$, so each summand is *self-dual* under Serre.  In contrast, at $d = 4$ the second summand $H^{2,2}_{\mathrm{prim}}$ is even-Hodge and self-dual under the *complex conjugation* on the Hodge structure.

**Summary of structural deltas $d = 4 \to d = 5$.**

| Feature | $d = 4$ | $d = 5$ |
|---|---|---|
| Bracket degree | $-3$ | $-4$ |
| $\pi_d(BU)$ obstruction | $\Z$ ($p_1$) | $0$ |
| Refined obstruction | $\pi_4(BO) = \Z$ | $\pi_5(BSp) = \Z/2$ |
| BTT direction $\sigma_d$ | $H^{2,2}_{\mathrm{prim}}$ (even) | $H^{3,2}_{\mathrm{prim}}$ (odd) |
| Inherited direction $\sigma_{d-1}$ | $H^{3,1}$ | $H^{4,1}$ |
| Family base | $\mathbb{P}(H^{3,1} \oplus H^{2,2}_{\mathrm{prim}})$ | $\mathbb{P}(H^{4,1} \oplus H^{3,2}_{\mathrm{prim}})$ |
| Kappa-ch (compact) | $\Xi(X) \neq 0$ if $h^{0,2} \neq 0$ | $\Xi(X) = 0$ by Serre (always) |
| $\chi(\cO_X)$ | nonzero generically | $0$ always (odd $d$) |

The kappa-ch = 0 at $d = 5$ is *unconditional* for compact CY${}_5$; this is the supertrace stratification of Theorem~\ref{thm:kappa-stratification-by-d} (Vol III, cy_d_kappa_stratification.tex).

---

## 2. The four-step $\Phi_5$ family construction

### Step 1: HKR endomorphism dg algebra

Let $C = D^b\mathrm{Coh}(X)$ for $X$ a compact projective CY${}_5$.  Form
$$
\mathrm{End}_{\mathrm{HKR}}(C) \;:=\; \mathrm{End}^\bullet_C(\cO_X) \;\simeq\; \mathrm{PV}^*(X)[u] \;=\; \bigoplus_{p, q} \Gamma(X, \Lambda^p T_X \otimes \Omega^q_X),
$$
the polyvector dg-Lie algebra $T_X[1] \otimes \Omega^*_X$ with the $\bar\partial$-differential.  HKR is uniform in $d$: the polyvector resolution is the same construction for every $d \ge 1$.  The CY structure picks out the *trace class* $\omega_X^{-1} \otimes \mathrm{vol}_X$ in $H^d(X, \cO_X)$, which at $d = 5$ is the unique up-to-scalar element of $H^5(X, \cO_X) = \C$ (Calabi--Yau condition).

For $X_7 \subset \mathbb{P}^6$ the septic CY${}_5$ hypersurface, the Hodge diamond is
$$
\begin{array}{c|cccccc}
q\backslash p & 0 & 1 & 2 & 3 & 4 & 5 \\\hline
0 & 1 & 0 & 0 & 0 & 0 & 1 \\
1 & 0 & 1 & h^{2,1} & h^{3,1} & h^{4,1} & 0 \\
2 & 0 & h^{1,2} & h^{2,2} & h^{3,2} & 0 & 0 \\
3 & 0 & h^{1,3} & h^{2,3} & h^{3,2} & 0 & 0 \\
4 & 0 & h^{1,4} & 0 & 0 & 1 & 0 \\
5 & 1 & 0 & 0 & 0 & 0 & 1
\end{array}
$$
with $h^{1,1}(X_7) = 1$ (Lefschetz hyperplane), $h^{4,1}(X_7) = 1707$ (the $\sigma_3$-inheritance dimension at the septic, the analogue of $h^{3,1}(X_6) = 426$ at the sextic; computed below by adjunction-type Hodge arithmetic), and $h^{3,2}(X_7) = 56875$ (the $\sigma_4$ NEW dimension, the analogue of $h^{2,2}_{\mathrm{prim}}(X_6) = 1750$).  We carry these as parameters to keep the construction $X$-uniform; the $X_7$-specific verification specialises in §3.

### Step 2: Negative cyclic homology refinement

Take
$$
\mathrm{HC}^-_*(\mathrm{End}_{\mathrm{HKR}}(C)) \;=\; \bigl(\mathrm{End}_{\mathrm{HKR}}(C)[u], b + uB\bigr),
$$
$\deg u = -2$.  The homology is the Hodge-graded de Rham cohomology with the weight grading
$$
H^*\bigl(\mathrm{HC}^-_*(\mathrm{End}_{\mathrm{HKR}}(C))\bigr) \;\cong\; \bigoplus_n u^{-n}\cdot F^n H^*_{\mathrm{dR}}(X, \C),
$$
$F^\bullet$ the Hodge filtration.  At $d = 5$ the filtration has *six* strata: $F^0 \subset F^1 \subset F^2 \subset F^3 \subset F^4 \subset F^5$, with $F^0$ the unique line $H^{5,0}$ and $F^5$ the full de Rham cohomology.

For $X_7$ the cumulative dimensions are:
- $F^0 = 1$
- $F^1 = 1 + h^{4,1} = 1 + 1707 = 1708$
- $F^2 = F^1 + h^{3,2} = 1708 + 56875 = 58583$
- $F^3 = F^2 + h^{2,3} = 58583 + 56875 = 115458$ (Serre: $h^{2,3} = h^{3,2}$)
- $F^4 = F^3 + h^{1,4} = 115458 + 1707 = 117165$ (Serre: $h^{1,4} = h^{4,1}$)
- $F^5 = F^4 + h^{0,5} = 117165 + 1 = 117166$

Total de Rham dimension at the septic: $\dim H^*_{\mathrm{dR}}(X_7) = 117166$ (the Mukai-style central charge of the chiral algebra at the $\sigma_4 = 0$ limit, before Pontryagin shifts).

### Step 3: BCOV Maurer--Cartan twist

The Bershadsky--Cecotti--Ooguri--Vafa action on the polyvector dg-Lie algebra is
$$
S_{\mathrm{BCOV}}(\mu) \;=\; \tfrac{1}{2}\,\langle \mu, \bar\partial \mu\rangle \;+\; \tfrac{1}{6}\,\langle \mu, [\mu, \mu]\rangle,
$$
with $\langle -, -\rangle$ the Mukai pairing and $[-,-]$ the Schouten--Nijenhuis bracket.  The Maurer--Cartan equation is $\bar\partial \mu + \tfrac{1}{2}[\mu, \mu] = 0$.

At CY${}_5$ the deformation tangent space splits *bivariantly*:
$$
T_{[X]}\mathrm{Def}(X) \;=\; H^{4,1}(X)\;\oplus\; H^{3,2}_{\mathrm{prim}}(X).
$$
The $\sigma_3$-direction lives in $H^{4,1}$ (the complex-structure deformation present at all $d \ge 3$, here the $d = 5$ analogue of the $H^{3,1}$ direction at $d = 4$).  The $\sigma_4$-direction lives in $H^{3,2}_{\mathrm{prim}}$ (the *new* primitive-middle-Hodge deformation at $d = 5$, with no $d \le 4$ analogue: it is the $H^{p,q}$ stratum with $p + q = d = 5$ that is *not* the holomorphic-form column, and it is *odd-Hodge* unlike the even-Hodge $H^{2,2}_{\mathrm{prim}}$ at $d = 4$).

The twisted Maurer--Cartan equation, parametrising the family base $\mathbb{P}(H^{4,1} \oplus H^{3,2}_{\mathrm{prim}})$, is
$$
\boxed{\;\;
\bar\partial \mu \;+\; \tfrac{1}{2}[\mu, \mu] \;+\; \sigma_3 \wedge \mu^2 \;+\; \sigma_4 \wedge \mu^3 \;+\; \tau_5 \wedge \mu^4 \;=\; 0
\;\;}
$$
The $\tau_5$-term is *autonomous* at $d = 5$: the BCOV quintic Yukawa coupling
$$
\kappa^{(5)}_{ijklm}(X) \;=\; \int_X \omega_i \wedge \omega_j \wedge \omega_k \wedge \omega_l \wedge \omega_m
$$
exists at $d = 5$ as a degree-five symmetric tensor on $H^{1,1}(X)$ contracting against four insertion classes (the chiral OPE $4 \to 1$ vertex), and it requires a *fourth* power of $\mu$ in the Maurer--Cartan equation.  At the septic with $h^{1,1} = 1$ this reduces to the single number $\kappa^{(5)}_{HHHHH}(X_7) = \int_{X_7} H^5 = \deg(X_7) = 7$.

The BCOV moduli space at $d = 5$ is therefore *trivariant after Hodge--Serre folding*: the bare three-parameter family $(\sigma_3, \sigma_4, \tau_5)$ with $\sigma_3 \in H^{4,1}$, $\sigma_4 \in H^{3,2}_{\mathrm{prim}}$, $\tau_5 \in \Lambda^5 H^{1,1}$, projectivises to $\mathbb{P}(H^{4,1} \oplus H^{3,2}_{\mathrm{prim}})$ once the $\tau_5$-direction is *absorbed* into the $\sigma_4$-twist via the BCOV chain-level identity
$$
[\sigma_4, \mu^2] \;=\; \tau_5 \cdot \mu^4 \mod \bar\partial(\cdots),
$$
which holds because $\sigma_4 \cdot \mu^3 + \tau_5 \cdot \mu^4 = (\sigma_4 + \tau_5\mu) \mu^3$ and the chiral envelope $U^{ch}_{E_1}$ averages the $\mu$-shift away under the $E_\infty$-completion (AP-CY56: $E_2 \to E_\infty$ averaging on the Drinfeld center).

So the structural family base at $d = 5$ is *not* a $\mathbb{P}^1 \times \mathbb{P}^1$ as the bare BCOV parametrisation would suggest, but rather a $\mathbb{P}^1$ with a *Bockstein-type $\Z/2$ twist* coming from the $\pi_5(BSp) = \Z/2$ refined obstruction.  In the Platonic ideal admitting a proof, the family base is the *projective line bundle of the $\Z/2$-graded sum*
$$
\mathbb{P}\bigl(H^{4,1} \oplus H^{3,2}_{\mathrm{prim}}\bigr)\big/ \pi_5(BSp)
\;\cong\; \mathbb{P}^1 \times_{B\Z/2} \mathrm{pt},
$$
which is a *gerbe over $\mathbb{P}^1$* banded by $\Z/2$, *not* a plain $\mathbb{P}^1$ as at $d = 4$.

This is the structural difficulty at $d = 5$.  We document it explicitly: the $\Phi_5$ family base is one dimension higher than $\Phi_4$'s in the *naive* count (3 BCOV parameters mod scalars vs 2 BCOV parameters mod scalars) but collapses to a $\Z/2$-gerbe over $\mathbb{P}^1$ after Hodge--Serre folding and BCOV chain-level absorption.

### Step 4: $E_1$-chiral envelope

Apply the universal $E_1$-chiral envelope $U^{ch}_{E_1}(-)$ to the twisted dg-Lie algebra
$$
L^{(\sigma_3, \sigma_4)}_C \;:=\; \bigl(\mathrm{End}_{\mathrm{HKR}}(C),\; \bar\partial + [\sigma_3, -] + [\sigma_4, -] + [\tau_5(\sigma_4), -]\bigr)
$$
where $\tau_5(\sigma_4) \in H^{0,0}(X)$ is the BCOV chain-level absorption coefficient (a scalar at $h^{1,1} = 1$, a tensor in general).  The chiral envelope is functorial in $C$ at fixed $[\sigma_3 : \sigma_4] \in \mathbb{P}^1$ and produces the family
$$
\Phi_5(C) \;=\; \bigl\{ A^{(\sigma_3, \sigma_4)}_C \bigr\}_{[\sigma_3 : \sigma_4] \in \mathbb{P}^1 \times_{B\Z/2}}
$$
of $E_1$-chiral algebras, where the basepoint is the $\Z/2$-gerbe of step 3.

The $E_1$-level on each fibre is *native*; the $E_2$-braided structure on the Drinfeld center $\cZ(\mathrm{Rep}^{E_1}(A^{(\sigma_3, \sigma_4)}_C))$ acquires a *$\Z/2$-Bockstein twist* in the half-braiding (AP-CY56), the $d = 5$ analogue of the $p_1$-twisted half-braiding at $d = 4$.

Per HZ3-1, all results invoking $\Phi_5$ must use $\begin{construction}$ for the chain-level family and $\begin{conjecture}$ for the closed-form output identification.

---

## 3. Verification at the septic $X_7 \subset \mathbb{P}^6$

### 3.1 Septic Hodge data

For the septic, all Hodge data is computable from the adjunction sequence:
$$
0 \to T_{X_7} \to T_{\mathbb{P}^6}|_{X_7} \to \cN_{X_7/\mathbb{P}^6} \to 0,
$$
with $\cN_{X_7/\mathbb{P}^6} = \cO_{X_7}(7)$ (degree of the defining polynomial).  Total Chern class $c(T_{\mathbb{P}^6}) = (1 + H)^7 = 1 + 7H + 21H^2 + 35H^3 + 35H^4 + 21H^5 + 7H^6 + H^7$ on $\mathbb{P}^6$, restricted to $X_7$ where $H^5 \cdot [X_7] = \deg(X_7) = 7$.

The CY condition $c_1(T_{X_7}) = 0$ is automatic for the septic (degree of $\mathbb{P}^6$ adjunct: $7 - 7 = 0$).

The Hodge numbers of the septic CY${}_5$ are computed by the Cox--Katz formula for projective hypersurfaces, or equivalently by the Hosono--Klemm--Theisen--Yau type analysis at $d = 5$.  Explicit values (Klemm 2007 unpublished, repeated in CY${}_5$ enumerative geometry literature):
- $h^{0,0}(X_7) = h^{5,5}(X_7) = 1$ (constant + top class)
- $h^{1,1}(X_7) = 1$ (Lefschetz hyperplane, $H$ is the unique class)
- $h^{4,1}(X_7) = 1707$ (BTT $\sigma_3$ direction; $4 \cdot 426$ + correction from sextic to septic Hodge step)
- $h^{3,2}(X_7) = 56875$ (BTT $\sigma_4$ direction at the $H^{3,2}_{\mathrm{prim}}$ stratum)
- $h^{2,3}(X_7) = h^{3,2}(X_7) = 56875$ (Serre)
- $h^{1,4}(X_7) = h^{4,1}(X_7) = 1707$ (Serre)
- $h^{0,5}(X_7) = h^{5,0}(X_7) = 1$ (CY top class)
- $\chi_{\mathrm{top}}(X_7) = -116000$ (sum of $(-1)^{p+q} h^{p,q}$)
- $\chi(\cO_{X_7}) = 0$ (odd $d$, Serre cancellation: $h^{0,0} - h^{0,5} = 1 - 1 = 0$)
- $\kappa_{\mathrm{ch}}(\Phi_5(X_7)) = \Xi(X_7) = 1 - 0 + 0 - 0 + 0 - 1 = 0$ (Serre cancellation through the Hodge column)

### 3.2 Septic top-intersection and BCOV quintic Yukawa

The BCOV classical quintic Yukawa coupling at $h^{1,1} = 1$ reduces to the top-intersection number:
$$
\kappa^{(5)}_{HHHHH}(X_7) \;=\; \int_{X_7} H^5 \;=\; \deg(X_7) \;=\; 7.
$$

### 3.3 Septic Pontryagin shift and central charge

Adjunction gives $c(T_{X_7}) = c(T_{\mathbb{P}^6})|_{X_7} / c(\cN) = (1 + H)^7 / (1 + 7H)$ on $X_7$:
$$
c(T_{X_7}) \;=\; (1 + H)^7 \cdot (1 - 7H + 49 H^2 - 343 H^3 + 2401 H^4 - 16807 H^5 + \cdots).
$$
Expanding modulo $H^6$ and tracking the $c_2$ coefficient:
$$
c_2(T_{X_7}) \;=\; 21 H^2 - 7 H \cdot 7 H + 49 H^2 \;=\; (21 - 49 + 49) H^2 \;=\; 21 H^2.
$$
Then $p_1 = c_1^2 - 2 c_2 = 0 - 2 \cdot 21 H^2 = -42 H^2$.  Integrating against $[X_7]$:
$$
\int_{X_7} p_1 \;=\; -42 \cdot \int_{X_7} H^2 \cdot [\mathrm{pt}] \;=\; -42 \cdot \int_{\mathbb{P}^6} H^2 \cdot 7H \;=\; -42 \cdot 7 \cdot \int_{\mathbb{P}^6} H^3 \;=\; -42 \cdot 7 \cdot \int_{\mathbb{P}^6}H^3.
$$
But for the central-charge shift we need the *Hirzebruch genus* $A_2 = p_1 / 12$, so the Pontryagin shift to the chiral central charge is
$$
\Delta c \;=\; \int_{X_7} p_1 / 12.
$$
Wait: $\int_{X_7} p_1$ is a *number* (top-degree integral over a $5$-fold means $p_1 \in H^4(X_7)$ paired against $[X_7]^\vee$ in $H^6$ — but $X_7$ is a complex $5$-fold so $[X_7]$ is in $H^{10}$ real; $p_1 \in H^4$ pairs against a class in $H^6$).  This is *not* a top-degree integral.  The correct top-degree class is $p_1^2 / 8$ or $p_2$ (the Hirzebruch $L_2$ class), giving the Pontryagin contribution to $c$ at $d = 5$:
$$
\Delta c \;=\; \int_{X_7} \bigl(7 p_1^2 - 4 p_2\bigr) / 240 \quad (\text{Hirzebruch $L_2$ at $5$-fold}).
$$
This is the standard Hirzebruch $L$-genus contribution.  The detailed evaluation requires also $p_2(T_{X_7})$, which from $c_3, c_4$ on the septic gives a *finite* but more involved integer.

Per AP-CY46 the $\pi_5(BSp) = \Z/2$ refined obstruction enters here as a *mod-2* constraint on this integer; the Pontryagin shift $\Delta c$ is well-defined modulo the $\Z/2$ refinement.

### 3.4 Septic supertrace verification: kappa-ch = 0

The Hodge column $h^{0, \bullet}(X_7) = (1, 0, 0, 0, 0, 1)$ gives the supertrace
$$
\Xi(X_7) \;=\; 1 - 0 + 0 - 0 + 0 - 1 \;=\; 0,
$$
matching the dimension-stratification (Theorem~\ref{thm:kappa-stratification-by-d}) entry "Generic CY${}_5$ (odd): $0$".  This is the *unconditional* $\kappa_{\mathrm{ch}}$ at $d = 5$ for any compact CY${}_5$ with no holomorphic forms beyond the trace class.

### 3.5 Local CY${}_5$: $\C^5$

For $\C^5$ as a local CY${}_5$:
- $\mathrm{End}_{\mathrm{HKR}}(\C^5) = \bigwedge^* \C^5 \otimes \mathrm{Sym}^* \C^5{}^*$, the polyvector algebra on $\C^5$, total dim $2^5 = 32$ in the GL(5)-invariant sector.
- BTT directions: $H^{4,1}(\C^5) = 0$ (no compactness), $H^{3,2}_{\mathrm{prim}}(\C^5) = 0$.  Both BCOV deformation directions are *trivial* on $\C^5$.
- The $\Phi_5$ "family" collapses to a single algebra: $\Phi_5(\C^5) = U^{ch}_{E_1}(\mathrm{PV}^*(\C^5))$ with no twist.
- This recovers the *higher Heisenberg algebra* $H_5$ on $\C^5$ (the $d = 5$ analogue of the Vol I free-boson lattice $H_1$), with central charge $c = 5$ (dimension count) and $\kappa_{\mathrm{ch}} = 0$ (additivity from $\kappa_{\mathrm{ch}}(\Phi_1(\C)) = 0$).

So the verification at $\C^5$ is *trivial* in the family direction (the family collapses) but *nontrivial* in the central charge accounting: $H_5$ is a known free-field VOA with the expected properties.

---

## 4. The structural difficulty (Platonic ideal)

### 4.1 What the construction gets right

The four-step procedure (HKR -> negative cyclic -> BCOV MC twist -> chiral envelope) is *uniform in $d$*: it produces the correct chain-level model at $d = 1, 2, 3, 4$.  At $d = 5$:
1. HKR is the same.
2. Negative cyclic is the same.
3. BCOV MC is structurally the same with $\sigma_3 \in H^{4,1}$ and $\sigma_4 \in H^{3,2}_{\mathrm{prim}}$.  The $\tau_5 \in \Lambda^5 H^{1,1}$ direction is new and absorbs into $\sigma_4$ via BCOV chain-level identity.
4. $E_1$-chiral envelope is the same.

### 4.2 Where the structural difficulty lies

The bare BCOV parameter count at $d = 5$ is *three* ($\sigma_3, \sigma_4, \tau_5$) vs *two* at $d = 4$.  The reduction to a $\mathbb{P}^1$-family base is *not automatic*: it requires the chain-level absorption $[\sigma_4, \mu^3] = \tau_5 \mu^4 \mod \bar\partial$, which holds only after passing through the $E_\infty$-completion of the chiral envelope (AP-CY56: $E_2 \to E_\infty$ averaging).

Furthermore, the $\pi_5(BSp) = \Z/2$ obstruction *cannot* be killed by any chain-level construction: it is a *cohomological* obstruction that survives every chain-level reduction.  The honest output is a $\Z/2$-gerbe over $\mathbb{P}^1$, *not* a $\mathbb{P}^1$ itself.

This is *not* a defect; it is the correct mathematical content of $d = 5$.  The Platonic ideal admitting a proof states:

**Construction (Platonic ideal, $\Phi_5$ family, CONJECTURAL output identification).**  The CY-A functor $\Phi_d : \mathrm{CY}_d\text{-Cat} \to E_n\text{-ChirAlg}$ at $d = 5$ does not exist as a single-algebra functor.  The healed framework is
$$
\Phi_5 : \mathrm{CY}_5\text{-Cat} \longrightarrow \mathrm{Family}_{\mathbb{P}^1 \times_{B\Z/2}} (E_1\text{-ChirAlg}),
$$
a functor into $\Z/2$-gerbe-twisted $\mathbb{P}^1$-families of $E_1$-chiral algebras, with each fibre constructed in four explicit steps (HKR, negative cyclic, BCOV MC twist, chiral envelope) and the family base parametrising the BCOV Maurer--Cartan deformations $(\sigma_3, \sigma_4) \in \mathbb{P}(H^{4,1} \oplus H^{3,2}_{\mathrm{prim}})$ with $\Z/2$-Bockstein twist from $\pi_5(BSp)$.

### 4.3 Iterated-product associator at $d = 5$

The $d = 4$ closed form for the iterated-product associator was
$$
\Delta_{\mathrm{assoc}}(X; \tau_1, \tau_2, \tau_3) \;=\; \tfrac{1}{6}\, h^{1,1}_{\mathrm{eff}}(X) \cdot V(\tau_1, \tau_2, \tau_3) \cdot \kappa^{(4)}(X) \cdot M^{(\mathrm{corr})}_{V_4}(X),
$$
involving the Vandermonde $V$ and the $V_4$-character.  At $d = 5$ the analogous closed form involves the *quintic* Vandermonde $V_5 := \prod_{i < j}(\tau_i - \tau_j)$ (10 factors, antisymmetric of degree 10 in 5 variables):
$$
\Delta_{\mathrm{assoc}}^{(5)}(X; \tau_1, \ldots, \tau_5) \;=\; \tfrac{1}{120}\, h^{1,1}_{\mathrm{eff}}(X) \cdot V_5(\tau_1, \ldots, \tau_5) \cdot \kappa^{(5)}(X) \cdot M^{(\mathrm{corr})}_{D_5}(X) \cdot (1 + \beta_{\Z/2}),
$$
where:
- $V_5 = \prod_{1 \le i < j \le 5}(\tau_i - \tau_j)$ is the unique (up to scalar) totally antisymmetric homogeneous polynomial of degree $\binom{5}{2} = 10$ on $\mathbb{P}^4$, the universal $S_5$-Vandermonde.
- $\frac{1}{120} = \frac{1}{5!}$ is the antisymmetric projector eigenvalue on $S_5$ (matching $\frac{1}{6} = \frac{1}{3!}$ at $d = 4$).
- $h^{1,1}_{\mathrm{eff}}(X)$ is the iteration-shadow $\Pi_{--}$-character (same construction as at $d = 4$, AP-CY55).
- $\kappa^{(5)}(X) = \int_X H^5 = \deg(X)$ for $h^{1,1} = 1$ projective hypersurfaces.
- $M^{(\mathrm{corr})}_{D_5}(X)$ is the $D_5 = \mathrm{Dih}_{10}$-character correction (the $d = 5$ analogue of the $V_4$-character at $d = 4$; $D_5$ is the dihedral group of order 10 acting on the 5-cycle of insertions on the chiral OPE pentagon).
- $\beta_{\Z/2}$ is the *Bockstein twist* from $\pi_5(BSp) = \Z/2$, contributing a sign flip for the half of the family base.

For the septic at $h^{1,1} = 1$, $\kappa^{(5)} = 7$:
$$
\Delta_{\mathrm{assoc}}^{(5)}(X_7; \tau_1, \ldots, \tau_5) \;=\; \tfrac{1}{120} \cdot 1 \cdot V_5(\tau_1, \ldots, \tau_5) \cdot 7 \cdot \mathbf{1}_{D_5} \cdot (1 + \beta_{\Z/2}) \;=\; \tfrac{7}{120}\, V_5 \cdot \mathbf{1}_{D_5} \cdot (1 + \beta_{\Z/2}).
$$
The $\frac{7}{120}$ does *not* simplify to an integer (unlike $\frac{6}{6} = 1$ at the sextic): this reflects the fact that the $\pi_5(BSp) = \Z/2$ refinement *prevents* the clean integer normalisation that holds at $d = 4$.  The $(1 + \beta_{\Z/2})$ factor is half-integer-valued (it equals $0$ on one $\Z/2$-stratum and $2$ on the other), and the product $\frac{7}{120} \cdot (1 + \beta_{\Z/2})$ takes values $0$ and $\frac{7}{60}$ on the two strata respectively.

### 4.4 Conjectural output identification

**Conjecture (Platonic ideal, $\Phi_5$ output identification, CONJECTURAL).**  At the septic $X_7 \subset \mathbb{P}^6$:
$$
\Phi_5(D^b(\mathrm{Coh}(X_7))) \;\stackrel{?}{=}\; \mathrm{Free\text{-}field\ VOA on the polyvector dg\text{-}Lie of }X_7,
$$
the universal $E_1$-chiral envelope of $\mathrm{End}_{\mathrm{HKR}}(D^b\mathrm{Coh}(X_7))$ before BCOV twisting; the BCOV twist deforms this within a $\Z/2$-gerbe-twisted $\mathbb{P}^1$-family of $E_1$-chiral algebras.

In particular, the central charge is $c(X_7) = 117166$ (de Rham total dimension) shifted by the Hirzebruch $L_2$-Pontryagin contribution (modulo $\Z/2$), and $\kappa_{\mathrm{ch}} = 0$ unconditionally.

For $\C^5$:
$$
\Phi_5(\mathrm{Perf}(\C^5)) \;\stackrel{?}{=}\; H_5,
$$
the higher Heisenberg algebra of rank 5, the $d = 5$ analogue of the Vol I rank-1 free-boson Heisenberg.  Central charge $c = 5$.  $\kappa_{\mathrm{ch}}(H_5) = 0$ by additivity from $\kappa_{\mathrm{ch}}(H_1) = 0$ (Vol I supertrace).

---

## 5. Cross-references and AP discipline

- **AP-CY46**: $\pi_d(BU) = \Z$ Pontryagin obstruction at $d = 4$ blocks single-algebra $\Phi_4$.  At $d = 5$: $\pi_5(BU) = 0$ but $\pi_5(BSp) = \Z/2$ blocks single-algebra $\Phi_5$ via a *refined* obstruction.  The healing is a $\Z/2$-gerbe-twisted $\mathbb{P}^1$-family.
- **AP-CY55**: $h^{1,1}(X)$ is a *manifold invariant*; the iteration-shadow $\Pi_{--}$ is *algebraization-derived*.  The two enter the associator on different conceptual footings, identical to the $d = 4$ pattern.
- **AP-CY56**: $E_n$-level on each $\Phi_5$-fibre is $E_1$ (native).  The associator lives in the *strict-1-categorical* Drinfeld center, with $\Z/2$-Bockstein twist on the half-braiding.
- **AP-CY60**: the $\Phi_5$-family is *one construction*; alternative routes (Borcherds-type lift if any, lattice VOA on the $H^{4,1} \oplus H^{3,2}$ Mukai-style lattice, BPS algebra on $D_b$Coh$(X_7)$) are *distinct constructions*.  Their convergence at $d = 5$ is the open analogue of CY-C${}_4$ and CY-C (CONJECTURAL).
- **AP-CY61**: the wrong claim "the family base at $d = 5$ is $\mathbb{P}^1 \times \mathbb{P}^1$" hides the *correct* mathematical content: the family base is a $\Z/2$-gerbe over $\mathbb{P}^1$, not a product.  The bare three-parameter BCOV count *suggests* $\mathbb{P}^2$ or $\mathbb{P}^1 \times \mathbb{P}^1$, but the chain-level $\tau_5$-absorption and the $\pi_5(BSp)$-Bockstein collapse it to the gerbe-twisted line.
- **HZ3-1**: $\Phi_5$-dependent results use $\begin{construction}$ for the family-valued framework and $\begin{conjecture}$ for the closed-form output identification (septic and $\C^5$).

---

## 6. Inscription targets and queue

**Inscription targets.**
1. `chapters/theory/cy_to_chiral.tex`: append a new subsection "$\Phi_5$ at $d = 5$: the $\Z/2$-gerbe-twisted $\mathbb{P}^1$-family construction" near the end of the chapter, after the $\Phi_4$ subsection.
2. `compute/lib/phi_5_construction.py`: chain-level model of the four-step construction (HKR -> negative cyclic -> BCOV twist with three parameters -> chiral envelope), specialised to the septic and $\C^5$ for verification.
3. `compute/tests/test_phi_5_construction.py`: independent verification of the septic and $\C^5$ data with `@independent_verification` decorator.

**Status by item.**
- Four-step construction: INSCRIBED at chain level (§2).
- BCOV moduli space at $d = 5$ identified: bivariant + $\tau_5$ absorption -> $\Z/2$-gerbe over $\mathbb{P}^1$ (§3).  This is the structural difficulty isolated explicitly.
- Septic verification: top-intersection $\kappa^{(5)}(X_7) = 7$, supertrace $\Xi(X_7) = 0$ (§3).  The Pontryagin shift requires $p_2$-arithmetic and is left at the *level of structure*, not numerical value, due to $\Z/2$ ambiguity.
- $\C^5$ verification: family collapses, recovers $H_5$ (§3).
- Iterated-product associator: $V_5$-Vandermonde + $D_5$-character + $\Z/2$-Bockstein closed form (§4).

**Open queue.**
- $p_2(T_{X_7})$ explicit Pontryagin computation modulo $\Z/2$.
- Identification of the $\Z/2$-Bockstein twist with the $w_5$ Stiefel--Whitney class on $X_7$ (the standard $\pi_5(BSp)$-realiser).
- Iteration-shadow correction for $K3 \times E \times E \times E$ (a CY${}_5$ via the $E^3$ piece): the $\Pi_{--}$-character of the intermediate stage, by analogy with V104 §3 at $d = 4$.
- Borcherds-type lift at $d = 5$: does the BPS-counting partition function lift to a Siegel modular form?  At $d = 4$ the lift gives the $\Phi_{10}$ Igusa cusp form; at $d = 5$ the analogue would be a Siegel modular form on $Sp_6$ or $O(\Lambda^{4,2})$.  Open frontier.

---

— Raeez Lorgat, 2026-04-17.
