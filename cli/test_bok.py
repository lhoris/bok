"""Test suite for the `bok` CLI — stdlib unittest, no external deps.

Run:  python cli/test_bok.py        (or: python -m unittest -v cli.test_bok)

BOK preaches "verify, don't trust prior output" — so the tool that enforces
that gets the same treatment. Each test builds a throwaway project in a temp
dir and drives it through bok.main(argv), asserting exit codes and the files
the pipeline produces.
"""
import io
import pathlib
import sys
import tempfile
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import bok  # noqa: E402

BOK_YAML = """\
bok_version: "0.1.0"
project: t
staleness: {reference_days: 90, explanation_days: 180, glossary_days: 180}
confidence: {cross_support_requires_distinct_kinds: true}
readiness:
  criticality_weights: {critical: 4, high: 3, normal: 2, low: 1}
  required_confidence: {critical: verified, high: corroborated, normal: inferred}
  tier_thresholds: {R3_score: 80}
  purpose_to_tier: {understand: R2, feature: R3, modernization: R4}
adversarial: {max_rounds: 3}
packs: [{source: core}]
coverage_template: arc42+tdd
"""


def run(*argv):
    """Invoke the CLI, return (exit_code, stdout)."""
    buf = io.StringIO()
    with redirect_stdout(buf):
        try:
            code = bok.main(list(argv))
        except SystemExit as e:
            code = e.code
    return code, buf.getvalue()


class BokTest(unittest.TestCase):
    def setUp(self):
        self.dir = pathlib.Path(tempfile.mkdtemp())
        (self.dir / "bok.yaml").write_text(BOK_YAML, encoding="utf-8")
        self.ctx = self.dir / "bok" / "shop"
        (self.dir / "bok" / "_system").mkdir(parents=True)

    def ku(self, kind, slug, confidence="inferred", provenance=None, relations="[]",
           layer="component", status="active"):
        prov = provenance if provenance is not None else "[{kind: code, locator: src/a.py}]"
        d = self.ctx / kind
        d.mkdir(parents=True, exist_ok=True)
        (d / f"{slug}.md").write_text(
            f"---\nid: bok://shop/{kind}/{slug}\ntitle: {slug}\nkind: {kind}\n"
            f"layer: {layer}\ncontext: shop\nstatus: {status}\nconfidence: {confidence}\n"
            f"provenance: {prov}\nrelations: {relations}\n---\n\n## TL;DR\n{slug} 요약.\n",
            encoding="utf-8",
        )
        return f"bok://shop/{kind}/{slug}"

    def src(self, relpath, text="x=1\n"):
        p = self.dir / relpath
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")

    def coverage(self, body):
        (self.dir / "bok" / "_system" / "coverage.yaml").write_text(body, encoding="utf-8")

    # ---- schema / compile -------------------------------------------------
    def test_schema_rejects_ku_missing_required_field(self):
        d = self.ctx / "reference"; d.mkdir(parents=True)
        (d / "bad.md").write_text("---\ntitle: no id\nkind: reference\n---\nx\n", encoding="utf-8")
        code, out = run("compile", str(self.dir))
        self.assertEqual(code, 1)
        self.assertIn("missing required field 'id'", out)

    def test_compile_detects_dangling_relation(self):
        self.ku("reference", "a", relations="[{type: depends-on, target: bok://shop/reference/ghost}]")
        code, out = run("compile", str(self.dir))
        self.assertEqual(code, 0)
        self.assertIn("dangling", out)
        cat = (self.dir / "bok/_system/catalog.yaml").read_text(encoding="utf-8")
        self.assertIn("ghost", cat)

    # ---- validate: confidence transitions ---------------------------------
    def test_cross_support_promotes_inferred_to_corroborated(self):
        self.src("src/a.py")
        self.ku("reference", "a", confidence="inferred",
                provenance="[{kind: code, locator: src/a.py}, {kind: human, locator: interview/x}]")
        code, _ = run("validate", str(self.dir), "--scope", "shop")
        self.assertEqual(code, 0)
        txt = (self.ctx / "reference/a.md").read_text(encoding="utf-8")
        self.assertIn("confidence:    corroborated", txt)

    def test_same_kind_provenance_does_not_promote(self):
        self.src("src/a.py"); self.src("src/b.py")
        self.ku("reference", "a", confidence="inferred",
                provenance="[{kind: code, locator: src/a.py}, {kind: code, locator: src/b.py}]")
        run("validate", str(self.dir), "--scope", "shop")
        txt = (self.ctx / "reference/a.md").read_text(encoding="utf-8")
        self.assertIn("confidence: inferred", txt)  # still single-perspective

    def test_grounding_failure_demotes_and_exits_2(self):
        self.ku("reference", "a", confidence="corroborated",
                provenance="[{kind: code, locator: src/missing.py}]")
        code, out = run("validate", str(self.dir), "--scope", "shop")
        self.assertEqual(code, 2)
        self.assertIn("GROUNDING FAIL", out)
        self.assertIn("confidence:    unverified", (self.ctx / "reference/a.md").read_text(encoding="utf-8"))

    def test_signoff_requires_corroborated_then_verifies(self):
        self.src("src/a.py")
        kid = self.ku("explanation", "a", confidence="inferred",
                      provenance="[{kind: code, locator: src/a.py}]")
        code, _ = run("validate", str(self.dir), "--sign", kid, "--owner", "kim")
        self.assertEqual(code, 2)  # refused: below corroborated
        # promote to corroborated, then sign succeeds
        (self.ctx / "explanation/a.md").write_text(
            (self.ctx / "explanation/a.md").read_text(encoding="utf-8").replace(
                "confidence: inferred", "confidence: corroborated"), encoding="utf-8")
        code, _ = run("validate", str(self.dir), "--sign", kid, "--owner", "kim")
        self.assertEqual(code, 0)
        self.assertIn("confidence:    verified", (self.ctx / "explanation/a.md").read_text(encoding="utf-8"))

    # ---- ready: hard gate + tiers -----------------------------------------
    def test_ready_hard_gate_blocks_on_critical_red(self):
        self.ku("reference", "a", confidence="authoritative", layer="component")
        self.coverage(
            "scope: shop\nareas:\n"
            "  - {id: building-blocks, criticality: high, kus: [bok://shop/reference/a]}\n"
            "  - {id: data-model, criticality: critical, kus: []}\n")  # empty critical -> red
        code, out = run("ready", str(self.dir), "--scope", "shop", "--purpose", "feature")
        self.assertEqual(code, 2)
        self.assertIn("NOT READY", out)
        self.assertIn("FAIL", out)

    def test_ready_all_green_is_ready(self):
        ids = []
        for area, crit in [("context-and-scope", "high"), ("data-model", "critical"),
                           ("business-rules", "critical"), ("decisions-rationale", "high")]:
            ids.append(self.ku("reference", area.replace("-", ""), confidence="authoritative"))
        lines = "\n".join(
            f"  - {{id: {a}, criticality: {c}, kus: [bok://shop/reference/{a.replace('-','')}]}}"
            for a, c in [("context-and-scope", "high"), ("data-model", "critical"),
                         ("business-rules", "critical"), ("decisions-rationale", "high")])
        self.coverage(f"scope: shop\nareas:\n{lines}\n")
        code, out = run("ready", str(self.dir), "--scope", "shop", "--purpose", "feature")
        self.assertEqual(code, 0)
        self.assertIn("READY", out)
        self.assertNotIn("NOT READY", out)

    # ---- onboard: one-command pipeline ------------------------------------
    def test_onboard_runs_full_pipeline(self):
        # fresh project (no bok.yaml yet) with a tiny source tree
        proj = pathlib.Path(tempfile.mkdtemp())
        (proj / "src" / "app").mkdir(parents=True)
        (proj / "src" / "app" / "m.py").write_text("x=1\n", encoding="utf-8")
        code, out = run("onboard", str(proj), "--scope", "app", "--source", "src")
        self.assertIn("init", out)
        self.assertIn("discovered", out)
        self.assertIn("VERDICT", out)
        self.assertTrue((proj / "bok.yaml").exists())
        self.assertTrue((proj / "bok/_system/readiness-report.md").exists())
        self.assertTrue(any((proj / "bok/app/reference").glob("pkg-*.md")))

    # ---- context: area mapping --------------------------------------------
    def test_context_maps_ku_to_area_by_layer(self):
        self.ku("reference", "tbl", layer="data")
        code, out = run("context", str(self.dir), "--scope", "shop")
        self.assertEqual(code, 0)
        cov = (self.dir / "bok/_system/coverage.yaml").read_text(encoding="utf-8")
        self.assertIn("data-model", cov)
        self.assertIn("bok://shop/reference/tbl", cov)

    # ---- assemble: gaps ---------------------------------------------------
    def test_assemble_reports_gaps(self):
        self.ku("reference", "a", relations="[{type: depends-on, target: bok://shop/reference/ghost}]")
        self.coverage("scope: shop\nareas:\n  - {id: data-model, criticality: critical, kus: []}\n")
        code, out = run("assemble", str(self.dir), "--scope", "shop", "--goal", "a 요약")
        self.assertEqual(code, 0)
        pack = (self.dir / "bok/_system/context-pack.yaml").read_text(encoding="utf-8")
        self.assertIn("ghost", pack)       # dangling gap
        self.assertIn("data-model", pack)  # coverage gap

    # ---- discover: mining -------------------------------------------------
    def test_discover_mines_packages_and_tables(self):
        self.src("src/orders/svc.py", "from payments.gw import G\n")
        self.src("src/payments/gw.py", "class G: pass\n")
        self.src("db/schema.sql", "CREATE TABLE orders (id BIGINT PRIMARY KEY);\n")
        code, out = run("discover", str(self.dir), "--scope", "shop", "--source", "src")
        self.assertEqual(code, 0)
        self.assertTrue((self.ctx / "reference/pkg-orders.md").exists())
        self.assertTrue((self.ctx / "reference/pkg-payments.md").exists())
        self.assertTrue((self.ctx / "reference/table-orders.md").exists())
        # discovered KU carries a depends-on relation from the import
        self.assertIn("pkg-payments", (self.ctx / "reference/pkg-orders.md").read_text(encoding="utf-8"))
        # all discovered KUs are inferred drafts
        code, _ = run("compile", str(self.dir))
        self.assertEqual(code, 0)

    def test_discover_is_idempotent(self):
        self.src("src/orders/svc.py")
        run("discover", str(self.dir), "--scope", "shop", "--source", "src")
        code, out = run("discover", str(self.dir), "--scope", "shop", "--source", "src")
        self.assertIn("0 candidate", out)  # nothing new; existing ids skipped

    # ---- unit: pure helpers -----------------------------------------------
    def test_confidence_ordering(self):
        self.assertLess(bok.conf_index("inferred"), bok.conf_index("verified"))
        self.assertEqual(bok.conf_index("authoritative"), 4)
        self.assertEqual(bok.conf_index("bogus"), -1)

    def test_compute_status_rules(self):
        cfg = {"readiness": {"required_confidence": {"critical": "verified", "high": "corroborated", "normal": "inferred"}}}
        self.assertEqual(bok.compute_status("critical", [], cfg), "red")            # missing
        self.assertEqual(bok.compute_status("critical", ["inferred"], cfg), "red")  # 2 levels short
        self.assertEqual(bok.compute_status("high", ["inferred"], cfg), "amber")    # 1 level short
        self.assertEqual(bok.compute_status("normal", ["inferred"], cfg), "green")
        self.assertEqual(bok.compute_status("normal", ["authoritative"], cfg, open_gap=True), "amber")


class RepoFrontmatterTest(unittest.TestCase):
    """Every shipped agent/skill/adapter markdown must have parseable
    frontmatter with a name/description — guards the docs (this catches the
    YAML-quoting bugs found during authoring)."""

    ROOT = pathlib.Path(__file__).resolve().parent.parent

    def _check(self, glob, need_name=True):
        import yaml
        files = list(self.ROOT.glob(glob))
        self.assertTrue(files, f"no files matched {glob}")
        for f in files:
            parts = f.read_text(encoding="utf-8").split("---", 2)
            self.assertGreaterEqual(len(parts), 3, f"{f}: no frontmatter")
            fm = yaml.safe_load(parts[1])
            self.assertTrue(fm.get("description"), f"{f}: missing description")
            if need_name:
                self.assertTrue(fm.get("name"), f"{f}: missing name")

    def test_core_skills(self):
        self._check("packs/core/**/SKILL.md")

    def test_framework_agents(self):
        self._check("agents/bok-*.md")

    def test_adapter_agents(self):
        self._check("adapters/claude-code/agents/*.md")

    def test_adapter_commands(self):
        self._check("adapters/claude-code/commands/*.md", need_name=False)

    def test_codex_prompts(self):
        self._check("adapters/codex/prompts/*.md", need_name=False)

    def test_copilot_prompts(self):
        self._check("adapters/github-copilot/prompts/*.prompt.md", need_name=False)


if __name__ == "__main__":
    unittest.main(verbosity=2)
