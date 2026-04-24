# Frontier resolution swarm synthesis, 2026-04-24

## Executive verdict

The six-agent attack found no hidden unconditional closure theorem beyond
the apex obstruction package already inscribed in `working_notes.tex`.
The platonic resolution is therefore not a larger assertion.  It is the
exact equivalence:

```tex
\mathfrak O_X=0
\quad\Longleftrightarrow\quad
(\Phi^{wit}_3(X),
 \mathcal H^{mot,or}_{X,\sigma,-},
 \Theta^{or}_{hCS->Hall},
 \mathrm{AutBorch},
 \Theta_{Hall},
 G_{adm}(X),
 \mathcal B_{\Delta_5})
\text{ exist compatibly.}
```

The strongest true formulation is a supplied-data theorem.  Every
remaining issue is an explicit construction coordinate.  No agent found
a valid route turning the compact CY3 Hall package, the Hall-Drinfeld
double, the Sigma-Delta OPE bridge, or the `N=5,7,8` rows into
unconditional theorems from the present local data.

## Lane verdicts

| Lane | Report | Killed | Survives |
|---|---|---|---|
| Hall cosheaf and hCS-to-Hall descent | `frontier_resolution_swarm_20260424_hall_cosheaf.md` | finite-first KS wall-crossing after motivic Hall cosheaf, motivic integration, and locally finite HN completion are supplied | `o_atlas`, `o_or`, `o_HN`, `o_TS`, `o_MC`, `o_gr`, `o_fact` |
| Hall-Drinfeld/BKM algebra | `frontier_resolution_swarm_20260424_hall_bkm_algebra.md` | primitive numerical seed, root multiplicities, Borcherds target, radical necessity | exact closed Hopf radical, rank-two Hall-Borcherds defects, continuous pairing, negative half, Cartan completion, centre compatibility |
| `Phi_3^{wit}` kernels | `frontier_resolution_swarm_20260424_phi3_kernel_witnesses.md` | functoriality on the witnessed kernel category; casewise support/cyclic/formality cells | arbitrary compact non-formal kernels still require K1--K7 witnesses |
| `G(X)` centre/hocolim | `frontier_resolution_swarm_20260424_gx_center_hocolim.md` | native CY3 output is `E_1`; `E_2` belongs only to the descended centre; raw centre-hocolim commutation is rejected | `o_cent`, `o_pair`, `o_Delta`, `o_rad` for multi-chart compact CY3 targets |
| `Sigma_{0,24}` to `Delta_5` OPE bridge | `frontier_resolution_swarm_20260424_sigma_delta_ope.md` | `c=-214` source anomaly; character-level `phi_{0,1}->Delta_5`; genus-two shortcut obstruction | `o_OPE` in restricted chiral `H^2`; uniqueness `H^1=0`; stress-tensor and `M24` field-map compatibility |
| `N=5,7,8` hosts and `AutBorch` | `frontier_resolution_swarm_20260424_n578_hosts_autborch.md` | order-indexed constants `(c_N(0),kappa_BKM)=(4,2),(2,1),(2,1)`; no product `K3 x E` host | `o_host` for all three rows; `AutBorch^{Hall}` bracket/refined seed data |

## Coordinate ledger

### Proved or controlled

- `Phi_3^{wit}` is an `(infty,1)`-functor on the category whose objects
  and morphisms already carry the required witnesses.
- The K3 x E denominator numerics match the Borcherds side:
  primitive superdimensions and root multiplicities are controlled by
  the same K3 elliptic-genus coefficients.
- The Borcherds/BKM target has theorem-grade denominator, PBW, parity,
  finite-height enveloping, and root-multiplicity data.
- The `Sigma_{0,24}` class-S ledger gives `c_2d=-214`.
- The character-level bridge sends the K3-Jacobi specialization
  `phi_{0,1}` to `Delta_5`.
- The order-indexed `N=5,7,8` boundary constants are fixed in their
  declared normalization.
- The native CY3 output is `E_1`; any `E_2` enhancement is centre-level.

### Conditional bridges

- Descent equals KS wall crossing only after the oriented motivic Hall
  cosheaf, motivic integration, and locally finite HN completion are
  built.
- The Hall-BKM map is a continuous Hopf quotient by the radical, the
  primitive numerical kernel, and the rank-two Hall-Borcherds defects.
- `G_adm(X)` exists only after centre descent, negative half, Cartan
  completion, continuous Hopf pairing, radical quotient, and
  compatibility with local transitions are supplied.
- The Sigma-Delta bridge becomes a chiral algebra bridge exactly when
  the restricted OPE Maurer-Cartan obstruction vanishes.
- `AutBorch^{den}` is theorem-grade as a denominator construction from
  automorphic seed data; `AutBorch^{Hall}` requires bracket-refined
  primitive BPS data.

### Surviving primitives

1. Construct the oriented `(-1)`-shifted critical Hall atlas on the full
   DWR/Cech/Ran nerve.
2. Prove coherent orientation transport, Thom-Sebastiani coherence, and
   locally finite HN completion.
3. Construct the full-nerve
   `Theta^{or}_{hCS->Hall}` Maurer-Cartan solution with grading and
   factorisation compatibility.
4. Supply K1--K7 for arbitrary compact non-formal CY3 kernels, not only
   the witnessed or local Morse-Bott loci.
5. Prove Hall product constants and Borcherds-Serre relations in every
   rank-two effective Mukai subchamber.
6. Build the compact Hall-Drinfeld double: negative half, Cartan,
   continuous pairing, radical quotient, bracket comparison, completion,
   and centre compatibility.
7. Prove centre totalization equals the global centre after wall
   equalization, rather than replacing it by raw hocolim of local
   centres.
8. Kill
   `o_OPE in H^2(C_ch^bullet(V_Sigma,V_Delta)_{B^char,T,M24})`
   or construct an explicit stress-tensor-preserving `M24`-equivariant
   OPE field map.
9. Prove the corresponding `H^1=0` if uniqueness of the Sigma-Delta
   lift is to be asserted.
10. Supply compact or stacky CY3 host data
    `(X_N, Gamma_tilde_N, L_N, Z_N)` for each of `N=5,7,8`.
11. Reconcile the Gritsenko-Clery bibliographic anchor before any
    manuscript inscription using that catalogue.

## Integration decision

No correction to the apex theorem in `working_notes.tex` is required.
The six reports support its present form: the programme is closed
exactly by construction data, not by weakening the desired objects and
not by silently upgrading evidence to theorem.

The next manuscript-strengthening edit, if desired, is not a new grand
claim.  It is a short corollary after `wn:thm:compact-cy3-apex-closure`
stating that the six lanes above exhaust the obstruction vector and
that the agents found no additional untyped residue.

## Verification surfaced by agents

- Hall cosheaf lane:
  `pytest compute/tests/test_compact_hall_construction_package.py -q`
  returned `12 passed`.
- Hall-BKM lane:
  `/opt/homebrew/bin/pytest compute/tests/test_k3e_coha_structure.py compute/tests/test_bkm_shadow_complete.py compute/tests/test_k3_elliptic_genus_bkm_bar.py`
  returned `231 passed`.
- `G(X)` lane:
  `pytest compute/tests/test_drinfeld_center_hocolim.py compute/tests/test_swiss_cheese_chart_gluing.py compute/tests/test_bar_hocolim_commutation.py compute/tests/test_compact_hall_construction_package.py -q`
  returned `273 passed`.
- The `Phi_3`, Sigma-Delta, and `N=5,7,8` lanes were notes-only source
  audits with `git diff --check` or readback verification reported by
  their agents.

## Files produced by the swarm

- `notes/frontier_resolution_swarm_20260424_hall_cosheaf.md`
- `notes/frontier_resolution_swarm_20260424_hall_bkm_algebra.md`
- `notes/frontier_resolution_swarm_20260424_phi3_kernel_witnesses.md`
- `notes/frontier_resolution_swarm_20260424_gx_center_hocolim.md`
- `notes/frontier_resolution_swarm_20260424_sigma_delta_ope.md`
- `notes/frontier_resolution_swarm_20260424_n578_hosts_autborch.md`
- `notes/frontier_resolution_swarm_20260424_SYNTHESIS.md`
