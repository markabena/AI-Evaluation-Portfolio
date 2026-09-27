# Adversarial Prompt Design

An adversarial prompt is only useful if the failure it produces is real, specific, and checkable. A prompt that makes the model fail because the prompt itself is vague, contradictory, or impossible tells you nothing about the model. Most of the craft is in avoiding that trap.

## Core principles

**1. Stack concrete requirements.** "A cat" gives a model nothing to get wrong. "A grey tabby asleep under a wooden chair, to the left of a brass floor lamp, with a paperback lying open face-down beside it" gives it five or six independent chances to fail, and each one is easy to check.

**2. Target known weak spots, then combine them.** Every generator and every LLM has predictable failure families (see the taxonomy below). One weak spot per prompt produces a coin-flip. Three or four, chosen so they interact, produce failures reliably.

**3. The failure has to be the model's fault.** Before keeping a failed output, ask: would a competent human, reading this prompt cold, know exactly what was wanted? If not, fix the prompt, not the verdict.

**4. Never ask for the failure directly.** "A hand with six fingers" is a request, not a test. The model complying with it proves nothing. You want the model to fail while trying to succeed.

**5. Realistic beats clever.** Prompts that read like real requests (a product photo brief, an analyst's memo, a client email) expose failures that matter in deployment. Puzzle-style prompts expose failures nobody cares about.

**6. If the output comes back clean, harden the prompt.** Never pad a critique with invented defects to justify the attempt. Rewrite denser and try again.

## Failure taxonomy

I sort failures into five families. The category matters less than catching the defect, but working through the families in order keeps coverage honest.

| Family | What breaks | Typical triggers |
|---|---|---|
| **Instruction following** | Something asked for is missing, wrong, or miscounted | Exact counts, left/right and above/below relations, named attributes (colours, materials), specified style or medium |
| **Symbols and text** | Letters, numbers, logos, and diagrams render wrong | Signs, receipts, labels, chalkboards, chart axes, clock faces, keyboard legends |
| **Factuality** | A real-world referent is rendered with the wrong content | Flags, maps, well-known instruments, chart values that should sum, a clock that should show a stated time |
| **Plausibility** | Physics, anatomy, or scene logic a layperson would catch | Hands gripping small objects, reflections, shadows against a stated light source, objects resting on or passing through others |
| **Aesthetics** | Nothing technically broken, but off | Uncanny faces, mismatched lighting across a scene, muddy colour, repeated texture tiles |

For LLM tasks the same idea applies with different families: **extraction** (hallucinated, omitted, or misread facts), **reasoning** (dropped dependencies, ignored constraints, wrong inferences), and **delivery** (right answer in the wrong format, structure, or level of detail).

## Review order for a generated output

Big structural failures first, micro-defects last. Starting with a zoomed-in hunt for tiny glitches is the most common way to miss an obvious broken hand.

1. Re-read the prompt and check every explicit ask against the output.
2. Scene logic: gravity, lighting direction, reflections, architecture.
3. Object integrity: anatomy, fused or merged objects, floating items.
4. Information integrity: text, numbers, real-world references.
5. Micro-defects at high zoom.

Before logging anything, check it against the prompt. If you asked for worn paint or a blurred background, it isn't a defect.

## Files in this folder

- [`text-to-image-stress-prompts.md`](text-to-image-stress-prompts.md): ten original prompts, each annotated with the failure families it targets and what to check.
- [`llm-professional-task-design.md`](llm-professional-task-design.md): designing hard, realistic tasks for LLMs, with two worked examples.
- [`defect-log-template.md`](defect-log-template.md): the template I use to record defects so each one is specific, located, and rated.
