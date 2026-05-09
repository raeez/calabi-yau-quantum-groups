# ChatGPT Chiral Duality Master Critique — Reconstitution Consequence Map

**Date:** 2026-05-09
**Source:** `/Users/raeez/Desktop/ChatGPT - Chiral Duality Master Critique.pdf`
**Scope:** Cross-volume (Vol I, Vol II, Vol III, igusa-cusp-form, mixed-holomorphic-topological-strings)
**Purpose:** Exhaustive ledger of consequences — large and small — for reconstituting the chiral-duality programme to be free of the seventeen unlicensed identifications named in the critique.

**Companion (supersedes parts of this map):** `notes/chatgpt_critique_consequence_map_adversarial_review.md` (2026-05-09). Deep first-principles attack on this document. Key corrections: (i) Phase 2's "Vol I `lattice_foundations.tex:5866` cross-volume contradiction" is NOT a contradiction — Vol I's remark is consistent with Vol III; the real issue is HZ-7 subscript overload on bare $\kappa_{\mathrm{ch}}$. (ii) Phase 1's preface-paragraph insertion is wrong architecture; the right move is theorem-statement scope rewrite. (iii) "Shadow = object" master pattern is too narrow; the deeper master pattern is **scope omission** along three orthogonal axes (level / chart / ambient). (iv) The two arrow chains FUSE at level 2 (Stage-2 chiral output = boundary algebra). (v) The five manuscripts are five FACES of one story, not five separate chains. (vi) AP-CY-Crit-N numbering scheme is wrong; integrate into existing type-organized AP-CY catalogue. The deep review installs the **three-axis (level, chart, ambient) scope discipline** and the **chain fusion conjecture** as the inner form. Read both documents together; Phase 0 (master architecture document at `~/ecosystem/UNIVERSAL_ARROW.md`) from the deep review is the new highest-leverage move.
**Bookkeeping discipline:** This document is `notes/`-bookkeeping; nothing here belongs in reader-facing manuscript prose. Specific repairs land in `chapters/`, `frame/`, `examples/`, `theory/`, `connections/`, `bibliography/`, `appendices/`. Manuscript prose follows the Chriss–Ginzburg voice (no AP-CY vocabulary, no wave/round/strand language).

---

## 0. The master pattern recognized

The critique's deepest finding is one pattern with seventeen instantiations:

> **shadow = object**: a place where a chart, trace, partition function, bar construction, scalar Borcherds form, positive half, Banach completion, formal-local model, or comparison map is treated as if it equalled the structural object it shadows.

The Beilinson move is **not** to delete the vision; it is to delete the false equal signs. Every shadow in the programme is real and useful. The error is asserting it as the whole structure before the connecting hypothesis (chart datum, descent, doubling, completion, endpoint admissibility, source recognition) is constructed.

### 0.1 The corrected reconstitution arrow

Two parallel arrow chains organise the entire programme. Once they are in place, every claim must declare which node of which chain it lives at.

**Open/closed chain (Vol I, Vol II, mixed-HT-strings):**
$$
\text{open factorization category on }(X,D,\tau) \;\rightsquigarrow\; A_b = \mathrm{End}_{\mathcal{C}}(b) \;\rightsquigarrow\; B(A_b) \;\rightsquigarrow\; Z^{\mathrm{der}}_{\mathrm{ch}}(A_b) \;\rightsquigarrow\; \text{line / scalar trace}
$$
- **Primitive:** the open factorization dg-category on the tangential log curve $(X, D, \tau)$ together with the closed-colour input $(\mathcal C^{\mathrm{op}}, \Theta_{\mathcal C}, \mathrm{Tr}_{\mathcal C})$.
- **Chart:** $A_b = \mathrm{End}_{\mathcal C}(b)$ for a chosen boundary vacuum $b$. $A_b$ is **not** primitive.
- **Twisting/coupling shadow:** $B(A_b)$. Bar/cobar is not the bulk; it is the universal twisting coalgebra and Koszul comparison datum.
- **Bulk:** $Z^{\mathrm{der}}_{\mathrm{ch}}(A_b) \simeq \mathrm{ChirHoch}^\bullet(A_b, A_b)$ — derived chiral centre, $E_2$ over the chosen $b$.
- **Scalar / modular trace:** the closed-shadow modular consequence after open-side $\text{trace} + \text{clutching}$. Modularity is a **property of the open category with closed-colour pairing**, not an adjective on $A_b$.

**Calabi–Yau / chiral chain (Vol III, igusa-cusp-form, mixed-HT-strings):**
$$
\mathrm{CY}_d\text{-cat}(X) \;\xrightarrow{\Phi^{\mathrm{FA}}_d}\; E_d\text{-}\mathrm{HolFA}(X) \;\xrightarrow{\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1},C}}\; \mathrm{ChirAlg}^{E_{n(d)}}(C) \;\rightsquigarrow\; Y^+(X) \;\rightsquigarrow\; G(X) = D(Y^+(X)) \;\rightsquigarrow\; \text{scalar Borcherds form}
$$
- **Primitive (CY-intrinsic):** the CY$_d$ category $\mathrm{Perf}(X)$ or $D^b\mathrm{Coh}(X)$ with the $d$-Calabi–Yau structure (cyclic $A_\infty$ pairing, PTVV $(2-d)$-shift symplectic, orientation).
- **Stage-1 native factorisation:** $\Phi^{\mathrm{FA}}_d(\mathcal C) \in E_d\text{-}\mathrm{HolFA}(X)$. Canonical up to GRT$_1(\mathbb Q)$-torsor by Kontsevich–Tamarkin formality + Costello–Gwilliam–Li holomorphic locality.
- **Stage-2 chiral specialisation:** $\Phi^{(\Sigma_{d-1},C)}_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1},C} \circ \Phi^{\mathrm{FA}}_d$. Specialisation, **not** inversion. A single CY$_d$ category admits a **family** of $E_1$-chiral shadows parametrised by $(\Sigma_{d-1}, C)$.
- **Positive half:** $Y^+(X) = H^\bullet_{\mathrm{eq}}(\mathcal M^+_{\mathrm{eff}}(X), \phi_W)$ — universal positive-geometry grammar. CoHA on the effective stable cone with vanishing-cycle sheaf.
- **Quantum vertex group:** $G(X) = D(Y^+(X))$ — Drinfeld double, only after Hall pairing, completion, integral form, stable-envelope transport, and descent are installed. **Not** present at $Y^+$.
- **Scalar Borcherds form:** $\Delta_5, \Phi_{10}, \Phi_{12}, \ldots$ — protected automorphic shadow whose Fourier coefficients $c_N(0)/2 = \kappa_{\mathrm{BKM}}$ index the Borcherds weight. **Not** the operator algebra; **not** a Hilbert space; **not** the gravitational path integral.

### 0.2 The promotion ladder

A statement is allowed to live at level $k$ only after the connecting hypotheses through level $k$ are established:

| Level | Object | Promotion condition for level $k+1$ |
|------:|---|---|
| 0 | Primitive open factorisation dg-category / CY$_d$-category | choose chart datum (boundary $b$ / Stage-2 $(\Sigma_{d-1},C)$) |
| 1 | Chart-dependent algebra: $A_b$ / $\Phi^{\mathrm{FA}}_d(\mathcal C)$ | apply Bar / specialise to curve |
| 2 | Twisting/coupling shadow: $B(A_b)$, Stage-2 chiral $\Phi^{(\Sigma,C)}_d(\mathcal C)$ | apply $Z^{\mathrm{der}}_{\mathrm{ch}}$ / Drinfeld double |
| 3 | Bulk/centre / quantum group: $Z^{\mathrm{der}}_{\mathrm{ch}}(A_b)$, $G(X) = D(Y^+(X))$ | extract trace / character / partition function |
| 4 | Scalar shadow: protected trace, Borcherds form, BKM weight | (terminus) |

Every claim in the manuscripts must declare its level. Bare "$\Phi$ produces a chiral algebra" is a level-0-to-level-2 jump that skips the Stage-1/Stage-2 distinction. Bare "$\Delta_5$ is the BPS Hilbert space" is a level-4-to-level-3 jump that asserts the operator object from its scalar shadow. Both are forbidden until the connecting hypothesis is supplied.

---

## 1. Per-dismissal consequence ledger

Each entry below has the format:

- **Collapse**: the false equality
- **Healed statement**: the corrected (level-discipline) form
- **Status across the programme**: `[locked]` if the discipline is already inscribed; `[partial]` if some files have it, others don't; `[unaddressed]` if no current statement of the discipline; `[contradiction]` if two volumes inscribe conflicting forms.
- **High-impact loci**: specific file:line places that need work (representative, not exhaustive — the bulk is left to a sweep grep)
- **Architectural ripples**: structural consequences that propagate through the programme
- **Cross-volume propagation**: which inscriptions in one volume must be imported by another
- **Bookkeeping**: AP-CY catalogue entry, cache row, memory pointer (drafted in §3 and §4 below)

---

### Dismissal 1: "the boundary algebra is the primitive open object"

**Collapse:** $A = $ primitive open object.

**Healed:** The primitive open object is a **factorization dg-category on the log/real-oriented boundary** of a tangential log curve $(X, D, \tau)$ with closed-colour input $(\mathcal C^{\mathrm{op}}, \Theta_{\mathcal C}, \mathrm{Tr}_{\mathcal C})$. The boundary algebra $A_b = \mathrm{End}_{\mathcal C}(b)$ is the endomorphism algebra of a chosen boundary vacuum object $b$ — a **chart**, not the invariant. Everything that begins from $A$ must be marked "after choosing $b$".

**Status:** Vol I `[locked]` at primitive level (configuration_spaces.tex:2077 defines tangential log curve; chiral_center_theorem.tex:1889 develops the global theory on $(X,D,\tau)$; the open factorization category is the primitive). Vol II `[partial]` — the Swiss-cheese architecture in `factorization_swiss_cheese.tex` and `raviolo.tex` is correct, but the introduction-level framing often opens with $A$ (e.g., `modular_swiss_cheese_operad.tex` master theorem). Vol III `[partial]` — `cy_to_chiral.tex:2840-2856` correctly says "correspondence programme, not a single functor", but downstream chapters use $A_X$ as primitive without the chart marker.

**High-impact loci:**
- Vol I `chapters/theory/chiral_center_theorem.tex:1889-1925` — already correct primitive framing; should be referenced from Vol II/III prefaces.
- Vol I `chapters/theory/configuration_spaces.tex:2062-2544` — the canonical $(X,D,\tau)$ definition + open-closed convolution. Reference target.
- Vol II `chapters/theory/modular_swiss_cheese_operad.tex:4177` — "master theorem realizes 3D quantum gravity" needs reframing through "open factorization category → bulk-with-chart" (see also Dismissal 13).
- Vol III `chapters/theory/cy_to_chiral.tex` — every assertion of "$A_X$ is the BPS chiral algebra" must declare the chart datum $(\Sigma_2, C, b)$.

**Architectural ripples:**
- Every theorem statement of form "Theorem: $A$ has property $P$" must be reread as "Theorem: $A_b$ has property $P$, for a fixed chart $b$" or "Theorem: the primitive package $(\mathcal C, b, A_b, Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal C), \Theta_{\mathcal C}, \mathrm{Tr}_{\mathcal C})$ has property $P$".
- The morphism category requires care: morphisms of primitive packages include **change of chart** (boundary vacuum gauge transformation), and properties stable under this gauge are the genuinely chart-independent invariants.

**Cross-volume propagation:**
- Vol I → Vol II: the tangential log curve discipline of `configuration_spaces.tex:2062-2544` should anchor every Vol II Swiss-cheese statement.
- Vol I → Vol III: every CY-side $\Phi$-image must be paired with the open-side framing as dual carriers of the same factorisation data on $C$.

**Bookkeeping:** AP-CY-Crit-1 (drafted §3); cache row "primitive open object vs chart algebra" (drafted §4); memory pointer to the new architecture entry.

---

### Dismissal 2: "bar/cobar is the bulk"

**Collapse:** $\mathrm{ChiralBar}(A) = \text{bulk}$.

**Healed:** $\mathrm{Bar}(A) = $ universal twisting/coupling coalgebra (single-colour $E_1$-chiral dg coalgebra). Bulk = $Z^{\mathrm{der}}_{\mathrm{ch}}(A) \simeq \mathrm{ChirHoch}^\bullet(A, A)$. The Swiss-cheese open/closed structure governs the pair $(Z^{\mathrm{der}}_{\mathrm{ch}}(A), A)$; the bar complex carries twisting data, not bulk operators.

**Status:** `[locked]` at the formal level — Vol III `quantum_chiral_algebras.tex:1247` correctly states "$Z^{\mathrm{der}}_{\mathrm{ch}}(A) = C^\bullet_{\mathrm{ch}}(A, A) = \RHom(\Omega B(A), A)$ is the bulk algebra (Vol I Theorem H). This is the ``$E_2$ uplift'', not $A^!$." Vol III `cy_to_chiral.tex:7525` "$Z^{\mathrm{der}}_{\mathrm{ch}}(A)$ is the bulk derived centre". Vol II `bar-cobar-review.tex:482` uses "ChiralBar as classifying space" — correct (twisting). Most "is the bulk" instances across the corpus are **of the centre**, not of the bar — they are correctly disciplined.

**Residual collapse risk:** Vol I `chapters/theory/en_koszul_duality.tex:8306` "topological $E_3$-algebra structure. This $E_3$ object is the bulk" — must verify this $E_3$ object is the centre, not the bar. Vol II `chapters/theory/foundations_recast_draft.tex:613` "the bulk-to-boundary coupling" is correct phrasing. Sweep `grep -n "Bar(A) is the bulk\|ChiralBar(A) = bulk\|bar.*\\\\to.*bulk"` after every batch edit.

**Architectural ripples:**
- The slogan "the bulk is the bar" must be retired wherever it appears. Replace with "the bulk is the derived chiral centre; the bar is the universal twisting coalgebra".
- Koszul duality framings: $A \mapsto B(A) \mapsto \Omega B(A) \mapsto A$ must be presented as a **comparison map** ($A \xleftarrow{\sim} \Omega B(A)$ when Koszul) rather than as identifying the bar as the bulk. The bulk is on a different side of the duality.

**Cross-volume propagation:**
- Vol II → Vol III: the bar-vs-centre split is most cleanly established in Vol II `bar-cobar-review.tex` and `hochschild.tex`. Vol III's invocations of $Z^{\mathrm{der}}_{\mathrm{ch}}$ should all cite Vol II's Theorem H (not Vol III's own restatement).
- Vol I → Vol II: Vol I's modular Koszul formulation of bar must be marked "bar = twisting; centre = bulk" at every cross-reference.

**Bookkeeping:** AP-CY-Crit-2 (drafted §3); cache row "bar = twisting, centre = bulk" (drafted §4).

---

### Dismissal 3: "$2d$ chiral $\rightsquigarrow 3d$ HT because there is an $E_1$-bar direction"

**Collapse:** the explanation of the $2d \rightsquigarrow 3d$ promotion is the existence of an extra interval direction modeled by $E_1$-bar.

**Healed:** the real mechanism is the **chiral Deligne–Tamarkin / Swiss-cheese principle**: the boundary $A_\infty$-chiral object lifts to a one-dimension-up acting object $Z^{\mathrm{der}}_{\mathrm{ch}}(A)$ via the Swiss-cheese open-to-closed promotion. The bar direction is a **computational model** for this in special cases, not the fundamental explanation.

**Status:** `[partial]`. Vol II has the Deligne–Tamarkin/Swiss-cheese architecture (`chiral_higher_deligne.tex`, `factorization_swiss_cheese.tex`, `raviolo.tex`) but introductory chapters frame the $2d \to 3d$ jump in bar-direction language.

**High-impact loci:**
- Vol II `chapters/theory/chiral_higher_deligne.tex` — verify the dimensional uplift is presented as Deligne–Tamarkin, not as bar-direction in its prose.
- Vol II `chapters/theory/introduction.tex:106, 113, 793, 909, 2081, 2084` — the "Universal Holography ⇒ 3d gravity" framing must thread through the Swiss-cheese promotion, not via "the bar gives the extra direction".
- Vol I `chapters/theory/e1_modular_koszul.tex` — the modular open-closed convolution is the right lens; cross-link from Vol II.

**Architectural ripples:**
- The $E_1$-to-$E_2$ centre passage is the **Lurie additivity theorem $E_1 \otimes_{\mathrm{Dunn}} E_1 = E_2$** applied to the Swiss-cheese pair. Bar appears as a tool inside this passage, not as the explanation.
- Boundary models (e.g., the bar-direction interval) survive as constructive computations — keep them, but rename them as "computational realisations" not "structural explanations".

**Cross-volume propagation:**
- Vol I's modular open-closed convolution → Vol II's chiral higher Deligne → Vol III's two-stage Φ_d Stage-2 specialisation. Three formulations of one mechanism; cross-link explicitly.

**Bookkeeping:** AP-CY-Crit-3 (drafted §3); cache row "Swiss-cheese promotion vs bar-direction explanation" (drafted §4).

---

### Dismissal 4: "there is a global open sector on a plain algebraic curve"

**Collapse:** an open sector lives on a bare curve $X$.

**Healed:** the open sector lives on the **real-oriented blowup / log boundary** of a tangential log curve $(X, D, \tau)$ with $D$ a divisor of punctures and $\tau$ tangential data — never on $X$ itself.

**Status:** Vol I `[locked]` — `configuration_spaces.tex:2062-2544` defines the tangential log curve; `chiral_center_theorem.tex:1889` develops the global theory on $(X,D,\tau)$; `e1_modular_koszul.tex` uses the $(X,D,\tau)$ primitive throughout. Vol II `[partial]` — Swiss-cheese sections use the discipline; some connection chapters reference "the curve $C$" without the log/tangential decoration. Vol III `[partial]` — the chiral shadow on the curve $C$ in $\Phi_d^{(\Sigma,C)}$ is implicitly $(C, D, \tau)$ when punctures from CY data are present, but this is not always made explicit.

**High-impact loci:**
- Vol II — sweep `grep -nE "open sector|open colour|open color" chapters/`. Wherever an open sector lives on an undecorated curve, add the $(X, D, \tau)$ qualifier.
- Vol III `chapters/theory/cy_to_chiral.tex` — the curve $C$ in $\Phi^{(\Sigma_2, C)}_3$ should be made tangential-log $(C, D_C, \tau_C)$ when the CY data carries marked points (e.g., conifold singularities, McKay $\mathbb C^3 / \Gamma$ orbifold points, K3 fibre punctures over the elliptic base).

**Architectural ripples:**
- "Boundary," "trace," "open category," "clutching" must always have a geometric carrier. Without $(X,D,\tau)$, these symbols float.
- The full primitive package becomes $(X, D, \tau; \mathcal C^{\mathrm{op}}, b, A_b, Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal C), \Theta_{\mathcal C}, \mathrm{Tr}_{\mathcal C})$.

**Cross-volume propagation:**
- Vol I `configuration_spaces.tex:2062-2544` is the canonical reference; all five manuscripts should cite this.

**Bookkeeping:** AP-CY-Crit-4 (drafted §3).

---

### Dismissal 5: "modularity is a property of the closed algebra"

**Collapse:** "the closed chiral algebra is modular" — modularity treated as an adjective on the closed algebra.

**Healed:** modularity is **trace + clutching on the open category**. The closed shadow has modular consequences via this open-side data, but the closed algebra alone is not the carrier of modularity. Say: "the open category carries a cyclic trace compatible with clutching; its closed shadow has modular consequences." That is the difference between a slogan and a modular functor.

**Status:** Vol I `[locked]` at the structural level — `configuration_spaces.tex:2865-2911` defines the open-closed modular convolution algebra; `e1_modular_koszul.tex:3618` puts the modular/chiral sector on the closed colour. Vol II `[partial]` — `axioms.tex:1470` correctly pairs "regularisation and the pairing of closed modular data with open"; `factorization_swiss_cheese.tex:2161, 2306` correctly says the closed input is the modular component, but recovery of the full modular structure requires the open-side trace. Vol III `[partial]` — many modularity claims on K3 chiral algebra etc. need the open-side clutching qualifier.

**High-impact loci:**
- Vol I → Vol II `axioms.tex` — the open-closed modular pairing axiom is the right form.
- Vol III `chapters/connections/modular_koszul_bridge.tex` — verify modularity statements thread through trace-and-clutching, not closed-algebra-property.

**Architectural ripples:**
- "Modular Koszul duality" as a phrase is correct — it is the open-side data pairing closed inputs. The duality lives on the open category, not on the closed algebra.
- $\mathrm{SL}_2(\mathbb Z)$ action, $S$-transformation, Verlinde formula — all are downstream consequences of the open-side modular functor structure, not direct closed-algebra properties.

**Cross-volume propagation:**
- Vol I's modular open-closed convolution definition → Vol II's universal holography → Vol III's modularity claims on K3 BKM etc.

**Bookkeeping:** AP-CY-Crit-5 (drafted §3); cache row "modularity = open-side trace + clutching" (drafted §4).

---

### Dismissal 6: "the five $\kappa$-numbers are one invariant"

**Collapse:** $\{0, 0, 3, 5, 24\}$ on $K3 \times E$ are reductions of one number; or the additive identity $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fiber}})$ holds.

**Healed:** the five $\kappa_\bullet$ on $K3 \times E$ — $(\kappa_{\mathrm{cat}} = 0, \kappa_{\mathrm{ch}}^{\mathrm{Hodge}} = 0, \kappa_{\mathrm{ch}}^{\mathrm{Heis}} = 3, \kappa_{\mathrm{BKM}}(\Delta_5) = 5, \kappa_{\mathrm{fiber}} = 24)$ — come from **five distinct constructions**. They are not collapsible. The naive additive shift $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fiber}})$ fails at $N = 1$ (left = $5$, right = $0+0=0$); the universal identity is $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ (Borcherds weight theorem; Gritsenko 1999 Thm 6.1) evaluated at the chosen Siegel input denominator.

**Status:** `[contradiction]`.
- Vol III `[locked]`: `chapters/examples/cy_d_kappa_stratification.tex` Theorem `thm:borcherds-weight-kappa-BKM-universal` and `chapters/examples/k3e_bkm_chapter.tex:14340` correctly state "No additive shift of the form $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fibre}})$ relates 5 and 12; the identity $\kappa_{\mathrm{BKM}} = c_\Lambda(0)/2$ is evaluated at two different Siegel input denominators."
- Vol I `[VIOLATION]`: `chapters/examples/lattice_foundations.tex:5866` still asserts the naive additive form `$\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fibre}})$`. **This is the cross-volume contradiction the AP5 lock pending in the cache (row 65) was waiting to surface.**

**High-impact loci:**
- Vol I `chapters/examples/lattice_foundations.tex:5866` — **highest-priority repair**. Replace the additive formula with the universal Borcherds-weight identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$, and add the cross-reference to Vol III `cy_d_kappa_stratification.tex` Theorem `thm:borcherds-weight-kappa-BKM-universal`.
- Vol I cache (`appendices/`?) and AP catalogue — the Vol I-side equivalent of Vol III AP-CY68/AP234 must be added.
- Cross-volume κ-spectrum table: `chapters/examples/cy_d_kappa_stratification.tex` is the canonical site; all volumes' κ-references should funnel through it.

**Architectural ripples:**
- The four-κ discipline (CLAUDE.md "Essential constants" + memory entry `feedback_four_kappa_discipline.md`) becomes a **cross-volume invariant**, not a Vol III house rule.
- Bare $\kappa$ remains forbidden; subscript always.
- $\kappa_{\mathrm{BKM}}(\mathbf H_{\Delta_5})$ at two different conventions ($\Phi_{12}$ vs $\Delta_5^2 = \Phi_{10}$) gives values 12 and 5 respectively — every site must name the input denominator (Vol III cache row 65).

**Cross-volume propagation:**
- Vol III → Vol I: the universal identity inscription must propagate to Vol I `lattice_foundations.tex` and any other Vol I files that mention $\kappa_{\mathrm{BKM}}$.
- Vol III → Vol II: same cross-reference; Vol II's `chapters/connections/ht_bulk_boundary_line_core.tex:3127` "Gritsenko–Nikulin denominator is the bulk–boundary gauge-class target" is the right primitive site.
- Vol III → igusa-cusp-form: the Igusa programme produces $\Delta_5$ and its Borcherds weight $5$; the cross-reference to $\kappa_{\mathrm{BKM}}(\Delta_5) = 5$ should be explicit, with the universal identity cited.

**Bookkeeping:** AP-CY-Crit-6 (drafted §3, cross-volume); cache row "universal Borcherds weight, naive additive form falsified" (drafted §4 — already partially in Vol III cache row 64). Vol I cache entry with same content. Memory entry `project_kappa_additive_form_cross_volume_lock.md`.

---

### Dismissal 7: "a Calabi–Yau category directly produces a chiral algebra"

**Collapse:** $\Phi: \mathrm{CY}_d\text{-Cat} \to \mathrm{ChirAlg}$ is a one-stage functor.

**Healed:** $\Phi$ factors through Stage-1 native factorisation $\Phi^{\mathrm{FA}}_d$ landing in $E_d$-holomorphic factorisation algebras on $X$, and Stage-2 chiral specialisation $\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C}$ depending on the choice of a closed $(d-1)$-cycle and a reference curve. A single CY$_d$ category admits a **family** of $E_1$-chiral shadows parametrised by $(\Sigma_{d-1}, C)$.

**Status:** Vol III `[partial]`. The two-stage factorisation is `[locked]` in:
- `working_notes.tex` sec:two-stage-factorisation:467, sec:organising-framework:528, 549, 567, 618, 624-625, 629, 865, 1004, 2622, 2733
- `chapters/theory/cy_to_chiral.tex:2840` — "{$\Phi_d$}_{d≥1} is not a single functor; it is a $d$-indexed family of constructions"
- `chapters/theory/cy_to_chiral.tex:2856` — "correspondence programme, not a single functor"
- `chapters/frame/preface.tex` rem:phi-not-unified-functor (per cache row 76)
- Cache row 76 (AP273 recurrence) explicitly registers the Vol III preference for "correspondence programme / per-$d$ assignment".

**Residual collapses (`hochschild_calculus.tex:1570`, `quantum_groups_foundations.tex:6261` etc.):**
- `chapters/theory/hochschild_calculus.tex:1570` writes bare `$\Phi_3: \mathrm{CY}\text{-cat}_3 \to \mathrm{ChirAlg}^{E_1}$` without the two-stage qualifier. **Should be inscribed as $\Phi^{(\Sigma_2,C)}_3 = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_2, C} \circ \Phi^{\mathrm{FA}}_3$.**
- `chapters/theory/quantum_groups_foundations.tex:6261` — same bare form.
- `chapters/theory/introduction.tex:1664` — same bare form: `\colon \CY_d\text{-}\Cat \to E_n\text{-}\mathrm{ChirAlg}$` 
- `chapters/theory/cyclic_ainf.tex:247` — bare form.
- `chapters/theory/e2_chiral_algebras.tex:2912` — `$\Phi_2\colon D^b\mathrm{Coh}(K3) \to \mathrm{ChirAlg}^{E_2}(K3)$` — correct at $d=2$ (single-stage works); but should still cite the $(\Sigma_1, C)$ datum for clarity.
- `chapters/theory/phi_universal_trace_platonic.tex:494` — bare form.

**High-impact loci:**
- All bare `\Phi_d : \mathrm{CY}_d\text{-Cat} \to \mathrm{ChirAlg}` in Vol III must be annotated with the two-stage form or the explicit chart $(\Sigma_{d-1}, C)$.

**Architectural ripples:**
- The "six routes to $G(K3 \times E)$" become **six $(\Sigma_2, C)$-specialisations** of one $\Phi^{\mathrm{FA}}_3(D^b\mathrm{Coh}(K3 \times E))$, not six $\Phi_3$-applications. Per memory `project_two_stage_factorisation.md`. Already inscribed in working_notes Wave 12 synthesis.
- Stage-1 has its own functoriality (canonical up to GRT$_1(\mathbb Q)$-torsor) separate from Stage-2 functoriality (depends on chart datum).
- "$\Phi$ is a functor" is allowed only at $d \le 2$ on smooth proper locus, with the $E_n$-target explicit. At $d \ge 3$, "correspondence programme" is the maximal honest claim.

**Cross-volume propagation:**
- Vol III's two-stage discipline must be imported by:
  - Vol II `chapters/theory/chiral_higher_deligne.tex` — when discussing the dimensional uplift, cite the two-stage form.
  - Vol I when referencing the chiral shadow of CY data.
  - mixed-HT-strings `main.tex` — the Costello–Gwilliam locality is part of Stage-1; should be cross-cited.

**Bookkeeping:** AP-CY-Crit-7 (drafted §3); already partially in Vol III cache row 76 and AP-CY (Wave 12 inscriptions); strengthen to forbid bare-$\Phi_d$-as-functor in any new theorem statement.

---

### Dismissal 8: "the quantum group is already present as soon as the positive half is present"

**Collapse:** $Y^+(X) = G(X)$, or $\mathrm{CoHA}(\mathbb{C}^3) = \mathcal W_{1+\infty}$.

**Healed:**
- $Y^+(X) \neq G(X)$ until Hall pairing, completion, integral form, stable-envelope transport, and descent data are installed. $G(X) = D(Y^+(X))$ is the Drinfeld double, not the positive half.
- $\mathrm{CoHA}(\mathbb{C}^3) = Y^+(\widehat{\mathfrak{gl}}_1)$ (positive half of affine Yangian). $\mathcal W_{1+\infty}$ appears only after Drinfeld doubling, Fock evaluation, and vertex-operator construction. Per Vol III cache row 67 and Schiffmann–Vasserot.

**Status:** Vol III `[locked]`:
- Cache row 67 explicitly: "$\mathrm{CoHA}(\mathbb C^3) = Y^+(\widehat{\mathfrak{gl}}_1)$ — the positive half of the affine Yangian; $\mathcal W_{1+\infty}$ appears only after Drinfeld doubling and Fock/evaluation."
- Memory entry `reference_coha_evaluation_chain.md`: "CoHA($\mathbb C^3$) = $Y^+(\widehat{\mathfrak{gl}}_1)$ [assoc.] $\hookrightarrow$ $Y(\widehat{\mathfrak{gl}}_1)$ [Drinfeld double, Hopf] -ev_$\lambda$-> End($\mathcal W_{1+\infty}[\lambda]$-vac)".
- Vol I `chapters/examples/w_algebras.tex:7680`: "$\cW_{1+\infty}$ at $c=1$ appears only after the Drinfeld" — correct discipline.
- Vol I `chapters/connections/holographic_datum_master.tex:5470`: "$\cW_{1+\infty}$ at $c=1$ via the Drinfeld-centre passage" — correct.

**Residual collapses:**
- Vol I `chapters/connections/frontier_modular_holography_platonic.tex:5244, 5252, 5289, 5356, 5398, 5440, 5473, 5496, 5547, 5550, 5657` — many "$\cA_{\mathrm{M5}}(N) = W_{1+\infty}[\lambda = N]$" identifications. These need to be marked: this identification is only valid **after** the Drinfeld-centre passage and at the specified Fock evaluation $\lambda$, and the M5 algebra is the **image** of the Drinfeld double under evaluation, not the CoHA itself.
- Vol II `chapters/connections/log_ht_monodromy_frontier.tex:282-293` — "$B(W_{1+\infty}) = T^c(s^{-1}\overline{W_{1+\infty}})$" is fine (correct bar of $W$, after Drinfeld). But generation context needs the doubling chain explicit.

**Architectural ripples:**
- The CoHA evaluation chain becomes a **canonical reference**: every site that touches CoHA $\to$ vertex algebra must pass through (i) CoHA = $Y^+$ (positive half, $E_1$-associative); (ii) Drinfeld double $\to$ full Yangian (Hopf); (iii) Fock/evaluation $\to$ $\mathcal W_{1+\infty}[\lambda]$-vacuum endomorphisms (vertex algebra image).
- Each arrow has its own associativity/coassociativity class; they are not interchangeable.
- For compact non-toric CY$_3$ (e.g. K3 $\times$ E), even the positive half $Y^+(K3 \times E)$ requires construction (compact critical CoHA gates per cache rows 70, 80; AP-CY351–353, 452–453).

**Cross-volume propagation:**
- Vol III's CoHA evaluation chain → Vol I, Vol II.
- Cross-link `reference_coha_evaluation_chain.md` from every site asserting CoHA $\to W_{1+\infty}$ identification.
- igusa-cusp-form: the Hall–Borcherds story for $\mathbf{H}_{\Delta_5}$ must thread through "compact-CoHA gates → finite Hall windows → compact critical CoHA → Drinfeld double $\to$ Borcherds recognition of $\mathfrak g_{\Delta_5}$" — never collapsing source to target.

**Bookkeeping:** AP-CY-Crit-8 (drafted §3); cache rows 67, 70, 80, 81 already cover much of this; strengthen with explicit "$Y^+ \neq G$ before doubling" lock.

---

### Dismissal 9: "six-dimensional hCS is ordinary three-dimensional Chern–Simons in disguise"

**Collapse:** the 6d hCS algebra of observables is a recoded 3d Chern–Simons (with cubic Casimir as the obstruction).

**Healed:** at $d = 3$, 6d hCS supplies the **physical realization of $\Phi^{\mathrm{FA}}_3$** on verified formal/object-level loci. The one-loop obstruction is the **quartic** integral $\int_X \mathrm{Tr}_{\mathrm{ad}}(A(F_A)^3)$ (cohomological piece sourced by the cubic symmetric Casimir $d^{abc}$ — but as a quartic-in-fields obstruction, not a cubic-Casimir analogue of 3d CS). Ordinary 3d Chern–Simons knot theory is **not** the source.

**Status:** Vol III `[locked]`:
- `chapters/theory/quantum_chiral_algebras.tex:464`: "$A_{\mathrm{w.f.}}$ is scheme-dependent and absorbed by the Costello–Li propagator counter-term. The cohomological piece $A_{\mathrm{anom}}$ vanishes identically on the real-root subsystem"
- `chapters/theory/quantum_chiral_algebras.tex:3995`: "renormalisation framework. The prior cubic-Casimir statement confused..."
- `chapters/theory/cy_to_chiral.tex:1750`: "cohomological anomaly piece (cubic symmetric Casimir source)"
- `chapters/theory/phi_universal_trace_platonic.tex:1175-1194`: section "The one-loop anomaly: cubic vs. quadratic Casimir split"
- `chapters/frame/preface.tex:467`: "not cubic Casimir $d^{abc}$. The Bochner–Martinelli propagator…"
- Memory entries `project_anomaly_cubic_vs_quadratic_casimir.md`, `project_kappa_ch_bv_five_invariant_extension.md`.

**Architectural ripples:**
- The hCS quantisation route is the **physical realisation** of one canonical Stage-1 datum, not a separate competing object.
- The Costello–Gaiotto–Yagi non-abelian 5D hCS $\to$ Yangian VOA all-orders theorem (CLAUDE.md "Key facts") is the converging-perturbative-expansion route by Kontsevich–Tamarkin formality, not a series-asymptotic result.
- 3D Chern–Simons knot intuition cannot be imported directly into 6d hCS without passing through BV/hCS obstruction theory.

**Cross-volume propagation:**
- Vol III's anomaly-treatise → Vol I (where 3d CS is sometimes invoked as physical motivation) and Vol II (where mixed-HT-strings/hCS shows up in 5D and 6D forms).
- mixed-HT-strings `main.tex:3207-3266` — already correctly threads through "holomorphic de Rham obstruction" rather than 3d-CS-knot intuition.

**Bookkeeping:** AP-CY-Crit-9 (drafted §3); already locked by AP-CY262 in Vol III; reinforce in cross-volume index.

---

### Dismissal 10: "formal local HT string theory globalizes automatically"

**Collapse:** the formal Darboux model on $\mathbb R^2_{\mathrm{top}} \times \mathbb C^2_{\mathrm{hol}}$ implies a global compact target theory.

**Healed:** formal Darboux model + descent / QME / anomaly / locality package $\Rightarrow$ candidate compact theory. The Hamiltonian identification is **local**; on a general holomorphic symplectic surface one needs either local Hamiltonians or vanishing of the holomorphic de Rham obstruction.

**Status:** mixed-HT-strings `[locked]`:
- `main.tex:3207`: "the vanishing of the corresponding holomorphic de Rham obstruction"
- `main.tex:3232`: "The obstruction for a locally Hamiltonian symplectic vector field to come [from a globally Hamiltonian field…]"
- `main.tex:3266`: "For a locally Hamiltonian vector field, $\delta$ is the period class of [the obstruction class]…"

**Architectural ripples:**
- Every local theorem in mixed-HT-strings must declare its global obstruction (holomorphic de Rham class, anomaly cocycle, sewing obstruction).
- Cross-volume: when Vol II / Vol III invoke the mixed-HT-strings local model (e.g. as a UV-completion or as the source of $\Phi^{\mathrm{FA}}_d$ at toric loci), the global obstruction must be cited and either verified or marked open.

**Cross-volume propagation:**
- mixed-HT-strings $\to$ Vol III `chapters/theory/` and `chapters/examples/local_p2_*` — every local toric Hamiltonian-BF realisation must inherit the obstruction discipline.
- mixed-HT-strings $\to$ Vol II Universal Holography master theorem — local-to-global gap is not closed without descent.

**Bookkeeping:** AP-CY-Crit-10 (drafted §3); cache row "formal Darboux + descent vs global compact theory" (drafted §4).

---

### Dismissal 11: "the Igusa square root already gives a compact BPS Hilbert space"

**Collapse:** $\Delta_5$ = physical (compact BPS) Hilbert space.

**Healed:** $\Delta_5$ = Borcherds denominator / protected scalar shadow. The construction gives a virtual $K_0$-determinant package and a Borcherds denominator algebra; it does **not** by itself produce a microscopic compact Hilbert space, compact Hall correspondences, an orientation, or a BPS operator product. The missing problem is to construct the operator-level object whose protected Pfaffian is $\Delta_5$.

**Status:** igusa-cusp-form `[locked]`:
- `main.tex:96`: "It does not supply a compact BPS Hilbert space, compact Hall correspondences, an orientation, or a BPS operator product."
- `notes/reconstitution_plan_20260428.md:44`: "$\Delta_5^2$. It is a protected Pfaffian / primitive algebra whose…"
- `notes/swarm_20260430/reports/A270_cross_repo_source_target_firewall.md`: explicitly enforces source/target firewall.
- `notes/sixth_attack_heal_20260428/agent2_costello_witten_bv_anomaly.md`: explicit O2 obstruction discipline.

**Cross-volume risks:** Vol III and Vol II must inherit the disclaimer when they reference $\Delta_5$:
- Vol II must mention $\mathbf H_{\Delta_5}$ only as a Vol III recognition target or scalar shadow comparator (cache row 79, AP-CY450).
- Vol III's $\mathbf H_{\Delta_5}$ recognition (per `notes/sixth_attack_heal_20260428` and the Wave 14-19 ledger) must thread through the source/target firewall — the scalar Δ_5 does not by itself recognize the operator object.

**Architectural ripples:**
- The Igusa programme is positioned as a **terminal scalar shadow** in the reconstitution arrow. Its job is to be the protected modular form whose Borcherds weight equals $c_N(0)/2$; constructing the operator object is a separate research line.
- The compact BPS Hilbert space construction problem is named and open (it is a research target, not a current claim).

**Cross-volume propagation:**
- igusa-cusp-form `main.tex:96` disclaimer → must be cited at every Vol II/III invocation of $\Delta_5$.
- Three independent verification paths required for any operator-level claim about $\mathbf H_{\Delta_5}$ (cache row 75, AP-CY446).

**Bookkeeping:** AP-CY-Crit-11 (drafted §3); cache rows 71-82 already cover much of this; reinforce as a master gate.

---

### Dismissal 12: "the scalar partition function is the operator algebra"

**Collapse:** $Z_{\mathrm{BPS}}^{K3 \times E} = (\Phi_{10}^{\mathrm{un}})^{-1} = \Delta_5^{-2}$ is the 3d gravitational path integral / the operator algebra of $\mathbf H_{\Delta_5}$.

**Healed:** $Z_{\mathrm{BPS}}^{K3 \times E}$ is a **scalar shadow** — a protected automorphic shadow / Borcherds denominator. Its promotion to a gravity-line partition function still requires the Hall–Borcherds comparison residual. Promotion to the operator algebra requires the full Hall–Drinfeld–Pfaffian source recognition (cache rows 71-82).

**Status:** Vol II `[partial]` — the Hall–Borcherds comparison is set up, but the prose sometimes elides "scalar shadow $\rightsquigarrow$ operator algebra" by implication. Vol III `[partial]` — the OP/Igusa normalisation split is locked (cache row 71, AP-CY357), but the gravity-line interpretation is referenced informally.

**High-impact loci:**
- Vol II and Vol III — every site that writes "$Z_{\mathrm{BPS}}$ = (something)" must declare whether that "something" is a scalar form (level 4), an operator-algebra trace (level 3), or a path-integral interpretation (additional descent required).
- Vol II `chapters/theory/modular_swiss_cheese_operad.tex:4177` "master theorem realizes 3D quantum gravity" — should be reframed as "constructs the algebraic holographic HT sector whose boundary is Virasoro and whose bulk is $Z^{\mathrm{der}}_{\mathrm{ch}}$"; the gravitational path integral is **not** constructed (see Dismissal 13).

**Architectural ripples:**
- $Z_{\mathrm{BPS}}$ is at level 4 (scalar shadow); $\mathbf H_{\Delta_5}$ at level 3 (operator algebra); $\Phi^{\mathrm{FA}}_3(K3 \times E)$ at level 1 (Stage-1 native factorisation); $D^b\mathrm{Coh}(K3 \times E)$ at level 0. Crossing levels requires named hypotheses.
- The Hall–Borcherds comparison residual is the missing certificate; cache rows 71-82 enumerate the gates.

**Cross-volume propagation:**
- igusa-cusp-form's source/target firewall (`notes/swarm_20260430/reports/A270`) must be the operating discipline in Vol II and Vol III.

**Bookkeeping:** AP-CY-Crit-12 (drafted §3); cache rows 71-82 cover the gates; reinforce with master entry "scalar trace ≠ operator algebra".

---

### Dismissal 13: "Universal Holography constructs the dynamical metric path integral for 3d gravity"

**Collapse:** Vol II's Universal Holography master theorem constructs quantum gravity.

**Healed:** the master theorem identifies (boundary = $A$, bulk = $Z^{\mathrm{der}}_{\mathrm{ch}}(A)$, interaction = $\mathrm{SC}^{\mathrm{ch,top}}$-brace action). For $A = \mathrm{Vir}_c$, this is the **boundary-CFT / holographic reading of pure 3d gravity** — significant but not the dynamical-metric path integral. BTZ/Cardy physics still requires modular-invariance, vacuum-dominance, and saddle hypotheses.

**Status:** Vol II `[partial]`:
- The disclaimers exist somewhere in Vol II per the critique's own quotation, but the introductory framing in `chapters/theory/introduction.tex:106, 113, 793, 909, 2081, 2084, 2622, 2966, 2973, 3019` and `modular_swiss_cheese_operad.tex:4177` reads as "constructs 3D quantum gravity" without the qualifier.

**High-impact loci:**
- Vol II `chapters/theory/introduction.tex` — every "3d quantum gravity" framing must be replaced with "the algebraic holographic HT sector whose boundary is Virasoro and whose bulk is the derived chiral centre"; explicit disclaimer about non-construction of the dynamical-metric path integral.
- Vol II `chapters/theory/modular_swiss_cheese_operad.tex:4177` — "master theorem realizes 3D quantum gravity" must be softened to "constructs the holographic HT pair" with the saddle/modular-invariance/vacuum-dominance hypotheses named.
- Vol II `chapters/theory/chiral_higher_deligne.tex:972` "Universal Holography functor" — verify scope.

**Architectural ripples:**
- The master theorem becomes "I have identified the algebraic holographic HT sector" — not "I have constructed quantum gravity". This is what is significant; do not inflate.
- The relationship to BTZ Cardy formula etc. becomes: the master theorem provides the **algebraic substrate** in which BTZ saddles are computed, conditional on modular invariance + vacuum dominance.

**Cross-volume propagation:**
- Vol II → Vol I: the claim that Vol II "constructs 3d gravity from Vol I bar-cobar" must be reframed as "Vol II identifies the holographic HT sector built on Vol I's bar-cobar primitive".
- Vol II → Vol III: the M5/W-algebra references in Vol III's CY landscape inherit the same softening.

**Bookkeeping:** AP-CY-Crit-13 (drafted §3); new cache row "Universal Holography = HT sector identification, not gravitational path integral" (drafted §4). This is a **publication-strategy** consequence: claims about "constructing quantum gravity" need to be replaced with the more precise "constructing the holographic HT sector".

---

### Dismissal 14: "the $W_\infty / E_\infty$ endpoint is proved by finite spin checks"

**Collapse:** $W_\infty[\lambda] \Rightarrow E_\infty$ is a theorem outside admissible scope.

**Healed:** the $W_\infty[\lambda]$ endpoint is **conditional** on Prochazka triangular truncation, Creutzig–Kanade–Linshaw parafermion compatibility, Pope–Romans–Shen / Bakas input, and a Yamada weight-window condition. Spin-$\le 8$ numerical checks are **evidence**, not a replacement for the structural hypotheses.

**Status:** Vol II `[partial]` — the conditionality is acknowledged in places, but the abstracts and intros sometimes assert the endpoint without listing the hypotheses.

**High-impact loci:**
- Vol II — every "$W_\infty[\lambda] \Rightarrow E_\infty$" assertion must list the four hypotheses (Prochazka triangular truncation; CKL parafermion compatibility; PRS input; Yamada weight-window condition) as its admissibility scope.
- Spin-$\le 8$ checks are inscribed as "evidence in admissible window", not as proof of the endpoint outside that window.

**Architectural ripples:**
- The "endpoint admissibility" becomes a named gate, like the κ_BKM input denominator gate.
- $W_\infty[\lambda]$ as a two-parameter family is correct primitive; the $E_\infty$-promotion is the level-3-to-level-3' jump that needs the hypothesis package.

**Cross-volume propagation:**
- Vol II → Vol I: when Vol I cites the M5 algebra as $W_\infty[\lambda]$, the conditionality must be carried.
- Vol II → Vol III: same — Vol III's CY-side identifications via M5 must respect endpoint admissibility.

**Bookkeeping:** AP-CY-Crit-14 (drafted §3); cache row "endpoint admissibility hypotheses for $W_\infty[\lambda] \Rightarrow E_\infty$" (drafted §4).

---

### Dismissal 15: "class M works chain-level in ordinary complexes"

**Collapse:** class M chain-level in ordinary (non-completed) complexes.

**Healed:** class M is **chain-level false in ordinary complexes**. One needs analytic HS-sewing, coderived BV=bar comparison, or weight-completed / pro / $J$-adic ambients.

**Status:** Vol II `[locked]`:
- `chapters/theory/equivalence.tex:145`: "chain-level may fail in class M. The present rectification theorem"
- `chapters/theory/weight_completed_topologization_class_m_platonic.tex` — full rigorous proof in the WEIGHT-COMPLETED ambient.
- `chapters/theory/chiral_higher_deligne.tex:909-946`: "Universal holography at chain level for class M" with the WEIGHT-COMPLETED qualifier.
- `chapters/connections/modular_pva_quantization_core.tex:187`: "requires the HS-sewing criterion".
- `chapters/connections/thqg_3d_gravity_movements_vi_x.tex:916`: "HS-sewing!Virasoro" — index entry confirms HS-sewing is named.

**Architectural ripples:**
- The ambient-qualifier discipline (CLAUDE.md "Pattern 236") becomes a **publication-strategy** invariant. Every chain-level theorem must declare its ambient (ordinary / weight-completed / pro / $J$-adic / HS-sewing).
- Forcing class M into ordinary complexes is named **forbidden** — it feels like optimism but blocks progress.

**Cross-volume propagation:**
- Vol II → Vol I and Vol III: any cross-volume invocation of class M chain-level mathematics must inherit the ambient qualifier.
- Cross-link: Vol II's `weight_completed_topologization_class_m_platonic.tex` and `topologization_class_m_original_complex_platonic.tex` are the canonical references.

**Bookkeeping:** AP-CY-Crit-15 (drafted §3); cache row "class M chain-level requires completed ambient" (drafted §4).

---

### Dismissal 16: "PVA Jacobi gives the whole quantum theory"

**Collapse:** the $\lambda$-Jacobi identity for Poisson vertex algebras gives the all-loop quantum HT theory.

**Healed:** PVA Jacobi gives **classical gauge invariance** (Khan–Zeng); a Virasoro element upgrades the mixed HT theory to a topological one. The all-loop boundary vertex algebra, $E_3$-lift, and analytic renormalized closed-open package are **extra data**. Finite-type freely generated finite-jet PVA all-loop statements are conditional on the KZ analytic SDR package, Stokes choices, reflected weights, and lift of $T = [Q_{\mathrm{tot}}, G]$.

**Status:** Vol II `[partial]` — finite-type freely generated finite-jet PVA all-loop statements are marked conditional in places, but other statements treat PVA Jacobi as the quantum theorem.

**High-impact loci:**
- Vol II `chapters/connections/modular_pva_quantization*.tex` — verify each PVA-quantum claim lists the conditions (KZ SDR, Stokes, reflected weights, $T$-lift).
- Vol II all-loop boundary VOA results — must list the four-package conditions.

**Architectural ripples:**
- The classical-PVA-Jacobi → quantum-HT-theory promotion becomes a named four-step ladder (KZ analytic SDR; Stokes choices; reflected weights; $T$-lift).
- The mixed-HT to topological-HT step is gated by the Virasoro-element data (separate from PVA Jacobi).

**Cross-volume propagation:**
- Vol II → mixed-HT-strings: the PVA-classical/HT-quantum split must be respected when invoking PVA in HT calculations.

**Bookkeeping:** AP-CY-Crit-16 (drafted §3); cache row "PVA Jacobi = classical, quantum requires four-step package" (drafted §4).

---

### Dismissal 17: "quadratic chiral duality already gives full chiral Koszul duality"

**Collapse:** quadratic dual exists $\Rightarrow$ Koszul duality theorem.

**Healed:** Gui–Li–Zeng (arXiv:2212.11252) prove an **injection** $\mathrm{Hom}(A, B) \hookrightarrow \mathrm{MC}(A^! \otimes B)$ with bijectivity only in special cases; general results parallel to associative algebra require a theory of chiral Koszulness in a suitable homotopy setting. Quadratic dual exists $\Rightarrow$ candidate dual and MC comparison map. Koszulness is the **separate theorem**.

**Status:** `[partial]` — the chiral Koszul programme (Vol I) takes this seriously, but introduction-level statements sometimes elide the gap.

**High-impact loci:**
- Vol I `chapters/theory/ordered_associative_chiral_kd.tex`, `e1_modular_koszul.tex`, `koszulness_fourteen_characterizations.pdf` (and the `.tex` source) — every Koszul-duality theorem must declare whether it is the candidate-dual injection or the full Koszulness theorem.
- Vol I `modular_koszul_duality.pdf` (`.tex` source) — verify scope.

**Architectural ripples:**
- The fourteen Koszulness characterizations become a **menu** (each is a distinct strengthening); the candidate-dual injection is the weakest entry; full Koszulness is the strongest.
- Where the manuscripts assert Koszul duality without naming the characterisation, the assertion needs strengthening or scope-narrowing.

**Cross-volume propagation:**
- Vol I → Vol II and Vol III: cross-references to "the Koszul duality theorem" must specify which characterisation/level.

**Bookkeeping:** AP-CY-Crit-17 (drafted §3); cache row "quadratic dual ≠ Koszulness theorem" (drafted §4).

---

## 2. Cross-volume backbone reorganization

Beyond the per-dismissal punch list, the critique forces a cross-volume backbone reorganization. Three meta-architectures must be installed at the abstract / preface / introduction level of all five manuscripts.

### 2.1 The level-discipline preface insert

Each manuscript abstract or preface should open with a **levels paragraph** (see §0.2) that names the level of every primary structural object the volume claims. Suggested form:

> The objects of this work live at four levels: primitive (open factorization category / CY$_d$-category), chart (boundary algebra / Stage-1 native factorisation), shadow (bar / Stage-2 chiral specialisation / positive half), and bulk-or-scalar (derived chiral centre / quantum vertex group / Borcherds form). A claim's level is declared at every theorem statement; promotion across levels requires the named connecting hypothesis, and is not asserted as automatic.

This paragraph replaces ambiguous "Φ produces a chiral algebra" or "the derived centre is the bulk" framings with a uniform vocabulary that exposes the gap between levels.

### 2.2 The two-stage Φ as the Vol III backbone

Vol III's seven-part architecture (CLAUDE.md "Seven parts") gains an explicit Stage-1 / Stage-2 split:

- **Part II reframing:** "CY-to-chiral functor $\Phi$" becomes "CY-to-chiral programme: Stage-1 ($\Phi^{\mathrm{FA}}_d$) + Stage-2 (chart-dependent specialisation)". The functor name is reserved for $\Phi^{\mathrm{FA}}_d$ at Stage-1; the per-chart Stage-2 specialisation is the family $\{\Phi^{(\Sigma_{d-1}, C)}_d\}$.
- **Part III reframing:** the $E_n$ hierarchy is now visible as **two layers**: Stage-1 lives in $E_d$-HolFA on $X$, Stage-2 lands in $E_{n(d)}$-ChirAlg on $C$. The $n(d)$ depends on $d$ and on the Stage-2 reduction.
- **Part V reframing:** the K3 $\times$ E "six routes" become "six $(\Sigma_2, C)$-specialisations of $\Phi^{\mathrm{FA}}_3(D^b\mathrm{Coh}(K3 \times E))$" — six chart choices, one Stage-1 datum.
- **Part VI reframing:** the "seven faces of $r_{\mathrm{CY}}$" become "seven measurements of one Stage-1 datum, taken under different chart-and-evaluation choices".

### 2.3 The open factorisation primitive as the Vol I/II backbone

Vol I's modular Koszul package and Vol II's universal holography both rest on the open factorisation primitive $(X, D, \tau; \mathcal C^{\mathrm{op}}, b, A_b, Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal C), \Theta_{\mathcal C}, \mathrm{Tr}_{\mathcal C})$. The reorganization makes this primitive **explicit** at the abstract level of both volumes:

- **Vol I abstract:** primitive = open factorisation dg-category on $(X, D, \tau)$ with closed-colour input. Bar = twisting coalgebra on a chart. Centre = bulk on a chart.
- **Vol II abstract:** primitive identified, and the universal holography master theorem operates on the **pair** (boundary $A_b$, bulk $Z^{\mathrm{der}}_{\mathrm{ch}}(A_b)$) — not on $A_b$ alone, not on $\mathrm{Bar}(A_b)$ as bulk.

### 2.4 The Igusa programme as terminal scalar shadow

igusa-cusp-form is positioned as the **scalar terminus** of the chiral chain. Its abstract, intro, and main theorem all carry the disclaimer (already in `main.tex:96`) that it constructs a protected scalar / Borcherds denominator, **not** a Hilbert space, Hall pairing, orientation, or operator product. Cross-volume invocations of $\Delta_5$, $\Phi_{10}$, $\mathfrak g_{\Delta_5}$ all carry this disclaimer.

### 2.5 The mixed-HT-strings programme as local theorem with named obstruction

mixed-holomorphic-topological-strings is positioned as the **local theorem** (formal Darboux + descent + QME + anomaly + locality). Cross-volume invocations import the local theorem **and** its named global obstruction (holomorphic de Rham class), never asserting global identification without the obstruction discipline.

---

## 3. New AP-CY entries — drafted

The following entries should be appended to `notes/antipatterns_catalogue.md` in Vol III (and mirrored as cross-references in Vol I and Vol II AP catalogues). Numbered AP-CY-Crit-1 through AP-CY-Crit-17 to mark them as flowing from this critique.

### AP-CY-Crit-1 — boundary algebra ≠ primitive open object

**Wrong claim:** $A$ is the primitive open object.

**Ghost theorem:** $A_b = \mathrm{End}_{\mathcal C}(b)$ for a chosen boundary $b$ is a useful chart-dependent description of the open structure.

**Precise error:** chart-vs-invariant collapse: the primitive is the open factorisation dg-category on $(X,D,\tau)$; $A_b$ depends on the choice of $b$.

**Correct relationship:** primitive = $(X, D, \tau; \mathcal C^{\mathrm{op}}, b, A_b, Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal C), \Theta_{\mathcal C}, \mathrm{Tr}_{\mathcal C})$. $A_b$ enters only after $b$ is named.

**Type:** primitive/chart.

### AP-CY-Crit-2 — bar ≠ bulk

**Wrong claim:** $\mathrm{Bar}(A)$ is the bulk; $\mathrm{ChiralBar}(A) = $ bulk.

**Ghost theorem:** $\mathrm{Bar}(A)$ is the universal twisting/coupling coalgebra, which controls Koszul comparison and is part of the (boundary, bulk) Swiss-cheese pair.

**Precise error:** identifying the coupling-data shadow with the bulk operator algebra. Bulk is $Z^{\mathrm{der}}_{\mathrm{ch}}(A) \simeq \mathrm{ChirHoch}^\bullet(A, A)$.

**Correct relationship:** $\mathrm{Bar}(A) = $ twisting/coupling coalgebra; $Z^{\mathrm{der}}_{\mathrm{ch}}(A) = $ bulk; $(Z^{\mathrm{der}}_{\mathrm{ch}}(A), A)$ is the Swiss-cheese pair.

**Type:** bar-vs-centre.

### AP-CY-Crit-3 — bar-direction ≠ Swiss-cheese promotion

**Wrong claim:** the $2d \rightsquigarrow 3d$ HT promotion is explained by the existence of an $E_1$-bar interval direction.

**Ghost theorem:** boundary models with an extra interval direction give one computational realisation of the dimensional uplift.

**Precise error:** treating the computational model as the structural mechanism. The mechanism is the chiral Deligne–Tamarkin / Swiss-cheese promotion: boundary $A_\infty$-chiral object $\rightsquigarrow$ one-dimension-up acting object $Z^{\mathrm{der}}_{\mathrm{ch}}(A)$.

**Correct relationship:** Swiss-cheese promotion is structural; bar-direction is one model.

**Type:** structure-vs-model.

### AP-CY-Crit-4 — open sector requires tangential log curve

**Wrong claim:** there is a global open sector on a bare curve $X$.

**Ghost theorem:** with a tangential log structure $(X, D, \tau)$, the open sector lives on the real-oriented blowup / log boundary.

**Precise error:** omitting the log/tangential decoration leaves "boundary," "trace," "open category," "clutching" without geometric carrier.

**Correct relationship:** every open-sector statement is attached to $(X, D, \tau)$.

**Type:** geometric-carrier omission.

### AP-CY-Crit-5 — modularity ≠ closed-algebra property

**Wrong claim:** the closed chiral algebra is modular.

**Ghost theorem:** modular consequences hold for the closed shadow when the open category carries trace + clutching; the modular functor lives on the open category.

**Precise error:** modularity treated as adjective on the closed algebra rather than as a property of the open-side data.

**Correct relationship:** "the open category carries a cyclic trace compatible with clutching; its closed shadow has modular consequences."

**Type:** open-vs-closed adjective.

### AP-CY-Crit-6 — five $\kappa_\bullet$ are not one invariant; naive additive form falsified

**Wrong claim:** $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fiber}})$ on $K3 \times E$.

**Ghost theorem:** the universal Borcherds-weight identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ (Gritsenko 1999 Thm 6.1) evaluated at the chosen Siegel input denominator.

**Precise error:** the naive additive form fails at $N = 1$ (left = $5$, right = $0+0=0$).

**Correct relationship:** five $\kappa_\bullet$ on $K3 \times E$ come from five distinct constructions: $\kappa_{\mathrm{cat}} = 0$ (Künneth multiplicative), $\kappa_{\mathrm{ch}}^{\mathrm{Hodge}} = 0$, $\kappa_{\mathrm{ch}}^{\mathrm{Heis}} = 3$, $\kappa_{\mathrm{BKM}}(\Delta_5) = 5$, $\kappa_{\mathrm{fiber}} = 24$.

**Cross-volume action required:** Vol I `chapters/examples/lattice_foundations.tex:5866` — repair contradiction with Vol III `chapters/examples/k3e_bkm_chapter.tex:14340` and `chapters/examples/cy_d_kappa_stratification.tex` Theorem `thm:borcherds-weight-kappa-BKM-universal`.

**Type:** numerical/cross-volume contradiction.

### AP-CY-Crit-7 — Φ is not a one-stage functor

**Wrong claim:** $\Phi: \mathrm{CY}_d\text{-Cat} \to \mathrm{ChirAlg}$ is a direct functor.

**Ghost theorem:** $\Phi^{(\Sigma_{d-1}, C)}_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} \circ \Phi^{\mathrm{FA}}_d$ is the two-stage construction; Stage-1 is canonical up to GRT$_1(\mathbb Q)$-torsor; Stage-2 depends on chart $(\Sigma_{d-1}, C)$.

**Precise error:** one-stage framing collapses Stage-1 (canonical) and Stage-2 (chart-dependent) into a single arrow, hiding the chart datum.

**Correct relationship:** the two-stage form. $\{\Phi_d\}$ is a correspondence programme (per-$d$ assignment), not a single functor (target $E_{n(d)}$-ChirAlg depends on $d$).

**Sweep target:** Vol III `chapters/theory/hochschild_calculus.tex:1570`, `quantum_groups_foundations.tex:6261`, `introduction.tex:1664`, `cyclic_ainf.tex:247`, `phi_universal_trace_platonic.tex:494` — all have bare `\Phi_d : \mathrm{CY}_d\text{-Cat} \to \mathrm{ChirAlg}` requiring two-stage annotation.

**Type:** functoriality scope.

### AP-CY-Crit-8 — Y⁺(X) ≠ G(X); CoHA(C³) ≠ W₁₊∞ before doubling

**Wrong claim:** the positive half is the quantum group; $\mathrm{CoHA}(\mathbb{C}^3) = \mathcal W_{1+\infty}$.

**Ghost theorem:** $G(X) = D(Y^+(X))$ (Drinfeld double, after pairing/completion/integral form/stable-envelope/descent); $\mathrm{CoHA}(\mathbb{C}^3) = Y^+(\widehat{\mathfrak{gl}}_1)$, with $\mathcal W_{1+\infty}$ appearing only after Drinfeld doubling and Fock evaluation.

**Precise error:** identifying positive half with full Drinfeld double (or with vertex evaluation image).

**Correct relationship:** the CoHA evaluation chain — $\mathrm{CoHA} = Y^+$ ($E_1$-associative) $\hookrightarrow$ $Y(\widehat{\mathfrak{gl}}_1)$ (Drinfeld double, Hopf) $\xrightarrow{\mathrm{ev}_\lambda}$ $\mathrm{End}(\mathcal W_{1+\infty}[\lambda]\text{-vac})$ (vertex algebra image).

**Sweep target:** Vol I `frontier_modular_holography_platonic.tex:5244, 5252, 5289, 5356, 5398, 5440, 5473, 5496, 5547, 5550, 5657` — every $\cA_{\mathrm{M5}}(N) = W_{1+\infty}[\lambda = N]$ identification needs the Drinfeld-doubling + Fock-evaluation qualifier.

**Type:** positive-half-vs-double.

### AP-CY-Crit-9 — 6d hCS ≠ 3d Chern–Simons; quartic obstruction

**Wrong claim:** 6d hCS is 3d CS in disguise; one-loop obstruction is cubic Casimir.

**Ghost theorem:** at $d = 3$, 6d hCS supplies the physical realization of $\Phi^{\mathrm{FA}}_3$ on verified loci; one-loop obstruction is the quartic $\int_X \mathrm{Tr}_{\mathrm{ad}}(A(F_A)^3)$ (cohomological piece sourced by cubic symmetric Casimir $d^{abc}$).

**Precise error:** import of 3d CS knot intuition into 6d hCS without passing through BV/hCS obstruction theory.

**Correct relationship:** 6d hCS is its own theory; the obstruction is quartic-in-fields, sourced by cubic Casimir.

**Status:** Vol III `[locked]` per AP-CY262 and `phi_universal_trace_platonic.tex:1175-1194`.

**Type:** physical-theory-import.

### AP-CY-Crit-10 — formal Darboux ≠ global compact theory

**Wrong claim:** formal Darboux model on $\mathbb R^2_{\mathrm{top}} \times \mathbb C^2_{\mathrm{hol}}$ implies global compact target theory.

**Ghost theorem:** formal Darboux model + descent + QME + anomaly + locality $\Rightarrow$ candidate compact theory.

**Precise error:** local Hamiltonian identification asserted globally without holomorphic de Rham obstruction discipline.

**Correct relationship:** every local-to-global step lists (i) descent datum, (ii) QME, (iii) anomaly, (iv) locality. The holomorphic de Rham class is the obstruction.

**Status:** mixed-HT-strings `[locked]` per `main.tex:3207-3266`.

**Type:** local-vs-global formal-to-physical promotion.

### AP-CY-Crit-11 — Δ₅ ≠ compact BPS Hilbert space

**Wrong claim:** $\Delta_5$ = physical Hilbert space.

**Ghost theorem:** $\Delta_5$ = Borcherds denominator / protected scalar shadow; the missing problem is to construct the operator-level object whose protected Pfaffian is $\Delta_5$.

**Precise error:** scalar-to-operator promotion without source-recognition gates (Pfaffian construction, Hall correspondences, orientation, BPS operator product).

**Correct relationship:** Igusa programme is terminal scalar shadow; operator-level construction is a separate research line.

**Status:** igusa-cusp-form `[locked]` per `main.tex:96` and `notes/swarm_20260430/reports/A270`.

**Type:** scalar-vs-operator promotion.

### AP-CY-Crit-12 — scalar partition function ≠ operator algebra

**Wrong claim:** $Z_{\mathrm{BPS}}^{K3 \times E} = \Phi_{10}^{-1}$ is the gravitational path integral / operator algebra.

**Ghost theorem:** $Z_{\mathrm{BPS}}$ is a protected scalar trace whose promotion to gravity-line / operator-algebra requires the Hall–Borcherds comparison residual.

**Precise error:** scalar-to-operator-algebra promotion without the comparison gates.

**Correct relationship:** scalar automorphic form = protected trace of a still-to-be-constructed operator package.

**Type:** scalar-vs-operator-algebra promotion (companion to AP-CY-Crit-11).

### AP-CY-Crit-13 — Universal Holography ≠ dynamical metric path integral

**Wrong claim:** the Vol II Universal Holography master theorem constructs the dynamical metric path integral for 3d gravity.

**Ghost theorem:** the master theorem identifies (boundary = $A$, bulk = $Z^{\mathrm{der}}_{\mathrm{ch}}(A)$, interaction = $\mathrm{SC}^{\mathrm{ch,top}}$-brace action). For $A = \mathrm{Vir}_c$, this is the holographic HT sector of pure 3d gravity.

**Precise error:** the dynamical-metric path integral requires saddle-dominance, modular invariance, and vacuum-dominance hypotheses that the master theorem does not supply.

**Correct relationship:** Vol II identifies the algebraic holographic HT sector; "constructing 3d gravity" claim should be retired.

**Type:** physical-interpretation overpromotion.

### AP-CY-Crit-14 — $W_\infty[\lambda] \Rightarrow E_\infty$ requires endpoint admissibility

**Wrong claim:** $W_\infty[\lambda] \Rightarrow E_\infty$ as theorem.

**Ghost theorem:** the implication holds within the admissible window characterised by Prochazka triangular truncation, CKL parafermion compatibility, PRS/Bakas input, and Yamada weight-window condition.

**Precise error:** spin-$\le 8$ numerical evidence treated as proof of the structural endpoint.

**Correct relationship:** four-condition admissible window; outside it, the implication is open.

**Type:** evidence-vs-proof / endpoint admissibility.

### AP-CY-Crit-15 — class M chain-level requires completed ambient

**Wrong claim:** class M works chain-level in ordinary complexes.

**Ghost theorem:** in the weight-completed / pro / $J$-adic / HS-sewing ambient, class M chain-level identifications hold.

**Precise error:** forcing class M into ordinary complexes blocks the theorem; the correct move is to work in the completed ambient.

**Correct relationship:** every chain-level theorem declares its ambient; class M lives in completed ambients.

**Status:** Vol II `[locked]` per `weight_completed_topologization_class_m_platonic.tex` and `chiral_higher_deligne.tex:909-946`.

**Type:** ambient-qualifier discipline.

### AP-CY-Crit-16 — PVA Jacobi ≠ all-loop quantum theory

**Wrong claim:** PVA $\lambda$-Jacobi gives the all-loop quantum HT theory.

**Ghost theorem:** PVA Jacobi gives classical gauge invariance (Khan–Zeng); a Virasoro element upgrades to topological. All-loop boundary VOA, $E_3$-lift, and analytic renormalized closed-open package are extra data, conditional on KZ analytic SDR + Stokes choices + reflected weights + $T = [Q_{\mathrm{tot}}, G]$ lift.

**Precise error:** classical-quantum collapse, omitting the four-step ladder.

**Correct relationship:** PVA Jacobi is classical; quantum requires the named four-step package.

**Type:** classical-vs-quantum promotion.

### AP-CY-Crit-17 — quadratic chiral duality ≠ Koszul duality theorem

**Wrong claim:** quadratic dual exists $\Rightarrow$ Koszul duality theorem.

**Ghost theorem:** Gui–Li–Zeng (arXiv:2212.11252) prove an injection $\mathrm{Hom}(A, B) \hookrightarrow \mathrm{MC}(A^! \otimes B)$ with bijectivity in special cases; full Koszulness in homotopy setting is the separate theorem.

**Precise error:** treating the candidate-dual MC injection as the Koszulness theorem.

**Correct relationship:** quadratic dual $\Rightarrow$ candidate dual + MC comparison map; Koszulness is a separate theorem (one of the fourteen characterisations).

**Type:** chiral-Koszulness scope.

---

## 4. Cache append — drafted

The following rows should be appended to `appendices/first_principles_cache.md` in Vol III (and mirrored in Vol I and Vol II caches).

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|---|---|---|---|---|
| Crit-1 | $A$ is the primitive open object | $A_b = \mathrm{End}_{\mathcal C}(b)$ chart-algebra | chart-vs-invariant collapse | primitive = $(X,D,\tau; \mathcal C, b, A_b, Z^{\mathrm{der}}_{\mathrm{ch}}, \Theta, \mathrm{Tr})$ | primitive/chart |
| Crit-2 | $\mathrm{Bar}(A)$ is the bulk | $\mathrm{Bar}$ = twisting coalgebra; $Z^{\mathrm{der}}_{\mathrm{ch}}$ = bulk | shadow-as-object | $(Z^{\mathrm{der}}_{\mathrm{ch}}(A), A)$ Swiss-cheese pair | bar/centre |
| Crit-3 | $E_1$-bar explains $2d \to 3d$ uplift | bar-direction is one model; Swiss-cheese is the structure | model-as-explanation | chiral Deligne–Tamarkin + Lurie additivity | structure/model |
| Crit-4 | open sector on bare $X$ | open sector on $(X,D,\tau)$ | log-decoration omission | tangential log curve required | geometry/log |
| Crit-5 | closed chiral algebra is modular | open category carries trace + clutching; closed shadow has modular consequence | adjective on closed | trace + clutching on open | modularity |
| Crit-6 | $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal O_{\mathrm{fiber}})$ | $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ at chosen Siegel denominator | additive-shift collapse | five distinct constructions on $K3\times E$ | numerical/Borcherds |
| Crit-7 | $\Phi: \mathrm{CY}_d\text{-Cat} \to \mathrm{ChirAlg}$ direct | $\Phi^{(\Sigma_{d-1}, C)}_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} \circ \Phi^{\mathrm{FA}}_d$ | one-stage collapse | two-stage; Stage-1 canonical, Stage-2 chart-dependent | functoriality |
| Crit-8 | $Y^+(X) = G(X)$ | $G(X) = D(Y^+(X))$ after pairing/completion/integral form/stable envelope/descent | positive-half-vs-double collapse | CoHA evaluation chain | $Y^+/G$ |
| Crit-9 | 6d hCS = 3d CS in disguise | 6d hCS is its own theory; obstruction quartic-in-fields | physical-import collapse | $\int_X \mathrm{Tr}_{\mathrm{ad}}(A(F_A)^3)$ | physical theory |
| Crit-10 | formal Darboux $\Rightarrow$ global compact theory | + descent + QME + anomaly + locality | local-to-global collapse | holomorphic de Rham obstruction | local/global |
| Crit-11 | $\Delta_5$ = compact BPS Hilbert space | $\Delta_5$ = Borcherds denominator / protected Pfaffian | scalar-to-operator collapse | terminal scalar shadow | scalar/operator |
| Crit-12 | $Z_{\mathrm{BPS}} = $ operator algebra | $Z_{\mathrm{BPS}}$ = protected scalar trace | scalar-to-operator-algebra collapse | Hall–Borcherds comparison required | scalar/operator |
| Crit-13 | Universal Holography = dynamical metric path integral | identifies algebraic holographic HT sector | construction overpromotion | algebraic HT sector identification | physical-interp |
| Crit-14 | $W_\infty[\lambda] \Rightarrow E_\infty$ | within Prochazka + CKL + PRS + Yamada window | endpoint scope collapse | four-condition admissible window | endpoint admissibility |
| Crit-15 | class M chain-level in ordinary complexes | weight-completed / pro / $J$-adic / HS-sewing ambient | ambient-omission collapse | declare ambient at every chain-level theorem | ambient qualifier |
| Crit-16 | PVA Jacobi $\Rightarrow$ all-loop quantum | classical gauge invariance; quantum needs KZ SDR + Stokes + reflected weights + $T$-lift | classical-quantum collapse | four-step ladder | classical/quantum |
| Crit-17 | quadratic chiral dual $\Rightarrow$ Koszul duality theorem | Hom $\hookrightarrow$ MC injection (Gui–Li–Zeng) | candidate-dual collapse | Koszulness is separate theorem | duality scope |

---

## 5. Sequencing the reconstitution

Five phases, ordered by dependency.

### Phase 1: Architectural taxonomy installation (≤ 1 session)

Insert the level-discipline preface paragraph (§2.1) into the abstract or introduction of all five manuscripts. This is **structural framing**, not content rewriting.

- Vol I: `chapters/frame/preface.tex` (or equivalent intro file).
- Vol II: `chapters/theory/introduction.tex` opening.
- Vol III: `chapters/frame/preface.tex` opening; `working_notes.tex` sec:organising-framework already has the two-stage form, just lift to top-level.
- igusa-cusp-form: `main.tex` already has the disclaimer at line 96; lift to abstract.
- mixed-HT-strings: `main.tex` already has the obstruction discipline at lines 3207-3266; lift to abstract.

**Deliverable:** five new preface paragraphs, one per manuscript, with cross-links.

### Phase 2: Cross-volume contradiction repair (highest priority)

The single hard contradiction surfaced by the critique:

- Vol I `chapters/examples/lattice_foundations.tex:5866` — repair the naive additive $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal O_{\mathrm{fibre}})$ to the universal Borcherds-weight identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$. Cite Vol III `cy_d_kappa_stratification.tex` Theorem `thm:borcherds-weight-kappa-BKM-universal`.

This is the AP5-pending lock (cache row 65). Fix it at the locus, then update both volumes' caches.

**Deliverable:** one specific edit to one Vol I file; cross-volume cache update.

### Phase 3: Per-dismissal residual repair (priority-ranked)

Order by severity × cross-volume reach:

1. **Dismissal 7** (two-stage Φ): sweep Vol III `chapters/theory/` for bare `\Phi_d : \mathrm{CY}_d\text{-Cat} \to \mathrm{ChirAlg}` and annotate with two-stage form. ~5–10 specific files.
2. **Dismissal 8** (Y⁺ ≠ G; CoHA(C³) ≠ W_{1+∞}): sweep Vol I `frontier_modular_holography_platonic.tex` for $\cA_{\mathrm{M5}} = W_{1+\infty}$ identifications and add Drinfeld-double + Fock-evaluation qualifier. ~10 line edits.
3. **Dismissal 13** (Universal Holography ≠ dynamical metric path integral): sweep Vol II `chapters/theory/introduction.tex` for "3d quantum gravity" framings and soften to "algebraic holographic HT sector". ~10 line edits + intro-paragraph rewrite.
4. **Dismissal 14** (endpoint admissibility): sweep Vol II for $W_\infty[\lambda] \Rightarrow E_\infty$ statements and add four-hypothesis admissible-scope clause.
5. **Dismissal 16** (PVA Jacobi): sweep Vol II `modular_pva_quantization*.tex` for classical-quantum overpromotions.
6. **Dismissal 17** (Koszul scope): sweep Vol I Koszul chapters for Koszul-duality-theorem claims; specify which characterisation.
7. **Dismissals 1, 2, 3, 4, 5** (open/closed architecture): mostly already locked; verify cross-references are explicit.
8. **Dismissals 9, 10, 11, 12, 15**: mostly already locked; verify cross-references are explicit.

**Deliverable:** ~50–80 specific file edits across the five volumes.

### Phase 4: Cross-volume citation graph

Once individual repairs are done, install the citation graph that makes the level discipline explicit:

- Vol III `cy_d_kappa_stratification.tex` Theorem `thm:borcherds-weight-kappa-BKM-universal` cited from Vol I, Vol II, igusa-cusp-form anywhere $\kappa_{\mathrm{BKM}}$ is named.
- Vol III `cy_to_chiral.tex:2840-2856` (correspondence-programme remark) cited from any cross-volume invocation of $\Phi$.
- Vol I `configuration_spaces.tex:2062-2544` (tangential log curve definition) cited from any open-sector statement in Vol II/III.
- Vol II `weight_completed_topologization_class_m_platonic.tex` cited from any class M chain-level statement.
- Vol II `chiral_higher_deligne.tex` cited from any Swiss-cheese / Universal Holography invocation.
- igusa-cusp-form `main.tex:96` (disclaimer) cited from any $\Delta_5$ invocation.
- mixed-HT-strings `main.tex:3207-3266` (obstruction discipline) cited from any local-Hamiltonian-BF statement in Vol II/III.
- `notes/sixth_attack_heal_20260428` source/target firewall cited from any operator-level claim about $\mathbf H_{\Delta_5}$.

**Deliverable:** ~10 canonical-reference \cite{} insertions across the five volumes.

### Phase 5: Bookkeeping update

- Append AP-CY-Crit-1 through AP-CY-Crit-17 to `notes/antipatterns_catalogue.md` (Vol III) and mirror cross-references in Vol I and Vol II AP catalogues.
- Append the 17 cache rows to `appendices/first_principles_cache.md` (Vol III) and mirror cross-references.
- Update memory entries:
  - new `feedback_shadow_object_master_pattern.md`
  - new `feedback_level_discipline_promotion_ladder.md`
  - new `project_kappa_additive_form_cross_volume_lock.md` (records the Vol I repair)
  - update `project_two_stage_factorisation.md` to include the AP-CY-Crit-7 sweep targets
  - update `reference_coha_evaluation_chain.md` to reference AP-CY-Crit-8

**Deliverable:** AP catalogue + cache + memory entries appended; cross-references installed.

---

## 6. Risk register: discard / downgrade / rename / preserve

The critique's own categories.

### Discard (sentences to delete from the manuscripts)

- $\mathrm{Bar}(A)$ is the bulk. (everywhere it appears)
- $A$ is the primitive open sector. (everywhere)
- $\Phi_d : \mathrm{CY}_d\text{-Cat} \to \mathrm{ChirAlg}$ is direct. (one-stage form)
- $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fiber}})$. (additive form)
- $\mathrm{CoHA}(\mathbb{C}^3) = \mathcal W_{1+\infty}$. (without doubling/evaluation qualifier)
- $\Delta_5$ constructs the compact BPS Hilbert space. (everywhere)
- $Z_{\mathrm{BPS}}$ is the gravitational path integral. (everywhere)
- formal local Hamiltonian BF $\Rightarrow$ compact twisted M-theory background. (without obstruction)
- $W_\infty[\lambda] \Rightarrow E_\infty$ without endpoint hypotheses. (out-of-scope)
- PVA Jacobi $\Rightarrow$ all-loop quantum HT theory. (without four-step package)

Each has a corrected version in the manuscripts already; the discard is replacement, not deletion-without-substitute.

### Downgrade (claims to weaken to conjecture / conditional)

- "Universal Holography constructs 3d quantum gravity" $\to$ "Universal Holography identifies the algebraic holographic HT sector; dynamical metric path integral conditional on saddle-dominance + modular invariance + vacuum dominance".
- "$\Phi_d$ is a functor at $d \ge 3$" $\to$ "$\Phi^{(\Sigma_{d-1}, C)}_d$ is constructed at object level on verified loci; morphism functoriality is per-$d$ conjecture".
- "$\Phi_d$ is a unified functor across $d$" $\to$ "correspondence programme; per-$d$ assignment; target $E_{n(d)}$-ChirAlg depends on $d$".
- "Quadratic chiral duality is Koszul duality theorem" $\to$ "candidate-dual injection of Gui–Li–Zeng; Koszulness theorem (in admissible homotopy setting) is separate".
- "Class M chain-level identification" $\to$ "class M chain-level identification in weight-completed / pro / $J$-adic / HS-sewing ambient".

### Rename (vocabulary realignment)

- "the M5 algebra **is** $W_{1+\infty}[\lambda = N]$" $\to$ "the M5 algebra is the Drinfeld-double + Fock-evaluation image of $Y^+(\widehat{\mathfrak{gl}}_1)$ at $\lambda = N$".
- "$\Phi$ functor" (at $d \ge 3$) $\to$ "$\Phi$ correspondence programme" or "$\Phi^{(\Sigma_2, C)}_3$ chart-specialisation".
- "the chiral algebra of CY data" $\to$ "the chiral shadow at chart $(\Sigma_{d-1}, C)$ of the CY data".
- "the bulk is the bar" $\to$ "the bulk is the derived chiral centre; the bar is the universal twisting coalgebra".
- "modular chiral algebra" $\to$ "open category carrying cyclic trace compatible with clutching; closed shadow has modular consequence".

### Preserve (the non-false core)

These statements are **correct** and should be preserved (per the critique's "What is not false" section):

- $(X, D, \tau; \mathcal C^{\mathrm{op}}, b, A_b, Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal C), \Theta_{\mathcal C}, \mathrm{Tr}_{\mathcal C})$ as the primitive open package.
- The open-side arrow: $\text{open factorization category} \rightsquigarrow A_b \rightsquigarrow B(A_b) \rightsquigarrow Z^{\mathrm{der}}_{\mathrm{ch}}(A_b) \rightsquigarrow \text{line / scalar trace}$.
- The CY-side arrow: $\mathrm{CY}_d\text{-cat} \rightsquigarrow \Phi^{\mathrm{FA}}_d \rightsquigarrow \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} \rightsquigarrow \text{chiral shadow} \rightsquigarrow Y^+ \rightsquigarrow G(X) \rightsquigarrow \Delta_5$.
- $\Phi$-correspondence-programme architecture (per Vol III `cy_to_chiral.tex:2840`).
- Universal Borcherds-weight identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ (per Vol III `cy_d_kappa_stratification.tex`).
- Class M chain-level theorem **in weight-completed ambient** (per Vol II `weight_completed_topologization_class_m_platonic.tex`).
- Six-dimensional hCS quartic obstruction (per Vol III `phi_universal_trace_platonic.tex:1175-1194`).
- igusa-cusp-form's protected Pfaffian / Borcherds denominator status with the disclaimer about non-construction of compact BPS Hilbert space.
- mixed-HT-strings's local theorem with the holomorphic de Rham obstruction discipline.

These are the **correct** mathematical content; the reconstitution is around them, not against them.

---

## 7. Concluding Beilinson cut

The seventeen dismissals reduce to one operating principle:

> **Primitive objects first, shadows second, scalar modular forms last.**

Applied uniformly across the five manuscripts, this principle:

- Resolves the cross-volume $\kappa_{\mathrm{BKM}}$ contradiction (Vol I `lattice_foundations.tex:5866` $\to$ Vol III universal identity).
- Strengthens Vol III's two-stage Φ from a Wave-12 inscription into a programme-wide invariant.
- Inserts the Drinfeld-double + Fock-evaluation gates between every CoHA $\to W_{1+\infty}$ identification.
- Softens Vol II's "constructs 3D quantum gravity" claim to the more precise (and more defensible) "identifies the algebraic holographic HT sector".
- Promotes Igusa's `main.tex:96` disclaimer and mixed-HT's `main.tex:3207-3266` obstruction discipline from local conventions to programme-wide invariants.
- Installs the level-discipline (primitive / chart / shadow / bulk-or-scalar) as the citation backbone.

The cost is small: ~80 specific file edits, ~17 AP-CY entries, ~17 cache rows, ~5 preface paragraphs, ~10 cross-volume \cite{} insertions.

The benefit is large: the reconstituted programme has **no shadow=object collapses**, and every theorem statement carries its level + chart datum + obstruction discipline. That is the architectural state in which the true ideas — the K3 BKM, the universal Borcherds weight, the two-stage Φ, the holographic HT sector, the protected Pfaffian on the Igusa scalar — can take root without competing for space with their own partial shadows.

This document is the punch list for that reconstitution. It is exhaustive at the architectural level (every dismissal mapped, every cross-volume ripple traced, every bookkeeping consequence drafted) and representative at the line level (specific high-impact loci named; sweep patterns provided for the bulk). The next step is execution: Phase 1 (architectural taxonomy) and Phase 2 (cross-volume contradiction repair) are the two highest-leverage actions and can proceed in parallel.

---

## 8. References to programme-internal canonical loci

For convenience, the canonical inscriptions cited throughout this document:

- **Vol I configuration_spaces.tex:2062-2544** — tangential log curve $(X, D, \tau)$ definition.
- **Vol I configuration_spaces.tex:2865-2911** — open-closed modular convolution algebra.
- **Vol I chiral_center_theorem.tex:1889-1925** — global theory on $(X, D, \tau)$.
- **Vol I e1_modular_koszul.tex** — modular Koszul package.
- **Vol I lattice_foundations.tex:5866** — naive additive κ formula (TO REPAIR).
- **Vol I frontier_modular_holography_platonic.tex:5244-5657** — M5-W_{1+∞} identifications (TO ANNOTATE with Drinfeld-double + Fock-evaluation qualifier).
- **Vol II equivalence.tex:145** — class M chain-level may fail in ordinary complexes.
- **Vol II weight_completed_topologization_class_m_platonic.tex** — class M in weight-completed ambient.
- **Vol II chiral_higher_deligne.tex:909-946** — universal holography for class M in weight-completed ambient.
- **Vol II modular_pva_quantization_core.tex:187-196** — HS-sewing criterion.
- **Vol II introduction.tex:106-3019** — "3d quantum gravity" framings (TO SOFTEN).
- **Vol II modular_swiss_cheese_operad.tex:4177** — "master theorem realizes 3D quantum gravity" (TO SOFTEN).
- **Vol II axioms.tex:1470** — open-closed modular pairing.
- **Vol III working_notes.tex** sec:two-stage-factorisation:467, sec:organising-framework:528, etc. — two-stage Φ.
- **Vol III cy_to_chiral.tex:2840-2856** — Φ correspondence programme, not unified functor.
- **Vol III cy_d_kappa_stratification.tex** Theorem `thm:borcherds-weight-kappa-BKM-universal` — universal Borcherds-weight identity.
- **Vol III k3e_bkm_chapter.tex:14340** — naive additive form falsified.
- **Vol III quantum_chiral_algebras.tex:1247** — $Z^{\mathrm{der}}_{\mathrm{ch}}$ is the bulk.
- **Vol III phi_universal_trace_platonic.tex:1175-1194** — cubic vs quadratic Casimir split.
- **Vol III hochschild_calculus.tex:1570** — bare $\Phi_3 : \mathrm{CY}\text{-cat}_3 \to \mathrm{ChirAlg}^{E_1}$ (TO ANNOTATE).
- **Vol III quantum_groups_foundations.tex:6261** — bare $\Phi_3$ form (TO ANNOTATE).
- **Vol III appendices/first_principles_cache.md** rows 64, 65, 66, 67, 70, 71-82 — existing scalar-vs-operator gates.
- **Vol III notes/antipatterns_catalogue.md** AP-CY68, AP234, AP262, AP273, AP345-454 — existing discipline catalogue.
- **igusa-cusp-form main.tex:96** — disclaimer "It does not supply a compact BPS Hilbert space, ...".
- **igusa-cusp-form notes/swarm_20260430/reports/A270** — cross-repository source/target firewall.
- **igusa-cusp-form notes/sixth_attack_heal_20260428/agent2_costello_witten_bv_anomaly.md** — O2 obstruction discipline.
- **mixed-HT-strings main.tex:3207-3266** — holomorphic de Rham obstruction; locally Hamiltonian symplectic vector field.

These loci are the structural skeleton; the punch list of edits in Phase 3 connects them to every dependent claim.

---

*End of consequence map. Phase 1 and Phase 2 (architectural taxonomy + cross-volume contradiction repair) are the recommended next-session actions.*
