Completed the explicit CY3 normalization comparison as a new, isolated candidate. Root acceptance remains pending.

The worktree is `/Users/raeez/mathematics/worktrees/frontier-resume-cy3-normalization-020-20260914`, branch `intake/resume-cy3-normalization-020-20260914`, based on principal `develop` HEAD `aaf325a7b7c4d9a8da252ce1a8db5448e5300aa9`. Only `research-candidates/cy3-native-normalization020/` and this evidence directory were written. Nothing was staged, committed, pushed, or published.

The predecessor is the complete native221002 reader with source-freeze SHA-256 `02bd496c44c7cffe61c565ffd96cec06829656bce7bf11f6d5c452c5f8da2a2a`. Its 404 frozen candidate-owned records were checked before construction and again before freezing. The original candidate and report remain untouched. The copied baseline contains exactly the original 28 source files. The construction changes four files and retains the other 24 exactly.

The mathematical comparison is internal to the reader. In `research-candidates/critical-hall-two-nonzero-blocks/two_nonzero_blocks.tex:594`, the one-pair quadratic is

\[
q=b_{ij}c_{ji}-b_{ji}c_{ij}.
\]

The B-positive disk has coordinates `(b_ij,b_ji,c_ij,c_ji)=(u,v,−conjugate v,conjugate u)`. Its lower-normal projection is `(u,v)↦(v,conjugate u)` and has real determinant −1. The upper-(B,C)-positive disk has coordinates `(p,−conjugate t,t,conjugate p)`. Its projection has determinant +1. Changing between these disk parameterizations conjugates one complex coordinate and reverses orientation.

Lines 617–640 compare orientations with the fixed support and cone construction. The positive relative Thom class has cone representative `(0,−α)` for the positive angular class α, because `(dβ,0)−d(β,0)=(0,−α)`. Product disks show that the actual support morphism preserves products of relative Thom classes. All relevant degrees are even. No support map, Thom map, potential, shift, or coefficient morphism is redefined.

Proposition 133.5, source line 671, proves the binary coefficient comparison. The lower A normal cancels the flag tangent through a complex linear isomorphism. Each of the `de` remaining cross pairs contributes −1 in the B convention. If `u_n` denotes the B generator and `e_n` the upper generator, then

\[
e_n=\epsilon_nu_n,\qquad \epsilon_n=(-1)^{\binom n2},
\qquad \epsilon_d\epsilon_e(-1)^{de}/\epsilon_{d+e}=1.
\]

Thus each defined binary map has coefficient `(-1)^(de)` per sheet in u coordinates and +1 in e coordinates. The source explicitly identifies these as two coordinates of the same derived map. This proposition concerns regular coefficients of the constructed maps, not all-rank derived associativity.

Lines 704–717 give the two flag calculations. For `(2,1,1)`, the cross-pair count is five. The left signs are `(+1)(−1)` and the right signs are `(−1)(+1)`. Both maps are minus the twelve-sheet sum in u coordinates and the positive twelve-sheet sum in e coordinates. The incoming vectors differ by `ε_2 ε_1²=−1`. For `(2,2,1)`, the count is eight and the trace is +30 in both conventions. The input and output changes are `ε_2² ε_1=ε_5=1`.

The positive trace passage at source lines 733–755 explicitly uses e generators and gives its u-coordinate value. The two native consumers at `platonic/chapters/hall_coefficient_maps.tex:114` and `platonic/chapters/Volume_IV_Calabi_Yau_Quantum_Groups.tex:255` state the same comparison. The shared consumer is also read by the focused driver. The native consumer additionally identifies the existing separated rank-two coordinates `(b12,c12)` in Equation 89.1 with this upper polarization. That existing two-sheet trace uses e2.

In `research-candidates/cy3-flag221019/flag221.tex:356`, the cyclic coefficient lemma names the B trivialization u and its rankwise scalar change e. Lines 395–423 give the extension across nondiagonalizable cyclic matrices. The B quotient by the centralizer is a complex bundle, paired with the C quotient. Contractible complement and metric choices preserve its oriented relative Thom generator. The construction therefore respects frame changes on the complete conjugation action diagram. Multiplication by ε_n respects potential monodromy and the central-restriction-to-nearby-cycles map after family pullback.

Lines 426–443 compute the eight-pair sign of the thirty-sheet trace. Lines 521–526 identify the input and output trivializations over the whole companion family, including its central point. Hence the existing actual sheaf map `Rπ_*Q_Y[10]→Q_D[10]`, its central value thirty, and the `j_!L` versus `Rj_*L` distinction use the same trivializations in both conventions. Ambient vanishing cycles remain pulled back, not recomputed from the identically zero restricted potential.

Preservation is exact for all derived-map constructions and both associativity proof bodies. The entire two-block prefix before its original regular section is unchanged. The entire flag prefix before its original cyclic section is unchanged. All proof bodies in both native consumer files are unchanged. The complete flag-cover and coefficient-gluing proof bodies are unchanged. The cyclic lemma gains only its explicit generator convention and support/cone reference. `normalization-calculations.json` records the preserved ranges and hashes.

Exact rational and integer calculations check the three real determinants by elimination and Leibniz expansion. They check every regular binary sign through total rank five. For each selected flag, direct enumeration, left factorization, and right factorization give the same count and sign. These finite checks support the internal proof within their stated ranges. They do not prove general derived coherence. The external support convention was checked in Massey, arXiv:math/9908101v1, pages 1–4; exact provenance and scope are in `primary-source-and-dispositions.md` and the downloaded primary PDF is in `inputs/`.

The unchanged baseline, full native candidate, and focused reader compile with the pinned shared template and no shell escape. Their page counts are 541, 541, and 22. Every required final pass converges. No fatal error, undefined citation, undefined reference, or duplicate-label diagnostic occurs. The native warnings are the same classes as the unchanged baseline: disabled shell escape, two existing amsrefs notices, one existing underfull box, and one existing 1.77861 pt overfull box outside this repair. The focused warning is disabled shell escape only.

All 541 native and 22 focused pages were rendered. Visual inspection covers native PDF pages 12–17, 107–109, 217–219, 359–363, and 366–371: 23 pages, including all 13 changed text pages and their transitions. All 22 focused pages and 14 baseline comparison pages were inspected. The final native PDF was independently rasterized to stdout on all 541 pages at 80 dpi and all 23 selected pages at 120 dpi; every raster matches the retained inspection image. No clipping, overlap, missing formula, or manuscript-firewall violation was found. The final consumer page 218 was reinspected after the separated-rank-two identification.

The new normalization proposition lands on native PDF361 / focused PDF13. The cyclic lemma lands on native PDF367 / focused PDF19. The gluing proposition now lands correctly on native PDF369 / focused PDF21. Its predecessor destination offset no longer manifests after the new mathematical paragraph. No template file was changed. Other whole-book navigation obligations were not re-certified.

The raw native recorder closure contains 352 inputs, including three generated inputs. The complete build closure adds the two bibliography databases and `amsrn.bst`, giving 355. The focused closure contains 326 inputs, including its generated auxiliary file. The manifests distinguish raw recorder inputs, generated inputs, and BibTeX inputs. Every dependency is either candidate source, the exact pinned shared template, or the TeX distribution/format. No reader input comes from a shared manuscript checkout. Cross-directory and exact-command reproduction results are recorded separately, including pdfTeX's output-path-dependent trailer ID.

`normalization-integration.patch` contains the four semantic source deltas against the preserved baseline. `git apply --check` succeeds without applying it. An independent in-memory hunk replay reconstructs every changed source byte. The reproducible archive contains all 28 source files, and every archive entry equals its source. `source-freeze.json` binds the complete source, patch, archive, input manifest, calculations, PDFs, and render evidence. `artifact-manifest.json` binds every owned evidence file and excludes itself.

Final native PDF: `build-candidate/cy3_candidate.pdf`, SHA-256 `a52dd1f2f85b2d30d5a5f3f97707a50254068d0ea08d09fb2fab2b24783892eb`.

Final focused PDF: `build-focused/cy3_focused.pdf`, SHA-256 `c607b562e75b5176175c97e1628f6d3480db8d249d112db8e3c51c08485889a3`.

The requested controls are independently observed in this task's own public turn metadata: `gpt-6-astra` with effort `ultra`. `runtime-controls.json` records the session path and line 8. No private reasoning was extracted. No delegation occurred.

The complete predecessor review and the independent normalization full return were read. The latter is preserved in `inputs/cy3_normalization_independent020-final-01.md`, SHA-256 `62def962452484601ecd968aebe30e725cdee3ec49a135251233e6414e44befd`. Its proposal-independent derivation agrees with the fixed cone sign, projection, lower-A/flag cancellation, flag parities, and rankwise generator comparison. No source change was required. This is predecessor evidence; fresh exact-byte mathematical acceptance of this candidate remains with the root. This constructor does not certify its own candidate.

No new mathematical obstruction remains in the constructed normalization comparison. Residual scope is unchanged: scalar f3/f4/f5 targets and images, all-rank coherence, Tate/Hodge refinements, coproducts, compact-CY comparison, whole-book acceptance, principal integration, and central accepted-PDF custody. The principal's manuscripts and accepted PDFs were not modified.
