# Agent 6: unified `PhiFA_d` and cross-volume pushforward gate

Date: 2026-04-24.

## Claim attacked

An unconditional unified `PhiFA_d` for `d >= 4`, together with automatic
pushforward of Vol I/II theorems A/B/C/D/H, the Vol II K3 mock theorem,
the ZTE T-matrix computation, and the shadow tower, into Vol III.

## Verdict

Rejected as an unconditional theorem.  The manuscript can support a
proof-grade gate theorem:

- `PhiFA_d` is constructed functorially at `d <= 2`.
- At `d = 3` it is a framed object-level assignment on witnessed loci.
- At `d >= 4` it is a conditional CY-A_d template until the
  holomorphic-twist, framing, and completion witnesses are constructed.
- A Vol I/II theorem pushes to Vol III only across an explicit
  chain-level comparison map into the stage-2 ordered bar, Hochschild,
  center, or representation category.

The gate is now inscribed as
`thm:cross-volume-comparison-gate` in
`chapters/connections/modular_koszul_bridge.tex`.

## Exact comparison maps

1. `Theta_A`:
   `B^ord(A_C) -> (int_{Sigma_{d-1}} B_{E_d}(PhiFA_d(mathcal C)))|_C`.
   Installed at `d=2`; available only on witnessed framed `d=3` loci;
   construction obligation at `d >= 4`.

2. `Theta_B`:
   `D_Ran B^ord(A_C) -> B^ord(D_Ran A_C)`, with finite graded pieces
   before completed products.  Higher-dimensional use requires the
   finite-piece and completion hypotheses.

3. `Theta_C`:
   `Rep(G(X)) -> Z(Rep^{E1}(A_C))`.  The K3 x E generator-level core
   and pentagon colimit are evidence; general `G(X)` and braided
   equivalence are not constructed.

4. `Theta_D`:
   separate Hodge, Heisenberg-Mukai, and Borcherds maps.  In particular
   `kappa_ch^{Heis}=3` and `kappa_BKM=5` on K3 x E are
   construction-dependent values, not alternate evaluations of one
   Hodge supertrace.

5. `Theta_H`:
   `HC^-_*(mathcal C) -> ChirHoch(A_C)`.  Vol I Theorem H identifies only the
   curve `tau_{<=2}` piece; residual CY degrees at `d >= 3` live in the
   derived center, Drinfeld center, and Verdier spectral pages.

6. `Theta_{mock -> K3 x E}`:
   `Theta_{Phi_2(K3)} boxtimes H_E -> Theta_{Phi_3^{(K3,E)}(K3 x E)`,
   compatible with the elliptic fibre, DMVV second quantization, and the
   Borcherds lift.  Without this map, the K3 mock theorem remains a
   `d=2` fibre theorem.

7. `Theta_{ZTE -> Phi}`:
   `R_Yang(z) -> sigma_{V_u}(V_v) in Z(Rep^{E1}(A_C))`, plus an
   identification of the ternary correction with `E_3` operations from
   `PhiFA_3(mathcal C)`.  The exact T-matrix is a chain-level Yangian
   deformation witness, not by itself a CY-A/CY-C theorem.

8. `Theta_{sh -> DT}`:
   `H^*(B^ord(A_C)) -> H^*_{van}(M_DT(X))`, compatible with Behrend
   signs and Hall multiplication.  The shadow tower originates in the
   ordered Ran bar complex of the stage-2 chiral algebra; Borcherds, DT,
   and BPS series are comparison targets.

## Manuscript anchors changed

- `chapters/theory/introduction.tex`
  - Lines 296-303: stage 1 is the native holomorphic factorisation
    algebra on constructed loci; `d >= 4` is conditional.
  - Lines 752-756: CY-A_d status split into functorial `d <= 2`,
    framed object-level `d = 3`, and conditional `d >= 4`.
  - Lines 1863-1872 and 2106-2110: ZTE uses the Yangian parameter
    `hbar_Y`; Phi-level interpretation requires the Drinfeld-center
    half-braiding comparison.
  - Lines 2030-2039: installed constructions are CY-A_2 and witnessed
    CY-A_3 loci, with compact non-formal CY_3 still conditional.

- `chapters/connections/modular_koszul_bridge.tex`
  - Lines 6-19 and 63-71: two-stage factorisation is restricted to
    constructed loci; `d >= 4` remains a CY-A_d conditional template.
  - Lines 151-158: shadow tower chain origin is the ordered Ran bar
    complex `B(A_C)` after the stage-2 object is constructed.
  - Lines 301-321: CY shadow CohFT now assumes the stage-2 chiral algebra
    and unit-vacuum comparison explicitly.
  - Lines 1660-1819: cross-volume comparison gate and exact missing-map
    list.
  - Lines 1848-1872: Vol I/II bridge summaries are candidate
    Phi-pushforwards only where comparison maps are installed.

- `chapters/connections/cy_holographic_datum_master.tex`
  - Lines 27-45: two-stage factorisation and seven faces are on
    constructed loci; `d >= 4` is conditional.
  - Lines 51-53, 164-171, 1602-1604, 2322-2324: K3 x E stage-1 language
    is chosen/framed rather than unconditional canonical.
  - Lines 1494-1498: heptagon transitivity is theorem-level only where
    the chosen six edges are theorem-level comparison maps.

## `en_factorization.tex` proposed snippets only

No edits were made to `chapters/theory/en_factorization.tex`.

Suggested replacement for lines 15-19:

```tex
The two-stage factorisation of Theorem~\ref{thm:phi-two-stage-factorisation}
assigns, on constructed loci, a stage-$1$ $E_d$-holomorphic
factorisation algebra $\PhiFA_d(\cC) \in \EdHolFA(X)$ on the CY$_d$
variety, followed by the chiral specialisation
$\SpCh_{\Sigma_{d-1}, C}$ to an $E_n$-chiral algebra on a reference
curve $C$. For $d\geq4$ this remains the CY-A$_d$ conditional template.
```

Suggested qualifier for proposition hypotheses around line 69:

```tex
Assume the stage-$1$ object $\PhiFA_d(\cC)$ and the framed
specialisation datum $(\Sigma_{d-1}, C)$ have been constructed.
```

The ZTE section already uses `\hbar_{\mathrm{Y}}` for the Yangian
deformation parameter and treats the T-matrix as a ternary `E_3`
correction.

## Tests

Command:

```bash
python3 -m pytest compute/tests/test_cross_volume_shadow_bridge.py compute/tests/test_mock_modular_k3_proof.py compute/tests/test_zte_t_matrix_exact.py
```

Result: 245 passed in 18.40s.

No session-end LaTeX build was run.

## Remaining open questions

- Construct the `d >= 4` holomorphic-twist, framing, and completion
  witnesses for `PhiFA_d`.
- Install the compact non-formal CY_3 chain-level witness for K3 x E
  beyond the framed object-level assignment.
- Build `Theta_{mock -> K3 x E}` and prove compatibility with elliptic
  fibre, DMVV second quantization, and the Borcherds lift.
- Build `Theta_{ZTE -> Phi}` identifying the Yang R-matrix with the
  Drinfeld-center half-braiding and the T-matrix with the `E_3` ternary
  operation.
- Build `Theta_{sh -> DT}` in all degrees, with Behrend signs and Hall
  multiplication.
- Construct the general braided comparison `Theta_C` and the general
  object `G(X)`.
