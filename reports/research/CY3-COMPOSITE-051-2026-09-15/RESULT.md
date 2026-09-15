# Composite operations and coherent current norms

## Concrete result

The 923-page combined working reader contains a new chapter, “Composite inputs
and finite cubic models,” on PDF pages 229–234. It also contains a creation-power
domain and norm proof on PDF pages 901–902. All 529 predecessor proof body is
preserved. Six new explicit proof environments are added.

The main pure-source commit is `dbf7a6f807b625cac99002cc64856e3fc80b4dc9`.
The native CY source commit is `76cef4687b9e6ed2562454906a828197290e92f6`.
The new composite chapter is byte-identical in both candidates, with SHA-256
`401eb6518c500f0752d7ebeeeab10cecdf9e91f4563e3d1d6ae6f7d8a58b987f`.
These are local proof candidates. Fresh independent review remains outstanding.
No whole-book acceptance or novelty claim is made.

## What the new construction establishes

The input is the specified ordered diagonal of a polynomial or formal potential
over any commutative rational algebra. Retained coefficients, parity signs, and
the actual normal-coordinate contraction remain fixed.

1. The general composite value is
   `b3(chi,chi,a1)=-W_(3,0)W_(0,2)e`.
   Its complete reduction is written in `eq:co-first-composite`.
   It extends the primitive-word formulas without deleting exterior products.
2. `prop:co-symbol-product` expresses Clifford multiplication through a finite
   exponential of exterior differential operators. Its associativity follows
   from three commuting tensor operators. Both ordered and antisymmetrized
   representatives receive explicit coefficient matrices.
3. `thm:co-all-inputs` gives finite scalar formulas for every composite input.
   Every tree vertex and edge is a specified scalar operation. No unknown
   lower-arity map or matrix inversion remains in this expression.
   The higher components lie in a specific left ideal. Consequently only the
   last-letter root split contributes to a transferred operation.
4. `thm:co-degree` counts contractions. For input exterior degree N, arity n,
   and output exterior degree h, an operation coefficient has potential degree
   `q=(N-n+2-h)/2`. For a potential of degree at most m, its coordinate degree
   is at most `q(m-2)-(n-2)`. The comparison components have the corresponding
   formula with their surviving exterior normal symbols included.
5. Every binary cubic, with arbitrary lower terms, has `b_n=0` for n>=7 and
   `F_n=0` for n>=6 in these transferred models. The bounds apply to all inputs.
   They follow from the general degree proof, not from finite enumeration.
6. For `W=a*x1^3+b*x1^2*x2+c*x1*x2^2+d*x2^3+lower terms`, the highest value is
   `b6(chi^6)=a*c*(b*d-c^2)e`. The fifth comparison component is
   `-a*c*(b*d-c^2) beta1 beta2` in suspended notation. The written proof gives
   the intermediate components and their scalar reductions.
7. That coefficient is not coordinate-invariant. The polynomial `x1^3+x2^3`
   has coefficient zero. Substitution `(x1,x2)=(s+t,s-t)` gives `2s^3+6s*t^2`
   and coefficient -432. A sixth multiplication alone is therefore not a
   formality invariant. Higher comparison components matter.
8. `prop:ao-creation-norms` proves domains of every creation power on the
   arithmetic coherent vector. Its exact norm is
   `sum_(j=0)^q binom(q,j)^2*j!*n^j*p^(-n*beta*(q-j))`.
   The proof derives the Poisson marginal from the annihilation equation,
   proves closed weighted-shift domains, and evaluates the factorial moments.

The scalar tree formula is a finite explicit expression. A further resummation
that avoids enumerating contractions remains a separate combinatorial question.
Coherent higher coordinate transformations and transport of a specified cyclic
structure remain substantive mathematical obligations.

## Concurrent-source reconciliation

All 28 research-source hunks from r3 to r5 were inspected against the live
combined source. Their dispositions and exact source anchors are in
`r5-hunk-reconciliation.json`. Most corrections were already supplied in 042–049.
The missing general composite value and exact creation norm are incorporated
and extended in 051. The unchanged r3 material retains its earlier review scope.

The new candidate preserves the current conormal quadratic form, the distinct
free and tensor-composed central ideals, and the stronger operator-domain and
quantitative time-average proofs. It does not replace the combined reader with
the older-base r5 PDF. Future source changes require their own reconciliation.

## Exact checks and their mathematical limits

`derive_binary_cubic.py` uses the universal rational polynomial coefficient ring,
including all cubic, quadratic, and linear coefficients and retained variables.
It checks 256 exterior-exponential products against a separate word reducer,
128 basis contraction cases, and228 coefficient-degree assertions.
It computes every nonunit input word through arity seven.

It then enumerates every potentially nonzero composition of the finite operation
and comparison tables, including unit inputs. All 3,609 operation compositions,
grouped into 934 words, cancel. The full morphism equation vanishes on all 808
potentially contributing words. The general degree proof excludes omitted
higher operations. This is stronger than checking only the initial 3,279 words.

`check_matrix_and_current_norms.py` independently uses actual 4-by-4 exterior
matrices and basis inversion. It derives the repeated-composite recurrence and
checks 84 matrix entries. It also checks 26 exact norm-polynomial identities.
The coordinate-change calculation is checked separately.
The first matrix attempt used structural equality between expanded and factored
polynomials. That mechanical error was corrected by expanding their difference.
Its failed log remains preserved.

These calculations check the stated algebraic models. They do not establish
geometric-centre, factorization, spatial quantum, or cyclic equivalences.
They do not replace fresh independent review of the exact manuscript.

## Reader artifacts and preservation

The combined PDF SHA-256 is
`5e0e23ab97f6c10c2cede283c7cda59b0cd0b0005456e4c9f9832c362a1d1072`.
The 117-file pure source archive has SHA-256
`dfa9821118f54849f6b086371dafd4afb8dd7f01c56cca10a7876b5bf75e1016`.
After extraction, `sh build.sh build-final` in `source/` reproduces the PDF
byte for byte. `SOURCE-FREEZE.json` records both source and output hashes.

The main final build has no errors, undefined references, duplicate labels,
or overfull boxes. Every changed page and transition in `render-pages.json`
was inspected. The initial 7.5186pt display overflow was repaired by splitting
the scalar definitions over two lines. Its source and render remain preserved.

The native CY diagnostic has 573 pages. Its SHA-256 is
`bf6b0dd83f303b15a57fecc4d543dd55f99607e0ba062146deff31583f5f2e59`.
Its source remains isolated in `frontier-cy3-boundary-043-20260915`.
Only the new composite chapter, the preceding chapter's closing consequence,
and their entrypoint change. It retains an inherited 1.77861pt overfull line
and other inherited manuscript-production language outside the changed region.
It is not a clean whole-book release.

Creation-norm propagation into the native arithmetic manuscripts remains a
separate candidate. The new arithmetic result is integrated in the combined
synthesis. All 26 saved workstreams and every prior intake remain in scope.

## Continuation

The next constructive intake is quantum collision and chiral descent. Start
from its actual moment-map complexes, central curvature, and overlap maps.
Keep the oscillator quotient's central character distinct from the full
enveloping algebra. The fusion/root-stack stream remains independently open.

The 051 composite model and 050 singular-current model both need fresh reviews.
The full chiral-centre comparison must preserve spatial modes and singular
operations. The higher-cup and zero-mode comparisons do not supply it.
No evidence-weighted whole-programme percentage can be inferred from this
bounded phase's pages, source hunks, or calculation counts.
