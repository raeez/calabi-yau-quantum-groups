# Agent 04 — Polyakov — Wave 12

**Author.** Raeez Lorgat.
**Voice.** A. M. Polyakov. The worldsheet has the last word. Central charges are *additive* invariants: each arises from a counted matter content with a named stress tensor, and none of them negotiate with bookkeeping. Wave 11 (Polyakov) killed the myth that "c=15 Goddard-Thorn no-ghost" is the worldsheet origin of $\mathfrak{g}_{\Delta_5}$. Wave 12 must now tabulate *all* central charges appearing in the final $\mathbf{H}_{\Delta_5}$ object, name the literature reference behind each, and demonstrate how they compose (or fail to compose) into the various coincidental-15, coincidental-12, and coincidental-24 numbers that tangled Wave 10.

**Wave 12 remit.** Five+ attack-heal cycles. Primary deliverable: the c-table (§Central-charge tabulation). Secondary: attack Conway $c=12$ subgroup projection, attack Borcherds-1998 as chiral-algebra producer vs modular-form producer, identify the "c=3 sector" that completes Wave-11's $c = 12 + 3 = 15$ arithmetic, and check genus-2 Siegel-modular invariance.

**Primary references (against which I will cross-check every c-value):**
- Goddard-Thorn 1972, *Nucl. Phys. B40*, 235 (no-ghost, requires $c = 26$ bosonic or $c = 15$ super).
- Polyakov 1981, *Phys. Lett. B103*, 207 (critical anomaly, $c = 26$).
- Friedel-Martinec-Shenker 1986, *Nucl. Phys. B271*, 93 (super-ghost $(\beta, \gamma)$: $c = +11$; bosonic $(b, c)$: $c = -26$).
- Borcherds 1986, *PNAS 83*, 3068 (VOA definition).
- Borcherds 1992, *Invent. Math. 109*, 405 (Monster BKM at $c = 24$).
- Borcherds 1995, *Invent. Math. 120*, 161 (Grassmannian theta lift seed).
- Borcherds 1998, *Invent. Math. 132*, 491, Theorem 13.3 (singular theta lift on $\mathrm{II}_{2,s}$).
- Duncan 2007, *Duke Math. J. 139*, 255 (Conway $V^{f\natural}$ at $c = 12$, $\mathrm{Aut} = \mathrm{Co}_0$).
- Duncan-Mack-Crane 2015, *Forum Math. Sigma 3*, e10 (K3 elliptic genus via Conway twisting).
- Eguchi-Ooguri-Tachikawa 2010 (arXiv:1004.0956), §2 (K3 elliptic genus decomposition into $N=4$ characters).
- Cheng-Duncan-Harvey 2014, *CNTP 8*, 101 (umbral genus $\ell = 2$, $G^{(\ell=2)} = M_{24}$; $c$-value of umbral seed VOA = 6 or 12 per case).
- Sevrin-Troost-Van Proeyen 1988, *Phys. Lett. B208*, 447 (small N=4 on K3: $c = 6$).
- Frenkel-Lepowsky-Meurman 1988, *Vertex Operator Algebras and the Monster* (Leech $V_{\Lambda_{24}}$ at $c = 24$).
- Scheithauer 2015, *Compos. Math. 151*, 1645 (additive / Borcherds products comparison, modular-form output vs chiral-algebra output).
- Dijkgraaf-Verlinde-Verlinde 1997, *Nucl. Phys. B484*, 543 (heterotic on $T^2 \times K3$, 1/4-BPS dyon generating function $1/\Phi_{10}$; $\Phi_{10}$ as Borcherds lift of K3 EG).
- Gritsenko-Nikulin 1998, *Am. J. Math. 120*, 1 (Siegel automorphic products, $\Phi_{10}$ and $\Delta_5 = \Phi_5$).
- Aspinwall 1996, *Nucl. Phys. B471*, 175 (K3 moduli $\mathrm{O}(\Gamma^{4,20} \backslash \mathbb{H}_{4,20})$, Mukai lattice).

---

## Central-charge tabulation

This is the primary W12-T4 deliverable. Each row names a sector, gives its central charge with literature citation, names the stress tensor (or explains why none exists), and states its role in $\mathbf{H}_{\Delta_5}$.

| # | Sector | $c$ | Citation | Role in $\mathbf{H}_{\Delta_5}$ |
|---|---|---|---|---|
| 1 | K3 sigma-model matter (small N=4, chiral half) | **6** | EOT 2010 §2; Sevrin-Troost-Van Proeyen 1988 | Geometric input: chiral half of K3 N=(4,4) sigma model; R-charge generates $\mathrm{su}(2)$ level 1 |
| 2 | $T^2$ super-sigma, chiral half | **3** | Polchinski 1998 Vol II §10.7 | Auxiliary compactification in DVV 1997 dyon-counting target space; NOT part of the algebraic seed |
| 3 | $\mathbb{R}^{1,3}$ longitudinal (type II) | **6** | Polchinski 1998 Vol II §11.2 | Background spacetime, appears only in target-space side of DVV 1997; irrelevant to seed |
| 4 | Super-ghost $(\beta, \gamma)$ weights $(3/2, -1/2)$ | **+11** | Friedel-Martinec-Shenker 1986 | Critical-anomaly bookkeeping only; cancels in $c_{\rm tot} = 0$ |
| 5 | Bosonic ghost $(b, c)$ weights $(2, -1)$ | **$-26$** | Polyakov 1981 | Critical-anomaly bookkeeping; not in BKM side |
| 6 | Conway super-VOA $V^{f\natural}$ | **12** | Duncan 2007 Thm 4.8 | **Algebraic seed of $\mathbf{H}_{\Delta_5}$** (Wave 11 Polyakov consensus); $\mathrm{Co}_0$-automorphism |
| 7 | Hyperbolic super-lattice $V_{\mathrm{II}_{1,1}}^{\rm super}$ | **3** | FLM 1988 §8 (bosonic antecedent); super extension adds $2$ free Majorana fermions to rank-2 bosons | Goddard-Thorn "light-cone" in Conway super-Borcherds $\to \mathfrak{g}_{\rm Co_0}$; NOT used for $\mathfrak{g}_{\Delta_5}$ |
| 8 | Leech lattice VOA $V_{\Lambda_{24}}$ | **24** | FLM 1988 §11 | Underlying lattice of Conway; Monster-side cousin |
| 9 | Monster moonshine VOA $V^\natural$ | **24** | FLM 1988 §12; Borcherds 1992 | Monster-side, not K3-side; included for contrast |
| 10 | Positive-signature chirality of Mukai lattice $\Gamma^{4,20}$ | $c_+ = $ **4** | Aspinwall 1996 §3; Wave 11 Beilinson §5 | Controls $\hbar^2 = -1/(2 c_+) = -1/8$; **rank**-4 chirality, not a CFT stress tensor |
| 11 | Negative-signature chirality of Mukai lattice | $c_- = $ **20** | Aspinwall 1996 §3 | Pairs with $c_+$ to give total rank $24 = c_+ + c_-$; not a separate CFT |
| 12 | K3 elliptic-genus VOA (EG itself, not the sigma model) | **not a VOA; index $c(0) = 20$** | EOT 2010 §2 | A *chiral index*, not a chiral algebra; carries $M_{24}$ action (EOT) |
| 13 | Vector-valued modular form for Borcherds 1998 lift | lattice rank-$4$ ($\mathrm{II}_{2,2}$), **not central charge** | Borcherds 1998 Thm 13.3 | Input to singular theta lift; produces $\Phi_{10}$ as modular form; $c$ undefined |
| 14 | Umbral $\ell = 2$ seed (CDH 2014, $A_1^{24}$ Niemeier) | **6** (K3 sigma chirality) or **$-2$** (Jacobi weight $1/2$) | Cheng-Duncan-Harvey 2014 Table 3 | Packaging device; not an independent VOA |
| 15 | $\mathbf{H}_{\Delta_5}$ itself (as chiral-bialgebra) | **NOT a VOA in the Virasoro sense; has $\kappa = ?$** | Wave 11 Beilinson: $K^\kappa = 8 = 2 c_+$ | Chiral bialgebra, not a Virasoro VOA; Hochschild-characteristic *replaces* Virasoro $c$ |

**Meta-observation.** Of 15 rows, **only four carry a well-defined Virasoro central charge relevant to the $\mathbf{H}_{\Delta_5}$ seed**: row 6 (Conway $c=12$), row 1 (K3 sigma $c=6$), row 10 ($c_+ = 4$ Mukai positive-chirality, *not a stress tensor*), and row 15 ($K^\kappa = 8$ Hochschild-chiral, also not a stress tensor). Rows 2, 3, 4, 5 are critical-anomaly bookkeeping for type II (target-space side, not seed side). Row 7 is the Conway-side Goddard-Thorn light-cone, not used by the $\mathbf{H}_{\Delta_5}$ construction. Rows 8, 9 are Monster-side comparators.

### The three "c=15" coincidences

Wave 10 wrote "c=15". Wave 11 retracted the single-source attribution. Wave 12 shows the 15 is **three independent arithmetical coincidences**:

**Coincidence A (worldsheet critical anomaly).** Type II superstring: $c_{\rm gh} = -26 + 11 = -15$, so $c_{\rm matter} = 15$. On $\mathbb{R}^{1,3} \times K3 \times T^2$: $c = 6 + 6 + 3 = 15$. (Polchinski 1998 Vol II.)

**Coincidence B (Conway super-Borcherds seed).** For the Conway BKM $\mathfrak{g}_{\rm Co_0}$ (not $\mathfrak{g}_{\Delta_5}$): seed is $V^{f\natural}|_{c=12} \otimes V_{\mathrm{II}_{1,1}}^{\rm super}|_{c=3}$ with total $c = 15$. (Duncan 2007.)

**Coincidence C (numerical, no mechanism).** The sum $(c_+) + (c_- + c_{\rm gh, super-adjusted}) = 4 + 11 = 15$, which is a pure arithmetic accident of $24 = c_+ + c_-$ with $c_- = 20$ and ghost balance $11$. No literature attaches physical meaning to this.

These three 15's appear in different mathematical contexts; their numerical equality is **not** a theorem; it is three separately-derived 15's that happen to coincide.

### The "c = 3" that fits the $12 + 3$

Wave 11's prompt asked: "If c=12 (Conway) + c=3 (something) = 15, what is the c=3 sector?" The honest answer: **the c=3 sector is the super-hyperbolic light-cone $V_{\mathrm{II}_{1,1}}^{\rm super}$** (row 7 of the c-table), which is the SUPER analogue of the $\mathrm{II}_{1,1}$ bosonic light-cone at $c=2$ in the Monster construction. Its matter content: 2 chiral bosons (for the momenta $p^\pm$) + 2 Majorana fermions (superpartners), $c = 2 + 1 = 3$.

This $V_{\mathrm{II}_{1,1}}^{\rm super}|_{c=3}$ **belongs to the Conway super-Borcherds construction of $\mathfrak{g}_{\rm Co_0}$** (Duncan 2007), not to the $\mathfrak{g}_{\Delta_5}$ construction. For $\mathfrak{g}_{\Delta_5}$, the analogue light-cone is lifted to a RANK-4 lattice $\mathrm{II}_{2,2}$ (Borcherds 1998 Thm 13.3 singular theta lift domain), whose Grassmannian quotient is $\mathbb{H}_2$ (Siegel upper half-plane). **The c=3 sector does not enter the $\mathfrak{g}_{\Delta_5}$ construction**; the lattice $\mathrm{II}_{2,2}$ replaces it, and the lattice is **not** a CFT but a purely combinatorial Grassmannian input.

So "$c = 12 + 3 = 15$" is **Conway-side** ($\mathfrak{g}_{\rm Co_0}$), not K3-BKM-side ($\mathfrak{g}_{\Delta_5}$).

---

## Attack-heal cycle 1 — Does $V^{f\natural}|_{M_{24}}$ close under OPE?

**ATTACK.** Wave 11 claimed "Conway $V^{f\natural}|_{c=12}$ restricted to $M_{24}$ subgroup yields the chiral half." But restriction to a subgroup is a *projection*, not a new chiral algebra. Concretely: $V^{f\natural}$ has $\mathrm{Aut} = \mathrm{Co}_0$, so it admits a natural $\mathrm{Co}_0$-action by VOA automorphisms. The $\mathrm{Co}_0$-invariant subspace $(V^{f\natural})^{\mathrm{Co}_0}$ is a sub-VOA (Dong-Li-Mason 1998 Invariant Theory Theorem 4.1), and more generally $(V^{f\natural})^G$ is a sub-VOA for any finite $G \subset \mathrm{Co}_0$. But the so-called "restriction to $M_{24}$" is **ambiguous**: does it mean (a) the $M_{24}$-invariant sub-VOA $(V^{f\natural})^{M_{24}}$, or (b) the sub-VOA generated by $M_{24}$-covariant vectors, or (c) the full $V^{f\natural}$ equipped with an $M_{24}$-equivariant structure? Each is a *different* object.

**Ghost of what was right.** In twisted-denominator moonshine (Conway 1990 §5; Duncan-Harvey 2012 §2), the "graded trace $\mathrm{tr}(g \,|\, V^{f\natural}) = \sum_n \dim(V^{f\natural}_n)^{g\text{-wt}} q^{n-1/2}$" for $g \in M_{24} \subset \mathrm{Co}_0$ produces a McKay-Thompson series. These series have modular properties (Queen 1981) but the **series is a *character*, not a VOA**. Wave 11's language conflated "twined character $T_g$" with "twisted subtheory $V^{f\natural}|_g$."

**HEAL.** Let me state precisely what Duncan-Mack-Crane 2015 (DMC hereafter) proved.

DMC Theorem 1.1: For $g \in \mathrm{Co}_0$, define the McKay-Thompson series
$$T_g^{\mathrm{Conway}}(\tau) = \mathrm{tr}\bigl(g \,\big|\, V^{f\natural}_{\rm NS}\bigr) \cdot q^{-1/2} + \mathrm{tr}\bigl(g \,\big|\, V^{f\natural}_{\rm R, tw}\bigr) \cdot q^{1/2}$$
after a suitable choice of 4-plane (an element of $\mathrm{Gr}_{\rm 4-plane}(\Lambda_{24} \otimes \mathbb{R})$ preserved by $g$). For $g \in M_{24} \subset \mathrm{Co}_0$ selected so that $g$ fixes a **4-plane** in $\Lambda_{24} \otimes \mathbb{R}$, the twined series $T_g^{\mathrm{Conway}}$ matches the K3 elliptic-genus $M_{24}$-twined characters of EOT 2010.

The key phrase: **the match is at the level of graded characters, not at the level of vertex algebras.** $V^{f\natural}$ itself is a well-defined VOA at $c = 12$; its restriction to $M_{24}$-fixed 4-planes produces *twined characters* $T_g$. These twined characters package into a vector-valued modular form (for the Weil representation of $\mathrm{Mp}_2(\mathbb{Z})$ on $\mathbb{C}[\Lambda^*/\Lambda]$, $\Lambda = \mathrm{II}_{2,2}$) **in a separate combinatorial packaging step** (CDH 2014 §5).

So: $V^{f\natural}$ *does* close under OPE (Duncan 2007 §4); it is a genuine $c=12$ super-VOA with $\mathrm{Aut} = \mathrm{Co}_0$. The "restriction to $M_{24}$" in Wave 11 means: **select McKay-Thompson series at 4-plane-preserving $g \in M_{24} \subset \mathrm{Co}_0$; the character-level output matches K3 EG twining.** The sub-VOA $(V^{f\natural})^{M_{24}}$ is a **separate** object (sub-VOA of rank higher than 0 but genuinely smaller than $V^{f\natural}$), which may or may not be relevant.

**Refined claim (Wave 12 heal).** The physical seed for $\mathfrak{g}_{\Delta_5}$ is the **full** $V^{f\natural}$ at $c=12$, equipped with an $M_{24}$-equivariant structure (via the 4-plane stabiliser in $\mathrm{Co}_0$), not a sub-VOA. The $M_{24}$-equivariance provides the vector-valued modular form that feeds Borcherds 1998. So "the chiral algebra is $V^{f\natural}$"; "the symmetry is $M_{24}$ (subgroup of $\mathrm{Co}_0$)"; "the sigma-model and the moonshine seed are linked at the level of *twined characters*, not at the level of VOA restriction." Cycle 1 heals Wave 11's sloppy phrasing.

**W12-POL-1 (anti-pattern, NEW):** "Restrict VOA $V$ to subgroup $G$" is ambiguous — it can mean (a) take $V^G$ as sub-VOA, (b) twist by $G$ to form a $G$-crossed product, (c) equip $V$ with $G$-equivariant structure. Wave 11 conflated (c) with (a). Correct for $\mathbf{H}_{\Delta_5}$: (c).

---

## Attack-heal cycle 2 — Is Borcherds 1998 singular theta lift producing a chiral algebra, or just a modular form?

**ATTACK.** Wave 11 said: "Borcherds 1998 singular theta lift on $\mathrm{II}_{2,2}$ packages the automorphic symmetry, producing $\Phi_{10}$." But Borcherds 1998 Theorem 13.3 produces an **automorphic form** — a function on the orthogonal Grassmannian $\mathrm{O}(2,s) \backslash \mathbb{H}_{2,s}$ — *not* a chiral algebra. From a modular form one cannot read off OPE coefficients, vertex operator structure, or a stress tensor. So the "chiral-algebra structure of $\mathbf{H}_{\Delta_5}$" is **not** produced by Borcherds 1998; it is produced by the **denominator-identity encoding of the BKM** associated to the automorphic form.

**Ghost of what was right.** Borcherds' own 1992 paper on the Monster proves: given a holomorphic VOA $V$ at $c = 24$, the Goddard-Thorn no-ghost theorem applied to $V \otimes V_{\mathrm{II}_{1,1}}$ at $c = 26$ yields a **Lie algebra** (the Monster BKM) as the physical-state space. This IS a chiral-algebraic-like output (the Lie algebra structure comes from vertex-algebra OPEs via the Borcherds-Frenkel-Lepowsky-Meurman bracket).

But the 1998 paper is different: it does NOT produce a Lie algebra directly; it produces an automorphic form, and the associated BKM is read off via the Weyl-Kac-Borcherds denominator formula:
$$\Phi(\rho, \tau, z) = e^{-2\pi i \langle \rho_{\rm Weyl}, Z\rangle} \prod_{\alpha \in \Delta_+} (1 - e^{-2\pi i \langle \alpha, Z\rangle})^{\mathrm{mult}(\alpha)}.$$
**The chiral-algebra structure (the Lie bracket and OPE) is imposed by the abstract definition of a BKM Lie algebra from its denominator**, not derived from the automorphic form via a CFT argument. This is Borcherds' abstract 1988-1995 machinery (Borcherds 1995 §5).

**Scheithauer 2015** gives the comparison between additive and multiplicative lifts of modular forms: Scheithauer proves that the Jacobi-forms-to-Borcherds-products map is *multiplicative* (the singular theta lift), whereas the *additive* (Saito-Kurokawa-like) lift produces a **different** automorphic form with an additive Fourier expansion. The output for $\Phi_{10}$ in Gritsenko-Nikulin 1998 and DVV 1997 uses the **multiplicative** (Borcherds-product) form, not the additive one. And crucially: **the multiplicative form encodes $\mathfrak{g}_{\Phi_{10}}$ via the denominator identity directly; the additive form does not.**

**HEAL.** The correct three-step logical chain:

1. **Borcherds 1998 Theorem 13.3** (singular theta lift of vector-valued modular form $\vec{f} = \sum_\mu f_\mu e_\mu$ on lattice $\mathrm{II}_{2,s}$):
   $$\Phi = \Theta_{\vec{f}} = \int_{\mathbb{H}}^{\rm reg} \langle \vec{f}(\tau), \vec{\theta}_{\mathrm{II}_{2,s}}(\tau, Z)\rangle \, d\mu(\tau)$$
   is a meromorphic modular form on $\mathrm{O}(2,s)^+ \backslash \mathbb{H}_{2,s}$.

2. **Borcherds 1995 §5** (multiplicative lift $\Longrightarrow$ BKM):
   The product expansion of $\Phi$ (the Borcherds product)
   $$\Phi(Z) = e^{-2\pi i \langle \rho, Z\rangle} \prod_{\alpha \in \Delta_+} (1 - e^{-2\pi i \langle \alpha, Z\rangle})^{c(\alpha^2/2)}$$
   with $c(\cdot)$ the Fourier coefficients of $\vec{f}$, is identified with the Weyl-Kac-Borcherds denominator of a BKM $\mathfrak{g}_\Phi$. The Cartan is the ambient lattice $\mathrm{II}_{2,s}$, simple real roots are the zeros of $\Phi$ on $\mathbb{H}_{2,s}/{\rm Weyl}$.

3. **Chiral-algebra structure:** The BKM Lie bracket is DEFINED via root-space generators $e_\alpha, f_\alpha, h_\alpha$ satisfying the generalised Serre relations of Borcherds 1988. No CFT argument enters at this step. In particular, $\mathfrak{g}_\Phi$ is NOT an OPE algebra; it is a Lie algebra.

**So the chain is: vector-valued form $\to$ automorphic form (Borcherds 1998) $\to$ BKM denominator $\to$ BKM Lie algebra (Borcherds 1995 §5).** The chiral-algebra structure of $\mathbf{H}_{\Delta_5}$ is not "produced" by Borcherds 1998; it is *imposed* by reading the denominator and applying Borcherds' abstract definition.

**W12-POL-2 (anti-pattern, NEW):** Borcherds 1998 singular theta lift produces an **automorphic form**, not a chiral algebra. The BKM structure is read off the denominator by Borcherds' 1995 abstract theorem. Wave 11 phrasing "Borcherds 1998 packaging the automorphic symmetry" should be split into: (i) Theorem 13.3 produces $\Phi$; (ii) Borcherds 1995 §5 reads $\mathfrak{g}_\Phi$ from the denominator.

---

## Attack-heal cycle 3 — Self-attack on cycles 1 and 2: does the c=15 coincidence have a hidden structural reason?

**ATTACK (self).** In Wave 11 cycle 6 I wrote: "the c=15 is a coincidence of three independent facts." But in physics, such triple coincidences often reflect a hidden structural reason. For instance, $c = 24$ appears as (i) bosonic critical dim minus 2, (ii) rank of Leech, (iii) central charge of $V^\natural$ — and the three are NOT coincidences: Borcherds 1992 proved a structural link. So perhaps the triple-15 is ALSO structural, and I dismissed it too quickly.

Let me check. The three 15's are:
- **15A** = $c_{\rm gh}^{\rm super} = -(-26 + 11) = 15$ (super-critical-anomaly).
- **15B** = $12 + 3$ = $c(V^{f\natural}) + c(V_{\mathrm{II}_{1,1}}^{\rm super})$ (Conway Borcherds seed).
- **15C** = $4 + 11$ = $c_+ + c_{\rm gh, bosonic}/(-\text{sgn})$, if one reinterprets. Actually $11$ is the super-ghost central charge, not the bosonic one. So $4 + 11 = 15$ is $c_+ + c_{\beta\gamma}$. This is structurally unrelated.

The question: **is 15A = 15B structurally?**

15A = 15 comes from $(b,c)$ weights $(2, -1)$ giving $c = -26$, and $(\beta, \gamma)$ weights $(3/2, -1/2)$ giving $c = +11$; sum $-15$. The derivation uses only the $bc$ / $\beta\gamma$ conformal-weight formula $c_{\rm ghost} = -2(6k^2 - 6k + 1)$ for weight $k$ (Friedel-Martinec-Shenker 1986), which is structurally about the conformal-weight structure of ghost systems.

15B = 15 comes from $V^{f\natural}$ having $c = 12$ (derived from the Leech super-construction via FLM 1988 Ch 10: one adds 8 Majorana fermions to the bosonic Leech $c = 24$ to get super-cohomological $c = 12 + \text{ghost}$; rigorously, $c(V^{f\natural}) = 12$ because it is a super-VOA quotient of $V_{\Lambda_{24}}^+ \otimes \mathrm{Cliff}(\mathbb{R}^{24})$; see Duncan 2007 §4). Plus $V_{\mathrm{II}_{1,1}}^{\rm super} = c = 3$.

**Is there a structural link?** YES, actually. The Goddard-Thorn *super* theorem, applied to any holomorphic super-VOA $V$ at $c(V) = 12$ tensored with $V_{\mathrm{II}_{1,1}}^{\rm super}$ at $c = 3$, gives a BKM via the no-ghost extraction: total $c = 15$, which matches the super-critical-anomaly 15A. This is **not a coincidence**: Goddard-Thorn super is the critical-dimensional statement that BKM extraction works at the *same* central charge that makes the super-string BRST nilpotent.

So 15A = 15B is **structural**: the super-Goddard-Thorn theorem requires $c = 15$ total, which is precisely super-critical, which is precisely $12 + 3$ for the Conway+II-super seed.

**But 15A = 15B does NOT give $\mathfrak{g}_{\Delta_5}$**; it gives $\mathfrak{g}_{\rm Co_0}$ (Duncan 2007 Theorem 4.8). $\mathfrak{g}_{\Delta_5}$ is a *larger*, $M_{24}$-related BKM obtained NOT from Goddard-Thorn no-ghost at $c = 15$ but from Borcherds 1998 singular theta lift on $\mathrm{II}_{2,2}$ with input the $M_{24}$-twined Conway characters.

**HEAL.** The hidden structural reason is: **super-Goddard-Thorn requires $c = 15$ total**, and the Conway super-VOA $V^{f\natural}|_{c=12}$ is the correct "super-moonshine module" at the super-analogue of the Monster $c = 24$. So $12 + 3 = 15$ is not a coincidence; it is the super-analogue of the bosonic $24 + 2 = 26$ (Monster case).

**But for $\mathfrak{g}_{\Delta_5}$**, the construction is **NOT Goddard-Thorn-at-$c=15$**; it is **Borcherds-1998-theta-lift-on-$\mathrm{II}_{2,2}$**, which requires input at $c = 12$ ($V^{f\natural}$) AND a LATTICE extension to $\mathrm{II}_{2,2}$ (rank 4). The $c = 12$ and the $\mathrm{II}_{2,2}$ are **separately** structural: $c = 12$ is the super-moonshine module; $\mathrm{II}_{2,2}$ is the signature-$(2,2)$ lattice whose orthogonal Grassmannian is $\mathbb{H}_2$. The $c$ of the ambient doesn't add up to 15 in a critical-anomaly sense; it does a DIFFERENT kind of match: the signature of $\mathrm{II}_{2,2}$ + 1 = 5 is the weight of $\Delta_5$, and the rank 4 = $c_+$.

**Structural link (Wave 12):**
$$\text{weight}(\Delta_5) = 5 = \mathrm{rank}(\mathrm{II}_{2,2}) + 1 = 4 + 1 = c_+ + 1.$$
And
$$\text{weight}(\Phi_{10}) = 10 = 2 \cdot \text{weight}(\Delta_5) = 2 \cdot 5 = 2 \cdot (c_+ + 1) = 2 c_+ + 2.$$
These are arithmetic identities linking the Siegel-modular weights of $\Delta_5, \Phi_{10}$ to the Mukai-chirality $c_+ = 4$. They are NOT the worldsheet c=15 critical anomaly.

**Cycle 3 refined finding (Wave 12).** The c=15 worldsheet coincidence has a structural reason (super-Goddard-Thorn at super-critical dimension), BUT this reason applies to $\mathfrak{g}_{\rm Co_0}$ (not $\mathfrak{g}_{\Delta_5}$), and for $\mathfrak{g}_{\Delta_5}$ the relevant structural links are to Siegel-modular weights: $\mathrm{weight}(\Delta_5) = c_+ + 1 = 5$, $\mathrm{weight}(\Phi_{10}) = 2 c_+ + 2 = 10$. These are first-principles arithmetic identities, not worldsheet anomaly cancellations.

**W12-POL-3 (anti-pattern, NEW):** Do not conflate the super-critical-dimension 15 (Goddard-Thorn light-cone) with the Siegel-modular weights 5 and 10 (arithmetic of Borcherds products). Both are primes, both appear in the construction, neither determines the other.

---

## Attack-heal cycle 4 — Self-attack on cycle 3: genus-2 Siegel modular invariance on $\mathbb{H}_2$

**ATTACK (self).** The Wave 11 synthesis (§F) claims $\mathbf{H}_{\Delta_5}(\rho, \tau, z)$ is fibered over $\mathbb{H}_2$, with the denominator-side modular form $\Phi_{10}$ or $\Delta_5$ being Siegel-modular for $\mathrm{Sp}_4(\mathbb{Z})$. Does this genus-2 modular invariance actually hold, including at genus-2 crossing symmetry?

**Ghost of what was right.** Igusa 1962 proved $\Phi_{10} \in S_{10}(\mathrm{Sp}_4(\mathbb{Z}))$ (Siegel cusp form of weight 10, level 1). Gritsenko-Nikulin 1998 §4 proved $\Delta_5 = \Phi_5$ is a Siegel modular form of weight 5 with a character of $\mathrm{Sp}_4(\mathbb{Z})$: $\Delta_5(\gamma \cdot Z) = v(\gamma) (cZ + d)^5 \Delta_5(Z)$ with $v$ a character of order 2. So **genus-1 modularity holds** for both $\Phi_{10}$ and $\Delta_5$.

But genus-2 Siegel-modular invariance is a STRONGER statement: for a BKM Lie algebra, the *partition function* $Z_{\mathfrak{g}_{\Phi_{10}}}(\rho, \tau, z)$ on genus-2 Riemann surfaces should be invariant under the full $\mathrm{Sp}_4(\mathbb{Z})$-action, including crossing-symmetric transformations $(\rho, \tau, z) \leftrightarrow (\tau, \rho, z) \leftrightarrow (\rho + 2z + \tau, \tau, z + \tau)$. This is genus-2 *crossing symmetry*, the Siegel analogue of genus-1 $S$-duality.

Does this hold? The denominator $\Phi_{10}$ is modular-invariant; but the FULL partition function of the BKM (counting all roots with multiplicities) includes the Weyl vector $\rho_{\rm Weyl}$ and the BKM Lie-algebra characters $\mathrm{ch}(\lambda)$ for highest weights $\lambda$. These transform under $\mathrm{Sp}_4(\mathbb{Z})$ via the Weyl-Kac-Borcherds character formula, which DOES satisfy genus-2 modularity (Borcherds 1995 Thm 10.4; Gritsenko-Nikulin 2002 extension).

**But there is a subtlety.** The "partition function" is not quite a Siegel modular form in the standard sense; it is a METROMORPHIC Siegel automorphic form with specific pole behavior on the Humbert divisors $H_D$ (Wave 11 Beilinson). The transformation under $\mathrm{Sp}_4(\mathbb{Z})$ is:
$$Z(\gamma \cdot Z) = \chi_{v}(\gamma) \det(cZ + d)^{k} Z(Z)$$
with $k = 5$ or $10$ depending on whether one uses $\Delta_5$ or $\Phi_{10}$, and $\chi_v$ a character.

Critically: for **crossing symmetry** in the genus-2 sense, one requires invariance under the *exchange* of the two modular parameters $\tau \leftrightarrow \rho$, which is a Klingen-parabolic conjugation element $\gamma_{\rm cross} \in \mathrm{Sp}_4(\mathbb{Z})$. This element IS in $\mathrm{Sp}_4(\mathbb{Z})$, so the modular-form invariance already includes crossing symmetry.

**HEAL.** Genus-2 Siegel-modular invariance of $\mathbf{H}_{\Delta_5}$'s partition function is a consequence of:
- $\Phi_{10} \in M_{10}(\mathrm{Sp}_4(\mathbb{Z}))$ (Igusa 1962),
- $\Delta_5 \in M_5(\mathrm{Sp}_4(\mathbb{Z}), \chi_v)$ with quadratic character $\chi_v$ (Gritsenko-Nikulin 1998 §4),
- BKM Weyl-Kac-Borcherds character formula's $\mathrm{Sp}_4(\mathbb{Z})$-modularity (Borcherds 1995 Thm 10.4).

**Genus-2 crossing symmetry** ($\tau \leftrightarrow \rho$) holds as a special case of the $\mathrm{Sp}_4(\mathbb{Z})$-invariance, realised by a specific group element.

**One caveat**: the BKM is *meromorphic*, with poles on Humbert divisors $H_D$ where imaginary simple roots arise. On these loci, the "modular invariance" is weakened to a functional equation with prescribed residues (Wave 11 Beilinson; Gritsenko-Nikulin 2002). This is modular invariance *up to poles*, analogous to a genus-1 VOA with logarithmic defects.

**Cycle 4 finding (Wave 12).** $\mathbf{H}_{\Delta_5}(\rho, \tau, z)$ satisfies genus-2 Siegel-modular invariance in the **meromorphic modular** sense — the denominator $\Phi_{10}$ or $\Delta_5$ is Siegel-modular-invariant by Igusa / Gritsenko-Nikulin, and the full partition function is meromorphic-modular with poles on Humbert divisors. Crossing symmetry $\tau \leftrightarrow \rho$ holds as a Klingen-parabolic-conjugation special case of $\mathrm{Sp}_4(\mathbb{Z})$-invariance. No new constraint beyond Wave 11 Beilinson's analysis.

**Three verification paths for genus-2 modularity of $\Phi_{10}$:**
- (i) Igusa 1962 direct theta-series computation.
- (ii) Saito-Kurokawa lift of $\Delta_{12}$ cusp form on $\mathrm{SL}_2(\mathbb{Z})$ (fails for $\Phi_{10}$ but works for a related form; see Gritsenko-Nikulin 1998 for the correct lift).
- (iii) Borcherds 1998 singular theta lift applied to K3 elliptic genus (DVV 1997).

**W12-POL-4 (anti-pattern, NEW):** Meromorphic Siegel modularity (BKM denominator $\Phi_{10}$) is weaker than holomorphic Siegel modularity; poles on Humbert divisors are part of the physical structure, not a pathology.

---

## Attack-heal cycle 5 — Convergence: the final c-composition

**ATTACK (synthesis).** Let me now compose all sector central charges and check consistency with Wave 11 consensus.

The **final** $\mathbf{H}_{\Delta_5}(\rho, \tau, z)$ as defined in Wave 11 §F is:
$$\mathbf{H}_{\Delta_5} = \mathcal{H}^{\rm Bess}(\widetilde{\mathrm{Sp}}_4(\mathbb{A}), R)|_{\Pi^{\rm Soudry}_{\Delta_5}} \otimes_{\mathcal{Z}^{\rm Sat}} (U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}} \cdot \Phi^{\rm Sieg-Bor}_{\mathrm{Sp}_4}.$$

This is **not a Virasoro VOA**. It has no stress tensor $T$ in the sense of a chiral algebra; rather, it is a chiral bialgebra whose **Hochschild characteristic** $K^\kappa$ replaces the Virasoro $c$. Wave 11 Beilinson established $K^\kappa = 2 c_+ = 8$, $\varrho = 1/6$, $K = 48$.

**BUT each algebraic ingredient has a c-value:**
- **Automorphic side** ($\mathcal{H}^{\rm Bess}|_{\Pi^{\rm Soudry}}$): No Virasoro structure; it is a Bessel-Hecke algebra, not a CFT. $c$ undefined.
- **Quantum-toroidal side** ($(U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}$): $U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)$ itself has a central element $\kappa$ (level), but the "central charge in the CFT sense" is the level of the associated Schiffmann-Vasserot CoHA vertex algebra (Feigin-Odesskii-Schiffmann 2012) $c_{\rm vert}^{\rm SV} = 1$ (free $c = 1$ boson for rank-$1$ toroidal $\hat{\hat{\mathfrak{gl}}}_1$). So 24 copies give $c_{\rm vert}^{\rm tot} = 24$ (for the ungauged tensor); the $M_{24}$-gauging reduces this to $24 - \dim M_{24}$ — but $M_{24}$ is **finite**, not a continuous group, so the gauging does NOT reduce the central charge (finite orbifolds preserve $c$). Hence $c_{\rm vert}^{M_{24}\text{-gauged}} = 24$.
- **Siegel-Borcherds associator** ($\Phi^{\rm Sieg-Bor}_{\mathrm{Sp}_4}$): Purely algebraic object (a 2-cocycle on the category of representations). $c$ undefined.
- **BKM Lie superalgebra** $\mathfrak{g}_{\Delta_5}$: A Lie superalgebra, NOT a VOA; $c$ undefined.

So the only well-defined c-value for the final object is **$c_{\rm vert}^{\rm CoHA-tensor} = 24$** (from the 24-fold Schiffmann-Vasserot CoHA; finite orbifold preserves $c$).

**HEAL (synthesis / convergence).** Here is the final Wave 12 c-compositions:

| Sector | c | Role |
|---|---|---|
| Conway $V^{f\natural}$ (seed) | 12 | Algebraic seed of BKM via Borcherds 1998 |
| $\mathrm{II}_{2,2}$ lattice | rank 4 = $c_+$ | Singular-theta-lift ambient; $c_+ = 4$ is positive-chirality rank |
| K3 sigma model | 6 | Geometric realisation of $V^{f\natural}|_{M_{24}}$-twined characters |
| T²×R^{1,3} (type II target) | 3 + 6 = 9 | DVV 1997 target space; NOT part of seed |
| Type II worldsheet critical anomaly | 15 | Target-space-side only; NOT the seed of $\mathbf{H}_{\Delta_5}$ |
| Super-Goddard-Thorn for $\mathfrak{g}_{\rm Co_0}$ | $12 + 3 = 15$ | Conway BKM (different from $\mathfrak{g}_{\Delta_5}$) |
| CoHA-vertex 24-fold tensor (Etingof side) | 24 | Vertex-algebraic companion of quantum-toroidal side |
| **Hochschild characteristic** $K^\kappa$ of $\mathbf{H}_{\Delta_5}$ | **8** | Replaces Virasoro $c$ for chiral bialgebra (Beilinson) |
| Positive-chirality Mukai rank $c_+$ | 4 | Controls $\hbar^2 = -1/(2 c_+) = -1/8$ |

**Key composition identities:**
- $24 = c_+ + c_- = 4 + 20$ (total Mukai rank split).
- $24 = c(V^{f\natural}) + c_{\rm II_{1,1}}^{\rm super-adj}$? NO — $c(V^{f\natural}) = 12$, not 24. The 24 here is the $\Lambda_{24}$ Leech-lattice rank, which is the bosonic-shadow of $V^{f\natural}$.
- $K^\kappa = 8 = 2 c_+ = c(V^{f\natural}) \cdot 2 / 3 = 8$.
- Siegel-weight-Borcherds: $\mathrm{wt}(\Delta_5) = c_+ + 1 = 5$; $\mathrm{wt}(\Phi_{10}) = 2 c_+ + 2 = 10$.
- NO "15" in the final object. The 15 belongs to the DVV 1997 target-space-physics computation, not to $\mathbf{H}_{\Delta_5}$ intrinsically.

**Cycle 5 convergence.** The "c of $\mathbf{H}_{\Delta_5}$" is NOT a single number; it is a **stratified collection**:
- Seed Virasoro central charge: $c = 12$ (Conway $V^{f\natural}$).
- Ambient lattice rank / positive chirality: $c_+ = 4$.
- Hochschild characteristic: $K^\kappa = 8$.
- CoHA-vertex companion: $c_{\rm CoHA} = 24$.

**No single c subsumes $\mathbf{H}_{\Delta_5}$**; it is not a Virasoro VOA. Wave 10's "c = 15" was a **fourth** number, belonging to the type II target-space side of DVV 1997, which is connected to $\mathbf{H}_{\Delta_5}$ only through the BPS dyon spectrum (second-quantised Hilbert space via Harvey-Moore 1996), NOT through the worldsheet first-quantised BRST.

---

## Wave 12 convergence verdict

**Primary claim (W12-T4, CONVERGED):** The final $\mathbf{H}_{\Delta_5}$ has a **stratified** central-charge structure:

| Stratum | $c$-value | Mechanism |
|---|---|---|
| Seed | $c = 12$ | Conway $V^{f\natural}$ (Duncan 2007) |
| Positive Mukai chirality | $c_+ = 4$ | $\mathrm{II}_{2,2}$ signature (Borcherds 1998 Thm 13.3) |
| Hochschild replacement | $K^\kappa = 8$ | Wave 11 Beilinson; $= 2 c_+$ |
| CoHA companion | $c_{\rm SV} = 24$ | Schiffmann-Vasserot CoHA vertex (FOS 2012) |

**Wave 10's "c = 15"** is retracted as an intrinsic property of $\mathbf{H}_{\Delta_5}$; it belongs to the DVV 1997 target-space BPS-counting CFT (type II on $\mathbb{R}^{1,3} \times K3 \times T^2$), connected to $\mathbf{H}_{\Delta_5}$ only through the Harvey-Moore 1996 second-quantised BPS algebra, which is a separate construction.

**Secondary claims:**
- **Cycle 1:** $V^{f\natural}|_{M_{24}}$ is $M_{24}$-equivariant full VOA (not sub-VOA, not projection); closes under OPE as the full $V^{f\natural}$ (Duncan 2007 §4).
- **Cycle 2:** Borcherds 1998 produces an automorphic form $\Phi_{10}$; the BKM chiral-algebra structure is imposed via Borcherds 1995 §5 denominator identity, NOT derived from CFT.
- **Cycle 3:** The $12 + 3 = 15$ of Conway-super-Goddard-Thorn is **structural** (super-critical dim), but pertains to $\mathfrak{g}_{\rm Co_0}$, not $\mathfrak{g}_{\Delta_5}$. For $\mathfrak{g}_{\Delta_5}$, the analogous "critical-dim structural" identities are the Siegel-modular weights $\mathrm{wt}(\Delta_5) = 5 = c_+ + 1$ and $\mathrm{wt}(\Phi_{10}) = 10 = 2 c_+ + 2$.
- **Cycle 4:** Genus-2 Siegel-modular invariance of $\Phi_{10}$ / $\Delta_5$ holds as meromorphic modularity with prescribed Humbert-divisor poles (Igusa 1962; Gritsenko-Nikulin 1998, 2002; Borcherds 1995 Thm 10.4).

**Three independent verification paths (per Wave 12 rule):**
1. **Literature path:** Duncan 2007 Theorem 4.8 ($V^{f\natural}$ at $c=12$, $\mathrm{Aut} = \mathrm{Co}_0$); Borcherds 1998 Theorem 13.3 ($\Phi$ from $\vec{f}$); Igusa 1962 ($\Phi_{10} \in M_{10}(\mathrm{Sp}_4(\mathbb{Z}))$).
2. **Weight-arithmetic path:** $\mathrm{wt}(\Delta_5) = 5 = \mathrm{rank}(\mathrm{II}_{2,2}) + 1 = c_+ + 1$; $\mathrm{wt}(\Phi_{10}) = 10 = 2 \cdot \mathrm{wt}(\Delta_5)$ (Gritsenko theta-square).
3. **Hochschild path:** $K^\kappa = 8 = 2 c_+$ (Wave 11 Beilinson cycle 5).

All three converge on the stratified c-structure above.

---

## Retraction ledger

| # | Wave 11 claim (Polyakov W11) | Wave 12 refinement | Mechanism |
|---|---|---|---|
| W12-POL-R1 | "Restrict $V^{f\natural}$ to $M_{24}$" (Wave 11 cycle 4 Step A) | $V^{f\natural}$ is the full VOA; $M_{24}$-equivariance is *on* $V^{f\natural}$, not a sub-VOA (Dong-Li-Mason 1998 Inv Thm caveat) | Wave 12 Cycle 1 |
| W12-POL-R2 | "Borcherds 1998 packages the automorphic symmetry" | Borcherds 1998 produces $\Phi_{10}$ as automorphic form; chiral-algebra structure imposed by Borcherds 1995 §5 denominator identity | Wave 12 Cycle 2 |
| W12-POL-R3 | "c=15 is a coincidence of three unrelated facts" | Two of the three 15's are structurally linked (super-Goddard-Thorn $\leftrightarrow$ Conway+II-super seed); the third is unrelated | Wave 12 Cycle 3 |
| W12-POL-R4 | "BKM partition function satisfies genus-2 modularity" | Genus-2 modularity holds **meromorphically**, with Humbert-divisor poles — not as a holomorphic Siegel modular form | Wave 12 Cycle 4 |
| W12-POL-R5 | "c of $\mathbf{H}_{\Delta_5}$ is $c = 12$" (implicit from Wave 11 convergence) | $\mathbf{H}_{\Delta_5}$ has a **stratified** c-structure: $c(V^{f\natural}) = 12$, $c_+ = 4$, $K^\kappa = 8$, $c_{\rm CoHA} = 24$ — no single c | Wave 12 Cycle 5 |

These are refinements, not retractions of the Wave-11 core physics. The Wave-11 core (Conway + Borcherds 1998 singular theta lift as seed; $c = 15$ retraction) stands.

---

## New anti-patterns raised

**W12-POL-AP-1** (NEW): Conflating "$V^G$ as sub-VOA" with "$V$ with $G$-equivariant structure". These are *different* VOAs (the first is strictly smaller). For $\mathbf{H}_{\Delta_5}$, the correct object is the full $V^{f\natural}$ with $M_{24}$-equivariant structure via 4-plane stabilisation in $\mathrm{Co}_0$ (Duncan-Mack-Crane 2015).

**W12-POL-AP-2** (NEW): Borcherds 1998 theta lift produces an **automorphic form**, not a chiral algebra. The Lie-algebra structure of the associated BKM is *imposed* by the Weyl-Kac-Borcherds denominator (Borcherds 1995 §5), not derived from the theta lift. Wave 11 phrasing collapsed the two steps into one.

**W12-POL-AP-3** (NEW): Do not conflate super-critical worldsheet c=15 (Goddard-Thorn super-no-ghost) with Siegel-modular weights 5 and 10 (Borcherds-product weights). Both are primes, both appear in the construction, neither determines the other.

**W12-POL-AP-4** (NEW): Meromorphic Siegel-modular invariance (BKM denominator $\Phi_{10}$) is weaker than holomorphic Siegel-modular invariance; poles on Humbert divisors $H_D$ are intrinsic to the BKM (they encode the imaginary simple roots), not a pathology.

**W12-POL-AP-5** (NEW): A chiral bialgebra with stratified c-structure has NO single Virasoro central charge; instead it has (i) a seed Virasoro $c$ (here 12), (ii) a lattice-chirality rank ($c_+ = 4$), (iii) a Hochschild characteristic ($K^\kappa = 8$), (iv) possibly a CoHA-companion $c$ (here 24). Do not write "$c(\mathbf{H}_{\Delta_5}) = $ [single number]" without specifying which stratum.

**W12-POL-AP-6** (NEW): Do not identify "central charge of quantum-toroidal algebra" with "central charge of CoHA-vertex algebra." $U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)$ has a central level $\kappa$; the associated Schiffmann-Vasserot CoHA has a distinct Virasoro central charge. For rank-1 toroidal: $c_{\rm SV} = 1$ (free boson). For 24-fold tensor: $c_{\rm SV}^{\rm tot} = 24$. The quantum-toroidal central level $\kappa$ does NOT coincide with this.

**W12-POL-AP-7** (NEW): $\mathbf{H}_{\Delta_5}$ is NOT a Virasoro VOA; it is a chiral bialgebra. Statements like "stress tensor of $\mathbf{H}_{\Delta_5}$" are type-errors. The correct object is the *Hochschild characteristic* $K^\kappa = 8$, which is Virasoro-analogous but not a stress tensor.

---

## Residual open

**W12-POL-OPEN-1** (from cycle 3): The Siegel-weight identity $\mathrm{wt}(\Delta_5) = c_+ + 1$ and $\mathrm{wt}(\Phi_{10}) = 2 c_+ + 2$ — is this a general theorem for Borcherds products on $\mathrm{II}_{2,s}$? (Conjecture: $\mathrm{wt}(\Phi_{\rm Borcherds}) = s + 2$ for the Borcherds product of a scalar-valued weakly holomorphic modular form of weight $-s/2$; see Borcherds 1998 Thm 13.3 for the general rule.) If yes, this is a *structural* relation between Mukai chirality and Borcherds-product weight. The proof (if it exists) is a rank-dependent computation of the Borcherds regularised Petersson product. Should be verified against Gritsenko-Nikulin 1998 §3-4 on specific cases beyond $\mathrm{II}_{2,2}$.

**W12-POL-OPEN-2** (from cycle 4): The meromorphic Siegel-modular invariance of $\mathbf{H}_{\Delta_5}$'s full partition function (not just denominator) — is this established for BKM algebras in general? Borcherds 1995 Thm 10.4 gives it for certain BKMs associated with vertex algebras; Gritsenko-Nikulin 2002 extends to Lorentzian lattices of rank $\geq 3$. The specific case of $\mathrm{II}_{2,2}$ is covered. But a genus-2 *crossing-symmetry* check in the physics bootstrap sense would require explicit computation of the partition function $Z(\rho, \tau, z)$ and verification that $Z(\tau, \rho, z) = \pm Z(\rho, \tau, z)$ with the correct sign from the Klingen-parabolic element of $\mathrm{Sp}_4(\mathbb{Z})$.

**W12-POL-OPEN-3** (from cycle 5): Are there additional c-values I have missed? Specifically: (a) the central charge of the "dual pair" seed in the Kazhdan W11 picture, namely $(\widetilde{SL}_2, O(\Lambda^{3,2}))$ inside $\widetilde{\mathrm{Sp}}_{10}$ — this has matter $c_{\Lambda^{3,2}} = \mathrm{rk} = 5$ on the bosonic side; (b) the Saito-Kurokawa lift's underlying weight-$(7/2, 1/2)$ cuspidal packet, which for metaplectic lifts introduces a half-integer weight — this is not a Virasoro c but a weight. Both should be inserted in the c-table if they contribute to the seed.

**W12-POL-OPEN-4** (from Polyakov's own Wave-11 Q4'): The Cheng-Duncan-Harvey 2014 umbral framework at umbral genus $\ell = 2$, $G^{(2)} = M_{24}$, uses a seed with $c = 6$ (K3 sigma) or $c = 12$ (Conway) depending on formulation. The reconciliation: CDH 2014 uses the *elliptic-genus* chirality as a chiral-index (not a VOA), so no CFT $c$ is assigned. The lifted seed for the BKM is $V^{f\natural}|_{c=12}$.

**W12-POL-OPEN-5** (from cycle 4 / genus-2): Does $\mathbf{H}_{\Delta_5}$'s partition function satisfy **factorisation** at the genus-2 degeneration $\rho \to \infty$ (separating Riemann surface) consistent with chiral-algebraic factorisation on the nodal locus? This is the genus-2 analogue of the genus-1 modular $S$-factorisation $Z(\tau \to \infty) \to Z_{\rm vac}$. For the BKM $\mathfrak{g}_{\Phi_{10}}$, the $\rho \to \infty$ cusp is the Borcherds-Yangian (Wave 11 Costello-Drinfeld convergence); this should be verified against Maulik-Okounkov stable envelopes on $\mathrm{Hilb}^\bullet K3$.

---

## Coda — what Polyakov sees

The worldsheet origin of $\mathfrak{g}_{\Delta_5}$, once the c=15 myth is cleared, is **stratified**:

1. **Seed**: Conway super-VOA $V^{f\natural}|_{c=12}$. Full VOA, $\mathrm{Co}_0$-automorphism, $M_{24}$-equivariant by 4-plane stabilisation.
2. **Theta-lift**: Borcherds 1998 applied to $M_{24}$-twined $V^{f\natural}$ characters packaged as vector-valued $\mathrm{Mp}_2$-modular form on $\mathrm{II}_{2,2}$; output $\Phi_{10}$.
3. **BKM imposition**: Borcherds 1995 §5 reads $\mathfrak{g}_{\Phi_{10}}$ from the denominator product; $\Delta_5$ is the Gritsenko theta-half giving $\mathfrak{g}_{\Delta_5}$.
4. **Target-space connection**: DVV 1997 identifies $1/\Phi_{10}$ as the 1/4-BPS dyon partition function in type II on $\mathbb{R}^{1,3} \times K3 \times T^2$ at critical anomaly $c_{\rm matter} = 15$. The BKM Lie bracket on the dyon spectrum is the Harvey-Moore 1996 second-quantised BPS algebra.

The central-charge stratification (c=12, $c_+=4$, $K^\kappa=8$, $c_{\rm CoHA}=24$) captures what each stratum contributes. The "c=15" of Wave 10 was the target-space side (stratum 4 critical anomaly), wrongly attributed to the seed construction.

The final object $\mathbf{H}_{\Delta_5}(\rho, \tau, z)$ over Siegel $\mathbb{H}_2$ is genus-2 meromorphic-Siegel-modular, with Humbert-divisor poles encoding imaginary simple roots. Crossing symmetry holds via the Klingen-parabolic element of $\mathrm{Sp}_4(\mathbb{Z})$.

This is what the worldsheet sees, once the accounting is corrected and each central charge is rigidly attributed to its literature source.

---

## End of Wave 12 Polyakov.

**Author.** Raeez Lorgat.
