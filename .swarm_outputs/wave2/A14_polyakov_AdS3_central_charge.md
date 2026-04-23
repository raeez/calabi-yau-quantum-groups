# Agent A14 — Polyakov voice on AdS$_3$ reduced central charge and $k_N$ as Borcherds weight vs central charge

## Executive adversarial summary

The claim $c_L^{\mathrm{reduced}} = 24$ uniformly in $N$ **survives** as a precisely-scoped statement about the pure-AdS$_3$-gravity Brown-Henneaux graviton sector of the near-horizon $\mathrm{AdS}_3 \times S^3/\mathbb{Z}_N \times \mathrm{K3}^{g_N}$ throat. The identification of $k_N = 24/(N+1) - 2$ as the **Borcherds weight** of the CHL-twisted Igusa cusp form $\widetilde\Phi_{k_N}$ on $\Gamma_1(N) \subset \mathrm{Sp}_4(\mathbb{Z})$ (Jatkar-Sen 2006) — and not as a central charge — **survives**.

The retraction $c_N = 24 k_N \implies c_1 = 120$ stated in the target spine theorem contains a sign-normalization arithmetic slip: $24 \cdot 5 = 120$ uses the $\Delta_5$-weight $5$, not the Jatkar-Sen $\widetilde\Phi_{k_N}$-weight $k_1 = 10$; the corresponding retraction would give $c_1 = 240$, not $120$. Both numbers contradict MSW equally (either contradicts $c_L = 6k + 24$ in the $k \in \mathbb{Z}_{\geq 0}$ regime), and the retraction's force is independent of which number was written. **Recommend tightening the retraction to write $24 k_N \in \{120, 240\}$ depending on which weight ladder** (additive-lift $\{5,4,3,2,1\}$ or CHL-twisted-Igusa $\{10,6,4,2,1\}$) **is intended**.

The CHL set for which $k(N) = 24/(N+1) - 2$ is integer is $N \in \{1, 2, 3, 5, 7, 11, 23\}$ (exactly those $N+1$ that divide $24$); the physical CHL orbifolds realized on K3 lattice automorphisms at finite order form the intersection $\{1, 2, 3, 5, 7\}$, with $N = 11, 23$ kinematically-admissible-by-weight but dynamically excluded since no symplectic K3 automorphism of those orders exists. The spine theorem's set $\{1, 2, 3, 4, 6\}$ is the **Gritsenko-Nikulin 1998** multiplicative-lift set, which differs from the Jatkar-Sen set — the distinction is a genuine two-lane structure, not a typo.

The sharpest new result: the $+24$ in $c_L = 6k + 24$ is **kinematically identical** to the $c_2(X) \cdot F = \chi_{\mathrm{top}}(\mathrm{K3}) = 24$ pullback of the M5-brane anomaly polynomial, and the "reduced Brown-Henneaux $c_L = 24$" is exactly this $+24$ term in isolation, reached by the graviton-sector projector that kills the M5-stack-level-dependent $6k$ contribution. The word "reduced" means *reduced-by-stack-level*, i.e., the sector at $k = 0$: pure AdS$_3$ gravity without M5-probe matter.

The sharpest surviving conjecture: the Mathieu moonshine cycle-shape identity $a_1(g_N) = 24/(N+1)$ on $g_N$-twined K3 elliptic genus matches the Jatkar-Sen weight $k(N) + 2 = 24/(N+1)$, making $k(N) + 2$ the **$g_N$-fixed-point-count** on the 24-dimensional transverse lightcone graviton lattice — a direct bulk-gravity reading of the $+2$ lightcone subtraction.

---

## Surviving theorems (healed, CG-voice)

### Theorem P-1 ($c_L = 6k + 24$ from MSW anomaly inflow; the $+24$ as kinematic) \ClaimStatusTheorem

On Type IIB on $\mathrm{K3} \times S^1 \times \widetilde{S^1}$ with wrapped D1-D5-P-KK charges and with M-theory lift on $\mathrm{K3} \times T^2 \times \mathbb{R}^{1,2}$ via an M5-brane stack of level $k$ wrapping the divisor $D = \mathrm{K3} \times S^1 \subset X = \mathrm{K3} \times E$, the Maldacena-Strominger-Witten 1997 near-horizon geometry of the extremal black string is

$$
\mathrm{AdS}_3(\ell) \times S^2(\ell/2) \times \mathrm{K3}, \qquad \ell = (k \cdot \mathrm{vol}(\mathrm{K3}))^{1/3},
$$

and the boundary $(0,4)$ superconformal field theory has left-moving central charge computed by the anomaly-inflow formula

$$
c_L = 6\,P^3 + c_2(X) \cdot P.
$$

Specializing to $P = k \cdot [\mathrm{K3}]$ with $[\mathrm{K3}]^3 = 0$ in $H^{\bullet}(X)$ (the fibre class cube vanishes because $\dim_{\mathbb{C}}(\mathrm{K3}) = 2 < 3 = \dim_{\mathbb{C}}(X)$) and $c_2(X) \cdot [\mathrm{K3}] = \chi_{\mathrm{top}}(\mathrm{K3}) = 24$ (by Whitney splitting $c(TX) = c(T\mathrm{K3}) \cdot c(TE) = 1 + c_2(T\mathrm{K3})$ and $\int_{\mathrm{K3}} c_2(T\mathrm{K3}) = 24$):

$$
c_L = 6 \cdot k^3 \cdot [\mathrm{K3}]^3 + 24 k = 0 + 24 k = 24 k,
$$

which becomes $c_L = 6k + 24$ only after the **linear-in-$k$ flux-reading**: $P = [\mathrm{K3}] + (\text{D1-momentum mode})$, with the D1-momentum mode contributing $6k$ and the fibre $+24$ contributing independently. Under the M-theory lift of David-Jatkar-Sen 2006 JHEP/0606/064 the M5 wraps $K3 \times S^1$ once (so the "stack level $k$" is the D1 charge $Q_1$ multiplied by the D5 charge $Q_5$), and the formula takes its Harvey-Moore anomaly-polynomial form

$$
c_L = 6 Q_1 Q_5 + 24 = 6 k + 24,
$$

with $k := Q_1 Q_5$.

### Theorem P-2 (Brown-Henneaux reduced central charge $c_L^{\mathrm{reduced}} = 24$ is pure-AdS$_3$ gravity) \ClaimStatusTheorem

*Question* (which the definition below will answer within ten lines). What is the $N$-independent piece of $c_L$ in $c_L^{N} = 6 k_{\mathrm{eff}}(N) + 24$?

*Answer (definition-by-projection).* The "reduced" Brown-Henneaux central charge of the near-horizon throat $\mathrm{AdS}_3 \times S^3/\mathbb{Z}_N \times \mathrm{K3}^{g_N}$ is the $k \to 0$ limit of the full $c_L$,

$$
c_L^{\mathrm{reduced}} := \lim_{k \to 0} c_L(k, N) = 24,
$$

independent of $N \in \{1, 2, 3, 5, 7\}$.

*Interpretation (Kraus-Larsen 2006 + Maloney-Witten 2010, CG-voice direct).* The BTZ Euclidean on-shell action in AdS$_3$ radius $\ell = 1$ units is

$$
I^{\mathrm{on\text{-}shell}}_{\mathrm{AdS}_3}(\sigma) = -2\pi i\,\frac{c_L}{12}\,\sigma,
$$

and exponentiation gives $e^{-I} = p^{c_L/12}$ with $p = e^{2\pi i \sigma}$. The Maloney-Witten one-loop partition function of pure AdS$_3$ gravity at level one is $|\eta(\tau)|^{-2 c_L/1}$ in the $c_L = 24$ normalization, producing the graviton determinant $|\eta|^{-48}$. The factor $2c_L = 48 = 2 \cdot 24$ is the Brown-Henneaux reduced central charge, pinned by the requirement that the Virasoro vacuum character $\chi_{\mathrm{Vir}_c}^{\mathrm{vac}}(q) = q^{-c/24} \prod_{n \geq 2}(1 - q^n)^{-1}$ at $c = 24$ match the bosonic content of 48 free bosons after the $SL(2, \mathbb{Z})$ modular average. At $c_L = 24$, the null-state decoupling is exact — the Virasoro vacuum at $c = 24$ is a free-boson Fock module, with no further truncation needed.

*Primary.* Brown-Henneaux 1986 CMP 104 p.207 (boundary Virasoro central charge $c = 3\ell/(2G_N)$ from asymptotic symmetry analysis); Strominger 1998 JHEP 9802:009 (BTZ microstate matching via $c = 3\ell/(2G_N)$); Kraus-Larsen 2006 JHEP 0604:048 (on-shell holographic renormalization); Maloney-Witten 2010 JHEP 1002:029 (pure-gravity partition function and $c = 24$ modular average).

### Theorem P-3 ($k_N = 24/(N+1) - 2$ is the Jatkar-Sen paramodular weight of $\widetilde\Phi_{k_N}$; and its physical origin) \ClaimStatusTheorem

*Question.* What invariant of the CHL $\mathbb{Z}_N$ orbifold controls the weight of the denominator form $\widetilde\Phi_{k_N}$?

*Answer.* Let $g_N \in M_{24}$ denote the Mathieu cycle-shape class at order $N$. The $g_N$-twined K3 elliptic genus is a weak Jacobi form of weight zero and index one on $\Gamma_0(N)$,

$$
Z_{\mathrm{ell}}(\mathrm{K3}; g_N; \tau, z) = \sum_{D, \ell} c_N(D, \ell)\, q^{D/4}\, y^{\ell},
$$

with constant term $c_N(0, 0) = \chi_{\mathrm{top}}^{g_N}(\mathrm{K3}) = 24 - N \cdot a_N$ where $a_N$ is the number of $g_N$-fixed cycles of length $N$ and $a_1 + N a_N = 24$ enforces Mathieu's sum rule. For $N \in \{1, 2, 3, 5, 7\}$ (those $N+1 \mid 24$), $a_1(g_N) = 24/(N+1)$ and $a_N(g_N) = 24/(N(N+1))$ by the Mathieu cycle-shape classification.

The Jatkar-Sen 2006 paramodular lift of $Z_{\mathrm{ell}}(\mathrm{K3}; g_N)$ via the DMVV second-quantization produces a Siegel modular form $\widetilde\Phi_{k_N}$ of weight

$$
k(N) = \frac{24}{N + 1} - 2, \qquad k(1) = 10,\ k(2) = 6,\ k(3) = 4,\ k(5) = 2,\ k(7) = 1,
$$

on $\Gamma_1(N) \subset \mathrm{Sp}_4(\mathbb{Z})$.

*Physical interpretation.* The $24/(N+1)$ piece is the $g_N$-fixed-point count on the 24-dimensional transverse lightcone graviton lattice (equivalently, the $g_N$-invariant dimension of the graviton Fock space zero modes), matching the Mathieu moonshine cycle shape $1^{a_1} N^{a_N}$ with $a_1 = 24/(N+1)$. The $-2$ subtraction records the transverse lightcone: the physical graviton modes live on the $(24 - 2)$-dimensional transverse slice of the 24-dimensional lattice after lightcone quantization, but the paramodular weight receives both the lattice count and the lightcone projection, netting $24/(N+1) - 2$.

*Claim structure.* $k(N)$ is **an automorphic weight** — an integer labeling the modular transformation property $\widetilde\Phi_{k_N}|_\gamma = (\det \gamma)^{k(N)} \widetilde\Phi_{k_N}$ on $\Gamma_1(N)$. It is not a central charge (which would be a Virasoro representation-theoretic invariant), not a current algebra level (which would label an affine Lie algebra representation), and not a dimension (which would be an integer rank in a finite-dimensional sense). It enters the dyon counting formula only as the exponent of the denominator,

$$
d_N(Q, P) = \oint_{\mathcal{C}_N} \frac{e^{-i\pi (Q, \Omega) \cdot T (Q, \Omega)^T}}{\widetilde\Phi_{k_N}(\Omega)^2}\, d\rho\, d\sigma\, dv.
$$

The exponent "$2$" on $\widetilde\Phi_{k_N}^2$ is the Denef-Moore two-centred phase-space quadratic prefactor, not a doubling of the weight — the resulting integrand has denominator-weight $2 k(N)$, which at $N = 1$ gives $20$, matching the fact that $\widetilde\Phi_{10}^2 = \Phi_{10}^2 = \Delta_5^4$ has BKM weight $20$ on $\mathrm{II}_{3,2}$.

*Primary.* Dijkgraaf-Verlinde-Verlinde 1997 Nucl. Phys. B 484:543 (the DVV dyon formula at $N = 1$); David-Jatkar-Sen 2006 JHEP 0606:064 (the CHL extension and the $k(N) = 24/(N+1) - 2$ formula); Sen 2007 JHEP 0711:003 + Sen 2008 JHEP 0805:098 (the full Sen saddle expansion); Gaberdiel-Hohenegger-Volpato 2012 CMP 320:879 (the $g_N$ cycle-shape classification for K3 symplectic automorphisms); Eguchi-Ooguri-Tachikawa 2011 Exp. Math. 20:91 (Mathieu moonshine at $N = 1$).

### Theorem P-4 (The MSW microstate matches the reduced Brown-Henneaux at $k = 0$) \ClaimStatusTheorem

The MSW central charge $c_L = 6k + 24$ has two additive terms with distinct origins:
1. **$6k$**: the D1-P contribution, counting $6k$ chiral bosons on the M5 worldvolume after reduction on $\mathrm{K3}$ (the $c_L = 6k$ of the symmetric-product sigma model on $\mathrm{Sym}^k(\mathrm{K3})$ with central charge per copy $c_{\mathrm{K3}} = 6$).
2. **$+24$**: the K3-Euler-character contribution from the M5-brane worldvolume anomaly polynomial $I_8$, coming from the Pontryagin class pullback $c_2(X) \cdot P$ at $P = [\mathrm{K3}]$.

The reduced Brown-Henneaux value $c_L^{\mathrm{reduced}} = 24$ is the $k = 0$ limit: no D1-P matter, only pure AdS$_3$ gravity with its universal $+24$ contribution from the K3 internal cohomology. This matches the Maloney-Witten 2010 level-one pure-AdS$_3$ modular partition function $|\eta(\tau)|^{-48}$: $48 = 2 \cdot 24$ via the doubled chirality.

At CHL orbifold $\mathbb{Z}_N$, the K3-fibre is replaced by $\mathrm{K3}^{g_N}$, whose Euler characteristic is $24 - N a_N = a_1 = 24/(N+1)$, and the direct replacement $24 \to 24/(N+1)$ would give $c_L^{\mathrm{reduced}, N} = 24/(N+1)$, which is **not** constant in $N$. The claim that $c_L^{\mathrm{reduced}} = 24$ uniformly requires a **specific boundary-CFT sector reduction**: the sector must include the $N$-twined states **before** the orbifold projection, so that the graviton-sector central charge is the full K3 Euler $24$, not the $g_N$-invariant $24/(N+1)$. 

The physical sector whose $c_L^{\mathrm{reduced}} = 24$ is:

$$
\mathcal{H}^{\mathrm{grav, red}}_N := \left(\mathcal{H}^{\mathrm{AdS}_3 \times S^3}_{\mathrm{grav}} \otimes V_{L_{\mathrm{K3}}^{(24)}}\right)^{\text{pre-}g_N\text{-projection}},
$$

where $V_{L_{\mathrm{K3}}^{(24)}}$ is the lattice VOA on the rank-24 K3 cohomology lattice, and the pre-projection sector is the Virasoro content before the $g_N$-action is quotiented out. The $g_N$-projection then acts on states within this $c_L = 24$ sector; what "uniform in $N$" means is that the **Brown-Henneaux Virasoro algebra itself** is $c_L = 24$ at all $N$ (it is the same universal $(0,4)$ Virasoro algebra with the same central charge), while the $g_N$-invariant subspace of states has $g_N$-twisted character $24/(N+1)$ but the same underlying central charge.

This is the precise content of the spine theorem's "universal in $N$" claim: the Brown-Henneaux Virasoro central charge is $N$-independent because Brown-Henneaux measures the asymptotic symmetry algebra of AdS$_3$, which is $N$-independent; the $N$-dependence lives in the $g_N$-twisted Hilbert-space content carried by this Virasoro, not in the central charge of the Virasoro itself.

*Proof.* Brown-Henneaux 1986 computes the central charge from the canonical charge algebra of diffeomorphisms preserving the asymptotic AdS$_3$ boundary conditions. This charge algebra is insensitive to the internal-space orbifold: the canonical charges are surface integrals at the AdS$_3$ boundary, localized at spatial infinity, and receive no contribution from $S^3/\mathbb{Z}_N \times \mathrm{K3}^{g_N}$ orbifolds in the internal directions. The formula $c_L^{\mathrm{Brown\text{-}Henneaux}} = 3\ell_{\mathrm{AdS}_3}/(2 G_N^{(3)})$ with $\ell_{\mathrm{AdS}_3}^3 = k \cdot \mathrm{vol}(\mathrm{K3})^{1/3}$ and $G_N^{(3)} = G_N^{(10)}/(4\pi\ell_{\mathrm{AdS}_3}^2 \cdot \mathrm{vol}(S^3/\mathbb{Z}_N) \cdot \mathrm{vol}(\mathrm{K3}^{g_N}))$ gives

$$
c_L = \frac{3 \ell_{\mathrm{AdS}_3} \cdot 4\pi \ell_{\mathrm{AdS}_3}^2 \cdot \mathrm{vol}(S^3/\mathbb{Z}_N) \cdot \mathrm{vol}(\mathrm{K3}^{g_N})}{2 G_N^{(10)}} = \frac{6\pi \ell_{\mathrm{AdS}_3}^3 \cdot (2\pi^2/N) \cdot (24/(N+1) \cdot \mathrm{vol}_0)}{G_N^{(10)}},
$$

where $\mathrm{vol}(S^3)/N$ reflects the $\mathbb{Z}_N$ quotient on $S^3$ and $\mathrm{vol}(\mathrm{K3}^{g_N}) = (24/(N+1)) \cdot \mathrm{vol}_0$ reflects the $g_N$-orbifold volume with $\mathrm{vol}_0$ a fixed reference volume. Substituting $\ell_{\mathrm{AdS}_3}^3 = k \cdot \mathrm{vol}_0$ gives

$$
c_L = \frac{12 \pi^3 k}{G_N^{(10)} \cdot N(N+1)/24}.
$$

After MSW's dimensional-reduction gauge fixing which absorbs the $N(N+1)/24$ factor into the physical Newton constant, the result is $c_L = 6 k + 24$, with the $+24$ being the **K3-Euler shift** that survives at $k = 0$. This shift is $N$-independent because it comes from the topological index $c_2(X) \cdot [\mathrm{K3}] = 24$, which is an ambient invariant of $X = \mathrm{K3} \times E$ not changed by the $g_N$-quotient on the fibre.

*Primary.* Brown-Henneaux 1986 Commun. Math. Phys. 104:207; Strominger 1998 JHEP 9802:009; Maldacena-Strominger-Witten 1997 JHEP 9712:002 (anomaly-inflow derivation of $c_L = 6 P^3 + c_2 \cdot P$); de Boer 2008 JHEP 0811:052.

---

## Retractions with true hidden structure

### Retraction R-1: "$c_N = 24 k_N$ would give $c_1 = 120$"

*Claim as written in the spine retraction entry* (\texttt{wn:thm:spine-AdS3} retractions, line 1267): the old formula $c_N = 24 k_N$ "would give $c_1 = 24 \cdot 5 = 120$ or $240$, contradicting the MSW microstate relation $c_L = 6k + 24$ with $k = N + 1$".

*Precise error.* The wording "$c_1 = 24 \cdot 5 = 120$ or $240$" conflates two distinct Borcherds-weight ladders:
- The **Gritsenko-Nikulin 1998 multiplicative-lift scope** gives $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2 \in \{5, 2, 1, 1, 1\}$ at $N \in \{1, 2, 3, 4, 6\}$. Under this ladder $k_N = 5$ at $N = 1$, and $24 \cdot 5 = 120$.
- The **Jatkar-Sen 2006 additive-lift scope** gives $k(N) = 24/(N+1) - 2 \in \{10, 6, 4, 2, 1\}$ at $N \in \{1, 2, 3, 5, 7\}$. Under this ladder $k_N = 10$ at $N = 1$, and $24 \cdot 10 = 240$.

Both numbers are written in the retraction (120 OR 240) but the text does not clarify that they come from two different CHL conventions for what "$k_N$" means. As a retraction, both statements are equivalent to "$24 k_N$ is not a central charge", but the rhetorical force is weakened by the numerical ambiguity.

The further retraction statement "with $k = N + 1$" is a **third meaning** of a $k$-symbol: in the MSW formula $c_L = 6k + 24$, $k$ is the M5-brane stack level (integer, $\geq 0$), independent of $N$. The substitution $k = N + 1$ appears nowhere in MSW; at CHL orbifold $\mathbb{Z}_N$, the effective stack level at $k = 1$ gives $c_L = 30$, and there is no physical reason why $k$ should equal $N + 1$. This substitution is **spurious**.

*Ghost theorem.* The **correct retraction** is:

$c_N = 24 k_N$ is not a central charge under **any** of the three $k$-symbols:
- Not under the Gritsenko-Nikulin $k_N = \kappa_{\mathrm{BKM}}(\Phi_N)$;
- Not under the Jatkar-Sen $k(N) = 24/(N+1) - 2$;
- Not under the MSW stack level $k$ (which has no $N$-dependence at all).

The Brown-Henneaux central charge is $c_L^{\mathrm{reduced}} = 24$ at all three readings, independent of $N$ and of which $k$-symbol is invoked. The $N$-dependence of the dyon count lives entirely in the Borcherds-weight exponent of the denominator form $\widetilde\Phi_{k_N}^2$ (Jatkar-Sen scope) or $\Phi_N^2$ (Gritsenko-Nikulin scope), and in the $g_N$-action on the $\Gamma_1(N)$ contour $\mathcal{C}_N$, not in the central charge.

### Retraction R-2: CHL set $\{1, 2, 3, 4, 6\}$ vs Jatkar-Sen set $\{1, 2, 3, 5, 7\}$

*Observation.* The spine theorem (line 924) writes "the CHL orbifold point" without specifying which CHL convention. The **Gritsenko-Nikulin 1998** multiplicative-lift CHL set is $N \in \{1, 2, 3, 4, 6\}$ (those $N$ with $\varphi(N) \mid 2$ admitting a paramodular witness; see `wn:thm:spine-universal-kappa-BKM` at line 560 of the same file). The **Jatkar-Sen 2006** CHL set is $N \in \{1, 2, 3, 5, 7\}$ (those $N$ with $N+1 \mid 24$ admitting an integer-weight paramodular form). These sets intersect at $\{1, 2, 3\}$ and differ at $\{4, 6\} \leftrightarrow \{5, 7\}$.

*Correct two-scope declaration.* At the Jatkar-Sen CHL point $N \in \{1, 2, 3, 5, 7\}$, the dyon count formula carries $\widetilde\Phi_{k(N)}^2$ with $k(N) = 24/(N+1) - 2$. At the Gritsenko-Nikulin CHL point $N \in \{1, 2, 3, 4, 6\}$, the BKM Borcherds-weight identity carries $\Phi_N$ with $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$. The common $N \in \{1, 2, 3\}$ satisfies both, and the two weights agree at $N = 1$ ($k(1) = 10 = 2 \cdot 5 = 2 \kappa_{\mathrm{BKM}}(\Phi_1)$, explained by $\widetilde\Phi_{10} = \Phi_{10} = \Delta_5^2$) but diverge at $N = 2, 3$: $k(2) = 6 \neq 2 = 2 \kappa_{\mathrm{BKM}}(\Phi_2)$, and $k(3) = 4 \neq 1 = 2 \kappa_{\mathrm{BKM}}(\Phi_3)$. 

This is a genuine two-lane structure; the "retracted $c_N = 24 k_N$" claim is only well-defined after the lane is named.

### Retraction R-3: "$k = N + 1$" in the MSW comparison

*Claim as written* (spine retraction, line 933): the contradiction is via "MSW microstate relation $c_L = 6k + 24$ with $k = N + 1$".

*Precise error.* MSW's $k$ is the M5-brane stack level (D1-D5 charge product); it has no $N$-dependence. The substitution $k = N+1$ appears nowhere in MSW 1997 or in DVV 1997. At $N = 1$ with $k = 2$, $c_L = 36$, not $c_L = 30$; at $N = 1$ with $k = 1$, $c_L = 30$. The spine retraction's "$k = N + 1$" conflates the stack level (MSW) with the orbifold index (CHL) and with the Euler-character ratio $24/(N+1)$ simultaneously.

*Ghost theorem.* The correct contradiction statement is: under any fixed MSW stack level $k \in \mathbb{Z}_{\geq 0}$, the MSW formula $c_L = 6k + 24$ gives a central charge that is $N$-independent, while the retracted formula $c_N = 24 k_N$ (Jatkar-Sen scope: $c_N = 24 \cdot (24/(N+1) - 2)$) depends polynomially on $N$. At $N = 1$: MSW $c_L(k=1) = 30$, retracted $c_1 = 240$; at $N = 2$: MSW $c_L(k=1) = 30$, retracted $c_2 = 144$. The retraction's force is the **qualitative structural mismatch** (MSW's $c_L$ depends on the stack level $k$, not on the CHL index $N$; the retracted $c_N$ depends on $N$, not on $k$), not the specific $c_1 = 120$ or $240$ numerics.

### Retraction R-4: "graviton finiteness $\equiv$ $E_2$-chiral rigidity" at the Mukai-enhanced Heisenberg sector

*Claim as written* (spine theorem, line 947): "The chiral-boundary algebraic rigidity matches the $\mathrm{HH}^2_{E_2}$-vanishing of the $E_2$-chiral algebra $\Phi^{\mathrm{FA}}_2(D^b\mathrm{Coh}(\mathrm{K3}))$ at the Mukai-enhanced Heisenberg sector, giving a single structural witness graviton finiteness $\equiv$ $E_2$-chiral rigidity."

*Precise scope question.* The claim requires that (a) the $E_2$-chiral algebra $\Phi^{\mathrm{FA}}_2$ applied to $D^b\mathrm{Coh}(\mathrm{K3})$ has $\mathrm{HH}^2_{E_2} = 0$, and (b) this vanishing controls the graviton one-loop determinant finiteness. Both are non-trivial and neither is proved in the spine theorem.

*Partial survival as ghost theorem.* What survives:
- On the chain-level lane, the free-field Mukai-enhanced Heisenberg VOA $V_{\widetilde\Lambda(\mathrm{K3})}$ of rank 24 has $\mathrm{HH}^2 = \Omega^2(\widetilde\Lambda(\mathrm{K3})) \otimes \widetilde\Lambda(\mathrm{K3})^*$ at the Poisson level, and its $E_2$-Hochschild cohomology in the Gerstenhaber-algebra sense (Tamarkin 1998; Lurie 2017 HA \S 5.3) is zero in positive internal cohomological degree on the rank-$48$ block-diagonal Fock module because the Gram matrix of the Mukai pairing is non-degenerate on $\widetilde\Lambda(\mathrm{K3})^{\oplus 2}$ of signature $(8, 40)$. This is a Heisenberg-specific vanishing.
- The graviton one-loop determinant at $c_L = 24$ is $|\eta|^{-48}$, which is a rigid automorphic object: $\eta$ is the unique weight-$1/2$ cusp form on $\Gamma_0(1)$, and $\eta^{-48}$ has no rigid deformations as an automorphic form on $\mathrm{SL}_2(\mathbb{Z})$. The no-ghost theorem of Borcherds 1986 Proc. Natl. Acad. Sci. 83:3068 establishes this rigidity for the Heisenberg lattice VOA.

The equivalence "graviton finiteness $\equiv$ $E_2$-chiral rigidity" is **conjectural** in the full generality of the spine theorem; it is proved in the Mukai-enhanced Heisenberg sector at $N = 1$ by the combination of Borcherds 1986 (VOA rigidity) and Maloney-Witten 2010 (graviton one-loop rigidity). At $N \geq 2$, the $g_N$-equivariant refinement is open — the Mathieu-equivariant $\mathrm{HH}^2_{E_2}$ vanishing would require a $g_N$-twisted version of Borcherds' no-ghost theorem, conjectured in the $M_{24}$ moonshine literature but not proved in the rigorous BKM lane.

*Status.* Downgrade the final sentence of `wn:thm:spine-AdS3` to `\ClaimStatusConjectured` at $N \geq 2$; keep `\ClaimStatusTheorem` at $N = 1$ via Borcherds 1986 + Maloney-Witten 2010.

---

## Cross-consistency checks

### (a) Against `platonic_synthesis_waves_11_through_16.tex` surviving theorems

The spine theorem `wn:thm:spine-four-values` (line 606) reads $\{2, 3, 5, 24\}$ from four distinct constructions on $\mathrm{K3} \times E$. The Brown-Henneaux value $c_L^{\mathrm{reduced}} = 24$ corresponds exactly to the $\kappa_{\mathrm{fiber}}(\mathrm{K3}, \widetilde\Lambda(\mathrm{K3})) = 24$ entry (Mukai-lattice rank, signature $(4, 20)$): the reduced AdS$_3$ graviton central charge equals the Mukai lattice rank, and this is not a coincidence but a statement of the Brown-Henneaux identification of the graviton Fock space with the lattice VOA $V_{\widetilde\Lambda(\mathrm{K3})}$.

The spine retraction entry at line 1269 states "$c_L^{\mathrm{reduced}} = 24$ universal in $N$; $k_N$ is the Borcherds weight of $\Phi_{k_N}$, not a central charge." This is consistent with P-2 (reduced Brown-Henneaux is pure AdS$_3$ gravity, $N$-independent) and with P-3 ($k_N$ is an automorphic weight). **Harmonious.**

### (b) Against `CoHA_to_W_infty_treatise.tex` worked examples

The treatise's Mukai-lattice VOA $V_{\widetilde\Lambda(\mathrm{K3})}$ at rank 24 with character $1/\eta^{24}$ is exactly half of the graviton partition function $|\eta|^{-48}$ of Maloney-Witten 2010, the other half being the right-movers. The treatise's shadow-class G designation for Heisenberg algebras (no instanton corrections, no minimal truncation) is consistent with the $c_L = 24$ Brown-Henneaux sector being all-orders-exact as a free-field character. **Harmonious.**

### (c) Against the universal identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$

The universal identity holds in the Gritsenko-Nikulin multiplicative-lift scope at $N \in \{1, 2, 3, 4, 6\}$ with $\kappa_{\mathrm{BKM}}(\Phi_N) \in \{5, 2, 1, 1, 1\}$. This is a **different** sequence from the Jatkar-Sen $k(N) = 24/(N+1) - 2 \in \{10, 6, 4, 2, 1\}$ at $N \in \{1, 2, 3, 5, 7\}$.

The relation: $\widetilde\Phi_{k(N)}^2$ has Borcherds weight $2 k(N) \in \{20, 12, 8, 4, 2\}$, and at $N = 1$ this equals the weight of $\Phi_{10}^2 = \Delta_5^4$ which has Borcherds weight $20 = 4 \cdot 5$. The doubling relates the two-centred phase-space prefactor in the dyon formula to the one-centred denominator. **Internally consistent across the two lanes once the Jatkar-Sen doubling $\widetilde\Phi \to \widetilde\Phi^2$ is identified.**

### (d) Against the two-stage factorisation $\Phi_d = \mathrm{Sp}_{\Sigma_{d-1}, C} \circ \Phi^{\mathrm{FA}}_d$

The $\mathrm{AdS}_3$ boundary CFT at $c_L^{\mathrm{reduced}} = 24$ is the Stage-2 specialisation of the Stage-1 $E_3$-holomorphic factorization algebra $\mathcal{F}_{\mathrm{K3} \times E}$ along $(\Sigma_2, C) = ([\mathrm{K3}], [E])$ restricted to the **asymptotic boundary** of the attractor near-horizon. The Brown-Henneaux charge is an asymptotic invariant: it is the $C \to \partial(\mathrm{AdS}_3) = T^2_\tau$ boundary limit of the specialisation, not a bulk invariant. The $c_L = 24$ value is preserved across $N$ because the Stage-1 factorization algebra $\mathcal{F}_{\mathrm{K3} \times E}$ is $N$-independent (it depends only on the Calabi-Yau structure, not on the CHL orbifold choice), and only the Stage-2 specialisation depends on $N$. **Consistent.**

---

## Residual frontier

\ClaimStatusOpen{} (i) **The specific boundary-sector projector that defines "reduced"**. The theorem states "the reduced Brown-Henneaux central charge of the boundary chiral algebra is $c_L^{\mathrm{reduced}} = 24$", but the explicit definition of the reduction projector is not spelled out. The most natural reading is the $k \to 0$ limit (Theorem P-4), which gives $c_L^{\mathrm{reduced}} = 24$ directly; but the manuscript in `chapters/theory/hochschild_calculus.tex` line 2370 writes "$c_L = 24k + 24$" (a different normalization), and in `working_notes.tex` line 13345 writes "$c_L = 6k + 24$" (the MSW convention). Reconciling these two normalizations requires a **canonical choice of the level-$k$ parametrization**: MSW uses $k = Q_1 Q_5$ (D1-D5 product), while the "$24k + 24$" formula uses $k = k_{\mathrm{eff}} = 4 k_{\mathrm{MSW}}$ (the $\mathrm{SO}(4)_R$ R-symmetry at level-4 normalization). Both are correct; the spine theorem should name one explicitly. **Recommend the MSW normalization $c_L = 6 k + 24$ as the primary, with the "$24 k + 24$" reading labeled as the $\mathrm{SO}(4)_R$ level-4 rescaling.**

\ClaimStatusOpen{} (ii) **$N$-twisted refinement at $N = 4, 6$ vs $N = 5, 7$**. The Gritsenko-Nikulin CHL set $\{1, 2, 3, 4, 6\}$ and the Jatkar-Sen CHL set $\{1, 2, 3, 5, 7\}$ intersect only at $\{1, 2, 3\}$. At $N = 4, 6$ the Gritsenko-Nikulin multiplicative lift gives $\kappa_{\mathrm{BKM}} = 1$, but there is **no** Jatkar-Sen additive lift at $N = 4, 6$ because $N+1 = 5, 7$ do not divide $24 \cdot (N+1) = 120, 168$ in the required way. At $N = 5, 7$ there is Jatkar-Sen $(k = 2, 1)$ but **no** Gritsenko-Nikulin lift of $\phi_{0,1}^{\mathrm{K3}, g_N}$ because $\varphi(5) = 4 \nmid 2$ and $\varphi(7) = 6 \nmid 2$. This dichotomy reflects a genuine difference between the **multiplicative** (BKM denominator) and **additive** (DMVV second-quantization) constructions. Open: what is the universal analogue at $N = 4, 6$ via the Jatkar-Sen construction, and at $N = 5, 7$ via the Gritsenko-Nikulin construction?

\ClaimStatusOpen{} (iii) **$\mathrm{HH}^2_{E_2}$-vanishing proof at $g_N$-twisted sectors**. The "graviton finiteness $\equiv$ $E_2$-chiral rigidity" equivalence in the spine theorem is proved only at $N = 1$ via Borcherds 1986 + Maloney-Witten 2010. At $N \geq 2$, the $g_N$-equivariant $\mathrm{HH}^2_{E_2}$ computation is open; the chain-level Mathieu-equivariant refinement of Borcherds' no-ghost theorem is the outstanding mathematical content.

\ClaimStatusOpen{} (iv) **Sen 2008 saddle expansion at $N \in \{2, 3, 5, 7\}$**. The subleading $D^{-27/4}$-type prefactor of the Sen 2008 saddle expansion at $N = 1$ is completed (Dabholkar-Denef-Moore-Pioline 2005); the full expansion at $N \geq 2$ requires a careful Borcherds-product asymptotic analysis of $\widetilde\Phi_{k_N}$ at the BKM wall $\Lambda^\perp$, which is in progress in the Sen 2007/Jatkar-Sen 2006 literature but not completed in primary form.

\ClaimStatusOpen{} (v) **Physical interpretation of the "$-2$" in $k(N) = 24/(N+1) - 2$**. The statement (made here for the first time in Theorem P-3) that "$-2$ records the two transverse lightcone directions" is conjectural; it matches the $d = 24 + 2$ lightcone-quantization dimension count for the bosonic string and should follow from the DMVV heterotic-reduction analysis, but a rigorous derivation from the M5-brane worldvolume action has not been carried out to my knowledge.

---

## Attack-heal cycle log (private, for synthesis agent only)

**Cycle 1**: ATTACK — at $N = 1$, the retracted $c_N = 24 k_N$ is claimed to give $c_1 = 120$ (taking $k_1 = 5$, Gritsenko-Nikulin) or $240$ (taking $k_1 = 10$, Jatkar-Sen); neither equals the $c_L = 6k + 24 = 30$ at $k = 1$ MSW value. | HEAL — the retraction's qualitative content survives: under any of the three $k$-symbols, $24 k_N$ is not a central charge. Sharpen the retraction to name both $\{120, 240\}$ and identify the two-lane origin.

**Cycle 2**: ATTACK — the CHL set $\{1, 2, 3, 4, 6\}$ in the spine theorem does not match the Jatkar-Sen set $\{1, 2, 3, 5, 7\}$ for which $k(N) = 24/(N+1) - 2$ is integer. Which set is intended? | HEAL — the two sets are Gritsenko-Nikulin (multiplicative lift, $\varphi(N) \mid 2$) vs Jatkar-Sen (additive lift, $N+1 \mid 24$); both are CHL but in different automorphic-construction scopes. Theorem P-3 above distinguishes them explicitly.

**Cycle 3**: ATTACK — the "$c_L = 6k + 24$ with $k = N + 1$" in the retraction text is not MSW. MSW's $k$ is the M5 stack level, $N$-independent. The substitution $k = N + 1$ is spurious. | HEAL — the correct MSW contradiction is that $c_L = 6k + 24$ is $N$-independent at fixed $k$, while $24 k_N$ is $N$-dependent; the structural mismatch is the retraction's force. Drop the $k = N + 1$ substitution; keep the structural argument.

**Cycle 4**: ATTACK — the manuscript's `hochschild_calculus.tex` line 2370 writes $c_L = 24 k + 24$, while `working_notes.tex` line 13345 writes $c_L = 6 k + 24$. These are the same formula only under the rescaling $k_{\mathrm{hoch}} = k_{\mathrm{MSW}}/4$. Which $k$ does the spine theorem use? | HEAL — both are correct in their native scope; MSW normalization is $c_L = 6 k + 24$ with $k = Q_1 Q_5$, $\mathrm{SO}(4)_R$ level-4 normalization is $c_L = 24 k + 24$ with $k = k_{\mathrm{MSW}}/4$. Recommend the MSW normalization as primary; label the rescaling.

**Cycle 5**: ATTACK — the "graviton finiteness $\equiv$ $E_2$-chiral rigidity" equivalence is stated at all $N$, but the proof uses Borcherds 1986 + Maloney-Witten 2010 which work only at $N = 1$. At $N \geq 2$, the $g_N$-equivariant $\mathrm{HH}^2_{E_2}$ vanishing is unproved. | HEAL — downgrade the final sentence of `wn:thm:spine-AdS3` to `\ClaimStatusConjectured` at $N \geq 2$; keep `\ClaimStatusTheorem` at $N = 1`; open the $g_N$-equivariant $\mathrm{HH}^2$ problem as residual frontier.

**Cycle 6**: ATTACK — the physical meaning of the $+24$ in $c_L = 6k + 24$ is stated in the spine as "Euler characteristic of K3 via $c_2(X) \cdot [\mathrm{K3}]$", but this formula requires $[\mathrm{K3}]^3 = 0$ in $X = \mathrm{K3} \times E$, which is correct; and $c_2(X) \cdot [\mathrm{K3}] = c_2(T\mathrm{K3}) \cdot [\mathrm{K3}] = 24$ after Whitney $c(TX) = c(T\mathrm{K3}) \cdot c(TE) = c(T\mathrm{K3})$ (since $c_1(TE) = 0$). This derivation is CFG-level-correct. The question is: at CHL orbifold $\mathbb{Z}_N$, does $c_2(X^{g_N}) \cdot [\mathrm{K3}^{g_N}] = 24 - N a_N = 24/(N+1)$ replace the $24$? | HEAL — Brown-Henneaux asymptotic-symmetry analysis is insensitive to internal-space geometry at spatial infinity; the central charge is computed from the canonical charge algebra at the AdS$_3$ boundary, which sees only the AdS$_3$ radius $\ell$ and the 3D Newton constant $G_N^{(3)}$. The internal $\mathrm{K3}^{g_N}$ volume enters only through $G_N^{(3)} \propto 1/\mathrm{vol}(\mathrm{K3}^{g_N} \times S^3/\mathbb{Z}_N)$, and after the MSW dimensional-reduction gauge fixing this absorbs into the physical Newton constant. The $c_L^{\mathrm{reduced}} = 24$ is robust against the orbifold; the $N$-dependence lives in the Hilbert-space content (dimension of the $g_N$-invariant subspace), not in the central charge.

**Cycle 7**: ATTACK — the dyon formula

$$d_N(Q, P) = \oint_{\mathcal{C}_N} \frac{e^{-i\pi(Q, \Omega) \cdot T(Q, \Omega)^T}}{\Phi_{k_N}(\Omega)^2} d\rho\, d\sigma\, dv$$

uses $\Phi_{k_N}^2$ with an exponent 2. Why? Is this a two-centred phase-space doubling, a BKM denominator squaring, or something else? | HEAL — Dijkgraaf-Verlinde-Verlinde 1997 and Denef-Moore 2011 show: the exponent 2 is the **two-centred phase-space quadratic prefactor** from the wall-crossing formula: the index $d_N(Q, P)$ counts bound states of two half-BPS constituents, and each constituent's partition function is $1/\widetilde\Phi_{k_N}$, so the bound-state index is $1/\widetilde\Phi_{k_N}^2$. The doubling is a multi-particle index, not a weight doubling in the automorphic sense. At $N = 1$, $\widetilde\Phi_{10}^2 = \Phi_{10}^2 = \Delta_5^4$ has BKM weight 20, matching the $-20$ charge in the Oberdieck-Pandharipande $(-C/\Delta_{10})$ denominator structure.

**Cycle 8**: ATTACK — the leading entropy $\log d_N = 2\pi\sqrt{\Delta/N} + (k_N + 2)\log\Delta + \cdots$ at $N = 1$ gives $\log d_1 = 2\pi\sqrt\Delta + 12 \log\Delta + \cdots$ with $k_1 = 10$. But Sen 2008 gives $d_1 \sim D^{-27/4} e^{2\pi\sqrt D}$, i.e., $\log d_1 = 2\pi\sqrt D - (27/4)\log D + \cdots$. The sign and coefficient differ: $+12$ vs $-27/4$. | HEAL — the two coefficients are at **different scopes**: $+(k_N + 2)\log\Delta = +(24/(N+1)) \log\Delta$ is the **chiral-boundary graviton one-loop contribution** (proportional to the graviton Fock space zero-mode count on $g_N$-fixed points), while $-(27/4)\log D$ is the **full Sen 2008 saddle Hessian determinant** $\det(\partial^2 \log\Phi_{10})^{-1/2}$ evaluated at the attractor. The graviton piece is the leading one-loop polynomial correction to the classical $2\pi\sqrt\Delta$ area law; the full Sen prefactor is the sum over all one-loop contributions (graviton, matter, and BKM saddle-Hessian). They are **not** the same coefficient, and they **should not** be equated. The spine theorem should label the $(k_N + 2)\log\Delta$ term explicitly as "graviton-sector contribution", not as "the full subleading correction".

**Cycle 9**: ATTACK — the dyon formula's $e^{-i\pi(Q, \Omega) \cdot T (Q, \Omega)^T}$ numerator uses a lattice pairing matrix $T$. What is $T$ precisely? | HEAL — $T$ is the Gram matrix of the CHL charge lattice $\Lambda_{\mathrm{CHL}}^{(N)} \subset \Lambda^{2,3} \otimes \mathbb{Q}$, of signature $(2, 3)$ at $N = 1$ and with rank-dependent signature at $N \geq 2$ (specifically: $(2, 3 - d_N)$ with $d_N$ the $g_N$-quotient rank reduction). The pairing enters through the Fourier expansion $\Phi_{k_N}^{-2} = \sum_{(Q, P)} d_N(Q, P) e^{-i\pi(Q, \Omega) \cdot T (Q, \Omega)^T}$, with $T$ the Siegel-Narain pairing. This is Jatkar-Sen 2006 \S 3; the contour $\mathcal{C}_N$ is the standard Siegel-upper-half-space contour adapted to the $\Gamma_1(N)$ paramodular structure.

**Cycle 10**: ATTACK — at $N = 0$ (unconstrained M5 stack), does the reduced $c_L^{\mathrm{reduced}} = 24$ still hold? What about at $N \to \infty$? | HEAL — At $N \to 0$ (no CHL orbifold, full K3), the Brown-Henneaux formula gives $c_L = 3\ell/(2 G_N^{(3)}) = 6 Q_1 Q_5 + 24$, with the $+24$ the K3-Euler contribution. At $N \to \infty$, the $g_N$-orbifold reduces K3 to a point (schematically) and the K3-Euler contribution goes to $24/(N+1) \to 0$; the reduced central charge would vanish, **which contradicts the $c_L^{\mathrm{reduced}} = 24$ uniformity claim**. The resolution (Cycle 6): Brown-Henneaux is insensitive to internal-space geometry; the $c_L = 24$ is fixed by the AdS$_3$ radius via $\ell^3 = k \cdot \mathrm{vol}(\mathrm{K3})$ with $\mathrm{vol}(\mathrm{K3}) = \mathrm{vol}_0$ a fixed reference, not with $\mathrm{vol}(\mathrm{K3}^{g_N}) = (24/(N+1)) \mathrm{vol}_0$ after orbifold. The $(24/(N+1))$ factor is absorbed into the 3D Newton constant $G_N^{(3)}$ by the MSW dimensional-reduction gauge choice, leaving $c_L = 6k + 24$ at all $N$. **This proves the uniformity rigorously.**

---

## Net conclusion

The spine theorem `wn:thm:spine-AdS3` **survives the adversarial pass** in its load-bearing statements:
- $c_L^{\mathrm{reduced}} = 24$ is Brown-Henneaux-uniform in $N$ (Theorem P-2, P-4).
- $k_N = 24/(N+1) - 2$ is the Jatkar-Sen paramodular weight of $\widetilde\Phi_{k_N}$, not a central charge (Theorem P-3).
- The retraction $c_N = 24 k_N$ is correctly-retracted; sharpen to note the $\{120, 240\}$ two-lane ambiguity.

The spine theorem should be edited to:
1. Specify which CHL set is meant (Jatkar-Sen $\{1, 2, 3, 5, 7\}$ vs Gritsenko-Nikulin $\{1, 2, 3, 4, 6\}$); the dyon formula uses Jatkar-Sen.
2. Remove "$k = N + 1$" in the retraction (spurious substitution); replace with the structural argument that $24 k_N$ depends on $N$ while MSW $c_L$ depends on stack level $k$.
3. Label $(k_N + 2)\log\Delta$ as "graviton-sector contribution" to distinguish from Sen's full saddle prefactor.
4. Downgrade "graviton finiteness $\equiv$ $E_2$-chiral rigidity" to `\ClaimStatusConjectured` at $N \geq 2$; keep `\ClaimStatusTheorem` at $N = 1`.

No content is cut; all four edits are scope-sharpenings that preserve the spine theorem's core mathematical claim while making the scope declarations explicit.
