#!/usr/bin/env python3
"""Mark 4 caption evaluation: transparent deterministic checks on reviewed cases.
Usage: python eval_suite.py cases.json
Cases must include source_facts, forbidden_claims, required_terms, and caption.
This is a screening rubric, NOT an LLM quality or legal-compliance certification.
"""
import json, re, sys
from pathlib import Path

def norm(s):
    return re.sub(r"\s+", " ", s.lower()).strip()

def score_case(case):
    caption = case.get("caption", "")
    lower = norm(caption)
    checks = {}
    checks["nonempty"] = bool(caption.strip())
    checks["no_em_dash"] = "—" not in caption
    checks["no_forbidden_claims"] = not any(norm(x) in lower for x in case.get("forbidden_claims", []))
    checks["required_terms"] = all(norm(x) in lower for x in case.get("required_terms", []))
    checks["max_length"] = len(caption) <= case.get("max_chars", 2200)
    checks["no_excessive_hashtags"] = len(re.findall(r"(?<!\w)#\w+", caption)) <= case.get("max_hashtags", 5)
    checks["no_excessive_emojis"] = sum(ord(c) > 0x1F000 for c in caption) <= case.get("max_emojis", 2)
    checks["no_unapproved_urls"] = all(u in case.get("approved_urls", []) for u in re.findall(r"https?://[^\s]+", caption))
    # Source facts are available to human reviewers; this script does NOT establish
    # semantic factual fidelity or detect every hallucination.
    return checks

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python eval_suite.py cases.json")
    cases = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    if not isinstance(cases, list) or not cases:
        raise SystemExit("Provide a nonempty JSON list of caption test cases")
    rows = []
    for case in cases:
        checks = score_case(case)
        rows.append({"id": case.get("id", "unnamed"), "checks": checks,
                     "passed": sum(checks.values()), "total": len(checks)})
    passed = sum(r["passed"] for r in rows)
    total = sum(r["total"] for r in rows)
    print(json.dumps({"screening_score_percent": round(100 * passed / total, 2),
                      "passed": passed, "total": total, "cases": rows}, indent=2))
    print("NOTE: This is only a mechanical screening score. Independent human review "
          "of factual fidelity, jurisdictional advertising, voice and usefulness is required.",
          file=sys.stderr)
    return 0 if passed == total else 1

if __name__ == "__main__":
    sys.exit(main())
