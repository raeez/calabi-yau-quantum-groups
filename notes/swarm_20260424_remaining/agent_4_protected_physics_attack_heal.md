# Agent 4: Protected Physics Attack/Heal

## Scope

Owned files:

- `notes/swarm_20260424_remaining/agent_4_protected_physics_attack_heal.md`
- `compute/lib/protected_physics_gate.py`
- `compute/tests/test_protected_physics_gate.py`

Read-only anchors:

- `compute/lib/cy3_bridge_normal_form.py`
- `chapters/connections/cy_holographic_datum_master.tex`
- `chapters/theory/phi_universal_trace_platonic.tex`
- selected physics compute engines under `compute/lib/`

## Attack

The final normal-form gate in `compute/lib/cy3_bridge_normal_form.py` is correct but under-typed.  It requires `protected_bps_functor` before `PROTECTED_PHYSICS`, but the gate does not say what the functor consumes, what it preserves, or which failures keep a physics datum at witness level.

The vulnerable shortcut has five forms.

1. **Protected index to chiral character.**  A protected index is an oriented trace in a BPS category.  It is not a chiral character unless an orientation-line trivialisation and an index-character map
   \[
   K_0(\mathsf{BPS}_X,\mathcal L_{\mathrm{or}})\to K_0(\mathsf{Bdry}_X)
   \]
   are supplied.  `cy_holographic_datum_master.tex` already states this at the pure mathematical bridge datum, especially the warning that lattice and index-character components alone are arithmetic shadows, not the bridge.

2. **BPS Hilbert space to protected index.**  A Hilbert space dimension is not a Witten/protected index.  The protected-sector projection or supercharge cohomology must be fixed before any trace is taken.  Otherwise signs, chambers, and non-protected excitations enter.

3. **Topological string or black-hole count to algebra equivalence.**  A partition function or Rademacher/Sen asymptotic can certify a character identity or a degeneracy formula.  It cannot produce an exact functor from a Hall category to a boundary factorisation category.  The risky surfaces are `bps_black_hole_e1_engine.py`, `bps_microstate_shadow.py`, `bps_entropy_shadow.py`, `bcov_wavefunction_bar.py`, `topological_string_from_bar.py`, and `k3e_topological_string_shadow.py`: several docstrings speak in equality language, but the manuscript status must remain character-level or conditional unless the typed functor is present.

4. **Holographic trace to CY-to-chiral theorem.**  The holographic trace may be theorem-grade physics or a consistency witness.  It is not a pure CY-to-chiral implication unless Hall product/OPE comparison, orientation compatibility, and wall-crossing coherence have been constructed.  The manuscript states this gate in `cy_holographic_datum_master.tex`; the compute surface did not enforce it.

5. **Positive Hall/CoHA data to BKM algebra.**  `CoHA(C^3)=Y^+` is a positive-half statement.  BKM requires the Hall-Drinfeld double plus Borcherds denominator normalisation
   \[
   \kappa_{\mathrm{BKM}}(\Phi_N)=c_N(0)/2.
   \]
   A topological-string weight, black-hole entropy coefficient, or `1/\Phi_{10}` coefficient is not a replacement for this BKM normalisation.

## Heal

The strongest integrable package is the following typed protected BPS-to-chiral/BKM package.  For a CY target \(X\) on a framed \(d=3\) locus, it consists of:

1. a protected-sector projection \(P_{\mathrm{prot}}\) or supercharge cohomology before trace;
2. an orientation-line trivialisation compatible with DT/Hall convolution;
3. a pairing-preserving isometry from the BPS charge lattice to the Hall/BKM root lattice;
4. an index-character map from oriented BPS \(K\)-theory to the graded chiral character group;
5. a wall-crossing coherence square sending KS wall-crossing to MC gauge equivalence of the chiral datum;
6. an exact charge-preserving functor
   \[
   \mathcal H_X:\mathsf{BPS}_X\to\mathsf{Bdry}_X
   \]
   carrying Hall convolution to boundary OPE/factorisation;
7. a Hall-Drinfeld double to BKM bialgebra map;
8. Borcherds denominator normalisation by \(c_N(0)/2\).

Exact failure modes:

- omit (1): full Hilbert-space dimension is being used as a protected index;
- omit (2): the BPS index and chiral trace live in different twisted \(K\)-groups;
- omit (3): charge labels are being read as roots without preserving the pairing;
- omit (4): a numerical BPS index is being identified with a chiral character;
- omit (5): a chamber-dependent BPS count is being used as a global invariant;
- omit (6): a trace or partition function is being promoted to an algebra functor;
- omit (7): positive-half Hall data or physics counts are being treated as BKM algebra;
- omit (8): a partition-function weight is being substituted for the Borcherds weight.

The executable gate in `compute/lib/protected_physics_gate.py` implements these levels:

- `WITNESS_ONLY`
- `PROTECTED_INDEX`
- `CHIRAL_CHARACTER`
- `CHAMBER_INDEPENDENT_TRACE`
- `HALL_TO_CHIRAL_FUNCTOR`
- `BKM_CHIRAL_TRACE_PACKAGE`

It deliberately rejects:

- heuristic holography promoted to chiral theorem;
- full BPS Hilbert space promoted directly to chiral character;
- black-hole/topological-string/holographic numerical evidence promoted to Hall-to-chiral functor;
- BKM claims without the Hall-Drinfeld double and Borcherds denominator gates.

## Integration Recommendation

Keep the main chapters unchanged in this swarm pass.  Integrate the new gate by importing `protected_physics_gate.py` into `cy3_bridge_normal_form.py` only after the current normal-form file is owned by the integration thread.  The final `protected_bps_functor` gate should be replaced or refined by the eight typed gates above, with the normal-form target `protected_physics` closing only at `BKM_CHIRAL_TRACE_PACKAGE`.

Manuscript language should use the following rule: protected physics supplies theorem-grade witnesses only at the level typed by the package.  A partition function proves a character identity only under the trace package.  A Hall/BKM algebra statement requires the categorical functor and Drinfeld-double gates.  No equality from BPS Hilbert spaces, OSV, AdS/CFT, black-hole entropy, or topological strings may be read as a CY-to-chiral/BKM equivalence without those maps.
