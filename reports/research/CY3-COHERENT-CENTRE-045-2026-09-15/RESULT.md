# Coherent centrality from the diagonal action

This continuation constructs the compatibility across arbitrary strings of
boundary maps left open in 044. It is a complete local proof candidate, with
an integrated reader. It does not establish a general equivalence of centres.

## Construction and coefficient boundary

Let k have characteristic zero, R=k[x_1,...,x_n], and let the boundary objects
be finite free based matrix factorizations of W-c. All their maps are R-linear.
The Hochschild cochains are multilinear over k, with R-linear maps as values.
Tensoring a map evaluates its coefficients at y, so this functor is k-linear,
not R-linear for the left x-action. The explicit difference is
T(x_j f)-x_j T(f)=(y_j-x_j)T(f).

For the strong diagonal contractions from 044, the cochain of a diagonal
operator a has components

U^a_m(sf_1,...,sf_m) = s pi_0 L_0(a) h_0 T(f_1) h_1 ... h_(m-1) T(f_m) i_m.

The chapter defines the suspended Hochschild complex, all insertion signs,
nullary operations and the product over arities. It proves d_H U^a=U^(delta a)
by differentiating each factor and cancelling every internal and endpoint
term. Nonclosed maps remain in this equation. The proof applies to arbitrary
composable object strings. Positive arities vanish on an identity input.
Each fixed formal arity is jointly continuous with order loss at most m.

This supplies a cochain comparison, not an A-infinity algebra morphism into
the Hochschild cup algebra and not a quasi-isomorphism. Those are separate
remaining constructions. It uses neither an isolated critical point nor a
regular-gradient assumption.

## Deciding examples

For W=x^3 and D=[[0,x],[x^2,0]], the odd matrices H=E21 and
e=[[0,1],[-x,0]] satisfy delta H=xI, delta e=0 and He+eH=I.
The full arbitrary-primitive argument shows that the scalar map into
HH_k^even of the whole boundary category has kernel exactly (x^2).
In particular, x survives coherently although it acts trivially on the
cohomology of every individual boundary endomorphism algebra.

The upper bound is constructive. The diagonal odd matrix
a=(E12+(2x+y)E21)/3 has delta a=x^2 I. Its Hochschild primitive on the
boundary category has nullary component D'_E/3, unary component -f'/3,
and no higher components. Entrywise differentiation verifies this primitive
without the diagonal construction. The derivative is not R-linear, making
the coefficient distinction necessary.

For W=x^3+xu^2 and the mixed boundary from 044, the even diagonal operator
extracting theta2 theta1 has U_2(s(uI),s(xI))=sI. The chapter derives this
nonzero binary component directly from the two-stage contraction. The bulk
operator is not assumed closed. For every W, differentiating D_Delta gives
explicit primitives for the gradient scalar relations.

## Checks and integration

check_coherence.py passed 443 exact assertions. It compares the full
Hochschild commutator with the diagonal differential, including nonclosed
matrix units, two distinct boundary objects, and arities zero through four.
It separately checks the cubic derivative primitive, the arbitrary primitive
obstruction, the nonzero binary example and identity-input normalization.
Finite checks supplement the complete written proof. No independent
mathematical acceptance is claimed. Runtime model/effort metadata is unavailable.

The native source commit is f5b80a6df659953378522ab742b980975b4d0e25.
The same new source is synthesis045 Chapter 15, PDF pages 230-235.
The native diagnostic build has 537 pages. Its addition and transitions were
inspected, but it retains unrelated defects and is not delivered as healed.
The combined reader has 868 pages. All six added pages, both transitions,
and selected changed contents pages were inspected.

The integration also repairs an inherited duplicate sec:da-operators label.
The previous 044 log contained that warning although its recorded log findings
omitted it. Only the diagonal-action anchor was renamed. Frozen044 remains
preserved and every predecessor proof body is byte-identical.

Keller's functor-category account and Dyckerhoff's Hochschild calculation
were checked at the locators in primary-source-check.json. The latter has
regular-local and isolated-singularity hypotheses. Neither establishes a
global polynomial comparison here by citation. No novelty claim is made.

## Remaining mathematical obligations

Construct the comparison on products of bulk operators and its higher
compatibilities. Determine its full kernel and cokernel, including the
appropriate critical-value support and any required completion. Construct
the cyclic and chiral operations and prove their compatibility with the
specified maps. The coherent centrality construction itself is now available
and should not be restarted.

All 26 prior workstreams, additive archive obligations, native repairs and
concurrent-source reconciliation remain. No whole-programme completion
percentage is inferred from this local result. Historical percentage ranges
have not been recalibrated. Continue on the main thread without subagents.
