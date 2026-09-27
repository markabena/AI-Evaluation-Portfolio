You are extracting a structured profile from a job seeker's CV. The profile will be used to match them to AI training and data annotation work, so accuracy matters more than completeness: record only what the CV states.

<cv>
{cv_text}
</cv>

Return a single JSON object that follows this schema exactly:

{schema}

Rules:
- Copy facts from the CV. Do not infer degrees, languages, or skills that aren't written down.
- If a field isn't supported by the CV, use null (for single values) or an empty list.
- `highest_degree.level` must be one of: "none", "secondary", "diploma", "bachelors", "masters", "doctorate", "professional".
- `domains` lists fields where the person has formal study or at least one year of work. For each, give the evidence from the CV in a short phrase.
- `languages` includes only languages the CV states. Use the proficiency word the CV uses; if none is given, use "unspecified".
- `writing_evidence` lists concrete signs of strong writing (publications, technical reports, editing roles). Leave it empty if there are none.
- `red_flags` lists anything that would weaken an application: unexplained gaps over 12 months, inconsistent dates, missing contact details. Keep it factual.

Return only the JSON object, with no text before or after it.
