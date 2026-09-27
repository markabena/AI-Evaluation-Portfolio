"""Offline tests for run_chain.py using a fake client (no API key needed).

Run with: python -m pytest test_chain.py
"""

import json
from types import SimpleNamespace

from run_chain import Chain, fill, parse_json

PROFILE = {
    "name": "Adaeze Okonkwo",
    "location": {"city": "Lagos", "country": "Nigeria"},
    "highest_degree": {"level": "bachelors", "field": "Economics", "institution": "University of Lagos", "year": 2023},
    "domains": [{"domain": "finance", "evidence": "Junior Credit Analyst since Jan 2024"}],
    "languages": [{"language": "English", "proficiency": "fluent"}],
    "technical_skills": ["Excel", "Stata", "Python"],
    "writing_evidence": ["Co-wrote a 30-page project report"],
    "years_experience": 2.5,
    "red_flags": [],
}

MATCHES = {
    "matches": [
        {"platform": "Outlier", "tier": "core", "fit": "strong", "evidence": ["x"], "unknowns": [], "suggested_roles": ["finance specialist"]},
        {"platform": "Made Up Platform", "tier": "core", "fit": "strong", "evidence": [], "unknowns": [], "suggested_roles": []},
    ],
    "cv_improvements": [],
}


class FakeClient:
    def __init__(self, replies):
        self.replies = list(replies)
        self.prompts = []
        self.messages = self

    def create(self, **kwargs):
        self.prompts.append(kwargs["messages"][0]["content"])
        return SimpleNamespace(content=[SimpleNamespace(type="text", text=self.replies.pop(0))])


def test_fill_leaves_json_braces_alone():
    assert fill('{"a": 1} {x}', x="ok") == '{"a": 1} ok'


def test_parse_json_handles_fences_and_chatter():
    assert parse_json('Here you go:\n```json\n{"a": 1}\n```') == {"a": 1}


def test_full_chain_and_unknown_platform_filtered():
    client = FakeClient(["```json\n" + json.dumps(PROFILE) + "\n```", json.dumps(MATCHES), "# Report"])
    result = Chain(client, model="test").run("CV text here")
    assert result["report"] == "# Report"
    assert [m["platform"] for m in result["matches"]["matches"]] == ["Outlier"]
    assert "CV text here" in client.prompts[0]
    assert "Adaeze Okonkwo" in client.prompts[1]


def test_retries_on_bad_json():
    client = FakeClient(["not json", json.dumps(PROFILE), json.dumps(MATCHES), "# Report"])
    Chain(client, model="test").run("CV")
    assert "not valid JSON" in client.prompts[1]
