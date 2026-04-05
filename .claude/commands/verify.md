---
description: "Multi-path formula verification for Vol III claims"
---

# Multi-Path Formula Verification — Vol III

**Claim**: $ARGUMENTS

Same 8-path taxonomy as Vol I `/verify`. Vol III-specific:

### Additional verification paths
- **CY trace check**: Verify claim is compatible with HC^-_d(C) trace (AP-CY2: NOT just HH_d -> k)
- **Dimension check**: CY dimension d != complex dimension n (AP-CY1)
- **KL consistency**: If claim involves quantum groups, verify q-parameter regime (AP-CY5: generic vs root of unity)
- **Convention bridge**: Verify the same formula in Vol I and Vol II conventions (AP49)
- **Existence check**: Does the claim require G(X) or A_X for CY3? If so, it is conditional (AP-CY6)

Minimum 3 independent paths. Write tests. Cross-check across volumes.
