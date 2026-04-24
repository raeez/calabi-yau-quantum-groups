# Agent 1 report: `Phi_3` kernels and the primitive envelope

## Attacked claim

Target: `chapters/theory/cy3_chain_level_bridge.tex:2149`, Theorem
`thm:cy3-universal-primitive-envelope`, read against the `Phi_3`
morphism problem in `chapters/theory/cy_to_chiral.tex:677` and
`chapters/examples/derived_categories_cy.tex:393`.

Question attacked: does the universal primitive envelope actually
realize global SYZ/Poincare/HMS kernels with orientation, cyclic
transfer, `S^3` framing, OPE completion, and all convolution coherences
beyond normal forms?

Verdict: no, not as a geometric theorem. It realizes the initial formal
obstruction-killing extension. It becomes a global `Phi_3` morphism
theorem only after the analytic/geometric primitives listed below are
constructed inside the relevant completed categories.

## Failure mode

1. Formal primitive is not analytic primitive.
   `cy3_chain_level_bridge.tex:2158-2167` freely adjoins generators
   `h_{j,a}` with `dh_{j,a}=o_{j,a}`. This proves formal acyclicity of
   the named first obstruction classes. It does not construct a
   Fourier-Mukai/SYZ kernel, a Fukaya bimodule, a Costello-Li naturality
   cell, or a completed OPE target.

2. The theorem itself contains the correct firewall.
   `cy3_chain_level_bridge.tex:2193-2205` says the envelope becomes an
   unconditional compact theorem exactly when realized by global
   witnessed kernels and the other analytic/completed objects.
   `cy3_chain_level_bridge.tex:2208-2237` proves only the formal
   universal property.

3. `Phi_3` morphisms already require K1-K7.
   `cy_to_chiral.tex:677-737` defines a `Phi_3`-admissible kernel datum:
   perfect/proper kernel, orientation and negative-cyclic transport,
   cyclic bar transfer commuting with `b`, `B`, `B^{(2)}`, formality and
   `S^3`-framing compatibility, Costello-Li naturality, witnessed
   specialization, and convolution unit/associativity cells.
   `cy_to_chiral.tex:806-839` states that without these data the
   object-level outputs exist but no morphism is defined.

4. HMS/SYZ remains raw until witnessed.
   `derived_categories_cy.tex:585-657` is correctly conditional:
   HMS/SYZ, flop, McKay, and wall-crossing kernels become `Phi_3`
   kernels only after the listed witnesses are attached.
   `derived_categories_cy.tex:847` treats the HMS kernel as raw and says
   the chain-level curved `L_infinity` morphism exists only after the
   witnessed data are fixed.

5. The compute oracle closes normal forms, not global analysis.
   `compute/lib/cy3_platonic_bridge.py:321-362` marks the four
   casewise `Phi_3` kernel components true, but
   `compute/lib/cy3_platonic_bridge.py:667-760` sets analytic
   realization false for every freely adjoined primitive.
   The tests enforce the separation: `compute/tests/test_cy3_platonic_bridge.py:199-213`
   proves formal closure while asserting `analytic_global_primitive_closure() is False`.

## Strongest truthful theorem

The correct theorem is:

For a raw Fourier-Mukai/SYZ/HMS/flop/McKay/wall-crossing kernel `K`,
the universal primitive envelope is the initial completed dg extension
in which the first obstruction classes of
`Def(K; or, cyc, S^3, OPE, \circ)` become boundaries. It gives a
global `Phi_3` morphism if and only if those formal primitives are
realized by:

- a global SYZ/Poincare or Fourier-Mukai/Fukaya kernel of finite
  Tor-amplitude/proper support, with the required brane/relative-spin
  and singular-fibration data in the HMS case;
- determinant-line square roots and negative-cyclic CY trace transport,
  including overlap and triple-overlap orientation coherences;
- cyclic transfer commuting with `b`, `B`, and `B^{(2)}`;
- a chain-level `S^3` framing homotopy compatible with the chosen
  `GRT_1` formality point;
- a Costello-Li naturality cell, anomaly cancellation, analytic
  completion, and OPE completion;
- Stage-2 specialization data: Beck-Chevalley, Fubini, compact-support,
  properness, and Tor-independence cells;
- convolution unit, associativity, pentagon, and higher associahedra
  coherences, killing the triple product class in
  `H^2(g_{Phi_3}(K_3 \circ K_2 \circ K_1))` and its higher successors.

## Recommended claim status

Keep `thm:cy3-universal-primitive-envelope` only as
`ProvedHere(formal obstruction resolution; analytic realisation is the
exact remaining condition)`. Any statement that the envelope itself
realizes global SYZ/Poincare/HMS kernels should be `Conditional` or
`Open`, depending on the named kernel class.

`prop:phi3-casewise-witnessed-kernels` should remain conditional.
The compute name `all_phi3_kernel_cases_close()` is safe only if read as
normal-form closure; it is misleading if read as global kernel closure.

## Files changed

- Added this report only:
  `notes/adversarial_swarm_20260424_primitive_envelope/agent_1_phi3_kernels.md`.

## Tests and computations run

- `pytest -q compute/tests/test_cy3_platonic_bridge.py`: 19 passed.
- Direct oracle query with `python3`:
  `formal_global_primitive_closure = True`,
  `analytic_global_primitive_closure = False`,
  `unconditional_global_theorem_claims = ()`,
  and `remaining_analytic_global_obligations == GLOBAL_WITNESS_REQUIREMENTS`.

## Remaining open questions

1. Construct a genuine HMS/SYZ Poincare kernel or Fukaya bimodule on the
   compact CY3 cases, including singular-fibration corrections and
   relative spin/orientation data.
2. Build the relative Costello-Li/BCOV naturality cell for that kernel,
   not only the scalar Yukawa or normal-form target.
3. Produce the cyclic transfer and `S^3` framing homotopies explicitly.
4. Prove OPE convergence/completion compatibility after Stage-2
   specialization.
5. Construct the convolution coherence tower beyond the displayed
   normal forms, including pentagon and higher associahedra primitives.
