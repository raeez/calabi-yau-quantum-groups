# Evaluation of the first higher scalar image

The new mathematical source is degree_four_image.tex. It extends the preserved proper-Milnor-map proposition without editing either frozen predecessor. This is a full candidate proof, pending independent mathematical review.

## Result and exact carrier

At the ordinary scalar atlas point for rank three, the actual degree−4 coefficient map mu_(2,1) has a two-dimensional source and a one-dimensional target. A canonical geometric basis of the source consists of a=H(v2 tensor v1), where H is the outer quotient-line Chern class, and b, the derived lift produced by decorating the internal complete flag with its quotient-line Chern class. Its matrix is [1,0] relative to the target generator w3=kappa3/2. Thus the image is the entire degree−4 target and the kernel is Qb.

The target normalization is geometric: kappa3/2 specializes to the rank-two class w2 at a scalar plane plus a separated line. The class w2 is nu2(h), with h the positive hyperplane class on the complete rank-two flag. Its nonvanishing is proved, not assigned as a definition. All maps retain the full critical incidence, normalized vanishing cycles, complex orientations and quotient-stack descent. No projected pair-incidence pushforward replaces the proper Milnor map.

## Decisive proofs

The rank-two calculation uses the determinant resolution Hom(C3,U) over P2. The original flag P1 embeds as a conic. Its positive class pushes to z². The exceptional rank-one locus has zero class in degree12 Borel–Moore homology of the resolution because p_*(q³)=c1(U)²−c2(U)=0. Its degree11 Borel–Moore homology vanishes, by the resolution over the complete flag variety. Closed-open exact sequences show the resolution map is an isomorphism in degree12. The determinant support map then gives a nonzero H5(SL3) class. This proves nu2(h)≠0.

For the target, remove pairs whose first matrix has only one eigenvalue; their complex dimension is at most10. The distinct-eigenvalue open stratum O has H1(O)=Q and H2(O)=0. The proof computes these groups from GL3/T times ordered configurations and the explicit S3 action. The complement has two top-dimensional components: a repeated Jordan eigenvalue and a semisimple repeated eigenspace. The discriminant boundary has coefficients(1,2), verified in local cyclic charts. Therefore BM22(C3)=Q²/Q(1,2)=Q.

At diag(0,0,1), the complete-flag fibre has three P1 components. The isolated line can occupy positions1,2,3. The line Chern restrictions are (0,−h,h), (−h,0,h), and (−h,h,0). The actual coefficient map on each component is nu2 with positive cross-pair factor. Hence kappa1,kappa2,kappa3 specialize to −2w2,0,2w2. Positive-scaling equivariance of their actual cohomology sections, together with the scalar target dimension, transfers nonvanishing and the zero relation to the origin. Proper refinement with the Chern insertions gives mu(a)=kappa3/2 and mu(b)=kappa2.

## Computation and rendering

check_degree_four_image.py uses only exact integer and rational arithmetic. Three paths check the two discriminants: the cubic coefficient formula, a Sylvester resultant determinant, and squared root differences. They give 4t(4−t)² and 4t²(4−t²)², with orders1 and2. Independent matrix actions compute the S3 fixed dimensions. Projective-bundle reduction verifies the zero exceptional class. The Chern restriction table gives(−2,0,2). The script distinguishes these finite checks from the geometric proofs.

The exact native consumer includes the corrected scalar module, the preserved degree−4 source/map proposition, and the new image evaluation. It builds in three passes to14 pages. New pages9–14 were visually inspected, including the final corrected pages12–13. The earlier source and page layout remain unchanged. There are no overfull boxes, undefined references or unknown bibliography keys. No standalone reader was opened.

## Preserved failures and scope

The nonproper pair-incidence projection is still a refuted method. Its explicit t-family remains in degree_minus_four.tex and in the earlier frozen calculation record. The successful evaluation uses proper determinant and Milnor incidence maps instead.

The initial conjecture that numerical flag traces might determine this image was not used. The rank-two decoration requires an additional support calculation, and the rank-three target requires a separate Jordan-stratum calculation. Neither follows from the lowest-degree coefficient numbers.

The earlier preserved report correctly recorded an uncomputed degree−4 image at its freeze. The present candidate supplies that missing evaluation. Independent review must check these new exact bytes before that obligation can be accepted as closed.

Remaining mathematical work includes other scalar degrees of mu_(2,1), the higher scalar images for ranks four and five, and equivariant extension data. The separate coproduct construction requires its own frozen evidence and review. No all-rank theorem, Hodge/Tate assertion or physical carrier comparison is inferred.
