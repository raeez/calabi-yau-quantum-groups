# Seven Extension Resolution for Chambered BPS Positive Geometry

Date: 2026-04-24.

## Principle

The object is the finite-first oriented motivic Hall cosheaf

```tex
\mathcal P^{BPS}_{\sigma,S,o,T_eq}(X)
 =
\varprojlim_{N,R}
\mathcal P^{BPS}_{\sigma,S,o,T_eq,<=N,<=R}(X).
```

Every extension problem is forced to become one of four strict forms:

```text
certificate,
radical quotient,
comparison cocycle,
vanishing obstruction complex.
```

This is stronger than an informal theorem claim.  It gives an iff
criterion, a finite quotient in which the criterion is checkable, and a
named source object whose functorial outputs are the decategorified
positive geometry, theta basis, automorphic denominator, hCS comparison,
and numerical BPS support.

## Lane 1: Quintic ExCert

### Attack

The false proof is:

```tex
PTVV shifted symplectic moduli + HKR dimensions
  => Bridgeland chamber on X_5.
```

The implication is false.  PTVV gives the `(-1)`-shifted symplectic
derived moduli stack of objects in a CY3 category.  HKR computes the
Hochschild surface of the category.  Neither constructs a Bridgeland
stability condition with support property, nor finite HN control in a
strict sector.

### Heal

The exact theorem is the certificate theorem:

```tex
ExCert(X_5;\sigma,Q,S,o,T_eq,Mot)
```

is equivalent to the simultaneous construction of:

```text
1. a Bridgeland stability condition sigma on Perf(X_5),
2. a support form Q for sigma,
3. finite HN sector control in S,
4. orientation output o for the PTVV critical atlas,
5. a motivic coefficient target Mot compatible with vanishing cycles,
6. an equivariant specialization T_eq preserving the preceding data.
```

With this certificate supplied, Theorem
`thm:bps-positive-finite-first-existence` constructs
`\mathcal P^{BPS}_{\sigma,S,o,T_eq}(X_5)`.  Without it, the quintic is
not a foundational gate; it is a stronger named compact example.

### Compute witness

The oracle function

```python
quintic_excert_surface_certificate()
```

checks that the PTVV and HKR inputs are present and that the open
Bridgeland/support/HN routes remain explicit certificate slots.  It
prevents a theorem from silently using data that has not been supplied.

## Lane 2: Schoen / Banana Local-to-Compact Gluing

### Attack

The false proof is:

```tex
local banana BPS data
  => compact Schoen chamber.
```

Local curve data do not automatically glue to compact Hall
correspondences.  Compact support, HN sector order, orientation, and
wall-crossing transport must survive on overlaps and on the global
compact derived moduli stack.

### Heal

The exact theorem is:

```tex
ExCert(X_Sch;\sigma,Q,S,o,T_eq,Mot)
```

if and only if the local banana Hall charts glue by compact-support
HN-compatible correspondences.  The required gluing data are:

```text
1. local oriented critical Hall charts,
2. overlap equivalences preserving the orientation gerbe,
3. compact-support Beck--Chevalley for Hall pull-push,
4. HN order compatibility for sector descent,
5. agreement of motivic integration on overlaps,
6. finite quotient compatibility for all (N,R).
```

### Compute witness

The oracle function

```python
schoen_banana_gluing_certificate()
```

checks the local banana shadow data:

```tex
S_4^{inst}=-44,
\qquad
r_max=-1,
```

and records the compact Hall gluing as the exact remaining
correspondence slot.  The negative `r_max` witness blocks any collapse
to the toric terminal fan case.

## Lane 3: Raw K3 x E Hall-BKM Bridge

### Attack

The false proof is:

```tex
AutBorch(phi_{0,1}) = Delta_5
  => raw Hall algebra = U(g_{Delta_5}^+).
```

An automorphic denominator sees only the denominator quotient.  It does
not prove that every raw Hall class is visible to the automorphic
pairing, orientation character, and denominator supertrace.

### Heal

The exact theorem is the quotient theorem:

```tex
CoHA^{Mot,o}_{crit}(K3 x E)^hat_S / Rad_Aut
  ~= Uhat(g_{Delta_5}^+).
```

The unquotiented theorem is strictly stronger and has the exact iff
form:

```tex
CoHA^{Mot,o}_{crit}(K3 x E)^hat_S
  ~= Uhat(g_{Delta_5}^+)
iff
Rad_{Aut,<=N,<=R}=0 for every finite quotient (N,R).
```

### Igusa input

The paper `~/igusa-cusp-form` fixes the normalization:

```tex
phi_{0,1} = sum f(n,l) q^n r^l,
f(0,0)/2 = 5,
AutBorch^{den}(phi_{0,1})
 = (Delta_5, nu_{Delta_5}, 64^{-1} Delta_5(2Z)).
```

The scalar protected object is square-normalized, while the denominator
half is the BKM object.  This separation is exactly what forces the
radical quotient statement.

### Compute witness

The oracle function

```python
k3e_unquotiented_radical_certificate()
```

delegates to the Igusa normalization certificate and records the full
Hall--Borcherds radical vector as the raw-theorem obstruction.  Finite
Gram nondegeneracy is only the pairing coordinate; the raw upgrade also
requires orientation-character, protected-integration, primitive-bracket,
Serre/imaginary-root, Hopf-pairing, and completion-separatedness
coordinates.

## Lane 4: Theta Enhancement

### Attack

The false proof is:

```tex
Hall wall crossing exists
  => GHKK / GMN / broken-line theta basis exists and agrees.
```

Hall wall-crossing constructs KS transport.  It does not identify that
transport with a broken-line, cluster, or GMN count without a comparison
map and a comparison cocycle.

### Heal

The intrinsic finite Hall theta package is:

```tex
theta_p^{lambda,c}
 =
Phi^{KS}_{b->c}(x_p).
```

It is path-independent exactly when every retained codimension-two KS
joint has identity holonomy.  Multiplication in the base chamber is

```tex
theta_p theta_q
 =
L^{<p,q>/2} epsilon_o(p,q) theta_{p+q},
```

with zero value when `p+q` leaves the finite quotient.  GHKK, GMN, and
broken-line packages are comparison enhancements:

```tex
Theta_Hall = Theta_cmp
iff
comparison cocycle = 0 in every finite quotient.
```

### Compute witness

The oracle function

```python
theta_comparison_certificate(bound)
```

checks support, Hall associativity, sector descent, and the finite
`A_2` KS holonomy witness.  It records comparison with GHKK/GMN/broken
lines as a stricter vanishing problem rather than as an assumption.

## Lane 5: hCS-to-Hall Localization in Named Geometries

### Attack

The false proof is:

```tex
local hCS stationary phase maps exist
  => compact hCS-to-Hall morphism exists.
```

Local stationary phase does not imply global Ran factorization descent,
orientation descent, Thom--Sebastiani compatibility, compact support
base change, or continuity in the completed Hall topology.

### Heal

The exact theorem is:

```tex
Theta^o_{hCS->Hall} exists
iff
o_MC=o_or^rel=o_gr=o_TS=o_fact=o_cs=o_wedge=0.
```

The seven classes are:

```text
o_MC     Maurer--Cartan defect,
o_or^rel relative orientation compatibility class,
o_gr     grading / Tate mismatch,
o_TS     Thom--Sebastiani associator defect,
o_fact   Ran disjoint-union factorization defect,
o_cs     compact-support Beck--Chevalley defect,
o_wedge  completion incompatibility.
```

For a named compact CY3, the problem is no longer vague localization.
It is the computation of the primitive source/target vector together
with these seven descent classes in that geometry.

### Compute witness

The oracle function

```python
hcs_named_obstruction_certificate()
```

records all fourteen obstruction names and checks that the ledger is
complete.  It is exact as a total obstruction list and conditional as a
named-geometry vanishing theorem until the source/target and descent
coordinates are computed.

## Lane 6: Executable Finite Oracle

### Attack

The false proof is:

```tex
the formal theory is coherent
  => finite computations automatically match it.
```

A positive geometry without finite quotient tests can hide sign errors,
orientation defects, false BKM normalizations, and toric collapse
misidentifications.

### Heal

The executable oracle implements exact finite certificates:

```text
support property,
orientation Cech and quadratic refinement,
Hall associativity,
HN sector descent,
KS A_2 holonomy,
conifold quantum pentagon,
C^3 toric collapse,
conifold toric collapse,
Igusa normalization,
quintic certificate surface,
Schoen banana gluing surface,
K3 x E radical surface,
theta comparison surface,
hCS fourteen-coordinate obstruction surface,
remaining point-coordinate gates,
aggregate seven-lane certificate.
derived solution stack certificate.
```

The aggregate function is:

```python
seven_extension_resolution_certificate(bound)
```

It has empty discrepancies exactly when all finite ledgers are internally
consistent.  Its `exact=False` flag is not a weakening; it is the typed
record that named-example upgrades still require their stated
certificates, radical vanishing, or comparison vanishing.

The stronger object is:

```python
derived_solution_stack_certificate(bound)
```

It represents every residual problem as a derived zero-fiber schema:

```tex
Sol^{BPS}_{<=N,<=R}
 =
D_{<=N,<=R}
 x^h_{V_Ex + V_glue + V_rad + V_theta + V_hCS}
 {0}.
```

The finite equations are:

```text
quintic         o_Ex = 0,
Schoen          o_glue = 0,
raw K3 x E      o_rad = 0,
theta           o_theta_pkg = 0,
hCS             Omega_hCS,Hall = 0.
```

The BMS compact non-toric class gives an actual point.  The other named
examples are no longer informal gaps; they are closed substacks of the
same derived solution object.  They become actual points only when their
obstruction coordinates are computed from the named finite geometry and
vanish in the finite-to-pro tower.

## Lane 7: Manuscript Inscription

### Attack

The false proof is:

```tex
notes describe the object
  => the manuscript contains the theorem.
```

Notes do not become mathematics until the construction, definitions,
theorems, and proofs are inscribed in the manuscript with references and
labels.

### Heal

The manuscript inscription is:

```text
chapters/theory/bps_positive_geometry_closure.tex
```

inserted into Part VII by:

```tex
\input{chapters/theory/bps_positive_geometry_closure}
```

The chapter proves:

```text
1. finite-first existence of the oriented motivic Hall cosheaf,
2. toric effective geometry as terminal degeneration,
3. compact non-toric existence in the Bayer--Macri--Stellari class,
4. quintic and Schoen named-example certificates,
5. Igusa automorphic boundary as radical quotient,
6. seven-class hCS obstruction theorem,
7. intrinsic Hall theta package and comparison cocycle criterion,
8. executable seven-lane certificate theorem,
9. residual derived solution stack theorem,
10. total seven-lane resolution theorem.
```

## Master Resolution

The foundational gap is closed at the correct level:

```tex
data-realized compact CY3 chamber
  => finite-first oriented motivic Hall cosheaf
  => BPS positive geometry.
```

The toric effective positive geometry is the most degenerate quotient.
Compact non-toric examples exist in the Bayer--Macri--Stellari class.
The quintic and Schoen problems are stricter named-example certificates.
The raw `K3 x E` theorem is stricter than the Igusa quotient and is
equivalent to finite radical vanishing.  Theta comparison is stricter
than Hall theta and is equivalent to comparison-cocycle vanishing.  hCS
localization is stricter than local stationary phase and is equivalent
to the fourteen-coordinate construction/descent vector vanishing.  The
oracle makes all finite claims executable.

Thus nothing remains as an untyped foundational gap.  What remains are
stronger named closed substacks of the derived solution object:

```text
quintic ExCert,
Schoen compact Hall gluing,
raw K3 x E radical-zero,
GHKK/GMN/broken-line comparison-zero,
named CY3 hCS fourteen-coordinate vanishing.
```
