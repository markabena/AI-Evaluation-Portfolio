# Evaluation Methodology

How I grade model outputs and design the questions and rubrics used to grade them.

| File | What it covers |
|---|---|
| [`rubric-authoring.md`](rubric-authoring.md) | Writing atomic, verifiable, weighted rubric criteria from a hand-built golden answer, with a worked 12-item rubric. |
| [`pairwise-preference-evaluation.md`](pairwise-preference-evaluation.md) | Comparing two responses: per-dimension scoring, bias checks, preference strength, and justification writing with a weak/strong example. |
| [`multi-hop-research-prompts.md`](multi-hop-research-prompts.md) | Designing chained research questions with one timeless, verifiable answer, with a sourced three-hop example. |

## Principles that run through all of it

- **Verdict first, then evidence.** State the call, then the minimum specific evidence that supports it.
- **Correctness alone doesn't settle a verdict.** A right answer delivered in the wrong form, or with unsupported reasoning, still loses points.
- **Never assert what you haven't checked.** If a call depends on a count, a date, or a value, verify it or flag it.
- **Score what's there.** No credit for implied or nearly-correct answers.
- **Fix the prompt, not the verdict.** If a failure comes from an unclear prompt, the prompt is the problem.
