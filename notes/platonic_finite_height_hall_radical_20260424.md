# Finite-Height Hall Pairing Radical / Serre Kernel Report

## Claim Attacked

Positive-half `K3 x E` Borcherds data had a residual promotion gap:
even after the broad finite-height obstruction criterion, four
primitive checks remained bundled rather than isolated:

- nondegenerate Hall pairing modulo the Borcherds Cartan radical;
- exact equality of the Hall kernel with the Borcherds--Serre ideal;
- absence of undeclared primitive central classes;
- inverse-limit compatibility of completion and the Siegel--Borcherds
  associator.

The attacked overreach is:

```text
finite-height character/PBW agreement
  => completed Hall-Drinfeld/Borcherds current object
```

without separately testing pairing radical, Serre kernel, centre, and
associator defects.

## Construction / Failure Mode

At each Borcherds height `H`, the promotion can fail in four independent
finite-dimensional ways:

1. the Hall pairing has radical larger than the allowed Borcherds
   Cartan radical;
2. the tensor algebra on primitive Hall classes has kernel different
   from the finite-height Borcherds--Serre ideal;
3. the finite double has primitive central classes beyond the Cartan
   radical and declared dynamical group-like parameters;
4. the Hall quasi-Hopf associator class does not match the
   Siegel--Borcherds associator, or the `H+1 -> H` transition map does
   not preserve the quotient data.

One nonzero defect at one height blocks completed promotion.  The
denominator identity and `kappa_BKM(Delta_5)=5` verify the Borcherds
target; they do not construct these four Hall-side primitives.

## File Anchors

- `chapters/examples/k3e_bkm_chapter.tex`
  - `thm:k3e-hall-drinfeld-super-yangian-criterion`
  - `cor:k3e-finite-height-promotion-obstruction`
  - `thm:k3e-finite-height-hall-radical-serre-kernel`
- `notes/platonic_finite_height_hall_radical_20260424.md`

## Theorem Added

Added `thm:k3e-finite-height-hall-radical-serre-kernel`.

The theorem defines four finite-height defects:

- `R_H`: symmetric defect measuring equality of the Hall-pairing
  radical with the Borcherds Cartan radical;
- `S_H`: symmetric defect measuring equality of the Hall
  primitive-presentation kernel with the Borcherds--Serre ideal;
- `C_H`: symmetric defect measuring equality of the primitive centre
  with Cartan radical plus declared dynamical central group-likes;
- `A_H`: Hall associator class minus the Siegel--Borcherds associator
  class.

Under the existing positive-half, PBW, and associated-graded coproduct
hypotheses, residual promotion to the completed
Hall--Drinfeld/Borcherds current object holds iff all four defects
vanish at every height and the inverse-system transition maps preserve
the vanished defects.  If not, the first residual failure height is

```text
H0 = min { H : R_H, S_H, C_H, or A_H is nonzero, or transition
           compatibility fails }.
```

## Verification Run

- Read `AGENTS.md` and `CLAUDE.md`.
- Checked existing K3xE finite-height anchors with `rg` and local
  `sed` reads.
- Checked current dirty worktree with `git status --short`; treated all
  pre-existing edits as external swarm work.
- Ran targeted LaTeX/source verification after the edit:
  - `rg -n "thm:k3e-finite-height-hall-radical-serre-kernel|mathcal R_H|mathcal S_H|mathcal C_H|mathcal A_H" chapters/examples/k3e_bkm_chapter.tex`
  - a PCRE literal-backslash kappa guard on the touched chapter and
    this note; it surfaced only pre-existing explanatory lines in the
    chapter, not a new formula introduced here.

No full `make fast` run was taken; repo instructions reserve builds for
session end/user opt-in.

## Remaining Primitive Obligations

- Construct the compact oriented critical CoHA on `K3 x E`.
- Construct the finite-height negative half and prove Hall-pairing
  nondegeneracy after quotient by the Borcherds Cartan radical.
- Prove the Hall primitive-presentation kernel is exactly the
  Borcherds--Serre ideal at each height.
- Prove no determinant-line, orientation-line, or chamber scalar
  contributes an extra primitive central class.
- Identify the Hall associator gauge class with the Siegel--Borcherds
  class and prove compatibility under all pro-cone transition maps.

The four-construction spectrum remains `{0, 3, 5, 24}`.
