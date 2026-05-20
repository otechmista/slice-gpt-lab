# Slice GPT Lab: Documentation

This is a teaching project. Its goal is to show how a GPT-style language model works — step by step, in real code you can read and run.

## What Is This Project?

**Slice GPT Lab** is a tiny AI trained to answer questions about a fictional pizzeria called The Slice Lab.

But the pizzeria is just a prop. The real subject is the model itself: how it reads text, learns from it, and generates answers one character at a time. Every step — tokenization, attention, loss, training, inference — is visible in small, readable files.

This project teaches the core mechanics of language models like ChatGPT, at a scale small enough to understand completely.

## Who This Is For

Anyone who wants to understand how AI language models work from the inside. You don't need a machine learning background — just curiosity and Python installed.

## The Core Idea

The model learns one skill, repeated thousands of times:

> Given the previous characters, predict the next character.

That same idea powers every GPT-style model. Here it's small enough to see clearly.

## Course Site

```txt
https://otechmista.github.io/mini-gpt-study/
```

## Where to Start

```txt
PROJECT_IDENTITY.md   ← what this project is and what you'll learn
00_course_guide.md    ← commands and study path
```

## The Lesson Path

| Step | Document | What You'll Learn |
|---|---|---|
| 1 | [PROJECT_IDENTITY.md](PROJECT_IDENTITY.md) | What this project teaches and who it's for |
| 2 | [00_course_guide.md](00_course_guide.md) | Commands and study order |
| 3 | [01_introduction.md](01_introduction.md) | What we're building and why |
| 4 | [02_how_llms_work.md](02_how_llms_work.md) | The full GPT-like pipeline |
| 5 | [15_simple_context_model.md](15_simple_context_model.md) | How a conversation becomes model input |
| 6 | [03_tokenization.md](03_tokenization.md) | How text becomes numbers |
| 7 | [04_embeddings.md](04_embeddings.md) | How numbers become vectors |
| 8 | [05_self_attention.md](05_self_attention.md) | How tokens read previous context |
| 9 | [06_transformer_blocks.md](06_transformer_blocks.md) | Attention + feed-forward together |
| 10 | [07_forward_pass.md](07_forward_pass.md) | How the model produces predictions |
| 11 | [08_loss_and_backpropagation.md](08_loss_and_backpropagation.md) | How the model learns from mistakes |
| 12 | [09_training_loop.md](09_training_loop.md) | The complete training process |
| 13 | [11_checkpoint_and_weights.md](11_checkpoint_and_weights.md) | How trained knowledge is saved |
| 14 | [10_inference.md](10_inference.md) | How the model generates answers |
| 15 | [12_openai_api_layer.md](12_openai_api_layer.md) | The web API |
| 16 | [13_limitations_of_the_model.md](13_limitations_of_the_model.md) | Why this isn't ChatGPT — and what that means |
| 17 | [14_file_by_file_lessons.md](14_file_by_file_lessons.md) | Every source file explained |

## Visual Diagrams

```txt
diagrams/README.md
```

## Architecture Views

For deeper context on design decisions:

```txt
contexts/
  01_CONTEXT_VIEW.md    ← problem, goals, and boundaries
  02_CONTAINER_VIEW.md  ← runtime components
  03_COMPONENT_VIEW.md  ← internal structure
  04_CODE_VIEW.md       ← contracts and rules
```
