You are matching a candidate to AI training and annotation platforms. Use only the candidate profile and the platform catalogue below.

<candidate_profile>
{profile_json}
</candidate_profile>

<platform_catalogue>
{catalogue_yaml}
</platform_catalogue>

For each platform in the catalogue, decide how well the candidate fits:

- "strong": the candidate clearly meets the platform's stated requirements and has a domain or skill the platform looks for.
- "possible": the candidate meets the basic requirements but lacks a clear advantage, or one requirement is uncertain.
- "weak": the candidate is missing a stated requirement.

Rules:
- Base every decision on specific profile fields. Quote the field and value in `evidence`.
- Where a requirement can't be confirmed from the profile, say so in `unknowns` rather than assuming.
- Respect `regions_note` in the catalogue: if a platform restricts location and the candidate's location is outside it or unknown, say so.
- Always return at least one "strong" or "possible" option from the entry tier, so the candidate has a fallback.
- Rank the final list with the best overall fit first.

Return a single JSON object:

{
  "matches": [
    {
      "platform": "<name from catalogue>",
      "tier": "<tier from catalogue>",
      "fit": "strong | possible | weak",
      "evidence": ["<profile field>: <value> -> <why it matters>"],
      "unknowns": ["<requirement that couldn't be confirmed>"],
      "suggested_roles": ["<role type from the catalogue>"]
    }
  ],
  "cv_improvements": ["<specific change that would raise fit, tied to a platform>"]
}

Return only the JSON object.
