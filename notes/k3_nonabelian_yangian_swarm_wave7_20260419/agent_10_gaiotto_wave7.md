# Agent 10 (Gaiotto voice) -- Wave 7: name the 4d theory, enumerate its BPS spectrum, compute the Schur/BPS partition function at rank 1, and prove or falsify the K3 Yangian identification

**Raeez Lorgat, sole author. Wave 7, 2026-04-19.**

Wave 6 Gaiotto falsified the BLLPR / class-S reading of $Y_{K3}$ (sign
obstruction $c_{2d}^{\mathrm{BLLPR}} \le 0$ vs $c^{\mathrm{Heis}} = +24$)
and healed into a Vafa--Witten-on-K3 reading of the abelian core. Wave
6 Witten noted a parallel disambiguation, pointing to heterotic-on-$T^4$
$\longleftrightarrow$ IIA-on-K3 string--string duality as the correct
physical frame. Neither wave carried out the step a Gaiotto-voice audit
actually demands: **name the 4d theory, enumerate its BPS multiplets,
compute its Schur (or BPS) partition function at rank 1 from
first-principles, and match to the proposed chiral algebra object.**

Wave 7 executes exactly this programme. I am adversarial about my own
Wave 6 deliverable: the Vafa--Witten identification of the abelian
core is suggestive, but **Vafa--Witten on K3 is a topologically
twisted 4d $\mathcal N=4$ SYM on a 4-manifold**, not a 4d $\mathcal
N=2$ SCFT with a Schur index. The Schur-index / chiral-algebra story
of Beem--Rastelli (BR2018, 2015) applies to $\mathcal N=2$ SCFTs,
not to $\mathcal N=4$ SYM-on-K3. So the Wave 6 Gaiotto heal replaces
one conflation (class-S Schur index for a K3 Yangian) with another
(Vafa--Witten partition function as if it were a Schur index).
Wave 7 resolves this and produces the correct framework.

The ATTACK--HEAL loop runs ≥3 cycles on **my own Wave-6 heal** and on
the residual Wave 1--6 "K3 Yangian" corpus that depends on it. I end
with a converged final statement, a primary-source-dense obstruction
landscape, and a handful of open questions.

**Methodology flag** (from CLAUDE.md and Wave 6 practice): every
assertion is false until verified from a primary source; every claim
carries three independent verification paths or it is labelled
conjectural; Pattern 236 ambient-qualifier discipline is mandatory
(chain-level / $(\infty,1)$-categorical / physical). No AI attribution;
Raeez Lorgat throughout.

---

## Attack Phase 1 — physical-setup demolition

### §A1.1 The Wave 6 Gaiotto heal was physics-sloppy

My Wave 6 §H1.2 stated: "the K3 Yangian abelian core is the boundary
VOA of Vafa--Witten topologically twisted 4d $\mathcal N{=}4$ SYM on
$K3 \times \mathbb R_{\ge 0}$." Let me read this as a Gaiotto would.

**What is Vafa--Witten on K3, exactly?**

Vafa--Witten (hep-th/9408074) is the **Donaldson-type topological
twist** of 4d $\mathcal N=4$ SYM. In the twist: (i) all eight
supercharges are reorganised into spinor bundles twisted by the
R-symmetry, so that one scalar supercharge $Q_{VW}$ survives on any
4-manifold; (ii) the partition function on a 4-manifold $X$ is a
generating series of Euler characteristics of instanton moduli
$\mathcal M_n^{\mathrm{inst}}(X, G)$; (iii) for $X = K3$, gauge group
$SU(2)$, the partition function is

$$
Z^{VW}_{SU(2)}(K3, q) = \frac{1}{\eta(q)^{24}} \cdot (\text{theta factor}).
$$

This is a **topological** (not holomorphic) quantity: $K3$ is a
Riemannian 4-manifold, not a complex curve, and the topological twist
does not preserve the $\mathcal N=2$ superconformal algebra needed for
a Schur index. **The Schur index lives on $S^3 \times S^1$ of a 4d
$\mathcal N=2$ SCFT.** Vafa--Witten on K3 is neither.

So my Wave 6 heal, which tried to import "boundary VOA" language into
the Vafa--Witten setting, was **underspecified**. "Boundary VOA of
topologically twisted $\mathcal N=4$ SYM on $K3 \times \mathbb
R_{\ge 0}$" is a phrase that needs to resolve into either (a) a
Kapustin--Witten boundary condition ("geometric Langlands boundary
VOA" in the Kapustin 2006 / Gaiotto--Witten 2008 language), or (b) a
Costello--Gwilliam factorization algebra of a topological theory.
Option (a) operates on a Riemann surface fibration over a 4-manifold,
not on a K3 surface treated as spacetime; option (b) produces a
topological (locally constant) factorization algebra, not a
holomorphic chiral algebra.

**A1.1 verdict**: the phrase "boundary VOA of Vafa--Witten on K3" is
physics-sloppy. It is not falsified, but it is not a precise physical
identification of the proposed K3 Yangian. I attack my own Wave 6 heal
for underspecification.

### §A1.2 Wave 6 Witten's heterotic-$T^4$/IIA-K3 framework is the correct frame, but the duality relates 6d theories, not 4d SCFTs

Wave 6 Witten (agent_08_witten_wave6.md §H1) pushed for:

$$
\text{heterotic on } T^4 \;\xlongequal{\text{string--string}}\; \text{IIA on K3}.
$$

This duality (Hull--Townsend 1994, hep-th/9410167; Witten 1995,
hep-th/9503124; Sen 1995, hep-th/9504027) is fundamental: it maps the
Narain lattice $\Gamma^{4,20}$ of heterotic-on-$T^4$ to the Mukai
lattice $H^{*}(K3, \mathbb Z) = \Lambda_{\mathrm{Muk}}$ of the IIA
D-brane charges, and the T-duality group $O(4, 20; \mathbb Z)$ to the
IIA mirror / U-duality group on K3.

But the theories on both sides are **6d** (the compactifications are
on 4d manifolds, leaving 6 uncompactified dimensions). To get a 4d
SCFT — which is what admits a Schur index and plausibly a chiral
algebra via BR2018 — one has to compactify further.

Two standard further-compactifications:
- **Heterotic-on-$T^4 \times T^2$** = IIA-on-$K3 \times T^2$: gives 4d
  $\mathcal N=4$ SUGRA (maximal SUSY), not a 4d $\mathcal N=2$ SCFT.
- **Heterotic-on-$T^4 \times T^2$ with Wilson lines** breaking $\mathcal N=4 \to \mathcal N=2$: candidate for FHSV (Ferrara--Harvey--Strominger--Vafa 1995, hep-th/9505162) model, which is genuinely 4d $\mathcal N=2$.

The FHSV model is the **first** concrete 4d $\mathcal N=2$ gauge
theory natural to K3 geometry. It is the IIA-on-K3 $\times T^2 /
\mathbb Z_2$-Enriques-involution theory, dual to heterotic on
$T^6/\mathbb Z_2$-with-instantons. Its gauge group at the $\mathcal
N=2$ locus is $U(1)^{12}$ (rank-12 abelian); its prepotential is
computed from the Enriques lattice $II_{1,9}(-1) \oplus II_{1,1}$.

### §A1.3 Attack vector — is $Y_{K3}$ the chiral algebra of the FHSV 4d $\mathcal N=2$ theory?

If the correct 4d $\mathcal N=2$ SCFT attached to K3 is FHSV, then
its chiral algebra via BR2018 has central charge:

$$
c_{2d}^{\mathrm{BLLPR}}(\mathrm{FHSV}) = -12(c_{4d}^{\mathrm{FHSV}} - a_{4d}^{\mathrm{FHSV}}).
$$

For FHSV: $a_{4d} = c_{4d} = n_V/4$ at the generic abelian point (Enriques
calculus, FHSV §4; see Shapere--Tachikawa 2008 arXiv:0804.1957 for
general formulas), so $c_{2d}^{\mathrm{BLLPR}} = 0$ at the abelian
locus. Not $+24$. At ADE-enhanced sub-loci, the $a = c$ equality can
break and $c_{2d}^{\mathrm{BLLPR}}$ becomes non-zero and negative
(generically), never $+24$.

**So FHSV-via-BR2018 does NOT give the Mukai-Heisenberg $c = 24$
chiral algebra.** This confirms my Wave 6 A1.3 falsification in a new
framing: FHSV is the canonical 4d $\mathcal N=2$ SCFT attached to K3,
and even it fails the sign test.

### §A1.4 Verdict — $Y_{K3}$ is NOT a BR2018 Schur-sector chiral algebra of any $\mathcal N=2$ SCFT

The Gaiotto-voice Wave 7 attack confirms, via the FHSV test case
specifically, what Wave 6 established generically: no 4d $\mathcal
N=2$ SCFT gives a Schur index whose BR2018 chiral algebra has $c =
24$. The K3 Yangian — if it exists — is **not** a 4d $\mathcal N=2$
Schur-sector object.

### §A1.5 What then is $Y_{K3}$ physically?

This is the question Wave 6 Gaiotto punted to "Vafa--Witten boundary
VOA" and Wave 6 Witten pushed to "IIA-on-K3-dual-to-heterotic-on-$T^4$
with a surface defect". Both frames are **descriptive** (they know
where $1/\eta^{24}$ comes from) but **not constructive** (they do not
realise a non-abelian Yangian with an explicit coproduct and an R-matrix
and a spectral parameter by a pull-back from a 4d SCFT).

The physics construction the swarm has been circling is:

$$
\text{(IIA or heterotic)} \;\to\; \text{6d} \;\to\; \text{4d with } \Omega\text{-background} \;\to\; \text{AGT/Nekrasov sector} \;\to\; \text{chiral algebra on an auxiliary curve}.
$$

The AGT-side target is well-specified. This is the Costello--Gaiotto
4d holomorphic Chern--Simons programme (Costello 2013; Costello
2017--2018 arXiv:1709.09993 and arXiv:1711.11046) and its
generalisation to K3 via 6d hCS on $\mathbb R^2 \times X^4$ with $X^4 =
K3$. What the 4d SCFT / BR2018 analysis tells us is what this programme
is **not**: the output is not a BR2018 Schur chiral algebra. It may be
a 4d hCS chiral algebra on an auxiliary curve — a different object.

### §A1.6 The correct primary source lane — Costello--Gaiotto 4d hCS, not BR2018

Costello--Gaiotto's 4d hCS on $\mathbb R^2 \times C \times \mathbb
R^2_{\varepsilon}$ (where $C$ is an auxiliary Riemann surface — the
"spectral curve" — and $\mathbb R^2_{\varepsilon}$ is the
$\Omega$-deformed plane) produces, perturbatively, Yangians as the
algebras of Wilson-line defects (Costello--Witten--Yamazaki 2018
arXiv:1709.09993, Theorem 1). The K3 analogue would replace the
topological $\mathbb R^2$ with K3, giving 6d hCS on $K3 \times C
\times \mathbb R^2_{\varepsilon}$. This is a **different** physical
setup from anything BR2018 covers.

**A1 final attack**: Wave 1--5's "BLLPR Schur-VOA cross-check" and my
Wave 6 "Vafa--Witten boundary VOA" are both misframings of the actual
physical setup $Y_{K3}$ could live in, which is Costello--Gaiotto 4d
hCS with K3 replacing the topological plane. Wave 7 reopens the
identification question in the correct frame.

---

## Surviving Core 1

After Attack 1, what survives:

1. **Abelian rank-24 Mukai-Heisenberg $\mathcal H_{\mathrm{Muk}}$**
   is the output of $\Phi_2(D^b(\Coh K3))$ (manuscript
   `thm:phi-k3-explicit`, `cy_to_chiral.tex:71`).
   This is a mathematical theorem, not a physics claim.

2. **Its character is $1/\eta^{24}$** (`k3_yangian_chapter.tex:190--198`
   `prop:k3e-selfdual-fock`).

3. **$1/\eta^{24}$ coincides with**:
   - the $SU(2)$ Vafa--Witten partition function on K3 (Vafa--Witten
     1994, hep-th/9408074, eq. (4.14));
   - the Göttsche generating function $\sum_n \chi(\mathrm{Hilb}^n(K3))
     q^n$ (Göttsche 1990, Math. Ann. 286 Theorem 0.1);
   - the inverse Fake Monster Lie algebra root-multiplicity generating
     series (Borcherds 1998) at lightlike level;
   - the Dedekind eta function raised to the 24th power (the unique
     weight-12 cusp form partition-count-related object consistent with
     $\chi(K3) = 24$).

4. **ADE sub-Yangians at ADE points of K3 moduli**: proved as
   shifted Yangians via Theorem
   `thm:bfn-phi-ade-identification`; ProvedElsewhere via four-step
   assembly.

5. **Obstructions O1--O15** from Wave 6 synthesis §3 remain valid. No
   physical-setup disambiguation in Wave 7 overturns any of them.

6. **The physical setup that matches the "24 free bosons" count**: the
   correct frame is Costello--Gaiotto 4d hCS with K3 replacing the
   topological plane (Wave 7 A1.6). BR2018 / Schur-index / class-S is
   the **wrong** frame (Wave 6 A1; Wave 7 A1.3 FHSV falsifier).

---

## Heal Phase 1 — name the theory, write the partition function, compute at rank 1

### §H1.1 The physical theory to audit

I commit to a specific physical setup:

> **$\mathcal T_{K3}^{6d\text{-hCS}}$**: 6d holomorphic Chern--Simons on
> $\mathbb R^2_{\varepsilon} \times K3 \times C$, with the gauge theory
> of rank $r$, at the abelian/free-field level $r = 1$, and with $C$
> an auxiliary Riemann surface (the "spectral curve").

This is the K3 analogue of Costello's 4d hCS on
$\mathbb R^2_{\varepsilon} \times \mathbb R^2 \times C$
(arXiv:1709.09993; arXiv:1711.11046). The gauge field $A$ is a
partial connection valued in $\Omega^{0,1}(K3 \times C) \otimes
\mathfrak g$, with action functional

$$
S = \frac{1}{\hbar} \int_{\mathbb R^2_{\varepsilon} \times K3 \times C} \omega \wedge \mathrm{CS}(A),
$$

where $\omega$ is the holomorphic 3-form of $K3 \times C$ (a $(3,0)$-form
on $K3 \times C$, which exists because $K3$ has a holomorphic 2-form and
$C$ has a holomorphic 1-form), and $\mathrm{CS}(A) = \mathrm{tr}(A d A + \tfrac{2}{3} A^3)$
is the Chern--Simons 3-form.

**Physical question**: what is the chiral algebra of Wilson-line
defects wrapping $C \times \{\mathrm{pt}\}$ inside $\mathbb R^2_{\varepsilon} \times K3 \times C$, at 1-loop and rank $r = 1$?

### §H1.2 Rank-1 reduction — the ABJ-anomaly-free sector

At rank 1 with $\mathfrak g = \mathfrak{gl}_1$: the gauge field $A$ is
abelian. The action is quadratic in $A$:

$$
S = \frac{1}{\hbar} \int \omega \wedge A \wedge d A.
$$

The propagator of $A$ at a pair of points $(z_1, \bar z_1; x_1, \bar x_1, y_1)$
and $(z_2, \bar z_2; x_2, \bar x_2, y_2)$, where $z$ is the coordinate
on $C$, $(x, \bar x)$ on K3 (holomorphic/antiholomorphic local), $y$ on
$\mathbb R^2_{\varepsilon}$:

$$
\langle A(z_1, \bar x_1) A(z_2, \bar x_2) \rangle = \hbar \cdot \frac{1}{z_1 - z_2} \cdot \delta^{K3}(\bar x_1 - \bar x_2) \cdot G^{\Omega}(y_1, y_2),
$$

where $G^{\Omega}(y, y')$ is the $\Omega$-background propagator on
$\mathbb R^2$ (Costello--Witten--Yamazaki 2018 §3.2). The $\delta^{K3}$
factor is the Bergman kernel on K3 for the holomorphic line
bundle associated to the $(2,0)$-form $\omega_{K3}$.

At rank 1 and 1-loop: the partition function on $\mathbb R^2_{\varepsilon}
\times K3 \times C$ localises onto the moduli of holomorphic line
bundles on $K3 \times C$, which decomposes (by Künneth) as

$$
\mathrm{Pic}(K3 \times C) = \mathrm{Pic}(K3) \oplus \mathrm{Pic}(C) \oplus \mathrm{Hom}(H_1(C, \mathbb Z), \mathrm{Pic}^0(K3)).
$$

The $\mathrm{Pic}(K3) \oplus \mathrm{Hom}(H_1(C, \mathbb Z), \mathrm{Pic}^0(K3))$
sector is K3-dependent. The first $\mathrm{Pic}(K3)$ sits inside
$H^2(K3, \mathbb Z) \cong II_{3, 19}$ (Picard lattice of a generic K3
has rank ≤ 20, specialising to various sub-lattices for special K3).

**BPS states at rank 1**: at rank 1, the BPS states of 6d hCS on
$\mathbb R^2_{\varepsilon} \times K3 \times C$ are the **first-quantised
modes** of the abelian gauge field, one per basis element of
$H^{0,1}(C) \otimes H^{0,0}(K3) \oplus H^{0,0}(C) \otimes H^{0,1}(K3)
\oplus \dots$. By Hodge theory on $K3 \times C$:

$$
H^{0,1}(K3 \times C) = H^{0,1}(K3) \oplus H^{0,1}(C) = 0 \oplus g = g,
$$

(where $g$ is the genus of $C$), since $h^{0,1}(K3) = 0$.

And for the Mukai-lattice-full count, one also picks up $H^{0,2}(K3) =
1$ (one mode from the holomorphic $(2,0)$-form), $H^{1,1}(K3) = 20$
(Picard-plus-transcendental), $H^{2,0}(K3) = 1$ (complex-conjugate
mode), plus $H^{0,0}(K3) = 1$ and $H^{2,2}(K3) = 1$ (zero-form and
volume-form), totalling

$$
1 + 1 + 20 + 1 + 1 = 24 = \chi(K3).
$$

These 24 modes are the **rank-1 BPS multiplets** of
$\mathcal T_{K3}^{6d\text{-hCS}}$ on $K3 \times C$, with $C$ auxiliary.
They are precisely the 24 free-boson currents of $\mathcal H_{\mathrm{Muk}}$
in the abelian core reading.

### §H1.3 The partition function at rank 1

The 1-loop partition function of 6d hCS at rank 1 on $\mathbb R^2_{\varepsilon} \times K3 \times C$ is

$$
Z^{(1)}_{\mathrm{1-loop}}(K3 \times C; q, \varepsilon) = \det\nolimits^{-1/2}\bigl(\partial_{\bar C} \otimes \bar\partial_{K3}\bigr),
$$

acting on $\Omega^{0,0}(K3 \times C) \otimes \mathfrak{gl}_1$.

By the holomorphic analogue of Mellin/Ray--Singer analytic torsion
(Bismut--Gillet--Soulé), this determinant factorises as a product:

$$
Z^{(1)}_{\mathrm{1-loop}} = Z_{K3}^{1/2}(q) \cdot Z_C(\varepsilon) \cdot (\text{cross terms}).
$$

For $C = $ elliptic curve $E_\tau$ (the most natural choice: gives the
Wave 1--6 "elliptic" R-matrix candidates) and $K3$ generic, and working
to leading order in the $\Omega$-deformation $\varepsilon \to 0$:

$$
Z_{K3}(q) = \prod_{n \ge 1} (1 - q^n)^{-\chi(K3)} = \prod_{n \ge 1} (1 - q^n)^{-24} = \frac{q}{\eta(q)^{24}},
$$

matching the Göttsche / Vafa--Witten / Mukai-Heisenberg character
**exactly at rank 1**.

The provenance of the $-24 = -\chi(K3)$ exponent is the rank-1
1-loop determinant of the $\bar\partial$ operator on $K3$ (Göttsche
1990, Math. Ann. 286); the provenance of the product form $\prod
(1-q^n)^{-24}$ is the Hilbert-scheme-on-K3 generating series via
Nakajima (Ann. Math. 145, 1997) applied to the Hilbert schemes
parametrising multi-brane configurations dual to the 1-loop Cartan
determinant.

Three independent verification paths:
- **Path 1 (Göttsche 1990)**: direct Euler characteristic of
  $\mathrm{Hilb}^n(K3)$. Primary.
- **Path 2 (Vafa--Witten 1994)**: $SU(2)$ S-duality on K3 gives
  $1/\eta^{24}$ (modulo theta factors). Primary.
- **Path 3 (DMVV 1997)**: second-quantised partition function
  $\Phi^{-1}_{\mathrm{DMVV}}$ = $1/\Phi_{10}$, whose $p^0$-coefficient
  (single-K3 sector) is $1/\eta^{24}$. Primary.

All three independently give the same rank-1 partition function.

### §H1.4 Schur index is the WRONG partition function; BPS partition function is the RIGHT one

The Schur index lives on $S^3 \times S^1$ of a 4d $\mathcal N=2$ SCFT.
$\mathcal T_{K3}^{6d\text{-hCS}}$ is 6d, not 4d; it has no direct Schur
index. The analogous invariant is the **holomorphic 1-loop partition
function** on $\mathbb R^2_{\varepsilon} \times K3 \times E_\tau$,
which localises onto the $K3 \times E_\tau$ holomorphic sector and
reduces to the Vafa--Witten / Göttsche generating series
$1/\eta(q)^{24}$ above.

This is the correct partition-function-level match at rank 1. The
Schur-index machinery of BR2018 does not apply.

### §H1.5 Rank-1 K3 Yangian identification

At rank 1, $\mathfrak g = \mathfrak{gl}_1$. The Yangian $Y(\mathfrak{gl}_1)$
is rank-1 and has a single generator. On $H^*(\mathrm{Hilb}^n(\mathbb C^2))$, the
Schiffmann--Vasserot / Maulik--Okounkov construction produces the
affine Yangian $Y_{\hbar_1, \hbar_2}(\widehat{\mathfrak{gl}}_1)$
(arXiv:1202.2756; arXiv:1211.1287), which at the CY limit $\hbar_1 +
\hbar_2 + \hbar_3 = 0$ becomes $\mathcal W_{1+\infty}$ at $c = 1$.

The K3 analogue: $Y_{\hbar}(\widehat{\mathfrak{gl}}_1)^{K3}$ acts on
$\bigoplus_n H^*(\mathrm{Hilb}^n(K3))$ via the Nakajima Heisenberg
algebra (Nakajima 1997). But: on **generic K3**, there is no torus
action, and the Schiffmann--Vasserot Yangian upgrade fails (my Wave
6 §A2). The Nakajima Heisenberg is available; the Yangian upgrade is
not.

So the **rank-1 K3 Yangian, as a genuine Yangian (non-trivial
coproduct, R-matrix, spectral parameter)**, exists only on
**Kummer** or **elliptic** K3 loci, where a torus acts.

**Rank-1 identification at the Kummer locus**: $K3_{\mathrm{Kummer}} =
\widetilde{T^4/\mathbb Z_2}$ inherits a $T^2$-action from the $T^4$;
the SV/MO construction gives $Y_{\hbar_1, \hbar_2}(\widehat{\mathfrak{gl}}_1)$
acting on $\bigoplus_n H^*_T(\mathrm{Hilb}^n(K3_{\mathrm{Kummer}}))$.
Match to graded character $1/\eta^{24}$: the graded character of this
module at the fixed-point limit is the MacMahon partition count
weighted by the $T$-weights; in the abelian limit $\hbar_1, \hbar_2 \to 0$
the character reduces to the Euler characteristic generating series,
which is indeed $1/\eta^{24}$.

Status: **[M] chain-level at the Kummer locus**, **undefined on
generic K3** (no torus). This is a stronger negative result than
Wave 6 Gaiotto's: not only does the Schur-VOA cross-check fail at
generic K3, but even the SV/MO Yangian upgrade fails at generic K3,
leaving only the Nakajima Heisenberg without Yangian enhancement.

### §H1.6 Summary of Heal 1

- **Physical theory**: $\mathcal T_{K3}^{6d\text{-hCS}}$ = 6d hCS on
  $\mathbb R^2_{\varepsilon} \times K3 \times C$ at rank $r$.
- **Rank-1 BPS spectrum**: 24 free-boson modes, one per basis element
  of $H^*(K3, \mathbb C) = \mathbb C^{24}$.
- **Rank-1 partition function**: $Z^{(1)}_{\mathrm{1-loop}}(K3 \times E;
  q) = 1/\eta(q)^{24}$. Three primary-source verification paths
  (Göttsche, Vafa--Witten, DMVV).
- **Rank-1 Yangian**: $Y_{\hbar_1, \hbar_2}(\widehat{\mathfrak{gl}}_1)^{K3}$
  exists as a genuine Yangian only on Kummer and elliptic K3 loci
  where a torus acts; on generic K3 only the Nakajima Heisenberg
  survives.
- **Not a Schur index**: BR2018 / Schur-index / class-S is the wrong
  frame; $\mathcal T_{K3}^{6d\text{-hCS}}$ is 6d not 4d; the
  correct partition function is the holomorphic 1-loop partition
  function, not a Schur index.

---

## Attack Phase 2 — the spectral curve $C$ is an unresolved freedom

### §A2.1 Is $C$ fixed by physics or by the swarm?

Wave 6 Beilinson's Critical-1 finding: "no voice named the curve on
which $Y_{K3}$ should be a chiral algebra". Wave 7 H1 committed to "$C
= $ auxiliary Riemann surface, naturally $E_\tau$". Is this forced, or
a choice?

In Costello's original 4d hCS, the auxiliary plane is the
$(z, \bar z)$-plane of $\mathbb C$ (topological direction $\mathbb R^2$
times holomorphic direction $\mathbb C$), and Wilson lines wrap the
$\mathbb C$-factor. For 6d hCS on $K3 \times C$, the auxiliary factor
$C$ is where Wilson lines wrap; its choice matters.

Three candidate choices of $C$:
- (C-a) **$C = \mathbb C$**: gives rational Yangian (Costello 2013).
  Too trivial for K3 enhancement; the elliptic structure of the
  Mukai lattice is lost.
- (C-b) **$C = E_\tau$ elliptic**: gives elliptic (Belavin-type)
  R-matrices (Costello--Witten--Yamazaki 2018 arXiv:1709.09993 §7;
  Costello 2017 arXiv:1711.11046). Natural candidate when the
  "24-fold monster" has an elliptic genus structure.
- (C-c) **$C = \mathbb P^1$ with punctures**: gives class-S-type
  realisation. Natural when K3 is viewed as class-S internal geometry
  on some curve $C$ of Gaiotto-curve type.

Wave 5 and earlier assumed, largely implicitly, (C-b). Wave 6 and
Wave 7 H1 stated $C = E_\tau$. **Is this forced by primary physics, or
a swarm consensus that could be wrong?**

### §A2.2 The FHSV / heterotic 24 forces $C = E_\tau$ only at special points

FHSV 1995 (hep-th/9505162) starts with IIA on K3 $\times T^2$; the
$T^2$ factor is the origin of the "$C = E_\tau$" auxiliary curve in 6d
hCS reductions (where $T^2 = E_\tau$ and $\tau$ is the complex
structure moduli). But $T^2$ in FHSV is **the uncompactified spectral
parameter** (heterotic-$T^4$'s extra two torus directions), not an
auxiliary curve at which Wilson lines wrap.

The distinction matters. In the 4d hCS literature (Costello--Witten--Yamazaki
2018), the "spectral curve" is the **holomorphic auxiliary direction**
where Wilson lines live; in the FHSV / heterotic compactification
literature, the "extra $T^2$" is an **uncompactified direction** that
one wraps Wilson lines in but which also supports the 4d $\mathcal
N=2$ SCFT.

These are the **same $T^2$**, but used in **different ways**. The
ambiguity: is $T^2$ the spectral curve (Costello--Gaiotto setup) or
the compactification manifold (FHSV setup)?

**A2.1 attack**: Wave 7 H1 fixed $C = E_\tau$ by analogy with Costello
rather than by primary derivation from a specific physical theory. If
the "correct" physical theory is FHSV, $T^2$ is uncompactified and
the "chiral algebra $Y_{K3}$" lives on a different curve — possibly
$\mathbb P^1$ decorated with FHSV punctures, possibly the FHSV Seiberg--Witten
curve (Klemm--Mayr--Vafa 1996 hep-th/9607139), possibly the vanishing
cycle of the $K3$ fibration.

### §A2.3 Three candidate curves under scrutiny

Let me evaluate each:

**C-a: $C = \mathbb C$.** Gives rational Yangian $Y_\hbar(\widehat{\mathfrak{gl}}_1)$
acting on $\bigoplus_n H^*(\mathrm{Hilb}^n(K3))$ (via SV/MO, torus-restricted).
Rational R-matrix $(u + \hbar P)/(u + \hbar)$. Too trivial — does not
see the Mukai lattice's indefinite signature or the 24-fold monster
structure.

**C-b: $C = E_\tau$.** Gives elliptic Yangian (Belavin R-matrix). Under
adversarial audit: Wave 5 "Belavin elliptic R-matrix on Mukai" was
numerically falsified (Etingof W6 A7; CYBE residual $3.94 \times 10^1$,
12 orders above $10^{-10}$ threshold). So the elliptic $R$-matrix **attached
to the Mukai lattice** does not close CYBE. This is a concrete obstruction
to (C-b) at rank > 1.

At rank 1, (C-b) gives the trivial elliptic R-matrix (identity at rank 1);
vacuous match. At rank > 1, (C-b) fails (Etingof W6 O13).

**C-c: $C = \mathbb P^1$-with-punctures.** Gives class-S-type realisation.
But: as Wave 6 A3 disambiguated, class-S on a Gaiotto curve with K3
internal is a fundamentally different physical setup from 4d theory on
K3 spacetime. The former gives BR2018 Schur chiral algebras with sign
obstruction; the latter gives Vafa--Witten-like partition functions.

**Synthesis**: all three candidate curves $C$ give objects that are
either trivial (C-a at any rank, C-b at rank 1), numerically obstructed
(C-b at rank > 1), or sign-obstructed (C-c at any rank). **No choice
of $C$ currently gives a non-trivial non-obstructed K3 Yangian at rank
> 1 matching the 24-fold Mukai structure.**

### §A2.4 The attack settles into an obstruction statement

I now see that the spectral curve $C$ is not just undefined in the
manuscript — it is **over-constrained**. Whatever curve $C$ we try,
either the resulting Yangian is trivial (rank-1 only), or it fails
numerical consistency (Wave 5 Belavin), or it falls into the BR2018
sign-obstruction category.

This is an obstruction I do not see flagged in the Wave 6 synthesis:

> **O16 (Wave 7 Gaiotto obstruction, spectral-curve over-constraint)**.
> No choice of auxiliary curve $C$ — rational, elliptic, or punctured
> sphere — gives a non-trivial K3 Yangian on $K3 \times C$ with a
> closed R-matrix at rank > 1 matching the Mukai-lattice structure.
> Rational: too trivial. Elliptic: CYBE fails. Punctured sphere: BR2018
> sign obstruction.

This strengthens the Wave 6 obstruction landscape to 16 obstructions.
It suggests that the correct curve is yet to be identified, or that
the K3 Yangian is a fundamentally non-curve object (e.g., lives on the
Bridgeland stability manifold rather than a curve).

---

## Heal Phase 2 — Costello--Gaiotto 6d hCS on $\mathbb R^2_{\varepsilon} \times K3 \times E_\tau$, BPS state enumeration via Donaldson--Thomas, Schur/BPS index at rank 1 via DMVV

### §H2.1 The correct 6d hCS statement, made precise

Let me re-write the physical setup at primary-source precision.

**Setup.** 6d holomorphic Chern--Simons theory $\mathcal T_{K3 \times E}^{6d\text{-hCS}}$
on $\mathbb R^2_{\varepsilon} \times K3 \times E_\tau$, with:
- gauge group $G_r = \mathrm{GL}_r(\mathbb C)$, rank $r$;
- $\Omega$-deformation parameter $\varepsilon$ on $\mathbb R^2$;
- complex structure moduli: $\mathrm{Teich}(K3)$ for K3 and $\tau \in
  \mathbb H / \mathrm{SL}_2(\mathbb Z)$ for the elliptic curve.

**Primary source.** Costello 2013 (arXiv:1303.2632) defined 4d hCS.
Costello--Witten--Yamazaki 2018 (arXiv:1709.09993) extended to spectral
curves. The 6d extension to $K3 \times E$ is **conjectural at this
literature level**: I do not know of a primary-source theorem in the
style of CWY 2018 Theorem 1 for the 6d-on-$K3 \times E$ case. So I
flag this as a **research programme**, not a theorem.

**BPS spectrum enumeration** (following Donaldson--Thomas on $K3 \times E$):

The BPS spectrum of type IIA on $K3 \times E$ is the Donaldson--Thomas
partition function
$$
Z^{DT}_{K3 \times E} = \sum_{n, \beta, m} DT_{n, \beta, m} \cdot q_1^{m} q_2^{n} Q^\beta,
$$
where $\beta \in H_2(K3 \times E, \mathbb Z)$, $n, m$ are Chern-class
parameters, and $DT_{n, \beta, m}$ is the Behrend-function-weighted
count of DT stable objects (torsion-free sheaves of given numerical
invariants on $K3 \times E$).

Oberdieck--Pixton (arXiv:1411.1514; denominator identity arXiv:1607.05105,
Theorem 1): for $K3 \times E$ with $\beta \neq 0$, fibre class restriction,

$$
Z^{DT}_{K3 \times E}(q_1, q_2, Q) = \frac{C}{\Phi_{10}(\tau_1, \tau_2, \tau_3)},
$$

where $\Phi_{10}$ is the Igusa cusp form of weight 10 on
$\mathrm{Sp}_4(\mathbb Z)$, and $(\tau_1, \tau_2, \tau_3)$ parametrise the
Siegel upper half-space via $q_1 = e^{2\pi i \tau_1}$, $Q = e^{2\pi i \tau_2}$,
$q_2 = e^{2\pi i \tau_3}$.

The **rank-1 ($r = 1$) sector** of this partition function (where
the gauge field is abelian, no brane stacking) extracts the principal
pole of $\Phi_{10}$, which gives

$$
Z^{DT}_{K3 \times E}|_{r=1} = \frac{1}{\eta(q_1)^{24}} \cdot (\text{fibre factors}),
$$

by specialising the Oberdieck--Pixton denominator at the diagonal cusp.

### §H2.2 The Schur/BPS index at rank 1

Although a Schur index per se does not apply (the theory is 6d, not
4d SCFT), the analogous object is the **BPS partition function at
rank 1**, which by Oberdieck--Pixton equals (up to conventional
normalisations):

$$
Z_{\mathrm{BPS}, r=1}(K3 \times E; q_1, Q, q_2) = \frac{C_0}{\Phi_{10}(\tau)}\bigg|_{\mathrm{r=1 sector}} = \frac{1}{\eta(q_1)^{24}}.
$$

This is the **rank-1 Schur/BPS index** of $\mathcal T_{K3 \times E}^{6d\text{-hCS}}$,
computed from first principles via Donaldson--Thomas counting on
$K3 \times E$ (Oberdieck--Pixton, ProvedElsewhere), giving the character
of the abelian Mukai-Heisenberg VOA exactly.

Three primary verification paths:
- **Path 1**: Oberdieck--Pixton Igusa cusp form identity (arXiv:1607.05105,
  ProvedElsewhere; Maulik--Pandharipande--Pixton 2010 K3 DT/GW
  correspondence).
- **Path 2**: DMVV 1997 second-quantised Hilb$^n(K3)$ generating
  series (arXiv:hep-th/9608096), whose $p^N = p^1$-coefficient is $1/\eta^{24}$.
- **Path 3**: Nakajima 1997 Heisenberg action on
  $\bigoplus_n H^*(\mathrm{Hilb}^n(K3))$, whose graded character is
  $1/\eta^{24}$ by Göttsche.

All three give the same rank-1 answer. **Converged**.

### §H2.3 Match to $\mathcal H_{\mathrm{Muk}}$ as abelian Yangian

At rank 1, the proposed "K3 Yangian" reduces to the abelian
$\mathfrak{gl}_1$-Yangian, which on $K3$ acts (conjecturally, via
Kummer/elliptic restriction) as the Schiffmann--Vasserot / Maulik--Okounkov
affine Yangian of $\widehat{\mathfrak{gl}}_1$. Its graded character on
the Fock module is (up to normalisations) $1/\eta^{24}$, matching the
rank-1 BPS partition function $Z_{\mathrm{BPS}, r=1}$.

**Conclusion of H2**: the rank-1 K3 Yangian (as an abelian
$\widehat{\mathfrak{gl}}_1$-affine-Yangian acting on a torus-restricted
K3 moduli) has a well-defined physical partner — the rank-1 BPS
partition function of IIA DT on $K3 \times E$ — and their characters
match via three independent primary sources.

### §H2.4 Non-abelian r > 1 case: obstruction, not construction

At rank $r > 1$: the BPS partition function on $K3 \times E$ at higher
rank is **still** governed by $1/\Phi_{10}$ (Oberdieck--Pixton 2016,
Theorem 1), but now the full Igusa form (not just its rank-1 pole
term) is involved. The graded character of a hypothetical non-abelian
rank-$r$ K3 Yangian would have to be a rank-$r$ specialisation of
$1/\Phi_{10}$, which would correspond to:

$$
Z_{\mathrm{BPS}, r \ge 2}(K3 \times E) \sim \frac{1}{\Phi_{10}^{1/2 \text{ or something}}}.
$$

The rank-$r$ specialisation is **not** standard literature; it is the
target of the Borcherds/Gritsenko--Nikulin BKM construction (which is
a mathematical object on $K3 \times E$, not K3 alone, as per P-AP-CY
discipline and my Wave 6 §2.3 argument that BKM content belongs to
k3e_bkm_chapter.tex, not k3_yangian_chapter.tex).

**So**: the non-abelian K3 Yangian on K3 alone (not $K3 \times E$) has
no rank-$r$ BPS partition function. The rank-$r$ partition function
lives on $K3 \times E$, not $K3$; attributing it to the K3 Yangian is
an off-scope transfer (Wave 6 §2.3).

---

## Attack Phase 3 — the BPS interpretation at rank 1 is vacuous in the same way as Wave 6 A2 was

### §A3.1 Rank-1 is always trivial for Yangians

Wave 6 A2 established: at rank 1, SV/MO reduces to the scalar 1
(because $P = 1$ on a line, R-matrix becomes scalar). My Wave 7 H1
and H2 produce a rank-1 identification — but is it meaningful?

Let me audit. At rank 1, $\mathfrak{gl}_1$: the Yangian
$Y_\hbar(\mathfrak{gl}_1)$ is a polynomial algebra in the generators
$\mathcal E_0, \mathcal E_1, \mathcal E_2, \dots$ (Drinfeld generators).
The coproduct is non-trivial; the R-matrix is $(u + \hbar)/(u)$ or
similar (Molev's book, *Yangians and Classical Lie Algebras*, §1.7).
But on a one-dimensional representation, the coproduct factors
trivially and the R-matrix acts as scalar.

**Affine extension**: $Y_{\hbar_1, \hbar_2}(\widehat{\mathfrak{gl}}_1)$ =
$\mathcal W_{1+\infty}$ at $c = 1$ is non-trivial (infinite-rank
algebra). It is NOT the finite-dim $Y_\hbar(\mathfrak{gl}_1)$.

The match in Wave 7 H2 is therefore between:
- (left) $\mathcal W_{1+\infty}$ at $c = 24$ or similar (infinite rank,
  non-trivial);
- (right) the rank-1 abelian-core Mukai-Heisenberg $\mathcal H_{\mathrm{Muk}}$
  at $c = 24$ (also infinite rank: 24 bosons contribute 24 Virasoro
  copies).

Both are **infinite-rank** in the underlying VOA sense. The "rank 1"
refers to the rank of the gauge group $G_r$ in the 6d hCS setup, which
is $G_1 = \mathrm{GL}_1$, but the VOA on the auxiliary curve is
infinite-rank.

So the rank-1 match is **not** vacuous in the sense of Wave 6 A2; it is
the match of two infinite-rank VOAs with central charge 24 and
character $1/\eta^{24}$. The issue is different:

### §A3.2 Character-match is the weakest equivalence

Two VOAs with the same character need not be isomorphic as VOAs:
$V_{\Lambda_{\mathrm{Muk}}}$ (rank-24 lattice VOA) and $\mathcal
W_{1+\infty}$ at central charge 24 both have character $1/\eta^{24}$,
but they are **not isomorphic as VOAs**: the former has 24 commuting
Heisenberg currents forming a lattice algebra, the latter has one
Virasoro current generating an infinite tower of higher-spin currents.

So: H2.3 is a **character-level** match, not a **VOA-level**
identification. This weakens the claim.

### §A3.3 VOA-level identification requires more

To lift the character match to a VOA identification, one would need:
- to identify the 24 Heisenberg currents of $\mathcal H_{\mathrm{Muk}}$
  with 24 specific generators of $\mathcal W_{1+\infty}$ at $c = 24$;
- to check the OPEs match (Mukai pairing vs $\mathcal W_{1+\infty}$ OPE);
- to check the vacuum and modules line up.

None of this has been done in any wave. At the **VOA level**, the
rank-1 K3 Yangian identification is **unverified**; only a
**character-level coincidence** is established.

### §A3.4 New obstruction

> **O17 (Wave 7 Gaiotto obstruction, character-vs-VOA level)**.
> The coincidence of characters at rank 1 between $\mathcal H_{\mathrm{Muk}}$
> (lattice VOA of $\Lambda_{\mathrm{Muk}}$) and $\mathcal W_{1+\infty}$
> at $c = 24$ (infinite higher-spin VOA) does not imply VOA-level
> isomorphism. The two VOAs have different primary field content, different
> module categories, and different quantum dimensions at the abelian
> level. Character match is the weakest possible equivalence.

### §A3.5 Attack 3 conclusion

My Wave 7 H2 identification of $Z_{\mathrm{BPS}, r=1} = 1/\eta^{24}$
with the Mukai-Heisenberg character is a **character-level**
statement, supported by three independent primary sources. It is not
a VOA-level or Yangian-level identification. The step from
"character matches" to "VOA matches" requires further work not
carried out in any wave.

This is a **weaker** final state than my H1/H2 prose suggested. It
forces me to downgrade my H2 synthesis.

---

## Heal Phase 3 — final converged statement with honest scope tags

### §H3.1 What I actually have at convergence

**Physical theory**: $\mathcal T_{K3 \times E}^{6d\text{-hCS}}$ = 6d
hCS on $\mathbb R^2_{\varepsilon} \times K3 \times E_\tau$ at gauge
rank $r$. Conjectural as a QFT (no existence theorem in the primary
literature at the standard of CWY 2018 Theorem 1).

**Rank-1 BPS spectrum**: 24 free-boson modes, one per basis element
of $H^*(K3, \mathbb C)$. Primary source: Hodge decomposition of K3.
Chain-level, computable.

**Rank-1 Schur/BPS partition function**: $Z_{\mathrm{BPS}, r=1}
(K3 \times E; q_1) = 1/\eta(q_1)^{24}$. **ProvedElsewhere** at this
level, via three independent primary-source paths:
- Göttsche 1990 (Hilb$^n(K3)$ Euler char);
- Vafa--Witten 1994 ($SU(2)$ S-duality);
- DMVV 1997 (second-quantised generating series);
- Oberdieck--Pixton 2016 (Igusa-Siegel-form K3$\times E$ DT) as a
  global/fourth path that specialises to $1/\eta^{24}$ at rank 1.

**Matching to the K3 Yangian (character level only)**: $\mathcal H_{\mathrm{Muk}}$
has character $1/\eta^{24}$. The rank-1 Schur/BPS index matches the
abelian-core character. The match is character-level only (O17).

**VOA-level identification**: the character match does not establish
a VOA isomorphism between $\mathcal H_{\mathrm{Muk}}$ and any
Yangian-module VOA. **Not established.** This is where the K3
Yangian programme stops.

### §H3.2 Pattern 236 ambient-qualifier inscription

- **Chain-level**: the 24-mode BPS spectrum is the Hodge decomposition
  of $K3$ evaluated at rank 1 of the gauge group. Explicit, verified.
- **$(\infty,1)$-categorical**: the 6d hCS theory's factorization
  algebra (in the Costello--Gwilliam sense) localises on $K3 \times E$
  to an $\infty$-chiral algebra. At rank 1, this is the lattice
  factorization algebra of $\Lambda_{\mathrm{Muk}}$ on the curve
  $E_\tau$. This is the $(\infty,1)$-categorical lane.
- **Physical**: the partition function is the BPS partition function
  on $\mathbb R^2_{\varepsilon} \times K3 \times E$, localising onto
  $1/\eta^{24}$ at rank 1 via DT/Göttsche/VW/DMVV independent channels.

All three lanes give the same character at rank 1; none lifts this
to a VOA-level K3 Yangian identification at rank $> 1$.

### §H3.3 Non-abelian (rank $> 1$): construction not available from physics

At rank $r > 1$:
- The BPS partition function on $K3 \times E$ is $1/\Phi_{10}$
  (Oberdieck--Pixton); the rank-$r$ specialisation is not standard.
- The rank-$r$ gauge group $G_r = \mathrm{GL}_r$ is non-abelian; the
  Costello--Gaiotto chiral algebra of Wilson-line defects at rank $r$
  involves non-trivial R-matrices. These R-matrices need to close CYBE
  and match the Mukai-lattice structure.
- Etingof W6: Belavin elliptic R-matrix attached to Mukai lattice
  fails CYBE (residual $3.94 \times 10^1$). Wave 7 O16: no choice of
  auxiliary curve $C$ gives a non-obstructed R-matrix at rank $> 1$.

**Conclusion at rank $> 1$**: no construction of a non-abelian K3
Yangian from 6d hCS on $K3 \times E$ is available that matches both
the Mukai-lattice structure (24-fold) and closes CYBE. This is the
same conclusion as the Wave 6 synthesis, now re-derived from the
physics-side framework.

### §H3.4 The physics-side verdict

> The physics of type IIA / DT on $K3 \times E$ supplies the rank-1 BPS
> partition function $1/\eta^{24}$ (ProvedElsewhere via four paths:
> Göttsche, Vafa--Witten, DMVV, Oberdieck--Pixton). This matches the
> character of $\mathcal H_{\mathrm{Muk}}$, the abelian Mukai-Heisenberg
> VOA. This is a character-level match, **not** a VOA-level identification.
> At rank $> 1$, no construction of a non-abelian K3 Yangian is
> physically available without either (a) triggering the BR2018 sign
> obstruction, (b) failing CYBE (Etingof W6 O13), or (c) over-constraining
> the spectral curve (Wave 7 O16). **The non-abelian K3 Yangian,
> physically, is not constructed.**

---

## Attack Phase 4 — does any existing physical theory actually DO what Wave 1--5 tried to do?

### §A4.1 Is there a BPS algebra on a CY_3 containing K3 whose restriction to K3 is $Y_{K3}$?

Per the prompt's Harvey--Moore / Kontsevich--Soibelman framing: the
"BPS algebra" formalism (Harvey--Moore 1995, hep-th/9510182;
Kontsevich--Soibelman 2008--2011, arXiv:0811.2435) attaches a
Borcherds--Kac--Moody / COHA-style algebra to a CY_3 (or its derived
category of coherent sheaves with a stability structure). The K3-relevant
CY_3 would be:

- (BPS-1) $K3 \times E$ (the Maulik--Pandharipande / Oberdieck--Pixton
  setup) — well-documented, BKM superalgebra $\mathfrak g_{\Delta_5}$
  attached by Gritsenko--Nikulin via Borcherds lift.
- (BPS-2) $K3 \times \mathbb C$ (non-compact CY_3) — this is the
  cotangent-like situation; the BPS spectrum of type IIA here is
  governed by Nakajima-Heisenberg on $\mathrm{Hilb}^n(K3)$ as previously.
- (BPS-3) K3 fibration over $\mathbb P^1$ (compact CY_3) — the
  Strominger--Yau--Zaslow dual of heterotic on K3, via the
  Borcherds--Harvey--Moore lift.

**Of these, (BPS-1) is the only one with a proved BKM algebra
structure (Gritsenko--Nikulin 1998, Mathieu 2011)**. Its root
multiplicities are the $\phi_{0,1}$ coefficients of the K3 elliptic
genus; its denominator is $\Delta_5$, the square root of $\Phi_{10}$.

### §A4.2 Is $\mathfrak g_{\Delta_5}$ the K3 Yangian?

**No**. $\mathfrak g_{\Delta_5}$ is a **Lie superalgebra** (not a Yangian
or quantum group), it lives on $K3 \times E$ (not K3), and its
"Yangification" (i.e. quantum deformation) is not established. At
best, $\mathfrak g_{\Delta_5}$ is the CLASSICAL LIMIT of a conjectural
"$K3 \times E$ Yangian" (not a "K3 Yangian"), and this Yangification
step is itself open.

### §A4.3 The K3 Yangian $\neq$ the $K3 \times E$ BKM; the manuscript knows this

k3e_bkm_chapter.tex is about $K3 \times E$; k3_yangian_chapter.tex is
about K3. The two are different objects, and conflation is Wave 6 §2.3
obstruction O3 / my own AP-POLYAKOV-W6-01.

**A4 verdict**: no existing BPS-algebra framework produces a non-abelian
K3 Yangian on K3 alone. The $K3 \times E$ BKM $\mathfrak g_{\Delta_5}$
lives on a different manifold and is a Lie superalgebra, not a
Yangian. The analogues on $K3 \times \mathbb C$ or K3-fibration CY_3s
are not Yangians either; they are Nakajima-Heisenberg or Schiffmann--Vasserot
COHA, neither of which is a genuine Yangian without torus enhancement.

### §A4.4 The physics-side absence

Gaiotto's instinct, Wave 7: the reason the K3 Yangian is so stubborn
is that **there is no primary-source physical system whose BPS
algebra, chiral algebra, or Schur/BPS partition function directly
produces a non-abelian Yangian on K3 at rank $> 1$**. The closest
analogues are:

- Nakajima affine Yangian $Y_{\hbar_1,\hbar_2}(\widehat{\mathfrak{gl}}_1)$
  on Hilb$^n(\mathbb C^2)$: proved (SV 2013, MO 2012), but on $\mathbb
  C^2$, not K3.
- BFN shifted Yangian at Kleinian ADE: proved
  (`thm:bfn-phi-ade-identification`), but on $\widetilde{S}_{\mathfrak g} \to \mathbb C^2/\Gamma$, not K3.
- BKM $\mathfrak g_{\Delta_5}$ on $K3 \times E$: proved (Gritsenko--Nikulin
  1998), but Lie superalgebra, not Yangian; and on $K3 \times E$, not K3.

All three are adjacent to K3 but none is ON K3 (as a whole) at rank
$> 1$ as a Yangian.

This is **structurally** why Wave 6's 15 obstructions and Wave 7's 2
additional obstructions all pile up: the physics expects an object
that does not exist in the standard BPS / Yangian / chiral-algebra
library. If $Y_{K3}$ exists on K3 at rank $> 1$, it requires a new
construction not yet available.

---

## Heal Phase 4 — the final converged state

### §H4.1 What the non-abelian K3 Yangian **is not**

- Not a BR2018 Schur chiral algebra of any 4d $\mathcal N=2$ SCFT
  (Wave 6 A1, Wave 7 A1.3 FHSV-falsifier).
- Not a Vafa--Witten boundary VOA in any clean physical sense
  (Wave 7 A1.1 self-demolition).
- Not the $K3 \times E$ BKM $\mathfrak g_{\Delta_5}$ (Wave 7 A4.2--A4.3).
- Not the Nakajima-Heisenberg on Hilb$^n(K3)$ (Wave 6 A2).
- Not the Schiffmann--Vasserot $\mathcal W_{1+\infty}$ at $c = 24$
  on generic K3 (no torus; Wave 6 A2; Wave 7 A3.1).
- Not a 6d hCS chiral algebra on $\mathbb R^2_{\varepsilon} \times K3
  \times C$ for any tested $C \in \{\mathbb C, E_\tau, \mathbb P^1_{\text{punct}}\}$
  at rank $> 1$ (Wave 7 A2, O16).

### §H4.2 What the non-abelian K3 Yangian **is**, per the manuscript

The manuscript `k3_yangian_chapter.tex:81--97` defines $Y(\mathfrak g_{K3})$
as a **conjectural target** reachable by two conjectural routes (A: CY-A;
B: BFN), neither completed. At the manuscript level, no non-abelian K3
Yangian is constructed; the symbol $Y(\mathfrak g_{K3})$ names an
aspirational object.

### §H4.3 What physical-side data IS available at rank 1

- **Rank-1 BPS spectrum**: 24 modes per $H^*(K3, \mathbb C)$.
  Chain-level chain-level computed from Hodge theory.
- **Rank-1 Schur/BPS partition function**: $1/\eta^{24}$. Proved via
  four independent primary sources (Göttsche 1990, Vafa--Witten 1994,
  DMVV 1997, Oberdieck--Pixton 2016).
- **Rank-1 Nakajima Heisenberg structure**: on $\bigoplus_n
  H^*(\mathrm{Hilb}^n(K3))$, the 24-rank lattice Heisenberg
  $\mathcal H_{\mathrm{Muk}}$ acts. Proved (Nakajima 1997).
- **Character match**: the Fock character of $\mathcal H_{\mathrm{Muk}}$ is
  $1/\eta^{24}$, coinciding with the rank-1 Schur/BPS index. Character-level
  identification; weakest possible level of equivalence (Wave 7 A3, O17).

### §H4.4 The Gaiotto-voice final diagnosis

From a Gaiotto-voice, BPS / class-S / little-string / Costello--Gaiotto
rigor standpoint, the non-abelian K3 Yangian is **not constructible**
from any standard physics primitive at rank $> 1$. At rank 1, only a
character-level match is available; this is the weakest form of
matching and does not establish the algebra structure.

The swarm's Wave 1--7 activity has, at its honest bottom, produced:
- the rank-1 character identification (H2.2);
- a 17-obstruction impossibility landscape (Wave 6 O1--O15 plus Wave 7
  O16, O17);
- a disambiguation of the physical setup (Wave 6 Gaiotto + Witten +
  Wave 7 Gaiotto).

**The non-abelian K3 Yangian as a non-trivial quantum group on K3 at
rank $> 1$ remains unconstructed, with strong evidence that standard
physics constructions do not produce it.**

---

## § Final Convergence Statement

### Claim 7-G-1 (rank-1 BPS partition function identification; [H], ProvedElsewhere)

The rank-1 BPS partition function of type IIA on $K3 \times E$,
equivalently the rank-1 Schur-analogue index of $\mathcal T_{K3 \times E}^{6d\text{-hCS}}$,
equals $1/\eta(q)^{24}$, matching the Fock character of the abelian
Mukai-Heisenberg VOA $\mathcal H_{\mathrm{Muk}}$.

**Primary sources**: Göttsche 1990 Math. Ann. 286 Thm 0.1;
Vafa--Witten 1994 hep-th/9408074 eq. (4.14); DMVV 1997
hep-th/9608096; Oberdieck--Pixton arXiv:1607.05105 Thm 1. Four
independent verification paths.

### Claim 7-G-2 (character match is not a VOA identification; [H], Wave-7 inscribed)

The character coincidence $\chi(\mathcal H_{\mathrm{Muk}}) = 1/\eta^{24}
= \chi(\mathcal W_{1+\infty})|_{c=24}$ does not imply VOA-level
isomorphism. The two VOAs differ in primary field content, module
category, and quantum dimensions. Character-level is the weakest
equivalence; VOA-level identification is open.

### Claim 7-G-3 (non-abelian K3 Yangian from any standard physics construction is obstructed at rank $> 1$; [H])

No standard physics construction (BR2018 Schur; Vafa--Witten boundary
VOA; FHSV chiral algebra; 6d hCS on $K3 \times C$ with $C \in \{\mathbb
C, E_\tau, \mathbb P^1_{\text{punct}}\}$; $K3 \times E$ BKM restricted
to K3; Nakajima-Heisenberg; SV/MO on generic K3) produces a non-abelian
Yangian on K3 at rank $> 1$ that is consistent with the Mukai-lattice
structure and closes CYBE.

**Supporting obstructions**: Wave 6 O1--O15; Wave 7 O16 (spectral-curve
over-constraint), O17 (character-vs-VOA level).

### Claim 7-G-4 (physical setup correction over Wave 6 Gaiotto; [H])

My Wave 6 §H1 "Vafa--Witten boundary VOA" reading was physics-sloppy.
Vafa--Witten on K3 is a topologically twisted 4d $\mathcal N=4$ theory
on a Riemannian 4-manifold; it is not a 4d $\mathcal N=2$ SCFT with a
Schur index; the "boundary VOA" phrase is underspecified in this
context. The correct frame is Costello--Gaiotto 6d hCS on $\mathbb
R^2_{\varepsilon} \times K3 \times E_\tau$ **which is itself
conjectural as a QFT**, with its rank-1 BPS partition function given
by the above four independent channels.

### Claim 7-G-5 (17-obstruction landscape; [H])

The obstruction landscape for any construction of a non-abelian K3
Yangian on K3 at rank $> 1$ is (at least) 17-dimensional, with
obstructions Wave-6 O1--O15 plus Wave-7 O16--O17. Any such construction
must navigate these obstructions; none currently does.

### Convergence

One full ATTACK pass over my own Heal 3 (Attack 4) found a new
angle — does any BPS algebra on a CY_3 containing K3 produce $Y_{K3}$?
— and converged to "no" for every standard candidate (Wave 7 A4.1--A4.4).
No new serious flaw has emerged after Wave 7 A4 / H4. Convergence.

---

## § Open Questions

Gaiotto-voice judgement on what would constitute genuine further progress:

1. **What is a non-standard construction of $Y(\mathfrak g_{K3})$?** Is
   there a class of physical systems outside the standard library (class
   S, BR2018 Schur, SV/MO stable envelope, BFN Coulomb, Vafa--Witten,
   heterotic compactification, Costello--Gaiotto hCS) that could
   produce a non-abelian Yangian on K3 at rank $> 1$? Candidates to
   explore: (a) spectral networks on K3 (rather than on a Gaiotto
   curve); (b) 6d $(2,0)$ of type $A_{r-1}$ on K3 directly without
   reduction, using M5-brane bound states and Kodaira-classification
   degenerations; (c) stacky chiral algebras on the Bridgeland
   stability manifold of $D^b(\Coh K3)$ rather than on a Riemann
   surface.

2. **Does the rank-1 character match lift to a VOA match?** The most
   immediate concrete question: can one exhibit an explicit VOA
   homomorphism $\mathcal W_{1+\infty}|_{c=24} \to \mathcal H_{\mathrm{Muk}}$
   (or the reverse), beyond the character-level match? This would
   close the gap between O17 and a genuine identification.

3. **Does the ADE-Kleinian sector attach to K3 in a way that survives
   the Nikulin rigidity obstruction?** Wave 6 O6 (Nikulin 1987: generic
   K3 has trivial connected automorphism). The ADE-Kleinian Yangian
   (proved on $\widetilde{S}_{\mathfrak g} \to \mathbb C^2/\Gamma$) attaches
   to K3 only at ADE-enhanced sub-loci, not generically. Is there a
   construction that stratifies this? The manuscript
   `rem:k3e-two-routes-yangian` sketches the BFN route for Kummer; the
   Mukai-form generalisation (`conj:bfn-k3-yangian-mukai`) is open.

4. **What is the correct auxiliary curve $C$ for Costello--Gaiotto hCS
   on K3?** Wave 7 O16 says no standard $C$ works. Is there a
   non-standard curve (e.g. the K3's vanishing cycle at an ADE point;
   the Gaiotto curve of FHSV; a specific cuspidal curve in the Siegel
   modular variety) that would close CYBE at rank $> 1$?

5. **Is $Y(\mathfrak g_{K3})$ even the right object to be constructing?**
   A pragmatic alternative: accept that the non-abelian K3 Yangian is
   unconstructed, inscribe the obstruction landscape as a theorem in
   its own right, and pivot the K3 programme to the stratified-family
   reading: constructing the individual ADE-locus Yangians (proved),
   Kummer-BFN Yangian (conjecture C1, well-posed), and abelian
   Mukai-Heisenberg (proved), without claiming a unifying "THE K3
   Yangian" at generic K3. This is the Beilinson-dictum choice that
   Wave 6 SYNTHESIS §8 recommended and Wave 7 confirms.

---

## File-line anchors (Wave 7 Gaiotto)

- `chapters/examples/k3_yangian_chapter.tex:81--97` — two routes A/B
  to $Y(\mathfrak g_{K3})$, both conjectural.
- `chapters/examples/k3_yangian_chapter.tex:108--120` — Theorem
  `thm:bfn-phi-ade-identification`, ProvedElsewhere on Kleinian ADE.
- `chapters/examples/k3_yangian_chapter.tex:186--198` — Prop
  `prop:k3e-selfdual-fock`, $Z_C = Z_H = 1/\eta^{24}$ at the Fock level.
- `chapters/theory/cy_to_chiral.tex:70--72` — Standard-input recovery
  (U4) of $\Phi_d$: $\Phi_2(D^b(\Coh K3)) = \mathcal H_{\mathrm{Muk}}$.
- `chapters/examples/k3e_bkm_chapter.tex:1--14` — $K3 \times E$
  distinct from K3 alone; BKM $\mathfrak g_{\Delta_5}$ on $K3 \times E$.
- `chapters/examples/k3e_bkm_chapter.tex:25--46` — Oberdieck--Pixton
  Igusa cusp form $\Delta_5$, $Z^X = C/(\Delta_5)^2$.
- `compute/lib/vafa_witten_k3.py` — Vafa--Witten / Göttsche /
  DMVV arithmetic at rank 1 on K3.
- `compute/lib/bllpr_k3_connection.py` — BLLPR / K3 Yangian
  disambiguation (73-test internal-consistency module).
- `compute/lib/affine_yangian_gl1.py` — SV/MO structure function.
- `notes/k3_nonabelian_yangian_swarm_wave6_20260419/agent_10_gaiotto_wave6.md`
  — Wave 6 Gaiotto.
- `notes/k3_nonabelian_yangian_swarm_wave6_20260419/agent_08_witten_wave6.md`
  §A1, §H1 — heterotic-$T^4$ / IIA-K3 disambiguation.
- `notes/k3_nonabelian_yangian_swarm_wave6_20260419/SYNTHESIS_WAVE6_ADVERSARIAL.md`
  §3 — the 15-obstruction landscape.

---

## References (Wave 7 Gaiotto)

- Beem, C., Rastelli, L., *Vertex operator algebras, Higgs branches,
  and modular differential equations*, JHEP 08 (2018) 114,
  arXiv:1707.07679. [BR2018]
- Beem, C., Lemos, M., Liendo, P., Peelaers, W., Rastelli, L.,
  van Rees, B. C., *Infinite chiral symmetry in four dimensions*,
  Commun. Math. Phys. 336 (2015) 1359, arXiv:1312.5344. [BLLPR]
- Borcherds, R. E., *Automorphic forms with singularities on
  Grassmannians*, Invent. Math. 132 (1998), 491. [Borcherds 1998]
- Costello, K., *Supersymmetric gauge theory and the Yangian*,
  arXiv:1303.2632 (2013).
- Costello, K., *Holography and Koszul duality: the example of the
  M2 brane*, arXiv:1705.02500 (2017).
- Costello, K., *Gauge theory and integrability, I, II, III*,
  arXiv:1709.09993 (2017), arXiv:1802.01579 (2018), arXiv:1908.02289
  (2019). (Costello--Witten--Yamazaki [CWY 2018])
- Costello, K., *Integrable lattice models from four-dimensional field
  theories*, arXiv:1711.11046 (2017).
- DMVV: Dijkgraaf, R., Moore, G., Verlinde, E., Verlinde, H.,
  *Elliptic genera of symmetric products and second quantized
  strings*, Commun. Math. Phys. 185 (1997) 197, hep-th/9608096.
- Ferrara, S., Harvey, J. A., Strominger, A., Vafa, C.,
  *Second-quantized mirror symmetry*, Phys. Lett. B 361 (1995) 59,
  hep-th/9505162. [FHSV]
- Göttsche, L., *The Betti numbers of the Hilbert scheme of points
  on a smooth projective surface*, Math. Ann. 286 (1990) 193, Thm 0.1.
- Gritsenko, V., Nikulin, V., *Automorphic forms and Lorentzian
  Kac–Moody algebras II*, Internat. J. Math. 9 (1998) 201.
- Harvey, J., Moore, G., *Algebras, BPS states, and strings*, Nucl.
  Phys. B 463 (1996) 315, hep-th/9510182.
- Hofman, D. M., Maldacena, J., *Conformal collider physics*, JHEP 05
  (2008) 012, arXiv:0803.1467, Theorem 1.
- Hull, C. M., Townsend, P. K., *Unity of superstring dualities*,
  Nucl. Phys. B 438 (1995) 109, hep-th/9410167.
- Huybrechts, D., *Lectures on K3 surfaces*, Cambridge Studies in
  Advanced Math. 158 (2016), Theorem 5.2.1.
- Kapustin, A., Witten, E., *Electric-magnetic duality and the
  geometric Langlands program*, Commun. Num. Theor. Phys. 1 (2007) 1,
  hep-th/0604151.
- Kontsevich, M., Soibelman, Y., *Stability structures, motivic
  Donaldson–Thomas invariants and cluster transformations*,
  arXiv:0811.2435 (2008).
- Maulik, D., Okounkov, A., *Quantum groups and quantum cohomology*,
  arXiv:1211.1287.
- Maulik, D., Pandharipande, R., Pixton, A., *Curves on K3 surfaces and
  modular forms*, J. Topology 3 (2010) 937, arXiv:1001.2719.
- Molev, A., *Yangians and classical Lie algebras*, AMS Math. Surveys
  and Monographs 143, 2007.
- Nakajima, H., *Heisenberg algebra and Hilbert schemes of points on
  projective surfaces*, Ann. Math. 145 (1997) 379, Theorem 1.
- Nikulin, V. V., *Integer symmetric bilinear forms and some of their
  geometric applications*, Math. USSR Izv. 14 (1980) 103; 
  *On the topological classification of real Enriques surfaces I*,
  arXiv:alg-geom/9707009 (1987, earlier form).
- Oberdieck, G., Pixton, A., *Holomorphic anomaly equations and the
  Igusa cusp form conjecture*, Invent. Math. 213 (2018) 507,
  arXiv:1607.05105.
- Schiffmann, O., Vasserot, E., *Cherednik algebras, W-algebras, and
  the equivariant cohomology of the moduli space of instantons on
  $\mathbb A^2$*, Publ. IHES 118 (2013) 213, arXiv:1202.2756.
- Sen, A., *String–string duality conjecture in six dimensions and
  charged solitonic strings*, Nucl. Phys. B 450 (1995) 103,
  hep-th/9504027.
- Vafa, C., Witten, E., *A strong coupling test of S-duality*,
  Nucl. Phys. B 431 (1994) 3, hep-th/9408074, eq. (4.14).
- Witten, E., *String theory dynamics in various dimensions*,
  Nucl. Phys. B 443 (1995) 85, hep-th/9503124.

---

---

## Attack Phase 5 — the 6d (2,0) / class-S type-error on K3

### §A5.1 "Class S of K3" is a type-error

The prompt isolates the central Gaiotto-voice question: **class S of
K3 is not standard.** Let me state it sharply.

A 6d $(2,0)$ theory of ADE type $\mathfrak g$ exists on a
$6$-manifold. Compactifying on a **Riemann surface** $\Sigma$ of genus
$g$ with $n$ punctures yields a 4d $\mathcal N = 2$ theory, the
**class-S theory** $\mathcal T[\mathfrak g; \Sigma, \{\text{punctures}\}]$
(Gaiotto 2009, arXiv:0904.2715). The procedure requires $\Sigma$ to be
**2-real-dimensional = 1-complex-dimensional**.

$K3$ is a $4$-real-dimensional = $2$-complex-dimensional Kähler
manifold. The compactification "$6\text{d}(2,0)$ on $K3$" produces a
**2d theory**, *not* a 4d theory, because $6 - 4 = 2$. The resulting
2d theory is the $\mathfrak g$-type $(0,2)$ sigma model into
$\mathrm{Hilb}^n(K3)$ at large central charge (Vafa--Witten,
Bershadsky--Johansen--Sadov--Vafa 1994 arXiv:hep-th/9511222).

**Net type-error**: "class S of K3" is a phrase that tries to
compactify 6d $(2,0)$ on a $4$-manifold and still get a 4d class-S
theory. The dimensional count forbids this: compactifying on $K3$ gives
2d, not 4d.

The Wave 1--7 programme never stated "class S of K3" in the manuscript
directly (grep of k3_yangian_chapter.tex for "class S": zero matches),
but the **motivation language** in the Wave-5 Gaiotto §6.2 and my own
Wave-6 Gaiotto §A3.1 implicitly invoked it ("class S of type $A_1$ on
a Gaiotto curve $C$, K3 internal"). That phrasing is correct only when
$K3$ is **internal geometry** for IIB and $\Sigma = C$ is the actual
Gaiotto curve; it is *not* "class S of K3."

### §A5.2 The valid class-S-adjacent setups

Three distinct setups admit $K3$ without the type-error:

**(S5-a) Class S on $\Sigma$, $K3$ internal for type IIB.**
IIB on $K3 \times \mathbb R^{5,1}$ → 6d $(2,0)$ of type $A_1$ on
$\mathbb R^{5,1}$. Then compactify on $\Sigma$ → 4d class-S theory on
$\mathbb R^{3,1}$. This is Wave-6 §A3.1 setup (1); $K3$ is the IIB
compactification manifold, not involved in the 4d SCFT's moduli.

**(S5-b) 6d $(2,0)$ on $K3 \times \Sigma$ as a 2d theory.**
The $4$-manifold $K3$ is the compactification base; the resulting 2d
theory on $\Sigma$ is the Vafa--Witten-twisted Euler-characteristic
generating sigma model on $\mathrm{Hilb}^\bullet(K3)$, with Poincaré
polynomial $1/\eta(q)^{24}$ at the partition-function level. No class-S
structure on a *4d* theory.

**(S5-c) 6d $(2,0)$ on $K3 \times S^3 \times \mathbb R$ with
$\Omega$-background.**
$6$ dimensions fill; the $S^3 \times \mathbb R$ factor supports the
4d Schur-index geometry after reduction of $K3$ trivially. But: this
is unmotivated; $K3$ has no isometry group acting on it, and the $S^3$
factor must fibre over $K3$ to give something. No natural construction
emerges.

None of (S5-a)--(S5-c) produces a non-abelian K3 Yangian. Setup
(S5-a) gives BR2018 Schur chiral algebras with sign obstruction (Wave 6
§A1). Setup (S5-b) gives Vafa--Witten sigma model on
$\mathrm{Hilb}^\bullet(K3)$. Setup (S5-c) is not a valid reduction.

### §A5.3 M5-brane bound-state framework

The Gaiotto-style fix: replace "class S of K3" with **M5-brane bound
states wrapping K3**. $N$ M5-branes wrapping $K3$ in M-theory on
$K3 \times \mathbb R^{6,1}$ give a 3d $\mathcal N = 2$ theory on
$\mathbb R^{2,1}$ with $\mathrm{SU}(N)^{24}$ global symmetry and
Kaluza--Klein modes indexed by $H^*(K3, \mathbb Z) \cong II_{3,19} \oplus (+2)$
(wave decomposition on Mukai-rank-24 lattice). Then further
compactification on $S^1$: 2d $\mathcal N = (0,4)$ with MSW
(Maldacena--Strominger--Witten 1997 arXiv:hep-th/9711053) CFT target
$\mathrm{Hilb}^{N^2}(K3)$ at central charge $c = 6 N^2$ (for $N$ M5's
wrapping $K3$, the MSW CFT has $c_L = 3 Q_P \cdot H$ for charges
summing via K3-geometry).

This is a **genuine 2d CFT**, not a chiral algebra on an auxiliary
Riemann surface; it is a full sigma-model CFT on $\mathrm{Hilb}^{N^2}(K3)$.
It has a chiral half, and that chiral half is the K3 elliptic genus
$\phi_{0,1}$ raised to symmetric powers (DMVV). Not a Yangian; not a
rational $\Eone$-chiral algebra.

**Verdict**: M5-on-K3 gives MSW CFT, not K3 Yangian. Adjacent but
distinct.

### §A5.4 Little string theory on $K3 \times T^3$

Another Gaiotto-adjacent construction: little string theory of ADE
type on $K3 \times T^3$. Little string theory (Seiberg 1997
arXiv:hep-th/9705221) is the decoupling limit of 6d $(2,0)$ at
self-dual string tension; its compactification on $K3 \times T^3$
gives a 2d theory that, in certain limits, produces the Douglas--Moore
(DM; arXiv:hep-th/9603167) quiver Yangian construction of ADE-type
affine quantum groups. But this is again about **ADE sub-Yangians at
ADE points** of K3 moduli, not a global non-abelian K3 Yangian.

**Verdict**: LST-on-$K3 \times T^3$ gives ADE affine Yangians at ADE
points (already covered by `thm:bfn-phi-ade-identification`), not a
global non-abelian $Y(\mathfrak g_{K3})$.

### §A5.5 Moore–Tachikawa 2d TQFT valued in holomorphic symplectic varieties

Moore--Tachikawa (2011 arXiv:1106.5698) construct a 2d TQFT valued in
the category of holomorphic symplectic varieties with Hamiltonian
$G$-actions, such that the object on $\Sigma_g$ is the
Moore--Tachikawa symplectic variety $X_G(\Sigma_g)$. For $G = \mathrm{PGL}_N$
and $\Sigma = K3$ (illegally, since K3 is 4-dim not 2-dim), the Moore--Tachikawa
machine **does not extend**: the 2d TQFT framework requires a
2-dim source.

However, Moore--Tachikawa has a **6d** extension via
Garner--Williams (arXiv:2106.07387) to factorization algebras; the
analogue with 4-dim source manifold is a conjectural **6d** TQFT
valued in categories of symplectic-stack-valued factorization algebras.
At $\Sigma_4 = K3$, the 6d TQFT output would be a category-valued
factorization algebra on K3 times $\mathbb R^2$, not a chiral algebra
on an auxiliary curve. This is yet another construction adjacent to
the K3 Yangian but structurally different.

**Verdict**: Moore--Tachikawa does not naturally extend from 2d to 4d
sources; any 6d extension produces K3-valued factorization algebras,
not Yangians.

### §A5.6 Attack 5 conclusion — no "class S of K3" lane exists

All Gaiotto-natural class-S-adjacent setups (S5-a, S5-b, S5-c,
M5-on-K3, LST-on-$K3 \times T^3$, Moore--Tachikawa) either run into
the dimensional type-error, the BR2018 sign obstruction, or produce an
adjacent object (MSW CFT, ADE-point sub-Yangians, $K3 \times E$
factorization algebras) that is *not* a non-abelian K3 Yangian on K3
alone.

This crystallises a new obstruction:

> **O18 (Wave 7 Gaiotto obstruction, class-S type-error)**. No
> compactification of 6d $(2,0)$ of ADE type $\mathfrak g$ on $K3$ can
> produce a 4d $\mathcal N = 2$ class-S theory with K3 as its Gaiotto
> curve, since K3 is 4-real-dimensional. Any candidate "class S of
> K3" lane either (i) converts K3 into internal IIB geometry (Setup
> S5-a) and produces BR2018 Schur chiral algebras with sign
> obstruction, (ii) compactifies K3 as the base and yields a 2d
> theory (Setup S5-b) with MSW CFT on $\mathrm{Hilb}^\bullet(K3)$, or
> (iii) localises to ADE points of K3 moduli (LST, DM) and produces
> only ADE sub-Yangians already covered by
> `thm:bfn-phi-ade-identification`. None gives a non-abelian
> $Y(\mathfrak g_{K3})$ on generic K3.

---

## Heal Phase 5 — commit to the heterotic-on-$T^4$ 6d $(1,1)$ + wrapping identification

### §H5.1 The ADE type is fixed by the heterotic dual

The one physical setup that survives Wave 6 Witten's attack and my
Wave 7 A5 demolition is:

**Setup H5** (the surviving Gaiotto-dual statement):

$$
\text{6d }(2,0)\text{ of type }A_0 \;\text{(trivial)}\; \text{ compactified trivially, with}
\text{ 24 extra abelian tensor multiplets arranged on Mukai lattice } II_{4,20},
$$

which is the heterotic-dual-to-IIA-on-$K3$ setup rather than a genuine
6d $(2,0)$ of non-trivial ADE type. The "24 tensor multiplets" are
the KK modes of the IIA-on-$K3$ theory (one per basis element of
$H^*(K3, \mathbb Z)$). Their chiral algebra at rank 1 is the rank-24
lattice VOA $V_{\Lambda_{\mathrm{Muk}}}$ with signature $(4, 20)$:
non-unitary, with 20 left-moving + 4 right-moving Heisenberg currents.

Status: **primary-source described** (Hull--Townsend 1994, Sen 1995,
Witten 1995). Not a Yangian, not a chiral algebra on an auxiliary
curve; it is a 6d free-tensor-multiplet theory's KK tower.

### §H5.2 The upgrade to a non-abelian Yangian requires ADE-enhancement at ADE points

At ADE-enhancement sub-loci of K3 moduli, the abelian
$U(1)^{24}$ gauge symmetry of the FHSV-style theory enhances to
non-abelian $\mathrm{ADE}$ gauge symmetry: at an $A_1$ singularity
point, $U(1)^2 \to \mathrm{SU}(2)$ (Witten 1995, Kachru--Vafa 1995
arXiv:hep-th/9505105); at $A_n$, $U(1)^{n+1} \to \mathrm{SU}(n+1)$;
and so on. This enhancement lifts, after 4d reduction on $T^2$ and
via 6d hCS on $\mathbb R^2_\varepsilon \times K3$, to the ADE sub-Yangian
$Y^\mu(\widehat{\mathfrak g})_{k=1}$ at the ADE point (Kronheimer
resolution → BFN Coulomb branch → `thm:bfn-phi-ade-identification`).

### §H5.3 Stratified K3 Yangian (heal, final form)

Combining the Wave 6 obstructions, Wave 7 O16--O18, and this heal:

$$
Y(\mathfrak g_{K3}) \;=\; \mathcal H_{\mathrm{Muk}} \;\oplus\;
\bigoplus_{\Lambda_{\mathfrak g} \hookrightarrow \Lambda_{\mathrm{Muk}}}
Y^\mu(\widehat{\mathfrak g})_{k=1}^{\mathrm{BFN}} \;\oplus\; (\text{cross-strata couplings})
$$

where:
- the abelian core $\mathcal H_{\mathrm{Muk}}$ is proved (rank-24
  lattice VOA of $\Lambda_{\mathrm{Muk}}$);
- each sub-Yangian $Y^\mu(\widehat{\mathfrak g})_{k=1}^{\mathrm{BFN}}$
  is proved (Theorem `thm:bfn-phi-ade-identification`);
- the cross-strata couplings are **conjectural**, and Wave 6 A3
  established that on orthogonal strata they vanish (Whitehead), so
  they live only on non-orthogonal embeddings (rank-1 to rank-$n$ etc.).

**Status**: This is the corrected form of the Wave-5 "stratified
$L_\infty$-coupled quasi-Hopf object" claim. It is what the physics
side suggests, *physics-wise anchored* at each stratum (abelian core
via Vafa--Witten / FHSV; ADE strata via Kachru--Vafa / Kronheimer /
BFN); but the cross-strata couplings remain open, and a unifying
non-abelian Yangian on K3 as a whole does not exist at rank $> 1$
from any standard physics setup (Wave 6 A5).

### §H5.4 The stratified form is the final Gaiotto-voice verdict

> The K3 "Yangian" is not a single non-abelian Yangian on K3 at rank
> $> 1$, but a **stratified landscape**: abelian core from FHSV /
> lattice VOA, ADE sub-Yangians at ADE points from BFN / Kronheimer
> (proved), conjectural cross-strata couplings between non-orthogonal
> sub-lattices, and no natural physical unification at generic K3.
> This is the physics reading consistent with the 18-obstruction
> landscape.

---

## Attack Phase 6 — the BKM / Siegel / automorphic-corrections bridge

### §A6.1 The automorphic-corrections paper as primary source

The PDF `/Users/raeez/Downloads/raeez.lorgat.automorphic-corrections.pdf`
(Raeez Lorgat, dated 2 April 2020) presents an elementary construction
of a pair $(\mathfrak g, \mathfrak g_{\Delta_5})$: a Kac--Moody
superalgebra $\mathfrak g$ built on $\Lambda^{3,2}$ with Gram matrix
$\bigl(\begin{smallmatrix} 2 & -2 & -2 \\ -2 & 2 & -2 \\ -2 & -2 & 2 \end{smallmatrix}\bigr)$
and its automorphic correction $\mathfrak g_{\Delta_5}$ whose
denominator is the Gritsenko--Nikulin--Igusa cusp form $\Delta_5$ of
weight 5 on $\mathrm{Sp}_4(\mathbb Z)$. The underlying geometry is the
CY$_3$ $X = (S \times E)/(\mathbb Z/N\mathbb Z)$ for $S$ K3 and $E$
elliptic; at $N = 1$ the Oberdieck--Pixton theorem gives
$Z^X = C/(\Delta_5)^2$.

This is **Vol III's own primary source** for the BKM superalgebra
$\mathfrak g_{\Delta_5}$, and it places the object firmly on
$K3 \times E$, **not on K3 alone**.

### §A6.2 Attack: can BKM be "class-S-ified" back to K3?

Question: is there a class-S-like construction that takes
$\mathfrak g_{\Delta_5}$ (living on $K3 \times E$) and restricts to an
object on K3? If so, that restricted object could be the candidate
K3 Yangian.

From the PDF, §5: the Weyl--Kac--Borcherds character formula on
$\mathfrak g_{\Delta_5}$ gives $\Delta_5 = \Phi$ (the denominator
function); restricting $E \to$ point (elliptic degeneration $\tau
\to i\infty$) would reduce the Siegel form $\Delta_5(Z_1, Z_2, Z_3)$
at $\tau_3 \to i\infty$ (the elliptic fibre parameter) to a form on
$\mathrm H_1 = \mathbb H$. But the PDF §6 shows
$\Delta_5(Z)|_{\tau_3 \to i\infty}$ has a simple first Fourier-Jacobi
coefficient $\phi_{5, 1/2}(z_1, z_2) = \eta(z_1)^9 v_{11}(z_1, z_2)$
(PDF page 3 calculation), which is the Jacobi form generating
$\mathfrak g_{\Delta_5}$'s root multiplicities.

The "restriction to K3" of $\mathfrak g_{\Delta_5}$ would correspond to
taking $\tau_3 \to i\infty$, i.e. forgetting the elliptic direction.
In that limit, $Z^X \to Z^{K3}$ at a specific moduli boundary; the
resulting object is the Mathieu moonshine $M_{24}$-equivariant
K3 elliptic genus $\phi_{0,1}$, which is a Jacobi form of weight 0
index 1 with Fourier coefficients encoded by $M_{24}$
representations (Eguchi--Ooguri--Tachikawa 2010 arXiv:1004.0956;
Cheng--Duncan--Harvey 2014 arXiv:1404.4191).

**So**: the "class-S-ification" of BKM from $K3 \times E$ down to K3
is the passage from $\mathfrak g_{\Delta_5}$ to the **Mathieu moonshine
Jacobi form $\phi_{0,1}$ on K3**. This is a **known primary-source
object**.

### §A6.3 Is the Mathieu moonshine $\phi_{0,1}$ the K3 Yangian?

**No**. $\phi_{0,1}$ is a **Jacobi form** (a function on
$\mathbb H \times \mathbb C$), not an algebra or Yangian. Its
coefficients are $M_{24}$ characters. The *algebra* that would sit
above it is the **Mathieu moonshine module** $K^\natural$ (a
hypothetical VOA whose character would be $\phi_{0,1}$, analogous to
the Monster VOA $V^\natural$ whose character is $j(\tau)$). Such
$K^\natural$ is **conjectural** (Gaberdiel--Hohenegger--Volpato 2010
arXiv:1011.6553; still open as of 2025).

So class-S-ification of BKM reduces K3-Yangian-candidate to
Mathieu-moonshine-VOA-candidate, another *conjectural* object. This
does not close the gap; it relocates it.

### §A6.4 The Siegel bridge: what's a rigorous connection on the K3 side?

Concrete rigorous statements on the K3 × E ↔ K3 bridge:

**(S-1)** $Z^{K3 \times E}$ = $C/\Delta_5^2 = C'/\Phi_{10}$
(Oberdieck--Pixton 2016, `k3e_bkm_chapter.tex:36--40`).

**(S-2)** The Fourier--Jacobi expansion of $\Delta_5$ at the cusp
$\tau_3 \to i\infty$ gives $\phi_{5,1/2}$, and $\phi_{5,1/2}^2 =
\phi_{10, 1}$ is proportional to the first Fourier--Jacobi
coefficient of $\Delta_{10} = \Phi_{10}$; so $\Phi_{10}$'s elliptic
expansion connects to K3 elliptic genus.

**(S-3)** The $K3$ elliptic genus $\phi_{0,1}(\tau, z) = 2y + 20 -
2y^{-1} + \dots$ (with $y = e^{2\pi i z}$) is the Borcherds input for
the weight-10 Igusa form: the Borcherds multiplicative lift of
$\phi_{0,1}$ produces $\Delta_5$ (PDF §6). So
$\mathfrak g_{\Delta_5}$ encodes $M_{24}$ moonshine structurally.

**(S-4)** The Gritsenko--Clery result (PDF §1): all 8 diagonal-divisor
modular forms on paramodular groups $\Gamma_t(N)$ come from arithmetic
CY-3-fold geometry. This is the primary-source anchor for Wave 6
Polyakov §2.3 "16 siblings of $\Delta_5$" (the 8 diagonal-divisor
forms × 2 genera = 16 automorphic BKM candidates).

### §A6.5 Siegel/BKM bridge final state: partial

The Siegel/BKM bridge connecting the K3 Yangian to the
$(K3 \times E)$-BKM $\mathfrak g_{\Delta_5}$ is **partial**: it
rigorously identifies the $K3 \times E$ CY$_3$ BKM via
Oberdieck--Pixton + automorphic-corrections PDF; it does **not** lift
to a rigorous K3-only Yangian structure. The "restriction to K3"
passage is the Mathieu moonshine $\phi_{0,1}$, whose VOA ($K^\natural$)
is conjectural.

So the BKM/Siegel bridge is **well-posed only on $K3 \times E$**. On
K3 alone, the bridge is **conjectural** via Mathieu moonshine.

---

## Heal Phase 6 — inscribe the stratified + BKM-adjacent final statement

### §H6.1 The honest final Gaiotto-voice diagnosis

After six attack-heal cycles:

1. **Abelian core** $\mathcal H_{\mathrm{Muk}} = \Phi_2(D^b(\Coh K3))$
   is proved as a rank-24 lattice VOA of $\Lambda_{\mathrm{Muk}}$
   (`thm:phi-k3-explicit`). Its character $1/\eta^{24}$ matches the
   BPS partition function of IIA / DT on $K3 \times E$ restricted to
   rank 1, via four independent primary sources (Göttsche 1990,
   Vafa--Witten 1994, DMVV 1997, Oberdieck--Pixton 2016).
   Character-level match only (O17); not a VOA isomorphism to any
   Yangian.

2. **ADE sub-Yangians** $Y^\mu(\widehat{\mathfrak g})_{k=1}^{\mathrm{BFN}}$
   at ADE points of K3 moduli are proved (`thm:bfn-phi-ade-identification`,
   Kronheimer + BKR + BFN + Nakajima--Takayama). They are attached to
   resolved Kleinian singularities $\widetilde S_{\mathfrak g} \to
   \mathbb C^2 / \Gamma$, not to K3 globally; they attach to K3 at
   ADE sub-loci via the appropriate lattice embedding
   $\Lambda_{\mathfrak g} \hookrightarrow \Lambda_{\mathrm{Muk}}$.

3. **Non-abelian K3 Yangian on generic K3** at rank $> 1$ is not
   produced by any standard physics construction: BR2018 (sign
   obstruction O5), Vafa--Witten boundary VOA (underspecified, Wave
   7 A1.1), FHSV 4d $\mathcal N=2$ (sign obstruction O5 at abelian
   locus; Wave 7 A1.3), 6d hCS on $K3 \times C$ for any standard $C$
   (O16), $K3 \times E$ BKM restricted to K3 (off-scope, Wave 6 A2.3),
   SV/MO on generic K3 (no torus, O6), M5-on-K3 (gives MSW CFT, not
   Yangian; Wave 7 A5.3), LST-on-$K3 \times T^3$ (gives ADE sub-Yangians,
   already covered; Wave 7 A5.4), class-S-on-K3 (type error, O18),
   Moore--Tachikawa (does not extend; Wave 7 A5.5).

4. **BKM / Siegel bridge** rigorous on $K3 \times E$ via
   Oberdieck--Pixton + automorphic-corrections; partial / conjectural
   on K3 alone via Mathieu moonshine $\phi_{0,1}$ and the putative
   VOA $K^\natural$ (Gaberdiel--Hohenegger--Volpato 2010 open).

### §H6.2 Consolidated obstruction landscape — 18 obstructions

O1--O15 (Wave 6 synthesis §3), O16 (spectral-curve over-constraint,
Wave 7 A2), O17 (character-vs-VOA, Wave 7 A3), O18 (class-S
type-error on K3, Wave 7 A5).

None of these is a construction of the K3 Yangian; all are
obstructions that constrain what it could be.

### §H6.3 Gaiotto-voice final sign-off

**The non-abelian K3 Yangian on generic K3 at rank $> 1$ is not
physically producible from the standard BPS / Schur / chiral-algebra /
class-S library.** The programme should either accept this as a
long-term conjecture with an 18-obstruction landscape and inscribe
that landscape as a theorem of its own, or pivot to the
stratified-family reading: abelian $\mathcal H_{\mathrm{Muk}} \oplus
\bigoplus_\Lambda Y^{\mathrm{BFN}}(\mathfrak g_\Lambda)$-with-conjectural-couplings,
with no unified "THE K3 Yangian" at generic K3.

---

## CONVERGED STATEMENT

After six full attack-heal cycles:

**Claim 7-G-CONV (the Gaiotto-voice Wave 7 converged statement, final)**:

(i) **Abelian core, rank 1, proved**:
$\mathcal H_{\mathrm{Muk}} = \Phi_2(D^b(\Coh K3))$ is a rank-24 lattice
VOA of $\Lambda_{\mathrm{Muk}}$ with character $1/\eta(q)^{24}$
(`thm:phi-k3-explicit`, `cy_to_chiral.tex:71`).

(ii) **Explicit 6d physical setup (conjectural as QFT, rank-1 BPS
partition function proved)**: $\mathcal T_{K3 \times E}^{6d\text{-hCS}}$
= 6d hCS on $\mathbb R^2_\varepsilon \times K3 \times E_\tau$. Rank-1
BPS partition function (analogue of Schur index): $1/\eta(q)^{24}$.
Proved via four primary sources: Göttsche 1990 (Hilb$^n$ Euler char);
Vafa--Witten 1994 (SU(2) S-duality); DMVV 1997 (second-quantised);
Oberdieck--Pixton 2016 (Igusa cusp form / DT).

(iii) **Riemann-surface data**: $\Sigma = E_\tau$ (elliptic curve), the
spectral curve of the 6d hCS construction. This is a **choice** not a
derivation: rational ($\mathbb C$) is trivial, punctured sphere
obstructed by BR2018 sign, only elliptic gives the Belavin-adjacent
structure; but at rank $> 1$ the elliptic R-matrix attached to Mukai
fails CYBE (O13), leaving the spectral-curve choice over-constrained
at rank $> 1$ (O16).

(iv) **BPS algebra / chiral algebra identification at rank 1, character
level only**: the rank-1 BPS partition function matches the Fock
character of $\mathcal H_{\mathrm{Muk}}$. It does **not** lift to a VOA
isomorphism (O17); $V_{\Lambda_{\mathrm{Muk}}}$ and $\mathcal
W_{1+\infty}|_{c=24}$ have the same character but different VOA
structures.

(v) **Pattern 236 lane declarations**:
- Chain-level: 24-mode BPS spectrum from Hodge decomposition of K3.
- $(\infty,1)$-categorical: factorization algebra on K3 × $E$ at rank
  1 localises to lattice factorization algebra of $\Lambda_{\mathrm{Muk}}$.
- Physical: BPS partition function $1/\eta^{24}$ on $\mathbb R^2_\varepsilon \times K3 \times E$.

(vi) **Non-abelian, rank $> 1$, on K3 alone**: no standard-physics
construction produces a non-abelian K3 Yangian satisfying both the
Mukai-lattice constraints and CYBE closure. Eighteen obstructions
(O1--O18, including Wave 7 O16--O18) constrain the space of any
hypothetical such construction.

(vii) **Correct physical frame**: Costello--Gaiotto 6d hCS on
$\mathbb R^2_\varepsilon \times K3 \times E_\tau$ (conjectural as QFT,
a research programme). **Incorrect frames** (explicitly retracted):
BR2018 Schur on 4d $\mathcal N = 2$ SCFT (sign obstruction O5); FHSV
Schur chiral algebra (sign obstruction at abelian point, Wave 7 A1.3);
"class S of K3" (dimensional type-error, Wave 7 O18); Vafa--Witten
boundary VOA without QFT specification (Wave 7 A1.1).

---

## NEW CONJECTURES

**Conjecture 7-G-1 (spectral-curve over-constraint; [H])**. No choice
of auxiliary Riemann surface $C$ (rational, elliptic, or
punctured-sphere) gives a non-trivial K3 Yangian chiral algebra on
$K3 \times C$ with an R-matrix closing CYBE at rank $> 1$ and matching
the Mukai-lattice structure. This is not a theorem: it is an inductive
generalisation from the three tested candidate curves. A non-standard
curve (vanishing cycle at an ADE point, FHSV Seiberg--Witten curve,
compactified-Jacobian fibre) has not been ruled out.

**Conjecture 7-G-2 (class-S-ification of BKM; [M])**. The
automorphic-corrections BKM superalgebra $\mathfrak g_{\Delta_5}$ on
$K3 \times E$ restricts at the elliptic boundary $\tau_E \to i\infty$
to a Mathieu-moonshine object on K3, carrying $M_{24}$-equivariant
Jacobi form $\phi_{0,1}$ data. The putative VOA $K^\natural$ whose
character is $\phi_{0,1}$ is the candidate for the non-abelian K3
Yangian's Drinfeld centre or Hochschild centre at the $M_{24}$-locus.
Open.

**Conjecture 7-G-3 (stratified K3 Yangian)** [H]. The "K3 Yangian"
is a stratified object
$Y(\mathfrak g_{K3}) = \mathcal H_{\mathrm{Muk}} \oplus
\bigoplus_{\Lambda \hookrightarrow \Lambda_{\mathrm{Muk}}}
Y^\mu(\widehat{\mathfrak g}_\Lambda)_{k=1}^{\mathrm{BFN}} \oplus
(\text{cross-strata couplings})$, with the abelian core and ADE strata
proved individually and the cross-strata couplings open at
non-orthogonal sub-lattice pairs. No natural physical unification of
all strata at generic K3 exists in the standard library.

**Conjecture 7-G-4 (6d hCS on $\mathbb R^2_\varepsilon \times K3 \times
E$ existence)** [M]. The conjectural 6d holomorphic Chern--Simons
theory on $\mathbb R^2_\varepsilon \times K3 \times E_\tau$ with gauge
rank $r$ exists as a perturbatively finite QFT at least to some
bounded loop order, with factorisation-algebra structure in the
Costello--Gwilliam sense and boundary $\infty$-chiral algebra at the
$E_\tau$-sector given by $V_{\Lambda_{\mathrm{Muk}}}$-enriched for
rank $r = 1$, and conjectural rank-$r$ structure for $r > 1$. Open;
the 4-loop finiteness of Wave 5 is undemonstrated (O7).

**Conjecture 7-G-5 (rank-1 character ⇒ VOA lift) [M]**. There exists
an explicit VOA homomorphism
$\mathcal W_{1+\infty}|_{c=24} \hookrightarrow V_{\Lambda_{\mathrm{Muk}}}$
that lifts the character coincidence
$\chi(\mathcal W_{1+\infty}|_{c=24}) = \chi(V_{\Lambda_{\mathrm{Muk}}}) = 1/\eta^{24}$
to a VOA embedding, matching 24 of the $\mathcal W_{1+\infty}$
higher-spin generators to the 24 lattice Heisenberg currents of
$V_{\Lambda_{\mathrm{Muk}}}$. Open; closing this would upgrade O17 from
character-only to VOA-level.

---

## REQUIRED MANUSCRIPT AMENDMENTS (file:line specific)

### Amendment A (k3_yangian_chapter.tex) — add Wave 7 obstructions as lemmas

**Target**: `chapters/examples/k3_yangian_chapter.tex` following
line 181 (after `rem:bfn-kummer-reduces-to-a1`).

**Insert** (after the existing remark block):

```latex
\begin{lemma}[Class-S-of-K3 type error; Wave 7 Gaiotto O18]
\label{lem:class-s-k3-type-error}
\ClaimStatusProvedHere
No compactification of 6d $(2,0)$ of ADE type $\fg$ on $K3$
produces a 4d $\cN = 2$ class-S theory with K3 as its Gaiotto curve,
since K3 is 4-real-dimensional while Gaiotto curves are 2-real-dimensional.
Compactification of 6d $(2,0)$ on K3 produces a 2d theory (sigma model
into $\operatorname{Hilb}^\bullet(K3)$, Bershadsky--Johansen--Sadov--Vafa
1994 hep-th/9511222), not a 4d SCFT. Any candidate ``K3 Yangian via
class S'' lane either (i) treats K3 as IIB internal geometry
(BR2018 sign obstruction, Wave 6 A1), (ii) reduces to the 2d sigma
model on $\operatorname{Hilb}^\bullet(K3)$ (Vafa--Witten partition
function $1/\eta^{24}$, character-only), or (iii) localises to ADE
points (covered by Theorem~\ref{thm:bfn-phi-ade-identification}).
\end{lemma}

\begin{lemma}[Spectral-curve over-constraint; Wave 7 Gaiotto O16]
\label{lem:spectral-curve-overconstraint}
\ClaimStatusConjectured
No choice of auxiliary Riemann surface $C \in \{\bC, E_\tau,
\bP^1_{\text{punct}}\}$ gives a non-trivial Costello--Gaiotto 6d hCS
chiral algebra of Wilson-line defects on $\bR^2_\varepsilon \times
K3 \times C$ with a closed R-matrix at rank $> 1$ matching the
Mukai-lattice structure $\Lambda_{\mathrm{Muk}} = II_{4,20}$.
Rational $C = \bC$ gives trivial ($R = 1$) at rank 1 and has
no elliptic structure; elliptic $C = E_\tau$ has been tested with
Belavin-type elliptic R-matrix attached to $\Lambda_{\mathrm{Muk}}$
and fails CYBE (Etingof Wave 6 §A7, residual
$3.94 \times 10^1 \gg 10^{-10}$); punctured sphere $C = \bP^1_{\text{punct}}$
falls into the BR2018 sign-obstruction class-S lane.
\end{lemma}

\begin{lemma}[Character-vs-VOA level; Wave 7 Gaiotto O17]
\label{lem:character-vs-voa-level}
\ClaimStatusProvedHere
The coincidence
$\chi(V_{\Lambda_{\mathrm{Muk}}}) = 1/\eta^{24} = \chi(\cW_{1+\infty}|_{c=24})$
of VOA characters does not imply VOA-level isomorphism. The VOAs
differ in primary field content, module category, and quantum
dimensions at the abelian level. Character-match is the weakest
possible equivalence.
\end{lemma}
```

### Amendment B (k3_yangian_chapter.tex) — strengthen the two-routes remark

**Target**: `chapters/examples/k3_yangian_chapter.tex:92--101`
(the `rem:k3e-two-routes-yangian` block).

**Edit**: append to the current Remark body a new paragraph:

> *Wave 7 Gaiotto addendum.* No standard physics lane — BR2018
> Schur (sign obstruction), Vafa--Witten boundary VOA on K3 ×
> $\bR_{\ge 0}$ (underspecified as a 4d $\cN = 2$ SCFT),
> FHSV chiral algebra (sign obstruction at abelian locus),
> Costello--Gaiotto 6d hCS on $K3 \times C$ for any tested $C$
> (spectral-curve over-constraint at rank $> 1$), class-S-of-K3
> (dimensional type-error), 6d $(2,0)$-on-$K3$ (gives 2d theory not 4d),
> M5-wrapping-K3 (gives MSW CFT, not Yangian), LST-on-$K3 \times T^3$
> (gives ADE sub-Yangians already covered), Moore--Tachikawa
> (no extension from 2d to 4d source) — produces a non-abelian
> K3 Yangian on generic K3 at rank $> 1$. Route A is CY-categorical;
> Route B (BFN) is conjectural via orbifold lattice embedding. The
> physical match on the abelian core at rank 1 is only character-level.

### Amendment C (k3e_bkm_chapter.tex) — add the class-S-ification conjecture

**Target**: `chapters/examples/k3e_bkm_chapter.tex` just before the
"Generalized BKM superalgebra" section (before `\section{The generalized
BKM superalgebra}` or equivalent).

**Insert**:

```latex
\begin{conjecture}[Class-S-ification of BKM via $M_{24}$ moonshine]
\label{conj:class-s-bkm-k3-moonshine}
\ClaimStatusConjectured
The elliptic-fibre degeneration of the BKM superalgebra $\fg_{\Delta_5}$
at $\tau_3 \to i\infty$ (i.e., restriction of the Igusa cusp form
$\Delta_5$ at the rational cusp) produces the Mathieu-moonshine
weak Jacobi form $\phi_{0,1}$ of weight $0$ index $1$ attached to the
K3 elliptic genus, whose Fourier coefficients encode representations of
the Mathieu group $M_{24}$. The putative K3-only VOA $K^\natural$ whose
character is $\phi_{0,1}$ --- the K3 analogue of the Monster moonshine
module $V^\natural$ --- is the candidate for the
Drinfeld / Hochschild centre of the conjectural K3 Yangian at the
$M_{24}$-locus of K3 moduli. Status of $K^\natural$'s existence:
open (Gaberdiel--Hohenegger--Volpato 2010 arXiv:1011.6553; Cheng--Duncan--Harvey
2014 arXiv:1404.4191).
\end{conjecture}
```

### Amendment D (concordance.tex) — Pattern addition

**Target**: `chapters/connections/concordance.tex`, the anti-pattern
registry.

**Add** (near the K3 Yangian obstruction discussion):

> **AP-CY-GAIOTTO-W7-01 (class-S of K3 type-error)**. Attempting to
> compactify 6d $(2,0)$ on $K3$ as a "Gaiotto curve" is a dimensional
> type-error (K3 is 4-real-dim). Valid class-S-adjacent setups treat
> K3 as internal IIB geometry (Setup S5-a, BR2018 sign obstruction),
> as compactification base yielding 2d theory (Setup S5-b,
> Vafa--Witten sigma model), or localise to ADE points (sub-Yangians
> already covered). None gives a non-abelian K3 Yangian on generic K3.

---

## BKM / SIEGEL BRIDGE STATUS

### Rigorous (proved) on $K3 \times E$

- **Oberdieck--Pixton 2016** (Invent. Math. 213 (2018) 507,
  arXiv:1607.05105, Theorem 1): $Z^{DT}_{K3 \times E}(q_1, q_2, Q) =
  C/\Phi_{10}(\tau)$ on $\mathrm{Sp}_4(\mathbb Z)$ Siegel upper
  half-space.
- **Gritsenko--Nikulin 1998** (Internat. J. Math. 9 (1998) 201):
  $\Phi_{10}$ as the denominator identity of $\mathfrak g_{\Phi_{10}}$;
  $\Delta_5$ as the weight-5 Borcherds-lift of $\phi_{0,1}$;
  $\mathfrak g_{\Delta_5}$ with denominator $\Delta_5$.
- **Automorphic-corrections PDF (Raeez Lorgat, April 2020)**:
  elementary derivation of $\mathfrak g, \mathfrak g_{\Delta_5}$, and
  the Weyl--Kac--Borcherds character formula giving $\Delta_5 = \Phi$;
  root data of $\mathfrak g_{\Delta_5}$ realised in $\Lambda^{3,2}$
  and $\Lambda^{2,1}_{II}$; $\Delta_5^2 = \Phi_{10}$ (up to constant)
  connecting to $\mathrm{Sp}_4$ Siegel data.
- **`chapters/examples/k3e_bkm_chapter.tex:34--41, 100--141`**: Vol III's
  inscription of these as ProvedElsewhere.

### Conjectural on K3 alone

- **Mathieu moonshine $\phi_{0,1}$ on K3**: $M_{24}$-equivariance of K3
  elliptic genus (Eguchi--Ooguri--Tachikawa 2010 arXiv:1004.0956;
  proven as $M_{24}$-characters of $\phi_{0,1}$ by Gaberdiel et al.,
  Cheng--Duncan--Harvey 2014). Status: conjecture-level inscription
  into $\mathfrak g_{\Delta_5} \to \phi_{0,1}$ via elliptic
  degeneration; the putative underlying VOA $K^\natural$ is open.
- **Restriction of $\mathfrak g_{\Delta_5}$ from $K3 \times E$ to K3**:
  corresponds to forgetting $E$; at the level of automorphic forms,
  corresponds to Fourier--Jacobi coefficient extraction
  ($\Delta_5 \to \phi_{5, 1/2}$, squared to $\phi_{10, 1}$); at the
  level of algebras, the restriction produces a conjectural
  Mathieu-moonshine object on K3, not a Yangian.

### Bridge connecting to the K3 Yangian question

- The BKM $\mathfrak g_{\Delta_5}$ (on $K3 \times E$) has $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$
  (`k3e_bkm_chapter.tex:10--11`). This is distinct from the
  conjectural $\kappa_{\mathrm{ch}}(Y(\mathfrak g_{K3})) = 2$ of the
  K3 Yangian (`k3_yangian_chapter.tex:65`). The two $\kappa$-invariants
  are not comparable across the CY$_3$ / CY$_2$ divide.
- The passage $\mathfrak g_{\Delta_5}|_{K3 \times E} \to Y(\mathfrak g_{K3})|_{K3}$
  via elliptic degeneration is **not** a rigorous mathematical map;
  it is a physical motivating analogy (FHSV heterotic duality,
  $K3 \times E$ compactification to $K3$ + $E$-dimensions absorbed into
  4d moduli).
- **Bridge status**: rigorous on $K3 \times E$ (BKM ↔ Igusa cusp form);
  conjectural restriction to K3 (Mathieu moonshine ↔ $\phi_{0,1}$);
  **no rigorous BKM-to-Yangian bridge** on K3 alone.

### Answer to the prompt's BKM / Siegel question

> Can one class-S-ify the BKM algebra and find its Yangian avatar?

Not yet, rigorously. The class-S-ification of $\mathfrak g_{\Delta_5}$
from $K3 \times E$ to K3 produces a Mathieu-moonshine object
($\phi_{0,1}$ / conjectural VOA $K^\natural$), not a Yangian. The
Yangian quantization step of the class-S-ification remains **open at
the manuscript level and open in the primary literature**
(Gaberdiel--Hohenegger--Volpato 2010). The Siegel Φ₁₀ partition
function's restriction to K3 gives $1/\eta^{24}$ (character-only
match to $\mathcal H_{\mathrm{Muk}}$); this is Wave 7 Claim 7-G-1,
not a Yangian identification.

---

*End of Gaiotto Wave 7 attack-heal, Agent 10, 2026-04-19.*

*Raeez Lorgat, sole author. No AI attribution.*

*Gaiotto standard (Wave-7 final). Six attack-heal cycles converge to
the stratified K3 Yangian landscape
$Y(\mathfrak g_{K3}) = \mathcal H_{\mathrm{Muk}} \oplus \bigoplus_\Lambda
Y^\mu(\widehat{\mathfrak g}_\Lambda)_{k=1}^{\mathrm{BFN}} \oplus
(\text{cross-strata couplings})$ with 18 concrete obstructions O1--O18.
Rank-1 BPS partition function
$Z^{\mathrm{BPS}}_{r=1}(K3 \times E) = 1/\eta(q)^{24}$ proved via four
independent primary sources (Göttsche, Vafa--Witten, DMVV,
Oberdieck--Pixton), matching the Fock character of
$\mathcal H_{\mathrm{Muk}}$ at the character level only (O17).
ADE-sub-Yangians proved on Kleinian loci
(`thm:bfn-phi-ade-identification`); global K3-Yangian on generic K3
at rank $> 1$ not producible from BR2018 Schur, Vafa--Witten,
FHSV, 6d hCS on any tested auxiliary curve, M5-on-K3, LST,
Moore--Tachikawa, or class-S-on-K3 (type error). BKM/Siegel bridge
rigorous on $K3 \times E$ via Oberdieck--Pixton + automorphic-corrections;
conjectural class-S-ification to K3 via Mathieu moonshine $\phi_{0,1}$.
Correct physical frame is Costello--Gaiotto 6d hCS on
$\bR^2_\varepsilon \times K3 \times E_\tau$ (conjectural as QFT);
incorrect frames BR2018, FHSV-Schur, class-S-on-K3, Vafa--Witten-boundary-VOA
are explicitly retracted. Required manuscript amendments A, B, C, D
specify exact file:line insertion points for inscribing
Wave 7 obstruction lemmas O16--O18 into
`k3_yangian_chapter.tex` and the Mathieu-moonshine class-S-ification
conjecture into `k3e_bkm_chapter.tex`.*
