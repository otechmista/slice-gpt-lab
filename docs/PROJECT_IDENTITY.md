# Slice GPT Lab

Slice GPT Lab is a teaching project. Its purpose is to show anyone — especially people new to AI — how a GPT-style language model works from the inside.

It uses a fictional pizzeria called **The Slice Lab** to keep everything concrete and fun. Every step of the model is exposed in plain, readable code: how text becomes numbers, how the model learns, how it generates answers one character at a time.

This is not a product. It is a classroom.

## Who This Is For

Anyone curious about how AI language models work. No machine learning background required — just curiosity and willingness to run some Python.

If you've ever wondered "how does ChatGPT actually produce text?", this project shows you the real mechanics at a scale small enough to understand completely.

## What You'll Be Able to Explain After This

- How text becomes token IDs
- How token IDs become vectors (embeddings)
- How the model knows word order (positional embeddings)
- How attention connects each token to earlier tokens
- How logits become a single predicted character
- How loss measures prediction error
- How backpropagation updates every weight
- How a checkpoint saves learned parameters
- How inference generates text one character at a time
- How a local model becomes a web API

## Project Name

```txt
Slice GPT Lab
```

Repository name:

```txt
slice-gpt-lab
```

API model identifier (used by tests and examples):

```txt
slice-gpt-lab
```

Only rename the model identifier when intentionally changing the API contract.

## Recommended Study Order

1. Read [00_course_guide.md](00_course_guide.md) — commands and study path
2. Read [01_introduction.md](01_introduction.md) — what we're building
3. Read [02_how_llms_work.md](02_how_llms_work.md) — the big picture
4. Read [15_simple_context_model.md](15_simple_context_model.md) — chat → tokens
5. Follow lessons [03](03_tokenization.md) through [13](13_limitations_of_the_model.md)
6. Read [14_file_by_file_lessons.md](14_file_by_file_lessons.md) — code walkthrough
7. Use [diagrams/README.md](diagrams/README.md) for visual maps
8. Read the architecture views in [contexts/](contexts/) before changing anything structural
9. Open the files in `app/`, run the tests, train the model

## Concept Lessons

| File | Topic |
|---|---|
| [01_introduction.md](01_introduction.md) | What we're building and why |
| [02_how_llms_work.md](02_how_llms_work.md) | The full GPT-like pipeline |
| [03_tokenization.md](03_tokenization.md) | Text → token IDs |
| [04_embeddings.md](04_embeddings.md) | Token IDs → vectors |
| [05_self_attention.md](05_self_attention.md) | How tokens read each other |
| [06_transformer_blocks.md](06_transformer_blocks.md) | Attention + feed-forward |
| [07_forward_pass.md](07_forward_pass.md) | Input → logits |
| [08_loss_and_backpropagation.md](08_loss_and_backpropagation.md) | Measuring and learning from error |
| [09_training_loop.md](09_training_loop.md) | The learning loop |
| [10_inference.md](10_inference.md) | Generating text |
| [11_checkpoint_and_weights.md](11_checkpoint_and_weights.md) | Saving what was learned |
| [12_openai_api_layer.md](12_openai_api_layer.md) | The web API |
| [13_limitations_of_the_model.md](13_limitations_of_the_model.md) | Why this isn't ChatGPT |
| [14_file_by_file_lessons.md](14_file_by_file_lessons.md) | Every file explained |
| [15_simple_context_model.md](15_simple_context_model.md) | Chat → context → tokens |

## Guiding Principle

Every file in this project should help you answer one question:

> What is this piece doing in a GPT-style system?

<!-- COURSE_THREAD_START -->
## Course Thread

Previous: this is the entry point for the study path.

Next: [Course Guide](00_course_guide.md) turns that promise into a study route.

<!-- COURSE_THREAD_END -->
