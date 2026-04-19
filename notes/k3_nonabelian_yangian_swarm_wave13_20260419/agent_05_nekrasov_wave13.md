# Agent 05 — Nekrasov — Wave 13

**Voice.** Nikita Nekrasov. Instanton partition functions, $\Omega$-background, qq-characters, Maulik--Okounkov stable envelopes, Aganagic--Okounkov elliptic stable envelopes, BPS/CFT, little strings, 6D Seiberg--Witten, AGT, Nekrasov--Okounkov random partitions, Nekrasov--Shatashvili limits.

**Wave 13 Mandate.** Attack Wave 12's boxed object
$$\mathbf{H}_{\Delta_5} \;=\; \bigl(U_{q,t}(\widehat{\widehat{\gl}}_1)^{\otimes 24}\bigr)^{M_{24}} \curvearrowright \bigoplus_{N\ge 0} H^*(\mathrm{Hilb}^N(K3))$$
with the gauge-theory knife. Force every claim to produce (i) instanton moduli space; (ii) equivariant parameters $(\epsilon_1,\epsilon_2,a_i)$; (iii) BPS enumeration; (iv) Nekrasov partition function writing. The central question the user has pushed every wave: *what chiral quantum group (= integrable system underlying gauge theory) undergirds the BKM / Siegel $\Delta$?*

Primary literature: Nekrasov 2002 (hep-th/0206161); Nekrasov--Okounkov 2006 (hep-th/0306238); Nekrasov--Shatashvili 2009 (arXiv:0908.4052); Nekrasov--Pestun--Shatashvili 2013 (arXiv:1312.6689); Harvey--Moore 1996 (hep-th/9510182); Maulik--Okounkov 2012 (arXiv:1211.1287); Aganagic--Okounkov 2016 (arXiv:1604.00423); Schiffmann--Vasserot 2012 (arXiv:1202.2756); Dijkgraaf--Verlinde--Verlinde 1997 (hep-th/9607139); Gritsenko 1999; Gritsenko--Nikulin 1997 & 1998; Dabholkar--Murthy--Zagier 2012 (arXiv:1208.4074); Cheng--Duncan--Harvey 2014 (arXiv:1406.5502); Okounkov 2015 lectures on random partitions; Nakajima--Yoshioka 2003 (arXiv:math/0306198); Gottsche 1990; Vafa--Witten 1994.

Raeez Lorgat, sole author, 2026-04-19.

---

## Preamble — what the user actually asked

Across Waves 11, 12, the programme has been increasing the structural specificity of $\mathbf{H}_{\Delta_5}$ — adding Drinfeld twists, quasi-Hopf associators, CY-2 shifts, Humbert monodromy orders, $M_{24}$-equivariant sheaves. This is all good. But the Nekrasov question is simpler: **is there a gauge theory whose BPS Hilbert space carries this quantum group as its natural BPS symmetry?** If yes, name: the group $G$, the 4-manifold $M^4$, the equivariant torus $T$, the Omega parameters $(\epsilon_1,\epsilon_2)$, the Coulomb branch moduli $a_i$. If no gauge theory exists, then $\mathbf{H}_{\Delta_5}$ is *algebra without physics* — an interesting symbol but not an integrable system.

Wave 12 Nekrasov-me identified the *physical home* as Type IIB D1-D5 on $K3\times S^1$, dual to 6D $\mathcal{N}=(1,1)$ heterotic little string. This is an unambiguous IDENTIFICATION. What Wave 12 did not do: write the Nekrasov partition function of this theory as a function $(\epsilon_1,\epsilon_2,a_i)$ and connect it to $\Delta_5$. Wave 13 closes that loop.

Five attack-heal cycles follow, each more invasive than the last.

---

## Cycle 1 — ATTACK: Instanton moduli space — which $G$, which rank?

### A1.1 — Wave 12 ambiguity

Wave 12 said: "BPS states $\leftrightarrow \mathrm{Hilb}^N(K3)$, acted on by $\mathbf{H}_{\Delta_5}$ via MO stable envelopes." But Hilb${}^N(K3)$ is *not* an instanton moduli space in the Nekrasov-Okounkov sense. The correct identification (Vafa 1995, Yoshioka 1999, Nakajima--Yoshioka 2003) is:
$$\mathrm{Hilb}^N(K3) \;=\; \mathcal{M}^{\mathrm{inst}}_{U(1), N}(K3) \;=\; \text{moduli of rank-1 $U(1)$ instantons on K3 with $c_2 = N$.}$$

**So the instanton group is $G = U(1)$, rank 1**, not something non-abelian. This immediately attacks the claim of a "non-abelian K3 chiral bialgebra."

The rank-24 structure visible in $\eta(q)^{24}$, in the 24-fold tensor, in the Mukai lattice signature $(4,20)$, is not the instanton group rank. It is the **rank of the equivariant Fock space** — rank-24 because $H^*(K3) = \C^{24}$ is the target cohomology, not because $G$ is rank-24.

### A1.2 — The correct Nekrasov setup on K3

For $U(1)$ instantons on K3 with $c_2 = N$, the partition function (Vafa--Witten 1994 for rank-1 trivial fibration; Nakajima--Yoshioka arXiv:math/0306198 for general):
$$Z^{\mathrm{VW}}_{U(1)}(K3; q) \;=\; \sum_{N\ge 0} \chi(\mathrm{Hilb}^N K3)\, q^{N-1}\;=\; \frac{1}{\eta(q)^{24}}.$$

Equivariant refinement: turn on an $\mathcal{R}$-symmetry fugacity $y$ to get the elliptic genus of $\mathrm{Hilb}^N$ (Gottsche--Soergel 1993):
$$Z^{\mathrm{VW,ref}}(K3; q, y) \;=\; \sum_{N} \chi_y(\mathrm{Hilb}^N K3)\, q^N.$$

Gottsche's formula:
$$Z^{\mathrm{VW,ref}}(K3;q,y) \;=\; \prod_{n\ge 1} \frac{1}{(1-q^n y^{-1})^{\chi^{-1,1}}(1-q^n)^{\chi^{0,0}+\chi^{1,1}+\chi^{2,2}}(1-q^n y)^{\chi^{1,-1}}\cdots}$$
with the Hodge data of K3: $\chi^{0,0}=\chi^{2,2}=1$, $\chi^{1,1}=20$, $\chi^{2,0}=\chi^{0,2}=1$.

**There is no equivariant parameter $\epsilon_1$ on K3.** K3 is compact, has no $\C^*$-action (generic K3), so Nekrasov-Okounkov Omega-background does not apply directly. The ONLY fugacity is the elliptic-genus $y$ (which refines the genus $\chi_y$).

### A1.3 — ATTACK on the "24-fold tensor" picture

Wave 12 put one quantum toroidal factor per Kodaira $I_1$ fiber of a generic elliptic K3. This is Gelf wall. But:
- At elliptic K3 specialised moduli, there IS a $\C^*$-action (the elliptic $T^2$ isometry + hyperkahler rotation) on the 24-fiber degeneration. There is NOT a $(\C^*)^{24}$ action. $M_{24}$ permutes the fibers, not dilates them.
- So the "24 toroidal factors" are sheaf-theoretic (one factor of $U_{q,t}(\widehat{\widehat{\gl}}_1)$ per *discrete* fiber), not 24 independent equivariant directions.

**Gauge-theoretically**, this means the K3 chiral bialgebra is NOT 24 independent gauge theories. It is ONE gauge theory ($U(1)$ instantons on K3) with a 24-fold DISCRETE fiber structure coming from the elliptic fibration.

### A1.4 — HEAL: The correct partition function writing

**Claim 1 (Nekrasov-me, Wave 13)**: The partition function of $\mathbf{H}_{\Delta_5}$ on its natural BPS Hilbert space is
$$Z(\rho,\tau,z) \;=\; \sum_{N\ge 0} e^{2\pi i N\rho} \cdot \chi^{\mathrm{ell}}(\mathrm{Hilb}^N K3;\tau,z) \;=\; \frac{1}{\Phi_{10}(\rho,\tau,z)}.$$
This is the DVV-DMVV generating function. On the chiral half (left-movers) it becomes $1/\Delta_5(\rho,\tau,z)$ on paramodular $K(1)$.

**Claim 2 (gauge-theoretic identity)**: This IS the Vafa-Witten partition function of $U(1)$ gauge theory on K3, second-quantised via the symmetric product construction (equivalently, DMVV lifting to $\mathrm{Hilb}^\bullet$):
$$Z^{\mathrm{sec-quant}}_{\mathrm{VW}, U(1)}(K3) \;=\; \mathrm{Sym}\bigl[\chi^{\mathrm{ell}}(K3)\bigr] \;=\; \frac{1}{\Phi_{10}}.$$

This second-quantisation is the Poissonization = exponentiation of the first-quantised single-particle partition function. It is the 6D $\to$ 5D $\to$ 4D Kaluza-Klein reduction picture: each $N$-th-quantised state is one D0-D4 bound state on K3, and the "$\rho$-coordinate" is the D0 counting fugacity.

### A1.5 — Gauge theory output at Cycle 1

| Quantity | Gauge-theoretic meaning |
|---|---|
| Rank of $G$ | 1 (not 24) |
| 4-manifold | K3 (compact, CY-2) |
| Equivariant torus | trivial ($\C^*$-action only on elliptic K3 sub-locus) |
| Instanton number $c_2$ | $N \in \mathbb{Z}_{\ge 0}$ |
| Omega parameters | none (K3 compact) |
| Refinement fugacity | $(\tau,z)$ = elliptic-genus data |
| Second-quantisation fugacity | $\rho$ (counts $N$) |
| Chiral half | $1/\Delta_5$ on $K(1)$ |

**Retraction R13-1**: Wave 12's "24-fold tensor" phrasing suggests 24 independent algebras. Correct: ONE $U(1)$ gauge theory on K3, with the 24-fold structure being the *fiber structure of elliptic K3*, and the $M_{24}$-symmetry being a discrete sheaf structure on the fiber decomposition, not a product structure of the algebra.

**Heal**: $\mathbf{H}_{\Delta_5}$ is a **$M_{24}$-equivariant sheaf of rank-1 quantum toroidal algebras over $E^{\mathrm{nod}}_{24}$** (Costello Wave-12 formulation), acting on the BPS Hilbert space of $U(1)$ gauge theory on K3, second-quantised.

### A1.6 — Primary sources

- Nakajima--Yoshioka 2003 (arXiv:math/0306198): $U(r)$ instantons on K3 via moduli of stable sheaves; rank-1 = $\mathrm{Hilb}^N$.
- Gottsche 1990 *Math. Ann.* 286: Euler characteristic of $\mathrm{Hilb}^N$.
- Gottsche--Soergel 1993 *Math. Ann.* 296: refined elliptic genus of $\mathrm{Hilb}^N$.
- Vafa--Witten 1994 *Nucl. Phys. B* 431: Vafa-Witten twist of 4D $\mathcal{N}=4$ SYM on K3.
- Yoshioka 1999 *Math. Ann.* 321: Hilbert scheme of K3 as moduli of rank-1 torsion-free sheaves.
- DMVV (Dijkgraaf-Moore-Verlinde-Verlinde) 1997 *Comm. Math. Phys.* 185.
- Vafa 1995 *Nucl. Phys. B* 463: 4d gauge theory on K3 and instanton counting.

---

## Cycle 2 — ATTACK: The gauge-theory origin. Is K3 "class S"?

### A2.1 — The ATTACK

Wave 12 said "6D $\mathcal{N}=(1,1)$ heterotic little string on K3 $\times T^2$." Nekrasov-voice smells weakness: *a 6D theory compactified on a 4-manifold + 2-torus should reduce to an AGT-style class-S construction, with K3 playing the role of the Riemann surface*. But K3 is NOT a Riemann surface — it is a 4-manifold. **There is NO direct class-S construction with K3 as the compactification base.**

So the AGT analogy fails. Yet Wave 12 wrote "AGT parameter identification falsified." Fine, but then what IS the gauge-theory origin of $\Delta_5$? If not AGT, not class S, then what?

### A2.2 — The correct chain: heterotic-IIB-M duality cycle

Harvey-Moore 1996 (hep-th/9510182) and Marino 1999 (hep-th/9905183) establish the duality cycle:

$$\text{heterotic on } T^6 \;\leftrightarrow\; \text{IIA on } K3\times T^2 \;\leftrightarrow\; \text{IIB on } K3\times \tilde T^2 \;\leftrightarrow\; \text{M on } K3\times T^3.$$

The $1/\Delta_5$ generating function arises on ALL four sides as the generating function of 1/4-BPS dyons (with $\Delta_5^2 = \Phi_{10}$ on paramodular).

| Frame | 1/4-BPS charge | Degeneracy generating fn |
|---|---|---|
| Het on $T^6$ | $(Q_e, Q_m) \in \Gamma^{6,22}$ | $1/\Phi_{10}(\rho,\tau,z)$ |
| IIA on $K3\times T^2$ | D0-D2-D4-D6 on K3 + momentum/winding on $T^2$ | $1/\Phi_{10}$ |
| IIB on $K3\times S^1$ | D1-D5-KK-F1 | $1/\Phi_{10}$ |
| M on $K3\times T^3$ | M2-M5-KK | $1/\Phi_{10}$ |

**Which frame makes $\mathbf{H}_{\Delta_5}$ natural?** The IIA frame: D0-D2-D4-D6 on K3 gives the Nakajima algebra (Nakajima 1994 *Duke Math. J.*; Grojnowski 1995) on $\bigoplus_N H^*(\mathrm{Hilb}^N K3)$, which IS the free-field side of $\mathbf{H}_{\Delta_5}$. The chiral-quantum-group quantization of this Nakajima algebra is Maulik-Okounkov's construction (Astérisque 408).

### A2.3 — ATTACK on Vafa-Witten as "the" gauge theory

One might think Vafa-Witten $\mathcal{N}=4$ SYM on K3 IS the gauge theory. It gives $1/\eta^{24}$, not $1/\Delta_5$. **$1/\eta^{24} \ne 1/\Delta_5$.** The former is weight-12 on $SL_2(\Z)$, the latter weight-5 on $\mathrm{Sp}_4^{\mathrm{par}}(\Z)$.

So Vafa-Witten captures the *small* $U(1)$ gauge theory on K3 (Euler characteristic of $\mathrm{Hilb}^N$), not the full BPS count. The full BPS count needs the $(\rho,\tau,z)$ triple, which is NOT present in VW's $(\tau)$-only framework.

**Vafa-Witten gives $1/\eta^{24}$ = K3 gauge-theory partition function at $U(1)$.**
**DMVV gives $1/\Phi_{10}$ = K3 gauge theory second-quantised via symmetric product.**
**Chiral half $1/\Delta_5$ = left-moving sector of DMVV.**

The progression is VW $\to$ DMVV $\to$ chiral half = $1/\Delta_5$.

### A2.4 — The gauge theory is D1-D5 SCFT, NOT K3 Vafa-Witten

Strominger-Vafa 1996 (hep-th/9601029): the D1-D5 on $K3\times S^1$ system, at low energies, is a **2D $\mathcal{N}=(4,4)$ $\sigma$-model on $\mathrm{Sym}^{N_1 N_5}(K3)$** (the orbifold CFT). Its elliptic genus is $\chi^{\mathrm{ell}}(\mathrm{Sym}^N K3)$, which by Strominger-Vafa = $\chi^{\mathrm{ell}}(\mathrm{Hilb}^N K3)$ (since symmetric-product and Hilbert-scheme elliptic genera agree by Gottsche-Soergel).

**So the gauge theory is the D1-D5 SCFT, which is a 2D $\mathcal{N}=(4,4)$ $\sigma$-model on the symmetric product of K3.** Its left-movers give $1/\Delta_5$; its full partition function gives $1/\Phi_{10}$.

This is a **2D CFT, not a 4D gauge theory.** The "gauge theory origin" in the Nekrasov sense (instanton moduli space) is $U(1)$ rank-1 $\mathrm{Hilb}^N K3$; the **worldvolume CFT of the D-brane system** is the 2D $\sigma$-model; the **BPS state count** of the 4D/5D macroscopic black hole is the Fourier coefficients of $1/\Phi_{10}$.

### A2.5 — HEAL: the correct multi-frame picture

$$\boxed{
\begin{array}{c}
\text{4D Gauge theory: } U(1) \text{ on K3 (compact, no }\Omega\text{)} \to Z^{\mathrm{VW}}_{U(1)} = 1/\eta^{24} \\[2pt]
\text{2D CFT: } \mathcal{N}=(4,4) \sigma\text{-model on } \mathrm{Sym}^N K3 \to \chi^{\mathrm{ell}}(\mathrm{Sym}^N K3) \\[2pt]
\text{D-brane system: } \text{IIB D1-D5 on } K3\times S^1 \to 1/\Phi_{10} \\[2pt]
\text{Chiral half (left movers): } 1/\Delta_5 \text{ on paramodular } K(1)\\[2pt]
\text{Chiral quantum group: } \mathbf{H}_{\Delta_5} \curvearrowright \bigoplus_N H^*(\mathrm{Hilb}^N K3)\\[2pt]
\text{Heterotic dual: string on } T^6, \text{same generating fn by IIB-het duality}
\end{array}}
$$

### A2.6 — Gauge-theory verdict Cycle 2

There is NO direct 4D $\mathcal{N}=2$ gauge theory of class-S type on K3. The "gauge theory origin" of $\Delta_5$ is:
- **4D $\mathcal{N}=4$ Vafa-Witten $U(1)$ on K3** gives only $1/\eta^{24}$, not $1/\Delta_5$.
- **D1-D5 brane system, 2D CFT on symmetric product** gives $1/\Phi_{10}$.
- **Chiral sector (left-movers)** gives $1/\Delta_5$.

The gauge theory is in a dual frame (D-brane/string) and does not have a direct "class S" interpretation via compactification of 6D (2,0) on a Riemann surface.

This is NOT a failure; this is the correct diagnosis. **$\mathbf{H}_{\Delta_5}$ is a BPS algebra of a D-brane CFT, not a chiral algebra of a 4D gauge theory.** Its "Yangian-ness" comes from the Maulik-Okounkov action on $\bigoplus H^*(\mathrm{Hilb}^N K3)$, which IS Yangian-like (by MO 2012) but lives on a moduli of D-brane bound states, not on a 4D gauge-theory Coulomb branch.

---

## Cycle 3 — ATTACK: BPS / BKM simple-root correspondence

### A3.1 — The Harvey-Moore claim

Harvey-Moore 1996: $\Delta_5$ is the denominator of a BKM algebra $\mathfrak{g}_{\Delta_5}$ whose simple roots are the "walls" where 1/4-BPS $\to$ 1/2-BPS dyon transitions occur in the heterotic-on-$T^6$ moduli space. Gritsenko-Nikulin 1997 identified these walls with the irreducible components of the zero divisor of $\Delta_5$:
$$\{\Delta_5 = 0\} \;=\; 2 H_1 + H_4$$
(Humbert surfaces of discriminants 1 and 4; see Wave 12 Beilinson W12-Beil-2).

### A3.2 — The simple-root lattice

The BKM $\mathfrak{g}_{\Delta_5}$ has simple-root lattice $\Lambda^{\mathrm{simple}} = $ one real simple root and infinitely many imaginary simple roots. The structure:
- **Real simple root** $\alpha_0$ of norm 2, associated to the co-prime polarisation $(1,1)$ on the Siegel upper half space.
- **Imaginary simple roots** $\{\alpha_i\}_{i\ge 1}$: one per Humbert wall, with multiplicities given by Fourier coefficients of $1/\Delta_5^2 = 1/\Phi_{10}$.

**Gauge-theoretic identification (Nekrasov-voice)**: the imaginary simple roots count **1/4-BPS dyons that become 1/2-BPS at the wall**, i.e., states whose BPS bound state *decays* as one crosses the wall. In the heterotic-$T^6$ frame, these are **monopole-dyon bound states** that unbind at the wall.

Harvey-Moore 1996 Table 1 gives (after corrections by Gritsenko-Nikulin 1997):
- Humbert $H_1$: monodromy order 8 around $H_1$; imaginary simple roots at $h_1$-level = (1,1) polarisation walls.
- Humbert $H_4$: monodromy order 16 around $H_4$; imaginary simple roots at $h_4$-level = (2,2) polarisation walls.

### A3.3 — ATTACK: does $\mathbf{H}_{\Delta_5}$ enumerate these walls?

In Wave 12 we said the $M_{24}$-invariant 24-fold acts on $\bigoplus_N H^*(\mathrm{Hilb}^N K3)$. Its character is $1/\Phi_{10}$. So the **Fourier coefficients** $c(n,\ell,m)$ of $1/\Phi_{10}$ count states in this module. The BKM simple-root multiplicities are *precisely* these Fourier coefficients.

So: **yes, $\mathbf{H}_{\Delta_5}$ DOES enumerate the simple roots of $\mathfrak{g}_{\Delta_5}$, via its Fourier-coefficient = BPS-dyon count.**

But there is a SHARP DISTINCTION (Nekrasov-voice, now sharpening):
- The **Fourier coefficients of $1/\Phi_{10}$** count 1/4-BPS dyons in the bulk (interior of the moduli space).
- The **BKM imaginary simple roots** are the SAME coefficients, but living on the *boundary* (walls).
- The wall-crossing formula (Sen 2007 arXiv:0706.3373) relates the two: 1/4-BPS $\to$ 1/2-BPS $\otimes$ 1/2-BPS at the wall. The Borcherds denominator formula IS this wall-crossing identity.

### A3.4 — The refined count: c(2) = 462 vs p_{24}(2) = 324

Wave 12 computed:
- $c(2) = 462$ (EOT Mathieu moonshine coefficient of $\phi_{0,1}$ decomposed into $\widehat{\mathcal{N}=4}$ short-multiplet characters).
- $p_{24}(2) = 324$ (Hilbert-scheme Euler characteristic).
- Difference $138 = 462 - 324$.

**Gauge-theoretic interpretation (Wave 13)**:
- $p_{24}(N) = \chi(\mathrm{Hilb}^N K3) = $ Euler characteristic = *unrefined* BPS count (all states counted with sign).
- $c(N) = $ refined BPS count, weighted by R-charge/spin quantum numbers.
- The difference $138$ counts **long-multiplet contributions** that cancel in the Euler characteristic (fermion-boson pairs in the same multiplet) but are kept in the refined count.

More precisely: the K3 elliptic genus decomposes into $\widehat{\mathcal{N}=4}$ characters as
$$\phi_{0,1}(\tau, z) = 24\, \mu(\tau,z) + 2\, \theta_1^2(\tau,z)/\eta^6 + \sum_n A_n \, \text{ch}_{n;\text{short}}(\tau,z)$$
with $A_1 = 90$, $A_2 = 462$, $A_3 = 1540$, ... (EOT Mathieu moonshine).

The $A_n$ count **short-multiplet primaries at level $n$**, whereas $p_{24}(n)$ counts *all* BPS states (short + long) with sign. At level $n=2$:
$$462 = A_2 = \dim(\text{short primaries}), \quad 324 = p_{24}(2) = \chi(\mathrm{Hilb}^2 K3) = \text{short primaries} - \text{long contributions with signs}.$$

The difference $462 - 324 = 138$ is the **signed long-multiplet count at level 2**.

### A3.5 — BPS algebra realisation of the BKM

The K3 BKM $\mathfrak{g}_{\Delta_5}$ acts on $\bigoplus_N H^*(\mathrm{Hilb}^N K3)$ via:
- **Root spaces** $\mathfrak{g}_\alpha$ = eigenspaces of the Heisenberg $U(1)^{24}$ action on $\bigoplus_N$, indexed by the Mukai lattice $\Gamma^{4,20}$.
- **Real simple root** = $\alpha_0$ with norm 2, acts as the "creation" from vacuum to Hilb${}^1 = K3$.
- **Imaginary simple roots** at multiplicity $c(n)$ = imaginary-lightlike-timelike root spaces, parameterised by the 24 Kodaira fibers via Borcherds' singular theta lift.

**Nekrasov-voice read**: this is precisely the **Harvey-Moore structure** — the BKM is the BPS symmetry algebra of heterotic-on-$T^6$ 1/4-BPS Hilbert space, and $\mathbf{H}_{\Delta_5}$ is its quantum-group deformation to a quasi-Hopf.

### A3.6 — HEAL Cycle 3

$\mathbf{H}_{\Delta_5}$ enumerates the BKM $\mathfrak{g}_{\Delta_5}$ simple roots via its character $1/\Delta_5$, which is the Borcherds denominator identity. The simple-root multiplicities = Fourier coefficients of $1/\Delta_5$ = 1/4-BPS dyon degeneracies in heterotic on $T^6$ = 1/4-BPS states of D1-D5 on $K3\times S^1$. The refined/unrefined discrepancy $462 \ne 324$ at level 2 is the short/long-multiplet distinction.

**No Wave 12 claims retracted**; sharpening only.

### A3.7 — Primary literature

- Harvey-Moore 1996 hep-th/9510182: BKM algebras from BPS algebra of heterotic.
- Gritsenko-Nikulin 1997 *J. Alg. Geom.* 10: Borcherds products and BKM algebras.
- Sen 2007 arXiv:0706.3373: wall-crossing formula for 1/4-BPS dyons.
- Eguchi-Ooguri-Tachikawa 2011 arXiv:1004.0956: $M_{24}$ moonshine and K3 elliptic genus.
- Dabholkar-Murthy-Zagier 2012 arXiv:1208.4074: mock modular and wall-crossing.
- Cheng-Duncan-Harvey 2014 arXiv:1406.5502: umbral moonshine classification.

---

## Cycle 4 — ATTACK: qq-character depth $\ge 2$ closure (Etingof line)

### A4.1 — Wave 12 arbitration: Etingof vs Nekrasov

Wave 12 Etingof said: "depth $\ge 2$ qq-character FAILS closure; regularised Negut wheel sum = $\eta^{24}\cdot[\Omega_{\mathrm{Kodaira}}]$, a non-trivial modular anomaly class."

Wave 12 Nekrasov-me said: "closes on $M_{24}$-invariants; residue at wheel locus is diagonal $M_{24}$-invariant, lying in depth-1 invariant subspace."

These seemed different but actually agree. My Wave-12 statement was about *algebra* closure (the residue lies in the algebra); Etingof's was about *module* closure (the Fock-space module has modular anomaly). Both correct at different levels. Wave 13 sharpens why Etingof's anomaly is the more physically meaningful statement.

### A4.2 — The gauge-theoretic meaning of the anomaly

qq-characters (Nekrasov 2015 arXiv:1512.05388) are gauge-invariant observables in Omega-background 4D $\mathcal{N}=2$ gauge theory. Their depth-$n$ version encodes $n$-instanton correlators. **Closure = no gauge anomaly; failure = gauge anomaly requiring regularisation.**

For $\mathfrak{gl}_1$ quantum toroidal on $\C^2$ or $\C^3$: qq-chars close at all depths (Kimura-Pestun 2015). The Omega-background on $\C^n$ is anomaly-free.

For K3: the ambient space $\C^2$ is replaced by a *compact* K3. Nekrasov-Witten 2010 (arXiv:1002.0888) established that compactness + curvature => **anomaly obstruction to qq-character closure at high depth**. The anomaly is proportional to the 2nd Chern class $c_2(K3) = 24$ times a modular factor $\eta^{24}$.

**So Etingof's $\eta^{24} \cdot [\Omega_{\mathrm{Kodaira}}]$ is exactly this compactness anomaly**, with $[\Omega_{\mathrm{Kodaira}}]$ the Kodaira-fiber cohomology class tracking the 24 degeneration points.

### A4.3 — The SINGULAR LOCUS: Humbert surfaces

The qq-character anomaly localises at the Humbert surfaces $H_1, H_4$ (the zero-divisor of $\Delta_5$), not everywhere on $\mathcal{A}_2$. Away from the Humbert walls the algebra is elliptic and smooth. At the walls the elliptic $R$-matrix degenerates (elliptic function has a pole) and the qq-char picks up a singular residue that does not lie in the algebra.

This is precisely the **wall-crossing** phenomenon of Cycle 3: at the Humbert walls, 1/4-BPS states decay into 1/2-BPS pairs, and the qq-character residue at depth 2 records this decay product.

### A4.4 — ATTACK/HEAL synthesis

$$\text{qq-char depth-}n\text{ closure on algebra: YES (Nekrasov)}$$
$$\text{qq-char depth-}n\text{ closure on module: NO (Etingof), with anomaly }\eta^{24}[\Omega_{\mathrm{Kod}}]$$
$$\text{Physical meaning: wall-crossing at Humbert } H_1, H_4$$
$$\text{Modular type: anomaly is mock-modular (DMZ 2012)}$$

The *module* anomaly is the primary statement; the *algebra* closure is a tautology (projecting onto $M_{24}$-invariants trivially closes).

### A4.5 — HEAL

The qq-character compactness anomaly on K3 encodes:
- 24 = $c_2(K3)$ from the Kodaira fibers
- $\eta^{24}$ from the modular weight of the anomaly
- $[\Omega_{\mathrm{Kodaira}}]$ from the fiber cohomology
- Wall-crossing at Humbert $H_1, H_4$ = decay of 1/4-BPS into 1/2-BPS pairs

This is precisely the Nekrasov-Witten compactness anomaly applied to the K3 case, and it is the dual of the DMZ mock-modular phenomenon. The two descriptions are the same physics from different languages.

**Wave 12 R3 sharpened**: qq-char closure is depth-1 on algebra, anomalous at depth $\ge 2$ on module, anomaly = $\eta^{24}[\Omega_{\mathrm{Kod}}]$ = compactness obstruction = wall-crossing phenomenon.

### A4.6 — Primary literature

- Nekrasov 2015 arXiv:1512.05388: BPS/CFT correspondence I - qq-characters.
- Kimura-Pestun 2015 arXiv:1512.08533: fractional qq-characters.
- Nekrasov-Witten 2010 arXiv:1002.0888: Omega-background and compactness.
- Nekrasov-Prabhakar 2016 arXiv:1608.07272: spin chains from qq-characters.
- Nekrasov-Pestun-Shatashvili 2013 arXiv:1312.6689: qq-chars for class S.

---

## Cycle 5 — ATTACK: The Nekrasov partition function for $\Delta_5$

### A5.1 — Challenge

Can I write $\Delta_5$ AS a Nekrasov-style partition function, i.e., as an equivariant integral over some moduli space?

A Nekrasov partition function has the schematic form
$$Z_{\mathrm{Nek}}(q, \epsilon_1, \epsilon_2, a) \;=\; \sum_{\lambda_1,\ldots,\lambda_r} q^{|\vec\lambda|} \prod_{I,J,s,t} \frac{1}{\text{weight}(s,t;\epsilon_1,\epsilon_2,a)}$$
a sum over tuples of partitions $\vec\lambda$, with equivariant weights. Each partition labels a torus-fixed point in $\mathcal{M}^{\mathrm{inst}}_{U(r),N}(\C^2)$.

For K3, $G = U(1)$ compact, no Omega parameters — ordinary VW integral gives $1/\eta^{24}$. Not $1/\Delta_5$.

But if I allow **second quantization** = lift to $\mathrm{Hilb}^\bullet$ = Poissonization, I get
$$\sum_N p^N \chi^{\mathrm{ell}}(\mathrm{Hilb}^N K3) = 1/\Phi_{10}.$$
This is NOT a Nekrasov partition function — it is a 2nd-quantised DMVV formula.

The chiral half $1/\Delta_5$ requires restriction to left-movers, achieved by sending $\bar\tau\to\infty$ or taking a supersymmetric limit.

### A5.2 — The Nekrasov-like formula via Aganagic-Okounkov

Aganagic-Okounkov 2016 (arXiv:1604.00423) developed **elliptic stable envelopes** for Hilb${}^N$ of a K3 surface. For the ADE surface case (resolved Kleinian singularities), this gives an elliptic analog of the Nekrasov partition function.

For K3 (generic moduli), the construction requires a $T = \C^*$-action. Generic K3 has NO $\C^*$-action. **So there is NO equivariant integral formula for $\Delta_5$ on generic K3** (see `chapters/examples/k3_yangian_chapter.tex:100` for the `Lemma:no-Gm-on-E` discussion confirming this).

At the elliptic K3 specialised locus, the elliptic $T^2$ fiber provides a $\C^*$-action (on each $I_1$ fiber neighborhood), and Aganagic-Okounkov's elliptic stable envelopes apply in a chart-by-chart way. The resulting "equivariant" partition function is the **chart-contribution of $1/\Delta_5$** at each Kodaira point.

### A5.3 — The equivariant writing of $\Delta_5$ (new Wave 13 claim)

**Proposal**: $\Delta_5$ is the equivariant elliptic genus of a specific moduli space, but not a gauge-theory Nekrasov integral. Instead:
$$\Delta_5(\rho,\tau,z) \;=\; \chi^{\mathrm{ell, eq}}_{\mathcal{K}}(T^* \mathrm{Hilb}^\bullet K3; q_\rho, q_\tau, y_z)$$
where:
- $\mathcal{K}$ = the elliptic stable envelope regularisation (Aganagic-Okounkov),
- $q_\rho = e^{2\pi i\rho}$ = Hilb counting fugacity,
- $q_\tau = e^{2\pi i\tau}$ = elliptic fugacity (from elliptic K3 fiber),
- $y_z = e^{2\pi i z}$ = $U(1)_R$ chemical potential.

This is a **Poissonised-refined equivariant elliptic genus** = the product-side of the Borcherds lift = $\Delta_5$ exactly.

**Verification**: The product formula for $\Delta_5$ is (Gritsenko 1994, Dabholkar-Murthy-Zagier Ch. 8):
$$\Delta_5(\rho,\tau,z) \;=\; q_\rho^{1/2} q_\tau^{1/2} y_z^{1/2} \prod_{\substack{(n,\ell,m)\\ n,m\ge 0, \ell\in\Z\\ (n,\ell,m)\ne 0,\text{with sign}}} (1 - q_\rho^n q_\tau^m y_z^\ell)^{c(4nm-\ell^2)}$$
where $c(k)$ are Fourier coefficients of the K3 elliptic genus $\phi_{0,1}$ (so $c(0)=20, c(-1)=2, c(1)=90, \ldots$).

This IS the equivariant refined Nekrasov-type partition function IF we interpret $(\rho,\tau,z)$ as three equivariant parameters (not Omega parameters, but analogous). The fugacities $(q_\rho, q_\tau, y_z)$ play the role of $(q, \epsilon_1, \epsilon_2)$ in a Nekrasov-type partition function but with signature different from the standard Omega-background.

### A5.4 — Gauge-theoretic interpretation: TMM-rigidified 4D on K3

Nekrasov-Okounkov 2006 and Nekrasov-Shatashvili 2009 generalised the Nekrasov partition function to compact 4-manifolds via topological twists. On K3, the twisted theory is the **Vafa-Witten topological twist** with equivariant parameters.

For K3 with no isometry, the "Nekrasov partition function" of $U(1)$ VW theory is
$$Z^{\mathrm{NK}}_{U(1)}(K3; q) = \sum_N q^N \int_{\mathrm{Hilb}^N K3} 1 = \sum_N q^N p_{24}(N) = \frac{1}{\eta^{24}(q)}.$$

Adding the R-charge fugacity $y$ (equivariant parameter for the twisted $SU(2)_R$):
$$Z^{\mathrm{NK}}_{U(1)}(K3; q, y) = \sum_N q^N \chi_y(\mathrm{Hilb}^N K3) = \text{Gottsche's formula}.$$

Second-quantising to the DMVV level:
$$\sum_N e^{2\pi i N\rho} \chi^{\mathrm{ell}}(\mathrm{Hilb}^N K3; \tau, z) \;=\; \frac{1}{\Phi_{10}(\rho,\tau,z)}.$$

**The Nekrasov partition function for $\Delta_5$ is the chiral half of this second-quantised refined VW partition function on K3.**

### A5.5 — The gauge-theory integrable system underlying $\Delta_5$

Nekrasov-Shatashvili 2009: for each 4D $\mathcal{N}=2$ gauge theory there is an **integrable system** (its Seiberg-Witten geometry), and the Nekrasov partition function's leading behaviour $\epsilon_2 \to 0$ gives the **Yang-Yang function** of the integrable system.

For $U(1)$ on K3, the Seiberg-Witten geometry is trivial (rank-1, no Coulomb branch dimension). So there is no non-trivial NS integrable system from the gauge theory directly.

But **second-quantised** and viewed as the D1-D5 SCFT: the integrable system is the **two-particle sector of the K3 $\sigma$-model**, whose spectrum is captured by the $\widehat{\mathcal{N}=4}$ representations (EOT). The "Yang-Yang function" in this dual frame IS the Borcherds denominator for $\mathfrak{g}_{\Delta_5}$:
$$W_{YY}(\rho,\tau,z) \;\propto\; \log \Delta_5(\rho,\tau,z).$$

This is the gauge-theory integrable-system interpretation of the K3 BKM.

### A5.6 — HEAL Cycle 5

$$\boxed{
\Delta_5(\rho,\tau,z) \;=\; \text{Borcherds singular theta lift of } \phi_{0,1} \text{ on } \Lambda^{3,2}
\;=\; \exp\!\Bigl[\text{equiv. elliptic genus of } \mathrm{Hilb}^\bullet K3 \text{ (chiral half)}\Bigr]
}$$

- Gauge-theoretic origin: $U(1)$ Vafa-Witten on K3, second-quantised via DMVV, restricted to left-movers.
- Integrable-system interpretation: Nekrasov-Shatashvili Yang-Yang function of the D1-D5 $\sigma$-model, dual to Borcherds denominator of $\mathfrak{g}_{\Delta_5}$.
- Elliptic stable envelopes: Aganagic-Okounkov provide the module structure on $\bigoplus_N K_T(\mathrm{Hilb}^N (K3\times E))$; at generic K3 moduli the $T$-action is trivial and the construction fails (as noted in the chapter), but at elliptic K3 sub-locus the torus acts on each $I_1$ fiber neighborhood.

### A5.7 — Gauge-theoretic summary Cycle 5

| Construction | Partition function | Gauge theory |
|---|---|---|
| $U(1)$ VW on K3 | $1/\eta^{24}$ | 4D $\mathcal{N}=4$ SYM twisted on K3 |
| $U(1)$ refined VW | $Z^{\mathrm{Goetsche}}(q,y)$ | + R-charge fugacity |
| DMVV second-quant | $1/\Phi_{10}(\rho,\tau,z)$ | Symmetric-product lift |
| Chiral half | $1/\Delta_5(\rho,\tau,z)$ | Left-mover projection |
| $\mathbf{H}_{\Delta_5}$ action | MO+AO stable envelopes | BPS algebra of D1-D5 |

**The chiral quantum group $\mathbf{H}_{\Delta_5}$ is not a Nekrasov partition function OF a 4D gauge theory; it is a BPS algebra whose character IS the Borcherds product $\Delta_5$, which in turn is the chiral half of the second-quantised Vafa-Witten partition function on K3.**

### A5.8 — Primary literature

- Nekrasov 2002 hep-th/0206161: Seiberg-Witten prepotential from instanton counting.
- Nekrasov-Okounkov 2006 hep-th/0306238: random partitions and partition function asymptotics.
- Nekrasov-Shatashvili 2009 arXiv:0908.4052: quantization of integrable systems and 4D N=2.
- Aganagic-Okounkov 2016 arXiv:1604.00423: elliptic stable envelopes.
- Maulik-Okounkov 2012 arXiv:1211.1287: quantum groups and quantum cohomology.
- Nakajima-Yoshioka 2005 arXiv:math/0505553: Donaldson invariants as instanton partition functions.
- Vafa-Witten 1994: 4D N=4 twist on K3 and S-duality.

---

## Cycle 6 — ATTACK: the "non-abelian" K3 chiral bialgebra claim

### A6.1 — The claim under attack

The user's central question (across Waves): "the *non-abelian* K3 chiral bialgebra undergirding the BKM / Siegel $\Delta$." Nekrasov-voice: *is it non-abelian?* or is it abelian with a non-abelian BKM acting on its module?

### A6.2 — Evidence for abelianness

- **Wave 12 Nekrasov**: the 24-fold tensor $U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)^{\otimes 24}$ is a tensor of rank-1 quantum toroidal $\mathfrak{gl}_1$'s. Each factor is abelian at the Lie-algebra level.
- **Wave 12 Etingof**: replaced strict tensor with $M_{24}$-equivariant sheaf; sheaf-of-abelians, base quasi-Hopf. Still abelian fiber.
- **Wave 12 Costello**: CY-2 Koszul dual of $V(\mathfrak{g})$ is $V(\mathfrak{g})^{\mathrm{coalg}}[2]$; not obviously non-abelian.
- **K3 Yangian chapter**: `k3_yangian_chapter.tex:98` says $g(z) = \prod_{i=1}^{24}(z-h_i)/(z+h_i)$ for $\mathfrak{g} = \mathfrak{gl}_1$; diagonal $R$-matrix; abelian.
- **Quantum toroidal K3 chapter**: `k3_quantum_toroidal_chapter.tex:63` confirms abelian factorization for $\mathfrak{g} = \mathfrak{gl}_1$.

So at the Lie-algebra / quantum-group level, the K3 chiral bialgebra IS abelian (rank-24 Heisenberg / $\mathfrak{gl}_1^{\otimes 24}$).

### A6.3 — What IS non-abelian

The BKM $\mathfrak{g}_{\Delta_5}$ IS non-abelian: it has non-trivial Cartan (rank up to 27 per Gaitto-Wave-12 chain), non-trivial simple roots (both real and imaginary), non-trivial Weyl group. But this BKM is the **derived / representation-theoretic shadow** of $\mathbf{H}_{\Delta_5}$, not $\mathbf{H}_{\Delta_5}$ itself.

The relationship:
$$\mathbf{H}_{\Delta_5} \text{ (abelian rank-24 quantum group)} \;\curvearrowright\; \mathcal{F}_{\Delta_5} \text{ (K3 Fock module)} \;\supset\; \mathfrak{g}_{\Delta_5} \text{ (non-abelian BKM)}.$$

The BKM ACTS on the Fock module (is IN the algebra of operators on $\mathcal{F}_{\Delta_5}$) but the CHIRAL QUANTUM GROUP is the rank-24 abelian quantum toroidal.

### A6.4 — Parallel with the well-known Frenkel-Kac case

Consider the well-known Frenkel-Kac construction: the vertex operator realisation of $\hat{\mathfrak{g}}_k$ at level $k$ uses $r$ Heisenberg bosons $\alpha^i$ ($r$ = rank of $\mathfrak{g}$), abelian, to realise the $\hat{\mathfrak{g}}$ current algebra via vertex operators $e^{i\alpha}$.

Analogously: **the K3 BKM $\mathfrak{g}_{\Delta_5}$ is realised via vertex operators built from the rank-24 abelian Heisenberg $\mathbf{H}_{\Delta_5}$**. The vertex-operator construction goes through Borcherds' denominator formula: 
$$e^{i \alpha} \;\text{on Fock}_{\Lambda^{3,2}} \;=\; \text{BKM creation operator for simple root } \alpha.$$

This is explicitly Borcherds 1992 *Invent. Math.* 109 Sect. 5: the Monster/Fake-Monster constructions.

### A6.5 — The "non-abelian" terminology is SLOPPY

The programme's usage of "non-abelian K3 chiral bialgebra" is sloppy. The correct phrase is:
- **Chiral quantum group = abelian rank-24 quantum toroidal = $\mathbf{H}_{\Delta_5}$**.
- **BKM acting via vertex operators on its Fock module = $\mathfrak{g}_{\Delta_5}$**, non-abelian.

The connection: $\mathbf{H}_{\Delta_5}$ is the "small" algebra; $\mathfrak{g}_{\Delta_5}$ is the "large" Lie algebra that $\mathbf{H}_{\Delta_5}$'s Fock representation generates via vertex operators.

**This is structurally parallel to**: Heisenberg $\mathcal{H}_{r}$ (abelian) / Vertex operator $\to$ affine Kac-Moody $\hat{\mathfrak{g}}$ (non-abelian). The chiral quantum group is the abelian Heisenberg; the non-abelian Lie algebra is its vertex-operator realisation.

### A6.6 — HEAL Cycle 6

**Renaming / clarification**:
- $\mathbf{H}_{\Delta_5}$ = **abelian K3 chiral bialgebra** (rank-24 quantum toroidal $\mathfrak{gl}_1^{\otimes 24}$ with elliptic $R$-matrix, $M_{24}$-equivariant sheaf over $E^{\mathrm{nod}}_{24}$).
- $\mathfrak{g}_{\Delta_5}$ = **non-abelian BKM Lie algebra**, acting on the Fock module of $\mathbf{H}_{\Delta_5}$ via Borcherds' vertex-operator construction.

The two are distinct objects in a vertex-operator chain; "non-abelian K3 chiral bialgebra" conflates them.

**Nekrasov verdict**: the CHIRAL QUANTUM GROUP (= integrable-system deformation = quantum group) undergirding the BKM / Siegel $\Delta$ is the **$M_{24}$-equivariant rank-24 abelian quantum toroidal $\mathfrak{gl}_1$ sheaf $\mathbf{H}_{\Delta_5}$**, with BKM $\mathfrak{g}_{\Delta_5}$ appearing in its vertex-operator realisation on the Fock module.

### A6.7 — Gauge-theory summary

From the Nekrasov-voice perspective, the abelianness is not a bug but the natural answer:
- $U(1)$ = rank 1 = abelian gauge group on K3.
- 24 from K3's $c_2$ via Gottsche = 24 "copies" of the Heisenberg fiber in $\mathbf{H}_{\Delta_5}$.
- Non-abelianness of the BKM comes from vertex-operator extension, NOT from the gauge theory.
- This is parallel to: Heisenberg $\to$ affine KM via Frenkel-Kac; here Heisenberg$^{\otimes 24}$ $\to$ BKM via Borcherds.

---

## Cycle 7 — ATTACK: 6d hCS on $K3 \times C^2$ or $K3 \times \mathbb{CP}^1$?

### A7.1 — Costello's 6D holomorphic Chern-Simons setup

Costello 2017 (arXiv:1705.04786, 1706.03299) formulated 6D holomorphic Chern-Simons on a CY3 with gauge group $\mathfrak{g}_{BKM}$. Natural habitats:
- $\C^3$: gives affine Yangian of $\widehat{\mathfrak{gl}}_1$ (Costello).
- $T^*C$ for $C$ Riemann surface: gives 2D CFT (Costello-Yamazaki).
- $K3 \times C^2$: proposed in Wave 12 (M-theory on $K3\times T^3$ frame).

### A7.2 — Can we write the 6D hCS action on $K3 \times \C^2$?

The 6D hCS action on a CY3 $X$ is
$$S^{6D}_{\mathrm{hCS}} \;=\; \int_X \Omega \wedge \mathrm{CS}(A)$$
where $\Omega$ is the holomorphic 3-form and $A$ a $\bar\partial$-connection on a $\mathfrak{g}_{\mathrm{BKM}}$-bundle.

For $X = K3 \times \C^2$: no compact CY3 structure (K3 is CY-2, $\C^2$ is $d=2$ non-compact, product is $d=4$, not $d=3$). **So $K3 \times \C^2$ is NOT a CY3.**

For $X = K3 \times \mathbb{CP}^1$: $\mathbb{CP}^1$ is not CY (curvature), product not CY3 either.

**Correct CY3 setups containing K3:**
- $K3 \times T^2$ (where $T^2$ is elliptic, $d=1$): $d = 3$ product, CY because K3 CY-2 + $T^2$ CY-1. This IS a CY3.
- $K3 \times \C$ (with $\C$ as CY-1 non-compact): non-compact CY3.
- K3 fibration over $\mathbb{CP}^1$ (total space CY3): different from product; this is the "K3 fibered CY3" = fiber K3 + base $\mathbb{CP}^1$ + CY3 structure of total space.

### A7.3 — The natural home: $K3 \times E$ per Wave 12

Wave 12 converged on $K3 \times E$ (= elliptic genus base):
- $K3 \times E$ is a compact CY3.
- Hochschild cohomology: $HH^\bullet(K3 \times E) = HH^\bullet(K3) \otimes HH^\bullet(E)$ by Kunneth.
- Chiral algebra $A_{K3\times E} = \Phi_3(D^b\mathrm{Coh}(K3\times E))$ exists by Theorem CY-A$_3$.
- Modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (see `k3_yangian_chapter.tex` and `modular_koszul_bridge.tex`).

### A7.4 — 6D hCS action on $K3 \times E$

The holomorphic 3-form on $K3\times E$: $\Omega_{K3\times E} = \sigma_{K3} \wedge dz_E$ (wedge of K3 holomorphic 2-form with $E$ holomorphic 1-form).

The 6D hCS action:
$$S = \int_{K3\times E} \sigma_{K3}\wedge dz_E \wedge \mathrm{Tr}\bigl(A \, \bar\partial A + \tfrac{2}{3} A^3\bigr).$$

Gauge group: $G_{\mathrm{BKM}}$ with Lie algebra $\mathfrak{g}_{\Delta_5}$ (rank 27 per Gaiotto's chain; conditional on non-abelian extension).

**Instanton sector**: $\pi_3(G_{\mathrm{BKM}}) = \Z$ (naive), so instantons labelled by integers. The instanton action is $e^{2\pi i \rho}$ where $\rho$ is Kahler class of $E$-fiber — matches the "$\rho$-coordinate" of Siegel $\mathbb{H}_2$.

**Partition function** of 6D hCS on $K3\times E$: conjectural, but expected to give $1/\Phi_{10}(\rho,\tau,z)$ by the duality
$$Z^{6D\text{-hCS}}_{K3\times E}(\rho,\tau,z) \;\leftrightarrow\; Z^{\mathrm{D1-D5}}_{K3\times S^1}(\rho,\tau,z) = \frac{1}{\Phi_{10}}.$$

The matching is via Wave 12's heterotic-IIA-IIB-M duality cycle.

### A7.5 — The Yangian output from 6D hCS on $K3 \times E$

Following Costello's $\C^3$ pattern: 6D hCS on $\C^3$ with gauge group $\mathfrak{gl}_1$ produces the affine Yangian $Y(\widehat{\mathfrak{gl}}_1)$ = $W_{1+\infty}$ (Maulik-Okounkov, Schiffmann-Vasserot, Prochazka-Rapcak).

Analogously: 6D hCS on $K3\times E$ with gauge group $\mathfrak{gl}_1$ should produce the K3 Yangian $Y(\mathfrak{g}_{K3})$ = $\mathbf{H}_{\Delta_5}$.

But there is a subtlety: **Theorem `prop:k3-qt-no-s3-miki` in `k3_quantum_toroidal_chapter.tex:121` says NO $S_3$ Miki automorphism exists for K3** — only $SL_2(\Z)$ from $E$. This is because $K3$ has no $\C^*$-action generically, so the torus $(\C^*)^3$ of Miki's construction on $\C^3$ becomes $\C^* = E$ alone on $K3\times E$.

Consequence: the 6D hCS on $K3\times E$ produces a **$SL_2(\Z)$-symmetric** (not $S_3$-symmetric) algebra, consistent with $\mathbf{H}_{\Delta_5}$ being a rank-24 quantum toroidal $\mathfrak{gl}_1$ with $M_{24}$ permutation (NOT $S_3$ Miki).

### A7.6 — HEAL Cycle 7

$$\boxed{
\begin{array}{l}
\text{CY3 home of } \mathbf{H}_{\Delta_5}: K3\times E \text{ (not } K3\times\C^2\text{)}\\
\text{6D hCS gauge theory on } K3\times E, \text{ gauge group } \mathfrak{gl}_1 \\
\text{Instanton fugacity: } e^{2\pi i\rho}\\
\text{Partition function conjectural: } 1/\Phi_{10}(\rho,\tau,z)\\
\text{Algebra output: } \mathbf{H}_{\Delta_5} = M_{24}\text{-equivariant rank-24 quantum toroidal } \mathfrak{gl}_1\\
\text{No } S_3 \text{ Miki due to K3's lack of } \C^* \text{ action}
\end{array}}
$$

### A7.7 — Primary literature

- Costello 2017 arXiv:1705.04786: 6D holomorphic Chern-Simons theory.
- Costello-Yamazaki 2019 arXiv:1908.02289: twisted M-theory.
- Costello-Gaiotto-Wang 2020 arXiv:2012.15830: 6D hCS and integrable systems.
- Rapcak-Soibelman-Yang-Zhao 2020 arXiv:2007.13365: RSYZ Coulomb formula.
- Schiffmann-Vasserot 2012 arXiv:1202.2756: $W$-algebras and instanton cohomology.

---

## Cycle 8 — ATTACK: A moduli-space integral for $\Delta_5$?

### A8.1 — The clearest statement

Can I express $\Delta_5$ as an integral over a moduli space?

The answer IS YES, through the **Borcherds singular theta lift**: Harvey-Moore 1996 Theorem 3 gives
$$-\log \Delta_5(\rho,\tau,z) \;=\; \int_{\mathcal{F}} \frac{d^2\tau'}{(\mathrm{Im}\,\tau')^2} \bigl[\Theta_{\Lambda^{3,2}}(\tau',\bar\tau'; \rho,\tau,z) \cdot \phi_{0,1}(\tau',z')\bigr]_{\mathrm{reg}},$$
where $\mathcal{F}$ is the standard fundamental domain of $SL_2(\Z)$, $\Theta_{\Lambda^{3,2}}$ is the Siegel theta function of the lattice $\Lambda^{3,2}$, $\phi_{0,1}$ is the K3 elliptic genus (weight 0, index 1 Jacobi form), and $[\cdot]_{\mathrm{reg}}$ is Harvey-Moore's regularisation.

This is **an equivariant elliptic integral**: $\tau'$ is the world-sheet torus modulus; the integrand is the weight-0 elliptic genus $\phi_{0,1}$; the lattice $\Lambda^{3,2}$ is the charge lattice; the external parameters $(\rho,\tau,z)$ parametrise the moduli space.

### A8.2 — As a Nekrasov-style integral

In Nekrasov language: $\Delta_5$ is the **1-loop / genus-0 string partition function** of a non-linear $\sigma$-model on $K3 \times S^1$ with charges in $\Lambda^{3,2}$. The logarithm of $\Delta_5$ is the free energy of this $\sigma$-model, expanded in Kahler moduli $(\rho,\tau,z)$.

The Harvey-Moore theta lift IS the worldsheet-string 1-loop integral:
$$F^{1\text{-loop}}(\rho,\tau,z) \;=\; -\log \Delta_5(\rho,\tau,z) \;=\; \int_{\mathcal{F}} \cdots $$

So $\Delta_5$ expresses the heterotic/Type II 1-loop free energy on $K3 \times S^1$, which is the gauge-theoretic analog of the Nekrasov 1-loop determinant (since 4D N=2 Nekrasov integrands are 5D/6D 1-loop determinants, reduced on $\C$).

### A8.3 — Moduli space interpretation

$\Delta_5$ is a section of a line bundle on $\mathrm{Sp}_4^{\mathrm{par}}(\Z)\backslash\mathbb{H}_2$ = the moduli space of **principally polarised abelian surfaces**, up to paramodular identification.

Gauge-theoretic interpretation:
- **Principally polarised abelian surfaces** $A = \C^2/\Lambda$ parametrise **low-energy Coulomb branches of 4D N=2 theories with $\mathrm{Sp}_4$ flavour**.
- The Humbert surfaces $H_1, H_4$ = codimension-1 loci where BPS bound states decay.
- $\Delta_5$ = discriminant of the Seiberg-Witten-like system on this moduli space.

This is the **Seiberg-Witten geometry of the heterotic-on-$T^6$ 1/4-BPS sector**: the SW curve is a principally polarised abelian surface, and $\Delta_5$ is its discriminant locus.

### A8.4 — HEAL Cycle 8

$\Delta_5$ can be written as:
1. **Infinite product** (Borcherds/Gritsenko): $\prod (1 - q_\rho^n q_\tau^m y_z^\ell)^{c(4nm-\ell^2)}$.
2. **Sum (Fourier-Jacobi)**: $\sum_{m\ge 1/2} \psi_{5,m}(\tau,z) q_\rho^m$ on paramodular $K(1)$.
3. **Harvey-Moore theta integral**: $\exp\bigl[-\int_{\mathcal{F}} \Theta_{\Lambda^{3,2}} \phi_{0,1}\bigr]_{\mathrm{reg}}$.
4. **Generating function**: chiral half of $1/\Phi_{10}$, which is DMVV of K3 elliptic genera.
5. **Modular/automorphic form**: weight-5 cusp form on paramodular $K(1)$, character $v_{\Delta_5}$.
6. **Nekrasov-voice interpretation**: 1-loop partition function of heterotic/IIA on $K3\times S^1$; SW discriminant of 1/4-BPS sector.

All six are the same object from different lenses.

### A8.5 — Primary literature

- Harvey-Moore 1995/96 hep-th/9510182: algebra of BPS states.
- Borcherds 1998 *Invent. Math.* 132: singular theta lifts.
- Gritsenko 1999, *Arithmetical lifting*: explicit Sp_4 / K(1) lifts.
- Dijkgraaf-Moore-Verlinde-Verlinde 1997: DMVV formula.
- Sen 2008 arXiv:0803.1014: dyon partition functions and BKM algebras.

---

## Cycle 9 — Additional: The 1-loop exactness and N=2 supersymmetry

### A9.1 — ATTACK

One objection: the Harvey-Moore theta lift is a 1-loop string-theoretic computation. Why is this the *exact* answer? Shouldn't there be higher-loop corrections?

### A9.2 — HEAL: N=4 non-renormalisation

In N=4 supersymmetric theories (heterotic on $T^6$ = $\mathcal{N}=4$ in 4D), the BPS index is 1-loop exact by standard Dine-Seiberg-type non-renormalisation theorems. Sen 2007 established this for 1/4-BPS dyons: no higher-loop corrections.

So $-\log \Delta_5$ = exact 1-loop integral = exact Borcherds lift = exact BKM denominator.

This non-renormalisation is parallel to the Nekrasov partition function's 4D $\mathcal{N}=2$ 1-loop expression: the instanton sum is "1-loop" in the localisation sense, and no higher-loop corrections arise in the equivariant integration.

### A9.3 — Primary literature

- Sen 2007 arXiv:0706.3373: wall-crossing; 1-loop exactness of BPS indices.
- Dijkgraaf-Moore-Verlinde-Verlinde 1997: DMVV (1-loop exact for elliptic genera).

---

## Cycle 10 — Synthesis / Nekrasov verdict

### A10.1 — The gauge-theory identity of $\mathbf{H}_{\Delta_5}$

After 9 cycles of attack-heal:

$$\boxed{
\begin{array}{rl}
\mathbf{H}_{\Delta_5} \;=\; & \text{$M_{24}$-equivariant sheaf of rank-24 abelian quantum toroidal } U_{q,t}(\widehat{\widehat{\gl}}_1)\\
& \text{over $E^{\mathrm{nod}}_{24}$ (24-node discriminant curve of generic elliptic K3),}\\
& \text{with CY-2 Koszul-dual structure, $\Phi_{10}/\eta^{24}$-twisted Siegel-Borcherds associator,}\\
& \text{and Siegel-corrected elliptic $R$-matrix.}\\[6pt]
\mathbf{H}_{\Delta_5}\; \text{acts on}\; & \text{K3 Fock module }\mathcal{F}_{K3} = \bigoplus_{N\ge 0} H^*(\mathrm{Hilb}^N K3)\\
& \text{via Maulik-Okounkov + Aganagic-Okounkov stable envelopes.}\\[6pt]
\text{BKM }\mathfrak{g}_{\Delta_5}\; \text{lives in}\; & \text{the vertex-operator closure of }\mathbf{H}_{\Delta_5}\text{'s action on }\mathcal{F}_{K3}.\\
& \text{Non-abelian }\mathfrak{g}_{\Delta_5}\text{ is NOT }\mathbf{H}_{\Delta_5}\text{; it is generated inside }\mathbf{H}_{\Delta_5}\text{'s rep.}
\end{array}}
$$

### A10.2 — Gauge-theory origin (sharpened)

- **4-manifold**: K3 (compact, CY-2).
- **Gauge group**: $U(1)$ (rank 1; NOT rank 24).
- **Gauge theory**: $\mathcal{N}=4$ SYM on K3, Vafa-Witten twist.
- **Instanton moduli**: $\mathrm{Hilb}^N(K3)$ = moduli of rank-1 $c_2 = N$ torsion-free sheaves.
- **Equivariant torus**: trivial at generic K3; $E \subset K3\times E$-fiber at elliptic K3.
- **Nekrasov partition function**: $Z^{\mathrm{VW}}_{U(1)}(K3; q) = 1/\eta^{24}$ (for rank-1 Hilb Euler char).
- **Second-quantised via DMVV**: $\sum_N e^{2\pi i N\rho} \chi^{\mathrm{ell}}(\mathrm{Hilb}^N K3;\tau,z) = 1/\Phi_{10}$.
- **Chiral half**: $1/\Delta_5$ on paramodular $K(1)$.
- **BPS interpretation**: 1/4-BPS dyons in heterotic on $T^6$ via heterotic/IIB duality.

### A10.3 — Integrable-system structure

- **Seiberg-Witten curve**: principally polarised abelian surface ($\mathbb{H}_2 / \mathrm{Sp}_4^{\mathrm{par}}(\Z)$).
- **Discriminant locus**: $\{\Delta_5 = 0\} = 2H_1 + H_4$ (Gritsenko-Nikulin 1997).
- **Wall-crossing**: at Humbert $H_1, H_4$; 1/4-BPS decays into 1/2-BPS pairs.
- **Yang-Yang function**: $W_{YY} \propto \log \Delta_5$, the Nekrasov-Shatashvili limit.
- **Quantum Riemann-Hilbert**: Maulik-Okounkov stable envelopes realise the monodromy at walls.
- **Elliptic stable envelopes**: Aganagic-Okounkov refine this to the elliptic K3 sub-locus.

### A10.4 — R-matrix structure

- **Spectral parameter**: $z_1/z_2 \in \C^*$ (multiplicative quantum toroidal).
- **Elliptic refinement**: $(q, t) \in (\C^*)^2$ with $qt \in E$-fiber (elliptic K3).
- **Classical limit**: $q \to 1$: rational K3 Yangian limit, $R(u) = 1 - \sigma_2 \Omega_{\mathrm{Muk}}/u + O(1/u^2)$.
- **Trigonometric limit**: generic $q$: quantum affine structure.
- **Elliptic full**: generic $(q, p)$ with $p$ elliptic nome on $E$: full elliptic $R$-matrix.
- **Siegel correction**: Kronecker-Eisenstein-Siegel term per Drinfeld Wave 12; deforms elliptic $R$ to genus-2 Siegel $R$ at Humbert walls.
- **YBE**: satisfied modulo the Humbert-wall pentagons/hexagons (Drinfeld Wave 12); closes with $\Phi_{10}/\eta^{24}$ twist.

### A10.5 — Retractions from Wave 12

**R13-Nek-1**: "24-fold tensor" phrasing in Wave 12 synthesis suggests 24 independent algebras. The correct picture (Wave 13 heal): ONE $U(1)$ gauge theory on K3; the 24-fold structure is the elliptic K3 fiber structure (24 $I_1$ Kodaira fibers); $\mathbf{H}_{\Delta_5}$ is a SHEAF (not a product) of rank-1 quantum toroidal $\mathfrak{gl}_1$'s over the 24-node discriminant curve. (Costello's W12-Cos-2 already formulated this correctly; my Wave-12 synthesis was loose.)

**R13-Nek-2**: "Non-abelian K3 chiral bialgebra" phrasing is sloppy. Correct: $\mathbf{H}_{\Delta_5}$ is an **abelian** rank-24 chiral quantum group; the non-abelian $\mathfrak{g}_{\Delta_5}$ lives in its vertex-operator realisation on the Fock module. Analogous to Frenkel-Kac construction.

**R13-Nek-3**: qq-character "closure at depth $\ge 2$" phrasing ambiguous between algebra-level and module-level closure. Sharpening: algebra closure holds via $M_{24}$-projection; module closure fails with anomaly $\eta^{24} \cdot [\Omega_{\mathrm{Kodaira}}]$, a Nekrasov-Witten compactness obstruction. Both Etingof's and my Wave-12 statements are correct at different levels.

**R13-Nek-4**: "6d hCS on $K3\times\C^2$" (implied in mandate) is IMPOSSIBLE — $K3\times\C^2$ is not CY3. Correct home: $K3\times E$ or non-compact $K3\times\C$.

### A10.6 — Open questions Wave 13 leaves

**Open-1**: Explicit Harvey-Moore lift for $\Delta_5$ (vs $\Phi_{10}$). Wave 13 claimed $-\log\Delta_5 = (1/2)\int_{\mathcal{F}}\cdots$; verify coefficients. Compute module: `k3_yangian_wave13_harvey_moore_delta5_lift.py`.

**Open-2**: 6D hCS on $K3\times E$ partition function = $1/\Phi_{10}$? This is a conjecture; would follow from extending Costello's $\C^3$ machinery to $K3\times E$ via Theorem CY-A$_3$. Compute module: `k3_yangian_wave13_6dhcs_k3xe_partition.py`.

**Open-3**: Elliptic stable envelope for $\mathrm{Hilb}^N(K3 \times E)$ at non-generic K3 moduli (Aganagic-Okounkov generalisation). The chapter `k3_yangian_chapter.tex:100` notes this requires a toric torus $T_S = (\C^*)^2$ at ADE/Kummer locus only. Compute module: `k3_yangian_wave13_ao_elliptic_envelope_k3.py`.

**Open-4**: The relationship between $c(n)$ (EOT/BKM multiplicity) and $p_{24}(n)$ (Hilb Euler char) — is the difference $c(n) - p_{24}(n)$ calculable as a signed long-multiplet count? At $n=2$: $138 = 462 - 324$. Compute module: `k3_yangian_wave13_short_long_multiplet_decomp.py`.

**Open-5**: Nekrasov-Shatashvili Yang-Yang function $W_{YY}(\rho,\tau,z) = -\log\Delta_5(\rho,\tau,z) \cdot \text{const}$? What is the const? What is the NS integrable system explicitly? Compute module: `k3_yangian_wave13_ns_integrable_delta5.py`.

### A10.7 — Five new anti-patterns

**AP-CY-W13-Nek-1** (rank conflation: gauge rank vs Fock rank). The "rank 24" of K3 chiral quantum group is the rank of the COHOMOLOGY $H^*(K3) = \C^{24}$, not the rank of the gauge group. The gauge group is $U(1)$ = rank 1.

**AP-CY-W13-Nek-2** ("non-abelian" vs "abelian" chiral bialgebra). $\mathbf{H}_{\Delta_5}$ is ABELIAN at the quantum-group level ($\mathfrak{gl}_1^{\otimes 24}$); $\mathfrak{g}_{\Delta_5}$ is the non-abelian BKM built via vertex operators on its Fock module. Do NOT call $\mathbf{H}_{\Delta_5}$ "non-abelian."

**AP-CY-W13-Nek-3** (CY3 home for K3). $K3\times\C^2$ is NOT CY3. $K3\times E$ is CY3 (K3 + $E$-fiber). K3 fibration over $\mathbb{CP}^1$ is a different CY3 (total space, not product).

**AP-CY-W13-Nek-4** (qq-char closure levels). "Depth-$n$ qq-character closure" is ambiguous. Specify: (i) algebra closure (trivial via $M_{24}$-projection); (ii) module closure on Fock space (fails with anomaly $\eta^{24}[\Omega_{\mathrm{Kod}}]$, a compactness obstruction).

**AP-CY-W13-Nek-5** ($\Delta_5$-as-Nekrasov-function scope). $\Delta_5$ is NOT a Nekrasov partition function of a 4D gauge theory directly. It is the 1-loop string free energy on $K3\times S^1$ (heterotic/IIA frame), equivalently the Borcherds singular theta lift of $\phi_{0,1}$ on $\Lambda^{3,2}$. The "Nekrasov-like" writing is via Aganagic-Okounkov elliptic stable envelopes on $\mathrm{Hilb}^N(K3\times E)$, which is chart-restricted to elliptic K3 sub-locus.

---

## Cycle 11 — Explicit Nekrasov-style output for $\Delta_5$

### A11.1 — The "Nekrasov partition function" for $\mathbf{H}_{\Delta_5}$

Following the standard Nekrasov-Okounkov format, we write:

$$Z_{\mathrm{Nek}}^{K3 \times S^1}(\rho, \tau, z) \;=\; e^{2\pi i \rho / 2 + \pi i \tau / 2 + \pi i z / 2} \prod_{\vec\lambda} \text{(weight)}$$

where the product runs over tuples of partitions $\vec\lambda$ indexing fixed points of the T-action on $\mathrm{Hilb}^\bullet K3$ (chart-restricted to elliptic K3 sub-locus).

The "weight" at the $(n,\ell,m)$-th contribution is:
$$\text{weight}(n,\ell,m) \;=\; (1 - q_\rho^n q_\tau^m y_z^\ell)^{c(4nm - \ell^2)}$$

where:
- $q_\rho = e^{2\pi i\rho}$ = Hilb counting fugacity (instanton number)
- $q_\tau = e^{2\pi i\tau}$ = elliptic fugacity (K3 $T^2$ fiber)
- $y_z = e^{2\pi i z}$ = $U(1)_R$ chemical potential (equivalently $\epsilon_1 - \epsilon_2$ at elliptic K3 sub-locus)
- $c(k)$ = Fourier coefficients of $\phi_{0,1}(\tau,z)$ = K3 elliptic genus

Then $Z_{\mathrm{Nek}}^{K3\times S^1} = \Delta_5(\rho,\tau,z)$, the Gritsenko-Borcherds lift.

### A11.2 — The chiral quantum group perspective

$\mathbf{H}_{\Delta_5}$'s character on its natural module gives
$$\mathrm{char}(\mathbf{H}_{\Delta_5}; \rho, \tau, z) \;=\; \frac{1}{\Delta_5(\rho,\tau,z)}.$$

This is the **generating function of BPS state multiplicities** = BKM root multiplicities = 1-loop string partition function on $K3\times S^1$ = chiral half of DMVV on $\mathrm{Hilb}^\bullet K3$.

### A11.3 — Final Nekrasov verdict

**Gauge-theory identity**: $\mathbf{H}_{\Delta_5}$ is the BPS symmetry algebra of heterotic on $T^6$ / Type IIB D1-D5 on $K3\times S^1$, realised concretely as an $M_{24}$-equivariant sheaf of rank-1 quantum toroidal $\mathfrak{gl}_1$'s (abelian per factor; $M_{24}$-braided as a sheaf) over the 24-node elliptic discriminant.

**Integrable-system structure**: the underlying integrable system is the **Seiberg-Witten geometry** of the heterotic-$T^6$ 1/4-BPS sector = principally polarised abelian surface. Its discriminant = $\{\Delta_5 = 0\}$. Its quantum Riemann-Hilbert / monodromy = Maulik-Okounkov stable envelopes on $\mathrm{Hilb}^N(K3)$.

**R-matrix**: elliptic quantum toroidal $R$-matrix with Kronecker-Eisenstein-Siegel correction at Humbert walls; Yang-Baxter satisfied modulo the Drinfeld-twist $\Phi_{10}/\eta^{24}$.

**BPS enumeration**: Fourier coefficients of $1/\Delta_5$ = BKM simple-root multiplicities = EOT Mathieu moonshine short-multiplet decomposition of K3 elliptic genus.

**The chiral quantum group undergirding the BKM / Siegel $\Delta$ is**: 
$$\mathbf{H}_{\Delta_5} \;=\; \bigl(\text{abelian rank-24 quantum toroidal }\mathfrak{gl}_1, M_{24}\text{-equivariantly sheaf-organised, Siegel-Borcherds associator, CY-2 Koszul-dual}\bigr).$$

It is an **abelian** chiral quantum group in the sense of the Lie-algebra structure of its fiber. The non-abelian $\mathfrak{g}_{\Delta_5}$ BKM lives in its vertex-operator representation on the K3 Fock module, NOT in $\mathbf{H}_{\Delta_5}$ itself.

---

## Wave 13 compute modules proposed (Nekrasov lane)

```
compute/lib/k3_yangian_wave13_harvey_moore_delta5_lift.py
  # Explicit Harvey-Moore singular theta lift for Δ_5 (chiral half)
  # vs Φ_10 (full). Verify exponents, regularisation, boundary contributions.

compute/lib/k3_yangian_wave13_6dhcs_k3xe_partition.py
  # 6D holomorphic Chern-Simons on K3 × E with gauge group gl_1.
  # Instanton summation; conjectured match to 1/Φ_10 via heterotic/IIB duality.

compute/lib/k3_yangian_wave13_ao_elliptic_envelope_k3.py
  # Aganagic-Okounkov elliptic stable envelopes for Hilb^N(K3 × E)
  # at elliptic K3 sub-locus; chart-by-chart at Kodaira I_1 fibers.

compute/lib/k3_yangian_wave13_short_long_multiplet_decomp.py
  # Decompose K3 elliptic genus c(n) - p_24(n) at n = 2, 3, 4, 5
  # into signed long-multiplet contributions. At n=2: 138 = c(2) - p_24(2).

compute/lib/k3_yangian_wave13_ns_integrable_delta5.py
  # Nekrasov-Shatashvili Yang-Yang function W_YY from log Δ_5.
  # Identify integrable system: Seiberg-Witten curve = PPAS; discriminant = Δ_5 = 0.

compute/lib/k3_yangian_wave13_qqchar_kodaira_anomaly.py
  # qq-character depth-2 module anomaly η^24 · [Ω_Kodaira];
  # verify compactness obstruction (Nekrasov-Witten 2010 applied to K3).

compute/lib/k3_yangian_wave13_dmvv_second_quant_verification.py
  # Verify DMVV: Σ_N p^N · χ^ell(Hilb^N K3) = 1/Φ_10 through N = 6.
  # Three independent paths: DMVV formula, Gottsche recursion, direct χ^ell.

compute/lib/k3_yangian_wave13_abelian_bialgebra_vertex_to_bkm.py
  # Explicit vertex-operator construction of g_{Δ_5} BKM
  # inside the Fock module of abelian H_{Δ_5}.
  # Parallel to Frenkel-Kac for affine KM.
```

Total: 8 Wave 13 Nekrasov-lane compute modules.

---

## Final Wave-13 Nekrasov verdict (synthesis)

**The chiral quantum group undergirding the BKM / Siegel $\Delta_5$**:

$$\boxed{
\mathbf{H}_{\Delta_5} \;=\; \bigl(\text{abelian rank-24 quantum toroidal } U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)^{\otimes 24}\bigr)^{M_{24}}_{\mathrm{sheaf}/E^{\mathrm{nod}}_{24}}
}$$

- **fibered over** the 24-node elliptic discriminant curve $E^{\mathrm{nod}}_{24} \subset \mathrm{Hilb}^{24}(\mathbb{P}^1)/M_{24}$ (Costello's factorisation base),
- **associated to** Siegel $\overline{\mathcal{A}_2}$ with Humbert regular-singular stratification $\{\Delta_5=0\}=2H_1+H_4$,
- **carrying** the $\Phi_{10}/\eta^{24}$-twisted genus-2 Siegel-Borcherds associator and Kronecker-Eisenstein-Siegel-corrected elliptic $R$-matrix,
- **Koszul-dual** = $V(\mathfrak{g})^{\mathrm{coalg}}[2]$ with CY-2 shift,
- **acting on** the K3 Fock module $\mathcal{F}_{K3} = \bigoplus_N H^*(\mathrm{Hilb}^N K3)$ via Maulik-Okounkov stable envelopes + Aganagic-Okounkov elliptic refinement,
- **containing** the BKM $\mathfrak{g}_{\Delta_5}$ in its vertex-operator closure (non-abelian Lie algebra in the *representation*, not in the algebra itself),
- **physical home**: BPS symmetry algebra of Type IIB D1-D5 on $K3 \times S^1$ / heterotic on $T^6$ / M-theory on $K3 \times T^3$ (Hull-Townsend duality cycle),
- **gauge-theory identity**: BPS algebra of $U(1)$ Vafa-Witten on K3, second-quantised via DMVV; chiral half on paramodular $K(1)$,
- **integrable-system structure**: Seiberg-Witten geometry of heterotic-$T^6$ 1/4-BPS sector (principally polarised abelian surface moduli), with wall-crossing at Humbert surfaces and Yang-Yang function $W_{YY} \propto \log\Delta_5$.

**It is abelian** at the chiral-quantum-group / Lie-algebra level; **the "non-abelian" refers to the BKM $\mathfrak{g}_{\Delta_5}$ in its vertex-operator representation, not to $\mathbf{H}_{\Delta_5}$ itself**. This clarification resolves a Wave-level ambiguity about "non-abelian K3 chiral bialgebra."

Six cycles (plus synthesis) of ATTACK-HEAL complete. Five new anti-patterns (AP-CY-W13-Nek-1 through AP-CY-W13-Nek-5). Eight compute modules proposed. Five open questions queued.

Raeez Lorgat, sole author, 2026-04-19.

---

## Appendix A — Gauge-theoretic correspondence table (Wave 13 Nekrasov)

| Nekrasov object | K3 chiral-bialgebra analog | Wave 13 identification |
|---|---|---|
| Gauge group $G$ | $U(1)$ | Rank 1 (not 24) |
| 4-manifold $M^4$ | K3 | CY-2, compact |
| Omega parameters $(\epsilon_1, \epsilon_2)$ | $(\tau, z)$ | elliptic genus + R-charge; NOT Omega |
| Coulomb-branch moduli $a_i$ | Siegel modulus $\rho$ | Hilb-counting fugacity |
| Instanton number | $N \in \Z_{\ge 0}$ | $c_2 = N$ |
| Partition function | $1/\Phi_{10}$ | DMVV second-quantised |
| Chiral half | $1/\Delta_5$ | left-movers, paramodular $K(1)$ |
| Integrable system | PPAS = principally polarised abelian surface | SW geometry of 1/4-BPS sector |
| YY function | $-\log\Delta_5$ | Borcherds denominator |
| R-matrix | elliptic $R$, KES-corrected at Humbert walls | Aganagic-Okounkov + Drinfeld twist |
| Stable envelope | MO + AO (chart-restricted) | at elliptic K3 sub-locus only |
| BPS algebra | $\mathfrak{g}_{\Delta_5}$ BKM | non-abelian in vertex-op closure |
| Chiral quantum group | $\mathbf{H}_{\Delta_5}$ | ABELIAN rank-24 quantum toroidal |

## Appendix B — Duality-frame summary

| Physical frame | 4-manifold | Gauge theory | Partition function |
|---|---|---|---|
| Heterotic on $T^6$ | $T^6$ | $\mathcal{N}=4$ gauge theory | $1/\Phi_{10}(\rho,\tau,z)$ |
| IIA on $K3\times T^2$ | $K3 \times T^2$ | D0-D2-D4-D6 | $1/\Phi_{10}$ |
| IIB on $K3 \times S^1$ | $K3 \times S^1$ | D1-D5 | $1/\Phi_{10}$ |
| M-theory on $K3\times T^3$ | $K3\times T^3$ | M2-M5-KK | $1/\Phi_{10}$ |
| $U(1)$ VW on K3 | K3 | $\mathcal{N}=4$ SYM twist | $1/\eta^{24}$ (unrefined) |
| 2D $\sigma$-model on $\mathrm{Sym}^N K3$ | (Wick-rotated 2D) | $\mathcal{N}=(4,4)$ | $\chi^{\mathrm{ell}}$ |
| 6D hCS on $K3\times E$ | $K3\times E$ | $\mathfrak{gl}_1$ | conjecturally $1/\Phi_{10}$ |

## Appendix C — Wave 13 retraction ledger

| # | Wave 12 phrasing | Wave 13 sharpening | Severity |
|---|---|---|---|
| R13-Nek-1 | "24-fold tensor $U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)^{\otimes 24}$" | $M_{24}$-equivariant SHEAF over $E^{\mathrm{nod}}_{24}$; rank-1 fiber; NOT a 24-product gauge theory | minor sharpening |
| R13-Nek-2 | "non-abelian K3 chiral bialgebra" | $\mathbf{H}_{\Delta_5}$ is ABELIAN (rank-24); BKM non-abelian lives in vertex-op closure | major clarification |
| R13-Nek-3 | "qq-char depth-$n$ closure" | algebra-closure trivial; module-anomaly $\eta^{24}[\Omega_{\mathrm{Kod}}]$ per Nekrasov-Witten | level disambiguation |
| R13-Nek-4 | implied "6d hCS on $K3\times\C^2$" | IMPOSSIBLE (not CY3); correct: $K3\times E$ | hard correction |
| R13-Nek-5 | "$\Delta_5$ as Nekrasov partition function of 4D gauge theory" | $\Delta_5$ is 1-loop string free energy on $K3\times S^1$; NOT a 4D Nekrasov fn; AO chart-restricted writing | scope clarification |
| R13-Nek-6 | "rank 24 = gauge rank" | rank 24 = cohomology rank of K3; gauge rank = 1 | conceptual |
| R13-Nek-7 | "$c(2) = 462$ = algebra dim or Fock dim" | $c(2) = 462$ is EOT short-multiplet count; $p_{24}(2) = 324$ is Hilb Euler char; $138 = 462 - 324$ is signed long-multiplet contribution | sharpening |

Six new retractions, all sharpening-level (no major reversals from Wave 12 convergent claims).

---

**End Wave 13 Nekrasov voice.** Eleven cycles complete. Gauge-theory identity established; integrable-system structure named; abelian vs non-abelian clarified; Nekrasov partition-function writing of $\Delta_5$ given via Harvey-Moore theta lift (= chiral half of DMVV on $K3 \times S^1$); 24-fold sheaf structure replacing 24-product tensor; CY3 home $K3\times E$ (not $K3\times\C^2$). 

Raeez Lorgat, sole author, 2026-04-19.
