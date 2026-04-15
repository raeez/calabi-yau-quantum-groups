# First-Principles Investigation Protocol

INVESTIGATION_ACTIVE

When a mathematical claim is challenged, confused, or found to be wrong, you MUST complete this protocol BEFORE making any Edit. Do NOT skip steps. Do NOT make shallow corrections (swapping one label for another).

## The Protocol

### Step 1: State the claim under investigation
Write out the exact mathematical claim being challenged. Quote the manuscript text.

### Step 2: What does it get RIGHT?
Every wrong claim contains the ghost of a true theorem. Find it. There is ALWAYS a mathematical relationship between the objects — identify it precisely. If you can't find anything right, you haven't looked hard enough.

### Step 3: What does it get WRONG?
Identify the PRECISE conflation, scope error, or false generalization. Name the two things being confused. State why they are different (different types, different categories, different levels of structure).

### Step 4: State the correct mathematical relationship
Write the actual theorem, construction, or factorization that connects the objects. This must be a MATHEMATICAL STATEMENT, not a label swap. If A ≠ B but they're related, state HOW they're related: adjunction, factorization, decategorification, restriction, specialization, etc.

### Step 5: What goes into the manuscript?
Based on Steps 2-4, determine what content to write:
- A remark explaining the correct relationship (if the claim had real mathematical content)
- A correction of scope (if the claim was true in a restricted case)
- A deletion (only if the claim was genuinely empty)

### Step 6: Make the edits
NOW and ONLY NOW make the corrections. Every correction must include the mathematical content from Step 4, not just a term swap.

## Examples

**BAD**: Replace "categorified averaging" with "right adjoint to forgetful"
**GOOD**: Replace "categorified averaging" with "right adjoint to forgetful" AND write rem:center-not-averaging explaining the factorization E_1 →^Z E_2 →^{Sym} E_∞

**BAD**: Replace "SN bracket vanishes" with "bracket has degree -2"
**GOOD**: Fix the scope (toric vs general), explain the two distinct mechanisms (abelian classical limit vs shifted classical limit), and state which applies where

**BAD**: Delete "CY frontier" as empty slogan
**GOOD**: Replace with the actual computable content (Borel summability, Stokes = KS wall-crossing)

## Step 7: Cache the analysis

Check if this investigation pattern has appeared before:
- Search memory for existing analyses of the same concepts
- If found: use the cached analysis, update if new content discovered
- If NOT found but this is a recurring confusion type: SAVE to memory as a cached investigation

Recurring confusion types to watch for:
- **Native vs derived** (E_n levels, braiding, center)
- **Algebra vs coalgebra** (CoHA vs bar complex, multiplication vs comultiplication)
- **Specific vs general** (toric vs all CY, C^d vs compact, GL(d)-invariant vs full)
- **Construction vs narration** ("gives" vs explicit arrow, "is the face of" vs mechanism)
- **Label vs content** ("CY frontier" vs computable Borel sum, "physical face" vs equivariant localization)

If the same confusion type appears 2+ times in a session, it MUST be cached to CLAUDE.md as a permanent entry with:
- The confusion pattern name
- What gets conflated
- The correct relationship (with actual mathematics)
- Worked example from the manuscript

## Mathematical Relationship Dictionary

Before any correction, check this dictionary (maintained in CLAUDE.md under "Cached First-Principles Analyses"). If the relationship is already cached, use it. If not, add it after completing the protocol.

## Systematic Techniques

Beyond the per-challenge protocol, apply these systematic defenses:

### 1. Mathematical type-checking
Every object has a type: algebra, coalgebra, category, functor, natural transformation, etc. When two objects are equated or identified, verify their types match. "CoHA = bar complex" fails: algebra ≠ coalgebra.

### 2. Scope-drift detection
When a result proved for case X (toric, d=2, C^3) is used in context Y (general, d=3, compact), the scope has drifted. The hook detects some of this; you must catch the rest by tracking the provenance of every claim.

### 3. Adversarial self-test
Before accepting a correction, try to break the NEW claim. If "the Drinfeld center is the right adjoint to forgetful" — can you construct a scenario where this framing is misleading? If so, refine further.

### 4. Ghost theorem extraction
Every wrong claim contains the seed of a correct theorem. "CoHA = bar complex" → the SV theorem. "SN bracket vanishes universally" → the operadic degree argument. "Categorified averaging" → the factorization E_1 → E_2 → E_∞. ALWAYS extract the ghost theorem.

### 5. Confusion fingerprinting
Track which TYPE of confusion each error belongs to (native/derived, algebra/coalgebra, specific/general, construction/narration, label/content). If a type recurs, the systematic defense for that type must be strengthened.

## Anti-pattern (AP-CY61)
Shallow correction without first-principles investigation. When a mathematical claim is challenged, do NOT just swap labels. ALWAYS investigate the actual mathematical relationship from first principles. Find: (1) what the claim gets RIGHT, (2) what it gets WRONG, (3) the correct mathematical statement connecting the objects.
