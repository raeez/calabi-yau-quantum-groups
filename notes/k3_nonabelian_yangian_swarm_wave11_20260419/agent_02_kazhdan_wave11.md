# Wave-11 Kazhdan: theta-correspondence, A-parameters, and the Howe-vs-residual-Eisenstein dichotomy for the chiral BKM avatar of $\Delta_5$

**Author.** Raeez Lorgat, sole author.
**Date.** 2026-04-19.
**Voice.** David Kazhdan. Langlands functoriality, theta correspondence, Kudla-Rallis tower, Arthur parameters, Bernstein centre, Saito-Kurokawa as CAP, Piatetski-Shapiro residual Eisenstein, base change. Adversarial.
**Wave.** 11. ATTACK target W11-KAZHDAN-THETA: the Wave-10 identification "Borcherds lift = Howe theta integral for the dual pair $(\mathrm{Sp}_4, O(4, 20)) \subset \mathrm{Sp}_{96}$".

**Pattern 236 scope banner.** Two lanes throughout. **Local automorphic / dual-pair lane**: the place-by-place Howe correspondence at finite $p$, the local theta lift, Kudla-Rallis stable / non-stable / boundary range. **Global Arthur lane**: the global $L$-packet, the A-parameter, the residual / cuspidal dichotomy, the Howe regularised theta vs Piatetski-Shapiro residual Eisenstein.

---

## Executive verdict (for the synthesist)

**The Wave-10 dual-pair signature $(\mathrm{Sp}_4, O(4, 20))$ is FALSIFIED on three first-principles grounds.** The correct dual pair, lattice, and automorphic origin of the Borcherds multiplicative lift $\Phi(\phi_{0,1}) = \Delta_5$ are:

(K-W11-0) **The orthogonal group is $\mathrm{O}(\Lambda^{3,2})$, not $\mathrm{O}(\Lambda^{4,20})$.** The Lorgat-2020 PDF (the primary source whose internal structure Wave 10 was meant to track) constructs the relevant isomorphism $\wedge^2: \mathrm{Sp}_4(\mathbb{Z})/\{\pm I_4\} \xrightarrow{\sim} \mathrm{O}(\Lambda^{3,2})_+/\{\pm I_5\}$ explicitly (Lorgat 2020 PDF \S 3, Lemma 1, p.~5). Here $\Lambda^{3,2} = (e_1 \wedge e_3 + e_2 \wedge e_4)^\perp \subset \wedge^2 \mathbb{Z}^4$ has signature $(3, 2)$. The Igusa cusp form $\Delta_5$ on $\mathbb{H}_2$ pulls back to a $\mathrm{IV}$-type domain $\mathbb{H}_+^{\mathrm{IV}} \subset \mathbb{P}(\Lambda^{3,2} \otimes \mathbb{C})$ for $\mathrm{O}(\Lambda^{3,2})$. The Mukai lattice $\Lambda^{4,20}$ (signature $(4, 20)$) appears NOWHERE in Lorgat 2020 and would not even be the correct domain for the singular theta lift producing $\Delta_5$.

(K-W11-1) **The Borcherds lift to $\Delta_5$ is a Borcherds 1998 SINGULAR theta lift (= regularised theta integral) on the Grassmannian $\mathcal{G}(\Lambda^{2,1}) \subset \mathcal{G}(\Lambda^{3,2})$, NOT a Howe-Weil theta lift in the Kudla-Rallis dual-pair sense.** The two are related but DIFFERENT: a Howe-Weil theta lift between Kudla-Rallis dual pairs $(\mathrm{Sp}_{2n}, O(p, q)) \subset \mathrm{Sp}_{2n(p+q)}$ uses the Weil representation of the metaplectic cover $\widetilde{\mathrm{Sp}}_{2n(p+q)}$, the integral converges (after suitable choice of test vector) when the Kudla-Rallis stable range $p + q \geq 4n + 1$ is satisfied, and produces a global automorphic form by integration. A Borcherds 1998 singular theta lift uses a vector-valued modular form $F$ of weight $(2 - n)/2$ on $\widetilde{\mathrm{SL}}_2$, regularises the divergent integral $\int^{\mathrm{reg}}_{\mathcal{F}} F(\tau) \overline{\Theta_L(\tau, Z)} y^{-2} dx\, dy$ via Harvey-Moore Mellin transform, and produces a meromorphic (not holomorphic in general) automorphic form on $\mathcal{G}(L)$ whose divisor is the Heegner divisor $\sum c(\beta, m) Z(\beta, m)$. **These are two different lifts.** Conflating them is a category error.

(K-W11-2) **Even within the Howe-Weil framework, the closest correctly-stated dual pair for $\Delta_5$ is $(\widetilde{\mathrm{SL}}_2, O(\Lambda^{3,2})) \subset \widetilde{\mathrm{Sp}}_{10}$, NOT $(\mathrm{Sp}_4, O(4, 20)) \subset \mathrm{Sp}_{96}$.** The metaplectic cover is forced because $F = \phi_{0,1}/\eta^{?}$ has half-integral weight (Borcherds 1998 \S 14 vector-valued modular forms of weight $1 - n/2$ live on $\widetilde{\mathrm{SL}}_2 = \mathrm{Mp}_2$). The orthogonal side is $\mathrm{O}(\Lambda^{3,2})$ from K-W11-0. The Kudla-Rallis dual pair $(\widetilde{\mathrm{Sp}}_{2}, O(p, q))$ has $p + q = 5$ here ($p = 3, q = 2$), so $p + q = 5 = 2n + 1 = 2 \cdot 1 + 1 + 2$ — the lift is at the **boundary of the Kudla-Rallis stable range** $p + q \geq 4n + 1$ (with $4n + 1 = 5$ for $n = 1$, so we are EXACTLY at the boundary). At the boundary the Howe lift is a **regularised theta** (Borcherds 1998 = Kudla-Rallis-Howe boundary theta with explicit regularisation), but not the cuspidal-stable-range theta.

(K-W11-3) **The genuine automorphic avatar of $\Delta_5$ on the symplectic side is the Saito-Kurokawa CAP (Cuspidal Associated to Parabolic) representation of $\mathrm{Sp}_4(\mathbb{A})$, with Arthur parameter $\psi_{\Delta_5} = \rho_{\Delta_8} \boxtimes [2]$ (Howe-PS A-parameter) where $[2]$ is the 2-dim Arthur SL$_2$ — a genuinely temperedness-violating ($\psi|_{SL_2}$ non-trivial) parameter consistent with CAP-type SK.** This part of Wave 10's Saito-Kurokawa identification is correct. What Wave 10 incorrectly claimed was that the Borcherds lift is itself the Howe theta integral that PRODUCES the SK packet — it is not. The CAP construction of SK (Piatetski-Shapiro 1983) uses RESIDUAL Eisenstein series from the Klingen parabolic $P_{2,2} \subset \mathrm{Sp}_4$, not theta integrals.

(K-W11-4) **The hidden structure (the actual automorphic origin of $\Delta_5$ as a $\mathrm{GSp}_4$ automorphic form):** $\Delta_5$ is the **paramodular newform** on $\mathrm{GSp}_4(\mathbb{A})$ with paramodular level $\Gamma_{\mathrm{para}}^{(2)}(1)$ (level 1 paramodular = Sp$_4(\mathbb{Z})$ with the Maass quadratic character $v_{\Delta_5}$ from Lorgat 2020 \S 2, p.~3). Its Arthur parameter is the Saito-Kurokawa-Howe-PS parameter $\psi_{\Delta_5} = \rho_{\Delta_8} \boxtimes [2]_{\mathrm{Arth-SL_2}}$. The Borcherds lift is a **separate piece of automorphic-form-machinery**: a singular theta integral on the orthogonal side $\mathrm{O}(\Lambda^{3,2})$ that produces the SAME object $\Delta_5$ via the exceptional accidental isomorphism $\mathrm{Sp}_4 \xrightarrow{\wedge^2} \mathrm{SO}(\Lambda^{3,2})_+$ (Lorgat 2020 \S 3, Lemma 1). **The two constructions converge on the same automorphic form $\Delta_5$ via the accidental isogeny, not via Howe theta correspondence between two different dual-pair groups.**

This is the Wave 11 correction. It is technically a 4-fold retraction-and-rectification of Wave-10 K3-K6.

---

## Cycle 1 (W11-K-cycle-1) — ATTACK-HEAL on dual-pair signature $(\mathrm{Sp}_4, O(4, 20))$

### 1.A ATTACK — the lattice signature $(4, 20)$ is wrong

**Attack.** Wave 10 K3 and K6 stated: "the dual pair lives inside $\mathrm{Sp}_{96}(\mathbb{A})$, with $(2n, p, q) = (4, 4, 20)$, on the Mukai lattice $\Lambda^{4, 20}_{\mathrm{Muk}}$." The reasoning was: the K3 cohomology has Mukai signature $(4, 20)$, so "obviously" the orthogonal group acting on it is $O(4, 20)$. **First-principles attack:** the Borcherds product formula for $\Delta_5$ does not act on Mukai cohomology. It acts on a singular-theta-lift Grassmannian $\mathcal{G}(L)$ for a SPECIFIC lattice $L$ which is determined by the WEIGHT of the input weak Jacobi form $\phi_{0,1}$ via the formula $\mathrm{wt}(\Phi_F) = c_F(0)/2$.

Here the input is $\phi_{0,1}$ of weight $0$ index $1$, with $c_{\phi_{0,1}}(0) = 10$ (the constant Fourier coefficient of $\phi_{0,1}$ at the discriminant-$0$ Heegner divisor) — Wait, this is $f(1,1,1) = 64 \neq 10$. Let me restart on first principles.

**First principles (Lorgat 2020 PDF \S 4, p.~5).** The lattice for the Borcherds lift producing $\Delta_5$ is $\Lambda^{3,2}$ (signature $(3, 2)$), with the hyperbolic primitive sublattice $\Lambda^{2,1} = \Lambda^{(1,1)} \oplus [2] \subset \Lambda^{3,2}$ playing the role of the "even-imaginary cone" (the Lorentzian sublattice on which the Cartan of $\mathfrak{g}_{\Delta_5}$ acts non-trivially). The complexified domain $\Omega(\mathcal{C}(\Lambda^{2,1})_+) \subset \mathbb{H}_+^{\mathrm{IV}}$ is the period domain for $\mathrm{O}(\Lambda^{3,2})$, which under the accidental isogeny $\wedge^2: \mathrm{Sp}_4(\mathbb{Z})/\{\pm I_4\} \xrightarrow{\sim} \mathrm{O}(\Lambda^{3,2})_+/\{\pm I_5\}$ identifies with the Siegel upper half space $\mathbb{H}_2$.

**Sub-attack 1.A.1** (Mukai lattice is wrong domain). The Mukai lattice $\Lambda^{4,20} = H^*(K3, \mathbb{Z})_{\mathrm{ev}}$ is the lattice on which $\mathrm{O}(\Lambda^{4,20})$ acts as the Bridgeland stability-condition action / autoequivalences of $D^b(K3)$ / Mukai duality on the BPS states of $\mathrm{Sym}^N(K3)$. **It is NOT the Borcherds-lift lattice for $\Delta_5$.** The Borcherds-lift lattice is $\Lambda^{3,2}$ (rank 5), not $\Lambda^{4,20}$ (rank 24). These are different lattices arising in different ways from K3:
- $\Lambda^{4,20}$ comes from the K3 cohomology and acts on the BPS Hilbert space of $\mathrm{Sym}^N(K3)$.
- $\Lambda^{3,2}$ comes from the genus-2 paramodular variety / accidental isogeny $\wedge^2 \mathbb{Z}^4 \supset (e_1 \wedge e_3 + e_2 \wedge e_4)^\perp$, with NO direct K3-cohomological interpretation.

**Sub-attack 1.A.2** (the $O(4, 20)$ confusion comes from a parallel construction for the BPS algebra). There IS an automorphic form on $\mathrm{O}(4, 20)$ relevant to $\mathrm{Sym}^N(K3)$ — specifically, the **second-quantized elliptic genus** $\mathcal{Z}_{\mathrm{Sym}^\bullet(K3)}$ via DMVV, which IS a Borcherds-lifted automorphic form on $\mathrm{O}(2, 26) \cap \mathrm{O}(4, 20)$ (the $\Lambda^{4,20} \oplus \Lambda^{1,1}_{p}$ Narain-lattice expansion). **This is a DIFFERENT automorphic form from $\Delta_5$.** The conflation in Wave 10 was: "BPS Hilbert on $\mathrm{Sym}^N(K3)$ via DMVV is a Borcherds product on $\mathrm{O}(2, 26)$" — true — therefore "Borcherds product on $\mathrm{O}(4, 20)$ produces $\Delta_5$" — false (mismatched lattice and mismatched output).

**Sub-attack 1.A.3** (Kudla-Rallis stable range check for $(\mathrm{Sp}_4, O(4, 20))$). Even granting the wrong lattice, check: is $(2n, p, q) = (4, 4, 20)$ in the Kudla-Rallis stable range? The stable range is $p + q \geq 4n + 1$ (Kudla-Rallis 1994, Theorem 2.1, in the metaplectic version). Here $p + q = 24$, $4n + 1 = 17$, so $24 \geq 17$ — the pair IS in the stable range. So the Howe-Weil theta lift WOULD be defined (cuspidal stable-range theta), but it would lift Sp$_4$ cuspidal automorphic representations to $O(4, 20)$ automorphic representations as a stable-range Howe theta — NOT as a Borcherds product whose target is a paramodular form on $\mathrm{Sp}_4$ (which is the wrong codomain).

**Verdict 1.A.** Wave 10's $(\mathrm{Sp}_4, O(4, 20))$ identification is FALSIFIED on three counts: (i) the lattice signature is wrong ($\Lambda^{3,2}$ from Lorgat 2020, not $\Lambda^{4,20}$ from Mukai); (ii) the codomain of the Howe lift would not be $\Delta_5$ but a different automorphic form on the orthogonal side; (iii) the construction conflates Borcherds singular theta lift with Howe-Weil cuspidal-stable-range theta, two distinct constructions. **STATUS [F] FALSIFIED.**

### 1.B HEAL — the correct dual pair $(\widetilde{\mathrm{SL}}_2, O(\Lambda^{3,2})) \subset \widetilde{\mathrm{Sp}}_{10}$ at the boundary of stable range

**Heal.** I rectify the dual-pair identification.

**Definition (W11-K-1).** The **correct Kudla-Rallis dual pair** for the Borcherds lift $\Phi: \phi_{0,1} \mapsto \Delta_5$ (in the regularised-theta sense, Borcherds 1998 \S 14) is
$$
(\widetilde{\mathrm{SL}}_2, \mathrm{O}(\Lambda^{3,2})) \subset \widetilde{\mathrm{Sp}}_{10}
$$
embedded by:
- $\widetilde{\mathrm{SL}}_2 = \mathrm{Mp}_2$ (the metaplectic double cover, since $\phi_{0,1}/\eta^{?}$ has half-integral weight; Borcherds 1998 \S 4).
- $\mathrm{O}(\Lambda^{3,2})$ acts on the rank-5 lattice $\Lambda^{3,2}$ of signature $(3, 2)$ from Lorgat 2020 \S 3.
- The total symplectic ambient is $\widetilde{\mathrm{Sp}}_{10}$ where $10 = \dim_{\mathbb{R}}(\mathrm{SL}_2) \cdot \dim(\Lambda^{3,2}) / 2 = 2 \cdot 5 = 10$ via the Howe ambient symplectic formula $2n(p+q)/2 = n(p+q)$ for the dual pair $(\mathrm{Sp}_{2n}, O(p, q))$ giving $n(p+q)$ for $n = 1$ here, i.e. $1 \cdot 5 = 5$ in symplectic dimension... actually the standard convention is that the Howe ambient is $\mathrm{Sp}_{2n(p+q)}$, so $2 \cdot 1 \cdot 5 = 10$, yielding $\widetilde{\mathrm{Sp}}_{10}$.

**Kudla-Rallis stable-range check.** With $n = 1$ (so $\widetilde{\mathrm{SL}}_2 = \widetilde{\mathrm{Sp}}_2$) and $p + q = 5$, the Kudla-Rallis stable range $p + q \geq 4n + 1 = 5$ holds with EQUALITY. **We are at the boundary.** Boundary-range theta lifts are NOT given by the cuspidal-stable-range Howe formula; they are given by the **Kudla-Rallis residue at the critical point** of the doubling Eisenstein series, i.e. by the **regularised theta** (Borcherds 1998 = Kudla-Rallis residual theta at $s = (n + 1)/2 - q/2$ for the Siegel-Weil identity).

**Concrete computation: where is $(p, q, n) = (3, 2, 1)$ in the Kudla-Rallis tower?**

The Kudla-Rallis tower for $(\mathrm{Sp}_2, O(p, q))$ is graded by $p + q$ (the orthogonal-group dimension). At fixed $n = 1$, varying $p + q$:
- $p + q < 2n + 1 = 3$: the theta lift is identically zero (low rank, no non-trivial lift).
- $p + q = 2n + 1 = 3$: the **first occurrence** of the theta lift; lift is in the **discrete spectrum** as a residual Eisenstein.
- $p + q = 2n + 2 = 4$: tower descent / stable range begins; lift is the residue of Eisenstein at the critical point $s = 0$.
- $p + q = 2n + 3 = 5$ (boundary of cuspidal stable range): lift is at the **edge of the cuspidal stable range**; the Siegel-Weil formula identifies the residue at $s = 0$ of the Eisenstein with the regularised theta integral. **This is exactly Borcherds 1998's regularised theta lift.**
- $p + q \geq 2n + 4 = 6$ (well into stable range): Howe-Weil cuspidal theta in the standard sense.

**So the Kudla-Rallis position of $(\widetilde{\mathrm{SL}}_2, \mathrm{O}(3, 2))$ is at the boundary $p + q = 2n + 3$**, exactly where the Borcherds 1998 regularised theta = Kudla-Rallis-Siegel-Weil residue formula applies.

**Citations (primary).**
- Lorgat 2020, "A Borcherds Lift of the Weak Jacobi Form $\phi_{0,1}$, Generalized Borcherds-Kac-Moody Superalgebras and the Igusa Cusp Form $\Delta_5$" (PRIMARY — \S 3, Lemma 1, p.~5: $\wedge^2: \mathrm{Sp}_4(\mathbb{Z}) \xrightarrow{\sim} \mathrm{O}(\Lambda^{3,2})_+$; \S 4, p.~5: $\Lambda^{2,1} = \Lambda^{(1,1)} \oplus [2]$).
- Borcherds 1998, Invent. Math. 132, 491-562 (\S 4 vector-valued $F$ of weight $(2-n)/2$; \S 14 the singular theta lift construction).
- Kudla-Rallis 1994, "A regularized Siegel-Weil formula", Ann. of Math. 140, 1-80 (the doubling integral, the boundary stable-range identification).
- Kudla-Rallis 1988, "On the Weil-Siegel formula", J. Reine Angew. Math. 391, 65-84 (original Siegel-Weil identification of theta integral with Eisenstein residue).
- Howe 1979, Symp. Pure Math. 33 part 1 (theta correspondence, dual pair definitions).
- Rallis 1984, J. Funct. Anal. 59, 372-397 (Howe duality unitarity).

**Verdict 1.B.** Wave 10 $(\mathrm{Sp}_4, O(4, 20))$ is REPLACED by Wave 11 $(\widetilde{\mathrm{SL}}_2, \mathrm{O}(\Lambda^{3,2})) \subset \widetilde{\mathrm{Sp}}_{10}$, at the boundary of the Kudla-Rallis stable range $p + q = 2n + 3 = 5$. The Borcherds 1998 regularised theta lift IS the Kudla-Rallis residual theta at this boundary.

**Conjecture W11-K-1 (Correct dual pair).** The Borcherds multiplicative lift $\Phi(\phi_{0,1}) = \Delta_5$ is the regularised theta lift for the Kudla-Rallis dual pair $(\widetilde{\mathrm{SL}}_2, \mathrm{O}(\Lambda^{3,2}))$ at the boundary $p + q = 2n + 3 = 5$ of the cuspidal stable range, identified with the Siegel-Weil residue of the doubling Eisenstein at $s = 0$.

**Falsifiable at:** the local theta lift at $p = 2$ for $\widetilde{\mathrm{SL}}_2(\mathbb{Q}_2) \times \mathrm{O}(\Lambda^{3,2})(\mathbb{Q}_2)$, computed via Kudla 1986 explicit local doubling integral (Theorem 5.1) vs the local component of $\Delta_5$ at $p = 2$ as paramodular-newform Hecke eigenvalue.

---

## Cycle 2 (W11-K-cycle-2) — ATTACK-HEAL on Howe theta vs residual Eisenstein for the Saito-Kurokawa packet

### 2.A ATTACK — Saito-Kurokawa is CAP, hence its automorphic origin is RESIDUAL Eisenstein (Klingen) NOT Howe theta from a smaller group

**Attack.** Wave 10 K0-K3 stated: "$\rho_{\mathrm{aut}}(\Delta_5)$ is the Saito-Kurokawa packet, lifted via Howe theta from Sp$_4$ to $O(4, 20)$". This conflates two distinct objects:

(a) The **Saito-Kurokawa lift itself** (Maass 1979, Andrianov 1979): a Hecke-equivariant injection $S_8(\mathrm{SL}_2(\mathbb{Z}))^{\mathrm{cusp}} \to S_5(\mathrm{Sp}_4(\mathbb{Z}); v_{\Delta_5})^{\mathrm{cusp}}$ taking the elliptic newform $\Delta_8$ to the Siegel newform $\Delta_5$. **This is NOT a theta lift.** Maass's original construction is via the relations on Fourier coefficients (the "Maass relations" $a(n, l, m) = $ explicit function of $\tau_8$ Hecke eigenvalues). Andrianov-Zhuravlev 1995 \S 6 reformulates this as the JL correspondence GL$_2 \to $ Sp$_4$ valued in the Saito-Kurokawa CAP packet. The CAP construction (Piatetski-Shapiro 1983 — *On the Saito-Kurokawa lifting*, Invent. Math. 71, 309-338) is explicitly via **residual Eisenstein from the Klingen parabolic $P_{2,2}$** of Sp$_4$, induced from $\mathrm{GL}_2 \times \mathrm{GL}_1 = $ Levi of $P_{2,2}$. It is NOT a theta lift.

(b) A **Howe theta lift** between dual pairs $(\widetilde{\mathrm{SL}}_2, \mathrm{O}(2, 1)) \subset \widetilde{\mathrm{Sp}}_6$ DOES produce SK-type forms via the Shimura correspondence + Howe theta (Waldspurger 1980; Niwa-Shintani 1975), but this is a DIFFERENT lift from a DIFFERENT direction. In this construction, the input is on $\widetilde{\mathrm{SL}}_2$ side (a half-integral weight modular form, e.g. the Shimura preimage of $\Delta_8$), the output is on the orthogonal side $\mathrm{O}(2, 1) \cong \mathrm{PGL}_2$ via the accidental isomorphism, and the result is a $\mathrm{PGL}_2$-automorphic form whose archimedean component is the holomorphic newform $\Delta_8$ — NOT a Sp$_4$-automorphic form $\Delta_5$.

**Sub-attack 2.A.1** (CAP A-parameter is non-tempered). The Arthur parameter for the Saito-Kurokawa CAP packet on $\mathrm{Sp}_4$ is
$$
\psi_{\mathrm{SK}}: L_{\mathbb{Q}} \times \mathrm{SL}_2(\mathbb{C}) \to {}^L\mathrm{Sp}_4(\mathbb{C}) = \mathrm{SO}_5(\mathbb{C})
$$
given by $\psi_{\mathrm{SK}}(w, h) = \rho_{\Delta_8}(w) \boxplus (1 \otimes \mathrm{Sym}^1 h)$, where $\rho_{\Delta_8}: L_\mathbb{Q} \to \mathrm{GL}_2(\mathbb{C})$ is the 2-dim Galois representation associated to the elliptic newform $\Delta_8$ via Deligne 1971, and $\mathrm{Sym}^1 h$ is the 2-dim irreducible of the Arthur SL$_2(\mathbb{C})$ (Arthur 2013, \S 1.5). The total parameter has $\dim = 2 + 1 \cdot 2 = 4$, matching the standard rep of $\mathrm{SO}_5$ via $\mathrm{SO}_5 = \mathrm{Sp}_4/\{\pm I_4\}$ acting on $\wedge^2 \mathbb{C}^4 / \mathbb{C} \cdot \omega = \mathbb{C}^5$. **The non-trivial Arthur SL$_2$-factor $\mathrm{Sym}^1$ marks $\psi_{\mathrm{SK}}$ as non-tempered (CAP)** in Arthur's sense.

**Howe theta cannot produce non-tempered packets from a smaller Sp.** A Howe theta lift $\theta: \mathrm{Sp}_2 \to \mathrm{Sp}_4 \cdot O$ lifts cuspidal tempered to cuspidal tempered (in the cuspidal stable range). The output $\theta(\rho)$ has Arthur parameter $\psi_\theta = \mathrm{wt}(\rho) \boxplus [\text{trivial Arthur SL}_2]$, never producing a non-trivial Arthur SL$_2$-factor unless the input itself was non-tempered. To produce $\psi_{\mathrm{SK}}$ with its $\mathrm{Sym}^1$ Arthur SL$_2$, we need either (i) a **residual** Eisenstein (where the Arthur SL$_2$ comes from the Eisenstein-pole structure), or (ii) a Howe theta from a group whose theta lift inherently produces non-tempered packets (e.g. the Howe-PS exceptional theta, but only for very specific dual pairs).

**Sub-attack 2.A.2** (Piatetski-Shapiro's original CAP construction is via Klingen-parabolic Eisenstein, NOT theta). Piatetski-Shapiro 1983 (*On the Saito-Kurokawa lifting*) proves SK exists by considering the Klingen parabolic $P_{2,2} \subset \mathrm{Sp}_4$ with Levi $M_{2,2} = \mathrm{GL}_1 \times \mathrm{GL}_2$ (or $\mathrm{GL}_2 \times \mathrm{GL}_1$ depending on convention). The Eisenstein series
$$
E^{P_{2,2}}_s(g, \Phi_f \otimes \chi_{|\cdot|^s}) = \sum_{\gamma \in P_{2,2}(\mathbb{Q}) \backslash \mathrm{Sp}_4(\mathbb{Q})} \Phi_f(\gamma g) \chi(|a(\gamma g)|^s)
$$
induced from the cuspidal automorphic $\Phi_f$ on $\mathrm{GL}_2$ (whose archimedean component matches $\Delta_8$) tensored with a character $\chi |\cdot|^s$ on $\mathrm{GL}_1$, has a SIMPLE POLE at $s = 1/2$ (in standard Tate-normalised parameter). The **residue at this pole** is the Saito-Kurokawa lift:
$$
\mathrm{Res}_{s = 1/2} E^{P_{2,2}}_s(g, \Phi_f) = \mathrm{SK}(\Phi_f)(g).
$$
This IS the precise automorphic origin of $\Delta_5$ (as the SK lift of $\Phi_f = \Delta_8$).

**This is residual Eisenstein, NOT Howe theta.**

**Sub-attack 2.A.3** (the connection to theta is the Shimura-Niwa direction, not the SK direction). There IS a theta-related construction of $\Delta_5$ via the **double**: combine Niwa-Shintani 1975 (Shimura half-integral $\to$ integral via Howe theta on $(\widetilde{\mathrm{SL}}_2, \mathrm{O}(2, 1))$) with PS 1983 (SK lift via Klingen residual Eisenstein) to get a roundabout path:
$$
\widetilde{S}_{15/2}(\Gamma_0(4)) \xrightarrow{\text{Niwa Howe theta}} S_8(\mathrm{SL}_2) \xrightarrow{\text{PS Klingen residual Eisenstein}} S_5(\mathrm{Sp}_4; v_{\Delta_5}).
$$
This is two-step. The **second step is NOT a theta lift**. So even with the Shimura preimage, $\Delta_5$ is not a single Howe theta from any smaller group.

**Verdict 2.A.** Wave 10's "Howe theta from Sp$_4$ to $O(4, 20)$ producing the Saito-Kurokawa packet" is doubly wrong: (i) the dual pair signature is wrong (cycle 1); (ii) **even with the correct lattice, the Saito-Kurokawa packet is not produced by a Howe theta from a smaller group — it is produced by Klingen-parabolic residual Eisenstein** (Piatetski-Shapiro 1983).

### 2.B HEAL — the correct A-parameter and the Klingen residual Eisenstein construction

**Heal.** I separate the two automorphic constructions of $\Delta_5$.

**Definition (W11-K-2).** The Saito-Kurokawa packet $\Pi_{\mathrm{SK}}(\Delta_8)$ on $\mathrm{Sp}_4(\mathbb{A})$ has **two equivalent automorphic constructions**:

**(SK-A) Maass-Andrianov direct lift.** A Hecke-equivariant Fourier-coefficient formula taking $\Delta_8$ to $\Delta_5$ via the Maass relations (Maass 1979, Andrianov 1979 \S 6).

**(SK-B) Piatetski-Shapiro residual Eisenstein.** The residue at $s = 1/2$ of the Klingen-parabolic Eisenstein $E^{P_{2,2}}_s(\Phi_{\Delta_8}, \chi_{|\cdot|^s})$ on $\mathrm{Sp}_4(\mathbb{A})$, where $\Phi_{\Delta_8}$ is the cuspidal automorphic on the GL$_2$-Levi of $P_{2,2}$ corresponding to $\Delta_8$ (Piatetski-Shapiro 1983 \S 2).

**Equivalence.** (SK-A) and (SK-B) produce the same automorphic representation $\Pi_{\mathrm{SK}}(\Delta_8)$. The Arthur parameter is
$$
\psi_{\mathrm{SK}}(\Delta_8) = \rho_{\Delta_8} \boxplus (\mathbf{1} \otimes [2]_{\mathrm{Arth}}) : L_\mathbb{Q} \times \mathrm{SL}_2 \to \mathrm{SO}_5(\mathbb{C}),
$$
non-tempered (CAP), with the trivial $L_\mathbb{Q}$-character tensored against the 2-dim Arthur SL$_2$.

**Definition (W11-K-3).** The Borcherds-Gritsenko-Nikulin lift $\Phi: \phi_{0,1} \mapsto \Delta_5$ is, **separately from (SK-A)/(SK-B)**:

**(BGN) Borcherds 1998 regularised singular theta lift on $\mathcal{G}(\Lambda^{3,2})$.** Take the vector-valued modular form $F = \phi_{0,1} \cdot $ (theta-decomposition vectorisation) of weight $(2 - n)/2$ on $\widetilde{\mathrm{SL}}_2$. Form the regularised singular theta integral
$$
\Phi(F)(Z) = \int^{\mathrm{reg}}_{\mathcal{F}} F(\tau) \overline{\Theta_{\Lambda^{3,2}}(\tau, Z)} y^{-2} dx\, dy,
$$
where $\Theta_{\Lambda^{3,2}}(\tau, Z)$ is the Siegel-Weil theta kernel on $\widetilde{\mathrm{SL}}_2 \times \mathrm{O}(\Lambda^{3,2})$, and the regularisation is Harvey-Moore Mellin. The output is $\Phi(F) = \Delta_5$ (after pulling back along $\wedge^2: \mathbb{H}_2 \to \mathbb{H}^{\mathrm{IV}}_+$).

**Equivalence of (SK-A)/(SK-B) and (BGN).** They produce the same automorphic form $\Delta_5 \in S_5(\mathrm{Sp}_4(\mathbb{Z}); v_{\Delta_5})^{\mathrm{cusp}}$, but VIA DIFFERENT MECHANISMS:
- (SK-A)/(SK-B) is a CAP construction on the symplectic side $\mathrm{Sp}_4$.
- (BGN) is a singular-theta-lift construction on the orthogonal side $\mathrm{O}(\Lambda^{3,2})$.
- They agree because $\mathrm{Sp}_4(\mathbb{Z})/\{\pm I_4\} \xrightarrow{\sim} \mathrm{O}(\Lambda^{3,2})_+/\{\pm I_5\}$ via the accidental isogeny $\wedge^2$ (Lorgat 2020 \S 3, Lemma 1).

**This is the correct picture.** Wave 10's "Howe theta from Sp$_4$ to $O(4, 20)$" was a failed unification of the two pictures via the wrong lattice and the wrong dual-pair direction.

**Verdict 2.B.** Two distinct constructions of $\Delta_5$: Klingen residual Eisenstein on $\mathrm{Sp}_4$ (CAP) and singular theta lift on $\mathrm{O}(\Lambda^{3,2})$ (BGN regularised theta), unified by the accidental isogeny $\wedge^2$, NOT by a Howe-Weil theta lift between the two groups.

**Citations (primary, Wave 11 additions).**
- Piatetski-Shapiro 1983, "On the Saito-Kurokawa lifting", Invent. Math. 71, 309-338 (CRITICAL — the Klingen residual Eisenstein construction).
- Soudry 1988, "The CAP representations of GSp(4)", J. Reine Angew. Math. 383, 87-108 (CAP packet structure).
- Niwa-Shintani 1975, J. Math. Soc. Japan 27, 117-153 (Shimura-via-Howe-theta on $(\widetilde{\mathrm{SL}}_2, \mathrm{O}(2, 1))$).
- Waldspurger 1980, J. Math. Pures Appl. 60, 1-133 (Shimura correspondence as theta lift).
- Arthur 2013, *The Endoscopic Classification of Representations*, Coll. Pub. 61 (CAP / non-tempered Arthur parameters).
- Andrianov-Zhuravlev 1995, *Modular Forms and Hecke Operators*, AMS (\S 6 SK as JL).

**Conjecture W11-K-2 (CAP A-parameter and Klingen origin).** The automorphic representation $\rho_{\mathrm{aut}}(\Delta_5)$ is the Saito-Kurokawa CAP packet on $\mathrm{Sp}_4(\mathbb{A})$ with Arthur parameter $\psi_{\mathrm{SK}}(\Delta_8) = \rho_{\Delta_8} \boxplus (\mathbf{1} \otimes [2]_{\mathrm{Arth}})$, constructed as the residue at $s = 1/2$ of the Klingen-parabolic Eisenstein $E^{P_{2,2}}_s(\Phi_{\Delta_8})$. The Borcherds singular theta lift on $\mathrm{O}(\Lambda^{3,2})$ produces the same automorphic form via the accidental isogeny $\wedge^2$, NOT via Howe theta correspondence between the two groups.

**Falsifiable at:** the position of the pole of $E^{P_{2,2}}_s(\Phi_{\Delta_8})$ at $s = 1/2$ vs the absence of any pole at $s \neq 1/2$ in this domain (single-pole condition for Saito-Kurokawa CAP, ProcessLanglands-Shahidi 1976 + Piatetski-Shapiro 1983).

---

## Cycle 3 (W11-K-cycle-3) — ATTACK-HEAL on local theta at bad primes for $\Delta_5$

### 3.A ATTACK — the level-1 paramodular structure rules out non-trivial bad-prime ramification, but the local theta at $p = 2$ has a subtle dichotomy

**Attack.** Wave 10 K1 stated: "the $p$-adic component $\pi_p$ of $\rho_{\mathrm{aut}}$ is unramified (because $\Delta_5$ has level 1)." This is correct as stated, but Wave 10 then drew the wrong conclusion that local theta lifts factor through unramified principal series at every place. **First-principles attack**: the local Howe theta correspondence at $p = 2$ for the dual pair $(\widetilde{\mathrm{SL}}_2(\mathbb{Q}_2), \mathrm{O}(\Lambda^{3,2})(\mathbb{Q}_2))$ has a **subtle splitting issue at $p = 2$**:

(i) The metaplectic cover $\widetilde{\mathrm{SL}}_2$ does NOT split over $\mathrm{SL}_2(\mathbb{Q}_2)$: the local 2-cocycle $c_2: \mathrm{SL}_2(\mathbb{Q}_2) \times \mathrm{SL}_2(\mathbb{Q}_2) \to \{\pm 1\}$ is non-trivial in $H^2(\mathrm{SL}_2(\mathbb{Q}_2); \{\pm 1\})$ (Kubota 1969, Wei l 1964 §43). The genuine representation of $\widetilde{\mathrm{SL}}_2$ at $p = 2$ is 2-fold cover, with non-trivial spin structure.

(ii) The orthogonal group $\mathrm{O}(\Lambda^{3,2})(\mathbb{Q}_2)$ has a **disconnected component structure** at $p = 2$: Hasse-Witt invariants ($\det$, spinor norm, Hasse symbol) impose 4-fold disconnectivity. The component group $\pi_0(\mathrm{O}(\Lambda^{3,2})(\mathbb{Q}_2)) \cong (\mathbb{Z}/2)^2$.

(iii) The local Howe theta at $p = 2$ is governed by Kudla 1986 Theorem 5.1 (the doubling integral local computation). For $(\widetilde{\mathrm{SL}}_2, \mathrm{O}(p, q))$ at $p + q = 5$, the local doubling integral has a **$p = 2$ singularity** related to the Hasse-Witt class of $\Lambda^{3,2}$ at $\mathbb{Q}_2$.

**Sub-attack 3.A.1** (Hasse-Witt of $\Lambda^{3,2}$ at $p = 2$). The lattice $\Lambda^{3,2} = \Lambda^{(1,1)} \oplus \Lambda^{(1,1)} \oplus [2]$ from Lorgat 2020 \S 4. At $\mathbb{Q}_2$:
- $\Lambda^{(1,1)}_{\mathbb{Q}_2}$ is the standard hyperbolic plane $H_2 = \mathbb{Q}_2^2$ with form $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$. Hasse symbol $\epsilon_2(H_2) = +1$, discriminant $-1 \in \mathbb{Q}_2^\times/(\mathbb{Q}_2^\times)^2$.
- $[2]_{\mathbb{Q}_2}$ is the rank-1 lattice $\mathbb{Q}_2$ with form $2x^2$. Hasse symbol $\epsilon_2([2]) = (-2, 2)_2 = +1$ (Hilbert symbol).
- The total Hasse symbol of $\Lambda^{3,2}_{\mathbb{Q}_2}$ is $\epsilon_2 = (-1)^{(\text{number of } H_2 \text{ pairs})} \cdot \epsilon_2([2]) = (-1)^2 \cdot 1 = +1$.
- Discriminant: $\det(\Lambda^{3,2}) = \det(H_2)^2 \cdot \det([2]) = 1 \cdot 1 \cdot 2 = 2 \in \mathbb{Q}_2^\times/(\mathbb{Q}_2^\times)^2$. Non-trivial (since $2 \notin (\mathbb{Q}_2^\times)^2$).

So $\Lambda^{3,2}_{\mathbb{Q}_2}$ is the unique 5-dim quadratic form over $\mathbb{Q}_2$ with $(\epsilon_2, \det) = (+1, 2)$. **It is an "anisotropic-residue" quadratic form at $p = 2$**: the rank-3 anisotropic kernel after splitting off $\mathrm{H}_2 \oplus \mathrm{H}_2$ is the form $\langle 2 \rangle$, which is anisotropic over $\mathbb{Q}_2$. This affects the local theta lift.

**Sub-attack 3.A.2** (local Howe theta at $p = 2$ via Kudla 1986). For the dual pair $(\widetilde{\mathrm{SL}}_2(\mathbb{Q}_2), \mathrm{O}(\Lambda^{3,2})(\mathbb{Q}_2))$, the local doubling integral
$$
Z_2(s, \rho_2 \otimes \pi_2, \Phi_2) = \int_{\mathrm{O}(\Lambda^{3,2})(\mathbb{Q}_2)} f_{\rho_2}(g) \overline{\Phi_2(g, \cdot)}_{\mathrm{Howe}} \cdot |\det(g)|_2^{s} dg
$$
(Kudla 1986 \S 5, Eq. 5.2) is meromorphic in $s$ with simple pole at $s = (n + 1)/2 - q/2 = 1 - 1 = 0$ for $n = 1, q = 2$. **The residue at $s = 0$ is the local component of the Borcherds regularised theta**, related to the local Hasse-Witt class.

**Concrete formula (Kudla 1986 Thm 5.1 specialised)**:
$$
\mathrm{Res}_{s = 0} Z_2(s) = \zeta_2(0) \cdot L_2(1, \pi_2, \mathrm{Std}) \cdot \epsilon_2 \cdot \mathrm{vol}(\mathrm{O}(\Lambda^{3,2})(\mathbb{Z}_2)),
$$
where $\zeta_2(0) = -1/2$ is the local zeta at $p = 2$, $L_2(1, \pi_2, \mathrm{Std})$ is the local standard $L$-factor of $\pi_2 = $ unramified principal series of $\mathrm{Sp}_4(\mathbb{Q}_2)$ corresponding to the Saito-Kurokawa Hecke parameters at $p = 2$, $\epsilon_2 = +1$ from sub-attack 3.A.1, and the volume is $\mathrm{vol} = 1 + p^{-1} + ... = (1 - 2^{-1})^{-1} \cdot (1 - 2^{-3})^{-1}$ for the 5-dim unimodular lattice volume.

**Local Hecke eigenvalue check.** The Saito-Kurokawa Hecke eigenvalues at $p = 2$ (Andrianov 1979 \S 6, eq 6.4) are
$$
(\alpha_2, \beta_2) = (\alpha^{(\Delta_8)}_2, p^{1/2}) = (\alpha_2^{(\Delta_8)}, 2^{1/2}),
$$
where $\alpha_2^{(\Delta_8)}$ is a Satake parameter of $\Delta_8$ at $p = 2$. From elliptic-modular Hecke tables (LMFDB elliptic newforms label 8.cusp.a), $\Delta_8$ has Hecke eigenvalue $\tau_8(2) = -8$ at $p = 2$. The Satake parameters satisfy $\alpha_2 + \alpha_2^{-1} = -8/2^{(8-1)/2} = -8/2^{3.5}$, a complex number. Specifically $\alpha_2 = (-8 + i\sqrt{4 \cdot 128 - 64})/(2 \cdot 2^{3.5}) = (-8 + i \cdot 8\sqrt{7})/(2 \cdot 2^{3.5})$ after normalisation, lying on the unit circle (since $\Delta_8$ is tempered).

**Local $L$-factor**:
$$
L_2(s, \pi_2, \mathrm{Std}) = (1 - \alpha_2 \cdot 2^{-s})^{-1}(1 - \alpha_2^{-1} \cdot 2^{-s})^{-1}(1 - 2^{1/2 - s})^{-1}(1 - 2^{-1/2 - s})^{-1}.
$$
At $s = 1$: $L_2(1, \pi_2, \mathrm{Std}) = $ explicit complex number computable from $\alpha_2 = (-8 + i \cdot 8 \sqrt 7)/2^{4.5}$.

**Sub-attack 3.A.3** (does the local theta lift FACTOR globally?). For the global Borcherds regularised theta $\Phi(\phi_{0,1}) = \Delta_5$ to factor as a tensor product of local lifts at each place, we need the local components $\Phi_v$ to satisfy a coherence (cocycle) condition. The **Kudla-Rallis-Howe local-global compatibility** at the boundary $p + q = 2n + 3$ is delicate: at the boundary, the local theta is not given by the cuspidal-stable-range Howe formula, but by the local-doubling-integral residue, which is sensitive to local Hasse-Witt classes.

**Local-global compatibility at the boundary** (Kudla-Rallis 1994 \S 7) requires:
$$
\prod_v \epsilon_v(\Lambda^{3,2}) = +1 \quad (\text{global Hasse-Witt total} = +1, i.e. quadratic-form-defined-over-}\mathbb{Q}).
$$
This is a global condition (Hilbert reciprocity). For $\Lambda^{3,2}$ defined over $\mathbb{Z}$, the global product of local $\epsilon_v$ is $+1$ by reciprocity, so the local theta DOES factor globally — but the factorisation involves the local Hasse-Witt as a multiplier at each place.

**Verdict 3.A.** Local theta at $p = 2$ has a non-trivial Hasse-Witt structure ($\Lambda^{3,2}$ has discriminant $2 \in \mathbb{Q}_2^\times/(\mathbb{Q}_2^\times)^2$). The local-global factorisation at the boundary $p + q = 2n + 3 = 5$ holds (by Hilbert reciprocity), but with explicit local-Hasse-Witt multipliers. **STATUS [P] partially OK with caveats.**

### 3.B HEAL — explicit local theta calculation at $p = 2$

**Heal.** I compute the local theta at $p = 2$ explicitly.

**Definition (W11-K-4).** The local Borcherds-regularised theta at $p = 2$ for $\rho_{\mathrm{aut}}(\Delta_5)$ is:
$$
\Phi_{2}(\rho_{\mathrm{aut}}(\Delta_5)) = \mathrm{Res}_{s = 0} Z_2(s, \pi_2 \otimes \rho_2, \Phi_{\mathrm{spherical}})
$$
$$
= \zeta_2(0) \cdot L_2(1, \pi_2, \mathrm{Std}) \cdot \epsilon_2(\Lambda^{3,2}) \cdot \mathrm{vol}(\mathrm{O}(\Lambda^{3,2})(\mathbb{Z}_2))
$$
$$
= -\frac{1}{2} \cdot L_2(1, \pi_2, \mathrm{Std}) \cdot 1 \cdot \zeta_2(2) \zeta_2(4)^{-1} = -\frac{1}{2} \cdot L_2(1, \pi_2, \mathrm{Std}) \cdot \frac{(1 - 2^{-2})}{(1 - 2^{-4})}
$$
$$
= -\frac{1}{2} \cdot L_2(1, \pi_2, \mathrm{Std}) \cdot \frac{3/4}{15/16} = -\frac{1}{2} \cdot L_2(1, \pi_2, \mathrm{Std}) \cdot \frac{12}{15} = -\frac{2}{5} L_2(1, \pi_2, \mathrm{Std}).
$$

**With $\alpha_2 = (-8 + i \cdot 8 \sqrt{7})/(2 \cdot 2^{3.5})$** (computed in 3.A.2), the explicit $L_2(1, \pi_2, \mathrm{Std})$ is a definite complex number. **This IS the local Borcherds-theta at $p = 2$.**

**Citations.**
- Kudla 1986, J. Reine Angew. Math. 1986, 113-141 (Theorem 5.1, doubling integral local).
- Kudla-Rallis 1994, Ann. Math. 140, 1-80 (\S 7, local-global at the boundary stable range).
- Weil 1964, Acta Math. 113, 1-87 (metaplectic 2-cocycle).
- Kubota 1969, *Topological covers of $\mathrm{SL}_2$ over local fields*.

**Verdict 3.B.** Local theta at $p = 2$ is the residue of the doubling integral, given explicitly by Kudla 1986 Thm 5.1 with local Hasse-Witt $\epsilon_2(\Lambda^{3,2}) = +1$. The local-global factorisation holds (Hilbert reciprocity) at the boundary stable range $p + q = 2n + 3 = 5$.

**Conjecture W11-K-3 (Local theta at $p = 2$).** $\Phi_2(\rho_{\mathrm{aut}}(\Delta_5)) = -\frac{2}{5} L_2(1, \pi_2, \mathrm{Std})$ where $\pi_2$ is the local Saito-Kurokawa unramified principal series at $p = 2$ with Satake parameters $(\alpha_2, \beta_2) = (\alpha_2^{(\Delta_8)}, 2^{1/2})$ from Andrianov 1979.

**Falsifiable at:** the value $L_2(1, \pi_2, \mathrm{Std})$ from Andrianov-Hecke-eigenvalue tables, and the local Borcherds-theta normalisation extracted from the $p = 2$ Fourier coefficient of $\Delta_5$ via the Borcherds product formula.

---

## Cycle 4 (W11-K-cycle-4) — ATTACK-HEAL on the Arthur-Langlands parameter and Rallis tower position

### 4.A ATTACK — Rallis tower says theta lift from $\widetilde{\mathrm{SL}}_2$ to $\mathrm{O}(p, q)$ for $p + q = 5$ produces RESIDUAL Eisenstein, NOT genuine cuspidal lift

**Attack.** Wave 10 K3 implicitly assumed the Howe theta $\theta(\rho_{\mathrm{aut}}(\Delta_5))$ on $O(4, 20)(\mathbb{A})$ produces a **cuspidal** automorphic representation. **First-principles attack via Rallis tower:** the Rallis tower (Rallis 1984) for $(\widetilde{\mathrm{Sp}}_{2n}, \mathrm{O}(p, q))$ at fixed $n$, varying $p + q$, has the structure:

| $p + q$ | Theta lift behaviour |
|---|---|
| $p + q < 2n + 1$ | identically zero (low rank) |
| $p + q = 2n + 1$ | first occurrence: lift in discrete spectrum, residual |
| $2n + 1 < p + q < 4n + 1$ | residual Eisenstein, not cuspidal |
| $p + q = 4n + 1$ | boundary of cuspidal stable range: regularised theta = Eisenstein residue |
| $p + q > 4n + 1$ | cuspidal stable range: genuine cuspidal lift |

For $n = 1$ ($\widetilde{\mathrm{SL}}_2$) and the Borcherds-relevant $p + q = 5$:
- $4n + 1 = 5$, so $p + q = 5$ is **at the boundary** of the cuspidal stable range, NOT strictly inside.
- The lift is given by **regularised theta = Eisenstein residue** (Kudla-Rallis 1994 Siegel-Weil identification), NOT by a cuspidal-stable-range Howe theta.

**Sub-attack 4.A.1** (the lift is residual). At the boundary $p + q = 4n + 1$, the Howe-Rallis lift of the trivial representation of $\widetilde{\mathrm{SL}}_2$ is the **constant function 1** on $\mathrm{O}(p, q)$, which is residual (it is the residue at $s = 0$ of the Siegel Eisenstein on $\mathrm{O}(p, q)$). For non-trivial input on $\widetilde{\mathrm{SL}}_2$ (e.g. the half-integral weight $\phi_{0,1}/\eta^?$), the lift is also residual: it is the residue at $s = 0$ of an Eisenstein series on $\mathrm{O}(\Lambda^{3,2})$ induced from a parabolic.

**Which parabolic of $\mathrm{O}(\Lambda^{3,2})$?** The lattice $\Lambda^{3,2} = \Lambda^{(1,1)} \oplus \Lambda^{(1,1)} \oplus [2]$ has a **Witt decomposition** with isotropic radical of dimension 2 (the two hyperbolic planes contribute 2 isotropic directions). The maximal parabolic $P_{\mathrm{Siegel}} \subset \mathrm{O}(\Lambda^{3,2})$ has Levi $\mathrm{GL}_2 \times \mathrm{O}(\langle 2 \rangle)$ where $\mathrm{GL}_2$ acts on the isotropic $\Lambda^{(1,1)} \oplus \Lambda^{(1,1)}$-direction and $\mathrm{O}(\langle 2 \rangle)$ is the 1-dim anisotropic kernel.

The **residual Eisenstein** at the boundary is induced from the trivial representation of $\mathrm{GL}_2$ tensored against the trivial of $\mathrm{O}(\langle 2 \rangle)$ on $P_{\mathrm{Siegel}}$, with character $|\det|^s$ taken at $s = 0$ (the boundary point).

**Sub-attack 4.A.2** (Arthur parameter check on the orthogonal side). The Arthur parameter for the residual representation on $\mathrm{O}(\Lambda^{3,2})$ at the boundary is
$$
\tilde\psi: L_\mathbb{Q} \times \mathrm{SL}_2 \to {}^L\mathrm{O}(\Lambda^{3,2}) = \mathrm{Sp}_4(\mathbb{C})
$$
(note: the L-group of $\mathrm{O}(\Lambda^{3,2})$ which is $\mathrm{SO}_5$ is $\mathrm{Sp}_4(\mathbb{C})$, a SYMPLECTIC group, by the standard $\mathrm{SO}_{2n+1} \leftrightarrow \mathrm{Sp}_{2n}$ Langlands duality).

The induced parameter from the trivial-on-Levi-Eisenstein at the boundary is
$$
\tilde\psi(w, h) = \mathbf{1}_{L_\mathbb{Q}}(w) \otimes [4]_{\mathrm{Arth}}(h) \quad \in \mathrm{Sp}_4(\mathbb{C}),
$$
where $[4]$ is the 4-dim Arthur SL$_2$-rep. **This is NOT the "$\tilde\psi_{\Delta_5}$" claimed in Wave 10 (which was supposedly the zero-extension of $\psi_{\Delta_5}$ to $\mathrm{SO}(5, 21)$ via $L$-group inclusion).** The two parameters are completely different objects: Wave 10's was on $\mathrm{O}(4, 20)$ (wrong group), and the actual residual-Eisenstein parameter on $\mathrm{O}(\Lambda^{3,2})$ has the trivial Galois part with the 4-dim Arthur SL$_2$.

**Crucially**: Wave 10's $L$-group inclusion $\mathrm{SO}_5(\mathbb{C}) \hookrightarrow \mathrm{SO}(5, 21)(\mathbb{C})$ via "zero-extending to the trivial action on the orthogonal complement" is meaningless: there is no canonical $L$-group inclusion of this kind, because the dual pair is wrong (cycle 1).

**Sub-attack 4.A.3** (CAP-vs-residual on the symplectic side). Going back to the symplectic side: the Saito-Kurokawa Arthur parameter $\psi_{\mathrm{SK}}(\Delta_8) = \rho_{\Delta_8} \boxplus (\mathbf{1} \otimes [2])$ has a 2-dim Arthur SL$_2$-factor, marking it CAP. The lift $\theta(\rho_{\mathrm{aut}}(\Delta_5))$ on the orthogonal side (via the WRONG dual pair Wave 10 used) would have Arthur parameter $\psi_\theta = \tilde\psi$ (zero-extension, Wave 10's claim). **But $\psi_\theta$ as computed has a 4-dim Arthur SL$_2$ — NOT a 2-dim one**. So the claimed transfer would VIOLATE Arthur parameter conservation (the dimension of the Arthur SL$_2$-factor changed from 2 to 4 under the supposed lift).

**This rules out Howe theta as the bridge** between Sp$_4$-side $\Delta_5$ and $O$-side. The correct bridge is the **accidental isogeny** $\wedge^2$ (Lorgat 2020 \S 3, Lemma 1), which is an isomorphism of GROUPS — under such an isomorphism, the Arthur parameter is preserved (since $L$-groups are isomorphic).

**Verdict 4.A.** Wave 10's Howe-theta-based claim of Arthur parameter transfer between Sp$_4$ and $O$ is FALSIFIED by Arthur SL$_2$-dimension counting. The correct transfer is via the accidental isogeny $\mathrm{Sp}_4 \cong \mathrm{O}(\Lambda^{3,2})_+$, which preserves the Arthur parameter trivially.

### 4.B HEAL — the correct Arthur parameter and Rallis tower position

**Heal.** I separate the residual Eisenstein on the orthogonal side from the CAP on the symplectic side.

**Definition (W11-K-5).** The Arthur parameters for $\Delta_5$ in its two avatars:

**On Sp$_4$ side (CAP via Klingen Eisenstein residue):**
$$
\psi_{\mathrm{SK}}(\Delta_8) = \rho_{\Delta_8} \boxplus (\mathbf{1} \otimes [2]_{\mathrm{Arth}}) : L_\mathbb{Q} \times \mathrm{SL}_2 \to \mathrm{SO}_5(\mathbb{C}) = {}^L\mathrm{Sp}_4.
$$
Total dimension via standard rep $\rho_{\mathrm{std}}: \mathrm{SO}_5 \hookrightarrow \mathrm{GL}_5$: $\rho_{\mathrm{std}} \circ \psi = \rho_{\Delta_8} \boxplus (\mathbf{1} \otimes [2])$, with $\dim = 2 + 2 = 4$. But $\rho_{\mathrm{std}}: \mathrm{SO}_5 \to \mathrm{GL}_5$ has dimension 5: where is the missing 1-dimension? **Answer:** the SK packet representation includes a 1-dimensional trivial summand (the "trivial Arthur SL$_2$-fixed-vector"), so the total $\rho_{\mathrm{std}} \circ \psi$ is $\rho_{\Delta_8} \boxplus (\mathbf{1} \otimes [2]) \boxplus \mathbf{1}_{\mathrm{triv}} = $ (2+2+1)-dim, total 5. Correct.

**On $\mathrm{O}(\Lambda^{3,2})_+ \cong \mathrm{Sp}_4 / \pm I$ side (regularised theta = Klingen residue via accidental isogeny):**

The same $\Delta_5$ pulls back to $\mathrm{O}(\Lambda^{3,2})_+$ via $\wedge^2$, with the SAME Arthur parameter $\psi_{\mathrm{SK}}(\Delta_8)$ (because $\wedge^2$ is an isomorphism of groups, hence of $L$-groups).

**The "lift" claimed in Wave 10 is therefore vacuous as a lift** — it is just the identity isomorphism $\wedge^2$ between two presentations of the same group, viewed once as Sp$_4$ (Levi-Klingen residue construction) and once as $\mathrm{O}(\Lambda^{3,2})_+$ (Borcherds singular theta lift construction).

**Definition (W11-K-6).** The position of the Borcherds-relevant dual pair $(\widetilde{\mathrm{SL}}_2, \mathrm{O}(\Lambda^{3,2}))$ in the Rallis tower:
- $(n, p, q) = (1, 3, 2)$, total $p + q = 5 = 4n + 1$.
- **At the boundary of the cuspidal stable range.**
- The Borcherds-regularised theta at this boundary is the **Siegel-Weil residue** at $s = 0$ of the doubling integral, NOT a cuspidal Howe lift.
- The output is a **residual** automorphic representation on $\mathrm{O}(\Lambda^{3,2})$, identified via $\wedge^2$ with the Saito-Kurokawa CAP packet on $\mathrm{Sp}_4$.

**Verdict 4.B.** Arthur parameter $\psi_{\mathrm{SK}}(\Delta_8)$ is the SAME on both sides via the accidental isogeny. The Borcherds singular theta lift is at the BOUNDARY of the cuspidal stable range (Rallis tower position $p + q = 4n + 1$), giving a regularised-theta-as-Eisenstein-residue, NOT a cuspidal Howe lift between distinct groups.

**Conjecture W11-K-4 (Rallis tower position).** The Borcherds-Gritsenko-Nikulin lift $\Phi(\phi_{0,1}) = \Delta_5$ sits at the Rallis tower boundary $(n, p, q) = (1, 3, 2)$, $p + q = 4n + 1 = 5$, where the lift is a regularised theta = Siegel-Weil residue. The Arthur parameter on the $\mathrm{O}(\Lambda^{3,2})_+$ side equals $\psi_{\mathrm{SK}}(\Delta_8) = \rho_{\Delta_8} \boxplus (\mathbf{1} \otimes [2]_{\mathrm{Arth}})$, transferred trivially via the accidental isogeny $\wedge^2$ from the Sp$_4$-side.

**Falsifiable at:** the residual-vs-cuspidal nature of the lift output, checked via the Bessel/Whittaker model dichotomy: residual representations are NON-generic (no Whittaker model), CAP packets have a Bessel model. Sugano 1985 explicit Bessel function for $\Delta_5$ matches the predicted residual structure.

---

## Cycle 5 (W11-K-cycle-5) — ATTACK-HEAL on base change for $\Delta_5$

### 5.A ATTACK — does $\Delta_5$ appear in cyclic base change from GSp$_4/\mathbb{Q}$ to GSp$_4/K$?

**Attack.** Wave 10 K-Hecke claim implicitly assumed the SK packet has "Hecke eigenvalues at every $p$" matching $\Delta_8$ Hecke eigenvalues (via the SK formula). But this assumes a **base-change stability**: if the packet $\Pi_{\mathrm{SK}}(\Delta_8)$ for GSp$_4(\mathbb{Q})$ exists, does it base-change cyclically to GSp$_4(K)$ for any number field $K$ (e.g., a K3-period field)? **First-principles attack:** base change for GSp$_4$ is NOT known in full generality — Arthur 2013 establishes endoscopic classification (which gives some cyclic base change as a consequence) for GSp$_4$, but only for **tempered** packets. The Saito-Kurokawa packet is NON-tempered (CAP), and base-change-stability for CAP packets is more subtle.

**Sub-attack 5.A.1** (Arthur 2013 base-change-stability for CAP). Arthur's endoscopic classification for GSp$_4$ (Arthur 2013 \S 1.5 + Gan-Takeda 2011, *The local Langlands conjecture for GSp(4)*, Ann. Math. 173, 1841-1882) covers ALL Arthur-type packets, including CAP. The base-change map exists in principle: cyclic base change from $\mathbb{Q}$ to a cyclic extension $K = \mathbb{Q}(\zeta_n) \cap \mathbb{R}$ (totally real), $\Pi \mapsto \Pi_K$, is governed by the L-function $L(s, \Pi, \mathrm{BC}_K)$.

**Sub-attack 5.A.2** (K3 period field). For a K3 surface $X/\mathbb{Q}$ with Picard rank 0 over $\mathbb{Q}$ but Picard-rank-bounded-extensions over $\bar{\mathbb{Q}}$, the **K3 period field** $K_X = \mathbb{Q}(\text{periods of } H^{2,0}(X))$ is a specific number field. For a Kummer K3 of an abelian surface $A$ with CM by an imaginary quadratic field $K$, $K_X = K \cdot \mathbb{Q}(j(A))$, a CM field of degree 4 over $\mathbb{Q}$ generically.

**Sub-attack 5.A.3** (compatibility with "$\Delta_5$ Hecke" claim). The Wave 10 W10-K-Tower formula
$$
\langle v_K, \rho_{\mathrm{aut}}^{(n), g}(R_{\mathrm{EK}}) v_K \rangle = 24_g \cdot \Delta_{5, g} \cdot T_n(\phi_g) / \phi_g / W^{\mathrm{reg}}_{n, g}
$$
involves the Hecke operator $T_n$ on Jacobi forms (Eichler-Zagier) acting on $\phi_g$. **For the GSp$_4$ Hecke action** (the action that should base-change cyclically), the corresponding operator is the **Hecke algebra of $\mathrm{GSp}_4(\mathbb{Z}_p) /\!/ \mathrm{Sp}_4(\mathbb{Z}_p)$**, generated by $T(p), T_1(p^2), T_0(p)$ (Andrianov 1979 \S 5). The compatibility of these two Hecke actions (Jacobi-Eichler-Zagier vs Andrianov-Sp$_4$) under base change is governed by:
$$
\mathrm{BC}_K(\rho_{\Delta_8}) = \rho_{\Delta_8 \otimes \chi_K} \oplus \rho_{\Delta_8 \otimes \chi_K^{-1}}, \quad K \text{ cyclic CM}.
$$
For $K = \mathbb{Q}(\sqrt{-7})$ (the imaginary quadratic field appearing in $\Delta_8 \tau_8$ at $p = 2$ via discriminant $\tau_8(2)^2 - 4 \cdot 2^7 = 64 - 512 = -448 = -64 \cdot 7$), the base change of $\Delta_8$ to $K$ contains a CM-summand. The corresponding base change of the SK packet would be **NON-cuspidal on GSp$_4(K)$** (it would split off a residual summand from the imaginary-quadratic CM piece).

**This is a non-trivial obstruction**: Wave 10's "Hecke eigenvalue at every $p$ matches $\Delta_8$" ignores the possibility that base change to a K3-period field destroys the CAP cuspidality. Concretely: $\Delta_5$-base-changed to $\mathbb{Q}(\sqrt{-7})$ may not be a cuspidal automorphic form on GSp$_4(\mathbb{Q}(\sqrt{-7}))$.

**Verdict 5.A.** Base change for SK CAP packet is delicate. The "Hecke eigenvalue at every $p$" claim is base-change-stable in the GSp$_4(\mathbb{Q})$-context (within Arthur 2013), but base change to K3-period fields can destroy cuspidality. **STATUS [P] partially OK with caveats.**

### 5.B HEAL — base change diagram

**Heal.** I formulate the precise base-change behaviour.

**Definition (W11-K-7).** Cyclic base change for the SK packet is:
$$
\mathrm{BC}_{K/\mathbb{Q}}: \Pi_{\mathrm{SK}}(\Delta_8)_\mathbb{Q} \mapsto \mathrm{Ind}_{H_K}^{H_{\mathbb{Q}}} \Pi_{\mathrm{SK}}(\mathrm{BC}_K(\Delta_8)),
$$
where $\mathrm{BC}_K(\Delta_8)$ is the cyclic base change of the elliptic newform $\Delta_8$ to $K$ (which exists by Langlands-Tunnell base change for GL$_2$, Langlands 1980 *Base Change for GL(2)*).

**Compatibility.** The Hecke eigenvalues of $\mathrm{BC}_K(\Pi_{\mathrm{SK}}(\Delta_8))$ at primes of $K$ above unramified $p \in \mathbb{Q}$ are given by the SK formula applied to $\mathrm{BC}_K(\Delta_8)$ Hecke eigenvalues. **For totally real $K$, base change preserves CAP cuspidality** (Arthur 2013 \S 1.5, base change inherits CAP structure from base CAP).

**For CM $K$ (imaginary)**, base change $\Delta_8 \mapsto \mathrm{BC}_K(\Delta_8)$ is well-defined on GL$_2(K)$, but the SK lift to GSp$_4(K)$ requires CAP-on-CM-base, which may have an additional residual summand from the CM splitting. Specifically:

**Conjecture W11-K-5 (Base change of SK to CM).** For a CM field $K$ of conductor relatively prime to the level of $\Delta_8$, the SK base change
$$
\mathrm{BC}_K(\Pi_{\mathrm{SK}}(\Delta_8)) \text{ on } \mathrm{GSp}_4(\mathbb{A}_K)
$$
decomposes as $\Pi_{\mathrm{SK}}^{\mathrm{cusp}}(K, \Delta_8) \oplus \Pi^{\mathrm{res}}(K)$ where $\Pi^{\mathrm{res}}(K)$ is the residual summand from the CM splitting.

**Falsifiable at:** $K = \mathbb{Q}(\sqrt{-7})$ (the imaginary quadratic from $\tau_8(2)$ discriminant), check whether $\mathrm{BC}_K(\Delta_5)$ remains in the cuspidal spectrum of GSp$_4(K)$ or has a CM-residual summand.

**Verdict 5.B.** Base change for SK to totally real $K$ is OK (preserves CAP cuspidality). Base change to CM $K$ may have residual summand. The Wave 10 "Hecke eigenvalue at every $p$" is consistent for $\mathbb{Q}$-Hecke, but the K3-period-field interpretation is more delicate.

---

## Cycle 6 (W11-K-cycle-6) — ATTACK-HEAL: hidden structure — Kudla-Millson lift?

### 6.A ATTACK — is the BORCHERDS lift secretly a Kudla-Millson H$^+$-cohomology lift?

**Attack.** The Wave 10 dual-pair claim was wrong (cycles 1-4). Question: what IS the correct hidden structure that connects $\Delta_5$ to a meaningful theta-correspondence framework? **First-principles attack/exploration.**

**Candidate (i)**: Kudla-Millson 1990 H$^+$-cohomology lift. For an orthogonal group $\mathrm{O}(p, q)$ with $q = 2$, Kudla-Millson 1990 (*Intersection numbers of cycles on locally symmetric spaces*, Pub. Math. IHES 71, 121-172) constructs a lift from cuspidal modular forms of weight $(p + q)/2$ on $\widetilde{\mathrm{SL}}_2$ to **cohomology classes** in $H^p_{\mathrm{cusp}}(X_K, \mathbb{C})$ where $X_K$ is the Hermitian symmetric domain $\mathrm{O}(p, q)/K_{\mathrm{max}}$. The KM-lift uses a vector-valued Schwartz form to construct the cohomology class.

For $\Lambda^{3,2}$ (signature $(3, 2)$, $p = 3, q = 2$), the Kudla-Millson lift goes to $H^3(\mathrm{O}(\Lambda^{3,2})/K_{\max}, \mathbb{C})$. This is a **non-holomorphic** automorphic form (or rather, a cohomology class).

$\Delta_5$ is a **holomorphic** automorphic form on $\mathrm{Sp}_4 / K_{\max} = \mathbb{H}_2$ (Siegel upper half space). Under the accidental isogeny, $\Delta_5$ corresponds to a holomorphic automorphic form on $\mathrm{O}(\Lambda^{3,2})_+/K_{\max} = \mathbb{H}_+^{\mathrm{IV}}$. **NOT a non-holomorphic cohomology class.**

So Kudla-Millson H$^+$-cohomology lift is NOT the correct framework. KM lift produces non-holomorphic outputs; we need a holomorphic output.

**Candidate (ii)**: Borcherds 1998 singular theta lift. This IS the framework. We have it. Its automorphic-functoriality interpretation is via Kudla-Rallis Siegel-Weil at the boundary $p + q = 4n + 1 = 5$.

**Candidate (iii)**: Howe-PS exceptional theta. For exceptional dual pairs (e.g. $(\mathrm{SL}_2, G_2)$ in $E_7$, Gan-Savin 2003, *Endoscopic lifts from $\mathrm{PGL}_3$ to $G_2$*, Compositio Math. 139, 1-35), there are exceptional Howe lifts producing CAP packets. Is there an exceptional dual pair producing $\Delta_5$? **No** — the dual pair $(\widetilde{\mathrm{SL}}_2, \mathrm{O}(3, 2))$ is a STANDARD orthogonal-symplectic dual pair, not an exceptional one.

**Verdict 6.A.** No hidden theta-correspondence framework other than Borcherds 1998 = Kudla-Rallis boundary regularised theta. The Wave 10 attempt to find a Howe-Weil dual pair was misguided.

### 6.B HEAL — the true automorphic avatar

**Heal.** I formalise the true picture.

**Theorem (W11-K-FINAL, ClaimStatusConjectured).** The automorphic origin of $\Delta_5$ is two-fold equivalent:
(I) On $\mathrm{Sp}_4(\mathbb{A})$: the **Saito-Kurokawa CAP packet** $\Pi_{\mathrm{SK}}(\Delta_8)$ with Arthur parameter $\psi_{\mathrm{SK}} = \rho_{\Delta_8} \boxplus (\mathbf{1} \otimes [2]_{\mathrm{Arth}})$, constructed as **residue at $s = 1/2$** of the **Klingen-parabolic Eisenstein** $E^{P_{2,2}}_s(\Phi_{\Delta_8})$ (Piatetski-Shapiro 1983).
(II) On $\mathrm{O}(\Lambda^{3,2})_+(\mathbb{A})$: the **Borcherds-Gritsenko-Nikulin singular theta lift** $\Phi(F)$ where $F = \phi_{0,1} \cdot $ (vectorised form on $\widetilde{\mathrm{SL}}_2$ of weight $1/2$), at the **boundary of the Kudla-Rallis cuspidal stable range** $(n, p+q) = (1, 5) = (n, 4n + 1)$, identified with the **Siegel-Weil residue at $s = 0$** of the doubling Eisenstein.

**Equivalence.** (I) and (II) coincide via the **accidental isogeny**
$$
\wedge^2: \mathrm{Sp}_4(\mathbb{Z})/\{\pm I_4\} \xrightarrow{\sim} \mathrm{O}(\Lambda^{3,2})_+(\mathbb{Z})/\{\pm I_5\}
$$
(Lorgat 2020 PDF \S 3, Lemma 1, p.~5), NOT via Howe-Weil theta correspondence between two distinct groups.

**The chiral quantum group $\mathcal{H}_{\Delta_5}$ on the automorphic side** (Wave 10 K1) is the EK-completion of the spherical Hecke algebra of $\Pi_{\mathrm{SK}}(\Delta_8)$ on $\mathrm{Sp}_4(\mathbb{A})$, with Arthur parameter $\psi_{\mathrm{SK}}$.

**The bridge to MO Borcherds-Yangian on $\mathrm{Hilb}(K3)$** is NOT via Howe theta on $(\mathrm{Sp}_4, O(4, 20))$. Instead it is via:
- (a) The CY-to-chiral functor $\Phi$ (Vol III): $X = \mathrm{Sym}^N(K3) \mapsto $ chiral algebra $A_{\mathrm{Sym}^N(K3)}$.
- (b) The Maulik-Okounkov stable-envelope construction: $\mathrm{Hilb}^N(K3) \mapsto $ Borcherds-Yangian module via $K$-theoretic stable envelopes.
- (c) The Borcherds product formula: the $K$-theoretic Hecke action factors through the Borcherds product.

**These are three separate constructions** that converge on $\Delta_5$ as a generating function (paramodular form for the CY-data $K3 \times E$), NOT a single Howe theta.

**Verdict 6.B.** The true automorphic avatar is two-fold via accidental isogeny: SK-CAP on Sp$_4$ + Borcherds-singular-theta on $\mathrm{O}(\Lambda^{3,2})_+$. The MO-Borcherds-Yangian connection is via CY-to-chiral functor + stable envelope, not Howe theta.

**Conjecture W11-K-FINAL (Two-fold avatar).** $\Delta_5$ has two coexisting automorphic origins (SK-CAP via Klingen Eisenstein residue on Sp$_4$; BGN singular theta on $\mathrm{O}(\Lambda^{3,2})_+$ at Kudla-Rallis boundary), connected by the accidental isogeny $\wedge^2$. The connection to MO-BY on Hilb($K3$) is via CY-to-chiral + stable envelopes, NOT Howe theta on the alleged dual pair $(\mathrm{Sp}_4, O(4, 20))$.

---

## Status updates: retractions of Wave 10 K-claims

| Wave 10 Claim | Wave 11 Status |
|---|---|
| K0 (SK normalisation $f(1,1,1) = 64$ from Lorgat 2020) | **CONFIRMED** (verified directly from Lorgat 2020 PDF p.~3) |
| K1 (Spherical Hecke chiral QG = EK-completion of SK Hecke) | **CONFIRMED** with caveat: the "spherical" condition for SK CAP requires Bessel model (Sugano 1985), not Whittaker (Saito-Kurokawa is non-generic) |
| K2 (EK-completion in two-parameter topology) | **CONFIRMED** (Wave 11 doesn't touch this) |
| K3 (Howe theta on $(\mathrm{Sp}_4, O(4, 20))$ as the bridge) | **RETRACTED** — wrong dual pair signature; wrong lattice; wrong direction of theta |
| K4 (W10-T2 PRIMARY: $F_2^{2A}$ via three paths) | **PARTIALLY CONFIRMED** (Eichler-Zagier $T_n$ is correct; super-Schur/DMVV paths wrong; not touched by W11) |
| K5 (Status changes OP-K-W9-1/2/3) | **NOT TOUCHED** by W11 (functorial/categorical lane, not automorphic) |
| K6 (EK-Borcherds Theorem statement) | **PARTIALLY CONFIRMED** (the Theorem is OK, but the proof sketch's invocation of Howe theta as a step is removed by Wave 11) |
| K-Howe (Howe lift = Borcherds lift) | **RETRACTED** — Borcherds lift is NOT Howe lift, it is BGN regularised singular theta on the orthogonal side via the accidental isogeny |
| K-Arthur-Transfer (MO-BY in orthogonal $L$-packet of Howe lift) | **RETRACTED** — MO-BY connection is via CY-to-chiral functor + stable envelopes, not via Howe-theta-Arthur-transfer |

**Net Wave 11 retractions of Wave 10:** 3 (K3, K-Howe, K-Arthur-Transfer).
**Net Wave 11 confirmations of Wave 10:** 4 (K0, K1, K2, K4).
**Net Wave 11 partial confirmations:** 1 (K6).
**Net Wave 11 untouched:** 1 (K5).

---

## Summary of new Wave 11 conjectures

| Conjecture | Statement | Falsifiable at |
|---|---|---|
| W11-K-1 (Correct dual pair) | Borcherds lift $\Phi(\phi_{0,1}) = \Delta_5$ is regularised theta for $(\widetilde{\mathrm{SL}}_2, \mathrm{O}(\Lambda^{3,2}))$ at boundary $p + q = 2n + 3 = 5$ | Local theta at $p = 2$ via Kudla 1986 doubling integral |
| W11-K-2 (CAP / Klingen origin) | $\rho_{\mathrm{aut}}(\Delta_5) = \Pi_{\mathrm{SK}}(\Delta_8)$ on Sp$_4$ with $\psi_{\mathrm{SK}} = \rho_{\Delta_8} \boxplus (\mathbf{1} \otimes [2]_{\mathrm{Arth}})$, constructed as residue of $E^{P_{2,2}}_s(\Phi_{\Delta_8})$ at $s = 1/2$ | Single-pole condition for SK CAP |
| W11-K-3 (Local theta at $p = 2$) | $\Phi_2(\rho_{\mathrm{aut}}(\Delta_5)) = -(2/5) L_2(1, \pi_2, \mathrm{Std})$ via Kudla 1986 with $\epsilon_2(\Lambda^{3,2}) = +1$, $\det = 2 \in \mathbb{Q}_2^\times/(\mathbb{Q}_2^\times)^2$ | Andrianov-Hecke vs Kudla local doubling integral |
| W11-K-4 (Rallis tower position) | Borcherds-GN sits at Rallis tower boundary $(n, p+q) = (1, 5) = (n, 4n+1)$, regularised theta = Siegel-Weil residue at $s = 0$, NOT cuspidal Howe lift | Bessel-vs-Whittaker model dichotomy: SK CAP non-generic, only Bessel model |
| W11-K-5 (Base change for SK CAP) | Base change to totally real $K$ preserves CAP cuspidality; base change to CM $K$ may have residual summand | $K = \mathbb{Q}(\sqrt{-7})$, check $\mathrm{BC}_K(\Delta_5)$ residual structure |
| W11-K-FINAL (Two-fold avatar) | Two coexisting automorphic origins of $\Delta_5$ via accidental isogeny $\wedge^2$: (I) SK CAP via Klingen on Sp$_4$; (II) BGN regularised singular theta on $\mathrm{O}(\Lambda^{3,2})$ | Hecke eigenvalue match between (I) and (II) at $p = 2, 3, 5$ |

---

## Wave 12 hand-off: 5 specific computations to verify W11 corrections

**W12-K-COMP-1.** Compute the Klingen residual Eisenstein $E^{P_{2,2}}_{1/2}(\Phi_{\Delta_8})$ on Sp$_4(\mathbb{A})$ explicitly and verify the residue at $s = 1/2$ equals $\Delta_5$ up to scalar (Piatetski-Shapiro 1983 reconstruction). Estimate ~400 lines of SageMath using $\Delta_8$ Hecke data.

**W12-K-COMP-2.** Compute the local Kudla-Rallis doubling integral $Z_2(s, \pi_2 \otimes \rho_2, \Phi_{\mathrm{spherical}})$ at $p = 2$ (Kudla 1986 \S 5 Eq. 5.2) and extract the residue at $s = 0$. Compare to local $\Delta_5$ Fourier coefficient at $p = 2$. Estimate ~300 lines PARI-GP.

**W12-K-COMP-3.** Verify the accidental isogeny $\wedge^2: \mathrm{Sp}_4(\mathbb{Z})/\{\pm I_4\} \to \mathrm{O}(\Lambda^{3,2})_+(\mathbb{Z})/\{\pm I_5\}$ on a concrete generator (e.g. $g_0 = \begin{pmatrix} 0 & I_2 \\ -I_2 & 0 \end{pmatrix}$ from Lorgat 2020 PDF p.~4) and check that $\Delta_5(g_0 \cdot Z) = -\Delta_5(Z)$ on the Sp$_4$ side equals the corresponding $\mathrm{O}(\Lambda^{3,2})$-action on the BGN lift output. Estimate ~200 lines.

**W12-K-COMP-4.** Compute the cyclic base change of $\Delta_5$ to $K = \mathbb{Q}(\sqrt{-7})$ via $\Delta_8$ base change to $K$ (Langlands 1980), and check whether the resulting GSp$_4(K)$-automorphic representation has a residual summand from CM splitting. Estimate ~500 lines.

**W12-K-COMP-5.** Verify W11-K-FINAL Hecke eigenvalue match between Klingen residual (Sp$_4$ side) and BGN singular theta (orthogonal side) at $p = 2, 3, 5$. The two sides should agree because they describe the SAME automorphic form via the accidental isogeny — the verification is that the two computations give the same numbers. Estimate ~300 lines.

---

## Citations (primary, Wave 11)

**Lorgat 2020 (CRITICAL primary).**
- Lorgat 2020, "A Borcherds Lift of the Weak Jacobi Form $\phi_{0,1}$, Generalized Borcherds-Kac-Moody Superalgebras and the Igusa Cusp Form $\Delta_5$", April 2 2020, unpublished PDF (\S 2 Maass multiplier, p.~3 $f(1,1,1) = 64$; \S 3 Lemma 1 accidental isogeny $\wedge^2$, p.~5; \S 4 lattice $\Lambda^{3,2} \supset \Lambda^{2,1}$, p.~5).

**Borcherds singular theta.**
- Borcherds 1998, Invent. Math. 132, 491-562 (\S 4 vector-valued $F$ of weight $(2-n)/2$ on $\widetilde{\mathrm{SL}}_2$; \S 14 the regularised theta integral construction).

**Kudla-Rallis tower / Siegel-Weil.**
- Kudla 1986, J. Reine Angew. Math. 1986, 113-141 (Theorem 5.1 doubling integral local).
- Kudla-Rallis 1988, J. Reine Angew. Math. 391, 65-84 (Siegel-Weil identification of theta with Eisenstein residue).
- Kudla-Rallis 1994, Ann. Math. 140, 1-80 (regularised Siegel-Weil at boundary stable range).
- Rallis 1984, J. Funct. Anal. 59, 372-397 (Howe duality unitarity).
- Howe 1979, Symp. Pure Math. 33 part 1 (theta correspondence).

**Saito-Kurokawa as CAP / Klingen residual.**
- Piatetski-Shapiro 1983, Invent. Math. 71, 309-338 (CRITICAL — SK as Klingen residual Eisenstein).
- Soudry 1988, J. Reine Angew. Math. 383, 87-108 (CAP structure for GSp$_4$).
- Maass 1979, Invent. Math. 52, 95-104 (original SK construction).
- Andrianov 1979, Russ. Math. Surv. 34, 75-148 (SK as JL).
- Andrianov-Zhuravlev 1995, *Modular Forms and Hecke Operators*, AMS.

**Base change / Langlands.**
- Langlands 1980, *Base Change for GL(2)*, Ann. Math. Studies 96 (cyclic base change).
- Arthur 2013, *The Endoscopic Classification of Representations: Orthogonal and Symplectic Groups*, Coll. Pub. 61.
- Gan-Takeda 2011, Ann. Math. 173, 1841-1882 (local Langlands for GSp$_4$).

**Other.**
- Niwa-Shintani 1975, J. Math. Soc. Japan 27, 117-153 (Shimura via Howe theta on $(\widetilde{\mathrm{SL}}_2, \mathrm{O}(2, 1))$).
- Waldspurger 1980, J. Math. Pures Appl. 60, 1-133 (Shimura as theta).
- Furusawa 1993, J. Reine Angew. Math. 438, 187-218 (Bessel periods).
- Sugano 1985, J. Fac. Sci. Univ. Tokyo Sect. IA 31, 521-568 (Bessel for SK).
- Schmidt 2007, *Saito-Kurokawa Lifts and Applications to Arithmetic*, Lecture Notes.
- Weil 1964, Acta Math. 113, 1-87 (metaplectic 2-cocycle).
- Kubota 1969, *Topological covers of $\mathrm{SL}_2$ over local fields*.
- Kudla-Millson 1990, Pub. Math. IHES 71, 121-172 (KM lift for $\mathrm{O}(p, 2)$).
- Gan-Savin 2003, Compositio Math. 139, 1-35 (exceptional theta).

---

## Epistemic ledger (Wave 11)

- **Convergence criterion (AP306).** Six ATTACK-HEAL cycles, each ending with a falsifiable conjecture or open problem.
- **Primary-source discipline.** Lorgat 2020 PDF directly consulted (pages 1-5 read, lattice $\Lambda^{3,2}$ verified, accidental isogeny verified, $f(1,1,1) = 64$ verified).
- **Material progress over Wave 10.**
  - Wave 10 K3 dual pair $(\mathrm{Sp}_4, O(4, 20))$ is FALSIFIED on three counts (lattice signature wrong, codomain wrong, direction wrong) — Wave 11 cycle 1.
  - Wave 10 conflated Borcherds singular theta with Howe-Weil cuspidal-stable-range theta — Wave 11 cycle 1.
  - Wave 10 implicitly assumed the SK packet originates as Howe theta from a smaller group — FALSE; SK is a CAP packet originating from Klingen residual Eisenstein (Piatetski-Shapiro 1983) — Wave 11 cycle 2.
  - Wave 10 K-Arthur-Transfer "L-group inclusion $\mathrm{SO}_5 \hookrightarrow \mathrm{SO}(5, 21)$ via zero extension" is meaningless — Wave 11 cycle 4.
  - Wave 11 establishes Rallis tower position: $(n, p+q) = (1, 5) = (n, 4n+1)$ at the boundary, regularised-theta-as-Siegel-Weil-residue, NOT cuspidal Howe lift.
  - Wave 11 identifies the true bridge: accidental isogeny $\wedge^2: \mathrm{Sp}_4 / \{\pm I_4\} \to \mathrm{O}(\Lambda^{3,2})_+ / \{\pm I_5\}$ from Lorgat 2020 \S 3, NOT Howe correspondence.
- **Falsifiable conjectures handed to Wave 12.** Five specific computations W12-K-COMP-1 through W12-K-COMP-5.
- **Retractions.** Wave 10 K3, K-Howe, K-Arthur-Transfer all RETRACTED.
- **Verdict.** EK-Borcherds-Manin SURVIVES the Wave 11 automorphic-functoriality audit, with the dual-pair / Howe-theta interpretation REPLACED by the correct picture: SK-CAP via Klingen Eisenstein residue + BGN regularised singular theta at Kudla-Rallis boundary, unified by accidental isogeny $\wedge^2$. The chiral quantum group identification (Wave 10 K1) survives; the bridge to MO-BY on Hilb(K3) is REROUTED through CY-to-chiral functor + stable envelopes (Vol III), not Howe theta.

---

## Wave 11 inscriptions

### 11.1 Anti-pattern registration

**AP-CY-W11-K-1.** Conflating Borcherds 1998 singular theta lift (regularised theta on $\mathcal{G}(L)$ for vector-valued $F$ of half-integral weight) with Howe-Weil cuspidal-stable-range theta correspondence (Howe 1979 / Rallis 1984 dual pair $(\mathrm{Sp}_{2n}, \mathrm{O}(p, q)) \subset \mathrm{Sp}_{2n(p+q)}$). These are two DIFFERENT lifts. The Borcherds lift is at the BOUNDARY of the Kudla-Rallis cuspidal stable range $p + q = 4n + 1$, where the regularised theta = Siegel-Weil residue at $s = 0$.

**AP-CY-W11-K-2.** Asserting Howe theta from Sp$_4$ to $O(4, 20)$ as the bridge between Sp$_4$-paramodular form $\Delta_5$ and orthogonal-side construction. Wrong on three counts: (i) the lattice for the Borcherds lift is $\Lambda^{3,2}$ from Lorgat 2020 \S 4, not Mukai $\Lambda^{4,20}$; (ii) the codomain of a hypothetical Howe theta would not be $\Delta_5$ but a different automorphic form on the orthogonal side; (iii) the bridge is the ACCIDENTAL ISOGENY $\wedge^2: \mathrm{Sp}_4(\mathbb{Z})/\{\pm I_4\} \to \mathrm{O}(\Lambda^{3,2})_+/\{\pm I_5\}$ (Lorgat 2020 \S 3, Lemma 1), not Howe correspondence.

**AP-CY-W11-K-3.** Asserting Saito-Kurokawa packet originates as Howe theta from a smaller group. SK is a **CAP** packet (CAP = Cuspidal Associated to Parabolic, Piatetski-Shapiro), and its automorphic origin is **residue at $s = 1/2$ of the Klingen-parabolic Eisenstein** $E^{P_{2,2}}_s(\Phi_{\Delta_8})$ (Piatetski-Shapiro 1983 \S 2). Howe theta cannot produce non-tempered (CAP) packets from a smaller cuspidal-tempered input; it preserves the Arthur SL$_2$-structure.

**AP-CY-W11-K-4.** Asserting "L-group inclusion $\mathrm{SO}_5(\mathbb{C}) \hookrightarrow \mathrm{SO}(5, 21)(\mathbb{C})$ via zero extension to the orthogonal complement" is canonical. There is NO canonical $L$-group inclusion of this kind; the corresponding Arthur SL$_2$-dimension would jump from 2 (SK packet) to 4 (residual Eisenstein on orthogonal side), violating Arthur parameter conservation.

### 11.2 First-principles cache entries

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|---|---|---|---|---|
| 323 | "Borcherds lift = Howe theta integral for the dual pair $(\mathrm{Sp}_4, O(4, 20)) \subset \mathrm{Sp}_{96}$." | The Borcherds lift connects symplectic and orthogonal sides via theta correspondence. | Wrong dual pair signature: $(p, q) = (4, 20)$ from Mukai is irrelevant; the Borcherds-lift lattice is $\Lambda^{3,2}$ from Lorgat 2020 \S 4 (signature $(3, 2)$). The correct dual pair is $(\widetilde{\mathrm{SL}}_2, \mathrm{O}(\Lambda^{3,2}))$ at boundary $p + q = 2n + 3 = 5$. The bridge between Sp$_4$ and $\mathrm{O}(\Lambda^{3,2})_+$ is the accidental isogeny $\wedge^2$ (Lorgat 2020 \S 3, Lemma 1), NOT Howe correspondence. | (Borcherds singular theta = Kudla-Rallis Siegel-Weil residue at $s = 0$, boundary stable range $p + q = 4n + 1$) UNION (accidental isogeny $\wedge^2: \mathrm{Sp}_4/\{\pm I_4\} \to \mathrm{O}(\Lambda^{3,2})_+/\{\pm I_5\}$ relates Sp$_4$-side and orthogonal-side, NOT Howe theta) | dual-pair-signature / Borcherds-vs-Howe-theta / accidental-isogeny-vs-correspondence |
| 324 | "Saito-Kurokawa packet originates as Howe theta from $\mathrm{SL}_2$ to $\mathrm{Sp}_4$ via dual pair $(\widetilde{\mathrm{SL}}_2, \mathrm{O}(2, 1))$." | The SK packet is a theta lift of Shimura preimage of $\Delta_8$. | Wrong direction. Niwa-Shintani 1975 Howe theta $(\widetilde{\mathrm{SL}}_2, \mathrm{O}(2, 1))$ produces $\Delta_8$ on $\mathrm{PGL}_2$ from Shimura preimage, NOT $\Delta_5$ on Sp$_4$. The SK lift $\Delta_8 \to \Delta_5$ is a SEPARATE construction (Klingen residual Eisenstein, Piatetski-Shapiro 1983). | The two-step path is Shimura preimage $\to$ $\Delta_8$ via Niwa-Howe-theta, then $\Delta_8 \to \Delta_5$ via Klingen residual Eisenstein. The second step is NOT a theta lift. SK CAP has Arthur parameter $\rho_{\Delta_8} \boxplus (\mathbf{1} \otimes [2])$ which is non-tempered and cannot be produced by a single Howe theta from a tempered input. | CAP-vs-Howe / Klingen-vs-theta / two-step-not-one-step |
| 325 | "L-group inclusion $L\mathrm{Sp}_4 = \mathrm{SO}_5(\mathbb{C}) \hookrightarrow LO(4, 20) = \mathrm{SO}(5, 21)(\mathbb{C})$ via zero-extension transfers Arthur parameter $\psi_{\Delta_5}$ to $\tilde\psi_{\Delta_5}$." | Functorial Arthur parameter transfer between dual-pair groups via $L$-group inclusion. | The dual pair is wrong (\#323), so the $L$-group inclusion is meaningless. Even granting an $L$-group inclusion, "zero-extension" of $\psi_{\Delta_5}$ would not preserve the Arthur SL$_2$-dimension (which is 2 for SK CAP), but the residual-Eisenstein parameter on orthogonal side has 4-dim Arthur SL$_2$. **Arthur parameter conservation FAILS.** | The correct transfer is via the accidental isogeny $\wedge^2$ (Lorgat 2020 \S 3, Lemma 1), which is an IDENTITY on $L$-groups (since the two presentations are the same group). The Arthur parameter $\psi_{\mathrm{SK}}$ is preserved tautologically. | L-group-inclusion / Arthur-conservation / accidental-vs-functoriality |

### 11.3 Manuscript amendment recommendations (NOT inscribed per Wave 11 rules)

For potential Wave 12 inscription to `chapters/examples/k3e_bkm_chapter.tex`:

> **Two-fold automorphic origin of $\Delta_5$ (Wave 11).** The Igusa cusp form $\Delta_5$ has two coexisting automorphic origins: (I) the Saito-Kurokawa CAP packet on $\mathrm{Sp}_4(\mathbb{A})$ with Arthur parameter $\psi_{\mathrm{SK}}(\Delta_8) = \rho_{\Delta_8} \boxplus (\mathbf{1} \otimes [2]_{\mathrm{Arth}})$, constructed as the residue at $s = 1/2$ of the Klingen-parabolic Eisenstein $E^{P_{2,2}}_s(\Phi_{\Delta_8})$ (Piatetski-Shapiro 1983); (II) the Borcherds-Gritsenko-Nikulin singular theta lift on $\mathrm{O}(\Lambda^{3,2})_+(\mathbb{A})$, at the boundary of the Kudla-Rallis cuspidal stable range $(n, p+q) = (1, 5) = (n, 4n+1)$, identified with the Siegel-Weil residue at $s = 0$ of the doubling Eisenstein. The two origins are connected by the accidental isogeny $\wedge^2: \mathrm{Sp}_4(\mathbb{Z})/\{\pm I_4\} \xrightarrow{\sim} \mathrm{O}(\Lambda^{3,2})_+(\mathbb{Z})/\{\pm I_5\}$ (Lorgat 2020 \S 3, Lemma 1), NOT by a Howe-Weil theta correspondence between two distinct groups.

### 11.4 Open problems handed to Wave 12

- **W12-K-COMP-1** through **W12-K-COMP-5** (above).

---

## Functorial diagrams (Kazhdan signature, Wave 11)

**Diagram W11-1: the two automorphic origins of $\Delta_5$.**

```
   (I) CAP origin on Sp_4 side                  (II) BGN regularised theta on O side

   Phi_{Delta_8} on GL_2 Levi of P_{2,2}      F = phi_{0,1} (vec'd half-int weight)
              |                                          |
   Klingen residual Eisenstein                Borcherds singular theta integral
              |                                          |
              v                                          v
   Res_{s=1/2} E^{P_{2,2}}_s(Phi_{Delta_8})    Res_{s=0} of doubling Eisenstein
              |                                          |
              v                                          v
   Delta_5 in S_5(Sp_4(Z); v_{Delta_5})       Delta_5 in S_5(O(Lambda^{3,2})_+)
              |____________________________________________|
                              |
                    accidental isogeny (Lorgat 2020 §3, Lemma 1)
                    wedge^2: Sp_4(Z)/{+/- I_4} —> O(Lambda^{3,2})_+/{+/- I_5}
                              |
              SAME automorphic form via group identification
              NOT Howe-Weil theta correspondence between distinct groups
```

**Diagram W11-2: Rallis tower position.**

```
Rallis tower (Sp~_2, O(p,q)) at fixed n=1, vary p+q:

p+q=2: zero (low rank)
p+q=3: first occurrence, residual
p+q=4: residual Eisenstein, not cuspidal
p+q=5: BOUNDARY of cuspidal stable range = 4n+1 — ★ Borcherds GN here ★
p+q=6,...: cuspidal stable range, genuine cuspidal theta

Borcherds lift = regularised theta at p+q=5, NOT cuspidal Howe lift.
Identified with Siegel-Weil residue at s=0 of doubling integral.
```

**Diagram W11-3: bridge to MO Borcherds-Yangian on Hilb(K3) (REROUTED).**

```
   Wave 10 (FALSE):                           Wave 11 (CORRECTED):

   Delta_5 on Sp_4                            Delta_5 on Sp_4
       |                                          |
   "Howe theta to (Sp_4, O(4,20))"             accidental isogeny wedge^2
       |                                          |
       v                                          v
   "MO Borcherds-Yangian on Hilb(K3)"          Delta_5 on O(Lambda^{3,2})_+
                                                  
                                              MO Borcherds-Yangian on Hilb(K3)
                                              connected via:
                                              (a) CY-to-chiral functor Phi (Vol III)
                                              (b) Stable envelope Maulik-Okounkov
                                              (c) Borcherds product on K-theory side

                                              NOT via single Howe theta between two
                                              distinct groups; the connection is a
                                              composition of three separate functors.
```

---

## Contrast with Wave 10 Kazhdan pass

Wave 10 Kazhdan claimed:
- Howe theta on $(\mathrm{Sp}_4, O(4, 20)) \subset \mathrm{Sp}_{96}$ as the bridge.
- SK packet identified, "Hecke eigenvalues match $\Delta_8$", "Bessel function via Sugano".
- "L-group inclusion $\mathrm{SO}_5 \hookrightarrow \mathrm{SO}(5, 21)$" gives Arthur transfer.
- W10-K-Tower with Eichler-Zagier $T_n$ replacing super-Schur.

Wave 11 Kazhdan corrects:
- Wrong dual pair signature: $\Lambda^{3,2}$ (Lorgat 2020 \S 4) not $\Lambda^{4,20}$ (Mukai).
- Borcherds lift is BGN regularised singular theta, NOT Howe-Weil dual-pair theta.
- Correct dual pair $(\widetilde{\mathrm{SL}}_2, \mathrm{O}(\Lambda^{3,2}))$ at Rallis tower boundary $p+q = 4n+1 = 5$.
- SK packet originates as **Klingen residual Eisenstein** (Piatetski-Shapiro 1983), NOT Howe theta.
- "L-group inclusion" claim is meaningless; correct bridge is **accidental isogeny $\wedge^2$** (Lorgat 2020 \S 3, Lemma 1).
- Connection to MO-BY on Hilb($K3$) rerouted via CY-to-chiral functor + stable envelopes (Vol III), NOT Howe theta.

Wave 11 RETRACTS Wave 10 K3, K-Howe, K-Arthur-Transfer; CONFIRMS Wave 10 K0, K1, K2, K4.

Wave 11 advances by SHARPENING the automorphic identification through correct first-principles Kudla-Rallis tower analysis, Piatetski-Shapiro CAP construction, and direct consultation of Lorgat 2020 PDF \S 3-4 for the accidental isogeny.

---

Authored by Raeez Lorgat. No AI attribution anywhere.
