Write a short advisory report for a job seeker, based on the matching results below. The reader is the candidate. They want to know where to apply first and what to fix on their CV.

<candidate_profile>
{profile_json}
</candidate_profile>

<match_results>
{matches_json}
</match_results>

Structure (Markdown, under 700 words):

1. **Summary** (2–3 sentences): the candidate's strongest angle for AI training work and the one platform to apply to first.
2. **Recommended platforms**: a table with Platform, Fit, Role to apply for, and Why (one line citing their background). Include only "strong" and "possible" matches, best first.
3. **Before you apply**: the three most useful CV changes, each tied to a platform it helps with.
4. **Things to confirm**: anything in `unknowns` the candidate should check on the platform's site (location rules, degree requirements).
5. **Next steps**: a numbered list of no more than five actions.

Rules:
- Write plainly and directly. No filler, no hype, no promises about acceptance or earnings.
- Don't state pay rates or acceptance odds.
- Don't mention platforms rated "weak" except, if useful, one line on what would change that.
- Every claim about the candidate must come from the profile.
- Remind the reader in one line at the end that platform requirements change and they should check each site before applying.
