# Compact hCS--Hall Resolution Surface

## Claim attacked

The vulnerable claim is that a local hCS normal form, a Hall-side
orientation trivialisation, or a finite torus-fixed \(\mathbb C^3\)
shuffle map is enough to construct the compact oriented comparison
\[
\Theta_{\hCS\to\Hall}^{\mathrm{or}}\colon
\Obs_{\hCS}^{q}(-,\mathfrak g)\to
\CoHA_{\mathrm{crit}}^{\mathrm{or}}(-).
\]

## Resolution

The compact comparison is reduced to a checkable primitive package in
`chapters/theory/cy3_chain_level_bridge.tex`:

- `def:hcs-hall-primitive-witness-package` defines the finite typed
  witness package
  \[
  (\theta^{(0)},\eta_{\mathrm{MC}},\lambda_{\mathrm{or}},
  \eta_{\mathrm{gr}},H_{\mathrm{TS}},H_{\mathrm{fact}},Q).
  \]
- `thm:hcs-hall-primitive-criterion` proves the formal equivalence:
  \(\Theta_{\hCS\to\Hall}^{\mathrm{or}}\) exists on the fixed DWR/Ran
  nerve if and only if the package exists.

The theorem does not claim that compact Hall is solved.  It says exactly
what must be supplied: a Maurer--Cartan higher-simplex correction,
orientation square-root primitive, grading/Tate primitive,
Thom--Sebastiani homotopy, factorisation homotopy, and vertexwise
quasi-isomorphism certificate.

## Remaining Primitive Obligations

1. Construct the full renormalised chart maps
   \(\theta_i:\Obs_{\hCS}^{q}(U_i,\mathfrak g)\to
   \CoHA_{\mathrm{crit}}^{\mathrm{or}}(U_i)\), beyond the positive
   torus-fixed finite-mode sector.
2. Produce \(\eta_{\mathrm{MC}}\) on the full Cech/Ran nerve.
3. Produce \(\lambda_{\mathrm{or}}\) for relative hCS--Hall orientation
   transport, not only the Hall-side orientation torsor.
4. Produce \(\eta_{\mathrm{gr}}\) for the shift/Tate normalisation.
5. Produce \(H_{\mathrm{TS}}\) for all iterated Hall extension
   parenthesisations.
6. Produce \(H_{\mathrm{fact}}\) for disjoint DWR/Ran products.
7. Produce \(Q\), the completed quasi-isomorphism certificate preserving
   the \(\hbar\)-adic, charge/HN, equivariant, orientation, shift, and
   Tate conventions.

The finite \(\mathbb C^3\) shuffle witness kills only the projected local
finite-mode component of \(o_\theta\).  It does not kill the compact
renormalised or descent components.
