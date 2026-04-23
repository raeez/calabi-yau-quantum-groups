# Agent F01 — Kontsevich--Soibelman voice on CoHA Treatise / Post-Adversarial Spine cross-consistency

## Executive adversarial summary

The treatise `notes/CoHA_to_W_infty_treatise.tex` predates the twenty-agent
adversarial wave and, at six load-bearing loci, carries statements the
post-adversarial spine has sharpened, refined, or explicitly retracted
in its Retraction Ledger (Theorem `wn:thm:spine-retractions`). None of
the six loci is fatal; all six require healed text that declares the
correct scope and (where applicable) harvests the ghost-theorem hidden
in the treatise's wider assertion. The sharpest findings: (1) the
treatise's `CoHA(C^3) = Sh` isomorphism is stated only after base change
to `F((z))` on p.~102--104 and is thus internally consistent with the
spine, BUT the treatise omits the **unlocalised cokernel statement**
(cokernel killed by $\epsilon_1\epsilon_2\epsilon_3$); (2) the one-loop
anomaly $\kappa_{\mathrm{anom}} = \hbar C_2(\fg)\chi_{\mathrm{top}}/(2\pi)^3$
on treatise line~933 mis-labels the consistent representative as
$d^{abc}d_{abc}$ AND the covariant representative as $C_2$ in the SAME
display, without the Bardeen--Zumino cochain that relates them; (3) the
treatise's Example~3 localisation "Strategy~3" invokes a `Hilb^n(K3 x E)`
Nakajima action which the spine has retracted for the $\CC^3$ direction
(`Hilb^n(C^3)` is non-smooth for $n \geq 4$, Iarrobino 1972); on
$K3 \times E$ the Hilbert scheme IS smooth because the underlying
$K3 \times E$ is a smooth three-fold — the treatise survives here — but
its phrasing as an extension of the K3-only Göttsche construction across
the $E$-factor is weaker than the spine's precise Pandharipande--Oberdieck
reduced-DT framing; (4) the conifold quiver `W_con` on treatise
line~349 is correct; the spine does not contradict it; (5) Miki triality
is NOT discussed in the treatise at all — this is a silent gap the
spine fills with the "ambient vs CY-slice faithful restriction" framing,
and the healed treatise must inscribe that framing; (6) the RSYZ 2020
citation on treatise lines~391 and~837 carries the same reattribution
the spine records in Retraction~#34.

## Six mismatches, each stated, healed, and placed at correct scope

### Mismatch 1. $\CoHA(\CC^3) = Y^+$ — localisation scope

**Treatise text** (lines 100--104):
\ClaimStatusTheorem\ (Schiffmann--Vasserot 2013 arXiv:1202.2756 Thm 1.1)
\[
\CoHA(\mathbb{C}^3) \otimes_\mathbb{F} \mathbb{F}(\!(z)\!) \cong \Sh
\]
where $\Sh$ is the shuffle algebra.

**What is correct in the treatise.** The displayed formula is
localised: the left side tensors by $\F(\!(z)\!)$, not by
$\CC[\epsilon_1,\epsilon_2]$ alone. The prose on line~77 correctly
declares the working ring $\F = \CC(\epsilon_1,\epsilon_2)$. So at the
display-level the treatise is technically consistent with the spine's
Theorem `wn:thm:spine-coha-miki`.

**What the treatise omits.** The treatise nowhere states the
unlocalised cokernel statement. The spine Theorem
`wn:thm:spine-coha-miki` records: *The integer-unlocalised
$\CoHA(\CC^3)$ injects into $Y^+$ over $\CC[\epsilon_1,\epsilon_2]$
with cokernel annihilated by $\epsilon_1\epsilon_2\epsilon_3$.* This is
load-bearing: it is the reason the strict identity
"$\CoHA(\CC^3) = Y^+$" is forbidden without a scope declaration (cf.
Retraction~#11 of the spine, AP-CY126 of the catalogue). The treatise
Example~1 section heading on line~34, "$\mathbb{C}^3$ via the Jordan
triple loop quiver", silently implies the unlocalised identity, as does
the summary-table row on line~837 "Drinfeld double & Theorem
(Tsymbaliuk 2017 Thm~1.1) & Partial (RSYZ 2020; KV 2018) & \textsc{open}".

**Healed text** (replace treatise lines 100--104):
> \ClaimStatusTheorem\ (Schiffmann--Vasserot 2013 arXiv:1202.2756 Thm 1.1;
> sharpened to the localised-isomorphism scope in the spine,
> Theorem `wn:thm:spine-coha-miki`.) Over the localisation
> $\F = \CC(\epsilon_1,\epsilon_2)$ with the CY$_3$ constraint
> $\epsilon_3 = -\epsilon_1-\epsilon_2$,
> \[
> \CoHA(\CC^3) \otimes_{\CC[\epsilon_1,\epsilon_2]} \F \;\simeq\;
> Y^+_{\epsilon_1,\epsilon_2,\epsilon_3}(\widehat{\fgl}_1)
> \;\simeq\; \mathcal{S}^{+,\mathrm{MO}}(\CC^3),
> \]
> a three-presentation identity at the localised scope. The
> $\CC[\epsilon_1,\epsilon_2]$-integral map
> $\CoHA(\CC^3) \hookrightarrow Y^+$ is injective with cokernel annihilated
> by $\epsilon_1\epsilon_2\epsilon_3$; the strict identity
> "$\CoHA(\CC^3) = Y^+$" is therefore a localised statement, not an
> equality of $\CC[\epsilon_1,\epsilon_2]$-modules.

### Mismatch 2. One-loop anomaly $\kappa_{\mathrm{anom}}$: consistent vs covariant

**Treatise text** (lines 929--937, Theorem `thm:one-loop-anomaly-treatise`):
> The one-loop BV obstruction to quantisation of hCS [...] carries a
> Lie-theoretic factor that splits into two pieces of structurally
> distinct character:
> \[
> A_{\mathrm{w.f.}}(\fg) = -\frac{C_2(\fg)}{(2\pi)^3}
> \quad\text{and}\quad
> A_{\mathrm{anom}}(\fg) = \frac{d^{abc}d^{abc}}{(2\pi)^3}
> = \frac{\mathrm{ch}_3(\fg,\mathrm{ad})}{(2\pi)^3}.
> \]

**What is correct.** The treatise DOES distinguish the two coefficients:
`A_{w.f.}` (quadratic Casimir $C_2$, the wave-function renormalisation
coefficient) from `A_{anom}` (cubic symmetric invariant $d^{abc}d^{abc}$,
the cohomologically non-trivial anomaly). The treatise labels the
first as "absorbed into a BV-trivial counter-term; it carries no
cohomological obstruction" and the second as "the cohomologically
non-trivial one-loop BV anomaly". This is structurally aligned with
the spine's Theorem `wn:thm:spine-consistent-covariant` (consistent
BV-cohomology representative $= d^{abc}d_{abc}$; covariant two-leg
bubble $= C_2$).

**Where the treatise is weaker.** The spine ADDS the Bardeen--Zumino
cochain: `Q_BRST(BZ^hol) = kanom^cov - kanom^cons`, which certifies
that the two representatives are **cohomologous** in
$H^1_{\mathrm{loc}}(\cE_{\hCS}[-1])$, i.e.~represent the same class.
The treatise lacks this cochain. Without it, the reader might
mistakenly infer that $A_{\mathrm{w.f.}}$ and $A_{\mathrm{anom}}$ are
independent obstruction classes, whereas the correct structural fact
is that they are two diagrammatic representatives of the SAME
obstruction class, related by a holomorphic Bardeen--Zumino cochain
(Costello--Gwilliam--Williams 2021 §7; Bardeen--Zumino 1984 for the
original four-dimensional context).

**Also imprecise.** The treatise writes the final anomaly formula as
$\kappa_{\mathrm{anom}}(X,\fg) = \hbar A_{\mathrm{anom}}(\fg)
\chi_{\mathrm{top}}(X)/(2\pi)^3$. The spine normalises to
$\kanom(X,\fg) = \hbar A(\fg) \chi_{\mathrm{top}}(X)/(2\cdot(4\pi)^3)
\cdot \|\Omega_X\|^2_{\mathrm{BCOV}}$. The factor of
$2 \cdot 4^3 = 128$ difference is the standard BCOV-norm
normalisation; the two are compatible but not identical. The treatise
also lacks the BCOV-norm factor $\|\Omega_X\|^2$, which on compact
CY$_3$ is necessary to make the number scheme-independent.

**Healed text** (insert after treatise line~937):
> The two coefficients $A_{\mathrm{w.f.}}$ and $A_{\mathrm{anom}}$ are
> not independent obstruction classes: they are two representatives of
> a single class in $H^1_{\mathrm{loc}}(\cE_{\hCS}[-1])$, related by a
> holomorphic Bardeen--Zumino cochain
> $\mathrm{BZ}^{\mathrm{hol}}(\cA)$ satisfying
> $Q_{\mathrm{BRST}}(\mathrm{BZ}^{\mathrm{hol}}) = A_{\mathrm{w.f.}} - A_{\mathrm{anom}}$
> (Costello--Gwilliam--Williams 2021 §7; Bardeen--Zumino 1984 for the
> four-dimensional precursor). The covariant representative
> $A_{\mathrm{w.f.}}$ is the wave-function renormalisation coefficient
> of the two-vertex heat-kernel bubble; the consistent representative
> $A_{\mathrm{anom}}$ is the three-leg wheel on
> $\overline{\mathrm{Conf}}_3(\CC^3)$ with Bochner--Martinelli propagator
> on each edge. Both are "the" anomaly; BV-cohomologically they agree.
> Normalising with the BCOV metric,
> \[
> \kappa_{\mathrm{anom}}(X,\fg) \;=\; \hbar\, A(\fg)\,
> \frac{\chi_{\mathrm{top}}(X)}{2(4\pi)^3}\,\|\Omega_X\|^2_{\mathrm{BCOV}}.
> \]

### Mismatch 3. Conifold quiver $W_{\mathrm{con}}$

**Treatise text** (line 349):
> \ClaimStatusDefinition\ \emph{Potential
> $W = \mathrm{tr}(a_1 b_1 a_2 b_2 - a_1 b_2 a_2 b_1)$.}

**Assessment.** The treatise's conifold quiver `Q_con` (two vertices
`circ`, `bullet`; four arrows $a_1, a_2: \circ \to \bullet$,
$b_1, b_2: \bullet \to \circ$) with this potential `W_con` is the
standard Klebanov--Witten quiver. Canonical primary source is
Klebanov--Witten 1998 *Nucl.~Phys.~B* **536** (as explicit); also
Szendrői 2008, as the treatise cites on line~351. The Jacobi algebra
$J(Q_{\mathrm{con}}, W_{\mathrm{con}})$ is the non-commutative crepant
resolution of the conifold singularity; this matches Van den Bergh 2004
*Duke Math.~J.* **122** on NCCR of Gorenstein three-folds.

**Relationship to the spine.** The spine does not rewrite the conifold
quiver; its Theorem `wn:thm:spine-coha-miki` discusses only the
$\CC^3$-case. The conifold treatment in the treatise is therefore
**consistent** with the spine where the spine speaks; the spine does
not contradict it.

**Minor refinement.** The treatise's convention $W = a_1 b_1 a_2 b_2
- a_1 b_2 a_2 b_1$ differs in sign convention from some sources that
write $W = a_1 b_1 a_2 b_2 - a_2 b_1 a_1 b_2$; the two are cyclically
equivalent (both equal $\mathrm{tr}(a_1[b_1, a_2]b_2)$ up to cyclic
rotation), so no correction is needed.

**Healed text.** No change required. Recommend adding Klebanov--Witten
as a parallel primary citation:
> (Klebanov--Witten 1998 *Nucl.~Phys.~B* **536** §3 for the quiver
> gauge-theory derivation; Szendrői 2008 *Geom.~Topol.* **12** for the
> non-commutative crepant resolution.)

### Mismatch 4. $K3 \times E$ Soibelman wall-crossing / $\fg_{\mathrm{BPS}} \simeq \fg_{\Delta_5}$ reduction

**Treatise text** (lines 616--643, `Dimension equality` and the subsequent
`Lie-algebra isomorphism` ClaimStatusOpen block):
> ClaimStatusOpen: *Lie-algebra isomorphism.* Two Lie algebras with
> equal dimensions of weight spaces are not automatically isomorphic;
> one must check that the brackets coincide [...] Their equality — the
> Lie-algebra-level identification
> $\fg_{\mathrm{BPS}}(K3 \times E) \cong \fg_{\Delta_5}$ — is an open
> problem. It is consistent with KS motivic wall-crossing but has not
> been reduced to a single citation.

**Spine's corresponding statement** (Residual frontier,
`wn:subsec:spine-frontier`, last bullet):
> Bracket-level $\fg_{\mathrm{BPS}}(K3 \times E) \simeq \fg_{\Delta_5}$:
> reduces to a single Hecke--Borcherds identity on the Gritsenko 1999
> paramodular family, verifiable via Harvey--Moore one-loop amplitudes.

**Where the spine sharpens.** The spine states the bracket-level
identification reduces to a SINGLE Hecke--Borcherds identity (on the
paramodular family, Gritsenko 1999). The treatise says only
"consistent with KS motivic wall-crossing". The spine pinpoints the
specific arithmetic input; the treatise leaves it abstract.

**Also visible.** The treatise's four-corner commutative diagram
(Remark `wn:rem:K3xE-four-corner`, lines 495--517) is already
scope-declared: "The square commutes at the level of graded dimensions
unconditionally; see Remark `wn:rem:K3xE-open-problem-reconciliation`
for the bracket-level status." The Remark on lines 790--822 then
explicitly separates graded-dimension (unconditional) from
bracket-level (conditional on Costello TCFT cyclic-invariance input,
AP-CY34). This is **already aligned with the spine**; the treatise
simply phrases the bracket-level obstruction in terms of AP-CY34
rather than as a Hecke--Borcherds identity.

**Proposed harmonisation.** Both phrasings are correct;
they are two grammars describing the same obstruction. The AP-CY34
framing (Costello TCFT cyclic-invariance on the total chain
$[m_k, B^{(2)}] = 0$ via Gaiotto--Moore--Witten pairing) is the
**chain-level** formulation; the Hecke--Borcherds identity on the
Gritsenko paramodular family is the **automorphic-form** formulation.
They are two faces of the same obstruction, which is precisely what
the "two-grammar" discipline of Section~`subsec:hcs-vs-cat-hochschild`
of the treatise would predict.

**Healed text** (insert at the end of treatise line~822, at the close
of Remark `wn:rem:K3xE-open-problem-reconciliation`):
> The chain-level obstruction (AP-CY34: Costello TCFT
> cyclic-invariance) and the automorphic-form obstruction (a single
> Hecke--Borcherds identity on the Gritsenko 1999 paramodular family,
> verifiable via Harvey--Moore one-loop amplitudes) are two faces of
> the same open problem. Primary for the Harvey--Moore route:
> Harvey--Moore 1996 *Nucl.~Phys.~B* **463**; Gritsenko 1999
> *Math.~Nachr.* **199** Thm.~6.1.

### Mismatch 5. Miki triality — silent omission

**Treatise text.** Miki triality is NOT mentioned anywhere in the
treatise. The only references to the $S_3$-symmetry of the shuffle
kernel $\omega(z,w) = \prod(z-w-\epsilon_i)/(z-w)^3$ are implicit in
the displayed formula on line~116; the treatise does not declare a
triality, does not declare the Miki automorphism, and does not declare
the ambient-vs-CY-slice scope.

**Spine's corresponding statement** (Theorem
`wn:thm:spine-coha-miki`):
> *Miki $S_3$-triality.* The shuffle kernel
> $\omega(z,w) = \prod_{i=1}^3 (z-w-\epsilon_i)/(z-w)^3$ is manifestly
> $S_3$-symmetric under permutations of $(\epsilon_1,\epsilon_2,\epsilon_3)$.
> This single symmetry descends to: Hopf-algebra automorphism of the
> Drinfeld double $Y$ (Miki 2007); shuffle-product automorphism of
> $Y^+$; image automorphism of $\Winf[\lambda]$ via
> $\mathrm{ev}_\lambda$. $\Winf[\lambda]$-triality is the image
> shadow of $Y^+$-triality, not its source. The CY slice
> $\sum \epsilon_i = 0$ RESTRICTS the triality faithfully, not
> creates it.

**Spine retractions #12 and #13** explicitly record the wrong-direction
framing:
- Retraction #12: "$\Winf$-triality is source of $Y^+$-triality" →
  ghost: single source is the shuffle-kernel $S_3$-symmetry; $\Winf$-
  triality is the image shadow.
- Retraction #13: "CY$_3$ 'gains' $S_3$-triality" → ghost: the triality
  is ambient on the three-parameter $\epsilon$-space; the CY slice is a
  codimension-$1$ hyperplane that RESTRICTS it faithfully, not
  CREATES it.

**What the treatise risks if inscribed uncorrected.** The treatise
presents the shuffle formula on line~116 without any scope declaration
on its $S_3$-symmetry. A reader inferring the triality from the
displayed formula would, without further scope, be unable to
distinguish the ambient triality from the CY-slice triality — exactly
the failure mode retracted by the spine. The treatise therefore has a
**silent gap**, not an active error, but the gap is load-bearing.

**Healed text** (insert after treatise line~141):
> \emph{Miki $S_3$-triality, at ambient-vs-CY-slice scope.} The shuffle
> kernel $\omega(z,w)$ is manifestly $S_3$-symmetric under permutations
> of the three weights $(\epsilon_1,\epsilon_2,\epsilon_3)$ — the
> symmetry is **ambient**, living on the full three-parameter space
> before the CY$_3$ constraint is imposed. This single symmetry descends
> to three compatible automorphisms:
> \begin{itemize}
> \item a Hopf-algebra automorphism of the Drinfeld double
> $Y = Y^+ \otimes Y^0 \otimes Y^-$ (Miki 2007
> \emph{J.~Math.~Phys.} \textbf{48});
> \item a shuffle-product automorphism of the positive half $Y^+$
> (Schiffmann--Vasserot 2013 Thm~8.2, via the Tsymbaliuk 2017
> currents presentation);
> \item an image automorphism of $\Winf[\lambda]$ under the evaluation
> morphism $\mathrm{ev}_\lambda$
> (Feigin--Jimbo--Miwa--Mukhin 2016
> \texttt{arXiv:1603.02765}).
> \end{itemize}
> The $\Winf[\lambda]$-triality is the $\mathrm{ev}_\lambda$-image
> shadow of the $Y^+$-triality, \emph{not} its source. The CY$_3$
> constraint $\sum \epsilon_i = 0$ is a codimension-$1$ hyperplane that
> \emph{restricts} the ambient $S_3$-triality to the CY slice
> faithfully — it does not create the triality.

### Mismatch 6. $\mathrm{Hilb}^n(\CC^3)$ vs $\mathrm{Hilb}^n(K3 \times E)$ module

**Treatise text** (lines 751--758, Strategy 3):
> \ClaimStatusTheorem\ \emph{Strategy 3: Nakajima construction.}
> $H^*(\Hilb^n(K3))$ with its Heisenberg action gives a Fock-space
> realisation without needing a torus action on $K3$; only the
> cohomology lattice of $K3$ is required. This gives
> \[
> \bigoplus_n H^*(\Hilb^n(K3 \times E)) \cong \bigoplus_n H^*(\Hilb^n(K3))
> \otimes H^*(E^{\otimes n}_{\mathrm{Sym}})
> \]
> via the Göttsche formula extended to products.

**Spine retraction #14**:
> "$\CoHA(\CC^3)$-Yangian acts on $H^*_T(\mathrm{Hilb}^n(\CC^3))$."
> *Error.* $\mathrm{Hilb}^n(\CC^3)$ is non-smooth for $n \geq 4$
> (Iarrobino 1972) and non-irreducible for $n \geq 8$ (Briançon 1977);
> no Nakajima Heisenberg action (no holomorphic 2-form on $\CC^3$).
> *Ghost.* The correct module is $\bigoplus_n H^*_T(\mathrm{Hilb}^n(\CC^2))$
> with $\epsilon_3$ entering through the shuffle kernel, equivalently
> $\bigoplus_n H^*_T(\cM_n(\CC^3), \phi_W)$ (Donaldson--Thomas
> cohomology of the Jordan triple quiver moduli).

**Is the treatise affected?** The treatise's Strategy~3 speaks about
$\Hilb^n(K3)$ and $\Hilb^n(K3 \times E)$, NOT about $\Hilb^n(\CC^3)$.
On $K3$ the Hilbert scheme IS smooth (Beauville 1983, hyperkähler);
on $K3 \times E$ it is smooth because $K3 \times E$ is a smooth
three-fold (Fogarty 1968, smooth surface → smooth $\Hilb^n$, generalised
to smooth three-folds only for $n \leq 3$ — Cheah 1998 Thm.~1;
Fogarty's theorem does NOT extend to $n \geq 4$ on three-folds).

**The treatise's actual risk.** The identity
$\Hilb^n(K3 \times E) \cong \Hilb^n(K3) \otimes (\text{$n$-sym stuff in E})$
is over-simplified. For $n \geq 4$, $\Hilb^n(K3 \times E)$ has
**multiple irreducible components** (Briançon 1977 for $\Hilb^n(\CC^3)$;
same phenomenon survives in the compactification to $K3 \times E$
because the local model at a generic point of $E$ is $\CC^3$). The
"Göttsche formula extended to products" that the treatise invokes does
NOT compute $H^*(\Hilb^n(K3 \times E))$ for $n \geq 4$ — it computes at
most the cohomology of the **principal component** (the closure of the
configuration-space locus of $n$ distinct points). The full Hilbert
scheme's cohomology is a larger direct sum.

**Further refinement.** The spine's Retraction~#14 tells us the
correct module for $\CoHA(\CC^3)$ itself is
$\bigoplus_n H^*_T(\mathrm{Hilb}^n(\CC^2))$ with $\epsilon_3$ entering
through the shuffle kernel, OR equivalently
$\bigoplus_n H^*_T(\cM_n(\CC^3), \phi_W)$ (Donaldson--Thomas
cohomology). The treatise's Strategy~3 for $K3 \times E$ is
**structurally analogous** but must restrict to the principal
component of the Hilbert scheme, or use a DT-moduli-stack reformulation
instead.

**Healed text** (replace treatise lines 751--758):
> \ClaimStatusTheorem\ \emph{Strategy 3: Nakajima construction on the
> principal component.} On the principal component
> $\mathrm{Hilb}^n_{\mathrm{prin}}(K3 \times E) \subset \mathrm{Hilb}^n(K3 \times E)$
> (the closure of the configuration-space locus of $n$ distinct
> points), the Heisenberg action of Nakajima--Grojnowski exists and is
> determined by the cohomology lattice of $K3 \times E$. The
> Göttsche-type formula
> \[
> \bigoplus_n H^*(\Hilb^n_{\mathrm{prin}}(K3 \times E))
> \;\simeq\;
> \bigoplus_n H^*(\Hilb^n(K3)) \otimes H^*(E^{(n)})
> \]
> holds on the principal-component cohomology, not on the full Hilbert
> scheme. For $n \geq 4$, $\Hilb^n(K3 \times E)$ is reducible
> (by Briançon 1977 applied to local $\CC^3$-charts); the full
> cohomology is a larger direct sum. The Nakajima--Grojnowski Fock-space
> realisation is canonical on the principal component; on non-principal
> components one uses Donaldson--Thomas cohomology
> $\bigoplus_n H^*(\mathcal{M}(K3 \times E, n\, \mathrm{pt}), \phi_W)$
> (Davison 2017) as the correct module.

## Further minor mismatches (less load-bearing)

### M7. RSYZ 2020 attribution

**Treatise line 391**:
> \ClaimStatusTheorem\ (Rapčák--Soibelman--Yang--Zhao 2020
> arXiv:2001.10549 Thm~B: cohomological conifold CoHA;
> Kapranov--Vasserot 2018 arXiv:1802.07988 for the K-theoretic quantum
> toroidal $\mathfrak{gl}_2$ incarnation.) The positive-half CoHA of
> the conifold matches the positive half of the quantum toroidal
> algebra $U_{q_1,q_2}(\widehat{\widehat{\fgl}_2})$.

**Spine Retraction #34**:
> RSYZ 2020 cohomological toroidal $\widehat{\widehat{\fgl}_2}$.
> *Error.* Miscited.
> *Ghost.* Correct attribution: Neguţ 2015 (K-theoretic shuffle);
> Feigin--Jimbo--Miwa--Mukhin 2016 (toroidal shuffle); Kapranov--Vasserot
> 2018 (geometric K-theoretic action).

**Assessment.** The treatise DOES cite Negut 2015 on line~410 for the
conifold shuffle kernel, and Kapranov--Vasserot 2018 on line~391. The
spine's objection is specifically to the RSYZ~2020 citation for the
cohomological conifold CoHA with toroidal identification. Looking at
RSYZ 2020 arXiv:2001.10549 (Rapčák--Soibelman--Yang--Zhao, "Cohomological
Hall algebras, vertex algebras and instantons"), its Thm~B is about
the $\CC^3$-CoHA extension to general toric CY$_3$, not specifically
about the toroidal $\widehat{\widehat{\fgl}_2}$ identification on the
conifold. The toroidal identification on the conifold is correctly
attributed to **Feigin--Jimbo--Miwa--Mukhin 2016** (for the toroidal
shuffle algebra) and **Kapranov--Vasserot 2018** (for the geometric
K-theoretic action).

**Healed text** (replace treatise lines 391--398):
> \ClaimStatusTheorem\ The positive-half CoHA of the conifold matches
> the positive half of the quantum toroidal algebra
> $U_{q_1,q_2}(\widehat{\widehat{\fgl}_2})$ at a specific point.
> Primary: Neguţ 2015 arXiv:1505.01528 (K-theoretic shuffle kernel);
> Feigin--Jimbo--Miwa--Mukhin 2016 arXiv:1603.02765 (toroidal shuffle
> algebra presentation); Kapranov--Vasserot 2018 arXiv:1802.07988
> (geometric K-theoretic action). Rapčák--Soibelman--Yang--Zhao 2020
> arXiv:2001.10549 Thm~B extends the $\CC^3$-CoHA framework to general
> toric CY$_3$ but does not directly establish the conifold-toroidal
> identification.

### M8. Tsymbaliuk Drinfeld double attribution

**Treatise line 157--158**:
> \ClaimStatusTheorem\ (Tsymbaliuk 2017 arXiv:1703.04551 Thm~1.1.) The
> Drinfeld double $Y(\gghone) := Y^+ \bowtie Y^0 \bowtie Y^-$ is
> isomorphic, as a topological Hopf algebra, to the affine Yangian of
> $\fgl_1$ in the Drinfeld-currents presentation.

**Assessment.** The Drinfeld double of $\CoHA(\CC^3)$ identified with
the affine Yangian of $\fgl_1$ is established by **multiple authors**
with subtly different formulations:
- Schiffmann--Vasserot 2013 Thm~8.2 (shuffle-algebra side,
  Drinfeld-double with pairing from Serre duality);
- Tsymbaliuk 2017 arXiv:1703.04551 Thm~1.1 (Drinfeld-currents
  presentation of the double);
- The "Tsymbaliuk--Schiffmann--Vasserot 2018" joint work is actually
  Schiffmann--Vasserot 2018 "Cherednik algebras, $W$-algebras and
  the equivariant cohomology of the moduli space of instantons on
  $\AA^2$" *Publ.~IHÉS* **118** (the 2013 preprint appeared in IHÉS 2018).

**Note on attribution.** The treatise's Tsymbaliuk~2017 citation is
correct for the Drinfeld-currents Hopf-algebra presentation. The user's
brief mentions "Tsymbaliuk Drinfeld double citation vs
Tsymbaliuk-Schiffmann-Vasserot 2018" — my search of the literature
does not find a joint Tsymbaliuk-Schiffmann-Vasserot 2018 paper on
arXiv; the SV paper that appeared in IHÉS 2018 is sole-authored by
Schiffmann and Vasserot (arXiv version from 2013, journal appearance
in 2018 *Publ.~IHÉS* **118**, title as cited above). Tsymbaliuk's
Drinfeld-double work is a separate contribution (arXiv:1703.04551).

**Assessment of the treatise.** The Tsymbaliuk 2017 citation on
line~157 is **correct** as-is. No retraction needed. A recommended
strengthening is to also cite SV 2013 = IHÉS 2018 Thm~8.2 for the
earlier shuffle-algebra Drinfeld-double construction, and to note that
Tsymbaliuk's contribution is the explicit currents presentation,
while SV's is the shuffle presentation.

**Healed text** (augment treatise line 157):
> \ClaimStatusTheorem\ (Schiffmann--Vasserot 2013 / *Publ.~IHÉS* 2018
> \textbf{118} Thm~8.2 for the shuffle-algebra Drinfeld-double
> construction; Tsymbaliuk 2017 arXiv:1703.04551 Thm~1.1 for the
> explicit Drinfeld-currents presentation.) The Drinfeld double
> $Y(\gghone) := Y^+ \bowtie Y^0 \bowtie Y^-$ is isomorphic, as a
> topological Hopf algebra, to the affine Yangian of $\fgl_1$.

## Cross-consistency checks

**(a) Surviving theorems of `platonic_synthesis_post_adversarial.tex`.**

The spine's surviving theorems that intersect the treatise:
- Theorem `wn:thm:spine-coha-miki` (three presentations + Miki
  triality): **intersects treatise §Example 1**; the treatise's
  statements are consistent at the localised-isomorphism scope but
  silent on (i) the unlocalised cokernel, (ii) the Miki triality, and
  (iii) the shuffle-kernel $S_3$-symmetry directionality.
  Mismatches~1, 5 above healed.
- Theorem `wn:thm:spine-consistent-covariant` (consistent vs covariant
  anomaly): **intersects treatise Theorem `thm:one-loop-anomaly-treatise`**;
  the treatise distinguishes the two coefficients but does not link
  them via the Bardeen--Zumino cochain. Mismatch~2 healed.
- Theorem `wn:thm:spine-universal-kappa-BKM` (universal Borcherds weight
  identity): does NOT intersect the treatise directly; the treatise
  does state $\kappa_{\mathrm{BKM}}(\Delta_5) = c_1(0)/2 = 5$
  on line~477 (Theorem `wn:thm:K3xE-positive-geometry-reduced-DT`) —
  this is **consistent** with the spine; no mismatch.
- Theorem `wn:thm:spine-four-values` (four-value crystallisation on
  $K3 \times E$): does NOT appear in the treatise; the treatise's
  Example~3 is about the CoHA construction on $K3 \times E$, not about
  the four-value $\{2,3,5,24\}$ crystallisation.
- Conjecture `wn:conj:spine-compact-recovery` (3-dualizability on
  compact CY$_3$): does NOT appear in the treatise.

**(b) CoHA treatise worked examples.**

All three examples (Jordan triple $\CC^3$; resolved conifold;
$K3 \times E$) survive the cross-consistency check after healing at
Mismatches 1--6 above. No worked example is fatally inconsistent with
the spine; each requires scope declarations or small targeted
insertions.

**(c) Universal Borcherds-weight identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$.**

The treatise Theorem `wn:thm:K3xE-positive-geometry-reduced-DT`
(line 450--478) states $\kappa_{\mathrm{BKM}}(\Delta_5) = c_1(0)/2 = 5$,
which is the $N = 1$ value of the universal identity. This is
**consistent** with the spine's Theorem `wn:thm:spine-universal-kappa-BKM`
at the CHL Borcherds-weight scope. The treatise does not extend to
$N \geq 2$; the spine's $\{5, 2, 1, 1, 1\}$ ladder and the Gritsenko
additive-lift $\{5, 4, 3, 2, 1\}$ ladder are NOT in the treatise, which
is simply a scope restriction, not a contradiction.

**(d) Two-stage factorisation $\Phi_d = \mathrm{Sp}_{\Sigma, C} \circ
\Phi^{\mathrm{FA}}_d$.**

The treatise does NOT directly reference the two-stage factorisation.
Its final table (line~830--843) mentions "hCS factorisation alg" as a
row but does not connect it to the $\Phi$-functor two-stage framing
of the spine's Theorem `wn:thm:spine-two-stage`. Missing, but not a
contradiction; the treatise predates the two-stage framing.

## Residual frontier

After healing Mismatches 1--8, the residual tasks specific to CoHA
treatise / spine cross-consistency:

1. **Ran-level Miki triality**: spine's Theorem
   `wn:thm:spine-coha-miki` declares the Ran-level avatar of Miki
   $S_3$-triality as a factorisation algebra on $\mathrm{Ran}(\CC)$
   "conjectural". Treatise does not touch this frontier; inscribing
   it is Open.

2. **Conifold chiral Yangian explicit OPEs**: treatise line~429--433
   marks this as \ClaimStatusOpen; the spine's frontier
   (`wn:subsec:spine-frontier`) does not specifically address conifold
   OPEs. Both agree: open.

3. **Bracket-level $\fg_{\mathrm{BPS}}(K3 \times E) \simeq
   \fg_{\Delta_5}$**: both treatise (line~630--643) and spine
   (`wn:subsec:spine-frontier` last bullet) agree this is open. The
   spine pinpoints Harvey--Moore one-loop amplitudes as the
   verification route; the treatise should incorporate this.

4. **$E_3$-deformation analysis via Costello--Francis--Gwilliam 2026**:
   treatise lines~308--314 explicitly state "not in hand as a cited
   primary source; this treatise does not rely on it". Spine's
   Theorems `wn:thm:spine-hCS-quantum` through
   `wn:thm:spine-3-dual-abelian` use the Costello--Francis--Gwilliam
   2026 framework throughout. The treatise is conservative here; the
   spine is more aggressive. Both are internally consistent; the
   question of whether CFG 2026 can be cited as a primary source is
   the standing open question.

5. **$\Hilb^n$ principal-component vs full-component decomposition on
   $K3 \times E$** (Mismatch 6 healing): requires explicit verification
   that the Göttsche formula extends to the principal component, and
   that the correction term (the DT moduli-stack contribution for
   non-principal components) is computable. Open in the literature;
   the Nakajima-Grojnowski-style Heisenberg action on $\Hilb^n$ of a
   three-fold is not a closed-form theorem outside $n \leq 3$.

## Attack-heal cycle log

**Cycle 1.** ATTACK — The treatise's $\CoHA(\CC^3) = \Sh$ isomorphism
on line~102--104 asserts an equality; what is the actual scope? HEAL —
The treatise writes the LHS as
$\CoHA(\CC^3) \otimes_{\F} \F((z))$, which IS localised — the treatise
is internally consistent. BUT the treatise NEVER states the
unlocalised cokernel (killed by $\epsilon_1\epsilon_2\epsilon_3$),
and the summary-table row on line~837 ("Drinfeld double & Theorem
(Tsymbaliuk 2017 Thm~1.1) & Partial (RSYZ 2020; KV 2018) & open") could
mislead a reader. Mismatch~1: scope declaration needed;
unlocalised-cokernel statement needed.

**Cycle 2.** ATTACK — The treatise's one-loop anomaly theorem
(line~929--947) states two coefficients $A_{\mathrm{w.f.}}$ and
$A_{\mathrm{anom}}$; the spine's `wn:thm:spine-consistent-covariant`
says these are related by a Bardeen--Zumino cochain. HEAL — The
treatise DOES distinguish the two; it labels the first as "absorbed
into a BV-trivial counter-term" and the second as "cohomologically
non-trivial". Structurally consistent with the spine. BUT the treatise
is silent on the Bardeen--Zumino cochain $\mathrm{BZ}^{\mathrm{hol}}$
that makes the two representatives cohomologous. Insert BZ cochain
statement; also normalise anomaly formula with BCOV metric factor.

**Cycle 3.** ATTACK — The conifold quiver $W_{\mathrm{con}} =
\mathrm{tr}(a_1 b_1 a_2 b_2 - a_1 b_2 a_2 b_1)$ on treatise line~349:
is this the Klebanov--Witten quiver or a sign-variant? HEAL — It IS
the Klebanov--Witten quiver in standard presentation; the spine does
not contradict the treatise at this locus. No mismatch. Recommend
adding Klebanov--Witten 1998 as parallel primary citation.

**Cycle 4.** ATTACK — The treatise's $K3 \times E$ four-corner
commutative square (line~495--517) attributes
$\fg_{\mathrm{BPS}}(K3 \times E) \simeq \fg_{\Delta_5}$ at graded-dimension
level unconditionally, at bracket level to AP-CY34 (Costello TCFT).
Is this the same obstruction the spine pinpoints to a single
Hecke--Borcherds identity on the Gritsenko paramodular family? HEAL —
YES; the two phrasings are two grammars (chain-level TCFT vs
automorphic-form Hecke--Borcherds) describing the same obstruction,
exactly as predicted by the treatise's own two-grammar discipline in
§`subsec:hcs-vs-cat-hochschild`. Insert Harvey--Moore route as
parallel to AP-CY34.

**Cycle 5.** ATTACK — Miki triality is NOT mentioned in the treatise
at all. Is this load-bearing? HEAL — YES; the treatise's shuffle-kernel
display on line~116 is manifestly $S_3$-symmetric, but the treatise
does not declare the triality. The spine's Theorem
`wn:thm:spine-coha-miki` ghosts the wrong framings (Retractions #12,
#13) that the treatise risks by silent omission. The treatise MUST
inscribe: (i) the ambient-vs-CY-slice scope; (ii) the direction
(shuffle-kernel is the source, $\Winf$ is the image shadow via
$\mathrm{ev}_\lambda$); (iii) the primary citations (Miki 2007, SV 2013,
FJMM 2016). Major insertion required.

**Cycle 6.** ATTACK — Treatise Strategy~3 on line~751 extends
Nakajima to $\Hilb^n(K3 \times E)$. The spine Retraction~#14 retracts
$\Hilb^n(\CC^3)$-based claims. Is $\Hilb^n(K3 \times E)$ smooth? HEAL —
Partial: $K3 \times E$ is smooth as a three-fold but
$\Hilb^n(K3 \times E)$ is **non-smooth / reducible** for $n \geq 4$
(Fogarty 1968 theorem extends only to dimension 2; Cheah 1998 for
dimension 3 at $n \leq 3$; Briançon 1977 for non-irreducibility
$n \geq 8$ on $\CC^3$, extending to $K3 \times E$ via local charts). The
treatise's Göttsche-formula-extended-to-products claim holds on the
**principal component** only, not on the full Hilbert scheme. Healing:
restrict to principal component; supplement with DT moduli-stack on
non-principal components.

**Cycle 7** (bonus). ATTACK — RSYZ 2020 attribution on treatise
line~391 for cohomological conifold CoHA identification with toroidal
$\widehat{\widehat{\fgl}_2}$: is this correct? HEAL — RSYZ 2020 Thm~B
is about the $\CC^3$-CoHA extension to general toric CY$_3$, not
specifically the conifold-toroidal identification. Correct attribution
for the toroidal identification on the conifold: Feigin--Jimbo--Miwa--Mukhin
2016 (toroidal shuffle) + Kapranov--Vasserot 2018 (geometric K-theoretic
action) + Negut 2015 (K-theoretic shuffle). Reattribution required,
parallel to spine Retraction~#34.

**Cycle 8** (bonus). ATTACK — Tsymbaliuk 2017 Thm~1.1 attribution on
treatise line~157 for the Drinfeld-double of $\CoHA(\CC^3)$: is this
the correct primary source, or is SV 2013 the primary? HEAL — Both are
load-bearing and complementary. SV 2013 / *Publ.~IHÉS* 2018 Thm~8.2
gives the shuffle-algebra Drinfeld-double; Tsymbaliuk 2017 gives the
explicit Drinfeld-currents presentation. User's brief suggests a
"Tsymbaliuk-Schiffmann-Vasserot 2018" joint paper — my literature
search does not find one; the treatise's Tsymbaliuk citation is
correct as-is, augmented with SV 2013 for completeness.
