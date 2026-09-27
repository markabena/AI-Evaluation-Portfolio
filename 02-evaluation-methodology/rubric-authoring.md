# Rubric Authoring

A rubric turns "is this response good?" into a list of yes/no checks that two graders would score the same way. Most rubric problems come from criteria that bundle several checks together, or that describe a process instead of a result.

## Workflow

1. **Build the golden answer first**, by hand, from the prompt and the input files. Take notes as you go: every decision you make while building it ("used the footnote limit for the variant", "excluded two aircraft in heavy check") is a candidate criterion.
2. **Draft criteria from those notes**, not from a model's response. Criteria written after reading model output drift toward describing what that model did.
3. **Make each criterion atomic, verifiable, and specific** (tests below).
4. **Weight criteria** by how much a professional would care if it were wrong.
5. **Add a few penalty criteria** for serious errors that positive criteria won't catch (fabricated figures, unsafe advice, ignoring an explicit exclusion).
6. **Grade the golden answer against the rubric.** It should score full marks. If it doesn't, the rubric is wrong.
7. **Grade real responses.** Give credit only for what's explicitly present, not for what's implied or nearly there.

## The four tests for a criterion

| Test | Question to ask | Fails when |
|---|---|---|
| **Atomic** | Does it check exactly one thing? | "States the top three aircraft and their margins and the data date" is three criteria. |
| **Verifiable** | Can a grader check it without judgment calls? | "Provides a thorough analysis" can't be checked. |
| **Stated as an outcome** | Does it describe what the answer contains? | "Considers the footnote in the manual" describes a process. "Uses a limit of 0.25 in for the -300 variant" describes a result. |
| **Self-contained** | Can a grader score it without re-deriving the answer? | "Correct margin for aircraft 5N-ABC" forces the grader to recompute. "States the margin for 5N-ABC as 18% (±1 pt)" doesn't. |

## Weighting

A simple three-level scale is enough in most cases.

| Weight | Use for |
|---|---|
| **Critical (5)** | The core answer. If this is wrong, the deliverable is unusable. |
| **Major (3)** | A key supporting fact, calculation, or constraint. |
| **Minor (1)** | Format, labelling, and presentation requirements stated in the prompt. |
| **Penalty (−3 to −5)** | Fabricated data, violating an explicit constraint, unsafe content. |

## Worked example

For the brake-wear task in [`../01-adversarial-prompt-design/llm-professional-task-design.md`](../01-adversarial-prompt-design/llm-professional-task-design.md), with invented values for illustration:

| # | Criterion | Weight |
|---|---|---|
| 1 | Names 5N-ABC as the aircraft with the lowest remaining wear margin. | 5 |
| 2 | Names 5N-ABF as the second-lowest margin. | 5 |
| 3 | Names 5N-ABK as the third-lowest margin. | 5 |
| 4 | States 5N-ABC's margin as 12% (±1 pt). | 3 |
| 5 | Computes each aircraft's margin from its worst wheel position, not an average across positions. | 3 |
| 6 | Uses the 0.25 in limit for -300 variant aircraft. | 3 |
| 7 | Excludes 5N-ABD and 5N-ABH, which are in heavy check. | 3 |
| 8 | States the data date as 12 May 2025. | 1 |
| 9 | Delivers a memo of one page or less. | 1 |
| 10 | Names the file `brake_wear_memo.docx`. | 1 |
| P1 | Recommends an aircraft that is in heavy check. | −5 |
| P2 | Quotes a wear reading that does not appear in the log. | −5 |

Criterion 5 is the only one that looks like a process, and it's there on purpose: averaging across positions can accidentally land on the right top three, and the rubric should still separate that from correct reasoning. It's still scored from what the memo shows.

## Common rubric failures

- **Stacked criteria.** The single most common problem. Split them.
- **Instructions instead of answers.** "Checks the Status column" should be "Excludes 5N-ABD and 5N-ABH."
- **Too few criteria.** A rubric with five items can't tell a good response from a lucky one.
- **Criteria copied from the prompt.** "Writes a memo" restates the task; it doesn't test the answer.
- **Rewarding length.** More words is not more correct.
