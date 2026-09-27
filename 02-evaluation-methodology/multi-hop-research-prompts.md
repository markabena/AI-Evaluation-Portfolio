# Multi-Hop Research Prompts

A multi-hop prompt can only be answered by finding one fact, using it to find the next, and so on. These prompts test whether a model with web search can plan a chain of lookups, rather than whether it has memorised a single answer.

## What makes a good one

| Property | Test |
|---|---|
| **Genuinely chained** | Each hop depends on the answer to the one before. If you can skip a hop by searching the final answer directly, the chain is broken. |
| **One verifiable answer** | Exactly one correct answer, checkable against a reliable source. No "it depends". |
| **Timeless** | The answer won't change next year. Avoid "current CEO", "latest version", "most recent". Anchor to fixed events. |
| **Not guessable** | A plausible guess shouldn't land on the answer by luck. Avoid yes/no and small multiple-choice sets. |
| **Fair** | Every hop is findable on the open web without paywalls, logins, or obscure archives. |
| **Unambiguous wording** | Each clue points to exactly one entity. "A British airline in the 1950s" matches many; "the airline that flew the first scheduled jet passenger service" matches one. |

## Build process

1. **Start from the answer and work backwards.** Pick a fixed fact and then describe it through a related entity, and that entity through another.
2. **Write each hop as a clue that identifies one thing.** Check that each clue on its own is unambiguous.
3. **Check for shortcuts.** Search for the final question directly. If the answer shows up in the first few results, add a hop or change the clues.
4. **Source every hop.** Record a source for each link in the chain before finalising.
5. **Test for drift.** Ask whether any hop could change (a renamed company, a record that could be broken). If so, anchor it to a date.

## Worked example (original)

**Prompt**

> The airline that operated the world's first scheduled passenger service with a jet airliner later merged with another state-owned carrier from the same country to form a new national airline. What was the full name of that other carrier?

**Chain**

| Hop | Question it resolves | Answer |
|---|---|---|
| 1 | Which jet airliner flew the first scheduled jet passenger service? | The de Havilland DH.106 Comet, on 2 May 1952 (London to Johannesburg). |
| 2 | Which airline operated that service? | British Overseas Airways Corporation (BOAC). |
| 3 | Which carrier did BOAC merge with, and into what? | British European Airways (BEA), forming British Airways in 1974. |

**Answer:** British European Airways.

**Why it works:** each hop is a fixed historical fact, so the answer won't drift. The answer is a specific name, not guessable from a short list. Searching the final question directly tends to surface British Airways itself, which is the wrong answer, so the model has to actually work the chain.

**Sources:** [de Havilland Comet (Wikipedia)](https://en.wikipedia.org/wiki/De_Havilland_Comet), [This Day in Aviation: 2 May 1952](https://www.thisdayinaviation.com/2-1952/), [History of British Airways (Wikipedia)](https://en.wikipedia.org/wiki/History_of_British_Airways).

## Common mistakes

- **Parallel, not chained.** "Name the capital of X and the river through Y" is two lookups, not a chain.
- **Answer depends on the date.** Anything with "currently" or "as of today" will go stale.
- **Ambiguous middle hop.** If hop 2 has two reasonable answers, the chain forks and the final answer is contested.
- **Unsourced hops.** If you can't point to where a hop is confirmed, you can't grade the model on it.
