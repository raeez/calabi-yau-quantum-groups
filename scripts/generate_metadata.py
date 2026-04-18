#!/usr/bin/env python3
"""
Generate machine-readable metadata for Vol II (A-infinity Chiral Algebras).

Portable adaptation of Vol I's scripts/generate_metadata.py. Scans
chapters/, standalone/, appendices/, and main.tex for \\label{...} and
tagged claim environments (\\ClaimStatus*). Outputs:

  metadata/claims.jsonl
  metadata/census.json
  metadata/dependency_graph.dot
  metadata/label_index.json
  metadata/theorem_registry.md

Usage:
  python3 scripts/generate_metadata.py
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field, asdict
from datetime import date
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parents[1]
METADATA_DIR = ROOT / "metadata"

CLAIM_ENVS = {
    "theorem", "lemma", "proposition", "corollary", "conjecture",
    "computation", "calculation", "maintheorem", "verification", "remark",
}

THEOREM_LIKE_ENVS = CLAIM_ENVS | {
    "definition", "example", "construction", "convention",
    "notation", "framework", "principle", "observation",
    "question", "openproblem", "setup", "strategy",
}

STATUS_RE = re.compile(
    r"\\ClaimStatus(ProvedHere|ProvedElsewhere|Conjectured|Conditional|Open|Heuristic)"
)
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
REF_RE = re.compile(
    r"\\(?:ref|autoref|Cref|cref|eqref|nameref|hyperref)\{([^}]+)\}"
)
CITE_RE = re.compile(r"\\cite(?:\[[^\]]*\])?\{([^}]+)\}")
INCLUDE_RE = re.compile(r"\\(?:include|input)\{([^}]+)\}")
BEGIN_RE = re.compile(r"\\begin\{([a-zA-Z]+)\}")
BEGIN_OPT_RE = re.compile(
    r"\\begin\{([a-zA-Z]+)\}\s*\[([^\]]*)\]", re.DOTALL
)

# Part specs: (key, path-prefix, pretty-title). Vol II organises under same
# chapters/{theory,examples,connections,frame} + standalone/ + appendices/.
PART_SPECS = [
    ("frame", "chapters/frame/", "Frame"),
    ("theory", "chapters/theory/", "Theory"),
    ("examples", "chapters/examples/", "Examples"),
    ("connections", "chapters/connections/", "Connections"),
    ("standalone", "standalone/", "Standalones"),
    ("appendices", "appendices/", "Appendices"),
]


@dataclass
class Claim:
    label: str
    env_type: str
    status: str
    file: str
    line: int
    title: str
    labels_in_block: list[str] = field(default_factory=list)
    refs_in_block: list[str] = field(default_factory=list)
    cites_in_block: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        d = asdict(self)
        if not d["labels_in_block"]:
            del d["labels_in_block"]
        if not d["refs_in_block"]:
            del d["refs_in_block"]
        if not d["cites_in_block"]:
            del d["cites_in_block"]
        return d


@dataclass
class LabelEntry:
    label: str
    file: str
    line: int
    env_type: Optional[str] = None


def strip_comments(text: str) -> str:
    lines = []
    for line in text.splitlines():
        result = []
        i = 0
        while i < len(line):
            if line[i] == "%" and (i == 0 or line[i - 1] != "\\"):
                break
            result.append(line[i])
            i += 1
        lines.append("".join(result))
    return "\n".join(lines)


def get_active_files() -> list[Path]:
    main_path = ROOT / "main.tex"
    if not main_path.exists():
        print("ERROR: main.tex not found", file=sys.stderr)
        return []

    main_text = strip_comments(main_path.read_text(encoding="utf-8", errors="ignore"))
    files: list[Path] = []
    seen: set[Path] = set()
    for match in INCLUDE_RE.finditer(main_text):
        rel = match.group(1)
        if not rel.endswith(".tex"):
            rel += ".tex"
        path = ROOT / rel
        if path.is_file() and path not in seen:
            seen.add(path)
            files.append(path)
    return files


def get_all_tex_files() -> list[Path]:
    """Scan chapters/, standalone/, appendices/ for all .tex files, plus main.tex."""
    dirs = [ROOT / "chapters", ROOT / "standalone", ROOT / "appendices"]
    files = []
    for d in dirs:
        if d.exists():
            files.extend(sorted(d.rglob("*.tex")))
    # Include main.tex itself (for \label{part:...} anchors)
    main = ROOT / "main.tex"
    if main.exists():
        files.append(main)
    return files


def find_env_end(lines: list[str], start_idx: int, env_name: str) -> int:
    end_token = f"\\end{{{env_name}}}"
    begin_token = f"\\begin{{{env_name}}}"
    depth = 1
    for i in range(start_idx + 1, len(lines)):
        if begin_token in lines[i]:
            depth += 1
        if end_token in lines[i]:
            depth -= 1
            if depth == 0:
                return i
    return len(lines) - 1


def extract_claims(path: Path) -> list[Claim]:
    rel_path = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    claims: list[Claim] = []

    i = 0
    while i < len(lines):
        line = lines[i]
        begin_match = BEGIN_RE.search(line)
        if not begin_match or begin_match.group(1) not in CLAIM_ENVS:
            i += 1
            continue

        env_name = begin_match.group(1)
        env_start = i
        env_end = find_env_end(lines, i, env_name)

        block_lines = lines[env_start:env_end + 1]
        block_text = "\n".join(block_lines)

        status_match = STATUS_RE.search(block_text)
        if not status_match:
            i = env_end + 1
            continue

        status = status_match.group(1)

        title = ""
        opt_match = BEGIN_OPT_RE.search(block_text[:500])
        if opt_match:
            raw_title = opt_match.group(2)
            raw_title = STATUS_RE.sub("", raw_title).strip()
            raw_title = raw_title.strip("; \t\n")
            title = raw_title

        block_labels = LABEL_RE.findall(block_text)

        block_refs = []
        for ref_match in REF_RE.finditer(block_text):
            for raw in ref_match.group(1).split(","):
                key = raw.strip()
                if key:
                    block_refs.append(key)

        block_cites = []
        for cite_match in CITE_RE.finditer(block_text):
            for raw in cite_match.group(1).split(","):
                key = raw.strip()
                if key:
                    block_cites.append(key)

        block_refs = list(dict.fromkeys(block_refs))
        block_cites = list(dict.fromkeys(block_cites))

        primary_label = block_labels[0] if block_labels else f"__unlabeled_{rel_path}:{env_start + 1}"

        label_line = env_start + 1
        for local_idx, local_line in enumerate(block_lines):
            if primary_label in local_line and "\\label{" in local_line:
                label_line = env_start + local_idx + 1
                break

        claim = Claim(
            label=primary_label,
            env_type=env_name,
            status=status,
            file=rel_path,
            line=label_line,
            title=title,
            labels_in_block=block_labels if len(block_labels) > 1 else [],
            refs_in_block=block_refs,
            cites_in_block=block_cites,
        )
        claims.append(claim)
        i = env_end + 1

    return claims


def extract_all_labels(path: Path) -> list[LabelEntry]:
    rel_path = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding="utf-8", errors="ignore")
    # NOTE: we do NOT strip comments here — we want to faithfully record every
    # \label{...} occurrence as it appears, so that a phantom-detector can
    # distinguish live labels from commented-out ones separately via env-scan.
    lines = text.splitlines()
    entries: list[LabelEntry] = []
    for i, line in enumerate(lines):
        # Skip lines that begin with % (pure comment lines)
        stripped = line.lstrip()
        if stripped.startswith("%"):
            continue
        for match in LABEL_RE.finditer(line):
            label = match.group(1)
            entries.append(LabelEntry(
                label=label,
                file=rel_path,
                line=i + 1,
            ))
    return entries


def classify_part(rel_path: str) -> tuple[Optional[str], Optional[str]]:
    for key, prefix, title in PART_SPECS:
        if rel_path.startswith(prefix):
            return key, title
    return None, None


def escape_md_cell(text: str) -> str:
    if not text:
        return "—"
    return " ".join(text.replace("|", "\\|").split())


def write_claims_jsonl(claims: list[Claim]) -> None:
    out_path = METADATA_DIR / "claims.jsonl"
    with open(out_path, "w", encoding="utf-8") as f:
        for claim in claims:
            f.write(json.dumps(claim.to_dict(), ensure_ascii=False) + "\n")
    print(f"  claims.jsonl: {len(claims)} claims")


def raw_grep_counts(all_files: list[Path]) -> dict[str, int]:
    counts: dict[str, int] = defaultdict(int)
    for path in all_files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in STATUS_RE.finditer(text):
            counts[match.group(1)] += 1
    return dict(counts)


def write_census_json(claims: list[Claim], all_files: list[Path]) -> None:
    status_counts: Counter[str] = Counter()
    for claim in claims:
        status_counts[claim.status] += 1

    grep_counts = raw_grep_counts(all_files)

    part_lines: dict[str, int] = {}
    for part_name, pattern, _ in PART_SPECS:
        total = 0
        for f in all_files:
            rel = f.relative_to(ROOT).as_posix()
            if rel.startswith(pattern):
                total += sum(1 for _ in open(f, encoding="utf-8", errors="ignore"))
        part_lines[part_name] = total
    total_lines = sum(part_lines.values())

    claims_by_part: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for claim in claims:
        part_name, _ = classify_part(claim.file)
        if part_name:
            claims_by_part[part_name][claim.status] += 1

    claims_by_file: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for claim in claims:
        claims_by_file[claim.file][claim.status] += 1

    census = {
        "date": date.today().isoformat(),
        "volume": ROOT.name,
        "totals": {
            "ProvedHere": status_counts.get("ProvedHere", 0),
            "ProvedElsewhere": status_counts.get("ProvedElsewhere", 0),
            "Conjectured": status_counts.get("Conjectured", 0),
            "Heuristic": status_counts.get("Heuristic", 0),
            "Conditional": status_counts.get("Conditional", 0),
            "Open": status_counts.get("Open", 0),
            "total_claims": len(claims),
        },
        "raw_grep_counts": {
            "_note": "Raw string occurrences (includes inline mentions).",
            "ProvedHere": grep_counts.get("ProvedHere", 0),
            "ProvedElsewhere": grep_counts.get("ProvedElsewhere", 0),
            "Conjectured": grep_counts.get("Conjectured", 0),
            "Heuristic": grep_counts.get("Heuristic", 0),
            "Conditional": grep_counts.get("Conditional", 0),
            "Open": grep_counts.get("Open", 0),
            "total_occurrences": sum(grep_counts.values()),
        },
        "lines": {
            "total": total_lines,
            **part_lines,
        },
        "by_part": {k: dict(v) for k, v in claims_by_part.items()},
        "by_file": {k: dict(v) for k, v in sorted(claims_by_file.items())},
    }

    out_path = METADATA_DIR / "census.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(census, f, indent=2, ensure_ascii=False)
    print(f"  census.json: PH={census['totals']['ProvedHere']} "
          f"PE={census['totals']['ProvedElsewhere']} "
          f"CJ={census['totals']['Conjectured']} "
          f"H={census['totals']['Heuristic']} "
          f"CD={census['totals']['Conditional']} "
          f"O={census['totals']['Open']} "
          f"total={census['totals']['total_claims']}")


def write_dependency_graph(claims: list[Claim], all_labels: dict[str, LabelEntry]) -> None:
    label_to_primary: dict[str, str] = {}
    for c in claims:
        label_to_primary[c.label] = c.label
        for lab in c.labels_in_block:
            label_to_primary[lab] = c.label

    out_path = METADATA_DIR / "dependency_graph.dot"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("digraph theorem_dependencies {\n")
        f.write("  rankdir=TB;\n")
        f.write("  node [shape=box, fontsize=9, fontname=\"Helvetica\"];\n")
        f.write("  edge [fontsize=7];\n\n")

        status_colors = {
            "ProvedHere": "#c8e6c9",
            "ProvedElsewhere": "#bbdefb",
            "Conjectured": "#fff9c4",
            "Heuristic": "#ffccbc",
            "Conditional": "#e1bee7",
            "Open": "#ef9a9a",
        }

        for claim in claims:
            color = status_colors.get(claim.status, "#ffffff")
            safe_label = claim.label.replace(":", "_").replace("-", "_").replace(".", "_")
            short_title = claim.title[:40] + "..." if len(claim.title) > 40 else claim.title
            display = f"{claim.label}\\n{claim.env_type} [{claim.status[:2]}]"
            if short_title:
                display += f"\\n{short_title}"
            f.write(f'  {safe_label} [label="{display}", style=filled, fillcolor="{color}"];\n')

        f.write("\n")
        for claim in claims:
            src = claim.label.replace(":", "_").replace("-", "_").replace(".", "_")
            for ref in claim.refs_in_block:
                primary = label_to_primary.get(ref)
                if primary and primary != claim.label:
                    dst = primary.replace(":", "_").replace("-", "_").replace(".", "_")
                    f.write(f"  {src} -> {dst};\n")
        f.write("}\n")

    edge_count = sum(
        1 for c in claims
        for r in c.refs_in_block
        if label_to_primary.get(r) and label_to_primary.get(r) != c.label
    )
    print(f"  dependency_graph.dot: {len(claims)} nodes, {edge_count} edges")


def write_label_index(all_labels: dict[str, LabelEntry]) -> None:
    index = {}
    for label, entry in sorted(all_labels.items()):
        index[label] = {
            "file": entry.file,
            "line": entry.line,
        }
        if entry.env_type:
            index[label]["env_type"] = entry.env_type

    out_path = METADATA_DIR / "label_index.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    print(f"  label_index.json: {len(index)} labels")


def write_theorem_registry(
    claims: list[Claim],
    active_files: list[Path],
    all_tex_files: list[Path],
) -> None:
    proved_claims = [c for c in claims if c.status == "ProvedHere"]
    status_counts = Counter(c.status for c in claims)
    env_counts = Counter(c.env_type for c in proved_claims)
    part_counts = Counter()
    file_counts = Counter()

    for c in proved_claims:
        part_name, _ = classify_part(c.file)
        if part_name:
            part_counts[part_name] += 1
        file_counts[c.file] += 1

    lines: list[str] = []
    lines.append(f"# Theorem Registry ({ROOT.name})")
    lines.append("")
    lines.append(f"Auto-generated {date.today().isoformat()}.")
    lines.append("")
    lines.append("## Snapshot")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|---|---:|")
    lines.append(f"| ProvedHere claims | {len(proved_claims)} |")
    lines.append(f"| Total tagged claims | {len(claims)} |")
    lines.append(f"| Active files in `main.tex` | {len(active_files)} |")
    lines.append(f"| Total `.tex` files scanned | {len(all_tex_files)} |")
    lines.append("")
    lines.append("## Status Totals")
    lines.append("")
    lines.append("| Status | Count |")
    lines.append("|---|---:|")
    for status in ["ProvedHere", "ProvedElsewhere", "Conjectured", "Conditional", "Heuristic", "Open"]:
        lines.append(f"| `{status}` | {status_counts.get(status, 0)} |")
    lines.append("")
    lines.append("## ProvedHere By Environment")
    lines.append("")
    lines.append("| Environment | Count |")
    lines.append("|---|---:|")
    for env_type, count in sorted(env_counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"| `{env_type}` | {count} |")
    lines.append("")
    lines.append("## ProvedHere By Part")
    lines.append("")
    lines.append("| Part | Count |")
    lines.append("|---|---:|")
    for part_key, _, title in PART_SPECS:
        lines.append(f"| {title} | {part_counts.get(part_key, 0)} |")

    out_path = METADATA_DIR / "theorem_registry.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"  theorem_registry.md: {len(proved_claims)} proved claims indexed")


def main() -> None:
    print(f"Generating metadata for {ROOT.name}...")
    print(f"  Root: {ROOT}")
    METADATA_DIR.mkdir(exist_ok=True)

    active_files = get_active_files()
    all_tex_files = get_all_tex_files()
    print(f"  Active files (in main.tex): {len(active_files)}")
    print(f"  All .tex files: {len(all_tex_files)}")

    all_claims: list[Claim] = []
    for path in all_tex_files:
        all_claims.extend(extract_claims(path))

    all_labels: dict[str, LabelEntry] = {}
    for path in all_tex_files:
        for entry in extract_all_labels(path):
            if entry.label not in all_labels:
                all_labels[entry.label] = entry

    print(f"\n  Extracted {len(all_claims)} tagged claims from {len(all_tex_files)} files")
    print(f"\nWriting metadata to {METADATA_DIR}/")
    write_claims_jsonl(all_claims)
    write_census_json(all_claims, all_tex_files)
    write_dependency_graph(all_claims, all_labels)
    write_label_index(all_labels)
    write_theorem_registry(all_claims, active_files, all_tex_files)
    print(f"\nDone.")


if __name__ == "__main__":
    main()
