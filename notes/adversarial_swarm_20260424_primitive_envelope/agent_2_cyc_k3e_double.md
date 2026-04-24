# Agent 2 - CY-C / K3 x E Double Assembly Attack

## Attacked claim

The target claim is that the universal primitive envelope for the
CY_3 platonic resolution realizes the CY-C object `G(K3 x E)` as global
chiral-algebra data: compact positive half, compact negative half,
non-degenerate Hopf pairing, completion/radical quotient, and
centre-continuity.

## Verdict

No global double is constructed by the primitive envelope. The theorem
`thm:cy3-universal-primitive-envelope` is correct only as a formal dg
obstruction resolution: it freely adjoins primitives `h_{j,a}` with
`d h_{j,a}=o_{j,a}` and proves the universal mapping property of that
completed extension (`chapters/theory/cy3_chain_level_bridge.tex:2149`,
`:2151`, `:2158`, `:2166`, `:2193`, `:2204`). It does not realize the
CY-C Manin-pair data inside compact Hall/chiral categories.

The compute oracle agrees. It reports `CY_C_double_assembly=True` only
at the finite normal-form layer, while `analytic_global_primitive_closure()`
is false and the remaining CY-C obligations are exactly:

1. `compact positive half`
2. `negative half`
3. `non-degenerate Hopf pairing`
4. `completion and radical quotient`
5. `centre-continuity`

## Failure Mode

The positive half is present only as a route/normal-form shadow. The
source file explicitly says the positive half alone is not a double and
that CY-C is controlled by the completed Manin-pair complex
`Def(Hall^+_cpt, Hall^-_cpt, pairing, completion, Z_ch^der)`
(`chapters/theory/cy3_chain_level_bridge.tex:1977`-`:1986`). The K3 x E
programme is even sharper: the Hall-to-Borcherds map compares only the
positive half; the Hall-Drinfeld double, E_2 centre, and VOA envelope are
subsequent assembly steps, not hidden in that map
(`chapters/examples/k3e_cy3_programme.tex:135`, `:141`).

The negative half is not constructed in the audited CY-C chapter. It is
named as part of the representability package
(`chapters/examples/cy_c_six_routes_convergence.tex:193`-`:195`), but
the pairwise bridge propositions construct scalar, character, OPE, and
positive-half comparison data, not a compact Serre-dual negative half
with topology (`:313`-`:335`, `:472`-`:507`).

The Hopf pairing is the first obstruction, not a solved input. The chain
chapter names the obstruction pair
`[rad <,>_Hall]` and `[ob_Z] in H^2(g_CYC)`, measuring degeneracy after
completion and failure of derived-centre continuity
(`chapters/theory/cy3_chain_level_bridge.tex:1986`-`:1996`). The quantum
groups foundation has the same condition: the double exists only after a
Serre-dual negative half, Cartan half, and continuous Hall-Serre pairing
are fixed and non-degenerate after radical quotient
(`chapters/theory/quantum_groups_foundations.tex:204`-`:220`).

Completion/radical quotient and centre-continuity are not finite
bookkeeping. The chain chapter states that no finite computation may
promote a normal-form package into an unconditional global theorem
(`chapters/theory/cy3_chain_level_bridge.tex:1924`-`:1927`) and that
global closure needs the completed compact Hall double
(`:2193`-`:2199`). The test suite enforces the same line:
`unconditional_global_theorem_claims()==()`,
`all_requested_global_theorems_close() is False`, and
`remaining_analytic_global_obligations()==GLOBAL_WITNESS_REQUIREMENTS`
(`compute/tests/test_cy3_platonic_bridge.py:160`-`:162`,
`:208`-`:213`).

The CY-C six-routes chapter overstates the status. It marks the central
six-route colimit and K3 x E worked-locus corollary as `ProvedHere`
(`chapters/examples/cy_c_six_routes_convergence.tex:106`-`:128`,
`:246`-`:258`), but the proof step from positive colimit to double says
only that "Hopf pairing, completion, and centre-continuity data then
give" H5-H6 (`:271`-`:275`). That is a hypothesis transfer, not a
construction. The local doctrine also says CY-C is conjectural and
`G(X)` is unconstructed in general (`CLAUDE.md:420`-`:424`).

## Healed Statement

**Conditional CY-C Manin-pair construction theorem.** Let
`X = K3 x E`. Suppose the positive-half comparison has produced a compact
completed Hall/chiral bialgebra `Y^+(X)` on the K3 x E charge cone, and
suppose one supplies five compatible primitives in the CY-C deformation
complex:

1. `h_CY_C_double_assembly_1`: compact positive half, with coproduct
   compatible with the route arrows and the Hall-Borcherds positive-half
   map.
2. `h_CY_C_double_assembly_2`: compact Serre-dual negative half
   `Y^-(X)`.
3. `h_CY_C_double_assembly_3`: continuous Hopf pairing
   `Y^+(X) \widehat\otimes Y^-(X) -> 1`.
4. `h_CY_C_double_assembly_4`: closed radical Hopf ideal and completed
   quotient on which the pairing is non-degenerate.
5. `h_CY_C_double_assembly_5`: continuous derived-centre transport
   `Z(Rep^{E_1}(Y^+(X))) ~= Rep^{E_2}(D_hbar(Y^+(X)))`.

Then `G(K3 x E):=D_hbar(Y^+(X)_red)` exists as a completed braided
E_2 chiral object, and the six routes identify its E_1 positive-half
shadows. Conversely, any unconditional CY-C double theorem determines
these five primitives. If any one is missing, the result is only the
positive-half / normal-form layer.

Equivalently, the obstruction criterion is:

`CY-C global double closes iff [rad <,>_Hall]=0 and [ob_Z]=0 in
H^2(g_CYC), with primitives compatible with the chosen completion,
orientation, and route coproducts.`

## Recommended Claim Status

Keep `thm:cy3-universal-primitive-envelope` as `ProvedHere` only with
the present parenthetical: formal obstruction resolution; analytic
realisation is the remaining condition.

Downgrade the global CY-C double/colimit assertions in
`chapters/examples/cy_c_six_routes_convergence.tex` from unconditional
`ProvedHere` to conditional on the five Manin-pair primitives above,
unless the integration owner can point to an actual construction of the
compact negative half, non-degenerate completed Hopf pairing, radical
quotient, and centre-continuity equivalence.

## Tests and Computations

Ran `python -m pytest compute/tests/test_cy3_platonic_bridge.py -q`:
failed because `python` is not on PATH.

Ran `python3 -m pytest compute/tests/test_cy3_platonic_bridge.py -q`:
`19 passed in 0.23s`.

Ran direct oracle query with `python3 -c ...`:
`gate_status['CY_C_double_assembly'] == True`,
`formal_global_primitive_closure() == True`,
`analytic_global_primitive_closure() == False`, and the remaining CY-C
obligations are the five listed above.

## Files Changed

Only this report:
`notes/adversarial_swarm_20260424_primitive_envelope/agent_2_cyc_k3e_double.md`.

## Remaining Open Questions

1. Construct the compact negative half for the K3 x E Hall/Borcherds
   sector and specify its topology.
2. Prove the completed Hall pairing has a closed Hopf radical and becomes
   non-degenerate after quotient.
3. Prove centre-continuity for the completed double, not just for a
   formal E_1 positive-half shadow.
4. Upgrade the positive-half Hall/Borcherds bracket and coproduct
   comparison from scalar/character evidence to a continuous chiral
   bialgebra theorem.
5. Identify the analytic or categorical category in which the five
   formal primitives above are represented by actual maps.
