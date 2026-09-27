# Pairwise Preference Evaluation

Given one prompt and two responses (A and B), decide which is better and by how much, then write a justification that another reviewer could check. The same process works for text, code, images, and video.

## Process

1. **Read the prompt as the user.** List every explicit requirement and any clear implicit ones (a request for a formal letter implies no slang). This list is your checklist for both responses.
2. **Assess each response on its own first.** Go through the checklist for A, then for B, before comparing. Comparing too early anchors you on whichever you read first.
3. **Score per dimension.** Rate each response on the dimensions that apply, independently of the others.
4. **Find the deciding difference.** Usually one or two differences drive the overall call. Name them.
5. **Choose the preference strength** from how much those differences matter to the user, not from how many small differences you found.
6. **Write the justification** (format below).

## Dimensions

| Dimension | Question |
|---|---|
| **Accuracy** | Is everything stated true and correctly computed? |
| **Instruction following** | Does it do what was asked, in the form asked? |
| **Completeness** | Does it cover every part of the request? |
| **Reasoning** | Are the steps sound, and do conclusions follow from them? |
| **Clarity** | Could the intended reader use it without re-reading? |
| **Relevance** | Does it stay on the task without padding? |
| **Safety** | Does it avoid harmful, misleading, or policy-violating content? |

Correctness on its own doesn't decide a comparison. A correct answer that ignores the requested format can lose to a slightly less polished answer that does what the user needed.

## Confound checks before locking a verdict

- **Length bias.** Am I preferring the longer response because it looks thorough? Check whether the extra length adds anything the user asked for.
- **Style bias.** Am I rewarding confident tone or nice formatting over substance?
- **Order bias.** Would I reach the same verdict if B had been shown first?
- **Shared failures.** If both responses make the same mistake, it doesn't separate them. Note it, but don't let it drive the preference.
- **My own uncertainty.** If the call depends on a fact I haven't verified (a count, a date, a line of code's behaviour), verify it or say it's unverified.

## Preference strength

| Strength | When to use it |
|---|---|
| **Much better** | One response fails a critical requirement or contains a material error the other avoids. |
| **Better** | Both are usable, but one handles a meaningful requirement clearly better. |
| **Slightly better** | Differences are real but minor: tone, small omissions, formatting. |
| **About the same** | Differences cancel out or don't matter to the user. |

## Writing the justification

Verdict first, then the least evidence that fully supports it. Every claim points to something in a response.

**Structure:** verdict → the deciding difference(s) with specifics → any secondary differences → shared issues (briefly).

**Weak**
> Response A is better because it is more accurate and complete. Response B has some issues.

**Strong**
> A is better. The user asked for the monthly payment on a ₦2,000,000 loan at 24% annual interest over 12 months. A computes it with the amortisation formula and gets about ₦189,100, which is correct. B adds a full year of flat interest to the principal and divides by 12, getting ₦206,667, which overstates the payment by about 9%. Both explain their steps clearly, and B's table is better formatted, but its core number is wrong.

The strong version names the task, quotes the numbers, says which is right, and explains why the formatting advantage doesn't change the call.

## Common mistakes

- Justifying with adjectives ("more helpful", "higher quality") instead of evidence.
- Letting a minor issue decide a comparison when a major one exists.
- Describing a response's content without saying why it matters.
- Mixing up which response did what. Re-check labels before submitting.
