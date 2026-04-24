# Agent 04: theta comparison adversarial lane

## claim attacked

The attacked claim is the theta-comparison part of the current platonic
closure:

```tex
Broken-line, GHKK, and GMN theta packages coincide with the intrinsic
Hall theta package exactly when their comparison obstruction cocycles
against the finite KS transport vanish in every quotient.
```

Local anchors:

- `chapters/theory/bps_positive_geometry_closure.tex:346-388` defines
  the intrinsic Hall theta package by finite KS transport and states the
  comparison corollary.
- `chapters/theory/bps_positive_geometry_closure.tex:488-515` inserts a
  single theta coordinate `o_theta` into the derived obstruction map.
- `chapters/theory/bps_positive_geometry_closure.tex:538-578` identifies
  the theta-comparison zero fiber with `o_theta = 0`.
- `compute/lib/bps_positive_truncation.py:722-742` implements
  `theta_comparison_certificate` from support, Hall associativity,
  sector descent, and an `A_2` KS/GPS holonomy check.
- `compute/lib/bps_positive_truncation.py:872-878` makes the
  solution-stack theta factor have only two obstruction coordinates:
  `joint_holonomy` and `comparison_cocycle`.

## strongest failure mode

The scalar comparison coordinate is not a complete obstruction object
for external theta packages.  It proves a finite intrinsic Hall
transport check, but it does not encode the existence hypotheses of the
external packages being compared.

The missing coordinates are visible already in the stronger local theta
note:

- broken-line package:
  `notes/bps_positive_geometry_total_resolution_20260424/agent_08_theta_enhancement.md:291-313`
  defines the data
  `(B_Z, iota, Sigma^sc, D^Hall, Asymp, Bend)`;
  `:317-333` requires local finiteness, consistency, strict height
  growth, finite bending, orientation compatibility, and triangular
  asymptotics; `:393-410` records
  `(o_locfin,o_joint,o_height,o_orient,o_tri)`.
- GHKK package:
  `agent_08_theta_enhancement.md:422-444` defines the cluster package
  with seed tori, cluster scattering, Hall-cluster identification, EGM,
  and canonical GHKK construction; `:452-466` lists the hypotheses;
  `:513-532` records
  `(o_atlas,o_scatter,o_EGM,o_upper,o_orient,o_mut)`.
- GMN package:
  `agent_08_theta_enhancement.md:541-577` defines the spectral-network
  package with spectral cover, Seiberg-Witten differential, relative
  charge lattice, networks, abelianization, detours, line defects,
  halos, and Hall comparison; `:581-596` requires central-charge period
  agreement, finite detours, 2d-4d wall crossing, halo/Hall
  identification, enough triangular line defects, spin/orientation
  agreement, and sector/truncation descent; `:651-676` records
  `(o_cover,o_period,o_detour,o_2d4d,o_halo,o_framed,o_spin,o_abel)`.
- package-to-package comparison:
  `agent_08_theta_enhancement.md:931-978` requires comparison data
  identifying core charges, wall factors, orientation signs, half-Tate
  normalizations, finite truncations, sector restriction maps, and
  multiplication correspondences.

The executable engine confirms the compression.  The command

```bash
python3 - <<'PY'
from compute.lib.bps_positive_truncation import (
    TruncationBound,
    derived_solution_stack_factors,
    theta_comparison_certificate,
)
b = TruncationBound(5, 6, 1)
c = theta_comparison_certificate(b)
print(c.name, c.passed, c.exact, c.checked_items, c.discrepancies)
for f in derived_solution_stack_factors(b):
    if f.name == "theta_comparison":
        print(f.obstruction.names, f.obstruction.values, f.obstruction.vanishes, f.certificate.exact)
PY
```

returned

```text
theta_comparison True False 318 ()
('joint_holonomy', 'comparison_cocycle') (Fraction(0, 1), Fraction(0, 1)) True False
```

Thus the finite oracle marks the theta obstruction vector as zero by
construction, while the certificate itself is not exact and does not
test the package-existence coordinates above.

## fatal/nonfatal verdict

Fatal for the advertised external comparison theorem as presently
stated.  A single `o_theta` does not decide equality with broken-line,
GHKK, or GMN theta packages.  It omits broken-line convergence/local
finiteness, GHKK seed/EGM/upper-algebra data, GMN central charge and
sector dependence, detour/halo/line-defect data, multiplication
compatibility, and compact-support finiteness.

Nonfatal for the intrinsic finite Hall theta construction under the
stated finite hypotheses.  The present engine does check Hall support,
Hall associativity, sector descent, and an `A_2` scattering witness.  It
is a correct intrinsic Hall-transport certificate, not a complete
external comparison certificate.

Nonfatal for the conifold/GPS toy comparison.  The targeted executable
checks

```bash
pytest -q \
  compute/tests/test_bps_positive_truncation.py::test_theta_comparison_certificate \
  compute/tests/test_scattering_diagram.py::test_scattering_diagram_seed_walls_and_first_symmetric_root \
  compute/tests/test_tropical_shadow_cluster.py::TestBrokenLines::test_forced_charge_count \
  compute/tests/test_tropical_shadow_cluster.py::TestMultiPathCrossVerification::test_cross_gps_vs_broken_line_at_11
```

gave

```text
4 passed in 0.20s
```

Those tests only certify the finite rank-two/A2 boundary surface.
`compute/lib/tropical_shadow_cluster.py:786-832` explicitly says its
broken-line counter is simplified and that the full GPS broken-line
algorithm requires more bookkeeping.

## exact repair/heal theorem statement

Replace the scalar theta coordinate by a package-indexed comparison
obstruction vector.

Let

```tex
T \in \{\mathfrak T_{\rm bl},\mathfrak T_{\rm GHKK},
        \mathfrak T_{\rm GMN},\mathfrak T_{\rm Hall}\}
```

be a theta package over the same finite chamber datum
`(Gamma, Z, S, o, lambda, b)`.  Define

```tex
V_\theta =
  V_{\rm bl}
  \oplus V_{\rm GHKK}
  \oplus V_{\rm GMN}
  \oplus V_{\rm Hall}
  \oplus V_{\rm cmp}
```

with

```tex
o_{\rm bl} =
(o_{locfin},o_{joint},o_{height},o_{bend},o_{orient},o_{tri},o_{sat}),
```

```tex
o_{\rm GHKK} =
(o_{atlas},o_{scatter},o_{EGM},o_{upper},o_{orient},o_{mut},o_{comp}),
```

```tex
o_{\rm GMN} =
(o_{cover},o_{period},o_{sector},o_{detour},o_{2d4d},
 o_{halo},o_{framed},o_{spin},o_{abel},o_{OPE},o_{comp}),
```

and `o_cmp(T,Hall)` the difference between the two finite theta
transports after identifying core charges, wall functions, orientation
signs, half-Tate normalizations, finite truncations, sector restriction
maps, and multiplication correspondences.

**Healed theorem.**  In a finite chamber quotient, the intrinsic Hall
theta package exists when finite KS joint holonomies vanish and the
Hall product is associative with sector descent.  For an external
package `T`, the equality

```tex
\Theta_T^{\lambda,b}
\simeq
\Theta_{\rm Hall}^{\lambda,b}
```

holds if and only if the package-existence obstruction `o_T` vanishes
and the comparison obstruction `o_cmp(T,Hall)` vanishes.  The completed
comparison is the inverse limit over `lambda`, provided the transition
maps preserve the package data, the comparison maps, and the saturated
theta label set.

This is strictly stronger than the current corollary: it keeps the
intrinsic Hall basis, decomposes every external comparison into its
actual geometric inputs, and makes the zero fiber faithful to broken
lines, GHKK, and GMN rather than collapsing them into one unnamed
cocycle.

## local file anchors

- `chapters/theory/bps_positive_geometry_closure.tex:346-379`:
  intrinsic Hall theta basis by finite KS transport.
- `chapters/theory/bps_positive_geometry_closure.tex:382-388`:
  comparison corollary being attacked.
- `chapters/theory/bps_positive_geometry_closure.tex:488-515`:
  current one-coordinate `V_theta` insertion.
- `chapters/theory/bps_positive_geometry_closure.tex:540-560`:
  derived zero-locus theorem identifying theta comparison with
  `o_theta = 0`.
- `compute/lib/bps_positive_truncation.py:722-742`:
  executable theta certificate checks only support, Hall associativity,
  sector descent, and finite A2 holonomy.
- `compute/lib/bps_positive_truncation.py:872-878`:
  theta obstruction vector has only `joint_holonomy` and
  `comparison_cocycle`.
- `compute/lib/scattering_diagram_e1_mc.py:32-50`:
  engine separates exact quantum-torus DT formulation from BCH
  approximation.
- `compute/lib/scattering_diagram_e1_mc.py:90-102`:
  warning that exact pentagon is quantum-torus level, while BCH forced
  wall multiplicities are not DT invariants.
- `compute/lib/scattering_diagram_e1_mc.py:104-110`:
  local literature anchors for Gross-Siebert, GPS, GHKK, KS,
  Bridgeland, and cluster technology.
- `compute/lib/tropical_shadow_cluster.py:786-832`:
  simplified broken-line counter and explicit warning that full GPS
  broken-line bookkeeping is absent.
- `notes/bps_positive_geometry_total_resolution_20260424/agent_11_hostile_synthesis.md:883-909`:
  prior hostile synthesis already states that a theta basis is not
  forced by the Hall cosheaf and must be package-specific.
- `notes/master_synthesis_chambered_bps_positive_geometry_20260424.md:1140-1145`:
  general compact-CY3 theta bases and non-class-S GMN bases remain
  outside theorem-grade construction unless a package is supplied.

## primary/literature anchors if needed from existing bibliography or local notes

- Kontsevich--Soibelman 2008, `bibliography/references.tex:707-708`,
  supplies the motivic DT stability and wall-crossing framework used in
  `bps_positive_geometry_closure.tex:371-374`.
- Gross--Pandharipande--Siebert, Gross--Hacking--Keel--Kontsevich,
  Bridgeland, and Gross--Siebert are recorded as local engine anchors in
  `compute/lib/scattering_diagram_e1_mc.py:104-110` and
  `compute/lib/tropical_shadow_cluster.py:138-146`.
- GMN wall crossing is recorded locally in
  `notes/research_bps_graph_spectral_network.md:225-235`; the same note
  warns that strict GMN spectral networks do not directly apply to
  `K3 x E` at `:333-345`.
- The manuscript itself keeps the K3/GMN-to-BKM bridge conjectural at
  `chapters/examples/k3_chiral_bialgebra_platonic.tex:2178-2203`.

## executable checks proposed or run

Run:

```bash
pytest -q \
  compute/tests/test_bps_positive_truncation.py::test_theta_comparison_certificate \
  compute/tests/test_scattering_diagram.py::test_scattering_diagram_seed_walls_and_first_symmetric_root \
  compute/tests/test_tropical_shadow_cluster.py::TestBrokenLines::test_forced_charge_count \
  compute/tests/test_tropical_shadow_cluster.py::TestMultiPathCrossVerification::test_cross_gps_vs_broken_line_at_11
```

Result:

```text
4 passed in 0.20s
```

Additional run:

```bash
python3 - <<'PY'
from compute.lib.bps_positive_truncation import (
    TruncationBound,
    derived_solution_stack_factors,
    theta_comparison_certificate,
)
b = TruncationBound(5, 6, 1)
c = theta_comparison_certificate(b)
print(c.name, c.passed, c.exact, c.checked_items, c.discrepancies)
for f in derived_solution_stack_factors(b):
    if f.name == "theta_comparison":
        print(f.obstruction.names, f.obstruction.values, f.obstruction.vanishes, f.certificate.exact)
PY
```

Result:

```text
theta_comparison True False 318 ()
('joint_holonomy', 'comparison_cocycle') (Fraction(0, 1), Fraction(0, 1)) True False
```

Proposed executable upgrades:

1. Add `theta_package_obstruction_certificate(package, bound)` returning
   package-specific coordinates for `bl`, `GHKK`, `GMN`, and `Hall`.
2. For `bl`, test local finiteness, strict height increase, finite
   bending, triangular leading term, orientation compatibility,
   saturation of labels, and transition compatibility.
3. For `GHKK`, test a cluster atlas object, exchange/skew-form
   agreement, Hall/cluster scattering identification, EGM or replacement
   basis hypothesis, mutation compatibility, and upper/regular algebra
   target.
4. For `GMN`, test central-charge period agreement, sector dependence
   in `zeta`, finite detour sums, 2d-4d wall crossing, halo/Hall
   conjugation, spin/orientation agreement, abelianization descent, and
   OPE saturation.
5. Replace the theta factor in `derived_solution_stack_factors` by the
   package-indexed vector above; the current two-coordinate vector is
   only the Hall-transport subfactor.

## remaining point-construction obligation

The remaining point-construction problem is not "define a theta basis"
in the abstract.  The base Hall theta package is already finite-first.
The remaining obligation is to produce, for a named non-toric compact
or compact-derived chamber, one actual external package point:

```tex
(\mathfrak T_{\rm bl} \text{ or } \mathfrak T_{\rm GHKK}
 \text{ or } \mathfrak T_{\rm GMN})
```

with all package obstructions zero and with a comparison map to the
Hall package preserving sectors, central charges, orientations,
half-Tate normalizations, finite truncations, and multiplication.

The smallest executable target is the conifold/cluster sector, already
covered by rank-two tests.  The first genuinely non-toric target should
be a cluster-atlas or spectral-network locus where the charge lattice,
central charge, and Hall scattering are explicitly identified; without
that point, the current zero fiber proves intrinsic Hall transport but
does not yet prove GHKK/GMN/broken-line equality for a compact CY3
chamber.
