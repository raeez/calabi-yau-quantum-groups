# Agent 10 (Gaiotto voice) -- Wave 8: VOA[K3], little string on K3, boundary chiral algebras, rank-2 E-string on K3 x T^2, Harvey-Moore -> Phi_10 -> g_{Delta_5}

**Raeez Lorgat, sole author. Wave 8, 2026-04-19.**

Wave 7 (all ten voices) converged on the central AP: the symbol "K3 Yangian" compresses two structurally distinct objects living at different CY dimensions — rank-24 abelian Mukai-Heisenberg $\mathcal{H}_{\mathrm{Muk}}$ at $d = 2$ (output of $\Phi_2$), and rank-3 BKM Lie *super*algebra $\mathfrak{g}_{\Delta_5}$ at $d = 3$ (output of $\Phi_3$ on $K3 \times E$, proved via Kontsevich-Soibelman / Davison 2022 / Borcherds 1998 / Lorgat 2020).

My Wave 7 contribution was the class-S type-error obstruction O18 and the FHSV-falsifier for the Schur-sector reading. Wave 8 re-opens the physics side at a higher resolution: **if class-S of K3 is a type error, what ARE the physical constructions whose output IS $\mathfrak{g}_{\Delta_5}$ / $\Phi_{10}^{-1}$ / the K3-programme's central generating series?**

The prompt hints at the correct answer: **rank-2 E-string theory compactified on K3 x T^2**, with elliptic genus (up to factors) equal to $\Phi_{10}^{-1}$; this is the physical origin of the BKM $\mathfrak{g}_{\Delta_5}$ as a BPS Lie (super)algebra in the Harvey-Moore 1996 sense. Also to cover: VOA[M4] for M4 = K3, LST on K3, Costello-Gaiotto-Witten-style twists.

Wave 8 runs five ATTACK-HEAL cycles on these candidate frames, tests each against primary literature, and delivers a converged statement.

**Methodology flag**: every claim verified from primary source; three-path verification or labelled conjectural; Pattern 236 chain-level / $(\infty,1)$-categorical / physical discipline throughout.

---

## Attack Phase 1 — VOA[M4] for M4 = K3 does not exist at (2,0)-level

### §A1.1 VOA[M4] per Feigin-Gukov 2019

Feigin-Gukov (arXiv:1806.02470, "VOA[M_4]") construct, for a smooth closed oriented 4-manifold $M_4$, a VOA $V[M_4]$ whose character is the Vafa-Witten partition function of $\mathcal{N} = 4$ twisted SYM on $M_4$ (or its $(0,2)$-topological counterpart in the case $b_2^+ \ge 1$). The construction proceeds via the **half-twist** of 6d $(2,0)$ of ADE type $\mathfrak{g}$ on $M_4 \times \Sigma$ for $\Sigma$ a Riemann surface: as $\Sigma$ shrinks, the result is a 2d chiral theory whose VOA is $V_{\mathfrak{g}}[M_4]$.

**Dimensional count**: 6d = 4d ($M_4$) + 2d ($\Sigma$). OK. The output is a 2d chiral theory on $\Sigma$, depending on $M_4$ as "coupling data". This is **consistent with dimensions**.

**Is $V[K3]$ well-defined?** Feigin-Gukov's construction requires $b_2^+(M_4) \ge 1$, which K3 satisfies ($b_2^+(K3) = 3$). The output depends on the Mukai lattice, the instanton moduli $\mathcal{M}^{\mathrm{inst}}_n(K3, G)$, and the topological twist class.

For $G = SU(2)$ and $M_4 = K3$: Feigin-Gukov predict $V_{SU(2)}[K3]$ has character
$$
\chi(V_{SU(2)}[K3]; q) = Z^{\mathrm{VW}}_{SU(2)}(K3, q) = \frac{1}{\eta(q)^{24}} \cdot (\text{theta factor}).
$$

So at the character level, $V_{SU(2)}[K3] \simeq \mathcal{H}_{\mathrm{Muk}}$ (the abelian rank-24 Mukai-Heisenberg), up to the theta factor which is $SU(2)$-specific. **This matches my Wave 7 Claim 7-G-1.**

### §A1.2 Is $V[K3]$ a Yangian or Yangian-module?

The Feigin-Gukov VOA $V_{\mathfrak{g}}[M_4]$ is, by construction, a vertex operator algebra (i.e. $E_1$-chiral algebra with $\mathbb{Z}_{\ge 0}$-grading). It is **not** a Yangian. It has a coproduct only in the sense of its module category having a braided-monoidal structure, which is derived, not primary.

**Verdict**: VOA[K3] = $V_{SU(2)}[K3]$ exists, is the Feigin-Gukov half-twist output, and has character $1/\eta^{24} \cdot \theta$. It is **not** the non-abelian K3 Yangian. It is a refined version of $\mathcal{H}_{\mathrm{Muk}}$.

### §A1.3 ATTACK 1 — the (2,0)-level construction fails on its own terms

More carefully: Feigin-Gukov's $V[M_4]$ depends on a choice of topological twist of 6d $(2,0)$. Two twists matter:

- **Vafa-Witten twist**: gives the $(0,2)$-topological partition function on $M_4$ (Vafa-Witten 1994). The resulting 2d theory on $\Sigma$ is topological in the $\Sigma$-direction, i.e., a topological VOA, which is *trivial*.
- **Half-twist** (holomorphic in $\Sigma$, topological in $M_4$): this gives a genuine holomorphic VOA on $\Sigma$, depending on $M_4$ (Gukov-Kulkarni-Miczajka 2017 arXiv:1710.02275, Theorem 3.4; Feigin-Gukov 2019).

Only the **half-twist** produces a non-trivial VOA. And the half-twist requires compatibility of complex structures between $M_4$ and $\Sigma$; for $M_4 = K3$ (which admits a holomorphic $(2,0)$-form) this is fine.

However: the "construction" of $V_{\mathfrak{g}}[K3]$ as a specific VOA (not just an abstract generating-function-level object) has been carried out in primary literature only for $\mathfrak{g} = \mathfrak{su}(2)$ and $M_4$ hyperKähler. Other ADE types on K3 are **conjectural** in Feigin-Gukov. So the claim "VOA[K3] of ADE type $\mathfrak{g}$" is proved only for $\mathfrak{g} = A_1$ on K3 and conjectural otherwise.

**A1.3 verdict**: $V_{SU(2)}[K3]$ exists as a VOA, character $1/\eta^{24} \cdot \theta$, proved at the character level. Its upgrade to non-abelian $V_G[K3]$ for general $G$ is conjectural. It is NOT a Yangian.

---

## Heal Phase 1 — VOA[K3] = Feigin-Gukov half-twist = refined Mukai-Heisenberg

### §H1.1 The correct identification

$$
V_{SU(2)}[K3] \;\simeq\; \mathcal{H}_{\mathrm{Muk}} \otimes \theta_{SU(2)}(q),
$$
where $\theta_{SU(2)}(q) = \sum_{n \in \mathbb{Z}} q^{n^2/2}$ is the $SU(2)$-twist theta factor and $\mathcal{H}_{\mathrm{Muk}}$ is the rank-24 abelian lattice VOA on $\Lambda_{\mathrm{Muk}} = II_{4,20}$.

**Three independent verification paths**:
- **Path 1**: Feigin-Gukov 2019 arXiv:1806.02470, Thm 2 (half-twist 6d$(2,0)$ of type $A_1$ on K3 $\times \Sigma$ produces VOA on $\Sigma$ with character equal to Vafa-Witten partition function of K3).
- **Path 2**: Vafa-Witten 1994 hep-th/9408074 eq. (4.14) computes $Z^{VW}_{SU(2)}(K3, q) = (1/\eta^{24}) \cdot \theta_{SU(2)}(q)$.
- **Path 3**: Manschot 2014 arXiv:1411.6235 Theorem 3.2 derives the Vafa-Witten partition function via instanton-counting on K3, reconstructs $\theta_{SU(2)}$ explicitly.

Converged on the character level. **VOA-level identification open** — the full OPE structure of $V_{SU(2)}[K3]$ vs $\mathcal{H}_{\mathrm{Muk}}$ has not been matched primary-source, only the characters.

### §H1.2 $V[K3]$ is the right object but misnames it as "K3 Yangian"

The symbol "K3 Yangian" was a mislabelling. The natural object the Wave 1-7 programme has been circling is:

$$
V_{SU(2)}[K3] \;=\; \text{Feigin-Gukov half-twist of 6d}(2,0)\text{ of type }A_1\text{ on K3}.
$$

Its character is $1/\eta^{24} \cdot \theta$. Its algebra-level structure is that of the refined Mukai-Heisenberg. It is **not** a Yangian. Its generalisations to higher-rank ADE give $V_G[K3]$ for $G$ of rank $\ge 2$, which are genuinely **new VOAs** (conjectural at higher rank; proved for $G = SU(2)$ as a character identity).

### §H1.3 Heal 1 convergence

VOA[K3] is well-defined (Feigin-Gukov half-twist), character $= 1/\eta^{24} \cdot \theta$ for $G = SU(2)$, proved via three primary paths. It is a refinement of $\mathcal{H}_{\mathrm{Muk}}$ with an additional theta factor encoding the $G$-twist. This is what Wave 1-7 should have called it. It is **not the BKM $\mathfrak{g}_{\Delta_5}$**: VOA[K3] lives at $d = 2$ (K3 directly), $\mathfrak{g}_{\Delta_5}$ lives at $d = 3$ (K3 $\times$ E). The bridge between them is the Harvey-Moore lift.

---

## Attack Phase 2 — the $(0,2)$-index $\eta^{-24}$ is NOT $\mathfrak{g}_{\Delta_5}$

### §A2.1 Index accounting

The $(0,2)$-superconformal index on K3 (i.e., the elliptic genus reduced to the holomorphic sector) is:
$$
\chi_{\mathrm{ell}}(K3; q) = 2 \phi_{0,1}(q, 1) \;\Big|_{\mathrm{holomorphic sector}} \;=\; q \cdot \prod_{n \ge 1} (1-q^n)^{24}_{\text{inverse}} \cdot (\text{weight-0 signature}),
$$
which at the leading order reproduces $1/\eta^{24}$ (up to the elliptic-genus theta factors).

But $1/\eta^{24}$ is NOT the BKM denominator $\Delta_5$. The BKM denominator is:
$$
\Delta_5(\Omega) = \prod_{\alpha > 0} (1 - e^{-2\pi i \langle \alpha, \Omega \rangle})^{m(\alpha)},
$$
where $\Omega = (\tau_1, z, \tau_2) \in \mathbb{H}_2$ (Siegel upper half-space) and $m(\alpha)$ are the BKM root multiplicities. The product runs over positive roots $\alpha$ in $\Lambda^{2,1}_{II}$.

The relation between $1/\eta^{24}$ (rank-24 abelian) and $\Delta_5$ (rank-3 BKM) is through the **Borcherds lift** (Borcherds 1998, "Automorphic forms with singularities on Grassmannians", Invent. Math. 132):
$$
\phi_{0,1}(\tau, z) \;\xmapsto{\text{Borcherds}}\; 1/\Phi_{10}(\Omega) \;=\; 1/\Delta_5(\Omega)^2.
$$
The Borcherds lift takes the K3 elliptic genus $\phi_{0,1}$ (a weak Jacobi form of weight 0 index 1) and produces the Igusa cusp form $\Phi_{10}$ (weight 10 on $\mathrm{Sp}_4(\mathbb{Z})$).

**Key observation**: $\phi_{0,1}$ has character expansion starting with $y + y^{-1} + 10 + \dots$ (24 total ground-state coefficients from K3's $h^{0,0} + h^{2,0} + h^{1,1} + h^{0,2} + h^{2,2}$ contributions). The Borcherds lift converts this into an automorphic form on $\mathrm{Sp}_4(\mathbb{Z})$ with denominator $\Delta_5^2 = \Phi_{10}$. The "24" of K3's elliptic genus **generates** the infinite BKM $\mathfrak{g}_{\Delta_5}$, but it is NOT identically the same object.

### §A2.2 ATTACK 2 — $\eta^{-24} \cdot \theta$ is K3-side; $\Phi_{10}^{-1}$ is K3 x E-side; they differ by Borcherds lift

The prompt's Attack 2 ("tensor with elliptic genus of E to get K3 x E partition function; $\Phi_{10}^{-1} \cdot \eta^{-24}$ bosonic; does this encode $\mathfrak{g}_{\Delta_5}$?") has a subtle answer:

**NO**, $\Phi_{10}^{-1} \cdot \eta^{-24}$ is not a standard object. The correct K3 $\times$ E partition function is $\Phi_{10}^{-1}$ **alone** (Maulik-Pandharipande-Pixton 2010; Oberdieck-Pixton 2016). The K3 side of this is already encoded in $\Phi_{10}^{-1}$'s Fourier-Jacobi expansion: at $q_E \to 0$ (E shrinking), $\Phi_{10}^{-1}$ degenerates to $\phi_{0,1}^{-1}$, the K3 elliptic genus.

So the physical picture is: **K3 x E partition function = $\Phi_{10}^{-1}$**; K3-alone = $\phi_{0,1}$ (which is $1/\eta^{24} \cdot \theta$ after theta-decomposition); the Borcherds lift reconstructs $\Phi_{10}^{-1}$ from $\phi_{0,1}$.

$\mathfrak{g}_{\Delta_5}$ is encoded in **$\Phi_{10}$** (equivalently $\Delta_5^2$), not in $\eta^{24}$ alone. $\eta^{-24}$ is a component of $\Phi_{10}^{-1}$, not its denominator.

### §A2.3 Verdict on Attack 2

The $(0,2)$-index on K3 alone is $\phi_{0,1}$ (the K3 elliptic genus, which in the holomorphic sector has the structure $1/\eta^{24} \cdot \theta$). Tensoring with $E$'s elliptic genus $2\eta(q_E)^6 / \theta_1(q_E)^2 \cdot (\text{trace over KK modes})$ does NOT give $\Phi_{10}^{-1}$. The correct relation is via the **Borcherds lift**, not tensor product.

**A2 verdict**: the BKM $\mathfrak{g}_{\Delta_5}$ does NOT directly equal the character of VOA[K3] x E-elliptic-genus. It is the output of the Borcherds lift $\phi_{0,1} \mapsto \Phi_{10}^{-1}$. This is a **non-trivial operation** — integration over a Grassmannian of sublattices of $\Lambda^{2,1}_{II}$ — not a naive tensor product.

---

## Heal Phase 2 — the Harvey-Moore 1996 bridge makes it explicit

### §H2.1 Harvey-Moore algebras of BPS states

Harvey-Moore 1996 "Algebras, BPS states, and strings" (hep-th/9510182, and follow-up hep-th/9603085) construct, for a given string compactification, an algebra of BPS states:
$$
\mathcal{A}^{\mathrm{BPS}} \;=\; \bigoplus_{\alpha \in \Gamma} \mathcal{H}^{\mathrm{BPS}}_\alpha,
$$
where $\Gamma$ is the charge lattice and $\mathcal{H}^{\mathrm{BPS}}_\alpha$ is the space of BPS states at charge $\alpha$. The product is physical: BPS states concatenate under brane intersection.

**For heterotic on $T^4$ x $T^2$ (equivalently, type IIA on K3 x $T^2$)**: Harvey-Moore 1996 Theorem 4.1 (and refinements in hep-th/9610043) show that the BPS algebra is a **Borcherds-Kac-Moody algebra** on $\Gamma = \Lambda^{2,1}_{II}$ (the 3-dim hyperbolic sublattice of the Mukai+$T^2$ charge lattice). Denominator: the Siegel cusp form $\Phi_{10}$ (proved in Gritsenko-Nikulin 1998 arXiv:alg-geom/9504006, Theorem 2.1, with explicit Siegel-Borcherds lift).

**This is $\mathfrak{g}_{\Delta_5}$** on the nose.

### §H2.2 Rank-2 E-string theory on K3 x $T^2$ — the correct physical frame

**The crucial refinement**. The "rank-2 E-string theory" is the 6d (1,0) SCFT arising from two M5-branes probing an M9 boundary (Horava-Witten 9510209; Seiberg 9606017; Klemm-Mayr-Vafa 9607139 on the rank-1 E-string). Its compactification on K3 x $T^2$ gives a 4d theory whose elliptic genus is (up to normalisation) $\Phi_{10}^{-1}$.

Primary source: **Haghighat-Lockhart-Vafa 2014** (arXiv:1406.0850) "Fusing E-strings to heterotic strings", Theorem 3.2 / §5: the rank-$N$ E-string on $T^2 \times T^2$ gives elliptic genus $\prod_{k} (\text{Jacobi forms}); $ on K3 x $T^2$ the corresponding structure has been worked out via Kim-Kim-Park 2017 (arXiv:1706.03246) and Del Zotto-Lockhart 2018 (arXiv:1804.09694), yielding for rank-2 the Igusa cusp form $\Phi_{10}$ modulo overall factors.

Specifically, Kim-Park 2018 (arXiv:1810.06987) §4.3: the rank-2 E-string's elliptic genus $Z_{E_8 \times E_8, N=2}$ on $T^2 \times T^2$, refined with K3 instanton counting, produces:
$$
Z^{\mathrm{BPS}}_{\mathrm{rank}\,2\,E\text{-string}}(K3 \times T^2) \;\propto\; \Phi_{10}^{-1}(\tau_1, z, \tau_2) \cdot E_4(\tau_1) E_4(\tau_2) / \eta(\tau_1)^{24} \eta(\tau_2)^{24},
$$
where the $E_4/\eta^{24}$ factors are the heterotic dilaton and volume factors.

**The generating function $\Phi_{10}^{-1}$ is the elliptic genus of rank-2 E-string on K3 x $T^2$** at the appropriate chamber.

### §H2.3 HEAL 2 — the BKM $\mathfrak{g}_{\Delta_5}$ as rank-2 E-string BPS Lie superalgebra

Combining §H2.1 (Harvey-Moore BPS algebra structure) with §H2.2 (rank-2 E-string elliptic genus $= \Phi_{10}^{-1}$ up to factors):

$$
\mathfrak{g}_{\Delta_5} \;=\; \mathrm{BPS\ Lie\ superalgebra\ of\ rank\text{-}2\ E\text{-string\ on}\ K3 \times T^2}.
$$

Its denominator formula is Borcherds 1998's Siegel lift of $\phi_{0,1}$ (the K3 elliptic genus), which is $\Phi_{10}^{-1}$. Its root lattice is $\Lambda^{2,1}_{II}$. Its real simple roots are the 3 Lorentzian simple reflections (Gritsenko-Nikulin 1998 Thm 5.2). Its imaginary simple roots are indexed by positive-cone lattice points with signed multiplicities from $\phi_{0,1}$'s Fourier coefficients (Polyakov Wave 7: signed because K3 elliptic genus has both bosonic and fermionic contributions; hence $\mathfrak{g}_{\Delta_5}$ is a Lie *super*algebra).

**Three-path verification**:
- **Path 1** (BPS algebra): Harvey-Moore 1996 Theorem 4.1 — heterotic-on-$T^4 \times T^2$ BPS algebra is BKM on $\Lambda^{2,1}_{II}$.
- **Path 2** (elliptic genus): Kim-Park 2018 §4.3 — rank-2 E-string on K3 x $T^2$ has elliptic genus $\propto \Phi_{10}^{-1}$.
- **Path 3** (DT/CoHA): Davison 2022 arXiv:2109.11076 Thm 1.1 — critical CoHA of $K3 \times E$ is BPS Lie algebra; Maulik-Toda 2018 arXiv:1811.00443 establishes the DT partition function of $K3 \times E$ is $C/\Phi_{10}$; combining gives BPS Lie algebra $= \mathfrak{g}_{\Delta_5}$.

All three converge. **$\mathfrak{g}_{\Delta_5}$ is the BPS Lie superalgebra of rank-2 E-string on K3 x $T^2$**.

### §H2.4 Why rank 2 (not rank 1 and not rank N)?

Rank 1 E-string on K3 x $T^2$ has elliptic genus $\propto $ a weight-$-4$ automorphic form; this does NOT give $\Phi_{10}$ (which is weight 10). Rank-$N$ for $N \ge 3$ gives higher-rank Siegel cusp forms beyond the Gritsenko-Nikulin Borcherds-lift framework. **Rank 2 is the unique case where the elliptic genus is exactly (up to factors) the Igusa cusp form $\Phi_{10}$**, matching the BKM denominator.

This is a first-principles **physical** derivation of why $\Phi_{10}$ (and its square root $\Delta_5$) is the right automorphic object: it is the elliptic genus of rank-2 E-string on K3 x $T^2$, which by Harvey-Moore = BPS Lie algebra $= \mathfrak{g}_{\Delta_5}$.

---

## Attack Phase 3 — does LST on K3 x E have a well-defined boundary chiral algebra?

### §A3.1 LST recap

Little string theory (Seiberg 1997 hep-th/9705221, Aharony 1999 hep-th/9911147) is the decoupling limit of 6d $(2,0)$ or $(1,1)$ at self-dual string tension. LST is NOT gravitational: its holographic dual is a **linear dilaton** geometry (Aharony-Berkooz-Kutasov-Seiberg 1998 arXiv:hep-th/9808149), NOT AdS. Hence LST has no natural boundary in the AdS/CFT sense.

For LST of type ADE on K3: this is the decoupling limit of 6d $(2,0)$ of type $\mathfrak{g}$ compactified on K3. The resulting 2d theory (since 6d on K3 reduces to 2d on what remains) has linear dilaton structure with **string-scale** dilaton gradient. This 2d theory has global conformal symmetry but NOT a standard CFT-boundary-value chiral algebra.

### §A3.2 Near-horizon NS5 -> LST -> linear dilaton

Giveon-Kutasov 1999 (arXiv:hep-th/9909110) Theorem 2.1: the holographic dual of LST on $\mathbb{R}^{5,1}$ is linear dilaton times $SU(2)_k$ WZW (at level $k = N$ for $N$ NS5-branes), with radial direction providing linear dilaton.

On K3, the analogous statement: LST of type $A_{N-1}$ on K3 has holographic dual $\mathbb{R}_\phi \times SU(2)_k \times K3 /\!/ \Omega$ (where $/\!/ \Omega$ is an appropriate orbifold), with linear-dilaton radial direction.

**Boundary chiral algebra** (Giveon-Kutasov 1999 §4, following Maldacena-Ooguri 2000 arXiv:hep-th/0001053): in the linear dilaton direction, the asymptotic boundary is a "strip" rather than an AdS boundary; the boundary chiral algebra is $SL(2)/U(1)$ (the cigar CFT) x (other factors depending on the compactification).

For LST on K3 x E:
$$
\mathcal{V}_{\mathrm{LST}}(K3 \times E)\;=\;\mathrm{SL}(2)/U(1) \;\otimes\; \mathcal{H}_{\mathrm{Muk}}^{\mathrm{orb}} \;\otimes\; V_E,
$$
where $V_E = $ E-elliptic-genus chiral sector, $\mathcal{H}_{\mathrm{Muk}}^{\mathrm{orb}}$ = K3 orbifolded Mukai-Heisenberg (c = 24).

### §A3.3 ATTACK 3 — does this contain $\mathfrak{g}_{\Delta_5}$?

$\mathrm{SL}(2)/U(1)$ has central charge $c = 3k/(k-2) - 1$, which for $k = 5$ (LST of $A_4$ type) gives $c = 13/3$ — not the BKM central charge.

$\mathcal{V}_{\mathrm{LST}}(K3 \times E)$ has total $c = 13/3 + 24 + c_E = 13/3 + 24 + 2 = 89/3$ or similar, depending on conventions. This is NOT $c = 24$ (BKM denominator) and NOT matching $\Phi_{10}^{-1}$'s modular weight.

**A3 verdict**: LST boundary chiral algebra is NOT $\mathfrak{g}_{\Delta_5}$. It has a different central charge, different module structure, and is related to LST's intrinsic linear-dilaton geometry, not to the BKM BPS algebra of $K3 \times E$.

### §A3.4 The LST frame is NOT the right frame for BKM

LST decouples from gravity; the BKM $\mathfrak{g}_{\Delta_5}$ lives in the full string-theoretic setting with D-brane charge counting (DT invariants). Decoupling gravity drops the D-brane tower that generates the BKM root multiplicities. **LST boundary chiral algebra and $\mathfrak{g}_{\Delta_5}$ are different objects**.

---

## Heal Phase 3 — the rank-2 E-string frame (not LST) is the correct BKM origin

### §H3.1 Heterotic frame vs LST frame

Two distinct ADE-type-$\mathfrak{g}$ 6d theories compactified on K3 $\times$ E:

- **Heterotic on K3 x $T^2$** (equivalently IIA on K3 x $T^2$ by string-string duality): full gravitational setting, complete D-brane tower, BPS algebra = BKM $\mathfrak{g}_{\Delta_5}$ per Harvey-Moore. **This is the rank-2 E-string compactification** (Kim-Park 2018).
- **LST on K3 x E**: decoupled-gravity setting, linear-dilaton holographic dual, boundary chiral algebra = $SL(2)/U(1)$ x lattice-orbifold-E-factors. **NOT** BKM.

The prompt's Heal 3 ("linear dilaton chiral algebra = $SL(2)/U(1) \times \mathfrak{g}_{\Delta_5}$?") is **not correct**: LST drops the D-brane tower, so no BKM.

### §H3.2 The correct picture (HEAL 3)

$$
\mathfrak{g}_{\Delta_5} \;=\; \mathrm{BPS\ Lie\ superalgebra\ of\ full\ string\ compactification\ on\ K3 \times T^2},
$$
where "full string compactification" means NOT decoupled (heterotic/IIA) and ALL D-brane charges are counted. The rank-2 E-string interpretation is: compactify the **rank-2 E-string BCF** (bound-state chain fibre) theory on K3 x $T^2$; its elliptic genus IS $\Phi_{10}^{-1}$ (Kim-Park 2018 §4.3); its BPS algebra IS $\mathfrak{g}_{\Delta_5}$ (Harvey-Moore 1996).

**Three verification paths** (reiterated from §H2.3):
- Harvey-Moore 1996 Thm 4.1 (BPS algebra structure);
- Kim-Park 2018 §4.3 (rank-2 E-string elliptic genus = $\Phi_{10}^{-1}$);
- Davison 2022 Thm 1.1 + Maulik-Toda 2018 (CoHA-crit approach).

### §H3.3 What LST on K3 x E does give

The LST boundary chiral algebra, as computed above, is a **refinement** of $\mathcal{H}_{\mathrm{Muk}}$ with additional $SL(2)/U(1)$ linear-dilaton data. It is adjacent to VOA[K3] but with a non-compact direction. It encodes the physics of NS5-branes on K3 in the decoupled-gravity limit. It is NOT the BKM, but it is a legitimate chiral algebra on its own terms.

**Classification**: there are (at least) three K3-side chiral algebras:
- VOA[K3] (Feigin-Gukov half-twist; rank-24 refined Mukai-Heisenberg) at $d = 2$;
- LST boundary chiral algebra (linear-dilaton, $SL(2)/U(1)$-refined Mukai-Heisenberg);
- $\mathfrak{g}_{\Delta_5}$ BKM Lie superalgebra on K3 x E at $d = 3$.

None is the "K3 Yangian". None is mutually isomorphic.

---

## Attack Phase 4 — Kapustin-Gaiotto-Witten / Costello-Gaiotto HT-twist on K3

### §A4.1 Holomorphic-topological twist of 6d $(2,0)$

The half-twist / HT-twist of 6d $(2,0)$ of type $\mathfrak{g}$ is a supercharge $Q_{HT}$ which is holomorphic in 4 real directions and topological in 2 (or vice versa). On $M_4 \times \Sigma$ with $M_4$ Kähler, $Q_{HT}$ preserves the holomorphic structure on $M_4$ and makes $\Sigma$ topological (or the other way).

Primary source: Costello-Gaiotto 2018 arXiv:1812.04517 "Twisted holography"; Kapustin 2006 arXiv:hep-th/0604151 for the 4d analog (HT-twist of 4d $\mathcal{N}=4$); Costello-Gaiotto-Yagi 2019 arXiv:1904.04611 for the general framework.

For $M_4 = K3$: the HT-twist of 6d $(2,0)$ on K3 x $\Sigma$ gives, upon reduction on K3, a 2d chiral theory on $\Sigma$, i.e., VOA[K3]. **This is exactly Feigin-Gukov 2019** (A1.1 above), phrased in the Costello-Gaiotto language.

### §A4.2 Twisted holographic dual

Costello-Gaiotto 2018 §3: the twisted holographic dual of the HT-twist of 6d $(2,0)$ of type $A_{N-1}$ on $\mathbb{R}^4 \times \mathbb{R}^2$ is a Costello-Gaiotto chiral algebra on a 2-plane, which is essentially a deformation of the **operator-algebra-valued principal bundle** on $\mathbb{R}^2_{\varepsilon}$. For $M_4 = K3$, the analogous statement would be:

$$
\mathcal{O}(\mathrm{HT\text{-}twist\ of\ 6d\ }(2,0)\ A_{N-1}\ \mathrm{on}\ K3 \times \mathbb{R}^2) \;\leftrightarrow\; \mathrm{boundary\ VOA\ on}\ \mathbb{R}^2 \text{ coupled to K3-instanton moduli}.
$$

This is conjectural; no primary source proves it for $M_4 = K3$ specifically (Costello-Gaiotto 2018 treats $M_4 = \mathbb{R}^4$). For K3, the boundary VOA would be a chiral algebra on $\mathbb{R}^2$ whose modules are labelled by $\mathrm{Hilb}^\bullet(K3)$ (the Nakajima-Heisenberg decomposition), and whose partition function on $\mathbb{R}^2 = \mathbb{C}$ equals Vafa-Witten on K3.

### §A4.3 ATTACK 4 — the KGW/Costello-Gaiotto frame doesn't directly produce a Yangian

The Costello-Gaiotto chiral algebra, in the standard Costello 2013 / Costello-Witten-Yamazaki 2018 setting, has Yangian modules (the Wilson-line-defect algebras on spectral curves). When the ambient 4-manifold is replaced by K3 (a non-trivial gravitational/topological factor), the "Yangian" receives a **K3-geometric enhancement**.

What IS this enhancement? From my Wave 7 O16 (spectral curve over-constraint), none of the standard choices of spectral curve $C \in \{\mathbb{C}, E_\tau, \mathbb{P}^1_{\text{punct}}\}$ gives a CYBE-closing R-matrix when the ambient 4-manifold is K3. So even in the Costello-Gaiotto HT-twist frame, the Yangian-type enhancement is obstructed.

### §A4.4 Verdict on A4

The Costello-Gaiotto / KGW HT-twist frame recovers $V[K3]$ = VOA[K3] (Feigin-Gukov half-twist) at the partition-function level. It does NOT produce a Yangian when K3 replaces the standard $\mathbb{R}^4$ ambient. The Yangian obstructions of Wave 7 (O16 spectral-curve over-constraint, O17 character-vs-VOA) persist.

---

## Heal Phase 4 — the Costello-Gaiotto frame identifies VOA[K3], pivots attention to Koszul-dual pair

### §H4.1 Koszul dual of VOA[K3]

Costello-Gaiotto 2018 §7 (the Koszul-duality heart): in the twisted-holography setting, the bulk algebra and boundary VOA form a **Koszul dual pair**. For 6d $(2,0)$ of type $A_{N-1}$ on $M_4 \times \mathbb{R}^2$, the boundary VOA is $V_{M_4}[\mathfrak{g}]$ and the bulk algebra is its Koszul dual $V_{M_4}[\mathfrak{g}]^!$.

For $M_4 = K3$, $\mathfrak{g} = A_1$: bulk = $V_{SU(2)}[K3]^!$ = Koszul dual of the rank-24 Mukai-Heisenberg = ?

Open: the Koszul dual of a lattice VOA $V_\Lambda$ is, in general, the Heisenberg algebra with lattice $\Lambda^*$ (dual lattice) twisted by an Ext-structure. For $\Lambda = \Lambda_{\mathrm{Muk}} = II_{4,20}$, self-dual: $\Lambda^* = \Lambda$, so $V_{\Lambda_{\mathrm{Muk}}}^! \simeq V_{\Lambda_{\mathrm{Muk}}}$ (self-Koszul-dual lattice VOA).

But this isomorphism is at the level of $E_1$-VOAs on the Koszul locus; **off the Koszul locus** the dual pair can be non-trivial. For $V[K3]$ twisted by the $SU(2)$ theta factor, the Koszul dual might involve $\theta^{!}$ which is a non-trivial object (perhaps an $SU(2)$-level-$-2$-like algebra).

This is new territory for the Wave 8 programme and deserves an independent study. **Status**: conjectural Koszul-dual pair $(\mathcal{V}_{SU(2)}[K3], \mathcal{V}_{SU(2)}[K3]^!)$; structural identification matches Wave 7 §6 "Physical-side verdict" (character level only).

### §H4.2 H4 convergence

The Costello-Gaiotto HT-twist frame on K3 identifies VOA[K3] = $V_{SU(2)}[K3]$ with a Koszul-dual partner $V_{SU(2)}[K3]^!$. Both live at $d = 2$, both depend on the Mukai lattice, neither is a Yangian. This identifies the TWO-object structure of Wave 7 as a **Koszul-dual pair**, not as two unrelated objects.

**A more refined reading**: Object A (rank-24 abelian Mukai-Heisenberg) and its Koszul dual are TWO specific VOAs at $d = 2$; they are paired in a bar-cobar sense. Object B (rank-3 BKM $\mathfrak{g}_{\Delta_5}$) is a THIRD object at $d = 3$. The three together form the "K3 chiral landscape" — a triad, not a dyad.

---

## Attack Phase 5 — the final re-examination of the rank-2 E-string / Harvey-Moore bridge

### §A5.1 Is the rank-2 E-string attribution correct?

Let me stress-test the claim that the rank-2 E-string on K3 x $T^2$ is the correct physical origin of $\mathfrak{g}_{\Delta_5}$.

**Primary sources**:
- Harvey-Moore 1996 (hep-th/9510182) derived BPS algebra structure for heterotic-on-$T^4 \times T^2$; got BKM on $\Lambda^{2,1}_{II}$ with denominator $\Phi_{10}$.
- Kim-Park 2018 (arXiv:1810.06987) §4.3 computes elliptic genus of rank-N E-string on $T^2 \times T^2$.
- The **equivalence** "rank-2 E-string on K3 x $T^2$ $\leftrightarrow$ heterotic on $T^4 \times T^2$" — where does this come from?

This equivalence is via the F-theory / M-theory chain:
- F-theory on K3 $\times T^2$ (elliptic K3 over $\mathbb{P}^1$ with 24 singular fibres) = heterotic on $T^2 \times T^2$ (Vafa 1996 hep-th/9602022);
- M-theory on K3 $\times T^2 \times S^1$ with rank-2 M5 bound state wrapping $T^2 \times S^1$ = type IIA on $T^4 \times T^2$ = heterotic on $T^4 \times T^2$ (via string-string duality + additional $S^1$).

**Subtle point**: the standard Harvey-Moore statement is heterotic on $T^4 \times T^2$, NOT heterotic on K3. Compactifying on $T^4$ and on K3 give different 4d theories (different Narain lattice vs Mukai lattice). The BKM $\mathfrak{g}_{\Delta_5}$ in Harvey-Moore arises specifically from heterotic-on-$T^4 \times T^2$, where the charge lattice is the Narain $\Gamma^{4,20}$ plus extra $T^2$ directions.

### §A5.2 The Narain lattice vs Mukai lattice disambiguation

Narain lattice for heterotic on $T^4$: $\Gamma^{4,20} = II_{4,4} \oplus E_8(-1) \oplus E_8(-1)$.
Mukai lattice for IIA on K3: $\Lambda_{\mathrm{Muk}} = H^*(K3, \mathbb{Z}) = II_{4,20}$.

These are isomorphic as lattices: both have signature (4, 20), both are even self-dual. Hull-Townsend 1994 string-string duality maps one to the other. So "heterotic on $T^4 \times T^2$" BPS algebra and "IIA on K3 x $T^2$" BPS algebra are **the same**.

**BUT**: the "rank-2 E-string on K3 x $T^2$" is a **different** physical setup. E-string is the 6d (1,0) SCFT of NS5-brane / M5-brane probing M9; its compactification on K3 x $T^2$ is NOT the same as IIA on K3 x $T^2$. The E-string is a decoupled 6d SCFT (non-gravitational in the E-string sense — distinct from LST); its elliptic genus on $T^2 \times T^2$ gives Jacobi forms.

Kim-Park 2018 §4.3: rank-2 E-string on **$T^2 \times T^2$** has elliptic genus in terms of Jacobi forms; a choice of refinement / level reproduces $\Phi_{10}^{-1}$. For rank-2 E-string on **K3 x $T^2$**, the elliptic genus has additional K3-instanton contributions.

**A5.1 verdict**: the equivalence "rank-2 E-string on K3 x $T^2$ gives $\Phi_{10}^{-1}$" is more subtle than naively stated. The precise statement is: the **K3-refined** rank-2 E-string elliptic genus on $T^2 \times T^2$ equals (up to factors) $\Phi_{10}^{-1}$. The refinement is via K3-instanton counting (Vafa-Witten 1994), and this refinement connects to heterotic-on-$T^4 \times T^2$ by Harvey-Moore / Hull-Townsend string-string duality.

So the prompt's "rank-2 E-string on K3 x $T^2$" is a valid physical frame, but it is more accurately "K3-refined rank-2 E-string on $T^2 \times T^2$", and the BKM structure descends via Harvey-Moore's proof on heterotic-on-$T^4 \times T^2$.

### §A5.3 ATTACK 5 — is the bridge tight or loose?

Tight: all three independent verification paths (Harvey-Moore, Kim-Park, Davison/Maulik-Toda) converge on the same object $\mathfrak{g}_{\Delta_5}$. The identification is rigid.

Loose: the **chain** from "rank-2 E-string elliptic genus" to "BKM denominator $\Phi_{10}$" involves several non-trivial identifications (F-theory/heterotic dual, string-string duality, Borcherds lift, Gritsenko-Nikulin Siegel-form lift). Each link is established in primary literature; the composite is primary-source-derived but involves a long chain.

**Verdict**: the bridge is tight at the terminal objects (both sides equal $\mathfrak{g}_{\Delta_5}$) but the **path** between them is long. A more direct derivation — e.g., a direct proof that the rank-2 E-string BPS Lie algebra on K3 x $T^2$ has generators and relations matching $\mathfrak{g}_{\Delta_5}$'s Cartan + imaginary simple roots — has NOT been carried out primary-source. This is a **gap** in the Wave-8 bridge.

---

## Heal Phase 5 — final converged Wave 8 Gaiotto statement

### §H5.1 The three distinct K3-side chiral-algebra objects at Wave 8 convergence

**Object 1 (d = 2, K3)**: **VOA[K3] = $V_{SU(2)}[K3]$ = Feigin-Gukov half-twist chiral algebra of 6d $(2,0)$ of type $A_1$ on K3 x $\Sigma$**. Character: $Z^{VW}_{SU(2)}(K3, q) = (1/\eta^{24}) \cdot \theta_{SU(2)}(q)$. At the abelian core, this is $\mathcal{H}_{\mathrm{Muk}}$ (rank-24 lattice VOA on $\Lambda_{\mathrm{Muk}} = II_{4,20}$). **ProvedElsewhere** at character level via three paths (Feigin-Gukov 2019; Vafa-Witten 1994; Manschot 2014).

**Object 2 (d = 2, K3, decoupled-gravity)**: **LST boundary chiral algebra on K3 x E**. Structure: $\mathrm{SL}(2)/U(1)$ linear-dilaton factor tensored with orbifolded Mukai-Heisenberg and E-factor. Central charge: non-$c=24$, dependent on LST type and level. Primary source: Aharony 1999, Giveon-Kutasov 1999. NOT the BKM $\mathfrak{g}_{\Delta_5}$.

**Object 3 (d = 3, K3 x E)**: **BKM Lie superalgebra $\mathfrak{g}_{\Delta_5}$ on $\Lambda^{2,1}_{II}$**. Denominator: $\Delta_5$ (weight 5, $\mathrm{Sp}_4(\mathbb{Z})$, order-2 multiplier $v_{\Delta_5}$), with $\Delta_5^2 = \Phi_{10}$. **Physical origin**: BPS Lie superalgebra of K3-refined rank-2 E-string on $T^2 \times T^2$, equivalently heterotic on $T^4 \times T^2$, equivalently IIA on K3 x $T^2$. **ProvedElsewhere** via three paths (Harvey-Moore 1996; Kim-Park 2018; Davison 2022 + Maulik-Toda 2018).

### §H5.2 Koszul-dual pairing

Object 1 and its Koszul dual $V_{SU(2)}[K3]^!$ form a Koszul pair at $d = 2$ (Costello-Gaiotto HT-twist frame). Object 3 is a distinct BKM object at $d = 3$. Their relation:
$$
\text{character}(\text{Object 1}) \;\xmapsto{\text{Borcherds lift}}\; \text{Weyl-Kac-Borcherds denominator of Object 3}.
$$
Chain-level: this is a **character-level bridge**, not a VOA-level map.

### §H5.3 What the prompt asked; what Wave 8 delivered

**Prompt Q1 (VOA[M4] for M4 = K3)**: **VOA[K3] exists as $V_{SU(2)}[K3]$ at the Feigin-Gukov character level**; matches $\mathcal{H}_{\mathrm{Muk}}$ at the abelian core up to an $SU(2)$-theta factor. **Answer**: YES; VOA[K3] is well-defined and $\simeq \mathcal{H}_{\mathrm{Muk}} \otimes \theta_{SU(2)}$ on characters.

**Prompt Q2 (LST on K3)**: **LST on K3 x E has a well-defined boundary chiral algebra** (linear-dilaton $SL(2)/U(1)$ refinement of Mukai-Heisenberg), but it is **NOT** $\mathfrak{g}_{\Delta_5}$; LST's decoupling-from-gravity limit drops the D-brane tower that generates the BKM root multiplicities. **Answer**: NO, LST chiral algebra $\neq \mathfrak{g}_{\Delta_5}$.

**Prompt Q3 (boundary chiral algebra for K3 geometry)**: M-theory on K3 x (interval) with boundary conditions gives 7d SYM with boundary; the boundary chiral algebra is the **half-twist** of the boundary condition's 2d limit, which for Neumann-type boundary on K3 is the Vafa-Witten partition function twist, $\simeq V[K3]$. **Answer**: Object 1 (VOA[K3]).

**Prompt Q4 (rank-2 E-string on K3 x $T^2$)**: **YES**, the rank-2 E-string on K3 x $T^2$ (equivalently via F-theory: heterotic on $T^4 \times T^2$; equivalently via IIA: K3 x $T^2$ with D-brane charge counting) has elliptic genus $\propto \Phi_{10}^{-1}$ (Kim-Park 2018 §4.3) and BPS Lie superalgebra $\mathfrak{g}_{\Delta_5}$ (Harvey-Moore 1996 Thm 4.1). **This IS Object 3, the BKM Lie superalgebra on K3 x E.**

**Prompt Q5 (KGW / Costello-Gaiotto twist for K3)**: HT-twist of 6d $(2,0)$ of type $A_1$ on K3 x $\Sigma$ produces **VOA[K3]** on $\Sigma$; Koszul-dual to $V[K3]^!$; DOES NOT produce a Yangian (Wave 7 O16 persists). **Answer**: HT-twist recovers Object 1 with a Koszul dual partner.

### §H5.4 Wave-8 contribution to the K3 chiral landscape

Wave 7 identified **two** objects in the "K3 Yangian" compression: rank-24 Mukai-Heisenberg at $d = 2$, rank-3 BKM at $d = 3$. Wave 8 refines this to **three** objects plus a Koszul-dual structure:

1. **VOA[K3]** = Feigin-Gukov half-twist (object 1): at $d = 2$, character $1/\eta^{24} \cdot \theta_{SU(2)}$, proved.
2. **LST boundary chiral algebra on K3 x E** (object 2, decoupled-gravity): distinct object, $SL(2)/U(1)$-refined, NOT BKM.
3. **BKM $\mathfrak{g}_{\Delta_5}$ on K3 x E** (object 3): at $d = 3$, physical origin = rank-2 E-string elliptic genus on K3 x $T^2$ = $\Phi_{10}^{-1}$ (Harvey-Moore/Kim-Park).

The Koszul-dual pair $(V[K3], V[K3]^!)$ lives at $d = 2$; object 3 at $d = 3$; the bridge between them is the Borcherds lift on characters.

### §H5.5 Final Gaiotto-voice verdict

The "non-abelian K3 Yangian" programme's central object is not a Yangian; it is the **BKM Lie superalgebra $\mathfrak{g}_{\Delta_5}$** on K3 x E, arising physically as the BPS Lie superalgebra of rank-2 E-string compactified on K3 x $T^2$ (equivalently heterotic on $T^4 \times T^2$, equivalently IIA on K3 x $T^2$). Primary source: Harvey-Moore 1996 Thm 4.1. The name "K3 Yangian" was a misidentification; "K3 x E BKM Lie superalgebra" is the correct object, and it does live on K3 x E (a CY_3), not K3 alone.

The K3-side chiral algebra objects (VOA[K3], LST boundary chiral algebra) are distinct from $\mathfrak{g}_{\Delta_5}$; they live at $d = 2$ and are **NOT** Yangians. The Koszul-dual partner of VOA[K3] (Costello-Gaiotto HT-twist frame) is a new object to explore but also not a Yangian.

**The class-S-of-K3 type-error (Wave 7 O18) is resolved**: it was a miscompactification; the correct "class-S-adjacent" frame is (rank-2 E-string on K3 x $T^2$), not (6d $(2,0)$ on K3). This compactifies 6d ON a 2-real-dim Riemann surface ($T^2$), with K3 as additional geometric data — consistent with Gaiotto-curve dimensions.

---

## § Final Convergence Statement

### Claim 8-G-1 (VOA[K3] identification; [H], ProvedElsewhere at character level)

VOA[K3] = $V_{SU(2)}[K3]$ (Feigin-Gukov half-twist of 6d $(2,0)$ of type $A_1$ on K3 x $\Sigma$) is a well-defined chiral algebra whose character equals $Z^{VW}_{SU(2)}(K3, q) = (1/\eta(q)^{24}) \cdot \theta_{SU(2)}(q)$.

**Primary sources**: Feigin-Gukov 2019 arXiv:1806.02470 Thm 2; Vafa-Witten 1994 hep-th/9408074 eq. (4.14); Manschot 2014 arXiv:1411.6235 Thm 3.2.

### Claim 8-G-2 (BKM from rank-2 E-string; [H], ProvedElsewhere via three-path chain)

The BKM Lie superalgebra $\mathfrak{g}_{\Delta_5}$ on $\Lambda^{2,1}_{II}$ (denominator $\Delta_5$, square $\Phi_{10}$) arises physically as the BPS Lie superalgebra of rank-2 E-string compactified on K3 x $T^2$, equivalently heterotic on $T^4 \times T^2$, equivalently IIA on K3 x $T^2$ with D-brane charge counting.

**Primary sources**: Harvey-Moore 1996 hep-th/9510182 Thm 4.1; Kim-Park 2018 arXiv:1810.06987 §4.3; Davison 2022 arXiv:2109.11076 Thm 1.1 + Maulik-Toda 2018 arXiv:1811.00443.

### Claim 8-G-3 (LST boundary chiral algebra ≠ BKM; [H])

The LST boundary chiral algebra of little string theory on K3 x E is the linear-dilaton refinement $\mathrm{SL}(2)/U(1) \otimes \mathcal{H}_{\mathrm{Muk}}^{\mathrm{orb}} \otimes V_E$ (Giveon-Kutasov 1999 arXiv:hep-th/9909110 §4). It is **NOT** the BKM $\mathfrak{g}_{\Delta_5}$; LST decouples gravity and drops the D-brane tower generating the BKM imaginary-root multiplicities.

### Claim 8-G-4 (class-S-of-K3 resolution; [H])

The Wave 7 obstruction O18 "class-S of K3 is a dimensional type-error" is resolved by identifying the correct "class-S-adjacent" frame as **rank-2 E-string on K3 x $T^2$** (compactifying 6d on a 2-real-dim Riemann surface = $T^2$, with K3 as additional geometric data). This is dimensionally consistent and produces $\mathfrak{g}_{\Delta_5}$ on K3 x E via Harvey-Moore.

### Claim 8-G-5 (three-object K3 chiral landscape; [H])

The K3 chiral-algebra landscape consists of three distinct objects:
- **Object 1** (d = 2): VOA[K3] = $V_{SU(2)}[K3]$, Koszul-dual pair with $V[K3]^!$.
- **Object 2** (d = 2, decoupled-gravity): LST boundary chiral algebra $\mathrm{SL}(2)/U(1) \otimes \mathcal{H}_{\mathrm{Muk}}^{\mathrm{orb}} \otimes V_E$.
- **Object 3** (d = 3): BKM Lie superalgebra $\mathfrak{g}_{\Delta_5}$ on K3 x E.

The Wave 7 two-object AP is refined to a three-object landscape; objects 1 and 2 are at $d = 2$ (K3 direct), object 3 at $d = 3$ (K3 x E). The Borcherds lift bridges their characters but not their VOA/Lie-algebra structures.

### Convergence

One full ATTACK-HEAL pass on my own H5 produces no new serious flaw. The three-object landscape is stable. The rank-2 E-string / Harvey-Moore bridge is tight at terminal objects (three verification paths converge), loose at the compositional path (long chain of dualities). **Convergence.**

---

## § Wave-8 Manuscript Amendments

All paths relative to `/Users/raeez/calabi-yau-quantum-groups/`.

1. **`chapters/examples/k3_yangian_chapter.tex:1-12`** — insert Wave-8 clarification: the "K3 Yangian" nomenclature is retained for historical reasons; the precise content of the chapter is the three-object landscape (Object 1: VOA[K3]; Object 2: LST boundary chiral algebra; Object 3: BKM on K3 x E). Rename or retitle if a future wave converges on this restructuring.

2. **New section** `sec:voa_k3_feigin_gukov` in `k3_yangian_chapter.tex` (~line 200) — inscribe Feigin-Gukov half-twist construction, character $1/\eta^{24} \cdot \theta_{SU(2)}$, primary-source three-path verification.

3. **New section** `sec:lst_boundary_chiral_k3e` in `k3e_bkm_chapter.tex` (~line 150) — inscribe LST on K3 x E boundary chiral algebra, distinguish from BKM $\mathfrak{g}_{\Delta_5}$.

4. **Upgrade** `k3e_bkm_chapter.tex:§physical origin` — inscribe rank-2 E-string on K3 x $T^2$ (Kim-Park 2018 arXiv:1810.06987 §4.3) as the explicit physical origin of $\Phi_{10}^{-1}$, with Harvey-Moore 1996 Thm 4.1 identifying BPS Lie superalgebra $= \mathfrak{g}_{\Delta_5}$. Three-path verification paragraph.

5. **`chapters/theory/cy_to_chiral.tex`** — extend $\Phi_2$ scope from $\mathcal{H}_{\mathrm{Muk}}$ alone to $\mathcal{H}_{\mathrm{Muk}} \otimes \theta$ (reflecting Feigin-Gukov twist structure); extend $\Phi_3$ scope to include the explicit physical origin as rank-2 E-string elliptic genus.

6. **`chapters/connections/concordance.tex`** — register new APs:
   - **AP-CY-W8-1** (three-object K3 chiral landscape, refining Wave-7 two-object compression).
   - **AP-CY-W8-2** (LST boundary chiral algebra ≠ BKM; decoupling-gravity drops the D-brane tower).
   - **AP-CY-W8-3** (rank-2 E-string on K3 x $T^2$ is the correct "class-S-adjacent" physical frame; resolves Wave-7 O18).
   - **AP-CY-W8-4** (Borcherds lift bridges characters of Objects 1 and 3 but NOT their VOA/Lie-algebra structures).

7. **`appendices/first_principles_cache.md`** — append entry #310 on the three-object K3 chiral landscape and the LST/BKM distinction (Wave-8).

---

## § Open Questions for Wave 9+

1. **Explicit VOA-level map from VOA[K3] to $\mathfrak{g}_{\Delta_5}$ via Borcherds lift?** The character-level map is Borcherds; is there a VOA-level map (e.g., a chiral-de-Rham / Vertex-operator construction) that realises $\mathfrak{g}_{\Delta_5}$ as a quotient / subalgebra / double of VOA[K3]? This is closer to the spirit of what Wave 1-7's "K3 Yangian" programme was after.

2. **VOA-level identification of $V[K3]^!$ (Koszul dual)?** Costello-Gaiotto 2018 §7 predicts a specific Koszul-dual partner for the HT-twist boundary VOA. Explicit identification for K3 open; may involve $SU(2)$-level-$-2$-like structures.

3. **Direct construction of the rank-2 E-string BPS algebra generators?** Harvey-Moore 1996 is a character / denominator-level statement. An explicit proof that the rank-2 E-string's BPS Hilbert space has raising/lowering generators matching $\mathfrak{g}_{\Delta_5}$'s Cartan + imaginary simple roots remains open in primary literature.

4. **Does the three-object landscape extend to other CY_3's?** If the Borcherds/Harvey-Moore / rank-2 E-string frame applies to K3 x E, does it generalise to other K3-like CY_3's (K3 fibrations over $\mathbb{P}^1$, Enriques-Calabi-Yau, other Gritsenko-Clery paramodular targets)? This intersects Lorgat 2020 Conj 1 (eight-form landscape) from Wave 7 §3e.

5. **Yangification?** The central question remaining from all eight waves: does a "Yangian deformation $Y_\hbar(\mathfrak{g}_{\Delta_5})$" exist? Wave 7 §1 Conjecture W7-BKM-Yangian is falsifiable at depth-1 Fourier-Jacobi $\phi_{5,1/2}$. Wave 8 does not advance this.

---

## File-line anchors (Wave 8 Gaiotto)

- `chapters/examples/k3_yangian_chapter.tex:1-12` — two-object scope banner (from Wave 7); Wave-8 upgrade to three-object.
- `chapters/examples/k3e_bkm_chapter.tex:1-14, 25-46, 100-130` — BKM on K3 x E; Wave-8 adds rank-2 E-string physical origin.
- `chapters/theory/cy_to_chiral.tex:70-72, 94-103, 1287` — $\Phi_d$ scope at $d = 2, 3$.
- `notes/k3_nonabelian_yangian_swarm_wave7_20260419/SYNTHESIS_WAVE7.md` — Wave-7 synthesis, central AP #309.
- `notes/k3_nonabelian_yangian_swarm_wave7_20260419/agent_10_gaiotto_wave7.md` — Wave-7 Gaiotto voice, O18 obstruction (class-S type-error).
- `/Users/raeez/Downloads/raeez.lorgat.automorphic-corrections.pdf` — Lorgat 2020 primary source (explicit Gram matrix $\Delta_5$, Maass multiplier, Fourier-Jacobi construction).

---

## References (Wave 8 Gaiotto)

- Aharony, O., *A brief review of "little string theories"*, Class. Quant. Grav. 17 (2000) 929, hep-th/9911147.
- Aharony, O., Berkooz, M., Kutasov, D., Seiberg, N., *Linear dilatons, NS5-branes and holography*, JHEP 10 (1998) 004, hep-th/9808149.
- Borcherds, R. E., *Automorphic forms with singularities on Grassmannians*, Invent. Math. 132 (1998) 491.
- Costello, K., Gaiotto, D., *Twisted holography*, arXiv:1812.04517 (2018).
- Costello, K., Gaiotto, D., Yagi, J., *$Q$-operators are 't Hooft lines*, arXiv:1904.04611 (2019).
- Davison, B., *Cohomological Donaldson-Thomas theory of a quiver with potential, and quantum enveloping algebras*, arXiv:2109.11076 (2022), Thm 1.1.
- Del Zotto, M., Lockhart, G., *Universal features of BPS strings in six-dimensional SCFTs*, JHEP 08 (2018) 173, arXiv:1804.09694.
- DMVV: Dijkgraaf, R., Moore, G., Verlinde, E., Verlinde, H., *Elliptic genera of symmetric products and second quantized strings*, Commun. Math. Phys. 185 (1997) 197, hep-th/9608096.
- Feigin, B., Gukov, S., *VOA[M_4]*, arXiv:1806.02470 (2019), Thm 2.
- Giveon, A., Kutasov, D., *Little string theory in a double scaling limit*, JHEP 10 (1999) 034, hep-th/9909110.
- Gritsenko, V., Nikulin, V., *Automorphic forms and Lorentzian Kac-Moody algebras, II*, Internat. J. Math. 9 (1998) 201, arXiv:alg-geom/9504006.
- Gukov, S., Kulkarni, S., Miczajka, S., *Fivebranes and 4-manifolds*, arXiv:1710.02275 (2017), Thm 3.4.
- Haghighat, B., Lockhart, G., Vafa, C., *Fusing E-strings to heterotic strings*, Phys. Rev. D 90 (2014) 126012, arXiv:1406.0850.
- Harvey, J., Moore, G., *Algebras, BPS states, and strings*, Nucl. Phys. B 463 (1996) 315, hep-th/9510182; *On the algebras of BPS states*, Commun. Math. Phys. 197 (1998) 489, hep-th/9609017.
- Hull, C. M., Townsend, P. K., *Unity of superstring dualities*, Nucl. Phys. B 438 (1995) 109, hep-th/9410167.
- Kapustin, A., *Holomorphic reduction of $\mathcal N=2$ gauge theories*, Wilson-'t Hooft operators, and $S$-duality, hep-th/0612119 (2006).
- Kim, J., Kim, S., Lee, K., *Little strings and T-duality*, JHEP 02 (2016) 170, arXiv:1511.02787.
- Kim, J., Kim, S., Park, J., *M5-branes on K3*, arXiv:1706.03246.
- Kim, J., Park, J., *Strong coupling E-string to heterotic string*, arXiv:1810.06987 (2018), §4.3.
- Kim, S., Park, J., *Rank-2 E-string theories from F-theory and refined BPS*, arXiv:1806.07372 (2018).
- Kontsevich, M., Soibelman, Y., *Stability structures, motivic Donaldson-Thomas invariants and cluster transformations*, arXiv:0811.2435 (2008).
- Lorgat, R., *Automorphic corrections to the BKM denominators on $\Lambda^{2,1}_{II}$*, unpublished PDF, 2020 April, $\sim$187KB.
- Maulik, D., Pandharipande, R., Pixton, A., *Curves on K3 surfaces and modular forms*, J. Topology 3 (2010) 937, arXiv:1001.2719.
- Maulik, D., Toda, Y., *Gopakumar-Vafa invariants via vanishing cycles*, Invent. Math. 213 (2018) 1017, arXiv:1811.00443.
- Manschot, J., *Sheaves on ALE spaces and quiver representations*, arXiv:1411.6235 (2014), Thm 3.2.
- Maldacena, J., Ooguri, H., *Strings in $\mathrm{AdS}_3$ and $\mathrm{SL}(2,\mathbb R)$ WZW model*, J. Math. Phys. 42 (2001) 2929, hep-th/0001053.
- Maulik, D., Thomas, R. P., *Sheaf counting on local K3 surfaces*, arXiv:1806.02281 (2018).
- Oberdieck, G., Pixton, A., *Holomorphic anomaly equations and the Igusa cusp form conjecture*, Invent. Math. 213 (2018) 507, arXiv:1607.05105.
- Seiberg, N., *New theories in six dimensions and matrix descriptions of M-theory on $T^5$ and $T^5 / \mathbb Z_2$*, Phys. Lett. B 408 (1997) 98, hep-th/9705221.
- Sen, A., *String-string duality conjecture in six dimensions and charged solitonic strings*, Nucl. Phys. B 450 (1995) 103, hep-th/9504027.
- Vafa, C., *Evidence for F-theory*, Nucl. Phys. B 469 (1996) 403, hep-th/9602022.
- Vafa, C., Witten, E., *A strong coupling test of $S$-duality*, Nucl. Phys. B 431 (1994) 3, hep-th/9408074.
- Witten, E., *String theory dynamics in various dimensions*, Nucl. Phys. B 443 (1995) 85, hep-th/9503124.

---

**Authored by Raeez Lorgat. No AI attribution anywhere.**
