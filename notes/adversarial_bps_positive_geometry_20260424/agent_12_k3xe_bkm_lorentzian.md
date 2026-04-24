# Agent 12: K3xE/BKM Lorentzian and Automorphic Boundary

Scope: non-toric Lorentzian and automorphic-boundary obstruction to extending
toric BPS positive geometry to \(K3 \times E\), the BKM imaginary cone,
\(\Delta_5\), the Mukai lattice, and the four \(\kappa_\bullet\)-invariants.
Owned file only. No manuscript files edited.

Claim attacked:
\[
  \text{toric positive geometry on } \mathbb C^3
  \quad\Longrightarrow\quad
  \text{the same positivity package for } K3\times E,\ \mathfrak g_{\Delta_5}.
\]

Verdict: false as stated. The healed statement is a stratified one. Toric
positivity is the terminal rational-polyhedral degeneration
\[
 \Gamma^+_{\mathrm{eff},\sigma}(X_\Sigma)=\mathbb Z_{\ge 0}^{Q_0},\qquad
 \mathcal M^+_{\mathrm{eff},\sigma}(X_\Sigma)
 =
 \coprod_{\mathbf d\in\mathbb Z_{\ge0}^{Q_0}}
 [\mathrm{Crit}(W_{\mathbf d})/G_{\mathbf d}],
 \qquad
 Y^+_\sigma(X_\Sigma)=\mathrm{CoHA}(Q_\Sigma,W_\Sigma),
\]
where the local model is quiver-critical and the fixed-point/shuffle basis is
terminal. The \(K3\times E\) face is non-toric: its positive half is expected
only after motivic Hall lift and Hall--BKM comparison, and its automorphic
boundary is carried by the Lorentzian Mukai/Humbert lattice
\[
 \widetilde H(K3,\mathbb Z)=\mathrm{II}_{4,20},\qquad
 \Lambda_{\mathrm{Muk}}^{\mathrm{ext}}(K3\times E)
 =\mathrm{II}_{4,20}\oplus U,\qquad
 \Lambda^{3,2}\subset \Lambda_{\mathrm{Muk}}^{\mathrm{ext}}(K3\times E).
\]
The BKM denominator is the Lorentzian product
\[
 e^{-2\pi i(\rho,z)}
 \prod_{\alpha\in\Delta_+}
 (1-e^{-2\pi i(\alpha,z)})^{\mathrm{mult}\,\alpha}
 =
 \frac{1}{64}\Delta_5(2Z),
\]
on the tube over the forward cone
\(\Omega(\mathcal C(\Lambda^{2,1}_{II})_+)\), not a toric shuffle product.

Local anchors read:

- `chapters/theory/quantum_groups_foundations.tex:15-203`: effective BPS
  positive geometry, positive half, conditional double, toric terminal
  degeneration, and equivariance stratification.
- `chapters/theory/quantum_groups_foundations.tex:4445-4599`: \(K3\times E\)
  reduced DT character, conditional Hall--BKM positive-half comparison, and
  \(E_1\)-not-\(E_2\) \(\Phi_3\) output.
- `chapters/theory/quantum_groups_foundations.tex:4671-4804`: Mukai lattice
  \(\mathrm{II}_{4,20}\), extended \(K3\times E\) lattice
  \(\mathrm{II}_{4,20}\oplus U\), and Humbert restriction
  \(\Lambda^{3,2}\).
- `chapters/theory/quantum_groups_foundations.tex:6277-6472`: terminal
  \(\mathrm{Perf}(\mathbb C^3)\) MO-residue vanishing and toric
  localisation, with non-trivial \(\kappa_{\mathrm{BKM}}\) only on the
  non-toric Lorentzian face.
- `chapters/examples/k3e_cy3_programme.tex:1215-1327`: chain-level
  Hodge-supertrace derivation and three-path triangulation of
  \(\kappa_{\mathrm{BKM}}(\mathfrak g_{\Delta_5})=5\).
- `chapters/examples/k3e_cy3_programme.tex:1338-1393`: \(24\) Kodaira
  curve-stalks and quasi-NCCR character
  \(-\Phi_{10}^{-1}=-\Delta_5^{-2}\).
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:2778-2895`: Humbert
  divisors, \(\mathcal L^{\Delta_5}\), monodromy orders \(8,16\), and
  \(K^{\kappa_{\mathrm{ch}}}=8\).
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:3449-3521`: Siegel
  character \(1/\Phi_{10}\) and boundary expansions.
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:3757-3800`: BKM roots
  as BPS decay walls and imaginary-root multiplicities.
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:6313-6608`: restriction
  \(\Phi_{10}=\Delta_5^2\) and Baily--Borel--Freitag four-stratum
  automorphic boundary.
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:7130-7223`: four
  \(\kappa_\bullet(K3\times E)\) values, curve-stalks, quasi-NCCR
  character, rank-\(23\) Cartan, Humbert order \(8\), and construction-grade
  stratification.
- `chapters/examples/cy_d_kappa_stratification.tex:34-185`: definitions of
  the four main \(\kappa_\bullet\)-invariants, canonical \(K3\times E\)
  spectrum, and failure of the additive decomposition.
- `chapters/examples/cy_d_kappa_stratification.tex:2018-2287`: universal
  \(\kappa_{\mathrm{BKM}}(\Phi_N)=c_N(0)/2\), \(\Delta_5\) value \(5\),
  and direct falsification of
  \(\kappa_{\mathrm{BKM}}=\kappa_{\mathrm{ch}}+\chi(\mathcal O_{\mathrm{fiber}})\).
- `chapters/examples/cy_d_kappa_stratification.tex:2529-2668`: WKB
  denominator identity for \(\mathfrak g_{\Delta_5}\) and the imaginary
  cone.
- `chapters/examples/cy_d_kappa_stratification.tex:3048-3099`: Mukai doubling
  \(K^{\kappa_{\mathrm{ch}}}=8\) and the Lusztig--Humbert stratum.
- `chapters/examples/cy_d_kappa_stratification.tex:3650-3810`: Gritsenko--
  Clery census and five-entry programme restriction.
- `chapters/examples/cy_d_kappa_stratification.tex:3964-4255`: chain-level
  master identity and the \(N=1\) flagship
  \(\kappa_{\mathrm{BKM}}(\Delta_5)=5\).

## ATTACK/HEAL 1: toric terminal positivity does not globalise to K3xE

Attack. The toric formula
\[
 \Gamma^+_{\mathrm{eff},\sigma}=\mathbb Z_{\ge0}^{Q_0},\qquad
 Y^+_\sigma=\mathrm{CoHA}(Q,W)
\]
tempts one to cover \(K3\times E\) by toric \(\mathbb C^3\)-charts and
sum the positive halves. This loses the period-domain equivariance and the
Lorentzian lattice. It also replaces \(24\) Kodaira curve-stalks by \(24\)
smooth points.

Heal. The toric statement is terminal, not universal. On a toric CY3 the
fan/quiver package is the rational-polyhedral collapse of
\(\mathfrak P^{\mathrm{BPS}}_\sigma(X)\). On \(K3\times E\), the relevant
local singular data are
\[
 F_p\times E,\qquad p\in\Delta,\qquad |\Delta|=24,
\]
with completed local ring
\[
 \widehat{\mathcal O}_{K3\times E,(p,q)}
 \simeq \mathbb C[[x_1,x_2,z]]/(x_1x_2),
\]
a nodal \(A_1\)-curve times an elliptic direction, not
\(\mathbb C[[x_1,x_2,z]]\). The correct local slogan is:
\[
 \text{curve-stalk CoHA of }(I_1\times E)
 \neq 24\cdot\mathrm{CoHA}(\mathbb C^3).
\]
Anchors: `k3e_cy3_programme.tex:1338-1365`,
`k3_chiral_bialgebra_platonic.tex:7148-7159`,
`quantum_groups_foundations.tex:129-170`.

## ATTACK/HEAL 2: the CoHA positive half is not the full BKM algebra

Attack. The character-level identity
\[
 \mathrm{Poinc}(\mathrm{CoHA}(K3\times E))\stackrel{?}{=}\Delta_5^{-2}
\]
can be over-read as
\[
 \mathrm{CoHA}(K3\times E)=\mathfrak g_{\Delta_5}
\]
or as a VOA statement. This repeats the local error
\(\mathrm{CoHA}(\mathbb C^3)=\mathcal W_{1+\infty}\).

Heal. The local model fixes the grammar:
\[
 \mathrm{CoHA}(\mathbb C^3)=Y^+(\widehat{\mathfrak{gl}}_1)
 \hookrightarrow
 Y(\widehat{\mathfrak{gl}}_1)
 \xrightarrow{\mathrm{ev}_\lambda}
 \mathrm{End}(\mathcal W_{1+\infty}[\lambda]\text{-vac}).
\]
For \(K3\times E\) the conditional comparison is only
\[
 \mathrm{CoHA}(K3\times E)
 \simeq
 U\bigl(Y^+(\mathfrak g_{\Delta_5})\bigr)_{\mathrm{num}},
 \qquad
 \mathrm{Lie}\,\mathrm{CoHA}(K3\times E)=Y^+(\mathfrak g_{\Delta_5}),
\]
after the motivic Hall lift and Hall--BKM comparison. The full algebra is
recovered only after adjoining Cartan and negative roots:
\[
 \mathfrak g_{\Delta_5}=Y^-\oplus\mathfrak h\oplus Y^+,\qquad
 D(Y^+(\mathfrak g_{\Delta_5}))
 =
 U_q(\mathfrak g_{\Delta_5})^{\mathrm{Hall}}.
\]
The \(\Phi_3\) output is \(E_1\)-chiral, not a VOA; the \(E_2\)-data lives
on the Drinfeld centre of the \(E_1\)-representation category. Anchors:
`quantum_groups_foundations.tex:545-568,4445-4599,4623-4650`,
`k3_chiral_bialgebra_platonic.tex:7207-7223`.

## ATTACK/HEAL 3: MO walls are not BKM Lorentzian walls

Attack. The Maulik--Okounkov residue
\[
 R^{\mathrm{MO}}(u)=\mathrm{Res}_{u=u_\star}\phi^+_{\mathrm{UV}}(u)
\]
on a toric chamber can be confused with the Borcherds wall residue that
produces \(\Delta_5\). On \(\mathbb C^3\) this would assign a nonzero
\(\kappa_{\mathrm{BKM}}\) to the toric terminal chart.

Heal. The walls live in different spaces. For \(\mathbb C^3\), the
Schiffmann--Vasserot shuffle/MO wall is a coordinate hyperplane in the
positive-definite equivariant parameter plane. The BKM wall is a real-root
hyperplane
\[
 W_{\mathrm{BKM}}(\alpha)=\{Z:(\alpha,Z)=0\}
\]
in a Lorentzian tube domain. The terminal-lattice base case has
\[
 K^{\mathrm{num}}_0(\mathrm{Perf}(\mathbb C^3))=\mathbb Z
\]
with degenerate Mukai pairing, no canonical Lorentzian sublattice, and
\[
 \Phi_{\Lambda=0}=1,\qquad
 c_{\mathrm{triv}}(0)=0,\qquad
 \kappa_{\mathrm{BKM}}^{\mathrm{MO}}(\mathbb C^3)=0.
\]
Thus toric localisation contributes zero to the BKM weight:
\[
 \kappa_{\mathrm{BKM}}^{\mathrm{MO}}(X)
 =
 \sum_{F\subset X^T}
 \frac{\mathrm{Res}_F(\text{trivial-lattice BKM integrand})}{e_T(N_{F/X})}
 +
 \kappa_{\mathrm{BKM}}^{\mathrm{non-toric}}(X),
\]
and the \(K3\times E\) value
\(\kappa_{\mathrm{BKM}}(\Delta_5)=5\) is entirely in the non-toric
Lorentzian Mukai face. Anchors:
`quantum_groups_foundations.tex:6277-6472`.

## ATTACK/HEAL 4: Delta_5 is not a toric shuffle character

Attack. Since the toric positive half has a shuffle presentation, one might
try to read \(\Delta_5\) as a global shuffle character. This erases the
automorphic denominator and the imaginary cone.

Heal. \(\Delta_5\) is the Borcherds denominator of a Lorentzian BKM:
\[
 \Phi(z)=
 \sum_{w\in W^{(2)}}\det(w)
 \left[
 e^{-2\pi i(w(\rho),z)}
 -
 \sum_{a\in\Lambda^{2,1}_{II}\cap\mathbb R_{>0}\mathcal P_{II}}
 m(a)e^{-2\pi i(w(\rho+a),z)}
 \right]
\]
\[
 =
 e^{-2\pi i(\rho,z)}
 \prod_{\alpha\in\Delta_+}
 (1-e^{-2\pi i(\alpha,z)})^{\mathrm{mult}\,\alpha}
 =
 \frac{1}{64}\Delta_5(2Z).
\]
The positive roots lie in
\(\mathcal C(\widetilde{\Lambda^{2,1}_{II}})_+\), and the product
converges on
\[
 \Omega(\mathcal C(\Lambda^{2,1}_{II})_+)
 =
 \Lambda^{2,1}_{II}\otimes\mathbb R
 + i\,\mathcal C(\Lambda^{2,1}_{II})_+.
\]
The imaginary multiplicities are Fourier coefficients of the K3 weak
Jacobi form:
\[
 \mathrm{mult}(n f_2+l f_3+m f_{-2})
 =
 f_{0,1}(nm,l),\qquad
 4nm-l^2=(\alpha,\alpha).
\]
This is Lorentzian automorphic product theory, not toric shuffle
enumeration. Anchors:
`cy_d_kappa_stratification.tex:2529-2668`,
`k3_chiral_bialgebra_platonic.tex:3757-3800`.

## ATTACK/HEAL 5: the automorphic boundary is Baily--Borel--Humbert, not a toric fan boundary

Attack. A toric fan has cones and boundary strata. It is tempting to identify
the boundary of the \(K3\times E\) BPS positive geometry with an analogous
fan boundary.

Heal. The boundary relevant to \(\Delta_5\) is the Baily--Borel--Freitag
stratification of \(\overline{\mathcal A_2}\) and its metaplectic cover:
interior, Klingen cusp, Humbert divisor, and metaplectic branch. The
Humbert divisors \(H_1,H_4\) carry the regular-singular
\(\mathcal D\)-module
\[
 \mathcal L^{\Delta_5}
 =
 \bigl(\mathcal O_{\overline{\mathcal A_2}\setminus(H_1\cup H_4)}
 \cdot\log\Delta_5\bigr)\otimes_{\mathcal O}
 \mathcal D_{\overline{\mathcal A_2}},
 \qquad
 \nabla(\log\Delta_5)=\frac{d\Delta_5}{\Delta_5}.
\]
The local monodromy orders are
\[
 \mathrm{ord}(\mathrm{mon}_{H_1}\mathcal L^{\Delta_5})=8,\qquad
 \mathrm{ord}(\mathrm{mon}_{H_4}\mathcal L^{\Delta_5})=16.
\]
The order \(8\) is the same Heegner Chern-class datum as the Mukai
doubling and Lusztig specialisation:
\[
 K^{\kappa_{\mathrm{ch}}}
 =
 2c_+(\widetilde H(K3,\mathbb Z))
 =
 2\cdot 4
 =
 8,\qquad
 \hbar^2 K^{\kappa_{\mathrm{ch}}}=-1.
\]
No toric boundary construction sees this Chern-class torsion. Anchors:
`k3_chiral_bialgebra_platonic.tex:2778-2895,6336-6608,7194-7205`,
`cy_d_kappa_stratification.tex:3048-3099`.

## ATTACK/HEAL 6: Mukai rank 24, Cartan rank 23, and kappa_fiber are distinct

Attack. The numbers \(24\), \(23\), and \(2\) can be collapsed into a single
"K3 rank" invariant, especially if one tries to force a toric vertex-count
interpretation.

Heal. They are different objects.
\[
 \kappa_{\mathrm{fiber}}(K3\times E)=24
 =
 \mathrm{rk}\,\widetilde H(K3,\mathbb Z)
 =
 \mathrm{rk}(H^0\oplus H^2\oplus H^4).
\]
The BKM Cartan rank is instead
\[
 23=22+1:
 \qquad
 \mathrm{II}_{4,20}/U\simeq \mathrm{II}_{3,19}
 \text{ gives }22,
 \quad
 \Lambda_{24}\text{ gives one Leech/Niemeier addback}.
\]
The fibre categorical value
\[
 \kappa_{\mathrm{cat}}(K3)=\chi(\mathcal O_{K3})=2
\]
is neither the Mukai rank nor the \(K3\times E\) total-space categorical
value. It is the source of the false \(2+3=5\) mnemonic and must not be
used as a \(K3\times E\) invariant. Anchors:
`k3e_cy3_programme.tex:1395-1403`,
`k3_chiral_bialgebra_platonic.tex:7180-7191`,
`cy_d_kappa_stratification.tex:131-153`.

## ATTACK/HEAL 7: the four kappa invariants do not add to Delta_5

Attack. The apparent arithmetic
\[
 5=2+3
\]
can be upgraded falsely to
\[
 \kappa_{\mathrm{BKM}}
 =
 \kappa_{\mathrm{ch}}+\chi(\mathcal O_{\mathrm{fiber}}).
\]
It also collides with an AGENTS essential-constants line listing
\(\{2,3,5,24\}\) as a \(K3\times E\) spectrum.

Heal. The canonical chapter and theorem-grade master-example statement give
\[
 \{\kappa_{\mathrm{cat}},
   \kappa_{\mathrm{ch}}^{\mathrm{Heis}},
   \kappa_{\mathrm{BKM}}(\mathfrak g_{\Delta_5}),
   \kappa_{\mathrm{fiber}}\}(K3\times E)
 =
 \{0,3,5,24\}.
\]
The entries are construction-distinct:
\[
 \kappa_{\mathrm{cat}}(K3\times E)
 =
 \chi(\mathcal O_{K3})\chi(\mathcal O_E)
 =
 2\cdot 0
 =
 0,
\]
\[
 \kappa_{\mathrm{ch}}(K3\times E)
 =
 \sum_{q=0}^3(-1)^q h^{0,q}(K3\times E)
 =
 1-1+1-1
 =
 0,
\]
while the Heisenberg--Mukai Stage-2 specialisation gives
\[
 \kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3\times E)=3.
\]
The BKM value is automorphic:
\[
 \kappa_{\mathrm{BKM}}(\Delta_5)
 =
 \frac{c_1(0)}{2}
 =
 \frac{10}{2}
 =
 5,
\]
and the fibre rank is
\[
 \kappa_{\mathrm{fiber}}(K3\times E)=24.
\]
The additive identity fails already at \(N=1\):
\[
 \kappa_{\mathrm{BKM}}(\Delta_5)=5
 \neq
 \kappa_{\mathrm{ch}}(K3\times E)+\chi(\mathcal O_E)=0+0=0,
\]
and at \(N=2\):
\[
 c_2(0)/2=4\neq 1+0.
\]
Thus the note should use \(\{0,3,5,24\}\); the value \(2\) is only the K3
fibre \(\kappa_{\mathrm{cat}}(K3)\). Anchors:
`cy_d_kappa_stratification.tex:34-64,131-185,2018-2116,2274-2287`,
`k3_chiral_bialgebra_platonic.tex:7135-7145`.

## ATTACK/HEAL 8: Phi_10 and Delta_5 mark a genus-2 automorphic shadow, not a stronger toric theorem

Attack. Since the derived character is
\[
 -\Phi_{10}^{-1}=-\Delta_5^{-2},
\]
one may claim the full \(K3\times E\) bialgebra is theorem-grade or that
\(\Delta_5\) is itself the character of a VOA.

Heal. The status stratifies:
\[
 Z^{\mathrm{red}}_{\mathrm{DT}}(K3\times E)
 =
 -\Phi_{10}^{-1}
 =
 -\Delta_5^{-2}
\]
is theorem-grade at character level by Oberdieck--Pandharipande plus
Gritsenko--Nikulin. The full bialgebra assertion
\[
 \mathcal A^{\mathrm{M},\Omega}_{\mathrm{prot}}(K3\times E)
 \cong
 Y_\hbar^{\mathrm{super}}(\mathfrak g_{\Delta_5})
 =
 D(\mathrm{CoHA}(K3\times E))
\]
is conjectural. The genus-2 character statement is
\[
 \mathrm{Ch}(\mathbf H_{\Delta_5})(Z)=\frac{1}{\Phi_{10}(Z)},
\]
with boundary expansions
\[
 \frac{1}{\Phi_{10}(Z)}
 =
 \frac{p^{-1}}{\phi_{10,1}(\tau,z)}+O(p^0),
 \qquad
 \frac{1}{\Phi_{10}(Z)}
 =
 -\frac{1}{4\pi^2z^2\eta(\tau)^{24}\eta(\sigma)^{24}}+O(z^0).
\]
The first is the Fourier--Jacobi cusp; the second is the separating
degeneration. Neither is a toric fan boundary, and neither upgrades the
\(E_1\)-chiral \(K3\times E\) output to a VOA. Anchors:
`k3e_cy3_programme.tex:1367-1393`,
`k3_chiral_bialgebra_platonic.tex:3449-3521,7162-7178,7207-7223`,
`quantum_groups_foundations.tex:4806-4935`.

## Healed Integration Statement

Use the following sentence if this axis is integrated into a synthesis:

Toric positivity supplies the terminal local model
\(Y^+_\sigma(X_\Sigma)=\mathrm{CoHA}(Q_\Sigma,W_\Sigma)\) and the
\(\mathbb C^3\) positive half \(Y^+(\widehat{\mathfrak{gl}}_1)\), but the
\(K3\times E\) BKM face is the non-toric Lorentzian/Humbert boundary:
its \(24\) inputs are Kodaira curve-stalks \(F_p\times E\), its automorphic
denominator is
\[
e^{-2\pi i(\rho,z)}
\prod_{\alpha\in\Delta_+}
(1-e^{-2\pi i(\alpha,z)})^{\mathrm{mult}\,\alpha}
=\Delta_5(2Z)/64,
\]
its character-level theorem is
\(-\Phi_{10}^{-1}=-\Delta_5^{-2}\), and its four construction-distinct
invariants are
\[
\{\kappa_{\mathrm{cat}},\kappa_{\mathrm{ch}}^{\mathrm{Heis}},
\kappa_{\mathrm{BKM}},\kappa_{\mathrm{fiber}}\}
=
\{0,3,5,24\}.
\]
The full Hall--BKM bialgebra comparison remains conditional/conjectural
beyond character level.

## Status Recommendation

- Safe theorem-grade statements: toric terminal positive half on constructed
  toric Hall loci; \(24\) curve-stalk distinction; \(\Phi_{10}=\Delta_5^2\);
  \(\kappa_{\mathrm{BKM}}(\Delta_5)=c_1(0)/2=5\); four-value
  \(K3\times E\) package \(\{0,3,5,24\}\); Humbert \(H_1\) monodromy
  order \(8\) within its cited theorem.
- Conditional statements: \(\mathrm{CoHA}(K3\times E)\simeq
  U(Y^+(\mathfrak g_{\Delta_5}))_{\mathrm{num}}\); Drinfeld double
  comparison; motivic lift beyond numerical DT character.
- Reject: any manuscript or synthesis line saying toric positivity extends
  unchanged to \(K3\times E\), that \(K3\times E\) is \(24\) copies of
  \(\mathbb C^3\), that \(\mathrm{CoHA}(K3\times E)=\mathfrak g_{\Delta_5}\),
  that \(\Delta_5\) is a VOA character, or that
  \(\kappa_{\mathrm{BKM}}=\kappa_{\mathrm{ch}}+\chi(\mathcal O_{\mathrm{fiber}})\).

Verification: local source read and targeted `rg`/`nl` anchor checks only.
No build run; no manuscript file touched.
