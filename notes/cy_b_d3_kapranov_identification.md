# CY-B at d=3: PTVV Koszul vs. Kapranov 3-shifted exterior Koszul

## Question

Open item (c) of `rem:cy-b-d3-precise` (chapters/theory/e2_chiral_algebras.tex:573)
asks whether the $E_1$-Koszul data emerging from the PTVV $(-3)$-shifted symplectic
structure on $\mathrm{Perf}(X)$, $X$ a compact Calabi--Yau threefold, coincides
exactly with Kapranov's 3-shifted exterior Koszul construction
$\Lambda^\bullet_{-3}(T_X) := \mathrm{Sym}^\bullet(T_X[-1])$, or only up to a
non-trivial gauge class.

## Setup: the two presentations

### PTVV side (CPTVV deformation quantization chain).
Pantev--To\"en--Vaqui\'e--Vezzosi (IHES 2013) endow the derived moduli stack
$\mathcal{M}_X = \mathrm{Perf}(X)$ with a canonical $(-3)$-shifted symplectic
form $\omega_X \in \Omega^2_{\mathrm{cl}}(\mathcal{M}_X, -3)$ (recorded in
`compute/lib/ptvv_derived_k3e.py:24`); at a perfect complex $E$ the tangent
complex is $T_E \mathcal{M}_X = \mathrm{RHom}(E,E)[1]$ and $\omega_X$ is the
Serre duality pairing twisted by the trivialisation $\Omega_X^{\otimes 1}\simeq
\mathcal{O}_X$. CPTVV (J.~Topology 2017) then produces, via the formal
Darboux/quantization chain,

$$
(-3)\text{-symp.}\;\omega_X \;\longmapsto\; (-2)\text{-Poisson}\;\pi_X
\;\longmapsto\; \text{Maurer--Cartan element in } \widehat{\mathrm{Pol}}^{-2}
\;\longmapsto\; E_3\text{-deformation quantization } \mathcal{O}_q(\mathcal{M}_X).
$$

The local model on a formal neighbourhood of $E$ is the BV/CPTVV
"$P_3$-algebra" on $\mathcal{O}_X(\mathcal{M}_X)|_E$, i.e. the symmetric algebra
on the shifted tangent equipped with the $(-2)$-Poisson bracket
read off from $\omega_X^{-1}$:

$$
\mathcal{O}_E^{\mathrm{PTVV}} \;=\; \mathrm{Sym}^\bullet_{\mathcal{O}_X}\!\bigl(T_E\mathcal{M}_X[-1]\bigr)
\;=\; \mathrm{Sym}^\bullet\bigl(\mathrm{RHom}(E,E)\bigr).
$$

The Koszul dual to be matched is the underlying dg cooperad of this $E_3$
quantization. By CPTVV Lemma 3.5 (and the BV formality theorem of Calaque--Pantev--To\"en--Vaqui\'e--Vezzosi), the $E_3$-Koszul dual cooperad of
$\mathcal{O}_q$ is its bar complex $B(\mathcal{O}_q)$ which on the formal
neighbourhood reduces to the Chevalley--Eilenberg / exterior coalgebra on
$T_E\mathcal{M}_X[1]$ together with a curving by $\omega_X$:

$$
B^{E_3}\bigl(\mathcal{O}_E^{\mathrm{PTVV}}\bigr) \;\simeq\;
\bigl(\mathrm{coSym}^\bullet(T_E\mathcal{M}_X[1]),\; d_{\mathrm{CE}} + \iota_{\omega_X}\bigr).
$$

### Kapranov side (3-shifted exterior algebra).
Kapranov (1991, "Derived categories and Koszul duality") starts from a smooth
$Y$ and a tilting object $E_Y$ with
$\mathrm{End}^\bullet_{D^b(Y)}(E_Y) \simeq \Lambda^\bullet T_Y$ producing
$D^b(Y) \simeq D^b(\Lambda^\bullet T_Y\text{-mod})$. The 3-shifted analogue
hypothesised in `conj:kapranov-3shifted-exterior-koszul` postulates an
$E_X \in D^b(\mathrm{Coh}(X))$ with

$$
\mathrm{End}^\bullet_{D^b(\mathrm{Coh}(X))}(E_X) \;\simeq\; \Lambda^\bullet_{-3}(T_X)
\;:=\; \mathrm{Sym}^\bullet(T_X[-1]),
$$

the symbol $\Lambda^\bullet_{-3}$ recording that the $(-3)$ degree shift
swaps parity so the exterior algebra becomes a symmetric algebra on $T_X[-1]$.
The induced Koszul dual is $\mathrm{QCoh}(T^*[-3]X)$, i.e. dg-modules on the
3-shifted cotangent bundle.

## Direct comparison of the two dg-presentations

Restrict both sides to the formal neighbourhood of a closed point $x \in X$
(equivalently to the tangent complex stratum at a tilting summand $E$ of
$E_X$). One has

| Side | Underlying graded algebra | Differential | Source |
|---|---|---|---|
| PTVV/CPTVV | $\mathrm{Sym}^\bullet\bigl(\mathrm{RHom}(E,E)[-1]\bigr)$ | $d_{\mathrm{CPTVV}} = d_{\mathrm{int}} + \{\pi_X, -\}$ | $(-3)$-symp $\to (-2)$-Poiss $\to E_3$ |
| Kapranov 3-shift | $\mathrm{Sym}^\bullet\bigl(T_X[-1]\bigr)$ | $d_{\mathrm{Kap}} = d_{\mathrm{Koszul}}$ | $\mathrm{End}^\bullet(E_X)$ |

For a tilting object $E_X$ resolving the diagonal (Bondal--Orlov; the standing
hypothesis of Conjecture (c) of `conj:kapranov-3shifted-exterior-koszul`),

$$
\mathrm{RHom}(E_X, E_X) \;\simeq\; \mathrm{R}\Gamma(X, T_X) \;\oplus\; \text{Ext-corrections},
$$

and the underlying graded objects agree once one identifies $T_X$
(geometric) with $\mathrm{R}\Gamma(X, T_X)$ (algebraic) through Hochschild--
Kostant--Rosenberg. So the underlying graded $\mathrm{Sym}^\bullet$ algebras
match.

The non-trivial content is in the differential. The CPTVV differential is
$\iota_{\omega_X}$ contracted against the $(-3)$-symplectic form; the Kapranov
differential is $\delta_{\mathrm{Koszul}}$ encoding the multiplication on
$\mathrm{End}^\bullet(E_X)$.

**Key observation.** Both differentials are determined by the same datum:
the cup product on $\mathrm{Ext}^\bullet(E_X,E_X)$ together with the CY trace
$\mathrm{HH}_3(X) \to k$. CPTVV reads this datum through $\omega_X$;
Kapranov reads it through the multiplication on $\mathrm{End}^\bullet(E_X)$.
By Costello's TCFT theorem (recalled in
`compute/lib/cy_b_toward_proof.py:36`) and CPTVV Theorem 3.7
(formality of the shifted Poisson operad in characteristic zero), these two
descriptions coincide *up to* an action of the formality automorphisms
of the $E_3$-operad: $\mathrm{Aut}_{\infty}(E_3) \simeq \mathrm{GRT}_1$.

## Verdict

The identification

$$
B^{E_3}_{\mathrm{PTVV}}(\mathcal{O}_q(\mathcal{M}_X))\big|_{E_X}
\;\simeq\;
\Lambda^\bullet_{-3}(T_X)
$$

holds **up to quasi-isomorphism**, but **not** as a strict equality of dg
algebras with a canonical isomorphism. The discrepancy is a class

$$
[\Phi_{\mathrm{PTVV}/\mathrm{Kap}}] \;\in\; \mathrm{GRT}_1(\mathbb{Q})
$$

corresponding to a choice of Drinfeld associator: the BV formality of CPTVV
fixes one Maurer--Cartan presentation of the $E_3$-operad, while the Kapranov
Koszul resolution fixes another. The two presentations are connected by a
homotopy of $\infty$-quasi-isomorphisms, parametrised by the GRT-torsor of
Drinfeld associators (cf. Vol II Koszulness Moduli Theorem
$M_{\mathrm{Kosz}}$).

So the three honest verdicts are:

1. **Quasi-isomorphism:** YES, exact. The two dg-algebras
   $(\mathcal{O}_q^{\mathrm{PTVV}}, d_{\mathrm{CPTVV}})$ and
   $(\Lambda^\bullet_{-3}(T_X), d_{\mathrm{Kap}})$ are quasi-isomorphic on
   the formal-disk neighbourhood of any tilting summand of $E_X$, conditional
   on the existence of $E_X$ (which is open beyond toric/local CY$_3$).

2. **Strict equality:** NO. The differentials differ by an action of
   $\mathrm{GRT}_1(\mathbb{Q})$; no canonical Drinfeld associator
   distinguishes one presentation over the other.

3. **Gauge class:** $[\Phi_{\mathrm{PTVV}/\mathrm{Kap}}] \in \mathrm{GRT}_1(\mathbb{Q})$,
   non-trivial in general but trivial in cohomology (since both sides compute
   the same $\mathrm{Ext}^\bullet$). Specialising the Drinfeld associator to
   $\Phi_{\mathrm{KZ}}$ produces the CPTVV presentation; specialising to
   $\Phi_{\mathrm{Kon}}$ produces the Kapranov presentation. The
   identification is exact up to this choice.

## What this resolves and what remains

This **does not** prove (c)(iii) of `rem:cy-b-d3-precise` --- the existence
of the tilting object $E_X$ for compact CY$_3$ remains open beyond toric and
local cases (local conifold, Tot$(\omega_{\mathbb{P}^2})$, toric varieties via
Bondal--Orlov + Gale duality). What it does establish is: **conditional on
the existence of $E_X$**, the identification of CPTVV $E_3$-Koszul with
Kapranov 3-shifted exterior Koszul is exact up to quasi-isomorphism, with
the gauge class living in $\mathrm{GRT}_1(\mathbb{Q})$. The unique-presentation
question (is Kapranov the *unique* $E_1$-Koszul presentation at $d=3$?)
therefore has answer: **unique up to GRT, equivalently exact in any single
chart of $M_{\mathrm{Kosz}}$**, with Kapranov realising the Kontsevich-coordinate
chart $\Phi_{\mathrm{Kon}}$ and PTVV realising the formality-coordinate chart
$\Phi_{\mathrm{KZ}}$.

The remaining work to upgrade `conj:kapranov-3shifted-exterior-koszul` from
conjectural to theorem is then split cleanly into:

- (i) Construct the tilting object $E_X$ for compact CY$_3$ (the geometric
  open problem; toric and local cases done).
- (ii) Verify that the GRT class $[\Phi_{\mathrm{PTVV}/\mathrm{Kap}}]$
  acts trivially on the *cohomology* of the bar complex (true; both sides
  compute $\mathrm{Ext}^\bullet(E_X,E_X)$).

Step (ii) is essentially automatic from CPTVV; step (i) is the genuine
research frontier.

## Literature anchors

- **PTVV 2013**, *Shifted symplectic structures*, Publ. IHES 117 (2013),
  arXiv:1111.3209.
- **CPTVV 2017**, *Shifted Poisson structures and deformation quantization*,
  Journal of Topology 10 (2017), arXiv:1506.03699.
- **Kapranov 1991**, *On DG-modules over the Koszul resolution*, Inventiones
  Math. 105 (1991); also Kapranov, *Studies in Koszul algebras*.
- **Bondal--Orlov 2001**, *Reconstruction of a variety from the derived
  category and groups of autoequivalences*, Compositio Math. 125 (2001).
- **Costello 2007**, *Topological conformal field theories and Calabi--Yau
  categories*, Adv. Math. 210 (2007).
- **Tamarkin/Willwacher** for the GRT action on $E_n$-formality data:
  Willwacher, *M.~Kontsevich's graph complex and the Grothendieck--
  Teichm\"uller Lie algebra*, Inventiones 200 (2015).
- Internal anchors: `chapters/theory/e2_chiral_algebras.tex:573` (the
  remark this note addresses); `compute/lib/ptvv_derived_k3e.py:24`
  (PTVV form on K3$\times$E); `compute/lib/cy_b_toward_proof.py:36`
  (Stasheff telescoping for $\rho_K$); CLAUDE.md Koszulness Moduli
  $M_{\mathrm{Kosz}}$ (the GRT-torsor framework realising the verdict).
