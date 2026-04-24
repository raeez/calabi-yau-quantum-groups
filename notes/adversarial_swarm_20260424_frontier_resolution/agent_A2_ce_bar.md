# A2 CE/Bar Report

Date: 2026-04-24.

Scope: continuous many-variable compact-support Dolbeault/chiral CE complex on a CY3 polydisc, its relation to the `E_3` bar/envelope, continuous duals, and Weiss/Ran descent. This report is the only file changed.

## Verdict

The direct slogan
\[
  C^\bullet_{\mathrm{Lie,cont}}(\Omega_c^{0,\bullet}(P,J^\infty_{\mathrm{hol}}\mathfrak l)[1],\mathbb C)
  \;=\;
  B_{E_3}(U^{\mathrm{fact},E_3}_P(\mathfrak L))
\]
is not proved in the current text. It is also typed incorrectly: the left side is a completed cochain algebra of continuous functions on compactly supported fields; the right side is a bar chain coalgebra of an `E_3` envelope. The correct local theorem is a continuous-duality statement:
\[
  \Obs^{\mathrm{cl}}_{\bar\partial,\mathrm{chir}}(P)
  \;\simeq\;
  \bigl(B_{E_3}U^{\mathrm{fact},E_3}_P(\mathfrak L)\bigr)^\vee_{\mathrm{cont}}
\]
after fixing nuclear locally convex conventions, compact-support conventions, a strong continuous dual, completed projective tensor products, and the Stage-1 `E_3` formality/Costello-Li witness.

This is inscribable now as a local classical proposition sequence. It does not prove the quantum BV renormalised statement, the hCS-to-Hall comparison, or compact non-formal CY3 functoriality.

## Attacked Claims

1. **Continuous cochains are written without a topology.**
   `chapters/theory/cy3_chain_level_bridge.tex:101-131` defines
   \[
   C^\bullet_{\mathrm{Lie,cont}}(\mathfrak L_{\mathcal C}(P),\mathbb C)
   =
   \widehat{\mathrm{Sym}}(\mathfrak L_{\mathcal C}(P)^\vee[-1])
   \]
   but does not define the locally convex topology on \(\mathfrak L_{\mathcal C}(P)\), the meaning of \((-)^\vee\), or which completed symmetric algebra is used. This is fatal for the word `cont`, but fixable.

2. **Compact support and the locally constant shadow are being mixed.**
   The local object uses \(\Omega_c^{0,\bullet}(P,-)\) at `cy3_chain_level_bridge.tex:112-129`. The later shadow
   \(\Omega^{0,\bullet}(P)\simeq\mathbb C\) at `cy3_chain_level_bridge.tex:181-193` drops compact supports. That is legitimate only after explicitly passing to the non-compact-support side, or after Serre duality. Compact-support Dolbeault cohomology on a polydisc is not the same object as ordinary Dolbeault cohomology.

3. **Bar chains and CE cochains are conflated.**
   `quantum_chiral_algebras.tex:455-490` correctly distinguishes CE chains, symmetric chains, and CE cochains. The many-variable CY3 definition should inherit that distinction. The bar object is chain/coalgebraic; the observable CE object is cochain/algebraic.

4. **The `E_3` lift is already marked conditional.**
   The manuscript correctly says the `E_3` lift is Stage-1 data and not a consequence of framed `E_2`/BV alone (`cy3_chain_level_bridge.tex:612-650`). Any CE/bar theorem must keep the same hypothesis: fixed formality point \(F\), CY3 chain-level framing, and Costello-Li holomorphic witness.

5. **Weiss/Ran descent is asserted at adjacent surfaces, not proved for this exact functor.**
   The Hall-valued target requires full DWR Cech/Ran naturality (`cy3_chain_level_bridge.tex:223-260`). The local-to-toric package is explicitly conditional on a comparison map over the whole DWR nerve (`cy3_chain_level_bridge.tex:325-360`). The missing hCS-to-Hall comparison is open (`cy3_chain_level_bridge.tex:430-486`). For the left-end CE object, the manuscript should prove a smaller descent lemma: compact-support Dolbeault fields form a nuclear cosheaf, and continuous CE cochains turn disjoint unions into completed tensor products.

6. **The executable CE tests are finite/truncated, not continuous analytic tests.**
   `compute/tests/test_chiral_ce_complex.py:792-907` independently verifies the finite PBW/CE statement. It does not model nuclear LF spaces, continuous strong duals, compact-support extension maps, or Ran descent. `compute/tests/test_dolbeault_cy3_homotopy.py:421-510` verifies Dolbeault homotopy witnesses, not their compatibility with continuous CE and `E_3` bar duality.

7. **Stale class-M assertions remain in the named CE test.**
   `compute/tests/test_chiral_ce_complex.py:619-627` and `:776-781` assert class M `E_3` bar cohomology is infinite. The current stronger engine says \(E_4=(3t(1+t))^g\), total \(6^g\), and \(E_4=E_\infty\) for \(g\le 3\) (`compute/lib/e3_bar_higher_genus_class_m.py:1-69`; tests at `compute/tests/test_e3_bar_higher_genus_class_m.py:1-29`). This is separate from the continuous CE/bar proof, but it is an executable contradiction on the bar side.

## Theorem Spine To Inscribe

### Definition A2.1: Nuclear Dolbeault-Jet Convention

Let \(P\subset\mathbb C^3\) be a relatively compact holomorphic polydisc. Topologize
\[
  J^\infty_{\mathrm{hol}}\mathfrak l_{\mathcal C}
\]
as the completed inverse limit of finite holomorphic jet bundles with its nuclear Fréchet/pro-Fréchet topology. Put
\[
  \mathfrak L_c(P)
  =
  \Omega_c^{0,\bullet}(P,J^\infty_{\mathrm{hol}}\mathfrak l_{\mathcal C})[1]
\]
with its standard strict nuclear LF topology, the inductive limit over compact subsets \(K\Subset P\) of nuclear Fréchet spaces of smooth forms supported in \(K\). Use the completed projective tensor product \(\widehat\otimes_\pi\). Use the strong continuous dual \((-)^\vee_b\).

This definition belongs immediately before `cy3_chain_level_bridge.tex:101`.

### Lemma A2.2: Continuity Of The Dolbeault-Jet dg Lie Algebra

The operators
\[
  \bar\partial,\quad d_{\mathfrak l},\quad
  [-,-]\colon \mathfrak L_c(P)\widehat\otimes_\pi\mathfrak L_c(P)\to\mathfrak L_c(P)
\]
are continuous. For disjoint polydiscs \(P_1,\ldots,P_r\subset P\),
\[
  \bigoplus_i \mathfrak L_c(P_i)\xrightarrow{\sim}\mathfrak L_c(\bigsqcup_iP_i)
\]
is a topological isomorphism of nuclear LF complexes.

Proof: compact support gives extension by zero; nuclearity makes projective tensor products exact; the bracket is wedge of smooth compactly supported forms tensored with the finite/pro-finite jet bracket.

### Lemma A2.3: Continuous CE Cochains Are Classical Observables

Define
\[
  C^\bullet_{\mathrm{CE,cont}}(\mathfrak L_c(P))
  :=
  \prod_{n\ge 0}
  \mathrm{Hom}_{\mathrm{cont}}\bigl(\widehat{\mathrm{Sym}}^n_\pi(\mathfrak L_c(P)[1]),\mathbb C\bigr)
  =
  \widehat{\mathrm{Sym}}\bigl(\mathfrak L_c(P)^\vee_b[-1]\bigr)
\]
with differential \(d_{\mathrm{CE}}+\bar\partial^\vee+d_{\mathfrak l}^\vee\). This is the Costello-Gwilliam classical observable algebra on compactly supported fields. For disjoint \(P_i\),
\[
  C^\bullet_{\mathrm{CE,cont}}\!\left(\bigoplus_i\mathfrak L_c(P_i)\right)
  \cong
  \widehat\otimes_i
  C^\bullet_{\mathrm{CE,cont}}(\mathfrak L_c(P_i)).
\]

This heals `cy3_chain_level_bridge.tex:125-131` without changing its mathematical intent.

### Lemma A2.4: `E_3` Bar/CE Chain Comparison

Assume the Stage-1 `E_3` datum fixed in `cy3_chain_level_bridge.tex:612-650`: formality point \(F\), CY3 chain-level framing, and Costello-Li holomorphic witness. Then the factorisation envelope satisfies
\[
  B_{E_3}\bigl(U^{\mathrm{fact},E_3}_P(\mathfrak L_c)\bigr)
  \simeq
  \mathrm{CE}^{\mathrm{ch},E_3}_*(\mathfrak L_c(P))
\]
as completed conilpotent coalgebras in nuclear complexes. This is the many-variable analogue of the finite PBW/CE statement at `quantum_chiral_algebras.tex:478-501`, not a cochain statement.

### Proposition A2.5: Continuous Dual CE/Bar Identification

Under the hypotheses of Lemma A2.4 and nuclear reflexivity on the chosen completed subcategory,
\[
  C^\bullet_{\mathrm{CE,cont}}(\mathfrak L_c(P))
  \simeq
  \left(
    B_{E_3}U^{\mathrm{fact},E_3}_P(\mathfrak L_c)
  \right)^\vee_b .
\]
The proof is formal after Lemmas A2.2-A2.4: continuous duality sends completed direct sums to products, completed tensor coalgebras to completed symmetric function algebras, and the CE differential to the dual bar differential.

This is the strongest correct replacement for the direct equality in `cy3_chain_level_bridge.tex:132-143`.

### Proposition A2.6: Weiss/Ran Descent For The Left End

Let \(\mathcal B_{\mathrm{poly}}\) be a Weiss-cofinal Stein-polydisc basis as in `cy3_chain_level_bridge.tex:226-229`. The assignment
\[
  P\mapsto C^\bullet_{\mathrm{CE,cont}}(\mathfrak L_c(P))
\]
with products induced by disjoint compact supports is a classical factorisation algebra satisfying Weiss descent. Its Ran extension over finite polydisc configurations satisfies:

- disjoint-union multiplicativity by Lemma A2.3;
- diagonal collision by the local-cohomology residue normal form already written at `cy3_chain_level_bridge.tex:148-180`;
- associativity by equality of nested residues/Fulton-MacPherson boundary orientation, provided the residue maps are declared continuous for the chosen topology.

This proves the left-end Stage-1 descent. It does not produce \(\Theta_{\hCS\to\Hall}\).

## Claim-Status Recommendations

- Add Definition A2.1 as `ClaimStatusDefinitional`.
- Lemmas A2.2 and A2.3 can be `ClaimStatusProvedHere` if the manuscript states the nuclear LF/Fréchet facts explicitly.
- Lemma A2.4 should be `ClaimStatusConditional` on the fixed Stage-1 `E_3` datum, matching `cy3_chain_level_bridge.tex:612-650`.
- Proposition A2.5 should be `ClaimStatusConditional` on Lemma A2.4 plus the continuous-dual convention.
- Proposition A2.6 can be `ClaimStatusProvedHere` for the left-end classical factorisation algebra, and must explicitly exclude Hall comparison and quantum renormalisation.
- Keep `op:cy3-hcs-hall-comparison` open.
- Keep quantum observables conditional on BV renormalisation/anomaly cancellation, as already stated in `quantum_chiral_algebras.tex:20-33`.

## Anchors

- Many-variable CE model: `chapters/theory/cy3_chain_level_bridge.tex:101-196`.
- Hall/DWR target and full comparison category: `chapters/theory/cy3_chain_level_bridge.tex:223-260`.
- Conditional local-to-toric descent: `chapters/theory/cy3_chain_level_bridge.tex:325-360`.
- Open hCS-to-Hall comparison: `chapters/theory/cy3_chain_level_bridge.tex:430-486`.
- Stage-1 `E_3` lift is extra data: `chapters/theory/cy3_chain_level_bridge.tex:612-650`.
- Stage-1 envelope and its scope: `chapters/theory/cy3_chain_level_bridge.tex:679-716`, `:786-813`.
- Two-stage \(\Phi_d\): `chapters/theory/cy_to_chiral.tex:249-304`, `:537-572`.
- Chiral CE chains/cochains distinction: `chapters/theory/quantum_chiral_algebras.tex:455-490`.
- PBW finite CE/bar proposition: `chapters/theory/quantum_chiral_algebras.tex:478-501`.
- Stage-2 Ran structure: `chapters/theory/e1_chiral_algebras.tex:363-454`.
- Current finite CE tests: `compute/tests/test_chiral_ce_complex.py:792-907`.
- Dolbeault homotopy tests: `compute/tests/test_dolbeault_cy3_homotopy.py:421-510`.

## Executable Tests To Add Or Repair

1. Add a small `continuous_ce_bar_model` test engine with finite jet cutoffs \(J^N\) and explicit metadata:
   `topology="nuclear_lf"`, `dual="strong_continuous"`, `tensor="completed_projective"`.
   Reject algebraic-dual mode.

2. Test disjoint-union multiplicativity:
   for finite truncations \(V_N,W_N\),
   \[
   \dim \widehat{\mathrm{Sym}}^m((V_N\oplus W_N)^\vee)
   =
   \sum_{a+b=m}\dim \widehat{\mathrm{Sym}}^a(V_N^\vee)\dim \widehat{\mathrm{Sym}}^b(W_N^\vee).
   \]
   This is the executable finite-cutoff shadow of
   \(CE_{\mathrm{cont}}^*(L_1\oplus L_2)\cong CE_{\mathrm{cont}}^*(L_1)\widehat\otimes CE_{\mathrm{cont}}^*(L_2)\).

3. Add a compact-support extension test:
   model three disjoint polydiscs \(P_i\), extension by zero into \(P\), and verify associativity of
   \((CE(P_1)\widehat\otimes CE(P_2))\widehat\otimes CE(P_3)\to CE(P)\)
   equals
   \(CE(P_1)\widehat\otimes(CE(P_2)\widehat\otimes CE(P_3))\to CE(P)\).

4. Add a finite Laurent-residue test:
   coefficient extraction in three normal directions commutes with nested partition refinement, matching `cy3_chain_level_bridge.tex:148-180`.

5. Repair `compute/tests/test_chiral_ce_complex.py:619-627` and `:776-781` so class M no longer asserts infinite `E_3` bar cohomology. It should import `E3BarHigherGenusClassM` and assert \(6^3=216\) at genus \(3\), while keeping \(g\ge4\) conditional on higher differentials.

6. Add a noncoverage test marker or metadata check proving the existing finite CE suite is not being used as evidence for continuous duality. The finite PBW test is valid, but it is not the many-variable theorem.

## Verification Run

- `python -m pytest ...` failed because `python` is not on this shell path.
- `python3 -m pytest compute/tests/test_chiral_ce_complex.py compute/tests/test_dolbeault_cy3_homotopy.py`: 142 passed in 0.47s.
- `python3 -m pytest compute/tests/test_e3_bar_higher_genus_class_m.py`: 170 passed in 0.34s.

## Files Changed

Only this report:

- `notes/adversarial_swarm_20260424_frontier_resolution/agent_A2_ce_bar.md`
