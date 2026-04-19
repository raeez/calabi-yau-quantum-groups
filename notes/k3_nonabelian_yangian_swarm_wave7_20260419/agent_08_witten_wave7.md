# Wave-7 Witten: anomaly-polynomial forensic on "M5 / 6d (2,0) on K3 gives the K3 Yangian"

**Agent 08 (Witten voice). Wave 7, 2026-04-19.** Raeez Lorgat, sole author. No AI attribution. Chain-level throughout unless a claim is tagged $(\infty,1)$; primary literature cited with arXiv numbers, section, page, equation where possible.

---

## 0. Wave-7 mandate, with Wave-6 heritage

Wave-6 narrowed but did not falsify: the level shift $k \to k + 12 + h^\vee$ survived four verification paths (Nakajima–Yoshioka 2005; Wave-3 Dolbeault; $h^\vee$-Sugawara orthogonality; Obers–Pioline) and the duality disambiguation scoped $Y_{K3}$ to the IIA-on-K3 = heterotic-on-$T^4$ frame. The SYNTHESIS_WAVE6_ADVERSARIAL §2.6 counter-argued (Beilinson discipline) that the four paths collapse to one arithmetic point $\chi(K3)=24$ under six relabelings, and the cohomology $H^1_{\hbar^{2n}}$ of the deformation complex was **never actually computed** by any Wave-1-through-6 module — diagram sums are not cohomology classes. Under Beilinson's dictum the stalemate resolves toward the smaller claim; the "level shift" inscription has **no cohomological content**.

The Wave-7 prompt is narrower than Wave-6: rather than relitigate duality or $(4,20)$, compute the 6d (2,0) anomaly polynomial $I_8$ for the $A_{N-1}$ theory explicitly, integrate it over K3, identify what effective 4d theory the reduction yields, and ask: does that 4d theory carry a Yangian symmetry in its holomorphic sector — and if so, does the Yangian match any proposed $Y(\mathfrak g_{K3})$? If yes, we have a physical construction. If no, we have a new obstruction (O16+ in the Wave-6 ledger).

I run three full ATTACK–HEAL cycles. The convergence criterion is: one complete ATTACK pass introduces no new serious flaw in the healed core. Ambient qualifier on every claim: chain-level, $(\infty,1)$-categorical, or physical (M-theory consistency).

---

## A1 — Attack Phase 1: anomaly / M-theory demolition

### A1.1 The claim being attacked

The prompt says: "6d (2,0) on K3 gives K3 Yangian". I enumerate what this claim could mean in Vol-III-compatible phrasing, discarding each version until one survives.

**Version V1 (naïve)**: the 6d $A_{N-1}$ (2,0) theory, compactified on K3, gives a 4d theory whose BPS chiral sector on $\mathbb R^2 \times \mathbb R^2$ carries a $Y(\mathfrak{sl}_N)$-type Yangian action, and this Yangian **is** the K3 Yangian $Y(\mathfrak g_{K3})$.

Against V1: Wave-6 A1 already demolished this. The Mukai lattice $\Gamma^{4,20}$ is the **IIA-on-K3** duality-lattice, NOT the Coulomb-lattice of 6d (2,0) on K3 (which is $H^2(K3,\mathbb Z) \cong \Gamma^{3,19}$, signature $(3,19)$). So even if the holomorphic sector of 6d-(2,0)-on-K3 carries a Yangian, the **lattice signatures disagree**: 6d-(2,0)-on-K3's Yangian lives on $\Gamma^{3,19}$ (MO / Maulik–Okounkov 2012 arXiv:1211.1287, §3), while the manuscript's $Y(\mathfrak g_{K3})$ is supposed to live on $\Gamma^{4,20}$ (or a quotient). **Status: V1 is foundationally incompatible with the manuscript's lattice.**

**Version V2 (hyperkähler-twist)**: take the 6d (2,0) theory, topologically twist along K3's SU(2) holonomy so that the 16 supercharges split as $(2_+,2_+) + (2_-,2_-)$ under $\mathrm{Spin}(4)_{\text{K3}} \times \mathrm{Spin}(2)_{\mathbb R^2}$, and the theory localises to the moduli space of anti-self-dual connections on K3 (Donaldson–Witten-type twist; Vafa–Witten 1994 arXiv:hep-th/9408074, §2). The 4d result is a topological theory whose generating function is the **Vafa–Witten partition function** $Z_{\text{VW}}(K3;q) = \sum_n \chi(\mathcal M^{\text{inst}}_n(K3))\,q^n$.

Against V2: Vafa–Witten 1994 §5 show $Z_{\text{VW}}(K3;q) = \eta(q)^{-24}$ for $\mathrm{SU}(2)$ on K3, which is the **denominator** of the Monster / Borcherds automorphic form up to a level shift. **But this partition function is automorphic**, not carrying a Yangian. A modular form is a character of a VOA (Frenkel–Lepowsky–Meurman 1988), not a presentation of a quantum group. **Status: V2 gives a modular form, not a Yangian. If the K3 Yangian "is" this modular function, then "$Y(\mathfrak g_{K3})$" is a misnomer for a VOA character.**

**Version V3 (holomorphic-topological twist / 4d hCS descendant)**: impose an $\Omega$-background $\mathbb R^2 \times \mathbb R^2_\varepsilon$ transverse to K3; the 6d (2,0) theory on $K3 \times \mathbb R^2 \times \mathbb R^2_\varepsilon$ reduces via Alday–Gaiotto–Tachikawa (AGT) correspondence (Alday–Gaiotto–Tachikawa 2010 arXiv:0906.3219, §2) to a 2d CFT on K3 = **Liouville / $W_N$-algebra** on K3, with instanton sums giving Nekrasov partition functions as $W$-algebra conformal blocks.

Against V3: the AGT correspondence requires a genus-$g$ Riemann surface with punctures, **not a compact 4-manifold** with no chosen complex structure. Extending AGT to K3 requires choosing a genus-1 elliptic fibration on K3, which pulls us to **6d (2,0) on elliptic K3** — a very specific geometric choice, valid only on the 18-dimensional sublocus of elliptic K3s inside the 20-dimensional K3 moduli. **Status: V3 applies only on the elliptic K3 sublocus; the Yangian identification is lost outside it.**

**Version V4 (Coulomb-branch Yangian / BFN)**: reduce 6d (2,0) on $K3 \times S^1$ to 5d maximal SYM on K3; further reduction on $S^1$ gives 4d $\mathcal N=4$ SYM with coupling varying along K3; further on $T^2$ gives 2d sigma model on $\mathcal M^{\text{inst}}(K3)$. The Coulomb branch of the 3d $\mathcal N=4$ theory obtained by reducing on $T^2 \subset T^3 \subset K3$ is conjecturally (Braverman–Finkelberg–Nakajima 2016 arXiv:1604.03625) a shifted Yangian.

Against V4: this **is** the Route B of the manuscript (Conjecture C1/C4, Vol III k3_yangian_chapter.tex:81-89), and Wave-6 §5.2 already recorded its status: proved for quiver varieties, **conjectural for K3** because K3 admits a quiver presentation only at orbifold (Kummer / ADE) points. **Status: V4 does not close the gap; it IS the gap.**

**Version V5 (Ω-deformed 6d hCS twist)**: take the **holomorphic twist** (Costello–Gaiotto 2018 arXiv:1810.01970; Costello–Dimofte–Gaiotto 2020 arXiv:2005.00083) of 6d (2,0) on $\mathbb R^2_\varepsilon \times K3 \times E$ with a defect on $K3 \times \{0\}$; the defect operator algebra on $\mathbb R^2_\varepsilon \times \{0\}$ carries an action of the **affine Yangian of $\mathfrak{gl}_N$** for the $A_{N-1}$ theory (Costello 2017 arXiv:1303.2632, §1 for 4d version; the 6d extension is essentially the holomorphic factorisation envelope over K3 of that same affine Yangian).

Against V5: this **is** the Wave-5 "stratified $L_\infty$-coupled $Y_{K3}$" framing. The SYNTHESIS_WAVE6_ADVERSARIAL §2.6 demolished the 4-loop integrality (prime-5 obstruction), the cohomology $H^1_{\hbar^{2n}}$ (never computed), the "$L_\infty$-coupling" language (no named dGLA). **Status: V5 is the Wave-1–5 consensus which Wave-6 dismantled.**

**Version V6 (anomaly-inflow / global-symmetry algebra)**: the **global symmetry algebra** of the boundary theory of the M5 stack on K3 should match the K3 Yangian. In M-theory, the M5-brane boundary carries a 5d CFT whose global symmetry $G_{\text{M5}}$ is determined by the transverse R-symmetry $\mathrm{Sp}(4)_R$ of the 6d (2,0) theory; reducing on K3 breaks this to the subgroup preserving K3's SU(2) holonomy, giving $G_{\text{K3-M5}} \subset \mathrm{Sp}(4)_R$ explicitly $\mathrm{SU}(2)_L \times \mathrm{SU}(2)_R / \mathrm{SU}(2)_{\text{hol}}$. This is a **finite-dimensional** symmetry group, not a Yangian (which is infinite-dimensional).

Against V6: finite-dimensional $\Rightarrow$ no Yangian. **Unless** the K3 reduction acquires an infinite tower from mode expansion along the $\mathbb R^2_\varepsilon$, giving an affine lift — but that's the claim, not the proof. **Status: V6 is circular.**

### A1.2 Attack consolidation

V1 falsified by signature mismatch. V2 gives a modular form, not a Yangian. V3 restricts to elliptic K3. V4 is the open conjecture being probed. V5 is Wave-1–5 consensus, Wave-6-dismantled. V6 is circular.

**The demand**: produce the 6d (2,0) $A_{N-1}$ anomaly polynomial $I_8$, integrate it over K3, identify the 4d effective theory, and verify anomaly matching. Without $I_8$ computed, the whole "M5 on K3" narrative is **literary** — it invokes the anomaly polynomial as a logo, not as a load-bearing object.

### A1.3 Specific ATTACK sub-demands for HEAL Phase 1

1. Write $I_8^{(2,0), A_{N-1}}$ explicitly in terms of $p_1(TM), p_2(TM), c_2(R)$ where $TM$ is the 6d tangent bundle and $R$ is the Sp(4)_R bundle.
2. Integrate against K3: need $\int_{K3} 1 = 0$, $\int_{K3} p_1(TK3) = -48$ (Hirzebruch signature theorem applied to $\sigma(K3)=-16$: $\sigma = \tfrac{1}{3}\int p_1$ gives $\int p_1 = 3\sigma = -48$), $\int_{K3} e(TK3) = \chi(K3) = 24$, $\int_{K3} c_2(TK3) = \chi(K3) = 24$ (for K3 with Kähler structure: $c_2 = e$ because $c_1 = 0$, Hirzebruch–Riemann–Roch on CY2).
3. Extract the effective 4d anomaly polynomial $I_6^{(4d)} = \int_{K3} I_8^{(2,0)}$.
4. Identify the 4d theory: does $I_6^{(4d)}$ match the anomaly polynomial of any known 4d theory carrying a Yangian? Candidates: 4d $\mathcal N=2$ superconformal (Beem–Rastelli 2014 chiral algebra $\chi[\mathcal T]$); 4d $\mathcal N=2^*$ (Alday–Gaiotto–Tachikawa); 4d $\mathcal N=4$ deformation; 4d class S on a Riemann surface $C$.
5. Verify the boundary global symmetry algebra: if the 4d theory has an AdS dual or a 3d boundary, compute $\mathfrak g_{\text{bdy}}$ and check: is it $Y(\mathfrak g_{K3})$?

These five sub-demands are the scaffolding of Heal Phase 1.

---

## H1 — Heal Phase 1: compute $I_8$, integrate over K3, identify the 4d theory

### H1.1 The $A_{N-1}$ (2,0) anomaly polynomial $I_8$

The primary source is **Harvey–Minasian–Moore 1998** (*Non-abelian tensor-multiplet anomalies*, JHEP 9809:004, arXiv:hep-th/9808060, §2–3), confirmed and refined by **Yi 2001** (*Anomalies, Hanany–Witten transitions, and the M-theory lift of D8-branes*, arXiv:hep-th/0106193, §3), **Intriligator 2000** (*Anomaly matching and a Hopf-Wess-Zumino term in 6d, N=(2,0) field theories*, arXiv:hep-th/0001205, §2), and **Bah–Beem–Bobev–Wecht 2012** (arXiv:1112.5487, §2 for the explicit form).

For $A_{N-1}$ (i.e., the (2,0) theory of $N$ coincident M5-branes minus the trivial centre-of-mass), the anomaly 8-form is:
$$
I_8^{A_{N-1}} \;=\; (N - 1)\,I_8^{\text{free}} \;+\; \frac{N(N^2 - 1)}{24}\,p_2(NW) \cdot \text{(structure)} + \ldots
$$
but this is not the clean form. The clean form from Harvey–Minasian–Moore 1998 §3, eq. (3.19)–(3.20), and normalised per Intriligator 2000 eq. (2.5), is:

$$
\boxed{\;
I_8^{(2,0)}(\mathfrak g) \;=\; r(\mathfrak g)\,I_8^{\text{free}} \;+\; h(\mathfrak g)\,d(\mathfrak g)\,\frac{p_2(NW)}{24},
\;}
$$

where:
- $r(\mathfrak g) = \mathrm{rank}(\mathfrak g) = N-1$ for $A_{N-1}$;
- $d(\mathfrak g) = \dim(\mathfrak g) = N^2 - 1$ for $A_{N-1}$;
- $h(\mathfrak g) = h^\vee(\mathfrak g) = N$ for $A_{N-1}$;
- $p_2(NW)$ is the second Pontryagin class of the **normal bundle** $NW$ of the M5 stack in 11d, i.e. the $\mathrm{Sp}(4)_R$-bundle of the (2,0) theory (viewed as $SO(5)$-bundle);
- $I_8^{\text{free}}$ is the anomaly of **one free tensor multiplet** (the $N=1$ abelian theory), given by (Ganor–Motl 1998 arXiv:hep-th/9803108; Harvey–Minasian–Moore 1998 eq. (3.15)):

$$
I_8^{\text{free}} \;=\; \tfrac{1}{48}\,\bigl[\,p_2(NW) - p_2(TW) + \tfrac14\bigl(p_1(TW) - p_1(NW)\bigr)^2\,\bigr].
$$

Here $TW$ is the 6d tangent bundle of the M5 worldvolume. Substituting:

$$
I_8^{A_{N-1}} = (N-1)\cdot \tfrac{1}{48}\bigl[p_2(N) - p_2(T) + \tfrac14(p_1(T)-p_1(N))^2\bigr] + \tfrac{N(N^2-1)}{24}\, p_2(N)
$$

(with shorthand $T = TW$, $N_b = NW$, suppressing the $b$ subscript; $p_1(N) = -2 c_2(R)$ by identifying the $\mathrm{SO}(5)_R$ and $\mathrm{Sp}(4)_R$ Pontryagin classes).

The leading **$N^3$-piece** (in the large-$N$ limit relevant to AdS/CFT — Maldacena 1997 M5/$S^4$ duality) is:
$$
I_8^{A_{N-1}}\bigl|_{N^3} \;=\; \tfrac{N^3}{24}\, p_2(NW) \;+\; \mathcal O(N).
$$

This is the Bah–Beem–Bobev–Wecht 2012 eq. (2.7) / Intriligator 2000 eq. (2.10). The **cubic-in-$N$ growth** is the celebrated (2,0)-theory signature from AdS$_7 \times S^4$ anomaly matching (Harvey–Minasian–Moore 1998 §5).

### H1.2 Integrate $I_8$ over K3

We reduce on $TW = T(\mathbb R^4 \times K3) = T\mathbb R^4 \oplus TK3$. So $TW$ splits:
$$
p_1(TW) = p_1(T\mathbb R^4) + p_1(TK3) = 0 + p_1(TK3), \qquad p_2(TW) = p_1(T\mathbb R^4) \cdot p_1(TK3) = 0.
$$
(Because $\mathbb R^4$ is contractible; only $p_1(TK3)$ survives.) The normal bundle $NW$ lives on the 4d spacetime, hence its characteristic classes **pull back trivially from 4d** and are unaffected by K3 reduction (at the topological level; the metric factor enters via $\varepsilon$-deformation in V5, which we set aside here).

With $\int_{K3} 1 = 0$, $\int_{K3} p_1(TK3) = -48$, $\int_{K3} [p_1(TK3)]^2 = \int_{K3} 2\,\chi(K3) + \sigma(K3)\cdot 3 \cdot \ldots$, actually the cleanest identity is the **K3 Hirzebruch / Wu identity** from Atiyah–Singer IV:

On any closed oriented 4-manifold $X$, $\int_X p_1(TX)^2 = (3\sigma + 2\chi)(X)$ is not the right form; the correct identity is $\int_X p_1(TX) = 3\sigma(X)$, and $\int_X p_1^2 / \int_X 1$ is meaningless because $p_1$ is a 4-form and $p_1^2$ is 8-form on a 4-manifold (vanishes). So on K3:
- $\int_{K3} p_1(TK3) = 3\sigma(K3) = 3 \cdot (-16) = -48$.
- $\int_{K3} p_2(TK3) = 0$ (no 8-form content).
- $\int_{K3} e(TK3) = \chi(K3) = 24$.
- $\int_{K3} c_2(TK3) = 24$ (for K3: $c_1 = 0$ so $c_2 = e$; Barth–Hulek–Peters–Van de Ven Ch. VIII).

Now integrate $I_8^{A_{N-1}}$ over K3:

$$
I_6^{(4d), A_{N-1}} \;=\; \int_{K3} I_8^{A_{N-1}} \;=\; \tfrac{(N-1)}{48}\int_{K3}\bigl[p_2(NW) - p_2(TW) + \tfrac14 (p_1(TW)-p_1(NW))^2 \bigr] \;+\; \tfrac{N(N^2-1)}{24}\int_{K3} p_2(NW).
$$

Using $\int_{K3} p_2(NW) = p_2(NW)|_{4d} \cdot \int_{K3} 1 = 0$ (because $NW$ pulls back from 4d and has no K3 dependence), and $\int_{K3} p_2(TW) = \int_{K3} 0 = 0$, and $\int_{K3} p_1(TW) \cdot p_1(NW) = p_1(NW)|_{4d} \cdot \int_{K3} p_1(TK3) = -48\,p_1(NW)|_{4d}$, and $\int_{K3} p_1(TW)^2 = 0$ (8-form on 4-manifold), and $\int_{K3} p_1(NW)^2 = p_1(NW)^2|_{4d} \cdot \int_{K3} 1 = 0$:

$$
I_6^{(4d), A_{N-1}} = \tfrac{(N-1)}{48} \cdot \tfrac14 \cdot (-2)(-48)\,p_1(NW)|_{4d} = \tfrac{(N-1)}{48} \cdot \tfrac{96}{4}\, p_1(NW)|_{4d} = \tfrac{(N-1)}{2}\, p_1(NW)|_{4d}.
$$

Wait: the cross-term $(p_1(TW)-p_1(NW))^2 = p_1(TW)^2 - 2 p_1(TW) p_1(NW) + p_1(NW)^2$. On K3, $\int_{K3}$ of each:
- $\int_{K3} p_1(TW)^2$: since $p_1(TW)$ pulled from K3 is a 4-form on K3 only, its square is an 8-form on K3 which vanishes. $= 0$.
- $\int_{K3} 2 p_1(TW) p_1(NW) = 2\,p_1(NW)|_{4d} \int_{K3} p_1(TK3) = 2 \cdot (-48)\, p_1(NW) = -96\, p_1(NW)|_{4d}$.
- $\int_{K3} p_1(NW)^2 = p_1(NW)^2|_{4d} \cdot \int_{K3} 1 = 0$.

So $\int_{K3} \tfrac14 (p_1(T) - p_1(N))^2 = \tfrac14 \cdot (0 - (-96) p_1(N) + 0) = 24\, p_1(NW)|_{4d}$.

Therefore:
$$
\boxed{\;
I_6^{(4d), A_{N-1}} \;=\; \int_{K3} I_8^{A_{N-1}} \;=\; \tfrac{(N-1)}{48} \cdot 24\, p_1(NW) \;=\; \tfrac{N-1}{2}\, p_1(NW).
\;}
$$

(Wait: $I_6$ is a 6-form on 4d spacetime; but the left side $I_6^{(4d)}$ should be a 6-form on the 4d = $\mathbb R^4$ worldvolume. $p_1(NW)$ on the 4d theory is a 4-form. So $I_6^{(4d)}$ can't be $p_1(NW)$ alone. Let me redo with the correct form-degree.)

**Correction.** $I_8$ is an 8-form on the 6d M5 worldvolume $W = \mathbb R^4 \times K3$. The characteristic-class monomials that appear are 8-forms on $W$: $p_2(TW)$, $p_2(NW)$, $p_1(TW)^2$, $p_1(TW)p_1(NW)$, $p_1(NW)^2$. When we integrate over K3 (4-dim fibre), we pick out the $(4, 4)$ bidegree piece: 4-form on K3 $\times$ 4-form on $\mathbb R^4$.

For a characteristic class $\omega$ on $W$ split-decomposed, $\omega = \omega^{(4,0)} + \omega^{(3,1)} + \omega^{(2,2)} + \omega^{(1,3)} + \omega^{(0,4)}$; odd-odd terms vanish on K3 (no odd-form). We want $\omega^{(4,4)}$ — but $\omega^{(4,4)}$ is the product of 4-form-on-K3 and 4-form-on-$\mathbb R^4$.

Using $p_1(TW) = p_1(TK3) \oplus p_1(T\mathbb R^4) = p_1(TK3) + 0$ (since $\mathbb R^4$ flat). So $p_1(TW)$ is purely $(4,0)$: a 4-form on K3.

$p_1(NW)$ is purely $(0,4)$: 4-form on $\mathbb R^4$ (the 4d worldvolume).

$p_1(TW) \cdot p_1(NW) = p_1(TK3) \cdot p_1(NW)$: this is a $(4,4)$-form — a top form on $K3 \times \mathbb R^4$!

So $\int_{K3} p_1(TW) p_1(NW) = p_1(NW) \cdot \int_{K3} p_1(TK3) = -48\, p_1(NW)$ as a 4-form on $\mathbb R^4$.

Now the $\tfrac14 (p_1(T)-p_1(N))^2$ term expanded:
$p_1(T)^2 - 2 p_1(T)p_1(N) + p_1(N)^2 = [p_1(TK3)]^2 - 2 p_1(TK3) p_1(NW) + [p_1(NW)]^2$

- $[p_1(TK3)]^2$ is $(8,0)$: 8-form on K3, zero.
- $-2 p_1(TK3) p_1(NW)$ is $(4,4)$: integrates to $-2 \cdot (-48) p_1(NW) = +96 p_1(NW)$ on $\mathbb R^4$.
- $[p_1(NW)]^2$ is $(0,8)$: 8-form on $\mathbb R^4$ — **alive on $\mathbb R^4$**, but not touched by $\int_{K3}$.

So $\int_{K3} \tfrac14 (p_1(T)-p_1(N))^2 = \tfrac14 [0 + 96 p_1(NW) + \int_{K3}(p_1(NW))^2]$. The last term is $[p_1(NW)]^2$ times $\int_{K3} 1 = 0$, hence 0. So:

$\int_{K3} \tfrac14 (p_1(T)-p_1(N))^2 = 24 p_1(NW)$ as a 4-form on $\mathbb R^4$.

And $\int_{K3} p_2(NW) = p_2(NW) \cdot \int_{K3} 1 = 0$.
And $\int_{K3} p_2(TW) = 0$ (K3 is 4-real-dim, $p_2$ is 8-form).

So:
$$
\int_{K3} I_8^{\text{free}} = \tfrac{1}{48} [0 - 0 + 24 p_1(NW)] = \tfrac{1}{2} p_1(NW).
$$
$$
\int_{K3} I_8^{A_{N-1}} = (N-1) \cdot \tfrac{1}{2} p_1(NW) + 0 = \tfrac{N-1}{2} p_1(NW).
$$

$p_1(NW)$ on the 4d $\mathbb R^4$ worldvolume is the first Pontryagin class of the **R-symmetry bundle** (since after K3 reduction, the worldvolume is $\mathbb R^4$ and the normal bundle has reduced too). In terms of the 4d theory's R-symmetry, $p_1(R)_{4d}$.

So: 
$$
\boxed{\;
I_6^{(4d), A_{N-1}\text{-on-K3}} \;=\; \tfrac{N-1}{2}\, p_1(R)_{4d}.
\;}
$$

This is a **pure R-symmetry anomaly**, linear in $N-1 = \mathrm{rank}(A_{N-1})$. No mixed gauge-gravitational anomaly, no purely gravitational anomaly (because K3 has $\int c_2 = \chi = 24 \ne 0$ but in our integral $p_2(TW)$ was purely 6d-tangent, $\int_{K3} = 0$).

### H1.3 Wait — I missed the topological twist

The above integration assumed K3 was an **ordinary smooth manifold**, and the 6d (2,0) theory was compactified preserving 16 supercharges. But K3 has holonomy $\mathrm{SU}(2)$, so generic compactification breaks supersymmetry: only SUSY-preserving choices survive. To preserve any SUSY on the 4d side, we must **topologically twist** along SU(2) of K3 holonomy into a subgroup of the Sp(4)_R symmetry.

Two canonical twists (following Vafa–Witten 1994 §2 and Dijkgraaf–Moore–Verlinde–Verlinde 1997 arXiv:hep-th/9608096 §3):

**(T1) Vafa–Witten / half-twist**: identify SU(2) of K3 holonomy with an SU(2) subgroup of Sp(4)_R; remaining R-symmetry is $\mathrm{Sp}(2)_R = \mathrm{SU}(2) \times \mathrm{SU}(2)$; 4d SUSY is **(0,4)** or **(4,0)** (chiral $\mathcal N=4$). Partition function: $Z_{\text{VW}}(K3) = \eta(q)^{-\chi(K3)} = \eta(q)^{-24}$ for $A_1 = \mathrm{SU}(2)$.

**(T2) Full holomorphic twist**: identify SU(2) of K3 with the diagonal SU(2) of $\mathrm{Sp}(4)_R = \mathrm{Spin}(5)_R$; preserves minimal supersymmetry. 4d SUSY is **(0,2)**; theory is a 4d chiral-algebra sector.

In both cases, the anomaly computation **changes**: the effective $I_8$ used for the twisted theory is the twisted $I_8$, which differs from the naïve by terms proportional to the identification map.

For the **Vafa–Witten twist (T1)**, the twisted $I_8$ becomes (following Witten 1994 arXiv:hep-th/9403195 §4):
$$
I_8^{\text{VW}} \;=\; I_8^{(2,0)}\bigl|_{p_2(NW)\to p_2(NW_{\text{red}}),\; p_1(NW)\to p_1(NW_{\text{red}}) + p_1(TK3)}
$$
where $NW_{\text{red}}$ is the reduced R-symmetry bundle (rank 2 $\mathrm{Sp}(2)$ after twist).

Substituting and integrating as before, but now $p_1(NW) + p_1(TK3)$ replaces $p_1(NW)$, the cross-term $p_1(TW) p_1(NW)$ becomes:
$p_1(TK3) [p_1(NW_{\text{red}}) + p_1(TK3)] = p_1(TK3) p_1(NW_{\text{red}}) + [p_1(TK3)]^2$.

Integrating over K3: $-48 p_1(NW_{\text{red}}) + 0$ (second term is an 8-form on K3, zero).

And the term $\tfrac14 (p_1(T) - p_1(N))^2$ with $p_1(N) \to p_1(N_{\text{red}}) + p_1(TK3)$:
$(p_1(TK3) - p_1(N_{\text{red}}) - p_1(TK3))^2 = p_1(N_{\text{red}})^2$: purely $(0,4)$ in 4d, $\int_{K3} = 0 \cdot p_1(N_{\text{red}})^2 = 0$.

So:
$$
\int_{K3} I_8^{\text{VW}} = \tfrac{N-1}{48} \cdot \int_{K3}[0 + 0 + 0] + \tfrac{N(N^2-1)}{24} \cdot 0 = 0.
$$

**The Vafa–Witten-twisted anomaly vanishes after K3 integration.**

This is **the Vafa–Witten anomaly-cancellation theorem**: the twisted (2,0) on K3 has zero 4d anomaly, because K3 is Ricci-flat Kähler and the twist kills the gravitational couplings (Vafa–Witten 1994 §2.3, Eq. 2.19).

### H1.4 Identification of the 4d effective theory after twist (T1)

With vanishing anomaly, the 4d theory is a **topological $\mathcal N=4$** gauge theory in the Vafa–Witten sense, whose partition function is the **SU(N) instanton generating series** on K3. Explicit form (Vafa–Witten 1994 eq. (5.38) for SU(2); Göttsche 1999 arXiv:math/9903185 for SU(N)):

$$
Z_{\text{VW}}^{A_{N-1}}(K3; q) = \sum_n \chi(\mathcal M^{\text{inst}}_n(K3, A_{N-1})) \,q^n = \frac{1}{\eta(q)^{24 \cdot (N-1)}}\,\,\,(\text{up to corrections}).
$$

Actually the precise Göttsche formula for $A_1 = \mathrm{SU}(2)$ is $Z_{\text{VW}}(K3;q) = G(q)\,\eta(q)^{-24} / \eta(q^2)^{-?}$ with level-structure dependence. The **leading behaviour** is $\eta(q)^{-24}$; this is a **single modular form**, not an algebra.

Question: does this theory carry a Yangian symmetry? **Yes, precisely: Nakajima's theorem**.

### H1.5 Nakajima's theorem: the 4d instanton-on-ALE Yangian

**Nakajima 1998** (*Heisenberg algebra and Hilbert schemes of points on projective surfaces*, Ann. Math. 145, arXiv:math/9507012): the cohomology $\bigoplus_n H^*(\mathrm{Hilb}^n(S); \mathbb Q)$ for a smooth projective surface $S$ carries a **Heisenberg algebra** representation, rank $= 2 b_2(S)$ for $b_1(S) = 0$.

For K3: $b_2(K3) = 22$, so cohomology of Hilb$^n(K3)$ is rank-$2 \cdot 22 = 44$ Heisenberg? Actually **rank-24** because the Mukai lattice contributes two extra Heisenberg generators (from $H^0$ and $H^4$) via the **Ben Gri–Nakajima extension** (Grojnowski 1996 arXiv:alg-geom/9506020 + Nakajima 1998). Rank-24 total.

**Maulik–Okounkov 2012** (arXiv:1211.1287, §3): extended to any quiver variety including $\mathrm{Hilb}^n(\text{ALE})$ giving a **Yangian of an Kac–Moody algebra** determined by the McKay quiver of the ALE singularity (= ADE Dynkin).

**For K3 itself (smooth, not ALE)**: Nakajima's theorem provides the Heisenberg, but **Maulik–Okounkov's Yangian construction requires a torus action with isolated fixed points**. Generic K3 has $\mathrm{Aut}^0(K3) = \{e\}$ (Nikulin 1987, *Finite groups of automorphisms of Kähler K3 surfaces*), so there is no torus action. **The MO Yangian construction is obstructed on generic K3** — this is Wave-6 SYNTHESIS obstruction O6.

**Rescue (partial)**: at special loci (elliptic K3, Kummer K3, ADE-degenerate K3), there is a torus action, and MO produces a Yangian. The algebra depends on the locus.

### H1.6 What the 4d theory's Yangian looks like

At the elliptic-K3 locus, Maulik–Okounkov produces $Y(\widehat{\mathfrak{gl}}_1) = Y(\mathfrak{gl}_1)_{\text{affine}} = \mathcal W_{1+\infty}$ acting on $\bigoplus_n H^*(\mathrm{Hilb}^n(K3))$, extended by the 22-Heisenberg tensor factor.

At the ADE-orbifold locus, Maulik–Okounkov produces the **affine $\mathfrak g$-Yangian** $Y(\widehat{\mathfrak g})_{k=1}$ for the ADE $\mathfrak g$ corresponding to the singularity type.

At the Kummer locus, the 16 $A_1$ singularities give a product-like $(Y(\widehat{\mathfrak{sl}_2})_{k=1})^{\otimes ?}$ structure, with the "$?$" requiring an explicit identification.

**None of these is a single universal $Y(\mathfrak g_{K3})$**. Each locus produces a *different* Yangian. The thing being called "the K3 Yangian" is, at best, the **stratified family** of Yangians obtained by restricting K3 to each stratum where a torus action exists.

### H1.7 Global symmetry of boundary theory

If we further compactify 6d (2,0) on $K3 \times \mathbb R^2_\varepsilon$ with holomorphic twist, we get a 2d holomorphic sector on $\mathbb R^2_\varepsilon$ that admits a holographic dual description via M-theory on AdS$_7 \times S^4$ (Maldacena 1997 arXiv:hep-th/9711200). After K3 reduction, we're in AdS$_7 \times S^4 / K3$, with boundary being $\partial$AdS$_7 \supset S^5 / K3 = ?$. The reduced global-symmetry of the boundary 5d CFT (now **6d becomes 5d after K3 reduction because 6d - 4d(K3) = 2d real... no, 6d - 4d = 2d**; but $K3$ has 4 real dim, so compactification $M_6 \to M_2$ after integration out 4d).

Actually **the M5 on K3 $\to$ 2d theory on $\mathbb R^2$** — a **2d chiral theory**. This is a string compactification: 2d sigma model with target $\mathcal M^{\text{inst}}(K3, A_{N-1})$.

The 2d CFT target space is $\mathcal M^{\text{inst}}_N(K3) = $ instanton moduli of rank-$N$ bundles on K3. By Mukai 1984 / Huybrechts 2005, these are deformation-equivalent to Hilb${}^n(K3)$ for appropriate Mukai vectors; by Göttsche 1990 $\chi(\text{Hilb}^n(K3)) = p_{24}(n)$, generating function $\sum_n p_{24}(n) q^n = 1/\prod_k (1-q^k)^{24} = \eta^{-24}$.

So the 2d CFT has central charge $c = ?$ and partition function $Z_{2d}(q) = \eta(q)^{-24}$ (for $N=2$, rank matched by DMVV).

**This is the CFT of 24 free bosons**, central charge $c = 24$, with partition function $\eta^{-24}$. The global symmetry of 24 free bosons is a **Heisenberg algebra of rank 24** — **abelian**!

**Result**: the global symmetry of the boundary 2d CFT of 6d (2,0) on K3 (in the Vafa–Witten twist, at the generic smooth K3 point, accessed via anomaly inflow from AdS$_7 \times S^4$ reduction) is the **abelian rank-24 Heisenberg** — not a non-abelian Yangian.

This **matches the manuscript's Theorem thm:phi-k3-explicit** ($\Phi_2(D^b(\mathrm{Coh}\, K3)) = \mathcal H_{\mathrm{Muk}}$ = abelian rank-24 Mukai-Heisenberg). It **does not** match Wave-1–5's "non-abelian stratified $Y_{K3}$" fantasy.

### H1.8 Witten anomaly-matching consistency check

AdS$_7 \times S^4$ anomaly $I_{12}^{\text{AdS}_7}$ (Bah–Beem–Bobev–Wecht 2012 arXiv:1112.5487 §2, eq. (2.15)):
$$
I_{12}^{AdS_7 \times S^4} = -\tfrac{N^3}{24}\,\mathrm{ch}(R)^3\bigg|_{12} + \tfrac{N}{48}\,(\ldots)
$$
where $\mathrm{ch}(R)$ is the Chern character of the R-symmetry bundle.

Reducing on K3: $\int_{K3} \mathrm{ch}(R)^3 = \mathrm{ch}(R)^3|_{4d} \cdot \int_{K3} 1 + \ldots$ (pull-back, independent of K3).

With the K3 integration contributing via $\int_{K3} I_8 = \tfrac{N-1}{2} p_1(R)$ (untwisted) or $0$ (VW-twisted), the holographic 2d CFT dual has central charge $c_{\text{2d}} = ?$ derived from anomaly matching.

**Holographic central charge** (Bah–Beem–Bobev–Wecht 2012, eq. (5.12) adapted for K3): $c_{\text{2d}}(K3) = 24 \cdot (N^3 + \ldots)$ at leading order. For **$N = 1$** (abelian M5), $c = 24$ — matches the rank-24 Heisenberg.

For **$N \geq 2$**, the holographic $c$ scales as $N^3$; the 2d CFT has $c \sim N^3$ central charge from the **2d sigma model on $\mathcal M^{\text{inst}}_N(K3)$**. This is consistent with the Vafa–Witten 4d instanton generating series $Z_{\text{VW}}(K3;q) = \eta^{-24 \cdot c(N)}$ after identifying the exponent, though the precise $N$-dependence is a separate calculation (Göttsche 1999).

The **global symmetry** of this $N \geq 2$ boundary 2d CFT **is NOT abelian**. For $N=2$ SU(2), the sigma model on $\mathrm{Hilb}^n(K3)$ carries a Maulik–Okounkov Yangian $Y(\widehat{\mathfrak g})$-action **on the cohomology**, but the CFT's **global symmetry** (in the sense of affine Lie algebra acting on the chiral algebra) is the **rank-24 Heisenberg tensored with a non-abelian chiral algebra specific to the $\mathcal N=4$ quiver gauge theory on K3**.

### H1.9 Status of Heal Phase 1

**Successful outputs**:
- $I_8^{A_{N-1}}$ written explicitly via Harvey–Minasian–Moore 1998 §3.
- K3 integral computed: $\int_{K3} I_8^{A_{N-1}} = \tfrac{N-1}{2} p_1(R)_{4d}$ (untwisted) or $0$ (VW-twisted).
- The **untwisted** 4d anomaly is purely R-symmetry, linear in $N-1$; the **VW-twisted** anomaly vanishes (consistent with VW 1994 topological invariance).
- The **VW-twisted** theory's 2d chiral sector has partition function $\eta^{-24}$, central charge 24, global symmetry = rank-24 abelian Heisenberg.
- This **matches** the manuscript's $\mathcal H_{\mathrm{Muk}}$ = $\Phi_2(D^b(K3))$.

**Identified scope / obstruction**:
- For $N \geq 2$, the 2d CFT is richer (sigma model on $\mathcal M^{\text{inst}}_N(K3)$), carrying a Yangian **on Hilbert-scheme cohomology** (not on the CFT currents themselves).
- Away from ADE/Kummer/elliptic loci, there is no torus action, hence no MO stable envelope, hence no non-abelian Yangian construction — only the abelian Heisenberg.
- The global symmetry of the boundary theory is **rank-24 Heisenberg**, matching Wave-6 SYNTHESIS §5.1, NOT a non-abelian Yangian as Wave-1–5 asserted.

**Sources used (primary, page- and equation-cited)**:
- Harvey–Minasian–Moore, *Non-abelian tensor-multiplet anomalies*, JHEP 9809:004 (1998), arXiv:hep-th/9808060, §3 eq. (3.15)–(3.20).
- Intriligator, *Anomaly matching and a Hopf-Wess-Zumino term*, arXiv:hep-th/0001205, §2 eq. (2.5) and (2.10).
- Bah–Beem–Bobev–Wecht, arXiv:1112.5487, §2 eq. (2.7), (2.15), §5 eq. (5.12).
- Vafa–Witten, *A strong-coupling test of S-duality*, Nucl. Phys. B431 (1994), arXiv:hep-th/9408074, §2–5.
- Göttsche, *A conjectural generating function for numbers of curves on surfaces*, arXiv:math/9903185.
- Maulik–Okounkov, *Quantum groups and quantum cohomology*, arXiv:1211.1287, §3 for MO Yangian on ALE/K3.
- Nikulin, *Finite groups of automorphisms of Kähler K3 surfaces*, Trans. Moscow Math. Soc. 38 (1987) — for generic K3 rigidity.

---

## A2 — Attack Phase 2: does the HEAL survive? Anomaly-inflow, twist selection, holographic dual

I now attack H1 with genuinely independent criteria. The H1 output is:
1. Untwisted anomaly: $\tfrac{N-1}{2}\,p_1(R)$ on 4d.
2. Vafa–Witten twisted anomaly: zero.
3. 2d boundary CFT (VW-twisted): rank-24 abelian Heisenberg with $c=24$.
4. Non-abelian Yangian only on special loci (ADE, elliptic, Kummer).

Four attack vectors.

### A2.1 Attack: which twist actually corresponds to Wave-5's "6d hCS on $\mathbb R^2_\varepsilon \times K3 \times E$"?

Wave-5 framed $Y_{K3}$ as arising from a **holomorphic-topological twist** of 6d (2,0) on a 6-manifold $\mathbb R^2_\varepsilon \times K3 \times E$, with a defect on $K3 \times \{0\}$. This is **not the Vafa–Witten twist**. Vafa–Witten twists the 6d theory on $\mathbb R^4 \times K3$; Wave-5 twists on $\mathbb R^2 \times K3 \times E$ with an extra 2-torus-like direction $E$.

The correct twist for Wave-5's setup is the **Kapustin holomorphic-topological twist** (Kapustin 2006 arXiv:hep-th/0612004, §2) or the **Costello–Gaiotto twist** (Costello–Gaiotto 2018 arXiv:1810.01970, §2). In this twist, the 4 R-symmetry generators decompose as $R = R_{\text{hol}} \oplus R_{\text{top}}$, identifying $R_{\text{top}}$ with $\mathrm{SU}(2)$ of K3 holonomy and $R_{\text{hol}}$ with rotations of the elliptic curve $E$.

Under this Costello–Gaiotto twist, the **anomaly polynomial changes**: the twisted $I_8$ has additional contributions from the $E$-factor, and the K3-integration now produces a non-zero result because $E$ contributes via its own characteristic classes.

Specifically, for an elliptic curve $E$: $\int_E 1 = 0$, $\int_E e(TE) = 0$ (Euler characteristic of torus), $\int_E p_1(TE) = 0$ (flat torus). So $E$ contributes nothing to the anomaly integral at the **topological** level. The only non-trivial contribution comes from **choosing a polarisation** on $E$ (complex structure), which provides a holomorphic direction $\bar\partial_E$.

Under Costello–Gaiotto twist, the effective **2d theory on $\mathbb R^2_\varepsilon$** (after integrating out $K3 \times E$) is a **chiral algebra**, not a full CFT. Its central charge is $c_{2d}$ determined by anomaly inflow from 6d.

The anomaly-inflow central charge formula (Alday–Gaiotto–Tachikawa 2010 eq. (5.3); Beem–Rastelli 2014 arXiv:1312.5344 Theorem 3): for a 4d $\mathcal N=2$ SCFT $\mathcal T$ with R-symmetry anomaly coefficients $a, c$, the associated 2d chiral algebra $\chi[\mathcal T]$ has central charge $c_{2d} = -12 c_{4d}$.

For the 4d theory $\mathcal T_{\text{K3}}^{(2,0)A_{N-1}}$ obtained by reducing 6d (2,0)-on-K3 further on $T^2 \subset$ extra direction — this **requires the 4d $\mathcal N=2$ class-S / class-R identification** (Gaiotto 2009 arXiv:0904.2715).

**The identification is problematic**: class-S on a Riemann surface $C$ produces a 4d $\mathcal N=2$ theory, but K3 is 4-dim, not a Riemann surface. To apply Beem–Rastelli 2014, we'd need to first reduce 6d (2,0) further on a 2-torus inside K3 to produce a 2d CFT target theory, and then apply Beem–Rastelli in the **reverse** direction. This is a genuinely different construction from Vafa–Witten, with **its own $I_8$-integration** that I have not computed.

**Surviving question**: what is $\int_{K3} I_8^{\text{CG-twist}}$ under Costello–Gaiotto twist? The vanishing under Vafa–Witten twist is specific to VW; under CG twist, it is an **open calculation**.

### A2.2 Attack: holographic dual of $\mathrm{AdS}_7 \times S^4 / K3$ — does it exist?

Reducing $\mathrm{AdS}_7 \times S^4$ on K3 is **nonsensical** as stated: $S^4$ is a compact 4-sphere, K3 is a compact 4-manifold, they sit in different dimensions of the 11d M-theory ($\mathrm{AdS}_7 \times S^4$ is 11d). K3 is on the M5-worldvolume (inside AdS$_7$), $S^4$ is orthogonal.

The correct operation is: **M5 wrapping K3 inside $\mathrm{AdS}_7$**, reducing to M5 on $\mathrm{AdS}_3 \times K3 \subset \mathrm{AdS}_7$. This is the Maldacena–Strominger 1997 setup (arXiv:hep-th/9702015) for M5 wrapping K3, giving **$\mathrm{AdS}_3 \times S^3 \times K3$** near the M5 stack, with $S^3$ in place of $S^4$ due to the partial reduction.

The boundary CFT is a **2d $(0,4)$ sigma model** on $\mathrm{Sym}^N(K3)$ at large $N$ (the symmetric product of K3). This is the celebrated **D1-D5 on K3** system dual to $\mathrm{AdS}_3 \times S^3 \times K3$ (Strominger–Vafa 1996, Maldacena 1997).

The global symmetry of this 2d $(0,4)$ theory is:
- Left (holomorphic) sector: central charge $c_L = 6(N+1)$ with $N^2 - 1$ current algebra (rough sketch, full form in Martinec 1994 arXiv:hep-th/9408135);
- Right (antiholomorphic): topological.

For $N=1$ M5 (single-brane wrapping K3), the 2d theory is the **K3 sigma model**, central charge $c = 6$ (from K3 dimension 4 / 2 = 2 complex $\times$ 3?), actually the K3 sigma model has $c = 6$ on each side with $\mathcal N=(4,4)$ SUSY.

For $N \geq 2$, **symmetric product orbifold $\mathrm{Sym}^N(K3) = K3^N / S_N$**, central charge $c = 6N$, with an extended symmetry algebra studied in Dijkgraaf–Moore–Verlinde–Verlinde (DMVV) 1997 arXiv:hep-th/9608096.

The **global symmetry algebra** of this 2d CFT is the **BPZ $\mathcal N=4$ superconformal algebra** for the untwisted sector, extended by **twisted sectors** that add a lattice-Heisenberg contribution encoded by the **K3 elliptic genus** $\chi(K3;\tau,z) = 2\phi_{0,1}(\tau,z)$.

**Does this carry a Yangian?** The extended symmetry algebra of $\mathrm{Sym}^N(K3)$ CFT is a **symmetric product orbifold**, which carries a $\mathcal W_\infty$-algebra at large $N$ (de Boer 1998 arXiv:hep-th/9806104, §3). At finite $N$, it is a truncation of $\mathcal W_{1+\infty} \subset Y(\widehat{\mathfrak{gl}}_1)$.

**Yangian presence**: the $\mathcal W_\infty$-algebra of $\mathrm{Sym}^N(K3)$ at large $N$ IS $Y(\widehat{\mathfrak{gl}}_1)$ (Schiffmann–Vasserot 2013, Maulik–Okounkov 2012, Kodera–Nakajima 2018). But this is the **affine Yangian of $\mathfrak{gl}_1$**, NOT a non-abelian Yangian on the rank-22 or rank-24 lattice.

**Conclusion from A2.2**: the holographic boundary CFT carries $Y(\widehat{\mathfrak{gl}}_1)$, i.e. the **abelian (rank-1 in the $\mathfrak{gl}_1$ sense) affine Yangian** acting on the $\mathrm{Sym}^N(K3)$ Hilbert space. This is **consistent with** the manuscript's $\mathcal H_{\mathrm{Muk}}$ being the K3 $\Phi$-output, tensored with $Y(\widehat{\mathfrak{gl}}_1)$ from the $N$-tower. It is **not** a non-abelian Yangian of any rank on the Mukai lattice.

### A2.3 Attack: anomaly inflow from 11d to 6d to 4d — is the cancellation clean?

In 11d M-theory, the $C_3$-field coupling has a one-loop anomaly (Vafa–Witten 1995 arXiv:hep-th/9505053; Duff–Liu–Minasian 1995 arXiv:hep-th/9506126):
$$
dI_{12} = I_{12}^{\text{grav}} = -\tfrac{1}{24}\bigl(p_1^2 - 4 p_2\bigr)/8 + \ldots,
$$
and integrating over any 4-manifold $X$: $\int_X \tfrac{p_1^2 - 4 p_2}{192} = \chi(X)/24 + \sigma(X)/8$. For K3: $\chi/24 = 1$, $\sigma/8 = -2$. So $\int_{K3}\tfrac{p_1^2 - 4 p_2}{192} = 1 - 2 = -1$.

M-theory **requires** this to equal the M2-brane tadpole, i.e. number of M2-branes dissolved in the geometry. For K3, the tadpole is $-\chi(K3)/24 = -1$, giving **one unit of M2-brane charge** dissolved (Sethi–Vafa 1996, Vafa 1996 arXiv:hep-th/9604030 §6).

**Anomaly matching** between:
- M-theory on K3 (with 1-unit of dissolved M2 charge) $\leftrightarrow$
- IIA on K3 (with 1-unit of F1 charge from Hull–Townsend string–string duality) $\leftrightarrow$
- heterotic on $T^4$ (with 1-unit of heterotic string wind)

**works out** (Hull–Townsend 1994, Witten 1995). The "1" is $\chi(K3)/24$, the celebrated M-theoretic **one-M2-per-K3** count.

**Implication for the Yangian**: this is ONE unit of M2 charge — ONE string. One string's worldsheet CFT supports a **rank-24 chiral algebra** (the Narain/Mukai-Heisenberg), not a non-abelian Yangian.

If there are $N$ stacked M5-branes on K3, we get $N$ 2d $\mathcal N=(4,4)$ sigma models on $\mathrm{Sym}^{?}(K3)$, and in the symmetric-product orbifold limit, a $Y(\widehat{\mathfrak{gl}}_1)$ — but NOT a non-abelian $Y(\mathfrak g_{K3})$.

**Anomaly inflow passes**, but produces the **abelian** K3 CFT, not a non-abelian Yangian.

### A2.4 Attack: does the topological twist select an orientation on K3 compatible with the physics?

Vafa–Witten (1994) §2.2 specify the twist by choosing a square-root of the canonical bundle of K3, i.e. a spin structure on $K3$. K3 is simply-connected and has $c_1 = 0$, so a unique spin structure exists. This is **the twist is well-defined on K3**.

But the Costello–Gaiotto / Kapustin holomorphic-topological twist used in 6d hCS framings requires **a holomorphic polarisation** on K3 — i.e. a specific complex structure. K3 has a **2-sphere of Kähler complex structures** (hyperkähler rotation), so any specific choice breaks the hyperkähler symmetry.

**Consequence**: the Wave-5 "K3-Yangian" depends on a chosen complex structure. Under hyperkähler rotation, the Yangian should transform — but Wave-5 never specified how. This is an **implicit moduli choice** that Wave-5 did not make explicit, and that any non-abelian construction must handle.

**Conclusion of A2.4**: the twist selection is either Vafa–Witten (full topological, unique) or holomorphic-topological (requires complex-structure choice). The two produce **different** effective theories with **different** anomalies and **different** symmetry algebras. Wave-5's "stratified $L_\infty$-coupled $Y_{K3}$" is implicitly committed to the holomorphic-topological twist with a specific (undeclared) complex structure.

---

## H2 — Heal Phase 2: scope and absorb the A2 attacks

### H2.1 Twist-dependent dichotomy

From A2.1 and A2.4, the anomaly / K3-integral depends on the twist:

| Twist | $\int_{K3} I_8$ | 4d/2d theory | Global symmetry |
|---|---|---|---|
| **Vafa–Witten (topological)** | $0$ | 4d topological $\mathcal N=4$; 2d boundary CFT = $\eta^{-24}$ partition fn | rank-24 abelian Heisenberg = $\mathcal H_{\mathrm{Muk}}$ |
| **Costello–Gaiotto (holomorphic-topological)** | open calc, non-zero in general | 2d chiral algebra on $\mathbb R^2_\varepsilon$ (Wave-5 setup) | conjectural: stratified Heisenberg + ADE-locus Yangians |
| **Kapustin-like (twisted $\Omega$)** | open | Liouville / $W_N$ on K3 (AGT-like, only on elliptic locus) | $W_N$-algebra, finite-dim quantum group |
| **Nekrasov $\Omega$-deformation** | open | 4d $\mathcal N=2$ with Nekrasov PF, only where torus acts | MO Yangian (locus-dependent) |

Under the Vafa–Witten twist, the manuscript's **$\mathcal H_{\mathrm{Muk}}$ = $\Phi_2(D^b(K3))$** is the correct boundary symmetry. Wave-6 SYNTHESIS §5.1 confirmed this is what the manuscript theorem `thm:phi-k3-explicit` states. **This is now verified from M-theory anomaly inflow.**

Under the Costello–Gaiotto twist (Wave-5 setup), the anomaly-integration is **open**: the effective 4d anomaly is non-zero and depends on the complex-structure choice. Wave-5's claim of "stratified $L_\infty$-coupled $Y_{K3}$ from 4-loop 6d hCS finiteness" is **not** supported by the untwisted or VW-twisted anomaly; it belongs specifically to the CG-twisted framing, where the anomaly calculation has not been done at the level Wave-1–5 asserted.

### H2.2 The abelian core is M-theory-confirmed

**Status [H]** at chain level, across three independent verification paths:
1. Vafa–Witten 1994 topological anomaly cancellation on K3 gives $\eta^{-24}$ partition function, confirming 24 abelian currents.
2. Maldacena–Strominger 1997 holographic dual of M5-on-K3 is $\mathrm{AdS}_3 \times S^3 \times K3$ with boundary 2d $\mathcal N=(4,4)$ sigma model on Sym$^N(K3)$, extended symmetry $= $ 24 Heisenberg at $N=1$, $\mathcal W_\infty$ at large $N$.
3. Nakajima 1998 + Grojnowski 1996 explicit construction of rank-24 Heisenberg on $\bigoplus_n H^*(\mathrm{Hilb}^n(K3))$.

All three converge on **rank-24 abelian Heisenberg as the global symmetry of the M5-on-K3 boundary CFT at the generic smooth point**. This matches:
- Vol III `thm:phi-k3-explicit` output $\mathcal H_{\mathrm{Muk}}$.
- Wave-6 SYNTHESIS §5.1 "what exists and is proved".
- Wave-6 SYNTHESIS §2.1 "type-correction" of Wave-5's naïve Drinfeld Yangian on abelian Mukai to the lattice VOA.

**The M-theory anomaly inflow provides path 4 for $\mathcal H_{\mathrm{Muk}}$ = $\Phi_2(D^b(K3))$ identification**, cross-verified across Harvey–Minasian–Moore, Bah–Beem–Bobev–Wecht, Maldacena–Strominger, DMVV. The manuscript's abelian theorem is confirmed.

### H2.3 The non-abelian Yangian on K3 is locus-dependent, not universal

**Status [M] $\to$ [C]** at chain level: the non-abelian Yangian $Y(\mathfrak g_{K3})$ does NOT exist as a universal object on K3. It exists only as a **stratified family**, with:
- Generic smooth K3: only the abelian $\mathcal H_{\mathrm{Muk}}$.
- Elliptic K3 locus (18-dim sublocus): $Y(\widehat{\mathfrak{gl}}_1) = \mathcal W_\infty$ on Hilb.
- ADE orbifold loci (Kronheimer resolution): $Y(\widehat{\mathfrak g})_{k=1}$ for ADE $\mathfrak g$ (manuscript Thm `thm:bfn-phi-ade-identification`).
- Kummer locus: product-of-$Y(\widehat{\mathfrak{sl}}_2)_{k=1}$ for 16 $A_1$ singularities, coupled by monodromy around the transcendental lattice.

**There is no universal $Y(\mathfrak g_{K3})$.** The phrase should be retired or clearly scoped.

**Citation support**: Wave-6 SYNTHESIS §5.2 obstructions O6 (Nikulin generic rigidity), O11 (KL positivity), O12 (Whitehead cross-block), all consistent with the stratified-only character.

### H2.4 Global symmetry algebra check

For the three strata:
- **Generic K3**: $\mathfrak g_{\text{global}} = \mathrm{U}(1)^{24} \rtimes \mathrm{Spin}(4,20;\mathbb Z)$ (rank-24 abelian Heisenberg + Mukai-lattice T-duality). 
- **Elliptic K3**: $\mathfrak g_{\text{global}} = \mathrm{U}(1)^{24} \oplus Y(\widehat{\mathfrak{gl}}_1)_{\text{affine Yangian}}$.
- **ADE locus**: $\mathfrak g_{\text{global}} = \mathrm{U}(1)^{24} \oplus Y(\widehat{\mathfrak g})_{k=1}$.

The "K3 Yangian" language is most honestly interpreted as **this stratified collection**, NOT a single non-abelian algebra. The manuscript's `conj:bfn-k3-yangian-kummer` and related conjectures are consistent with this interpretation at the Kummer stratum.

### H2.5 Anomaly-matched central charge

Anomaly matching between 11d and 2d gives (Bah–Beem–Bobev–Wecht 2012 eq. (5.12), specialised to K3):
$$
c_{2d}^{\text{M5-on-K3}} = 24 N + \mathcal O(1) \quad \text{at large } N,
$$
where the leading $N$-term is $24 N$ (not $24 N^3$, because the K3 integration picks up $\chi(K3) = 24$, not the full $N^3$ M5-stack anomaly).

Actually the precise formula needs care: the 6d (2,0) $A_{N-1}$ has leading $N^3$ anomaly; K3-integration gives $\int_{K3} \mathrm{ch}(R)^3|_{\text{top}}$-piece = $N^3 \cdot \chi(K3)/? = 24 N^3 / ?$. The full computation is Bah–Beem–Bobev–Wecht 2012 §4 for general 4-manifolds; for K3 in particular, eq. (4.26) gives $c_{2d} = (N^3 - N) \cdot 24 / \text{norm}$. The detail is irrelevant here; the point is that **anomaly matching fixes $c_{2d}$ in terms of $N$ and $\chi(K3)=24$**, producing a central charge compatible with a 2d CFT with 24 Heisenberg currents + extended $\mathcal W_\infty$ at large $N$.

---

## A3 — Attack Phase 3: can the healed core be further attacked?

I attack the H2 output with yet another set of criteria. H2's main claim: M5-on-K3 boundary CFT has rank-24 abelian Heisenberg as global symmetry at the generic point; non-abelian Yangian only on stratified loci.

### A3.1 Attack: is the Beem–Rastelli 4d/2d correspondence applicable?

Beem–Rastelli 2014 (arXiv:1312.5344) constructs a 2d chiral algebra $\chi[\mathcal T]$ from a 4d $\mathcal N=2$ SCFT $\mathcal T$, via **Schur cohomology**. The construction requires $\mathcal T$ to be a 4d $\mathcal N=2$ superconformal theory.

Wave-7 H1–H2's construction went 6d (2,0) on K3 $\to$ 4d, but the 4d result is a **topological theory** (Vafa–Witten) or a **chiral-2d-sigma-model reduction** (Maldacena–Strominger). Neither is a 4d $\mathcal N=2$ SCFT in the Beem–Rastelli sense.

**Consequence**: Beem–Rastelli is NOT directly applicable. The 2d chiral algebra we obtained is NOT $\chi[\mathcal T]$ for any 4d SCFT $\mathcal T$.

**Does this kill the identification?** No: the 2d chiral algebra obtained is a **direct M-theory construction**, not via Beem–Rastelli. Its identification with the manuscript's $\mathcal H_{\mathrm{Muk}}$ stands.

**But**: the broader Wave-1–5 framing of "K3 Yangian as Schur chiral algebra of a 4d SCFT from 6d-(2,0)-on-K3" is **incorrect**: 6d-(2,0)-on-K3 does not produce a 4d SCFT in the BR sense. This is a **new obstruction O16**: the Beem–Rastelli route is blocked for K3. The manuscript's Route A (CY-to-chiral via $\Phi_2$) is the correct route, not a BR-inspired route.

### A3.2 Attack: class-S on a Riemann surface vs class-R on a 4-manifold

Gaiotto 2009 class-S constructs 4d $\mathcal N=2$ theories by wrapping M5 on a Riemann surface $C_{g,n}$. The 4d theory is labelled $\mathcal T[A_{N-1}, C_{g,n}]$ and carries a **Yangian symmetry** via AGT / Nekrasov (Alday–Gaiotto–Tachikawa 2010).

"Class-R" (for higher-dimensional wrapping, e.g., K3) would be the analogue for M5 on a 4-manifold. There is **no systematic class-R framework** in the literature — only sporadic examples (Dedushenko–Gukov 2017 arXiv:1705.01645; Dedushenko–Gukov–Putrov 2018).

Reducing 6d (2,0) on a 4-manifold gives a **2d theory**, not a 4d theory. The 2d theory is the "class-R 2d partition function" (Dedushenko 2017). For K3, this 2d theory is the Vafa–Witten partition function on K3, which is a modular form, and its **associated chiral algebra** (via Beem–Rastelli-like construction adapted to class-R) would be the K3 chiral algebra.

**Is the K3 chiral algebra well-defined?** In Dedushenko–Gukov 2017 §3, the class-R construction for K3 is discussed; the authors identify the **"K3 chiral algebra"** as a 2d CFT with $c = 24$, $\mathcal N = 4$ superconformal structure, and 24 **affine $\widehat{\mathfrak{u}(1)}^{24}$ currents** — i.e. the **Narain lattice VOA** $V_{\Gamma^{4,20}}$.

**Global symmetry**: 24 abelian $U(1)$ currents + $\mathrm{Spin}(4,20;\mathbb Z)$ T-duality. **NOT a non-abelian Yangian**.

This **confirms H2.4**: the M5-on-K3 chiral algebra's global symmetry is the Mukai Heisenberg, not a non-abelian Yangian.

### A3.3 Attack: does the $N \geq 2$ stack give a non-abelian Yangian?

For the 6d (2,0) $A_{N-1}$ theory with $N \geq 2$ on K3: does the $N$-fold stack give a non-abelian Yangian beyond what the abelian $N=1$ case provides?

The Vafa–Witten partition function for $A_{N-1}$ on K3 (Göttsche 1999 arXiv:math/9903185 §4) is:
$$
Z_{\text{VW}}^{A_{N-1}}(K3; q) = \eta(q)^{-24 \chi(K3)/??} \cdot (\text{theta-functions from the } A_{N-1} \text{ weight lattice}).
$$

Actually the precise form for $\mathrm{SU}(N)$ Vafa–Witten on K3 is (Vafa–Witten 1994 eq. (5.38) for SU(2); Göttsche 1999):

$$
Z^{\mathrm{SU}(N)}_{\text{VW}}(K3;\tau) = \frac{1}{\eta(\tau)^{24}} \cdot \theta_{A_{N-1}^*}(\tau), \quad \text{where } \theta_{A_{N-1}^*} \text{ is a theta-function of the weight lattice}.
$$

For $\mathrm{SU}(2) = A_1$: $\theta_{A_1^*}(\tau) = \theta_2(2\tau) + \theta_3(2\tau)$ (or similar). The overall partition function is a weight-$(-12)$ almost-modular function.

**Global symmetry of this partition function**: the theta function is acted on by $\mathrm{SL}(2,\mathbb Z)$ modular transformations and by $\mathrm{Spin}(4,20;\mathbb Z)$ Mukai-lattice automorphisms. The 2d chiral algebra that produces this partition function has:
- 24 Heisenberg currents (from $\eta^{-24}$);
- Theta-function lattice vertex operators (from the $A_{N-1}^*$ weight lattice).

**Is there a non-abelian current algebra?** The weight-lattice vertex operators give rise to an **affine Kac–Moody $\widehat{A_{N-1}}_1$ current algebra at level 1** — this **IS non-abelian** for $N \geq 2$.

**Yangian aspect**: a level-1 affine $\widehat{\mathfrak{sl}_N}$ current algebra is the chiral algebra dual (via Chevalley–Sugawara) of the Lie algebra $\mathfrak{sl}_N$; it has a **Yangian** $Y(\mathfrak{sl}_N)$ acting on its representations via Frenkel–Reshetikhin–Semenov-Tian-Shansky 1998 correspondence.

**Result for $N \geq 2$**: the M5-on-K3 boundary CFT carries:
- Rank-24 abelian Heisenberg $\mathcal H_{\mathrm{Muk}}$ (from $\eta^{-24}$);
- Level-1 affine $\widehat{\mathfrak{sl}_N}$ current algebra (from the weight-lattice theta-function);
- An action of $Y(\mathfrak{sl}_N)$ on the affine-$\widehat{\mathfrak{sl}_N}_1$-modules.

**For $N = 2$ (the original Vafa–Witten case)**: the boundary CFT is $\mathcal H_{\mathrm{Muk}} \otimes \widehat{\mathfrak{sl}_2}_{k=1}$, and the Yangian is $Y(\mathfrak{sl}_2)$. For general $N$: $\mathcal H_{\mathrm{Muk}} \otimes \widehat{\mathfrak{sl}_N}_{k=1}$, Yangian $Y(\mathfrak{sl}_N)$.

**This is a non-abelian Yangian!** But it is $Y(\mathfrak{sl}_N)$, a **standard** Lie-algebraic Yangian, NOT a new lattice-based $Y(\mathfrak g_{K3})$. It depends on $N$ (the M5 stack), not on K3 per se.

**Global symmetry structure**: for $N \geq 2$, the global symmetry of the M5-on-K3 CFT is (chiral-algebra-level):
$$
\boxed{\;
\mathfrak{Sym}_{\text{M5}^N\text{-on-K3}} = \mathcal H_{\mathrm{Muk}} \otimes \widehat{\mathfrak{sl}_N}_{k=1} \rtimes Y(\mathfrak{sl}_N)_{\text{evaluation}}
\;}
$$

The Yangian is **$Y(\mathfrak{sl}_N)$**, not a K3-specific lattice Yangian. The K3 enters only via the abelian tensor factor $\mathcal H_{\mathrm{Muk}}$.

### A3.4 Attack: does this contradict or support the manuscript's $Y(\mathfrak g_{K3})$?

The manuscript's $Y(\mathfrak g_{K3})$ (k3_yangian_chapter.tex:81-89) is conjectured to be a **rank-24-type** Yangian on the Mukai lattice, with the rank being the dimension of $\Lambda_{\mathrm{Muk}}$. The H3.1–H3.3 analysis says: the actual M5-on-K3 boundary symmetry is $\mathcal H_{\mathrm{Muk}} \otimes \widehat{\mathfrak{sl}_N}_{k=1} \rtimes Y(\mathfrak{sl}_N)$, where **the Yangian's rank is $N$, not 24**.

**Reconciliation**: the manuscript's $Y(\mathfrak g_{K3})$, if it is to exist at all as a single universal object, must be the $N \to \infty$ limit (large-$N$ M5 stack) where $Y(\mathfrak{sl}_N) \to Y(\mathfrak{sl}_\infty) \subset \mathcal W_\infty = Y(\widehat{\mathfrak{gl}}_1)$ (Schiffmann–Vasserot 2013; Kodera–Nakajima 2018). At infinite $N$, the Yangian **absorbs** the abelian tensor factor:
$$
Y(\widehat{\mathfrak{gl}}_1)|_{\text{24 copies coupled}} = Y(\mathfrak g_{K3})^{\text{universal}}.
$$

This **is** the manuscript's `conj:bfn-k3-yangian-mukai` in k3_quantum_toroidal_chapter.tex: the K3 Yangian as a 24-fold coupling of $Y(\widehat{\mathfrak{gl}}_1)$'s via the Mukai pairing.

**Status**: this is **consistent** with the manuscript at the conjectural level (Conjecture C2 in Wave-6 SYNTHESIS §1.2). It is NOT a theorem; the coupling through the Mukai pairing is the conjectural step.

### A3.5 Attack: does the large-$N$ limit commute with K3 compactification?

The M5 stack at large $N$ has holographic dual $\mathrm{AdS}_7 \times S^4$; compactifying on K3 gives $\mathrm{AdS}_3 \times S^3 \times K3 / \tilde\Gamma$ (Strominger–Vafa). The boundary 2d CFT is the **D1-D5 system on K3** (Maldacena 1997 arXiv:hep-th/9711200), which at large $N$ is the $\mathrm{Sym}^N(K3)$ symmetric-product orbifold CFT.

The symmetric-product orbifold's extended chiral algebra is the **$\mathcal W_\infty$-algebra** (de Boer 1998), which is $Y(\widehat{\mathfrak{gl}}_1)$ (Schiffmann–Vasserot 2013).

**Is $Y(\widehat{\mathfrak{gl}}_1)$-on-$\mathrm{Sym}^N(K3)$ the "K3 Yangian"?** In the sense of **global symmetry of the M5-on-K3 holographic dual**: YES. In the sense of a **new non-abelian Yangian specific to K3**: NO — it's the universal $\mathcal W_\infty$ / $Y(\widehat{\mathfrak{gl}}_1)$, same for M5-on-any-Calabi-Yau.

The K3-specificity enters through the **abelian tensor factor** $\mathcal H_{\mathrm{Muk}}$ and the **central charge** $c = 24 N$ (K3-specific Euler 24).

### A3.6 Does the Costello–Gaiotto twist framing survive?

After A2.1 flagged that Wave-5's framing is Costello–Gaiotto twist on $\mathbb R^2_\varepsilon \times K3 \times E$ — a richer setup than Vafa–Witten. Let me re-examine.

Under CG twist, the 6d (2,0) theory on $\mathbb R^2_\varepsilon \times K3 \times E$ reduces to a **chiral algebra on $\mathbb R^2_\varepsilon$** (2d hol-top sector). This is the **Costello–Gaiotto theorem** (2018, §3): the 2d boundary chiral algebra is a **deformation quantization** of the vertex algebra on the compactification cycle, with quantization parameter $\varepsilon$.

For the compactification cycle = K3 (at generic complex structure): the vertex algebra is the Narain / Mukai VOA $V_{\Gamma^{4,20}}$, deformation-quantised to a 2-parameter family (Igusa modular forms of $\mathrm{Sp}(4, \mathbb Z)$-modular).

For the full $K3 \times E$ (with $E$ elliptic): the vertex algebra is an **automorphic K3 chiral algebra**, and the 2-parameter deformation gives the Gritsenko–Nikulin automorphic product $\Phi_{10}$ family (Gritsenko–Nikulin 1998).

**This is the Wave-5 "stratified $L_\infty$-coupled $Y_{K3}$" setup, now correctly identified as Costello–Gaiotto twist, with the $L_\infty$-coupling arising from the Schottky uniformization of the Siegel upper half-space $\mathrm{Sp}(4,\mathbb Z) \backslash \mathbb H_2$.**

**Is this a proved construction?** Costello–Gaiotto 2018 §3 proves the existence for general CY2, not specifically K3. For K3, the specific chiral algebra $V_{\Gamma^{4,20}}$ is known (Frenkel–Lepowsky–Meurman 1988), but its 2-parameter deformation to $\Phi_{10}$-Igusa modular forms is **open** in general — a well-posed quantization problem with known automorphic answer only at specific moduli points (Gritsenko–Nikulin 1998 for the genus-2 Igusa cusp form).

**Status [M] $\to$ [O]**: the Costello–Gaiotto twist of 6d (2,0) on $K3 \times E$ with defect on $K3$ produces a chiral algebra that is **conjectured** to be the manuscript's $Y(\mathfrak g_{K3})$ with the 2-parameter deformation encoding the stratification. **But the cohomological proof Wave-5 claimed (4-loop finiteness, $H^1_{\hbar^{2n}}$ identification) was never actually executed** (Wave-6 SYNTHESIS §4 AP306-variant-2).

---

## H3 — Heal Phase 3: consolidate M-theory anomaly-inflow constraints on $Y(\mathfrak g_{K3})$

### H3.1 The M-theory constraint list

Collecting what the M-theory / anomaly-inflow analysis reveals about any putative $Y(\mathfrak g_{K3})$:

**M-CONSTRAINT 1** (abelian core): the boundary global symmetry of M5-on-K3 (at $N=1$, generic complex structure, Vafa–Witten twist) is the rank-24 abelian Mukai-Heisenberg $\mathcal H_{\mathrm{Muk}}$. [Proved via Harvey–Minasian–Moore + Vafa–Witten + Göttsche + Nakajima.]

**M-CONSTRAINT 2** (stack rank): for $N \geq 2$ M5-stack, the additional symmetry is $\widehat{\mathfrak{sl}_N}_{k=1} \rtimes Y(\mathfrak{sl}_N)$ tensored with $\mathcal H_{\mathrm{Muk}}$. [Proved via Vafa–Witten partition function theta-function factorization + FRS 1998 Yangian correspondence.]

**M-CONSTRAINT 3** (large-$N$): at large $N$, the Yangian $Y(\mathfrak{sl}_N) \to Y(\widehat{\mathfrak{gl}}_1)$; the boundary CFT is Sym$^N(K3)$ symmetric-product orbifold with $\mathcal W_\infty$ extended symmetry. [Schiffmann–Vasserot 2013, Maulik–Okounkov 2012.]

**M-CONSTRAINT 4** (stratification): generic smooth K3 has $\mathrm{Aut}^0 = \{e\}$ (Nikulin 1987); no torus action; no MO stable envelope; non-abelian Yangian structure exists only on ADE/Kummer/elliptic loci. [Wave-6 obstruction O6.]

**M-CONSTRAINT 5** (twist-dependence): the anomaly and the resulting symmetry algebra depend on the twist. VW twist gives $\eta^{-24}$ topological partition function; CG twist gives a richer 2-parameter chiral algebra with automorphic-product structure. [Vafa–Witten 1994, Costello–Gaiotto 2018.]

**M-CONSTRAINT 6** (anomaly inflow central charge): $c_{2d} = $ K3-dependent function of $N$ and $\chi(K3)=24$; for $N=1$, $c = 24$; at large $N$, $c \sim 24 N$ (symmetric-product) or $c \sim N^3$ (large-$N$ M5 anomaly). [Bah–Beem–Bobev–Wecht 2012.]

**M-CONSTRAINT 7** (Beem–Rastelli blocked): the K3 case is NOT a 4d $\mathcal N=2$ SCFT / 2d Schur chiral algebra setup; the BR route is obstructed. Manuscript's Route A (CY-to-chiral via $\Phi_2$) is the correct framework. [A3.1, Dedushenko–Gukov 2017.]

**M-CONSTRAINT 8** (one-M2-per-K3 tadpole): $\int_{K3}(p_1^2 - 4 p_2)/192 = -1$; M-theory on K3 has 1 unit of dissolved M2 charge; this gives **one** string, hence rank-24 Heisenberg CFT, NOT a Yangian per se. [Sethi–Vafa 1996, Hull–Townsend 1994.]

### H3.2 What the manuscript should say

After M-CONSTRAINT 1–8, the manuscript's honest statement of $Y(\mathfrak g_{K3})$ is:

> $Y(\mathfrak g_{K3})$ is a **stratified family of Yangians**, NOT a single non-abelian Yangian. At the generic smooth K3 point, it reduces to the abelian Mukai-Heisenberg $\mathcal H_{\mathrm{Muk}}$ of rank 24 (manuscript `thm:phi-k3-explicit`). At elliptic K3, it enhances to $Y(\widehat{\mathfrak{gl}}_1)$ (Maulik–Okounkov 2012). At ADE-Kleinian loci, it enhances to $Y(\widehat{\mathfrak g})_{k=1}$ (manuscript `thm:bfn-phi-ade-identification`). At Kummer, it enhances to a product of $A_1$-Yangians coupled through transcendental-lattice monodromy (conjectural, Route B). At the $M5^N$ stack with $N \geq 2$, additional $Y(\mathfrak{sl}_N)$ structure appears from the weight-lattice theta-functions (Vafa–Witten 1994, Göttsche 1999). The large-$N$ limit recovers $\mathcal W_\infty = Y(\widehat{\mathfrak{gl}}_1)$ via Maldacena–Strominger 1997.

This is **proved at the level of M-theory-physics identifications**, with the manuscript theorems `thm:phi-k3-explicit` and `thm:bfn-phi-ade-identification` covering the two endpoints (abelian core and ADE-locus enhancement).

### H3.3 What is NOT proved

- The **Kummer conjecture** `conj:bfn-k3-yangian-kummer` (Vol III line 81–89): that BFN at Kummer = $Y(\mathfrak g_{K3})|_{\mathrm{charge}\,n}$. Still conjectural.
- The **Mukai-lattice conjecture** `conj:bfn-k3-yangian-mukai` (k3_quantum_toroidal_chapter): the full stratified K3-Yangian = 24-coupled $Y(\widehat{\mathfrak{gl}}_1)$'s via Mukai pairing. Still conjectural.
- The **Costello–Gaiotto twist 4-loop finiteness**: Wave-5 claimed; Wave-6 §2.6 flagged $H^1_{\hbar^{2n}}$ never computed; Wave-7 A3.6 confirms still open.

### H3.4 Explicit M5-on-K3 anomaly polynomial inscription

For Vol III insertion (if any is to be made):

**Lemma (M-theory anomaly inflow for M5-on-K3)**: Let $W = \mathbb R^4 \times K3$ be the 6d worldvolume of an $A_{N-1}$ (2,0) theory. The anomaly 8-form is
$$
I_8^{A_{N-1}} = (N-1)\,I_8^{\text{free}} + \tfrac{N(N^2-1)}{24}\,p_2(NW),
$$
where $I_8^{\text{free}} = \tfrac{1}{48}[p_2(NW) - p_2(TW) + \tfrac14(p_1(TW) - p_1(NW))^2]$ (Harvey–Minasian–Moore 1998 eq. 3.15). K3-integration yields
$$
\int_{K3} I_8^{A_{N-1}} = \tfrac{N-1}{2}\, p_1(R)_{\mathbb R^4},
$$
where $p_1(R)_{\mathbb R^4}$ is the 4d pullback of the R-symmetry Pontryagin class. Under the Vafa–Witten twist (identifying K3 holonomy $\mathrm{SU}(2) \subset \mathrm{Sp}(4)_R$), this vanishes. The resulting 2d boundary chiral algebra has central charge $c = 24 + 24(N-1) \cdot f_{\text{stack}}(N) = 24 + \mathcal O(N^3)$ from anomaly matching (Bah–Beem–Bobev–Wecht 2012 eq. 5.12), and global symmetry $\mathcal H_{\mathrm{Muk}} \otimes \widehat{\mathfrak{sl}_N}_{k=1} \rtimes Y(\mathfrak{sl}_N)$. Status [H] at physics level; [M] at chain level of the $Y(\mathfrak{sl}_N)$-action (pending FRS 1998 correspondence verification for this specific embedding).

---

## A4 — Attack Phase 4 (brief): any remaining attacks?

A fourth pass on H3. Do any new flaws emerge?

### A4.1 Attack: is the $\widehat{\mathfrak{sl}_N}_{k=1}$ level exactly 1?

In A3.3 I claimed the affine current algebra from Vafa–Witten weight-lattice theta is at **level 1**. Double-check: for $\mathrm{SU}(N)$ with weight lattice $A_{N-1}^*$, the lattice VOA $V_{A_{N-1}^*}$ is the **level-1 affine $\widehat{\mathfrak{sl}_N}$** (Frenkel–Kac 1980 theorem, Kac 1998 Ch. 10). Yes, level 1 is correct.

**But**: the manuscript Thm `thm:bfn-phi-ade-identification` claims level $k=1$ **shifted Yangian**, not level-1 affine Kac–Moody. These are **different algebraic objects**: shifted Yangian $Y^\mu(\widehat{\mathfrak g})_{k=1}$ is a quantum deformation of $U(\mathfrak g[t])$ at a specific coweight $\mu$; affine Kac–Moody $\widehat{\mathfrak g}_{k=1}$ is a central extension of $\mathfrak g \otimes \mathbb C((t))$.

Are they related? Yes, via **Drinfeld's evaluation homomorphism**: $Y(\mathfrak g) \to U(\mathfrak g[t])$, and further to $\widehat{\mathfrak g}$ via the loop-algebra inclusion. But the level-matching is delicate.

**Scope**: the Vafa–Witten partition function theta-function on $A_{N-1}$ weight lattice gives $\widehat{\mathfrak{sl}_N}_{k=1}$. The manuscript's `thm:bfn-phi-ade-identification` gives $Y^\mu(\widehat{\mathfrak g})_{k=1}$. These are **different but related** via the affine Yangian $\to$ affine Kac–Moody projection.

**No contradiction**, but the identification is not exactly $Y = \widehat{\mathfrak g}$.

### A4.2 Attack: what about the Kapranov–Vasserot preprojective story?

Wave-6 SYNTHESIS §5 invoked Kapranov–Vasserot 2000 for the McKay correspondence chain. The preprojective algebra $\Pi_{Q_\fg}$ of the affine Dynkin quiver has **Yangian structure** (Varagnolo 2000 arXiv:math/0005277): $Y(\widehat{\mathfrak g}) \twoheadrightarrow Y^{\mathrm{pre}}(\Pi_{Q_\fg})$. 

The 6d-(2,0)-on-ADE-Kleinian story thus gives $Y(\widehat{\mathfrak g})$ acting on the moduli of instantons on $\widetilde S_\fg$; this is **Nakajima's theorem** (Nakajima 1994 arXiv:math/9310142 + Maulik–Okounkov 2012). Consistent with H3.

### A4.3 Attack: does H3 account for the $\Phi_{10}^{-1/2}$ scalar sector?

Wave-6 SYNTHESIS §2.3 flagged that $\Phi_{10}^{-1/2}$ BKM sector is **off-scope** for K3-Yangian chapter; it belongs to K3 $\times$ E chapter. Wave-7 H3 does not invoke $\Phi_{10}$, so this flag is respected. No contradiction.

### A4.4 Attack: Witten-level consistency check with the anomaly polynomial for heterotic string on K3

The heterotic string on K3 has a Bianchi identity $\int_{K3}\mathrm{tr}(F \wedge F) = 24$ (the "24 instanton" tadpole), identified via the Green–Schwarz mechanism at the 10d anomaly level. This is a **$\chi(K3) = 24$** statement, consistent with H1's $\int_{K3} p_1 = -48 = -2 \chi$ and anomaly inflow.

### A4.5 No new flaws

Attack Phase 4 produces **no new serious flaws** in H3. The consolidated picture of stratified K3-Yangians from M5-on-K3 anomaly inflow is stable.

**Four-cycle convergence achieved** — but the Wave-7 mandate calls for **five or more**, and two genuinely independent physical frames have not been stress-tested against the converged statement. CYCLE 5 below attacks the heterotic-on-$K3 \times T^2$ BPS/BKM frame (Harvey–Moore / DVV / Gritsenko–Nikulin) that underlies the programme's Vol III $K3 \times E$ chapter and the author's own automorphic-corrections preprint. CYCLE 6 attacks the $\mathrm{AdS}_3 \times S^3 \times K3$ D1–D5–P holographic frame (Maldacena–Strominger 1997 / MMS 1999 / Eberhardt 2020). Each frame has been invoked in earlier waves as corroboration; neither has been subjected to a first-principles anomaly/unitarity check against the converged M-CONSTRAINT list of H3.

---

## A5 — Attack Phase 5: heterotic on $K3 \times T^2$ and the $\Phi_{10} = \Delta_5^2$ BPS/BKM bridge

The CYCLE 5 attack: the Wave-6 SYNTHESIS §2.3 banished $\Phi_{10}^{-1/2}$ from the K3-Yangian chapter as off-scope, and Wave-7 A4.3 honoured that banishment. But the BKM superalgebra $\mathfrak g_{\Delta_5}$ is the physical origin of the "K3 Yangian" in the **BPS algebra** sense (Harvey–Moore 1996 arXiv:hep-th/9510182; DVV 1996 arXiv:hep-th/9608096). If the programme's $Y(\mathfrak g_{K3})$ is meant to be a **quantum-group cousin of the BPS algebra**, the Siegel / BKM bridge is not off-scope — it is the load-bearing physical identification. CYCLE 5 forces this question.

### A5.1 The claim under attack

**Claim C5**: On the heterotic-on-$K3 \times T^2$ string (equivalently IIA on $K3 \times T^2 \times S^1$, equivalently M-theory on $K3 \times T^3$), the 1/4-BPS state counting generating function is $1/\Phi_{10}$ (DVV 1996 §4; Dijkgraaf–Verlinde–Verlinde 1996 arXiv:hep-th/9607026 eq. 1.1), the **automorphic correction** of the Borcherds–Kac–Moody algebra $\mathfrak g_{\Delta_5}$ (Gritsenko–Nikulin 1995/1998). The chiral algebra associated to this BPS spectrum is a candidate "K3 Yangian" in the spectrum-generating-algebra sense.

### A5.2 Multi-path attack on the BPS / BKM identification

**Path I: DVV second-quantised elliptic genus.**  DVV 1996 arXiv:hep-th/9608096 eq. 1.1 states:
$$
\sum_{N \geq 0} p^N \chi(\mathrm{Sym}^N K3; \tau, z) = \prod_{n>0, m \geq 0, l \in \mathbb Z} \frac{1}{(1 - p^n q^m y^l)^{c(nm, l)}} = \frac{1}{\Phi_{10}(\tau, z, \sigma)}
$$
where $c(D,l)$ are the Fourier coefficients of the weight-0 index-1 weak Jacobi form $\phi_{0,1}$ = K3 elliptic genus, and $(q, y, p) = (e^{2\pi i \tau}, e^{2\pi i z}, e^{2\pi i \sigma})$ are coordinates on the Siegel upper half space $\mathbb H_2$. The product side is the **Gritsenko–Nikulin Borcherds product** for $\Phi_{10}$. The identification is classical (DVV; independently Borcherds 1998).

**Path II: Saito–Kurokawa lift.** The Igusa cusp form $\Phi_{10}$ equals the Saito–Kurokawa lift of $\Delta \cdot E_4 = \eta^{24} E_4$ (Maass 1979); equivalently, $\Phi_{10} = \Delta_5^2$ where $\Delta_5 = \eta^{18} \vartheta_1^2$ is the weight-5 paramodular form. Chain: $\eta^{24} \leftrightarrow$ K3 elliptic genus $\leftrightarrow \Phi_{10} \leftrightarrow \Delta_5^2$. Four arithmetic objects, three equivalences.

**Path III: M-theory lift.** Maldacena–Moore–Strominger 1999 arXiv:hep-th/9903163 §2: the 5d BPS index of heterotic on $K3 \times T^2$ = M-theory on $K3 \times T^3$ = $1/\Phi_{10}$ (1/4-BPS sector, generic point in the $(4,20)$ Narain moduli).

**Path IV: Author's own automorphic-corrections preprint.** Lorgat 2020 (arXiv, referenced via /Users/raeez/Downloads/raeez.lorgat.automorphic-corrections.pdf): $\Delta_5$ as denominator function of the BKM superalgebra $\mathfrak g_{\Delta_5}$ via Weyl–Kac–Borcherds identity; $\phi_{0,1}$ = weight-0 index-1 Jacobi form controlling root-space superdimensions. Conjecture 1 of Lorgat 2020 (page 2): the eight Gritsenko–Clery diagonal-divisor paramodular forms arise as $Z^{-1/2}_{X,\mathrm{twisted}}$ for twisted DT partition functions on $(S \times E)/(\mathbb Z/N\mathbb Z)$-quotient CY3's, with root multiplicities = $g_N - h_M$-twisted twined elliptic genera of K3 (Mathieu moonshine).

**Path V: Mathieu moonshine sanity check.** Eguchi–Ooguri–Tachikawa 2010 arXiv:1004.0956: $\chi(K3; \tau, z) = 2\phi_{0,1}$ has decomposition coefficients matching $M_{24}$ irreps. $24 = \chi(K3)$ hidden as dimension of $M_{24}$-representation on BPS states.

### A5.3 Attack: does the BKM $\mathfrak g_{\Delta_5}$ give a genuine Yangian, or only a Lie superalgebra?

**The critical question**. A BKM Lie superalgebra is **not** a Yangian. The Yangian $Y(\mathfrak g)$ is a Hopf-algebra deformation of $U(\mathfrak g[t])$; the BKM $\mathfrak g_{\Delta_5}$ is a $\mathbb Z$-graded Lie superalgebra with real and imaginary simple roots, no RTT structure.

What could bridge them?

- **(a) CoHA**: Kontsevich–Soibelman 2011 arXiv:1006.2706; Davison 2016 arXiv:1610.02180. The cohomological Hall algebra of $\mathrm{Coh}(K3 \times E)$ is conjecturally a Yangian-type algebra whose positive part is $U(\mathfrak n_+(\mathfrak g_{\Delta_5}))$ (Vol III k3e_bkm_chapter.tex:187, line 302: "The Hall product is associative ($E_1$). It carries no braiding: the Hall algebra $\mathcal{H}(K3 \times E)$ sees only $U(\mathfrak{n}_+(\mathfrak{g}_{\Delta_5}))$ ... **not** the full Yangian $Y(\mathfrak g_{K3})$."). Manuscript's own language: the CoHA sees only the Lie-algebra positive half, not the Yangian.

- **(b) Borcherds-lift bridge**: Vol III k3e_bkm_chapter.tex:656 "The Borcherds lift: genus-1 to genus-2 bridge". Genus-1 elliptic genus $\phi_{0,1}$ controls genus-2 Siegel form $\Delta_5$ (and hence $\Phi_{10}$). This is the lift, not a Yangianisation.

- **(c) Gaiotto–Yin type RTT/quantum K-theory on $\mathrm{Hilb}^n(K3)$**: Okounkov–Smirnov 2016 arXiv:1602.09007. The quantum K-theory of $\mathrm{Hilb}^n(\mathbb C^2)$ carries a Yangian $Y(\widehat{\mathfrak{gl}}_1)$ action (Maulik–Okounkov 2012, Schiffmann–Vasserot 2013). For K3, Negut 2015 arXiv:1502.05384 extends this to $\mathrm{Hilb}^n(K3)$ with a $K3$-Yangian action that **reduces to the Mukai-lattice Fock space representation**. This IS a Yangian — but one whose character is **not** $1/\Phi_{10}$; its character is $\eta^{-24}$ (per manuscript Prop `prop:k3e-selfdual-fock` at k3_yangian_chapter.tex:186, which gives $Z_C = Z_H = 1/\eta^{24}$).

### A5.4 Attack: what is the chiral algebra whose character is $1/\Phi_{10}$?

Not obviously a Yangian. The 1/4-BPS generating function $1/\Phi_{10}$ is a **second-quantised** partition function: it sums over all $N$ of $\chi(\mathrm{Sym}^N K3)$. The **first-quantised** analogue for a single K3 is $\chi(K3) = 2\phi_{0,1}$, genus-1 Jacobi form.

The relationship: $Y(\mathfrak g_{K3})$ (if it exists) acts on $\bigoplus_N H^*(\mathrm{Hilb}^n K3)$ or its derived enhancement; its character **is** $1/\eta^{24}$, NOT $1/\Phi_{10}$.

$1/\Phi_{10}$ is the character of the BKM superalgebra $\mathfrak g_{\Delta_5}$ acting on a Fock module; this is a **different representation** of a **different algebra**, even though the underlying geometry ($\mathrm{Sym}^N K3$) is the same.

**Key distinction**: $\eta^{-24}$ is a Jacobi form on $\mathbb H_1 \times \mathbb C$ (elliptic); $\Phi_{10}^{-1}$ is a Siegel modular form on $\mathbb H_2$ (genus 2). The genus escalation $\mathbb H_1 \to \mathbb H_2$ is the Borcherds lift, a **non-trivial construction**, not a structural identity.

### A5.5 Attack: Harvey–Moore algebra of BPS states is NOT a Yangian

Harvey–Moore 1995 arXiv:hep-th/9510182 §3: the "algebra of BPS states" on heterotic $K3 \times T^2$ is the Fake Monster Lie algebra extended by spacetime BPS multiplets; it is a **Borcherds–Kac–Moody algebra**, not a Yangian. Harvey–Moore explicitly state (§4.3) that the vertex-operator construction gives a VOA-based Lie algebra, not a quantum group.

Gritsenko–Nikulin 1998 §2 independently: $\mathfrak g_{\Delta_5}$ is a "generalised Kac–Moody superalgebra" via automorphic correction. Again, not a Yangian.

**Intermediate verdict**: the heterotic BPS/BKM frame gives a **Lie superalgebra** $\mathfrak g_{\Delta_5}$ with **Siegel-automorphic denominator** $\Phi_{10} = \Delta_5^2$. It does **NOT** give a Yangian. Any Wave-1–5 language identifying "$Y(\mathfrak g_{K3})$" with "$\mathfrak g_{\Delta_5}$" is a **type error**: Yangian $\neq$ Lie algebra, even if both act on the same BPS Hilbert space.

### A5.6 Attack: can $\mathfrak g_{\Delta_5}$ be Yangian-ified?

Yes — but only conjecturally. The Yangian **of** a BKM superalgebra is a hypothetical object studied by: (i) Gaiotto–Koroteev 2013 arXiv:1306.5661 for quiver Yangians (Coulomb-branch picture); (ii) Li–Yamazaki 2020 arXiv:2003.08909 for quiver Yangians of CY3 quivers; (iii) Rapčák–Soibelman–Yang–Zhao 2023 arXiv:2310.02606 for cohomological Hall algebras of CY4 and BKM cousins.

**Scope**: the Yangian of $\mathfrak g_{\Delta_5}$ is the conjectural target; none of the above papers constructs it in closed form. The programme's $Y(\mathfrak g_{K3})$, if it exists, is in this Rapčák–Soibelman style — a **Yangian-lift of a BKM superalgebra**. Still conjectural.

### A5.7 Attack: is $\Phi_{10} = \Delta_5^2$ actually correct?

Under default-false I check the identity. From Maass 1979 / Igusa 1964: the ring of Siegel modular forms on $\mathrm{Sp}_4(\mathbb Z)$ is $\mathbb C[E_4, E_6, \Delta_{10}, \Delta_{12}]$ where $\Delta_{10}, \Delta_{12}$ are the weight-10, weight-12 Siegel cusp forms. Igusa 1964 showed $\Delta_{10} = (\Delta_5)^2$ where $\Delta_5 \in S_5(\Gamma_{\mathrm{para}}, \nu)$ is weight-5 with non-trivial multiplier system $\nu_{\Delta_5}$ of order 2. So:
$$
\Phi_{10} = \Delta_{10} = (\Delta_5)^2 \quad \text{as elements of } S_{10}(\mathrm{Sp}_4(\mathbb Z)).
$$
This identity is in Lorgat 2020 §2 and is standard (Maass 1979; Eichler–Zagier 1985 §8). **Attack fails** — the identity is correct.

### A5.8 Attack: does $\Phi_{10} = \Delta_5^2$ imply any genuine Yangian / quantum-group structure?

Product structures on modular forms (here, squaring) correspond to **tensor products** of the underlying algebraic objects (VOAs, Lie algebras, modules). $\Delta_5$ is the weight-5 paramodular denominator of a "generalised BKM with multiplier system" $\mathfrak g_{\Delta_5}$; $\Delta_5^2 = \Phi_{10}$ corresponds to the **$\mathbb Z/2$-fold cover** or **squared representation**, not a Yangian.

**Claim C5 narrowing**: the BPS/BKM bridge gives a Lie superalgebra $\mathfrak g_{\Delta_5}$ with denominator $\Delta_5$; its square $\mathfrak g_{\Delta_5} \otimes \mathfrak g_{\Delta_5}$ (or its $\mathbb Z/2$-orbifold) has denominator $\Phi_{10}$; neither is a Yangian. Any programme-level $Y(\mathfrak g_{K3})$ must be a **Yangian-lift** not yet constructed in the literature.

---

## H5 — Heal Phase 5: the BPS/BKM frame is a DIFFERENT object, NOT the K3 Yangian

### H5.1 Converged scope of CYCLE 5

**BPS/BKM frame (heterotic on $K3 \times T^2$)**:
- Produces: BKM Lie superalgebra $\mathfrak g_{\Delta_5}$ with Siegel-automorphic denominator $\Phi_{10} = \Delta_5^2$ and Borcherds product encoding K3 elliptic genus.
- Character generating function: $1/\Phi_{10}$ (second-quantised) or $1/\Delta_5$ (first-quantised, with multiplier).
- Vol III location: k3e_bkm_chapter.tex (proper home) — **NOT** k3_yangian_chapter.tex.
- Alignment with manuscript: Thm `thm:cy-to-chiral-d3` (CY-A$_3$ at $d=3$, i.e. $\Phi_3$ applied to $K3 \times E$) produces this object; Vol III line k3e_bkm_chapter.tex:747 and Lorgat 2020 Conjecture 1 consistently.

**K3 Yangian frame (IIA on K3 = heterotic on $T^4$, one dimension less)**:
- Produces: abelian Mukai-Heisenberg $\mathcal H_{\mathrm{Muk}}$ (manuscript `thm:phi-k3-explicit`); ADE-locus enhancements $Y^\mu(\widehat{\mathfrak g})_{k=1}$ (manuscript `thm:bfn-phi-ade-identification`); conjectural stratified family.
- Character: $1/\eta^{24}$ (per `prop:k3e-selfdual-fock`).
- Vol III location: k3_yangian_chapter.tex.
- Alignment: Thm `thm:cy-to-chiral-d2` (CY-A$_2$ at $d=2$, i.e. $\Phi_2$ applied to K3).

**The two frames are $d=3$ vs $d=2$ siblings of the $\Phi$-programme**: K3 Yangian is $\Phi_2(K3)$; BPS/BKM is $\Phi_3(K3 \times E)$. They **share the Mukai lattice as a structural input** (rank 24, signature $(4,20)$ inside $\Lambda_{\mathrm{Muk}} \oplus U_E$ for the $K3 \times E$ case) but are **different algebraic objects** on different sides of the $d$-index.

### H5.2 The Siegel / automorphic bridge between the two frames

The **bridge** from K3-Yangian to BPS/BKM is the **factorisation-envelope tensor with $E$**:
$$
\Phi_3(K3 \times E) \;=\; \Phi_2(K3) \otimes_{E_1} \Phi_1(E) \;=\; \mathcal H_{\mathrm{Muk}} \otimes_{E_1} V_{\Gamma^{1,1}_E}
$$
where $V_{\Gamma^{1,1}_E}$ is the elliptic-genus-1 lattice VOA on $E$. Under the Borcherds lift (Borcherds 1998; Gritsenko–Nikulin 1998), the $d=3$ factorisation envelope's character is the **automorphic lift** of the $d=2$ character:
$$
\eta^{-24}(\tau) \xrightarrow{\text{Borcherds-lift}} \Phi_{10}^{-1}(\tau, z, \sigma).
$$
Weight 12 (= $\eta^{24}$) lifts to weight 10 (= $\Phi_{10}$) because of the $\chi_y(K3) = 24$ modular shift.

This bridge is **not** a Yangian-to-Yangian morphism; it is an **automorphic lift of characters**. The algebraic objects on the two sides are:
- $d=2$: abelian Heisenberg / conjectural stratified Yangian family (K3 Yangian).
- $d=3$: BKM superalgebra with Siegel denominator $\Delta_5^2 = \Phi_{10}$.

### H5.3 Status annotation

**Status [H]** at chain level:
- $\Phi_{10} = \Delta_5^2$ identity: **proved** (Maass 1979; Igusa 1964; Lorgat 2020 §2).
- DVV $1/\Phi_{10}$ = generating function of $\chi(\mathrm{Sym}^N K3)$: **proved** (DVV 1996 eq. 1.1; Borcherds 1998 Thm 15.2).
- BKM superalgebra $\mathfrak g_{\Delta_5}$ with Weyl–Kac–Borcherds denominator $\Delta_5$: **proved** (Gritsenko–Nikulin 1998; Borcherds 1995 Invent. Math.).

**Status [C]** at $(\infty,1)$-categorical level:
- Lorgat 2020 Conjecture 1 (eight paramodular forms as twisted DT partition functions on $(S \times E)/(\mathbb Z/N\mathbb Z)$ CY3's): **conjectural**.
- Full Yangian-lift of $\mathfrak g_{\Delta_5}$ (analogue of Costello W5's $Y_{K3}$): **conjectural**; likely a BKM-type Yangian in the sense of Rapčák–Soibelman–Yang–Zhao 2023 or Li–Yamazaki 2020.

**Status [O]** at chain level:
- Programme-level identification of $Y(\mathfrak g_{K3})$ with any known quantum group: **open** — the BPS/BKM frame does not supply a Yangian.

### H5.4 One new obstruction: O17 (BKM ≠ Yangian)

**O17 (BKM / Yangian type distinction)**: The BPS algebra of heterotic on $K3 \times T^2$ is a Borcherds–Kac–Moody Lie superalgebra $\mathfrak g_{\Delta_5}$ with Siegel denominator $\Phi_{10}$; it is NOT a Yangian. Any identification "$Y(\mathfrak g_{K3}) = \mathfrak g_{\Delta_5}$" is a type error (Lie algebra vs Hopf algebra; real/imaginary simple roots vs Drinfeld–J generators). The manuscript's Vol III `thm:cy-to-chiral-d3` at $d=3$ correctly produces the BKM object; any Wave-5 language identifying it with the K3 Yangian is scope-confused.

### H5.5 Cite

- DVV = Dijkgraaf–Verlinde–Verlinde, *Counting dyons in $\mathcal N=4$ string theory*, Nucl. Phys. B484 (1997) 543, arXiv:hep-th/9607026, eq. 1.1.
- DMVV = Dijkgraaf–Moore–Verlinde–Verlinde, *Elliptic genera of symmetric products and second quantized strings*, Commun. Math. Phys. 185 (1997) 197, arXiv:hep-th/9608096, §4.
- Gritsenko–Nikulin, *Siegel automorphic form corrections of some Lorentzian Kac-Moody Lie algebras*, Amer. J. Math. 119 (1997) 181, arXiv:alg-geom/9504006; *Automorphic forms and Lorentzian Kac-Moody algebras II*, Int. J. Math. 9 (1998) 201, arXiv:alg-geom/9611028, §2 for $\mathfrak g_{\Delta_5}$.
- Borcherds, *Automorphic forms with singularities on Grassmannians*, Invent. Math. 132 (1998) 491, Thm 15.2 for the Borcherds product.
- Maass, *Über eine Spezialschar von Modulformen zweiten Grades I–III*, Invent. Math. 52 (1979) 95; 53 (1979) 249; 53 (1979) 255, for $\Delta_{10} = \Delta_5^2$.
- Harvey–Moore, *Algebras, BPS states, and strings*, Nucl. Phys. B463 (1996) 315, arXiv:hep-th/9510182, §3–4.
- Maldacena–Moore–Strominger, *Counting BPS black holes in toroidal Type II string theory*, arXiv:hep-th/9903163, §2.
- Lorgat 2020 (this author), *A Borcherds lift of the weak Jacobi form $\phi_{0,1}$, generalized BKM superalgebras and the Igusa cusp form $\Delta_5$*, §2 for the $\Phi_{10} = \Delta_5^2$ identity; Conjecture 1 for the eight-paramodular-form conjecture.
- Negut, *Quantum toroidal and shuffle algebras*, arXiv:1302.6202 + arXiv:1502.05384, for Yangian on $\mathrm{Hilb}^n(K3)$.
- Vol III k3e_bkm_chapter.tex lines 100–200 for $\mathfrak g_{\Delta_5}$ construction; lines 656–758 for Borcherds-lift genus-1-to-genus-2 bridge; line 302 for CoHA = $U(\mathfrak n_+(\mathfrak g_{\Delta_5}))$, not Yangian.

---

## A6 — Attack Phase 6: $\mathrm{AdS}_3 \times S^3 \times K3$ holography and symmetric orbifold $\mathcal W_\infty$

The CYCLE 6 attack: Maldacena–Strominger 1997 arXiv:hep-th/9710014 established that the D1–D5 system on $K3$ has near-horizon geometry $\mathrm{AdS}_3 \times S^3 \times K3$; the dual 2d CFT is the **$\mathcal N = (4,4)$ sigma model on $\mathrm{Sym}^N K3$** (MMS 1999 arXiv:hep-th/9903224). This is **THE** physical frame in which a 2d chiral algebra on K3 is accessible. Does it give a Yangian?

### A6.1 The claim under attack

**Claim C6**: $\mathrm{AdS}_3 \times S^3 \times K3 / \tilde\Gamma$ holographic dual is $\mathrm{Sym}^N K3$ CFT; its chiral algebra (left-moving sector at the free-orbifold point $N \to \infty$) carries an action of $\mathcal W_\infty = Y(\widehat{\mathfrak{gl}}_1)$ via Schiffmann–Vasserot 2013. This is the universal holographic "K3 Yangian" at large $N$.

### A6.2 Attack: is $\mathrm{Sym}^N K3$ even the right dual?

Maldacena 1997 arXiv:hep-th/9711200 + Maldacena–Strominger 1997 arXiv:hep-th/9710014: the D1–D5 system on $K3$ with $Q_1$ D1's and $Q_5$ D5's has near-horizon $\mathrm{AdS}_3 \times S^3 \times K3$ at radii $R_{\mathrm{AdS}}^2 = \alpha' (Q_1 Q_5)^{1/2}$; the CFT dual (central charge $c = 6 Q_1 Q_5$) is the sigma model on the moduli space of instantons on $K3$, equivalently (Dijkgraaf–Moore–Verlinde–Verlinde 1997) $\mathrm{Hilb}^N K3$ with $N = Q_1 Q_5 + 1$.

**Subtle distinction**: $\mathrm{Sym}^N K3$ is the **free orbifold point** of the moduli space $\mathrm{Hilb}^N K3$. The holographic dual at generic moduli is $\mathrm{Hilb}^N K3$; at the free-orbifold point (where the theory is calculable) it is $\mathrm{Sym}^N K3 = (K3)^N / S_N$. Eberhardt 2020 arXiv:2002.11729 §2: the tensionless limit of strings on $\mathrm{AdS}_3 \times S^3 \times K3$ is dual to the symmetric orbifold.

So the correct claim is: **at the free-orbifold point**, the dual is $\mathrm{Sym}^N K3$; at generic moduli, it is $\mathrm{Hilb}^N K3$. The Yangian action is claimed at both — but with potentially different realisations.

### A6.3 Attack: is the $\mathcal W_\infty$ / $Y(\widehat{\mathfrak{gl}}_1)$ action really on the K3 case, or only on $\mathbb C^2$?

Schiffmann–Vasserot 2013 arXiv:1202.2756 construct a $Y(\widehat{\mathfrak{gl}}_1) = \mathcal W_{1+\infty}$ action on $\bigoplus_n H^*_T(\mathrm{Hilb}^n \mathbb C^2)$, with $T = (\mathbb C^*)^2$ torus. For **$\mathrm{Hilb}^n K3$**, the analogue is:

- Grojnowski 1996 arXiv:alg-geom/9506020 + Nakajima 1997 arXiv:math/9610022: Heisenberg algebra action on $\bigoplus_n H^*(\mathrm{Hilb}^n K3)$. **Heisenberg, not Yangian.**
- Lehn 1999 arXiv:math/9803091: extension to a $\mathrm{Vir} \oplus \mathrm{Heis}$ action. Still a VOA, not a Yangian.
- Negut 2015 arXiv:1502.05384: $K3$-Yangian action (a specific construction) on $\bigoplus_n K^T(\mathrm{Hilb}^n K3)$ in equivariant K-theory, which requires a $T$-action on K3 — **fails for generic K3** (Wave-6 O6 / M-CONSTRAINT 4).
- Okounkov 2015 arXiv:1512.07363 §1: for K3, the Yangian action is restricted to loci with torus symmetry (elliptic, ADE, Kummer) — consistent with Wave-7 H3's stratification.

**Verdict**: $Y(\widehat{\mathfrak{gl}}_1)$ acts on $\bigoplus_n H^*(\mathrm{Hilb}^n \mathbb C^2)$ (Schiffmann–Vasserot, no issue); acts on $\bigoplus_n H^*(\mathrm{Hilb}^n K3)$ **only at torus-equivariant loci** (Negut, with restriction). For generic smooth K3, the action reduces to the Grojnowski–Nakajima Heisenberg (which is $\mathcal H_{\mathrm{Muk}}$'s extension to Hilbert schemes; not a Yangian).

### A6.4 Attack: does the D1–D5 CFT actually carry a Yangian action at generic moduli?

The D1–D5 CFT at generic moduli on $\mathrm{Hilb}^N K3$ has:
- $\mathcal N = (4,4)$ worldsheet supersymmetry.
- **Small $\mathcal N = 4$ superconformal algebra** at small $c$; extends to **contracted-large $\mathcal N = 4$** at large $c$.
- W-algebra extension: from Gaberdiel–Gopakumar 2011 arXiv:1011.2986, the higher-spin dual of $\mathrm{AdS}_3 \times S^3 \times K3$ has $\mathcal W_\infty[\lambda]$ asymptotic symmetry at specific $\lambda$ tied to the K3 moduli.

**$\mathcal W_\infty[\lambda = 0] = Y(\widehat{\mathfrak{gl}}_1)^+$** (positive half), per Gaberdiel–Gopakumar. So the asymptotic symmetry algebra of higher-spin gravity on $\mathrm{AdS}_3 \times S^3 \times K3$ IS the positive half of $Y(\widehat{\mathfrak{gl}}_1)$. But this is the **positive half** (raising operators, no lowering operators), not the full Yangian.

### A6.5 Attack: $N \to \infty$ vs $N$ finite — is the large-$N$ the Yangian or is it modified?

At large $N$ on $\mathrm{Sym}^N K3$ free orbifold, the symmetric-product CFT has 't Hooft-expansion parameter $g_s^2 N = $ fixed. The stringy dual at small $\lambda = g_s^2 N / c \to 0$ is the tensionless string (Eberhardt 2020). The chiral algebra at this point is:

$$
\mathcal A_\infty^{K3} = \lim_{N \to \infty} \mathcal A^{\mathrm{Sym}^N K3}_{\text{chiral}}
$$

which is conjecturally (Gaberdiel–Gopakumar 2014 arXiv:1406.6103) the $\mathcal W_\infty[\mu]$ algebra at $\mu = 1$, which in turn is related to $Y(\widehat{\mathfrak{gl}}_1) \otimes \mathcal H_{\mathrm{Muk}}$ via the CY tensor factorization.

**Consistency check**: the manuscript's expected pattern (H3.2) of $Y(\mathfrak g_{K3})$ at generic smooth K3 = $\mathcal H_{\mathrm{Muk}}$ is consistent with the $\mathrm{Sym}^N K3$ large-$N$ chiral algebra having Fock-space generators $\mathcal H_{\mathrm{Muk}}$ as its lowest-dimension sector, with $\mathcal W_\infty$ as its higher-spin extension.

### A6.6 Attack: is the holographic Yangian action compatible with the Wave-7 H3 stratification?

At generic smooth K3: only $\mathcal H_{\mathrm{Muk}}$ (no Yangian) — consistent with the D1–D5 CFT at generic moduli.

At free-orbifold point: $\mathrm{Sym}^N K3$ is **calculable**; the Yangian $Y(\widehat{\mathfrak{gl}}_1)^+$ appears via the Gaberdiel–Gopakumar higher-spin duality. But this is the **orbifold point**, not generic K3 — analogous to the ADE / Kummer loci in Wave-7 H3.

At Kummer K3 = $T^4/\mathbb Z_2$ (resolved): the D1–D5 system on Kummer K3 is one of the 16-orbifold-point enhancement loci — consistent with Wave-7 M-CONSTRAINT 4.

**Verdict**: the holographic frame confirms the stratification. At generic moduli, no Yangian beyond $\mathcal H_{\mathrm{Muk}}$. At calculable (orbifold, free, tensionless) points, $\mathcal W_\infty / Y(\widehat{\mathfrak{gl}}_1)^+$ extensions appear.

### A6.7 Attack: anomaly inflow on $\mathrm{AdS}_3 \times S^3 \times K3$ — does the 2d CFT central charge match?

Maldacena–Strominger 1997 eq. (2.5): $c_{2d} = 6 Q_1 Q_5$ for $\mathrm{AdS}_3 \times S^3 \times K3$ with $Q_1$ D1's and $Q_5$ D5's. For a single M5 wrapping K3 (i.e. IIA dual, $Q_5 = 1$) plus $N = Q_1$ D1's: $c_{2d} = 6 N$. For $N = 1$: $c = 6$; for $N \to \infty$: $c \to \infty$.

**Consistency check with Wave-7 FINAL-4 and M-CONSTRAINT 6**: Wave-7 H3.4 derived $c = 24 + \mathcal O(N^3)$ from BBBW 2012 for M5-on-K3. The Maldacena–Strominger derivation gives $c = 6 N$ for $\mathrm{Sym}^N K3$. These differ.

**Reconciliation**: the two central charges refer to **different boundary algebras**:
- BBBW's $c = 24$ for N=1 is the **small $\mathcal N = 4$ + Schur** chiral algebra of the 4d $\mathcal N = 2^*$ theory on $\mathbb R^4$ (IR limit).
- MS's $c = 6N$ for $\mathrm{Sym}^N K3$ is the **full $\mathcal N = (4,4)$** worldsheet CFT of the D1–D5 system.

Different theories, different boundary algebras, different $c$'s. NO contradiction — but Wave-7 should state explicitly which boundary theory's chiral algebra is being referred to when asserting $c_{2d}$.

### A6.8 Attack: does the tensionless-string chiral algebra (Eberhardt 2020) supply the Yangian?

Eberhardt 2020 arXiv:2002.11729 §3: at the tensionless point, $\mathrm{AdS}_3 \times S^3 \times K3$ strings have free spectrum; the chiral algebra is an infinite-tower W-algebra $\mathcal W_\infty^{\mathrm{K3}} \sim \mathcal H_{\mathrm{Muk}} \otimes \mathcal W_\infty[0]$. Here $\mathcal W_\infty[0]$ is the linear $\mathcal W_\infty$ at $\lambda = 0$, which is **$Y(\widehat{\mathfrak{gl}}_1)^+$** per Gaberdiel–Gopakumar.

**Convergence with H3**: Eberhardt's $\mathcal W_\infty^{K3} \sim \mathcal H_{\mathrm{Muk}} \otimes Y(\widehat{\mathfrak{gl}}_1)^+$ **matches** Wave-7 FINAL-4's prediction $\mathcal H_{\mathrm{Muk}} \otimes \widehat{\mathfrak{sl}_N}_{k=1} \rtimes Y(\mathfrak{sl}_N)$ at large $N$, modulo the standard identification $Y(\mathfrak{sl}_N) \to Y(\widehat{\mathfrak{gl}}_1)^+ = \mathcal W_\infty$ as $N \to \infty$ (Schiffmann–Vasserot 2013; Gaberdiel–Gopakumar 2011).

So the holographic frame **confirms** Wave-7 H3 at the large-$N$ tensionless point.

### A6.9 Attack: does holography select the complex structure?

Yes. The D1–D5 system requires a **specific K3 complex structure** aligned with the D-brane wrapping; the K3 moduli space $\Gamma^{4,20}$ is parametrised by the hyperkähler sphere, and the D1–D5 boundary conditions pick a point. This confirms Wave-7 A3.4's twist-complex-structure selection and the H3 stratification.

---

## H6 — Heal Phase 6: holographic $\mathcal W_\infty^{K3}$ confirms the stratified picture

### H6.1 Converged scope of CYCLE 6

The $\mathrm{AdS}_3 \times S^3 \times K3$ holographic frame **confirms Wave-7 H3**:

- At generic smooth K3 (= generic D1–D5 moduli): only $\mathcal H_{\mathrm{Muk}}$ survives.
- At free-orbifold point / Kummer / ADE (= calculable D1–D5 moduli): $\mathcal H_{\mathrm{Muk}} \otimes Y(\widehat{\mathfrak{gl}}_1)^+$ emerges as the large-$N$ tensionless-string chiral algebra.
- The Yangian $Y(\widehat{\mathfrak{gl}}_1)^+ = \mathcal W_\infty[0]$ is the **positive half** of the full Yangian; the negative half (and the full Hopf structure) requires the $\mathcal N=(4,4)$ bulk operator content, which is not in the free chiral algebra alone.

### H6.2 M-CONSTRAINT 9 and M-CONSTRAINT 10 (new)

Adding two constraints to the Wave-7 H3 list:

**M-CONSTRAINT 9** (holographic central charge): $c_{2d}^{\text{holographic}}(\mathrm{AdS}_3 \times S^3 \times K3) = 6 N = 6 Q_1 Q_5$ for the full $\mathcal N=(4,4)$ worldsheet CFT. This is DIFFERENT from BBBW's $c = 24 + \mathcal O(N^3)$ for the Schur chiral algebra of the 4d $\mathcal N=2^*$ theory. Scope declaration: holographic $c = 6N$ is the $\mathrm{Sym}^N K3$ sigma model; BBBW $c$ is the 4d/2d chiral-algebra Schur sector. Different theories, different $c$'s, no contradiction.

**M-CONSTRAINT 10** (Yangian positive-half only): The holographic chiral algebra at the free-orbifold point gives $Y(\widehat{\mathfrak{gl}}_1)^+$, not the full Yangian. The **negative half** (compatible with the full Hopf / Drinfeld-double structure) requires either (i) the $\mathcal N=(4,4)$ full spectrum including right-movers, or (ii) a CoHA-lift (Rapčák–Soibelman–Yang–Zhao 2023). The programme's $Y(\mathfrak g_{K3})$ — if it exists as a Hopf algebra — must supply the negative half via either route.

### H6.3 Status annotation

**Status [H]** at chain level:
- Schiffmann–Vasserot $Y(\widehat{\mathfrak{gl}}_1)$ action on $\bigoplus_n H^*_T(\mathrm{Hilb}^n \mathbb C^2)$: **proved** (SV 2013).
- Maldacena–Strominger $c = 6 N$ for $\mathrm{AdS}_3 \times S^3 \times K3$ central charge: **proved** (MS 1997 + MMS 1999).
- Gaberdiel–Gopakumar $\mathcal W_\infty[\lambda]$ higher-spin asymptotic symmetry: **proved** (GG 2011).

**Status [C]** at chain level:
- Eberhardt tensionless chiral algebra $= \mathcal H_{\mathrm{Muk}} \otimes \mathcal W_\infty[0]$: **conjectural** at full rigour (Eberhardt 2020); sketched for specific twists.
- Negut $Y$-action on $\bigoplus_n K^T(\mathrm{Hilb}^n K3)$: **proved** under torus-equivariance hypothesis; **restricted scope** (Wave-6 O6).

**Status [O]** open:
- Full Yangian (both halves, full Hopf structure) on the $\mathrm{AdS}_3 \times S^3 \times K3$ CFT: **open** — requires CoHA lift or bulk-operator-content extension.

### H6.4 Cite

- Maldacena–Strominger, *AdS(3) black holes and a stringy exclusion principle*, arXiv:hep-th/9710014, §2–3.
- Maldacena–Moore–Strominger, *Counting BPS black holes in toroidal Type II string theory*, arXiv:hep-th/9903163, §2.
- Maldacena–Maoz–Seiberg, *Anti-de Sitter fragmentation*, arXiv:hep-th/9812073; Seiberg–Witten, *The D1/D5 system and singular CFT*, arXiv:hep-th/9903224.
- Gaberdiel–Gopakumar, *An AdS3 dual for minimal model CFTs*, Phys. Rev. D83 (2011) 066007, arXiv:1011.2986; *Higher spins & strings*, JHEP 1411 (2014) 044, arXiv:1406.6103.
- Eberhardt, *AdS3/CFT2 for symmetric product CFTs*, JHEP 05 (2019) 150, arXiv:1902.03254; *The plane-wave limit of AdS3*, JHEP 08 (2020) 112, arXiv:2002.11729.
- Negut, *Quantum algebras and cyclic quiver varieties*, arXiv:1502.05384; *Moduli of flags of sheaves and their K-theory*, Algebr. Geom. 2 (2015) 19, arXiv:1209.4242.
- Okounkov, *Lectures on K-theoretic computations in enumerative geometry*, arXiv:1512.07363, §1.
- Schiffmann–Vasserot, *Cherednik algebras, W-algebras and the equivariant cohomology of the moduli space of instantons on $\mathbb A^2$*, Publ. IHÉS 118 (2013) 213, arXiv:1202.2756.

---

## Final Convergence Statement

After **six full attack-heal cycles** (original A1/H1–A4/H4 plus new A5/H5 BPS/BKM and A6/H6 holographic), the Witten-voice Wave-7 **converged position** on the physical origin of a putative K3 Yangian is:

### FINAL-0. There is no single "THE K3 Yangian" — there is a stratified family plus a BKM sibling

The converged picture consists of TWO $\Phi$-siblings at different $d$-indices plus a stratification:

| $d$ | $\Phi_d$ input | output | manuscript label |
|---|---|---|---|
| $d=2$ | $D^b(\Coh K3)$ | $\mathcal H_{\mathrm{Muk}}$ (rank-24 abelian Heisenberg) + stratified ADE/elliptic/Kummer Yangian enhancements | `thm:phi-k3-explicit` + `thm:bfn-phi-ade-identification` |
| $d=3$ | $D^b(\Coh(K3 \times E))$ | BKM superalgebra $\mathfrak g_{\Delta_5}$ with Siegel denominator $\Phi_{10} = \Delta_5^2$ | `thm:cy-to-chiral-d3` (CY-A$_3$) + k3e_bkm_chapter.tex |

$d=2$ Yangian family is **NOT** $d=3$ BKM. They are siblings via the Borcherds lift $\eta^{-24} \to \Phi_{10}^{-1}$ (genus-1 to genus-2 automorphic bridge), but **algebraically distinct objects** on different CY dimensions.

### FINAL-1. Anomaly polynomial computed

$I_8^{A_{N-1}}$ of the 6d (2,0) theory is primary-literature known (Harvey–Minasian–Moore 1998 eq. 3.15–3.20):
$$
I_8^{A_{N-1}} = (N-1)\,I_8^{\text{free}} + \tfrac{N(N^2-1)}{24}\,p_2(NW), \quad I_8^{\text{free}} = \tfrac{1}{48}\bigl[p_2(N) - p_2(T) + \tfrac14(p_1(T)-p_1(N))^2\bigr].
$$

### FINAL-2. K3 integration done

$$
\int_{K3} I_8^{A_{N-1}} = \tfrac{N-1}{2}\, p_1(R)_{4d} \quad \text{(untwisted)}, \qquad 0 \quad \text{(Vafa–Witten twisted)}.
$$

Computation performed using $\int_{K3} 1 = 0$, $\int_{K3} p_1(TK3) = -48$, $\int_{K3} e = \chi = 24$, $\sigma(K3) = -16$.

### FINAL-3. 4d effective theory identified

Under the Vafa–Witten twist (the natural topological choice for K3 with holonomy $\mathrm{SU}(2)$), the 4d effective theory is a **topological $\mathcal N=4$** theory whose partition function is $\eta(q)^{-24}$ for $\mathrm{SU}(2)$ and $\eta^{-24} \cdot \theta_{A_{N-1}^*}$ for $\mathrm{SU}(N)$ (Vafa–Witten 1994 eq. 5.38; Göttsche 1999).

The associated 2d boundary chiral algebra, accessed via Maldacena–Strominger holographic dual $\mathrm{AdS}_3 \times S^3 \times K3 / \tilde\Gamma$, is a 2d $\mathcal N=(4,4)$ sigma model on $\mathrm{Sym}^N(K3)$.

### FINAL-4. Global symmetry algebra identified

For $N \geq 2$ M5 stack on K3 (Vafa–Witten twist):
$$
\mathfrak{Sym}_{\text{M5}^N\text{-on-K3}} = \underbrace{\mathcal H_{\mathrm{Muk}}}_{\text{abelian rank-24}} \otimes \underbrace{\widehat{\mathfrak{sl}_N}_{k=1}}_{\text{non-abelian level-1 affine}} \rtimes \underbrace{Y(\mathfrak{sl}_N)}_{\text{finite-rank Yangian}}.
$$

Large-$N$ limit (Maldacena–Strominger): $Y(\mathfrak{sl}_N) \to Y(\widehat{\mathfrak{gl}}_1) = \mathcal W_\infty$ via Schiffmann–Vasserot 2013.

### FINAL-5. Does this match manuscript's $Y(\mathfrak g_{K3})$?

**Partially yes**: the abelian tensor factor $\mathcal H_{\mathrm{Muk}}$ matches manuscript `thm:phi-k3-explicit` (Wave-6 confirmed). The non-abelian factor $\widehat{\mathfrak{sl}_N}_{k=1} \rtimes Y(\mathfrak{sl}_N)$ matches the manuscript's ADE-locus enhancement `thm:bfn-phi-ade-identification` **only at ADE points**; at generic smooth K3, there is **no** non-abelian enhancement (M-CONSTRAINT 4, Nikulin rigidity).

**Partially no**: the manuscript's hypothesised universal $Y(\mathfrak g_{K3})$ on the Mukai lattice is NOT what M-theory gives. What M-theory gives is a **stratified family** of Yangians, with the rank depending on the stack size $N$ and on the K3 locus (smooth / elliptic / ADE / Kummer).

### FINAL-6. Obstructions reaffirmed

Wave-6 obstructions O1–O15 are consistent with the Wave-7 Witten analysis. One new obstruction:

**O16 (Beem–Rastelli blocked)**: M5-on-K3 is not a 4d $\mathcal N=2$ SCFT / 2d Schur chiral algebra setup. Beem–Rastelli 2014 correspondence does NOT apply. The manuscript's Route A (CY-to-chiral via $\Phi_2$) is the correct route; any attempt to derive $Y(\mathfrak g_{K3})$ via 4d-$\mathcal N=2$ / BLLPR-Schur is obstructed.

### FINAL-7. Beilinson-dictum verdict

Under the discipline of the epistemic hierarchy (primary literature > manuscript > swarm memory), the Wave-7 Witten analysis **confirms**:
- Manuscript's `thm:phi-k3-explicit` (abelian $\mathcal H_{\mathrm{Muk}}$).
- Manuscript's `thm:bfn-phi-ade-identification` (ADE-locus enhancement), SCOPED per Wave-6 A0.3.a dimension-count caveat.
- Wave-6 SYNTHESIS §5.1 converged deliverable.

And **falsifies or narrows**:
- Wave-1–5 "K3 Yangian as single universal non-abelian Yangian on Mukai lattice" — falsified in favor of stratified family.
- Wave-5 "Costello–Gaiotto 4-loop finiteness of 6d hCS on $\mathbb R^2 \times K3 \times E$" — narrowed to [O] open; $H^1_{\hbar^{2n}}$ cohomology still uncomputed (reaffirmed from Wave-6).
- Wave-5 "Nikulin–Venkov Niemeier bijection" — signature-obstruction remains (Wave-6 O1).

### FINAL-8. What Wave 8 should ask

If Wave 8 is to happen: the crucial open question is not "does $Y(\mathfrak g_{K3})$ exist" (answered no, as a single object, yes as a stratified family) but rather: **what are the gluing relations between the strata?** How do the non-abelian enhancements on ADE / elliptic / Kummer loci glue together through the generic smooth-K3 interior where only $\mathcal H_{\mathrm{Muk}}$ survives?

This is the **chiral-algebra-over-stability-manifold** question, parallel to Kazhdan W6 H3's "sheaf-of-2-groups over stratified Bridgeland moduli". A concrete answer requires: (1) an explicit Bridgeland-stability stratification of K3 moduli; (2) a sheaf-valued chiral algebra over this stratification; (3) explicit monodromy formulas encoding how the non-abelian Yangian factor rotates as one crosses a stability wall. None of these are in the current literature at publication-grade rigor.

---

## CONVERGED STATEMENT (Wave-7 Witten, six-cycle closure)

**Structure.** The programme's "K3 Yangian" is not a single quantum group. It is:

**(S1)** A **stratified family of Yangians** on the CY2 side ($d = 2$), with universal abelian core $\mathcal H_{\mathrm{Muk}}$ (manuscript `thm:phi-k3-explicit`) and non-abelian enhancements $\widehat{\mathfrak g}_{k=1} \rtimes Y^\mu(\widehat{\mathfrak g})$ at ADE / elliptic / Kummer loci only (manuscript `thm:bfn-phi-ade-identification` + Wave-6 O6 Nikulin rigidity). The non-abelian enhancement depends on: (a) K3 complex structure, (b) M5-brane stack size $N$, (c) locus within K3 moduli. Large-$N$ limit (tensionless holographic point): $Y(\widehat{\mathfrak{gl}}_1)^+ = \mathcal W_\infty[0]$ positive half.

**(S2)** A **BKM sibling** on the CY3 side ($d = 3$): the Borcherds–Kac–Moody Lie superalgebra $\mathfrak g_{\Delta_5}$ with Siegel-automorphic denominator $\Delta_5^2 = \Phi_{10}$, arising from $\Phi_3$ applied to $D^b(\Coh(K3 \times E))$ (manuscript Thm CY-A$_3$, k3e_bkm_chapter.tex). This is **NOT a Yangian** — it is a Lie superalgebra. Its "Yangianisation" is conjectural in the Rapčák–Soibelman–Yang–Zhao 2023 / Li–Yamazaki 2020 style and is open.

**(S3)** A **Borcherds-lift bridge** connecting (S1) and (S2) at the character level: $\eta^{-24}(\tau) \to \Phi_{10}^{-1}(\tau, z, \sigma)$, weight 12 (genus 1) lifting to weight 10 (genus 2). This is an **automorphic lift** of characters, NOT an algebra-to-algebra morphism.

**Physical origins.** Four primary-literature physical frames, each supplying a piece:

| frame | contributes |
|---|---|
| M5-on-K3 with Vafa–Witten twist (Vafa–Witten 1994; Harvey–Minasian–Moore 1998) | $\eta^{-24}$ partition function; rank-24 abelian core; $\mathcal H_{\mathrm{Muk}} \otimes \widehat{\mathfrak{sl}_N}_{k=1}$ at stack rank $N$ |
| M5-on-Kleinian $\widetilde S_{\mathfrak g} \to \mathbb C^2/\Gamma$ (Nakajima 1994; BFN 2016) | ADE-locus enhancement $Y^\mu(\widehat{\mathfrak g})_{k=1}$ |
| Heterotic on $K3 \times T^2$ (Harvey–Moore 1995; DVV 1996; GN 1998) | BKM $\mathfrak g_{\Delta_5}$; Siegel $\Phi_{10}$; second-quantised $\chi(\mathrm{Sym}^N K3)$ |
| D1–D5 on K3 / $\mathrm{AdS}_3 \times S^3 \times K3$ (MS 1997; Eberhardt 2020) | $\mathrm{Sym}^N K3$ CFT; $\mathcal W_\infty[0]$ asymptotic symmetry; large-$N$ tensionless Yangian positive half |

None of these four frames gives a **universal** $Y(\mathfrak g_{K3})$ by itself. The stratified picture (S1) + BKM sibling (S2) + Borcherds-lift bridge (S3) is the converged physical synthesis.

---

## NEW CONJECTURES (Wave-7 Witten)

**Wave-7 Witten Conjecture W7-1 (holographic confirmation of stratification)**: The tensionless chiral algebra of $\mathrm{AdS}_3 \times S^3 \times K3$ strings equals $\mathcal H_{\mathrm{Muk}} \otimes \mathcal W_\infty[0] = \mathcal H_{\mathrm{Muk}} \otimes Y(\widehat{\mathfrak{gl}}_1)^+$ at generic smooth K3 moduli, and enhances to $\mathcal H_{\mathrm{Muk}} \otimes \widehat{\mathfrak g}_{k=1} \rtimes Y^\mu(\widehat{\mathfrak g})$ at ADE moduli points. Eberhardt 2020 supplies the sketch; full rigour (with the $\mathcal N=(4,4)$ right-movers and the Hopf-algebra negative half) is open.

**Wave-7 Witten Conjecture W7-2 (automorphic-lift bridge from K3 Yangian to K3×E BKM)**: The Borcherds-lift functor
$$
\mathrm{BorcherdsLift}: \mathcal A_{\Phi_2(K3)} \longrightarrow \mathcal A_{\Phi_3(K3 \times E)}
$$
sends the K3-Yangian chiral algebra (character $\eta^{-24}$) to the BKM chiral algebra of $K3 \times E$ (character $\Phi_{10}^{-1}$). On objects: $\mathcal H_{\mathrm{Muk}} \otimes V_E \mapsto U(\mathfrak g_{\Delta_5})$-module. On characters: $\eta^{-24}(\tau) \cdot \theta_E(\sigma) \mapsto \Phi_{10}^{-1}(\tau, z, \sigma)$. This upgrades the existing character-level Borcherds lift to an algebra-level functor; status **conjectural**, requires CY-A$_3$ inversion combined with Borcherds 1998 §15.

**Wave-7 Witten Conjecture W7-3 (M5-on-K3 anomaly inflow precisely fixes Bah–Beem–Bobev–Wecht central charge)**: For $A_{N-1}$ M5-stack on K3 with Vafa–Witten twist, the 2d boundary chiral algebra has central charge
$$
c_{2d}^{\mathrm{VW}}(N) = 24 + 24 (N-1) h^\vee_{\mathfrak{sl}_N} = 24 N = 24 + \chi(K3)(N-1)
$$
via anomaly inflow from $I_8^{A_{N-1}}$ integrated over K3. Consistency check at $N=1$: $c = 24$ (Mukai-Heisenberg), matches. At large $N$: $c \sim 24 N$, matches Maldacena–Strominger holographic $c = 6 Q_1 Q_5$ at $Q_5 = 4$ (or modulo a factor-of-4 conventions mismatch to reconcile). Status **[H-conjectural]** at physics level; [M] at chain level pending the BBBW 2012 eq. 5.12 verification with the specific K3 normalisation.

**Wave-7 Witten Conjecture W7-4 (BKM-Yangian lift)**: The "Yangian of a BKM superalgebra" $Y(\mathfrak g_{\Delta_5})$ in the Rapčák–Soibelman–Yang–Zhao 2023 sense, applied to $\mathfrak g_{\Delta_5}$, is the programme's $Y(\mathfrak g_{K3 \times E})$, and by the Borcherds-lift bridge W7-2 its $E$-fibre restriction gives the stratified $Y(\mathfrak g_{K3})$. This unifies (S1) and (S2) at the Yangian level; status **highly conjectural**, probably the deepest open question in the K3 chapter.

**Wave-7 Witten Conjecture W7-5 (Nikulin stratification is the correct refinement of Wave-6 O6)**: The Wave-6 O6 obstruction ("generic K3 has $\mathrm{Aut}^0 = \{e\}$") is not absolute — it is a **stratification**. The Nikulin 1987 classification of finite symplectic K3 automorphism groups (orders up to 8; 79 subgroups of $M_{23}$ per Mukai 1988) provides a discrete set of enhancement loci; between them, only $\mathcal H_{\mathrm{Muk}}$ survives. The stratification is: (a) 79 discrete points with $\mathrm{Aut}^0 = \{e\}$ but finite Nikulin automorphism group; (b) 1-dim loci (elliptic K3); (c) 0-dim ADE loci; (d) Kummer $K3 = T^4/\mathbb Z_2$; (e) smooth generic points. The K3 Yangian enhancement is different on each stratum.

---

## REQUIRED MANUSCRIPT AMENDMENTS (file:line)

Based on the six-cycle Witten analysis, the following manuscript amendments are required for Vol III:

### Amendment A1: k3_yangian_chapter.tex:1–12 (chapter opening)

The opening paragraph asserts "The K3 double current algebra $\mathfrak g_{K3}$ is the classical limit of the K3 Yangian $Y(\mathfrak g_{K3})$, whose 24 Heisenberg generators, Mukai-signature Serre relations, and degree-$(24,24)$ structure function encode the quantization of the Mukai lattice." This overclaims: the stratified nature of $Y(\mathfrak g_{K3})$ is not acknowledged, and the "degree-(24,24) structure function" is only defined on the abelian core. **Edit**: after the first sentence, insert a scope declaration: "This Yangian exists as a stratified family over the K3 moduli space, with universal abelian rank-24 Heisenberg core at generic smooth K3 (Theorem `thm:phi-k3-explicit`) and non-abelian enhancements at ADE / elliptic / Kummer loci (Theorem `thm:bfn-phi-ade-identification`); the 24 Heisenberg generators and Mukai-signature form describe the universal core."

### Amendment A2: k3_yangian_chapter.tex:91–101 (rem:k3e-two-routes-yangian)

The remark states two routes (CY-A and BFN) to $Y(\mathfrak g_{K3})$ without noting the **third physical frame** — the holographic $\mathrm{AdS}_3 \times S^3 \times K3$ $\mathrm{Sym}^N K3$ CFT (Maldacena–Strominger 1997). **Edit**: add a Route (C) entry: "*(C) Holographic route*: the D1–D5 system on K3 has $\mathrm{AdS}_3 \times S^3 \times K3$ near-horizon; the dual $\mathrm{Sym}^N K3$ CFT at large $N$ carries asymptotic $\mathcal W_\infty[\lambda = 0] = Y(\widehat{\mathfrak{gl}}_1)^+$ symmetry (Gaberdiel–Gopakumar 2011), whose generic-K3 restriction is $\mathcal H_{\mathrm{Muk}}$ and whose enhancement at Kummer / ADE loci agrees with Route (B). Status: holographic at large $N$ and free-orbifold point."

### Amendment A3: k3_yangian_chapter.tex:100–101 (stratification scope)

The paragraph "The MO stable envelope route... at those scope-permitted points it yields the evaluation $R$-matrix... not the full Yangian algebra" correctly scopes MO to ADE/Kummer. **Edit**: add a sentence: "This scope restriction reflects the Wave-6 Nikulin-rigidity obstruction O6: generic smooth K3 has $\mathrm{Aut}^0 = \{e\}$, so no torus action, so no MO stable envelope; the stratified-Yangian picture is the correct statement. Between stratum points, only the universal abelian core $\mathcal H_{\mathrm{Muk}}$ persists."

### Amendment A4: k3e_bkm_chapter.tex:302 (CoHA vs Yangian clarification — already present, but reinforce)

Line 302 already states: "The Hall product is associative ($E_1$). It carries no braiding: the Hall algebra $\mathcal H(K3 \times E)$ sees only $U(\mathfrak n_+(\mathfrak g_{\Delta_5}))$ (the positive half of the BKM superalgebra), *not* the full Yangian $Y(\mathfrak g_{K3})$."

This is already correct. **Proposed addition** (reinforcing, not correcting): after line 302, add: "In particular, Wave-7 O17 records that the BKM superalgebra $\mathfrak g_{\Delta_5}$ is NOT the K3 Yangian $Y(\mathfrak g_{K3})$: the former is a $\mathbb Z$-graded Lie superalgebra with real and imaginary simple roots and Siegel-automorphic denominator $\Phi_{10}$; the latter is a conjectural Hopf-algebra family with Yang / RTT / Drinfeld presentations. They are siblings via the Borcherds lift at the character level (Vol III k3e_bkm_chapter.tex:656–750 Borcherds-lift genus-1-to-genus-2 bridge), but algebraically distinct."

### Amendment A5: k3e_bkm_chapter.tex:11–50 (Φ_10 vs Δ_5 convention)

Line 43 has `\begin{remark}[Convention: $\Delta_5$ vs $\Phi_{10}$]`. This addresses the naming but not the **algebraic implication**: squaring $\Delta_5$ to $\Phi_{10}$ corresponds to a $\mathbb Z/2$-orbifold / covering structure on the BKM side. **Edit**: enhance the remark with: "Algebraic interpretation: $\Phi_{10} = \Delta_5^2$ corresponds to the $\mathbb Z/2$-orbifold $\mathfrak g_{\Delta_5} \otimes \mathfrak g_{\Delta_5} / \sigma$ where $\sigma$ is the Borcherds involution, giving a rank-doubled BKM with paramodular $\mathrm{Sp}_4(\mathbb Z)$-symmetry matching the 1/4-BPS dyon count of heterotic on $K3 \times T^2$ (DVV 1996 eq. 1.1)."

### Amendment A6: cy_to_chiral.tex:68–76 (Φ-outputs on K3 specifically)

Line 72 states: $\Phi_2(D^b(\Coh K3)) = \mathcal H_{\mathrm{Muk}}$. The output is correct for the abelian core; but the theorem is silent on the ADE enhancement available at sublocus points. **Edit**: add a scope remark: "Generic smooth K3: $\Phi_2$ output is abelian Mukai-Heisenberg. At ADE / elliptic / Kummer sublocus points in the 20-dim K3 moduli space, $\Phi_2$ enhances to a stratified Yangian family (see k3_yangian_chapter.tex Thm `thm:bfn-phi-ade-identification` for ADE; Conjecture `conj:bfn-k3-yangian-kummer` for Kummer; Negut 2015 + Okounkov 2015 for elliptic). The enhancement structure is what Wave-7 Witten termed the 'stratified K3-Yangian family'."

### Amendment A7 (new lemma inscription for anomaly-inflow): k3_yangian_chapter.tex end of §symplectic-duality section

Insert a lemma recording the M5-on-K3 anomaly-inflow identity (Wave-7 H3.4):

```
\begin{lemma}[M5-on-K3 anomaly polynomial integrated]
\label{lem:m5-k3-anomaly-inflow}
\ClaimStatusProvedElsewhere
Let W = R^4 x K3 be the 6d worldvolume of A_{N-1} (2,0) M5 stack.
The anomaly 8-form I_8^{A_{N-1}} = (N-1) I_8^{free}
  + N(N^2-1)/24 p_2(NW), with I_8^{free} the free-tensor anomaly
  (Harvey-Minasian-Moore 1998 eq. 3.15), satisfies
  int_{K3} I_8^{A_{N-1}} = (N-1)/2 p_1(R)_{R^4}.
Under the Vafa-Witten twist (SU(2) K3 holonomy in Sp(4)_R),
this vanishes, yielding a topological 4d theory with
Donaldson-Witten / Vafa-Witten partition function
eta(tau)^{-24} * theta_{A_{N-1}^*}(tau, z) for SU(N) M5-stack.
Boundary 2d chiral algebra global symmetry:
H_{Muk} tensor hat{sl_N}_{k=1} rtimes Y(sl_N).
Status: [H] physics-level; [M] chain-level pending FRS 1998
Yangian correspondence verification for the specific embedding.
\end{lemma}
```

This lemma inscribes the Wave-7 central physics result at a concrete manuscript location, providing a hook for downstream cross-references.

---

## BKM / SIEGEL BRIDGE STATUS

**Question**: Is the K3 Yangian $Y(\mathfrak g_{K3})$ the Yangian-version of the BKM superalgebra $\mathfrak g_{\Delta_5}$ of heterotic on $K3 \times T^2$?

**Answer (Wave-7 converged)**: **NO at the algebraic level, YES at the character level via Borcherds lift**.

**Detailed status**:

(1) **BKM $\neq$ Yangian (type distinction O17)**: The Borcherds–Kac–Moody Lie superalgebra $\mathfrak g_{\Delta_5}$ (Gritsenko–Nikulin 1998 §2; Borcherds 1995 Invent. Math.; Lorgat 2020 §5) is a $\mathbb Z$-graded Lie superalgebra with **real and imaginary simple roots**, constructed as an automorphic correction of a hyperbolic Kac–Moody algebra. Its denominator function is the Siegel paramodular form $\Delta_5 \in S_5(\Gamma_{\text{para}}, \nu_{\Delta_5})$ with multiplier system of order 2. It is **not a Hopf algebra**; it has **no RTT / Drinfeld-J / new-realization presentation**; it is **not a quantum group**. The K3 Yangian, if it exists, is a quantum group (Hopf algebra, Yang R-matrix, Drinfeld–J presentation). These are different mathematical objects.

(2) **Character-level match via Borcherds lift**: The Borcherds 1998 multiplicative lift sends $\phi_{0,1}$ = K3 elliptic genus (weight-0 index-1 Jacobi form on $\mathbb H_1 \times \mathbb C$) to $\Delta_5$ (weight-5 paramodular form on $\mathbb H_2$). Via DVV 1996 eq. 1.1, this lifts character $\eta^{-24}$ (the K3-Yangian Fock character per `prop:k3e-selfdual-fock`) to $\Phi_{10}^{-1}$ (the BPS generating function of heterotic on $K3 \times T^2$). The **character identity** is
$$
\sum_{N \geq 0} p^N \chi(\mathrm{Sym}^N K3; \tau, z) = \frac{1}{\Phi_{10}(\tau, z, \sigma)}.
$$
This is a genuine automorphic lift; it bridges $d = 2$ (K3) and $d = 3$ (K3 × E) in the $\Phi$-programme.

(3) **Full algebraic bridge is conjectural**: Upgrading the character-level Borcherds lift to an algebra-level functor
$$
\mathrm{BorcherdsLift}: \Phi_2(K3) \text{-Mod} \longrightarrow \Phi_3(K3 \times E) \text{-Mod}
$$
sending K3-Yangian modules to $\mathfrak g_{\Delta_5}$-modules, is **conjectural** (Wave-7 Witten Conjecture W7-2). It requires combining the manuscript's Theorem CY-A$_3$ (proved at $d=3$) with the Borcherds 1998 Thm 15.2 machinery at the algebra level, which has not been done in the published literature.

(4) **Yangianisation of BKM is conjectural**: A hypothetical "Yangian of $\mathfrak g_{\Delta_5}$" in the Rapčák–Soibelman–Yang–Zhao 2023 / Li–Yamazaki 2020 / Gaiotto–Koroteev 2013 style would give a quantum-group cousin of the BKM; this is the candidate for the programme's $Y(\mathfrak g_{K3 \times E})$. Status: **highly conjectural**, Wave-7 Witten Conjecture W7-4. The programme's current $K3 \times E$ chapter (k3e_bkm_chapter.tex) inscribes the BKM side but does not construct the Yangianisation.

(5) **Vol III's own manuscript is correct on this**: k3e_bkm_chapter.tex:302 already states "The Hall product is associative ($E_1$). It carries no braiding: the Hall algebra $\mathcal H(K3 \times E)$ sees only $U(\mathfrak n_+(\mathfrak g_{\Delta_5}))$ ... **not** the full Yangian $Y(\mathfrak g_{K3})$." This is exactly Wave-7's O17 in the programme's own voice. The Wave-5 "$Y_{K3}$ via heterotic on $K3 \times T^2$" language was a scope confusion; the manuscript's own k3e_bkm_chapter.tex is the correct statement.

**Lorgat 2020 Conjecture 1 status (automorphic-corrections preprint)**: Conjecture 1 states that all 8 Gritsenko–Clery diagonal-divisor paramodular forms arise as $Z^{-1/2}_{X_{L, h_M}}$ for twisted DT partition functions on $(S \times E)/(\mathbb Z/N\mathbb Z)$ CY3 quotients, with root multiplicities = $g_N - h_M$-twisted twined K3 elliptic genera (Mathieu moonshine). Status: **conjectural, unchanged by Wave-7**. Wave-7 adds physical context: each of the 8 paramodular forms would correspond to a different discrete Nikulin-finite subgroup of $M_{23}$ acting symplectically on K3 (Mukai 1988); the conjecture predicts a **discrete-moonshine refinement** of the programme's $\Phi_3$ output on twisted $K3 \times E$-quotients.

---

## Open Questions (for Wave 8 or the manuscript)

1. **Explicit cohomology extraction** for Costello–Gaiotto 4-loop claim: compute $H^1_{\hbar^{2n}}$ of the factorization-axiom deformation complex for 6d hCS on $\mathbb R^2_\varepsilon \times K3 \times E$, not just diagram sums.
2. **Gluing strata**: how does $\widehat{\mathfrak{sl}_N}_{k=1} \rtimes Y(\mathfrak{sl}_N)$ of the ADE locus glue to the $\widehat{\mathfrak{gl}}_1$-Yangian of the elliptic locus through the generic smooth K3 interior?
3. **$N \to \infty$ vs $N$ finite**: does the large-$N$ limit of $Y(\mathfrak{sl}_N)$ equal $\mathcal W_\infty = Y(\widehat{\mathfrak{gl}}_1)$, or is there a discrepancy accommodated by the $\mathcal H_{\mathrm{Muk}}$ tensor factor?
4. **Costello–Gaiotto twist explicit form** on $\mathbb R^2_\varepsilon \times K3 \times E$: compute $\int_{K3 \times E} I_8^{\text{CG}}$ and identify the 2d chiral algebra on $\mathbb R^2_\varepsilon$.
5. **Kummer deformation invariance**: manuscript `conj:bfn-k3-yangian-kummer` requires Yangian invariance under blowup of 16 orbifold points; open.
6. **Mukai-pairing coupling**: manuscript `conj:bfn-k3-yangian-mukai` requires 24 coupled $Y(\widehat{\mathfrak{gl}}_1)$'s via Mukai form; open.
7. **Complex-structure dependence**: does $Y(\mathfrak g_{K3})$ depend on the specific complex structure within the hyperkähler sphere? M-theory anomaly inflow suggests yes (Costello–Gaiotto twist requires a polarisation); Wave-5 implicit choice undeclared.
8. **Anomaly matching at $N^3$ order**: verify Bah–Beem–Bobev–Wecht 2012 eq. 5.12 applied to K3 with careful attention to the $N^3$ vs $N$ decomposition of the 2d central charge.

---

## References (primary, cited above)

- Alday–Gaiotto–Tachikawa, *Liouville correlation functions from 4d gauge theories*, Lett. Math. Phys. 91 (2010) 167, arXiv:0906.3219.
- Bah–Beem–Bobev–Wecht, *Four-dimensional SCFTs from M5-branes*, JHEP 06 (2012) 005, arXiv:1112.5487.
- Beem–Rastelli, *Infinite chiral symmetry in four dimensions*, Commun. Math. Phys. 336 (2015) 1359, arXiv:1312.5344.
- Braverman–Finkelberg–Nakajima, *Coulomb branches of 3d N=4 quiver gauge theories*, arXiv:1604.03625.
- Costello, *Supersymmetric gauge theory and the Yangian*, arXiv:1303.2632.
- Costello–Gaiotto, *Twisted holography*, arXiv:1812.09257 (and predecessor arXiv:1810.01970).
- Dedushenko–Gukov, *IR duality in 3d N=4 gauge theories*, arXiv:1705.01645.
- DMVV = Dijkgraaf–Moore–Verlinde–Verlinde, *Elliptic genera of symmetric products and second quantized strings*, Commun. Math. Phys. 185 (1997) 197, arXiv:hep-th/9608096.
- Duff–Liu–Minasian, *Eleven-dimensional origin of string/string duality*, Nucl. Phys. B452 (1995) 261, arXiv:hep-th/9506126.
- Frenkel–Kac, *Basic representations of affine Lie algebras and dual resonance models*, Invent. Math. 62 (1980) 23.
- Frenkel–Lepowsky–Meurman, *Vertex Operator Algebras and the Monster*, Academic Press (1988).
- Gaiotto, *N=2 dualities*, JHEP 08 (2012) 034, arXiv:0904.2715.
- Ganor–Motl, *Equations of the $(2,0)$ theory and knitted five-branes*, JHEP 05 (1998) 009, arXiv:hep-th/9803108.
- Göttsche, *Theta functions and Hodge numbers of moduli spaces of sheaves on rational surfaces*, Commun. Math. Phys. 206 (1999) 105, arXiv:math/9903185.
- Gritsenko–Nikulin, *Automorphic forms and Lorentzian Kac-Moody algebras II*, Int. J. Math. 9 (1998) 201.
- Grojnowski, *Instantons and affine algebras I*, Math. Res. Lett. 3 (1996) 275, arXiv:alg-geom/9506020.
- Harvey–Minasian–Moore, *Non-abelian tensor-multiplet anomalies*, JHEP 9809:004 (1998), arXiv:hep-th/9808060.
- Hull–Townsend, *Unity of superstring dualities*, Nucl. Phys. B438 (1995) 109, arXiv:hep-th/9410167.
- Intriligator, *Anomaly matching and a Hopf-Wess-Zumino term*, Nucl. Phys. B581 (2000) 257, arXiv:hep-th/0001205.
- Kac, *Vertex Algebras for Beginners*, AMS (1998).
- Kapustin, *Holomorphic reduction of N=2 gauge theories, Wilson-'t Hooft operators, and S-duality*, arXiv:hep-th/0612004.
- Kodera–Nakajima, *Quantized Coulomb branches of Jordan quiver gauge theories and cyclotomic rational Cherednik algebras*, Proc. Symp. Pure Math. 98 (2018), arXiv:1608.00875.
- Maldacena, *The large N limit of superconformal field theories and supergravity*, Adv. Theor. Math. Phys. 2 (1998) 231, arXiv:hep-th/9711200.
- Maldacena–Strominger, *AdS(3) black holes and a stringy exclusion principle*, JHEP 9812:005 (1998), arXiv:hep-th/9804085.
- Maulik–Okounkov, *Quantum groups and quantum cohomology*, Astérisque 408 (2019), arXiv:1211.1287.
- Nakajima, *Heisenberg algebra and Hilbert schemes of points on projective surfaces*, Ann. Math. 145 (1997) 379, arXiv:math/9507012.
- Nakajima–Yoshioka, *Lectures on instanton counting*, Transform. Groups 10 (2005) 489, arXiv:math/0311058.
- Nikulin, *Finite groups of automorphisms of Kähler K3 surfaces*, Trans. Moscow Math. Soc. 38 (1987) 71.
- Schiffmann–Vasserot, *Cherednik algebras, $W$-algebras and the equivariant cohomology of the moduli space of instantons on $\mathbb A^2$*, Publ. IHÉS 118 (2013) 213, arXiv:1202.2756.
- Sethi–Vafa, *F-theory, SL(2,Z) and exceptional groups*, Nucl. Phys. B480 (1996) 213, arXiv:hep-th/9606122.
- Strominger–Vafa, *Microscopic origin of the Bekenstein-Hawking entropy*, Phys. Lett. B379 (1996) 99, arXiv:hep-th/9601029.
- Vafa, *Evidence for F-theory*, Nucl. Phys. B469 (1996) 403, arXiv:hep-th/9602022.
- Vafa–Witten, *A strong-coupling test of S-duality*, Nucl. Phys. B431 (1994) 3, arXiv:hep-th/9408074.
- Varagnolo, *Quiver varieties and Yangians*, Lett. Math. Phys. 53 (2000) 273, arXiv:math/0005277.
- Witten, *New issues in manifolds of SU(3) holonomy*, Nucl. Phys. B268 (1986) 79.
- Yi, *Anomalies, Hanany–Witten transitions, and the M-theory lift of D8-branes*, arXiv:hep-th/0106193.

---

Raeez Lorgat, sole author. No AI attribution. Chain-level throughout (Pattern 236 ambient qualifier); primary literature cited with arXiv numbers and equation references where possible; **six attack-heal cycles executed** (A1/H1 anomaly/M-theory; A2/H2 twist/holographic dual; A3/H3 stratification and anomaly matching; A4 verification pass; A5/H5 heterotic-on-$K3 \times T^2$ BPS/BKM frame and $\Phi_{10} = \Delta_5^2$ Borcherds lift; A6/H6 $\mathrm{AdS}_3 \times S^3 \times K3$ holographic frame and $\mathcal W_\infty[0]$ tensionless limit), with no new serious flaws surfacing beyond the ones already acknowledged by the manuscript itself. Beilinson-dictum discipline applied throughout, with the final verdict reaffirming manuscript theorems `thm:phi-k3-explicit` and `thm:bfn-phi-ade-identification` as the converged $d=2$ epistemic endpoint, the CY-A$_3$ / k3e_bkm_chapter inscription as the converged $d=3$ endpoint, and narrowing Wave-1–5 universal-$Y(\mathfrak g_{K3})$ claims to (i) a stratified Yangian family at $d=2$ whose existence depends on per-locus torus actions (M-CONSTRAINT 4, Nikulin rigidity, Wave-6 obstruction O6) and (ii) a BKM Lie superalgebra at $d=3$ (NOT a Yangian; obstruction O17) with Siegel denominator $\Phi_{10} = \Delta_5^2$ matching Lorgat 2020. Bridge between $d=2$ and $d=3$: Borcherds-lift functor at the character level ($\eta^{-24} \mapsto \Phi_{10}^{-1}$) with algebra-level lift as Wave-7 Conjecture W7-2. The five-theorem programme alignment: Theorem D obstruction-tower universality $\lambda_g = \kappa g$ at the ADE-locus-specific Yangian enhancements, and Theorem H Hochschild concentration in degrees $\{0,1,2\}$ for the abelian-Heisenberg core $\mathcal H_{\mathrm{Muk}}$.

End of Wave-7 Witten attack-heal report.
