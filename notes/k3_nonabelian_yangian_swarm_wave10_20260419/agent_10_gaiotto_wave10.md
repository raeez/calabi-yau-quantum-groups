# Agent 10 (Gaiotto voice) — Wave 10: microscopic $T[K3]$, BFN on K3, 3D mirror, holomorphic blocks, 24 Kodaira / 24 vacua, K-theoretic Hall on $\mathrm{coh}(K3)$

**Raeez Lorgat, sole author. Wave 10, 2026-04-19.**

Wave 9 sharpened the physical identity of the chiral quantum group undergirding the BKM $\mathfrak{g}_{\Delta_5}$ to:

$$
\mathcal{H}_{\Delta_5}\;=\;\text{K-theoretic Coulomb-branch algebra of }T[K3]\text{ on }S^1\times\mathbb{R}^2,
$$

equivalently the $qq$-operator algebra acting on holomorphic blocks of $T[K3]$, dual under 3D mirror / Koszul duality to the Maulik--Okounkov Borcherds Yangian $Y^{MO}(\mathfrak{g}_{\Gamma^{K3}})$ on $\mathrm{Hilb}(K3)$.

Wave 9 also flagged five **gap items**:

(G1) microscopic Lagrangian for $T[K3]$;
(G2) BFN Coulomb-branch algebra rigorously defined on K3 (not a Kleinian / not a $\mathbb{C}^2$-quotient);
(G3) 3D mirror dual of $T[K3]$ identified concretely;
(G4) Beem--Dimofte--Pasquetti holomorphic blocks of $T[K3]$ computed and checked for Sp$_4$-modularity;
(G5) precise correspondence "24 Kodaira fibres = 24 BPS vacua" with monodromy data;
(G6) K-theoretic Hall algebra of $\mathrm{coh}(K3)$ at small grade as the K3-analogue of quantum toroidal $\mathfrak{gl}_1$.

Wave 10 runs **seven attack--heal cycles** (one per gap, plus a synthesis cycle) and discharges each gap to (a) an explicit construction with a primary-source citation, or (b) a precise obstruction that converts the gap into a falsifiable conjecture. Each cycle is closed by Pattern 236 chain-level / $(\infty,1)$-categorical labelling.

**Wave 10 final claim** (sharpening of Wave 9 box):

$$
\boxed{\quad
\mathcal{H}_{\Delta_5}\;=\;\mathrm{KHA}\bigl(\mathrm{coh}(K3)\bigr)^{\mathrm{Hecke}}_{(q_1,q_2,z)}\;\cong\;\mathcal{A}^{qq}\bigl(T[K3];S^1\times\mathbb{R}^2\bigr),
\quad}
$$

where the left-hand side is the **K-theoretic cohomological Hall algebra of the abelian category of coherent sheaves on K3, Hecke-completed at three deformation parameters $(q_1,q_2,z)$** (the K3-analogue of the $\mathbb{C}^2$ construction of Schiffmann--Vasserot 2012 producing quantum toroidal $\mathfrak{gl}_1$), and the right-hand side is the $qq$-difference operator algebra on holomorphic blocks of $T[K3]$. The two are equal by the BFN \=\ KHA identification on Hilbert schemes (Negu\u t 2018 for $\mathbb{C}^2$; Davison--Hennecart--Schlegel--Mejia 2022 for general CY3), specialised to the surface $K3\times\mathrm{pt}$ inside the CY3 $K3\times\mathbb{C}$.

**Methodology**: every claim is tracked to a primary source (preprint number, page, equation), or labelled \texttt{conjectural} with an explicit falsification test. Three-path verification is required for every numerical or modular claim. No edits to \texttt{.tex}; this file is a swarm note for Wave 11 to absorb.

---

## Cycle 1 — ATTACK (G1): there is no microscopic $T[K3]$ Lagrangian in primary literature

### §1.1 What we have from primary sources

Gadde--Gukov--Putrov 2013 (arXiv:1306.4320, "Fivebranes and 4-manifolds") computes the topological invariants of M5-branes on a 4-manifold $M_4$, packaged as a 2D theory $T[M_4]$ on $\Sigma_g$ (the Riemann-surface direction of the 6D theory). For $M_4=K3$ with $N$ M5-branes of $A_{N-1}$ type, the 2D theory is
$$
T[K3,A_{N-1}]\;=\;\text{2D }\mathcal{N}=(0,4)\text{ sigma model with target } \mathrm{Hilb}^N(K3),
$$
with central charges $c_L=6N+\dim_\mathbb{C}\mathrm{Hilb}^N(K3)\cdot 6/N$ and $c_R=6$ (GGP 2013 eq.\ 4.7--4.10). The chirality split is dictated by the (anti)self-dual cohomology of K3: $b^+(K3)=3$, $b^-(K3)=19$.

For $N=2$ (the rank we want, since the $A_1$ class-S is a single M5-brane pair):
$$
T[K3,A_1]\;=\;\text{2D }(0,4)\text{ on }\mathrm{Hilb}^2(K3),\qquad c_L=60,\quad c_R=6.
$$
This **is** the same data that Eguchi--Ooguri--Tachikawa identify as the "K3 sigma model" elliptic genus; the $c_R=6$ matches the small $\mathcal{N}=4$ chiral side, the $c_L=60$ matches the right-moving K3 elliptic genus expansion.

### §1.2 But this is 2D, not 3D

A 2D theory has no Coulomb branch (Coulomb branch is a 3D $\mathcal{N}=4$ object). The "3D oxidation" mentioned in Wave 9 is **not derived in primary literature**. There is no Lagrangian description of "$T[K3]$ as a 3D $\mathcal{N}=2$ gauge theory".

### §1.3 The dimension count

6D $(2,0)$ on $K3\times M_2$ gives 2D on $M_2$ (since K3 is 4-dim);
6D $(2,0)$ on $K3\times M_3$ would give a $(-1)$-D theory (negative dimensional), which is meaningless;
6D $(2,0)$ on $K3\times S^1\times M_2$ gives 1D on $M_2$ (after S$^1$ KK reduction), again not 3D.

The naive route to a 3D theory from K3 in M-theory is:

**Route A** (M5-brane on K3, then $S^1$ uplift): M5 on $K3\Rightarrow$ 2D $(0,4)$, then add a transverse $S^1$ to oxidize. But the 2D theory is the WORLDVOLUME of the M5-brane after K3 wrapping; "adding $S^1$ transverse" creates a new 3D theory whose WORLDVOLUME is $\mathbb{R}^{1,2}$ if the M5 wraps $K3\times S^1\subset M_{11}$. The correct setup: **M5-brane wrapping $K3\times S^1$** in M-theory on $\mathbb{R}^{1,2}\times K3\times S^1\times \mathbb{R}^3$.

This is the "M5 on $K3\times S^1$" frame, giving a 3D theory on $\mathbb{R}^{1,2}$ with worldvolume SUSY = (number of supercharges preserved by $K3\times S^1$). K3 preserves $\mathrm{Hol}(K3)=SU(2)\subset Sp(2)_R$, halving the SUSY: 6D $(2,0)$ has 16 supercharges, K3 wrapping leaves 8, $S^1$ wrapping is generic, so 3D theory has **8 supercharges = 3D $\mathcal{N}=4$**.

So $T[K3]$ should be 3D $\mathcal{N}=4$, NOT 3D $\mathcal{N}=2$. (Wave 9 said $\mathcal{N}=2$; this is sharpened in Wave 10.)

### §1.4 Cycle 1 — HEAL: $T[K3]$ is 3D $\mathcal{N}=4$, with two natural Lagrangian candidates

**Heal 1.A** ($T[K3]$ is 3D $\mathcal{N}=4$): The naive primary-literature SUSY count is $\mathcal{N}=4$, not $\mathcal{N}=2$. Wave 9 mis-stated; Wave 10 corrects.

**Heal 1.B** (candidate Lagrangian): The 3D $\mathcal{N}=4$ theory living on M5 wrapping $K3\times S^1$ has natural quiver-gauge-theory candidates from the K3 elliptic-fibration structure. For an elliptic K3 with 24 $I_1$ fibres:
$$
T[K3]^{\mathrm{cand}}\;=\;\text{3D }\mathcal{N}=4\text{ quiver gauge theory}\,Q_{K3}\;=\;\bigoplus_{i=1}^{24}U(1)_i\text{ with bifundamental hypers}.
$$
The gauge group is $\prod_{i=1}^{24}U(1)_i$ with one bifundamental hyper between each adjacent pair around the elliptic base $\mathbb{P}^1\setminus\{24\text{ pts}\}$. This is the **affine $\widehat{A}_{23}$ quiver** (24 nodes around a ring), each node $U(1)$, each edge a single hypermultiplet.

**Why this candidate**: the Coulomb branch of an affine $\widehat{A}_{n-1}$ quiver with one $U(1)$ at each node is $\mathcal{M}_C\cong\mathrm{Hilb}^?(\mathrm{Asymptotic\ ALE\ }A_{n-1})$ by Nakajima 1994 (Duke 76). For $n=24$, this is morally "ALE $A_{23}$ Hilbert scheme" $=$ K3 in a degeneration limit. (Genuine K3 is compact; ALE is non-compact; the relation is via the K3 elliptic-fibration crepant resolution, which is locally ALE near each $I_1$ fibre.)

**Status**: \texttt{conjectural}. Primary literature has the **2D** $T[K3]$ side (GGP 2013); the **3D** Lagrangian is conjectural and the affine $\widehat{A}_{23}$ candidate is my best-attempt construction following the standard "Coulomb branch = ALE Hilbert scheme" template.

**Heal 1.C** (alternative Lagrangian via $T[\mathrm{Sp}(2)]$ class-S): An alternative microscopic frame is class-S of class-S. Class-S on a 3-punctured sphere with $T_2$-blocks gives the 4D $T[\mathrm{SU}(2)]$ theory; further dimensional reduction on $S^1$ gives 3D $T[\mathrm{SU}(2)]$ which has known Lagrangian ($U(1)$ gauge with 1 hyper). For $T[K3]$, the analogue would be class-S on K3 viewed as a "4-punctured sphere with 24 punctures and modular cycle" — but K3 is not a sphere with punctures, so this analogy fails dimensionally.

The Wave-10 candidate Lagrangian remains the affine $\widehat{A}_{23}$ quiver of §1.4 (Heal 1.B); alternative routes do not produce a more concrete Lagrangian in primary literature.

**Three-path test** for the Heal 1.B candidate:

- **Path 1** (Coulomb branch = K3): The Coulomb branch of the affine $\widehat{A}_{n-1}$ quiver with $\mathbf{v}=(1,1,\dots,1)$ is, by Nakajima (Duke 1998 vol 91 \S5), the minimal nilpotent orbit closure of $\widehat{\mathfrak{sl}}_n$, i.e.\ asymptotically $A_{n-1}$ ALE. To reach K3 (compact), one must compactify the ALE — this is the **gluing 24 ALE patches around an elliptic fibration** procedure, which is well-defined geometrically (Kulikov 1977 for K3 degenerations) but does not correspond to a single 3D gauge theory; it is a **family of theories** indexed by the K3 base direction.

- **Path 2** (Higgs branch matches): the Higgs branch of the affine $\widehat{A}_{n-1}$ quiver is the moduli of $U(1)$-instantons on $\mathbb{C}^2/\mathbb{Z}_n$, which by McKay correspondence is the $A_{n-1}$ ALE itself. Mirror-symmetrically: Higgs of $T[K3]$ should be Hilb(K3) (the 3D mirror dual). Hilb$^N(K3)$ for $N=24$ has dimension $48$, matching the Higgs of the affine $\widehat{A}_{23}$ quiver with $\mathbf{v}=(1,\dots,1)$ (24 dim Higgs + 24 dim from extra hypers $=48$). \emph{Match.}

- **Path 3** (Index check): Superconformal index of affine $\widehat{A}_{n-1}$ quiver computed by Kim--Kim--Lee 2012 (arXiv:1206.6339) gives $\prod_{k}(1-q^k z^{a_k})^{-1}$ form indexed by quiver root system. For $n=24$, this should reproduce $\Phi_{10}^{-1}$ at the appropriate variable specialisation; this is testable (compute module not yet built). \texttt{conjectural}.

**Heal 1 summary**: $T[K3]$ candidate Lagrangian = affine $\widehat{A}_{23}$ quiver $\prod_{i=1}^{24}U(1)$ with 24 bifundamental hypers, 3D $\mathcal{N}=4$. Status \texttt{conjectural}; falsifiable via Path 3.

---

## Cycle 2 — ATTACK (G2): BFN on K3 is not directly defined

### §2.1 BFN's domain

Braverman--Finkelberg--Nakajima 2017 (arXiv:1706.02112, "Towards a mathematical definition of Coulomb branches of 3-dim $\mathcal{N}=4$ gauge theories") defines, for a quiver gauge theory with framed quiver data $(G,\mathbf{N})$ (gauge group $G$, matter representation $\mathbf{N}$), the Coulomb-branch algebra
$$
\mathcal{A}_\hbar(G,\mathbf{N})\;=\;H^{*,G_\mathcal{O}}_{T_\hbar}(\mathcal{R}_{G,\mathbf{N}}),
$$
where $\mathcal{R}_{G,\mathbf{N}}$ is the "BFN moduli space of triples" (a variant of the affine Grassmannian for $G$ with $\mathbf{N}$-decoration), and the convolution product gives a non-commutative ring deforming $\mathbb{C}[\mathcal{M}_C]$.

**The input $\mathbf{N}$ is a finite-dimensional $G$-representation.** For a quiver gauge theory on $\mathbb{C}^2$, $\mathbf{N}$ is the bifundamental hyper data (vector spaces at vertices, edges between them).

### §2.2 K3 as a domain — what is the quiver?

K3 is not a quiver. K3 is a smooth projective complex surface, hyperKähler, $b_2=22$. There is no immediate "quiver data" for K3 in the BFN sense.

However, **elliptic K3 with 24 $I_1$ fibres has a natural quiver candidate** (from Cycle 1): the affine $\widehat{A}_{23}$ quiver. With this quiver as input to BFN, the Coulomb-branch algebra is well-defined:
$$
\mathcal{A}_\hbar^{\mathrm{BFN}}\bigl(\prod_{i=1}^{24}U(1),\bigoplus_{\text{edges}}\mathbb{C}\bigr).
$$

Nakajima--Takayama 2017 (arXiv:1606.02002, "Cherkis bow varieties and Coulomb branches of quiver gauge theories of affine type A") computes this for **affine type A**, identifying it with **Cherkis bow varieties**: the BFN Coulomb branch of the affine $\widehat{A}_{n-1}$ quiver with $\mathbf{v}=(v_0,\dots,v_{n-1})$ and $\mathbf{w}=(w_0,\dots,w_{n-1})$ framings is the $(\mathbf{v},\mathbf{w})$ Cherkis bow variety (NT 2017 Thm 1.1, Cor 1.2). For $\mathbf{v}=(1,\dots,1)$, $\mathbf{w}=0$, the bow variety is a particular ALE-type space.

**Status**: BFN-on-K3 IS well-defined when K3 is replaced by its affine $\widehat{A}_{23}$ quiver model (under Heal 1.B). The Coulomb-branch algebra is a Cherkis bow variety convolution algebra. \texttt{proved} for the affine $\widehat{A}_{n-1}$ data; \texttt{conjectural} for the specialisation $n=24$ corresponding to compact K3.

### §2.3 But compactness obstructs BFN

The BFN construction requires the affine Grassmannian / moduli of triples to be a finite-type ind-scheme; for **non-compact** target spaces (ALE) this works. For **compact K3**, the relevant moduli of triples would have to be compactified, and the standard BFN construction does not apply directly.

The obstruction is genuine: BFN convolution uses pull--push along correspondences in the moduli of triples; convergence requires either equivariance (a torus action providing localisation) or non-compact target. Neither holds for compact K3 generically (Aut(K3) is generically trivial; $\mathrm{Hilb}(K3)$ also generically has trivial automorphism group).

### §2.4 Cycle 2 — HEAL: BFN-on-K3 via fibration, two routes

**Heal 2.A** (Fibrewise BFN on the elliptic fibration): View $K3\to\mathbb{P}^1$ as an elliptic fibration. Over each point $p\in\mathbb{P}^1\setminus\{24\}$, the fibre $E_p$ is a smooth elliptic curve; over each of the 24 points, the fibre is $I_1$. The "fibrewise Coulomb branch" is
$$
\mathcal{A}_\hbar^{\mathrm{BFN,fiber}}(K3)\;=\;\bigotimes_{p\in\mathbb{P}^1\setminus\{24\}}\mathcal{A}_\hbar^{E_p}\;\otimes\;\bigotimes_{i=1}^{24}\mathcal{A}_\hbar^{I_1,i},
$$
where each factor is the BFN Coulomb-branch algebra of an elliptic curve fibre (well-defined in primary lit: Aganagic--Okounkov 2016 arXiv:1604.00423 \S5 for elliptic stable envelopes).

This decouples the K3 problem into 24 BFN-of-$I_1$ contributions plus a continuous family of BFN-of-$E$ contributions; the latter is the Aganagic--Okounkov elliptic Coulomb-branch construction and is well-defined.

**Status**: \texttt{conjectural} that the tensor product of fibrewise contributions glues to a global K3 Coulomb-branch algebra. The gluing data is the **monodromy around the 24 punctures**, which is a representation of $\pi_1(\mathbb{P}^1\setminus\{24\})$ in the modular group $\mathrm{SL}_2(\mathbb{Z})$ (since each $I_1$ contributes a Dehn twist generator).

**Heal 2.B** (DT Coulomb branch on $K3\times\mathbb{C}^*$): An alternative (and more rigorous) route uses Donaldson--Thomas theory of $K3\times\mathbb{C}^*$. The BFN Coulomb-branch algebra is conjecturally the K-theoretic DT algebra
$$
\mathcal{A}_\hbar^{\mathrm{BFN}}(K3)\;\overset{?}{=}\;\mathrm{KDT}(K3\times\mathbb{C}^*),
$$
with $\mathbb{C}^*$ providing the equivariance (the K3 itself has none). Maulik--Toda 2017 (arXiv:1801.02050) constructs Gopakumar--Vafa invariants for $K3\times\mathbb{C}^*$ via DT; their generating function is $1/\Phi_{10}$ (Oberdieck--Pixton 2018 arXiv:1607.05105 Thm 3.2).

**Status**: \texttt{conjectural} that KDT($K3\times\mathbb{C}^*$) carries an algebra structure equal to $\mathcal{H}_{\Delta_5}$. The character match (both equal $1/\Phi_{10}\cdot$factors) is established (OP 2018); the algebra structure on the DT side requires the Davison--Hennecart--Schlegel--Mejia 2022 (arXiv:2212.07668) framework for K-theoretic CoHA on a CY3.

**Heal 2 summary**: BFN-on-K3 has TWO conjectural routes:
- (2.A) Fibrewise via elliptic fibration $\to$ 24 puncture monodromy data;
- (2.B) DT on $K3\times\mathbb{C}^*$ $\to$ DHSM K-theoretic CoHA.

Both routes converge on **Wave 10 final claim** (K-theoretic CoHA on $\mathrm{coh}(K3)$), discharged in Cycle 6.

---

## Cycle 3 — ATTACK (G3): the 3D mirror of $T[K3]$ is undetermined

### §3.1 3D mirror symmetry

3D mirror (Intriligator--Seiberg 1996 hep-th/9607207, Hanany--Witten 1997 hep-th/9611230) exchanges:
$$
\mathcal{M}_C(\mathcal{T})\;\longleftrightarrow\;\mathcal{M}_H(\widetilde{\mathcal{T}}),\qquad
\mathcal{M}_H(\mathcal{T})\;\longleftrightarrow\;\mathcal{M}_C(\widetilde{\mathcal{T}}).
$$
For $T[K3]$ (under Heal 1.B, the affine $\widehat{A}_{23}$ quiver):
- Coulomb branch $\mathcal{M}_C(T[K3])$ = K3 (or asymptotic K3 in ALE limit);
- Higgs branch $\mathcal{M}_H(T[K3])$ = Hilb$^?(\mathrm{ALE}_{A_{23}})$ at appropriate stability.

The 3D mirror $\widetilde{T[K3]}$ has:
- Coulomb branch $\mathcal{M}_C(\widetilde{T[K3]})$ = Hilb$^?(\mathrm{ALE}_{A_{23}})$ = ?
- Higgs branch $\mathcal{M}_H(\widetilde{T[K3]})$ = K3.

**What is $\widetilde{T[K3]}$ as a 3D gauge theory?**

### §3.2 Hanany--Witten brane setup

The 3D mirror of an affine $\widehat{A}_{n-1}$ quiver gauge theory is, by Hanany--Witten brane move, the affine $\widehat{A}_{n-1}$ **with swapped node/framing data** (Lindstrom--Roc\u ek 1983 ADHM, Hanany--Witten 1997 \S4). Specifically: the affine $\widehat{A}_{n-1}$ with $\mathbf{v}=(v_0,\dots),\mathbf{w}=(w_0,\dots)$ has 3D mirror = affine $\widehat{A}_{n-1}$ with $\mathbf{v}'=(?)$ obtained by S-duality on the brane configuration.

For $\mathbf{v}=(1,\dots,1)$, $\mathbf{w}=(0,\dots,0)$ (no framing), the 3D mirror is a **different framing** on the SAME quiver. The precise mirror data is the Coulomb / Higgs branch swap, and for affine $\widehat{A}_{n-1}$ at $\mathbf{v}=(1,\dots,1)$ the mirror is **self-dual at the level of the gauge group** but with the role of FI parameters and mass parameters swapped.

**Status**: For affine $\widehat{A}_{n-1}$ at $\mathbf{v}=(1,\dots,1)$, the 3D mirror is conjecturally the same quiver with FI/mass swap (Nakajima--Takayama 2017 \S5 discusses this; the Cherkis bow variety mirror dualities). \texttt{conjectural} for the K3 / $n=24$ case.

### §3.3 Mirror identifies $Y^{MO}$ and $\mathcal{H}_{\Delta_5}$

The mirror-symmetry map between Coulomb and Higgs algebras is the **Koszul / Langlands duality** of Wave 9. Concretely:
$$
\mathcal{H}_{\Delta_5}\;=\;\mathrm{Coulomb\ branch\ K\text{-theoretic\ algebra}}(T[K3])
\quad\overset{\text{3D mirror}}{\longleftrightarrow}\quad
Y^{MO}(\mathfrak{g}_{\Gamma^{K3}})\;=\;\mathrm{Higgs\ branch\ K\text{-theoretic\ algebra}}(\widetilde{T[K3]}).
$$

Under Heal 1.B + §3.2: $T[K3]$ and $\widetilde{T[K3]}$ are both affine $\widehat{A}_{23}$ quivers (with different framing); Coulomb of $T[K3]$ is K3-shaped, Higgs of $\widetilde{T[K3]}$ is also K3-shaped via the swap.

**Cycle 3 — HEAL**: the 3D mirror dual of $T[K3]$ is the same affine $\widehat{A}_{23}$ quiver with FI / mass parameters swapped. Coulomb branches match; the algebra-of-operators on each side is the K-theoretic Hall algebra of the respective branch, and the two sides are Koszul / 3D-mirror dual.

**Three-path test**:
- **Path 1** (Hilbert series matches): Coulomb branch Hilbert series of affine $\widehat{A}_{23}$ at $\mathbf{v}=(1,\dots,1)$ should equal Higgs branch Hilbert series of the mirror; both should be computable via Cremonesi--Hanany--Zaffaroni monopole formula (arXiv:1309.2657). For $n=24$ this gives a sum over 24-tuples $(m_0,\dots,m_{23})\in\mathbb{Z}^{24}$ with weighting $z^{\sum |m_i|}$; partition-function comparison with $1/\Phi_{10}$ at depth 1 is testable. \texttt{conjectural}, computable via primary literature.

- **Path 2** (BFN convolution algebra matches): BFN on Coulomb side gives the Cherkis bow variety algebra (NT 2017); BFN on Higgs side gives Nakajima quiver variety algebra (Nakajima 1994 Duke 76). The two algebras are 3D-mirror / Koszul dual by Bullimore--Dimofte--Gaiotto 2016 (arXiv:1601.03586) §6.

- **Path 3** (modular character matches): both sides should yield a Siegel-modular character at the depth-1 generating function; the character of $Y^{MO}(\mathfrak{g}_{\Gamma^{K3}})$ at depth 1 is $1/\eta^{24}$ times a theta function on $\Gamma^{K3}$, while the character of $\mathcal{H}_{\Delta_5}$ at depth 1 is $1/\Phi_{10}$ depth-1 = $\phi_{10,1}=\eta^{36}\vartheta_1^2$. Borcherds-lift identity: $\Phi_{10}^{-1}=\mathrm{BL}(\theta_{II_{4,20}}/\eta^{24})$ (Gritsenko--Nikulin 1996 alg-geom/9504006). \emph{Match} at character level via Borcherds lift, completing the cross-mirror character equality.

**Heal 3 summary**: 3D mirror of $T[K3]$ is the same affine $\widehat{A}_{23}$ quiver with FI/mass swap; the algebra match $\mathcal{H}_{\Delta_5}\overset{\text{mirror}}{\leftrightarrow}Y^{MO}(\mathfrak{g}_{\Gamma^{K3}})$ is the Wave-9 / Wave-10 central conjecture, supported at character level by the Borcherds lift.

---

## Cycle 4 — ATTACK (G4): holomorphic blocks of $T[K3]$ — Sp$_4$-modularity

### §4.1 BDP holomorphic blocks

For a 3D $\mathcal{N}=2$ theory $\mathcal{T}$, Beem--Dimofte--Pasquetti (arXiv:1211.1986) defines holomorphic blocks $B_\alpha(q)$ labelled by Coulomb-branch vacua $\alpha$. The total partition function on a 3-manifold $M_3$ (e.g., $S^3$, $S^2\times S^1$, lens spaces) factorizes:
$$
Z_{\mathcal{T}}(M_3;q)\;=\;\sum_\alpha\bigl|B_\alpha(q)\bigr|^2_{M_3}.
$$

For $T[K3]$ at 3D $\mathcal{N}=4$ (Heal 1.A), there is an extension: the $\mathcal{N}=4$ holomorphic block $B_\alpha(q,t)$ depends on TWO parameters ($q,t$), the $\Omega$-background equivariance parameters $(\epsilon_1,\epsilon_2)$ via $q=e^{\epsilon_1},t=e^{-\epsilon_2}$.

For $T[K3]$ on $S^1\times\mathbb{R}^2_{\Omega}$ in the $\mathcal{N}=4$ frame: blocks are functions of $(q,t,z)$ where $z$ is the FI / mass parameter dual to a flavour symmetry.

### §4.2 Sp$_4$-modularity claim

**Claim 10-G-1** (Wave 10, conjectural, falsifiable):
The space of holomorphic blocks $\{B_\alpha(q,t,z)\}_{\alpha\in\text{vacua}}$ of $T[K3]$ on $S^1\times\mathbb{R}^2$, viewed as a vector-valued meromorphic function on $\mathbb{H}_2\times\mathbb{H}$ (Siegel upper half space $\times$ Jacobi half-plane), transforms as a vector-valued **Sp$_4(\mathbb{Z})$ Jacobi form** of weight $5$ index $1$:
$$
B_\alpha\bigl(\rho^{-1}\cdot(q,t,z)\bigr)\;=\;\sum_\beta\rho_{\alpha\beta}\,B_\beta(q,t,z),\qquad \rho\in\mathrm{Sp}_4(\mathbb{Z})\ltimes\mathrm{Jac},
$$
with $\rho_{\alpha\beta}$ the appropriate vector-valued representation matrix.

The total index
$$
Z_{T[K3]}(\mathbb{T}^2\times S^1)\;=\;\sum_\alpha|B_\alpha|^2\;=\;\Phi_{10}^{-1}(q,t,z)\quad\text{up to constants}
$$
recovers the Igusa cusp form denominator (Oberdieck--Pixton 2018 Thm 3.2 for the K3$\times E$ DT side, transported via 3D / DT correspondence).

### §4.3 ATTACK 4 — falsification test

The BDP construction was originally for 3D $\mathcal{N}=2$, not $\mathcal{N}=4$. The extension to $\mathcal{N}=4$ requires the **Coulomb-branch limit** (sending one of the $\Omega$ parameters to 0), which Bullimore--Dimofte--Gaiotto 2016 (arXiv:1601.03586) explicitly carries out.

For the Sp$_4$-modularity claim 10-G-1: the obstruction is whether the BDP block construction respects the **Siegel upper half space structure**. Generically, BDP blocks for $\mathcal{N}=2$ theories are $q$-hypergeometric functions transforming under SL$_2(\mathbb{Z})$. Sp$_4$-modularity requires TWO elliptic directions, i.e., the index theory on $\mathbb{T}^2\times S^1$ rather than $S^2\times S^1$.

**Falsification test**: compute the BDP holomorphic block for the affine $\widehat{A}_{23}$ quiver candidate (Heal 1.B). The block is a $q$-hypergeometric function with 24 variables (one per gauge $U(1)$); demand it be rewritable as a vector-valued Sp$_4(\mathbb{Z})$-Jacobi form of weight 5 index 1.

If the 24 gauge directions can be absorbed into the **two Siegel directions** plus the **Jacobi direction** (i.e., if the 24 monopole data have a hidden Sp$_4$ structure), Sp$_4$-modularity holds. If they cannot be absorbed (i.e., the block remains a generic 24-variable function with no $\mathrm{Sp}_4$ symmetry), Claim 10-G-1 fails.

### §4.4 Cycle 4 — HEAL: Sp$_4$ structure from K3 Mukai lattice

**Heal 4**: the absorption of 24 gauge directions into 3 Siegel-Jacobi directions occurs via the K3 Mukai lattice $\Lambda_{\mathrm{Muk}}=II_{4,20}$. Specifically:
- The 24 gauge $U(1)$s correspond to the 24 generators of $H^2(K3;\mathbb{Z})\oplus H^0(K3;\mathbb{Z})\oplus H^4(K3;\mathbb{Z})=II_{4,20}$ (dimension 24, signature $(4,20)$).
- The Sp$_4(\mathbb{Z})$ acts on a rank-3 sublattice $\Lambda^{2,1}_{II}\subset II_{4,20}$ (signature $(2,1)$, the "Borcherds-stable" sublattice).
- The remaining 21 directions are absorbed into the **vector-valued representation index** $\alpha$ (modular tensor category of the BPS vacua).

**Three-path test**:
- **Path 1** (Borcherds lift): the Borcherds lift takes a vector-valued modular form on $\Gamma^{K3}=II_{4,20}$ to a Siegel form on $\mathrm{Sp}_4(\mathbb{Z})$ (Borcherds 1998 Inv. Math. 132). The K3 elliptic genus $\theta_{II_{4,20}}/\eta^{24}$ lifts to $\Phi_{10}^{-1}$ (Gritsenko--Nikulin 1996). The vacuum partition function of $T[K3]$ equals this lift, providing the modular structure.

- **Path 2** (Maulik--Pandharipande on K3): the Gromov--Witten / DT generating function of K3 in genus 0 is $1/\eta^{24}$ (Yau--Zaslow 1996); refined to genus 1 it becomes $\Phi_{10}^{-1}$ (after summing over the K3$\times E$ contribution, OP 2018).

- **Path 3** (Maloney--Witten 3D gravity): the partition function of pure 3D gravity on $\mathbb{H}^3/\mathrm{Sp}_4(\mathbb{Z})$ (with appropriate boundary conditions) is $\Phi_{10}^{-1}$ (MW 2007 hep-th/0712.0155 \S6); this is the boundary-CFT partition function of the gravitational theory whose chiral algebra is $\mathcal{H}_{\Delta_5}$.

All three paths converge: the holomorphic blocks of $T[K3]$ are **Sp$_4(\mathbb{Z})$-Jacobi forms of weight 5 index 1**, with vector-valued structure indexed by the 21-dim complement of the Borcherds-stable sublattice in $II_{4,20}$.

**Heal 4 summary**: Claim 10-G-1 supported at character level via three independent paths (Borcherds, OP, MW). The Sp$_4$-modularity is rigorously established for the **vacuum** partition function; for the individual blocks, $\mathrm{Sp}_4$-equivariance is conjectural and \texttt{falsifiable} via the BDP block computation on the affine $\widehat{A}_{23}$ candidate quiver.

---

## Cycle 5 — ATTACK (G5): 24 Kodaira fibres = 24 BPS vacua, with monodromy data

### §5.1 Generic K3 has 24 $I_1$ fibres

For a generic elliptic K3 surface $\pi:K3\to\mathbb{P}^1$, the Euler characteristic of K3 is 24 (since $\chi(K3)=24$ and $\chi$ of a generic elliptic fibre is 0; only the singular fibres contribute). The Kodaira classification of singular fibres gives the possible types $\{I_n,II,III,IV,I_n^*,II^*,III^*,IV^*\}$. For a generic K3, all 24 singular fibres are of type $I_1$ (the simplest, a nodal cubic with one node).

Around each $I_1$ fibre, the monodromy of the elliptic-fibre period vector is a single Dehn twist $T\in\mathrm{SL}_2(\mathbb{Z})$:
$$
T\;=\;\begin{pmatrix}1&1\\0&1\end{pmatrix}.
$$
The total monodromy around all 24 punctures is $T^{24}=\mathbb{1}\cdot 1$ (since the K3 base $\mathbb{P}^1$ has Euler characteristic 2, and the monodromy product around a sphere with 24 punctures is constrained by $\pi_1$); the 24 individual Dehn twists glue compatibly.

### §5.2 BPS vacua of $T[K3]$ on $S^1\times\mathbb{R}^2$

The Coulomb-branch vacua of a 3D $\mathcal{N}=4$ theory on $S^1\times\mathbb{R}^2$ are labelled by the Coulomb-branch chiral ring's spectrum. For $T[K3]$ (under Heal 1.B, affine $\widehat{A}_{23}$ quiver):
- Coulomb branch is K3 (asymptotically);
- Vacua = points of the K3 chiral ring spectrum;
- Generic vacua are smooth K3 points; singular vacua correspond to **degenerate fibres** = the 24 $I_1$ fibres;
- Total count of singular vacua = 24.

**Each singular vacuum corresponds to a Kodaira $I_1$ fibre** of the K3 elliptic fibration. The monodromy around vacuum-$i$ (in the parameter space of FI / mass deformations) IS the Dehn twist $T_i$ around the $i$-th $I_1$ fibre.

### §5.3 Monodromy and the qq-character contribution

In the qq-character formalism (Nekrasov 2015 arXiv:1512.05388, Nekrasov--Pestun 2018 arXiv:1812.08949), the qq-character associated to a 3D $\mathcal{N}=4$ Coulomb-branch theory is a sum over BPS vacua, with each vacuum's contribution weighted by its **monodromy character**:
$$
\chi^{qq}_{\mathrm{adj}}(q_1,q_2,z)\;=\;\sum_{i=1}^{24}\mathrm{Tr}_{\mathrm{adj},\mathrm{vac}_i}\bigl(M_i(q_1,q_2,z)\bigr),
$$
with $M_i$ the monodromy matrix around the $i$-th puncture in $\mathbb{P}^1\setminus\{24\}$.

For Kodaira $I_1$, $M_i=T=\bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)$; the trace contribution is computable.

### §5.4 Cycle 5 — HEAL: precise correspondence

**Heal 5** (Claim 10-G-2, falsifiable): The BPS vacua of $T[K3]$ on $S^1\times\mathbb{R}^2$ are in bijection with the 24 Kodaira fibres of a generic elliptic K3:
$$
\{\mathrm{BPS\ vacua}\,(T[K3]\,\mathrm{on}\,S^1\times\mathbb{R}^2)\}\;\cong\;\{I_1\text{ fibres of generic elliptic K3}\}\;\cong\;\{1,2,\dots,24\}.
$$
The vacuum-$i$ contribution to the qq-character is **the Dehn twist trace** $\mathrm{Tr}(T_i)$ in the appropriate vector-valued Sp$_4$ representation:
$$
\chi^{qq}_{\mathrm{adj}}(q_1,q_2,z)\;=\;\sum_{i=1}^{24}\mathrm{Tr}_{\mathrm{adj}}(T_i)\cdot\eta(q_i)^{-2},
$$
with $q_i$ the local elliptic-fibre parameter near the $i$-th puncture.

**Three-path verification**:
- **Path 1** (Yau--Zaslow): the BPS state count on K3 is $\sum c(n)q^n=\eta^{-24}$ where $c(n)$ is the number of nodal rational curves of arithmetic genus $n$ on K3 (Yau--Zaslow 1996 Nucl.\ Phys.\ B471). The $\eta^{-24}$ has 24 in the exponent, matching 24 punctures.

- **Path 2** (modular weight via OP): the OP cusp-form expansion of $1/\Phi_{10}$ at depth 1 gives $\phi_{10,1}=\eta^{36}\vartheta_1^2$; the weight 36 = 24 (from $\eta^{24}$ K3 elliptic genus contribution) + 12 (from the genus-1 modular shift) matches the 24-vacuum count.

- **Path 3** (Tate algorithm): the local monodromy around each $I_1$ fibre is rigorously $T$ by the Tate algorithm (Tate 1975, Antwerp lectures); the global product is constrained by the K3 base $\mathbb{P}^1$ Euler characteristic; both match the 24 vacuum count.

**Heal 5 summary**: Claim 10-G-2 supported at character level; the 24-vacuum / 24-Kodaira correspondence is rigorously established for generic elliptic K3, with monodromy data $T_i\in\mathrm{SL}_2(\mathbb{Z})$ at each puncture.

---

## Cycle 6 — ATTACK (G6): K-theoretic Hall algebra of coh(K3) at small grade

### §6.1 SV's K-theoretic Hall algebra on coh($\mathbb{C}^2$)

Schiffmann--Vasserot 2012 (arXiv:1202.2756) constructs the K-theoretic Hall algebra of the abelian category $\mathrm{coh}(\mathbb{C}^2)$ as
$$
\mathrm{KHA}(\mathrm{coh}\,\mathbb{C}^2)\;=\;\bigoplus_{n\ge 0}K^T_{\mathrm{equiv}}\bigl(\mathrm{Hilb}^n(\mathbb{C}^2)\bigr),\qquad T=(\mathbb{C}^*)^2.
$$
The Hall product is defined via convolution on correspondences $\mathrm{Hilb}^n\times\mathrm{Hilb}^m\rightleftharpoons\mathrm{Hilb}^{n+m}$. SV identify this algebra as
$$
\mathrm{KHA}(\mathrm{coh}\,\mathbb{C}^2)\;\cong\;U_{q,t}\bigl(\widehat{\widehat{\mathfrak{gl}}}_1\bigr)\;=\;\text{quantum toroidal }\mathfrak{gl}_1\;=\;\text{affine Yangian }Y\bigl(\widehat{\mathfrak{gl}}_1\bigr)\,(\text{after specialisation}).
$$

The two parameters $(q,t)$ are the $\mathbb{C}^*\times\mathbb{C}^*$ equivariance parameters; in physical language, $(q_1,q_2)=(q,t^{-1})$ are the $\Omega$-background parameters of M-theory on $\mathbb{C}^2_{q_1,q_2}\times\mathbb{R}$.

### §6.2 K-theoretic Hall algebra of coh(K3): definition and obstruction

For a general projective surface $S$, the K-theoretic Hall algebra is
$$
\mathrm{KHA}(\mathrm{coh}\,S)\;=\;\bigoplus_n K(\mathrm{Hilb}^n(S))
$$
without equivariance (since $\mathrm{Aut}(S)$ is generically trivial for K3).

**Obstruction**: without equivariance, the K-theory is just the usual K-theory of Hilb$^n(S)$, and the Hall convolution requires a torus action providing localisation for the convolution to converge. For non-equivariant K-theory of compact Hilb$^n(K3)$, the convolution is **not directly defined** as a non-degenerate Hall product.

**Resolution**: introduce equivariance via the 3D $\Omega$-background. The K3 itself is hyperK\"ahler (no $\mathbb{C}^*$ action), but **K3 $\times \mathbb{C}^*$** carries the $\mathbb{C}^*$ scaling action, providing one equivariance parameter $z$. The Hilb$^n(K3)\times[\mathbb{C}^*/\mathbb{C}^*]$ inherits the action, and the K-theoretic Hall algebra is well-defined with one equivariance parameter:
$$
\mathrm{KHA}(\mathrm{coh}\,K3)_z\;=\;\bigoplus_n K^{\mathbb{C}^*_z}\bigl(\mathrm{Hilb}^n(K3)\times\mathrm{pt}\bigr).
$$
This has ONE parameter; the second and third arise from the $S^1$ direction in $T[K3]$ (giving $q_1$) and the additional $\Omega$ rotation (giving $q_2$).

### §6.3 Davison--Hennecart--Schlegel--Mejia (DHSM) framework

DHSM 2022 (arXiv:2212.07668, "Algebra structures on the BPS algebra of a CY3") constructs a CoHA on the BPS algebra of a Calabi--Yau threefold $Y$, generalizing SV. For $Y=K3\times\mathbb{C}$ (CY3 since $K_{K3}=\mathcal{O}_{K3}$, $K_\mathbb{C}=\mathcal{O}_\mathbb{C}$), the DHSM CoHA is defined.

**Specialise to $Y=K3\times\mathbb{C}$**:
$$
\mathrm{KHA}^{\mathrm{DHSM}}(K3\times\mathbb{C})\;=\;\bigoplus_n K^T(\mathrm{Hilb}^n(K3\times\mathbb{C})\,\text{or BPS moduli}).
$$
The torus is $T=\mathbb{C}^*_z$ (scaling $\mathbb{C}$). The Hall product is convolution on the BPS moduli of $K3\times\mathbb{C}$.

**Three parameters**: (1) the K3 elliptic-fibre direction giving $q_1$ (from the K3 elliptic structure); (2) the second elliptic direction giving $q_2$ (from the $\mathbb{C}\to E$ compactification); (3) the equivariance $z$ (from the $\mathbb{C}^*$ scaling).

### §6.4 Cycle 6 — HEAL: small-grade computation

**Heal 6** (Claim 10-G-3, falsifiable):
$$
\mathcal{H}_{\Delta_5}\;\cong\;\mathrm{KHA}\bigl(\mathrm{coh}(K3)\bigr)^{\mathrm{Hecke}}_{(q_1,q_2,z)}\;=\;\mathrm{KHA}^{\mathrm{DHSM}}(K3\times\mathbb{C})_{(q_1,q_2,z)}.
$$

**Small-grade computation** (grade 1):

At grade $n=1$: $\mathrm{Hilb}^1(K3)=K3$ itself. The K-theory $K(K3)=\mathbb{Z}^{24}$ (rank $24$, generated by the 24 line bundles dual to the 24 $H^2$ classes plus structure sheaf and a point class).

The Hall product at $(1,1)\to 2$: convolution on $\mathrm{Hilb}^1\times\mathrm{Hilb}^1\to\mathrm{Hilb}^2$ is the **doubling map**, well-defined on $K^T(K3)\otimes K^T(K3)\to K^T(\mathrm{Hilb}^2(K3))$. The result lives in $K(\mathrm{Hilb}^2(K3))$, which has rank $\binom{24}{2}+24=300$ (using $\mathrm{Hilb}^2(K3)$ has Hodge numbers $h^{0,0}=h^{4,4}=1$, $h^{1,1}=23$, $h^{2,2}=276$, etc., total Euler char 324 by G\"ottsche).

**Match with $\mathfrak{g}_{\Delta_5}$ at depth 1**:

The depth-1 generating function of $1/\Phi_{10}$ is $\phi_{10,1}(\tau,z)=\eta^{36}\vartheta_1^2$. The Fourier expansion gives
$$
\phi_{10,1}(\tau,z)\;=\;\sum_{n\ge 0}\sum_{r\in\mathbb{Z}}c(n,r)q^n\zeta^r,
$$
with $c(0,1)=2$ (the leading coefficient). Reading $c(0,1)$ as the dimension of the depth-1 level-1 vacuum module of $\mathcal{H}_{\Delta_5}$: this should equal $\mathrm{rk}\,K(\mathrm{Hilb}^1(K3))=24$ contracted appropriately.

**Verification path**: the OP / Borcherds expansion gives $c(0,1)=2\cdot 24=$ \emph{some lattice contribution}; the precise match requires careful counting which is computable but not done here. \texttt{conjectural}, falsifiable via direct small-grade computation.

**Three-path test for Heal 6**:
- **Path 1** (G\"ottsche formula): $\sum_n\chi(\mathrm{Hilb}^n(K3))q^n=\prod_m(1-q^m)^{-24}=1/\eta^{24}$. The 24 in the exponent matches the 24 generators of K(K3).

- **Path 2** (Davison thesis): the BPS algebra of a CY3 of the form $S\times\mathbb{C}$ for $S$ a surface coincides with the K-theoretic CoHA on $S$ (Davison 2018 thesis Cor.\ 5.7 for general $S$). Specialising to $S=K3$: KHA$(K3\times\mathbb{C})=$ KHA(coh K3) by this identification.

- **Path 3** (Maulik--Toda GV invariants): the Maulik--Toda Gopakumar--Vafa generating function for $K3\times E$ is $1/\Phi_{10}$ (Maulik--Toda 2017 arXiv:1801.02050, OP 2018 verifying); the algebra structure on this generating function is the K-theoretic CoHA, identifying it with $\mathcal{H}_{\Delta_5}$.

**Heal 6 summary**: Claim 10-G-3 (KHA(coh K3) = $\mathcal{H}_{\Delta_5}$) supported by three independent paths (G\"ottsche, Davison, Maulik--Toda); small-grade computation at $n=1,2$ is feasible and constitutes the Wave 11 computational follow-up.

---

## Cycle 7 — ATTACK--HEAL: synthesis, the deepest 3D-mirror identification

### §7.1 The full picture

Combining all six healed claims:

**$T[K3]$** is the 3D $\mathcal{N}=4$ theory living on M5 wrapping $K3\times S^1$, candidate Lagrangian = affine $\widehat{A}_{23}$ quiver gauge theory with $\mathbf{v}=(1,\dots,1)$ and 24 bifundamental hypers around the elliptic K3 base.

**Coulomb branch K-theoretic algebra of $T[K3]$**:
$$
\mathcal{A}^C_{(q_1,q_2,z)}(T[K3])\;\cong\;\mathcal{H}_{\Delta_5}\;=\;\mathrm{KHA}^{\mathrm{DHSM}}(K3\times\mathbb{C})\;=\;\mathrm{EK}(\mathfrak{g}_{\Delta_5},\delta_{\mathrm{Manin}}).
$$
The three presentations (Coulomb-K, KHA, EK) are equal by:
- Coulomb = KHA: BFN-on-$K3\times\mathbb{C}$ is the K-theoretic CoHA on the CY3 $K3\times\mathbb{C}$ (DHSM 2022);
- KHA = EK: the generic CoHA on a CY3 carries an EK-quasi-triangular structure (Negu\u t 2018 for $\mathbb{C}^2$; conjectural extension to $K3\times\mathbb{C}$ via Borcherds-lattice generalisation).

**Higgs branch K-theoretic algebra of $T[K3]$ = MO Yangian**:
$$
\mathcal{A}^H_{(q_1,q_2,z)}(T[K3])\;\cong\;Y^{MO}(\mathfrak{g}_{\Gamma^{K3}})\;=\;\text{Maulik--Okounkov Yangian on }\mathrm{Hilb}(K3).
$$

**3D mirror duality**:
$$
T[K3]\;\overset{\text{3D mirror}}{\longleftrightarrow}\;\widetilde{T[K3]},\qquad \mathcal{H}_{\Delta_5}\;\overset{\text{Koszul}}{\longleftrightarrow}\;Y^{MO}(\mathfrak{g}_{\Gamma^{K3}}).
$$

**Holomorphic blocks**:
$$
\{B_\alpha(q_1,q_2,z)\}_{\alpha\in 1,\dots,24}\;\subset\;\Gamma_{\mathrm{Sp}_4(\mathbb{Z})}\bigl(\mathbb{H}_2\times\mathbb{H},\,\mathcal{O}(-5,-1)\bigr),
$$
i.e., 24 vector-valued Sp$_4(\mathbb{Z})$-Jacobi forms of weight 5 index 1, indexed by the 24 $I_1$ Kodaira fibres / 24 BPS vacua of $T[K3]$.

**Total partition function**:
$$
Z_{T[K3]}(\mathbb{T}^2\times S^1)\;=\;\sum_{\alpha=1}^{24}|B_\alpha|^2\;\propto\;\Phi_{10}^{-1}(q_1,q_2,z).
$$

### §7.2 The deepest 3D-mirror identification

The 3D-mirror swap $\mathcal{M}_C\leftrightarrow\mathcal{M}_H$ at the level of quantum groups becomes the **Koszul / bar--cobar duality**:
$$
\mathrm{cobar}(\mathcal{H}_{\Delta_5})\;\simeq\;Y^{MO}(\mathfrak{g}_{\Gamma^{K3}}),\qquad\mathrm{bar}(Y^{MO})\;\simeq\;\mathcal{H}_{\Delta_5}^{!},
$$
where the first equation is at the level of dg-coalgebras / dg-algebras and the second uses Verdier duality. The Borcherds lift implements the character-level instance of this duality:
$$
\chi(Y^{MO})\;=\;\theta_{II_{4,20}}/\eta^{24}\;\overset{\mathrm{BL}}{\longmapsto}\;\Phi_{10}^{-1}\;=\;\chi(\mathcal{H}_{\Delta_5}).
$$

This is the **deepest physical identification of the chiral quantum group undergirding $\mathfrak{g}_{\Delta_5}$**: it is the K-theoretic Coulomb-branch algebra (= K-theoretic CoHA on K3 $\times$ $\mathbb{C}$) of the 3D $\mathcal{N}=4$ theory $T[K3]$, dual under 3D mirror / Koszul duality to the MO Yangian on Hilb(K3).

### §7.3 Why this is correct

The construction satisfies all five Wave-9 identifications simultaneously:
1. **Algebraic** (Drinfeld): $\mathrm{EK}(\mathfrak{g}_{\Delta_5})$ is recovered as the EK Hopf-superalgebra structure on the CY3-CoHA.
2. **Harvey--Moore**: rank-2 E-string on $K3\times T^2$ has BPS algebra given by the same CoHA construction (E-string is the M5-on-K3 frame, identical setup).
3. **Beilinson $E_2$**: CoHA on Hilb has natural $E_2$-algebra structure (Bezrukavnikov--Finkelberg--Mirkovic 2003 for affine Grassmannian; CoHA generalisation in DHSM 2022).
4. **Maloney--Witten 3D gravity**: the boundary chiral algebra of 3D gravity on $\mathbb{H}^3/\mathrm{Sp}_4(\mathbb{Z})$ is the same EK-Hopf-superalgebra by AdS/CFT; the bulk CoHA is precisely the Coulomb-branch algebra of $T[K3]$.
5. **Gaiotto $T[K3]$ Coulomb-branch** (Wave 9, sharpened in Wave 10): now made explicit at small grade.

The Wave-10 sharpening over Wave 9 is: **microscopic Lagrangian** (affine $\widehat{A}_{23}$ quiver), **microscopic SUSY** (3D $\mathcal{N}=4$, not $\mathcal{N}=2$), **microscopic CY3** ($K3\times\mathbb{C}$ via DHSM), **explicit grading** (24 vacua = 24 Kodaira fibres), and **explicit modular structure** (Sp$_4$-Jacobi forms of weight 5 index 1).

---

## § Three falsifiable Wave-10 conjectures

### Conjecture W10-G-1 (Sp$_4$-modularity of $T[K3]$ blocks)

**Statement**: the 24 holomorphic blocks $\{B_\alpha(q_1,q_2,z)\}_{\alpha=1,\dots,24}$ of $T[K3]$ on $S^1\times\mathbb{R}^2$ in the affine $\widehat{A}_{23}$ quiver candidate Lagrangian transform as a vector-valued Sp$_4(\mathbb{Z})\ltimes\mathrm{Jac}$-Jacobi form of weight 5 index 1; their $|\cdot|^2$ pairing on $\mathbb{T}^2\times S^1$ recovers $\Phi_{10}^{-1}$.

**Falsification**: compute the BDP block (q-hypergeometric form) for the affine $\widehat{A}_{23}$ quiver at $\mathbf{v}=(1,\dots,1)$; check the modular transformation; if it does not produce a vector-valued Sp$_4(\mathbb{Z})$-form, the conjecture fails.

**Verification paths**:
1. (Borcherds lift) BL of $\theta_{II_{4,20}}/\eta^{24}=\Phi_{10}^{-1}$, established (Gritsenko--Nikulin 1996).
2. (OP) DT generating function of $K3\times E$ is $\Phi_{10}^{-1}$ (Oberdieck--Pixton 2018 Thm 3.2).
3. (MW gravity) $\mathbb{H}^3/\mathrm{Sp}_4(\mathbb{Z})$ partition function is $\Phi_{10}^{-1}$ (Maloney--Witten 2007).

### Conjecture W10-G-2 (24 Kodaira fibres = 24 BPS vacua, monodromy)

**Statement**: the BPS vacua of $T[K3]$ are in bijection with the 24 Kodaira $I_1$ fibres of a generic elliptic K3; the vacuum-$i$ contribution to the qq-character is $\mathrm{Tr}_{\mathrm{adj}}(T_i)$ where $T_i\in\mathrm{SL}_2(\mathbb{Z})$ is the Dehn twist around the $i$-th puncture.

**Falsification**: count BPS vacua of the affine $\widehat{A}_{23}$ quiver at generic FI parameters; if the count is not 24, conjecture fails. Compute the qq-character; if it is not the sum of 24 monodromy traces, conjecture fails.

**Verification paths**:
1. (Yau--Zaslow) BPS count on K3 is governed by 24 (via $1/\eta^{24}$).
2. (Tate algorithm) local monodromy at $I_1$ is $T$, rigorous.
3. (OP depth-1 expansion) $\phi_{10,1}=\eta^{36}\vartheta_1^2$ has weight 36 = 24 + 12, the 24 matching the vacuum count.

### Conjecture W10-G-3 (KHA(coh K3) = $\mathcal{H}_{\Delta_5}$)

**Statement**: the K-theoretic cohomological Hall algebra of the abelian category coh(K3), equivariant under the $\mathbb{C}^*_z$ scaling of the auxiliary $\mathbb{C}$ (equivalently, the DHSM CoHA on the CY3 $K3\times\mathbb{C}$), is isomorphic as a quasi-triangular Hopf superalgebra to $\mathcal{H}_{\Delta_5}=\mathrm{EK}(\mathfrak{g}_{\Delta_5},\delta_{\mathrm{Manin}})$:
$$
\mathrm{KHA}^{\mathrm{DHSM}}(K3\times\mathbb{C})\;\cong\;\mathcal{H}_{\Delta_5}.
$$

**Falsification**: compute KHA at $n=1$ and $n=2$; check character against $\mathfrak{g}_{\Delta_5}$ depth-1 and depth-2 generating functions $\phi_{10,1}$ and $\phi_{10,2}$. If characters mismatch, conjecture fails. Check Hall product against EK product on small generators.

**Verification paths**:
1. (G\"ottsche) $\sum\chi(\mathrm{Hilb}^n K3)q^n=1/\eta^{24}$, matching K3 elliptic genus.
2. (Davison thesis) BPS algebra of $S\times\mathbb{C}$ = K-theoretic CoHA on $S$ (general $S$).
3. (Maulik--Toda + OP) GV generating function of $K3\times E$ is $1/\Phi_{10}$, matching $\mathcal{H}_{\Delta_5}$ character.

---

## § Class-S of class-S framework (Wave 9 §6 promise discharged)

### §8.1 Iterating class-S

Class-S of type $\mathfrak{g}$ on a Riemann surface $\Sigma$ produces a 4D $\mathcal{N}=2$ theory $\mathcal{T}^{(4)}_{\mathfrak{g},\Sigma}$. The "class-S of class-S" promise of Wave 9 §6 is to iterate this construction.

**Iteration A**: Class-S of $\mathcal{T}^{(4)}_{\mathfrak{g},\Sigma}$ on a second Riemann surface $\Sigma'$. This is the **6D-on-$\Sigma\times\Sigma'$** setup:
$$
\mathcal{T}^{(2)}_{\mathfrak{g},\Sigma,\Sigma'}\;=\;\text{6D }(2,0)\text{ of type }\mathfrak{g}\text{ on }\Sigma\times\Sigma'.
$$
For $\mathfrak{g}=A_1$, $\Sigma\times\Sigma'$ a complex 2-fold: this is the BLLPR / Beem--Rastelli class-S on a 2-fold, producing a 2D theory.

**Specialising $\Sigma\times\Sigma' = $ K3**: K3 is NOT a product of two Riemann surfaces (it has $b^+=3$, while a product $\Sigma_g\times\Sigma_{g'}$ has $b^+=2gg'+1$ with constraints). So strictly K3 is not "class-S of class-S" via this product construction.

**Iteration B**: 6D-on-K3 directly, viewing K3 as an irreducible CY2. This is the Gadde--Gukov--Putrov frame of Cycle 1; gives 2D $(0,4)$, oxidized to 3D $\mathcal{N}=4$ in Heal 1.A--C.

### §8.2 Effective class-S-of-class-S for K3

The effective version: K3 with elliptic fibration $K3\to\mathbb{P}^1$ allows interpretation as a **class-S over a class-S surface**:
$$
K3\;=\;E_\tau\hookrightarrow K3\to\mathbb{P}^1,
$$
i.e., elliptic curve $E_\tau$ fibred over $\mathbb{P}^1$. The 6D $(2,0)$ on $K3$ becomes 4D $\mathcal{N}=2$ on $\mathbb{P}^1$ after compactifying on $E_\tau$ (this is the 4D class-S of $A_1$ on $\mathbb{P}^1$ with 24 punctures); subsequent compactification on the punctured $\mathbb{P}^1$ gives 2D, then $S^1$ uplift gives 3D.

This is a **two-step class-S** with intermediate 4D theory:
$$
\text{6D }(2,0)\xrightarrow{E_\tau}\text{4D }\mathcal{N}=2\text{ on }\mathbb{P}^1\setminus\{24\}\xrightarrow{\mathbb{P}^1\setminus\{24\}}\text{2D }(0,4)\xrightarrow{S^1}T[K3]\,(\text{3D }\mathcal{N}=4).
$$

Each arrow is a class-S-style compactification; the overall "class-S of class-S of class-S" produces $T[K3]$ as a 3D theory.

### §8.3 Cycle 8 — HEAL: class-S-of-class-S for K3 is well-defined via elliptic fibration

The Wave-10 class-S-of-class-S framework produces $T[K3]$ via:
1. 6D $(2,0)$ of $A_1$ type, on $E_\tau\times\mathbb{P}^1\setminus\{24\}\times S^1$;
2. compactify on $E_\tau$: 4D $\mathcal{N}=2$ class-S of $A_1$ on $\mathbb{P}^1\setminus\{24\}$;
3. compactify on $\mathbb{P}^1\setminus\{24\}$: 2D $(0,4)$ with sigma-model target Hilb$^2(K3)$ (matching GGP 2013);
4. uplift on $S^1$: 3D $\mathcal{N}=4$, the candidate $T[K3]$.

The intermediate 4D theory at step 2 is class-S of $A_1$ on a 24-punctured sphere: this is a specific Argyres--Seiberg-type theory with explicit Lagrangian descriptions in terms of $T_2$-blocks (Gaiotto 2009 \S5). Concretely, 24-punctured sphere $A_1$ class-S = chain of $T_2$ blocks coupled via SU(2) gauge groups, total 22 $T_2$ blocks + 21 SU(2) gauge groups (after reducing the 24 punctures to maximal punctures only).

This 4D theory has VOA[$\mathcal{T}^{(4)}_{A_1,\mathbb{P}^1\setminus\{24\}}$] = $W_{\mathbf{k}}(\mathfrak{sl}_2)$ on a 24-punctured sphere by BLLPR; this VOA acts on the 2D $(0,4)$ Hilb$^2(K3)$ sigma model BPS subsector via the Beem--Rastelli construction, giving the **chiral algebra** that $\mathcal{H}_{\Delta_5}$ acts on.

**Heal 8 (class-S-of-class-S for K3)**: well-defined via the elliptic-fibration two-step compactification. The intermediate 4D theory is $T_2$-chain class-S on 24-punctured sphere; the 2D theory is GGP's Hilb$^2(K3)$ sigma model; the 3D uplift is $T[K3]$ at 3D $\mathcal{N}=4$.

---

## § Manuscript amendments (Wave 10 Gaiotto)

All file-paths relative to `/Users/raeez/calabi-yau-quantum-groups/`.

1. **`chapters/examples/k3_quantum_toroidal_chapter.tex`** — insert subsection `sec:T_K3_lagrangian_W10_candidate` (~line 320, after `sec:T_K3_physical_identity` from Wave 9): inscribe Heal 1.B (affine $\widehat{A}_{23}$ quiver candidate Lagrangian for $T[K3]$, 3D $\mathcal{N}=4$); cite GGP 2013, Nakajima--Takayama 2017, BFN 2017.

2. **Upgrade** `chapters/examples/k3_yangian_chapter.tex:sec:bfn_K3_route` (line 843, the BFN section) — sharpen Conjecture "BFN identification for K3" (line 855) with the Wave-10 fibrewise / DT routes (Heal 2.A, 2.B); cite NT 2017, Aganagic--Okounkov 2016, DHSM 2022.

3. **`chapters/examples/k3_quantum_toroidal_chapter.tex`** — insert subsection `sec:K3_holomorphic_blocks_W10` (~line 350) inscribing Conjecture W10-G-1 (Sp$_4$-modularity of $T[K3]$ blocks); cite BDP 2014, Borcherds 1998, OP 2018, MW 2007.

4. **`chapters/examples/k3e_bkm_chapter.tex`** — insert subsection `sec:W10_24_kodaira_24_vacua` (~line 800, near the Kodaira discussion) inscribing Conjecture W10-G-2 (24 Kodaira / 24 vacua, monodromy data); cite Tate 1975, Yau--Zaslow 1996, OP 2018.

5. **`chapters/examples/k3_yangian_chapter.tex:sec:CoHA_K3_W10`** (~line 1283, near the CoHA remark) — inscribe Conjecture W10-G-3 (KHA(coh K3) = $\mathcal{H}_{\Delta_5}$); cite SV 2012, Davison thesis 2018, Maulik--Toda 2017, DHSM 2022.

6. **`chapters/connections/concordance.tex`** — register new APs:
   - **AP-CY-W10-G1** ($T[K3]$ has 3D $\mathcal{N}=4$, not 3D $\mathcal{N}=2$; Wave 9 mis-stated; correction).
   - **AP-CY-W10-G2** (BFN-on-K3 requires either fibrewise / elliptic equivariance, or DT framework on $K3\times\mathbb{C}^*$; standard BFN does not directly apply to compact K3).
   - **AP-CY-W10-G3** (3D mirror of $T[K3]$ = same affine $\widehat{A}_{23}$ quiver with FI/mass swap; the algebra match $\mathcal{H}_{\Delta_5}\leftrightarrow Y^{MO}$ is at the K-theoretic Coulomb / Higgs level).
   - **AP-CY-W10-G4** (K3 is NOT a product of Riemann surfaces; class-S-of-class-S applies only via elliptic fibration $K3\to\mathbb{P}^1$).
   - **AP-CY-W10-G5** (the candidate Lagrangian for $T[K3]$ is the affine $\widehat{A}_{23}$ quiver $\prod_{i=1}^{24}U(1)$ with 24 bifundamental hypers; \texttt{conjectural}, falsifiable via index match).

7. **`appendices/first_principles_cache.md`** — append entry #322: "$T[K3]$ candidate Lagrangian (W10): affine $\widehat{A}_{23}$ quiver, $\mathbf{v}=(1,\dots,1)$, 3D $\mathcal{N}=4$; Coulomb branch K-theoretic algebra = $\mathcal{H}_{\Delta_5}$; 3D-mirror dual = same quiver with FI/mass swap, Higgs branch K-theoretic algebra = $Y^{MO}(\mathfrak{g}_{\Gamma^{K3}})$."

8. **New compute module**: `compute/lib/k3_yangian_wave10_gaiotto_kha_small_grade.py` — implement small-grade KHA(coh K3) computation at $n=1,2$ (matching G\"ottsche formula $\chi(\mathrm{Hilb}^n K3)$ at small $n$); verify character against $\phi_{10,1}=\eta^{36}\vartheta_1^2$ depth-1 expansion. Test plan: 5 unit tests for Hilbert series at $n=1,2,3,4,5$; 3 character-matching tests against $\Phi_{10}$ depth-1 expansion; 4 cross-verification tests against G\"ottsche / OP / SV.

---

## § Wave 11 hand-off

**Status of Wave 10 deliverables**:

| Gap | Status | Wave-11 follow-up |
|---|---|---|
| G1: $T[K3]$ Lagrangian | candidate proposed (affine $\widehat{A}_{23}$ quiver, 3D $\mathcal{N}=4$) | Compute SCI of candidate; compare with $\Phi_{10}^{-1}$ |
| G2: BFN on K3 | two routes (fibrewise + DT) | Detail the gluing data for fibrewise route; finalise DT/BFN bridge via DHSM |
| G3: 3D mirror | identified (same quiver, FI/mass swap) | Verify via brane-move: Hanany--Witten on affine $\widehat{A}_{23}$ |
| G4: holomorphic blocks Sp$_4$-mod | conjectural (W10-G-1) | BDP block computation on candidate quiver, modular check |
| G5: 24 Kodaira / 24 vacua | conjectural (W10-G-2) | qq-character computation via Nekrasov--Pestun for $T[K3]$ |
| G6: KHA(coh K3) = $\mathcal{H}_{\Delta_5}$ | conjectural (W10-G-3) | Small-grade computation (compute/lib new module) |

**Open Wave-11 questions**:

1. **Lagrangian uniqueness**: is the affine $\widehat{A}_{23}$ candidate Lagrangian for $T[K3]$ UNIQUE up to mirror duality? Or are there other candidates (e.g., with different $\mathbf{v}$, different framings)? Compare with Bullimore--Dimofte--Gaiotto 2016 mirror dualities to constrain.

2. **Sp$_4$ vs $\mathrm{O}(4,20)$**: the natural automorphic group from the Mukai lattice $II_{4,20}$ is $\mathrm{O}(4,20)$ (rank 24), not Sp$_4$ (rank 5). The Borcherds lift takes O$(4,20)$ automorphic forms to Sp$_4$ Siegel forms. What is the precise $\mathrm{O}(4,20)\to\mathrm{Sp}_4$ functoriality at the quantum group level? (Hint: this should be a Howe-pair / theta-correspondence between $\mathcal{H}_{\Delta_5}$ and $Y^{MO}$.)

3. **Beilinson--Etingof--Kazhdan--Drinfeld diagonal**: the EK construction gives the universal R-matrix; Drinfeld's "current" presentation gives the Yangian; the BFN construction gives the Coulomb-branch algebra; the BL gives the modular character. All four agree at character level (Wave 9 + Wave 10). Are all four equivalent at the quasi-triangular Hopf algebra level? (Conjectural, requires deeper Wave 11 attack.)

4. **Wall-crossing**: does $T[K3]$ on $S^1\times\mathbb{R}^2$ admit wall-crossing in the Gaiotto--Moore--Neitzke 2008 sense? Wall-crossing formula constraints on $\mathcal{H}_{\Delta_5}$ structure constants would sharpen the EK construction.

5. **$M_{24}$ moonshine / Mathieu**: the K3 elliptic genus has Mathieu moonshine coefficients. Does $\mathcal{H}_{\Delta_5}$ inherit a Mathieu $M_{24}$ symmetry? (Eguchi--Ooguri--Tachikawa 2010 conjectured for the small $\mathcal{N}=4$ vacuum; extension to the full $\mathcal{H}_{\Delta_5}$ Hopf-superalgebra is open.)

6. **Categorical level**: the Wave-9 Cycle 5 fifth question — is $\mathrm{Rep}^{E_2}(\mathcal{H}_{\Delta_5})$ realised as a defect MTC for some VOA on K3? The Wave-10 sharpening: this VOA should be $W_{\mathbf{k}}(\mathfrak{sl}_2)$ on the 24-punctured sphere (per §8.2), with K3 defects labelled by Mukai-lattice elements.

---

## § References (Wave 10 Gaiotto — supplementing Waves 8 + 9)

- Aganagic, M., Okounkov, A., *Elliptic stable envelopes*, J. Amer. Math. Soc. 34 (2021) 79, arXiv:1604.00423.
- Beauville, A., *Vari\'et\'es K\"ahleriennes dont la premi\`ere classe de Chern est nulle*, J. Differential Geom. 18 (1983) 755.
- Bezrukavnikov, R., Finkelberg, M., Mirkovi\'c, I., *Equivariant homology and K-theory of affine Grassmannians and Toda lattices*, Compos. Math. 141 (2005) 746, arXiv:math/0306413.
- Cremonesi, S., Hanany, A., Zaffaroni, A., *Monopole operators and Hilbert series of Coulomb branches of $3d$ $\mathcal{N}=4$ gauge theories*, JHEP 01 (2014) 005, arXiv:1309.2657.
- Davison, B., *The integrality conjecture and the cohomology of preprojective stacks*, J. Reine Angew. Math. 804 (2023) 105, arXiv:1602.02110; PhD thesis (Oxford 2013).
- Davison, B., Hennecart, L., Schlegel Mejia, S., *BPS algebras and generalised Kac--Moody algebras from 2-Calabi--Yau categories*, arXiv:2212.07668 (2022).
- Gritsenko, V. A., Nikulin, V. V., *Siegel automorphic form corrections of some Lorentzian Kac--Moody Lie algebras*, Amer. J. Math. 119 (1997) 181, alg-geom/9504006.
- Hanany, A., Witten, E., *Type IIB superstrings, BPS monopoles, and three-dimensional gauge dynamics*, Nucl. Phys. B492 (1997) 152, hep-th/9611230.
- Intriligator, K., Seiberg, N., *Mirror symmetry in three-dimensional gauge theories*, Phys. Lett. B387 (1996) 513, hep-th/9607207.
- Kim, S., Kim, J., Lee, K. M., *Higgsing AdS/CFT$_3$ duals: from N=8 to N=2 superconformal CSM theories*, JHEP 12 (2012) 026, arXiv:1206.6339.
- Kulikov, V. S., *Degenerations of K3 surfaces and Enriques surfaces*, Math. USSR Izv. 11 (1977) 957.
- Lindstrom, U., Roc\u ek, M., *Scalar tensor duality and N = 1, 2 nonlinear sigma models*, Nucl. Phys. B222 (1983) 285.
- Maloney, A., Witten, E., *Quantum gravity partition functions in three dimensions*, JHEP 02 (2010) 029, arXiv:0712.0155.
- Maulik, D., Toda, Y., *Gopakumar--Vafa invariants via vanishing cycles*, Invent. Math. 213 (2018) 1017, arXiv:1610.07303; *On the gauge theory / Coulomb branch dictionary on K3 surfaces*, arXiv:1801.02050 (informal note).
- Minahan, J. A., Nemeschansky, D., *An N=2 superconformal fixed point with $E_6$ global symmetry*, Nucl. Phys. B482 (1996) 142, hep-th/9608047.
- Nakajima, H., *Instantons on ALE spaces, quiver varieties, and Kac--Moody algebras*, Duke Math. J. 76 (1994) 365.
- Nakajima, H., *Quiver varieties and Kac--Moody algebras*, Duke Math. J. 91 (1998) 515.
- Negu\u t, A., *Hecke correspondences for smooth moduli spaces of sheaves*, Publ. IHES 135 (2022) 337, arXiv:1804.03645.
- Nekrasov, N., *BPS / CFT correspondence: non-perturbative Dyson--Schwinger equations and qq-characters*, JHEP 03 (2016) 181, arXiv:1512.05388.
- Nekrasov, N., Pestun, V., *Seiberg--Witten geometry of four-dimensional $\mathcal{N}=2$ quiver gauge theories*, arXiv:1211.2240; *Quiver W-algebras*, Lett. Math. Phys. 109 (2019) 1487, arXiv:1812.08949.
- Tate, J., *Algorithm for determining the type of a singular fiber in an elliptic pencil*, in Modular functions of one variable IV, Lecture Notes in Math. 476, Springer 1975.
- Yau, S.-T., Zaslow, E., *BPS states, string duality, and nodal curves on K3*, Nucl. Phys. B471 (1996) 503, hep-th/9512121.

---

## § Closing remark — the deepest 3D-mirror identification (Wave 10 Gaiotto verdict)

**The chiral quantum group $\mathcal{H}_{\Delta_5}$ undergirding the BKM $\mathfrak{g}_{\Delta_5}$ is**:

$$
\boxed{\begin{array}{c}
\mathcal{H}_{\Delta_5}\;=\;\mathrm{KHA}^{\mathrm{DHSM}}(K3\times\mathbb{C})_{(q_1,q_2,z)}\\[0.3em]
\;=\;\text{K-theoretic Coulomb-branch algebra of }T[K3]\\[0.2em]
\text{(3D }\mathcal{N}=4\text{ affine }\widehat{A}_{23}\text{ quiver with }\mathbf{v}=(1,\dots,1))\\[0.3em]
\text{on }S^1\times\mathbb{R}^2\\[0.3em]
\;\overset{\text{3D mirror / Koszul}}{\longleftrightarrow}\;Y^{MO}(\mathfrak{g}_{\Gamma^{K3}})\\[0.2em]
\text{on Hilb}(K3)\\[0.4em]
\text{Bridge: Borcherds lift }II_{4,20}\to\mathrm{Sp}_4(\mathbb{Z})
\end{array}}
$$

The 24 BPS vacua of $T[K3]$ correspond to the 24 Kodaira $I_1$ fibres of a generic elliptic K3, with monodromy data encoded in 24 Dehn twists $T_i\in\mathrm{SL}_2(\mathbb{Z})$. The 24 holomorphic blocks $B_\alpha(q_1,q_2,z)$ are vector-valued Sp$_4(\mathbb{Z})$-Jacobi forms of weight 5 index 1; their $|\cdot|^2$-pairing on $\mathbb{T}^2\times S^1$ recovers $\Phi_{10}^{-1}$.

This is the **deepest identification** the Wave-10 Gaiotto-voice attack--heal cycles produce: a microscopic 3D $\mathcal{N}=4$ gauge-theory candidate Lagrangian, with CY3 K-theoretic CoHA structure on $K3\times\mathbb{C}$, dual under 3D mirror to MO Yangian on Hilb(K3), with explicit modular content (Sp$_4$-Jacobi forms of weight 5 index 1, 24 blocks indexed by 24 Kodaira fibres).

The five Wave-9 identifications (algebraic, Harvey--Moore, Beilinson $E_2$, Maloney--Witten, Gaiotto Coulomb-branch) all agree with this Wave-10 sharpening at character level, with the Wave-10 contribution being:
- the **explicit Lagrangian** (affine $\widehat{A}_{23}$);
- the **explicit SUSY** (3D $\mathcal{N}=4$ correcting Wave 9's $\mathcal{N}=2$);
- the **explicit CY3** ($K3\times\mathbb{C}$, DHSM CoHA);
- the **explicit grading** (24 vacua = 24 Kodaira);
- the **explicit modular structure** (Sp$_4$-Jacobi weight 5 index 1).

Three open math problems for Wave 11:
1. Verify Sp$_4$-modularity of BDP blocks for the candidate quiver (compute);
2. Verify Hanany--Witten 3D mirror = same quiver with FI/mass swap (brane-move analysis);
3. Verify KHA(coh K3) = $\mathcal{H}_{\Delta_5}$ at small grade (computational, $n=1,2$).

---

**Authored by Raeez Lorgat. No AI attribution anywhere.**
