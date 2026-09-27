# Defect Log Template

One row per distinct defect. A defect that can't be located, described as a specific fact, and tied to one of the five families doesn't go in the log.

## Template

| # | Location | Family | Description (one factual sentence) | Severity |
|---|---|---|---|---|
| 1 | | | | |

**Location.** The exact spot: "extra finger between ring and little finger, left hand", not "the hand". For something missing from the image, point to the part of the prompt it failed ("prompt: 'exactly five items'").

**Family.** Instruction following, symbols/text, factuality, plausibility, or aesthetics.

**Description.** A statement of fact, not a question or a mood. Name what's wrong and, where it helps, what it should be.

**Severity.**
- *High:* obvious within a couple of seconds. Keep this for the few most damaging defects.
- *Medium:* unmistakable once noticed, but not the first thing you see.
- *Low:* subtle; only reads as a defect alongside others.

## Example (illustrative output for prompt 2 in the stress-prompt set)

| # | Location | Family | Description | Severity |
|---|---|---|---|---|
| 1 | Prompt: "exactly five items" | Instruction following | The board lists four items; "Banana ₦800" is missing. | High |
| 2 | Board, line 2 | Symbols/text | "Pawpaw" is rendered as "Pawaw". | Medium |
| 3 | Board, line 3, currency sign | Symbols/text | The naira sign is drawn as a plain N with no strokes. | Medium |
| 4 | Seller's right hand | Plausibility | The index and middle fingers merge into one digit from the second knuckle. | High |
| 5 | Seller's right hand, pointing direction | Instruction following | The finger points at the mango line, not the pineapple line. | Medium |
| 6 | Whole image | Aesthetics | Chalk strokes have an identical texture on every letter, like a font, not hand-written chalk. | Low |

## Common mistakes

- Logging something the prompt asked for (worn paint, blur, an unusual colour) as a defect.
- Splitting one uncertain observation into several rows to raise the count.
- Copying the same description onto two different locations.
- Putting whole-image qualities (overall grain, general blur) on a specific point instead of an overall note.
- Treating an extra, unflawed object as a defect just because the prompt didn't mention it.
