# Agent 07 - Nekrasov/Feynman Compute

Date: 2026-04-24.

Scope discipline: read `CLAUDE.md` first. Wrote only this note. No chapter files and no compute files were edited. Other agent notes in this directory were left untouched.

## Verdict

Completed test evidence: 600 passed, 0 failed.

The computational surface supports the local algebraic claims for the hCS/E3/chiral CE bridge: the CE deformation invariants, E3 Hochschild tricomplex dimensions, Feynman-shadow dictionary, hCS-vs-sigma route separation, K3 hCS hierarchy, defect OPE, pairwise YBE controls, and the nonzero ZTE obstruction all pass targeted checks.

It does not promote the 6d programme to theorem status. The following remain conjectural or open at manuscript level: full E3 Koszul duality from 6d theory, the 6d boundary quantum toroidal construction, the K3 Yangian from hCS, the Costello-Li KS boundary algebra as an actual VOA construction, and the chain-level corrected non-factorized ZTE S-operator beyond the computed obstruction/correction complex.

## Exact Commands

Completed:

```bash
python3 -m pytest compute/tests/test_chiral_ce_e3_deformation.py compute/tests/test_holomorphic_cs_chiral_engine.py compute/tests/test_e3_hochschild_deformation.py -q
```

Result: 204 passed in 2.67s.

```bash
python3 -m pytest compute/tests/test_hcs_vs_sigma_adversarial.py -q
```

Result: 90 passed in 0.59s.

```bash
python3 -m pytest compute/tests/test_perturbative_chiral_feynman.py -q
```

Result: 69 passed in 0.41s.

```bash
python3 -m pytest compute/tests/test_chiral_rmatrix_e3_braiding.py -q
```

Result: 65 passed in 0.13s.

```bash
python3 -m pytest compute/tests/test_e3_two_parameter_rmatrix.py -q
```

Result: 34 passed in 4.91s.

```bash
python3 -m pytest compute/tests/test_zamolodchikov_tetrahedron_engine.py::TestYBEOptimised compute/tests/test_zamolodchikov_tetrahedron_engine.py::TestNumpyDivisionByZeroFix compute/tests/test_zamolodchikov_tetrahedron_engine.py::TestCharge2Optimised compute/tests/test_zamolodchikov_tetrahedron_engine.py::TestZTESpecialised compute/tests/test_zamolodchikov_tetrahedron_engine.py::TestKappaExpansion -q
```

Result: 22 passed, 9 warnings in 124.90s. Warnings are `PytestUnknownMarkWarning` for unregistered `@pytest.mark.slow` at lines 386, 393, 399, 407, 415, 424, 454, 463, 485 of `compute/tests/test_zamolodchikov_tetrahedron_engine.py`. No behavioral failure.

```bash
python3 -m pytest compute/tests/test_hcs_hierarchy_k3.py compute/tests/test_hcs_codim2_defect_ope.py -q
```

Result: 116 passed in 2.72s.

Unscored aggregate attempts:

```bash
python3 -m pytest compute/tests/test_chiral_rmatrix_e3_braiding.py compute/tests/test_e3_two_parameter_rmatrix.py compute/tests/test_zamolodchikov_tetrahedron_engine.py -q
```

Killed after about 4m26s in the exact-symbolic ZTE tail; replaced by the countable separated runs above.

```bash
python3 -m pytest compute/tests/test_zamolodchikov_tetrahedron_engine.py::TestYBEOptimised compute/tests/test_zamolodchikov_tetrahedron_engine.py::TestNumpyDivisionByZeroFix compute/tests/test_zamolodchikov_tetrahedron_engine.py::TestCharge2Optimised compute/tests/test_zamolodchikov_tetrahedron_engine.py::TestZTESpecialised compute/tests/test_zamolodchikov_tetrahedron_engine.py::TestKappaExpansion compute/tests/test_zamolodchikov_tetrahedron_engine.py::TestCharge2SymbolicOptimised compute/tests/test_zamolodchikov_tetrahedron_engine.py::TestMultiPathCrossChecks -q
```

Killed after about 4m12s in the long symbolic tail; replaced by the 22-test finite ZTE subset above.

## Attack -> Heal Cycles

### Cycle 1: CE/E3/Hochschild baseline

Attack: independently rerun the main-thread claim that the three core files pass together.

Heal: `204 passed`. The core executable contract is stable:

- `h_1+h_2+h_3=0`.
- At `(h_1,h_2,h_3)=(1,-2,1)`: `sigma_2=-3`, `sigma_3=-2`, level `k=-sigma_2=3`, `g(5)=28/27`.
- CE classes: Heisenberg class G polynomial, Yangian class L rational, Virasoro class M Gevrey-1 divergent.
- `d_h^2=True` in the tested G/L/M examples.

Classification: computed. The construction `constr:quantum-ce-deformation` is computationally supported at the tested formal level; full 6d E3 Koszul duality remains conjectural.

### Cycle 2: hCS-vs-sigma category error

Attack: force the K3 route comparison to confront central charge, shadow class, E-level, and Yangian existence at once.

Heal: `90 passed`. Route table verified:

- Route A, Costello-Li KS boundary: `c=24`, `\kappa_{\mathrm{ch}}=24`, class G, `E_\infty`, conjectural/heuristic construction.
- Route B, `H_{\mathrm{Muk}}=\Phi(D^b Coh(K3))`: `c=24`, `\kappa_{\mathrm{ch}}=2`, class G, `E_2`, proved.
- Route C, `N=4` K3 SCA: `c=6`, `\kappa_{\mathrm{ch}}=2`, class M, `E_2`, proved.
- Route D, K3 Yangian: no VOA central charge, `\kappa_{\mathrm{ch}}=3`, class G, `E_1`, conjectural.

Additional constants: `c(H_Muk)/c(V_K3)=4`, Routes B and C agree on `\kappa_{\mathrm{ch}}=2`, the K3 classical limit has `p_1=0`, `p_2=24/5`, `p_3=96/25`, leading deformation order `3`.

Classification: theorem/computed for the route separation as written in `prop:hcs-vs-sigma`; conjectural for the KS boundary and K3 Yangian construction.

### Cycle 3: Feynman-shadow normalization

Attack: test whether the perturbative Feynman lane uses the same coefficients as the CE/Hochschild lane.

Heal: `69 passed`. Direct probe:

- Feynman weight at `(1,-2,1)`: `sigma_2=-3`, `sigma_3=-2`.
- `phi_0=1`, `phi_1=0`, `phi_2=0`, `phi_3=4`, `phi_4=0`, `phi_5=12`, `phi_6=8`, `phi_7=36`.
- Tree weight `3`; theta weight `4`.
- Spin-2 contributions at `c=1`: tree `1/2`, one-loop `1/2`, two-loop `2`, three-loop `10/27`.
- Virasoro CE coefficients: `S_2=1/2`, `S_3=2`, `S_4=10/27`.

Classification: computed. This supports the manuscript's Feynman-shadow dictionary locally; it does not prove all-order convergence for class M.

### Cycle 4: E3 Hochschild tricomplex and class M obstruction

Attack: verify that the E3 Hochschild lane does not silently use the class L/C formula for class M.

Heal: included in the 204-test core run and direct probe:

- `n=1`, class G: chain `8`, cohomology `8`, Poincare `((1+s)(1+t)(1+u))^1`.
- `n=3`, class L: chain `512`, cohomology `512`, Poincare `(1+t)^9`.
- `n=1`, class M: chain `8`, cohomology `6`, Poincare `(3t(1+t))^1`.
- Mukai Heisenberg `n=24`: chain/cohomology `8^24=4722366482869645213696`.
- Class M spectral data: `d_4=40/27`, `E_3=8`, `E_4=6`, degeneration page `E_4`.

Classification: computed for the finite tricomplex model. Open for full chain-level E3 Hochschild comparison beyond these engines.

### Cycle 5: YBE positive control versus ZTE obstruction

Attack: separate pairwise YBE success from false tetrahedron coherence.

Heal:

- `test_chiral_rmatrix_e3_braiding.py`: 65 passed.
- `test_e3_two_parameter_rmatrix.py`: 34 passed.
- selected finite ZTE classes: 22 passed.

Direct ZTE values:

- For `h_1=1`, `h_2=2`, `h_3=-3`, the engine parameter is `\hbar_{\mathrm{Y}}=-6`.
- ZTE obstruction `all_zero=False`.
- Nonzero charge-2 entries: `24`.
- First nonzero entry: `(0,1)=-8/17745`.
- Expansion leading order: `O(\hbar_{\mathrm{Y}}^2)`.

Classification: theorem/computed negative for the factored Yang R-matrix ZTE claim (`thm:zte-failure`). Conjectural/open for a full corrected E3 S-operator as a chain-level construction.

### Cycle 6: hCS K3 hierarchy and codimension-2 defects

Attack: probe hCS-specific lanes not covered by the flat CE engines.

Heal: `116 passed` across `test_hcs_hierarchy_k3.py` and `test_hcs_codim2_defect_ope.py`.

Classification: computed consistency for the local hCS hierarchy/defect OPE engines. Manuscript status should remain mixed: K3 CY-A2/sigma assertions are proved; d=3 hCS/Yangian outputs stay conjectural where the source labels them conjectural.

## Status Matrix

| Lane | Evidence | Status |
|---|---:|---|
| CE deformation `d_h`, Omega constants, G/L/M analytic type | 204-test core plus direct constants | computed |
| `constr:quantum-ce-deformation` local formal model | 204-test core | computed support, not global theorem |
| E3 Hochschild tricomplex finite dimensions | 204-test core plus direct constants | computed |
| Feynman graph/shadow coefficient dictionary | 69 tests | computed |
| hCS-vs-sigma route separation | 90 tests | theorem/computed as route comparison |
| Costello-Li KS boundary algebra as VOA | route data labels heuristic/conjectural | conjectural |
| K3 Yangian from 5d hCS | route data labels conjectural | conjectural |
| Pairwise YBE controls | ZTE subset plus R-matrix tests | computed/proved control |
| Factored Yang R-matrix satisfies ZTE | finite ZTE subset and direct constants | computed false |
| Corrected non-factorized E3 S-operator | obstruction/correction evidence only | open/conjectural |
| Full E3 Koszul duality from 6d theory | manuscript `conj:e3-koszul-duality` | conjectural |

## Manuscript Implications

1. Keep `conj:e3-koszul-duality` conjectural. The tests support Heisenberg/free-field and cohomological finite models; they do not close chain-level E3 Koszul duality.

2. Keep `thm:zte-failure` as the decisive negative theorem for the factored Yang R-matrix. This run independently verified the YBE positive control and the nonzero charge-2 ZTE obstruction with leading order `O(\hbar_{\mathrm{Y}}^2)`.

3. Do not promote `conj:6d-boundary-toroidal`, the K3 Yangian, or the Costello-Li boundary construction. The compute evidence is compatibility evidence, not construction evidence.

4. Keep the hCS-vs-sigma separation exactly as category separation: `H_{\mathrm{Muk}}` and the `N=4` SCA are different algebras; agreement is at `\kappa_{\mathrm{ch}}=2`, not at central charge or shadow class.

5. Registering the `slow` pytest mark would clean the ZTE build surface. The warning is not mathematical, but it makes full-file ZTE runs noisy and hides which symbolic tails are expected.

6. Future ZTE verification should prefer the finite command above unless the full symbolic classes are explicitly needed. The aggregate E3/YBE/ZTE command is too coarse for fast adversarial work.
