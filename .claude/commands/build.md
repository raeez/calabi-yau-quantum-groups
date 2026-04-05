---
description: "Build Vol III, run tests"
---

# Build Vol III

```bash
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2
cd ~/calabi-yau-quantum-groups && make fast
echo "=== Vol III build complete ==="
cd ~/calabi-yau-quantum-groups && python3 -m pytest compute/tests/ -x --tb=short -q 2>/dev/null || echo "No Vol III tests or test failure"
echo "=== Tests complete ==="
```
