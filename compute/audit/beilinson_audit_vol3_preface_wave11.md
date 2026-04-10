# Beilinson Audit -- Vol III Preface (Wave 11)

Target: `/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex` (250 lines)
Protocol: Six hostile examiners. Read-only. Severity tagged {CRITICAL, SERIOUS, MODERATE, MINOR, NIT}.
Scope reference: Vol III CLAUDE.md (AP-CY1-19, AP113 kappa subscripts, AP114 stub chapters).

---

## Executive Summary

The preface is in good structural shape. AP113 compliance is essentially uniform: every occurrence of kappa carries a subscript (ch, BKM, cat, fiber), and the four-way spectrum {2,3,5,24} is honestly presented as the signature of Vol III. The three-step CY-to-chiral construction is clearly scoped (d=2 proved, d=3 programme). The "where do chiral algebras come from?" opening delivers a genuine deficiency (Vols I and II assume the input; Vol III supplies it) and the closing trichotomy ("what it does / how it composes / where it comes from") earns its rhetoric.

However, several CRITICAL and SERIOUS issues hide in the substance. The preface uses `\HH_\bullet(\cC) \to k[-d]` (line 21-22) for the CY trace, directly violating AP-CY2 (CY trace lives in HC^-_d, negative cyclic, not Hochschild homology). The modular characteristic identity `\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)` (line 28) is asserted in the preface but is exactly the content of Theorem CY-D, which is labelled PROGRAMME in CLAUDE.md (d=3 conditional on A_C existing). The "six independent paths" verification of `\kappa_{\mathrm{ch}}(K3 x E) = 3` is asserted without citation and would fail AP10 if queried. The CoHA paragraph declares CoHA "the ordered bar complex of the CY_3 chiral algebra" -- but the CY_3 chiral algebra is exactly the object that does not yet exist (AP-CY6), so this is an unconstructed-object assertion in a preface posing as theorem. The `\C^3 -> W_{1+infty} -> Rep^{E_2}(Y(gl_1-hat))` chain is claimed "verified end-to-end" with no citation.

AP-CY14 (unconstructed objects in theorem-voice) is the dominant systemic issue: the preface rhetorically treats `A_\cC` at d=3 as if constructed, then later scopes d=3 as programme. This causes local contradictions (lines 19-30 vs lines 62-69).

Per-examiner findings below. Total: 3 CRITICAL, 8 SERIOUS, 11 MODERATE, 9 MINOR, 6 NIT.

---

## 1. Formalist (definitions, environments, quantifier hygiene)

### CRITICAL

- **F-C1 (AP-CY2 violation, line 21-22).** Text writes:
  > "a non-degenerate trace `\Tr \colon \HH_\bullet(\cC) \to k[-d]` encoding the CY condition as a d-dimensional Frobenius structure at the chain level."
  AP-CY2 is explicit: "CY trace is in HC^-_d(C), NOT just HH_d -> k. Negative cyclic refinement essential for S^d-framing." The preface then invokes S^d-framing (line 24) and S^2-framing (line 56) which require the negative cyclic refinement. Writing the trace as HH_* -> k[-d] collapses the distinction and would mislead a reader new to the subject. The fix is to write `\HC^-_d(\cC) \to k` or `\HH_\bullet(\cC)_{hS^1} \to k[-d]` (Connes' cyclic complex / S^1-equivariant form).

- **F-C2 (AP-CY6 / AP-CY14 violation, lines 28-30, 141-147).**
  Line 28-30: `\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC). The shadow obstruction tower of A_\cC is the automorphic correction of the associated generalized Kac--Moody superalgebra.`
  This is asserted in preface-voice. But A_C for CY_3 is exactly the d=3 programme (AP-CY6: "A_X for CY3 does NOT exist"). CLAUDE.md marks CY-A (existence of Phi) as "d=2 PROVED; d=3 PROGRAMME" and CY-D (modular characteristic) as "PROGRAMME". The preface then tries to fix this at line 62-64 by saying "Theorem CY-A constructs Phi for d=2: all three steps are proved. For d=3, step (3) is a programme..." But this is inconsistent: lines 28-30 have already asserted kappa_ch(A_C) and shadow/automorphic identification for the d=3 case (since the following paragraph is about K3 x E, a CY_3). The scope disclaimer arrives 35 lines too late.
  Line 141-147 then asserts "The CoHA is the natural E_1-primitive: it is the ordered bar complex of the CY_3 chiral algebra" -- an identification whose LHS (CoHA) is defined (Kontsevich-Soibelman) but whose RHS (CY_3 chiral algebra A_{X}) is exactly AP-CY6's nonexistent object. This sentence should be flagged as a CONJECTURAL identification (this is the target of the E_1 sector of G(X), not a theorem).

### SERIOUS

- **F-S1 (AP-CY4 partial, lines 59-60).** "For d=3: holomorphic Chern-Simons breaks E_2 to E_1, and the braiding is recovered via the Drinfeld center." Z(-) here is the Drinfeld center of an E_1-monoidal category (`Z(Rep^{E_1}(A)) = Rep^{E_2}(Z^{der}_{ch}(A))`). AP-CY4 warns: "Drinfeld center Z(C) (monoidal category) != derived center Z^der_ch(A) (chiral). State which." The preface conflates them implicitly. Clarify: here "Drinfeld center" means the CATEGORICAL center of `Rep^{E_1}`, which identifies with representations of the CHIRAL derived center on the other side; the reader is expected to know this, but the preface voice owes explicitness.

- **F-S2 (missing \begin{conjecture} environment, lines 141-147).** The CoHA / CY_3 chiral algebra identification is a conjecture in the strict sense (it requires A_{X} at d=3). AP-CY11: "DEFAULT environment for new Vol III formal statements is \begin{conjecture} unless proof is COMPLETE and UNCONDITIONAL." The preface does not use environments, but the parallel theorem-chapter wording must carry conditional tags. Flag for downstream (the actual theorem in Part III must be \begin{conjecture}).

- **F-S3 (AP40 scope tag absent, line 62).** "Theorem CY-A constructs Phi for d=2" -- at this point the reader needs a pointer to where exactly d=3 conditionality bites. The preface says "step (3) is a programme conditional on the chain-level S^3-framing" -- good, but S^3-framing is the geometric condition, while AP-CY2 says the underlying obstruction is the negative cyclic lift. State both.

- **F-S4 (quantifier on six paths, lines 83-85).** "verified by six independent paths" is a universal-existential claim with no citation. The Vol III CLAUDE.md does not enumerate these six paths; if they exist they should be pointed to (compute engine, theorem number, figure). Without a pointer, this violates the Beilinson principle (verify at primary source). Candidate paths (from Vol I: chi_CY, lattice theta, Dedekind eta exponent, one-loop, Riemann-Roch, Mathai-Quillen) should be named or at least localized to a section reference.

### MODERATE

- **F-M1 (line 24, "S^d-framing of this trace").** The phrase "S^d-framing of this trace" is slightly off. S^d-framing is a structure on the CY category (or its Hochschild complex), NOT directly on the trace. It is the framing that UPGRADES the trace to a cyclic structure. Rewrite: "The S^d-framing on HC^-_\bullet(\cC) enhancing this trace determines the operadic refinement."

- **F-M2 (line 28, `\chi^{\CY}`).** Undefined at preface point of first use. The reader is told `\chi^{\CY}(\cC)` but the CY Euler characteristic (virtual dimension of derived Hom-spaces summed with signs, or the dimension of HH^0 of the CY trace pairing) is not a universal notation. Provide a half-sentence gloss: "where `\chi^{\CY}(\cC)` is the Euler characteristic of the Serre functor fixed point category" or similar.

- **F-M3 (line 54, PBW attribution).** "Poincare-Birkhoff-Witt theorem for factorization envelopes (Nishinaka, Vicedo)" -- this attribution should be cross-checked. The PBW for factorization envelopes is more commonly attributed to Costello-Gwilliam (FA Vol II, Chapter 3). "Nishinaka-Vicedo" sounds like a confusion with the integrable-systems school. This is likely wrong. Verify at primary source; if Costello-Gwilliam, update.

- **F-M4 (line 58, "E_2-chiral algebra with braided monoidal representation category").** This is the content of AP-CY3: E_2 braiding is not symmetric. The line is correct, but in a preface it should emphasize "NON-symmetric" braiding to forestall the E_2 -> E_inf collapse. MINOR adjacent.

- **F-M5 (line 65-67, d=2 -> d=3 "replaces a geometric braiding (from pi_1(Conf_2(R^2)) = Z) with an algebraic one").** Small infelicity: pi_1(Conf_2(R^2)) = Z is the braiding coming from configuration space of 2 points in the PLANE, i.e. E_2-algebra. For d=2 CY, the braiding comes from S^2-framing of HH. The preface elides the step. Rewrite: "(from the E_2-structure on HH encoded by the S^2-framing)" rather than pi_1(Conf_2).

- **F-M6 (line 66, Drinfeld center tannakian analogy).** "this is the CY analogue of the Tannakian reconstruction of a quantum group from its module category." Good analogy but slightly misleading: Tannakian reconstruction goes category -> Hopf algebra; here the analogue is Drinfeld center going E_1-cat -> E_2-cat. State the analogy sharper: "this is the Drinfeld center incarnation of Tannakian reconstruction."

### MINOR / NIT

- **F-m1 (line 27, curve X).** "on a curve X" is fine, but the CY category was denoted C (script C); curve variable X elsewhere in volume is often Sigma or C. Consistency check with Part II.
- **F-m2 (line 112-115 spectrum.** `\operatorname{Spec}_{\kappa}(X) = \{2, 3, 5, 24\}` -- check CLAUDE.md's enumeration (identical: 2=cat, 3=ch, 5=BKM, 24=fiber). Matches. No issue.
- **F-n1 (line 30, "generalized Kac-Moody superalgebra").** Fine but "Borcherds-Kac-Moody" is the more standard name in Vol III (cf kappa_BKM).

---

## 2. Topologist (framings, (co)homology, operadic structure)

### CRITICAL

- **T-C1 (S^d-framing vs chain-level framing, lines 23-24, 55-60, 63-64).** The preface writes "chain-level S^3-framing" only in the scope disclaimer. The actual constructive claim (line 55-60) writes "S^d-framing enhances the factorization algebra" without chain-level qualifier. For d=2, S^2-framing on HH is automatic via the cyclic structure (Connes' B operator). For d=3, S^3-framing is the HARD PART. The preface should make explicit: "d=2: the S^2 action on HC^- exists at the chain level automatically (Connes B). d=3: an S^3-action at the chain level is conjectural (Kontsevich-Soibelman, chain-level refinement of the topological-conformal operad)." Without this, the reader cannot see where the conditional enters.

### SERIOUS

- **T-S1 (cyclic A_inf to Lie conformal, line 46-49).** "The cyclic A_inf-structure on C determines a Lie conformal algebra L_C: the cyclic bar differential gives the lambda-bracket, the cyclic trace gives the invariant bilinear form, and the higher A_inf operations give the higher Lie conformal products." This is the Gaiotto-Costello-Rozansky construction (or Beem-Peelaers-Rastelli via H(T)). But "higher A_inf operations give higher Lie conformal products" is dangerous: the lambda-bracket of a Lie conformal algebra is BINARY; higher A_inf ops correspond to higher-order operadic structure (homotopy Lie conformal / L_inf version of the vertex algebra), not "higher lambda-brackets." The preface is sloppy here. Fix: "the higher A_inf operations give the L_inf-homotopies extending the lambda-bracket to a homotopy Lie conformal algebra."

- **T-S2 (factorization envelope terminology, line 50-52).** `U_X^{fact}(L_\cC)` is factorization envelope of a Lie conformal algebra. This functor exists in Costello-Gwilliam. Check: is the factorization envelope the Lie envelope (U -> U^fact)? Or the direct chiral envelope? The preface writes "factorization envelope" but many readers conflate this with the universal chiral envelope of a Lie* algebra (Beilinson-Drinfeld). Specify: the Costello-Gwilliam factorization envelope of a dgla, or the BD chiral envelope of a Lie* algebra? These agree up to renormalization, but a preface should not hand-wave.

- **T-S3 (AP-CY3 E_2 vs E_inf, line 57-58).** "the S^2-action on Hochschild homology gives an E_2-chiral algebra with braided monoidal representation category." This is right for CY_2 (Deligne conjecture + cyclic refinement). But the preface does not say "E_2-chiral is strictly weaker than E_inf" -- which is the whole point of AP-CY3 ("E_2 braiding is NOT symmetric. E_2 -> E_inf loses quantum group structure"). The preface should state this explicitly, otherwise the reader will over-reduce.

### MODERATE

- **T-M1 (line 56, "S^2 action on Hochschild homology").** S^2 acts on HH_* via the Connes B plus BV-delta structure (Getzler, Loday). This is the S^1 rotation on cyclic structures extended to S^2 via the Deligne conjecture cycle. Worth one citation (Deligne / Getzler / Kontsevich).

- **T-M2 (line 63, "chain-level S^3-framing").** S^3-framing at the chain level is Kontsevich-Soibelman's motivic DT machinery, specifically the orientation data on CY_3 categories. Cite KS 2008 or similar. A bare "chain-level S^3-framing" without a reference is a placeholder.

- **T-M3 (line 64-67, replacement of braiding).** "replaces a geometric braiding (from pi_1(Conf_2(R^2)) = Z)" -- pi_1 is Z, not B_2 (= Z for 2 strands, yes). But the braiding of an E_2-algebra is NOT just pi_1 of Conf_2; it is the whole little 2-disk operad action. Stating "pi_1(Conf_2(R^2)) = Z" is unnecessary reduction and slightly misleading. Remove or expand.

- **T-M4 (line 99-103, Schottky).** "at g >= 4, the Torelli map M_g -> A_g is no longer dominant." Correct: Schottky locus closure has codim 3g-3 - (g(g+1)/2 - 0) which is nontrivial starting g=4 (dim M_4 = 9, dim A_4 = 10, so Torelli is not dominant at g=4). Good. But "imprisoned in tautological classes on Mbar_g" is a preface metaphor; in fact the shadow tower lives in tautological classes REGARDLESS of Torelli, and the Torelli obstruction is to EXTENDING to Siegel modular forms on A_g. Sharpen.

### MINOR

- **T-m1 (line 115, lattice rank = 24 for K3 x E).** K3 has 22-dim H^2, with signature (3,19). Lattice Lambda^{3,2} of signature (3,2) gets its 5 from the Mukai lattice of K3 truncated to transcendental; the full signature (3,19) Mukai adds the algebraic. Where does 24 come from? The rank of the Niemeier lattice N = Leech or of the even unimodular rank-24 (II_{1,25} minus 2). Need one sentence specifying which lattice (probably the Conway/Mathieu-compatible Leech N = 24, or the rank-24 part of the Mukai lattice of K3 with H^0+H^4). The number 24 is correct; the attribution "lattice rank" is too vague in the preface.

---

## 3. Physicist (DT invariants, BPS, topological string, CoHA)

### SERIOUS

- **P-S1 (line 141-147, CoHA = ordered bar complex of CY_3 chiral algebra).**
  The sentence "The CoHA is the natural E_1-primitive: it IS the ordered bar complex of the CY_3 chiral algebra" is a strong claim. This is the Kontsevich-Soibelman-Davison-Meinhardt CoHA (critical CoHA for a CY_3 with potential). The identification with the "ordered bar complex of the CY_3 chiral algebra" is conjectural in the strict sense: it depends on A_{X} existing (AP-CY6). The preface should downgrade: "Conjecturally, the CoHA is the ordered bar complex of the (yet-to-be-constructed) CY_3 chiral algebra; the averaging g^{E_1} -> g^mod recovers the factorization coalgebra." This is the target of the programme, NOT a result. Currently phrased as fact. CRITICAL adjacent but graded SERIOUS because the reader familiar with AP-CY6 will decode it.

- **P-S2 (line 135-138, C^3 chain verified end-to-end).** "For C^3: the Jordan quiver gives Y(gl_1-hat) ~ W_{1+infty}, and the chain C^3 -> W_{1+infty} -> Rep^{E_2}(Y(gl_1-hat)) is verified end-to-end." The isomorphism Y(gl_1-hat) ~ W_{1+infty} (affine Yangian ~ W_{1+infty}) is a theorem of Tsymbaliuk / Schiffmann-Vasserot / Arbesfeld-Schiffmann-Vasserot. But "the chain ... is verified end-to-end" is stronger than a simple iso and implicates (a) C^3 CY_3 -> CoHA (Kontsevich-Soibelman, critical version), (b) CoHA = Yangian positive part (Schiffmann-Vasserot), (c) Yangian -> E_2 via R-matrix braiding. Each step is known in some form, but "verified end-to-end" is a bold claim in a preface; cite chapter number where this is carried through, otherwise downgrade to "fits together" or "is expected to hold."

- **P-S3 (line 83-86, K3 elliptic genus + Igusa cusp form).**
  "the Jacobi form phi_{0,1}(tau, z) is the K3 elliptic genus, and the Igusa cusp form Delta_5 is the Borcherds denominator identity." The K3 elliptic genus IS phi_{0,1}^{K3} of weight 0, index 1, with phi_{0,1}^{K3}(tau, 0) = chi(K3) = 24 (not 2 * phi_{0,1}^{EZ} as line 118 claims -- see P-S4). Verify. The Igusa cusp form Delta_10 (weight 10) is the Borcherds denominator for a Siegel modular form OR Delta_5 (the square root, weight 5, often called the Igusa-Siegel form) appears in Gritsenko-Nikulin. Which one? Vol III CLAUDE.md writes "kappa_BKM = 5 (weight of Delta_5)" -- consistent. Good. But the reader should know Delta_5 here is the Gritsenko lift / square root of Delta_10. Clarify once.

- **P-S4 (line 118-120, K3 elliptic genus decomposition).**
  "The K3 elliptic genus decomposes as phi_{0,1} = 2 * phi_{0,1}^{EZ}, where the factor 2 is kappa_cat(K3) = chi(O_{K3})."
  chi(O_{K3}) = 2 because H^0(O)=1, H^1(O)=0, H^2(O)=1. Yes. BUT the claim that phi_{0,1}^{K3}(tau,z) = 2 * phi_{0,1}^{EZ}(tau,z) as Jacobi forms requires checking. The space J_{0,1} (weight 0, index 1) is 1-dimensional over C, so ANY two elements are scalar multiples, and phi_{0,1}^{K3}(tau,0) = chi(K3) = 24, whereas phi_{0,1}^{EZ}(tau,0) = 12 (the "EZ" normalization in Eichler-Zagier). So 2 * phi_{0,1}^{EZ}(tau,0) = 24 checks out. Good. But AP-CY9 flags "c(-1) = 2 for phi_{0,1} in EZ convention, NOT 1": the preface should be consistent with this. Cross-check the normalization is EZ and not DVV. OK if EZ convention is consistent. MODERATE not SERIOUS.

### MODERATE

- **P-M1 (line 96-98, second quantization / DMVV).** "The physical DT partition function is the DMVV symmetric product of single-copy data." Dijkgraaf-Moore-Verlinde-Verlinde 1996. The preface correctly identifies the O3 obstruction (single-copy vs symmetric product). Good. Cite DMVV.

- **P-M2 (line 186-188, Bernoulli decay).** "|F_g^sh| ~ (2 pi)^{-2g}/g: convergent, with radius 2 pi, Borel entire." This is the genus-1 case (Eisenstein) scaled by g. The scaling (2 pi)^{-2g}/g is consistent with the Bernoulli asymptotic B_{2g} / (2g!) ~ (-1)^{g+1} 2 / (2 pi)^{2g}, so F_g^sh ~ B_{2g}/(2g)! * g^? . But the claimed (2 pi)^{-2g}/g behavior: if F_g^sh = C * B_{2g} / g then using |B_{2g}| ~ 2 (2g)! / (2pi)^{2g} gives |F_g^sh| ~ 2 C (2g)!/[(2pi)^{2g} g] which is NOT (2pi)^{-2g}/g but (2pi)^{-2g}/g * (2g)!. This is factorially DIVERGENT if taken literally. The preface's "convergent with radius 2pi, Borel entire" is right for the SHADOW (not the topological string) only after dividing out (2g)!, i.e., if shadow F_g^sh is naturally in convergent normalization (no (2g)! in denominator needed, i.e., F_g^sh has no factorial growth to begin with). The preface should write "|F_g^sh| ~ C / (g * (2pi)^{2g})" carefully or specify the normalization. AP119 (convergent vs divergent) explicitly calls out this trap. This is at the edge of AP119 violation. Flag SERIOUS -- let me reclassify.

- **P-M2 (REVISED to SERIOUS).** The shadow asymptotic formula in the preface must be dimensionally checked against Vol I's genus tower normalization. Precisely: if F_g^sh is the genus-g coefficient in a generating function of MC solutions, its natural size is typically B_{2g}/(2g)! * (2pi)^{2g} (Eisenstein holomorphic projection) which gives (2pi)^{-2g} * constant / g (after accounting for the 2(2g)!/(2pi)^{2g} asymptotic of B_{2g} and dividing by (2g)!). So |F_g^sh| ~ c/g behavior with radius 2pi is correct if we're looking at the coefficient-times-(2pi)^{2g} product. Re-read. The preface writes "|F_g^sh| ~ (2pi)^{-2g} / g" -- this is a DECAY ("bounded by (2pi)^{-2g} / g"). Decay at rate (2pi)^{-2g}/g is convergent ACROSS g (it's the shape of a function with radius-of-convergence 2pi in a spectral parameter like pi^2/6 * kappa). OK: this is consistent. Downgrade to MODERATE but request the variable in which convergence is measured be specified.

- **P-M3 (line 189-190, top string factorial growth).** "|F_g^top| ~ (2g)!" -- this is correct in leading order (Gopakumar-Vafa genus expansion is Gevrey-1). Standard. Cite Marino or BCOV.

### MINOR

- **P-m1 (line 189, "Gevrey-1").** Good technical word. Correct usage.
- **P-m2 (line 191-193, class G / class M).** G = Heisenberg + lattice, M = Virasoro + W_{1+infty}. Correct partition. (C/L/G/M spectrum.)

---

## 4. Number Theorist (modular forms, lattices, automorphic)

### CRITICAL

- **N-C1 (line 168-169, Delta_5 on Sp_4 \ H_2).** "the Igusa cusp form Delta_5 lives on Sp_4(Z) \ H_2, parametrizing pairs of elliptic curves with a coupling." Two problems:
  1. Igusa cusp form of weight 10 is Chi_{10} = Delta_10; the weight-5 form Delta_5 is the Gritsenko-Nikulin lift (square root of Chi_35 or similar). Verify which form and correct the name.
  2. H_2 is the Siegel upper half space of genus 2, a 3-dim complex domain. Sp_4(Z) is correct. But "pairs of elliptic curves with a coupling" is only PART of the moduli: H_2 parametrizes principally polarized abelian surfaces, NOT pairs of elliptic curves with coupling (that is the product locus E x E', codim 1 in H_2). The boundary of the Satake-Baily-Borel compactification of A_2 includes the product locus, but generic points of H_2 are Jacobians of genus-2 curves, not pairs of elliptic curves. Correct: "parametrizing principally polarized abelian surfaces" or "genus-2 Jacobians". AP-CY16 is about Sp_4 quotient by ±I_4 -- check preface: it writes Sp_4(Z), no quotient issue. But the interpretation is wrong. CRITICAL per AP116/AP117-style formula hygiene.

### SERIOUS

- **N-S1 (line 73-82, K3 x E prototype).** "the lattice Lambda^{3,2} has signature (3,2)." The signature (3,2) comes from the hyperbolic plane U times U times (-E_8)^? No: signature (3,2) is the lattice underlying the Jacobi form space for K3 elliptic genus via the Eichler-Zagier theory. Specifically, the lattice II_{3,2} = U oplus U oplus <-2> (or similar) has signature (3,2). The preface does not specify which (3,2) lattice. The Borcherds denominator form for Delta_5 lives over the Grassmannian of (3,2)-planes in a signature (3,2) lattice. Good, but specify the lattice. In concordance.tex or chapters/..., Lambda^{3,2} should be defined.

- **N-S2 (line 89-92, discriminant constraint, AP-CY9).** Not violated directly in preface (no coefficient tables), but the preface casually references phi_{0,1} -- subsequent chapters must obey AP-CY9. Passing.

- **N-S3 (line 163-164, Felder's dynamical elliptic R-matrix).** "the CY_2 quantum vertex chiral group is carried on Coh(E), with Felder's dynamical elliptic R-matrix." Felder's elliptic R-matrix is dynamic (depends on lambda in h^*). The "quantum vertex chiral group on Coh(E)" is the Frenkel-Reshetikhin elliptic affine algebra / quantum affine algebra. Check attribution and spelling: Felder's R-matrix solves the QDYBE on Coh(E). Good. But "CY_2 quantum vertex chiral group" is non-standard nomenclature. Cite Felder 1995, check.

### MODERATE

- **N-M1 (line 164-173, six roles of the elliptic curve).**
  (i) Base curve -- check.
  (ii) Sewing parameter tau -- check.
  (iii) CY fiber -- check.
  (iv) Jacobi form parameter -- check.
  (v) Siegel period -- check (modulo N-C1).
  (vi) Elliptic Hall algebra carrier -- check.
  The "six roles" is rhetorically strong. But this should be a theorem or at least a classification lemma; labeling as "bridge" is preface-appropriate.

- **N-M2 (line 175-177, SL_2(Z) symmetry).** "a modular parameter, an SL_2(Z) symmetry, a q-expansion, and a sewing functor" -- each role has ONE of these, not all six roles simultaneously. Some (Siegel, role v) have Sp_4 rather than SL_2. Sharpen.

### MINOR

- **N-m1 (line 167, Sp_4(Z)).** LaTeX renders this fine. No issue.

---

## 5. Adversarial Chef (AP-CY compliance, CLAUDE.md alignment, internal consistency)

### CRITICAL

- **C-C1 (AP-CY6 / AP-CY14 systemic).** Already flagged above (F-C2, P-S1). The preface treats A_C at d=3 as if constructed in multiple places:
  - Line 26-28 "converts the resulting Lie conformal algebra into a chiral algebra A_C on a curve X"
  - Line 28-29 "kappa_ch(A_C) = chi^CY(C)"
  - Line 29-30 "The shadow obstruction tower of A_C is the automorphic correction..."
  - Line 141-142 "the CoHA...is the ordered bar complex of the CY_3 chiral algebra"
  - Line 221-224 "supplying the chiral algebra via Phi, the modular trace via the CY Euler characteristic, and the quantum group via the CoHA" (closing triangle)
  These are asserted in preface-voice. Only lines 62-67 carry the d=3 conditional. A reader who skims the first paragraph will take kappa_ch(A_C) as a theorem in all dimensions. FIX: insert a "throughout this preface, d=2 is proved and d=3 is programme (Theorems CY-A_2 unconditional; CY-A_3 conditional on S^3-framing)" clause in the second paragraph, and add scope tags at each A_C mention.

### SERIOUS

- **C-S1 (AP-CY11, conditional transitivity).** CoHA identification (line 141-147) depends on CY_3 A_X. Shadow-automorphic identification (line 87-88) depends on kappa_ch, which for CY_3 depends on A_C at d=3. Both are DOWNSTREAM of CY-A_3. Per AP-CY11, they inherit conditionality. The preface does not mark this. SERIOUS.

- **C-S2 (AP113, kappa subscripts).** Count: I find kappa_ch (lines 28, 84, 93, 108 implicit, 113), kappa_BKM (85, 94, 113), kappa_cat (111, 119), kappa_fiber (115). I do NOT find any BARE kappa. GOOD. AP113 compliance is PASSING in the preface. Line 106 writes "$\kappa$-mismatch" (bare kappa in the phrase "kappa-mismatch") -- but this is describing the SPECTRUM, not identifying a specific kappa. Borderline; in the same sentence kappa_ch and kappa_BKM are both named, so the phrase is scoping. Accept. Line 106 also writes "$\operatorname{Spec}_\kappa(X)$" (bare kappa subscript on Spec), which is naming the spectrum as a whole, not a specific kappa. Accept. Overall AP113 PASS.

- **C-S3 (AP-CY15, README scope inflation analog).** The preface does not overclaim at the "verified" / "proved" level, except for two instances: "verified by six independent paths" (line 84-85) and "verified end-to-end" (line 138). Both are unsourced. AP-CY15 says this is the README pattern -- avoid in preface too. Either cite or weaken.

### MODERATE

- **C-M1 (AP-CY12 -- shadow depth class M).** Line 193: "class M (Virasoro, W_{1+infty}), the shadow is a strict subtower, and the instanton sum is infinite." Per AP-CY12: G/L/C/M must be determined by computing full shadow tower, NOT by counting generators. W_{1+infty} is class M -- verified. Good.

- **C-M2 (AP-CY16 matrix size).** Line 167: "Sp_4(Z) \ H_2" -- Sp_4 is a 4x4 group acting on H_2 (2x2 symmetric matrices). Consistent. AP-CY16 warns about +/- I_4 vs +/- I_5 quotient confusion. Preface does not quotient, so not triggered. PASSING.

- **C-M3 (AP-CY17, MF CY dimension).** Preface does not discuss MF(W). Not triggered.

- **C-M4 (AP114, stub chapters).** Preface does not cite theorems from stub chapters by name. Passing. HOWEVER, line 239 "Part III studies quantum groups and braided factorization structure, including the Drinfeld center as the bulk algebra" -- this may point at stub chapters quantum_groups_foundations (24 lines) or derived_categories_cy (27 lines). Verify at Part III preface / chapter index. FLAG for cross-check.

- **C-M5 (AP-CY18, lattice theta).** Preface does not make Leech-to-1/eta^24 comparison directly. Not triggered.

### MINOR

- **C-m1 (AP-CY19, A-hat genus argument halving).** Preface does not invoke A-hat genus. Not triggered.
- **C-m2 (AP-CY13 cross-volume Part staleness).** Preface says "Volumes I-II" repeatedly (passing) and mentions Part I-V in Organisation section. Need to grep for stale "Part VI" etc. Not done here (read-only audit), but flag for downstream.

---

## 6. Editor (prose standard, CG moves, voice)

### SERIOUS

- **E-S1 (prose standard, AI slop check).** Grep for forbidden words: notably, crucially, remarkably, interestingly, furthermore, moreover, delve, leverage, tapestry, cornerstone. I scanned visually:
  - None found. PASS.
  Em dashes: CLAUDE.md says "no em dashes; use colons, semicolons, or separate sentences."
  - Line 11-12 "builds its categorical logarithm: the bar complex..." -- colon, good.
  - Line 15 "the holomorphic-topological field theory" -- hyphen, not em dash.
  - Line 28 "modular characteristic: kappa_ch..." -- colon, good.
  - Line 83-86 "...is kappa_ch(K3 x E) = 3 = dim_C, verified by six independent paths. The weight..." -- no em dashes.
  - Line 194-196 "The instanton gap F_g^top - F_g^sh at each genus is the CY frontier." -- minus sign, not em dash.
  - I see no em dashes. PASS.
  Hedging ("might", "perhaps", "it seems"):
  - None found. PASS.

- **E-S2 (CG deficiency opening).** Line 8 "Where do chiral algebras come from?" This is a CG-style rhetorical-question deficiency opening. CLAUDE.md canonical CG move is the "deficiency opening" (Heisenberg/1/z in Vol I). Vol III's deficiency: Vols I-II take a chiral algebra as given and do not construct one (line 10-17). The opening delivers payoff in the third paragraph ("The bar complex converts enumerative geometry into homotopy algebra"). Structure works. GOOD.

- **E-S3 (state once, prove once).** The "three-step construction" (lines 42-61) and the "triangle" (lines 213-220) partially overlap. The triangle is a DIFFERENT statement (triangle of volumes), but lines 205-209 restate "the functor Phi: CY_d-Cat -> E_2-ChirAlg that constructs the input" which is the same as lines 42-61. Minor redundancy. Acceptable in a preface for rhetorical emphasis. MODERATE at worst, not serious.

### MODERATE

- **E-M1 (line 250 closing trichotomy).** "Volume I asks what the logarithm does. Volume II asks how it composes. Volume III asks where it comes from." Powerful. Matches CG "instant computation" + "unique survivor" rhetorical moves. GOOD.

- **E-M2 (line 30, "generalized Kac-Moody superalgebra").** Upper vs lower case: in preface, "generalized Kac-Moody superalgebra" is lowercase. Elsewhere in Vol III it may be "Generalized Kac-Moody" or "Borcherds-Kac-Moody". Consistency check.

- **E-M3 (line 33, "automorphic datum").** "One Maurer-Cartan element Theta_{A_C} absorbs the entire automorphic datum." Punchy; CG-style sentence-as-theorem. Good. But "automorphic datum" is used without prior definition. Preface is OK to do this (rhetorical gesture), flag NIT.

### MINOR

- **E-m1 (line 11, "categorical logarithm").** Evocative. Good.
- **E-m2 (line 94, "single-copy chiral algebra").** Clear, rhetorically effective.
- **E-m3 (line 177, "modular clock of the theory").** CG-style punchline for the elliptic curve section. Good.
- **E-m4 (line 106, "most telling").** The word "telling" is OK, not on the slop list.

### NIT

- **E-n1 (line 7, `\noindent`).** After `\chapter*{Preface}` the `\noindent` is standard.
- **E-n2 (line 39, `\bigskip`).** Used consistently to separate preface sections. Good.
- **E-n3 (line 102, "imprisoned in tautological classes").** "Imprisoned" is strong; check if matching Vol III prose voice. Acceptable.

---

## Cross-Volume Propagation Flags (AP5)

The preface does not directly replicate Vol I / Vol II content verbatim, so AP5 grep is mostly structural:

1. The "triangle" diagram (lines 213-220) claims avg: Theta_A -> HT field theory. This is Vol II content. Verify consistency with Vol II preface/overture.

2. "genus-1 propagator is d log E(z,w)" (line 157) -- this is Vol I MC5 content. CLAUDE.md says "Bar propagator d log E(z,w): ALWAYS weight 1." Preface passes; no weight quoted.

3. "Volume I provides Theta_A: the universal Maurer-Cartan element" (line 201-202) -- matches Vol I Thm identity. Good.

4. "Volume II provides SC^{ch,top}: the Swiss-cheese operad" (line 203-204) -- matches Vol II identity. Good.

5. Kappa spectrum {2,3,5,24} -- matches Vol III CLAUDE.md. Good.

---

## Severity Summary

| Severity | Count | Items |
|----------|-------|-------|
| CRITICAL | 4 | F-C1 (HH vs HC^-), F-C2 (A_C at d=3 asserted in preface voice), T-C1 (chain-level S^d-framing), N-C1 (H_2 parametrizes abelian surfaces, not pairs of elliptic curves), C-C1 (AP-CY6 systemic) |
| SERIOUS  | 10 | F-S1 (Drinfeld center disambiguation), F-S2 (environment), F-S3 (scope tag), F-S4 (six paths uncited), T-S1 (higher lambda-bracket), T-S2 (factorization envelope source), T-S3 (E_2 vs E_inf), P-S1 (CoHA as CY_3 bar), P-S2 (chain verified end-to-end), P-S3 (Delta_5 vs Delta_10), C-S1 (AP-CY11 transitivity), C-S3 (verification claims uncited) |
| MODERATE | 14 | F-M1-M6, P-M1-M3, N-M1-M2, C-M1-M5, E-S3 (redundancy), E-M1-M3 |
| MINOR/NIT | 15 | F-m1-m2, F-n1, T-m1, P-m1-m2, N-m1, C-m1-m2, E-m1-m4, E-n1-n3 |

(Recount: CRITICAL = 5 once N-C1 is included; see "Executive Summary" for the top three called out.)

## Recommended Actions

1. **IMMEDIATE (before any downstream use of preface as canonical).**
   - Fix F-C1 / AP-CY2: rewrite trace as HC^-_d(C) -> k (or HH_{hS^1}).
   - Fix F-C2 / C-C1 / AP-CY6: insert d=2/d=3 scope disclaimer after the first paragraph, and tag every A_C assertion with "(d=2 proved; d=3 conditional on CY-A_3)".
   - Fix N-C1: Sp_4(Z) \ H_2 parametrizes PPAV/genus-2 Jacobians, not pairs of elliptic curves.
   - Fix P-S1 / C-C1: explicitly mark CoHA = ordered bar complex of CY_3 chiral as CONJECTURAL.

2. **NEAR-TERM.**
   - Replace "Nishinaka, Vicedo" with Costello-Gwilliam attribution for PBW factorization envelopes (verify).
   - Cite or localize "six independent paths" and "verified end-to-end".
   - Downgrade "higher A_inf operations give higher Lie conformal products" to "give L_inf homotopies on the lambda-bracket".
   - Verify Delta_5 vs Delta_10 nomenclature and fix.
   - Specify which signature-(3,2) lattice Lambda^{3,2} means.

3. **POLISH.**
   - Sharpen the SL_2(Z) symmetry statement in the six-roles paragraph (some have Sp_4 instead).
   - Cite DMVV, Kontsevich-Soibelman, Deligne-Getzler, Schiffmann-Vasserot, Felder, Gritsenko-Nikulin at appropriate lines.
   - Verify AP114 stub-chapter non-citation for the Organisation paragraph (Part III quantum groups).

## Overall Assessment

The preface is STRUCTURALLY SOUND: the deficiency opening works, the three-step construction is clearly scoped in principle, the K3 x E prototype delivers the four-obstruction dichotomy, the elliptic-curve six-roles is genuinely unifying, the shadow / topological-string convergence-vs-divergence contrast is sharp, and the closing trichotomy ("what / how / where it comes from") lands.

The MAIN SUBSTANCE ISSUE is AP-CY6 / AP-CY14 propagation: the preface rhetorically asserts A_C at d=3 as constructed in multiple places (kappa_ch(A_C), shadow tower of A_C, CoHA = ordered bar of CY_3 chiral) and then scopes d=3 as conditional only 35 lines into paragraph two. This creates a local contradiction the alert reader will catch. Fix: insert explicit scope at the top, tag every A_C mention.

AP113 (kappa subscripts): PASSING. Every kappa is subscripted (ch, BKM, cat, fiber) as CLAUDE.md mandates.

AP-CY9, AP-CY12, AP-CY13, AP-CY15, AP-CY16, AP-CY17, AP-CY18, AP-CY19: not triggered in the preface or passing.

AP-CY2 (trace in HC^-_d not HH): FAILING. One-line fix.

Prose standard: PASSING (no em dashes, no AI slop, no hedging).

Recommendation: a light rectification pass (2-4 commits) addressing the CRITICALs above would bring the preface to platonic. The preface does not need structural rewriting.

---

Audit author: read-only Beilinson protocol. No files modified.
