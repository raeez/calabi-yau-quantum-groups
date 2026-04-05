---
description: "Cross-volume AP5 propagation check from Vol III"
---

# Cross-Volume Propagation Check (AP5) — Vol III

**Pattern**: $ARGUMENTS

Same protocol as Vol I `/propagate`. Extra Vol III nuance:

**AP49 Convention Alert**: Vol III uses motivic/categorical conventions. Vol I uses OPE modes. Vol II uses lambda-brackets. When grepping for a Vol III formula in Vol I/II, verify convention compatibility before comparing.

**AP-CY8**: Borcherds product identities may look like bar Euler products but the identification requires the CY-to-chiral functor to exist in the relevant dimension. For d=3, this is OPEN.

```bash
grep -rn "$ARGUMENTS" ~/chiral-bar-cobar/chapters/ ~/chiral-bar-cobar/appendices/ 2>/dev/null
grep -rn "$ARGUMENTS" ~/chiral-bar-cobar-vol2/chapters/ ~/chiral-bar-cobar-vol2/appendices/ 2>/dev/null
grep -rn "$ARGUMENTS" ~/calabi-yau-quantum-groups/chapters/ ~/calabi-yau-quantum-groups/notes/ 2>/dev/null
```
