# Chriss-Ginzburg Rectification — Kickstart for Volume Instances

> **Audience**: the Claude instance working on a Volume of the Modular Koszul Duality monograph (Vol I, Vol II, or Vol III). This file tells you how to stand up the same CG-rectify cron architecture Vol III set up on 2026-04-17.

## What this is

A scheduled remote agent runs `/chriss-ginzburg-rectify` once per hour on the next pending chapter of this volume, commits, pushes, advances the queue, exits. Fresh context per tick. The user does not babysit.

Reference implementation: **Vol III** (`~/calabi-yau-quantum-groups`), trigger `trig_01EwyA6My2f9sdmBdMYCcMZD`, queue file `notes/chriss_ginzburg_full_rectify_queue.md`, commit `b5648b4` (2026-04-17).

## Why this architecture

Large volumes have 30+ chapters. Some are 5,000+ lines. Running the full 5-phase skill (global diagnostic → platonic restructuring → chunk-by-chunk 5-gate loop → 3-agent adversarial re-audit → final convergence) on every chapter requires many independent sessions. Doing this in one long interactive session:

- blows out context budget (each chapter consumes ~30% of a session)
- loses coherence when compaction fires mid-chapter
- needs human presence

The cron solves all three: one chapter per firing, fresh context each time, no human required.

## One-time setup (do this now)

### 1. Read your volume's `CLAUDE.md`

Every volume has its own `CLAUDE.md` with volume-specific anti-patterns, conventions, and hard rules. Internalize it. Vol III's is canonical for CY/chiral conventions; Vol I's is canonical for bar-cobar/modular characteristic; Vol II's is canonical for SC^{ch,top}/PVA/DK.

### 2. Build the queue file

Create `notes/chriss_ginzburg_full_rectify_queue.md`. Enumerate every chapter in this volume EXCEPT the abstract, preface, and introduction. Use this format:

```markdown
# Chriss-Ginzburg full-rectify queue (Vol <N>, <date>)

Loop directive: run `/chriss-ginzburg-rectify` on every <volume> chapter EXCEPT
abstract, preface, introduction. Cron: `<trigger_id>` (hourly, claude-opus-4-7).
Dashboard: https://claude.ai/code/scheduled/<trigger_id>

One chapter per tick. Each tick: pick first `[ ]` entry, rectify, mark `[x]`
(or `[~]` partial for files >3000 lines), commit with author "Raeez Lorgat",
push to main.

## Chapters

### <part>/ (<N files>)

- [ ] `chapters/<part>/<chapter1>.tex`
- [ ] `chapters/<part>/<chapter2>.tex`
...

## Standalone papers

- [ ] `standalone/<paper1>.tex`
...

## Completion log

Each entry: `YYYY-MM-DD HH:MM  <file>  commit=<sha>  notes`
```

Source the chapter list from `main.tex` (look for `\input{chapters/...}` lines) in the correct reading order. Do NOT include introduction.tex, preface.tex, or the abstract.

### 3. Load the RemoteTrigger tool

```
ToolSearch select:RemoteTrigger
```

### 4. Create the cron trigger

Call `RemoteTrigger({action: "create", body: <below>})` with the volume-specific placeholders filled in.

**Body template:**

```json
{
  "name": "CG-rectify Vol <N> loop",
  "cron_expression": "0 * * * *",
  "enabled": true,
  "job_config": {
    "ccr": {
      "environment_id": "env_01R28K7zJ8jcrHR79Zw1FkkK",
      "session_context": {
        "model": "claude-opus-4-7",
        "sources": [
          {"git_repository": {"url": "https://github.com/raeez/<REPO_NAME>"}}
        ],
        "allowed_tools": ["Bash", "Read", "Write", "Edit", "Glob", "Grep",
                          "Skill", "Agent", "TaskCreate", "TaskUpdate",
                          "TaskList", "TaskGet"]
      },
      "events": [{"data": {
        "uuid": "<generate fresh v4 lowercase UUID>",
        "session_id": "",
        "type": "user",
        "parent_tool_use_id": null,
        "message": {"role": "user", "content": "<ONE-TICK PROMPT BELOW>"}
      }}]
    }
  }
}
```

Replace:
- `<N>` with the volume number
- `<REPO_NAME>` with the volume's GitHub repo name
  - Vol I: `chiral-bar-cobar`
  - Vol II: `chiral-bar-cobar-vol2`
  - Vol III: `calabi-yau-quantum-groups`
- Generate a fresh v4 UUID yourself
- Inline the one-tick prompt (next section) as the `content`

Minimum cron interval is 1 hour. Keep it hourly unless you have reason otherwise.

Use Momentum environment `env_01R28K7zJ8jcrHR79Zw1FkkK` (confirmed working). Use model `claude-opus-4-7` (deep math requires Opus).

### 5. Commit the queue file and cron reference

```bash
git add notes/chriss_ginzburg_full_rectify_queue.md notes/cg_rectify_kickstart.md
git commit -m "CG-rectify Vol <N>: queue + cron <trigger_id> set up"
git push origin main
```

Make sure the queue file contains the trigger ID before committing so the remote agent (and future you) knows which cron owns this queue. Author: `Raeez Lorgat`. NO Anthropic/Claude attribution.

## The one-tick prompt (inline into `events[].data.message.content`)

Copy this verbatim, substituting `<VOLUME>` with `Vol I` / `Vol II` / `Vol III`:

```
You are a remote agent running one tick of the Chriss-Ginzburg rectification
loop on <VOLUME> of *Modular Koszul Duality*.

=== ONE-TICK MISSION ===
Rectify exactly ONE chapter per firing. The queue file
`notes/chriss_ginzburg_full_rectify_queue.md` tracks progress across sessions.
Fresh context every tick — rely only on the repo state and the queue file.

=== PROCEDURE ===
1. Read `CLAUDE.md` (volume-specific anti-patterns, conventions, hard rules).
   Skim sibling volumes' CLAUDE.md for cross-volume context if they exist at
   `~/chiral-bar-cobar`, `~/chiral-bar-cobar-vol2`, `~/calabi-yau-quantum-groups`.

2. Read `notes/chriss_ginzburg_full_rectify_queue.md`. Find the FIRST pending
   entry matching `- [ ] \`chapters/...` (unchecked backticked path). If none,
   look for `[~]` (partial) entries and select one for a second pass. If neither
   exists, report `QUEUE EMPTY — campaign complete` and exit cleanly.

3. Invoke the rectification skill on that file:
     Skill(skill="chriss-ginzburg-rectify", args="<the file path>")

4. Execute ALL FIVE phases (do NOT shortcut):
   - Phase 1: Global diagnostic (read the whole file; 7-heading diagnostic).
   - Phase 2: Platonic restructuring (skeleton + AP-metadata scrub:
     strip all `AP-CY*`, `AP1*`, `HZ3-*`, `2026-*`, `inscription`, `campaign`,
     `healed`, `first edition`, `earlier phrasing`, `adversarial` labels,
     `RECTIFICATION-FLAG` markers from reader-facing prose).
   - Phase 3: 50-line chunk loop, 5 gates per chunk to convergence
     (up to 11 iterations; then flag with `% RECTIFICATION-FLAG` comment).
   - Phase 4: 3-agent parallel re-audit (RED adversarial, BLUE consistency,
     GREEN quality). Launch via Agent tool in ONE message. Apply findings at
     severity >= MODERATE.
   - Phase 5: Final report (line count, chunks, iterations, findings by class,
     agent verdicts).

5. BUDGET: If target file > 3000 lines, do Phase 2 scrub + Phase 4 audit +
   apply CRITICAL/SERIOUS findings, mark queue entry `[~]` partial with
   detailed residual-findings note. Large chapters need multiple ticks.

6. Build check: `make fast` if it works; else grep-based balance check
   (`grep -c '^\\begin{'` == `grep -c '^\\end{'`).

7. Run relevant tests: `make test` or
   `python3 -m pytest compute/tests/test_<name>.py -v`.

8. Update the queue file: `- [ ]` → `- [x]` (or `[~]` partial) with one-line
   note: date, phase coverage, key fixes, agent verdicts.

9. Commit:
     git add -A
     git commit -m "CG-rectify: <filename> — <one-line summary>"
     git push origin main

=== HARD RULES ===
- Author is ALWAYS `Raeez Lorgat`. NEVER add `Co-Authored-By: Claude` or any
  LLM attribution. `git stash` is FORBIDDEN.
- NEVER use `--no-verify` or `--no-gpg-sign`.
- NEVER skip phases; if context runs short, flag partial progress and exit.
- NEVER preemptively edit a different chapter (AP5 cross-volume formula fixes
  are the one exception — propagate but note in the target chapter's queue).
- ZERO TOLERANCE on manuscript metadata: prose must not contain AP/HZ3 tags,
  session timestamps, commit hashes, "healed" / "now proved" / "is now
  constructed" / "adversarial audit" / "earlier phrasing" / "first edition".
  These belong in commit messages / notes/. Strip on sight.
- ZERO TOLERANCE on bare `\kappa`: must carry a subscript (volume-specific
  allowed set; see CLAUDE.md).

=== VOLUME-SPECIFIC RULES ===
<Add any additional hard rules specific to this volume's CLAUDE.md here.
 Example for Vol III: CY-A_3 IS PROVED (inf-cat framework); CY-C CONJECTURAL;
 CoHA(C^3)=Y^+ not full Yangian; six routes to G(K3xE) are different
 constructions not six Phi applications.>

=== EXIT ===
Report in one short paragraph: which file, phase coverage, agent verdicts,
line count, key fixes, any residual flags. The report appears in the cron log;
the diff speaks for itself in the repo.
```

## Operational notes

- **First firing**: The trigger's first firing is within an hour of creation. Check the dashboard URL in the queue file to monitor.
- **Monitoring**: Each tick commits + pushes. `git log --oneline` on main will show the rectification trail. Cron logs are at the dashboard URL.
- **Budget**: A tick runs against Opus 4.7. Large chapters may hit context limits; the one-tick prompt's BUDGET rule handles this gracefully by marking `[~]` partial.
- **Stopping**: The cron stops only when the queue is empty (emits `QUEUE EMPTY — campaign complete`), or when you disable it via the dashboard.
- **Partial chapters**: A `[~]` entry will be picked up on a later tick for a second pass. Keep them in the queue until fully `[x]`.
- **Cross-volume AP5 fixes**: If a rectification in Vol N touches formulas that have duplicates in Vol M ≠ N, the agent should edit the parallel location in Vol M as well (when accessible locally), note the propagation in the Vol M queue, but NOT invoke the skill on the Vol M file. That belongs to Vol M's own queue.

## Hard rules worth re-stating

- **All commits authored by Raeez Lorgat**. No LLM attribution. No `Co-Authored-By:`. No emojis in commit messages.
- **`git stash` is forbidden**. Use branches or discard explicitly.
- **Pre-commit verification**: build passes (if pdflatex available), tests pass (if applicable), no AI attribution.
- **Sibling volumes**: when cross-referencing Vol I / II / III, use `\ref{...}` with a clear label, never `Part~N` hardcoded. Refer to sibling CLAUDE.md for the right label namespace.

## If something goes wrong

- **Trigger creates but never fires**: check it is enabled via `RemoteTrigger({action: "get", trigger_id: "..."})`. `enabled` must be `true`.
- **Agent fails with "queue file not found"**: the queue file was not committed to main. Commit and push it.
- **Agent fails with "skill not available"**: the rectification skill lives at `.claude/commands/chriss-ginzburg-rectify.md` in the repo. Verify it's present and on main.
- **Agent commits but never pushes**: the remote agent's git auth may not include push. Check the environment config.
- **Agent reports CONVERGED but the diff looks thin**: check that the chunk loop actually ran Phase 3. Some chapters genuinely need few fixes; a small diff is not evidence of a shortcut. The completion log entry in the queue file should list agent verdicts.

## Reference artefact

Vol III's trigger was created with this exact shape on 2026-04-17. Grep Vol III's `notes/chriss_ginzburg_full_rectify_queue.md` for the trigger ID and use it as a working example.
