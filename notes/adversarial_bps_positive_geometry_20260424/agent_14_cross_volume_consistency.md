# Agent 14: Cross-Volume Consistency Audit

Object attacked: chambered effective BPS positive geometry.

Files changed: this report only.

Verification surface: `CLAUDE.md`, `AGENTS.md`,
`chapters/theory/quantum_groups_foundations.tex`,
`chapters/theory/cy_to_chiral.tex`,
`chapters/examples/cy_d_kappa_stratification.tex`,
`chapters/examples/coha_wall_crossing_platonic.tex`, Vol I
`chapters/examples/landscape_census.tex`, Vol II
`chapters/connections/programme_climax_platonic.tex`,
`chapters/connections/spectral-braiding-core.tex`,
`chapters/examples/examples-worked.tex`, `FRONTIER.md`, `README.md`,
and Vol II `main.tex`.

Global verdict: compatible only in the scoped form below.  The chambered
datum is a CY3 Hall/vanishing-cycle positive half
\[
  Y^+_\sigma(X)=H^\bullet_{\mathrm{eq}}(\mathcal M^+_{\mathrm{eff},\sigma}(X),\phi_W)
\]
with conditional Drinfeld double
\[
  G_\sigma(X)=D(Y^+_\sigma(X))
  =Y^+_\sigma(X)\bowtie Y^0_\sigma(X)\bowtie Y^-_\sigma(X).
\]
It is not a replacement for Vol I scalar \(\kappa\)/\(r(z)\) data, not
an intrinsic \(E_3\)-topological theory, not a direct curve-level
\(\Phi_d\), not \(\mathcal W_{1+\infty}\) before doubling and
representation, and not a plain K3 Yangian on the K3 x E BKM lane.

## Cycle 1 - Vol I \(\kappa/r(z)\) Compatibility

Attacked claim: \(Y^+_\sigma(X)\) is the cross-volume source of the Vol I
landscape scalar \(\kappa\) and the spectral \(r(z)\).

Conflict or compatibility: conflict if read literally.  Vol I defines
the modular Koszul triple as
\[
  \mathfrak T=(\mathcal A,\mathcal A^!,r(z)),
\]
with examples such as \((\mathcal H_\kappa,\operatorname{Sym}^{ch}(V^*),
\kappa/z)\), \((\widehat{\mathfrak g}_k,\widehat{\mathfrak g}_{-k-2h^\vee},
k\Omega_{\mathrm{tr}}/z)\), and Virasoro
\(\frac{c}{2z^3}+\frac{2T}{z}\).  These are chiral/OPE-side data.
Vol I also states that central charges and \(\kappa\) are not defined
for \(E_1\)-chiral Yangians in the same sense as for vertex algebras.
Vol III \(Y^+_\sigma(X)\) is instead equivariant vanishing-cycle
cohomology of effective BPS moduli with Hall product.

Healed wording/theorem: "The chambered effective BPS geometry supplies
the Hall positive half.  A Vol I modular Koszul triple is obtained only
after a constructed Stage-2 chiral shadow \(A_X\) or a boundary HT model
has been fixed; \(r(z)\) is then the SC\(^{ch,top}\)/boundary-line
spectral \(R\)-matrix infinitesimal, not a scalar invariant of
\(\mathfrak P^{BPS}_\sigma(X)\) itself."

Local anchors: `quantum_groups_foundations.tex:80-113`,
`cy_to_chiral.tex:147-162`.

Cross-volume anchors: Vol I `landscape_census.tex:360-400`,
`landscape_census.tex:1062-1096`; Vol II
`spectral-braiding-core.tex:167-230`, `spectral-braiding-core.tex:286-306`.

Remaining obstruction: the comparison map from the BPS Hall positive
half to a specific chiral algebra remains explicit only on constructed
loci; for general compact CY3 chambers it is a proof obligation, not a
definition.

Claim-status recommendation: Conditional for general cross-volume
\(Y^+\to(\mathcal A,\mathcal A^!,r(z))\); ProvedElsewhere/constructed
only on the standard Hall/HT examples where the boundary algebra and
propagator are fixed.

## Cycle 2 - Vol II \(E_3\)/HT Topological Field Theory

Attacked claim: chambered positive geometry is already the Vol II
\(E_3\)-topological HT QFT.

Conflict or compatibility: conflict if the \(E_3\) structure is placed
on \(Y^+_\sigma(X)\) directly.  Vol II's master theorem sends a chiral
algebra \(A\) to an HT QFT with boundary \(A\), bulk
\[
  Z^{\mathrm{der}}_{\mathrm{ch}}(A),
\]
and SC\(^{ch,top}\)-brace interaction; topologisation by a non-critical
conformal vector promotes the SC\(^{ch,top}\) pair to \(E_3\)-topological.
Vol III at \(d\ge 3\) places \(A_\mathcal C\) natively in \(E_1\), with
\(E_2\) braiding on the Drinfeld centre, not on \(A_\mathcal C\).

Healed wording/theorem: "The BPS positive half is the open/Hall boundary
input for the HT interpretation.  The \(E_3\)-topological structure lives
on the Vol II derived-centre bulk \(Z^{\mathrm{der}}_{\mathrm{ch}}(A)\)
after the chiral boundary \(A\), conformal vector, and topologisation
data are fixed."

Local anchors: `cy_to_chiral.tex:46-59`,
`quantum_groups_foundations.tex:205-207`.

Cross-volume anchors: Vol II
`programme_climax_platonic.tex:13-37`,
`programme_climax_platonic.tex:611-625`,
`programme_climax_platonic.tex:1060-1079`; Vol II `README.md:77`.

Remaining obstruction: Vol II status summaries sometimes compress
"weight-completed/pro-object class M" into "chain-level class M".  The
safe import is: classes G/L/C have original-complex chain-level
topologisation where proved; class M original-complex statements remain
open unless the text explicitly moves to the weight-completed ambient.

Claim-status recommendation: Conditional/ambient-qualified for
general \(E_3\)-topological import; ProvedHere only on the named Vol II
non-critical and completed loci.

## Cycle 3 - Two-Stage \(\Phi_d\) Discipline

Attacked claim: \(\Phi_d\) sends a CY category directly to the chambered
chiral quantum group, and different \(\kappa_\bullet\) values are
multiple applications of \(\Phi_d\).

Conflict or compatibility: conflict.  Vol III's proved local discipline
is
\[
  \Phi_d^{(\Sigma_{d-1},C)}
  =\mathrm{Sp}^{ch}_{\Sigma_{d-1},C}\circ\Phi^{FA}_d,
  \qquad
  n(d)=\infty,2,1 \text{ for } d=1,2,d\ge3.
\]
Stage 1 is the holomorphic \(E_d\)-factorisation algebra on \(X\);
Stage 2 is factorisation homology/specialisation along
\((\Sigma_{d-1},C)\).  Distinct chiral shadows of one CY input come from
distinct specialisation data, not repeated functor applications.

Healed wording/theorem: "Chambered effective BPS positive geometry
belongs to the Stage-1/Stage-2 interface: \(Y^+_\sigma(X)\) records the
Hall positive half in a chamber; the chiral quantum group appears after a
specified \(\mathrm{Sp}^{ch}_{\Sigma_{d-1},C}\) specialisation and, when
needed, Drinfeld doubling.  Six K3 x E routes are six constructions or
specialisations, not six \(\Phi_3\)-applications."

Local anchors: `cy_to_chiral.tex:4-43`, `cy_to_chiral.tex:169-212`,
`cy_d_kappa_stratification.tex:14-31`,
`cy_d_kappa_stratification.tex:1343-1424`.

Cross-volume anchors: Vol II `FRONTIER.md:27-40`, Vol II
`CLAUDE.md:535-549`.

Remaining obstruction: full \((\infty,1)\)-functoriality on arbitrary CY
morphisms and global \(G(\mathcal C)\) remain outside the proved object
level.

Claim-status recommendation: ProvedHere only for the two-stage
factorisation on verified loci; Conjectured for arbitrary functoriality
and global quantum-group assembly.

## Cycle 4 - CoHA Positive Half versus \(\mathcal W_{1+\infty}\)

Attacked claim: \(\mathrm{CoHA}(\mathbb C^3)\), \(Y^+_\sigma(\mathbb C^3)\),
and \(\mathcal W_{1+\infty}\) are the same object.

Conflict or compatibility: conflict.  The local toric degeneration gives
\[
  Y^+_\sigma(X_\Sigma)=\mathrm{CoHA}(Q_\Sigma,W_\Sigma),
  \qquad
  Y^+_\sigma(\mathbb C^3)=Y^+(\widehat{\mathfrak{gl}}_1).
\]
The full affine Yangian is obtained by Drinfeld doubling the positive
half through a Hopf pairing.  \(\mathcal W_{1+\infty}\) is a
Fock/vacuum representation target for the full Yangian after evaluation,
not the direct Hall positive half.

Healed wording/theorem: "For \(\mathbb C^3\), the chambered positive
half is \(Y^+(\widehat{\mathfrak{gl}}_1)\).  The chain
\[
Y^+(\widehat{\mathfrak{gl}}_1)\hookrightarrow
Y(\widehat{\mathfrak{gl}}_1)\to
\operatorname{End}(\mathcal W_{1+\infty}[\lambda]\text{-vac})
\]
is an inclusion/doubling/evaluation chain, not an equality of the first
and last terms."

Local anchors: `coha_wall_crossing_platonic.tex:29-38`,
`quantum_groups_foundations.tex:129-169`,
`cy_to_chiral.tex:122-142`, `cy_to_chiral.tex:162`.

Cross-volume anchors: Vol II `examples-worked.tex:4878-4907`; Vol I
`landscape_census.tex:566-568`,
`landscape_census.tex:1094-1096`.

Remaining obstruction: outside \(\mathbb C^3\) and standard toric
no-compact-4-cycle loci, the Hopf pairing and identification with a
specific affine super Yangian require explicit hypotheses.

Claim-status recommendation: ProvedElsewhere for
\(\mathbb C^3\) positive half; Conditional for general toric
identification with a named full Yangian; never label
\(\mathrm{CoHA}=\mathcal W_{1+\infty}\).

## Cycle 5 - K3 x E BKM versus Yangian

Attacked claim: the K3 x E BKM-side object is a plain "K3 Yangian", and
the Vol I/III \(5,8,12,24\) numbers are one invariant in different
notations.

Conflict or compatibility: conflict.  The K3 x E BKM-side object is the
Hall-Drinfeld double with Siegel-Borcherds associator and dynamical
Siegel \(R\)-matrix:
\[
\mathbf H_{\Delta_5}
=\mathcal D_\hbar\bigl(
  \mathcal Y^{\mathrm{Hall}}_\hbar(\mathrm{CoHA}_{K3\times E}),
  \widetilde\Phi^{\mathrm{Sieg-Bor}}_{\mathrm{Sp}_4}[\Phi_{10}/\eta^{24}],
  R_{\mathrm{Sieg,dyn}}
\bigr).
\]
The four K3 x E values are construction-distinct:
\[
 \{\kappa_{\mathrm{cat}},\kappa_{\mathrm{ch}}^{\mathrm{Heis}},
   \kappa_{\mathrm{BKM}},\kappa_{\mathrm{fiber}}\}(K3\times E)
 =\{0,3,5,24\}.
\]
The K3 fibre value \(2\) is not the total-space value.  Vol I's
\(K^{\kappa_{\mathrm{ch}}}=8\) is the Mukai-doubling/conductor face,
not \(\kappa_{\mathrm{BKM}}\).  The Fake-Monster value \(12\) belongs to
the \(\mathrm{II}_{25,1}\) lattice row, not the paramodular
\(\Delta_5\) row.

Healed wording/theorem: "Use 'Hall-Drinfeld double \(\mathbf H_{\Delta_5}\)'
for the BKM-side K3 x E lane.  Reserve 'K3 Yangian' for the historical
self-mirror/Mukai Yangian branch only.  Record
\(\kappa_{\mathrm{BKM}}(\Delta_5)=c_1(0)/2=5\), the conductor
\(K^{\kappa_{\mathrm{ch}}}=8=\operatorname{ord}(H_1)\), and
\(\kappa_{\mathrm{fiber}}=24\) as distinct faces."

Local anchors: `cy_d_kappa_stratification.tex:131-185`,
`cy_d_kappa_stratification.tex:2018-2056`,
`quantum_groups_foundations.tex:6110-6129`.

Cross-volume anchors: Vol I `landscape_census.tex:5255-5323`; Vol II
`FRONTIER.md:50-64`, `FRONTIER.md:88`,
`examples-worked.tex:5632-5642`, `examples-worked.tex:5682-5694`,
`main.tex:1463-1470`.

Remaining obstruction: line-level compatibility between the Hall
coproduct, Siegel-Borcherds associator, and dynamical \(R\)-matrix is
still a construction-level problem; the report does not certify a full
presentation theorem beyond the cited scoped statements.

Claim-status recommendation: ProvedHere/ProvedElsewhere for the
subscripted numerical separation and Borcherds weight formula; avoid
plain-Yangian status labels on the BKM lane; keep presentation-level
claims conditional unless the Hall-Drinfeld associator and \(R\)-matrix
compatibility are explicitly proved.

## Cycle 6 - Status Labels and Scope Hygiene

Attacked claim: the manuscript concept can be labelled ProvedHere as a
general theorem.

Conflict or compatibility: conflict.  Local status already separates:
the positive geometry is a definition; the Drinfeld double theorem is
\(\ClaimStatusConditional\); toric degeneration is
\(\ClaimStatusProvedElsewhere\) on standard toric Hall loci and
conditional in exotic cases; the general effective BPS cone and positive
basis are \(\ClaimStatusConjectured\).  The two-stage \(\Phi_d\) theorem
is ProvedHere only on verified loci with admissible specialisation data.
The global \(G(\mathcal C)\) assembly is explicitly S5/conjectural.

Healed wording/theorem: "The chambered effective BPS positive geometry
package has a tiered status: definition of
\(\mathfrak P^{BPS}_\sigma(X)\); proved/ProvedElsewhere toric Hall
degeneration; Conditional \(G_\sigma(X)=D(Y^+_\sigma(X))\) under
oriented atlas, PBW integrality, and non-degenerate Hall pairing;
Conjectured local finiteness, positive basis, and general compact CY3
construction."

Local anchors: `quantum_groups_foundations.tex:15-78`,
`quantum_groups_foundations.tex:96-126`,
`quantum_groups_foundations.tex:129-187`,
`cy_to_chiral.tex:101-119`.

Cross-volume anchors: Vol II `FRONTIER.md:81-90`,
Vol II `programme_climax_platonic.tex:611-625`,
`programme_climax_platonic.tex:1060-1079`, Vol I
`landscape_census.tex:1760-1820`,
`landscape_census.tex:1928-1948`.

Remaining obstruction: cross-volume summaries should not override local
claim decorators.  If an integration pass imports this concept into
manuscript prose, every claim must name its tier rather than relying on a
single status badge.

Claim-status recommendation: no new ProvedHere label for the general
concept.  Use: Definition; ProvedElsewhere on standard toric Hall loci;
Conditional for the Drinfeld double; Conjectured for general compact CY3
positive bases and global \(G\)-assembly.

## Final Claim-Status Recommendations

1. Definition: \(\mathfrak P^{BPS}_\sigma(X)\) and
   \(Y^+_\sigma(X)\) as chambered effective Hall/vanishing-cycle data.
2. ProvedElsewhere with hypotheses: toric degeneration
   \(Y^+_\sigma(X_\Sigma)=\mathrm{CoHA}(Q_\Sigma,W_\Sigma)\), including
   \(\mathbb C^3\mapsto Y^+(\widehat{\mathfrak{gl}}_1)\).
3. Conditional: \(G_\sigma(X)=D(Y^+_\sigma(X))\) unless the oriented
   critical atlas, Davison-Meinhardt PBW integrality, and non-degenerate
   Serre/Hall pairing have all been constructed.
4. Conjectured: general compact CY3 positive basis
   \(\Theta^{BPS}_\sigma\), general wall-compatible \(Y^+\to A_X\)
   specialisation, and global quantum group \(G(\mathcal C)\).
5. Cross-volume convention: Vol I \(\kappa\)/\(r(z)\) attaches to chiral
   algebra triples after specialisation; Vol II \(E_3\)-topological
   structure attaches to the derived-centre HT bulk; Vol III
   \(\kappa_{\mathrm{BKM}}=c_N(0)/2\) is a Borcherds-weight invariant of
   the BKM denominator lane.

No build run.  Verification was source inspection and targeted
cross-volume grep only.
