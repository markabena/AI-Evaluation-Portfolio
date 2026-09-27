# Designing Hard, Realistic Tasks for LLMs

The goal is a task a capable professional could complete in a few hours with the files provided, where a strong model still gets something material wrong. "Material" means a professional would refuse to ship the output over it.

## What every task needs

| Attribute | What it means in practice |
|---|---|
| **Unambiguous** | Any failure is the model's, not the prompt's. If two careful readers could disagree on what was asked, rewrite. |
| **Professional framing** | A named role, an audience, and stakes. "You're the reliability engineer preparing a note for the fleet manager before Monday's planning meeting." |
| **Realistic** | Reads like a real email, ticket, or brief. No riddles, no roleplay flourishes. |
| **Fixed in time** | If a date matters, state it. Never rely on the model knowing today's date. |
| **Clear deliverable** | Format, file name, length, and the quality bar are spelled out. |
| **Explicit constraints** | The must-nots are written down. If the model is going to be marked down for an assumption, the prompt has to rule that assumption out first. |

## Sources of difficulty

A task gets hard by using at least two of these, not by piling on length.

- **Volume and noise.** The files contain far more than is needed; the model has to find the relevant subset.
- **Conflicting sources.** Two documents disagree, and one of them is authoritative for a stated reason (a signed revision beats a draft; a regulator's figure beats a vendor's).
- **Buried constraints.** A decisive rule sits in a footnote, an appendix, or a second tab.
- **Multi-step dependency.** A later calculation depends on an earlier correction the model has to notice.
- **Domain convention.** The correct answer follows a professional convention the prompt doesn't restate (units, rounding rules, fiscal-year boundaries). It's fair as long as the convention is standard in the field or written down in the files provided.

Things that are not difficulty: typos, contradictions nobody could resolve, trick wording, and missing information the task silently depends on.

## Checking a failure before citing it

Answer yes to all four before logging a model miss:

1. Is it objectively wrong, not a defensible judgment call?
2. Was the requirement stated in the prompt or files?
3. Did I re-open the source and confirm the correct value and where it lives?
4. Does it matter? Would a professional reject the work over it?

---

## Worked example A: Engineering (original)

**Prompt**

> You're a reliability engineer at a regional airline. The fleet manager wants a one-page memo (`brake_wear_memo.docx`) by Monday recommending which three aircraft should have brake assemblies replaced at their next A-check. Use the attached wear log (`brake_wear_log.xlsx`, tabs "Readings" and "Limits") and the maintenance manual extract (`MM_32-42_extract.pdf`). Rank all aircraft by remaining wear margin as a percentage of the allowable limit, list the top three with their margin, and state the data date you used. Do not include aircraft currently in heavy check (see the "Status" column). Readings are dated; use only the most recent reading per wheel position.

**Built-in difficulty**

- *Volume:* 14 aircraft × 4 wheel positions × 6 months of readings; only the latest reading per position counts.
- *Buried constraint:* the "Limits" tab gives the wear-pin limit in inches; one aircraft variant has a different limit listed only in a footnote of the manual extract.
- *Dependency:* two aircraft are marked "HEAVY CHECK" in the Status column and must be excluded before ranking. Excluding them changes the third place.
- *Convention:* the manual extract defines margin per wheel position and treats the aircraft's margin as its worst position, not its average. The prompt doesn't repeat this; the model has to read it from the source.

**Where models tend to fail:** averaging positions instead of taking the worst one; applying the common limit to the variant; ranking before excluding heavy-check aircraft; using an older reading.

## Worked example B: Finance (original)

**Prompt**

> You're an analyst at a small logistics company. Prepare a reconciliation (`q2_fuel_recon.xlsx`) of fuel card spend against the general ledger for April to June. Inputs: the card provider's statement export (`card_export.csv`), the ledger extract (`gl_fuel.xlsx`), and the finance team's policy note (`expense_policy_2025.pdf`). Show matched items, unmatched items on each side, and the net difference. Where the card export and ledger disagree on an amount, the card export is authoritative. Use formulas rather than hard-coded values for all totals.

**Built-in difficulty**

- *Conflicting sources:* six transactions differ by small amounts between the two files; the prompt states which source wins.
- *Buried constraint:* the policy note says transactions posted within three days after month-end belong to the prior month. Four June transactions posted on 2 and 3 July must be pulled in.
- *Delivery:* totals must be live formulas. A correct number typed in as a constant is still a failure.

**Where models tend to fail:** missing the posting-date rule; averaging disputed amounts instead of taking the card figure; hard-coding totals.

---

Both examples come with a golden (reference) answer built by hand from the files before any model is run. The rubric is written from that golden answer, not from the model's output. See [`../02-evaluation-methodology/rubric-authoring.md`](../02-evaluation-methodology/rubric-authoring.md).
