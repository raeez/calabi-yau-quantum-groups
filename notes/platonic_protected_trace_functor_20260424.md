# Protected Trace Functor Primitive

## Claim Attacked

Protected-index equality from a BPS Hilbert space, black-hole count,
topological-string partition function, or holographic trace does not by
itself construct a protected trace functor from the physical sector to
the chiral/BKM trace side.

The attacked shortcut is:

\[
\text{protected index equality}
\quad\Longrightarrow\quad
\text{Hall-to-OPE functorial protected trace}.
\]

## Construction / Failure Mode

The functorial object must be a typed package:

1. protected-sector projection or \(Q\)-cohomology before trace;
2. orientation-line trivialisation compatible with DT/Hall convolution;
3. compact-support compatibility for the same Borel--Moore or
   renormalised \( ! \)-pushforward used in the Hall product;
4. charge-lattice isometry to the chiral/BKM root or weight lattice;
5. index-character map from oriented BPS \(K\)-theory to the chiral
   character group;
6. wall-crossing coherence, sending KS wall-crossing to MC gauge
   equivalence;
7. exact symmetric monoidal trace functor preserving product;
8. for BKM output, Hall--Drinfeld double map plus
   \(\kappa_{\mathrm{BKM}}(\Phi_N)=c_N(0)/2\) denominator normalisation.

Failure of any gate leaves a character-level or witness-level statement.
The scalar index is not faithful: it kills classes in the kernel of the
protected index, forgets orientation twists, forgets compact-support
pushforward data, and can kill chamber motion. A proof that factors only
through this scalar quotient cannot determine a monoidal functor.

## File Anchors

- `chapters/connections/cy_holographic_datum_master.tex`
  - `def:pure-math-holographic-bridge-datum`: compact-support wording
    added to the existing bridge datum.
  - `def:protected-trace-functor-package`: new typed package for the
    protected trace functor.
  - `thm:protected-index-vs-trace-functor`: new criterion/obstruction
    separating scalar protected-index equality from functorial protected
    trace.
- `compute/lib/protected_physics_gate.py`
  - read-only executable gate already encodes the same levels:
    `PROTECTED_INDEX`, `CHIRAL_CHARACTER`,
    `CHAMBER_INDEPENDENT_TRACE`, `HALL_TO_CHIRAL_FUNCTOR`,
    `BKM_CHIRAL_TRACE_PACKAGE`.
- `compute/tests/test_protected_physics_gate.py`
  - read-only tests verify that numerical physics evidence cannot prove
    algebra functors and that BKM claims require the double and
    denominator gates.

## Theorem / Criterion Added

The new theorem proves:

- A complete protected trace functor package promotes protected-index
  identities to functorial chiral trace identities preserving products,
  orientations, wall-crossing, charge gradings, and compact support.
- BKM-valued trace requires the Hall--Drinfeld double and
  \(\kappa_{\mathrm{BKM}}=c_N(0)/2\) denominator normalisation.
- Scalar protected-index equality alone gives at most a character-level
  statement; it cannot construct or determine the protected trace
  functor.

## Verification

- Read `AGENTS.md` and `CLAUDE.md`.
- Read the local bridge datum and gate theorem in
  `chapters/connections/cy_holographic_datum_master.tex`.
- Read `notes/swarm_20260424_remaining/agent_4_protected_physics_attack_heal.md`.
- Read the executable protected gate and tests in
  `compute/lib/protected_physics_gate.py` and
  `compute/tests/test_protected_physics_gate.py`.

Targeted verification run:

```bash
pytest compute/tests/test_protected_physics_gate.py
git diff --check -- chapters/connections/cy_holographic_datum_master.tex notes/platonic_protected_trace_functor_20260424.md
rg -n -F "\label{def:protected-trace-functor-package}" -g '*.tex'
rg -n -F "\label{thm:protected-index-vs-trace-functor}" -g '*.tex'
rg -n -F "\ref{def:protected-trace-functor-package}" -g '*.tex'
```

Result: protected gate tests passed (`8 passed`), whitespace checks were
clean, and the new labels/ref anchors resolve locally. No
`scripts/check_labels.py` exists in this repository; no session-end
`make fast` was run.

## Remaining Primitive Obligations

1. Construct \(P_X^{\mathrm{prot}}\) for the chosen physical model,
   not just its scalar index.
2. Construct the exact symmetric monoidal
   \(\operatorname{Tr}^{\mathrm{prot}}_X\).
3. Prove Hall convolution matches boundary OPE/factorisation with the
   same compact-support pushforward.
4. Prove orientation-line compatibility, not just sign agreement in
   examples.
5. Prove KS wall-crossing maps to MC gauge equivalence on the chiral
   datum.
6. For BKM output, construct the Hall--Drinfeld double map and verify
   Borcherds denominator normalisation independently.
