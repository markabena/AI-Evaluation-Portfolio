"""Run the three-stage CV -> platform matching -> report chain.

Usage:
    python run_chain.py path/to/cv.txt --out report.md
    python run_chain.py path/to/cv.txt --dry-run      # print the stage-1 prompt, no API call

Requires ANTHROPIC_API_KEY in the environment. Set CHAIN_MODEL to choose a model.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).parent
PROMPTS = HERE / "prompts"
CONFIG = HERE / "config"

DEFAULT_MODEL = os.environ.get("CHAIN_MODEL", "claude-sonnet-4-5")
MAX_RETRIES = 2


def fill(template: str, **values: str) -> str:
    """Replace {name} placeholders without touching other braces (the prompts contain JSON)."""
    for key, value in values.items():
        template = template.replace("{" + key + "}", value)
    return template


def load_prompt(name: str) -> str:
    return (PROMPTS / name).read_text(encoding="utf-8")


def parse_json(text: str) -> dict:
    """Parse a JSON object from a model reply, tolerating code fences or stray text."""
    text = text.strip()
    fenced = re.search(r"```(?:json)?\s*(\{.*\})\s*```", text, re.DOTALL)
    if fenced:
        text = fenced.group(1)
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError("No JSON object found in model reply.")
    return json.loads(text[start : end + 1])


def validate_profile(profile: dict, schema: dict) -> None:
    try:
        import jsonschema
    except ImportError:
        missing = [k for k in schema.get("required", []) if k not in profile]
        if missing:
            raise ValueError(f"Profile missing required fields: {missing}")
        return
    jsonschema.validate(profile, schema)


class Chain:
    def __init__(self, client, model: str = DEFAULT_MODEL):
        self.client = client
        self.model = model

    def ask(self, prompt: str, max_tokens: int = 2000) -> str:
        reply = self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt}],
        )
        return "".join(block.text for block in reply.content if getattr(block, "type", "") == "text")

    def ask_json(self, prompt: str) -> dict:
        last_error = None
        for _ in range(MAX_RETRIES + 1):
            try:
                return parse_json(self.ask(prompt))
            except (ValueError, json.JSONDecodeError) as err:
                last_error = err
                prompt += "\n\nYour last reply was not valid JSON. Return only the JSON object."
        raise RuntimeError(f"Model did not return valid JSON: {last_error}")

    def extract_profile(self, cv_text: str, schema: dict) -> dict:
        prompt = fill(load_prompt("01_extract_profile.md"), cv_text=cv_text, schema=json.dumps(schema, indent=2))
        profile = self.ask_json(prompt)
        validate_profile(profile, schema)
        return profile

    def match(self, profile: dict, catalogue: dict) -> dict:
        prompt = fill(
            load_prompt("02_match_platforms.md"),
            profile_json=json.dumps(profile, indent=2),
            catalogue_yaml=yaml.safe_dump(catalogue, sort_keys=False),
        )
        result = self.ask_json(prompt)
        known = {p["name"] for p in catalogue["platforms"]}
        result["matches"] = [m for m in result.get("matches", []) if m.get("platform") in known]
        if not any(m["fit"] in ("strong", "possible") for m in result["matches"]):
            raise RuntimeError("Matching returned no usable options; check the profile and catalogue.")
        return result

    def report(self, profile: dict, matches: dict) -> str:
        prompt = fill(
            load_prompt("03_write_report.md"),
            profile_json=json.dumps(profile, indent=2),
            matches_json=json.dumps(matches, indent=2),
        )
        return self.ask(prompt, max_tokens=3000)

    def run(self, cv_text: str) -> dict:
        schema = json.loads((CONFIG / "candidate_profile.schema.json").read_text(encoding="utf-8"))
        catalogue = yaml.safe_load((CONFIG / "platforms.yaml").read_text(encoding="utf-8"))
        profile = self.extract_profile(cv_text, schema)
        matches = self.match(profile, catalogue)
        return {"profile": profile, "matches": matches, "report": self.report(profile, matches)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("cv", type=Path, help="Plain-text or Markdown CV")
    parser.add_argument("--out", type=Path, default=Path("report.md"))
    parser.add_argument("--save-intermediate", action="store_true", help="Also write profile.json and matches.json")
    parser.add_argument("--dry-run", action="store_true", help="Print the stage-1 prompt and exit")
    args = parser.parse_args(argv)

    cv_text = args.cv.read_text(encoding="utf-8")

    if args.dry_run:
        schema = (CONFIG / "candidate_profile.schema.json").read_text(encoding="utf-8")
        print(fill(load_prompt("01_extract_profile.md"), cv_text=cv_text, schema=schema))
        return 0

    try:
        import anthropic
    except ImportError:
        print("Install dependencies first: pip install -r requirements.txt", file=sys.stderr)
        return 1

    result = Chain(anthropic.Anthropic()).run(cv_text)
    args.out.write_text(result["report"], encoding="utf-8")
    if args.save_intermediate:
        args.out.with_name("profile.json").write_text(json.dumps(result["profile"], indent=2), encoding="utf-8")
        args.out.with_name("matches.json").write_text(json.dumps(result["matches"], indent=2), encoding="utf-8")
    print(f"Report written to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
