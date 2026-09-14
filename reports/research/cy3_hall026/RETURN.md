# Scalar Hall images through rank five

The candidate constructs the actual lowest-degree scalar Hall images for the three-loop potential. Independent mathematical acceptance remains pending.

## Frozen question and result

The target is the first scalar image and coherence calculation after the existing orientation calculation for the `(2,2,1)` flag. The ambient potential remains `Tr(A[B,C])`. The source remains the full critical incidence stack, with all commutator equations and stabilizers.

The new module proves these candidate statements.

1. At a scalar atlas point, `H^j(P_n) = H_BM_(2n^2-j)(C_n)` for `2 <= n <= 5`. Here `C_n` is the variety of commuting pairs of matrices. This is an isomorphism of ordinary rational groups.
2. The scalar coefficient vanishes below degree `-2n`. Its group in degree `-2n` has dimension one. The proof uses a Jordan-type stratification, without assuming irreducibility of the entire commuting variety.
3. Complete flags define a quotient-stack morphism `sigma_n: Q[2n] -> P_n`. It extends the specified regular generator and has a nonzero scalar stalk. Positive scaling and the sheaf stalk definition prove nonvanishing.
4. Complete-flag refinement identifies `mu_(d,e)(sigma_d,sigma_e)` with `binomial(d+e,d) sigma_(d+e)`. This computes the whole map in the lowest scalar degree.
5. The scalar images for `(2,1),(2,2),(3,1),(4,1),(2,3)` are `3,6,4,5,10`, respectively. Their kernels in the lowest degree vanish.
6. The actual derived triple maps agree for positive constituent ranks with total rank at most five. The lowest scalar images for `(1,1,1),(2,1,1),(2,2,1)` are `6,12,30`.
7. Rotation of the B matrix gives identity potential monodromy on the entire scalar stalk complex. This rotation preserves centered Milnor balls and returns to the identity after one turn.

The reader module is `research-candidates/cy3_hall026/scalar_coefficient_images.tex`. Its theorem anchors are `sch:prop:scalar`, `sch:thm:generator`, and `sch:thm:images`. The exact file hashes are in `candidate-manifest.json`.

## Proof dependencies and decisive construction

The scalar support calculation is explicit. Homogeneity identifies the positive half-plane complement with the global fibre times a contractible half-plane. Projection from `f_n = 1` to the noncommuting pair `(A,C)` has affine fibres of dimension `n^2-1`. A continuous section is `B = [C,A]^* / Tr([C,A]^*[C,A])`. The closed-open Borel--Moore sequence and Poincare duality then give the stated shift.

For a Jordan type with `r` distinct eigenvalues and centralizer dimension `c`, the matrix stratum has dimension `n^2-c+r`. Adding a commuting matrix gives dimension `n^2+r`. Only the distinct-eigenvalue stratum reaches dimension `n^2+n`, and this stratum is irreducible. This proves the top Borel--Moore group is one-dimensional.

The actual coefficient comparison is constructed through complete flags. Their potential vanishes on the ambient preserving incidence. The complex Thom map and flag integration give a degree `2n(n-1)` morphism. After normalized vanishing cycles and the input shift `[2n]`, this yields a map to `P_n`. The adjunction unit gives `h_n`, and `sigma_n = h_n/n!`.

The regular sign is reconstructed from the real map `(u,v) -> (v,conjugate(u))`, with determinant `-1`. The prescribed conversion `e_n = (-1)^binomial(n,2) u_n` makes each complete-flag sheet positive. Thus `h_n` restricts to `n! e_n`. A scaling-equivariant cohomology section that vanished at the origin would vanish on a neighborhood, then everywhere. Therefore its scalar value is nonzero.

Refinement of a partial flag by complete flags recovers the complete flag incidence. Complex Thom classes multiply, flag integrations compose, and the support product commutes with coefficient maps and proper direct image. These identities hold before taking scalar stalks. They give the divided-power formula without identifying Hall maps with Borel--Moore pushforwards.

The construction is self-contained apart from the standard sheaf operations used explicitly in its proofs. The frozen preceding modules supply the exact orientation and Hall-carrier comparison points. They are read-only inputs, not extra reader includes. No archive statement supplies a theorem.

## Failed and unused routes

The first attempted route was to identify the entire scalar Hall map directly with a pushforward on commuting-pair varieties. Projection of a Milnor incidence removes points with commuting diagonal blocks but noncommuting off-diagonal blocks. The resulting pair-space map need not be proper. No unproved dimensional-reduction compatibility is used.

A regular sheet count alone does not determine the scalar coefficient. The proof adds the global complete-flag morphism and positive-scaling argument before using the count.

The scalar target groups alone do not determine the coefficient image. The proof constructs the comparison morphism separately and proves its refinement identity.

Literature searches located dimensional-reduction papers, but no theorem from those searches is imported. The affine bundle, shift, Jordan dimension and scalar nonvanishing arguments are reconstructed in the module. No novelty claim is made.

The first build capture encountered a Python UTF-8 decoding error from TeX output. The build process itself produced its output. The reproducible builder now preserves raw log bytes, and subsequent builds completed normally. No mathematical source change addressed this capture error.

## Verification

`python3 reports/research/cy3_hall026/check_scalar.py` passes. It uses exact rational arithmetic with the Python standard library. The check covers ten binary splits and ten ordered triples through total rank five. Flag coefficients are checked through permutation enumeration, recursive subset enumeration, and factorial formulas. Explicit real determinants check the sheet signs. Matrix multiplication checks the potential restriction and the exclusion of a noncommuting off-diagonal example.

The same program checks fifty-one Jordan types. Independent matrix commutator ranks agree with the partition formula for each centralizer dimension. Explicit rational sections and affine homotopies satisfy `Tr(B[C,A])=1`. These finite checks verify their stated formulas, not the general sheaf arguments.

`python3 reports/research/cy3_hall026/build.py` reproduces the native seven-page module with the exact frozen shared template. The build has no undefined references or overfull boxes. Two underfull paragraphs remain legible. The expected shell-escape warning reflects the disabled shell escape setting.

All seven pages were rasterized with Poppler and visually inspected. No clipping, overlap, missing text, or manuscript-firewall violation was observed. The standalone PDF was not opened in a reader application. This local PDF is build evidence; the main owner controls the combined reader.

## Exact remaining obligations

The next scalar image target is degree `-4` for `mu_(2,1)` at a scalar rank-three triple. The rank-two coefficient in degree `-2`, tensored with the line coefficient, and the flag's degree-two cohomology both contribute. The present construction fixes neither the full incoming derived family nor that map to `H^-4(P_3)`.

The higher scalar images for `f_4` and `f_5`, including contributions from odd rank-two coefficients, remain uncomputed. The Borel--Moore model of their targets does not identify the Hall operations on those groups. Equivariant derived extension data are retained, but no splitting is claimed.

A holomorphic field-theory comparison still requires its source, target and compatible morphism. Tate refinements, higher homotopies and further ranks remain separate constructions. The candidate does not close any of these obligations.

The required research controls are `gpt-6-astra` and reasoning effort `ultra`. Independently observed execution metadata is unavailable in this runtime. The configuration is therefore unverified. This record does not independently certify the mathematical candidate.

## Custody and handoff

All changes remain under the two assigned paths in the isolated worktree. No staging, commit, push, cleanup or publication occurred. Source, input, build and calculation hashes are recorded in the manifests. The dispatcher owns independent review. The synthesis owner owns inclusion in the combined reader.
