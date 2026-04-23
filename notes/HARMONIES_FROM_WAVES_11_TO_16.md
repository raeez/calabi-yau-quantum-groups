# Harmonies from the Waves 11--16 Synthesis

**Author**: Raeez Lorgat. **Date**: 2026-04-22.
**Sources read**:
- Target (raw material, directionally suggestive but with incorrect specifics):
  `/Users/raeez/calabi-yau-quantum-groups/notes/platonic_synthesis_waves_11_through_16.tex` (lines 1--769).
- Canonical baselines (cross-checked against):
  `/Users/raeez/chiral-bar-cobar/notes/TRUTH_REPORT_WAVES_14_TO_26.md`;
  `/Users/raeez/calabi-yau-quantum-groups/notes/GRAND_SYNTHESIS_WAVES_14_TO_20.md`;
  `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3e_bkm_chapter.tex`;
  `/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex`;
  `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex`;
  `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/hochschild_calculus.tex`.

**Method**. Each harmony lists (1) what the document was reaching for, (2) where the
specific claim is wrong against the canonical baseline, (3) the correct canonical
statement with scope, (4) the inscription path that would upgrade the harmony to a
manuscript theorem. Five attack-heal cycles per harmony are folded into the canonical
form. Harmonies are ranked at the end by "closest to theorem-ready".

The criterion for inclusion is *directional fertility*: a directionally-correct claim
that is specifically wrong is more valuable than a directionally-wrong claim that is
incidentally numerically correct, because the former exposes a load-bearing structural
identity that has not yet been precisely stated.

---

## Harmony 1. The two-stage factorisation $\Phi_d = \mathrm{Sp}_{\Sigma_{d-1},C}\circ\Phi^{\mathrm{FA}}_d$ as the canonical home of "many BKMs from one CY".

**Directional claim** (target lines 47--73). The CY-to-chiral functor decomposes as
$\Phi_d = \mathrm{Sp}_{\Sigma_{d-1},C}\circ\Phi^{\mathrm{FA}}_d$, with Stage 1 producing
the canonical $E_d$-holomorphic factorisation algebra $\mathcal F_X$ on $X$ and Stage 2
specialising via factorisation homology over $\Sigma_{d-1}$ followed by restriction to
a reference curve $C$. Different $(\Sigma_{d-1}, C)$ produce different $E_1$-chiral
shadows; "many BKMs from one CY$_3$" then becomes a theorem about the $(\Sigma_2, C)$
parameter space rather than coincidence. The Borcherds Monster and Igusa
$\mathfrak g_{\Delta_5}$ are sibling specialisations.

**What is actually true**. Stage 1 alone is canonical (Kontsevich--Tamarkin
$E_d$-formality + Costello--Gwilliam--Li locality), and CLAUDE.md / Vol III canonicalise
exactly this two-stage picture. The directional content -- "Stage 1 produces a single
canonical $E_d$-hFA on $X$; Stage 2 is parametrically a $(\Sigma_{d-1}, C)$ choice" --
is correct. **What is wrong** in the target is the casting of "Borcherds Monster vs
Igusa $\mathfrak g_{\Delta_5}$" as $d=3$ siblings of one CY$_3$: these are siblings of
$\Psi$ (the CY-Siegel-automorphic functor), not of $\Phi_3$ on a single CY$_3$. Vol III
canonicalises five $\Psi$-images on five distinct lattice inputs, not five $\Phi_3$
specialisations on one CY$_3$ (`GRAND_SYNTHESIS_WAVES_14_TO_20.md` Section 11; Vol III
$\Psi$-functor table). The "Fake Monster cousin at $d=5$ with $K3\times K3\times E$"
(target lines 433--450) is also incorrect: Fake Monster has *no compact CY host* and
sits as a $\Psi$-image on $\mathrm{II}_{25,1}$ alone (healed draft line 297; TRUTH I.9,
I.24).

**Correct canonical statement** (two-sentence scope). On a fixed CY$_d$ $X$, the
two-stage factorisation $\Phi_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1},C}\circ
\Phi^{\mathrm{FA}}_d$ produces a *family* of $E_1$-chiral shadows of $X$, indexed by
the $(\Sigma_{d-1}, C)$ parameter space inside $X$; the Lorgat~2020 "many BKMs from one
CY$_3$" conjecture is the statement that this family realises the BKM landscape
attached to *the host CY$_3$*, not the entire $\Psi$-landscape. The sibling-relation
**within** $\Psi$ (Monster, Conway, Enriques, K3, Fake-Monster) is a separate functorial
phenomenon: $\Psi$ takes lattice + Jacobi-form inputs to BKM Hopf images, with no
requirement that the inputs come from a common host.

**Inscription path**. File:
`/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex`.
Inscribe a `\begin{theorem}[Two-stage factorisation; family of $E_1$-shadows on a
fixed host]` whose hypotheses are (i) Stage 1 is the canonical $E_d$-hFA produced by
KT formality + CGL locality (citing Kontsevich~1999 + Tamarkin~2003 + Willwacher~2014 +
Costello--Gwilliam~2017 + Costello--Li~2016), (ii) Stage 2 is $\int_{\Sigma_{d-1}}$
factorisation homology composed with restriction to $C$. Conclusion: the family
$\{\mathrm{Sp}_{\Sigma, C}\mathcal F_X\}_{(\Sigma, C)}$ of $E_1$-chiral algebras on
varying curves indexes the BKM zoo attached to $X$ at the $\Phi_d$-level. The companion
theorem inscribed in the same file should be a *negative result*: $\Psi$-siblings on
inequivalent lattices need not arise from a common host CY$_d$; the functor
$X \mapsto \{\mathrm{Sp}_{\Sigma, C}\mathcal F_X\}$ is *not* surjective onto the
$\Psi$-image landscape. Cross-reference Vol III $\Psi$-functor surjectivity table
(`k3e_bkm_chapter.tex` 4-sibling section) and the Vol I climax theorem on
five-archetype B row.

---

## Harmony 2. The $\Psi$-functor on CY-Siegel-automorphic data, four-sibling closure, rank discipline.

**Directional claim** (target lines 326--363, 433--450). There is a universal functor
$\Psi$ from CY-Siegel-automorphic data to BKM quantum-Hopf algebras; its images are
sibling specialisations of a common $E_d$-hFA framework; the Borcherds Monster
($\mathrm{II}_{1,1}$, $K=2$), Igusa $\mathfrak g_{\Delta_5}$ ($\Lambda^{2,1}$, $K=8$),
Fake Monster ($\mathrm{II}_{25,1}$, $K=50$) and Conway/Enriques cousins are co-siblings.

**What is actually true**. $\Psi$ is *not a single functor*; it is a *four-sibling
family* $\{\Psi, \Psi^{\deg}, \Psi^{\mathrm{tor}}, \Psi^{\mathrm{metap}}\}$ surjective
onto Gritsenko--Nikulin reflective signature-$(2, n\geq 3)$ BKMs (TRUTH I.24:
Scheithauer~2017 + DMS~2021 + Scheithauer~2006 chain). The single-$\Psi$ "Conway as
fifth bosonic image" was retracted at Wave 19/20 to "Conway as
$\Psi^{\mathrm{metap}}$-image" (TRUTH II Conway $\Psi$-placement row;
AP-CY111). The 22 non-Leech Niemeier BKMs (e.g.\ $24A_1$) are *genuine
counterexamples* to single-$\Psi$ surjectivity (TRUTH III.8). The directional claim
that there is *a* functor $\Psi$ with sibling closure is correct; the specifics
"$\Psi$ as a single functor" and "Conway as fifth bosonic" are wrong.

**Correct canonical statement** (three-sentence scope). The four-sibling family
$\{\Psi, \Psi^{\deg}, \Psi^{\mathrm{tor}}, \Psi^{\mathrm{metap}}\}$ from CY-Siegel-
automorphic data $\{(L, \phi_L) : L\text{ even lattice of signature } (2, n\geq 3),
\phi_L \in J^{!,\mathrm{wk}}_{0,\bullet}\}$ to BKM quantum-Hopf algebras is jointly
surjective onto the Gritsenko--Nikulin reflective signature-$(2, n\geq 3)$ class on the
Koszul locus, with the four siblings indexed by the four ramification types of the
Borcherds singular-theta lift (bosonic / degenerate / torsion / metaplectic). Conway
$V^{s\natural}$ ($c=12$, super-twin via Duncan diamond) sits on the
$\Psi^{\mathrm{metap}}$ branch, not as a fifth bosonic $\Psi$-image. Rank discipline:
Cartan rank ($2$ for Monster, $3$ for K3-BKM, $26$ for Fake Monster) is orthogonal
to Mukai-grading rank ($24$ for K3 specifically); the universal identity
$\hbar^2 K^{\kappa_{\mathrm{ch}}} = -1$ holds per-row with $K = 2c_+(L)$ where $c_+$
is the *positive-signature contribution* of the input lattice (`k3e_bkm_chapter.tex:3849--3850, 4055--4078`).

**Inscription path**. File:
`/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3e_bkm_chapter.tex`.
Already partially inscribed at Section "$\Psi$-functor landscape" of Grand Synthesis
W14--20. Required upgrade: a single Vol III theorem `\begin{theorem}[Four-sibling
$\Psi$ family: surjectivity onto reflective sig-$(2, n\geq 3)$ BKMs]` consolidating
Scheithauer 2017 + DMS 2021 + Scheithauer 2006 into a structural statement; companion
theorem on the four ramification types and how they distinguish bosonic / degenerate /
torsion / metaplectic; companion remark establishing the Conway placement on the
metaplectic branch (citing Duncan~2007). Counter-example: the $24A_1$ Niemeier BKM
(Borcherds 1995 *Invent Math* 120 §13, singular weight $12$ on sig $(2,24)$) lies
*outside* the four-sibling image, witnessing the residual frontier.

---

## Harmony 3. The three-faces identity $\hbar^2 K^{\kappa_{\mathrm{ch}}} = -1$ with row-by-row $K$ and the meaning of the constant $-1$.

**Directional claim** (target lines 35, 36, 39 of the synthesis are missing the
explicit $-1$ form; canonical baseline `GRAND_SYNTHESIS_WAVES_14_TO_20.md` line 35
inscribes it). The number $K^{\kappa_{\mathrm{ch}}}$ admits three independent route
identifications -- Mukai doubling $2c_+$, Humbert local-monodromy order, Lusztig small
quantum group level -- all converging on the same integer per row. The constant $-1$
on the right-hand side is dimensionless and universal; the row-dependence is in $K$
and $\hbar^2 = -1/K$ alone.

**What is actually true**. WOV-1 / WOV-10 of the K3 row is fully validated:
$(K, \hbar^2) = (8, -1/8)$ via three routes
($2c_+(\mathrm{Mukai}(K3)) = 8$;
$\mathrm{ord}(\mathrm{mon}\,\mathcal L^{\Delta_5}|_{H_1}) = 8$;
$\ell_{\mathrm{Lusztig}} = 8$). Per-row $K$-values: Monster $K = 2$, K3 $K = 8$,
Fake Monster $K = 50$, Enriques $K = 4$, Conway via metaplectic $K = 2$
(`k3e_bkm_chapter.tex:3849--3850, 7492, 8479`). The Conway row $K = 2$ is *on the
super-extension* $L^s_{\mathrm{Conway}}$, not on Leech itself; the bosonic Leech
plug-in $L = \Lambda_{24}$ would give $K = 2c_+(\Lambda_{24}) = 48$
(`k3e_bkm_chapter.tex:8012`) but is *out of scope* on Leech (no hyperbolic plane;
TRUTH VI Conway dual reading). The directional claim "three independent routes
converge on a row-specific integer" is correct; the only refinement needed is that
the three routes coincide *only after* applying the Bruinier 2002 Prop 5.1 reciprocity
(Heegner-Chern reciprocity), which forces $K = 2c_+(L)$ from the signature of the
Gram matrix of the input lattice (`k3e_bkm_chapter.tex:4078, 4091`).

**Correct canonical statement** (two-sentence scope). For each row in the four-sibling
$\Psi$-family with input lattice $L$ of signature $(2, n)$, the universal identity
$\hbar^2 K^{\kappa_{\mathrm{ch}}} = -1$ holds with $K = 2c_+(L)$; the three coincidences
(Mukai-doubling / Humbert-monodromy / Lusztig-level) are routes through Bruinier 2002
Prop 5.1 Heegner-Chern reciprocity. Per-row table: Monster $(K, \hbar^2) = (2, -1/2)$,
Enriques $(4, -1/4)$, K3 $(8, -1/8)$, Fake Monster $(50, -1/50)$, Conway via metaplectic
$(2, -1/2)$ (super-extension scope; bosonic Leech plug-in gives $48$, out of scope).

**Inscription path**. Vol III `k3e_bkm_chapter.tex` already has the row-by-row table
(Section "Universal identity per $\Psi$-row"; lines 3849--3850, 4055--4078, 4174--4183).
Required upgrade: a single closing theorem
`\begin{theorem}[Universal identity, four-sibling per-row form]` consolidating Bruinier 2002
Prop 5.1 + Lusztig 1990/1993 small quantum group + Mukai 1988 lattice signature into a
single structural statement, with the explicit table and an explicit "out-of-scope"
remark for Leech bosonic. Cross-volume: synchronise with Vol I `landscape_census.tex`
B-row at lines 5078, 5137, 5292, 5306, 5324; Vol II SC^{ch,top} chain-level
witnesses at the $\hbar^2$-specialisation locus.

---

## Harmony 4. The universal Borcherds weight $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ at two scopes.

**Directional claim** (target lines 237--263). The "universal Borcherds weight"
$\kappa_{\mathrm{BKM}} = c_N(0)/2$ is universal across all $\Psi$-siblings; a stronger
"universal additive law" $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal O_{\mathrm{fiber}})$
might hold (target line 495).

**What is actually true**. $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ is canonical
**at two coexistent scopes**:
- BKM-denominator scope (CHL slice $N \in \{1,2,3,4,6\}$, $\varphi(N)\mid 2$):
  values $\{5, 4, 3, 2, 1\}$, per Gritsenko 1999 Thm 1.2
  (`k3e_bkm_chapter.tex:949--957`).
- Borcherds-weight scope (full 8-form Gritsenko--Cl\'ery class $N\in\{1,\ldots,8\}$):
  values $\{5, 2, 1, 1, 1/2, 1, 1/4, 0\}$, per Borcherds 1998 Thm 13.3, including
  metaplectic ($N=5$, weight $1/2$), spin double ($N=7$, weight $1/4$),
  abelian-degenerate ($N=8$, weight $0$) (`k3e_bkm_chapter.tex:962--964`).
The two scopes give the same value at $N=1$ but diverge at $N\geq 2$
(`k3e_bkm_chapter.tex:979`). The proposed additive law
$\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal O_E)$ is **retracted**:
the alleged $N=1$ coincidence ($5 = 0 + 0$) is itself confabulated (healed draft
line 295; AP238). The directional content "$c_N(0)/2$ is universal at *some* scope" is
correct; the specifics "additive decomposition through $\kappa_{\mathrm{ch}}$" are
wrong. The remaining cross-volume tension is the AP5 issue between Vol I (writing 12,
indexed against Fake-Monster $\Phi_{12}$) and Vol III (writing 5, indexed against
$\Phi_{10} = \Delta_5^2$): TRUTH III.1 / TRUTH IV (only open AP5 gap) /
TRUTH VI third dual reading.

**Correct canonical statement** (three-sentence scope). The universal Borcherds-weight
identity $\kappa_{\mathrm{BKM}}(\Phi) = c(0)/2$ holds at two scopes: BKM-denominator
($N \in \{1,2,3,4,6\}$ CHL, values $\{5,4,3,2,1\}$, Gritsenko 1999) and full Borcherds
singular-theta ($N \in \{1,\ldots,8\}$ GC, values $\{5,2,1,1,1/2,1,1/4,0\}$, Borcherds
1998). Cross-volume convention: the two volumes use different denominator inputs
($\Phi_{10} = \Delta_5^2$ in Vol III gives $5$; Fake-Monster $\Phi_{12}$ in Vol I
gives $12$). The proposed additive decomposition
$\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal O_{\mathrm{fiber}})$
is *not* a structural law; it fails already at $N=1$ ($5 \neq 0 + 0$), and the
"universal additive structure" is not what $c_N(0)/2$ encodes.

**Inscription path**. Vol III `k3e_bkm_chapter.tex:943--985` already inscribes both
scopes as one theorem (`thm:k3e-universal-kBKM-two-scopes`). Required upgrade:
(i) cross-volume AP5 lock: insert a remark at `k3e_bkm_chapter.tex:946` and at
`/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex` B-row pinning
the two conventions and their relation; (ii) inscribe a `\begin{theorem}[Negative
result: $\kappa_{\mathrm{BKM}}$ does not decompose additively through
$\kappa_{\mathrm{ch}}$ and fibre]` with the $N=1$ counterexample, citing AP238 / healed
draft line 295. The negative result is load-bearing because it scopes the universality:
the universal datum *is* $c_N(0)/2$ from the input weak Jacobi form, not from a
breakdown into chiral and fibre invariants.

---

## Harmony 5. The Heisenberg--Mukai $\eta^{-48}$ identity as a doubling of $24$, not as Virasoro-minimal coincidence.

**Directional claim** (target lines 391--410). The character identity
$\chi_{\mathrm{Heis}(\mathrm{Muk}(K3)^{\oplus 2})}(q) = \prod_n(1-q^n)^{-48}
= -q^{-2}[(2\pi i z)^2 \Delta_5^{-2}]|_{H_1, z=0}$ holds to all orders and is the
Heisenberg-side projection of $\Delta_5^{-2}$ at the Humbert $H_1$ residue. This
is *not* a Virasoro-minimal coincidence; the original
"$\chi_{\mathcal V_{24}} = \Delta_5^{-2}$ via Virasoro $(2,45)$-minimal" was retracted
(target line 506; healed draft line 299).

**What is actually true**. The Heisenberg-Mukai identity is correct *provided* the
$48$ is read as $2\cdot 24$ where one factor of $24$ is the Mukai rank
($H^*(K3,\mathbb Z) \cong \mathrm{II}_{4,20} \oplus \langle 0 \rangle^{\otimes \cdot}$
of total rank $24$) and the other factor is the doubling
$\mathrm{Muk}(K3)^{\oplus 2}$ entering the Heisenberg algebra construction
(target line 394 reads exactly this). The Vol II canonical reads
$\eta^{-24}$ as the Göttsche generating function of K3 punctual Hilbert schemes
(`GRAND_SYNTHESIS_WAVES_14_TO_20.md` line 76); the doubling to $\eta^{-48}$ is the
$\mathrm{Muk}^{\oplus 2}$ Heisenberg-doubling, *not* an "independent $24$" coincidence.
Specifically, the two $24$s are the same $\chi_{\mathrm{top}}(K3) = 24$ entering
twice through the Heisenberg construction. The directional claim "all-orders
Heisenberg = Mukai-doubled" is correct; the alleged "two unrelated $24$s coinciding"
reading is wrong.

**Correct canonical statement** (two-sentence scope). The character identity
$\chi_{\mathrm{Heis}(\mathrm{Muk}(K3)^{\oplus 2})}(q) = \prod_n (1-q^n)^{-48}$ is exact
to all orders, with the exponent $48 = 2\cdot 24$ encoding the
$\mathrm{Muk}(K3)^{\oplus 2}$-Heisenberg doubling of the single Mukai-rank-$24$ input;
the residue identity
$-q^{-2}[(2\pi i z)^2 \Delta_5^{-2}]|_{H_1, z=0} = \prod_n (1-q^n)^{-48}$
follows from Gritsenko--Nikulin 1996 Cor 5.2 at the Humbert $H_1$ divisor combined
with Frenkel--Ben-Zvi 2004 Heisenberg character. The Heisenberg Shapovalov form is
block-diagonal with unit determinants, so no null vectors; the match is exact at
the Heisenberg level rather than via a Virasoro-minimal coincidence (which would
require a null-vector cancellation that does not exist here).

**Inscription path**. File:
`/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:421` (per
target line 514: already inscribed as the residue identity at $H_1$). Required
upgrade: add a remark distinguishing this Heisenberg-doubled identity from the
retracted Virasoro-minimal claim, with explicit citation to AP238 / healed draft
line 299. Cross-reference `landscape_census.tex` B-row $\eta^{-24}$ Göttsche entry
and the GRAND_SYNTHESIS twelve-faces-of-$24$ table
(`GRAND_SYNTHESIS_WAVES_14_TO_20.md` lines 65--77).

---

## Harmony 6. CoHA $= Y^+$, with Drinfeld double recovering the affine Yangian, and the relation to $\mathcal W_{1+\infty}$.

**Directional claim** (target lines 360--389). $\mathrm{CoHA}(\mathbb C^3) = Y^+$
(positive half of affine Yangian); $\mathcal W_{1+\infty}$ is the
$\mathrm{ev}_\lambda$-image shadow; the Miki $S_3$-automorphism descends from
Drinfeld-double level to coalgebra-dual / factorisation algebra on $\mathrm{Ran}(\mathbb C)$
levels.

**What is actually true**. The cache rule "$\mathrm{CoHA}(\mathbb C^3) = Y^+ \neq
\mathcal W_{1+\infty}$" is correct at the structural level; Schiffmann--Vasserot 2013
Publ Math IH\'ES $118$ §6 establishes the CoHA-shuffle product $\mu_3^{\mathrm{CoHA}}$
and the identification of the Drinfeld double $D(Y^+) = Y(\widehat{\mathfrak{gl}}_1)$
(`hochschild_calculus.tex:717, 1779; quantum_chiral_algebras.tex:86, 102`). The
$\mathrm{ev}_\lambda$ image shadow construction is a real algebraic operation
(Pro\v{c}hazka--Rap\v{c}\'ak 2018 trinion correspondence) and gives the
$\mathcal W_{1+\infty}[\lambda]$ family. The Miki $S_3$ automorphism, on the
$(q, t, s)$-deformed quantum-toroidal $\mathfrak{gl}_1$ algebra
(Feigin--Jimbo--Miwa--Mukhin 2016), descends structurally on the CY torus
$(q_1, q_2, q_3)$ via Weyl group on the CY constraint $\sum \epsilon_i = 0$. The
directional content is correct; the **specific** wrinkle to fix is that the Miki
automorphism is *algebra-specific* (`quantum_chiral_algebras.tex:712`), not a generic
operadic feature, and the CY$_3$ "non-truncation under $\sum\epsilon_i = 0$" is *not*
a refutation of any conjecture but rather the canonical content
(target line 386 reads this correctly).

**Correct canonical statement** (three-sentence scope). At the cohomological Hall
algebra level, $\mathrm{CoHA}(\mathbb C^3) = Y^+$ (positive half of the affine
Yangian $Y(\widehat{\mathfrak{gl}}_1)$) via Schiffmann--Vasserot 2013, with
Drinfeld double $D(Y^+)$ identified with the full affine Yangian; the Pro\v{c}hazka--
Rap\v{c}\'ak $\mathrm{ev}_\lambda$ slice gives $\mathcal W_{1+\infty}[\lambda]$ as a
one-parameter family of vertex algebras. The Miki 2007 $S_3$-automorphism on
$\mathcal W_{1+\infty}[\lambda]$ is the $\mathrm{ev}_\lambda$ shadow of an
$S_3$-equivariant structure on the $(q_1, q_2, q_3)$-deformed quantum-toroidal
algebra; it descends on the Drinfeld double, on the positive half $Y^+$, and on
the coalgebra dual realised as a factorisation algebra on $\mathrm{Ran}(\mathbb C)$
(Beilinson--Drinfeld §3.4). At the Calabi--Yau evaluation $\sum \epsilon_i = 0$
the qq-character recursion gains $S_3$-triality; the natural "CY$_3$ forces finite-rank
truncation" guess is wrong. The Miki automorphism is *algebra-specific*, not a generic
operadic structure of Drinfeld doubles.

**Inscription path**. Vol III `quantum_chiral_algebras.tex:50, 86, 102, 152, 205, 661,
712` already has the structural skeleton. Required upgrade: a single Vol III theorem
`\begin{theorem}[CoHA-to-W-infinity triality: structural descent]` consolidating the
five lines of descent (Miki $S_3$ on $\mathcal W_{1+\infty}$; Drinfeld double on $Y$;
positive half $Y^+$; coalgebra dual on $\mathrm{Ran}(\mathbb C)$; quantum-toroidal
$(q_1,q_2,q_3)$-equivariance). Companion remark on the CY$_3$ non-truncation,
referencing Wave 14 K2 and Feigin--Jimbo--Miwa--Mukhin 2016 Triality. Cross-reference
the Vol II SC^{ch,top} factorisation-algebra story.

---

## Harmony 7. Anomaly-free gauge-algebra locus for $6$d hCS: $d^{abc}$-vanishing structural identity.

**Directional claim** (target lines 122--146). For $6$d hCS on a CY$_3$ with gauge
Lie algebra $\mathfrak g$, the one-loop BV obstruction factorises as
$\kappa_{\mathrm{anom}}(X, \mathfrak g) = \hbar A(\mathfrak g)\cdot
\chi_{\mathrm{top}}(X)/(2(4\pi)^3)\cdot \|\Omega_X\|^2$, where $A(\mathfrak g)$ is the
cubic-Casimir coefficient $d^{abc}$. $\kappa_{\mathrm{anom}} = 0$ automatically for
gauge algebras with $d^{abc} = 0$, namely $\{\mathrm{SU}(2), \mathrm{SO}(N), E_6, E_7, E_8,
F_4, G_2\}$.

**What is actually true**. The factorisation pattern is structurally correct: the
cubic Casimir $d^{abc}$ on the gauge Lie algebra is the chiral-anomaly coefficient
in $6$d, and $d^{abc} = 0$ on $\mathfrak g$ is a *necessary and sufficient* condition
for $\kappa_{\mathrm{anom}}$ to vanish for *generic* CY$_3$. The claim that
$\{\mathrm{SU}(2), \mathrm{SO}(N), E_6, E_7, E_8, F_4, G_2\}$ all have $d^{abc} = 0$ is
**not quite right**: the strict list of simple Lie algebras with $d^{abc} = 0$ on the
adjoint is $\{\mathfrak{su}(2), \mathfrak{so}(N) \text{ for } N \neq 6,
E_6 \text{ has } d^{abc} \neq 0, E_7, E_8, F_4, G_2\}$ -- $E_6$ is the
**counter-example** since $E_6$ has a cubic invariant via $\mathrm{Sym}^3(\mathbf{27})$.
The correct anomaly-free list (in $4$d gauge theory parlance, for which $6$d hCS is
the holomorphic shadow) is the *Deligne exceptional series* refined by
$d^{abc} = 0$, which excludes $E_6$ and includes $\mathfrak{su}(2)$. The directional
content is right; the specific list needs $E_6$ removed.

**Correct canonical statement** (three-sentence scope). The $6$d hCS one-loop BV
anomaly $\kappa_{\mathrm{anom}}(X, \mathfrak g) = \hbar\cdot d^{abc}_{\mathfrak g}\cdot
[\chi_{\mathrm{top}}(X)/(2(4\pi)^3)]\cdot \|\Omega_X\|^2$ vanishes if and only if
$d^{abc}_{\mathfrak g} = 0$ (for generic CY$_3$ with $\chi_{\mathrm{top}} \neq 0$); the
simple gauge algebras with $d^{abc} = 0$ are $\{\mathfrak{su}(2), \mathfrak{so}(N) \text{ for }
N\neq 6, E_7, E_8, F_4, G_2\}$, with $E_6$ excluded (via the $\mathrm{Sym}^3(\mathbf{27})$
cubic invariant). For non-generic CY$_3$ with $c_3(X) = 0$ (e.g.\ $K3 \times E$),
the anomaly vanishes for *any* simple $\mathfrak g$ on $\chi_{\mathrm{top}}$-grounds,
and only the universal gauge-independent piece (Costello--Li 2016 $\alpha_{\mathrm{BCOV}}$)
remains.

**Inscription path**. File needs identification (target Theorem `wn:thm:plat-anomaly`
points to a hCS chapter). The natural home is Vol II
`/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/six_d_hcs_feynman_coefficients.tex`.
Required upgrade: inscribe a single theorem
`\begin{theorem}[$6$d hCS anomaly-free gauge-algebra locus]` with the corrected list,
citing Costello 2013 §5 (chiral-anomaly factorisation of $d^{abc}$), Costello--Li 2016
Prop 5.2 (one-loop BV obstruction class), Costello--Gwilliam 2017 Vol II §15.4 (cubic-
Casimir trace identity). Companion remark: on $K3 \times E$, *all* simple $\mathfrak g$
are $\kappa_{\mathrm{anom}}$-trivial because $\chi_{\mathrm{top}}(K3 \times E) = 0$;
the universal gauge-independent obstruction $\alpha_{\mathrm{BCOV}}$ also vanishes
(target Remark `wn:rmk:plat-formality-witness` lines 602--611). Cross-reference Vol III
`/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex`
hCS quantisation section.

---

## Harmony 8. The all-orders $1/\Phi_{10}$ exponentiation from the BV anomaly tower.

**Directional claim** (target lines 268--305). The all-orders BV anomaly tower
exponentiates to $(\Phi_{10}/\eta^{24})^\hbar$, with the $\hbar^n$-coefficients
$c_n = c_{\phi_{-2,1}}(-n)$ following the Heegner pattern ($n \equiv 0, 3 \bmod 4$
admissibility, otherwise zero). Proved at $1$-loop, $2$-loop, $3$-loop; conjectural
at $4+$-loop.

**What is actually true**. The structural reason for all-orders equality is the
**Borcherds singular-theta lift**: the input data $\phi_{-2,1}$ (weak Jacobi form of
weight $-2$, index $1$) lifts via Borcherds 1998 Thm 13.3 to the Igusa cusp form
$\Phi_{10}$, and the BV anomaly tower in twisted 11D SUGRA on $\mathbb R^3 \times K3
\times \mathbb C^2$ with $24$ M5-branes on $I_1$ Kodaira fibres tracks Fourier
coefficients of $\phi_{-2,1}$ via Costello--Gaiotto--Paquette 2018 one-loop
factorisation-algebra holography. The exponentiation
$\exp(\sum_n \hbar^n c_n) = (\Phi_{10}/\eta^{24})^\hbar$ is canonical
(`GRAND_SYNTHESIS_WAVES_14_TO_20.md` lines 230--235; explicit values at lines 213--225).
The status table is **wrong** in the target: only $1$-loop is unconditionally proved
($\alpha_{\mathrm{BCOV}}$ via Costello--Li 2016 Prop 5.2); the structure of higher-loop
BV obstructions $c_n$ is *conjecturally* the Heegner pattern (Wave 18 Costello),
proved as an *all-orders identity* (modulo Bruinier 2002 Heegner-Chern reciprocity
+ Borcherds 1998 lift), not as a per-loop statement. The "$1$-, $2$-, $3$-loop proved
versus $4$+-loop conjectural" framing is thus **inverted from the truth**: the
all-orders structural identity is what is proved (modulo two primary-source
reductions); the per-loop direct verification is what is open beyond $3$-loop. The
specific values $c_3 = -8$ (not $176256$) corrected at TRUTH II row $c_3$ /
GRAND_SYNTHESIS row 3 are now stable.

**Correct canonical statement** (three-sentence scope). The all-orders BV anomaly
tower of twisted 11D SUGRA on $\mathbb R^3 \times K3 \times \mathbb C^2$ with $24$
M5-branes on $I_1$ Kodaira fibres exponentiates to $(\Phi_{10}/\eta^{24})^\hbar$, with
$\hbar^n$-coefficient $c_n = c_{\phi_{-2,1}}(-n)\cdot[H_n]$ (Heegner pattern,
admissibility $n\equiv 0,3\bmod 4$). The structural reason for all-orders equality is
Borcherds 1998 Thm 13.3 (singular-theta lift $\phi_{-2,1}\mapsto \Phi_{10}$) combined
with Bruinier 2002 Prop 5.1 (Heegner-Chern reciprocity), reducing the BV problem to
two primary-source automorphic-form identities. Per-loop direct verification has
been carried out at $1$-, $2$-, $3$-loop (Costello--Li 2016 + Costello--Gaiotto--
Paquette 2018 + Wave 18 Costello $c_3 = -8$); $4+$-loop is open as direct
computation but is *implied* by the all-orders identity.

**Inscription path**. Vol III `k3e_bkm_chapter.tex` BV-tower section already inscribes
the all-orders identity. Required upgrade: explicitly invert the status table to
read "all-orders identity proved; per-loop direct verification is the open frontier".
This inversion is the load-bearing structural content. Cross-reference the
`GRAND_SYNTHESIS_WAVES_14_TO_20.md` BV-table at lines 213--225 with explicit values
$\{c_3 = -8, c_4 = 12, c_7 = -39, c_8 = 56, c_{11} = -152, c_{12} = 208\}$ and the
asymptotic $|c_n| \sim \exp(\pi\sqrt n)$ (Ramanujan-Petersson for Jacobi forms,
Gevrey-$1$ divergence in naive $\hbar$).

---

## Harmony 9. The $\mathrm{GRT}_1$-torsor as the unification of motivic Galois on K3 periods and Drinfeld-associator gauge on quantisations.

**Directional claim** (target lines 720--752). The KT formality space is a
$\mathrm{GRT}_1(\mathbb Q)$-torsor; choosing a Drinfeld associator rigidifies the
torsor; Costello--Li 2016 6d hCS produces a specific associator $\Phi_{\mathrm{CL}}$
conjecturally equivalent to Kontsevich $\Phi_{\mathrm{KZ}}$. The four-$\kappa$ stage
assignment ($\kappa_{\mathrm{ch}}$, $\kappa_{\mathrm{cat}}$, $\kappa_{\mathrm{fiber}}$,
$\kappa_{\mathrm{BKM}}$) lives at the $\mathrm{GRT}_1$-torsor level.

**What is actually true**. The structural identification is correct
(Tamarkin 2003 + Willwacher 2014 $H^0(\mathrm{GC}_2) = \mathfrak{grt}_1$). The
**deep harmony** the document is reaching for is the *unification* of two distinct
$\mathrm{GRT}_1$-actions:
- $\mathrm{GRT}_1$ as gauge on $\mathbf H_{\Delta_5}$-quantisations
  (Etingof--Kazhdan torsor: `GRAND_SYNTHESIS_WAVES_14_TO_20.md` lines 120--143).
- $\mathrm{GRT}_1$ as motivic-Galois on K3 periods (Witten side, via K3 period map).

These two actions **AGREE through the Kuga--Satake functor**
(`GRAND_SYNTHESIS_WAVES_14_TO_20.md` line 141, line 491). The "MGSL = motivic Galois
super-Lie equivalent to BKM-Cartan $\times$ Kuga--Satake" claim is *not yet inscribed*
in any of the three volumes; it is a **frontier conjecture** that the
$\mathrm{GRT}_1$-double-action AGREEMENT *is* the motivic-Galois-side structure
witnessed by Kuga--Satake. Brown 2011 Ann Math 175 transitivity is *unconditional
through weight 12*; weights $\geq 13$ require Zagier-Hoffman depth-reduction.

**Correct canonical statement** (three-sentence scope). The KT formality space on
$\Omega^{0,\bullet}(X, \mathfrak g)$ is a $\mathrm{GRT}_1(\mathbb Q)$-torsor (Tamarkin
2003, Willwacher 2014); on the K3-BKM row, $\mathrm{GRT}_1$ acts simultaneously as
Etingof--Kazhdan gauge on quantisations of $\mathbf H_{\Delta_5}$ and as motivic-Galois
on K3 periods, the two actions agreeing through the Kuga--Satake functor (Wave 20
Witten + Etingof). The four-$\kappa$ stage assignment ($\kappa_{\mathrm{ch}}$ at
Stage 1 before Drinfeld-associator choice; $\kappa_{\mathrm{cat}}$ and
$\kappa_{\mathrm{fiber}}$ both $\mathrm{GRT}_1$-invariant; $\kappa_{\mathrm{BKM}}$ at
Stage 2 depending on the specialisation $(\Sigma_2, C)$ and the associator lift)
follows from the $\mathrm{GRT}_1$-torsor structure; transitivity through weight $12$
is unconditional, weights $\geq 13$ are doubly-conditional on Zagier--Hoffman.

**Inscription path**. Vol III `cy_d_kappa_stratification.tex:rem:four-kappa-stage-
assignment-cy-d-strat` already has the four-$\kappa$ stage skeleton. Required upgrade:
a Vol III theorem
`\begin{theorem}[$\mathrm{GRT}_1$-double-action agreement via Kuga--Satake]` with the
two actions made precise (Etingof--Kazhdan gauge on quantisations, motivic Galois
on K3 periods) and the Kuga--Satake functor witnessing the agreement. Companion
**conjecture** at the frontier:
`\begin{conjecture}[MGSL conjecture: motivic Galois super-Lie equivalent to BKM-Cartan
$\times$ Kuga--Satake]`. Cross-reference Vol I `landscape_census.tex` for the
$\kappa$-stratification, and Vol II SC^{ch,top} for the chain-level
$L_\infty$-quasi-isomorphism ambient. The MGSL conjecture is the open frontier item
worth advertising as "what would be theorem-grade if proved".

---

## Harmony 10. Three-tier stratification of $r_{\mathrm{CY}}$ on $K3\times E$ and the orthogonal seven-presentation slicing.

**Directional claim** (target lines 335--358). The arithmetic faces of $r_{\mathrm{CY}}$
on $K3\times E$ sort into three tiers: (i) CY-datum intrinsics ($\kappa_{\mathrm{ch}}$,
Mukai pairing), (ii) Stage-1 invariants of $\mathcal F_X$ ($\kappa_{\mathrm{fiber}} = 24$),
(iii) $(\Sigma_2, C)$-specialisations ($\kappa_{\mathrm{BKM}}$, Niemeier-twist family,
Humbert boundary, CHL twined family). The seven-presentation slicing
(bar--cobar / CoHA / coisson / MO / Yangian / Sklyanin / Gaudin) is **orthogonal**, not
a competitor.

**What is actually true**. The directional content is correct and is one of the most
load-bearing structural identities in the document; the three-tier stratification is
exactly the canonical content of CLAUDE.md ($\kappa_{\mathrm{ch}}$ vs $\kappa_{\mathrm{cat}}$
vs $\kappa_{\mathrm{fiber}}$ vs $\kappa_{\mathrm{BKM}}$ all distinct invariants attached
to different stages of the two-stage factorisation). The orthogonal-slicing claim
("algebraic seven-presentation is orthogonal to the arithmetic three-tier") is the
correct restatement of the seven-routes-to-$\mathbf H_{\Delta_5}$ theorem
(`GRAND_SYNTHESIS_WAVES_14_TO_20.md` Section 15: "Six routes are DIFFERENT
constructions, not six applications of a single $\Phi$"). The directional content is
fully correct; the only refinement needed is to make the orthogonality precise as a
*Cartesian product structure* on the data, with the three-tier filtration as one
factor and the seven-presentation slicing as the other.

**Correct canonical statement** (three-sentence scope). On a fixed CY$_3$ host
$X = K3 \times E$ (and more generally on any CY$_3$ admitting a Stage-2 specialisation
to a curve), the data attached to $\Phi_3 X$ admits a Cartesian product structure:
the *arithmetic* axis carries the three-tier stratification (CY-datum intrinsics /
Stage-1 invariants / Stage-2 $(\Sigma_2, C)$-specialisations) of the four $\kappa$
invariants; the *algebraic* axis carries the orthogonal seven-presentation slicing
(bar--cobar / CoHA / coisson / MO / Yangian / Sklyanin / Gaudin) of the resulting
chiral algebra. The two axes commute: a $(\Sigma_2, C)$-specialisation produces a
chiral algebra whose seven presentations all agree on the Koszul locus, and a
seven-presentation choice does not collapse the tier structure.

**Inscription path**. Vol I `landscape_census.tex` and Vol III
`cy_d_kappa_stratification.tex` already have both axes inscribed separately. Required
upgrade: a single Vol III theorem
`\begin{theorem}[Cartesian product structure: three-tier stratification orthogonal
to seven-presentation slicing]` consolidating the two axes into one structural
statement. Cross-reference: Vol II SC^{ch,top} pentagon-of-equivalences and Vol I
`mc5_class_m_chain_level_platonic.tex:229` ambient-qualified statement (chain-level
vs $(\infty,1)$-categorical Pattern 269 / Pattern 236 ambient discipline).

---

## Closing: Ranking of the harmonies by closeness to theorem-ready

**Tier A (theorem-ready, primary inscription required only).**

1. **Harmony 1** (two-stage factorisation: family of $E_1$-shadows on a fixed host,
   with negative result on $\Psi$-sibling reach). The two-stage decomposition is fully
   canonical, Stage 1 is Kontsevich--Tamarkin formality + Costello--Gwilliam--Li
   locality, Stage 2 is factorisation homology + restriction. The negative result
   (Vol III $\Psi$-siblings need not arise from a common host) is what differentiates
   this from the target's incorrect "many BKMs from one CY$_3$".

2. **Harmony 3** (universal identity per-row, $K = 2c_+(L)$ from Bruinier 2002 Prop 5.1).
   Per-row table fully validated by WOV-1/10; only required upgrade is consolidating
   the per-row presentation into one closing theorem with the explicit "out-of-scope"
   remark for Conway bosonic Leech.

3. **Harmony 4** (universal Borcherds weight $c_N(0)/2$ at two scopes, with negative
   result on additive decomposition). Both scopes already inscribed; the negative
   result is the load-bearing structural new statement.

**Tier B (theorem-ready, depends on AP5 cross-volume lock).**

4. **Harmony 2** (four-sibling $\Psi$-family surjective onto reflective signature
   $(2,n\geq 3)$ BKMs; Conway placement on metaplectic branch). Requires Scheithauer
   2017 + DMS 2021 + Scheithauer 2006 chain to be consolidated into one theorem;
   companion remark on $24A_1$ Niemeier as the non-image counterexample.

5. **Harmony 8** (all-orders $(\Phi_{10}/\eta^{24})^\hbar$ exponentiation; per-loop
   verification is the open frontier, *not* the all-orders identity). Requires
   inverting the status table, which is the load-bearing reframing.

**Tier C (theorem-ready conditional on primary-literature audit).**

6. **Harmony 6** (CoHA-W-infinity triality with descending Miki $S_3$). Five lines of
   descent already present in `quantum_chiral_algebras.tex`; consolidation theorem
   needed plus the algebra-specific (not generic-operadic) caveat.

7. **Harmony 10** (Cartesian product structure of arithmetic three-tier and
   algebraic seven-presentation slicing). Both axes already inscribed; product
   structure is the new theorem.

**Tier D (frontier; conjecture inscription appropriate).**

8. **Harmony 9** (MGSL conjecture: motivic Galois super-Lie equivalent to BKM-Cartan
   $\times$ Kuga--Satake, witnessed by $\mathrm{GRT}_1$-double-action agreement
   through Kuga--Satake). The double-action agreement is theorem-ready;
   the MGSL identification is conjecture-ready and is the deepest open structural
   item. Brown 2011 transitivity through weight $12$ unconditional; $\geq 13$
   doubly-conditional.

9. **Harmony 7** ($d^{abc} = 0$ anomaly-free locus, with corrected list excluding $E_6$).
   Theorem-ready in Vol II hCS chapter; the $E_6$ correction is structurally important
   because it shifts the Deligne-exceptional-series story.

**Tier E (theorem-ready but lower priority for the climax architecture).**

10. **Harmony 5** (Heisenberg-Mukai $\eta^{-48}$ as Mukai-doubled $24$, not Virasoro-
    minimal coincidence). Already inscribed at `cy_to_chiral.tex:421`; required
    upgrade is the AP238 cross-reference and the explicit retraction of the
    Virasoro-minimal reading.

---

**Ranking summary**: Harmonies 1, 3, 4 are the most load-bearing for the climax
architecture (two-stage factorisation, universal identity per-row, universal
Borcherds weight at two scopes). Harmony 2 is the deepest *expansion* (four-sibling
$\Psi$ closure, replacing single-$\Psi$). Harmony 8 is the most load-bearing
*reframing* (all-orders identity proved, per-loop verification open). Harmony 9 is the
most load-bearing *frontier* (MGSL via Kuga--Satake double action). The remaining
harmonies (5, 6, 7, 10) are load-bearing local refinements that consolidate already-
inscribed material into single theorems.

**Cross-volume operating discipline**: every harmony admits both chain-level and
$(\infty,1)$-categorical realisations, with both lanes load-bearing per CLAUDE.md
preamble (Pattern 269 ambient discipline). The four-sibling $\Psi$-family expansion
(Harmony 2) is the structural item most at risk of an AP5 cross-volume drift if not
locked at primary-source level.

**Files of inscription** (absolute paths):
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex` -- Harmonies 1, 5.
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3e_bkm_chapter.tex` -- Harmonies 2, 3, 4, 8.
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex` -- Harmony 6.
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/cy_d_kappa_stratification.tex` -- Harmonies 9, 10.
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/six_d_hcs_feynman_coefficients.tex` -- Harmony 7.
- `/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex` -- AP5 cross-references for Harmonies 3, 4.

End of harmonies synthesis.
