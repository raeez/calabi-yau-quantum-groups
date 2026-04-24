# Agent 05 Report: K3 x E, BKM, Yangian

## Scope

Anchors audited:

- `chapters/examples/k3e_bkm_chapter.tex`
- `chapters/examples/k3_yangian_chapter.tex`
- `chapters/examples/k3_chiral_algebra.tex`
- `chapters/examples/k3_quantum_toroidal_chapter.tex`
- `chapters/examples/k3_chiral_bialgebra_platonic.tex`
- `compute/lib/k3_yangian_adversarial.py`
- `compute/lib/k3_yangian_borcherds_weight_theta_refinement.py`
- `compute/lib/k3_yangian_unified_cross_check.py`
- `compute/lib/k3_yangian_whole_object_verifier.py`
- `compute/lib/hyperkahler_BKM_lift.py`
- `compute/scripts/verify_igusa_high_precision.py`

Verdict: CONVERGED with five repairs proposed. The mathematics is mostly protected by local guardrails, but two status/convention collisions and three wording hazards remain capable of reintroducing the forbidden identifications:

1. BKM-as-Yangian.
2. Delta_5 input/output collapse.
3. Four-construction spectrum drift.
4. Lie-level abelianity versus vertex-level nonabelianity.
5. CHL/Borcherds-weight family collision.

No manuscript files were edited in this pass. This report is the only file written.

Verification run:

```bash
PYTHONDONTWRITEBYTECODE=1 pytest -q -p no:cacheprovider \
  compute/tests/test_k3_yangian_adversarial.py \
  compute/tests/test_k3_yangian_borcherds_weight_theta_refinement.py \
  compute/tests/test_hyperkahler_BKM_lift.py \
  compute/tests/test_k3_yangian_unified_cross_check.py
```

Result: `240 passed in 3.64s`.

Direct high-precision Igusa check:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 compute/scripts/verify_igusa_high_precision.py
```

Result: the script verifies the sign-correct Borcherds product for Delta_5 at seven points, with the absorbed-sign ratio equal to `+1` to 25--58 decimal digits.

## ATTACK_1: BKM-as-Yangian status collision

Claim attacked: the K3 x E BKM-side object is not a Drinfeld Yangian. The correct BKM-side object is the Hall--Drinfeld double / BKM quantisation attached to the Delta_5 denominator datum; the historical "K3 Yangian" branch is the separate K3/Mukai self-mirror branch.

Failure mode found:

- `chapters/examples/k3_yangian_chapter.tex:35`--`53` correctly states the guardrail: the BKM-side K3 object is not a Drinfeld Yangian and lacks a Drinfeld `J`-presentation, Kac--Moody Cartan, and Weyl action on imaginary simple roots.
- `chapters/examples/k3_yangian_chapter.tex:160`--`175` again correctly routes the Delta_5 object through a Hall--Drinfeld double, not through a standard Yangian presentation.
- `chapters/examples/k3_yangian_chapter.tex:2225`--`2262` then over-promotes the situation: it says the generalized Yangian has been explicitly constructed as `Y_hbar^super(g_Delta5)` and that the former "no framework exists" statement is upgraded to a constructed framework.
- The same chapter later contradicts that upgrade: `chapters/examples/k3_yangian_chapter.tex:2288`--`2292` says no Drinfeld presentation exists for a BKM with nontrivial imaginary roots, and `chapters/examples/k3_yangian_chapter.tex:10440`--`10463` keeps the full nonabelian extension and the `Y_osp(4|20)` bridge conjectural.
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:5003`--`5055` and `5451`--`5459` similarly state that an explicit super-Yangian presentation discharges the open conjecture, while `chapters/examples/k3_chiral_bialgebra_platonic.tex:7034`--`7035` still marks the full bialgebra identification
  `A^{M,Omega}_{prot} = Y_hbar^super(g_Delta5) = D(CoHA)` as conjectural.
- Compute-side guardrails agree with the conservative reading: `compute/lib/k3_yangian_adversarial.py:42`--`52` and `379`--`428` identify `g_Delta5` as the obstruction to a standard Yangian presentation and keep BKM multiplicities as bar-complex / denominator data, not Yangian generators.

HEAL_1:

1. In `chapters/examples/k3_yangian_chapter.tex:2230`, replace the status-upgrade heading by:

   ```tex
   \subsection{Candidate super-Yangian presentation; full Hall--Drinfeld/BKM identification remains conjectural}
   ```

2. Replace the prose at `chapters/examples/k3_yangian_chapter.tex:2232`--`2262` by the following separation:

   ```tex
   The platonic chapter supplies a Serre--Borcherds-style formal presentation
   denoted \(Y^{\mathrm{super}}_{\hbar}(\mathfrak g_{\Delta_5})\).  This is
   not a Drinfeld Yangian presentation of \(\mathfrak g_{\Delta_5}\), and it
   does not by itself identify the resulting algebra with
   \(\mathcal D_{\hbar}(\mathrm{CoHA}_{K3\times E})\).  The proved content is
   the stated presentation/PBW consistency in that chapter's convention; the
   Hall--Drinfeld double identification and the full chiral bialgebra
   comparison remain conjectural unless the CY-C and BKM quantisation inputs
   are supplied.
   ```

3. In `chapters/examples/k3_chiral_bialgebra_platonic.tex:5049`--`5055`, either demote `\ClaimStatusProvedHere` to a conditional/conjectural status, or narrow the theorem title to:

   ```tex
   \begin{theorem}[PBW consistency of the Serre--Borcherds presentation]
   ```

   with an explicit sentence saying that the theorem proves internal presentation consistency, not a standard Yangian structure and not the full `D(CoHA)` identification.

4. Preserve `chapters/examples/k3_yangian_chapter.tex:10440`--`10463` and `chapters/examples/k3_chiral_bialgebra_platonic.tex:7034`--`7035` as the governing scope: the full nonabelian BKM/Yangian/Hall comparison remains conjectural.

## ATTACK_2: Delta_5 input/output collapse

Claim attacked: Delta_5 has two distinct roles and the manuscript must not collapse them. On the input side, Delta_5 is the Borcherds/Gritsenko--Nikulin denominator form fixing the BKM root data. On the output side, the platonic architecture argues that the same form is forced by the one-loop anomaly/paramodular calculation.

Failure mode found:

- `chapters/examples/k3e_bkm_chapter.tex:100`--`137` gives the correct two-role theorem: denominator input is fixed by Borcherds product data, while one-loop output is produced by the anomaly-cancellation argument.
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:5952`--`5959` repeats the same separation: DT input gives `1/Delta_5^2`, while the chiral quantisation side makes Delta_5 both denominator and one-loop output.
- `compute/scripts/verify_igusa_high_precision.py` confirms the denominator identity numerically. The sign-free absorbed form matches `(1/64) Delta_5` to high precision.
- The hazard is local wording. `chapters/examples/k3e_bkm_chapter.tex:889` titles a section "The denominator identity: Delta_5 = Phi", and `chapters/examples/k3e_bkm_chapter.tex:96` says the specialization produces the Borcherds--Delta_5 chiral algebra. Both are defensible in context, but they invite the false reading that `Phi_3` alone constructs Delta_5 without the external automorphic input and without the one-loop argument.

HEAL_2:

1. Rename `chapters/examples/k3e_bkm_chapter.tex:889` from:

   ```tex
   \section{The denominator identity: \(\Delta_5=\Phi\)}
   ```

   to:

   ```tex
   \section{The Weyl--Kac--Borcherds denominator identity for \(\Delta_5\)}
   ```

2. After `chapters/examples/k3e_bkm_chapter.tex:96`, insert:

   ```tex
   This is a specialization statement, not an autonomous construction of
   \(\Delta_5\) from \(\Phi_3\).  The denominator input is the
   Gritsenko--Nikulin/Borcherds automorphic product; the one-loop output
   statement is the separate paramodular anomaly-cancellation theorem in the
   platonic chapter.
   ```

3. Enforce labels in future prose:

   - "Delta_5 as denominator input" for BKM root-data construction.
   - "Delta_5 as Borcherds lift" for automorphic product statements.
   - "Delta_5 as one-loop output" only for the paramodular anomaly theorem.

4. Keep `compute/scripts/verify_igusa_high_precision.py` as the denominator-product witness, not as evidence for the one-loop-output claim.

## ATTACK_3: Four-construction spectrum drift

Claim attacked: the K3 x E construction spectrum is the four-value spectrum

```tex
\{\kappa_{\mathrm{cat}}(K3\times E),
  \kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3\times E),
  \kappa_{\mathrm{BKM}}(\Delta_5),
  \kappa_{\mathrm{fiber}}(K3\times E)\}
= \{0,3,5,24\}.
```

The fibre witness `\kappa_{\mathrm{cat}}(K3)=2` and the compact/BV Hodge value `\kappa_{\mathrm{ch},BV}(K3\times E)=0` are separate annotations, not extra entries in the four-construction spectrum.

Failure mode found:

- `chapters/examples/k3_chiral_bialgebra_platonic.tex:6948`--`6960` is the cleanest canonical statement: four values `{0,3,5,24}`, plus the separate compact BV value `0`.
- `chapters/examples/k3_quantum_toroidal_chapter.tex:718`--`741` is also clean: it separates K3 fibre values from K3 x E total-space values.
- `chapters/examples/k3e_bkm_chapter.tex:67`--`80` calls the display a "four kappa spectrum" but lists compact total-space `0`, compact chiral `0`, BKM `5`, and fibre `24`; it omits the Heisenberg value `3` that the later canonical spectrum requires.
- `chapters/examples/k3_chiral_algebra.tex:21`--`33`, `250`--`266`, and `348`--`351` sometimes package `{0,2,3,5,24}` as the K3 x E spectrum. That wording is imprecise because `2` is the K3 fibre Hodge/Euler witness, not a total-space K3 x E construction value.
- `chapters/examples/k3_chiral_algebra.tex:250` says "All five kappa values" while the table has six rows once both `\kappa_{\mathrm{cat}}(K3)` and `\kappa_{\mathrm{ch}}(K3)` are displayed.

HEAL_3:

1. Use this canonical sentence wherever the K3 x E spectrum is summarized:

   ```tex
   For \(Y=K3\times E\), the four construction values are
   \[
     \kappa_{\mathrm{cat}}(Y)=0,\qquad
     \kappa_{\mathrm{ch}}^{\mathrm{Heis}}(Y)=3,\qquad
     \kappa_{\mathrm{BKM}}(\Delta_5)=5,\qquad
     \kappa_{\mathrm{fiber}}(Y)=24.
   \]
   The fibre witness \(\kappa_{\mathrm{cat}}(K3)=2\) and the compact
   BV/Hodge value \(\kappa_{\mathrm{ch},BV}(Y)=0\) are recorded separately.
   ```

2. In `chapters/examples/k3e_bkm_chapter.tex:67`--`80`, either add the missing Heisenberg value `3` and move compact chiral `0` to a separate sentence, or retitle the display as a compact/BV reconciliation rather than the four-construction spectrum.

3. In `chapters/examples/k3_chiral_algebra.tex:21`--`33`, replace the phrase "spectrum `{0,2,3,5,24}`" by "four construction values `{0,3,5,24}` plus the fibre witness `2`".

4. In `chapters/examples/k3_chiral_algebra.tex:250`--`266`, split the table into:

   - K3 x E construction values: `0,3,5,24`.
   - Fibre/compact witnesses: `2` and compact/BV `0`.

5. Treat `chapters/examples/k3_chiral_bialgebra_platonic.tex:6948`--`6960` and `chapters/examples/k3_quantum_toroidal_chapter.tex:718`--`741` as the local canonical references.

## ATTACK_4: Lie-level abelianity versus vertex-level nonabelianity

Claim attacked: the primary K3/Mukai Heisenberg input is abelian modulo its centre, but the Delta_5 BKM root algebra is nonabelian after vertex closure. The manuscript must not say that `g_Delta5` itself is abelian.

Failure mode found:

- `chapters/examples/k3e_bkm_chapter.tex:700`--`782` correctly derives the BKM algebra from vertex closure.
- `chapters/examples/k3e_bkm_chapter.tex:870`--`886` is the key guardrail: `g_Delta5` is nonabelian as a root-space Lie algebra, but its nonabelianity is derived from the vertex OPE on abelian-mod-centre Heisenberg input.
- `chapters/examples/k3_yangian_chapter.tex:70`--`116` also says the Heisenberg mode algebra is abelian modulo centre and that nonabelian BKM brackets arise after vertex exponentials.
- The hazard is `chapters/examples/k3_yangian_chapter.tex:56`--`67`, which says that both `g_K3` and `g_Delta5` are abelian when restricted to a single Miki/Heisenberg factor. In isolation this can be read as saying that `g_Delta5` itself is abelian, contradicting the BKM root-space theorem.
- Compute-side evidence supports the stricter wording: `compute/lib/k3_yangian_adversarial.py:197`--`199` and `227`--`235` keep the abelian gl_1 stratum separate from the nonabelian enhancement; `compute/lib/k3_yangian_adversarial.py:379`--`428` says the input is `H_Muk`, not `g_Delta5`.

HEAL_4:

1. Replace the first sentence of `chapters/examples/k3_yangian_chapter.tex:56`--`67` by:

   ```tex
   The Lie-primary Heisenberg inputs underlying the K3 and \(K3\times E\)
   branches are abelian modulo their centres.  The BKM algebra
   \(\mathfrak g_{\Delta_5}\) itself is not abelian: its nonabelian root-space
   brackets are produced only after the Frenkel--Kac/Borcherds vertex closure.
   ```

2. Add one sentence after the theorem at `chapters/examples/k3_yangian_chapter.tex:70`--`116`:

   ```tex
   Thus "abelian at Lie level" refers to the Heisenberg input algebra, not to
   the resulting BKM root Lie algebra.
   ```

3. Preserve `chapters/examples/k3e_bkm_chapter.tex:870`--`886` as canonical, since it already states the exact separation.

4. In future uses of "abelian-at-Lie", require an object qualifier:

   - Correct: "the Heisenberg/Mukai input is abelian modulo centre."
   - Incorrect: "`\mathfrak g_{\Delta_5}` is abelian at Lie level."

## ATTACK_5: CHL/Borcherds-weight convention collision

Claim attacked: the default CHL/Borcherds-weight formula is

```tex
\kappa_{\mathrm{BKM}}(\Phi_N)=c_N(0)/2,
\qquad
N\in\{1,2,3,4,6\}.
```

With the default Gritsenko--Clery/CHL normalization, the values are `{5,4,3,2,1}`. The alternative twined/singular-weight family must carry an explicit superscript and must not be written as the default `\kappa_{\mathrm{BKM}}(\Phi_N)`.

Failure mode found:

- `compute/lib/k3_yangian_borcherds_weight_theta_refinement.py:12`--`18`, `35`--`40`, `94`--`139`, and `161`--`176` verify the default formula and the values `{5,4,3,2,1}`.
- `chapters/examples/k3e_bkm_chapter.tex:11561`--`11578` states the same default theorem for the BKM-denominator scope.
- `chapters/examples/k3e_bkm_chapter.tex:11584`--`11587` then introduces a second paramodular family on the same CHL index set, with weights `(5,2,1,1,1)`, but the notation does not sufficiently prevent this from being read as the same `\kappa_{\mathrm{BKM}}(\Phi_N)`.
- `chapters/examples/k3e_bkm_chapter.tex:12053`--`12055` says the programme-core Gritsenko lift weights are `{5,2,1,1,1}`, which conflicts with the default theorem and compute witness unless it is explicitly marked as the second family.
- `compute/lib/hyperkahler_BKM_lift.py:73`--`84` adds a second convention hazard: the manuscript `g_Delta5` convention uses `c(0)=10` and weight `5`, while the DMVV/Igusa `Phi_10` convention uses `c(0)=20` and weight `10`. These are distinct BKM superalgebras/conventions, not interchangeable normalizations inside one formula.

HEAL_5:

1. Declare the default convention once near `chapters/examples/k3e_bkm_chapter.tex:11561`:

   ```tex
   Unless a superscript is displayed, \(\kappa_{\mathrm{BKM}}(\Phi_N)\)
   denotes the Gritsenko--Clery/CHL denominator family with values
   \((5,4,3,2,1)\) for \(N=1,2,3,4,6\).
   ```

2. Rename the second family everywhere it appears, for example:

   ```tex
   \kappa_{\mathrm{BKM}}^{\mathrm{tw}}(\Phi_N)=(5,2,1,1,1).
   ```

   Any use of `(5,2,1,1,1)` without this superscript should be treated as a convention bug.

3. Edit `chapters/examples/k3e_bkm_chapter.tex:12053`--`12055` to one of the following:

   - If the default family is intended:

     ```tex
     \{\kappa_{\mathrm{BKM}}(\Phi_N):N=1,2,3,4,6\}=\{5,4,3,2,1\}.
     ```

   - If the second family is intended:

     ```tex
     \{\kappa_{\mathrm{BKM}}^{\mathrm{tw}}(\Phi_N):N=1,2,3,4,6\}=\{5,2,1,1,1\}.
     ```

4. Add a cross-reference from the default theorem to `compute/lib/k3_yangian_borcherds_weight_theta_refinement.py`, and from the convention note to `compute/lib/hyperkahler_BKM_lift.py:73`--`84`.

5. Keep `\Delta_5` weight `5` and `\Phi_{10}` weight `10` visibly separated. The identity `Z^{red}_{DT}=-\Phi_{10}^{-1}=-\Delta_5^{-2}` is a character-level square relation, not permission to identify the two BKM denominator conventions.

## Final Recommendations

The five repairs above are local and should be made before any further architecture-level inscription touches K3 x E. The highest-priority edits are:

1. Demote or narrow the "super-Yangian constructed" claims so they do not override the conjectural Hall--Drinfeld/BKM identification.
2. Canonicalize the K3 x E four-construction spectrum as `{0,3,5,24}` with fibre `2` and compact/BV `0` recorded separately.
3. Add superscripted notation for the second CHL/twined Borcherds-weight family.

After those edits, rerun:

```bash
PYTHONDONTWRITEBYTECODE=1 pytest -q -p no:cacheprovider \
  compute/tests/test_k3_yangian_adversarial.py \
  compute/tests/test_k3_yangian_borcherds_weight_theta_refinement.py \
  compute/tests/test_hyperkahler_BKM_lift.py \
  compute/tests/test_k3_yangian_unified_cross_check.py
PYTHONDONTWRITEBYTECODE=1 python3 compute/scripts/verify_igusa_high_precision.py
```
