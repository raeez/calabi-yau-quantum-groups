# Hall/Borcherds Gate: Attack-Heal Report

## Scope

Owned surface:

- `notes/swarm_20260424_remaining/agent_3_hall_borcherds_attack_heal.md`
- `compute/lib/hall_borcherds_gate.py`
- `compute/tests/test_hall_borcherds_gate.py`

No chapter file is edited.  The live chapter anchors used here are:

- `chapters/theory/cy_to_chiral.tex`, subsection "K3 x E as the
  primary specialisation", where the principal-locus comparison is
  stated and the global hCS-to-Hall and Hall-Borcherds maps remain
  named extension obligations.
- `chapters/examples/k3e_bkm_chapter.tex`, sections on
  $\Delta_5$, $\Phi_{10}=\Delta_5^2$, root multiplicities, reduced DT,
  and the four $K3 \times E$ invariants.
- `chapters/examples/cy_d_kappa_stratification.tex`, canonical
  spectrum
  $(\kappa_{\mathrm{cat}},\kappa_{\mathrm{ch}}^{\mathrm{Heis}},
  \kappa_{\mathrm{BKM}},\kappa_{\mathrm{fiber}})=(0,3,5,24)$.

## RED: first-principles attack

The wanted global strengthening is not a map from the local
$\mathbb C^3$ normal form to $\mathfrak g_{\Delta_5}$.  It is a
comparison between five different structures.

1. **Oriented critical CoHA.**  One must construct an oriented critical
   cohomological Hall algebra
   \[
     Y^+_{\mathrm{crit}}(X,\sigma)
     = H^\bullet_{\mathrm{eq}}\bigl(\mathcal M_{\mathrm{eff}}(X),
       \varphi_W,\mathrm{or}_\sigma\bigr)
   \]
   with a specified $(-1)$-shifted orientation line, extension product,
   coproduct correspondence, and stability/chamber control.  For
   $\mathbb C^3$ the result is the positive half
   $Y^+(\widehat{\mathfrak{gl}}_1)$; it is not
   $\mathcal W_{1+\infty}$.

2. **Hall-Drinfeld double.**  Passing from the positive half to the
   full object requires a non-degenerate Hall pairing and a completed
   Drinfeld double:
   \[
     D_\hbar(Y^+_{\mathrm{crit}}(K3\times E)).
   \]
   This is the K3 BKM-side object.  It is not a strict Drinfeld
   Yangian.  The double carries Manin-pair, quasi-Hopf, coproduct,
   associator, and $R$-matrix data.

3. **Borcherds denominator datum.**  The BKM side is not specified by
   a weight alone.  It requires a lattice and denominator package:
   \[
     (L,\mathcal C,\rho,f,\Psi_f)
     =
     (\Lambda^{2,1}_{II},\mathcal P_{II},\rho,\phi_{0,1},\Delta_5).
   \]
   The normalisation is primitive:
   \[
     \Delta_5=\mathrm{BorLift}(\phi_{0,1}),\qquad
     \kappa_{\mathrm{BKM}}(\Delta_5)=c_1(0)/2=10/2=5.
   \]
   The Igusa form is the square,
   \[
     \Phi_{10}=\Delta_5^2,\qquad \mathrm{wt}(\Phi_{10})=10.
   \]
   Confusing $\Phi_{10}$ with the primitive BKM denominator shifts the
   weight by a factor of two.

4. **Root multiplicity lane.**  A denominator-weight theorem does not
   construct the Hall comparison.  The bridge needs a charge-lattice map
   \[
     \Gamma_{\mathrm{Hall}}(K3\times E)\longrightarrow
     \Lambda^{2,1}_{II}
   \]
   and a coefficient oracle identifying primitive roots by
   \[
     \mathrm{mult}_{\mathfrak g_{\Delta_5}}(\alpha)
       = c_{\phi_{0,1}}(4nm-\ell^2)
       \quad(\alpha=(n,\ell,m),\ \gcd(n,\ell,m)=1),
   \]
   with a separate imprimitive divisor-sum lane.  The Hall/DT equality
   then requires the oriented Behrend-weighted reduced DT comparison,
   not only the Borcherds product.

5. **K3xE spectrum.**  The four values
   \[
     (0,3,5,24)
   \]
   are four invariant lanes:
   $\kappa_{\mathrm{cat}}(K3\times E)=0$ by Kunneth on the total space;
   $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}=3$ from the Heisenberg-Mukai
   specialisation; $\kappa_{\mathrm{BKM}}(\Delta_5)=5$ by Borcherds
   weight; $\kappa_{\mathrm{fiber}}=24$ from the Mukai lattice.  The
   spectrum is a consistency check, not a construction of the double.

## BLUE: exact failure modes

- **Local chart overreach.**  The $\mathbb C^3$ chart gives
  $\mathrm{CoHA}(\mathbb C^3)=Y^+(\widehat{\mathfrak{gl}}_1)$.
  It does not produce a compact $K3\times E$ oriented CoHA, a Hall
  pairing, or a Borcherds denominator.

- **Positive half equals full algebra.**  False.  $Y^+$ is the positive
  Hall half.  The full object requires Drinfeld double / center /
  evaluation data.

- **BKM as Yangian.**  False.  The K3 BKM object is the
  Hall-Drinfeld double of the K3xE CoHA/BKM Manin-pair datum, not a
  strict Drinfeld Yangian with finite-rank $J$-presentation.

- **Weight theorem as bridge theorem.**  False.  Borcherds' theorem
  gives $\mathrm{wt}(\Psi_f)=c_0(0)/2$.  It does not construct the
  oriented critical CoHA, the Hall pairing, or the root-graded
  comparison functor.

- **$\kappa_{\mathrm{BKM}}$ from additive Euler data.**  False as a
  structural formula.  The $N=1$ equality
  $5=3+2$ is a Heisenberg-fibre coincidence; the theorem-level formula
  is $\kappa_{\mathrm{BKM}}(\Phi_N)=c_N(0)/2$.

- **Six routes as six $\Phi$ applications.**  False.  The routes to
  $G(K3\times E)$ are distinct constructions/specialisation data, not
  repeated applications of one $\Phi_3$ output.

## GREEN: healed theorem package

### Theorem A: denominator normalisation

**Status: proved, local to the Borcherds denominator lane.**

With the primitive Gritsenko-Nikulin normalisation,
\[
  \Delta_5=\mathrm{BorLift}(\phi_{0,1}),
  \qquad c_1(0)=10,
  \qquad \kappa_{\mathrm{BKM}}(\Delta_5)=5.
\]
The physical/reduced-DT denominator uses
\[
  \Phi_{10}=\Delta_5^2,\qquad \mathrm{wt}(\Phi_{10})=10.
\]
Thus the primitive BKM weight is attached to $\Delta_5$, while
$1/\Phi_{10}=1/\Delta_5^2$ is the squared counting denominator.

### Theorem B: typed Hall/Borcherds gate

**Status: conditional.**

Let $X=K3\times E$.  Suppose the following data are constructed:

1. an oriented critical CoHA
   $Y^+_{\mathrm{crit}}(X,\sigma)$ with extension product and shuffle
   coproduct;
2. a non-degenerate Hall pairing making the completed positive and
   negative halves into a Manin-pair input;
3. the completed Hall-Drinfeld double
   $D_\hbar(Y^+_{\mathrm{crit}}(X,\sigma))$;
4. a Borcherds denominator datum
   $(\Lambda^{2,1}_{II},\mathcal P_{II},\rho,\phi_{0,1},\Delta_5)$
   with the primitive normalisation of Theorem A;
5. a root-graded charge map from Hall/DT charges to
   $\Lambda^{2,1}_{II}$, identifying primitive multiplicities with
   Jacobi coefficients and imprimitive multiplicities through the
   divisor-sum lane;
6. compatibility of coproduct, associator, and $R$-matrix under the
   Stage-2 specialisation to $E$;
7. separation of the four K3xE invariant lanes
   $(0,3,5,24)$.

Then there is a root-completed filtered comparison
\[
  \Theta_{\mathrm{Hall}\to\mathrm{Borch}}\colon
  \widehat{D_\hbar(Y^+_{\mathrm{crit}}(K3\times E))}
  \longrightarrow
  \widehat{\mathbf H}_{\Delta_5}
\]
whose primitive Lie super-bialgebra shadow is
\[
  \mathrm{Prim}\,\widehat{D_\hbar(Y^+_{\mathrm{crit}}(K3\times E))}
  \longrightarrow
  \mathfrak g_{\Delta_5}.
\]
It preserves the root grading, sends the Hall denominator character to
$\Delta_5^{-1}$ in the primitive lane, sends the reduced-DT counting
character to $\Phi_{10}^{-1}=\Delta_5^{-2}$ in the squared lane, and
recovers $\kappa_{\mathrm{BKM}}(\Delta_5)=5$ from $c_1(0)/2$.

This is the strongest true package: it is a theorem from the listed
witnesses, not a theorem that the witnesses already exist globally.

### Proposition C: root multiplicity lane

**Status: conditional on the coefficient and Hall/DT witnesses.**

For a primitive charge $\alpha=(n,\ell,m)$ mapped into
$\Lambda^{2,1}_{II}$, the multiplicity key is
\[
  D(\alpha)=4nm-\ell^2.
\]
The multiplicity claim is not the integer $D(\alpha)$ itself.  It is
the value of the chosen K3 elliptic-genus coefficient oracle at that
key, with the sign/parity convention fixed by the Borcherds product.
For imprimitive $\alpha$, the divisor-sum formula is a separate lane and
cannot be replaced by the primitive coefficient.

## Compute gate

Added `compute/lib/hall_borcherds_gate.py` and
`compute/tests/test_hall_borcherds_gate.py`.

The gate verifies:

- $c_1(0)=10$ gives $\kappa_{\mathrm{BKM}}(\Delta_5)=5$.
- $\Phi_{10}$ has weight $10$, distinct from primitive
  $\kappa_{\mathrm{BKM}}(\Delta_5)$.
- The K3xE spectrum is exactly $(0,3,5,24)$.
- The denominator-weight check alone leaves the Hall/Borcherds gate
  open.
- The gate closes only if all typed witnesses are supplied.
- Primitive root multiplicity code returns the discriminant key and
  refuses imprimitive roots rather than guessing a coefficient.
- All known shortcuts are rejected.

## Integration recommendation

Do not edit `chapters/theory/cy3_chain_level_bridge.tex` from this
lane.  The integration owner should add one boxed "Hall/Borcherds gate"
paragraph near the CY3 bridge theorem, with this status:

\[
\text{local }\mathbb C^3/Y^+\text{ bridge proved on charts;}
\quad
\text{principal }K3\times E/\Delta_5\text{ comparison conditional;}
\quad
\text{global Hall/Borcherds map open.}
\]

The paragraph should cite the typed witness list above and explicitly
forbid the four shortcuts: $Y^+=\mathcal W_{1+\infty}$, BKM-as-Yangian,
$\Phi_{10}$-weight-as-$\kappa_{\mathrm{BKM}}$, and additive
$\kappa_{\mathrm{BKM}}$.
