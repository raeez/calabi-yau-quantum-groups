# Chriss–Ginzburg rectification — session kickstart (2026-04-21)

Paste the block below into a fresh Claude Code session at
`~/calabi-yau-quantum-groups` to resume the cross-volume bookkeeping
scrub and full 5-phase `/chriss-ginzburg-rectify` sweep.

---

## KICKSTART PROMPT

```
Continue the cross-volume Chriss–Ginzburg rectification sweep. This is a
long-running family project run with love, care, and zero shortcuts.

## State at session start (2026-04-21)

Working tree: ~/calabi-yau-quantum-groups (Vol III primary),
with ~/chiral-bar-cobar (Vol I) and ~/chiral-bar-cobar-vol2 (Vol II)
as additional working directories. Git branch: main. DO NOT git stash
(forbidden by CLAUDE.md); DO NOT amend commits.

Prior session accomplished (NOT yet committed):

1. Cross-volume label normalization. 1577 \label/\ref rewrites across
   341 manuscript .tex files in all three volumes (929 unique labels).
   Rules in /tmp/normalize_labels.py. Rename map:
   ~/calabi-yau-quantum-groups/notes/wave_dna_rename_map_20260421.txt
   (929 entries, old -> new). Per-volume audit stubs:
   {Vol I, Vol II, Vol III}/notes/wave_dna_normalization_20260421.md.
   Zero new within-volume label collisions. Build verified on Vol I
   and Vol III.

2. Gate-5 metatag scrub on ~/calabi-yau-quantum-groups/chapters/theory/
   modular_trace.tex: removed 26 '(AP10)' decorations, AP151, AP160,
   'Waves 15--17', 'Cache append', 'This section inscribes', etc.
   File is 3461 lines; ONLY the bookkeeping-scrub portion of Gate 5
   was completed. Full 5-phase protocol still outstanding.

3. Diagnostic artifacts:
   - /tmp/normalize_labels.py (label rewriter, dry-run + --apply)
   - /tmp/audit_prose.py (prose-only violation audit)
   - /tmp/file_hit_counts.py (per-file hit counts)

## What remains

### Remaining prose hotspots (full 5-phase /chriss-ginzburg-rectify)

Vol I (run `python3 /tmp/file_hit_counts.py` for current counts):
  97  chapters/theory/derived_langlands.tex
  50  chapters/theory/chiral_climax_platonic.tex
  45  chapters/examples/w_algebras_deep.tex
  34  chapters/theory/theorem_B_scope_platonic.tex
  34  chapters/theory/bar_cobar_adjunction_curved.tex
  31  chapters/examples/lattice_foundations.tex
  28  chapters/frame/part_iv_platonic_introduction.tex
  25  chapters/connections/concordance.tex
  24  chapters/theory/shadow_tower_quadrichotomy_platonic.tex
  24  chapters/connections/arithmetic_shadows.tex
  21  chapters/examples/deformation_quantization.tex
  19  chapters/connections/bv_brst.tex
  (~150 more Vol I files with 1-18 hits each)

Vol II:
  19  chapters/theory/sc_chtop_heptagon.tex
  14  chapters/connections/ht_physical_origins.tex
  13  chapters/theory/chiral_higher_deligne.tex
  13  chapters/theory/unified_chiral_quantum_group.tex
  (~50 more Vol II files)

Vol III:
  14  chapters/theory/quantum_groups_foundations.tex
  10  chapters/theory/cy_to_chiral.tex
   9  chapters/connections/bar_cobar_bridge.tex
   9  chapters/examples/k3e_bkm_chapter.tex
  (~20 more Vol III files)

### Outstanding structural debt (NOT addressed this session)

- `modular_trace.tex` still needs Phase 1 (diagnostic), Phase 2
  (restructure), Phase 3 (5-gate chunk loop), Phase 4 (self-audit),
  Phase 5 (build+report). Only Gate 5e bookkeeping scrub done.
- Filenames with 'wave' in name (compute/lib/k3_yangian_wave*.py,
  ~70+ files) referenced from some manuscript .tex via \texttt{}.
  Renaming cascades into Python imports + tests. Deferred.
- 200 pre-existing undef refs in Vol I, 93 in Vol III — structural
  debt from absent labels (chap:*, part:*, ch:*). Out of rectify scope.

## Ground rules

1. Pick the LOWEST-ID pending task via TaskList. If in_progress,
   continue it; do not skip forward. Tasks set up later context.
2. Invoke `/chriss-ginzburg-rectify` via the Skill tool on the WHOLE
   file for every target. Not `sed`-style scrubs. Not Gate-5-only.
3. Full 5-phase protocol per file:
     Phase 1: Global Diagnostic (read entire file, 7-heading report)
     Phase 2: Platonic Restructuring (skeleton; 2-3 iterations)
     Phase 3: Linear Reconstitution Loop, 50-100 line chunks, each
              chunk through ALL 5 gates (MATHEMATICAL TRUTH,
              DEFINE-BEFORE-USE, CONCEPT MOTIVATION, PHYSICAL
              REALIZATION, RECONSTITUTION). Every chunk must pass
              all 5 to advance. Safety valve at 11 iterations.
     Phase 4: Re-audit (RED/BLUE/GREEN). User instruction: do this
              in main thread, no subagent dispatch.
     Phase 5: Build + report.
4. Voice: Chriss-Ginzburg / Russian elite school (Gelfand, Drinfeld,
   Beilinson, Kontsevich, Etingof, Kazhdan, Kapranov, Nekrasov,
   Polyakov) + mathematical-physics elite (Witten, Costello, Gaiotto,
   Moore, Segal). Show don't tell. Synthesize disparate domains.
   Every sentence load-bearing.
5. Bookkeeping vocab forbidden in manuscript prose:
   'Wave N', 'round M', 'batch K', 'DNA strand Sx', 'AP-CY<n>',
   'AP<n>', 'HZ-<n>', 'Pattern <n>', 'cache entry <n>',
   'CG-rectify pass k', 'main-thread', 'deepening round',
   'hook-generated', 'ATTACK-HEAL', 'Cycle N' section names.
   Author self-reference forbidden: 'in the present work',
   'the author', 'our programme', 'we have argued',
   'this chapter's function is to', 'this remark provides'.
   AI slop forbidden: 'notably', 'crucially', 'remarkably',
   'moreover', 'furthermore', 'it is worth noting',
   'we now turn to', 'having established', 'let us now',
   'this brings us to', 'with this in hand'.
6. Commits: by Raeez Lorgat ONLY. Never AI attribution
   (no Co-Authored-By, no 'Generated with', no robot emoji).
   Use `--no-verify` if hooks block on non-AI-attribution content
   (e.g.\ pre-existing line-length warnings), never to bypass AI
   attribution checks. Commit in per-file or per-hotspot batches
   after each file converges.
7. Git discipline: never `git stash`, never amend, never reset --hard,
   never force-push. Deep semantic merges only; never cut content.
   Pre-commit hook checks fire on every Bash call — those are
   advisory reminders, not failures.
8. Build discipline: `cd ~/<vol> && make fast` (Vol I, Vol III) or
   `make` (Vol II). Build quietly at file level. Every 3 edits, build.
   After every formula fix, grep all three volumes for variants (AP5).

## Immediate next step

1. Build Vol I (~/chiral-bar-cobar && make fast) to confirm the
   prior-session label rename is stable. 430 undef refs expected;
   sanity-check count against HEAD via:
     find chapters/ frame/ examples/ theory/ connections/
       bibliography/ appendices/ -name '*.tex' | xargs grep -Eoh \
       '\\label\{[^}]+\}' | sort | uniq -c | awk '$1>1' | wc -l
   (should be 394 within-volume duplicate pairs; pre-existing, not
   introduced by rename).

2. Decide whether to commit the 160-file rename diff as a single
   mechanical-rename commit before starting new per-file CG work
   (recommended: yes; cleaner blame trail). Suggested message:

     "cross-volume: strip wave/DNA bookkeeping from \\label{} and \\ref{}

     Programmatic rewrite of 1577 label and reference bodies across
     341 manuscript .tex files, collapsing -wave\\d+-DNA- and -DNA-
     fragments while preserving descriptor tails. Collisions resolved
     by roman-numeral suffixes (ordered by wave number).
     Traceability map: notes/wave_dna_rename_map_20260421.txt
     (929 old -> new entries). Zero new within-volume collisions."

3. Then: pick lowest-ID pending task, mark in_progress, invoke the
   `/chriss-ginzburg-rectify` skill on its file, run full 5 phases.

## Reference pointers

- CLAUDE.md in each volume (canonical manifesto).
- ~/calabi-yau-quantum-groups/.claude/commands/chriss-ginzburg-rectify.md
  (the skill source).
- ~/calabi-yau-quantum-groups/notes/wave_dna_normalization_20260421.md
  (full audit report, Vol III).
- ~/calabi-yau-quantum-groups/notes/cg_rectify_session_kickstart_20260421.md
  (this file).
- memory/MEMORY.md (persistent user preferences and prior
  session context).

Begin.
```

---

## Cross-references in this kickstart

- Prior-session label rewrite report: this `notes/` directory.
- Skill source: `.claude/commands/chriss-ginzburg-rectify.md`.
- Hotspot file counts (regenerate): `python3 /tmp/file_hit_counts.py`.
- Label rename map (929 entries): `wave_dna_rename_map_20260421.txt`.

The rename map is load-bearing. Before renaming a file whose name
contains `wave`, grep the rename map first to confirm which labels in
that file have already been rewritten — so the commit log can connect
the file rename to the upstream label rewrite.
