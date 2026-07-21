#!/usr/bin/env python3
"""bok — Body of Knowledge CLI (Walking Skeleton, ROADMAP M1).

Vendor-neutral, dependency-light (stdlib + pyyaml). Implements the two
commands needed to regenerate examples/acme-billing by tooling rather than
by hand:

    bok compile   design/05 D20 — read authored KUs -> catalog.yaml + graph.json
                  + schema check + dangling-relation detection (D21).
    bok ready     design/04 B.3/B.4 — coverage -> traffic lights -> hard gate
                  -> score -> Readiness Tier, purpose-relative (D17/D18).

Everything else (discover/context/validate) is later milestones.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys

import yaml

# ---------------------------------------------------------------- model

CONFIDENCE_ORDER = ["unverified", "inferred", "corroborated", "verified", "authoritative"]
TIER_RANK = {"R0": 0, "R1": 1, "R2": 2, "R3": 3, "R4": 4}
KINDS = {"reference", "explanation", "how-to", "tutorial", "glossary"}
REQUIRED_FIELDS = ["id", "title", "kind", "context", "status", "confidence", "provenance"]


def conf_index(name: str) -> int:
    try:
        return CONFIDENCE_ORDER.index(name)
    except ValueError:
        return -1


class KU:
    def __init__(self, path: pathlib.Path, meta: dict):
        self.path = path
        self.meta = meta

    @property
    def id(self) -> str:
        return self.meta.get("id", "")

    def relations(self) -> list[tuple[str, str]]:
        out = []
        for r in self.meta.get("relations") or []:
            if isinstance(r, dict) and "type" in r and "target" in r:
                out.append((r["type"], r["target"]))
        return out


# ---------------------------------------------------------------- parsing

def parse_ku(path: pathlib.Path) -> tuple[KU | None, list[str]]:
    """Parse frontmatter (YAML between leading ---) + return schema errors."""
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    if not text.startswith("---"):
        return None, [f"{path}: missing frontmatter"]
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, [f"{path}: malformed frontmatter"]
    try:
        meta = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as e:
        return None, [f"{path}: YAML error: {e}"]

    for f in REQUIRED_FIELDS:
        if f not in meta or meta[f] in (None, "", []):
            errors.append(f"{path}: missing required field '{f}'")
    if meta.get("kind") not in KINDS:
        errors.append(f"{path}: invalid kind '{meta.get('kind')}'")
    if conf_index(meta.get("confidence", "")) < 0:
        errors.append(f"{path}: invalid confidence '{meta.get('confidence')}'")
    prov = meta.get("provenance") or []
    if not prov:
        errors.append(f"{path}: provenance required (>=1) — no evidence, no knowledge")
    return KU(path, meta), errors


def load_project(root: pathlib.Path) -> tuple[dict, list[KU], list[str]]:
    cfg_path = root / "bok.yaml"
    if not cfg_path.exists():
        sys.exit(f"error: no bok.yaml at {root}")
    cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}
    bok_dir = root / "bok"
    kus: list[KU] = []
    errors: list[str] = []
    for md in sorted(bok_dir.rglob("*.md")):
        if "_system" in md.parts:
            continue
        ku, errs = parse_ku(md)
        errors.extend(errs)
        if ku:
            kus.append(ku)
    return cfg, kus, errors


# ---------------------------------------------------------------- compile

def cmd_compile(root: pathlib.Path) -> int:
    cfg, kus, errors = load_project(root)
    if errors:
        print("SCHEMA ERRORS:")
        for e in errors:
            print("  -", e)
        # schema errors are fatal for compile (design/05 §8 pre-commit gate)
        return 1

    ids = {k.id for k in kus}
    # graph + dangling detection (D21)
    edges = []
    dangling = []
    for k in kus:
        for rtype, target in k.relations():
            edges.append({"from": k.id, "type": rtype, "to": target})
            if target not in ids:
                dangling.append((k.id, rtype, target))

    catalog = {
        "generated_by": "bok compile",
        "note": "GENERATED — do not edit by hand (design/05 D20)",
        "units": [
            {
                "id": k.id,
                "title": k.meta.get("title"),
                "kind": k.meta.get("kind"),
                "layer": k.meta.get("layer"),
                "context": k.meta.get("context"),
                "confidence": k.meta.get("confidence"),
                "relations": [f"{t}:{tgt}" for t, tgt in k.relations()],
            }
            for k in kus
        ],
        "warnings": [
            f"dangling relation: {tgt} referenced by {src} ({rt}) but not authored"
            for src, rt, tgt in dangling
        ],
    }

    sysdir = root / "bok" / "_system"
    sysdir.mkdir(parents=True, exist_ok=True)
    (sysdir / "catalog.yaml").write_text(
        "# GENERATED by `bok compile` — do not edit by hand (design/05 D20)\n"
        + yaml.safe_dump(catalog, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
    (sysdir / "graph.json").write_text(
        json.dumps({"nodes": sorted(ids), "edges": edges}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"compiled {len(kus)} KUs, {len(edges)} relations -> bok/_system/")
    if dangling:
        print(f"WARNING: {len(dangling)} dangling relation(s):")
        for src, rt, tgt in dangling:
            print(f"  - {tgt}  <- {src} ({rt})")
    return 0


# ---------------------------------------------------------------- ready

def compute_status(criticality: str, ku_confidences: list[str], cfg: dict, open_gap: bool = False) -> str:
    """design/04 B.3 — status from required-confidence of present KUs.

    `open_gap` = authored "known incomplete/unresolved" flag: even when present
    KUs meet confidence, a declared open gap caps the area at amber (B.3:
    "미해소 gap/contradicts 존재 → amber"). This models completeness that pure
    confidence-of-present-KUs cannot (M1 finding, see cli/README.md).
    """
    req_map = cfg.get("readiness", {}).get("required_confidence", {})
    required = conf_index(req_map.get(criticality, "inferred"))
    if not ku_confidences:
        return "red"  # no KU -> gap
    min_conf = min(conf_index(c) for c in ku_confidences)
    gap = required - min_conf
    if gap >= 2:
        return "red"
    if gap == 1:
        return "amber"
    return "amber" if open_gap else "green"


def compute_tier(areas: dict[str, str], hard_pass: bool, score: float, cfg: dict) -> str:
    """design/04 B.4 step 3 (M1 approximation)."""
    def g(name):
        return areas.get(name) == "green"
    structural = g("context-and-scope") and g("data-model")
    understood = structural and g("business-rules") and g("decisions-rationale")
    r3 = hard_pass and score >= cfg.get("readiness", {}).get("tier_thresholds", {}).get("R3_score", 80)
    r4 = r3 and g("risks-tech-debt") and g("dependencies-eol") and g("team-bus-factor")
    if r4:
        return "R4 (Modernization-Ready)"
    if r3:
        return "R3 (Development-Ready)"
    if understood:
        return "R2 (Understood)"
    if structural:
        return "R1 (Mapped)"
    return "R0 (below Mapped)"


def cmd_ready(root: pathlib.Path, scope: str, purpose: str) -> int:
    cfg, kus, errors = load_project(root)
    if errors:
        print("SCHEMA ERRORS (fix before ready):")
        for e in errors:
            print("  -", e)
        return 1
    conf_by_id = {k.id: k.meta.get("confidence") for k in kus}

    cov_path = root / "bok" / "_system" / "coverage.yaml"
    if not cov_path.exists():
        sys.exit("error: bok/_system/coverage.yaml not found (run context/authoring first)")
    cov = yaml.safe_load(cov_path.read_text(encoding="utf-8")) or {}

    weights = cfg.get("readiness", {}).get("criticality_weights", {})
    status_val = {"green": 1.0, "amber": 0.5, "red": 0.0}

    rows = []
    area_status: dict[str, str] = {}
    num = den = 0.0
    for area in cov.get("areas", []):
        aid = area["id"]
        crit = area.get("criticality", "normal")
        kids = area.get("kus", []) or []
        confs = [conf_by_id[i] for i in kids if i in conf_by_id]
        st = compute_status(crit, confs, cfg, open_gap=bool(area.get("open_gap")))
        area_status[aid] = st
        w = weights.get(crit, 1)
        num += w * status_val[st]
        den += w
        rows.append((aid, crit, st))

    score = round((num / den) * 100) if den else 0

    # Hard gate (D18): any critical area red -> NOT READY
    critical_reds = [a for a, c, s in rows if c == "critical" and s == "red"]
    hard_pass = not critical_reds

    tier = compute_tier(area_status, hard_pass, score, cfg)
    target = cfg.get("readiness", {}).get("purpose_to_tier", {}).get(purpose, "R3")

    gaps = [a for a, c, s in rows if s in ("red", "amber")]
    # tier meets OR exceeds the purpose's target tier (R4 satisfies an R3 target)
    tier_ok = TIER_RANK.get(tier.split()[0], 0) >= TIER_RANK.get(target.split()[0], 3)
    verdict = "READY" if (hard_pass and tier_ok) else "NOT READY"

    # write report
    lines = [
        f"<!-- GENERATED by `bok ready --scope {scope} --purpose {purpose}` -->",
        f"# Readiness Report — {scope} (purpose: {purpose} -> 목표 {target})",
        "",
        "## 1. Hard Gate (design/04 B.4)",
        f"**{'PASS' if hard_pass else 'FAIL'}**"
        + ("" if hard_pass else f" — critical red: {', '.join(critical_reds)}"),
        "",
        "## 2. Coverage",
        "| area | criticality | status |",
        "|------|:-:|:-:|",
    ]
    icon = {"green": "green", "amber": "amber", "red": "red"}
    for a, c, s in rows:
        lines.append(f"| {a} | {c} | {icon[s]} |")
    lines += [
        "",
        f"## 3. Score\n{score} / 100",
        f"\n## 4. Tier\n**{tier}** (목표 {target})",
        "\n## 5. Gaps (→ 다음 discover, design/02 D8)",
    ]
    lines += [f"- {gp}" for gp in gaps] or ["- (none)"]
    lines += [f"\n## 6. Verdict\n> **{verdict} ({purpose}).**"]
    report = "\n".join(lines) + "\n"
    (root / "bok" / "_system" / "readiness-report.md").write_text(report, encoding="utf-8")

    # console summary
    print(f"scope={scope} purpose={purpose} target={target}")
    for a, c, s in rows:
        print(f"  [{s:>5}] {a} ({c})")
    print(f"hard_gate={'PASS' if hard_pass else 'FAIL'} score={score} tier={tier}")
    print(f"VERDICT: {verdict}")
    return 0 if verdict == "READY" else 2


# ---------------------------------------------------------------- cli

def main(argv=None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")  # Windows consoles default to cp949
        except Exception:
            pass
    p = argparse.ArgumentParser(prog="bok", description="Body of Knowledge CLI (M1)")
    sub = p.add_subparsers(dest="cmd", required=True)
    pc = sub.add_parser("compile", help="compile catalog/graph + schema/dangling check")
    pc.add_argument("path", nargs="?", default=".")
    pr = sub.add_parser("ready", help="evaluate Development Readiness")
    pr.add_argument("path", nargs="?", default=".")
    pr.add_argument("--scope", required=True)
    pr.add_argument("--purpose", default="feature")
    args = p.parse_args(argv)

    root = pathlib.Path(args.path).resolve()
    if args.cmd == "compile":
        return cmd_compile(root)
    if args.cmd == "ready":
        return cmd_ready(root, args.scope, args.purpose)
    return 1


if __name__ == "__main__":
    sys.exit(main())
