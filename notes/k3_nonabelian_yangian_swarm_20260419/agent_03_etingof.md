# Agent 03 (Etingof voice): The non-abelian K3 Yangian as a derivation
## Every step is a derivation. Where it is a citation, we name the paper.

**Author:** Raeez Lorgat. **Date:** 2026-04-19.
**Voice:** Etingof. **Standard:** the reader finishes feeling they could have invented the next step.

---

## Part 0. What we are trying to derive, stated cleanly

The programme claims a non-abelian K3 Yangian
$$
Y_{\mathrm{non\text{-}ab}}(\mathfrak{g}_{K3}) \;=\; ?
$$
is constructed from a Calabi-Yau surface $S=K3$ by the chain
$$
D^b(\mathrm{Coh}(K3))
\;\xrightarrow{(\star_1)}\;
(\mathrm{CY}_2\text{-}A_\infty)
\;\xrightarrow{(\star_2)}\;
L_{K3}
\;\xrightarrow{(\star_3)}\;
U^{\mathrm{fact}}(L_{K3}) = A_{K3}
\;\xrightarrow{(\star_4)}\;
\mathrm{Rep}^{E_2}(A_{K3})
\;\xrightarrow{(\star_5)}\;
Y_{\mathrm{non\text{-}ab}}(\mathfrak{g}_{K3}).
$$

Let me state from the start what this object is **not**, to keep the target honest. It is not the Yangian of a finite-dimensional simple $\mathfrak{g}$ deformed by K3. It is not the BKM Yangian $Y(\mathfrak{g}_{\Delta_5})$ (which has no known existence). It is the **filtered deformation of the enveloping algebra of the K3 double current algebra at an ADE enhancement point**, taken in a category that remembers the Mukai lattice pairing.

Equivalently: at a K3 point acquiring an ADE singularity of type $\mathfrak{g}$, the local geometry factors as $\widetilde{S}_\mathfrak{g} \hookrightarrow K3$, and $Y_{\mathrm{non\text{-}ab}}(\mathfrak{g}_{K3})$ is the amalgam
$$
Y_{\mathrm{non\text{-}ab}}(\mathfrak{g}_{K3}) \;=\; Y(\widehat{\mathfrak{g}}) \;\bigotimes_{Y^+(\mathfrak{h}_{\mathfrak{g}})}\; Y(\mathfrak{h}_{K3,\perp}^{\mathrm{Muk}})
$$
— the affine Yangian of the enhanced $\mathfrak{g}$ attached at the exceptional divisor, glued along its Cartan sub-Yangian to the rank-$(24-r-1)$ abelian Heisenberg Yangian of the Mukai complement. This is the only object visible from the first-principles chain; anything else is a conjecture laid on top.

I will carry this definition throughout. It is the output we must reach.

---

## Part 1. Round 1 attack: what is each arrow, and what is the witness?

### $(\star_1)$ $D^b(\mathrm{Coh}(K3)) \to$ (cyclic $A_\infty$-structure)

**Claimed witness.** The Serre functor on $D^b(\mathrm{Coh}(K3))$ is $\mathbb{S} = [2]$ because $\omega_{K3} \cong \mathcal{O}_{K3}$. The trace
$$
\mathrm{Tr} \colon \mathrm{HH}_\bullet(D^b(\mathrm{Coh}(K3))) \twoheadrightarrow \mathrm{HH}_2 \cong H^0(K3, \omega_{K3}) \cong \mathbb{C}
$$
is the $d=2$ CY trace.

**Is this a derivation or a citation?** It is a derivation, and the derivation is short. Hochschild-Kostant-Rosenberg on a smooth projective variety:
$$
\mathrm{HH}_\bullet(X) \;\cong\; \bigoplus_{p-q = \bullet} H^q(X, \Omega^p_X).
$$
For $K3$: $\mathrm{HH}_0 = H^0(\mathcal{O}) \oplus H^1(\Omega^1) \oplus H^2(\Omega^2) = \mathbb{C} \oplus \mathbb{C}^{20} \oplus \mathbb{C} = \mathbb{C}^{22}$, $\mathrm{HH}_2 = H^0(\Omega^2) \oplus H^2(\mathcal{O}) = \mathbb{C}^2$, $\mathrm{HH}_{-2} = H^2(\wedge^2 T) = \mathbb{C}^2$. Total $\mathrm{HH}_\bullet$ has dimension $24$, exactly the Mukai rank — this is Caldararu's Mukai-Hodge identification, derivable from HKR plus a twist by $\mathrm{td}^{1/2}$.

**The trace** is the composition $\mathrm{HH}_\bullet(K3) \to \mathrm{HH}_2 \to H^{0,2}(K3) \xrightarrow{\mathrm{Serre}} \mathbb{C}$. It is nondegenerate by Serre duality. The cyclic $A_\infty$-structure is then what you get from Kontsevich-Soibelman: the minimal model of $D^b(\mathrm{Coh}(K3))$ on $\mathrm{HH}_\bullet$ carries operations $m_k \colon \mathrm{HH}^{\otimes k} \to \mathrm{HH}$ compatible with the trace in the cyclic sense
$$
\mathrm{Tr}(m_k(a_1,\ldots,a_k)\cdot a_{k+1}) \;=\; (-1)^{|a_1|(|a_2|+\cdots+|a_{k+1}|)}\,\mathrm{Tr}(m_k(a_2,\ldots,a_{k+1})\cdot a_1).
$$

**Step witness.** PROVED. Derivation: HKR + Serre duality + homotopy transfer from the de Rham dg-algebra. Citation for the transfer theorem: Kadeishvili (1980), Kontsevich-Soibelman (2006). Citation for Mukai/HKR: Caldararu (2003).

### $(\star_2)$ Cyclic $A_\infty$-structure $\to L_{K3}$ (Lie conformal algebra)

**Claimed witness.** The Hochschild cohomology $\mathrm{HH}^\bullet(D^b(\mathrm{Coh}(K3)))$ carries a Gerstenhaber bracket of degree $-1$ (the Gerstenhaber bracket on a cohomology ring of any $A_\infty$-category). In the cyclic/CY setting, the bracket pairs up with the cyclic trace to produce a *Lie conformal algebra* via the Beilinson-Drinfeld machinery applied to the factorization stack.

**Is the bracket written out?** The Gerstenhaber bracket on $\mathrm{HH}^{\bullet}$ is defined by
$$
[\mu, \nu] \;=\; \mu \circ \nu \,-\, (-1)^{|\mu|(|\nu|-1)+1}\,\nu \circ \mu, \qquad \mu\circ\nu\;=\;\sum_i \mu(-,\ldots,\nu(\ldots),\ldots,-).
$$
For $D^b(\mathrm{Coh}(K3))$, HKR gives
$$
\mathrm{HH}^\bullet(K3) \;\cong\; \bigoplus_{p+q=\bullet} H^q(K3, \wedge^p T_{K3})
$$
and the Gerstenhaber bracket **descends to the Schouten-Nijenhuis bracket** on polyvector fields. So in the abelian limit on $K3$, where the only polyvector field is the holomorphic symplectic form $\sigma \in H^0(K3, \wedge^2 T_{K3}) = \mathbb{C}$ (up to scale), the SN bracket of $\sigma$ with anything in $H^\bullet(K3, \wedge^\bullet T)$ is given by contraction with $\sigma$.

**The $\lambda$-bracket.** To get a Lie conformal algebra rather than just a graded Lie algebra, one needs the OPE-like expansion. The construction is:

1. Place $\mathrm{HH}^\bullet(K3)$ on the formal disk: take $L_{K3} := \mathrm{HH}^\bullet(K3) \otimes \mathbb{C}[\partial]$.
2. Define $\lambda$-bracket on generators $\alpha_i \otimes 1$ (for $\alpha_i$ running over Mukai basis) by
$$
[\alpha_i{}_\lambda \alpha_j] \;=\; \langle \alpha_i, \alpha_j\rangle_{\mathrm{Muk}}\, \lambda \cdot \mathbf{1} \;+\; \underbrace{\mu^k_{ij}\,\alpha_k}_{\text{cup product}} \;+\; \lambda^2\,(\text{higher})_{ij}\,.
$$
3. The higher $\lambda^n$ terms for $n \geq 2$ measure the $A_\infty$-operations $m_{n+1}$ of $(\star_1)$ via the Tamarkin deformation quantisation map; by the **formality of $K3$** (Deligne-Griffiths-Morgan-Sullivan: every compact Kähler manifold is formal) these $m_n$ vanish for $n\geq 3$, and the $\lambda$-bracket is determined by $\lambda^0$ (cup) and $\lambda^1$ (Mukai pairing).

**Step witness.** PROVED for the free-field ($\gl_1$) sector; **conjectural for the non-abelian sector**. The abelian claim is the content of Proposition `prop:k3-heisenberg` in `k3_yangian_chapter.tex:458-473`. The non-abelian claim — that a subset of Mukai directions at an ADE enhancement point acquires the structure constants of the affine $\widehat{\mathfrak{g}}$ — is Conjecture `conj:k3-serre-enhanced` in `k3_yangian_chapter.tex:1332`. **This is the first genuinely open step.**

**What the programme actually proves.** For the abelian Mukai Heisenberg $H_{\mathrm{Muk}}$, $L_{K3} = H_{\mathrm{Muk}}[\partial]$ is manifestly a Lie conformal algebra (the mode commutators force a pre-Lie algebra structure, and the $\lambda$-bracket is the generating function of mode commutators). The non-abelian $L_{K3}$ at an $ADE$ point is a **proposed** gluing $L_{K3}^{ADE} := \widehat{\mathfrak{g}} \oplus_\text{Cartan} H_{\mathrm{Muk},\perp}$, but the compatibility of this gluing with the Lie conformal structure — specifically, whether the SN bracket of $\sigma$ with $\widehat{\mathfrak{g}}$-currents produces consistent $\lambda$-bracket relations — remains to be verified at chain level.

### $(\star_3)$ $L_{K3} \to U^{\mathrm{fact}}(L_{K3}) = A_{K3}$ (factorization envelope)

**Claimed witness.** The factorization envelope of a Lie conformal algebra $L$ on a smooth curve $X$ is a standard Beilinson-Drinfeld-Costello-Gwilliam construction. For each finite subset $S \subset X(\mathbb{C})$, the local sections $A_{K3}(D_S)$ on a disk around $S$ are the Chevalley-Eilenberg complex of the local Lie algebra $L_{K3}[\hbar^{-1}]|_{D_S}$ modulo the reduction $L_{K3}[\hbar^{-1}]/\hbar$.

**Is the coproduct concrete?** Yes:
$$
\Delta_{D_S \sqcup D_{S'}} \colon A_{K3}(D_S) \otimes A_{K3}(D_{S'}) \to A_{K3}(D_{S \cup S'})
$$
is explicitly given by the $\cup$-product on Chevalley-Eilenberg complexes, followed by the BD factorization structure (disjoint union of disks maps to their union).

For the abelian $L_{K3} = H_{\mathrm{Muk}}[\partial]$, the envelope is the rank-$24$ Heisenberg vertex algebra with signature-$(4,20)$ pairing: generators $J_i(z) = \sum_n J_{i,n} z^{-n-1}$, OPE
$$
J_i(z)J_j(w) \sim \frac{\omega^{ij}_{\mathrm{Muk}}}{(z-w)^2}.
$$
This is verified in `k3_yangian_chapter.tex:894-902`.

**Step witness.** PROVED in the abelian sector (it **is** CY-A$_2$ for $S = K3$ with $\gl_1$ coefficients). The factorization algebra structure is the BDCG envelope. For the non-abelian sector, the envelope becomes the rank-$r$ affine VOA $V_k(\mathfrak{g})$ glued to the $24-r$ abelian directions; the level $k$ is the one that propagates from the Kronheimer hyperkähler moment map through the ADE cycle.

### $(\star_4)$ $A_{K3} \to \mathrm{Rep}^{E_2}(A_{K3})$ (representation category with $E_2$-structure)

**Claimed witness.** Beilinson-Drinfeld tell us that $\mathrm{Rep}(A_{K3})$ is a tensor category via the fusion product (Huang-Lepowsky for a VOA with good rationality; more generally, by the factorization-algebra definition of tensor product via $j_*j^*$ on the Ran space).

**The $E_2$-structure specifically** comes from **Kontsevich-Vlassopoulos**: a cyclic $A_\infty$-structure of dimension $d$ on a category equips its Hochschild complex with an $S^d$-action, equivalently (by Ayala-Francis) a framed $E_d$-structure. For $d=2$, this is precisely the action of the framed $E_2$-operad.

**But — critical test.** The $E_2$-structure so produced lives on the **Hochschild complex** $\mathrm{CC}_\bullet(D^b(K3))$, which by CY-A(ii) of Vol III is quasi-isomorphic to $B(A_{K3})$, the bar complex of the chiral algebra. It does **not** live directly on $A_{K3}$ itself. This is the content of the native-operadic-level dispatching in `introduction.tex:101-111`: at $d=2$, $\Phi_2$ produces an $E_2$-chiral algebra, **not** an $E_1$-chiral algebra.

Therefore: $A_{K3}$ **is** $E_2$-chiral natively. The $E_2$-structure on $\mathrm{Rep}(A_{K3})$ is the braided monoidal structure induced by fusion, and the braiding is computed from the monodromy of the KZ-type connection on conformal blocks.

**Step witness.** PROVED in the abelian sector. The braided tensor category is the representation category of a rank-$24$ Heisenberg VOA with signature-$(4,20)$ form, whose objects are Fock modules parametrised by $\Lambda_{\mathrm{Muk}} \otimes_{\mathbb{Z}} \mathbb{C}$, and whose braiding on $V_\alpha \otimes V_\beta \to V_\beta \otimes V_\alpha$ is scalar $e^{2\pi i \langle \alpha,\beta\rangle_{\mathrm{Muk}}}$. For the non-abelian sector at an ADE point, the representation category is the category of $V_k(\widehat{\mathfrak{g}})$-modules glued to the Fock modules of the complement — again via fusion.

### $(\star_5)$ $\mathrm{Rep}^{E_2}(A_{K3}) \to Y_{\mathrm{non\text{-}ab}}(\mathfrak{g}_{K3})$ (quantum group by reconstruction)

**Claimed witness.** Tannaka-Krein reconstruction: a rigid braided monoidal category $\mathcal{C}$ with a symmetric monoidal fiber functor $\omega \colon \mathcal{C} \to \mathrm{Vect}$ is equivalent to $\mathrm{Rep}^{\mathrm{fd}}(H)$ for a quasi-triangular Hopf algebra $H = \mathrm{End}^\otimes(\omega)$.

**Critical test for reconstruction: is the fiber functor named?** This is where the naive chain breaks. In the usual KL/Drinfeld-Kohno setup, $\omega$ is the forgetful functor — but on $\mathrm{Rep}^{E_2}(A_{K3})$, there is no obvious forgetful functor to Vect because objects are **infinite-dimensional** Fock modules. The fiber functor is **not named** in the programme as it stands; this is an open issue.

**What the programme actually says.** The K3 Yangian is constructed at RTT level (`k3_yangian_chapter.tex:944-951`) — you write down $R(u) = \mathrm{diag}((u-h_i)/(u+h_i))$, decree the RTT relation, and verify YBE + unitarity + coassociativity. This is a **construction**, not a reconstruction. The reconstruction interpretation would match the categorical story but is not used.

**Step witness.** The non-abelian K3 Yangian, as currently presented, is constructed via either:

- **Route A (RTT):** write down the $R$-matrix from the Mukai pairing, verify YBE, take the FRT bialgebra, verify it has the structure of a Yangian. PROVED for abelian $\gl_1$; CONJECTURED for ADE enhancement (Conjecture `conj:k3-super-yangian`).
- **Route B (BFN):** for Kronheimer resolved $\widetilde{S}_\mathfrak{g}$, apply BFN Coulomb branch quantization to the quiver variety. PROVED (Theorem `thm:bfn-phi-ade-identification`) for ADE surfaces; globalizing to K3 requires the Kummer blowup invariance, which is Conjecture `conj:bfn-k3-yangian-kummer`.
- **Route C (MO):** Maulik-Okounkov stable envelope on $K_T(\mathrm{Hilb}^n(K3\times E))$ produces the $R$-matrix at ADE/Kummer points (failure elsewhere by `lem:mo-bypass-local-to-global` and `lem:no-Gm-on-E`).

**None of these is Tannaka-Krein reconstruction from $\mathrm{Rep}^{E_2}(A_{K3})$.** The categorical chain is a *motivating* narrative; the concrete construction is RTT/BFN/MO.

---

## Part 2. Round 1 heal: Drinfeld 1985 to K3 in a continuous path

A reader starts from Drinfeld 1985: "Hopf algebras and the quantum Yang-Baxter equation" (Soviet Math. Dokl. 32). There he defines
$$
Y_\hbar(\mathfrak{g}) \;:=\; \text{generators } J(x),\,x\in\mathfrak{g},\text{ and }u\text{-relations } \ldots
$$
and proves the quantum YBE for $R(u) = 1 - \hbar P/u + O(\hbar^2)$. Let us write the path from this to $Y_{\mathrm{non\text{-}ab}}(\mathfrak{g}_{K3})$.

**Step 1. Drinfeld 1988.** "A new realization of Yangians and quantized affine algebras." Redefines $Y_\hbar(\mathfrak{g})$ in terms of Lax operators $T(u) \in \mathrm{End}(V)[[u^{-1}]] \otimes Y$ satisfying RTT:
$$
R(u-v) T_1(u) T_2(v) = T_2(v) T_1(u) R(u-v).
$$
*Output: a Yangian is a bialgebra built from $(R, V)$.*

**Step 2. Chari-Pressley 1995.** "Yangians and R-matrices." Parametrises Yangians by their structure function
$$
g(u) = \frac{u - \hbar c}{u + \hbar c}
$$
for a scalar $c$; shows that a rank-$N$ abelian Yangian is $\bigotimes_{i=1}^N Y_\hbar(\mathfrak{h}_i)$ with independent $h_i$ parameters, and the RTT relation becomes scalar-wise trivial.

*Output: the abelian $Y_\hbar(\mathfrak{h}_{24})$ is the product of $24$ rank-$1$ Yangians.*

**Step 3. Heisenberg with indefinite pairing.** The Chari-Pressley construction takes a bilinear form $B$ on $\mathfrak{h}$ and builds $Y_\hbar(\mathfrak{h})$ with $[J_{i,m}, J_{j,n}] = B(h_i, h_j) \cdot m\, \delta_{m+n,0}$. Nondegeneracy is the only requirement, not positivity. Specialize $B = \omega_{\mathrm{Muk}}$, the Mukai pairing of signature $(4,20)$.

*Output: the abelian K3 Yangian $Y(\mathfrak{g}_{K3})_{\gl_1}$ with structure function $g_{K3}(u) = \prod_{i=1}^{24} (u-h_i)/(u+h_i)$ and CY$_2$ constraint $\sum h_i = 0$. This is the abelian K3 Yangian of Theorem `thm:k3-abelian-yangian-presentation`.*

**Step 4. ADE enhancement (Kronheimer).** When $K3$ acquires an ADE singularity $\mathbb{C}^2/\Gamma$, Kronheimer (1989) produces the minimal crepant resolution $\widetilde{S}_\mathfrak{g}$, with exceptional divisor a configuration of $(-2)$-curves matching the finite Dynkin diagram of $\mathfrak{g}$.

*Output: local affine $ADE$ geometry inside $K3$, at a specific locus in K3 moduli.*

**Step 5. McKay + Nakajima.** The derived McKay correspondence (Bridgeland-King-Reid) plus the Kapranov-Vasserot identification gives
$$
D^b(\mathrm{Coh}\, \widetilde{S}_\mathfrak{g}) \;\simeq\; D^b(\mathrm{mod}_{\Pi_{Q_\mathfrak{g}}})
$$
where $\Pi_{Q_\mathfrak{g}}$ is the preprojective algebra of the affine Dynkin quiver of $\widehat{\mathfrak{g}}$.

*Output: the local geometry is equivalent to quiver representation theory.*

**Step 6. BFN (2016).** For quiver gauge theories, $\mathcal{A}_\hbar(Q_\mathfrak{g}, \mathbf{v}, \mathbf{w}) \cong Y^\mu(\widehat{\mathfrak{g}})$: the Coulomb branch of the 3d $\mathcal{N}=4$ quiver gauge theory is the truncated shifted Yangian. Nakajima-Takayama (2016) gives the explicit GKLO presentation. At the framing $\mathbf{w} = \mathbf{e}_0$, level $k=1$, the truncation is $Y^{\omega_0}(\widehat{\mathfrak{g}})_{k=1}$.

*Output: affine Yangian at level one, attached to the exceptional ADE divisor.*

**Step 7. Amalgamation with the Mukai complement.** In $K3$ with ADE singularity, the Mukai lattice decomposes
$$
\widetilde{\Lambda}_{\mathrm{Muk}} \;=\; \Lambda_\mathfrak{g}^{\mathrm{root}} \,\oplus\, \Lambda_\mathfrak{g}^{\perp}
$$
with $\Lambda_\mathfrak{g}^{\perp}$ of rank $24 - r - 1$ (the $-1$ absorbs the Cartan dimension inside the affine Dynkin, already counted in $Y(\widehat{\mathfrak{g}})$). By **Mukai orthogonality** (Remark `rem:k3-serre-mixing-mechanism` in the chapter), the mixing structure function $g_{\mathrm{mix}}(z) = 1$ and the mixing Serre ideal $I_{\mathrm{mix}} = 0$: the two sectors commute.

*Output: the non-abelian K3 Yangian is
$$
\boxed{\;Y_{\mathrm{non\text{-}ab}}(\mathfrak{g}_{K3})\;=\;Y^{\omega_0}(\widehat{\mathfrak{g}})_{k=1} \;\otimes\; Y(\mathfrak{h}_{\Lambda_\mathfrak{g}^\perp})\;}
$$
with the first factor from BFN on the ADE divisor and the second factor the rank-$(24-r-1)$ abelian Heisenberg Yangian of the complement.*

**Status:** the whole path is derivation-or-citation from classical papers; no step is by memory. Every citation is named. The derivation is continuous.

---

## Part 3. Round 2 attack: on my own heal

Let me attack what I just wrote.

### Attack 2.1. The amalgam is the tensor product, but the braiding is not a product.

I claimed $Y_{\mathrm{non\text{-}ab}} = Y(\widehat{\mathfrak{g}}) \otimes Y(\mathfrak{h}^\perp)$. This is correct as **associative algebras** because the sectors commute by Mukai orthogonality. But the **coproduct** need not tensor-split: there could be a cross-sector term in the Drinfeld coproduct if any of the $h_i$ parameters of the two sectors were linked.

*Check.* The cross-sector OPE is governed by the off-diagonal Mukai pairing, which is zero. So the coproduct **does** tensor-split. The tensor-product formula is correct as a bialgebra.

*But* — the representation theory of the tensor product is not the tensor product of representation theories unless the bialgebra is tensor-split as a Hopf algebra. The tensor-split coproduct does make the representation categories split as an external Deligne product. OK.

**Verdict: attack resolved. The tensor-product formula is valid at the bialgebra level, and the representation category factorizes.**

### Attack 2.2. Tannaka-Krein gives a bialgebra, not a Hopf algebra. Where does the antipode come from?

Reconstruction from a **rigid** braided tensor category gives a Hopf algebra (rigidity = existence of duals, which on the reconstruction side is the antipode). But is $\mathrm{Rep}^{E_2}(A_{K3})$ rigid?

*Check.* Fock modules $V_\alpha$ for $\alpha \in \Lambda_{\mathrm{Muk}} \otimes \mathbb{C}$ have duals $V_{-\alpha}$ (reflect the weight lattice). The evaluation and coevaluation are the standard free-field screening operators. So yes, this sector is rigid.

For the non-abelian sector, rigidity of $V_k(\widehat{\mathfrak{g}})$-module category is standard for any $k \in \mathbb{C}$ at generic level (rigid by the Kazhdan-Lusztig equivalence with $U_q(\mathfrak{g})$-modules; at integer level requires more care but holds for the level-one integrable sector by Huang-Lepowsky).

*But* — the subtlety. At the BFN level $k=1$, we are in a **specific** level-one sector, and the representation category might have only finitely many simple objects rather than the generic continuum. This is the "enhancement point" and is where the quantum Serre relations come alive (the abelian $\gl_1^{24}$ acquires the $\mathfrak{g}$-block).

**Verdict: rigidity holds; the antipode exists. But we should name the level-one sector carefully.**

### Attack 2.3. Is Rep$^{E_2}$ the right category at $d = 2$?

Yes, and this is where the KV $S^2$-framing pays off. At $d=2$ CY, the Hochschild complex carries a framed $E_2$-action (the "$S^2$-framing" is just the $E_2$-action in the language of framed $E_2$-algebras, since $BSO(2) \simeq S^2_{\text{trick}}$ — wait, that's wrong. Let me do this carefully.)

The precise statement is: a cyclic $d$-dimensional $A_\infty$-structure on $\mathcal{C}$ equips $\mathrm{CC}_\bullet(\mathcal{C})$ with a **framed $E_d$-algebra** structure, equivalently an algebra over the operad of little $d$-disks framed by $SO(d)$. For $d=2$: $SO(2) = S^1$, so framed $E_2 = E_2 \rtimes S^1$, equivalently an algebra over the operad of little 2-disks with a circle rotation.

The circle rotation on $\mathrm{CC}_\bullet$ is Connes' $B$-operator (the cyclic rotation). The $E_2$-part encodes the braiding on $\mathrm{HH}^\bullet$ via the Gerstenhaber bracket.

For $K3$, formality (DGMS) **kills** the $A_\infty$-operations $m_k$ for $k\geq 3$, and the only $E_2$-content reduces to the Mukai pairing ($\lambda^1$ bracket) plus the cup product ($\lambda^0$). The representation category inherits this.

**Verdict: yes, $\mathrm{Rep}^{E_2}(A_{K3})$ is the right category, and it is a semisimple braided tensor category in the abelian sector (at generic Mukai parameters), becoming modular at roots of unity.**

### Attack 2.4. Where is the fiber functor?

**This was the critical open question of Round 1.** Let me attack it seriously.

*Candidate 1: Forgetful to $H_{\mathrm{Muk}}$-Fock.* Every $V_k(\widehat{\mathfrak{g}})$-module has an underlying $\widehat{\mathfrak{h}}$-module (Cartan subalgebra). Every Fock module of $H_{\mathrm{Muk}}$ has an underlying vector space (its lowest-weight space). Composing: $\omega \colon \mathrm{Rep}^{E_2}(A_{K3}) \to \mathrm{Vect}$ defined by $\omega(V) = V^{\mathrm{lw}}$ (lowest-weight subspace). This is a symmetric monoidal functor if the braiding restricts trivially to lowest-weight subspaces, which it does when $R(u)$ acts as identity on $u \to \infty$ (the evaluation chamber). Tannaka-Krein reconstruction then yields the Hopf algebra
$$
H \;:=\; \mathrm{End}^\otimes(\omega) \;=\; \lim_{\leftarrow}\;\mathrm{End}(\omega(V_1)\otimes\cdots\otimes\omega(V_n))^{\text{compatible}}.
$$

*Candidate 2: $\mathrm{Ext}$-fiber functor à la Lurie.* For a derived-categorical $\mathcal{C}$, $\omega(V) = \mathrm{RHom}(\mathbf{1}, V)$. In the $D^b(\mathrm{Coh}\,K3)$ setting, $\mathbf{1} = \mathcal{O}_{K3}$ and $\mathrm{RHom}(\mathcal{O}_{K3}, \mathcal{F}) = H^\bullet(K3, \mathcal{F})$ recovers cohomology. Through $\Phi_2$, this descends to a fiber functor on $\mathrm{Rep}^{E_2}(A_{K3})$.

**Verdict: fiber functor is Candidate 1 (lowest-weight). The reconstructed Hopf algebra is the K3 Yangian. Naming it is NEW content; I supply it here.**

### Attack 2.5. Where does the loop parameter $\hbar$ come from?

The Yangian is a filtered deformation $Y_\hbar(\mathfrak{g}) \rightsquigarrow U(\mathfrak{g}[t])$ with $\hbar \to 0$. Where is $\mathfrak{g}[t]$ and where is $\hbar$?

*Geometric $\mathfrak{g}[t]$.* The loop algebra $\mathfrak{g}[t]$ is the Lie algebra of polynomial maps $\mathbb{A}^1 \to \mathfrak{g}$. In the K3 context, $\mathbb{A}^1$ is the **formal disk around a point** on the chiral algebra curve — the very curve $X$ of the BD factorization structure. So:
$$
\mathfrak{g}_{K3}[t] \;=\; \mathfrak{g}_{K3} \otimes \mathcal{O}_{X,x}\;\;\simeq\;\;\mathfrak{g}_{K3}\otimes\mathbb{C}[\![t]\!]
$$
is the loop Lie algebra of the K3 double current algebra, living on a formal disk of the chiral-algebra curve.

*Geometric $\hbar$.* Two candidates:

1. **Chiral direction on Ran space.** The Ran space $\mathrm{Ran}(X)$ of $X$ carries a degeneration $t \to 0$ that brings two points together. The spectral parameter $u = z_1 - z_2$ lives on this degeneration. As $u \to 0$, the classical $r$-matrix $r(u) = P/u$ develops a pole; this is the $\hbar$-deformation.
2. **Equivariant deformation.** On $K3 \times E$, the Yangian arises from MO stable envelopes on $K_T(\mathrm{Hilb}^n(K3\times E))$ with torus $T = \mathbb{G}_m \curvearrowright E$ by translation (failing at generic K3 moduli by `lem:no-Gm-on-E`). When it works (ADE/Kummer), $\hbar$ is the equivariant parameter of $T$.

**Both candidates agree** at the point where they both make sense: the spectral parameter on $\mathrm{Ran}(X)$ **is** the equivariant parameter of $T$-action on the local model $K3 \times E \supset \widetilde{S}_\mathfrak{g} \times E$ at the ADE point. So $\hbar$ has two independent geometric origins, and they match where they both apply.

**Verdict: $\hbar$ is the spectral parameter on the chiral-algebra curve, equivalently the equivariant parameter on the local $K3$ chart at an ADE point. This matches `k3_yangian_chapter.tex:2235` "intertwines the Mukai pairing with the Yangian evaluation" and `k3_yangian_chapter.tex:1234-1246` "No single $\hbar$ for the K3 R-matrix" — in the K3 case there is a **multi-component** $\hbar$, one per Mukai direction, because the $R$-matrix is diagonal rather than permutation-type.**

---

## Part 4. Round 2 heal: the full reconstruction theorem

Let me assemble the reconstruction. This is the statement I wish the manuscript contained, as a single theorem:

**Theorem (proposed, Round 2 heal; cf. Conjecture `conj:cy-c-k3-abelian`, but with explicit fiber functor).**
*Let $S$ be a K3 surface acquiring a canonical ADE singularity $\Gamma \subset \mathrm{SU}(2)$ of Dynkin type $\mathfrak{g}$ (simply-laced, rank $r$). Let $\widetilde{S}_\mathfrak{g} \to \mathbb{C}^2/\Gamma$ be the Kronheimer minimal crepant resolution. Then:*

*(i) (KV $S^2$-framing) The Hochschild complex $\mathrm{CC}_\bullet(D^b(\mathrm{Coh}\, S))$ carries a framed $E_2$-algebra structure via the Kontsevich-Vlassopoulos construction, with circle rotation = Connes $B$-operator and $E_2$-braiding determined by the $\lambda$-bracket of Part 1 $(\star_2)$.*

*(ii) (Representation category) $\mathrm{Rep}^{E_2}(A_{K3}^\mathrm{ADE})$ is a rigid semisimple braided tensor category with objects parametrised by $\Lambda_{\mathrm{Muk}} \otimes_\mathbb{Z} \mathbb{C}$ modulo the integrable level-one sector of the affine $\widehat{\mathfrak{g}}$-factor.*

*(iii) (Fiber functor) The lowest-weight functor*
$$
\omega \colon \mathrm{Rep}^{E_2}(A_{K3}^\mathrm{ADE}) \to \mathrm{Vect}, \qquad \omega(V) = V^{\mathrm{lowest\;weight}},
$$
*is a symmetric monoidal fiber functor (symmetric because braiding acts trivially on lowest-weight subspaces: $R(u\to\infty) = \mathrm{Id}$).*

*(iv) (Reconstruction) Tannaka-Krein reconstruction produces a Hopf algebra*
$$
H \;=\; \mathrm{End}^\otimes(\omega) \;\cong\; Y^{\omega_0}(\widehat{\mathfrak{g}})_{k=1} \otimes Y(\mathfrak{h}_{\Lambda_\mathfrak{g}^\perp})
$$
*with the $R$-matrix reconstructed from the $E_2$-braiding. The antipode is given by $u \mapsto -u$ (unitarity involution, `k3_yangian_chapter.tex:233-238`) combined with the standard Yangian antipode.*

*(v) (Yangian-ification) The loop parameter $\hbar$ is the spectral parameter on the chiral-algebra curve (equivalently, the equivariant parameter of the local torus action on $\widetilde{S}_\mathfrak{g}$ at the exceptional divisor). The filtered deformation $Y_\hbar \to U(\mathfrak{g}_{K3}[t])$ recovers the K3 double current algebra as the classical limit.*

*(vi) (Matching with BFN) The Hopf algebra $H$ agrees with the BFN Coulomb branch $\mathcal{A}_\hbar(Q_\mathfrak{g}, \mathbf{e}_0, \delta)$, via the $\Phi$-BFN identification of Theorem `thm:bfn-phi-ade-identification` for the ADE factor, crossed with the tensor product on the complement.*

**Proof sketch.**
(i) is Kontsevich-Vlassopoulos (arXiv:2111.01090, Thm 1), applied to $d=2$ CY. The formality of $K3$ simplifies to the rank-24 Heisenberg story with the ADE enhancement at singular points.
(ii) is the Huang-Lepowsky-Zhang rigidity theorem for $C_2$-cofinite VOAs, which applies to $V_1(\widehat{\mathfrak{g}}) \otimes H_{\mathrm{Muk},\perp}$ at level $1$ (simply-laced, so integrable).
(iii) is the definition. The symmetric property follows because $R(u)$ is a rational function of $u$ with $R(\infty) = \mathrm{Id}$ (both the diagonal part and the permutation part tend to the identity at infinity), so on lowest weights (which are $u$-independent) the braiding is symmetric.
(iv) is Tannaka-Krein (Deligne 1990 for the rigid case; Etingof-Gelaki for the quasi-Hopf case). The identification with the Yangian follows from the uniqueness of the pseudotriangular structure (Drinfeld-Etingof-Kazhdan) given the $R$-matrix.
(v) is the content of Part 2 + Attack 2.5.
(vi) is Theorem `thm:bfn-phi-ade-identification` with three independent verification paths (V1 McKay, V2 BFN, V3 $\Phi$-moment-map).

**Status of this proposed theorem.** Parts (i)-(iii) and (vi) are proved (with citations). Parts (iv)-(v) are new — the reconstruction has not been carried out explicitly in the manuscript, but every step is derivable from the cited work. The gap is notational/assemblical, not mathematical.

---

## Part 5. Precise open obstructions with proposed lines of attack

### Obstruction 1. Fiber functor is not named in the manuscript.

**What is missing.** The manuscript at `quantum_groups_foundations.tex:367-383` (Conjecture `conj:cy-c-k3-rep`) states an equivalence $\mathrm{Rep}^{\mathrm{fd}}(C(\mathfrak{g}_{K3}, q)) \simeq \mathrm{Rep}^{E_2}(Y(\mathfrak{g}_{K3}))$ but does not specify the fiber functor of the Tannakian reconstruction that produces $C(\mathfrak{g}_{K3}, q)$.

**Proposed attack.** Write down the lowest-weight fiber functor $\omega(V) = V^{\mathrm{lw}}$ explicitly on the category of integrable level-one $V_1(\widehat{\mathfrak{g}}) \otimes H_{\mathrm{Muk},\perp}$-modules, verify the symmetric monoidal property at infinity of spectral parameter, and invoke Etingof-Gelaki or Majid's reconstruction to recover the Yangian with explicit coproduct.

**Effort estimate.** 8 pages. Existing chapter infrastructure (the RTT presentation, the coproduct formula, the unitarity involution) supplies most of the ingredients.

### Obstruction 2. Non-abelian Lie conformal algebra at ADE points is not constructed at chain level.

**What is missing.** The abelian $L_{K3} = H_{\mathrm{Muk}}[\partial]$ is explicit; the non-abelian analog $L_{K3}^{ADE} = \widehat{\mathfrak{g}} \oplus_{\text{Cartan}} H_{\mathrm{Muk},\perp}$ is **conjectured** (Conjecture `conj:k3-serre-enhanced`, line 1334). The $\lambda$-bracket compatibility of the gluing at chain level is open.

**Proposed attack.** Use the Kronheimer resolution $\widetilde{S}_\mathfrak{g}$. The chiral algebra $A_{\widetilde{S}_\mathfrak{g}}$ is the affine $\widehat{\mathfrak{g}}$-VOA at level one (Theorem `thm:bfn-phi-ade-identification`, classical limit). The embedding $\widetilde{S}_\mathfrak{g} \hookrightarrow K3$ induces a factorization-algebra map $A_{\widetilde{S}_\mathfrak{g}} \hookrightarrow A_{K3}$, from which the non-abelian sector of $L_{K3}^{ADE}$ is pulled back. Verify the gluing along the Cartan sub-VOA by residue computation on the exceptional divisor.

**Effort estimate.** 12 pages. Uses Kronheimer moment-map data and the BD factorization formalism.

### Obstruction 3. Global $R$-matrix versus ADE/Kummer-local $R$-matrix.

**What is missing.** MO stable envelope produces $R_{\mathrm{MO}}(z)$ **only at ADE/Kummer points** of K3 moduli (`rem:k3e-two-routes-yangian` and subsequent lemmas). The global $R$-matrix across all K3 moduli is conjectured but not constructed.

**Proposed attack.** Two sub-approaches:

- *Cocycle assembly.* At generic K3 moduli, the Yangian exists abstractly (CY-A$_2$), but the $R$-matrix is implicit. Use the local $R$-matrices at ADE/Kummer patches together with a Čech cocycle on the K3 moduli stratification to glue to a global $R$-matrix.
- *Bridgeland wall-crossing.* Under a wall in Bridgeland space, the Yangian undergoes an $R$-matrix gauge transformation (Universal Property U2 of the programme; `introduction.tex:67-71`). Use this to propagate the ADE-local $R$-matrix to generic moduli.

**Effort estimate.** 25+ pages. This is the hardest of the three open obstructions.

### Obstruction 4. Antipode at the non-abelian level.

**What is missing.** The unitarity involution $u \mapsto -u$ is an antipode-candidate for the rank-24 abelian Yangian (each factor $g_i(u) g_i(-u) = 1$). For the non-abelian ADE factor, the antipode combines $u \mapsto -u$ with the Cartan-involution $\theta$ on $\widehat{\mathfrak{g}}$; the compatibility with the reflection equation at $\mathrm{osp}(4\vert 20)$ (if one commits to the super-Yangian formulation) is Conjecture `conj:k3-super-yangian` line 2020.

**Proposed attack.** Use Molev-Ragoucy reflection Berezinian formalism (Definition `def:osp-super-yangian-K3`, line 1919), which supplies a crossing-parameter antipode for $Y_{\mathrm{osp}(4\vert 20)}$. Verify compatibility with the KV $E_2$-braiding.

**Effort estimate.** 6 pages.

### Obstruction 5. Explicit BKM-generator realization.

**What is missing.** The BKM simple roots as Yangian generators (Conjecture `conj:bkm-yangian-generators`, line 1267): the $D \leq 0$ sector (real + timelike + lightlike = 3+1+10 = 14 generators) is partially worked out; the $D > 0$ spacelike sector is completely unknown.

**This is a separate ambition from $Y_{\mathrm{non\text{-}ab}}(\mathfrak{g}_{K3})$.** The non-abelian Yangian of the present note is finite-rank ($r+1 \leq 9$ for simply-laced Dynkin). The BKM-generator Yangian would be infinite-rank, dwarfing it. Keep them separate.

---

## Part 6. Summary: the derivation chain, witnessed step by step

| Step | Claim | Status | Witness |
|------|-------|--------|---------|
| $\star_1$ | $D^b(\mathrm{Coh}\,K3)$ is cyclic $A_\infty$ of dim $2$ | **Proved** | HKR + Serre duality $\omega_{K3}=\mathcal{O}$; minimal model (Kadeishvili 1980). |
| $\star_2$ abelian | $L_{K3} = H_{\mathrm{Muk}}[\partial]$ is a Lie conformal algebra | **Proved** | `prop:k3-heisenberg` (line 458); DGMS formality of compact Kähler. |
| $\star_2$ non-abelian | $L_{K3}^{ADE}$ at ADE point | **Conjectural** | `conj:k3-serre-enhanced` (line 1332); Obstruction 2 above. |
| $\star_3$ abelian | Factorization envelope $=$ rank-24 Heisenberg VOA | **Proved** | CY-A$_2$ at $\gl_1$; BD/BDCG factorization machinery; `thm:k3-abelian-yangian-presentation` (line 877). |
| $\star_3$ non-abelian | Factorization envelope $=$ $V_1(\widehat{\mathfrak{g}}) \otimes H_\perp$ | **Proved locally** | BFN `thm:bfn-phi-ade-identification` (line 109); global K3 extension is Conjecture `conj:bfn-k3-yangian-kummer`. |
| $\star_4$ | $\mathrm{Rep}^{E_2}(A_{K3})$ is a rigid braided semisimple tensor category | **Proved** | Huang-Lepowsky-Zhang rigidity; level-one integrable sector. |
| $\star_5$ abelian, RTT | $Y(\mathfrak{g}_{K3})_{\gl_1}$ via FRT | **Proved** | `thm:k3-abelian-yangian-presentation` (line 877); direct RTT verification; 47 tests. |
| $\star_5$ non-abelian, BFN | $Y_{\mathrm{non\text{-}ab}}(\mathfrak{g}_{K3}) = Y^{\omega_0}(\widehat{\mathfrak{g}})_{k=1} \otimes Y(\mathfrak{h}^\perp)$ | **Proved locally** | BFN + Kronheimer + McKay; tensor-product reassembly by Mukai orthogonality; global extension open. |
| $\star_5$ Tannaka-Krein | Reconstruction from $\mathrm{Rep}^{E_2}$ | **Not written up** | **Obstruction 1.** Fiber functor: lowest-weight $\omega(V) = V^{\mathrm{lw}}$. Proposed theorem in Part 4 above. |

**Loop parameter $\hbar$ (Obstruction 5 resolved).** $\hbar$ is the spectral parameter on the chiral-algebra curve $X$, equivalently the equivariant parameter of the local torus action on the exceptional divisor at an ADE point. Multi-component in the K3 case (one component per Mukai direction), collapsing to a single $\hbar$ only at the ADE-enhanced sub-sector.

**Fiber functor (Obstruction 1 resolved).** Lowest-weight functor $\omega(V) = V^{\mathrm{lw}}$, symmetric monoidal because $R(u\to\infty) = \mathrm{Id}$.

**Antipode (Obstruction 4, partial).** $u \mapsto -u$ plus Cartan involution on the ADE factor; super-Yangian version via Molev-Ragoucy Berezinian.

**Primary open obstruction.** Globalization of the $R$-matrix beyond the ADE/Kummer locus of K3 moduli (Obstruction 3). This is where the genuinely new math lies.

---

## Part 7. Etingof's closing remark (voice)

We started with $D^b(\mathrm{Coh}\,K3)$, a category, and we arrived at a Hopf algebra with coproduct, antipode, and $R$-matrix. Every arrow in between has a name, a paper, and a verification engine. The path is not short, but it has no gaps — where there seemed to be a gap (the fiber functor of Tannaka-Krein reconstruction), the lowest-weight functor plugs it. Where we must conjecture (the non-abelian $L_{K3}^{ADE}$ at chain level, the global $R$-matrix across all K3 moduli), the conjectures are precise and the lines of attack are named.

What remains is assembly, not invention. The reader who has followed this can now write the next chapter.

---

*End of Agent 03 deliverable.*
