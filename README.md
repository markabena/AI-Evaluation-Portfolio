# AI Evaluation Portfolio

Working methods and original examples from my work as an AI data annotator and model evaluator: adversarial prompt design, rubric authoring, preference evaluation, and a small prompt-chain tool.

I'm an aerospace engineering graduate (B.Eng, AFIT Kaduna) who now spends most of my working hours stress-testing generative models: writing prompts meant to make them fail, grading their outputs against rubrics, and writing the justifications that go with each call. This repo is where I keep the reusable parts of that work in a form I can share.

## What's here

| Folder | What it covers |
|---|---|
| [`01-adversarial-prompt-design/`](01-adversarial-prompt-design/) | How I design prompts that expose real model failures, for image generators and for LLMs working on professional tasks. Includes a failure taxonomy, original example prompts, and a defect-logging template. |
| [`02-evaluation-methodology/`](02-evaluation-methodology/) | Rubric authoring, pairwise preference evaluation, justification writing, and multi-hop research prompt design, each with worked examples. |
| [`03-cv-platform-matching-workflow/`](03-cv-platform-matching-workflow/) | A three-stage prompt chain (CV extraction → platform matching → advisory report) with a Python runner, JSON schema, and a fictional end-to-end example. |

## Related repo

**[prompt-engineering-workspace](https://github.com/markabena/prompt-engineering-workspace)**: my working lab. Prompt library entries with failure analysis, reusable templates, monthly mock assessments, and Anthropic SDK scripts.

## A note on confidentiality

Everything in this repo is my own writing. It contains no client guidelines, project names, task data, rubrics, or model outputs from any annotation platform I've worked on. The examples are original and built for this portfolio; the methods are general practice in the field, described in my own words.

## Skills this demonstrates

- Adversarial prompt design for text-to-image and LLM systems
- Rubric design: atomic, verifiable, weighted criteria with penalty items
- Pairwise preference evaluation and written justification
- Multi-hop research question design with verifiable answers
- Prompt chaining with structured (JSON) intermediate outputs
- Technical writing for annotator-facing documentation

## Contact

Mark Abena · Kaduna, Nigeria · [github.com/markabena](https://github.com/markabena)

## License

Code is released under the MIT License. Written material is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). See [LICENSE](LICENSE).
